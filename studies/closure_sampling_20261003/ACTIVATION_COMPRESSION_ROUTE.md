# Compression for a concrete class of bounded analytic activations

2026-10-03. Scoped activation-axis derivation. Inputs are exactly the five
assigned two-input/complex notes, the maintained notation contract, and the
manuscript setting and activation assumptions. No other route, verdict,
study, experiment, or Git operation is an input. This is internally derived
research, not an independent promotion review. Canonical-notation,
rigorous-proof and conjecture-audit instructions apply.

The independent route is frozen in this file before receiving any other
axis's mathematical findings. Its central conclusion is a verified sufficient
activation class, not a claim that analyticity is necessary for every possible
compression algorithm.

## 1. Contract, activation class, and conclusion

Fix input dimension d>=2, two orthogonal training inputs
\(x_a=\sqrt d\,e_a\), a=1,2, and two hidden layers of width n. For
\(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\),
\(w\in\mathbb R^n\), the forward pass is

\[
 h(x)=\phi_1(Ax/\sqrt d),\qquad z(x)=Wh(x),\qquad
 g(x)=\phi_2(z(x)),\qquad f_n(x)=w^\top g(x)/n.
 \tag{1}
\]

Initially A has iid standard Gaussian entries, W has iid N(0,1/n)
entries independently, and w=0. The loss is
\(\mathcal L=\tfrac12\sum_{a=1}^2(f_n(x_a)-y_a)^2\), with block
mobilities (n,1,n). Write \(r_a=f_n(x_a)-y_a\) and
\(c_a=-r_a=y_a-f_n(x_a)\). Thus c is the negative residual used in
the assigned notes. Let \(Y=|y|\).

The sufficient activation hypotheses are:

1. Each \(\phi_\ell\) is real on the real axis and has a bounded
   holomorphic extension to a fixed strip \(|\Im z|<b_\ell\).
2. \(\phi_1'(x)>0\) for every real x; \(\phi_2\) is nonconstant.

Bounds and strip widths are fixed independently of n. Fixed activations and
their derivatives are given data, as tanh was in the original construction.
There is no hypothesis about regularity of a learned response. In particular
there is no uniform positive lower bound on \(\phi_1'\).

**Conclusion.** There are activation- and d-dependent constants
\(Y_*,C>0\) such that, for each fixed \(|y|\le Y_*\), fixed
\(0<\eta<1/2\), and sufficiently large n, an initialization-only
construction gives an autonomous positive-weight network with its own
residuals and evolving hidden matrix such that, with probability at least
\(1-\eta\),

\[
 \sup_{0\le t\le\infty}\sup_{|x|=\sqrt d}
       |f_C(t,x)-f_n(t,x)|\le Cn^{-1/2}.
 \tag{2}
\]

The total moving and fixed real-coordinate storage after setup is at most

\[
 C[\log(en/\eta)]^{6d+4}.
 \tag{3}
\]

For d=2 this is the original exponent 16 and the full circle. Setup may
use arbitrarily large finite initial-derivative calculations and exact real
arithmetic; efficient or well-conditioned preprocessing is not claimed.
Both networks continue autonomously for all time and fit. All signs and
ratios of the two labels are allowed. Zero labels give the stationary zero
readout. For each fixed nonzero small y, both hidden feature layers have
RMS displacement at least \(cY^2\) at one fixed positive physical time,
with probability tending to one; the same holds in the compressed weighted
norms for sufficiently large n. Section 7 proves this for the full stated
class, including nonodd sigmoid activations.

## 2. Uniform inverse strip without a lower slope bound

Define the real coordinate and its real inverse by

\[
 \Psi(a)=\int_0^a\frac{dv}{\phi_1'(v)},\qquad
 \psi=\Psi^{-1},\qquad \sigma=\phi_1\circ\psi.
 \tag{4}
\]

Because \(0<\phi_1'\le M\), the map \(\Psi\) is strictly increasing
and tends to both infinities, so its inverse exists on all of R.
On the real axis,

\[
 \psi'(u)=\phi_1'(\psi(u)),\qquad
 \sigma'(u)=\phi_1'(\psi(u))^2.
 \tag{5}
\]

Here is a complete uniform holomorphic extension argument. Choose
\(0<b<b_1/4\). Cauchy's integral formula on disks inside the original
strip bounds \(\phi_1'\) and \(\phi_1''\) by fixed constants
\(M_1,M_2\) on \(|\Im a|\le2b\). For any real \(u_0\), put
\(a_0=\psi(u_0)\), and solve on \(|v|\le\rho\)

\[
 A(v)=a_0+\int_0^v\phi_1'(A(s))\,ds,
 \qquad \rho M_1\le b/2,\quad \rho M_2\le1/2.
 \tag{6}
\]

The integral follows the straight segment. On the closed sup-norm ball
of holomorphic functions with \(\sup|A-a_0|\le b\), its right side
preserves that ball and contracts by at most 1/2. Iterating from the
constant function gives a uniformly convergent holomorphic solution;
the same contraction proves uniqueness. On the real interval it equals
the real inverse in (4), by differentiating (4) and uniqueness of the
real integral equation. Two disks with real centers have connected
intersection containing a real interval. Their solutions agree there and
therefore agree on the intersection: the difference has a Taylor expansion
at a real accumulation point, and its first nonzero coefficient would
contradict its accumulating zeros. Thus all disks patch to a single
holomorphic \(\psi\) on \(|\Im u|<\rho\).

In particular,

\[
 |\Im\psi(u)|\le M_1|\Im u|,\qquad
 |\psi'(u)|\le M_1,\qquad |\sigma(u)|\le C.
 \tag{7}
\]

The first inequality follows by integrating (5) vertically from the real
axis. Cauchy estimates on smaller u-strips bound every fixed number of
derivatives of \(\psi'\) and \(\sigma\). The function \(\psi\) itself
need not be bounded on the whole strip. No complex primitive of
\(1/\phi_1'\), no complex zero-free strip for that derivative, and no
univalence assertion for a complex extension of \(\Psi\) are required.
Equation (6) is the inverse construction even if complex zeros of
\(\phi_1'\) approach the real axis at large real part.

For \(a_a=Ae_a\), \(u_a=\Psi(a_a)\), define training features
\(h_a=\sigma(u_a)\), \(z_a=Wh_a\), \(g_a=\phi_2(z_a)\),
\(\delta_a=w\odot\phi_2'(z_a)\), and \(k_a=W^\top\delta_a\).
The exact physical equations are

\[
 \dot u_a=c_ak_a,\qquad
 \dot W=\frac1n\sum_b c_b\delta_bh_b^\top,
 \qquad \dot w=\sum_b c_bg_b.
 \tag{8}
\]

The columns \(Ae_j\), j>2, remain at initialization. Thus the same
regular-coordinate vector fields used for tanh have no diagonal carrier
in their first-state Jacobian. The only replacements are
\(\tanh\to\phi_\ell\), \(\operatorname{sech}^2\to\phi_\ell'\),
and \(\operatorname{sech}^4a\to\phi_1'(a)^2\).

## 3. Initialization Gram and all-time real geometry

Let Z be standard normal, \(\mu=E\phi_1(Z)\), and
\(v=\operatorname{Var}(\phi_1(Z))>0\). Positivity holds because
\(\phi_1\) is strictly increasing and the Gaussian has full support.
The empirical initial lower-feature Gram converges to

\[
 Q=vI_2+\mu^2\mathbf1\mathbf1^\top\succ0.
 \tag{9}
\]

Conditional on A, the initial top-preactivation rows are independent
Gaussians with this empirical covariance. If \(Z_*\sim N(0,Q)\),
the limiting top-feature Gram is

\[
 G=E[\phi_2(Z_*)\phi_2(Z_*)^\top]\succ0.
 \tag{10}
\]

To prove the positive gap, a null quadratic form would give
\(b_1\phi_2(z_1)+b_2\phi_2(z_2)=0\) almost everywhere under a
strictly positive Gaussian density. Continuity makes the identity true
everywhere. Varying z_1 and z_2 separately, and nonconstancy of
\(\phi_2\), give b_1=b_2=0. On bounded covariance sets Gaussian
square-root representations and boundedness of \(\phi_2\) give
continuity of (10) by dominated convergence. Bounded-variable exponential
concentration at each layer therefore yields an initial gap
\(G_{0,n}\succeq\gamma I_2\) with exponentially small failure.
The Gaussian operator, coordinate-maximum, and RMS estimates are exactly
those in the assigned source proof, with activation-dependent constants.

For positive masses D_1,D_2 of total mass one, use the weighted adjoint
\(B^*=D_1^{-1}B^\top D_2\). The state is
\(x=(u_1,u_2,B,w)\), with the sum of the two D_1 norms, the weighted
Hilbert--Schmidt norm of B, and the D_2 norm of w. Equations (8), with
\(1/n\) replaced by the relevant masses, define the residual-free
field V_a. The bounded real functions \(\sigma,\sigma',\sigma''\)
and \(\phi_2,\phi_2',\phi_2''\) imply, on a small activity tube,

\[
 \|w\|_\infty\le CS,\quad
 \|B-B_0\|_{\rm HS}+\sum_a\|u_a-u_{a,0}\|_{D_1}\le CS^2,
 \quad \|DV_a\|\le C,
 \tag{11}
\]

where \(S=\int|c|\). For example \(\delta=w\phi_2'(z)\)
has a Lipschitz difference bounded by
\(C\|\Delta w\|+CS\|\Delta z\|\); the forward difference
\(\Delta z\) is bounded by the state difference. Products in the B
equation are rank one, and the u equation is just \(B^*\delta\).
This verifies the field derivative bound without a carrier maximum.

The fixed observation derivative L_0 uses the initial top features.
Its remainder is explicitly
\(N_a(x)=w^\top D_2(g_a-g_{a,0})\), so
\(\operatorname{Lip}(N)\le CS\), while
\(\|V_a-V_{a,0}\|\le CS\). The initial matrix
\(L_0V_0=G_{0,n}\) retains its positive gap.

Differentiating the residual gives \(\dot c=-Kc\), with

\[
 K_{ab}=g_a^\top D_2g_b
 +(\delta_a^\top D_2\delta_b)(h_a^\top D_1h_b)
 +\mathbf1_{a=b}\|\phi_1'(a_a)\odot B^*\delta_a\|_{D_1}^2.
 \tag{12}
\]

The second matrix is a tensor-product Gram and the last is nonnegative
diagonal. Hence the readout Gram alone supplies the gap. Its change is
O(S^2) by (11). The same first-exit argument as in the stable-geometry
note gives, for sufficiently small fixed Y,

\[
 |c(t)|\le Ye^{-\kappa t},\qquad
 \int_0^\infty|c|\,dt\le CY,
 \quad\|w\|_\infty\le CY,
 \quad\text{hidden displacement}\le CY^2.
 \tag{13}
\]

The signed-activity comparison lemma in that note applies with exactly
the verified constants above. Its proof uses only (11), the displayed
remainder N, and the gap; it never uses tanh parity. The singleton cavity
deletion sources are still an omitted column times one bounded feature,
or an omitted row times one bounded response. Thus its all-time cavity
comparisons survive unchanged: in the unnormalized (u_1,u_2,H,w) norm,
H=\sqrt nW, lower deletion costs CY and upper deletion costs
\(C(Y^2+Y/\sqrt n)\). Every cavity evolves with its own residuals and
is independent of the omitted Gaussian vector. Its initial Gram changes
by O(n^{-1/2}) or O(n^{-1}), so it also satisfies (13).

## 4. Actual complex sources: the activation-dependent checks

Put \(\ell=\log(en/\eta)\), \(T=B\ell\), and
\(r=c/\sqrt\ell\), with fixed B. The source rectangle is
\(-r\le\Re t\le T+r\), \(|\Im t|\le r\). We give the
estimates needed to transplant the full stopped-domain proof; no new
regularity hypothesis on the trained path is inserted.

Choose a fixed pole margin b so that \(|\Im u|\le2b\) lies in the
inverse strip from Section 2, and \(|\Im z|\le2b\) lies in the
top-activation strip. The functions and derivatives used in the equations
are bounded there. On an operator tube and \(\|w\|_\infty\le CY\),
the complex algebraic K in (12) has bounded norm: in its last term use
\(\sigma'(u)k_a^2\) and \(\|k_a\|_2/\sqrt n\le CY\).
Short vertical continuation from the real anchor \(\Re t\) therefore
gives

\[
 |c(t)|\le CYe^{-\kappa\max(\Re t,0)},\quad
 \|W\|_{\rm op}\le C,\quad
 \|w\|_\infty+\|\delta_a\|_\infty\le CY,
 \tag{14}
\]

\[
 \frac{\|k_a\|_2}{\sqrt n}\le CY,\quad
 \frac{\|\dot u_a\|_2+\|\dot h_a\|_2+\|\dot z_a\|_2}{\sqrt n}
 \le CY|c|,\quad
 \frac{\|\dot\delta_a\|_2+\|\dot k_a\|_2}{\sqrt n}\le C|c|.
 \tag{15}
\]

For example
\(\dot\delta_a=\dot w\phi_2'(z_a)+w\phi_2''(z_a)\dot z_a\).
Integrating rank-one coordinates gives learned row and column norms
\(CY^2/\sqrt n\), and learned entries \(CY^2/n\). The real
all-time cavity comparison supplies the anchor for a vertical comparison.
The finite differences verified after (11) apply to the endpoint safe
strips. They give full/cavity distance \(D_c\le CY\) on every common
stopped domain; no Gronwall factor is integrated over the long length T.

Define \(q_a=\sigma'(u_a)\odot k_a\), so \(\dot h_a=c_aq_a\)
without division by a residual. Set carrier caps
\(M=L=AY\sqrt\ell\). The reinsertion estimates are

\[
 |k_{a,i}-\xi_i^\top\delta_a^{-i}|\le CY,\qquad
 |(Wq_a)_j-\xi_j^\top q_a^{-j}|\le C(Y+YM),
 \tag{16}
\]

where \(\xi_i=W_{0,:,i}\), \(\xi_j^\top=W_{0,j,:}\). The second
bound follows from
\(\|q_a-q_a^{-j}\|_2\le C\|\Delta k_a\|_2+
C M\|\Delta u_a\|_2\le C(Y+YM)\), using bounded
\(\sigma''\). Cavity sources v=\(\delta_a^{-i}\) and
v=\(q_a^{-j}\) have RMS at most CY and derivative RMS at most
\(CY(1+YM)\), by differentiating their displayed formulas and (15).

Condition on A_0 and the retained initialization of each cavity. Its own
stop and reference values are then independent of the omitted Gaussian
vector. A polynomial-size grid of its own stopped rectangle, with mesh
\(n^{-3}/[C(1+YM)]\), controls interpolation. Real and imaginary
Gaussian tails give \(CY\sqrt\ell\) bounds for all pairings in (16)
after a union over grid points, two samples and 2n cavities. The log of
the total count is O(ell). References are set to zero if their retained
operator or initial Gram test fails; no full-network event is used in
the conditional Gaussian estimate.

The full caps therefore improve to

\[
 \max|k_a|\le C_GY\sqrt\ell+CY,
 \quad\max|Wq_a|\le C_GY\sqrt\ell+CY+CYM.
 \tag{17}
\]

Choose A large and then Y_* small. Since \(CYM/L=CY\), both
carrier caps improve strictly. Pole comparisons cost CY plus an
initialized entry \(C\sqrt{\ell/n}\); with Y_* small the cavity
double pole caps improve on every common prefix. Hence no cavity stops
first. Finally

\[
 \dot z_a=\sum_b c_b\delta_b(h_b^\top h_a/n)+c_aWq_a,
 \tag{18}
\]

so vertical integration over r bounds both imaginary u and z by
\(CY^2\sqrt\ell\,r=CY^2c\). Reducing c improves the full pole
caps. Uniform local Picard iteration on safe subdomains and the bounded
coordinate estimates extend past any alleged first stop. This proves the
full source rectangle for actual feedback dynamics. Holomorphic Picard
iteration here is the same contraction as (6), on a sufficiently small
finite-dimensional sup-norm ball; bounded local derivatives supply its
contraction constant. Compact boundary covers patch it by uniqueness.

## 5. Sphere queries and retained-space dimension

For d=2 use \(v(\theta)=(\cos\theta,\sin\theta)\). For general
fixed d use the spherical trigonometric map

\[
 v_1=\cos\theta_1,\quad
 v_j=\Big(\prod_{k<j}\sin\theta_k\Big)\cos\theta_j
 \ (2\le j<d),\quad
 v_d=\prod_{k<d}\sin\theta_k.
 \tag{19}
\]

It maps the real (d-1)-torus onto the unit sphere, including the pole
points, and is entire in every angle. Query inputs are x=\sqrt d v.
Set \(a_\theta=\sum_{j=1}^d(Ae_j)v_j(\theta)\) and
\(h_\theta=\phi_1(a_\theta)\). All frozen first-layer columns have
RMS O(1) and maxima O(\sqrt\ell), and the active ones retain these
bounds by (7), (13), and (17). Their imaginary maxima are at most
\(C b\). Choose b first small in terms of d and the first gate strip,
then \(|\Im\theta_j|\le c_d/\sqrt\ell\). Formula (19) and bounded
trigonometric derivatives put a_theta in a fixed safe first-gate strip.

The residual-free query derivative is

\[
 q_{\theta,a}=\phi_1'(a_\theta)\odot v_a(\theta)
                    \psi'(u_a)\odot k_a,\qquad
 \dot h_\theta=\sum_{a=1}^2c_aq_{\theta,a}.
 \tag{20}
\]

It has RMS CY. Each angular derivative of h_theta has RMS C and
coordinate size at most C\sqrt\ell. The derivatives needed for grids
(one time derivative of q and two angular derivatives of h) have bounds
polynomial in ell: they contain bounded gate derivatives, one carrier
of RMS CY and maximum M, and at most two initialized/active input
coordinates of maximum C\sqrt\ell. Row reinsertion differences are
\(C(Y+YM)\) for q and \(CY(1+\sqrt\ell)\) for angular derivatives,
by the same product differences used in (16).

Conditioning on each row cavity and using a grid in the 2d real
coordinates of complex time and angles is still polynomial in n for
fixed d. Its Gaussian bounds and reinsertion give

\[
 \max|Wq_{\theta,a}|+\max|W_0q_{\theta,a}|\le CY\sqrt\ell,
 \quad\max|\partial_{\theta_j}(Wh_\theta)|
       +\max|\partial_{\theta_j}(W_0h_\theta)|\le C\sqrt\ell.
 \tag{21}
\]

These bounds are proved before applying the query top activation.
Integrate from real time and real angles, first vertically in time and
then successively vertically in each angle. The imaginary query top
preactivation is at most \(CY^2c+C(d-1)c_d\), inside the top strip
after shrinking the radii. Thus g_theta is bounded and holomorphic.
Integrating real angular paths of bounded total length and the time
derivative against the finite residual integral gives
\(\max|W_0h_\theta|\le C\sqrt\ell\). Finally the exact identity

\[
 [(W(t)-W_0)^\top\delta_a(t)]_i
 =\int_0^t\sum_b c_b(s)h_{b,i}(s)
                    \delta_b(s)^\top\delta_a(t)/n\,ds
 \tag{22}
\]

bounds that correction by CY^3. Consequently the complete paired sources
\(h_\theta,g_\theta,W_0h_\theta,\delta_a,W_0^\top\delta_a\)
have the same complex bounds as in the assigned theorem: C\sqrt\ell
for source coordinates and fixed bounds for activation coordinates.

The initial-jet continuation and Chebyshev/Fourier construction in Section 4
of `TWO_INPUT_STABLE_GEOMETRY.md` now applies. Its proof uses only the
rectangle, the periodic strips, and the source bounds just proved. For
each extra angle repeat its Fourier interpolation step; allocate a fixed
fraction of the target error to each axis. Degrees are

\[
 p=O(\ell^{5/2}),\qquad L_j=O(\ell^{3/2}),\qquad
 r_1,r_2=O\!\left(\ell^{(3d+2)/2}\right).
 \tag{23}
\]

Indeed the number of coefficient vectors is at most
\((p+1)\prod_{j=1}^{d-1}(2L_j+1)\). Apply identical scalar operations
to each paired mixer source, so pairs of coefficients are exactly
\((v,W_0v)\) or \((d,W_0^\top d)\). Add the d initialized read-in
columns and the finitely many initialized training features needed for
exact initialization. Their number does not change (23).

## 6. Autonomous network and all-time error

Use positive cubature on products of bases of the two spaces in (23),
exactly as in `TWO_INPUT_CANONICAL_COMPRESSION.md`: select
\(N_i\le1+r_i(r_i+1)/2\) original neurons and positive masses D_i.
If normalized bases are V,U, define

\[
 C_0=U^\top W_0V/n,\qquad
 B_0=U_JC_0V_I^\top D_1.
 \tag{24}
\]

Cubature makes the sampled bases weighted isometries, so B_0 has norm
at most \(\|W_0\|\), matches both paired initial actions, and preserves
the initial training-feature Gram exactly. Initialize
\(A_C=(A_0)_I\), \(B_C=B_0\), \(w_C=0\). At runtime use (1)
with \(\phi_1,\phi_2\), weighted readout \(w_C^\top D_2g_C\), and

\[
 \dot A_C=\sum_{a=1}^2c_{C,a}
       [\phi_1'(A_Ce_a)\odot B_C^*\delta_{C,a}]e_a^\top,
 \quad B_C^*=D_1^{-1}B_C^\top D_2,
 \tag{25}
\]

\[
 \dot B_C=\sum_a c_{C,a}\delta_{C,a}h_{C,a}^\top D_1,
 \qquad \dot w_C=\sum_a c_{C,a}g_{C,a},\qquad
 \delta_{C,a}=w_C\odot\phi_2'(z_{C,a}).
 \tag{26}
\]

This stores dN_1+N_1N_2+N_2 moving coordinates and the two mass vectors,
labels, and fixed model data. Equations (23)--(24) give (3). Full source
arrays, original W, bases, initial jets, and all intermediate setup
coefficients are discarded. No trained snapshot enters setup.

To verify error transfer, define only in the proof the selected reference
matrix
\(B_R=B_0+\int\sum_a c_{n,a}\delta_{a,J}h_{a,I}^\top D_1\).
Positive cubature and uniform source error \(\varepsilon=Cn^{-1/2}\)
give forward defect \(\|B_Rh_{\theta,I}-z_{\theta,J}\|_{D_2}\le C\varepsilon\),
reverse defect \(\|B_R^*\delta_{a,J}-(W^\top\delta_a)_I\|_{D_1}
\le C\varepsilon\), and readout pairing error C epsilon. To check the
learned parts, expand B_R and W by their rank-one integral formulas;
the remaining terms are discrepancies of inner products of two sources,
integrated against c. Their coefficient bounds follow from (13).
Both sampled and empirical norms of an approximant agree by cubature,
and coordinate errors have norm at most epsilon because masses sum to one.
No minimum mass is used.

The selected regular reference state therefore has residual-free velocity
defect \(C\varepsilon|c_n|\) and observation defect C epsilon. Its
hidden displacement is O(Y^2+Y epsilon), by the reverse defect. The
signed-activity stability lemma applies using Section 3 and the exact
initial Gram. It gives same-physical-time state error C epsilon through
T, independent of T. Query forward maps are uniformly Lipschitz in the
weighted state norm by (7), bounded activations, and fixed |x|; hence
query error is C epsilon uniformly on the sphere. Each autonomous model
has a sphere-query tail \(CYe^{-\kappa t}\), by (13). Taking B large
enough makes the tail after T at most epsilon and proves (2), including
the fitted endpoint. No statement here replaces signed residual histories
by a path-independent vector activity.

## 7. Feature learning without oddness or positive label signs

The first-layer feature certificate in the assigned feature note uses
oddness for its particular test matrix. That proof cannot simply be reused
for sigmoid. The following replacement handles the full class above.

Assume \(\|W_0\|\le K\). For \(0\le t\le1\), the same real
estimates as in that note, using only bounded gates, give

\[
 \|w-tv\|_2/\sqrt n\le CYt^2,\quad
 \|u_a-u_{a,0}\|_2/\sqrt n\le CY^2t^2,
 \quad v=\sum_b y_bg_{b,0},
 \tag{27}
\]

\[
 \left\|u_a-u_{a,0}-\frac{t^2}{2}y_a k_a^v\right\|_2/\sqrt n
 \le CY^2t^3,\qquad
 k_a^v=W_0^\top[v\odot\phi_2'(z_{a,0})].
 \tag{28}
\]

The RMS upper bounds for each feature displacement are CY^2t^2.
We construct bounded initialized tests for the lower bound.

Let H have columns h_{1,0},h_{2,0}, Z=W_0H, and
\(P=H(H^\top H)^{-1}H^\top\). The inverse exists on the event
\(H^\top H/n\succeq q_0I\), whose probability tends to one by (9).
Conditionally on A_0,Z (and hence on H,Z), Gaussian row decomposition gives

\[
 W_0=Z(H^\top H)^{-1}H^\top+n^{-1/2}G(I-P),
 \tag{29}
\]

where G has iid standard Gaussian entries independent of H,Z. To verify
this, decompose each isotropic Gaussian row into its orthogonal projections
onto the column space of H and its orthogonal complement. Their covariance
cross terms vanish, so the joint Gaussian density factors after orthogonal
coordinates; the parallel projection is fixed by W_0H=Z.

Define the two response columns
\(d_{a,b}=g_{b,0}\odot\phi_2'(z_{a,0})\), b=1,2. Their empirical
Gram matrices converge to positive definite limits. Indeed their limiting
quadratic form is

\[
 E\left[\phi_2'(Z_{*,a})^2
          \left(\sum_b v_b\phi_2(Z_{*,b})\right)^2\right]>0
 \quad(v\ne0).
 \tag{30}
\]

The derivative of a nonconstant holomorphic function is not identically
zero and its real zeros are isolated: a nonisolated zero set contradicts
the first nonzero Taylor coefficient. Thus its zeros have Gaussian
probability zero. A zero in (30) would consequently force the same
impossible continuous linear relation used in (10). Conditional bounded
concentration gives, simultaneously in a,
\((d_{a,b}^\top d_{a,c}/n)_{bc}\succeq\mu_0I\) with high probability.

For a unit label direction \(\widehat y=y/Y\), set
\(d_a=\sum_b\widehat y_bd_{a,b}\) and
\(\zeta_a=W_0^\top d_a=k_a^v/Y\). From (29),

\[
 \zeta_a=m_a+(I-P)\xi_a,\quad
 m_a=H(H^\top H/n)^{-1}Z^\top d_a/n,\quad
 \xi_a=G^\top d_a/\sqrt n.
 \tag{31}
\]

The coordinates of m_a have absolute bound C, since H is coordinatewise
bounded, its Gram inverse is bounded, Z has bounded RMS, and d_a is
bounded. Conditionally the coordinates of xi_a are independent Gaussians
with common variance \(\|d_a\|_2^2/n\in[\mu_0,C]\). For the four
fields indexed by a,b this joint covariance is bounded, and
\(E\|P\xi_{a,b}\|_2^2/n\le C/n\), because P has rank two.
Thus removing P changes any weighted empirical average of a Lipschitz
function by o(1), simultaneously for all unit label directions.

Fix R>0, and let \(\chi_{a,i}=\mathbf1_{|a_{a,0,i}|\le R}\).
A fixed positive fraction of these indicators equal one with high
probability. On those coordinates
\(\sigma'(u_{a,0,i})=\phi_1'(a_{a,0,i})^2\ge c_R>0\), by
strict positivity and compactness. The scalar function F(z)=z tanh z is
nonnegative and has bounded derivative. Uniformly for |m|<=C and
\(s^2\in[\mu_0,C]\),
\(E F(m+sZ)\ge c>0\): the expectation is positive for every such
pair, continuous by a common integrable Gaussian majorant, and its
parameter set is compact. Conditional independence and bounded second
moments give a variance O(1/n) for its weighted empirical average.
Consequently, with probability tending to one,

\[
 \frac1n\sum_i\chi_{a,i}\sigma'(u_{a,0,i})
                  \zeta_{a,i}\tanh\zeta_{a,i}\ge c_0>0
 \quad(a=1,2)
 \tag{32}
\]

uniformly over unit label directions. For detail on uniformity, choose
a finite delta-net of the unit circle. Conditional Chebyshev proves (32)
at all its points. The empirical Lipschitz constant in the direction is
bounded by the RMS norms of the finitely many carrier fields in (31),
which are bounded with probability tending to one by conditional Gaussian
square-moment concentration and the bounded means. Choose fixed delta sufficiently
small to transfer a strict positive half-margin to the entire circle.
Projection removal costs o(1) by Cauchy--Schwarz and the rank-two bound.

Use the initialized bounded test

\[
 b_{a,i}=\widehat y_a\chi_{a,i}\tanh\zeta_{a,i},\qquad
 |b_{a,i}|\le1.
 \tag{33}
\]

Taylor expansion of sigma with bounded second derivative, followed by
(28), gives

\[
 \sum_a\frac{b_a^\top(h_a(t)-h_{a,0})}{n}
 =\frac{t^2Y^2}{2}\sum_a\widehat y_a^2
     \frac1n\sum_i\chi_{a,i}\sigma'(u_{a,0,i})
                    \zeta_{a,i}\tanh\zeta_{a,i}
 +O(Y^2t^3+Y^4t^4).
 \tag{34}
\]

The nonlinear remainder is controlled in normalized L1 by
\(C\|u_a-u_{a,0}\|_2^2/n\), so no fourth moment of the trained
increment is required. Choose fixed t_*>0 and Y_* small; (32)--(34)
and Cauchy--Schwarz prove

\[
 \left(\sum_a\|h_a(t_*)-h_{a,0}\|_2^2/n\right)^{1/2}
 \ge cY^2.
 \tag{35}
\]

For second-layer motion, the argument in Section 5 of the assigned feature
note now applies without parity: its only initial requirements are a positive
lower-feature Gram and the two positive matrices (30), already verified.
For completeness, keep v from (27) fixed, put
\(d_a^v(t)=v\phi_2'(z_a(t))\), \(K_a^v=W^\top d_a^v\), and
\(P_g(t)=\sum_a y_av^\top(g_a(t)-g_{a,0})/n\). Current gates give
\(\delta_a=t d_a^v+O_{\rm RMS}(Yt^2)\). Direct differentiation yields

\[
 \dot P_g(t)=t\left\|\frac1n\sum_a y_ad_a^v h_a^\top\right\|_F^2
 +t\sum_a y_a^2\|\phi_1'(a_a)\odot K_a^v\|_2^2/n
 +O(Y^4t^2).
 \tag{36}
\]

Both main terms are nonnegative. The first is at least cY^4t: the
lower-feature Gram keeps a fixed gap, and (30) plus the O(Y^2t^2)
feature displacement keeps \(\|d_a^v\|_2^2/n\ge cY^2\).
The tensor-product Gram identity gives the stated lower bound for every
sign pattern. Integrating to a sufficiently small fixed t_* and using
\(\|(y_av)_a\|_{\rm RMS}\le CY^2\) proves the analogue of (35)
for g. The feature upper bounds from (27) show both layers move on scale
Y^2. The initialization event and t_* are independent of label direction.

Positive cubature approximates squared feature displacements at t_* with
error O(n^{-1/2}), and the own-dynamics comparison gives weighted feature
error O(n^{-1/2}). Therefore the same cY^2 lower bounds transfer to the
compressed model for each fixed nonzero Y at sufficiently large width.
No assumption about a fitted-endpoint displacement is made.

## 8. Explicit examples and the smoothness boundary

The following first activations satisfy every hypothesis, with arbitrary
fixed real offset c, positive amplitude a, positive scale b, and real shift s:

\[
 c+a\tanh(bx+s),\qquad c+a\operatorname{erf}(bx+s),\qquad
 c+a\arctan(bx+s).
 \tag{37}
\]

The logistic sigmoid is included through
\((1+e^{-x})^{-1}=[1+\tanh(x/2)]/2\). Any finite positive sum of
the nonconstant terms in (37), with another real offset, is also admissible.
This supplies a substantive family beyond affine reparameterizations of tanh.
Independent choices can be made in the two layers. At the top one may also
use sine or any other bounded strip-holomorphic nonconstant real function;
strict monotonicity is only needed for the first-layer regular coordinate.

Here are direct complex checks. Tanh has no poles on a strip narrower
than pi/2, and its magnitude is bounded there by its expression in
\(e^{2z}\); for example \(|\tanh z|\le1\) on \(|\Im z|\le\pi/4\).
Arctan is the primitive of \(1/(1+z^2)\) in \(|\Im z|<1\), real
on R. For fixed b<1, vertical integration and
\(|1+(x+iv)^2|\ge1-v^2\) give
\(|\arctan(x+iy)|\le\pi/2+b/(1-b^2)\).
The entire error function is defined by
\(\operatorname{erf}z=(2/\sqrt\pi)\int_0^z e^{-s^2}ds\).
On \(|\Im z|\le b\), vertical integration gives

\[
 |\operatorname{erf}(x+iy)|
 \le1+(2/\sqrt\pi)|y|e^{y^2}e^{-x^2}
 \le1+(2/\sqrt\pi)b e^{b^2}.
 \tag{38}
\]

Their real derivatives are respectively sech^2 x, 2e^{-x^2}/sqrt(pi),
and 1/(1+x^2), all strictly positive. Shifts, positive rescalings and
finite positive mixtures preserve bounded strip holomorphy and positivity.
Sine is bounded by cosh(b)+sinh(b) on a fixed strip. This verifies the
examples directly; no guessed analyticity of a trained inverse is needed.

The paper's actual all-time assumptions are weaker than this route's:
`paper/results.tex`, theorem `thm:alltime`, requires C1 activations with
globally bounded and globally Lipschitz first derivative. Values may be
unbounded; softplus, GELU, SiLU and softsign are listed. The all-time
proof starts from bounds on phi(0), phi', and Lip(phi'). Neither it nor
its finite-order closure estimate supplies exponential source approximation.
Our conclusion is an additional theorem on a verified narrower activation
class, not a reinterpretation of that broad theorem as polylog storage.

Even C-infinity with every derivative bounded does not imply a
polylogarithmic Fourier approximation bound. To see this, define the
2pi-periodic real function

\[
 F(\theta)=\sum_{k=1}^\infty
      e^{-[\log(k+1)]^2}\cos(k\theta).
 \tag{39}
\]

For every fixed integer j, the derivative series converges absolutely:
eventually \(k^j e^{-[\log(k+1)]^2}\le k^{-2}\). Thus F is smooth
with bounded derivatives of every order. For any trigonometric polynomial
P of degree L, its Fourier coefficient at L+1 vanishes, while that of
F is \(\tfrac12e^{-[\log(L+2)]^2}\). Since each Fourier coefficient
is bounded by the uniform norm,

\[
 \|F-P\|_\infty\ge\tfrac12e^{-[\log(L+2)]^2}.
 \tag{40}
\]

Accuracy n^{-1/2} therefore requires
\(L\ge\exp(c\sqrt{\log n})\), exceeding every fixed power of log n.
This is a rigorous obstruction to obtaining the needed generic source
approximation lemma from qualitative smoothness alone. It is not a
counterexample to every autonomous compression of a smooth network.

The initialization-jet construction has another specific boundary:
nonzero smooth flat functions can have all derivatives zero at a point
(for example e^{-1/t^2} for t>0, extended by zero for t<=0). Hence an
entire trajectory cannot in general be recovered from its initial jets
without a uniqueness principle stronger than smoothness. Analyticity is
one sufficient principle. Quantified nonanalytic classes such as suitable
Gevrey classes could in principle permit stretched-exponential polynomial
approximation and still polylog degrees, but the initial-jet continuation
and actual-network uniform derivative bounds would need a new proof.
No necessity claim for analyticity, no extension to every paper activation,
and no impossibility claim for alternative smooth-activation algorithms is
made here.

## 9. Audit and claim boundary

The verified extension is orthogonal two-input, fixed finite d, two hidden
layers, fixed sufficiently small labels, and unrestricted exact-real setup.
The initialized Gram is derived for nonodd activations. The inverse strip
is proved with uniform constants despite saturation. Real all-time
stability, autonomous cavities, conditional Gaussian domains, query top-gate
ordering, paired forward/reverse approximation, and both feature-motion
certificates have explicit checks above. Constants can deteriorate with the
chosen activation, and the sufficiently-large-width threshold may depend
on the fixed nonzero label magnitude and confidence.

Analytic but unbounded activations and first activations with real derivative
zeros are outside this proof. An entire activation alone does not establish
the needed bounded-strip estimates. Merely smooth activation hypotheses do
not justify the polylog source-space bound. These are boundaries of the
present witness and proof, not general compression lower bounds. Nothing
in this file resolves nonorthogonal data or additional hidden depth.
