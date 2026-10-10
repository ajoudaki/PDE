# Optional-code candidate assembly notes

## Current correction status

The original assembly record below describes packet v1. The current overlay
includes the coordinator's numerical-admissibility correction: scale-relative
Gram rank validation and a reconstructed-training-identity check, without
regularization. Regression cases include duplicate, antipodal, zero and nearly
duplicate features, and an accepted small well-conditioned Gram. The original
sources and adverse reviews remain recoverable from the immutable v1 packet.
Current exact sources are frozen in `promotion_packet_v2.tar.gz`; the current
overlay SHA256 is
`1e4fd4d35961a0bf7c8831ae3fc9305b83f5826726cf3080c06b5cd0cda26ef7`.
The corrected compression/data suites passed 29 tests in standalone edition v5;
see `data/generated/book_promotion_20261010/promotion_validation_v3/`.
Original assembly identities in `core_sources.json` remain historical;
`promotion_review_inputs_v2.json` records the current proposed maintained files.

## Initial assembly record

Date: 2026-10-10. Assembler: Codex subagent `/root/draft_code_package`.
This is a complete proposed code overlay, not an independent review or promotion approval.
No live maintained file or Git index was changed. Source algorithms were preserved; no numerical correction was made.

## Artifacts and reproduction

`promotion_code.tar.gz` contains 21 regular files rooted at `code/`.
Apply it over the frozen `promotion_base.tar.gz` edition, not over another study.
`promotion_code_build.py` reproduces the overlay from the 20 frozen inputs below.
It checks every input hash before writing, uses deterministic tar/gzip metadata,
and writes only its candidate archive and generated `draft_code` namespace.
Its default standalone scratch includes frozen `code/` and `docs/`; the latter
is extracted only so the structural library-link checker can resolve targets.

```sh
python -B studies/book_promotion_20261010/promotion_code_build.py
```

Archive SHA256: `18c282178dc10e3ca7afa9968b413ded46779549a6b589b4efb97c6dec42c3ad`.
Builder SHA256: `a382091f83d323a4a52a4947b3aab019889321dc224035bc6bf6e1c9a858c107`.

## Source mapping and adjustments

| Frozen study source | Candidate destination |
|---|---|
| `compression_core.py` | `code/pde/compression.py` |
| `dictionary_core.py` | `code/pde/observable_dictionaries.py` |
| `data_core.py` | `code/pde/compression_data.py` |
| `visual_core.py` | `code/pde/prediction_views.py` |
| `radial_explorer.py` | `code/pde/radial_explorer.py` |
| `radial_explorer.html` | `code/pde/radial_explorer.html` |
| `test_compression_core.py` | `code/tests/test_compression.py` |
| `test_dictionary_core.py` | `code/tests/test_observable_dictionaries.py` |
| `test_data_core.py` | `code/tests/test_compression_data.py` |
| `test_visual_core.py` | `code/tests/test_prediction_views.py` |
| `test_radial_data.py` | `code/tests/test_radial_data.py` |
| `test_radial_viewer.py` | `code/tests/test_radial_viewer.py` |
| `support_example.py` | `code/scripts/example_compression.py` |
| `radial_example.py` | `code/scripts/example_radial_explorer.py` |
| `CODE.md` | `code/COMPRESSION.md` |
| `DICTIONARIES.md` | `code/OBSERVABLE_DICTIONARIES.md` |
| `DATA.md` | `code/COMPRESSION_DATA.md` |
| `VISUALS.md` | `code/PREDICTION_VIEWS.md` |
| `RADIAL.md` | `code/RADIAL_EXPLORER.md` |

- Imports now resolve only through `pde`; tests/examples no longer import study modules.
- `compression_data` provenance now hashes the actual packaged module and records its maintained path. It no longer claims a paper file is the running implementation. Dataset recipes and array hashes are unchanged.
- Example source receipts use the sibling `code/pde` modules and adjacent HTML template; the radial example also records Python/NumPy/Torch/device/thread metadata.
- Temporary outputs use `data/established/` inside the standalone edition, with `PDE_OPTIONAL_TEST_SCRATCH` overrides. Examples require explicit fresh output directories.
- The compression tests add an independent established NumPy finite-network comparison for tanh/atan, depths 1–3 and transferred actual states; equal seeds across libraries are not treated as coupling.
- The dictionary adapter reuses `observable_initialization.build_dictionary` and `observable_torch_p1.ClosureEngine`; no solver implementation is copied. Its unused historical-order constant is omitted. Order support remains 1 through 9.
- New guides remove source-paper/study dependencies, historical numerical findings and historical PASS claims while retaining complete numerical scope. They explicitly distinguish source builders from the certified initialization-only compiler, normalized rows from physical columns, zero from small random readout, and sampled comparisons from continuum guarantees.
- `code/README.md` gains one compact entry section linking all five complete guides. Existing maintained content is preserved.
- `code/tools/check_library.py` gains only `matplotlib` and `torchvision` in its declared external-import allowlist.
- `pde/__init__.py` is unchanged. Torch and TorchVision remain opt-in; Matplotlib loads only for plotting. The radial HTML remains adjacent to its Python module and preserves its bundled D3 attribution.

## Actual source reading and dependencies

Complete reading: assigned core modules, six tests, two examples, five component guides;
the radial template except its one minified third-party D3 line; the promotion
selection; AGENTS, workflow Part 2, canonical-notation skill and neural reference;
current notation, finite-network contract/API portions of `code/README.md`,
full `code/GENERAL_P1.md` and `code/tools/check_library.py`.
Current `docs/index.qmd` scientific-objective opening was read for notation context.
No other study or source-paper implementation was read. Maintained import declarations
were inspected recursively to close runtime dependencies; their complete bodies are
inputs for the paired reviewers, not claimed as a fresh scientific audit here.

The complete maintained implementation dependency closure for imports, tests and
runnable guide examples is:

```text
code/pde/__init__.py
code/pde/finite_network.py
code/pde/finite_torch.py
code/pde/gaussian_moments.py
code/pde/observable_arithmetic.py
code/pde/observable_compiler.py
code/pde/observable_fixed.py
code/pde/observable_initialization.py
code/pde/observable_p1_initialization.py
code/pde/observable_solver.py
code/pde/observable_torch_p1.py
code/pde/observable_words.py
```

Also supply the comparison guide dependency `code/pde/closure_comparison.py`,
full `code/GENERAL_P1.md`, overlaid `code/README.md`, the current notation contract
and complete book model dependencies in the paired scientific packet. The native
circle solver appears only in a guide example; the compression runtime itself
uses NumPy/Torch and no maintained solver. These paths must come from the frozen
base snapshot. External operational dependencies are Python 3.10+, NumPy, optional
Torch, optional Matplotlib, optional TorchVision for MNIST, and optional Node for
the executable JavaScript checks. No download was requested.

## Standalone checks

Working directory: `/home/amir/Codes/PDE/data/generated/book_promotion_20261010/draft_code/edition`.
Python: `/home/amir/miniconda3/bin/python`.
Only candidate `code/` was on `PYTHONPATH`; no study import path was supplied.
All command stdout/stderr and exact invocation/environment records are in
`data/generated/book_promotion_20261010/draft_code/validation02/`.
The temporary Python runner is in the same scratch namespace; it is not a
maintained dependency. The earlier validation01 records are preserved.

| Check | Outcome | Wall seconds |
|---|---|---:|
| `boundary` | exit 0 | 0.683 |
| `test_compressionall` | exit 0 | 2.348 |
| `test_observable_dictionaries` | exit 0 | 2.441 |
| `test_prediction_views` | exit 0 | 0.718 |
| `test_radialall` | exit 0 | 0.291 |
| `example_compression` | exit 0 | 3.632 |
| `example_radial` | exit 0 | 1.678 |
| `numpy_only_imports` | exit 0 | 0.105 |
| `COMPRESSION_block1` | exit 0 | 1.560 |
| `OBSERVABLE_DICTIONARIES_block1` | exit 0 | 1.479 |
| `OBSERVABLE_DICTIONARIES_block2` | exit 0 | 1.585 |
| `OBSERVABLE_DICTIONARIES_block3` | exit 0 | 0.112 |
| `COMPRESSION_DATA_block1` | exit 0 | 1.561 |

The deterministic suite contains 52 passing tests: 16 compression, 11 data,
8 dictionary, 7 plotting/simple viewer and 10 radial schema/viewer tests.
The two Node checks ran (not skipped). The structural boundary check passes.
Both bounded examples and every runnable non-download Python guide block pass.
The NumPy-only import check installs an import finder that rejects Torch,
TorchVision and Matplotlib before importing `pde` and all three data/view modules.
The real MNIST cache snippet was not run; its loader behavior is checked by
synthetic fixtures/mocks. API-signature snippets and snippets requiring supplied
arrays are exercised by their full example producers rather than executed with
undefined placeholder variables.

Exact main test/example commands (environment below applies to all):

```sh
export PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
export MPLCONFIGDIR="$PWD/data/established/matplotlib"
export PDE_OPTIONAL_TEST_SCRATCH="$PWD/data/established/optional_tests" TMPDIR="$PWD/data/established/optional_tests"
mkdir -p "$PDE_OPTIONAL_TEST_SCRATCH"
python -B code/tools/check_library.py
python -B -m unittest discover -s code/tests -p 'test_compression*.py' -v
python -B -m unittest discover -s code/tests -p 'test_observable_dictionaries.py' -v
python -B -m unittest discover -s code/tests -p 'test_prediction_views.py' -v
python -B -m unittest discover -s code/tests -p 'test_radial*.py' -v
python -B code/scripts/example_compression.py --out data/established/compression_example02
python -B code/scripts/example_radial_explorer.py --out data/established/radial_example02
```

The actual interpreter above was `/home/amir/miniconda3/bin/python`; the
portable guide uses `python` from an environment containing the required packages.
Fresh output directories are required when repeating these commands.

No training campaign, historical empirical reproduction, fitted-limit test,
CUDA check, timing comparison, certified source compiler or browser pixel/layout
review was performed. The tests establish finite software behavior only.
Observed maintained Torch TF32 deprecation warnings do not change arithmetic policy.

## Frozen author inputs

| Input | SHA256 |
|---|---|
| `promotion_base.tar.gz` | `9c3351f4eee0e79d8d11bd80960445ef521d530e083d65bf42d13aa59195e3fc` |
| `compression_core.py` | `770ceab1dc5917eb14759071002d824ae45feaabfc85be1e7f228945d3cdb3a6` |
| `dictionary_core.py` | `c7b1c377185641a9e9c99047bada7e22d3f673b2b061dfeee4179db371474a87` |
| `data_core.py` | `6bed73460f7be1ab730264747694f9b91c4cec23f79dc5f9075676d359a6c2c8` |
| `visual_core.py` | `7441de806852517447657f949ab251c20a64a8d6228976db7ea21abacd83adde` |
| `radial_explorer.py` | `6b5ffe5b89100f6523466623d7dad0e03f4cf538c1614dae7eb12cfcc7333644` |
| `radial_explorer.html` | `390499a83fcaba395614cebf31dc2935b072aa0b9cfbd7cdd5832fe8fc08296c` |
| `test_compression_core.py` | `9c365aede9d1f7bd60530c0e912a4a51a290680ca3cfc4121bfa4ff50781f716` |
| `test_dictionary_core.py` | `e8ee898b7559387d4b57f885494f069e239513a243beb7bf95e7bea98e2672ba` |
| `test_data_core.py` | `6882b61d6ade2f640158c2afc1e62ebe5da52d4d75967b4d2478e24b9da6e3a8` |
| `test_visual_core.py` | `d8424ff35a94e66e3d3e7bd780ef91555a80d2d8e167aa46b06a69396af3045f` |
| `test_radial_data.py` | `04ad397385c2d4ee2c91534efdd34f234ece41839b98981855df818b015de93a` |
| `test_radial_viewer.py` | `10e605e929c34d94e8196c06cdc7d0136467e2d49bef3f8a7becc92169f6f090` |
| `support_example.py` | `8741b09e06d96568b7d4ad577c6e02fbb1eb3136e8f966f8acad75558b112bdb` |
| `radial_example.py` | `fd86dfb304fe80e5ce53679e001017b3eead3666bf2a3a557829cd617edebe87` |
| `CODE.md` | `2eda3877e23da26f9ebd305582149fd8f777dd1c78568cde3ab706d5f7c2eeae` |
| `DICTIONARIES.md` | `9032e3843e29637767cdbc09f3f7373bd1a125751d9b4fa9608156759a9e0cea` |
| `DATA.md` | `719158fa71b5e4036c236c1488570e4484fe04c06ae8cd7f772bcec310832e98` |
| `VISUALS.md` | `3a8b9a299d57520b9116cfa86dedad519cc50312956298d90a01ff8f74b3c862` |
| `RADIAL.md` | `415404cfeb52d2c4ff09d747333eed8f04a048a034e6937a528d5508cc445da6` |

## Proposed file receipts

| Candidate path | SHA256 |
|---|---|
| `code/COMPRESSION.md` | `43280504b77f738b6ea30a3de9e1ef4cc57f51a985833d030eafe42f44a375e6` |
| `code/COMPRESSION_DATA.md` | `189c0a7ffd62364d47d3670f9667f9f83af0ff7fb09c9ff1c3d4c0a2c400f346` |
| `code/OBSERVABLE_DICTIONARIES.md` | `807e679baa162ea151e419fef58e0bb570fb253a7e54307f27c9cc61c861ad87` |
| `code/PREDICTION_VIEWS.md` | `ea1cce40fcc7d253309351e0e2a0e0c9b9fe1ab4ac79f3fbf36c59dbc31979d5` |
| `code/RADIAL_EXPLORER.md` | `c15d04bad246ab801ded97674fdb205cd7f38423ef1890855ad5732d53873f18` |
| `code/README.md` | `01f833c1c541f43d9a4a6d1a82d9fc67b71cd4a4ace29583d12a78bfb0464f12` |
| `code/pde/compression.py` | `47b0045f128b3ef36431e3311514632724fc5c6208a4466c017094e3685968d3` |
| `code/pde/compression_data.py` | `12b8e9c351d368660f8655587e05e828fee4608e369c5ce128c982c19f5557d6` |
| `code/pde/observable_dictionaries.py` | `4ac8d595f8250e8e2e90cb12e9ad83c61dfb50210057f07060b2a551fe05d5b3` |
| `code/pde/prediction_views.py` | `9f1fa503ed0f4a60e63c0cdda80ea33b9b443be8993c722e52b32ed0a6af2e5f` |
| `code/pde/radial_explorer.html` | `390499a83fcaba395614cebf31dc2935b072aa0b9cfbd7cdd5832fe8fc08296c` |
| `code/pde/radial_explorer.py` | `61412b5c2202a1ed45f49c56ce2092da5234c2fd231119f3bc796833fc903506` |
| `code/scripts/example_compression.py` | `90df9f20cef5fb0964b8b09ee7a1970695fbeeb98ba2641adbd316eef8279435` |
| `code/scripts/example_radial_explorer.py` | `706636fcd3868dc2b6f4f19efce073d31fdf17433df8ba917b3222c865d9f525` |
| `code/tests/test_compression.py` | `99c23de2fa009f7af0469166305229f7afa99a589e1dcc4ca420e27ca4ebf95c` |
| `code/tests/test_compression_data.py` | `24115018f7f1231bc2b1bdcb8ccb8096bf067e75d0b0837008006cc00bda11d7` |
| `code/tests/test_observable_dictionaries.py` | `149b3d8be11fed0689b1d8e0389d6e3ab057924b750952277bfdafdfbceb8457` |
| `code/tests/test_prediction_views.py` | `4d808ba2bb1a8e832685d09f6a843987eb969044bbe4eac08962d5f6ddead4f7` |
| `code/tests/test_radial_data.py` | `4db24ee6165e6d00144fb0a77664052a0f60d951e0bf002090171962a8e6db58` |
| `code/tests/test_radial_viewer.py` | `a37a4e2ab0e301bd8069146e1e9c2e2cce53e1c3c81e37168e6dadad85702c0a` |
| `code/tools/check_library.py` | `c47052910683fff26a448f854a55a5f1378346836b9a8c03cccadc373d794054` |
