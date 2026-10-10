"""Small array-only circle/sphere plots and an offline comparison viewer.

Directions are normalized inputs v=x/sqrt(d), with unit rows. Predictions
are supplied values, not evaluated or rescaled by this module. See code/PREDICTION_VIEWS.md.
"""
from collections.abc import Mapping
import json
from pathlib import Path

import numpy as np


def _directions(values, dimension=None, *, allow_empty=False):
    values = np.asarray(values, dtype=float)
    if (values.ndim != 2 or values.shape[1] not in (2, 3)
            or (dimension is not None and values.shape[1] != dimension)
            or (not allow_empty and len(values) == 0)
            or not np.isfinite(values).all()
            or not np.allclose(np.linalg.norm(values, axis=1), 1., rtol=0., atol=1e-10)):
        raise ValueError('Directions must be finite unit rows with shape (N,2) or (N,3).')
    return values


def _prepare(queries, predictions, *, times=None, reference=None,
             training_inputs=None, training_labels=None):
    q = _directions(queries)
    if not isinstance(predictions, Mapping) or not predictions:
        raise ValueError('predictions must be a nonempty mapping of names to arrays.')
    arrays = {}
    for name, value in predictions.items():
        if not isinstance(name, str) or not name:
            raise ValueError('Model names must be nonempty strings.')
        value = np.asarray(value, dtype=float)
        if value.ndim == 1:
            value = value[None, :]
        if (value.ndim != 2 or value.shape[1] != len(q) or not len(value)
                or not np.isfinite(value).all()):
            raise ValueError('Each prediction must be finite with shape (N,) or (T,N).')
        arrays[name] = value
    if len({a.shape for a in arrays.values()}) != 1:
        raise ValueError('All models must have the same frame count and query order.')
    frames = next(iter(arrays.values())).shape[0]
    if times is not None:
        times = np.asarray(times, dtype=float)
        if (times.shape != (frames,) or not np.isfinite(times).all()
                or np.any(np.diff(times) <= 0)):
            raise ValueError('times must be finite, strictly increasing, and have length T.')
    if reference is not None and reference not in arrays:
        raise ValueError('reference must name a supplied prediction array.')
    train = (np.empty((0, q.shape[1])) if training_inputs is None else
             _directions(training_inputs, q.shape[1], allow_empty=True))
    labels = None
    if training_labels is not None:
        labels = np.asarray(training_labels, dtype=float)
        if training_inputs is None or labels.shape != (len(train),) or not np.isfinite(labels).all():
            raise ValueError('training_labels must be finite and align with training_inputs.')
    return q, arrays, times, train, labels


def _limit(values):
    """Finite symmetric data range; a zero field gets the nondegenerate range ±1."""
    maximum = max(float(np.max(np.abs(v))) for v in values if np.size(v))
    return maximum if maximum > 0 else 1.


def radial_coordinates(queries, values, *, limit):
    """Return (1 + 0.8*value/limit)*direction; negative values remain same-angle."""
    q = _directions(queries, 2)
    values = np.asarray(values, dtype=float)
    if (not np.isfinite(limit) or limit <= 0 or values.shape != (len(q),)
            or not np.isfinite(values).all() or np.any(np.abs(values) > limit)):
        raise ValueError('A finite positive limit must include every signed value.')
    return q * (1. + .8 * values / limit)[:, None]


def sphere_projection(queries, *, back=False):
    """Orthographic ±z cameras: front (x,y), back (-x,y); equator belongs to front."""
    q = _directions(queries, 3, allow_empty=True)
    xy = q[:, :2].copy()
    if back:
        xy[:, 0] *= -1
    visible = q[:, 2] < 0 if back else q[:, 2] >= 0
    return xy, visible


def _frame_index(frame, frames):
    if isinstance(frame, bool) or not isinstance(frame, (int, np.integer)) or not -frames <= frame < frames:
        raise ValueError('frame must be a valid integer frame index.')
    return frame % frames


def _circle_axes(ax, limit):
    from matplotlib.patches import Circle
    for value in (-limit, 0., limit):
        radius = 1. + .8 * value / limit
        ax.add_patch(Circle((0, 0), radius, fill=False, color='#89939c',
                            lw=1., ls='--' if value == 0 else ':'))
        ax.text(-radius / np.sqrt(2), radius / np.sqrt(2), f'{value:.3g}', fontsize=9,
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1})
    ax.axhline(0, color='#e1e5e9', lw=.7, zorder=0)
    ax.axvline(0, color='#e1e5e9', lw=.7, zorder=0)
    for x, y, label in ((2., 0., '0°'), (0., 2., '90°'), (-2., 0., '180°'), (0., -2., '270°')):
        ax.text(x, y, label, ha='center', va='center', fontsize=9)
    ax.set(xlim=(-2.3, 2.3), ylim=(-2.3, 2.3), aspect='equal')
    ax.set_axis_off()


def plot_circle(queries, predictions, *, frame=-1, reference=None,
                training_inputs=None, training_labels=None):
    """Plot supplied circle predictions and optional signed model-minus-reference errors.

    Curves join query samples in angular order. Scales include every supplied
    frame/model, and label markers if present; no per-curve normalization occurs.
    Training directions without labels are marked on the zero ring.
    """
    import matplotlib.pyplot as plt
    q, arrays, _, train, labels = _prepare(queries, predictions, reference=reference,
                                         training_inputs=training_inputs, training_labels=training_labels)
    if q.shape[1] != 2:
        raise ValueError('plot_circle requires two-dimensional unit directions.')
    frame = _frame_index(frame, next(iter(arrays.values())).shape[0])
    scale = _limit([*arrays.values(), [] if labels is None else labels])
    errors = {} if reference is None else {name: v - arrays[reference] for name, v in arrays.items()
                                          if name != reference}
    fig, axes = plt.subplots(1, 2 if errors else 1, figsize=(11 if errors else 6, 5.8), squeeze=False)
    order = np.argsort(np.arctan2(q[:, 1], q[:, 0]))
    order = np.r_[order, order[0]]
    palette = plt.get_cmap('tab10')
    for index, (name, values) in enumerate(arrays.items()):
        points = radial_coordinates(q, values[frame], limit=scale)
        axes[0, 0].plot(*points[order].T, label=name, color=palette(index % 10), lw=1.5)
    _circle_axes(axes[0, 0], scale)
    axes[0, 0].set_title('Prediction: radius = 1 + 0.8 f / scale')
    if len(train):
        markers = train if labels is None else radial_coordinates(train, labels, limit=scale)
        axes[0, 0].scatter(*markers.T, c='black', s=24, edgecolors='white', zorder=6,
                           label='training directions (zero ring)' if labels is None else 'training labels')
    axes[0, 0].legend(loc='lower center', bbox_to_anchor=(.5, -.14), ncol=2, fontsize=9)
    if errors:
        error_scale = _limit(errors.values())
        for index, (name, values) in enumerate(arrays.items()):
            if name == reference:
                continue
            points = radial_coordinates(q, errors[name][frame], limit=error_scale)
            rms = np.sqrt(np.mean(errors[name][frame] ** 2))
            axes[0, 1].plot(*points[order].T, color=palette(index % 10), lw=1.5,
                            label=f'{name}: sampled RMS {rms:.3g}')
        _circle_axes(axes[0, 1], error_scale)
        axes[0, 1].set_title(f'Signed error: model − {reference}')
        axes[0, 1].legend(loc='lower center', bbox_to_anchor=(.5, -.14), fontsize=9)
    fig.suptitle(f'Frame {frame} · dashed ring = zero · radial tick labels = signed values', fontsize=11)
    fig.text(.5, .015, f'{len(q)} supplied queries; curves join samples. RMS is a sample statistic, not a continuum norm.',
             ha='center', fontsize=9)
    fig.subplots_adjust(top=.88, bottom=.2, wspace=.24)
    return fig


def plot_sphere(queries, predictions, *, frame=-1, model=None, reference=None,
                training_inputs=None):
    """Plot complementary orthographic hemispheres using colors at supplied queries.

    Selected/reference predictions share one color scale; signed errors have a
    separate common scale over all supplied models/frames. No interpolation.
    """
    import matplotlib.pyplot as plt
    from matplotlib.colors import LinearSegmentedColormap, Normalize
    from matplotlib.patches import Circle
    q, arrays, _, train, _ = _prepare(queries, predictions, reference=reference,
                                     training_inputs=training_inputs)
    if q.shape[1] != 3:
        raise ValueError('plot_sphere requires three-dimensional unit directions.')
    model = next(iter(arrays)) if model is None else model
    if model not in arrays:
        raise ValueError('model must name a supplied prediction array.')
    frame = _frame_index(frame, next(iter(arrays.values())).shape[0])
    scale = _limit(arrays.values())
    columns = [(model, arrays[model][frame], scale)]
    if reference is not None:
        if model != reference:
            columns.append((reference, arrays[reference][frame], scale))
        error_scale = _limit([v - arrays[reference] for v in arrays.values()])
        error = arrays[model][frame] - arrays[reference][frame]
        rms = np.sqrt(np.mean(error ** 2))
        columns.append((f'{model} − {reference}\nsampled RMS {rms:.3g}', error, error_scale))
    fig, axes = plt.subplots(2, len(columns), figsize=(4.1 * len(columns), 8.5), squeeze=False)
    cmap = LinearSegmentedColormap.from_list('signed_samples', ['#2166ac', '#f7f7f7', '#b2182b'])
    size = max(3., min(45., 14000. / len(q)))
    for col, (name, values, limit) in enumerate(columns):
        for row, back in enumerate((False, True)):
            ax = axes[row, col]
            xy, visible = sphere_projection(q, back=back)
            dots = ax.scatter(*xy[visible].T, c=values[visible], cmap=cmap,
                              norm=Normalize(-limit, limit), s=size, linewidths=0, clip_on=True)
            ax.add_patch(Circle((0, 0), 1., fill=False, ec='#7c8790', lw=.8))
            if len(train):
                positions, show = sphere_projection(train, back=back)
                ax.scatter(*positions[show].T, c='black', s=18, edgecolors='white', linewidths=.6)
            ax.set(xlim=(-1.1, 1.1), ylim=(-1.1, 1.1), aspect='equal',
                   xlabel='−x (view from −z)' if back else 'x (view from +z)', ylabel='y')
            ax.set_title(name if row == 0 else ('back: z < 0' if back else 'front: z ≥ 0'), fontsize=10)
        bar = fig.colorbar(dots, ax=axes[:, col].tolist(), orientation='horizontal', fraction=.035, pad=.08,
                     ticks=[-limit, 0., limit], format='%.3g',
                     label='signed error' if reference is not None and col == len(columns) - 1 else 'prediction')
        # Keep endpoint text inside each bar so adjacent panels cannot collide.
        bar.ax.get_xticklabels()[0].set_horizontalalignment('left')
        bar.ax.get_xticklabels()[-1].set_horizontalalignment('right')
    fig.suptitle(f'Frame {frame} · orthographic ±z hemispheres · black dots = training inputs', fontsize=11)
    fig.text(.5, .02, f'{len(q)} supplied queries; no surface interpolation. RMS uses all queries with equal weights.',
             ha='center', fontsize=9)
    fig.subplots_adjust(top=.9, bottom=.2, wspace=.38, hspace=.4)
    return fig


def write_viewer(path, queries, predictions, *, times=None, reference=None,
                 training_inputs=None, training_labels=None, title='Prediction comparison'):
    """Write one offline HTML file with model/reference selectors, time slider and playback.

    All arrays are embedded; no network resources, model evaluation or training.
    Omitted times are labelled frame indices, never physical training time.
    """
    q, arrays, times, train, labels = _prepare(queries, predictions, times=times, reference=reference,
                                             training_inputs=training_inputs, training_labels=training_labels)
    names = list(arrays)
    packed = np.stack(list(arrays.values()))
    scale = _limit([packed, [] if labels is None or q.shape[1] == 3 else labels])
    # The maximum pairwise difference at each frame/query supports arbitrary
    # reference changes without color/radial scale changes.
    error_scale = _limit([packed.max(axis=0) - packed.min(axis=0)])
    payload = dict(title=str(title), dimension=q.shape[1], queries=q.tolist(), names=names,
                   predictions=packed.tolist(), times=None if times is None else times.tolist(),
                   reference=names.index(reference) if reference is not None else 0,
                   training_inputs=train.tolist(), training_labels=None if labels is None else labels.tolist(),
                   scale=scale, error_scale=error_scale)
    # HTML raw-text elements still recognize </script>; escape before embedding.
    encoded = json.dumps(payload, ensure_ascii=True, allow_nan=False, separators=(',', ':'))
    encoded = encoded.replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(_HTML.replace('__DATA__', encoded), encoding='utf-8')
    return path


_HTML = r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Prediction comparison</title><style>
*{box-sizing:border-box}body{margin:0;background:#f4f6f8;color:#182b3a;font:15px system-ui,sans-serif}
main{max-width:1250px;margin:auto;padding:24px}h1{font-size:26px;margin:0 0 8px}.note{line-height:1.55;color:#4a5d6d}
.controls{display:flex;gap:18px;flex-wrap:wrap;align-items:center;background:white;padding:16px;border-radius:10px;margin:18px 0}
select,button{font:inherit;padding:7px;border:1px solid #b5c1cb;border-radius:5px;background:white}input{vertical-align:middle}
.plots{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px}.panel{background:white;border:1px solid #dce3e9;border-radius:10px;padding:12px}
h2{font-size:16px;margin:0 0 6px;overflow-wrap:anywhere}canvas{display:block;width:100%;height:auto}.bar{height:12px;background:linear-gradient(to right,#2166ac,#f7f7f7,#b2182b)}
.ticks{display:flex;justify-content:space-between;font-size:12px;margin-top:3px}#metrics{padding:16px;background:#e8eef4;border-radius:8px;line-height:1.7;overflow-wrap:anywhere}
</style></head><body><main><h1 id="title"></h1><p class="note" id="description"></p>
<div class="controls"><label>Model <select id="model"></select></label><label>Reference <select id="reference"></select></label>
<button id="play" type="button">Play</button><label><span id="clock">Frame</span> <input id="frame" type="range" min="0" value="0" step="1"><output id="time"></output></label></div>
<div class="plots" id="plots"></div><p id="metrics" aria-live="polite"></p>
<p class="note">Scales are fixed across all supplied models and frames. Signed error means selected prediction minus reference prediction.
RMS and maximum absolute error are computed on the supplied queries with equal weights. They are sample statistics, not true continuum errors or error certificates.</p>
</main><script id="data" type="application/json">__DATA__</script><script>
'use strict';
const D=JSON.parse(document.getElementById('data').textContent);
const el=id=>document.getElementById(id), fmt=x=>Number(x).toPrecision(4);
el('title').textContent=D.title; document.title=D.title;
const circle=D.dimension===2, frames=D.predictions[0].length;
el('description').textContent=circle
  ? 'Circle directions set angle. Radius = 1 + 0.8 × signed value / scale; dashed ring = zero. Curves join supplied queries in angular order. Black dots mark training labels, or directions on the zero ring when labels are absent.'
  : 'Unit sphere, orthographic views from +z and −z. Front: (x,y), z ≥ 0; back: (−x,y), z < 0. Colors show supplied query values without surface interpolation. Black dots mark training directions.';
D.names.forEach((name,i)=>{for(const id of ['model','reference']){const o=document.createElement('option');o.value=i;o.textContent=name;el(id).appendChild(o);}});
el('reference').value=D.reference;el('model').value=D.names.length>1?(D.reference===0?1:0):0;
el('frame').max=frames-1;el('clock').textContent=D.times===null?'Frame':'Time';
el('play').disabled=frames<2;el('frame').disabled=frames<2;
const panels=[];
function makePanel(kind,back=false){const box=document.createElement('section');box.className='panel';
 const title=document.createElement('h2'),canvas=document.createElement('canvas');canvas.width=480;canvas.height=450;
 canvas.setAttribute('role','img');box.appendChild(title);box.appendChild(canvas);
 const scale=kind==='error'?D.error_scale:D.scale;
 if(!circle){const bar=document.createElement('div');bar.className='bar';box.appendChild(bar);
 const ticks=document.createElement('div');ticks.className='ticks';for(const x of [-scale,0,scale]){const s=document.createElement('span');s.textContent=fmt(x);ticks.appendChild(s);}box.appendChild(ticks);}
 el('plots').appendChild(box);panels.push({kind,back,title,canvas,scale});}
if(circle){makePanel('prediction');makePanel('error');}else{for(const back of [false,true]){makePanel('prediction',back);makePanel('reference',back);makePanel('error',back);}}
const order=D.queries.map((_,i)=>i).sort((a,b)=>Math.atan2(D.queries[a][1],D.queries[a][0])-Math.atan2(D.queries[b][1],D.queries[b][0]));
function text(ctx,s,x,y,color='#4a5d6d'){ctx.fillStyle=color;ctx.fillText(s,x,y);}
function dot(ctx,x,y,r,color){ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.fillStyle=color;ctx.fill();}
function ring(ctx,cx,cy,r){ctx.beginPath();ctx.arc(cx,cy,r,0,Math.PI*2);ctx.stroke();}
function curve(ctx,values,scale,color){ctx.strokeStyle=color;ctx.lineWidth=2;ctx.beginPath();
 for(let k=0;k<=order.length;k++){const j=order[k%order.length],r=(1+.8*values[j]/scale)*90;
 const x=240+r*D.queries[j][0],y=222-r*D.queries[j][1];if(k===0)ctx.moveTo(x,y);else ctx.lineTo(x,y);}ctx.stroke();}
function radial(panel,values,ref){const ctx=panel.canvas.getContext('2d');ctx.clearRect(0,0,480,450);ctx.font='13px system-ui';ctx.textAlign='center';
 for(const value of [-panel.scale,0,panel.scale]){const r=(1+.8*value/panel.scale)*90;ctx.strokeStyle='#9aa6af';ctx.lineWidth=1;ctx.setLineDash(value===0?[5,4]:[2,3]);ring(ctx,240,222,r);text(ctx,fmt(value),240-r/Math.sqrt(2),218-r/Math.sqrt(2));}ctx.setLineDash([]);
 for(const [s,x,y] of [['0°',438,226],['90°',240,22],['180°',37,226],['270°',240,430]])text(ctx,s,x,y);
 if(panel.kind==='prediction')curve(ctx,ref,panel.scale,'#525b64');curve(ctx,values,panel.scale,'#187aab');
 if(panel.kind==='prediction'){D.training_inputs.forEach((q,j)=>{const value=D.training_labels===null?0:D.training_labels[j],r=(1+.8*value/panel.scale)*90;dot(ctx,240+r*q[0],222-r*q[1],3.4,'#152a38');});}
 text(ctx,panel.kind==='prediction'?'blue: selected · gray: reference':'blue: signed error',240,449);
}
function color(value,scale){const t=value/scale,a=[247,247,247],b=t>=0?[178,24,43]:[33,102,172];return 'rgb('+a.map((v,i)=>Math.round(v+Math.abs(t)*(b[i]-v))).join(',')+')';}
function sphere(panel,values){const ctx=panel.canvas.getContext('2d');ctx.clearRect(0,0,480,450);ctx.font='13px system-ui';ctx.textAlign='center';
 const show=q=>panel.back?q[2]<0:q[2]>=0, sign=panel.back?-1:1,r=Math.max(1.4,Math.min(5,115/Math.sqrt(D.queries.length)));
 ctx.save();ctx.beginPath();ctx.arc(240,220,182,0,2*Math.PI);ctx.clip();
 D.queries.forEach((q,j)=>{if(show(q))dot(ctx,240+182*sign*q[0],220-182*q[1],r,color(values[j],panel.scale));});
 D.training_inputs.forEach(q=>{if(show(q)){dot(ctx,240+182*sign*q[0],220-182*q[1],4.1,'white');dot(ctx,240+182*sign*q[0],220-182*q[1],2.7,'#142a38');}});ctx.restore();
 ctx.strokeStyle='#8c9aa4';ctx.lineWidth=1;ctx.setLineDash([]);ring(ctx,240,220,182);
 text(ctx,panel.back?'−x → (view from −z)':'x → (view from +z)',240,428);text(ctx,'y ↑',35,220);
}
function update(){const m=Number(el('model').value),r=Number(el('reference').value),t=Number(el('frame').value);
 const value=D.predictions[m][t],ref=D.predictions[r][t],error=value.map((x,j)=>x-ref[j]);
 el('time').textContent=D.times===null?String(t):fmt(D.times[t]);
 for(const panel of panels){const values=panel.kind==='error'?error:panel.kind==='reference'?ref:value;
 const label=panel.kind==='error'?D.names[m]+' − '+D.names[r]:panel.kind==='reference'?D.names[r]+' (reference)':D.names[m];
 panel.title.textContent=label+(circle?'':panel.back?' · back z < 0':' · front z ≥ 0');panel.canvas.setAttribute('aria-label',panel.title.textContent);
 if(circle)radial(panel,values,ref);else sphere(panel,values);}
 const rms=Math.sqrt(error.reduce((a,x)=>a+x*x,0)/error.length),maximum=error.reduce((a,x)=>Math.max(a,Math.abs(x)),0);
 const lo=value.reduce((a,x)=>Math.min(a,x),Infinity),hi=value.reduce((a,x)=>Math.max(a,x),-Infinity);
 el('metrics').textContent=D.names[m]+' versus '+D.names[r]+' · '+(D.times===null?'frame '+t:'time '+fmt(D.times[t]))+' · '+error.length+' queries · sampled RMS '+fmt(rms)+' · sampled max |error| '+fmt(maximum)+' · selected range ['+fmt(lo)+', '+fmt(hi)+']';
}
for(const id of ['model','reference','frame'])el(id).addEventListener('input',update);
let timer=null;function stop(){if(timer!==null)clearInterval(timer);timer=null;el('play').textContent='Play';}
el('play').addEventListener('click',()=>{if(timer!==null){stop();return;}el('play').textContent='Pause';timer=setInterval(()=>{el('frame').value=(Number(el('frame').value)+1)%frames;update();},500);});
document.addEventListener('visibilitychange',()=>{if(document.hidden)stop();});update();
</script></body></html>'''
