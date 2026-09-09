# One nonlinear activation for all two-sample inputs with a fixed separation

Extension proof, 2026-09-07. Review status is recorded separately in
REVIEW_STATUS.md. This document proves the new uniformity
step and verifies the premises of the attached population construction
and observable lemmas. Those mathematical lemmas, not their historical
review outcomes, are the dependencies of this corollary.

## 1. Statement and the exact model

Fix \(0<\delta\le2\). There is \(e_\delta>0\), depending only on
\(\delta\), with the following property. Choose any fixed
\(0<e\le e_\delta\) and use
\[
                 \phi_e(z)=1+z+e\arctan z                 \tag{1}
\]
in all three hidden layers. For every fixed \(d\ge1\), every two
deterministic inputs and labels satisfying
\[
 x_1,x_2\in\mathbb R^d,\quad \|x_a\|^2/d=1,\quad
 \rho=x_1^Tx_2/d\in[-1,1-\delta],\quad y_a\in\{-1,1\},     \tag{2}
\]
the full L3 population/GF/raw-GD theorem below holds. Correlations not
realizable at a particular \(d\) impose no requirement. The endpoint
\(\rho=-1\) is included.

Here is the finite model, fixing all normalizations. At width \(n\),
let \(W^1\in\mathbb R^{n\times d}\), \(W^2,W^3\in\mathbb R^{n\times n}\),
and \(C\in\mathbb R^n\). Initialize all entries independently with laws
\[
 W^1_{ij}\sim N(0,1/d),\quad W^2_{ij},W^3_{ij}\sim N(0,1/n),
 \quad C_i\sim N(0,n^{-2}).                              \tag{3}
\]
Use \(\langle u,v\rangle_n=u^Tv/n\). For \(a=1,2\), define
\[
 z_a^1=W^1x_a,\quad h_a^\ell=\phi_e(z_a^\ell),\quad
 z_a^2=W^2h_a^1,\quad z_a^3=W^3h_a^2,\quad
 f_a=\langle C,h_a^3\rangle_n,\quad r_a=f_a-y_a.
\]
Nonlinearities and vector products act coordinatewise. Backward vectors
exclude the residual:
\[
 b_a^3=C\phi_e'(z_a^3),\quad
 b_a^2=\phi_e'(z_a^2)(W^3)^Tb_a^3,\quad
 b_a^1=\phi_e'(z_a^1)(W^2)^Tb_a^2.                        \tag{4}
\]
The loss is \(\mathcal L=(r_1^2+r_2^2)/2\). Its gradient flow uses
\[
 \|\dot\Theta\|_{\rm raw}^2
 =\frac dn\|\dot W^1\|_F^2+\|\dot W^2\|_F^2
       +\|\dot W^3\|_F^2+\|\dot C\|_n^2,
\]
and therefore has equations
\[
 \dot W^1=-\frac1d\sum_a r_ab_a^1x_a^T,\quad
 \dot W^\ell=-\frac1n\sum_a r_ab_a^\ell(h_a^{\ell-1})^T
       \quad(\ell=2,3),\quad
 \dot C=-\sum_a r_ah_a^3.                                \tag{5}
\]
Raw GD is simultaneous Euler for exactly (5), with step \(\eta_n=n^{-2}\).
Raw parameters are interpolated linearly at physical times \(k\eta_n\);
hidden fields are recomputed from that interpolation. Hidden velocities
at nodes are right derivatives, with left derivatives at the terminal
endpoint. The finite readout in (3) is never reset to zero.

The conclusions are:

1. **Global population flow.** On the canonical generated Gaussian action
   spaces there is one autonomous uncut population solution for all
   \(t\ge0\). It is strong, has bounded primal quantities on compact
   intervals, is unique against bounded-primal strong competitors on
   the same action spaces, and has unique continuation from each reached
   state. Its state consists of a first-layer \(\mathbb R^d\)-valued
   field, two bounded operators with actual adjoints and Hilbert--Schmidt
   training increments, and a readout field. These are finitely many
   objects, not a claim of finite scalar dimension.
2. **Joint limits.** For every deterministic \(T<\infty\), finite GF and
   the exact raw GD converge along the full width sequence in probability
   to that flow, with the observable scope specified in Section 2.
   Predictions, loss, all four raw kernel blocks, hidden paths, and the
   stipulated recomputed hidden velocities and squared speeds converge.
   Both orientations of both initialized and trained actions are retained.
3. **Nontriviality.** At every finite physical time, every layer/sample
   has strictly positive best affine activation-approximation error.
   Every hidden parameter block and each sample's hidden features have
   nonzero initial acceleration, and the projected total kernel changes
   near zero. This is a positive small-time feature-learning certificate,
   not nonzero velocity at every later individual instant.

The same \(e\) works for all data in (2) and every finite \(T\).
Convergence and stability constants may depend on the fixed data,
\(d,e,T\). There is no supremum over datasets inside a probabilistic
limit, no interchange of \(T\to\infty\) and \(n\to\infty\), and no
selection of one activation for all \(\delta>0\). The activation is (1),
not the different bounded one-sample activation \(1+\arctan(z)/10\).

## 2. Population notation, observables, and the supplied lemmas

Write \(H_\ell=L^2(\Omega_\ell,\mu_\ell)\), \(\ell=1,2,3\), for three
separate neuron spaces. Inner products use the indicated layer's
probability measure. There is no coordinatewise pairing of neurons in
different layers. The first weight field is
\(w\in L^2(\Omega_1;\mathbb R^d)\). The current actions are
\(A:H_1\to H_2\), \(B:H_2\to H_3\), and the readout is \(C\in H_3\).
For \(u\in H_j,v\in H_i\), \(u\otimes v:H_i\to H_j\) maps \(q\)
to \(u\langle v,q\rangle_i\).

Population equations are (4)--(5), replacing normalized finite sums by
these inner products, transposes by actual adjoints, and normalized
outer products by \(\otimes\). The initial readout is zero in this
limit. Initial action norms are at most 10 on the canonical generated
spaces. The first projected pair is centered Gaussian with covariance
\(\left(\begin{smallmatrix}1&\rho\\\rho&1\end{smallmatrix}\right)\).
These are conclusions of the canonical construction, not extra
initialization assumptions.

The four raw kernel blocks are
\[
 K^1_{ab}=\rho_{ab}\langle b_a^1,b_b^1\rangle_1,\quad
 K^2_{ab}=\langle b_a^2,b_b^2\rangle_2\langle h_a^1,h_b^1\rangle_1,
\]
\[
 K^3_{ab}=\langle b_a^3,b_b^3\rangle_3\langle h_a^2,h_b^2\rangle_2,
 \qquad K^4_{ab}=\langle h_a^3,h_b^3\rangle_3,             \tag{6}
\]
where \(\rho_{aa}=1\) and \(\rho_{12}=\rho_{21}=\rho\).
Their convergence and prediction/loss convergence are uniform on
\([0,T]\). For each layer, empirical joint two-sample
preactivation/feature path laws converge in
\(\mathcal W_2(C([0,T];\mathbb R^4))\), with the supremum norm.
The joint same-layer laws including recomputed preactivation and feature
velocities converge in \(\mathcal W_2\), uniformly in time; fixed finite
collections of times also have joint \(\mathcal W_2\) convergence.
Second moments and integrated squared speeds converge. Operator
statements concern canonical generated probes, their joint laws and
both actions, and strong comparisons of learned increments on common
spaces. They do not assert operator-norm convergence of unrelated
finite matrices under an unspecified cross-width identification.

The following consequences of the attached mathematical proofs are used.
Their exact files are in sources/ and their hashes in SOURCE_HASHES.json.
Their historical status headers and review outcomes are not premises.

* **Affine/radial facts:** SYMMETRY_RADIAL_CLOCK.md, Sections 3--7,
  constructs the affine \(\phi_0=1+z\) scalar-feature gradient path.
  For \(g=\frac12\sum_a y_af_a\), feature time \(s\), and
  \(\kappa_0=\|\frac12\sum_a y_ah^3_{a,0}\|_3^2\), it gives
  \(g'\ge\kappa_0\), \(\|C'\|_3^2\ge\kappa_0\),
  \(\int_0^s\|\Theta'\|_{\rm raw}^2=g(s)\), and a bounded affine
  path through its first hit \(S\) of \(g=3/2\). It proves Gaussianity
  of its hidden preactivations, the common/contrast identities used
  below, and the initial kernel formula (7).
* **Uniform parameter interface of the response lemma:**
  TWO_SAMPLE_SOURCE_BASELINE.md, Sections 3--8, and
  NONLINEAR_RESPONSE_PERTURBATION.md, Sections 1--7, show that if
  affine Euler prefixes of duration at most \(s_0\) obey primal bound
  \(p\ge1\), there is \(\mathcal E(p,s_0)>0\), independent of the
  correlation, labels, width, mesh and caps, such that every
  \(0\le e\le\mathcal E(p,s_0)\) has bounded nonlinear response
  coefficients and \(\|Q\|_{L^q}\le K\sqrt q\), \(q\ge2\), for the
  actual readout and both reverse queries. Its auxiliary backward gate
  is \(q+e(1+z^2)^{-1}\tau_R(q)\), with only the nonlinear part clipped.
  Learned memories and current-source returns are retained.
* **Comparison and global bridge:**
  PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md, Sections 1--4, gives
  raw strong comparison with the affine path, cap removal, physical
  time conversion, uniqueness and restart, and finite GF/raw-GD and
  observable limits, when response tails and the endpoint margin
  \(g_{e,R}(S)>1\) hold. FIXED_CAP_VELOCITY_BRIDGE.md supplies its
  velocity bridge.
* **Initial motion:** INITIAL_FEATURE_LEARNING.md proves the stated
  initial feature and parameter motion and changing-kernel certificate
  for every fixed \(e>0\), every \(\rho<1\), and both label sectors,
  once the regular population path exists.

The finite Gaussian conditioning, singular-query, common-action and
adjunction ingredients are in the attached L3_LOCAL_COMPLETE_PROOF.md,
in its fixed-program, common-action and adjunction sections. Below all
data-dependent smallness premises of these lemmas are discharged;
the desired uniform-angle theorem is not assumed.

The response lemma's parameter interface can be checked explicitly.
Its equation (4) permits
\[
 A_0=2(24p^2\exp{36p^2s_0}+\tfrac92p^4),\qquad
 M_0=2s_0(8p^2\exp{36p^2s_0}+p^4).
\]
Its equation (65) permits
\[
 \mathcal E(p,s_0)=
 \min\left\{1,\frac1{480p^2s_0\exp{36p^2s_0}},
                    \frac1{2K \exp{Ks_0}}\right\},          \tag{R}
\]
where one \(K\ge1\) is obtained from the finite stage estimates using
only \(p,s_0,A_0,M_0\). No lower covariance eigenvalue enters. Geometry
enters there only through
\(\|\Gamma\operatorname{diag}(y/2)\|_{\infty\to\infty}\le1\).
Thus fixed numerical \(p,s_0\) select one threshold, not uncontrolled
pointwise choices. Below \(s_0>0\).

## 3. A uniformly bounded affine reference interval

Fix arbitrary data satisfying (2). For the affine model,
\[
 \kappa_0=
 \begin{cases}(7+\rho)/2,&y_1=y_2,\\
               (1-\rho)/2,&y_1=-y_2.
 \end{cases}                                            \tag{7}
\]
In either case \(\kappa_0\ge\delta/2\). Put
\[
 S_\delta=3/\delta,\qquad R_\delta=3/\sqrt{2\delta},
 \qquad U=11+R_\delta.                                  \tag{8}
\]
Until the first affine hit of \(g=3/2\), the radial and energy
estimates give
\[
 S\le\frac{3}{2\kappa_0}\le S_\delta,\qquad
 \|\Theta(s)-\Theta(0)\|_{\rm raw}
 \le\sqrt{s\,g(s)}\le\frac{3}{2\sqrt{\kappa_0}}
 \le R_\delta.                                         \tag{9}
\]
Existence through the hit follows from the polynomial affine field's
bounded-ball local Lipschitzness and its strong endpoint energy
estimate, as proved in the affine lemma. This uses no nonlinear
continuation.

Every projected first-layer norm, both current action norms, and the
readout norm on \([0,S]\) are at most \(U\): their initial bounds are
1, 10, 10, 0, and the raw displacement controls their changes. The full
initial first-row norm \(\sqrt d\|w_0\|_{L^2}=\sqrt d\) need not be
bounded independently of \(d\); only its projections and raw displacement
enter activation selection.

The endpoint \(S\) may depend on the data. No affine path is extended
beyond its own hit to \(S_\delta\). Every use of \(S_\delta\) below
is an upper bound on the duration of its prefixes.

## 4. Uniform nondegeneracy and a positive nonlinear margin

For the affine reference set
\(M_\ell=(z_1^\ell+z_2^\ell)/2\),
\(D_\ell=(z_1^\ell-z_2^\ell)/2\), and \(v_D=(1-\rho)/2\).
For opposite labels \(y=(\sigma,-\sigma)\),
\[
 D_2=AD_1,\qquad D_3=BD_2,\qquad C'=\sigma D_3.
\]
The radial lower bound \(\|C'\|^2\ge\kappa_0=v_D\) and
\(\|A\|,\|B\|\le U\) give, for every \(s\in[0,S]\),
\[
 \|D_3\|^2\ge v_D,\qquad
 \|D_2\|^2\ge v_D/U^2,\qquad
 \|D_1\|^2\ge v_D/U^4.                                 \tag{10}
\]
These also hold at zero. Affine sign symmetry gives
\(E D_\ell=E[M_\ell D_\ell]=0\), and hence
\(\operatorname{Var}(z_a^\ell)=\operatorname{Var}(M_\ell)+\|D_\ell\|^2\).
For same labels, the affine contrast is frozen in each population,
has variance \(v_D\), and has zero common/contrast covariance: this is
the conditional-Gaussian argument in equation (44) of the affine lemma.
Both sectors therefore satisfy
\[
 \operatorname{Var}(z_{a,0}^{\ell}(s))\ge m^2,\qquad
                m=\frac{\sqrt{\delta/2}}{U^2}>0.         \tag{11}
\]
The subscript 0 here denotes the affine activation, not initial time.
No input Gram inverse is used, including at \(\rho=-1\).

Affine forward propagation and the bound \(U\) give
\[
 \|z_{a,0}^1\|_2\le U,\quad
 \|z_{a,0}^2\|_2\le2U^2,\quad
 \|z_{a,0}^3\|_2\le3U^3=:L.                             \tag{12}
\]
For a scalar variable with positive variance, define
\[
 \mathcal R(Z)=\inf_{\alpha,\beta\in\mathbb R}
 E[\arctan Z-\alpha-\beta Z]^2
 =\operatorname{Var}(\arctan Z)
 -\frac{\operatorname{Cov}(Z,\arctan Z)^2}
                {\operatorname{Var}(Z)}.                \tag{13}
\]
For \(G\sim N(0,1)\), define
\[
 \eta=\min_{|\mu|\le L,\ m\le\sigma\le L}
                         \mathcal R(\mu+\sigma G).       \tag{14}
\]
This depends only on \(\delta\) and is positive. Coupling all variables
using the same \(G\), bounded Lipschitz arctangent and the lower variance
bound make (13) continuous in \((\mu,\sigma)\). A zero error would
identify arctangent with an affine function Gaussian-almost everywhere,
and hence everywhere by full support and continuity, contrary to its
nonconstant derivative. Compactness of this explicit parameter
rectangle then gives a positive minimum. Affine Gaussianity and
(11)--(12) imply, uniformly over all reference intervals,
\[
                    \mathcal R(z_{a,0}^{\ell}(s))\ge\eta. \tag{15}
\]
Compactness is used on Gaussian parameters, not on an unspecified
pointwise threshold.

Here is a quantitative stability version. Suppose
\(\|Z-Z_0\|_2\le t\), \(\operatorname{sd}(Z_0)\ge m\), and
\(\mathcal R(Z_0)\ge\eta\). If \(t\le m/2\), then
\(\operatorname{sd}(Z)\ge m/2\), because centering is an orthogonal
projection in \(L^2\). The optimal regression slope for arctangent
of \(Z\) has magnitude at most \(\pi/m\), by Cauchy--Schwarz and
\(\operatorname{sd}(\arctan Z)\le\pi/2\). Using its intercept and slope
as a competitor for \(Z_0\), the triangle inequality gives
\[
 \sqrt{\mathcal R(Z_0)}
 \le\sqrt{\mathcal R(Z)}+(1+\pi/m)t.
\]
Consequently
\[
 t\le\min\left\{m/2,\frac{\sqrt\eta}{2(1+\pi/m)}\right\}
       \quad\Longrightarrow\quad\mathcal R(Z)\ge\eta/4.   \tag{16}
\]
No Gaussianity of \(Z\) is required in this stability statement.

## 5. Selecting one coefficient from the separation alone

All constants in this section depend only on \(\delta\). Set
\[
 b=4U,\quad Q=40b^3S_\delta \exp{9b^2S_\delta},\quad
 J=12b^2Q+\pi b^2,\quad O=10b^3Q+b(J+\pi/2).              \tag{17}
\]
Affine Euler on its reference interval has projected primal bound
\(2U\) for sufficiently fine meshes, by its bounded-ball Euler
estimate. Source-baseline equation (32) supplies the finite-array
affine bound
\[
                         p=11+2U+4S_\delta(2U)^3.        \tag{18}
\]
Apply the response lemma at these fixed numerical arguments to select
\(\mathcal E(p,S_\delta)>0\). Mesh families for a dataset stop at its
own \(S\); all durations are at most \(S_\delta\). Thus (18) verifies
the affine premise without assuming a uniform-in-data limit theorem.

Define
\[
 e_\delta=\frac12\min\left\{
  1,\mathcal E(p,S_\delta),\frac b{4Q},\frac1{4O},
  \frac m{2J},\frac{\sqrt\eta}{2(1+\pi/m)J}
                                      \right\}>0.       \tag{19}
\]
This uses only finite bounds from the response lemma and the fixed
Gaussian minimization (14). It uses no actual input pair, trajectory,
width, or physical horizon. An optimal coefficient or numerical
optimization is unnecessary.

We verify every smallness use. For \(0<e\le e_\delta\), compare an
auxiliary nonlinear-cap feature flow with its affine reference on
the same canonical action spaces. On a projected primal ball of
radius \(b\), the direct comparison in the supplied bridge gives,
in the sum of raw component difference norms,
\[
                    \sup_{s\le S}E(s)\le Qe.             \tag{20}
\]
The affine path has primal bound \(U=b/4\). The restriction
\(Qe<b/4\) leaves strict room before nonlinear exit. A stopped
comparison therefore proves existence and (20) through \(S\) for
every finite cap, uniformly in that cap. The same estimate holds
for sufficiently fine Euler prefixes. Only the affine vector field
is used for the Lipschitz comparison.

For completeness, (20) gives a preactivation comparison with the
explicit constant \(J\). Both states have projected primal sizes
at most \(b\), and \(\|h_e^1\|\le4b\), \(\|h_e^2\|\le7b^2\),
\(\|h_e^3\|\le10b^3\). First \(\|z_e^1-z_0^1\|\le E\).
Expanding the second-layer action gives
\[
 \|z_e^2-z_0^2\|
 \le4b\|A_e-A_0\|_{\rm op}
           +b(\|z_e^1-z_0^1\|+\pi e/2)
 \le5bE+(\pi/2)be.
\]
The third-layer expansion gives
\[
 \|z_e^3-z_0^3\|
 \le7b^2E+b(5bE+(\pi/2)be+(\pi/2)e)
 \le12b^2E+\pi b^2e.
\]
Hence for every layer and sample,
\[
                    \sup_{s\le S}\|z_e^\ell-z_0^\ell\|_2\le Je.
                                                               \tag{21}
\]
The subscript 0 on an operator in these comparisons denotes its
affine-reference current value, not its initialized value.

For the projected prediction, Cauchy--Schwarz and
\(\sum_a|y_a/2|=1\) give
\[
 |g_{e,R}(S)-g_0(S)|
 \le10b^3E(S)+b(J+\pi/2)e\le Oe<1/4.
\]
Thus \(g_{e,R}(S)>5/4\) for every finite cap. The response lemma
supplies actual cap- and mesh-uniform subGaussian bounds on
\(C,q^2,q^1\), because \(e\le\mathcal E(p,S_\delta)\).
Every premise has been discharged with constants selected before
the data.

Equations (19),(21),(16) give
\(\mathcal R(z_e^\ell(s))\ge\eta/4\). After cap removal the same
strong comparison gives this for the uncut path. Absorbing \(1+Z\)
into the free affine approximant gives the exact identity
\[
 \inf_{\alpha,\beta}E[\phi_e(Z)-\alpha-\beta Z]^2
                         =e^2\mathcal R(Z).
\]
The uncut feature path therefore satisfies
\[
 \inf_{a,\ell,\ s\in[0,S]}\ \inf_{\alpha,\beta}
 E[\phi_e(z_a^\ell(s))-\alpha-\beta z_a^\ell(s)]^2
                          \ge e^2\eta/4>0.               \tag{22}
\]

## 6. The global flow, raw GD and observables

We detail the application of the supplied bridge, so that the affine
reference is not mistaken for the target dynamics.

The response \(L^q\) estimates give Gaussian \(L^2\) tail bounds for
the actual incoming fields. The asymmetric cap comparison has error
at most
\[
                 C\exp\{C(1+eR)S-cR^2\}\longrightarrow0. \tag{23}
\]
Only the reference path requires tails; a competitor does not. Thus
the cap family converges strongly, including its Hilbert--Schmidt
increments and raw directions, to an autonomous uncut \(C^1\)
feature-gradient path through \(S\).

The endpoint margin and constructed sample symmetry give a first
hit \(s_*<S\) of \(g=1\). Radial coercivity applies to this actual
strong gradient path. Its initial projected kernel is positive for
both label sectors, including \(\rho=-1\), by the initial Gaussian
calculation in the affine/radial lemma. Thus \(g'>0\) before fitting.

For this population path, \(f_a=y_ag\). Define
\[
 t(s)=\int_0^s\frac{du}{2(1-g(u))},\qquad 0\le s<s_*.     \tag{24}
\]
Its inverse satisfies \(ds/dt=2(1-g)\), converting the feature
gradient to exactly the population loss gradient (5). The kernel
is continuous and bounded on \([0,S]\); hence for some finite \(M\),
\(1-g(s)\le M(s_*-s)\). The integral (24) diverges at \(s_*\).
This single path therefore supplies every finite physical horizon,
and the nonaffinity margin (22) holds at every such time with no
further restriction on \(e\).

The finite dynamics do not have exact sample symmetry. As required
by the bridge, they are compared with same-width fixed-cap physical
systems using both actual residuals at every update. Fixed-program
Gaussian identification, deterministic fixed-cap Euler errors, and
stopped comparisons identify these references. On each fixed
physical \([0,T]\), cap-removal error has the form
\(C_T\exp(C_TR-cR^2)\), which tends to zero for every finite \(T\)
without further amplitude smallness. The same asymmetric
physical-field estimate proves uniqueness against any bounded-primal
strong physical competitor, including a nonsymmetric one. Applying
it at a reached time proves unique restart there.

For exact raw GD the extra reference-comparison error is
\(C_{R,T}\eta_n\). Width tends to infinity at each fixed cap and
auxiliary mesh, deterministic Euler estimates remove the auxiliary
mesh, and then the cap is removed. This identifies the full diagonal
scheme \(\eta_n=n^{-2}\), without a Gaussian theorem for a growing
number of queries. The small random finite readout (3) is retained.

The fixed-cap velocity lemma requires bounded primal paths,
bounded-derivative coordinate maps at fixed cap, and the fixed-program
construction, all supplied here. To remove the cap for velocities,
its deterministic comparison first fixes a truncation of a reference
preactivation velocity. Population cap velocities converge strongly
to the uncut velocity, whose \(L^2\) time image is compact. Sending
the cap to infinity at fixed truncation, then the truncation to
infinity, controls products of a gate difference and that velocity.
This is the ordered limit in the bridge's Section 4; it requires
no growth bound on cap-dependent moment constants. It yields
the velocity and second-moment scope in Section 2; products of
strongly converging \(L^2\) factors give (6).

For path laws the bridge uses
\[
 \|x-I_hx\|_{C([0,T])}^2
                         \le4h\int_0^T|x'(t)|^2\,dt,
\]
where \(I_h\) interpolates on a fixed observation grid. Averaging
this coupling bound, using the squared-speed bounds and then sending
the observation mesh to zero, upgrades finite-time laws to the
claimed path-space \(\mathcal W_2\) limits. Hidden velocities and
path laws are not inferred merely from weak state convergence.

The initial-motion lemma applies to every positive \(e\) in (19).
It retains the full Gaussian source and both reused-transpose
returns; its relevant feature-Gram matrices are positive even at
antipodal inputs. If \(V\) denotes initial hidden acceleration in
feature time, it gives nonzero blocks and sample feature accelerations,
and
\[
 \kappa(s)=\kappa(0)+2s^2\|V\|_{\rm hidden}^2+o(s^2),
                         \quad \|V\|_{\rm hidden}>0,
\]
where \(\kappa=\frac14y^T(\sum_{\ell=1}^4K^\ell)y\).
Since \(s(t)=2t+o(t)\), the certificate holds at small positive
physical times. It needs only \(e>0\), with no further
data- or \(T\)-dependent threshold. Together with (22), it discharges
all nontriviality requirements. The conclusions of Section 1 follow.

## 7. Logical extent

The quantifier proved is
\[
 \forall\delta\in(0,2]\ \exists e_\delta>0\
 \forall e\in(0,e_\delta]\
 \forall(d,x_1,x_2,y_1,y_2)\text{ satisfying (2)}\
 \forall T<\infty.
\]
Each limit is one global autonomous trajectory whose restrictions
give the compact-time convergence assertions. This is not convergence
uniformly over the whole half-line. The proof gives no positive
lower bound for \(e_\delta\) as \(\delta\downarrow0\), and does not
show that such a bound is impossible. It does not turn the known
nonlazy certificate into perpetual nonzero motion at each instant,
or identify (1) with the earlier bounded one-sample activation.
