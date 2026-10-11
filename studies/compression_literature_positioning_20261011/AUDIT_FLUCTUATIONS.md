# Independent audit: Pham–Nguyen (NeurIPS 2021)

Source: *Limiting fluctuation and trajectorial stability of multilayer neural networks with mean field training*, Huy Tuan Pham and Phan-Minh Nguyen. Frozen inputs: `data/generated/compression_literature_positioning_20261011/meanfield/pham_nguyen_2021_main.pdf` (13 pages) and `pham_nguyen_2021_supp.pdf` (45 pages, printed pages 14–58), with their text extractions. Audit date: 2026-10-11.

This is a fresh, source-first, venue-neutral audit. The complete main paper and supplement were read. Important equations were also checked visually on main p. 6 and supplement pp. 16, 33, 40, 52, 54. No submitted code, training, or numerical experiment was executed. The requested single report combines the evidence record, claim ledger, severity analysis, and review. Full reading is not a claim of independent reconstruction of every technical estimate.

## Assessment

The decomposition into sampled-neuron fluctuations and a linear response of mean-field weights is mathematically substantive. It is genuinely coupled to the finite network's sampled neurons. It should not be described as merely an uncoupled central limit law. However, the supplied proofs do not justify treating every advertised quantitative and long-time result as independently verified:

1. The scalar variance recursion on main p. 6 is false in a bounded three-layer example; the fuller appendix covariance construction avoids this error.
2. Lemma 12 is false for the pair-valued index permitted by the supplement. In addition, the sensitivity estimate proved in Lemma 31 only gives an `O(N^{-1/4})` error through Lemma 12, whereas Lemma 31 asserts `O(N^{-1/2})`. This affects the advertised second-order finite-width rate.
3. Lemma 38's uniform bound for the *weight* fluctuation is false even within the paper's hypotheses. An explicit infinite-rank, stationary, two-layer example is given below. The long-time proof subsequently also asserts a uniform weight-fluctuation bound and uses an invalid backward variation-of-constants identity. These are substantive gaps in the supplied proof of Theorem 10. They do not establish that Theorem 10's output-variance conclusion is false.

The stationary output-semigroup argument behind Theorem 9 survives independent reconstruction at the limiting-process level. The finite-horizon fluctuation construction remains a strong relevant contribution, with the quantitative coupling proof requiring repair.

## Exact model and quantifiers

The source's (L) counts all weight layers, including the scalar readout; there are (L-1) hidden layers. Let (N_1=\cdots=N_{L-1}=N), (N_L=1), and (x\in\mathbb R^d). At finite width,

\[
H_1^N(t,j,x)=w_1^N(t,j)\cdot x,\qquad
H_i^N(t,j,x)=\frac1{N_{i-1}}\sum_k w_i^N(t,k,j)\varphi_{i-1}(H_{i-1}^N(t,k,x)),
\qquad f_N(t,x)=\varphi_L(H_L^N(t,1,x)).
\]

The continuum version replaces each neuron average by integration over a probability space \((\Omega_i,P_i)\), with \(\Omega_0=\Omega_L=\{1\}\). Its weights are functions \(w_i(t,c_{i-1},c_i)\), its preactivations are \(H_i(t,c_i,x)\), and its output is \(f(t,x)\).

Both systems follow continuous-time population gradient flow for \(\mathcal L=\mathbb E_{X,Y}\ell(Y,f(X))\). The source uses *width-rescaled parameter derivatives*. In ordinary finite-network parameter coordinates the mobility is \(N_{i-1}N_i\) for (i>1), and (N_1) for the first layer. Thus the displayed ODE is not ordinary gradient flow with a common unscaled learning rate for every matrix entry. There is no mini-batch/data-sampling noise in the theorem.

Assumption 1 (main pp. 4–5): bounded inputs; bounded hidden activations; bounded, Lipschitz first and second activation derivatives; bounded, Lipschitz first and second loss derivatives in the prediction; sub-Gaussian marginal initialization moments; separable \(L^2(P_i)\); equal hidden widths. These conditions exclude ReLU as stated and exclude the globally unbounded derivative of squared loss unless an additional localization argument is supplied. Smooth Huber-type losses and tanh are examples. No convexity of the loss is required for the finite-time statements.

Initialization is coupled by independently sampling neuron labels \(C_i(j)\sim P_i\) and setting

\[
w_i^N(0,j,k)=w_i^0(C_{i-1}(j),C_i(k)),\qquad w_i(0,c,d)=w_i^0(c,d).
\]

This permits correlated weight arrays through shared neuron labels. One must check a proposed iid-edge construction and its probability-space regularity rather than infer that every ordinary Gaussian parameterization is covered. The normalization remains (1/N), regardless of which initialization is encoded.

The sampled mean-field network \(\widetilde f_N\) evaluates the *continuum trajectory* on those same sampled labels. The paper defines

\[
\widetilde G^y_N=\sqrt N(\widetilde f_N-f),\qquad
\widetilde G_i^w=\sqrt N(D_i\widetilde f_N-D_if),\qquad
\mathcal R_i^N=\sqrt N\{w_i^N-w_i(C_{i-1},C_i)\}.
\]

Here (D_i f) denotes the source's rescaled derivative. The response (R_i(G,t,c,d)) starts at zero and solves Eq. (3), with the complete ordinary/local derivative terms in supplement Eq. (6). It is linear in the forcing (G), although its coefficients depend on the nonlinear mean-field trajectory. The output correction is

\[
V_N(t,x)=\widetilde G_N^y(t,x)+\sum_i\mathbb E_C[R_i(\widetilde G_N,t,C_{i-1},C_i)D_if(t,C_{i-1},C_i,x)].
\]

Theorem 5 claims, for each (t\le T<\infty),

\[
\mathbb E\mathbb E_J|\mathcal R_i^N(t,J)-R_i(\widetilde G_N,t,C(J))|^2\le K_T/N.
\]

Theorem 6 and supplement E.2 claim

\[
\sqrt N(f_N-f)=V_N+O_T(N^{-1/2})
\]

in the supplement's mean-square convention, hence an unscaled output RMS remainder (O_T(N^{-1})). This is a *claimed sample-coupled correction*, not just a Gaussian draw. The asymptotic Gaussian replacement (G) is a different, distributional step, with polynomial-moment discrepancies (N^{-1/8+o(1)}). The proof defects below prevent this audit from certifying the sharper coupling remainder.

The bounds are on each fixed finite horizon with horizon-dependent constants. The displayed estimates put the time supremum outside the expectation or apply at each (t\le T); they should not silently be promoted to an expected supremum trajectory norm. Theorem 6's explicitly specified tests are moments integrated against bounded functions of the input. A path-space topology and a uniform-in-time endpoint coupling are not established by that displayed moment bound alone.

For long time, (V^*(t)=\lim_{N\to\infty}N\mathbb E_X\operatorname{Var}(f_N(t,X))). The limit order is width first, then time. Assumption 2 requires the conditional expected loss curvature at a conditional stationary prediction to be a positive constant. Theorem 9 assumes initialization is conditional-risk stationary. Theorem 10 assumes

\[
\int_0^\infty t^{2+\delta}\left\|\mathbb E[\partial_2\ell(Y,f(t,X))\mid X]\right\|_{L^2(P_X)}\,dt<\infty
\]

for some \(\delta>0\). This is a strong convergence-rate hypothesis, not a rate proved for arbitrary training. Neither theorem supplies relative error divided by the *realized* seed discrepancy, exchanges (N\to\infty) with (t\to\infty), or controls a fitted finite-width endpoint uniformly in width.

## Checked calculations and concerns

### L1: the main-text scalar variance recursion omits covariance

At (t=0), take (L=3,d=1,X=1), independent Rademacher labels (C_1,C_2), (w_1(C_1)=C_1), (w_2(C_1,C_2)=1), (w_3(C_2)=C_2), tanh hidden activations, and identity readout. Put (a=\tanh(1)>0). Then (H_2=H_3=f=0), while

\[
\widetilde f_N=\overline C_2\tanh(a\overline C_1),\qquad
N\mathbb E\widetilde f_N^2\le N\mathbb E\overline C_2^2\,a^2\mathbb E\overline C_1^2=a^2/N\longrightarrow0.
\]

The main p. 6 recursion instead gives (v_2=a^2) and (v_3=\mathbb E C_2^2\,v_2=a^2). All variables are bounded, the spaces are finite, and a smooth Huber-type loss meets Assumption 1. This is an in-scope contradiction, not a scaling objection.

The correction retains cross-label covariance: if (A_i(c)=w_i(c,c_i)\varphi'_{i-1}(H_{i-1}(c))), the propagated contribution is

\[
\mathbb E_{c,c'}[A_i(c)A_i(c')\operatorname{Cov}(G_{i-1}^{\widetilde H}(c),G_{i-1}^{\widetilde H}(c'))],
\]

not \(\mathbb E_c[A_i(c)^2\operatorname{Var}(G_{i-1}^{\widetilde H}(c))]\). Appendix B.3, pp. 23–24, does preserve the full Gaussian process and linear integral recursion; it yields zero in this example. Severity: **minor flaw in the displayed explanatory formula**, since the appendix provides the required repair and the central process need not be abandoned.

### M1: pair sampling and the Lemma 31 exponent do not support Theorem 5's rate

Appendix A allows the bold index to mean either one neuron label or the pair of adjacent layer labels. Lemma 12 (pp. 16–17) asserts RMS error (O(N^{-\alpha/4}+N^{-|i|/2})) when replacing the empirical average of a sample-dependent function by its population average, with a one-replacement mean-square sensitivity (O(N^{-\alpha})).

For a pair index, take (f(S,c,d)=c), where (c\) is Rademacher and (f) is independent of (S\). Sensitivity is zero, so the hypothesis holds for every \(\alpha\). But

\[
\frac1{N^2}\sum_{j,k}f(S,C_j,D_k)=\frac1N\sum_j C_j,
\qquad \mathbb E\left|\frac1N\sum_j C_j\right|^2=1/N.
\]

With \(\alpha=4\), the lemma predicts RMS (O(N^{-1})), contradicting the exact RMS (N^{-1/2}). The proof's cancellation for distinct pair indices fails for two pairs sharing one coordinate. There are order (N^3), not order (N^2), potentially nonzero overlapping terms among the (N^4) pairs.

Even correcting that term to (N^{-1/2}) does not fix the next invocation. Lemma 31 (p. 40) proves

\[
\mathbb E|R(\widetilde G_N,C(J))-R(\widetilde G_N^{J},C(J))|^4\le K_T/N^2.
\]

Cauchy–Schwarz with the finite fourth moment of (D_if\) gives the required (f)-sensitivity only as

\[
\mathbb E|f(S,C(J))-f(S^{J},C(J))|^2\le
(K_T/N^2)^{1/2}(\mathbb E|D_if|^4)^{1/2}\le K_T/N.
\]

Thus \(\alpha=1\), so Lemma 12 gives (O_T(N^{-1/4})), not the (O_T(N^{-1/2})) asserted in Lemma 31. The exponents and the supplement's RMS convention were checked on the PDF.

This is a **major proof flaw for the stated sharp coupling rate**, not a demonstrated counterexample to Theorem 5 itself. Theorem 5 uses this estimate through Lemmas 32–33 and D.4, and the (O_T(N^{-1})) output RMS remainder uses it again in E.2. A repair needs a stronger concentration argument exploiting the actual linear/smooth empirical process structure, or a weaker rate. The underlying CLT may survive weaker errors: an (N^{-1/4}) error in the scaled expansion still tends to zero and is faster than (N^{-1/8}). That observation does not itself complete the missing proof.

### L2: an invalid high-moment combinatorial bound has a short alternative

On p. 33 the proof of Lemma 23 bounds a product of edge endpoint degrees by a quantity raised only to the number of high-degree vertices. For a star with (m=kL\) edges, the product on the left is (m^m\), whereas the nonzero side on the right has size (m\). Using two disjoint (r\)-edge stars, one centered on each part, avoids its undefined (0^0\) convention: (m=2r\), both high-degree counts are one, the displayed right side is (m^2\), and the left side is (r^{2r}\). The preceding graph-count explanation also counts half-edge choices using a vertex-count exponent.

The needed initial empirical-square moment bound can nevertheless be reconstructed without this counting or Finner's theorem. Let (A=N^{-2}\sum_{j,k}w(C_j,D_k)^2\). Decompose the complete bipartite average into its (N\) cyclic perfect matchings, (A=N^{-1}\sum_s A_s\), where each (A_s\) is an average of (N\) independent, identically distributed copies of (w(C,D)^2\). Jensen gives \(\mathbb EA^q\le\mathbb EA_s^q\). Sub-Gaussian (w\) implies \(\mathbb E e^{c w^2}<\infty\) for sufficiently small (c>0\): expand the exponential and use \(\mathbb E|w|^{2r}\le(K\sqrt{2r})^{2r}\) and (r!\ge(r/e)^r\). Independence then gives \(\mathbb E e^{cN A_s}\le M^N\), so \(\Pr(A_s>u)\le e^{-cNu/2}\) once (u\ge 2\log M/c\). Integrating this tail yields \(\|A_s\|_{L^q}\le C+Cq/N\). Hence \(\mathbb EA^q\le C^q\) for (q\le N\), more than sufficient for this part of Lemma 23's range. Boundary layers use a single iid average.

This verifies the needed initial-square estimate but not every subsequent higher-power/truncation estimate in Remark 24 and Lemma 27. Severity: **minor flaw in this local subargument**, with an explicit repair. It does not rescue M1.

### M2: false uniform weight-fluctuation bound in the long-time proof

Lemma 38 (p. 54) states that the solution of \(\dot{\overline R}=\overline A\overline R+\overline H\), initialized at zero, has uniformly bounded norm relative to \(\overline H\). Its proof writes \(\overline R=e^{t\overline A}\overline H\). The actual solution is

\[
\overline R(t)=\int_0^t e^{(t-s)\overline A}\overline H\,ds.
\]

Nonpositive spectrum alone gives no uniform bound on this integral. The following example verifies that the lemma itself, not just this formula, fails under Assumptions 1–2.

Take (L=2,d=1\). Let neuron labels be (k\in\mathbb N\) with (p_k=Z^{-1}e^{-4^k}\), (Z=\sum_{k\ge1}e^{-4^k}\). Set (w_1(k)=2^k\), (w_2(k)=1\). Let (X=2^{-k}\) with probabilities (q_k=2^{-k}\). Choose a (C^\infty\) activation \(\varphi_1\) supported in \((3/4,5/4)\), equal to one in a neighborhood of 1. Then

\[
\varphi_1(2^j2^{-k})=\mathbf1_{j=k},\qquad
\varphi'_1(2^j2^{-k})=0.
\]

Its first two derivatives are bounded and Lipschitz. The first-layer initialization is sub-Gaussian, since \(\sum_k p_k e^{c4^k}<\infty\) for (c<1\); the readout is bounded and the countable neuron space has separable (L^2\). Set identity output activation and deterministic target (Y=p_k\) at (X=2^{-k}\). Use \(\ell(y,u)=\sqrt{1+(u-y)^2}-1\). This loss meets the bounded-derivative assumptions, has unique conditional stationary prediction (u=y\), and curvature one there. The mean-field network is stationary, fitting (f(2^{-k})=p_k\) exactly.

Its initial Gaussian output sampling error has coordinates

\[
G_k=\sqrt{p_k}Z_k-p_k U,\qquad
U=\sum_j\sqrt{p_j}Z_j,
\]

for independent standard Gaussian (Z_j\). Thus \(\mathbb E G_k^2=p_k(1-p_k)\). First-layer tangent features vanish. The readout response satisfies

\[
\dot R_2(t,k)=-q_k\{p_kR_2(t,k)+G_k\},\qquad
R_2(t,k)=-\frac{1-e^{-q_kp_kt}}{p_k}G_k.
\]

Consequently,

\[
\mathbb E\|R_2(t)\|_{L^2(P_1)}^2
=\sum_k(1-e^{-q_kp_kt})^2(1-p_k)\longrightarrow\infty.
\]

The norm also diverges almost surely: its limiting squared summands are \((Z_k-\sqrt{p_k}U)^2\), an iid Gaussian sequence plus an \(\ell^2\) perturbation, hence not square-summable. The forcing \(H_2(k)=-q_kG_k\) has finite, nonzero (L^2(P_1)\) norm almost surely. For every finite (t\), the response has finite norm because \(1-e^{-q_kp_kt}\le tq_kp_k\). The counterexample is therefore consistent with finite-time well-posedness.

By contrast, its output fluctuation is

\[
\widehat G(t,2^{-k})=e^{-q_kp_kt}G_k,\qquad
\mathbb E\|\widehat G(t)\|_{L^2(P_X)}^2
=\sum_kq_kp_k(1-p_k)e^{-2q_kp_kt}\longrightarrow0.
\]

Thus output variance decay does not imply bounded weight corrections. This is a counterexample to Lemma 38 and to the uniform moment assertion for (R\) in the proof of Lemma 39, not a counterexample to Theorems 9 or 10.

There are additional explicit breaks in F.3: p. 52 writes a terminal-time integral involving \(e^{-t\overline A}\) for a forward initial-value problem, with no terminal condition and the wrong propagator; p. 55 asserts \(\int_0^\infty\mathbb E\|H_t\|^2dt<\infty\), even though at a stationary example (H_t\) is a nonzero constant forcing. The correct forward identity for (D=R-\overline R\), (D(0)=0\), is

\[
D(t)=\int_0^t e^{(t-s)\overline A}\{(A_s-\overline A)R(s)+(H_s-\overline H)\}\,ds.
\]

Severity: the universal statement of Lemma 38 is **false**; the resulting issue in Theorem 10's proof is **major**, because repair requires different growth or output-space estimates. It is not classified as a fatal flaw of the entire paper: the fluctuation construction and stationary output argument are substantial independent components. A finite data set or a suitable spectral/inverse-range condition could remove this particular infinite-rank obstruction, but would materially narrow the theorem's advertised arbitrary-distribution scope.

F.3 also changes the main theorem's conditional loss-gradient norm into an unconditional square (Eq. (8), p. 50). With noisy labels those are not interchangeable. Conditional averaging can plausibly repair the setup because the network coefficients depend on (X\), but that rewrite is required; it is not supplied by assuming noise vanishes. This discrepancy is secondary to the explicit false bounds above.

## Surviving stationary argument, reconstructed

At a conditional stationary mean-field predictor define the tangent map

\[
(Tu)(x)=\sum_i\mathbb E_C[D_if(C_{i-1},C_i,x)u_i(C_{i-1},C_i)].
\]

The derivative-moment bounds make it Hilbert–Schmidt from the direct sum of weight (L^2\) spaces into (L^2(P_X)\). The output kernel operator (K=TT^*\) is compact, self-adjoint and nonnegative. Conditional curvature is a positive constant (c\), so Eq. (6) gives

\[
\dot{\widehat G}=-cK\widehat G,
\qquad
\frac d{dt}\mathbb E\|\widehat G\|^2=-2c\mathbb E\|T^*\widehat G\|^2\le0.
\]

Appendix F.1's correct covariance decomposition is a sum, over layers, of the covariance of

\[
x\longmapsto\mathbb E_{C_i}[w_i(C_{i-1},C_i)D_if(C_{i-1},C_i,x)].
\]

If (v\in\ker T^*\), each of these functions has zero (L^2(P_X)\) pairing with (v\), almost surely in the remaining label. Fubini and finite moments justify the pairing; its variance is zero. A countable dense subset of the kernel therefore gives \(\widehat G(0)\perp\ker K\) almost surely. Expand in the eigenvectors of compact (K\): on each positive eigenvalue \(\lambda_j\), the coefficient is multiplied by \(e^{-c\lambda_jt}\). Dominated convergence of the squared coefficients, and then expectation, proves decay to zero. A positive spectral gap is not needed for output decay, and no uniform bound on (R\) is used.

This reconstructs the limiting-process conclusion behind Theorem 9. Identification with the finite-network width-scaled variance still invokes the finite-time CLT. Main p. 10's informal claim about being *in the range* of the operator is stronger than necessary; the appendix correctly uses the orthogonal complement of its kernel, equivalently the closure of its range.

## Evidence hierarchy and dependencies

| Claim | Source support | Audit status | Downstream impact |
|---|---|---|---|
| Gaussian sampled-neuron process, Theorem 2 | B.1–B.4; covariance and pairing moment expansion | Main scalar variance display falsified; full process construction and leading pairing mechanism checked | Use appendix covariance, not p. 6 scalar formula |
| Linear response existence, Theorem 3 | C, pp. 26–30, truncation and tail estimates | Complete proof read; not every unbounded-operator estimate independently reconstructed | Retain as a source theorem with coverage qualification |
| Second-order coupled rate, Theorem 5 | D, pp. 31–45 | Major concentration/rate gap M1 | Advertised (O_T(N^{-1})\) output RMS correction not certified |
| Gaussian output moment limit, Theorem 6 | E, pp. 45–46 | Plausible; depends on rate argument, though a weaker vanishing coupling could suffice | Do not infer a pathwise endpoint guarantee |
| Stationary limiting variance decay, Theorem 9 | F.1–F.2, pp. 47–49 | Semigroup/covariance-nullspace chain independently reconstructed | Survives at the limiting-process level |
| Long-time variance after fast convergence, Theorem 10 | F.3, pp. 50–57 | Major proof flaw M2; conclusion not disproved | Requires repaired argument before use as verified theorem |

The main external technical dependency is Nguyen–Pham's mean-field framework [17], invoked for Lemma 11 and the leading-order coupling. Its needed moment estimate can also be reconstructed directly here: the bounded loss derivative and bounded activation derivatives give \(\|\dot w_i\|_{L^p}\le C\|w_{i+1}\|_{L^p}\prod_{j\ge i+2}\|w_j\|_{L^2}\), with \(\|\dot w_L\|_{L^p}\le C\). Starting at the top, integrate the (p=2\) bounds on any finite horizon, then the general (p\) bounds; this preserves \(\|w_i\|_{L^p}\le C_T\sqrt p\). The same integral majorants apply to \(\|\sup_{t\le T}|w_i(t)|\|_{L^p}\). This checks the specific marginal moment input, not every theorem in [17]. The separate framework audit covers that source.

Finner (1992), *A Generalization of Hölder's Inequality and Some Probability Inequalities*, is invoked on supplement p. 33. A primary publisher retrieval was attempted at `https://projecteuclid.org/journals/annals-of-probability/volume-20/issue-4/A-Generalization-of-Holders-Inequality-and-Some-Probability-Inequalities/10.1214/aop/1176989534.full`, but exposed only an iframe. Exact external theorem invocation remains **unverifiable — source unavailable** in this audit. The matching argument above supplies the needed initial empirical-square moment estimate independently; it does not certify all uses of higher-power variants. The bad degree-product inequality is subsequent internal algebra, not evidence against Finner's theorem.

The spectral step was checked in its precise compact self-adjoint form: the tangent kernel is Hilbert–Schmidt by finite derivative moments, the positive eigenspaces span the orthogonal complement of the kernel, and square-summable coefficients permit dominated convergence. The short derivation above verifies all prerequisites needed for the application; no unverified global-convergence theorem is needed for the stationary result. References [17], [20], [21] supply motivation for reaching stationary predictors, but Theorem 10 *assumes* its own convergence rate and does not derive it from those papers.

## Finite retained-state and empirical interpretation

The continuum state consists of functions (w_i(c,d)\), a Gaussian process indexed by time, labels and inputs, and response functions (R_i(c,d)\). In the coupled correction, \(\widetilde G_N\) is generated by the realized sampled labels. The equations specify an autonomous mathematical system on function spaces; they do not by themselves give a fixed finite list of moving coordinates, a width-independent quadrature rule, or an error bound for truncating those functions. This conclusion follows from the explicit state and update definitions, not from the absence of the word “compression.” A finite-dimensional special initialization or feature family could change the representation problem, but would require a closure argument.

Appendix G uses three layers, tanh, width 50–400, 100 MNIST training images, full-batch discrete GD with learning rate (7\times10^{-3}\), and the ordinary nonsmooth-at-the-join Huber loss. It uses 1,000 seeds for the histogram and 10 for variance curves; the “mean-field” comparison for subsampling is one width-5,000 network. The empirical centered variance divides by (M\), giving the usual ((M-1)/M\) expectation factor. These are illustrations, not a reproduction of the exact continuous-time smooth-loss hypotheses. The paper itself reports no error bars. No empirical claim was used to repair a failed proof step.

Overall confidence is high in the explicit counterexamples, exponent audit, model/limit-order reading, and reconstructed stationary output mechanism; it is lower in un-reconstructed truncation estimates and in conclusions depending on the flawed concentration and long-time arguments. The scientifically appropriate conclusion is to retain the source's useful coupled fluctuation framework while qualifying its quantitative rate and post-convergence proof, rather than either dismissing fluctuation theory or treating all statements as verified.
