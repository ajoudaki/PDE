# Independent complete scientific review R1-A

**Verdict: ACCEPT, within the exact scope of THEOREM.md.**

I found no material mathematical or implementation defect requiring revision in
the frozen candidate. This acceptance covers all five numbered conclusions,
the complete proof chain, and the numerical realization with its stated
iterated limits. It is not an acceptance of an arbitrary simultaneous limit,
a growing-dimension result, a finite-resolution accuracy certificate, or a
cost-to-accuracy claim. It supplies scientific review, not permission to
promote or change maintained material.

## Independence, inputs, and completeness

I reviewed the neutral assignment without reading the study README, study
history, corrections, previous reports, commits, other studies, or another
reviewer's findings. I read the required `solve-math-rigorously` and
`investigate-conjectures` skills and applicable research-contract,
adversarial-audit, and decisive-experiment instructions. I did not use an
author status or a successful test as a premise of the proof.

The input boundary is `REVIEW_INPUTS_R1.json`, supplemented during this
review by the supervisor-authorized
`REVIEW_DEPENDENCY_SUPPLEMENT_R1.json`. The original manifest contains 30
files, and the supplement supplies the three transitive package-import files
`code/pde/__init__.py`, `finite_network.py`, and `gaussian_moments.py`.
The supplement did not replace or change a scientific candidate. All 33
file hashes matched their manifests. Initial verification of the original
manifest preceded scientific reading; the supplemental hashes were checked
when supplied. Complete recorded before/after verification is retained in
this review's scratch directory.

My complete candidate coverage was:

| Unit | Coverage |
| --- | --- |
| `THEOREM.md` | Entire statement, model, quantifiers, all conclusions, limits, and architecture |
| `REFERENCE_PROOF.md` | Entire proof, including signed symmetry, clock, global continuation, initialized reused-action calculation, quantitative activity, nonaffinity, and finite interpretation |
| `PERTURBATION_PROOF.md` | Entire proof, P1–P45, including the independent reference anchor, both cap transfers, explicit radius, strong completion, uniqueness, and query tails |
| `FINITE_CAPTURE_PROOF.md` | Entire fixed-proxy GF/GD and observation argument |
| `CX1_CLOSURE_PROOF.md` | Entire hierarchy, density, enrichment, closure, numerical limit, implementation, and cost argument |
| `ASSEMBLY_PROOF.md` | Entire margin transfer, final radius, edge cases, and assembly |
| `cx1_closure.py`, `test_cx1_closure.py` | Every function, test, imported interface, state representation, and output path |
| `check_reference_constants.py`, `validate_trajectories.py`, `VALIDATION_PLAN.md`, `VALIDATION.md` | Complete code and declarations; numerical evidence kept distinct from proof |

I read the following complete maintained mathematical units required by the
candidate, rather than treating their headings as black-box guarantees:

- `special_data_limits.md`, III.F.1–11: finite Gaussian programs, common
  carriers, singular extension, actual adjunction, HS ranks, and scalar calculus.
- `global_nonlinear.md`, A.1–A.4; B.1; C.3 including the weighted correction;
  C.4.1; C.4.5.1 and C.4.5.2 including the exact rational certificate;
  C.4.7.1–C.4.7.5; C.4.7.8; C.4.7.9; and complete C.4.7.10 parts A–D.
  I also read the complete finite Gaussian calculation in Section 3.
- `docs/NOTATION.md` and `docs/observable_p1.md` in full; the relevant
  computational-scope section of `docs/README.md`; and the model/API,
  Gaussian-moment, observable-closure, numerical-closure, time-40, and optional
  tensor-backend sections of `code/README.md`.

All 11 original frozen `observable_*` modules were read completely:
`observable_arithmetic`, `observable_closure`, `observable_compiler`,
`observable_fixed`, `observable_initialization`, `observable_laws`,
`observable_p1_initialization`, `observable_solver`,
`observable_torch_circle`, `observable_torch_p1`, and `observable_words`.
The three supplemental package-import files were also read completely.
The optional tensor implementations and specialized first-order initializer
were not substituted for the candidate's general-dimensional generic
initializer. No runtime source dependency necessary to the claimed execution
was left outside the supplied review boundary.

## Model and theorem contract

The normalization is consistent throughout. Inputs are `x=sqrt(d)u`; the
first preactivation is `W1 u`; the stored middle entries already have variance
`1/n`; the output is `c^T h2/n`; and the stored initial readout has variance
`1/n^2`. The loss has factor `1/m` and no half. Mobilities `(n,1,n)` produce
the displayed physical velocities with factor `-2/m`, and the middle rank
uses the normalized lower-population inner product. The finite algorithms
retain the random readout. Only its population limit is zero.

The raw state keeps all `d` row coordinates. Only `K=A-A0` is HS; the
initialized action itself is a bounded action with its actual adjoint. The
raw metric is the stated sum of row/readout L2 and increment HS distances.
This matters both to the finite scaling and to the strong-completion proof.
The hierarchy and solver do not replace the reverse action by independently
sampled noise or a separately fitted map.

All conclusions fix `m,d`, the labels, and the data before width and closure
limits. The proof does not obtain a general-dimensional claim by applying a
two-dimensional trained-flow theorem unchanged: the signed reference, full
row estimates, source bootstrap, fixed-proxy capture, and dictionary
construction explicitly carry the new finite dimensions. Constants may
depend on the separately fixed dimensions. The `m=d=1` sphere is handled
literally. For `m>=2`, the final strictly positive radius admits actual
nonorthogonal configurations. No claim of a nontrivial angular neighborhood
on `S^0` is smuggled into the conclusion.

## Scientific checks and findings

### 1. Reference flow, fitting, and both-layer activity

I checked the mixed-label symmetry using the signed permutation action,
including the factor `y_a y_{pi(a)}`. It preserves the initialized joint
model and the reference equations and gives `f_a=y_a b`. It does not require
balanced labels. At `m=1` the same conclusion follows directly, without a
nontrivial permutation assumption.

The feature-time equations retain the mean-loss normalization. The derivative
of `b` is the sum of the readout contribution and the squared feature
gradient. The convexity argument for the readout norm supplies the positive
lower bound `b_s >= v/m > 1/(5m)`. Reintroducing physical time by
`s_t=2(1-b)` gives the claimed exponential residual bound. In particular,
at `T=5m` the reference loss is strictly below `1/16`. A missing factor of
`m` or two here would change the learning horizon; neither is missing.

The strong reference construction uses the activation chart where it is
needed, and its continuation controls raw fields and the operator increment.
Passive directions are reconstructed from the complete first row. Endpoint
continuation is supported by strong Cauchy bounds, not just bounded loss.

For early feature motion, I checked the initialization source calculation,
including the nonzero response in the transpose and the subsequent forward
reuse. The covariance of the reverse source is the full second moment of
the upper input. Its positivity argument works with arbitrary label signs
and at `m=1`. For the second layer, the residual Gaussian variance after
projection is positive and the retained response contributes with the stated
sign. Thus neither layer's positive coefficient relies on an unjustified
fresh-matrix substitution or on cancellation being absent by assertion.

The cutoff remainder estimates, the choices of `R_m`, `s_0`, `t_act`, and
`a_m`, and the reverse triangle inequality give a strictly positive paired
displacement on the actual reference trajectory. These are initial/current
pairs on the same neuron population, not differences between unrelated
marginals. The best-affine tanh error is positive for the nondegenerate
initial Gaussian laws. The displayed L2 continuity bound for that error and
variance applies at the chosen activity time. The rational constant
certificate is finite, has the required signs, and supplies the reference
learning inequality independently of floating quadrature.

**Finding:** no material defect in the reference or positivity arguments.

### 2. Source bounds, perturbations, and strong completion

The most important possible circularity is resolved in the supplied proof.
The reference physical-clock program is built first using the already
constructed reference, finite Gaussian programs, and fresh-root forcing.
Its source-coefficient bound is obtained independently of the desired
perturbed raw Euler cap. The raw-clock transfer then compares against that
anchor; it does not use a cap that it is simultaneously attempting to prove.

I checked the causal source ordering and normalized mass factors. Past
response coefficients carry their atom/time masses; the current upper
distinguished slot is treated separately. The derivative of the raw chart
defect has the required cancellation of one time factor against the
normalized source mass. In particular, the displayed `h^2 (2/m)/(h/m)=2h`
calculation prevents a spurious inverse mesh dependence.

Within a temporary cap, the upper fields and lower queries are a Gaussian
part plus a bounded response. Weighted Jensen estimates control the complete
source sums without counting mesh points as independent unit contributions.
The lower row moments, normalized pulse bounds, and Holder interpolation
are adequate for the response comparison. The weakened positive exponent
in the comparison estimate is harmless; no Lipschitz claim in the raw L2
norm is being used for an unbounded product.

The raw comparison has only one reference cutoff. The reference readout is
bounded, and the remaining dangerous multiplication is treated with the
reference query tail. A competing strong solution needs its raw L2 bounds,
not an independently assumed matching query-tail estimate. The explicit
radius construction makes the perturbation and Gaussian-tail error smaller
than the cap-improvement threshold; the negative quadratic cutoff exponent
dominates the positive linear exponent. The radius is positive and independent
of width and all numerical resolutions, despite its impractical size.

After both caps close, two raw Euler approximations can be compared directly.
The uniform tails, consistency defects, and raw estimates make them Cauchy
in the common strong state space. Convergence of the nonlinear field then
gives the raw differential equations. This is stronger than mere proximity
to the reference: it constructs a perturbed solution and its strong
derivative. The same one-reference comparison proves uniqueness and
reached-state continuation. Gaussian-source decompositions and the tail
bounds pass to the reached fields through the stated source isometry.

**Finding:** no unclosed source-cap assumption, circular reference anchor,
or missing strong-completion step remains.

### 3. Actual finite GF and raw GD

The fixed oracle proxy is essential and is used with the correct order.
At each fixed proxy mesh it is a finite initialized Gaussian program, so
the maintained finite-program theorem applies before its query count changes.
The full first row and the actual random finite readout are retained.
Scalar contractions and finite-rank updates are restored by the fixed-program
induction, with both action orientations on the same initialized matrix.

Finite raw norm bounds and the positive-part query-tail argument yield the
one-reference comparison against this proxy. The resulting error estimate
allows the cutoff to be chosen first, the oracle mesh next, and width last.
For raw GD, its local mesh error then contributes through `eta_n` on this
fixed comparison. Consequently `eta_n -> 0` suffices for the claim as stated;
one need not apply a finite-transcript theorem to a transcript of length
`1/eta_n`, nor impose the stronger step restriction from the separate
reference chart argument. The latter argument is not misused as the proof
of the stronger general capture conclusion.

Fixed typed same-population observation graphs pass through the same
couplings and actual action bounds. Named L2 fields multiplied by bounded
gates require truncation of the target and its uniform integrability; this
is supplied. Full-sphere predictions use the complete row and compact-input
modulus, followed by finite nets. Uniform time uses the bounded raw speeds
and interpolation with nonlinear observations recomputed from interpolated
raw weights. There is no cross-layer neuron pairing claim.

**Finding:** the finite GF/raw-GD and stated observation conclusions are
supported, with the precise probability and limit order in the candidate.

### 4. Hierarchy, dense closure, and convergence

The hierarchy keeps typed joint laws, marks, named fields, and both action
directions. Bounded determining tests, rather than an unjustified moment
determinacy assumption, identify the current observable spaces. The
Fourier-cylinder density argument and actual adjunction give the needed
reducing action spaces. Invariance is justified by finite raw Euler steps
and their already established strong limit. Reached-state sufficiency is
therefore tied to actual canonical solutions, not arbitrary formal moment
sequences.

The polynomial core supplies genuine enrichment, and the exhaustive bounded
word tail supplies density beyond that core. Every finite code has smaller
dependencies, and the enumeration covers rational scales and all grammar
operations. Duplicate bounded outputs are retained rather than silently
deleted. The positive-density and odd-polynomial calculation establish new
initialized action information, including the early `N=1` to `N=3`
enrichment. A fixed low-degree dictionary would not be dense; it is not the
one used in the theorem.

The inverse-lower-Cholesky normalization has all required transposes.
The operators `Q_{ell,N}` are contractions and approach the identity
strongly on the generated spaces. The coefficient bound for a fixed earlier
word remains fixed when embedded into a larger dictionary, even though the
output list is reordered or contains duplicates. Both initialized action
orientations converge strongly; no operator-norm approximation to `A0` is
asserted or needed.

At a fixed order, the equations are autonomous on their complete joint mark
laws and full coefficient matrix. Their gradient metric is weighted L2 for
rows/readout and ordinary Frobenius for the coefficient matrix. The energy
identity and bounded feature envelopes give global finite-horizon existence
and own-state restart. The lifted matrix velocity is the two-sided filtered
canonical rank velocity, as required for the omitted-source estimate.

The omitted-source error actually tends to zero: strong convergence is
uniform on compact target field images, and the compact HS derivative curve
is approximated by finite ranks. The one-reference tail comparison then
propagates this produced error through the prescribed horizon. For the
weaker exponential-tail formulation the Osgood modulus has divergent
reciprocal integral; for the stronger Gaussian tails already proved here,
a fixed-cutoff Gronwall limit also suffices. The closure proof imposes no
unproved uniform tail condition on projected trajectories.

**Finding:** the finite population closure is dense and convergent in the
claimed observations. It is not a replay of the trained trajectory or an
unclosed initialized-action oracle.

### 5. Numerical realization and all interfaces

The general-dimensional adapter changes lower Gaussian seeds and offsets,
while inheriting structural ingestion and frozen-source reverse
differentiation. I checked initialization and independent population replay
in both orientations, including seed indices beyond two. Both dictionaries
and their forward/reverse action union are compiled before normalization.
Every named covariance direction receives positive regularization; an
unresolved positive pivot raises an error. Formal derivative slots are
retained when their eventual Gaussian covariance is singular.

The deterministic Gaussian rule, its polynomial-moment control, and
finite-coefficient induction support the initializer-quadrature limit at
fixed positive regularization. Population replay freezes the coefficient
program and samples the complete joint marks, including `g`. Removing
regularization is justified by continuous PSD square roots and Gaussian
envelopes, not by continuity of a singular Cholesky factor or deletion of
small eigenvalues. The feature ridge stays positive at each fixed order.

Inner dynamics do not assume that independent population replay exactly
reproduces the initializer Gram or is a contraction. Their fixed-order
bounded-feature estimates suffice. Precision, time mesh, optional input
representation, population quadrature, initializer quadrature, source
regularization, and dictionary order occur in the stated innermost-first
order. Exact data omit the coordinate-representation limit. Literal working
weights stay in the vector field; probability normalization is used only
where a returned law needs that interpretation. The mass-error estimate
accounts for their arithmetic approximation.

The Heun stages are bounded before the mesh argument, and the rational
elementary algorithms are locally consistent on the fixed compact operand
sets encountered at fixed outer resolution. Uniform passive prediction
follows from a finite continuous evaluation graph on the compact sphere,
not merely from checking a finite panel. Fixed precision alone has no
asymptotic precision guarantee.

Runtime uses one full matrix `M` and its transpose. Polymorphic state copies,
stage construction, and validators preserve general row dimension through
the inherited integrator. Frozen upper observations use `g,D` on the same
marks. Joint observations retain same-population weights. Checkpoints store
all nine current/frozen arrays, data, arithmetic, and metadata; loading does
not call the initializer or require past predictions. The supplied restart
guarantee is for the same backend, reduction environment, and step schedule.

The scalar state, RHS, initialization, block-workspace, and elementary-call
counts agree with the actual arrays and contractions. The exact rational
temporary costs are included separately from fixed-point scalar storage.
Default resource guards are correctly described as adjustable planning
estimates, not certified process peaks. There is no neural-width parameter
or runtime source tape. A finite population closure still uses population
integrals; the subsequent quadrature level is what produces a finite scalar
computation. The candidate makes this distinction explicitly.

**Finding:** no material mismatch between the proof's numerical method and
the candidate implementation or its maintained producers/consumers.

### 6. Assembly and strict margins

The assembly bounds predictions, paired differences, and preactivation
fields on one raw comparison ball. Its final radius is the minimum of the
source-cap radius and independently fixed margin-preserving radii. The
reference loss margin plus the prediction discrepancy gives strictly
`L(T)<9/64`; the paired RMS discrepancy leaves at least `a_m/2`, hence
squared displacement at least `a_m^2/4`. The variance and best-affine-error
continuity calculation gives `q/16` and `nu_*/4` at every training anchor
in both layers. The denominators in that calculation stay bounded away
from zero. Finite W2 convergence then transfers any fixed smaller margins,
and the strict population loss bound implies finite loss at most `1/4`
with probability tending to one.

The conditional interface called Input C in the closure unit is discharged
by the separate reference/perturbation/capture units; its local list of
remaining study obligations is not an additional unresolved hypothesis in
the assembled theorem. The finite-width and numerical-closure approximations
are separate routes to the same canonical target. They are not silently
combined into a diagonal rate.

**Finding:** all numbered conclusions in THEOREM.md are covered without
weakening the theorem during review.

## Independent finite checks and evidence limits

Before running anything, I recorded a fixed plan in
`data/generated/cx1_many_point_closure_20260919/review_r1_a/semantic_test_plan.json`.
I then ran the frozen seven semantic tests exactly once with one numerical
thread, a 120-second wall timeout, CPU limits of 119/120 seconds, and a
512 MiB address-space limit. `CX1_CLOSURE_CHECK_OUTPUT` pointed to the fresh
review-owned `semantic_tests/` directory. No training experiment, adaptive
parameter change, or rerun was performed.

Result: **7 tests passed, 0 failures, 0 errors; exit status 0; 14.80 seconds
wall time**, within the declared limits. The tests cover dictionary
enrichment/dimensions, the iterative high-dimensional exponent enumerator,
adapter agreement with the maintained compiler, forward/reverse response
and a seventh Gaussian seed, actual weighted adjunction and all gradient
blocks, joint observations and exact continuation after restart, rational
arithmetic, and resource/domain rejection. Tiny Heun steps are semantic
restart checks, not learning experiments. Full stdout, stderr, run metadata,
test results, and checkpoints are retained only in the review namespace.

I also inspected the allowed existing `reference_constants_01`,
`operational_02`, and `closure/deterministic_v4` records. The exact-constant
record agrees with the frozen certificate source. All ten outputs hashed
by the operational record exist and match their recorded hashes. The
operational configurations preserve their shapes and report exact
own-state restarts. Their integration-refinement prediction discrepancy
is about `0.061`, much larger than the time-refinement discrepancy about
`1.82e-7`. These facts support operation and the stated diagnostic caveats;
they do not establish finite-order accuracy. The resolved nonorthogonal
run is explicitly outside the certified-radius claim. I did not regenerate
its trajectories, infer a convergence rate from them, or treat its fitted
loss as evidence for the theorem.

## Unresolved issues and acceptance limits

There are **no identified blocking or nonblocking scientific corrections**
to the frozen candidate from this review. This is a full manual scientific
review with one bounded semantic reproduction, not a formal proof-assistant
verification or an exhaustive software-input audit. The acceptance is
restricted to the model, finite fixed dimensions, small fixed geometric
family, horizon, observation grammar, and order of limits actually stated.
It does not certify a chosen closure order, practical resolution of the
extremely small supported radius, numerical risk/activity margins, or
efficiency at prescribed approximation error.

Final hash verification after the review and report preparation matched all
33 supplied frozen inputs. The full records are
`review_r1_a/hashes_before_tests.json` and `review_r1_a/hashes_after_review.json`
under this study's generated namespace. No candidate, maintained source,
Git state, or other review was changed.
