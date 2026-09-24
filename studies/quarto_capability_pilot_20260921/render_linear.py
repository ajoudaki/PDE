"""Render a verified contiguous book prefix without modifying the old book."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assemble(packet_path):
    """Return the packet, verified piece records, and byte-exact prefix source."""
    packet_path = packet_path.resolve()
    base = packet_path.parent
    packet = json.loads(packet_path.read_text())
    progress = json.loads((base / packet['progress']).read_text())
    sources = json.loads((base / packet['sources']).read_text())['files']
    pieces = []
    source_index = 0
    expected_start = 1
    for item in progress['accepted'] + [packet]:
        if source_index >= len(sources):
            raise ValueError('Packet does not continue the source manifest')
        source = sources[source_index]
        if (item['source'] != source['source'] or item['start'] != expected_start
                or not item['start'] <= item['end'] <= source['lines']):
            raise ValueError('Packet does not continue the accepted prefix')
        path = base / item['candidate']
        actual = sha256(path)
        if 'candidate_sha256' in item and actual != item['candidate_sha256']:
            raise ValueError(f'Accepted candidate hash mismatch: {path.name}')
        pieces.append(dict(packet=item.get('packet', item.get('id')), candidate=path.name,
                           source=item['source'], qmd=source['qmd'],
                           start=item['start'], end=item['end'], sha256=actual))
        expected_start = item['end'] + 1
        if item['end'] == source['lines']:
            source_index += 1
            expected_start = 1
    return packet, pieces, b''.join((base / p['candidate']).read_bytes() for p in pieces)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('packet', type=Path)
    parser.add_argument('--quarto', required=True, type=Path)
    parser.add_argument('--run-directory', required=True, type=Path)
    args = parser.parse_args()
    packet_path = args.packet.resolve()
    base = packet_path.parent
    packet, pieces, assembled = assemble(packet_path)
    tooling = base.parents[1] / 'data/generated' / base.name / 'batch02-render-tooling'
    browser = tooling / 'browser/chrome-headless-shell-linux64/chrome-headless-shell'
    browser_launcher = tooling / 'browser/chrome-padded-viewport'
    run = args.run_directory.resolve()
    run.mkdir(parents=True, exist_ok=False)
    book = run / 'book'
    book.mkdir()
    inputs = run / 'inputs'
    inputs.mkdir()
    paths = [packet_path, base / 'migration_rules.md', base / 'migration_quarto.yml']
    batch_rules = base / 'migration_batch02_rules.md'
    if batch_rules.is_file():
        paths.append(batch_rules)
    render_rules = base / 'migration_render_rules.md'
    if render_rules.is_file():
        paths.append(render_rules)
    table_filter = base / 'pdf_breakable_tables.lua'
    if table_filter.is_file():
        paths.append(table_filter)
    if browser_launcher.is_file():
        paths.append(browser_launcher)
    paths += [base / packet[key] for key in ('candidate', 'edits', 'targets', 'sources', 'registry', 'progress')]
    paths += [base / piece['candidate'] for piece in pieces[:-1]]
    paths = list(dict.fromkeys(paths))
    for path in paths:
        shutil.copyfile(path, inputs / path.name)
    hashes = {p.name: sha256(p) for p in paths}
    (run / 'input_hashes.json').write_text(json.dumps(hashes, indent=2) + '\n')
    (inputs / 'assembled.qmd').write_bytes(assembled)
    chapters = {}
    for piece in pieces:
        chapters.setdefault(piece['qmd'], bytearray()).extend((base / piece['candidate']).read_bytes())
    for name, content in chapters.items():
        (book / name).write_bytes(content)
    assembly = dict(source=packet['source'], start=1, end=packet['end'], pieces=pieces,
                    assembled='assembled.qmd', sha256=hashlib.sha256(assembled).hexdigest(),
                    chapters=[dict(qmd=name, sha256=hashlib.sha256(content).hexdigest())
                              for name, content in chapters.items()])
    (run / 'assembled_source.json').write_text(json.dumps(assembly, indent=2) + '\n')
    config = (base / 'migration_quarto.yml').read_text()
    assert config.count('    - index.qmd\n') == 1
    config = config.replace('    - index.qmd\n', ''.join(f'    - {name}\n' for name in chapters))
    (book / '_quarto.yml').write_text(config)
    if table_filter.is_file():
        shutil.copyfile(table_filter, book / table_filter.name)
    env = dict(os.environ, XDG_CACHE_HOME=str(run / 'cache'), XDG_CONFIG_HOME=str(run / 'config'))
    if browser_launcher.is_file() and browser.is_file():
        env['QUARTO_CHROMIUM'] = str(browser_launcher)
    elif browser.is_file():
        env['QUARTO_CHROMIUM'] = str(browser)
    commands = []
    for fmt in ('html', 'pdf', 'latex'):
        command = [str(args.quarto.resolve()), 'render', '--to', fmt, '--output-dir', '_out-' + fmt]
        with (run / (fmt + '.log')).open('w') as log:
            proc = subprocess.run(command, cwd=book, env=env, stdout=log, stderr=subprocess.STDOUT, timeout=180)
        commands.append(dict(command=command, cwd=str(book), exit_code=proc.returncode))
        (run / 'commands.json').write_text(json.dumps(commands, indent=2) + '\n')
        print(fmt, proc.returncode, flush=True)
    raise SystemExit(any(c['exit_code'] for c in commands))


if __name__ == '__main__':
    main()
