# One-sample loss time: exact reduction and paired-Euler expansion

## 1. Convention and exact finite-width reduction

Let `f_n(theta)` be the same `q=1`, two-hidden-layer network and let

\[
 \ell_n(\theta)={1\over2}(1-f_n(\theta))^2 .
\]

Write \(g_n=n\nabla f_n\) for the feature-ascent vector field in the scaled
parameter metric.  One scaled gradient-descent step for the loss is

\[
 \theta^+=\theta-hn\nabla\ell_n(\theta)
          =\theta+h(1-f_n(\theta))g_n(\theta).             \tag{1.1}
\]

Define the potential

\[
 P_n(\theta)=f_n(\theta)-{1\over2}f_n(\theta)^2 .          \tag{1.2}
\]

Then, exactly at finite width,

\[
 n\nabla P_n=(1-f_n)g_n,
 \qquad \ell_n={1\over2}-P_n.                             \tag{1.3}
\]

Thus loss gradient descent is explicit Euler ascent for `P_n`.  This
identity is algebraic and survives any fixed-step width limit for which the
two terminal observables are uniformly integrable.

For the remainder of the note, put

\[
 E_hx=x+h\nabla P(x),\qquad
 d_t(h)=\ell(E_h^{2t}x_0)-\ell(E_{2h}^{t}x_0).             \tag{1.4}
\]

All gradients below are in the same scaled metric.

## 2. Exact continuous-time time change

Let `Theta(s)` solve feature ascent

\[
 {d\Theta\over ds}=\nabla f(\Theta),\qquad F(s)=f(\Theta(s)). \tag{2.1}
\]

If `s(t)` solves

\[
 s'(t)=1-F(s(t)),\qquad s(0)=0,                            \tag{2.2}
\]

then `theta(t)=Theta(s(t))` obeys

\[
 \dot\theta=(1-f(\theta))\nabla f(\theta)=-\nabla\ell(\theta).
                                                                    \tag{2.3}
\]

Conversely, every such loss-flow solution with nonzero residual lies on the
same feature-ascent characteristic.  If

\[
 r(t)=1-f(\theta(t)),\qquad K(t)=\|\nabla f(\theta(t))\|^2,
\]

then

\[
 r'(t)=-r(t)K(t),\qquad
 r(t)=r(0)\exp\{-\int_0^tK(u)\,du\}.                       \tag{2.4}
\]

In particular, from `r(0)=1`, the residual remains in `(0,1]` and
`0<=s(t)<=t` as long as the flow exists.  For the unhalved loss
`(1-f)^2`, replace the right side of (2.2) by `2(1-F)`.

For hard ReLU, the words “as long as the flow exists” are substantive:
attracting gate contacts can make the classical fixed-derivative vector
field noncontinuable.  The time-change identity applies to a chosen
absolutely continuous characteristic where one exists; it is not a proof of
a global ReLU characteristic or of a discrete mesh limit.  See
`RELU_COMPACT_TIME_AUDIT.md`.

## 3. Universal smooth paired expansion through cubic order

Assume in this section that `P` is `C^4` near `x_0`.  At `x_0` define

\[
 p=\nabla P,\qquad H=\nabla^2P,
\]

\[
 T_P=\langle p,Hp\rangle,qquad
 S_P=\|Hp\|^2,qquad
 U_P=D^3P[p,p,p].                                      \tag{3.1}
\]

Then, for every fixed integer `t>=1`,

\[
 \boxed{
 d_t(h)=-tT_Ph^2-{t(2t-1)\over2}(4S_P+U_P)h^3+O_t(h^4).}
                                                                    \tag{3.2}
\]

Here the remainder is only a fixed-`t` statement; (3.2) does not assert a
horizon-uniform bound.

### Proof

For a general vector field `V` and scalar observable `L`, iterating
`x^+=x+hV(x)` gives

\[
\begin{aligned}
x_N={}&x+NhV+{N\choose2}h^2V'V\\
&+h^3\left\{{N\choose3}V'^2V
+{N(N-1)(2N-1)\over12}V''[V,V]\right\}+O_N(h^4).
                                                               \tag{3.3}
\end{aligned}
\]

This follows by substituting a cubic series in
`x_{k+1}=x_k+hV(x_k)` and using

\[
 \sum_{k=0}^{N-1}k={N\choose2},\quad
 \sum_{k=0}^{N-1}{k\choose2}={N\choose3},\quad
 {1\over2}\sum_{k=0}^{N-1}k^2={N(N-1)(2N-1)\over12}.
\]

Taylor-expanding `L(x_N)` and subtracting the `N=t`, step `2h` expression
from the `N=2t`, step `h` expression gives the quadratic coefficient

\[
 t\,DL[V'V],                                               \tag{3.4}
\]

and the cubic coefficient

\[
 2t(t-1)DL[V'^2V]
 +{t(2t-1)\over2}DL[V''[V,V]]
 +2t^2D^2L[V,V'V].                                        \tag{3.5}
\]

Take \(V=\nabla P\) and \(L=\ell=1/2-P\).  Then

\[
 DL[V'V]=-T_P,\quad
 DL[V'^2V]=-S_P,\quad
 DL[V''[V,V]]=-U_P,\quad
 D^2L[V,V'V]=-S_P.                                        \tag{3.6}
\]

Equations (3.4)--(3.6) yield (3.2).

The same chronology gives a useful all-fixed-orders check.  If `P` is
smooth enough for order `m`, the coefficient of `h^m` in
\(\ell(E_h^N x_0)\) is a polynomial in \(N\) of degree at most \(m\). Its
degree-\(m\) part is the exact-flow term
\((N^m/m!)A^m\ell\), where \(A=(\nabla P)\mathbin{\cdot}\nabla\).
Therefore

\[
 [h^m]d_t(h)=[h^m]\ell(E_h^{2t}x_0)
              -2^m[h^m]\ell(E_h^t x_0)                     \tag{3.7}
\]

has degree at most `m-1` in `t`: the degree-`m` terms cancel.  Thus every
individual fixed Taylor order is `O(1/t)` after `h=T/(2t)`.  This statement
does not control the sum over all orders and hence is not a uniform
continuous-time theorem.

## 4. Formula in feature-potential invariants

At an initialization point with `f(x_0)=0`, put

\[
 g=\nabla f,\quad H_f=\nabla^2f,\quad
 K=\|g\|^2,\quad T=\langle g,H_fg\rangle,
\]

\[
 S=\|H_fg\|^2,qquad U=D^3f[g,g,g].                         \tag{4.1}
\]

Since `P=f-f^2/2`,

\[
\begin{aligned}
T_P&=T-K^2,\\
S_P&=S-2KT+K^3,\\
U_P&=U-3KT .                                               \tag{4.2}
\end{aligned}
\]

Consequently

\[
\begin{aligned}
d_t(h)={}&t(K^2-T)h^2\\
&+t(2t-1)
 \left[-2K^3+{11\over2}KT-2S-{1\over2}U\right]h^3
 +O_t(h^4).                                                \tag{4.3}
\end{aligned}
\]

For the RMS-normalized two-hidden-layer ReLU or leaky-ReLU initialization,

\[
 d_\phi=\mathbb E\phi'(G)^2=1,\qquad
 K=1+d_\phi+d_\phi^2=3.                                  \tag{4.4}
\]

Indeed, the output-weight, second-layer-weight, and first-layer-weight
blocks contribute respectively

\[
 \mathbb E\phi(Z_2)^2=1,\qquad
 \mathbb E[A^2\phi'(Z_2)^2],\mathbb E\phi(U)^2=d_\phi,
 \qquad d_\phi^2.
\]

The initialization Gaussian blocks are independent and both hidden RMS
values equal one.

The annealed within-cell value of `T` is zero by readout-sign parity.  Thus
the classical smooth part is

\[
 9t h^2-t(2t-1)(54+2S+U/2)h^3+O_t(h^4).                   \tag{4.5}
\]

For a hard kink, `S,U` in (4.5) do not include the missing Gaussian
boundary distributions, so (4.5) must not be advertised as the complete
cubic hard-ReLU coefficient.

## 5. Hard ReLU and leaky ReLU: conditional boundary term

Use

\[
 \phi_{a,b}(x)=ax_++bx_-,\qquad x_-:=\min\{x,0\},
 \qquad {a^2+b^2\over2}=1,
 \quad 0\le b<a.                                          \tag{5.1}
\]

The audited marked top-gate calculation for feature ascent gives the
candidate coefficient

\[
 D_{a,b}={3(a-b)\over4\pi\sqrt e}
 \int_{2b}^{2a}{(y-2b)(2a-y)\over(1+y^2/e)^{5/2}}\,dy,
 \qquad e={a^4+b^4\over2}.                                \tag{5.2}
\]

At `f=0`, the loss potential `P=f-f^2/2` has the same first-order gate
jump and the same two normal velocities as `f`; the loss observable is
`-P` up to a constant.  Therefore the boundary contribution changes only
its sign.  Conditional on the same fixed-step indicator-DAG identification
and marked-response intertwining required by the feature-ascent result,

\[
 \boxed{
 d_t(h)=9t h^2-tD_{a,b}h|h|+o_t(h^2).}                     \tag{5.3}
\]

For positive learning rate,

\[
 d_t(h)=t(9-D_{a,b})h^2+o_t(h^2).                          \tag{5.4}
\]

For normalized ReLU,

\[
 D_{\rm ReLU}={\sqrt2\over\pi}(1-1/\sqrt5).
\]

Also `e>=1`, so (5.2) and
`int_0^L x(L-x)dx=L^3/6` give

\[
 0<D_{a,b}\le{(a-b)^4\over\pi\sqrt e}\le {4\over\pi}<9. \tag{5.5}
\]

Thus the right-sided leading loss discrepancy is positive.  Statement
(5.3) remains conditional for the actual hard-activation width-first
network because the two indicator-valued OMFP bridges are open.

For the unhalved MSE `L=(1-f)^2` with learning rate `eta`, its update equals
the half-MSE update at `h=2eta`, and its observable is twice the half-MSE.
Hence (5.3) becomes

\[
 L_{2t}(\eta)-L_t(2\eta)
 =72t\eta^2-8tD_{a,b}\eta|\eta|+o_t(\eta^2).               \tag{5.6}
\]

## 6. What this says, and does not say, about continuous time

At a fixed physical horizon `T=2th`, every displayed paired coefficient
has the Euler scaling `O(1/t)`.  In particular, the kink term in (5.3) is

\[
 tD_{a,b}(T/(2t))^2={D_{a,b}T^2\over4t}.                  \tag{6.1}
\]

It therefore does not obstruct a continuous-time limit.  The fact that a
cubic-subtracted fifth quotient is infinite is a statement about an
over-strong fifth-order norm, not a failure of first-order Euler
consistency.

Nor does any finite expansion prove a continuous-time limit.  Its
remainder may depend super-polynomially on `t`, and a fixed-`t`
`o_t(h^2)` cannot be evaluated along `h=T/(2t)`.

Here is an exact sufficient uniform theorem.  Suppose that every fine,
coarse, and hybrid state of total time at most `T`, together with every
line segment used below, lies in a convex set on which

\[
 \|\nabla P\|\le G_T,\qquad \|\nabla^2P\|_{\rm op}\le L_T. \tag{6.2}
\]

Then

\[
 \boxed{
 |d_t(h)|\le L_TG_T^2\,t h^2e^{2L_Tt h},
 \qquad 2th\le T.}                                       \tag{6.3}
\]

Indeed,

\[
 \|E_h^2x-E_{2h}x\|
 =h\|\nabla P(x+h\nabla P(x))-\nabla P(x)\|
 \le L_TG_T h^2,                                         \tag{6.4}
\]

while `Lip(E_h)<=1+hL_T`.  A hybrid telescope through the `t` macro-steps
therefore bounds the endpoint difference by
`L_TG_Tt h^2 exp(2L_Tth)`.  Since `ell=1/2-P` is `G_T`-Lipschitz, (6.3)
follows.  At `h=T/(2t)`,

\[
 |d_t(T/(2t))|
 \le {L_TG_T^2T^2e^{L_TT}\over4t}.                        \tag{6.5}
\]

The summability of (6.5) over dyadic refinements proves dyadic Euler
convergence.

For the actual width-first hard ReLU/leaky-ReLU OMFP, (6.2) is unavailable:
the pointwise Hessian has gate jumps, and the required horizon-uniform
Gaussian-averaged crossing/response estimate for the reused connector has
not been proved.  Therefore the correct current conclusion is:

1. the candidate kink correction is compatible with, rather than hostile
   to, a continuous-time limit;
2. the continuous loss flow is exactly a residual time change of feature
   ascent;
3. the actual width-first hard-activation continuous-time limit is not
   proved or disproved by the expansion.
