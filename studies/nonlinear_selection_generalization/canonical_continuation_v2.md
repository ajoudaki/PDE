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
