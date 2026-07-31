# Numerical routes to an honest width-independent neural-PDE simulation

## Bottom line

The old `dense_mup_long_horizon_repro` bundle does **not** contain an
executable instance of its displayed response PDE.  It contains a very good
finite-matrix \(q/r\) response projection, but its state still includes
\(W\in\mathbb R^{L\times n\times n}\).  More importantly, the theory note
does not emit the objects a PDE solver would need:

- the value of \(J_*\);
- the finite tag and historical-\(\kappa\) tables;
- the actual source dimension \(D_{K,J,N}\);
- the moment list;
- the finite conditional Gaussian kernel \(\Gamma_{K,J,N}\);
- the closed drift DAGs \(V^{(q)}_{K,J,N}\) and
  \(B^{(q)}_{K,J,N}\); or
- an explicit initial Gaussian pushforward.

There is no numerical trick that can repair a missing vector field.  Thus
none of the three generic solvers below can literally run
\((\mathrm{PDE}\text{-}K,J,N)\) from the current note.

There is, however, a second and substantially more explicit route.  I
derived and implemented an **isonormal Hermite operator-Galerkin PDE**.  It
has no network width, no \(n\times n\) matrix, uses the same finite row
coefficients for \(W\) and \(W^\top\), and trains those coefficients by the
projected ordinary Euclidean \(\mu\)P gradient.  It is an actual autonomous
conditional Liouville PDE at every finite Hermite order \(P\).  Two
independently written implementations agree to machine precision.

This is the recommended immediate route.  It is scientifically admissible
as an accuracy-dependent Galerkin approximation of the standard dense
model, but only if its \(P\to\infty\) and depth limits are tested.  At fixed
\(P\) it is a rank-\(P\) operator approximation, so it must never be
described as the original dense architecture itself.

## 1. What numerical object would count

For a compiled finite Liouville system, put

\[
b(\xi;\rho,\kappa)
=
\sum_{q=1}^m e_q[\rho]\,
V^{(q)}(\xi;\mathcal M[\rho],\kappa),
\]

\[
\partial_t\rho+\nabla_\xi\!\cdot(\rho b)=0,
\qquad
\dot\kappa
=
\sum_{q=1}^m e_q[\rho]B^{(q)}(\mathcal M[\rho],\kappa).
\tag{1}
\]

An honest numerical state may be

\[
\rho_M=\sum_{i=1}^M w_i\delta_{\xi_i},
\qquad \xi_i\in\mathbb R^D,
\tag{2}
\]

or a grid/spectral representation on the same fixed
\(\mathbb R^D\).  The coordinate dimension \(D\) and every moment and drift
formula must depend only on compiler indices and the fixed sample count.
The numerical resolution \(M\) may grow, but there may be no microscopic
neuron-pair parameter and no \(n\times n\) action.

Under this definition, the existing `FieldState.W` simulations do not
qualify.  The operator-Galerkin system in Section 2 does.

## 2. Explicit alternative: isonormal Hermite operator Galerkin

### 2.1 Derivation from the dense operator

Let \(g\) be the immutable neuron latent consisting of the initial input-map
row and initial readout:

\[
g=(B(0)_{i,\cdot},a_i(0)/A)\sim\mu=N(0,I_{d+1}).
\]

For orthogonal \(m=d\) samples only the \(m\) projections of the \(B\)-row
are needed, so the intrinsic base dimension is \(m+1\).

Fix, before training, the first \(P\) orthonormal Hermite functions
\(\phi_1,\ldots,\phi_P\) in \(L^2(\mu)\).  At finite width let
\(\Phi_{ij}=\phi_j(g_i)\).  The column-Galerkin projection of one dense layer
has the form

\[
W_{\ell,P}
=
\frac1n C_\ell\Phi^\top,
\qquad
C_\ell=W_\ell\Phi.
\tag{3}
\]

If \(h\) is a neuron field and

\[
H_{rj}=\mathbb E_\mu[\phi_j(g)h_r(g)],
\tag{4}
\]

then the same row coefficient \(c=(c_1,\ldots,c_P)\) gives both orientations:

\[
(W_Ph_r)(g,c)
=
\sum_{j=1}^P c_jH_{rj},
\tag{5}
\]

\[
(W_P^\top v)(g)
=
\sum_{j=1}^P\phi_j(g)\,
\mathbb E_{g',c}[c_jv(g',c)].
\tag{6}
\]

At initialization the rows of \(C_\ell\) converge to
\(N(0,\sigma_w^2I_P)\).  Equation (6), not an independent Gaussian
transpose tag, automatically contains the correct Stein/Onsager
correlation.

Projecting the exact standard Euclidean update

\[
\dot W_\ell
=
-\frac{\gamma}{n}\sum_qe_q\beta_qh_q^\top
\]

onto (3) gives

\[
\boxed{
\dot c_j
=
-\gamma\sum_qe_q\beta_qH_{qj}.
}
\tag{7}
\]

No custom metric or projected manifold descent has been introduced:
equation (7) is the orthogonal Galerkin projection of the ordinary ambient
Euclidean \(\mu\)P vector field.

### 2.2 Closed conditional Liouville PDE

It is clearest to split a row coefficient into an immutable Gaussian
innovation and a learned part:

\[
r_j=\sigma_w\varepsilon_j+c_j,
\qquad
\varepsilon\sim N(0,I_P),\quad c(0)=0.
\]

For every depth \(s\), let
\(\eta_{s,t}(d\varepsilon,dc\mid g)\) be its conditional law.  Define

\[
z_r(g,\varepsilon,c;s,t)
=
\sum_jr_jH_{rj}(s,t),
\qquad
\beta_r
=
\operatorname{sech}^2(z_r)\,p_r(g,s,t).
\tag{8}
\]

The depth forward/adjoint boundary-value problem is

\[
\partial_sh_r(g,s,t)
=
\gamma\,
\mathbb E_{\eta_{s,t}(\cdot\mid g)}[\tanh z_r],
\qquad
h_r(g,0,t)=B(g,t)x_r,
\tag{9}
\]

\[
-\partial_sp_r(g,s,t)
=
\gamma\sum_j\phi_j(g)\,
\mathbb E_{\mu(dg')\eta_{s,t}(d\varepsilon,dc\mid g')}
[r_j\beta_r],
\qquad
p_r(g,1,t)=a(g,t).
\tag{10}
\]

The conditional measure evolves by

\[
\boxed{
\partial_t\eta_{s,t}
+
\nabla_c\!\cdot
\left[
\eta_{s,t}
\left(
-\gamma\sum_qe_q\beta_qH_q
\right)
\right]
=0.
}
\tag{11}
\]

The remaining standard Euclidean blocks are

\[
\dot a(g,t)=-\sum_qe_qh_q(g,1,t),
\tag{12}
\]

\[
\dot B(g,t)=-\sum_qe_qp_q(g,0,t)x_q^\top,
\tag{13}
\]

\[
f_r(t)=\mathbb E_\mu[a(g,t)h_r(g,1,t)],
\qquad e=f-y.
\tag{14}
\]

Equations (8)--(14) are autonomous and restartable from the current
\((B,a,\eta)\).  They contain no training-time history.

Their tangent kernel is explicitly positive semidefinite:

\[
\begin{aligned}
\Theta^P_{rq}
={}&
\mathbb E_\mu[h_r(1)h_q(1)]
+
(x_r^\top x_q)\mathbb E_\mu[p_r(0)p_q(0)]
\\
&+
\gamma^2\int_0^1
\left(\sum_jH_{rj}H_{qj}\right)
\mathbb E_{\mu\eta_s}[\beta_r\beta_q]\,ds .
\end{aligned}
\tag{15}
\]

The implemented flow passes the independent identity

\[
\dot f=-\Theta^Pe.
\tag{16}
\]

### 2.3 Why this is promising, and the precise risk

At fixed \(P\), (3) is a rank-\(P\) column projection.  That is acceptable
as a numerical Galerkin surrogate only if

\[
\sup_{t,s}
\left(
\|f_P(t)-f(t)\|
+
\|G_P(s,t)-G(s,t)\|_F
\right)\longrightarrow0
\tag{17}
\]

as \(P\to\infty\).  It is not acceptable to call the fixed-\(P\) system the
original architecture.

The key structural assumption is that, after iid-depth homogenization, the
slow fields \(h,p,B,a\) are measurable functions of the immutable \(g\).
Fast layer innovations must contribute only through their local conditional
law.  If an \(O(1)\) depth-path latent survives, a basis on \(g\) alone is
not complete and this route fails.

The paired-\(W\) experiment in Section 6 is direct evidence for this
assumption: conditional forward and adjoint variances both decay almost
exactly as \(1/L\), at initialization and after feature-learning training.

Other unresolved points are:

- convergence is strong on the actual query orbit, not in operator norm;
- high Hermite modes can feed back to low modes through \(\tanh\);
- propagation of chaos conditional on \(g\) and the specified
  width-then-depth order remain unproved;
- uniform-in-training-time Galerkin stability remains unproved.

## 3. Three independent numerical realizations

### Route A: randomized QMC characteristics

For (1), choose a frozen scrambled Sobol rule
\(g_i\), map it through the static Gaussian initial pushforward
\(\xi_i(0)=T(g_i)\), and evolve

\[
\dot\xi_i
=
b\!\left(
\xi_i;
\sum_jw_j\Phi(\xi_j),
\kappa
\right),
\qquad
\dot\kappa=K\!\left(\sum_jw_j\Phi(\xi_j),\kappa\right).
\tag{18}
\]

For the operator PDE, use nested points \(g_i\) and
\(\varepsilon_r\), while \(c_{s,i,r}\) follows (7).  Centering and whitening
the frozen Sobol points is permissible because it is fixed before seeing
positive-time curves and is applied identically in (5) and (6).
The implementation reuses one epsilon cubature table at different depth
nodes only as a deterministic integration rule: every displayed formula is
pointwise in \(s\), and no cross-depth epsilon product is evaluated.  If a
future observable needs a joint fast law at two depths, it must use the
appropriate independent product rule rather than infer correlation from
shared node labels.

Cost for the operator PDE is

\[
\text{memory}=O(NMRP),
\qquad
\text{RHS}=O(NMR(Pm+P)+NMPm),
\tag{19}
\]

where \(N\) is the numerical depth grid, \(M\) the base quadrature,
\(R\) the fast quadrature, and \(P\) the operator order.  None is a network
width.
Here \(N\) is a residual/Riemann discretization of the physical depth BVP;
it is not the Legendre budget called \(N\) in the unimplemented response
compiler.

Use \(R=2^8,2^9,2^{10}\) and at least four independent scrambles.  Report
the scramble confidence interval separately from \(P\)-truncation.

### Route B: positive deterministic Gauss--Hermite characteristics

Use tensor Gauss--Hermite nodes for the intrinsic initial Gaussian and for
the fast row variables.  Push every positive-weight node along (18).
For the first nontrivial levels this is an unusually clean audit because:

- weights remain positive;
- mass is exact;
- mean and covariance are exact;
- the same nodes are used in \(W\) and \(W^\top\); and
- the result has no stochastic sampling error.

If the base latent has dimension \(r_0=m+1\), a tensor rule of order
\(q_b\) uses \(q_b^{r_0}\) base nodes.  A fast rule of order \(q_f\) uses
\(q_f^P\) nodes.  Thus this route is practical at degree-one Hermite order
\(P=m+2\), but not at large \(P\).

This is independent of Sobol QMC.  The \(m=3,P=5\) order-three rule has
\(3^4=81\) base nodes and \(3^5=243\) fast nodes.

### Route C: Hermite stochastic Galerkin of the characteristic map

The compiled initial law is often a low-intrinsic-dimensional Gaussian
pushforward even when its ambient state dimension \(D\) is large.  Write

\[
\xi(g,t)
\approx
\sum_{|\alpha|\le R}u_\alpha(t)H_\alpha(g),
\qquad
g\sim N(0,I_{r_0}).
\tag{20}
\]

Project the characteristic equation:

\[
\dot u_\alpha
=
\mathbb E\!\left[
H_\alpha(g)\,
b\!\left(
\xi_R(g);
\mathbb E[\Phi(\xi_R(g))],
\kappa
\right)
\right].
\tag{21}
\]

The number of coefficients is

\[
S(r_0,R)=\binom{r_0+R}{R}.
\tag{22}
\]

For the first persuasive \(m=2\) test, \(r_0=3\).  Degree \(R=5\) uses only
56 coefficients per transported coordinate.  A 9-point tensor
Gauss--Hermite projection uses 729 residual evaluations.  This method
evolves global polynomial coefficients rather than measure particles and
therefore gives an independent discretization error.

The supplied `liouville_solvers.py` implements both (18) and (21).  On the
analytic mean-field benchmark

\[
\dot x=-(x-\mathbb E x),\qquad x(0)=1+2g,
\]

both solvers had maximum \(T=1\) error \(2.79\times10^{-10}\) at
\(\Delta t=0.01\).  This only validates the generic solver mechanics; it is
not presented as neural-PDE evidence.

For the operator PDE one can instead expand the conditional density in the
fast \(c\)-variables,

\[
\eta(c\mid g,s,t)
=
\varpi(c)\sum_{|\alpha|\le R}d_\alpha(g,s,t)H_\alpha(c),
\]

and use the weak equation

\[
\dot d_\alpha
=
\mathbb E_\eta[\nabla H_\alpha(c)\cdot v_c].
\tag{23}
\]

An adaptive affine Gaussian reference is advisable after the distribution
moves away from its initialization.

### Direct Eulerian grid: useful only as a smoke test

A direct finite-volume grid in the response-PDE ambient coordinate is not
credible.  Even before derived tags, the response grammar has the lower
bound

\[
D_{\min}
=
1+2mN+2(K+1)m^2N.
\tag{24}
\]

For \(N=2\):

| \(m\) | \(K=0\) | \(K=1\) | \(K=2\) |
|---:|---:|---:|---:|
| 1 | 9 | 13 | 17 |
| 2 | 25 | 41 | 57 |
| 3 | 49 | 85 | 121 |

These are lower bounds: nonlinear slow tags can increase them.  A
16-point grid in \(D=13\) already has \(4.5\times10^{15}\) cells.  The
initial law can also be singular in ambient coordinates, so artificial
Eulerian diffusion is dangerous.  Tensor-train or sparse spectral methods
may eventually be useful, but a plain grid is not a serious first route.

## 4. Lowest-dimensional tests

There are two different notions of “lowest.”

### Solver smoke test

\[
m=1,\quad P=3\ \text{(constant, input coordinate, readout coordinate)},
\quad N=8.
\]

The immutable latent has dimension two and the conditional fast PDE has
three learned coefficient coordinates.  This is computationally tiny and
does exercise dense \(W/W^\top\) reuse.  It has only one Gram scalar, so it
is not persuasive evidence for the project.

### First scientifically persuasive test

\[
\boxed{
m=d=2,\quad
X=I_2,\quad
y=(0.8,-0.55),\quad
P=4,\quad N=16.
}
\tag{25}
\]

The degree-one basis contains the constant, both input coordinates, and the
readout coordinate.  It predicts a nontrivial off-diagonal hidden Gram.
A positive tensor rule with \(q_b=5,q_f=3\) uses

\[
5^3\times3^4=10{,}125
\]

nested nodes per depth cell.  The CPU prototype ran to \(T=4\) in about
25 seconds.

### Central three-sample test

For the conjecture's \(m=d=3\) instance, degree one gives \(P=5\).  The
\(3^4\times3^5\) deterministic rule has 19,683 nested nodes per depth cell
and is still practical.  Higher total degrees have
\[
P=5,\ 15,\ 35
\]
at degrees one, two, and three, so fast QMC is required beyond the first
level.

## 5. Exact dense reference matching protocol

The PDE is deterministic.  It must be compared with an ensemble estimate of
the ordered target

\[
n\to\infty\quad\text{at each fixed }L,
\qquad\text{then}\qquad L\to\infty.
\tag{26}
\]

A single \(n=64,L=16\) trajectory is not a valid reference.

### Frozen grid

For the \(m=2\) pilot, use

\[
L\in\{8,16,32,64\},
\qquad
n\in\{64,128,256,512\}.
\]

Allocate more seeds at small width to equalize uncertainty, for example
\[
S_n=(256,128,64,32).
\]

At every fixed \(L\), fit each time/depth observable to both

\[
O_{n,L}=O_{\infty,L}+a_L/n
\]

and

\[
O_{n,L}=O_{\infty,L}+a_L/n+b_L/n^2.
\]

Use an omitted width as a held-out check and a simultaneous bootstrap of
the complete curve.  Only after this width extrapolation fit

\[
O_{\infty,L}
=
O_{\infty,\infty}+c/L+d/L^2.
\tag{27}
\]

The \(1/L\) term is not arbitrary: the paired-\(W\) diagnostic below
measures precisely this scaling.

### What to compare

On a common dense time/depth check grid, record

\[
\max_t\|f_{\rm PDE}-f_{\rm ref}\|_2,
\]

\[
\max_{t,s}\|G^h_{\rm PDE}(s,t)-G^h_{\rm ref}(s,t)\|_F,
\]

\[
\max_t\|\Theta_{\rm PDE}(t)-\Theta_{\rm ref}(t)\|_F.
\]

Loss is secondary near interpolation.  The same fixed PDE must run through
an audit-fixed plateau horizon.  Separately report:

1. time-integration error;
2. base quadrature error;
3. fast quadrature error;
4. operator-order \(P\) error;
5. depth discretization error;
6. finite-width reference error;
7. finite-depth reference error; and
8. ensemble sampling uncertainty.

The PDE process must never import a reference curve.

## 6. Prototype results and audits

### 6.1 Actual PDE behavior

The \(m=2,P=4,N=16\), positive-cubature PDE run gave

| quantity | value |
|---|---:|
| initial loss | \(4.7125\times10^{-1}\) |
| loss at \(T=4\) | \(1.0141\times10^{-13}\) |
| maximum all-depth Gram motion | \(5.8081\times10^{-1}\) |

Thus the PDE itself—not a finite \(W\)-matrix surrogate—fits and displays
substantial nonlazy feature motion.

The independent central \(m=3,P=5,N=16\) deterministic-GH run in
`dense_mup_pde_repro` gave:

| quantity | value |
|---|---:|
| initial loss | \(5.3250\times10^{-1}\) |
| loss at \(T=8\) | \(3.4802\times10^{-25}\) |
| maximum all-depth Gram motion | \(6.4819\times10^{-1}\) |
| minimum sampled \(\lambda_{\min}(\Theta^P)\) | \(2.7062\) |
| minimum retained Hermite energy of \(h\) | \(0.999974\) |

The high projected-energy fraction is evidence that the slow hidden fields
remain close to the immutable-latent Hermite span at this first level.  It
is not a proof of convergence.

### 6.2 Independent implementation agreement

My `operator_hermite_pde.py` and the independently developed
`dense_mup_pde_repro/src/dense_pde/operator_galerkin.py` use different code
but the same equations.  For

\[
m=3,\quad P=5,\quad N=16,\quad
M=3^4=81,\quad R=3^5=243,\quad
\Delta t=0.02,
\]

their common-grid discrepancies through \(T=1\) were:

| observable | maximum difference |
|---|---:|
| output coordinates | \(2.78\times10^{-16}\) |
| every time/depth Gram entry | \(8.88\times10^{-16}\) |

This is strong evidence that the displayed PDE has been implemented
correctly twice.  It says nothing by itself about the dense-limit model
error.

### 6.3 Algebraic audits

The independent prototype passes:

- weighted finite-difference gradients for \(B,a,c\), including the depth
  metric factor for \(c\);
- the exact shared-operator pairing
  \(\langle W_Pu,v\rangle=\langle u,W_P^\top v\rangle\);
- a directional finite-difference check of
  \(\dot f=-\Theta^Pe\);
- positive semidefiniteness of \(\Theta^P\); and
- a numerical restart/semigroup split from a copied complete state.

All four automated tests pass.

### 6.4 Conditional fast variance: the main homogenization diagnostic

At width \(n=128\), for each \(L\), 24 pairs shared \(B(0),a(0)\) and
independently redrew every \(W_\ell(0)\).  They were then trained
independently with the same data.  The two statistics were

\[
\frac{1}{2nm}\|H_L-H_L'\|_F^2.
\]

\[
\frac{1}{2nm}\|P_0-P_0'\|_F^2.
\]

| \(L\) | \(H_L,t=0\) | \(P_0,t=0\) | \(H_L,t=0.5\) | \(P_0,t=0.5\) |
|---:|---:|---:|---:|---:|
| 8 | \(0.031556\pm0.000652\) | \(0.034066\pm0.001164\) | \(0.037548\pm0.000686\) | \(0.045198\pm0.001534\) |
| 16 | \(0.014904\pm0.000284\) | \(0.016544\pm0.000506\) | \(0.017835\pm0.000322\) | \(0.022043\pm0.000677\) |
| 32 | \(0.007647\pm0.000192\) | \(0.007961\pm0.000311\) | \(0.009212\pm0.000195\) | \(0.010792\pm0.000357\) |
| 64 | \(0.003740\pm0.000083\) | \(0.004320\pm0.000171\) | \(0.004601\pm0.000122\) | \(0.005791\pm0.000172\) |

The fitted log-log slopes are

\[
\begin{array}{c|cc}
&t=0&t=0.5\\ \hline
H_L&-1.0193&-1.0039\\
P_0&-0.9993&-0.9924
\end{array}.
\]

This is unusually clean evidence that fast iid-depth randomness contributes
only \(O(L^{-1/2})\) forward/adjoint fluctuations and \(O(L^{-1})\)
conditional variance, even after feature learning has begun.  It directly
supports both sides of the slow-latent premise behind (9)--(10).

### 6.5 Numerical convergence of the \(m=2\) PDE

All entries below are full-curve maxima through \(T=4\), including every
depth Gram:

| comparison | output | Gram |
|---|---:|---:|
| whitened QMC \(R=256\) vs \(R=512\), \(P=4\) | \(3.42\times10^{-4}\) | \(5.30\times10^{-4}\) |
| \(P=4\) vs \(P=10\), whitened QMC \(R=256\) | \(7.93\times10^{-4}\) | \(1.05\times10^{-3}\) |
| \(P=4\) vs \(P=10\), whitened QMC \(R=512\) | \(5.69\times10^{-5}\) | \(4.19\times10^{-4}\) |
| \(P=10\), whitened QMC \(R=256\) vs \(R=512\) | \(5.43\times10^{-4}\) | \(9.45\times10^{-4}\) |
| GH order 3 vs 4, \(P=4\) | \(1.319\times10^{-2}\) | \(2.647\times10^{-2}\) |
| GH order 4 vs 5, \(P=4\) | \(5.66\times10^{-3}\) | \(1.078\times10^{-2}\) |
| whitened QMC \(R=512\) vs GH order 5 | \(1.75\times10^{-3}\) | \(3.27\times10^{-3}\) |

Changing the base GH order from 4 to 5 at fixed fast GH order 3 changed
outputs by \(1.71\times10^{-4}\) and Grams by \(2.36\times10^{-4}\).
Thus the dominant deterministic-cubature error was the fast row integral,
not the base latent integral.

Raw scrambled-normal Sobol \(R=256,P=4\) had maximum mean error
\(9.16\times10^{-4}\) and covariance operator error \(2.02\times10^{-2}\).
The reported “whitened QMC” results use a fixed, pre-curve
center-and-whiten correction so these first two moments are exact.  Higher
Gaussian moments still require \(R\)-refinement.

The QMC and GH sequences are converging toward one another, but a
\(3.3\times10^{-3}\) cross-method Gram discrepancy remains.  This is a
numerical uncertainty, not a model error.

### 6.6 Current dense-reference comparison is unresolved

For \(m=2,L=16\), the large pilot ensemble used:

| width | seeds | maximum output SE per coordinate | maximum Gram-entry SE |
|---:|---:|---:|---:|
| 64 | 128 | \(1.09\times10^{-2}\) | \(1.78\times10^{-2}\) |
| 128 | 96 | \(9.17\times10^{-3}\) | \(1.36\times10^{-2}\) |
| 256 | 48 | \(1.04\times10^{-2}\) | \(1.30\times10^{-2}\) |

Against the \(n=256\) ensemble mean, the \(P=4\) PDE had maximum output
and all-depth Gram gaps \(1.54\times10^{-2}\) and
\(2.62\times10^{-2}\).  These are comparable to:

- ensemble uncertainty;
- the measured \(L=16\) conditional fast variance; and
- the lower-order fast quadrature discrepancy.

Therefore this pilot neither confirms nor refutes dense-limit accuracy.
The correct width-then-depth extrapolation in Section 5 is mandatory.

## 7. Recommended execution order

1. **Use the explicit operator PDE now.**  It is the only route currently
   possessing a fully explicit drift and an actual width-independent run.
2. **Freeze the cofinal family.**  Use total-degree Hermites
   \(P=5,15,35,\ldots\) for the central \(m=3\) case and
   \(N=8,16,32,\ldots\).  Keep \(M,R,\Delta t\) as separate solver
   resolutions.
3. **Finish solver convergence before model comparison.**  Require two
   independent methods (whitened randomized QMC and deterministic GH at the
   first level), three \(R\)'s, three time steps, and three depth grids.
4. **Build the ordered dense reference.**  Extrapolate width at each fixed
   depth, then extrapolate depth, with simultaneous curvewise confidence
   bands.
5. **Run through an audit-fixed plateau.**  Keep \(P,N\) fixed through the
   whole trajectory.
6. **Only then make the scientific claim.**  If error shrinks with \(P,N\)
   and is larger than neither solver nor reference uncertainty, this is
   direct numerical evidence for an accuracy-dependent finite neural PDE.
7. **In parallel, implement the response compiler.**  The generic
   characteristic and Hermite-map solvers are ready, but the response
   conjecture's finite drift must first be emitted.  Operator-Galerkin
   success does not automatically prove convergence of the specific
   \((K,J,N)\) response family.

The operator route is more than a rebranding of the old matrix-response
experiment: it actually simulates a finite autonomous Liouville PDE with no
network-width state.  The honest present conclusion is that the PDE can now
be run and behaves nontrivially; convergence to the canonical dense
continuous-depth limit remains the next numerical question.

## 8. Files produced in this audit

- `agent_outputs/numerics/operator_hermite_pde.py`  
  Independent operator-Galerkin PDE and nested characteristic solver.
- `agent_outputs/numerics/test_operator_hermite_pde.py`  
  Gradient, transpose, tangent-kernel, and restart audits.
- `agent_outputs/numerics/liouville_solvers.py`  
  Generic tensor-GH, Sobol-characteristic, and Hermite-map solvers.
- `agent_outputs/numerics/paired_w_variance.py`  
  Reproduction code for the forward/adjoint conditional fast-variance
  experiment.
- `agent_outputs/numerics/paired_W_conditional_variance_hp.csv`  
  The four-depth forward/adjoint variance table above.
- `agent_outputs/numerics/exact_m2_reference.py`  
  Reproduction code for the \(m=2,L=16\) width ensemble.
- `agent_outputs/numerics/exact_m2_L16_width_ensemble_large.npz`  
  The 128/96/48-seed reference summaries.
- `agent_outputs/numerics/operator_pde_m2_*.npz`  
  Raw \(m=2\) PDE traces for GH/QMC, \(P=4,10\), and the listed
  refinements.
- `agent_outputs/numerics/operator_pde_m3_P5_N16_GH3_T1.npz`  
  Independent central-run trace used for the machine-precision
  cross-implementation check.
