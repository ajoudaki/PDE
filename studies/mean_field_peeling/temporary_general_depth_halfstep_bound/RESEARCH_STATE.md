# General-depth two-versus-one half-step comparison

## Scope and limit order

For every fixed hidden depth `L >= 1`, first send the common width `n` to infinity at fixed nonzero step size `h`.  Only after the finite-width network has been identified pointwise with its Gaussian operator DAG do we study `h -> 0`.

The discrepancy is

\[
\Delta_L(h)=F_{2,L}(h)-F_{1,L}(2h).
\]

No finite-width Taylor expansion may be interchanged with the width limit, and no coefficient or remainder constant may be defined from derivatives, continuity moduli, or trajectories of the unknown limiting output.

## Target claim

Construct, directly from Gaussian integrals of the activation and a stated weighted derivative envelope,

\[
\kappa_{\phi,L},\qquad B_\phi\ge1,\qquad 0<h_\phi\le1,
\]

and an explicit depth-only integer `E_L`, so that

\[
\left|\Delta_L(h)-\kappa_{\phi,L}h^3\right|
\le B_\phi^{E_L}|h|^5,
\qquad |h|\le h_\phi^{E_L}.
\]

The coefficient may depend on depth through its finite Gaussian recursion.  The bases `B_phi` and `h_phi` must not depend on depth.  A sharper intermediate theorem with explicitly recursively computed `B_{phi,L}` and `h_{phi,L}` is also retained.

## Required bridges

1. Exact finite-width network and updates at depth `L`.
2. Pointwise fixed-`h` convergence of the actual one- and two-step expected outputs, including every reused-matrix response, empirical Gram, concentration estimate, and uniform-integrability step.
3. An inverse-free primitive-coordinate Gaussian DAG and independent `C^5` regularity at `h=0`, including singular two-time covariances.
4. Exact nodewise Price-jet recursion for `kappa_{phi,L}` and an activation-envelope fifth-order bound.
5. Explicit positivity/radius estimates for all `2(L-1)` nonterminal two-time Grams.
6. A finite induction that separates activation-only bases from an explicit depth-only factor.

If any bridge is not closed, the quantitative theorem is to be labelled conditional or open.

## Current verdict

Proved after the independent defect-finding audit recorded in `AUDIT.md`.
WIDTH_GENERAL.md closes the fixed-nonzero-step finite-width
bridge, including the adaptive reused-matrix responses, concentration, and
uniform integrability.  RANK_GENERAL.md proves positivity of exactly the
\(2(L-1)\) nonterminal Grams and constructs their activation-defined
radius.  COMPILER_GENERAL.md proves singular-covariance \(C^5\)
regularity, defines the Gaussian-integral cubic coefficient, and supplies
the fifth-order envelope and the explicit depth separation.  The cases
\(L=1\) and \(d=0\) are handled directly.

## Claim policy

- `proved`: every bridge above is closed in the accompanying files.
- `conditional`: the algebraic/envelope theorem is proved for the displayed DAG, but finite-width identification or a regularity bridge is assumed.
- `open`: an indispensable positivity, conditioning, concentration, regularity, or limit-identification step is missing.
