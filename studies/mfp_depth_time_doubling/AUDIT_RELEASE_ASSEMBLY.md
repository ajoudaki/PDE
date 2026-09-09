# Post-repair release audit

## Verdict

**PASS.** The assembled theorem in `PROOF.md` is consistent with the three
proved bridges:

1. `WIDTH_DEPTH_TIME.md` identifies the actual finite-width network with
   the inverse-free DAG at each fixed nonzero step;
2. `COMPILER_DEPTH_TIME.md` proves singular-covariance \(C^5\) regularity
   and the explicit activation-envelope fifth-order bound;
3. the repaired fixed bounded-operator construction in
   `CUBIC_DEPTH_TIME.md` proves the compact cubic identity, and receives a
   clean independent pass in `AUDIT_CUBIC_REAUDIT.md`.

The failed finite-list route remains explicitly superseded in
`APPROACH_REGISTRY.md`; no claim in `PROOF.md` depends on it.

## Coefficient and sign

The exact Price compiler first defines

\[
 \kappa_{\phi,L,t}
 =\frac{8\mathcal J^{\mathrm{PJ}}_{3,t,L}
       -\mathcal J^{\mathrm{PJ}}_{3,2t,L}}6.
\]

The fixed operators

\[
 W_{a,0}=I_a+J_a^*,
 \qquad W_{a,0}^*=I_a^*+J_a
\]

then give one compatible population gradient germ. The Euler time
coefficients and nodewise contractions prove

\[
 \kappa_{\phi,L,t}
 =-\frac{t(2t-1)}2J_{\phi,L}.
\]

Thus

\[
 D_{t,L}(\eta)-\kappa_{\phi,L,t}\eta^3
 =D_{t,L}(\eta)
  +\frac{t(2t-1)}2J_{\phi,L}\eta^3,
\]

so the signs in (T.16), (C.10a), and the \(L=3\) formulas agree. At
\(t=2\), the coefficient is \(-3J_{\phi,3}\), explaining the
\(+3J_{\phi,3}\eta^3\) inside (T.21).

## Constants and specializations

The remainder base

\[
 B_\phi=\max\{4,M_\phi\}
\]

contains all activation dependence in the compiler envelope. The integer
\(E_{L,N}\) is given by terminating displayed recursions. For \(L=3\),

\[
 M_{3,2t}=8t+2,
\]

and substitution gives exactly (T.19). The fifth-derivative chain factor
is \(2^5=32\), so the two Taylor remainders contribute
\((32+1)/120<1\), as used in Section 5.

The compact coefficient uses exactly nine Gaussian activation moments.
The shared activation-only base

\[
 A_\phi=\max\{4,4M_\phi^4\}
\]

and the terminating two-pass recursion (M.2)--(M.4) give

\[
 |J_{\phi,L}|\le\overline J_L,
 \qquad
 |\kappa_{\phi,L,t}|
 \le\frac{t(2t-1)}2\overline J_L.
\]

All \(L\)- and \(t\)-dependence is explicit. Neither base is defined from
an output, trained trajectory, or continuity modulus.

## Limit order and branches

The proof first takes \(n\to\infty\) at every fixed step. Only the resulting
population DAG is differentiated at zero. No finite-width Taylor expansion
or width/step limit exchange occurs.

The nonconstant nonlinear and affine rank branches are covered by the width
theorem. If \(\mathbb E\phi'(G)^2=0\), continuity and Gaussian full support
give \(\phi\equiv\pm1\); then \(F_{N,L}(h)=Nh\), \(J_{\phi,L}=0\), and the
discrepancy vanishes exactly.

## Rendering and reference audit

The inline and display math delimiters in `PROOF.md` are balanced:

\[
 \#\text{inline opens}=\#\text{inline closes}=97,
 \qquad
 \#\text{display opens}=\#\text{display closes}=103.
\]

No duplicate equation tag occurs. The previously damaged strings `tge1`
and `Gsim` are absent, and no raw `\left{` remains. References to the
compact coefficient are unconditional; the only remaining open claim is
the separately identified time-uniform \(t^4|\eta|^5\) remainder theorem.

`EVIDENCE_LEDGER.md` and `APPROACH_REGISTRY.md` now agree with these claim
levels and with both the failed old route and the successful replacement.
