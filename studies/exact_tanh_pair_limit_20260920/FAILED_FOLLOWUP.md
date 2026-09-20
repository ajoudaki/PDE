# Failed further attempt at the exact pair limit

2026-09-20. This continues the same study after the user rejected presenting
an unresolved continuation estimate as a meaningful resolution. The objective
was an unconditional, substantial result about the canonical exact dynamics
for equal-weight opposite-label pairs at arbitrary angular separation.

**Outcome: failed.** No extension of the exact-network population limit was
proved. No counterexample to that limit was proved either. The calculations
below explain why two additional approaches were stopped; they are not a
replacement achievement or an answer to the requested theorem.

## Direct contraction of Gaussian response coefficients

The previously proposed next route was to control the contracted response
without controlling the absolute sum of its coefficients. The finite-program
source identities in global_nonlinear.md C.4.7.10.A.2 permit an exact check of
what Gaussian projection alone provides.

Fix a finite program and an upper backward query Delta. Write its forward
Gaussian sources as xi=(xi_1,...,xi_m), with covariance
G_ij=E_1[H_i H_j], where H_i are the corresponding lower features. Freeze the
deterministic program coefficients exactly as in the book, and put
beta_j=E_2[partial_(xi_j) Delta]. The finite-program derivative envelopes
justify Gaussian integration by parts. It gives

\[
 E_2[\xi\Delta]=G\beta.
\]

This identity also holds for singular G, by expressing xi as a linear map
of a standard Gaussian vector and applying integration by parts there.
Consequently Delta-beta^T xi is orthogonal to every coordinate of xi.
Thus beta^T xi is the orthogonal projection of Delta onto their linear span,
including when this span has dimension less than m. In particular,

\[
 \left\|\sum_j\beta_jH_j\right\|_{L^2(\Omega_1)}^2
 =\beta^TG\beta
 =\|\beta^T\xi\|_{L^2(\Omega_2)}^2
 \le\|\Delta\|_{L^2(\Omega_2)}^2.
\]

The reverse source has the same second moment as Delta. Hence its sum with
this reaction field has norm at most 2||Delta||_2. This is the already-known
initialized-action bound ||A_0^* Delta||_2<=2||Delta||_2. It supplies no new
continuation estimate.

Even bounded features, bounded upper queries, and this exact projection
identity do not imply uniform integrability of the contracted field. To see
this at the level of those proposed hypotheses, take an event E of probability
epsilon on the lower space, H=1_E, and xi=sqrt(epsilon) G_0 on the upper space,
where G_0 is standard Gaussian. Let Delta=tanh(xi/sqrt(epsilon)). With
a=E[sech^2(G_0)]>0, the coefficient is beta=a/sqrt(epsilon). The features and
query are bounded by one and have precisely the required matching covariance,
but

\[
 \beta H=\frac{a}{\sqrt\epsilon}\mathbf 1_E,
 \qquad
 \|\beta H\|_2^2=a^2.
\]

For every fixed cutoff, all of this second-moment mass lies beyond the cutoff
when epsilon is sufficiently small. This example is **not** asserted to be a
reachable neural query. It only refutes the attempted deduction of the needed
tail estimate from the projection identity and boundedness alone. Determining
the actual causal queries remains unresolved.

## Averaged response bounds

Read the complete section S, including its Frobenius calculation, logarithmic
singular-value estimate, physical-time conversion, and unresolved-amplitude
discussion, in docs/finite_optimization_and_controls.md. Its model is a
one-input three-hidden-layer arctangent network, so its result was not imported
as a theorem about this study's tanh pair.

Even a successful analogue would not by itself close the proposed argument:
a bound on the mean squared logarithms of singular values does not bound
the mean squared amplification. The section's explicit diagonal propagator
example establishes that algebraic non-implication. This approach was stopped
before expanding a model-specific calculation that would leave that same gap.

## Saturation and conclusion

The attempt also reconsidered whether the first-layer tanh saturation could
remove the problematic response through a coordinate change. The correlated
two-control obstruction already checked in RESULTS.md remains applicable.
No signed estimate for the actual coupled trajectory was obtained to replace
that unavailable coordinate reduction.

The earlier conditional fitting estimates and finite-action approximation
results have not thereby been disproved. They also have not delivered the
requested unconditional exact-network result. The correct report for this
follow-up is failure, not a narrowed or resolved version of the target.

No simulation, independent review, promotion, established-source edit, or
Git mutation was performed. Scientific inputs were this study and the named
established book sections only.

The newly consulted finite_optimization_and_controls.md source had SHA-256
`80dcce91ed3cd8313654523725e28b312ab925376cd7a28d71323bed648a5628`.
