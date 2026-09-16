# Independent scientific promotion review A2

Date: 2026-09-16. Reviewer: fresh isolated agent `/root/review_a2`.
Candidate: `general-p1-promotion-candidate-v2`, frozen root
`/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/promotion_20260916/frozen_v2`.
Manifest SHA256: `395ac0e660eadaca2bb9972a55e2f8dc8627ad60796a13db3458dd449b30660d`.

**Verdict: changes required; this frozen candidate is not acceptable for promotion.**
The explicit general-dimensional initialized object, its finite equations and
the principal implementation checks are sound within the stated finite scope.
Two required remedies remain: the comparison routine fails its promised null
correlation behavior for exactly constant vectors, and the packet does not
supply the prior dictionary definition needed to verify one exact compatibility
assertion. The latter is an input-completeness objection, not a counterexample
to the new coefficient formulas. Corrected inputs require two fresh complete
reviews under the supplied workflow.

## Scope, independence and complete reading

I received only the neutral assignment, manifest location/hash, allowed frozen
inputs, output ownership and resource allocation. I did not author or assemble
the candidate and was not its selector. I read no study README, historical
result, author validation report, selector verdict, earlier review, other
reviewer's findings, other study or live scientific source. The supervisor
acknowledged my own initial finding and requested completion; no outside
scientific conclusions were supplied. I delegated no part of this complete
review. I neither edited frozen/live source nor used Git. All retained writes are this report
and my own generated scratch under
`data/generated/first_order_dimension_mnist/review_a2_20260916/`.

The exact finite object reviewed has two bias-free tanh hidden layers, stored
Gaussian variances `(1,1/n,1/n²)`, input rows `U=x/sqrt(d)`, output `cᵀh2/n`,
unhalved weighted square loss and physical mobilities `(n,1,n)`. I kept closure
order `p=1`, population count `P`, width `n`, dimension `d` and input count `m`
separate. No MNIST/PCA conclusion, trained-network convergence for general d,
fixed-order approximation guarantee, speed ratio, cost-to-accuracy guarantee or
general-d higher-order hierarchy is within the review's positive conclusions.

Complete substantive reading covered:

| Frozen input | Exact coverage |
|---|---:|
| `docs/observable_p1.md` | All 326 lines |
| `docs/NOTATION.md` | All 98 lines |
| `dependencies/global_nonlinear_source_units.md` | All 393 lines, including every proof body |
| `code/GENERAL_P1.md` | All 212 lines, both Python examples and reproduction recipe |
| `code/pde/observable_p1_initialization.py` | All 181 lines |
| `code/pde/observable_torch_p1.py` | All 403 lines |
| `code/pde/finite_torch.py` | All 153 lines |
| `code/pde/closure_comparison.py` | All 125 lines |
| `code/tests/test_general_p1.py` | All 271 lines |
| `code/scripts/example_general_p1.py` | All 131 lines |
| `code/scripts/analyze_general_p1.py` | All 46 lines |
| `code/pde/finite_network.py` | All 363 lines |
| `code/pde/gaussian_moments.py` | All 114 lines |
| `code/pde/__init__.py` | All 26 lines |
| `docs/README.md` | All 742 lines |
| `code/README.md` | All 1117 lines |
| `dependencies/original_docs_README.md` | Complete 738-line/59369-byte content, verified byte-for-byte equal to the already fully read candidate-guide prefix |
| `dependencies/original_code_README.md` | Complete 1113-line/62761-byte content, verified byte-for-byte equal to the already fully read candidate-guide prefix |

The initial combined read truncated portions of NOTATION and the source
dependency units. I repaired it by rereading complete NOTATION and dependency
lines 1–200 and 201–393 in separate bounded outputs. The larger guides were read
in consecutive complete ranges. Their only changes from the original guides
are the four appended lines each; both full-prefix equality and complete diffs
were checked. Original guide content was not treated as an author verdict or
as a request to reproduce unrelated book results.

I read the neutral assignment and complete manifest, frozen AGENTS and complete
RESEARCH_WORKFLOW including Part 2, the full `solve-math-rigorously` skill,
the frozen `investigate-conjectures` skill, and its complete adversarial-audit
and decisive-experiments references. The actual system solve-math skill hash
equals its frozen counterpart. I applied the skill's mathematical proof and
hypothesis checks and the research audit's bounded-computation distinctions.

Unread complement: `PROMOTION_PLACEMENT.md` and `PROMOTION_assemble.py` were
metadata-hashed without inspecting their contents, preserving isolation from
placement/assembly conclusions. Skill agent YAML and the nonapplicable
research-contract/evidence-ledger/proof-search-orchestration references were
likewise only hashed. I did not read the full older global-nonlinear chapter,
older dictionary/initializer/compiler implementations, other chapters described
by the guides, or their historical generated outputs. Only the complete named
source units were supplied for older theory. This is the source of R2 below;
I did not silently retrieve the missing older definition.

## Required corrections

### R1: constant predictions receive a spurious defined correlation

Location: `code/pde/closure_comparison.py`, `_metrics`, especially the centered
vectors and denominator at lines 36–41; guide constant-vector semantics.

The guide says either constant vector gives null correlation. The code detects
this only by asking whether the product of centered norms is zero. Floating
reduction of an exactly constant vector need not recover its constant exactly.
For three copies of `0.1`, NumPy 1.26.4 gives mean
`0.10000000000000002`; all three centered values are the same small nonzero
number. Their artificial correlation is then approximately one.

Exact reproducer, using only frozen code:

```python
import numpy as np
from pde.closure_comparison import prediction_metrics
a = np.full(3, 0.1)
result = prediction_metrics(a, a, ids=np.arange(3), reference_ids=np.arange(3))
assert np.ptp(a) == 0
print(result['overall']['correlation'])
# Observed: 1.0000000000000002. Required by the API: None.
```

It also fails for the within-class statistics: constant predictions with two
three-element classes produce the same spurious correlation in both classes.
This is not an insignificant numerical perturbation of a well-defined
correlation: the statistic is undefined, and reporting near-perfect correlation
is materially misleading. The maintained test uses exactly representable
integer constants and misses the case. CPU and CUDA review invocations both
reproduce the defect because the metric itself is NumPy code.

Required remedy: detect exactly constant candidate or reference arrays from the
original entries before centering and return `None`. Add meaningful regression
cases with repeated non-binary-exact constants, including within-class slices,
and either vector constant with the other nonconstant. Preserve the existing
zero-reference, absent-class and empty-subset behavior. A separate treatment of
near-constant vectors may be documented if desired; it is not a substitute for
fixing exact constants.

### R2: the exact older-dictionary identification lacks its definition

Location: `docs/observable_p1.md:64`: the text asserts the d=2 order is exactly
that of `build_dictionary(1)` and that codes 0 and 1 add no features. The packet
contains neither `build_dictionary` nor the relevant decoding/order definition.
The H3.N1/N2 dependency excerpt says to use the exact coding/order of earlier
part B but does not supply that part. The full guides give feature counts and
general descriptions; they do not determine literal feature order or decode
these two codes. The current deterministic tests reconstruct the new feature
ordering independently of the older dictionary, so cannot verify this claim.

The new feature list, ridge, raw Gram and contraction identities can be checked
without this old API and passed my audit. What remains unverified is the
specific equality to that named older construction. Under the complete-input
review requirement, supply the minimal complete frozen dictionary/decoder
definition and dependencies needed to verify this statement, or remove/narrow
the exact compatibility sentence so the explicit new target stands on its own.
This is a narrow required completeness remedy, not a request to import a whole
older convergence proof or to conduct a new research campaign.

## Mathematical audit and component verdicts

**Gaussian initialization and response: pass for the explicitly defined target.**
For each coordinate, forward covariance is `v`; bounded odd upper activation
has second moment `tau`, and its expected derivative is `alpha=1-tau`.
The supplied complete finite source/response proof therefore gives reverse
coordinate `sqrt(tau) Z + alpha tanh(G)`, jointly with G. Its innovation variance
is the full second moment tau, not a residual variance after subtracting the
response. Different coordinate pairs are independent in this finite law.
All queried coordinate maps are finite compositions of tanh and linear maps
with bounded first derivatives and Gaussian roots with all finite moments, so
the proof's fixed finite smooth-program hypotheses apply. No growing query
program or time-evolving network theorem is imported.

For a retained F and upper B, the forward-after-reverse contraction is the sum
of the Gaussian regression/Stein term and the reverse-source response term.
For `F=k_i`, `B=H_i` these are `alpha beta` and `tau gamma`. The response cannot
be discarded. For `F=h_i` only `alpha v` remains. Symmetry and independence
remove constant and cross-coordinate entries. Thus the displayed raw C and
block Grams follow, including the within-population G/R coupling. Integration
by parts is justified by bounded functions/derivatives and Gaussian tails;
the finite-source dependency also supplies its singular-covariance argument.

**Ridge and normalization: pass.** The ridge is exactly `1/4096`. Cauchy–Schwarz
gives `beta²<=vs`, hence `b²>=eta+s eta/(v+eta)>0`, with the other denominators
positive. Direct block multiplication of `L2^-1 C L1^-T` gives the two displayed
bands, including the residual `alpha beta eta/(v+eta)` in the k band. The right
transpose is essential. The dense-Cholesky maintained tests check this at
d=1,2,7,17, including both antithetic representations. They use the same scalar
coefficients, so I additionally evaluated independent 200-node Gauss–Hermite
integrals: all six basic constants differed by at most
`4.9960036108132044e-15`. This is strong numerical corroboration at the tested
rule, not a certified Gaussian-integral error bound.

**Numerical initialization: pass with the stated limitations.** Independent
SeedSequence child streams preserve the full lower `(G,R)` tuple and separate
upper population. Antithetic pairs are simultaneous sign changes of whole
marks; P/2 independent bases are not presented as P independent draws. The
normalization uses population-target block coefficients, not an empirical-Gram
projection. Global NumPy RNG ownership, explicit seeds and representation
metadata were audited. Quadrature refinement, scalar tails, population sampling,
closure order and finite width remain separate. The finite d=2 Halton
initializer is not claimed to be bitwise equivalent to these scalar coefficients.
Its detailed older implementation was not supplied, as recorded under R2.

**Finite vector field, arbitrary supplied dimensions and metric: pass.**
With `a=B1ᵀ diag(pi1) h1` and
`upsilon=B2ᵀ diag(pi2)[c(1-h2²)]`, the w, c and M derivatives of f are
`pi1_i (1-h1_i²) q_i u`, `pi2_j h2_j` and `upsilon aᵀ` respectively. Multiplying
by `2 mu r` verifies all signs, factors, matrix shapes and weight locations.
The code uses the full dense M and the actual M transpose. Both optimized
associations are ordinary matrix reassociations of the same contractions.
Input blocks sum a single full-batch velocity before any state update.

The loss derivative equals the stated negative weighted velocity squares and
negative Frobenius square. Zero population weights require no division:
the corresponding ordinary gradients are zero, and the direct weighted identity
still holds. I checked this with unequal P1=5, P2=7, K1=4, K2=6, d=3, dense
nonzero w/c/M, zero entries in both population weights, nonuniform data weights,
and zero/nonunit/duplicate inputs. Independent autograd weighted-gradient error
was at most `3.469446951953614e-18` on CPU and
`6.938893903907228e-18` on CUDA; energy error was
`4.336808689942018e-19` on both. This specifically covers zero population
weights beyond the maintained positive-weight autograd test.

**Simultaneous Heun and folding: pass.** Both stages update w/c/M from a common
stage state. Odd initial/current w and c, zero constant row/column of M and
odd nonconstant marks form the sign-invariant class. Lower activations and
upper activations are odd; gates are even; the necessary feature pairings are
even. Constant feature contractions vanish, so constant matrix directions
remain zero without requiring symmetric labels or inputs. The nontrivial
maintained folding check perturbs dense M, w and nonzero c before four steps,
compares full and folded velocities/trajectories, and checks the signed pair
law and all observations. I verified the proof does not impose diagonal or
low-rank moving M. Euler/Heun and affine stage combinations preserve the class
in real arithmetic; floating reduction discrepancies remain admitted.

**Full network comparator: pass.** I read the complete actual NumPy initializer
and its draw order. It draws first weights unscaled, middle entries divided
by sqrt(n), stored readout divided by n, and retains the nonzero readout.
The tensor comparator calls that initializer rather than replacing it by a
zero readout or independently chosen feature law. Full forward/backward
derivatives give `w_dot=-2 sum mu r delta1 uᵀ`,
`c_dot=-2 sum mu r h2` and
`M_dot=-(2/n) sum mu r delta2 h1ᵀ`, exactly as implemented after mobilities.
The maintained NumPy oracle has independent layerwise contraction code and
better saturation-range derivatives; the tests stay in a regime where this
comparison is meaningful. I additionally tested weighted gradients at n=1
and n=11 with dense supplied states and zero data weights. Maximum mismatch
was `2.220446049250313e-16` on CPU and `2.7755575615628914e-17` on CUDA.
No identification of finite initial seeds with the closure marks is inferred.

**Ownership, domains, cached weights and observations: pass within contract.**
Construction and prepared-data copies prevent caller input aliasing. Ordinary
tensor mutations and replacement invalidate version/identity checks; deliberate
`.data`/NumPy-view bypass is explicitly outside the supported contract.
I tested returned-observation mutation, zero-step return independence, constructor
input mutation and cache mutation rejection. The maintained suite covers invalid
sizes, probabilities, steps and nonfinite data/state, plus frozen/data mutations.
Initial upper fields use g and D on the same marks. Cross Grams order initial
rows and current columns. Folded output returns both signs and halves base
weights, restoring the full signed joint observation law; RMS/Grams remain the
corresponding weighted statistics. Zero input gives the expected zero hidden
activations and prediction without division by an input norm.

**Restart, float32, CUDA and storage: pass at tested resolutions.** The complete
NPZ state owns frozen/current arrays, data, representation and arithmetic policy,
uses no pickle and requires no initializer/history on loading. Maintained tests
give exact float64 continuation on both devices. My additional folded float32
three-step/save/load/three-step continuation is bitwise identical to six direct
steps on each device. The maintained 12-step float32-versus-float64 check and
saturation finiteness check pass. These are finite checks, not bounds for all
states or devices; saturation cancellation, finite precision and intermediate
overflow remain honestly disclosed.

I independently recounted frozen arrays plus cached weighted B1 transpose and
B2 transpose, and current w/c/M. The count is
`P1*d+P2+K1*K2 + 2*P1*K1+P1*d+2*P2*K2+P1+P2+K1*K2`.
It yields the stated unfolded and folded specializations. My generic test
gives 1768 retained bytes in float64; folded P=20,d=3 gives 1224 in float32.
Both equal `retained_bytes`. Producer values are closure 2016 and network 5120
bytes. These are entry counts, not allocator peaks; data, stage copies, panel
output and histories are separately accounted for. Input blocking and a bounded
number of Heun states do not accumulate elapsed-time history. Precontractions
cost O(Pd²); the direct p=1 RHS costs O(m(Pd+d²)). No uniform joint d,n advantage
is asserted.

**Comparison tools: partial failure R1.** I checked unweighted RMS, relative
error, signs, raw Gram normalization, absent classes, IDs and all seed pairs.
Duplicate/misaligned Gram IDs and a large signed/unsigned integer mismatch are
rejected in the tested NumPy environment. Training-loss matching receives only
times/losses/target, chooses the nearest saved loss with earliest-time ties,
handles nonmonotone losses, returns nearest attained loss brackets and rejects
extrapolation. This does not establish equal maps or a clock change. Those
parts passed; exact constant-vector correlation did not.

**Producer/analyzer and new guides: pass except R1/R2.** I read both scripts
completely before running them. The producer validates identity semantics,
constructs both systems from scratch, preserves actual network initialization,
saves full arrays and a closure restart, records source/output hashes and
explicit phase scopes, and writes failure status on exceptions. Its synthetic
operation is bounded by a 120-second alarm and CUDA allocator fraction 0.15.
The work timer excludes imports/setup/final record writes as stated, and process
peaks retain both systems. The analyzer separately reconstructs predictions and
Grams with NumPy, verifies output hashes and diagnostic records, and checks
every repeat array exactly. It does not independently prove integration accuracy
or infer any closure approximation. Both documented Python fragments execute.
Ordinary `import pde` was separately checked to leave Torch unimported.

## Executed commands, controls and actual outcomes

All scientific commands used the frozen root as working directory and absolute
`/home/amir/miniconda3/bin/python`. The common environment was:

```sh
export PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
export CUBLAS_WORKSPACE_CONFIG=:4096:8
```

Let `S=/home/amir/Codes/PDE/data/generated/first_order_dimension_mnist/review_a2_20260916`
and `PY=/home/amir/miniconda3/bin/python`. The executed main commands were:

```sh
PDE_TEST_DEVICE=cpu "$PY" -B code/tests/test_general_p1.py > "$S/tests_cpu.log" 2>&1
PDE_TEST_DEVICE=cuda:0 "$PY" -B code/tests/test_general_p1.py > "$S/tests_cuda.log" 2>&1
"$PY" -B code/scripts/example_general_p1.py --output "$S/cpu_a" --device cpu
"$PY" -B code/scripts/example_general_p1.py --output "$S/cpu_b" --device cpu
"$PY" -B code/scripts/analyze_general_p1.py --run "$S/cpu_a" --repeat "$S/cpu_b" --output "$S/analysis_cpu.json"
"$PY" -B code/scripts/example_general_p1.py --output "$S/cuda_a" --device cuda:0
"$PY" -B code/scripts/example_general_p1.py --output "$S/cuda_b" --device cuda:0
"$PY" -B code/scripts/analyze_general_p1.py --run "$S/cuda_a" --repeat "$S/cuda_b" --output "$S/analysis_cuda.json"
A2_DEVICE=cpu TMPDIR="$S" "$PY" -B "$S/independent_checks.py" > "$S/independent_cpu.log" 2>&1
A2_DEVICE=cuda:0 TMPDIR="$S" "$PY" -B "$S/independent_checks.py" > "$S/independent_cuda.log" 2>&1
```

All ten exited zero. The independent script deliberately records and asserts
the existence of R1; its successful execution is not an overall acceptance.
Its fixed scope, sizes, seeds, tolerances and stopping condition are retained
in its header. No exploratory training grid or data search was conducted.
CUDA execution used the supervisor-allocated device 0 with approved tool
escalation, not CPU-only inference about CUDA support. Tests used one worker
and one numerical thread. Temporary-file deviation: the two maintained test invocations initially used
the operating system default temporary directory for their short-lived NPZ
archives because TMPDIR was not overridden. Those TemporaryDirectory contexts
removed their files on exit. No unrelated temporary input was read, and no
artifact survives outside the assigned paths. The later independent checks set
TMPDIR explicitly to my study-owned scratch. This is a scratch-location deviation,
not contamination by another scientific input.

The fixed maintained test suite ran 12 tests in
0.332 seconds CPU and 0.924 seconds CUDA, within its 300/600-second allowances.
The environment emitted a Torch TF32-API deprecation warning, not a failed
test. Python was 3.10.14, NumPy 1.26.4, Torch 2.9.0+cu130, GPU an NVIDIA
GeForce RTX 3090. TF32 was disabled and deterministic algorithms enabled.

| Run | Integration seconds | Validation work seconds | Peak process RSS bytes | Peak CUDA allocated / reserved bytes |
|---|---:|---:|---:|---:|
| cpu_a | 0.0242333561 | 0.0488095246 | 517472256 | n/a |
| cpu_b | 0.0272011496 | 0.0745272487 | 517500928 | n/a |
| cuda_a | 0.2281215303 | 0.3910725601 | 920231936 | 33610752 / 35651584 |
| cuda_b | 0.2317062877 | 0.3893366866 | 920518656 | 33610752 / 35651584 |

These tiny finite-operation timings are not benchmarks or a speed comparison.
Both analyzers report exact repeat arrays. Independent NumPy reconstruction
maximum absolute error is `2.220446049250313e-16` CPU and
`1.1102230246251565e-16` CUDA. The synthetic closure/network prediction RMS
difference is about 0.0186128; relative RMS is about 1.06737 and Gram relative
differences about 0.490975 and 1.42708. These are descriptive finite comparison
outputs, not evidence for a small approximation error. No claim in the candidate
requires their being small, and I do not use their high prediction correlation
as proof of agreement of learned maps.

Evidence is retained in the named fresh scratch: maintained logs, complete
independent-check source/logs, all four complete producer outputs, and both
analyzer JSON files. Every archived array in this review was newly generated.

## Optional improvements and limits

After R1 is fixed, clipping a nonconstant correlation's last-bit result to the
mathematical interval [-1,1] would be reasonable defensive presentation, provided
it does not conceal nonfinite arithmetic. It is optional and does not fix R1.
The maintained suite could also retain my zero-population-weight energy and
float32 restart cases; they currently pass and are coverage improvements.
Removing duplicated prose about the unused generic compiler would improve
readability without changing the scientific content.

No other correctness counterexample was found within the supplied explicit
finite target. That does not certify arbitrary numerical ranges, CUDA devices,
library versions, unbounded horizons, Gaussian coefficient quadrature errors,
general-d trained-network convergence, higher-order closure convergence or
MNIST/PCA behavior. The older broad guide statements were read as context and
not re-proved or promoted anew. R2 is the only identified missing dependency
for a specific new assertion. This report completes the assigned review and
does not constitute user promotion approval.

## Input integrity

I verified the manifest's supplied SHA256 before substantive checks and again
after execution. All 32 frozen file hashes matched before and after. The table
below records every frozen hash; `H` means metadata hashing only, `R` means
complete substantive reading, and `R*` means full content covered by verified
byte-identical copy/prefix as explained above. Hashing unread placement or
assembly files was an integrity operation and did not expose their contents.

| Frozen path | Coverage | SHA256 |
|---|---|---|
| `PROMOTION_PLACEMENT.md` | H | `b3ca29eb03eaacf95b7b06410bf50bdb8141d2ca343881ce33fc9d34b3a26db6` |
| `PROMOTION_REVIEW_ASSIGNMENT.md` | R* | `2ca132680a8965644cfc4f9e44b4a0380821588de2485736979b945c5a773ede` |
| `PROMOTION_assemble.py` | H | `9afd22e391e517a741a12b3c1752732acc8c8efe0c3d0e692b9f5241bca16bf2` |
| `code/GENERAL_P1.md` | R | `982cace29181a9e049fe9e9e88a735c8631015d36614c13d8c81b9074f90f114` |
| `code/README.md` | R | `ff5a89effef3fc1bc86a2bcc699453731c50bebffd9fd5ff0844f690717dc237` |
| `code/pde/__init__.py` | R | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `code/pde/closure_comparison.py` | R | `750203dc5ceb7a72dc2abf160fa97c3e38311c0cac38bc1463b2dfaa1c75809b` |
| `code/pde/finite_network.py` | R | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `code/pde/finite_torch.py` | R | `76d87cb0ddd25e974acf85935dc8fbfc8bc4a9eb829d5e60782e64d20e4f55a8` |
| `code/pde/gaussian_moments.py` | R | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `code/pde/observable_p1_initialization.py` | R | `65ded7e9faa352612fb833735d3075cbe41c0b24a535bf742d1fc86849aded6d` |
| `code/pde/observable_torch_p1.py` | R | `d67f0d832d265e75925f0020c42ab4d8e1dd3387e7e485412eff946ae5d20f1f` |
| `code/scripts/analyze_general_p1.py` | R | `e09242bd75dcabd1f6bdc759fd8b0a6c669db158ff93285c659ef63856ceca8b` |
| `code/scripts/example_general_p1.py` | R | `c288ef22b9cb5f167cff37931d35dc9c5b149ca1bb9d1805fcb0145afa2dae41` |
| `code/tests/test_general_p1.py` | R | `4ceeab90632505a694783a44a254acdcb57214ce9e9eaffba65b485b6a0e298a` |
| `dependencies/global_nonlinear_source_units.md` | R | `4363b0710431373d92d6c4957eba139b752fcc74ddf4979b3a756487db283766` |
| `dependencies/original_code_README.md` | R* | `b25c0ad7be0a770881c7ae75446a1718d4217ceec5576bdc14864790daffc91e` |
| `dependencies/original_docs_README.md` | R* | `0a27a6bc697c65b290bbe6d16c9992575c6221115b992efaef1a78ad983ae13e` |
| `docs/NOTATION.md` | R | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/README.md` | R | `60816cf89cf93abc9d752b7d56a66b3302cd9ca0caff4b247991647dfb49b3ad` |
| `docs/observable_p1.md` | R | `290f97011bf4cd04be8962030cec8c3d58f5ad9667bfe67ba47ad9de17c3c93e` |
| `instructions/AGENTS.md` | R | `7b3e384e1a627903835fa91c7396da7e399add57987334e07fc0168682b09747` |
| `instructions/RESEARCH_WORKFLOW.md` | R | `0906284c80dced0b2ee1beaf7c5f160a12d17f41afd060a536eeac0903406f85` |
| `instructions/investigate-conjectures/SKILL.md` | R | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `instructions/investigate-conjectures/agents/openai.yaml` | H | `ba8e39aba0463d706c4fa49375b90d0b9ce4d0ce436875e6d35ca61bcf387d02` |
| `instructions/investigate-conjectures/references/adversarial-audit.md` | R | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
| `instructions/investigate-conjectures/references/decisive-experiments.md` | R | `6abdb4d2d850ec7a40a34dd0461af70952ef097ee3629b7c62a3449d221768e9` |
| `instructions/investigate-conjectures/references/evidence-ledger.md` | H | `9e7573b37cbd954432236bdcb13f6b83b6325e0ff2653a198939842bc81c3a2e` |
| `instructions/investigate-conjectures/references/proof-search-orchestration.md` | H | `6f288341eb90f9618ab9fa6fc8c37225f41230de6a40285761c17cc257edecdd` |
| `instructions/investigate-conjectures/references/research-contract.md` | H | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| `instructions/solve-math-rigorously/SKILL.md` | R* | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `instructions/solve-math-rigorously/agents/openai.yaml` | H | `13e1679d378e917628b9f7d58c687e78e0442df8b6ad9089a4720a87f6bb3d1c` |
