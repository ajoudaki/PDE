"""Final finite interface acceptance cases, with no science or report builds."""
from contextlib import ExitStack, redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
from unittest import mock
import numpy as np
from bounded import BASE, OUT
from acceptance import module, note, rows, StopWork

post = module('mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/postprocess_h3_sine_regression.py')
retained = BASE / 'data/historical/studies/mfp_gaussian_calculus/depth_order5_scalar/multi_observable/audit/H3_NORMALIZED_SINE_RESULT.json'
before = hashlib.sha256(retained.read_bytes()).hexdigest()
with tempfile.TemporaryDirectory() as tmp:
    root = Path(tmp)
    raw = root / 'selected-raw.npz'
    names = ('layer2_gamma04', 'layer2_q4', 'layer3_gamma04', 'layer3_q4')
    values = np.tile(np.array([-1., 0., 1.])[None, :, None], (3, 1, 4))
    np.savez(raw, widths=np.array([16, 32, 64]), names=names, values=values)
    output = root / 'fresh'
    output.mkdir()
    (output / retained.name).symlink_to(retained)
    predictions = {'layers': {2: {'Gamma04': 0., 'Q4': 0.}, 3: {'Gamma04': 0., 'Q4': 0.}}}
    with mock.patch.object(post, 'EXPECTED_RAW_SHA256', hashlib.sha256(raw.read_bytes()).hexdigest()), \
         mock.patch.object(post, 'compile_numeric', return_value=predictions), \
         mock.patch.object(post, 'normalized_sine_moment', return_value=None), \
         mock.patch.object(Path, 'write_text', autospec=True, side_effect=StopWork('before final output write')) as writer:
        try:
            post.run(raw, output)
        except StopWork:
            pass
    target = writer.call_args.args[0]
    assert target.resolve() == retained
    note('Actual Gaussian writer accepts retained-file alias', chosen_output=output,
         attempted_child=target, resolves_to=target.resolve(), retained_sha256=before,
         retained_unchanged=before == hashlib.sha256(retained.read_bytes()).hexdigest(),
         limit='Tiny 3x3x4 fixture and existing affine fit only; prediction and fixture hash patched; write_text tripwire prevents all target writes; no real frozen hash reset')

# Consumer dispatch: only the selected file is read, math is stopped immediately.
for relative, entry, stop_name in (
    ('mfp_gaussian_calculus/order5/independent/compare_primary.py', 'main', '_read_map'),
    ('mfp_gaussian_calculus/order5/independent/nonpolynomial_prediction.py', 'main', 'evaluate'),
):
    m = module(relative)
    for flags in ([], ['--historical']):
        with mock.patch.object(sys, 'argv', [relative] + flags), \
             mock.patch.object(m, stop_name, side_effect=StopWork('before map evaluation')) as stop:
            try:
                getattr(m, entry)()
            except StopWork:
                pass
        note('Gaussian common consumer selection', consumer=relative, flags=flags, selected_arguments=stop.call_args.args,
             limit='Actual parser and main; stopped at first map reader/evaluator, no quadrature or compilation')

# A report missing an old source-local run result is not an archive refusal.
builder = module('mfp_gaussian_calculus/depth_order5/primary/build_self_contained_report.py')
missing = [str(path) for path in builder.AUDIT_PATHS if not path.exists()]
note('Unguarded report callable current preconditions', missing_source_local_inputs=missing,
     limit='Existence checks only; current build is obstructed by missing run inputs, but lacks its callable archive guard')

# Fixed source formulas remain in source while selected run data changes roots.
audit = module('mfp_gaussian_calculus/depth_order5_scalar/primary/audit_full_scalar_recurrence.py')
with mock.patch.object(Path, 'read_text', autospec=True, side_effect=StopWork('before control data read')) as read:
    try:
        audit.companion_controls(audit.selected_input_root(historical_inputs=True), historical_inputs=True)
    except StopWork:
        pass
assert read.call_args.args[0] == audit.ROOT / 'order5/compiler/MANIFEST.json'
note('Gaussian fixed source control role', first_payload=read.call_args.args[0], limit='Stopped before JSON read; source path binding only')

# Quadratic maintained mathematical payload and import are source-only.
quadratic = module('mfp_quadratic_l2_order5/quadratic_exact.py')
target = Path(quadratic.assemble_moving_recurrence.__code__.co_filename)
assert target == BASE / 'studies/mfp_gaussian_calculus/depth_order5_scalar/primary/moving_scalar_extension.py'
note('Quadratic shared source import', target=target, limit='Import and code-object inspection only; no recurrence calls')

(OUT / 'final-probes.json').write_text(json.dumps(rows, indent=2, default=str) + '\n')
