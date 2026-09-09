# Research contract: linearly growing counterexample search

## Claim under test

For the width-first, `q=1`, two-hidden-layer OMFP dynamics, put

\[
 \Delta_t(h)=F_{2t}(h)-F_t(2h),\qquad
 \mathcal C_\phi(t,\rho)=
 \sup_{0<|h|\le \rho/t}
 \frac{|\Delta_t(h)-\kappa_t h^3|}{|h|^5}.
\]

The universal claim under test is

\[
 |\phi(x)|\le C(1+|x|)
 \quad\Longrightarrow\quad
 \mathcal C_\phi(t,\rho)=O_\phi(t^5)
\]

for some fixed `rho>0`.  A genuine disproof must exhibit one fixed
activation for which the width-first outputs exist at every finite
schedule and

\[
 \limsup_{t\to\infty}\mathcal C_\phi(t,\rho)/t^5=\infty.
\]

The exact coefficient `[h^5] Delta_t` is not the target: its temporal
degree is universally at most four whenever the fifth width-first jet
exists.

## Admissibility used in the nontrivial search

The activation is fixed, smooth, RMS-normalized, at most linearly growing,
and has every Gaussian derivative moment required by each finite OMFP DAG.
An activation for which the first gradient field or a fixed-step output is
undefined is recorded only as an ill-posedness counterexample, not as a
counterexample to the intended finite-output statement.

## Candidate families

1. Natural oscillatory residuals
   \[
   \phi_{p,\lambda}(x)=
   \frac{x+\lambda\sin(x^p)}{
   \|G+\lambda\sin(G^p)\|_2},
   \qquad p\in\{3,5\}.
   \]
   These are linearly growing and smooth, all their Gaussian derivative
   moments are finite, but their derivatives are unbounded.
2. Smooth monotone spike ladders, whose derivative has very high, very
   narrow positive bumps of summable area.  These separate linear growth
   of the activation from high derivative moments along transported laws.

## Proof obligations

1. Keep the fixed-width/width-first network and its reused-matrix response
   terms; a scalar proxy is evidence only.
2. Establish a signed lower bound for the actual paired discrepancy, not
   merely an upper bound on a trajectory moment.
3. Control cancellation between fine and coarse schedules and between
   all OMFP response histories.
4. Check fixed-schedule integrability before taking `t -> infinity`.

