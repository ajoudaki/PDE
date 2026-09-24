"""Partial-edition reference gate: only exact registered future targets may be missing."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from reference_gate import Page


def check(run):
    failures = []
    inputs = run / 'inputs'
    packet_files = list(inputs.glob('linear_*_packet.json'))
    if len(packet_files) != 1:
        raise ValueError('Expected exactly one frozen packet')
    packet = json.loads(packet_files[0].read_text())
    manifest = json.loads((inputs / packet['sources']).read_text())
    sources = {s['source']: s for s in manifest['files']}
    assembly_path = run / 'assembled_source.json'
    if assembly_path.is_file():
        assembly = json.loads(assembly_path.read_text())
        assembled_path = inputs / assembly['assembled']
        assembled = assembled_path.read_bytes()
        if hashlib.sha256(assembled).hexdigest() != assembly['sha256']:
            failures.append('assembled source hash mismatch')
        if 'chapters' in assembly:
            rendered = []
            for chapter in assembly['chapters']:
                content = (run / 'book' / chapter['qmd']).read_bytes()
                rendered.append(content)
                if hashlib.sha256(content).hexdigest() != chapter['sha256']:
                    failures.append(f"chapter source hash mismatch: {chapter['qmd']}")
            if b''.join(rendered) != assembled:
                failures.append('rendered chapters differ from frozen assembled source')
        elif (run / 'book/index.qmd').read_bytes() != assembled:
            failures.append('rendered index differs from frozen assembled source')
        candidate = assembled.decode()
    else:
        # Compatibility with the accepted packet-001 run and frozen audit.
        candidate = (inputs / packet['candidate']).read_text()
    entries = json.loads((inputs / packet['registry']).read_text()) + json.loads((inputs / packet['targets']).read_text())
    targets = {}
    for entry in entries:
        previous = targets.get(entry['id'])
        if previous is not None and previous != entry:
            failures.append(f"conflicting registry entries: {entry['id']}")
        targets[entry['id']] = entry
    defined = set(re.findall(r'\{#([a-z0-9-]+)\}', candidate))
    unknown_defined = defined - set(targets)
    if unknown_defined:
        failures.append(f'unregistered defined targets: {sorted(unknown_defined)}')
    reserved = set(targets) - defined
    expected_native = Counter(re.findall(r'@([a-z]+-[a-z0-9-]+)', candidate))
    expected_native = Counter({k: v for k, v in expected_native.items() if k in reserved})
    expected_links = Counter(key for _, key in re.findall(r'\]\(([^)\s]+\.qmd)#([a-z0-9-]+)\)', candidate) if key in reserved)
    pending_urls = {}
    for key in expected_links:
        filename = sources[targets[key]['source']]['qmd']
        # Quarto can retain a future .qmd URL or rewrite it to the eventual HTML.
        for output_name in (filename, str(Path(filename).with_suffix('.html'))):
            pending_urls[output_name + '#' + key] = key
    directory = run / 'book' / '_out-html'
    texts = {p.resolve(): p.read_text() for p in directory.rglob('*.html')}
    pages = {p: Page(t) for p, t in texts.items()}
    pending_links = []
    seen_pending_links = Counter()
    if not pages:
        failures.append('no HTML output')
    seen_ids = Counter(k for p in pages.values() for k in p.ids if k in targets)
    for key in defined:
        if seen_ids[key] != 1:
            failures.append(f'defined target missing/duplicated in HTML: {key}')
    for path, page in pages.items():
        if page.duplicates:
            failures.append(f'duplicate HTML IDs in {path.name}: {page.duplicates}')
        for href in page.links:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            if href in pending_urls:
                pending_links.append(href)
                seen_pending_links[pending_urls[href]] += 1
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if target.suffix in ('.html', '.qmd'):
                if target not in pages or (url.fragment and unquote(url.fragment) not in pages[target].ids):
                    failures.append(f'unknown broken link in {path.name}: {href}')
    if seen_pending_links != expected_links:
        failures.append(f'future links differ from source: {dict(seen_pending_links)} vs {dict(expected_links)}')
    unresolved = Counter()
    for text in texts.values():
        unresolved.update(re.findall(r'class="quarto-unresolved-ref">\?([^<]+)</span>', text))
    if unresolved != expected_native:
        failures.append(f'unresolved HTML refs differ from reservations: {dict(unresolved)} vs {dict(expected_native)}')
    diagnostics = []
    for fmt in ('html', 'pdf', 'latex'):
        path = run / (fmt + '.log')
        if not path.is_file():
            failures.append(f'missing {fmt} log')
            continue
        for line in path.read_text().splitlines():
            if 'Unable to resolve crossref' in line:
                match = re.search(r'Unable to resolve crossref @([a-z]+-[a-z0-9-]+)\s*$', line)
                if not match or match[1] not in expected_native:
                    failures.append(line)
                else:
                    diagnostics.append(dict(format=fmt, target=match[1]))
            elif 'Unable to resolve link target:' in line:
                match = re.search(r'Unable to resolve link target: ([^\s]+)\s*$', line)
                pending_files = {urlsplit(url).path for url in pending_urls}
                if not match or match[1] not in pending_files:
                    failures.append(line)
                else:
                    diagnostics.append(dict(format=fmt, future_file=match[1]))
            elif re.search(r'citation .+ not found|Duplicate identifier|undefined citations|undefined references', line, re.I):
                failures.append(line)
    commands = json.loads((run / 'commands.json').read_text())
    if len(commands) != 3 or any(c['exit_code'] for c in commands):
        failures.append('not all three formats built successfully')
    return dict(pass_partial=not failures, failures=failures, defined=sorted(defined),
                reserved=sorted(reserved), pending_native=dict(expected_native),
                pending_links=sorted(set(pending_links)), expected_diagnostics=diagnostics,
                complete_edition=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run', type=Path)
    args = parser.parse_args()
    result = check(args.run.resolve())
    print(json.dumps(result, indent=2))
    raise SystemExit(not result['pass_partial'])
