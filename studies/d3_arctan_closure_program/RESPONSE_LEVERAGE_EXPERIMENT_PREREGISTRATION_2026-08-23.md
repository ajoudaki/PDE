# Preregistration: column-response leverage and entropy

**Frozen before execution:** 23 August 2026.

This experiment tests only the specific mechanism left open by the signed
transport and no-self-loop audits: whether the canonical Frobenius column
response remains delocalized across neuron rows.  It cannot prove the tail
lemma.

## Quantity

For a sampled middle column \(j\), let

\[
 g_j=\sqrt n\,\Gamma_{2,:,j},\qquad
 J_j(s)=D_{g_j}B_3(s).
\]

For independent Rademacher probes \(v_a\in\{-1,1\}^n\), central differences
estimate \(J_jv_a\).  The Hutchinson row-energy estimator is

\[
 \widehat\ell_i^2=q^{-1}\sum_{a=1}^q|(J_jv_a)_i|^2,
 \qquad
 \widehat w_i=\frac{\widehat\ell_i^2}{\sum_k\widehat\ell_k^2}.
\]

At every checkpoint record

\[
 \widehat F=\Big(\sum_i\widehat\ell_i^2\Big)^{1/2},\quad
 \widehat H=\sum_i\widehat w_i\log(n\widehat w_i),\quad
 \widehat I=n\sum_i\widehat w_i^2,
\]

the largest \(n\widehat w_i\), and the mass carried by the largest one
percent of rows.  Here \(H=0,I=1\) for perfectly uniform leverage and
\(H=\log n,I=n\) for one-row condensation.

## Frozen design

- widths: \(128,256,512\);
- four seeds per width;
- feature horizon: \(4\);
- RK4 step: \(0.02\), checkpoints every \(0.2\);
- one uniformly sampled raw middle column per run;
- four Rademacher probes;
- central perturbation \(\varepsilon=2\cdot10^{-4}\) in the standard-Gaussian
  column coordinate \(g_j\);
- solver/finite-difference audit at widths \(128,256\) with step \(0.01\) and
  perturbation \(10^{-4}\) on the same seeds and probes.

All decisions use the maximum over checkpoints up to horizons \(1,2,4\),
then the median across seeds at each width.  Log--log slopes are computed
from the three width medians.  The small solver audit passes if every
reported statistic changes by at most 10 percent symmetrically (or \(10^{-3}\)
absolutely when both values are below \(0.02\)).

## Frozen interpretation

Subject to the solver audit:

**Evidence against delocalization** is declared if, at horizon 2 or 4, any
of the following occurs:

1. the median response Frobenius norm has width slope at least \(0.25\);
2. the median inverse participation \(\widehat I\) has width slope at least
   \(0.30\) and its width-512 value exceeds \(8\);
3. the median top-one-percent leverage mass exceeds \(0.35\) at width 512
   and increases from width 128;
4. the median entropy ratio \(\widehat H/\log n\) exceeds \(0.45\) at width
   512 and increases from width 128.

**Mechanistic support** is declared only if, at both horizons 2 and 4,

1. the Frobenius slope is below \(0.15\);
2. the inverse-participation slope is below \(0.15\) and its width-512 value
   is below \(5\);
3. the width-512 top-one-percent mass is below \(0.20\); and
4. \(\widehat H/\log n<0.30\) at width 512.

Any other outcome is inconclusive.  Even a support verdict leaves the
mesh-uniform logarithmic-moment theorem open.
