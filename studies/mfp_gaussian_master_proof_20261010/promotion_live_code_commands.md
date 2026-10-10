# Command ledger

All commands used `/home/amir/Codes/PDE` as working directory.  All entries
exited with code 0; the named session log retains its output and exit marker.

```sh
python -B studies/mfp_gaussian_master_proof_20261010/promotion_live_code_check__hash_manifest.py data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v7/candidate_manifest.json
```

Logs: `pre_manifest_hashes.log`, `post_manifest_hashes.log`,
`post_fences_manifest_hashes.log`, and `final_manifest_hashes.log`.

```sh
env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=code OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -B -m unittest discover -s code/tests -p "test_mfp_*.py" -v
env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=code OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -B code/tools/check_library.py
env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=code OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -B studies/mfp_gaussian_master_proof_20261010/promotion_live_code_check__run_fences.py code/MFP_CALCULUS.md --output-dir data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/fences_v3
env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=code OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -B code/scripts/example_mfp_kernel_jets.py --activation all --output-dir data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/producer
```

Logs: `tests.log`, `check_library.log`, `fences_v3.log`, and `producer.log`.

```sh
python -B -c "import hashlib,json,pathlib; prior=json.load(open(\"data/generated/mfp_gaussian_master_proof_20261010/promotion_candidate_v4/edition/data/established/mfp_kernel_jets_01/manifest.json\"))[\"output_sha256\"]; current=json.load(open(\"data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/producer/manifest.json\"))[\"output_sha256\"]; rows=[{\"name\":k,\"approved\":prior[k],\"live\":current.get(k),\"match\":prior[k]==current.get(k)} for k in sorted(prior)]; print(json.dumps({\"files\":len(rows),\"matched\":sum(r[\"match\"] for r in rows),\"mismatches\":[r for r in rows if not r[\"match\"]]},indent=2)); raise SystemExit(0 if all(r[\"match\"] for r in rows) else 1)"
sha256sum data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/producer/identity.txt data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/producer/identity.json data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/producer/quadratic.txt data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/producer/quadratic.json data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/producer/symbolic.txt data/generated/mfp_gaussian_master_proof_20261010/promotion_live_integration_v1/code_check/producer/symbolic.json
```

Logs: `producer_comparison.log` and `producer_output_sha256.log`.

The retained invalid `fences/` run was produced before the runner's regex and
block-count guard were corrected.  The passing intermediate `fences_v2/` run
is retained; `fences_v3/` is the final guarded evidence.
