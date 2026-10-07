# Lower-cost Harmonic setup: current research contract

Date: 2026-10-06. The first bounded theoretical round below produced component
lemmas and a conditional label-amplitude construction. The second round is
now complete and internally checked under the user's clarified computational
contract; its current result is [LOCAL_SETUP_RESULT.md](LOCAL_SETUP_RESULT.md).
The local-time construction achieves near-quadratic setup with unchanged
Harmonic error/storage. The initial-label continuation conjecture below is
still open, but is not needed for that result. All claims of a missing complete
initializer below describe the first round, not the current research status.

**Contract clarification.** The user clarified that full physical-time coverage
is permitted when its total cost is close to quadratic and overwhelmingly
smaller than ordinary dense Euler training. The comparison is with
\(n^2T/h\), where \(T\) is physical horizon and \(h\) the Euler step,
not with \(n^2T\) treating physical time as a step count. A step such as
\(h=n^{-1/2}\) is an illustrative baseline, not a newly imposed theorem
assumption. This clarification supersedes the earlier provenance-based
exclusion of all full-horizon dense reconstruction. The component proofs
and their frozen reviews remain valid; exclusions below describe the first
round's then-operative interpretation.

This is a continuation of the user-requested initialization-cost analysis
for the current integrated Harmonic method. The checked RESULT remains
the reference theorem and is not being replaced by provisional routes.

## Target and unchanged contract

Construct a Harmonic model from the initialized dense network, data and
labels with polynomial work in the dense width, ideally near quadratic,
while retaining the original activation class (including unbounded values),
general compatible sphere data, fixed arbitrary depth, original shared
label allowance and feature-Gram qualification. The comparison must cover
the whole input sphere, equal physical training times and fitted limits.
Neither frozen features nor a different training metric is a substitute.

Preserve the current accuracy/storage exponents, including the stronger
original source-tolerance specialization when claimed. Preserve source
approximation, exact initialized additions, paired initialized-matrix images,
coordinate-selection metric identities and autonomous corrected-readout
training, or prove replacements sufficient for the same conclusions.
Any necessary change to these interfaces must be identified explicitly.

No successful result may assume free access to a fitted reference or observed
dense trajectory. Under the clarified contract, a computed reference trajectory
is permitted when its generation, source evaluation and assembly are all
charged and the resulting total work meets the stated near-quadratic target.
Speedup is compared with a specified numerical baseline, not inferred from
calling a dense trajectory computation initialization.

Arithmetic and finite precision remain separate. The full activation class
does not specify an efficient derivative-generation algorithm; any oracle
or backend dependence must remain explicit. A fixed-problem width exponent
is not a uniform bound in growing sample count, dimension or depth.

## Authorized work and source boundary

The user authorized creative theoretical redesign and implementation
analysis. This round contains no numerical training experiment, book
promotion, paper change or Git commit. Ordinary deterministic algebra
checks may be used if needed; a training campaign is not inferred.

Scientific inputs are this integrated study's current RESULT and the
maintained notation/setup. Other studies, their histories and artifacts
are not being imported. The author writes this record and README; scoped
agents write only their assigned flat route notes. RESULT is unchanged
until a complete candidate receives a separate reconstruction.

The required additional canonical-notation skill is inaccessible even
with read-only escalation. The accessible rigorous-math and conjecture
workflows, maintained notation and user's explicit presentation rules are
used; compliance with unread instructions is not claimed.

## Initial evidence and claim boundaries

The current source theorem gives a time strip and sphere tube, hence a
polylogarithmic retained coefficient count at fixed problem parameters.
The finite initial-jet construction is valid but its sufficient order
can be exponential in the ratio of time horizon to strip width.

There is a matching obstruction for a strictly weaker information model:
the bounded strip functions
\[
g_\pm(t)=\pm[\tanh(\pi t/(4r))]^{K+1}
\]
have identical derivatives through order \(K\) at zero. At a distant
time their separation stays order one unless \(K\) is exponential in
the horizon divided by \(r\). This is not a lower bound for the actual
neural initializer, which also knows the initial matrices and vector field.

Neither the current theorem nor this observation proves that polynomial
Harmonic setup is possible or impossible. Efficient coefficient extraction
is the central open implication.

## Bounded route portfolio

This round uses three separately scoped mathematical routes, with synthesis
reserved for the author. Each must produce a precise lemma or construction,
its proof, exact remaining gaps and a status; no route is accepted on a
plausibility argument alone.

| Route | Mechanism and deliverable | Assigned artifact | Current status |
|---|---|---|---|
| Initial-data algebra | Expand in label amplitude about the stationary zero-label initialization | POLYNOMIAL_SETUP_INITIAL_ROUTE.md | Exact hierarchy and local bivariate algebra internally reconstructed; global complex-label continuation open |
| Spectral quadrature | Certify efficient source-coefficient integration from the existing joint holomorphy | POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md | Internally reconstructed after a domain clarification; source-value access remains separate |
| ODE-aware recovery | Quantify trajectory perturbation stability and test global coefficient recovery without a forbidden full rollout | POLYNOMIAL_SETUP_ODE_ROUTE.md | Defect stability and parameter lifting internally reconstructed; permitted source recovery open |

A complete result requires all extraction, propagation, source-rank and
operation-count obligations, not merely one successful component.
The following conclusions distinguish those claim levels explicitly.

## Results of this round

### What was obtained

**Efficient quadrature, conditional on source values.** The explicit positive
Fejer-I/trapezoidal product rule in
[the quadrature note](POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md) preserves the
existing joint mode set, exact initialized-matrix pairing, initialized
additions, source-rank budget and coordinate tolerance. For each fixed
admissible dataset, depth, activation, label size and confidence, at the
existing sufficiently large individual widths, its polynomial-accuracy,
logarithmic-horizon specialization has

\[
N_t=O(\log(en)^{5/2}),\qquad
N_x=O(\log(en)^{3(d-1)/2})\quad(d\ge2).
\]

Here \(N_t\) and \(N_x\) are the time and input-space quadrature counts;
\(N_x=2\) for \(d=1\). The hidden constants may depend on the fixed
parameters just listed. The general rule and its explicit dimension
coefficients appear in equations (11), (16), (22), (24), and (30)--(33)
of that note. No uniform growing-dimension statement is inferred from the
display. Neither the values at these nodes nor their generation time are
free. This improvement by itself leaves the expensive physical-time jet
order of the current initializer intact.

**Better dense perturbation stability and full-parameter lifting.**
[The ODE note](POLYNOMIAL_SETUP_ODE_ROUTE.md) proves a finite-horizon
defect estimate using the negative prediction-error square and the
integrable true residual. At fixed admissible parameters the sufficiently
small integrated defect is amplified by at most
\(\exp(a_0+a_1\sqrt{\log(en)})\), with the two nonnegative coefficients
defined by the explicit layer recurrences in its equations (2)--(3), (7).
Polynomially small defect therefore suffices for source-coordinate accuracy
\(1/n\); exponential-in-horizon precision is unnecessary. Its equation
(16) also lifts the existing compressed comparison to normalized dense
parameter increments. Both are deterministic consequences of the inherited
source/fitting event, not a new probabilistic source theorem. Neither
constructs a permitted initializer or proves a restart theorem.

**An initial-algebra route with a precise missing lemma.**
[The label-amplitude note](POLYNOMIAL_SETUP_INITIAL_ROUTE.md) replaces
\(y\) by \(\zeta y\) during setup and expands at \(\zeta=0\), where
zero readout makes the dense state stationary. Its triangular coefficient
equations and bivariate Taylor computation use only initialized weights,
training data and activation derivatives at initialized preactivations.
They do not propagate a nonlinear dense state through physical training
time. Equations (11)--(20) supply a local complex existence bound,
sufficient time-polynomial degree and polynomial arithmetic count in the
two orders; this is not a convergence theorem at \(\zeta=1\).

The exact conditional implication is:

- A polynomially bounded complex-label tube of width at least
  \(c/\log(en)\) around \([0,1]\) would give polynomial coefficient
  recovery at polynomial target accuracy, for fixed problem parameters.
  That polynomial's degree is not claimed to be an absolute constant
  independent of the tube coefficient \(c\).
- Width at least \(c/\sqrt{\log(en)}\), combined with the quadrature
  lemma above, would give \(n^{2+o(1)}\) non-activation arithmetic for
  the whole setup, at fixed admissible parameters. In this conditional
  calculation all local orders are \(n^{o(1)}\), and the unchanged
  orthogonalization, selection and mixer assembly are also within that
  bound. The dense parameter arrays need \(n^{2+o(1)}\) peak words
  in the materialized execution. Activation derivative generation,
  elementary-function evaluation and finite-precision conditioning retain
  their separate original qualifications.

**Neither required complex-label tube is proved.** These implications
are not current setup-cost guarantees. The source-value procedure must
also preserve the exact paired images, as explicitly verified by the
common finite coefficient operations in Section 4 of the label note.
The unchanged comparison would then preserve the current retained model,
including its \(O(\log(en)^{3d+2})\) storage and original stronger
\(n^{-1+o(1)}\) error specialization. Those are conditional preservation
statements, not replacements of the checked construction.

### Why the remaining step is substantive

The existing source proof controls instantaneous gradient responses along
the physical-time flow. Label differentiation produces a transported
gradient response between two different times. Section 6 of the label
note derives the exact sensitivity/deficit equations and identifies the
missing coordinatewise estimate, uniform on a stopped complex-label slab.
Real-label fitting and complex-time analyticity alone do not establish it.
The available worst-case variational amplification does not yield a wide
enough complex-label tube for the desired polynomial continuation.

A prefix of length \(O((m/\gamma)\log\log(en))\) would make the
remaining residual inverse-polylogarithmic, while being a vanishing fraction
of the \(O((m/\gamma)\log(en))\) source horizon. Recentring labels at
that trained anchor gives another stationary-amplitude problem. This is
an exact candidate, but not a proved efficient construction: generic
parameter-to-coordinate conversion loses \(\sqrt n\), and a new
cavity comparison must account for the trained anchor and its
network-dependent centered labels. A short physical horizon is not itself
a complete arithmetic cost certificate.

Two alternatives were excluded from the claimed answer rather than hidden
inside setup: solving a simultaneous dense coefficient system over the
whole horizon, and regenerating dense ODE jets at every local window.
The former computes the complete dense path; the latter performs the core
work of a high-order dense continuation. Neither meets the clarified
computational restriction merely by changing its representation.

No lower bound on permissible initialization algorithms for this network
class was established. The generic finite-time-jet obstruction above is
strictly weaker and must not be promoted to such a lower bound.

## Evidence and preservation

The root read the three complete candidate notes and reconstructed their
core algebra. Separate scoped cross-route checks were commissioned; these
are internal mathematical checks, not independent promotion reviews or a
re-audit of the entire inherited source theorem.

- [Quadrature check](POLYNOMIAL_SETUP_QUADRATURE_CHECK.md): positive rule,
  exactness, joint domain, error allocations, paired sources, ranks, time,
  peak memory and width exponents. Its sole required correction made the
  inherited \(T\ge T_0\), \(0<\eta\le\eta_0\) domain explicit.
  The final-hash addendum verifies that correction and the explicit-log
  presentation changes.
- [ODE check](POLYNOMIAL_SETUP_ODE_CHECK.md): normalization, one-endpoint
  estimates, defect bootstrap, source-coordinate precision and full-state
  lift. A layer-count notation collision was corrected and the exact
  revised hash rechecked. No unresolved must-fix mathematical defect was
  identified in these conditional component lemmas.
- [Initial-algebra check](POLYNOMIAL_SETUP_INITIAL_CHECK.md): triangular
  hierarchy, exponential-polynomial class, local complex ball, bivariate
  cutoff, conservative arithmetic count, exact pairing and transported
  sensitivity identities. No must-fix mathematical defect was identified;
  the complex-label tube and complete initializer remain explicitly open.

Final candidate hashes for the three completed checks:

| Candidate | SHA-256 |
|---|---|
| POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md | `2d58da5a418f6d5a8f1bb54ce343b205978770424c0940789b15231e251daf42` |
| POLYNOMIAL_SETUP_ODE_ROUTE.md | `46e9c2b4ed9f118b3812ce8208d26ebbfa9c9f1fb3efc6e68f3854e0be8cf5a6` |
| POLYNOMIAL_SETUP_INITIAL_ROUTE.md | `6cae513b17db1930326b13c381b6aacefa4ad2144ba41b2ae4ac9b8454d82f3f` |

The source `RESULT.md` remains unchanged at SHA-256
`c2cbd1bb0e6a39de87181df89be977eaf2e272fda4f1459ac934396d84e1b278`.
No training rollout, timing experiment, finite-precision implementation,
book promotion, paper modification or Git mutation was performed in this
research round. The new notes and README update remain uncommitted.
The study-scoped tracked diff passed `git diff --check`; a separate
trailing-whitespace scan covered the new notes. No Markdown/TeX rendering
or numerical validation is claimed.
