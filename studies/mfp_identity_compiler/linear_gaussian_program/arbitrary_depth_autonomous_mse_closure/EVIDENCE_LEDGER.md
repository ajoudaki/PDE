# Evidence ledger: arbitrary-depth autonomous linear-MSE closure

## Current research state

| Category | Contents |
|---|---|
| Established here | Exact finite-width normalization and chain identities at every fixed hidden depth; one deterministic rooted-path operator ODE/counting-measure IDE; exact internal output/kernel/loss identities; local and global well-posedness and exponential loss convergence for that deterministic equation.  Positive-time width identification is rigorous at `L=1,2`. |
| Independently checked | The directional derivative equals the displayed kernel for hidden depths 1 through 5; the rooted source gives `(f(0),K(0))=(0,L+1)` through hidden depth 6; the exact path recurrence reproduces the first five feature derivatives at `L=1,2,3`; the `L=1` reduction is the known hyperbolic closed form. |
| Published support | Chizat--Colombo--Fernandez-Real--Figalli rigorously prove the one-middle-matrix `ell^2` limit and give the same arbitrary-matrix-depth path construction and coefficient dynamics. |
| Important source limitation | The published paper explicitly labels its arbitrary-depth section formal.  The local manuscript previously claimed that its short Wick/Picard sketch filled this gap; the supervisory audit found that it does not. |
| Open | The multi-edge rooted-word variance/action estimates and coefficient-lift lemma needed for positive-time width convergence at `L>=3`; a scalar one-coordinate spectral reduction for `L>=3`; depth-uniform computational cost; all-order Stieltjes positivity; minimality of the path state. |
| Superseded | The idea that the depth-two scalar spectral measure should extend by simply diagonalizing all deep balancedness invariants.  Those sources are noncommuting from hidden depth three onward. |

### C-1: exact normalized finite-width chain

- Statement: after dividing every raw vector or matrix block by `sqrt(n)`,
  the muP full-MSE flow is ordinary gradient flow of the multilinear chain,
  with the endpoint and rank-one matrix equations in (5.4).
- Status: Proved exactly for every finite `n` and `L`.
- Evidence: chain rule and direct differentiation in
  `THEOREM_AND_PROOF.md`, Section 5.
- Falsifier: a missing or extra power of `n` in any block equation.

### C-2: one deterministic rooted-path source

- Statement: fixed Gaussian words converge to orthonormal rooted path
  vectors, and multiplication by each initialized Gaussian matrix acts as
  path creation plus immediate annihilation.
- Status: Lemma target for two or more middle matrices; proved in the
  one-edge case and supported by exact finite-word computations more
  generally.
- Evidence: precise target and proof obligations in `CANONICAL_NOTE.md`,
  Section 6; the archived Wick/free-index sketch in
  `THEOREM_AND_PROOF.md`, Section 8; the
  one-edge version is Proposition 3.3 and Proposition 3.6 of the published
  paper.
- Dependency: iid centered unit-variance Gaussian raw initialization and
  fixed depth before width tends to infinity.
- Falsifier: a fixed pair of distinct colored paths with a nonzero limiting
  Gram entry, or a matrix-action residual with nonvanishing normalized norm.

### C-3: autonomous operator ODE / coordinate IDE

- Statement: equations (3.3)--(3.9) use one fixed block source, two endpoint
  vectors, one trainable Hilbert--Schmidt operator, and one residual; the
  current state determines all future readouts.
- Status: Proved by construction.
- Evidence: gradient identities (6.1)--(6.3) and the coordinate form (3.9).
- Falsifier: any required past state, externally supplied clock, or
  width-dependent list of source moments.

### C-4: positive-time width identification

- Statement: finite-width output, feature kernel, and loss converge in
  probability uniformly on every compact physical-time interval.
- Status: Proved at `L=1,2`; conditional at every fixed `L>=3` on the
  rooted-word and coefficient-lift lemmas in `CANONICAL_NOTE.md`, Sections 6
  and 9.
- Evidence: the energy and dimension-free Picard argument completes the ODE
  stability step once those lemmas are assumed.  The local Section 8 did not
  prove their multi-edge Gaussian combinatorics.
- Falsifier: a finite time horizon and subsequence on which one readout error
  remains separated from zero with positive probability.

### C-5: global loss theorem

- Statement: the deterministic path state exists for all physical time and,
  for every nonzero target, its residual tends exponentially to zero.
- Status: Proved.
- Evidence: dissipation bound (6.5), endpoint balance (7.2), kernel lower
  bound (7.3), and the positive lower bound (7.4).
- Falsifier: finite-time state escape, residual sign change, or a nonzero
  limiting residual.

### C-6: depth checks and relation to the previous theorem

- Statement: `L=1` gives `F(s)=sinh(2s)`; `L=2` is the path representation of
  the already proved scalar spectral IDE; all depths have `K(0)=L+1`.
- Status: Proved for the internal path equation and regression-tested; the
  `L=3` row is not a positive-time width-limit proof.
- Evidence: Section 9 and `test_arbitrary_depth_closure.py`.
- Test result: `4 passed` on 20 August 2026.
- Falsifier: failure of the algebraic directional-derivative or rooted-source
  initialization tests.

### C-7: compression classification

- Statement: the formula has an `O(1)` number of evolving objects and no
  width/order dependence.  The path source is depth-graded and the RHS
  contains `L-1` edge contributions, so constant work in `L` is not proved.
- Status: Proved as a representation statement; uniform-depth compression is
  open.
- Evidence: frozen distinction in `PROTOCOL.md` and block packaging (2.4),
  (3.1)--(3.6).
- Falsifier: hidden dependence on `n`, Taylor order, or stored trajectory
  history.

### C-8: Stieltjes scope

- Statement: the deterministic arbitrary-depth path equation is logically
  independent of all-order Hankel/Stieltjes positivity.  Its positive-time
  network identification at `L>=3` is a separate open bridge.
- Status: Logical separation proved; both the width bridge at `L>=3` and the
  arbitrary-depth Stieltjes conjecture remain open.
- Evidence: `THEOREM_AND_PROOF.md`, Sections 10--11.
- Falsifier: a step in the closure or positive-time proof that assumes a
  Stieltjes representing measure for the output-kernel moments.

## Authoritative external source

- L. Chizat, M. Colombo, X. Fernandez-Real, and A. Figalli, *Infinite-width
  limit of deep linear neural networks*, Communications on Pure and Applied
  Mathematics 77 (2024), 3958--4007,
  <https://doi.org/10.1002/cpa.22200>.  The rigorous main analysis focuses on
  one middle random matrix; Section 6 records the formal arbitrary-depth
  path construction.
