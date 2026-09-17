"""Embed saved study data into the literal, study-owned viewer fragment."""
import argparse
import base64
import gzip
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--display', type=Path, required=True)
    args = parser.parse_args()
    source = Path(__file__).with_name('RADIAL_VIEWER.html')
    raw = args.data.read_bytes()
    data = json.loads(raw)
    payload = base64.b64encode(gzip.compress(raw, compresslevel=9, mtime=0)).decode('ascii')
    template = source.read_text()
    assert template.count('__COMPRESSED_VIEWER_DATA__') == 1
    rendered = template.replace('__COMPRESSED_VIEWER_DATA__', payload).encode()
    assert len(rendered) < 1_000_000, f'Fragment too large: {len(rendered)} bytes'
    for path in (args.output, args.display):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(rendered)
    report = {'cases': len(data['cases']), 'fragment_bytes': len(rendered),
              'sha256': hashlib.sha256(rendered).hexdigest(),
              'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'data_sha256': hashlib.sha256(raw).hexdigest(),
              'output': str(args.output.resolve()), 'display': str(args.display.resolve())}
    args.output.with_name('build_check.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
