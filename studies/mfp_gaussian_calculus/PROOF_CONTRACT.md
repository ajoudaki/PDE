# Generic first Stieltjes correction: proof contract

**Status:** Base-case contract; amended after the probabilistic bridge audit  
**Frozen:** 2026-08-18  
**Amended:** 2026-08-18

## 1. Base model

The first accepted target is a bias-free fully connected network with two
hidden layers, one fixed input, one scalar output, and the centered mean-field
readout

\[
u_j=\frac{w_j^\top x}{\sqrt{d_0}},\qquad
z_i=\frac1{\sqrt n}\sum_{j=1}^n W_{ij}\phi(u_j),\qquad
f_n=\frac1n\sum_{i=1}^n a_i\phi(z_i).
\]

All entries of \(w,W,a\) are independent standard Gaussians.  The fixed input
has \(q_0=\|x\|^2/d_0\in(0,\infty)\).  The raw-coordinate feature-ascent
operator and the one-sample squared-loss flow are

\[
D_n=n\nabla f_n\mathbin\cdot\nabla,
\qquad
\dot\theta=2\eta(1-f_n)n\nabla f_n,
\qquad
L_n=(1-f_n)^2.
\]

The theorem-level activation class is **polynomially smooth**:
\(\phi\in C^\infty(\mathbb R)\), with every derivative of every order bounded
by a polynomial (whose degree may depend on the derivative order).  The final
normal form itself uses only \(\phi,\phi',\phi'',\phi'''\), but the published
\(L^p\) Tensor-Program theorem used for the annealed limit has this stronger
all-orders hypothesis.  A weaker tier, in which only these four maps are
pseudo-Lipschitz, gives the almost-sure coefficient but requires a separate
uniform-integrability condition for convergence of expectations.  This
deliberately excludes a direct ReLU claim; weak-derivative and
Gaussian-boundary formulas are a later contract.

## 2. Target coefficients and limit order

At fixed derivative order, before any positive-time or series-convergence
claim, define

\[
A=\lim_{n\to\infty}\mathbb E[D_nf_n],\qquad
C=\lim_{n\to\infty}\mathbb E[D_n^3f_n],\qquad
\mu_0=\frac{C}{2A^2},
\]

provided the displayed limits exist and \(A>0\).  The mandatory logical order
is:

1. differentiate and scalarize at finite width;
2. perform the complete equality/response and global-width audit on that exact
   finite-width scalar;
3. justify the joint Gaussian limit and empirical-covariance replacement;
4. justify passage to the annealed coefficient, either by an exact
   finite-width expectation calculation or by \(L^1\) (in particular \(L^p\))
   convergence of the exact scalar;
5. keep the derivative order fixed throughout the \(n\to\infty\) argument.

The base target is an annealed coefficient.  For this particular observable,
the exact scalar Tensor Program converges almost surely to its deterministic
normal form, so no separate multi-copy argument is required for the typical
limit.  Multi-copy machinery would still be needed for quantitative variance
rates or observables not encoded as one fixed program scalar.

## 3. Required Gaussian normal form

An accepted result for \(C\) must be a finite sum of explicitly specified
Gaussian atoms

\[
\mathcal I(\Sigma;\mathbf i,\mathbf r)
=
\mathbb E_{G\sim N(0,\Sigma)}
\left[\prod_{s=1}^m\phi^{(r_s)}(G_{i_s})\right].
\]

Every atom must display or recursively construct from earlier displayed atoms:

- its finite dimension and covariance matrix \(\Sigma\);
- every coordinate index \(i_s\) and activation-derivative order \(r_s\);
- its exact rational/integer coefficient and every factor of \(q_0\);
- all products and contractions between atoms.

The final expression may not contain random weights, neuron sums, random
empirical covariances, implicit backward/tangent variables, unnamed response
terms, unevaluated Stein derivatives, or an instruction to take a limit.
No Hermite, polynomial, or numerical approximation to \(\phi\) is permitted.

## 4. Exact algebraic skeleton

In raw coordinates write \(p_\theta=\nabla_\theta f_n\),
\(H_\theta=\nabla_\theta^2f_n\), and
\(T_\theta=\nabla_\theta^3f_n\).  Then the exact identity is

\[
D_n^3f_n=n^3\left(
4\|H_\theta p_\theta\|^2
+2T_\theta[p_\theta,p_\theta,p_\theta]
\right).
\]

Equivalently, whiten the constant optimizer metric by defining

\[
\vartheta=\theta/\sqrt n,
\qquad \theta=\sqrt n\,\vartheta.
\]

Only after this definition, put

\[
p_n=\nabla f_n,\qquad H_n=\nabla^2f_n,\qquad T_n=\nabla^3f_n.
\]

The equivalent whitened-coordinate identity

\[
D_n^3f_n=4\|H_np_n\|^2+2T_n[p_n,p_n,p_n]
\]

must be derived and then expanded without deleting a term because its
one-copy mean vanishes.  Readout parity may be used only after the complete
finite-width contraction carrying that readout factor has been formed.

## 5. Acceptance gates

The base case is accepted only if all gates pass.

1. **Finite-width derivation:** every chain/product-rule term and metric factor
   is accounted for.
2. **Peeling audit:** readout, second-layer, and first-layer eliminations list
   every equality partition, Wick branch, Stein branch, and final width degree,
   or an equivalent exact Tensor-Program response registry proves that the
   listed response/equality sectors are exhaustive.
3. **Explicitness:** the result satisfies Section 3 literally.
4. **Independent route:** a second derivation with a distinct representation
   agrees atom-for-atom after canonicalization, or an exact identity proves the
   two representations equivalent.
5. **Quadratic regression:** substituting \(\phi(x)=x^2\) gives exactly
   \[
   A=111,\qquad C=1\,685\,184,\qquad
   \mu_0=\frac{280864}{4107}.
   \]
6. **Degenerate controls:** readout-only training gives \(C=0\), and at least
   one independently solvable nonquadratic or linear specialization agrees.
7. **Loss conversion:** direct differentiation of the finite-width loss and
   conversion through the feature coordinate agree through the first
   feature-dependent loss coefficient.
8. **Probabilistic scope:** expectation, covariance replacement, and
   concentration claims are separately labelled; no positive-time conclusion
   is inferred from a fixed jet.
9. **Reproducibility:** exact scripts, tests, commands, source hashes, and any
   failed route are retained.

Failure of a gate makes the base result incomplete, not approximately accepted.

## 6. Extension order

No extension is promoted before the base case passes all applicable gates.
The intended order is

\[
(L=2,B=1)\to(L=2,B=2)\to(L=2,B\text{ fixed})
\to(L\text{ fixed},B\text{ fixed}).
\]

The \(B=2\) stage first treats normalized equal/opposite-label symmetry
channels, where a scalar Stieltjes coordinate remains meaningful, and then
arbitrary fixed labels through the first non-NTK loss jet.  The depth stage
requires a separately proved layer-local boundary-state closure; an \(O(L)\)
normal-form DAG is a conclusion, not an assumption.
