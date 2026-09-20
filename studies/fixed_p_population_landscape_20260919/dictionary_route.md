# Full-dictionary analytic support and parity route

Frozen independent route, 2026-09-19. This report uses only `docs/NOTATION.md`, complete parts 2–4 of `docs/global_nonlinear.md` C.4.7.9, and complete C.4.7.10.B, C.1, D.3. Required mathematical/research skills were read. No other study, route artifact, numerical experiment, or Git history was consulted. Findings below are internal mathematical analysis, not established-library additions.

Presentation revision, 2026-09-19, after independent freeze: two backspace-corrupted \beta commands and three tab-corrupted \tanh commands were repaired. No mathematical assertion or proof argument was changed. Pre-revision SHA-256: e0f1bc93ac7ef6d96c8ec2c0878d09675b81fabc8f16d068a2fb89361a54e914.

## Target and outcome

Fix arbitrary closure order (p\ge1), retain the **entire** canonical polynomial-plus-initialized-word list with its positive Cholesky ridge, and use the exact populations. The physical state space is

\[
 L^2(\lambda_1;\mathbb R^2)\times L^2(\lambda_2)
       \times\mathbb R^{d_2\times d_1}
\]

with the population (L^2,L^2) and ordinary Frobenius norms. The question concerns local minima of the finite-data square loss on this state space, not just reached gradient-flow states. Input representatives (u_i\in S^1) are distinct modulo sign; repeated/antipodal observations can first be combined when their labels agree with the bias-free oddness constraint. Positive observation weights are allowed. The unrestricted compatible problem has global minimum zero, as proved below.

This route establishes three useful facts: finite-program analytic support; existence and density of full-rank readout-feature states at every fixed order; and an explicit failure of mark-parity preservation by the full dictionary's ridge filter at order 260. It also gives a range-compatible counterexample to a universal derivative-feature nonmembership statement. It **does not prove or refute** absence of suboptimal local minima. The remaining logical bridge is from dense full-rank hidden states to a loss-decreasing perturbation with readout change tending to zero.

Write (U_\ell v=b_\ell^Tv), (a_i=E_1[b_1\tanh(w\cdot u_i)]), (z_i=U_2Ma_i), and (H_i=\tanh z_i). Constants belong to both raw spans and hence both normalized spans. Each normalized feature is bounded; redundant words are retained.

## 1. Analytic support of the full initialized dictionary

Every fixed-order mark law admits a finite Gaussian-source realization

\[
 b_\ell=\beta_\ell(G_\ell),\qquad G_\ell\sim N(0,I_{k_\ell}),
\]

where every coordinate of (\beta_\ell:\mathbb R^{k_\ell}\to\mathbb R^{d_\ell}) is bounded and real analytic. Singular innovations are represented by fixed linear maps of standard Gaussians; zero innovations need no coordinate. This representation does not assert that the feature law has a density in its ambient coefficient space.

Here is the finite-program justification. The initial seeds are linear Gaussian functions. Addition, scalar multiplication, bounded products, and sin/cos/tanh preserve real analyticity on real source space. In the stated complete source rule, each new action answer is a deterministic linear combination of previously exposed Gaussian sources, a fresh Gaussian innovation with deterministic covariance, and earlier opposite-orientation input fields multiplied by deterministic expected named-source derivatives. Thus the new answer is real analytic if earlier fields are. The expectations determine constants, not functions of the current source point. Induction handles the finite initialization union. Positive-ridge Cholesky normalization is a fixed invertible linear transformation, preserving these properties. The envelopes and source construction in the assigned established sections ensure the needed integrals exist.

Consequences:

* The support of the mark law is the closure of (\beta_\ell(\mathbb R^{k_\ell})), because every nonempty open Gaussian-source set has positive probability. In particular it is connected.
* A continuous function of the source coordinates which vanishes almost surely vanishes everywhere: a nonzero value would persist on an open neighborhood of positive Gaussian probability.
* Every current (z_i), (H_i), and ((U_2h)\operatorname{sech}^2(z_i)) is a bounded real-analytic function of the upper source coordinates. Their almost-sure linear relations therefore hold pointwise on all source space.
* A nonconstant continuous scalar feature has an image containing a nondegenerate interval. The raw upper core contains the specific feature (X=\tanh\xi_1), whose law has strictly positive density on ((-1,1)).

These conclusions survive the entire initialized-word tail. They do **not** justify treating (b_2) as a vector with an open Euclidean support: its polynomial coordinates satisfy many exact algebraic relations, and its tail coordinates have additional exact functional relations. Analytic support by itself does not prove independence of arbitrary (\tanh(U_2v_i)).

## 2. Exact interpolation at every fixed order

Let (u_1,\ldots,u_m) be distinct modulo sign. Choose (v\in\mathbb R^2) outside the finitely many lines

\[
 v\cdot u_i=0,\qquad v\cdot(u_i-u_j)=0,
 \qquad v\cdot(u_i+u_j)=0.
\]

All defining vectors are nonzero, so such (v) exists. Put (t_i=\tanh(v\cdot u_i)); then every (t_i\ne0) and their absolute values are pairwise distinct. Set (w\equiv v) and (v_0=E_1b_1\ne0). The last assertion follows by pairing (v_0) with any coefficient vector representing the constant one. Then (a_i=v_0t_i).

Choose (e\in\mathbb R^{d_2}) with (U_2e=X=\tanh\xi_1), available already in the polynomial core, and set

\[
 M=\frac{e v_0^T}{|v_0|^2}.
\]

This gives (z_i=t_iX) and (H_i=\tanh(t_iX)). These (m) functions are linearly independent in (L^2(\lambda_2)). Indeed an almost-sure relation gives (sum_i\alpha_i\tanh(t_ix)=0) on ((-1,1)), by the positive density and continuity. Real analyticity extends it to every real (x). Absorb the signs of (t_i) into coefficients and order the positive absolute slopes (s_1<\cdots<s_m). The limit (x\to\infty) first gives (sum_i\alpha_i=0). Subtracting that constant relation and multiplying by (e^{2s_1x}), the identity

\[
 \tanh(sx)-1=-\frac{2}{e^{2sx}+1}
\]

gives (alpha_1=0). Repeat to obtain every coefficient zero.

Consequently (G_{ij}=E_2[H_iH_j]) is positive definite. For arbitrary compatible labels (y_i), the bounded readout (c=\sum_j(G^{-1}y)_jH_j) fits all representatives exactly, and oddness fits their antipodes. Extra full-dictionary features remain present throughout; the matrix simply chooses a permitted rank-one direction. This proves attainability, not reachability from the prescribed initialization.

## 3. Full-rank hidden states are dense in the physical topology

The preceding interpolation construction can be connected to any current (w_0\in L^2), (M_0) by

\[
 w_t=(1-t)w_0+tv,\qquad M_t=(1-t)M_0+tM_*,\qquad 0\le t\le1.
\]

For every (t_0<1), (a_i(t)), and then (H_i(t)) as an (L^2(\lambda_2))-valued function, are real analytic near (t_0). The point requiring care is that (w_0) has only a second moment. For fixed real (x=w_0\cdot u_i), (A=v\cdot u_i), consider (\tanh((1-t)x+tA)) for complex (t). On a sufficiently small complex neighborhood of (t_0), (operatorname{Re}(1-t)\ge\delta>0). If the real part of the argument is bounded, this forces (x) into a bounded interval independent of the sample point. Choosing the imaginary width sufficiently small then keeps the imaginary part of the argument away from (pi/2+\pi\mathbb Z). Outside that bounded real-argument region, the formula for complex tanh gives a uniform bound and excludes poles. Thus tanh has a uniformly bounded holomorphic extension in (t), uniformly over all real (x). Multiplication by bounded (b_1) and dominated integration proves analyticity of (a_i(t)). Since (b_2) is bounded and (M_t,a_i(t)) are finite-dimensional analytic functions, the same argument, or their uniformly convergent local power series, gives (L^2)-analyticity of (H_i(t)).

The Gram determinant (det(E_2[H_i(t)H_j(t)])) is therefore real analytic on an open interval containing every (t\in[0,1)). It is continuous at (1), by boundedness of the gates and (L^2) continuity of (w_t), and strictly positive at (1) by the preceding construction. Hence it is not identically zero on ([0,1)). A nonzero real-analytic function cannot have zeros accumulating at an interior point: its first nonzero Taylor coefficient would give a punctured neighborhood without zeros. In particular there are full-rank states for arbitrarily small (t>0), and (w_t\to w_0) in (L^2), (M_t\to M_0) in Frobenius norm.

This density result does not itself prove a local-minimum theorem. The readout needed to exploit a newly appearing feature may involve inverse Gram eigenvalues diverging as (t\downarrow0). Its (L^2) distance from the current readout need not tend to zero. An argument using only full rank arbitrarily nearby silently misses the required physical topology.

## 4. A derivative-feature nonmembership claim fails inside the current range

The statement

\[
 (U_2h)\operatorname{sech}^2(z_i)
       \notin\operatorname{span}\{\tanh z_j:1\le j\le m\}
\]

is false if asserted for every nonzero current-range direction and every index. This remains false when (U_2h\in\operatorname{range}(U_2M)).

An explicit finite prefix suffices. Code 7 is (A_0 1), an upper standard Gaussian (\xi_0). Code 62 is (W=\tanh\xi_0), and code 502 is (\tanh W). Thus at every (p\ge502) the entire upper span contains (1,W,\tanh W). They are linearly independent, because a putative relation on the interval-valued support would make tanh affine on an interval.

Choose a current matrix with range containing those three functions and sample fields (z_1=0,z_2=W). Choose (h) so that (U_2h=\tanh W) is in that range. Then

\[
 (U_2h)\operatorname{sech}^2(z_1)=\tanh W=H_2.
\]

The sample assignment is physically admissible, not merely a formal coefficient choice. For two inputs distinct modulo sign, lower fields can be chosen so that (a_1,a_2) are linearly independent: take two disjoint lower-mark sets with independent moment vectors (E[b_1 1_{E_k}]), and set (w) equal to suitable constant vectors on those sets and zero elsewhere. Such moment vectors exist because the lower mark span has dimension at least five already at (p=1). If all set integrals lay in a proper subspace, a nonzero linear combination of independent lower features would vanish almost surely, a contradiction. Constant vectors (v_1,v_2) can be chosen so that the two-by-two matrix (\tanh(v_k\cdot u_i)) is nonsingular; since (u_1,u_2) are linearly independent in two dimensions, prescribe their two projections directly. The remaining unused lower coefficient directions allow the matrix range to include (1,\tanh W) while sending (a_1\mapsto0,a_2\mapsto W).

This is only a **proof-route counterexample**. Other directions in the same range may work, and the constructed state need not be a local minimum. In particular it does not defeat a lemma asserting existence of some useful index/direction when the residual is nonzero and all local-minimum conditions hold.

## 5. Explicit failure of finite-prefix mark-parity preservation

Input oddness (f(-u)=-f(u)) holds at every state and every order. Initialization-mark reversal is a different issue. The full prefix does not in general preserve the mark-parity decomposition even at the level of its positive ridge filter.

Take (p=260). Cantor pairing gives (pi(2,0)=3), so code 32 is the lower word (g_1+1); code (4+8\cdot32=260) is

\[
 F=\sin(g_1+1)=\cos(1)\sin g_1+\sin(1)\cos g_1.
\]

Both (sin g_1) and (cos g_1) are already retained, at codes 20 and 21. The law of the needed lower marks can be represented by (g,\zeta,\eta), where (p_i=\zeta_i+\alpha\tanh g_i) as in part B and (eta=A_0^*1). The new reverse constant probe has zero named-source derivative, variance one, and covariance (E_2\tanh\xi_i=0) with the two old reverse sources. Hence (eta) is independent of ((g,\zeta)). The involution

\[
 S_1(g,\zeta,\eta)=(-g,-\zeta,\eta)
\]

preserves this law and reverses all four lower core coordinates.

Every retained lower feature before code 260 is homogeneous under this involution. To verify the finite-prefix claim without a program search: a unary code below 260 has operand code at most 31. The valid operands up to 31 are constants, (g_1,g_2), (A_01), (A_0^*1), and sin/cos/tanh of (g_1,g_2); their lower gates are all homogeneous under (S_1). Binary/scaling codes below 260 have paired indices (a,b) with (pi(a,b)\le32), hence (a+b\le7). Their bounded retained lower operands therefore involve only constants; terms involving a Gaussian seed are unbounded and are not retained (zero terms cause no problem). Action answers are not retained as bounded features. The polynomial core is homogeneous by the Chebyshev parity identity. Code 260 is the first lower bounded feature in this prefix that mixes these two parity sectors.

Let (R) be the unitary involution induced by (S_1), and let

\[
 T_0=\sum_{\text{raw features before 260}}\psi\otimes\psi,
 \qquad T=T_0+F\otimes F.
\]

Every homogeneous rank term commutes with (R), so (T_0R=RT_0). The odd-to-even block of the extra rank is

\[
 P_+(F\otimes F)P_-
 =\sin(1)\cos(1)\,\cos g_1\otimes\sin g_1\ne0.
\]

The two functions have positive norms and both coefficients are nonzero. Thus (TR\ne RT). For the exact normalized dictionary,

\[
 Q=S(G+\eta I)^{-1}S^*=T(T+\eta I)^{-1},\qquad\eta>0.
\]

This identity follows either by diagonalizing the finite-rank operator or multiplying by (T+\eta I). If (Q) commuted with (R), then so would (T=\eta Q(I-Q)^{-1}); the inverse exists because (Q) is finite rank and every nonzero eigenvalue is (lambda/(\lambda+\eta)<1). The contradiction proves (QR\ne RQ).

The raw span itself is invariant here, since (F) lies in the span of the already present sine and cosine. The obstruction comes from retaining the extra feature with a positive ridge: the filter depends on the full raw feature frame, including redundant/mixed words, rather than only its span. Replacing the full dictionary by its polynomial core, deleting this feature, or replacing the filter by the orthogonal projection changes the specified closure.

This calculation defeats the blanket extension of the order-one/order-two parity-filter argument. It does not prove that no invariant subset of any kind exists, and it does not by itself prove that a specific trained path loses every symmetry. A purported arbitrary-order parity proof must handle the actual noncommuting filter and full initialized matrix, rather than assume an odd-to-odd block structure.

## Remaining bottleneck

The strongest positive result here is exact interpolation plus density of full-rank hidden states in the required (L^2\)/Frobenius topology for the entire canonical dictionary. The missing step is control of a **small readout perturbation** near a potentially rank-deficient local minimum. Universal per-index derivative separation is false, and simple mark parity is unavailable at arbitrary prefix order. A successful local-minimum proof may still use all local-minimum conditions, readout-nullspace perturbations, and higher-order analytic information along the explicit interpolation path. Those conditions were not completed in this independent route.
