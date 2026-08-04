window.infoBimProjectRuntimeData = window.infoBimProjectRuntimeData || {};

if (!window.infoBimProjectRuntimeData.location) {
  window.infoBimProjectRuntimeData.location = {
    "latitude": -22.868585,
    "longitude": -43.214664
  };
}

if (!window.infoBimProjectRuntimeData.absolutePath) {
  window.infoBimProjectRuntimeData.absolutePath = "C:\\Users\\EliasMagalhães\\Documents\\Brasidata\\06_Projetos\\01_Projetos_Ativos\\my-desktop\\techcenter-doc";
}

(function () {
  "use strict";

  const runtimeData = window.infoBimProjectRuntimeData || {};
  const card = document.querySelector('[data-card="project-information-card"]');

  if (!card) {
    return;
  }

  function metadataList() {
    return card.querySelector(".metadata-list");
  }

  function metadataRowByLabel(label) {
    return Array.from(card.querySelectorAll(".metadata-row")).find((row) => {
      const term = row.querySelector("dt");
      return term && term.textContent.trim().toLocaleLowerCase("pt-BR") === label.toLocaleLowerCase("pt-BR");
    }) || null;
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

  function configuredAbsolutePath() {
    const value = String(runtimeData.absolutePath || "").trim();
    return value;
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
      || configuredAbsolutePath()
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

    let row = metadataRowByLabel("Geolocalização");
    if (row) {
      return row;
    }

    row = document.createElement("div");
    row.className = "metadata-row";

    const term = document.createElement("dt");
    term.textContent = "Geolocalização";
    const description = document.createElement("dd");

    row.append(term, description);
    list.appendChild(row);
    return row;
  }

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

  renderAbsolutePath();
  renderGeolocation();
}());
