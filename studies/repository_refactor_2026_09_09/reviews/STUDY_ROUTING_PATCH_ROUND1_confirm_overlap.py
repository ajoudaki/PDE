"""Confirm only the named-destination collision using private, inert writer bytes."""
import csv
import json
from pathlib import Path
from unittest import mock
import acceptance as q

root = q.PRIVATE / 'overlap-evidence'
root.mkdir()
args = q.arguments('g', root)
args.report = args.output_dir
env, loader = q.entry('g')
env['_preflight_analysis_outputs'](args)
with mock.patch.object(Path, 'mkdir') as mkdir:
    try:
        env['run_analysis'](args)
    except q.StopIngestion:
        pass
    else:
        raise AssertionError('whole-entry loader tripwire did not fire')
    mkdir.assert_not_called()
loader.assert_called_once_with(args.root / 'protocol/generalization_protocol.json')
assert list(root.iterdir()) == []
env['_preflight_analysis_outputs'](args)

# Use the actual writer bodies in actual publication order, with mock figures
# and ordinary inert text. This never enters the scientific routing middle,
# parses a protocol, verifies a seal, or reads an archive array.
writers = q.extract(q.G, {'_atomic_bytes', '_atomic_text', '_atomic_csv', '_atomic_figure'},
                    dict(Path=Path, os=q.os, csv=csv, require_output=q.gp.require_output, plt=mock.Mock()))
for name in q.GF:
    figure = mock.Mock()
    figure.savefig.side_effect = lambda handle, **kw: handle.write(b'inert figure')
    writers['_atomic_figure'](args.figures_dir / name, figure)
writers['_atomic_text'](args.output_dir / 'summary.json', 'inert summary; not analysis JSON\n')
for name in q.GN[1:]:
    writers['_atomic_csv'](args.output_dir / name, [{'inert': 'not scientific results'}])
try:
    writers['_atomic_text'](args.report, 'inert report\n')
except IsADirectoryError as exc:
    error = str(exc)
else:
    raise AssertionError('expected file-versus-directory publication failure')

published = [args.output_dir / n for n in q.GN] + [args.figures_dir / n for n in q.GF]
partial = args.report.with_name(args.report.name + '.partial')
assert all(p.is_file() for p in published)
assert args.report.is_dir()
assert partial.read_bytes() == b'inert report\n'
after = {str(p.relative_to(q.REPO)): q.digest(p) for p in q.EXPECTED}
assert after == q.BEFORE
record = dict(
    layout='report = output_dir',
    selected_report=str(args.report),
    nested_summary=str(args.output_dir / 'summary.json'),
    initial_guard='accepted',
    whole_entry='reached first _json; stopped without ingestion or directory creation',
    repeated_guard='accepted',
    writer_consequence=error,
    already_published={str(p): q.digest(p) for p in published},
    retained_partial={str(partial): q.digest(partial)},
    source_test_helper_hashes_unchanged=after == q.BEFORE,
)
with (q.PRIVATE / 'overlap-result.json').open('x') as handle:
    json.dump(record, handle, indent=2)
    handle.write('\n')
print(json.dumps(record, indent=2))
