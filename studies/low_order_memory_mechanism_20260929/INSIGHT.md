# Learning by moving the addresses of accumulated credit

This first synthesis is extended by [DEEPER_INSIGHT.md](DEEPER_INSIGHT.md),
which derives whole-function selection, local nonlinear feature feedback,
and clock-induced relearning effects. The results below remain valid.

29 September 2026. Internally derived synthesis for the autonomous response
memory model in MODEL.md. This is a new investigation of the closure itself,
not a dense-network approximation theorem. The derivations below use its own
responses. No population limit, neuron independence or empirical fitting
result is assumed. The paper has not been changed.

The useful organizing principle is **adaptive reciprocal associative memory,
with an exact temporal energy budget**. Learning has two operations: accumulating
new error credit, and moving the feature addresses at which existing credit is
applied. Their alignment is an exact diagnostic of the hidden layers' effect
on loss and supplies a sufficient route to successful learning. It is not a
necessary condition: outer-layer descent can compensate adverse hidden
contributions. The general Gaussian, multi-input alignment theorem is still
open.

## 1. The simplest closure already changes how old experience is used

Take m samples and a width-n hidden link. Write h_a for sample a's forward
feature at its input, delta_a for its backward response at its output, and
r_a=f_a-y_a. The activity clock satisfies

\[
 \dot\tau=\rho,\qquad
 \rho^2=\frac1m\sum_a r_a^2,\qquad\tau(0)=1.
\]

At order q=1, replace the two raw moments B_a,C_a by

\[
 a_a=B_a/\tau,\qquad u_a=-2C_a.
\]

Here a_a is the remembered feature address and u_a the accumulated error
credit. Their exact equations, reconstruction and initialization are

\[
 \dot a_a=\frac\rho\tau(h_a-a_a),\quad
 \dot u_a=-2r_a\delta_a,\quad
 W=W_0+\frac1{mn}\sum_a u_a a_a^T,
 \qquad a_a(0)=h_a(0),\ u_a(0)=0.                 \tag{1}
\]

Consequently a new input with current feature h receives

\[
 Wh=W_0h+\frac1m\sum_a u_a\frac{a_a^Th}{n}.        \tag{2}
\]

Its overlap with each remembered feature determines how much of that
sample's accumulated credit is applied. These are signed similarity scores,
not probabilities or normalized attention weights. The exact transpose

\[
 W^T\delta=W_0^T\delta+
       \frac1m\sum_a a_a\frac{u_a^T\delta}{n}     \tag{3}
\]

routes backward credit through the same associations in reverse. Nonlinear
gates and the adjacent layers supply the fields written back into (1).

Crucially, moving an address changes the use of *previously* accumulated
credit. Differentiating (1) gives

\[
 \dot{\Delta W}=
 -\frac2{mn}\sum_a r_a\delta_a a_a^T
 +\frac\rho{mn\tau}\sum_a u_a(h_a-a_a)^T.        \tag{4}
\]

The first term writes new credit; the second transports old credit to a
changing feature address. A fixed dictionary suppresses this mechanism. An
ordinary trained low-rank factorization generally has a different equation
for its factors, so the representation rank alone does not specify learning.

In particular a nonzero address has direction e_a=a_a/||a_a|| satisfying

\[
 \dot e_a=\frac\rho{\tau\|a_a\|}(I-e_ae_a^T)h_a. \tag{5}
\]

Only a component of the present response outside the old address rotates it.
The instantaneous learned rank is at most m, but its neuron-space subspaces
are not fixed. Small temporal order does not impose a small degree of spatial
nonlinearity: (2) is composed with nonlinear features through all layers.

For a test input x the score in (2) is exactly

\[
 \frac{a_a(t)^Th(t,x)}n=
 \frac{h_a(0)^Th(t,x)+\int_0^t\rho(s)h_a(s)^Th(t,x)\,ds}
      {n\tau(t)}.                                \tag{6}
\]

Thus transfer from training to test inputs depends on similarity to the
*evolving history* of training features, measured using the current test
feature. This cross-time similarity need not be a symmetric positive
semidefinite kernel on the training samples.

## 2. Velocity and acceleration: a precise version of the intuition

Let g(xi) be any one component of a forward or backward activity history,
including the prescribed initial prefix, and let

\[
 \mu_k=\int_0^1g(\tau v)p_k(v)\,dv
\]

be its normalized shifted Legendre moment. For g in H^k(0,tau), Rodrigues'
formula followed by k integrations by parts gives

\[
 \mu_k=\frac{\tau^k}{k!}
          \int_0^1[v(1-v)]^k g^{(k)}(\tau v)\,dv. \tag{7}
\]

The boundary terms vanish since v^k(v-1)^k and its derivatives of orders
less than k vanish at both endpoints. In particular,

\[
 \mu_1=\frac\tau6\int_0^1 6v(1-v)g'(\tau v)\,dv,
 \qquad
 \mu_2=\frac{\tau^2}{60}
         \int_0^1 30v^2(1-v)^2g''(\tau v)\,dv.    \tag{8}
\]

Both displayed weights integrate to one. Order q=1 retains mean history;
q=2 adds a weighted average of activity-time velocity; q=3 adds a weighted
average of activity-time acceleration, with the explicit scale factors in
(8). These are historical derivative averages, not current derivatives or a
Taylor prediction of the future. If the artificial prefix creates a jump or
kink, the required Sobolev condition must be checked. The integral moments
themselves remain valid without derivative regularity.

For paired forward and backward histories, the retained interaction is
proportional to

\[
 \sum_{k<q}(2k+1)\mu_{b,k}\mu_{h,k}^T.           \tag{9}
\]

At q=1 this is the product of their means. The omitted full-history term is
their temporal cross-covariance. Higher orders retain progressively more of
that correlated variation: the first trend pairs with the first trend, and
curvature with curvature. Orthogonality is in the temporal coordinate; it
does not assert orthogonality or independence between neurons. This describes
which information higher order restores without referring to a dense model.

## 3. A passive filter, not an arbitrary memory recurrence

For normalized moments mu_k=M_k/tau, in logarithmic activity s=log(tau),

\[
 \frac{d\mu_k}{ds}=g-(k+1)\mu_k-
                      \sum_{j<k}(2j+1)\mu_j.    \tag{10}
\]

The homogeneous eigenvalues are -1,...,-q. At q=1 the remembered feature
obeys da/ds=h-a: uniform averaging in activity is exponential smoothing in
logarithmic activity. All neurons share this filter, but their inputs are
generated by the evolving nonlinear network.

There is a stronger statement than eigenvalue stability. Define

\[
 E(\tau)=\frac1\tau\sum_{k<q}(2k+1)\|M_k\|^2,
 \qquad g_*(\tau)=\frac1\tau\sum_{k<q}(2k+1)M_k.
\]

Direct differentiation of the triangular moment equations gives exactly

\[
 \boxed{\frac{dE}{d\tau}=\|g\|^2-\|g-g_*\|^2.}  \tag{11}
\]

The coefficient identity proving this is given in PROJECTION_MECHANISM.md
and independently in STABILITY_PRINCIPLE.md. It is valid for any order and
in any real Hilbert norm, including normalized neuron RMS. Integrating (11)
shows that initial storage plus supplied response energy pays for both stored
memory and the integrated squared endpoint mismatch. There is no width or
order factor. This is an energy balance for the filter; since the network
endogenously supplies g, it is not by itself a loss-descent theorem.

At finite width and order, the tanh closure is globally defined for all
finite physical times, for arbitrary finite labels. One proof bounds the
readout and residual on each finite interval, then bounds backward moments
and reconstructed matrices successively from the last layer toward the
first. This establishes existence, not all-time boundedness or fitting;
the complete continuation proof is in STABILITY_PRINCIPLE.md.

## 4. The direct learning question becomes temporal alignment

On an interval with rho>0, for a hidden link let h_* and b_* be the projected
endpoints of its own histories, b_a=(r_a/rho)delta_a, and write

\[
 G_\ell=\sum_a r_a\delta_a^\ell(h_a^{\ell-1})^T,
 \qquad
 R_\ell=\sum_a(b_a-b_{*,a})(h_a-h_{*,a})^T.
\]

Differentiating the paired moments gives the exact physical velocity

\[
\dot W_\ell=-\frac2{mn}(G_\ell-\rho R_\ell).    \tag{12}
\]

At zero residual use the original undivided moment ODE; all velocities are
zero. No ratio r_a/rho is needed by the algorithm there.

Set g_w=sum_a r_a h_a^L and
g_1=sum_a r_a delta_a^1 x_a^T/sqrt(d). The closure's own loss obeys

\[
 \dot\rho^2=
 -\frac4{m^2n}(\|g_w\|^2+\|g_1\|_F^2)
 -\frac4{m^2n^2}\sum_\ell\|G_\ell\|_F^2
 +\frac{4\rho}{m^2n^2}\sum_\ell\langle G_\ell,R_\ell\rangle_F.
                                                               \tag{13}
\]

The final scalar term is the precise feedback obstacle. Temporal memory
discrepancy matters through its *alignment with the current loss gradient*,
not just its magnitude. For example, if
rho sum <G,R> <= kappa sum ||G||^2 with kappa<1, memory preserves a fixed
fraction of the hidden-layer gradient dissipation. A persistent lower bound
on total gradient dissipation relative to loss then implies exponential
fitting. These are sufficient conditions, not assumed properties of Gaussian
training. LEARNING_GEOMETRY.md also expresses the q=1 condition directly
through current-feature/remembered-feature cross-Gram matrices and the
transport term in (4).

## 5. A complete nonlinear fitting benchmark

**Established here:** take q=1, one nonzero training input, width n=1,
arbitrary finite hidden depth, tanh, zero readout, and independent nondegenerate
scalar Gaussian hidden initialization (and Gaussian first-layer row). For
every fixed finite scalar label y, almost surely the output moves monotonically
from zero toward y and

\[
 |f(t)-y|\le |y|\exp[-2|h^L(0)|^2t].            \tag{14}
\]

No small-label assumption or dense reference is used. The rate is positive
almost surely, but can be small and is not uniform in depth or initialization.

The proof is constructive. Oddness of tanh permits sign changes of each
scalar hidden coordinate so that the initial first response and all scalar
links are positive; changing the readout sign handles y<0. These changes
preserve the closure equations and replace y by |y|. Before first fit,
r<0, readout and backward responses are nonnegative, and the accumulated
backward moments are nonpositive. The remembered forward features stay below
their current features. Consequently both terms in (4) make each hidden link
increase. All hidden features are nondecreasing. Thus

\[
 \dot f=\dot w h^L+w\dot h^L
       \ge 2(y-f)(h^L)^2
       \ge 2(y-f)|h^L(0)|^2.
\]

At fit all velocities vanish, so uniqueness prevents crossing the target.
Integration gives (14). The complete invariant-cone and sign-gauge arguments
are in STABILITY_PRINCIPLE.md. For nonzero y, hidden features actually move;
their gates have not been frozen. A deterministic arbitrary-width extension
holds when initial first features are entrywise positive and hidden matrices
are entrywise nonnegative, with rate 2||h^L(0)||^2/n. Those sign hypotheses are
not generic Gaussian initialization at width greater than one.

This benchmark is deliberately limited: readout training alone could fit one
point, so it does not establish the necessity or advantage of feature learning.
It shows rigorously that the evolving deep memory feedback can cooperate with
fitting, rather than destabilize it. The scalar sign argument does not extend
automatically to mixed-sign wide matrices or competing training examples.

## 6. What this makes worth investigating

The central direct question is now whether training creates or preserves
enough *temporal coherence* for old credit and moving feature addresses to
cooperate. This connects an exact microscopic equation (4), a dimension-free
memory energy balance (11), an exact loss diagnostic (13), and a reachable
case of global learning (14). It is more specific than saying only that a
low-rank state can represent useful functions.

The next minimal unresolved test is q=1, one sample, two hidden layers,
width at least two, standard fixed Gaussian mixing. Does fitting occur
almost surely for every fixed label? The scalar result supports this as a
conjecture, but does not prove it. An arbitrary inconsistent memory state
with increasing loss is not a reachable counterexample; conversely filter
passivity is not a proof of fitting. The reports preserve that distinction.

With m samples and q modes there are O(mq) vector channels per layer, each
still containing n coordinates. The same W0 and W0^T are reused, so their
correlations remain part of the direct problem. No finite global scalar ODE,
independent Monte Carlo interpretation, or population-limit theorem has been
derived here.

## Verification and artifacts

- MODEL.md fixes the complete autonomous equations and initializer.
- PROJECTION_MECHANISM.md derives (1)--(11) in detail.
- LEARNING_GEOMETRY.md derives direct loss/alignment identities and the
  positive-sign fitting proof.
- STABILITY_PRINCIPLE.md independently derives passivity, proves global
  existence and the Gaussian scalar sign reduction, and separates actual
  reachability from arbitrary-state obstructions.
- check_identities.py verifies the moment differentiation, derivative
  interpretation, filter recursion, energy identity and paired velocity for
  q=1,...,6. The deterministic maximum discrepancy was 4.51e-13 with tolerance
  1e-9. This verifies algebra only, not learning trajectories. The record is
  data/generated/low_order_memory_mechanism_20260929/identity_check_01/checks.json.

These are internally derived, checked results. No empirical neural experiment,
literature novelty assessment, paper revision or Git operation was performed.
