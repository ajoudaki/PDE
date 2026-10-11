# Narrow reconstruction: actual-network off-span endpoint extension

2026-10-11. Internal mathematical check, not a promotion review.

## Scope and verdict

I reconstructed Section 2 of `TEST_PANEL_DENSE_ROUTE.md` using the finite-oracle construction in Section 6 of `GELU_SILU_FLOW_ROUTE.md`, the exact conditioning and endpoint assembly in Sections 1–7 of `GAUSSIAN_ORACLE_ENDPOINT.md`, the complete projected-innovation and projected-scalar modules, and the directly cited readout-moment extraction in Sections 1–2 of `NONODD_MOMENT_ROUTE.md`. Those supporting files are in the authorized `general_nonlinear_endpoint_lower_20261010` study. I did not inspect the frozen-feature comparator or another check report. The rigorous-math, research, and canonical-notation instructions, including the neural-network reference, govern this check.

**Verdict: the off-span extension is valid under the imported fitting/source and finite-oracle modules.** No source correction is required. In particular, the line break preceding the bound variable `u` in (10) is valid TeX; an apparent `\nu` in escaped tool output is not present in the file. This report does not modify the source note.

The result concerns the original fully trained network, not just its auxiliary finite-oracle approximation. It holds for each fixed deterministic query outside the training span, at every sufficiently large individual width. It is neither a full-span result nor a polynomial-onset result. The underlying fitting and source theorems remain explicit imported inputs rather than newly audited conclusions here.

## 1. Setup and fresh randomness

Write the physical input as \(x=\sqrt d\,v\), with \(\|v\|=1\), and let

\[
S=\operatorname{span}\{x_a/\sqrt d:1\le a\le m\},\qquad
v=v_S+v_\perp,\qquad
\sigma=\|v_\perp\|>0.
\]

All data, activations, nonzero labels and this query are fixed before width tends to infinity. Keep the canonical Gaussian initialization, mobilities, positive population training gap, and the stated small-label cap. The layerwise activations satisfy the imported strip-analytic assumptions and are nonaffine.

Let \(\mathcal T_n\) be the finite training-oracle transcript. Its initialized first-layer access is entirely through \(W_0^{(1)}P_S\). In particular, linear dependence among the training directions is harmless: their actions still determine the restriction to their span. Its other initialized-weight access consists solely of adaptive hidden-matrix actions with a deterministic total envelope

\[
r_n=O_{\mathrm{problem}}(\log(en)^{9/2})=o(n).
\]

For Gaussian first-layer rows, \(W_0^{(1)}P_S\) and \(W_0^{(1)}P_{S^\perp}\) are independent. The latter is also independent of every initialized hidden matrix. Consequently

\[
G:=W_0^{(1)}v_\perp/\sigma\sim N(0,I_n)
\]

is independent of the transcript and, jointly, of the remaining hidden-matrix randomness conditional on that transcript. Adaptivity does not alter this conclusion: the training algorithm is a deterministic function of the active first-layer restriction and its hidden-matrix answers, never of \(G\).

The finite-oracle Gaussian decomposition is therefore still valid jointly with this fresh \(G\): for each hidden layer \(j\ge2\),

\[
\widehat W^{(j)}=A_j+(I-P_{U_j})G'_j(I-P_{V_j}),
\]

where the \(A_j,U_j,V_j\) are transcript measurable and, conditional on the transcript, the \(G'_j\) are mutually independent fresh matrices with entry variance \(1/n\), also independent of \(G\). The same conclusion would generally be false if one instead conditioned on the complete trained weights or on the original full-parameter fitting event.

Every true first-layer gradient increment and every numerical first-layer increment has right support in \(S\). Thus the returned first preactivation is exactly

\[
\widehat z^{(1)}(v)=a+\sigma G,\qquad
a=\widehat W^{(1)}v_S.
\]

There is no approximation in this conditional law.

## 2. The added empirical mean-norm event is legitimate

The event

\[
\|\widehat W^{(1)}P_S\|_{\mathrm{op}}/\sqrt n\le10
\]

is transcript measurable. The imported fitting cap of nine and the mobility-norm approximation error \(e_n=O(n^{-16})\) imply that it has probability tending to one, since the normalized operator difference is at most \(e_n\). On it,

\[
\|a\|/\sqrt n\le B_1:=10\|v_S\|.
\]

This is a bound on the empirical RMS of the coordinate means, not a coordinatewise bound and not a claim that the means coincide. It is exactly the hypothesis needed by the projected-innovation lemma. The use of the fitting event only to estimate the probability of this measurable event is essential and correct.

The old measurable conditions on the known hidden parts and returned readout remain unchanged:

\[
\max_{j\ge2}\|A_j\|_{\mathrm{op}}\le40,\qquad
\|\widehat w\|/\sqrt n\ge E:=Y/(4H),\qquad
\frac1n\sum_i\widehat w_i^4\le
M_4:=16\beta^{114L}(Ym/\gamma)^4+1.
\]

Here \(Y=\|y\|/\sqrt m>0\), \(\gamma>0\) is the population training gap, and \(H\) is the source note's maximal population feature RMS. Their high-probability justification does not require conditioning the fresh query Gaussians on the source or fitting events. The empirical fourth-moment bound, not a coordinate maximum with logarithmic growth, is the relevant scalar-lemma input.

## 3. First-layer innovation and the later recursion

Condition on a good transcript. Apply the one-layer innovation lemma to \(a+\sigma G\), with preactivation-removal projector zero and feature-removal projector \(P_{V_2}\). Its parameters are precisely (8): \(K_1=s_1\sigma\), the compact positive variance minimum there, and \(\kappa_1=v_1/32\). Nonconstancy, continuity, Gaussian full support and Lipschitz growth prove positivity and continuity of that minimum.

The first-layer rank conditions reduce to

\[
r_n\le v_1n/(4K_1^2),\qquad n\ge8K_1^2/v_1.
\]

They hold eventually. The resulting conditional failure probability is at most \(32K_1^2/(v_1n)\). Independently of any feature-removal projection, the elementary norm bound gives

\[
\|\widehat h^{(1)}\|/\sqrt n
\le c_1+s_1(B_1+2\sigma)=H_1
\]

whenever \(\|G\|\le2\sqrt n\). Since \(\operatorname{Var}\|G\|^2=2n\), Chebyshev bounds the latter event's failure by \(2/(9n)\). No independence between these two success events is needed.

At a later layer, expose the earlier query layers but not \(G'_j\). Conditional on everything exposed, the exact next preactivation is

\[
\widehat z^{(j)}
=A_j\widehat h^{(j-1)}
 +\sigma_j(I-P_{U_j})g_j,\qquad
\sigma_j=\frac{\|(I-P_{V_j})\widehat h^{(j-1)}\|}{\sqrt n},
\]

where \(g_j\sim N(0,I_n)\) is fresh. On preceding success,

\[
\sqrt{\kappa_{j-1}}\le\sigma_j\le H_{j-1},\qquad
\|A_j\widehat h^{(j-1)}\|/\sqrt n\le40H_{j-1}.
\]

Thus the innovation lemma with removal projectors \(P_{U_j}\) and \(P_{V_{j+1}}\) gives exactly (10)–(11). Both projector ranks are bounded by \(r_n\); its additional condition \(r_n\le n/8\) is also eventual. The norm event gives

\[
\|\widehat h^{(j)}\|/\sqrt n
\le c_j+s_j(40H_{j-1}+2H_{j-1})=H_j.
\]

The noise intervals used to define the successive variance minima are nonempty: Gaussian Poincare gives \(v_1\le s_1^2\sigma^2\le H_1^2\), and subsequently \(v_j\le s_j^2H_{j-1}^2\le H_j^2\). Since \(\kappa_j=v_j/32\), this suffices inductively. Uniform conditional bounds followed by a union bound yield (11); conditioning on earlier success never exposes the next residual matrix. The argument also covers \(L=2\), where only the first-layer innovation precedes the final scalar step.

## 4. Final scalar law and its hypotheses

After exposing the lower query layers through \(L-1\), the final Gaussian remains fresh. The returned output therefore has exactly the conditional form (12), with

\[
B=40H_{L-1},\qquad
\sigma_- =\sqrt{\kappa_{L-1}}>0,\qquad
\sigma_+=H_{L-1}.
\]

Together with \(E,M_4\) above and \(\operatorname{rank}P_{U_L}\le r_n\), these are all the projected-scalar lemma's hypotheses. In particular, arbitrary coordinate means and arbitrary transcript-dependent readout weights are permitted.

The Hermite-tail minimum \(d_R\) in (14) is positive: a zero degree-two-and-higher tail at any positive Gaussian scale would make the continuous activation affine on all of \(\mathbb R\). Continuity on its compact parameter set then gives a strictly positive minimum. With \(v_0=d_RE^2/16\), the scalar module yields the uniform small-ball estimate

\[
\sup_{b\in\mathbb R}
\Pr\{|\sqrt n\widehat f_n-b|\le c\}
\le\frac{2c}{\sqrt{2\pi v_0}}+C n^{-1/4}
\]

under the indicated conditioning. The deterministic rank envelope ensures the scalar lemma's leverage conditions eventually hold uniformly over all good transcripts. The constant \(C\) and \(v_0\) depend on the fixed problem **and fixed query**. Averaging the conditional estimate adds only the probabilities of excluded transcript/lower-layer events, which tend to zero. No final-Gaussian norm or fitting event is imposed in this conditioning.

## 5. Explicit transfer to the actual endpoint

Here is the deterministic subtraction underlying (16). Work now on the high-probability approximation and fitting events; this restriction is for transfer, not for the preceding Gaussian conditioning. Put

\[
e=\|\widehat\theta-\theta_\infty\|_{\mathrm{par}},\qquad
R_G=\|G\|/\sqrt n.
\]

Because the true and returned first-layer increments both have right support in \(S\), their unused components agree exactly. Consequently

\[
\frac{\|(\widehat W^{(1)}-W_\infty^{(1)})v\|}{\sqrt n}
=\frac{\|(\widehat W^{(1)}-W_\infty^{(1)})v_S\|}{\sqrt n}
\le e\|v_S\|\le e.
\]

Both first-layer feature RMS norms are at most \(C(1+R_G)\), and their difference RMS is at most \(s_1e\). The hidden operators of both parameter tuples are bounded, and each hidden operator difference is at most \(e\). If \(D_j=\|\widehat h^{(j)}-h_\infty^{(j)}\|/\sqrt n\), forward subtraction gives

\[
D_j\le s_j\left(CD_{j-1}
       +e\,\|h_\infty^{(j-1)}\|/\sqrt n\right).
\]

Fixed depth and linear activation growth imply feature RMS norms at most \(C(1+R_G)\) and \(D_j\le Ce(1+R_G)\). Finally, using the bounded normalized endpoint readout and normalized readout error at most \(e\),

\[
|\widehat f_n-f_n(\infty,\sqrt d\,v)|
\le e\,\|\widehat h^{(L)}\|/\sqrt n
 +\frac{\|w_\infty\|}{\sqrt n}D_L
\le Ce(1+R_G).
\]

This proves (16). Since \(e=O(n^{-16})\) and \(R_G\le2\) except with probability \(O(1/n)\), the transfer error is negligible compared with \(n^{-1/2}\).

Apply the unconditional approximant small-ball estimate with radius \(2c/\sqrt n\) and average its center over the independent second run's endpoint (extended arbitrarily on fitting failure). The transfer estimate and both fitting failures then give

\[
\Pr\{\text{both fit and }|f_n(\infty,\sqrt d\,v)
 -\widetilde f_n(\infty,\sqrt d\,v)|\ge c/\sqrt n\}
\ge1-\frac{4c}{\sqrt{2\pi v_0}}-o(1).
\]

Thus \(c=c_\delta=\delta\sqrt{2\pi v_0}/16\) gives the claimed probability at every sufficiently large individual width. Only one run needs the auxiliary approximant.

## 6. Exact reach of the conclusion

- The query need not be orthogonal to the training span. A nonzero orthogonal component is sufficient, with its active component handled by an empirical mean-norm bound.
- If \(v\in S\), the first fresh Gaussian disappears. The proof then supplies no positive first-layer variance. This is a limitation of this route, not a proof that every full-span endpoint lower bound is false. Separation from individual training directions does not imply the needed off-span condition.
- A fixed finite test panel containing one such deterministic query inherits the endpoint supremum lower bound without requiring independence among its query predictions.
- The result is eventual in width for a fixed problem and fixed query. Constants can deteriorate as \(\|v_\perp\|\downarrow0\); the imported high-probability events and compact variance minima do not provide a polynomial threshold in the displayed problem parameters. It does not address width-dependent queries approaching \(S\), changing labels, or a simultaneous all-width probability event.
- Combined with the stated existing uniform-in-time upper approximation errors, the endpoint witness yields a ratio of separate trajectory suprema tending to zero in probability. It does not yield a positive dense–dense denominator, or a comparison quotient, at every positive time.

No substantive gap was found in this off-span adaptation. Making the fixed query dependence of symbols such as \(O_{\mathrm{problem}}(\cdot)\) explicit would improve clarity, but that dependence is already allowed by the theorem's quantifiers.
