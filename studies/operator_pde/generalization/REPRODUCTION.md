# Reproducing the fixed-\(P=5\) generalization study

## Compact release versus regenerated evidence

The compact release contains all scientific source, frozen protocols, tests,
processed tables, evidence seals, and the three key figures. It deliberately
omits the 101 raw NPZ archives, which occupy about 1.35 GB.

Install Python 3.12 and the pinned dependencies:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-lock.txt
```

The captured platform and package versions are in `environment.json`. This is
a source-level reproducibility environment, not a hermetic container or a
promise of byte-identical BLAS behavior across machines.

Run the full frozen experiment and verify every regenerated archive:

```bash
PYTHONPATH=src python protocol/reproduce_generalization_postfreeze.py
```

The defaults run:

1. all 50 unit and integrity tests;
2. 28 primary PDE segments, 14 independent scrambles, seven method/depth/time
   audits, and six preregistered \(R=256\) diagnostics;
3. 46 exact dense-network ensemble blocks;
4. the 2,000-replicate block-stratified simultaneous bootstrap;
5. complete source, archive-seal, processed-output, and figure verification.

Parallelism can be reduced for a small machine:

```bash
PYTHONPATH=src python protocol/reproduce_generalization_postfreeze.py \
  --parallel-pde 1 --parallel-dense 1 --dense-workers 1
```

## Why the post-freeze orchestrator exists

The frozen scientific source is not edited. Two execution-only issues were
found after trajectories had completed:

- a legacy `dict.get` default eagerly referenced a redundant `seed_start`
  alias even though the authoritative `seed_blocks` schedule existed;
- the analyzer expected redundant `m`, `d`, and `seed_ids` JSON fields even
  though they were already fixed by the case registry, observable shapes,
  stored exact seed array, schedule, and scientific-configuration hash.

The wrappers add only those aliases in memory, register a dynamically loaded
module for Python 3.12 dataclass resolution, and then invoke the unchanged
frozen sealer/analyzer. They do not modify trajectories, metrics, bootstrap
draws, thresholds, case selection, or reference tiers. Their exact scope and
hashes are recorded in:

- `protocol/POSTFREEZE_EXECUTION_AMENDMENT.json`
- `protocol/POSTFREEZE_ANALYSIS_AMENDMENT.json`

The reproduction driver routes dense sealing through
`protocol/seal_dense_verified.py`, which first checks that the historical
execution wrapper still has the hash declared by its amendment record.

## Fast checks

Before regenerating evidence:

```bash
PYTHONPATH=src python verify_study.py source
python ../verify_release.py
```

After the full run:

```bash
PYTHONPATH=src python verify_study.py evidence
```

The last command verifies all frozen source hashes, PDE/dense archive
inventories and content hashes, processed tables, figures, bootstrap count,
and then reruns the 50 tests.
