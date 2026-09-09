# One activation for three separated inputs: global L3 theorem

2026-09-07. The current review status and exact reviewed versions are in
REVIEW_STATUS.md. This proof uses a fixed large affine gain in the
activation. Its conclusions concern the original raw training dynamics.

## 1. The statement and finite model

For each \(0<\delta\le3/2\), there are numbers \(a_\delta\ge1\) and
\(e_\delta>0\), depending only on \(\delta\), such that every fixed
\(0<e\le e_\delta\) and the single activation
\[
                   \phi(z)=a_\delta(1+z)+e\arctan z                 \tag{1}
\]
have the following property. Fix any \(d\ge1\), three deterministic
inputs \(x_i\in\mathbb R^d\), and labels \(y_i\in\{-1,1\}\), with
\[
 \|x_i\|^2/d=1,\qquad
 \Gamma_{ij}=x_i^Tx_j/d\le1-\delta\quad(i\ne j).                    \tag{2}
\]
Use (1) in all three hidden layers. The endpoint of a singular input
Gram is included. Only geometries realizable in the chosen dimension
are quantified over. For \(\delta>3/2\) this three-input class is empty.

At width \(n\), initialize independently
\[
 W^1_{ij}\sim N(0,1/d),\quad W^2_{ij},W^3_{ij}\sim N(0,1/n),
 \qquad C_i\sim N(0,n^{-2}).
\]
Write \(\langle u,v\rangle_n=u^Tv/n\), and, for \(i=1,2,3\), set
\[
 z_i^1=W^1x_i,\quad h_i^\ell=\phi(z_i^\ell),\quad
 z_i^2=W^2h_i^1,\quad z_i^3=W^3h_i^2,\quad
 f_i=\langle C,h_i^3\rangle_n,\quad r_i=f_i-y_i.
\]
The loss is \(L=\frac12\sum_i r_i^2\). The raw metric is
\[
 \|\dot\Theta\|_{\rm raw}^2
 =\frac dn\|\dot W^1\|_F^2+\|\dot W^2\|_F^2
                    +\|\dot W^3\|_F^2+\|\dot C\|_n^2.
\]
Define residual-free backward fields
\[
 b_i^3=C\phi'(z_i^3),\quad b_i^2=\phi'(z_i^2)(W^3)^Tb_i^3,\quad
 b_i^1=\phi'(z_i^1)(W^2)^Tb_i^2.
\]
The gradient-flow equations are exactly
\[
 \dot W^1=-d^{-1}\sum_i r_i b_i^1x_i^T,\quad
 \dot W^\ell=-n^{-1}\sum_i r_i b_i^\ell(h_i^{\ell-1})^T
       \quad(\ell=2,3),\qquad
 \dot C=-\sum_i r_i h_i^3.                                         \tag{3}
\]
Raw GD is simultaneous Euler for (3), with step \(n^{-2}\), and
piecewise-linear interpolation of the raw parameters at those physical
times. Hidden fields are recomputed from the interpolated parameters.
At mesh nodes velocities use right derivatives, with the terminal-left
convention on a closed observation interval. The finite random readout
is retained throughout.

The theorem asserts:

1. There is one global autonomous strong \(C^1\) population solution of
   (3). It is unique against bounded-primal strong competitors on the
   same canonical action spaces, and has unique continuation from every
   reached state.
2. On every fixed finite physical interval, finite GF and the exact raw
   GD converge jointly, along the full width sequence in probability,
   with all the observables and topologies stated below.
3. Every layer and sample has a positive best affine activation
   approximation error uniformly for all finite physical times.
   Every hidden population parameter block and every sample's hidden
   features have nonzero initial acceleration. The projected total
   kernel changes at small positive physical times.

The activation is independent of actual angle, labels, dimension,
width and physical horizon. Convergence constants may depend on fixed
data and horizon. No supremum over datasets is inserted into a
probabilistic limit, and convergence is not claimed uniformly over the
entire infinite time half-line. This theorem establishes the gain family
(1); it does not establish the restricted unit-slope family.

## 2. Population state, observables and mathematical dependencies

There are three separate canonical neuron spaces
\(H_\ell=L^2(\Omega_\ell,\mu_\ell)\). The state comprises
\[
 w\in L^2(\Omega_1;\mathbb R^d),\quad
 A:H_1\to H_2,\quad B:H_2\to H_3,\quad C\in H_3.
\]
The initialized Gaussian actions have norms at most 10 and actual
adjoints; their learned increments are Hilbert--Schmidt. The initial
first projections have joint law \(N(0,\Gamma)\), and \(C_0=0\).
These are conclusions of the canonical finite-program construction.
They are not substitute initializations. Outer products become
\(u\otimes v:q\mapsto u\langle v,q\rangle\), and (3) becomes its
population equation with layer-specific inner products.

The four \(3\)-by-\(3\) kernel blocks are
\[
 K^1_{ij}=\Gamma_{ij}\langle b_i^1,b_j^1\rangle,\quad
 K^2_{ij}=\langle b_i^2,b_j^2\rangle\langle h_i^1,h_j^1\rangle,
\]
\[
 K^3_{ij}=\langle b_i^3,b_j^3\rangle\langle h_i^2,h_j^2\rangle,\qquad
 K^4_{ij}=\langle h_i^3,h_j^3\rangle.                              \tag{4}
\]
Their limits, predictions, and loss are uniform in \(t\in[0,T]\).
In each layer, the empirical joint three-sample preactivation/feature
path law converges in
\(\mathcal W_2(C([0,T];\mathbb R^6))\), with the supremum norm.
The joint same-layer laws including recomputed preactivation and
feature velocities converge in \(\mathcal W_2\), uniformly in time,
and jointly at every fixed finite collection of times. Second moments
and integrated squared speeds converge. Both initialized and trained
action orientations are retained on canonical generated probes.
Strong comparisons of increments are on a common population space or
at the same width; no unspecified cross-width operator-norm
identification is asserted.

Two companion proofs supply the new ingredients:

- [GEOMETRY_AND_INITIAL_MOTION.md](GEOMETRY_AND_INITIAL_MOTION.md):
  the quantitative augmented-Gram bound and the initial-motion proof
  without sample-exchange symmetry.
- [CONTROLLED_RESPONSE_LEMMA.md](CONTROLLED_RESPONSE_LEMMA.md):
  the source-response theorem for three samples, gain \(a\), and
  arbitrary time-varying coefficients of bounded \(\ell^1\) norm.

The attached source files retain their exact mathematical versions,
listed in SOURCE_HASHES.json. The generic fixed-program conditioning,
singular-query, common-action and adjunction proofs are in
sources/L3_LOCAL_COMPLETE_PROOF.md. The response companion extends
the supplied source-baseline and nonlinear-response proofs explicitly,
including current transpose returns. Sections 6--7 below verify the
hypotheses and changes needed for the supplied primal/continuation and
fixed-cap velocity bridges. Neither the old two-sample theorem nor
its review outcomes is used as a three-sample theorem.

The proof architecture is: use separation to obtain an initial positive
feature Gram; choose a fixed large gain so a short residual-clock
budget bounds every controlled path; prove that the actual capped
physical flows stay within that budget; obtain uniform response tails
and remove the caps; then verify the limits and nontriviality.

## 3. Initial coercivity and a gain chosen from separation alone

Set
\[
                         \lambda=\delta^2/4.                    \tag{5}
\]
The geometry companion proves
\(\Gamma+\mathbf1\mathbf1^T\succeq\lambda I_3\).
Its argument applies also to singular \(\Gamma\): for a mixed-sign
coefficient vector write it, after a sign change and permutation, as
\((\alpha_1,\alpha_2,-b)\), with \(A_0=\alpha_1+\alpha_2\).
Projection of \(\sum q_i x_i/\sqrt d\) onto the third unit input gives
the lower quadratic
\((A_0-b)^2+((1-D_0)A_0-b)^2\), where \(\delta\le D_0\le2\).
Its matrix has determinant \(D_0^2\) and trace at most 4. Hence its
smallest eigenvalue is at least \(\delta^2/4\).
Same-sign coefficient vectors are controlled by \((\sum q_i)^2\).

For any \(a\ge1\) and \(e\ge0\), initial Gaussian propagation gives
\[
 Q_3:=\big(\langle h_i^3(0),h_j^3(0)\rangle\big)_{ij}
 \succeq a^6\Gamma+(a^6+a^4+a^2)\mathbf1\mathbf1^T
 \succeq a^6\lambda I_3.                                         \tag{6}
\]
For completeness, at each initialized layer the preactivations are
centered Gaussian with common marginal variance \(v>0\).
The odd function \(az+e\arctan z\) has Gaussian linear projection
coefficient \(a+e\,E[Z\arctan Z]/v\ge a\). The constant projection of
the feature is \(a\). Its orthogonal remainder has a positive
semidefinite Gram. Thus \(Q_\ell\succeq a^2\mathbf1\mathbf1^T+
a^2Q_{\ell-1}\), starting with \(Q_0=\Gamma\). Projection onto
independent Gaussian roots proves this even when the covariance is
singular; no inverse is needed.

We also define an absolute constant for later use. With \(G\sim N(0,1)\),
let
\[
 \mathcal R(Z)=\inf_{\alpha,\beta}E[\arctan Z-\alpha-\beta Z]^2,
 \qquad \eta_*=\inf_{\sigma\ge1}\mathcal R(\sigma G)>0,\qquad
 t_*=\min\{1/2,\sqrt{\eta_*}/[2(1+\pi)]\}.                          \tag{7}
\]
The positivity is proved in Section 8. Select
\[
 a=a_\delta=\max\left\{\frac{2000}{\sqrt\lambda},
                  \left(\frac{10^{12}}{\lambda^2t_*}\right)^{1/4}
                         \right\},\qquad
 S=\frac{12}{\lambda a^6}.                                       \tag{8}
\]
These are finite numbers determined before the data or trajectory.

## 4. A bounded controlled interval, with no scalar symmetry

Fix smooth odd clips satisfying
\[
 |\tau_R(q)|\le\min(|q|,2R),\quad |\tau_R'|\le1,\quad
 \tau_R(q)=q\ (|q|\le R).
\]
For example integrate a smooth even cutoff equal to one on \([-1,1]\)
and zero outside \([-2,2]\), and then rescale by \(R\).
Only the nonlinear backward part is clipped:
\[
                 D_{e,R}(z,q)=aq+e(1+z^2)^{-1}\tau_R(q).          \tag{9}
\]
Forward activations remain (1).

Replace \(-r_i\) in every update by any measurable \(c_i(s)\) with
\(\sum_i|c_i(s)|\le1\). Define the hidden raw displacement
\[
 D=\sqrt d\|w-w_0\|_2+\|A-A_0\|_{\rm HS}+\|B-B_0\|_{\rm HS}.
\]
On \(D\le1\), action norms are at most 11. Population first
preactivation norms are at most 2; allowing finite initial projection
norms up to 2 gives at most 3. For \(0\le e\le1\), forward and
backward propagation gives, in either case,
\[
 \|h_i^1\|\le6a,\quad\|h_i^2\|\le70a^2,\quad\|h_i^3\|\le800a^3,
\]
\[
 \|\delta_i^3\|\le2a\|C\|,\quad
 \|\delta_i^2\|\le44a^2\|C\|,\quad
 \|\delta_i^1\|\le968a^3\|C\|.                                  \tag{10}
\]
Here \(\delta^\ell\) denotes the capped backward field. The same
inequalities hold for the true backward fields.
Indeed \(|\phi(z)|\le a(3+|z|)\), and every backward gate has norm
at most \(2a\) times its incoming norm.

The hidden block speeds sum to at most
\((968+264+140)a^3\|C\|\le1400a^3\|C\|\), and
\(\|C'\|\le800a^3\). Starting with \(C_0=0\), every stopped
controlled prefix obeys
\[
 \|C(s)\|\le800a^3s,\qquad
 D(s)\le560000a^6s^2\le10^6a^6s^2.
                                                                    \tag{11}
\]
This proof also holds directly for arbitrary positive Euler meshes:
\(\sum_{j<k}h_js_j\le s_k^2/2\).
Consequently all controlled paths of duration at most \(S\) satisfy
\[
 C_S:=800a^3S=\frac{9600}{\lambda a^3},\qquad
 D_S:=10^6a^6S^2=\frac{1.44\cdot10^8}{\lambda^2a^6}.               \tag{12}
\]
The choice (8) ensures the strict inequalities
\[
 D_S<\min\{1/2,\lambda/(3\cdot10^7)\},\quad
 C_S<1,\quad 6\cdot10^6C_S^2<\lambda/4,\quad
 615a^2D_S<t_*.                                                  \tag{13}
\]
For the first three, use \(a^6\ge6.4\cdot10^{19}\lambda^{-3}\)
and \(0<\lambda\le9/16\). For the last, use
\(a^4\ge10^{12}/(\lambda^2t_*)\), giving a bound
\(0.08856t_*\).
The strict bounds close the stopped argument, uniformly in controls,
caps and meshes. At fixed cap, Picard's integral contraction applies
because (9) is Lipschitz in its two \(L^2\) arguments and other
operations are bounded bilinear maps on primal balls. The affine
controlled system is a polynomial field with the same bounds.

In particular these estimates provide the affine primal premise of
the controlled-response lemma with \(B=12\). At finite width the
initial action norms are at most 10 and first projection norms at
most 2 on events whose probabilities tend to one. Take the comparator
readout initially zero. The same stopped Euler bounds control every
operator increment directly by its rank-one update lengths; thus
the required finite-array bound holds, without assuming trained
operator-norm convergence. The actual small finite readout is
transferred in the finite-dynamics comparison in Section 7.

## 5. Global capped physical flows and response tails

On a controlled path, comparison with its own initialized state gives
\[
 \|\Delta h_i^1\|\le2aD,\quad \|\Delta z_i^2\|\le26aD,\quad
 \|\Delta h_i^2\|\le52a^2D,\quad
 \|\Delta z_i^3\|\le615a^2D,\quad
 \|\Delta h_i^3\|\le1500a^3D.                                  \tag{14}
\]
For example \(\Delta z^2=(A-A_0)h^1+A_0\Delta h^1\).
The next layer uses \(70a^2D+10(52a^2D)\le615a^2D\).
The norms of both current and initial feature columns are at most
\(800a^3\), so (14) and the three-column operator bound give
\[
 \|K^4-K^4(0)\|_{\rm op}\le7.2\cdot10^6 a^6D,\qquad
                         K^4\succeq(3/4)\lambda a^6 I_3.         \tag{15}
\]

This controls the actual physical cap flow even though it need not
be a gradient flow. Let \(J_h\) be the true hidden prediction
Jacobian and \(U_{h,R}\) the map from sample coefficients to capped
hidden directions. By (10),
\[
 \|J_h\|,\|U_{h,R}\|\le\sqrt3\,1400a^3\|C\|,\qquad
 \|J_hU_{h,R}\|\le6\cdot10^6a^6C_S^2\le\lambda a^6/4.
\]
Its residual equation is
\(\dot r=-(K^4+J_hU_{h,R})r\). The hidden contribution can have
either sign; bounding its absolute size and using (15) yields
\[
 \|r(t)\|_2\le\sqrt3\,\exp(-\lambda a^6t/2),\qquad
 \int_0^\infty\|r(t)\|_1\,dt\le\frac6{\lambda a^6}=S/2.            \tag{16}
\]

Initially this argument is stopped before the clock
\(s(t)=\int_0^t\|r(v)\|_1\,dv\) reaches \(S\). Before that event,
the physical path is precisely a controlled path with
\(c_i=-r_i/\|r\|_1\). If the residual vanishes, its physical
field is zero and the path is stationary. Equation (16) excludes
the clock-budget hit with strict slack. The attained raw state and
velocity are bounded on every finite physical interval; fixed-cap
local Lipschitzness supplies a strong endpoint and continuation.
Thus every cap flow is global and obeys (11)--(16).
No symmetry or clipped loss-energy identity is assumed.

Now apply the [controlled-response lemma](CONTROLLED_RESPONSE_LEMMA.md)
at the fixed arguments \((a,12,S)\). It supplies
\[
 e_{\rm resp}=e_*(a,12,S)>0,\qquad
 \sup_{R,t}\{\|C_R(t)\|_p+\|q_R^2(t)\|_p+\|q_R^1(t)\|_p\}
                      \le K\sqrt p\quad(p\ge2),                 \tag{17}
\]
for every \(e\le e_{\rm resp}\). To verify the application, at a
fixed finite physical mesh set \(h_j=\Delta t_j\|r_j\|_1\) and
\(c_j=-r_j/\|r_j\|_1\). Omit zero steps. Fixed-cap Euler convergence
and the strict \(S/2\) bound imply \(\sum h_j<S\) for all sufficiently
fine meshes on any fixed physical horizon. At the population level
these numbers are deterministic causal contractions. Formal source
derivatives freeze them; the affine comparison uses exactly the
same numbers, rather than its own residuals. The lemma is uniform
over all such sequences and does not differentiate the normalized
residual. Passing its moment bounds through fixed-cap strong Euler
convergence proves (17). The coefficient and \(K\) are independent
of the physical horizon.

## 6. Removing the caps and proving global autonomous uniqueness

The moment bounds (17) imply uniform Gaussian \(L^2\) tails for
the incoming fields: \(K_1e^{-cR^2}\), for constants depending only
on the fixed parameters. For \(R'\ge R\), including \(R'=\infty\),
the exact asymmetric gate estimate is
\[
 |D_{e,R'}(z_A,q_A)-D_{e,R}(z_B,q_B)|
 \le(a+e)|q_A-q_B|+C eR|z_A-z_B|
                    +2e|q_B|\mathbf1_{\{|q_B|>R\}}.              \tag{18}
\]
It follows by first changing \(q\), then \(z\), then the clip.
In the successive backward substitutions only a new forward-state
error receives a factor \(R\); a preceding incoming error is
multiplied by bounded actions and bounded \(q\)-derivatives.
Thus the raw-field comparison has one linear loss in \(R\),
not three multiplied cap factors. Physical residual coefficients
are Lipschitz on the primal ball, by forward propagation and
Cauchy--Schwarz.

The proof of Part 2 and the physical comparison in Part 3 of
sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md therefore gives,
on each fixed \([0,T]\), a raw state and direction difference
bounded by
\[
                       C_T\exp(C_TR-cR^2)\longrightarrow0.       \tag{19}
\]
Here the change from two to three samples is only in finite sums;
\(\sum_i|r_i|\le\sqrt3\|r\|_2\). Replacing the affine gate 1 by \(a\)
changes bounded constants in (18), not its power of \(R\).
The Gaussian tails are required only of the reference path.
These verify precisely the bridge's comparison hypotheses.

The cap paths hence converge strongly, including HS increments
and raw directions, to an uncut strong \(C^1\) physical solution
on every compact interval. The limits of (3) hold by bounded
actions, (18), and the strong forward chain rule. A common
canonical construction may include the countable cap/mesh
programs on all integer horizons. Their limits agree on overlaps.
This defines one global autonomous trajectory.

For any other bounded-primal strong physical solution with the
same initialization on those action spaces, use the same
reference-only estimate. Its bounds may depend on the competitor
and \(T\), but its error still vanishes in (19). This proves
uniqueness without a symmetry assumption or a tail assumption on
the competitor. Starting at a reached time gives the same argument:
the reference's initial discrepancy is already Gaussian-small in
the cap. Existence after that time is supplied by the global
trajectory. Thus reached-state continuation is unique. No general
Peano theorem on the ambient \(L^2\) space is invoked.

## 7. Finite GF, exact raw GD, and the complete observable limits

The required generic Gaussian-conditioning proof handles any fixed
finite collection of queries, both orientations of each matrix,
and independent initial root tuples. Three sample slots satisfy
these hypotheses. Singular query Grams are handled by the supplied
independent-query regularization proof and its zero-noise limit,
not by continuity of a pseudoinverse. At fixed cap, all forward
and backward coordinate instructions are continuously
differentiable with bounded first derivatives. The countable
generated-space construction then gives bounded actions and
actual adjoints from the finite transpose identities.

For a fixed cap and fixed auxiliary physical mesh, these facts
identify the joint finite-program laws, including each actual
residual contraction. The affine-initial/readout comparison at
fixed transcript retains the finite \(C_i\sim N(0,n^{-2})\);
its RMS size is \(O_{\mathbb P}(n^{-1})\), hence its limiting
population value is zero. It is never reset in the finite training.
Initialized matrix norms and exact rank-one update lengths bound
the current finite operators. Bounded population cap paths and
stopped, width-independent fixed-cap Euler estimates remove the
auxiliary mesh and identify finite cap GF.

Compare actual uncut finite GF with that same-width physical cap
reference. Its actual three residuals are retained. The finite
version of (18), reference-tail convergence at fixed cap, and
stopped stability give the width-limit error (19). Take width
first at fixed cap, then remove the cap. This proves full-sequence
convergence in probability. No finite sample symmetry is used.

For exact raw GD, evaluating its raw direction at the preceding
node instead of the reference's current time adds
\(C_{R,T}n^{-2}\) to the comparison. This is the physical Euler
argument in Part 3 of the supplied bridge: its hypotheses are
bounded reference paths, fixed-cap Lipschitz constants,
vanishing raw step, and the same asymmetric comparison.
All are now established for three samples and gain \(a\).
It does not require a Gaussian theorem for a growing number of
queries or a width-independent Lipschitz bound for the uncut field.
The two algorithms can be compared to the same reference, giving
their joint limit.

The fixed-cap hidden-velocity proof uses the actual physical
residuals, finite source rows, and bounds on
\(|\phi'|,|\phi''|,|D_q|,|D_z|\). Here these are respectively
\(a+e,C e,a+e,2eR\). Its nonlinear Gaussian probes, absolute
source-derivative rows, and two appended forward-action velocity
queries apply with three sample coordinates: block norms are
submultiplicative, and conversion from output rows costs the
fixed factor 3. The independent derivative proof in the response
companion verifies the needed source formalism and both current
returns. Velocity product instructions are first smoothly
truncated, as in Sections 4--6 of the supplied velocity proof;
they are not assumed to satisfy bounded-derivative hypotheses
before that truncation. Only \(L^2\) action bounds are used.

For cap removal, its deterministic velocity comparison has the form
\[
 K\{b+(1+M)a_0+
            \sum_{\ell,i}\|(|P_{{\rm ref},i}^\ell|-M)_+\|_2\},
                                                                    \tag{20}
\]
where \(a_0,b\) are state and raw-direction discrepancies and
\(P_{\rm ref}\) denotes reference preactivation velocity.
First compare population cap velocities against the uncut
population velocity. The latter is a continuous \(L^2\) path,
whose compact time image has uniformly vanishing \(L^2\) tails.
At fixed \(M\), remove the cap, then send \(M\) to infinity.
For finite comparisons, take width first at fixed cap and \(M\),
then cap to infinity at fixed \(M\), then \(M\) to infinity.
This is the ordered proof in Part 4 of the supplied bridge and
does not require control of the growth of fixed-cap moment
constants. It establishes the velocity laws and second moments
stated in Section 2, with the stipulated node conventions.

Products of converging \(L^2\) fields give all contractions in
(4). Finally, for an absolutely continuous coordinate path and
its interpolation \(I_h\) on a fixed observation grid,
\[
             \|x-I_hx\|_\infty^2\le4h\int_0^T|x'(t)|^2\,dt.
\]
Averaging this coupling bound and using the integrated squared
speed bounds upgrades fixed joint-time \(\mathcal W_2\) laws
to \(\mathcal W_2(C([0,T];\mathbb R^6))\).
Uniform-time velocity second-moment convergence also gives
integrated squared-speed convergence. This supplies every
observable listed in Section 2.

## 8. Uniform nonaffinity and initial feature learning

Each initialized scalar preactivation is centered Gaussian with
standard deviation at least 1: the first has variance 1, and
\(|az+e\arctan z|\ge a|z|\) in the initial covariance recursion.
For (7), Gaussian full support makes
\(\mathcal R(\sigma G)>0\) at every finite \(\sigma>0\).
The regression formula and dominated convergence give
\[
 \mathcal R(\sigma G)
 =E[\arctan(\sigma G)^2]-(E[G\arctan(\sigma G)])^2
 \longrightarrow\frac{\pi^2}{4}(1-2/\pi)>0.
\]
Continuity on compact positive \(\sigma\)-intervals then proves
\(\eta_*>0\).

If \(\|Z-Z_0\|_2\le t_*\), \({\rm sd}(Z_0)\ge1\) and
\(\mathcal R(Z_0)\ge\eta_*\), then \({\rm sd}(Z)\ge1/2\).
The optimal arctangent regression slope at \(Z\) has magnitude
at most \(\pi\). Testing its affine predictor at \(Z_0\) gives
\(\sqrt{\mathcal R(Z_0)}\le\sqrt{\mathcal R(Z)}+(1+\pi)t_*\),
and therefore \(\mathcal R(Z)\ge\eta_*/4\).
Equations (13)--(14) apply this to every sample/layer at every
time, first at finite cap and then in the uncut limit. Thus
\[
 \inf_{t\ge0,\ i,\ell}\ \inf_{\alpha,\beta}
 E[\phi(z_i^\ell(t))-\alpha-\beta z_i^\ell(t)]^2
                         \ge e^2\eta_*/4>0.                       \tag{21}
\]
No Gaussianity of trained preactivations is assumed.

The companion initial-motion proof uses \(p=y/3\),
\(m_p=\sum p_i\ne0\), and the initial scalar-feature objective
\(g=\sum_i p_i f_i\) only to compute derivatives at initialization.
It is not used as a physical scalar clock. For every \(e>0\)
the initial feature Grams and the two backward source Grams
are positive definite. The full reused-transpose source covariances
and their returns then give nonzero acceleration of every hidden
parameter block and every sample's first-layer features.

For each upper sample, the companion proves an affine
initial-acceleration lower bound and a uniform perturbation
estimate. With \(V\) the hidden acceleration for the
scalar-feature ascent and \(U_i^\ell\) its preactivation
acceleration, those bounds are
\[
 \|U_i^2\|^2\ge\frac{a^8m_p^4}{5}(a^2+a^4+a^6),\qquad
 \|U_i^3\|^2\ge
       \frac{a^{12}m_p^4}{14}(6+8a^{-2}+5a^{-4})
                                                               \tag{22}
\]
at \(e=0\), and
\(\|U_{i,e}^\ell-U_{i,0}^\ell\|\le2\cdot10^8a^7e\)
for \(\ell=2,3\), \(a\ge1\), \(e\le1\).
Since \(|m_p|\ge1/3\), the choice
\[
          e_\delta=\frac12\min\{1,e_*(a_\delta,12,S),
                                         (10^{10}a_\delta)^{-1}\}
                                                               \tag{23}
\]
preserves strictly positive acceleration for every upper sample.
The companion supplies the Gaussian moment derivation of (22)
and the direct norm induction for its perturbation bound.
This closes each sample separately, without sample symmetry.
Feature acceleration is nonzero because \(\phi'\ge a\).

In physical time,
\(C(t)=3tH+o(t)\), with \(H=\sum p_i h_i^3(0)\), and hidden
displacement \(9t^2V/2+o(t^2)\). Strong chain rules and adjunction
give
\[
 \kappa(t)=\kappa(0)+18t^2\|V\|_{\rm hidden}^2+o(t^2),
 \qquad \kappa=p^T\Big(\sum_{\ell=1}^4K^\ell\Big)p,\quad
 \|V\|_{\rm hidden}>0.                                          \tag{24}
\]
Hence the kernel changes near zero under the actual physical
three-residual dynamics. The assertion is an initial, small-time
feature-learning certificate, not perpetual nonzero velocity.

Every number in (8) and (23) depends only on separation. The
controlled-response coefficient is fixed before any physical
horizon is chosen, and (16) supplies one bounded residual-clock
budget for all horizons. Equations (3)--(24), the two companion
proofs, and the verified generic bridge hypotheses prove all
three conclusions of Section 1.
