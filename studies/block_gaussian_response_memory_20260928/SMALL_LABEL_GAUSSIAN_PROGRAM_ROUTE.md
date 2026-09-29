# Small-label Gaussian-program route

This is an independent scoped theoretical attempt. Scientific inputs were the assignment, `docs/notation.qmd`, the complete relevant fixed-program proofs in `docs/02-gaussian-reuse.qmd`, the complete local theorem and weighted response proof C.1–C.2 in `docs/03-local-population.qmd`, and their required fixed-program dependency III.F.1–III.F.7 in `docs/12-three-sample-learning.qmd`. No other study, experiment, or external source was used.

**Conclusion.** This route does not prove an all-time trained block-to-dense error $Ck^{-\beta}$ for fixed nonzero small labels, for any specified positive $\beta$. The maintained fixed-program argument cannot be promoted to that statement by inserting a small total-activity bound: its conditioning constants degenerate under mesh refinement, its moment ledger grows with the number of calls, and its directly quantitative estimate is a strong $k^{-1/2}$ estimate rather than a weak $k^{-1}$ estimate. The book's uniform first-source-response bounds address a different part of the proof.

A qualitative full nonlinear bridge follows from the parent route's explicit polynomial primal bounds, by a same-array fixed-mesh oracle comparison that separates bad initialization blocks. Section 4 gives that argument, including a version for actual finite networks uniform over the number of blocks. It assumes no trained block Gaussian law or quantitative Gaussian approximation. Initialization estimates already proved by the parent are not repeated. During this attempt the supervisor explicitly added `SMALL_LABEL_BLOCK_FITTING.md` as an input; it was read completely after the independent initial analysis. Its verified fitting and test-tail estimates supply the finite-network prerequisites below.

## 1. Target, clocks, and the exact block oracle

The network and rates are exactly those in the assignment:

\[
z_a^1=W^1x_a/\sqrt d,\qquad z_a^\ell=W^\ell h_a^{\ell-1},
\qquad h_a^\ell=\tanh z_a^\ell,\qquad f_a=w^Th_a^L/n,
\]
\[
\dot w=-\frac2m\sum_a r_a h_a^L,\quad
\dot W^1=-\frac2{m\sqrt d}\sum_a r_a\delta_a^1x_a^T,
\quad
\dot W^\ell=-\frac2{nm}\sum_a r_a\delta_a^\ell(h_a^{\ell-1})^T.
\tag{1}
\]

Here (w(0)=0), (r=f-y), and (L,m,d) are fixed. The hidden initialization is a direct sum of independent $k\times k$ Gaussian blocks of entry variance (1/k), aligned across layers; (n=Bk). Every learned increment in (1) is unmasked. First-layer rows are independent standard Gaussian rows. Test inputs form any fixed finite set; constants below may depend on that set and on (L,m,d). The intended block population is the $B\to\infty$ limit at fixed $k$, followed by comparison with the canonical dense population as $k\to\infty$.

For example, the exact initialized-plus-trained decomposition is

\[
W^\ell(t)=D^\ell-
rac2m\sum_b\int_0^t
r_b(s)\,\frac{\delta_b^\ell(s)(h_b^{\ell-1}(s))^T}{n}\,ds.
\tag{2}
\]

Consequently its forward action is

\[
z_a^\ell(t)=D^\ell h_a^{\ell-1}(t)
-\frac2m\sum_b\int_0^t r_b(s)\delta_b^\ell(s)
\frac{(h_b^{\ell-1}(s))^Th_a^{\ell-1}(t)}n\,ds,
\tag{3}
\]

and its transpose action has the corresponding global backward contraction. Formula (3) retains interactions between distinct initialization blocks. Training an isolated $k$-neuron network with its own empirical contractions would substitute a different model.

At a separately fixed Euler transcript, replace all scalar contractions and residuals by prescribed deterministic oracle values. The restriction of that oracle to one initialization block is then exactly the execution of the same deterministic-coefficient Gaussian program at width $k$. Distinct blocks are independent copies of this execution. This is an exact finite-program statement: the initial action has variance (1/k), all coordinate operations are local to a block, and all cross-block information in (3) has become a deterministic scalar coefficient. Its $k\to\infty$ scalar law is therefore the dense fixed-program law, using A.1–A.2/III.F after clipping the backward products as in their proofs.

This proves neither an estimate uniform in transcript length nor identification of an evolved block population with that oracle. Restoring the empirical feedback is an additional comparison, even though its finite-transcript qualitative version can be handled causally.

Define residual activity by

\[
\mathcal A(t)=\frac2m\int_0^t\sum_a|r_a(s)|\,ds.
\tag{4}
\]

The elementary pathwise estimate

\[
\sup_i|w_i(t)|\le \mathcal A(t)
\tag{5}
\]

holds for finite networks and for every frozen-control block oracle. It follows directly by integrating the readout equation and using $|\tanh|\le1$.

Small labels alone do not imply finite activity. For identical training inputs with labels (Y,-Y), zero-readout training stays stationary because the two gradient contributions cancel, whereas (4) grows as (2Yt). A coercive training geometry, a projected effective forcing estimate, or a separately proved finite-activity bound is needed. This example concerns the clock, not the truth of a block-to-dense prediction estimate.

## 2. What small total activity actually supplies from C.2

C.2 proves mesh-uniform subGaussian marginal bounds for population backward fields, bounded full rows of expected forward-source derivatives, and one-mesh-factor bounds for backward-source pulses. It admits arbitrary bounded deterministic controls in place of the residual coefficients and arbitrary positive step lengths with small total sum. It permits singular covariance matrices. Its derivative convention freezes deterministic residuals, contractions, response coefficients, and covariance laws.

For a deterministic controlled Euler transcript, let $c_{a,j}$ be the physical coefficient replacing $2r_{a,j}$, so an increment contains (\Delta_jm^{-1}\sum_a c_{a,j}$\cdots$). Set

\[
\widehat\Delta_j=\Delta_j\max_a|c_{a,j}|,
\qquad \widehat c_{a,j}=c_{a,j}/\max_b|c_{b,j}|,
\tag{6}
\]

and omit a zero-control step. The same parameter update is now an update of length $\widehat\Delta_j$ with controls bounded by one. If

\[
\sum_j\widehat\Delta_j\le S_0
\tag{7}
\]

and the preliminary RMS bounds required by C.2 hold, the proof in C.2 applies with constants independent of the physical horizon, number of steps, and covariance ranks. In the flow version, $ds/dt=2\max_a|r_a(t)|$, and the total new time is at most $m\mathcal A(\infty)$. Thus sufficiently small finite activity supplies the *population first-response/tail part* on the whole physical path, after a control-clock reformulation. The factor $m$ is harmless here because $m$ is fixed.

This conclusion has three precise limitations.

1. It is about the already identified population Gaussian program. It is not a quantitative Gaussian approximation theorem for a trained $k$-block.
2. It controls first derivatives in named Gaussian source slots with coefficients frozen. It does not control derivatives of the self-consistent covariance/response map, or finite-width weak-bias remainders.
3. Normalizing the residual as in (6) does not make its feedback map Lipschitz near zero residual. Comparing two trained paths still requires an independent stability argument. A common short control interval is useful, but is not by itself an all-time comparison theorem.

The exact weighted pulse factor in C.2 is a useful ingredient for a new proof; throwing it away in favor of a maximum over all source coordinates would reintroduce transcript-length factors.

## 3. Initialization calculation omitted

The parent route independently established the initialization-kernel weak bias and exact initial-velocity estimates. They are not rederived or used to close a nonlinear trained claim here. A fixed nonzero-label approximation with a remainder independent of k would not give the requested trained convergence rate.

## 4. A qualitative full nonlinear bridge from explicit polynomial primal bounds

The following proposition makes the useful upgrade precise. Its assumptions are deterministic path bounds or ordinary existence/uniqueness statements. In particular, none assumes that trained block fields have Gaussian laws, satisfy propagation of chaos, or admit a quantitative Gaussian comparison. The parent fitting note supplies the finite-network bounds. For an already constructed block population the argument in §§4.1–4.4 is conditional on their population counterparts. Section 4.6 gives the direct finite-network conclusion without assuming that a fixed-block-size population has been constructed.

### 4.1 Statement and exact prerequisite package

For each $k$, realize a random initialization block on its mark probability space. At each layer use the Hilbert space of measurable random $k$-vectors with norm

\[
\|v\|_{\mathcal H_k}^2=\mathbb E\frac{\|v\|_2^2}{k}.
\tag{22}
\]

The expectation includes the entire initialization block mark. The layer spaces have different types but can use the same underlying block mark. The initialized action $D^\ell$ is pointwise multiplication by that mark's matrix. The learned increment $M^\ell$ is the global rank-one integral in (2), with the expectation inner product in (22). Its adjoint is the transpose learned action. This represents unmasked training, including connections between different block marks.

Assume the block population and canonical dense population exist uniquely, and that for every fixed physical horizon $T$:

1. Their residual activities are at most a common $A_0$, sufficiently small for the dense response estimate after the control-clock change. The bound parameters and the smallness margin are independent of (k,T).
2. The block states $Z_a^1,w,M^\ell$, with $M^\ell$ measured in operator or Hilbert–Schmidt norm on (22), and their velocities have common deterministic bounds on $[0,T]$. These follow, for example, from (5), bounded tanh, and the polynomial backward bounds in item 3. The dense state has the analogous bound. Bounds on the full unbounded initialized $D^\ell$ are not assumed.
3. With $R_k=\max_{2\le\ell\le L}\|D^\ell\|_{\mathrm{op}}$, there are fixed nonnegative polynomials $P_\ell$, independent of (k,t), such that

\[
\frac{\|\delta_{a,k}^{\ell}(t)\|_2}{\sqrt k}
\le A_0P_\ell(R_k)
\quad\text{for almost every block mark, all }a,t.
\tag{23}
\]

Fixed test inputs need only the usual forward bounds; they need not enter (23) unless their backward observables are requested. Gaussian initialized matrix moments then give uniform global backward RMS bounds. The fitting note proves the concrete envelope with a fixed constant times $(1+R_k)^{L-\ell}$ and its integrated state bounds. Its activity is $\int\|r\|_2/\sqrt m$, whereas (4) is at most twice that activity; this changes only the fixed smallness threshold. Its block radius includes an additional one, also absorbed in this polynomial.

The dense reference admits finite Euler or controlled-Euler approximants with the same primal bounds and the C.2 mesh-uniform reference tails on $[0,T]$. This last fact follows from the small-activity version in §2 and the C.1 construction: first stop Euler schemes at a slightly larger activity cap, apply the C.2 first-response bounds there, and use C.1's asymmetric comparison to construct their limit. Uniqueness identifies that limit with the dense solution. If the true activity lies strictly below the cap, uniform prediction convergence implies convergence of the integrated residual activity on every fixed $[0,T]$, so sufficiently fine schemes do not hit the cap. No continuity of normalized residual direction at zero is needed, because this final comparison is in physical time.

**Qualitative bridge.** Under this package, for every fixed $T<\infty$ and finite test set,

\[
\sup_{t\le T}\max_u|f_{k,u}(t)-f_{\mathrm{dense},u}(t)|\longrightarrow0
\qquad(k\to\infty).
\tag{24}
\]

If, in addition, the parent proves common prediction tails

\[
\sup_{t\ge T}|f_{k,u}(t)-f_{k,u}(T)|
+\sup_{t\ge T}|f_{\mathrm{dense},u}(t)-f_{\mathrm{dense},u}(T)|
\le C Y e^{-\lambda T},
\tag{25}
\]

for all sufficiently large $k$, then (24) holds with the supremum over all $t\ge0$. More generally, any right side of (25) tending to zero uniformly in $k$ suffices.

### 4.2 Bad initialization blocks have vanishing polynomial mass

Choose a fixed $M_0\ge10$, enlarged for the finite number of layers, and define $E_k=\{R_k\le M_0\}$. The elementary Gaussian matrix net bound in chapter 2 §5.10 or III.F.2 gives

\[
\mathbb E[(1+R_k)^j\mathbf1_{E_k^c}]
\le C_j e^{-c_j k}
\quad\text{for every separately fixed }j<\infty.
\tag{26}
\]

For completeness, its tail estimate is bounded by (C_L\exp$-k u^2/16$) for $u\ge M_0$. The expectation in (26) is bounded by its threshold term plus the integral of (j(1+u)^{j-1}\mathbb P$R_k>u$); the Gaussian factor dominates the fixed polynomial, giving (26). The constants may depend on $j$, which will be fixed before $k\to\infty$.

The multiplication operator $D^\ell\mathbf1_{E_k}$ has norm at most $M_0$ on (22). Since every activation vector has block RMS at most one,

\[
\|D^\ell\mathbf1_{E_k^c}h_a^{\ell-1}(t)\|_{\mathcal H_k}
\le(\mathbb E R_k^2\mathbf1_{E_k^c})^{1/2}=o_k(1).
\tag{27}
\]

By (23), the true backward action on the bad part also satisfies

\[
\|(D^\ell)^T\mathbf1_{E_k^c}\delta_a^\ell(t)\|_{\mathcal H_k}
\le A_0[\mathbb E R_k^2P_\ell(R_k)^2\mathbf1_{E_k^c}]^{1/2}
=o_k(1),
\tag{28}
\]

uniformly in $t\le T$. This is the only place where a trained block moment envelope is needed to handle the unbounded initialized operator.

Equations (27)–(28) do **not** assert that the full trajectory is close to a separately evolved truncated-vector-field trajectory. Such a claim would require controlling additional coordinate multipliers. The proof instead uses the good/bad decomposition directly inside differences against a reference with verified tails.

### 4.3 Fixed-mesh dense oracle on the block mark space

Fix a dense population Euler mesh $\Delta>0$. Use its deterministic residuals, contractions, and trained rank-memory coefficients to form the same-array oracle of C.1. Execute that finite oracle using one $k\times k$ Gaussian block at each layer and the actual $k$ first-layer roots. Its coefficient tables come from the dense Euler recursion only; this is a proof device, not an admissible final closure.

The fixed-program theorem III.F and extension A.2 apply even with zero readout, zero reverse queries, repeated inputs, and singular history Grams. For a fixed finite tuple of oracle nodes, its within-layer empirical law converges in probability in $\mathcal W_2$ to the dense tuple law. Thus all required contractions and continuous functions with at most quadratic growth converge in probability.

To upgrade this to convergence of their expectations over the random block mark, use fixed-mesh uniform integrability. At a fixed number of instructions, the RMS of every oracle node is bounded by a finite polynomial in initialized matrix norms and first-root RMS norms. This follows by induction: tanh is bounded, tanh' is bounded, an initialized action multiplies an RMS by $R_k$, a frozen linear combination has fixed coefficients, and there are finitely many instructions. Gaussian matrix moments and Gaussian first-root RMS moments are bounded uniformly in $k$. Hence these polynomial majorants have uniformly bounded moments of every separately fixed order. Quadratic observables are uniformly integrable, proving expectation convergence. This does not request any moment order uniform in $\Delta\downarrow0$.

Build proxy parameters $\theta_k^\Delta=(Z^{1,\Delta}_k,w_k^\Delta,M_k^{\ell,\Delta})$ from the oracle's endpoint fields and rank-memory expansion, now interpreting each rank term as an operator on (22). Recomputing the network at these parameters differs from prescribed oracle actions only by finitely many contraction errors of the form displayed in C.1, eq. l2785. Their expectations tend to zero, so all forward and backward recomputation errors vanish in $\mathcal H_k$, at fixed mesh.

One can justify every use of the unbounded initialized operator in this finite induction by the same split as (27): its good part is bounded, and all fixed-mesh proxy and oracle fields have polynomial block RMS envelopes; their bad-part contributions tend to zero by (26). The same reasoning establishes consistency of proxy velocities and residuals. No estimate uniform in the number of instructions is asserted.

The fixed-mesh proxy learned-operator, RMS, and velocity bounds have limiting upper bounds independent of $\Delta$, because their contractions converge to the dense Euler values and the dense Euler states obey the primal bounds. All proxy/oracle bad-part bounds are (o_k(1)) at fixed $\Delta$, though their polynomial degrees and constants can depend on that mesh.

Let $P_{a,k}^{\ell,\Delta}$ denote the *recomputed* incoming backward field of the proxy. The continuous quadratic tail tests of its oracle, C.2, and the RMS recomputation error imply

\[
\limsup_{k\to\infty}
\max_{a,\ell,j\Delta\le T}
\|P_{a,k}^{\ell,\Delta}
\mathbf1_{\{|P_{a,k}^{\ell,\Delta}|>R\}}\|_{\mathcal H_k}
\le C e^{-cR^2}.
\tag{29}
\]

The constants on the right are independent of $\Delta$. To avoid the discontinuous threshold test, use a continuous cutoff dominating $x^2\mathbf1_{|x|>R}$ and supported outside (|x|>R/2). RMS recomputation errors transfer tails by the elementary inequality used in C.1,

\[
\|v\mathbf1_{|v|>2R}\|_2
\le2\|v-u\|_2+2\|u\mathbf1_{|u|>R}\|_2.
\]

All limits in this paragraph are width-first at a fixed finite mesh.

### 4.4 Direct asymmetric comparison, including both matrix orientations

Measure state error by the sum of first-field and readout $\mathcal H_k$ norms and learned-increment operator norms. For forward actions in a difference of actual and proxy states, the only new term relative to C.1 is

\[
D^\ell(h-\widetilde h)
=D^\ell\mathbf1_{E_k}(h-\widetilde h)
+D^\ell\mathbf1_{E_k^c}(h-\widetilde h).
\]

The first term is bounded by $M_0\|h-\widetilde h\|_{\mathcal H_k}$; the second by twice (27), since both activation vectors are bounded. All trained-operator difference terms have the usual bounded rank-increment estimate. Forward states and predictions are therefore Lipschitz in the state distance up to an (o_k(1)) forcing.

For a reverse initialized action, use

\[
(D^\ell)^T(\delta-\widetilde\delta)
=(D^\ell)^T\mathbf1_{E_k}(\delta-\widetilde\delta)
+(D^\ell)^T\mathbf1_{E_k^c}\delta
-(D^\ell)^T\mathbf1_{E_k^c}\widetilde\delta.
\tag{30}
\]

The good part is bounded by $M_0\|\delta-\widetilde\delta\|_{\mathcal H_k}$. The actual bad part is (28); the fixed-mesh proxy bad part is (o_k(1)) by its polynomial envelope and (26). This handles the true transpose of the same initialized matrix.

For coordinate multiplier differences write, with the proxy as reference,

\[
\tanh'(Z)P-\tanh'(\widetilde Z)\widetilde P
=\tanh'(Z)(P-\widetilde P)
+[\tanh'(Z)-\tanh'(\widetilde Z)]\widetilde P.
\]

The second term is bounded by

\[
C R\|Z-\widetilde Z\|_{\mathcal H_k}
+2\|\widetilde P\mathbf1_{|\widetilde P|>R}\|_{\mathcal H_k}.
\tag{31}
\]

Only the reference requires coordinatewise tails. Polynomial **block RMS** bounds alone would not justify replacing the last term by a coordinatewise Gaussian tail; (29) is the essential separate input. Downward substitution through the fixed number of layers introduces one factor (1+R), as in C.1, rather than a power $R^L$. The remaining factors are bounded operators or bounded activation derivatives.

Consequently, with $F_k$ denoting the exact full nonlinear field and with the reference at a proxy grid state,

\[
\|F_k(\theta_k)-F_k(\theta_k^\Delta)\|
\le C(1+R)d_k(\theta_k,\theta_k^\Delta)
+C e^{-cR^2}+o_k^{\Delta,R}(1),
\tag{32}
\]

in the limiting-upper-bound sense of (29). Constants (C,c) are independent of $k,\Delta$; the last term is only asserted to tend to zero for separately fixed $\Delta,R$. Outer-product differences use

\[
\|u\otimes v-\widetilde u\otimes\widetilde v\|
\le\|u-\widetilde u\|\|v\|+\|\widetilde u\|\|v-\widetilde v\|,
\]

and all velocity formulas (1) have the same residual and bounded-RMS structure, so (32) controls the entire state velocity.

Compare the true continuous path with the linearly interpolated proxy. The assigned proxy velocity differs from its recomputed grid velocity by $o_k^\Delta(1)$; the preceding grid state is within $C\Delta$ of the proxy interpolant. Initial state distance is zero because first roots, zero readout, and zero learned increments agree. Integrating (32) and the elementary Gronwall inequality gives

\[
\limsup_{k\to\infty}\sup_{t\le T}
d_k(\theta_k(t),\theta_k^\Delta(t))
\le C_Te^{C_T(1+R)}
\big[(1+R)\Delta+e^{-cR^2}\big].
\tag{33}
\]

The proxy's predictions converge at fixed mesh to the dense Euler predictions, and the dense Euler predictions converge to the canonical dense flow. First let $k\to\infty$ at fixed $\Delta,R$; then let $\Delta\downarrow0$; then $R\to\infty$. The Gaussian tail dominates $e^{C_TR}$, so (33) proves (24).

Finally, (25) and the triangle inequality give

\[
\sup_{t\ge0}|f_{k,u}(t)-f_{\mathrm{dense},u}(t)|
\le\sup_{t\le T}|f_{k,u}(t)-f_{\mathrm{dense},u}(t)|
+CY e^{-\lambda T}.
\]

Take $k\to\infty$ and then $T\to\infty$. This proves the all-time qualitative extension.

The proof deliberately retains ordered limits. In particular, the $o_k^{\Delta,R}(1)$ in (32) has no claimed modulus; selecting $\Delta=\Delta(k)$, a memory order $q=q(k)$, or an accuracy cost from it would be unjustified. This is a full nonlinear qualitative identification conditional on explicit primal/tail bounds, not the requested polynomial rate.

### 4.5 Why treating the whole curve as one Gaussian query does not yet give a rate

For deterministic nonadaptive query curves, the entire initialized action can indeed be viewed as a Hilbert-valued Gaussian variable. For the actual trained query curve, the curve depends on the same matrix in both orientations. Assigning it a Gaussian law conditional on the whole curve would skip the adaptive-conditioning and response step. The finite sequential conditional identities still have to be reconciled with that whole-curve construction.

Small path variation alone gives no lower conditioning bound even in a curve formulation. In a Hilbert space with orthonormal vectors $e_j$, consider

\[
u(s)=e_0+\varepsilon\sum_{j\ge1}\frac{2^{-j}}j\sin(js)e_j,
\qquad 0\le s\le2\pi.
\tag{34}
\]

Its derivative norm is at most (\varepsilon$\sum_j4^{-j}$^{1/2}), so its total variation is arbitrarily small. Nevertheless, observing (Wu$s$) for the entire curve reveals every $We_j$, by integrating against (\sin(js)) and dividing by its nonzero coefficient. In a finite $k$-dimensional version, an arbitrarily small-variation curve can therefore reveal all $k$ input directions. In the infinite version the covariance operator is compact with eigenvalues tending to zero; its inverse on the range is unbounded. This is a counterexample to an inference from small variation to well-conditioned noiseless conditioning, not a claim that (34) is a reachable neural trajectory.

A genuine whole-curve weak-comparison argument could avoid those inverses by estimating only activity-weighted responses and discarded directions. It would need to construct the causal source/response fixed point and prove that its nonlinear covariance and response maps are stable in the chosen path topology. C.2 bounds first source rows with coefficients fixed, but does not prove this covariance-map contraction or a centered finite-$k$ defect estimate. Near a singular covariance, square-root coupling is only Hölder without extra structure. Hence writing a Hilbert Gaussian source from the desired covariance is a representation proposal, not yet the missing finite-block identification theorem or its (1/k) error bound.

### 4.6 Direct finite-network theorem, uniform over the block count

Assume the canonical dense population flow exists uniquely as a regular
global solution in the field/operator state of C.1; this is the dense
existence assumption permitted by the problem, not a finite-width rate
assumption. Its initialized Gaussian actions on the generated spaces
have the bounded operator norms constructed in C.1. The deterministic
proof in SMALL_LABEL_BLOCK_FITTING.md applies to this dense solution by
replacing the normalized vector norms by the corresponding population
Hilbert norms and using a single fixed bound for those initialized
operators. The zero readout and bounded activations give the same
pointwise readout bound, and the same backward, feature-displacement,
Gram-preservation and first-exit inequalities follow. Thus the dense
activity, fitting and prediction-tail bounds used here are consequences
of that proof, not additional hypotheses of trained stability. Reduce
the positive label threshold, if necessary, to meet C.2's small-activity
margin. It still depends only on fixed problem data and not on B,k,time.

The preceding argument has a useful finite-network formulation that removes the assumption of an existing fixed-block-size population. Let the canonical dense initialized training feature Gram divided by m have a positive gap. Choose a fixed moment threshold $S_0$ and then the fixed label bound small enough to satisfy both `SMALL_LABEL_BLOCK_FITTING.md` and the strict activity margin for C.2 used above. All constants can depend on the fixed data, depth and test set. Then, for every $\epsilon>0$,

\[
\sup_{B\ge1}\mathbb P\left\{
\sup_{t\ge0}\max_u
|f_{Bk,k,u}(t)-f_{\mathrm{dense},u}(t)|>\epsilon
\right\}\longrightarrow0
\qquad(k\to\infty).
\tag{35}
\]

Here every finite network has exactly B independent initialization blocks of size k and the full unmasked learned updates. Equation (35) is qualitative; no rate in k is asserted.

To prove it, replace expectation norms (22) in §§4.2–4.4 by the empirical average over the B blocks and their k coordinates. Each part of that proof continues to hold in probability uniformly in B for the following explicit reasons.

First, for every fixed polynomial p,

\[
\mathbb E\left[\frac1B\sum_{b=1}^B
p(R_{k,b})\mathbf1_{\{R_{k,b}>M_0\}}\right]
=\mathbb E[p(R_k)\mathbf1_{\{R_k>M_0\}}]\longrightarrow0.
\tag{36}
\]

Use a nonnegative polynomial majorant if necessary. Markov's inequality makes every needed bad-part error vanish in probability uniformly in B. The learned terms use global empirical contractions exactly as in the finite network, so the initialized action split does not discard off-block updates.

Second, the fitting note's moment event has probability tending to one uniformly in B, rather than only a fixed high probability, when k grows. Indeed

\[
\frac1B\sum_b(1+R_{k,b})^{4L}
\le(1+M_0)^{4L}
+\frac1B\sum_b(1+R_{k,b})^{4L}
\mathbf1_{\{R_{k,b}>M_0\}}.
\]

Choose $S_0>1+M_0$. Equation (36) shows that the right side exceeds $S_0^{4L}$ with probability tending to zero uniformly in B. The initialized training Gram converges in probability to the dense Gram uniformly in B by the fixed-program argument in the next paragraph, applied just at initialization. Thus its positive-gap event also has probability tending to one. The fitting theorem then supplies (23), the state/velocity bounds, and the test tails uniformly in B on this event. Gaussian first-layer RMS bounds for the fixed input set also hold with probability tending to one uniformly in B, since n is at least k.

Third, fix a dense oracle transcript and any scalar contraction or continuous quadratic tail statistic in it. For one block call the empirical statistic $X_k$ and its dense limiting value $x_\infty$. Section 4.3 proves $X_k\to x_\infty$ in probability and uniform integrability, hence in $L^1$. For the B-block oracle,

\[
\mathbb E\left|\frac1B\sum_{b=1}^B X_{k,b}-x_\infty\right|
\le\mathbb E|X_k-x_\infty|\longrightarrow0.
\tag{37}
\]

The bound is uniform in B and does not require B to tend to infinity. There are finitely many tests at each fixed mesh. This proves all fixed-mesh proxy consistencies and reference-tail bounds uniformly in B. Fixed-transcript polynomial majorants likewise justify (36) for proxy bad terms, with constants depending on that fixed transcript.

Proxy recomputation also involves products with global empirical
contractions or their RMS bounds. The finite list of these quantities
converges to bounded dense values, or has uniformly bounded higher
moments by the same fixed-transcript majorants. Restrict to their
uniformly tight moment event before multiplying a bad-block error by
such a quantity; then let that event's bound grow. This verifies that
those products still vanish in probability uniformly in B, without
declaring the interacting trained blocks independent.

These checks give the probabilistic version of (33): for each fixed R and mesh, the residual forcing is $o_{\mathbb P}(1)$ uniformly in B; all deterministic constants in (33) are independent of B. Given a target error, choose R sufficiently large, then the mesh sufficiently small, then k sufficiently large for the finite list of oracle and bad-part tests. This proves compact-time convergence in probability uniformly in B. Finally choose T sufficiently large in the fitting theorem's common prediction-tail bound before these compact-time choices. The triangle inequality used after (33) proves (35).

This proof covers multi-input fixed finite depth and zero readout specifically: C.1–C.2 explicitly allow zero readout and arbitrary fixed input Grams, and III.F treats singular query Grams. No use is made of the different order-one-readout strict-rank theorem in chapter 2 §5. If a fixed-k block population is separately constructed as a B-to-infinity prediction limit with the same tail bounds, (35) implies its all-time convergence to the canonical dense population as k tends to infinity. The theorem itself does not construct that fixed-k limit.

The conclusion also holds in the whole-test metric

\[
\left\|\sup_{t\ge0}|f_{Bk,k}(t,\cdot)
-f_{\mathrm{dense}}(t,\cdot)|\right\|_{L^2(\mu)}
\longrightarrow0
\quad\text{in probability, uniformly over }B.
\tag{38}
\]

Here mu may be any fixed Borel probability law on finite input vectors, assuming the natural joint measurability of the prediction maps. In particular it covers the parent's finite-second-moment test laws. The absence of a moment condition in this qualitative extension comes from bounded tanh predictions, not from a quantitative tail estimate uniform over unbounded inputs.

To check (38), let the common good event be the moment/gap event above. Its complement has probability tending to zero uniformly in B. On it the fitting bound and bounded activation give an absolute prediction bound independent of the test input:

\[
|f_{Bk,k}(t,x)|\le2M^2Y/\gamma,
\qquad |f_{\mathrm{dense}}(t,x)|\le2M^2Y/\gamma
\quad\text{for every }t,x,
\]

after using common enlarged constants and the smaller of the two positive gap bounds. Thus the prediction difference is at most a fixed constant K on this event. For each fixed x, (35) gives

\[
\sup_B\mathbb E\left[
\sup_{t\ge0}|f_{Bk,k}(t,x)-f_{\mathrm{dense}}(t,x)|^2
\mathbf1_{\mathrm{good}}\right]\longrightarrow0.
\]

Indeed it is at most delta squared plus K squared times the supremum over B of the probability that the difference exceeds delta; first take k to infinity, then delta to zero. These quantities are bounded by K squared. The supremum is over countably many integer B, so it is measurable. Dominated convergence in x, Tonelli's theorem, and Markov's inequality now imply (38), since the supremum over B of an integral is bounded by the integral of the pointwise supremum. Add the vanishing probability of the common bad event.

The parent test-tail theorem supplies the end-of-training limit for each finite model on its good event, and for the dense model. Define the finite final predictor to be zero, or any other fixed measurable extension, on the complement of that event. On the good event its difference from the dense final predictor is bounded pointwise by the all-time supremum difference. Since the complementary probability tends to zero uniformly in B, these extended final predictors converge in the same whole-test metric in probability, uniformly in B. This does not claim existence of a training limit on every bad initialization draw. For a test law without a second moment, pointwise existence on the good event together with the uniform bounded prediction envelope also gives existence of the final predictor in L2(mu) by dominated convergence. None of these dominated-convergence arguments supplies a rate in k or a finite-closure sample complexity.

## 5. Why the quantitative fixed-program proof does not close the target

### 5.1 Model and rank hypotheses differ

The quantitative moment construction in chapter 2, §5.9, is attached to the §5 theorem with one input, a fixed nonzero feature-ascent step, and independent order-one Gaussian stored readout. Its rank proof uses nonzero initial cotangent variances. These are not the present zero-readout loss-flow hypotheses. General singular programs are covered by III.F/A.1–A.2, but there the conclusion is qualitative.

In the present first Euler update, $\delta_a^\ell(0)=0$, so every hidden parameter remains unchanged. The forward queries at steps zero and one are exactly equal, and the initial reverse queries are exactly zero. Thus the full history Grams in that proof are singular before considering any mesh limit. Removing redundant columns is legitimate for exact conditioning, but does not restore a uniform positive gap for the remaining history.

More generally, for a Hilbert-space query path $u(s)$ with $\|u(s+\Delta)-u(s)\|\le V\Delta$, the $2\times2$ Gram of these consecutive queries has

\[
\lambda_{\min}\le\frac12\|u(s+\Delta)-u(s)\|^2
\le\frac{V^2\Delta^2}{2}.
\tag{17}
\]

Use the unit vector $2^{-1/2}(1,-1)$ in its Rayleigh quotient. The least eigenvalue of a larger history Gram is no larger, by extending that test vector by zeros. Small total activity can make $V$ small; it cannot supply the missing lower spectral bound. The innovation variance is also bounded above by the squared error from predicting the new query by the immediately preceding one.

At finite block width, more than $k$ linearly independent history queries are impossible. Any argument requiring a positive definite empirical Gram of a larger history cannot run at that width. An inverse-free or effective-rank argument is needed before taking a growing transcript limit.

### 5.2 The explicit constants depend badly on transcript length

For the book's one-input chronology, there are

\[
J=(2N+1)(L-1),\qquad \Lambda=3J+1
\]

microsteps. To control terminal moment order $\nu$, §5.9.4 uses root moments of order $\nu8^\Lambda$. For stopping probability (O$k^{-b}$), the displayed order is

\[
2b\,8^{3(2N+1)(L-1)+1}.
\tag{18}
\]

The Gaussian $L^r$ norm itself grows on the order of $\sqrt r$. Thus these are not uniformly bounded high moments as $N\to\infty$. The coefficients additionally use inverse-Gram bounds and square-root-variance bounds involving the fixed-program gap $\gamma_{L,N,h}$. Equations (17) and the exact initial degeneracies show why that gap cannot simply be held fixed.

For the current multi-input oracle, a direct chronology has at most $m(2N+1)(L-1)$ initialization actions, with additional fixed test actions. The same type of moment bookkeeping consequently grows with $mN(L-1)$. This observation is about the supplied proof's constants, not a lower bound on the optimal theorem.

### 5.3 Regularizing a fixed program does not supply the missing rate

III.F.5 adds fresh noise $\epsilon\chi$ to each query. At fixed transcript length this gives innovation variances at least $\epsilon^2$, a finite-array perturbation bound $C_J\epsilon$, and continuity of the inverse-free scalar recursion as $\epsilon\downarrow0$. The limits are taken in that order; no joint modulus uniform in $J\to\infty$ is proved.

One must not identify a lower bound on successive innovation variances with a lower bound $\epsilon^2$ on the full history Gram. If its size is $J$ and all query second moments are at most $M_J^2$, the immediate determinant/trace argument gives only

\[
\det G\ge\epsilon^{2J},\qquad
\lambda_{\min}(G)\ge
\frac{\epsilon^{2J}}{(JM_J^2)^{J-1}}.
\tag{19}
\]

Indeed the determinant is the product of the successive Schur complements; every other eigenvalue is at most the trace. This lower estimate can be extremely poor as $J$ grows. The input-perturbation proof propagates one error through every instruction, so its $C_J$ is also not a mesh-uniform constant.

Nor is ordinary positive-semidefinite square-root coupling uniformly Lipschitz at rank loss: already in dimension one, covariances $0,\eta$ have standard deviations $0,\sqrt\eta$. The inverse-free population formula avoids invalid pseudoinverse limits, but does not automatically convert a covariance error into a linear-order strong coupling bound. Weak smooth Gaussian observables can behave better, as the separately established initialization calculation demonstrates.

### 5.4 Strong $1/\sqrt{k}$ does not imply weak (1/k)

Even if all conditioning problems were bypassed and the chapter-2 coupled-field estimate had a uniform constant, its direct output would be a $Ck^{-1/2}$ strong error. Taking an expectation does not upgrade its exponent. A proof of $\beta>2/3$ needs additional cancellation or a more accurate comparison. The parent initialization calculation obtains (1/k) because conditional sampling fluctuations are centered and the smooth covariance map has a bounded second derivative. For a reused trained matrix, response terms and adaptive queries must be included in the analogous centering calculation.

The supplied first-source-response bounds do not prove that cancellation or bound its second-order remainder uniformly in the number of calls. They therefore cannot substitute for a quantitative trained Gaussian-law theorem.

### 5.5 The block population has a separate operator issue

At fixed $k$, the operator norm of the finite block-diagonal initialized matrix is $\max_{b\le B}\|D_b\|_{\mathrm{op}}$. The Gaussian block norm has unbounded support, so this maximum tends to infinity almost surely as $B\to\infty$. For each fixed threshold, the probability all $B$ blocks remain below it is a fixed number less than one raised to the $B$-th power; a countable threshold argument gives the assertion.

Correspondingly, multiplication by a Gaussian block is unbounded on the full block-population $L^2$ space. To see this without measurable singular-vector selection, fix a deterministic unit vector $e\in\mathbb R^k$ and take an input supported on ${\|D e\|>M}$, proportional to $e$. The ratio of its output $L^2$ norm to its input $L^2$ norm exceeds $M$. This event has positive probability for every $M$.

The bounded initialized population operators in C.1 are constructed from the *dense* width limit. Their operator bound therefore cannot be transplanted to the raw fixed-$k$ block population. A block proof may use polynomial moments, weighted spaces, or appropriately restricted generated fields; this is a repair to be proved, not a no-go theorem. At a fixed oracle transcript, polynomial envelopes and Gaussian moments suffice, so the issue does not invalidate the fixed-program observation in §1.

## 6. Sampling: what is affordable already, and what remains unproved

Here B denotes the number of independent block replicas; q is reserved for memory order. No dependence on that order is controlled by this sampling observation. For a supplied frozen-control oracle at a fixed time, let

\[
F_b(t)=\frac1k\sum_{i=1}^k w_{b,i}(t)h^L_{b,i}(t).
\]

If (\mathcal A$t$\le A_0), then (5) gives (|F_b$t$|\le A_0). Thus

\[
\left\|\frac1B\sum_{b=1}^B F_b(t)-\mathbb E F_1(t)\right\|_{L^2}
\le A_0/\sqrt B.
\tag{20}
\]

The constant is independent of $k$ and of the number of queries used to evaluate this particular oracle. For finitely many times, a direct sum-of-squares argument incurs a square root of their number. An all-time supremum needs temporal regularity or a more suitable process estimate; bounded values alone are insufficient.

For example, the following useful sufficient condition is elementary. If (F_b$s$) are iid absolutely continuous paths on ([0,S]), (F_b(0)=0), differentiation commutes with expectation, and (\mathbb E\int_0^S|F_b'$s$|^2ds\le V^2), then

\[
\mathbb E\sup_{s\le S}
\left|B^{-1}\sum_bF_b(s)-\mathbb EF_1(s)\right|^2
\le SV^2/B.
\tag{21}
\]

Indeed the centered average is the integral of its centered derivative, Cauchy–Schwarz contributes $S$, and independence divides the integrated derivative variance by B. A block-uniform derivative bound for the actual self-consistent oracle would verify this sufficient condition. It is not a consequence of (20).

Most importantly, (20) samples a prescribed oracle. In a finite autonomous closure, the sampled contractions alter subsequent queries, so the B blocks are no longer independent unconditionally at later times. An oracle-to-feedback stability argument with constants controlled jointly in k, B and memory order q is necessary. First-coordinate boundedness of $w$ does not bound the backward multiplier or its sensitivity to the law. No such all-time nonlinear feedback estimate is supplied by the fixed-program theorem.

For nonlinear training, neither a 1/k block bias nor a 1/sqrt(Bk) sampling variance is established here. Consequently this route cannot certify a learned-complexity exponent better than $\epsilon^{-4}$. A fixed finite-program convergence statement, without a modulus and joint sampling constants, cannot determine such an exponent.

## 7. Exact remaining bridge

A useful next proof obligation is a **uniform weak estimate for controlled, reused Gaussian block oracles**, retaining both orientations and every learned-memory contraction in (3). On a sufficiently small total-activity interval, it would need to prove the required moment and response discrepancies at order (1/k), uniformly over time meshes, while allowing singular and nearly repeated queries. The constants must be explicit functions of fixed depth, data bounds, and activity, with no dependence hidden in a query-Gram inverse or in a moment order growing with the mesh count.

Such an estimate is not assumed in this report. Its principal missing mechanism is a centered finite-$k$ error identity plus a summable second-order remainder for matrix reuse. Gaussian integration by parts and the weighted causal response rows are plausible ingredients, but a first-derivative response representation alone supplies neither identity nor remainder.

To convert that oracle estimate into the target, two further checked implications are needed:

* stability of the self-consistent residual/covariance/response equations on the small-activity interval, strong enough to compare the two nonlinear trained laws;
* all-time passage and finite-block feedback sampling with constants that remain affordable jointly in block size and replica count.

Section 4 proves the qualitative finite-network trained-law passage uniformly in B using the parent fitting theorem, and gives the conditional implication for any separately constructed fixed-k block population. It leaves the quantitative error production and joint memory/sampling complexity open. Failure of the fixed-program proof to supply those rates is a proof-route limitation, not a counterexample to the requested trained comparison.
