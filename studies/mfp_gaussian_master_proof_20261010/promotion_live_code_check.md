# Live code integration check (v1)

**Result: PASS.** This is a mechanical live-check only.  The approved v7
manifest matched all 116 paths before execution and again after all execution;
there were no source, requirements, or generated-output hash mismatches.

All commands ran from `/home/amir/Codes/PDE` with
`PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH=code`, `OPENBLAS_NUM_THREADS=1`,
`OMP_NUM_THREADS=1`, and `MKL_NUM_THREADS=1` where Python code was executed.
The command forms are listed below; the `script` logs retain output and
`COMMAND_EXIT_CODE="0"`.

| Check | Actual result | Retained evidence |
| --- | --- | --- |
| Approved manifest, before execution | 116/116 SHA-256 matches | `data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/pre_manifest_hashes.log` |
| MFP tests | 72 tests passed | `data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/tests.log` |
| Library boundary | 104 files checked | `data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/check_library.log` |
| Python fences in `code/MFP_CALCULUS.md` | Exactly 5 blocks; all exit 0 (guarded by an explicit `len(blocks) == 5` assertion) | `data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/fences_v3/results.json`, `fences_v3.log` |
| Fresh all-activation producer | Exit 0; 3 cases written | `data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/producer.log` |
| Six producer text/JSON outputs | 6/6 hashes equal the permitted v4 producer manifest | `data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/producer_comparison.log`, `producer_output_sha256.log` |
| Approved manifest, after all execution | 116/116 SHA-256 matches | `data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/final_manifest_hashes.log` |

Commands (all exit 0):

```sh
python -B studies/mfp_gaussian_master_proof_20261010/promotion_live_code_check__hash_manifest.py data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v7/candidate_manifest.json
env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=code OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -B -m unittest discover -s code/tests -p "test_mfp_*.py" -v
env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=code OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -B code/tools/check_library.py
env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=code OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -B studies/mfp_gaussian_master_proof_20261010/promotion_live_code_check__run_fences.py code/MFP_CALCULUS.md --output-dir data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/fences_v3
env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=code OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -B code/scripts/example_mfp_kernel_jets.py --activation all --output-dir data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/producer
python -B studies/mfp_gaussian_master_proof_20261010/promotion_live_code_check__hash_manifest.py data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v7/candidate_manifest.json
```

The exact six-file comparison command is retained in
`data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/command_ledger.md`;
its output is `producer_comparison.log` (6/6 matches) and
`producer_output_sha256.log` (the six observed hashes).

The first fence-run (`code_check/fences/`, retained with its log) was invalid:
the checker regex matched a literal `\\n`, executed zero blocks, and therefore
did not satisfy the required check.  I corrected only the owned helper, then
observed five passing blocks in `fences_v2/`.  The final `fences_v3/` run adds
an explicit five-block assertion and again passes all five.  This was a harness
defect, not a candidate or live-source mismatch.

No maintained source, candidate, Git index, or root README was edited by this
check.  The helper sources are
`promotion_live_code_check__run_fences.py` and
`promotion_live_code_check__hash_manifest.py` in this study folder.
