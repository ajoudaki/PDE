# Evidence ledger: unfrozen-readout depth-three closure

## Current state

| Category | Result |
|---|---|
| Established | Exact finite-width four-cycle equation, trace readouts, self-commutator invariant, and central product reduction. |
| Established | One deterministic six-color pointed Fock source (two circular matrix bulks plus two orthogonal root tails) and one autonomous trace-class perturbation field, equivalently a two-root free-Wishart IDE. |
| Established | Local and global physical-time well-posedness; direct prediction, feature-kernel, residual, and loss readouts. |
| Established | Compact-physical-time convergence in probability by pointed source convergence plus dimension-free Picard stability. |
| Established | Limiting loss tends to zero; the feature path reaches every finite label. |
| Independently checked | The closure gives \((F'(0),F^{(3)}(0),F^{(5)}(0))=(4,160,13888)\). |
| Falsified | Closure by the cyclic spectrum alone, by separate Gram spectra, by commuting MP variables, or by any finite state-universal polynomial word-moment list. |
| Not claimed | A finite-scalar or one-dimensional commuting spectral quadrature; all-order Stieltjes positivity; joint width/long-time uniformity. |

## C-1: exact cyclic lift

- **Statement.**  With the four-cycle matrix \(\mathcal C_n\),
  \(\mathcal C_n'=(\mathcal C_n^*)^3\),
  \(f_n=\operatorname{Tr}(\mathcal C_n^4)/4\), and
  \(K_n=\operatorname{Tr}[\mathcal C_n^3(\mathcal C_n^*)^3]\).
- **Status.** Proved for every finite width.
- **Evidence.** Direct block multiplication and differentiation; numerical
  randomized regression test.
- **Falsifier.** One block, transpose, factor, or trace identity fails.
- **Source.** `THEOREM_AND_PROOF.md`, Section 2.

## C-2: conserved moment map

- **Statement.**
  \(\mathcal C_n^*\mathcal C_n-\mathcal C_n\mathcal C_n^*\) is constant and
  packages all adjacent Gram differences.
- **Status.** Proved exactly.
- **Evidence.** Both Gram derivatives equal
  \(\mathcal C_n^4+(\mathcal C_n^*)^4\); numerical derivative test.
- **Falsifier.** A nonzero derivative at any finite-dimensional state.

## C-3: source law

- **Statement.** Two independent normalized Ginibre matrices and the two
  Gaussian endpoint roots converge in the required pointed sense to the
  six-color free-circular Fock source \(\mathcal C_0\); the two endpoint tail
  colors make their rooted sectors exactly orthogonal.
- **Status.** Proved from joint strong circular convergence and conditional
  Gaussian quadratic/bilinear concentration.
- **Dependencies.** Fixed depth and fixed word degree; finite-fourth-moment
  iid entries; Gaussian roots independent of all matrices.
- **Falsifier.** A fixed rooted word with a limiting Gram entry different from
  the vacuum law, or loss of the uniform source operator-norm bound.
- **Primary external support.** Xiang--Zhang, arXiv:2608.04824, Theorem 3.3.

## C-4: autonomous closure

- **Statement.** Equations (1.1)--(1.2) form a locally Lipschitz,
  restartable ODE on one fixed trace-class ideal and one scalar residual.
- **Status.** Proved.
- **Evidence.** The trace ideal property, rank-four source term, and the
  cubic trace-norm Lipschitz estimate.
- **Falsifier.** The cubic vector field leaves trace class or requires a past
  value not contained in \((Q,e)\).

## C-5: global physical dynamics

- **Statement.** The limiting physical state exists for every finite time and
  its squared residual tends to zero.
- **Status.** Proved.
- **Evidence.** Loss dissipation, the rank-four trace-norm bound, the positive
  central lift, and logistic comparison.
- **Falsifier.** Finite physical-time trace-norm escape or a nonzero limiting
  residual.

## C-6: width-limit identification

- **Statement.** Prediction, feature kernel, and squared loss converge in
  probability uniformly on every compact physical-time interval.
- **Status.** Proved.
- **Evidence.** Fixed Picard iterates are finite-rank rooted-word expressions;
  their Gram data converge by C-3, while dimension-free Picard tails and the
  energy bound remove the truncation.
- **Falsifier.** A compact horizon and subsequence with a readout error bounded
  away from zero with nonvanishing probability.

## C-7: derivative control

- **Statement.** The independently constructed free-Wishart recurrence gives
  \(F'(0)=4\), \(F^{(3)}(0)=160\), and \(F^{(5)}(0)=13888\).
- **Status.** Passed exactly.
- **Evidence.** Exact free-moment calculation and an independent truncated
  free-Wick path regression test.
- **Test result.** `5 passed` in the local closure module, and `9 passed`
  jointly with the prior arbitrary-depth regression module, on 20 August
  2026.
- **Scope.** This is a falsification check, not the positive-time proof.

## C-8: compression boundary

- **Statement.** Ordinary marginal spectra and finite polynomial moment lists
  cannot replace the noncommutative source; one current trace-class spatial
  field is sufficient.
- **Status.** Proved for the stated natural classes.
- **Evidence.** The free-MP commutator has squared trace norm two; equal cyclic
  spectra can have kernels \(4\) and \(25/4\); the output Lie orbit contains
  connected words of every length.
- **Not claimed.** An impossibility theorem against pathological encodings or
  every conceivable analytic transform.
