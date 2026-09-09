# Gaussian-Space No-Go and the Surviving Typed Scale

## Claim level

This note proves that a natural class of universal Hilbert/Fock state algebras cannot support CFPC.  The result is a machinery-level negative theorem, not a negative result about the network limit.  It forces a typed symbolic calculus.

## 1. Exact Hermite coefficients of arctangent

Let `Z` be standard Gaussian and let

\[
h_q(x)=\frac{\operatorname{He}_q(x)}{\sqrt{q!}}
\]

be the normalized probabilists-Hermite basis.  Define

\[
c_q=\mathbb E[\arctan(Z)h_q(Z)].
\]

Gaussian integration by parts gives

\[
c_q=\frac{\mathbb E[\arctan^{(q)}(Z)]}{\sqrt{q!}}.
\tag{1}
\]

Since

\[
\frac1{1+x^2}=\int_0^\infty e^{-t}\cos(tx)\,dt,
\tag{2}
\]

parity and differentiation under the integral yield

\[
c_{2m}=0,
\]

\[
c_{2m+1}
=\frac{(-1)^m}{\sqrt{(2m+1)!}}
\int_0^\infty t^{2m}e^{-t-t^2/2}\,dt.
\tag{3}
\]

This identity is exact.

## 2. Root-exponential asymptotic

Put `k=2m` and

\[
I_k=\int_0^\infty
\exp\left(k\log t-t-\frac{t^2}{2}\right)dt.
\]

The unique saddle is

\[
r_k=\frac{\sqrt{1+4k}-1}{2},
\qquad r_k^2+r_k=k.
\]

At the saddle,

\[
k\log r_k-r_k-\frac{r_k^2}{2}
=\frac{k}{2}(\log k-1)-\sqrt{k}+\frac14+O(k^{-1/2}),
\]

and the second derivative tends to `-2`.  Laplace's method therefore gives

\[
I_k
\sim
\sqrt\pi\,
\exp\left[
\frac{k}{2}(\log k-1)-\sqrt{k}+\frac14
\right].
\tag{4}
\]

Stirling's formula in (3) now gives, along odd `q`,

\[
|c_q|
\sim
Cq^{-3/4}e^{-\sqrt q},
\qquad
C=e^{1/4}\left(\frac\pi2\right)^{1/4}.
\tag{5}
\]

Equivalently,

\[
\log|c_q|+\sqrt q+\frac34\log q
\longrightarrow
\frac14+\frac14\log\frac\pi2.
\tag{6}
\]

For `d(x)=(1+x^2)^{-1}`, its even coefficient `b_k` satisfies

\[
b_k=\sqrt{k+1}\,c_{k+1},
\]

and hence

\[
|b_k|\sim Ck^{-1/4}e^{-\sqrt k}.
\tag{7}
\]

This agrees with the rigorous strip-analytic Hermite estimates of Wang and Zhang, who prove root-exponential convergence and analyze rational functions with poles off the real axis in [Convergence analysis of Hermite approximations for analytic functions](https://arxiv.org/html/2312.07940v3#S3.SS1).

## 3. Consequence for Malliavin weights

Let `J_qF` denote the order-`q` Wiener-chaos projection.  The identity

\[
\mathbb E\|D^kF\|^2
=\sum_{q\ge k}(q)_k\|J_qF\|_2^2
\tag{8}
\]

shows a crucial distinction between two derivative-generating norms.

The norm

\[
\sum_{k\ge0}\frac{a^k}{k!}\mathbb E\|D^kF\|^2
=\sum_q(1+a)^q\|J_qF\|_2^2
\]

has an exponential chaos weight and excludes arctangent for every `a>0`.

In contrast,

\[
\sum_{k\ge0}\frac{r^{2k}}{(k!)^2}\mathbb E\|D^kF\|^2
=\sum_qL_q(-r^2)\|J_qF\|_2^2,
\tag{9}
\]

and the Laguerre weight grows on the root-exponential scale.  This is the Hilbert counterpart of an `l^1` factorial response-jet norm.  Such a norm may contain arctangent for a finite radius; it is not an exponentially weighted chaos norm.

## 4. No multiplication-closed diagonal Hilbert norm

The obstruction is stronger than the failure of exponential weights.

Suppose

\[
\|F\|_W^2=\sum_{q\ge0}W_q\|J_qF\|_2^2,
\qquad W_q\ge1,
\tag{10}
\]

and suppose ordinary pointwise multiplication were bounded:

\[
\|FG\|_W\le C\|F\|_W\|G\|_W.
\tag{11}
\]

The top-chaos term in the exact Hermite product is

\[
h_m^2
=\frac{\sqrt{(2m)!}}{m!}h_{2m}+\text{lower chaoses},
\]

where

\[
\frac{\sqrt{(2m)!}}{m!}
\sim\frac{2^m}{(\pi m)^{1/4}}.
\tag{12}
\]

Apply (11) to `h_m/sqrt(W_m)`.  The order-`2m` component forces

\[
\frac{\sqrt{(2m)!}}{m!}\sqrt{W_{2m}}
\le CW_m.
\tag{13}
\]

Writing `a_m=log W_m`, (13) implies

\[
\frac{a_{2m}}{2m}
\le
\frac{a_m}{m}-\log2+o(1).
\]

Iteration along `m,2m,4m,...` makes the left side eventually negative, contradicting `W_q>=1`.  Thus no diagonal Hilbert chaos norm that dominates `L^2` can be an algebra under ordinary multiplication.

In particular, moving from exponential to root-exponential weights does not repair the problem.

## 5. A separate normalized-energy obstruction

Normalized coordinate energy alone is also not an algebra.  If

\[
x=y=\sqrt n\,e_1,
\]

then

\[
\|x\|_{2,n}=\|y\|_{2,n}=1,
\qquad
\|x\odot y\|_{2,n}=\sqrt n.
\tag{14}
\]

This counterexample is deterministic and does not involve Gaussian dependence.

## 6. What survives

The network does not use arbitrary products of arbitrary energy fields.  Its grammar distinguishes:

- bounded activation/gate multipliers;
- unbounded energy vectors;
- immutable Gaussian source morphisms;
- learned nuclear/rank-one morphisms;
- scalar normalized contractions;
- marked response objects.

The following rules remain dimensionally plausible:

\[
\text{bounded multiplier}\odot\text{energy}
\longrightarrow\text{energy},
\]

\[
\text{energy}\times\text{energy}
\longrightarrow\text{scalar contraction or normalized rank-one map},
\]

but not arbitrary `energy odot energy -> energy`.

Moreover, MFP can retain `arctan`, `d`, and their derivatives as primitive coordinate nodes.  It need not expand them in Hermite chaos before applying network products.  A projective syntax norm may therefore be multiplication-stable even though a universal Hilbert chaos norm is impossible.

The revised machinery target is consequently precise:

> prove that the restricted typed network grammar preserves a response/tail certificate, without embedding all Gaussian functionals into one multiplication algebra.

That theorem remains open.  The no-go result prevents the program from pursuing a provably impossible ambient space.
