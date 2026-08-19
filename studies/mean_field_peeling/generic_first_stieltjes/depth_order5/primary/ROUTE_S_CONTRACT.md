# Route S contract: fixed-depth order-five Gaussian normal forms

## Canonical target

For one deterministic input `x`, `Q0 = ||x||^2/d0`, common hidden width
`n`, and `H >= 2` hidden layers, the model is

\[
u^1_j={w_j^T x\over\sqrt{d_0}},\qquad h^\ell=\phi(u^\ell),
\qquad u^\ell={W^\ell h^{\ell-1}\over\sqrt n}
\quad(2\leq\ell\leq H),
\]
\[
f_n={1\over n}a^T h^H,
\qquad D_n=n\nabla f_n\mathbin\cdot\nabla,
\qquad F_H^{(k)}(0)=\lim_{n\to\infty}\mathbb E[D_n^k f_n].
\]

All entries of `w,W^2,...,W^H,a` are mutually independent standard
Gaussians at initialization.  Every parameter appearing above is trained and
the input is fixed.  The limit is width first, at fixed depth and fixed
derivative order.

Define `Q^0=Q0` and recursively

\[
Q^\ell=\mathbb E_{G\sim N(0,Q^{\ell-1})}[\phi(G)^2].
\]

The admissible activation has enough classical derivatives and Gaussian
moments to justify every displayed order-five contraction; theorem-level
uniform-integrability hypotheses are a separate proof obligation and must be
stated in the report rather than silently assumed.

## Required construction and observable

Route S must produce, for `H=3,4`, terminal deterministic arithmetic DAGs for

\[
A_H=F_H'(0),\qquad B_H=F_H^{(3)}(0),\qquad C_H=F_H^{(5)}(0),
\]

whose only non-rational leaves are `Q0` and the layer-tagged one-dimensional
moments

\[
L_\ell(\nu)=\mathbb E_{G\sim N(0,Q^{\ell-1})}
 \prod_{r=0}^{5}\phi^{(r)}(G)^{\nu_r}.
\]

The clean unit-Gram quotient imposes `Q^0=...=Q^H=1`, identifies all
`L_ell(nu)` with `M_nu`, and replaces `M_200000` by `1`.  The arbitrary-Gram
artifact must retain layer tags and every explicit `Q0` power.

The required derived quantities are the exact rational expressions

\[
\mu_{0,H}={B_H\over2A_H^2},\qquad
\mu_{1,H}={4B_H^2-A_HC_H\over24A_H^5}.
\]

## Permitted and forbidden methods

Permitted internally: ordinary Taylor jets, exact parameter differentiation,
finite covariance registries, Wick pairing, Gaussian integration by parts,
hash-consed arithmetic DAGs, exact rational arithmetic, and finite-width
regression as a diagnostic.

Forbidden terminal objects: Hermite or polynomial approximation of a generic
activation; unnamed Gaussian variables or covariances; tangent/backward
carriers; pseudoinverses; an instruction to run a recursion in place of the
finite formula.  No coefficient may be fitted from another derivation.

## Independence, freezing, and stopping

This primary route may reuse the previously audited `H=2` deterministic
expression IR, but all new files are confined to `depth_order5/primary/`.
It must not inspect another depth route's formulas until the tagged and unit
`H=3,4` coefficient artifacts and exact-byte hashes are frozen.  Comparison
may then report equality or discrepancies without altering the frozen map.

The hard scope is `H in {3,4}` and derivative order at most five.  The route
stops rather than silently changing representation if exact distributive
canonicalization is infeasible; the factored terminal DAG and the precise
canonicalization obstruction are then the retained result.

## Claim ladder and falsifiers

1. **Exact finite construction:** the chronological jet and every Wick--Stein
   elimination rule are algebraic identities in the typed IR.
2. **Algebraic audit:** parity, maximum derivative five, polynomial controls,
   and frozen-map comparisons pass exactly.
3. **Empirical diagnostic:** a preregistered smooth nonpolynomial finite-width
   regression is consistent with the population coefficient.
4. **Theorem-level limit:** an annealed tensor-program/peeling theorem plus
   verified uniform integrability identifies the algebraic output with the
   stated large-width expectation.

A mismatch with the audited `H=2` map falsifies the compiler witness.  A
polynomial-control mismatch falsifies the emitted formula.  Failure of the
smooth regression is inconclusive if its numerical validity gates fail and
otherwise defeats the population witness over the tested case.  Lack of a
verified expectation-limit bridge leaves rung 4 open without invalidating
the exact algebraic construction.

