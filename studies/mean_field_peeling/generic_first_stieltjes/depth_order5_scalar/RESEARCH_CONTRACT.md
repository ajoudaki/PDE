# Research contract: scalar unit-Gram order-five depth recursion

**Frozen target.**  For the one-sample network and operator
\(D_n=n\nabla f_n\cdot\nabla\), construct a deterministic scalar recursion
for

\[
A_H=F_H'(0),\qquad B_H=F_H^{(3)}(0),\qquad
C_H=F_H^{(5)}(0),
\]

at every separately fixed hidden depth \(H\), in the shared-activation,
unit-forward-Gram regime \(Q^0=\cdots=Q^H=1\).

## Admissible terminal alphabet

The only non-rational leaves are

\[
M_{\nu_0\ldots\nu_5}
=\mathbb E_{G\sim N(0,1)}
  \prod_{r=0}^5\phi^{(r)}(G)^{\nu_r},
\qquad M_{200000}=1,
\]

together with \(d=M_{020000}\),
\(\tau_\ell=\sum_{j=0}^{\ell}d^j\), and deterministic scalar states already
constructed by the displayed recursion.

Every initialization, forward transition, backward transition, and terminal
contraction must be an explicit finite rational-arithmetic expression in
this alphabet.  The state dimension must be independent of \(H\).  We seek
the smallest state found and will not claim mathematical minimality without
a proof.

## Forbidden terminal objects

No final transition may contain an auxiliary Gaussian, multivariate Gaussian
expectation, random tangent/backward variable, covariance or response matrix,
implicit Stein derivative, empirical covariance, pseudoinverse, time
integral, generating-function instruction, unnamed algebraic operator, or
the existing 66-entry response-aware proof IR.  Such objects may appear only
inside the derivation and must be completely Wick--Stein contracted before
the final recurrence is stated.

## Exact limit and claim ladder

Width tends to infinity at each fixed \(H\); no \(H=H(n)\) limit is in
scope.  Claim levels are kept separate:

1. exact finite-width feature-flow identities and readout parity;
2. a formal deterministic scalar contraction of the audited proof IR;
3. exact algebraic agreement with frozen Gaussian-moment maps;
4. empirical finite-width diagnostics;
5. identification with the annealed width limit under explicit regularity
   and uniform-integrability hypotheses.

No fixed positive-time convergence or depth-uniform flat-polynomial-size
claim is included.

## Mandatory exact falsifiers

After freezing a candidate recursion, distribute it in exact rational
arithmetic and compare with the accepted unit-Gram maps:

- \(H=2\): 974 monomials in \(C_H\);
- \(H=3\): 6,519 monomials;
- \(H=4\): 17,641 monomials.

Any nonzero coefficient discrepancy, any terminal derivative above five, or
any forbidden terminal object falsifies the proposed witness.  The same
candidate must recover \(A_H=\tau_H\), the accepted compact order-three
recursion for \(B_H\), finite-width readout parity, constant/affine controls,
the exact linear and quadratic controls, and a preregistered smooth
nonpolynomial finite-width check.

## Completion rule

Promotion requires two independently derived/canonicalized scalar recursions
or one derivation plus an independently frozen exact coefficient-map
canonicalizer, followed by a hostile audit.  If contraction does not close,
the deliverable must instead list the exact surviving deterministic states,
the unresolved branches, passed depth comparisons, and the open claim in the
evidence ledger.  The 66-state Gaussian/response recursion is never accepted
as a substitute.

