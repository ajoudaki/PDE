# Explicit circle functions from the p=1 population closure

## Current scope after the user's clarification

The intended question restricts read-in/readout choices to finite
initialization-based Gaussian/dictionary/derivative operations. The earlier
angular-transport constructions and unrestricted density result below are
mathematically separate results and did not answer that intended question.
The current answer is [INITIALIZATION_CALCULUS.md](INITIALIZATION_CALCULUS.md):
keep w=G, use initialized activation/derivative readouts, and derive exact
convergent circle expansions from Gaussian derivative and product expectations.
It includes a cubic orthogonal readout with zero first-order M response at
p=1,2 and nonzero first-order response at p=3. Its complete persisted-source
check passed after a raw/normalized matrix notation repair; see
[CALCULUS_CHECK.md](CALCULUS_CHECK.md) for the exact hash, source coverage,
equation-by-equation check and limitations. Root owns the corrected derivation
and this README; init_calculus_route owns that internal contributor check.
No training or numerical campaign was authorized or run. The corrected
theoretical answer is complete; no experiment is queued.

Date: 2026-09-21. This is a new, theory-only study of static representation.
The user asked to customize read-in/readout populations and M, using the actual
Gaussian dictionary law, so that the output can be written explicitly.
No training, optimizer comparison, or new numerical experiment is part of this study.

## Model and result

The model is the bias-free, two-hidden-layer tanh population closure with d=2,
p=1, lower dictionary dimension 5, upper dimension 3, and the maintained
ridge-normalized dictionary. The read-in and readout remain arbitrary measurable
population functions, as in the closure state definition. The frozen dictionary
law includes the response term in its reused reverse Gaussian action.

[DERIVATION.md](DERIVATION.md) gives an exact construction. For every positive
odd integer q, fixed 0<b<1 and every real pair (lambda,mu), a customized population
and a rank-one 3-by-5 matrix give

    f(theta) = L(b[lambda cos(q theta) + mu sin(q theta)]),
    L(t) = log(cosh(t))/t,  L(0)=0.

The read-in can have fixed radius, or exactly the ordinary N(0,I_2) marginal.
No added population marks are necessary, and the realization preserves oddness
under simultaneous mark negation. It changes the joint law of the moving
read-in and the frozen dictionary. A further construction gives L(a T(theta))
for any finite odd Fourier polynomial T; rescaling the readout approximates T
arbitrarily closely, with an explicit uniform error bound.

These are representation results, not canonical-initialization or gradient-flow
results. High frequency has a quantified middle-weight cost. The construction
does not prove an advantage over a matched finite dense network, nor a bound on
the population count needed to approximate these expectations.

## Sources, verification, and status

Permitted scientific inputs were the established [p=1 specialization](../../docs/observable_p1.md),
[notation contract](../../docs/NOTATION.md), the finite Gaussian source/reuse
calculus and closure definitions in [global_nonlinear.md](../../docs/global_nonlinear.md),
and Gaussian conditioning/integration identities in [gaussian_calculus.md](../../docs/gaussian_calculus.md).
The Fourier-coefficient proof uses the [NIST cosh product](https://dlmf.nist.gov/4.36.E2)
and supplies its required differentiation and Fourier steps explicitly.
No other study supplied research inputs.

Root authored the derivation and owns this README and DERIVATION.md.
Two fresh scoped mathematical agents checked the population law and scalar
Fourier/readout identities. Their checks are internal collaboration, not a
promotion audit. The retained law check is [CHECK.md](CHECK.md); final source
hashes and read coverage belong there. The complete derivation is the
reproduction procedure: there is no empirical result to reproduce.

Status: exact arguments internally checked, including a complete read of the
frozen derivation, the normalized matrix norm, and the polynomial extension.
No mathematical correction was requested in that final check. The explicit
constructed states have unbounded w-G and hence are not finite-time endpoints
of the canonical bounded-increment flow; their output functions might still
be approximable along other states or trajectories.
The follow-up [CAPACITY.md](CAPACITY.md) proves that this unrestricted p=1
class is uniformly dense in all continuous antipodally odd circle functions.
Consequently p=2 or p=3 cannot add a new uniform-approximation target under
the same permissions. It distinguishes cost, fixed-population and canonical
training comparisons and records a fresh prompt-only mathematical check.
Not promoted to established material. The authorized theoretical task is
complete. Further training or a new comparison would require a separate
experimental design.
