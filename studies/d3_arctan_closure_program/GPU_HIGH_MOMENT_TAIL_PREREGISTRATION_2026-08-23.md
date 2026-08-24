# Preregistration: high-moment and action-stratified middle-query audit

**Frozen before running the new GPU simulation.**

## Question

For the exact canonical, fully trained, three-hidden-vector arctangent
feature flow, does the empirical coordinate law of

\[
 R_2(s)=G_2(s)^*B_3(s)
\]

show the moment growth expected from a mesh- and width-uniform
(\psi_1) bound, or does it show reproducible super-exponential-tail moment
growth at the first horizons where the column response localizes?

This is a falsification/route-selection experiment.  It cannot prove an
Orlicz theorem.

## Frozen model and solver

- iid (A_0,u_0,W_1,W_2\sim N(0,1)), with
  (G_\ell=W_\ell/\sqrt n);
- exact feature vector field from the frozen contract, with every block
  trained and no clipping or normalization;
- explicit midpoint (RK2) integration in the original (u)-coordinate,
  (u'=D_1Q_1), so that the natural-coordinate correction is not omitted;
- main step (h=0.01), paired solver audit at (h=0.005) on a frozen
  subset;
- feature horizons (s\in\{1,2,4,8\}), subject to the solver checks below;
- float32 main simulation, with a frozen float64 CPU/GPU spot audit at the
  two smallest widths.

Widths and target independent replicas are

\[
(n,N_n)=(256,512),(512,256),(1024,128),(2048,32).
\]

Before inspecting any output, the paired fine/coarse subset is fixed as
((64,32,16,8)) replicas at the same four widths, using common initial
draws identified by seed offset `314159`.  The float64 spot audit uses eight
common-draw replicas at widths 256 and 512 and horizon 2.  These smaller
paired samples test discretization/arithmetic only; they are not substituted
for the main moment sample.

The run may stop a horizon for all widths if the paired relative RMS solver
difference exceeds the threshold below; a failed horizon is reported, not
silently discarded.  Seeds are generated from the fixed master seed
`2026082303` by a documented counter-based rule.

## Recorded quantities

At every frozen horizon and replica record

1. empirical moments of (|R_2|) at
   (p\in\{2,3,4,6,8,10,12\});
2. the same moments for (B_2=D_2R_2) and (Q_1=G_1^*B_2);
3. the maximum and the (0.99,0.999,0.9999) pooled absolute quantiles;
4. every raw tangent-kernel block;
5. the accumulated lower action
   \[
   \mathcal A_2(s)=\int_0^s\langle R_2,H_2R_2\rangle_n,d\sigma,
   \quad
   H_2=D_2\{\rho_1I+G_1D_1^2G_1^*\}D_2;
   \]
6. per-replica moments, so all uncertainty calculations cluster by network
   rather than treating coordinates as independent.

For each field (Y), define

\[
 m_p(Y)=\langle|Y|^p\rangle_n^{1/p},\qquad
 \widehat\alpha_Y=\operatorname{slope}_{p=4,6,8,10,12}
       \{\log(m_p/m_2)\text{ versus }\log p\}.
\]

Also record (m_{12}/(2m_6)), which is asymptotically at most constant
under linear moment growth and grows like (\sqrt2) for an ideal cubic
Gaussian-chaos scale after normalization.

## Frozen numerical-validity checks

A horizon/width comparison passes only if, for (R_2,B_2,Q_1), all of

- paired fine/coarse relative RMS difference is at most (0.03);
- relative differences of (m_p) are at most (0.06) for (p\le8) and
  (0.12) for (p=10,12);
- the raw-kernel relative difference is at most (0.03);
- no NaN/Inf occurs and the exact nonnegative-kernel identity is respected
  to the stated floating-point tolerance.

Failure triggers a rerun at half the main step; it does not authorize
dropping the width or horizon.

## Frozen interpretation rules

Use a network-cluster bootstrap with 2,000 deterministic resamples.

Evidence **against** the proposed uniform (psi_1) route is declared only
if, at a solver-valid horizon, both largest widths have

1. the lower 95% cluster-bootstrap endpoint of
   (widehat\alpha_{R_2}) above (1.15); and
2. the lower endpoint of (m_{12}/(2m_6)) above (1.20);

with neither statistic decreasing from (n=1024) to (n=2048).

Evidence **supporting continued pursuit** of the (psi_1) route is declared
only if every solver-valid width at horizons (2) and (4) has

1. upper endpoint (widehat\alpha_{R_2}\le1.05);
2. upper endpoint (m_{12}/(2m_6)\le1.20);
3. no positive width slope above (0.10) for any normalized moment
   (m_p/p), (p\le12); and
4. the upper endpoint of the width slope of each raw kernel block is below
   (0.10).

Anything else is inconclusive.  Even a formal support result is only
empirical weight: it neither supplies the signed predictor/bracket lemma nor
changes a theorem status.

## Action-stratified exploratory diagnostic

The action relation is recorded under this preregistration, but no binary
claim is attached to it.  Replicas are stratified into fixed empirical
quartiles of (mathcal A_2), and the same moment-growth statistics are
reported within each stratum.  This distinguishes a tail driven by large
total lower work from one driven by response leverage at ordinary work.
It may suggest a sharper theorem but cannot retroactively alter the frozen
support/rejection thresholds.
