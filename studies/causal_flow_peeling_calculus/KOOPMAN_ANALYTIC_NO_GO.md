# No Uniform Koopman--Taylor Radius with Gaussian Readout Seeds

## Claim level

This note proves that the simple analytic Koopman continuation proposed as Candidate A cannot be the CFPC completion theorem under Gaussian readout initialization.  The obstruction already occurs in a one-hidden-layer arctangent model.  It does not obstruct Picard completion, Gevrey/asymptotic expansions, bounded-seed analytic results, or a typed tail/influence calculus.

## 1. The scalar calibration cell

Consider one coordinate of the `L=1` arctangent feature flow:

\[
\dot A=\arctan u,
\qquad
\dot u=A d(u),
\qquad
d(u)=\frac1{1+u^2},
\tag{1}
\]

with

\[
u(0)=0,
\qquad
A(0)=a.
\]

The raw coordinate kernel is

\[
\Theta(t;a)=\arctan(u(t;a))^2+A(t;a)^2d(u(t;a))^2.
\tag{2}
\]

Write its ordinary time series as

\[
\Theta(t;a)=\sum_{k\ge0}P_k(a)t^k.
\]

Because (1) has rational/analytic coefficients at real states and starts at `u=0`, each `P_k` is a polynomial in `a` of degree at most `k+2`.

## 2. Exact leading weighted degree

Define

\[
R(u)=u+\frac{u^3}{3},
\qquad
\psi=R^{-1}
\]

near zero.  Under the scaling

\[
\tau=at,
\]

the highest power of `a` freezes `A/a` at one and gives

\[
\frac{du}{d\tau}=d(u),
\qquad
u(0)=0.
\]

Hence

\[
u=\psi(\tau),
\qquad
d(u)=\psi'(\tau).
\]

The first term of (2) has no factor `a^2`; the highest weighted-degree part of the second term is therefore

\[
a^2\psi'(at)^2.
\]

If

\[
\psi'(\tau)^2=\sum_{k\ge0}h_k\tau^k,
\]

then

\[
P_k(a)=h_ka^{k+2}+\text{a polynomial of degree at most }k.
\tag{3}
\]

This is an identity of formal power series, not an asymptotic in `a`.

## 3. The leading coefficient has radius `2/3`

The critical points of `R` are `u=+/-i`.  Their images are

\[
R(i)=\frac{2i}{3},
\qquad
R(-i)=-\frac{2i}{3}.
\]

Near either critical value the inverse has a square-root branch.  Since

\[
\psi'(\tau)=\frac1{1+\psi(\tau)^2},
\]

its square has a nonremovable singularity at both critical values.  Thus its Taylor radius is exactly `2/3`, and Cauchy--Hadamard gives

\[
\limsup_{k\to\infty}|h_k|^{1/k}=\frac32.
\tag{4}
\]

Only even coefficients occur, but (4) holds along that subsequence.

## 4. Gaussian coefficient norms have zero time radius

Now let `a~N(0,1)`.  The monic probabilists-Hermite polynomial `He_{k+2}` is orthogonal to every polynomial of degree at most `k+1`.  Equation (3) therefore gives

\[
\mathbb E[P_k(a)\operatorname{He}_{k+2}(a)]
=h_k(k+2)!.
\]

Projection onto the normalized Hermite mode yields

\[
\|P_k\|_{L^2(\gamma)}
\ge |h_k|\sqrt{(k+2)!}.
\tag{5}
\]

Combining (4), (5), and Stirling,

\[
\limsup_{k\to\infty}
\frac{\|P_k\|_2^{1/k}}{\sqrt k}
\ge\frac{3}{2\sqrt e}>0.
\tag{6}
\]

Thus the `L^2` coefficient roots are unbounded.

The same is true in `L^1`.  For a Gaussian polynomial `P` of degree at most `d`, hypercontractivity with `q=3/2` gives

\[
\|P\|_2\le2^{d/2}\|P\|_{3/2}.
\]

Interpolation gives

\[
\|P\|_{3/2}\le\|P\|_1^{1/3}\|P\|_2^{2/3},
\]

and hence

\[
\|P\|_1\ge2^{-3d/2}\|P\|_2.
\tag{7}
\]

The exponential factor in (7) changes only the constant in the `k`-th root.  Equations (6)--(7) imply

\[
\limsup_k\|P_k\|_1^{1/k}=\infty.
\tag{8}
\]

Therefore a bound of the form

\[
\sup_k
\left(
\mathbb E|\mathscr L^k\Theta(Y_0)|/k!
\right)^{1/k}<\infty
\]

is false under Gaussian readout seeds, already at `L=1`.

## 5. Preregistered numerical check

The exact scalar power-series compiler was evaluated by Gauss--Hermite quadrature at orders 256 and 384 through time order 80.  The two quadratures agreed through the full range, the gradient identity `(k+1)f_{k+1}=Theta_k` held to `9e-16`, and the extracted leading polynomial coefficient agreed with the independent inverse-series value.

At even orders 20, 40, 60, and 80, the signed-mean coefficient roots were respectively

\[
4.74,\quad6.32,\quad7.55,\quad8.60,
\]

while the `L^2` roots were

\[
6.90,\quad9.06,\quad10.78,\quad12.24.
\]

The leading-coefficient roots approached `1.5` as predicted.  The computation is not needed for (6)--(8), but it validates the formal-series implementation and shows that even the signed deterministic expectation exhibits the Gevrey, nonanalytic growth in this cell.

## 6. Strategic consequence

The following route is rejected:

> evaluate every time derivative statically at initialization, prove a width-uniform positive Taylor radius, and cover compact time by finitely many analytic restart blocks.

The failure is caused by unbounded Gaussian seed velocities, not by transpose reuse.  Bounded readout initialization can still admit an analytic radius, but changing the target initialization solely for this purpose would not resolve the stated contract.

The surviving completion mechanisms are:

1. uniform Picard approximation in a nonanalytic stability/Osgood metric;
2. clipped-flow approximation followed by a proved reachable-tail limit;
3. a typed response/influence certificate that controls precisely the network's bounded-multiplier products;
4. possibly a Gevrey summation theorem, but only if it provides a computable real-time remainder rather than a formal divergent series.

This rollback is substantial: Koopman diagrams remain useful syntax for finite derivatives and audits, but ordinary Taylor analyticity can no longer be the master compact-time estimate.
