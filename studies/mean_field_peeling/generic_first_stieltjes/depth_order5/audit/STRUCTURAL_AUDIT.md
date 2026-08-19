# Independent structural audit through order five

## 1. Exact arbitrary-depth feature flow

Write `M^ell=W^ell/sqrt(n)` for `2<=ell<=H`, and define the unnormalised
backward coordinates

\[
b^H=a\odot\phi'(z^H),\qquad
b^\ell=\phi'(z^\ell)\odot(M^{\ell+1})^Tb^{\ell+1}
\quad(1\leq\ell<H).
\]

Direct differentiation of the frozen model gives, before a width limit,

\[
\boxed{
\dot a=h^H,qquad
\dot M^\ell={1\over n}b^\ell(h^{\ell-1})^T,qquad
\dot z^1=Q^0b^1.}
\tag{1.1}
\]

The last factor is metric, not conventional: with the active Euclidean
first-layer coordinate `r`, `z^1=sqrt(Q0) r` and
`rdot=sqrt(Q0)b^1`, hence `zdot^1=Q0 b^1`.

For ordinary Taylor coefficients, (1.1) implies

\[
M^\ell_m={1\over mn}\sum_{p+q=m-1}
b^\ell_p(h^{\ell-1}_q)^T,
\tag{1.2}
\]

and every order-five finite-width jet can be evaluated by alternating an
exact forward convolution, exact reverse convolution, and (1.2).  The
implementation in [`finite_jets.py`](finite_jets.py) is independent of both
population compilers.

As a first-derivative normalization check, direct raw-gradient squaring gives

\[
\begin{aligned}
D_nf_n={}&{1\over n}\|h^H\|^2
 +{Q^0\over n}\|b^1\|^2\\
&+\sum_{\ell=2}^H{1\over n^2}
\|b^\ell\|^2\|h^{\ell-1}\|^2.
\end{aligned}
\tag{1.3}
\]

The moving-flow coefficient `F'(0)` and (1.3) agree seedwise.

## 2. Exact parity

Let `S` change only `a` to `-a`.  Then `f(S theta)=-f(theta)`, and orthogonality
of `S` gives

\[
(D_n^kf_n)(S\theta)=(-1)^{k+1}(D_n^kf_n)(\theta).
\]

Thus, whenever the moments exist,

\[
\boxed{\mathbb E f_n=\mathbb E D_n^2f_n=\mathbb E D_n^4f_n=0}
\]

at every finite width and every fixed depth.  This is not a compiler
cancellation.

## 3. Typed equality and transpose census

Fix one matrix layer `ell`.  Although every hidden width is numerically `n`,
neuron indices at different layers are distinct types, and different weight
matrices are independent.  A Wick delta can therefore connect only two uses
of the same `M^ell` with compatible orientation.

At time coefficient `k`, a forward multiplication by `M^ell_0` has exactly:

1. one all-free same-orientation sector, a fresh forward Gaussian;
2. `k` opposite-orientation identifications with the earlier transpose uses
   at orders `0,...,k-1`;
3. `sum_(m=1)^k m=k(k+1)/2` literal rank-update terms from (1.2).

A transpose multiplication by `(M^ell_0)^T` at coefficient `k<=4` has:

1. one all-free transpose Gaussian;
2. `k+1` identifications with forward uses at orders `0,...,k`, including
   the same-order forward use, which is chronologically earlier;
3. `k(k+1)/2` literal transposed rank-update terms.

An additional equality of a free index of the same type loses one free sum
with no compensating normalization and is `O(1/n)`.  A numerical equality of
indices from different layer types is not a legal delta.  Hence these sectors
exhaust the leading equality partitions.

Through the terminal order, **per matrix layer**, the registry contains

- 15 forward response slots and 15 transpose response slots;
- 21 forward fresh covariances through order five;
- 15 reverse fresh covariances through order four.

For depth `H`, this is `30(H-1)` response slots and `36(H-1)` covariance
slots before zero branches or algebraically identical moment polynomials are
merged.  The readout involution forces

\[
\alpha^\ell_{ks}=\beta^\ell_{ks}=0\quad\text{if }k-s\text{ is even},
\]

and each forward/reverse covariance at orders `(k,s)` vanishes when `k+s` is
odd.  Every nonzero response is layer-local in the reused matrix but its
coefficient depends on the full earlier forward/reverse chronology.  Calling
the recurrence "local in depth" does not permit that history to be dropped.

## 4. Derivative ceiling and termination obligation

The exact finite-width moving jet needs only `phi^(0),...,phi^(5)`:
`h^ell_5` uses `phi^(5)`, while the reverse vector field is needed only
through order four and its `phi'` composition also stops at `phi^(5)`.

This alone does **not** prove that a fully one-dimensional Wick--Stein normal
form stops at derivative five.  Gaussian integration by parts can raise an
activation derivative, e.g. `E[G phi^(5)(G)]=E[phi^(6)(G)]`.  A producer must
therefore show either cancellation of every higher derivative or a different
allowed canonical atom.  The frozen-map scan is a mandatory, independent
gate; finite-width derivative counting cannot substitute for it.

## 5. Complexity nonclaim

The chronological program has `O(H)` matrix layers at fixed Taylor order, but
its deterministic state per layer contains all time cross-covariances and
responses.  Fully distributing products of those states can grow rapidly in
`H`.  Therefore:

- `O(H)` oracle transitions do not imply an `O(H)` flattened formula;
- a recurrence that stores a growing response/covariance dictionary is not a
  constant-state scalar recursion merely because its outer loop is over
  layers;
- an arbitrary-depth claim is pointwise in fixed `H` unless constants and
  state size are proved uniform.

