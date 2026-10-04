# Finite Lipschitz programs with a reused fast mixer

Author derivation, 2026-10-02. Status: **internally checked corollary of published universality results; not independently reviewed or promoted.** The proof below supplies the corrected finite-program premise needed by the separate clipping argument. It does not itself prove that the unclipped tanh learner is approximated by such programs. No experiment is a proof input.

The program may learn features, reuse the same matrix and its transpose, retain its full finite history, and use adaptive scalar feedback. Its length, number of coordinate channels, and all deterministic maps are fixed independently of width. The conclusion concerns empirical observables as width tends to infinity, not a numerical rate, a growing training horizon, or an ODE limit.

## The matrix ensembles and typed computation

Let $n=2^b\to\infty$. Distinguish two copies $L_n,R_n$ of $\mathbb R^n$. A vector has one of these two types even though the dimensions agree. Write

\[
 \|v\|_n^2=\frac1n\sum_{i=1}^n v_i^2,
 \qquad \langle v\rangle_n=\frac1n\sum_{i=1}^n v_i.
\]

For several coordinate channels the same norm uses their Euclidean row norm. Compare the Gaussian matrix $W_0^G:R_n\to L_n$, with independent entries $N(0,1/n)$, and

\[
 W_0^F=\Pi_U\mathsf H_n\Pi_E\operatorname{diag}(s_n)
           \Pi_F^\top\mathsf H_n^\top\Pi_V^\top.                 \tag{1}
\]

Here $\mathsf H_n$ is the normalized Hadamard matrix and the four $\Pi$'s are independent uniform signed permutation matrices. They are independent of all initialization. Let $Q$ be the quarter-circle probability law

\[
 Q(ds)=\pi^{-1}\sqrt{4-s^2}\,\mathbf 1_{[0,2]}(s)\,ds.
\]

One admissible exact spectrum is

\[
 t_{n,i}=F_Q^{-1}((i-1/2)/n),\qquad
 c_n^2=n^{-1}\sum_i t_{n,i}^2,\qquad s_{n,i}=t_{n,i}/c_n.      \tag{2}
\]

The theorem also holds for deterministic nonnegative spectra with empirical convergence to $Q$ in every Wasserstein order and a uniform eventual bound on their maximum. Unlike the polynomial-program result, the proof here uses an operator-norm bound.

There are finitely many initial coordinate channels on each side. Their rows are iid vectors with a fixed Gaussian law, permitting a singular covariance, constant coordinates, and duplicate coordinates. The two sides may be taken independent, as in the intended application. They are independent of the matrix. Initial scalar registers are deterministic. A program is a fixed finite ordered list of these instructions:

1. **Local instruction:** form a new vector on one side by applying the same deterministic map to the earlier coordinate channels on that side and to earlier scalar registers.
2. **Matrix instruction:** form $W_0v\in L_n$ from $v\in R_n$, or $W_0^\top u\in R_n$ from $u\in L_n$.
3. **Average instruction:** take an empirical average of a bounded Lipschitz function of finitely many earlier channels on one side.
4. **Scalar instruction:** apply a fixed continuous function to earlier scalar registers. Its domain contains a neighborhood of their recursively obtained finite limits and it is finite there.

Copies and fixed linear combinations are local instructions. There is no coordinatewise operation between opposite sides and no coordinate-dependent map chosen from a row index. Scalar registers may communicate between the sides. There are no width-dependent branching rules, empirical quantiles, or stopping times hidden in this definition.

For clarity, the required regularity of a local map $\phi(x;c)$, with local history $x\in\mathbb R^r$ and scalar registers $c\in\mathbb R^p$, is the following. For every compact set $K$ in its allowed scalar domain there is a finite $L_K$ such that

\[
\begin{split}
 |\phi(x;c)-\phi(x';c)|&\le L_K\|x-x'\|,\\
 |\phi(x;c)-\phi(x;c')|&\le L_K(1+\|x\|)\|c-c'\|,\\
 \sup_{c\in K}|\phi(0;c)|&<\infty,\qquad c,c'\in K .          \tag{3}
\end{split}
\]

Finite-dimensional vector outputs satisfy the same condition. This permits scalar multiplication $cx$; it does not falsely require that multiplication be globally Lipschitz jointly in unrestricted $c,x$. An average test that depends explicitly on scalar registers must obey the corresponding locally uniform Lipschitz condition in them, in addition to being bounded and Lipschitz in its coordinate arguments. Restricting registers to compact neighborhoods of their limits is an eventual property in the proof, not an assumption that their limits are known beforehand.

**Lemma.** For every program just specified and every fixed finite list of bounded Lipschitz empirical tests of its same-side coordinate histories, all scalar outputs and test averages converge almost surely to finite deterministic limits, and these limits agree for $W_0^F$ and $W_0^G$. Continuous functions of finitely many such scalar limits also agree. Both sides may have redundant or initially zero channels. The conclusion holds along Hadamard widths, on any joint construction of the two ensembles that preserves each specified marginal model and its initialization independence.

If a scalar instruction is undefined at finitely many widths, those outputs may be assigned arbitrary values; the neighborhood condition and the causal induction below ensure almost-sure eventual definition. The exceptional null set may depend on the fixed program and tests. This is not a claim uniform over all programs, all Lipschitz constants, or all lengths. The lemma can be weakened to convergence in probability without changing its intended use.

Bounded measurable tests cannot replace bounded Lipschitz tests: take $c_n=n^{-1}\sum_i\tanh(\xi_i)$, broadcast $c_n$ as a constant vector, and test its coordinate with $\mathbf1_{(0,\infty)}$. This average is Bernoulli with probability $1/2$ for each width, although $c_n\to0$. Predictions and bounded feature Gram entries after bounded-state extensions do not have this defect.

## Published input and its verified specialization

Use Wang–Zhong–Fan (WZF), Theorem 2.22, with aspect ratio one. Its matrix must be rectangular generalized invariant in Definition 2.20, have the same limiting diagonal distribution as a bi-orthogonally invariant reference, and have bounded operator norm almost surely eventually. Its independent side roots must satisfy Assumption 2.17: all-order empirical Wasserstein convergence, all moments, polynomial density in their real $L^2$ spaces, and positive second moment of the first left message. Coordinate maps are continuous, of polynomial growth, and Lipschitz in their AMP-history arguments. The prescribed state-evolution covariance matrices must be nonsingular. The conclusion is empirical $W_2$ convergence of roots and AMP fields for every fixed number of steps. [WZF, §§2.3 and D.3](https://arxiv.org/html/2206.13037v5)

Proposition D.1(a,b1) applies to (1) and to independent Haar singular bases with the same all-order singular-value limit. The Hadamard entries have magnitude $n^{-1/2}$. Midpoint Riemann sums in (2) give $c_n\to1$, all-order convergence to $Q$, and $\max_i s_{n,i}\le3$ eventually. The iid Gaussian matrix is bi-orthogonally invariant and its singular-value empirical law converges almost surely in every Wasserstein order to $Q$. A self-contained Wick-pairing proof, including the random-spectrum versus deterministic-quantile distinction and the sampler correspondence, is already given in [POLYNOMIAL_TRANSFER.md](/home/amir/Codes/PDE/studies/response_memory_fast_mixing_20261002/POLYNOMIAL_TRANSFER.md). In brief, $n^{-1}\operatorname{tr}[(W_0^G(W_0^G)^\top)^k]$ has expectation tending to the $k$-th Catalan number and variance $O_k(n^{-2})$; higher moments give uniform integrability, and the compactly supported moment limit is determinate. Thus both ensembles have the required identical limiting diagonal distribution. Matching the ordinary spectrum alone would not imply that property for an arbitrary singular basis.

There is also an elementary eventual operator-norm bound for the Gaussian matrix. Choose $1/4$-nets of both unit spheres, each containing at most $9^n$ points. Bilinear approximation gives

\[
 \|W_0^G\|_{\rm op}\le2\max_{a,b\text{ in the nets}}|a^\top W_0^G b|.
\]

Each fixed bilinear form is $N(0,1/n)$. Consequently

\[
 \mathbb P(\|W_0^G\|_{\rm op}>8)
 \le2\exp\{(2\log9-8)n\},                                  \tag{4}
\]

which is summable. Borel–Cantelli supplies an almost-sure eventual bound, independent of any coupling across widths. For (1), the norm is exactly $\max_i s_{n,i}$. We may use the common eventual bound 8.

The AMP prescriptions for this diagonal law are precisely the Gaussian prescriptions. At aspect ratio one the quarter-circle even moments are Catalan. In the rectangular moment-cumulant relation, taking $\kappa_2=1$ and every higher rectangular cumulant zero leaves exactly the noncrossing pairings, hence precisely those moments. Triangularity of the moment-cumulant relation makes this solution unique. Substitution in Fan's equations (5.12)–(5.13) gives the identities below; his Remark 5.1 states the same Gaussian specialization. [Fan, §2.4 and §5.1](https://arxiv.org/html/2008.11892v5)

In notation used only for the AMP embedding, left and right queried messages are $u_t,v_t$, and AMP fields are $y_t,z_t$. Write their scalar state-evolution limits as $U_t,V_t,Y_t,Z_t$. With left roots $F$ and right roots $G$, the prescription is

\[
\begin{split}
 \Omega_t&=(\mathbb E[U_rU_s])_{r,s\le t},&
 \Sigma_t&=(\mathbb E[V_rV_s])_{r,s\le t},\\
 b_{ts}&=\mathbb E[\partial_s u_t(Y_{1:t-1},F)],&s&<t,\\
 a_{ts}&=\mathbb E[\partial_s v_t(Z_{1:t},G)],&s&\le t.         \tag{5}
\end{split}
\]

Here $Z_{1:t}\sim N(0,\Omega_t)$ is independent of right roots, and $Y_{1:t}\sim N(0,\Sigma_t)$ is independent of left roots. These are uncentered message Gram matrices, not centered message covariances. The Gaussian fields themselves are centered. The prescriptions are causal: $\Omega_t,b_{t\cdot}$ are determined before defining $v_t$, and $\Sigma_t,a_{t\cdot}$ before defining $u_{t+1}$.

## Proof for deterministic scalar registers

First replace all scalar registers used by local maps by fixed finite constants. The resulting program uses only same-side globally Lipschitz operations and matrix actions. Eliminating intermediate local assignments expresses each queried vector as a globally Lipschitz function of its side's roots and previous raw matrix outputs on that side. All stored vectors can be decoded from this history. This elimination involves finitely many compositions.

Serialize the matrix queries into alternating transpose and forward slots. If the next desired query has the wrong direction, insert an ignored slot of the other direction. Prepend an entirely ignored transpose/forward pair. The number $T$ of slots is finite and independent of $n$.

Fix $0<\varepsilon\le1$. Augment the initial roots by independent iid standard Gaussian vectors $\xi_1,\ldots,\xi_T\in L_n$ and $\zeta_1,\ldots,\zeta_T\in R_n$, independent of everything else. At every transpose slot replace the vector actually passed to $W_0^\top$ by the desired vector plus $\varepsilon\xi_t$; at every forward slot use the desired vector plus $\varepsilon\zeta_t$. An ignored slot queries only its noise vector, and its raw result is ignored by the desired computation. For the initial dummy pair,

\[
 u_1=\varepsilon\xi_1,\qquad v_1=\varepsilon\zeta_1.           \tag{6}
\]

This changes only the matrix-query arguments. **A message saved by the original computation remains its unnoised vector.** For example, if the original code computes $h$, saves $h$, and queries $W_0h$, the perturbed program saves the same currently computed $h$ and receives $W_0(h+\varepsilon\zeta_t)$. It does not silently replace every subsequent use of stored $h$ by $h+\varepsilon\zeta_t$. The unnoised value can also be recovered locally by subtracting the known root $\varepsilon\zeta_t$ from the noisy message. Future noise roots are never consumed before their designated slots.

Let $\bar z_t=W_0^\top u_t$ and $\bar y_t=W_0v_t$ denote these raw noisy-query outputs. We now represent this exact perturbed program as an AMP iteration,

\[
 z_t=W_0^\top u_t-\sum_{s<t}b_{ts}v_s,
 \qquad
 y_t=W_0v_t-\sum_{s\le t}a_{ts}u_s.                          \tag{7}
\]

Suppose $u_t$ has already been defined as a deterministic coordinate function of $y_{1:t-1}$ and left roots. Formula (5) determines $b_{ts}$ and $\Omega_t$. Inside the right-side coordinate computation set

\[
 \bar z_t=z_t+\sum_{s<t}b_{ts}v_s.                          \tag{8}
\]

Every $v_s$ here is already a coordinate function of earlier right AMP fields and right roots. Use (8), the earlier decoded right raw outputs, and the right roots to run the desired local instructions and produce $v_t$, adding only its fresh query noise. Formula (5) now determines $a_{ts}$ and $\Sigma_t$. Inside the next left-side computation recover

\[
 \bar y_t=y_t+\sum_{s\le t}a_{ts}u_s,                       \tag{9}
\]

and use the decoded left history to construct $u_{t+1}$. The term $u_t$ on the right of (9) is already defined using $y_{1:t-1}$. Thus no implicit equation is introduced. Every transformed map is globally Lipschitz jointly in its finite AMP history and roots, with constants that may depend on $\varepsilon$ and $T$. Its weak derivatives in the AMP arguments exist almost everywhere and are bounded. We use deterministic expectation coefficients in (5), not empirical derivative estimates.

Equations (8)–(9) imply pathwise that this AMP reproduces the noisy raw-query computation at every finite width. They do not assert that the raw fields are Gaussian. Gaussianity applies to the corrected AMP fields in the width limit.

**Nondegeneracy.** The construction of the state evolution is well defined inductively. Each message limit has finite second moment because the maps are globally Lipschitz and its arguments are Gaussian roots and Gaussian fields of finite covariance. On the right it has the form

\[
 V_t=B_t(Z_{1:t},G\text{ without }\zeta_t,\zeta_{t+1},\ldots)
       +\varepsilon\zeta_t,
\]

where $B_t$ denotes the decoded unnoised message, not a matrix. The Gaussian field vector is independent of all right roots. For a nonzero deterministic coefficient vector $c_{1:t}$, let $r$ be its largest nonzero index. Earlier messages and $B_r$ do not depend on $\zeta_r$. Conditioning on the Gaussian field and every root except $\zeta_r$,

\[
 \mathbb E\left[\left(\sum_{s\le t}c_sV_s\right)^2\right]
 \ge \varepsilon^2c_r^2>0.                                \tag{10}
\]

This proves $\Sigma_t$ positive definite. The identical argument with $\xi_r$, using independence of the left Gaussian field from left roots, proves $\Omega_t$ positive definite. In particular $\mathbb E U_1^2=\varepsilon^2>0$. No lower bound uniform as $\varepsilon\downarrow0$ is needed.

**Root hypotheses.** The dummy first pair ensures that $(u_1,F)$ itself is Gaussian plus constants even if the first desired message is a nonlinear function of roots. It may contain the duplicated coordinate $\xi_1$; this is harmless. For every root monomial, Chebyshev's inequality gives a deviation bound $O(1/n)$, summable along $n=2^b$. A countable intersection gives almost-sure convergence of all mixed moments. Tightness, moment determinacy of a Gaussian law, and higher-moment uniform integrability give empirical convergence in every Wasserstein order.

Polynomials are dense in $L^2$ of a possibly degenerate Gaussian law. For a standard Gaussian vector, if $f\in L^2$ is orthogonal to every polynomial, the function $z\mapsto\int f(x)e^{z\cdot x}\,d\gamma(x)$ is entire by Cauchy–Schwarz and Gaussian exponential integrability. All its derivatives at zero vanish, so it vanishes identically. Its restriction to imaginary arguments is the Fourier transform of the finite signed measure $f\,d\gamma$, hence that measure is zero and $f=0$. A Gaussian law with constants and duplicates is an affine image of a nondegenerate Gaussian on its support; a linear inverse on that support transfers the density assertion. Initialization remains independent of the matrix after adding the noises.

All hypotheses of WZF Theorem 2.22 are now verified for each fixed $\varepsilon>0$. It supplies the same deterministic $W_2$ limit of the AMP roots and fields for both ensembles. Decoding any finite list of same-side stored histories is a globally Lipschitz map at fixed $\varepsilon$, so their empirical laws also converge in $W_2$. In particular every bounded Lipschitz empirical test has a common deterministic limit, denoted $\ell_\varepsilon$.

## Removing the auxiliary noise in the raw program

This step compares the two **raw computations**, not their AMP Onsager coefficients or their state-evolution covariance inverses. Couple a noisy computation and the original computation by using the same matrix and original roots. Let $E_j$ be the sum of normalized Euclidean errors of all stored vector channels after instruction $j$. On $\|W_0\|_{\rm op}\le C$, a local instruction of Lipschitz constant $L_j$ increases the error by at most $L_jE_{j-1}$. A matrix instruction increases it by at most

\[
 C E_{j-1}+C\varepsilon\|\eta_j\|_n,                        \tag{11}
\]

where $\eta_j$ is its fresh noise vector. Copies and ignored queries satisfy the same bound. Therefore, for a fixed program of $N$ instructions,

\[
 \max_{j\le N}E_j
 \le K\varepsilon\sum_{r\le2T}\|\eta_r\|_n,                 \tag{12}
\]

where $K$ depends on $C$ and the original program's finitely many Lipschitz constants, and is independent of $n$ and $0<\varepsilon\le1$. Each Gaussian noise norm tends almost surely to 1. The auxiliary messages and the stored unnoised messages were distinguished precisely so that (11) compares the intended program.

For a bounded Lipschitz test $g$, Cauchy–Schwarz gives

\[
 |\langle g(X^\varepsilon)\rangle_n-\langle g(X^0)\rangle_n|
 \le\operatorname{Lip}(g)\|X^\varepsilon-X^0\|_n.
\]

Take a countable sequence $\varepsilon_k\downarrow0$ and the intersection of its probability-one AMP events, root events, noise-norm events, and eventual matrix-norm event. On it,

\[
 \limsup_n|O_n^0-\ell_{\varepsilon_k}|\le K_g\varepsilon_k.  \tag{13}
\]

Using the same zero-noise output between two approximants shows

\[
 |\ell_{\varepsilon_k}-\ell_{\varepsilon_l}|
 \le K_g(\varepsilon_k+\varepsilon_l).
\]

The deterministic limits are Cauchy. Their limit $\ell$ is common to the two ensembles, and (13) implies $O_n^0\to\ell$ almost surely. A finite list of tests is handled by intersecting finitely many such events. Although auxiliary roots were used in the proof, the zero-noise output is measurable with respect to the original model, so its almost-sure convergence holds under the original model as well. This proves the lemma with deterministic scalar registers.

## Adaptive scalar feedback

Consider the average instructions in their finite causal order. Before the first, all scalar registers are deterministic, so the preceding result gives a deterministic common limit for that average. Every subsequent continuous scalar instruction then has a finite deterministic common limit, provided its domain condition holds.

Suppose this is proved for all averages and scalar registers before the next average. Compare the actual prefix with the prefix obtained by replacing those scalar values everywhere by their deterministic limits. The vector channels of the frozen prefix have uniformly bounded normalized Euclidean norms eventually: the roots do, matrix instructions multiply a norm by at most 8, and each local instruction obeys uniform linear growth from (3). The same bound holds for the actual prefix, since its finitely many scalar values converge and therefore eventually belong to compact neighborhoods of their limits.

For a local instruction its additional error from freezing is bounded, by (3), by

\[
 L_K\|X-X'\|_n+
 L_K(1+\|X'\|_n)\|c_n-c\|,                                \tag{14}
\]

with a harmless fixed constant if several channels are present. Matrix instructions are bounded linear maps. A finite induction therefore makes every actual-versus-frozen vector error tend to zero. The same estimate for an average test implies that its actual and frozen averages differ by $o(1)$. The frozen prefix is covered by the already-proved deterministic-register result; thus the next actual average has its deterministic common limit. Continuity then handles the following scalar instructions. This induction ends after finitely many averages, proves the conclusion for all requested final tests, and proves the lemma. No independence between a feedback coefficient and the matrix-dependent vectors was assumed.

## What the proof import contains

The external source proofs were inspected beyond theorem statements. WZF's actual path is Theorem 2.22 through D.4 and D.9, with matrix classification D.1. Its D.4 rectangular approximation proof explicitly refers to the symmetric approximation argument and omits the repeated rectangular details. The complete §3.3 argument, including Lemmas 3.10–3.14, was read, as were complete D.3 and Appendix A. Its approximation step chooses polynomials in $L^2$ under the corresponding Gaussian state evolution, uses Stein's identity and nonsingular covariance to control expected derivatives and Onsager coefficients, and uses bounded operator norm plus the original maps' Lipschitz bounds to transfer the polynomial approximation to the actual iteration. The two rectangular half-steps use the same estimates in their causal order. This is the published proof import, not an inference from the theorem title.

For this specialization the roots and the polynomial-AMP Gaussian fields have a jointly Gaussian law, possibly with degenerate root coordinates. Hence moment determinacy in the polynomial-to-law step follows directly from Gaussian exponential integrability. We do not rely on an unsupported assertion that polynomial density alone makes every arbitrary measure moment-determinate. The density product lemma in WZF Appendix A was also read in full.

For the state-evolution input behind that approximation, Fan's complete rectangular proof Appendix B, including the preamble and Lemmas B.1–B.4, was read. This includes the partial-moment recursions, block identities, conditioning induction, and nondegeneracy argument. The symmetric conditioning argument in Appendix A.3, to which the rectangular proof refers for repeated manipulations, was also read completely. Appendix E (E.1–E.5) and the Haar auxiliary results F.1–F.2 were read completely. The proof requires polynomial-growth functions and their derivatives for the auxiliary polynomial AMP; the approximating polynomials satisfy these conditions. Small dependence of each auxiliary polynomial on its newest AMP coordinate can enforce Fan's nondegeneracy condition. The quarter-circle law has positive variance and second moment, so the spectral nondegeneracy assumptions hold. WZF then removes the derivative-continuity restriction for the target Lipschitz maps by its approximation argument.

**Version correction.** The initial Fan reading used arXiv v3. Its finite-dimensional Haar-conditioning display used a projected full-dimensional Haar matrix, which is not the exact conditional law. The latest arXiv version is v5. Every change in the relevant §§2.4, 5, Appendix B, Appendix E, and F.1 was compared; the changed conditioning formulas and complete revised F.1–F.2 proof were read. Version v5 uses the correct Haar matrix on the remaining orthogonal complement. All final Fan citations in this note refer to v5. The spectral prescriptions in §5 are unchanged. WZF was also first read in v3 and then reconciled with its published-version v5: every change in §1.2, §2.3, §§3.1–3.3, Appendix A, Appendix B, and Appendix D was inspected. The relevant theorem hypotheses, numbered lemmas, and proof arguments are unchanged apart from clarifications, formatting, and equation renumbering. Final WZF citations here use v5; the earlier polynomial note records its original v3 reading. The source's polynomial-growth composition bound in E.2 should use an order at least the product of the growth orders; the all-order moment hypotheses used here make that harmless exponent correction sufficient.

The exact Haar conditioning identity needed in that proof can also be justified without an unread external result. If $O Y=X$ for full-column-rank $X,Y\in\mathbb R^{n\times k}$ with $X^\top X=Y^\top Y$, the prescribed isometry on their spans is $X(Y^\top Y)^{-1}Y^\top$. Choose orthonormal complement bases $B_X,B_Y$. Every orthogonal extension has the unique form

\[
 O=X(Y^\top Y)^{-1}Y^\top+B_X R B_Y^\top,
 \qquad R\in\mathbb O(n-k).
\]

Haar invariance under the stabilizers of the two spans makes the conditional law of $R$ invariant under independent orthogonal changes of these complement bases. The unique invariant probability is Haar on $\mathbb O(n-k)$. This proves the F.1 identity used in the conditioning induction. Consequently the separately cited Rangan–Schniter–Fletcher conditioning lemma need not be an unread theorem dependency here. Gaussian Stein identities for the target Lipschitz maps follow by smooth convolution, ordinary Gaussian integration by parts with cutoffs, and dominated convergence using the bounded weak derivatives and Gaussian moments. No separate Sobolev reference is required for this specialization.

For WZF D.9 and D.1, the complete reading already recorded in POLYNOMIAL_TRANSFER.md includes D.10–D.12; Lemmas 3.3, 3.6, 3.7, 3.9 and their proofs; D.2; Appendix B; and Proposition 2.7's proof. These establish the tree moments and generalized invariance required by D.4. Their Haar entry bound is supplied directly in that note. Thus there is no remaining unread heavy proof dependency needed for the stated Gaussian/quarter-circle specialization. Standard finite-dimensional linear algebra, Gaussian integration, moment convergence, and elementary probability principles are used as specified in the proof. This is an author check of the reduction and its imports, not an independent verification of every published algebraic identity.

## Scope for the response-memory learner

The lemma accommodates finite fixed $m,d,J$, vector-valued sample channels represented as finitely many scalar coordinate channels, initially zero readout and backward moments, fixed-step Heun staging, bounded empirical residual feedback, and inverse-clock feedback on a domain bounded away from zero. Applying it to a particular learner still requires checking that its local maps satisfy (3). For the actual tanh learner the unbounded backward-credit product is the reason a separate clipping argument is needed; this note does not replace that argument.

The same finite-program theorem applies to an explicitly unrolled dense finite-history learning algorithm whenever its maps meet the same conditions or admit a justified approximation. Universality is therefore not exclusive to a bounded response-memory representation. The potential distinction concerns the representation and computational cost as the number of training steps grows; this theorem keeps that number fixed and establishes neither an exclusive learning advantage nor a long-time approximation guarantee. The fast prescribed-spectrum construction and AMP universality are prior results. The contribution here is the explicit reduction with adaptive feedback and a verified treatment of zero and redundant channels.
