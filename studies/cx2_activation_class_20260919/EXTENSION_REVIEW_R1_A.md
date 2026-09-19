# Independent complete review A — extension R1

**Verdict: ACCEPT the complete frozen result in its stated scope.** I found
no scientific blocker, missing dependency needed by the new claims, or
implementation defect requiring correction. This is an internal scientific
and implementation verdict, not promotion or approval to change established
material. The explicit exclusions in REVISED_RESULT.md remain exclusions;
in particular this verdict does not assert the bounded-C1,1 nonatomic fitting
extension that the packet leaves open.

## Scope, independence, and integrity

The assignment was EXTENSION_R1_ASSIGNMENT.md. My scientific input was only
the packet at
`data/generated/cx2_activation_class_20260919/extension_r1_inputs`, its
manifest, and required skills/process instructions. I read all thirty
manifest-listed files completely: 16,155 lines, including all candidate
proofs, older partial dependencies, seven frozen foundation excerpts,
notation, implementation, tests, and the entire repository Python import
closure. Truncated tool output was repaired by reading the omitted ranges.
I did not read author startup/history, live proof or implementation files,
other studies, or other reviewers' reports. No input file or Git state was
modified.

I personally read solve-math-rigorously and investigate-conjectures and the
latter's applicable research-contract, adversarial-audit,
decisive-experiments, and evidence-ledger references. A scoped helper read
the frozen numerical note, plan, closure proof, adapter, tests, and all ten
frozen `code/pde` modules for an additional static implementation audit. It
did not execute tests, read outside that scope, or edit anything. I also
read those files myself and checked the mathematical dependencies outside
that helper's scope. This report's complete-scope judgment is mine.

Manifest SHA-256, verified before and after:

`b7ea60fc3c0335530c4d06e39ea96cc7ff1e82f2fbb86f79a53b3344a6753990`.

Every listed file's SHA-256 and line count agreed with the manifest both
before and after the review. The per-file values are recorded below and in
my scratch `hashes_before.json` and `hashes_after.json`. My scratch is
`data/generated/cx2_activation_class_20260919/extension_review_r1_a/`.

## 1. Model, claim boundaries, and reference solution

The assembly consistently uses normalized inputs `u=x/sqrt(2)`, the same
fixed activation in both hidden layers, initial stored variances
`(1,1/n,1/n²)`, mobilities `(n,1,n)`, and the unhalved probability-weighted
squared loss. Population initial readout zero is a limit assertion; the
finite bridge retains the actual random readout. The persistent initialized
action has its actual adjoint. Only the learned increment is claimed to be
Hilbert–Schmidt. Strong convergence and uniqueness refer to the stated
full-row L2/HS/readout state on the canonical carrier, not convergence in
operator norm between different widths.

I checked REFERENCE_PROOF.md, the activation-foundation clock construction,
and the reference use in REVISED_RESULT.md. The signed exchange symmetry
does not require oddness of the activation. With `h=(H1-H2)/2`, feature time
gives `c_s=h` and `c_ss=J J* c`; convexity of `||c||` yields
`||h||² >= q0`. Hence the physical-time equation gives
`L_*(t) <= exp(-4 q0 t)`. Nonaffinity implies nonconstancy; the initialized
two-coordinate covariance has a strictly positive independent component,
so the displayed `q0` is strictly positive. Thus the reference risk at
`T_phi=log(8)/(4 q0)` is at most `1/8`, leaving the needed strict margin
for perturbation. The argument allows nonzero activation mean, nonodd
functions, nonmonotonicity, and flat gates.

The bounded reference endpoint calculation is also valid. Integrating the
decaying residual first bounds `c` in L-infinity, then `K` in HS, then `w`
in L2. Their integrable velocities give an actual strong endpoint. The
displayed prediction difference estimate is uniform over the circle and
gives the stated exponential reference endpoint bound. At the separately
fixed enlarged horizon the two errors `1/8` and `1/16` sum to `3/16<1/4`.
The near-reference theorem is available at every fixed finite horizon, so
using this enlarged horizon is justified. This does not create a
changed-law infinite-time theorem or a hierarchy-order rate.

The older partial files retain their narrower conditional statements. The
new onset/pair/C2 constructions supply the strong target and tails needed
by those conditional closure and finite-width arguments; they do not
silently remove the older hypotheses. The frozen tanh-specific dependencies
also contain broader historical statements, but the new activation result
uses its own reference margin rather than importing an unspecified tanh
numerical fitting estimate.

## 2. Full-class all-Borel onset

I accept ONSET_EXTENSION.md's claim for each fixed nonaffine globally
C1,1 activation with bounded derivative, including unbounded activations.
The positive time is uniform over all Borel laws on
`S1 × [-1,1]` in normalized coordinates, and is activation dependent.

The construction does not start by assuming its limiting solution. The
common raw ball and its time bound control all finite steps. SOURCE_PROOF.md
and the frozen source foundations provide the small-time response estimate
for smooth approximants with constants depending on value/first-derivative
bounds and the Lipschitz constant of the first derivative. At each fixed
finite program, mollification is removed through value and
first-derivative convergence; the response tails survive by Fatou. There
is no passage to a limit in second derivatives at their discontinuities.

The transport estimate properly treats the two potentially unbounded
reference multipliers separately: readout in the upper derivative product,
and backward field in the lower gate product. The resulting cutoff
coefficient is linear in `1+R`; the source tail errors are additive.
Consequently Gaussian tails defeat the cutoff amplification. The common
carrier, finite unions of rational programs, and subsequent completion
produce a strong Cauchy family in the full state norm as both law and mesh
are refined. Continuity of the Banach-valued integrands passes the exact
integral equation. The reference-only version gives uniqueness and law
continuity without assuming tail estimates for an arbitrary competitor.

The limiting tail statement is an integrated law statement, obtained using
bounded truncations of the exponential. It is not incorrectly promoted to
an exponential moment of a supremum over all inputs or times. These
integrated tails suffice for the later transport and hierarchy estimates.
The energy identity and full-row solution regularity have the required
strong interpretation.

The full represented C-H3 family is within this domain, with the prescribed
fixed rational parameters and rotation. Its cross-input bound does not
provide a general fitting claim. The nonlazy subfamily instead uses the
weighted initial-variation result at the nonparallel central two-atom
member and then law continuity. This distinction is maintained.

## 3. Bounded C1,1 pair theorem: preferred raw-Euler proof

I audited COMMUTATOR_RESPONSE.md in full, with Section 9 as the preferred
construction and Sections 1–8 as its separately assessed alternative.
The following are the decisive checks for acceptance.

* The raw bounds on residual, readout, learned increment, and action norm
  precede the source cap. They are uniform over the smooth approximants
  when the common bounds on `phi`, `phi'`, and `Lip(phi')` are fixed.
  They do not use the desired response estimate.
* The artificial tangent program is explicitly placed on the actual base
  trajectory and action. Its lower tangent coordinates, hidden variations,
  upper/readout variations, and middle variation use the true bounded base
  gates. Its finite-width norm recurrence is an L2/HS argument using the
  actual operator and adjoint. No unsupported Lp bound for that operator
  or division by a possibly zero gate is used.
* The centered independent probe makes tangent quantities odd and base
  quantities even. Mixed contractions vanish. Conditional finite-width
  operator bounds justify the corresponding limiting centered products;
  this is not merely a verbal parity assertion. The surviving learned
  action terms give the stated tangent source skeleton.
* The derivative convention freezes scalar coefficients and laws and
  differentiates explicit named-source expressions. Formal source slots
  remain present at zero variance and at singular covariance. Neither a
  covariance inverse nor deletion of a zero innovation is used in this
  analytic identification.
* Different probe insertions have different Gaussian covariance data, but
  the derivative recursions determining their response coefficients use
  the same fixed base law and gates. This supplies the common artificial
  response rows needed by the comparison. The coefficient of the fresh
  upper probe solves the same pulse recursion, so extraction by
  `E[e d_tan]` is the claimed beta entry. The finite-width L2 bound then
  supplies a cap for those artificial rows independently of the real cap.
* For `V_a(w)=phi'(w.u_a)u_a`, the cross bracket is bounded by
  `2 |u1.u2| Lip(phi') ||phi'||`. The preferred raw-Euler transport keeps
  the extra after-Jacobian insertion term. For each smooth approximant,
  the step defect has the stated bracket part and a term controlled by
  its finite `S=||phi'''||`. Summing uses
  `sum h_j² s_j² <= h_max sum h_j s_j²` in the required moment norms,
  giving the normalized error
  `C_B (|u1.u2| + (1+S) h_max)`. The constant multiplying the angle
  and the causal Volterra sum is independent of S.
* True and artificial derivatives are compared on the same base. The
  argument therefore does not subtract second derivatives at two nearby
  trajectories. The final recursion is causal: the new real row is
  bounded using earlier capped rows and the independently bounded
  artificial row. Choosing the cap with slack, then the angle, then the
  sufficiently small mesh closes the induction without self-reference.

The order of these choices matters. The angle neighborhood is fixed
independently of smoothing. The mesh tends to zero separately for each
smooth activation; its threshold may depend on S. Only after that limit
is the activation smoothing removed using the common value/first-derivative
bounds and uniform tail estimates. Nothing in the argument requires a
uniform bound on the mollifiers' third derivatives or convergence of their
second derivatives. The passive-query formula in Section 9.1 supplies
uniform-in-query marginal tails without requiring a small bracket between
a passive direction and each training direction.

I found no defect in the alternative controlled-step construction in
Sections 1–8 either. Its lower controlled flow uses the same frozen base
controls, its variation identity gives the stated bracket term, and the
fixed-program differentiation and consistency have the required moment
envelopes. The preferred proof does not depend on treating that controlled
flow as an actual raw-Euler update. In particular, acceptance of the
preferred route does not hide a failed consistency step in the alternative.

Rotation reduces the nearby two-atom geometry to the small cross-angle
case. Strong completion, uniqueness, continuous dependence, and the
reference `1/8` margin then yield the stated `<1/4` pair-fitting theorem.
No nonatomic bounded-C1,1 fitting theorem is inferred from this argument.

## 4. Bounded C2 supported-law theorem

BOUNDED_EXTENSION.md supplies the additional half-mass binary Borel-law
extension under continuous bounded second derivative, including nonatomic
laws in fixed sufficiently small caps. I checked its clock anchor,
differentiated consistency, local-modulus comparison, cap closure, and
Borel completion rather than assuming that C2 regularity supplies a global
modulus or a third derivative.

The orthogonal clock source bound is established independently of the raw
source comparison. Its transformed flow needs no inverse gate. The
differentiated scalar consistency estimate uses a compact-set modulus of
`phi''`; the argument splits compact values from tails before letting the
mesh shrink. For comparison between trajectories, the displayed modulus
bound first restricts both arguments to a compact interval and their
difference to a small threshold, with L2/tail estimates controlling the
complement. Taking the infimum in those cutoffs gives a modulus tending
to zero. This is valid for bounded continuous `phi''` even when it is not
uniformly continuous on the whole real line.

The normalized response pulses and source comparison yield a causal
Volterra bound. The independently controlled clock path first anchors
the raw orthogonal path, after which a small law displacement closes the
changed-law cap. The neighborhood is fixed before the mesh, finite-law,
hierarchy, or numerical limits. Finite approximations supported in the
same two caps preserve label masses; the strong transport completion
therefore gives the full Borel statement and its passive tails.

The explicit fitting estimate has strict slack: the reference residual
norm is at most `1/sqrt(8)` and the chosen perturbation leaves its square
strictly below `1/4`. A fixed sufficiently small rational radius with
`2 rho <= eps_phi` puts the represented orthogonal arc family inside the
caps. Nondegenerate intervals are genuinely nonatomic; numerical collapse
of a tiny radius is separately reported and is not a mathematical change
of the target law.

The recorded bounded-C1,1 obstruction concerns the earlier comparison
route and within-cluster brackets at jumps of curvature. The packet
correctly retains this as the remaining nonatomic gap, not a contradiction
of the new two-atom route or a counterexample to the neural dynamics.

## 5. Activity, observations, finite GF/GD, and data sequences

Weighted C.3 applies at the stated central/reference initial laws because
the first rows are nondegenerate Gaussian, the two directions are
nonparallel, the weights and mobilities are positive, and the relevant
labels are nonzero. Its positive leading squared-displacement coefficient
is of order t². Choosing one early positive time before perturbing gives
a fixed positive same-row RMS margin in each layer. The source/strong
continuity results preserve that margin in a smaller neighborhood. No
claim about activity at the later fitting endpoint is needed.

The affine-fit assertion uses the exact least-squares expression
`Var(phi(Z)) - Cov(Z,phi(Z))²/Var(Z)`. At a nondegenerate Gaussian input
it is positive for a nonaffine continuous activation. L2 continuity of
the preactivations and their activated values preserves the denominator
and these moments on the asserted initial interval and neighborhood.

The finite bridge compares actual finite trajectories to fixed proof
proxies before removing proof cutoffs and meshes. Its errors include the
small but nonzero actual initialized readout. Finite-dimensional C1,1
vector fields have the required local regularity; the energy estimate
controls finite GF continuation. For simultaneous raw GD, the stopped
raw estimates control all stages and the `eta_n -> 0` defect; a discrete
energy identity or arbitrary-step loss decrease is not assumed.

The data-law extension is a transport term on the same raw ball with tails
kept on the fixed comparison proxy. It permits deterministic convergent
data-law sequences and the stated independent random in-probability
version, without a sample-count/width growth relation. In the pair theorem
the approximating finite data laws need not themselves be two-atomic;
the constructed nonlinear target remains the fixed admitted two-atom law.
There is no claimed uniform finite-width time bound as the target horizon
tends to infinity.

Whole-circle predictions follow from the uniform input Lipschitz bound
and finite nets. Fixed admissible joint observables use the same population
rows for initial/current pairs, include both action directions, and retain
the required second moments. They are not replaced by products of separate
marginal laws. Strict fitting and endpoint margins transfer the population
inequalities to the stated finite-GF/GD high-probability conclusions.

## 6. Dense hierarchy and finite numerical consistency

The activation-independent smooth dictionary is genuinely dense. Its
rational cylinder trigonometric words are total on each finite collection
of initialized coordinates; bounded approximations such as
`R tanh(V/R)` recover unbounded L2 words. Including both action orientations
and using the actual adjoint produces the reducing pair of generated
spaces. The reference-only comparison first establishes that the strong
target stays in these spaces; invariance is not used circularly to prove
its own approximation.

Ridge normalization retains duplicate columns and yields positive
contractions converging strongly to the identity. A fixed earlier finite
span gives the vanishing ridge error as the cofinal prefix grows. The
filtered initialized actions and their adjoints converge on compact target
sets, and the filtered increment velocities converge in HS. There is no
claim of operator-norm convergence. Fixed-order finite dynamics have the
stated gradient energy estimate and continuation bounds.

CLOSURE_PROOF.md's error propagation uses reference tails for both readout
and backward field. Its linear-cutoff estimate and Osgood step give
vanishing errors over the whole fixed horizon. The compact-target
approximation defect is exactly the one supplied by the dense contractions.
The onset and the two substantial-training constructions meet the S/E
interface required here, so the conditional hierarchy composes with each
new target on its precise domain.

The initialized Gaussian compiler uses one complete finite union of words,
source queries, and opposite-orientation responses. Derivatives freeze
response numbers and covariance data and differentiate named-source
expressions. Uncentered operand Grams are correct even for nonzero means.
Positive covariance regularization is an approximation parameter; it is
removed in its stated limit, not identified with the exact singular source
law at finite resolution. Numerical Cholesky keeps every positive
regularized direction and rejects unresolved pivots. Forward contraction C
defines the runtime action, and the runtime reverse action is its transpose;
the separate reverse estimate is only a diagnostic.

I also checked the supplied finite-program Gaussian law, deterministic
Halton/Box–Muller moment and tail argument, and rational elementary-function
consistency in the frozen foundations. Fixed-dimensional integration is
justified for the admitted envelopes. Prefix compatibility matters when
the finite source dimension grows. These statements supply the explicit
initializer, not an unproved exact-Gaussian sampling oracle.

The numerical limits have the correct order, written with the outermost
first:

`lim_N lim_epsilon↓0 lim_Q lim_P lim_input-quadrature lim_h↓0 lim_precision`.

The exact finite-law case omits input quadrature. Literal finite arithmetic
additionally requires pure locally uniformly consistent evaluators of
`phi` and its actual derivative. Regularity alone does not assert their
computability. The implementation's optional ordinary floating-point
backend does not supply an unlimited precision axis; the explicitly
refinable backend and evaluator contract supply that axis. The proofs
establish no arbitrary diagonal, order rate, practical cost-to-tolerance
bound, or certified fixed-run trajectory error.

## 7. Implementation correspondence and resource claims

The frozen adapter at `activation_closure.py` implements the stated
cofinal bounded-word prefix through code `16N` and ridge `2^-N` without
dropping duplicates. It always uses the complete initialized source
compiler; it does not reuse the inherited tanh polynomial fast path for
a general activation. The inverse-lower-Cholesky transforms and all action
transposes match the formulas.

I checked the fields and all three weighted velocities against the
population equations, including the factor of two from the unhalved loss,
the placement of each population weight, and the single use of each data
weight. Heun computes simultaneous stages of this autonomous vector field.
Initial/current paired fields share frozen marks and reconstruct the
initial upper field with D, while current fields use M. Callback copies
prevent caller-visible mutation or reused-buffer aliasing; validation
checks shape and finiteness. As documented, callback validation cannot
verify the derivative's semantic correctness or purity.

Restart preserves intended float, Decimal, and rational working scalars
exactly and binds the activation descriptor. It stores current joint marks,
dynamic state, fixed action, data and metadata, without a trajectory tape
or an elapsed-step-dependent source history. The complete mathematical
hierarchy restart applies to reached compatible states, not arbitrary
sequences of finite arrays.

The state scalar counts and the leading field/RHS costs agree with the
arrays and matrix contractions. Initialization retains finite-program
workspace only while needed; limits reject oversized requests rather
than silently changing the dictionary. Evaluator cost, temporary stage
workspace, initializer workspace, metadata, and growing scalar bit sizes
are separately qualified. Thus the claims are storage/algebra counts for
specified resolutions, not promises of feasible computation at a chosen
accuracy. No neural-width parameter is hidden in the runtime state.

## 8. Independently reproduced evidence

I read NUMERICAL_VALIDATION_PLAN.md and the complete test before executing
the supplied suite exactly once from the frozen packet root. The invocation
was:

```text
timeout 120s python -B studies/cx2_activation_class_20260919/test_activation_closure.py
```

The specified environment was:

```text
PYTHONPATH=code:studies/cx2_activation_class_20260919
PYTHONDONTWRITEBYTECODE=1
OPENBLAS_NUM_THREADS=1
OMP_NUM_THREADS=1
MKL_NUM_THREADS=1
ACTIVATION_NUMERICS_SCRATCH=/home/amir/Codes/PDE/data/generated/cx2_activation_class_20260919/extension_review_r1_a
```

The entry point additionally applied its 120-second CPU and 1-GiB
address-space limits. Result: **8 tests, 0 failures, 0 errors, status 0**.
Suite elapsed wall time was 1.069265 seconds; wrapper wall time was
1.212993 seconds; recorded process CPU was 1.148641 seconds and peak RSS
was 38,896 KiB. Environment: Python 3.10.12, NumPy 1.26.4, Linux x86-64.

The eight reproduced checks were:

1. Cofinal dictionary prefix, duplicates, and resource rejection.
2. Nested complete source response and frozen derivatives.
3. Generic initialization and activation independence.
4. All gradients, energy contraction, and actual adjunction.
5. Dense finite-network normalization at the supplied state.
6. Same-row pairs, simultaneous Heun map, and restart.
7. Precision refinement and law-scope metadata.
8. Callback shape, finiteness, ownership, and activation binding.

The full log, exact command/environment record, source hashes, and
validation record are retained in `suite.log`, `execution.json`, and
`validation_record.json` in my assigned scratch, alongside the test-created
restart files and integrity records. No training, parameter sweep,
trajectory-accuracy study, or empirical campaign was run. The tests support
the bounded algebraic/execution claims, not the mathematical existence or
convergence theorems; those were assessed from the proofs.

## Required corrections and final decision

**Required scientific corrections: none. Required implementation corrections:
none. Missing scientific inputs needed for the accepted claims: none.**
I have no optional exposition request that needs to hold up this packet.

The complete result is accepted as frozen: full-class all-Borel onset;
bounded-C1,1 perturbed-pair substantial training; bounded-C2 supported
Borel/nonatomic substantial training; the stated activity, nonaffinity,
reference endpoint, finite-GF/GD and observation consequences; and the
dense autonomous hierarchy with its qualified executable numerical limits.
The explicitly open or excluded extensions remain outside this decision.
Any subsequent scientific or implementation correction changes the packet
and requires fresh complete reviews under the assignment's rule.

## Per-file integrity record

The following SHA-256 values and line counts matched the manifest before
and after review. Paths are relative to the frozen packet root.

| Frozen file | Lines | SHA-256 |
| --- | ---: | --- |
| `code/pde/__init__.py` | 26 | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/finite_network.py` | 363 | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/gaussian_moments.py` | 114 | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/observable_arithmetic.py` | 230 | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `code/pde/observable_compiler.py` | 528 | `1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac` |
| `code/pde/observable_fixed.py` | 223 | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `code/pde/observable_initialization.py` | 397 | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `code/pde/observable_laws.py` | 472 | `6fb38416ce02ca77aae0392201927eb9aeba5c672ebe774181822dfb805d0503` |
| `code/pde/observable_solver.py` | 350 | `711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605` |
| `code/pde/observable_words.py` | 217 | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `dependencies/activation_foundation.md` | 1996 | `58e7dc1d8cf7abd991fcba7e305d084bfb522795cc5b9aee443c183fe4fa1c03` |
| `dependencies/gaussian_foundation.md` | 542 | `8a8dbe6a31a51d3f73c999b75c75dcade76b3d533c8901a062c66587776cdd0a` |
| `dependencies/law_construction.md` | 1288 | `87e17770daea404d80da2c8a3e45cb5925f8110527660f2d7e70b08d3a92e0a1` |
| `dependencies/numerical_proof.md` | 815 | `ac29b96116d1e6069b0eee190e07359b8fe156567e8fc21abbf7d2dfdc1d4e83` |
| `dependencies/onset_law_proof.md` | 567 | `d205fbd13d1fe8dd97876d0a7ffa4f502380216a15a29bd4e2d016a2622c90b1` |
| `dependencies/source_and_completion.md` | 1384 | `10851308aa9a132214f828df24a99225b15f5d1798e187fbddc207fae08ff411` |
| `dependencies/supported_law_proof.md` | 1283 | `1046d356e89e34c829354eb633e246594ed65910b03c9ec43f88a7dc1bdc2e8e` |
| `docs/NOTATION.md` | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `studies/cx2_activation_class_20260919/BOUNDED_EXTENSION.md` | 690 | `4cf3bce600d5518defd67225329d0f52720babd15e3d86984aab47a5187e09a2` |
| `studies/cx2_activation_class_20260919/CLOSURE_PROOF.md` | 741 | `15270cb49004fe359c49722508ad0c96695d8ddb2f939a66b84939a3be0f0d6c` |
| `studies/cx2_activation_class_20260919/COMMUTATOR_RESPONSE.md` | 887 | `632a158323c53dfaa50034a08855c9b51cc19c29af889e3176d160a101005625` |
| `studies/cx2_activation_class_20260919/NUMERICAL_EXTENSION.md` | 276 | `dd3dfeeedbec2381d1d33a8fc80a8e5086e7d3cd08243b399754a64f03c23dd3` |
| `studies/cx2_activation_class_20260919/NUMERICAL_VALIDATION_PLAN.md` | 68 | `edb4e15ff0b079ac356556460cd44765a440fcacd7a24a9810c36ba4436954fb` |
| `studies/cx2_activation_class_20260919/ONSET_EXTENSION.md` | 394 | `d5853c29a24e3075053ce0629e5aed63ea7f259107118f36d97f5805684b4593` |
| `studies/cx2_activation_class_20260919/PARTIAL_RESULT.md` | 230 | `a47d85ca451bfe1d70e44fad4cb695d5011445a19b0ab9f182e8b5bf4293cd1b` |
| `studies/cx2_activation_class_20260919/REFERENCE_PROOF.md` | 430 | `535d4576ac2de2711bcacbed64d5864d2207a54eb1b7bc84bc668e8402395be7` |
| `studies/cx2_activation_class_20260919/REVISED_RESULT.md` | 252 | `c7fbacd698236a800e737d0732d6a183f8cd96314a510df72d4e9aa218c5128d` |
| `studies/cx2_activation_class_20260919/SOURCE_PROOF.md` | 651 | `4b944a9c4bfe290a4b294a3586d1c67607ac776926482beeb8fa832c2613ceff` |
| `studies/cx2_activation_class_20260919/activation_closure.py` | 395 | `49b385deb1d1d700a168f5d17025037bf647a9f6e03b0f6dd85ede10284ccec3` |
| `studies/cx2_activation_class_20260919/test_activation_closure.py` | 248 | `6cc53274173f8bd376a5da904070eb5066843980bb04a84de0bc131f2f16deb3` |
