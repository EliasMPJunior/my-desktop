window.infoBimProjectRuntimeData = window.infoBimProjectRuntimeData || {};

(function () {
  "use strict";

  const runtimeData = window.infoBimProjectRuntimeData;

  // Projeção estática desta visualização dos valores mantidos no project.ttl
  // e do caminho absoluto exigido exclusivamente pelo card Project Information.
  const projectProjection = {
    absolutePath: "C:\\Users\\EliasMagalhães\\Documents\\Brasidata\\06_Projetos\\01_Projetos_Ativos\\my-desktop\\techcenter-doc",
    location: {
      latitude: -22.868585,
      longitude: -43.214664,
    },
  };

  function validLocation(value) {
    if (!value || typeof value !== "object") {
      return false;
    }

    const latitude = Number(value.latitude);
    const longitude = Number(value.longitude);
    return Number.isFinite(latitude)
      && Number.isFinite(longitude)
      && latitude >= -90
      && latitude <= 90
      && longitude >= -180
      && longitude <= 180;
  }

  if (!validLocation(runtimeData.location)) {
    runtimeData.location = projectProjection.location;
  }

  if (!String(runtimeData.absolutePath || "").trim()) {
    runtimeData.absolutePath = projectProjection.absolutePath;
  }

  const card = document.querySelector('[data-card="project-information-card"]');

  function metadataList() {
    return card ? card.querySelector(".metadata-list") : null;
  }

  function normalizedLabel(row) {
    const term = row ? row.querySelector("dt") : null;
    return term
      ? term.textContent.trim().toLocaleLowerCase("pt-BR")
      : "";
  }

  function metadataRowsByLabel(label) {
    if (!card) {
      return [];
    }

    const expected = label.toLocaleLowerCase("pt-BR");
    return Array.from(card.querySelectorAll(".metadata-row")).filter(
      (row) => normalizedLabel(row) === expected,
    );
  }

  function metadataRowByLabel(label) {
    return metadataRowsByLabel(label)[0] || null;
  }

  function localAbsolutePath() {
    if (window.location.protocol !== "file:") {
      return "";
    }

    let pathname = decodeURIComponent(window.location.pathname || "");
    pathname = pathname.replace(/\/index\.html?$/i, "");

    if (/^\/[A-Za-z]:\//.test(pathname)) {
      pathname = pathname.slice(1);
    }

    if (/^[A-Za-z]:\//.test(pathname)) {
      return pathname.replace(/\//g, "\\");
    }

    return pathname || "/";
  }

  function dashboardAbsolutePath() {
    const dashboard = window.infoBimProjectDashboard || {};
    const value = String(dashboard.path || "").trim();
    const isWindowsAbsolute = /^[A-Za-z]:[\\/]/.test(value);
    const isUncAbsolute = /^\\\\/.test(value);
    const isPosixAbsolute = /^\/(?!\/)/.test(value);
    return isWindowsAbsolute || isUncAbsolute || isPosixAbsolute ? value : "";
  }

  function renderAbsolutePath() {
    const row = metadataRowByLabel("Path");
    if (!row) {
      return;
    }

    const value = row.querySelector("dd");
    if (!value) {
      return;
    }

    value.textContent = localAbsolutePath()
      || String(runtimeData.absolutePath || "").trim()
      || dashboardAbsolutePath()
      || "não definido";
  }

  function ensureGeolocationStyles() {
    if (document.getElementById("project-geolocation-styles")) {
      return;
    }

    const style = document.createElement("style");
    style.id = "project-geolocation-styles";
    style.textContent = `
      .project-geolocation-value {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        max-width: 100%;
      }

      .project-geolocation-coordinates {
        overflow-wrap: anywhere;
        font-variant-numeric: tabular-nums;
      }

      .project-map-pin {
        display: inline-grid;
        place-items: center;
        flex: 0 0 auto;
        width: 32px;
        height: 32px;
        border: 1px solid rgba(103, 232, 249, 0.34);
        border-radius: 999px;
        color: inherit;
        background: rgba(103, 232, 249, 0.08);
        text-decoration: none;
        line-height: 1;
      }

      .project-map-pin:hover {
        border-color: var(--accent);
        background: rgba(103, 232, 249, 0.14);
      }

      .project-map-pin:focus-visible {
        outline: 2px solid var(--accent-strong);
        outline-offset: 2px;
      }
    `;
    document.head.appendChild(style);
  }

  function ensureGeolocationRow() {
    const list = metadataList();
    if (!list) {
      return null;
    }

    const geolocationRows = metadataRowsByLabel("Geolocalização");
    let row = geolocationRows.shift() || null;
    geolocationRows.forEach((duplicate) => duplicate.remove());

    if (!row) {
      row = document.createElement("div");
      row.className = "metadata-row";
      row.dataset.projectGeolocationRow = "";

      const term = document.createElement("dt");
      term.textContent = "Geolocalização";
      const description = document.createElement("dd");
      description.className = "project-geolocation-value";

      row.append(term, description);
    }

    const nameRow = metadataRowByLabel("Name");
    if (nameRow) {
      nameRow.insertAdjacentElement("afterend", row);
    } else if (!row.isConnected) {
      list.prepend(row);
    }

    return row;
  }

  function renderGeolocation() {
    const row = ensureGeolocationRow();
    if (!row) {
      return;
    }

    const value = row.querySelector("dd");
    if (!value) {
      return;
    }

    value.textContent = "";
    value.classList.add("project-geolocation-value");

    if (!validLocation(runtimeData.location)) {
      value.textContent = "não definida";
      return;
    }

    const latitude = Number(runtimeData.location.latitude);
    const longitude = Number(runtimeData.location.longitude);
    const mapUrl = `https://www.openstreetmap.org/?mlat=${encodeURIComponent(latitude)}&mlon=${encodeURIComponent(longitude)}#map=18/${encodeURIComponent(latitude)}/${encodeURIComponent(longitude)}`;

    ensureGeolocationStyles();

    const coordinates = document.createElement("span");
    coordinates.className = "project-geolocation-coordinates";
    coordinates.textContent = `${latitude.toFixed(6)}, ${longitude.toFixed(6)}`;

    const pin = document.createElement("a");
    pin.className = "project-map-pin";
    pin.href = mapUrl;
    pin.target = "_blank";
    pin.rel = "noopener noreferrer";
    pin.title = "Abrir localização no OpenStreetMap";
    pin.setAttribute("aria-label", "Abrir localização no OpenStreetMap");
    pin.textContent = "📍";

    value.append(coordinates, pin);
  }

  function bindMenuActions() {
    document.querySelectorAll(".menubar-item[data-action]").forEach((button) => {
      if (button.dataset.navigationBound === "true") {
        return;
      }

      button.dataset.navigationBound = "true";
      button.addEventListener("click", () => {
        const action = String(button.dataset.action || "").trim();
        if (!action) {
          return;
        }
        window.location.assign(new URL(action, document.baseURI).href);
      });
    });
  }

  renderAbsolutePath();
  renderGeolocation();
  bindMenuActions();
}());
