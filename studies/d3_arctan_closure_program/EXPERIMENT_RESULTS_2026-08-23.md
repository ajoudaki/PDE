# Preregistered middle-response experiment: results

**Run date:** 23 August 2026.  **Claim level:** empirical route evidence only.
The frozen design and interpretation rule are in
`EXPERIMENT_PREREGISTRATION_2026-08-23.md`; the complete machine-readable
aggregation is `experiment_summary_2026-08-23.json`.

## Verdict under the frozen rule

The experiment is numerically valid.  It is **inconclusive**, rather than a
formal pass or evidence against the cavity route.

- All main-trajectory instances of conditions 1, 2, 3, and 5 passed at
  horizons 0.5, 1, and 2.
- Condition 4 passed at horizon 0.5.  At horizons 1 and 2, the central
  log--log slopes of both same-column response statistics remained below
  0.10, but four upper 95% clustered-bootstrap endpoints exceeded 0.10.
  Consequently the precommitted all-pass decision failed.
- This is only one failed condition family, and none of its lower 95%
  endpoints exceeded 0.15 at both horizons.  The precommitted criterion for
  evidence *against* the route therefore did not trigger.

## Quantitative signatures

For the full query (R_2), every smallest-to-largest width ratio of the
median compact-time (|R_2|_{p,n}/p), (p=2,4,6,8), lay between 0.989 and
1.035.  All corresponding upper 95% bootstrap slopes were at most 0.029.
The median condensation ratio fell from about 0.258 at width 128 to about
0.081 at width 2048.

The cavity state perturbation obeyed the predicted scale:

\[
 \sup_{s\le S}\|B_3(s)-B_3^{(-j)}(s)\|_{2,n}
 \asymp n^{-1/2}.
\]

Its fitted slopes were approximately -0.477, -0.487, and -0.477 at horizons
0.5, 1, and 2; multiplying by \(\sqrt n\) produced nearly flat central
slopes 0.023, 0.013, and 0.023.  The same-column contraction

\[
 \Delta_j=c_j^{\mathsf T}(B_3-B_3^{(-j)})
\]

remained order one, as a signed quadratic-response calculation predicts.
For \(|\Delta_j|\), the central slopes were -0.302, -0.151, and -0.026;
for the relative response they were -0.245, -0.070, and 0.039.  The wide
clustered intervals at the last two horizons, not a positive central growth
estimate, caused the formal failures.

The raw tangent-block median ratios were all between 0.949 and 1.087.  The
step-halving audit had 1,104 main and 240 cavity paired comparisons with no
solver failures.  Its maximum symmetric relative discrepancies were
\(1.92\times10^{-9}\) and \(7.84\times10^{-9}\), and the largest
\(f'=K\) integration defects were \(2.18\times10^{-6}\) and
\(1.74\times10^{-6}\).

## Evidentiary consequence

These runs reject neither adaptive focusing nor the cavity proof route in
the mathematical sense.  They do localize the useful proof target: the
normalized state response has the expected \(n^{-1/2}\) scale, whereas the
same-column Gaussian contraction retains an order-one signed quadratic
term.  A proof must control that signed term; an argument that simply treats
the cavity state difference as negligible is quantitatively false.

