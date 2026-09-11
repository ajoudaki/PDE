# R1 independent scientific review B

**Overall verdict: ACCEPT for the precise scope of the frozen candidate.**

The frozen proof establishes a bounded, strongly continuous forced linear
equation in the stated clock/HS/readout space, its identification with the
actual finite-GF right data derivative on every separately fixed physical
horizon and the whole input circle, and a uniformly bounded population
homogeneous propagator. I found no surviving proof gap in those claims after
the complete dependency audit below. This is a scientific review, not formal
verification, a promotion decision, or approval to extend the claim to
nonlinear perturbed population dynamics.

## 1. Reviewer identity, isolation, and inputs

Reviewer: `/root/scientific_r1_b`, a fresh reviewer distinct from the four
authors listed in the manifest. I read the neutral assignment first. I did
not perform author startup; read the study README, history, other rounds,
other reviews, live author drafts, or author conversations; use Git; edit an
input; or delegate any part of the reading or assessment. I read the frozen
README and notation excerpts only as parts of the explicitly allowed
dependency file. I wrote only this assigned report and files under
`data/generated/trained_data_response/review_r1_b/`.

I used the required skills at
`/etc/codex/skills/solve-math-rigorously/SKILL.md` and
`/etc/codex/skills/investigate-conjectures/SKILL.md`, together with the latter's
`references/research-contract.md` and `references/adversarial-audit.md`.
No external specialized theorem was supplied from memory to fill a missing
dependency. No external source was needed: the invoked probability, action,
reference-flow, and rational-certificate arguments are contained in the
frozen inputs.

The hashes below matched before scientific review and again after the
complete reading and checks. All declared input line counts also matched.

| Input | Lines | SHA256 |
|---|---:|---|
| R1_MANIFEST.json | 90 | `17cfcd0231bd39079f8f5d4b33e1911201ed3c20d62cce8fe8b5a281cd3cd362` |
| R1_ASSIGNMENT.md | 49 | `5d49497988a172dabefd80e13c214564018495f28ea0b126e83aaac475eb89d6` |
| R1_PROOF.md | 2358 | `38b2c81be6e32f3d93f7fd85145487b33b2676b6d8698c504230189b9e625721` |
| R1_DEPENDENCIES.md | 3238 | `ca696bc4ed14ea337028eb1e6ef9c7f729ed2a0153bc210de8e16dea18f5ee79` |
| R1_CHECK_IDENTITIES.py | 197 | `b0bbbde5f1f024dbb46975b2092d3aa2a79cabd0375f4520c05489f934d3902f` |
| R1_REFERENCE_CERTIFICATE.py | 56 | `112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e` |

I additionally extracted the seven embedded dependency bodies, removing only
the wrapper blank lines, and recomputed their SHA256 values. Each matched
its manifest `excerpt_sha256`, with the declared original line count.
The standalone rational certificate equals the complete Python block in the
dependency file byte for byte. I did not inspect the live source paths or
claim that their present contents match their frozen versions. The manifest
author-source hashes are provenance declarations; the complete reviewed
candidate is the frozen proof itself.

Integrity evidence is retained in `input_consistency.json` and
`post_review_hashes.json` in the assigned scratch directory.

## 2. Complete reading coverage

All intervals here refer to one-based lines of the frozen files.

| File | Coverage |
|---|---|
| R1_ASSIGNMENT.md | 1–49, complete |
| R1_MANIFEST.json | 1–90, complete |
| R1_PROOF.md | 1–430; 431–930; 931–1460; 1461–1910; 1911–2358 |
| R1_DEPENDENCIES.md | 1–600; 601–1080; 1081–1490; 1491–1890; 1891–2300; 2301–2720; 2721–3100; 3101–3238 |
| R1_CHECK_IDENTITIES.py | 1–197, complete before execution |
| R1_REFERENCE_CERTIFICATE.py | 1–56, complete before execution; also the embedded copy at dependency lines 2677–2732 |

Two dependency reads were truncated by the output interface. I repaired
them by rereading lines 170–280 and 730–890 respectively; those repairs
cover the omitted material. Thus the intervals above represent complete
reading, not attempted coverage with unnoticed truncation. Both skill files
and the two applicable references were read in full.

The dependency content covered was: the complete frozen reading guide and
notation; finite gradients/energy/existence; the complete fixed-program,
conditioning, singular-query, common-action and strong-chain-rule material
included in the allowlist; the at-most-linear value extension, response
extension and sharp initialized-action estimate; B.1's full activation
transform and finite-flow bridge; the full-row/common-carrier passages;
and the complete supplied fitted-reference endpoint, activity, rational
certificate, active response-tail and actual finite-GF bridge proofs.

## 3. Contract assessed

The network has two width-n tanh hidden layers without biases, normalized
input `u=x/sqrt(2)`, independent stored Gaussian variances `(1,1/n,1/n²)`,
mobilities `(n,1,n)`, output `c^T H²/n`, and unhalved mean-square loss.
The base law is the equally weighted opposite-label orthogonal pair.
The perturbing law is an arbitrary fixed deterministic Borel probability
on the circle with labels in `[-Y,Y]`, with `Y>=1`.

The target is the right derivative at epsilon zero of the actual finite
exactly integrated GF along the mixture of these two laws. It is taken
before width tends to infinity. The limit is in probability, uniformly in
physical time on each fixed `[0,T]` and over the complete circle. It is not
a derivative of an assumed global population law-to-flow map.

The linear state includes the full two-coordinate first-row clock tangent,
a Hilbert–Schmidt middle increment, and the readout tangent. The initialized
middle action is a bounded action with its actual adjoint, not an HS kernel.
The identification of carriers is through fixed finite programs and
same-width norm errors. The all-time assertion concerns the homogeneous
population propagator; finite-width convergence remains on fixed horizons.

Coefficients come from the independently constructed autonomous reference,
not from future observations of a perturbed flow. No finite-dimensional
compression assertion is being smuggled into the use of function/operator
fields. Deterministic constants are independent of the perturbing law's
support size, positive atom weights, and Gram rank. Probabilities are for
each fixed law and are not claimed uniform over all laws.

## 4. Component findings and reconstruction

### A. Exact finite differentiation and normalization — PASS

Proof lines 18–45, 954–969, and 1854–1906 agree with the finite gradient
and metric identities at dependency lines 425–505. The middle velocity
uses `delta h^T/n`; the readout velocity has no extra `1/n`; the first-row
velocity contains the normalized input. For the two weight-one-half atoms,
the factor two from differentiating the unhalved square cancels the weight.
The finite raw energy metric is exactly row Frobenius divided by n,
ordinary middle Frobenius, and readout Euclidean divided by n in squared
norms.

For fixed width, compact data support bounds every parameter derivative
of the integrated loss on compact parameter sets. Its field is smooth
and affine in the mixture parameter. The energy inequality bounds all
mixture trajectories in one finite-dimensional ball over a fixed horizon.
Subtracting the integral equations, dividing by epsilon, and applying the
mean-value formula therefore proves the right derivative before any width
limit. The constants in this step may depend on width; the later proof
does not use them as width-uniform estimates.

Since `F'=cosh²=1/phi'` and `phi'>0`, the raw first variation is
`delta w_a=phi'(w_a)xi_a`. At the reference, the active first clock velocity
is `-r_a Q_a`. Differentiating this identity produces the displayed
homogeneous tangent without an unbounded own-gate multiplier. Equivalently,
the gate derivative in the raw differential cancels the derivative of
the conversion factor on the left. The direct law derivative retains the
passive ratio `phi'(w.u)/phi'(w_a)` and the signed reference subtraction.
Both orientations of the same matrix survive all these calculations.

The actual small finite Gaussian readout is present in the finite flow,
its derivative, cavity construction, and mesh comparison. Only separately
labeled auxiliary feature programs start from zero readout. The fixed-mesh
comparison justifying their limiting initialization does not reset the
actual finite network.

### B. Reference construction and endpoint dependencies — PASS

The common-action construction at dependency lines 624–945 and 2034–2109
constructs both actions on generated L² spaces by finite-program laws,
bounded completion, and the actual finite transpose pairing. The singular
case is handled by independent query regularization at a fixed program
followed by covariance-square-root continuity and zero-noise removal.
No inverse of a nearly singular empirical Gram is passed through a limit.
The at-most-linear value extension at 1169–1179 is adequate for the clock
map: it does not demand a bounded derivative in the frozen Gaussian root.

B.1 at 1230–1600 supplies the same-root transformed stability and the
continuous finite-GF width bridge on every fixed horizon. Its unhalved
sum-loss coefficients specialize to `kappa_a=1/2` here. Replacing increment
operator distance by HS distance is justified by the identical rank
difference inequality and `||K||op<=||K||HS`; dependency 2803–2813
explicitly performs that upgrade.

The feature equation at 2168–2226 is globally defined on finite feature
intervals. Its two-atom symmetry is a statement about population action
laws and does not impose false finite-network symmetry. The identities
`c_ss=JJ*c` and `b_s=||theta_s||raw²`, together with convexity of `||c||`,
give `b_s>=m>=1/10`. Thus the first level `b=1` occurs by feature time ten.
The physical clock has positive speed before that level and takes infinite
physical time to reach it. The raw path estimate follows by Cauchy–Schwarz
in feature time, yielding `Delta(t)<=sqrt(10)e(t)` and `e(t)<=exp(-t/5)`.
These are precisely the bounds consumed by the proposed propagator.

The active endpoint L4 input has a complete supplied proof at dependency
2745–3129. In particular the fresh-root pulse estimates isolate the named
source coefficient with width taken first, then forcing removed. The
bounded remainder and Gaussian source are placed on the same common
space by cross-program covariance and L² convergence. No independence of
that remainder from the Gaussian is needed for the L4 estimate. The new
cavity argument also gives higher moments, but this assessment did not
silently substitute it for a missing imported proof: the imported proof
is present and was checked.

### C. Actual finite cavity and Gaussian supremum estimate — PASS

Proof lines 971–1025 derive the needed deterministic bounds on `E_n` from
the true finite loss, not from a surrogate flow. The readout supremum bound
is crucial for the time/input L² Lipschitz bounds of the passive backward
field. The root enters the input modulus only through its RMS at this step.

Deleting initialized column i while continuing to train the entire learned
increment gives a cavity independent of that column conditional on all
remaining initialization. The event `E_n^i` is measurable with respect
to those remaining variables and contains `E_n` (1043–1054). Conditional
Gaussian estimates are made on `E_n^i`; the proof does not condition a
Gaussian column on the full event involving that column.

The two subtractions in (S21), at 1084–1093, are exact. The forward deletion
term is `a_i Htilde_i`, whose RMS is at most `||a_i||/sqrt(n)`. The reverse
deletion term is `e_i a_i^T deltatilde`, also divided by sqrt(n) in RMS.
Using the full A on the backward-field difference preserves this favorable
decomposition. The estimates also include residual differences and the
trained cavity K; they do not freeze either to its full-flow counterpart.
Substitution into (S23) gives the stated coarse `100 D0^4` coefficient
and then (S25).

The learned-transpose term in (S27) is bounded coordinatewise using its
integrated rank representation, bounded hidden features and two RMS
backward factors. Combining it with (S25)–(S26) gives
`N_i<=A_T Z_i^#+B_T` on `E_n`, with the displayed constants. In particular
an operator-norm-small deletion was never assumed.

Conditional on the cavity, `Z_i(t,u)` is an actual finite Gaussian process
with deterministic bounded covariance and increment metric. The union
bound, Gaussian tail integration and dyadic two-parameter grid argument
at 1198–1265 give a summable maximum bound and `C sqrt(p)` moments. No
independence among grid values is required. Finite-width sample continuity
justifies taking the full time/circle supremum. Conditioning and
`E_n subset E_n^i` then give the uniform moment estimate for the actual
adapted Q, rather than an independent replacement. The selected-column
and arbitrary-adapted-query obstructions do not defeat this argument,
because this reached flow satisfies the explicit deletion stability bound.

### D. Weighted source, uniform integrability, and Borel forcing — PASS

The exact identity `partial_X cosh² J=2 tanh J` at 1285–1297 yields a
linear bound in the clock, `cosh²w_a<=cosh²g_a+2|X_a|`. Together with
`|X_a|<=3T N_i`, this reduces all required products to Gaussian-root and
actual-query moments. Hölder is valid without independence of those
factors. The higher-moment tail estimate (S38) proves empirical square-tail
uniform integrability before width passage; RMS convergence is not used
as a substitute.

For the population all-time bound, lines 1349–1459 use auxiliary finite
feature equations on the fixed interval `[0,10]`. Their polynomial
deterministic bounds permit the same cavity calculation on the entire
interval. Fixed-list W2 convergence, bounded tests, monotone convergence,
and a countable dense parameter set yield one Lp envelope for canonical
query classes. Strong L² continuity extends its bound to each deterministic
parameter. Fubini then bounds the absolutely continuous active clocks.
This suffices for the weighted passive L² bound and does not assert
continuous Gaussian sample paths for arbitrary population queries.

The continuity argument at 1473–1519 uses weighted interpolation for the
Q difference and the exact clock-weight derivative for the other factors.
All resulting products are controlled by the proved envelopes. Hence the
forcing integrand is a continuous Hilbert-valued map on compact data and
feature parameter sets. Its Bochner integral against any finite signed
Borel measure exists. Total variation is its mass, with no half factor.
For the theorem's sharper row constant, `sum u_a²=1` combines the separate
weighted component bounds; the middle rank contributes at most sqrt(10)
and the readout field at most one. This gives the advertised bound (9).

The finite random modulus and clipping/quadrature estimates are justified
by the same empirical moment bounds. Partition quadrature approximates the
forcing in a norm controlled by its modulus, rather than pretending that
nonatomic probability laws are approximated in total variation. Exact cell
masses and total mass one prevent dependence on atom count or a smallest
weight.

### E. Bounded operators and uniform homogeneous propagation — PASS

Proof lines 343–463 type every tangent term correctly. The conversion from
clock to raw state is bounded and injective; no bounded inverse is used.
The coefficients involving readout are bounded multipliers. Remaining
action and rank terms are bounded on the stated L²/HS space. The generator
is strongly continuous on each vector by bounded-multiplier convergence,
HS continuity, and finite-rank continuity. The proof explicitly avoids
operator-norm continuity of general varying multiplication operators and
ambient Frechet differentiability of an L²-valued nonlinear field.

At 467–503, `E=S*D`, with `D=R*R` positive and injective, gives
`ker(ES)=ker S=ker E*`. Taking orthogonal complements in the two-dimensional
training-output space gives the required range compatibility. This matters:
positivity of ES alone would allow a nonzero nilpotent SE and unbounded
semigroup. The actual factorization excludes it, including the K=0 case.

The power-series computation (16) is valid for a singular Gram. Its finite
pseudoinverse is used only at the fixed endpoint, and finiteness does not
require a uniform coercivity estimate on D or full rank of K. The bound
`B_infty` correctly exposes endpoint conditioning without evaluating it.

For the nonautonomous coefficients, the finite-rank synthesis converges at
rate O(Delta). The extra evaluation term contains a gate difference times
the fixed endpoint Q. Hölder with that Q's L4 norm and
`|gate difference|<=min(1,4|w-w_infty|)` gives the displayed
O(sqrt(Delta)) bound. This is a finite-rank column estimate, not an assertion
of norm convergence of all multiplication operators. The exponential
reference decay makes both contributions and residual curvature integrable
in physical time. The constants in (21)–(22) follow by integrating
`e<=exp(-t/5)` and `sqrt(e)<=exp(-t/10)`.

Strong Picard construction, endpoint variation of constants, and scalar
Gronwall yield `sup_{s<=t}||U(t,s)||<=B_infty exp(B_infty J0)`. The forcing
representation and L1-in-time response bound then follow. This proves
uniform propagation of the actual population coefficients, not just the
frozen endpoint system. It does not claim convergence of U to the endpoint
projection.

### F. Fixed-program capture of the actual finite tangent — PASS

Proof lines 2015–2100 build only fixed finite programs after choosing source
cutoff, data quadrature and time mesh. Finite sums of learned/tangent ranks
reduce both action directions to initialized calls and scalar contractions.
The bounded readout clip is inactive. Coordinate instructions have at most
linear growth, including bounded gates times a tangent field, so A.1
applies. Same-index truncation (F16) transfers scalar feedback and products
even when the coordinate map is not globally Lipschitz.

The main mesh-removal step at 2102–2205 is present and sufficient. On the
population side, uniformly bounded generators converge strongly on fixed
vectors and hence uniformly on compact tangent families. This proves
uniform convergence of tangent Euler to its strong solution without
operator-norm multiplier convergence.

On the finite side, (F20) compares the actual finite linear equation with
the affine finite-mesh interpolant on the same carrier. The second and
third defects have ordinary O(h) bounds. For the first, the proof lists
the coefficient-error products in the lower gate, upper preactivation,
upper backward variation, reverse variation, rank updates and scalar
evaluation. Their testing fields are fixed-mesh nodes. The population
testing families along a refining mesh sequence are relatively compact in
L² because the tangent meshes converge and the reference actions and
multipliers act strongly continuously. Their square tails therefore vanish
uniformly.

At each fixed mesh, finite empirical cutoff moments converge. Width is
taken first; mesh refinement is then performed at a fixed multiplier
cutoff; the cutoff is removed last. Multiplying each node estimate by its
time-cell length and summing avoids an illicit uniform theorem for a
transcript growing with width. The resulting integrated defect tends to
zero, and the actual finite generator bound converts it to uniform
same-width state error by Gronwall. Finally the forcing cutoff and
quadrature errors are removed using the independently proved uniform
integrability estimates. This proves (F22) and identifies the intended
finite derivative rather than only an auxiliary linear equation.

Finite-rank Gram expansions identify HS norms and pairings. Same-width
errors and bounded actions extend their conclusions to the actual tangent.
The stated finite-list same-layer W2 topology includes second moments and
both action directions; it does not compare matrices on different carriers
in operator norm.

### G. Whole-circle observation and downstream boundary — PASS

The observation field (F23) represents the actual directional prediction
derivative and has a uniform L²/HS norm. Thus state capture yields scalar
capture at every fixed time/input. Its time modulus uses the deterministic
reference L² velocity bound plus the proved reference Q tails, while the
tangent has a tight Lipschitz-in-time norm bound from its linear equation.
No higher moment of a generic tangent is inserted here.

For circle uniformity, (F24) gives the strong angular derivatives of
reference hidden fields and Q. The only extra unbounded product in the
observation derivative is `(w.u')Q` times bounded gates. The weighted
source theorem supplies its L² envelope uniformly in physical time on a
fixed horizon. Strong curve differentiation, coordinate representatives
from Fubini, and dominated convergence justify the product calculation.
The Hilbert-valued H1 estimate then gives a one-half-Hölder circle modulus.
Together with the time modulus and a finite product net, this proves the
full supremum in (F10), rather than a finite-panel claim.

The endpoint projection obeys `P²=P`, `ran P=ker E` and `ker P=ran S`.
Under the raw conversion it is the orthogonal projection away from the
weighted raw training gradients. No conclusion about a nonzero unseen
change in every direction, its sign, or its risk benefit follows, and none
is claimed. The boundary at proof lines 239–253, 790–798, 1644–1652 and
2340–2356 is appropriate: products of two arbitrary L² variations are
still uncontrolled away from the reference. No finite-contamination
remainder, global perturbed population flow, CLT, raw-GD derivative, or
uniform-time finite-width theorem has been established here.

## 5. Commands and reproducible results

All commands ran with working directory `/home/amir/Codes/PDE`. Reading used
`cat`, `wc -l`, and `nl -ba ... | sed -n 'a,bp'` with the exact intervals
listed in Section 2. Initial integrity used `sha256sum` for the manifest
and a Python `hashlib.sha256`/`splitlines()` loop over its five inputs.
The same loop was repeated at completion and saved the final records.
The embedded-body audit used only `R1_MANIFEST.json`,
`R1_DEPENDENCIES.md` and the standalone certificate; it saved the results
as `input_consistency.json`.

The required execution commands were:

```text
python studies/trained_data_response/R1_CHECK_IDENTITIES.py --output data/generated/trained_data_response/review_r1_b/identities
python studies/trained_data_response/R1_REFERENCE_CERTIFICATE.py > data/generated/trained_data_response/review_r1_b/reference_certificate.txt
```

Both exited zero. The identity script reported PASS with tangent central
difference errors
`[1.0292819331017236e-06, 2.573205074969171e-07,
6.433012185025226e-08, 1.608263607613758e-08]`, consistent with its tested
second-order stencil. Its loss-metric error was
`7.900680110140001e-12`; the largest singular semigroup discrepancy was
`1.5265444420160054e-14`. Runtime: Python 3.10.12, NumPy 1.26.4,
SciPy 1.13.0. Full output is in `identities/results.json`.

The rational certificate printed
`[0.392108947877, 0.396376711612, 0.233120735618,
0.339792209687, 0.631761866359]` and all exact rational assertions passed.
I checked the exponential remainder, monotonic endpoint bounds,
outward rounding, two-sided Gaussian tail, and the lower/upper scale
substitutions underlying those assertions. Decimal printing is not the
certificate's inequality test.

I also wrote and ran:

```text
python data/generated/trained_data_response/review_r1_b/independent_checks.py
```

It exited zero and reported PASS. Exact rational checks cover the singular
pseudoinverse, endpoint projection, metric symmetry, compatible zero mode,
the incompatible nilpotent boundary, formal clock cancellation, and the
clock-envelope Laurent-polynomial identity. The nonzero rank-one metric
coefficient is exactly `3881/6000`. A fixed deterministic array check of the
two cavity identities gave forward error `1.2719202621569003e-16` and
reverse error `4.443059973708341e-17`. Results are in
`independent_results.json`; script SHA256 is
`8db3aea15a5922a4ddee02083e53b61fde8effa267d044bb1931ba4852bfc077`.

These were algebra/boundary checks only. I ran no optimizer trajectory,
training experiment, parameter sweep, or claim of formal verification.
Numerical identity agreement was not used to replace any of the analytic
arguments audited above.

## 6. Surviving gaps, required corrections, and optional suggestions

**Surviving mathematical gaps for the proposed scope: none identified.**
**Missing required proof/input: none identified.**
**Required corrections before scientific acceptance: none.**

Optional editorial suggestions, separate from the verdict:

1. At proof lines 208–212, replace “This operator is injective” with
   “D_infty is injective.” The derivation makes that referent clear, but
   naming it avoids accidentally reading the statement as injectivity of
   the potentially singular Gram K_infty.
2. At proof lines 1553–1556, the reference to “C.4.5.3's active call” could
   instead point directly to the supplied C.4.5.2, Section 5, or to frozen
   dependency lines 3163–3218. The actual supporting finite-GF argument is
   present in the allowlist, so this is a locator issue rather than a
   missing dependency.
3. The arbitrary `L1_loc` forcing assertion at proof lines 681–694 can
   explicitly say that the solution is strongly absolutely continuous and
   its differential equation holds almost everywhere. For the continuous
   measure forcing of the theorem, the solution is strongly C1. This is
   a clarification of the conventional solution interpretation.

The accepted result supplies the stated linear reference response and
propagation estimates. The nonlinear-continuation obligations remain
outside this verdict exactly as the candidate states them.
