# Independent review of the finite initial-jet compiler

2026-10-08. Scoped verdict: **conditional PASS**, with the elementary-function accounting clarification below. No error was found in the deterministic approximation, initialization-only construction, rank/storage powers, or analytic-oracle obstruction in the assigned sections.

## Scope and hypotheses

I read `INITIALIZATION.md` §§1–5 and `PANEL_BOUND.md` §§1–5 completely, together with the required rigorous-math and canonical-notation skills and the latter's neural-network reference. I did not read the study README, result, other reports, source-study history, or the exploratory amplitude route. This is a review of the stated deterministic implication, not an independent proof of its inherited probabilistic or runtime interfaces.

The following are explicit hypotheses of this verdict: the dense-source holomorphic rectangle and coordinate bound; the selector support, metric, and simultaneous paired-action interfaces; the corrected-runtime error and fitting certificates; and the dense-pair lower bound witnessed at a training input. In particular I do not certify those hypotheses by citing the files mentioned in the reviewed notes. The numerical inherited comparison envelopes and training-storage inventory are used as supplied interfaces.

Write \(N=m+p\), where \(p\) counts additional passive inputs, \(\lambda=\gamma/m\), \(\ell=\log(en)\), and \(\chi=a/[1024(Y/\lambda)^2U_{\rm fin}]\). The horizon and rectangle half-width are \(T=32\ell/\lambda\) and \(r=\chi/(\lambda\sqrt\ell)\). The coordinate source bound is \(M=M_0\sqrt n\). The case \(Y=0\) is correctly separated.

## Deterministic construction

For \(\alpha=r/(4T)\le1\), the map \(t=T(1+\cos\theta)/2\) takes the stated complex \(\theta\)-strip into the source rectangle. Indeed \(|\Im t|\le T\sinh\alpha/2\le T\alpha=r/4\), and the real overshoot is at most \(T(\cosh\alpha-1)/2\le T\alpha^2/2\le r/8\). Contour shifting therefore gives \(\|c_k\|_\infty\le Me^{-\alpha|k|}\). Summing the geometric tail gives the claimed \(4M\alpha^{-1}e^{-\alpha(K+1)}\) bound. Degree (4) in `INITIALIZATION.md`, or (10) in `PANEL_BOUND.md`, leaves a tail at most one sixteenth of the requested source tolerance.

The finite quadrature is sufficient. Since \(N_t>2K\), its alias error for each coefficient is at most
\[
\frac{2Me^{-\alpha(N_t-K)}}{1-e^{-\alpha N_t}}
\le4Me^{-\alpha(N_t-K)}.
\]
The specified node count makes the reconstructed alias error at most \(\varepsilon/32\). Node error \(\eta=\varepsilon/[16(2K+1)]\) contributes at most \(\varepsilon/16\), because the absolute sum of each discrete cosine coefficient's weights is at most one. Together with the analytic tail, the budget is at most \(5\varepsilon/32<\varepsilon\). Symmetric real cosine evaluation preserves reality.

For the conformal map, put \(\vartheta=b_0/b_1\) as in (7), and write \(w=b_1(\xi-\vartheta)/(1-\vartheta\xi)\). For \(|\xi|<1\), \(|w|<b_1<1\). The Cayley transform \((1+w)/(1-w)\) has positive real part, so its logarithm has imaginary part of magnitude less than \(\pi/2\). Its real part has magnitude at most \(2\operatorname{arctanh}b_1\). These bounds give precisely the stated rectangle. Substitution gives \(\mathfrak t(0)=0\) and \(\mathfrak t(\xi_*)=T\), and positivity of its derivative on the intervening real interval gives monotonicity.

Cauchy's coefficient bound for \(u\circ\mathfrak t\) is \(\|a_j\|_\infty\le M\). Its truncation error is at most \(M\xi_*^{J+1}/(1-\xi_*)\), so cutoff (9) is sufficient. Formula (8) uses only source jets through order \(j\) because \(\mathfrak t(0)=0\). The ODE recurrence (10) is triangular, and the network's activation compositions occur at initialized preactivations. These formulas therefore construct the needed derivatives from initial arrays and the declared activation backend. They do not require a sequence of positive-time trained dense states.

The scalar matrix in (11) can be formed before application to the source jets. A common scalar map commutes with every fixed initialized matrix and its transpose. Computing paired jets by those initialized actions gives exact paired retained coefficients. Applying the analytic error argument separately to each paired source avoids an unjustified matrix infinity-norm bound.

## Rank, inverse accuracy, and retained storage

Only \(K+1\) coefficient vectors per source remain after compilation. The larger jet order \(J\) is setup workspace. The counts \(4N(K+1)+2m+d+1\) and the sharper \(2(2m+p)(K+1)+2m+d+1\) are compatible: the former includes unnecessary passive backward sources.

Under the stated gates, \(K+1\le6\ell/\alpha\). Since
\[
\alpha^{-1}=128\chi^{-1}\ell^{3/2}
=2^{17}(U_{\rm fin}/a)(Y/\lambda)^2\ell^{3/2},
\]
the numerical coefficients in `INITIALIZATION.md` (12) and `PANEL_BOUND.md` (23) are correct. Quadratic retained storage therefore has leading dependence
\[
(L+1)(2m+p)^2(U_{\rm fin}/a)^2
Y^4(m/\gamma)^4\ell^5.
\]
The displayed initial-dimension, input, output, and evaluator terms must accompany this expression. The reviewed complete inventories retain them, and use no inequality \(d\le m\). The recurrence exponent bounds leading to \(U_{\rm fin}/a\le\beta^{60L}\) are conservative and sufficient; squaring gives the advertised \(\beta^{120L}\) envelope without consuming the leading label/gap powers.

Given the runtime certificate \(\mathcal A_n\eta+\mathcal D e^{-8\ell}\), the tail test and choice \(\eta_\varepsilon=\min\{\eta_0,\varepsilon/(2\mathcal A_n)\}\) imply the inverse accuracy bound. The exact dense branch handles the alternative \(q=n\). The coefficient in the full-allowance comparison envelope is **64**, not 32. The certificate and supplied inventory are hypotheses here; the algebraic inversion does not reprove the corrected optimizer.

The assumed training-index witness implies the stated panel-quantile lower bound. Norm domination gives \(b_{n,\mathrm{panel}}\le b_n\). Thus target \(3P_n\) yields a panel error bounded by both benchmark multiples, without converting it into a whole-sphere error claim. Under the stated positive comparison-coefficient behavior, the logarithms in (19) have leading coefficients \(3/2\) and \(1\), giving recipe ratios \(2/3\) for degree and \(4/9\) for quadratic inventory. One may use the displayed positive explicit upper certificate to obtain this comparison without access to an unstated recurrence implementation. These ratios concern sufficient recipes, not minimum possible rank.

## Setup work and the analytic information bound

The identity
\[
1-\xi_*\asymp e^{-\pi T/(2r)}
\]
follows from (15) under \(T/r\ge1\). Hence the stated cutoff has exponential factor
\[
e^{\pi T/(2r)}
=e^{16\pi\chi^{-1}\ell^{3/2}}
=e^{16384\pi(Ym/\gamma)^2(U_{\rm fin}/a)\ell^{3/2}}.
\]
For fixed positive problem parameters, the explicitly chosen cutoff is superpolynomial in \(n\). This is consistent with exponent-five retained storage and does not establish cheap setup.

The declared online activation-composition cost is essential. With it, the convolution term \(P(m+N)(J+1)^2\), where \(P=nd+(L-1)n^2+n\), includes the input-dimension and sample costs of dense series propagation. The scalar map-power table need not consume \(J^2\) memory: its rows can be streamed. In detail, \(\mathfrak t'(\xi)=C/Q(\xi)\), where
\[
C=4rb_1(1-\vartheta^2)/\pi,
\qquad Q(\xi)=(1-\vartheta\xi)^2-b_1^2(\xi-\vartheta)^2.
\]
Consequently \(Q(\mathfrak t^s)'=sC\mathfrak t^{s-1}\) gives a coefficient recurrence using the previous power and two current-power coefficients. This justifies the scalar compilation work and the streamed memory count. The additional whitening, selection, and mixer-assembly work is explicitly separated; it is not hidden in the source-production bound.

There is one operational clarification: (17) does not separately charge for constructing the scalar conformal-map and quadrature constants, which involve functions such as \(\tanh\), \(\log\), and \(\cos\), and the inverse-map node values. As an algebraic-operation inventory with those scalars supplied, (17) is sound. For a literal executable operation count, state whether these elementary evaluations have unit cost, introduce their evaluation cost, or specify finite-precision evaluation and charge it. The activation oracle alone does not specify that convention. This does not invalidate the real-coordinate retained bound or the displayed series-arithmetic terms, and no bit-complexity or stability theorem is claimed.

Finally, the analytic adversaries are valid. The functions \(\pm M\tanh(\pi t/(4r))^{J+1}\) are bounded on the strip, agree through jet order \(J\) at zero, and have endpoint separation \(2M\tanh(\pi T/(4r))^{J+1}\). Their indistinguishability proves (19). Products centered at queried prefix points prove (20), including deterministic adaptive queries by following the zero-answer transcript. These arguments concern finite value/derivative information about arbitrary bounded analytic sources. They do not realize those sources as neural training trajectories and do not obstruct every compiler that uses full weights and the vector field. The reviewed text preserves this restriction. The local Taylor and fixed-prefix consequences in §5 also follow from their stated smaller horizons and do not imply all-time accuracy.

The supported result is thus an explicit, conditional, initialization-only compiler with exponent-five retained storage, a large certified preprocessing cost, and a matching exponential aspect-ratio obstruction for the restricted analytic-source information model.

## Addendum: exact panel-span reduction and scalar evaluation convention

I additionally reviewed only `PANEL_BOUND.md` §9 and the new scalar-evaluation paragraph following the setup inventory in `INITIALIZATION.md`. **Both additions pass this scoped check.**

The orthonormal matrix \(U\in\mathbb R^{d\times k}\) is fixed by the declared input panel, independently of initialization. Each Gaussian row of \(A_0U\) has covariance \(U^\top U=I_k\), so the reduced first matrix has independent standard Gaussian entries and remains independent of the other initialized layers. For each normalized panel input \(v_i\), its transformed vector \(U^\top v_i\) has norm one, and every panel inner product is preserved. Thus the population feature Gram and its training gap \(\gamma\) are unchanged.

The pathwise claim also holds: all first-layer velocities lie in the input span, so the orthogonal component \(A(t)(I-UU^\top)\) is constant. The projected matrix \(A(t)U\) satisfies the same first-layer flow on transformed inputs, with the same mobility, and \(A(t)v_i=A(t)UU^\top v_i\). Substitution through the forward pass, residuals, backward pass, and remaining parameter equations identifies their trajectories with the original coupled dense trajectories. This argument preserves the declared-panel prediction process, not merely its initialization law.

Replacing \(d\) by \(k\le\min(d,N)\) in the source construction gives \(B=2m+k+1\le4N\), where \(N=m+p\ge1\). Together with \(2m+p\le2N\), this converts the previous quadratic inventory to the bound in (29). The additive \(36A\ell^{5/2}\) term is absorbed using \(x\le1+x^2\) for \(x\ge0\); it introduces no new parameter power. The separately retained map has \(dk\le Nd\) entries, and retaining both original and transformed inputs costs at most \(2Nd\). The first compressed matrix can remain \(q\)-by-\(k\), so a \(q\)-by-\(d\) parameter block need not be materialized. The resulting additive dependence \(O((L+1)N^2+Nd)\) is valid and uses no assumption \(d\le m\).

The additional basis/projection setup allowances \(O(dN^2+N^3+ndk)\) work and \(O(dN+N^2+nk)\) workspace are sufficient in the stated exact-real arithmetic model. The extra per-query projection takes \(O(dk)\) work and \(O(k)\) workspace. This addendum checks that extra cost; it does not independently review the previously unassigned runtime formula (27). The section explicitly limits the accuracy conclusion to the declared panel, so it makes no new whole-sphere claim.

The new elementary-function convention resolves the earlier accounting clarification. Its inverse-node formula is the algebraic inverse of (7). Only a constant number of elementary evaluations per quadrature node is needed; subsequent cosine modes follow from their two-term recurrence. Therefore the stated additional \(O((N_t+1)A_{\rm elem})\) work and \(O(W_{\rm elem})\) workspace suffice for that evaluation convention. As the note states, this does not supply an independent finite-precision error or bit-complexity theorem.
