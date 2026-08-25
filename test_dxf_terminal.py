#!/usr/bin/env python3
"""Interactive DXF terminal viewer experiment.

Dependencies:
    pip install ezdxf textual

Usage:
    python test_dxf_terminal.py
    python test_dxf_terminal.py path/to/file.dxf

Controls:
    Up/Down or j/k   select entity
    Enter            focus selected entity
    a                show all entities
    l                cycle layer filter
    q                quit

The viewer keeps the DXF parsing intentionally small, but adds an interactive
Textual UI: drawing canvas on the left, entity list/details on the right, and
selection highlighting directly in the Braille drawing.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional

import ezdxf
from rich.text import Text
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import DataTable, Footer, Header, Static


BRAILLE_BASE = 0x2800
BRAILLE_BITS = {
    (0, 0): 0x01,
    (0, 1): 0x02,
    (0, 2): 0x04,
    (0, 3): 0x40,
    (1, 0): 0x08,
    (1, 1): 0x10,
    (1, 2): 0x20,
    (1, 3): 0x80,
}
SUPPORTED_TYPES = {"LINE", "LWPOLYLINE", "CIRCLE", "ARC", "POINT"}


@dataclass
class DxfEntityRecord:
    index: int
    handle: str
    kind: str
    layer: str
    points: list[tuple[float, float]]
    entity: object

    @property
    def label(self) -> str:
        return f"{self.kind}  {self.handle}  [{self.layer}]"


def sampled_line(
    x1: float, y1: float, x2: float, y2: float, *, steps_hint: int = 200
) -> Iterable[tuple[float, float]]:
    distance = math.hypot(x2 - x1, y2 - y1)
    steps = max(2, min(steps_hint, int(distance * 4)))
    for i in range(steps + 1):
        t = i / steps
        yield x1 + (x2 - x1) * t, y1 + (y2 - y1) * t


def sampled_arc(
    cx: float,
    cy: float,
    radius: float,
    start_deg: float,
    end_deg: float,
) -> Iterable[tuple[float, float]]:
    while end_deg < start_deg:
        end_deg += 360.0
    sweep = end_deg - start_deg
    steps = max(12, min(240, int(abs(sweep) / 2)))
    for i in range(steps + 1):
        angle = math.radians(start_deg + sweep * i / steps)
        yield cx + radius * math.cos(angle), cy + radius * math.sin(angle)


def entity_points(entity) -> list[tuple[float, float]]:
    kind = entity.dxftype()

    if kind == "LINE":
        return list(
            sampled_line(
                entity.dxf.start.x,
                entity.dxf.start.y,
                entity.dxf.end.x,
                entity.dxf.end.y,
            )
        )

    if kind == "LWPOLYLINE":
        vertices = [(float(x), float(y)) for x, y, *_ in entity.get_points("xy")]
        if entity.closed and vertices:
            vertices.append(vertices[0])
        points: list[tuple[float, float]] = []
        for a, b in zip(vertices, vertices[1:]):
            points.extend(sampled_line(a[0], a[1], b[0], b[1]))
        return points

    if kind == "CIRCLE":
        return list(
            sampled_arc(
                entity.dxf.center.x,
                entity.dxf.center.y,
                entity.dxf.radius,
                0,
                360,
            )
        )

    if kind == "ARC":
        return list(
            sampled_arc(
                entity.dxf.center.x,
                entity.dxf.center.y,
                entity.dxf.radius,
                entity.dxf.start_angle,
                entity.dxf.end_angle,
            )
        )

    if kind == "POINT":
        return [(entity.dxf.location.x, entity.dxf.location.y)]

    return []


def load_entities(path: Path) -> list[DxfEntityRecord]:
    doc = ezdxf.readfile(path)
    records: list[DxfEntityRecord] = []
    for index, entity in enumerate(doc.modelspace()):
        kind = entity.dxftype()
        if kind not in SUPPORTED_TYPES:
            continue
        points = entity_points(entity)
        if not points:
            continue
        records.append(
            DxfEntityRecord(
                index=index,
                handle=str(entity.dxf.handle or "?"),
                kind=kind,
                layer=str(entity.dxf.layer or "0"),
                points=points,
                entity=entity,
            )
        )
    return records


def entity_details(record: Optional[DxfEntityRecord]) -> str:
    if record is None:
        return "No entity selected."

    entity = record.entity
    lines = [
        f"Type   : {record.kind}",
        f"Handle : {record.handle}",
        f"Layer  : {record.layer}",
        f"Points : {len(record.points)} sampled",
    ]

    if record.kind == "LINE":
        lines.extend(
            [
                f"Start  : ({entity.dxf.start.x:.3f}, {entity.dxf.start.y:.3f})",
                f"End    : ({entity.dxf.end.x:.3f}, {entity.dxf.end.y:.3f})",
            ]
        )
    elif record.kind in {"CIRCLE", "ARC"}:
        lines.extend(
            [
                f"Center : ({entity.dxf.center.x:.3f}, {entity.dxf.center.y:.3f})",
                f"Radius : {entity.dxf.radius:.3f}",
            ]
        )
        if record.kind == "ARC":
            lines.extend(
                [
                    f"Start° : {entity.dxf.start_angle:.3f}",
                    f"End°   : {entity.dxf.end_angle:.3f}",
                ]
            )
    elif record.kind == "POINT":
        lines.append(
            f"At     : ({entity.dxf.location.x:.3f}, {entity.dxf.location.y:.3f})"
        )
    elif record.kind == "LWPOLYLINE":
        lines.append(f"Closed : {bool(entity.closed)}")

    return "\n".join(lines)


def render_braille(
    records: list[DxfEntityRecord],
    *,
    selected: Optional[DxfEntityRecord] = None,
    columns: int = 80,
    rows: int = 28,
    focus_selected: bool = False,
) -> Text:
    visible = [selected] if focus_selected and selected is not None else records
    visible = [record for record in visible if record is not None]
    all_points = [point for record in visible for point in record.points]
    if not all_points:
        return Text("No supported 2D geometry found.")

    min_x = min(x for x, _ in all_points)
    max_x = max(x for x, _ in all_points)
    min_y = min(y for _, y in all_points)
    max_y = max(y for _, y in all_points)
    width = max(max_x - min_x, 1e-9)
    height = max(max_y - min_y, 1e-9)

    pixel_w = max(4, columns * 2)
    pixel_h = max(8, rows * 4)
    scale = min((pixel_w - 2) / width, (pixel_h - 2) / height)
    drawing_w = width * scale
    drawing_h = height * scale
    offset_x = (pixel_w - drawing_w) / 2
    offset_y = (pixel_h - drawing_h) / 2

    def project(points: Iterable[tuple[float, float]]) -> set[tuple[int, int]]:
        pixels: set[tuple[int, int]] = set()
        for x, y in points:
            px = int(round(offset_x + (x - min_x) * scale))
            py = int(round(offset_y + (max_y - y) * scale))
            if 0 <= px < pixel_w and 0 <= py < pixel_h:
                pixels.add((px, py))
        return pixels

    selected_pixels = project(selected.points) if selected is not None else set()
    normal_pixels: set[tuple[int, int]] = set()
    for record in visible:
        if selected is not None and record.handle == selected.handle:
            continue
        normal_pixels.update(project(record.points))

    normal_canvas = [[0 for _ in range(columns)] for _ in range(rows)]
    selected_canvas = [[0 for _ in range(columns)] for _ in range(rows)]

    for pixels, canvas in (
        (normal_pixels, normal_canvas),
        (selected_pixels, selected_canvas),
    ):
        for px, py in pixels:
            cell_x, dot_x = divmod(px, 2)
            cell_y, dot_y = divmod(py, 4)
            if cell_x < columns and cell_y < rows:
                canvas[cell_y][cell_x] |= BRAILLE_BITS[(dot_x, dot_y)]

    output = Text()
    for y in range(rows):
        for x in range(columns):
            selected_bits = selected_canvas[y][x]
            normal_bits = normal_canvas[y][x]
            bits = selected_bits | normal_bits
            if not bits:
                output.append(" ")
            elif selected_bits:
                output.append(chr(BRAILLE_BASE + bits), style="bold reverse")
            else:
                output.append(chr(BRAILLE_BASE + bits))
        if y < rows - 1:
            output.append("\n")
    return output


class DxfViewerApp(App):
    TITLE = "DXF Terminal Viewer"
    SUB_TITLE = "Braille canvas + selectable DXF entities"

    CSS = """
    Screen { layout: vertical; }
    #main { height: 1fr; }
    #canvas { width: 2fr; border: round $accent; padding: 0 1; overflow: hidden; }
    #side { width: 1fr; min-width: 34; }
    #entities { height: 2fr; border: round $panel; }
    #details { height: 1fr; border: round $panel; padding: 1; }
    #status { height: 3; padding: 0 1; }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("j", "next_entity", "Next"),
        Binding("k", "previous_entity", "Previous"),
        Binding("enter", "toggle_focus", "Focus"),
        Binding("a", "show_all", "All"),
        Binding("l", "next_layer", "Layer"),
    ]

    def __init__(self, path: Path) -> None:
        super().__init__()
        self.path = path
        self.records = load_entities(path)
        if not self.records:
            raise RuntimeError(
                "No supported 2D geometry found (LINE/LWPOLYLINE/CIRCLE/ARC/POINT)."
            )
        self.filtered_records = list(self.records)
        self.selected_index = 0
        self.focus_selected = False
        self.layers = ["*"] + sorted({record.layer for record in self.records})
        self.layer_index = 0

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(id="main"):
            yield Static(id="canvas")
            with Vertical(id="side"):
                yield DataTable(id="entities", cursor_type="row")
                yield Static(id="details")
        yield Static(id="status")
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one("#entities", DataTable)
        table.add_columns("#", "Type", "Handle", "Layer")
        self._rebuild_table()
        table.focus()
        self._refresh_view()

    @property
    def selected(self) -> Optional[DxfEntityRecord]:
        if not self.filtered_records:
            return None
        self.selected_index = max(0, min(self.selected_index, len(self.filtered_records) - 1))
        return self.filtered_records[self.selected_index]

    def _canvas_size(self) -> tuple[int, int]:
        canvas = self.query_one("#canvas", Static)
        columns = max(20, canvas.size.width - 4)
        rows = max(8, canvas.size.height - 2)
        return columns, rows

    def _rebuild_table(self) -> None:
        table = self.query_one("#entities", DataTable)
        table.clear(columns=False)
        for idx, record in enumerate(self.filtered_records):
            table.add_row(str(idx + 1), record.kind, record.handle, record.layer, key=record.handle)
        if self.filtered_records:
            table.move_cursor(row=self.selected_index, column=0, animate=False)

    def _refresh_view(self) -> None:
        selected = self.selected
        columns, rows = self._canvas_size()
        self.query_one("#canvas", Static).update(
            render_braille(
                self.filtered_records,
                selected=selected,
                columns=columns,
                rows=rows,
                focus_selected=self.focus_selected,
            )
        )
        self.query_one("#details", Static).update(entity_details(selected))
        layer = self.layers[self.layer_index]
        mode = "selected only" if self.focus_selected else "all visible"
        self.query_one("#status", Static).update(
            f"{self.path.name} | entities {len(self.filtered_records)}/{len(self.records)} "
            f"| layer {layer} | view {mode} | selection rendered in reverse video"
        )

    def on_resize(self) -> None:
        if self.is_mounted:
            self._refresh_view()

    def on_data_table_row_highlighted(self, event: DataTable.RowHighlighted) -> None:
        if event.cursor_row < len(self.filtered_records):
            self.selected_index = event.cursor_row
            self._refresh_view()

    def action_next_entity(self) -> None:
        if not self.filtered_records:
            return
        self.selected_index = (self.selected_index + 1) % len(self.filtered_records)
        self.query_one("#entities", DataTable).move_cursor(
            row=self.selected_index, column=0, animate=False
        )
        self._refresh_view()

    def action_previous_entity(self) -> None:
        if not self.filtered_records:
            return
        self.selected_index = (self.selected_index - 1) % len(self.filtered_records)
        self.query_one("#entities", DataTable).move_cursor(
            row=self.selected_index, column=0, animate=False
        )
        self._refresh_view()

    def action_toggle_focus(self) -> None:
        self.focus_selected = not self.focus_selected
        self._refresh_view()

    def action_show_all(self) -> None:
        self.layer_index = 0
        self.filtered_records = list(self.records)
        self.selected_index = 0
        self.focus_selected = False
        self._rebuild_table()
        self._refresh_view()

    def action_next_layer(self) -> None:
        self.layer_index = (self.layer_index + 1) % len(self.layers)
        layer = self.layers[self.layer_index]
        self.filtered_records = (
            list(self.records)
            if layer == "*"
            else [record for record in self.records if record.layer == layer]
        )
        self.selected_index = 0
        self.focus_selected = False
        self._rebuild_table()
        self._refresh_view()


def main() -> int:
    path = (
        Path(sys.argv[1])
        if len(sys.argv) > 1
        else Path(__file__).with_name("sample_terminal.dxf")
    )
    if not path.exists():
        print(f"DXF not found: {path}", file=sys.stderr)
        return 2

    try:
        DxfViewerApp(path).run()
    except Exception as exc:
        print(f"Failed to open {path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
