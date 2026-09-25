# Aggregate closure: original algebra findings and collaborative audit

2026-09-25. Scoped agent `aggregate_criterion_check`. This is an internal
collaborative check, not an isolated independent review or a promotion review.
The supervisor supplied the task and subsequently the complete root note.
No experiment, numerical computation, external retrieval, other-study input,
maintained-source edit, or Git-index write was performed. The only written
artifact is this assigned report.

## Scope and inputs

The original assignment was to assess whether the current finite
response-moment construction could become finitely many autonomous scalar
aggregate ODEs without neuron populations, for predictions or loss. It
specifically requested projectability, conditional variance, a concrete simple
closure obstruction, and separation of arbitrary restart states from the
Gaussian reachable population family.

All five original scientific inputs below were read completely. The complete
root note was then read for the final audit. Hashes were checked before that
audit; the root-note hash matched the supervisor's frozen input exactly.

| Input | SHA256 |
|---|---|
| `AGGREGATE_OBSERVABLE_CLOSURE.md` | `4471150b831c1294f69f73d40f880ea248bec6d4e6ee8ae6765ad4f8e31d4b6e` |
| `SELF_CONSISTENCY_CRITERIA.md` | `479f3f99b86bce19a1d70e29cf33e288c0ab74bba45a4f19bec2ad77acfedb8d` |
| `AUTONOMOUS_CLOSURE_CERTIFICATES.md` | `6308ca4479eeea7f2b6e41ba7294d607e6f30648359dc81f466eb5e57956be93` |
| `MOMENT_CONSTRUCTION.md` | `5d8bf7fb354fbdef138676ca0ee5d59799a9032e6f6f531ca4650c8e0e5a9025` |
| `RATIONAL_ORTHOGONAL_MOMENT_ROUTE.md` | `677b4d4f7abd5239e1894411c127cf87230ddbde27ec447c2ae56836b7629f23` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

The supervisor additionally supplied, as a premise rather than an independently
verified result, that `RESPONSE_STATE_SYNTHESIS.md` section 2 accepts zero
Taylor radius for the intended canonical population observable and distinguishes
finite state per neuron from finite total scalar state. That source was not
read, since it was outside this agent's authorized scientific inputs.

Required process instructions read: `solve-math-rigorously/SKILL.md`,
`investigate-conjectures/SKILL.md`, and the latter's research-contract,
evidence-ledger and adversarial-audit references. Their respective SHA256
hashes are:

```
9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7
a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de
7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e
9e7573b37cbd954432236bdcb13f6b83b6325e0ff2653a198939842bc81c3a2e
8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501
```

## Original findings

### 1. History order and aggregate dimension are different reductions

`MOMENT_CONSTRUCTION.md` lines 200–207 specifies 2nMP history scalars,
additional neuronal states, and retained W0 actions. Fixed P is finite history
order per neuron, not finite total scalar dimension. The population analogue
still retains neuron-valued functions. `docs/NOTATION.md` lines 92–98 explicitly
distinguishes finite collections of fields from finite scalar dimension.

### 2. Exact aggregate projectability and its statistical test

For a complete candidate state S with S'=F_P(S), let q=A(S) be a differentiable
finite aggregate vector and suppose the desired readout factors through A.
A single-valued aggregate velocity exists algebraically on the admissible
image exactly when

    A(S)=A(T) => DA(S)F_P(S)=DA(T)F_P(T),

with the same fixed problem parameters. Define G(A(S)) by the common velocity.
Then the chain rule gives (A(S(t)))'=G(A(S(t))). If the reduced ODE has unique
solutions and matching initial data, its solution equals A(S(t)) on their
common existence interval. Existence of a regular, computable, efficient G is
an additional issue. Full physical reconstruction is unnecessary for this
output target. These are direct specializations of
`SELF_CONSISTENCY_CRITERIA.md` lines 125–151 and
`AUTONOMOUS_CLOSURE_CERTIFICATES.md` lines 135–141.

For square-integrable v=DA(S)F_P(S) and any candidate b(q), adding and
subtracting E[v|q] yields

    E||v-b(q)||^2
      = E||v-E[v|q]||^2 + E||E[v|q]-b(q)||^2.

The mixed term vanishes by conditional expectation. Positive conditional
variance rejects deterministic exact closure for this aggregate interface
under the sampling law. Zero variance only gives almost-sure measurable
factorization, with no automatic regularity or efficiency. A common autonomous
law across times requires a state law that includes the intended times and
restarts without revealing time as an additional oracle. Separate fixed-time
zero-variance statements can use different predictors. The source explicitly
states these distinctions at `AUTONOMOUS_CLOSURE_CERTIFICATES.md` lines 329–359.

For the one-sample canonical output equation f'=-2(f-y)Theta, the particular
output-only test becomes

    Var(f'|f)=4(f-y)^2 Var(Theta|f),

when all quantities are square-integrable and fixed parameters are understood.
For loss ell=(f-y)^2, ell'=-4ell Theta and

    Var(ell'|ell)=16ell^2 Var(Theta|ell).

Positive derivative error alone does not establish a large output trajectory
error; transient or output-invisible physical errors remain possible.

### 3. Exact prediction and loss identities

Let <u,v>=u^T v/n, G_ab=x_a^T x_b/d, and use M samples with mean squared loss.
For two hidden layers define

    Theta_ab = <h2_a,h2_b>
             + <h1_a,h1_b><delta2_a,delta2_b>
             + G_ab<delta1_a,delta1_b>.

The three terms arise respectively from the readout, middle-weight and first-
weight derivative. In detail, the middle update contributes

    <delta2_a,W2' h1_a>
       = -(2/M) sum_b r_b <delta2_a,delta2_b><h1_b,h1_a>,

and the first-weight update contributes

    <W2^T delta2_a,phi'(z1_a) .* z1_a'>
       = -(2/M) sum_b r_b G_ab<delta1_a,delta1_b>.

Consequently the canonical equations are

    f'=-(2/M)Theta r,
    loss'=-(4/M^2)r^T Theta r.

For the fixed-P surrogate with middle-velocity defect E2, one must add

    e_a=<delta2_a,E2 h1_a>,
    f'=-(2/M)Theta r+e,
    loss'=-(4/M^2)r^T Theta r+(2/M)r^T e.

Theta is evaluated at the surrogate state. These formulas use the physical
normalizations in `docs/NOTATION.md` lines 16–42, the outer equations in
`MOMENT_CONSTRUCTION.md` lines 73–94, and the exact middle defect in that
file's lines 146–159. The one-sample kernel is also explicitly given in
`AUTONOMOUS_CLOSURE_CERTIFICATES.md` lines 169–196.

Determining the full matrix Theta is stronger than determining the combined
prediction velocity: only Theta r and e through their displayed combination
are needed. Thus failure to determine each kernel entry separately is not a
complete output-closure obstruction.

### 4. Differentiating the currently used overlap exposes a new observable

Use H_ak=m1_a^(k), U_ak=m2_a^(k), rho=Q_rms, L=Q_length. For a same-layer
overlap B_(ak,b)=<H_ak,h1_b>, the exact raw moment equations give

    Bdot_(ak,b)
      = rho<h1_a,h1_b>
        -(rho/L)[kB_(ak,b)+sum_(j<k)(2j+1)B_(aj,b)]
        +<H_ak,hdot1_b>.

The outer-weight equation and tanh chain rule give

    hdot1_b=-(2/M) sum_c r_c G_bc
       (1-h1_b^2) .* (1-h1_c^2) .* (W2^T delta2_c).

Hence the final term introduces a gated mixed contraction not supplied by
the original simple factor-action overlap list. These identities were
derived directly from `MOMENT_CONSTRUCTION.md` lines 44–58, 76–84 and 98–109.
This is a missing relation for the displayed aggregates, not a no-go theorem
for every finite nonlinear aggregate map on a possibly smaller reached class.

### 5. Generic restart counterexample and Gaussian limitation

Take n=d=1, x=1, y!=0, tanh, W0=W2=1, and readout c=0. Compare z1=0 with
z1=arctanh(1/2). Both states have f=0 and loss=y^2. In the first state all
gradients vanish. In the second, h2=tanh(1/2), delta1=delta2=0, and

    f'=2y tanh(1/2)^2,
    loss'=-4y^2 tanh(1/2)^2.

For every P>=1, prescribe the usual initial history moments. The study's
exact E2(0)=0 identity makes the same initial derivatives valid for the
finite-P candidate. Even adding rho=|y| and L=1 does not distinguish these
states. This disproves output-only/loss-only closure on this broad restart
class. It does not show two restarts on one prescribed Gaussian limiting
trajectory or an obstruction to enriched aggregates.

There is a qualified finite-width Gaussian corollary, not needed by the root
note. Conditional on a fixed nonzero W0, nondegenerate Gaussian z1 and c have
full support. If a continuous b(f;W0) equalled the continuous canonical initial
output velocity almost surely, continuity and full support would extend that
equality to every (z1,c). But c=0 and z1=0 versus W0 tanh(z1)!=0 contradict
it when y!=0. The same argument applies to a continuous loss-only law and
to a finite-P law initialized by the prescribed moment rule. Gaussian finite-
width variances must be nonzero for this support argument. Concentration in
an infinite-width population limit can remove this obstruction; no positive
limiting conditional variance is established here.

### 6. Conditional analytic obstruction

If the particular requested deterministic observable has zero Taylor radius
at initialization, a finite deterministic autonomous real-analytic vector
field near a finite initial point and an analytic readout cannot reproduce it
exactly near initialization. The local solution and its readout are analytic.
Rational vector fields meet this condition away from vanishing denominators,
or after an analytic removable extension.

This statement assumes, rather than proves, the parent-supplied nonanalyticity
premise for the specified target. It does not establish nonanalyticity for a
fixed-P population observable, and does not reject approximate, nonanalytic
or singular scalar descriptions. An average of analytic solutions over an
unbounded random initial law can fail to be analytic, so a population of
simple rational equations is not covered by this finite deterministic state
argument. `MOMENT_CONSTRUCTION.md` lines 122–128 makes this distinction.

## Final audit of the complete frozen root note

Verdict on hash `4471150b831c1294f69f73d40f880ea248bec6d4e6ee8ae6765ad4f8e31d4b6e`:
the mathematical conclusions and substantive scope qualifications pass this
internal check, with one required local population-typing correction below.
No blocking algebraic or logical error was found in the two-hidden dynamics,
the exact projection criterion, the approximation estimate, the restricted
analytic theorem, or the counterexample's properly qualified conclusion.

### Required local correction

At root-note lines 97–99, `<U,H>` is called a covariance. But that note already
defines U as a second-layer moment and H as a first-layer moment. Their index
sets may have the same finite cardinality, but they are distinct populations:
the population expectation is not canonically a same-space pairing. This
conflicts with `docs/NOTATION.md` lines 46–55. Replace the example by

    <H_ak,h1_b> - <H_ak><h1_b>,

which is the same-layer covariance actually relevant to the displayed overlap.
The root was notified before this report was written.

### Small precision suggestions

For the root-note counterexample at lines 156–168, explicitly choose x!=0,
y!=0, W0!=0 and P>=1. The displayed choice of nonzero first preactivation
requires nonzero input; the initial defect identity uses positive history
order. These choices are available, and initialized Gaussian W0 is nonzero
almost surely, so they do not weaken the intended counterexample.

For an invariant finite-dimensional law family at lines 172–178, use regular
identifiable coordinates q, or explicitly assume a well-defined induced
vector field in the chosen parameterization. Redundant or singular parameters
need not be uniquely determined by tangency alone. The paragraph already says
such a family "could supply closure" rather than asserting a theorem for an
arbitrary parameterization.

### Coverage and actual checks

1. Lines 8–59: checked the distinction between output and state reconstruction,
   non-vacuity restrictions, 2nMP state count, fibre criterion, chain-rule proof,
   uniqueness requirement, and restriction to fixed parameters and the reached
   class. No unjustified impossibility claim is made.
2. Lines 61–111: independently differentiated the learned action and B overlap;
   verified every factor 2, M, n, rho and L, and both sample-dependent tanh
   gates. Checked that adaptive reuse does not justify fresh independence.
   Found the local cross-population covariance notation error above. The note
   treats unclosed terms as missing relations, not a proof of universal failure.
3. Lines 113–168: independently derived the two-hidden kernel, its loss
   normalization, and the middle-defect contribution by chain rule. Also
   derived the displayed three-hidden algebra conditionally on its stated
   block velocities: the extra hidden link contributes H2 D3 to Theta, and
   each link defect contributes <delta_l,E_l h_(l-1)> to e. Verified the
   counterexample and its loss derivative; checked that no Gaussian limiting
   reachability claim is inferred from it.
4. Lines 170–190: checked the affine mean/covariance illustration. Writing
   u=x-mu gives u'=B(q)u, so Sigma'=E[u'u^T+u(u')^T]
   =B(q)Sigma+Sigma B(q)^T. The same coefficients act on every particle;
   otherwise this displayed equation would need additional mixed moments.
   The paragraph explicitly treats this as sufficient extra structure, not
   as a replacement for the neural model.
5. Lines 192–213: set p=A(S), so p'=G(p)+eta(S). For e=q_reduced-p,
   e'=G(q_reduced)-G(p)-eta(S). The stated C-Lipschitz bound yields
   d|e|/dt<=C|e|+|eta| almost everywhere, or via norm regularization at zero.
   Multiplying by exp(-Ct), integrating and using e(0)=0 gives exactly the
   displayed convolution bound. A Lipschitz readout transfers it. Separate
   history truncation, aggregate truncation and numerical error are correctly
   distinguished; no aggregate-defect estimate is claimed from varying P.
6. Lines 215–238: checked the local analytic argument in detail. Shrink a
   complex polydisc around q0 so G and its derivative are bounded, and so the
   analytic readout has a holomorphic extension there. Choose a time radius
   tau with tau sup|G| below the spatial margin and tau sup|DG|<1. Picard
   integration maps holomorphic paths starting at q0 into that polydisc and
   is a contraction in supremum norm. Its holomorphic fixed point restricts
   to the unique real solution. Composition with R therefore has positive
   local Taylor radius. This contradicts the stated zero-radius premise.
   The note correctly excludes singularities, nonanalytic readouts, unresolved
   random-law averages and approximation from this restricted conclusion.
7. Lines 240–269: checked that the mathematical status summary agrees with the
   preceding derivations and identifies a new aggregate-defect obligation.
   Empirical/history provenance in this paragraph is outside this agent's
   source scope and was not independently verified.

### Limits of this check

The three-hidden link-count and physical-formula algebra are consistent with
the root note and general notation, but this agent did not read
`DEEP_CIRCLE_DERIVATION.md` or independently verify that implementation. The
cross-reference to `FIRST_PRINCIPLES_DMFT_CLOSURE.md`, the nonanalyticity source,
the empirical campaign descriptions, and the root's complete-read assertions
were not independently verified. No additional scientific inputs were fetched
to fill those gaps. No existence or convergence theorem for a finite scalar
aggregate closure was proved. No claim about unpromoted material from another
study entered the analysis.

The broad research status is unchanged: the current history projection leaves
population information; a useful aggregate map needs a separate factorization
or aggregate-defect bound on the intended reached family. The checked
counterexample rejects only a simple retained interface over its stated class.

## Final corrected note: complete reread and verdict

The supervisor supplied a revised complete note. This agent read it fully,
not only its changes, and verified its SHA256 directly:

    2c2da60072343a86d804ff7316a1d4ac9618b46d94c3fb25f67675ab437ab34e

Verdict: PASS for this scoped internal mathematical check. No correction
remains required in that frozen version.

The final note replaces the ill-typed cross-layer covariance example with
the same-layer overlap H_ak^T h1_b/n and the product of its separate means.
It explicitly assumes nonzero x, nonzero y, nonzero W0 and P>=1 in the
counterexample. Its invariant-family paragraph now requires regular,
identifiable coordinates. These resolve the reported correction and both
precision suggestions. All finite vector pairings in the final note now show
the factor 1/n explicitly; the earlier shorthand in this report records the
original source-based calculation and means exactly that explicit quotient.

The complete reread rechecked the learned-action formula, both sample gates
in hdot1_b, the overlap derivative, the two- and three-hidden kernel algebra,
the physical-defect contributions to output and loss, the scalar-counterexample
derivatives, the projectability/uniqueness argument, the defect convolution
bound and the analytic Picard argument. The normalization edits preserve each
of these identities. The distinctions between broad restart states and the
initialization-generated population family, between exact and approximate
closure, and between finite history order and finite scalar state remain intact.

The affine illustrative sufficient case is read as q=(mu,Sigma), with B and
b functions of those retained statistics; alternatively any additional q
coordinates require their own closed equations. The displayed mean and
covariance identities are correct under either reading, but unspecified extra
coordinates would not by themselves establish a closed complete q system.
This intended reading is sufficient for the paragraph's illustrative purpose.

This final verdict does not expand the actual input scope. In particular,
the note's empirical history and the external-to-scope nonanalyticity source
remain unverified here. No concurrent activation-research artifacts were read.
The root note appropriately keeps its assessment within the cited tanh
construction. No new experiment or theoretical investigation was added during
the correction check.

## Additional scoped check retained by root

Root read this entire report, the complete root note and both other agents'
complete final responses. After the algebra checker's write ownership ended,
root retained the following final message from `aggregate_deep_check` verbatim
(formatting converted only to plain Markdown). It checks the same final source
hash. This is additional collaborative evidence, not a promotion review.

> **Verdict: PASS within the assigned mathematical scope.**
>
> Checked the complete frozen `AGGREGATE_OBSERVABLE_CLOSURE.md`, SHA256:
>
> `2c2da60072343a86d804ff7316a1d4ac9618b46d94c3fb25f67675ab437ab34e`
>
> The three-hidden-layer kernel and both defect contributions have the correct normalization, signs, and transpose semantics:
>
> Theta_ab=H3_ab+H2_ab D3_ab+H1_ab D2_ab+G_ab D1_ab,
>
> fdot=-2 Theta r/M+e, e_a=(delta2_a^T E2 h1_a+delta3_a^T E3 h2_a)/n.
>
> The corresponding loss identity is correct.
>
> The note correctly distinguishes:
>
> - An exact observable identity from autonomous evolution of its scalar contractions.
> - History truncation from removal of neuron populations.
> - Failure of a particular aggregate list from impossibility of every finite nonlinear representation.
> - Finite-width, population-limit, exact-reduction, and approximation claims.
> - Conditional invariant-family constructions from established structure of the present model.
>
> The aggregate fiber criterion, differentiated-overlap calculation, same-population covariance explanation, and conditional aggregate-defect estimate are mathematically sound. The initialized matrices remain genuine coupled forward/transpose operators; their Gaussian initialization does not justify fresh independence after reuse. The broad-state counterexample correctly rejects output-only and loss-only closure on its stated class without claiming a canonical-population no-go theorem.
>
> The earlier corrections were verified: normalized finite contractions now display 1/n; the covariance example uses two coordinates from the same layer; and the counterexample specifies nonzero input, nonzero label, nonzero initialized operator, and P>=1. No further correction is required within scope.
>
> The phrase “Gaussian population family” is interpreted here as the family generated by the prescribed Gaussian initialization. The note elsewhere explicitly declines to assume trained-state Gaussianity.
>
> This was a collaborative internal check, not an independent promotion review. Scientific inputs were limited to the complete frozen note, `DEEP_CIRCLE_DERIVATION.md`, `DEEP_CIRCLE_CONTEXT_DIGEST.md`, `DEEP_CIRCLE_RESULTS.md`, `DEEP_CIRCLE_REPORT_CHECK.md`, and `docs/NOTATION.md`. The inherited nonanalyticity premise and references outside those inputs were not independently verified. No experiments, external retrieval, or writes were performed.

Root verified the mathematical normalization in that message directly against
the complete deep derivation. Its source SHA256 is
`17ffa7efe44d588a47b8f566c5cbdc72199e012ae058bab232427e6685203bd9`;
the context digest SHA256 is
`827c829e2f25085813b72cf8cd0e759b6792866ae0a57c17a6370a77d9028816`.

## Empirical scope audit retained by root

Agent `aggregate_evidence_scope` read all eleven assigned reports completely:
MOMENT_RESULTS, MOMENT_INDEPENDENT_CHECK, FACTOR_CONTROL_RESULTS,
FACTOR_CONTROL_CHECK, MNIST_RESULTS, MNIST_CHECK, MNIST100_RESULTS,
MNIST100_CHECK, DEEP_CIRCLE_RESULTS, DEEP_CIRCLE_CHECK and
DEEP_CIRCLE_REPORT_CHECK. No raw array, code, outside study, external source,
experiment or write was used. Root read the complete returned findings.
This was a source-scope audit, not fresh empirical reproduction. Its findings:

- No campaign tests width-independent scalar aggregate evolution. Neuron
  states, neuron-indexed history arrays and dense initialized matrices remain.
  MNIST100_CHECK:64 and DEEP_CIRCLE_RESULTS:223 give the relevant state counts.
- The principal comparisons use each model's own loss crossing. Earlier
  circle experiments also have finite sampled common-time predictions;
  this does not give a continuous-time supremum guarantee. Sources:
  MOMENT_RESULTS:72, MOMENT_INDEPENDENT_CHECK:168, MNIST_CHECK:123,
  MNIST100_CHECK:131 and DEEP_CIRCLE_RESULTS:108.
- The factor comparison's 29 resolved wins concern the specified directly
  trained factor flow with W0 retained. They establish no scalar aggregation
  result; one cell is capped and inconclusive. Sources:
  FACTOR_CONTROL_RESULTS:17,79 and FACTOR_CONTROL_CHECK:143.
- Original circle lifted runs needed refinements after activation-drift
  failures. MNIST1000 P2/P3 fail the frozen relative numerical gate;
  MNIST100 passes and resolves a small P3 worsening. Deep-circle P2/P3
  improve on P1 in all five tasks but P3 is worse than P2 on both alternating
  tasks. These results neither prove monotone order convergence nor test
  removal of neuron populations. Sources: MOMENT_INDEPENDENT_CHECK:225,476;
  MNIST_CHECK:104; MNIST100_CHECK:114; DEEP_CIRCLE_RESULTS:120;
  DEEP_CIRCLE_CHECK:253,292.
- The deep report's rank bound concerns each learned increment. The bounded
  report check predates complete replay; the later implementation audit
  records replay after one-bit archive recovery with no changed scientific
  predictions. Sources: DEEP_CIRCLE_REPORT_CHECK:8 and
  DEEP_CIRCLE_CHECK:192.

The mathematical identities and conditional criteria in the frozen assessment
are internally checked over their declared scopes. Aggregate closure for the
neural model remains open, and the canonical zero-radius claim remains an
inherited premise. Nothing in these checks promotes the study results to
established material or authorizes additional computation.
