(function () {
  "use strict";

  const cardId = "project-weather-card";
  const forecastEndpoint = "https://api.open-meteo.com/v1/forecast";
  const runtimeData = window.infoBimProjectRuntimeData || {};

  function createElement(tagName, className, text) {
    const element = document.createElement(tagName);
    if (className) {
      element.className = className;
    }
    if (text !== undefined) {
      element.textContent = text;
    }
    return element;
  }

  function createMetric(label, id) {
    const metric = createElement("span", "weather-card-metric");
    const metricLabel = createElement(
      "span",
      "weather-card-metric-label",
      label,
    );
    const metricValue = createElement(
      "strong",
      "weather-card-metric-value",
      "—",
    );
    metricValue.id = id;
    metric.append(metricLabel, metricValue);
    return metric;
  }

  function numericDataGrid() {
    return document.querySelector('[data-card="numeric-data-grid"]');
  }

  function createCard() {
    const grid = numericDataGrid();
    if (!grid) {
      return null;
    }

    const existing = document.getElementById(cardId);
    if (existing) {
      return existing;
    }

    grid.querySelectorAll('[data-card="weather-card"]').forEach((card) => {
      card.remove();
    });

    const card = createElement("div", "view-badge weather-card is-loading");
    card.id = cardId;
    card.dataset.card = "weather-card";
    card.setAttribute("aria-live", "polite");

    const label = createElement("span", "view-badge-label", "Tempo na obra");
    const main = createElement("div", "weather-card-main");
    const temperature = createElement(
      "strong",
      "weather-card-temperature",
      "—",
    );
    temperature.id = "weather-temperature";
    const condition = createElement(
      "span",
      "weather-card-condition",
      "Verificando localização IFC...",
    );
    condition.id = "weather-condition";
    main.append(temperature, condition);

    const metrics = createElement("div", "weather-card-metrics");
    metrics.append(
      createMetric("Chuva 6h", "weather-rain"),
      createMetric("Rajada 6h", "weather-gust"),
    );

    const footer = createElement("span", "weather-card-footer", "");
    footer.id = "weather-footer";

    card.append(label, main, metrics, footer);
    grid.appendChild(card);
    return card;
  }

  function cardElements(card) {
    return {
      card,
      temperature: card.querySelector("#weather-temperature"),
      condition: card.querySelector("#weather-condition"),
      rain: card.querySelector("#weather-rain"),
      gust: card.querySelector("#weather-gust"),
      footer: card.querySelector("#weather-footer"),
    };
  }

  function setCardState(elements, state) {
    elements.card.classList.remove(
      "is-loading",
      "is-ready",
      "is-missing",
      "is-error",
    );
    elements.card.classList.add(state);
  }

  function validLocation(value) {
    if (!value || typeof value !== "object") {
      return false;
    }
    const latitude = Number(value.latitude);
    const longitude = Number(value.longitude);
    return (
      Number.isFinite(latitude)
      && Number.isFinite(longitude)
      && latitude >= -90
      && latitude <= 90
      && longitude >= -180
      && longitude <= 180
    );
  }

  function renderMissing(elements) {
    setCardState(elements, "is-missing");
    elements.temperature.textContent = "—";
    elements.condition.textContent = "Localização IFC não definida";
    elements.rain.textContent = "—";
    elements.gust.textContent = "—";
    elements.footer.textContent = runtimeData.locationSource
      || "IfcSite.RefLatitude / RefLongitude";
  }

  function renderError(elements, error) {
    setCardState(elements, "is-error");
    elements.temperature.textContent = "—";
    elements.condition.textContent = "Previsão indisponível";
    elements.rain.textContent = "—";
    elements.gust.textContent = "—";
    elements.footer.textContent = error instanceof Error
      ? error.message
      : String(error || "Erro ao consultar o serviço meteorológico.");
  }

  function buildForecastUrl(location) {
    const parameters = new URLSearchParams({
      latitude: String(location.latitude),
      longitude: String(location.longitude),
      timezone: "auto",
      current: [
        "temperature_2m",
        "weather_code",
      ].join(","),
      hourly: [
        "precipitation_probability",
        "wind_gusts_10m",
      ].join(","),
      daily: [
        "temperature_2m_max",
        "temperature_2m_min",
      ].join(","),
      forecast_days: "2",
    });
    return `${forecastEndpoint}?${parameters.toString()}`;
  }

  function weatherDescription(code) {
    const descriptions = new Map([
      [0, "Céu limpo"],
      [1, "Predomínio de sol"],
      [2, "Parcialmente nublado"],
      [3, "Nublado"],
      [45, "Neblina"],
      [48, "Neblina com geada"],
      [51, "Garoa fraca"],
      [53, "Garoa"],
      [55, "Garoa forte"],
      [56, "Garoa congelante"],
      [57, "Garoa congelante forte"],
      [61, "Chuva fraca"],
      [63, "Chuva"],
      [65, "Chuva forte"],
      [66, "Chuva congelante"],
      [67, "Chuva congelante forte"],
      [71, "Neve fraca"],
      [73, "Neve"],
      [75, "Neve forte"],
      [77, "Grãos de neve"],
      [80, "Pancadas fracas"],
      [81, "Pancadas de chuva"],
      [82, "Pancadas fortes"],
      [85, "Pancadas de neve"],
      [86, "Pancadas fortes de neve"],
      [95, "Trovoadas"],
      [96, "Trovoadas com granizo"],
      [99, "Trovoadas fortes com granizo"],
    ]);
    return descriptions.get(Number(code)) || "Condição meteorológica";
  }

  function nextHours(data, field, hourCount) {
    const times = Array.isArray(data.hourly && data.hourly.time)
      ? data.hourly.time
      : [];
    const values = Array.isArray(data.hourly && data.hourly[field])
      ? data.hourly[field]
      : [];
    if (!times.length || !values.length) {
      return [];
    }

    const currentTime = String(data.current && data.current.time || times[0]);
    const foundIndex = times.findIndex((time) => String(time) >= currentTime);
    const startIndex = foundIndex >= 0 ? foundIndex : 0;
    return values
      .slice(startIndex, startIndex + hourCount)
      .map(Number)
      .filter(Number.isFinite);
  }

  function maximum(values) {
    return values.length ? Math.max(...values) : null;
  }

  function formatNumber(value, suffix) {
    return Number.isFinite(value)
      ? `${Math.round(value)}${suffix}`
      : "—";
  }

  function forecastFooter(data) {
    const maximumTemperature = Number(
      data.daily
      && data.daily.temperature_2m_max
      && data.daily.temperature_2m_max[0],
    );
    const minimumTemperature = Number(
      data.daily
      && data.daily.temperature_2m_min
      && data.daily.temperature_2m_min[0],
    );
    if (
      !Number.isFinite(maximumTemperature)
      || !Number.isFinite(minimumTemperature)
    ) {
      return "";
    }
    return `Máx. ${Math.round(maximumTemperature)}° · Mín. ${Math.round(minimumTemperature)}°`;
  }

  function renderForecast(elements, data) {
    const temperature = Number(data.current && data.current.temperature_2m);
    const rainProbability = maximum(
      nextHours(data, "precipitation_probability", 6),
    );
    const windGust = maximum(nextHours(data, "wind_gusts_10m", 6));

    setCardState(elements, "is-ready");
    elements.temperature.textContent = formatNumber(temperature, "°");
    elements.condition.textContent = weatherDescription(
      data.current && data.current.weather_code,
    );
    elements.rain.textContent = formatNumber(rainProbability, "%");
    elements.gust.textContent = formatNumber(windGust, " km/h");
    elements.footer.textContent = forecastFooter(data);
  }

  async function loadForecast(elements, location) {
    const response = await fetch(buildForecastUrl(location), {
      headers: { Accept: "application/json" },
    });
    if (!response.ok) {
      throw new Error(`Serviço meteorológico: HTTP ${response.status}`);
    }
    const data = await response.json();
    if (!data || !data.current) {
      throw new Error("Resposta meteorológica sem condições atuais.");
    }
    renderForecast(elements, data);
  }

  const card = createCard();
  if (!card) {
    return;
  }
  const elements = cardElements(card);
  if (!validLocation(runtimeData.location)) {
    renderMissing(elements);
    return;
  }

  loadForecast(elements, runtimeData.location).catch((error) => {
    console.error(error);
    renderError(elements, error);
  });
}());
