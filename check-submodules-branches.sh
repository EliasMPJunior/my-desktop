#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
GITMODULES_FILE="${ROOT_DIR}/.gitmodules"
OUTPUT_FILE="${SCRIPT_DIR}/submodules-latest-branches.md"
TEMP_DIR="$(mktemp -d)"
SUBMODULES_LIST="${TEMP_DIR}/submodules_list.txt"

trap 'rm -rf "${TEMP_DIR}"' EXIT

if [[ ! -f "${GITMODULES_FILE}" ]]; then
    echo "Erro: Arquivo .gitmodules não encontrado em ${GITMODULES_FILE}" >&2
    exit 1
fi

parse_gitmodules() {
    local gitmodules_file="$1"
    local output_file="$2"

    awk '
        /^\[submodule / {
            if (current_path != "" && current_url != "") {
                print current_path "\t" current_url
            }
            current_path = ""
            current_url = ""
            next
        }
        /^[[:space:]]*path[[:space:]]*=/ {
            sub(/^[[:space:]]*path[[:space:]]*=[[:space:]]*/, "")
            current_path = $0
            next
        }
        /^[[:space:]]*url[[:space:]]*=/ {
            sub(/^[[:space:]]*url[[:space:]]*=[[:space:]]*/, "")
            current_url = $0
            next
        }
        END {
            if (current_path != "" && current_url != "") {
                print current_path "\t" current_url
            }
        }
    ' "${gitmodules_file}" > "${output_file}"
}

list_remote_branches() {
    local remote_url="$1"
    git ls-remote --heads --quiet "${remote_url}" 2>/dev/null | \
        awk '{print $2}' | \
        sed 's|^refs/heads/||'
}

extract_version_number() {
    local branch_name="$1"
    local version=""

    if [[ "${branch_name}" =~ v?([0-9]+(\.[0-9]+)*) ]]; then
        version="${BASH_REMATCH[1]}"
    fi

    echo "${version}"
}

version_to_tuple() {
    local version="$1"
    local IFS='.'
    read -ra parts <<< "${version}"
    local padded=""
    local i
    for i in "${!parts[@]}"; do
        if [[ ${i} -gt 0 ]]; then
            padded+="."
        fi
        padded+="$(printf '%010d' "${parts[$i]}")"
    done
    echo "${padded}"
}

find_latest_branch() {
    local branches_file="$1"
    local latest_branch=""
    local latest_version=""
    local latest_tuple=""
    local branch
    local version
    local tuple

    while IFS= read -r branch; do
        [[ -z "${branch}" ]] && continue
        version="$(extract_version_number "${branch}")"
        if [[ -n "${version}" ]]; then
            tuple="$(version_to_tuple "${version}")"
            if [[ -z "${latest_tuple}" || "${tuple}" > "${latest_tuple}" ]]; then
                latest_tuple="${tuple}"
                latest_version="${version}"
                latest_branch="${branch}"
            fi
        fi
    done < "${branches_file}"

    echo "${latest_branch}"
}

extract_package_name_from_url() {
    local remote_url="$1"
    local repo_name=""

    repo_name="$(basename "${remote_url}" .git 2>/dev/null || true)"
    echo "${repo_name}"
}

read_package_name_from_pyproject() {
    local submodule_full_path="$1"
    local pyproject_file="${submodule_full_path}/pyproject.toml"
    local package_name=""

    if [[ -f "${pyproject_file}" ]]; then
        package_name="$(awk '
            /^name[[:space:]]*=/ {
                sub(/^name[[:space:]]*=[[:space:]]*/, "")
                gsub(/"/, "")
                gsub(/'\''/, "")
                print $0
                exit
            }
            /^\[project\]/ { in_project = 1; next }
            in_project && /^name[[:space:]]*=/ {
                sub(/^name[[:space:]]*=[[:space:]]*/, "")
                gsub(/"/, "")
                gsub(/'\''/, "")
                print $0
                exit
            }
        ' "${pyproject_file}" 2>/dev/null || true)"
    fi

    echo "${package_name}"
}

read_package_name_from_setup() {
    local submodule_full_path="$1"
    local setup_py="${submodule_full_path}/setup.py"
    local setup_cfg="${submodule_full_path}/setup.cfg"
    local package_name=""

    if [[ -f "${setup_cfg}" ]]; then
        package_name="$(awk '
            /^\[metadata\]/ { in_metadata = 1; next }
            /^\[/ { in_metadata = 0 }
            in_metadata && /^name[[:space:]]*=/ {
                sub(/^name[[:space:]]*=[[:space:]]*/, "")
                print $0
                exit
            }
        ' "${setup_cfg}" 2>/dev/null || true)"
    fi

    if [[ -z "${package_name}" && -f "${setup_py}" ]]; then
        package_name="$(grep -oE 'name[[:space:]]*=[[:space:]]*["\x27][^"\x27]+["\x27]' "${setup_py}" 2>/dev/null | \
            head -n 1 | \
            sed -E 's/name[[:space:]]*=[[:space:]]*["\x27]([^"\x27]+)["\x27]/\1/' || true)"
    fi

    echo "${package_name}"
}

determine_pypi_package_name() {
    local submodule_path="$1"
    local remote_url="$2"
    local submodule_full_path="${ROOT_DIR}/${submodule_path}"
    local package_name=""

    package_name="$(read_package_name_from_pyproject "${submodule_full_path}")"

    if [[ -z "${package_name}" ]]; then
        package_name="$(read_package_name_from_setup "${submodule_full_path}")"
    fi

    if [[ -z "${package_name}" ]]; then
        package_name="$(extract_package_name_from_url "${remote_url}")"
    fi

    echo "${package_name}"
}

fetch_pypi_version() {
    local package_name="$1"
    local pypi_url="https://pypi.org/pypi/${package_name}/json"
    local response=""
    local version=""

    response="$(curl -s --max-time 5 --connect-timeout 3 "${pypi_url}" 2>/dev/null || true)"

    if [[ -n "${response}" ]]; then
        version="$(echo "${response}" | \
            grep -oE '"version"[[:space:]]*:[[:space:]]*"[^"]+"' 2>/dev/null | \
            head -n 1 | \
            sed -E 's/"version"[[:space:]]*:[[:space:]]*"([^"]+)"/\1/' || true)"
    fi

    echo "${version}"
}

get_pypi_version_with_fallbacks() {
    local package_name="$1"
    local candidates
    local candidate
    local version=""

    if [[ -z "${package_name}" ]]; then
        echo ""
        return 0
    fi

    candidates=(
        "${package_name}"
        "${package_name//-/_}"
        "${package_name//_/-}"
    )

    for candidate in "${candidates[@]}"; do
        version="$(fetch_pypi_version "${candidate}")"
        if [[ -n "${version}" ]]; then
            echo "${version}"
            return 0
        fi
    done

    echo ""
}

main() {
    parse_gitmodules "${GITMODULES_FILE}" "${SUBMODULES_LIST}"

    echo "# Submodules - Branches Remotas Mais Recentes" > "${OUTPUT_FILE}"
    echo "" >> "${OUTPUT_FILE}"
    echo "Data de geração: $(date '+%Y-%m-%d %H:%M:%S')" >> "${OUTPUT_FILE}"
    echo "" >> "${OUTPUT_FILE}"
    echo "| Submodule Path | URL Remoto | Branch Mais Recente | Versão Branch | Versão PyPI |" >> "${OUTPUT_FILE}"
    echo "|---|---|---|---|---|" >> "${OUTPUT_FILE}"

    local submodule_path
    local remote_url
    local branches_file
    local total_branches
    local latest_branch
    local latest_version
    local pypi_package
    local pypi_version
    local pypi_display

    while IFS=$'\t' read -r submodule_path remote_url; do
        [[ -z "${submodule_path}" ]] && continue

        echo "Processando submodule: ${submodule_path}..." >&2

        if [[ -z "${remote_url}" ]]; then
            echo "| ${submodule_path} | ERRO: URL não encontrada | - | - | - |" >> "${OUTPUT_FILE}"
            continue
        fi

        branches_file="${TEMP_DIR}/${submodule_path//\//_}_branches.txt"
        if ! list_remote_branches "${remote_url}" > "${branches_file}" 2>/dev/null; then
            echo "| ${submodule_path} | ${remote_url} | ERRO: Falha ao listar branches | - | - |" >> "${OUTPUT_FILE}"
            continue
        fi

        total_branches="$(wc -l < "${branches_file}" | tr -d ' ')"
        if [[ "${total_branches}" -eq 0 ]]; then
            echo "| ${submodule_path} | ${remote_url} | Nenhuma branch remota | - | - |" >> "${OUTPUT_FILE}"
            continue
        fi

        latest_branch="$(find_latest_branch "${branches_file}")"

        latest_version=""
        if [[ -n "${latest_branch}" ]]; then
            latest_version="$(extract_version_number "${latest_branch}")"
        fi

        if [[ -z "${latest_branch}" ]]; then
            latest_branch="Nenhuma branch com versão numérica"
        fi

        pypi_package="$(determine_pypi_package_name "${submodule_path}" "${remote_url}")"
        pypi_version=""
        if [[ -n "${pypi_package}" ]]; then
            echo "  Consultando PyPI: ${pypi_package}..." >&2
            pypi_version="$(get_pypi_version_with_fallbacks "${pypi_package}")"
        fi

        if [[ -n "${pypi_version}" ]]; then
            pypi_display="${pypi_version}"
        else
            pypi_display="Não publicado / N/A"
        fi

        echo "| ${submodule_path} | ${remote_url} | ${latest_branch} | ${latest_version:- -} | ${pypi_display} |" >> "${OUTPUT_FILE}"

    done < "${SUBMODULES_LIST}"

    echo "" >&2
    echo "Relatório gerado com sucesso: ${OUTPUT_FILE}" >&2
}

main "$@"
