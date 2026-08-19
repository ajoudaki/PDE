# Independent Route S contract: hidden-activation RMS head

**Frozen before inspecting any competing `Gamma_04` transition.**

## Canonical target

For one input, shared activation, unit forward Grams, and every separately
fixed hidden depth `H`, let

\[
 \dot\theta=n\nabla f(\theta),\qquad
 X_\ell^{(r)}=\left.\frac{d^r}{ds^r}x^\ell(\theta(s))\right|_{s=0}.
\]

The target is the annealed population contraction

\[
 \Gamma^\ell_{04}
 =\lim_{n\to\infty}\mathbb E\,n^{-1}
   \langle X_\ell^{(0)},X_\ell^{(4)}\rangle
\]

for every `1 <= ell <= H`, expressed by an arbitrary-depth deterministic
recurrence containing only rational arithmetic, prior scalar states, and

\[
 M_{\nu_0\ldots\nu_5}
 =\mathbb E_{G\sim N(0,1)}\prod_{r=0}^5\phi^{(r)}(G)^{\nu_r}.
\]

The universal inputs are the already frozen and audited feature-ascent
backbone states through the `R3` pass.  They may be reused but not changed.
The observable head must not retain auxiliary Gaussians, response matrices,
random covariances, pseudoinverses, or an unnamed Wick operator.

## Limit and theorem boundary

The algebra is first derived at finite width and then Wick--Stein contracted
at a separately fixed depth.  Identification with the annealed limit is a
separate theorem-level bridge.  A sufficient convenient hypothesis is that
`phi` is polynomially smooth and the finite tensor program converges in every
finite `L^p`; a weaker bridge must separately establish convergence in
probability plus uniform integrability of the finite-width hidden-feature
derivatives used through order four.

No statement is depth-uniform, positive-time, growing-width/depth joint,
multi-sample, or all-orders.

## Required proof and audit obligations

1. Derive the exact finite-width feature and squared-norm Leibniz identities.
2. Enumerate every local product-rule/equality-partition contribution,
   including the transpose-response terms inherited from the gradient jets.
3. Eliminate every local Gaussian by a terminating Wick--Stein recursion.
4. Freeze the resulting scalar transition before inspecting a competing
   `Gamma_04` formula.
5. Expand the frozen recurrence and compare it atom by atom, with exact
   rational arithmetic, against an independently canonicalized population
   jet at several depths.
6. Pass constant, linear, and normalized affine controls and the separately
   frozen smooth-nonpolynomial regression.

## Sharp candidate and falsifiers

The candidate is that `Gamma_04` closes in one additional bottom-up pass
after `R3`, with a fixed scalar dimension independent of `H`.  The smallest
state found will be reported without a minimality claim.

A nonzero exact atom discrepancy against the independent population jet is a
witness falsifier.  A missing response derivative, an unpaired Gaussian, or
an activation derivative above order five is a derivation falsifier.  A
valid preregistered nonpolynomial regression with `|z| > 5` falsifies either
the witness or its annealed scaling bridge, but not the universal-observable
principle in general.

## Authorization and budget

The user authorized theory, implementation, exact symbolic computation,
finite-width experiments, and independent parallel audit.  The regression
budget is fixed separately in `NONPOLYNOMIAL_EXPERIMENT_CONTRACT.md`.
