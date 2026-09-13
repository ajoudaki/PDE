# H4 scientific review E — frozen candidate v3

**Verdict: PASS for the complete stated qualitative objective.** I found no
required mathematical, implementation, provenance, or bounded empirical
correction in this frozen candidate. This is a fresh whole-candidate review,
not a review of changes from an earlier edition. It is an independent review
finding, not permission to promote or a finite-run accuracy certificate.

Reviewer: `/root/h4_scientific_e_v3`. Date: 2026-09-13.
Frozen manifest SHA256:
`06132871ed70c3c13651a3fbb1f8e76d13582301237acb811f50756bdb223d02`.
Standalone edition:
`data/generated/observable_hierarchy/H4_candidate_v3`.

## Scope, isolation, and complete coverage

I read the complete neutral assignment, both required skills at
`/etc/codex/skills/solve-math-rigorously/SKILL.md` and
`/etc/codex/skills/investigate-conjectures/SKILL.md`, and the latter's
research-contract, adversarial-audit, decisive-experiments and evidence-ledger
references. I read the complete shared RESEARCH_WORKFLOW.md, including Part 2.
I did not perform author startup, read the study README, read another study,
consult author history or excluded reviews, inspect reproduction findings,
fetch research inputs, or exchange findings with reviewer F. I did not modify
the candidate, established material, or Git. All writes are my assigned flat
report/checking sources and my assigned generated scratch. No research
trajectory or finite-network training was executed.

I read all 1,754 lines of `H4_proposed_section_v2.md` and all 8,531 lines of
`H4_dependencies.md`, including complete proof bodies. Truncated display reads
were repaired by narrower reads, including the singular-query proof around
dependency lines 455–578 and the compiler's full AD/new-source methods. The
proposed source was read in consecutive blocks 1–600, 601–1200, 1201–1754.
The dependency reading covered 1–900 (with repaired displays), then 901–1450,
1451–2100, 2101–2800, 2801–3500, 3501–4250, 4251–4950, 4951–5650,
5651–6350, 6351–7100, 7101–7800, and 7801–8531. Important proof passages were
then revisited while auditing the constants and resource accounting.

The nine complete dependency units, identified by original source line
intervals, were:

| Frozen source | Complete assigned interval | Subject |
| --- | --- | --- |
| finite_dynamics.md | 1–227 | Finite normalization, metric, energy, existence |
| special_data_limits.md | 3785–4286 | III.F Gaussian programs, singular queries, adjoints and differentiation |
| global_nonlinear.md | 1840–1898 | Action norm, extensions and chain rule |
| global_nonlinear.md | 1903–2453 | Orthogonal reference and actual finite GF |
| global_nonlinear.md | 2924–3440 | Weighted named-source response proof |
| global_nonlinear.md | 3982–4815 | Raw comparison, common carrier, completion, finite proxy |
| global_nonlinear.md | 5270–6903 | Learning/activity, tails, exact scalar certificate, finite GF comparison |
| global_nonlinear.md | 8989–10554 | Time-40 coefficient bootstrap and strong construction |
| global_nonlinear.md | 11398–13981 | Binary passage and complete H1/H2/H3 numerical foundations |

I read the complete edition notation contract (98 lines), docs guide (738
lines), and code guide (1,113 lines), the complete additional H4 code-guide
source, dependency manifest, edition manifest, and assembler. Duplicate full
guide sources have identical hashes to the guides read. I did not read unused
scientific chapter sections. Mechanical hashing and extraction used full
chapter bytes only to verify provenance and the assigned section boundaries.

I read every complete implementation, test, plan and recipe in the edition:
all eleven pde Python files (`__init__`, finite_network, gaussian_moments,
observable_arithmetic, observable_closure, observable_compiler,
observable_fixed, observable_initialization, observable_laws,
observable_solver, observable_words); all five scripts (both validation
workers, both analyzers, and the supervisor); all seven observable test files;
both complete plans. The older prototype is understood only as an imported
test dependency, not the proposed runtime or hierarchy.

All 271 manifest files were hashed and their byte lengths verified: 32 edition
files, 225 author-run files, and 14 other assigned files. The checker verified
all edition destination hashes and all nine exact dependency excerpt hashes.
Removing the one exact proposed insertion from the assembled chapter recovers
the frozen older chapter hash
`77e0f2b9a2ecd337c1a47b8f6c2025c72122e28512ca7481377418fe3f235932`.
The full 271-entry verification is retained in `hash_coverage.json`. A final
read-only rehash after testing again matched all 271 inputs.

Principal scientific hashes:

| Input | SHA256 |
| --- | --- |
| Proposed section | `b755c3d05eacc0ef20df6d0499f73dcc6fbf46abdcf4a04084c346ce6b4ad432` |
| Complete dependencies | `4099bc462040ad9df526f5ef63eef6e1c5462eb3325418354c6120d1fd44af50` |
| Notation | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| Docs guide | `0a27a6bc697c65b290bbe6d16c9992575c6221115b992efaef1a78ad983ae13e` |
| Code guide | `b25c0ad7be0a770881c7ae75446a1718d4217ceec5576bdc14864790daffc91e` |
| Assembled chapter | `cbcf00fd705a9a938a6a3fd0d2bbc2f1c2dd3ab4303d848740a549dbb169f629` |

Every field of the 14 author records, their 14 logs, the supervisor and full
analysis JSON was parsed and reconciled. Every exact observation and restart
array was decoded, and every NPZ array was read: 84 observations and 28
checkpoints, totaling 3,416,112 decoded scalar entries. This was whole-record
and whole-array inspection, not selected-row sampling. Full array values are
verified mechanically rather than printed millions of times. The complete
analysis JSON was recomputed and compared recursively, excluding only its
measured analysis CPU duration; its complete Markdown was also reproduced.
The full deterministic-check records, logs and exact certificate source were
read. No missing input remains.

## Mathematical audit

**Model and family — PASS.** The equations retain the bias-free two-hidden
tanh model with x=√2u, stored Gaussian variances (1,1/n,1/n²), mobilities
(n,1,n), unhalved loss and physical time. The action A0 has norm at most two
on the prescribed common Gaussian carrier; its reverse is its actual adjoint.
Only K is a learned HS perturbation. Population zero readout is not substituted
for the actual finite random initial readout in the finite-width comparison.

The fixed radius uses E0=8192 and exactly ten power-of-two applications,
ρ=2^(-E10). Rational interval endpoints specify each separately fixed law
independently of closure order and all numerical resolutions. The exact
quarter-turn parameterization has the stated nonorthogonal atomic example;
nondegenerate intervals are nonatomic because U(ρs) is injective. Equal label
masses and the support-distance bound place both exact laws and midpoint rules
in the proved cap domain. No rank or minimum atom mass hypothesis is hidden.

**Explicit cap, tails and continuation — PASS.** I checked the dependency
source calculus and the entire new derivation (H40.E2)–(E33). The lower
normalized source pulse includes the direct impulse, changing residual/input
factors, the φ''Q term, and every learned-memory/source-response term. Its
weights remain attached to source atoms, so the bounds do not count atoms.
Hölder interpolation from L2 and L24 gives an exponent stronger than the
deliberately weakened 1/16; the gate estimates and L12 factors fit the L4
forcing estimate. Propagation uses the pointwise weighted query sum inside
an exponential, followed by its L4 estimate; it does not interchange an
unbounded supremum with population expectation.

The upper U,C,V recurrences retain the readout derivative and cφ''U term.
The changed current impulse cancels, and E_k depends only on E_j with j<k.
Thus both discrete Gronwall steps are causal. The explicit constants
J0, A_low, Z_low, Cv, Cα, FΔ, AU, AC, AV, V_force, V_prop and C_src dominate
the displayed telescoping terms; no unquantified predecessor constant is
used to select the radius.

The raw comparison is in the sum of lower L2, upper L2 and middle HS norms.
The one-cutoff product bound controls the problematic gates with reference
tails only. The explicit C_raw expansion covers all three velocity products,
including the rank-one middle difference in HS. Gaussian-plus-bounded Q
gives H exp(-Rc²/S), with Rc≥2D*. The same-mesh recurrence has no mesh-error
floor. For A=1+Γ+H+Z and Rc=4SA, the algebra
log(4ΓH)+X+Z < 6SA² < 16SA² verifies the tail term. The law term and
ε term are each strictly below the stated fractions of z. The first possibly
failed row is consequently below B*+1/4, strictly below B. The initial row is
zero. Fractional Euler steps also fit the cap argument.

I checked the finite tower domination argument and its successive envelopes:
the primitive constants fit the stated E2-based bounds, the subsequent
polynomial/exponential envelopes have slack, and Λ is below E10 log 2.
The positive symbolic radius therefore lies inside the explicit cap radius.
This is a finite mathematical construction even though it is impractical to
resolve at working precision.

The resulting uniform tails and crude raw bounds supply the actual
hypotheses of the complete inherited strong-construction proof. Compact-cap
finite approximations preserve label masses, and meshes eventually satisfy
the inherited step threshold. The logarithmic-cutoff comparison gives a
Cauchy sequence in C([0,40];E); the current-field continuity estimate gives
the C1 autonomous limit. Uniqueness comes from the one-sided tail estimate
against that constructed solution. It is not inferred from compactness.
Continuation from a reached state uses the same argument.

**Identification and substantial learning — PASS.** Finite-program capture
is invoked with one fixed finite comparison law and mesh before taking width
to infinity. The additive initial-readout proxy and the finite energy bounds
cover the actual finite initial readout. Arbitrary empirical laws tending to
the fixed supported law may be compared to that proxy without themselves
being cap-supported. The required probability mode is convergence in
probability; no simultaneous order/width rate is introduced.

The complete inherited reference proof and exact rational integration check
support the risk/activity margins. The new cap radius is also below the
required binary comparison scale. At physical time 1/200 the lower bound is
(1/2500000)² − 26·10^(-18) − 8·12² exp(-exp(3000)) > 1.59·10^(-13),
so both required 10^(-13) squared-motion thresholds follow. The time-40 risk
comparison has strict limiting margin 1/128<1/4. Passing these through the
established prediction and same-population pair convergence is justified.
No activity-at-40 statement is needed or used.

**Exact closures and order limit — PASS.** The retained dictionary is the
specified nested bounded Chebyshev core plus exhaustive literal word prefix;
it contains both initialized action directions. Ridge normalization is by
inverse lower Cholesky, with η_N=1/[1024(N+1)²]. The two population feature
maps define contractions and filters Q_l; D=L2^(-1) C L1^(-T), and the runtime
reverse is D^T. The exact closure lifts to B_N=Q2 A0 Q1 and the projected
learned HS increment. The gradient identity and horizon bounds give each
fixed-order global characteristic solution.

The generated sigma-fields contain the bounded Fourier words needed for
density and are invariant under both action orientations. The ridge error on
a fixed padded coefficient vector tends to zero; density and contraction
then give strong filter convergence. Compact sets of exact hidden fields,
upper backward fields and HS derivatives upgrade it where uniformity is
needed. The forcing includes both initialized-action errors and the projected
HS source. The reference-tail cutoff comparison first takes N to infinity
at fixed cutoff and then removes the cutoff. It gives full-circle,
uniform-time prediction convergence and, through joint couplings, both
initial/current pair laws, their RMS motions and risks. Separate marginal
activation laws would be insufficient; the proof retains the required pairs.

**Finite numerical convergence — PASS.** The order of removal is arithmetic,
time mesh, input rule, population replay, initializer quadrature, generic
source regularization, then closure order. This is an iterated limit for
each fixed exact represented law. It does not imply arbitrary simultaneous
refinement or computable error-to-resolution selection.

The Gaussian initializer replays a complete joint mark law with Q-frozen
coefficients. It preserves covariance prefixes and all named source
directions, including singular limiting directions, until the positive
regularizer is removed. Frozen source derivatives do not differentiate the
Gaussian covariance construction. The optimized core's contraction includes
both covariance and response contributions; its unused regularizer is
disclosed. H3's polynomial-envelope cubature argument supplies the Q/P moment
limits, including the unbounded Gaussian g marks.

The midpoint transport bound is ρ[(b-a)+(d-c)]/(4m)≤ρ/m. Fixed-order drift
stability uses bounded marks, L2 joint couplings, and a linear W1 data term.
Pair W2 transport legitimately introduces a square-root data term. Literal
rounded masses appear as s1 in a, s2 in f,d, and sd in the velocity; the
mass-defect estimate accounts for them. Pair probabilities normalize only for
interpretation. Raw RMS²=s_l s_d times normalized RMS², and raw risk retains
sd. Thus rounding does not silently alter the operational equations.

Heun has independent finite-horizon stage bounds at every fixed outer
resolution, without asserting discrete energy decay. Its O(h²) local
comparison and Lipschitz recurrence suffice for the required uniform-time
mesh limit. Precision-first convergence uses eventually positive pivot
margins and locally uniform primitive algorithms. The full-circle arithmetic
argument applies to compact sets of query direction and interpolation
fraction, including initial-field evaluation; a finite output panel is not
used to infer a supremum. Direct query rounding, weight validation, step
rounding and radius replacement are each handled explicitly. For fixed E10,
increasing precision eventually exits the replacement branch with enlarged
finite resource allowances. No default resource ceiling is mistaken for a
mathematical convergence guarantee.

## Implementation and resource audit

**Runtime and representation — PASS.** I traced the actual contraction order
in `_fields`, `rhs`, and paired observations. M and M^T represent one action
and its adjoint with the two literal weighted feature measures. Runtime state
is precisely the full lower (b1,g,w) and upper (b2,c) populations, both
weights, M and D. Initial upper activations use g,D and the same frozen
weights. The solver takes its own simultaneous Heun stages. The worker does
not evolve an interpolated observation, import an intermediate target state,
reset approximation errors, fit a surrogate, retain a source tape during
evolution, or call an arbitrary-action oracle.

The nine-array state count S=P1(d1+5)+P2(d2+2)+2d1d2 and law count 4A
match the implementation and all archived checkpoint dimensions. The RHS,
block workspace and constant-stage bounds match the coefficient-first
products. Runtime grows with J while retained state does not. Initializer
table/AD/covariance/normalization bounds account for both orientations and
Q/P replay. The predecessor's explicit prime-generation and Halton digit
costs remain applicable; D.5's displayed I4/I5 are the identified table and
contraction work, not an exemption for those initialization operations.
Exact syntax/envelopes, scalar bit size, elementary Fraction temporaries,
the enormous resolved law denominator, output pair arrays and serialization
have separately stated costs. The measured state-byte counters and structural
stage allowances are not presented as exact process-wide peak allocations.

**Law and saved-state semantics — PASS.** Bounded symbolic evaluation does
not expand the tower. Exact descriptors survive all backends and restart.
The supported worker checks the canonical fixed radius before giving the
supported scope tag; rational-radius calls explicitly carry exploratory
scope. Quadrature distinguishes deliberate replacement, coordinate-rounding
collapse, nonatomic components, and exact reference midpoints. It records
actual rational coordinate/weight errors. Own-state restart compares all
nine state arrays, all three law arrays, both metadata mappings, arithmetic,
and prediction. Time and remaining-step information is in the companion
record. Exact continuation requires the same arithmetic and reduction
environment, as stated.

**Supervisor, outputs and scientific scope — PASS.** The plan has precisely
14 configurations, one serial numerical thread, explicit per-run CPU/wall/RSS
and cumulative CPU budgets, fixed observation times and a fixed circle panel.
The supervisor validates names and plans before output, caps logs, verifies
worker provenance, accounts for child CPU, records failures and unstarted
configurations, and reaps workers. Sampled resource enforcement can overshoot;
that limitation is expressly recorded. Producer observations are output only.
Exact hexadecimal/fixed-unit JSON accompanies float64 NPZ diagnostics. The
analyzer's finite-panel comparisons are not treated as trajectory error bounds.

## Actual predeclared tests and results

The specific tests were saved before execution in
`H4_scientific_E_v3_predeclared.md`. The sole runner command was
`python -B studies/observable_hierarchy/H4_scientific_E_v3_run.py` from the
repository root. The runner set edition-only PYTHONPATH, disabled bytecode,
restricted all temporary output to my assigned scratch, imposed 4 GiB address
space and at most the remaining CPU allowance on each subprocess, and set all
six numerical thread variables to one. It executed serially:

| Command from frozen edition | Result | CPU seconds |
| --- | --- | ---: |
| `python -B -m unittest discover -s code/tests -p 'test_observable*.py' -v` | All 67 tests passed | 4.625079 |
| Frozen `H4_full_tests_v1/reference_certificate.py` | Exact rational assertions passed | 3.295677 |
| My `H4_scientific_E_v3_check.py` | All independent checks passed | 9.928033 |

Reaped child CPU, including descendants, was **17.848789 seconds**; runner
CPU was 0.018461395 seconds. Peak child RSS was **98,172,928 bytes**. No
limit was reached and no test failed. The rational certificate returned
[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687,
0.631761866359]; the assertions use Fractions, not these printed floats.

The independent checker attacked every manufactured w,c,M gradient entry
with unequal populations and slightly nonunit literal masses; maximum
absolute derivative discrepancy was 1.0326600978407402e-10, below the
predeclared 3e-10 tolerance. It checked adjoint duality and that validation
and evaluations left masses unchanged. Permuting g relative to its fixed
population changed both paired RMS values, detecting loss of joint identity.
It also checked 125 exact rational chord identities and twelve cutoff
boundary cases. The frozen suite separately checks source derivatives by
coordinate perturbation, singular/zero sources, exact covariance prefixes,
the missing-response alternative, Cholesky orientation, all-backend
serialization, precision refinement, off-mesh nonfeedback and supervisor
failure/resource paths.

The archive checker did not evolve saved trajectories. It recomputed both
time-20 and time-40 observations directly from each stored current state,
matching every exact encoded scalar. It verified all 84 exact observation
JSONs against their NPZ views, recomputed risk and weighted paired RMS, checked
zero-time pairing, all law descriptions and node rules, every source hash,
complete restart fields, byte counts, stage records and plan/worker provenance.
It reproduced the full analysis and all twelve comparable pairs.

The author logs record 14 completed exact restarts; the producer and frozen
deterministic fixtures support their semantics. I independently verified the
complete stored restart evidence and recomputed observations, but did not
repeat fourteen continuations to time 40, which the review assignment forbids.
The older deterministic record's two test-source hashes differ from the
current edition's law/worker test files; therefore I did not use that record
as a test result for the current bytes. The fresh 67-test execution above
checks the exact frozen v3 files.

The recomputed worker CPU sum is **506.290977526 seconds**, maximum reported
peak RSS **56,119,296 bytes**, and supervisor charged CPU **508.253257
seconds**, within the frozen bounds. All 12 supported-law configurations
explicitly collapse at the declared precision; the two radius-1/20
exploratory configurations do not. Representative complete-panel/saved-time
comparison maxima are:

| Changed axis | Maximum prediction difference |
| --- | ---: |
| Order-3 step count doubled | 1.204920860309322e-6 |
| Order-3 initializer nodes doubled | 0.0032738148784794974 |
| Order-3 population nodes doubled | 0.012399564417638897 |
| Supported input nodes doubled | 4.440892098500626e-16 |
| Exploratory input nodes doubled | 0.00022518790365366748 |
| Tiny rational 24/36 digits | 0 in the float64 prediction view |

The guide rounds these correctly. Exact high-precision records remain
distinct; equality of a floating view is not equality of the exact working
states. None of these empirical differences establishes the theorem's
whole-circle/time-uniform error or resolves the supported positive radius.

## Corrections, limitations and completion

Required corrections: **none found**. Missing inputs: **none**. Unresolved
component verdicts: **none**. All components of the stipulated qualitative
objective, implementation and bounded empirical claims pass this review.
The candidate expressly excludes rates, affordable accuracy selection,
finite-run certification and arbitrary simultaneous limits; those exclusions
are consistent with what the proofs and experiments establish.

The handwritten checking sources and original full results are preserved.
Relevant SHA256 values are:

| Review artifact | SHA256 |
| --- | --- |
| Predeclaration | `82f0bdb92d5020722d1bfebb71f605a56f38b5e4c976b982e4e30b3f8f075a73` |
| Independent checker | `00653a951edfcd1a65cf2758649e38fa80183aa6a4d31f80c76fb1bc115b1e5e` |
| Bounded runner | `495727e82344d34f3eafc44a8657ae4a64ddbaeb390957aff4f6ca795b95deba` |
| hash_coverage.json | `b3669c38f3335c064ed8a0f7b0045493559956ff1577cbfa7e4866a3efa737a0` |
| audit.json / check_2.log | `a999f0b4cd678379766cede598747f04d62cc73682d4db7e86fd9dffd29354c5` |
| run.json | `562aeda4e1ccc63c309dfab7eec8540b259a02aa9123cae37d45877acb7ab18c` |
| check_0.log | `75b98d6322fdcabaffaf15295b75d015d0c0fea4bc58f3aa5451ae758e77dc4f` |
| check_1.log | `ad40e8d8f73fed6d22cc9b68a19f7f9e6c3f2f59383d581e372ce0c976786900` |

Generated artifacts are in
`data/generated/observable_hierarchy/H4_scientific_E_v3/`; handwritten files
are flat `studies/observable_hierarchy/H4_scientific_E_v3_*` files. This is
the original full report. No earlier or concurrent review was used to obtain
or calibrate this verdict.
