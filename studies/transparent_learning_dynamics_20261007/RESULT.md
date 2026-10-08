# Learning as evolving response geometry and coactivation

2026-10-07. Current synthesis of a new research direction. This is not a
revision or promotion of the compression study.

## Current diagnostic: independently integrated averages change the mismatch

[Fresh-quadrature self-consistency audit](FROZEN_QUADRATURE_RESULT.md) holds
the three recorded causal coefficient histories fixed and re-evaluates their
local circuits on 32,768 fresh Gaussian samples each. It is a diagnostic,
**not a new autonomous solver or an improved coupled-model accuracy result**.

The lower-layer dense-comparison errors nominally decrease from 27–31% to
12–15%; the measured fresh-minus-original similarity changes are 23–27% of
dense movement. This supports finite-particle integration as a contributor
to the mismatch. But the predeclared lower-layer fresh-resolution gates fail,
so the registered explanation criterion does not pass. Upper-layer effects
are mixed; passive similarity-change error slightly worsens.

This strengthens the distinction between feature-movement size and pairwise
associations without attributing a new physical mechanism to numerical
error. Recorded memory and reciprocal responses remain untouched. Four
prescribed replays completed, one repeated every non-timing array exactly,
and an independent saved-array audit confirmed the statistics. The coupled
system's accuracy remains the previous result below; global proofs and
two-input cubic refinement remain paused.

## Current coupled-model result: stable 16-input tests still miss lower-layer accuracy

The latest bounded continuation is
[Stable steps are not yet accurate trajectories](RESIDUAL_FILTER_RESULT.md).
It keeps the causal feature–response mechanism and replaces the unstable
Euler step by a consistent residual-filtered step, tested against a refined
dense RK4 reference. Its 24 prescribed runs and independent saved-array audit
are complete; global proofs remain paused.

- The dense reference now passes the checked step-halving test, with hidden
  similarity differences between meshes below \(10^{-8}\). All new dense and causal runs have
  nonincreasing saved loss, without a claim of unconditional nonlinear stability.
- At 16 training inputs and four passive inputs, same-filtered-mesh
  ensemble-mean similarity-change errors are 27–31% in layer 1 and 12–17%
  in layer 2. The lower layer **misses** the predeclared 20% accuracy target.
  Comparisons against refined dense RK4 give 29–32% and 15–19%, respectively.
- Matching training loss does not remove the lower-layer discrepancy.
  Individual-feature displacement can be close while sample associations
  differ: fitting and movement size do not validate the relational state.
- Particle-count changes are as large as the measured mean discrepancies,
  and causal step refinement still fails all four numerical gates. These
  results do not yet identify a faulty causal term or establish continuum
  accuracy. One fresh run reproduces every saved array exactly.

No response channel is removed, and no additional two-input approximation is
pursued. This supersedes the failed 16-input dense-reference status below,
but does not retroactively validate the earlier Euler cohort or its ablations.

## Previous result: 4–16 interacting training inputs

The preceding bounded phase is
[Feature learning with 4–16 interacting training inputs](MULTISAMPLE_TRAJECTORY_RESULT.md).
It keeps the causal equations unchanged and compares both hidden layers'
training–training and training–passive similarities at all 49 saved times,
using four passive inputs, nonorthogonal geometry and varied mixed-sign labels.
The phase completed 30 dense and 22 causal trajectories; no global proof or
two-input cubic refinement was attempted.

- At 4 and 8 training inputs, ensemble-mean feature-change errors are
  3.6–11.8% of the dense change in maximum-time block RMS. This is
  resolution-limited **same-Euler-mesh** agreement, not a continuous-flow
  guarantee. The independent dense RK4 references pass refinement checks.
- The 16-input test does **not** pass: errors are 57–67% and the prescribed
  meshes are strongly time-step sensitive. Even its RK4 reference fails
  full-horizon refinement. A broad variability envelope is not counted as
  evidence of accuracy in this case.
- The initialized feature direction predicts early geometry, but it turns
  later; a frozen-direction continuation is insufficient. Learned middle
  memory redistributes feature motion between layers. Removing reciprocal
  return can increase individual lower-feature motion while weakening
  off-diagonal sample associations, even though labels still fit.
- The full-horizon affine-activation control is numerically unresolved.
  A narrower early fitting-stage contrast survives the available refinements;
  it does not resolve its late dynamics or isolate a pure gate contribution.

The report separates predeclared predictions, exact identities, observed
mechanisms, numerical failures and missing guarantees, with full blockwise
tables and time-resolved error curves. Its numerical-integration follow-up is
the current result above. Global proofs remain paused.

## Earlier result: learning beyond initialization

The preceding continuation is
[Beyond one clock: ordered learning and passive nonlinear geometry](UNEQUAL_RESIDUALS_RESULT.md).
It tests unequal labels and correlated inputs, retains the full causal
system, and rejects the attempted cubic passive simplification at moderate
labels. An exact same-trajectory decomposition now separates readout,
middle-write and propagated lower-feature contributions to passive
nonadditivity. The controls show why a small endpoint ablation effect can
hide a substantial contribution: another layer compensates. Sample-order
memory affects two-time response even when it cancels from leading same-time
training Grams. Numerical step errors and finite-ensemble uncertainty remain
explicit; no global guarantee is asserted.

Global-proof work is paused at the user's request. The new
[analytical and numerical report](BEYOND_INITIALIZATION_RESULT.md) follows the
existing two-hidden-layer tanh system through fitting, with a passive input.

- The full causal history solver agrees with matched dense Euler ensembles
  within the measured sampling/refinement resolution in this bounded example.
- Removing reciprocal feedback still fits the labels but substantially
  changes both hidden similarities and passive prediction. Freezing learned
  middle memory instead shifts more feature movement to the first layer.
- A one-state, initialization-derived cubic residual clock explains both
  training cross-feature curves to within 3.4% of their final mean change on
  the tested grids, without fitting trajectory coefficients.
- That simplification does **not** fully close passive behavior: its passive
  cubic misses about 13% at the larger opposite-label amplitude. The full
  passive feature–response state is retained rather than discarded.

The detailed report separates exact identities, perturbative coefficients,
empirical evidence and missing guarantees. The tested amplitudes are not
certified against the original conservative small-label cap; neither a
general all-time theorem nor arbitrary-data validation follows.

## Current candidate and nonlinear mechanism

The user-requested next deliverable is
[Causal feature--response dynamics](CANDIDATE_SYSTEM.md). It specifies one
closed autonomous **history-state population system**: representative
forward/backward field laws, their joint first local sensitivities, and
the two-time similarities obtained from those laws. No learned inter-neuron
matrix or future dense trajectory is supplied.

For two hidden tanh layers, two orthogonal training inputs develop a
nonzero initial cross-feature acceleration whose sign is the product of
their labels. The equations identify the actual write: the other sample's
feature enters through the shared backward return and is filtered by
squared activation sensitivity. The same calculation shows how an unlabeled
passive input changes representation. Both hidden layers are included;
the middle-matrix contribution is separated from first-layer feature motion.
See the [closure check](CANDIDATE_CLOSURE_CHECK.md) and
[nonlinear example check](TWO_LAYER_MECHANISM_CHECK.md).

The rigorous constructed object is the finite chronological system; its
history and Gaussian integration dimension grow with the number of steps.
It is not a small finite-dimensional Markov ODE. Continuous loss decay is
an exact identity of the compatible gradient flow, not a claim for an
arbitrarily large Euler step. The full-trajectory dense-variability guarantee
and a general explicit continuous-response-kernel theorem remain open.
The latest user request pauses that quantitative proof project. The current
priority is understanding this same system beyond initialization through
analytical approximations and controlled numerical experiments, including
passive inputs. The experiment contract is recorded in README.md. Numerical
agreement, if obtained, will not be promoted into a global theorem.

## Current research checkpoint

The requested all-time explanatory closure is **not yet established**.
The exact geometric theorem below remains valid, but its transfer information
is too complete to count by itself as the desired observable reduction.

The following internally checked advances now go beyond that representation:

- A typical-initialization obstruction shows that even the full Gram of
  features, derivative features and their mixtures can miss an actual
  prediction fluctuation of order \(n^{-1/2}\), at one fixed positive time.
  This is stronger than the earlier support-only counterexample. It concerns
  the specified one-layer sine model and that information class, not all
  conceivable aggregate states.
- An explicit causal Gaussian history law now describes the actual deep
  finite-step neural computation at root-width accuracy up to logarithms.
  It retains forward/backward response memory and requires neither invertible
  full histories nor clipping of unbounded activations. For each fixed
  \(Q\)-instruction computation and every fixed \(r>0\), its output and
  pairing errors are at most
  \(C_r n^{-1/2}[\log(en)]^{2Q+2}\), except with probability
  \(C_r n^{-r}\), at sufficiently large width. The constants depend on the
  fixed program and its positive retained-history gaps. This is not uniform
  in time discretization or over the full training horizon.
- The Gaussian query law can be written entirely using feature/response
  covariances and expected directed derivatives, with no inverse Gram in
  its formulation. This equivalence includes singular histories. It does
  not yet remove history-gap constants from the quantitative proof.
- Compatible finite laws now have a unique global continuous Hilbert-flow
  limit, and qualitative all-time prediction convergence, **conditional
  on explicitly stated finite-width operator, carrier and fitting-tail
  bounds**. These upstream bounds are not re-proved by this study's
  internal check. The theorem supplies no root-width rate.

The new mechanism separates **learned association memory** from **reciprocal
initial-response memory**. The first is the familiar residual-weighted
forward/backward write; the second is the cross-direction correction created
when the same initialized Gaussian map is used forward and backward. Treating
the latter as fresh independent noise gives the wrong feature dynamics.
The exact formulas, finite-step law, and information accounting are in
[Finite response memory](FINITE_RESPONSE_MEMORY.md). The unclipped
identification theorem is in
[Actual neural finite-history laws](UNCLIPPED_FINITE_HISTORY.md), and the
stronger obstruction is in
[Fixed-time Gram-information obstruction](TYPICAL_GRAM_FIXED_TIME.md).

The quantitative refinement is in
[Fixed-history width rate](FIXED_HISTORY_RATE.md), with its
[scoped internal check](FIXED_HISTORY_RATE_AUDIT.md). The inverse-Gram-free
[response formulation](RESPONSE_GAUSSIAN_CLOSURE.md) and its
[finite-program check](RESPONSE_GAUSSIAN_AUDIT.md) are complete.
The [continuous transfer theorem](CONTINUOUS_RESPONSE_LIMIT.md) has its own
[conditional check](CONTINUOUS_RESPONSE_AUDIT.md). Neither is silently
substituted for the missing all-time, finite-memory, dense-variability
approximation theorem.
The polar construction below is therefore an exact available representation,
not a superseded false result and not a declaration that this research
question is solved.

The [explicit neural kernel circuit](CAUSAL_KERNEL_DYNAMICS.md) now displays
the learned association, reciprocal feedback, and same-time curvature
responses together. In particular, instantaneous backward susceptibility
equals local carrier-weighted activation curvature plus the higher layer's
susceptibility transmitted through squared activation sensitivity.
This specialization is a lead derivation awaiting its own scoped check.

## Headline and claim boundary

There is an exact, autonomous geometric realization of the Harmonic runtime
whose moving objects are response Gram matrices, coactivation tensors, a
readout response and training deficits. It works for arbitrary rectangular or
singular layer maps. Its predictions equal those of that runtime, so it adds
no error, failure probability, width requirement, label restriction or training
horizon restriction to a valid certificate for that runtime.

The substantive mechanism is more specific than “the kernel evolves.” Each
training deficit writes an association between a forward feature and a backward
response. Symmetric and antisymmetric parts of these writes respectively enter
response-metric deformation and relative rotation. The latter rotates the
alignment between propagated responses and the nonlinear coactivation law.
The exact decomposition includes the moving-frame terms; it is not an informal
claim that only symmetric writes can change a Gram matrix.

At layer widths at most \(q\), the full geometric state uses
\(O(L(d+Lq)^3+m)\) real scalars, with fixed geometric data of the same order.
Thus polynomial overhead in a polylogarithmic Harmonic width remains
polylogarithmic in dense width. This is an explanatory representation, not
a faster implementation or a further compression theorem.

There is an important unresolved distinction. This construction does not
discard the relevant information in the compressed layer maps. Its response
Grams can encode those maps, and its coactivation tensors encode nonlinear
orientation. The new equations reveal an exact mechanism, but exact conjugacy
alone does not establish the much stronger scientific claim that a small set
of sample similarities is a sufficient explanation of feature learning. That
stronger goal remains open. It would be incorrect to call a renamed matrix or
a redundant Gram lift a completed solution to it.

## 1. Setup and inherited scope

The dense width is \(n\); there are \(m\) labeled inputs in \(\mathbb R^d\)
with \(\|x_a\|=\sqrt d\), \(L\) hidden layers, and compressed layer widths
\(q_\ell\le q\). Write \(v_a=x_a/\sqrt d\), so \(\|v_a\|=1\). Additional inputs may be
declared for validation, without their labels. Every driving sum below ranges
only over \(a=1,\ldots,m\). The training labels are \(y_a\), predictions
are \(f_a\), and deficits are \(c_a=y_a-f_a\).

The imported scope is the current Harmonic construction: arbitrary fixed
depth, the same strip-analytic activation class, possibly unbounded activation
values, the same positive initial feature-Gram gap, Gaussian dense
initialization, zero initial readout, and its existing label and sufficient-width
conditions. None of these conditions is sharpened or weakened here. Activations
may differ by layer; a layer subscript on \(\phi\) is understood below.

The source is the user-invoked integrated result, specifically its supplied
Harmonic optimizer and comparison certificate. Its proof-completion work is
owned by another task. This study has checked the new exact transformations,
not independently re-audited that entire probability/comparison theorem.
An inherited theorem and a new algebraic theorem must not be conflated.

For full-sphere predictions, use the entire input space \(\mathbb R^d\).
For just the declared panel, its span can replace that space. Both choices
are made at initialization; neither requires validation labels or training
observations from the future.

## 2. What ordinary similarities lose

Even at zero readout, the first nonlinear feature-learning response needs more
than the activation Gram. With one hidden layer, put
\(h_a=\phi(z_a)\) and \(p_a=\phi'(z_a)\) at initialization. A necessary
next object is

\[
\frac1n\sum_i h_{b,i}h_{c,i}p_{a,i}p_{d,i}
=\frac1n\langle p_a\odot h_b,p_d\odot h_c\rangle.
\tag{1}
\]

This is a Gram matrix of **features restricted by activation sensitivity**.
It tells us whether two features occupy the same responsive coordinates, not
merely whether their signed inner product is large.

The complete calculation and a counterexample are in
[Observable geometry, Sections 3–4](OBSERVABLE_GEOMETRY.md). In that example,
sine activation, two orthogonal inputs and arbitrarily small opposite labels
give two initial configurations with the same positive feature Gram, all
pairings among preactivations, activations, readout and initial velocities,
and the same first two prediction derivatives. Their third prediction
derivatives differ because (1) differs. The configurations are in Gaussian
support, not asserted to be typical draws. This refutes universal exact
closure of that specified Gram state; it does not prove a probabilistic
impossibility at the dense-variability scale.

A second obstruction is temporal rather than spatial. Sample-induced vector
fields generally do not commute. The exact memory identities and cubic
calculation in [Response memory](RESPONSE_MEMORY.md) show that applying two
sample forces in opposite orders can change predictions, even with the same
total forces and a positive initial feature Gram. This is an open-loop
controlled-path statement, not an impossibility theorem for fixed-label
feedback. It explains why simply replacing the trajectory by accumulated
residuals loses information.

These two findings motivate retaining **coactivation geometry and directed
response interactions**, not merely one evolving similarity matrix.

## 3. The precise source dynamics

This section fixes the optimizer being represented. At layer \(\ell\),
let \(M_\ell\) be the Harmonic construction's fixed SPD metric, and put
\(M_0=I_d\), \(B_1=A\). For \(\ell\ge2\), \(B_\ell\) is its
hidden map. Inner products use the appropriate \(M_\ell\), and
\(B_\ell^*=M_{\ell-1}^{-1}B_\ell^\top M_\ell\).

The forward fields and corrected readout are

\[
h_a^{(0)}=v_a,\qquad z_a^{(\ell)}=B_\ell h_a^{(\ell-1)},
\qquad h_a^{(\ell)}=\phi(z_a^{(\ell)}),
\]
\[
V=\frac1{\sqrt m}[h_1^{(L)},\ldots,h_m^{(L)}],\qquad
\widehat w=w+V(V^\top M_LV)^{-1}
\left[\frac{y-c}{\sqrt m}-V^\top M_Lw\right],\qquad
f_a=\langle\widehat w,h_a^{(L)}\rangle_{M_L}.
\tag{2}
\]

The stipulated backward responses are

\[
\delta_a^{(L)}=\phi'(z_a^{(L)})\odot\widehat w,\qquad
\delta_a^{(\ell)}=\phi'(z_a^{(\ell)})\odot
B_{\ell+1}^*\delta_a^{(\ell+1)}.
\]

Their update law is

\[
\dot B_\ell=\frac2m\sum_a c_a\delta_a^{(\ell)}
 h_a^{(\ell-1)\top}M_{\ell-1},\qquad
\dot w=\frac2m\sum_a c_a h_a^{(L)},\qquad
\dot c=-\frac2mKc,
\tag{3}
\]
\[
K_{ab}=\langle h_a^{(L)},h_b^{(L)}\rangle_{M_L}
+\sum_{\ell=1}^L
\langle\delta_a^{(\ell)},\delta_b^{(\ell)}\rangle_{M_\ell}
\langle h_a^{(\ell-1)},h_b^{(\ell-1)}\rangle_{M_{\ell-1}}.
\tag{4}
\]

For nondiagonal metrics the coordinate gate need not be self-adjoint.
Equations (2)–(4) are the specified runtime, not a proposed replacement
gradient flow. In particular, (4) must not be called the tangent kernel of
the corrected predictor without a separate calculation. On its original
correction domain \(V^\top M_LV>0\), the identity \(f_a=y_a-c_a\)
holds for training inputs.

## 4. A nonsingular geometric realization

### 4.1 Retain the earlier features, not just the last one

Form the direct sum of the input and hidden feature spaces, of dimension

\[
D=d+\sum_{\ell=1}^Lq_\ell\le d+Lq.
\]

Its metric is block diagonal with blocks \(I_d,M_1,\ldots,M_L\).
Flatten it once by its positive square root. In this section all vectors and
maps are in those orthonormal coordinates. The coordinatewise product becomes
a fixed bilinear product \(\mu_0\), with a unit and block indicator vectors.
For example, if the whitening map is \(Q\), then
\(\mu_0(u,v)=Q[(Q^{-1}u)\odot(Q^{-1}v)]\). This is an exact finite
commutative, associative algebra, not a polynomial approximation to \(\phi\).

Temporarily denote isometric block injections by \(\iota_j\). Replace
each whitened map by

\[
F_\ell=I+\iota_\ell B_\ell\iota_{\ell-1}^\top.
\tag{5}
\]

Here \(B_\ell\) means its whitened representation just in (5). The
off-diagonal term squares to zero, so \(F_\ell^{-1}=I-(F_\ell-I)\).
There is no rank or shape assumption on the original map. Applying this
shear, then activating only block \(\ell\), builds the memory
\((v,h^{(1)},\ldots,h^{(\ell)},0,\ldots,0)\). Earlier features remain
unchanged; unvisited blocks remain zero even when \(\phi(0)\ne0\).

### 4.2 What the geometric state means

Starting with a fixed orthogonal frame \(O_0\) on the full direct sum, take the sequential
positive polar factorizations

\[
F_\ell O_{\ell-1}=O_\ell S_\ell,\qquad
O_\ell^\top O_\ell=I,\qquad
S_\ell>0,\qquad G_\ell=S_\ell^2.
\tag{6}
\]

The stored \(G_\ell\) is a **response Gram**, not the sample feature Gram:

\[
u^\top G_\ell v
=\langle F_\ell O_{\ell-1}u,F_\ell O_{\ell-1}v\rangle.
\tag{7}
\]

It measures how similar the responses to two prescribed feature perturbations
are. The input/source and receiver directions may be chosen from initialized
sample-generated feature/response landmarks, as constructed in
[Relational quotient, Section 3](RELATIONAL_QUOTIENT.md). Using the full
layer spaces is also valid; no proper invariant subspace is assumed.

In frame \(O_\ell\), store the coefficients \(T_{\ell,ijk}\) of

\[
\mu_\ell(u,v)=O_\ell^\top\mu_0(O_\ell u,O_\ell v),\qquad
\mu_\ell(u,v)_i=\sum_{j,k}T_{\ell,ijk}u_jv_k.
\tag{8}
\]

Each coefficient pairs one response direction with the coactivation of two
others. The last two indices are symmetric; the first generally is not.
Calling this a fully symmetric population third moment would be wrong for
the source's nondiagonal metrics.

Store also the algebra unit \(u_\ell\), the indicator \(e_\ell\) of
block \(\ell\), the final readout coordinates \(\rho\), and \(c\).
Multiplication by \(e_\ell\) is the block projection in that frame.
One such indicator per frame suffices: that block becomes the next layer's
source. The frame-zero input indicator and algebra remain fixed.

The moving state is therefore

\[
\bigl(G_\ell,T_\ell,u_\ell,e_\ell\bigr)_{\ell=1}^L,
\qquad \rho,\qquad c.
\tag{9}
\]

The maps \(B_\ell,F_\ell\) and frames \(O_\ell\) are needed for
initialization and proof, not to evaluate the new right-hand side.

## 5. Exact nonlinear evaluation from the state

For a vector \(z\) in the current algebra, multiplication by \(z\) is
the matrix with entries \(\sum_kT_{\ell,ikj}z_k\). For a scalar function
\(\psi\), evaluate its matrix function on this multiplication matrix,
then apply it to the unit \(u_\ell\). Denote the result by
\(\psi_{T_\ell}(z)\).

This rule is exact. In the original coordinates, multiplication is diagonal,
and applying the matrix function to the unit gives the vector of scalar values
\(\psi(z_i)\). Similarity transformation proves the rule in every current
frame. Equivalently, polynomial interpolation on the finitely many distinct
coordinate values proves it without an infinite Taylor expansion. Repeated
values do not cause a mathematical singularity. A stable floating-point
implementation is a separate question.

For a query, let \(x_a^{(0)}\) be its fixed input-block coordinates. The
full forward memory and the current-layer feature are computed by

\[
z_a^{(\ell)}=S_\ell x_a^{(\ell-1)},\qquad
x_a^{(\ell)}=z_a^{(\ell)}+
\mu_\ell\bigl(e_\ell,\phi_{T_\ell}(z_a^{(\ell)})-z_a^{(\ell)}\bigr),
\]
\[
h_a^{(\ell)}=\mu_\ell(e_\ell,x_a^{(\ell)}),\qquad
h_a^{(0)}=x_a^{(0)}.
\tag{10}
\]

Here the \(D\)-dimensional \(h_a^{(\ell)}\) is the original layer
feature, zero-extended and expressed in its polar frame. It is not a new
approximation. Different layers use their own frame, but every within-layer
dot product is the corresponding original metric pairing.

Let \(H\) have the final training features as columns. Then

\[
\widehat\rho=\rho+H(H^\top H)^{-1}(y-c-H^\top\rho),
\qquad f_a=\widehat\rho^\top h_a^{(L)}.
\tag{11}
\]

This is exactly (2); the factors \(\sqrt m\) cancel. Only the final block
enters this correction, not the entire retained forward memory.

For each training input, start a full backward vector at
\(b_a^{(L)}=\widehat\rho\). Downward recursion is

\[
g_a^{(\ell)}=b_a^{(\ell)}+
\mu_\ell\left(e_\ell,
 \mu_\ell\bigl(\phi'_{T_\ell}(z_a^{(\ell)})-u_\ell,b_a^{(\ell)}\bigr)
\right),
\]
\[
d_a^{(\ell)}=\mu_\ell(e_\ell,g_a^{(\ell)}),\qquad
b_a^{(\ell-1)}=S_\ell g_a^{(\ell)}.
\tag{12}
\]

The full \(g\) must be transported. Only its projected part \(d\) is
used for the learning write. Discarding the other blocks too early changes
the lifted backward computation. The prime in (12) means the original scalar
derivative evaluated in the algebra, not an adjoint gate or the Jacobian of
the corrected predictor.

## 6. The autonomous geometric ODE

For each layer compute, rather than store, the current pulse matrix

\[
U_\ell=\frac2m\sum_{a=1}^m
c_a d_a^{(\ell)}h_a^{(\ell-1)\top}.
\tag{13}
\]

Every contribution has the same meaning: **training deficit times receiving
backward response times sending forward feature**. The two factors are in
the adjacent polar frames, as required for a map between them.

Set \(\Omega_0=0\). In increasing layer order, determine the skew matrix
\(\Omega_\ell\) from

\[
(\Omega_\ell-\Omega_{\ell-1})S_\ell
+S_\ell(\Omega_\ell-\Omega_{\ell-1})=U_\ell-U_\ell^\top.
\tag{14}
\]

The solution is unique: in an eigenbasis of \(S_\ell\), divide each
right-hand-side entry by the positive sum of the corresponding two
eigenvalues. There is no eigenvalue-difference denominator and no assumed
nonzero singular value of an original layer map.

The state evolves by

\[
\dot G_\ell=S_\ell U_\ell+U_\ell^\top S_\ell
+G_\ell\Omega_{\ell-1}-\Omega_{\ell-1}G_\ell,
\tag{15}
\]
\[
\dot T_{\ell,ijk}=
-\sum_p(\Omega_\ell)_{ip}T_{\ell,pjk}
+\sum_pT_{\ell,ipk}(\Omega_\ell)_{pj}
+\sum_pT_{\ell,ijp}(\Omega_\ell)_{pk},
\tag{16}
\]
\[
\dot u_\ell=-\Omega_\ell u_\ell,\qquad
\dot e_\ell=-\Omega_\ell e_\ell,\qquad
\dot\rho=\frac2m\sum_a c_a h_a^{(L)}-\Omega_L\rho,
\qquad \dot c=-\frac2mKc,
\tag{17}
\]
\[
K_{ab}=h_a^{(L)\top}h_b^{(L)}
+\sum_{\ell=1}^L
(d_a^{(\ell)\top}d_b^{(\ell)})
(h_a^{(\ell-1)\top}h_b^{(\ell-1)}).
\tag{18}
\]

Equations (9)–(18) are closed. They require current state, input geometry,
labels and the given activation, not original weights, future source values
or a trajectory table. They restart from their retained state. All nonlinear
coactivation orders are evaluated using one finite associative algebra;
differentiating it produces (16), not an unclosed fourth-order hierarchy.

### The precise deformation–rotation split

For this paragraph only, write \(E_\ell=(U_\ell+U_\ell^\top)/2\).
Use \([A,B]=AB-BA\). Equations (14)–(15) imply

\[
\dot G_\ell-
\left[G_\ell,\frac{\Omega_\ell+\Omega_{\ell-1}}2\right]
=S_\ell E_\ell+E_\ell S_\ell.
\tag{19}
\]

To verify it, put \(\Lambda=\Omega_\ell-\Omega_{\ell-1}\) locally.
Equation (14) gives
\([S_\ell,(U_\ell-U_\ell^\top)/2]=[G_\ell,\Lambda]/2\).
Insert the symmetric/skew decomposition of \(U_\ell\) into (15).

The commutator in (19) is an isospectral rotation. Thus the skew pulse
interaction determines relative frame rotation and its associated rotation
of the response metric. In the frame rotating at the average of the two
angular velocities, the symmetric pulse interaction gives the remaining
metric deformation. Symmetric off-diagonal terms can also move principal
directions; “symmetric changes only lengths” would be too strong.

Equation (16) says what rotation matters for learning: it changes the
alignment of response directions with the fixed nonlinear coactivation
operation. The activation function itself is not being learned. With
nondiagonal source metrics this operation is not a symmetric cubic form.

For ordinary maps, equal stretches can yield different nonlinear behavior:
rotating both a map and its readout preserves their linear geometry but
generally does not commute with coordinatewise activation. The explicit
sine example in [Polar mechanism, Section 5](POLAR_MECHANISM.md) verifies
this. It is not an example of two different shears with the same full
known-frame response Gram; those richer Grams also retain cross-block
transfer information.

## 7. Exactness theorem and proof

**Theorem.** Start (9) from the compatible state obtained by (5)–(8) from
the source initialization. On the source runtime's interval of existence,
with its original readout correction defined, (10)–(18) give exactly its
predictions and its metric feature pairings on the represented input space.
Original layer maps may be rectangular, singular or pass through rank changes.
No new layer-rank assumption is necessary.

**Proof.** The shear forward induction was established after (5). Its full
backward adjoint induction gives
\(d_a^{(\ell)}=O_\ell^\top\iota_\ell\delta_a^{(\ell)}\), with
whitening understood. The source and target projections in (13) consequently
give \(U_\ell=O_\ell^\top\dot F_\ell O_{\ell-1}\). The final mask
makes (11) exactly the source correction. Similarity preservation gives (18).

Differentiate (6) and set \(\dot O_\ell=O_\ell\Omega_\ell\). Then

\[
\dot S_\ell=U_\ell+S_\ell\Omega_{\ell-1}-\Omega_\ell S_\ell.
\tag{20}
\]

The symmetry of \(\dot S_\ell\) is precisely (14). Differentiating
\(G_\ell=O_{\ell-1}^\top F_\ell^\top F_\ell O_{\ell-1}\) gives
(15). Differentiating (8), its unit and mask, and the rotated readout gives
(16)–(17). Thus a source solution produces a solution of the closed system.

Conversely, from a solution of that system integrate
\(\dot O_\ell=O_\ell\Omega_\ell\) for the proof only. Skew symmetry
preserves orthogonality. The tensor, unit and mask equations imply that they
remain the rotated original algebra objects: both descriptions solve the
same linear transformation equations with the same initial values.

The positive square root \(S_\ell=G_\ell^{1/2}\) has derivative determined
uniquely by
\(S_\ell\dot S_\ell+\dot S_\ell S_\ell=\dot G_\ell\).
The expression in (20) is symmetric by (14) and satisfies this equation
by (15). Reconstructing \(F_\ell=O_\ell S_\ell O_{\ell-1}^\top\)
therefore gives \(\dot F_\ell=O_\ell U_\ell O_{\ell-1}^\top\).
Because both pulse factors were projected, this derivative occupies exactly
the original single off-diagonal block. It preserves the shear form and is
the original optimizer. The readout and deficits reconstruct likewise.

Smoothness is local on the SPD and readout-invertibility domain. For matrix
activation evaluation, strip analyticity supplies a holomorphic matrix-function
extension to a neighborhood of every compatible state: its multiplication
matrices have real spectrum, and a nearby contour lies in the activation
strip. Thus repeated eigenvalues do not prevent local smoothness or uniqueness.
The proof does not use numerical spectral interpolation near a collision.

Finally, for an original whitened map of norm \(\|B_\ell\|\),

\[
(1+\|B_\ell\|)^{-2}I\preceq G_\ell
\preceq(1+\|B_\ell\|)^2I,
\tag{21}
\]

because both \(F_\ell\) and its explicit inverse have norm at most
\(1+\|B_\ell\|\). A finite source map therefore cannot cause a polar
rank singularity. Local uniqueness and continuation establish equality
throughout the source existence interval. This proves both necessity and
sufficiency of the closed equations. \(\square\)

There is also a direct endpoint argument. In this paragraph only, let
\(\theta\) collect the source maps and raw readout, with the fixed product
Hilbert--Schmidt metric induced by their source/target feature metrics.
Equation (4) is the Gram of their update directions, so (3) gives exactly
\[
\|\dot\theta\|^2=\frac4{m^2}c^\top Kc
=-\frac1m\frac d{dt}\|c\|^2.
\]
Consequently
\[
\int_k^{k+1}\|\dot\theta(t)\|\,dt
\le\left(\int_k^{k+1}\|\dot\theta(t)\|^2\,dt\right)^{1/2}
\le\frac{\|c(k)\|}{\sqrt m}.
\]
For a global source trajectory with exponentially decaying deficits, the sum
over integer \(k\ge0\) is finite. Hence the source parameters have limits,
without inferring a backward-response bound from forward boundedness alone.
The polar construction is continuous there by (21), and its geometric state
has the corresponding limit. If the source supplies the uniform correction
Gram gap, the limiting state evaluates the same fitted prediction by (11).
More generally, prediction equality alone transfers any fitted-predictor
limit supplied by the source theorem, without asserting that a potentially
singular limiting correction formula is defined.

## 8. Actual sample-feature motion, not just frame geometry

To interpret the learned features themselves, return temporarily to the
physical source variables of Section 3. Define \(J_{ab}^{(\ell)}\) as
the preactivation change at input \(a\) per unit update from training
input \(b\), with the deficit coefficient omitted. Then

\[
J_{ab}^{(1)}=\delta_b^{(1)}(v_b^\top v_a),
\]
\[
J_{ab}^{(\ell)}=
\delta_b^{(\ell)}
\langle h_b^{(\ell-1)},h_a^{(\ell-1)}\rangle_{M_{\ell-1}}
+B_\ell\bigl(\phi'(z_a^{(\ell-1)})\odot J_{ab}^{(\ell-1)}\bigr).
\tag{22}
\]

This follows directly by differentiating the forward pass along the rank-one
update. The two terms are respectively the direct write at this layer and
feature motion arriving from earlier layers. The receiving input's gate
then gives its activation motion:

\[
\dot h_a^{(\ell)}=\frac2m\sum_{b=1}^m
c_b\,\phi'(z_a^{(\ell)})\odot J_{ab}^{(\ell)}.
\tag{23}
\]

Consequently the actual feature similarity obeys

\[
\begin{split}
\frac d{dt}\langle h_a^{(\ell)},h_b^{(\ell)}\rangle_{M_\ell}
=\frac2m\sum_{s=1}^m c_s\bigl[&
\langle\phi'(z_a^{(\ell)})\odot J_{as}^{(\ell)},h_b^{(\ell)}\rangle_{M_\ell}
\\+&\langle h_a^{(\ell)},\phi'(z_b^{(\ell)})\odot J_{bs}^{(\ell)}\rangle_{M_\ell}
\bigr].
\end{split}
\tag{24}
\]

Thus “same label attracts” is not the law. The sign depends on the current
deficit, which layer writes the change, the sending feature overlap, the
backward response, and the receiving activation sensitivity. Feature
similarities may increase or decrease. Their Gram remains PSD, although its
time derivative need not be PSD.

Equations (22)–(24) by themselves are not closed without source maps. Here
they are an interpretation of the already closed system: equivalent response
computations follow by differentiating (10)–(12) using its current tensors
and square roots. No weight oracle is added to (9)–(18). The finite algebra
contains the coactivation information needed to evaluate these responses.

Validation inputs can occupy either observed slot \(a,b\), but never the
driving slot \(s\). This gives their evolving representations without
letting them influence training.

## 9. Dense comparison: exactly what transfers

Let \(f_{\mathrm{geom}}\) denote this realization and
\(f_{\mathrm{Harm},n,q}\) its source runtime. In the full-input-space
version, the theorem gives

\[
f_{\mathrm{geom}}(t,x)=f_{\mathrm{Harm},n,q}(t,x)
\quad\text{for every represented time and every }x.
\tag{25}
\]

Therefore every valid supplied-budget Harmonic certificate transfers verbatim:
same dense reference, probability event, label cap, width threshold and norm
\(\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|\cdot|\), including the
fitted endpoint. This assertion introduces no independent randomness.

For example, the imported original source-tolerance \(1/n\) specialization
has the stated error

\[
C\beta^{CL}Y\frac m\gamma
\left(1+\sqrt{\frac m\gamma}\right)
\frac{\exp(C\sqrt{\log(en)})}{n}.
\tag{26}
\]

Here \(Y=\|y\|/\sqrt m\), \(\gamma\) is the initial limiting feature-Gram
gap, and \(\beta\) is the source activation/depth envelope. The constants,
qualification and event in (26) are the imported ones, not newly optimized
constants. At fixed admissible nonzero label scale and other fixed parameters,
the rate is \(n^{-1+o(1)}\). If the source theorem compares this to actual
dense-run variability, the same comparison holds for (25). No label cap is
shrunk with \(n\) by this transformation.

An exact coordinate conversion does **not** prove that its new tensors equal
similarly named tensors of the dense network. In particular (25) alone is not
a theorem about all hidden features or all internal response derivatives.
The following elementary consequence records the more limited hidden-Gram
information actually available from the source comparison proof.

### Finite-horizon hidden-Gram consequence

Fix a layer and a source construction interval. Suppose each dense feature
has RMS norm at most \(H\), its source approximation error is at most
\(\eta\) per coordinate, and the source comparison proves
\(\|h_{\mathrm{Harm}}-h_{n,I}\|_M\le e\), uniformly in time and input.
The source metric bounds give
\(\|h_{n,I}\|_M\le H+3\eta\) and pairing defect at most
\(6H\eta+9\eta^2\). Hence, for every pair of represented inputs,

\[
\left|
\langle h_{\mathrm{geom},a},h_{\mathrm{geom},b}\rangle
-\frac1n h_{n,a}^\top h_{n,b}
\right|
\le 2(H+3\eta)e+e^2+6H\eta+9\eta^2.
\tag{27}
\]

Indeed, subtract the selected dense pairing, expand the two feature errors,
and bound the two cross terms and their product by Cauchy–Schwarz; then add
the source pairing defect. No additional hypothesis is created by this
algebraic implication. In the source's notation its finite-horizon forward
and scalar comparison bounds give explicitly

\[
e=F\eta\left[1+(1+\sqrt{m/\gamma})(e^{\mathcal B_n}-1)\right].
\tag{28}
\]

Here \(F,\mathcal B_n\) are exactly the coefficients defined in the
integrated result's “Harmonic forward subtraction coefficients” and “Harmonic
exact error coefficient,” not new free parameters. This is a finite-source-
interval consequence. We do not silently extend (27) to the endpoint, to
backward tensors, or to a stronger norm without the appropriate tail/response
estimates. The all-time **prediction** guarantee (25) does not have this
additional limitation.

## 10. Storage, arithmetic and initialization provenance

With one block indicator per frame, a direct dense-tensor representation has
exact moving scalar count

\[
L\left[\frac{D(D+1)}2+D^3+2D\right]+D+m,
\qquad D=d+\sum_\ell q_\ell.
\tag{29}
\]

Fixed frame-zero algebra, input embedding, masks and labels must also be
retained. Their storage is polynomial in \(D,d,m\), bounded by the same
leading cubic envelope, apart from an explicitly stored input panel if desired.
An input panel of \(N\) points adds \(Nd\) words in the full-space version;
it can instead be streamed. The panel-span version replaces \(d\) by its
rank and stores the projected inputs. There is no claim uniform in input
dimension, depth or tensor conditioning hidden in “polylogarithmic.”

Conversion from an already initialized Harmonic model is finite: flatten
metrics, build the fixed product, form the shears, take their sequential
polar factors, rotate the tensor/unit/masks, and transform the readout.
Naive dense tensor rotation costs \(O(LD^4)\) scalar arithmetic operations;
the matrix factorizations cost \(O(LD^3)\). These are additional conversion
costs; they do not replace or erase the source initializer's costs.

For a supplied state, the dense tensor derivative in (16) costs
\(O(LD^4)\). Apart from activation matrix-function evaluation, a direct
training right-hand side has the remaining cost
\(O(mLD^3+m^2LD+m^3)\), with peak storage including
\(O(mLD+m^2)\) workspace in addition to the retained state. Treating a
matrix function at the requested accuracy as a cubic-cost primitive gives
that displayed arithmetic envelope. A precision-dependent implementation
must instead add its actual matrix-function work. No uniform bit-complexity,
stable interpolation, or practical speedup is being claimed.

Every new coefficient uses the initialized compressed model and its specified
metrics, plus the input geometry. No later dense or compressed trajectory is
queried to define the geometric state. The source initializer's own provenance
and computational qualifications are inherited, not altered.

## 11. What has and has not been resolved

The exact finite ODE is established, including all gates, masks, correction,
rank changes, passive validation, prediction-certificate transfer and polynomial
state overhead. Its mechanisms are tangible: error-weighted forward/backward
associations; direct and propagated feature motion; response-metric deformation;
and coactivation alignment. These are more informative than an unexplained
time-dependent kernel.

However, in physical source/target blocks,

\[
\begin{pmatrix}I&0\\B&I\end{pmatrix}^{\!\top}
\begin{pmatrix}I&0\\B&I\end{pmatrix}
=\begin{pmatrix}I+B^\top B&B^\top\\B&I\end{pmatrix}.
\tag{30}
\]

Thus a full shear Gram contains the original map in its cross block. The
moving tensors and masks make it possible to evaluate nonlinear feedback
without reconstructing that map; they do not prove its information has been
removed. Likewise, \(\det G_\ell=1\) is an artifact of the shear embedding,
not a new conservation law of learning. These facts must accompany any claim
of interpretation.

The more ambitious open target is an approximation at dense variability
using a smaller, directly sample-indexed collection of meaningful responses,
without complete map-orientation information or an opaque closure rule.
The ordinary-Gram counterexample and the noncommuting-force examples specify
what such a theory must retain. They do not rule it out. Neither low-order
moment truncation, a frozen-kernel approximation, nor the cubic small-label
expansion currently proves that target at fixed nonzero labels.

## 12. Checks, competing routes and next step

| Route or claim | Current status |
|---|---|
| Ordinary feature/velocity Grams | Exact obstruction for the specified state; no typical-Gaussian no-go claim |
| Ordered force-memory model | Explicit first nonlinear response; arbitrary-order all-time compression not proved |
| Fixed semantic activation algebra | Exact closure with transfer state; generic full algebra retains neuron information |
| Anchored Gram-particle lift | Exact but redundant: its new particle Gram is determined by the old transfer coordinates |
| Direct polar layer model | Reveals geometry; additional invertibility/shape assumptions make it insufficient alone |
| Shear-polar model (9)–(18) | Exact full-scope realization; retains map information with explicit geometric mechanism |
| Dense comparison | Exact inheritance of the source certificate, not an independent reproof of that certificate |
| Further sample-observable reduction | Open; not implied by any preceding row |

The completed independent first routes are recorded in
[Observable geometry](OBSERVABLE_GEOMETRY.md),
[Relational quotient](RELATIONAL_QUOTIENT.md), and
[Response memory](RESPONSE_MEMORY.md). Cross-pollination was permitted only
after those independent routes were frozen. The polar construction and
singularity repair are in [Singularity-free polar](SINGULARITY_FREE_POLAR.md),
with separate exactness and mechanism reconstructions in
[Polar audit](POLAR_AUDIT.md) and [Polar mechanism](POLAR_MECHANISM.md).
These are internal derivations and bounded checks, not promotion reviews.

The deterministic check is
[polar_identity_check.py](polar_identity_check.py), run by the lead with
NumPy 1.26.4 and SciPy 1.13.0. It tests three rectangular/multilayer cases,
including rank-deficient maps and nondiagonal SPD metrics. It checks
prediction/kernel equality, the projected update, finite-difference derivatives
of the response Grams and rotating tensors, the exact midpoint identity,
readout transport and passivity. Maximum forward identity error was
\(1.2\times10^{-13}\); maximum finite-difference derivative discrepancy was
\(9.6\times10^{-9}\). This verifies local implementation identities, not
global convergence or probabilistic accuracy. No neural training campaign or
literature search was conducted.

Next research bottleneck: identify which **nonlinear orientation information**
can be replaced by sample-response/coactivation observables at the target error,
with a stability theorem that does not freeze feature learning or shrink labels
with width. Until that bridge is proved, the strongest defensible result is the
exact geometric realization above, not a claim that the full explanatory goal
has been settled.
