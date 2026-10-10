# Bounded mathematical check

Checked the complete `RESULT.md` and its final local corrections. Final
SHA-256: `b103e063d4c62e5d4d00867f733d4edb294811dd16bbdb9f45bb0959c4cbc804`.
The only additional scientific input was the setup of `paper/compact.tex`,
for the normalization, activation assumptions, population Gram and label cap.
No route notes, study history, other studies, experiments or inherited paper
theorems were audited. Canonical-notation and rigorous-math instructions
were applied.

**Outcome: the assigned claims pass within their stated scope.** No claimed
unconditional sample-uniform all-time theorem depends on an unproved bound;
the general all-time and width-uniform extensions remain explicit conditions
or open obligations.

- **Repeated data and finite time.** Frequency weighting preserves the loss
  and gradient exactly. Dividing the first-layer weights and readout by
  `sqrt(n)` converts the stated mobilities into Euclidean gradient flow.
  Its energy identity and Cauchy–Schwarz give path length at most
  `M sqrt(T)`. The resulting compact parameter ball, bounded labels and
  compact input sphere yield finite force and prediction derivative bounds
  at fixed width and initialization. Positive representative weights preserve
  the same energy bound. Subtracting the two ODEs gives
  `D'(t) <= A_T D(t) + B_T h`, with `D(0)=0`, and hence the displayed
  Gronwall and whole-sphere prediction estimates. The zero-`A_T` convention
  is correct. These constants are independent of the data count under the
  stated fixed parameters, but need not be controlled as width or time grows.

- **Latent packing and mean labels.** Partitioning `[0,1]^k` into cells of
  side at most `h/(2A sqrt(k))` gives the stated upper bound. Greedy observed
  representatives are pairwise farther apart than `h`, so a cell contains
  at most one. Latent coordinates are unnecessary for the algorithm. For
  a cluster representative `v_j` with mean label, its force discrepancy is
  the average of
  `-2[(f grad(f))(v)-(f grad(f))(v_j)]`
  plus `2y[grad(f)(v)-grad(f)(v_j)]`; its norm is therefore at most
  `2(U_T + M V_T)h`. No label regularity is needed for this refinement.

- **Finite moments and exact dictionaries.** Linear dependence of more
  than `R` evaluation columns, together with the constant coordinate,
  gives the stated nonnegative weight elimination and at most `R` atoms.
  Uniform force approximation error `eta` contributes at most `2 eta`
  after moment matching. The sphere-polynomial dimension and its fixed-
  dimension growth are correct; the assertion remains conditional on a
  uniform approximation of the force family, not labels alone. For the
  global finite-output-dictionary identity, the loss gradient depends only
  on `G` and `b`; the omitted label-square moment is parameter independent.
  The stated statistic and atom counts suffice. Global `C^2` coefficients
  give local uniqueness, and the nonnegative-loss energy bound excludes
  finite-time escape, so equality of the flows holds for all times.

- **Gap and conditional extensions.** Unit inputs give a common initial
  Gram diagonal. Bounded activation derivatives imply at most linear growth,
  so the Gaussian second-moment recursion keeps each subsequent common
  diagonal bounded by an activation/depth constant. Thus
  `gamma <= trace(Q)/m <= C`, and `gamma/m <= C/m`; the cited sufficient
  label cap cannot allow fixed positive `Y` as `m` grows. The residual
  leakage identity has the correct `-2/m` factor. Adding the two assumed
  prediction tails to the finite-time error proves the conditional
  all-time statement. Adding and subtracting both anchor predictions proves
  the Taylor spatial-net inequality in normalized input distance. Neither
  argument supplies its own uniform tail, Lipschitz or coverage assumptions.

Three small clarifications were checked in the final candidate: the
continuous sphere-curve observation now distinguishes `d=1` from `d>=2`;
the constant latent generator `A=0` is handled separately; and the exact
dictionary identity now holds for every parameter state. The last condition
justifies differentiating the loss identity; membership in a dictionary
only along an original training path would not suffice.

This is an internal check of the listed arguments, not a promotion review
or validation of the inherited three-method theorem.
