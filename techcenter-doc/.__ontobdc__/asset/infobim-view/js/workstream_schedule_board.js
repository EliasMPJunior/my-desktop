(function () {
  "use strict";

  const relationMap = window.infoBimWorkStreamScheduleRelations || {};
  const locale = "pt-BR";
  const previousBusinessDays = 5;
  const nextBusinessDays = 5;

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

  function calendarWindow() {
    const today = normalizeDate(new Date());
    const previous = [];
    let cursor = new Date(today);
    for (let index = 0; index < previousBusinessDays; index += 1) {
      cursor = moveBusinessDay(cursor, -1);
      previous.unshift(new Date(cursor));
    }
    const following = [];
    cursor = new Date(today);
    for (let index = 0; index < nextBusinessDays; index += 1) {
      cursor = moveBusinessDay(cursor, 1);
      following.push(new Date(cursor));
    }
    return [...previous, today, ...following];
  }

  function localName(value) {
    const parts = String(value).split(/[\/#:]/);
    return parts[parts.length - 1];
  }

  function valueByLocalName(item, names) {
    if (!item || typeof item !== "object") {
      return null;
    }
    const accepted = new Set(names.map((name) => name.toLowerCase()));
    for (const [key, value] of Object.entries(item)) {
      if (!accepted.has(localName(key).toLowerCase())) {
        continue;
      }
      const candidate = Array.isArray(value)
        ? (value.length ? value[0] : null)
        : value;
      if (candidate && typeof candidate === "object" && "@value" in candidate) {
        return candidate["@value"];
      }
      if (candidate && typeof candidate === "object" && "@id" in candidate) {
        return candidate["@id"];
      }
      return candidate;
    }
    return null;
  }

  function jsonLdNodes() {
    const nodes = [];
    document.querySelectorAll('script[type="application/ld+json"]').forEach((script) => {
      try {
        const payload = JSON.parse(script.textContent || "{}");
        const documents = Array.isArray(payload) ? payload : [payload];
        documents.forEach((document) => {
          if (Array.isArray(document["@graph"])) {
            nodes.push(...document["@graph"]);
          } else {
            nodes.push(document);
          }
        });
      } catch (error) {
        console.warn("INFOBIM: JSON-LD inválido ignorado na relação de cronogramas.", error);
      }
    });
    return nodes;
  }

  function nestedRecords(nodes) {
    const records = [];
    const visit = (value) => {
      if (!value || typeof value !== "object") {
        return;
      }
      if (Array.isArray(value)) {
        value.forEach(visit);
        return;
      }
      records.push(value);
      Object.values(value).forEach(visit);
    };
    nodes.forEach(visit);
    return records;
  }

  function parseScheduleDate(value) {
    if (value instanceof Date && !Number.isNaN(value.getTime())) {
      return normalizeDate(value);
    }
    if (typeof value !== "string") {
      return null;
    }
    const source = value.trim();
    const brazilian = source.match(/(?:^|\s)(\d{2})\/(\d{2})\/(\d{2}|\d{4})$/);
    if (brazilian) {
      const year = Number(brazilian[3]);
      return new Date(
        year < 100 ? 2000 + year : year,
        Number(brazilian[2]) - 1,
        Number(brazilian[1]),
      );
    }
    const iso = source.match(/^(\d{4})-(\d{2})-(\d{2})/);
    return iso
      ? new Date(Number(iso[1]), Number(iso[2]) - 1, Number(iso[3]))
      : null;
  }

  function scheduleTasks(scheduleUri) {
    const records = nestedRecords(jsonLdNodes());
    const scheduleRecords = records.filter((item) => {
      const id = String(valueByLocalName(item, ["@id"]) || "");
      return id === scheduleUri || id.startsWith(`${scheduleUri}/`);
    });
    const datedRecords = scheduleRecords.filter((item) => {
      const start = valueByLocalName(item, [
        "schedule_start", "ScheduleStart", "StartDateField",
      ]);
      const finish = valueByLocalName(item, [
        "schedule_finish", "ScheduleFinish", "FinishDateField",
      ]);
      return parseScheduleDate(start) && parseScheduleDate(finish);
    });
    const taskRecords = scheduleRecords.filter((item) => (
      valueByLocalName(item, [
        "work_breakdown_structure", "Identification", "WorkBreakdownStructureField",
      ])
      && valueByLocalName(item, ["name", "Name"])
    ));
    return datedRecords.map((timeRecord, index) => {
      const taskRecord = valueByLocalName(timeRecord, ["name", "Name"])
        ? timeRecord
        : taskRecords[index] || timeRecord;
      return {
        name: String(valueByLocalName(taskRecord, ["name", "Name"]) || "Tarefa sem nome"),
        wbs: String(valueByLocalName(taskRecord, [
          "work_breakdown_structure", "Identification", "WorkBreakdownStructureField",
        ]) || ""),
        start: parseScheduleDate(valueByLocalName(timeRecord, [
          "schedule_start", "ScheduleStart", "StartDateField",
        ])),
        finish: parseScheduleDate(valueByLocalName(timeRecord, [
          "schedule_finish", "ScheduleFinish", "FinishDateField",
        ])),
      };
    });
  }

  function tasksInWindow(tasks, dates) {
    const first = dates[0];
    const last = dates[dates.length - 1];
    return tasks
      .filter((task) => task.start <= last && task.finish >= first)
      .sort((left, right) => (
        left.start - right.start
        || left.finish - right.finish
        || left.name.localeCompare(right.name, locale)
      ));
  }

  function taskGridRange(task, dates) {
    const visible = dates
      .map((date, index) => ({ date, index }))
      .filter(({ date }) => date >= task.start && date <= task.finish);
    if (!visible.length) {
      return null;
    }
    return {
      start: visible[0].index + 1,
      span: visible[visible.length - 1].index - visible[0].index + 1,
    };
  }

  function workstreamUris() {
    const values = [];
    const seen = new Set();
    nestedRecords(jsonLdNodes()).forEach((item) => {
      const facade = valueByLocalName(item, ["conformsTo"]);
      if (!String(facade || "").endsWith("WorkStreamFacade")) {
        return;
      }
      const id = String(valueByLocalName(item, ["@id"]) || "").trim();
      if (id && !seen.has(id)) {
        seen.add(id);
        values.push(id);
      }
    });
    return values;
  }

  function relatedScheduleUris(workstreamUri) {
    const value = relationMap[workstreamUri];
    if (Array.isArray(value)) {
      return value.map(String).filter(Boolean);
    }
    return value ? [String(value)] : [];
  }

  function timeline(tasks, dates) {
    const element = document.createElement("div");
    element.className = "workstream-board-cell general-schedule-timeline workstream-schedule-timeline";
    element.style.minHeight = "112px";
    element.style.setProperty(
      "--general-schedule-row-count",
      String(Math.max(tasks.length, 1)),
    );
    tasks.forEach((task, index) => {
      const range = taskGridRange(task, dates);
      if (!range) {
        return;
      }
      const bar = document.createElement("div");
      bar.className = "general-schedule-task-bar";
      bar.style.gridColumn = `${range.start} / span ${range.span}`;
      bar.style.gridRow = String(index + 1);
      bar.title = [task.wbs, task.name].filter(Boolean).join(" — ");
      const label = document.createElement("span");
      label.textContent = task.wbs ? `${task.wbs} — ${task.name}` : task.name;
      bar.appendChild(label);
      element.appendChild(bar);
    });
    return element;
  }

  function render() {
    const board = document.querySelector("[data-workstream-board]");
    if (!board || !Object.keys(relationMap).length) {
      return;
    }
    const dates = calendarWindow();
    const uris = workstreamUris();
    const labels = Array.from(board.querySelectorAll(".workstream-board-workstream"));
    labels.forEach((label, index) => {
      const workstreamUri = uris[index];
      if (!workstreamUri) {
        return;
      }
      const schedules = relatedScheduleUris(workstreamUri);
      if (!schedules.length) {
        return;
      }
      const tasks = tasksInWindow(
        schedules.flatMap((scheduleUri) => scheduleTasks(scheduleUri)),
        dates,
      );
      const slots = [];
      let cursor = label.nextElementSibling;
      while (cursor && slots.length < 11 && cursor.classList.contains("workstream-calendar-slot")) {
        slots.push(cursor);
        cursor = cursor.nextElementSibling;
      }
      if (slots.length !== 11) {
        return;
      }
      const replacement = timeline(tasks, dates);
      slots[0].replaceWith(replacement);
      slots.slice(1).forEach((slot) => slot.remove());
      const status = label.querySelector(".workstream-board-link span");
      if (status) {
        status.textContent = tasks.length
          ? `${tasks.length} tarefas no período`
          : "Cronograma relacionado";
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", render, { once: true });
  } else {
    render();
  }
}());
