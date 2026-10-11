# Author-side proof-reuse opportunities

This is bounded structural advice, not an independent review or a verdict on a rewritten manuscript. I read the complete original `compact_width.tex`, `compact_initialization.tex`, `compact_fitting.tex`, `compact_foundations.tex`, `compact_legendre.tex`, `compact_selected.tex`, and `compact.tex`, together with the notation contract and required mathematical presentation skills. I did not read another study, review history, author candidate, or the archived book. Line numbers below refer to the original files at the start of this assignment; equation labels are the stable locators.

The strongest simplification is to replace the width proof's private map and time coefficient recurrences with explicit majorants derived from the already displayed differentiated network equations. The initializer's largest exact duplication is its capped-panel counting proof. Several smaller derivations can likewise become checked invocations of existing results. The numerical continuation, finite-probability argument, and Gaussian sampler have substantial new obligations and cannot be removed by citing the older qualitative results.

## 1. Replace private map recurrences by a verified majorant table

**Target:** `compact_width.tex`, approximately lines 349–494, from the definitions of the first-variation coefficients through their numerical table. Reuse `cp:src-local-lemma`, whose proof displays the three port forces and the exact forward/backward first-variation equations, and `cp:src-propagator`. Retain the bounds in `cp:poly:eq:map-interface` and the original source gate.

Here (X=\beta^L\ge100), (\lambda=\gamma/m\in(0,1]), (\chi=1+\lambda^{-1}), (S=16Y/\lambda\le1), and (\ell_n=\log(en)), as defined by the width module. The number of deleted neurons is (u). Its explicit base bounds are

\[
J_0\le X,\quad \Gamma\le X^7,\quad
\tau_*\le X^4,\quad f_*\le X^3,\quad
M_0\le X^{31},\quad A_0\le X^{33},\quad
B_0\le X^{32},\quad E_0\le X^{38}.
\]

These are the existing scalar quantities: the propagator coefficient, gradient envelope, response/feature derivative envelopes, carrier envelope, two control amplitudes, and Hessian envelope. Keep their definitions or identify them explicitly with the original source coefficients; the table alone must not replace their meaning.

The same original quantitative bounds follow without introducing a named scalar coefficient for every layer and derivative:

| Object | Scalar coefficient bound, apart from its stated (u,n,\ell_n) factors |
|---|---:|
| Parameter insertion | (X^{80}\chi) |
| Forward insertion | (X^{85}\chi) |
| Backward insertion | (X^{125}\chi) |
| Dependence on scalar controls | (X^{90}\chi) |
| Parameter time derivative | (X^{125}\chi) |
| Forward time derivative | (X^{140}\chi) |
| Backward time derivative and lower probes | (X^{190}\chi) |

The finite checks that should replace the removed recurrences are as follows.

1. Duhamel applied to the three existing port forces bounds the parameter coefficient by

   \[
   X\{X^{33}(128\lambda^{-1}X^{11}+X^{38})+SX^{35}\}
   \le X^{80}\chi.
   \]

   This keeps the contour length (64\ell_n/\lambda), the normalized activity (2\int\rho/S\le1), and all three forces, including the residual-change force. Zero initial readout is what prevents an inverse (S).

2. The forward derivative bound (P_j\le X^3) gives preactivation coefficient at most (X^{84}\chi), then activation differentiation gives (X^{85}\chi). In the backward equation the largest forcing is the single reference-carrier term, with exponent (1+31+84=116). Complete homogeneous propagation and the layer sum cost at most (X^3); this fits (X^{125}\chi). This explicitly preserves the fact that the carrier enters additively, not once per homogeneous layer.

3. For control differences replace the two control amplitudes by one in the same forces. The parameter coefficient is at most (X^{41}\chi), the forward coefficient at most (X^{46}\chi), and the backward coefficient at most (X^{80}\chi). Hence the original common (X^{90}\chi) bound remains valid, including enlarged control nets.

4. The reference speed coefficients can be kept as a short bound row:

   \[
   a_j^z\le\lambda X^7,\quad a_j^h\le\lambda X^8,\quad
   a_j^W\le\lambda X^7,\quad
   a_j^\delta\le\lambda X^{45},\quad a_j^k\le\lambda X^{47},
   \quad D_c\le\lambda X^{45}.
   \]

   The original control-speed recursion has forcing bounded by (X^{40}) and total propagation bounded by (X^3), so its (X^{45}) bound has room. For the parameter time derivative the generator bound (2\mathcal K+(\lambda/4)SE_0\le X^{40}) and the first line give (X^{125}\chi). In the forward time products the largest forcing exponent is (3+125=128), fitting (X^{140}\chi) after propagation. In the backward time products the largest is (1+31+140=172), while the other forcing exponents are at most 133. The same propagation gives (X^{190}\chi). The lower-Jacobian probes have smaller products.

5. Preserve the width/logarithm factors explicitly: first maps have (\sqrt u n^{1/4000}\ell_n^2), with (\ell_n^3) for backward maps; control differences have (\sqrt u n^{1/4000}\ell_n^2); terminal derivatives have (\sqrt{un}n^{1/4000}\ell_n^4). The old exact product equations explain the one raw-coordinate (\sqrt n) and one extra carrier logarithm. Do not replace them by an unspecified polynomial in (n) or (\ell_n).

Thus the existing (C_0=X^{300}\chi) remains valid. The response-product envelope

\[
X^{100}(1+X^{80}+4U_{\rm fin})^2(1+C_0)^2
\le X^{1000}\chi^2
\]

also remains unchanged. This removes a substantial list of disposable scalar names while retaining a finite numerical verification, rather than importing the older qualitative `poly(log n)` claim. The width author has been sent this calculation and reports implementing this structure; I have not inspected that candidate.

## 2. Further exact proof reuse

| Original target | Existing proof to invoke | Content that must remain |
|---|---|---|
| Width 496–524: response recursion, linearized products, lower-adjoint product subtraction | `cp:src-response-recursion`, `cp:src-direct-reverse`, and the passive-observable/lower-adjoint portions of `cp:src-local-lemma` | Identify evaluated query and training driver; state that both changed lower factors retain (d_0+n^{-1/2}). Keep the new (X^{80}) amplitude, (X^{1000}\chi^2) envelope, exponent check, map-interface bounds, control count and speed. |
| Width 561–600: flaring domain, retraction, and imaginary-time generator explanation | Deterministic domain proof of `cp:src-panel-working`, `cp:src-gradient-derivative`, `cp:src-vertical`, `cp:src-flaring-gate` | Substitute the capped radius from `cp:poly:eq:panel-radius`. Define or explicitly import (h,D_s,P_s), since the later endpoint grid uses them. Keep (H_0=128\ell_n/\lambda), (J_*\le X^{34}), (C_g\le X^{38}), the numerical gate below (1/100), activity/operator/pole margins. The earlier eventual probability conclusion does not supply the finite event. |
| Width 990–1007: repeated squared-area and spectral calculation | Proof of `cp:innovation`, before it uses equal diagonal moments | Its general bound holds for any (\bar Q\succeq gI). Keep the substitutions (g=\gamma/2), (\operatorname{tr}\bar Q\ge mg), (\mathbb E\|U\|^4\le m^2X^{16}), and the resulting conditional coordinate variance. Keep the measurable maximizing coordinate, conditional third moment, and new finite small-ball argument. |
| Width 1349–1364: coefficient approximation, exact images, input reduction, retained count | Taylor construction proof `cp:panel` and compiler `cp:jets` | Keep the new panel count, tolerance, exact (K,R), retained inventory, finite degree gate, and explicit (X^{810},X^{820}) bounds. Cite the same coefficient tolerance (\eta/128), initialized operator norm eight, and exact pairing, without repeating their geometric-series proof. |
| Initialization 583–608: capped-panel count integration and reciprocal-radius estimate | `cp:poly:source`, especially `cp:poly:eq:panel-count` and its concluding proof | Identify (X=\beta^L), (\ell_n=\ell), (r_n=r_{\rm cap}), (b_n=b_{\rm cap}), (B_n=B_{\rm cap}). Keep the exact panel construction, numerical-disk inclusion (h(0)/4), (2\mathcal K r_{\rm cap}\le1), (h(0)\ge r_{\rm cap}/2), and (h(0)^{-1}=O(\sqrt\ell)). |
| Initialization 540–547: proof of first-layer input-span reduction | `cp:panel`, input reduction paragraph | Define (U_0,k) and the transformed inputs/matrix; cite equality of panel paths and Gaussian row laws. Retain the map storage and the separate (dM^2,ndk) execution costs. |
| Initialization 688–707: repeated harmonic mode parameters | `cp:harmonic-approximation`, with (\alpha_T=\alpha) | Bind its (b_d,D_d,P_T,H_*,h_j\) by reference; retain the actual set (\Lambda), (N,p_t,j_*,H_{\rm sph},\mathcal Y), because numerical quadrature and its costs use them. |

The source-source correspondence in the fifth row is exact, including the cap. It is not valid to replace this finite-panel proof by the older uncapped eventual panel statement. The numerical nodal degree (K_s) also differs from the width module's coefficient degree (K); its own (K_s+1\le8\ell) verification must remain.

The initializer can reuse the exact signed subtraction identity in the proof of `cp:signed`. It cannot simply invoke that lemma's final exponential estimate with the current constants: the initializer keeps a negative prediction-error square, optimizes it into a cubic parameter-error term, and uses a separate bootstrap. Its (C^{\rm r},J^{\rm r},A_n), endpoint remainder estimate, cubic inequality, and defect restrictions are substantive.

## 3. An exact way to bundle the four cost cases

This is optional algebraic regrouping, not permission to omit a finite-order term. It gives four common kernels and a two-model table instead of eight repeated long sums. Every expression below is inside (O(\cdot)) with numerical constants only, exactly as in `cp:init:sec:costs`. No problem parameter is absorbed. Keep all eight old equation labels by attaching them to their corresponding kernel-plus-row specializations if they are referenced elsewhere.

Use the existing numerical orders (J,K,D), source bound (R), actual source rank (r), selected support (q), and source-node count (N_s). Let (k_*=d,F=N_x) for Harmonic and (k_*=k,F=M=m+p) for Taylor; put (B=m+F) and (P_*=(L-1)n^2+n(k_*+1)). (P_d=(L-1)n^2+n(d+1)) always denotes the supplied full input array size. The original exact query budgets remain

\[
Q_H=m+2JB(K+1)+2N+r,\qquad
Q_T=m+JB(K+1)+BN_s+r.
\]

For supplied matrices take common work

\[
\begin{aligned}
W_E={}&P_d+LD^2+mP_*+nm^2+m^3+L+k_*+m+1\\
&+J[P_*BK+LmBK^2(n+K)+LnBDK^2]\\
&+LnRr+Lnr^3+Lq^2r,
\end{aligned}
\]

and common memory

\[
M_E=P_d+LnmDK+LnR+Lq^2+LD+m^2+J+L+k_*.
\]

The original supplied ledgers are exactly (W_E+W_{E,H}), (W_E+W_{E,T}), (M_E+M_{E,H}), (M_E+M_{E,T}), with

\[
\begin{aligned}
W_{E,H}={}&(N_t+J)(p_t+1)K+LnJK(N_xH_{\rm sph}+N)\\
&+Ln^2N+Ln^2r+\mathcal G_{\rm time}+N_t\log(2+N_t),\\
W_{E,T}={}&dM^2+ndk+LnMKN_s+Ln^2R\\
&+N_s\log(2+N_s)+J_s+N_s,\\
M_{E,H}={}&Lm^2K^2+LnKH_{\rm sph}+(p_t+1)K+N_t\\
&+m(d+1)+\mathcal G_{\rm memory},\\
M_{E,T}={}&LnMK+LmMK^2+N_s+J_s+Md+dk+m+1.
\end{aligned}
\]

For the implicit contract take common work

\[
\begin{aligned}
W_I={}&nk_*(1+m)+k_*m^2+nm^2+m^3+L+k_*+m+1+L(D+1)^2\\
&+(L-1)nQ^2+(L-1)nmB J(J-1)K(K+1)\\
&+J[nk_*B+k_*mF]+JLmB(K+1)^2(n+K+1)\\
&+JLnB(D+1)(K+1)^2\\
&+LnRr+Lnr^3+(L-1)nr^2+L(qr^2+r^3+q^2r)+qk_*,
\end{aligned}
\]

and common memory

\[
\begin{aligned}
M_I={}&nk_*+(L-1)n[Q+JmK]+Lmn(D+1)(K+1)\\
&+LnR+Lq^2+q(k_*+Lm+1)+m^2+L(D+1)+J+L+k_*+m+1.
\end{aligned}
\]

The method-specific additions are

\[
\begin{aligned}
W_{I,H}={}&(N_t+J)(p_t+1)(K+1)\\
&+LnJ(K+1)(N_xH_{\rm sph}+N)\\
&+\mathcal G_{\rm time}+N_t\log(2+N_t),\\
W_{I,T}={}&dM^2+LnB(K+1)N_s\\
&+N_s\log(2+N_s)+N_s+J+J_s,\\
M_{I,H}={}&Lm^2(K+1)^2+Ln(K+1)H_{\rm sph}+m(d+1)\\
&+(p_t+1)(K+1)+N_t+\mathcal G_{\rm memory},\\
M_{I,T}={}&Md+dk+LnM(K+1)+LmM(K+1)^2+Mk+N_s+J_s.
\end{aligned}
\]

These are literal partitions of the original eight expressions, with no use of eventual dominance. In particular the sampler, accumulated trained factors, (nr^3) selector, initialized source images, final basis images, node evaluation, geometry, original input storage, and small matrix solves remain charged. The finite sampler operation/sample/address bounds, scalar primitive counts, evaluator scratch qualification, rank fallback, and fixed-parameter specialization remain separate and unchanged.

This regrouping only helps if its common kernels make the computation easier to inspect. The setup author currently prefers retaining the eight original ledgers; that is a defensible choice because the ledgers are substantive finite-order claims.

## 4. Proof content with no safe wholesale replacement

- The finite source argument's own-stop endpoint grid, conditional measurability, interpolation to an adaptive common prefix, and the growing confidence order (u_\rho) are new. The older eventual local-map or budget-removal conclusions do not establish them.
- The finite scalar small-ball estimate and its numerical width gates are stronger than the old conditional central-limit argument. They need a finite proof.
- The third-order Legendre estimate needs the defect-subtracted forward history, the vanishing derivative at the prefix join, terminal-weight cancellation, the second-order Legendre tail, and the new absorption/bootstrap. The old (q^{-2}) comparison does not give (q^{-3}).
- The initializer's computed-anchor restart proof, activation value-only backend, quadrature positivity and normalization, harmonic basis evaluation recurrences, and causal factor representation establish computation that the old initialization-jet compiler did not bound.
- The two-direction Gaussian sampler, completion coupling, independent-layer law, degeneracy handling, deterministic query budget, and pathwise equality of the final arrays are new. Small retained source rank alone does not bound the client's queries or trained-factor work.

Recommendations were sent directly to both authors and the root. No manuscript file or Git state was changed by this subtask.
