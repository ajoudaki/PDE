# Internal check of the arbitrary-label geometry route

2026-10-03. **Verdict: INTERNAL PASS for the scientific claims at the frozen hash below.** There is one cosmetic formula typo: \(v=c,v_0+v_\perp\) in Section 2 should read \(v=cv_0+v_\perp\). The definitions on the next line and every subsequent calculation use the intended multiplication. No mathematical repair is required.

This is an internal check by the author of the separately frozen ARBITRARY_LABEL_NEGATIVE_ROUTE.md, whose scalar continuation result overlaps Section 1. It is not a fresh independent promotion review. The geometry candidate was first read after both routes were frozen. No supervisor proof of the remaining scalar population rate, other new route, experiment, or other study was read. The supervisor independently reported the same cosmetic typo after this check's reconstruction was complete.

## Frozen inputs and actual coverage

The entire 408-line geometry candidate was read and independently reconstructed. Its hash was verified before reading:

    ARBITRARY_LABEL_GEOMETRY_ROUTE.md:
    414a766ac02a67660e0efc0c8f0d09f7c8c01e8ee53c4a3c1dab6f706c2d95fa

The current hashes of its named inputs match those listed by the candidate:

    paper/main.tex:
    60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95
    paper/results.tex:
    6e76e83aae3a3e36f588bdf37dddf72ac811bf2644de664fb0b4b83f117704a1
    docs/index.qmd:
    f7a21b794e21f145ebad87fb1d7bde05f5f55e5877c92440109c1b22232b06de
    docs/notation.qmd:
    78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023
    LARGE_LABEL_ASSESSMENT.md:
    736ad09b8081657373ba98687cc32f52bfdc2db33d46c72c69e5ad85ce977208
    LARGE_LABEL_ASSESSMENT_CHECK.md:
    c3692e1ec1cceb30a49be266769433542572506b97099d0a20c956054f23564a
    GENERAL_SELF_AVERAGING.md:
    bfbc14cbb3cccf902420db74ca6e3627e341f27a84b52a229362848b376a56d5

Both book entry files and all three named study notes were read completely. The manuscript setting, population definition, and all-time theorem statement were read for conventions. Other manuscript sections and the dependencies of GENERAL_SELF_AVERAGING were not needed: none of its concentration conclusions is used to prove the geometry candidate, whose probability estimates are reconstructed directly below. This check does not validate that separate theorem or its dependencies.

Required canonical-notation and rigorous-math instructions were applied. The only shell actions for this check were reading, line counting, and SHA-256 hashing; no numerical experiment or CPU fallback was performed. Only this report is written.

## 1. Arbitrary-label scalar continuation

The mobility is \(M=(n,1,\ldots,1,n)\), and the controlled vector field is the exact dense field with \(2(y-f)dt\) replaced by \(du\). Therefore
\[
w'=h^{(L)},\qquad
P'=\nabla P^\top M\nabla P=\|\theta'\|_{M^{-1}}^2
 \ge \|h^{(L)}\|_2^2/n.
\]
The normalized norm here divides first-weight and readout squares by \(n\), and leaves hidden-matrix Frobenius squares unscaled. The factors are correct for the manuscript's unhalved squared loss.

For \(R=\|w\|_2/\sqrt n>0\), direct differentiation gives \(RR'=P\), and Cauchy–Schwarz gives \((R')^2\le\|h^{(L)}\|_2^2/n\). Hence \(RR''=P'-(R')^2\ge0\). At zero readout, all hidden velocities vanish, \(P'(0)=Q_0\), and \(R'(0+)=\sqrt{Q_0}\). This proves \(P'\ge Q_0\), with no division by zero at initialization.

The continuation argument only needs a bound on \(P\) before the target is reached. If \(P<Y\) up to a putative finite maximal controlled time \(U\), then
\[
\|\theta(t)-\theta(s)\|_{M^{-1}}^2
\le (t-s)\int_s^t\|\theta'\|_{M^{-1}}^2du
\le Y(t-s).
\]
At fixed finite width the parameter space is complete, so the curve has a finite endpoint; the assumed locally Lipschitz vector field continues there. Together with \(P\ge Q_0u\), this proves that \(P=Y\) is reached by \(Y/Q_0\). Cauchy–Schwarz gives the claimed path length \(Y/\sqrt{Q_0}\).

There are \(L+1\) parameter blocks. Passing from their Euclidean sum of squares to the manuscript's sum of normalized block norms costs \(\sqrt{L+1}\), exactly as stated.

The physical clock has \(\dot u=2(Y-P(u))\), so
\[
\frac{d}{dt}(Y-P)=-2P'(u)(Y-P).
\]
This proves the residual exponent \(2Q_0\) and the activity identity \(2\int|r|dt=u_Y\). Sign reversal of \(y,w\) preserves the hidden equations, and the zero-label solution is stationary. Positive \(Q_0\) is essential; the candidate retains it.

The result proves finite-target continuation, not global existence of the unrestricted ascent curve. This distinction is handled correctly. No dynamical population theorem is imported outside its hypotheses.

## 2. Gaussian independence and the exact passive law

Let \(v_0=x_0/\sqrt d\) be unit length. For the deep linear network, every first-matrix update has right factor \(v_0^\top\). Writing \(a(u)=W^{(1)}(u)v_0\), its orthogonal component therefore remains exactly
\[
B=W^{(1)}(0)(I-v_0v_0^\top).
\]
Rowwise Gaussian orthogonal decomposition makes \(B\) independent of \(a_0\) and of all initialized hidden matrices. The training trajectory depends only on these latter variables. Its fitted time is also measurable with respect to them, because it is the unique crossing of a continuous strictly increasing training prediction.

For \(v=x/\sqrt d=cv_0+v_\perp\), linearity gives
\[
f_n(t,x)-cf_n(t,x_0)=k(u(t))^\top Bv_\perp/n,
\]
where \(k=W^{(2)\top}\cdots W^{(L)\top}w\). This verifies the candidate's formulas (8)–(9), including the factor \(n^{-2}\) in the covariance. The whole family is conditionally jointly Gaussian because each member is a linear functional of the same Gaussian matrix \(B\), with training-measurable coefficients.

The event \(G_n\) uses only \(a_0\) and hidden matrices. It does not restrict the unused Gaussian matrix \(B\); conditioning on it preserves the argument. A good event involving the full first-weight Frobenius norm would require additional care, but the candidate correctly avoids that choice.

The initialization proof is sufficient. Conditional on a preceding nonzero feature vector, the next Gaussian matrix produces independent coordinates with variance equal to its normalized squared norm. The next energy is therefore the old energy multiplied by a variable of conditional law \(\chi_n^2/n\). Fixed depth, conditional variance \(2/n\), and a union bound give convergence of the initial energy to one. Taking \(0<q<1\) and a sufficiently large fixed \(K\), the stated net estimate gives \(\Pr(G_n)\to1\).

## 3. Entire-time control and endpoint lower bound

On \(G_n\), the scalar path-length bound controls all normalized training vectors and all trained hidden operator norms by constants depending on \(K,q,L,Y\). For linear activations, forward and backward recursions then control their RMS norms. Each hidden controlled derivative has operator norm bounded by
\[
\|\delta^{(\ell)}h^{(\ell-1)\top}/n\|_{\mathrm{op}}
\le
\frac{\|\delta^{(\ell)}\|_2}{\sqrt n}
\frac{\|h^{(\ell-1)}\|_2}{\sqrt n}.
\]
Differentiating the finite product defining \(k\) gives precisely \(L\) terms, all bounded in RMS. Thus \((\|k\|+\|k'\|)/\sqrt n\le C_{K,q,L,Y}\) holds at arbitrary fixed depth.

Extending \(k\) constantly after its fitted time gives an absolutely continuous function \(\bar k\) on the deterministic interval \([0,S]\), \(S=Y/q\), with \(\bar k(0)=0\). Cauchy–Schwarz yields the supremum bound in the candidate. Conditional independence then gives
\[
\mathbb E_B|\bar k'(u)^\top Bv_\perp|^2
=\|\bar k'(u)\|_2^2\|v_\perp\|_2^2.
\]
After integrating over \(u\), dividing by \(n^2\), and integrating queries, this proves
\[
\mathbb E[\mathbf1_{G_n}\mathcal R_{n,\mu}^2]
\le \frac Cn\int\|v_\perp\|_2^2d\mu.
\]
The time supremum is correctly inside the query integral. A second query moment suffices, and the factor \(S^2\) is legitimately absorbed into a constant depending on fixed \(Y,q\). The \(Y=0\) case is handled separately. Markov and \(\Pr(G_n^c)\to0\) give the claimed fixed-confidence strict root-width bound. No unconditional second moment on the exceptional event is claimed.

At fitting, \(f_n(\infty,x_0)=y\), so the deterministic center in the conditional Gaussian law is exactly \(yx_0^\top x/d\). This identifies the endpoint limit directly, without using a width-dependent concentration center.

For \(y\ne0\), the identity \(y=k_*^\top a_*/n\) and the bound \(\|a_*\|_2/\sqrt n\le M\) imply
\[
\|k_*\|_2/\sqrt n\ge |y|/M.
\]
For a nonparallel query, the conditional standard deviation is consequently at least \(|y|\|v_\perp\|/(M\sqrt n)\) on \(G_n\). If \(\sigma\ge c_*/\sqrt n\), then
\[
\Pr\{|\sigma Z|\ge c_*/\sqrt n\}\ge\Pr\{|Z|\ge1\}.
\]
Integrating this inequality over \(G_n\) gives formula (17). It is an actual canonical lower bound at scale \(n^{-1/2}\); it neither proves nor suggests a slower exponent.

The all-time passive theorem centers at \(c(x)f_n(t,x_0)\), not at the complete canonical population transient. Thus scalar training prediction convergence remains a separate obligation. The candidate states this limit correctly. Endpoint identification alone would not justify exchanging width and infinite time in a general nonlinear population system.

## 4. Exact two-hidden-layer reduction

The normalized controlled equations \(A'=W^\top b\), \(W'=bA^\top\), \(b'=WA\) are correct. Differentiating gives
\[
\frac d{du}(WW^\top-bb^\top)=0,\qquad
\frac d{du}(\|A\|^2-\|b\|^2)=0.
\]
Therefore
\[
b''=b\|A\|^2+WW^\top b
=\left[W_0W_0^\top+
(\|A_0\|^2+2\|b\|^2)I\right]b.
\]
The coefficient 2 is correct, as are \(b(0)=0\), \(b'(0)=W_0A_0\), and \(P=b^\top b'\).

Diagonalize the fixed symmetric matrix \(W_0W_0^\top\). Each coordinate of \(b\) solves the same scalar linear equation apart from its eigenvalue and its initial velocity. It is its initial velocity multiplied by the stated propagator \(\psi(u,\lambda)\). Summing squared coordinates and their products with derivatives proves both spectral formulas, including the candidate's weighted spectral measure. Independence between that measure and \(A_0\) is neither assumed nor needed.

On the training good event, the finite-target tube bounds the shared scalar potential and \(\lambda\in[0,K^2]\). Writing the propagator as a first-order two-dimensional system and integrating its norm inequality gives a width-independent bound over \(u\le Y/q\). This rules out unbounded amplification of an individual fixed initial spectral component on that interval; it does not control the feedback sensitivity to changing the entire random spectral measure. The candidate explicitly leaves that stronger step open.

The closing homogeneous-activation observation is also correct: positive degree-one homogeneity and differentiability at zero force the same linear slope on both rays.

## 5. Limits of this pass and a bounded next diagnostic

The pass covers the scalar continuation theorem, arbitrary-depth linear passive all-time bound, sharp endpoint Gaussian law, and exact two-hidden-layer reduction. It does not cover a nonlinear multi-sample width rate or the supervisor's separately assigned scalar population proof.

The failed scalar trapping attempt suggests one concrete diagnostic, rather than another generic instability example. For a general finite training set, let
\[
\langle a,b\rangle_m=m^{-1}a^\top b,\quad
\rho=\|y-f\|_m,\quad c=(y-f)/\rho,\quad
\frac{ds}{dt}=2\rho
\]
on an interval with \(\rho>0\). Let \(J\) be the matrix of parameter gradients of the training predictions and set \(\Gamma=JMJ^\top/m\). With primes now denoting \(s\)-derivatives, direct substitution gives
\[
\theta'=MJ^\top c/m,\quad
f'=\Gamma c,\quad
\rho'=-\gamma,\quad
c'=(\gamma c-\Gamma c)/\rho,\qquad
\gamma=\langle c,\Gamma c\rangle_m=\|\theta'\|_{M^{-1}}^2.
\]
For \(R=\|w\|_2/\sqrt n>0\), one has
\[
RR'=\langle c,f\rangle_m,\qquad
RR''=\gamma-(R')^2+\langle c',y\rangle_m,
\qquad \gamma\ge(R')^2.
\]
The last identity uses \(\langle c',c\rangle_m=0\) and \(f=y-\rho c\). Thus **rotation of the residual direction is the sole extra term in the scalar readout-convexity calculation**. This is an exact finite-network identity, not a closed population model.

A bounded new theoretical route could specialize this rotation identity to one explicitly specified two-sample nonlinear population trajectory and establish either a signed bound on \(\langle c',y\rangle_m\) or a reachable mechanism making it sufficiently negative. No such trajectory or sign estimate has been constructed here. Without that concrete input, a new broad counterexample search would repeat the existing gap; no additional route file was opened.

## Presentation-only update

After the foregoing check, the source author corrected the one query-decomposition typo. The new source SHA-256 is

    9a728907c452c26b35a26eccdd0de79808eaf5038a4149dbd70f48fd20b90931

The exact change replaces the single occurrence of \(v=x/\sqrt d=c,v_0+v_\perp\) by \(v=x/\sqrt d=c v_0+v_\perp\). I verified the new file hash and used a read-only textual reversal of precisely that replacement; its SHA-256 equals the original frozen hash recorded above. This verifies that there are no other changes. The scientific INTERNAL PASS therefore applies to the corrected source as well. The original version and its cosmetic finding remain recorded here.
