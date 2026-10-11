# Internal check of conditional endpoint coercivity

Checked 2026-10-11 by `intrinsic_geometry_check`. The complete 181-line
`INTRINSIC_ENDPOINT_ROUTE.md` was read at original SHA-256
`4181ea233a75fb5e632729ad49c5293983125d26c6c4d4110fc49a610f42c0cf`.
The complete corrected file was subsequently reread at SHA-256
`b4c64992bf2fb556f28cb1f3b155833331c001e95a31468e3c499f6cfa659bc9`.
Other scientific inputs were only the already-authorized canonical model
and the supervisor's quantitative conjecture, proved below. Required proof
and canonical-notation skills were applied. No linked scientific sources,
external references, other studies, or experiments were used.

**Verdict:** the corrected source passes this internal mathematical check.
Both endpoint lemmas, the forced-path counterexample, and signed-input
conjugacy are valid for their stated hypotheses. The additional quantitative
bound below is also valid. This is not promotion or an all-time fitting proof.

## Checks of the supplied claims

1. **Conditional sign-pattern protection.** Distinct nonantipodal unit inputs
   have distinct central hyperplanes. Crossing just the \(a\)-th hyperplane
   changes its sign coordinate alone, so the realizable sign vectors span
   \(\mathbb R^m\); the \(d=1,m=1\) edge case also passes. For the
   source's root balls, initial margins are at least \(2L\). Until row
   displacement reaches \(L\), all margins stay at least \(L\), and
   \(\|\alpha'\|\le4e^{-2L}\|B\|/\sqrt m\). Exit therefore requires
   \(\int_0^S\|B\|\,ds\ge\sqrt mLe^{2L}/4\). Conditional Markov
   gives exactly \(16C_S^2e^{-4L}/(mL^2)\). The resulting protected event
   has probability at least \(p_k/2\), and the endpoint feature error is
   at most \(2\sqrt m e^{-2L}\). Selecting one sign vector for each unit
   test direction gives precisely
   \(Q_U(S)\succeq p_{\min}\gamma^2I_m/(8m)\). Independence and
   disjointness of protected events are unnecessary. Constants are
   data-dependent; no empirical concentration or dimension-uniform bound
   has been proved. The row equation's \(1/m\) factor agrees with ascent
   of the mean prediction under canonical first-layer mobility \(n\).

2. **Unconditional energy is insufficient for this abstract inference.**
   Differentiating
   \(\alpha(s)=\zeta^{-1}((1-s/S)\zeta(G))\), with
   \(\zeta'=\cosh^2\), gives exactly
   \(\alpha'=\operatorname{sech}^2(\alpha)[-\zeta(G)/S]\).
   Gaussian exponential moments imply \(\mathbb E\zeta(G)^2<\infty\),
   while the conditional integrated squared drive is \(\zeta(G)^2\),
   with no uniform bound. The endpoint is zero. This forced-path example
   proves that additional information is needed beyond the unconditional
   estimate; it does not prove that the particular conditional hypothesis
   is necessary or that actual Gaussian gradient flow collapses.

3. **Simplex endpoint coercivity.** The kernel is the Gram matrix of
   \((h_a,b_a\otimes u_a)\), with the correct normalized finite-network
   factors. Permutation invariance gives one common and one contrast
   eigenvalue. Positive mean prediction implies positive common energy.
   If contrast energy vanished, all \(h_a\) would agree; hence all
   \(b_a\) would equal a common nonzero \(b\), since \(w\ne0\) and
   finite top preactivations give strictly positive gates almost everywhere.
   Tensor-norm factorization then forces all \(u_a\) equal. Tanh injectivity
   and \(\sum_aAv_a=0\) force all first preactivations to vanish,
   contradicting positive mean prediction. This proof needs the zero-sum
   relation and the stated kernel symmetry; it assumes neither a population
   construction nor symmetry of a particular finite Gaussian realization.

4. **Conditional path application.** On an already constructed scalar-ascent
   path, \(g'=m^{-2}\mathbf1^\top K_{\mathrm{full}}\mathbf1\ge0\).
   Positive initial common energy and continuity imply \(g(s)>0\) at
   every positive existing time when \(g(0)=0\). Initial positive
   definiteness suffices for that strictness. Continuous positive-definite
   kernels have a positive minimum eigenvalue on each fixed compact interval.
   No construction, identification, or initialization theorem for the claimed
   population path is proved in this file; external radial statements were
   not imported into the check.

5. **Exact signed-input conjugacy.** Oddness gives
   \(u(\sigma_av_a)=\sigma_au(v_a)\), and likewise for \(h,f\),
   at every state. Thus signed labels \(c\sigma_a\) give identically the
   unsigned loss with labels \(c\), so parameter gradients and trajectories
   coincide under the same initialization. The signed scalar contrast equals
   the unsigned mean. Top gates and \(b_a\) are unchanged, while \(u_a,h_a\)
   acquire signs, giving \(K_x=D_\sigma K_vD_\sigma\). Eigenvalues and
   input-Gram rank are preserved. The common direction becomes \(\sigma\).

The only wording objection concerned the original Section 4 assertion that
the conditional-energy hypothesis was "weaker" than the proposed
total-variation requirement. No such logical implication was supplied.
The supervisor's correction replaces it with the following literal text:

> Lemma 1 gives an alternative explicit sufficient root-conditional energy hypothesis for endpoint feature diversity, without requiring a total-variation response representation. No logical ordering of the two hypothesis packages is asserted.

The corrected complete source, identified by the second hash above, preserves
the mathematical arguments and resolves this objection. The earlier Section 1
statement about not requiring a response-history bound is accordingly read as
a statement about the lemma's explicit premises, not an ordering of hypothesis
packages.

## Audited additional lemma: an explicit symmetric-state kernel gap

Use probability-normalized neuron spaces; finite spaces have uniform measure.
Let \(m\ge3\), \(\sum_av_a=0\), and let the finite or already-constructed
population state have a linear first layer \(A\), bounded middle operator
\(W\), and readout \(w\). Define
\[
u_a=\tanh(Av_a),\quad z_a=Wu_a,\quad h_a=\tanh z_a,\quad
b_a=w\odot(1-h_a^2),\quad f_a=\langle w,h_a\rangle,
\]
\[
K_{ab}=\langle h_a,h_b\rangle
 +\langle b_a,b_b\rangle\langle u_a,u_b\rangle.
\]
Assume \(K\) is invariant under all sample permutations and
\[
g=m^{-1}\sum_af_a>0,\qquad \|w\|_\infty\le S,
\qquad \|W\|_{\mathrm{op}}\le M.
\]
Here \(S\) is a readout bound, not the horizon in the source's first lemma.
Positive mean prediction forces \(S,M>0\). Individual predictions need
not be equal. If \(\lambda\) is the contrast eigenvalue and
\(\lambda_{\mathrm{com}}\) the common eigenvalue, then
\[
\lambda\ge
\frac{g^4\operatorname{sech}^4(\sqrt2SM/g)}
 {4S^2M^2(m-1)(1+2S)^2}>0,
\qquad
\lambda_{\mathrm{com}}\ge\frac{mg^2}{S^2}.
\tag{1}
\]

Probability normalization gives \(\|u_a\|,\|h_a\|\le1\),
\(\|w\|\le S\), and \(\|w\|\ge g\). Also
\(\|z_a\|\le M\). Put \(R=\sqrt2SM/g\). For every \(a\),
\[
\int_{|z_a|>R}|w|^2
\le S^2\Pr\{|z_a|>R\}\le S^2M^2/R^2=g^2/2.
\]
At least \(g^2/2\) of the squared readout mass therefore lies where
\(|z_a|\le R\), yielding
\[
\|b_a\|^2=\int|w|^2\operatorname{sech}^4z_a
\ge(g^2/2)\operatorname{sech}^4R.
\tag{2}
\]

Pair contrasts have energy \(2\lambda\), so
\[
\|h_a-h_b\|\le\sqrt{2\lambda},\quad
\|b_a\otimes u_a-b_b\otimes u_b\|\le\sqrt{2\lambda}.
\]
The gate difference satisfies
\(\|b_a-b_b\|\le2S\|h_a-h_b\|\). Subtracting
\((b_a-b_b)\otimes u_b\) from the tensor difference, and using
\(\|u_b\|\le1\), gives
\[
\|u_a-u_b\|
\le(1+2S)\sqrt{2\lambda}/\|b_a\|.
\tag{3}
\]

Pointwise \(\sum_bAv_b=0\). If \(Av_a\ne0\), some other
preactivation has its opposite weak sign. Tanh preserves signs, so for
that sample \(|u_a-u_b|\ge|u_a|\). The zero case is immediate.
Therefore \(u_a^2\le\sum_b(u_a-u_b)^2\) pointwise, and (3) gives
\[
\|u_a\|^2\le\sum_b\|u_a-u_b\|^2
\le\frac{2(m-1)\lambda(1+2S)^2}{\|b_a\|^2}.
\tag{4}
\]
Choose \(a\) with \(f_a\ge g\). Since \(|\tanh z|\le|z|\),
\[
g\le f_a\le\|w\|\|h_a\|\le SM\|u_a\|.
\]
Combining this with (4) and (2) proves the contrast bound in (1).
For \(\bar h=m^{-1}\sum_ah_a\),
\[
\lambda_{\mathrm{com}}
=m^{-1}\mathbf1^\top K\mathbf1
\ge m\|\bar h\|^2\ge mg^2/\|w\|^2\ge mg^2/S^2,
\]
which proves the remaining bound. The smaller of the two bounds in (1)
is a state-dependent lower bound for \(\lambda_{\min}(K)\). Signed-input
conjugacy preserves it when \(g\) denotes the corresponding signed contrast.

This additional lemma supplies an explicit deterministic endpoint bound,
not a population or dynamical existence theorem. Its constants deteriorate
when \(g\to0\) or \(S,M\) grow. Actual conditional energy bounds,
population construction, finite-width approximation, and all-time fitting
remain unproved here. No actual-Gaussian-flow counterexample was produced.

The check used analytical derivations, constant and normalization audits,
boundary cases, and rereading of both source versions. Only this assigned
report was written; no source edits, experiments, staging, or commits were
performed. Repository HEAD was
`ef8362764b4eb8144d7af8d6f8db080fdaaf82ca`; the shared index was empty.
