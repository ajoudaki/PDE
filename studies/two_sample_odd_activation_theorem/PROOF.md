# A single odd activation for two inputs separated from both endpoints

Extension, 2026-09-07. This proof consists of this assembly and the three
companion lemmas AFFINE_CORE.md, SOURCE_AND_LIMIT_BRIDGE.md, and
INITIAL_MOTION_AND_NORMALIZATION.md. The immutable mathematical source
dependencies are attached in sources/ and identified in SOURCE_HASHES.json.
Review outcomes and historical status headers are not mathematical premises.

## 1. The theorem and exact model

For every \(0<\delta\le1\), there is \(e_\delta>0\), depending only on
\(\delta\), such that every activation
\[
 \phi_{a,e}(z)=az+e\arctan z,
 \qquad a\in[1/2,1],\qquad 0<e\le e_\delta                 \tag{1}
\]
has the complete two-input L3 population/GF/raw-GD conclusions below,
for every fixed dimension and deterministic dataset satisfying
\[
 x_1,x_2\in\mathbb R^d,\quad \|x_i\|^2=d,\quad
 \rho=x_1^Tx_2/d,\quad |\rho|\le1-\delta,\quad
 y_1,y_2\in\{-1,1\}.                                    \tag{2}
\]
Unrealizable dimension/correlation combinations impose no requirement.
The same activation is used at all three hidden layers; there are no
biases or activation offsets.

In particular, one may choose any \(0<\theta\le e_\delta\) and use the
genuine convex mixture
\[
                 \psi_\theta(z)=(1-\theta)z+\theta\arctan z.       \tag{3}
\]
Our choice below has \(e_\delta\le1/4\). A second admissible family,
also with coefficients fixed from \(\delta\) alone, is
\[
 \widehat\phi_r(z)=\frac{z+r\arctan z}
 {\sqrt{\mathbb E(G+r\arctan G)^2}},\qquad
 0<r\le e_\delta,\quad G\sim N(0,1).                     \tag{4}
\]
It satisfies \(\mathbb E\widehat\phi_r(G)^2=1\) exactly.

Here are the finite model and metric. At width \(n\), initialize all
entries independently:
\[
 W^1_{ij}\sim N(0,1/d),\quad W^2_{ij},W^3_{ij}\sim N(0,1/n),
 \quad C_i\sim N(0,n^{-2}),
\]
where \(W^1\in\mathbb R^{n\times d}\), \(W^2,W^3\in\mathbb R^{n\times n}\).
With \(\langle u,v\rangle_n=u^Tv/n\), define
\[
 z_i^1=W^1x_i,\quad h_i^\ell=\phi_{a,e}(z_i^\ell),\quad
 z_i^2=W^2h_i^1,\quad z_i^3=W^3h_i^2,\quad
 f_i=\langle C,h_i^3\rangle_n,\quad r_i=f_i-y_i.
\]
All products between neuron vectors in a layer are coordinatewise. Put
\[
 b_i^3=C\phi'(z_i^3),\quad
 b_i^2=\phi'(z_i^2)(W^3)^Tb_i^3,\quad
 b_i^1=\phi'(z_i^1)(W^2)^Tb_i^2.
\]
The loss \(\mathcal L=\frac12\sum_i r_i^2\) uses the raw metric
\[
 \|d\Theta\|_{\rm raw}^2
 =\frac dn\|dW^1\|_F^2+\|dW^2\|_F^2+\|dW^3\|_F^2+\|dC\|_n^2.
\]
Thus its exact gradient flow is
\[
 \dot W^1=-\frac1d\sum_i r_i b_i^1x_i^T,\quad
 \dot W^\ell=-\frac1n\sum_i r_i b_i^\ell(h_i^{\ell-1})^T
 \quad(\ell=2,3),\quad \dot C=-\sum_i r_i h_i^3.           \tag{5}
\]
Raw GD is simultaneous Euler for (5) at step \(\eta_n=n^{-2}\).
Interpolate raw parameters linearly at times \(k\eta_n\); recompute
hidden fields from this interpolation. At nodes use right hidden
derivatives and at a terminal endpoint use left derivatives. Retain
the initialized finite random readout throughout both algorithms.

The conclusions are as follows.

1. One autonomous, uncut, strong \(C^1\) population flow exists for all
   \(t\ge0\) on the canonical generated Gaussian action spaces. Its
   bounded-primal strong solution is unique on these spaces, including
   against nonsymmetric competitors, and has unique continuation from
   each reached state.
2. On every fixed finite physical interval, GF and raw GD converge
   jointly in probability along the full width sequence to this flow,
   with all observables and topologies in Section 2.
3. At every finite physical time every sample and hidden layer has
   strictly positive best affine activation-regression error. Every
   hidden parameter block and every sample's preactivation and feature
   in every hidden layer has nonzero initial physical acceleration.
   The projected total kernel changes near zero. These are initial
   feature-learning claims, not perpetual nonzero velocity claims.

The constants selecting \(a,e\) are independent of angle, labels,
dimension, width, caps, meshes and physical horizon. Each convergence
assertion concerns a fixed dataset and fixed \(T<\infty\); it is not a
supremum over datasets or convergence uniformly over the whole half-line.

## 2. Population objects and observable scope

There are three separate canonical neuron spaces
\(H_\ell=L^2(\Omega_\ell,\mu_\ell)\). The state is
\[
 w\in L^2(\Omega_1;\mathbb R^d),\quad A:H_1\to H_2,
 \quad B:H_2\to H_3,\quad C\in H_3,
\]
with bounded actions, their actual adjoints, and Hilbert--Schmidt learned
increments. For \(u\in H_j,v\in H_i\),
\((u\otimes v)q=u\langle v,q\rangle_i\). Replace the normalized sums,
transposes and outer products in the finite equations by these inner
products, adjoints and rank-one actions. The metric on increments is
\(d\|dw\|_2^2+\|dA\|_{\rm HS}^2+\|dB\|_{\rm HS}^2+\|dC\|_2^2\).
The canonical initial actions have norms at most 10, \(C(0)=0\), and
the initial first projected pair has covariance
\(\Gamma=\left(\begin{smallmatrix}1&\rho\\\rho&1\end{smallmatrix}\right)\).
These are the constructed initialization law, not new hypotheses on
the finite model.

All four raw kernel matrices, including their off-diagonal entries, are
\[
 K^1_{ij}=\Gamma_{ij}\langle b_i^1,b_j^1\rangle_1,\quad
 K^2_{ij}=\langle b_i^2,b_j^2\rangle_2\langle h_i^1,h_j^1\rangle_1,
\]
\[
 K^3_{ij}=\langle b_i^3,b_j^3\rangle_3\langle h_i^2,h_j^2\rangle_2,
 \qquad K^4_{ij}=\langle h_i^3,h_j^3\rangle_3.             \tag{6}
\]
They and the predictions/loss converge uniformly on \([0,T]\).
For each layer, the empirical joint two-sample preactivation/feature
path law converges in \(\mathcal W_2(C([0,T];\mathbb R^4))\), with the
supremum norm. The joint same-layer law including recomputed
preactivation/feature velocities converges in \(\mathcal W_2\) uniformly
in time, and jointly for each fixed finite collection of times. Second
moments and integrated squared speeds converge. Both orientations of
initialized and trained actions on their canonical generated probes
are retained. Strong comparisons of learned increments use common
spaces. No cross-layer neuron pairing, continuous-path velocity law,
or cross-width operator-norm identification is asserted.

The fixed-program Gaussian conditioning, singular-query regularization,
common actions and adjunction are proved in the attached
L3_LOCAL_COMPLETE_PROOF.md. The precise source-response and limit bridge
needed here is proved in SOURCE_AND_LIMIT_BRIDGE.md. It verifies the
zero-offset/gain changes in the attached controlled-response proof,
source baseline, comparison/continuation proof and fixed-cap velocity
proof. Its hypotheses will be checked below. In particular we do not
invoke the earlier shifted-activation theorem as though its statement
included (1).

The proof proceeds through a uniform bounded affine reference, a
uniform nonlinear perturbation and its source tails, and the exact
scalar time conversion. Separate initial-motion and nonaffinity
arguments verify that the resulting theorem concerns nonlinear feature
learning.

## 3. Symmetry, affine reference and nondegeneracy

Write \(y_1=\sigma,y_2=\sigma\tau\), with \(\sigma,\tau\in\{-1,1\}\).
Oddness gives an exact finite identity: replacing \((x_i,y_i)\) by
\((y_i x_i,1)\) leaves the loss as a function of raw parameters,
and hence every GF/GD trajectory, unchanged. Forward fields and
residuals acquire the factor \(y_i\), while residual-free backward
fields do not. The folded input correlation is \(\tau\rho\).

An orthogonal reflection exchanges the folded inputs. Gaussian
initialization and the raw vector field are invariant under this
exchange. At fixed caps and fixed Euler meshes this is an exact
finite-program equivariance. The limiting contractions are
deterministic, so their exchange-invariant laws force equal folded
predictions. Strong limits preserve this identity without assuming
uniqueness of an unconstructed flow. Thus the constructed population
paths, including cap paths, satisfy
\[
 f_i=y_i g,\quad g=\tfrac12\sum_i y_i f_i,\quad
 \mathcal L=(1-g)^2.                                    \tag{7}
\]
For the uncut field, \(\dot\Theta=2(1-g)\nabla g\). For a cap,
\(\dot\Theta=2(1-g)V_R\), where \(V_R\) is the capped feature field;
it need not be a gradient.
Finite-width predictions need not satisfy (7). These statements and
their action-space implementation are proved in AFFINE_CORE.md §1.

Let feature time mean \(\Theta'=\nabla g\). For the affine reference
\(\phi_{a,0}(z)=az\), define the orthogonal directions
\[
 u=(x_1+\tau x_2)/2,\quad v=(x_1-\tau x_2)/2,\quad
 v_u=(1+\tau\rho)/2,\quad v_v=(1-\tau\rho)/2.
\]
Both variances are at least \(\delta/2\). If
\(P_\ell=(z_1^\ell+\tau z_2^\ell)/2\) and
\(Q_\ell=(z_1^\ell-\tau z_2^\ell)/2\), then
\[
 P_1=w\cdot u, Q_1=w\cdot v,\quad
 P_2=aAP_1, Q_2=aAQ_1,\quad P_3=aBP_2, Q_3=aBQ_2.
\]
Writing \(H=\frac12\sum_i y_i h_i^3=\sigma aP_3\), the exact equations are
\[
 C'=\sigma aP_3,\quad B'=\sigma a^2 C\otimes P_2,\quad
 A'=\sigma a^3 B^*C\otimes P_1,\quad
 P_1'=\sigma v_u a^3 A^*B^*C,\quad Q_1'=0.                \tag{8}
\]
They depend only on the active initial root and the initial matrices.

The affine polynomial Hilbert field is locally Lipschitz on bounded
balls. With \(J\) the hidden linearization of \(H\),
\(C'=H\), \(C''=JJ^*C\), and \(\langle C,C''\rangle\ge0\).
Convexity of \(\|C\|\) and its initial right slope \(\|H(0)\|\)
give \(\|C'\|^2\ge\kappa_0\), where
\[
 \kappa_0=a^6 v_u\ge\delta/128,\quad
 g'=\|\Theta'\|_{\rm raw}^2\ge\kappa_0,\quad
 \int_0^s\|\Theta'\|_{\rm raw}^2=g(s).                  \tag{9}
\]
The first hit \(S\) of \(g=3/2\) exists: before it the energy is at
most \(3/2\), the strong endpoint estimate
\(\|\Theta(v)-\Theta(u)\|\le\sqrt{3(v-u)/2}\) gives a reached state
at any finite maximal endpoint, and local existence extends there.
A longer branch below the target contradicts \(g(s)\ge\kappa_0s\).
Consequently
\[
 S\le S_\delta:=192/\delta,\quad
 \sup_{s\le S}\|\Theta(s)-\Theta(0)\|_{\rm raw}
 \le R_\delta:=12\sqrt{2/\delta}.                        \tag{10}
\]
Set \(U=11+R_\delta\). All first projected norms, both current action
norms and the readout norm are at most \(U\). The full initial raw
first-layer norm need not be bounded independently of dimension; its
projections and changes have the bounds just used. Each reference stops
at its own hit \(S\); \(S_\delta\) only bounds the duration.

AFFINE_CORE.md §5 proves the following stronger nondegeneracy fact:
\[
 Q_1(s)=Q_1(0),\quad Q_2(s)=aA_0Q_1(0),\quad
 Q_3(s)=a^2B_0A_0Q_1(0),\quad
 \mathbb E Q_\ell=\mathbb E(P_\ell Q_\ell)=0.             \tag{11}
\]
Here \(A_0,B_0\) denote initialized actions. The proof conditions finite
affine programs on the active root and initial matrices: the independent
inactive Gaussian root has conditional covariance \(v_v I\), while a
learned increment has bounded Frobenius norm. Its action on that root
has normalized squared expectation \(v_v\|\Delta A\|_F^2/n\to0\).
The same argument applies to \(BA-B_0A_0\), and conditional scalar
contractions give zero active/inactive covariance. Fixed-program and
then strong affine Euler limits prove (11), rather than an inference
from bounded operators alone.

Every affine field is centered Gaussian: fixed source programs are
linear in joint Gaussian coordinates with deterministic contractions,
and strong limits preserve their Gaussian laws. Active-root sign
symmetry gives zero mean. Therefore, uniformly for all reference
times, layers, samples, gains and admissible data,
\[
 z_{i,a,0}^\ell(s)\sim\nu G,\quad
 m:=\sqrt{\delta/32}\le\nu\le L:=U^3.                   \tag{12}
\]
Indeed the frozen contribution has variance
\(a^{2(\ell-1)}v_v\ge\delta/32\); forward norm bounds give the upper
bound. This is the place where excluding both endpoints replaces the
offset argument.

Define
\[
 \mathcal R(Z)=\inf_{\alpha,\beta}\mathbb E[
       \arctan Z-\alpha-\beta Z]^2,\quad
 \eta=\min_{m\le\nu\le L}\mathcal R(\nu G)>0.            \tag{13}
\]
Positivity follows from continuity on this compact interval and the
impossibility of an affine arctangent identity on a full-support
Gaussian law. More explicitly,
\(\mathcal R(Z)=\operatorname{Var}(\arctan Z)-
\operatorname{Cov}(Z,\arctan Z)^2/\operatorname{Var}(Z)\),
whose denominator is bounded away from zero here. AFFINE_CORE.md §6
also proves the quantitative transfer
\[
 \|Z-Z_0\|_2\le\min\left\{m/2,
       \frac{\sqrt\eta}{2(1+\pi/m)}\right\}
 \quad\Longrightarrow\quad\mathcal R(Z)\ge\eta/4,        \tag{14}
\]
when \(\operatorname{sd}(Z_0)\ge m\) and \(\mathcal R(Z_0)\ge\eta\).
It follows by using the optimal regression slope for \(Z\), whose
magnitude is at most \(\pi/m\), as a competitor for \(Z_0\).

## 4. One coefficient choice and the nonlinear construction

All quantities selected in this section depend only on \(\delta\).
Put
\[
 b=4U,\quad Q=40b^3S_\delta e^{9b^2S_\delta},\quad
 J=12b^2Q+\pi b^2,\quad O=10b^3Q+b(J+\pi/2),
\]
\[
                   p=11+2U+4S_\delta(2U)^3.             \tag{15}
\]
The symbol \(J\) in (15) is now a numerical comparison constant, not
the temporary linearization operator in Section 3.

SOURCE_AND_LIMIT_BRIDGE.md §§1--3 proves a uniform source threshold
\(E_*(p,S_\delta)>0\) for the zero-offset family, with constant controls
\(c_i=y_i/2\). Its precise premise is the finite-array affine primal
bound at each fixed mesh, on events tending to probability one.
The bounded affine path has population Euler primal bound \(2U\) on
sufficiently fine meshes. Exact rank-one unrolling plus the finite
Gaussian operator bound yields that premise with the numerical \(p\)
in (15). No trained operator-norm convergence is assumed.

For specificity, with \(F=\exp(36p^2S_\delta)\), that lemma permits
\[
 A_0=2(24p^2F+9p^4/2),\quad M_0=2S_\delta(8p^2F+p^4),
\]
\[
 E_*(p,S_\delta)=\min\left\{1,
 \frac1{640p^2S_\delta F},\frac1{2K e^{KS_\delta}}\right\},          \tag{16}
\]
where one \(K\ge1\) is obtained from the finite derivative-envelope
and chronological response estimates using only these numerical
arguments. The lemma explicitly bounds all occurrences of the gain
by one before choosing \(K\). Thus this is a uniform constant,
not an infimum of possibly vanishing pointwise thresholds.

Choose
\[
 e_\delta=\frac12\min\left\{
 \frac12,E_*(p,S_\delta),\frac b{4Q},\frac1{4O},
 \frac m{2J},\frac{\sqrt\eta}{2(1+\pi/m)J}\right\}>0.     \tag{17}
\]
Use any fixed \(a\in[1/2,1]\) and \(0<e\le e_\delta\).
For smooth odd clips with
\(|\tau_R(q)|\le\min(|q|,2R)\), \(|\tau_R'|\le1\), and identity on
\([-R,R]\), the auxiliary backward gate is
\[
 D_{a,e,R}(z,q)=aq+e(1+z^2)^{-1}\tau_R(q).               \tag{18}
\]
Forward activations remain (1). This auxiliary construction will be
removed; it is not a modification of the target optimizer.

On a primal ball of radius \(b\), the same-state raw vector-field
difference from the affine field is at most \(40eb^3\) in the sum of
raw component difference norms. The affine field is \(9b^2\)-Lipschitz.
Both assertions hold uniformly in cap and gain, as verified term by
term in the source lemma. Stopped Gronwall gives
\[
 \sup_{s\le S}\|\Theta_{a,e,R}(s)-\Theta_{a,0}(s)\|_{\mathcal X}
 \le Qe.                                                \tag{19}
\]
Here the first component is \(\sqrt d\|\Delta w\|_2\), the next two
are learned-increment Hilbert--Schmidt differences, and the fourth is
the readout difference. The same product estimates hold in this norm
as in the projected/operator sum norm used by the finite-array lemma.
The affine primal bound is \(U=b/4\); (17) leaves a strict margin before
exit. Thus cap paths and sufficiently fine cap Euler prefixes exist
through the whole \([0,S]\).

To make the forward comparison explicit, write \(E\) for the
state discrepancy in (19). Using \(a\le1\) and bounded arctangent,
\[
 \|z_e^1-z_0^1\|_2\le E,\quad
 \|z_e^2-z_0^2\|_2\le5bE+(\pi/2)be,
\]
\[
 \|z_e^3-z_0^3\|_2\le12b^2E+\pi b^2e.
\]
For example expand \(A_eh_e^1-A_0h_0^1\), use
\(\|h_e^1\|\le4b\), and then repeat with
\(\|h_e^2\|\le7b^2\). Therefore
\[
              \sup_{i,\ell,s\le S}\|z_{i,e,R}^\ell-z_{i,0}^\ell\|_2
                 \le Je.                               \tag{20}
\]
The subscripts 0 here mean the affine current state. The prediction
comparison, using \(\sum_i|y_i/2|=1\), is
\[
 |g_{e,R}(S)-3/2|
 \le10b^3Qe+b(J+\pi/2)e=Oe<1/4.                         \tag{21}
\]
Thus every cap path has endpoint greater than \(5/4\).

The source lemma applies by (15)--(17). It controls the actual source
program, including both matrix orientations, full second-moment
covariances, learned memories and current transpose returns. It gives
cap- and mesh-uniform bounds \(\|C\|_q+\|q^2\|_q+\|q^1\|_q\le K_1\sqrt q\)
for \(q\ge2\). No inverse input covariance or positive activation
offset enters this lemma. Bounds such as \(|\phi'|,|D_q|\le2\) and
\(|D_z|\le2eR\) verify the fixed-program hypotheses.

The asymmetric comparison of SOURCE_AND_LIMIT_BRIDGE.md §4 uses tails
only from the reference path and has error
\[
                   C\exp\{C(1+eR)S-cR^2\}\longrightarrow0.        \tag{22}
\]
It follows by successive backward substitution with one factor \(R\)
on a forward-state discrepancy, and Gaussian tails of the three
incoming fields. Thus the cap paths converge strongly, including raw
directions, to an autonomous uncut strong \(C^1\) feature-gradient
path through \(S\). The endpoint margin (21) passes to this path.

By (14), (17), (20) and strong cap removal,
\[
 \inf_{i,\ell,s\le S}\inf_{\alpha,\beta}
 \mathbb E[\phi_{a,e}(z_i^\ell(s))-\alpha-\beta z_i^\ell(s)]^2
 = e^2\inf_{i,\ell,s\le S}\mathcal R(z_i^\ell(s))
 \ge e^2\eta/4>0.                                       \tag{23}
\]
The equality absorbs the linear term \(az\) into the affine approximant;
Gaussianity is required only of the reference, not of the trained flow.

## 5. Global physical time, uniqueness and the finite limits

For the nonlinear initial Gaussian recursion, oddness and
\(\phi'\ge a\) give \(q_\ell\pm c_\ell\ge a^2(q_{\ell-1}\pm c_{\ell-1})\).
Hence the actual initial projected kernel satisfies
\[
 \kappa_{a,e}(0)=\tfrac14 y^TK^4(0)y
              =(q_3+\tau c_3)/2\ge\delta/128.            \tag{24}
\]
The radial argument applies to the constructed uncut strong gradient
path: the strong trajectory chain rule gives \(C''=JJ^*C\), whence
\(g'=\|\nabla g\|^2\ge\kappa_{a,e}(0)>0\). This argument is used
after construction, not as a substitute for it.

Let \(s_*<S\) be the first hit of \(g=1\). On \([0,s_*)\) set
\[
 t(s)=\int_0^s\frac{du}{2(1-g(u))}.                     \tag{25}
\]
The compact feature path has continuous bounded kernel, say \(g'\le M\).
Thus \(1-g(s)\le M(s_*-s)\), so (25) diverges at \(s_*\).
Its inverse gives precisely the loss flow (5), for every finite
physical time, on one global autonomous trajectory. The bound (23)
therefore holds at every such time without shrinking \(e\).
In fact \(d(1-g)/dt=-2g'_s(1-g)\), so
\(\mathcal L(t)\le\exp(-\delta t/32)\).

Every cap also has a first hit of one by (21), starts below it, and
has bounded derivative on \([0,S]\). The same divergent-clock argument
produces its global physical reference path; monotonicity of its
projected prediction is not required because the capped feature field
need not be a gradient. These references inherit the uniform primal
and incoming-field tail bounds from their feature intervals.

SOURCE_AND_LIMIT_BRIDGE.md §§4--5 now applies on each physical
\([0,T]\). The physical asymmetric estimate retains both actual
residuals, has constants depending on \(T\), and requires tails only
of the cap reference. It proves uniqueness against every bounded-primal
uncut strong competitor, including nonsymmetric ones. Starting the
same estimate at any reached time proves unique restart. It does
not assert arbitrary-state existence beyond the reached states.

At fixed cap and fixed auxiliary mesh the generic finite-program law
identifies the finite reference using its two actual residuals and
learned contractions. Rank-one unrolling bounds current operators.
Deterministic fixed-cap Euler estimates remove the auxiliary mesh,
with constants independent of width. The finite asymmetric comparison
and strict stopping margin then identify uncut GF. Width is sent to
infinity before the cap; its physical error is bounded by
\(C_T\exp(C_TR-cR^2)\), tending to zero at every fixed \(T\).
For actual simultaneous raw GD the additional error is
\(C_{R,T}\eta_n\to0\). This identifies the full sequence
\(\eta_n=n^{-2}\) without applying a Gaussian theorem to an increasing
number of queries. Fixed-program stability retains the finite readout
whose normalized norm is \(O_{\mathbb P}(n^{-1})\).

For velocities the source lemma first smoothly truncates product
queries so that fixed-program bounded-derivative hypotheses apply.
The deterministic hidden-velocity comparison then fixes a truncation
of the reference velocity in products with a gate difference. The
uncut population velocity is continuous in \(L^2\) by the trajectory
chain rule and bounded continuous gates, so its compact time image
has uniformly vanishing \(L^2\) tails. Send the cap to infinity at fixed
velocity truncation, then the truncation to infinity; for finite
velocities take width first at each fixed cap and truncation. This
gives exactly the same-layer joint laws and speeds in Section 2,
without a growth assumption on cap-dependent fourth moments.

Products of converging \(L^2\) fields yield (6). For path laws use
\(\|x-I_hx\|_\infty^2\le4h\int_0^T|x'(t)|^2dt\), where \(I_h\)
is fixed-grid interpolation. Average over neurons, use the proved
speed bounds and fixed-grid joint \(\mathcal W_2\) convergence, and
send \(h\downarrow0\). This proves the stated path laws, rather than
inferring them from weak state convergence.

## 6. Initial feature learning and normalization

INITIAL_MOTION_AND_NORMALIZATION.md §§1--5 proves initial motion for
exactly (1)--(2). Each initial forward Gram is positive definite by
full Gaussian support and strict monotonicity. With
\(p_i=y_i/2\), \(H_0=\sum_i p_i h_{i,0}^3\), put
\(\beta_i^3=H_0\phi'(z_{i,0}^3)\). Its full second-moment matrix is
positive definite: a zero linear combination would force
\((\sum_i p_i\phi(z_i))(\sum_i v_i\phi'(z_i))=0\) everywhere,
contradicting nonconstant \(\phi'\) unless \(v=0\).

The first reused transpose has a Gaussian source with this full
second-moment covariance and the explicit derivative response. The
second reused transpose likewise has the full covariance of its
actual middle query and its response. Conditional variances and
\(\phi'\ge a\) make all three hidden acceleration blocks nonzero.
Adjunction gives positive aggregate sample accelerations in the upper
layers; input-exchange symmetry equates their squared norms, making
each sample's acceleration nonzero. The companion derives these
identities with all response terms, rather than omitting matrix reuse.

In its notation \(V\) is initial hidden feature-time acceleration,
\(\|V\|_{\rm hidden}>0\), and
\[
 \vartheta(s)=\vartheta(0)+\tfrac12s^2V+o(s^2),\quad
 \kappa(s)=\kappa(0)+2s^2\|V\|_{\rm hidden}^2+o(s^2),
\]
where \(\kappa=\frac14 y^T(\sum_\ell K^\ell)y\).
Since \(s'(0)=2\), physical hidden acceleration is \(4V\) and
\[
             \kappa(t)=\kappa(0)+8t^2\|V\|_{\rm hidden}^2+o(t^2).
\]
All sample preactivation and feature accelerations are nonzero as
claimed. The readout already has initial velocity \(2H_0\ne0\).

Finally, (3) has \(a=1-\theta\in[1/2,1]\), \(e=\theta\le e_\delta\).
For (4), let \(\mu=\mathbb E[G\arctan G]\) and
\(\nu=\mathbb E(\arctan G)^2\). Pointwise strict contraction gives
\(0<\nu<\mu<1\). Thus for \(0<r\le e_\delta\le1\),
\[
 D_r=\sqrt{1+2\mu r+\nu r^2},\quad 1<D_r<1+r\le2,
\]
\[
 a_r=D_r^{-1}\in[1/2,1],\quad e_r=r/D_r\le e_\delta.
\]
This directly places (4) in the proved parameter rectangle and proves
unit Gaussian energy. Its normalized positive coefficients sum to
\((1+r)/D_r>1\). A nontrivial literal convex mixture (3) has
\(|\psi_\theta(G)|<|G|\) almost surely and therefore energy strictly
less than one. Both requests can be met by positive normalized
weights, but not by weights summing to one. Normalization preserves
unit initial forward second moment through all layers by Gaussian
propagation; it does not assert trained variance conservation.

The proved quantifiers are
\[
 \forall\delta\in(0,1]\ \exists e_\delta>0\
 \forall a\in[1/2,1]\ \forall e\in(0,e_\delta]\
 \forall\text{ data satisfying (2)}\ \forall T<\infty.
\]
This is a two-input result. It supplies neither a single positive
coefficient for every \(\delta>0\), nor an odd or normalized
three-input theorem. At the excluded endpoint \(\rho=-1\), equal
labels remain incompatible with oddness; at \(\rho=1\), opposite
labels are incompatible with identical inputs. The new theorem
removes those configurations by (2), without invalidating the earlier
endpoint obstruction.
