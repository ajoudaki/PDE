# Three inputs in the scalar density closure

Date: 2026-09-18. Internal research synthesis; no promotion.

The unconditional pair theorem does not currently extend to a genuinely
three-constraint initialized family. This investigation proves a finite-state
exponential certificate, a stationary-loss gap with a sharp non-escape
obligation, and an exact balanced three-input initialization obstruction.
It also proves finite-time progress for open sets of genuine triples close
to a successful pair. None of these statements silently supplies the missing
all-time hypothesis.

## 1. Exact model and conventions

The model is the declared scalar-dictionary closure, not the full canonical
p=1 dictionary and not the finite neural network. Write phi=tanh. The two
independent integration spaces carry g~N(0,I_2) and Z~N(0,1). With

\[
\nu=E\phi(G)^2,\quad \tau=E\phi(\sqrt\nu G)^2,\quad \eta=1/4096,
\]
\[
b_1=\frac{\phi(g_1)}{\sqrt{\nu+\eta}},\quad
b_2=\frac{\phi(\sqrt\nu Z)}{\sqrt{\tau+\eta}},\quad
w_0=g,\quad c_0=0,\quad
M_0=\frac{\nu(1-\tau)}{\sqrt{(\nu+\eta)(\tau+\eta)}}.
\]

The marks are frozen; the evolving density measures are
rho_1=Law(b_1,w), rho_2=Law(b_2,c). They need not have Lebesgue densities.
For inputs x_i in sqrt(2)S^1, positive masses p_i summing to one and
y_i in {-1,1}, set

\[
a_i=\int b_1\phi(w^Tx_i/\sqrt2)\,d\rho_1,\quad
H_i(b_2)=\phi(b_2Ma_i),\quad
f_i=\int cH_i\,d\rho_2,\quad r_i=f_i-y_i,
\]
\[
d_i=\int b_2c\phi'(b_2Ma_i)\,d\rho_2.
\]

The characteristic velocities are exactly

\[
\dot w=-2\sum_i p_ir_i b_1Md_i\phi'(w^Tx_i/\sqrt2)x_i/\sqrt2,
\quad \dot c=-2\sum_i p_ir_iH_i,
\quad \dot M=-2\sum_i p_ir_id_ia_i.
\tag{1}
\]

They transport rho_1 and rho_2 while retaining the marks. The loss is
L=sum_i p_i r_i^2; time and the Hilbert metric are physical:
||delta w||_2^2+||delta c||_2^2+|delta M|^2. In particular
L_dot=-||dot w||_2^2-||dot c||_2^2-dot M^2. All integrals below use the
current state or the declared fixed Gaussian carriers.

## 2. A finite-state exponential potential, including both hidden layers

Define the lower activation gradients

\[
A_i=b_1\phi'(w^Tx_i/\sqrt2)x_i/\sqrt2,
\]

and the weighted full tangent Gram matrix

\[
\Theta_{ij}=\sqrt{p_ip_j}\left[
\int H_iH_j\,d\rho_2
+a_id_i a_jd_j
+M^2d_id_j\int A_i\cdot A_j\,d\rho_1\right].
\tag{2}
\]

The three terms are respectively the readout, connector, and first-layer
responses. If R_i=sqrt(p_i)r_i, direct differentiation gives
R_dot=-2Theta R and L_dot=-4 R^T Theta R.

Here is a checkable sufficient condition at one finite time T; it does not
assume a uniform future Gram bound. Let kappa=lambda_min(Theta_T)>0. Put
B_1=(nu+eta)^(-1/2), B_2=(tau+eta)^(-1/2), C=||c_T||_2+1,
m=|M_T|+1, and define the fixed constants

\[
D=B_1\sqrt{1+m^2},\qquad
A=2B_2D+2B_2^2CD^2+2B_1B_2C(1+m),\qquad
\rho=\min\{1,\sqrt\kappa/(2A)\}.
\]

**Conditional exponential theorem.** If

\[
\frac{2\sqrt{L(T)}}{\sqrt\kappa}<\rho,
\tag{3}
\]

then the fixed current-state potential

\[
\boxed{\Phi(S)=\frac{4L(S)}{\kappa}}
\tag{4}
\]

satisfies, for every t>=T,

\[
\dot\Phi\le-\kappa\Phi,\quad
L(t)\le L(T)e^{-\kappa(t-T)},\quad
\left(\int_t^\infty\|\dot S_s\|\,ds\right)^2\le\Phi(S_t).
\tag{5}
\]

Thus the complete state converges strongly on its fixed carriers to a
finite interpolating state. The same coupling bounds transport of both
population measures. No preselected endpoint occurs in (4).

**Proof.** Let J be the derivative of the weighted prediction vector, so
Theta=JJ*. On the unit Hilbert ball about S_T the explicit A above bounds
||J(S)-J(S')||/||S-S'||. To see this, the lower feature derivative obeys
||Da_i||<=B_1 and ||Da_i(w)-Da_i(v)||<=2B_1||w-v||_2. The derivative of
s_i=Ma_i has norm at most D and Lipschitz constant at most
2B_1(1+m). The derivative of f_i=<c,phi(b_2 s_i)> consequently has the
three Lipschitz contributions in A: the two readout/feature cross terms,
the phi' difference, and the s_i derivative difference. Cauchy--Schwarz
and bounded phi',phi'' justify each estimate in L2. This requires C^{1,1}
regularity, not a false claim of twice Frechet differentiability of a
pointwise Nemytskii map on L2.

Inside the radius-rho ball, ||J(S)^*v||>=sqrt(kappa)|v|/2. Hence
||grad L||>=sqrt(kappa L) and -L_dot>=kappa L. Before any possible first
exit from the ball, its physical arc length is at most

\[
\int_T^t\|\dot S\|\,ds
=\int_T^t\frac{-\dot L}{\|\nabla L\|}\,ds
\le\frac{2}{\sqrt\kappa}(\sqrt{L(T)}-\sqrt{L(t)})<\rho.
\]

This excludes first exit and proves exponential loss. Repeating the same
integral from t proves (5); completeness of the Hilbert space and continuity
of the prediction map identify its limiting fitting state. Zero loss at a
finite time is handled by the stationary continuation. QED.

The theorem applies to generic three-input states, and in fact any finite
number of inputs. Its unresolved part for the question asked is attainment
of (3) from the specified initialization. Initial positive definiteness
alone does not establish it. The theorem is not advertised as that missing
initialized-trajectory result.

## 3. A global restriction on failure to fit

**Stationary gap.** For any three inputs and binary labels, every finite
readout-stationary state has either L=0 or L>=p_min=min_i p_i.

**Proof.** Write s_i=Ma_i. The functions phi(bs) for distinct nonzero
absolute slopes are linearly independent, after identifying their signs.
A linear identity on the upper population is a continuous identity on its
open support. The first three odd Taylor coefficients at b=0 give a
Vandermonde system in the distinct positive s^2; its determinant is nonzero.
Partition the nonzero s_i into classes C with equal |s_i|. Put sigma_i=sign(s_i),
P_C=sum_C p_i and Y_C=sum_C p_i sigma_i y_i. Readout stationarity says
sum_i p_i r_i H_i=0, and independence gives the common signed prediction
Y_C/P_C in class C. Zero slopes predict zero. Therefore

\[
L=\sum_{s_i=0}p_i+\sum_C\left(P_C-\frac{Y_C^2}{P_C}\right).
\tag{6}
\]

If the aligned labels sigma_i y_i in C have masses P_+,P_-, its cost is
4P_+P_-/(P_++P_-). A positive such cost is at least
2min(P_+,P_-)>=2p_min; a zero-slope atom costs at least p_min. QED.

**Trajectory consequence.** If L(T)<p_min, then

\[
\liminf_{t\to\infty}\|c_t\|_2<\infty
\quad\Longrightarrow\quad L(t)\longrightarrow0.
\tag{7}
\]

Equivalently, a positive limiting loss below p_min forces ||c_t||_2 to
tend to infinity. No bound on w or M is required for this implication.

To prove it, choose an unbounded sequence of times with bounded readout.
The dissipation on each following unit interval tends to zero. A time in
that interval has ||dot c||_2 tending to zero, while Cauchy--Schwarz keeps
its readout bounded. Pass to a subsequence for which all three slopes
s_i converge in [-infinity,infinity] and all residuals converge. The upper
features converge strongly in L2 to phi(bs_i), zero, or +/-sign(b).
This is dominated convergence; the upper law has no atom at zero.
Bounded readout preserves every zero or signed-equality relation among
these limiting features in their predictions. Readout stationarity holds
in the limit. The finite-slope functions together with sign(b) are still
independent: the one-sided limit b downarrow0 removes sign(b), after
which the previous Taylor argument applies. Formula (6) therefore applies
to the limiting predictions, even if the slopes diverged. It excludes
0<L_infinity<p_min and proves (7).

The needed readout bound is not a consequence of the energy identity.
In fact three_generic_route.md, section 5, constructs smooth parity-preserving
finite states with L approaching any of certain arbitrarily small positive
values while the full gradient tends to zero, c and w diverge and M tends
to zero. Flipping one input and its label produces mixed binary labels;
weights (1/4,1/4,1/2) make them balanced. These are ambient states, not
trajectories. They invalidate a compactness or uniform-PL shortcut; they
do not prove that the initialized dynamics fails to converge.

## 4. An exact three-input obstruction, and positive finite-time progress

Fix 0<delta<1 and s=sqrt(1-delta^2). Take

\[
(x_1,y_1)=(\sqrt2(\delta,s),+1),\quad
(x_2,y_2)=(\sqrt2(-\delta,s),+1),\quad
(x_3,y_3)=(\sqrt2(0,1),-1),
\]

with weights (1/4,1/4,1/2). These are three distinct, pairwise nonparallel
inputs and balanced classes. The fixed e1-probe initialization gives
a_1=A>0, a_2=-A, a_3=0. Thus H_2=-H_1 and H_3=0. At c=0, the readout
forcing cancels and both other velocities vanish. By uniqueness,

\[
S_t=S_0,\qquad L(t)=1\quad\text{for every }t.
\tag{8}
\]

This is a failure of this initialization with this frozen scalar probe,
not an incompatible labeling or an expressivity theorem. A finite fitting
state exists with the same frozen marks and M=M_0. The full construction
in three_stalled_triple.md perturbs the lower field by bounded odd vectors
so that its three scalar feature magnitudes become nonzero and distinct,
then solves the positive definite readout Gram system exactly. The lower
feature differential is onto because its three derivative fields are
independent; this is proved using directions perpendicular to individual
inputs. Consequently no finite strictly decaying potential that controls
loss can apply to every three-input law for this fixed scalar model.
The counterexample does not establish failure for generic configurations.

There is also an actual-flow delay theorem near this obstruction. Keep these
inputs fixed and change the weights to (1/4+epsilon,1/4-epsilon,1/2).
The classes remain balanced and the initial velocity is now nonzero:
dot c_0=4epsilon H_1. Uniform local Lipschitz estimates for the vector field
give, for each fixed loss threshold 0<ell<1, constants B,r>0 independent
of small nonzero epsilon such that

\[
\tau_\varepsilon(\ell):=\inf\{t:L_\varepsilon(t)\le\ell\}
\ge B^{-1}\log\left(1+\frac{Br}{4|\varepsilon|}\right).
\tag{8a}
\]

Indeed, until the state leaves a radius-r ball around initialization,
Gronwall gives its displacement at most
4|epsilon|(exp(Bt)-1)/B. Choose r small enough that prediction continuity
keeps loss above ell throughout that ball. The first possible exit then
gives (8a). The proof and explicit constants are in three_stalled_triple.md.
This is a lower bound on an actual initialized hitting time, allowing that
time to be infinite; it is not merely a family of ambient states.

Consequently any proposed common-rate potential satisfying
L<=Phi^alpha and Phi_t<=exp(-lambda t)Phi_0 across these perturbed laws
must obey

\[
\Phi_\varepsilon(S_0)\ge
\ell^{1/\alpha}\left(1+\frac{Br}{4|\varepsilon|}\right)^{\lambda/B}.
\tag{8b}
\]

The power law is a necessary lower bound, not a sharp growth theorem or a
construction of the potential. Geometry-dependent rates may instead vanish.

Conversely, genuine triples close to a successful pair do make arbitrarily
substantial finite-time progress. Take angles pi/3+epsilon, pi/3-epsilon,
2pi/3, labels (+,+,-), and weights (1/4,1/4,1/2). At epsilon=0 the first
two atoms combine to the proved pair with delta=1/2. For each chosen
0<ell<1, the pair loss is at most ell/2 by the finite time
T=log(2/ell)/(4K_0). Continuous dependence of (1) on the data on that
finite interval then gives L(T)<ell for all sufficiently small nonzero
epsilon, and for an open neighborhood of each such configuration. The
three initialized feature magnitudes are distinct for these epsilon, so
this is an actual third independent fitting constraint. The complete
finite-time argument is in three_entry_lemma.md. The neighborhood depends
on ell; this statement is not convergence for one fixed triple as ell
tends to zero, and it does not establish (3) or (7)'s readout hypothesis.

## 5. What the symmetric three-point test actually shows

A second natural family has positive inputs sqrt2(delta,+/-s), each of
weight 1/4, and negative input -sqrt2 e1 of weight 1/2. Its preserved
reflection reduces the three samples to two independent fitting equations.
The two residuals cannot remain positive: three_symmetry_route.md proves
a finite transverse overshoot of the axial prediction for every 0<delta<1.
Thus the pair's one-error positivity proof cannot be repeated for this
family. The overshoot does not disprove a mixed potential.

For generic independent upper features define h_i=sqrt(p_i)H_i,
G=integral hh^T d rho_2 and R_i=sqrt(p_i)r_i. The natural candidate remains

\[
\Phi_{\rm read}=R^TG^{-1}R
=\min\{\|q\|_2^2:\ \int qH_i\,d\rho_2=-r_i\text{ for every }i\}.
\]

It is the exact squared minimum readout correction with the current hidden
features. Since tr(G)<=1, L<=Phi_read wherever G is invertible. Its exact
derivative, including the changing metric, is

\[
\dot\Phi_{\rm read}
=-v^T\{\dot G+2(\Theta G+G\Theta)\}v,\qquad v=G^{-1}R.
\tag{9}
\]

No sign or uniform coercivity for the bracket is proved along a general
initialized triple. On the symmetric two-mode invariant subspace the same
formula uses the two distinct features; using the singular full three-row
Gram without removing its exact redundancy would be incorrect.

The precommitted three-resolution deterministic quadrature diagnostic at
delta=1/2 observed a decreasing candidate through t=1000 and the predicted
residual overshoot. Its late-time potential and slope were not numerically
resolved across the grids. It is neither a proof of monotonicity nor an
asymptotic rate. See three_diagnostic_result.md for exact numbers and limits.

## 6. Scope and remaining obligation

Proved results include the exact stalled initialized family, finite-time
entry for an open set of genuine triples, the stationary gap, implication
(7), and the finite-state exponential certificate (3)--(5). Independent
routes and a scoped cross-audit support the latter two arguments. They
remain study results, not established book material.

For a nondegenerate triple starting at the prescribed initialization, the
missing step is an actual dynamical estimate ensuring bounded readout
after entry below p_min, or ensuring entry into (3). The former would
prove fitting; the latter would prove exponential loss and full-state
convergence. A direct proof of the directional bound in (9) could provide
a different resolution. Initial Gram positivity, absence of finite bad
critical values, and the observed finite-time curve do not supply any
of these estimates.
