# DEBUG SESSION — infobim-view-slow-crash

Session ID: `infobim-view-slow-crash`
Status: [OPEN]
Date opened: 2026-08-17
Opened by: Elias (production command `infobim view` on O&G client dataset)

---

## 🚨 Symptom

Running `infobim view --log-level debug` on O&G / LabSea2025 project exhibits two critical defects:

1.  **Unacceptable generation wall-time (~13 min 20 s end-to-end, 10:06 → 10:19)** with extreme hotspots on:
    - Matching presentation data vs. Component definitions + support envelopes: 23 s (10:06:55 → 10:07:28)
    - Assembling presentation tiles → layout: 59 s (10:07:35 → 10:08:34)
    - Embedding browser component implementations: 131 s (10:08:34 → 10:11:45)
    - Validating packaged offline HTML Surface: 144 s (10:11:45 → 10:14:09)
    - Publishing standalone entity detail pages: 201 s (10:16:27 → 10:19:54)
2.  **Browser crash** after opening the generated Surface: "This page isn't responding" (Chrome unresponsive-dialog, main thread blocked / JS loop / DOM explosion during tile render).

Project path (from screenshot — Windows machine, not local mac):
- `C:\Users\epaixao\OneDrive - Digicorner\Real Estate Brazil (Official)-Obras - Exp LabSea2025`
- Local mac counterpart (for code inspection only, no repro here):
  - `/Users/eliasmpjunior/Brasidata/07_Engenharia_e_Tecnologia/06_Solucoes_Reutilizaveis/OntoBDC/infobim`
  - `/Users/eliasmpjunior/Brasidata/07_Engenharia_e_Tecnologia/06_Solucoes_Reutilizaveis/OntoBDC/ontobdc` (shared Ontology / view / storage adapters)

---

## 🔬 Falsifiable Hypotheses

| # | Hypothesis | Predicted runtime evidence | Observation point |
|---|---|---|---|
| H1 | **`publish detail pages` (201 s) is O(N²) per entity or reads/writes each N files serially (no batching)**. N = number of BIM entities + documents + relationships ≥ some thousand; each iteration does a costly template re-render, a synchronous file open/close, or an inner scan. | Wall-time per page printed: ~linear growth or long tail; total syscalls of `open`/`write` ~N+; inner loop call-count to renderer per page > 1. | standalone page publish loop (find render module) |
| H2 | **`embed browser components` (131 s) concatenates / minifies / string-replaces a huge JS blob per component instead of reading once + inject once**. Worse: regex or string scan across the entire packed HTML, which grows with entity count. | Time per component grows with total HTML size; cumulative `len(html)` is copied or scanned hundreds of times. | embed step (find "Embedding Surface Browser component implementations") |
| H3 | **`validate packaged offline HTML` (144 s) parses the entire Surface HTML with a slow HTML parser N times (once per rule, or a full regex scan for every component)**. Or it loads the entire embedded JSON-LD payload into DOM memory twice without streaming. | Cumulative parse-count of HTML/JSON >> 1; time grows >linear with HTML byte-size. | validate step (find "Validating the packaged offline HTML Surface") |
| H4 | **`assembling tiles` (59 s) + `components match` (23 s) do a Cartesian-product match between (entities × regions × component envelopes × support conditions)**. O(E·R·C) without early break, caching, or index. | per-entity match iteration count scales with C (component count); condition re-evaluated multiple times per tuple. | match components + assemble tiles capabilities (two consecutive steps) |
| H5 | **Browser main-thread crash = DOM explosion + synchronous tree-walk on first paint**: Surface boot script creates a tile / node DOM element for every entity in the embedded JSON-LD, or runs a DFS through the full entity graph synchronously before yielding to the event loop (no requestIdleCallback / chunking). | JS heap grows >100MB on first paint; `Performance.navigation` timing shows blocking script >10 s; DOM node count before crash >50k; Chrome profiler shows a single long task >30 s in tile/entity loop. | embedded browser surface JS (find HTML template + inline JS render bootstrap) |

---

## 📏 Instrumentation Plan

- **Python (generation side)**: inject per-step wall-time + counters at each of 5 log boundaries + at each iteration of the inner loop (pages/components/tiles). Report **directly embedded in capability return-values `_dbg_*`**, which appear in the `--log-level debug` log output automatically (no Debug Server required on Windows).
- **JS (render side)**: wrap connectedCallback, first paint `#layout()`, `#itemsIn()`, `#itemsInRole()`, `#fitsRegionCapacity()` with counters + timers. Report via `console.debug()` and a global singleton `window.__ONTOBDC_SURFACE_DBG__` inspectable from Chrome DevTools.
- Reproduction: run once against the O&G dataset with instrumentation, collect logs, then compare hypotheses.

### Instrumented Python files (delimited by `#region debug-point (infobim-view-slow-crash)`)

| File | Step | Hypothesis | What is measured |
|---|---|---|---|
| `ontobdc/src/ontobdc/view/plugin/capability/transformation/surface_matched.py` | Matching presentation data (23 s) | H4 | `_auto_matched_requests` total subjects, total surfaceable, requests matched; seconds spent on `_is_surfaceable()` vs `_components.match()` vs resolve envelope; per-request time in `_with_resolved_tile()`. |
| `ontobdc/src/ontobdc/view/plugin/capability/transformation/surface_assembled.py` | Assembling tiles (59 s) | H3/H4 | Seconds per sub-step: read, extract matches, `assemble_surface_markup`, regex assembled attribute, set state marker, write, `require_check(is_surface_assembled)`. Includes snapshot of `surface_common._DBG_METRICS`. |
| `ontobdc/src/ontobdc/view/plugin/capability/transformation/surface_packaged.py` | Embedding components (131 s) | H2 | Seconds per sub-step: read, context adapter component_scripts, `_read_component_sources`, `embed_component_scripts`, state, write, `require_check(is_surface_packaged)`. Includes snapshot of `surface_common._DBG_METRICS`. |
| `ontobdc/src/ontobdc/view/plugin/check/surface_common.py` | *shared by all require_check calls (59s + 131s + 144s)* | H2/H3 | `has_assembled_tiles()`: seconds, number of regex scans (`per_tile_regex_searches`), document size in chars, matches count, early short-circuit reasons. Stored in module-global `_DBG_METRICS["has_assembled_tiles"]` for caller snapshot. |
| `ontobdc/src/ontobdc/view/plugin/capability/transformation/entity_views_published.py` | Standalone detail pages (201 s) | H1 | Total nodes, render_seconds_total (sum of `render_entity_view`), write_seconds_total (**sum of every fsync atomic_write call**), per-page averages (ms), skip counts (render None, result invalid), seconds per sub-step (read, loop, state, final write). |

### Instrumented JS file (delimited by `//#region debug-point (infobim-view-slow-crash)`)

| File | Symptom | Hypothesis | What is measured |
|---|---|---|---|
| `presentation/src/ontobdc_view/component/asset/onto-presentation-surface.js` | Main thread hang > 30 s → Chrome "This page isn't responding" | H5 | `DBG_SURFACE` singleton: `connectedCount`, `connectedWallMs` (total connect wall-time), `reconcileWallMs` (time walking N children on connect), `layoutCallCount`, `layoutFirstMs` (time of the first `#layout()`), `itemsInCallCount`, `itemsInRoleCallCount`, `fitsRegionCallCount`, `childrenCount`. Logged as `console.debug()` on connect, on first layout, and every 25th layout / any layout > 250 ms. Also available on `window.__ONTOBDC_SURFACE_DBG__` if you can open DevTools fast enough. |

---

## 🧭 REPRODUÇÃO — PASSO-A-PASSO PARA O USUÁRIO (WINDOWS / CLIENTE DE O&G)

**1. Garanta que os arquivos instrumentados estão instalados**

Se você estiver usando os fontes locais (editable install / `pip install -e .`), só o que foi salvo aqui já serve.
Se estiver usando uma wheel instalada globalmente, reinstale os pacotes `ontobdc` e `presentation` / `ontobdc_view` do repo atual ANTES de rodar.
Para rebuildar o JS instrumentado: rode o build do `presentation` (ex: `npm run build` ou `task presentation:build` — o mesmo comando você já usa hoje) para que os scripts sejam empacotados no wheel / pasta de componentes antes do próximo `infobim view`.

**2. Rode o comando com log redirecionado para arquivo (evita perder no terminal):**

```powershell
# No PowerShell (Windows), dentro do diretório do projeto (LabSea2025):
$DebugPreference = "Continue"
infobim view --log-level debug *>&1 | Tee-Object -FilePath "infobim-view-dbg-labsea2025.log"
```

Ele vai demorar os mesmos ~13 minutos de sempre. O `Tee-Object` garante que você vê na tela e salva em arquivo simultaneamente.

**3. Depois que o comando terminar (antes de abrir qualquer navegador), abra o log e COPIE (screenshot ou select+copy) as linhas FINAL de cada capability que contêm `Output keys:` — ou qualquer linha que contenha `_dbg_`**.
As linhas são do formato:
```
INFO Transformation capability completed successfully.  Capability: SurfaceMatchedCapability.  Id: org.ontobdc.view.plugin.capability.transformation.target.surface_matched.  Output keys: [_dbg_auto_match, _dbg_requests_explicit, _dbg_requests_total, _dbg_resolve_tile, _dbg_seconds_total, match_count, resulting_state, surface_path].  Total outputs: 8.
```
Se você habilitar `--log-level trace` (ou DEBUG), os valores dessas chaves `_dbg_*` devem aparecer no log logo antes/depois dessa linha. Se não aparecer, procure na seção 5 abaixo um snippet de `json.dumps` manual que eu botei no capability runner, ou simplesmente me envie o arquivo `.log` TODO.

**4. AGORA ABRA O SURFACE HTML GERADO (index.html) — mas ANTES do Chrome travar, abra o DevTools:**

Truque para pegar os dados ANTES do hang:
- Clique no `index.html` com botão direito → Abrir com Chrome.
- IMEDIATAMENTE após apertar Enter, pressione **F12** (ou Ctrl+Shift+I) para abrir o DevTools. Vá direto para a aba **Console**.
- Na barra de levels do Console (Default levels), certifique-se que **Verbose** está LIGADO (senão os `console.debug` ficam ocultos).
- Copie TODAS as linhas do Console que começam com `[OntoBDC Surface][DBG]`. Elas são a prova H5.
- Se mesmo assim a página travar antes de você ver as linhas:
  - No DevTools → aba Sources, clique em ⏸ (Pause script execution) OU pressione **Ctrl+\\** (Windows). Isso pausa o loop infinito síncrono. Depois volte para Console, digite `window.__ONTOBDC_SURFACE_DBG__` e Enter. Copie o objeto retornado. Ele contém TODOS os contadores H5.
  - Outro jeito: adicione `?ontodbgpause=1` na URL do index.html antes de carregar (ex: `file:///C:/.../index.html?ontodbgpause=1`). Depois, no Console do DevTools (depois de pausar), digite manualmente `window.__ONTOBDC_SURFACE_DBG__`.

**5. Me envie 2 arquivos:**

1. `infobim-view-dbg-labsea2025.log` (saída completa do `infobim view --log-level debug`)
2. Um screenshot / texto do Console do Chrome, OU só o objeto `window.__ONTOBDC_SURFACE_DBG__` copiado do DevTools.

---

## 📊 Evidence Log

(Empty — to populate after instrumentation run)

---

## 🔧 Minimal Fix Plan

Only after ≥1 hypothesis is CONFIRMED by evidence:

- If H1: batch template + batch file writes, avoid re-reading base template per entity
- If H2: one-pass string substitution / concatenation in memory for all components, no per-component regex over entire HTML
- If H3: parse HTML/JSON-LD ONCE into memory, run all rules against the AST, re-validate checksum only
- If H4: build an inverted index of component applicability keys, or vectorize entity→region→tile assignment in O(E + R + C)
- If H5: chunked tile creation / graph walk, virtualize the DOM (render only viewport tiles on demand), or paginate entity lists.

---

## 🧪 Pre vs Post Verification Metrics

| Metric | Pre (expected) | Post (target) | Status |
|---|---|---|---|
| End-to-end `infobim view` | ~800 s (13:20) | ≤ 180 s (3 min) — 4.5× speedup min | TBD |
| Component match | 23 s | ≤ 3 s | TBD |
| Tiles assemble | 59 s | ≤ 10 s | TBD |
| Embed components | 131 s | ≤ 15 s | TBD |
| Validate HTML | 144 s | ≤ 15 s | TBD |
| Publish standalone pages | 201 s | ≤ 45 s | TBD |
| Browser TTI (time to interactive on open) | main thread blocked >30 s (hang dialog) | ≤ 5 s, no unresponsive dialog | TBD |
| Peak browser DOM nodes | TBD | ≤ 10k in steady state | TBD |

---

## ⚙️ Debug Server

- URL: TBD (after starting server)
- Log file: `trae-debug-log-infobim-view-slow-crash.ndjson`
- Env file: `.dbg/infobim-view-slow-crash.env`

---

## 🚩 Status

[OPEN] — Session opened. Next step: locate the 5 Python capability modules + the frontend bootstrap, then add instrumentation.
