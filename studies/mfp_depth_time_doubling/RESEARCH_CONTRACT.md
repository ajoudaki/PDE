# Research contract: simultaneous depth and time doubling

## Scope

Only the material under `studies/mean_field_peeling` is admissible as
project evidence.  This study concerns the actual fully trained mean-field
MLP with scalar input, common hidden width `n`, no biases, and `L` hidden
layers.  The width limit is always taken at fixed nonzero step size before
the small-step limit.

## Network and comparison

For `s >= 0`,

\[
 Z_1^s=u^s,\quad X_1^s=\phi(Z_1^s),\qquad
 Z_\ell^s=n^{-1/2}W_\ell^sX_{\ell-1}^s,\quad
 X_\ell^s=\phi(Z_\ell^s),
\]

for `2 <= ell <= L`, and

\[
 f_{n,L}^s=n^{-1}(a^s)^TX_L^s.
\]

All entries of `u^0,a^0,W_2^0,...,W_L^0` are independent standard
Gaussians.  Every parameter is updated simultaneously by

\[
 \theta^{s+1}=\theta^s+hn\nabla_\theta f_{n,L}^s.
\]

At each fixed `h`, define

\[
 F_{N,L}(h)=\lim_{n\to\infty}\mathbb E f_{n,L}^N,
 \qquad
 D_{t,L}(\eta)=F_{t,L}(2\eta)-F_{2t,L}(\eta).
\]

## Activation class

\[
 \phi\in C^{12}(\mathbb R),\qquad
 \mathbb E\phi(G)^2=1,
\]

\[
 M_\phi=\max\left\{1,
 \sup_x\frac{|\phi(x)|}{1+|x|},
 \max_{1\le r\le12}\|\phi^{(r)}\|_\infty\right\}<\infty .
\]

The constant-activation branch is to be treated exactly and separately.

## Primary claim ladder

1. **Depth-three, fixed-time theorem.**  For every integer `t >= 1`,
   identify both width-first outputs at every fixed nonzero step, prove
   singular-covariance `C^5` regularity, reduce the cubic coefficient to a
   terminating Gaussian activation-integral recursion, and give an
   activation-envelope fifth-order remainder with explicit `t` dependence.

2. **Arbitrary fixed depth and time.**  Prove the same theorem for every
   finite pair `(L,t)`, with activation-only numerical bases and a completely
   explicit exponent depending only on `(L,t)`.

3. **Sharp time law for the cubic coefficient.**  Test whether
   `kappa_{phi,L,t}` is exactly a quadratic polynomial in `t`, and whether
   it reduces to `-t(2t-1)J_{phi,L}/2`.  Promote the one-invariant formula
   only after a nodewise width-first intertwining or an equivalent Gaussian
   DAG identity is proved.  Otherwise retain the proved two-invariant
   quadratic formula.

4. **Uniform-in-time fifth-order scale.**  A bound of the form
   `C_phi,L t^4 |eta|^5` on `|eta| <= c_phi,L/t` is a separate conjecture.
   It is not implied by a terminating fixed-time compiler.  The linear
   activation obstruction rules out any general power below four.

## Required proof bridges

1. Exact finite-width update and the full `(2N+1)(L-1)` predictable
   reused-matrix action chronology.
2. Full-rank population history Grams at every fixed `h != 0`, including
   non-affine, affine, and constant branches.
3. Adaptive row/column Gaussian conditioning for all reused matrices,
   response cancellation, empirical concentration, stopping removal, and
   terminal uniform integrability.
4. An inverse-free depth-time Gaussian DAG derived from that network.
5. A terminating singular Price compiler through order five with a stated
   activation envelope and no output-derived constants.
6. A direct nodewise derivation of the time polynomial for the cubic jet.
7. An explicit remainder constant and radius; no unspecified little-o,
   trajectory modulus, or opposite-order finite-width Taylor limit.

## Claim policy

- `proved`: every bridge is closed in the written proof and survives a
  fresh hostile audit.
- `conditional`: the exact extra hypothesis and the missing bridge are
  displayed next to the claim.
- `open`: no available argument closes an indispensable bridge.

