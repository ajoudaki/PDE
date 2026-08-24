# Preregistration: forward-query characteristic budget

**Frozen before the run:** 23 August 2026.

## Mathematical question

The exact top characteristic for a row response uses
\(V=\delta Z_3/d(Z_3)\).  Its homogeneous coefficient contains no naked
\(A,d'(Z_3)\); the remaining unbounded scalar coefficient is bounded by
\[
 W_i(T)=\int_0^T |(G_2(t)\dot X_2(t))_i|\,dt.             \tag{1}
\]
A row-cavity proof based on finite-difference saturation would become viable
if a positive exponential parameter for the empirical law of \(W(T)\) were
stable with width.  Energy controls only \(n^{-1}\sum_iW_i^2\) and does not
imply such an estimate.  This experiment tests width scaling; it cannot prove
an exponential moment or change a theorem rung.

The exact feature-time velocity used in the diagnostic is
\[
\begin{aligned}
 \dot X_1&=D_1^2Q_1,\\
 \dot Z_2&=\|X_1\|_n^2B_2+G_1\dot X_1,\\
 \dot X_2&=D_2\dot Z_2,\\
 w&=G_2\dot X_2.
\end{aligned}                                             \tag{2}
\]
The integral in (1) is accumulated at the explicit-midpoint state.  We also
record its static and learned pieces, \(\Gamma_2\dot X_2\) and
\((G_2-\Gamma_2)\dot X_2\), separately.

## Frozen design and statistics

Use the canonical iid-Gaussian initialization and the unclipped feature-time
flow.  Main widths are
\[
 n=256,512,1024,2048,4096,
\]
with independent-replica counts \(64,48,24,12,6\), respectively.  The main
integrator is explicit midpoint with step \(h=0.01\), float32 evolution and
float64 aggregation.  Record at \(T=1,2,4\):

1. \(\|W(T)\|_{q,n}\) for \(q=2,4,6,8\);
2. \(L_\lambda(T)=\lambda^{-1}\log\langle
   e^{\lambda W(T)}\rangle_n\) for \(\lambda=0.25,0.5,1\);
3. the same quantities for the static and learned absolute-integral pieces;
4. the 0.99 and 0.999 empirical quantiles and maximum of \(W\); and
5. the midpoint identity residual
   \(\|w-(\Gamma_2+(G_2-\Gamma_2))\dot X_2\|_n\).

A common-draw step-halving audit uses \(h=0.005\) at \(n=256,512\), and a
common-draw float64 audit uses \(n=128,256\).

## Frozen interpretation

For each horizon and each primary statistic in items 1--2, fit the OLS slope
of the log replica median against \(\log n\), with a replica bootstrap
95-percent interval.  The result is **formal empirical support** for width
stability only if:

1. every central slope is at most \(0.08\);
2. every upper 95-percent endpoint is at most \(0.15\);
3. every available largest-width/smallest-width median ratio is at most
   \(1.60\);
4. every median symmetric relative step-halving and arithmetic discrepancy is
   at most \(0.08\); and
5. the decomposition residual is at most \(10^{-5}\) in float32 and
   \(10^{-10}\) in float64.

There is **formal evidence against** width stability if, for some
\(\lambda\in\{0.5,1\}\), the lower 95-percent slope endpoint of
\(L_\lambda(T)\) exceeds \(0.15\) at both \(T=2,4\), the largest/smallest
median ratio exceeds \(1.60\), and all numerical audits pass.  Any other
outcome is inconclusive.  Passing cannot exclude a rare-event divergence or
supply the conditional row-cavity exponential required by a proof.
