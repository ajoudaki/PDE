# Finite-window test error for the original frozen-top NTH

Status: proved and internally checked continuation, 2026-10-10. The
finite-window benchmark and its consequence below do not establish a new
necessary storage exponent. No experiment, change of closure, or other study
is used. These are same-study checks, not independent promotion reviews.

## What changes, and what does not

The previous nonlinear lower bound was already a worst-over-time bound with
an early-time witness. It did not require an error at the fitted endpoint.
Restricting both sides of the comparison to a fixed finite time window does
improve the proved dense-pair benchmark from the deliberately loose
`n^(-1/64000)` to `sqrt(log(n)/n)`. It does not, by itself, improve the
necessary order from `log(n)/loglog(n)` to `log(n)` or a larger scale.

The correct finite-window comparison can nevertheless be stated entirely
in terms of a distinct passive test input, with no endpoint condition.

## Model, test input, and theorem

Use the same explicit witness as NONLINEAR_RESULT.md:

\[
f_n(v)=\frac1n u^\top W^{(2)}
       \phi(W^{(1)}v),\qquad
\phi(z)=z+\varepsilon\sin z,
\quad\varepsilon\in[1/8,1/4].
\]

There are two trained hidden layers, the second activation is the identity,
and `m=d=L=2`. The normalized training inputs are `e_1,e_2`, their labels
are `(eta,0)`, and `0<eta<=10^(-62)` is fixed independently of width.
The independent Gaussian initial weights have entry variances one and
`1/n`; the readout is zero. The loss is
`((f(e_1)-eta)^2+f(e_2)^2)/4`, with mobilities `(n,1,n)`.
The physical input is `x=sqrt(2)v`. The population final feature Gram has
gap at least `9/16`; these are the same admissibility qualifications as
before, not newly imposed finite-window restrictions.

The original order-`q` NTH copies initialized response tensors through rank
`q`, freezes rank `q`, and uses its own training residual in every lower
equation. In formulas, with `K_1=f`, `V_b=M grad f(e_b)`, and
`K_{s+1,...b}=D K_s[V_b]`,

\[
\dot K^{(q)}_{s,a_1\ldots a_s}
=\frac12\sum_{b=1}^2(y_b-f^{(q)}(e_b))
 K^{(q)}_{s+1,a_1\ldots a_s b},\quad s<q,
\qquad \dot K^{(q)}_q=0.
\]

Supply the single passive query `v=-e_1` without its label. For any fixed
`T>0`, define the two actual test-prediction discrepancies

\[
\begin{aligned}
E_n(q;T)&=\sup_{0\le t\le T}
 |f_n(t,-e_1)-f_n^{(q)}(t,-e_1)|,\\
D_n(T)&=\sup_{0\le t\le T}
 |f_n(t,-e_1)-\widetilde f_n(t,-e_1)|.
\end{aligned}
\tag{1}
\]

The tilde denotes an independently initialized dense run. Nonexistence
of the closure on the required window counts as failure; existence or
fitting after `T` is irrelevant to this definition.

**Finite-window conclusion.** For almost every one fixed activation
parameter, along `n_k=ceil(exp(k))`, with probability tending to one,
simultaneously for `2<=q<=floor(k/4)`,

\[
E_{n_k}(q;T)\ge
\exp[-C_\eta q\{\log(q+1)+\log(k+1)\}],
\qquad
D_{n_k}(T)\le C_T\sqrt{k}\,e^{-k/2}.
\tag{2}
\]

The same `C_eta` from NONLINEAR_RESULT can be used; sufficient onset may
depend on `T` and the fixed activation parameter. Neither depends on the
realized initialization. In particular, for every fixed comparison factor,
the probability that some

\[
2\le q\le\frac{k}{8C_\eta\log(k+1)}
\tag{3}
\]

matches that factor times the actual `D_{n_k}(T)` tends to zero. Increase
`C_eta` to at least one if necessary. Thus the necessary literal-array
storage remains

\[
\exp\!\left(c_\eta\frac{\log n_k}{\log\log n_k}\right).
\tag{4}
\]

This is superpolylogarithmic but subpolynomial in width. Equation (2)
is a sharper benchmark comparison, not a proof of an `Omega(n)` bound.
It is a worst-time statement: it gives a positive time within the window,
not a lower bound at every prescribed time. In particular both errors
are zero at initialization.

## Proof of the finite-window dense benchmark

The real-coordinate argument in SINE_DENSE_VARIABILITY.md establishes an
initialization event with probability at least `1-C exp(-cn)` and the
following two bounds on it:

1. For every fixed real `t` and query on the circle, its output is
   `80 exp(400t)`-Lipschitz as a function of the normalized independent
   Gaussian initial entries, which have variance `1/n`.
2. Its query output is `20000`-Lipschitz in physical time.

These statements follow from the exact transformed-state equations,
the real derivative bounds `3/4<=phi'<=5/4`, the bounded-state bootstrap,
and Gronwall. No NTH estimate or coefficient concentration is used in
this dense-pair argument. The same-study source provides their complete
derivation and the Gaussian concentration hypotheses.

Extend each fixed-time observable from the good initialization event to
the full Euclidean Gaussian space by the same-constant Lipschitz extension.
The two independent extensions have the same mean. Gaussian concentration
(Proposition 5.34 of
[Vershynin's notes](https://arxiv.org/pdf/1011.3027), rescaled to variance
`1/n`, and applied to each sign and each copy) therefore gives

\[
\Pr\{|F(t)-\widetilde F(t)|>2s\}
\le4\exp\left(-\frac{ns^2}{2(80e^{400T})^2}\right),
\qquad 0\le t\le T.
\tag{5}
\]

For clarity the extension may be chosen separately at each grid point;
no differentiability or time regularity of these extensions is assumed.
Time interpolation uses only the actual outputs on the common good event.

Let `N=ceil(nT)`, and use the `N+1` equally spaced points of `[0,T]`.
Their mesh is at most `1/n`. Apply (5) with

\[
s=80e^{400T}
\sqrt{\frac{2\log(4(N+1)/\delta)}n}.
\]

A union bound and the time Lipschitz estimate give, with probability
at least `1-delta-C exp(-cn)`,

\[
D_n(T)\le
160e^{400T}\sqrt{\frac{2\log(4(\lceil nT\rceil+1)/\delta)}n}
+\frac{40000}{n}.
\tag{6}
\]

This proof is valid for every fixed `T>0`, every `0<delta<1`, and every
integer `n>=1`; empty good events at very small widths are harmless to
the stated probability inequality. Take `delta=1/n` for `n>=2` to obtain
the second assertion of (2). The constant is allowed to depend on `T`,
but the power of `n` does not. No claim uniform in arbitrarily growing
`T` is made.

## Proof of the early-time NTH comparison

NONLINEAR_RESULT.md, equations (14)--(19), prove the first inequality
of (2) on an interval `[0,tau]`, where, locally within this proof,

\[
\begin{aligned}
j&=2\lfloor q/2\rfloor+1,\\
L_{k,q}&=(\eta/16)^j(8e k^4)^{-(j+1)},\\
\tau&=\frac{L_{k,q}^{1/(j+1)}}{64C_+B^2},\qquad
C_+\ge1,\quad B\ge1.
\end{aligned}
\]

In particular `tau<=1/(512 e k^4)` uniformly in the stated orders.
For every fixed `T>0`, these intervals lie in `[0,T]` for all sufficiently
large `k`. Both activations are odd, so all dense predictions and all
first-index query tensors at `-e_1` are the negatives of those at `e_1`.
The frozen-top equations preserve that identity with their own residual.
The proved training-input discrepancy is therefore exactly the same
discrepancy magnitude at the distinct passive query. This supplies the
first assertion of (2) with no endpoint requirement.

For (3), throughout the range in question,
`log(q+1)<=log(k+1)` and hence the lower bound in (2) is at least
`exp(-k/4)`. The upper bound for the actual dense pair is
`C_T sqrt(k) exp(-k/2)`. Their ratio tends to infinity, simultaneously
over this range of orders. The training arrays alone contain
`2^(q+1)-2` entries, or at least `2^(q-1)` if a redundant frozen odd
top is omitted. This gives (4). Query coefficients only add storage.

## Why this is not yet a stronger storage theorem

Two losses in the current NTH proof precede every long-time estimate:

- Selecting one fixed genuinely nonlinear activation by the coefficient
  sublevel argument gives `log(1/L)=O(q loglog n)`, already at time zero.
- The finite Taylor remainder has base
  `B=[C(q+1)log(en)]^C`; turning the coefficient into a real prediction
  error also costs `O(q(log q+loglog n))` in its logarithm.

Both are finite-order, early-time issues. Replacing the dense comparison
by (6) changes the available constant in front of `log n`, not those
losses. A stronger result requires a new lower bound for the *full*
nonlinear omitted coefficient and a cancellation-resistant real-error
transfer. A large individual-neuron derivative, a high Gaussian-chaos
variance, or a shrinking complex-time radius is not that result.

Two checked diagnostics make this distinction more concrete.
[FINITE_TIME_COEFFICIENT.md](FINITE_TIME_COEFFICIENT.md) constructs
degree-`q` polynomials with value one at the linear parameter and
coefficient norm at most `9^q`, for which every fixed nonlinear parameter
has infinitely many values as small as `q^(-q)`. Thus the available
parameter-polynomial information alone cannot give an eventual
`exp(-Cq)` lower bound. These polynomials are not asserted to be NTH
coefficients.
[FINITE_TIME_REMAINDER.md](FINITE_TIME_REMAINDER.md) proves that the
exact transformed scalar activation, composed with independent Gaussian
directions, has normalized vector Taylor coefficients with RMS at least
`(c sqrt(q))^q`. Merely replacing coordinate maxima by an average state
norm therefore does not supply a uniform geometric majorant. The true
flow has correlated directions and additional terms: cancellations at the
scalar prediction level remain possible. Neither diagnostic proves that
the current NTH storage lower bound is optimal.

For two tanh activations, even these growing-order lower coefficients
remain unproved. The checked fixed-order result in TANH_RESULT.md already
has a positive early-time error at orders two and three, but cannot be
extrapolated to growing order. The stronger linear-activation result is
also already early-time: it has polynomial necessary array size, but a
sublinear polynomial sufficient size on the same witness. Neither result
justifies claiming a universal `Omega(n)` bound for all instances.

There is a new, narrower positive step for two tanh activations in
[FINITE_TIME_TANH.md](FINITE_TIME_TANH.md). For two orthogonal training
inputs and fixed labels `(eta,0)`, `0<eta<=1`, it proves actual dense and
original own-residual NTH degree-`R` prediction remainders
`C(Bt)^(R+1)` on `0<=t<=1/B`, with
`B=[C_A(R+1)log(en)]^(C_A)`, simultaneously for
`2<=q<=R<=floor(log(en))`, with probability at least `1-Cn^(-A)`.
This removes the absence of a proved remainder estimate for that witness.
It does not remove the need for a noncancelling full omitted coefficient
with an adequate-probability lower bound. The transformed equations rely
on orthogonal inputs; general correlated data are not covered by this
new lemma. Root read its complete proof, and the averaged-upper author
checked its coordinate, Gaussian-moment, and actual-remainder arguments.

This continuation therefore sharpens and harmonizes the finite-time
benchmark and test-input qualification, while leaving the stronger
nonlinear storage question open.

## Check record

The generic-route author checked the complete quantitative theorem and
proof at SHA256
`1ed16f8dc3c6821247ba064816b6acd8c4ab6d049daaeb5540acee7a9e35d176`:
the fixed-time Gaussian threshold, grid and interpolation constants,
simultaneous order range, passive-query identity, and finite-window ratio
argument passed. If the good initialization event is empty at a small
width, the probability lower bound is vacuous and no extension is needed.
The present status and check paragraphs do not change those estimates.

Root read and reconstructed the complete coefficient diagnostic, including
the exact rank-two matrix-exponential counterexample to polynomial parameter
dependence at positive time. The averaged-upper author separately checked
its polynomial counterexample and limsup argument. Root and the
generic-route author read and checked the complete averaged-norm diagnostic.
These checks confirm the stated proof-route limitations, not any stronger
NTH prediction lower bound. The authoritative paper and book are unchanged.
