# Research contract: linear growth versus uniform fifth remainder

## Frozen model and order of limits

We use the previously established width-first OMFP dynamics for the same
single-input, two-hidden-layer, scalar-output network.  At width `n`,

\[
x_j=\phi(u_j),\qquad
z_i=n^{-1/2}\sum_{j=1}^nW_{ij}x_j,\qquad
f_n=n^{-1}\sum_{i=1}^na_i\phi(z_i),
\]

with independent standard-Gaussian initialization for `u`, `W`, and `a`.
One simultaneous gradient-ascent step of size `h` is

\[
\begin{aligned}
a_i^+&=a_i+h\phi(z_i),\\
W_{ij}^+&=W_{ij}+{h\over\sqrt n}
 a_i\phi'(z_i)x_j,\\
u_j^+&=u_j+h\phi'(u_j)b_j,\\
b_j&=n^{-1/2}\sum_{i=1}^nW_{ij}a_i\phi'(z_i).
\end{aligned}
\]

For each fixed integer `s` and fixed nonzero `h`, width tends to infinity
first.  Its expected limiting output is `F_s(h)`.  Only after this limit do
we let `t` tend to infinity with `h=rho/t`.

## Quantity under test

\[
\Delta_t(h)=F_{2t}(h)-F_t(2h),\qquad
\kappa_t=[h^3]\Delta_t(h).
\]

The literal fifth Taylor coefficient is not the object under test: Euler
word combinatorics makes it a polynomial of degree at most four in `t`.
The nonlocal effective coefficient is

\[
\mathcal C_\phi(t,\rho)=
\sup_{0<|h|\le \rho/t}
{\left|\Delta_t(h)-\kappa_t h^3\right|\over |h|^5}.
\]

The conjecture to resolve is:

> For every admissible linearly growing activation, there exist
> `rho_phi>0` and `C_phi<infty` such that
> `C_phi(t,rho_phi) <= C_phi t^5` for every integer `t>=1`.

A counterexample must be one fixed activation and must show, for every
candidate local radius (or at least under the exact quantifier claimed),
that `C_phi(t,rho)/t^5` is unbounded.  Merely showing a large constant, an
order-five jet, or instability beyond a positive flow time does not count.

## Meaningful admissible class

To avoid vacuous failures in which the gradient or output is undefined, a
counterexample sought here must satisfy all of:

1. `phi` is `C^infty` and `E phi(G)^2=1`;
2. `|phi(x)| <= C_phi(1+|x|)`;
3. every Gaussian moment of every derivative needed at a fixed finite
   number of OMFP steps is finite;
4. `F_s(h)` is finite for every fixed finite `s` and all sufficiently small
   fixed `h`.

If the broad phrase “any linearly bounded activation” is read literally
without items 1, 3, and 4, it is already false for trivial reasons and does
not formulate a remainder theorem.

## Claim levels

- **Theorem:** complete width-first proof for the actual network.
- **Conditional theorem:** proof inside the established OMFP DAG whose
  finite-width identification requires an explicitly named missing bridge.
- **Mechanism evidence:** finite-width or symbolic computation only.
- **Open:** no valid proof of either the universal bound or a counterexample.

