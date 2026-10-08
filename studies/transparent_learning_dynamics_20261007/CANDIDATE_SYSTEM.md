# Candidate: causal feature--response dynamics

2026-10-07. This is the next conceptual deliverable requested by the user:
one explicit system, a nonlinear two-hidden-layer mechanism, and an honest
separation between the constructed system and missing approximation theorems.

The candidate retains the **history of representative feature and backward
response laws**, together with their first local sensitivities. It does not
retain learned inter-neuron matrices. Its currently rigorous form is a closed
discrete-time population dynamical system. Its continuous-time interpretation
is a history-state law, not a small finite-dimensional Markov ODE.

Latest diagnostic: the
[fresh-quadrature audit](FROZEN_QUADRATURE_RESULT.md) independently integrates
the recorded coefficient histories without updating them. Lower-layer
similarities shift substantially toward dense, while the strict fresh-sampling
resolution gate still fails. This is evidence about a necessary moment
self-consistency defect, not an improved autonomous trajectory or a change
to the equations below. The full coupled-model accuracy remains unresolved.

Latest coupled numerical update: the
[16-input integration repair](RESIDUAL_FILTER_RESULT.md) retains every causal
mechanism and tests a consistent residual-filtered numerical step. This changes
the finite-step program, not the intended continuous vector field to first
order; convergence of the growing-history program remains unproved. All 24
prescribed runs are stable in saved loss, and the checked dense RK4 reference
is resolved. But lower-layer mean similarity errors remain 27–31% on the same
filtered mesh, and particle/mesh checks prevent a definitive population-law
accuracy conclusion. The equations below retain their original unfiltered
step convention; the new report specifies the filtered convention separately.

Preceding experimental update: the
[4–16-input trajectory tests](MULTISAMPLE_TRAJECTORY_RESULT.md) retain this
system unchanged. With four passive inputs, they support both hidden layers'
same-mesh similarity dynamics for 4 and 8 training inputs, while the
16-input meshes fail numerical resolution. They distinguish individual
feature displacement from shared off-diagonal associations: reciprocal
removal can increase the former while weakening the latter. They also
confirm middle-memory redistribution on two seeds and identify unresolved
late-time activation-control numerics. Global proofs and further two-input
cubic work remain paused.

Previous experimental update: the
[unequal-residual and passive-mechanism tests](UNEQUAL_RESIDUALS_RESULT.md)
retain the equations below. They show why a training-only cubic reduction
must not replace the passive history: its predicted passive response fails
at moderate labels even after adding the leading ordered-write correction.
The new exact diagnostic is the passive feature's departure from the
geometric mixture of training features, projected onto the readout. Its
evolution separates readout learning, middle-layer writes and lower-feature
motion, with distinct activation gates. The tests support these mechanisms
on fixed examples, not a general full-trajectory accuracy guarantee.

## 1. What is the state?

Fix normalized inputs \(v_a=x_a/\sqrt d\), training indices \(a\le m\),
a declared panel \(a\le p\), and a timestep \(\Delta>0\).
Only training indices have labels. Write
\(S_{ab}=v_a^\top v_b\) and \(c_a^k=y_a-f_a^k\).
Use the inherited strip-analytic activation class. In particular each
activation is \(C^2\) on the real line with bounded first and second
derivatives, while its values may be unbounded with at most linear growth.

For two hidden layers, in each of two distinct neuron populations retain
the joint histories of its scalar fields:
\[
\begin{array}{c|c}
 \text{lower population}&z_{1,a},\ h_{1,a}=\phi_1(z_{1,a}),
       \ b_{1,a},\ \delta_{1,a}=\phi_1'(z_{1,a})b_{1,a}\\
 \text{upper population}&z_{2,a},\ h_{2,a}=\phi_2(z_{2,a}),
       \ w,\ \delta_{2,a}=\phi_2'(z_{2,a})w .
\end{array}
\]
Here \(b\) is the signal arriving backward before the derivative gate;
\(\delta\) is that signal after the gate. These are representative-neuron
random fields; none is an \(n\)-coordinate vector.

The state is not just their separate marginals. It includes their canonical
joint Gaussian-to-field computation rules and all joint first tangent
fields needed below. This preserves which activations and sensitivities
occur together, information ordinary Gram matrices lose.

From the state evaluate the two-time similarities
\[
 C^1_{ab}(k,j)=\mathbb E[h_{1,a}^k h_{1,b}^j],\quad
 C^2_{ab}(k,j)=\mathbb E[h_{2,a}^k h_{2,b}^j],\quad
 D^2_{ab}(k,j)=\mathbb E[\delta_{2,a}^k\delta_{2,b}^j].
 \tag{1}
\]
Expectations are within one population, never an arbitrary pairing of
neuron coordinates across layers.

The first layer starts with a centered Gaussian panel of covariance \(S\).
Two additional centered Gaussian primitive families have covariances
\[
 \mathbb E[\eta_a^k\eta_b^j]=C^1_{ab}(k,j),\qquad
 \mathbb E[\xi_a^k\xi_b^j]=D^2_{ab}(k,j).
 \tag{2}
\]
The first-layer root, the upper family \(\eta\), and the lower family
\(\xi\) are independent families. Within each family, times and samples
are correlated according to (2). They are not fresh training noise.

The directed responses are
\[
 R^h_{ab}(k,j)=
 \mathbb E[\partial_{\xi_b^j}h_{1,a}^k],\qquad
 R^\delta_{ab}(k,j)=
 \mathbb E[\partial_{\eta_b^j}\delta_{2,a}^k].
 \tag{3}
\]
These are total derivatives through the local scalar circuit, holding all
deterministic population coefficients \(c,C,D,R\) fixed. That convention
defines a local Gaussian probe, not a perturbation of all training data or
of the whole population law.

## 2. Its explicit closed evolution

Start with \(w^0=0\). At step \(k\), the equations are
\[
\begin{aligned}
 z_{1,a}^k
 &=z_{1,a}^0+
       \frac{2\Delta}{m}\sum_{j<k,b\le m}
         c_b^jS_{ab}\delta_{1,b}^j,\\
 w^k
 &=\frac{2\Delta}{m}\sum_{j<k,b\le m}c_b^j h_{2,b}^j,\\
 z_{2,a}^k
 &=\eta_a^k+
     \sum_{j<k,b\le p}R^h_{ab}(k,j)\delta_{2,b}^j
     +\frac{2\Delta}{m}\sum_{j<k,b\le m}
         c_b^jC^1_{ab}(k,j)\delta_{2,b}^j,\\
 b_{1,a}^k
 &=\xi_a^k+
     \sum_{j\le k,b\le p}R^\delta_{ab}(k,j)h_{1,b}^j
     +\frac{2\Delta}{m}\sum_{j<k,b\le m}
         c_b^jD^2_{ab}(k,j)h_{1,b}^j,\\
 f_a^k&=\mathbb E[w^k h_{2,a}^k].
\end{aligned}
\tag{4}
\]
Use the pointwise definitions in Section 1 and set \(c=y-f\) only on
training indices.

Equations (1)--(4) do not outsource the response coefficients. Append the
following **first-tangent update rule** for every already introduced
primitive coordinate:
\[
 \partial h_\ell=\phi_\ell'(z_\ell)\partial z_\ell,\qquad
 \partial\delta_1
   =\phi_1''(z_1)b_1\,\partial z_1+\phi_1'(z_1)\partial b_1,
 \qquad
 \partial\delta_2
   =\phi_2''(z_2)w\,\partial z_2+\phi_2'(z_2)\partial w .
 \tag{5}
\]
In (4), differentiate every displayed field term with these rules,
keep \(c,C,D,R\) fixed, set the derivative of the probed primitive to
one and other primitive derivatives to zero, and start with zero
derivatives before that probe is introduced. All remaining operations in
(4) are scalar linear combinations. Thus (5) is a complete deterministic
update algorithm for the tangent fields, not an undefined hierarchy.
Average the indicated tangent fields to obtain (3). Full expanded
two-layer recursions are in CANDIDATE_CLOSURE_CHECK.md, equations (4)--(5).

At each step the order is: lower features and their tangents; new upper
Gaussian coordinates; upper features/output/backward signals and tangents;
new lower Gaussian coordinates; lower backward signals and tangents.
Each new covariance row is an uncentered Gram of already available fields
and is positive semidefinite. Singular covariances are allowed.

This makes the system autonomous on its **whole history state**. Its rule
uses the current state, fixed inputs, labels and timestep, not an external
dense trajectory or a time-dependent fitted coefficient table. It is not
autonomous on \(C,D,R\) alone. The retained history and integration dimension
grow with the number of steps; exact Gaussian expectation evaluation is
not claimed computationally cheap.

Passive indices may be included as observations in the reciprocal sums.
They are absent from every label-driven write. Active fields have no
dependence on passive formal primitives, so adding passive probes does
not change training.

For arbitrary fixed depth, repeat the same forward/reverse interface
at every adjacent layer, use the bottom update in (4) at layer one, and
the readout update at layer \(L\). The complete indexed equations are in
CAUSAL_KERNEL_DYNAMICS.md. This is one construction, not a different
approximation for each depth.

## 3. What each interaction does

The learned forward write is
\[
 c_b^j C^1_{ab}(k,j)\delta_{2,b}^j .
\]
A training sample with an unmet label writes in its backward-response
direction. How much the current query receives depends on its feature
agreement with that sample at the time of the write.

The learned backward write is
\[
 c_b^j D^2_{ab}(k,j)h_{1,b}^j .
\]
Agreement of backward responses selects which earlier forward features
contribute to the current backward signal. These two writes are the
forward and reverse views of the same learned rank-one association.

The \(R\) terms are a different interaction: reciprocal feedback through
the *same initialized random map*. They account for the fact that a feature
used in the forward direction may itself have been changed by a previous
backward use of that map. Removing these terms gives a wrong law, even
for elementary linear forward/reverse cycles.

The current-step term is explicit:
\[
 R^\delta_{ab}(k,k)
 =\mathbf1_{a=b}\mathbb E[w^k\phi_2''(z_{2,a}^k)] .
 \tag{6}
\]
It contributes carrier-weighted nonlinear curvature times the current
feature to the backward signal. The strict-past terms encode the remaining
delayed response; they need not disappear for linear activations.

Finally the predictor is
\[
 f_a^k=\frac{2\Delta}{m}
       \sum_{j<k,b\le m}c_b^j C^2_{ab}(k,j).
 \tag{7}
\]
It matches the query's **current** representation against the training
samples' **earlier** representations. The representation used to interpret
a past learning write can itself change later.

## 4. Nonlinear worked example: labels couple initially orthogonal samples

Take two hidden \(\tanh\) layers, \(m=d=2\), and
\[
 v_1=e_1,\qquad v_2=e_2,\qquad
 v_3=(2e_1+e_2)/\sqrt5 .
 \tag{8}
\]
Input 3 is passive. Choose any fixed sufficiently small nonzero training
labels allowed by the original assumptions. Compare equal and opposite
label signs without changing the initialization law.

At initialization, let \(X_1,X_2\) be independent standard Gaussians in the
first population, \(X_3=(2X_1+X_2)/\sqrt5\), and put, locally in this example,
\[
 \sigma^2=\mathbb E\tanh^2 X,\qquad
 Z_1,Z_2\ \text{independent }N(0,\sigma^2).
\]
The two training features have zero cross-similarity at both hidden layers.
Their initial top feature Gram is
\((\mathbb E\tanh^2 Z)I_2\), with strictly positive gap.
The passive top preactivation is correlated with both training
preactivations, through the first-layer similarities.

The first nonzero readout derivative is
\[
 \dot w(0)=y_1\tanh Z_1+y_2\tanh Z_2 .
 \tag{9}
\]
The first-layer backward carrier's derivative has the exact initial
Gaussian-response law
\[
\begin{aligned}
 \dot b_{1,1}(0)
   ={}&\zeta_1
      +y_1\mathbb E[
          \operatorname{sech}^4 Z+\tanh Z\,\tanh'' Z]\tanh X_1\\
     &+y_2(\mathbb E\operatorname{sech}^2 Z)^2\tanh X_2 ,
\end{aligned}
\tag{10}
\]
and the symmetric formula for sample 2. The centered Gaussian pair
\(\zeta\) is independent of the lower \(X\)'s. Its covariance is the
uncentered Gram of
\(\operatorname{sech}^2 Z_a\dot w(0)\); it is generally not diagonal and
is not obtained by subtracting the displayed reciprocal mean.

Because the first-layer initial velocity is zero,
\[
 \ddot h_{1,a}(0)=
 y_a\operatorname{sech}^4X_a\,\dot b_{1,a}(0),
 \qquad a=1,2 .
 \tag{11}
\]
The cross-sample contribution to the first feature is therefore
\[
 y_1y_2(\mathbb E\operatorname{sech}^2 Z)^2
       \operatorname{sech}^4X_1\,\tanh X_2 .
 \tag{12}
\]
This is a concrete feature-learning rule: the other sample's feature is
written into sample 1's representation, with label-product sign, and only
strongly on neurons where sample 1 remains responsive. Saturated neurons
are suppressed by the squared derivative gate. It is not an assertion
that a mysterious kernel happens to change.

Taking the actual feature inner product gives
\[
 \ddot C^1_{12}(0)
 =2y_1y_2\,\sigma^2
   (\mathbb E\operatorname{sech}^4X)
   (\mathbb E\operatorname{sech}^2Z)^2 .
 \tag{13}
\]
Every coefficient other than \(y_1y_2\) is strictly positive.
Equal labels initially align the two hidden representations; opposite
labels initially separate them, even though their input inner product
and their initial hidden feature inner products are zero.

Both hidden layers participate. The total top-feature cross-acceleration is
\[
\begin{aligned}
 \ddot C^2_{12}(0)=2y_1y_2\big[
 &(\sigma^2+\mathbb E\operatorname{sech}^4X)
       (\mathbb E\tanh^2Z)(\mathbb E\operatorname{sech}^4Z)\\
 &+\sigma^2(\mathbb E\operatorname{sech}^4X)
             (\mathbb E\operatorname{sech}^2Z)^4
 \big].
\end{aligned}
\tag{14}
\]
The part coming from learning the middle matrix alone is
\(2y_1y_2\sigma^2(\mathbb E\tanh^2Z)
(\mathbb E\operatorname{sech}^4Z)\). The remaining terms are first-layer
feature motion propagated through that same initialized interface.
Confusing the first term with the whole answer would hide part of deep
feature learning.

### The passive input moves without supplying a force

Its first-layer acceleration is
\[
 \ddot h_{1,3}(0)=\operatorname{sech}^2X_3
 \left[
 \frac{2y_1}{\sqrt5}\operatorname{sech}^2X_1\,\dot b_{1,1}(0)
 +\frac{y_2}{\sqrt5}\operatorname{sech}^2X_2\,\dot b_{1,2}(0)
 \right].
 \tag{15}
\]
There is no \(y_3\). Isolating the cross-label channel gives
\[
\begin{aligned}
 y_1y_2(\mathbb E\operatorname{sech}^2Z)^2
 \operatorname{sech}^2X_3
 \big[
 &\tfrac2{\sqrt5}\operatorname{sech}^2X_1\,\tanh X_2\\
 &+\tfrac1{\sqrt5}\operatorname{sech}^2X_2\,\tanh X_1
 \big].
\end{aligned}
\tag{16}
\]
Input geometry controls how much of each training force it receives;
the training/query derivative gates select the responsive coordinates.
Thus it does not merely read out a fixed kernel: training changes its
representation through the same signed cross-sample writes.

Its prediction at every discrete step is exactly (7) with \(a=3\).
Already initially,
\(\dot f_3(0)=y_1C^2_{31}(0)+y_2C^2_{32}(0)\).
For the geometry in (8),
\(C^2_{31}(0)>C^2_{32}(0)>0\). To check this without an external formula,
Gaussian integration by parts differentiates
\(\mathbb E[\tanh X\tanh(\rho X+\sqrt{1-\rho^2}U)]\)
in \(\rho\) to
\(\mathbb E[\operatorname{sech}^2X
\operatorname{sech}^2(\rho X+\sqrt{1-\rho^2}U)]>0\).
Apply this first to the input correlations \(2/\sqrt5,1/\sqrt5\),
then to the top Gaussian covariance. Consequently for \(y_1=y>0,y_2=-y\)
the passive initial prediction moves positively, while (13)--(16) describe
the representation change that follows. No validation label is used.

The displayed accelerations are initialized finite-program identities in
the width limit, obtained by differentiating the actual dense equations
at zero and then applying the proved Gaussian response law. No interchange
of a full training-time limit and a width limit is needed for those
identities. TWO_LAYER_MECHANISM_CHECK.md supplies the separate reconstruction.

## 5. Loss decay and the continuous-time interpretation

The exact canonical dense flow, and its compatible Hilbert population flow,
have the tangent kernel
\[
 K_{ab}
 =C^2_{ab}(t,t)
  +C^1_{ab}(t,t)D^2_{ab}(t,t)
  +S_{ab}\mathbb E[\delta_{1,a}(t)\delta_{1,b}(t)] .
\tag{17}
\]
For the dense identity, every expectation and feature/response Gram in
(17) means the corresponding normalized empirical inner product over
neurons. For the Hilbert identity it means the population inner product.
These conventions are separate exact identities, not an assertion that
finite-width empirical Grams already equal their population counterparts.
Each summand is positive semidefinite: a feature Gram, a product of two
Gram entries (equivalently a tensor-product feature Gram), or the same
construction with input and backward-response Grams. Therefore
\[
 \dot f_a=\frac2m\sum_{b\le m}K_{ab}c_b,\qquad
 \frac d{dt}\frac{\|c\|^2}{m}
   =-\frac4{m^2}c^\top K_{\mathrm{tr},\mathrm{tr}}c\le0 .
 \tag{18}
\]
If the inherited fitting argument supplies \(K_{\mathrm{tr},\mathrm{tr}}
\succeq\kappa I\), then
\(\|c(t)\|\le e^{-2\kappa t/m}\|c(0)\|\).
This last step is conditional on that gap, not a new unconditional
small-label theorem.

At fixed positive timestep, (4) is an Euler-history system; exact continuous
loss dissipation must not be asserted for an arbitrary large Euler step.
Its infinitesimal output change has (18), by its common Hilbert
gradient realization. Finite-step loss control additionally requires
an appropriate discretization/stepsize statement.

CONTINUOUS_RESPONSE_LIMIT.md proves a unique global limiting Hilbert
flow and qualitative all-time output convergence under its explicitly
listed finite-width carrier/operator/tail premises. It gives a continuous
dynamical meaning to the compatible finite programs. It does not yet prove
that every explicit discrete \(R\) sum converges to an ordinary time-density
kernel: there is a same-time term (6), and strict-past masses need control
to exclude further concentrated response.

## 6. Exact, conditional, and still missing

**Established inside the study.** The discrete scalar-law system is closed,
causal and autonomous on its full augmented history state; it is the actual
fixed finite neural Euler-program limit, not a fresh-independent-noise
approximation. Singular histories and unbounded activation values are
allowed. First tangent fields suffice. The nonlinear initialization
mechanism above is computed from that same law.

For a fixed \(Q\)-instruction program, the quantitative theorem supplies
\(C_r n^{-1/2}\log^{2Q+2}(en)\) prediction/pairing error outside probability
\(C_rn^{-r}\), at sufficiently large width. Constants depend on the fixed
program and its positive retained-history gaps.

**Conditional established continuum result.** With the stated finite-width
budgets and fitting tails, the compatible laws have a unique continuous
Hilbert flow and qualitative all-time prediction convergence, including
passive inputs and the fitted endpoint. The exact loss identity (18) holds
for that gradient flow. Those upstream budgets are not independently
audited here.

**Not established.** A finite-dimensional Markov ODE; a general explicit
continuous-response density theorem; a mesh-uniform width rate; and the
requested all-time dense-variability guarantee under the complete original
qualifications. Gaussian expectation evaluation and history costs are
also not claimed small.

The candidate passes an initial conceptual test: its equations expose
a signed, gate-selected cross-sample feature write and its passive-query
effect in a genuinely nonlinear two-layer model. The next priority is the
user-directed beyond-initialization phase: analytical approximations and
controlled numerical comparison, including passive inputs and separate memory,
reciprocity and sensitivity diagnostics. Global-proof work is paused. An
initialized mechanism alone does not establish explanatory value throughout
learning.

Internal checks: CANDIDATE_CLOSURE_CHECK.md verifies the explicit finite
closure; TWO_LAYER_MECHANISM_CHECK.md verifies the nonlinear initialized
mechanism. A final scoped claims/indexing check of this synthesis found
only the activation-assumption and empirical-versus-population clarifications,
which are incorporated above. No upstream all-time quantitative theorem was
included in those checks.
