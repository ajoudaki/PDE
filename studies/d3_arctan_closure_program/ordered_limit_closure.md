# Ordered-limit audit: the `n^(-3/2)` kernel operator bound is unnecessary

The relevant order of limits is

\[
 n\longrightarrow\infty\quad\hbox{at fixed Euler mesh }h
 \qquad\hbox{and only then}\qquad h\longrightarrow0.                    \tag{1}
\]

Let `m=T/h`, which is finite during the first limit.  This changes the
required estimates substantially.  The conclusion of this note is:

\[
 \boxed{
 \|R_{n,h}\|_p\le C_Tp+n^{-1/2}C_{p,h,T}
 }                                                                      \tag{2}
\]

is sufficient.  Only `C_T` must be uniform in `h`; the remainder constant
may grow arbitrarily with `p` and the finite program length `m`.

## 1. Why the `p/n` third-kernel branch is harmless

For one source entry `e=(s,l)`, the third cavity replacement discussed in
`third_mixed_kernel_operator_audit.md` is a two-row Gaussian chaos.  The
available Hilbert--Schmidt estimate is

\[
 \|K_e\|_{\rm HS}\le {C_{p,h,T}\over n},
 \qquad
 \|K_e\|_{\rm op}\le {C_{p,h,T}\over n}.                               \tag{3}
\]

Conditional Hanson--Wright (or the corresponding decoupled-chaos moment
bound) therefore gives

\[
 \|H_e\|_p
 \le {C_{p,h,T}\over n};                                                \tag{4}
\]

for every fixed `p,h`.  The sharper `n^(-3/2)` operator bound would replace
the fixed-`p` constant in (4) by a sharp Gaussian `sqrt(p)` branch.  It does
not improve the power of `n` needed below.

The `n` source entries in one row must **not** be summed by triangle.  Couple
the original and replacement source rows entry by entry, and let
`(M_l)_(l=0)^n` be the Doob martingale obtained by revealing the entry
pairs sequentially.  Its differences `D_l=M_l-M_(l-1)` are centered and
are dominated by a single-entry replacement.  Thus

\[
 \|D_l\|_p\le {C_{p,h,T}\over n}.                                       \tag{5}
\]

Burkholder and Minkowski for the square function give

\[
\begin{split}
 \left\|\sum_{l=1}^nD_l\right\|_p
 &\le C_p\left\|
   \left(\sum_{l=1}^n\mathbb E_{l-1}|D_l|^2\right)^{1/2}
   \right\|_p\\
 &\le C_p\left(\sum_{l=1}^n\|D_l\|_p^2\right)^{1/2}
 \le {C_{p,h,T}\over\sqrt n}.                                         \tag{6}
\end{split}
\]

If one works with explicit finite-difference increments rather than their
Doob projections, write each as a centered part plus its conditional mean.
The leading entry carrier is odd and has zero conditional mean.  Gaussian
integration by parts puts one more `n^(-1/2)` entry factor in the nonlinear
mean, so

\[
 |\mathbb E_{l-1}H_{(s,l)}|
 \le {C_{p,h,T}\over n^{3/2}},
 \qquad
 \sum_{l=1}^n|\mathbb E_{l-1}H_{(s,l)}|
 \le {C_{p,h,T}\over\sqrt n}.                                         \tag{7}
\]

Equivalently, (6) absorbs these means automatically because a replacement
row and its independent copy have the same conditional law.

Thus even the crude operator branch in (3) contributes only
`C_(p,h,T)/sqrt(n)` to a whole-row replacement.  For the stronger
finite-`n` logarithmic-moment audit one obtains, for example,
`p^(3/2)/sqrt(n)`; this is already `o(p)` for `p <= c log n`.  Under (1) the
fixed-`p` statement (6) is all that is required.

## 2. A fixed-mesh sensitivity lemma

The following lemma replaces the infinite cavity hierarchy.

**Lemma.**  Fix `m<infinity` and `p<infinity`.  For the `m`-step Euler
program there is `C_(m,p,T)<infinity`, independent of `n`, such that every
state has bounded normalized `L^p` norm, and

\[
\begin{array}{ll}
 \|\partial_{g_{sl}}X_2^k\|_{L^p(\|\cdot\|_n)}
       \le C_{m,p,T}/n,&
 \left\|\left(\sum_l\|\partial_{g_{sl}}X_2^k\|_n^2\right)^{1/2}
       \right\|_p\le C_{m,p,T}/\sqrt n,\\[2mm]
 \|\partial_{g_q}\partial_{g_{sl}}X_2^k\|_{L^p}
       \le C_{m,p,T}/n^{3/2},&
 \|D(\hbox{third-kernel integrand})\|_{L^p({\rm HS})}
       \le C_{m,p,T}/n .                                                \tag{8}
\end{array}
\]

Here `g_sl` is a raw standard Gaussian, so the explicit matrix entry is
`g_sl/sqrt(n)`; `partial_(g_q)` denotes the Hilbert gradient in a whole raw
row.

**Proof.**  Induct over the finite sequence of Euler operations.  The
base derivative of `Gx` with respect to `g_sl` is

\[
 {1\over\sqrt n}e_sx_l,qquad
 \left\|{1\over\sqrt n}e_sx_l\right\|_n={|x_l|\over n}.                 \tag{9}
\]

The coordinate maps `atan` and `d=(1+z^2)^(-1)` have bounded derivatives
of every fixed order.  Differentiating a normalized outer product preserves
the displayed powers of `n`.  Multiplication by a Ginibre matrix costs its
operator norm, whose every fixed moment is bounded uniformly in `n`;
multiplication by a learned matrix costs

\[
 \|P^k\|_{\rm op}
 \le h\sum_{t<k}\|B^t\|_n\|X^t\|_n.                                   \tag{10}
\]

The right side has every fixed moment because
`|A_i^k| <= |A_i^0|+T pi/2`.  Product rules create only finitely many terms
at fixed derivative order and fixed `m`; Holder raises moment indices but
all relevant Gaussian moments are finite.  This proves the induction.
The constants can grow exponentially or worse in `m`; (1) permits this.

The same proof applies to replacement differences, using the exact divided
difference identities instead of derivatives.

## 3. One Gaussian-Sobolev step replaces all further cavities

For a fixed source entry, write the adapted off-column row sum as

\[
 S_e=\sum_{r\ne s}g_r u_{r,e},qquad
 u_{r,e}={\sigma_rC_{r,e}\over\sqrt n}.                                \tag{11}
\]

On the entry scale, `C_(r,e)=O(n^(-1))`, so

\[
 \|u_e\|_{L^p(\ell^2_r)}\le {C_{p,h,T}\over n}.                        \tag{12}
\]

The variables `u_(r,e)` need not be jointly independent of the row
Gaussians.  Use the exact Gaussian divergence identity

\[
 S_e=\delta(u_e)+\operatorname{tr}D u_e,                                \tag{13}
\]

with the convention
`delta(u)=sum_r(g_ru_r-partial_ru_r)`.  Meyer's Gaussian divergence
inequality, valid for every fixed `p>=2`, is

\[
 \|\delta(u_e)\|_p
 \le C_p\left(
       \|u_e\|_{L^p(\ell^2)}+
       \|D u_e\|_{L^p({\rm HS})}
      \right).                                                         \tag{14}
\]

The second bound in (8) gives

\[
 \|D u_e\|_{L^p({\rm HS})}le {C_{p,h,T}\over n}.                     \tag{15}
\]

The trace in (13) is precisely the diagonal/Stein (same-column) term.
Its invariant part belongs to the exact leading recurrence; every cavity
replacement part has the extra entry factor and is also
`C_(p,h,T)/n`.  Therefore

\[
 \|S_e^{\rm error}\|_p\le {C_{p,h,T}\over n}.                          \tag{16}
\]

This uses only the Hilbert--Schmidt scale of the third mixed derivative.
It does not require `||K_e||_op=O(n^(-3/2))`, a fourth cavity, or an
all-orders cavity expansion.  The response obstruction prevents (15) from
being uniform in `h`, but fixed `h` is enough in (1).

## 4. Time summation and the exact recurrence

At fixed `h`, there are `m=T/h` updates.  Hence (6) and (16), summed through
all causal propagators and all update times, give

\[
 \|E_{n,h}^{\rm cav}\|_p
 \le {C_{p,h,T}\over\sqrt n}.                                          \tag{17}
\]

No time square-function gain is asserted.  A triangle over the finite
program is legitimate, and all losses are absorbed in `C_(p,h,T)`.

Separate the predictor/response coordinate into

\[
 R_{n,h}=R_{n,h}^{\rm lead}+E_{n,h}^{\rm cav}.                          \tag{18}
\]

The leading object consists of the jointly row-summed fresh Gaussian
series and the exact diagonal/Onsager corrections.  The Abel identity

\[
 h\sum_{k<m}T_{k+1}F_3^k=T_mb_m-T_1b_0                                \tag{19}
\]

and the exact gate/learned-row cancellation apply to this object before
absolute values.  If the resulting same-column leading recurrence is
bounded by

\[
 \|R_{n,h}^{\rm lead}\|_p\le C_Tp                                    \tag{20}
\]

with `C_T` independent of `h`, then (17)--(20) prove (2).  In particular,
none of the off-column mixed-kernel errors has to retain the sharp
`sqrt(p)` scale; any fixed polynomial in `p` multiplying `n^(-alpha)` is
irrelevant under (1).

## 5. Passing through the ordered limits

Let `R_h` be the fixed-mesh tensor-program limit.  Fixed-mesh convergence
and lower semicontinuity of `L^p` give, from (2),

\[
 \|R_h\|_p
 \le\liminf_{n\to\infty}\|R_{n,h}\|_p
 \le C_Tp,                                                            \tag{21}
\]

and the right side is uniform in `h`.  If `R_h` converges along the Euler
limit to `R`, another Fatou/lower-semicontinuity step gives

\[
 \|R\|_p\le C_Tp                                                       \tag{22}
\]

for every fixed integer `p>=1`.  Taking the limits separately for each
`p` is legitimate: the limiting law is the same, and no simultaneous
`p,n,h` estimate is needed.

Finally, (22) implies a uniform subexponential bound.  Indeed

\[
 \mathbb E\exp\{|R|/(2eC_T)\}
 \le 1+\sum_{k\ge1}{(C_Tk)^k\over(2eC_T)^kk!}<2,                        \tag{23}
\]

after an inessential enlargement of the numerical constant.  Thus
`||R||_(psi_1) <= C C_T`.

## 6. Verdict

The `n^(-3/2)` operator estimate is needed only for a sharp, mesh-uniform,
finite-width Gaussian RD bound.  It is not needed for the ordered TP/Euler
limit.  The `p/n` per-entry branch is square-summed over the source entries
and becomes `C_(p,h,T)/sqrt(n)`.  At fixed mesh, one Gaussian divergence
estimate plus the finite-program sensitivity lemma controls all adapted
row dependence at Hilbert--Schmidt scale; the fourth-and-higher cavity
hierarchy can be placed entirely in the vanishing remainder (17).

The only term that still requires a genuinely mesh-uniform `C_Tp` proof is
the exact row-summed/same-column leading recurrence in (20).  The mixed
kernel is no longer an obstruction under the correct quantifier order.
