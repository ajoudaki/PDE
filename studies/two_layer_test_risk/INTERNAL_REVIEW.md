# Internal adversarial review of the matched-risk reduction

Reviewer: `internal_adversary`, 2026-09-10. Assignment:
`REVIEW_ASSIGNMENT.md`. This reviewer is distinct from the coordinator and
the three authors of the frozen derivation, remainder, and quadrature work.
This is an internal check, not either isolated promotion review or approval
to promote material.

## Verdict and exact accepted scope

**The frozen inputs support the stated local partial theorem. They do not
prove a positive or negative finite-time test-risk comparison.** I found no
blocking error in the cubic coefficient, the unique population matching
clock, the uniform fourth-order risk remainder, or their stated finite-width
consequences. The remaining sign obligation is substantive: no supplied
argument bounds the exact scalar `chi` away from zero. The numerical
convergence check is inconclusive even by its stated diagnostic gate.

This assessment concerns precisely two tanh hidden layers with linear stored
readout, initialization variances `(1,1/n,1/n^2)`, mobilities `(n,1,n)`, the
mean squared loss on angles `0,pi/5,-pi/5` of the radius-sqrt(2) circle,
labels `cos(3 alpha)`, and uniform whole-circle squared test risk for that
teacher. The frozen comparison trains only its readout from the same initial
features and matches the trained loss. In the population both initial
readouts are zero. At finite width both retain the same actual small random
readout.

With the notation of CUBIC_DERIVATION, the accepted conclusion is existence
of a deterministic `T>0` and finite `M>=1` for this fixed model such that

\[
 \tau(t)=t+\beta t^3+O(t^4),\qquad
 \beta=\frac{8\mathcal A}{3B_0}>0,\qquad
 |\Delta(t)-\chi t^3|\le Mt^4\quad(0\le t\le T),
\]

where `Delta=R(g_tau)-R(f)`, `B_0=E[S^2]`, and

\[
 \chi=2\int\cos(3\alpha)
       [J(x(\alpha))-\beta a(x(\alpha))],\frac{d\alpha}{2\pi}.
\]

The coefficient is explicit in fixed initial Gaussian moments, with at
most four upper Gaussian coordinates and two lower roots. These are ordinary
time coefficients, not derivatives without factorial normalization. The
constants are existential finite bounds on a local interval; no evaluated
radius, width rate, or quantitative width requirement is established.
The source C.1 theorem is applied on its own local interval with all its
hypotheses verified, as detailed below.

The nonzero hidden onset and positive initial nonaffinity also survive the
review at their stated fixed-model local scale. Whole-circle predictions
and risks converge uniformly on the local time interval in probability
under finite GF and every deterministic vanishing raw-GD step sequence.
Exact finite matching, convergence of those clocks, and any conditional
sign transfer are restricted to fixed closed intervals `[delta,t0]`,
`delta>0`. A sign on such intervals would follow from a subsequently proved
nonzero sign of `chi`. No unconditional sign transfer is accepted.

## Reading, isolation, and provenance

I read every scientific line of the six frozen central inputs: RESULT,
CUBIC_DERIVATION, MATCHING_AND_REMAINDER, both Python producers, and
QUADRATURE. I read the complete neutral assignment. SOURCE_AND_CHECKS was
consulted for source locations and hashes; its author verdicts were not
used as correctness evidence. I did not open the study history,
continuation disposition, previous reviews, or other reviewers' reports,
and did not perform author startup. All conclusions below were checked
against derivations and producer code rather than historical verdicts.

Complete relevant dependency coverage:

- `docs/README.md`, `docs/NOTATION.md`, and `code/README.md` in full.
- `docs/global_nonlinear.md`, sections 2--3 (181--500), A.1--A.4
  (1835--1893), and the complete C introduction/C.1--C.3 including the
  weighted correction (2449--3829). This includes the actual conditional
  Gaussian proof, singular-covariance passage, common action construction,
  weighted response/tail induction, one-reference stability, every-mesh
  comparison, GF diagonal argument, and strict-activity proof.
- `docs/finite_dynamics.md`, introduction and sections 1--4 (1--227).
- `docs/gaussian_calculus.md`, introduction and sections 1--3 (1--202),
  complete section 7.1 (1824--2155), and E (5338--5473).
- `code/pde/finite_jets.py` (1--304), including the complete called
  `finite_flow_jets`, composition/convolution helpers and argument checks;
  `code/pde/finite_network.py` (1--340), including its parameter, scaling,
  callback, input, label and mobility dependencies.
- Both required skills, `solve-math-rigorously` and
  `investigate-conjectures`, plus the research-contract, evidence-ledger,
  adversarial-audit and decisive-experiments references. The last was used
  to assess the retained numerical evidence and stopping rule, without
  authorizing a new run. No new proof-search portfolio was conducted.

Initial aggregate reads that were truncated were repaired with smaller
reads. No required proof input was missing. Sections for other architectures
and unrelated API operations were not imported as premises. No external
specialized theorem was needed beyond the contained proof scopes above.

I inspected all three retained metadata files, all aggregate result fields,
the entire finite-identity result, and parsed all 320 saved passive-angle
rows. A read-only verification recomputed each saved row's defining
identities, angle and teacher, the three risk sums, reflection/antipodal
diagnostics and successive relative changes. This only reaggregated saved
numbers; it performed no Gaussian or angle quadrature, network training,
new random sampling, or trajectory integration. The finite derivative
producer was reviewed but not rerun. The only file written by this reviewer
is this report. No Git operation was performed.

All six central hashes match the assignment. The dependency hashes match
the source inventory. Observed SHA-256 values are:

| Input | SHA-256 |
|---|---|
| REVIEW_ASSIGNMENT.md | `97fcb3ebbd06845144b006d20f6654127dd4320e261193656144a5dc0d33e88b` |
| RESULT.md | `845374726a1a378c3edd922a0e3b9ffc86e60c91cc191013deea96f11f815139` |
| CUBIC_DERIVATION.md | `3f46c878a77dd046c876d5195950f6262b3db06a025cb756518643f4c97ca495` |
| MATCHING_AND_REMAINDER.md | `ebefcae59267dd14a71d4e93e3a287126471f178a42646fe60b5abd45894157d` |
| check_coefficient.py | `2f6b9cb2c36415fcd910a4e5e16bb4eaa57ec450a7aef81c95a2a562c35728a3` |
| check_finite_identity.py | `fbf00ca6267536e9126b2dde3cfa416e352643044b45b155c233bf7a8bff7edf` |
| QUADRATURE.md | `54bcd350546353dca2282bdb2418768d0c153be62c84f9df0990927481d3a266` |
| docs/README.md | `4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453` |
| docs/NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| docs/global_nonlinear.md | `8c575acb99ed713ef688cafb39fe9d8d8430e80815d2a69ac6686bac2cc19101` |
| docs/finite_dynamics.md | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| docs/gaussian_calculus.md | `d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e` |
| code/README.md | `00f5070d35a3e9fb9d0e9886f0f6d9f680a8d34bb32307807d1f88afc807a774` |
| code/pde/finite_jets.py | `a8e22e14c7ce387636a7981a5e80556b975f83f8cf6a2b85ab22af877f5cca4c` |
| code/pde/finite_network.py | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |

The two skill hashes are respectively
`9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`
and `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de`.

## Actual mathematical attacks and outcomes

### 1. Loss normalization, stored scaling, and common lower orders

The strongest normalization failure would be importing C.3's unweighted
onset fields while evolving a mean loss, or treating the stored readout as
order one. Direct differentiation gives first/connector/readout velocities
with prefactors `-2/(3 sqrt(2))`, `-2/(3n)`, and `-2/3` respectively in raw
finite coordinates. The population connector rank-one map is `u E[v .]`,
so its finite representative is `u v^T/n`; no additional width factor is
missing. The initial readout RMS tends to zero, permitting C.1's explicit
vanishing-initialization-perturbation clause.

With `p=y/3`, I reconstructed `v(t)=2tS+O_L2(t^2)` and the two hidden
increments `2t^2 T_x` and `2t^2 R_x^hid`. In MATCHING_AND_REMAINDER the
unweighted `S,U,P,B` are three times these fields, whereas `T,A,M,R` are
nine times; its factor `c^2/2=2/9` produces the same hidden coefficient.
This resolves the apparent notation conflict between its hidden `J` and
the predictor `J` of CUBIC_DERIVATION.

Subtracting the actual readout equations gives, with `d=v-w` and
`e_x=H_f(x)-H_0(x)`,

\[
 d'=-\frac23\sum_b[(f_b-g_b)H_b+(f_b-y_b)e_b],\qquad
 f_x-g_x=E[dH_x]+E[v e_x].
\]

The estimate `e_x=O_L2(t^2)` makes `d=O_L2(t^3)` by the displayed integral
inequality. The moving-residual difference contributes only `O(t^4)` to
`d`, while `d=(4/3)t^3 sum_b p_b E_b+O_L2(t^4)`. This gives exactly
`J_x=4E[S E_x]+(4/3)sum_b p_b E[H_x E_b]`. The common frozen training
terms are `(2/3)Ky t`, `-(2/3)^2 K^2 y t^2/2`, and
`(2/3)^3 K^3 y t^3/6`. None is replaced by a fixed-residual trajectory.

As an independent algebraic route, expanding the three kernel blocks gives
`K^[2]=4(G o D+Q o V)+2E[E H^T+H E^T]`. Adjunction gives
`E[S E_a]=sum_b p_b(G_ab D_ab+Q_ab V_ab)`; integration of the output
equation then gives `J=(2/3)K^[2]p` and
`p^T J=(16/3) mathcal A`. Both routes agree, including the moving readout.

### 2. Reused matrices and singular/passive geometry

Replacing either orientation by a fresh matrix would delete the response
mean. I checked the finite conditional projection formula against both
constraints `WV=Y` and `W^TU=P`: its mean satisfies both, and its residual
is the Gaussian matrix projected off both observed spans. This yields
the reverse innovation covariance `E[FG]`, not a response-subtracted
covariance. Gaussian integration by parts converts the reverse mean into
`sum_i h_i E[partial_i F]`. Taking products therefore gives exactly the
`L_ab E[FG]` term plus the mean-product term in Lambda. The latter is
present in both the proof and `check_coefficient.py`.

The next forward call cannot be asserted to preserve fourth moments from
an L2 operator bound alone. Here it is explicitly conditioned on the three
forward and three reverse calls. For `A_x^perp` it has the law

\[
 WA_x=\sum_j q_{x,j}Y_j+\sum_j v_{x,j}U_j
                 +\|A_x^\perp\|_2\xi_x.
\]

The finite removed output projection has fixed rank, hence vanishing RMS
size. Its coefficients depend on the fixed `Q,V` and initial moments.
The query is measurable from the old transcript and the original lower
roots before its answer is observed. This proves the required marginal
fourth-moment bound. It does not require `xi_x` to be independent of the
passive `Y_x`, and the proof correctly makes no such assertion.

I checked the rank-two input representation
`Z_alpha=xi_1 cos(alpha)+xi_2 sin(alpha)`. Pairwise nonparallel training
directions make the tanh ridge functions independent: the finite-difference
argument isolates one ridge and forces a bounded scalar function with
vanishing high differences to be constant if dependence held. Thus `Q`
is positive definite without inverting `G`. Full support of `N(0,Q)`
makes `K` positive definite by varying one upper coordinate at a time.
The same full-support argument applied to
`S sum_a c_a tanh'(Y_a)` makes `V` positive definite; it does not divide
by `S`. All labels are nonzero here.

At coincident or antipodal passive inputs the four-slot covariance can be
singular. Integration by parts on a Gaussian root representation is still
valid. A covariance null vector is also a zero L2 combination of its
source fields, so different formal derivatives along that null direction
give the same contracted response. No passive Gram inverse occurs in
the analytic coefficient. The code solves against the nonsingular
training factor only and admits zero conditional passive variance.

### 3. Uniform remainder without false L2 smoothness

I attacked the proposed `O(t^4)` risk remainder at its potentially weakest
point: tanh need not define a sufficiently Frechet-smooth map on an entire
L2 ball. The proof avoids that premise.

The readout integral first gives an L-infinity bound `O(t)`. Integration
then gives `Z^1-Z^1_0=O_L2(t^2)`, `W-W_0=O_op(t^2)`, and
`Z^2-Y=O_L2(t^2)`, uniformly in the circle angle. The reverse law is
a bounded root function plus a Gaussian, so each fixed `P_b` has a
finite fourth moment. The bounded Lipschitz gate estimate

\[
 \|b(Z_t)-b(Z_0)\|_4
 \le C\|Z_t-Z_0\|_2^{1/2}=O(t)
\]

combined with Holder gives an `O(t)` error in the divided lower backward
field. It follows that the hidden velocity errors are `O_L2(t^2)` and
the parameter expansion errors are `O(t^3)` in their stated norms.
This uses no higher moment of the trained path.

The needed initial `T_x,A_x,R_x` fourth moments are uniformly bounded:
the training sums are finite with bounded angular coefficients, and the
two conditional Gaussian laws above have uniformly bounded coefficients.
For a fixed direction `V` with such a bound, scalar Taylor and the
Lipschitz removal of an L2 error give

\[
 \|\tanh(Z_0+t^2V+e_t)-\tanh(Z_0)-t^2b(Z_0)V\|_2
 \le \|e_t\|_2+C t^4\|V\|_4^2.
\]

Consequently the uniform feature error is `O_L2(t^3)`. In the predictor
it is paired with an `O(t)` readout, while the learned-readout error is
`O_L2(t^4)`. Every error product is bounded by Cauchy--Schwarz, giving
the claimed uniform predictor `O(t^4)` remainder. This is an estimate on
the actual integral solution; finite-width jets are not used to commute
derivatives with a width limit.

### 4. Whole-circle capture and source theorem applicability

The C.1 hypotheses hold with `L=2`, `d=2`, `m=3`, `omega_a=1/3`, unit
Gaussian variances and mobilities, bounded labels, tanh's bounded first
two derivatives, and zero limiting readout. Its weighted response proof
retains each source pulse's `Delta omega_b`, and its stability comparison
uses a single reference's tails. I checked the causal construction order
and the limit order: width first at fixed cutoff and coarse mesh, then
coarse mesh to zero, then cutoff to infinity. The GF consequence comes
from the separate finite-width Euler diagonal argument. No growing
program theorem or stronger global theorem is needed here.

The strongest passive-input concern would be silently applying a theorem
requiring positive training weights to zero-weight extra samples. Instead,
the two training first-layer fields at `0,pi/5` linearly determine every
passive first preactivation, at finite width and in the population. Tanh,
one action of the actual connector and pairing with the readout are
permitted fixed probes. On the finite and population norm balls their
predictors have a common angular Lipschitz bound. A finite angle net,
followed by the width limit and then shrinking the net spacing, gives
the supremum over the full circle. Uniform boundedness transfers it to
the risk. This verifies the compact-input extension without changing
the updates or asserting a growing-data limit.

### 5. Matching inverse, positive clock shift, and risk orientation

The frozen loss is `|exp(-(2/3)Kt)y|^2/3`, strictly decreasing from its
initial value to zero, because `K` is positive definite and `y` is nonzero.
The trained loss is nonincreasing and satisfies
`L_f(t)>=L_f(0) exp(-2c B_K t)>0`. These inequalities place it inside
the frozen range and give `0<=tau(t)<=B_K t/lambda_min(K)`, with the
inequality direction as written. A shorter interval keeps both clocks
inside C.1 and gives a lower bound on the magnitude of the frozen slope.

Directly, `L'_g(0)=-4B_0` and
`L_f(t)-L_g(t)=-2p^T J t^3+O(t^4)`. The mean value theorem first bounds
`tau-t` by `Ct^3`, then identifies its coefficient as
`p^T J/(2B_0)`. The resulting identity
`p^T(J-beta a)=0` checks loss matching and shows why positive hidden
training contraction cannot decide the teacher projection.

For the risk convention `Delta=R(g_tau)-R(f)`,
`g_tau-f=t^3(beta a-J)+O(t^4)` and the other factor in the difference
of squares is `-2 cos(3 alpha)+O(t)`. This gives the positive factor
`2 cos(3 alpha)(J-beta a)` in `chi`, with the stated remainder.
Reflection-even and antipodal-odd predictor symmetry permits a third
cosine harmonic; symmetry alone forces neither zero nor a sign here.

### 6. Hidden motion and nonaffinity

Conditional Gaussian reverse variance makes `D` positive definite.
The coefficient vector of `T_a` has entry `p_a G_aa=p_a!=0`, proving
its nonzero L2 norm. Conditional variance of `A_a` contains the nonzero
coefficient `p_a tanh'(Z_a)^2` against a nondegenerate Gaussian. Projection
onto the initial forward span cannot remove it. The subsequent forward
innovation therefore has positive variance which the training-only
`M_a` cannot cancel. Thus both hidden onset directions are nonzero.
The derivative gates are strictly positive for finite arguments, so their
activation onset directions are nonzero too. Direct substitution into
the flow gives order-t speeds and the stated integrated squared-speed
coefficients; an initial speed bounded away from zero is not inferred.

For variance `v>0`, Gaussian integration by parts gives
`Cov(sqrt(v)N,tanh(sqrt(v)N))=v E[sech^2(sqrt(v)N)]`.
The displayed best-affine-fit error is therefore correct. Equality in
the corresponding Cauchy--Schwarz inequality would make tanh affine
on a full-support Gaussian law, which is impossible. L2 continuity
and the positive initial variances preserve the finitely many local
lower bounds. This certificate concerns absolute nonaffinity at fixed
depth and does not by itself imply a test-risk benefit.

### 7. Finite GF/raw-GD quantifiers

The initialized finite hidden kernel blocks are generally nonzero with
the actual finite random readout. Treating them as exactly zero would
invalidate a fixed-width expansion; the report explicitly avoids that
identification. Convergence of the empirical frozen Gram to positive
definite `K` gives a positive definite finite Gram with probability
tending to one. For raw GD the eventually satisfied condition
`eta_n c lambda_max(K_n)<1` gives positive residual contraction factors
strictly below one. Linear parameter interpolation preserves their
strict decay, so the frozen interpolated loss has a unique inverse.

On fixed `[delta,T]`, strict population loss decrease from initialization
and positive loss leave uniform margins inside the frozen range.
Uniform finite loss errors and the nonzero population inverse slope
give uniform clock convergence. The whole-circle risk convergence then
transfers a sign only if it has first been proved in the population,
whose magnitude would be bounded below by `|chi| delta^3/2` there.
This does not allow `delta_n` to tend to zero with width or assert a
fixed-width sign arbitrarily near initialization.

## Numerical/code audit and unresolved obligations

The coefficient code implements the displayed upper derivative means and
both terms of the reverse mean product with the correct index orientation.
Its `mu_F` retains the two partials when a passive slot equals a training
slot. Its conditional covariance construction preserves the original
two-root input law. The maintained jet producer updates all degree splits
of the residual and actual transpose and uses the raw mean-loss factors.
The finite deterministic check compares those jets to independently
assembled onset fields, the frozen matrix-exponential coefficients, and
the kernel expansion at one supplied width-five state. The retained
maximum discrepancy is `8.673617379884035e-19`. This is a finite algebra
check, not a Gaussian limit or test-risk result.

The three quadrature result hashes match their metadata. Reaggregation
of every saved row gives the recorded risk coefficients within
`5.43e-20`; row coefficient/matching discrepancies are at most
`3.26e-19`. All saved numbers are finite, all saved angles and teachers
match their definitions, and the recomputed parity errors match the
metadata summaries. The results are:

| Order / angles | Saved `chi` diagnostic | Relative change from prior run |
|---|---:|---:|
| 12 / 64 | `0.00029320434041843317` | — |
| 20 / 128 | `0.0002776889548020482` | `5.58732544%` |
| 28 / 128 | `0.00027307732354152825` | `1.68876390%` |

The algebraic training identity holds even under consistently substituted
quadrature, so its small discrepancy cannot certify integration accuracy.
The final training covariance still has `Q00-Q11` approximately
`7.7671e-6`, whereas exact rotational invariance makes these diagonal
entries equal. Thus parity preservation and covariance reconstruction
accuracy do not establish accuracy of the Gaussian integration itself.
The change of both Gaussian and angle resolutions in the first pair also
does not separately estimate their errors. No supplied analytic or interval
bound encloses either error, and no error has been propagated through
`Q`, the response means, `B_0`, `beta`, and the signed risk projection.

The metadata records three successful runs of the same producer, one
numerical-library thread, no random seed, float64 arithmetic, and total
reported CPU time about 21.043 seconds. The stated three-run budget is
exhausted. I did not run another quadrature or independently regenerate
these retained integrations; source review and complete saved-row checks
are the numerical review scope.

Retained output SHA-256 values (paths below are relative to
`data/generated/two_layer_test_risk/`):

| File | SHA-256 |
|---|---|
| finite_identity_20260910_01/result.json | `969a9f66d1734970ad829fd90a73f911024dd81253e672113ce53b03a47aeeaf` |
| quadrature_20260910_gh12_a64/result.json | `92237f9d7e0ea48ebe731cf8850100b96d9b04d73680d5e127c862c4bef225ac` |
| quadrature_20260910_gh12_a64/metadata.json | `1c7381a9bf07d7446c8aaaaa4fc696e0d0e07324d4d92e8a3e30479f2f73007c` |
| quadrature_20260910_gh20_a128/result.json | `fbc918cb54c8e04229469a941428665677c14855793d5afb6b668c2e2e0843d6` |
| quadrature_20260910_gh20_a128/metadata.json | `5f0bda253ac8b6551eec39d3e7f4aeb28bd85f0a98b73f8b095311174670f429` |
| quadrature_20260910_gh28_a128/result.json | `94ef9f751004aa55fd7ed4f1eba788a245efa869ee25c509e2d33b8295a60409` |
| quadrature_20260910_gh28_a128/metadata.json | `569cdaf4f2e45789ae06524d783c2a0d35c8356649bfdafd0ba305f71ea922da` |

The unresolved major obligation for the desired full result is a rigorous
nonzero signed bound for the exact `chi`, or a further justified coefficient
if it is zero. None of the finite identities, positive hidden motion,
positive clock shift, or positive quadrature values supplies that bridge.
No further mathematical objection to the explicitly scoped partial theorem
survived the attacks above. This internal acceptance does not establish
novelty, generalization to other teachers/data, a global flow comparison,
or promotion readiness.
