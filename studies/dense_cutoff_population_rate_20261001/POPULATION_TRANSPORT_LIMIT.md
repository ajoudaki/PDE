# A limitation of transporting the entire parameter population

2026-10-03. Coordinator-derived exact diagnostic for the common-space
stability route. This is not a prediction lower bound.

Let \(A_1,\ldots,A_n\in\mathbb R^d\) be any finite read-in rows,
and let \(\nu_n=n^{-1}\sum_i\delta_{A_i}\) be their empirical law.
The canonical population read-in law is \(\gamma_d=N(0,I_d)\).
For every coupling \((A,G)\) with these two marginal laws,
\[
 \bigl(\mathbb E\|A-G\|^2\bigr)^{1/2}\ge c_d n^{-1/d},
 \qquad c_d>0.
 \tag{1}
\]
The bound is deterministic in the finite rows.

Here is a complete proof. Write \(v_d\) for the volume of the
Euclidean unit ball, and \(b_d=(2\pi)^{-d/2}\) for the maximum
density of \(\gamma_d\). The union of the \(n\) balls of radius
\[
 r_n=(2b_d v_d n)^{-1/d}
\]
centered at the rows has Gaussian probability at most
\(b_d n v_d r_n^d=1/2\). Outside this union, every possible
value of \(A\) is at distance at least \(r_n\) from \(G\).
Consequently \(\mathbb E\|A-G\|^2\ge r_n^2/2\), proving (1).
Repeated centers only decrease the union volume, so no distinctness
assumption is needed.

Thus, when \(d>2\), a coupling of the *entire* finite read-in
density with the Gaussian density cannot have \(L^2\) error
\(n^{-1/2+o(1)}\). The ratio of the lower bound (1) to
\(n^{-1/2}e^{C\sqrt{\log n}}\) diverges for every fixed \(C\).
This obstruction occurs before training. A finite network embedded
as step functions on a common probability space retains its
empirical read-in law, so the same bound applies to that embedding.

This places a precise limit on using the parameter-distance stability
estimate in POPULATION_RESPONSE_TRANSPORT.md as the finite-width
comparison. It does not invalidate that population-to-population
stability result. To obtain the desired prediction rate, a construction
must instead compare sampled population fields, use weaker observables,
or otherwise account for empirical averaging before demanding a small
full-law parameter distance.

It would be incorrect to call (1) the negative theorem requested by
the user. The initial predictors are exactly zero at every width.
More generally, for a deterministic feature map
\(\Psi:\mathbb R^d\to H\) into a real Hilbert space with finite
second moment, independent Gaussian rows satisfy
\[
 \mathbb E\left\|\frac1n\sum_i\Psi(A_i)
                         -\mathbb E\Psi(G)\right\|_H^2
 =\frac1n\,\mathbb E\|\Psi(G)-\mathbb E\Psi(G)\|_H^2.
 \tag{2}
\]
Expanding the square proves (2): the centered cross terms vanish
by independence. It applies, for example, to square-integrable
query-feature functions. Root-width functional averaging and the
slower full-law transport bound therefore coexist even at
initialization.

Equations (1)–(2) are exact. Neither proves a rate for the
nonlinear adaptively trained predictor. No numerical experiment,
external theorem or other study is used.
