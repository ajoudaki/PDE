# Audited resolution: what linear growth does and does not imply

Use

\[
\Delta_t(h)=F_{2t}(h)-F_t(2h),\qquad
\mathcal C_\phi(t,\rho)=
\sup_{0<|h|\le\rho/t}
\frac{|\Delta_t(h)-\kappa_t h^3|}{|h|^5}.
\]

There are two mathematically different meanings of “fifth remainder
coefficient.”  They have different answers.

## 1. The literal fifth Taylor coefficient cannot be a counterexample

Whenever the width-first fifth jet exists, autonomous Euler chronology gives

\[
[h^5]F_N(h)=\sum_{j=1}^5{N\choose j}\Theta_{5,j}.
\]

Consequently

\[
\begin{aligned}
[h^5]\Delta_t
&=\sum_{j=1}^5
 \left\{{2t\choose j}-32{t\choose j}\right\}\Theta_{5,j}
\end{aligned}
\]

is a polynomial in `t` of degree at most four: the degree-five term cancels
because `2^5=32`.  Under the established weighted `C^12` envelope,

\[
|[h^5]\Delta_t|
\le {227\over180}B_\phi^{E_{2,5}}t^4.
\]

The identity activation attains a nonzero quartic term.  Thus no activation
can have a *literal* fifth coefficient with super-`t^5` growth.  Any negative
result must concern `C_phi(t,rho)`, hence all source orders on a shrinking
nonzero interval.

## 2. Linear growth alone is not an admissibility theorem

For `c>0` and `0<eps<=1`, let

\[
\Phi(x)=3+\sqrt{1+x^2}+\varepsilon\sin(e^{cx}),
\qquad \phi={\Phi\over\|\Phi(G)\|_2}.
\]

This activation is positive, `C^infinity`, RMS normalized, and linearly
growing.  Every initialization Gaussian derivative moment is finite because

\[
|\phi^{(r)}(x)|\le C_r(1+e^{rcx}).
\]

Nevertheless, if `U,B` are independent nondegenerate centered Gaussians and

\[
U_1=U+hB\phi'(U),\qquad h\ne0,
\]

then

\[
\mathbb E|\phi'(U_1)|^2=\infty.
\]

The proof conditions on intervals on which
`cos(e^(cU))>=3/4`, integrates over `B in [1,2]`, and uses

\[
\int_0^Yq\cos^2q\,dq
={Y^2\over4}+{Y\sin2Y\over4}+{\cos2Y-1\over8}.
\]

The resulting lower series is

\[
\sum_n n^{-1}\exp\{c_1n-c_2(\log n)^2\}=\infty.
\]

Thus linear growth, smoothness, and even all initialization Gaussian
derivative moments do not guarantee a finite second fixed-step OMFP gradient.
The literal assertion “every linearly growing activation has a uniform
remainder coefficient” is therefore false before any `t`-growth comparison
can be made.  A meaningful finite-output conjecture must separately assume
fixed-schedule integrability of every adaptive derivative query.

## 3. A finite-output scalar counterexample exists

Let `T(y)=arcsin(sin y)` and

\[
\phi(x)=
{2+\sqrt{1+x^2}+\lambda T(x^3)\over
 \|2+\sqrt{1+G^2}+\lambda T(G^3)\|_2},
\qquad 0<\lambda\le1/\pi.
\]

Then `phi` is positive and linearly growing and
`|phi'(x)|>=c x^2` almost everywhere for large `|x|`.  For the exact scalar
particle ascent

\[
a_{r+1}=a_r+h\phi(z_r),\qquad
z_{r+1}=z_r+ha_r\phi'(z_r),
\qquad F_N^{sc}=\mathbb E[a_N\phi(z_N)],
\]

one has, for `h=rho/t`,

\[
F_{2t}^{sc}(h)\ge
\exp\{c_1 4^t-c_2t^2\}-c_3t,
\qquad
|F_t^{sc}(2h)|\le\exp\{c_4t3^t\}.
\]

The negative part is bounded rather than discarded: positivity of `phi`
makes `a_r` increasing, and on `{a_N<0}` all preterminal `z_r` are bounded by
`|a_0|/(mh)`.  Hence this is a genuine signed-expectation counterexample
with finite output at every fixed schedule.

## 4. The actual two-hidden-layer finite-output question remains open

The scalar theorem is not an `L=2` theorem.  At finite width the exact first
updated top preactivation is

\[
z_i^+=G_i^++h a_i\phi'(z_i)Q_n,
\qquad
G_i^+=n^{-1/2}\sum_jW_{ij}\phi(u_j^+),
\qquad
Q_n=n^{-1}\sum_j\phi(u_j)\phi(u_j^+).
\]

Although a positive activation gives `Q_n>=m^2`, the reused term `G_i^+` is
not fresh noise: `u^+` already depends on `W^T(a phi'(z))`.  In the OMFP DAG
this becomes the full signed aggregate response.  On the proposed rare-tail
corridors it can have the same scale as the explicit amplifier.  No proved
inequality prevents cancellation, and no sign-safe decomposition of the
terminal output is currently available.

Two independent searches reached the same boundary:

1. residual polynomial phases `x+lambda sin(x^p)` have finite moments at
   every fixed schedule and show violent rare-tail behavior numerically, but
   adaptive phases can concentrate near derivative zeros;
2. remote sawtooth/spike corridors can transport mass from a Gaussian shell
   at `R` to an amplifier at `S`, evading every initialization moment bound,
   but their reused-adjoint lower comparison is unproved.

Therefore neither of the following has been proved for the actual nonlinear
`q=1,L=2` network:

\[
\mathcal C_\phi(t,\rho)\le C_\phi t^5
\quad\hbox{for every fixed-schedule-integrable linearly growing }\phi,
\]

or the existence of one such activation for which

\[
\limsup_{t\to\infty}{\mathcal C_\phi(t,\rho)\over t^5}=\infty.
\]

Calling either statement a theorem would fail the reused-matrix audit.

## 5. Proven positive boundary

For every normalized affine activation, the actual width-first `L=2` OMFP
does satisfy the stronger estimate

\[
|\Delta_t(h)-\kappa_t h^3|
\le 10^9 22^{10}t^4|h|^5,
\qquad |h|\le(30976t)^{-1}.
\]

For genuinely nonlinear bounded-derivative activations, even the weaker
uniform `t^5` interval theorem still requires a horizon-uniform
moving-query/aggregate-adjoint estimate not supplied by the current OMFP
machinery.

