# Tame-gate H2 repaired audit 02

**Provenance:** fresh clean-room referee; it received a self-contained
description of the repaired theorem, was forbidden to inspect project files
or communicate with other agents, and did not inherit the first referee's
analysis.

**Date:** 2026-08-24  
**Verdict:** reject as a complete proof in its submitted form, though the
current-\(A\) invariant-envelope repair is correct and the common theorem
appears recoverable. The remaining defects are quantifier and named-lemma
defects, not arctangent-specific failures.

## Modules accepted

The referee verified the natural-coordinate identities and raw kernel. It
also verified that saturating the current \(A\) inside \(B\) gives

\[
 \|\chi_R(A)d(Z)-\chi_R(\widetilde A)d(\widetilde Z)\|_2
 \le \|d\|_\infty\|A-\widetilde A\|_2
 +R\operatorname{Lip}(d)\|Z-\widetilde Z\|_2,
\]

so the cutoff vector field is genuinely locally Lipschitz. The pointwise
bound on \(A-a_{0,M}\) makes the saturation inactive for both exact and
sufficiently fine Euler paths. The referee further verified that the state
Euler estimate controls \(Q\) through

\[
\begin{aligned}
 \|Q-\widetilde Q\|_2
 &\le(\|\Gamma\|+\|q\|_{\rm op})\|B-\widetilde B\|_2
   +\|q-\widetilde q\|_{\rm op}\|\widetilde B\|_2,\\
 \|Z-\widetilde Z\|_2
 &\le(\|\Gamma\|+\|q\|_{\rm op})L_\psi
       \|r-\widetilde r\|_2
   +\|q-\widetilde q\|_{\rm op}\|\widetilde X\|_2.
\end{aligned}
\]

## Mandatory source-construction lemma

Separate fixed-program limits are insufficient by themselves. A promoted
proof must enumerate a countable program class closed under finite parallel
joins and rational linear combinations, take all joint limits on one event,
prove projective consistency, realize the countable family on one
probability space per sort, quotient null program fields, and define
\(\Gamma,\Gamma^*\) on the resulting dense program algebras. Bai--Yin must
make those maps bounded independently of the chosen representation, and
the finite adjoint identity must pass before continuous extension. The
logical order is fixed-program laws, then source/action construction, then
the Banach ODE, then Euler identification.

## Mandatory two-mesh UI lemma

For fixed cutoff \(M\), an auxiliary mesh \(\bar h\) gives

\[
 U_M(R)\le4C^2\bar h^2+8C_{\bar h}/R^2,
\]

where \(U_M\) is the exact-orbit square-tail functional. One first chooses
\(\bar h\) and then \(R\). After that, a **different** comparison mesh
\(h\) is chosen for the saturated observable
\(c(r)^2T_R(Q)^2\), whose Euler error is \(O(C_Rh)\). Conflating the meshes
would create a circular competition between \(C_h/R^2\) and \(C_Rh\).

## Mandatory cutoff/Osgood lemmas

The proof must state cutoff-uniform compact-slab bounds for
\(A,B,q,Q,r\). For \(M'\ge M\), the comparison must read

\[
 \sup_{|s|\le S}D_{M,M'}(s)
 \le C_Se^{C_SM}\|a_{0,M'}-a_{0,M}\|_2,
\]

with \(D\) including the state and derived fields \(B,Q\). This makes clear
why only the smaller cutoff enters the exponent and why Gaussian tails make
the family Cauchy.

The Gaussian multiplier statement must include the boundedness hypothesis.
For \(\|w\|_\infty\le H\) and \(\delta=\|w\|_2\le H\),

\[
 \|a_0w\|_2
 \le C_H\delta\sqrt{\log(eH/\delta)}.
\]

Without the \(L^\infty\) hypothesis the assertion is false. Here it applies
because \(w=d(Z)-d(\widetilde Z)\) is bounded. The uncut solution is built
on each fixed slab and globalized by restriction compatibility/restart.

## Probability and topology quantifiers

For each fixed activation in the uncountable tame class, the theorem may
assert a probability-one event depending on that activation. A single event
for all integer \(\phi_m\) is available by countability. A single event for
the entire uncountable class needs a separate separability theorem and is
not claimed.

Training convergence must mean uniform convergence of the named scalars and
convergence of declared empirical observables/joint laws. It cannot mean a
cross-width \(L^2\) or trace-norm subtraction of parameter states.

## Disposition

These requirements are incorporated as explicit lemmas and limit orders in
the next theorem revision. A further isolated reconstruction is required
before promotion.
