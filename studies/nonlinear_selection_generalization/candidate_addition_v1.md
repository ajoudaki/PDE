#### C.4.10. Generalization during a finite added-data episode

The selected nonlinear predictor can learn a family specified independently of
the network, from finitely many noisy added observations. The family below has
full-circle input support and independently varying Fourier coefficients. A
finite-mode contraction connects that structure to an explicit approximation
floor, sampling and noise errors, and a positive stopping time. The hidden
features evolve throughout the episode. All quantitative constants are defined
from the class and the established reference; their numerical practicality is
not asserted.

##### C.4.10.1. Model, target family and observations

Retain exactly the bias-free two-hidden-layer tanh network
\[
 u=x/\sqrt2\in S^1,\qquad h^1_n=\tanh(W^1_nu),\qquad
 h^2_n=\tanh(W^2_nh^1_n),\qquad f_n=(W^3_n)^Th^2_n/n.
 \tag{NG1}
\]
Every stored entry and block is initialized independently, centered Gaussian
with variances \((1,1/n,1/n^2)\); the mobilities are \((n,1,n)\). Training is
physical GF of the unhalved mean square loss. The actual finite Gaussian
readout is retained. Every physical run starts from these initial arrays and
uses its fixed training law throughout.

Write
\[
 \nu_*={1\over2}\delta_{(\sqrt2e_1,1)}
                 +{1\over2}\delta_{(\sqrt2e_2,-1)},\qquad
 \mu_{\varepsilon,\nu}=(1-\varepsilon)\nu_*+\varepsilon\nu.
 \tag{NG2}
\]
Use C.4.9's full first-row state \(\theta=(w,K,c)\), raw Hilbert metric,
initialized Gaussian action \(A_0\), actual adjoint, and \(A=A_0+K\). Only
\(K\) is Hilbert–Schmidt. Its endpoint \(\theta_\dagger\), determined by the
complete reference feature flow from \((g,0,0)\), and
\(F_*(\sqrt2u)=f_{\theta_\dagger}(u)\) are those of C.4.9. In particular
\(F_*\) is odd, fits the two anchors, and changes sign under swapping the
two coordinates. The raw gradient and constraint projection are exactly
\[
 g_\theta(u)=\bigl(\phi'(w\cdot u)A^*[c\phi'(AH^1(u))]u,
          [c\phi'(AH^1(u))]\otimes H^1(u),H^2(u)\bigr),
 \quad \phi=\tanh,
\]
\[
 G_\theta=(g_\theta(e_1),g_\theta(e_2)),\quad
 M_\theta=G_\theta^*G_\theta,\quad
 \Pi_\theta=I-G_\theta M_\theta^{-1}G_\theta^*.
 \tag{NG3}
\]
Here \(H^1(u)=\phi(w\cdot u)\), \(H^2(u)=\phi(AH^1(u))\). No action,
adjoint, readout or feature is replaced by an independent surrogate.

Let \(\rho\) be normalized arc measure, with angle \(\alpha\) modulo
\(2\pi\) and \(u_\alpha=(\cos\alpha,\sin\alpha)\). Densities belong to
the fixed class
\[
 \mathcal P_D=\{p:\tfrac12\le p\le2,\ \int p\,d\rho=1,
                    \operatorname{Lip}_{\rm circle}(p)\le D\},\qquad D\ge0.
 \tag{NG4}
\]
In circle integrals, a function of physical input \(x\) is also written as
its pullback at \(x=\sqrt2u_\alpha\); this applies to \(q,F_*,P_\nu\) and
the sampled inputs in the force formulas.
Thus every input distribution has the entire circle as support. Neither its
support nor these bounds depend on width, sample size or contamination.
Fix \(s\ge1\), \(0\le R\le1/8\), and set
\[
 q_0(\alpha)=\cos^3\alpha-\sin^3\alpha,\qquad h(\alpha)=\sin^2(2\alpha),
 \qquad q=q_0+h v,
\]
\[
 v(\alpha)=\sum_{k\ge0}\{a_k\cos((2k+1)\alpha)+b_k\sin((2k+1)\alpha)\},
 \qquad \sum_{k\ge0}(2k+1)^s(|a_k|+|b_k|)\le R.
 \tag{NG5}
\]
Finite coefficient cap \(N\ge0\) means all coefficients with \(k>N\) are
zero; the resulting target's harmonic degree is at most \(2N+5\). Infinite
series are admitted with the same summability bound. This is a family of
targets specified without using any trained prediction. They are odd and
agree with the known anchor labels, so these constraints have no target
approximation cost. Other targets are not covered by the theorem.

For \(X=\sqrt2u_\alpha\) with density \(p\in\mathcal P_D\), labels obey
\[
 Y=q(X)+\xi,\qquad \mathbb E[\xi\mid X]=0,\qquad
 |\xi|\le h(\alpha)/8,\qquad \mathbb E[\xi^2\mid X]\le\sigma^2,
 \quad 0\le\sigma\le1/8.
 \tag{NG6}
\]
These laws have \(|Y|\le1\), and so are admitted for any prescribed label
bound at least one. Indeed, if \(a=|\cos\alpha|\), \(b=|\sin\alpha|\),
and \(t=ab\le1/2\), then
\((a^3+b^3)^2=1-3t^2+2t^3\le1-2t^2\le(1-t^2)^2\).
Consequently \(|q_0|\le1-h/4\); the perturbation and noise each use at most
\(h/8\) of this margin. Also \(\|v\|_\infty,\|v'\|_\infty\le R\), so
the series and derivative are uniformly convergent and the targets are
uniformly Lipschitz. Nonzero centered noise is permitted on arcs where
\(h>0\).

Draw \((X_i,Y_i)_{i=1}^m\) independently from \(\nu\), independently of
the Gaussian initialization, and train on
\[
 \widehat\nu_m={1\over m}\sum_{i=1}^m\delta_{(X_i,Y_i)},\qquad
 \widehat\mu_{\varepsilon,m}=(1-\varepsilon)\nu_*+
                                      \varepsilon\widehat\nu_m.
 \tag{NG7}
\]
Only the added observations are sampled. The anchor weights remain exactly
\((1-\varepsilon)/2\); no random rare-component count occurs in this design.
For an independent test input with law \(\nu_X\), use excess risk
\[
 \mathcal E_\nu(f)=\|f-q\|_{L^2(p\rho)}^2
                   =R_\nu(f)-\mathbb E\xi^2.
 \tag{NG8}
\]
Predictions are nevertheless retained on the entire circle.

The next three subsections prove the theorem package: common nonlinear
selection and original-GF capture for bounded added laws; continuum separation
and finite target-mode conditioning; then approximation, separated sampling
and noise, a class-determined positive stop, and robust unseen-risk and paired
upper-hidden margins. The limits are width first at each fixed positive
\(\varepsilon\) and each fixed sample, then \(\varepsilon\downarrow0\),
then increasing sample size. Nothing below invokes the time-40 sampling
theorem, a simultaneous rate, raw GD, or an all-time changed-law endpoint.

##### C.4.10.2. Bounded added laws: continuation, stability and finite-width capture

###### 1. State, constants and theorem

Retain C.4.9's two-hidden-layer bias-free tanh network, independent stored Gaussian
variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`, division of the readout by `n`,
unhalved square loss and physical GF. Each run uses
`mu_(epsilon,nu)=(1-epsilon)nu_*+epsilon nu` from its original initialization. The two
anchor weights in `nu_*` remain exactly `1/2`. Let `Y_0>=1`, and allow every Borel
probability added law on `sqrt(2)S1 x [-Y_0,Y_0]`. In integrals below, write
`u=x/sqrt(2)` and use the same symbol for the corresponding normalized law.

The canonical raw state is `theta=(w,K,c)`, with `A=A_0+K`, where only the middle
increment `K` is Hilbert–Schmidt. Its increment norm is

\[
\|\Delta\theta\|_{raw}^2=
\|\Delta w\|_2^2+\|\Delta K\|_{HS}^2+\|\Delta c\|_2^2.
\]

The initialized action and its actual adjoint act on C.4.9's common generated Gaussian
carrier. Write `phi=tanh` and

\[
H^1_\theta(u)=\phi(w\cdot u),\quad Z^2_\theta(u)=AH^1_\theta(u),
\quad H^2_\theta(u)=\phi(Z^2_\theta(u)),
\]
\[
f_\theta(u)=\langle c,H^2_\theta(u)\rangle,\quad
\delta_\theta(u)=c\phi'(Z^2_\theta(u)),\quad Q_\theta(u)=A^*\delta_\theta(u),
\]
\[
g_\theta(u)=
\bigl(\phi'(w\cdot u)Q_\theta(u)u,
             \delta_\theta(u)\otimes H^1_\theta(u),H^2_\theta(u)\bigr),
\]
\[
G_\theta=(g_\theta(e_1),g_\theta(e_2)),\quad M_\theta=G_\theta^*G_\theta,
\quad\Pi_\theta=I-G_\theta M_\theta^{-1}G_\theta^*.
\tag{NSC1}
\]

Let `theta_dagger` be the specified fitted reference endpoint of C.4.9. Its anchor Gram
has gap `k=lambda_min(M_dagger)>0` by C.4.9 proof unit B. Choose once the constants from
its proof unit A, decreasing its source radius to `0<delta_src<=1` if necessary. Denote
its control-mesh threshold by `h_src>0`. Put `L_src=10+delta_src` and choose
`M_src<infinity,c_src>0` so that its controlled raw Euler states satisfy

\[
\|c\|_\infty\le L_{src},\qquad
\sup_{u\in S^1}\tau_R(Q(u))\le M_{src}e^{-c_{src}R^2}\quad(R\ge1),
\tag{NSC2}
\]

whenever their complete controls have integrated distance at most `delta_src` from the
full reference history. Here `tau_R(Q)=||Q 1_(|Q|>R)||2`. The spatial-support uniformity
and passage of (NSC2) to the new flows are proved below.

The following constants are fixed before choosing the added law:

\[
a_b=3+\sqrt{10},\quad c_b=1+\sqrt{10},\quad H=L_{src},
\quad L=\sqrt{1+c_b^2(1+a_b^2)},\quad z_b=\sqrt{1+a_b^2},
\]
\[
D_b=\sqrt{1+4H^2z_b^2},\quad Q_b=c_b+a_bD_b,
\quad D_0=Q_b+D_b+c_b+z_b,
\]
\[
b_{src}=\max\{1,c_{src}^{-1/2}\},\qquad
C_g=D_0+2b_{src}+M_{src}/e,
\]
\[
\rho_s=\min\left\{\tfrac12,
                  \left(\frac{k}{8LC_g}\right)^2\right\},\qquad
C_d=C_g(1+4L/\sqrt k),
\]
\[
\mathcal K=2\{L^2+(c_b+Y_0)C_d\},\qquad B_r=c_b+Y_0.
\tag{NSC3}
\]

For the common positive episode define

\[
A_s=2B_r+4B_rL/\sqrt k,\quad V_s=2B_rL,
\quad C_s=32B_rL^2/k+\sqrt2+2B_r,
\]
\[
T_c=\min\left\{
\frac{\delta_{src}}{16A_s},\frac{\rho_s}{16V_s},
\frac{\delta_{src}}{16C_s},\frac{\rho_s}{16LC_s}\right\}>0.
\tag{NSC4}
\]

In particular the source radius is retained separately from its tail constants. A tail
bound alone would not determine the admissible episode. For a law `nu` set

\[
v_\nu(\theta)=\int(f_\theta(u)-y)g_\theta(u)\,d\nu(u,y),
\quad V_\nu(\theta)=-2\Pi_\theta v_\nu(\theta),
\quad d_\theta(u)=\Pi_\theta g_\theta(u).
\tag{NSC5}
\]

**Bounded-law continuation theorem.** There is `epsilon_0>0`, depending only on the
reference and `Y_0`, with the following properties. For every admitted Borel law the
equation

\[
\theta_\nu'(\tau)=V_\nu(\theta_\nu(\tau)),\qquad
\theta_\nu(0)=\theta_\dagger
\tag{NSC6}
\]

has a unique strong solution on `[0,T_c]` in the radius-`rho_s` neighborhood. It
preserves both anchor predictions and determines

\[
P_\nu(\tau,\sqrt2u)=f_{\theta_\nu(\tau)}(u)
\tag{NSC7}
\]

on the entire circle. It is unique from each reached state on the remaining interval.
The original-initialization mixture population GF exists uniquely through `T_c/epsilon`
for `0<epsilon<epsilon_0`, and for each `0<tau_-<T_c`,

\[
\lim_{\epsilon\downarrow0}\sup_\nu\sup_{\tau_-\le\tau\le T_c}
\|\theta_{\mu_{\epsilon,\nu}}(\tau/\epsilon)-\theta_\nu(\tau)\|_{raw}=0.
\tag{NSC8}
\]

This also holds for whole-circle prediction and for both hidden activations uniformly in
input in population `L2` norm. For every separately fixed `epsilon in (0,epsilon_0)` and fixed
added law, actual finite GF converges in probability to the mixture prediction in
`C([0,T_c/epsilon] x sqrt(2)S1)`. With reference and mixture trained on the same initial
arrays, their paired hidden squared distances converge uniformly over this time interval
and the entire circle. Consequently width first and epsilon second capture (NSC7) and
its paired distance from the reference endpoint. These assertions hold for every
empirical law, including repeated observations and singular input configurations.

On the constructed neighborhood the observation constants are `|f|<=c_b`, `||g||<=L`,
and scalar prediction raw Lipschitz constant `L`. Moreover, with

\[
\omega(s)=s\sqrt{\log(e/s)}\ (0<s\le1),\qquad\omega(0)=0,
\tag{NSC9}
\]

the one-reference bound is `||V_Q(theta)-V_Q(bar theta)||<=mathcal K omega(||theta-bar
theta||)` for every bounded-label law `Q`, when the barred state bears (NSC2). Law
continuity, with an explicit modulus, is proved in §4. There is no assertion of a
changed-law final endpoint, a raw-GD extension or a simultaneous width/epsilon rate.

###### 2. Uniformity in the number of spatial slots

Apply C.4.9 proof unit A to an arbitrary finite list containing the two anchors.
Reference controls outside the two anchor slots are zero. For paired Euler coefficients
put `m_p=|gamma_p|+|bar gamma_p|` and, at nonzero mass, `e_p=|gamma_p-bar gamma_p|/m_p`.
Its comparison identities use

\[
\sum_pm_p\le20+\delta_{src},\qquad
\sum_pm_pe_p=\sum_p|\gamma_p-\bar\gamma_p|.
\tag{NSC10}
\]

These bounds explain why adding spatial slots leaves its constants unchanged. Direction
factors in CT12–CT16 have norm at most one. CT29–CT31 attach the injection mass
`|gamma_p|` to each old response. CT28 applies Jensen with normalized absolute
coefficient masses and never takes a maximum of Gaussian queries over the growing list.
After CT40 divides the pulse discrepancy by `m_p`, CT41 sums it using (NSC10). The upper
row calculation CT43–CT44 exchanges finite sums whose total mass is bounded. Its
Gronwall exponent depends on that mass; CT36 explicitly has no source-slot-count
dependence.

The reference anchor in A.4 has only two nonzero controls. Additional zero slots inject
nothing into later states. A passive current query has one distinguished direct source;
unused earlier passive queries have zero later derivatives. Thus its reference cap and
final choice of `delta_src` remain the same. The fixed-program singular-query proof
retains distinct formal source names at duplicated or antipodal inputs. No inverse of
their input Gram enters these estimates.

It follows that one source tube gives (NSC2), all fixed query moments and the controlled
norm bounds uniformly over finite support size, minimum atom weight and every
quadrature. The elementary full-row update also gives, for each fixed `p>=2`,

\[
\|w\|_{L^p(\Omega_1;\mathbb R^2)}
\le\|g\|_p+\sum_p|\gamma_p|\|Q_p\|_p.
\tag{NSC11}
\]

This is Minkowski with total control mass at most `H`; it makes no `Lp` operator
assertion about the initialized action. All histories, including the full retained
reference prefix, use the same action and its actual adjoint.

###### 3. Explicit gradient, projector and spatial bounds

On the raw unit ball about the endpoint, the established endpoint bounds give
`||A||<=a_b`, `||c||2<=c_b`. The three gradient block norms are at most `a_b c_b,c_b,1`,
proving `||g_theta(u)||<=L`. Scalar differentiability from A.4 and integration along a
straight raw segment give

\[
|f_\theta(u)-f_{\bar\theta}(u)|\le L\|\theta-\bar\theta\|_{raw}.
\tag{NSC12}
\]

Let `d=||theta-bar theta||raw`, and suppose only the barred state has (NSC2). The
forward difference is bounded by `z_b d`. Splitting the upper gate against its bounded
barred readout yields `||delta-bar delta||2<=D_b d`; actual adjunction then gives
`||Q-bar Q||2<=Q_b d`. The middle-gradient and readout-gradient differences are at most
`(D_b+c_b)d` and `z_b d`, respectively. For the remaining row product, `0<=phi'<=1` and
`|phi''|<=2` give

\[
\|[\phi'(w\cdot u)-\phi'(\bar w\cdot u)]\bar Q(u)\|_2
\le2Rd+\tau_R(\bar Q(u)).
\]

Adding the block bounds proves

\[
\|g_\theta(u)-g_{\bar\theta}(u)\|_{raw}
\le(D_0+2R)d+M_{src}e^{-c_{src}R^2}.
\tag{NSC13}
\]

For `0<d<=1`, choose `R=b_src sqrt(log(e/d))`. Then `R>=1`, the tail is at most `M_src
d/e`, and

\[
\|g_\theta(u)-g_{\bar\theta}(u)\|_{raw}\le C_g\omega(d).
\tag{NSC14}
\]

Consequently `||G||<=sqrt(2)L`, `||G-bar G||<=sqrt(2)C_g omega(d)` and
`||M_theta-M_dagger||<=4LC_g omega(||theta-theta_dagger||)`. The inequality `s
log(e/s)<=1` on `(0,1]` implies `omega(s)<=sqrt(s)`. The radius in (NSC3) therefore
ensures `M_theta>=k I/2`. Two states in that radius have distance at most one.

Put `B=GM^{-1}` and `P=GM^{-1}G*`. Since `B*B=M^{-1}`, `||B||<=sqrt(2/k)`. The exact
projection identity

\[
P-\bar P=\bar\Pi(G-\bar G)B^*
                         +\bar B(G-\bar G)^*\Pi
\tag{NSC15}
\]

follows by expanding `bar Pi P-bar P Pi`. It gives `||Pi-bar Pi||<=4C_g
omega(d)/sqrt(k)`, and hence

\[
\|d_\theta(u)-d_{\bar\theta}(u)\|\le C_d\omega(d).
\tag{NSC16}
\]

Splitting the residual and projected gradient in (NSC5), using `|f-y|<=B_r`, proves the
stated field modulus with coefficient `mathcal K=2(L^2+B_r C_d)`. This is a
one-reference estimate; it does not assert ambient local Lipschitzness.

Here is a quantitative spatial bound for the Borel-law step. Layer cake and
`Pr(|Q|>R)<=tau_R(Q)^2/R^2` imply

\[
q_4:=\left(1+M_{src}^2e^{-2c_{src}}/c_{src}\right)^{1/4}
\ge\sup_u\|Q(u)\|_4.
\tag{NSC17}
\]

Let `W=sqrt(2)+sqrt(10)+1` and `W_4=8^(1/4)+H q_4`. The first is a unit-ball row bound;
the second follows from (NSC11) since `E|g|^4=8`. For `h=|u-v|`, forward and upper
subtraction give

\[
\|H^1(u)-H^1(v)\|_2\le Wh,\quad
\|Z^2(u)-Z^2(v)\|_2\le a_bWh,
\]
\[
\|\delta(u)-\delta(v)\|_2\le2Ha_bWh,\quad
\|Q(u)-Q(v)\|_2\le2Ha_b^2Wh.
\tag{NSC18}
\]

The lower changed gate times the old query is at most `2h ||w||4 ||Q(v)||4<=2W_4q_4h`.
Subtracting the explicit input vector and the rank factors thus proves
`||g(u)-g(v)||<=L_x h`, where

\[
L_x=a_bc_b+2Ha_b^2W+2W_4q_4+2Ha_bW+c_bW+a_bW.
\tag{NSC19}
\]

The prediction input Lipschitz constant is at most `c_b a_b W`. Use Wasserstein distance
with cost `d_c(u,v)+|y-z|`, where `d_c` is circular arc distance. Integrating a coupling
at a reached state gives

\[
\|V_\nu(\theta)-V_\lambda(\theta)\|
\le\Lambda\mathcal W_1(\nu,\lambda),\qquad
\Lambda=2\{L(1+c_ba_bW)+B_rL_x\}.
\tag{NSC20}
\]

These estimates prove the required uniform spatial regularity. The integrands are
continuous Hilbert-valued functions on compact data space, hence have separable compact
range and are Bochner integrable.

###### 4. Strong completion over all added laws

For an increasing extension of (NSC9), the following elementary comparison will be used.
If `D(t)<=eta+K_0 integral_0^t omega(D(s))ds`, then

\[
D(t)\le\mathcal O_{K_0,t}(\eta):=
e\exp[-(\sqrt{\log(e/\eta)}-K_0t/2)^2]
\tag{NSC21}
\]

provided `sqrt(log(e/eta))>1+K_0t/2`. To prove it, use the integral upper comparison
`Z`, for which `Z'<=K_0 Z sqrt(log(e/Z))` before its first exit at one. Thus
`(sqrt(log(e/Z)))'>=-K_0/2`; integration proves the bound, whose strict size condition
prevents that exit. At zero let positive upper errors decrease to zero. This proves
uniqueness and convergence for every fixed finite horizon.

First let `nu=sum_j p_j delta_(u_j,y_j)` be any finite law. Its constrained controls
consist of added coefficients `-2p_j(f(u_j)-y_j)` and anchor vector `2M^{-1}G*v_nu`.
Their absolute sum is at most `A_s`, since `||v_nu||<=B_rL` and
`||GM^{-1}||<=sqrt(2/k)`. Raw speed is at most `V_s`. Append constrained Euler to
increasingly long reference raw-Euler prefixes, with their exact integrated reference
controls. Choose prefix endpoint error, integrated-control error and omitted reference
suffix below `rho_s/32,delta_src/32,delta_src/32`, respectively. By (NSC4) the appended
control mass and displacement are each smaller than one sixteenth of the relevant outer
radius. Every complete history is therefore strictly source admissible before (NSC2) is
used. Its control mesh is chosen below `h_src`.

Compare two affine Euler interpolants. Their preceding-node error is at most their speed
times their maximal steps. The one-reference field modulus then bounds their integrated
discrepancy by (NSC21), with an additive error tending to zero with the meshes and
prefixes. They are Cauchy in the strong raw path norm, uniformly over finite added laws.
Their integral equations pass to (NSC6).

The source bounds pass to that limit. Readout bounds pass by an almost surely convergent
subsequence. Query convergence in `L2` follows from factor subtraction with the bounded
comparison readout; the positive-part inequality

\[
\tau_{2R}(Q)\le2\|(|Q|-R)_+\|_2
\tag{NSC22}
\]

passes a Gaussian tail bound through this strong limit. In fact the original constants
themselves pass: take an almost surely convergent subsequence and apply Fatou to the
nonnegative lower semicontinuous function `q -> q^2 1_(|q|>R)` at each fixed `R`. Thus
(NSC2) holds with the same `M_src,c_src` used in (NSC3)–(NSC4). Row moments pass by
Fatou. Interpolation between `L2` convergence and uniform `L8` bounds gives query
convergence in `L4`, also proving strong measurability for the measure/time integrals
below.

For a Borel law choose finite Borel quantizers `T_l` with `sup_z d_Z(T_lz,z)<=h_l->0`
and put `nu_l=(T_l)#nu`. Equations (NSC16), (NSC20), (NSC21) give

\[
\sup_{\tau\le T_c}\|\theta_{\nu_l}(\tau)-\theta_{\nu_j}(\tau)\|
\le\mathcal O_{\mathcal K,T_c}(\Lambda T_c(h_l+h_j))
\tag{NSC23}
\]

for sufficiently small errors. Their strong limit is independent of the quantizers. The
same bounds pass, and (NSC20) together with the state modulus passes the integral
equation. Its field is continuous in time, so its solution is strongly `C1`. The finite
laws and their prefixes are realized through the fixed common language of III.F; a
countable dense law family and the displayed uniform completion represent every law on
the same carrier. No fresh source is inserted when a prefix is removed or a path is
restarted.

The comparison with any competing strong raw solution uses only the constructed path's
tails, so (NSC21) proves uniqueness in the stated neighborhood and from each reached
state. The scalar chain rule gives `(f(e1),f(e2))'=G*V_nu=0`. Bounded gradients
also justify differentiation under the added-law integral, giving the exact identity

\[
\frac d{d\tau}\int(f_{\theta_\nu(\tau)}(u)-y)^2d\nu
=-4\|\Pi_{\theta_\nu(\tau)}v_\nu(\theta_\nu(\tau))\|^2.
\tag{NSC24a}
\]

For two laws the quantitative bound is

\[
\sup_{\tau\le T_c}\|\theta_\nu(\tau)-\theta_\lambda(\tau)\|
\le\mathcal O_{\mathcal K,T_c}(\Lambda T_c\mathcal W_1(\nu,\lambda))
\tag{NSC24}
\]

whenever its size condition holds; use the common raw diameter for larger errors.
Prediction difference is at most `L` times the raw bound, and both hidden `L2`
differences obey the direct forward bounds.

###### 5. Strong derivatives along reached controlled curves

Let a reached curve have a signed measure of controls with total absolute mass `m(t)`
per unit time. The controlled equations and (NSC17) give

\[
\|w'\|_2\le a_bc_bm,\quad\|w'\|_4\le q_4m,\quad
\|K'\|_{HS}\le c_bm,\quad\|c'\|_\infty\le m.
\tag{NSC25}
\]

These statements hold also along an affine Euler step with its fixed node velocity;
intermediate queried states are fractional versions of the last source-admissible
update. Put

\[
Z_t=c_b(1+a_b^2),\quad D_t=1+2HZ_t,\quad Q_t=c_b^2+a_bD_t,
\]
\[
T_g=2q_4^2+Q_t+D_t+a_bc_b^2+Z_t,
\quad T_B=2\sqrt2T_g/k+16\sqrt2L^2T_g/k^2.
\tag{NSC26}
\]

The forward and upper differentiation identities are

\[
(H^1(u))'=\phi'(w\cdot u)w'\cdot u,\qquad
(Z^2(u))'=K'H^1(u)+A(H^1(u))',
\]
\[
(H^2(u))'=\phi'(Z^2(u))(Z^2(u))',\quad
\delta(u)'=c'\phi'(Z^2(u))+c\phi''(Z^2(u))(Z^2(u))',
\]
\[
Q(u)'=K'^*\delta(u)+A^*\delta(u)'.
\tag{NSC27}
\]

Their `L2` norms are bounded respectively using (NSC25), then `||(Z2)'||2<=Z_t m`,
`||delta'||2<=D_t m`, `||Q'||2<=Q_t m`. For the gradient's first block the extra product
is `phi''(w.u)(w'.u)Q(u)`, of norm at most `2q_4^2 m` by Hölder. The rank derivative
costs `(D_t+a_b c_b^2)m`; its readout derivative costs `Z_t m`. Hence

\[
\|g(u)'\|_{raw}\le T_gm,\quad\|G'\|\le\sqrt2T_gm,
\quad\|M'\|\le4LT_gm,
\]
\[
B'=G'M^{-1}-GM^{-1}(G'^*G+G^*G')M^{-1},\quad
\|B'\|\le T_Bm.
\tag{NSC28}
\]

For completeness these are strong absolutely continuous identities, not formal ambient
Hessian calculations. The raw integral equations and Fubini provide coordinatewise
absolutely continuous representatives. Apply the scalar chain rule almost everywhere in
those coordinates. The displayed integrable `L2` bounds identify their Bochner integrals
with the strong differences. Bounded `c` handles the upper products; the two `L4`
factors handle `w'Q`. Measure controls cause no change: Minkowski bounds their `L4` and
`L2` integrals by total variation. Finite-dimensional absolute continuity and the anchor
gap justify the inverse differentiation. Thus (NSC28) supplies the genuine product rule
needed below.

###### 6. Original-mixture continuation inside the control tube

Write `r=(f(e1)-1,f(e2)+1)`. The exact mixture equations are

\[
\theta'=-(1-\epsilon)Gr-2\epsilon v_\nu(\theta),\qquad
r'=-(1-\epsilon)Mr-2\epsilon G^*v_\nu(\theta).
\tag{NSC29}
\]

Controls for added points remain separately tagged even at an anchor. Their total
absolute mass on the conditioned region is at most `sqrt(2)|r|+2B_r epsilon`. The
reference controls are `(e_*,-e_*)` with total mass at most 10.

First fix an arbitrary finite physical prefix `b`. Every finite-law mixture raw Euler
recursion exists without a source assumption. From `|f|<=||c||infty` and unit law mass
its readout obeys `||c_k||infty<=Y_0(e^(2b)-1)`. Summing the rank and row updates gives
bounded raw norms, actions and interpolation speed depending only on `b,Y_0`. Compare
this arbitrary recursion with the existing reference GF using the latter's passive
tails. The same factor subtraction as (NSC13), on the larger prefix ball, gives

\[
\sup_{t\le b}\|\theta^h_{\mu_{\epsilon,\nu}}(t)-\theta_*(t)\|_{raw}
\le C_be^{C_b(1+R)b}
       \{(1+R)(\epsilon+h)+e^{-c_{src}R^2}\}.
\tag{NSC30}
\]

The error `epsilon` is the changed force evaluated at the reference, bounded using added
mass one and bounded labels. The mesh term is the preceding-node interpolation error.
Only the reference's readout supremum and query tails enter the nonlinear comparison.
This is C.4.9 C.6's unchanged prefix inequality with its finite sums integrated against
the added law; every constant remains independent of support. Choose `R` proportional to
`sqrt(log(e/(epsilon+h)))`, with factor large enough that the Gaussian term is a fixed
power of `epsilon+h`. The resulting bound, denoted `omega_b(epsilon+h)`, tends to zero.

Scalar prediction continuity also bounds the actual tagged control discrepancy on this
prefix by

\[
D^h_{\epsilon,b}:=\int_0^b\left[
\sum_{a=1}^2|a_a^h-a_{*,a}|+
2\epsilon\int|f_{\theta_k^h}(u)-y|d\nu\right]dt
\le C_b\{\epsilon+h+\omega_b(\epsilon+h)\}.
\tag{NSC31}
\]

Thus integrated control closeness is proved before applying the changed-program source
estimate. For small epsilon and mesh, these prefixes lie in a strict source tube. Their
now capped refinements are Cauchy by the one-reference modulus, constructing their
strong prefix GF and preserving uniform convergence to the reference as epsilon
decreases at every separately fixed `b`.

Include `b` as a node and continue actual mixture Euler, with inner stopping radii
`rho_s/2,delta_src/2` and outer radii `rho_s,delta_src`. Choose each step so its affine
segment remains inside the outer regions and meets `h_src` in the dominating control
clock. Every fractional step is source admissible, as noted in §5. Put

\[
\lambda_0=k/4,\quad F=2\sqrt2B_rL^2,\quad
R_{max}=\sqrt2(c_b+1),\quad C_R=2\sqrt2LT_gB_r^2.
\tag{NSC32}
\]

Using (NSC28) along the affine step and integrating the scalar chain rule twice yields

\[
r_{j+1}=[I-h_j(1-\epsilon)M_j]r_j
 -2h_j\epsilon G_j^*v_{\nu,j}+R_j,
\qquad |R_j|\le C_Rh_j^2(|r_j|+\epsilon)^2.
\tag{NSC33}
\]

Indeed node control mass is at most `2B_r(|r_j|+epsilon)`; gradient derivative and raw
velocity are bounded by `T_g` and `L` times that mass. The two anchor remainders
contribute the factor `sqrt(2)`. Choose additionally

\[
h_j\le\min\{(2L^2)^{-1},\ k/[8C_R(R_{max}+1)]\}.
\tag{NSC34}
\]

For `epsilon<=1/2`, the first matrix in (NSC33) has norm at most `1-lambda_0 h_j`. Since
residuals are at most `R_max`, the remainder is absorbed to give contraction `k/8` and
forcing `F+k/8`:

\[
|r_{j+1}|\le(1-kh_j/8)|r_j|+(F+k/8)h_j\epsilon.
\]

Telescoping and summing the absolute controls therefore give

\[
\sum_{j:b\le t_j<t_N}h_jm_j
\le\frac{8\sqrt2}{k}|r_b|+C_s\epsilon(t_N-b),
\quad
\|\theta_N-\theta_b\|_{raw}\le L\sum_jh_jm_j.
\tag{NSC35}
\]

This estimate has no accumulated `hT` error. It is the reason a fixed positive slow
interval can survive arbitrarily large physical time.

The parameter choices can now be made in a fixed order. The established reference bounds
are

\[
\|\theta_*(b)-\theta_\dagger\|\le\sqrt{10}e^{-b/5},\quad
|r_*(b)|\le\sqrt2e^{-b/5},\quad
s_\dagger-s_*(b)\le10e^{-b/5}.
\tag{NSC36}
\]

Choose `b` so the endpoint error and `L(8sqrt(2)/k)|r_*(b)|` are each below `rho_s/32`,
and the reference suffix and `(8sqrt(2)/k)|r_*(b)|` are each below `delta_src/32`. These
are explicit exponential inequalities in `b`. Next choose epsilon and mesh small enough
that (NSC30)–(NSC31), and their scalar residual errors, use at most the same margins. By
(NSC4) the terms `C_s T_c` and `LC_s T_c` use at most one sixteenth of their outer
radii. Through `b+T_c/epsilon`, the full source discrepancy is at most

\[
D^h_{\epsilon,b}+(s_\dagger-s_*(b))
                 +(8\sqrt2/k)|r_b|+C_sT_c.
\tag{NSC37}
\]

The raw distance has the corresponding endpoint-plus-displacement bound from (NSC35).
Both bounds remain strictly below the inner half-radii; a first exiting node is
impossible. Thus the finite-law Euler programs continue through that horizon with
uniform source bounds. At every fixed positive epsilon this is finite physical time, so
one-reference comparison makes their mesh limits Cauchy. Their equations and tails pass
to the unique strong original GF.

For Borel laws, compare finite quantizations on the fixed horizon
`T=b+T_c/epsilon`. Their complete
source-tube controls have total mass at most `H`. At every prefix the elementary updates
therefore give

\[
\|c\|_\infty\le H,\quad\|A\|\le a_s:=2+H^2/2,
\quad\|w\|_2\le W_s:=\sqrt2+H^2+H^4/8.
\]

The same query `q_4` and row `W_4` bounds apply. In (NSC3), (NSC19) and (NSC20) replace
`a_b,c_b,W` by `a_s,H,W_s`; denote the resulting gradient, input and law constants by
`C_(g,s),L_(x,s),Lambda_s`, and let `L_s=sqrt(1+H^2(1+a_s^2))`. For the physical field,
which has no projector, direct residual-gradient subtraction now gives state coefficient
`K_s=2{L_s^2+(H+Y_0)C_(g,s)}`. Its law difference at fixed state is at most `epsilon
Lambda_s W1(nu_l,nu_j)`, since the anchor components are identical. Thus (NSC21) on the
fixed horizon has initial error `epsilon Lambda_s T W1(nu_l,nu_j)` and coefficient
`K_s`. It makes the finite-law paths Cauchy, uniformly in time. Their integral
equations, bounds (NSC35)–(NSC37) and source tails pass to the Borel limit. This
supplies every empirical law, including exceptional repeated or rank-deficient samples.
No almost-everywhere restriction on laws is needed.

###### 7. The exact residual identity and capture on the slow clock

On the reached physical interval the residual equation gives

\[
|r(t)|\le r_b e^{-\lambda_0(t-b)}+H_r\epsilon,
\qquad H_r=F/\lambda_0,
\]
\[
\int_b^t|r(s)|ds\le r_b/\lambda_0+H_r\epsilon(t-b),
\qquad r_b=|r(b)|.
\tag{NSC38}
\]

Pair (NSC29) with `r/|r|` and regularize at zero to obtain these inequalities. Its exact
projected identity is

\[
\theta'=\epsilon V_\nu(\theta)+B(\theta)r'.
\tag{NSC39}
\]

It follows by multiplying the residual equation by `GM^{-1}`; the two exact anchor
weights are already included in (NSC29). Equation (NSC28), with `m<=sqrt(2)|r|+2B_r
epsilon`, legitimizes the absolutely continuous product rule and hence

\[
\theta(t)=\theta(b)+B(t)r(t)-B(b)r(b)
 +\epsilon\int_b^tV_\nu(\theta(s))ds-\int_b^tB'(s)r(s)ds.
\tag{NSC40}
\]

For `t-b<=T_c/epsilon`, (NSC38) bounds the last integral by

\[
T_B\left\{
\frac{\sqrt2}{2\lambda_0}r_b^2
+\frac{2\sqrt2H_r+2B_r}{\lambda_0}\epsilon r_b
+(\sqrt2H_r^2+2B_rH_r)\epsilon T_c\right\}.
\tag{NSC41}
\]

This follows by squaring the first bound of (NSC38), integrating its exponential terms,
and adding `2B_r epsilon integral |r|`. Define `tilde
theta_(epsilon,b,nu)(tau)=theta_mu(b+tau/epsilon)`. Equations (NSC40)–(NSC41) make its
integral equation equal to (NSC6) with an error whose uniform norm is at most

\[
\|\theta_\mu(b)-\theta_\dagger\|
+\sqrt{2/k}(2r_b+H_r\epsilon)
+\text{the right side of (NSC41)}.
\tag{NSC42}
\]

At fixed `b`, its epsilon-limsup is bounded uniformly over laws by

\[
E_b=\sqrt{10}e^{-b/5}
+2\sqrt{2/k}\sqrt2e^{-b/5}
+T_B\frac{\sqrt2}{\lambda_0}e^{-2b/5},
\tag{NSC43}
\]

using the prefix convergence and (NSC36). Compare its integral equation with (NSC6),
taking the constrained path on the source-bearing side. The difference is bounded by
`O_(mathcal K,T_c)(E_b)` in the epsilon-limsup. The same `T_c` works for every
sufficiently large `b`; only epsilon and proof mesh need further decrease. Sending `b`
to infinity proves shifted capture. At original unshifted times `tau>=tau_->0`, write
`sigma=tau-epsilon b>=0`. The constrained path changes by at most `V_s epsilon b`
between `sigma` and `tau`. This proves (NSC8). Forward subtraction and (NSC12) give its
stated whole-circle prediction and hidden consequences. The actual reference at these
same physical times tends to `theta_dagger`.

The exclusion of zero slow time is necessary: the original initialized state is not the
fitted endpoint. The reference prefixes used in the proof do not alter the mixture law
or create a pretraining phase.

###### 8. Actual finite GF and paired whole-circle observations

Fix a positive epsilon and `T=T_c/epsilon`. At every finite width the Borel-law field is
a smooth finite-dimensional field. Its derivatives may be integrated against the law
because they are bounded over compact parameter sets and the compact data space. Loss
dissipation bounds raw displacement by `sqrt(T L_n(0))` and

\[
\|c_n(t)\|_\infty\le\|c_n(0)\|_\infty+2T\sqrt{\mathcal L_n(0)}.
\tag{NSC44}
\]

Together with the initialized action norm and Frobenius increment, these bounds prevent
finite-time escape and prove global finite GF. On the Gaussian initial events of
probability tending to one they give a common raw ball, readout supremum and bounded
velocity for this separately fixed physical horizon.

Choose a finite added-law quantization `nu_l` at transport error `h_l`, and a separately
fixed population Euler partition for its mixture GF. Freeze that population program's
scalar coefficients and run it on the actual finite Gaussian arrays. This is a fixed
finite program before width grows. The III.F finite-program theorem and A.1–A.2 identify
its joint values and second moments with the same action in both orientations. Its
actual initial readout is retained. To check its vanishing population contribution,
compare it to the zero-readout oracle on the same first/middle arrays. The initial RMS
error tends to zero, and

\[
\Pr(\max_j|c_{n,j}(0)|>r)\le2n\exp(-n^2r^2/2)\longrightarrow0.
\tag{NSC45}
\]

At each of the finitely many changed gate products, split the fixed oracle factor at a
cutoff. Its bounded part is controlled by the preceding raw error; its remainder is
controlled by an empirical soft-tail second moment, which converges at fixed program and
tends to zero as the cutoff grows. Direct action and rank differences control the other
terms. Induction gives the actual-readout proxy's joint law. This is C.4.9 D.2's
fixed-program argument, and sets no actual finite readout to zero.

We give the extra comparison needed for Borel training. For two finite states use

\[
d_n^2=\|\Delta W^1\|_F^2/n+\|\Delta W^2\|_F^2
                                      +\|\Delta c\|_2^2/n.
\]

Couple the actual added law to `nu_l`. At paired inputs `u,v`, forward/action
subtraction costs `C_T(d_n+|u-v|)` in RMS. A changed lower gate against the proxy query
has normalized norm at most

\[
C_TR(d_n+|u-v|)+C_T\tau_{R,n}(Q_{proxy}(v)),
\qquad\tau_{R,n}(q)=\|q1_{|q|>R}\|_2/\sqrt n.
\tag{NSC46}
\]

The proxy's bounded readout controls the upper gate; the finite rank identity is
`||ab^T/n||F=(||a||2/sqrt(n))(||b||2/sqrt(n))`. Residual subtraction additionally costs
`C_T(d_n+|u-v|+|y-z|)`. Integrating the coupling therefore adds only `C_T(1+R)h_l` and a
proxy-weighted sum of finite query tails. The two anchor masses are coupled identically.
There is no claim about a random supremum of finite feedback controls.

Let `h` be the maximal physical proxy step and `zeta_(n,h,l)` its finite maximum
population-coefficient prediction error. In (NSC47), `j` ranges over the entire quantized mixture, including the two anchors,
and `p_j` denotes its full mixture weights, with sum one. Coupling anchor inputs
identically removes their transport error, not their state-comparison tails.
The same one-reference comparison as C.4.9 D.2 now gives

\[
\sup_{t\le T}d_n(t)\le C_Te^{C_TR}
\left[(1+R)(h+h_l+\zeta_{n,h,l})
+\sup_t\sum_jp_j\tau_{R,n}(Q_{proxy}(t,u_j))
+\sup_t\tau_{R,n}(c_{proxy}(t))\right].
\tag{NSC47}
\]

Both finite states have the same initial arrays. Constants are fixed independently of
quadrature and fine mesh: the proxy's total control mass and population raw bounds were
uniform. At fixed `l,h,R`, `zeta` tends to zero in probability. The empirical soft-tail
squares are continuous second-moment observations of this fixed program. Their
convergence and

\[
\tau_{2R,n}(q)\le2\|(|q|-R)_+\|_2/\sqrt n
\tag{NSC48}
\]

bound the width-limsup of the tail term by `C exp(-cR^2)`. This is uniform over
interpolation time: first append a finite interpolation grid; then use the bounded raw
speed and the `L2` Lipschitz bounds for `Q,c` on the common ball with bounded readout.
Soft-tail norms are one-Lipschitz in RMS, so grid refinement supplies the claimed time
bound. Population queries at fractional steps have the source estimate by their
fractional-update representation.

Given an error, first choose finite `R` so the amplified Gaussian tail is small, then
finite quantization and mesh so their amplified errors are small, and finally let width
grow at this fixed program. Strong population quantization and Euler completion identify
the unique mixture path. Thus no growing transcript is used in a fixed-program width
theorem.

On the common finite balls, `sup_u|f_n(theta,u)-f_n(bar theta,u)|<=C_Td_n` and both
hidden RMS differences are at most `C_Td_n`. Input Lipschitz constants are bounded by
products of readout RMS, action norm and full-row RMS; the hidden bounds omit the
readout factor. Their population versions hold in `L2`. Finite input and time nets
therefore upgrade proxy prediction convergence to `C([0,T] x sqrt(2)S1)`.

For the paired statement, run reference and mixture proxies on the same arrays and apply
the fixed-program theorem to their finite union. Their paired hidden products are
bounded second-moment observations. For `ell=1,2`, define

\[
D_{\ell,n,\epsilon,\nu}(t,u)=
\frac1n\|h^\ell_{n,\mu_{\epsilon,\nu}}(t,\sqrt2u)
                   -h^\ell_{n,\nu_*}(t,\sqrt2u)\|_2^2.
\tag{NSC49}
\]

At fixed epsilon they converge in probability, uniformly over `[0,T] x S1`, to

\[
D_{\ell,\epsilon,\nu}(t,u)=
\|H^\ell_{\theta_{\mu_{\epsilon,\nu}}(t)}(u)
                              -H^\ell_{\theta_*(t)}(u)\|_2^2.
\tag{NSC50}
\]

Indeed RMS hidden closeness passes each squared distance by Cauchy–Schwarz; bounded
activations and uniform spatial/time `L2` moduli pass from finite nets to the full
domain. Equation (NSC8) and reference convergence then identify their epsilon-limit,
uniformly for `tau_-<=tau<=T_c` and all inputs, as

\[
\|H^\ell_{\theta_\nu(\tau)}(u)-H^\ell_{\theta_\dagger}(u)\|_2^2.
\tag{NSC51}
\]

The uniform statement allows integration against any fixed observation probability on
the circle, including laws with atoms. All paired quantities use the same
initialization; this measures adaptation after reference fitting, with no endpoint
substituted at finite width.

Finally, for a random empirical added law independent of initialization, condition on
its realized observations. The finite-GF theorem holds for every such fixed law.
Conditional failure probabilities converge to zero and are bounded by one, so dominated
convergence removes the conditioning. Width is taken first at each positive epsilon; the
original-mixture capture then takes epsilon to zero. A later sampling limit is separate.
These steps retain the actual finite Gaussian readout and both orientations of the
reused middle action throughout.

##### C.4.10.3. Continuum separation and finite target conditioning

Write \(u_\alpha=(\cos\alpha,\sin\alpha)\), with angles modulo \(2\pi\),
and let \(\rho(d\alpha)=d\alpha/(2\pi)\) be normalized arc measure on the
entire normalized circle. Physical inputs are \(x=\sqrt2u_\alpha\).
Fix \(D\ge0\) and the density class
\[
 {\cal P}_D=\{p\in C(S^1):\ \tfrac12\le p\le2,\quad
          \int p\,d\rho=1,\quad \operatorname{Lip}_{S^1}(p)\le D\},
 \tag{NSS1}
\]
where the Lipschitz constant uses shortest circular angle distance.
The uniform density belongs to this class, including when \(D=0\).

Use the fitted reference state \(\theta_\dagger=(w_\dagger,K_\dagger,
c_\dagger)\) and its actual action \(A_\dagger=A_0+K_\dagger\) from
C.4.5 and C.4.9. At that state abbreviate
\[
 \begin{aligned}
 H^1(u)&=\tanh(w_\dagger\cdot u),&
 Z^2(u)&=A_\dagger H^1(u),& H^2(u)&=\tanh Z^2(u),\\
 \delta(u)&=c_\dagger\operatorname{sech}^2Z^2(u),&
 Q(u)&=A_\dagger^*\delta(u).
 \end{aligned}
\]
\[
 g(u)=\bigl(u\operatorname{sech}^2(w_\dagger\cdot u)Q(u),
                \delta(u)\otimes H^1(u),\,H^2(u)\bigr),\qquad
 F_*(\alpha)=\langle c_\dagger,H^2(u_\alpha)\rangle.
 \tag{NSS2}
\]
Here \(g(u)\) is the scalar prediction gradient in the raw Hilbert
increment space \({\cal E}\). Its hidden subspace \({\cal E}_H\) contains
the first-row and middle Hilbert--Schmidt blocks; it excludes the readout.
Only the middle increment is Hilbert--Schmidt. The initialized action and
the adjoint in (NSS2) are the same retained Gaussian action and its true
Hilbert adjoint.

The reference bounds used below are
\[
 \|c_\dagger\|_2\le C:=\sqrt{10},\quad \|c_\dagger\|_\infty\le10,
 \quad\|A_\dagger\|_{\rm op}\le M:=2+\sqrt{10},\quad
 \|w_\dagger\|_2\le W:=\sqrt2+\sqrt{10}.
 \tag{NSS3}
\]
Consequently \(\sup_u\|g(u)\|\le L_0:=\sqrt{1+C^2(1+M^2)}<17\).
The fields \(H^1,H^2,g,F_*\) are odd in \(u\), whereas \(\delta,Q\)
are even. The reference fits \(F_*(0)=1,F_*(\pi/2)=-1\), and its input
Lipschitz constant is at most \(CMW<76\).

We first prove separation for signed input measures. This gives
injectivity of the constrained gradient even in its middle block.
Compactness then explains why a positive lower bound must be restricted
to the finite target spaces defined below.

###### Protected rows separate odd signed measures

Let \(\mathfrak F(z)=z/2+\sinh(2z)/4\), so
\(\mathfrak F'(z)=\cosh^2z\). The reference feature clock on
\(0\le s\le s_\dagger\le10\) satisfies
\[
 \mathfrak F(w_a(s))-\mathfrak F(g_a)=X_a(s),\qquad
 X_a(s)=\tfrac12y_a\int_0^s Q(e_a;v)\,dv,\qquad
 (y_1,y_2)=(1,-1),
 \tag{NSS4}
\]
with independent standard normal roots \(g_1,g_2\).
The reference source bound in C.4.9.A gives a finite constant \(C_Q\)
such that \(\sup_{s,a}\|Q(e_a;s)\|_{L^r}\le C_Q\sqrt r\) for every
\(r\ge2\). Equivalently this follows from C.4.6.S40--S44.
Define the nonnegative random variable
\[
 \begin{gathered}
 N_{\rm ref}=\tfrac12\sum_{a=1}^2\int_0^{s_\dagger}|Q(e_a;s)|\,ds,
 \qquad C_{\rm env}:=10C_Q,\\
 \|N_{\rm ref}\|_{L^r}\le C_{\rm env}\sqrt r,\qquad
 \sup_s|X_a(s)|\le N_{\rm ref}\quad\hbox{almost surely}.
 \end{gathered}
 \tag{NSS5}
\]
Minkowski proves the moment bound. The strong integral equations and
Fubini give the simultaneous clock bound. This uses integrals of the
active queries, without a random supremum over passive inputs.
Taking \(r=(z/(eC_{\rm env}))^2\ge2\) in Markov's inequality gives
\[
             \Pr\{N_{\rm ref}>z\}\le \exp[-z^2/(e^2C_{\rm env}^2)].
 \tag{NSS6}
\]
No independence of \(N_{\rm ref}\) and the first-row roots is asserted.

Fix a unit vector \(v\) with nonzero coordinates. For every sufficiently
large positive integer \(R_{\rm box}\), the Gaussian density gives
\[
 \Pr\{|g-R_{\rm box}v|_\infty\le1\}
       \ge(2/\pi)\exp[-(R_{\rm box}+\sqrt2)^2/2]
                     >\Pr\{N_{\rm ref}>R_{\rm box}^2\}.
 \tag{NSS7}
\]
Thus the box intersects \(\{N_{\rm ref}\le R_{\rm box}^2\}\) in positive probability.
On that intersection put \(c_v=\min_a|v_a|/2>0\); for large \(R_{\rm box}\),
\(|g_a|\ge c_vR_{\rm box}\). The minimum of \(\mathfrak F'\) on
\([g_a-1,g_a+1]\) is at least \(e^{2(|g_a|-1)}/4>R_{\rm box}^2\).
Monotonicity and (NSS4)--(NSS5) first place \(w_a(s)\) inside that
interval and then imply
\[
 \sup_{s\le s_\dagger}|w_a(s)-g_a|
                  \le4R_{\rm box}^2e^{-2(|g_a|-1)}\longrightarrow0.
 \tag{NSS8}
\]
For example, leaving the interval would change \(\mathfrak F\) by more
than \(R_{\rm box}^2\), contrary to (NSS5); the displayed bound then follows by
integrating its derivative between \(g_a\) and \(w_a(s)\).

**Signed-measure separation.** If a finite real signed Borel measure
\(\mu\) on the circle is odd under \(u\mapsto-u\), then
\[
             \int H^1(u)\,d\mu(u)=0\ \hbox{in }H_1
                    \quad\Longrightarrow\quad \mu=0 .
 \tag{NSS9}
\]
The integral is Bochner integrable, since \(H^1\) is continuous into
\(H_1=L^2(\Omega_1)\) and bounded by one in norm.

To prove (NSS9), intersect each positive-probability event in (NSS7)
with the full-measure sets where the clock identities and the asserted
zero integral hold. Choose one first-layer coordinate from each
intersection. Along these choices \(w_\dagger/R_{\rm box}\to v\).
If the two inputs perpendicular to \(v\) are not atoms of \(|\mu|\),
bounded convergence against the total variation gives
\[
 \int\operatorname{sign}(v\cdot u)\,d\mu(u)=0.
 \tag{NSS10}
\]
A finite measure has at most countably many atoms: for every positive
integer \(k\), only finitely many can have mass at least \(1/k\).
The excluded perpendicular directions and coordinate-axis directions
therefore form a null set of angles. Consequently
\(S(\beta)=\int\operatorname{sign}(\cos(\alpha-\beta))\,d\mu(\alpha)\)
vanishes for almost every \(\beta\).

For \(k(t)=\operatorname{sign}(\cos t)\), direct integration on the two
half circles gives
\[
 \widehat k(j):=\int k(t)e^{-ijt}\,d\rho(t)
       =\frac{2\sin(j\pi/2)}{\pi j}\ (j\ne0),\qquad \widehat k(0)=0.
 \tag{NSS11}
\]
Indeed its sine integrals vanish, and subtracting the complementary
half-circle cosine integral doubles the integral on
\((-\pi/2,\pi/2)\). Fubini applies to the bounded kernel and finite
variation measure, and gives
\(\widehat S(j)=\widehat k(j)\int e^{-ij\alpha}\,d\mu(\alpha)\).
Every odd Fourier coefficient of \(\mu\) is zero. Oddness already
annihilates each even coefficient, including its total mass.

Here is the required uniqueness step for finite measures. The Fejer kernels
\[
 {\cal K}_m(t)=\frac1{m+1}\left|\sum_{j=0}^m e^{ijt}\right|^2
 \tag{NSS12}
\]
are nonnegative and have \(\rho\)-integral one. Outside circular distance
\(\eta>0\) from zero they are at most
\(((m+1)\sin^2(\eta/2))^{-1}\), by the finite geometric sum.
Uniform continuity therefore makes \({\cal K}_m*f\to f\) uniformly
for every continuous circle function \(f\): split its convolution error
inside and outside that neighborhood, then decrease \(\eta\).
These convolutions are trigonometric polynomials, so all their integrals
against \(\mu\) vanish. Hence \(\int f\,d\mu=0\) for every continuous
\(f\). Continuous ramps converging to an arc indicator give zero mass
on every arc whose endpoints are not atoms of \(|\mu|\), by dominated
convergence. Choose a dense set of such endpoints. Finite unions of
these arcs form a generating algebra, and continuity under monotone
limits extends the zero measure to all Borel sets. This proves (NSS9).

###### The middle block and the anchor projection

The stronger weighted assertion is
\[
 \int\delta(u)\otimes H^1(u)\,d\mu(u)=0
      \ \hbox{in }{\cal S}_2(H_1,H_2),\quad \mu\ \hbox{finite and odd}
                         \quad\Longrightarrow\quad\mu=0.
 \tag{NSS13}
\]
The integrand is continuous in Hilbert--Schmidt norm: the first feature
is \(L^2\)-continuous, the bounded action preserves continuity, and
\[
 \|\delta(u)-\delta(v)\|_2
       \le2\|c_\dagger\|_\infty\|Z^2(u)-Z^2(v)\|_2 .
\]
Rank-one subtraction then gives the asserted continuity and
integrability against \(|\mu|\).

We make the representatives needed for (NSS13) explicit. Work with this
fixed finite measure \(|\mu|\), which is even when \(\mu\) is odd.
Approximate the continuous map \(u\mapsto Z^2(u)\in H_2\) uniformly
in \(L^2\) by simple input fields. A subsequence converges in the product
measure \(|\mu|\otimes\mathbb P_2\), giving a jointly measurable
representative finite almost everywhere and representing \(Z^2(u)\)
for \(|\mu|\)-almost every input. Construct on one semicircle and extend
by oddness; this also retains the separately chosen values at any named
atoms and their antipodes. Applying the gate with the fixed representative
of \(c_\dagger\) makes \(\delta(u,z)\) even, jointly measurable, and
bounded by 10. No exceptional set uniform over all measures is required.

The Hilbert--Schmidt norm of a finite sum of tensors equals the \(L^2\)
norm of its kernel on \(\Omega_2\times\Omega_1\): expansion gives
\(\sum_{i,j}\langle a_i,a_j\rangle_2\langle b_i,b_j\rangle_1\)
on both sides for \(\sum_i a_i\otimes b_i\).
Bochner simple approximations and completion therefore identify the
kernel of the integral in (NSS13) with
\(\int\delta(u,z)H^1(u,\omega_1)\,d\mu(u)\).
Boundedness by \(10|\mu|(S^1)\) justifies Fubini. The zero operator
thus gives a zero first-layer integral for almost every \(z\in\Omega_2\).

The readout is nonzero since
\(\langle c_\dagger,H^2(e_1)\rangle=1\). Choose \(z\) outside all the
preceding null sets with \(c_\dagger(z)\ne0\).
The measure \(d\mu_z(u)=\delta(u,z)d\mu(u)\) is finite and odd.
By (NSS9) it is zero. For \(|\mu|\)-almost every \(u\), its multiplier
\(c_\dagger(z)\operatorname{sech}^2Z^2(u,z)\) is nonzero, because its
preactivation is finite. The identity
\(|\mu_z|=|\delta(\cdot,z)|\,|\mu|\) then forces \(|\mu|=0\).
This proves (NSS13), without assuming injectivity of \(A_\dagger\).

Let \(G:\mathbb R^2\to{\cal E}\) have columns \(g(e_1),g(e_2)\).
If their middle blocks had a nontrivial linear relation, (NSS13) applied
to \(\frac12\sum_a\beta_a(\delta_{e_a}-\delta_{-e_a})\) would make
all its coefficients zero. Thus
\[
 M_\dagger=G^*G>0,\qquad
 \Pi_\dagger=I-GM_\dagger^{-1}G^*,\qquad d(u)=\Pi_\dagger g(u).
 \tag{NSS14}
\]
These are the same anchor Gram and orthogonal projection as in C.4.9.
Write \(d_H(u)\) for the first-row/middle block of \(d(u)\).

For \(p\in{\cal P}_D\), let \({\cal H}_p\) be the real closed odd subspace
of \(L^2(p\rho)\), with norm \(\|\cdot\|_p\). Closure follows from
equivalence with the \(L^2(\rho)\) norm. Its norm and all force integrals
below are unchanged on replacing \(p\) by
\(p_s(u)=(p(u)+p(-u))/2\): products of two odd functions are even.
Define
\[
 T_pa=\int a(u)d(u)p(u)d\rho(u),\qquad
 T_{H,p}a=\int a(u)d_H(u)p(u)d\rho(u).
 \tag{NSS15}
\]
Both operators have norm at most \(L_0\), by Cauchy--Schwarz.
They are injective, even after retaining only their middle block.
Indeed set \(U=\int a(u)g(u)p(u)d\rho(u)\) and
\(\beta=M_\dagger^{-1}G^*U\). A zero middle block gives (NSS13) for
\[
 d\mu=a(u)p_s(u)d\rho(u)
            -\tfrac12\sum_{b=1}^2\beta_b
                              (\delta_{e_b}-\delta_{-e_b}).
 \tag{NSS16}
\]
This is a finite odd measure since \(a\in{\cal H}_p\subset L^1(p\rho)\).
Its absolutely continuous and atomic parts are mutually singular.
The conclusion \(\mu=0\), together with \(p_s\ge1/2\), gives \(a=0\).

###### Compact operators and uniform finite target conditioning

The endpoint map \(u\mapsto g(u)\) is raw-norm continuous.
To check its only unbounded gate product, subtract \(Q(u)-Q(v)\) first.
The remaining bounded multiplier difference converges against the fixed
\(Q(v)\in L^2\): truncate \(|Q(v)|\) at a fixed level, use bounded
convergence on the truncated part, then remove its \(L^2\) tail.
Forward fields, upper gates, the actual adjoint, and the rank-one block
are continuous by their factorwise bounds. Hence \(d,d_H\) are continuous.
Finite input partitions approximate them uniformly by finitely valued
kernels. Their induced finite-rank operators approximate \(T_p,T_{H,p}\)
in operator norm, with error at most the kernel's uniform error.
Thus these operators are compact.

There is no positive coercivity constant on all of \({\cal H}_p\).
This space is infinite-dimensional since positive density preserves
linear independence of all odd trigonometric modes. For an orthonormal
sequence \(a_j\), every finite-rank operator sends \(a_j\) to zero in
norm, by Bessel's inequality applied to its finitely many linear
functionals. Finite-rank approximation then gives
\(\|T_pa_j\|\to0\) and \(\|T_{H,p}a_j\|\to0\).
The finite-dimensional restriction below supplies the needed lower bounds.

Put \(q_0(\alpha)=\cos^3\alpha-\sin^3\alpha\) and
\(h(\alpha)=\sin^2(2\alpha)\). For each integer \(N\ge0\), define
\[
 E_N=\operatorname{span}\{F_*-q_0,\,
 h\cos((2k+1)\alpha),\,h\sin((2k+1)\alpha):0\le k\le N\}.
 \tag{NSS17}
\]
All generators are odd Lipschitz functions vanishing at the anchors.
The space is nonzero because \(h\cos\alpha\) is nonzero. It contains
\(F_*-q_N\) for every target whose prescribed series \(v\) has coefficient
indices at most \(N\). The actual harmonic degree of that target is at
most \(2N+5\); \(E_N\) itself also retains the possibly nonpolynomial
reference generator \(F_*-q_0\) exactly.

Let \(d_N=\dim E_N\). Delete any exact dependencies using the
\(L^2(\rho)\) Gram of the listed generators, and orthonormalize the
remaining functions to obtain \(b_1,\ldots,b_{d_N}\).
This chooses a fixed basis independent of \(p\) and of target coefficients.
For \(p\in{\cal P}_D\), define real \(d_N\times d_N\) matrices
\[
 \begin{aligned}
 C_N(p)_{ij}&=\int b_i b_jp\,d\rho,\\
 A_N(p)_{ij}&=\langle T_pb_i,T_pb_j\rangle_{\cal E},\\
 A_{H,N}(p)_{ij}&=\langle T_{H,p}b_i,T_{H,p}b_j\rangle_{{\cal E}_H}.
 \end{aligned}
 \tag{NSS18}
\]
One has \(\frac12I\le C_N(p)\le2I\), and both other matrices are
positive definite by (NSS15)--(NSS16).
Their uniform generalized eigenvalue bounds are
\[
 \lambda_N=\min_{\substack{p\in{\cal P}_D\\z^TC_N(p)z=1}}
                          z^TA_N(p)z,\qquad
 \lambda_{H,N}=\min_{\substack{p\in{\cal P}_D\\z^TC_N(p)z=1}}
                          z^TA_{H,N}(p)z .
 \tag{NSS19}
\]
Both minima exist and satisfy \(0<\lambda_{H,N}\le\lambda_N\le L_0^2\).
Here are the compactness details establishing strict positivity uniformly.
Bounded densities have a subsequence converging on a fixed countable
dense set, by diagonal extraction. The common Lipschitz bound makes that
subsequence uniformly Cauchy, using a finite sufficiently fine input net.
Its uniform limit preserves the bounds, integral and Lipschitz constant.
Thus \({\cal P}_D\) is compact. All entries in (NSS18) are continuous
in the uniform density norm, by bounded kernels and their Bochner integrals.
The constraint in (NSS19) gives \(|z|\le\sqrt2\); it is closed and
prevents a limiting vector from being zero. Its feasible set is therefore
compact. A zero attained minimum would contradict injectivity of \(T_p\)
or \(T_{H,p}\) on the nonzero function \(\sum_i z_i b_i\).
The upper and ordering bounds follow from (NSS15) and the hidden
coordinate projection being a contraction.

In particular, for every \(p\in{\cal P}_D\) and \(a\in E_N\),
\[
 \|T_pa\|^2\ge\lambda_N\|a\|_p^2,\qquad
 \|T_{H,p}a\|^2\ge\lambda_{H,N}\|a\|_p^2 .
 \tag{NSS20}
\]
These constants depend only on \(N,D\) and the specified reference.
They are defined by finite matrices and a compact density minimization;
no numerical value or positive bound uniform as \(N\to\infty\) is asserted.
The reference residual is included exactly in \(E_N\); subsequent
approximation errors concern the prescribed target tail and the movement
of the actual nonlinear state.

##### C.4.10.4. Nonlinear approximation, noisy samples and a positive stop

Use the common source neighborhood, constants \(L,C_g,\mathcal K,\rho_s\)
and episode \(T_c>0\) from C.4.10.2, with label bound \(Y_0=1\). Put
\[
 C=\sqrt{10},\quad M_b=2+\sqrt{10},\quad a_b=M_b+1,\quad c_b=C+1,
 \quad B_0=C+1,
\]
\[
 L_0=\sqrt{1+C^2(1+M_b^2)},\quad
 C_d=C_g(1+4L/\sqrt{k}),\quad V=2(c_b+1)L,
 \quad k=\lambda_{\min}(M_\dagger).
 \tag{NGL1}
\]
Thus \(\|g_\dagger(u)\|\le L_0\), while \(\|g_\theta(u)\|\le L\)
and \(|f_\theta(u)|\le c_b\) in the common unit endpoint ball. The constants
\(\lambda_N,\lambda_{H,N}>0\) refer to the finite matrices in C.4.10.3.
Every constant in this subsection is determined by the reference and declared
class parameters. In particular no unknown changed-law solution enters them.

**Population approximation theorem.** Let \(q_N\) truncate (NG5) at index
\(N\), and use either the actual coefficient tail
\(a_N=\sum_{k>N}(|a_k|+|b_k|)\) or its class bound
\(a_N=R/(2N+3)^s\). For a class with declared finite cap \(N\), take
\(a_N=0\). If
\[
 0<T\le T_c,\qquad C_d^2VT\le\lambda_N/8,
 \qquad
 \mathfrak A_N(T)=2(1+2L_0^2/\lambda_N)(a_N+LVT)^2,
 \tag{NGL2}
\]
then the whole-circle reconstruction \(P_\nu\) of the actual constrained
selection satisfies, for \(0\le\tau\le T\),
\[
 \mathcal E_\nu(P_\nu(\tau))
 \le e^{-\lambda_N\tau/2}\mathcal E_\nu(F_*)
       +\mathfrak A_N(T)(1-e^{-\lambda_N\tau/2}).
 \tag{NGL3}
\]
The initial excess risk is at most \(B_0^2\). The floor in (NGL2) bounds
omitted target modes and movement away from the endpoint analysis space. It
is not defined by a trained risk. For fixed \(N\), longer training within
this admitted interval contracts toward this floor. Increasing \(N\) decreases
the target tail but may decrease \(\lambda_N\) and the admitted duration;
there is no assertion that \(a_N^2/\lambda_N\to0\), or of universal
consistency.

To prove the theorem, abbreviate
\(r_\tau=f_{\theta_\nu(\tau)}-q\), \(E(\tau)=\|r_\tau\|_p^2\), and
\[
 T_{\theta,p}r=\int r(u)\Pi_\theta g_\theta(u)p(u)\,d\rho(u).
\]
The scalar gradient rule and bounded Bochner integrands give the exact identity
\[
 E'(\tau)=-4\|T_{\theta_\nu(\tau),p}r_\tau\|^2.
 \tag{NGL4}
\]
Centered label noise has zero population force. The velocity is bounded by
\(V\), so \(\|\theta_\nu(\tau)-\theta_\dagger\|\le V\tau\).
The state comparison in C.4.10.2 and
\(d\sqrt{\log(e/d)}\le\sqrt d\) for \(0\le d\le1\) imply
\[
 \|f_{\theta_\nu(\tau)}-F_*\|_\infty\le LV\tau,
 \qquad
 \|T_{\theta_\nu(\tau),p}-T_p\|\le C_d\sqrt{V\tau}.
 \tag{NGL5}
\]
Here \(T_p=T_{\theta_\dagger,p}\). Let \(P_N\) denote orthogonal
projection onto \(E_N\) in the odd subspace of \(L^2(p\rho)\).
Because \(F_*-q_N\in E_N\),
\[
 \|(I-P_N)r_\tau\|_p\le a_N+LV\tau=:b(\tau).
 \tag{NGL6}
\]
For vectors in any Hilbert space,
\(\|x+y\|^2\ge\frac12\|x\|^2-\|y\|^2\), as follows by completing
the square \(\frac12\|x+2y\|^2\). Apply this first to
\(T_{\theta,p}r=T_pr+(T_{\theta,p}-T_p)r\), then to
\(T_pr=T_pP_Nr+T_p(I-P_N)r\). The operator norm of \(T_p\) is at
most \(L_0\), and its finite-space conditioning gives
\[
 \|T_{\theta,p}r_\tau\|^2
 \ge(\lambda_N/4-C_d^2V\tau)E(\tau)
                -(\lambda_N/4+L_0^2/2)b(\tau)^2.
 \tag{NGL7}
\]
Orthogonality is used in the function space, not between its images under
\(T_p\); thus possible cancellation between modes has been bounded. Under
(NGL2), (NGL4) yields
\[
 E'\le-\lambda_NE/2+(\lambda_N+2L_0^2)(a_N+LVT)^2.
\]
Multiplication by \(e^{\lambda_N\tau/2}\) and integration proves (NGL3).
The training field in this argument always uses the current residual, current
features and current anchor projection.

**Sampling theorem with centered noise separated.** For positive failure
allowances \(\delta_I,\delta_\xi\) with sum less than one, define
\[
 \eta_m={2TL\over\sqrt m}
       \left({B_0\over\sqrt{\delta_I}}+
                            {\sigma\over\sqrt{\delta_\xi}}\right),
\]
\[
 \mathcal O_T(\eta)=e\exp\left[-
              \left(\sqrt{\log(e/\eta)}-\mathcal KT/2\right)^2\right].
 \tag{NGL8}
\]
Set \(\mathcal O_T(0)=0\), and require for \(\eta_m>0\) that
\(\sqrt{\log(e/\eta_m)}>1+\mathcal KT/2\). With probability at least
\(1-\delta_I-\delta_\xi\) over the added observations, simultaneously
for \(0\le\tau\le T\),
\[
 \|\theta_{\widehat\nu_m}(\tau)-\theta_\nu(\tau)\|
           \le\mathcal O_T(\eta_m),\qquad
 \|P_{\widehat\nu_m}(\tau)-P_\nu(\tau)\|_\infty
           \le L\mathcal O_T(\eta_m),
 \tag{NGL9}
\]
and therefore
\[
 \sqrt{\mathcal E_\nu(P_{\widehat\nu_m}(\tau))}
 \le\sqrt{e^{-\lambda_N\tau/2}\mathcal E_\nu(F_*)
             +\mathfrak A_N(T)(1-e^{-\lambda_N\tau/2})}
          +L\mathcal O_T(\eta_m).
 \tag{NGL10}
\]
When \(\sigma=0\), omit the noise term and allowance. For fixed episode and
confidence, the statistical error tends to zero as
\(m^{-1/2}\exp(O(\sqrt{\log m}))\). The two separate contributions in
(NGL8) display input sampling and centered label noise.

For proof, evaluate all random forcing on the deterministic population path.
Put \(d_\tau(u)=\Pi_{\theta_\nu(\tau)}g_{\theta_\nu(\tau)}(u)\) and
\[
 I_m(\tau)={1\over m}\sum_i r_\tau(X_i)d_\tau(X_i)
                   -\mathbb E[r_\tau(X)d_\tau(X)],\qquad
 N_m(\tau)={1\over m}\sum_i\xi_i d_\tau(X_i).
\]
Independence and centering eliminate off-diagonal inner products. Since
\(E(\tau)\le E(0)\le B_0^2\),
\[
 \mathbb E\|I_m(\tau)\|^2\le L^2B_0^2/m,\qquad
 \mathbb E[\|N_m(\tau)\|^2\mid X_1,\ldots,X_m]\le L^2\sigma^2/m.
 \tag{NGL11}
\]
The second assertion uses conditional independence of labels in iid pairs,
not independence between empirical trained features and their own labels.
For \(Z_I=2\int_0^T\|I_m\|\,d\tau\) and
\(Z_\xi=2\int_0^T\|N_m\|\,d\tau\), Cauchy–Schwarz in time and Tonelli
give \(\mathbb EZ_I^2\le4T^2L^2B_0^2/m\) and
\(\mathbb EZ_\xi^2\le4T^2L^2\sigma^2/m\). Markov and a union bound
give \(Z_I+Z_\xi\le\eta_m\) with the declared probability.

Subtract the two constrained integral equations by first comparing states
under the empirical law. The population state supplies the source tails for
the one-reference bound in C.4.10.2. The remaining law difference at this
fixed population state is exactly \(-2I_m+2N_m\). Thus, with
\(D(\tau)=\|\theta_{\widehat\nu_m}(\tau)-\theta_\nu(\tau)\|\) and
\(\omega(d)=d\sqrt{\log(e/d)}\),
\[
 D(\tau)\le\eta_m+\mathcal K\int_0^\tau\omega(D(s))\,ds.
 \tag{NGL12}
\]
For the scalar comparison solution, differentiating
\(\sqrt{\log(e/Z)}\) gives derivative \(-\mathcal K/2\).
Its explicit solution is (NGL8) with \(T\) replaced by \(\tau\).
The branch condition keeps it below one, so a first-exit comparison applies.
At zero forcing decrease positive upper errors to zero; equivalently the
Osgood integral diverges at zero. This proves (NGL9). The risk triangle
inequality proves (NGL10); the same event also gives the useful additive bound
\[
 |\mathcal E_\nu(P_{\widehat\nu_m}(\tau))-
       \mathcal E_\nu(P_\nu(\tau))|
       \le2(c_b+1)L\mathcal O_T(\eta_m).
 \tag{NGL13}
\]

**Robust strict learning and paired second-hidden motion.** Fix finite
\(N\ge0\), \(R>0\), \(s\ge1\), and \(D\ge0\). Inside (NG5) take
\[
 a=R/4,\qquad v=a(\cos\alpha+\sin\alpha)+w(\alpha),\qquad
 \sum_{k=0}^N(2k+1)^s(|w_{c,k}|+|w_{s,k}|)\le a/4.
 \tag{NGL14}
\]
This has nonempty relative interior in every fixed finite coefficient space,
with budget at most \(9R/16<R\). Retain every \(p\in\mathcal P_D\) and
every noise law (NG6). Its initial excess risk is uniformly bounded below by
\[
 e_*={a^2\over2}\left(\sqrt{3/8}-1/4\right)^2>0.
 \tag{NGL15}
\]
Indeed \(F_*-q_0\) is antisymmetric under the coordinate swap, while
\(\psi=h(\cos\alpha+\sin\alpha)\) is symmetric. Their inner product in
\(L^2(\rho)\) is zero, and
\(\|\psi\|_\rho^2=\int\sin^4(2\alpha)(1+\sin2\alpha)\,d\rho=3/8\).
The odd sine term integrates to zero; the remaining identity follows by
expanding \(\sin^4\). Since \(\|hw\|_\rho\le a/4\), the reverse
triangle inequality and \(p\ge1/2\) prove (NGL15). This uses full-circle
mass and an independently specified symmetric target component.

Here are explicit common stopping and hidden-observation constants. Define
\[
 \gamma=\lambda_{H,N}e_*,\quad G_0=\sqrt2L_0,\quad
 B_\beta=G_0L_0B_0/k,\quad S=B_0+\sqrt2B_\beta,\quad
 B_2=2B_0^2+B_\beta^2,
\]
\[
 C_V=2L^2+2B_0C_d,\qquad A_H=SC_gV+L_0B_0C_V,
\]
\[
 T={1\over2}\min\left\{T_c,\ {\lambda_N\over8C_d^2V},\
 {\sqrt{e_*/[4(1+2L_0^2/\lambda_N)]}\over LV},\
 {\gamma^2\over A_H^2V}\right\}>0,
\]
\[
 a_*={e_*\over2}(1-e^{-\lambda_NT/2}),\qquad
 j_*={\gamma^2T^2\over3C^2B_2}>0.
 \tag{NGL16}
\]
This deterministic stop uses only class and reference information and is
chosen before training. Its physical value is \(T/\varepsilon\). Because
\(a_N=0\), it ensures \(\mathfrak A_N(T)\le e_*/2\), so (NGL3) gives
\(\mathcal E_\nu(F_*)-\mathcal E_\nu(P_\nu(T))\ge a_*\).

The paired upper-hidden observable is
\[
 J_2(\theta)={1\over3}\left[
  \int\|H^2_\theta(u)-H^2_\dagger(u)\|_2^2\,d\rho(u)
   +\sum_{a=1}^2\|H^2_\theta(e_a)-H^2_\dagger(e_a)\|_2^2\right].
 \tag{NGL17}
\]
Both states use the same initialized carrier. The observation measure here
is uniform circle plus the two anchors, independently of the unknown test
density. The lower bound below is for their sum; it does not assert a lower
bound for its circle-only part.

To prove finite hidden displacement, put \(r_0=F_*-q\) and
\[
 u_0=\int r_0g_\dagger p\,d\rho,\quad
 \beta=M_\dagger^{-1}G_\dagger^*u_0,\quad d_0=\Pi_\dagger u_0.
\]
The hidden block consists of the first-row and middle-increment components.
Since \(r_0\in E_N\), \(\|(d_0)_H\|^2\ge\gamma\), while
\(\|r_0\|_p\le B_0\), \(|\beta|\le B_\beta\), and
\(\|d_0\|\le L_0B_0\). Keep \(r_0,\beta,c_\dagger\) fixed only in
the scalar observation
\[
 O(\theta)=\int r_0(u)\langle c_\dagger,H^2_\theta(u)\rangle p(u)\,d\rho
       -\sum_a\beta_a\langle c_\dagger,H^2_\theta(e_a)\rangle.
 \tag{NGL18}
\]
Its endpoint gradient is \(o_\dagger=((d_0)_H,0)\), and the actual
constrained velocity at the endpoint is \(-2d_0\). Hence
\(O'(0)=-2\|(d_0)_H\|^2\le-2\gamma\).

This derivative remains negative on the declared finite episode. For raw
distance \(d=\|\theta-\theta_\dagger\|\le\rho_s\), the fixed-readout
hidden gradient is the hidden part of the prediction gradient at the
auxiliary state \((w,K,c_\dagger)\). This auxiliary state is in the unit
endpoint ball. Apply the one-reference gradient estimate against the
endpoint, discard its readout component, and use \(\omega(d)\le\sqrt d\).
Integrating absolute contrast coefficients gives
\[
 \|o_\theta-o_\dagger\|\le SC_g\sqrt d.
\]
Subtracting residuals and projected gradients in the actual velocity gives
\(\|V_\nu(\theta)-V_\nu(\theta_\dagger)\|\le C_V\sqrt d\).
Therefore
\[
 |O'(\tau)-O'(0)|\le A_H\sqrt{V\tau}\le\gamma,
                         \qquad 0\le\tau\le T.
\]
Integrating yields \(|O(\theta_\nu(\tau))-O(\theta_\dagger)|\ge\gamma\tau\).
Finally Cauchy–Schwarz in the upper population and in the direct sum of the
circle and two anchor observations, using
\(\int r_0^2p^2\,d\rho\le2B_0^2\), proves
\[
 |O(\theta)-O(\theta_\dagger)|^2\le3C^2B_2J_2(\theta),\qquad
 J_2(\theta_\nu(\tau))\ge{\gamma^2\tau^2\over3C^2B_2}.
 \tag{NGL19}
\]
This establishes \(J_2(\theta_\nu(T))\ge j_*\) for evolving second-hidden
activations, rather than inferring it from parameter motion or an initial
derivative alone.

**An explicit sample threshold and the actual GF conclusion.** Let
\(0<\delta<1\), take \(\delta_I=\delta_\xi=\delta/2\) when \(\sigma>0\),
and take only \(\delta_I=\delta\) when \(\sigma=0\). Put
\[
 H_L=\sqrt{1+a_b^2},\quad
 d_* =\min\{1/2,\ a_*/[8(c_b+1)L],\ j_*/[16H_L]\},
\]
\[
 C_{\rm sample}=2TL\left({B_0\over\sqrt{\delta_I}}
                       +{\sigma\over\sqrt{\delta_\xi}}\right),\quad
 \eta_* = e\exp[-(\sqrt{\log(e/d_*)}+\mathcal KT/2)^2],
\]
\[
 m_* =\max\{1,\lceil(C_{\rm sample}/\eta_*)^2\rceil\}.
 \tag{NGL20}
\]
The noise summand is omitted in the noiseless case. For \(m\ge m_*\),
inverting (NGL8) gives \(\mathcal O_T(\eta_m)\le d_*\); since
\(d_*\le1/2\), the strict branch condition is satisfied.
Factor subtraction gives
\(\sup_u\|H^2_\theta(u)-H^2_{\bar\theta}(u)\|_2\le H_L\|\theta-\bar\theta\|\).
Each displacement from the endpoint has norm at most two, so subtracting
squared norms in (NGL17) gives
\(|J_2(\theta)-J_2(\bar\theta)|\le4H_L\|\theta-\bar\theta\|\).
Together with (NGL13), this proves, with sample probability at least
\(1-\delta\),
\[
 \mathcal E_\nu(F_*)-\mathcal E_\nu(P_{\widehat\nu_m}(T))\ge3a_*/4,
 \qquad J_2(\theta_{\widehat\nu_m}(T))\ge3j_*/4.
 \tag{NGL21}
\]

For actual finite GF, train the empirical mixture and reference on the same
initial arrays, including the Gaussian readout, and evaluate both at the same
physical time \(T/\varepsilon\). Define
\[
 J_{2,n,\varepsilon}={1\over3n}\left[
  \int\|h^2_{n,\widehat\mu_{\varepsilon,m}}(T/\varepsilon,\sqrt2u)
           -h^2_{n,\nu_*}(T/\varepsilon,\sqrt2u)\|_2^2\,d\rho(u)
\right.
\left.\hspace{5mm}+\sum_{a=1}^2
  \|h^2_{n,\widehat\mu_{\varepsilon,m}}(T/\varepsilon,\sqrt2e_a)
           -h^2_{n,\nu_*}(T/\varepsilon,\sqrt2e_a)\|_2^2\right].
 \tag{NGL22}
\]
For every fixed law in (NGL14), every \(m\ge m_*\), and the constants
above, the bounded-law capture and finite-GF theorem in C.4.10.2 imply
\[
 \liminf_{\varepsilon\downarrow0}\liminf_{n\to\infty}
 \Pr_{\rm samples,init}\left\{
  \mathcal E_\nu(F_*)-
     \mathcal E_\nu(f_{n,\widehat\mu_{\varepsilon,m}}(T/\varepsilon))
       \ge a_*/2,\quad J_{2,n,\varepsilon}\ge j_*/2\right\}
 \ge1-\delta.
 \tag{NGL23}
\]
The same conclusion holds with the paired finite reference risk in place
of \(\mathcal E_\nu(F_*)\).

Indeed, for each fixed realized sample and positive \(\varepsilon\), width
first gives its deterministic population-law flow, including joint paired
observations. Sending \(\varepsilon\) to zero then gives its constrained
selection at \(T\); the reference converges to \(\theta_\dagger\).
The bounds hold for every empirical law, including repeated observations.
Conditional failure probabilities are bounded by one, so dominated convergence
integrates them over samples. On (NGL21)'s sample event, the spare margins
allow both transfers. Whole-circle uniform prediction convergence implies
excess-risk convergence, and the same-array hidden limits give (NGL22).
This proves (NGL23) without interchanging the order of limits.

The constants and sample threshold are uniform on the robust class; no width
threshold uniform over that class is asserted. The positive margins are
independent of \(\varepsilon\) and \(n\). With sample size increasing after
the width and contamination limits, the probability tends to one, since
\(\delta\) can be made arbitrarily small. More data reduces the statistical
term; more training within the declared episode reduces the population bound
toward its explicit floor. The result proves a finite nonlinear learning
episode for this class, not arbitrary-accuracy fitting, an all-time endpoint,
or superiority over another architecture or training method.
