#!/usr/bin/env python3
"""Build standalone HTML pages, thumbnails and a thumbnail index for the explainer figures.

Usage:
    python paper/figures/explainers/build_html.py [--json data/generated/explainer_figures_20261009/json]
                                                  [--no-thumbs] [--force-thumbs]

Each fragments/<name>.frag is the exact widget code shown in conversation.
With --json, the data-driven fragments are first regenerated from
templates/<name>.tpl and json/<figNN>.json (written by scripts/export_data.py).
Every fragment is then wrapped into html/<name>.html. A page is rewritten only
when its content changes, and thumbs/<name>.webp is regenerated (headless
Firefox) only when it is missing or older than its page, so adding a fragment
and rerunning this script adds its card to index.html.

index.html also lists, when served over HTTP, any page in html/ that this
script has not indexed yet, with a live preview in place of a thumbnail.
"""
import argparse
import hashlib
import html
import json
import queue
import re
import shutil
import subprocess
import tempfile
import threading
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Status of each figure: (label, note). Superseded versions are kept for reference.
STATUS = {
    'fig01': ('rejected', 'learning clock, equal-area bands'),
    'fig02': ('superseded by 15–17', 'Legendre product of tails'),
    'fig03': ('superseded by 18b', 'pick, do not mix'),
    'fig04': ('superseded by 19c', 'price of random neurons'),
    'fig05': ('superseded by 21c', 'caps on the sphere'),
    'fig06': ('rejected', 'flaring analytic disks'),
    'fig07': ('rejected', 'feedback amplification'),
    'fig08': ('superseded by 20c', 'rotated petals'),
    'fig09': ('duplicate of 4', 'resampled neurons'),
    'fig10': ('rejected', 'response block, three axes'),
    'fig11': ('rejected', 'function-space tubes'),
    'fig12': ('rejected', 'commuting diagrams'),
    'fig13': ('rejected', 'clock and moments, static'),
    'fig14': ('rejected', 'spectral decay and flaring, static'),
    'fig15': ('superseded by 15c', 'trail fades, moments remember (illustrative)'),
    'fig15b': ('superseded by 15c', 'same, real histories, polynomial continuation'),
    'fig15c': ('current', 'moments are enough to continue (real, restarted moment model)'),
    'fig16': ('appendix candidate', 'moments are averaged derivatives'),
    'fig16b': ('superseded by 16c', 'clock folds infinite run (fitted tail)'),
    'fig16c': ('current, appendix', 'clock folds an infinite run (real, t to 112)'),
    'fig17': ('superseded by 17c', 'pairing grid'),
    'fig17b': ('superseded by 17c', 'Mondrian, illustrative moments'),
    'fig17c': ('current', 'Mondrian of real moments, click a cell for orthogonality'),
    'fig18': ('superseded by 18b', 'chord and curve'),
    'fig18b': ('current', 'pick and weigh, do not mix (four steps)'),
    'fig19': ('superseded by 19c', 'random vs selected, width chart'),
    'fig19b': ('superseded by 19c', 'sampling slider restored'),
    'fig19c': ('current', 'price of random neurons by width'),
    'fig20': ('superseded by 20c', 'rotated petals with kernel check'),
    'fig20b': ('superseded by 20c', 'decluttered petals'),
    'fig20c': ('current', 'petals spelled with Fourier shapes'),
    'fig21': ('superseded by 21c', 'rotation shuffles within a degree (zonal toy)'),
    'fig21b': ('superseded by 21c', 'real neuron, degree cutoff'),
    'fig21c': ('current', 'real neuron in a spherical-harmonic pyramid'),
}

HEAD = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
:root{{--p:#1f1f1e;--s:#6b6b68;--t:#888780;--b:#c8c6bd;--text-primary:#1f1f1e;--text-secondary:#6b6b68;
--text-muted:#9a9890;--border:rgba(0,0,0,.12);--border-strong:rgba(0,0,0,.25);--surface-1:#f4f3ef;
--surface-2:#fff;--bg-success:#e3f3e8;--text-success:#1d6b3a;--radius:8px;--page:#fbfaf7}}
@media (prefers-color-scheme: dark){{:root{{--p:#ecebe6;--s:#a8a69e;--t:#8f8d86;--b:#55544f;
--text-primary:#ecebe6;--text-secondary:#a8a69e;--text-muted:#7d7b75;--border:rgba(255,255,255,.14);
--border-strong:rgba(255,255,255,.28);--surface-1:#2a2a28;--surface-2:#222220;--bg-success:#1f3b29;
--text-success:#8fd3a5;--page:#1c1c1b}}}}
body{{margin:0;padding:24px 16px;background:var(--page);color:var(--text-primary);
font-family:system-ui,-apple-system,"Segoe UI",sans-serif}}
main{{max-width:{width}px;margin:0 auto}}
.sr-only{{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}}
svg text.th{{font-size:14px;font-weight:500;fill:var(--text-primary)}}
svg text.t{{font-size:14px;fill:var(--text-primary)}}
svg text.ts{{font-size:12px;fill:var(--text-secondary)}}
button,select{{font:inherit;color:var(--text-primary);background:transparent;border:.5px solid var(--border-strong);
border-radius:var(--radius);cursor:pointer}}
button:hover{{background:var(--surface-1)}}
input[type=range]{{accent-color:#2a78d6}}
nav{{font-size:13px;margin-bottom:16px}} nav a{{color:var(--text-secondary)}}
</style></head><body><main>
"""
NAV = '<nav><a href="../index.html">All explainer figures</a></nav>\n'
TAIL = "\n</main></body></html>\n"

# Screenshot geometry: window size, then the crop (page minus the nav line) and the thumbnail size.
SHOT_W, SHOT_H = 760, 700
CROP = (22, 50, 738, 587)
THUMB = (480, 360)

INDEX_BODY = """<h1 style="font-size:20px;font-weight:500;margin:0 0 4px">Explainer figures</h1>
<p style="color:var(--text-secondary);font-size:14px;margin:0 0 20px">Interactive sketches of the three compression
mechanisms. Click a card to open the figure. See README.md for data and reproduction.</p>
<style>
h2{font-size:16px;font-weight:500;margin:24px 0 10px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:14px}
.card{display:flex;flex-direction:column;text-decoration:none;color:inherit;border:.5px solid var(--border);
border-radius:12px;overflow:hidden;background:var(--surface-2)}
.card:hover{border-color:var(--border-strong)}
.card:hover .shot img{transform:scale(1.03)}
.shot{aspect-ratio:4/3;background:#fbfaf7;position:relative;overflow:hidden;border-bottom:.5px solid var(--border)}
.shot img{width:100%;height:100%;object-fit:cover;object-position:top;display:block;transition:transform .2s}
.shot iframe{position:absolute;left:0;top:0;width:760px;height:600px;border:0;transform-origin:0 0;pointer-events:none}
.meta{padding:8px 10px 10px;font-size:13px;line-height:1.4;display:flex;flex-direction:column;gap:2px}
.title{font-weight:500}
.note{color:var(--text-secondary)}
.pill{align-self:flex-start;margin-top:4px;font-size:11px;padding:1px 7px;border-radius:var(--radius);
background:var(--surface-1);color:var(--text-secondary)}
.pill.cur{background:var(--bg-success);color:var(--text-success)}
</style>
<h2>Current</h2><div class="grid" id="cur"></div>
<section id="newsec" hidden><h2>Not yet indexed</h2><div class="grid" id="new"></div></section>
<h2>Earlier versions</h2><div class="grid" id="old"></div>
<script>
const PAGES=__MANIFEST__;
function live(shot,href){const f=document.createElement('iframe');f.src=href;f.loading='lazy';f.tabIndex=-1;
f.setAttribute('aria-hidden','true');shot.appendChild(f);
const fit=()=>{f.style.transform=`scale(${shot.clientWidth/716}) translate(-22px,-50px)`};fit();new ResizeObserver(fit).observe(shot)}
function card(p,box){const a=document.createElement('a');a.className='card';a.href='html/'+p.file;
const shot=document.createElement('div');shot.className='shot';a.appendChild(shot);
if(p.thumb){const img=new Image();img.alt='';img.src=p.thumb;img.onerror=()=>{img.remove();live(shot,a.href)};shot.appendChild(img)}
else live(shot,a.href);
const m=document.createElement('div');m.className='meta';
m.innerHTML=`<span class="title"></span><span class="note"></span>${p.status?'<span class="pill"></span>':''}`;
m.children[0].textContent=(p.key?p.key+' · ':'')+p.title;m.children[1].textContent=p.note||'';
const cur=p.status.startsWith('current')||p.status==='new';
if(p.status){m.children[2].textContent=p.status;if(cur)m.children[2].classList.add('cur')}
a.appendChild(m);document.getElementById(box).appendChild(a)}
PAGES.forEach(p=>card(p,p.status.startsWith('current')||p.status==='new'?'cur':'old'));
if(location.protocol.startsWith('http'))fetch('html/').then(r=>r.ok?r.text():'').then(t=>{
const known=new Set(PAGES.map(p=>p.file));
const found=[...new Set([...t.matchAll(/href="([^"?#\\/]+\\.html)"/g)].map(m=>decodeURIComponent(m[1])))].filter(f=>!known.has(f)).sort();
found.forEach(f=>card({file:f,key:'',title:f.replace(/\\.html$/,''),note:'live preview; run build_html.py to index',status:''},'new'));
if(found.length)document.getElementById('newsec').hidden=false}).catch(()=>{});
</script>"""


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def write_if_changed(path, text):
    if not path.exists() or path.read_text() != text:
        path.write_text(text)


def make_thumbs(pages, force, workers=4):
    """Screenshot each page whose thumbnail is missing or stale; crop the nav line and shrink."""
    thumb_dir = HERE/'thumbs'
    thumb_dir.mkdir(exist_ok=True)
    todo = [p for p in pages if force or not (thumb_dir/f'{p.stem}.webp').exists()
            or (thumb_dir/f'{p.stem}.webp').stat().st_mtime < p.stat().st_mtime]
    if not todo:
        return
    firefox = shutil.which('firefox')
    if not firefox:
        print('firefox not found; skipping', len(todo), 'thumbnails (the index shows live previews)')
        return
    from PIL import Image
    # Snap Firefox can only write under ~/snap/firefox/common.
    snap = Path.home()/'snap/firefox/common'
    work = Path(tempfile.mkdtemp(prefix='explainer-thumbs-', dir=snap if snap.is_dir() else None))
    server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(HERE)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    profiles = queue.Queue()
    for k in range(workers):
        (work/f'profile{k}').mkdir()
        profiles.put(work/f'profile{k}')

    def shoot(page):
        profile, png = profiles.get(), work/f'{page.stem}.png'
        try:
            subprocess.run([firefox, '--headless', '--no-remote', '--profile', str(profile),
                            f'--window-size={SHOT_W},{SHOT_H}', '--screenshot', str(png),
                            f'http://127.0.0.1:{server.server_address[1]}/html/{page.name}'],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
        finally:
            profiles.put(profile)
        if not png.exists():
            return f'failed {page.stem}'
        Image.open(png).convert('RGB').crop(CROP).resize(THUMB, Image.LANCZOS).save(
            thumb_dir/f'{page.stem}.webp', 'WEBP', quality=88)
        return f'thumbnail {page.stem}'

    try:
        with ThreadPoolExecutor(workers) as pool:
            for msg in pool.map(shoot, todo):
                print(msg)
    finally:
        server.shutdown()
        shutil.rmtree(work)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--json', type=Path, help='directory with figNN.json from scripts/export_data.py')
    ap.add_argument('--no-thumbs', action='store_true', help='do not generate thumbnails')
    ap.add_argument('--force-thumbs', action='store_true', help='regenerate every thumbnail')
    args = ap.parse_args()
    frag_dir, out_dir = HERE/'fragments', HERE/'html'
    out_dir.mkdir(exist_ok=True)
    if args.json:
        for tpl in sorted((HERE/'templates').glob('*.tpl')):
            data = args.json/f"{tpl.stem.split('_')[0]}.json"
            write_if_changed(frag_dir/f'{tpl.stem}.frag', tpl.read_text().replace('__DATA__', data.read_text()))
            print('regenerated', tpl.stem)
    pages, manifest = [], []
    for frag in sorted(frag_dir.glob('*.frag')):
        code = frag.read_text()
        m = re.search(r'<title>(.*?)</title>', code)
        title = html.unescape(m.group(1)) if m else frag.stem
        page = out_dir/f'{frag.stem}.html'
        write_if_changed(page, HEAD.format(title=html.escape(title), width=700) + NAV + code + TAIL)
        pages.append(page)
        key = frag.stem.split('_')[0]
        status, note = STATUS.get(key, ('new', ''))
        short = re.sub(r'^Figure \w+:\s*', '', title)
        manifest.append(dict(file=page.name, key=key[3:], title=short[:1].upper() + short[1:],
                             note=note, status=status))
    if not args.no_thumbs:
        make_thumbs(pages, args.force_thumbs)
    for entry in manifest:
        thumb = HERE/'thumbs'/entry['file'].replace('.html', '.webp')
        # Content hash, not mtime, so a checkout or revert rebuilds the same index.
        entry['thumb'] = (f"thumbs/{thumb.name}?v={hashlib.sha1(thumb.read_bytes()).hexdigest()[:10]}"
                          if thumb.exists() else '')
    body = INDEX_BODY.replace('__MANIFEST__', json.dumps(manifest, ensure_ascii=False).replace('</', '<\\/'))
    write_if_changed(HERE/'index.html', HEAD.format(title='Explainer figures', width=1100) + body + TAIL)
    print('wrote', len(pages), 'pages and index.html')


if __name__ == '__main__':
    main()
