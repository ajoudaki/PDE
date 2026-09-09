# Reproducing the fixed-\(P=5\) generalization study

## Current migration status

Source and frozen protocols are in this study tree. Retained products and
seals are read-only under repository
`data/historical/studies/resnet_generalization/`. Fresh products belong under
`data/generated/resnet_generalization/`, not the source or historical tree.
The historical compact release omitted 101 raw NPZ archives (about 1.35 GB);
that release description is not a current evidence-inventory guarantee.

The current source hashes no longer match the old freeze. Both reproduction
drivers retain source-hash gates and cannot currently complete; the post-freeze
driver verifies source first, whereas the original driver runs tests before
the grid's source check. The post-freeze compatibility
wrappers retain their original source-hash gates. Reproduction is therefore
blocked under the current historical authorization, not silently repaired by
migration. Do not waive a gate, refresh an expected hash, or generate a new
seal as a workaround. The interfaces below remain useful for an independently
authorized future replay; none authorizes one now.

The historical environment used Python 3.12 and pinned dependencies:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-lock.txt
```

The captured platform and package versions in `environment.json` describe
23 July 2026, not the current runtime, a hermetic container, or a promise of
byte-identical BLAS behavior across machines.

The retained post-freeze orchestration command (currently hash-blocked) is:

```bash
PYTHONPATH=src python protocol/reproduce_generalization_postfreeze.py
```

After its source gate, the driver is designed to run:

1. the study's unit and integrity tests;
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

The historical amendments addressed two execution-only issues after
trajectories had completed:

- a legacy `dict.get` default eagerly referenced a redundant `seed_start`
  alias even though the authoritative `seed_blocks` schedule existed;
- the analyzer expected redundant `m`, `d`, and `seed_ids` JSON fields even
  though they were already fixed by the case registry, observable shapes,
  stored exact seed array, schedule, and scientific-configuration hash.

The wrappers were designed to add only those aliases in memory, register a dynamically loaded
module for Python 3.12 dataclass resolution, and then invoke the unchanged
frozen sealer/analyzer after checking its hash. They do not modify trajectories, metrics, bootstrap
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
```

For generated evidence (not an implicit historical replay):

```bash
PYTHONPATH=src python verify_study.py evidence
```

The last command verifies all frozen source hashes, PDE/dense archive
inventories and content hashes, processed tables, figures, bootstrap count,
and then reruns the study tests. `--skip-tests` skips only tests, never source
or evidence checks. Current hash failures remain expected limitations.
