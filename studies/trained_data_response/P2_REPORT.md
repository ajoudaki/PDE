# P2 nonlinear trained-law continuation: current resolution and exact gap

Coordinator: task 01a09106-41c4-7193-9db9-8068144fd825, /root.
Checkpoint date: 2026-09-11. This report predates the full author candidate
in [P2_THEOREM.md](P2_THEOREM.md) and the new H proof in
[P2_SOURCE_BOOTSTRAP.md](P2_SOURCE_BOOTSTRAP.md). Those frozen inputs
are undergoing the required full reviews. The following preserves the
earlier exact gap and evidence rather than silently rewriting its history.
**At this checkpoint the requested A–C theorem remained open.**
There is no complete proof, neural counterexample, or promotion claim.
This report records the strongest retained conclusions and one precise
sufficient missing lemma. It does not replace that lemma by an assumption
and call the original task complete.

## 1. Unchanged target and scientific inputs

The exact target is [P2_CONTRACT.md](P2_CONTRACT.md): two equal-width tanh
hidden layers, no biases, stored Gaussian variances (1,1/n,1/n²),
mobilities (n,1,n), exact unhalved squared-loss integrals, physical time
T=40, and all Borel laws on
\(Z=\sqrt2 S^1\times[-Y,Y]\), \(Y\ge1\), with
\[
d_Z((x,y),(x',y'))=|x-x'|/\sqrt2+|y-y'|.
\]
All references below use \(u=x/\sqrt2\), so the data diameter is at most
\(D_Y=2+2Y\). The reference has masses 1/2 at \((e_1,+1)\) and
\((e_2,-1)\) in normalized coordinates.

The canonical population state is
\[
\theta=(w,K,c)\in L^2(\Omega_1;\mathbb R^2)
\oplus\mathcal S_2(H_1,H_2)\oplus H_2,\qquad A=A_0+K.
\]
The actual initialized Gaussian action \(A_0\), its actual Hilbert adjoint,
and the full Gaussian first row are retained. Only K is Hilbert–Schmidt.
The population initial readout is zero; every finite comparison retains
the actual stored readout \(c_n=W^3_n\), of entry variance \(n^{-2}\).
The raw norm is the requested square-sum norm. Its equivalent sum norm is
used in comparison inequalities. Finite counterparts are first-row
Frobenius/\(\sqrt n\), ordinary middle Frobenius, and readout
Euclidean/\(\sqrt n\).

P1's frozen package verifies and is now incorporated, byte-for-byte, as
established C.4.6. Its old unpromoted status is superseded. Its proof
bodies, not review verdicts, are inputs. Complete scientific reading and
hash/command evidence are in [P2_RUN_RECORD.md](P2_RUN_RECORD.md).
No other study, historical campaign, or concurrent P2 argument was used.

## 2. Unconditional conclusions retained

The following arguments are fully persisted; their scope is narrower
than A–C.

1. **Actual finite GF exists globally for every fixed Borel law.**
   Differentiating the exact loss integral in finite parameter dimension
   is valid on compact parameter sets. Its raw gradient energy identity
   gives finite-length continuation and width-independent raw bounds
   through 40 on a Gaussian initialization event of probability tending
   to one. The readout has a uniform coordinate bound. See
   [P2_REFERENCE_COMPARISON.md](P2_REFERENCE_COMPARISON.md), §1.

2. **An existing strong population trajectory has energy and a strong
   raw endpoint.** This does not prove that a trajectory starts from
   that endpoint. The learned transpose contribution has a coordinate
   bound
   \[
   \|K(t)^*\delta(t,u)\|_\infty\le\tfrac43Y^3t^2,
   \qquad \delta=c\phi'(AH^1(u)).
   \]
   The raw Euler counterpart follows by the same finite rank sum.
   See [P2_CONTINUATION.md](P2_CONTINUATION.md), §2.

3. **The C.4.1 transport inequality holds in the full raw HS metric.**
   All middle velocity terms are ranks, whose operator and HS estimates
   use the same product of vector norms; action differences are bounded
   by the HS increment norm. No cross-carrier subtraction is made.
   Combined with the actual finite reference tails, it identifies
   actual finite flows for every sequence of laws tending to \(\nu_*\),
   with reference-only modulus
   \[
   \Phi_Y(q)=C_Yq\exp\{C_Y\sqrt{\log(e/q)}\}\longrightarrow0.
   \]
   The probability statement at a fixed q is a vanishing positive excess
   over this bound. See P2_REFERENCE_COMPARISON, §§2–3.

4. **Tanh saturation controls the full row's radial growth.** Since
   \(|z|\phi'(z)\le1/2\),
   \[
   \frac{d}{dt}|w_i|^2
   \le2\int |r(u,y)Q_i(u)|\,d\mu,\qquad Q=A^*\delta.
   \]
   The raw energy bounds then give actual finite, law-uniform fourth
   moments of \(\sup_{t\le40}|w_i(t)|\), averaged over neurons, on the
   initialization event. They do not give inverse-gate or Q exponential
   tails. See [P2_REACHED_TAILS.md](P2_REACHED_TAILS.md), §3.
   An independent supplied-state algebra check covers the identity,
   unhalved gradient metric, nonzero readout, and correlated/repeated
   inputs. It is not a training experiment.

5. **The P1 contamination-response family is relatively compact in
   continuous clock/HS/readout curves.** Its atom-forcing map is strongly
   continuous on a compact time/input/label set. Probability integration
   and the bounded linear response map preserve relative compactness.
   Strong Taylor estimates therefore hold uniformly on these compact
   directions; no ambient \(L^2\) Fréchet claim follows. See
   [P2_RESPONSE_BRIDGE.md](P2_RESPONSE_BRIDGE.md), §§1–2.

The exact observation grammar in P2_REFERENCE_COMPARISON uses raw
fields and identified generated fields, finitely many typed bounded
actions/adjoints, globally Lipschitz coordinate maps, and bounded
continuous gates multiplying named \(L^2\) fields. It retains same-layer
joint laws, second moments, initialized/current action measurements,
and paired initial/current hidden observables. Inverse gates and nonlinear
clocks require their own moment arguments. Arbitrary products of two
unbounded varying \(L^2\) fields are not admitted.

## 3. One sufficient unresolved lemma

Let \(U_r=\{\lambda:W_1(\lambda,\nu_*)<r\}\), and set
\(\tau_R(V)=\|V1_{\{|V|>R\}}\|_2\).
Every separately fixed finite-law raw population Euler graph from
\((g,0,0)\) exists by direct recursion on the canonical carrier. Write
\(\theta_{\lambda,k}^{h}\) for its nodes and
\(Q_{\lambda,k}^{h}(u)=(A_{\lambda,k}^{h})^*
\{c_{\lambda,k}^{h}\phi'(A_{\lambda,k}^{h}H^1_{\lambda,k}(u))\}\).

**Missing lemma H.** There exists \(\rho>0\) such that, for every
\(0<r<\rho\), there are \(a_r,M_r,h_r>0\) with
\[
\tau_R(c_{\lambda,k}^{h})
+\int_Z\tau_R(Q_{\lambda,k}^{h}(u))\,d\lambda(u,y)
\le M_r e^{-a_rR},\qquad R\ge1,
\tag{H}
\]
for every finitely supported probability law \(\lambda\in U_r\), every
raw Euler mesh of maximum step at most \(h_r\) through T=40, and every
node. Constants may depend on r,Y and the fixed model/horizon, but not
on mesh length, atom count, atom weights, Gram rank, or angles.
The readout term already vanishes beyond a uniform coordinate bound.
The substantive obligation is the adapted initial query
\(A_0^*\delta\); adding \(K^*\delta\) only changes tail constants.

H is a sufficient hypothesis, not a necessary condition for the neural
target. Failure to prove H, or even a future refutation of this particular
raw-Euler contract, would leave alternative constructions available.

The complete conditional arguments are in
[P2_CONTINUATION.md](P2_CONTINUATION.md),
[P2_COMBINED_TAIL_CONTRACT.md](P2_COMBINED_TAIL_CONTRACT.md),
[P2_VARIATION.md](P2_VARIATION.md), and P2_RESPONSE_BRIDGE.
Their dependency chain is:

- H and the one-reference raw comparison give the scalar inequality
  \(s'\le Ls\log(e/s)\). Thus
  \(s(t)\le e^{1-e^{-Lt}}s(0)^{e^{-Lt}}\), including zero-initial-error
  uniqueness. Raw Euler refinements and finite-law approximations are
  Cauchy, with a quantitative Hölder modulus on each smaller ball.
- The limit is a strong \(C^1\) raw solution of the autonomous integral
  equation. Its tails are inherited from H, and only this constructed
  path needs the tails when compared to any competing strong solution.
  Restriction to \([s,40]\) gives unique restart from each reached state
  with the same law and retained primitives. No arbitrary ambient-state
  well-posedness or continuation beyond 40 is asserted.
- Fixed-program oracles identify the finite dynamics. Choose a finite
  time partition, then finitely many cutoffs and error tolerances
  backwards, then one sufficiently close finite law and one sufficiently
  fine mesh, then let width and the target empirical law converge.
  Each transcript is fixed before its width limit. This gives state and
  observation identification and whole-circle capture without a relative
  sample/width rate.
- Adding a probe atom of mass \(\eta\) at any passive u and using
  same-mesh Hölder law continuity gives
  \[
  \tau_R(Q_\lambda(u))
  \le C\eta^\alpha+C\eta^{-1}e^{-aR/2}.
  \]
  Choosing \(\eta\) exponentially small in R yields uniform passive
  exponential marginal tails on a smaller ball.
- The radial identity and Jensen over time and the data law give
  \[
  \sup_\mu\mathbb E\exp\{\gamma\sup_{t\le40}|w_\mu(t)|^2\}<\infty.
  \]
  No coordinate supremum of Q is used. Hölder then supplies every fixed
  finite moment of the inverse-gate forcing
  \(u_j\cosh^2(w_j)\phi'(w\cdot u)Q(u)\), including uniform integrability
  of its square.
- In the absolute coordinate clock
  \(X_j=F(w_j)\), \(F(z)=z/2+\sinh(2z)/4\), the reference-law field is
  Lipschitz when one compared readout is uniformly bounded.
  Decompose the perturbed field as reference field plus contamination
  forcing. The preceding uniform integrability makes the latter
  continuous along reached paths. Compact P1 response directions supply
  uniform Taylor consistency. Comparison with the linear response curve
  gives the uniform \(o(\epsilon)\) raw and prediction remainder.
  Subtracting the fixed \(F(g_j)\) identifies this clock and its tangent
  with P1 exactly.

For a final ball choose any \(0<r_0<r_1<\rho\). Constants from the larger
ball give one modulus on all of \(U_{r_0}\), which can serve as the U_Y
in the task. Set
\(\epsilon_Y=\min(1/2,r_0/(2D_Y))\); the inclusive contamination interval
then lies strictly in that open ball for every contaminating law.

The finite comparison also covers a **fixed arbitrary Borel law**:
in P2_CONTINUATION (17) take every target \(\lambda_j=\mu\) while the
fixed approximating oracle law remains finite. Finite smoothness and the
same-carrier transport inequality use exact Borel integrals, so no
empirical-law premise is needed for this specialization. The identical
ordered argument proves convergence. Independent iid laws converge in
W1 in probability by compact finite partitions; the fixed-oracle
initialization errors and union bounds then give the sampling conclusion.

Finally, for each fixed \(\nu,\epsilon>0\), the exact triangle inequality
in P2_RESPONSE_BRIDGE (5) gives
\[
\frac{\|f_{n,\mu_\epsilon}-f_{n,*}-\epsilon D_\sigma f_n\|_\infty}
{\epsilon}
\le\omega_Y(\epsilon)
+\frac{\|f_{n,\mu_\epsilon}-f_{\mu_\epsilon}\|_\infty
       +\|f_{n,*}-f_*\|_\infty}{\epsilon}
+\|D_\sigma f_n-D_\sigma f\|_\infty .
\]
Take width first at fixed positive epsilon, then epsilon to zero.
This is exactly the requested finite nonlinear limit bridge. It asserts
neither a width-uniform finite-n remainder nor a joint epsilon/width
rate. The exclusion of a “finite-width nonlinear remainder” in the
frozen combined report concerns those stronger claims, not this
conditional double-limit consequence.

## 4. Why the existing estimates do not prove H

A fixed-distance comparison with the reference leaves
\(2\Phi_Y(W_1(\mu,\nu_*))>0\) for two approximations of one changed law.
It cannot make them Cauchy. Likewise, transferring a reference tail
through a fixed \(L^2\) error leaves a positive tail floor.

P1's exact lower clock cancellation uses the reference axes. At a
general u the clock force contains
\[
u_j\frac{\phi'(w\cdot u)}{\phi'(w_j)}Q(u).
\]
In raw coordinates its comparison includes
\[
[\phi'(w\cdot u)-\phi'(\widetilde w\cdot u)]\widetilde Q(u).
\]
Neither is controlled by arbitrary raw \(L^2\) increments. Column removal
controls the cavity's independent Gaussian part, but its learned
response needs a new estimate for this product. A sufficient stronger
cavity statement is isolated in P2_REACHED_TAILS, §7; it is also open.

Each fixed mesh has a compact family of law-dependent Euler states.
There is no demonstrated uniform spatial compactness as the mesh is
refined. Even supplied compactness of backward \(L^2\) fields would give
vanishing tails without an Osgood uniqueness rate; the power-tail
singleton in P2_CONTINUATION §5 exhibits the failed implication.

The unconditional row fourth moment and bounded learned transpose do not
bound the adapted initialized query. Bounded activation derivatives do
not provide an \(L^p\) bound for \(A_0^*\), and treating an adapted query
as a fresh independent Gaussian would change the model.

The finite dimension of each network does not make its nonlinear
remainder uniform in width. Bounded homogeneous response propagation
does not control nonlinear error production. No route failure above
is a counterexample to A–C.

## 5. Immediate risk and hidden-activity interfaces

These are interfaces, not a new universal fitting claim. Under H, the
full raw and prediction capture passes risk and paired hidden activity
to the constructed changed-law population. On a uniform raw ball let
\(|f|\le B\) and let its input Lipschitz constant be L. Then
\[
|R_\mu(f)-R_\mu(g)|\le2(B+Y)\|f-g\|_\infty,\qquad
|R_\mu(f)-R_\rho(f)|
\le2(B+Y)\max(L,1)W_1(\mu,\rho).
\]
The first follows from the difference of two squares; the second
follows by coupling and the joint input/label Lipschitz bound.

For paired activity, the current and initialized features share the
same carrier. Each feature has magnitude at most one, so
\[
\left|\|H-H_0\|_2^2-\|\bar H-H_0\|_2^2\right|
\le4\|H-\bar H\|_2.
\]
Uniform input continuity and the law coupling pass its training average,
including the actual initialized/current pairing.

Consequently, on the **binary-label subclass** and the intersection of
the proposed neighborhood with the established C.4.5 ball
\(W_1(\mu,\nu_*)<\exp\{-\exp(3000)\}\), C.4.5's finite-GF comparison
and its strict margins imply for the conditionally constructed population
risk at time 40 at most 1/4 and both averaged paired squared hidden
displacements at time 1/200 at least \(10^{-13}\). The finite-GF case
uses the same reference comparison in C.4.5.3 with zero discretization
defect. These finite guarantees already hold on that exact admitted
subclass; the new conditional conclusion is their identification with
an actual changed-law population trajectory through 40.

This does not claim hidden activity at time 40, activity for every law,
fitting of arbitrary bounded-label laws, a changed-law endpoint, or a
feature-learning advantage. C.4.4's different equal-label activity
family is not substituted for this opposite-label subclass.

## 6. Checks, review limits, and remaining work

The original three independent reports were frozen before comparison.
The variation theorem received a fresh isolated adversarial check:
[P2_VARIATION_AUDIT.md](P2_VARIATION_AUDIT.md). Its acceptance is
conditional on strong solutions and its stated uniform-integrability
hypothesis, not on their being established for this neural model.

A scoped collaborator checked the two root lemmas:
[P2_ROOT_LEMMAS_CHECK.md](P2_ROOT_LEMMAS_CHECK.md). The residual factor,
normalized metric, continuous-gate contract and exact starting-field
scope have been corrected in the root files. Its original report and
input hashes are preserved.

The fresh isolated [combined audit](P2_COMBINED_AUDIT.md) found the full
H-implies-A–C reduction valid, including fixed Borel-law capture and the
width-first finite nonlinear bridge. Its complete neutral assignment is
[P2_COMBINED_AUDIT_ASSIGNMENT.md](P2_COMBINED_AUDIT_ASSIGNMENT.md).
This validates an implication with an open premise; it is not either of
the user's two unconditional success reviews.

The fresh [bounded-feature attempt](P2_TAIL_ALTERNATIVE.md) additionally
exhibits a stationary controlled row with arbitrarily fast positive
linearized expansion for three correlated directions. It rules out an
estimate of the isolated row-curvature term from row speed, radial
growth, or bounded features alone. It also proves that one smooth common
coordinate change cannot flatten the noncommuting correlated tanh row
fields. These are precise proof-route obstructions, not reachable neural
counterexamples. Root read and checked the entire 566-line report.
The remaining source-response attempt is checking a different possible
uniform coefficient bound; no such bound is currently established.

The exact remaining mathematical action is to prove H (or replace it
by a different complete reached-trajectory construction), then freeze
an unconditional A–C theorem with full dependencies and obtain two fresh
complete isolated adversarial reviews. No established addition is
currently proposed. Deterministic algebra and standalone dependency
validation pass; they do not test or certify H.
