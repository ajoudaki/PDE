# Nonlinear training near the substantially trained two-atom reference

Authors/assembler: /root, /root/p2_continuation, /root/p2_variation,
/root/p2_reached_tails. Candidate date: 2026-09-11.
**Status: complete author candidate awaiting two fresh complete isolated
adversarial reviews. No success verdict or promotion is asserted.**

This candidate uses the proof of the raw-Euler tail hypothesis H in
P2_SOURCE_BOOTSTRAP.md, followed by the complete continuation and
remainder proofs listed in §6. Earlier frozen reports call H open because
they precede that proof; those historical status sentences do not serve
as mathematical premises. Reviewers must check the new proof itself.
No prior review verdict is a dependency.

## 1. Exact model, norms and law neighborhood

Fix \(Y\ge1\), \(T=40\), and
\[
Z=\sqrt2 S^1\times[-Y,Y],\qquad
d_Z((x,y),(x',y'))=|x-x'|/\sqrt2+|y-y'|.
\]
Write \(\mathcal W_1\) for its Wasserstein distance and \(u=x/\sqrt2\).
The two-hidden-layer network, with no biases and equal width n, is
\[
h^1_n=\tanh(W^1_nu),\quad h^2_n=\tanh(W^2_nh^1_n),
\qquad f_n(x)=(W^3_n)^Th^2_n/n.
\]
All initialized entries and blocks are independent centered Gaussians
with stored variances \((1,1/n,1/n^2)\). All blocks train by physical GF
for \(L_\mu=\int(f_n(x)-y)^2\,d\mu(x,y)\), with stored mobilities
\((n,1,n)\). Every Borel-law loss integral is exact. In particular the
actual finite initial readout is retained.

The reference law is
\[
\nu_*=\tfrac12\delta_{(\sqrt2e_1,+1)}
       +\tfrac12\delta_{(\sqrt2e_2,-1)}.
\]
On the common canonical Gaussian carrier retain the full first-row
field \(w\), the initialized Gaussian action \(A_0:H_1\to H_2\) and its
actual Hilbert adjoint. Put \(A=A_0+K\) and use the raw state space
\[
\mathcal E=L^2(\Omega_1;\mathbb R^2)
 \oplus\mathcal S_2(H_1,H_2)\oplus H_2,\qquad\theta=(w,K,c),
\]
\[
\|\Delta\theta\|_{\rm raw}^2
=\|\Delta w\|_2^2+\|\Delta K\|_{\rm HS}^2+\|\Delta c\|_2^2.
\]
Only K is Hilbert–Schmidt. The canonical initial state is
\((g,0,0)\), where \(g\sim N(0,I_2)\) is the full Gaussian row.
The initialized action, adjoint and coordinate operations are the
jointly constructed ones in the supplied established proofs.

There is \(\delta_Y>0\), independent of width and sample count, for
which all conclusions below hold on
\[
U_Y=\{\mu\in\mathcal P(Z):\mathcal W_1(\mu,\nu_*)<\delta_Y\}.
\]
This is relative to all probability laws on Z. There is no atom-count,
minimum-weight, input-angle, Gram-rank, or prescribed-label-function
condition. Constants may depend on Y and the fixed model and T.

## 2. Autonomous strong population flow and reached-state uniqueness

At each current state and every normalized input u, set
\[
h^1(u)=\phi(w\cdot u),\quad z^2(u)=Ah^1(u),\quad
h^2(u)=\phi(z^2(u)),\quad f(u)=\langle c,h^2(u)\rangle,\quad \phi=\tanh,
\]
\[
\delta(u)=c\phi'(z^2(u)),\quad Q(u)=A^*\delta(u),\quad r(u,y)=f(u)-y.
\]
For every \(\mu\in U_Y\) there is a solution
\(\theta_\mu\in C^1([0,40];\mathcal E)\), with one-sided endpoint
derivatives, to the autonomous strong equation
\[
\theta'_\mu=-2\left(
\int r\phi'(w\cdot u)Q(u)u\,d\mu,\quad
\int r\delta(u)\otimes h^1(u)\,d\mu,\quad
\int rh^2(u)\,d\mu\right),\qquad \theta_\mu(0)=(g,0,0).
\tag{A}
\]
The integrals are Bochner integrals in the displayed spaces.
The rank convention is \((a\otimes b)v=a\langle b,v\rangle\).
The equation computes every coefficient from the current state and
the fixed law; no prospective trajectory or response is supplied.

Uniqueness holds among strong raw solutions of (A) on the prescribed
carrier with the same initialized primitives and state. For any
\(s\in[0,40]\), its restriction to \([s,40]\) is the unique strong
continuation from its reached state, using the same law and retained
Gaussian primitives. This does not assert well-posedness from arbitrary
ambient operator states or any extension beyond this horizon.

The constructed paths satisfy the energy identity
\[
L_\mu(t)+\int_0^t\|\theta'_\mu(v)\|_{\rm raw}^2\,dv
=L_\mu(0)\le Y^2,\qquad \|c_\mu(t)\|_\infty\le2Yt.
\]
Additional query tails and weighted moments used in the proof are
conclusions for the constructed trajectories, not hypotheses of the
solution class or the competing solution.

## 3. Quantitative law continuity and actual finite capture

There are deterministic \(C_Y,a_Y>0\) and \(q_Y>0\) such that
\[
\sup_{t\le40}\|\theta_\mu(t)-\theta_\rho(t)\|_{\rm raw}
\le C_Y q^{a_Y}\quad
(q=\mathcal W_1(\mu,\rho)\le q_Y,\ \mu,\rho\in U_Y).
\tag{B1}
\]
The common raw bound extends this to a deterministic modulus for all
q. In particular, after increasing \(C_Y\),
\[
\sup_{t\le40,x}|f_\mu(t,x)-f_\rho(t,x)|
\le\Omega_Y(q),\qquad
\Omega_Y(q)=C_Yq^{a_Y}\ (0\le q\le q_Y),\quad
\Omega_Y(q)=C_Y\ (q>q_Y),
\tag{B2}
\]
where the constants may be enlarged so the second branch bounds all
states. Thus \(\Omega_Y(q)\to0\). The source proof actually supplies
Gaussian tails, but the weaker explicit Osgood/Hölder modulus already
proves the requested quantitative claim.

For each fixed Borel law \(\mu\in U_Y\), the actual finite GF exists
globally and
\[
\sup_{t\le40,x}|f_{n,\mu}(t,x)-f_\mu(t,x)|
\longrightarrow0\quad\hbox{in probability}.
\tag{B3}
\]
For every deterministic sequence of empirical laws \(\lambda_k\) with
\(\mathcal W_1(\lambda_k,\mu)\to0\), and every \(n_k\to\infty\),
\[
\sup_{t\le40,x}|f_{n_k,\lambda_k}(t,x)-f_\mu(t,x)|
\longrightarrow0\quad\hbox{in probability}.
\tag{B4}
\]
There is no restriction relating observation count to width.
For iid samples of sizes \(m_k\to\infty\) from the fixed \(\mu\),
independent of initialization, (B4) holds in joint probability for
every \(n_k\to\infty\).

Here is the state approximation and observation contract underlying
these prediction statements. For every fixed target law and required
accuracy, choose one finite comparison law, one finite raw Euler mesh,
and a finite oracle program, on the common population carrier, before
taking width to infinity. Its population raw path approximates
\(\theta_\mu\). Its realization on the actual initialized finite arrays,
with the actual initial readout included additively, approximates the
actual finite GF in the same-carrier metric
\[
\|\Delta w_n\|_F/\sqrt n+\|\Delta K_n\|_F+
                       \|\Delta c_n\|_2/\sqrt n
\]
uniformly through40, with error arbitrarily small in probability in
the ordered approximation limit. The learned increment is expanded
as finite ranks. Its HS norm and pairings are identified by the finite
double sums of the two corresponding same-layer Gram contractions.
No finite matrix is subtracted from an operator on another carrier.

An admitted observation starts with finitely many raw w,c and
forward/backward \(h^1,z^2,h^2,\delta,Q\) fields at specified times and
inputs, together with identified initialized generated fields. It uses
finitely many correctly typed \(A_0,A_0^*,A(t),A(t)^*,K(t),K(t)^*\)
actions, continuous globally Lipschitz coordinate operations, and fixed
bounded continuous gates multiplying named \(L^2\) fields. Its joint
same-layer empirical law converges with second moments, equivalently
in \(W_2\) for each finite tuple, to the specified population law.
Quadratic contractions and the paired initialized/current hidden
observables are included. Arbitrary unbounded coordinate products,
nonlinear clocks and inverse-gate fields are not admitted merely
because they have names elsewhere; separate moment proofs are needed.

The comparison fixes finitely many cutoffs and incoming tolerances
backwards over a finite time partition, then its finite law and mesh,
then takes the width/empirical-law limit. It never uses a width theorem
for a growing transcript or assumes operator-norm convergence between
different carriers. The same comparison with the actual target law
held equal to the fixed Borel \(\mu\) proves (B3); only its oracle law
must be finite. Compact data partitions give the iid consequence.

## 4. Uniform nonlinear response and the finite nonlinear limit

For any \(\nu\in\mathcal P(Z)\), let
\(\sigma=\nu-\nu_*\) and \(\mu_\epsilon=(1-\epsilon)\nu_*+\epsilon\nu\).
Choose
\[
\epsilon_Y=\min\{1/2,\delta_Y/[2(2+2Y)]\}>0.
\]
The coupling retaining unchanged mass gives
\(\mathcal W_1(\mu_\epsilon,\nu_*)\le\epsilon(2+2Y)\), so the whole
inclusive interval \(0\le\epsilon\le\epsilon_Y\) is inside U_Y.

Let \(D_\sigma f\) be exactly the response of frozen P1, identified
there from actual finite-GF right derivatives taken before width.
There is a deterministic modulus \(\omega_Y(\epsilon)\to0\), uniform
over \(\nu\in\mathcal P(Z)\), such that
\[
\sup_{t\le40,x}
|f_{\mu_\epsilon}(t,x)-f_{\nu_*}(t,x)-\epsilon D_\sigma f(t,x)|
\le\epsilon\omega_Y(\epsilon).
\tag{C1}
\]
The proof also gives the analogous \(o(\epsilon)\) raw-state remainder
with P1's raw linear variation.

The exact clock is \(X_j=F(w_j)\),
\(F(z)=z/2+\sinh(2z)/4\). Its initial value \(F(g_j)\) is in \(L^2\).
Subtracting the fixed initial field gives exactly P1's clock; the two
response tangents coincide. At the reference axes its homogeneous
field has no first-layer gate, and the signed-law forcing and bounded
linear generator are P1's. Uniqueness of that linear equation identifies
the response. No differentiation of an assumed population map is used.

For completeness, the nonlinear error proof first establishes tails
on the actual reached family. Active Euler query tails imply passive
query tails by insertion of a small probe atom and quantitative law
comparison. Tanh radial saturation then gives a Gaussian-square
moment for the reached row using Jensen in time and data. Hölder
supplies square uniform integrability of the inverse-gate forcing.
The reference source family is compact in continuous Hilbert-space
curves, so its propagated response directions are compact.
Taylor consistency on these directions, and a Lipschitz comparison
with one uniformly bounded readout endpoint, gives (C1). This is not
ambient \(L^2\) Fréchet differentiability, nor a quadratic remainder.

Using common initialization across epsilon, the actual finite right
derivative
\(D_\sigma f_n=\partial_{\epsilon+}f_{n,\mu_\epsilon}|_{\epsilon=0}\)
exists for each width. For every separately fixed \(\nu\) and \(a>0\),
\[
\lim_{\epsilon\downarrow0}\limsup_{n\to\infty}
\Pr\left[
\frac{\sup_{t\le40,x}|f_{n,\mu_\epsilon}-f_{n,\nu_*}
                         -\epsilon D_\sigma f_n|}{\epsilon}>a
\right]=0.
\tag{C2}
\]
Indeed the normalized left remainder is bounded by
\(\omega_Y(\epsilon)\), plus the two finite prediction errors divided
by the fixed positive epsilon, plus the P1 finite-derivative error.
(B3) and P1 send the random errors to zero at fixed epsilon; only then
is epsilon sent to zero. No width-uniform finite-n remainder,
supremum of failure probabilities over laws, or joint epsilon/width
rate is asserted.

## 5. Existing risk and hidden-activity subclasses

On the binary-label subclass and the intersection with the established
C.4.5 ball
\(\mathcal W_1(\mu,\nu_*)<\exp\{-\exp(3000)\}\), the constructed
population has risk at time40 at most 1/4 and both training-averaged
paired squared hidden displacements at time1/200 at least \(10^{-13}\).
These are the exact existing admitted subclass and times.

To justify the interface, the C.4.5.3 comparison applies to finite GF
with zero discretization defect, giving its strict margins.
For uniformly bounded predictions,
\(|R_\mu(f)-R_\mu(g)|\le2(B+Y)\|f-g\|_\infty\).
The fixed-state loss integrand is Lipschitz on the compact input/label
space with constant \(2(B+Y)\max(\operatorname{Lip}f,1)\).
Thus (B3)–(B4) pass the risks. For hidden features bounded by one,
\[
|\|H-H_0\|_2^2-\|\bar H-H_0\|_2^2|
\le4\|H-\bar H\|_2 .
\]
The raw observation approximation retains H and \(H_0\) on the same
carrier, and input continuity passes the training-law integral.
It therefore passes the paired activity margins as well.
No universal fitting, all-law activity, time40 activity, endpoint
selection, or superiority to frozen features is claimed.

## 6. Complete proof map and review boundaries

Every invoked scientific argument is included in the frozen candidate
and dependency inputs. The proof chain is:

1. P2_SOURCE_BOOTSTRAP, §§2–3: exact depth-two named-source recursions,
   step/atom-mass densities, and temporary-cap moment bounds.
2. Its §6.1: fresh complete-query forcing, finite width first and forcing
   second, establishes the reference physical clock Euler coefficient
   bound without assuming a response cap.
3. Its §§5 and6.2: differentiated clock consistency and a causal
   bootstrap transfer that bound to reference raw Euler.
4. Its §4: weighted all-law coefficient comparison, retaining tiny
   atom masses and same passive output queries, closes a second causal
   bootstrap on one positive law neighborhood. Gaussian query tails
   give H for all fine raw Euler programs.
5. P2_CONTINUATION, §§2–4: raw HS comparison, Osgood completion,
   strong integral equation, reached uniqueness/restart and actual
   finite capture. Choose a smaller radius than the source theorem's
   radius so every constant is uniform on U_Y.
6. P2_COMBINED_TAIL_CONTRACT, §§3–6, and P2_VARIATION: reached
   weighted forcing, compact response directions and uniform nonlinear
   remainder, with exact P1 identification.
7. Corrected P2_REFERENCE_COMPARISON supplies the precise observation
   grammar; P2_RESPONSE_BRIDGE supplies the exact ordered limit (C2).
   Frozen P1 supplies its actual finite-first derivative theorem.

The exact model and physical equation in this document also supply the
assignment referred to by the original variation proof. Its response
is defined there by its displayed linear equation before being identified
with P1 here. The original combined report's exclusion of a finite-width
nonlinear remainder excludes a uniform finite-n bound/rate; it does not
exclude the explicitly proved ordered limit (C2).

The source proof's historical root-comparison hash records its reading
snapshot. This candidate uses the corrected current comparison and
bridge files listed in its manifest. The corrections make the residual
factor, normalized law metric, continuous gates, raw starting fields,
and law quantifiers explicit. No previous acceptance verdict substitutes
for rereading any of these proofs.

The statements concern GF only. No training experiment, parameter
sweep, GD derivative, global changed-law dynamics, or change of
architecture or initialization forms any part of this candidate.
