# Characteristic tangent and Gaussian-divergence reduction

**Date:** 23 August 2026.  This is an exact reduction, not a proof of the
middle-tail theorem.  It records the strongest common core left by the
independent column-Jacobi, row-cavity, and Gaussian-functional searches.

## 1. Gaussian divergence keeps the Onsager term

Fix a middle column (j), condition on every initial variable except

\[
 \xi=\sqrt n\,\Gamma_{2,:,j}\sim N(0,I_n),
\]

and write (B(\xi)=B_3(s;\xi)) and (J=D_\xi B).  With the Gaussian
divergence convention

\[
 \delta u=\xi^{\mathsf T}u-\operatorname{div}u,
\]

one has the exact identity

\[
 \frac1{\sqrt n}\xi^{\mathsf T}B
 =\delta(B/\sqrt n)+\frac1{\sqrt n}\operatorname{tr}J.       \tag{1.1}
\]

The second term is the same-column Onsager response; it has not been
discarded.  The finite-dimensional Meyer inequality gives, for (p\ge2),

\[
 \|\delta u\|_p\le Cp
 \left(\|\|u\|_2\|_p+\|\|Du\|_{\rm HS}\|_p\right).          \tag{1.2}
\]

It follows from (1.1), (1.2), and

\[
 |\operatorname{tr}J|\le\sqrt n\|J\|_{\rm HS}
\]

that

\[
 \left\|\frac1{\sqrt n}\xi^{\mathsf T}B\right\|_p
 \le Cp\|\|B\|_n\|_p
 +\left(1+\frac{Cp}{\sqrt n}\right)
   \|\|J\|_{\rm HS}\|_p.                                 \tag{1.3}
\]

Here (|B|_n^2=n^{-1}\sum_iB_i^2).  Since

\[
 |B_{3,i}(s)|\le |A_{0,i}|+\frac\pi2S,
\]

standard Gaussian empirical-norm estimates make the first factor in (1.3)
uniform on compact time for (p\lesssim\log n).  Therefore the concrete
sufficient statement is

\[
 \boxed{
 \sup_{s\le S,j}
 \|\|D_{\xi_j}B_3(s)\|_{\rm HS}\|_p\le C_Sp,
 \qquad 2\le p\le c_S\log n.}                            \tag{1.4}
\]

The learned part of (R_2) is already bounded.  Thus (1.4) implies the
required middle-query moment estimate.  At time zero,

\[
 D_{\xi_j}B_3(0)
 =\frac{X_{2,j}(0)}{\sqrt n}
   \operatorname{diag}\{A_0d'(Z_3(0))\},                 \tag{1.5}
\]

whose Hilbert--Schmidt norm is order one.  The normalization in (1.4) is
therefore the correct one.

## 2. Exact top characteristic cancellation

Suppress the layer index and put

\[
 z'=\alpha b+h,\qquad A'=\phi(z),\qquad
 b=A d(z),\qquad \alpha=\|x\|_n^2,                       \tag{2.1}
\]

where at the top (z=Z_3), (x=X_2), and (h=G_2X_2').  For any source
derivative (D), set

\[
 Z=Dz,\quad U=DA,\quad B=Db,\quad a=D\alpha,\quad H=Dh,
 \quad \kappa=d'/d,quad V=Z/d(z).                       \tag{2.2}
\]

Differentiating gives

\[
 Z'=ba+\alpha B+H,
 \qquad B=dU+Ad'Z.                                      \tag{2.3}
\]

Using (z'=\alpha b+h) in the derivative of (V=Z/d) yields the exact
cancellation

\[
 \boxed{
 V'=Aa+\alpha U+d^{-1}H-\kappa hV,\qquad
 U'=d^2V,}                                               \tag{2.4}
\]

and

\[
 B=dU+\kappa A d^2V.                                    \tag{2.5}
\]

The coefficient (alpha A d'), which a raw tangent Gronwall estimate
would charge through (|A_0|_\infty), cancels identically.  The remaining
rank-one term has the correctly normalized estimate

\[
 \|Aa\|_{\rm HS}
 \le2\|A\|_n\|x\|_n\|Dx\|_{\rm HS}.                    \tag{2.6}
\]

No coordinate maximum occurs in (2.6).

## 3. Middle and input identities

The middle preactivation satisfies

\[
 Z_2'=\alpha_2B_2+h_2,
 \qquad \alpha_2=\|X_1\|_n^2,
 \qquad h_2=G_1X_1'.                                   \tag{3.1}
\]

With (U_2=DR_2), (V_2=DZ_2/d(Z_2)), and the corresponding variations,
the same calculation gives

\[
 \boxed{
 V_2'=R_2D\alpha_2+\alpha_2U_2+d(Z_2)^{-1}Dh_2
       -(d'/d)(Z_2)h_2V_2.}                             \tag{3.2}
\]

Thus the local (R_2d'(Z_2)) multiplier also cancels.  Unlike the top
case, (U_2') is supplied by the coupled backward system, not by a scalar
identity.

At the input,

\[
 r=\Theta(u),\qquad \Theta'=1/d(u),qquad r'=Q_1,
\]

so the characteristic tangent is already exact:

\[
 V_1:=Du/d(u)=Dr,qquad V_1'=DQ_1.                       \tag{3.3}
\]

## 4. Complete diagonal loop erasure

More generally, suppose a tagged scalar coordinate is decomposed using its
complete instantaneous diagonal return,

\[
 z'=\varkappa b+y,qquad b=R d(z).                      \tag{4.1}
\]

If a variation has the form

\[
 \delta z'=\varkappa\{d\,\delta R+R d'\delta z\}+F,
\]

then (eta=\delta z/d(z)) satisfies

\[
 \boxed{
 \eta'=\varkappa\delta R+F/d-(d'/d)y\eta.}             \tag{4.2}
\]

This is the loop-erased form of (3.2): every contribution included in the
diagonal self-return cancels, while only the off-diagonal bath (y), the
variation of the return coefficient hidden in (F), and transported
forcing remain.

## 5. The remaining leverage lemma

Equations (2.4)--(3.3) reduce (1.4) to weighted row overlaps such as

\[
 \sum_i h_i^2\|V_{i\bullet}\|_2^2                       \tag{5.1}
\]

and the analogous term involving (d^{-1}Dh).  Separate normalized
(L^2) bounds do not control (5.1): the transport field and tangent energy
may concentrate on the same row.  Exchangeability alone also permits a
common uniformly random exceptional row.

The exact probabilistic leaf needed here is row diffuseness.  A tempting
estimate is

\[
 \left\|
 \left(\sum_i|\gamma_i^{\mathsf T}v_i|^2L_i^2\right)^{1/2}
 \right\|_p
 \le C\sqrt p
 \left(\sum_i\|\|v_i\|_nL_i\|_p^2\right)^{1/2}.         \tag{5.2}
\]

This estimate is valid under a genuinely joint conditional decoupling in
which, after conditioning on one common environment, all Gaussian rows are
fresh relative to the entire family \((v_i,L_i)_i\).  It is **false** if one
assumes only that row \(\gamma_i\) is independent of its own pair
\((v_i,L_i)\): that pair may encode rare events in every other row, and a
scalar leave-own-coordinate construction makes the ratio between the two
sides grow as \(\sqrt{\log n}\).  Thus (5.2) is a target consequence of a
block-decoupling theorem, not a conditional-Gaussian fact already available.

A full proof must replace each actual row by a jointly decoupled cavity
family, include the whole private block \((\gamma_i,A_{0,i})\), retain and
resum every order-one diagonal return in (4.2), and show that the square-summed
cavity remainders cost at most the second \(\sqrt p\) factor.  The fixed
network depth would then give \(Cp\); time-ordered Euler returns must sum with
their simplex weights \(h^m\binom Km\le T^m/m!\).  Factorial time ordering
alone is insufficient if each return independently costs \(\sqrt p\), since
that would sum to \(e^{C_T\sqrt p}\).

No theorem status above the conditional reduction (1.4) is claimed until
that row-leverage estimate and the nonlinear finite-difference remainder
are proved.
