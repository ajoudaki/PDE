# Endpoint transverse route: exact residual identity and a relative-metric obstruction

2026-10-11. Scoped author derivation. Scientific inputs were only
`paper/compact.tex`, `paper/compact_fitting.tex`,
`NONPARALLEL_INITIAL_VARIABILITY.md`, and
`ENDPOINT_SEPARATION_STRUCTURE.md`. Required proof, research, and canonical
notation instructions were read. No experiment, manuscript edit, or Git
operation was performed.

**Result.** The requested endpoint lower bound remains open in this route.
There is a new exact endpoint identity that removes the component determined
by fitting, and the readout component transverse to its initial training
span is bounded by a width-independent multiple of the cube of the label
scale. The identity also gives an explicit cubic label coefficient. A
high-frequency admissible activation family shows that a proposed relative
feature estimate cannot follow just from the paper's strip envelope and
small-motion tube for first-layer residuals, even for a well-conditioned orthogonal training pair and
a test at angle \(\pi/4\) from both inputs. This obstruction concerns that proof
route; it is not a counterexample to endpoint variability.

The unchanged target is two independent, fully trained canonical runs with
zero initial readout, fixed nonzero labels under the original cap, fixed
depth at least two, nonaffine strip-analytic activations with bounded
derivative, pairwise nonparallel training directions, and a fixed test
separated from both signs of every training direction. The desired lower
bound is a positive confidence-dependent constant times \(n^{-1/2}\), eventually
at each individual width. No smaller label cap is used below.

## 1. Definitions and the exact endpoint identity

Retain the source network, with normalized inputs \(v=x/\sqrt d\):

\[
z^{(1)}=W^{(1)}v,\qquad z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},
\qquad h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad
f_n=w^\top h^{(L)}/n.
\]

Put \(r_a=f_n(x_a)-y_a\) and use the source loss
\(\mathcal L=m^{-1}\|r\|_2^2\) and its physical gradient flow.
The normalized readout and feature columns are

\[
a(t)=w(t)/\sqrt n,\quad
B(t)=[h^{(L)}(t,x_1),\ldots,h^{(L)}(t,x_m)]/\sqrt n,
\quad b_q(t)=h^{(L)}(t,x_q)/\sqrt n.
\]

Thus \(B\) is an \(n\) by \(m\) matrix, \(a\) and \(b_q\) are \(n\)-vectors,
\(F(t)=B(t)^\top a(t)\) is the training prediction vector, and

\[
\dot a(t)=-\frac2m B(t)r(t),\qquad a(0)=0.
\tag{1}
\]

Work on the source fitting event. In particular
\(G_0=B(0)^\top B(0)\) is invertible. Let

\[
c_q=G_0^{-1}B(0)^\top b_q(0),\qquad
R_q(t)=b_q(t)-B(t)c_q,
\qquad
P_0=B(0)G_0^{-1}B(0)^\top.
\tag{2}
\]

Here \(c_q\) is fixed throughout training. \(R_q(0)\) is the initial test feature
residual after orthogonal projection on the training columns; \(R_q(t)\) uses
these same initial projection coefficients, so it is not the moving
orthogonal projection residual. We have
\(B(0)^\top R_q(0)=0\).

The fitted endpoint obeys the exact identity

\[
\begin{split}
f_n(\infty,x_q)-c_q^\top y
={}&a(\infty)^\top[R_q(\infty)-R_q(0)]\\
&-\frac2m\int_0^\infty
 R_q(0)^\top[B(t)-B(0)]r(t)\,dt.
\end{split}
\tag{3}
\]

To prove it, fitting gives
\(f_n(\infty,x_q)-c_q^\top y=a(\infty)^\top R_q(\infty)\).
Integrating (1) and using initial orthogonality gives

\[
a(\infty)^\top R_q(0)
=-\frac2m\int_0^\infty R_q(0)^\top[B(t)-B(0)]r(t)\,dt.
\]

Adding and subtracting \(R_q(0)\) proves (3). Residual decay and bounded
features justify all integrals. This is a fully trained identity. It does
not replace the dynamics by frozen features.

There is also an exact formula for the transverse readout component:

\[
(I-P_0)a(\infty)
=-\frac2m\int_0^\infty(I-P_0)[B(t)-B(0)]r(t)\,dt.
\tag{4}
\]

The expression \(c_q^\top y\) in (3) is precisely the initialized frozen-feature
interpolant at the test. Equation (3) identifies the two actual sources of
its endpoint error: motion of the test residual and transverse readout
motion. At a training query both terms vanish exactly.

## 2. A cubic bound under the original cap

Write \(\lambda=\gamma/m\). To recall the constants in the source
fitting proof, put

\[
H=\max_{0\le j\le L}\sqrt{Q^{(j)}_{11}},\qquad
\sigma=\max\left\{1,\max_j\sup_{|\operatorname{Im}z|\le a/2}
                    |\phi_j'(z)|\right\},
\qquad
F=\sigma^2\left[(9\sigma)^{2L-2}
      +4H^2\sum_{j=0}^{L-2}(9\sigma)^{2j}\right].
\]

In the supremum, \(a\) denotes the source's strip width, not the
time-dependent normalized readout \(a(t)\). That proof gives, with
\(D=8FY^2/\lambda^{3/2}\),

\[
\sup_t\|B(t)-B(0)\|_{\mathrm{op}}\le\sqrt m D,
\quad \sup_t\|b_q(t)-b_q(0)\|\le D,
\quad \|a(\infty)\|\le2Y/\sqrt\lambda,
\quad \int_0^\infty\|r(t)\|\,dt\le2\sqrt mY/\lambda.
\tag{5}
\]

Applying (5) to (4) yields the explicit bound

\[
\|(I-P_0)a(\infty)\|
\le\frac{4DY}{\lambda}
=\frac{32FY^3}{\lambda^{5/2}}.
\tag{6}
\]

Equation (3) gives the more geometry-sensitive statement

\[
|f_n(\infty,x_q)-c_q^\top y|
\le\frac{2Y}{\sqrt\lambda}
       \|R_q(\infty)-R_q(0)\|
    +\frac{32FY^3}{\lambda^{5/2}}\|R_q(0)\|.
\tag{7}
\]

For comparison, a purely absolute bound follows from
\(\|R_q(\infty)-R_q(0)\|\le D(1+\sqrt m\|c_q\|)\),
\(\|R_q(0)\|\le3H/2\), and
\(\sqrt m\|c_q\|\le3H/\sqrt{2\lambda}\):

\[
|f_n(\infty,x_q)-c_q^\top y|
\le\frac{16FY^3}{\lambda^2}
        \left(1+\frac{3H}{\sqrt{2\lambda}}\right)
     +\frac{48HFY^3}{\lambda^{5/2}}.
\tag{8}
\]

The coefficient bound uses
\(\lambda_{\min}(G_0)\ge\gamma/2\) and
\(\|B(0)c_q\|\le\|b_q(0)\|\le3H/2\).
These estimates hold at every width on the supplied fitting event and do
not require nonparallel geometry. They do not establish endpoint
anti-concentration: their error is fixed as width grows.

## 3. The exact cubic coefficient in label amplitude

For this section only, replace labels \(y\) by \(sy\) and fix a finite-width
initialization with full-rank \(B(0)\). Use hidden mobility coordinates

\[
u=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)}).
\]

For a training or test input, \(b_x(u)\) denotes its normalized final feature
vector. The full flow in \((u,a)\) is

\[
\dot a=-\frac2m B(u)r,\qquad
\dot u=-\frac2m\sum_{j=1}^m r_j D b_j(u)^\top a,
\qquad r=B(u)^\top a-sy.
\tag{9}
\]

Here \(D b_j\) is the derivative with respect to \(u\); its transpose is for the
Euclidean mobility inner product. All quantities below are evaluated at
this fixed finite width.

The endpoint and trajectories near \(s=0\) admit local Taylor expansions.
One can justify the infinite-time statement directly as follows. At the
zero-label stationary state, use coordinates \((u,e,r,s)\), where
\(e=(I-P_0)a\), solving

\[
a=e+B(0)[B(u)^\top B(0)]^{-1}[r+sy-B(u)^\top e].
\]

Here \(e\) ranges in the fixed subspace \(\ker B(0)^\top\), not in all
of the readout space. This is an analytic coordinate chart near
\((u(0),0,0,0)\). The \(r\) equation is
\(\dot r=-(2/m)JJ^\top r\), where \(J\) is the training Jacobian in
mobility coordinates. Its coefficient at the base point is
\((2/m)G_0\succ0\); it remains accretive in a sufficiently small
complex neighborhood, because it is a continuous analytic matrix there.
The transpose remains the ordinary transpose under analytic continuation;
accretivity means positivity of the Hermitian part near the positive real
base matrix, not that the continued matrix is Hermitian.
The \((u,e)\) velocities are analytic matrices times \(r\). For small complex \(s\),
exponential decay of \(r\) and its integrable bound prevent exit from this
neighborhood. The endpoint is therefore a locally uniform limit of
holomorphic finite-time maps and is holomorphic. Cauchy's formula on a
smaller \(s\) disk also justifies termwise endpoint derivatives. This local
radius can depend on width and initialization; no original-cap radius is
claimed.

Symmetry under \((s,a)\mapsto(-s,-a)\) gives expansions

\[
a=s a_1+s^3a_3+O(s^5),\qquad
u=u(0)+s^2u_2+O(s^4),\qquad
r=s r_1+s^3r_3+O(s^5).
\]

Put \(B_0=B(0)\). Substitution in (9) gives explicitly

\[
\begin{aligned}
r_1(t)&=-e^{-2G_0t/m}y,\\
a_1(t)&=B_0G_0^{-1}(I-e^{-2G_0t/m})y,\\
\dot u_2(t)&=-\frac2m\sum_j r_{1,j}(t)
                         D b_j(u(0))^\top a_1(t),
\qquad u_2(0)=0.
\end{aligned}
\tag{10}
\]

In particular \(a_1(\infty)=B_0G_0^{-1}y\). Let
\(R_q(u)=b_q(u)-B(u)c_q\), with the fixed coefficient in (2).
Expanding the exact identity (3), rather than discarding the trained
hidden motion, gives

\[
\begin{split}
f_n(\infty,x_q;sy)
={}&s c_q^\top y+s^3 p_3+O(s^5),\\
p_3={}&a_1(\infty)^\top D R_q(u(0))[u_2(\infty)]\\
&-\frac2m\int_0^\infty
 R_q(u(0))^\top D B(u(0))[u_2(t)]r_1(t)\,dt.
\end{split}
\tag{11}
\]

The integrals converge: \(a_1\) is bounded, \(r_1\) decays exponentially, and \(u_2\)
has an integrable derivative. Formula (11) identifies a new
requirement for relative perturbation. The cubic term contains \(D R_q\) as
well as \(R_q\). Initial feature novelty alone does not control it.

For perspective, the differential of the frozen-feature interpolant
\(p_1=b_q^\top B(B^\top B)^{-1}y\) is itself

\[
D p_1[\xi]
=a_1(\infty)^\top(D b_q[\xi]-D B[\xi]c_q)
 +R_q(0)^\top D B[\xi]G_0^{-1}y.
\tag{12}
\]

This follows by differentiating the inverse Gram and grouping the terms.
The parallel structure of (11) and (12) suggests a metric involving both
the residual and its hidden derivative. It does not supply coercivity of
that metric under training, or control of its Gaussian divergence.

## 4. A relative bound unavailable from the strip envelope alone

Here is an explicit first-layer obstruction to deriving
\(\|D R[\xi]\|\le C\|R\|\|\xi\|\), with C controlled just by
the paper's beta, depth, geometry, and training gap.

For integers \(k\ge1\) choose the admissible odd activation

\[
\phi_k(z)=z+\varepsilon_k\sin(kz),\qquad
\varepsilon_k=e^{-2k}/k.
\tag{13}
\]

Take strip width \(a=1\). On the full strip,
\(|\phi_k'(z)|\le1+e^{-k}\); on its half strip,
\(|\phi_k''(z)|\le k e^{-3k/2}<1\). Thus the paper's common envelope
can be \(\beta=16\) for every \(k\). Every activation is nonaffine and has unbounded
values, as the paper permits. The same activation can be used at every
layer.

At the first layer let \(v_1=e_1\), \(v_2=e_2\), and
\(v_q=(e_1+e_2)/\sqrt2\). For a Gaussian row, let \(Z_1,Z_2\) be
independent standard normals and \(U=(Z_1+Z_2)/\sqrt2\). The residual using
the exact linear-input coefficients is

\[
R_k=\phi_k(U)-\frac{\phi_k(Z_1)+\phi_k(Z_2)}{\sqrt2}
=\varepsilon_k\left[\sin(kU)
-\frac{\sin(kZ_1)+\sin(kZ_2)}{\sqrt2}\right].
\tag{14}
\]

Write \(\rho=1/\sqrt2\),
\(s_k=(1-e^{-2k^2})/2\), and
\(t_k=[e^{-k^2(1-\rho)}-e^{-k^2(1+\rho)}]/2\).
The elementary Gaussian characteristic function gives

\[
\mathbb E R_k^2=\varepsilon_k^2(2s_k-2\sqrt2t_k),
\qquad \|R_k\|_{L^2}/\varepsilon_k\longrightarrow1.
\tag{15}
\]

Now dilate that hidden row by \(1+\eta\). The derivative at \(\eta=0\) is

\[
\partial_\eta R_k
=\varepsilon_k k\left[U\cos(kU)
-\frac{Z_1\cos(kZ_1)+Z_2\cos(kZ_2)}{\sqrt2}\right].
\tag{16}
\]

Its squared \(L^2\) norm divided by \(\varepsilon_k^2 k^2\) tends to one.
The dilation direction itself has fixed Gaussian \(L^2\) norm
\(\|(Z_1,Z_2)\|_{L^2}=\sqrt2\), independent of \(k\).
Indeed
\(\mathbb E[Z^2\cos^2(kZ)]
=[1+(1-4k^2)e^{-2k^2}]/2\to1/2\).
The two independent-coordinate cross terms vanish by oddness. The remaining
cross terms tend to zero, since differentiating the joint Gaussian
characteristic function bounds them by a polynomial in \(k\) times
\(e^{-k^2(1-\rho)}\). Consequently

\[
\frac{\|\partial_\eta R_k\|_{L^2}}{\|R_k\|_{L^2}}
\sim k.
\tag{17}
\]

This also holds using the true initial population projection coefficients,
held fixed during the subsequent displacement as in (2). The training
feature Gram is \(g_k I_2\), where
\(g_k=1+2\varepsilon_k k e^{-k^2/2}+\varepsilon_k^2s_k\to1\).
Each population projection coefficient is

\[
\frac{\rho(1+2\varepsilon_k k e^{-k^2/2})+
             \varepsilon_k^2t_k}{g_k}
=\rho+O(\varepsilon_k^2).
\]

Replacing the coefficient \(\rho\) in (14) by this coefficient changes the
residual by \(O(\varepsilon_k^2)\) in \(L^2\) and the dilation derivative by
\(O(\varepsilon_k^2)\). These are negligible in (15) and (17).

There is a finite-motion version. Choose \(\eta_k>0\) with \(\eta_k\to0\) and
\(k\eta_k\to\infty\). The covariance between the bracket in (14) at frequency
\(k\) and its value at frequency \(k(1+\eta_k)\) tends to zero. For equal directions
the covariance is bounded by
\(e^{-(k\eta_k)^2/2}\); for the other nonparallel directions it is
bounded by an exponential in \(-k^2\). Each variance tends to one, so

\[
\frac{\|R_k((1+\eta_k)Z)-R_k(Z)\|_{L^2}}
     {\|R_k(Z)\|_{L^2}}\longrightarrow\sqrt2.
\tag{18}
\]

An arbitrarily small hidden displacement can therefore make an order-one
relative change to test novelty while the strip envelope, input angles, and
training conditioning stay controlled. For independent first-layer rows,
the corresponding normalized empirical norms converge to these Gaussian
norms by the ordinary second-moment law of large numbers. The training
Gram at every fixed depth also stays near \(I_2\) as \(k\) grows: oddness preserves
zero off-diagonal covariance and (13) converges uniformly to the identity
on the real line. Hence a training gap bounded away from zero does not
repair the missing uniform relative constant.

The dilation above is an allowed small hidden displacement, not a claim
about the displacement actually produced by canonical gradient flow.
Thus (17)--(18) refute a bound inferred from the tube and strip envelope
alone; they do not refute a special cancellation or transport identity
along the reachable training flow. This calculation is at the first
hidden layer; a proposed estimate specific to the final layer still needs
its own analysis. A bound with an additional
activation-dependent constant is not excluded, but absorbing it by a
smaller label cap would change the assignment.

## 5. Exact status and reopening condition

| Claim | Status |
| --- | --- |
| Exact fitted residual identity (3) and readout formula (4) | Proved on the supplied fitting event |
| Width-independent cubic transverse-readout bound (6) under the original cap | Proved |
| Local finite-width cubic endpoint coefficient (11) | Proved; local amplitude radius has no uniform claim |
| Beta-controlled relative first-layer residual derivative bound from arbitrary small hidden motion | Refuted by (13)--(18) |
| The reachable canonical flow satisfies a stronger relative identity that prevents endpoint cancellation | Open |
| Fixed-test or sphere endpoint discrepancy has a c_delta/sqrt(n) lower bound under the original cap | Not proved or disproved |

The useful reopening condition is a flow-specific estimate linking the
two terms in (3), or their Gaussian derivatives, to a nonvanishing
transverse signal. An estimate of \(R_q\) alone is insufficient because (11)
contains \(D R_q\); an unrestricted relative derivative estimate is invalid
by Section 4. An alternative would be a nonperturbative transport argument
that preserves an appropriate residual norm without requiring the residual
to remain close to its initial value. No such transport theorem is asserted
here. The existing Gaussian small-ball criterion still additionally needs
width-uniform regularity of the normalized pulled-back direction.

This route is blocked for the requested full theorem at that concrete
bridge. The new identities can be retained independently of the unresolved
endpoint lower bound. The fresh isolated reconstruction in
`ENDPOINT_TRANSVERSE_CHECK.md` accepted the stated partial results, with
their first-layer and arbitrary-displacement scope. After the frozen review,
those scope words, the fixed projection coefficients, and the complex-chart
conventions were made explicit above; no mathematical claim was strengthened.
These are internally checked research, not promoted established material.

## Frozen input hashes

| Input | SHA-256 |
| --- | --- |
| `paper/compact.tex` | `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `NONPARALLEL_INITIAL_VARIABILITY.md` | `017c2dcbd3e3b938099ab7dd748a211f859126bd636767b667ef3432386e33bc` |
| `ENDPOINT_SEPARATION_STRUCTURE.md` | `158d5bbfa8aa9a29cf6aeb26c36aeba6da9f2580aad536972b9b264a631b3a1c` |
