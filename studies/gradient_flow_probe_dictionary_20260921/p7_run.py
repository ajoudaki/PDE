"""Bounded p7-only continuation of the frozen eleven-case suite producer."""
import json
import sys
from pathlib import Path
import torch
import suite_run as suite
from new_dictionary_p7 import build, raw_features
from new_dictionary_p45 import raw_features as old_raw

METHODS = ('new_p7',)
original_hashes = suite.hashes


def hashes():
    result = original_hashes()
    for name in ('P7_PROTOCOL.md', 'P7_DICTIONARY_SPEC.md', 'P7_DERIVATION.md',
                 'P7_GAUSSIAN_CONTRACTIONS.md'):
        path = suite.HERE/name
        result[str(path.relative_to(suite.ROOT))] = suite.sha(path)
    return result


def construct(initial, method):
    assert method == 'new_p7'
    return build(initial, 7, block_size=256)


@torch.no_grad()
def preflight(initial, manifest, directory, device):
    engine, state, metadata = construct(initial, 'new_p7')
    assert (engine.K1, engine.K2) == (26, 46)
    assert torch.equal(state.w, initial.w) and torch.equal(state.c, initial.c)
    projection_error = float((state.M-engine.b2.T@(initial.M@engine.b1)/2048).abs().max())
    assert projection_error <= 1e-12
    left, right, _ = raw_features(initial, 7)
    previous_left, previous_right, _ = old_raw(initial, 5)
    assert torch.equal(left[:, :14], previous_left)
    assert torch.equal(right[:, :24], previous_right)
    for side in ('lower', 'upper'):
        assert metadata[side]['ridge_condition'] <= 1e10
        assert metadata[side]['triangular_relative_residual'] <= 1e-8
    checks = {'new_p7': metadata, 'projection_max_error': projection_error,
              'p5_raw_prefix_bitwise_equal': True}
    # Same complete initialization check as the frozen suite preflight.
    for name in manifest['cases']:
        for level in ('primary', 'refined'):
            path = manifest['archive_cells'][name+'_full'][level]['arrays_path']
            other = suite.inherited.read_initial(path, device)
            deltas = {key: float((getattr(initial,key)-getattr(other,key)).abs().max())
                      for key in ('w','c','M')}
            assert max(deltas.values()) == 0
            checks[name+'_'+level] = deltas
    suite.save_json(directory/'validation.json', dict(passed=True, checks=checks,
                                                     source_hashes=hashes()))


if __name__ == '__main__':
    if '--budget' not in sys.argv:
        sys.argv.extend(['--budget','225'])
    budget = float(sys.argv[sys.argv.index('--budget')+1])
    ceiling = 50 if '--preflight' in sys.argv else 225
    if not 0 < budget <= ceiling:
        raise ValueError('p7 invocation exceeds its frozen reservation ceiling')
    # Reuse the unchanged archive trajectory function and suite scheduler.
    suite.METHODS = METHODS
    suite.hashes = hashes
    suite.construct = construct
    suite.preflight = preflight
    suite.main()
