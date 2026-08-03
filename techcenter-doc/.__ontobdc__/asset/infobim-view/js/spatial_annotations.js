(function () {
  "use strict";

  const ontology = "http://datacenter.app.br/ontology/productivity/entity/enrichment_annotation/type.ttl#";
  let dialog = null;
  let annotations = [];
  let loadedHandle = null;
  let openGeneration = 0;
  let dialogRelease = null;
  let dialogOnClose = null;
  const previewSurfaces = new WeakMap();

  function literal(value) {
    return JSON.stringify(String(value == null ? "" : value));
  }

  async function datasetFileHandle(containerHandle) {
    const metadata = await containerHandle.getDirectoryHandle(".__ontobdc__");
    const dataset = await metadata.getDirectoryHandle("dataset", {
      create: true,
    });
    return dataset.getFileHandle("EnrichmentAnnotation.ttl", {
      create: true,
    });
  }

  function parseAnnotations(source) {
    const values = [];
    const pattern = /ea:payload\s+("(?:\\.|[^"\\])*")/g;
    let match = pattern.exec(source);
    while (match) {
      try {
        values.push(JSON.parse(JSON.parse(match[1])));
      } catch (_error) {
        // Ignore malformed records while preserving every valid annotation.
      }
      match = pattern.exec(source);
    }
    return values;
  }

  async function loadAnnotations(containerHandle) {
    const handle = await datasetFileHandle(containerHandle);
    if (loadedHandle === handle) {
      return;
    }
    annotations = parseAnnotations(await (await handle.getFile()).text());
    loadedHandle = handle;
  }

  function serializeAnnotations() {
    const lines = [
      "@prefix ea: <" + ontology + "> .",
      "@prefix oa: <http://www.w3.org/ns/oa#> .",
      "@prefix dcterms: <http://purl.org/dc/terms/> .",
      "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .",
      "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .",
      "",
    ];
    annotations.forEach(function (annotation) {
      lines.push(
        "<" + annotation.id + "> a ea:EnrichmentAnnotation ;",
        "    ea:logicalSource " + literal(annotation.logicalSource)
          + "^^xsd:anyURI ;",
        "    ea:representationSource "
          + literal(annotation.representationSource) + "^^xsd:anyURI ;",
        "    ea:representationHash "
          + literal(annotation.representationHash) + " ;",
        "    ea:relatedDimension " + literal(annotation.dimension)
          + "^^xsd:anyURI ;",
        "    ea:markerColor " + literal(annotation.color) + " ;",
        "    dcterms:created " + literal(annotation.created)
          + "^^xsd:dateTime ;",
        "    oa:hasBody [",
        "        a oa:TextualBody ;",
        "        rdf:value " + literal(annotation.text),
        "    ] ;",
        "    oa:hasTarget [",
        "        a oa:SpecificResource ;",
        "        oa:hasSource " + literal(annotation.representationSource)
          + "^^xsd:anyURI ;",
        "        oa:hasSelector [",
        "            a ea:PointSelector ;",
        "            ea:sourceWidth " + annotation.width + " ;",
        "            ea:sourceHeight " + annotation.height + " ;",
        "            ea:normalizedPoint "
          + literal(JSON.stringify(annotation.points)),
        "        ]",
        "    ] ;",
        "    ea:payload " + literal(JSON.stringify(annotation)) + " .",
        "",
      );
    });
    return lines.join("\n") + "\n";
  }

  async function persist(containerHandle) {
    const handle = await datasetFileHandle(containerHandle);
    const writable = await handle.createWritable();
    await writable.write(serializeAnnotations());
    await writable.close();
    loadedHandle = handle;
  }

  function rotateRight(value, shift) {
    return (value >>> shift) | (value << (32 - shift));
  }

  function sha256Fallback(bytes) {
    const constants = [
      0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
      0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
      0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
      0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
      0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
      0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
      0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
      0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
      0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
      0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
      0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
      0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
      0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
      0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
      0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
      0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
    ];
    const hash = [
      0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
      0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19,
    ];
    const bitLength = bytes.length * 8;
    const paddedLength = Math.ceil((bytes.length + 9) / 64) * 64;
    const padded = new Uint8Array(paddedLength);
    padded.set(bytes);
    padded[bytes.length] = 0x80;
    const paddedView = new DataView(padded.buffer);
    paddedView.setUint32(
      paddedLength - 8,
      Math.floor(bitLength / 0x100000000),
      false,
    );
    paddedView.setUint32(paddedLength - 4, bitLength >>> 0, false);

    const words = new Uint32Array(64);
    for (let offset = 0; offset < paddedLength; offset += 64) {
      for (let index = 0; index < 16; index += 1) {
        words[index] = paddedView.getUint32(offset + index * 4, false);
      }
      for (let index = 16; index < 64; index += 1) {
        const value15 = words[index - 15];
        const value2 = words[index - 2];
        const sigma0 = (
          rotateRight(value15, 7)
          ^ rotateRight(value15, 18)
          ^ (value15 >>> 3)
        );
        const sigma1 = (
          rotateRight(value2, 17)
          ^ rotateRight(value2, 19)
          ^ (value2 >>> 10)
        );
        words[index] = (
          words[index - 16]
          + sigma0
          + words[index - 7]
          + sigma1
        ) >>> 0;
      }

      let a = hash[0];
      let b = hash[1];
      let c = hash[2];
      let d = hash[3];
      let e = hash[4];
      let f = hash[5];
      let g = hash[6];
      let h = hash[7];
      for (let index = 0; index < 64; index += 1) {
        const sum1 = (
          rotateRight(e, 6)
          ^ rotateRight(e, 11)
          ^ rotateRight(e, 25)
        );
        const choice = (e & f) ^ (~e & g);
        const temporary1 = (
          h + sum1 + choice + constants[index] + words[index]
        ) >>> 0;
        const sum0 = (
          rotateRight(a, 2)
          ^ rotateRight(a, 13)
          ^ rotateRight(a, 22)
        );
        const majority = (a & b) ^ (a & c) ^ (b & c);
        const temporary2 = (sum0 + majority) >>> 0;
        h = g;
        g = f;
        f = e;
        e = (d + temporary1) >>> 0;
        d = c;
        c = b;
        b = a;
        a = (temporary1 + temporary2) >>> 0;
      }
      hash[0] = (hash[0] + a) >>> 0;
      hash[1] = (hash[1] + b) >>> 0;
      hash[2] = (hash[2] + c) >>> 0;
      hash[3] = (hash[3] + d) >>> 0;
      hash[4] = (hash[4] + e) >>> 0;
      hash[5] = (hash[5] + f) >>> 0;
      hash[6] = (hash[6] + g) >>> 0;
      hash[7] = (hash[7] + h) >>> 0;
    }
    return hash
      .map(function (value) {
        return value.toString(16).padStart(8, "0");
      })
      .join("");
  }

  async function digest(file) {
    const bytes = new Uint8Array(await file.arrayBuffer());
    if (
      globalThis.crypto
      && globalThis.crypto.subtle
      && typeof globalThis.crypto.subtle.digest === "function"
    ) {
      const value = await globalThis.crypto.subtle.digest("SHA-256", bytes);
      return Array.from(new Uint8Array(value))
        .map(function (byte) {
          return byte.toString(16).padStart(2, "0");
        })
        .join("");
    }
    return sha256Fallback(bytes);
  }

  function makeUuid() {
    if (
      globalThis.crypto
      && typeof globalThis.crypto.randomUUID === "function"
    ) {
      return globalThis.crypto.randomUUID();
    }
    const bytes = new Uint8Array(16);
    if (
      globalThis.crypto
      && typeof globalThis.crypto.getRandomValues === "function"
    ) {
      globalThis.crypto.getRandomValues(bytes);
    } else {
      for (let index = 0; index < bytes.length; index += 1) {
        bytes[index] = Math.floor(Math.random() * 256);
      }
    }
    bytes[6] = (bytes[6] & 0x0f) | 0x40;
    bytes[8] = (bytes[8] & 0x3f) | 0x80;
    const value = Array.from(bytes, function (byte) {
      return byte.toString(16).padStart(2, "0");
    }).join("");
    return [
      value.slice(0, 8),
      value.slice(8, 12),
      value.slice(12, 16),
      value.slice(16, 20),
      value.slice(20),
    ].join("-");
  }

  function ensureOpenIsActive(generation, surface) {
    if (generation === openGeneration) {
      return;
    }
    if (surface && typeof surface.release === "function") {
      surface.release();
    }
    throw new DOMException(
      "A abertura da anotação foi cancelada.",
      "AbortError",
    );
  }

  function cancelOpen() {
    openGeneration += 1;
  }

  function close() {
    const onClose = dialogOnClose;
    dialogOnClose = null;
    if (dialogRelease) {
      dialogRelease();
      dialogRelease = null;
    }
    if (dialog) {
      dialog.remove();
      dialog = null;
    }
    document.body.classList.remove("has-annotation-dialog");
    if (onClose) {
      Promise.resolve(onClose()).catch(function (error) {
        console.error(error);
      });
    }
  }

  function clearPreview(context) {
    const preview = context && context.previewElement;
    if (!preview) {
      return;
    }
    const release = previewSurfaces.get(preview);
    if (release) {
      release();
      previewSurfaces.delete(preview);
    }
  }

  async function imageSurface(file, context) {
    const url = URL.createObjectURL(file);
    const image = document.createElement("img");
    image.className = "workstream-annotation-image";
    image.alt = context.representation.name || "Representação anotável";
    image.src = url;
    await new Promise(function (resolve, reject) {
      image.onload = resolve;
      image.onerror = function () {
        reject(new Error("Não foi possível carregar a imagem."));
      };
    });
    return {
      element: image,
      width: image.naturalWidth,
      height: image.naturalHeight,
      release: function () {
        URL.revokeObjectURL(url);
      },
    };
  }

  async function pdfSurface(file) {
    const pdfjs = await import(
      "https://cdn.jsdelivr.net/npm/pdfjs-dist@4.10.38/build/pdf.min.mjs"
    );
    pdfjs.GlobalWorkerOptions.workerSrc =
      "https://cdn.jsdelivr.net/npm/pdfjs-dist@4.10.38/build/pdf.worker.min.mjs";
    const task = pdfjs.getDocument({
      data: new Uint8Array(await file.arrayBuffer()),
    });
    const pdf = await task.promise;
    const page = await pdf.getPage(1);
    const viewport = page.getViewport({ scale: 2 });
    const canvas = document.createElement("canvas");
    canvas.className = "workstream-annotation-image";
    canvas.width = Math.ceil(viewport.width);
    canvas.height = Math.ceil(viewport.height);
    await page.render({
      canvasContext: canvas.getContext("2d"),
      viewport: viewport,
    }).promise;
    return {
      element: canvas,
      width: canvas.width,
      height: canvas.height,
      release: function () {
        pdf.destroy();
      },
    };
  }

  async function makeSurface(context) {
    const mediaType = context.mediaType || context.file.type || "";
    if (
      mediaType.startsWith("image/")
      || /\.(png|jpe?g|webp|gif|bmp)$/i.test(context.representation.id)
    ) {
      return imageSurface(context.file, context);
    }
    if (
      mediaType === "application/pdf"
      || /\.pdf$/i.test(context.representation.id)
    ) {
      return pdfSurface(context.file);
    }
    throw new Error("Este formato ainda não possui representação anotável.");
  }

  function markerRadius(session) {
    return Math.max(session.width, session.height) * 0.008;
  }

  function matchesContext(annotation, context) {
    return (
      annotation.logicalSource === context.resource.id
      && annotation.representationSource === context.representation.id
    );
  }

  function selectAnnotation(session, annotation) {
    session.selectedId = annotation.id;
    session.points = annotation.points.map(function (point) {
      return { x: point.x, y: point.y };
    });
    session.textarea.value = annotation.text;
    session.color.value = annotation.color || "#67e8f9";
    session.deleteButton.disabled = false;
    renderMarkers(session);
  }

  function makeMarker(session, point, annotation, draft) {
    const marker = document.createElementNS(
      "http://www.w3.org/2000/svg",
      "circle",
    );
    marker.classList.add("workstream-annotation-marker");
    if (draft) {
      marker.classList.add("is-draft");
    }
    if (annotation && session.selectedId === annotation.id) {
      marker.classList.add("is-selected");
    }
    marker.setAttribute("cx", String(point.x * session.width));
    marker.setAttribute("cy", String(point.y * session.height));
    marker.setAttribute("r", String(markerRadius(session)));
    marker.setAttribute(
      "fill",
      annotation ? annotation.color : session.color.value,
    );
    if (annotation) {
      marker.setAttribute("tabindex", "0");
      marker.setAttribute("role", "button");
      marker.setAttribute("aria-label", annotation.text || "Nota");
      marker.addEventListener("click", function (event) {
        event.stopPropagation();
        selectAnnotation(session, annotation);
      });
      marker.addEventListener("keydown", function (event) {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          selectAnnotation(session, annotation);
        }
      });
      const title = document.createElementNS(
        "http://www.w3.org/2000/svg",
        "title",
      );
      title.textContent = annotation.text;
      marker.appendChild(title);
    }
    return marker;
  }

  function renderMarkers(session) {
    session.overlay.replaceChildren();
    annotations
      .filter(function (annotation) {
        return matchesContext(annotation, session.context);
      })
      .forEach(function (annotation) {
        annotation.points.forEach(function (point) {
          session.overlay.appendChild(
            makeMarker(session, point, annotation, false),
          );
        });
      });
    if (!session.selectedId) {
      session.points.forEach(function (point) {
        session.overlay.appendChild(
          makeMarker(session, point, null, true),
        );
      });
    }
  }

  function resetEditor(session) {
    session.selectedId = null;
    session.points = [];
    session.textarea.value = "";
    session.deleteButton.disabled = true;
    renderMarkers(session);
  }

  function button(label, className) {
    const element = document.createElement("button");
    element.type = "button";
    element.textContent = label;
    if (className) {
      element.className = className;
    }
    return element;
  }

  async function showPreview(context) {
    const preview = context && context.previewElement;
    if (!preview) {
      throw new Error("A área de visualização não está disponível.");
    }

    clearPreview(context);
    await loadAnnotations(context.containerHandle);
    const surface = await makeSurface(context);
    const related = annotations.filter(function (annotation) {
      return matchesContext(annotation, context);
    });
    const stage = document.createElement("div");
    stage.className = "workstream-annotation-preview-stage";
    stage.style.aspectRatio = surface.width + " / " + surface.height;
    surface.element.classList.add("workstream-annotation-preview-base");
    stage.appendChild(surface.element);

    const overlay = document.createElementNS(
      "http://www.w3.org/2000/svg",
      "svg",
    );
    overlay.classList.add("workstream-annotation-preview-overlay");
    overlay.setAttribute(
      "viewBox",
      "0 0 " + surface.width + " " + surface.height,
    );
    overlay.setAttribute("preserveAspectRatio", "xMidYMid meet");

    let openNoteId = null;
    let activeMarker = null;
    const note = document.createElement("aside");
    note.className = "workstream-annotation-note-popover";
    note.hidden = true;
    note.setAttribute("role", "status");
    const noteColor = document.createElement("span");
    noteColor.className = "workstream-annotation-note-color";
    noteColor.setAttribute("aria-hidden", "true");
    const noteText = document.createElement("p");
    const noteClose = button("×", "workstream-annotation-note-close");
    noteClose.setAttribute("aria-label", "Fechar nota");
    note.append(noteColor, noteText, noteClose);

    function hideNote() {
      note.hidden = true;
      openNoteId = null;
      if (activeMarker) {
        activeMarker.classList.remove("is-selected");
        activeMarker.setAttribute("aria-expanded", "false");
        activeMarker = null;
      }
    }

    function showNote(annotation, point, marker) {
      if (openNoteId === annotation.id && activeMarker === marker) {
        hideNote();
        return;
      }
      hideNote();
      openNoteId = annotation.id;
      activeMarker = marker;
      marker.classList.add("is-selected");
      marker.setAttribute("aria-expanded", "true");
      noteText.textContent = annotation.text || "Nota sem texto.";
      noteColor.style.backgroundColor = annotation.color || "#67e8f9";
      note.style.left = (point.x * 100) + "%";
      note.style.top = (point.y * 100) + "%";
      note.classList.toggle("opens-left", point.x > 0.62);
      note.classList.toggle("opens-above", point.y > 0.62);
      note.hidden = false;
    }

    related.forEach(function (annotation) {
      annotation.points.forEach(function (point, pointIndex) {
        const marker = document.createElementNS(
          "http://www.w3.org/2000/svg",
          "circle",
        );
        marker.classList.add("workstream-annotation-marker");
        marker.setAttribute("cx", String(point.x * surface.width));
        marker.setAttribute("cy", String(point.y * surface.height));
        marker.setAttribute(
          "r",
          String(Math.max(surface.width, surface.height) * 0.008),
        );
        marker.setAttribute("fill", annotation.color || "#67e8f9");
        marker.setAttribute("tabindex", "0");
        marker.setAttribute("role", "button");
        marker.setAttribute("aria-expanded", "false");
        marker.setAttribute(
          "aria-label",
          "Exibir nota: " + (annotation.text || "Nota sem texto."),
        );
        marker.dataset.annotationPoint = annotation.id + ":" + pointIndex;
        marker.addEventListener("click", function (event) {
          event.stopPropagation();
          showNote(annotation, point, marker);
        });
        marker.addEventListener("keydown", function (event) {
          if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            event.stopPropagation();
            showNote(annotation, point, marker);
          }
        });
        const title = document.createElementNS(
          "http://www.w3.org/2000/svg",
          "title",
        );
        title.textContent = annotation.text || "Nota";
        marker.appendChild(title);
        overlay.appendChild(marker);
      });
    });

    note.addEventListener("click", function (event) {
      event.stopPropagation();
    });
    noteClose.addEventListener("click", hideNote);
    stage.addEventListener("click", hideNote);
    stage.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        hideNote();
      }
    });

    stage.append(overlay, note);
    preview.replaceChildren(stage);
    previewSurfaces.set(preview, surface.release);
    return related.length;
  }

  async function decoratePreview(context) {
    return showPreview(context);
  }

  async function open(context) {
    const generation = ++openGeneration;
    await loadAnnotations(context.containerHandle);
    ensureOpenIsActive(generation);
    const surface = await makeSurface(context);
    ensureOpenIsActive(generation, surface);
    const representationHash = await digest(context.file);
    ensureOpenIsActive(generation, surface);
    close();

    const root = document.createElement("section");
    root.className = "workstream-annotation-dialog";
    root.setAttribute("role", "dialog");
    root.setAttribute("aria-modal", "true");
    root.setAttribute(
      "aria-label",
      "Anotar " + (context.resource.name || "arquivo"),
    );

    const header = document.createElement("header");
    header.className = "workstream-annotation-header";
    const heading = document.createElement("div");
    const eyebrow = document.createElement("span");
    eyebrow.textContent = "InfoBIM Annotation";
    const title = document.createElement("strong");
    title.textContent = context.resource.name || "Arquivo";
    heading.append(eyebrow, title);
    const closeButton = button("Fechar");
    closeButton.addEventListener("click", close);
    header.append(heading, closeButton);

    const workspace = document.createElement("div");
    workspace.className = "workstream-annotation-workspace";
    const scroller = document.createElement("div");
    scroller.className = "workstream-annotation-stage-scroller";
    const stage = document.createElement("div");
    stage.className = "workstream-annotation-stage";
    stage.style.aspectRatio = surface.width + " / " + surface.height;
    stage.appendChild(surface.element);
    const overlay = document.createElementNS(
      "http://www.w3.org/2000/svg",
      "svg",
    );
    overlay.classList.add("workstream-annotation-overlay");
    overlay.setAttribute(
      "viewBox",
      "0 0 " + surface.width + " " + surface.height,
    );
    overlay.setAttribute("preserveAspectRatio", "xMidYMid meet");
    stage.appendChild(overlay);
    scroller.appendChild(stage);

    const editor = document.createElement("aside");
    editor.className = "workstream-annotation-editor";
    const instructions = document.createElement("p");
    instructions.textContent =
      "Clique na imagem para marcar um ou mais pontos da mesma nota.";
    const textarea = document.createElement("textarea");
    textarea.rows = 8;
    textarea.placeholder = "Escreva a nota...";
    textarea.setAttribute("aria-label", "Texto da nota");
    const colorLabel = document.createElement("label");
    colorLabel.textContent = "Cor";
    const color = document.createElement("input");
    color.type = "color";
    color.value = "#67e8f9";
    colorLabel.appendChild(color);
    const actions = document.createElement("div");
    actions.className = "workstream-annotation-actions";
    const newButton = button("Nova nota");
    const deleteButton = button("Excluir");
    deleteButton.disabled = true;
    const saveButton = button("Salvar", "is-primary");
    actions.append(newButton, deleteButton, saveButton);
    editor.append(instructions, textarea, colorLabel, actions);
    workspace.append(scroller, editor);
    root.append(header, workspace);
    document.body.appendChild(root);
    document.body.classList.add("has-annotation-dialog");
    dialog = root;
    dialogRelease = surface.release;
    dialogOnClose = typeof context.onClose === "function"
      ? context.onClose
      : null;

    const session = {
      context: context,
      width: surface.width,
      height: surface.height,
      overlay: overlay,
      textarea: textarea,
      color: color,
      deleteButton: deleteButton,
      selectedId: null,
      points: [],
    };

    stage.addEventListener("click", function (event) {
      if (event.target.closest(".workstream-annotation-marker")) {
        return;
      }
      if (session.selectedId) {
        resetEditor(session);
      }
      const rectangle = stage.getBoundingClientRect();
      session.points.push({
        x: Math.max(
          0,
          Math.min(1, (event.clientX - rectangle.left) / rectangle.width),
        ),
        y: Math.max(
          0,
          Math.min(1, (event.clientY - rectangle.top) / rectangle.height),
        ),
      });
      renderMarkers(session);
    });

    newButton.addEventListener("click", function () {
      resetEditor(session);
    });
    color.addEventListener("input", function () {
      renderMarkers(session);
    });

    saveButton.addEventListener("click", async function () {
      const text = textarea.value.trim();
      if (!text || session.points.length === 0) {
        textarea.focus();
        return;
      }
      const index = annotations.findIndex(function (annotation) {
        return annotation.id === session.selectedId;
      });
      const annotation = {
        id: session.selectedId
          || "urn:ontobdc:annotation:" + crypto.randomUUID(),
        text: text,
        color: color.value,
        logicalSource: context.resource.id,
        representationSource: context.representation.id,
        representationHash: representationHash,
        dimension: context.dimensionUri,
        width: session.width,
        height: session.height,
        points: session.points.map(function (point) {
          return { x: point.x, y: point.y };
        }),
        created: index >= 0
          ? annotations[index].created
          : new Date().toISOString(),
      };
      if (index >= 0) {
        annotations[index] = annotation;
      } else {
        annotations.push(annotation);
      }
      session.selectedId = annotation.id;
      await persist(context.containerHandle);
      session.deleteButton.disabled = false;
      renderMarkers(session);
    });

    deleteButton.addEventListener("click", async function () {
      if (!session.selectedId) {
        return;
      }
      annotations = annotations.filter(function (annotation) {
        return annotation.id !== session.selectedId;
      });
      resetEditor(session);
      await persist(context.containerHandle);
    });

    renderMarkers(session);
  }

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && dialog) {
      close();
    }
  });

  window.InfoBIMSpatialAnnotations = {
    open: open,
    close: close,
    cancelOpen: cancelOpen,
    decoratePreview: decoratePreview,
    showPreview: showPreview,
    clearPreview: clearPreview,
  };
}());
