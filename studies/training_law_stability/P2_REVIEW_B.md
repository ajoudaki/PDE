# Independent scientific review B of proposed edition P2

**Verdict: ACCEPT for the scientific scope stated in the frozen candidate.**

I found no required correction in the proposed theorem, its necessary proof
dependencies, or the new guide and chapter-scope assertions. This is a complete
independent scientific review of the supplied edition, not an integration
review, a novelty certification, or authorization to promote it.

## Identity, isolation, and coverage

Reviewer identity: `/root/p2_scientific_b`, a fresh reviewer distinct from the
named authors/assembler `/root`, `/root/transport`, `/root/population`,
`/root/nonlazy`, and selector `/root/selector`.

I read the neutral assignment `P2_SCIENTIFIC_ASSIGNMENT.md` and the following
scientific inputs completely, including every dependency proof body:

| Input | Exact coverage |
|---|---|
| `P2_ADDITION.md` | Lines 1–1423, all statement and proof units C.4.1–C.4.4 |
| `P2_DEPENDENCIES.md` | Lines 1–1310, including the notation contract, III.F.1–9, A.1–A.2, C.2, and finite dynamics §§1–4 |
| `P2_DOCS_README.md` | Lines 1–269, complete proposed guide |
| `P2_GLOBAL_EDITS.json` | Lines 1–22, every complete old/new replacement |
| `P2_MANIFEST.json` | Complete manifest |

An output truncation in the initial batched read of the dependencies was
repaired by rereading lines 1–112; all other dependency lines were read in
complete sequential excerpts. The addition was read in complete sequential
excerpts, with overlap at excerpt boundaries.

I personally read the required skills
`/etc/codex/skills/solve-math-rigorously/SKILL.md` and
`/etc/codex/skills/investigate-conjectures/SKILL.md`, and the latter's complete
`references/research-contract.md` and `references/adversarial-audit.md`.

I did not read author startup material, the study README or history, prior
packets, verdicts, author checks, selector findings, or another review. I did
not contact another reviewer, delegate this review, run training experiments,
modify a candidate, or perform any Git operation. The assembled/baseline
files and unchanged live dependencies were read as bytes solely to verify
their listed hashes, not consulted for their content. The scientific review
does not depend on the unchanged chapter complement. My only written product
is this assigned report.

## Frozen-input verification

All seven `inputs` and all five `unchanged_live_dependencies` entries in the
manifest matched their SHA-256 digests when checked:

| File | Verified SHA-256 |
|---|---|
| `P2_ADDITION.md` | `b1d34b78bd50354ce2d036046a180a2beba415530472cbd32264684b0b378774` |
| `P2_DOCS_README.md` | `95b14c5a0430a783023d412d0103d8598a476963bad19180e2d4d0e2291bce3e` |
| `P2_GLOBAL_EDITS.json` | `bd802de5b3a69d1c903eb1454f7a5d353195e340ceb16a63ba85de9c820e369a` |
| `P2_DEPENDENCIES.md` | `606fe87a97b91a8cad31a26d9e545c4b51ebefd582e55a7ba1b2311bfa2f9469` |
| `P2_GLOBAL_BASELINE.md` | `8c575acb99ed713ef688cafb39fe9d8d8430e80815d2a69ac6686bac2cc19101` |
| `P2_README_BASELINE.md` | `4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453` |
| `P2_GLOBAL_EDITION.md` | `1945ef5d407eafd534b32185e952fa3ed479605f3ffec09afd468b6266fd18d9` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| `docs/finite_dynamics.md` | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| `AGENTS.md` | `a5e5b3749d9e9ee088c659bc2cf4ddb2d88adf371d98bf34140ded532020a517` |
| `RESEARCH_WORKFLOW.md` | `4323e5ada1a4875af2c8121c742c50f07d8ff5b569c3aa71e11ef9a14605b442` |

The dependency document's internal heading says version R1. This does not
create a mathematical input ambiguity: P2 names and hashes the exact complete
dependency document it uses.

## Reconstructed contract and hypotheses

The target is the actual simultaneous stored-weight GD algorithm for two
equal-width hidden tanh layers, input dimension two, no biases, mean
unhalved square loss, Gaussian block variances `(1,1/n,1/n²)`, and mobilities
`(n,1,n)`. Inputs range over the entire normalized circle and labels lie in
`[-Y,Y]`, with fixed `Y>0`. Initialization is independent of iid observations
when random observations are used.

The limiting state is the full first row in `L²(Omega_1; R²)`, a bounded
middle action between the two generated probability Hilbert spaces, and the
stored readout in `L²(Omega_2)`. State comparison uses the sum of row L²,
middle operator norm, and readout L², on a common population carrier or at
the same finite width. It is not a cross-width operator-norm convergence
claim. The initialized action retains the Gaussian matrix and its actual
transpose limit. Learned increments are Hilbert–Schmidt.

The horizon is one positive interval depending only on the fixed model and
Y. The law class is every probability law on the compact observation space,
including degenerate, atomic, and nonatomic laws. The comparison metric is
Wasserstein-1 for `|u-u'|+|y-y'|`. The theorem promises a near-linear law
modulus, the associated deterministic infinite-width replacement bound, and
an absolute value of an expected train–test gap with time supremum outside
the expectation. It separately promises actual-GD prediction, risk, and
paired activation-observable consistency under arbitrary simultaneous
sampling/width/step growth satisfying the stated limits.

The finite reference oracle is a proof construction from previously computed
population Euler contractions. It is not the asserted deployed population
state or a playback of the future actual network. The final flow is
autonomous and restartable in the reached bounded class. No finite scalar
dimension, fitting, useful risk reduction, global time, finite-width rate,
or universal hidden-activity assertion is made.

## Argument reconstruction and component verdicts

### 1. Exact finite normalization and full-row transport — PASS

Differentiating `f=c^T h²/n` gives gradients `delta¹ u^T/n`,
`delta²(h¹)^T/n`, and `h²/n`. Multiplication by the three mobilities and by
the derivative `2r` of the unhalved squared loss gives exactly (T2), with
finite rank-one representative `a b^T/n`. The reverse matrix action and
rank-one adjoint therefore have the claimed normalization. Raw GD evaluates
all three blocks at the same old state, and parameter interpolation requires
the recomputed forward map used in the proof.

The retained row gives
`||(w-bar w)·u + bar w·(u-u')||₂ <= D+B|u-u'|`.
This controls every passive input and the explicit input factor in the
first-row update. The successive backward comparisons are also correct:
the top gate contributes one factor R; the lower comparison propagates that
error through only bounded operators and gates, and adds a second term
proportional to R. It does not multiply the two cutoff factors. The
first-row, middle, and readout integrand decompositions in lines 323–350
then yield (T7) with a single `(1+R)`.

All tails are individual fields of the second marginal of the coupling.
Integration consequently yields exactly the weighted reference tail sum.
There is no hidden maximum over data, no root/backward-product tail premise,
and no Gram inverse. The same estimates hold under normalized finite
pairings. The tanh bounds give the common first-exit ball and velocity bound
independently of the law's support size.

### 2. Fixed Gaussian programs and common actions — PASS

I checked the full conditional Gaussian argument in III.F.1–5. Successive
conditioning is justified for adaptive inputs because each query is fixed
conditional on the prior transcript. The minimum-norm constrained Gaussian
formula respects both orientations of the same matrix. The removed fresh
projection has normalized expected squared size at most the fixed number of
past queries divided by n. Conditional test-function and second-moment
calculations establish the fixed-program convergence in probability.

The source-response calculation cancels the previous-query regression
terms. Independence belongs to the oriented source groups, not to the
forward and reverse answers. The singular-query proof adds an independent
input perturbation at each call, proves the fixed positive perturbation
case, and then removes it through the operator bound and continuous
positive-semidefinite square roots. It does not assume pseudoinverse
continuity. Its formal derivative convention retains the correct contracted
answer on singular support.

The countable language contains the full root pair and enough bounded
smooth cylinder maps for density in each generated L² space. Passing exact
finite linear identities and the high-probability operator bound to every
fixed generated probe gives a well-defined bounded linear action. Passing
the finite transpose pairing first on the dense generated span, then by
continuity, gives its actual Hilbert adjoint. Compatibility follows from
finite unions using the same arrays. Completion handles arbitrary input
directions and coefficients, with no law-dependent unspecified extension.

A.1 correctly extends values by continuous at-most-linear instructions and
L² approximation, choosing each smooth approximation before its prefix
tolerance. A.2 supplies the necessary neural-product derivatives: with a
fixed transcript, the bounded gate and gate derivative give polynomial
derivative envelopes in finitely many subGaussian roots/Gaussian sources.
Their uniform integrability justifies removing the clips. These arguments
are used only for separately fixed programs.

### 3. Weighted response tails — PASS

I checked all of C.2, not only its concluding bound. Its neural recursions
are the projected full-row and actual-action updates. The residual bound,
source RMS bound, bounded first two activation derivatives, unit marginal
first-preactivation variance, zero readout root, and `|G_ab|<=1` required in
the application all follow from the candidate's stated model and ball.

The norm `sup_(p>=2) ||U||_p/sqrt(p)` gives the displayed exponential-square
and absolute-exponential bounds. Jensen uses the weights
`Delta omega_b/(k Delta)`, so it needs no independence over input or time.
The derivative-prefix maxima in the proof are bounded by a common weighted
sum of individual backward magnitudes; they are not estimated by a maximum
of Gaussian fields.

In the backward-slot argument the direct pulse is exactly proportional to
`Delta omega_b`. The recursive terms preserve it, so the bound on the
forward response contains no inverse tiny weight. The full forward-slot
row bound and Cauchy–Schwarz give the backward response cap without summing
unweighted data tails. The caps can be selected in the stated bottom-up,
then top-down order before reducing the time. The literal causal induction
does not use its own unconstructed current response. For L=2 specifically,
the forward response uses only prior lower backward fields, and the current
backward response starts from the already computed readout.

This validates the uniform-in-finite-law, uniform-in-mesh subGaussian
marginal estimates needed for (P11). The positive variable-step extension
also justifies a recomputed affine interpolation time by one final shorter
Euler step; no path-supremum Gaussian tail is inferred.

### 4. Strong integrals, arbitrary laws, uniqueness, and restart — PASS

The bounded-multiplier argument proves joint backward continuity in the
strong state/input topology despite the lack of a general L² Fréchet
derivative. Compactness of the circle turns the needed convergence into
uniform convergence over input. Continuous Banach-valued integrands have
compact, hence separable range, resolving Bochner measurability even in the
ambient operator space. The rank-one difference bound also holds in the HS
norm; thus the learned increment assertion is stronger than merely compact
increments and is justified.

For finite laws, comparison of preceding Euler grid states introduces only
`V(Delta+Delta')`. The one-reference Gaussian tail gives a Cauchy estimate
`C exp(aR)[(1+R)(Delta+Delta')+exp(-cR²)]`. Sending meshes to zero and then
R to infinity produces a full-state continuous limit, and field continuity
identifies its integral equation and strong C¹ regularity.

Finite law approximations of any compactly supported probability law exist
without boundary-zero cells or restrictions on weights. The same comparison
completes the finite-law flows in the full state path space. Joint
state/law continuity of the vector field is explicitly proved with a
coupling and uniform continuity, so the limit is a solution, not just a
limit of observations.

The transfer of tails is appropriately weaker than a continuum-wide
pointwise subGaussian claim: bounded Lipschitz truncations first pass the
expectations and law integral, then monotone convergence yields the
integrated exponential bound. Cauchy–Schwarz over the law gives exactly the
integrated individual tail norm needed for comparison.

Uniqueness compares an arbitrary strong solution against the constructed
reference; no tail hypothesis is silently imposed on the other solution.
The bound `C exp(aR-cR²)` tends to zero. Choosing
`R=K sqrt(log(e/q))` in the changed-law bound, with `cK²>=2`, yields the
claimed `q exp(C sqrt(log(e/q)))` modulus. The proof separately treats q=0
and q>1. Restart applies on the remaining local interval in the stated ball.
Its intrinsic generated-space statement is supported by restarted Euler
comparison to the already constructed continuation and closure under law
integrals; it does not presume new Gaussian bounds at arbitrary states.

### 5. Actual GD and all simultaneous limits — PASS

The proxy uses the actual first and middle initialized arrays and adds the
actual random readout to its readout parameter. Its population program uses
zero limiting readout. These are consistent because the actual readout's
normalized squared RMS has expectation n^(-2). The actual GD readout is
never set to zero.

At a fixed finite law and proof mesh, expanding the proxy middle matrix
exposes only finitely many contraction errors. Each tends to zero by the
fixed-program theorem. Forward recomputation follows by Lipschitz bounds;
backward recomputation uses a fixed reference cutoff and then removes it.
The tail comparison via an oracle field and a continuous cutoff avoids
assuming convergence for discontinuous tail tests. The resulting assigned
velocity errors and individual weighted tails suffice for (A7).

The actual, possibly very large dataset appears in (A7) only through its
transport distance to the fixed reference law. Fine GD history is never
passed to the fixed-program theorem. The actual state has the deterministic
ball estimate on an initialization event; it does not need a finite-width
Gaussian-tail theorem. The enlarged proxy ball and its speed bound follow
from sums of finite rank-one increments and their limiting RMS bounds.

For fixed passive-input/time nets, additional forward evaluations remain a
fixed program. Full-row and operator bounds supply the uniform Lipschitz
estimates that remove both nets. Interior-time evaluations identify the
forward map of interpolated parameters, not linearly interpolated outputs.
The stated order—width and actual-step sequence first at fixed reference,
proof mesh and cutoff; then proof mesh and reference accuracy; then cutoff—
is valid. Equivalently one selects the cutoff first for a desired error,
then the finite reference and mesh, and finally sufficiently large indices.
No uniform rate over all fixed programs is needed.

### 6. Risk limits and the ghost exchange — PASS

The square-loss integrand on the good state ball has the displayed uniform
Lipschitz constant on joint input/label space. Predictor uniform error and
law transport therefore control the empirical training loss and population
risk uniformly in time. Only convergence in probability is asserted for
finite random networks, so no unstated integrability of bad initialization
events is needed.

The elementary compact-partition proof gives iid empirical W1 convergence
for atomic and singular laws as well. Since all remaining reference-program
errors depend only on the fixed reference and initialization, a union bound
extends the deterministic-data comparison to independent iid sampling
without a relative growth condition on n, m, or eta.

Single replacement costs at most `(2+2Y)/m`. The proof correctly uses the
unoptimized cutoff estimate for large m rather than assuming monotonicity
of a displayed modulus. Enlarging the constant covers all remaining small
m. The resulting loss stability is deterministic for the infinite-width
empirical-law map.

In (A12), exchange of `(Z_i,Z_i')` transforms
`ell(f_S,Z_i')` into `ell(f_(S^(i)),Z_i)` while preserving the joint law.
Subtracting `ell(f_S,Z_i)` then exposes the replacement difference. This
identity holds at each deterministic time; taking an absolute value of its
expectation and then a time supremum gives (A13). It does not bound
`E|gap|`, `E sup_t |gap|`, or the gap at a sample-selected time. The
statement and guide preserve precisely that order.

### 7. Paired activation observables and open-family motion — PASS

The fixed-program observable includes current and initial activations on
the same neuron indices. Its second-moment convergence, the state/input
bounds, and fixed time/input nets transfer the training-averaged squared
displacement. This is an independent observable argument, not an inference
from predictor convergence or an arbitrary coupling of activation marginals.

For the reference law I independently checked the factors in (6).
Writing `p=y_0/2`, the readout derivative at zero is `2S`; the two backward
fields are therefore `2t U_a` and `2t phi'(g_a)P_a` to first order. The
mean-loss factors give lower-preactivation and middle-action increments
`2t² T_a` and `2t² sum_b p U_b tensor h_b`. The activation multiplier
argument and `E[h_a h_b]=q_0 delta_ab` then give the stated `C_a`, `R_a`,
and `E_a`. Only strong continuity and bounded multipliers are required;
there is no unjustified second Fréchet derivative on an L² ball.

Actual adjunction gives
`<h_a,P_a>=p E[xi_a tanh(xi_a) phi'(xi_a)]>0`.
The independent other upper Gaussian contributes zero. Because the tanh
gate is positive almost surely, each lower `C_a` is nonzero. For the upper
layer the positive identity (9) retains both the changing-matrix and
changing-lower-feature contributions, so they cannot cancel collectively.
Its left side equals `p sum_a E[S E_a]`; hence the upper averaged squared
coefficient is strictly positive.

The resulting `A_ell(mu_0,t)=2 c_ell t²+o(t²)` supplies the specified
positive time and margin. The supremum definition of s_0 causes no endpoint
problem because t_0 lies strictly below it. The transport bound for J uses
both state change and change of averaging law, including the initialized
activation's input dependence. Choosing a radius using a modulus tending
to zero proves a relative open neighborhood in all admissible laws.
Short-arc spreading and small input rotation respectively produce nonatomic
and correlated members. The simultaneous observable limit then gives the
joint high-probability finite-network lower bounds with the smaller margin.

### 8. Proposed guide and chapter scope edits — PASS

The new guide claim in line 155 states the fixed two-hidden-tanh, bounded
circle-input, local scope and lists only the established theorem's outputs.
Lines 254–261 distinguish the absolute value of the expected gap from the
expected absolute gap and retain the global-input-population limitation.
Every old/new replacement in `P2_GLOBAL_EDITS.json` properly separates C.4
from the fixed-data statements and confines activity to the specified open
family. None upgrades the theorem to a finite-width rate, fitting, useful
risk improvement, global time, or universal activity claim.

The guide's prior-work paragraphs are contextual and explicitly do not
supply theorem hypotheses. This isolated review does not independently
certify all unchanged chapter summaries or external literature summaries;
none is needed to complete the candidate's scientific proof.

## Adversarial checks and outcomes

| Attack | Actual check and outcome |
|---|---|
| One atom, repeated inputs, incompatible labels | The force integrates linearly in the residual and needs no distinctness or invertibility. Averaging incompatible labels changes the force and achievable risk, not existence. No fitting conclusion is used. Survives. |
| Arbitrarily tiny atom weights | Followed a single backward-source pulse through C.2 (30)–(32): its factor remains `Delta omega_b`; cap constants never divide by it. Survives. |
| Singular query and data Grams | Read and checked the positive-noise regularization and square-root passage, then verified the transport argument uses only `|G_ab|<=1`. Survives. |
| Training directions do not span the input plane | Full first-row initialization and updates retain the passive root coordinate. The full Frobenius/L² bound, rather than a training-projection norm, controls arbitrary input directions. Survives. |
| q=0, q near one, and q>1 | Equality/uniqueness covers zero; cutoff optimization is confined to its logarithmic domain; the common ball handles larger q. No illegal log evaluation. Survives. |
| m=1 and replacement distance above one | The finite number of small m values is absorbed using the uniform predictor bound, with constants allowed to depend on Y. Survives. |
| Zero signal or zero conditional label mean | At `(w_0,A_0,0)`, hidden velocities vanish and `dot c=2 int y H_0²(x) dmu=0` when the conditional label mean vanishes. Uniqueness permits the stationary solution. The open-family assertion is not universal and is consistent with this case. |
| Actual random readout, including unusually large individual coordinates | Its RMS perturbation is retained exactly. The comparison uses tails of the fixed reference, so no individual-coordinate or actual-GD-tail bound is required. Survives in the stated probability mode. |
| Arbitrarily many fine steps or actual observations | The growing objects enter only the deterministic comparison and bounded law cost; all probabilistic program uses remain fixed before width tends to infinity. Survives. |
| Interpolation mismatch | Checked appended interior-time evaluations and state-speed bounds: the limit concerns recomputed forward quantities at interpolated parameters. Survives. |
| Hidden high-to-low tail feedback | Operator norms propagate the existing backward error without a second R, and Gaussian reference tails control the new gate multiplier. No omitted tail source remains in (T7). Survives. |
| Cancellation of upper hidden motion | Identity (9) makes the combined upper coefficient positive using the actual adjoint; no independent-backward replacement or omission of the lower-feature contribution. Survives. |
| Wrong expectation/supremum order | Reconstructed the ghost exchange at fixed deterministic time and checked the subsequent operations. Stronger absolute-gap and selected-time assertions are expressly absent. Survives. |
| Hidden oracle or nonrestartable state | The oracle is fixed and removed in the approximation proof; the final equation and reached-state Euler restart use only the current full state, actions, adjoints, and fixed law. Survives. |

These are analytical checks of the supplied proof and limiting boundary
cases. No numerical training evidence was used or inferred.

## Required corrections

None. I found no surviving scientific gap that blocks acceptance of the
frozen candidate in its stated scope.

## Optional suggestions

For readability only, the theorem or its proof overview could explicitly
remind the reader that the deterministic replacement and expected-gap bounds
refer to the infinite-width empirical-law learner `f_S`; the existing
definition and lines 1033–1034 already establish this distinction. This is
not a mathematical correction and is not a condition of acceptance.

## Missing inputs, limitations, and completion

No necessary mathematical input is missing. All proof dependencies used by
the new theorem are contained in the frozen dependency document and have
been read and assessed. I did not inspect the unchanged assembled chapter
complement, test destination-link integration, or validate unrelated
established chapter theorems. Those are outside this neutral scientific
assignment. The result remains local, nonquantitative in finite width, and
silent about useful risk reduction and fitting, exactly as stated.

**Review complete.** All requested scientific components and adversarial
boundary cases were assessed. There are no deferred required checks in this
review and no required corrections.
