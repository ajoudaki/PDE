#!/usr/bin/env python3
"""One entry point for the paper's circle, sphere and training-stage figures.

Commands: circles, spheres, training-capture, training-render.
See README.md beside this script for sources, scopes and reproduction recipes.
Rendering reuses saved predictions. Only training-capture launches training;
it requires CUDA and imports the existing study Flow implementation.
"""
from __future__ import annotations

import argparse
import base64
from dataclasses import dataclass
import hashlib
import html
import io
import json
import math
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
CASES = (
    ('two_outliers_alternating', 'Two outliers · alternating'),
    ('quadrant_alternating', 'Quadrant · alternating'),
    ('quadrant_pairs', 'Quadrant · paired labels'),
    ('quadrant_center_edges', 'Quadrant · center / edges'),
    ('equal_mixed_odd', 'Equally spaced · mixed labels'),
)
COLORS = {0: '#22282e', 1: '#d87d25', 2: '#3278b5', 3: '#23856a', 7: '#8762ad'}
INK, MUTED, GRID = '#26323b', '#73808a', '#dfe5e9'
OFFSET, RADIAL_MAX = 3.0, 5.5
VIEW = np.array([1.5, -2., 1.1])
VIEW /= np.linalg.norm(VIEW)
BLUE, WHITE, RED = '#346e9f', '#fbfaf7', '#c45538'
OUTPUT_LIMIT, ERROR_LIMIT = 2.5, .10
MODELS = ('dense', 'P1', 'P2', 'P3')
TIMES, LEVELS = (0., 4., 16., 80.), (.5, .1, .01)


def load_plotting(*, sphere=False, font_dir=FONT_DIR):
    # Keep the CUDA-only capture command independent of plotting packages.
    global pdfmetrics, canvas, ImageReader, Image, ConvexHull, cKDTree, scipy
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas
    if sphere:
        import scipy
        from scipy.spatial import ConvexHull, cKDTree
        from PIL import Image
        from reportlab.lib.utils import ImageReader
    for name, filename in [('RadialSans', 'DejaVuSans.ttf'), ('RadialBold', 'DejaVuSans-Bold.ttf')]:
        pdfmetrics.registerFont(TTFont(name, str(font_dir/filename)))


# Shared rendering and circle data.

def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def array_sha(values):
    return hashlib.sha256(np.ascontiguousarray(values).tobytes()).hexdigest()


@dataclass
class CirclePanel:
    case: str
    title: str
    angles: np.ndarray
    train_angles: np.ndarray
    labels: np.ndarray
    predictions: dict[int, np.ndarray]
    rms: dict[int, float]


class CircleInputs:
    """Read the paper's explicit figure inputs and retain reproducible checks."""
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.base = self.root / 'data/generated/neural_response_memory_20260922'
        self.records = {}
        self.checks = []

    def path(self, value):
        path = Path(value)
        if path.is_absolute():
            # Original producer paths are portable across repository locations.
            parts = path.parts
            if 'data' in parts:
                path = self.root.joinpath(*parts[parts.index('data'):])
        else:
            path = self.root / path
        return path.resolve()

    def read_json(self, path, expected=None):
        path = self.path(path)
        digest = sha(path)
        if expected and digest != expected:
            raise ValueError(f'JSON source hash mismatch: {path}')
        self.records[str(path.relative_to(self.root))] = {'sha256': digest}
        return json.loads(path.read_text())

    def read_arrays(self, path, names, expected_file=None):
        path = self.path(path)
        record = self.records.setdefault(str(path.relative_to(self.root)), {})
        if expected_file:
            digest = sha(path)
            if digest != expected_file:
                raise ValueError(f'Archive source hash mismatch: {path}')
            record['sha256'] = digest
        with np.load(path, allow_pickle=False) as saved:
            data = {name: saved[name].copy() for name in names if name in saved}
        record['used_arrays_sha256'] = {name: array_sha(x) for name, x in data.items()}
        return data

    @staticmethod
    def check_geometry(reference, candidate):
        for name in ('angles', 'train_angles', 'labels'):
            if not np.allclose(reference[name], candidate[name], atol=2e-14, rtol=0):
                raise ValueError(f'Geometry differs between models: {name}')

    @staticmethod
    def circle_geometry(data):
        inputs = data.get('original_training_inputs', data['training_inputs'])
        labels = data.get('original_labels', data['labels'])
        return {'angles': data['endpoint_angles'],
                'train_angles': np.mod(np.arctan2(inputs[:, 1], inputs[:, 0]), 2*np.pi),
                'labels': labels}

    def shallow(self):
        meta = self.read_json(self.base/'analysis01/metrics.json')
        panels = []
        for case, title in CASES:
            fresh = case in meta['fresh_dense_references']
            if fresh:
                ref_info = meta['fresh_dense_references'][case]
                ref_path = self.path(ref_info['selected_source'])
                fresh_record = next(row for row in meta['fresh_dense_runs']
                                    if row['source'] == ref_info['selected_source'])
                dense_meta = self.read_json(ref_path, fresh_record['source_sha256'])
                archive_hash = fresh_record['arrays_sha256']
                prediction_hash = fresh_record['endpoint_prediction_sha256']
                if not ref_info['valid']:
                    raise ValueError(f'Invalid selected fresh reference: {case}')
            else:
                # The paper retains its refined archived reference for this task.
                ref_info = meta['dense_references'][case]
                ref_path = self.path(ref_info['selected_archive']).with_name('summary.json')
                dense_meta = self.read_json(ref_path)
                archive_hash = None
                prediction_hash = ref_info['endpoint_prediction_sha256'][-1]
            data = self.read_arrays(ref_path.parent/'arrays.npz',
                ('endpoint_angles', 'endpoint_prediction', 'training_inputs', 'labels'),
                expected_file=archive_hash)
            if array_sha(data['endpoint_prediction']) != prediction_hash:
                raise ValueError('Dense prediction hash differs from the selection record')
            geometry = self.circle_geometry(data)
            predictions = {0: data['endpoint_prediction']}
            errors = {}
            for order in (1, 3, 7):
                row = next(x for x in meta['selected'] if x['case'] == case and x['P'] == order)
                if not row['valid'] or (fresh and not row['fresh_reference_valid']):
                    raise ValueError(f'Invalid selected closure: {case}, P={order}')
                source = self.path(row['source'])
                self.read_json(source, row['source_sha256'])
                data = self.read_arrays(source.parent/'arrays.npz',
                    ('endpoint_angles', 'endpoint_prediction', 'training_inputs',
                     'labels', 'original_training_inputs', 'original_labels'))
                if array_sha(data['endpoint_prediction']) != row['endpoint_prediction_sha256']:
                    raise ValueError(f'Closure prediction hash mismatch: {source}')
                self.check_geometry(geometry, self.circle_geometry(data))
                predictions[order] = data['endpoint_prediction']
                errors[order] = self.check_rms(case, 'shallow', order, predictions,
                    row['fresh_reference_circle_rms'] if fresh else row['circle_rms'])
            self.checks.append({'case': case, 'depth': 'shallow',
                                'dense_training_mse': dense_meta['loss'],
                                'reference': ('fresh dense reference' if fresh else 'refined archived reference')
                                             + ' used by paper table'})
            panels.append(CirclePanel(case, title, **geometry, predictions=predictions, rms=errors))
        return panels

    def deep(self):
        meta = self.read_json(self.base/'deep_circle_analysis01/metrics_summary.json')
        cases = self.read_json(self.root/'studies/neural_response_memory_20260922/deep_circle_cases.json',
                               meta['source_sha256']['deep_circle_cases.json'])
        panels = []
        for case, title in CASES:
            predictions, errors = {}, {}
            angles = None
            for order in (0, 1, 2, 3):
                name = 'dense' if order == 0 else f'P{order}'
                original = meta['selected'][case][name]['finest']
                path = self.path(original)
                provenance = meta['provenance'][original]
                summary = self.read_json(path/'summary.json', provenance['summary_sha256'])
                if summary['status'] != 'target_loss':
                    raise ValueError(f'Unfitted deep run: {path}')
                data = self.read_arrays(path/'arrays.npz',
                    ('circle_angles', 'circle_predictions', 'observation_labels',
                     'observation_training_mse', 'train_inputs', 'train_labels'),
                    expected_file=provenance['arrays_sha256'])
                observations = [str(x) for x in data['observation_labels']]
                index = observations.index('loss_0.001')
                if abs(float(data['observation_training_mse'][index])-.001) > 1e-9:
                    raise ValueError('Wrong loss endpoint selected')
                if angles is not None and not np.array_equal(angles, data['circle_angles']):
                    raise ValueError('Deep circle grids differ')
                angles = data['circle_angles']
                definitions = cases[case]
                expected = np.deg2rad(definitions['angles_degrees'])
                actual = np.mod(np.arctan2(data['train_inputs'][:, 1], data['train_inputs'][:, 0]), 2*np.pi)
                if not np.allclose(actual, expected, atol=2e-14, rtol=0):
                    raise ValueError('Deep task geometry differs from its definition')
                if not np.array_equal(data['train_labels'], definitions['labels']):
                    raise ValueError('Deep training labels differ')
                predictions[order] = data['circle_predictions'][index]
                if order:
                    row = next(x for x in meta['endpoint_comparisons']
                               if x['case'] == case and x['P'] == order)
                    if not row['numerical_pass'] or row['milestone'] != .001:
                        raise ValueError('Deep comparison did not pass the original gates')
                    errors[order] = self.check_rms(case, 'deep', order, predictions, row['rms_8192'])
            definitions = cases[case]
            train_angles = np.deg2rad(definitions.get('original_angles_degrees', definitions['angles_degrees']))
            labels = np.asarray(definitions.get('original_labels', definitions['labels']), float)
            panels.append(CirclePanel(case, title, angles, train_angles, labels, predictions, errors))
        return panels

    def check_rms(self, case, depth, order, predictions, expected):
        rms = float(np.sqrt(np.mean((predictions[order]-predictions[0])**2)))
        if not np.isclose(rms, expected, rtol=2e-11, atol=2e-13):
            raise ValueError(f'RMS mismatch for {case}, {depth}, P={order}: {rms} vs {expected}')
        self.checks.append({'case': case, 'depth': depth, 'P': order,
                            'recomputed_rms': rms, 'reported_rms': expected,
                            'absolute_difference': abs(rms-expected)})
        return rms


class Drawing:
    """Identical vector primitives in editable SVG and publication PDF."""
    def __init__(self, path, width, height, inches=6.5):
        self.path, self.width, self.height = Path(path), width, height
        self.scale = inches*72/width
        self.pdf = canvas.Canvas(str(self.path.with_suffix('.pdf')),
            pagesize=(width*self.scale, height*self.scale), pageCompression=1,
            invariant=1, initialFontName='RadialSans')
        self.pdf.setTitle(self.path.stem.replace('_', ' '))
        self.pdf.setCreator('paper/scripts/figures.py')
        self.svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
                    f'<rect width="{width}" height="{height}" fill="white"/>']
        self.pdf.setFillColorRGB(1, 1, 1)
        self.pdf.rect(0, 0, width*self.scale, height*self.scale, fill=1, stroke=0)
        self.text_boxes = []

    @staticmethod
    def rgb(color):
        return tuple(int(color[i:i+2], 16)/255 for i in (1, 3, 5))

    def style(self, color, width, fill=None, dash=()):
        self.pdf.setStrokeColorRGB(*self.rgb(color))
        self.pdf.setLineWidth(width*self.scale)
        self.pdf.setDash([v*self.scale for v in dash])
        if fill:
            self.pdf.setFillColorRGB(*self.rgb(fill))

    def text(self, x, y, value, size=23, color=INK, anchor='middle', bold=False):
        value = str(value)
        font = 'RadialBold' if bold else 'RadialSans'
        width = pdfmetrics.stringWidth(value, font, size)
        left = x - (width/2 if anchor == 'middle' else width if anchor == 'end' else 0)
        if left < 0 or left+width > self.width or y-size < 0 or y > self.height:
            raise ValueError(f'Text outside figure: {value}')
        self.text_boxes.append((left, y-size, left+width, y, value))
        self.svg.append(f'<text x="{x:.3f}" y="{y:.3f}" font-family="DejaVu Sans, sans-serif" font-size="{size}" font-weight="{"bold" if bold else "normal"}" text-anchor="{anchor}" fill="{color}">{html.escape(value)}</text>')
        self.pdf.setFont(font, size*self.scale)
        self.pdf.setFillColorRGB(*self.rgb(color))
        self.pdf.drawString(left*self.scale, (self.height-y)*self.scale, value)

    def line(self, x1, y1, x2, y2, color=GRID, width=1.2, dash=()):
        self.path_line(np.array([[x1, y1], [x2, y2]]), color, width, dash)

    def path_line(self, points, color, width=2, dash=()):
        if not np.isfinite(points).all():
            raise ValueError('Nonfinite plot coordinates')
        path = 'M '+' L '.join(f'{x:.4f},{y:.4f}' for x, y in points)
        dashed = f' stroke-dasharray="{" ".join(map(str,dash))}"' if dash else ''
        self.svg.append(f'<path d="{path}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"{dashed}/>')
        self.style(color, width, dash=dash)
        self.pdf.setLineJoin(1)
        self.pdf.setLineCap(1)
        p = self.pdf.beginPath()
        p.moveTo(points[0, 0]*self.scale, (self.height-points[0, 1])*self.scale)
        for x, y in points[1:]:
            p.lineTo(x*self.scale, (self.height-y)*self.scale)
        self.pdf.drawPath(p, stroke=1, fill=0)

    def circle(self, x, y, radius, color=GRID, width=1.2, fill=None, dash=()):
        dashed = f' stroke-dasharray="{" ".join(map(str,dash))}"' if dash else ''
        self.svg.append(f'<circle cx="{x:.4f}" cy="{y:.4f}" r="{radius:.4f}" fill="{fill or "none"}" stroke="{color}" stroke-width="{width}"{dashed}/>')
        self.style(color, width, fill, dash)
        self.pdf.circle(x*self.scale, (self.height-y)*self.scale, radius*self.scale,
                        stroke=1, fill=int(fill is not None))

    def finish(self):
        for i, (left, top, right, bottom, value) in enumerate(self.text_boxes):
            for l2, t2, r2, b2, v2 in self.text_boxes[:i]:
                if min(right, r2) > max(left, l2) and min(bottom, b2) > max(top, t2):
                    raise ValueError(f'Overlapping text labels: {value!r}, {v2!r}')
        self.svg.append('</svg>')
        self.path.with_suffix('.svg').write_text('\n'.join(self.svg)+'\n')
        self.pdf.showPage()
        self.pdf.save()


def polar_xy(cx, cy, angles, radii):
    return np.column_stack((cx+radii*np.cos(angles), cy-radii*np.sin(angles)))


def draw_circle_panel(draw, data, cx, cy, radius=168, letter='a'):
    if data.angles.shape != (8192,) or not np.allclose(
            data.angles, np.arange(8192)*(2*np.pi/8192), atol=2e-14, rtol=0):
        raise ValueError('Expected the paper\'s uniform 8192-point circle grid')
    if any(p.shape != data.angles.shape for p in data.predictions.values()):
        raise ValueError('Prediction length differs from the angle grid')
    draw.text(cx, cy-231, f'({letter})  {data.title}', size=24, bold=True)
    unit = radius/RADIAL_MAX
    for angle in (0, np.pi/2, np.pi, 3*np.pi/2):
        x, y = polar_xy(cx, cy, np.array([angle]), np.array([radius]))[0]
        draw.line(cx, cy, x, y)
        x, y = polar_xy(cx, cy, np.array([angle]), np.array([radius+28]))[0]
        draw.text(x, y+7, f'{int(round(np.degrees(angle)))}°', size=21, color=MUTED)
    for output in (-2, -1, 0, 1, 2):
        r = unit*(OFFSET+output)
        draw.circle(cx, cy, r, color='#9da9b2' if output == 0 else GRID,
                    width=1.5 if output == 0 else 1.0,
                    dash=(4, 5) if output == 0 else ())
        # The reference labels are outside dense data in the upper-left sector.
        x, y = polar_xy(cx, cy, np.array([np.deg2rad(124)]), np.array([r]))[0]
        draw.text(x-5, y-3, str(output).replace('-', '−'), size=18, color=MUTED, anchor='end')
    for order, prediction in data.predictions.items():
        r = unit*(OFFSET+prediction)
        if np.any(r <= 0) or np.any(r > radius):
            raise ValueError('Fixed radial offset/limits would fold or clip a curve')
        a = np.r_[data.angles, data.angles[0]+2*np.pi]
        rr = np.r_[r, r[0]]
        draw.path_line(polar_xy(cx, cy, a, rr), COLORS[order], width=4.2 if order == 0 else 2.4)
    positions = polar_xy(cx, cy, data.train_angles, unit*(OFFSET+data.labels))
    for x, y in positions:
        draw.circle(x, y, 4.5, color='#ffffff', width=1.4, fill=COLORS[0])
    orders = list(data.rms)
    draw.text(cx-205, cy+235, 'RMS', size=20, color=MUTED, anchor='start')
    for i, order in enumerate(orders):
        label = f'{data.rms[order]:.3g}'.replace('e-0', 'e−')
        draw.text(cx-87+112*i, cy+235, label, size=21,
                  color=COLORS[order])


def draw_circle_figure(panels, path, depth):
    draw = Drawing(path, 1440, 1220)
    width, layers = (4096, 'Three') if depth == 'deep' else (2048, 'Two')
    draw.text(720, 43, f'{layers} hidden layers · width {width}', size=30, bold=True)
    draw.text(720, 79, 'Response memory and dense training at MSE 0.001', size=23, color=MUTED)
    positions = [(240, 360), (720, 360), (1200, 360), (480, 866), (960, 866)]
    for i, (data, (cx, cy)) in enumerate(zip(panels, positions)):
        draw_circle_panel(draw, data, cx, cy, letter=chr(ord('a')+i))
    orders = list(panels[0].rms)
    labels = [(0, 'Dense'), *[(p, f'q = {p}') for p in orders]]
    for i, (order, label) in enumerate(labels):
        x = 185+225*i
        draw.line(x, 1151, x+47, 1151, COLORS[order], 4.2 if order == 0 else 3)
        draw.text(x+60, 1158, label, size=23, anchor='start')
    draw.circle(1112, 1151, 4.5, color='#ffffff', width=1.4, fill=COLORS[0])
    draw.text(1125, 1158, 'Training labels', size=23, anchor='start')
    draw.text(720, 1200, 'Angle = input direction     Radius = 3 + prediction     Dashed ring = zero', size=22, color=MUTED)
    draw.finish()


def save_circle_bundle(path, groups):
    arrays = {}
    description = {}
    for depth, panels in groups.items():
        description[depth] = []
        for i, data in enumerate(panels):
            prefix = f'{depth}_{i}_'
            arrays.update({prefix+'angles': data.angles,
                           prefix+'train_angles': data.train_angles,
                           prefix+'labels': data.labels})
            for order, values in data.predictions.items():
                arrays[prefix+f'P{order}'] = values
            description[depth].append({'case': data.case, 'title': data.title,
                                      'orders': list(data.predictions), 'rms': data.rms})
    arrays['description_json'] = np.asarray(json.dumps(description))
    np.savez_compressed(path, **arrays)


def load_circle_bundle(path):
    groups = {}
    with np.load(path, allow_pickle=False) as z:
        description = json.loads(str(z['description_json']))
        for depth, items in description.items():
            groups[depth] = []
            for i, info in enumerate(items):
                prefix = f'{depth}_{i}_'
                data = CirclePanel(info['case'], info['title'], z[prefix+'angles'],
                    z[prefix+'train_angles'], z[prefix+'labels'],
                    {p: z[prefix+f'P{p}'] for p in info['orders']},
                    {int(p): v for p, v in info['rms'].items()})
                for p, expected in data.rms.items():
                    actual = np.sqrt(np.mean((data.predictions[p]-data.predictions[0])**2))
                    if not np.isclose(actual, expected, rtol=2e-11, atol=2e-13):
                        raise ValueError('Portable bundle metric mismatch')
                groups[depth].append(data)
    return groups


# Spherical surface rendering and endpoint data.

def sphere_color(values, limit):
    """Linear, symmetric blue--off-white--red map, without lighting changes."""
    if np.max(np.abs(values)) > limit + 1e-10:
        raise ValueError('Color limits would clip data')
    t = values/limit
    anchors = np.array([Drawing.rgb(c) for c in (BLUE, WHITE, RED)])*255
    result = anchors[1] + np.abs(t)[..., None]*(
        np.where((t >= 0)[..., None], anchors[2], anchors[0])-anchors[1])
    return np.rint(result).astype(np.uint8)


def sphere_camera(back=False):
    toward = -VIEW if back else VIEW
    right = np.cross([0., 0., 1.], toward)
    right /= np.linalg.norm(right)
    up = np.cross(toward, right)
    return np.stack([right, up, toward])


class SphereSurface:
    """Ray/triangle interpolation on the complete stored spherical mesh."""
    def __init__(self, points):
        if points.shape != (8192, 3):
            raise ValueError('Expected 8192 saved sphere queries')
        if not np.allclose(np.linalg.norm(points, axis=1), 1, atol=1e-13, rtol=0):
            raise ValueError('Query directions are not on the unit sphere')
        hull = ConvexHull(points)
        if len(hull.vertices) != len(points) or np.any(hull.equations[:, 3] >= 0):
            raise ValueError('Mesh must use every point and contain the origin')
        self.triangles = hull.simplices
        vertices = points[self.triangles]
        self.inverse = np.linalg.inv(vertices.transpose(0, 2, 1))
        centers = vertices.mean(axis=1)
        self.tree = cKDTree(centers/np.linalg.norm(centers, axis=1)[:, None])
        self.maximum_weight_defect = 0.

    def locate(self, directions):
        indices, weights = [], []
        for start in range(0, len(directions), 20000):
            q = directions[start:start+20000]
            candidates = self.tree.query(q, k=8)[1]
            coefficients = np.einsum('bkij,bj->bki', self.inverse[candidates], q)
            inside = np.all(coefficients >= -2e-12, axis=2)
            if not inside.any(axis=1).all():
                raise ValueError('Failed to locate a surface triangle; do not extrapolate')
            choice = np.argmax(inside, axis=1)
            rows = np.arange(len(q))
            w = coefficients[rows, choice]
            w = w/w.sum(axis=1, keepdims=True)
            self.maximum_weight_defect = max(self.maximum_weight_defect,
                float(np.max(np.abs(w.sum(axis=1)-1))))
            indices.append(self.triangles[candidates[rows, choice]])
            weights.append(w)
        return np.concatenate(indices), np.concatenate(weights)

    def texture_coordinates(self, resolution, back):
        v = (np.arange(resolution)+.5)*2/resolution-1
        x, y = np.meshgrid(v, -v)
        inside = x*x+y*y < 1
        local = np.column_stack([x[inside], y[inside], np.sqrt(1-x[inside]**2-y[inside]**2)])
        directions = local @ sphere_camera(back)
        indices, weights = self.locate(directions)
        return inside, indices, weights


class SphereDrawing(Drawing):
    def bitmap(self, x, y, width, height, pixels):
        content = io.BytesIO()
        Image.fromarray(pixels).save(content, format='PNG')
        encoded = base64.b64encode(content.getvalue()).decode()
        self.svg.append(f'<image x="{x}" y="{y}" width="{width}" height="{height}" '
                        f'href="data:image/png;base64,{encoded}"/>')
        content.seek(0)
        self.pdf.drawImage(ImageReader(content), x*self.scale,
            (self.height-y-height)*self.scale, width*self.scale, height*self.scale,
            mask='auto')

    def faint_line(self, points):
        self.pdf.saveState()
        self.pdf.setStrokeAlpha(.28)
        self.path_line(points, '#627680', width=.8)
        self.svg[-1] = self.svg[-1].replace('fill="none"', 'fill="none" opacity="0.28"')
        self.pdf.restoreState()


def visible_segments(points, basis):
    projected = points @ basis.T
    good = projected[:, 2] > 1e-8
    split = np.flatnonzero(np.diff(np.r_[False, good, False]))
    for first, last in zip(split[::2], split[1::2]):
        if last-first > 1:
            yield projected[first:last, :2]


def draw_globe(draw, cx, cy, radius, values, limit, train, coords, back):
    inside, indices, weights = coords
    field = np.sum(values[indices]*weights, axis=1)
    pixels = np.zeros((*inside.shape, 4), dtype=np.uint8)
    pixels[inside, :3] = sphere_color(field, limit)
    pixels[inside, 3] = 255
    draw.bitmap(cx-radius, cy-radius, 2*radius, 2*radius, pixels)
    basis = sphere_camera(back)
    circles = []
    angle = np.linspace(0, 2*np.pi, 1000)
    for latitude in (-60, -30, 0, 30, 60):
        lat = np.deg2rad(latitude)
        circles.append(np.column_stack([np.cos(lat)*np.cos(angle),
                         np.cos(lat)*np.sin(angle), np.full_like(angle, np.sin(lat))]))
    lat = np.linspace(-np.pi/2, np.pi/2, 500)
    for longitude in range(0, 360, 60):
        lon = np.deg2rad(longitude)
        circles.append(np.column_stack([np.cos(lat)*np.cos(lon),
                         np.cos(lat)*np.sin(lon), np.sin(lat)]))
    for circle in circles:
        for piece in visible_segments(circle, basis):
            draw.faint_line(np.column_stack([cx+radius*piece[:, 0], cy-radius*piece[:, 1]]))
    draw.circle(cx, cy, radius, color='#c8d0d5', width=.9)
    projected = train @ basis.T
    for x, y, depth in projected:
        if depth > 0:
            draw.circle(cx+radius*x, cy-radius*y, 3.7, color='#ffffff', width=1.4, fill=INK)


def draw_colorbar(draw, x, y, width, limit, label):
    values = np.linspace(-limit, limit, 1024)
    pixels = np.repeat(sphere_color(values, limit)[None, :, :], 14, axis=0)
    draw.bitmap(x, y, width, 14, pixels)
    draw.text(x+width/2, y-18, label, size=23)
    for value, fraction in ((-limit, 0), (0., .5), (limit, 1)):
        text = ('0' if value == 0 else f'{value:g}').replace('-', '−')
        draw.line(x+width*fraction, y+17, x+width*fraction, y+23, MUTED, .9)
        draw.text(x+width*fraction, y+47, text, size=22, color=MUTED)


def draw_sphere_figure(path, data, metadata, coordinates, kind):
    draw = SphereDrawing(path, 1470, 1140)
    dense = data['dense']
    fields = [dense, data['P3'], data['P3']-dense] if kind == 'comparison' else [
        dense, *[data[f'P{p}']-dense for p in (1, 2, 3)]]
    centers = [245, 735, 1225] if kind == 'comparison' else [210, 560, 910, 1260]
    radius = 158 if kind == 'comparison' else 146
    titles = ['Dense network', 'Memory closure · q = 3', 'Difference · q = 3'] if kind == 'comparison' else [
        'Dense network', 'Difference · q = 1', 'Difference · q = 2', 'Difference · q = 3']
    heading = 'The fitted function on the sphere' if kind == 'comparison' else 'More memory, smaller discrepancy'
    draw.text(735, 47, heading, size=33, bold=True)
    draw.text(735, 87, 'ReLU · four hidden layers · width 2048 · 64 training inputs', size=23, color=MUTED)
    for i, (cx, values, title) in enumerate(zip(centers, fields, titles)):
        is_output = i < 2 if kind == 'comparison' else i == 0
        draw.text(cx, 146, title, size=25, bold=True)
        if i == 0:
            subtitle = 'Fitted output'
        else:
            p = 3 if kind == 'comparison' else i
            subtitle = f"RMS vs dense  {metadata['rms'][f'P{p}']:.5f}"
        draw.text(cx, 183, subtitle, size=22, color=MUTED)
        for back, cy in ((False, 360), (True, 740)):
            draw_globe(draw, cx, cy, radius, values, OUTPUT_LIMIT if is_output else ERROR_LIMIT,
                  data['inputs'], coordinates[back], back)
    draw.text(32, 367, 'Front', size=18, color=MUTED)
    draw.text(32, 747, 'Back', size=18, color=MUTED)
    if kind == 'comparison':
        draw_colorbar(draw, 170, 966, 640, OUTPUT_LIMIT, 'Prediction · same scale for both models')
        draw_colorbar(draw, 1085, 966, 280, ERROR_LIMIT, 'Closure − dense')
    else:
        draw_colorbar(draw, 95, 966, 230, OUTPUT_LIMIT, 'Prediction')
        draw_colorbar(draw, 520, 966, 780, ERROR_LIMIT, 'Closure − dense · one scale for every order')
    draw.circle(598, 1051, 3.7, color='#ffffff', width=1.4, fill=INK)
    draw.text(612, 1058, 'Training inputs', size=22, anchor='start')
    draw.text(735, 1105, '8192 equal-area queries · Each model stopped at training RMS ≤ 0.01', size=23, color=MUTED)
    draw.finish()


def load_sphere_source(path):
    metadata = json.loads((path/'results.json').read_text())
    if metadata['dimension'] != 3 or metadata['samples'] != 64 or metadata['task'] != 'xyz':
        raise ValueError('This layout describes the selected xyz/64 experiment')
    if sha(path/'data.npz') != metadata['data_sha256']:
        raise ValueError('Original data hash differs from the run record')
    with np.load(path/'data.npz', allow_pickle=False) as z:
        data = {key: z[key].copy() for key in z.files}
    records = {name: sha(path/name) for name in ('results.json', 'data.npz')}
    checks, errors = [], {}
    for model in ('dense', 'P1', 'P2', 'P3'):
        name = f'relu_{model}.npz'
        records[name] = sha(path/name)
        with np.load(path/name, allow_pickle=False) as z:
            data[model] = z['test_prediction'].copy()
            data[model+'_train'] = z['prediction'].copy()
        row = next(r for r in metadata['rows'] if r['activation'] == 'relu' and r['model'] == model)
        train_rms = float(np.sqrt(np.mean((data[model+'_train']-data['labels'])**2)))
        rms = float(np.sqrt(np.mean((data[model]-data['dense'])**2)))
        if row['status'] != 'target_rms' or train_rms > .01:
            raise ValueError('Selected model is not fitted to the stated target')
        if not np.isclose(train_rms, row['train_rms'], rtol=1e-12, atol=1e-14):
            raise ValueError('Training metric differs from the stored record')
        if not np.isclose(rms, row['test_rms_vs_dense'], rtol=1e-12, atol=1e-14):
            raise ValueError('Sphere metric differs from the stored record')
        errors[model] = rms
        checks.append({'model': model, 'train_rms': train_rms, 'sphere_rms_vs_dense': rms,
                       'source_rms_vs_dense': row['test_rms_vs_dense'], 'flow_time': row['physical_time']})
    metadata.update(rms=errors, source_records=records, checks=checks, source_directory=str(path))
    return data, metadata


# Training-stage capture and rendering.

def capture_checkpoints(flow, queries, *, times=TIMES, levels=LEVELS, step=1/128,
                block=32, seconds=60.):
    """Use the existing fitter to stop at each time or loss event in order.

Every saved prediction is an actual state. Loss events are the first checked
block at/below a threshold, not interpolated states or precisely equal losses.
"""
    ticks = np.rint(np.asarray(times)/step).astype(int)
    if ticks[0] != 0 or np.any(np.diff(ticks) <= 0):
        raise ValueError('Times must increase strictly from zero')
    if not np.allclose(ticks*step, times, atol=1e-12, rtol=0):
        raise ValueError('Times must fall on the Euler step grid')
    if np.any(ticks % block):
        raise ValueError('Use common-time milestones aligned with checked blocks')
    if any(a <= b for a, b in zip(levels, levels[1:])) or min(levels) <= 0:
        raise ValueError('Loss levels must decrease and remain positive')
    saved = {'time': [], 'loss': []}
    start = time.perf_counter()
    count, itime, iloss = 0, 1, 0

    def sample():
        train = flow.predict(flow.inputs).detach().cpu().numpy().astype(float)
        labels = flow.labels.detach().cpu().numpy().astype(float)
        # Batches limit peak memory without changing these unnormalized models.
        values = np.concatenate([flow.predict(queries[i:i+1024]).detach().cpu().numpy()
                                 for i in range(0, len(queries), 1024)]).astype(float)
        return {'time': count*step, 'train_rms': float(np.sqrt(np.mean((train-labels)**2))),
                'prediction': values, 'training_prediction': train}

    first = sample()
    saved['time'].append(first)
    saved['loss'].append(first)
    current_rms = first['train_rms']
    if current_rms <= levels[0]:
        raise ValueError('Initial loss is already below the first requested loss milestone')
    while itime < len(ticks):
        remaining = seconds-(time.perf_counter()-start)
        if remaining <= 0:
            return saved, {'status': 'wall_limit', 'seconds': time.perf_counter()-start}
        target = levels[iloss] if iloss < len(levels) else 1e-30
        report = flow.fit(step=step, target_rms=target, max_steps=int(ticks[itime]-count),
                          block=block, max_seconds=remaining, adaptive=False)
        count += report['steps']
        current_rms = report['rms']
        if report['status'] in ('wall_limit', 'nonfinite'):
            return saved, {'status': report['status'], 'seconds': time.perf_counter()-start}
        time_event = count == ticks[itime]
        loss_event = iloss < len(levels) and current_rms <= levels[iloss]
        if not (time_event or loss_event):
            raise ValueError('Fitter returned without reaching the next observation event')
        record = sample()
        if time_event:
            saved['time'].append(record)
            itime += 1
        while iloss < len(levels) and current_rms <= levels[iloss]:
            saved['loss'].append(record)
            iloss += 1
    status = 'complete' if iloss == len(levels) else 'physical_complete_loss_incomplete'
    return saved, {'status': status, 'seconds': time.perf_counter()-start}


def capture_training(args):
    import torch
    if not torch.cuda.is_available():
        raise RuntimeError('No CUDA device is available. Capture is not launched on CPU at width 2048.')
    sys.path.insert(0, str(ROOT/'studies/neural_response_memory_20260922'))
    from compact_flow import Flow
    torch.set_num_threads(1)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    source = ROOT/'data/generated/neural_response_memory_20260922/compact_sphere01/xyz_m64'
    with np.load(source/'data.npz', allow_pickle=False) as z:
        data = {key: z[key].copy() for key in z.files}
    source_metadata = json.loads((source/'results.json').read_text())
    if sha(source/'data.npz') != source_metadata['data_sha256']:
        raise ValueError('Original task data hash differs')
    metadata = {'kind': 'New trajectory capture with explicitly recorded initialization settings',
        'times': list(TIMES), 'loss_thresholds': list(LEVELS),
        'model': {'width': 2048, 'depth': 4, 'activation': 'relu', 'seed': 20260920,
                  'hidden_gain': args.hidden_gain, 'readout_std': args.readout_std,
                  'normalization': 'none', 'dtype': 'float32'},
        'optimizer': {'step': 1/128, 'block': 32, 'adaptive': False},
        'seconds_cap_per_model': args.seconds, 'device': args.device,
        'gpu': torch.cuda.get_device_name(torch.device(args.device)), 'torch': torch.__version__,
        'source_data_sha256': sha(source/'data.npz'),
        'flow_source_sha256': sha(ROOT/'studies/neural_response_memory_20260922/compact_flow.py'),
        'capture_source_sha256': sha(__file__), 'reports': {}, 'observations': {}}
    args.out.mkdir(parents=True, exist_ok=False)
    for name in MODELS:
        flow = Flow(data['inputs'], data['labels'], width=2048, depth=4, activation='relu',
                    seed=20260920, order=None if name == 'dense' else int(name[1:]),
                    device=args.device, dtype=torch.float32, normalization='none',
                    hidden_gain=args.hidden_gain, readout_std=args.readout_std)
        saved, report = capture_checkpoints(flow, data['test_inputs'], seconds=args.seconds)
        if len(saved['loss']) == 4:
            with np.load(source/f'relu_{name}.npz', allow_pickle=False) as old:
                report['rms_difference_from_archived_fitted_prediction'] = float(np.sqrt(
                    np.mean((saved['loss'][-1]['prediction']-old['test_prediction'])**2)))
        metadata['reports'][name] = report
        metadata['observations'][name] = {}
        for kind, entries in saved.items():
            data[f'{name}_{kind}'] = np.stack([r['prediction'] for r in entries])
            data[f'{name}_{kind}_train'] = np.stack([r['training_prediction'] for r in entries])
            metadata['observations'][name][kind] = [
                {k: r[k] for k in ('time', 'train_rms')} for r in entries]
        np.savez_compressed(args.out/'sphere_training_data.npz', **data,
                            metadata_json=np.asarray(json.dumps(metadata)))
        print(json.dumps({'model': name, **report,
                          'time_observations': len(saved['time']), 'loss_observations': len(saved['loss'])}), flush=True)
        del flow
        torch.cuda.empty_cache()
        if report['status'] != 'complete':
            raise RuntimeError('Capture incomplete; partial arrays preserved, no retries or automatic scope changes')
    for name in MODELS[1:]:
        if not np.allclose(data[f'{name}_time'][0], data['dense_time'][0], atol=1e-10, rtol=1e-6):
            raise ValueError('Dense and closures do not start from the same predictor')
    return args.out/'sphere_training_data.npz'


def nice_limit(maximum):
    if maximum <= 0:
        return 1.
    power = 10**np.floor(np.log10(maximum))
    return float(next(v*power for v in (1, 2, 2.5, 5, 10) if v*power >= maximum))


def render_training(bundle, out, no_png=False, *, dpi=280, resolution=640, font_dir=FONT_DIR):
    load_plotting(sphere=True, font_dir=font_dir)
    with np.load(bundle, allow_pickle=False) as z:
        metadata = json.loads(str(z['metadata_json']))
        data = {key: z[key].copy() for key in z.files if key != 'metadata_json'}
    for kind in ('time', 'loss'):
        for name in MODELS:
            if data[f'{name}_{kind}'].shape != (4, 8192):
                raise ValueError('Four complete recorded stages per model are required')
            obs = metadata['observations'][name][kind]
            losses = np.sqrt(np.mean((data[f'{name}_{kind}_train']-data['labels'])**2, axis=1))
            if not np.allclose(losses, [r['train_rms'] for r in obs], rtol=1e-12, atol=1e-14):
                raise ValueError('Recorded training losses differ from saved predictions')
            if kind == 'time' and [r['time'] for r in obs] != metadata['times']:
                raise ValueError('Common-time rows do not share physical times')
            if kind == 'loss' and np.any(losses[1:] > np.asarray(metadata['loss_thresholds'])*(1+1e-6)):
                raise ValueError('Loss rows have not reached their stated thresholds')
    surface = SphereSurface(data['test_inputs'])
    coords = surface.texture_coordinates(resolution, False)
    output_limit = nice_limit(max(np.max(np.abs(data[f'dense_{kind}'])) for kind in ('time', 'loss')))
    error_limit = nice_limit(max(np.max(np.abs(data[f'{name}_{kind}']-data[f'dense_{kind}']))
                           for name in MODELS[1:] for kind in ('time', 'loss')))
    outputs, metrics = [], {}
    out.mkdir(parents=True, exist_ok=True)
    if (out/'training_figure_manifest.json').exists():
        raise FileExistsError('Use a fresh render directory')
    for kind in ('time', 'loss'):
        path = out/f'sphere_training_{kind}'
        draw = SphereDrawing(path, 1880, 2040)
        heading = 'LAYOUT CHECK — synthetic data' if metadata.get('validation_only') else 'Response memory through training'
        draw.text(940, 48, heading, size=37, bold=True)
        subtitle = 'Matched physical time' if kind == 'time' else 'Comparable training loss · first checked threshold crossings'
        draw.text(940, 94, subtitle, size=27, color=MUTED)
        centers = [390, 800, 1210, 1620]
        for cx, label in zip(centers, ['Dense output', 'P = 1 error', 'P = 2 error', 'P = 3 error']):
            draw.text(cx, 157, label, size=30, bold=True)
        metrics[kind] = {}
        for row, cy in enumerate([440, 850, 1260, 1670]):
            if row == 0:
                label = 'Initialization'
            elif kind == 'time':
                label = f"t = {metadata['times'][row]:g}"
            else:
                label = f"RMS ≤ {metadata['loss_thresholds'][row-1]:g}"
            draw.text(108, cy, label, size=26)
            for cx, name in zip(centers, MODELS):
                actual = data[f'{name}_{kind}'][row]
                values = actual if name == 'dense' else actual-data[f'dense_{kind}'][row]
                error = float(np.sqrt(np.mean((actual-data[f'dense_{kind}'][row])**2)))
                draw_globe(draw, cx, cy, 155, values, output_limit if name == 'dense' else error_limit,
                      data['inputs'], coords, False)
                obs = metadata['observations'][name][kind][row]
                first = f"Train RMS {obs['train_rms']:.3g}" if name == 'dense' else f'Error RMS {error:.3g}'
                draw.text(cx, cy+191, first, size=24)
                second = f"t = {obs['time']:g}" if kind == 'loss' else f"Train RMS {obs['train_rms']:.3g}"
                if name != 'dense' or kind == 'loss':
                    draw.text(cx, cy+220, second, size=22, color=MUTED)
                metrics[kind][f'{row}_{name}'] = {'error_rms': error, **obs}
        # Legends are above the first row, leaving room for four training stages.
        draw_colorbar(draw, 266, 207, 248, output_limit, 'Prediction')
        draw_colorbar(draw, 740, 207, 940, error_limit, 'Closure − dense')
        draw.text(940, 2010, 'One fixed view · Black dots: training inputs · RMS: whole sphere · Common color scales throughout', size=24, color=MUTED)
        draw.finish()
        outputs.extend([path.with_suffix('.pdf'), path.with_suffix('.svg')])
        if not no_png:
            subprocess.run(['pdftoppm', '-r', str(dpi), '-png', '-singlefile',
                            str(path.with_suffix('.pdf')), str(path)], check=True)
            outputs.append(path.with_suffix('.png'))
    report = {'bundle_sha256': sha(bundle), 'script_sha256': sha(__file__),
              'validation_only': bool(metadata.get('validation_only')),
              'output_limit': output_limit, 'error_limit': error_limit,
              'metrics': metrics, 'outputs': {p.name: sha(p) for p in outputs},
              'rendering': 'One front hemisphere; errors measured on all original 8192 sphere queries'}
    (out/'training_figure_manifest.json').write_text(json.dumps(report, indent=2)+'\n')
    return report


# Entry points.

def run_circles(args):
    load_plotting(sphere=False, font_dir=args.font_dir)
    args.out.mkdir(parents=True, exist_ok=True)
    if (args.out/'manifest.json').exists():
        raise FileExistsError('Choose a fresh output directory; existing render manifests are preserved')
    inputs = None
    if args.bundle:
        groups = load_circle_bundle(args.bundle)
    else:
        inputs = CircleInputs(args.root)
        groups = {'deep': inputs.deep(), 'shallow': inputs.shallow()}
    save_circle_bundle(args.out/'radial_source_data.npz', groups)
    outputs = []
    for depth, panels in groups.items():
        path = args.out/f'circle_{depth}_radial'
        draw_circle_figure(panels, path, depth)
        outputs.extend([path.with_suffix('.pdf'), path.with_suffix('.svg')])
        if not args.no_png:
            executable = shutil.which('pdftoppm')
            if executable is None:
                raise RuntimeError('pdftoppm is required for PNG previews; use --no-png for vector-only export')
            subprocess.run([executable, '-r', str(args.dpi), '-png', '-singlefile',
                            str(path.with_suffix('.pdf')), str(path)], check=True)
            outputs.append(path.with_suffix('.png'))
    manifest = {'scope': 'Saved-figure replot only; no new training or empirical validation',
        'source_sha256': sha(__file__), 'command': sys.argv,
        'python': platform.python_version(), 'numpy': np.__version__,
        'radius': '3 + signed prediction; fixed common scale across all panels',
        'query_points': 8192, 'smoothing': False, 'decimation': False,
        'source_records': inputs.records if inputs else {'bundle': {'path': str(args.bundle), 'sha256': sha(args.bundle)}},
        'metric_checks': inputs.checks if inputs else 'All bundled RMS values recomputed',
        'source_bundle_sha256': sha(args.out/'radial_source_data.npz'),
        'outputs': {p.name: sha(p) for p in outputs}}
    (args.out/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps({'outputs': [str(p) for p in outputs],
                      'rms_checks': sum(len(p.rms) for panels in groups.values() for p in panels)}, indent=2))


def run_spheres(args):
    load_plotting(sphere=True, font_dir=args.font_dir)
    args.out.mkdir(parents=True, exist_ok=True)
    if (args.out/'manifest.json').exists():
        raise FileExistsError('Use a fresh output directory')
    if args.bundle:
        with np.load(args.bundle, allow_pickle=False) as z:
            data = {key: z[key].copy() for key in z.files if key != 'metadata_json'}
            metadata = json.loads(str(z['metadata_json']))
        for p in ('P1', 'P2', 'P3'):
            actual = float(np.sqrt(np.mean((data[p]-data['dense'])**2)))
            if not np.isclose(actual, metadata['rms'][p], rtol=1e-12, atol=1e-14):
                raise ValueError('Bundled RMS mismatch')
    else:
        data, metadata = load_sphere_source(args.source)
    np.savez_compressed(args.out/'sphere_source_data.npz', **data,
                        metadata_json=np.asarray(json.dumps(metadata)))
    surface = SphereSurface(data['test_inputs'])
    # Interpolation must recover all stored vertex values before any rendering.
    indices, weights = surface.locate(data['test_inputs'])
    vertex_error = max(float(np.max(np.abs(np.sum(data[key][indices]*weights, axis=1)-data[key])))
                       for key in ('dense', 'P1', 'P2', 'P3'))
    if vertex_error > 1e-10:
        raise ValueError('Surface interpolation fails the stored-vertex check')
    coordinates = {back: surface.texture_coordinates(args.resolution, back) for back in (False, True)}
    if sum(int(np.sum(data['inputs'] @ sphere_camera(back)[2] > 0)) for back in (False, True)) != 64:
        raise ValueError('Hemisphere views do not display every training point exactly once')
    outputs = []
    for kind in ('orders', 'comparison'):
        path = args.out/f'sphere_{kind}'
        draw_sphere_figure(path, data, metadata, coordinates, kind)
        outputs += [path.with_suffix('.pdf'), path.with_suffix('.svg')]
        if not args.no_png:
            subprocess.run(['pdftoppm', '-r', str(args.dpi), '-png', '-singlefile',
                            str(path.with_suffix('.pdf')), str(path)], check=True)
            outputs.append(path.with_suffix('.png'))
    report = {'scope': 'Replot saved predictions only; no new training or model evaluation',
        'source_sha256': {Path(__file__).name: sha(__file__)},
        'command': sys.argv, 'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__,
        'source_records': metadata['source_records'], 'checks': metadata['checks'],
        'source_directory': metadata['source_directory'],
        'sphere_query_count': len(data['test_inputs']), 'triangle_count': len(surface.triangles),
        'vertex_reconstruction_max_error': vertex_error,
        'barycentric_weight_sum_max_error': surface.maximum_weight_defect,
        'camera_front': VIEW.tolist(), 'camera_back': (-VIEW).tolist(),
        'output_color_limits': [-OUTPUT_LIMIT, OUTPUT_LIMIT], 'error_color_limits': [-ERROR_LIMIT, ERROR_LIMIT],
        'texture': 'Piecewise-linear triangular interpolation of saved values; no lighting or fitted smoothing',
        'texture_resolution': args.resolution, 'training_points_displayed': 64,
        'qualification': 'One seed; float32 Euler step 1/128; separate endpoint times; no continuous-GF refinement certificate',
        'outputs': {p.name: sha(p) for p in outputs},
        'source_bundle_sha256': sha(args.out/'sphere_source_data.npz')}
    (args.out/'manifest.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'rms': metadata['rms'], 'vertex_check': vertex_error, 'outputs': [str(p) for p in outputs]}, indent=2))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)

    def plotting_arguments(command, *, dpi, resolution=None):
        command.add_argument('--out', type=Path, required=True)
        command.add_argument('--no-png', action='store_true')
        command.add_argument('--dpi', type=int, default=dpi)
        command.add_argument('--font-dir', type=Path, default=FONT_DIR)
        if resolution is not None:
            command.add_argument('--resolution', type=int, default=resolution)

    circles = commands.add_parser('circles', help='Render both circle figures from saved arrays')
    plotting_arguments(circles, dpi=240)
    circles.add_argument('--root', type=Path, default=ROOT)
    circles.add_argument('--bundle', type=Path)

    spheres = commands.add_parser('spheres', help='Render the two endpoint sphere layouts')
    plotting_arguments(spheres, dpi=260, resolution=768)
    spheres.add_argument('--source', type=Path, default=ROOT/
        'data/generated/neural_response_memory_20260922/compact_sphere01/xyz_m64')
    spheres.add_argument('--bundle', type=Path)

    capture = commands.add_parser('training-capture', help='Record new sphere stages on CUDA; no rendering')
    capture.add_argument('--out', type=Path, required=True)
    capture.add_argument('--device', default='cuda:0')
    capture.add_argument('--seconds', type=float, default=60.)
    capture.add_argument('--hidden-gain', type=float, default=1.)
    capture.add_argument('--readout-std', type=float, default=1/2048)

    training = commands.add_parser('training-render', help='Render genuine recorded stages or labelled validation fixtures')
    plotting_arguments(training, dpi=280, resolution=640)
    training.add_argument('--bundle', type=Path, required=True)
    args = parser.parse_args()
    if args.command == 'circles':
        run_circles(args)
    elif args.command == 'spheres':
        run_spheres(args)
    elif args.command == 'training-capture':
        print(capture_training(args))
    else:
        render_training(args.bundle, args.out, args.no_png, dpi=args.dpi,
                        resolution=args.resolution, font_dir=args.font_dir)


if __name__ == '__main__':
    main()
