# Frozen hostile-audit contract: `B=1`, depth `H=3,4`, order five

**Freeze date:** 2026-08-18  
**Producer isolation:** this route is written without reading either depth-
order-five coefficient artifact.  Producer artifacts may be opened only after
both producers declare their maps frozen.

## 1. Exact model and normalization

For one deterministic input `x`, put

\[
z^1_j={w_j^Tx\over\sqrt{d_0}},\qquad h^1=\phi(z^1),
\]

and, for `2<=ell<=H`,

\[
z^\ell={1\over\sqrt n}W^\ell h^{\ell-1},\qquad
h^\ell=\phi(z^\ell),
\qquad
f_n={1\over n}a^Th^H.
\]

Every entry of `w,W^2,...,W^H,a` is an independent standard Gaussian at
initialization.  The Euclidean gradient includes every one of these
parameters, and

\[
D_n=n\nabla f_n\mathbin\cdot\nabla,
\qquad
F_H^{(k)}(0)=\lim_{n\to\infty}{\mathbb E}[D_n^kf_n].
\]

The first forward variance is `Q0=||x||^2/d0`; recursively
`Q^ell=E[phi(G_{Q^(ell-1)})^2]`.  Width tends to infinity only after every
finite-width derivative is formed.  Hidden depth and batch size remain fixed.

## 2. Target and terminal grammar

For each `H=3,4`, the proposed deliverable must give

\[
A_H=F_H'(0),\qquad B_H=F_H^{(3)}(0),\qquad C_H=F_H^{(5)}(0)
\]

as a literal finite deterministic arithmetic expression in layer-tagged
one-dimensional Gaussian atoms

\[
M^{\ell}_{\nu}
=\mathbb E_{G\sim N(0,Q^{\ell-1})}
\prod_{r=0}^5\phi^{(r)}(G)^{\nu_r}.
\]

The clean unit-Gram quotient may identify the layer tags and impose
`M_200000=1`.  A response recursion, unevaluated Gaussian auxiliary,
pseudoinverse, empirical covariance, or unnamed tangent/backward Gram is not
a terminal formula.  No Hermite or polynomial approximation of `phi` is
allowed.

## 3. Claim ladder

1. **Exact finite width:** feature-flow ODE, moving Taylor jet, raw-coordinate
   derivative checks, scaling, and readout parity.
2. **Formal population candidate:** equality partitions, fresh Gaussian
   sectors, transpose responses, and rank-update branches before elimination.
3. **Algebraically audited normal form:** all auxiliaries eliminated, terminal
   derivative order at most five, two independently frozen maps equal literally
   over a declared common quotient, and every exact control passes.
4. **Theorem-level annealed coefficient:** the fixed finite program satisfies
   a named tensor-program theorem's hypotheses and an `L^1`/uniform-
   integrability bridge.

No empirical check promotes item 2 or 3.  No almost-sure limit alone promotes
item 4.

## 4. Mandatory hostile gates

- derive the exact arbitrary-depth feature ODE and all width factors;
- verify `E f_n=E D_n^2f_n=E D_n^4f_n=0` at finite width;
- compare a moving-flow fifth-order jet with a separately implemented raw
  multivariate derivative route at `H=3,4`;
- census every same-orientation, opposite-orientation/transpose-response, and
  explicit rank-update sector through order five at every layer;
- prove that the terminal activation derivative order is at most five;
- obtain exact deep-linear large-width controls for `H=3,4`, preferably from
  an arbitrary-`H` formula, and check finite-width corrections independently;
- include constant and affine controls and a smooth nonpolynomial finite-width
  discriminator fixed before reading producer maps;
- state exact theorem regularity and uniform-integrability hypotheses;
- after producer freeze, compare every coefficient atom by atom and verify
  hashes, grammar, derivative ceiling, and layer normalization;
- attack any claimed simple arbitrary-depth recursion for hidden chronological
  state, nonlocal transpose responses, or an implicitly exponential terminal
  expansion.

Promotion is forbidden while any leading equality/response branch, exact
control, literal coefficient difference, or annealed-limit hypothesis remains
unresolved.

## 5. Falsifiers fixed before map inspection

The route fails promotion if any of the following occurs:

1. the moving-flow and raw-coordinate jets differ beyond floating roundoff;
2. a producer terminal atom contains `phi^(r)` with `r>5`;
3. the two frozen coefficient dictionaries differ at one canonical key;
4. either map fails a deep-linear, constant, affine, or frozen
   nonpolynomial control;
5. a purported local-in-depth recursion omits a response to an earlier use of
   the same matrix or retains unbounded hidden state without declaring it;
6. the theorem tier lacks convergence in `L^1` or a separately proved
   uniform-integrability bridge.

