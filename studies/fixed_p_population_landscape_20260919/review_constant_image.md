# Informed internal audit of constant-image exclusion

2026-09-19. **Verdict: PASS for the frozen constant-image theorem and its stated combination with rank-one exclusion. No mathematical correction is required.**

This is an explicitly informed internal audit, not an isolated or promotion review. I authored the dictionary route/count files and previously reviewed the finite-sample and rank-one theorems. I read the complete frozen constant-image candidate. The allowed established source scope remains docs/NOTATION.md and complete C.4.7.9.2–4 and C.4.7.10.B, C.1, D.3 of docs/global_nonlinear.md. I did not read abstract_route.md. Only this review file was written; all candidates and earlier reviews remain unchanged.

## Exact inputs

| Input | SHA-256 |
|---|---|
| constant_image_exclusion.md | f513804bcbf7d0b2ff040be6f3cc6c179e7e1cb0d1428f44bf79934b7a71b305 |
| finite_sample_theorem.md | 5242bfda61ed94f2e5bda83b8843fe713d37dcbf4b7e2f204dc1ba8c23757c24 |
| rank_one_exclusion.md | d5d335988e0b35e0b22b79f8aadf14040638e8ff50749f1f56428b4d9b805a9d |
| dictionary_route.md | a95512882aa16474e6f6bd9ad0d4a88e3d9499d2b6976191188e4fa752079c53 |
| dictionary_counts.md | 87ddaf612ff335f0829a9cc5103c74022786dfec04de4bc9749800319c1fa804 |
| docs/global_nonlinear.md | 81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |

## 1. Model and effective constant image

The operator \(K=U_2M|_{B_1}\) is the correct effective map, including all lower and upper coordinate redundancies. If its range is contained in the constant functions, it has the factorization \(Kh=(v\cdot h)1\) with \(v\in B_1\), including \(v=0\). Thus the upper fields are the deterministic scalars \(\alpha_i=v\cdot a_i\), and the predictions are \((Ec)\tanh\alpha_i\).

The assumptions that constants belong to both mark spans imply \(E b_1\ne0\) and \(E b_2\ne0\): pair each expectation with coefficients representing the constant one. A nonconstant upper mark combination has positive variance, with nonconstancy understood as an \(L^2\) property. All three assumptions hold in the canonical full dictionary at every positive order.

## 2. Modified ridge independence

For every finite real \(\kappa\),

\[
 h_\kappa(t)=\tanh(t)\operatorname{sech}^2(\kappa\tanh(t))
\]

is odd, bounded, real analytic on the whole real line, and has derivative one at zero. If only finitely many Taylor coefficients were nonzero, its Taylor polynomial would agree with the function near zero. The real-analytic identity theorem would extend that equality along the connected real line. Boundedness would make the polynomial constant, contradicting its derivative. Thus infinitely many odd coefficients are nonzero. The proof does not require every odd coefficient to be nonzero.

The finite hyperplane avoidance step gives nonzero projection values with distinct positive squares for every finite set of input directions distinct modulo sign. Choosing any \(m\) nonzero odd coefficients yields the stated square generalized Vandermonde matrix with increasing nonnegative integer exponents and distinct positive nodes.

Its invertibility proof is valid. More explicitly, divide a polynomial having \(k\) nonzero monomials by its smallest power of \(x\), without changing its positive zeros. The resulting polynomial has a nonzero constant term and \(k-1\) other monomials. Its nonzero derivative has \(k-1\) monomials. By induction it has at most \(k-2\) distinct positive roots, while Rolle's theorem places at least one derivative root between each pair of distinct positive roots of the original polynomial. The original therefore has at most \(k-1\) such roots. The case \(k=1\) is immediate. Singularity of the square evaluation matrix would give a nonzero linear combination of at most \(m\) monomials vanishing at \(m\) distinct positive nodes, a contradiction.

This verifies ridge independence for every \(\kappa\), including \(\kappa=0\), and without linear independence of the physical inputs.

## 3. Flat predictions and the analytic continuation

In section 3, either \(v=0\) or \(Ec=0\) makes predictions zero for every lower field with the same matrix and readout. Hence every sufficiently close lower-field change preserves the loss and is itself a local minimum on a smaller ball. Residuals remain the fixed vector \(-y\).

Writing \(m_c=E[b_2c]\), matrix stationarity is exactly

\[
 0=2m_c\left[\sum_i\mu_i r_i\phi'(v\cdot a_i)a_i\right]^T.
\]

If \(m_c\ne0\), cancellation of this outer product gives equation (5). The factors and transpose are correct. No assertion about interiority of the set of attainable moment arrays is used.

An \(L^2\) lower field admits bounded truncations converging in \(L^2\). One can therefore choose a bounded truncation strictly within the original local-minimum ball. Its equal loss makes it a new local minimum, still with the same matrix, readout, and constant-image property. This step is valid in the stated physical topology and does not need an \(L^\infty\) neighborhood of the original field.

For any fixed finite vector \(s\), the path \(w_t=(1-t)\widetilde w+ts\) lies in that new local-minimum neighborhood for all sufficiently small real \(t\). The left side of (5) is real analytic at every real \(t_0\). Indeed \(\widetilde w\) and \(s\) are bounded, so near \(t_0\) the complex arguments of the first tanh gates have uniformly bounded real parts and arbitrarily small imaginary parts. A common small complex disk avoids all poles and bounds the integrands uniformly. Integration against bounded marks yields a holomorphic finite moment array. Its real value at \(t_0\), followed by continuity in a possibly smaller disk, similarly avoids the poles of each outer \(\phi'(v\cdot a_i(t))\).

This argument supplies local analyticity at every real point; it does not require one global complex strip or any holomorphic extension of an unbounded lower field. The real-analytic identity, initially valid near zero, therefore extends along all of \(\mathbb R\), in particular to \(t=1\). There \(a_i=(E b_1)\tanh(s\cdot u_i)\), giving equation (6) with the single common value \(\kappa=v\cdot E b_1\). Nonzero \(E b_1\), modified ridge independence, and positive sample weights force every residual to vanish. This contradicts positive loss and proves the necessary condition \(E[b_2c]=0\).

## 4. Both final perturbations are admissible

If \(v=0\), any constant readout change \(c+\varepsilon\) remains in \(L^2\), is arbitrarily small, and preserves every zero prediction. The necessary condition from section 3 applies before and after. Their difference is \(\varepsilon E b_2=0\), impossible for nonzero \(\varepsilon\). This covers effective rank zero regardless of the original readout mean.

If \(v\ne0\), the previously verified small-population-subset condition reduces to

\[
 r_i(v\cdot b_1)(Ec)\phi'(\alpha_i)=0.
\]

For a nonzero-residual sample, the positive finite gate and positive variance of \(v\cdot b_1\) force \(Ec=0\). Section 3 then applies. For a nonconstant upper mark combination \(B=e^Tb_2\), the centered bounded function \(k=B-EB\) has zero mean and satisfies

\[
 e^TE[b_2k]=\operatorname{Var}(B)>0.
\]

The readout change \(c+\varepsilon k\) preserves its zero mean, all predictions, and local minimality for sufficiently small nonzero \(\varepsilon\). Applying \(E[b_2c]=0\) at both points gives the contradiction \(\varepsilon E[b_2k]=0\). No uniform radius over readout directions or unrestricted-size perturbation is required.

## 5. Combination and limits

Every canonical effective rank-one image is spanned either by a nonzero constant or by a nonconstant scalar mark. The former is covered here. For the latter, the previously audited finite-Gaussian-source representation makes its essential support a nondegenerate interval, so the rank-one exclusion theorem applies. Rank zero is covered here as well.

Consequently, for every fixed canonical order \(p\ge1\) and every finite compatible circle dataset, an ambient local minimum whose effective current operator has rank at most one has zero loss. Repeated or antipodal observations are handled by the previously verified signed grouping identity; incompatible labels replace zero by the corresponding irreducible weighted variance.

This conclusion has no sample-count restriction, but it does have the stated effective-rank restriction. It does not settle higher-rank states at arbitrary sample count, prove trajectory convergence, impose a rank restriction on the full initialized dynamics, or replace the unconditional sample-bounded theorem. The internal PASS verdict does not constitute promotion approval.
