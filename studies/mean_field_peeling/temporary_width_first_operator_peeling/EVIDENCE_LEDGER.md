# Evidence ledger: width-first operator peeling

## C-1: singular Gaussian operator calculus

- **Statement:** A Gaussian expectation along a \(C^k\) positive-semidefinite
  covariance curve is \(C^k\), including at rank changes, and obeys the
  Price/heat differentiation rule.
- **Status:** Proved.
- **Assumptions:** The integrand has the required derivatives with polynomial
  growth.
- **Evidence:** Fourier proof plus cutoff and Gaussian moment domination in
  `OPERATOR_PEELING.md`.

## C-2: regularity of the four-stage Gaussian DAG

- **Statement:** The one- and two-step width-first Gaussian outputs are \(C^3\)
  near zero.
- **Status:** Proved for the displayed Gaussian DAG.
- **Assumptions:** \(\phi\in C^8\), with derivatives through order eight of
  polynomial growth.
- **Dependencies:** C-1 and the chronological Gram construction.

## C-3: cubic operator asymptotic and implicit-radius corollary

- **Statement:** For every \(\varepsilon>0\),
  $$
  |\mathsf F_2(\eta/2)-\mathsf F_1(\eta)|
  \le(|\widehat\kappa_\phi|+\varepsilon)|\eta|^3
  $$
  for all sufficiently small \(|\eta|\), where
  \(\widehat\kappa_\phi\) is the coefficient returned by the finite
  activation-only Gaussian operator-jet compiler.
- **Status:** Proved for the displayed Gaussian DAG, but this is not the
  requested explicit quantitative remainder theorem because its radius is
  chosen from an unspecified continuity modulus.
- **Evidence:** Operator parity, direct first-jet matching, three applications
  of the singular Price calculus, and Taylor's integral identity.
- **Sharpness:** The identity activation has
  \(\Delta(\eta)=3\eta^3+5\eta^5/8\).

## C-3a: compact nine-moment simplification

- **Statement:** The operator coefficient satisfies
  $$
  \widehat\kappa_\phi=\frac{4H_\phi+S_\phi}{16}.
  $$
- **Status:** Proved for the width-first Gaussian DAG.
- **Evidence:** The atom-by-atom Price-jet table in `OPERATOR_PEELING.md`
  proves
  $$
  J_3^{(2)}-8J_3^{(1)}=3S_\phi+12H_\phi.
  $$
- **Independent audit:** `operator_third_jet_audit.py` verifies the terminal
  polynomial identity by exact rational arithmetic; an independent manual
  audit checked every upstream Price and Taylor factor.
- **Why separate:** This was computed directly from the limiting operators;
  no finite-width initialization coefficient or limit interchange was used.

## C-3b: explicit fifth-order activation-envelope remainder

- **Statement:** Construct activation-defined numbers $B_\phi<\infty$ and
  $h_\phi>0$ such that
  $$
  |\mathsf F_2(\eta/2)-\mathsf F_1(\eta)-\widehat\kappa_\phi\eta^3|
  \le B_\phi|\eta|^5
  $$
  for every $|\eta|\le h_\phi$.
- **Status:** Open.
- **Established part:** $C^5$ operator regularity follows under a safe
  weighted $C^{12}$ activation envelope, and Taylor's integral formula would
  give the displayed estimate from explicit fifth-jet majorants.
- **Missing closure:** The current symbols
  $c_j=\sup\|C^{(j)}\|_1$ and $a_{j,s}$ have not been replaced by a completely
  specified chronological table of numerical majorants generated solely from
  the activation envelope.  No explicit rank/validity radius $h_\phi$ has
  been produced.
- **Cheapest resolver:** Instantiate all mixed Bell--Leibniz envelopes through
  the four stages, replace every covariance derivative supremum by the sum of
  preceding-node Price majorants, and use corresponding fourth-derivative
  determinant bounds to choose an explicit rank radius.

## C-4: identification with the trained-network width limit

- **Statement:** At each fixed step size, the finite-width one- and two-step
  annealed outputs converge to the displayed four-stage Gaussian DAG.
- **Status:** Open.  The exact regression algebra is proved, but the
  probability bridge is currently a proof outline even under the strong
  bounded-derivative, linear-growth class.
- **Scope:** This is a pointwise fixed-step dynamic-cavity statement, not a
  width-uniform Taylor statement.
- **Strong-class evidence:** `FIXED_ETA_CAVITY.md` gives exact adaptive Gaussian
  regression, both response cancellations, and the architecture of a
  rank-localized high-moment coupling/LLN argument when
  $\phi',\ldots,\phi^{(8)}$ are bounded and $\phi$ has at most linear growth.
- **Missing proof:** Formally define the stopped stage-indexed coupling;
  preserve all innovations as one correlated Gaussian block; augment the
  induction with the tangent fields whose empirical averages define
  $\rho,\sigma$; prove the circular good-event step by stopping; prove raw
  high moments and exact-versus-stopped bad-event removal; then establish
  uniform integrability of the terminal output.
- **Current bottleneck:** In the second transpose use, the tagged feature
  $h_j^1$ depends on the same column $W_{\cdot j}$ through $\chi_j^0$.  Exact
  two-sided Gaussian regression resolves this and produces a necessary
  cancellation between the raw-action overlaps.  The analogous terminal-row
  cancellation is also recorded in `FIXED_ETA_CAVITY.md`.
- **Remaining extension:** For general polynomial-growth derivatives, supply
  a truncation and width-uniform high-moment bootstrap at each fixed step
  size.  No inverse-Gram moment assumption is permitted; regression is
  localized and uses projectors off the rank-stable event.
- **Algebra audit:** No missing order-one response or learned low-rank term was
  found.  In particular, the initial transpose response vanishes by readout
  parity and no $hK_{11}h^1$ term is present before the second matrix update.
- **Concrete falsifier:** A missing order-one response term or nonconcentrating
  empirical Gram in the exact two-step finite-width recursion.

## Supersession

The earlier claim that C-4 was proved under bounded derivatives and linear
growth is superseded by the hostile audit above.  The earlier claim that the
displayed $B_\phi$ recursion was already noncircular is also superseded: it is
a construction schema until all covariance and mixed-integrand majorants are
explicitly closed.  Width-uniform Taylor control is still unnecessary for the
width-first route, but C-4 and C-3b must both be proved before the requested
trained-network inequality follows.
