# `paper_MFP` standalone bundle check

Date: 2026-10-11. This is a mechanical execution and copy-integrity check only;
it does not assess mathematical claims.

## Result

All requested checks passed.

- With the working directory `paper_MFP/`, `PYTHONPATH=code`, and `python -B`,
  `pde.__file__` resolved to
  `/home/amir/Codes/PDE/paper_MFP/code/pde/__init__.py` (exit status 0).
- All 13 copied Python files and `requirements.txt` byte-compare with their
  maintained counterparts. The pre-execution and post-execution SHA-256 values
  agree in every pair; the complete before/import hash record and the complete
  post-execution record are retained below.
- `python -B -m unittest discover -s code/tests -p 'test_mfp_*.py' -v`, with
  the requested environment variables, passed: 72 tests in 19.408 seconds,
  exit status 0.
- `code/MFP_CALCULUS.md` contains exactly five fenced `python` blocks. They
  were extracted unchanged and each was run once in its own fresh Python
  process; all five exited 0.
- All three example scripts exited 0. The kernel-jets command used
  `--activation all` and a fresh output leaf within the assigned scratch
  directory; it produced three activation cases.

## Copied-source hashes

The following SHA-256 was identical for maintained source and bundle copy,
both before execution and after all executions:

| Relative path | SHA-256 |
| --- | --- |
| `pde/__init__.py` | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `pde/finite_network.py` | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `pde/gaussian_moments.py` | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `pde/mfp_expr.py` | `1340df2e1cd7279d568aa07610bfba033eaf95d8fc75426d8149b2b4d9cbcfa8` |
| `pde/mfp_compiler.py` | `19e862cf6863b28fc2949be3c9fa2a60ab13f985e2d4c7bb97928423127f12b6` |
| `pde/mfp_finite.py` | `84060153c467172eaabaed073ece4e8fd0d77fbc1ed2fee3e8a66542d2c7c037` |
| `scripts/example_mfp_calculus.py` | `20b727df8e386907f1ae17de427b3f41ff86b4f29f33a0cea9711bbc7a679d07` |
| `scripts/example_mfp_mlp_derivative.py` | `9c7fefb3ac2dcc50c90f1bef45cf64bf4f7f37d0c0b1b5e26c8c30a4478d4527` |
| `scripts/example_mfp_kernel_jets.py` | `3298421fad2776bf306b0928611517b938529429de7606efd53ecf1caaa2d03c` |
| `tests/test_mfp_expr.py` | `06dac966c1b74ba8dfe9ebfb9a2dde1abccc175102aef435cf8ba110c1824d65` |
| `tests/test_mfp_compiler.py` | `4b0f6b38cc0f9d35d82cfc38a5a95aafd91053d80ace4bed451b4589451995de` |
| `tests/test_mfp_mlp_example.py` | `e3dfffb2e8bb28b128903d92df84567225b81e7957f04d166dfc755972d15ad5` |
| `tests/test_mfp_kernel_jets.py` | `a2fd1f7f64bfdf7dde921991f15f84992d30859f662dd71cd33e0996e156e3ce` |
| `requirements.txt` | `c907c176d0ef35a2a05a8650accb80616d99d55f620dc0fd55d8bfe994bc7ae2` |

## Retained evidence

All logs, the five exact extracted Markdown blocks, and the fresh kernel-jets
output directory are in
`data/generated/mfp_gaussian_master_proof_20261010/paper_bundle_check_20261011/`:

- `import_and_hashes.log`: standalone import and pre-execution source/bundle hashes.
- `post_execution_hashes.log`: post-execution byte comparisons and hashes.
- `unittest.log`: verbose test run and exit status.
- `mfp_calculus_blocks.log`: fence count, each block's compact output, and exits.
- `examples.log` plus one log per example: compact outputs and exits.
- `kernel_jets_all/`: fresh output from the all-activation kernel-jets example.
