# Can the current response-memory populations collapse to scalar aggregates?

2026-09-25. Theory-only continuation explicitly requested by the user.
Root owns this note and its README entry. No experiment, new implementation,
external scientific retrieval, promotion or Git-index change is authorized
by this assessment. The completed empirical campaigns remain closed.

## Conclusion and contract

Observable-only compression is a legitimate, weaker target than reconstructing
the neuron populations. It requires a second closure beyond the study's finite
history projection. The present construction supplies no exact finite aggregate
closure, and its existing low-order moments do not acquire closed dynamics
merely because only output/loss is requested. A useful approximate aggregate
closure remains open. Failure of the displayed moment list is not a theorem
excluding every nonlinear finite aggregate representation.

Here a scalar system means a finite vector q in R^J, not necessarily one
equation for loss. J may depend on the number of samples, depth, history order,
accuracy and horizon, but should not grow with width or elapsed integration
steps. Its coefficients and initialization must be computable from the model,
data and declared initialization information. No precomputed target curve,
hidden population law, arbitrary-real encoding, or time-driven playback counts.
One rule must work on a declared family of admissible reached restarts, rather
than just parameterizing one known trajectory. Approximation at finite width,
a population limit, and an exact reduction of the fixed-P candidate are three
different claims.

The current candidate is the chronological shifted-Legendre construction in
MOMENT_CONSTRUCTION.md and RATIONAL_ORTHOGONAL_MOMENT_ROUTE.md, extended to
two learned links in DEEP_CIRCLE_DERIVATION.md. Earlier hypothetical action
closures and rational activity-bin schemes are not the adopted candidate.
Each retained history moment is a neuron vector. The two-hidden version has
2nMP history coordinates; the three-hidden version has 4nMP. Both retain the
actual initialized dense matrices and their actual transposes.

## 1. Exact aggregate criterion

Let S'=F_P(S) be the current finite-width candidate, including its fixed
initialized operators as parameters. Let q=A(S) be a differentiable vector
of proposed aggregates, and suppose the requested outputs factor as
O(S)=R(A(S)). An autonomous aggregate law exists algebraically exactly when

    A(S)=A(T) implies DA(S)F_P(S)=DA(T)F_P(T)

on the admitted states, with the same fixed problem parameters. In that case
define G(A(S))=DA(S)F_P(S); the implication makes G single-valued. Conversely,
any identity DA F_P=G o A implies the condition. If G has unique solutions,
the chain rule and matching initial data identify A(S(t)) with the solution
q'=G(q) on the common existence interval.

Thus equal aggregates must determine the same aggregate velocity. The reduced
state need not reconstruct neurons, individual matrix entries, or the entire
kernel separately. The fibre criterion is imposed on the relevant reached
class; counterexamples on an unrestricted ambient state space do not by
themselves refute a closure on a smaller Gaussian population family.
Regularity, computability and useful complexity are additional obligations.
This is SELF_CONSISTENCY_CRITERIA.md section 4 applied a second time, now to
the finite-P population model instead of to its physical reconstruction.

## 2. Where current population overlaps cease to close

Use two hidden tanh layers, M uniformly weighted samples, and physical
mobilities (n,1,n). All quantities here belong to the current surrogate.
Write H_ak=m_(1,a)^(k), U_ak=m_(2,a)^(k), rho=Q_rms and L=Q_length.
Every finite neuron contraction retains its explicit factor 1/n. The learned
forward action is

    (What2-W0) h_(1,b)
      = -2/(ML) sum_(a,k<P) (2k+1) U_ak (H_ak^T h_(1,b)/n).

This motivates retaining B_(ak,b)=H_ak^T h_(1,b)/n. Its exact derivative is

    Bdot_(ak,b)
      = rho h_(1,a)^T h_(1,b)/n
        -rho/L [k B_(ak,b)+sum_(j<k)(2j+1) B_(aj,b)]
        +H_ak^T hdot_(1,b)/n.

For G_bc=x_b^T x_c/d, the canonical outer-weight equation gives

    hdot_(1,b)
      = -2/M sum_c r_c G_bc
          (1-h_(1,b)^2) .* (1-h_(1,c)^2) .* (What2^T delta_(2,c)).

Substitution exposes the additional aggregate

    H_ak^T [(1-h_(1,b)^2) .* (1-h_(1,c)^2)
                                  .* (What2^T delta_(2,c))]/n.

The moment transport is linear in the retained history orders, but its source
and the differentiated overlap include new nonlinear, jointly coupled neuron
observables. Further differentiation produces further gated products and
operator actions. No identity in the present construction expresses all of
these using its existing finite contraction list on the intended reached
family. This is a missing closure relation, not a proof that no alternative
finite nonlinear aggregate map could work.

Already H_ak^T h_(1,b)/n cannot generally be recovered from the separate means
of H_ak and h_(1,b): the difference from their product is their same-population
covariance. Keeping second moments repairs that specific
omission but does not close their derivatives under this nonlinear flow.
Rational or polynomial neuron equations do not imply a closed hierarchy of
bounded-degree population moments.

There is a separate initialized-operator issue. What2=W0+DeltaWhat2, and
W0 h and W0^T delta remain receiver-indexed fields. They are not common
scalar averages. Initially Gaussian W0 does not justify imposing fresh
Gaussian independence after adaptive reuse. Any aggregate-only solver must
compute the necessary joint action/response statistics from its retained
aggregates. Retaining W0 as an unevaluated oracle requiring hidden neuron
vectors would leave the requested reduction unfinished. FIRST_PRINCIPLES_
DMFT_CLOSURE.md gives the earlier distinction between equal-time covariance
and the additional response/history information.

## 3. Loss and outputs: exact scalar identities without a scalar closure

Write c for the readout, f_a=c^T h_(2,a)/n, r=f-y, and

    H^(ell)_ab=h_(ell,a)^T h_(ell,b)/n,
    D^(ell)_ab=delta_(ell,a)^T delta_(ell,b)/n.

The two-hidden tangent kernel in the original gradient metric (Theta, distinct
from the learned-increment symbol K in MOMENT_CONSTRUCTION.md) is

    Theta_ab=H^(2)_ab+H^(1)_ab D^(2)_ab+G_ab D^(1)_ab.

For the original dense flow, direct differentiation gives

    fdot=-(2/M)Theta r,       lossdot=-(4/M^2) r^T Theta r,
    loss=r^T r/M.

Indeed the readout derivative supplies H2, the middle derivative supplies
H1 D2, and the first-weight derivative supplies G D1 after using the actual
transpose. This is a derivation from the stated block equations, with no
frozen-kernel assumption.

For the fixed-P candidate, the middle weight velocity has its exact defect
E2 from MOMENT_CONSTRUCTION.md, so the correct identities are instead

    fdot=-(2/M)Theta r+e,
    e_a=delta_(2,a)^T E2 h_(1,a)/n,
    lossdot=-(4/M^2)r^T Theta r+(2/M)r^T e.

The kernel is evaluated at the current surrogate weights. At three hidden
layers the same calculation gives

    Theta_ab=H^(3)_ab+H^(2)_ab D^(3)_ab
                        +H^(1)_ab D^(2)_ab+G_ab D^(1)_ab,
    e_a=delta_(2,a)^T E2 h_(1,a)/n+delta_(3,a)^T E3 h_(2,a)/n.

These match the physical two-link defect in DEEP_CIRCLE_DERIVATION.md.
Ignoring e would misstate the proposed model and incorrectly infer automatic
loss monotonicity. It is enough for output closure that the combined drift
-(2/M)Theta r+e be determined by q; Theta and e need not each be separately determined.
For loss alone, only its displayed scalar drift needs to be determined.
Nevertheless, no such factorization is supplied by the current candidate.

A simple finite-width example illustrates why output alone is insufficient
on a broad restart class. Take one sample with x nonzero and y nonzero, P>=1, c=0, zero
learned increment and the same fixed nonzero W0. Both z1=0 and a z1 with
W0 tanh(z1) nonzero give f=0 and loss=y^2. Set moments to their prescribed
initial values, so E2=0. Then

    fdot=2y ||tanh(W0 tanh(z1))||_2^2/n.

It is zero in the first state and nonzero in the second. Their loss derivatives
also differ. This refutes f-only/loss-only closure on that broad class. These
states are not asserted to be two positive-probability canonical Gaussian
initializations or two restarts of its limiting trajectory; the example is
not a no-go theorem for that narrower family or for enriched aggregates.

## 4. Extra structure that would suffice

An exact finite-dimensional family of joint state/action laws, invariant
under this coupled dynamics and regularly parameterized by identifiable
coordinates q, could supply closure.
All required expectations would be computable functions of q, and tangency
of the evolution to that family would determine qdot. The family need not
be Gaussian or linear. Invariance and the correct coupling of both operator
directions must be proved; merely fitting a family at initialization or
postulating Gaussianity of trained neuron states does not establish them.

A finite set of observable functions closed under the dynamics' derivative
operator is another sufficient case. For example, for a particle system
x'=B(q)x+b(q), q containing its mean and covariance, with coefficients
depending only on q, the exact equations are

    mudot=B(q)mu+b(q),    Sigmadot=B(q)Sigma+Sigma B(q)^T.

They follow by averaging x' and differentiating the centered second moment.
This is an illustration of the needed structure, not a model replacement:
the present tanh and reused-operator dynamics have not been put in that form.
Finite nonlinear aggregate closures need not arise from a finite linear span.

For approximation, choose A and a computable G and define its own defect

    eta(S)=DA(S)F_P(S)-G(A(S)).

If G is C-Lipschitz on the relevant connecting region, both systems exist
through T and initial aggregates agree, their integral equations imply

    |q_reduced(t)-A(S(t))|
      <= integral_0^t exp(C(t-s)) |eta(S(s))| ds.

This follows by subtracting the equations, applying the Lipschitz inequality
and the integrating factor (or its norm-regularized version at zeros).
A Lipschitz output readout transfers the bound to outputs. It is a
conditional criterion: bounding eta on the intended family is new work.
Observable closure can be easier than full physical reconstruction because
unresolved variations matter only through their effects on future requested
observables. Full-state or matrix-error bounds are sufficient, not necessary.

There are now two approximation axes: history order P and aggregate resolution
J. The existing estimates concern the former. Neither changing P nor an
accurate fixed-P network supplies a bound for eta. A final comparison with
canonical outputs must account separately for both errors and numerical error.

## 5. Restricted obstruction from the earlier nonanalyticity premise

RESPONSE_STATE_SYNTHESIS.md section 2 already distinguishes a finite state
per population member from a finite total deterministic state. If a specified
target population observable has zero Taylor radius at initialization, it
cannot be exactly produced near initialization by a finite deterministic ODE
q'=G(q), finite q0, with G analytic near q0 and analytic output R(q).

For completeness, real-analytic G locally extends holomorphically to a complex
polydisc. On a smaller closed polydisc its derivative and value are bounded.
For a sufficiently small complex-time disc, Picard integration maps bounded
holomorphic paths into that polydisc and is a contraction in the supremum
norm. Its holomorphic fixed point is the real solution by local uniqueness.
Composing with the analytic readout gives a convergent time series on a
nonzero disc, contradicting the premise. Rational G is analytic wherever
its denominators are nonzero, or after any analytic removable extension.

This exclusion is conditional on nonanalyticity of that particular requested
observable; this note accepts the earlier premise rather than reproving a
canonical population theorem. It does not assert nonanalyticity of every
fixed-P population surrogate, nor exclude nonanalytic scalar laws, singular
initializations, approximation, or a population of simple ODEs. Averaging over
an unbounded random initial state can destroy analyticity, but retaining that
unresolved law is not a closed deterministic finite aggregate vector.

## Evidence, check status and next bottleneck

Exact finite identities and algebraic closure criteria above were derived
from the current study sources. Proposed invariant-law families and small
observable aggregate defects are unproved hypotheses for the neural model.
The analytic exclusion has the explicit inherited nonanalyticity premise.
No general finite-aggregate impossibility theorem is claimed.

The existing campaigns test history compression while retaining neurons and
initial matrices. Their central predictor comparisons are at each model's
own training-loss threshold; some earlier circle results also contain
matched-time observations. They do not test removal of neuron populations.
Numerical success, failure or nonmonotonicity in P does not settle aggregate
closure. No empirical result was reproduced for this assessment.

The next theoretical bottleneck is to propose a finite observable aggregate
map A, including the needed nonlinear/action information, and derive or bound
DA F_P-G(A) on the intended reached family. This is more informative than
assuming that already-computed averages are automatically a sufficient state.

Root read the complete README, MOMENT_CONSTRUCTION, RATIONAL_ORTHOGONAL_
MOMENT_ROUTE, SELF_CONSISTENCY_CRITERIA, AUTONOMOUS_CLOSURE_CERTIFICATES,
COUPLED_CURRENT_STATE_SYNTHESIS, RESPONSE_STATE_SYNTHESIS, FIRST_PRINCIPLES_
DMFT_CLOSURE, DEEP_CIRCLE_DERIVATION and DEEP_CIRCLE_CONTEXT_DIGEST, together
with current shared instructions, docs/README and docs/NOTATION and required
skills. Scoped read-only agents checked aggregate projectability/two-hidden
identities, the three-hidden extension, and empirical claim scope. These are
collaborative internal checks, not independent promotion reviews. No other
study's scientific contents were accessed. The full algebraic check, read
coverage, source hashes, correction record and limitations are retained in
AGGREGATE_CLOSURE_ALGEBRA_CHECK.md. This assessment concerns the cited tanh
construction; a concurrently recorded activation-robustness campaign does
not supply additional evidence for scalar aggregation here.
