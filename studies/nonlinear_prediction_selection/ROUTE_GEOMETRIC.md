# Geometric route: slow constrained feature learning

Frozen independent candidate, 2026-09-12. Author: `geometric_route` scoped agent.
Status: exact finite-width identities, a conditional slow-limit theorem, and an
exact nonlinear finite-state witness inside the stated architecture. **The
prescribed Gaussian-initialization, infinite-width target is not proved.**
No experiment was run. No Git write was made.

## 1. Contract and actual input scope

The scientific input was exclusively the supervisor's prompt: two hidden tanh
layers; \(h_1=\tanh(W_1u)\), \(h_2=\tanh(W_2h_1)\),
\(f=W_3^Th_2/n\), \(u\in S^1\), physical input \(x=\sqrt2u\); independent
stored Gaussian variances \((1,1/n,1/n^2)\); mobilities \((n,1,n)\); unhalved
square loss; fixed mixture

\[
 L_\varepsilon=(1-\varepsilon)R_0+\varepsilon R_\nu,
 \quad R_0=\tfrac12[(f(e_1)-1)^2+(f(e_2)+1)^2],
 \quad R_\nu=\sum_{a=1}^kp_a(f(v_a)-y_a)^2.
\]

All mixture runs start from the original initialization. An established reference
has a fitted latent endpoint with whole-circle prediction \(F_*\). Supplied
changed-law population capture only covers physical times through 40; supplied
first-response information is fixed-time information. Neither statement supplies
a nonlinear slow-time theorem. No formula for the latent state, its metric, its
endpoint, or its derivatives was supplied.

The requested observables are a determining whole-circle prediction, an
added-law risk improvement bounded below independently of \(\varepsilon\), actual
hidden-feature displacement, and finite autonomous capture on a nonzero slow
episode. I interpret the risk as \(R_\nu\). At a fitted starting state,

\[
0\le L_\varepsilon(\theta_*)=\varepsilon R_\nu(\theta_*),
\]

so a positive decrease of total mixture risk bounded below independently of
\(\varepsilon\) is impossible on the post-fitting episode for bounded fixed
labels. Its natural size is \(O(\varepsilon)\).

The desired population limit would require, for example, for every
\(0<\delta<T\),

\[
 \lim_{\varepsilon\downarrow0}\limsup_{n\to\infty}
 \Pr\!\left(\sup_{\delta\le\tau\le T}
 \|f_{n,\varepsilon}(\tau/\varepsilon,\cdot)-\bar F_\tau\|_{C(S^1)}
 >\eta\right)=0.
\]

The finite-width theorem below instead fixes \(n\) before taking
\(\varepsilon\downarrow0\). The distinction is substantive.

Process sources actually read, in full: `AGENTS.md`, `RESEARCH_WORKFLOW.md`,
`/etc/codex/skills/solve-math-rigorously/SKILL.md`,
`/etc/codex/skills/investigate-conjectures/SKILL.md`, and the latter skill's
`references/research-contract.md`, `references/adversarial-audit.md`, and
`references/proof-search-orchestration.md`. These were process inputs, not
scientific evidence. No study file, book/code source, other route, prior verdict,
scientific website, or scientific reference was read. Missing scientific inputs
are listed in Section 8. The scoped assignment replaces routine study startup.

## 2. Exact metric and finite-width dynamics

Write \(\theta=(W_1,W_2,W_3)\) and
\(M_n=\operatorname{diag}(nI,I,nI)\). The flow is
\(\dot\theta=-M_n\nabla L_\varepsilon\). Set
\(q=M_n^{-1/2}\theta\). The Euclidean metric of \(q\) is the mobility metric

\[
 \|d\theta\|_{M_n^{-1}}^2
 =n^{-1}\|dW_1\|_F^2+\|dW_2\|_F^2+n^{-1}\|dW_3\|_2^2.
\]

The \(q\)-flow is ordinary gradient flow. Smoothness of tanh gives local
existence and uniqueness. It is global at each fixed width: energy dissipation
gives \(\int_0^t\|\dot q\|^2ds\le L_\varepsilon(q(0))\), hence
\(\|q(t)-q(0)\|\le\sqrt{tL_\varepsilon(q(0))}\). A finite-time solution stays
in a finite Euclidean ball, where the smooth vector field is bounded and locally
Lipschitz; it therefore extends across every finite time.

Let \(w_i\) denote row \(i\) of \(W_1\), let \(a_j=(W_3)_j\), and let
\(s_{1i}=1-h_{1i}^2, s_{2j}=1-h_{2j}^2\). Direct differentiation gives

\[
 \partial_{a_j}f=h_{2j}/n,\qquad
 \partial_{(W_2)_{ji}}f=a_js_{2j}h_{1i}/n,
\]
\[
 \nabla_{w_i}f=\frac{s_{1i}}n
 \left(\sum_j a_js_{2j}(W_2)_{ji}\right)u.
\]

These identities keep both hidden feedback terms. In particular,
\(\dot a_j=-2\mathbb E[(f-y)h_{2j}]\),
\(\dot W_{2,ji}=-(2/n)\mathbb E[(f-y)a_js_{2j}h_{1i}]\), and
\(\dot w_i=-2\mathbb E[(f-y)s_{1i}(\sum_j a_js_{2j}W_{2,ji})u]\), with
expectation under the fixed mixture throughout.

## 3. Conditional slow limit from the original starting point

Define

\[
 g(q)=(f_q(e_1)-1,f_q(e_2)+1),\quad
 J(q)=Dg(q),\quad \mathcal M=\{q:g(q)=0\}.
\]

Assume at this fixed width that the unperturbed trajectory from the prescribed
starting point converges to a finite \(q_*\in\mathcal M\), and that
\(J(q_*)\) has rank two. For a sufficiently small neighborhood, \(\mathcal M\)
is a smooth manifold and \(J(q)J(q)^T\succeq\lambda I_2\) for some
\(\lambda>0\). The tangent projection at \(q\in\mathcal M\) is

\[
 P(q)=I-J(q)^T[J(q)J(q)^T]^{-1}J(q).
\]

Let \(\bar q\) solve

\[
 \frac{d\bar q}{d\tau}=-P(\bar q)\nabla R_\nu(\bar q),
 \qquad \bar q(0)=q_*.
 \tag{G}
\]

There is a fixed \(T>0\) such that this trajectory remains in a compact part of
the regular neighborhood. For every \(0<\delta<T\),

\[
 \sup_{\delta\le\tau\le T}
 \|q_\varepsilon(\tau/\varepsilon)-\bar q(\tau)\|\longrightarrow0.
 \tag{1}
\]

Here \(q_\varepsilon\) is the actual fixed-mixture trajectory from the original
starting point, without a restart or optimizer change.

### Proof

The elementary geometric fact used is this: a \(C^3\) map \(g\) with surjective
derivative has a local \(C^3\) zero manifold; in a sufficiently small tube each
point has a unique representation \(q=m+z\), \(m\in\mathcal M\),
\(z\perp T_m\mathcal M\), and nearest projection \(\pi(q)=m\) is \(C^2\),
with \(D\pi(m)=P(m)\). To see the needed hypotheses and construction, choose two
coordinate directions on which \(Dg\) is invertible and solve \(g=0\) for those
coordinates by the local inverse-function theorem. The normal-coordinate map
\((m,z)\mapsto m+z\) has invertible derivative at \(z=0\), since tangent and
normal spaces are complementary. Apply the same local inverse theorem and
shrink the neighborhood. Compact subpatches have uniform derivative bounds.

At \(q=m+z\), Taylor expansion gives

\[
 \nabla R_0(q)=J(m)^TJ(m)z+O(|z|^2),\qquad
 D\pi(q)\nabla R_0(q)=O(|z|^2).
\]

The second estimate uses \(P(m)J(m)^T=0\), together with
\(D\pi(q)=P(m)+O(|z|)\). Since the squared distance has gradient \(2z\), the
normal distance \(d=|z|\) satisfies, after shrinking the tube,

\[
 D^+d\le-cd+C\varepsilon,
 \quad
 d(t)\le d(t_0)e^{-c(t-t_0)}+C'\varepsilon.
 \tag{2}
\]

Indeed \(z\) is normal at \(m\), so
\(\langle z,J(m)^TJ(m)z\rangle\ge\lambda |z|^2\). The cubic Taylor error is
absorbed by half this term. The added gradient is uniformly bounded in the
chosen compact tube. The same inequality holds at \(d=0\) in the upper right
derivative sense.

For \(m(t)=\pi(q_\varepsilon(t))\),

\[
 \dot m=-\varepsilon P(m)\nabla R_\nu(m)
       +O(d^2+\varepsilon d).
 \tag{3}
\]

The integrated error over \(0\le t-t_0\le T/\varepsilon\) is bounded by

\[
 \int_{t_0}^{t_0+T/\varepsilon}C(d^2+\varepsilon d)dt
 \le C_T[d(t_0)^2+\varepsilon d(t_0)+\varepsilon].
 \tag{4}
\]

The constrained vector field is Lipschitz on the compact patch. Comparing the
integral equations in slow time yields an error bounded by (4) times \(e^{LT}\),
plus the initial projected-state difference. This comparison follows directly
by iterating \(E(\tau)\le a+L\int_0^\tau E(s)ds\), which gives
\(E(\tau)\le ae^{L\tau}\).

Now choose a large *fixed* \(t_0\) along the original unperturbed trajectory.
Continuous dependence on the loss parameter gives
\(q_\varepsilon(t_0)\to q_0(t_0)\). As \(t_0\to\infty\),
\(\pi(q_0(t_0))\to q_*\) and its normal distance tends to zero. Apply (2)--(4),
first sending \(\varepsilon\to0\), then \(t_0\to\infty\). The slow-time shift
\(\varepsilon t_0\) tends to zero. The normal distance at
\(t=\tau/\varepsilon\), \(\tau\ge\delta\), vanishes by (2). This proves (1).
A first-exit argument justifies staying in the patch: choose the reduced path
in its interior, use the preceding estimates up to the first exit, and choose
the initial normal distance and \(\varepsilon\) small enough that an exit is
impossible. There is no training restart in this proof.

The clock is therefore \(\tau=\varepsilon t\). It comes from the nonzero
tangential force of size \(\varepsilon\) and \(O(1)\) normal restoration, not
from extrapolating a fixed-time Taylor response.

On a compact parameter patch, \(q\mapsto f_q\in C(S^1)\) is Lipschitz: its
parameter derivative is jointly continuous on the compact product with \(S^1\).
Thus (1) implies whole-circle convergence. The same argument applies to the
hidden-feature map

\[
 H_n(q)(u)=\big(n^{-1/2}h_1(u),n^{-1/2}h_2(u)\big)
 \in C(S^1;\mathbb R^{2n}).
\]

All constants in this theorem may depend on \(n\). No assertion of uniformity
in width, Gaussian probability, or latent-state validity is included.

## 4. Determining dynamics and strict open-family criteria

Write the mobility kernel as
\(K_q(u,v)=\nabla_q f_q(u)\cdot\nabla_q f_q(v)\). With \(E=(e_1,e_2)\), define

\[
 K_q^c(u,v)=K_q(u,v)-K_q(u,E)K_q(E,E)^{-1}K_q(E,v).
 \tag{5}
\]

Along (G),

\[
 \partial_\tau\bar F_\tau(u)
 =-2\sum_a p_a[\bar F_\tau(v_a)-y_a]K_{\bar q(\tau)}^c(u,v_a).
 \tag{6}
\]

This is exact but is not a closed prediction-only equation: the kernel evolves
with both hidden layers. The determining object is (G) together with
\(\bar F_\tau(u)=f_{\bar q(\tau)}(u)\). Freezing (5) would change the model.

There is a precise local criterion for the required open family. Put
\(V_\nu=-P\nabla R_\nu\), evaluated at \(q_*\), and suppose

\[
 \|V_\nu\|>0,\qquad
 \|DH_n(q_*)V_\nu\|_{C(S^1)}>0.
 \tag{7}
\]

The second condition is about hidden features, and excludes a mere parameter
gauge displacement. Fix an observation \(u_0\in S^1\). To also separate the
nonlinear path from the frozen constrained kernel, require

\[
 A_\nu(u_0):=-2\sum_a p_a[F_*(v_a)-y_a]
 DK^c_{q_*}(u_0,v_a)[V_\nu]\ne0.
 \tag{8}
\]

The frozen comparison is the autonomous linear prediction equation obtained by
replacing \(K^c_{\bar q(\tau)}\) in (6) by \(K^c_{q_*}\), with initial prediction
\(F_*\). Both paths have the same first derivative. Differentiating (6) shows
that their second-derivative difference at zero is exactly (8): the derivatives
of residuals cancel, leaving only the displayed kernel derivative.

For a sufficiently small fixed \(\tau_1>0\), conditions (7)--(8) give constants
\(c_R,c_H,c_N>0\) such that, for \(0<\tau\le\tau_1\),

\[
 R_\nu(q_*)-R_\nu(\bar q(\tau))\ge c_R\tau,
\]
\[
 \|H_n(\bar q(\tau))-H_n(q_*)\|_{C(S^1)}\ge c_H\tau,
\]
\[
 |\bar F_\tau(u_0)-F^{\rm frozen}_\tau(u_0)|\ge c_N\tau^2.
 \tag{9}
\]

For the first inequality use the exact identity
\(dR_\nu/d\tau=-\|P\nabla R_\nu\|^2\) and continuity. For the second use the
Banach-space Taylor expansion of \(H_n(\bar q(\tau))\); its leading coefficient
is nonzero by (7). For the third use the second-order Taylor expansion and (8).
One can, for example, take half the positive leading coefficient after
shrinking \(\tau_1\).

These inequalities persist uniformly on a small closed neighborhood of the
atom parameters \(v_a\in S^1,\ y_a\in\mathbb R,\ p_a>0\), with \(\sum p_a=1\), because all displayed
strict quantities are continuous. Select an interior law whose inputs have
nonzero pairwise inner products and nonzero inner products with both reference
inputs. A sufficiently small neighborhood retains those properties and is
open in the finite-atom parameter space. At any one fixed \(0<\tau\le\tau_1\),
the finite-width convergence theorem transfers the first two lower bounds to
the actual fixed-mixture run for all sufficiently small \(\varepsilon\), with
smaller positive constants independent of \(\varepsilon\). In the hidden
comparison one may use the actual reference run at the same physical time,
since \(H_n(q_0(\tau/\varepsilon))\to H_n(q_*)\).

Conditions (7)--(8), including their nonzero margins, have **not** been verified
at the supplied latent endpoint. The next section proves they are simultaneously
possible in the exact architecture, rather than assuming that nonlinear motion
is excluded by the two fitted samples.

## 5. Exact two-state nonlinear witness, uniform in width

For every \(n\), the permutation-symmetric parameter family

\[
 (W_1)_{i,:}=w^T,\qquad (W_2)_{ji}=b/n,\qquad (W_3)_j=a
 \tag{10}
\]

is invariant under the **full fixed-mixture gradient flow for arbitrary data**.
Substitute (10) into the derivatives in Section 2: every first-layer row has
the same velocity, every second-layer entry has velocity \(\dot b/n\), and
every readout has velocity \(\dot a\), with

\[
 f(u)=a\tanh(b\tanh(w\cdot u)),
\]
\[
 \dot w=-2ab\mathbb E[(f-y)s_2s_1u],\quad
 \dot b=-2a\mathbb E[(f-y)s_2h_1],\quad
 \dot a=-2\mathbb E[(f-y)h_2].
\]

The induced mobility metric is exactly
\(|dw|^2+db^2+da^2\): the \(n\) first-layer copies cancel their factor \(n^{-1}\),
the \(n^2\) second-layer copies cancel \((db/n)^2\), and the readout copies cancel
their factor \(n^{-1}\). This is an exact four-state subsystem at every width.

In the positive branch of its fitted set, write

\[
 w=(s,-s),\quad s,b>0,\quad
 a(s,b)=\frac1{\tanh(b\tanh s)}.
 \tag{11}
\]

The equation \(w_2=-w_1\) is forced by the two fitting equations and the strict
injectivity and oddness of tanh. The entire circle is determined by two states:

\[
 F_{s,b}(u)=\frac{\tanh(b\tanh(s(u_1-u_2)))}{\tanh(b\tanh s)}.
 \tag{12}
\]

The induced metric on (11) is

\[
 G(s,b)=
 \begin{pmatrix}2+a_s^2&a_sa_b\\a_sa_b&1+a_b^2\end{pmatrix},
 \quad
 \binom{s'}{b'}=-G(s,b)^{-1}\nabla_{s,b}R_\nu(s,b).
 \tag{13}
\]

This is a finite autonomous determining equation with active hidden feedback.
Both its dimension and coefficients are independent of width and of
\(\varepsilon\). The full reference derivative has rank two at these points:
the derivative with respect to the first-layer first coordinate is nonzero for
\(e_1\) and zero for \(e_2\), and conversely for the second coordinate. Thus the
regularity hypothesis of Section 3 really holds here. Symmetry of the full
gradient and its normal projection makes its restriction equal to (13).

Choose \(0<\alpha<\pi/4\),
\(v=(\cos\alpha,\sin\alpha)\), \(\widetilde v=(\sin\alpha,\cos\alpha)\),
and \(d=\cos\alpha-\sin\alpha\in(0,1)\). Their inner product is
\(\sin(2\alpha)\in(0,1)\), and both coordinates of both inputs are nonzero.
Let

\[
 F(s,b)=F_{s,b}(v),\qquad
 \nu=\tfrac12\delta_{(v,y)}+\tfrac12\delta_{(\widetilde v,-y)}.
\]

Then \(R_\nu=(F-y)^2\). The function \(F\) is nonconstant and has nonzero
gradient everywhere on the positive branch. Here is a direct sign proof. Put
\(e(z)=2z/\sinh(2z)\). For \(z>0\), \(e(z)>0\) and \(e'(z)<0\), since
\(\sinh(2z)-2z\cosh(2z)<0\); the latter expression is zero at zero and has
derivative \(-4z\sinh(2z)<0\). For
\(\phi_b(s)=\tanh(b\tanh s)\), its logarithmic elasticity is

\[
 E_b(s)=\frac{s\phi_b'(s)}{\phi_b(s)}=e(s)e(b\tanh s).
\]

It strictly decreases in \(s>0\). Therefore

\[
 \partial_s\log F(s,b)=\frac{E_b(sd)-E_b(s)}s>0.
 \tag{14}
\]

Let \(k(s,b)=\|\operatorname{grad}_G F\|_G^2>0\). There is at least one point
\(q_0=(s_0,b_0)\) where

\[
 c(q_0):=Dk(q_0)[\operatorname{grad}_G F(q_0)]\ne0.
 \tag{15}
\]

This existence claim has a short proof which avoids assuming a generic
curvature condition. The surface (11) is closed as a subset of finite Euclidean
\((w,b,a)\)-space: a finite convergent sequence on it cannot have \(s\to0\) or
\(b\to0\), since then \(a\to\infty\), and the formula passes to every other
finite limit. Suppose \(Dk[\operatorname{grad}_G F]=0\) everywhere. Start the
gradient-ascent ODE for \(F\) at any point. Then \(k\) is the positive constant
\(k_0\) along its trajectory, so its Euclidean speed on the embedded surface is
\(\sqrt{k_0}\). It cannot escape to infinity in finite time. Closedness and
local smoothness imply extension for all positive time. But
\(dF/dt=k_0\), while \(F<1\) everywhere, a contradiction. This proves (15).
Continuity makes its set nonempty and open, so \(s_0,b_0\) can also be chosen
rational. This is an existential construction; no numerical search was used.

Set \(y=(1+F(q_0))/2\) and \(r_0=F(q_0)-y<0\). Both labels \(y,-y\)
lie strictly inside \((-1,1)\). For the constrained flow,

\[
 F'=-2(F-y)k,\quad k'=-2(F-y)c.
\]

At zero the residual is \(r_0\ne0\), so the risk decreases at rate
\(4r_0^2k(q_0)>0\).
The second prediction derivative differs from the frozen-kernel derivative by

\[
 F''(0)-(F^{\rm frozen})''(0)=4r_0^2c(q_0)\ne0.
 \tag{16}
\]

The hidden-feature velocity is also nonzero. By (14), the state velocity is
nonzero. If \(s'\ne0\), already \(h_1(e_1)'=\operatorname{sech}^2(s)s'\ne0\).
If \(s'=0\), then \(b'\ne0\) and
\(h_2(e_1)'=\operatorname{sech}^2(b\tanh s)\tanh(s)b'\ne0\).
The normalized \(H_n\) norm of these replicated features is independent of
width. Consequently all three inequalities (9) hold with positive constants
independent of both \(n\) and \(\varepsilon\) for this invariant class.

Small independent perturbations of the two inputs, their labels, and their
positive weights preserve the strict inequalities. Thus the construction gives
an open finite-atom family, not merely the exactly swap-symmetric law. Formula
(13) remains valid for every such perturbed law.

There is no need for a staged optimizer even in this restricted construction.
Choose an initial point in a sufficiently small neighborhood of (11) inside
the invariant four-state family. The estimates (2)--(3) with
\(\varepsilon=0\) imply normal exponential decay and integrable tangential
velocity, hence convergence to a nearby fitted point. The strict properties
persist there. Train the fixed mixture from that same initial point; Section 3
then supplies the episode. This gives an open set of starts *within the
four-state family*.

**Decisive limitation:** for \(n\ge2\), (10) has probability zero under the
prescribed independent Gaussian stored initialization. No attraction of the
original initialized system to (10), or replacement of its endpoint by (11),
is claimed. The normal restoration of the two reference errors does not
contract the enormous collection of tangential directions. Thus this exact
witness establishes that the architecture and mobility permit the mechanism;
it does not answer the original Gaussian population problem by itself.

## 6. What a finite-capture bridge would actually require

There is a useful elementary approximation lemma, conditional on a suitable
latent state space. Suppose a limiting constrained equation
\(q'=V(q)\) exists on a separable Hilbert space, \(V\) is locally Lipschitz on a
neighborhood of its compact path \(q([0,T])\), and a known increasing sequence
of finite-rank orthogonal projections \(P_N\to I\) is available. Suppose also
that the restrictions \(P_NV|_{\operatorname{ran}P_N}\) are computable from the
specified model and retained initial data, with no hidden trajectory oracle.
Use

\[
 q_N'=P_NV(q_N),\quad q_N(0)=P_Nq(0).
\]

For paths remaining in the Lipschitz neighborhood, integral comparison gives

\[
 \sup_{t\le T}\|q_N(t)-q(t)\|
 \le e^{LT}\left(\|(I-P_N)q(0)\|
 +\int_0^T\|(I-P_N)V(q(s))\|ds\right).
 \tag{17}
\]

The second term tends to zero uniformly because the continuous image
\(V(q([0,T]))\) is compact: cover it by finitely many small balls, use convergence
at their centers, and use \(\|I-P_N\|\le1\). The initial term also vanishes.
An interior-neighborhood first-exit argument removes the provisional path
restriction. If the prediction and hidden observation maps are locally
Lipschitz into their stated whole-circle spaces, (17) captures both uniformly.

The choice of basis and projected vector field precedes the trajectory. The
proof uses compactness of the true path to establish convergence, not as an
input to the numerical vector field. Uniform capture over a small compact
finite-atom family follows if solution dependence is continuous and the family
remains in a common Lipschitz neighborhood; its path union is then a continuous
image of a compact parameter-time set.

This supplies **no rate** without a source estimate for the projection tail.
It also does not supply the latent equation, a Hilbert topology with all these
properties, uniform width estimates, or a permitted finite representation of
its projected coefficients. In particular, treating an arbitrary function or
the whole original width-\(n\) state as a single “coordinate” would violate the
finite-capture contract. The raw finite-width \(q\)-norm itself is not uniformly
bounded at initialization: \(\mathbb E\|W_2\|_F^2=n\). A centered/random-field
latent representation and suitable norm have to be established first.

## 7. Counterexample attacks and logical force

1. **Fitting does not imply a regular normal manifold.** Here is an exact
   fitted rank-deficient point at width two. Set both first-layer rows to
   \((s,-s)\), \(h=\tanh s>0\), and set the two rows of \(W_2\) to
   \((b_j/2,b_j/2)\), with \(b_1=1/h,b_2=2/h\). Choose readouts \(a_1,a_2\) to
   satisfy
   \(\sum_j a_j\tanh(j)=2\) and
   \(\sum_j a_jb_j\operatorname{sech}^2(j)=0\).
   This linear system is invertible: the ratios
   \(\tanh(j)/(j\operatorname{sech}^2(j))=\sinh(2j)/(2j)\) are distinct.
   The point fits \(+1,-1\). Both first-layer prediction gradients vanish by
   the second equation, while the \(W_2,W_3\) prediction gradients at \(e_2\)
   are the negatives of those at \(e_1\). Consequently \(J\) has rank one.
   This is a proof-route counterexample to deriving a normal gap from fitting
   alone, not a counterexample to the desired Gaussian endpoint.

2. **The whole-circle endpoint prediction does not determine its slow law.**
   A hidden branch with readout zero contributes no prediction, but its
   readout derivative contributes a feature outer product to \(K\). Its
   hidden weights can therefore be changed without changing \(F_*\), while
   changing future readout-learning directions. Conditioning against the two
   reference evaluations only removes two evaluation directions; it does not
   in general remove the branch's circle-valued feature. Hence a formula for
   \(F_*\) alone cannot identify (5).

3. **Hidden parameter motion is weaker than feature motion.** Redundant hidden
   weights can move while leaving the actual features unchanged. The criterion
   used here is \(DH_nV\ne0\), not merely a nonzero hidden parameter component.

4. **Feature motion is weaker than nonlinearity in prediction dynamics.** A
   moving representation could keep its effective kernel constant. Condition
   (8), and the exact witness (16), exclude that explanation locally. They
   establish a positive fixed-τ discrepancy from the matched frozen constrained
   kernel, rather than merely comparing with a zero-motion baseline.

5. **A symmetric finite subsystem is not population capture from Gaussian
   starts.** Its measure-zero initialization and uncontrolled transverse
   tangential directions are a major, currently unresolved reachability
   obstruction. Treating (13) as the desired population answer would substitute
   a different initialization.

6. **The clocks and limits do not interchange automatically.** A theorem only
   through physical time 40 never reaches fixed positive \(\tau\) as
   \(\varepsilon\to0\). At fixed \(n\), the normal gap may exist but deteriorate
   with width. Both gaps affect necessary identification bridges, not merely
   constants in an already proved population theorem.

7. **Fixed-order response does not control the episode.** On \(t=\tau/\varepsilon\)
   all secular orders \((\varepsilon t)^j\) can contribute. The reduction proof
   controls the full vector field on that interval; it does not infer it from
   a first derivative in \(\varepsilon\).

## 8. Exact unresolved obligations and route recommendation

The desired theorem needs the following model-specific inputs, none of which
was present in this route's prompt-only source packet:

* A complete nonlinear latent-state equation, its original Gaussian
  initialization, its mobility topology, and whole-circle and hidden-feature
  observation maps.
* The endpoint *state* and derivative operators, not only \(F_*\). One must
  verify a uniform two-reference normal gap in the relevant topology, or
  develop a separate singular-manifold analysis if the gap fails.
* Long-time capture from the original fixed-mixture initialization. It must
  reach physical \(T/\varepsilon\) for small fixed \(\varepsilon\) and support
  the required order of width and perturbation limits. Capture through 40 is
  insufficient.
* At that actual endpoint, one open finite-atom family with the strict
  quantities (7)--(8), in norms that survive the population limit. The abstract
  projection formula and the explicit symmetric witness do not verify this.
* A finite approximation space with computable projected coefficients and a
  production estimate for its tails, plus propagation estimates controlling
  whole-circle prediction and hidden state. Section 6 supplies propagation and
  qualitative compact-path approximation only after the latent assumptions
  are established.

The best route-specific next bottleneck is to obtain the actual endpoint's
normal operator and the constrained off-reference feature gradient. Computing
or proving a positive normal gap and a nonzero hidden projected response there
would distinguish a viable slow-manifold route from its exact rank-deficient
obstruction. Even a positive answer would leave the nonlinear curvature,
long-time population capture, and finite-capture bridges to prove.

Recommended registry status: **concrete conditional reduction; blocked on
model-specific endpoint and long-time bridges**. The result is not a complete
target proof and is not described as nearly complete. The invariant witness,
scale selection, original-start reduction proof, and explicit singular fitted
point remain useful regardless of how those bridges are resolved. All claims
are author-derived and self-audited; there has been no independent review or
promotion.
