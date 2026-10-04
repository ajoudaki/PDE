# Joint Gaussian sources and empirical neuron cubature

2026-10-03. Scoped theoretical calculation. These are internally checked
lemmas and a conditional construction, not a completed neuron-compression
theorem. No experiments or Git operations were performed.

The target is an autonomous weighted order-$q$ residual-RMS closure with
fewer neurons than the original realized width $n$, preserving the forward
and adjoint dependence of the same initialized Gaussian mixer, and satisfying

\[
 \left(\int\sup_{t\ge0}|\widetilde f_{N,q}(t,x)
       -\widehat f_{n,q}(t,x)|^2\,d\mu(x)\right)^{1/2}
 \le C_\delta n^{-1/2}
\]

with probability at least $1-\delta$. The desired moving count is
$O(Nq)$, preferably $o(n)$. The current separate history approximation
result supplied by the supervisor uses $q=n^{1/6+o(1)}$. That result
concerns the original closure and does not automatically transfer to a
weighted neuron-reduced system.

The strongest positive result obtained here is narrower: **both hidden
populations can be reduced to polylogarithmically many weighted neurons
while preserving the initial training kernel exactly and the whole-query
initial kernel to order $n^{-1/2}$**. The fixed reduced mixer is built
from the actual realization, has bounded weighted operator norm, and is
used with its true weighted adjoint. It defines an autonomous weighted
residual-RMS closure, but its all-time fidelity remains unproved. This
explicitly defeats a universal Monte Carlo lower bound for query-aware
sampling. Sections 3--4 give the top-only result and its joint-population
strengthening.

Two exact calculations identify the remaining difficulty. The first
adjoint source creates a new forward Gaussian source in the actual second
time derivative. Moreover the entire initialized query source already has
infinite Gaussian rank in the population limit. Infinite exact rank is
compatible with the positive polylogarithmic approximation just stated.

Inputs: the model and residual-clock construction in `paper/main.tex`;
complete `paper/results.tex`, `paper/proof_alltime.tex`, and
`paper/proof_tracking.tex`; `docs/index.qmd`, `docs/notation.qmd`, and the
complete conditioning sections 1, 2 and 5.4 of
`docs/02-gaussian-reuse.qmd`; the scoped status note
`NEURON_SAMPLING_ROUTE.md`; the supervisor's explicit source-space
construction checked in Section 4. No other route or study was read. The canonical
notation skill and neural reference, rigorous-math skill, and research
contract/adversarial-audit instructions were applied.

## 1. The actual closure and two successive Gaussian reveals

Write $v_a=x_a/\sqrt d$. The first matrix is
$A=W^{(1)}\in\mathbb R^{n\times d}$, the hidden mixer is
$W=W^{(2)}\in\mathbb R^{n\times n}$, and the readout is
$w\in\mathbb R^n$. Thus

\[
 h_a^{(1)}=\tanh(Av_a),\qquad z_a^{(2)}=Wh_a^{(1)},\qquad
 h_a^{(2)}=\tanh z_a^{(2)},\qquad f_a=w^\top h_a^{(2)}/n.
\]

The loss is $m^{-1}\sum_a r_a^2$, with $r_a=f_a-y_a$ and
$\rho=(m^{-1}\sum_a r_a^2)^{1/2}$. Backward responses exclude residuals:

\[
 \delta_a^{(2)}=w\odot\operatorname{sech}^2z_a^{(2)},\qquad
 \delta_a^{(1)}=\operatorname{sech}^2(Av_a)
                    \odot W^\top\delta_a^{(2)}.
\]

The first matrix and readout obey

\[
 \dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\qquad
 \dot w=-\frac2m\sum_a r_a h_a^{(2)}.
\]

The closure has $\dot\tau=\rho$, $\tau(0)=1$, forward moments
$\bar h_{a,j}^{(1)}$, backward moments $\bar\delta_{a,j}^{(2)}$, and

\[
 \widehat W=W_0-\frac2{mn\tau}\sum_{a,j<q}(2j+1)
          \bar\delta_{a,j}^{(2)}\bar h_{a,j}^{(1)\top}.
\tag{1}
\]

The moment source terms are respectively $\rho h_a^{(1)}$ and
$r_a\delta_a^{(2)}$; the dilation term on either moment $M_j$ is
$-(\rho/\tau)[jM_j+\sum_{k<j}(2k+1)M_k]$. Initially only
$\bar h_{a,0}^{(1)}=h_a^{(1)}(0)$ is nonzero. All fields in these
equations belong to this closure. Initial entries of $A_0$ and $W_0$
are independent $N(0,1)$ and $N(0,1/n)$, and $w(0)=0$.

Consider the allowed special case $m=1$, $\|v\|_2=1$, $y\ne0$.
Define the initial vectors

\[
 a=A_0v,\quad h=\tanh a,\quad z=W_0h,\quad
 u=2y\tanh z\odot\operatorname{sech}^2z,\quad k=W_0^\top u.
\]

At every $q\ge1$, the hidden velocities vanish at zero time and

\[
 \dot w(0)=2y\tanh z,\quad \dot\delta^{(2)}(0)=u,\quad
 \ddot A(0)=2y[\operatorname{sech}^2a\odot k]v^\top.
\]

Consequently the actual first feature acceleration is

\[
 v_2:=\ddot h^{(1)}(0)=2yDk,\qquad
 D=\operatorname{diag}(\operatorname{sech}^4a).
\tag{2}
\]

For completeness, differentiating (1) at zero gives
$\dot{\widehat W}(0)=0$ and
$\ddot{\widehat W}(0)=2yu h^\top/n$. Indeed each backward moment
has zero first derivative and second derivative $-yu$, while only the
zeroth forward moment is initially nonzero. Thus

\[
 \ddot z^{(2)}(0)=W_0v_2+2y\frac{\|h\|_2^2}{n}u.
\tag{3}
\]

This is an identity for the actual residual-RMS closure, including $q=1$.

Let $P_h=hh^\top/\|h\|_2^2$ and
$P_u=uu^\top/\|u\|_2^2$. Their denominators are positive almost surely.
Condition first on $A_0,z$. Gaussian projection gives

\[
 k=c_nh+\sigma_n(I-P_h)\xi,\qquad
 c_n=\frac{z^\top u}{\|h\|_2^2},\quad
 \sigma_n^2=\frac{\|u\|_2^2}{n},
\tag{4}
\]

in conditional law, with $\xi\sim N(0,I_n)$ independent of this
conditioning. After also revealing $k$, the remaining matrix law is

\[
 W_0=\frac{zh^\top}{\|h\|_2^2}
       +\frac{u k^\top(I-P_h)}{\|u\|_2^2}
       +(I-P_u)\frac{G}{\sqrt n}(I-P_h),
\tag{5}
\]

where $G$ is conditionally independent standard Gaussian. The first two
terms satisfy both $W_0h=z$ and $W_0^\top u=k$, using
$u^\top z=k^\top h$; their orthogonal Gaussian remainder preserves
both constraints. Because $v_2$ is now measurable, (5) gives

\[
 \operatorname{Cov}(W_0v_2\mid A_0,z,k)
      =\frac{\|(I-P_h)v_2\|_2^2}{n}(I-P_u).
\tag{6}
\]

This new conditional covariance is nonvanishing at large width. To see
its precise limit, put

\[
 s_h^2=\mathbb E\tanh^2G_*,\quad
 Z_*\sim N(0,s_h^2),\quad G_*\sim N(0,1),
\]

\[
 U_*=2y\tanh Z_*\operatorname{sech}^2Z_*,\quad
 \sigma^2=\mathbb E U_*^2>0,\quad
 c=\mathbb E[Z_*U_*]/s_h^2,\quad D_*=\operatorname{sech}^4G_*.
\]

Conditionally on $A_0$, the entries of $z$ are independent
$N(0,\|h\|_2^2/n)$. The bounded functions defining $u$ give
$\sigma_n^2\to\sigma^2$ and $c_n\to c$ in probability. From (4),

\[
 k_i=c_nh_i+\sigma_n\xi_i-\sigma_nh_i
                 \frac{h^\top\xi}{\|h\|_2^2}.
\]

The coefficient in the last term is $O_{\mathbb P}(n^{-1/2})$.
For every bounded function of $a_i$, the weighted averages of $\xi_i$
converge to zero and those of $\xi_i^2$ converge to the corresponding
weight average: their conditional variances are $O(1/n)$. Applying
these statements to the diagonal entries of $D,D^2$ yields

\[
 \frac{\|(I-P_h)v_2\|_2^2}{n}\longrightarrow
 4y^2\left[
 \sigma^2\mathbb ED_*^2+
 c^2\left\{\mathbb E(D_*^2\tanh^2G_*)-
       \frac{(\mathbb E[D_*\tanh^2G_*])^2}{s_h^2}\right\}
 \right].
\tag{7}
\]

The expression in braces is nonnegative by Cauchy--Schwarz. The limit
is therefore at least
$4y^2\sigma^2\mathbb E\operatorname{sech}^8G_*>0$, of order $y^4$.
The expected squared RMS of the innovation in (6) is $(1-1/n)$
times its displayed scalar variance.

**Consequence.** Appending the exact initial adjoint $k$ to initial
forward marks still does not close the actual source list: the next
forward acceleration contains a new Gaussian direction of order $y^2$.
Equations (2)--(7) do not prove a positive prediction error, an all-time
lower bound, or a growing-rank theorem for every subsequent derivative.

## 2. Whole-query source rank is already infinite at initialization

Assume $d\ge2$ and restrict queries to a great circle
$v(\theta)=(\cos\theta,\sin\theta,0,\ldots,0)$. The population initial
second-layer preactivation is a centered Gaussian field with covariance

\[
 K_1(\theta,\theta')=
 \mathbb E\left[\tanh(G_1\cos\theta+G_2\sin\theta)
                \tanh(G_1\cos\theta'+G_2\sin\theta')\right].
\tag{8}
\]

This covariance is the limit of the exact conditional finite covariance
$n^{-1}\sum_i h_i(v(\theta))h_i(v(\theta'))$. Write
$(G_1,G_2)=R(\cos\Theta,\sin\Theta)$, where $\Theta$ is uniform
and independent of $R$. For fixed $r$, the function
$\tanh(r\cos\theta)$ has a real cosine series containing only odd
modes. Each odd coefficient is nonzero as a function of $r$.

Here is an elementary verification. If
$\tanh t=\sum_{k\ge0}c_kt^{2k+1}$ near zero, the identity
$\tanh'=1-\tanh^2$ gives $c_0=1$ and

\[
 (2k+1)c_k=-\sum_{a+b=k-1}c_ac_b\qquad(k\ge1).
\]

Induction gives $(-1)^kc_k>0$. The coefficient of
$\cos((2k+1)\theta)$ in $\cos^{2k+1}\theta$ is $2^{-2k}$,
whereas lower powers have no such mode. The corresponding Fourier
coefficient of $\tanh(r\cos\theta)$ thus has leading term
$2^{-2k}c_kr^{2k+1}\ne0$. Its square has strictly positive radial
expectation because the Gaussian radial density is positive near zero.

Averaging the random phase $\Theta$ in (8) makes distinct Fourier
modes orthogonal. Every odd sine/cosine pair therefore has a positive
covariance eigenvalue. The Gaussian query field has infinite covariance
rank.

In particular it cannot be an affine function of a fixed finite list of
Gaussian sources. There is also no fixed-dimensional locally Lipschitz
source representation of all its values: infinite rank supplies
arbitrarily large nonsingular finite Gaussian value vectors. A locally
Lipschitz map from $\mathbb R^D$ into $\mathbb R^K$, $K>D$, has image
of $K$-dimensional Lebesgue measure zero. Indeed, on a bounded cube with
Lipschitz constant $L$, subdividing into $O(J^D)$ cubes of diameter
$O(J^{-1})$ covers the image by balls of total $K$-volume
$O(L^KJ^{D-K})\to0$; countably many local pieces cover the domain.
Such an image cannot support a nonsingular $K$-variate Gaussian.

This last statement imposes the regularity needed by useful geometric
quadrature. An arbitrary measurable encoding can hide countably many
random variables in one real number, so dimension alone is not a
meaningful obstruction without regularity. For $d=1$ the unit sphere
has only two points and this whole-query argument does not apply.

## 3. A positive result: polylogarithmic initial kernel cubature

Infinite exact source rank does not prevent efficient sampling of an
observable. The following finite-realization result uses the cancellation
in the actual Gaussian mixer, without replacing it by independent noise.

**Proposition.** Fix $d,m$ and $0<\delta<1$. For all sufficiently large
$n$, with probability at least $1-\delta$, the initialized top feature
functions

\[
 b_j(v)=\tanh\left(\sum_{i=1}^n(W_0)_{ji}\tanh(A_{0,i}\cdot v)\right),
 \qquad v\in[-1,1]^d,
\]

have polynomial approximants $P_j$ from one common space, of coordinate
degree at most

\[
 p\le C_d\log(en/\delta)
 \left[\log(1/\varepsilon)+d\log\log(en/\delta)+C_d\right],
\tag{9}
\]

such that $\max_j\sup_v|b_j(v)-P_j(v)|\le\varepsilon$ for every
$0<\varepsilon<1/2$. Consequently there are selected top neurons
$S$ and positive weights $\omega_j$, summing to one, with

\[
 |S|\le m(p+1)^d+1,
\]

for which every training/query initial kernel coefficient satisfies

\[
 \sup_{v\in[-1,1]^d}\max_{a\le m}
 \left|\sum_{j\in S}\omega_jb_j(v_a)b_j(v)
       -\frac1n\sum_{j=1}^n b_j(v_a)b_j(v)\right|
 \le2\varepsilon.
\tag{10}
\]

Here all $v_a$ lie in the box, as sphere-normalized inputs do. The
weights and selected neurons depend only on the actual initialization.

*Proof of the common approximation space.* Put
$\Lambda_n=\log(en/\delta)$. With probability at least $1-\delta/3$,

\[
 \max_i\|A_{0,i}\|_1\le R=C_d\sqrt{\Lambda_n},
 \qquad\|W_0\|_{\rm op}\le K
\tag{11}
\]

for a fixed $K$ and all sufficiently large $n$ depending on $\delta$.
The first event follows from Gaussian scalar tails and a union bound
over $nd$ entries. The second follows from the two-sphere-net Gaussian
bound stated and proved in `paper/proof_alltime.tex`.

Parametrize the box by $v_k=\cos\theta_k$. Extend each $\theta_k$
to the complex strip $|\operatorname{Im}\theta_k|\le s_0=c/R$,
with a sufficiently small fixed $c>0$. For $s_0\le1$,

\[
 |\operatorname{Im}(A_{0,i}\cdot\cos\theta)|
 \le R\sinh(s_0)\le2c.
\]

Choose $2c<\pi/8$. On $|\operatorname{Im}z|\le\pi/8$,
$|\tanh z|\le1$ and $|\operatorname{sech}^2z|\le2$; these follow
from $|\cosh(x+iy)|^2=\sinh^2x+\cos^2y$. Thus all first features
are analytic and bounded by one on this strip, and their coordinate
derivatives have magnitude at most $C R$.

Define the analytic initial top preactivation

\[
 z_j(\theta)=\sum_i(W_0)_{ji}\tanh(A_{0,i}\cdot\cos\theta).
\]

At each fixed complex $\theta$, conditional on $A_0$, its real and
imaginary parts are centered real Gaussians of variance at most one.
On the operator event in (11), its derivative in each coordinate is
bounded deterministically by

\[
 |\partial_{\theta_k}z_j|\le
 \|(W_0)_{j,:}\|_2
 \left(\sum_i|\partial_{\theta_k}h_i|^2\right)^{1/2}
 \le CK R\sqrt n.
\]

Cover the compact complex strip with real parts in $[0,2\pi]^d$
by a net of mesh $(nR)^{-1}$ in its $2d$ real coordinates. The net
has at most $(C nR)^{2d}$ points. Gaussian tails and a union bound
over these points and all $j$ show, with additional failure probability
at most $\delta/3$, that $|z_j|\le M=C_d\sqrt{\Lambda_n}$ on the net.
The derivative bound extends this to the whole strip, after increasing
$M$ by a constant: the interpolation error is at most $C_d/\sqrt n$.
No coordinate independence after training is used; these are
initialization-only Gaussian linear forms.

Cauchy's formula on the inner half-strip now gives
$|\partial_{\theta_k}z_j|\le C M/s_0$. Because $z_j$ is real
for real $\theta$, on the narrower strip

\[
 |\operatorname{Im}\theta_k|\le s_1=\frac{c' s_0}{dM}
\]

we have $|\operatorname{Im}z_j|\le\pi/8$, taking $c'$ sufficiently
small. Thus $b_j(\cos\theta)=\tanh z_j(\theta)$ is analytic and
bounded by one on this common strip. Notice that
$s_1^{-1}\le C_d RM\le C_d\Lambda_n$.

For a bounded $2\pi$-periodic function analytic in this product strip,
shifting the contour in each Fourier integral gives the coefficient
bound $|\widehat b_j(k)|\le e^{-s_1\|k\|_1}$. Truncating to
$|k_r|\le p$ therefore has uniform error at most

\[
 C_d s_1^{-d}e^{-s_1p}.
\]

Indeed sum the geometric series and union-bound the $d$ coordinates
whose frequency exceeds $p$. The function is even in each $\theta_k$
and real on the real torus. Its truncated series is consequently a real
polynomial in $v_k=\cos\theta_k$, with coordinate degree at most $p$
and at most $(p+1)^d$ tensor Chebyshev coefficients. Choosing $p$ to
make the preceding bound at most $\varepsilon$ proves (9).

*Proof of the empirical cubature.* Write the coefficients of $P_j$ in
that common basis as $c_{j,k}$, $1\le k\le(p+1)^d$. Associate to
neuron $j$ the real vector with entries
$b_j(v_a)c_{j,k}$, for all $a,k$. Its empirical mean is in the convex
hull of these $n$ vectors. It has a representation by at most
$m(p+1)^d+1$ vectors with nonnegative weights summing to one.

For a self-contained proof of this last fact, start with the uniform
weights. If more than $D+1$ positive weights remain for vectors in
$\mathbb R^D$, their augmented vectors $(1,\Phi_j)$ are linearly
dependent. Choose coefficients $c_j$, not all zero, with
$\sum c_j=0$ and $\sum c_j\Phi_j=0$. Vary the weights by
$-t c_j$, choosing the first positive $t$ for which one becomes zero.
No weight becomes negative, and their sum and all moments are preserved.
Repeat until at most $D+1$ remain; discard zero weights.

For the resulting weights, the kernel coefficients with $P_j(v)$
in place of $b_j(v)$ agree exactly for every $v$. Returning to $b_j$
costs at most $\varepsilon$ in each of the two positive averages,
since $|b_j(v_a)|\le1$. This proves (10).

At zero readout the initial prediction velocity of every closure order is

\[
 \dot f(0,v)=\frac2m\sum_a y_a K_n(v,v_a),\qquad
 K_n(v,v_a)=\frac1n\sum_j b_j(v)b_j(v_a).
\]

The cubature velocity therefore has uniform error at most $4Y\varepsilon$,
where $Y=(m^{-1}\sum_a y_a^2)^{1/2}$. With
$\varepsilon=n^{-1/2}$, (9) gives
$|S|=O_{d,m,\delta}((\log n)^{2d})$. Uniformity on the input box
implies the corresponding $L^2(\mu)$ estimate for any probability law
supported on the sphere.

This is actual empirical moment matching, not a population replacement.
It bypasses the $1/N$ variance lower bound for selectors measurable only
with respect to the training-forward marks, because the coefficient
vectors use the entire initialized query function of each top neuron.
Exact initial training-Gram matching can additionally be imposed by
including its $m(m+1)/2$ entries in those vectors.

**Limits of the proposition alone.** Each retained $b_j(v)$ still uses the
full original initialized first population and mixer. At initialization
these are fixed data. The proposition supplies neither a joint lower-layer
sampling rule nor an update of a moving $N$-neuron system. Applying its
proof to the evolved neuron functions would require fresh estimates for
their complex extension, and selecting their coefficients after seeing the
whole trajectory would be an oracle construction. Neither is asserted.
The next section removes the need to evaluate all lower initialized
features when computing the reduced snapshot or its own subsequent dynamics.

## 4. A joint-population snapshot with a bounded mixer and true adjoint

The following strengthening was proposed by the supervisor and checked
here. It uses only the initialization and training inputs, including no
trained trajectory. Both retained populations consist of original neuron
indices, although their fixed reduced mixer is a computed compression of
$W_0$, not its raw submatrix or a new independently initialized matrix.

Work on the probability-$1-\delta$ event of Section 3. Put
$\varepsilon_1=n^{-1}$ and $\varepsilon_2=n^{-1/2}$. The first-layer
functions $h_i(v)=\tanh(A_{0,i}\cdot v)$ are analytic and bounded by
one in the strip of width $s_0=c/R$ already constructed. The same
Fourier truncation argument supplies polynomials $P_i^{(1)}$ such that

\[
 \sup_{v\in[-1,1]^d}\max_i|h_i(v)-P_i^{(1)}(v)|
 \le\varepsilon_1,
\]

with coordinate degree

\[
 p_1\le C_d R[\log(1/\varepsilon_1)+d\log R+C_d]
       =O_{d,\delta}((\log n)^{3/2}).
\]

Let $S_1\subset\mathbb R^n$ be the span of all coefficient columns
of the vector-valued polynomial $P^{(1)}(v)$, together with the exact
training feature columns $h(v_a)$. Choose a matrix
$V\in\mathbb R^{n\times r}$ whose columns are an orthonormal basis
in the empirical inner product:

\[
 V^\top V/n=I_r,\qquad
 r\le(p_1+1)^d+m.
\]

Thus $P^{(1)}(v)=Va(v)$ for a polynomial coefficient vector
$a(v)\in\mathbb R^r$, and for every training input there is a vector
$a_a$ with $h(v_a)=Va_a$ exactly. Define the actual forward images
$U=W_0V\in\mathbb R^{n\times r}$. No orthonormality of $U$ is
assumed or required.

For the lower population, choose positive weights on a subset $I$ to
match mass one, every entry of $V_iV_i^\top$, and optionally every
entry of $A_{0,i}A_{0,i}^\top$. Here $V_i$ and $A_{0,i}$ denote
the respective rows, viewed as column vectors in those products. Let
$D_1$ be the diagonal matrix of these weights. The finite elimination
proof from Section 3 gives

\[
 V_I^\top D_1V_I=I_r,\qquad
 A_{0,I}^\top D_1A_{0,I}=A_0^\top A_0/n,
\]

\[
 |I|\le1+r(r+1)/2+d(d+1)/2.
\tag{J1}
\]

The second equality uses the optional root moments, included from now
on. In particular it preserves the weighted first-matrix RMS bound.

For the upper population, use the common top polynomials of Section 3
with accuracy $\varepsilon_2$, coordinate degree $p_2$, and
$R_2=(p_2+1)^d$ real coefficients $c_{j,k}$. Select positive weights
on a subset $J$ matching mass one and all entries of the three lists

\[
 U_jU_j^\top,\qquad
 (b_j(v_a)c_{j,k})_{a,k},\qquad
 (b_j(v_a)b_j(v_b))_{a\le b}.
\]

With $D_2$ the upper diagonal weight matrix, this gives

\[
 U_J^\top D_2U_J=U^\top U/n,
\]

\[
 |J|\le1+r(r+1)/2+mR_2+m(m+1)/2.
\tag{J2}
\]

All weights in (J1)--(J2) sum to one and zero weights have been
discarded. These are convex combinations of finite coefficient vectors;
their entries need not be uniformly bounded to obtain their exact moment
identities. No future state or population expectation enters selection.

Define the fixed reduced mixer and its weighted adjoint by

\[
 B_0=U_JV_I^\top D_1,\qquad
 B_0^*=D_1^{-1}B_0^\top D_2=V_IU_J^\top D_2.
\tag{J3}
\]

For lower vectors $g$, write $\|g\|_{D_1}^2=g^\top D_1g$;
upper norms use $D_2$. The map $V_I:\mathbb R^r\to
\mathbb R^{|I|}$ is an isometry by (J1), and its adjoint has norm
one. Also (J2) gives, for every $c\in\mathbb R^r$,

\[
 \|U_Jc\|_{D_2}^2
 =\|W_0Vc\|_2^2/n
 \le K^2\|Vc\|_2^2/n=K^2\|c\|_2^2.
\]

Consequently $\|B_0\|_{D_1\to D_2}\le K$, and $B_0^*$ is
exactly the adjoint of this same bounded operator. In particular both
orientations preserve the dependence of the chosen original matrix
coefficients. The identity $B_0(V_Ic)=U_Jc$ holds exactly.

The reduced network's initialized feature maps now use only retained
neurons:

\[
 h_c(v)=\tanh(A_{0,I}v),\qquad
 z_c(v)=B_0h_c(v),\qquad b_c(v)=\tanh z_c(v).
\tag{J4}
\]

For a training input, $h_c(v_a)=V_Ia_a$, hence
$z_c(v_a)=U_Ja_a=(W_0h(v_a))_J$. Therefore

\[
 b_c(v_a)=b_J(v_a)
\tag{J5}
\]

exactly. The last moments in (J2) give exact equality of the full
initial training kernels:

\[
 b_c(v_a)^\top D_2b_c(v_b)
 =\frac1n\sum_{j=1}^n b_j(v_a)b_j(v_b).
\tag{J6}
\]

Thus the normalized initial training Gram and its smallest eigenvalue
are exactly preserved. At zero readout, the training predictions and
their first physical-time derivatives also agree exactly at every
closure order. This is a statement about predictions at initialization,
not an identification of subsequent hidden derivatives.

For a general query, subtract $U_Ja(v)$ from both preactivations.
The first polynomial error gives
$\|h_c(v)-V_Ia(v)\|_{D_1}\le\varepsilon_1$, so

\[
 \|z_c(v)-U_Ja(v)\|_{D_2}\le K\varepsilon_1.
\]

On the original network, each selected row obeys

\[
 |[W_0(h(v)-Va(v))]_j|
 \le\|(W_0)_{j,:}\|_2\|h(v)-Va(v)\|_2
 \le K\sqrt n\,\varepsilon_1.
\]

Positive upper weights of total mass one then imply, uniformly over
the entire query box,

\[
 \|z_c(v)-z_J(v)\|_{D_2}
 \le K(1+\sqrt n)\varepsilon_1.
\tag{J7}
\]

Real tanh is 1-Lipschitz, so (J7) holds for the corresponding feature
difference. The upper cubature still satisfies (10), since it matches
all the same coefficient moments; its additional constraints do not
change that proof. Using (J5) and $\|b_J(v_a)\|_{D_2}\le1$, the
actual jointly reduced kernel therefore satisfies

\[
 \begin{aligned}
 &\sup_{v\in[-1,1]^d}\max_{a\le m}
 \left|b_c(v)^\top D_2b_c(v_a)-K_n(v,v_a)\right|\\
 &\hspace{15mm}\le 2\varepsilon_2+
                   K(1+\sqrt n)\varepsilon_1
 \le (2+2K)n^{-1/2}.
 \end{aligned}
\tag{J8}
\]

This comparison is against the original realized empirical kernel,
uniform on a continuum of queries. The associated initial prediction
velocity discrepancy is at most $2Y(2+2K)n^{-1/2}$, and is zero on
the training inputs.

For fixed $d,m,\delta$, the dimensions above satisfy
$r=O((\log n)^{3d/2})$ and $R_2=O((\log n)^{2d})$. Hence
both $|I|$ and $|J|$ are $O((\log n)^{3d})$. They are smaller than
$n$ for all sufficiently large $n$. The degree, support and weight
construction are finite procedures from the actual initialization.
They may require substantial setup work; no efficient setup-time bound
or floating-point conditioning guarantee is claimed.

To obtain an actual autonomous reduced order-$q$ closure, use
$A_{0,I}$, zero readout, and (J3) as fixed initialization, with first
and second population expectations given by $D_1,D_2$. Use its own
residual and RMS clock, the original moment source/dilation rules, and
the reconstruction (16) below with $W_N$ replaced by $B_0$. The
weighted adjoint is always that of the same reconstructed operator.
This specifies a finite evolving algorithm with moving state
$mq(|I|+|J|)+d|I|+|J|+1$.

After setup, neither (J4) nor this reduced evolution evaluates any
discarded lower neuron. Its fixed matrix can be stored as $B_0$ or in
the factored form (J3). The original Gaussian mixer is used during
setup to form $U=W_0V$; it is not replaced by independent randomness.
What has been approximated is its action away from the selected source
space. The same weighted operator and adjoint are then used in every
reduced forward and backward pass.

**Scope of this construction.** It is a concrete joint-population
reduction with certified initial observable accuracy, initial Gram,
and operator bounds. These properties do not prove accuracy after
training starts. A weighted version of the paper's deterministic
small-label fitting argument is a separate verification; fitting
itself would still not prove the desired trajectory fidelity. The
unproved all-time comparison is unchanged.

## 5. What source-space cubature preserves exactly

There is a useful finite-dimensional algebraic mechanism that keeps both
orientations of one matrix. It is conditional on finding useful spaces.
Let $V\in\mathbb R^{n\times r}$ and
$U\in\mathbb R^{n\times s}$ have columns spanning first- and
second-population source spaces, normalized by

\[
 V^\top V/n=I_r,\qquad U^\top U/n=I_s.
\]

Select positive cubature weights on first and second neurons that match
all pairwise products of basis coordinates. The elementary elimination
argument above supplies node sets $I,J$ with

\[
 |I|\le1+r(r+1)/2,\qquad |J|\le1+s(s+1)/2.
\]

Write $V_I,U_J$ for the evaluation matrices, and let $D_1,D_2$ be
diagonal matrices of the positive weights. Exact Gram matching says

\[
 V_I^\top D_1V_I=I_r,\qquad U_J^\top D_2U_J=I_s.
\tag{12}
\]

Thus evaluation on the nodes is an isometry on each specified source
space, for the empirical inner product $a^\top b/n$ on the original
population and the weighted inner product on the sampled one. Define

\[
 B=U^\top W_0V/n,\qquad
 W_N=U_J B V_I^\top D_1.
\tag{13}
\]

The adjoint for these two weighted spaces is

\[
 W_N^*=D_1^{-1}W_N^\top D_2
       =V_I B^\top U_J^\top D_2.
\tag{14}
\]

Equations (12)--(14) exactly reproduce the original Galerkin matrix
$P_UW_0P_V$ and its actual adjoint on the selected spaces, where
$P_V=VV^\top/n$ and $P_U=UU^\top/n$. They use one fixed realization
of $W_0$ and one transpose of its coefficient matrix $B$; no fresh
independent reverse noise is introduced. Also
$\|B\|_{\rm op}\le\|W_0\|_{\rm op}$.

For example, $W_N(V_Ic)=U_JBc$ and
$W_N^*(U_Jb)=V_IB^\top b$. The original identities are
$P_UW_0(Vc)=UBc$ and $P_VW_0^\top(Ub)=VB^\top b$.
The omitted errors are explicitly

\[
 (I-P_U)W_0Vc,\qquad (I-P_V)W_0^\top Ub.
\tag{15}
\]

Matching empirical moments proves no bound on (15).

The projected sampled system nevertheless has a concrete autonomous
weighted residual-RMS closure: use (1) with $1/n$ pairings replaced by
the corresponding weights, $W_N$ as its fixed mixer, and the weighted
adjoint (14) in backpropagation. More explicitly its reconstruction is

\[
 \widehat W_N=W_N-\frac2{m\tau}
  \sum_{a,j<q}(2j+1)\bar\delta_{a,j}^{(2)}
                      \bar h_{a,j}^{(1)\top}D_1.
\tag{16}
\]

Its prediction is $w^\top D_2h^{(2)}$, its lower backward response is
$\operatorname{sech}^2(Av_a)\odot\widehat W_N^*\delta_a^{(2)}$,
and its first/readout updates and moment source/dilation rules are those
in Section 1 with its own residual. First weights are initialized by the
selected rows of $A_0$, and readout and backward memories are zero.
This describes an actual finite algorithm without future trajectory data.
Its moving count is

\[
 m q(|I|+|J|)+d|I|+|J|+1=O_{m,d}(Nq),
 \qquad N=\max\{|I|,|J|\}.
\]

It is an approximation to the original mixer, not an identity on all
original neurons. Establishing the requested theorem requires proving
that the approximation in (15), nonlinear source-space errors, and
cubature errors along this system's own feedback stay small. Definition
(16) alone does not establish that comparison.

## 6. Exact invariant spaces are generically full-dimensional

An exact linear source-space solution cannot simply assume that finite
spaces are invariant under both matrix orientations. Almost surely a
square Gaussian $W_0$ has distinct positive singular values. If a
nonzero vector $h$, independent of $W_0$, belongs to a space $S_1$ and

\[
 W_0S_1\subseteq S_2,\qquad W_0^\top S_2\subseteq S_1,
\tag{17}
\]

then $S_1=\mathbb R^n$ almost surely. Indeed (17) forces every
$(W_0^\top W_0)^kh$ into $S_1$. The right singular vectors are
rotationally invariant, so $h$ has a nonzero component in every one
almost surely. In this basis the first $n$ Krylov vectors are the
product of a nonzero diagonal matrix with the Vandermonde matrix on
the distinct squared singular values. Their determinant is nonzero.

Distinctness and positivity hold because the determinant and
characteristic-polynomial discriminant are nonzero polynomials of the
Gaussian entries, and a nonzero polynomial vanishes with probability
zero under a density. Rotational invariance follows from the unchanged
law of $W_0O$ for every orthogonal $O$; each eigenvector direction
therefore assigns probability zero to the hyperplane perpendicular to
fixed $h$. The initial first feature $h=\tanh(A_0v)$ is independent
of $W_0$ and nonzero almost surely, so it is a valid example.

This obstruction concerns exact invariance on whole linear spaces.
Approximate low-rank actions on the trajectory, weak cancellation in
predictions, and weighted nonlinear source encodings remain possible.
The initial cubature proposition is one explicit example of that
distinction.

## 7. The remaining quantitative bridge

The joint-population construction in Section 4 proves that an infinite-rank
source can have a small effective approximation space and a finite
weighted implementation with a bounded mixer. Equations (2)--(7)
prove that updating initial marks once does not automatically preserve
this property under hidden learning. Neither result determines the
effective source dimension of the entire closure trajectory.

A sufficient positive route would construct, from the initialization
and training data without the future path, spaces of dimensions $r,s$
and cubature rules such that all evolving feature, backward-response,
and history fields are approximable there, the two residuals in (15)
are controlled on the required sources, and the integrated feedback
defect is $O_\delta(n^{-1/2})$ after its stability amplification.
All-query evaluation must obey the same bound with the supremum over
physical time inside the $L^2(\mu)$ norm. An estimate for selected
time/query pairs is insufficient.

If the maximal source-space dimension were $r_*=\max(r,s)$, Section
5 would give $N=O(r_*^2)$. Only after separately proving an appropriate
neuron approximation theorem uniformly in the original closure order
could this be combined with the supervisor's current history choice
$q=n^{1/6+o(1)}$. Under that additional theorem, a dimension
$r_*=n^{\gamma+o(1)}$ with $\gamma<5/12$ would make $Nq=o(n)$;
polylogarithmic dimension would give $Nq=n^{1/6+o(1)}$. These are
conditional counts, not rates established for the actual evolving source
spaces or inherited by the weighted closure.

Small fixed labels suggest an expansion by interaction depth, but they
do not by themselves certify it. A geometric truncation estimate
$C\eta^p$, $0<\eta<1$, would require
$p\gtrsim\log n/(2|\log\eta|)$ for the requested accuracy. The number
of independent or important sources generated through that depth and
their anisotropic weights then matter. A bounded effective dimension
cannot be inferred merely from fixed $m,d$ or from $q$ stored history
modes. Conversely, growth in the number of exact sources does not prove
a lower bound on the number needed to approximate predictions.

The established all-time parameter comparison in the paper concerns
systems in the same width-$n$ physical space. It does not already give
stability of the weighted system (16), nor a quantitative finite-width
population bias of size $C_\delta/\sqrt n$. A proof using a population
intermediate would have to supply that separate bias. The empirical
cubature construction avoids an initial population bias, but currently
only for its stated initial observables and fixed source-space algebra.

**Current verdict.** Better-than-Monte-Carlo sampling is provably possible
for both initialized neuron populations while retaining the original
training kernel exactly and the whole-query kernel to root-width
accuracy, including the realized width-$n$ fluctuations. A concrete
weighted autonomous residual-RMS closure can be initialized by this
construction, with bounded mixer and true adjoint. Its all-time fidelity
is not proved. The decisive unresolved task is a source-space
approximation theorem through hidden learning that controls both
orientations of the same mixer and the sampled system's own feedback.
