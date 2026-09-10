# A rigorous angular quadrature bound for the exact cubic coefficient

Author: coordinator, 2026-09-10. Approach B, supporting the reopened sign
calculation. This is an analytic error certificate, not a coefficient sign.
It uses only the exact formulas in CUBIC_DERIVATION (14)--(19), reproduced
below as needed. The original model and teacher are unchanged.

## Statement

Assume the separately computed training clock coefficient satisfies
`|beta|<=1/10`. Put `P=sum_a |p_a|=(1+sqrt(5))/6<27/50` and

`F(alpha)=2 cos(3 alpha) [J(alpha)-beta a(alpha)]`.

For `N=256`, the full periodic equally spaced rule satisfies

\[
 \left|\chi-\frac1N\sum_{j=0}^{N-1}F(2\pi j/N)\right|<10^{-6}.
 \tag{A1}
\]

The rational calculation in `angle_error_bound.py` gives a sharper bound;
the looser displayed rational value is used by the certificate driver.
The hypothesis on beta must be checked by its independent rigorous interval,
not assumed from old numerical estimates. The proof does not differentiate
any Cholesky factor, square root of a passive conditional variance, or
inverse of a singular augmented Gram.

## Smooth Gaussian angular fields and derivative majorants

Write `phi=tanh`, `Z_alpha=N1 cos(alpha)+N2 sin(alpha)`, and
`h_alpha=phi(Z_alpha)`, where the two roots are independent standard normals.
The upper initialized Gaussian process `Y_alpha` has covariance
`E[h_alpha h_theta]`. It has derivatives in every fixed `L^p`: realize it
as an isonormal Gaussian map on the closed span of the lower `h_alpha`.
That map preserves L2 norms. The lower angular map is smooth in every
finite Lp by scalar differentiation, Gaussian moments and bounded
derivatives. Its image derivatives are centered Gaussian variables with
standard deviations `||h_alpha^(k)||_2`, uniformly in alpha. Gaussian
moments then give the claimed upper Lp differentiability by difference
quotients. This constructs the required derivative expectations without
requiring a sample-path analyticity assertion.

Let `m_r` bound `sup_real |phi^(r)|`. We use

\[
 m_0=m_1=m_2=1,\quad m_3=2,\qquad
 m_r=r!(4/3)^r\quad(r\ge4).
 \tag{A2}
\]

The first four bounds follow from `phi'=1-phi^2`,
`phi''=-2phi(1-phi^2)` and `phi'''=-2+8phi^2-6phi^4` on `|phi|<=1`.
For the others, when `|Im z|<=3/4<pi/4`,

\[
 |\tanh(x+iy)|^2=
 \frac{\sinh^2x+\sin^2y}{\sinh^2x+\cos^2y}\le1.
\]

Cauchy's integral formula on a radius-3/4 circle centered at any real x
therefore gives `r!(4/3)^r`. No pole lies in that strip.

Let `mu_j` be the following rational upper bound for `E|N|^j`:
`mu_(2s)=(2s-1)!!`, with `mu_0=1`, and
`mu_(2s+1)=(4/5)2^s s!`. Integration of the Gaussian density by parts gives
these moments with `sqrt(2/pi)` instead of `4/5` in the odd case, and
`sqrt(2/pi)<4/5`. Let `c_j` be the least integer whose square is at least
`(2j-1)!!`, so `sqrt(E|N|^(2j))<=c_j`.

Use Stirling numbers `S(k,j)` and exponential partial Bell polynomials
`B_(k,j)` only as finite nonnegative combinatorial sums. They can be
defined, avoiding any theorem import, by

\[
 S(0,0)=1,\quad S(k,j)=S(k-1,j-1)+jS(k-1,j),
\]
\[
 B_{0,0}=1,\quad B_{k,j}(v)=
 \sum_{l=1}^{k-j+1}\binom{k-1}{l-1}v_l B_{k-l,j-1}(v),
 \tag{A3}
\]

with other zero-boundary entries zero. Repeated product and chain rules
give the derivative expansion with `B_(k,j)`; this can also be proved
inductively from (A3). Every derivative of `Z_alpha` is a signed rotated
standard Gaussian. Holder's inequality bounds the L1 norm of a product
of j such variables by `mu_j` and its L2 norm by `c_j`, regardless of
their dependence. Since `B_(k,j)(1,...,1)=S(k,j)`, define

\[
 s_k=\sum_{j=1}^k m_j S(k,j)c_j\quad(k\ge1),
\]
\[
 l_r(0)=u_r(0)=m_r,\quad
 l_r(k)=\sum_{j=1}^k m_{r+j}S(k,j)\mu_j,
 \quad
 u_r(k)=\sum_{j=1}^k m_{r+j}B_{k,j}(s)\mu_j.
 \tag{A4}
\]

Then `s_k>=||h_alpha^(k)||_2`, `l_r(k)` bounds the L1 norm of the kth
angular derivative of `phi^(r)(Z_alpha)`, and `u_r(k)` bounds its upper
counterpart `phi^(r)(Y_alpha)`. For the last assertion apply Holder to
the jointly Gaussian upper derivatives with standard deviations at most
`s_k`, then apply the repeated chain rule. All orders used are at most
eight, with scalar tanh derivatives at most ten. The preceding finite
Gaussian moment bounds justify all derivative/expectation interchanges.

If two scalar functions have derivative bounds v,w, write
`(v*w)_k=sum_(j=0)^k binom(k,j) v_j w_(k-j)` for their product bound.
This notation denotes a finite convolution, not matrix multiplication.
Put `g_k=1` for a cosine of unit frequency and `t_k=3^k` for the teacher.

## Bounding the exact coefficient without hiding a matrix response

Use lower `h_i=phi(Z_i), e_i=phi'(Z_i)` and upper
`H_i=phi(Y_i), d_i=phi'(Y_i), d'_i=phi''(Y_i)`.
Here all named training fields are fixed as alpha varies. Set

\[
 S=\sum_a p_aH_a,\qquad
 M_{bj}=p_j E[d_jd_b]+\mathbf1_{j=b}E[Sd'_b],
 \qquad \mu_b=\sum_j h_jM_{bj}.
 \tag{A5}
\]

Both sums over j here are training-only. The elementary bound
`sum_j |M_bj|<=2P` implies `|mu_b|<=2P` on the lower real probability
space. Expanding the exact inverse-free formula gives `J=4F_x+(4/3)B_x`,
where

\[
\begin{aligned}
F_x={}&\sum_b p_b\{Q_{xb}E[S^2d_xd_b]
 +G_{xb}E[e_xe_b]E[S^2d_xd_b]\\
&+G_{xb}\sum_{i,j}p_iM_{bj}E[e_xe_bh_ih_j]E[d_id_x]\\
&+G_{xb}\sum_j M_{bj}E[e_xe_bh_xh_j]E[Sd'_x]\},
\end{aligned}\tag{A6}
\]

and

\[
\begin{aligned}
B_x={}&\sum_{a,b}p_ap_b\{(Q_{ab}+G_{ab}E[e_ae_b])
                         E[H_xd_aSd_b]\\
 &+G_{ab}E[e_ae_bh_x\mu_b]E[d_xd_a]
  +G_{ab}E[e_ae_bh_a\mu_b]E[H_xd'_a]\}.
\end{aligned}\tag{A7}
\]

All sums in (A6)--(A7) are over training indices. The factors involving
alpha in each expectation are exactly displayed; all other factors are
bounded in absolute value by one, P or 2P as appropriate. For example,
`Q_xb=E[h_xh_b]` has bounds `l_0`, while `E[S^2d_xd_b]` has bounds
`P^2 u_1`. Independence of lower and upper roots is not asserted for the
network; these are separate scalar expectations whose products follow
from the already derived response formula. Each is bounded separately.

The identity `e_x h_x=-phi''(Z_x)/2` improves the last term of (A6).
Termwise product differentiation and sums of absolute label weights yield

\[
 |F_x^{(k)}|\le P^3[l_0*u_1+3g*l_1*u_1+g*l_2*u_2]_k,
\]
\[
 |B_x^{(k)}|\le P^3[4u_0+2l_0*u_1]_k,
 \qquad |a_x^{(k)}|\le2P u_0(k).
 \tag{A8}
\]

Thus a bound for `sup_alpha |F^(8)(alpha)|` is the eighth entry of

\[
 t*2\left\{(27/50)^3
 \left[\tfrac{20}3 l_0*u_1+12g*l_1*u_1+4g*l_2*u_2
                         +\tfrac{16}3u_0\right]
          +2(1/10)(27/50)u_0\right\}.
 \tag{A9}
\]

Every entry and operation in (A2)--(A9) is rational. The retained producer
evaluates them using exact integer/Fraction arithmetic and asserts the
final strict rational comparison to `10^-6`.

## From derivative bounds to the periodic rule

For a 2pi-periodic C8 function with eighth derivative bounded by D, eight
integrations by parts give `|Fhat_k|<=D/|k|^8` for nonzero k. Its Fourier
series is absolutely convergent, equals F, and can be averaged termwise
over the N roots of unity. Only multiples of N survive, so the error is
at most `2 zeta(8)D/N^8`. The elementary integral comparison gives
`zeta(8)<=1+integral_1^infty x^-8 dx=8/7`. Using this slightly loose bound
and (A9) proves (A1) by the exact rational check.

Finally, reflection of both initial roots and the symmetric training
labels gives `J(-alpha)=J(alpha)` and `a(-alpha)=a(alpha)`. Oddness of
tanh and the linear readout gives `J(alpha+pi)=-J(alpha)` and the same
for a. These properties also follow directly from (A5)--(A7), by changing
the passive signs and permuting training indices under reflection. The
teacher has the same two symmetries, hence F is even and pi-periodic.
Its value at pi/2 is zero because the teacher is zero. Therefore its full
N=256 rule is exactly

\[
 \frac{2}{256}F(0)+\frac{4}{256}
                   \sum_{j=1}^{63}F(2\pi j/256).
 \tag{A10}
\]

This symmetry is used for the exact integrand, not inferred from
floating-point parity tests. Each of the 64 computed nodal values still
requires its own rigorous primitive/covariance/rounding enclosure.
