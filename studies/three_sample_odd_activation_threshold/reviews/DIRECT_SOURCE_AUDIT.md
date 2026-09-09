# Independent bounded-claim audit: direct Gaussian response and full-rank geometry

Date: 2026-09-08. Auditor: three_geometry_sharpness. Theory only; no experiments or prior-file edits.

Inspected:
- `/tmp/three_direct_source_20260908.md`
- `studies/mean_field_peeling/three_sample_odd_activation_threshold/REPORT.md`, specifically Section 2
- Original scalar gradient and multiplier statements in Appendix C, Part F, of `odd_mixture_separation_quantitative/REPORT.md`

## Verdict

**PASS for the inverse-free combined L2 response lemma, its singular-covariance interpretation, the Walsh obstruction to uniform higher moments, and the full-rank near-equilateral geometry lemma.** These results do not prove a positive amplitude cutoff for the complete three-input theorem.

One wording restriction in the direct-source note Section 1 is required before treating its energy discussion as precise: the statement that energy bounds the variances of "all Gaussian innovations of any already identified finite query program" should be restricted to innovations whose actual input queries are the primal forward/backward fields just bounded there. Arbitrary extra product/derivative probes need not have L2 bounds controlled by the raw ball. This does not affect the displayed regression or Walsh lemmas or the report's conclusion. A minor `+and` typographical artifact in the report's geometry source link was also reported.

## 1. Combined Gaussian response

Let `U:R^m -> H` have columns `u_j`, and `Sigma=U*U`. Subject to the note's explicit Gaussian integration-by-parts hypothesis,

\[
 E[G F(G)]=\Sigma E\nabla F(G)=\Sigma d.
\]

Therefore `d^T G` is orthogonal in L2 to the residual `F-d^T G` against every element of the Gaussian linear span. Since that span is centered, it is equivalently the projection of `F-EF`. Hence

\[
 \|Ud\|_H^2=d^T\Sigma d
 =\|d^TG\|_2^2\le\operatorname{Var}(F).
\]

This is valid with singular covariance, requires no inverse, and remains valid with independent extra random arguments in F when the stated integrability/IBP conditions hold. If a formal derivative extension changes d by an element of `ker Sigma`, its image under U is zero. Thus the combined response is an intrinsic object even when its individual named coefficients are not intrinsic.

The note does not incorrectly assume that square-integrability of F by itself justifies IBP: it states that justification as an additional hypothesis. At a particular finite neural program those hypotheses still must be established. The text correctly refrains from promoting this fixed-program identity to mesh/cap-uniform moment bounds.

## 2. Coefficient counterexamples

For covariance `diag(1,epsilon^2)`, `F(x,y)=y/epsilon` has unit realized L2 norm and derivative coefficient `1/epsilon`. At singular covariance `diag(1,0)`, `F_k(x,y)=k y` vanishes almost surely but has arbitrary transverse derivative coefficient k. Both examples are correct. The latter coefficient lies in the kernel and its combined Hilbert response vanishes, in agreement with the preceding lemma.

## 3. Walsh higher-moment obstruction

On a group of size N, with N a power of two, the N Walsh characters are L2 orthonormal and bounded by one. Their sum is N at the identity and zero elsewhere. Thus

\[
 v_N=N^{-1/2}\sum_j u_j
 =\sqrt N\,1_{\{\mathrm{identity}\}},
\]

and `||v_N||_2=1`, while `||v_N||_p=N^(1/2-1/p)` for p>2.
Taking `F=N^-1/2 sum_j G_j` with covariance I_N produces exactly this response and a standard Gaussian F. The example disproves a dimension-independent Lp transport bound based solely on L2 regression and separate uniform bounds of the input query fields. It also disproves uniform integrability of response squares: for each fixed threshold K and N>K^2, `E[v_N^2 1_{|v_N|>K}]=1`.

The note correctly identifies this as a counterexample for arbitrary query families, not a realization by the trained neural flow. Consequently it proves a missing hypothesis, not the impossibility of neural source-tail estimates.

## 4. Full-rank near-equilateral lemma

For the normalized vectors in REPORT Section 2 the correlations are

\[
 \rho_{12}=-1/2,\qquad
 \rho_{13}=\rho_{23}=-\frac1{2\sqrt{1+\eta^2}}.
\]

They obey the closed absolute-separation bound for every `delta <= 1/2`.
The determinant of the input-row matrix is
`sqrt(3) eta/[2 sqrt(1+eta^2)]`, so

\[
 \det\Gamma=\frac{3\eta^2}{4(1+\eta^2)}>0
\]

for eta>0. The weighted sum with
`v=(1,1,sqrt(1+eta^2))` is `(0,0,eta)` and `||v||^2=3+eta^2`. Hence its Rayleigh quotient is exactly `eta^2/(3+eta^2)`, which bounds the strictly positive least eigenvalue from above and tends to zero.

Therefore no delta-only input spectral lower bound follows by adding merely full rank to the pairwise condition. The construction lives in dimension three and can be embedded in every higher dimension. For a strictly separated version it applies for each fixed `delta<1/2`; the report uses the closed condition, so the endpoint statement is correct as written.

## 5. Claim boundary

The direct energy statements are conditional on an already existing true strong gradient flow and its chain rule. The original Part F theorem supplies a continuously Frechet differentiable scalar loss, but not local Lipschitzness of its uncut Hilbert gradient. A strong endpoint and continuous limiting derivative therefore do not alone establish restart. The note preserves this distinction.

No complete theorem, amplitude asymptotic, or certificate of full population-limit validity follows from these bounded claims. The report's conclusion that the current investigation supplies no proved positive cutoff is consistent with the statements audited here.

## Final-copy verification and resolved status

Rechecked the published route copy at
`studies/mean_field_peeling/three_sample_odd_activation_threshold/routes/DIRECT_SOURCE.md`.
Its SHA256 is
`f2431508bcf36a4b66375a652fe052f72a250f7f4e571ce51709fae04b02b083`.
The complete difference against the original audited temporary note is precisely the requested Section 1 restriction: the innovation variance bound now applies only to actual queries among the bounded primal forward/backward fields, and arbitrary additional product/derivative probes are explicitly excluded without separate moment estimates.

The scope issue is **resolved**. Final bounded-claim verdict for this exact direct-source copy: **PASS, with no unresolved issue found**. This remains an audit of the stated partial lemmas and limitations, not certification of a full three-input theorem or any positive amplitude cutoff.
