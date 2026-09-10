# Fresh independent scientific review B of signed promotion v1

Reviewer: `/root/signed_promotion_b`. Date: 2026-09-10.

## Decision and exact scope

**Scientific acceptance of the frozen addition: PASS.** I found no required
scientific or implementation correction. The result is a computer-assisted
positive cubic difference `R(g_tau(t))-R(f_t)` at equal mean training loss for
the specified two-hidden-layer tanh model, with an actual-population-flow
fourth-order remainder and unique matching clock. Its finite-width transfer
has the stated local, fixed-positive-time scope. This verdict does not grant
integration acceptance or the user's separate final promotion approval.

The decisive numerical evidence is the complete error argument together with
verified primitive provenance and arithmetic. I reconstructed every saved node
of both completed runs, reproduced the displayed rational endpoints exactly,
and separately reconstructed all nodes with a four-formal-slot implementation
of (C4.28)--(C4.30). The latter uses independent 112-bit outward interval
arithmetic, independently enclosed constants and primitive radii, and a
different contraction organization. It also proves the stated strict rational
sign bounds. No coefficient integration, training run, resolution change,
random experiment, or search was performed in this review.

## Isolation, inputs, and read coverage

My only task inputs were the neutral `SIGNED_PROMOTION_ASSIGNMENT.md`, the
frozen `signed_promotion_v1/manifest.json`, and its `packet/`, `edition/`, and
`evidence/` trees. I did not perform author startup, read the live study README,
study history, selector/internal reports, scientific reports, or another
reviewer's findings. I am absent from all nine authors/assemblers and the
selector named in the manifest. I did not stage, commit, reset, clone, or alter
any frozen or established input. My writes are this report and the assigned
`data/generated/two_layer_test_risk/signed_promotion_v1/reviewer_b/` scratch.
Root remains the sole Git writer.

I personally read `solve-math-rigorously/SKILL.md`,
`investigate-conjectures/SKILL.md` and its `adversarial-audit.md` reference,
and `review-ai-paper/SKILL.md` with its severity rubric. The neutral assignment's
single-report restriction takes precedence over the paper-review skill's
generic multiple-artifact layout. This report contains the evidence, claim,
code, and limitation records. The research skill's applicable scope, claim
ladder, error-production, limit-order, and adversarial rules were applied;
this was no new proof-search or experiment program. No external theorem or
literature claim was needed to complete the contained proof review.

The frozen manifest SHA256 is
`bef8b4af500bfef3e8a5f4234e239ac68e30c5891841280b0f38be55bfb2ffb3`.
All **16 packet, 18 edition, and 1,160 evidence file hashes** agree with it.
The full per-file path/hash/size inventory is retained in
`reviewer_b/input_hashes.json`; these hashes establish input identity, not
proof correctness.

Complete substantive reading was:

| Frozen input | Coverage |
|---|---|
| `packet/candidate.md` | Every line 1--1736, including every proof and executing-arithmetic paragraph. |
| `packet/dependencies.md` | Every line 1--1775: Section 2's applicable bounds/convergence/chain facts; all of Section 3's adaptive conditioning, both orientations, source response and singular regularization; A.1--A.4; all C.1 existence/convergence, C.2 response/tail proof, C.3 strict activity, and its weighted correction. |
| Dependency correspondence | Independently checked exact excerpt equality with edition global-nonlinear lines 181--500, 1835--1893, and 2449--3829. These are complete operative proof units, not merely statements. The candidate is the exact final suffix of the edition chapter. |
| `packet/NOTATION.md` | Every line 1--98. |
| Docs guide before/after | Complete 265-line before and 271-line after guides, including scientific motivation, chapter table, contextual bibliography and scope statements. |
| Code guide before/after | Complete 591-line before guide and complete after guide: the after guide's first 591 lines are byte-identical to the fully read before guide, and all 30 appended lines were read in the exact diff. |
| Tool guide | Complete `packet/README.md`, 169 lines. |
| Maintained numerical sources | Complete `certificate.py` 429 lines, kernel 236 lines, angular helper 88 lines, driver check 140 lines, and kernel check 161 lines. Packet/edition identities were verified. |
| Original executing source | Complete `original_numerical_source.py`, 382 lines; direct comparison of all numerical functions, the full node loop, and final assembly. |
| Other supplied check/assignments | Complete edition `check_library.py` 100 lines and both packet assignments. The separate integration assignment was read to keep verdict boundaries explicit. |
| Raw numerical evidence | Both metadata, constants, compile logs, complete result objects and all 64 lower/upper input, output, audit, stderr, and enclosure sets in each run; every numeric bit array was parsed, validated and consumed by reconstruction. |

The first combined manifest/file inventory output was truncated. I repaired
that access by structured parsing of every manifest group, a complete
per-file hash inventory, and focused metadata/source reads. One combined
before/after docs-guide display was truncated at their join; targeted reads
of before-guide lines 205--265 and after-guide lines 1--105 repaired the
omitted region. No candidate or dependency scientific read was truncated.
The unrelated remainder of the eight older book chapters was hash-checked,
not scientifically reviewed. This is not a whole-book audit.

No operative input is missing. Historical explanatory filenames in old run
metadata are provenance labels; the complete candidate proof is available in
the packet, and the original executing Python, unchanged kernel, and helper
are supplied and hash-matched.

## Claim ledger and scientific attacks

### 1. The exact model, flow identification, and normalization

Verdict: **sound for the stated fixed model**. The first stored matrix acts
with `1/sqrt(2)`, the middle matrix with no additional width factor, and the
stored linear readout with `1/n`. Initial variances are exactly `(1,1/n,1/n^2)`
and raw mobilities `(n,1,n)`. With the full mean square over three samples,
the field and operator equations have coefficient `-2/3`, and the initialized
forcing is `p=y/3`. A half-loss or sum-loss substitution would change the
clock and cubic coefficient; neither occurs in the proof or producer.

The specified Gram has rank two. Its correlations are `cos(pi/5)` and
`cos(2pi/5)`; labels at both nonzero training angles are `cos(3pi/5)`.
There is no whitening or independent-sample replacement. `G` is never
inverted. The different positive-activation constants at the beginning of
the older Section 2 are not used as tanh bounds: C.4 states and checks its own
bounded activation/derivative assumptions and uses Section 2 only for the
applicable general operator, continuity, and Gronwall facts.

I checked the C.1 construction rather than treating existence as a black-box
assertion. Finite joint programs are coupled on common generated L2 spaces;
initialized action inequalities pass to their spans and closures, and finite
adjunction identifies the actual adjoint. C.2's causal bounds retain each
single backward pulse's `Delta*omega_b`; its cap order is forward from bottom
to top, then backward from top to bottom, then a sufficiently small time.
The field bounds and expected-derivative bounds do not need their own future
values. Weighted exponential Jensen estimates need no temporal independence
or maximum of a Gaussian history. The one-reference tail inequality has
`C(1+R)` stability growth and `exp(-cR^2)` forcing, rather than an unproved
global Lipschitz property of the activation map on L2. This suffices for
Euler Cauchy convergence and uniqueness against an arbitrary strong solution
on the preliminary ball. The finite oracle/proxy comparison retains both
matrix orientations and uses the stated order `n`, fixed coarse mesh, then
cutoff removal. It does not infer a refining-mesh theorem from a fixed
finite program alone.

The vanishing stored Gaussian readout is covered by C.1's explicit RMS-small
initialization perturbation clause. Frozen zero hidden mobilities are allowed
by that theorem. Its finite-GF corollary uses a deterministic diagonal Euler
mesh after finite-width existence, rather than silently changing the claimed
joint raw-GD limit. All hypotheses used by C.4 hold for tanh and this fixed
dataset.

### 2. Initial Gaussian law and both uses of the same connector

Verdict: **sound, including singular passive covariances**. Pairwise
nonparallel directions and a bounded nonconstant tanh give a positive
training activation Gram by the contained ridge-difference proof; the
singular input Gram does not obstruct it. The upper training Gaussian then
has full support. Varying one coordinate proves `K>0`. The response-Gram
argument uses nonzero signed `p_a`, does not divide by `S`, and proves `V>0`.
Conditional Gaussian variance with nonzero lower gates proves `D>0`.

The reused transpose law has the bounded deterministic response plus an
innovation whose covariance is the **full** `E[U_a U_b]`. Subtracting a
response covariance would be an incorrect alternative. The next forward
law (C4.15) comes from the same matrix conditioned on training forward and
reverse calls. Its finite output projection costs only fixed rank divided
by width. Its coefficients use the fixed positive training Grams `Q,V`.
The input `A_x` is measurable before its own forward answer; the passive
first-layer field is already determined by the lower roots. No independence
of that forward innovation from a separately considered passive `Y_x`, or
between different passive innovations, is required or claimed.

For the explicit scalar formulas I derived `Lambda` from the conditional
product of two transpose answers. Gaussian integration by parts converts
`Q^-1 E[YF]` into expected formal-slot derivatives where invertible; the
contained singular regularization and source covariance identity justify
the same contraction at rank loss. Coincident or antipodal test slots stay
formally separate. Their null combinations are zero L2 combinations of
source inputs, so derivative-coordinate nonuniqueness cannot change the
answer. The mean-product term and the innovation term both remain in
`Lambda`. The independently implemented four-slot oracle checks this full
formula rather than only repeating the producer's expanded training-slot
expressions.

### 3. Actual-flow remainder, unique matching, and signed risk coefficient

Verdict: **sound**. The initialized fourth moments are proved in the correct
order: bounded training response means plus Gaussian innovations give
`P_b` finite L4 norm; bounded gates then give `T_x,A_x` uniformly finite
L4 norm; the forward conditional law gives uniform L4 norm for
`R_x^hid`. These estimates concern fixed initialized directions and make
no all-moment assertion about the trained trajectory.

The readout integral has an L-infinity representative of size `O(t)`.
Both hidden parameter velocities consequently start at `O(t)`, and their
increments are `O(t^2)`. The lower gate difference is `O_L4(t)` by boundedness
and Lipschitz continuity combined with its `O_L2(t^2)` argument difference;
Hölder against the fixed L4 response produces the required `O_L2(t)`
backward quotient error. Integration gives (C4.19)'s `O(t^3)` state errors.
The fixed-direction scalar Taylor estimate first removes the L2 error
through Lipschitz continuity, then uses the fixed direction's L4 norm;
it does not invoke false ambient Frechet smoothness of tanh on L2.

Exact readout subtraction (C4.22) retains both
`(f_b-g_b) H_b(0)` and the **actual moving residual** times the hidden
activation difference. Integral Gronwall gives `D^(3)=O_L2(t^3)`, after
which the residual difference contributes only an integrated `O(t^4)`.
The cubic readout correction is `(4/3)t^3 sum p_b E_b`, and the output
product contributes `4t^3 E[S E_x]`. Thus both hidden blocks and the readout
correction appear in the stated `J`. Cauchy--Schwarz bounds all remaining
products uniformly over the circle.

Adjunction gives `p^T J=(16/3) A` and `p^T a=2 B0`. Hence
`L_f-L_g=-(32/3)A t^3+O(t^4)` while `L_g'(0)=-4B0`; matching produces
`beta=8A/(3B0)`. Positivity comes from the Schur-product Gram argument with
positive diagonal, not the smallest eigenvalue of singular `G`.
The training projection of `J-beta*a` cancels exactly. Consequently the
positive training-speed coefficient cannot on its own determine the test
projection.

Unique matching is proved before expansion. Positive definite frozen `K`
makes its loss strictly decrease from the common initial loss to zero at
all finite frozen times. The trained energy inequality and the explicit
kernel norm bound keep the trained loss positive, with
`tau(t)<=B_K*t/lambda_min(K)`. Shrinking the local interval gives the clock
margin and a derivative lower bound for inverse comparison. The mean-value
argument first proves `tau-t=O(t^3)` and then obtains its coefficient and
fourth-order remainder. Squared-risk subtraction has sign
`2*cos(3alpha)*(J-beta*a)`, as defined; the opposite sign would contradict
the subtraction order. Its zero, linear and quadratic differences vanish.
The strictly positive enclosed cubic coefficient and the proved `Mt^4`
error yield exactly the stated small positive-time improvement.

### 4. Complete numerical error argument

Verdict: **sound under the explicit arithmetic/compiler contract**.

* The one-coordinate contour shift is legitimate for a bounded strip
  integrand times the Gaussian. Its vertical edges vanish, periodization
  converges uniformly, and the Fourier bound gives an absolutely convergent
  series. Tensor telescoping requires only separate strips with other
  coordinates real. Positive prior rule masses multiply each error;
  they are bounded by `1+delta_j`, not silently set to one. The removed
  Gaussian lattice tails are bounded from radius `m_j h_j` by monotonicity
  and the direct Gaussian tail integral.
* The exact dyadic grid has `a*c<=3/4<pi/4`,
  `6a/h-a^2/2>=26`, and `h^2<=18/26`; `pi>3` therefore supplies all
  required analytic inequalities. Radius and count gates are checked for
  every axis of every saved node. I separately checked the exact exponential
  partial-sum lower bounds at 26, 30 and 32. Their slack validates both
  documented rule envelopes, although no target-30 integration is asserted.
* The complex tanh bounds are valid on the stated strip. Real second,
  third and fourth derivative bounds follow from their displayed
  polynomials; the fourth derivative bound of five suffices. The product
  Hessian sums `4,6,10,18` and Price constants `2,3,5,9` include repeated
  slots. Gaussian covariance interpolation with `delta I` regularization
  proves its estimate for singular positive semidefinite endpoints.
  Lower direction error and upper factor discrepancy are charged
  separately. The latter uses exact dyadic `A A^T`, so the numerical solve,
  conditional variance, and possible clipping are never assumed exact.
* Every primitive receives the `10^-9` arithmetic radius, its Gaussian
  strip/tail radius, the appropriate covariance radius, and its label
  radius. Both exact and dyadic label absolute sums are checked below
  `27/50`. The error for `S^2` is `2P*epsilon_p`; that for a single `S`
  is `epsilon_p`. Signed weights remain inside all integrals and
  contractions. Training moments have three root dimensions and are not
  multiplied by the passive rule mass. The kernel's conditional inner
  integral preserves the original joint four-coordinate upper law.
* The degree-12 exponential's coefficient rounding plus 24 Horner
  operations is bounded by `gamma_25`; the alternating truncation gives
  the stated initial relative error below `46u`. Eight squarings have
  multiplicities 256 and 255. Exact rational checking proves the final
  bound below `2e-12`. The tanh ratio and saturation branches yield the
  stated global absolute bound. The proof explicitly charges rounded
  arguments, derivative-polynomial evaluation, Gaussian exponents and
  weight products. The maximum dot-product magnitude 72, count bound
  `401^3`, and long-double unit roundoff `2^-64` give the stated summation
  margin. Underflow is treated by absolute slack; overflow is excluded
  by the finite ranges. The deliberately looser `10^-9` primitive bound
  exceeds the assembled `<2.2e-10` accounting.
* Rational interval arithmetic rounds every endpoint outwards. Exact
  scalar Taylor coefficients are multiplied before rounding. Machin's
  identity, alternating arctangent remainders, integer square roots,
  trigonometric polynomial remainder and input-bit echoes close the
  input-constant and serialization obligations. Root proposals may use
  ordinary numerical linear algebra precisely because their exact
  covariance discrepancy is charged afterward.
* For the angle rule, the isonormal Gaussian construction differentiates
  the lower L2 curve, not a possibly singular passive Cholesky factor.
  Gaussian moments turn those derivatives into every required finite Lp
  derivative. Hölder and the finite Bell/Stirling expansions justify all
  expectation differentiations. I checked the four forward terms and
  three backward terms of (C4.A6)--(C4.A7): their bounds give exactly the
  coefficients `20/3,12,4,16/3` in (C4.A9), including both matrix responses.
  An independent integer-partition enumeration of Bell polynomials
  reproduces `D8=41272525446939874982/31640625` and
  `16 D8/(7*256^8)=20636262723469937491/127677049435953561600000000`.
  Eight integrations by parts and the roots-of-unity average yield the
  periodic error. The separate `|beta|<=1/10` premise is verified by each
  node's exact clock interval.
* Reflection with equal side labels and the passive antipodal sign prove
  evenness and pi-periodicity of the integrand. The teacher vanishes
  at pi/2. The weights `2/256` at zero and `4/256` at indices 1--63
  therefore represent the complete 256-point rule. The raw teacher
  projection, clock subtraction and their difference are reconstructed
  separately, and only then is the `10^-6` angular radius added.

### 5. Finite GF/GD capture and limitations

Verdict: **sound with the stated limit order**. Every circle first-layer
field is an exact bounded linear combination of two training fields, also
for affine parameter interpolation. The fixed norm ball and bounded
angular derivatives give a uniform angular Lipschitz estimate. Finite nets
and C.1's fixed correctly typed probes then give whole-circle prediction
convergence; boundedness transfers it to risk. No zero-weight extension
of the population theorem is needed.

Finite frozen GF has strictly decreasing loss when its empirical training
Gram is positive and its actual initial residual is nonzero; both events
have probability tending to one. For raw GD, eventual
`(2/3) eta_n lambda_max(K_n)<1` makes every frozen eigendirection strictly
contract without a sign crossing even inside the linear parameter
interpolation. On each fixed `[delta,T]`, trained finite losses lie inside
that frozen range with high probability. The population derivative lower
bound and uniform losses give uniform clock convergence. This transfers
the strictly positive minimum risk difference on `[delta,t0]`.

The common finite random readout is retained. The proof gives no uniform
finite-width sign down to time zero and no arbitrary choice `delta_n->0`.
It evaluates neither the local horizon nor the fourth-order constant, and
supplies no width rate, iid-average theorem, global-time improvement,
growing design/depth limit, universal feature benefit, or practical effect
size. No activity claim alone is used as a surrogate for the signed risk
conclusion. These limitations are accurately reflected in the guides.

## Executing source, raw evidence, and independent reconstruction

The maintained source SHA256 is
`36dd0b21dea51647dcbb9aef7c958d8f2ddadc397529e629ada5b122af0d2810`;
the original executing Python SHA256 is
`a2e49e1c635b347e6542372bbdb4fb8ad3438e6c923e4292dc79964a000d48e1`.
The kernel SHA256 is
`9d7bbcd743e465ae0e4caacd0f1e670d78283e1388a2fe48bda6193ef0e66ad9`.
The original run metadata names exactly this numerical Python and kernel,
and the unchanged angular helper. The two original compiler command arrays
use `g++ -O3 -std=c++17 -fno-fast-math -ffp-contract=off`.

Direct AST comparison, with docstrings removed but all executable operations
retained, gives equality for all 20 pre-run functions/classes, the complete
64-node loop, and the final interval/decision assembly. I also read the
source differences. They remove study/Git dependencies, resolve the kernel
beside its source, add public argument validation and a fresh worker, and
improve failure metadata. They do not change constants, grids, primitive
inputs, operation order, error radii, root proposals, contractions, or
matching subtraction. The compiler-version query moves into accounted
execution; this affects timing provenance, not coefficient arithmetic.
This is my own source comparison, not an author equivalence verdict.

The supplied full runs are:

| Evidence directory | Recorded command | Recorded CPU / wall seconds |
|---|---|---|
| `evidence/certificate_20260910_01` | `studies/two_layer_test_risk/certificate_driver.py --target 26 --output data/generated/two_layer_test_risk/certificate_20260910_01` | 31.17975 / 31.13373264670372 |
| `evidence/certificate_reproduction_20260910_01` | `/home/amir/Codes/PDE/studies/two_layer_test_risk/certificate_driver.py --target 26 --output /home/amir/Codes/PDE/data/generated/two_layer_test_risk/certificate_reproduction_20260910_01` | 30.667729999999995 / 30.621354784816504 |

Both metadata files record working directory `/home/amir/Codes/PDE`, Python
3.10.12, NumPy 1.26.4, Linux x86_64/glibc 2.35 and g++ 11.4.0. Their command
arrays identify script arguments, not a separately reconstructed shell
invocation. I did not rerun those commands. Their result JSONs independently
hash to
`89815a7b16fb69f51683834049b370256fd32aba26528630f4c4f6b427fe406d`.
The fresh focused build in this review produces binary SHA256
`8c5b241801eaa4b8912989b9e404eb9693e63e94487661071c3bfa7044c189c7`,
exactly the binary hash recorded by both runs. Binary identity is supporting
correspondence evidence; it is not substituted for the error proof.

For every one of the 128 node pairs I checked both modes, all input counts
and lengths, intended versus echoed binary64 bits, finite output bits,
every tensor shape, long-double precision, outer and total node counts,
all one-dimensional masses, exact grid selections and inequalities, and
the input/output hashes in its audit. All stderr and compile logs are
empty. The exact lower-direction inputs and labels regenerate from the
stated constants. Root-factor recomputation from saved lower moments
matches the supplied upper inputs, including the tiny nonzero passive
factor at angle zero; its discrepancy is charged, not treated as exact
zero. Every covariance/label error and all seven saved scalar intervals
per node reproduce exactly, as do teacher intervals, raw/clock terms,
cumulative sums, final clock intersection and final risk bounds.
Each run accounts for **86,101,134 upper nodes** in its recorded integration.

The exactly replayed final risk bounds are

```
5358604107658561212253567/19807040628566084398385987584
<= chi <=
21597479156841685713774185/79228162514264337593543950336
```

and the exactly replayed clock bounds are

```
2797504526179671494928101665/79228162514264337593543950336
<= beta <=
2797556156441557459457527739/79228162514264337593543950336.
```

Independent four-slot assembly instead gives, for each raw run,

```
1404725688299265884392478181589/5192296858534827628530496329220096
<= chi <=
707706310460780788766131078031/2596148429267413814265248164610048.
```

This is approximately `[0.0002705403266745527, 0.0002725985550296455]`.
It differs slightly because interval dependencies and rounding are organized
differently. Exact comparisons, not these decimals, put it strictly within
`(27/100000,273/1000000)`; its clock interval lies strictly within
`(35309/1000000,35311/1000000)`. All 64 independent node intervals in each
run overlap their saved counterparts. The independent source constructs
the full four-slot derivative vectors and evaluates generic `Lambda` and
`C_a`, instead of copying the producer's three-slot expanded F/B sums.
The complete per-node independent intervals are retained in the two
`reviewer_b/*_independent.json` files. Agreement of runs or intervals is
not used to replace the analytic radii.

## Standalone execution and interface review

All new tool imports and commands were exercised from the standalone edition;
none required a study path, live code tree, Git, network, or archived arrays
as a runtime input. The saved-bit verification naturally reads the frozen
evidence as its explicit review input. The public success path was tested
with a mocked worker for launching/result ownership only; this is labeled
separately and supplies no numerical proof evidence.

The exact maintained focused commands used the edition as working directory:

```sh
ulimit -t 60
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B code/tools/two_layer_risk/check_driver.py --output /home/amir/Codes/PDE/data/generated/two_layer_test_risk/signed_promotion_v1/reviewer_b/driver
```

```sh
ulimit -t 60
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B code/tools/two_layer_risk/check_kernel.py --output /home/amir/Codes/PDE/data/generated/two_layer_test_risk/signed_promotion_v1/reviewer_b/kernel
```

```sh
ulimit -t 60
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B code/tools/two_layer_risk/angle_error_bound.py --output /home/amir/Codes/PDE/data/generated/two_layer_test_risk/signed_promotion_v1/reviewer_b/angle
```

All exited zero. The driver check took 3.118 seconds wall time and passed
longer rational series, square roots, grids, direct supplied-table response
contractions and the exact symmetry-weight identity. The kernel check took
0.820 seconds wall time; its largest direct-tensor discrepancy was
`5.88418203051333e-15`, below `10^-9`, and its singular omitted-root branch
used 27 supplied nodes. All 19 primitive checks passed their rational
oracles. These are finite supplied-state checks, not extra Gaussian
coefficient integrations. The angular helper's exact output agrees with
the separate Bell-partition calculation above.

The unique review program was executed from the same edition directory as:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B /home/amir/Codes/PDE/data/generated/two_layer_test_risk/signed_promotion_v1/reviewer_b/review_b_checks.py inventory
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B /home/amir/Codes/PDE/data/generated/two_layer_test_risk/signed_promotion_v1/reviewer_b/review_b_checks.py inequalities
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B /home/amir/Codes/PDE/data/generated/two_layer_test_risk/signed_promotion_v1/reviewer_b/review_b_checks.py interfaces
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B /home/amir/Codes/PDE/data/generated/two_layer_test_risk/signed_promotion_v1/reviewer_b/review_b_checks.py reconstruct 0
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B /home/amir/Codes/PDE/data/generated/two_layer_test_risk/signed_promotion_v1/reviewer_b/review_b_checks.py reconstruct 1
```

The program imposes `RLIMIT_CPU=(60,60)` at entry. The initial combined
`reconstruct` invocation, without a run index, was killed at that cap
(exit 137) after completing the first run and before completing the second.
It supplied no combined PASS. I changed only selection/output bookkeeping
to allow one evidence run per bounded check; the oracle and arithmetic
were unchanged. The separate reconstructions completed in 44.235 and 44.860 CPU
seconds, respectively, both with exit status zero. Results, exact run timing, check-source hashes and all outcomes
are retained in `reviewer_b/inventory.json`, `inequalities.json`,
`interfaces.json`, `reconstruction_0.json`, and `reconstruction_1.json`.
This capped failed attempt is a review-computation record, not a producer
failure or an additional coefficient run.

The interface tests establish: import does not change the caller's
environment; CLI help exits zero without compilation; invalid output types,
empty/NUL/byte paths, existing paths and dangling final symlinks fail before
work; boolean, floating, string and unsupported targets fail with the
documented exception classes; optimized Python fails without creating an
output directory. The worker receives one-thread environment settings in
the launch call; returned JSON is freshly read and independently mutable.
Worker failure is propagated. An actual fresh worker with the compiler
absent from PATH records failed metadata, raises through the public API,
and produces no result or Gaussian integration. Kernel negative tests
reject unknown mode, empty primitive count, nonfinite input, omission of a
nonzero passive root, and omission of a lower root.

Static review also verifies the public fresh-directory race is closed by
the worker's `mkdir(exist_ok=False)`, parameter paths are passed as argument
lists, and the kernel is found relative to source. Partial failures after
metadata initialization preserve their diagnostic files. The guide correctly
describes the 900-second cumulative CPU checks as gates around primitive
calls, not a hard process/compiler timeout; kernel children have their
separate CPU and wall limits. No unsupported whole-process resource guarantee
was inferred. Direct use of private helpers is not part of the public API.

## Concerns, confidence, and boundaries of acceptance

There are **no unresolved blocking scientific objections** and no required
corrections. The conclusions and their proof are highly plausible and sound
over the stated scope. Confidence is high because all operative mathematical
proof bodies, every numerical operation and error axis, all saved node
contracts, and independent reconstruction were checked; this is not a claim
of formal machine verification or a re-audit of the unrelated library.

One strictly nonblocking editorial observation: the kernel's second comment
line still says `See CERTIFICATION_ENGINE.md`. The maintained complete
specification is in C.4 and the adjacent tool guide, and no runtime or proof
step loads that historical filename. This does not require a correction for
scientific acceptance. It must not be silently edited into this accepted
frozen packet; any later cleanup remains a separately reviewable change.

The two supplied full integrations are prior recorded executions whose raw
evidence I verified; I did not claim to perform a third fresh integration.
No target-30 full run, wide-network training experiment, quantitative time
window or width threshold was produced. Mocked interface testing is not
numerical evidence. This report addresses the scientific promotion gate;
the independent integration review and explicit user approval remain
separate.

## Retained unique verification source

The complete independent check source follows so its distinctive oracle,
commands and checks survive independently of scratch retention. The final
source SHA256 is recorded below and in completed reconstruction records.
The earlier pre-split version differed only by looping over both runs
unconditionally and writing `reconstruction.json` with fixed counts 128/896;
its SHA256 was
`7cb9ecde07a5e1b117304152767acad97237d7eab06b6a41d30f5d683dffc651`.

Final check-source SHA256: `0f9a33d59cf2859b81c04bbf2c1b5632157bda37e30ccc1a6c6ceeec1f325e53`.

```python
"""Reviewer B's independent checks; never performs a coefficient integration.

Modes are separate <=60 CPU-second checks.  Reconstruct reads primitive bits,
replays the supplied assembler for exact endpoint correspondence, and uses an
independent four-formal-slot implementation of C4.28 with 112-bit outward boxes.
"""
import ast
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import resource
import struct
import subprocess
import sys
import time
from unittest import mock

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
EDITION = BASE/'edition'
SRC = EDITION/'code/tools/two_layer_risk/certificate.py'
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
START = time.process_time()

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p): return json.loads(Path(p).read_text())
def unbit(b): return struct.unpack('=d', struct.pack('=Q', b))[0]
def bit(v): return struct.unpack('=Q', struct.pack('=d', v))[0]
def load():
    spec=importlib.util.spec_from_file_location('reviewed',SRC)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod
def save(name, result):
    result.update(cpu_seconds=time.process_time()-START, source_sha256=sha(__file__))
    (HERE/(name+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

class Box:
    """Independent endpoint implementation, 112-bit outward rounding."""
    scale=1<<112
    def __init__(self,a=0,b=None):
        if isinstance(a,Box): self.lo,self.hi=a.lo,a.hi;return
        a=F(a);b=a if b is None else F(b)
        self.lo=F(a.numerator*self.scale//a.denominator,self.scale)
        self.hi=F(-((-b.numerator*self.scale)//b.denominator),self.scale)
        assert self.lo<=self.hi
    def __add__(self,b):
        if not isinstance(b,Box): b=Box(b)
        return Box(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return Box(-self.hi,-self.lo)
    def __sub__(self,b):return self+-Box(b)
    def __rsub__(self,b):return Box(b)+-self
    def __mul__(self,b):
        if isinstance(b,Box):
            ps=[x*y for x in (self.lo,self.hi) for y in (b.lo,b.hi)]
        else:ps=[self.lo*F(b),self.hi*F(b)]
        return Box(min(ps),max(ps))
    __rmul__=__mul__
    def __truediv__(self,b):
        if not isinstance(b,Box):return self*F(1,b)
        assert b.lo*b.hi>0
        return self*Box(1/b.hi,1/b.lo)
    def __rtruediv__(self,b):return Box(b)/self
    def __pow__(self,n):
        out=Box(1)
        for _ in range(n):out=out*self
        return out
    def radius(self):return max(abs(self.lo),abs(self.hi))
    def widen(self,r):return Box(self.lo-r,self.hi+r)
    def data(self):return {'lo':str(self.lo),'hi':str(self.hi),'lo_display':float(self.lo),'hi_display':float(self.hi)}

def sqrtbox(v):
    v=Box(v);s=Box.scale
    low=math.isqrt(v.lo.numerator*s*s//v.lo.denominator)
    high=math.isqrt(v.hi.numerator*s*s//v.hi.denominator)+1
    return Box(F(low,s),F(high,s))
def independent_constants():
    def atan(q):
        v=sum(F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(100))
        return Box(v,v+F(1,201*q**201))
    pi=16*atan(5)-4*atan(239)
    labels=[Box(F(1,3)),(1-sqrtbox(5))/12,(1-sqrtbox(5))/12]
    return pi,labels,1/sqrtbox(2*pi)
def trig(x,sine=False):
    x=Box(x);assert x.radius()<=5
    out=Box()
    for k in range(40):
        r=2*k+int(sine)
        out=out+x**r*F((-1)**k,math.factorial(r))
    return out.widen(F(5**80,math.factorial(80)))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),Box())
def overlap(a,b):return max(a.lo,F(b['lo']))<=min(a.hi,F(b['hi']))

def four_slot(lower,upper,p):
    """Literal C4.28--C4.30. No three-slot expanded F/B source copied."""
    p=p+[Box(0)]
    Q,L,T,G=(lower[k] for k in ('Q','L','T','G'))
    def q(a,b):return Q[4*a+b]
    def lam(a,b,cross,df,dg):
        return L[4*a+b]*cross+sum((T[64*a+16*b+4*i+j]*df[i]*dg[j]
                   for i in range(4) for j in range(4)),Box())
    def mean_u(a):
        if a==3:return [p[i]*upper['dynamic_dd'][i] for i in range(3)]+[upper['dynamic_ESdd'][0]]
        return [p[i]*upper['ddgram'][3*i+a]+(upper['ESdd'][a] if i==a else 0)
                for i in range(3)]+[Box()]
    means=[mean_u(a) for a in range(4)]
    def C(a,cross,df):
        return sum((p[b]*(q(a,b)*cross[b]+G[a][b]*lam(a,b,cross[b],df,means[b]))
                    for b in range(3)),Box())
    A=sum((p[a]*C(a,upper['V'][3*a:3*a+3],means[a]) for a in range(3)),Box())
    forward=C(3,upper['dynamic_V'],means[3])
    backward=Box()
    for a in range(3):
        df=[Box() for _ in range(4)]
        df[3]=upper['dynamic_dd'][a]
        df[a]=upper['dynamic_Hdd'][a]
        backward=backward+p[a]*C(a,upper['dynamic_C'][3*a:3*a+3],df)
    B0=upper['ES2'][0]
    assert B0.lo>0
    beta=8*A/(3*B0)
    assert beta.radius()<F(1,10)
    return dict(A=A,B0=B0,beta=beta,J=4*forward+backward*F(4,3),
                a=2*upper['dynamic_SH'][0],F=forward,B=backward)

def independently_enclose(rawlo,rawhi,dirs,uf,factor,p,pf):
    P=F(27,50)
    G=[[dot(a,b) for b in dirs] for a in dirs]
    Gh=[[sum(F(x)*F(y) for x,y in zip(a,b)) for b in uf] for a in uf]
    eg=max((G[a][b]-Gh[a][b]).radius() for a in range(4) for b in range(4))
    def enclose(raw,key,strip,real,price,eps,label):
        r=F(1,10**9)+F(5,10**11)*strip+F(6,10**15)*real+price*eps+label
        return [Box(F(unbit(v))).widen(r) for v in raw[key+'_bits']]
    lower=dict(Q=enclose(rawlo,'Q',1,1,2,eg,0),L=enclose(rawlo,'L',4,1,3,eg,0),
               T=enclose(rawlo,'T',4,1,9,eg,0),G=G)
    Qh=[[sum(F(x)*F(y) for x,y in zip(a,b)) for b in factor] for a in factor]
    eq=max((lower['Q'][4*a+b]-Qh[a][b]).radius() for a in range(4) for b in range(4))
    ep=sum((p[a]-F(pf[a])).radius() for a in range(3))
    specs={'ES2':(P*P,P*P,2*P*P,2*P*ep),'V':(4*P*P,P*P,9*P*P,2*P*ep),
           'dynamic_V':(4*P*P,P*P,9*P*P,2*P*ep),'ddgram':(4,1,3,0),
           'dynamic_dd':(4,1,3,0),'ESdd':(4*P,P,5*P,ep),
           'dynamic_ESdd':(4*P,P,5*P,ep),'dynamic_C':(4*P,P,9*P,ep),
           'dynamic_Hdd':(4,1,5,0),'dynamic_SH':(P,P,2*P,ep)}
    upper={k:enclose(rawhi,k,s,r,c,eq,e) for k,(s,r,c,e) in specs.items()}
    return lower,upper,eg,eq,ep

def inventory():
    manifest=read(BASE/'manifest.json')
    assert sha(BASE/'manifest.json')=='bef8b4af500bfef3e8a5f4234e239ac68e30c5891841280b0f38be55bfb2ffb3'
    checked=[]
    for group in ('packet','edition','evidence'):
        for rel,digest in manifest[group+'_sha256'].items():
            path=BASE/group/rel;assert sha(path)==digest,(group,rel)
            checked.append(dict(path=str(path.relative_to(BASE)),sha256=digest,bytes=path.stat().st_size))
    old=ast.parse((BASE/'packet/original_numerical_source.py').read_text())
    new=ast.parse(SRC.read_text())
    def functions(tree):return {n.name:n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
    def clean(n):
        for a in ast.walk(n):
            if isinstance(a,(ast.FunctionDef,ast.ClassDef)) and isinstance(a.body[0],ast.Expr) and isinstance(a.body[0].value,ast.Constant) and isinstance(a.body[0].value.value,str):a.body=a.body[1:]
        return ast.dump(n,include_attributes=False)
    o,n=functions(old),functions(new)
    names=[k for k in o if k!='run']
    assert all(clean(o[k])==clean(n[k]) for k in names)
    def mainloop(tree):return next(a for a in ast.walk(tree) if isinstance(a,ast.For) and ast.unparse(a.target)=='j' and ast.unparse(a.iter)=='range(64)')
    assert clean(mainloop(o['run']))==clean(mainloop(n['run']))
    def between(tree,first,last):
        body=next(a.body for a in ast.walk(tree) if isinstance(a,ast.Try))
        text=[ast.unparse(a) for a in body]
        i=next(i for i,x in enumerate(text) if x.startswith(first));j=next(i for i,x in enumerate(text) if x.startswith(last))
        return text[i:j+1]
    assert between(o['run'],'chi =','print(')==between(n['run'],'chi =','print(')
    a=(BASE/'packet/code_README_before.md').read_bytes();b=(BASE/'packet/code_README_after.md').read_bytes();assert b.startswith(a)
    deps=(BASE/'packet/dependencies.md').read_text()
    chapter=(EDITION/'docs/global_nonlinear.md').read_text().splitlines()
    for start,end in [(181,500),(1835,1893),(2449,3829)]:
        assert '\n'.join(chapter[start-1:end]) in deps,(start,end)
    assert (EDITION/'docs/global_nonlinear.md').read_text().endswith((BASE/'packet/candidate.md').read_text())
    (HERE/'input_hashes.json').write_text(json.dumps(checked,indent=2)+'\n')
    save('inventory',dict(status='PASS',manifest_sha256=sha(BASE/'manifest.json'),
         files_hashed=len(checked),identical_numerical_units=names,
         identical_full_node_loop=True,identical_final_assembly=True,
         dependency_excerpts_exact=True,code_guide_unchanged_prefix_bytes=len(a)))

def contracts(folder,mode):
    txt=(folder/(mode+'_input.txt')).read_text().split()
    q=2 if mode=='lower' else 4
    assert txt[0]==mode
    counts=list(map(int,txt[1:q+1]));vals=list(map(float,txt[q+1:]))
    assert len(vals)==(11 if q==2 else 24)
    obj=read(folder/(mode+'_stdout.json'));audit=read(folder/(mode+'_audit.json'))
    assert obj['mode']==mode and audit['mode']==mode
    assert obj['parsed_input_bits']==[bit(x) for x in vals]
    assert obj['long_double_mantissa_bits']>=64
    assert obj['total_points']==math.prod(2*m+1 for m in counts)==audit['total_points']
    assert obj['outer_points']==(obj['total_points'] if q==2 else math.prod(2*m+1 for m in counts[:3]))
    assert len(obj['grid_mass_bits'])==q
    assert all(abs(F(unbit(v))-1)<F(1,10**8) for v in obj['grid_mass_bits'])
    for k,v in obj.items():
        if k.endswith('_bits') and isinstance(v,list):assert all(math.isfinite(unbit(x)) for x in v)
    shapes={'Q':16,'L':16,'T':256} if q==2 else {'ES2':1,'V':9,'ddgram':9,'ESdd':3,'dynamic_V':3,'dynamic_C':9,'dynamic_dd':3,'dynamic_ESdd':1,'dynamic_Hdd':3,'dynamic_SH':1}
    assert all(len(obj[k+'_bits'])==n for k,n in shapes.items())
    assert audit['input_sha256']==sha(folder/(mode+'_input.txt'))
    assert audit['output_sha256']==sha(folder/(mode+'_stdout.json'))
    assert (folder/(mode+'_stderr.txt')).read_text()==''
    matrix=[vals[q+1+i*q:q+1+(i+1)*q] for i in range(4)]
    assert all(abs(F(x))<=2 for row in matrix for x in row)
    for j,(m,h) in enumerate(zip(counts,vals[:q])):
        if m==0:
            assert q==4 and j==3 and h==0 and all(row[3]==0 for row in matrix)
            continue
        h=F(h);c=max(abs(F(row[j])) for row in matrix)
        a=min(F(7),F(3,4)/c) if c else F(7)
        hstar=6*a/(26+a*a/2)
        assert h==F(hstar.numerator*1024//hstar.denominator,1024)
        assert m==(8*h.denominator+h.numerator-1)//h.numerator
        assert 0<h<=1 and 1<=m<=200 and 8<=m*h<=9
        assert a*c<=F(3,4) and 6*a/h-a*a/2>=26 and h*h<=F(18,26)
        assert audit['grid'][j]==dict(c=str(c),a=str(a),h=str(h),m=m,exponent_lower=str(6*a/h-a*a/2))
    if q==4:assert all(row[3]==0 for row in matrix[:3])
    return obj,matrix,vals

def reconstruct():
    drv=load();pi,p,normal,nf=drv.constants();ipi,ip,inormal=independent_constants()
    outputs=[]
    selected = int(sys.argv[2]) if len(sys.argv)>2 else None
    runs=sorted((BASE/'evidence').iterdir())
    if selected is not None:runs=[runs[selected]]
    for run in runs:
        meta=read(run/'metadata.json');result=read(run/'result.json')
        assert meta['source_sha256']['certificate_driver.py']==sha(BASE/'packet/original_numerical_source.py')
        assert meta['source_sha256']['certificate_kernel.cpp']==sha(BASE/'packet/certificate_kernel.cpp')
        assert meta['source_sha256']['angle_error_bound.py']==sha(BASE/'packet/angle_error_bound.py')
        assert meta['result_sha256']==sha(run/'result.json')
        assert meta['configuration']['target']==26 and meta['configuration']['evaluated_indices']==list(range(64))
        assert meta['exit_status']==0 and meta['cpu_seconds']<900
        assert meta['compile_command'][1:5]==['-O3','-std=c++17','-fno-fast-math','-ffp-contract=off']
        assert (run/'compile.log').read_text()==''
        assert read(run/'constants.json')==dict(pi=pi.json(),p=[v.json() for v in p],normal=normal.json(),normal_float_bits=bit(nf))
        total=drv.I();raw=drv.I();clock=drv.I();common=None
        independent=Box();iraw=Box();iclock=Box();icommon=None;rows=[];nodes=0
        for j in range(64):
            folder=run/f'angle_{j:03d}'
            lo,uf,lvals=contracts(folder,'lower');hi,factor,uvals=contracts(folder,'upper')
            assert lvals[2]==nf==uvals[4] and (inormal-F(nf)).radius()<F(1,10**15)
            dirs=drv.directions(pi,j);pf=uvals[-3:]
            assert uf==[[v.midfloat() for v in row] for row in dirs]
            assert pf==[v.midfloat() for v in p] and sum(abs(F(v)) for v in pf)<F(27,50)
            # Root proposals, not integrations. Comparison checks run correspondence.
            proposed,var=drv.root_factor(lo);assert proposed==factor
            lower=drv.lower_intervals(lo,dirs,uf,26)
            upper=drv.upper_intervals(hi,lower,factor,p,pf,26)
            c=drv.contraction(lower,upper,p);saved=read(folder/'enclosure.json')
            assert c.keys()==saved['moments'].keys()
            assert all(v.json()==saved['moments'][k] for k,v in c.items())
            assert str(lower['epsilon_first_covariance'])==saved['epsilon_first_covariance']
            assert str(upper['epsilon_upper_covariance'])==saved['epsilon_upper_covariance']
            assert str(upper['epsilon_labels'])==saved['epsilon_labels']
            assert var==saved['heuristic_conditional_variance'] and saved==result['rows'][j]
            common=c['beta'] if common is None else drv.I(max(common.lo,c['beta'].lo),min(common.hi,c['beta'].hi))
            teacher=drv.trig(6*pi*F(j,256),'cos');weight=F(2 if j==0 else 4,256)
            r=2*weight*teacher*c['J'];s=2*weight*teacher*c['beta']*c['a']
            raw+=r;clock+=s;total+=r-s
            assert r.json()==saved['weighted_raw'] and s.json()==saved['weighted_clock'] and total.json()==saved['cumulative']
            assert teacher.json()==saved['teacher'] and (2*pi*F(j,256)).json()==saved['alpha']
            angles=[Box(),ipi/5,-ipi/5,2*ipi*F(j,256)]
            idirs=[[trig(a),trig(a,True)] for a in angles]
            il,iu,eg,eq,ep=independently_enclose(lo,hi,idirs,uf,factor,ip,pf)
            ic=four_slot(il,iu,ip)
            assert all(overlap(v,saved['moments'][k]) for k,v in ic.items())
            it=trig(6*ipi*F(j,256));r=2*weight*it*ic['J'];s=2*weight*it*ic['beta']*ic['a']
            iraw+=r;iclock+=s;independent+=r-s
            icommon=ic['beta'] if icommon is None else Box(max(icommon.lo,ic['beta'].lo),min(icommon.hi,ic['beta'].hi))
            nodes+=hi['total_points']
            assert hi['total_points']==saved['upper_points'] and lo['total_points']==saved['lower_points']
            rows.append(dict(index=j,moments={k:v.data() for k,v in ic.items()},
                 epsilon_G=str(eg),epsilon_Q=str(eq),epsilon_p=str(ep)))
        aggregate=dict(nodal_sum=total,raw_nodal_projection=raw,clock_nodal_subtraction=clock,
                       beta_intersection=common,chi=total.widen(F(1,10**6)))
        assert all(v.json()==result[k] for k,v in aggregate.items())
        assert nodes==86101134==result['total_upper_nodes']
        ichi=independent.widen(F(1,10**6))
        assert F(27,100000)<ichi.lo<ichi.hi<F(273,1000000)
        assert F(35309,1000000)<icommon.lo<icommon.hi<F(35311,1000000)
        assert overlap(ichi,result['chi'])
        detail=dict(run=run.name,nodes=nodes,chi=ichi.data(),beta=icommon.data(),
                    nodal_sum=independent.data(),raw=iraw.data(),clock=iclock.data(),rows=rows)
        (HERE/(run.name+'_independent.json')).write_text(json.dumps(detail,indent=2)+'\n')
        outputs.append({k:v for k,v in detail.items() if k!='rows'})
    save('reconstruction'+('' if selected is None else '_'+str(selected)),dict(status='PASS',raw_node_pairs_checked=len(runs)*64,
         replayed_scalar_enclosures=len(runs)*64*7,independent_four_slot_node_enclosures=len(runs)*64,
         primitive_integrations=0,runs=outputs))

def interfaces():
    before=os.environ.copy();drv=load();assert os.environ==before
    checked=[]
    with mock.patch.object(drv.subprocess,'run',side_effect=AssertionError('unexpected computation')):
        invalid=[(None,26,TypeError),('',26,ValueError),(b'bytes',26,TypeError),
                 ('bad\x00path',26,ValueError),(HERE,26,FileExistsError)]
        for target,typ in [(True,TypeError),(26.0,TypeError),('26',TypeError),(25,ValueError),(0,ValueError)]:
            invalid.append((HERE/'must_not_exist',target,typ))
        for output,target,typ in invalid:
            try:drv.certify(output,target)
            except typ:checked.append([repr(output),repr(target),typ.__name__])
            else:raise AssertionError('invalid request accepted')
        link=HERE/'dangling_output';link.symlink_to(HERE/'absent')
        try:
            try:drv.certify(link)
            except FileExistsError:checked.append(['dangling symlink','26','FileExistsError'])
            else:raise AssertionError('dangling output accepted')
        finally:link.unlink()
    assert not (HERE/'must_not_exist').exists()
    fresh=HERE/'fake_worker_result'
    def fake_run(command,**kwargs):
        assert command[0]==sys.executable and command[1]=='-B' and command[-1]=='--_worker'
        assert kwargs['check'] is True
        assert all(kwargs['env'][k]=='1' for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'))
        dest=Path(command[command.index('--output')+1]);assert dest==fresh
        dest.mkdir();(dest/'result.json').write_text('{"rows": [1], "decision": "INCONCLUSIVE"}')
        return subprocess.CompletedProcess(command,0)
    with mock.patch.object(drv.subprocess,'run',side_effect=fake_run):got=drv.certify(fresh)
    got['rows'].append(2);assert read(fresh/'result.json')['rows']==[1] and os.environ==before
    with mock.patch.object(drv.subprocess,'run',side_effect=subprocess.CalledProcessError(1,['fake'])):
        try:drv.certify(HERE/'failed_no_output')
        except subprocess.CalledProcessError:checked.append(['worker failure','26','CalledProcessError'])
        else:raise AssertionError('worker failure swallowed')
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    help_run=subprocess.run([sys.executable,'-B',str(SRC),'--help'],cwd=EDITION,env=env,capture_output=True,text=True)
    assert help_run.returncode==0 and '--output' in help_run.stdout and '--target' in help_run.stdout
    (HERE/'help.txt').write_text(help_run.stdout)
    opt=subprocess.run([sys.executable,'-O','-B',str(SRC),'--output',str(HERE/'optimized_rejected')],cwd=EDITION,env=env,capture_output=True,text=True)
    assert opt.returncode!=0 and 'without -O or -OO' in opt.stderr and not (HERE/'optimized_rejected').exists()
    (HERE/'optimized_stderr.txt').write_text(opt.stderr)
    # Actual worker failure before Gaussian integration: omit compiler from PATH.
    env['PATH']='/nonexistent'
    bad=subprocess.run([sys.executable,'-B',str(SRC),'--output',str(HERE/'compiler_failure')],cwd=EDITION,env=env,capture_output=True,text=True)
    assert bad.returncode!=0 and read(HERE/'compiler_failure/metadata.json')['status']=='failed'
    assert not (HERE/'compiler_failure/result.json').exists()
    (HERE/'compiler_failure_stderr.txt').write_text(bad.stderr)
    binary=HERE/'kernel/certificate_kernel'
    root=[.5,0,0,0,.375,.125,.25,0,.375,.125,-.25,0,.25,-.125,.25,.125]
    vals=[.5,.5,.5,0,.3989422804014327]+root+[.25,-.125,-.0625]
    bad_inputs=['unknown\n','primitives\n0\n','primitives\n1\nnan\n',
      'upper\n1 1 1 0\n'+' '.join(map(str,vals))+'\n',
      'lower\n0 1\n0 .5 .3989422804014327 1 0 1 0 1 0 1 0\n']
    errors=[]
    for body in bad_inputs:
        proc=subprocess.run([str(binary)],input=body,text=True,capture_output=True)
        assert proc.returncode!=0;errors.append(proc.stderr.strip())
    save('interfaces',dict(status='PASS',invalid_api_cases=checked,import_environment_unchanged=True,
         mocked_worker_scope='launch and result ownership only; no arithmetic evidence',
         fresh_worker_configuration=True,mutable_result_independent=True,help_exit=help_run.returncode,
         optimized_exit=opt.returncode,actual_missing_compiler_exit=bad.returncode,kernel_rejections=errors))

def inequalities():
    u=F(1,2**53)
    gamma=lambda n,v=u:n*v/(1-n*v)
    d0=F(16,9)*gamma(25)+F(4,3)*F(1,4)**13/math.factorial(13)
    assert d0<46*u
    assert (1+46*u)**256*(1+u)**255-1<F(2,10**12)
    assert 4*gamma(401**3,F(1,2**64))<F(15,10**12)
    expbounds={26:195000000000,30:10000000000000,32:78900000000000}
    for x,v in expbounds.items():assert sum(F(x**k,math.factorial(k)) for k in range(81))>v
    # Bell polynomial by enumerating integer set-partition block counts.
    n=8;m=[F(math.factorial(j))*F(4,3)**j for j in range(11)];m[:4]=[F(1),F(1),F(1),F(2)]
    def partitions(k,j,ell=1):
        if ell>k:
            if k==j==0:yield ()
            return
        if k==0:
            if j==0:yield ()
            return
        for count in range(min(j,k//ell)+1):
            for rest in partitions(k-count*ell,j-count,ell+1):yield ((ell,count),)+rest
    def bell(k,j,v):
        ans=F(0)
        for part in partitions(k,j):
            val=F(math.factorial(k))
            for ell,count in part:val*=v[ell]**count/F(math.factorial(count)*math.factorial(ell)**count)
            ans+=val
        return ans
    mu=[F(1)];c=[1]
    for j in range(1,9):
        moment=math.prod(range(1,2*j,2));s=math.isqrt(moment);c.append(s+(s*s<moment))
        mu.append(F(math.prod(range(1,j,2))) if j%2==0 else F(4,5)*2**((j-1)//2)*math.factorial((j-1)//2))
    ones=[F(1)]*9
    sigma=[F(1)]+[sum(m[j]*bell(k,j,ones)*c[j] for j in range(1,k+1)) for k in range(1,9)]
    low=[[m[r]]+[sum(m[r+j]*bell(k,j,ones)*mu[j] for j in range(1,k+1)) for k in range(1,9)] for r in range(3)]
    up=[[m[r]]+[sum(m[r+j]*bell(k,j,sigma)*mu[j] for j in range(1,k+1)) for k in range(1,9)] for r in range(3)]
    def conv(v,w):return [sum(F(math.comb(k,j))*v[j]*w[k-j] for j in range(k+1)) for k in range(9)]
    a=conv(low[0],up[1]);b=conv(ones,conv(low[1],up[1]));c=conv(ones,conv(low[2],up[2]))
    profile=[2*(F(27,50)**3*(F(20,3)*a[k]+12*b[k]+4*c[k]+F(16,3)*up[0][k])+F(27,250)*up[0][k]) for k in range(9)]
    D=conv([F(3**j) for j in range(9)],profile)[8]
    assert D==F(41272525446939874982,31640625)
    error=F(16,7)*D/256**8;assert error<F(1,10**6)
    save('inequalities',dict(status='PASS',Horner_relative_bound=str(d0),
         exponential_eight_square_strict_bound='1/500000000000',
         long_double_summation_bound=str(4*gamma(401**3,F(1,2**64))),
         derivative_bound=str(D),angle_bound=str(error),independent_Bell='partition-count enumeration'))

if __name__=='__main__':
    {'inventory':inventory,'reconstruct':reconstruct,'interfaces':interfaces,'inequalities':inequalities}[sys.argv[1]]()
```

## Review artifact integrity

All review-output hashes, including the complete independent node tables and focused-check source hashes, are retained in `reviewer_b/artifact_hashes.json`.

SHA256 of this report up to, but excluding, this integrity sentence: `d866ba5642658fda6cd850615157af0ff53f76e48c0721b67706d0763e0e8b23`. The full final-file hash is retained separately in `reviewer_b/report.sha256` and returned to the coordinator.
