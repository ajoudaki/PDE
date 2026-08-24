# Preregistered discriminating experiment: middle-adjoint response

**Frozen before execution:** 23 August 2026.

This experiment is evidence about the first open bridge C-13 in
`CORE_EVIDENCE_LEDGER_2026-08-23.md`.  It cannot prove C-13 and will not be
used to promote any theorem claim.  Its purpose is to discriminate between a
cutoff-uniform cavity/response strategy and adaptive coordinate focusing.

## 1. Exact object and competing mechanisms

Run the exact finite feature-time flow (unit feature-ascent vector field)

\[
 A'=X_3,\quad r'=Q_1,\quad
 G_1'=B_2\otimes_n X_1,\quad G_2'=B_3\otimes_n X_2
\]

from the canonical iid Gaussian initialization.  No field is clipped.  The
primary field is

\[
 R_2(s)=G_2(s)^*B_3(s)
       =\Gamma_2^*B_3(s)+P_2(s)^*B_3(s).
\]

The learned term is reported separately.  The unresolved term is the static
query \(R_2^{\rm stat}=\Gamma_2^*B_3\).

The response/delocalization mechanism predicts compact-horizon exponential
tails, hence moment growth \(\|R_2\|_{p,n}=O(p)\), and no increasing
single-column self-influence.  The competing focusing mechanism predicts a
width-growing high-moment or cavity-response signature even though the
normalized \(L^2\) energy remains bounded.

## 2. Exact cavity diagnostic

For a sampled column \(j\), write \(c_j=\Gamma_{2,:,j}\).  Beside the original
flow, run a coupled cavity flow in which only this static column is set to
zero at initialization; all endpoint marks, \(\Gamma_1\), all other columns
of \(\Gamma_2\), and numerical choices are shared.  Learned updates remain
fully active.  Denote its top backpropagated field by \(B_3^{(-j)}(s)\).  Then

\[
 H_j(s)=c_j^\top B_3^{(-j)}(s)
\]

is conditionally Gaussian given the cavity trajectory, with conditional
variance \(\|B_3^{(-j)}(s)\|_{2,n}^2\).  The exact same-column response is

\[
 \Delta_j(s)
 =c_j^\top\{B_3(s)-B_3^{(-j)}(s)\},\qquad
 (R_2^{\rm stat})_j=H_j+\Delta_j.
\]

This directly separates a fresh Gaussian cavity contribution from the
adaptive reuse of the same column.  Merely plotting \(R_2\) would not do so.

## 3. Frozen design

- Feature horizons: \(S\in\{0.5,1,2\}\), with checkpoints every \(0.1\).
- Widths for the main trajectories: \(n\in\{128,256,512,1024,2048\}\).
- Widths for the more expensive cavity pairs:
  \(n\in\{128,256,512,1024\}\).
- Independent seeds: eight main seeds at every width; four cavity seeds and
  eight uniformly sampled columns per cavity seed.
- Integrator: classical RK4, base step \(h=0.01\), float64.
- Solver audit: repeat every seed at \(n=128,256\) with \(h=0.005\).  The run
  is numerically valid only if all primary normalized moments and cavity RMS
  diagnostics differ by at most 5% (or by absolute \(10^{-3}\) when the
  statistic is below \(0.02\)), and the trapezoidal defect in
  \(f(s)-f(0)=\int_0^sK(q)dq\) is below 1% of
  \(1+|f(s)-f(0)|\).
- No horizon, seed, width, moment, or checkpoint will be added after seeing a
  favorable plot.  If the hard budget is too costly, the design is truncated
  from the largest width downward and that loss of power is reported.

At every checkpoint report, separately for \(R_2,R_2^{\rm stat}\), and the
learned term:

\[
 \|V\|_{p,n}/p\quad(p=2,4,6,8),\qquad
 \max_i|V_i|,\qquad
 \frac{\max_i|V_i|}{\sqrt{n}\,\|V\|_{2,n}},
\]

the empirical survival probabilities at standardized thresholds
\(2,3,4,5\), the raw kernel and its four block energies, and the maximum over
time of each statistic.  For cavity pairs report the empirical RMS and
0.5/0.9/0.99 quantiles of

\[
 |H_j|/\|B_3^{(-j)}\|_{2,n},\quad |\Delta_j|,\quad
 |\Delta_j|/(1+|H_j|),
\]

and the normalized trajectory difference
\(\sup_s\|B_3-B_3^{(-j)}\|_{2,n}\).

## 4. Precommitted interpretation

Evidence supports continuing the cavity/response route only if all of the
following hold after the solver audit:

1. across every completed width and all three horizons, no median
   \(\sup_s\|R_2\|_{p,n}/p\) grows by more than a factor 1.5 between the
   smallest and largest width, for any reported \(p\);
2. a log-log regression of each such statistic against width has upper 95%
   bootstrap slope below 0.10;
3. the median condensation ratio decreases with width and is below 0.20 at
   the largest completed width;
4. the cavity response \(|\Delta_j|\) and relative response have upper 95%
   bootstrap log-log slopes below 0.10; and
5. no raw tangent block shows a factor-two width increase in its median
   compact-time maximum.

Evidence weighs against that route if a solver-valid statistic violates two
or more of conditions 1--5, or if one violation has lower 95% bootstrap slope
above 0.15 and reproduces at both \(S=1\) and \(S=2\).  An isolated maximum or
one seed is inconclusive.  Passing is not a proof of a \(\psi_1\) envelope;
failure is not a counterexample unless the non-tightness is separately
established as \(n\to\infty\).

## 5. Hard budget and retained artifacts

The CPU budget is six wall-clock hours and the storage budget is 5 GiB.  Only
aggregated JSON records, seed/column indices, software versions, and the
script hash are retained; full matrices are not.  Any crash, truncation,
post-freeze correction, or deviation is appended to this file before the
results are interpreted.

## 6. Frozen aggregation rule

This paragraph was added after the implementation smoke test but before any
cross-width statistic was computed.  For horizon (S\in\{0.5,1,2\}), the
per-run value of a diagnostic is its maximum over the recorded checkpoints
(s\le S).  Width summaries are medians over the eight independent main
seeds.  A reported log--log slope is the ordinary least-squares slope of the
log width medians against log width.  Its 95% interval is obtained from
20,000 independently seeded nonparametric bootstrap replicates, resampling
runs within each width and recomputing both medians and the slope.  Cavity
columns are clustered: first take the median over the eight columns in each
seed, then resample the four seed clusters within each width.  Zero values
are replaced only for logarithms by the smallest positive float; raw values
remain unchanged.  The bootstrap seed is 2026082399.  Solver comparisons are
paired by initialization seed, width, horizon, field, and statistic and use
the symmetric relative discrepancy
(2|x_h-x_{h/2}|/(|x_h|+|x_{h/2}|)), with the preregistered absolute exception.
