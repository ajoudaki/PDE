# Label scale, stability and fitting

2026-10-07. New theoretical investigation requested by the user: determine
whether the small-label hypothesis is essential for the Gaussian deep-network
compression program, or is a limitation of the existing stability argument.

This study does not change the integrated theorem, the maintained book, or
the optimizer. Its proofs use the canonical finite network from
`docs/notation.qmd`, with exactly zero initial readout as stipulated by the
user. No unpromoted approximation theorem is assumed. The separate read-only
diagnosis of the user's integrated results is not a theorem dependency here.

## Contract

Fixed sphere training data, independent Gaussian first weights of variance
one and hidden weights of variance `1/n`, hidden depth at least two, analytic
activations with bounded strip derivatives and possibly unbounded values,
zero initial readout, mean squared loss, and block mobilities
`(n,1,...,1,n)`. The central open target is arbitrary fixed label scale with
the original all-time, whole-sphere high-probability comparison and storage
scope, for **multiple inputs (`m>=2`)**. The user has already established
arbitrary-label one-sample compression; that case is a baseline, not the
unresolved target. Changing the optimizer, using specially selected initial parameters,
or making labels grow with width does not answer that target.

Only theoretical analysis and bounded proof checking are performed. No
simulation, empirical search, promotion or Git commit is authorized or done.

## Current results

Complete derivations are in [LABEL_SCALE.md](LABEL_SCALE.md).

- Every finite-width gradient-flow trajectory exists for all finite times,
  for every finite label vector. This excludes finite-time parameter blowup,
  not escape as time tends to infinity.
- The known one-sample fitting mechanism is reconstructed only to identify
  its multi-input obstruction: its readout bound has rank one, and the
  corresponding matrix derivative need not be positive semidefinite.
- Label rescaling changes hidden/readout relative mobility by the square
  of the label multiplier. It is not a removal of the hypothesis for the
  unchanged dynamics.
- Initial feature learning improves the label-weighted feature norm, but
  need not improve every direction in sample space. An explicit nonlinear
  two-input example has negative initial curvature of its smallest feature-
  Gram eigenvalue with probability tending to one at Gaussian initialization.
  This disproves a monotone initial-gap invariant, not fitting or compression.
- Instantaneous variational expansion already occurs at zero-readout
  initialization for nonzero labels in nonlinear tanh networks that satisfy
  the preceding fitting theorem. It is not evidence of failed learning.
- A two-sample, two-layer analytic network with positive initial population
  feature-Gram gap has non-fitting local minima. They exist at every positive
  label scale. Their reachability from Gaussian initialization with
  nonvanishing probability at arbitrarily large width is not established.
- General-dataset arbitrary-label fitting and unchanged compression remain
  open. No incompressibility lower bound is proved.

## Routes and check status

| Route | Result | Remaining obstruction |
|---|---|---|
| Energy and readout geometry | Global finite-width existence; exact multi-input rank-one identity | Multi-sample residual can be orthogonal to the current prediction |
| Matrix-gap invariant | Typical-Gaussian initial gap decrease in an analytic nonlinear example | A decreasing gap need not vanish; fitting and compression remain unresolved |
| Bad-basin construction | Exact nonglobal local minimum | Gaussian basin probability at fixed labels as width grows |
| Variational instability | Exact initial expansive direction | Expansion does not establish failure or storage lower bounds |

The lead assembled the proof with prompt-scoped mathematical agents;
a separate agent diagnosed the existing integrated proof read-only. Original
route messages used inconsistent half-loss factors in places; the persisted
proof uses the stipulated mean squared loss throughout. A fresh isolated
scoped reconstruction checked all seven sections and passed the final
candidate, after one missing plus sign was corrected. Its exact scope and
checked hash are in [CHECK.md](CHECK.md). Status: internally checked partial
results, not an established or promoted removal of the small-label assumption.

Source scope: user-specified canonical model; maintained `docs/index.qmd` and
`docs/notation.qmd`; required research/proof/notation instructions. No other
study's scientific results were imported into these proofs.

Next decisive obligation: prove persistent coercivity in the actual
multi-sample residual direction, or construct a fixed-label Gaussian-basin
counterexample. Either outcome would still need a separate bridge to the
claimed all-time compression complexity.
