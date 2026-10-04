# An autonomous population-interaction and response-memory construction

Research synthesis, 2026-09-30. This continues the current study under the user's clarified requirement: subquadratic **evolving** learned state, with two orders, and no concurrently trained dense driver. No paper changes, experiments or promotion are part of this note.

The construction meets the state and autonomy requirements. A width-uniform population-source approximation theorem is proved below. The full width-uniform, matched-prediction-accuracy theorem remains open. In particular the rate of the source approximation must not be advertised as the rate of the autonomous predictor.

## 1. The object worth compressing

For fixed depth L and width n, use

\[
h_1=\phi(W_1x/\sqrt d),\quad h_\ell=\phi(W_\ell h_{\ell-1}),
\quad f=w^Th_L/n,\quad r=f-y.
\]

The backward fields exclude the residual:

\[
\delta_L=w\odot\phi'(z_L),\qquad
\delta_\ell=\phi'(z_\ell)\odot W_{\ell+1}^T\delta_{\ell+1}.
\]

Under canonical squared-loss scaling,

\[
\dot W_1=-2E[r\delta_1x^T/\sqrt d],\qquad
\dot w=-2E[rh_L],\qquad
\dot W_\ell=G_\ell:=-\frac2nE[r\delta_\ell h_{\ell-1}^T],\quad \ell\ge2.
\tag{1}
\]

All expectations may be over any finite weighted dataset or a continuous probability law. The input population affects each hidden learned matrix through the cross interaction G, not through every individual response function separately. The proposed p is the number of directions used to represent this current cross interaction. It need not scale with the number of data points and does not mean low Fourier degree or a fixed feature dictionary.

This remains a low-rank representation of an interaction matrix. What changes is **which** object receives a rank budget and why its tail should decay. We do not assume every response field has low rank, or that the accumulated trained matrix keeps rank p. Over time its directions can rotate; q remembers their evolution.

## 2. An actual finite-state construction

For each hidden layer, fix an n-by-p independent Gaussian probe matrix Omega. At the current reconstructed network state, compute

\[
J=G\Omega,\quad A=J(J^TJ+\lambda I)^{-1/2},\quad B=G^TA,
\qquad \lambda>0.
\tag{2}
\]

Then AB^T is a rank-at-most-p approximation of G. The ridge term makes these factors smooth even at singular-value crossings. Both factors vanish at zero-readout initialization. Their neuron-space directions change as the reconstructed network changes.

Neither G nor a learned dense matrix is stored. For any thin V and U,

\[
GV=-\frac2nE[r\delta(h^TV)],\qquad
G^TU=-\frac2nE[rh(\delta^TU)].
\tag{3}
\]

These are streamed averages of current forward/backward evaluations. The exact initialized matrix and its transpose are always used. All responses come from the compressed model itself.

Let ell_k(u)=sqrt(2k+1) P_k(2u-1), the orthonormal shifted Legendre basis on [0,1]. For k=0,...,q-1 retain n-by-p matrices U_k,V_k satisfying

\[
\dot U_k=\sqrt{2k+1}A-\frac1t\left[kU_k+
\sqrt{2k+1}\sum_{j<k}\sqrt{2j+1}U_j\right],
\tag{4}
\]

and the same equation for V with source B. Their exact definitions are

\[
U_k(t)=\int_0^t A(s)\ell_k(s/t)ds,\qquad
V_k(t)=\int_0^t B(s)\ell_k(s/t)ds.
\]

Use

\[
\widehat W_\ell=W_{\ell,0}+\frac1t\sum_{k<q}U_{\ell,k}V_{\ell,k}^T.
\tag{5}
\]

W1 and w follow (1) evaluated on this same reconstructed network. Add the clock tdot=1. Equations (2)--(5) then define an autonomous system. The integral definitions specify its regular startup at t=0; both factors initially vanish. Every future test input can be evaluated through the resulting network without storing its own history.

This version uses physical-time moments to give a transparent exact construction. It does not silently inherit the old or joint activity clock's theorem. An activity reparametrization needs consistent factor rescaling and a fresh regularity estimate.

For fixed p and positive lambda, the finite-dimensional source maps are locally Lipschitz under bounded C_b^2 activation and bounded input/label assumptions. The integral map is a contraction on a sufficiently short interval and agrees with the finite ODE for t>0. Fixed-p, fixed-lambda temporal convergence can be proved by the comparison below. Global well-posedness for every arbitrary finite q is not asserted merely from these local facts.

## 3. Counted state and work

Moment state is 2(L-1)npq numbers. Including the trained first layer, readout and temporary source algebra gives

\[
O(Lnpq+nd+Lp^2+Lnp+n).
\tag{6}
\]

For 1<=p<=n and q>=1 this is O(Lnpq+nd). The correction rank is at most pq. Strictly subquadratic hidden learned state requires pq=o(n); including the first layer requires d=o(n). The fixed Gaussian matrices still have O(Ln^2+nd) storage if explicitly stored. Probe matrices use O(Lnp) immutable storage.

With N integration points per source evaluation, a streamed implementation has arithmetic cost

\[
O\!\left(N[L(n^2+npq)+nd]+L(np^2+p^3+npq)\right).
\tag{7}
\]

Two passes suffice for (2)--(3); the second uses the A computed after the first. Constants cover forward and backward evaluations. Prefix sums evaluate (4) in O(Lnpq), not O(Lnpq^2). No N-by-n activation table is required when examples are streamed.

A continuous law needs computable integration or sampling access. N and integration error are separate numerical costs; finite learned state is not finite-cost exact access to an arbitrary measure. A finite dataset can be streamed exactly, with N=m and no m-dependent learned state. A sampling implementation requires its own adaptive numerical-error analysis.

## 4. A proved reason the population source can be economical

Use normalized input distance d_X(x,x')=||x-x'||/sqrt(d). Define

\[
Q_p=\inf_{c_1,\ldots,c_p}E\min_jd_X(x,c_j)^2.
\]

Suppose b(x)=h_(ell-1)(x)/sqrt(n) is L_b-Lipschitz, and a(x,y)=-2r delta_ell/sqrt(n) has L2 norm at most M_a. Then G=E[ab^T] satisfies

\[
\boxed{\inf_{\operatorname{rank}Z\le2p}\|G-Z\|_F
\le M_aL_b\sqrt{Q_p/(p+1)}.}
\tag{8}
\]

Proof: assign inputs to p nearest-center cells and let bbar be the conditional mean of b in each cell. The matrix C=E[a bbar^T] has rank at most p. The remainder R=E[a(b-bbar)^T] has nuclear norm at most M_a L_b sqrt(Q_p), by the conditional-mean least-squares property and Cauchy--Schwarz. Its best rank-p approximation has Frobenius error at most ||R||_*/sqrt(p+1), because the sum of the discarded squared singular values is bounded by sigma_(p+1)||R||_* <= ||R||_*^2/(p+1). Adding that approximation to C proves (8). Take near-optimal centers if the infimum is unattained.

The centers are a proof device. The construction (2) stores no geometric mesh and does not approximate arbitrary functions pointwise on it. The extra p^(-1/2) is a spectral benefit of the cross interaction, not a claim about the accuracy of p-point quadrature.

For zero readout, finite label second moment Y^2, bounded activation/derivative, and normalized Gaussian operator bounds, exact dense loss dissipation gives

\[
\int_0^T\!\left[\|\dot W_1\|_F^2/n+
\sum_{\ell\ge2}\|\dot W_\ell\|_F^2+\|\dot w\|^2/n\right]dt\le Y^2.
\]

It bounds hidden operator growth, normalized readout magnitude, and normalized forward input Lipschitz constants independently of n. Therefore M_a<=C_(L,T)rho(t) and L_b<=C_(L,T), for every hidden layer. Full constants and proof are in SOURCE_GEOMETRY.md. No backward input derivative or teacher derivative is required. Bounds are on each fixed time interval, not all time.

For input laws with Q_p^(1/2)<=D p^(-1/s), (8) gives

\[
\inf_{\operatorname{rank}Z\le p}\|G_\ell(t)-Z\|_F
\le C_{L,T}\rho(t)\,p^{-\beta},\qquad
\beta=\tfrac12+\tfrac1s.
\tag{9}
\]

Any probability law supported on a bounded Lipschitz s-dimensional parametrized set, or finitely many such charts, has this quantization property. It can have infinitely many inputs. The exponent uses intrinsic support dimension, not the ambient vector length. No smooth density is needed. A curve gives beta=3/2; a surface gives beta=1. A generic full-dimensional cube instead uses s=d. A simple teacher alone does not imply low input-support dimension or this stronger rate.

## 5. Connection to the concrete sketch and temporal order

For fixed G independent of the extra Gaussian probe, elementary ridge least squares gives, for k<p-1,

\[
E_\Omega\|G-AB^T\|_F^2
\le\left(1+\frac{k}{p-k-1}\right)
\sum_{j>k}\sigma_j(G)^2+\lambda\frac{k}{p-k-1}.
\tag{10}
\]

INTERACTION_BASIS_ROUTE.md proves this using a trial inverse of the leading Gaussian row block, including the needed inverse chi-square expectation. Constant-factor oversampling combines (9) and (10) into a mean-square source estimate O(p^(-2 beta)+lambda) on the dense reference trajectory. The exact reference does not depend on the extra probes. On the probe-dependent surrogate path, one must use a comparison argument instead of falsely asserting independence.

For given differentiable factor histories with ||Adot||F<=K_A and ||Bdot||F<=K_B, Legendre orthogonality gives

\[
\left\|\int_0^t AB^Tds-\frac1t\sum_{k<q}U_kV_k^T\right\|_F
\le\frac{t^3K_AK_B}{6q(q+1)}.
\tag{11}
\]

Only the product of the two omitted histories remains; the two mixed products vanish. The derivative-weighted Legendre tail bounds supply (11). This is a fixed-history estimate. Its constants depend on the particular source factorization.

There is also a finite-horizon trajectory comparison with constants independent of q: L2 contraction of temporal projection bounds the difference of reconstructions from two parameter paths by C sqrt(t) times the L2-in-time parameter difference. Gronwall on the squared error yields

\[
\sup_{t\le T}\|\widehat\theta(t)-\theta(t)\|
\le\sqrt2 e^{C^2T^2}
(\varepsilon_{\rm source}+\varepsilon_{\rm memory}+\varepsilon_{\rm integration}).
\tag{12}
\]

Here C is a local bound for the source-factor and outer-gradient maps in the canonical metric, and defects are evaluated on the exact path. A small-right-side exit-time argument closes the common-region condition. This is a complete conditional finite-n comparison, not a width-uniform theorem: C and K_A,K_B may depend on n,p,lambda. Reducing lambda to achieve (10)'s desired source accuracy can worsen them. Neither (9) nor the old finite-dataset moment theorem removes this new dependence automatically.

## 6. What would constitute the requested success

The intended full theorem would bound predictor discrepancy by C_T(p^(-beta)+q^(-alpha)+integration error), with C_T independent of n,p,q, under explicit data and initialization assumptions. Equation (12) has not established that stronger statement.

If it were proved, epsilon accuracy would permit p~epsilon^(-1/beta), q~epsilon^(-1/alpha). At a common width n, subquadratic hidden state then requires epsilon^(-1/beta-1/alpha)=o(n). If a separate dense population approximation theorem supplies n~epsilon^(-2), the criterion becomes

\[
1/\beta+1/\alpha<2.
\tag{13}
\]

For alpha=2 and curve data, this would give p~epsilon^(-2/3), q~epsilon^(-1/2) and learned state O(epsilon^(-19/6)) at that illustrative width, versus dense O(epsilon^(-4)). For surfaces the prospective exponent is 7/2. With beta=1/2+1/s, the strict power-count criterion is s<6. These are feasibility calculations, not proved compression-versus-accuracy corollaries: both the uniform trajectory rate and the specified dense width rate remain extra obligations.

There is a further distinction for an all-time theorem. A positive finite-data Gram gap does not automatically extend to a positive gap on an infinite-dimensional population L2 space. To see the obstruction without a spectral citation, let an initial kernel be K(x,x')=<g(x),g(x')> in a Hilbert feature space with E||g||^2<infinity. For any finite orthonormal input family e_1,...,e_M, vector-valued Bessel gives

\[
\sum_{j=1}^M\langle e_j,Ke_j\rangle
=\sum_{j=1}^M\|E[g e_j]\|^2\le E\|g\|^2.
\]

If K>=lambda I with lambda>0 on the entire input L2 space, the left side is at least M lambda, a contradiction as M grows. A population all-time extension must therefore use a restricted observable/task space, quantitative target alignment with the kernel spectrum, evolving-feature coercivity, or a different stability mechanism. Smooth labels alone with no specified quantitative class do not supply that missing estimate. This is an obstruction to directly recycling a finite-data gap argument, not an impossibility theorem for population learning or compression.

## 7. Alternatives and scientific position

Three routes were developed independently before cross-checks. QUADRATURE_ROUTE.md gives autonomous causal history panels on p sampled inputs, and p^(-1/2) population-source concentration. Its deep stability hypothesis remains open, and its generic rate is too weak for the preceding matched-accuracy savings. REGULAR_TASK_ROUTE.md proves exact population reductions for homogeneous networks on finitely many rays and polynomial networks on low-dimensional input support. These are useful special classes, not a broad smooth-activation solution.

The source-mode construction is the preferred candidate because it combines genuine autonomy with the stronger geometry-to-interaction estimate (8). It is not yet evidence that all simple high-dimensional teachers admit efficient population encoding.

Adaptive low-rank differential equations and singular-value-robust integration are established ingredients: Lubich and Oseledets, *A projector-splitting integrator for dynamical low-rank approximation*, https://arxiv.org/pdf/1301.1058; Kieri, Lubich and Walach, *Discretized dynamical low-rank approximation in the presence of small singular values*, https://doi.org/10.1137/15M1026791 (full text https://www.diva-portal.org/smash/get/diva2:874116/FULLTEXT01.pdf). Both full texts were read. The latter's main error theorem assumes bounded/Lipschitz dynamics and a small non-tangent component; it does not provide the needed neural width-uniform constants or derive a suitable rank budget from teacher simplicity. No priority claim for low-rank dynamics, Gaussian range sketches, or polynomial moment algebra is made here.

SOURCE_GEOMETRY_CHECK.md records the internal source-theorem check and corrections. INTERACTION_BASIS_CHECK.md records the completed internal construction check; its minor qualifications and rendering corrections are incorporated. These are within-study checks, not established-book promotion. No numerical validation was performed.
