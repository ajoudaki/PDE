# Milestone 2: independent scientific digest and proof audit

Date: 2026-09-11. Scope: the frozen proposed C.4.7 and its complete supplied
proof dependencies. This is a read-only mathematical assessment, with three
supplied deterministic checks, not a new research campaign or a promotion
decision.

The packet supports its stated result: on a positive Wasserstein neighborhood
of the opposite-label reference, the specified two-hidden-layer tanh model has
unique strong population GF through physical time 40, actual finite-GF capture,
and a contamination expansion whose population first-order remainder is uniform
over all contaminating probability laws. I found no remaining logical gap in
these stated conclusions during this audit. This finding is restricted to the
frozen text and exact quantifiers below; it does not certify a statistical or
endpoint theorem beyond them.

## Reading scope and independence

I read all 2,461 lines of `P2_SECTION.md`, all 7,434 lines of
`P2_PROMOTION_DEPENDENCIES.md`, the complete manifest and recipe, and all three
supplied check scripts. The frozen dependency bundle includes the complete
guide/notation, finite dynamics §§1–4, special-data III.F.1–11, global-nonlinear
A.1–A.4 and B.1, C.2, and the complete C.4 introduction through C.4.6.
Two truncated tool outputs were repaired by rereading dependency lines
190–235 and 765–794; all check scripts were subsequently read completely.

Required process reading was the complete `solve-math-rigorously/SKILL.md` and
`investigate-conjectures/SKILL.md`, plus the latter's adversarial-audit,
evidence-ledger and decisive-experiments references. The supervisor's isolated
assignment replaced author startup reading. I did not read the study README,
original drafts, prior reviews/verdicts, other assessments, other studies,
P2B material, Git history, or live canonical scientific files. No agent was
contacted or delegated to. The parent's metadata notice about concurrent live
promotion did not change the frozen scientific input.

The manifest and recipe mention additional edition/build/navigation artifacts.
Those were outside this assignment and were not opened or executed. This audit
does not assess live-edition assembly or promotion-process compliance. External
literature links in the frozen guide were contextual, explicitly not proof
dependencies; no external theorem or literature-priority claim was imported.

## Exact mathematical contract

The model has input dimension two, two equal-width tanh hidden layers, no
biases, independent centered stored Gaussian variances `(1,1/n,1/n²)`, and
mobilities `(n,1,n)` for the unhalved mean-square loss. The actual finite initial
readout is retained. The data domain is
`sqrt(2) S¹ × [-Y,Y]`, `Y≥1`, with distance `|x-x'|/sqrt(2)+|y-y'|`.
Every finite-network Borel-law loss is integrated exactly. The reference is
`ν* = (δ_(sqrt(2)e1,+1)+δ_(sqrt(2)e2,-1))/2`.

The state is the full first row in `L²(Ω1;R²)`, a learned increment in
`HS(H1,H2)`, and the stored readout in `L²(Ω2)`. The initialized action `A0`
is bounded and retains its actual Hilbert adjoint; it is not assumed
Hilbert–Schmidt. The new result is on `[0,40]` and a relative open ball
`U_Y={μ: W1(μ,ν*)<δ_Y}` with `δ_Y>0`. It allows arbitrary atom counts,
arbitrarily small nonzero weights, repeated/correlated inputs, singular Grams,
nonatomic laws, and nondeterministic labels conditional on input. It supplies
no useful numerical lower bound on this radius.

The strong solution is `C¹` in the raw Hilbert norm and obeys the exact energy
identity. Uniqueness compares against any strong raw solution on the same
prescribed carrier and primitives. Tails are proved for the constructed
solution and need not be assumptions on its competitor. Restart means the
unique continuation of a reached state for the same law through the remaining
portion of `[0,40]`; it is not existence from every ambient operator state.

The state width assertion is an approximation statement: fix a finite-law,
finite-mesh oracle at the desired accuracy before sending width to infinity.
Compare its realization to actual GF on the same finite arrays. Identify its
population counterpart through joint node laws and rank contractions. No
finite matrix is subtracted from an operator on another carrier. Admitted
observations are finite correctly typed action/gate programs with joint
same-layer `W2` convergence, including quadratic and paired initial/current
hidden observations. Arbitrary unbounded products are excluded unless given
their own moment proof.

## What is new relative to the supplied dependencies

This is a comparison with the frozen mathematical library, not a claim of
external literature novelty.

1. **Uniform named coefficients for nearby raw Euler programs.** C.2 supplies
   only a short-time absolute cap; C.4.5.2 supplies a fitted-reference anchor.
   C.4.7.3 proves the new cap `N-cap` through 40 for all sufficiently fine
   finite-law raw Euler programs in one positive law neighborhood. The cap
   concerns the sum of absolute named upper-source coefficients for a fresh
   passive query. It is uniform in support size, least mass, mesh length and
   covariance rank. It yields `Q=ζ+J`, with a uniformly bounded Gaussian
   variance and a uniformly bounded remainder, hence passive Gaussian tails.

2. **Transport of source coefficients with their masses intact.** Equations
   `N14` and `N17` retain `h_s p_b` for each old source. The latter bound is
   stronger than a row-sum cap and is necessary in `N27a`: a past-source input
   error is averaged with its own mass, rather than bounded by the worst
   transport displacement. The discrepancy estimate `N24`/`N31` compares the
   same passive output in the two programs and gives causal continuation of
   the cap. This is more than continuity of raw values alone.

3. **Strong nonlinear completion and finite capture through 40.** The raw
   comparison is upgraded to HS increments. Exponential query tails give the
   Osgood inequality `s'≤L s log(e/s)` and its positive Hölder law modulus.
   Finite-law/mesh paths become Cauchy in the full raw state norm. Joint field
   continuity identifies a strong autonomous equation and permits reached
   uniqueness. A finite proxy and an explicit order of cutoffs, laws, meshes
   and widths then capture actual GF, including arbitrary sampling/width
   sequences and exact nonatomic-law training.

4. **Reached inverse-gate control away from the reference.** C.4.7.6 proves
   uniform passive exponential moments, the radial inequality
   `sup_t |w_μ(t)|² ≤ |g|² + 2 R_rad ∫∫|Q_μ|`, and an exponential-square
   moment of the row maximum. These imply every separately fixed finite
   moment of `cosh²(w_μ,j) Q_μ(t,u)` and uniform integrability of squared
   actual clock forcing. This is the nonlinear weighted estimate that a
   reference tangent bound alone would not furnish.

5. **Uniform finite-contamination consistency with the old response.** The
   reached clock equation is exact. Its reference part is Lipschitz whenever
   one compared readout is pointwise bounded. Forcing is uniformly continuous
   along the actual contamination family. Atom forcing curves form a compact
   set, their closed convex hull is compact, and the linear solution operator
   sends it to a compact family of response directions. Taylor estimates on
   that compact family and an integral comparison give the raw and prediction
   `o(ε)` remainders, uniformly over contaminating laws. The generator and
   source are explicitly identified with C.4.6, including the clock shift,
   loss factor two, sign and reference subtraction.

The reference fitting/endpoint certificate, reference all-time homogeneous
propagator, finite-first reference derivative capture, and early hidden-motion
certificate are inherited results. C.4.7 attaches the applicable risk and
paired-motion margins to its newly constructed nearby-law population paths.

## Adversarial checks of the main bridges

**Fresh queries and coefficient caps.** Every old source pulse enters with
`m_p=h_s p_b`. A fresh current forward slot has exactly one direct derivative;
other current inputs do not create an unweighted sum. Repeated and singular
queries remain separate formal arguments. Splitting a reference atom splits
its old coefficients proportionally, while retaining the single current
coefficient. This supplies the common coupling transcript without an inverse
minimum mass. Appending unused queries does not alter earlier fields.

The reference cap is proved for physical-clock Euler with actual residual
feedback. A fresh Gaussian root is inserted into a complete query answer and
all descendants are recomputed. The finite state sensitivity bound passes
through the fixed-graph width limit, then Gaussian integration by parts
extracts the named coefficient, then forcing tends to zero. Complete
fixed-graph source-derivative continuity is supplied, including zero variance.
This does not infer transverse derivatives from a singular unforced value law.

The transfer to raw reference Euler includes the actual scalar clock defect
and its normalized named derivative: `Σ ||∂_p R_h||/m_p≤C_B h_max` (`N36`).
The first cap bootstrap uses only past rows to control this defect; the second
uses the established raw reference cap and weighted transport. Neither
bootstrap assumes the cap of its still-unconstructed current query.

**Weighted transport and Gaussian degeneracy.** The source difference identity
`N21` comes from cross-program Gram covariances on the common carrier. It does
not require Lipschitz dependence of a covariance square root or continuity of
a pseudoinverse at rank loss. The `L12` interpolation used in the lower pulse
comparison has a valid exponent: interpolating `L2` smallness with a uniform
`L24` bound gives `1/11`, which permits the weaker `1/16` on the bounded
distance range. Source errors keep their masses through Hölder, Jensen and
the causal sums. In particular `Σ p_a e_a^(1/16)≤q^(1/16)` is used instead of
`max_a e_a`.

**Singular trained Gram.** The C.4.6 dependency proves `E=S*D`, where `D=R*R`
multiplies the row by `φ'(w_a)²` and is identity on other blocks. Since tanh's
gate is strictly positive at almost every finite coordinate, `D` is injective
although not uniformly bounded below. Thus
`ker Γ=ker S=ker E*` for `Γ=ES=S*DS`, and `ran E⊂ran Γ`. The exact formula
`exp(-2t SE)=I+S Γ+ (exp(-2t Γ)-I)E` follows by its power series. This closes
the nilpotent-zero-mode objection. The endpoint pseudoinverse is of one fixed
finite matrix; no positive spectral gap uniform over nearby laws is claimed.
The actual nonautonomous perturbation of the frozen generator has integrable
operator norm, yielding the bounded reference homogeneous propagator. It is
not merely an estimate of a frozen Hessian.

**Raw Euler versus actual GF.** Raw Euler is a proof approximation with actual
population residuals. It is not equated to transformed Euler. Its crude bounds
use the updates, not a discrete energy law. Population completion removes its
mesh. Finite capture compares actual raw GF to a fixed oracle on the same
arrays, retaining the finite random readout additively. The finite-program
theorem is applied only after all proxy choices are fixed. For the weakened
exponential tails, `NAP` partitions time into intervals with
`Cℓ<a'/2`; backward choice of cutoffs/tolerances then removes the amplified
tail before the finite proxy is selected. This addresses the possible failure
of one global cutoff with a small tail exponent.

**Nonlinear products.** The radial bound uses the exact full-row equation and
`|z| sech²(z)≤1/2`; no favorable input angle or sign of the residual is needed.
Jensen bounds the exponential moment of the integrated query, and
Cauchy–Schwarz combines it with the Gaussian root without independence.
These steps justify the unbounded clock on the reached paths, rather than on
all of `L2`. The reference field's comparison factorization uses its bounded
readout endpoint, so the linear response readout need not be pointwise bounded.
In the Taylor argument the only extra product,
`d[φ'(Z_new)-φ'(Z_*)]`, is handled by uniform square tails of the compact
readout-direction family. No bounded bilinear multiplication map on arbitrary
`L2×L2` is assumed.

I found no surviving objection in these bridges that blocks the theorem as
written. Stronger interpretations listed below remain unsupported; that is a
scope boundary, not a contradiction to the stated theorem.

## Remainder and limit quantifiers that must be preserved

At population level, with `μ_ε,ν=(1-ε)ν*+εν`, the result is

`sup_ν sup_(t≤40,x) |f_μ_ε,ν - f_ν* - ε D_(ν-ν*) f| ≤ ε ω_Y(ε)`,

where `ω_Y(ε)→0` is deterministic and there is an analogous raw-state
remainder. Thus the population contaminating law may vary with ε. The result
does not say `O(ε²)` or provide a numerical rate for the modulus.

At finite width the actual derivative is first defined at each fixed n,
using common initialization. For every separately fixed ν and every a>0,

`lim_(ε↓0) limsup_(n→∞) P( ||f_n,μ_ε - f_n,ν* - ε D_(ν-ν*)f_n||∞ / ε > a ) = 0`.

The proof divides two ordinary prediction-capture errors by ε only while ε is
fixed and positive, and uses C.4.6's finite-first derivative capture. It proves
neither a finite-n remainder uniform in n nor arbitrary simultaneous sequences
`ε_n↓0,n→∞`, nor a supremum over ν of finite failure probabilities.

Separately, for each fixed μ in the neighborhood, prediction consistency holds
uniformly on `[0,40]×sqrt(2)S1` for every deterministic empirical law sequence
converging to μ and every width sequence diverging to infinity. Independent
iid sampling has the corresponding joint-probability conclusion with no
relative sample/width rate. The lack of a relative rate here concerns the
unscaled approximation error; it does not supply a rate after multiplication
by `sqrt(m)` or division by a contamination size.

## Tools available for a later prediction/statistical milestone

| Available now | Exact use and restriction |
|---|---|
| A canonical finite-time trained map `μ→f_μ` on `U_Y` | It is continuous in `W1`, with a positive Hölder modulus, and is attached to the actual finite GF. This permits well-defined comparison of passive predictions and risks on the stated interval. |
| A strong raw trajectory and finite action observations | Learned operators and both orientations remain present. Paired hidden displacement and quadratic contractions are identified; arbitrary nonlinear coordinate products are not automatically admitted. |
| A bounded linear reference response on signed zero-mass measures | C.4.6 supplies the TV-bounded forcing/evolution and actual finite derivative; C.4.7 proves its nonlinear meaning for finite contaminations at ν*. It is a derivative at that reference, not at every μ in `U_Y`. |
| A continuous bounded reference atom-response kernel | Define `I(t,x;z)=D_(δ_z-ν*) f(t,x)`. Linearity and the proved Bochner integrals give `D_(ν-ν*)f=∫I(t,x;z)dν(z)` and `∫I(t,x;z)dν*(z)=0`. This is an exact reference influence representation. It is not an established influence expansion for the nonlinear empirical predictor centered at an arbitrary nearby μ. |
| Uniform contamination-direction compactness and `o(ε)` | These allow population first-order calculations along the specified contamination family, even if ν varies with ε. They do not identify the scale of a generic empirical-law fluctuation in `W1`. |
| Frozen endpoint metric geometry | The reference projector onto `ker E_∞`, and its raw orthogonal-gradient-span interpretation, can diagnose training-preserving tangent directions. The geometry alone assigns neither a nonzero unseen response nor a favorable risk sign. |
| Zero-order sample/width consistency | Predictions, and by bounded-loss/input continuity the corresponding risks, have an unscaled population limit through 40. No quantitative finite-width approximation is provided. |
| Restricted useful-risk and hidden-motion margins | On the binary-label intersection with the old explicit ball, risk at 40 is at most `1/4` and paired squared activity at `1/200` is at least `10^-13`. These do not prove a causal advantage over frozen features or activity at time 40. |

The atom-kernel identity in the table is a direct rewriting of the established
linear response: if `b_z(t)` denotes the atom integrand in C.4.6.T5, then
`I(t,x;z)=ℓ(t,x)∫_0^t U(t,s)[b_z(s)-∫b_(z')(s)dν*(z')]ds`.
Continuity of the atom forcing curves, boundedness of the solution/evaluation
maps, and the finite horizon justify the integrations. No new lemma or
nonlinear differentiability assumption is needed for this representation.

The following remain separate proof obligations:

- Differentiability about an arbitrary nearby law, a uniform derivative field
  on `U_Y`, and differentiability in a topology that controls generic empirical
  fluctuations. The axis cancellation of the reference clock does not give a
  bounded generator for arbitrary nearby laws by itself.
- A von Mises/influence expansion for `f_(μ_S)-f_μ` about a general fixed μ,
  a nonlinear sampling CLT, covariance formula for that actual nonlinear
  estimator, expected-risk expansion, excess-risk bound, or a risk-sign result.
  The linear reference kernel can be studied statistically, but attaching its
  statistics to the trained nonlinear estimator requires an additional bridge.
- Generic sample-scale remainders. Empirical laws of nonatomic μ do not become
  TV-small relative to μ, and are not generally contaminations of ν* with
  vanishing contamination size. A fixed small contamination expansion leaves a
  fixed approximation error as sample size grows. The proved uniform population
  remainder does apply to deliberately chosen vanishing contamination paths;
  this favorable case should not be confused with a general empirical delta
  method.
- Finite-network statistical scaling: to transfer a `sqrt(m)` statement one
  needs finite-width errors negligible at that scale, or a separate theorem for
  their interaction. Ordinary `o_P(1)` capture and the width-first remainder do
  not supply this.
- A nearby-law infinite-time limit, continuous endpoint selection, an endpoint
  derivative, or convergence of the nonautonomous propagator to the frozen
  projector. Uniform boundedness of homogeneous reference propagation does not
  imply convergence of a forced response; off-support forcing need not vanish
  at the fitted endpoint.
- A raw-GD variation theorem through 40, a simultaneous vanishing-step
  contamination expansion, global arbitrary-law fitting, or a useful certified
  law-neighborhood size. These are outside the new theorem.

For a next milestone centered on general empirical prediction selection, the
main mathematical choice is the base law and fluctuation topology. A theorem
at a general μ requires a new differentiability/remainder argument there.
A milestone restricted to the fitted reference can instead start directly
from the atom-response kernel and the now justified contamination expansion.
Either choice must preserve the separate finite-width scaling obligation if
its conclusion concerns actual trained finite networks.

## Deterministic validation and limitations

Only the supplied tangent, rational-reference and radial checks were run, once
each, without code changes, training or parameter sweeps. Their existing
assertions and zero exit status were the decision rule before execution.
All passed under Python 3.10.12, NumPy 1.26.4 and SciPy 1.13.0, with bytecode
disabled, empty `PYTHONPATH`, and one BLAS/OpenMP thread.

- Tangent central-difference errors decreased by approximately four per
  halving, ending at `1.6082636076e-08`; loss-metric error was
  `7.9006801101e-12`; the largest singular-semigroup error was
  `1.5265444420e-14`. The incompatible nilpotent negative control passed.
- The rational certificate returned bounds
  `[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687,
  0.631761866359]` and satisfied all exact rational assertions.
- The radial identity and unhalved-loss dissipation errors were both
  `5.5511151231e-17`, with positive saturation-bound slack at every supplied
  row, retaining nonzero readout, repeated inputs and conflicting labels.

Commands, environment, complete logs, log hashes and results are retained in
`data/generated/trained_data_response/m2_assessment_proof_20260911/`.
These checks verify finite algebra and constant arithmetic; they do not test
the uniform coefficient bootstrap, strong completion, weighted nonlinear
integrability or limit interchanges. Those conclusions depend on the audited
proofs. No live edition builder or manifest-wide promotion runner was used.

## Frozen input integrity

The following SHA-256 hashes were recorded before scientific reading and
matched after validation and report preparation. No scientific input was
modified. The same records are retained in the assigned generated directory.

| Input | SHA-256 before = after |
|---|---|
| `P2_SECTION.md` | `707a7d42eb2e2e58ae92fa2ee8e25343977224fe1307675e7c0c82609b0571f0` |
| `P2_PROMOTION_DEPENDENCIES.md` | `a68aaa0107f4f73cd0df22af8a8f3867b1c76b515c5d0a920ef387ff2d32acd3` |
| `P2_PROMOTION_MANIFEST.json` | `7ad4d1a5479153bc568c67706c1497ed28d5c64acace30ac0f43ef5f8334a73e` |
| `P2_PROMOTION_TANGENT_CHECK.py` | `b0bbbde5f1f024dbb46975b2092d3aa2a79cabd0375f4520c05489f934d3902f` |
| `P2_PROMOTION_REFERENCE_CHECK.py` | `112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e` |
| `P2_PROMOTION_RADIAL_CHECK.py` | `91ef15a16d42063dc210e82055da3a855c4d9e9e6694b90db8b0191f3390998a` |
| `P2_PROMOTION_RECIPE.md` | `1fc72c36d72a574b37a4e095eecf1b7e3506068497a1012f3348928c20a697eb` |
