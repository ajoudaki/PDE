# Explicit theoretical first-layer neurons

2026-10-06. A self-contained initialization module, not a full nonlinear
training comparison. No realized dense network or dataset is an input.
The only activation considered here is tanh. This is a new author proof
within the direct-initialization study, not promoted material.

## Statement and construction

Write sphere queries as `x=sqrt(d) v`, with `||v||=1`. For a standard
Gaussian row `a` in `R^d`, the first-layer population pairing is

\[
 K(v,u)=\mathbb E[\tanh(a^Tv)\tanh(a^Tu)].
\]

For every `0<epsilon<=1/2`, the following deterministic positive-weight
neurons approximate this pairing to error at most `epsilon`, simultaneously
for all unit `v,u`. In the construction only, put

\[
 B=2^{d+10}d/\epsilon,\qquad
 h=\min\{1,\pi^2/(4\sqrt d\log B)\},\qquad
 M=\left\lceil2\sqrt{\log B}/h\right\rceil.
\]

For every integer multi-index `j` with `|j_l|<=M`, take

\[
 a_j=hj,\qquad
 p_j=\frac{\exp(-h^2\|j\|^2/2)}
 {\displaystyle\sum_{|k_l|\le M}\exp(-h^2\|k\|^2/2)}.
\]

Thus the initial weights and positive neuron weights are explicit, and

\[
 \sup_{\|v\|=\|u\|=1}
 \left|\sum_jp_j\tanh(a_j^Tv)\tanh(a_j^Tu)-K(v,u)\right|
 \le\epsilon.
 \tag{1}
\]

There are

\[
 q=(2M+1)^d=O_d\bigl(\log(1/\epsilon)^{3d/2}\bigr)
 \tag{2}
\]

neurons. The notation `O_d` means that its constant may depend on the fixed
input dimension, not on the requested accuracy. At `epsilon=n^{-1}` this
is `O_d(log(n)^{3d/2})` neurons, generated with no width-`n` array and no
random draws. This statement concerns the first-layer initialization only.

## Proof

For fixed unit vectors `v,u`, let

\[
 F(a)=(2\pi)^{-d/2}e^{-\sum_l a_l^2/2}
              \tanh(a^Tv)\tanh(a^Tu).
\]

The squares in the complex extension are algebraic squares. Set
`rho=pi/(8 sqrt(d))` within this proof. If every `|Im a_l|<=rho`,
then `|Im(a^Tv)|<=rho ||v||_1<=pi/8`, and likewise for `u`.
For real `s,t`,

\[
 |\tanh(s+it)|^2
 =\frac{\sinh^2s+\sin^2t}{\sinh^2s+\cos^2t}\le1
 \quad (|t|\le\pi/4).
\]

Consequently `F` is holomorphic in this closed polystrip and has
integrable Gaussian decay there. With the Fourier convention
`Fhat(xi)=integral F(a) exp(-i xi.a) da`, shift each coordinate contour
by `-i rho sign(xi_l)`. The end faces vanish by Gaussian decay, yielding

\[
 |\widehat F(\xi)|
 \le e^{d\rho^2/2}e^{-\rho\|\xi\|_1}
 <2e^{-\rho\|\xi\|_1}.
 \tag{3}
\]

For completeness, periodize `F` on a cube of side `h`. Gaussian decay
gives uniform convergence of the periodization and its derivatives; its
Fourier coefficient of integer index `k` is
`h^{-d} Fhat(2 pi k/h)`, by splitting the full-space integral into
translated cubes. Equation (3) makes this Fourier series absolutely
convergent. Evaluating at zero gives

\[
 h^d\sum_{j\in\mathbb Z^d}F(hj)
       =\sum_{k\in\mathbb Z^d}\widehat F(2\pi k/h).
\]

Since `2 pi rho/h>=log B`, (3) bounds the difference from the integral by

\[
 2\left[\left(1+\frac2{B-1}\right)^d-1\right]
 \le16d/B.
 \tag{4}
\]

Indeed `B>=2`, `2/(B-1)<=4/B`, and `4d/B<=1`, so the square bracket is
at most `exp(4d/B)-1<=8d/B`. The same bound holds for the pure Gaussian
density, with the tanh factors removed.

Next truncate the real lattice. Its one-dimensional Gaussian mass is at
most `1+h/sqrt(2 pi)<2`: compare its positive decreasing half with the
integral and keep the single origin term. The discarded one-dimensional
tail is bounded by

\[
 \frac{2h}{\sqrt{2\pi}}\sum_{j>M}e^{-h^2j^2/2}
 \le\frac2{\sqrt{2\pi}}\int_{Mh}^\infty e^{-s^2/2}\,ds
 \le e^{-(Mh)^2/2}\le B^{-2}.
\]

The penultimate inequality follows from the bound of the integral by
`exp(-(Mh)^2/2)/(Mh)` and `Mh>=1`. A union over the `d` discarded
coordinate directions therefore bounds the total omitted lattice mass
by `d 2^{d-1} B^{-2}`. The real tanh factors have modulus at most one,
so the same tail bound applies to `F`.

The raw truncated Gaussian sum and the raw truncated pairing thus differ
from their integrals by at most

\[
 16d/B+d2^{d-1}B^{-2}\le\epsilon/4.
\]

Let `Z` denote that truncated Gaussian sum and `Q` the pairing sum.
We have `|Z-1|<=epsilon/4`, `|Q-K|<=epsilon/4`, and `|K|<=1`.
Dividing by `Z` is precisely the normalization defining `p_j`. Hence

\[
 |Q/Z-K|\le\frac{|Q-K|+|K||1-Z|}{Z}
 \le\frac{\epsilon/2}{1-\epsilon/4}\le\epsilon.
\]

All bounds were uniform in `v,u`, proving (1). The definitions give
`h^{-1}=O_d(log(1/epsilon))` and
`M=O_d(log(1/epsilon)^{3/2})`, which proves (2).

## Computation, storage, and exact scope

Enumerating the grid, forming the rows, and computing and normalizing the
positive weights uses `O(dq)` exact-real arithmetic operations and `q`
exponential evaluations, plus scalar logarithms and square roots. A
two-pass enumeration avoids retaining any additional cloud. The stored
rows and weights use `dq+q` reals; the grid can alternatively be regenerated
from `d,h,M`. Evaluating one feature vector costs `O(dq)`. No population
expectation is queried: the proof certifies explicit weights.

These are real-coordinate and elementary-function counts, not a bit
complexity theorem. Approximating the displayed values numerically needs
an additional rounding-error budget. The proof gives strict slack, and
all finite sums are continuous with positive denominators, so certified
finite precision can attain any slightly larger requested tolerance.
An implementation need not decide whether a computable real is exactly
an integer: it may choose a certified rational spacing between half the
displayed `h` and `h`, then take an integer `M` above a certified upper
approximation of `2 sqrt(log B)/h`. An upper approximation of error less
than one suffices. The proof uses only the upper bound on the spacing and
the lower bound on `Mh`; these choices preserve both and change (2) by
only a dimension-dependent constant.

This is a genuine dataset-blind initialization result for the first-layer
pairing on the entire sphere. It does **not** claim preservation of the
second-layer reused Gaussian operator, hidden-layer training, the dense
initialization's realized features, or the full prediction trajectory.
Readout-only training of these features would be a different learning
procedure and would not repair that gap. Its role is to show, with a fully
explicit polylogarithmic construction, that the Gaussian integration and
selection of initial tanh rows are not inherently dense-network operations.
