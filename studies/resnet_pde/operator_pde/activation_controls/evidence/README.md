# Archived compact evidence

`processed/` contains the deterministic summary, metrics, and figure tables
produced from the completed sealed run.

`seals/` contains copies of the authoritative frozen-input, PDE-stage, and
dense-stage manifests. Their file maps bind the omitted raw trajectory
archives by SHA-256. These copies are provenance records only; the runner
does not read them from this location.

The compact release omits raw PDE and dense `.npz` files so that the active
`results/` directory is absent on first use. Run

```bash
python run_experiment.py all
```

from the release root to regenerate and seal the complete result tree under
the frozen protocol.
