(function () {
  "use strict";

  const calendarDayCount = 11;
  const previousBusinessDays = 5;
  const nextBusinessDays = 5;
  const locale = "pt-BR";
  const runtimeData = window.infoBimWorkStreamData || null;

  function projectTabsCard() {
    return document.querySelector('[data-card="project-tabs-card"]');
  }

  function panelHeader(card) {
    return card ? card.querySelector(".view-panel-head") : null;
  }

  function tabNavigation(card) {
    return card ? card.querySelector("[data-project-tablist]") : null;
  }

  function tabContent(card) {
    return card ? card.querySelector(".project-tabs-content") : null;
  }

  function replacePanelHeading(card) {
    const header = panelHeader(card);
    if (!header) {
      return;
    }
    const title = header.querySelector(".view-panel-title");
    const description = header.querySelector(".view-panel-copy");
    if (title) {
      title.textContent = "Frentes de Trabalho";
    }
    if (description) {
      description.textContent =
        "Acompanhe as frentes do projeto em uma janela móvel de duas semanas.";
    }
  }

  function createSingleTab() {
    const button = document.createElement("button");
    button.className = "project-tab";
    button.type = "button";
    button.id = "project-tab-workstreams";
    button.setAttribute("role", "tab");
    button.setAttribute("aria-selected", "true");
    button.setAttribute("aria-controls", "project-tab-panel-workstreams");
    button.setAttribute("tabindex", "0");
    button.dataset.tabId = "workstreams";

    const icon = document.createElement("span");
    icon.className = "project-tab-icon";
    icon.setAttribute("aria-hidden", "true");
    icon.textContent = "≋";

    const label = document.createElement("span");
    label.textContent = "Frentes de Trabalho";

    button.append(icon, label);
    return button;
  }

  function replaceTabNavigation(card) {
    const navigation = tabNavigation(card);
    if (!navigation) {
      return;
    }
    navigation.setAttribute("aria-label", "Frentes de Trabalho");
    navigation.replaceChildren(createSingleTab());
  }

  function createBoardPanel() {
    const panel = document.createElement("section");
    panel.className = "project-tab-panel";
    panel.id = "project-tab-panel-workstreams";
    panel.setAttribute("role", "tabpanel");
    panel.setAttribute("aria-labelledby", "project-tab-workstreams");
    panel.setAttribute("tabindex", "0");

    const scroll = document.createElement("div");
    scroll.className = "workstream-board-scroll";

    const board = document.createElement("div");
    board.className = "workstream-board";
    board.dataset.workstreamBoard = "";

    scroll.appendChild(board);
    panel.appendChild(scroll);
    return panel;
  }

  function replaceTabContent(card) {
    const content = tabContent(card);
    if (!content) {
      return null;
    }
    const panel = createBoardPanel();
    content.replaceChildren(panel);
    return panel.querySelector("[data-workstream-board]");
  }

  function normalizeDate(value) {
    return new Date(value.getFullYear(), value.getMonth(), value.getDate());
  }

  function isBusinessDay(value) {
    const weekday = value.getDay();
    return weekday !== 0 && weekday !== 6;
  }

  function moveBusinessDay(value, direction) {
    const next = new Date(value);
    do {
      next.setDate(next.getDate() + direction);
    } while (!isBusinessDay(next));
    return next;
  }

  function previousDays(today) {
    const values = [];
    let cursor = new Date(today);
    for (let index = 0; index < previousBusinessDays; index += 1) {
      cursor = moveBusinessDay(cursor, -1);
      values.unshift(new Date(cursor));
    }
    return values;
  }

  function followingDays(today) {
    const values = [];
    let cursor = new Date(today);
    for (let index = 0; index < nextBusinessDays; index += 1) {
      cursor = moveBusinessDay(cursor, 1);
      values.push(new Date(cursor));
    }
    return values;
  }

  function calendarWindow() {
    const today = normalizeDate(new Date());
    return [...previousDays(today), today, ...followingDays(today)];
  }

  function sameDate(first, second) {
    return (
      first.getFullYear() === second.getFullYear()
      && first.getMonth() === second.getMonth()
      && first.getDate() === second.getDate()
    );
  }

  function weekdayLabel(value) {
    return new Intl.DateTimeFormat(locale, { weekday: "short" })
      .format(value)
      .replace(".", "");
  }

  function dayLabel(value) {
    return new Intl.DateTimeFormat(locale, {
      day: "2-digit",
      month: "2-digit",
    }).format(value);
  }

  function monthLabel(value) {
    return new Intl.DateTimeFormat(locale, { month: "short" })
      .format(value)
      .replace(".", "");
  }

  function createCell(className) {
    const cell = document.createElement("div");
    cell.className = `workstream-board-cell ${className}`;
    return cell;
  }

  function createBoardHeading(workstreamCount) {
    const heading = createCell("workstream-board-heading");
    const title = document.createElement("strong");
    title.textContent = "Frentes de trabalho";
    const subtitle = document.createElement("span");
    subtitle.textContent = workstreamCount === 1
      ? "1 frente publicada"
      : `${workstreamCount} frentes publicadas`;
    heading.append(title, subtitle);
    return heading;
  }

  function createCalendarHeading(date, today) {
    const cell = createCell("workstream-calendar-day");
    if (sameDate(date, today)) {
      cell.classList.add("is-today");
    }

    const weekday = document.createElement("abbr");
    weekday.textContent = weekdayLabel(date);
    weekday.title = new Intl.DateTimeFormat(locale, { weekday: "long" }).format(date);

    const day = document.createElement("strong");
    day.textContent = dayLabel(date);

    const month = document.createElement("span");
    month.textContent = sameDate(date, today) ? "Hoje" : monthLabel(date);

    cell.append(weekday, day, month);
    return cell;
  }

  function workstreamList(payload) {
    if (!payload || typeof payload !== "object") {
      return [];
    }
    if (Array.isArray(payload.workstreams)) {
      return payload.workstreams;
    }
    if (Array.isArray(payload["schema:hasPart"])) {
      return payload["schema:hasPart"];
    }
    return [];
  }

  function textValue(item, keys, fallback) {
    for (const key of keys) {
      const value = item && item[key];
      if (typeof value === "string" && value.trim()) {
        return value.trim();
      }
    }
    return fallback;
  }

  function workstreamName(item) {
    return textValue(item, ["name", "schema:name"], "WorkStream");
  }

  function workstreamDescription(item) {
    return textValue(
      item,
      ["description", "schema:description"],
      "Sem descrição publicada.",
    );
  }

  function workstreamStatus(item) {
    return textValue(item, ["status", "schema:status"], "Abrir frente");
  }

  function workstreamView(item) {
    return textValue(item, ["view", "schema:url"], "");
  }

  function createWorkstreamCell(item) {
    const cell = createCell("workstream-board-workstream");
    const view = workstreamView(item);
    const link = document.createElement(view ? "a" : "div");
    link.className = "workstream-board-link";
    if (view) {
      link.href = view;
    }

    const name = document.createElement("strong");
    name.textContent = workstreamName(item);

    const description = document.createElement("p");
    description.textContent = workstreamDescription(item);

    const status = document.createElement("span");
    status.textContent = workstreamStatus(item);

    link.append(name, description, status);
    cell.appendChild(link);
    return cell;
  }

  function createCalendarSlot(date, today) {
    const slot = createCell("workstream-calendar-slot");
    if (sameDate(date, today)) {
      slot.classList.add("is-today");
    }
    slot.dataset.date = date.toISOString().slice(0, 10);
    return slot;
  }

  function renderHeader(board, dates, workstreamCount) {
    const today = normalizeDate(new Date());
    board.appendChild(createBoardHeading(workstreamCount));
    dates.forEach((date) => {
      board.appendChild(createCalendarHeading(date, today));
    });
  }

  function renderWorkstreamRow(board, item, dates) {
    const today = normalizeDate(new Date());
    board.appendChild(createWorkstreamCell(item));
    dates.forEach((date) => {
      board.appendChild(createCalendarSlot(date, today));
    });
  }

  function createGeneralScheduleLabel() {
    const cell = createCell("general-schedule-label");
    const title = document.createElement("strong");
    title.textContent = "Cronograma Geral";
    const subtitle = document.createElement("span");
    subtitle.textContent = "3 linhas simuladas";
    cell.append(title, subtitle);
    return cell;
  }

  function createMockScheduleBar(row, start, span) {
    const bar = document.createElement("span");
    bar.className = "general-schedule-mock-bar";
    bar.dataset.mock = "true";
    bar.setAttribute("aria-hidden", "true");
    bar.style.gridRow = String(row);
    bar.style.gridColumn = `${start} / span ${span}`;
    return bar;
  }

  function createGeneralScheduleTimeline() {
    const timeline = createCell("general-schedule-timeline");
    timeline.setAttribute(
      "aria-label",
      "Cronograma Geral com três linhas de barras simuladas",
    );
    timeline.append(
      createMockScheduleBar(1, 1, 4),
      createMockScheduleBar(2, 4, 5),
      createMockScheduleBar(3, 8, 3),
    );
    return timeline;
  }

  function renderGeneralScheduleRow(board) {
    board.append(
      createGeneralScheduleLabel(),
      createGeneralScheduleTimeline(),
    );
  }

  function renderEmptyState(board, message) {
    const state = document.createElement("div");
    state.className = "workstream-board-state";
    const text = document.createElement("p");
    text.textContent = message;
    state.appendChild(text);
    board.appendChild(state);
  }

  function renderBoard(board, payload) {
    const dates = calendarWindow();
    const workstreams = workstreamList(payload);

    if (dates.length !== calendarDayCount) {
      throw new Error("A janela do calendário deve conter 11 dias úteis.");
    }

    board.replaceChildren();
    renderHeader(board, dates, workstreams.length);

    if (!payload) {
      renderEmptyState(board, "Frentes de trabalho ainda não publicadas.");
      return;
    }

    if (!workstreams.length) {
      renderEmptyState(board, "Nenhuma frente de trabalho cadastrada.");
      return;
    }

    workstreams.forEach((item) => {
      renderWorkstreamRow(board, item, dates);
    });
    renderGeneralScheduleRow(board);
  }

  function initialize() {
    const card = projectTabsCard();
    if (!card) {
      return;
    }

    replacePanelHeading(card);
    replaceTabNavigation(card);
    const board = replaceTabContent(card);
    if (!board) {
      return;
    }

    card.dataset.workstreamBoardReady = "true";
    renderBoard(board, runtimeData);
  }

  initialize();
}());
