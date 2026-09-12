# H3 complete isolated scientific review B, frozen version 1

**Verdict:** PASS for the explicitly bounded reference components and their
fresh numerical reproduction. **The original full C-H3 milestone is not met.**
The fixed-order comparison has a nonzero error floor; the executable handles
one orthogonal two-atom training law and the specified scalar observations.
It supplies neither a terminating arbitrary-tolerance nonlinear closure nor
an effectively certified nonorthogonal/nonatomic family nor every admissible
finite same-population observation tuple. These are substantive open
obligations, not consequences of the successful reference calculation.

No required scientific correction to the positive bounded-reference claims
was identified in this review. This verdict does not approve promotion,
certify an assembled canonical edition, or reopen the completed H2 prototype
audits. The ordinary explanation that a very short-time frozen prediction is
accurate survives; the result additionally certifies small positive motion of
both hidden layers, but proves no advantage over frozen features or substantial
learning.

## Identity, isolation, authority and input integrity

Reviewer: `/root/h3_review_b`, distinct from the declared authors/assemblers
`/root`, `/root/h3_shorttime_route`, `/root/h3_effective_route`, selector
`/root/h3_relevance`, and the other complete reviewer. I started from only
`H3_review_assignment_v1.md` and `H3_review_manifest_v1.json`. I did not read the
study README, history, original route/numerical reports, internal audits,
relevance reports, another reviewer report, another study, or Git history.
I did not delegate, fetch additional scientific sources, modify the frozen
inputs, or change Git state. Communications to the coordinator reported only
my scope/progress/results; no other review findings were supplied to me.

The manifest SHA256 before and after reproduction is
`bc60684162353c63704644f4a543b2f644eb7a27ec6179e293a3bbbb71f241f9`.
All 16 source hashes and all 16 standalone-copy hashes matched. The manifest
and `input_verification.json` retain the full check. Metadata-only Git checks
found HEAD `675e43fc666aabb81f1ee68efa5e4315a3f0ed93`, an empty staged list and
existing modifications in `.gitignore` and book-exporter maintenance paths.
Their contents were not read and they were untouched.

I read the complete root `AGENTS.md` and `RESEARCH_WORKFLOW.md`, both required
skills at `/etc/codex/skills/{solve-math-rigorously,investigate-conjectures}/SKILL.md`,
and the latter skill's complete `research-contract.md`, `evidence-ledger.md`,
`adversarial-audit.md`, and `decisive-experiments.md`. The isolated-review scope
replaced ordinary author startup reading. The first combined skill output was
truncated; both skill files were reread completely. The first guide output was
truncated; explicit reads of README lines 200–480 and 480–570 repaired it.

Complete actual manifest read coverage follows. Every range is inclusive;
implementation, proof bodies, tests and examples were read, not just searched.

| Input | Complete lines read | SHA256 |
|---|---:|---|
| H3_candidate_reference_v1.md | 1–620, in 1–310 and 311–620 | `2135a0d1f3bd9cdb754b1a0f08f7ae9d3c059cfb646360487f7eb1f92c2c78a2` |
| H3_candidate_circle_v1.md | 1–342 | `567247c7afa09ac4502bafa4f3dfea0197c449ba5ca46a8a3826ff74d37f54dc` |
| H3_stability_proof.md | 1–124 | `a5a68240508b3601faddbc30005626c144190fe38d02d1291787ef3ebeb69735` |
| H3_stability.py | 1–140 | `a59194db71e5b17fcd8a4884a0a5839a16c93007cd4e06dc65dbd1bb22bcf65d` |
| H3_shorttime_solver.py | 1–530 | `cf3b479826c8900bc4097d023128330c380df415d83b2a782054c5e565542e6b` |
| H3_shorttime_test.py | 1–154 | `11dd36c0d7ead265ddc3bfc20f7d5b688d1f6dacac7cfe8b7b652468c81eedb5` |
| H3_circle_kernel.py | 1–337 | `ec4975ae0f469755f0fa025e4b4b0b185f6b05fd97dbfa74bd60d34e61ffdef2` |
| H3_circle_kernel_test.py | 1–98 | `6550f472cc5876307832e62ed8a0cb451bccfe9a3deafe67ce9d86fb9a1aeb45` |
| H3_reference_solver.py | 1–106 | `5ce7e2789083269ed9f5b02a02fc277d9464551655f31b2bc890a0fed1273f62` |
| H3_make_review_capsule.py | 1–58 | `7fea40ee5aaa34c666bb94155350e0c839312e2babb97ce96915b506f33f72b1` |
| H3_demo_config_v1.json | 1–55 | `baacdb913ed2b92053aa8b647744c2e9260c70d2f6d2b74e0a464d9345091125` |
| dependencies_v1.md | 1–3569, consecutive 400-line chunks and 3201–3569 | `6a40bc9ee6e6de49fbefd9118298c4ab807b1ef52ecf29b99a71937eab0a63d7` |
| H2_proposed_section_v3.md | 1–470 | `c84617a514adaa43224c0f2990b75abb48eb92611ee3b45da753f47866ed90d2` |
| docs/README.md | 1–670, including repaired middle reads | `269f481c6198971875ec22cb1b7e451ad0f3fbf3fe21a41be42a72dd49ae7ce2` |
| docs/NOTATION.md | 1–98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| code/README.md | 1–748, in 1–375 and 376–748 | `3ffc27a58e8e090828fbac3f7d4b86c9e33f4ff5cdd7b0690e086364e8e82731` |

Total complete scientific/code/guide coverage: **8119 manifest lines**. I also
read the builder-generated `capsule/RUN.md` completely. The complete necessary
H3 source-action, strong-calculus, reference and law-flow dependencies are in
the supplied dependency packet. Its reference rational certificate source was
read, but not reexecuted: the new moment producer supplies stronger checks for
the constants needed here, and the assigned budget authorizes no second
historical reproduction.

One input-scope limitation was reported to the coordinator: H2's text invokes
C.4.7.8/H1 proofs not reproduced in `dependencies_v1.md`, which ends at C.4.7.5.
Accordingly I treat H2 as the assignment's established qualitative foundation,
not as a newly self-contained complete audit of H2 and all H1 ancestry. The
positive reference comparison needs no H1 dictionary or hierarchy uniqueness
proof, so this missing ancestry does not supply a premise of its PASS. No
unsupplied material was fetched. It would have to be supplied if a fresh audit
of H2 itself were requested.

## Scientific checks and component verdicts

| Component | Verdict | Exact scope |
|---|---|---|
| Model normalization and canonical finite-GF interpretation | PASS | Two tanh hidden layers, actual Gaussian finite readout, physical unhalved-loss GF, mobilities `(n,1,n)` |
| Finite initialized forward/reverse response formulas | PASS | Fixed finite law/observation calls; singular covariance semantics preserved |
| Nonlinear comparison S7–S16 and sharpened N1/N5 | PASS | Fixed positive horizon and stated bounds; no arbitrary-order convergence |
| Explicit small-time source cap | PASS | Marginal time/input tails for canonical paths; no Gaussian supremum claim |
| Scalar propagation calculation | PASS, conditional as stated | Same-base approximants with independently established bounds and full defect |
| Reference interval quadrature and paired RMS | PASS | Frozen reference configuration and named observations |
| Hermite whole-circle certificate | PASS | Initialized kernel plus independently proved nonlinear-GF envelope |
| Saved-state restart and cumulative error | PASS | The certified reference state and initialized kernel, within the fixed horizon |
| Full original C-H3 | NOT MET | Effective general-law arbitrary-accuracy solver and full observation certificate absent |

### Model, actions and coupling

I rederived the physical vector field from the loss and the stated metric.
For `u=x/sqrt(2)`, `h1=tanh(w·u)`, `z2=A h1`, `h2=tanh(z2)`,
`d2=c phi'(z2)` and `q=A* d2`, its blocks are
`-2 integral r phi'(w·u)q u`, `-2 integral r d2 tensor h1`, and
`-2 integral r h2`. The population rank has finite representative `d2 h1^T/n`;
the first/readout metrics yield the remaining factors of n. At reference
masses one half this gives `b'=1-kb`, not `2(1-kb)` or a feature-clock equation.
The finite initial readout remains independent Gaussian variance `1/n^2`.
Its limiting zero value and the finite maximum/RMS estimates in the dependency
proof justify population `c(0)=0`; this review executed no zero-readout finite
network.

The dependencies prove source laws for fixed finite programs by adaptive
Gaussian conditioning, then handle rank loss with noise regularization and
continuous positive square roots. Their common-space completion proves actual
adjunction; A.3 improves its operator constant to two. I checked the density,
scalar weighted Taylor remainder and strong multiplier/curve arguments used
for energy and comparisons. No ambient `L2 × L2 -> L2` product estimate is
being imported.

For S4, differentiating `H_b phi'(z_a)` in the named forward slots gives
`h_b E[s_a s_b]+h_a E[H_b phi''(z_a)]`. At `a=b` both paths contribute.
The reverse noise has covariance `E[D_ab D_cd]` and is independent of the
lower root. Replacing the reverse action by fresh independent answers, or
keeping its response alone, would change the law and the RMS coefficients.
For S5 I checked the saturated approximation: its only opposite-source
derivative is `l_u l_a phi'(P_ab/R)`. Dominated convergence in L2 and the
bounded action identify the completed input limit, including covariance
limits at singularity. The bound
`|x-R tanh(x/R)| <= |x|^3/(3R^2)` and the sixth-moment envelope give exactly S6.
This permits the stated one bounded-gate completed action; it is not an
unrestricted extension to arbitrary unbounded programs.

At the orthogonal reference the reverse mean is
`alpha h1-gamma h2`, where
`alpha=E[(1-H^2)(1-3H^2)]` and `gamma=(E s)^2`. I checked V by conditioning on
the lower root and independent reverse Gaussian. For the forward return J,
its covariances with z1,z2 are `alpha n` and `-gamma qm`. Conditioning on
these two Gaussian coordinates gives residual variance
`V-q(A^2+B^2)`. In the squared upper increment the B-squared contributions
cancel and the cross term has the displayed **negative B** sign. The supplied
four-point rational test checks this expansion against the unexpanded square;
the preceding source calculation, not that toy law, establishes its Gaussian
interpretation.

The leading hidden increments are `beta l1^2 P1` and
`beta s1(q U1+J1)`. Their L2 norms are exactly the executed
`beta sqrt(V)` and `beta sqrt(F)`. Both subtract the identical initial hidden
coordinate on the same population. Symmetry equates the two support-direction
squared norms, so averaging with weights one half produces these RMS values,
without an extra square-root-of-two factor. The lower and upper populations
are never coupled to each other. N5 uses the reverse triangle inequality on
these correctly paired increments.

### Remainders and explicit source/propagation constants

The loss bound `integral |r| <=Y` and pointwise readout bound `2Yt` imply S7.
I checked the row integral `2Y(2+2Y^2t^2)(2Yt)` and the forward decomposition
`A0(H1-h)+K H1`; these give the stated coefficients of t squared and t fourth.
The independent frozen loss identity gives S8 and the finite beta bound.
Readout subtraction gives `Ec'<=2 Ec+2Y(1+2t) Z`; prediction subtraction costs
`Ec+2Yt Z`, verifying S9–S10.

For the row subtraction the three costs are `8Yt F`,
`2Y(2Ec+4Yt Z+4Y^3t^3)`, and `4Y^2t(R W+tau_R)`.
For the middle subtraction they are `4Yt F`,
`2Y(Ec+2Yt Z)`, and `4Y^2t W`. They reproduce every coefficient in S13 and,
after integration, S14. The tail is cut on the **explicit initialized frozen
query**, not on an unknown trained error. The preliminary spatial Taylor
remainder is applied to the known Duhamel increment with a proved L4 bound,
not to a general L2 row difference. Bounded A0 contributes the factor two in
S16; the remaining `K(H1-h)` cost is accounted for.

For the sharper constants, `max |phi''|=4/(3sqrt(3))` and
`E min(G^2,1)=1-2phi_G(1)<.52` are valid. The preliminary Z bound first supplies
`||c||2<=2 kappa t`; reintegration then supplies the sharper row/action/Z
bounds without circularity. The frozen query's normalized Gaussian standard
deviation is at most sigma and its bounded shift at most `1+L sigma`.
Integrating `(sigma |G|+S)^2` beyond d and applying Mills' upper bound yields
the displayed tau. The sharper row coefficients use changed-residual cost
`8 sigma t F`, learned-action cost `8 kappa^2 t^3`, and gate cost
`4t(L R W+tau)`; the sharper middle coefficients likewise match. N1 bounds
the cheaper frozen prediction fF relative to canonical GF, while N5 adds the
separate scalar spatial errors needed for the two nonlinear hidden motions.
These two error sources were not conflated with moment quadrature widths.

The source-cap proof specializes the complete causal N9–N19 dependencies.
Earlier beta rows bound lower pulses before the current upper derivative row
is constructed. The single distinguished current slot prevents an unweighted
sum over all training inputs. The exact rational check gives
`Psi=0.030328853085402327 < B=0.03125`, with margin
`0.0009211469145976715`; `D=0.03125103040301`. Cross-program Gaussian isometry
and strong convergence pass the Gaussian-plus-bounded decomposition to
canonical paths. This is uniform over marginal time and input and does not
assert a tail for their supremum. At cutoff .2 the bound is below
`1.159626e-16`.

I separately collected the x,k,z coefficients of the comparison sum. They are
`5.53612824`, `2.368824`, and `8.2608`, so L is `8.2608` and the tail factor is
`4.08`. The integrating-factor bound for defect `1e-5` is below `5.104697e-8`.
The code's exact rational comparisons and range-reduced exponential lower
bounds are correctly directed. This is conditional propagation: it constructs
no path having that defect. A changed base action cannot be silently charged
as a Hilbert–Schmidt state increment.

### Uniform circle integration and arithmetic

The contained Hermite completeness argument uses an integrable entire
transform and Gaussian convolution uniqueness, with valid domination and
Fubini hypotheses. The correlated Gaussian generating identity includes
rho=±1, and the independent endpoint tests below verify the singular algebra.
Parseval gives summable positive spectral masses. The integration-by-parts
Bessel estimate `sum n beta_n <=q` implies the needed outer Lipschitz bound
without endpoint differentiation of a power series. It follows that the two
omitted masses add in the uniform composed-kernel error on all `[-1,1]`.

The two applications of the exact fourth-derivative polynomial operator
match their integrands, with sigma in `[0,1]`. Gaussian monomial maxima bound
all terms; scalar tails have the correct powers and factors of two. Simpson's
Peano kernel is nonpositive and has absolute integral `1/90`; I independently
checked its rational polynomial integral and the exact x-fourth saturation.
The reference nonnegative moments receive one-sided tail additions, whereas
the signed Hermite coefficients receive symmetric tails. Upper initialization
propagates the complete lower q interval. The positive q gate makes division
legitimate; no tiny Gram eigenvalue is discarded or inverted.

Every endpoint arithmetic operation expands outward. Integer powers use
rounded multiplication and include zero for even powers crossing zero. I
checked local `Decimal.exp` and `Decimal.sqrt` docstrings: both explicitly
guarantee correctly rounded `ROUND_HALF_EVEN` results. Rational exponential
tail checks independently confirm the used elementary operations at several
signs/scales. Machin's pi interval comes from exact alternating rational
terms. Error is therefore not inferred from agreement of quadrature
resolutions or untracked floating last digits.

Coefficient centers/radii and the midpoint kernel use exact Fractions.
Projection onto `[-1,1]` cannot enlarge distance to the true normalized inner
polynomial. The parameter-error expression charges alpha, q and beta
uncertainty separately. K9 uses the supplied current b interval, including its
saved uncertainty; K10 bounds coordinate-box error. Exact rational unit
inputs and outward boxes enclosing irrational unit inputs are both supported.
The norm-range test correctly rejects a rectangle disjoint from the circle,
and the fixed coordinate-radius budget is charged. Uniformity is analytic,
not inferred from finitely many queried directions.

The uniform-time readout-width proof uses one partial closed step before
the midpoint and one further partial step after it. Its conservative bound
is `1.0679004772960533e-11`, comfortably below the `2e-8` allowed width. The
actual final width is `1.0374382931981154e-11`. The arithmetic reserve dominates
the finite endpoint operations. The analytical envelope is evaluated at the
total elapsed time, so the uniform-time certificate does not reset at restart.

## Fresh standalone reproduction and deterministic attacks

All generated work is under
`data/generated/observable_hierarchy/H3_review_b_v1/`. Its preregistration was
written before executing the producer. The builder verified all frozen hashes
and copied only manifest inputs; this is a standalone reproduction capsule,
not a second repository checkout. No study path is required by its imports.

Actual producer commands, from the repository root and then the capsule:

```text
python -B studies/observable_hierarchy/H3_make_review_capsule.py --output data/generated/observable_hierarchy/H3_review_b_v1/capsule
/usr/bin/time -v -o ../reproduction_resources.txt timeout 900s python -B H3_reference_solver.py --output run > ../reproduction_stdout.log 2> ../reproduction_stderr.log
```

The second command's working directory was the absolute repository path plus
`data/generated/observable_hierarchy/H3_review_b_v1/capsule`. It was executed
**once**. Its combined run performs one reference initialization, one circle
initialization, midpoint serialization, reload, continuation and observations.
All thresholds used the frozen JSON/model configuration and matching constants
in source. No parameter sweep, trained trajectory or long-time extension ran.

Observed environment: Python 3.10.12, Linux 5.15.0-151-generic x86_64,
glibc 2.35; standard library only; 60 Decimal digits. The producer pins itself
to one allowed core, sets an 8-GiB address-space limit and 890-second CPU limit;
the outer command adds a 900-second wall limit. Exit status was zero and
stderr was empty. External resource measurement: **20.47 wall seconds,
10.67 user CPU seconds, 0.00 system CPU seconds, maximum RSS 18,720 KiB**.
The internal producer measured 20.413064651191235 seconds and 18,316 KiB;
its circle initialization took 8.076983474195004 seconds. Timing differs from
the candidate's prior run but is far inside the declared budget.

The resulting final true paired RMS enclosures, rounded outward, are
`[4.4732053e-6,4.5182496e-6]` and `[6.6076920e-6,6.7410684e-6]`.
Each lower endpoint exceeds `1e-7`. Their total absolute errors, including
moment/step interval widths, are respectively
`2.2522125991418018e-8` and `6.668816216190719e-8`, both below `1e-7`.
The reference scalar e1 prediction enclosure is
`[0.0011791368,0.0011839702]`, rounded outward; its total error is
`2.416666707483651e-6`. This is the high-accuracy scalar observation, distinct
from the coarser degree-seven whole-circle observation.

The reproduced inner/outer omitted masses are bounded by
`0.000480719508` and `0.000014597495`; the kernel parameter error is
`2.996579310873196e-10`, and total kernel error is
`0.0004953173017001104`. Including b, input and conversion budgets, and adding
the `2.417e-6` nonlinear-GF envelope, gives uniform total prediction error
**`7.3763635540102575e-6 <1e-5`**. The combined wrapper's e1 enclosure is
`[0.0011725855510,0.0011873193781]`, rounded outward, with positive lower
endpoint above `1e-4`; its diagonal enclosure contains zero as required.
All reported numbers came from this fresh producer, not another run's arrays.

The extra-check runner was executed as
`python -B run_extra_checks.py` from my generated directory. It sequentially
ran the following commands in the capsule, pinning one core and enforcing the
cumulative 60-core-second allowance. Supplied tests used a task-owned TMPDIR.

| Command/check | Result | CPU seconds | Wall seconds |
|---|---|---:|---:|
| `python -B H3_shorttime_test.py -v` | 9/9 PASS | 2.203844 | 2.219830 |
| `python -B H3_circle_kernel_test.py -v` | 7/7 PASS | 0.107884 | 0.116179 |
| `python -B H3_stability.py --output stability` | exact scalar assertions PASS | 0.121209 | 0.165867 |
| `python -B ../reviewer_checks.py` (absolute path used) | 6/6 PASS | 0.077837 | 0.116369 |

Extra computational checks consumed **2.510774 CPU seconds** in total; their
maximum child RSS was 20,920 KiB. Logs and exact commands are retained in
`shorttime_tests.log`, `circle_tests.log`, `stability.log`,
`reviewer_attacks.log`, and `extra_resources.json`.

The six additional independent attacks tested: Decimal exp/tanh against exact
rational Taylor/geometric-tail enclosures; nonzero-width current-state steps
against an independently computed rational exponential enclosure at all
selected rate/state corners; every Hermite covariance pair through degree
seven at both singular correlations ±1; the exact Peano-kernel integral and
quartic Simpson error; actual checkpoint continuation at zero duration and
the final horizon, including rejection past it; and actual-kernel oddness,
invalid/overwide coordinate boxes and rejection below 60-digit precision.
They introduce no new initialization quadrature or trained-flow run.

Main fresh output hashes:

| Artifact | SHA256 |
|---|---|
| capsule/run/result.json | `bfa5725d4cd649f60da7b505adfeba9a4f3d4fbd0f586c841f3b13c164bad149` |
| capsule/run/midpoint_checkpoint.json | `b259269d531197a0feb466c68e4a90459f86cf0763079619def1f7deee622e17` |
| capsule/run/kernel.json | `58d9743932e0f7c46321a2b2cd4e0bfaf06fc6bf631b9241fb23e73ff4d2bf61` |
| capsule/stability/result.json | `3a6cdfbfd5e9c59da71dff06f5b414c4e23d583c152302c2d37ed300e6e06445` |
| reviewer_checks.py | `7add7eea57959daef88226c12b7388ab96e22d17a63a898d9729216c1cd21744` |
| run_extra_checks.py | `e4b6f4a62b33c52f6dbcbcdaad3f068f10bd537cfb25002791c50bfd5417ae40` |

`output_hashes.json` retains a complete generated-file hash/size inventory.

## Information, storage, restart and limits

The general two-atom mathematical b/beta state has six scalar coordinates.
Reference symmetry reduces the executed moving state to b and diagonal beta.
Its checkpoint additionally retains seven initialized contraction intervals,
exact elapsed time, horizon, precision and original analytical error origin.
The circle object requires ten further intervals: q,v and eight spectral
masses. Thus the combined essential numerical values are **19 intervals / 38
Decimal endpoints**, plus the finite certificate/configuration metadata. This
count is not a claim that the complete program occupies 38 machine words.
The checkpoint is 2,123 bytes and the serialized kernel 2,883 bytes. The latter
also serializes four derived exact rational error quantities; in memory the
object stores coefficient centers, q center, tails, parameter/kernel errors
and midpoint Lipschitz bound as exact Fractions. Their integer numerator and
denominator storage is part of the measured resources.

The reference initializer streams 11 moment accumulators, retaining both
11-moment stages and their derivative/tail budgets for reporting; circle
initialization streams five accumulators and retains both five-integral
results. Polynomial derivative dictionaries, Hermite recurrence temporaries,
interval arithmetic intermediates, source/configuration objects, all three
observation reports, current/reloaded values and JSON serialization buffers
also consume memory. There is no tensor quadrature node array or expanding
history. The external peak RSS measurement includes these objects, Python
runtime/modules and arithmetic buffers, and is the complete observed memory
cost of this executed accuracy/configuration. The result JSON is 28,865 bytes,
and the circle configuration 2,616 bytes. No general-order or unrestricted
input-bit-length memory bound follows from this measurement; rational query
cost can grow with supplied input precision.

The saved endpoints round-trip without numerical loss. The actual driver
reloads both the midpoint coefficient record and kernel before continuation.
The exact identity for beta follows from `beta'=b'b`; b's closed scalar step
has the semigroup property. Interval evaluation preserves the previous
uncertainty even when dependence is lost. The direct/restarted overlap is a
sanity check, not the reason the restart is valid. Zero-duration and endpoint
attacks confirm that no artificial fresh initialization is substituted.
Elapsed time is certificate metadata used for a cumulative error envelope;
it is absent from the autonomous vector field. Loading arbitrary fabricated
positive coefficient files does not certify their canonical provenance, as
the candidate explicitly states.

The current source docstrings retain historical proof-note filenames not
present under those names in the capsule. The complete texts are nevertheless
present as the candidate files and are identified in RUN.md/candidate headers.
This is an editorial pointer cleanup for a later assembled edition, not a
missing scientific premise or a failed executable dependency here.

## Full original requirements: required additions and unresolved obligations

The complete stronger milestone remains open. To claim it, a revised package
must resolve all the following; this review authorizes no new research run.

1. **Effective family membership:** specify finite computable representations
   of a fixed nontrivial law family inside H2's supported neighborhood, with
   actual nonorthogonal and nonatomic examples and justified integration.
   The unknown positive H2 radius is not a numerical admission certificate.
2. **Terminating refinement:** construct or certify the nonlinear closure at
   every positive requested tolerance. The fixed Duhamel/kernel analytical
   remainder does not vanish as Simpson panels, Hermite degree or precision
   increase. The exact rational source-cap and propagation constants remove
   one bottleneck but produce no vanishing full closure defect.
3. **Effective source and integration errors:** replace qualitative compact-set
   convergence, exact unknown target curves and assumed omitted tails with
   computable initialization/closure/population/input error controls. H2's
   target-dependent proof errors cannot serve as runtime certificate inputs.
4. **All fixed admitted observation tuples:** implement and certify their
   joint same-population laws or the required distances, including action
   reuse and initial/current pairs. Two leading RMS scalars do not determine
   arbitrary joint observations, although the two scalars here are correctly
   paired and relative to canonical GF.
5. **Complete chosen-accuracy resources and continuation:** establish storage,
   conditioning, precision and work costs for the above representation and
   refinement, with every frozen/moving correlation and numerical buffer
   counted. Carry all accumulated error across its own-state restarts. The
   successful fixed-reference 5,006-byte checkpoint/kernel and measured RSS
   supply no such family/order theorem.
6. **Independent full demonstration:** reproduce the resulting broader solver
   under its frozen useful signal/error/resource thresholds, without fitting,
   neural trajectories, an arbitrary Gaussian-action oracle or retained
   history. The present reference demonstration meets its own thresholds
   completely but cannot substitute for the missing general construction.

These are major missing bridges to full C-H3, not evidence that such a solver
is impossible. They are consistent with the candidate's explicit limitations.
The original narrower proofs, unchanged input hashes, exact tests and this
fresh reproduction support retaining the bounded result at its stated scope.
