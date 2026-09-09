# Complete three-input odd-mixture theorem: renewed proof search

2026-09-08. The user asks for a substantially harder attempt to resolve
the full result unconditionally for every admissible three-input
configuration. The target is one 0<theta_delta<=1/2 depending only on
0<delta<=1, with phi(z)=(1-theta_delta)z+theta_delta atan(z) at all three
hidden layers, and every triple of RMS-unit inputs with
|rho_ij|<=1-delta for i!=j and all binary labels. Singular input Grams
are allowed. A single successful witness suffices; an interval of
amplitudes is stronger and not assumed.

Retain the original model, independent Gaussian initialization including
the finite small random readout, raw Hilbert metric, simultaneous raw GD
step n^-2, population action spaces and actual adjoints. The target is
the complete theorem in ../two_sample_odd_activation_theorem/PROOF.md
with three samples: global autonomous strong population GF, uniqueness
against nonsymmetric bounded-primal strong competitors, restart from
reached states, and the full GF/GD population-limit and observable
statements on every fixed finite physical interval. Width convergence
is for each fixed dataset, not a uniform supremum over datasets.

UPDATE: The user's subsequent steering explicitly permits replacing the
identity term by a fixed affine map a z+b, where a,b are absolute constants
independent of delta. The newly authorized principal route is
phi_delta(z)=(1-theta_delta)(a z+b)+theta_delta atan(z), with a=b=1
the first candidate. The original exact odd mixture remains a separate,
stronger target. The user explicitly rejected a delta-dependent overall
gain; the separate gain theorem does not resolve either accepted target.

Constants may depend on delta, theta, the fixed dataset and finite
physical horizon. The activation cannot depend on the horizon, width,
mesh or clipping level. No delta-dependent affine coefficients or gain, different metric,
frozen hidden weights, reduced depth, additional input spectral gap, or
conditional existence/tail premise may substitute for the target.
Fitting-based reference arguments must prove their own fitting and
source hypotheses. Initialization positivity or a bound conditional on
an already existing strong flow is not a complete resolution.

Authoritative starting boundaries are the corrected three-input note
in ../odd_activation_lower_powers_three_inputs and the later partial
investigation in ../three_sample_odd_activation_threshold. The latter's
bounded claims remain valid, but it proves no positive full-theorem
threshold. The separate large-gain candidate is only a possible source
of mathematical mechanisms and does not prove the convex-mixture claim.

Authorized work: sustained theoretical research, primary-literature
verification where useful, local artifacts, independent route search
and fresh adversarial review of a complete candidate. No experiments,
older-proof edits, commits or external messages are required. Existing
workspace changes must be preserved. There is no user-imposed hard
time or token budget. Three independent route workers and root synthesis
are available; adapt routes only after concrete new mathematics.

New mechanisms sought: direct finite-time Gaussian dynamic-limit
construction; same-array Gaussian/nonlinear cancellation and restartable
source bounds; energy-preserving scalar-loss regularization and compact
continuation; reachable-state concentration/one-sided stability. A
complete candidate must be audited through all original limit bridges.
Failure of one mechanism will not be reported as falsity of the theorem.
