# Audit of the general-depth half-step theorem

Date: 2026-08-25.

## Scope

This audit treats as untrusted the theorem

\[
 \left|F_{2,L}(\eta)-F_{1,L}(2\eta)-\kappa_{\phi,L}\eta^3\right|
 \le B_\phi^{E_L}|\eta|^5,
 \qquad |\eta|\le h_\phi^{E_L},
\]

with the width limit taken at each fixed nonzero step before the
small-step analysis.  It checks the finite-width bridge, reused-matrix
responses, rank opening, singular-covariance compiler, explicit envelope,
and final composition of constants.

## Defects found and repaired

1. `WIDTH_GENERAL.md` incorrectly propagated an \(O(n^{-1/4})\) terminal
   coupling error through every remaining layer.  Successive zero Schur
   complements can weaken that rate.  The corrected recursion is

   \[
    \delta_{1,n}=n^{-1/2},\qquad
    \delta_{a+1,n}=C_a(n^{-1/2}+\delta_{a,n})^{1/2},
   \]

   hence \(\delta_{a,n}=O(n^{-2^{-a}})=o(1)\) for each fixed depth.
   No terminal three-time Gram is inverted, so stopping, uniform
   integrability, and expected-output convergence survive.

2. `COMPILER_GENERAL.md`, Lemma 6.1, originally omitted the
   \(D^s\le5^{10}\) ordered-index aggregation and the covariance/binomial
   contraction multiplicities.  The corrected fully expanded tree ledger
   uses at most

   \[
    1+10+1+5+1=18<20
   \]

   complexity levels.  A structural induction proves
   \(|\partial e|\le2|e|^2\); multiindex aggregation costs one level; and
   each Price assembly is bounded after expanding at most 801 summands.
   The original \(c_{20},A_*,q_*\), hence \(B_\phi,h_\phi,E_L\), remain
   sufficient.

3. The first singular-Gaussian regularization argument did not control
   large Gaussian components in covariance-null directions.  It now uses
   the coupling

   \[
    Y_{\epsilon,h}=(\Sigma(h)+\epsilon I)^{1/2}G,
    \qquad Y_h=\Sigma(h)^{1/2}G,
   \]

   truncates on \(\{\|G\|\le R\}\), and controls the complement by an
   explicit Gaussian polynomial tail.  This proves uniform convergence
   of the regularized Price identities and permits iteration through order
   five at singular covariances.

4. The binary-tree template counts and the \(L\ge2\) scope of the top
   rank estimate were corrected explicitly.  The largest raw template is
   now 81, still below \(c_0=128\).

## Final subsystem verdicts

- Exact network, normalization, adaptive Gaussian conditioning, and all
  reused-row/column responses: pass.
- Concentration, stopping removal, uniform integrability, and pointwise
  fixed-step expected-output convergence: pass after repair 1.
- Feature/cotangent determinant jets, positivity, affine and constant
  activation branches, and rank radius: pass.
- Inverse-free \(3L-2\)-call DAG, singular \(C^5\) Price regularity,
  activation-integral definition of \(\kappa_{\phi,L}\), and explicit
  envelope compiler: pass after repairs 2--4.
- Final factors \(8\), \(32\), \(1/120\), the interval for both
  \(F_{2,L}(\eta)\) and \(F_{1,L}(2\eta)\), and the corollary with
  \(\varepsilon\): pass.

## Verdict

The pre-audit artifact was **not fully valid as written**.  After the
displayed repairs, the theorem passes the stated audit for every fixed
finite depth \(L\) under its stated \(C^{12}\), bounded-derivative,
at-most-linear-growth activation assumptions.  The proof preserves the
required order \(n\to\infty\) at fixed step, followed by \(\eta\to0\),
and no constant is defined from the unknown limiting output or trained
trajectory.
