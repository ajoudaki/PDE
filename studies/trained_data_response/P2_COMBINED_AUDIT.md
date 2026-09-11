# Independent audit of the conditional combined P2 reduction

Reviewer: `/root/p2_combined_audit`, fresh isolated context, 2026-09-11.

**Verdict: conditional PASS for H ⇒ A–C**, with the precise observation and
limit contracts below. I found no substantive mathematical defect in this
implication. **H remains unproved.** This is neither an unconditional P2
success verdict nor a promotion review. The requested positive-neighborhood
theorem remains open until H, or an alternative sufficient mechanism, is
proved for the specified neural model.

This original report was completed and frozen before receiving another
reviewer's findings. I authored none of the reviewed scientific inputs and
did not inspect prior verdicts, unassigned attempts, histories, other studies,
or study README files. The only README text encountered was the established
reading-guide excerpt embedded in the expressly supplied frozen dependency
packet; no live README was opened. There was no external scientific retrieval,
training experiment, test execution, Git operation, book/code edit, or source
repair. The exact rational certificate in the established proof was read as
part of that proof but was not rerun; its numerical activity constants are
not needed to obtain the conditional compact-horizon implication here.

## 1. Assignment and reviewed conclusion

The assignment was a fresh adversarial check of one conditional reduction,
not an independent proof of H. Permitted scientific inputs were the six
named P2 derivations, frozen P1_SECTION/P1_DEPENDENCIES/P1_MANIFEST,
docs/NOTATION, established global-nonlinear C.4.1–C.4.6 and their complete
invoked dependencies. Writable outputs were this report and
`data/generated/trained_data_response/p2_20260911_02/combined_audit/`.
No new proof search or experiments were authorized by this assignment.

The model is two equal-width tanh hidden layers, no biases, full two-component
first row, Gaussian stored variances `(1,1/n,1/n²)`, mobilities `(n,1,n)`,
unhalved exactly integrated mean-square GF, normalized input `u∈S¹`, bounded
labels `[-Y,Y]`, `Y≥1`, and physical horizon `T=40`. The law metric uses
`|u-v|+|y-z|`. Its diameter is at most `D=2+2Y`. The reference is
`ν*=½δ_(e₁,1)+½δ_(e₂,-1)`.

The raw population state is `(w,K,c)` in row L², middle HS, and readout L²,
with `A=A₀+K`, actual canonical initialized Gaussian action A₀ and its Hilbert
adjoint. Initialization is `(g,0,0)`, `g∼N(0,I₂)`. Finite comparisons use
row Frobenius/√n, middle Frobenius, and readout Euclidean/√n on the same
initialized arrays, including the actual random readout. Only K is HS.

The only extra scientific hypothesis accepted is H in
P2_COMBINED_TAIL_CONTRACT §2: on every smaller positive W₁ ball, all
separately fixed sufficiently fine raw population Euler meshes through 40,
for every finitely supported law in that ball, have a uniform averaged
exponential L² tail for the active backward queries and the readout.
Its constants and mesh threshold may depend on the smaller radius and Y,
but not on the support, weights, Gram rank, or mesh length. H is not a
finite-width moment assumption and does not assume an already constructed
changed-law flow or a nonlinear difference quotient.

For a smaller fixed positive radius, the proved implications are:

| Component | Conditional conclusion checked |
|---|---|
| A | Strong autonomous raw population GF through 40 for every Borel law in the ball; initialized uniqueness and unique restart along reached states. |
| B | A raw law modulus tending to zero, whole-circle prediction continuity, capture of actual finite GF for every fixed Borel law, and arbitrary simultaneous empirical-law/width limits without a relative rate. |
| B observations | Fixed generated raw observations with joint same-layer W₂ laws and quadratic contractions, HS norms/pairings through finite-rank approximation, and both initialized/current action directions. |
| C population | Uniform `o(ε)` raw-state and whole-circle prediction remainder over all contaminating Borel probability laws, with the exact P1 response. |
| C finite | For each fixed contaminating law and positive threshold, the probability of the normalized finite nonlinear remainder exceeding that threshold tends to zero in the order width first, then ε↓0. |

There is no uniform finite-width failure probability over contaminating
laws, no width-uniform finite-n remainder, and no simultaneous ε/width rate.
The last exclusions do not remove the required width-first double limit.

## 2. Exact field, norms, and deterministic estimates

I checked the three gradient blocks directly. For `r=f-y`,

\[
F_\mu=-2\left(\int r\phi'(w\cdot u)Q(u)u\,d\mu,
\int r\delta(u)\otimes H^1(u)\,d\mu,
\int rH^2(u)\,d\mu\right).
\]

The finite representative of `a⊗b` is `abᵀ/n`; its population HS norm is
`||a||₂||b||₂`, and its finite HS norm is the ordinary Frobenius norm.
These factors give precisely the stated mobilities. The loss derivative is
`2∫r df dμ`; pairing its negative gradient with the velocity gives
`L(t)+∫||θ′||²_raw=L(0)`. This uses the square-sum raw Hilbert norm, whereas
the transport estimates use the equivalent sum distance. No squared sum
distance is substituted into the energy identity.

The Euler supremum recurrence `C_(k+1)+Y≤(1+2h_k)(C_k+Y)` gives a law- and
mesh-independent bound through T, even without discrete energy decay.
The rank and row increments then give uniform HS, action, row and speed
bounds. Strong-solution energy and readout bounds are separately legitimate:
scalar prediction is C¹ in raw parameters by III.F.10's weighted remainder
proof; compact data make its gradient continuous uniformly in input.
Differentiating the law integral is therefore justified. Finite Borel-loss
GF is smooth locally, and the energy displacement bound prevents finite
escape at each fixed width. The initial high-probability event is common
to all laws.

The HS upgrade of C.4.1 is valid. All action differences satisfy
`||ΔK||op≤||ΔK||HS`; all middle velocity differences are rank differences
and obey the same two-factor inequality in HS. The only unbounded
coordinate multiplications are split at the reference c and Q cutoffs.
They give **one** factor `1+R`, because the earlier backward error is
transported through a bounded gate/action before a new additive cutoff
error is introduced. Full-row input subtraction and the explicit changed
u factor are both retained. Hence, on a fixed common raw ball,

\[
\|F_\lambda(\theta)-F_\kappa(\bar\theta)\|_{\rm sum}
\le C(1+R)(d+W_1(\lambda,\kappa))+C\tau_{\kappa,R}(\bar\theta).
\]

The learned-transpose formula is a genuine bounded-coordinate rank integral.
It leaves only `A₀*δ` potentially unbounded. This proves the claimed
equivalence of H and the initialized-query tail estimate up to constants
and cutoff rescaling; it does not prove either estimate.

## 3. Strong construction, law completion, and restart

P2_CONTINUATION §4.1 correctly optimizes the cutoff dynamically. With
`s=d+q+V(h+h′)`, H gives `s′≤Ls log(e/s)` while `0<s≤1`, by choosing
`R=1+a⁻¹log(1/s)`. The scalar solution is
`e^(1-exp(-Lt)) s(0)^(exp(-Lt))`. Small initial discrepancy keeps this
below one through T; regularization at zero proves the zero-discrepancy
case. An arbitrarily small positive tail exponent suffices; no unspoken
condition `a>CT` is used.

This estimate makes all fine raw meshes Cauchy in continuous-curve
row-L²/HS/readout-L², also when the finite law varies. Finite law
approximations to any target strictly inside Uρ eventually lie in one
fixed smaller ball. Joint continuity of the field follows from bounded
multiplier continuity, bounded actions, HS rank continuity, and coupling
a fixed continuous Banach-valued integrand on compact data. A compact-time
subsequence argument upgrades field convergence to uniform time convergence
and passes the integral equations. The result is a strong C¹ solution,
not merely a collection of observable limits.

The transfer of tails through changing laws is sound: positive-part norms
are continuous in L², Q depends continuously on raw state uniformly over
the compact input set, and the fixed limiting integrand is continuous in u.
Using `||v 1_(|v|>2R)||₂≤2||(|v|-R)₊||₂` preserves an exponential tail
with a reduced exponent. These are uniform deterministic-parameter
marginal bounds, without any samplewise time/input supremum assertion.

Uniqueness compares an arbitrary competing strong solution against the
constructed tail-controlled solution; only the latter's tails enter.
The competing continuous path has finite raw bounds on its compact
interval. The same zero-error comparison applies after any reached time.
Restarted Euler paths need no fresh Gaussian initialization or new H:
they are compared to the existing continuation, whose tails are known.
Their norms and speeds are bounded directly from the reached state.
Closing its generated spaces under current coordinate operations and both
current action directions contains the Euler constructions and their limit.
Thus restart uses the current raw state/action law and fixed training law,
not stored response history. The claim stops at the constructed horizon.

## 4. Finite GF, arbitrary Borel laws, and observation identification

The finite-width proof uses a finite law ν and a raw mesh h fixed before
the width limit. Expanding K into its finitely many ranks produces a finite
program in A₀ and its actual transpose. III.F.1–7 plus A.1 applies to its
continuous at-most-linear value instructions, including bounded gates times
L² fields. Oracle contractions are replaced in their causal order. A fixed
testing-field cutoff followed by its fixed-program second-moment limit
controls every non-Lipschitz product. The proxy includes the actual finite
initial readout additively; its vanishing RMS and supremum are propagated
at the fixed graph. No readout is reset in the actual GF.

At every fixed cutoff R, the proxy's finitely many node tails have the
uniform exponential population upper bound plus `o_P(1)`. The raw GF/proxy
comparison on a slab of length ℓ has amplification `exp(C(1+R)ℓ)`.
Choosing `Cℓ<a′/2` makes its amplified exponential tail vanish as R→∞.
The continuation proof correctly selects finitely many cutoffs and incoming
accuracy tolerances **backwards** across a finite partition before choosing
one finite ν and one mesh h, and only then sends width and empirical-law
indices to infinity. All fixed-proxy random errors therefore vanish
together. This avoids both a growing-program theorem and an unjustified
whole-horizon `exp(CRT)` comparison against an insufficient tail exponent.

**The proof includes fixed arbitrary Borel-law finite GF.** In the actual
side of this comparison, every field is an exactly integrated Borel loss,
its finite existence/energy bound is independent of support cardinality,
and the transport estimate holds for every Borel law. The sole finite-law
restriction belongs to the chosen comparison proxy ν. Set the actual laws
`λ_j=μ` for any fixed Borel μ; then `W₁(λ_j,ν)=W₁(μ,ν)`, so the identical
ordered comparison proves capture. More generally it works for arbitrary
Borel `λ_j→μ`, and hence for the requested empirical laws. Independent
sampling is handled by the finite Borel-partition proof of empirical W₁
convergence and a union bound with the fixed-proxy initialization events.
No relative sample/width rate is needed.

The current reference comparison defines the admitted fixed observation
contract explicitly: start from finitely many raw w,c and forward/backward
h,z,H,δ,Q fields at specified times/inputs and identified initialized
generated fields; apply finitely many same-layer globally Lipschitz
continuous operations, fixed bounded continuous gates times named L²
fields, and typed A₀,A₀*,A,A*,K,K* actions. Observe joint same-layer W₂
laws and quadratic contractions. Bounded continuous gate operations are
passed by truncating their testing field and restricting their argument
tuple to a compact box; tightness and second-moment uniform integrability
justify removal. This induction applies to the continuation proxies just
as to the fixed reference. It does not admit arbitrary unbounded products
or inverse-gate clocks as starting observations.

For a fixed rank expansion,

\[
\left\|\sum_i a_i\otimes b_i\right\|_{HS}^2
=\sum_{i,j}\langle a_i,a_j\rangle\langle b_i,b_j\rangle.
\]

Joint two-layer Gram contractions therefore identify HS norms and pairings,
and the rank expansion identifies both directions on generated test fields.
The raw approximation extends those conclusions to actual K. There is no
distance between a finite initialized matrix and a population operator on
another carrier. Uniform row/action/readout and speed bounds supply time
and input nets for the whole-circle predictor. This is sufficient for B.

## 5. Probe atoms and the reached moment bound

The new same-mesh estimate in the combined report is essential and correct.
For two laws on the identical raw mesh there is no interpolation defect:
`s_(k+1)≤s_k+h_k Ls_k log(e/s_k)`, `s_0=q`. The scalar velocity is
increasing on `(0,1)`, so its exact flow dominates its explicit Euler step.
Induction with a small fixed q₀ gives `max_k d_k≤Cq^α`,
`α=exp(-LT)>0`, independently of mesh length. The q=0 case is equality
of literal recursions.

For fixed `0<r₀<r₁<ρ`, the law
`λ_η=(1-η)λ+ηδ_(u,0)` belongs to U_(r₁) for every λ∈U_(r₀) when η has
one fixed sufficiently small upper bound. Its W₁ distance from λ is at
most Dη. The readout supremum makes passive Q Lipschitz in raw state,
uniformly in u. The active tail at the inserted atom costs η⁻¹, exactly
as the report records. Therefore

\[
\tau_R(Q_\lambda(u))\le C\eta^\alpha
 +2M\eta^{-1}e^{-aR/2}.
\]

Taking `η=η̄ exp(-aR/[2(1+α)])` yields uniform passive exponential
tails for R≥2. This does not infer off-support control from the original
law's average alone. Strong completion and bounded truncated exponentials
pass the resulting exponential marginal moment to every fixed time/input
of every Borel flow in U_(r₀). The constants are uniform in those parameters.

The radial identity keeps its exact factor four from the unhalved loss:
`d|w|²/dt=-4∫r Q(w·u)φ′(w·u)dμ`. Since
`|z|φ′(z)≤1/2`, it yields
`sup_t |w(t)|²≤|g|²+2R_T J`, where `J=∫₀ᵀ∫|Q|dμ ds` and
`R_T=Y(1+√T)`. Coordinate representatives and this identity follow from
the strong raw equation and Fubini. Jensen uses the probability measure
`T⁻¹ds dμ`: if `λT≤β`, then `E exp(λJ)≤M`. Hölder, without independence
of g and Q, and the two-dimensional Gaussian integral give the stated
`E exp(η sup_t|w|²)≤(1-4η)^(-1/2)M^(1/2)` with its conservative η choice.

This uses **marginal** exponential Q estimates uniformly in time and input,
not a moment of their supremum. The `4pW≤ηW²+4p²/η` estimate and Hölder
then give every separately fixed moment of `cosh²(w_j)Q(t,u)`.
Multiplying by `u_jφ′(w·u)` cannot enlarge it. The third moment therefore
gives the explicit square-tail estimate `C₃/R`, exactly (UI) in
P2_VARIATION. There is no A₀:Lᵖ→Lᵖ premise and no assumption about divided
nonlinear deviations. The optional reached-source `d^(1/3)` modulus also
checks: L²/L⁸ interpolation gives L⁴ differences with exponent 1/3;
the cross-state exponential weight products are controlled by Hölder.

## 6. Uniform response and its finite nonlinear bridge

Under the newly verified UI, the variation proof's transformed curve exists
in clock-L²/HS/readout-L² by the pointwise scalar chain rule and integrable
clock forcing. `F(g_j)∈L²` follows from Gaussian linear-exponential moments.
The reference clock field has a uniform Lipschitz estimate whenever at
least one compared readout is bounded pointwise. In particular the actual
perturbed readout supplies that bound when compared with a linear-response
curve whose tangent readout need only be L².

UI first bounds the contamination forcing, so the clock state difference
is derived to be O(ε). Raw convergence, compact time/input selection and
UI then give strong uniform continuity of that forcing along the perturbed
curves. The reference atom forcing is continuous into the continuous-curve
Hilbert space. Its probability averages lie in the compact closed convex
hull of a compact set; the proof's finite-net argument establishes this
compactness in norm. The bounded linear solution map gives a compact
response family.

Taylor consistency on this compact direction family is legitimate. Scalar
bounded-derivative remainders are split into bounded directions and uniformly
small L² tails. The readout/backward cross term after division by ε is
`b[q(z_new)-q(z)]`: the bracket is bounded and tends to zero in measure;
the compact b family has uniformly integrable squares. The remaining
products are bounded coefficients, scalar pairings, or HS ranks. This is
not an ambient L² Fréchet differentiability claim. Subtracting the linear
response equation and applying the one-bounded-readout Lipschitz comparison
gives uniform `o(ε)` clock and raw remainders, then the whole-circle
prediction remainder.

The P1 response identification is exact. P1's clock differs by the fixed
field F(g) only. Both give `δw_j=φ′(w_*,j)ξ_j`; at ν* the clock equation
is `X′_j=-r_jQ(e_j)`. Differentiation produces the same typed bounded
generator, and the direct signed-law source is precisely P1.T5 with
`σ=ν-ν*`, including factor -2 and signed reference subtraction. Uniqueness
of the bounded linear equation identifies the solutions. The full P1
source and finite-capture proofs retain the actual transpose, column
dependence, finite readout, weighted tails, and whole-circle output nets.
No derivative is moved through a width limit.

Finally choose one positive radius δ inside the construction ball and
`ε₀≤min(1/2,δ/(2D))`. For each fixed ν and ε>0, fixed-Borel capture from
§4 and P1's finite derivative capture apply simultaneously on the same
initialization. If `ω(ε)→0` is the uniform population remainder modulus,
the triangle inequality in P2_RESPONSE_BRIDGE (5) gives

\[
\frac{\|f_{n,\mu_\epsilon}-f_{n,*}-\epsilon D_\sigma f_n\|_\infty}
{\epsilon}
\le\omega(\epsilon)
+\frac{\|f_{n,\mu_\epsilon}-f_{\mu_\epsilon}\|_\infty
+\|f_{n,*}-f_*\|_\infty}{\epsilon}
+\|D_\sigma f_n-\mathscr D_\sigma f\|_\infty.
\]

At fixed ε the random terms vanish as n→∞. For every a>0, take ε small
enough that ω(ε)<a/2. A union bound proves

\[
\lim_{\epsilon\downarrow0}\limsup_{n\to\infty}
\Pr\left\{\epsilon^{-1}
\|f_{n,\mu_\epsilon}-f_{n,*}-\epsilon D_\sigma f_n\|_\infty>a\right\}=0,
\]

for each fixed ν, with the supremum norm over `[0,40]×S¹`. This completes C
in its requested order. There is no claim uniform in ν of the finite
failure probability or a permissible arbitrary ε_n→0.

## 7. Surviving issues and scope cautions

No major or fatal objection survives to the stated conditional implication.
The following are clarifications, not additional scientific hypotheses:

1. The continuation theorem's headline emphasizes empirical-law sequences.
   Its actual-side argument works for exact arbitrary Borel integrals;
   §4 above explicitly supplies the fixed-law specialization needed by C.
2. The combined report's sentence excluding a “finite-width nonlinear
   remainder” must be read as excluding a width-uniform finite-n bound/rate.
   The ordered double limit is proved by the separately supplied response
   bridge and is included in this verdict.
3. The combined report records a historical hash of the reference comparison.
   The current reviewed package uses the corrected files recorded below.
   Their full new text was read, not merely the supervisor's description.
4. The displayed formula for the supremum in combined (9) contains a
   carriage-return/formatting blemish in the word “finite.” It has no
   mathematical consequence.

H is a nontrivial finite-program estimate on a fixed positive neighborhood,
not an oracle assumption encoding the future flow. Nevertheless it is
substantially stronger than norm bounds or closeness to one reference.
The reference column argument cancels a first gate only at e₁,e₂.
For changed laws, `[φ′(w·u)-φ′(w̃·u)]Q̃(u)` remains. Bounded A₀ and bounded
δ give only an L² query estimate, and a fixed positive proximity error
does not vanish with the cutoff. The probe-atom law comparison itself
consumes H, so it cannot bootstrap H from P1. The radial fourth moment
alone likewise does not supply its exponential estimate. Those checks
support the authors' explicit OPEN status; this audit supplies no proof
of H and no counterexample to it.

## 8. Complete read coverage, checks, and frozen inputs

The six P2 files were read completely. P2_REFERENCE_COMPARISON and
P2_RESPONSE_BRIDGE were read again completely after the supervisor supplied
their current clarified versions, before this report was frozen. No other
reviewer's finding was supplied in that notice. P1_SECTION was read in full
(2,062 lines), and its full text equals current C.4.6 exactly. P1_DEPENDENCIES
was read completely through its embedded units or byte-identical current
counterparts. Truncated outputs were repaired with smaller overlapping
reads, including the complete III.F.5–6 and the P2 continuation/variation
boundary. No substantive conclusion relies on a truncated proof.

Current global-nonlinear coverage was the C.4 introduction and all C.4.1–6,
lines 3836–8959, plus complete C.2, lines 2924–3440. Frozen A.1–A.4/B.1,
lines 1840–2453 in their original source, were read completely. Complete
finite-dynamics §§1–4 and special-data III.F.1–11 were read from the frozen
dependency packet. Uninvoked book material outside those units was not
used. Cross-checking excerpt occurrence was a content-identity check,
not retrieval of additional scientific inputs.

The metadata check parsed every frozen excerpt and confirmed exact current
matches for NOTATION, finite-dynamics §§1–4, III.F.1–11, A/B.1, and both
frozen C.4 excerpts. The latter begin at current lines 3976 and 5469.
The check and all input hashes are retained in
`data/generated/trained_data_response/p2_20260911_02/combined_audit/input_metadata.json`.
Commands used were bounded text reads, line-number reads, SHA-256 hashing,
and Python exact-substring comparisons. All metadata checks completed
successfully. No empirical claims were reproduced or inferred.

Required process sources read were AGENTS, RESEARCH_WORKFLOW (including its
research/promotion distinction), solve-math-rigorously, investigate-conjectures,
and its research-contract and adversarial-audit references. Their required
proof, claim-level, non-vacuity and adversarial checks were applied.

| Frozen reviewed input | SHA-256 |
|---|---|
| P2_COMBINED_TAIL_CONTRACT.md | `818d2885fa706d6ceae1101afc3cee2e91afea27ec49c431a4d87f6321e3f994` |
| P2_CONTINUATION.md | `fe59ffe02281be549d6d7815d9c3b58bfe9b51545236cbffb9899339838669d2` |
| P2_VARIATION.md | `ef28df6745758adc1c587a4d73442c3a49db575026ac2bee86708a24de44c5fd` |
| P2_REFERENCE_COMPARISON.md, current | `a6d229fd69be98df8bf41fa7fdde9dad55cfcae86799f2c268791dc3e3904c4d` |
| P2_RESPONSE_BRIDGE.md, current | `7a410d6d5e2fc16a07b4a04ab355878d51ec9940a1d52c1ca506b6288d528e89` |
| P2_REACHED_TAILS.md | `837535f363d8140516ed993698f0e48d183dc029fe66cffc1277aff79e328716` |
| P1_SECTION.md | `33c819282d83f7f4704cbd3a90e87b445d17ce161cc922c1ad786b5eb0d9de38` |
| P1_DEPENDENCIES.md | `ca696bc4ed14ea337028eb1e6ef9c7f729ed2a0153bc210de8e16dea18f5ee79` |
| P1_MANIFEST.json | `f9f3ac7dd834429f2afd1b2d819e20cf04da37446311405943332300ca4fa53d` |
| docs/NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| docs/global_nonlinear.md | `3f32122dea7915e25e4abc7abe9d74017d535badfa5abbe1939e84fe2b100bdf` |
| AGENTS.md | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| RESEARCH_WORKFLOW.md | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |

The P1 scientific hashes agree with its manifest. The two corrected root
files are the reviewed inputs; their earlier versions were not used to
override current wording. This report's freeze record is stored alongside
the metadata in the assigned scratch directory, before any inter-review
comparison. Conditional correctness, verification status, and promotion
status remain separate.
