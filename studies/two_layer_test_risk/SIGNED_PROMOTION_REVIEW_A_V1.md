# Fresh complete scientific promotion review A — signed tanh risk C.4, frozen v1

**Verdict: ACCEPT the scientific addition exactly as frozen. No required correction was identified.** This verdict covers the stated fixed-model theorem and its computer-assisted certificate. It is neither the separate integration review nor user approval to promote. The nonblocking editorial observation below does not authorize a post-freeze source edit.

Reviewer: `/root/signed_promotion_a`, a newly created isolated reviewer, distinct from every author/assembler and selector named in the manifest. Date: 2026-09-10. Frozen manifest SHA256: `bef8b4af500bfef3e8a5f4234e239ac68e30c5891841280b0f38be55bfb2ffb3`.

## Isolation, authority and complete reading coverage

I started from `SIGNED_PROMOTION_ASSIGNMENT.md` and the supplied frozen manifest. I did not perform author startup, read the live study README, study history, selection reports, earlier internal/scientific reports, another reviewer's findings, or Git history. The author/assembler and selector names were read only from the neutral manifest. I used no previous verdict as a premise and communicated no findings with another scientific reviewer. I sent progress to the root coordinator. I changed no candidate proof, implementation or frozen input, and made no Git/index operation. My only created files are this report and scratch beneath `data/generated/two_layer_test_risk/signed_promotion_v1/reviewer_a/`.

Required skills read completely: `/etc/codex/skills/solve-math-rigorously/SKILL.md`, `/etc/codex/skills/investigate-conjectures/SKILL.md`, and its `references/adversarial-audit.md` and `references/decisive-experiments.md`. No external theorem is needed to complete the candidate's proof. I did not use external literature as a substitute for an operative proof body. The unchanged guides' contextual literature descriptions were read as orientation, not imported theorem hypotheses.

The packet prefix below is `data/generated/two_layer_test_risk/signed_promotion_v1/packet/`. I read every line of the following:

| Input | Complete line coverage |
|---|---:|
| Neutral assignment / packet assignment | 1–68 |
| `candidate.md` | 1–1736, including every statement, derivation, error table, arithmetic contract and final rational endpoint |
| `dependencies.md` | 1–1775: complete Section 2, Section 3.1–3.4, A.1–A.4, C.1, C.2, C.3 and the weighted-loss correction |
| `NOTATION.md` | 1–98 |
| Tool `README.md` | 1–169 |
| `certificate.py` | 1–429 |
| `certificate_kernel.cpp` | 1–236 |
| `angle_error_bound.py` | 1–88 |
| `check_driver.py` | 1–140 |
| `check_kernel.py` | 1–161 |
| `original_numerical_source.py` | 1–382 |
| `code_README_before.md` / `code_README_after.md` | 1–591 / 1–621 |
| `docs_README_before.md` / `docs_README_after.md` | 1–265 / 1–271 |

I also read the complete frozen edition's `code/tools/check_library.py`; its structural role is distinct from scientific proof checking. Before/after guide correspondence was computed exactly, then both complete after guides were read as well. The initial oversized manifest display was truncated: I repaired this by loading the complete JSON, inspecting its structural fields, and checking every listed packet, edition and evidence hash. A later combined display clipped a short part of `docs_README_after.md`; lines 190–240 were reread to repair it. Candidate and dependency reads were partitioned into bounded consecutive ranges without omissions.

All **16 packet files, 18 edition files and 1160 evidence files** match the manifest's hashes. The two full-run metadata files and constants were read completely. Every saved node's input, stdout, stderr, audit, enclosure, and corresponding final-result row was loaded and checked, including all primitive arrays, input echoes and rational endpoints. This covers both runs, not just a sample of nodes. Hashes identify copied inputs; they are not treated as a proof of their content. There is no missing operative input.

Key scientific input hashes:

- Candidate: `dcb03d4c95a34c2ea3f616cc98ad30ea212abdc8e9dfe64624a666f4eee90bbc`.
- Dependencies: `00ff7d1ba44f98733a1ef57e0cd0d0c595f8016f112b1a03a7858efa067c4794`.
- Maintained driver: `36dd0b21dea51647dcbb9aef7c958d8f2ddadc397529e629ada5b122af0d2810`.
- Original executed driver: `a2e49e1c635b347e6542372bbdb4fb8ad3438e6c923e4292dc79964a000d48e1`.
- Kernel: `9d7bbcd743e465ae0e4caacd0f1e670d78283e1388a2fe48bda6193ef0e66ad9`.
- Angular helper: `cc3d750d096212016534056d35d221d6e7840a4a9f192379d283c093b0f94149`.
- Both full-run `result.json` files: `89815a7b16fb69f51683834049b370256fd32aba26528630f4c4f6b427fe406d`.

## Contract and proof audit

The accepted object is exactly the two-hidden-layer, scalar-readout, bias-free tanh network with stored variances `(1,1/n,1/n^2)`, raw mobilities `(n,1,n)`, `x(alpha)=sqrt(2)(cos(alpha),sin(alpha))`, training angles `0,pi/5,-pi/5`, mean square loss, and teacher `cos(3 alpha)` on the uniform circle. The baseline freezes both initialized hidden layers and trains its stored readout. The comparison is `R(g_tau(t))-R(f_t)` at equal training loss. No selection over data, targets or resolution is part of the stated theorem.

### Normalization, model identification and reuse — PASS

Direct differentiation of the stored finite model gives the C4.17 equations: the first and readout mobilities remove the raw `1/n` gradient factor, while the connector update retains the normalized rank-one operator. Mean loss supplies `2/3`, and `G=x^T x'/2` is the actual correlated rank-two Gram. Thus the initialized forcing is `p=y/3`, not `y`, and no hidden variance factor belongs in a trained rank-one increment. The output is divided by `n`, the lower input by `sqrt(2)`, and there is no extra hidden `1/sqrt(n)`.

C.1 applies with bounded smooth tanh, three fixed inputs, unit multipliers and the vanishing readout perturbation. I checked the supplied full existence/capture argument rather than just its statement: common generated action spaces and adjunction; bounded operator/RMS balls; fixed-program Gaussian induction; C.2's entrywise `Delta*omega_b` source pulse and row-sum bounds; simultaneous subGaussian field/response induction; one-reference tail localization with coefficient linear in the cutoff; the ordered `n,Delta,R` limits; strong continuity of the bounded-multiplier product; and uniqueness against an arbitrary competing strong solution. These steps do not presume an ambient smooth map on L2 or higher-moment bounds for all trained finite coordinates. The fixed-program versus growing-mesh distinction remains explicit.

The conditional transpose law includes its response mean and innovation covariance equal to the **full second moment** `E[F1 F2]`. Multiplying the two transpose answers produces both terms of Lambda. C4.28–31 correctly retain formal passive slots even at coincidence or antipodes. Integration by parts in a Gaussian root factor handles singular laws; the supplied regularization and bounded-action argument identifies the source response with the actual reused matrix at rank loss. No passive inverse is taken. The second forward use is retained by adjunction in `C_a(F)`. Replacing either orientation by an independent fresh action would remove a required term; the code does not do so.

C.3's finite-difference ridge argument applies because all three directions are pairwise nonparallel. It proves `Q>0` even though `G` has rank two. Upper Gaussian full support then proves `K>0`. The weighted correction applies because all labels and all weights are nonzero. The `V>0` argument permits a zero set of S without dividing by it; conditional innovation gives `D>0`. In particular the strict clock speed is not incorrectly attributed to a positive eigenvalue of G.

### Actual-flow fourth-order remainder — PASS

The proof uses only fourth moments of fixed initialized directions. Conditional transpose projection gives bounded response mean plus a Gaussian for P. The next forward projection uses only the positive training Q,V and gives a finite Gaussian-plus-bounded representation with uniformly bounded coefficients. Therefore T, A and `R^hid` have the needed uniform fourth moments. The fresh forward innovation is not asserted independent of the passive `Y_x`.

Starting from zero population readout, the strong readout integral has an L-infinity representative of size O(t); consequently the two backward fields are O_L2(t), lower displacement and connector change are O(t^2), and upper hidden displacement is O_L2(t^2). The rescaled readout/backward estimates in C4.18 are O_L2(t). For the first-layer gate, boundedness and Lipschitz continuity convert the O_L2(t^2) displacement to an O_L4(t) gate difference; Holder against fixed P in L4 is exactly sufficient. This establishes the O(t^3) errors in C4.19 without incorrectly demanding a uniform trained L4 bound.

The fixed-direction Taylor inequality C4.20 removes the O_L2(t^3) error first, and charges the fixed direction's quadratic Taylor term by its L4 norm. It therefore produces C4.21 on the actual integral flow. The connector/activation cross term is O_L2(t^4).

Crucially, C4.22 subtracts **moving** trained and frozen residuals. Gronwall first gives a readout difference O_L2(t^3). Its leading term is `(4/3)t^3 sum p_b E_b`; the residual-difference term integrates only into O(t^4). The other output contribution is `(2tS)(2t^2 E_x)`. Hence

`J(x)=4 E[S E_x]+(4/3) sum p_b E[H_x E_b]`.

This coefficient contains lower motion, connector training and readout feedback, and the error bound is uniform on the circle. No finite-width jet is substituted for a population remainder theorem.

### Unique matching, risk sign and finite capture — PASS

The frozen equation is `r'=-2Kr/3`; diagonalization gives strictly decreasing positive loss at all finite frozen times and convergence to zero. The full tangent kernel is positive semidefinite and norm bounded on the local ball, giving the positive lower loss bound in C4.12. Its range is therefore matchable uniquely. The exponential comparison yields the stated upper bound on tau and allows a strict clock margin inside the C.1 interval.

Adjunction gives `p^T J_train=16 A/3`, whereas `p^T a_train=2 B0`. With `L'_g(0)=-4 B0`, the mean-value argument yields `tau=t+8A t^3/(3B0)+O(t^4)`. The matched predictor correction is `J-beta a`, whose training p-projection vanishes. Thus positive training speed alone does not establish the risk sign; the candidate correctly retains the signed teacher projection after subtraction. Expanding the two squared errors gives exactly `chi=2 integral cos(3 alpha)(J-beta a)dmu`, with the claimed sign convention.

The passive first-layer identity C4.9 is exact because two training directions span R2, including under raw-GD parameter interpolation. A fixed angular net and uniform angular Lipschitz bound extend C.1's finite probes to whole-circle predictions and risk. Frozen capture follows with zero hidden mobilities. Finite frozen GF has a positive definite kernel with high probability; sufficiently small deterministic raw steps give positive decreasing eigenmode factors, including between steps. The matching range is interior on every fixed `[delta,T]`, so inverse stability transfers clocks and matched risks there. The finite random readout is retained. The proof neither takes `delta_n` to zero nor interchanges an infinite training-time and width limit.

## Analytic and arithmetic certificate audit

### Gaussian strip, tail and covariance bounds — PASS

The one-coordinate Fourier contour shift needs only one nonreal root coordinate at a time. Gaussian decay removes the vertical sides, and absolute Fourier convergence justifies evaluating periodization at zero. The deleted tail begins beyond `m*h`; monotonicity gives `2 gamma(mh)/(mh)`. Tensor telescoping multiplies previous positive rule masses; these masses are bounded by `1+delta_j`, not set equal to one. The kernel and driver do not renormalize them.

The tanh strip bounds `1,2,4` on imaginary magnitude at most pi/4 hold, including repeated factors. The executing dyadic grid uses `a=min(7,3/(4c))`, floors its spacing, and checks exact inequalities with `pi>3`. Its actual truncation radius is at least eight. Both target envelopes were checked with exact rational exponential partial sums; no target-30 coefficient execution is inferred.

The covariance interpolation inequality follows by twice integrating derivatives of a nonsingular Gaussian density and then adding/removing `delta I`. Bounded derivatives justify the singular endpoint limit. The lower covariance error charges exact versus stored directions. The upper covariance is the exact dyadic `A A^T`, automatically positive semidefinite; the full discrepancy from certified Q is charged even if a proposed residual variance was clipped. Hence no accuracy or smoothness theorem for numerical Cholesky/root construction is assumed.

The product-rule Hessian sums are 4, 6, 10 and 18 for the four primitive monomial types. Formal repeated indices do not invalidate the upper bounds. Finite label expansions give exactly the Price radii in C4.E9 and the executing table. Both exact and dyadic label L1 sums lie below 27/50, so the S and S-squared perturbation charges are valid. Neither the full innovation covariance nor the response mean-product is omitted.

### Elementary functions, operations and accumulation — PASS

I checked the degree-12 Horner recurrence against the C++ source. Its initial relative error is bounded by `(16/9)gamma_25+(4/3)(1/4)^13/13!<46u`. Eight squarings amplify the initial factor 256 times and rounding factors 255 times; exact rational comparison confirms the `2e-12` bound. The tanh rational map, rounding and saturation then give the global `5e-12` absolute bound. The tiny-input underflow exception is absorbed in the declared strict slack.

For grid nodes and preactivation dot products, the stated radius, coefficient and dimension bounds give the charged absolute errors. Gate errors follow from `1-H^2` and `(-2H)(1-H^2)`. The direct C++ evaluation has at most the stated six expanded activation/gate factors; finite label coefficient sums are bounded by one. Gaussian weights receive elementary, argument and density-constant errors. I checked that training moments are accumulated with three root masses only, while dynamic moments include the passive conditional sum. Otherwise a nonunit passive mass could bias ES2 and beta.

Long-double outer accumulation has at most `401^3` terms, with a separate bounded 401-term inner sum; the stated `4 gamma_(401^3)(2^-64)<1.5e-11` is verified exactly. The `1e-9` primitive envelope is safely larger than the summed operation bounds. IEEE binary64, round-to-nearest, long-double significand and excluded fast-math/FMA assumptions are checked or explicitly required. The rebuilt tested binary has exactly the hash recorded for both original runs.

### Circle differentiation and symmetry — PASS

The upper angular field is constructed as an isonormal image of the lower activation curve. Its mean-square derivatives are Gaussian with the indicated standard deviations; Gaussian moment bounds upgrade to every fixed Lp needed. This avoids differentiating a passive root factor at singular covariance. Lower/upper derivative bounds use finite Bell/Stirling recurrences with explicit Gaussian moment bounds, not sample-path analyticity.

I expanded the response terms in A6/A7 against C4.28. In A6, the first two terms contribute `l0*u1` and `g*l1*u1`; the training derivative response contributes another `2g*l1*u1`; the passive mean response uses `phi' H=-phi''/2` and contributes `g*l2*u2`. A7 contributes `4u0+2l0*u1`. These yield A9's coefficients `20/3,12,4,16/3` and the separately bounded clock term. The helper reproduces D8 exactly.

Eight integrations by parts and root-of-unity averaging give `2 zeta(8)D8/256^8`; the supplied elementary bound `zeta(8)<=8/7` suffices. Exact reflection/exchange and antipodal oddness make the integrand even and pi-periodic; the pi/2 teacher value is zero. Thus endpoint weight 2/256 and other 63 weights 4/256 are correct. The separate beta interval verifies the required `|beta|<=1/10` premise. The proved angular bound is approximately `1.61629e-7`; the producer conservatively adds `1e-6`.

## Original execution, maintained-source correspondence and independent reconstruction

The supplied original recorded argument vectors are (not rerun):

```text
studies/two_layer_test_risk/certificate_driver.py --target 26 --output data/generated/two_layer_test_risk/certificate_20260910_01
/home/amir/Codes/PDE/studies/two_layer_test_risk/certificate_driver.py --target 26 --output /home/amir/Codes/PDE/data/generated/two_layer_test_risk/certificate_reproduction_20260910_01
```

The metadata records the script arguments shown above; the original launcher and interpreter flags are not retained by `sys.argv`, so I do not claim to recover them. The source requires the compiler command `g++ -O3 -std=c++17 -fno-fast-math -ffp-contract=off`. Both supplied runs completed with exit status zero, target 26, 256 nominal angles, 64 evaluated nodes, 96-bit outward intervals, 86,101,134 upper nodes, and the same result hash. Recorded CPU times are 31.17975 and 30.667729999999995 seconds. These are supplied execution records, not runs launched by this reviewer.

I compared the original and maintained source directly and by normalized Python AST. All 20 shared helpers/classes have identical executable syntax after removing docstrings. The complete calculation/assembly `try` block, exception handling and final timing write are identical after removing the maintained version's moved compiler-version metadata query. All substantive changes concern locating source/kernel, fresh-output/type/optimization validation, one-thread worker isolation, return decoding and provenance. No mathematical operation, constant, loop, contraction order or error radius changed. An initial comparison assertion included the moved metadata query and failed; narrowing it to executable scientific correspondence repaired the check, without changing candidate code.

The rebuilt kernel hash is `8c5b241801eaa4b8912989b9e404eb9693e63e94487661071c3bfa7044c189c7`, identical to both recorded executions. The candidate therefore is not an unexecuted alternate numerical algorithm.

The saved-state reconstruction validates both complete runs. For each of 64 nodes per run it verifies: input token counts and exact binary echoes; deterministic root/grid recreation; every grid inequality/audit; reported outer and total counts; finite arrays of all declared lengths; Gaussian mass diagnostics; empty stderr; input/output hashes; exact lower and upper covariance/label errors; all seven contraction intervals; alpha/teacher intervals; separate raw and clock contributions; cumulative sum; and correspondence with the final-result row. All 128 node enclosures and all 256 supplied primitive calls pass. Every final fraction is reproduced exactly.

A separate calculation implements integer-endpoint interval arithmetic at 110 bits, 100-term Machin bounds, longer trigonometric series, fresh covariance-error bounds, and the generic four-slot Lambda/C contraction in C4.28–31. It does not call the driver's specialized contraction, use stored enclosures as primitive data, or evaluate a Gaussian coefficient sum. It rebuilds the primitive intervals from the saved IEEE bits. Every generic node result overlaps its independently reconstructed maintained enclosure, and its own aggregate plus the complete angular error is strictly positive:

```
175590711037408235549059771111 / 649037107316853453566312041152512
 <= chi <=
44231644403798799297883192773 / 162259276829213363391578010288128.
```

This independent enclosure also lies strictly inside `27/100000 < chi < 273/1000000`. It differs slightly from the published enclosure because the precision and algebraic grouping differ. The maintained saved-state reconstruction reproduces exactly:

```
5358604107658561212253567 / 19807040628566084398385987584
 <= chi <=
21597479156841685713774185 / 79228162514264337593543950336

2797504526179671494928101665 / 79228162514264337593543950336
 <= beta <=
2797556156441557459457527739 / 79228162514264337593543950336.
```

Exact cross-multiplication verifies C4.8a, including the strictly positive sign and the separate angular beta hypothesis. The raw teacher projection and clock subtraction are both retained in the independent check; the result is not a sign claim about the unadjusted projection alone.

## Standalone tests, interface and bounded execution

All commands below were run from the frozen edition, or by absolute path to its sources, with output confined to reviewer A scratch. Each new check was subject to a 60 CPU-second soft limit and 61-second hard limit. No third Gaussian coefficient integration, different resolution, network training or teacher/design search was run.

```sh
python -B code/tools/two_layer_risk/check_driver.py --output ../reviewer_a/driver_check
python -B code/tools/two_layer_risk/check_kernel.py --output ../reviewer_a/kernel_check
python -B code/tools/two_layer_risk/angle_error_bound.py --output ../reviewer_a/angle_check
python -B data/generated/two_layer_test_risk/signed_promotion_v1/reviewer_a/reconstruct.py
python -B data/generated/two_layer_test_risk/signed_promotion_v1/reviewer_a/boundaries.py
python -B data/generated/two_layer_test_risk/signed_promotion_v1/reviewer_a/arithmetic.py
```

The first three were launched through short `resource.setrlimit` wrappers and their full stdout/stderr retained as `driver_check.log`, `kernel_check.log`, `angle_check.log`. The final three scripts contain their own limits and are embedded in full below. The full reconstruction was repeated after an asynchronous output handle was not retained; the final logged run used 52.541500373 CPU seconds and passed. Neither execution called an integrator. The auxiliary arithmetic check initially passed all assertions but failed while converting a giant Fraction to a display string; only that diagnostic display was changed to float, with every deciding inequality remaining exact, and the completed check passed.

Results:

- Driver focused checks: PASS, including longer exact series, square roots, both grid targets, direct response-mean synthetic probability tables and Fourier symmetry weights.
- Kernel focused checks: PASS. Largest supplied finite-tensor discrepancy `5.88418203051333e-15`; rational elementary-function checks satisfy declared bounds. Omitted passive root returns 27 nodes; long-double significand is 64 bits.
- Angular helper: PASS, reproducing `41272525446939874982/31640625` and `20636262723469937491/127677049435953561600000000`.
- Full saved-state and independent generic reconstruction: PASS as detailed above.
- Boundary checks: PASS for import preserving caller environment; rejection of bool/float/string/Fraction/None targets; unsupported integers; empty/NUL/bytes/invalid outputs; existing file/directory and dangling symlink; unsupported platform; worker failure propagation; independent JSON return ownership; and worker command/thread environment. CLI help was executed from `/tmp` without compiling or calculating. Optimized Python was actually invoked and rejected before creating output. Five malformed/out-of-contract kernel inputs fail. Successful public-worker launch was tested with a recorder rather than launching another full calculation.
- Exact scalar arithmetic: PASS for Horner/squaring, long-double accumulation, finite rule mass, exponential partial sums, and both target envelopes.

The wrapper documentation accurately states that 900 seconds is a cumulative gate around primitive calls, not a hard compiler/process wall timeout. The output-directory reservation contract handles races; it does not promise general concurrent-writer protection. Partial output is retained on failure, and only `certify` is the supported callable entry point. Exact zero crossing returns INCONCLUSIVE rather than a successful positive certificate. The tool is independent of study files, archived arrays and Git at runtime; the only numerical dependency used to propose roots is NumPy, with its root error charged explicitly.

## Objections, scope and final component decision

| Attacked failure mode | Result |
|---|---|
| Wrong mean-loss/width normalization or initial readout regime | Closed for the stated model by raw differentiation and weighted correction |
| Dropped trained block, moving residual or readout response | Closed by the exact subtraction and integral expansion |
| Fresh-independent replacement of reused forward/transpose matrix | Closed by full source-response laws and generic reconstruction |
| Singular input/passive covariance invalidates inverse or derivative step | Closed: only Q,V training inverses; passive Price/isonormal constructions |
| Formal jet mistaken for actual population remainder | Closed by fixed-direction L4 and strong integral estimates |
| Training speed mistaken for equal-loss test-risk improvement | Closed by beta subtraction and signed teacher projection |
| Uncharged Gaussian mass, tails, root covariance, label or arithmetic error | Closed by explicit estimates, exact inequalities and all-node reconstruction |
| Conditional integration loses fourth-coordinate interactions or changes training masses | Closed by source inspection and direct finite-tensor tests |
| Angular Cholesky smoothness or floating symmetry implicitly assumed | Closed by isonormal derivative proof and exact symmetry |
| New maintained algorithm lacks executed correspondence | Closed by full source/AST correspondence, exact saved-state replay and matching rebuilt binary |
| Finite-width sign asserted uniformly at zero or unspecified limit order | Closed by the fixed-delta qualification and ordered C.1 capture |
| Missing required input or unexplained source mismatch | None found |

**Nonblocking editorial observation only:** the kernel's leading comment still says `See CERTIFICATION_ENGINE.md`, a historical name absent from the relocated tool directory, and the check-driver docstring uses the old `certificate_driver` name. Neither is a runtime dependency or a missing proof: the adjacent README and the complete C.4 supply the content. These comments can be left unchanged in this frozen accepted version. I do not require an edit, and this observation must not be used to silently modify accepted frozen bytes.

The accepted conclusion remains small and local: a positive cubic coefficient for one fixed three-point design, with a finite but unevaluated fourth-order remainder constant and time interval. No iid-sample bound, universal usefulness of feature learning, practical effect size, quantitative width, later-time benefit, or joint shrinking-delta claim is established. Two matching floating runs alone would not establish the result; the complete analytic bounds, source correspondence, checked execution contracts and exact rational decision are all necessary.

**All scientific components pass for the immutable v1 packet; there are no unresolved blocking objections and no required corrections.** If any proof or code correction is subsequently made, this report does not certify that changed packet.

## Reproducible reviewer sources and hashes

The full unique check sources below are retained in this tracked report, so generated scratch is not their sole durable source. The run prefix is the frozen directory; keep the scripts at their indicated `reviewer_a/` relative locations when reproducing. The final complete report SHA256 is retained separately as `reviewer_a/report.sha256` and delivered to the coordinator, avoiding a self-referential hash field. The manifest lists all remaining input hashes.

### reconstruct.py

SHA256: `c3731ac37742a1a5deaece8bb82127c4bce6ca0851d018f2f1670330e1e41456`.

```python
"""Independent saved-state audit; no coefficient integrator is called."""
from pathlib import Path
from fractions import Fraction as F
import ast, hashlib, importlib.util, json, math, resource, struct, sys, time
resource.setrlimit(resource.RLIMIT_CPU,(60,61))
ROOT=Path(__file__).resolve().parent.parent
ED=ROOT/'edition/code/tools/two_layer_risk/certificate.py'
sp=importlib.util.spec_from_file_location('candidate',ED); c=importlib.util.module_from_spec(sp);sp.loader.exec_module(c)
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bits(x):return struct.unpack('=Q',struct.pack('=d',x))[0]
def value(x):return F(struct.unpack('=d',struct.pack('=Q',x))[0])
def load(p):return json.loads(p.read_text())
# Compare executable mathematical syntax, not an author's equivalence claim.
o=ast.parse((ROOT/'packet/original_numerical_source.py').read_text());n=ast.parse(ED.read_text())
def strip_doc(node):
 if isinstance(node,(ast.FunctionDef,ast.ClassDef)) and node.body and isinstance(node.body[0],ast.Expr) and isinstance(node.body[0].value,ast.Constant) and isinstance(node.body[0].value.value,str):node.body=node.body[1:]
 return node
od={v.name:strip_doc(v) for v in o.body if isinstance(v,(ast.FunctionDef,ast.ClassDef))}
nd={v.name:strip_doc(v) for v in n.body if isinstance(v,(ast.FunctionDef,ast.ClassDef))}
unchanged=[k for k in od if k!='run']
assert all(ast.dump(od[k])==ast.dump(nd[k]) for k in unchanged)
# Complete loop/final assembly is identical, including exception and final metadata writes.
new_try=nd['run'].body[-1]
assert isinstance(new_try.body[0],ast.Assign) and ast.unparse(new_try.body[0].targets[0]) == "meta['environment']['compiler']"
new_try.body=new_try.body[1:]
assert ast.dump(od['run'].body[-1])==ast.dump(new_try)
# Box is independently implemented with INTEGER dyadic endpoints at 110 bits.
# It uses C4.27--31 generic four-slot Lambda, not the special A6/A7 loop.
S=1<<110
class B:
 def __init__(self,a=0,b=None):
  if isinstance(a,B):self.l,self.u=a.l,a.u;return
  a=F(a);b=a if b is None else F(b)
  self.l=(a.numerator*S)//a.denominator;self.u=-((-b.numerator*S)//b.denominator)
  assert self.l<=self.u
 @classmethod
 def ints(cls,l,u):
  z=cls();z.l=l;z.u=u;return z
 def __add__(self,v):v=B(v);return B.ints(self.l+v.l,self.u+v.u)
 __radd__=__add__
 def __neg__(self):return B.ints(-self.u,-self.l)
 def __sub__(self,v):return self+-B(v)
 def __rsub__(self,v):return B(v)+-self
 def __mul__(self,v):
  v=B(v);a=[self.l*v.l,self.l*v.u,self.u*v.l,self.u*v.u]
  return B.ints(min(a)//S,-((-max(a))//S))
 __rmul__=__mul__
 def __truediv__(self,v):
  v=B(v);assert v.l*v.u>0
  return self*B(F(S,v.u),F(S,v.l))
 def __rtruediv__(self,v):return B(v)/self
 def power(self,k):
  out=B(1)
  for _ in range(k):out=out*self
  return out
 def radius(self,r):return B(F(self.l,S)-r,F(self.u,S)+r)
 def mag(self):return F(max(abs(self.l),abs(self.u)),S)
 def out(self):return {'lo':str(F(self.l,S)),'hi':str(F(self.u,S))}
# Independent 100-term Machin enclosure, exact square roots, longer sin/cos.
def ar(q):
 a=sum(F((-1)**k,(2*k+1)*q**(2*k+1)) for k in range(100));return B(a,a+F(1,201*q**201))
PI=16*ar(5)-4*ar(239)
def root(z):
 z=B(z);a=math.isqrt(z.l*S);b=math.isqrt(z.u*S)+1;return B.ints(a,b)
labels=[B(F(1,3)),(1-root(5))/12,(1-root(5))/12];normal=1/root(2*PI)
def trig(z,sine=False):
 z=B(z);assert z.mag()<5
 r=B(0)
 for k in range(50):
  deg=2*k+int(sine)
  # Multiply exact scalar AFTER powers, unlike B scalar multiplication's grid.
  t=z.power(deg);a=F((-1)**k,math.factorial(deg))
  r+=B(min(F(t.l,S)*a,F(t.u,S)*a),max(F(t.l,S)*a,F(t.u,S)*a))
 return r.radius(F(5**100,math.factorial(100)))
def direction(j):return [[trig(a),trig(a,True)] for a in [B(0),PI/5,-PI/5,2*PI*F(j,256)]]
def cov(rows):return [[sum((x*y for x,y in zip(a,b)),B(0)) for b in rows] for a in rows]
def exactcov(rows):return [[sum(x*y for x,y in zip(a,b)) for b in rows] for a in rows]
def enclose(raw,key,st,real,price,eps,lab=0):
 r=F(1,10**9)+F(5,10**11)*st+F(6,10**15)*real+price*eps+lab
 return [B(value(x)).radius(r) for x in raw[key+'_bits']]
P=F(27,50)
def independent(j,lr,ur):
 ue=direction(j);uu=[[value(x) for x in lr['parsed_input_bits'][3+2*a:5+2*a]] for a in range(4)]
 G=cov(ue);Gh=exactcov(uu)
 eg=max((G[a][b]-Gh[a][b]).mag() for a in range(4) for b in range(4))
 Q=enclose(lr,'Q',1,1,2,eg);L=enclose(lr,'L',4,1,3,eg);T=enclose(lr,'T',4,1,9,eg)
 aa=[[value(x) for x in ur['parsed_input_bits'][5+4*a:9+4*a]] for a in range(4)];qh=exactcov(aa)
 eq=max((Q[4*a+b]-qh[a][b]).mag() for a in range(4) for b in range(4))
 pp=[value(x) for x in ur['parsed_input_bits'][-3:]]
 ep=sum((labels[a]-pp[a]).mag() for a in range(3));assert sum(abs(v) for v in pp)<P
 specs={'ES2':(P*P,P*P,2*P*P,2*P*ep),'V':(4*P*P,P*P,9*P*P,2*P*ep),'ddgram':(4,1,3,0),'ESdd':(4*P,P,5*P,ep),'dynamic_V':(4*P*P,P*P,9*P*P,2*P*ep),'dynamic_C':(4*P,P,9*P,ep),'dynamic_dd':(4,1,3,0),'dynamic_ESdd':(4*P,P,5*P,ep),'dynamic_Hdd':(4,1,5,0),'dynamic_SH':(P,P,2*P,ep)}
 H={k:enclose(ur,k,*v[:3],eq,v[3]) for k,v in specs.items()}
 # Complete formal slot derivative vectors E[partial_i U_a], i=0..3.
 Edd=[[B(0) for _ in range(4)] for _ in range(4)]
 for a in range(3):
  for b in range(3):Edd[a][b]=H['ddgram'][3*a+b]
  Edd[a][3]=Edd[3][a]=H['dynamic_dd'][a]
 Es=H['ESdd']+H['dynamic_ESdd'];p=labels+[B(0)]
 deriv=[[p[i]*Edd[i][a]+(Es[a] if i==a else B(0)) for i in range(4)] for a in range(4)]
 def lam(a,b,prod,d1,d2):
  return L[4*a+b]*prod+sum((T[64*a+16*b+4*i+k]*d1[i]*d2[k] for i in range(4) for k in range(4)),B(0))
 def contract(a,prods,d):
  return sum((p[b]*(Q[4*a+b]*prods[b]+G[a][b]*lam(a,b,prods[b],d,deriv[b])) for b in range(3)),B(0))
 train=[contract(a,H['V'][3*a:3*a+3],deriv[a]) for a in range(3)]
 A=sum((p[a]*train[a] for a in range(3)),B(0));beta=8*A/(3*H['ES2'][0]);assert H['ES2'][0].l>0 and beta.mag()<F(1,10)
 fx=contract(3,H['dynamic_V'],deriv[3]);back=B(0)
 for a in range(3):
  d=[B(0) for _ in range(4)];d[3]=H['dynamic_dd'][a];d[a]=H['dynamic_Hdd'][a]
  back+=p[a]*contract(a,H['dynamic_C'][3*a:3*a+3],d)
 return {'A':A,'B0':H['ES2'][0],'beta':beta,'a':2*H['dynamic_SH'][0],'J':4*fx+F(4,3)*back,'F':fx,'B':back},trig(6*PI*F(j,256))
# Saved-state preflight and exact maintained-source reconstruction for BOTH full runs.
manifest=load(ROOT/'manifest.json');checks=[];ind_rows=[];timer=time.process_time()
for run in ['certificate_20260910_01','certificate_reproduction_20260910_01']:
 d=ROOT/'evidence'/run;res=load(d/'result.json');meta=load(d/'metadata.json')
 assert meta['status']=='completed' and meta['exit_status']==0
 assert meta['source_sha256']['certificate_driver.py']==h(ROOT/'packet/original_numerical_source.py')
 assert meta['source_sha256']['certificate_kernel.cpp']==h(ROOT/'packet/certificate_kernel.cpp')
 assert meta['result_sha256']==h(d/'result.json')
 pi,p,no,nf=c.constants();pf=[v.midfloat() for v in p]
 assert load(d/'constants.json')=={'pi':pi.json(),'p':[v.json() for v in p],'normal':no.json(),'normal_float_bits':bits(nf)}
 total=c.I(0);raw=c.I(0);clock=c.I(0);beta=None;points=0
 for j in range(64):
  nd=d/f'angle_{j:03d}';row=load(nd/'enclosure.json');u=c.directions(pi,j);uf=[[v.midfloat() for v in a] for a in u]
  lr=load(nd/'lower_stdout.json');factor,var=c.root_factor(lr);ur=load(nd/'upper_stdout.json')
  for mode,mat,rr in [('lower',uf,lr),('upper',factor,ur)]:
   text=(nd/(mode+'_input.txt')).read_text();tokens=text.split();dim=2 if mode=='lower' else 4;counts=list(map(int,tokens[1:1+dim]));reals=list(map(float,tokens[1+dim:]));a=load(nd/(mode+'_audit.json'))
   cm,st,ev=c.grid(mat,26);wanted=st+[nf]+[v for aa in mat for v in aa]+(pf if mode=='upper' else [])
   assert counts==cm and [bits(x) for x in reals]==[bits(x) for x in wanted]==rr['parsed_input_bits']
   assert rr['mode']==mode and rr['long_double_mantissa_bits']>=64
   assert rr['total_points']==math.prod(2*x+1 for x in counts)==a['total_points']
   assert rr['outer_points']==math.prod(2*x+1 for x in (counts[:3] if mode=='upper' else counts))
   assert a['grid']==ev and a['input_sha256']==h(nd/(mode+'_input.txt')) and a['output_sha256']==h(nd/(mode+'_stdout.json'))
   assert not (nd/(mode+'_stderr.txt')).read_bytes()
   assert all(abs(value(x)-1)<F(1,10**8) for x in rr['grid_mass_bits'])
   for k,v in rr.items():
    if k.endswith('_bits') and isinstance(v,list):assert all(math.isfinite(float(value(x))) for x in v)
  assert len(lr['Q_bits'])==16 and len(lr['L_bits'])==16 and len(lr['T_bits'])==256
  for k,size in {'ES2':1,'V':9,'ddgram':9,'ESdd':3,'dynamic_V':3,'dynamic_C':9,'dynamic_dd':3,'dynamic_ESdd':1,'dynamic_Hdd':3,'dynamic_SH':1}.items():assert len(ur[k+'_bits'])==size
  low=c.lower_intervals(lr,u,uf,26);hi=c.upper_intervals(ur,low,factor,p,pf,26);vals=c.contraction(low,hi,p)
  assert {k:v.json() for k,v in vals.items()}==row['moments']
  for k,v in [('epsilon_first_covariance',low['epsilon_first_covariance']),('epsilon_upper_covariance',hi['epsilon_upper_covariance']),('epsilon_labels',hi['epsilon_labels'])]:assert str(v)==row[k]
  assert var==row['heuristic_conditional_variance']
  te=c.trig(6*pi*F(j,256),'cos');w=F(2 if j==0 else 4,256);ra=2*w*te*vals['J'];cl=2*w*te*vals['beta']*vals['a'];raw+=ra;clock+=cl;total+=ra-cl
  assert row['alpha']==(2*pi*F(j,256)).json() and row['teacher']==te.json()
  assert row['weighted_raw']==ra.json() and row['weighted_clock']==cl.json() and row['cumulative']==total.json()
  assert row==res['rows'][j] and row['index']==j
  beta=vals['beta'] if beta is None else c.I(max(beta.lo,vals['beta'].lo),min(beta.hi,vals['beta'].hi));points+=ur['total_points']
  if run=='certificate_20260910_01':
   vals2,te2=independent(j,lr,ur)
   for k,v in vals2.items():assert max(F(v.l,S),vals[k].lo)<=min(F(v.u,S),vals[k].hi),(j,k)
   ind_rows.append((vals2,te2,w))
 assert res['chi']==total.widen(F(1,10**6)).json() and res['nodal_sum']==total.json()
 assert res['raw_nodal_projection']==raw.json() and res['clock_nodal_subtraction']==clock.json()
 assert res['beta_intersection']==beta.json() and res['total_upper_nodes']==points==86101134
 assert F(res['chi']['lo'])>F(27,100000) and F(res['chi']['hi'])<F(273,1000000)
 assert F(res['beta_intersection']['lo'])>F(35309,1000000) and F(res['beta_intersection']['hi'])<F(35311,1000000)
 checks.append({'run':run,'nodes':64,'primitive_calls':128,'raw_arrays_and_contracts':'all checked','source_and_result_sha256_verified':True,'cpu_seconds_recorded':meta['cpu_seconds'],'chi':res['chi'],'beta':res['beta_intersection']})
raw2=sum((2*w*t*v['J'] for v,t,w in ind_rows),B(0));clock2=sum((2*w*t*v['beta']*v['a'] for v,t,w in ind_rows),B(0));chi2=(raw2-clock2).radius(F(1,10**6))
assert F(chi2.l,S)>F(27,100000) and F(chi2.u,S)<F(273,1000000)
out={'status':'PASS','unchanged_mathematical_functions_AST':unchanged,'main_calculation_try_block_AST_identical':True,'runs':checks,'independent_generic_four_slot_chi':chi2.out(),'independent_raw_projection':raw2.out(),'independent_clock_subtraction':clock2.out(),'independent_interval_bits':110,'cpu_seconds':time.process_time()-timer,'check_source_sha256':h(Path(__file__))}
(ROOT/'reviewer_a/reconstruction.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
```

### boundaries.py

SHA256: `0fa99a3fc2b812657669fabcb73cd762a98d71e9de3723577dcda348fd5baadf`.

```python
"""Standalone public-interface boundaries; worker launch replaced by a recorder."""
from pathlib import Path
from fractions import Fraction
from unittest.mock import patch
import importlib.util,json,os,resource,subprocess,sys,time
resource.setrlimit(resource.RLIMIT_CPU,(60,61))
root=Path(__file__).resolve().parent.parent;scratch=root/'reviewer_a';src=root/'edition/code/tools/two_layer_risk/certificate.py'
env=dict(os.environ);spec=importlib.util.spec_from_file_location('isolated_certificate',src);c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
assert dict(os.environ)==env
checks=[]
def reject(out,target,typ):
 try:c.certify(out,target)
 except typ:checks.append(typ.__name__)
 else:raise AssertionError((out,target,typ))
for t in [True,26.0,'26',Fraction(26),None]:reject(scratch/'never',t,TypeError)
for t in [0,25,27,31,-1]:reject(scratch/'never',t,ValueError)
for o in ['', '\0bad']:reject(o,26,ValueError)
for o in [b'bytes',12,None]:reject(o,26,TypeError)
reject(scratch,26,FileExistsError)
existing=scratch/'existing_file';existing.write_text('keep');reject(existing,26,FileExistsError)
link=scratch/'dangling_link';link.symlink_to(scratch/'absent_target');reject(link,26,FileExistsError)
assert existing.read_text()=='keep' and not (scratch/'never').exists()
with patch.object(c.sys,'platform','darwin'):reject(scratch/'never',26,RuntimeError)
# Check command/env/fresh paths/JSON return ownership without invoking any sums.
commands=[]
def fake_run(command,**kwargs):
 commands.append((command,kwargs))
 out=Path(command[command.index('--output')+1]);out.mkdir()
 (out/'result.json').write_text('{"decision":"INCONCLUSIVE","chi":{"lo":"-1","hi":"1"}}')
 return subprocess.CompletedProcess(command,0)
with patch.object(c.subprocess,'run',side_effect=fake_run):
 a=c.certify(scratch/'mock_api_26');b=c.certify(scratch/'mock_api_30',30)
a['chi']['lo']='changed';assert b['chi']['lo']=='-1'
assert json.loads((scratch/'mock_api_26/result.json').read_text())['chi']['lo']=='-1'
for cmd,kw in commands:
 assert cmd[:3]==[sys.executable,'-B',str(src.resolve())] and cmd[-1]=='--_worker'
 assert kw['check'] is True
 for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:assert kw['env'][k]=='1'
assert dict(os.environ)==env
with patch.object(c.subprocess,'run',side_effect=subprocess.CalledProcessError(1,['mock'])):
 reject(scratch/'never',26,subprocess.CalledProcessError)
help_result=subprocess.run([sys.executable,'-B',str(src),'--help'],capture_output=True,text=True,check=True,cwd='/tmp')
assert '--output' in help_result.stdout and '--_worker' not in help_result.stdout
optimized=subprocess.run([sys.executable,'-O','-B',str(src),'--output',str(scratch/'optimized_absent')],capture_output=True,text=True,cwd='/tmp')
assert optimized.returncode!=0 and 'without -O or -OO' in optimized.stderr and not (scratch/'optimized_absent').exists()
# Private kernel rejects violated fixed contracts before any substantial sums.
binary=scratch/'kernel_check/certificate_kernel';normal=.3989422804014327
cases=['','unknown\n','primitives\n0\n','primitives\n1\nnan\n','lower\n0 1\n0 .5 '+str(normal)+'\n'+'0 '*8]
for inp in cases:
 r=subprocess.run([str(binary)],input=inp,text=True,capture_output=True);assert r.returncode!=0 and r.stderr
checks+=['import_environment_unchanged','worker_environment_and_command','fresh_return_ownership','worker_failure_propagates','standalone_help','optimized_rejected','five_invalid_kernel_inputs']
result={'status':'PASS','checks':checks,'help':help_result.stdout,'optimized_rejection':optimized.stderr,'full_coefficient_runs':0}
(scratch/'boundaries.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
```

### arithmetic.py

SHA256: `62290fa5f1732d2717677b9ed562282c05d59be84ea272b230b3052da95b7951`.

```python
"""Exact finite inequalities used by the declared analytic/arithmetic bounds."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json,resource
resource.setrlimit(resource.RLIMIT_CPU,(60,61))
u=F(1,2**53)
def gamma(k,u=u):return k*u/(1-k*u)
delta=F(16,9)*gamma(25)+F(4,3)*F(1,4)**13/factorial(13)
assert delta<46*u
assert (1+46*u)**256*(1+u)**255-1<F(2,10**12)
assert 4*gamma(401**3,F(1,2**64))<F(15,10**12)
assert F(1000001,1000000)**4<F(1000005,1000000)
for x,b in [(26,195000000000),(30,10000000000000),(32,78900000000000)]:
 assert sum(F(x**j,factorial(j)) for j in range(81))>b
# Gaussian mass/tail/tensor bound via exact rational lower exponential bounds.
for target,expb,envelope in [(26,195000000000,F(5,10**11)),(30,10000000000000,F(1,10**12))]:
 delta_mass=F(2,expb-1);mass=sum((1+delta_mass)**j for j in range(4))
 strip=F(2,expb-1)*mass;tail=F(1,10*78900000000000)*mass
 assert strip<envelope
 if target==26:assert tail<F(6,10**15)
 else:assert strip+tail<envelope
p=Path(__file__).resolve().parent
out={'status':'PASS','initial_exponential_relative_error_in_u':str(delta/u),'eight_squares_upper':float((1+46*u)**256*(1+u)**255-1),'long_double_summation_upper':str(4*gamma(401**3,F(1,2**64))),'checks':'exact exponential partial sums, both cubature envelopes, summation and rule mass'}
(p/'arithmetic.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS: exact scalar arithmetic and B=26/B=30 envelopes')
```

### Output artifact hashes

- `reconstruction.json`: `81ca154bc0af7df645b1740d9025cac4d8bfa8fb4d323d9cd819c2a3281580f3`.
- `boundaries.json`: `db5a4657fbafda8e21aa27a59f8c8808a9eb949ad95e483007094c4b52942c32`.
- `arithmetic.json`: `7aef8648847eb1d2919115b6dbe5cd2d1639b5931b55fd71391a2f21bfefcbf2`.
- `driver_check/result.json`: `24bed93d205d655623135b6d52efdfa3fb18eb19f664510720d324eba758d277`.
- `kernel_check/result.json`: `27cbf86bf4a00dab38568ee3abab21484d23e339f6091a1d5f079b06c4df7792`.
- `angle_check/result.json`: `2a1d5ec88889cbe2f9dd80cd9b4faa7274b727db33a6c37d8c122122662c5f0a`.
