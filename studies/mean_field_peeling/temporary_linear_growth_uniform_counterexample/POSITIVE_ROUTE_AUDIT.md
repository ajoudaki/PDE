# Positive-route audit: fifth jet versus a uniform fifth remainder

## 1. Verdict

For the same width-first (q=1,L=2) OMFP dynamics, the following three
claims have different statuses.

1. **Exact fifth coefficient.**  For the weighted (C^{12}) activation
   class in Section 2 below,
   
   \[
   \big|[h^5]\{F_{2t}(h)-F_t(2h)\}\big|
   \le K_{\phi,2}t^4.
   \]
   
   This is proved, explicit, and stronger than (O(t^5)).

2. **Uniform interval remainder for affine activations.**  For every
   normalized affine activation, the actual width-first (L=2) network
   satisfies
   
   \[
   |\Delta_t(h)-\kappa_t h^3|
   \le C_{22}t^4|h|^5,
   \qquad |h|\le(30976t)^{-1},
   \]
   
   with (C_{22}=10^9 22^{10}).  This follows from the exact population
   Euler realization and the audited transported-defect theorem.

3. **Uniform interval remainder for genuinely nonlinear Lipschitz
   activations.**  This is not proved, even with (C^{12}), bounded
   derivatives, and at-most-linear growth.  The missing statement is a
   horizon-independent generated-core estimate for moving queries and
   aggregate reused-adjoint responses.  Replacing (t^4) by (t^5) does
   not close this analytic bridge.

Thus “globally Lipschitz and linearly growing” is not presently a valid
activation-only hypothesis for the proposed full interval theorem.

## 2. The exact fifth coefficient is quartic in time

Assume

\[
 \phi\in C^{12}(\mathbb R),\qquad \mathbb E\phi(G)^2=1,
\]

and

\[
 M_\phi=\max\left\{1,
  \sup_x\frac{|\phi(x)|}{1+|x|},
  \max_{1\le r\le12}\|\phi^{(r)}\|_\infty\right\}<\infty,
 \qquad B_\phi=\max\{4,M_\phi\}.
\]

Let

\[
 A_5(N)=[h^5]F_N(h).
\]

An order-five marked Euler word can use at most five distinct time slices.
Translation invariance of the autonomous one-step map therefore gives the
exact Newton representation

\[
 A_5(N)=\sum_{j=1}^5{N\choose j}\Theta_{5,j}(\phi,2).
\]

The five numbers (\Theta_{5,j}) are defined by the width-first singular
Price compiler at horizons (0,1,\ldots,5), so this does not interchange
width and step-size limits.  Equivalently,

\[
 A_5(N)=\sum_{d=1}^5\gamma_dN^d.
\]

For

\[
 \Delta_t(h)=F_{2t}(h)-F_t(2h),
\]

one consequently has

\[
\begin{aligned}
 [h^5]\Delta_t
 &=A_5(2t)-32A_5(t)\\
 &=\sum_{d=1}^5(2^d-32)\gamma_dt^d\\
 &=\sum_{d=1}^4(2^d-32)\gamma_dt^d.
\end{aligned}
\]

The possible fifth power cancels identically because (2^5=32).  The
audited Newton-envelope estimate is

\[
 \boxed{
 |[h^5]\Delta_t|
 \le \frac{227}{180}B_\phi^{E_{2,5}}t^4,}
\]

where (E_{2,5}) is the explicit terminating integer recursion in
`../temporary_near_identity_omfp/FIFTH_JET_POLYNOMIAL_THEOREM.md`.
Therefore the literal fifth coefficient can never be super-(t^5) in this
class; it is universally (O(t^4)), and the quartic power is attained by
the identity activation at (L=2).

This conclusion concerns the coefficient at (h=0).  It does not bound
the effective coefficient on (0<|h|\le\rho/t).

## 3. Global Lipschitzness alone is too weak

There are smooth globally Lipschitz, linearly growing functions for which
even the Gaussian moments required by the cubic and fifth Price compilers
are infinite.

Choose (\chi\in C_c^\infty((-1,1))), (0\le\chi\le1), with
(\chi'\not\equiv0).  Put

\[
 x_n=3n,\qquad w_n=e^{-n^4},
\]

and, for (0<\epsilon<1), define

\[
 g(x)=1+\epsilon\sum_{n\ge1}
 \chi\!\left(\frac{x-x_n}{w_n}\right),
 \qquad
 \Phi(x)=\int_0^xg(s)\,ds.
\]

The supports are disjoint and locally finite.  Hence (g,\Phi\) are
(C^\infty),

\[
 1\le\Phi'(x)\le1+\epsilon,
\]

and (\Phi) is globally Lipschitz.  Moreover

\[
 |\Phi(x)-x|\le2\epsilon\sum_nw_n<\infty,
\]

so it has linear growth and (0<\|\Phi(G)\|_2<\infty).  Let

\[
 \phi=\Phi/\|\Phi(G)\|_2.
\]

On a fixed subinterval (J\Subset(-1,1)) where
(|\chi'|\ge c_\chi>0),

\[
 |\phi''(x)|\ge
 \frac{\epsilon c_\chi}{\|\Phi(G)\|_2w_n},
 \qquad x\in x_n+w_nJ.
\]

The Gaussian density on this interval is at least a constant times
(e^{-(x_n+1)^2/2}).  Therefore

\[
\begin{aligned}
 \mathbb E|\phi''(G)|^2
 &\ge C\sum_{n\ge1}w_n^{-1}e^{-(x_n+1)^2/2}\\
 &=C\sum_{n\ge1}
   \exp\{n^4-(3n+1)^2/2\}=\infty.
\end{aligned}
\]

Since (\phi'\) is bounded below by a positive constant, also

\[
 \mathbb E[\phi''(G)^2\phi'(G)^2]=\infty.
\]

This is one of the standard activation moments entering the width-first
derivative compiler.  Thus smooth global Lipschitzness and linear growth do
not even supply the finite local data needed for a fifth-remainder theorem.

## 4. A complete positive interval theorem for normalized affine activations

Let

\[
 \phi(x)=\alpha x+\beta,\qquad \alpha^2+\beta^2=1.
\]

Use the fixed population Hilbert spaces (\mathcal H_1,\mathcal H_2),
unit constant vectors (e_1,e_2), and the initialized connector (W_0),
with (\|W_0\|_{\rm op}\le2).  Write the trainable population state as

\[
 \theta=(a,K,u)\in
 \mathcal H_2\oplus{\rm HS}(\mathcal H_1,\mathcal H_2)
 \oplus\mathcal H_1
\]

and use the sum norm.  The exact width-first vector field is

\[
\begin{aligned}
 x&=\alpha u+\beta e_1,\qquad W=W_0+K,\\
 y&=\alpha Wx+\beta e_2,\\
 g_a&=y,\\
 g_K&=(\alpha a)\otimes x,\\
 g_u&=\alpha^2W^*a.
\end{aligned}
\]

The observable is

\[
 f(a,K,u)=\langle a,\alpha(W_0+K)
             (\alpha u+\beta e_1)+\beta e_2\rangle.
\]

This is a polynomial map on the Hilbert/HS state space.  At initialization
(\|A\|_2=\|U\|_2=1), (K=0).  On the closed unit ball about that state,

\[
 \|a\|_2\le2,qquad \|u\|_2\le2,qquad
 \|K\|_{\rm HS}\le1,qquad \|W\|_{\rm op}\le3.
\]

Consequently

\[
 \|x\|_2\le3,\quad \|y\|_2\le10,\quad
 \|g\|\le22,\quad \|Dg\|\le16,\quad
 \|D^2g\|\le6,\quad D^3g=0.
\]

Because \(Df=g\), the derivatives of \(f\) through order four obey the
same bound \(22\).  Thus the hypotheses of the audited Banach-space
paired-Euler theorem hold with \(K=22\).  Readout reflection makes the
paired discrepancy odd.  Its cubic coefficient is the established
activation integral

\[
 \kappa_t=\frac{t(2t-1)}2J_{\phi,2},
\]

not an output-defined constant.  The theorem therefore gives

\[
 \boxed{
 |\Delta_t(h)-\kappa_t h^3|
 \le 10^9 22^{10}t^4|h|^5,
 \qquad |h|\le\frac1{64\cdot22^2t}
 =\frac1{30976t}.}
\]

This is an actual width-first OMFP theorem, not a finite-width Taylor
statement.  If (\alpha=0), the discrepancy is identically zero.

## 5. Why the affine boundary is sharp for the ambient-Hilbert proof route

Let (Z) have a density positive on every interval and suppose
(\phi\in C^2) with (\phi''\not\equiv0).  If the Nemytskii map

\[
 N_\phi:v\mapsto\phi(v)
\]

were twice Frechet differentiable from an (L^2) neighborhood of (Z)
to (L^2), its second derivative on bounded directions would be

\[
 D^2N_\phi(Z)[v,w]=\phi''(Z)vw.
\]

Choose sets (E_m\) of probabilities (p_m\downarrow0) inside an interval
where (|\phi''(Z)|\ge c>0), and put

\[
 v_m=w_m=p_m^{-1/2}\mathbf1_{E_m}.
\]

Then (\|v_m\|_2=\|w_m\|_2=1), but

\[
 \|\phi''(Z)v_mw_m\|_2\ge cp_m^{-1/2}\to\infty.
\]

Thus (N_\phi:L^2\to L^2) is not (C^2).  With continuous
(\phi''), avoiding this obstruction for every Gaussian state forces
(\phi''\equiv0), hence (\phi) affine.  Therefore affine activations are
the maximal class to which the existing ambient-Hilbert transported-defect
proof applies directly.  A nonlinear theorem requires a new intrinsic
reachable-core/aggregate-adjoint calculus.

## 6. Exact remaining proof obligation

The paired factorization

\[
 \Delta_t(h)=h^2\sum_{j=0}^{t-1}A_{j,t}(h)
\]

is exact.  Oddness and Taylor's integral formula show that a uniform bound

\[
 \sup_{j<t,\ |h|\le\rho/t}|A_{j,t}^{(3)}(h)|
 \le C_\phi t^3
\]

would imply the stronger (C_\phi t^4|h|^5) remainder.  For (L=2), the
unclosed generated terms include

\[
 a_s\phi''(z_s)\zeta_s^i,qquad
 r_s\phi''(u_s)p_s^i,
\]

their moving-query derivatives, and their aggregate (J^*,I^*) response
descendants.  Existing (L^2) energy estimates do not control the required
(L^4,L^8,\ldots) hierarchy uniformly in the horizon.  An (O(t^5))
target still requires a polynomial bound on this same hierarchy, so it is
not obtained merely by allowing one extra power of (t).
