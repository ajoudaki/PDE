# Generic first Stieltjes correction: evidence ledger

This ledger uses the status vocabulary in the repository's conjecture
investigation protocol.  It is subordinate to `PROOF_CONTRACT.md`.

## C-1: feature/loss coordinate identity

- **Statement:** In the one-sample scalar channel, if the formal feature jet is
  odd and \(A=F'(0)>0\), then
  \(K(y)=F'(F^{-1}(y))=A+\mu_0y^2+O(y^4)\) with
  \(\mu_0=F'''(0)/(2A^2)\).
- **Rung:** Exact formal identity.
- **Status:** Proved.
- **Evidence:** Formal series inversion in the maintained Stieltjes master.
- **Open dependency:** Identification with a positive-time deterministic
  neural trajectory is not needed for the fixed coefficient and remains open.

## C-2: first feature-dependent loss order

- **Statement:** With label one and the project's squared-loss normalization,
  the linear and quadratic loss jets equal the frozen-NTK jets; the first term
  involving \(C=F'''(0)\) is cubic in physical time.
- **Rung:** Exact formal identity once \(A,C\) exist.
- **Status:** Proved from the finite-width loss generator.  The required
  moment/UI passage is theorem-covered under polynomial smoothness and under
  the bounded pseudo-Lipschitz tier recorded in
  `PROBABILISTIC_BRIDGE_AUDIT.md`.
- **Evidence:** `AUDIT_REPORT.md`, equations (3.1)--(3.8), including the
  otherwise easily missed `112 K_n J_n` term.
- **Falsifier:** A complete finite-width third loss derivative with an additional
  leading contraction not represented by \(A,C\).

## C-3: generic-activation NTK coefficient

- **Statement:** For the frozen base model,
  \[
  A=q_2+q_1d_2+q_0d_1d_2,
  \]
  where \(q_1=\mathbb E\phi(U)^2\),
  \(d_1=\mathbb E\phi'(U)^2\), \(U\sim N(0,q_0)\), and
  \(q_2,d_2\) are the analogous moments under \(N(0,q_1)\).
- **Rung:** Mean-field identity under the maintained backward-kernel assumptions.
- **Status:** Exact under named assumptions.
- **Evidence:** Maintained generic-activation NTK/backward-kernel calculation.
- **Audit:** Quadratic substitution gives \(27+36+48=111\).

## C-4: explicit Gaussian normal form for \(C\)

- **Statement:** The base-model coefficient
  \(C=\lim_n\mathbb E[D_n^3f_n]\) equals a fully explicit finite Gaussian
  normal form satisfying the proof contract.
- **Rung:** Exact coefficient construction plus mean-field identification.
- **Status:** Proved and audited under the polynomially-smooth activation
  envelope; almost-sure but annealed-conditional under the weaker assumption
  controlling only derivatives through order three.
- **Strongest result:** `L2_B1_GAUSSIAN_NORMAL_FORM.md` gives
  \(C=4H_\star+2S_\star\) as a polynomial in exactly seventeen literal
  one-dimensional Gaussian atoms through \(\phi'''\).  The independently
  grouped derivation gives \(C=4\mathcal H_\star+6\mathcal T_\star\) and
  canonicalizes atom-for-atom to the same expression.
- **Passed gates:** finite-width product rules and metric factors; literal GNF;
  independent atom canonicalization; constant, linear, affine, quadratic,
  sine, and tanh regressions; direct loss conversion.
- **Probabilistic evidence:** `PEELING_AND_PROBABILITY_LEDGER.md` encodes
  \(C_n\) as one exact NETSOR\({}^\top+\)/Tensor Program.  Tensor Programs III,
  Theorem E.15 proves the joint Gaussian/response and deterministic
  covariance-replacement limit; Non-Gaussian Tensor Programs, Theorem 3.7
  proves almost-sure and every-finite-\(L^p\) convergence under polynomial
  smoothness.  Only the weaker finite-order regularity tier retains the
  explicit UI condition (8.3) of that ledger.
- **Falsifier for the current witness:** Failure to reproduce the accepted
  quadratic value or a surviving term outside the declared normal-form grammar.

## C-5: generic Stieltjes positivity

- **Statement:** \(\mu_0\ge0\) for every admissible generic activation.
- **Rung:** Sign theorem.
- **Status:** Refuted.  The sine activation is polynomially smooth, so the
  probabilistic theorem applies to the audited negative coefficient.
- **Counterexample:** For \(q_0=1\) and the smooth bounded activation
  \(\phi(x)=\sin x\), exact Gaussian Fourier evaluation gives
  \(A=1\) and \(C=-1.88699982730593\ldots\), hence
  \(\mu_0<0\).  Independent finite-width simulations agree.
- **Consequence:** For generic activations the coefficient is a first
  nonlinear feature correction, not automatically a Stieltjes moment.

## C-6: batch and depth extensions

- **Statement:** The accepted base state extends first to fixed batch and then
  to fixed arbitrary depth, with an explicit normal-form DAG and no hidden
  response variables.
- **Rung:** Finite construction and closure theorem.
- **Status:** Proved for this fixed order-three directional observable.  The
  two-hidden-layer extension to every separately fixed \(B\) is proved:
  `b2/FIXED_BATCH_EXTENSION.md` gives the explicit \(O(B^4)\)
  Gaussian-normal-form DAG.  At arbitrary separately fixed \(H,B\),
  `depth/DEPTH_FIXED_BATCH_GAUSSIAN_RECURSION.md` gives an explicit
  compact Gaussian DAG with \(O(B^2)\) retained state per layer; its hostile
  audit accepts all responses, the probability bridge, and the loss map.
- **Passed gates:** two independently derived joint recursions; exact
  reductions to both accepted axes; a nondegenerate nonlinear \(H=3,B=2\)
  rational contraction; independent finite-width extrapolation; deep-linear,
  singular-Gram, inactive-channel, and parity controls.
- **Boundary:** This does not prove closure for the general MFP grammar,
  \(H=H(n)\), \(B=B(n)\), polynomial flat-expansion complexity, or positive
  training time.

## C-7: arbitrary scalar label at \(B=1\)

- **Statement:** Replacing label one by a fixed scalar \(y_\star\) requires no
  new GNF atoms.  Under the same theorem-covered moment/UI passage, the first
  feature-dependent loss coefficient is
  \(-\frac83\eta^3y_\star^4C\,t^3\).
- **Rung:** Exact finite-width loss algebra plus the accepted base coefficient.
- **Status:** Proved under the same activation tiers as C-4.
- **Evidence:** Substitute \(r_n=y_\star-f_n\) in the exact generator
  calculation before taking the width limit.

## C-8: arbitrary-label local MSE coefficient at fixed batch

- **Statement:** For any separately fixed hidden depth \(H\), batch size \(B\),
  fixed deterministic labels \(y\), and deterministic PSD input Gram, the
  first feature-dependent term in the annealed local MSE jet is
  \(-\frac83\eta^3 C_{H,y/B}t^3\), with \(C_{H,y/B}\) given by the explicit
  fixed-depth/fixed-batch Gaussian normal form.
- **Rung:** Exact finite-width loss identity, complete response peel, and
  fixed-program probability theorem.
- **Status:** Proved under polynomial smoothness; almost-sure but
  annealed-conditional under the weaker finite-order pseudo-Lipschitz tier.
- **Evidence:** `b2/B2_FINITE_WIDTH_AUDIT.md`, Section 9, encodes the two
  additional cubic response scalars, proves their frozen-channel readout
  parity, and passes four independent full raw-coordinate MSE third-jet
  checks.  `b2/FIXED_BATCH_EXTENSION.md`, Section 8, gives the limiting loss
  formula at \(H=2\).
  `depth/DEPTH_FIXED_BATCH_GAUSSIAN_RECURSION.md`, Section 11, gives its
  arbitrary-fixed-\(H\) extension, and
  `depth/DEPTH_FIXED_BATCH_HOSTILE_AUDIT.md`, Sections 6--7,
  independently checks the tensor-program and parity/Hölder bridges.
- **Qualification:** \(C_{H,c}\) alone is not the exact finite-width
  arbitrary-label loss jet; the response cancellation is a proved wide-limit
  statement.
