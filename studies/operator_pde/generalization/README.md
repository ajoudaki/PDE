# Fixed-\(P=5\) neural-PDE generalization study

This project tests whether the previously validated width-independent
operator–Liouville PDE was accidentally tuned to one dataset.

The closure is fixed before every comparison:

- ambient dimension \(d=3\);
- complete degree-one Hermite basis
  \(\{1,B_1,B_2,B_3,a/A\}\), hence \(P=5\);
- \(N=16\) depth nodes;
- order-three tensor Gauss–Hermite base cubature (\(M=81\));
- \(R=128\) scrambled-Sobol row cubature;
- RK4 with \(dt=0.02\);
- \(\sigma_w=0.65,\ A=\gamma=1\).

The same \(P=5\) is used for \(m=2,3,4,5\). Sample count does not determine
the basis size; the fixed immutable neuron-label dimension does.

## What is varied

`protocol/cases.json` declares 14 cases:

- the original baseline;
- four label changes, including an exact boundary perturbation, different
  label directions at fixed norm, and doubled amplitude;
- two input geometries, including pairwise correlation \(0.85\);
- \(m=2,4,5\) in the same three-dimensional input space;
- normalized erf,
  \(\operatorname{erf}(\sqrt{\pi}z/2)\), and normalized arctangent,
  \((2/\pi)\arctan(\pi z/2)\), whose ranges and derivatives at zero
  match tanh;
- correlation-by-label and sample-count-by-activation interactions.

The exact compute tiers, seeds, numerical audits, plateau rules, bootstrap
construction, equivalence margin, and interpretation boundaries are frozen
in:

- `protocol/generalization_protocol.json`
- `protocol/analysis_plan.json`

Only the baseline and the small `Y1` perturbation are direct tests of the
current narrow residual-tanh conjecture. The other cases test a proposed
extension; their success would not prove \(P\to\infty\) convergence or the
ordered dense limit.

## Integrity gates

The PDE source imports no dense-reference code or trajectory. Every PDE run
is completed and sealed before dense references may start.

Each archive records:

- an immutable case hash;
- the exact \(X,y\), activation, and physical parameters;
- quadrature-array and compiler hashes for PDE runs;
- deterministic scientific-configuration hashes excluding runtime;
- restart-source content hashes;
- the sealed PDE evidence hash inside every dense-reference archive.

The comparison layer rejects a mismatch in case, activation, parameters,
time grid, or evidence seal.

## Reproduce

Create an environment from `requirements-lock.txt`, then run:

```bash
PYTHONPATH=src python protocol/reproduce_generalization.py
```

This executes tests, all PDE curves and numerical audits, the PDE-only
quadrature decision, exact stage sealing, dense screening and held-out
references, trajectory bootstrap analysis, figures, and final verification.

The full run creates large raw `.npz` arrays under
`results/generalization/`. A compact source release may omit those arrays;
the same command regenerates them.

Useful checks:

```bash
PYTHONPATH=src python verify_study.py source
PYTHONPATH=src python verify_study.py evidence
```

The second command requires regenerated raw evidence and processed outputs.

## Scientific decision rule

The primary statistic is the uniform-in-time, uniform-in-depth Frobenius
error of hidden-Gram increments, normalized by the larger PDE/reference
feature motion. Output-increment and loss-curve errors are co-primary.

Strong transfer requires a one-sided simultaneous 95% upper confidence bound
at most 5% for all active primary metrics, plus numerical-resolution and
two-window plateau gates. The bootstrap is simultaneous across all 14 cases
and all three metrics. Wide uncertainty is reported as unresolved, never as a
pass.
