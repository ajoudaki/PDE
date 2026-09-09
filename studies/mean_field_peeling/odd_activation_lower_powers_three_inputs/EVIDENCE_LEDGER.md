# Lower-power and three-input evidence ledger

2026-09-07. Complete two-input exponent-two proof assembled and subjected
to three fresh independent full-proof audits. Their final reports are
linked from REVIEW_STATUS.md. The generic three-input odd-mixture theorem
remains open.

| Claim | Current status | Evidence / remaining resolver |
|---|---|---|
| Full two-input theorem for c_poly delta^4 | Previously proved; unchanged | Prior power4 mathematical files |
| Weighted raw discrepancy is O(e lambda^-1 w(t)^3), hence O(e M7) | Complete derived lemma | SECTOR_RESPONSE.md §2; exact two-time affine propagator |
| Weighted FL/RF products and enlarged sector boxes give typed closure | Complete derived lemma | WEIGHTED_AFFINE_AND_CLOSURE.md §§1–5 |
| Sector Gaussian scales give incoming subGaussian powers 10,9,7 | Complete derived lemma | SECTOR_RESPONSE.md §4; actual primal/source covariance bounds |
| Random sector mixing yields the stated forcing table under e H200 M16 <=1 | Proved | SECTOR_RESPONSE.md §§5–8; exact two-sector response and full-proof audits |
| Full two-input theorem for c_poly delta^3 | Proved as a consequence of delta² | TWO_INPUT_PROOF.md |
| Full two-input theorem for c_poly delta^2 | Proved | Largest cost M16, exact unchanged-prefactor arithmetic; full original bridges retained |
| Three-input initial nonlinear Gram is uniformly positive, including singular input Grams | Proved initialization statement | THREE_INPUT_ANALYSIS.md §1; cubic lifting and Hermite projection |
| Worst-case first-feature Gram is Theta(e²delta²) for d>=2, delta<=1/4 | Existing result, scoped correctly | Original THREE_INPUT_GEOMETRY.md; initial independent review corrected omitted range |
| Pairwise absolute separation forces invertible input Gram | False | Equilateral planar triple |
| Equilateral affine population trajectory with equal labels is stationary | Proved | THREE_INPUT_ANALYSIS.md §2 |
| Fitting the equilateral triple requires R >= (pi e)^(-1/3)-11 | Proved algebraic lower bound | THREE_INPUT_ANALYSIS.md §3; three-input and full-proof audits |
| Symmetric scalar ascent has monotone J/||C|| and clock O(e^-2) | Proved conditional lemma | THREE_INPUT_ANALYSIS.md §4; strong existence and chain rule remain assumptions |
| Complete generic three-input odd-mixture theorem | Open | Uniform source tails/strong continuation and trained-law nondegeneracy are missing |
| Optimal exponent or practical universal prefactor | Open | No necessity or optimality claim |

## Route registry and scope

The response route and root independently obtained the weighted primal
estimate. The closure route retained time-dependent Gaussian probe costs
and causal kernel weights, then separated the four forcing types and
sample sectors. The response route retained deterministic sectors while
allowing every individual random gate to mix them. Source paths that
leave and return to a sector contain two perturbative factors. This is
the mechanism used by the candidate.

A provisional scalar enlarged-gain domination was abandoned: a scalar
gain does not entrywise dominate off-diagonal random sector gates. No
final claim uses that step. The exact two-sector causal majorant replaces
it.

The three-input route investigated the initial Gram, affine cancellation,
nonlinear scalar-clock comparison, and energy-preserving regularization.
It produced the quantitative displacement/time bounds and conditional
scalar lemma, but no complete generic strong-source construction.
The older three-input offset/large-gain theorem addresses a different
activation family and is not substituted for this task.

## Adversarial corrections before final freeze

1. The three-input worst-case Theta(e²delta²) statement now includes
   d>=2 and 0<delta<=1/4. The unqualified version would be false at
   delta=1, where the initial input Gram is identity.
2. Nonlinear outer-box strict-density assertions for R1-I and R2-I
   were removed. Arbitrary backward row errors do not carry a past-column
   mesh factor. Only their weighted complete rows are used; forward
   F,V,U strict densities and affine reference products remain valid.
3. Plaintext logarithms now write exp(1) explicitly, distinguishing
   Euler's number from the mixing coefficient e.
4. The equation (6) spacing command in TWO_INPUT_PROOF.md was corrected;
   all final complete reviews identify the corrected main-file hash.

Four mathematical files and 30 dependencies are frozen in their hash
manifests. Fresh reviewers inspected the entire proof and the original
bridges without using historical/sibling review opinions as premises.
The audit is mathematical review, not machine formalization. Neither
optimality of exponent two nor a useful numerical prefactor is claimed.
