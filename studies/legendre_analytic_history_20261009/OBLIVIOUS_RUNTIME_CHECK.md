# Independent runtime check of oblivious physical-time moments

Date: 2026-10-09.

## Verdict and review boundary

**PASS for the single-global-interval construction and its claimed mathematical guarantees, conditional on the stated imported paper interfaces.** The zero-length initialization, online moment equations, exact defect, quadratic feedback estimate, signed comparison, readout-only tail, and learned-state count are consistent. I found no blocking error, circular inference, or missing factor of width or sample count.

The earlier multi-panel construction supplies valid shared startup and stability arguments. The primary result is the final section's one interval, one order construction, followed by the prescribed readout-only tail. This changes the original residual-clock method; it does not justify lowering the order in that unchanged method.

This reviewer reused its existing knowledge of the permitted paper files and required mathematical-presentation skills. This is an independent check of a new candidate, **not a claim that the review began in a fresh context**. Scientific inputs for this check were only the complete frozen candidate and the same five permitted paper files. No author discussion, other study note, or other review was used as mathematical evidence. No source file was edited.

## Frozen sources

| Input | SHA256 |
|---|---|
| `studies/legendre_analytic_history_20261009/OBLIVIOUS_WINDOWS.md` | `7cd8051dda86a6bc7bee09cd46ab51ddce1fb8d21f7891f97148e34cc6137298` |
| `paper/compact.tex` | `47199d5c9e374b80b9eafefd60699c2f4bfe06dde00ebd0a1c53e2805598a0c4` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `paper/compact_foundations.tex` | `6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0` |
| `paper/compact_legendre.tex` | `862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9` |
| `paper/compact_selected.tex` | `3add2b694f38a4d7dbce90e51dafd375a7e8dee2e06d26b2d5af451bddb44885` |

The network setup, mobility coordinates, and fixed-problem probability convention come from `compact.tex`. Imported probabilistic conclusions are the real fitting event in Lemma `cp:fit`, the analytic rectangle and dense carrier bound in Proposition `cp:source`, and the dense-variability lower bound in Proposition `cp:dense-lower`. The long probabilistic proofs of the source and variability propositions are not re-certified here. The deterministic signed perturbation lemma, its carrier-based Jacobian estimate, and the Legendre endpoint projection bound were checked against their complete relevant proofs. No coefficient compiler or result from `compact_selected.tex` is needed for this candidate.

Write \(\lambda=\gamma/m\), \(z=Y/\lambda\), \(X=\beta^L\), and \(\ell_n=\log(en)\). All problem parameters, including \(Y>0\), are fixed separately as \(n\) grows. Norms of parameters are the paper's mobility norm; the aggregate history norm is \(\|g\|_{mn}^2=(mn)^{-1}\sum_a\|g_a\|_2^2\).

## Exact online construction and initialization

At a panel start \(s\), let \(A=t-s\). The active coefficients in (3) are unnormalized integrals of the actual online histories \(\widehat h_a\) and \(\widehat b_a=\widehat r_a\widehat\delta_a\). In particular, the backward history includes the physical residual and has no division by a residual.

For the shifted Legendre basis \(p_j^A(u)=P_j(2(u-s)/A-1)\), differentiation at fixed historical time gives

\[
\partial_Ap_j^A
=-A^{-1}\left(jp_j^A+\sum_{i<j}(2i+1)p_i^A\right).
\]

The endpoint value is one, so differentiating the defining integrals yields exactly (5), with all its coefficients and factors. Orthogonality gives

\[
\int_s^t(\Pi_q b)(u)(\Pi_q h)(u)^\top du
=\frac1A\sum_{j<q}(2j+1)\bar b_j\bar h_j^\top.
\]

Thus (4) is precisely the projected bilinear history integral with the canonical factor \(-2/(mn)\). The first-layer and readout equations retain their original mobilities.

The zero-length prescription is mathematically adequate. For a continuous trial parameter path, the rescaled form (7) makes every moment continuous and of size \(O(A)\). Formula (8) is the same bilinear integral on the fixed interval \([0,1]\). On a fixed finite-dimensional parameter ball, each source and its derivative is bounded, so source differences are bounded by a finite constant times the uniform path difference. Orthogonal projection contracts the vector-valued \(L^2([0,1])\) norm. Therefore the active hidden-increment map satisfies both

\[
\|\mathcal F(\vartheta)-\mathcal F(\widetilde\vartheta)\|_{C^0}
\le aC\|\vartheta-\widetilde\vartheta\|_{C^0},\qquad
\|\mathcal F(\vartheta)-\widehat\theta(s)\|_{C^0}\le aC,
\]

after including the first-layer and readout integral equations. The constants can be independent of \(q\), since this argument uses only projection contraction. Their width dependence is harmless for finite-width local existence. Choosing a sufficiently small positive \(a\) gives a contraction on the closed ball of continuous paths with prescribed value at \(s\).

At the resulting fixed point, continuous histories suffice to differentiate moments for \(A>0\): differentiating the moving polynomial kernel does not differentiate the source. The physical path reconstructed from these moments is consequently differentiable there and solves the finite moment ODE. At the left endpoint,

\[
\bar h_0/A\to\widehat h(s),\quad
\bar b_0/A\to\widehat b(s),\quad
\bar h_j/A,\bar b_j/A\to0\quad(j>0).
\]

The last assertion uses \(\int_0^1P_j(2u-1)du=0\). For each fixed finite \(q\), reconstruction then gives the correct first-order hidden increment \(-2A\sum_a\widehat b_a(s)\widehat h_a(s)^\top/(mn)+o(A)\). This proves the stated right derivative and selects a unique regular branch at zero. There is no reliance on a positive startup time or on a classical locally Lipschitz vector field at clock zero.

Bounded physical parameters bound all moments on a finite panel directly through their integral definitions. For positive clock length, the moment ODE has no singular denominator and admits ordinary continuation. At panel joins, the new active increment is zero, so physical parameters are continuous; a jump of their derivative is allowed. For the primary construction there is only the initial zero-length point and the final deterministic switch.

## Exact defect

For histories on the active interval, put \(e_g(t)=g(t)-(\Pi_qg)(t)\). The full bilinear integral decomposes into projected and remainder pairings:

\[
\int_s^tbh^\top
=\int_s^t(\Pi_qb)(\Pi_qh)^\top
+\int_s^t(b-\Pi_qb)(h-\Pi_qh)^\top.
\]

Cross terms vanish by polynomial orthogonality. Differentiating the last integral gives only its endpoint product: each interior derivative term contains a polynomial of degree below \(q\) paired with an orthogonal remainder. Therefore

\[
\frac d{dt}\int_s^t(\Pi_qb)(\Pi_qh)^\top
=b(t)h(t)^\top-e_b(t)e_h(t)^\top.
\]

Multiplication by \(-2/(mn)\), summation over samples, and differentiation of frozen earlier panels give exactly (9), including its positive defect sign. This identity is valid for the online histories. It does not assert that they are analytic.

## Dense reference approximation

The imported source rectangle supplies, for dense sources,

\[
\|h\|_{mn}\le\beta^{3L},\qquad
\max_a\|\delta_a\|_2/\sqrt n\le16\beta^{4L}z.
\]

The corresponding readout bound gives \(\max_a|f_a|\le16\beta^{7L}z\). Although an individual label need not be bounded by \(Y\), the candidate's aggregate backward-history bound is correct: use

\[
\|r\|_m\le16\beta^{7L}z+Y,\qquad
\|r\delta\|_{mn}
\le\left(\max_a\|\delta_a\|_2/\sqrt n\right)\|r\|_m.
\]

Since \(Y\le z\), this yields precisely the bound \(272\beta^{11L}z^2\) in (10), without a \(\sqrt m\) factor. The products are holomorphic because labels are constant and the dense network fields are holomorphic.

For a panel of length at most \(r_t/2\), the disk Taylor estimate gives the remainder \(2B2^{-q}\). The endpoint operator norm \(64\sqrt q\), applied after subtracting that polynomial, yields (11).

For the primary global interval put

\[
A=\max\{1,T/r_t\},\qquad q=\lceil16A\ell_n\rceil.
\]

For every \(0<t\le T\), the Bernstein ellipse with parameter \(e^{1/A}\) is strictly inside the same source rectangle. Its imaginary half-height and real excess are the expressions displayed in the candidate; \(1/A\le1\) and \(T/A\le r_t\) make both strictly less than \(r_t\). The vector-valued Cauchy estimate for the Joukowski Laurent series gives the degree-below-\(q\) uniform error \(4BAe^{-q/A}\). Applying the endpoint projection bound gives exactly (19), uniformly over every growing interval.

Here \(A=O(\ell_n^{3/2})\) and \(q=O(\ell_n^{5/2})\), while \(e^{-q/A}\le(en)^{-16}\). Consequently both dense endpoint errors are eventually at most \(\varepsilon=(en)^{-8}\), simultaneously for all relevant layers, intervals, and histories. The source event already controls the whole complex rectangle; no order-dependent or interval-dependent probability union is needed. These approximating polynomials remain proof objects and never enter the runtime or initialization.

## Quadratic feedback and signed stability

Let \(D(t)=\sup_{u\le t}\|\widehat\theta(u)-\theta(u)\|_{\mathrm{par}}\), stopped at \(D\le\varepsilon\). Forward subtraction on the bounded parameter region gives uniform sphere feature and output differences bounded by \(CD(t)\), as in (12).

Backward subtraction uses

\[
\widehat\delta-\delta
=\phi'(\widehat z)\odot(\widehat k-k)
+[\phi'(\widehat z)-\phi'(z)]\odot k.
\]

The changed-gate term is bounded in neuron RMS by the preactivation RMS difference times \(\sup_i|k_i|\). Only the dense carrier bound \(M_n=32X^{21}z\sqrt{\ell_n}\) is needed. Changed matrices act on dense responses bounded in RMS, and propagation uses bounded operator norms. Thus the response difference is at most \(C(1+M_n)D(t)\) in each sample's neuron RMS.

For \(\widehat b-b\), multiply that uniform response bound by the sample RMS \(\widehat\rho\), and bound the second product by the uniform output difference times the dense response RMS. Since \(\widehat\rho\le Y+CD(t)\), this proves (13) with a width-independent fixed-problem constant. No maximum-label or width factor is introduced.

The endpoint map \(g\mapsto g(t)-(\Pi_qg)(t)\) has norm at most \(1+64\sqrt q\) from uniform history norm to endpoint norm. Consequently the online forward endpoint error is bounded by \(\varepsilon+C\sqrt qD\), and the online backward endpoint error by \(\varepsilon+C\sqrt q(1+\sqrt{\ell_n})D\). The sample Cauchy--Schwarz estimate is

\[
\frac2{mn}\sum_a\|e_{\widehat b_a}\|_2\|e_{\widehat h_a}\|_2
\le2\|e_{\widehat b}\|_{mn}\|e_{\widehat h}\|_{mn}.
\]

This proves the primary construction's (20), with only one factor \(1+\sqrt{\ell_n}\), because only the backward-error factor incurs the carrier cost. The same reasoning gives the panel estimate (14). The feedback is quadratic in \(\varepsilon+D\); no nonvanishing endpoint error was silently substituted.

The same backward identity, on every point of the straight parameter segment, bounds training-output gradient differences by \(K_nu\|\widehat\theta-\theta\|_{\mathrm{par}}\), where \(K_n\le C(1+\sqrt{\ell_n})\). The gradient blocks have exactly the normalizations listed in the candidate. Integration along the segment proves both hypotheses of the paper's signed perturbation lemma. This is a pair-of-states argument and makes no assumption that the online state follows the original residual-clock closure.

On the stopped interval,

\[
\int_0^T\rho\le2z,\qquad
\int_0^T\widehat\rho\le2z+CT\varepsilon\le3z
\]

eventually, since \(z>0\) is fixed. Applying the signed lemma to the exact defect then gives

\[
D(t)\le e^{11zK_n}\int_0^t\sum_{j=2}^L\|\mathcal E_j(u)\|_Fdu.
\]

The coefficient \(11\) is \(2+3\cdot3\). Continuous joins create no jump contribution in the panel version. Combining this estimate with the quadratic defect under \(D\le\varepsilon\) yields

\[
D(t)\le4e^{11zK_n}C Tq(1+\sqrt{\ell_n})\varepsilon^2.
\]

Its prefactor is \(n^{o(1)}\). It is eventually less than \(1/(2\varepsilon)\), so the bound improves the stop to \(D<\varepsilon/2\). Local startup and bounded-moment continuation exclude a first stop and prove the finite-horizon bound \(D(T)\le n^{-16+o(1)}\) for the global version. Fitting of the online nonlinear flow before \(T\) was not assumed; it is not needed.

The sharper universal exponent in (21) is also justified. The paper's fitting proof gives the stronger uniform dense operator margin \(8+1/8<9\), and dense readout RMS at most \(2z\sqrt\lambda\). Under the stop, eventually the online state therefore has operators below nine and readout RMS at most \(8z\sqrt\lambda\). The explicit paper ledger applies, giving

\[
11Kz\le11X^9z+352X^{34}z^2\sqrt{\ell_n}
\le1+\sqrt{\ell_n},
\]

because \(z\le X^{-30}\) and \(X\ge100\). For exposition, the uniform operator margin from the fitting proof is the precise justification here; the bare statement that dense operators are strictly below nine would not by itself provide a width-independent margin. The needed stronger margin is present in the permitted source.

## Tail, fitting, and all-time accuracy

At \(T\), freezing moments, their reconstruction length, and the first layer fixes all hidden features. The top-feature matrix difference satisfies

\[
\|\widehat{\mathsf H}-\mathsf H\|_{\mathrm{op}}/\sqrt{mn}
\le\max_a\|\widehat h_a^{(L)}-h_a^{(L)}\|_2/\sqrt n
\le CD(T).
\]

The dense smallest singular value is at least \(\sqrt\lambda/2\). Eventually the perturbation is small enough to imply the claimed fixed Gram bound \(\widehat{\mathsf H}^\top\widehat{\mathsf H}/(mn)\succeq\lambda I/8\).

The tail residual equation is exactly

\[
\dot{\widehat r}=-\frac2{mn}\widehat{\mathsf H}^\top\widehat{\mathsf H}\widehat r.
\]

It gives residual decay at rate \(\lambda/4\), and the bounded fixed feature RMS gives \(\|\dot{\widehat w}\|_2/\sqrt n\le C\widehat\rho\). Thus readout length is finite, the parameters converge, and the labels are fitted exactly. Uniform sphere query-feature bounds imply the stated output tail \(C\widehat\rho(T)/\lambda\).

Since \(\widehat\rho(T)\le Y(en)^{-16}+CD(T)\), combining the online tail, dense output tail, and discrepancy at \(T\) proves an all-time error bounded by a fixed-problem constant times \(D(T)+Y(en)^{-16}\). This includes the fitted limit and is \(n^{-16+o(1)}\) in the global construction. It is eventually at most \(Y/n\) for every fixed positive \(Y\). The required width threshold can depend on every fixed problem parameter; there is no uniform vanishing-label or growing-data conclusion.

Intersecting with the imported dense-variability event and dividing gives the upper ratio \(C\ell_n^{5/2}/\sqrt{\gamma n}\to0\). Arbitrarily high fixed confidence gives convergence in probability without any independence assumption between these events.

## Retained information and qualifications

For the primary construction, each hidden interface stores \(m q\) forward vectors and \(m q\) residual-weighted backward vectors, all of length \(n\). The first layer and readout use \(n(d+1)\) coordinates, and the clamped clock uses one. Arrays frozen after \(T\) remain counted. This gives exactly

\[
n(d+1)+2(L-1)mnq+1.
\]

Reconstruction and its transpose can apply the rank-one sums directly; no updated dense hidden matrix is an additional persistent state. The initialized mixers use the separately declared \((L-1)n^2\) fixed coordinates. Data, activation evaluator resources, and transient forward/backward scratch have the same separate accounting as the paper.

Since \(\ell_n\ge1\), the choice of order also gives the explicit bound

\[
q\le17\ell_n+
512\beta^{30L}Y^2(m/\gamma)^2\sqrt{d+3}\,\ell_n^{5/2}.
\]

An absolute constant therefore suffices in the displayed state bound (24), with all depth and problem dependence shown there. This is \(n^{1+o(1)}\) learned storage for fixed parameters. The parameter-dependent order and schedule are fixed before evolution; stored vectors arise solely from the online model's own responses. There is no response-subspace compilation, dense rollout, initialization-jet calculation, or hidden source-coefficient table.

The statement's qualifications are necessary and accurately disclosed: the temporal basis/order/schedule depend on qualification parameters; the initialization is a specified regular Volterra branch rather than an ordinary locally Lipschitz clock-zero ODE; the tail is readout-only; fixed dense mixers remain quadratic; and no finite-precision, numerical-step-size, arithmetic-speed, or subquadratic total-memory guarantee follows. No mathematical correction is required within this review's scope.
