# Prompt para o TRAE — Pyodide não carrega na WorkStream View

Cole o texto abaixo como instrução inicial para o TRAE.

---

## Objetivo

Na página gerada `.__ontobdc__/view/work_stream/<id>.html` (ontobdc-view,
branch `v0.5`), o botão "Conectar pasta" dispara o carregamento do Pyodide
para ler a workbook do WorkStream (openpyxl) e os linksets ICDD (rdflib)
inteiramente no browser. **O Pyodide não está carregando** — o fluxo de
conexão falha antes de o usuário conseguir usar a página. Já foram feitas
3 rodadas de tentativas de conserto que NÃO resolveram o problema real
(detalhes abaixo). Preciso que você:

1. Reproduza o erro num browser real (Chrome/Edge) abrindo uma
   `work_stream_view.html` gerada de um container OntoBDC real.
2. Abra o DevTools → Console e Network **antes** de clicar em "Conectar
   pasta", e capture: (a) todo log que começa com `[work-stream-view]`
   e `[ontobdc-pyodide]`; (b) a stack trace completa de qualquer erro;
   (c) na aba Network, o status de todas as requisições para
   `cdn.jsdelivr.net` (script `pyodide.js`, `pyodide.asm.wasm`,
   `pyodide-lock.json`, pacotes `micropip`/`rdflib`/`openpyxl`).
3. Só depois de ter a evidência real, diagnostique a causa raiz e
   corrija. **Não repita conserto especulativo sem antes rodar e ver o
   erro de verdade** — isso já causou 2 rodadas de "conserto" que não
   resolveram nada (ver seção "O que já foi tentado").

## Arquitetura relevante

- O Pyodide é carregado dinamicamente via `<script>` injetado apontando
  para `https://cdn.jsdelivr.net/pyodide/v0.27.2/full/pyodide.js`
  (constante `PYODIDE_CDN_URL`), dentro da função `ensurePyodide()`.
- Depois do `loadPyodide()`, o runtime faz `instance.loadPackage("micropip")`,
  depois `micropip.install('rdflib')`, e sob demanda
  `micropip.install('openpyxl')`.
- Todo esse código vive em **ontobdc-view**, arquivo
  `src/ontobdc_view/page/adapter/work_stream_script.py`, método
  `_pyodide_runtime_source()` (a partir da linha ~875). Esse método
  devolve uma string Python (`r"""..."""`) contendo o JS inteiro do
  arquivo `pyodide_runtime.js`, incluindo três blocos de Python "cru"
  embutidos dentro de template literals JS (crases): `WORKBOOK_PARSE_SCRIPT`,
  e nos métodos irmãos `_linkset_operations_source()` (`LINKSET_PYTHON_SCRIPT`)
  e `_file_category_source()` (`FILE_DISPLAY_PARSE_SCRIPT`).
- Esse `.py` é só o **gerador**. O JS de fato só existe depois que o
  pipeline de build (ontobdc-wip) roda e grava os 10 arquivos `.js` em
  `.__ontobdc__/asset/work_stream_view/` dentro do container publicado.
  A página `work_stream_view.html.j2` carrega os 10 via
  `<script defer src="../../asset/work_stream_view/<nome>.js">`.
- No lado ontobdc-wip (branch `v0.18`), o statechart que gera esses 10
  arquivos é `WorkStreamScriptGenerationProcessState`
  (`src/ontobdc/view/domain/machine/work_stream_script_state.py` +
  `standard_work_stream_script_generation.yaml` +
  `src/ontobdc/view/adapter/work_stream_script_machine.py`), disparado
  dentro de `EntityViewsPublishedCapability.execute()`
  (`src/ontobdc/view/plugin/capability/transformation/entity_views_published.py`)
  sempre que uma página WorkStream é publicada.

## Regra de ouro do projeto (não violar)

A Surface (`index.html`) e a WorkStream view **nunca leem bytes reais de
arquivo** — toda informação vem do RO-Crate JSON-LD embutido, exceto pelo
`onto-file-viewer-tile` (um único iframe, só em duplo-clique explícito).
Não introduza nenhuma leitura de arquivo fora desse padrão.

## O que já foi tentado (e o resultado real, não o esperado)

1. **Statechart de geração dos 10 scripts + wiring no
   `ENTITY_VIEWS_PUBLISHED`** — resolveu um crash real
   (`FileNotFoundError` no `work_stream_view.js` monolítico) e a página
   parou de renderizar vazia. Commits: `ce9a086`, `7e7906d`, `e362353`
   (ontobdc-wip), `d35f4d4` (ontobdc-wip). **Confirmado funcionando.**
2. **Remoção da race de `pyodide.FS.syncfs(true, callback)` não
   aguardado após `mountNativeFS()`** — bug real (o `techcenter-doc` de
   referência nunca chama `syncfs()` depois de `mountNativeFS()`), mas
   **não resolveu o sintoma relatado pelo usuário**. Commit `405c314`
   (ontobdc-view v0.5).
3. **5 chaves de i18n faltando** (`browserFileSystemAccessUnavailable`,
   `noWorkStreamContext`, `multipleDatasetsSelectedFolder`,
   `noDatasetSelectedFolder`, `datapackageJsonNotFound`) — confirmado
   pelo usuário que a mensagem traduzida passou a aparecer, mas **o erro
   de fundo continuou**. Commit `1713d68` (ontobdc-view v0.5).
4. **`SyntaxError: unterminated string literal (detected at line 73)`**
   dentro do `WORKBOOK_PARSE_SCRIPT` — causado por `\"` e `\n` escritos
   crus dentro do template literal JS, que o próprio JS processava como
   escape *antes* do Pyodide receber o texto (`\"` virava `"`, `\n`
   virava quebra de linha real), quebrando a string Python no meio e
   fazendo o módulo inteiro falhar ao compilar em **toda** tentativa de
   conectar, não só quando faltava `datapackage.json`. Corrigido
   dobrando as barras (`\"` → `\\"`, `\n` → `\\n`) nas linhas 1015–1022
   de `work_stream_script.py`. Verificado executando o JS gerado de
   verdade no Node e rodando `ast.parse()` no valor real da string em
   runtime (não só `node --check`, que não pega esse tipo de bug).
   Commit `e57fe2c` (ontobdc-view v0.5). **Ainda não confirmado pelo
   usuário no browser real — pode não ser a causa (única ou principal)
   de "Pyodide não carrega".**

## Hipóteses ainda não descartadas para "Pyodide não carrega"

Como ainda não há stack trace/evidência fresca de browser para o
sintoma atual, considere investigar, nesta ordem:

- **CSP/bloqueio de rede para `cdn.jsdelivr.net`** — se a página é aberta
  via `file://` ou atrás de um proxy corporativo/firewall que bloqueia
  jsdelivr, o `<script src="https://cdn.jsdelivr.net/...">` nunca
  carrega e `loadPyodide` nunca vira função. Veja se há erro de CSP
  (`Refused to load the script ... because it violates the following
  Content Security Policy directive`) ou erro de rede (`net::ERR_*`) no
  Console/Network.
- **`micropip.install('rdflib')` ou `('openpyxl')` falhando** — essas
  instalações dependem de acesso de rede ao índice de pacotes do
  Pyodide/PyPI a partir do worker/main thread do browser. Um erro aqui
  aparece como uma `PythonError`/`Promise rejection`, não como falha de
  `loadPyodide()` propriamente dita — vale diferenciar os dois casos.
- **Origem `file://` sem contexto seguro** — Pyodide/WASM podem se
  comportar de forma inconsistente ou falhar silenciosamente quando a
  página é aberta via duplo-clique (`file://`) em vez de servida por
  `http(s)://`. Confirme como o usuário está abrindo a página gerada.
- **Erro de sintaxe/execução em outro dos 10 arquivos JS gerados** —
  como o bug de escaping mostrou, `node --check` não é suficiente;
  qualquer um dos 10 arquivos pode ter o mesmo padrão de bug (Python cru
  dentro de crase) se algum outro bloco Python usar `\"`, `\n`, `` ` ``
  ou `${` sem escapar. Foi conferido que só `WORKBOOK_PARSE_SCRIPT` tinha
  esse problema (`LINKSET_PYTHON_SCRIPT` e `FILE_DISPLAY_PARSE_SCRIPT`
  não têm nenhuma barra invertida no conteúdo atual) — mas vale
  reconferir depois de qualquer edição nova.
- **Falha silenciosa por exceção não tratada em `ensurePyodide()`** —
  se `loadScriptTag` rejeita (ex.: 404, CORS) e ninguém trata o reject
  no chamador, o botão pode simplesmente "não fazer nada" sem log
  visível. Vale conferir se toda chamada de `ensurePyodide()` tem
  try/catch com mensagem visível ao usuário.

## Como validar de verdade (metodologia obrigatória)

Não aceite "parece corrigido" sem: (1) gerar o JS de verdade a partir do
adapter Python (`ontobdc_view.work_stream_script_source(<nome>)`), (2)
executar esse JS de verdade (Node para sintaxe/strings; browser real para
o fluxo completo de conexão), (3) para qualquer Python embutido em
template literal JS, extrair o **valor de runtime da string** (não o
texto bruto do arquivo `.py`) e rodar `ast.parse()` nele. Extração via
fatiamento de texto Python passa direto por cima de bugs de escaping do
JS — foi exatamente esse ponto cego que deixou o bug da linha 1015
passar antes.

## Regras de branch (obrigatórias)

- `ontobdc-view`: desenvolver e dar push em `v0.5`.
- `ontobdc-wip`: desenvolver e dar push em `v0.18`.
- **Nunca** em `master`.
- Antes de começar E antes de cada push: `git fetch origin <branch>` e
  comparar com o HEAD local — outros agentes (inclusive você mesmo, em
  outras sessões) podem ter empurrado direto para essas branches sem
  coordenação.

## Entregável esperado

- Diagnóstico com evidência real (console/network do browser).
- Fix aplicado no arquivo correto (`ontobdc-view` para geração de JS,
  `ontobdc-wip` para o pipeline/statechart, conforme o caso).
- Prova de verificação (execução real do JS gerado, não só lint/`node
  --check`).
- Commit + push na branch correta, com mensagem explicando causa raiz
  (não só o sintoma).
