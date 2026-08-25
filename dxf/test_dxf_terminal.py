#!/usr/bin/env python3
"""Minimal DXF -> terminal renderer experiment.

Dependency:
    pip install ezdxf

Usage:
    python test_dxf_terminal.py
    python test_dxf_terminal.py path/to/file.dxf

The renderer reads simple 2D DXF geometry and projects it to a Unicode Braille
canvas. It is intentionally small: the goal is to test whether a DXF preview
is useful inside a terminal before integrating anything into OntoBDC/InfoBIM.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Iterable

import ezdxf


BRAILLE_BASE = 0x2800
# (x mod 2, y mod 4) -> braille dot bit
BRAILLE_BITS = {
    (0, 0): 0x01,  # dot 1
    (0, 1): 0x02,  # dot 2
    (0, 2): 0x04,  # dot 3
    (0, 3): 0x40,  # dot 7
    (1, 0): 0x08,  # dot 4
    (1, 1): 0x10,  # dot 5
    (1, 2): 0x20,  # dot 6
    (1, 3): 0x80,  # dot 8
}


def sampled_line(x1: float, y1: float, x2: float, y2: float) -> Iterable[tuple[float, float]]:
    distance = math.hypot(x2 - x1, y2 - y1)
    steps = max(2, int(distance * 4))
    for i in range(steps + 1):
        t = i / steps
        yield x1 + (x2 - x1) * t, y1 + (y2 - y1) * t


def sampled_arc(cx: float, cy: float, radius: float, start_deg: float, end_deg: float) -> Iterable[tuple[float, float]]:
    while end_deg < start_deg:
        end_deg += 360.0
    sweep = end_deg - start_deg
    steps = max(12, int(abs(sweep) / 3))
    for i in range(steps + 1):
        angle = math.radians(start_deg + sweep * i / steps)
        yield cx + radius * math.cos(angle), cy + radius * math.sin(angle)


def entity_points(entity) -> list[tuple[float, float]]:
    kind = entity.dxftype()

    if kind == "LINE":
        return list(sampled_line(entity.dxf.start.x, entity.dxf.start.y, entity.dxf.end.x, entity.dxf.end.y))

    if kind == "LWPOLYLINE":
        vertices = [(float(x), float(y)) for x, y, *_ in entity.get_points("xy")]
        if entity.closed and vertices:
            vertices.append(vertices[0])
        points: list[tuple[float, float]] = []
        for a, b in zip(vertices, vertices[1:]):
            points.extend(sampled_line(a[0], a[1], b[0], b[1]))
        return points

    if kind == "CIRCLE":
        return list(sampled_arc(entity.dxf.center.x, entity.dxf.center.y, entity.dxf.radius, 0, 360))

    if kind == "ARC":
        return list(sampled_arc(
            entity.dxf.center.x,
            entity.dxf.center.y,
            entity.dxf.radius,
            entity.dxf.start_angle,
            entity.dxf.end_angle,
        ))

    if kind == "POINT":
        return [(entity.dxf.location.x, entity.dxf.location.y)]

    return []


def render(path: Path, columns: int = 80, rows: int = 28) -> str:
    doc = ezdxf.readfile(path)
    modelspace = doc.modelspace()

    points: list[tuple[float, float]] = []
    counts: dict[str, int] = {}
    for entity in modelspace:
        kind = entity.dxftype()
        counts[kind] = counts.get(kind, 0) + 1
        points.extend(entity_points(entity))

    if not points:
        raise RuntimeError("No supported 2D geometry found (LINE/LWPOLYLINE/CIRCLE/ARC/POINT).")

    min_x = min(x for x, _ in points)
    max_x = max(x for x, _ in points)
    min_y = min(y for _, y in points)
    max_y = max(y for _, y in points)

    width = max(max_x - min_x, 1e-9)
    height = max(max_y - min_y, 1e-9)

    pixel_w = columns * 2
    pixel_h = rows * 4
    scale = min((pixel_w - 2) / width, (pixel_h - 2) / height)

    drawing_w = width * scale
    drawing_h = height * scale
    offset_x = (pixel_w - drawing_w) / 2
    offset_y = (pixel_h - drawing_h) / 2

    pixels: set[tuple[int, int]] = set()
    for x, y in points:
        px = int(round(offset_x + (x - min_x) * scale))
        # DXF Y grows upward; terminal rows grow downward.
        py = int(round(offset_y + (max_y - y) * scale))
        if 0 <= px < pixel_w and 0 <= py < pixel_h:
            pixels.add((px, py))

    canvas: list[list[int]] = [[0 for _ in range(columns)] for _ in range(rows)]
    for px, py in pixels:
        cell_x, dot_x = divmod(px, 2)
        cell_y, dot_y = divmod(py, 4)
        if cell_x < columns and cell_y < rows:
            canvas[cell_y][cell_x] |= BRAILLE_BITS[(dot_x, dot_y)]

    header = (
        f"DXF: {path.name} | entities: "
        + ", ".join(f"{key}={value}" for key, value in sorted(counts.items()))
        + f" | extents: ({min_x:.2f}, {min_y:.2f}) .. ({max_x:.2f}, {max_y:.2f})"
    )
    body = "\n".join("".join(chr(BRAILLE_BASE + bits) if bits else " " for bits in row).rstrip() for row in canvas)
    return f"{header}\n{'-' * min(columns, len(header))}\n{body}"


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("Residential Buildings 003.dxf")
    if not path.exists():
        print(f"DXF not found: {path}", file=sys.stderr)
        return 2

    try:
        print(render(path))
    except Exception as exc:
        print(f"Failed to render {path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
