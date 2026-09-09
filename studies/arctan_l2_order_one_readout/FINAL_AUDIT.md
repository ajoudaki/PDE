# Final audit: nonlinear two-hidden-layer operator IDE

Status: C5 passed, 21 August 2026.

## Decision

The selected activation is

\[
\phi(x)=\arctan x.
\]

For canonical mutually independent initialization

\[
A_{0,i},u_{0,i}\sim N(0,1),\qquad
G_{0,ij}\sim N(0,1/n),
\]

the autonomous pointed-action IDE in `ARCTAN_THEOREM_AND_PROOF.md` is an
exact, globally well-posed, restartable infinite-width description on every
fixed compact physical-time interval.  The finite predictors, tangent
kernels, residuals, and squared losses converge uniformly in probability to
its direct current-state readouts.

## Claim ladder

| Level | Requirement | Verdict | Decisive argument |
|---|---|---|---|
| C0 | exact finite algebra | passed | mixed-metric differentiation, natural coordinate, and finite central-difference regression |
| C1 | immutable source | passed | two-sided finite-program Master Theorem, countable projective completion, Gaussian spectral-norm bound, exact adjoint identity |
| C2 | finite-field autonomous IDE | passed | two current \(L^2\) fields, one trace-class perturbation, one residual, one fixed source |
| C3 | global well-posedness | passed | cutoff Picard, Gaussian-tail cutoff removal, and Osgood uniqueness in the Gaussian-envelope class |
| C4 | width identification | passed | fixed Euler program, dimension-free mesh removal, \(2+\varepsilon\) moment control, square-UI transfer, physical clock |
| C5 | nonlinear conjecture | passed | C0--C4 for the genuinely nonlinear arctangent activation |

## Audit rounds

1. Independent activation routes compared superlinear polynomials, bounded
   smooth activations, residual perturbations, and piecewise-linear choices.
   Arctangent emerged as the best combined contract/convergence target.
2. Hostile routes attacked extreme Gaussian coordinates, adaptive column
   concentration, weak action topologies, transpose reuse, and kink
   crossings.  They rejected several naive arguments but found no canonical
   arctangent counterexample.
3. Dedicated source, exchangeable/cavity, and canonical-counterexample
   routes isolated the central obligation: the shared \(G_0/G_0^*\) action
   and square uniform integrability of \(Q\).  The exchangeable route alone
   retained an unproved low-influence lemma; the finite-program route closed
   the obligation without a two-time response field.
4. Three fresh repair audits separately checked the generated probability
   algebra/source, cutoff and kernel analysis, and the whole theorem.  All
   returned PASS after the initialization was stated unambiguously.
5. A post-selection isolated round rechecked the two decisive dependencies.
   The source audit returned PASS for fixed finite adaptive
   `NETSOR^{T+}` programs and the ordinary projective/GNS operator
   construction.  The kernel audit found that the original direct Hölder
   mesh-removal estimate was invalid because its high-moment constant could
   grow with the number of Euler steps.  It supplied, and the theorem now
   uses, a square-tail-first truncation argument.  A whole-proof audit was
   conditional exactly on these source and tail lemmas; the two dedicated
   audits discharge those conditions.
6. A final clean-room round separately reconstructed the complete proof,
   searched for rare-row/column and vanishing-time counterexamples, and
   audited the strict Markov contract.  All three returned PASS.  In
   particular, increasing numerical rank of the one trace-class field
   (q(t)) was distinguished from adding time-indexed state species, and the
   counterexample route verified that the repaired square-tail estimate
   excludes the concentration mechanism that blocked the quadratic model.

## Material repairs forced by audit

- The layerwise parameter metrics and normalized rank-one convention are now
  explicit.
- The source is a countably generated pair of probability algebras with a
  bounded operator and genuine adjoint, not an ordinary kernel, a fresh
  Gaussian oracle, or an ultralimit chosen after training.
- Singular query Gram matrices are covered by the transpose Master Theorem's
  extended core-set/rewrite result; Moore--Penrose notation is not used as a
  substitute for that theorem.
- The continuous-time step includes explicit dimension-free cutoff
  Lipschitz and Euler estimates.
- Kernel convergence uses convergence of fixed-program
  \((2+\varepsilon)\)-moments and an explicit square-tail inequality; a bare
  \(L^2\) energy bound is not called uniform integrability.
- Mesh removal for the weighted term \(c(r)^2Q^2\) uses the established
  square-tail tightness followed by truncation.  It does not multiply the
  vanishing Euler error by a mesh-dependent high-moment constant.
- Gaussian cutoff removal uses
  \(e^{C_TM}\|A_0-\operatorname{clip}_M A_0\|_2\to0\), so no unproved
  leave-one-out estimate is hidden in the proof.
- The loss variable and residual are distinguished, and no unsupported
  infinite-time interpolation claim is made.

## Claim boundary

The result uses a constant number of field/operator species, not a
finite-dimensional state.  The immutable source is infinite-dimensional and
must be retained on restart.  The theorem is canonical-iid and compact-time;
it does not assert robustness to unrelated deterministic spikes, convergence
in operator norm, uniqueness for arbitrary ambient \(L^2\) data, or
\(e(t)\to0\) as \(t\to\infty\).

Arctangent is not the only viable nonlinear activation.  Tanh and softsign
are credible co-competitors.  It is selected because no audited alternative
combines smoothness, bounded output, globally nonvanishing derivative, and a
polynomial natural coordinate more cleanly.

## Mechanical check

`test_arctan_finite_identities.py` checks the inverse coordinate,
coordinate-transformed flow, normalized rank-one update, nonnegativity of
the finite kernel, and \(f_n'=K_n\) by central differences.
