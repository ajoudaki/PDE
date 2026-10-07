# Dense-flow perturbation stability and the unresolved global setup route

2026-10-06. Scoped theoretical candidate; no experiments, no promotion, and no
claim of a completed efficient Harmonic setup algorithm.

The dense nonlinear flow has substantially better defect stability than the
generic Lipschitz bound over its physical training horizon suggests. The lemma
below gives amplification of order `exp(C sqrt(log(en)))` at fixed admissible
problem parameters, on the existing source event and on the full original label
allowance. Polynomial precision is sufficient for the coordinate accuracy used
by Harmonic compression. This does not itself construct the required source
coefficients. In particular, solving a global dense collocation system through
the whole training horizon would reconstruct the excluded dense training path.
Calling that operation a coefficient solve does not satisfy the clarified task.

## Scope and dependencies

The target retains arbitrary fixed hidden depth, real analytic activations with
bounded first derivative on a strip but possibly unbounded values, sphere
inputs, the feature-Gram gap, all nonlinear hidden updates, and the original
Harmonic prediction/storage theorem. The desired replacement concerns setup
only. The final prediction norm remains

\[
\sup_{t\in[0,\infty]}\sup_{\|x\|_2=\sqrt d}|f_C(t,x)-f_n(t,x)|.
\]

The supervisor's clarification excludes a complete dense training rollout,
including one represented as a global coefficient solve. A very short initial
dense prefix would require a demonstrated substantial cost reduction relative
to complete training. None is constructed here.

Allowed scientific inputs were `RESULT.md` in this study and
`docs/notation.qmd`. The relevant complete sections read were the shared setup;
the label/width conventions and dense model/fitting statements; the dense
comparison statements; the full Harmonic statement and setup cost section;
source recurrences S.2 and S.6--S.8; the dense global-fitting, signed-energy and
residual-damping proofs; the Harmonic source-expansion/initial-jet proof; the
source-metric/readout-cancellation proofs; and the all-horizon source extension.
The probabilistic source event is an imported hypothesis from `RESULT.md`, not
independently re-proved in this scoped note. No other study was read.

Input hashes at reading:

- `RESULT.md`: `c2cbd1bb0e6a39de87181df89be977eaf2e272fda4f1459ac934396d84e1b278`.
- `docs/notation.qmd`: `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023`.

Process instructions used were Part 1 of `RESEARCH_WORKFLOW.md`,
`investigate-conjectures` with its research-contract/adversarial-audit references,
and `solve-math-rigorously`. The required canonical-notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` was unreadable
even with a read-only escalation; no accessible copy was found in the available
skill roots. The supervisor authorized the fallback to the accessible rigorous
math skill, the notation contract, and the user's explicit notation rules.

## Deterministic setup

Let \(v=x/\sqrt d\), so \(\|v\|_2=1\), and retain the dense network

\[
z^{(1)}=Av,\qquad z^{(j)}=W^{(j)}h^{(j-1)},\qquad
h^{(j)}=\phi_j(z^{(j)}),\qquad f_n=w^Th^{(L)}/n.
\]

Its parameter coordinates with Euclidean mobility metric are

\[
\theta=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n).
\]

Write \(r_a=f_n(v_a)-y_a\), \(\rho=\|r\|_2/\sqrt m\),
\(Y=\|y\|_2/\sqrt m\), and \(\lambda=\gamma/m\). With
\(\xi_a(\theta)=\nabla_\theta f_n(v_a)\), the exact vector field is

\[
F(\theta)=-\frac2m\sum_{a=1}^m r_a\xi_a(\theta),\qquad
\dot\theta=F(\theta).
\tag{1}
\]

The initial readout is zero. All blocks train with the loss and mobilities of
`RESULT.md`; no frozen-feature model replaces (1).

Condition on the existing real-fitting and source event, including the stated
analytic-extension gates when all-time carrier control is used. The complete
original common label allowance is unchanged. The imported deterministic
conclusions needed here are

\[
\|A(t)\|_{\rm op}/\sqrt n<9,\qquad
\|W^{(j)}(t)\|_{\rm op}<9,\qquad
\|w(t)\|_2/\sqrt n\le 2Y/\sqrt\lambda,
\]
\[
\rho(t)\le Ye^{-\lambda t/2},\qquad
\int_0^\infty\rho(t)\,dt\le 2Y/\lambda,
\]
\[
\max_{a,j,i,t\ge0}|k_{a,i}^{(j)}(t)|\le M_n,
\qquad M_n=2K_{\rm src}S\sqrt{\log(en)},\qquad S=16Y/\lambda.
\tag{2}
\]

Here \(k^{(L)}=w\) and
\(k^{(j)}=(W^{(j+1)})^T\delta^{(j+1)}\), with
\(\delta^{(j)}=\phi_j'(z^{(j)})\odot k^{(j)}\).
The carrier maximum in (2) concerns only the true training trajectory. No
carrier maximum for perturbed trajectories or parameter segments is assumed.

Take \(b=\max_j|\phi_j(0)|\), and let \(s\ge1\), \(t_2\ge1\)
bound the first and second activation derivatives on the safe strip, as in the
source recurrences. Define explicit deterministic coefficients

\[
H_1=\max(1,b+10s),\qquad H_j=\max(1,b+10sH_{j-1}),\qquad H=H_L,
\]
\[
R=1+2Y/\sqrt\lambda,\quad B=Rs(10s)^{L-1},\quad
F_z=H(10s)^{L-1},\quad P_{\rm layer}=1+(L-1)H,\quad
G=H+P_{\rm layer}B,
\]
\[
D(M)=(10s)^{L-1}\{s(1+B)+Lt_2F_zM\},
\]
\[
J(M)=\sqrt{L+1}\{P_{\rm layer}D(M)+[1+(L-1)B]sF_z\},
\]
\[
C(M)=sF_z\sqrt L+LBsF_z+\frac12L^2t_2F_z^2M.
\tag{3}
\]

These constants expose dependence on depth, activation bounds and
\(Y/\sqrt\lambda\); \(\lambda=\gamma/m\) exposes the sample/gap
dependence. The parameter norm and these bounds are independent of input
dimension once the input norm is one. The original source event still has its
stated problem-dependent eventual-width qualification.

Every real state \(u\) within Euclidean distance one of \(\theta(t)\)
has mixer and normalized first-matrix operator caps ten and readout RMS at most
\(R\). Linear activation growth therefore gives feature RMS at most \(H\)
on the entire input sphere. These statements do not require bounded activation
values.

## Endpoint estimates with only one controlled carrier endpoint

Let \(e=u-\theta\), \(E=\|e\|_2\le1\), and let
\(D_h\) be the sum of the first normalized Frobenius discrepancy and
the hidden-matrix Frobenius discrepancies; let \(D_w\) be the readout
RMS discrepancy. Then
\(D_h\le\sqrt L E\) and \(D_h+D_w\le\sqrt{L+1}E\).
Forward subtraction through matrices with operator norm at most ten gives

\[
\sup_{v,j}\frac{\|z^{(j)}(u,v)-z^{(j)}(\theta,v)\|_2}{\sqrt n}
 \le F_zD_h,
\qquad
\sup_{v,j}\frac{\|h^{(j)}(u,v)-h^{(j)}(\theta,v)\|_2}{\sqrt n}
 \le sF_zD_h.
\tag{4}
\]

Indeed the first direct coefficient is one; every later direct coefficient is
at most \(H\), and each propagation contributes \(10s\). The sum of
the parameter block discrepancies is already in \(D_h\).

For a training sample, split the backward difference using the true carrier:

\[
\delta^{(j)}(u)-\delta^{(j)}(\theta)
=\phi_j'(z^{(j)}(u))\odot[k^{(j)}(u)-k^{(j)}(\theta)]
+[\phi_j'(z^{(j)}(u))-\phi_j'(z^{(j)}(\theta))]\odot k^{(j)}(\theta).
\]

The second term in RMS is bounded by \(t_2M_nF_zD_h\).
The first propagates with factor \(10s\), and changed mixers cost at
most \(sB\|\Delta W\|_F\). The top readout difference costs
\(sD_w\). Summing the resulting finite geometric recursion gives

\[
\frac{\|\delta_a^{(j)}(u)-\delta_a^{(j)}(\theta)\|_2}{\sqrt n}
\le D(M_n)(D_h+D_w).
\]

The exact gradient blocks are

\[
\xi_a=
\left(\frac{\delta_a^{(1)}v_a^T}{\sqrt n},
 \left(\frac{\delta_a^{(j)}h_a^{(j-1)T}}n\right)_{j=2}^L,
 \frac{h_a^{(L)}}{\sqrt n}\right).
\]

Bounding and subtracting these blocks gives

\[
\|\xi_a(u)\|_2,\|\xi_a(\theta)\|_2\le G,\qquad
\|\xi_a(u)-\xi_a(\theta)\|_2\le J(M_n)E.
\tag{5}
\]

There is also a Taylor remainder anchored at the true state:

\[
|f_n(u,v_a)-f_n(\theta,v_a)-\langle\xi_a(\theta),e\rangle|
\le C(M_n)E^2.
\tag{6}
\]

For completeness set \(\Delta h=h(u)-h(\theta)\),
\(\Delta z=z(u)-z(\theta)\), and
\(a^{(j)}=\Delta h^{(j)}-\phi_j'(z^{(j)}(\theta))\odot\Delta z^{(j)}\).
Scalar Taylor's formula gives
\(|a_i^{(j)}|\le t_2|\Delta z_i^{(j)}|^2/2\). Expanding the
network discrepancy by forward differentiation and then backward substitution
expresses its scalar remainder as

\[
\frac1n\sum_j k_a^{(j)}(\theta)^Ta_a^{(j)}
+\frac1n\sum_{j=2}^L\delta_a^{(j)}(\theta)^T
             \Delta W^{(j)}\Delta h_a^{(j-1)}
+\frac1n\Delta w^T\Delta h_a^{(L)}.
\]

The three absolute bounds are respectively
\(L^2t_2M_nF_z^2E^2/2\), \(LBsF_zE^2\), and
\(sF_z\sqrt L E^2\), proving (6). No Hessian bound on an
uncontrolled interpolating state has been inserted.

## Defect stability lemma

Let \(u:[0,T]\to\mathbb R^P\) be an absolutely continuous approximate
parameter path, where \(P=(L-1)n^2+n(d+1)\). Its additive ODE defect is

\[
d(t)=\dot u(t)-F(u(t)),\qquad
E_0=\|u(0)-\theta(0)\|_2+\int_0^T\|d(t)\|_2\,dt.
\]

Write \(J=J(M_n)\), \(C=C(M_n)\), and
\(A_n=4JY/\lambda\). Suppose

\[
E_0\le e^{-A_n}/4,\qquad
8(C+J)^2T e^{2A_n}E_0^2\le1.
\tag{7}
\]

Then

\[
\sup_{0\le t\le T}\|u(t)-\theta(t)\|_2\le 2e^{A_n}E_0.
\tag{8}
\]

**Proof.** Stop at discrepancy one. Put
\(e_{f,a}=f_n(u,v_a)-f_n(\theta,v_a)\), so the perturbed residual is
\(r_a+e_{f,a}\). The exact vector-field subtraction in (1) gives

\[
\frac12\frac d{dt}E^2
=-\frac2m\sum_a e_{f,a}\langle e,\xi_a(\theta)\rangle
 -\frac2m\sum_a(r_a+e_{f,a})
                  \langle e,\xi_a(u)-\xi_a(\theta)\rangle
 +\langle e,d\rangle.
\]

Using (5)--(6) and the ordinary sample RMS gives

\[
\frac12\frac d{dt}E^2
\le-2\frac{\|e_f\|_2^2}{m}
 +2(C+J)\frac{\|e_f\|_2}{\sqrt m}E^2
 +2J\rho E^2+E\|d\|_2.
\]

Maximizing the first two terms over their nonnegative scalar argument bounds
them by \((C+J)^2E^4/2\). Consequently, in the upper-derivative sense,

\[
E'\le 2J\rho E+\frac12(C+J)^2E^3+\|d\|_2.
\tag{9}
\]

At zero discrepancy use \((E^2+\varepsilon^2)^{1/2}\) and pass to
zero \(\varepsilon\); all coefficients and the defect are integrable.
Let \(a(t)=2J\int_0^t\rho(s)\,ds\le A_n\) and
\(z(t)=e^{-a(t)}E(t)\). As long as \(z\le2E_0\), integration
of (9) gives

\[
z(t)\le E_0+4(C+J)^2T e^{2A_n}E_0^3\le\frac32E_0.
\]

Thus a first crossing of \(2E_0\) is impossible. The first condition
in (7) also keeps \(E\le1/2\), so the geometric stop cannot occur.
The case \(E_0=0\) follows by uniqueness or the same regularization.
This proves (8).

At fixed admissible \(m,d,L,\gamma,Y\) and activations, (3) is affine
in \(M_n\), hence

\[
A_n=a_0+a_1\sqrt{\log(en)}
\]

for explicitly defined nonnegative coefficients \(a_0,a_1\).
The amplification is therefore subpolynomial in width. Its exponent has no
factor \(T\): the training residual is integrable and the negative
prediction-error square was retained before estimating it.

This is a finite-horizon defect theorem. It does not assert that an arbitrary
perturbed flow fits labels, nor that a persistent nonzero defect is harmless
over an infinite horizon. The original Harmonic endpoint theorem is unchanged.

## Polynomial precision for all source coordinates

The source families contain backward fields at every passive query. Their
carrier maxima are not supplied by (2). A deterministic RMS-to-coordinate
conversion is sufficient for this precision estimate.

Set

\[
K_q=R(10s)^{L-1},\qquad
C_{\rm src}=8\sqrt{L+1}\max\left\{
sF_z,\ (10s)^{L-1}[s(1+B)+Lt_2F_zK_q]\right\}.
\]

Every query carrier has RMS at most \(K_q\), hence maximum at most
\(\sqrt nK_q\). Repeat the backward subtraction above with that
maximum. A final RMS-to-coordinate conversion and \(\sqrt n\le n\)
show that each feature or response family differs between \(u(t)\) and
\(\theta(t)\) in coordinate norm by at most \(C_{\rm src}nE(t)\).
The factor eight also includes its initialized forward/reverse image because
\(\|W_0\|_{\rm op}\le8\). Consequently source accuracy \(\eta\)
is guaranteed if, in addition to (7),

\[
E_0\le \frac{\eta e^{-A_n}}{2C_{\rm src}n}.
\tag{10}
\]

For \(\eta=n^{-a}\), fixed \(a>0\), and
\(T=O((m/\gamma)\log n)\), the logarithm of the required inverse
defect tolerance is \(O(\log n+\sqrt{\log n})\), with the explicit
coefficients above. Thus polynomial precision suffices at the original
\(\eta=1/n\) specialization. This is a statement about the required
numerical tolerance, not the bit complexity of an activation evaluation or
the condition number of coordinate selection.

The source coefficient construction must still apply identical scalar linear
operations to both members of every initialized-mixer pair. Approximate ODE
solutions do not by themselves preserve that algebraic identity. Forming the
image from the computed base coefficient preserves it exactly in the same
exact-real operation model as `RESULT.md`; finite precision needs its own
roundoff allowance.

## What a global coefficient solve would and would not establish

A proposed Volterra construction would choose a temporal basis, represent
\(u(t)\), and solve the projected equation

\[
u(t)=\theta(0)+\int_0^tF(u(s))\,ds.
\tag{11}
\]

Any output satisfying a certified defect tolerance (7), (10) would suffice
for the source accuracy bridge. This is a genuine gain over the bound obtained
by multiplying a worst-case Jacobian norm by \(T\). It does not prove that
Picard, Newton, or a frozen-kernel preconditioner computes such an output from
initialization in polynomial work.

In particular:

1. The source's local holomorphy is a statement about the exact trajectory.
   It supplies neither a contraction region containing global solver iterates
   nor a defect certificate for an arbitrary interpolant.
2. A local linearized inverse is well behaved: differentiating (9) at zero
   discrepancy gives the same factor \(e^{A_n}\) for the forced variational
   equation. Newton convergence still requires an initial candidate in its
   basin and control of higher derivatives on that basin.
3. A frozen training Gram preconditions the damped sample-residual directions.
   The normalized parameter space has many directions in the kernel of the
   training Jacobian. The feature gap does not give coercivity on those
   directions; the residual-weighted curvature remains. The available bound
   for its accumulated norm grows like \(\sqrt{\log n}\), and does not
   imply a uniform Banach contraction at the full fixed label allowance.
   This is a missing proof, not a counterexample to all such constructions.
4. Enforcing small successive windows obtains a continuation method, but if
   those windows carry the dense state through \([0,T]\), this is a dense
   full-training computation under the clarified exclusion.
5. Even a successful simultaneous solution of (11) computes a dense path
   through the whole source horizon. Its lack of sequential time steps is not
   sufficient to meet the user's computational provenance restriction.

For clarity, a conditional operation inventory is possible without asserting
solver convergence. Let \(D+1\) be the number of temporal coefficient or
collocation nodes. One dense vector-field evaluation at every node costs
\(O(mP(D+1))\) scalar arithmetic plus \(O(Lmn(D+1))\) activation and
derivative calls. A direct scalar integral/basis transform applied to all
parameters costs \(O(P(D+1)^2)\). A simultaneous iteration retaining
all temporal parameter values uses \(O(P(D+1)+Lmn(D+1))\) words.
After \(I\) iterations the corresponding work bound is

\[
O\!\left(I\{mP(D+1)+P(D+1)^2\}\right),
\quad P=(L-1)n^2+n(d+1),
\tag{12}
\]

plus separately charged activation evaluation, quadrature construction,
source projection, selection, and assembly. Formula (12) becomes near quadratic
in \(n\) if both \(I,D\) are polylogarithmic, but no such convergence
theorem has been established here. It also performs the full dense path solve
excluded above. A full Newton factorization instead has a generic cubic cost
in \(P(D+1)\); numerical stability of the continuous flow does not make
that factorization free.

## Claim status and remaining bottleneck

The deterministic endpoint estimates (3)--(6) and defect lemma (7)--(10) have
complete derivations in this note, conditional on the stated inherited source
event. They retain the full original label cap and activation class. This is
an author-derived candidate, not an independently checked or promoted result.

The proposed global ODE coefficient route is incomplete as an algorithm and,
when interpreted as a dense solve through the full horizon, excluded by the
clarified task. The general existence of a permissible polynomial or near
quadratic initialization algorithm remains open. The decisive missing bridge
is a construction of the source coefficients with controlled error and cost
that avoids dense full-path reconstruction; stability alone does not supply
that information.

## Post-freeze assessment: lifting a compressed warmup trajectory

The preceding route was frozen before the supervisor supplied a further
candidate: evolve short-window Harmonic models, retain the initialized dense
mixers and transient source bases, lift only compressed increments, regenerate
local source jets at window boundaries, and finally assemble one model at the
original initialization. The following analysis concerns that supplied idea;
it is not an independent rediscovery. The complete source-metric selection
section of `RESULT.md` was additionally read for this assessment.

There is a useful exact bridge: the existing comparison does control a lift of
the full parameter state, even though its displayed conclusion emphasizes
prediction. Let \(U_j^TU_j/n=I\), \(P_j=(U_j)_{I_j}\), and
\(P_j^TM_jP_j=I\) be the actual source basis, selected restriction,
and metric. Define linear maps

\[
\mathcal L_j=U_jP_j^TM_j:\mathbb R^{q_j}\longrightarrow\mathbb R^n,
\qquad
\mathcal L_j^*=P_jU_j^T/n:\mathbb R^n\longrightarrow\mathbb R^{q_j}.
\tag{13}
\]

The adjoint in (13) uses the ordinary selected metric and the dense normalized
pairing \(u^Tv/n\). The map \(\mathcal L_j\) is a contraction:
\(P_jP_j^TM_j\) is the selected-space orthogonal projection onto
\(\operatorname{ran}P_j\), and

\[
\frac{\|\mathcal L_j z\|_2^2}{n}
=\|P_j^TM_jz\|_2^2\le\|z\|_{M_j}^2.
\]

It exactly recovers source vectors: \(\mathcal L_jp_{I_j}=p\) for
\(p\in E_j\). If \(\|u-p\|_\infty\le\eta\) for such a
vector, the diagonal mass bound of the selector gives

\[
\frac{\|u-\mathcal L_ju_{I_j}\|_2}{\sqrt n}
\le\frac{\|u-p\|_2}{\sqrt n}
 +\|(u-p)_{I_j}\|_{M_j}\le3\eta.
\tag{14}
\]

Define the lifted compressed parameters on a source interval beginning at the
original initialization by

\[
\widetilde A=A_0+\mathcal L_1(A_C-A_C(0)),\qquad
\widetilde w=\mathcal L_Lw_C,
\]
\[
\widetilde W^{(j)}=W_0^{(j)}+
\mathcal L_j(B_C^{(j)}-B_C^{(j)}(0))\mathcal L_{j-1}^*.
\tag{15}
\]

Only the raw compressed readout is lifted in this formula. Its error is
controlled by the existing cancellation variables because
\(w_C-w_R=\zeta-p\), hence \(\|w_C-w_R\|_{M_L}\le b_e\).
The effective corrected readout remains the actual compressed predictor.

Let \(a_h,b_e\) be the comparison quantities in `RESULT.md`, and write
\(E_C=a_h+b_e\). Let \(H_{j-1}^{\rm src},\tau_j^{\rm src}\)
be the source RMS coefficients, so that dense feature and response RMS bounds
are \(H_{j-1}^{\rm src}\) and \(S\tau_j^{\rm src}\). Then

\[
\|\widetilde\theta(t)-\theta(t)\|_2
\le E_C(t)+12(Y/\lambda)\eta
 \left[2+\sum_{j=2}^L
   (S\tau_j^{\rm src}+H_{j-1}^{\rm src}+3\eta)^2\right]^{1/2},
\tag{16}
\]

where \(\widetilde\theta\) uses the normalized parameter coordinates
of (1). This applies uniformly throughout the interval on which the existing
source approximation and Harmonic comparison hold.

To prove (16), first lift the proof reference \((A_R,B_R,w_R)\) from
`RESULT.md` instead of the compressed parameters. The resulting differences
from (15) have normalized parameter norm at most \(a_h+b_e\): (13)
is a contraction on vectors and on the left/right Hilbert--Schmidt matrix
factors. For example, writing \(U_j/\sqrt n\) as an ordinary
orthonormal matrix shows directly that
\(\|\mathcal L_jB\mathcal L_{j-1}^*\|_F\) is at most the selected
Hilbert--Schmidt norm of \(B\).

The first-weight projection error has zero initial value because all columns
of \(A_0\) are source members. Its derivative is the sample sum of
\(2c_a/m\) times the response error in (14), tensored with \(v_a\).
Its integrated normalized Frobenius norm is at most
\(6\eta\int\rho\le12(Y/\lambda)\eta\). The readout error has
the same bound, using the top-feature source and zero initial readout.

For a hidden matrix, the dense rank-one update and lifted reference update
differ by

\[
\delta_a^{(j)}\frac{h_a^{(j-1)T}}n-
(\mathcal L_j\delta_{a,I_j}^{(j)})
     \frac{(\mathcal L_{j-1}h_{a,I_{j-1}}^{(j-1)})^T}{n}.
\]

Its Frobenius norm is at most
\(3\eta(S\tau_j^{\rm src}+H_{j-1}^{\rm src})+9\eta^2\),
by adding and subtracting one mixed outer product and using (14).
Multiplication by \(2|c_a|/m\), summation over samples, and integration
give \(12(Y/\lambda)\eta
(S\tau_j^{\rm src}+H_{j-1}^{\rm src}+3\eta)\).
The Euclidean sum of these block bounds proves (16).

Thus full-state reconstruction is controlled by (16), even though the existing
theorem emphasizes prediction. Inserting the existing scalar bound

\[
E_C(t)\le\eta(1+\lambda^{-1/2})(e^{\mathcal B_n}-1)
\]

retains subpolynomial width amplification. The increment representation in
(15) has rank at most the transient selected widths, while preserving the
original initialized mixers.

This bridge does not complete the proposed sequence of windows. Three further
scientific obligations remain:

- A restart has nonzero readout and nonzero residual, and generally a learned
  mixer. Exact initialization should add the current readout to the source
  space and preserve its feature pairings. The original zero-readout fitting
  statement does not by itself supply this restarted theorem.
- Local source jets computed at a lifted approximate anchor describe the dense
  ODE from that anchor. A quantitative complex stability/continuation argument
  must show that its source domain and coefficient bounds remain comparable
  to those of the true trajectory. The real defect lemma above does not prove
  complex holomorphy of those approximate-anchor trajectories. A sufficiently
  small real discrepancy alone is not a proof of that analytic bridge.
- Accumulated lifting/restart error, spatial projection, final temporal
  reconstruction and the numerical solution of every compact transient flow
  need a single error budget and complete arithmetic cost. The final source
  rank must match the requested retained budget; retaining the union of all
  local source spaces without reapproximation may change it.

There is also a separate scope objection. If order-\(K\) **dense ODE jets**
are regenerated at every anchor over all \(O(T/r_t)\) windows, those jets
already contain the information needed to advance a high-order dense
continuation solver through the complete training horizon. They require its
dense matrix actions, and the passive source queries add work. Evolving a
compact state between those anchors does not by itself demonstrate that the
expensive full-horizon dense computation has been avoided. Under the clarified
exclusion, the candidate must avoid dense-jet regeneration through most of the
horizon, or otherwise establish the requested substantial reduction in dense
training work. Formula (16) removes one mathematical obstacle; it does not
remove this computational/provenance obligation.
