(async function () {
  const bootstrapScript = document.currentScript;
  const statusDot = document.getElementById("pyodide-status-dot");
  const statusLabel = document.getElementById("pyodide-status-label");
  const consoleElement = document.getElementById("pyodide-console");
  const projectPayload = window.infoBimProjectDashboard || {};

  function moduleUrl(relativePath) {
    if (!bootstrapScript || !bootstrapScript.src) {
      throw new Error("Dashboard bootstrap URL unavailable.");
    }
    return new URL(relativePath, bootstrapScript.src).href;
  }

  function loadScript(relativePath) {
    return new Promise((resolve, reject) => {
      const url = moduleUrl(relativePath);
      const existing = document.querySelector(`script[src="${url}"]`);
      if (existing) {
        if (existing.dataset.loaded === "true") {
          resolve();
          return;
        }
        existing.addEventListener("load", resolve, { once: true });
        existing.addEventListener("error", reject, { once: true });
        return;
      }

      const script = document.createElement("script");
      script.src = url;
      script.async = false;
      script.addEventListener("load", () => {
        script.dataset.loaded = "true";
        resolve();
      }, { once: true });
      script.addEventListener("error", () => {
        reject(new Error(`Não foi possível carregar ${relativePath}.`));
      }, { once: true });
      document.head.appendChild(script);
    });
  }

  function loadStyle(relativePath) {
    const url = moduleUrl(relativePath);
    if (document.querySelector(`link[href="${url}"]`)) {
      return;
    }
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = url;
    document.head.appendChild(link);
  }

  function hasEmbeddedWorkstreamJsonLd() {
    return Boolean(document.getElementById("work-stream-jsonld"));
  }

  async function loadLegacyWorkstreamDataWhenNeeded() {
    if (!hasEmbeddedWorkstreamJsonLd()) {
      await loadScript("work_stream_runtime_data.js");
    }
  }

  async function loadWorkstreamBoardModule() {
    loadStyle("../css/workstream_board.css");
    await loadLegacyWorkstreamDataWhenNeeded();
    await loadScript("workstream_board.js");
  }

  function writeStatus(message, cssClass) {
    if (statusLabel) {
      statusLabel.textContent = message;
    }
    if (statusDot) {
      statusDot.classList.remove("is-ready", "is-error");
      if (cssClass) {
        statusDot.classList.add(cssClass);
      }
    }
  }

  function writeConsole(message) {
    if (consoleElement) {
      consoleElement.textContent = message;
    }
  }

  try {
    await loadWorkstreamBoardModule();
  } catch (error) {
    console.error("Dashboard module initialization failed.", error);
  }

  writeStatus("Loading Pyodide runtime...", "");
  writeConsole("Preparing browser Python runtime...");

  if (typeof loadPyodide !== "function") {
    writeStatus("Pyodide loader unavailable", "is-error");
    writeConsole(
      [
        "The page loaded, but the Pyodide loader was not found.",
        "Check internet connectivity or host the Pyodide distribution locally.",
      ].join("\n"),
    );
    return;
  }

  try {
    const pyodide = await loadPyodide();
    pyodide.globals.set("project_payload_json", JSON.stringify(projectPayload));
    const runtimeReport = await pyodide.runPythonAsync(`
import json
import platform

payload = json.loads(project_payload_json)
lines = [
    f"Python runtime: {platform.python_version()}",
    f"Project ID: {payload.get('projectId', '')}",
    f"Name: {payload.get('name', '')}",
    f"Path: {payload.get('path', '')}",
]
"\\n".join(lines)
`);

    writeStatus("Pyodide runtime ready", "is-ready");
    writeConsole(String(runtimeReport));
  } catch (error) {
    writeStatus("Pyodide initialization failed", "is-error");
    writeConsole(String(error));
  }
}());
