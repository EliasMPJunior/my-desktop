(function () {
  "use strict";

  const forecastEndpoint = "https://api.open-meteo.com/v1/forecast";
  const runtimeData = window.infoBimProjectRuntimeData || {};
  const cardDefinitions = [
    { key: "current", id: "project-weather-current-card", label: "Tempo na obra" },
    { key: "rain", id: "project-weather-rain-card", label: "Chuva 6h" },
    { key: "gust", id: "project-weather-gust-card", label: "Rajada 6h" },
  ];

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

  function numericDataGrid() {
    return document.querySelector('[data-card="numeric-data-grid"]');
  }

  function createWeatherCard(definition) {
    const card = createElement("div", "view-badge weather-card is-loading");
    card.id = definition.id;
    card.dataset.card = "weather-card";
    card.dataset.weatherMetric = definition.key;
    card.setAttribute("aria-live", "polite");

    const label = createElement("span", "view-badge-label", definition.label);
    const value = createElement("strong", "weather-card-value", "—");
    value.dataset.weatherValue = definition.key;
    const detail = createElement("span", "weather-card-detail", "Carregando...");
    detail.dataset.weatherDetail = definition.key;
    const footer = createElement("span", "weather-card-footer", "");
    footer.dataset.weatherFooter = definition.key;

    card.append(label, value, detail, footer);
    return card;
  }

  function ensureWeatherCards() {
    const grid = numericDataGrid();
    if (!grid) {
      return null;
    }

    grid.querySelectorAll('[data-card="weather-card"]').forEach((card) => {
      card.remove();
    });

    const cards = {};
    cardDefinitions.forEach((definition) => {
      const card = createWeatherCard(definition);
      grid.appendChild(card);
      cards[definition.key] = {
        card,
        value: card.querySelector(`[data-weather-value="${definition.key}"]`),
        detail: card.querySelector(`[data-weather-detail="${definition.key}"]`),
        footer: card.querySelector(`[data-weather-footer="${definition.key}"]`),
      };
    });
    return cards;
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

  function setCardValue(element, value, unit) {
    element.textContent = "";
    element.appendChild(document.createTextNode(value));
    if (unit) {
      element.appendChild(createElement("span", "weather-card-unit", unit));
    }
  }

  function setCardContent(elements, state, value, detail, footer, unit) {
    setCardState(elements, state);
    setCardValue(elements.value, value, unit);
    elements.detail.textContent = detail;
    elements.footer.textContent = footer;
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

  function renderMissing(cards) {
    setCardContent(
      cards.current,
      "is-missing",
      "—",
      "Localização não definida",
      "",
    );
    setCardContent(
      cards.rain,
      "is-missing",
      "—",
      "Sem previsão",
      "Próximas 6 horas",
    );
    setCardContent(
      cards.gust,
      "is-missing",
      "—",
      "Sem previsão",
      "Próximas 6 horas",
    );
  }

  function renderError(cards, error) {
    const message = error instanceof Error
      ? error.message
      : String(error || "Serviço indisponível");
    setCardContent(cards.current, "is-error", "—", "Previsão indisponível", message);
    setCardContent(cards.rain, "is-error", "—", "Sem previsão", "Serviço indisponível");
    setCardContent(cards.gust, "is-error", "—", "Sem previsão", "Serviço indisponível");
  }

  function buildForecastUrl(location) {
    const parameters = new URLSearchParams({
      latitude: String(location.latitude),
      longitude: String(location.longitude),
      timezone: "auto",
      current: ["temperature_2m", "weather_code"].join(","),
      hourly: ["precipitation_probability", "wind_gusts_10m"].join(","),
      daily: ["temperature_2m_max", "temperature_2m_min"].join(","),
      forecast_days: "2",
    });
    return `${forecastEndpoint}?${parameters.toString()}`;
  }

  function weatherDescription(code) {
    const descriptions = new Map([
      [0, "Céu limpo"], [1, "Predomínio de sol"], [2, "Parcialmente nublado"],
      [3, "Nublado"], [45, "Neblina"], [48, "Neblina com geada"],
      [51, "Garoa fraca"], [53, "Garoa"], [55, "Garoa forte"],
      [56, "Garoa congelante"], [57, "Garoa congelante forte"],
      [61, "Chuva fraca"], [63, "Chuva"], [65, "Chuva forte"],
      [66, "Chuva congelante"], [67, "Chuva congelante forte"],
      [71, "Neve fraca"], [73, "Neve"], [75, "Neve forte"],
      [77, "Grãos de neve"], [80, "Pancadas fracas"],
      [81, "Pancadas de chuva"], [82, "Pancadas fortes"],
      [85, "Pancadas de neve"], [86, "Pancadas fortes de neve"],
      [95, "Trovoadas"], [96, "Trovoadas com granizo"],
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
    return Number.isFinite(value) ? `${Math.round(value)}${suffix}` : "—";
  }

  function temperatureRange(data) {
    const maximumTemperature = Number(
      data.daily && data.daily.temperature_2m_max && data.daily.temperature_2m_max[0],
    );
    const minimumTemperature = Number(
      data.daily && data.daily.temperature_2m_min && data.daily.temperature_2m_min[0],
    );
    if (!Number.isFinite(maximumTemperature) || !Number.isFinite(minimumTemperature)) {
      return "Hoje";
    }
    return `Máx. ${Math.round(maximumTemperature)}° · Mín. ${Math.round(minimumTemperature)}°`;
  }

  function renderForecast(cards, data) {
    const temperature = Number(data.current && data.current.temperature_2m);
    const rainProbability = maximum(nextHours(data, "precipitation_probability", 6));
    const windGust = maximum(nextHours(data, "wind_gusts_10m", 6));

    setCardContent(
      cards.current,
      "is-ready",
      formatNumber(temperature, "°"),
      weatherDescription(data.current && data.current.weather_code),
      temperatureRange(data),
    );
    setCardContent(
      cards.rain,
      "is-ready",
      formatNumber(rainProbability, "%"),
      "Probabilidade máxima",
      "Próximas 6 horas",
    );
    setCardContent(
      cards.gust,
      "is-ready",
      formatNumber(windGust, ""),
      "Máxima prevista",
      "Próximas 6 horas",
      "km/h",
    );
  }

  async function loadForecast(cards, location) {
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
    renderForecast(cards, data);
  }

  const cards = ensureWeatherCards();
  if (!cards) {
    return;
  }
  if (!validLocation(runtimeData.location)) {
    renderMissing(cards);
    return;
  }
  loadForecast(cards, runtimeData.location).catch((error) => {
    console.error(error);
    renderError(cards, error);
  });
}());
