# Independent three-input geometry audit and separation-dependent excursion bound

Date: 2026-09-08. Theory only. No earlier proof files were edited and no experiments were run.

## Scope verdict

The current three-input notes prove a sharp initialization scale
`lambda_min Q_1(0) = Theta(theta^2 delta^2)` in the worst case, for
`0 < theta <= 1/2`, `0 < delta <= 1/4`, and fixed input dimension at least two.
They do **not** establish a positive sufficient amplitude cutoff for the full
original three-hidden-layer population/GF/raw-GD theorem. In particular,
none of `theta <= c delta^p`, `theta <= exp(-C delta^-p)`, or a constant
positive theta is currently supplied by those notes as a theorem for the
full three-input class. This is a proof gap, not a disproof of those choices.

The initialization scale cannot be reinterpreted as a necessary or
sufficient scaling law for theta. The desired theorem includes construction
and uniqueness of the uncut strong population trajectory, source tails and
cap removal, restart, trained-law nonaffinity, and the original full
observable limits. Positive initialization alone proves none of those
continuation requirements.

## A new necessary excursion bound containing delta

Work in the original canonical raw model, with activation
`phi(z) = a z + e atan(z)`, where `a = 1-e`, `0 < e <= 1/2`.
For `0 < delta <= 1/4`, let `c = 1-delta`, `s = sqrt(1-c^2)`, and choose

\[
 u_+=(c,s),\qquad u_0=(1,0),\qquad u_-=(c,-s),
 \qquad y=(1,-1,1).
\]

The normalized inputs are `x_i = sqrt(d) u_i`, embedded in any `d >= 2`.
Their pairwise absolute cosines satisfy the requested closed condition:
`c = 1-delta`, and `2c^2-1 = 1-4delta+2delta^2` lies between zero and c.
The vector `v=(1,-2c,1)` satisfies `sum_i v_i u_i=0` and
`v^T y = ||v||_1 = 2+2c`.

At any raw parameter state, write

\[
 N=\|\sqrt d\,w:\mathbb R^d\to H_1\|_{\rm op},\quad
 A_*=\|A\|,\quad B_*=\|B\|,\quad C_*=\|C\|_2.
\]

The notation for the first map means
`q -> sqrt(d) w . q`. Its initialized operator norm is exactly one:
its first Gaussian coordinates have identity covariance. The learned
increment operator norm is bounded by its raw Hilbert norm.

Since `0 < phi'(z) <= 1`, this activation acts as a 1-Lipschitz map on
all the actual neuron L2 spaces. Since
`||u_+-u_0|| = ||u_--u_0|| = sqrt(2delta)`, the preactivation differences obey

\[
 \|z_\pm^\ell-z_0^\ell\|_2
 \le \sqrt{2\delta}\,P_\ell,
 \qquad
 (P_1,P_2,P_3)=(N,A_*N,B_*A_*N).
\]

Set `T_l = atan z_+^l - 2c atan z_0^l + atan z_-^l`.
Adding and subtracting `2 atan z_0^l`, using the Lipschitz constant one
and `|atan| <= pi/2`, gives the all-state estimate

\[
 \|T_\ell\|_2\le2\sqrt{2\delta}\,P_\ell+\pi\delta.
 \tag{1}
\]

The exact Gram-null telescoping identity from the earlier note is

\[
 S_3:=\sum_i v_i h_i^3
 =e(a^2BAT_1+aBT_2+T_3).
\]

Consequently, without any trajectory assumption,

\[
 |v^Tf|
 \le e C_*\left[
 6\sqrt{2\delta}\,B_*A_*N
 +\pi\delta(1+B_*+B_*A_*)\right].
 \tag{2}
\]

Indeed, the three first terms are bounded by
`2 sqrt(2delta) BAN (a^2+a+1) <= 6 sqrt(2delta) BAN`.
The remaining terms use `a <= 1`.

Suppose now that the state is at raw Hilbert distance R from canonical
initialization, with `C(0)=0` and `||A(0)||,||B(0)|| <= 10`. Then

\[
 C_*\le R,\qquad N\le1+R,\qquad A_*,B_*\le10+R.
\]

Writing `U=11+R >= 11` in (2) gives

\[
 |v^Tf|
 \le \left(6\sqrt2+\frac{3\pi}{11}\right)e\sqrt\delta\,U^4
 <10e\sqrt\delta\,U^4.
 \tag{3}
\]

Here `delta <= sqrt(delta)`, `R <= U`, and
`1+B_*+B_*A_* <= 3U^2` suffice for the second summand.
If the squared loss is at most `3/8`, then `||r||_2 <= sqrt(3)/2`, and

\[
 v^Tf\ge2+2c-\|v\|_2\|r\|_2
 \ge\frac72-\frac{\sqrt{18}}2>1.
\]

Therefore every such fitted state satisfies

\[
 \boxed{\quad
 R> (10e\sqrt\delta)^{-1/4}-11.
 \quad} \tag{4}
\]

The strict sign is harmless; the weak lower bound also follows.
This strengthens the prior geometry-free excursion diagnostic with an
explicit small-separation dependence. It is a necessary state-size bound,
not a sufficient training theorem, and no sharpness claim is made for its
joint powers of e and delta.

If an uncut strong gradient flow with the original energy identity reaches
that loss at time T, then its path length satisfies
`R <= sqrt(T(L(0)-L(T))) <= sqrt(3T/2)`. Thus (4) also gives the conditional
necessary fitting-time estimate

\[
 T\ge\frac23\left[(10e\sqrt\delta)^{-1/4}-11\right]_+^2.
 \tag{5}
\]

For the strictly separated class, choose `c=1-2delta`, as in the previous
geometry note. For `delta <= 1/8`, the same proof applies with the actual
small-angle parameter `2delta`; this changes only the absolute constant
in (4), from 10 to `10 sqrt(2)`.

## The earlier e-only obstruction remains separately relevant

The equilateral triple, allowed for every `delta <= 1/2`, obeys the earlier
stronger e-power lower bound

\[
 R\ge(\pi e)^{-1/3}-11
\]

at loss at most `3/8`. Thus a state-size estimate claimed uniformly over
all admissible triples must accommodate both the equilateral example and
(4). In orders, the worst required radius is at least

\[
 \max\{e^{-1/3},\ (e\sqrt\delta)^{-1/4}\}
\]

up to constants and an additive initialization constant. This expression
is not an all-state upper bound and has not been proved sharp.
For a proposed amplitude `e ~ delta^p`, these necessary excursion powers
are respectively `delta^{-p/3}` and `delta^{-(p/4+1/8)}`.
Neither inequality forbids such an amplitude: the target theorem permits
its trajectory and time constants to depend on delta and e.

## Why one cannot simply retain a delta-sized first-layer Taylor remainder on raw L2 balls

At Gaussian initialization the near-collinear Gram-null first-layer
arctangent combination has L2 norm `O(delta)` by its bounded second
derivative and Gaussian fourth moments. That rate is not uniform on a
fixed-radius raw L2 neighborhood of the initialization.

Here is a precise diagnostic. In a two-dimensional first Gaussian root
write the initialized projected weight map as `(G_1,G_2)`. Let
`c=1-delta`, `s=sqrt(1-c^2)`. Choose a measurable event E_delta, contained
in `{|G_1| <= 1, |G_2| <= 1}`, of probability delta; this is possible for
all sufficiently small delta because that rectangle has positive
non-atomic Gaussian probability. On E_delta replace the projected
coefficients `(G_1,G_2)` by `(1,1/s)` and leave them unchanged outside it.
The raw squared norm of the change is bounded by

\[
 \delta\{4+(1+1/s)^2\}=O(1),
\]

uniformly as `delta -> 0`. On E_delta the first-layer Gram-null
arctangent combination is exactly

\[
 \arctan(c+1)+\arctan(c-1)-2c\arctan(1)
 \longrightarrow\arctan(2)-\pi/2\ne0.
\]

Its L2 norm is therefore at least `c_0 sqrt(delta)` for a fixed
`c_0>0` and all sufficiently small delta. This demonstrates why a
source-tail or stronger moment argument is needed to transport the
initial `delta` finite-difference scale along arbitrary raw L2 states.
It does not exhibit degeneration of the Gram or a bad actual GF path:
it only invalidates a uniform raw-ball Taylor estimate that would
otherwise be tempting to use in a proof.

## Audited logical boundary

The statements above are algorithm-independent identities and necessary
bounds. The initial Gram lower bound remains positive for every e>0,
including singular input Grams; no exact positive-e cancellation or
counterexample to global population flow has been found.
The affine comparison fails for reasons already established in the
three-input note, and reducing e cannot repair its circular long-clock
smallness condition. A new nonlinear source/continuation argument would
be needed before a genuinely sufficient e(delta) can be claimed.
