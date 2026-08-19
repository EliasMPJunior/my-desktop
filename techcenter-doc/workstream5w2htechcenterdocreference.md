# WorkStream 5W2H — Reference of `techcenter-doc` (working implementation)

Fonte lida por completo, sequencialmente, do início ao fim:

- `techcenter-doc/.__ontobdc__/asset/infobim-view/js/workstream_5w2h.js` (2087 linhas)
- `techcenter-doc/.__ontobdc__/asset/infobim-view/js/spatial_annotations.js` (819 linhas)
- `techcenter-doc/template/work_stream.html.jinja` (a página real que hospeda os dois scripts acima — lida numa segunda passada, depois de perceber que a primeira versão deste documento descrevia só a mecânica interna do JS sem nunca ter visto a página/DOM real que a aciona)
- 3 páginas geradas reais, para conferir contra o template: `view/work_stream/7c7e9d91-...html`, `view/work_stream/f834661b-...html`, `.workstream/payload/view/work_stream/7c7e9d91-...html`

Este documento lista **todas as funcionalidades** da página WorkStream 5W2H e o **passo a passo real** de como cada uma funciona no código que já está pronto, testado e funcionando. É referência para reimplementar/comparar com `ontobdc-view`, não uma proposta de redesenho.

**Nota sobre a primeira versão deste documento**: a versão inicial documentou apenas a mecânica das funções JS, sem nunca ter aberto o HTML/template que efetivamente desenha a página. Isso causou pelo menos um erro factual (rótulo inicial do botão de abrir projeto) e uma omissão relevante (o módulo de anotações não é carregado sob demanda na prática — já vem incluído no HTML). Ambos corrigidos abaixo, na Seção 0.5.

---

## 0. Ponto de entrada e estado global

O IIFE lê `window.infoBimWorkStreamView` (o `payload`, escrito pelo servidor/gerador da página) e resolve os elementos do DOM: `#open-container`, `#update-project`, `#container-status`, `#container-status-dot`.

Estado de módulo (variáveis fechadas no IIFE, não em `window`):

- `activeContainerHandle` — o `FileSystemDirectoryHandle` do contêiner atualmente aberto.
- `activePyodide` — a instância do Pyodide carregada para esse contêiner.
- `resourceModel = { resources, catalogResources, relationships }` — o modelo de recursos vindo do último `openContainer()`.
- `previewObjectUrl` — URL de objeto (`URL.createObjectURL`) do preview atual, revogada antes de trocar de preview.
- `spatialAnnotationsLoading` — promessa em andamento do carregamento lazy de `spatial_annotations.js`.

`payload.projectId` vira a chave (`handleKey`) usada no IndexedDB, com fallback para a string `"active-project"`.

---

## 0.5. A página real (`template/work_stream.html.jinja`) — o que o usuário efetivamente vê

Este é o template Jinja que o gerador do projeto renderiza uma vez por WorkStream (um arquivo `.html` por `elementId`, em `view/work_stream/<id>.html`, e uma cópia espelhada em `.workstream/payload/view/work_stream/<id>.html` para o caso de "sourceView" — WorkStream acessado a partir de dentro do payload de um dataset ICDD, com paths relativos mais profundos: `../../../../` em vez de `../../`).

**Estrutura real do DOM** (tudo isto existe ANTES de qualquer JS rodar, exceto o `<section id="five-w-two-h-layout">`, que é preenchido depois):

1. **Hero** (`.five-w-two-h-hero`): logo (`#workstream-logo`, `src` setado via JS para `<assetRoot>/logo.png`), `"InfoBIM WorkStream"` + nome do projeto (`#project-title`), título `"5W2H"` (`#workstream-name`), descrição inicial fixa `"Abra o projeto para carregar os dados vivos desta frente de trabalho."` (`#workstream-description`) — ambos sobrescritos por `renderWorkStream()` assim que há dados (embutidos ou carregados).
2. **Barra de status** (`.workstream-status-bar`):
   - Indicador de status: bolinha (`#container-status-dot`) + texto (`#container-status`, começa como `"Não carregado"`).
   - Botão **"Atualizar"** (`#update-project`, ícone de setas circulares) — **começa `disabled` no HTML** (só é habilitado depois do primeiro `openContainer()` bem-sucedido).
   - Botão **"Carregar"** (`#open-container`) — **este é o rótulo inicial real**, não "Abrir projeto" como uma versão anterior deste documento descreveu por engano (documentado só a partir da mecânica JS, sem ter visto o HTML). Vira **"Reabrir projeto"** após o primeiro sucesso (seção 14).
   - Link **"Voltar à página principal"** / **"Voltar ao projeto"** (`#workstream-main-link`, o texto varia entre as páginas geradas) — aponta para o `index.html` do projeto (a Surface principal), com o `href` calculado em runtime conforme a página está em `view/work_stream/` (`../../index.html`) ou em `.workstream/payload/view/work_stream/` (`../../../../index.html`). **Esta é uma funcionalidade inteira que não estava na primeira versão deste documento**: a página 5W2H não é uma ilha — todo WorkStream tem um link de volta explícito para a Surface (o `index.html` com a listagem RO-Crate) de onde ele foi aberto.
3. **`#five-w-two-h-layout`** — vazio no HTML estático; um script inline (executado antes de `workstream_5w2h.js`) monta a lista de 7 dimensões (`what, why, where, when, who, how, how-much`, cada uma com símbolo `W`/`H`, rótulo e uma pergunta norteadora em português, ex. `"O que será executado?"`) e injeta via `innerHTML` um `<article class="five-w-two-h-row" data-dimension="...">` por dimensão, cada um contendo:
   - Cabeçalho com símbolo (W/H) + rótulo.
   - Painel com a pergunta (`<h2>`) e o valor do campo (`[data-field]`, inicialmente `"—"`).
   - Nav com 4 botões de categoria de recurso: **Pranchas, Documentos, Comunicação, Fotos** (`data-resource-toggle`).
   - O painel de recursos completo (inicialmente `hidden`): árvore de arquivos + toolbar de expandir/recolher + 3 abas **Relacionadas/Sugeridas/Encontradas** (`data-resource-view`) + área de preview com uma **toolbar de 5 botões**: "Tela cheia", "Início" (documento, ativo por padrão), "Anotações" (desabilitado até um arquivo anotável ser selecionado), "Anotar" (idem), "Relacionar à próxima" (idem).
4. Depois disso, três `<script>` adicionais: um define `window.infoBimWorkStreamView` (o `payload`, injetado pelo servidor via Jinja — `{{ ... | tojson }}`), opcionalmente um `<script id="facades-jsonld" type="application/ld+json">` (só presente em algumas variantes, ver nota abaixo), e por fim um bloco que injeta via `document.write` (nessa ordem, todos `defer`): `pyodide.js` (do CDN jsDelivr), `email_reader.js`, `spatial_annotations.js`, `workstream_5w2h.js`.

**Duas variantes reais da página, encontradas comparando páginas geradas de fato** (não estava documentado antes):
- **WorkStream na raiz do projeto** (ex. `7c7e9d91-...html`): `payload` **sem** `datasetPath`, e **sem** `<script id="facades-jsonld">` — a página começa sem nenhum dado pré-carregado (`loadEmbeddedWorkStream()` falha silenciosamente por falta do elemento, ver seção 5) e sem prefixo de dataset nos paths (`dataset_prefix = ""` no script Python, seção 14).
- **WorkStream dentro de um sub-dataset** (ex. `f834661b-...html`, dataset `"desmobilizacao"`): `payload.datasetPath = "desmobilizacao"`, **com** `facades-jsonld` embutido (renderização inicial grátis funciona), e todos os paths de metadados (`datapackagePath`, `linksetPath`, etc.) prefixados com `desmobilizacao/`. Gerada por uma versão ligeiramente mais nova do gerador (cache-bust `workstream_5w2h.js?v=20260805-dataset-paths` vs. `v=20260804-dataset-view` na variante de raiz) — ou seja, o suporte a `datasetPath`/prefixo de dataset foi adicionado depois, e nem toda página existente necessariamente foi regenerada com ele.

**Dependência de CSS**: `<assetRoot>/css/project_dashboard.css` — todas as classes usadas acima (`five-w-two-h-row`, `workstream-resource-panel`, `workstream-file-tree`, etc.) vêm desse arquivo, não inline. Uma reimplementação (`ontobdc-view`) precisa ou reusar essas classes exatamente, ou ter seu próprio CSS equivalente — a estrutura de `data-*` attributes é o contrato real que `workstream_5w2h.js` espera encontrar no DOM; qualquer `data-resource-toggle`, `data-field`, `data-dimension`, `data-file-tree` etc. ausente ou com nome diferente quebra silenciosamente a funcionalidade correspondente (a maioria das funções faz `row.querySelector(...)` e segue em frente com `null`/`undefined` sem lançar erro visível).

---

## 1. Carregamento do módulo de anotações espaciais

**Funções:** `spatialAnnotationsScriptUrl()`, `ensureSpatialAnnotations()`

**Correção importante em relação à primeira versão deste documento**: na página real (seção 0.5), `spatial_annotations.js` **já vem incluído** como `<script defer>` no HTML, carregado em paralelo com `workstream_5w2h.js`. Ou seja, `window.InfoBIMSpatialAnnotations` normalmente **já existe** antes de qualquer botão ser clicado — não há, na prática, um carregamento "sob demanda" visível ao usuário. O código abaixo é um caminho defensivo/de fallback (cobre o caso de a página não incluir a tag, ou de a ordem de carregamento dos `defer` não ter terminado ainda quando o usuário clica rápido demais), não o caminho principal:

1. `spatialAnnotationsScriptUrl()` primeiro procura uma tag `<script src*="spatial_annotations.js">` já presente no documento (vai achar, na página real); se não achar, deriva a URL a partir da tag `<script src*="workstream_5w2h.js">` (troca o nome do arquivo, preservando o diretório), anexando um `?v=...` fixo de cache-busting.
2. `ensureSpatialAnnotations()` é idempotente: se `window.InfoBIMSpatialAnnotations` já existe (caso normal), retorna na hora, sem criar nenhuma tag nova; se um carregamento já está em andamento, devolve a mesma promessa (evita `<script>` duplicada em cliques rápidos); senão cria a tag `<script async>`, resolve no evento `load` (checando que o global realmente apareceu) e rejeita no evento `error`, sempre limpando `spatialAnnotationsLoading` em caso de falha para permitir nova tentativa.

---

## 2. Persistência do `FileSystemDirectoryHandle` via IndexedDB

**Funções:** `openDatabase()`, `loadStoredHandle()`, `storeHandle()`, `deleteStoredHandle()`

- Banco `"infobim-container-access"`, versão 1, object store `"handles"` (criada em `onupgradeneeded`).
- A chave é `handleKey` (o `projectId`), o valor é o próprio `FileSystemDirectoryHandle` — os handles são **estruturalmente clonáveis** e o IndexedDB os serializa nativamente, então isso persiste a referência ao diretório real do SO entre sessões do navegador (não é preciso o usuário escolher a pasta de novo toda vez).
- `storeHandle`/`deleteStoredHandle` usam transações `readwrite`; `loadStoredHandle` usa `readonly`.

---

## 3. Resolução do diretório do contêiner (raiz vs. pasta-mãe)

**Funções:** `isContainerHandle()`, `resolveContainerHandle()`, `requestWritableHandle()`, `acquireContainerHandle()`

Passo a passo de `acquireContainerHandle()` (chamada por `openContainer()`):
1. Tenta `loadStoredHandle()`. Se existir um handle salvo:
   - Chama `requestWritableHandle(handle)`, que primeiro faz `queryPermission({mode:"readwrite"})` (não dispara diálogo do navegador) e só chama `requestPermission(...)` (dispara diálogo) se ainda não estiver `"granted"`.
   - Se a permissão foi concedida, tenta `resolveContainerHandle(handle)`; se isso falhar (ex.: pasta não é mais um contêiner válido), **apaga** o handle armazenado (`deleteStoredHandle`) e cai para o fluxo de escolher pasta.
   - Se a permissão **não** foi concedida, também apaga o handle armazenado.
2. Se não havia handle salvo (ou foi invalidado acima), chama `window.showDirectoryPicker({id: "infobim-project-container", mode: "readwrite", startIn: "documents"})` — diálogo nativo do SO, só funciona com um usuário real na tela.
3. O handle escolhido passa por `resolveContainerHandle()` e o resultado (a pasta real do contêiner) é salvo via `storeHandle()`.

`isContainerHandle(handle)` define "é um contêiner": tenta abrir `handle/.__ontobdc__/datapackage.json`; se `NotFoundError`, retorna `false`; qualquer outro erro é propagado.

`resolveContainerHandle(selectedHandle)` tolera o usuário escolher tanto a pasta do contêiner diretamente quanto sua pasta-mãe:
1. Se `selectedHandle` já é um contêiner, retorna ele mesmo.
2. Senão, itera `selectedHandle.values()` procurando subpastas que **sejam** contêiner.
3. Exatamente 1 match → retorna esse match. 0 matches → erro "não contém um projeto InfoBIM". >1 matches → erro "contém mais de um projeto InfoBIM, escolha diretamente a pasta do projeto".

---

## 4. Renderização de texto com formatação leve (markdown-like)

**Funções:** `normalizeRuntimeText()`, `appendInlineFormatting()`, `appendFormattedText()`, `splitStructuredList()`, `renderStructuredField()`

Usadas para exibir os campos 5W2H (texto livre digitado por usuários em uma planilha Excel) com alguma estrutura visual, sem um parser de markdown completo:

1. `normalizeRuntimeText(value)` — normaliza `\r\n`/`\r` para `\n`, também decodifica sequências literais `\n` (2 caracteres, caso o texto tenha vindo escapado), e dá `trim()`.
2. `appendInlineFormatting(element, value)` — regex `/(\*\*([\s\S]+?)\*\*|__([\s\S]+?)__)/g` percorre o texto de uma linha, transformando `**negrito**` em `<strong>` e `__ênfase__` em `<em>`, preservando o resto como nós de texto puro (nunca `innerHTML`, então é seguro contra XSS).
3. `appendFormattedText(element, value)` — quebra o valor por `\n`, insere `<br>` entre linhas e chama `appendInlineFormatting` em cada uma.
4. `splitStructuredList(value)` — tenta detectar se o texto é uma lista (numerada `1.`/`1)`/`1-`, ou com marcadores `*`/`-`/`•`/`▪`/`◦`/`●`/`>`):
   - Insere `; ` antes de cada nova linha que começa com um marcador de item, depois separa por esse `;` (lookahead do marcador).
   - Se algum item resultante ficar vazio, desiste (retorna `null` — cai no texto plano).
   - Localiza o primeiro item que tem marcador; tudo antes disso vira `preamble` (texto introdutório antes da lista).
   - Todos os itens a partir daí devem ter marcador, senão desiste.
   - Detecta se é lista ordenada (todos os itens com marcador numérico) e, se sim, qual o número inicial (para `<ol start="N">`).
   - Remove os marcadores de cada item.
5. `renderStructuredField(element, value)` — usa `structuredList` se detectado (monta `<span class="...-list-preamble">` + `<ol>`/`<ul>` com `<li>` formatados via `appendFormattedText`); senão só chama `appendFormattedText` direto. Texto vazio/nulo vira `"—"`.

---

## 5. Renderização do registro 5W2H (What/Why/Who/Where/When/How/How Much)

**Funções:** `renderWorkStream()`, `jsonLdPropertyValue()`, `embeddedWorkStreamRecord()`, `loadEmbeddedWorkStream()`

- `renderWorkStream(record)` — preenche `#workstream-name` e `#workstream-description` (texto simples), e para cada elemento `[data-field]` na página chama `renderStructuredField(element, record[element.dataset.field])` — ou seja, cada campo 5W2H no HTML tem um atributo `data-field="What"` (etc.) que casa com a chave do `record`.
- **Fallback sem pyodide/sem pasta conectada**: antes mesmo de o usuário conectar uma pasta, a página já mostra dados a partir do JSON-LD embutido:
  - `embeddedWorkStreamRecord()` lê `<script id="facades-jsonld">`, pega o array `@graph`, acha o nó cujo `@id === payload.workstreamUri`, e monta um `record` no mesmo formato usando `jsonLdPropertyValue(node, localName)` — que acha a propriedade cujo **nome local** (parte após `#` ou `/` da URI) bate (case-insensitive) com `localName` (`"identifier"`, `"title"`, `"description"`, `"what"`, `"why"`, `"who"`, `"where"`, `"when"`, `"how"`, `"howMuch"`), resolve o primeiro valor do array JSON-LD (podendo ser `{"@value":...}` ou `{"@id":...}` ou literal), retorna string.
  - `loadEmbeddedWorkStream()` chama isso, renderiza com `renderWorkStream`, marca status como `"Dados incorporados à página."` — usado até o usuário clicar em "Carregar"/"Reabrir projeto" e o pyodide carregar os dados reais da planilha.

---

## 6. Árvore de recursos / navegador de arquivos por dimensão

**Funções:** `categoryMatches()`, `resourceIsRelatedToRow()`, `decodeCatalogComponent()`, `visibleResources()`, `appendTreeItems()`, `renderResourceTree()`, `setTreeExpansion()`

Cada linha 5W2H (`.five-w-two-h-row`, uma por dimensão: what/why/who/where/when/how/how-much) tem um painel de recursos com abas **Relacionados / Sugeridos / Encontrados** e categorias (Pranchas/Documentos/Comunicação/Fotos).

1. `visibleResources(row)` decide o que mostrar:
   - Filtra `resourceModel.resources` pela categoria ativa (`row.dataset.activeResource`, ex. `"drawings"`).
   - Se a aba ativa (`row.dataset.activeView`) é `"suggested"` → retorna lista vazia (funcionalidade de sugestão automática não está implementada aqui; é só um placeholder de aba).
   - Se é `"related"` → filtra ainda mais para só os recursos cujo `id` está em `resourceModel.relationships[dimensionUri]` (o linkset ICDD carregado do WorkStreamResource.ttl).
   - Se é `"found"` (nem sugerido nem filtrado por relação) → todos os recursos da categoria, relacionados ou não.
2. `appendTreeItems(parent, node, row)` — monta recursivamente uma árvore `<ul><li>` a partir de uma estrutura `{directories: {...}, files: [...]}`: pastas viram `<details><summary>` (fechadas por padrão), arquivos viram `<button>` clicável que chama `previewResource(row, resource)`. Se o arquivo é o `row.dataset.selectedResource` atual, ganha classe `is-active` e um botão extra de ação de relação (relacionar/desrelacionar) ao lado, delegando o clique para o botão principal de ação de relação da linha (`row.querySelector("[data-relation-action]").click()`).
3. `renderResourceTree(row)` — chama `visibleResources`, monta uma árvore de diretórios em memória a partir do `id` (ou `displayParts`, se presente) de cada recurso — decodificando cada segmento de path com `decodeCatalogComponent` (`decodeURIComponent` com fallback silencioso) — e desenha via `appendTreeItems`. Se não há recursos, mostra uma mensagem vazia contextual ("Nenhum arquivo sugerido/encontrado/relacionado").
4. `setTreeExpansion(row, expanded)` — os botões "Expandir tudo"/"Recolher tudo" (`[data-tree-action]`) simplesmente ligam/desligam `.open` em todos os `<details class="workstream-tree-directory">` daquela linha.

---

## 7. Preview em tela cheia

**Funções:** `updateFullscreenAction()`, `exitPreviewFullscreen()`, `togglePreviewFullscreen()`

- `togglePreviewFullscreen(row)` — se já está em tela cheia (real, `document.fullscreenElement === previewPane`, ou fallback CSS `.is-fullscreen-fallback`), sai; senão tenta `previewPane.requestFullscreen()` (API real do navegador); se isso falhar (ex.: navegador bloqueia fullscreen dentro de iframe/contexto restrito), aplica um **fallback CSS**: classe `is-fullscreen-fallback` no painel de preview + `has-preview-fullscreen` no `<body>` (presumivelmente CSS `position: fixed` cobrindo a tela).
- `exitPreviewFullscreen(row)` — chama `document.exitFullscreen()` se aplicável (com try/catch silencioso), sempre remove as classes de fallback.
- `updateFullscreenAction(row)` — atualiza o texto/aria-label/estado `is-active` do botão de tela cheia conforme o estado atual.
- Listener global `document.addEventListener("fullscreenchange", ...)` mantém todos os botões de tela cheia de todas as linhas sincronizados quando o navegador sai do fullscreen por conta própria (ex. tecla F11/Esc do SO).
- Listener global de `keydown` para `Escape` fecha qualquer preview em fallback CSS (já que `Escape` sozinho não dispara `fullscreenchange` no modo fallback, que não é fullscreen real).

---

## 8. Alternância Documento ↔ Anotações (modo de preview)

**Funções:** `setPreviewMode()`, `annotationCapable()`, `showAnnotationsMode()`

- Cada linha tem dois botões de modo: `[data-document-mode-action]` e `[data-annotations-mode-action]`, mais um `[data-annotation-action]` (para **criar/editar** uma anotação, diferente de apenas visualizá-las).
- `annotationCapable(context)` — um arquivo só suporta anotação espacial se `context.mediaType` começa com `image/`, é `application/pdf`, ou a extensão do `id` da representação bate com `.png/.jpg/.jpeg/.webp/.gif/.bmp/.pdf`.
- `setPreviewMode(row, mode)` — só alterna classes visuais `is-active`/`aria-pressed` dos dois botões de modo; não troca o conteúdo sozinho.
- `showAnnotationsMode(row, context)` — exige um `context` válido; via `ensureSpatialAnnotations()` carrega o módulo (se necessário) e chama `spatialAnnotations.showPreview(context)` (ver seção 13, "Visualização — sem edição"), depois `setPreviewMode(row, "annotations")`.
- O botão de modo "Documentos" (`documentModeAction`) simplesmente re-chama `previewResource(row, resource)` para o recurso atualmente selecionado (recuperado de `resourceModel.catalogResources`), o que já deixa o modo em "document" (ver seção 9).

---

## 9. Preview de conteúdo de arquivo (por tipo)

**Funções:** `fileFromCatalogId()`, `decodedCatalogPath()`, `previewRepresentation()`, `clearPreview()`, `previewResource()`

`previewResource(row, resource)` é o **dispatcher central** chamado ao clicar em um arquivo na árvore:

1. Marca `row.dataset.selectedResource = resource.id`, re-renderiza a árvore (para destacar o item ativo e mostrar o botão de relação ao lado dele), configura os botões de ação de relação (`configureRelationAction`) e de propagação (`configurePropagateAction`), atualiza o título do preview.
2. Limpa qualquer preview de anotação anterior (`InfoBIMSpatialAnnotations.clearPreview`) e o conteúdo do painel.
3. `previewRepresentation(resource)` — **fallback de representação para DWG**: se o recurso é um `.dwg` (CAD, não visualizável no navegador), procura no catálogo (`resourceModel.catalogResources`) um arquivo irmão com o mesmo caminho mas extensão `.png` ou `.pdf` (nessa ordem) — se achar, usa **esse** arquivo para a prévia visual, mantendo o `.dwg` original como o "recurso" lógico selecionado.
4. `fileFromCatalogId(resourceId)` — resolve o `id` do RO-Crate (um path relativo, url-encoded por segmento) navegando `activeContainerHandle` via `getDirectoryHandle`/`getFileHandle` segmento a segmento (decodificando cada um com `decodeURIComponent`, ignorando `.`/`..`), retorna o `File` real via `handle.getFile()`.
5. Monta `window.infoBimAnnotationContext` / `row.infoBimAnnotationContext` — objeto com `containerHandle, resource, representation, file, mediaType, dimensionUri` — consumido tanto pelo botão de anotação quanto por `spatial_annotations.js`. Habilita/desabilita os botões de anotação conforme `annotationCapable()` **e** conforme o recurso já estar relacionado à dimensão daquela linha (`resourceIsRelatedToRow`) — ou seja, **só se pode anotar um arquivo que já está relacionado à dimensão**.
6. Chama `setPreviewMode(row, "document")`.
7. Renderiza o conteúdo conforme `mediaType`/extensão, sempre revogando a `previewObjectUrl` anterior antes:
   - `image/*` → `<img>` com `URL.createObjectURL(file)`.
   - `application/pdf` → `<iframe>` apontando pro object URL (visualizador PDF nativo do navegador).
   - `.msg`/`.eml` → `parseEmail()` + `renderEmail()` (seção 10).
   - `text/*` ou `.txt/.md/.csv/.json/.ttl/.xml` → `<pre>` com `file.text()` (texto plano, sem parsing).
   - Qualquer outro tipo → uma `<dl>` de metadados (nome, caminho, tipo) — sem preview de conteúdo.
8. Revela a barra de ferramentas do preview (`[data-preview-toolbar]`) e atualiza o botão de fullscreen.
9. Dispara `document.dispatchEvent(new CustomEvent("infobim:preview-ready", {detail: ...}))` — hook para qualquer script externo reagir ao preview.
10. Qualquer erro no processo cai no `catch`, que chama `clearPreview(row, "Não foi possível abrir o arquivo: ...")`.

`clearPreview(row, message)` — reseta tudo: sai do fullscreen, esconde a toolbar, revoga object URL, limpa `dataset.selectedResource/selectedRepresentation/selectedMediaType`, zera o `infoBimAnnotationContext`, desabilita os botões de anotação/propagação, chama `configureRelationAction(row, null)` (esconde o botão de relação), chama `InfoBIMSpatialAnnotations.clearPreview` se o módulo já estiver carregado, e mostra a mensagem padrão "Selecione um arquivo" (ou uma mensagem customizada).

---

## 10. Visualização de e-mail (.msg/.eml)

**Funções:** `emailAddress()`, `emailAddressList()`, `msgRecipients()`, `safeEmailDocument()`, `appendEmailField()`, `renderEmail()`, `parseEmail()`

1. `parseEmail(file, resourceId)` — exige `window.InfoBIMEmailReader` (biblioteca externa, carregada em outro lugar da página, não neste arquivo); route para `parseMsg(buffer)` ou `parseEml(buffer)` conforme a extensão do `resourceId`.
2. `emailAddress(value)` — normaliza um valor de endereço (string simples, ou `{name, address}`/`{name, email}`) para `"Nome <endereço>"` ou só um dos dois.
3. `emailAddressList(values)` — aplica em array (ou valor único), junta com `"; "`.
4. `msgRecipients(message, type)` — para formatos `.msg` que trazem uma lista `recipients` com `recipType` (`"to"`/`"cc"`), filtra por tipo.
5. `renderEmail(preview, message)` monta o cabeçalho (assunto, De/Para/Cc com fallback entre os vários formatos de campo possíveis dependendo se veio de `.eml` ou `.msg`, Data) e o corpo:
   - `safeEmailDocument(html)` — **sanitização do HTML do e-mail antes de exibir**: usa `DOMParser` para parsear, remove elementos perigosos (`script, object, embed, iframe, form, input, button`), remove qualquer atributo `on*` (handlers inline) e qualquer `href/src/action` que comece com `javascript:` ou `data:text/html`, depois envolve o HTML resultante num documento próprio com CSP restritivo (`default-src 'none'; img-src data: blob:; style-src 'unsafe-inline'`) — esse documento sanitizado vira o `srcdoc` de um `<iframe sandbox="">` (sandbox vazio = máxima restrição, sem scripts, sem same-origin), então mesmo que a sanitização falhasse o iframe ainda estaria isolado.
   - Corpo de texto puro (sem HTML) é escapado manualmente (`&`, `<`, `>`) e envolvido em `<pre>`.
   - Anexos (se houver) aparecem num rodapé listando nomes, sem preview individual.

---

## 11. Sincronização do manifesto RO-Crate (botão "Atualizar")

**Funções:** `directoryContainsFile()`, `isDatasetDirectory()`, `collectProjectFiles()`, `encodeCatalogPath()`, `makeRoCrate()`, `synchronizeProjectManifest()`, `updateProject()`

Esta é a funcionalidade por trás do botão `updateButton` ("Atualizar projeto" / `#update-project`) — **regera o catálogo de arquivos do zero a partir do sistema de arquivos real**, sem precisar do usuário editar `ro-crate-metadata.json` manualmente.

1. `collectProjectFiles(directory, prefix)` — percorre recursivamente `directory.values()`, construindo paths relativos. Pula:
   - Qualquer pasta chamada `.__ontobdc__` (a pasta de metadados do OntoBDC) ou `.__onmtobdc__` (typo defensivo — provavelmente uma variante histórica/erro de digitação que também precisa ser ignorada).
   - Qualquer pasta que `isDatasetDirectory()` identifique como um **dataset ICDD aninhado** (contém `.__ontobdc__/dataset.ttl`, `.__ontobdc__/nid.ttl`, ou `linkset/datapackage.json`) — ou seja, datasets ICDD dentro do contêiner não são recatalogados recursivamente por este mecanismo (evita duplicar/misturar catálogos de sub-datasets).
   - Retorna a lista de paths ordenada alfabeticamente.
2. `makeRoCrate(filePaths)` — monta um RO-Crate **mínimo**: `ro-crate-metadata.json` descritor + `Dataset` raiz (`hasPart` apontando para todos os arquivos) + um nó `File` para cada path (só com `@id`/`@type`, sem metadados enriquecidos como `name`/`encodingFormat`/categoria). Cada `id` é url-encoded segmento por segmento (`encodeCatalogPath`).
3. `synchronizeProjectManifest()` — chama `collectProjectFiles`, escreve o resultado de `makeRoCrate` em `.__ontobdc__/ro-crate-metadata.json` (cria o arquivo se não existir), retorna a contagem de arquivos.
4. `updateProject()` (handler do clique) — desabilita os botões, mostra status "Atualizando os arquivos do projeto...", chama `synchronizeProjectManifest()`, mostra quantos arquivos foram catalogados, e **imediatamente chama `openContainer()` de novo** para recarregar tudo (inclusive re-executar a classificação por categoria do `file_display.ttl` sobre o RO-Crate recém-regravado). Em caso de erro, mostra status de erro; sempre reabilita `openButton` e reabilita `updateButton` só se `activeContainerHandle` ainda existir.

Importante: este mecanismo só recataloga **existência e path** dos arquivos — a categorização (Pranchas/Documentos/etc.), nome amigável e `encodingFormat` são recalculados depois, durante `openContainer()`, a partir do RO-Crate + `file_display.ttl` (ver seção 14). Ou seja, "Atualizar" é sobre **detectar arquivos novos/removidos no disco**, não sobre editar metadados.

---

## 12. Relacionar / desrelacionar arquivo a uma dimensão (linkset ICDD via Pyodide+rdflib)

**Funções:** `relationActionIcon()`, `configureRelationAction()`, `relationActionDetails()`, `resourceLinksetHandle()`, `serializeRelationship()`, `updateRelationship()`

Este é o mecanismo que grava a relação Recurso↔Dimensão no arquivo `WorkStreamResource.ttl`, seguindo o modelo ISO 21597 ICDD Linkset (`ls:DirectedBinaryLink`).

1. `relationActionDetails(row, resource)` decide o que o botão de ação de relação deve fazer, dependendo da aba ativa (`row.dataset.activeView`):
   - Na aba "found" (encontrados, fora do filtro de relacionados), se o recurso **já** está relacionado, não mostra ação (retorna `null` — já é o botão da árvore que cobre isso via `relationButton`, mas o botão principal fica escondido para não duplicar).
   - Aba "related" → ação `"remove"` ("Remover relação"). Qualquer outra aba → ação `"add"` ("Relacionar arquivo").
2. `configureRelationAction(row, resource)` aplica isso ao botão `[data-relation-action]`: esconde se não há ação, senão mostra, seta `dataset.action`, classe `is-remove`, aria-label/title, e o ícone SVG (`relationActionIcon` — dois ícones diferentes de "corrente" ligada/quebrada, desenhados inline como paths SVG).
3. `resourceLinksetHandle()` — resolve/cria `activeContainerHandle/.__ontobdc__/linkset/WorkStreamResource.ttl` (com `create: true` em cada nível).
4. `serializeRelationship(action, dimensionUri, resourceId)` — **o núcleo Python via Pyodide**:
   - Lê o conteúdo atual do `.ttl`, passa como `relationship_request_json` (JSON com `action`, `dimensionUri`, `resourceId`, `turtle`) para o Pyodide via `pyodide.globals.set`.
   - O script Python (usando `rdflib`) parseia o turtle existente num `Graph()` (se não vazio).
   - `endpoint_value(element)` — helper que resolve o valor real de um `LinkElement` (via `hasIdentifier` → `ls:uri` ou `ls:identifier`).
   - Procura links `ls:DirectedBinaryLink` cujos dois extremos (`hasFromLinkElement`/`hasToLinkElement`, resolvidos via `endpoint_value`) casem exatamente com `{dimensionUri, resourceId}` (checando que ambos os valores pedidos estão no conjunto de valores dos dois extremos — `issubset`).
   - **Ação "add"**, sem match existente: gera um `hashlib.sha256(dimensionUri + "|" + resourceId)` truncado (24 chars) como sufixo de URI determinístico (`urn:infobim:linkset:workstream-resource:<hash>`), cria toda a estrutura ICDD: o `link` (`DirectedBinaryLink`), dois `LinkElement`s (`:dimension`, `:resource`), e seus respectivos identificadores tipados — `URIBasedIdentifier` (`ls:uri`, `xsd:anyURI`) para a dimensão, `StringBasedIdentifier` (`ls:identifier`) para o recurso.
   - **Ação "remove"**: para cada link que casou, remove o triplo do link em si (como sujeito e como objeto), depois para cada `LinkElement` extremo checa se ainda é referenciado por **outro** link (`hasFromLinkElement`/`hasToLinkElement`); se não for mais usado, remove o elemento e, em cascata, o identificador associado (também checando se ele não é referenciado por mais ninguém) — **limpeza garbage-collected do grafo**, não deixa nós órfãos.
   - Serializa o grafo de volta para turtle (`graph.serialize(format="turtle")`) com o prefixo `ls:` vinculado.
5. `updateRelationship(row, resource, action)`:
   - Atualiza **otimisticamente** `resourceModel.relationships[dimensionUri]` em memória primeiro (adiciona/remove o `resource.id`).
   - Chama `serializeRelationship`, escreve o turtle resultante de volta no arquivo via `createWritable()`/`write()`/`close()`.
   - Se qualquer etapa falhar, **reverte** `resourceModel.relationships[dimensionUri]` ao valor anterior e relança o erro (rollback do estado otimista).

---

## 13. Propagar relação para a próxima dimensão

**Funções:** `nextDimensionRow()`, `dimensionDisplayName()`, `configurePropagateAction()`

- `nextDimensionRow(row)` — pega todas as `.five-w-two-h-row` em ordem no DOM, acha o índice da linha atual, retorna a próxima (ou `null` se for a última — a ordem das dimensões no DOM **é** a ordem lógica de propagação, ex. What→Why→Who→...→How Much).
- `configurePropagateAction(row, resource)` decide o estado/tooltip do botão `[data-propagate-action]`:
  - Sem recurso selecionado → desabilitado, "Selecione um arquivo."
  - Recurso não relacionado à dimensão atual → desabilitado, "Relacione o arquivo a esta dimensão antes de enviá-lo à próxima."
  - Sem próxima dimensão → desabilitado, "Esta é a última dimensão."
  - Já relacionado à próxima dimensão → habilitado, mas tooltip informativo "O arquivo já está relacionado à dimensão X."
  - Senão → habilitado, "Relacionar também à dimensão X."
- O handler de clique (dentro de `configureResourcePanels`) chama `updateRelationship(nextRow, resource, "add")` (reaproveitando toda a lógica ICDD da seção 12, mas mirando a **próxima** linha/dimensão), depois re-renderiza a árvore da próxima linha se ela estiver na aba "related", e mostra status de sucesso. Isso permite ao usuário "empurrar" um arquivo por toda a cadeia 5W2H sem reabrir/re-selecionar em cada dimensão.

---

## 14. Abertura do contêiner — orquestração principal (`openContainer`)

Esta é a função mais longa e central, acionada pelo clique em "Carregar"/"Reabrir projeto" (`openButton`, ver rótulo real na seção 0.5).

Passo a passo:
1. Desabilita `openButton`, status "Solicitando acesso ao projeto...".
2. Verifica pré-requisitos: `window.showDirectoryPicker` deve existir (senão erro pedindo Edge/Chrome); `loadPyodide` deve existir globalmente (script do Pyodide precisa já estar incluído na página).
3. `acquireContainerHandle()` (seção 3) resolve o `FileSystemDirectoryHandle` real do contêiner — com ou sem diálogo, dependendo se já havia permissão salva.
4. Atualiza `#project-title` com o nome da pasta.
5. **Carrega o Pyodide**: `loadPyodide()` (runtime WASM completo, baixado/inicializado do zero a cada chamada — não há cache entre chamadas dentro desta função, mas o objeto `pyodide` retornado é reaproveitado via `activePyodide` para as próximas ações de relação/etc. até o próximo `openContainer()`).
6. **Monta o diretório real no FS virtual do Pyodide**: cria um path único por timestamp (`/container_${Date.now()}`, evita colisão entre reaberturas), `pyodide.FS.mkdirTree(mountPath)`, depois `pyodide.mountNativeFS(mountPath, containerHandle)` — a partir daqui, código Python dentro do Pyodide pode ler/escrever arquivos reais do contêiner do usuário como se fossem um filesystem POSIX normal.
7. Instala pacotes: `pyodide.loadPackage("micropip")`, depois via `micropip.install(["openpyxl", "rdflib"])` (ambos puros-Python/wheels compatíveis com Pyodide, para ler planilhas `.xlsx` e turtle RDF).
8. Passa dois globais para o Python: `view_payload_json` (o `payload` inteiro serializado) e `container_mount_path` (o path de montagem).
9. **Executa o script Python principal** (`WORKBOOK_PARSE_SCRIPT`), que faz, nesta ordem:
   a. Resolve os paths absolutos dentro do mount (`datapackage.json`, `WorkStream.ttl`, `WorkStreamResource.ttl`, `ro-crate-metadata.json`, `file_display.ttl`) a partir das chaves do `payload` (`datapackagePath`, `linksetPath`, `resourceLinksetPath`, `roCratePath`, `fileDisplayOntologyPath`), concatenadas ao `container_mount_path`. `dataset_prefix` vem de `payload["datasetPath"]` (sem barras nas pontas).
   b. Lê `datapackage.json`, acha o recurso nomeado `"work_stream"` na lista `resources`, resolve o path da planilha (`.xlsx`) relativo ao diretório do `datapackage.json`, e a aba (`resource["dialect"]["excel"]["sheet"]`, default `"WorkStream"`).
   c. **Carrega o linkset de mapeamento de colunas** (`WorkStream.ttl`, ICDD): para cada `ls:DirectedBinaryLink`, resolve `from`→coluna da planilha (`ls:identifier`, literal) e `to`→campo do facade (`ls:uri`), monta um dicionário `mappings = {coluna_da_planilha: uri_do_campo}`. Se o arquivo não existir, `mappings` fica vazio.
   d. Abre a planilha com `openpyxl.load_workbook(..., data_only=True, read_only=True)`, lê os cabeçalhos da primeira linha, itera as linhas de dados procurando aquela cujo `GlobalId` bate exatamente com `payload["elementId"]` — é esse o **registro 5W2H específico desta instância de WorkStream**. Fecha o workbook.
   e. Se nenhum registro foi encontrado → erro `"WorkStream not found in workbook: <elementId>"`.
   f. **Validação de integridade do mapeamento**: se `mappings` não está vazio, mas algum cabeçalho da planilha não tem mapeamento correspondente, levanta erro listando os campos faltantes — isso é uma checagem de consistência entre a planilha real e o linkset declarado.
   g. **Classificação de recursos por categoria** (`file_display.ttl`): lê perfis `FileDisplayProfile` (cada um com `displayCategory`, conjuntos de `requiredSemanticType`, `acceptedMimeType`, `acceptedExtension`). Para cada item do grafo RO-Crate, `category_for(item, resource_id)` resolve o mimetype (`encodingFormat`), os tipos semânticos (`@type`/`additionalType`), a extensão do arquivo, e casa contra cada perfil: só considera o perfil se os tipos semânticos requeridos (se houver) baterem (por URI completa OU pelo nome local após `#`/`/`), **e** (mimetype OU extensão) baterem — primeiro perfil que casa vence, retorna sua `displayCategory`; sem match, retorna `None` (arquivo aparece no catálogo mas não em nenhuma aba de categoria).
   h. **Parse do RO-Crate**: para cada nó do `@graph` (exceto `.`/`./`), calcula um `resource_id` — se é uma URI externa/`urn:`, mantém como está; senão, se há `dataset_prefix`, prefixa (`f"{dataset_prefix}/{...}"`) — isso é o que permite ao WorkStream de um **sub-dataset** referenciar arquivos do contêiner-mãe com paths corretos. Só considera nós cujo `@type` intersecta `{File, MediaObject, DigitalDocument, CreativeWork, Message, EmailMessage}`. Monta `catalog_resources` (todo arquivo válido, com `id`, `sourceId` original, `name` — do RO-Crate `name` ou do nome do path —, `displayParts` decodificados, `encodingFormat`) e, se `category_for` achou uma categoria, também adiciona (com a categoria) em `resources` (a lista efetivamente navegável nas abas).
   i. **Relações Recurso↔Dimensão** (`WorkStreamResource.ttl`, se existir): monta um índice `resource_id_by_endpoint` (mapeando tanto o `id` prefixado quanto o `sourceId` original de cada recurso para o `id` final — cobre o caso do linkset ter sido gravado com um dos dois formatos). Para cada `DirectedBinaryLink`, resolve os dois extremos, filtra o que bate com `payload["dimensionBaseUri"] + "/"` (a URI da dimensão) e o que bate com um `resource_id_by_endpoint` conhecido; se achar ambos, adiciona `resource_id` à lista `relationships[dimension_uri]`.
   j. Retorna tudo serializado em JSON: `record, mappings, resources, catalogResources, relationships, workbookPath, linksetPath`.
10. De volta no JavaScript: parseia o resultado, chama `renderWorkStream(result.record)` (seção 5), popula `resourceModel`, e **re-renderiza a árvore de qualquer linha que já estava com uma categoria de recurso aberta** (`row.dataset.activeResource` setado) — útil no fluxo de "Atualizar projeto", que reabre o contêiner com o painel já aberto.
11. Status final: `"Projeto aberto: <nome>. Dados carregados."`, texto do botão vira "Reabrir projeto" (ele nunca fica desabilitado permanentemente — pode ser clicado de novo a qualquer momento para recarregar), habilita `updateButton`.
12. Em erro: mensagem específica se envolve `"datapackage.json"` (provavelmente ausente/inacessível), senão a mensagem crua do erro. `openButton` é sempre reabilitado no `finally`, **independente de sucesso ou falha** — nunca fica travado em "Requesting access..." indefinidamente, e o texto do botão só é trocado no caminho de sucesso, então uma falha deixa o texto como estava (geralmente ainda "Carregar" na primeira tentativa).

---

## 15. Inicialização final / listeners globais

No fim do arquivo:
- `document.addEventListener("fullscreenchange", ...)` (seção 7).
- `document.addEventListener("keydown", Escape → sai de qualquer preview em fullscreen fallback)` (seção 7).
- `openButton.addEventListener("click", openContainer)`.
- `updateButton.addEventListener("click", updateProject)`.
- `configureResourcePanels()` é chamada **imediatamente na carga do script** (não espera o contêiner abrir) — liga todos os listeners de clique/teclado dos painéis de recurso de cada linha 5W2H (toggles de categoria, abas related/suggested/found, ações de árvore, modos documento/anotações, botão de anotar, botão de propagar, botão de relacionar/desrelacionar). Isso é possível porque a estrutura DOM das 7 linhas já existe no HTML estático da página (o servidor já sabe as 7 dimensões e desenha os painéis vazios); só o **conteúdo** de cada painel depende dos dados carregados depois via `openContainer()`.

---

## 16. Módulo de Anotações Espaciais (`spatial_annotations.js`)

Carregado lazy (seção 1) e exposto como `window.InfoBIMSpatialAnnotations = {open, close, cancelOpen, decoratePreview, showPreview, clearPreview}`.

### 16.1 Persistência (Turtle customizado, não RDF genérico via rdflib — serialização manual em JS)

**Funções:** `datasetFileHandle()`, `parseAnnotations()`, `serializeAnnotations()`, `persist()`, `loadAnnotations()`

- As anotações vivem em `containerHandle/payload/triple/EnrichmentAnnotation.ttl` (não em `.__ontobdc__/linkset` como as relações — é um path de "payload" do dataset ICDD, não de metadados do OntoBDC).
- `datasetFileHandle()` cria a cadeia de pastas (`payload/triple/`) e o arquivo, com `create: true` em cada nível.
- **Formato de armazenamento**: cada anotação é serializada duas vezes dentro do mesmo `.ttl` — uma vez como triplos RDF "de verdade" (`ea:EnrichmentAnnotation` com `oa:hasBody`/`oa:hasTarget`/`oa:hasSelector` seguindo o vocabulário Web Annotation, `ea:logicalSource`, `representationSource`, `representationHash`, `relatedDimension`, `markerColor`, `dcterms:created`) — **e** uma segunda vez como um único triplo `ea:payload "<json escapado>"` contendo o objeto JS inteiro serializado como string JSON. A leitura (`parseAnnotations`) **não usa um parser Turtle de verdade** — usa uma regex (`/ea:payload\s+("(?:\\.|[^"\\])*")/g`) para extrair só os valores de `ea:payload`, faz `JSON.parse` duas vezes (a string Turtle escapada, depois o JSON dentro dela) e reconstrói o array `annotations` inteiro a partir disso, ignorando silenciosamente entradas malformadas. Ou seja: **os triplos RDF "formais" são gerados para interoperabilidade/leitura por outras ferramentas, mas o próprio `techcenter-doc` só confia no `ea:payload` para reconstruir seu próprio estado** — os dois precisam ficar sempre sincronizados porque são escritos juntos por `serializeAnnotations()`.
- `loadAnnotations(containerHandle)` é cacheada por identidade do `FileHandle` (`loadedHandle === handle` pula a releitura) — evita reparsear a cada abertura se o handle não mudou.
- `persist(containerHandle)` reescreve o arquivo inteiro (`serializeAnnotations()` gera tudo do zero a partir do array `annotations` em memória) a cada save/delete — não é um append incremental.

### 16.2 Hash da representação (SHA-256 nativo com fallback puro-JS)

**Funções:** `rotateRight()`, `sha256Fallback()`, `digest()`

- `digest(file)` tenta `crypto.subtle.digest("SHA-256", bytes)` (API nativa do navegador); se `crypto.subtle` não existir (contexto não-seguro, ex. `file://` sem certos flags, ou navegador antigo), cai para `sha256Fallback()` — uma implementação manual completa do SHA-256 em JavaScript puro (constantes/rotação de bits/schedule de mensagem — implementação de referência do padrão FIPS 180-4). O hash resultante (`representationHash`) é gravado em cada anotação para registrar **qual versão exata do arquivo** foi anotada (útil se o arquivo for substituído depois).

### 16.3 Geração de UUID

**Função:** `makeUuid()` — usa `crypto.randomUUID()` se disponível; senão gera 16 bytes aleatórios (`crypto.getRandomValues` ou `Math.random` como último recurso), ajusta os bits de versão/variante (v4 UUID: nibble mais significativo do byte 6 = `0100`, dois bits mais significativos do byte 8 = `10`), formata em 5 grupos hexadecimais.

### 16.4 Renderização da superfície anotável (imagem ou PDF)

**Funções:** `imageSurface()`, `pdfSurface()`, `makeSurface()`

- `makeSurface(context)` decide entre os dois pelo `mediaType`/extensão.
- `imageSurface(file, context)` — cria um `<img>` a partir de `URL.createObjectURL(file)`, espera `onload` (ou rejeita em `onerror`), retorna `{element, width: naturalWidth, height: naturalHeight, release}` (o `release` revoga o object URL).
- `pdfSurface(file)` — importa **dinamicamente** `pdfjs-dist` de um CDN externo (`cdn.jsdelivr.net`, versão fixa `4.10.38`) — **nota**: isso é a mesma dependência de CDN que, na sandbox de teste deste projeto, retorna 403 na política de rede; em produção/navegador real funciona normalmente. Configura o `workerSrc` também do CDN. Carrega o documento, renderiza a **primeira página** (`getPage(1)`) num `<canvas>` com escala 2x (maior resolução para zoom), retorna `{element: canvas, width, height, release: () => pdf.destroy()}`. **Limitação notável**: só a primeira página de um PDF multi-página é anotável/visualizável aqui.

### 16.5 Marcadores (pontos de anotação sobre a imagem/PDF)

**Funções:** `markerRadius()`, `matchesContext()`, `selectAnnotation()`, `makeMarker()`, `renderMarkers()`, `resetEditor()`

- Cada anotação tem 1+ `points` (`{x, y}` **normalizados** de 0 a 1, não pixels absolutos — permite reescalar a superfície sem perder a posição).
- `matchesContext(annotation, context)` — uma anotação "pertence" a este arquivo se `logicalSource === resource.id` **e** `representationSource === representation.id` (nota: usa o `id` da representação, não da anotação original — então anotações em um `.dwg` cuja prévia é um `.png` associado ficam ligadas ao `.png`, não ao `.dwg`, ver seção 9 item 3).
- `markerRadius(session)` — raio proporcional ao maior lado da imagem (`0.008 * max(width, height)`), então os marcadores mantêm tamanho visual consistente em qualquer resolução.
- `makeMarker(session, point, annotation, draft)` — desenha um `<circle>` SVG; se `annotation` é passado (marcador de uma anotação já salva, não um rascunho em edição), fica clicável/focável (`tabindex`, `role="button"`, `Enter`/`Espaço` também ativam) e ao clicar chama `selectAnnotation` (carrega essa anotação no editor lateral); um `<title>` SVG dá tooltip nativo com o texto da nota.
- `renderMarkers(session)` — redesenha **todos** os marcadores do overlay: primeiro os de anotações já persistidas que casam com o contexto atual (via `matchesContext`), depois, se não há nenhuma anotação selecionada (`!session.selectedId`), também os pontos do rascunho em edição (`session.points`, marcados com classe `is-draft`).
- `selectAnnotation(session, annotation)` — carrega uma anotação existente no editor: copia os pontos, texto, cor, habilita o botão excluir, re-renderiza.
- `resetEditor(session)` — limpa a seleção/pontos/textarea, desabilita excluir, re-renderiza (usado ao clicar "Nova nota" ou ao clicar num ponto vazio da imagem enquanto uma nota já estava selecionada).

### 16.6 Diálogo de edição (`open()`) — criar/editar anotações

Passo a passo de `InfoBIMSpatialAnnotations.open(context)`:
1. Sistema de **geração** (`openGeneration`, incrementado a cada chamada) para suportar cancelamento: se o usuário clicar em outro arquivo/anotação antes deste `open()` terminar de carregar (await de `loadAnnotations`, `makeSurface`, `digest`, todos assíncronos), `ensureOpenIsActive(generation, surface)` detecta que a geração mudou e lança um `AbortError`, liberando qualquer recurso (`surface.release()`) já alocado por essa chamada obsoleta — evita condição de corrida onde um diálogo antigo "vence" e sobrescreve um mais novo.
2. Carrega anotações do contêiner, monta a superfície (imagem/PDF), calcula o hash SHA-256 do arquivo, **fecha qualquer diálogo já aberto** (`close()`).
3. Monta o DOM do diálogo do zero via `document.createElement` (nunca `innerHTML` com dados externos): cabeçalho com nome do arquivo e botão fechar; área de trabalho com o `stage` (imagem/PDF + overlay SVG) rolável (`scroller`) e um painel editor lateral (textarea de nota, seletor de cor, botões Nova nota/Excluir/Salvar).
4. Anexa ao `document.body`, adiciona classe `has-annotation-dialog` no body (provavelmente para CSS de bloqueio de scroll/z-index).
5. **Clique no stage** (fora de um marcador existente): se havia uma anotação selecionada, reseta o editor primeiro (começa uma nota nova); calcula a posição normalizada do clique relativa ao `stage.getBoundingClientRect()` (clampada entre 0 e 1), adiciona um ponto ao rascunho, re-renderiza — permite **múltiplos pontos por nota** (o usuário pode clicar várias vezes antes de salvar, todos os pontos ficam ligados à mesma anotação).
6. **Salvar**: exige texto não-vazio e ao menos 1 ponto (senão só foca a textarea, sem salvar). Reusa o `id` se estava editando uma existente (`session.selectedId`) ou gera um novo via `makeUuid()` prefixado `urn:ontobdc:annotation:`. Monta o objeto completo da anotação (incluindo `representationHash` calculado no passo 2, `dimension: context.dimensionUri`, `created` preservado se era edição ou `new Date().toISOString()` se nova). Atualiza/insere no array `annotations` em memória, persiste no arquivo (`persist`), habilita excluir, re-renderiza marcadores.
7. **Excluir**: remove a anotação selecionada do array, reseta o editor, persiste.
8. `close()` — remove o diálogo do DOM, libera a superfície (`dialogRelease`, ex. revoga object URL ou destrói o PDF), remove a classe do body, e **chama `context.onClose` se foi passado** (usado por `workstream_5w2h.js`, seção 9/12, para voltar ao modo "annotations" — visualização — depois de fechar o editor, mas só se o recurso selecionado na linha ainda for o mesmo que estava sendo anotado).
9. `Escape` no `keydown` global também fecha o diálogo, se aberto.

### 16.7 Visualização (sem edição) — `showPreview()`/`decoratePreview()`

Usada pelo modo "Anotações" da seção 8 (só **ver** as notas já existentes sobre o arquivo, sem abrir o editor completo em overlay/modal):
1. Limpa qualquer preview anterior naquele elemento (`clearPreview`, que consulta um `WeakMap` associando o elemento de preview ao seu `release` de superfície — permite múltiplas superfícies vivas simultaneamente, uma por preview element, sem vazar).
2. Carrega anotações, monta a superfície, filtra as anotações que casam com o contexto (`related`).
3. Monta um `<div class="...-preview-stage">` com a imagem/PDF de fundo e um overlay SVG com um marcador **por ponto** de cada anotação relacionada (não por anotação — se uma nota tem 3 pontos, aparecem 3 círculos clicáveis, todos abrindo o mesmo popover de nota).
4. Cada marcador, ao clicar (ou `Enter`/`Espaço`), abre um **popover** (`showNote`) posicionado percentualmente sobre a própria posição normalizada do ponto, mostrando cor + texto da nota; clicar de novo no mesmo marcador fecha (`hideNote`); classes `opens-left`/`opens-above` evitam o popover vazar para fora da tela quando o ponto está perto da borda direita/inferior (threshold `> 0.62`).
5. Clicar fora (no `stage`) ou `Escape` fecha o popover aberto.
6. Retorna a contagem de anotações relacionadas (`related.length`) — usada em algum lugar para exibir "N anotações" (não visto neste arquivo, mas o valor de retorno sugere consumo externo).

---

## Resumo das funcionalidades (checklist)

1. Persistência da permissão de pasta entre sessões (IndexedDB + File System Access API).
2. Reconexão silenciosa (sem diálogo) quando a permissão já foi concedida antes.
3. Tolerância a escolher a pasta-mãe em vez da pasta exata do contêiner.
4. Renderização inicial "grátis" a partir do JSON-LD embutido, antes de qualquer pasta ser conectada.
5. Parsing de planilha Excel (via Pyodide/openpyxl) para os 7 campos 5W2H, localizando a linha certa por `GlobalId`.
6. Mapeamento de colunas da planilha → campos do facade via linkset ICDD (`WorkStream.ttl`), com validação de completude.
7. Formatação leve de texto livre (negrito/itálico, listas numeradas/com marcadores) sem lib de markdown.
8. Catalogação de arquivos a partir de um RO-Crate + classificação em categorias via ontologia `file_display.ttl` (mimetype/extensão/tipo semântico).
9. Árvore de arquivos por categoria e por dimensão, com abas Relacionados/Sugeridos/Encontrados.
10. Preview de conteúdo por tipo: imagem, PDF, e-mail (.msg/.eml, com sanitização robusta de HTML), texto puro, fallback de metadados.
11. Fallback de preview para `.dwg` usando um `.png`/`.pdf` irmão gerado externamente.
12. Preview em tela cheia com fallback CSS quando a Fullscreen API real falha.
13. Relacionar/desrelacionar arquivo↔dimensão, gravando/removendo triplos ICDD Linkset via Pyodide+rdflib, com limpeza de nós órfãos e rollback em caso de erro de escrita.
14. Propagação de uma relação arquivo↔dimensão para a próxima dimensão da cadeia 5W2H.
15. Regeneração do catálogo RO-Crate a partir do sistema de arquivos real (botão "Atualizar"), ignorando pastas de metadados e datasets ICDD aninhados.
16. Anotações espaciais (pontos sobre imagem/PDF) com editor completo (criar/editar/excluir, múltiplos pontos por nota, múltiplas notas por arquivo) e modo de visualização somente-leitura com popovers.
17. Hash SHA-256 (nativo com fallback puro-JS) de cada arquivo anotado, para rastrear a versão exata anotada.
18. Serialização de anotações em Turtle com vocabulário Web Annotation + payload JSON redundante para leitura própria robusta.
19. Carregamento sob demanda do PDF.js (de CDN) — só quando o usuário realmente abre uma anotação sobre um PDF; `spatial_annotations.js` em si é carregado eager (junto com `workstream_5w2h.js`), não lazy, na página real (ver correção na seção 1).
20. Link explícito de volta à Surface principal (`#workstream-main-link`, "Voltar ao projeto"/"Voltar à página principal"), com `href` calculado conforme a página é acessada a partir de `view/work_stream/` ou de dentro do payload de um sub-dataset (seção 0.5).
21. Duas variantes de geração da página — WorkStream na raiz do projeto (sem `datasetPath`, sem JSON-LD embutido) vs. WorkStream dentro de um sub-dataset (`datasetPath` setado, JSON-LD embutido, paths prefixados) — controladas inteiramente pelo `payload` que o servidor injeta, não por lógica cliente (seção 0.5).
