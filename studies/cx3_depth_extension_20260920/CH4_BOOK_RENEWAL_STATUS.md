# Renewed C-H4 depth proof using the established book

2026-09-20. Author synthesis and scoped mathematical check. This continues
the same C-X3 contract; it is not an established result or a promotion review.

## Outcome

**The substantial-training extension is still unproved, already at three
hidden tanh layers.** The renewed work extends substantial parts of the
book's two reference constructions and isolates two sufficient new lemmas.
Neither lemma has been proved. The completed local C-H3 author package is
unchanged, and no part of the C-X3 contract has been weakened.

The maintained existence results located at the user's request are useful
inputs, not missing all-depth theorems. B.1 gives a global orthogonal-input
flow for two hidden layers; C.4.5.1 proves the opposite-label reference's
fitting and endpoint; C.4.7 constructs its strong nearby-law flow. The new
attempt therefore uses their actual proofs: C.4.7's named source equations
and C.4.6.3's initialized-column deletion.

## What the new deductions establish

The two detailed reports are:

- [CH4_BOOK_SOURCE_EXTENSION.md](CH4_BOOK_SOURCE_EXTENSION.md), SHA-256
  `a22515ab840411f139fbf0695de2e11a3f475ed08504471b10907ed3d48885d2`.
- [CH4_BOOK_CAVITY_EXTENSION.md](CH4_BOOK_CAVITY_EXTENSION.md), SHA-256
  `61d19b82426e8a33caa83649a853bb6f3796ed1b42332c4b2e0910316a4e9a40`.

The source report derives the complete middle response equations, including
the current transpose-return coefficient. In its notation the new multiplier
is

    M = phi''(z2) q2 + beta3_current phi'(z2)^2.

Keeping only the first summand would omit an actual reused-matrix response.
Temporary response caps give explicit mesh-independent bounds, but their
absolute-value bootstrap cannot close over feature horizons S>=1. That
calculation disproves this particular bootstrap, not the desired theorem.

The report also proves a sign fact along the actual local reference. At the
first nonzero order the middle multiplier has both signs with positive
probability. After folding the labels, its expected current coefficient is
strictly negative, while the first past-source coefficients are positive.
This favorable averaged onset does not prove a bound for the later causal
response: the response pulse is correlated with the multiplier.

A focused follow-up also checked the possible use of Gram positivity. The
positive output Gram controls loss decay, but the parameter Hessian includes
residual-weighted output Hessians as well as its positive Gram part. The
middle response needs an estimate on M times its actual adapted pulse, not
on E[M] alone. At onset the folded M has a nondegenerate conditional Gaussian
component. For any finite C, the bounded test v=1_{folded M>C} therefore has
E[folded M v^2]>C E[v^2]. Thus there is no universal dissipative multiplication
bound from the negative mean. This test does not rule out a special estimate
for the actual causal pulses; such an estimate is still a possible proof route.

The cavity report proves, for actual finite GF at every fixed depth and
physical horizon, uniform Gaussian moment bounds for the independent
deleted-column probe and a pointwise bound on the learned-column memory.
The actual random finite readout is retained. All hidden matrices remain
trainable, and no actual adjoint is replaced by an independent action.

The remaining dependence error is quantitative. For U=c phi'(z_L), let
U^(i) be the fully trained trajectory after deleting initialized column i
of the top hidden matrix, and put

    S_(n,i) = sup_(t<=T,u in S1) ||U(t,u)-U^(i)(t,u)||_Euclidean.

On the initialization event E_n specified in that report, with probability
tending to one, the actual top incoming coordinate is bounded by

    sup_(t,u)|P_(L-1),i(t,u)| <= Z_i^# + 10 S_(n,i) + 4 T C_T^2,
    ||1_(E_n) Z_i^#||_Lp <= C_Z,T sqrt(p).

The important norm in S_(n,i) is Euclidean, not normalized RMS. A raw RMS
bound would lose sqrt(n) and would not suffice.

## Two precise sufficient lemmas, both open

**Source version.** For the orthogonal three-layer reference clock-Euler
programs through feature time S0=1/m3, prove a uniform bound on the row sums
of the top responses beta3, with constants independent of mesh cardinality.
Here m3=q3/2 and q_l=E[tanh(sqrt(q_(l-1))G)^2], q0=1. Section 5 of the
source report proves that this one bound would construct the unique strong
reference through S0, hence for all physical times, with a strong learned
endpoint. This statement does not assume a reference path through S0.

**Finite-GF version.** At L=3 and a prescribed physical horizon T, prove

    ||1_(E_n) S_(n,i)||_Lp <= K_T p,  p>=2,

uniformly in n and i. Sections 3–4 of the cavity report show that this would
give exponential tails of the actual middle incoming field and construct
the unique strong orthogonal reference through T, together with actual
finite-GF convergence. The construction compares fixed-mesh finite Euler
paths to actual finite GF first, and only then takes width to infinity.
It does not assume uniform Euler source caps or an existing population flow.

These are alternative sufficient certificates. Neither is asserted necessary,
and neither is silently substituted for a proved hypothesis.

If the finite-GF certificate were proved through T=20, the existing fitting
identity and q3>=1/10 would give reference loss at most exp(-4). This is the
same conditional fitting implication as before. No new unconditional fitting
claim follows from the renewed reports.

## Why the two-layer argument has not yet closed either lemma

The exact three-layer backward subtraction contains

    [phi'(z2)-phi'(z2_bar)] P2_bar.

The book's bottom clock removes the corresponding first-layer gate. It does
not remove this middle-layer factor: z2'=K2' h1+A2 h1' includes a moving-input
term without a phi'(z2) factor. Dividing by that gate is not a justified
second copy of the first-layer clock argument.

For source pulses the same issue is the product phi''(z2) q2 delta_z2.
An initially independent Gaussian pulse becomes correlated with q2 under the
reused actions. Separate L2 bounds on the two factors do not bound its L2
norm. In a column-deletion comparison the cutoff tail is multiplied by
sqrt(n), so the ordinary raw-distance estimate does not establish the
required susceptibility. Neither primal energy nor the independent probe
bound discharges this step.

Even a completed reference certificate would leave the positive supported-law
radius, all nearby Borel laws, long-horizon raw-GD and autonomous hierarchy
claims to prove. The finite-GF route in particular makes no raw-GD claim.
Early all-layer activity remains available from the local author result.

## Checks, independence, and preservation

The supervisor read the complete 522-line source report and checked its
normalizations, both current and past terms in the middle response, the
temporary-cap inequalities, the conditional construction, and the onset
Gaussian conditioning and signs. No missing term or invalid inference was
found within those stated partial claims. In particular, a negative expected
multiplier was not treated as a dissipative propagator estimate. The source
author received the supervisor's suggestion to test folded-label signs; this
is disclosed author collaboration, not an independent sign discovery.

The source author separately checked the supervisor's complete cavity report
against the assigned book proof. Its check is recorded in
[CH4_BOOK_CAVITY_CHECK.md](CH4_BOOK_CAVITY_CHECK.md), SHA-256
`25b831b4b8e5b2ebdc7d1d8c2af15028a75cd71df92fe1c0ddc26eccdac0a237`.
The conditional implication passed that check. The report supplies explicit
mesh-uniform Euler bounds and the fixed-mesh empirical-feedback proxy
induction, and verifies the tail-transfer order. The supervisor read that
complete check. This is an internal scoped check, not a fresh complete review
of C-X3 or of all maintained dependencies.

No numerical experiment or finite training run was used in this renewal.
The reasoning checks do not validate the unproved certificates. Existing
local implementation tests were not rerun because their files and claims
were unchanged.

CONTRACT.md remains at
`ab0b818cc82ac709f32f44e26d2760d79c153dad6a631b48e62a12015018ca6b`.
The earlier CH4_PROOF_STATUS.md and CH4_CHECK.md remain unchanged at their
previous hashes; this report adds the new deductions without rewriting that
frozen check history. Maintained scientific sources and shared instructions
retain the hashes listed in README.md. No other study was a scientific input.

No Git mutation was performed by this task. During concurrent work the shared
HEAD advanced from the study's opening commit to
`80c5e50fadbe56063c25be12eb7a9b02ad0e9b3f`; the assigned maintained-source
hashes stayed unchanged, and both tracked and index diffs were empty at the
renewal check. The unrelated writer's work was preserved.
