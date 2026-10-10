"""Reproduce the code overlay from frozen study sources and maintained snapshot.

Run from any directory with Python 3.10+. Only the assigned study archive and
its generated draft_code namespace are written; live code/docs are not edited.
Numerical source algorithms are preserved. Adaptations are explicit below.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
from pathlib import Path
import re
import tarfile

STUDY = Path(__file__).resolve().parent
ROOT = STUDY.parents[1]
SCRATCH = ROOT / 'data/generated/book_promotion_20261010/draft_code'
INPUT_SHA256 = {'promotion_base.tar.gz': '9c3351f4eee0e79d8d11bd80960445ef521d530e083d65bf42d13aa59195e3fc', 'compression_core.py': '92195e851ac8d0a314ddebe88b962c78f84c5f0f1280b8021b385a8d69b7c480', 'dictionary_core.py': 'c7b1c377185641a9e9c99047bada7e22d3f673b2b061dfeee4179db371474a87', 'data_core.py': '6bed73460f7be1ab730264747694f9b91c4cec23f79dc5f9075676d359a6c2c8', 'visual_core.py': '7441de806852517447657f949ab251c20a64a8d6228976db7ea21abacd83adde', 'radial_explorer.py': '6b5ffe5b89100f6523466623d7dad0e03f4cf538c1614dae7eb12cfcc7333644', 'radial_explorer.html': '390499a83fcaba395614cebf31dc2935b072aa0b9cfbd7cdd5832fe8fc08296c', 'test_compression_core.py': '9c549ff53268478204fa3e2edf2d895cc8ab3c7aa398e2d10e6ee78586e6db6c', 'test_dictionary_core.py': 'e8ee898b7559387d4b57f885494f069e239513a243beb7bf95e7bea98e2672ba', 'test_data_core.py': '6882b61d6ade2f640158c2afc1e62ebe5da52d4d75967b4d2478e24b9da6e3a8', 'test_visual_core.py': 'd8424ff35a94e66e3d3e7bd780ef91555a80d2d8e167aa46b06a69396af3045f', 'test_radial_data.py': '04ad397385c2d4ee2c91534efdd34f234ece41839b98981855df818b015de93a', 'test_radial_viewer.py': '10e605e929c34d94e8196c06cdc7d0136467e2d49bef3f8a7becc92169f6f090', 'support_example.py': '8741b09e06d96568b7d4ad577c6e02fbb1eb3136e8f966f8acad75558b112bdb', 'radial_example.py': 'fd86dfb304fe80e5ce53679e001017b3eead3666bf2a3a557829cd617edebe87', 'CODE.md': '98565299d08cd2c0ee2230d84d1b7511bd3f1b9fce96e2dcba4ba68c3d7351c0', 'DICTIONARIES.md': '9032e3843e29637767cdbc09f3f7373bd1a125751d9b4fa9608156759a9e0cea', 'DATA.md': '719158fa71b5e4036c236c1488570e4484fe04c06ae8cd7f772bcec310832e98', 'VISUALS.md': '3a8b9a299d57520b9116cfa86dedad519cc50312956298d90a01ff8f74b3c862', 'RADIAL.md': '415404cfeb52d2c4ff09d747333eed8f04a048a034e6937a528d5508cc445da6'}

MODULES = {
    'compression_core.py': 'compression.py',
    'dictionary_core.py': 'observable_dictionaries.py',
    'data_core.py': 'compression_data.py',
    'visual_core.py': 'prediction_views.py',
    'radial_explorer.py': 'radial_explorer.py',
    'radial_explorer.html': 'radial_explorer.html',
}
TESTS = {
    'test_compression_core.py': 'test_compression.py',
    'test_dictionary_core.py': 'test_observable_dictionaries.py',
    'test_data_core.py': 'test_compression_data.py',
    'test_visual_core.py': 'test_prediction_views.py',
    'test_radial_data.py': 'test_radial_data.py',
    'test_radial_viewer.py': 'test_radial_viewer.py',
}
EXAMPLES = {'support_example.py': 'example_compression.py',
            'radial_example.py': 'example_radial_explorer.py'}
GUIDES = {'CODE.md': 'COMPRESSION.md', 'DICTIONARIES.md': 'OBSERVABLE_DICTIONARIES.md',
          'DATA.md': 'COMPRESSION_DATA.md', 'VISUALS.md': 'PREDICTION_VIEWS.md',
          'RADIAL.md': 'RADIAL_EXPLORER.md'}


def replace_imports(s):
    for old, new in MODULES.items():
        if not old.endswith('.py'):
            continue
        a, b = old[:-3], new[:-3]
        s = re.sub(r'(?m)^(\s*)from '+a+r' import ', r'\1from pde.'+b+' import ', s)
        s = re.sub(r'(?m)^(\s*)import '+a+r' as ', r'\1from pde import '+b+' as ', s)
    return s


def neutral_names(s):
    for old, new in {**MODULES, **TESTS, **EXAMPLES, **GUIDES}.items():
        s = re.sub(r'(?<![A-Za-z0-9_])' + re.escape(old), new, s)
    return s


def source_module(name):
    s = neutral_names((STUDY/name).read_text())
    if name == 'compression_core.py':
        s = s.replace('see COMPRESSION.md.', 'see code/COMPRESSION.md.')
        s = s.replace('No paper driver, experiment archive, filesystem writes or global settings are\nused at runtime. Harmonic/Taylor numerical source setup is NOT the compact\npaper\'s certified initialization-only continuation compiler.',
                      'No experiment archive, filesystem writes or global settings are used at\nruntime. Harmonic/Taylor numerical source setup is NOT a certified global\ninitialization-only continuation compiler.')
        s = s.replace('compact-paper', 'complete-trajectory').replace('compact paper', 'complete-trajectory theory')
        s = s.replace('zero readout (paper)', 'zero readout (compression convention)')
        s = s.replace("The appendix's sparsity-nine", 'Sparsity-nine')
    elif name == 'dictionary_core.py':
        s = s.replace('Study-owned extraction of the 2026-09-20 scaling dictionary, with CPU support\nand the maintained p=2,p=4 word definitions added (no historical results for\nthose orders). Requires PYTHONPATH=code and Torch. No import from an old study.',
                      'Optional Torch adapter over the maintained word compiler and closure engine.\nSupports dictionary orders 1 through 9, including even orders; see\ncode/OBSERVABLE_DICTIONARIES.md. Requires PYTHONPATH=code and Torch.')
        s = s.replace("the scaling campaign's fixed legacy/appended draw", 'fixed prefix/appended draw')
        s = s.replace('HISTORICAL_ORDERS = (1, 3, 5, 6, 7, 8, 9)\n', '')
    elif name == 'data_core.py':
        start = s.index('PAPER_SOURCE = {')
        end = s.index('\n\n\n@dataclass', start)
        s = s[:start]+s[end:]
        s = s.replace("source_implementation=dict(PAPER_SOURCE, scopes=list(PAPER_SOURCE['scopes'])),",
                      "source_implementation=dict(path='code/pde/compression_data.py',\n                                                 sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),")
        s = s.replace('paper-compatible ', '').replace('paper data-seed contract', 'data-seed contract')
        s = s.replace('Unscaled paper target', 'Unscaled toy target').replace('Paper toy recipe', 'Toy recipe')
        s = s.replace('see COMPRESSION_DATA.md.', 'see code/COMPRESSION_DATA.md.')
    elif name == 'visual_core.py':
        s = s.replace('See PREDICTION_VIEWS.md.', 'See code/PREDICTION_VIEWS.md.')
    elif name == 'radial_explorer.py':
        s = s.replace('Adapt assembled-core arrays', 'Adapt normalized model arrays')
        s = s.replace('Pass data_core.Dataset arrays directly.', 'Pass compression_data.Dataset arrays directly.')
    return s


SCRATCH_HELPER = '''

def _test_scratch():
    import os
    root = Path(os.environ.get('PDE_OPTIONAL_TEST_SCRATCH',
                               Path(__file__).resolve().parents[2] / 'data/established/optional_tests'))
    root.mkdir(parents=True, exist_ok=True)
    return root

'''

ORACLE_TEST = '''
    def test_dense_matches_maintained_numpy_equations(self):
        from pde import ARCTAN, TANH, Parameters, flow_velocity, forward

        # Transfer actual tensors: equal seeds across NumPy/Torch do not couple draws.
        for activation, numpy_activation in (('tanh', TANH), ('atan', ARCTAN)):
            for depth in (1, 2, 3):
                model = c.Dense(7, 2, depth, activation, seed=12, readout='small_gaussian')
                state = model.initial_state
                theta = Parameters(tuple(v.numpy() for v in [state[0], *state[2:]]), state[1].numpy())
                physical_columns = np.sqrt(2) * self.inputs.numpy().T
                oracle = flow_velocity(theta, physical_columns, self.labels.numpy(), numpy_activation)
                actual = model.rhs(state, self.inputs, self.labels)
                np.testing.assert_allclose(model.predict(state, self.inputs).numpy(),
                    forward(theta, physical_columns, numpy_activation).output, atol=2e-14, rtol=2e-13)
                for observed, expected in zip(actual, [oracle.weights[0], oracle.readout, *oracle.weights[1:]]):
                    np.testing.assert_allclose(observed.numpy(), expected, atol=2e-14, rtol=2e-13)

'''


def source_test(name):
    s = replace_imports((STUDY/name).read_text())
    if name == 'test_compression_core.py':
        s = s.replace("if __name__ == '__main__':", ORACLE_TEST+"\nif __name__ == '__main__':")
    if name in ('test_visual_core.py', 'test_radial_viewer.py'):
        s = s.replace('with tempfile.TemporaryDirectory() as directory:',
                      'with tempfile.TemporaryDirectory(dir=_test_scratch()) as directory:')
        at = s.index('\n\nclass ')
        s = s[:at]+SCRATCH_HELPER+s[at:]
    if name == 'test_radial_data.py':
        s = re.sub(r'SCRATCH = .*radial_support"',
                   SCRATCH_HELPER + "\nSCRATCH = _test_scratch()", s)
    return s


def source_example(name):
    s = replace_imports((STUDY/name).read_text())
    s = s.replace('Path(__file__).with_name(name)', "Path(__file__).resolve().parents[1] / 'pde' / name")
    s = s.replace('Path(__file__).with_name(n)', "Path(__file__).resolve().parents[1] / 'pde' / n")
    s = neutral_names(s)
    if name == 'radial_example.py':
        s = s.replace('import json', 'import json\nimport platform\nimport numpy as np')
        s = s.replace("manifest = dict(purpose=", "manifest = dict(environment=dict(python=platform.python_version(), numpy=np.__version__, torch=torch.__version__, device='cpu', numerical_threads=1), purpose=")
    return s


def commands():
    return '''Run from the standalone edition or repository root with Python 3.10+,
NumPy and PyTorch. Static plotting additionally requires Matplotlib; Node is
optional for the executable JavaScript checks. Choose fresh output directories.
TorchVision is needed only for explicit MNIST loading.

```sh
mkdir -p data/established
optional_test_scratch=$(mktemp -d "$PWD/data/established/optional_tests.XXXXXX")
export PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
export PDE_OPTIONAL_TEST_SCRATCH="$optional_test_scratch" TMPDIR="$optional_test_scratch" MPLCONFIGDIR="$optional_test_scratch/matplotlib"
python -B -m unittest discover -s code/tests -p 'test_compression*.py' -v
python -B -m unittest discover -s code/tests -p 'test_observable_dictionaries.py' -v
python -B -m unittest discover -s code/tests -p 'test_prediction_views.py' -v
python -B -m unittest discover -s code/tests -p 'test_radial*.py' -v
python -B code/scripts/example_compression.py --out data/established/compression_example
python -B code/scripts/example_radial_explorer.py --out data/established/radial_example
```

These bounded CPU checks and examples make no fitted-endpoint, dense-fidelity,
GPU, speed, convergence-rate or theorem-certification claim. They require no
retained arrays or downloads. Keep the generated manifests and local dependency
versions for replay. Examples refuse existing output directories.
'''


def source_guide(name):
    s = (STUDY/name).read_text()
    if name == 'CODE.md':
        start = s.index('**The selected-model numerical setup')
        s = '# Optional numerical trajectory compression\n\n' + s[start:]
        s = s[:s.index('Run from the repository root without installing packages:')]
        s += ('The tests use independent autograd and maintained NumPy finite-network\n'
              'oracles, moment quadrature/transport, source-jet derivatives, metric\n'
              'identities and explicit continuation checks. Finite arithmetic can\n'
              'overflow or saturate; no automatic precision or stability guarantee\n'
              'is supplied. See the [data guide](COMPRESSION_DATA.md),\n'
              '[prediction views](PREDICTION_VIEWS.md) and\n'
              '[radial explorer](RADIAL_EXPLORER.md).\n\n## Bounded reproduction\n\n'+commands())
        s = s.replace('For dense state `[W1,w,W2,...,WL]`,',
                      'The stored readout `w` is $W^{(L+1)}$ in the book. For dense state\n`[W1,w,W2,...,WL]`,')
        s = s.replace("the paper driver's sparsity-nine BSS barrier selector", 'a sparsity-nine BSS barrier selector')
        s = s.replace("The driver's low-budget spectral-floor branch\nis deliberately outside this core's exact-Gram contract.",
                      'There is no spectral-floor fallback in this exact-Gram contract.')
        s = s.replace("the compact paper", 'the complete-trajectory theorem').replace("compact paper", 'complete-trajectory theory')
        s = s.replace("the\npaper's", "the\ntheorem's")
        s = s.replace("broadens the old driver's\ntwo-layer tanh Legendre/Harmonic setup by using the compact equations directly", 'uses the same direct equations throughout')
        s = s.replace("This direct\nstate omits the driver's lifted features and lifted residual norm, so it\ndoes not reproduce that solver's finite-step lift drift.",
                      'This direct state stores moments themselves, without auxiliary lifted\nfeatures or a separately integrated residual norm.')
    elif name == 'DICTIONARIES.md':
        s = s[s.index('## Model, order and retained state'):s.index('## Historical evidence, with later qualifications retained')]
        s = '# Initialized observable dictionaries on finite carriers\n\n' + s
        s = s.replace('| Historical scaling orders |', '|').replace('|:---:|', '|')
        s = re.sub(r' \| (yes|no) \|', ' |', s)
        start = s.index('The original width-512 campaign')
        end = s.index('Observable raw spans', start)
        s = s[:start]+s[end:]
        s = re.sub(r'The historical\nwidth-2048 discovery lower ranks were .*?numerical ranks\.',
                   'Different finite carriers can have different numerical ranks.', s, flags=re.S)
        s = s.replace("The scaling campaign's frozen draw protocol is preserved:", 'The frozen random draw protocol is:')
        s = s.replace('the $p=2,4$ cells are executable additions, with no historical result implied.', 'all even and odd orders use the same maintained word definition.')
        s = s.replace('`dictionary_core.py` imports maintained `pde` modules only.', '`pde.observable_dictionaries` reuses maintained `pde` modules and optional Torch.')
        s = s.replace('This small operational example was checked at both orders two and three.\n', '')
        s = s.replace('historical within-step convention', 'within-step chord convention')
        s = s.replace('It does not reproduce the\nold adaptive integration controller.', 'It uses a fixed Heun step size.')
        s = s.replace('## Relation to maintained closures and the compact paper', '## Relation to population closures and selected-coordinate compression')
        s = s.replace("The compact paper's", 'The complete-trajectory').replace("the compact paper's", 'the complete-trajectory theorem\'s')
        s = s.replace('the paper\'s source-approximation', 'that theorem\'s source-approximation')
        s = s.replace('The compact paper also starts', 'The selected-coordinate construction starts')
        s = s.replace('the historical\nfinite comparison retained', 'this finite comparison retains')
        s += ('\nThe [general first-order guide](GENERAL_P1.md) specifies engine ownership,\n'
              'arithmetic, integration and restart contracts. Its comparison section\n'
              'documents `pde.closure_comparison`: saved-loss matching, parameter-chord\n'
              'stopping here, and display interpolation are different operations.\n'
              'The adapter retains its four basic endpoint metrics for convenience;\n'
              'they use ordinary float64 squares and supply no extreme-range promise.\n'
              'Diagnostic condition numbers are finite-carrier measurements.\n\n'
              'Deterministic tests cover all retained words against a NumPy interpreter,\n'
              'ridge orientation, seeded prefixes, gradient blocks, complete-basis\n'
              'dense equivalence, weighted population initialization and endpoint\n'
              'status. Run the commands in [the compression guide](COMPRESSION.md).\n')
    elif name == 'DATA.md':
        s = s[:s.index('## Sources and checks')]
        s = s.replace("a small NumPy module for the paper's circle/sphere target and", 'a NumPy module for circle/sphere targets and')
        s = s.replace("'data/generated/book_promotion_20261010/data_support/mnist_cache'", "'data/established/mnist_cache'")
        s = s.replace('No data were downloaded for this assembly.', 'The deterministic tests use synthetic fixtures and request no downloads.')
        s += ('## Deterministic checks\n\nRun the commands in [the compression guide](COMPRESSION.md). Tests use\n'
              'independent target formulas, pinned fixture IDs, pixel-normalization\n'
              'oracles, official-split loader mocks, train-only scaling and seeded\n'
              'replay. They do not validate downloaded MNIST files or dataset quality.\n')
    elif name == 'VISUALS.md':
        s = s[:s.index('## Source scope and provenance')]
        s = s.replace('This is study-owned support, not promoted plotting infrastructure.', '')
        s = s.replace('study-owned output location', 'explicit output location')
        s = s.replace("The study's [support_example.py](support_example.py)", '[example_compression.py](scripts/example_compression.py)')
        s = s.replace('No paper figure driver is imported.', 'All inputs are generated by the maintained example.')
        block_start = s.index('```bash')
        block_end = s.index('```', block_start+3)+3
        s = s[:block_start]+'''```sh
PYTHONPATH=code OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python -B code/scripts/example_compression.py --out data/established/compression_example
```'''+s[block_end:]
        s += ('## Checks and limits\n\nThe tests check signed geometry, fixed scales, complementary hemispheres,\n'
              'safe embedded JSON and the actual viewer control logic in Node with a\n'
              'DOM/canvas stand-in. Node absence produces an explicit skip. This is\n'
              'not a browser-layout or screenshot comparison. The small viewer has no\n'
              'external resource dependency. See [reproduction commands](COMPRESSION.md).\n')
    elif name == 'RADIAL.md':
        start = s.index('## Data and export')
        s = ('# Offline radial experiment explorer\n\n'
             '`pde.radial_explorer` validates supplied data and embeds them in the\n'
             'adjacent `pde/radial_explorer.html` template. **Distribute both files.**\n'
             'D3 7.9.0 is inlined with its attribution. Generated HTML works locally\n'
             'without a server or network request. The interface supplies experiment,\n'
             'width and seed selectors, playback, model toggles and hover/pinned values.\n'
             'Use [prediction views](PREDICTION_VIEWS.md) for static plots and sphere previews.\n\n')+s[start:]
        s = s.replace('The adapter accepts\nall 15 cases and 124 model records in the original payload; that was a schema\ncompatibility check, not scientific validation of its results.', '')
        s = s.replace('python studies/book_promotion_20261010/radial_explorer.py run-a.json run-b.json --out data/generated/book_promotion_20261010/explorer.html',
                      'PYTHONPATH=code python -B -m pde.radial_explorer run-a.json run-b.json --out data/established/explorer.html')
        s = s[:s.index('## Reproduce the small example and checks')]+('## Reproduce the small example and checks\n\n'
             'Run the commands in [the compression guide](COMPRESSION.md). The\n'
             '[radial example](scripts/example_radial_explorer.py) creates two toy\n'
             'experiments with three/four training inputs, 96 queries and three saved\n'
             'times through 0.04. Only Dense width 64, seed 17 shares initialization\n'
             'with its compression models; other variants exercise selectors. It\n'
             'writes case JSON, populated/empty HTML and source/output hash manifests\n'
             'into a fresh directory. It is an operational example, not a fitting\n'
             'or approximation experiment.\n\n'
             'Schema tests check arrays, weighted losses, endpoints, IDs and safe\n'
             'export. The Node test executes the actual bundled D3 and application\n'
             'with a DOM/SVG stand-in; it checks controls, alignment and finite SVG\n'
             'paths. It does not assess browser layout or pixels.\n')
    s = replace_imports(s)
    s = neutral_names(s)
    s = s.replace('PYTHONPATH=code:studies/book_promotion_20261010', 'PYTHONPATH=code')
    s = s.replace('`compression.py`', '`pde.compression`').replace('`compression_data.py`', '`pde.compression_data`')
    s = s.replace('`prediction_views.py`', '`pde.prediction_views`')
    s = s.replace('data_core.toy_data', 'pde.compression_data.toy_data')
    s = s.replace("Compact paper's direct physical-time", 'Direct physical-time')
    if name == 'CODE.md':
        s = s.replace('Legendre state is', 'Let $q$ be the positive integer memory order. Legendre state is')
        s = s.replace('velocities vanish, $\\dot w=2H_Ly/m$,', 'velocities vanish. With $H_L=[h_1^{(L)},\\ldots,h_m^{(L)}]$,\n$\\dot w=2H_Ly/m$,')
    return s


def build():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--edition', type=Path, default=SCRATCH/'edition')
    args = parser.parse_args()
    for name, expected in INPUT_SHA256.items():
        if hashlib.sha256((STUDY/name).read_bytes()).hexdigest() != expected:
            raise ValueError('Frozen input changed: '+name)
    edition = args.edition.resolve()
    if not edition.is_relative_to(SCRATCH.resolve()):
        parser.error('--edition must stay in the assigned draft_code scratch namespace')
    edition.mkdir(parents=True, exist_ok=True)
    with tarfile.open(STUDY/'promotion_base.tar.gz') as base:
        for member in base.getmembers():
            if member.isfile() and member.name.split('/')[0] in ('code', 'docs'):
                destination = edition/member.name
                if not destination.resolve().is_relative_to(edition):
                    raise ValueError('Unsafe base member')
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(base.extractfile(member).read())
    overlay = {}
    for source, target in MODULES.items():
        overlay['code/pde/'+target] = source_module(source)
    for source, target in TESTS.items():
        overlay['code/tests/'+target] = source_test(source)
    for source, target in EXAMPLES.items():
        overlay['code/scripts/'+target] = source_example(source)
    for source, target in GUIDES.items():
        overlay['code/'+target] = source_guide(source)
    readme = (edition/'code/README.md').read_text()
    at = readme.index('## Model and normalization')
    entry = '''## Optional compression, datasets and prediction views

Explicitly import `pde.compression` for the Torch Dense, Legendre and
selected-coordinate models; `pde.observable_dictionaries` adapts initialized
finite carriers to the existing closure engine. Their numerical source builders
are **not a certified global initialization-only compiler**. See the complete
[compression contract and commands](COMPRESSION.md) and
[dictionary contract](OBSERVABLE_DICTIONARIES.md).

[Datasets](COMPRESSION_DATA.md), [array prediction views](PREDICTION_VIEWS.md)
and the [offline radial explorer](RADIAL_EXPLORER.md) are separate NumPy-only
modules. Static plots opt into Matplotlib; explicit MNIST loading opts into
TorchVision. Ordinary `import pde` remains NumPy-only.

'''
    overlay['code/README.md'] = readme[:at]+entry+readme[at:]
    checker = (edition/'code/tools/check_library.py').read_text()
    overlay['code/tools/check_library.py'] = checker.replace('"psutil", "torch"}', '"psutil", "torch", "matplotlib", "torchvision"}')
    for name, s in overlay.items():
        path = edition/name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(s, encoding='utf-8')
    archive = STUDY/'promotion_code.tar.gz'
    with archive.open('wb') as raw, gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=0) as packed:
        with tarfile.open(fileobj=packed, mode='w') as tar:
            for name, text in sorted(overlay.items()):
                data = text.encode('utf-8')
                info = tarfile.TarInfo(name)
                info.size, info.mode, info.mtime = len(data), 0o644, 0
                tar.addfile(info, io.BytesIO(data))
    print(f'{archive}: {len(overlay)} files; sha256 {hashlib.sha256(archive.read_bytes()).hexdigest()}')
    print(edition)


if __name__ == '__main__':
    build()
