# Two samples: reinforcement, contrast suppression, and the unresolved endpoint

2026-09-30. Author: root, integrating the frozen scoped routes named below.
Status: conditional research candidate corrected after its recorded internal
check; correction verification is recorded in README.md. This note works
directly on infinite population spaces. There is no
trained finite network, dense comparison, width expansion, or experiment.

The substantive local result is stronger than output progress: **in each of
the two hidden populations, the squared common response increases and the
squared difference response decreases at the first nonzero order.** This
holds for every nondegenerate signed input correlation. The difference-key
lag then contributes negatively to progress. Thus cooperation and a specific
form of interference arise together, from the same feature-learning mechanism.
The exact whole-query symmetry survives for all defined times and any endpoint.
Global fitting and the full fitted amplitude remain open.

## 1. Object and mathematical status

There are two equally weighted inputs of norm sqrt(d), binary labels,
two tanh hidden layers, no biases, unit mobilities, zero readout and value
memories. Normalize and absorb labels into the inputs:

\[
u_a=x_a/\sqrt d,\qquad p_a=y_au_a,\qquad
c=p_1\cdot p_2\in(-1,1).
\]

Oddness makes this an exact change of training variables: replace each label
by +1 and its key/value by y_a times that field. The query predictor is unchanged.

Use two probability spaces with inner products \(\langle\cdot,\cdot\rangle_j\).
The first population contains the vector read-in field A and the keys K_a;
the second contains the readout field W and values V_a. These are population
random variables, not parameters of a chosen finite neuron system. T is the
fixed initialized Gaussian source action, with its true adjoint T* on the
common generated population spaces. Write only as a reconstructed abbreviation

\[
\mathcal B=T+\frac12\sum_a V_a\otimes K_a,
\quad (v\otimes k)h=v\langle k,h\rangle_1.
\]

For a normalized query u the exact prediction is

\[
H(u)=\tanh(A\cdot u),\quad Z(u)=\mathcal B H(u),\quad
G(u)=\tanh Z(u),\quad F(u)=\langle W,G(u)\rangle_2.                 \tag{1}
\]

Define \(D_a=W(1-G_a^2)\), \(L_a=(1-H_a^2)\mathcal B^*D_a\),
\(r_a=F(p_a)-1\), and \(\rho^2=(r_1^2+r_2^2)/2\). Physical time satisfies

\[
\dot W=-\sum_a r_aG_a,\quad
\dot A=-\sum_a r_a L_a p_a,\quad
\dot V_a=-2r_aD_a,\quad
\dot K_a=(\rho/\tau)(H_a-K_a),\quad \dot\tau=\rho.                \tag{2}
\]

Initially A is standard isotropic Gaussian, W=V_a=0, K_a=H_a, and tau=1.
On initial sources h depending only on A_0, T gives jointly centered Gaussian
forward fields with covariance \(\langle h,\tilde h\rangle_1\). Reusing its
adjoint obeys the Gaussian conditioning law stated in Section 3.

This is the manuscript's learning-speed q=1 closure with
\(K_a=\bar h_{a,0}/\tau\), \(V_a=-2\bar\delta_{a,0}\), the same
physical time and learning-rate factors. In particular the factor 1/2 in
(1) is the sample average, not a width factor. At the stipulated zero
readout initialization the joint-clock physical trajectory has the same
q=1 equation if its key is normalized by its accumulated mass rather than
by its different coordinate clock. See MANUSCRIPT_RECONCILIATION.md.

**Foundation hypothesis.** For trajectory assertions below, assume a local
strong population solution with a bounded fixed source/true adjoint on its
generated L2 spaces, the integrability/chain rules displayed here, deterministic
scalar observables, and uniqueness/equivariance under joint sample exchange
and input rotations of the complete Gaussian initialization. For all-time
identities, these conditions apply on the interval in question. Second-order
feature expansions are in L2; their scalar consequences use the corresponding
pairings. We do not assert Gaussianity or independence of trained fields.

The paper calls its fixed-order population limit a conjecture. Its finite-width
existence theorem does not establish this hypothesis, and a bounded operator
alone does not establish local Lipschitz continuity of all the gated L2
products. The initial finite-source Gaussian calculation is well specified;
its realization along a flow is conditional on this foundation. Constructing
the entire canonical q=1 population flow, or identifying a trained-width
limit, is a separate open claim here.

The laws may be singular; Lebesgue densities are unnecessary. Precisely, the
joint law \(\mu_{1,s}\) of (A,K_+,K_-) has the weak transport identity

\[
\frac d{ds}\int\psi\,d\mu_{1,s}
=\mathbb E_1[\nabla_A\psi\cdot A'
 +\partial_{K_+}\psi K_+'+\partial_{K_-}\psi K_-'],                \tag{3}
\]

and similarly for the joint second-population law of (W,V_+,V_-), for smooth
test functions with integrable derivatives. Fixed-source marks must be retained
to evaluate the velocities. Separate unmarked marginal densities do not supply
the adjoint response. All subsequent results concern these population laws.

## 2. Two channels and the exact training clock

Full swap equivariance gives F(p_1)=F(p_2)=f. It also makes scalar pairings
between a sample-even and a sample-odd field vanish. This is an invariance of
joint population laws, not equality of individual neuron responses.

Before f reaches 1 set \(s=2\int_0^t(1-f(r))dr\); then
\(\tau=1+s/2\). Use \(X_\pm=(X_1\pm X_2)/2\) for every sample field.
Define

\[
a_\pm=\|H_\pm\|_1^2,\quad b_\pm=\langle K_\pm,H_\pm\rangle_1,
\quad d_\pm=\langle V_\pm,D_\pm\rangle_2,
\quad \gamma_\pm=(1\pm c)/2.
\]

The exact equations, with primes denoting s derivatives, are

\[
Z_\pm=TH_\pm+b_\pm V_\pm,\quad
J_\pm=T^*D_\pm+d_\pm K_\pm,                                    \tag{4}
\]
\[
E=1-H_+^2-H_-^2>0,\quad C=-2H_+H_-,\quad
P=1-G_+^2-G_-^2>0,\quad R=-2G_+G_-,
\]
\[
L_+=EJ_++CJ_-,\quad L_-=CJ_++EJ_-,\qquad
D_+=PW,\quad D_-=RW,                                           \tag{5}
\]
\[
A'=L_+\frac{p_1+p_2}{2}+L_-\frac{p_1-p_2}{2},\quad
W'=G_+,\quad V_\pm'=D_\pm,\quad K_\pm'=\frac{H_\pm-K_\pm}{2+s}. \tag{6}
\]

For \(q_\pm=A\cdot(p_1\pm p_2)/2\), one has
\(q_\pm'=\gamma_\pm L_\pm\) and

\[
H_+=\frac{\sinh(2q_+)}{\cosh(2q_+)+\cosh(2q_-)},\quad
H_-=\frac{\sinh(2q_-)}{\cosh(2q_+)+\cosh(2q_-)}.                 \tag{7}
\]

The same formula gives G from Z_+,Z_-. Adding/subtracting the two tanh
derivatives proves (5); parity eliminates cross-channel memory contractions
in (4). Thus (4)--(7) follow directly from (1)--(2).

In particular, the difference memory has the exact identity

\[
V_-'=-(W^2)'G_-.                                               \tag{8}
\]

It opposes the instantaneous response difference wherever W squared is
increasing. This alone does not prove contraction: TH_-, b_-, and G_- move.
Both memory channels are present even though the residual is one scalar.

## 3. The first return through the fixed random mixer

Everything in this section is evaluated at initialization. The first
preactivations \(\xi_a=A_0\cdot p_a\) form a centered Gaussian pair of
unit variances and correlation c. Write h_a=tanh xi_a, h_±=(h_1±h_2)/2.
The initial z_a=Th_a form a nondegenerate Gaussian pair of covariance
\(\langle h_a,h_b\rangle_1\). Hence z_± are independent centered
Gaussians with variances a_±>0. Put g_a=tanh z_a and g_±=(g_1±g_2)/2.
The gates E,C,P,R now refer to these initial fields.

For any finite list of bounded C1 functions U_a(z_1,z_2) with bounded first
derivatives, the canonical first reverse call has joint law

\[
T^*U_a=\sum_b M_{ab}h_b+\zeta_a,
\quad M_{ab}=\mathbb E_2\partial_{z_b}U_a,
\quad \mathbb E_1[\zeta_a\zeta_b]=\mathbb E_2[U_aU_b],            \tag{9}
\]

where the centered Gaussian innovation vector is independent of A_0.
It is one jointly sampled vector for all the sources. Its covariance is the
full source second moment, not the variance after subtracting regression.

For clarity, the conditioning argument is: given the forward answers, the
reverse mean lies in span(h_1,h_2) with coefficients
\(\mathcal C^{-1}\mathbb E[zU_a]\), where
\(\mathcal C_{ab}=\langle h_a,h_b\rangle_1\). The remaining initialized
Gaussian action is projected off that input span and has reverse source
covariance \(\mathbb E[U_aU_b]\). In the generated population law its
coordinate innovation is independent of the first-layer roots. Gaussian
integration by parts gives
\(\mathbb E[z_jU_a]=\sum_b\mathcal C_{jb}\mathbb E[\partial_bU_a]\),
which yields (9). Integration by parts follows by writing z as a linear map
of standard normals and integrating their density; bounded derivatives remove
boundary terms. This is the initialized finite-source rule of the maintained
Gaussian-conditioning construction, not a theorem about training convergence.
It checks the necessary adjunction
\(\langle h_b,T^*U_a\rangle_1=\langle z_b,U_a\rangle_2\).

Use two pairs of sources

\[
U_1=g_+(1-g_1^2),\ U_2=g_+(1-g_2^2),\quad
Y_1=g_-(1-g_1^2),\ Y_2=-g_-(1-g_2^2).
\]

Their channels are

\[
U_+=Pg_+,\quad U_-=-2g_+^2g_-,\qquad
Y_+=-2g_+g_-^2,\quad Y_-=Pg_-.                                 \tag{10}
\]

Equation (9) and exchange parity imply

\[
T^*U_\pm=\lambda_\pm h_\pm+\zeta^U_\pm,\qquad
T^*Y_\pm=\nu_\pm h_\pm+\zeta^Y_\pm,
\]
\[
\lambda_\pm=\frac{\mathbb E[z_\pm U_\pm]}{a_\pm},\quad
\nu_\pm=\frac{\mathbb E[z_\pm Y_\pm]}{a_\pm},\qquad
\lambda_+>0>\lambda_-,\quad \nu_+<0<\nu_-.                     \tag{11}
\]

The signs are pointwise: g_± has the sign of z_±, and P>0.
All are strict since the initial Gaussian pair has full support. Also

\[
\mathbb E[\zeta^U_+\zeta^Y_+]
=\mathbb E[\zeta^U_-\zeta^Y_-]
=-2\mathbb E_2[P g_+^2g_-^2]=:\omega<0,                         \tag{12}
\]

and both cross-parity covariances vanish. Thus reverse reuse supplies both a
nonzero supervised drift and correlated innovations. Replacing T* by a fresh
independent mixer deletes the drift and changes the learning mechanism.

## 4. A strict theorem for both hidden populations

**Theorem (initial common-response growth and difference suppression).** Under
the foundation and initialized Gaussian source law above, for each j=1,2 set

\[
\mathcal S_1=\|H_+\|_1^2,\quad\mathcal D_1=\|H_-\|_1^2,
\qquad\mathcal S_2=\|G_+\|_2^2,\quad\mathcal D_2=\|G_-\|_2^2.
\]

Every first derivative at zero vanishes, and

\[
\boxed{\quad\mathcal S_j''(0)>0,\qquad\mathcal D_j''(0)<0
\quad(j=1,2).\quad}                                            \tag{13}
\]

Consequently both normalized feature overlaps
\(\mathcal R_j=(\mathcal S_j-\mathcal D_j)/(\mathcal S_j+\mathcal D_j)\)
increase strictly for sufficiently small positive s. Equal marginal second
moments make these the normalized overlaps of the two actual sample feature
fields. If centered, they are also Pearson correlations. In original labels,
this means increased alignment after multiplying each response by its label;
opposite-label responses move toward anticorrelation in the original gauge.

**Proof of the first-layer assertion.** At zero W'=g_+, while A'=V'=K'=0.
Let
\(\mathcal A_U=\frac12\sum_a(1-h_a^2)(T^*U_a)p_a\).
Then \(A''=\mathcal A_U\). Continuity of the strong flow gives this as an L2 jet:
W(s)/s tends to g_+, D_a(s)/s to U_a, and \(A'(s)/s\) to \(\mathcal A_U\).
Boundedness of T*, bounded gates and convergence of the rank-two correction
justify these limits. Multiplication by a varying bounded gate follows by
splitting off the limiting L2 field and dominated convergence on that field.

Define J^U_±=T*U_± and
\(L^U_+=EJ^U_++CJ^U_-\), \(L^U_-=CJ^U_++EJ^U_-\).
The Jacobian in (7) gives

\[
H_+''=(\gamma_+E^2+\gamma_-C^2)J^U_++ECJ^U_-,\quad
H_-''=ECJ^U_++(\gamma_+C^2+\gamma_-E^2)J^U_-.                    \tag{14}
\]

The innovations in (11) have mean zero conditional on A_0. Put

\[
J_0=\mathbb E_1[h_+^2h_-^2E]>0,
\quad Q_+=\mathbb E_1[h_+^2(\gamma_+E^2+\gamma_-C^2)]>0,
\quad Q_-=\mathbb E_1[h_-^2(\gamma_+C^2+\gamma_-E^2)]>0.
\]

Pairing (14) with h_± gives

\[
\chi_+:=\langle h_+,H_+''\rangle_1=\lambda_+Q_+-2\lambda_-J_0>0,
\quad
\chi_-:=\langle h_-,H_-''\rangle_1=-2\lambda_+J_0+\lambda_-Q_-<0.
                                                                    \tag{15}
\]

Since H_±'=0, the second derivatives of their squared norms are 2chi_±.
These are moment statements, not movement in the same direction at every
population point: the conditional acceleration covariance of the two sample
preactivation channels is nondegenerate (the full vector read-in acceleration
has covariance supported on their two-dimensional training span).

**Proof of the full second-layer assertion.** Separate only the additive
contributions of read-in acceleration and of memory acceleration; neither
state is frozen in the trajectory. Since V_±''=U_± and b_±(0)=a_±,

\[
Z_{+,\mathrm{mem}}''=a_+Pg_+,\quad
Z_{-,\mathrm{mem}}''=-2a_-g_+^2g_-.
\]

The second-layer Jacobian is [[P,R],[R,P]], so

\[
G_{+,\mathrm{mem}}''=g_+[a_+P^2+4a_-g_+^2g_-^2],\quad
G_{-,\mathrm{mem}}''=-2(a_++a_-)P g_+^2g_-.                     \tag{16}
\]

The memory contributions to S_2'' and D_2'' are therefore strictly positive
and strictly negative, respectively.

For the moving read-in contribution, the gradients of S_2 and D_2 with T
fixed at initialization are \(2\mathcal A_U\) and \(2\mathcal A_Y\), respectively,
where \(\mathcal A_Y\) is defined as \(\mathcal A_U\) with Y replacing U. Thus

\[
\mathcal S_{2,A}''=2\|\mathcal A_U\|_1^2\ge0,\qquad
\mathcal D_{2,A}''=2\langle\mathcal A_U,\mathcal A_Y\rangle_1.     \tag{17}
\]

We prove the latter pairing strictly negative, including the innovation.
Conditional means of the first-layer gated source channels are

\[
\begin{array}{ll}
m^U_+=h_+(E\lambda_+-2h_-^2\lambda_-),&
m^Y_+=h_+(E\nu_+-2h_-^2\nu_-),\\
m^U_-=h_-(E\lambda_--2h_+^2\lambda_+),&
m^Y_-=h_-(E\nu_--2h_+^2\nu_+).
\end{array}
\]

The plus pair has opposite signs and the minus pair has opposite signs,
outside null zero sets, by (11). Hence each m^U_±m^Y_± is negative.
Using (12), the conditional covariance between the corresponding gated
channels is \((E^2+C^2)\omega<0\). Consequently

\[
\mathbb E_1[L^U_\pm L^Y_\pm]
=\mathbb E_1[m^U_\pm m^Y_\pm+(E^2+C^2)\omega]<0.
\]

The two input directions in (6) are orthogonal of squared lengths gamma_±.
Therefore

\[
\langle\mathcal A_U,\mathcal A_Y\rangle_1
=\gamma_+\mathbb E_1[L^U_+L^Y_+]
 +\gamma_-\mathbb E_1[L^U_-L^Y_-]<0.                            \tag{18}
\]

Combining (16)--(18) proves the full second-layer assertion. Finally, for
positive S,D with S'=D'=0,
\(\mathcal R''=2(D S''-S D'')/(S+D)^2>0\). This proves the overlap
claim. These statements can equivalently be read as second-order expansions;
no convergent analytic series is needed. Physical-time second derivatives
are four times the displayed values, since ds/dt=2 initially. QED.

Two further concrete consequences follow. First, both V_±=(s²/2)U_±+o_L2(s²)
are nonzero and orthogonal for sufficiently small s>0. Both keys are likewise
nonzero and orthogonal. Thus the reconstructed memory perturbation has rank
exactly two, despite the one scalar residual. Second, with
\(\kappa=\mathcal S_2(0)>0\), integration of W'=G_+ gives

\[
f(s)=\kappa s+\tfrac13\mathcal S_2''(0)s^3+o(s^3).               \tag{19}
\]

Indeed G_+(s)=g_++s²G_+''(0)/2+o_L2(s²) and
W(s)=s g_++s³G_+''(0)/6+o_L2(s³). Pairing them proves (19).
Feature learning strictly improves the first nonlinear correction to training
progress per accumulated residual. This is a local result, not all-time ascent.

## 5. The lag obstruction is reached by the initialized trajectory

The exact output derivative along feature time is

\[
f'=\|G_+\|_2^2+\|A'\|_1^2
 +\sum_{\pm}\left[b_\pm\|D_\pm\|_2^2
       +\frac{d_\pm(a_\pm-b_\pm)}{2+s}\right].                  \tag{20}
\]

To verify all terms, the gradients of f in its independent state blocks
(A,W,V_±,K_±) are (A',G_+,b_±D_±,d_±H_±); contracting them with (6)
gives (20). The key history and value balance are

\[
K_\pm(s)=\frac{2h_\pm+\int_0^s H_\pm(v)dv}{2+s},\qquad
d_\pm=\tfrac12(\|V_\pm\|_2^2)',\qquad
\tfrac12(\|W\|_2^2)'=f.                                      \tag{21}
\]

Current-past overlaps b_± are not squared norms. In particular (15) implies

\[
a_--b_- =\tfrac12\chi_-s^2+o(s^2),\quad
d_- =\tfrac12\|U_-\|_2^2s^3+o(s^3),
\]
\[
\boxed{\quad\frac{d_-(a_--b_-)}{2+s}
=\tfrac18\chi_-\|U_-\|_2^2s^5+o(s^5)<0.\quad}                  \tag{22}
\]

Here K_±'=K_±''=0 at zero, so (a_±−b_±)''=chi_±. This proves (22),
including its sign, on the initialized flow under the same foundation.
Its accumulated work is also negative near zero, with leading coefficient
chi_-||U_-||²s^6/48. The positive memory response b_-||D_-||² is order s²
and dominates it initially. No increasing-loss claim follows.

This pinpoints a substantive mechanism: shrinking the current sample
difference leaves a larger past difference in the key; that obsolete
difference hinders progress. The same feature change that creates useful
agreement creates this opposing memory work. Proving fitting needs a
compensation estimate, not positivity of every term in (20).

For precision, suppose the actual feature flow satisfies f'>=||G_+||² while
f<1 and remains regular until its first fitting point or through s=1/kappa
if it has not fitted earlier. Then it crosses 1 by s<=1/kappa. Indeed n=||W|| obeys
\(n''=f'/n-f^2/n^3\ge0\) by Cauchy--Schwarz and (21);
n'(0+)=sqrt(kappa), so f'=n'^2+nn''>=kappa. Regular continuation through
the first crossing gives physical loss <=exp(−4kappa t). This is a useful
conditional bridge. Its hypothesis has not been proved for this population.

## 6. What is fixed about the entire function, including an endpoint

Set

\[
e_+=\frac{p_1+p_2}{\sqrt{2(1+c)}},\quad
e_-=\frac{p_1-p_2}{\sqrt{2(1-c)}},\quad
u=\alpha e_++\beta e_-+u_\perp.
\]

Swap symmetry gives evenness in beta. Input rotations fixing the training
span give radial dependence on u_perp. Architectural oddness then gives
oddness in alpha. Thus, at every defined time,

\[
F_t(u)=\Phi_t(\alpha,\beta,\|u_\perp\|),\quad
\Phi_t(-\alpha,\beta,r)=-\Phi_t(\alpha,\beta,r),\quad
\Phi_t(\alpha,-\beta,r)=\Phi_t(\alpha,\beta,r).                   \tag{23}
\]

In particular

\[
\boxed{\quad (y_1x_1+y_2x_2)\cdot x=0\ \Longrightarrow\ f_t(x)=0.\quad} \tag{24}
\]

This passes to every pointwise endpoint limit. It is a mandatory zero set,
not a proof that it is the only zero set or that the sign changes there.
Under query C1 regularity (23) is equivalent to
F_t(u)=alpha Psi_t(alpha²,beta²,||u_perp||²), with continuous Psi.

On the unit circle u=cos(theta)e_++sin(theta)e_-, this becomes

\[
F_t(\theta)=\cos\theta\,Q_t(\cos^2\theta).                       \tag{25}
\]

If a C1 fitted endpoint exists, put a=sqrt((1+c)/2). Its training constraint
is precisely Q_*(a²)=1/a. Neither that condition nor symmetry determines Q_*
or excludes additional zeros. For instance the bounded smooth functions
tanh(alpha)/tanh(a) times [1+lambda(tanh²(alpha)−tanh²(a))] interpolate and
have all these symmetries; lambda>1/tanh²(a) creates extra zeros. These are
counterexamples to a symmetry-only inference, not asserted reachable flows.

At initialization the full query velocity has a stricter sign:

\[
\dot F_0(u)=k_{\|u\|}(p_1\cdot u)+k_{\|u\|}(p_2\cdot u),\qquad
\operatorname{sign}\dot F_0(u)=\operatorname{sign}((p_1+p_2)\cdot u). \tag{26}
\]

Here k_R is the composition of the two initial tanh Gaussian covariance
functions. Each is odd and strictly increasing in covariance: differentiating
the bivariate Gaussian density in its covariance equals its mixed spatial
derivative, and integration by parts gives derivative
E[sech² X sech² Y]>0. Continuity extends monotonicity to covariance endpoints.
Since p_1·u and −p_2·u are ordered by alpha, (26) follows. Thus every fixed
query off (24) has that sign for sufficiently small positive physical time.
There is no proved all-time sign propagation here.

There is also a precise conditional selection formula. If a regular feature
curve fits at finite s_* and converges in the needed L2 spaces, then

\[
W_* =\int_0^{s_*}G_+(s)ds,\quad
W_\perp=W_*-\frac{G_{+,*}}{\|G_{+,*}\|_2^2},
\]
\[
F_*(u)=\frac{\langle G_{+,*},G_*(u)\rangle_2}{\|G_{+,*}\|_2^2}
       +\langle W_\perp,G_*(u)\rangle_2.                        \tag{27}
\]

Parity gives W_* orthogonal to G_{-,*}, and fitting gives
<W_*,G_{+,*}>=1. Therefore the displayed first readout is the minimum-norm
readout fitting both final training features, and W_perp is orthogonal to
both. The second term vanishes on training inputs. No assertion is made that
it is nonzero or zero at the population endpoint: previous finite-neuron
examples cannot answer that question. Equation (27) identifies the unresolved
history dependence; it is not a solved endpoint formula in initial data.

If c=−1, the signed samples are antipodal with identical targets: the exact
initialized solution has F=0, W=V=0, fixed A and K, and tau=1+t. It never fits.
If c=1, the signed samples coincide and there is only one sample channel;
the strict two-channel conclusions (13) do not apply.

## 7. Evidence, claim levels, and next question

Dependencies read completely by root after freezing: TWO_SAMPLE_MIXING_ROUTE.md
(initial reverse law and preactivation correlation), TWO_SAMPLE_SYMMETRY_ROUTE.md
(symmetries, rank two, initial query sign), TWO_SAMPLE_FITTING_ROUTE.md including
its targeted addendum (exact derivative and initialized adverse lag). The
strict **full second-layer difference contraction**, via the four-source
covariance and opposing gated drifts in (17)--(18), is an additional root
derivation. All source routes and their assumptions are retained separately.

The primary manuscript and both included appendices were read completely;
notation provenance is in MANUSCRIPT_RECONCILIATION.md. Initialized Gaussian
conditioning inputs are docs/02-gaussian-reuse.qmd lines 1--170 and
docs/03-local-population.qmd lines 174--278; this note imports no trained-dense
monotonicity theorem. Source hashes and scoped author inputs are in
TWO_SAMPLE_POPULATION_CONTRACT.md and the route reports.

Exact conditional results: (4)--(8), (13), (19)--(24), and endpoint restriction
(27) under its additional convergence/fitting assumptions. Established-book
status: none. Open: construction and uniqueness of the canonical flow, sustained
reinforcement or compensation, global fitting for −1<c<1, existence of a fitted
endpoint, and determination/sign of its full amplitude Q_*. No numerical
experiment, novelty-priority claim, compression claim, or manuscript edit.

The next substantive bottleneck is to control the **sum** of memory work and
read-in dissipation in (20) along the canonical reachable law while allowing
the necessarily negative term (22). A candidate Lyapunov quantity must account
for decreasing contrast and its lag together. Merely assuming lag positivity,
discarding the difference channel, or making later source calls independently
Gaussian would erase mechanisms already proved here.
