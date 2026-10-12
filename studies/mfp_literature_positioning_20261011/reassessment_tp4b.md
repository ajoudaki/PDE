# Independent reassessment: MFP versus Tensor Programs IVb

This comparison reads the complete `paper_MFP/main.tex`, its complete compiler guide `paper_MFP/code/MFP_CALCULUS.md`, and all 87 pages of **Tensor Programs IVb: Adaptive Optimization in the Infinite-Width Limit**, arXiv:2308.01814v2. Page references below are printed PDF pages. An independent text extraction and full v1/v2 diff found only title-page authorship/date/layout changes; the mathematical text is unchanged. I did not read earlier study reports, reviews, or verdicts. This report is a comparison of mathematical scope and constructive content, not a software audit.

The principal sources are [TP IVb v2](https://arxiv.org/abs/2308.01814v2), [TP III v2](https://arxiv.org/abs/2009.10685v2), and Golikov–Yang, [Non-Gaussian Tensor Programs](https://openreview.net/forum?id=AcHUIG2wA8-). Local primary PDFs were used for the actual proof reading. The OpenReview landing page was browser-blocked, but the main paper and supplementary PDF were available locally. Dependency checks and their limits are recorded at the end.

## Finding

**TP IVb already gives a constructive Gaussian expectation calculus for a primitive language strictly containing MFP's primitive language, together with an explicit general backpropagation construction.** It covers matrix identity and transpose reuse, causal empirical scalar feedback, singular limiting covariances, and—under the same polynomial smoothness used by MFP—scalar convergence in every finite $L^p$. These are not new mathematical principles introduced by MFP.

**MFP supplies an explicit end-to-end contract for a more specialized query language:** physical derivatives versus formal Gaussian-source derivatives, represented matrix directions, ambient gradients versus differentiation through update history, fixed-order moving-flow jets, and a restricted activation-moment normal form. TP IVb does not state that entire contract or give its complete compiler. A reader must still do exact finite algebra and prove closure of the requested derivatives and directions before applying its theorem. That work is mathematically meaningful because normalization, state dependence and parameter sharing can change the answer. It is also a finite chain-rule/adjoint/Stein construction very close to the machinery TP IVb already provides, rather than a new large-width limit mechanism.

Thus the two extreme descriptions are both inaccurate: “TP IVb only proves a primitive theorem, so MFP introduces derivative-to-Gaussian reduction” understates TP IVb; “the primitive theorem applies, so MFP contains only implementation” omits a real, explicit exact-compilation and normal-form result. A defensible contribution is the specified derivative calculus, its complete derivation and executable realization on an admitted language. A claim of a new general probabilistic theorem, or the first constructive treatment of scalar feedback, reuse, singularity or all-$L^p$, is unsupported by this comparison.

## The actual primitive-language embedding

MFP fixes a finite graph, equal width $n$ in every vector type, independent named Gaussian matrices $W:\tau\to\sigma$ with entries $N(0,1/n)$, Gaussian root tuples, and deterministic initial scalars. Its maps are finite expressions in constants, sums, products and activation derivatives $\phi^{(r)}$, where every derivative of $\phi$ has polynomial growth. Its main theorem is `thm-mfp-finite-derivative-program` (`main.tex`, line 695); the primitive definition starts at line 614.

TP IVb Definition 2.6.1, p. 20, has three instructions: `MatMul` by a named initial matrix or its transpose; `Avg`; and `OuterNonlin`, which applies a function to one coordinate tuple, finitely many further coordinate tuples averaged over indices, and all earlier scalar variables. Setting its outer-product order to $r=0$ is an ordinary coordinate function with scalar arguments. This is sufficient for MFP; the genuinely additional nonlinear outer products in TP IVb are not needed.

| MFP construction | Exact TP IVb realization and checked qualification |
| --- | --- |
| Coordinate map $v_i=F(u_i;s)$ | `OuterNonlin` with $r=0$, selecting the used vector and scalar arguments. |
| $n^{-1}\sum_i F(u_i;s)$ | That coordinate instruction followed by `Avg`. |
| Scalar sums, products, or admitted scalar functions | Broadcast the scalar function using `OuterNonlin`, then `Avg`; Lemma 2.6.2, p. 20, states exactly this construction. |
| $Wh$, $W^Tu$, including repeated uses | `MatMul`; the same matrix symbol is retained. Definition 2.6.5, Eq. (2.18), explicitly interprets equality as equality of program symbols, not random numerical equality. |
| Vector types | Retain the type restrictions as a syntactic restriction of TP IVb's equal-width vectors. No cross-type operation is added when forgetting type labels for the embedding. |
| Fixed nonzero root means and correlated or singular Gaussian root tuples | Write a root tuple as $\mu+BG$, $BB^T=K$, with independent standard Gaussian roots $G$, followed by a linear coordinate map. Setup 2.6.3 footnote 14, p. 20, explicitly makes this reduction. It needs no inverse or full rank. |
| Fixed deterministic scalar parameters | Keep them in the finite derivative calculation; for each specified value, absorb them into coordinate maps for the limit theorem. Equivalently use zero initial scalars and add the fixed constants. |
| $A=W_0+\sum_\nu c_\nu u_\nu v_\nu^T/n$ acting on $h$ | $W_0h+\sum_\nu c_\nu u_\nu\operatorname{Avg}(v_\nu h)$. The transpose lowers in the same way. These are exact identities. The training construction on pp. 23–24 and 46–47 already performs this update expansion, even for more general nonlinear outer-product updates. |

The root factorization is an evaluation device, not a change of trainable coordinates. If correlated roots are treated as separate ambient parameter blocks in MFP, take their physical derivatives first and then substitute $\mu+BG$. Differentiating with respect to $G$ instead would compute a different gradient metric. Similarly, first-layer columns shared across samples must stay shared; replacing sample preactivations by independent parameters changes the query.

Every finite MFP coordinate expression is polynomially smooth in the TP sense: finite product and chain rules preserve polynomial bounds on all derivatives. In particular its first derivative gives the pseudo-Lipschitz bound needed in Setup 2.6.3. It also satisfies Setup 2.6.4: Gaussian matrix entries have the stipulated moments $E|W_{ij}|^k=E|G|^k n^{-k/2}$, and deterministic initial scalars have all moments. The word “non-Gaussian” in that setup does not exclude Gaussian entries.

The derivative expansion must precede this embedding. TP IVb's theorem takes a fixed finite program, not a symbolic request that has not yet been shown to have such a program. Conversely, once the expansion has been proved, each derivative output is an ordinary scalar output, and its convergence does not require an interchange of width limits and differentiation.

## The Gaussian recursion is the same construction

Write TP IVb's ket of a vector $h$ as $Z^h$ for comparison, and its hat component of a matrix output as $\widehat Z^{Wh}$. For forward calls $y_r=Wh_r$ and reverse calls $v_s=W^Tu_s$, set

\[
H_r=Z^{h_r},\quad U_s=Z^{u_s},\quad
\xi_r=\widehat Z^{Wh_r},\quad
\zeta_s=\widehat Z^{W^Tu_s}.
\]

Then TP IVb Definition 2.6.5, pp. 21–22, Eqs. (2.18)–(2.19), gives exactly

\[
E[\xi_r\xi_t]=E[H_rH_t],\qquad
E[\zeta_s\zeta_v]=E[U_sU_v],
\]
\[
Z^{Wh_r}=\xi_r+\sum_{s\text{ earlier}}U_sE[\partial_{\zeta_s}H_r],
\qquad
Z^{W^Tu_s}=\zeta_s+\sum_{r\text{ earlier}}H_rE[\partial_{\xi_r}U_s].
\]

These are MFP's `eq-mfp-source-grams` and `eq-mfp-source-response` (line 760), with matrix variance factor one. The different oriented Gaussian groups are independent; the full outputs need not be. Means of inputs contribute to the *uncentered* second moments above. The expectation recursion is a finite construction, not an unspecified closure equation. TP IVb calls it an algorithm on pp. 12 and 40, defines it explicitly on pp. 21–22, and constructs its integrated program on pp. 77–79.

MFP's directed graph of Gaussian integrals follows by unrolling this construction in the $r=0$ subclass. All roots and hats on a type are a finite joint Gaussian family; each field is a specified function of that family and previously evaluated scalar coefficients. The final scalar assembly is polynomial because MFP only permits scalar sums/products outside averages. Giving this construction an explicit serialized graph is useful, but the mathematical Gaussian expectation evaluator is already present in TP.

### Physical scalar feedback versus source differentiation

These are different operations in both frameworks. For a physical variation,

\[
\delta F(u;s)=\sum_jF_{u_j}(u;s)\delta u_j+
\sum_bF_{s_b}(u;s)\delta s_b.
\]

The scalar variations include derivatives of finite empirical averages. TP IVb's backpropagation Definition 2.9.14, pp. 31–32, explicitly propagates adjoints to scalar arguments of `OuterNonlin` and backwards through `Avg`. It is therefore incorrect to say that it freezes empirical scalar feedback during physical differentiation.

For the *limit* evaluator the earlier scalars have already become deterministic coefficients, so formal hat/source partials hold them fixed. Definition 4.8.1, pp. 77–78, explicitly replaces scalars by their limits before differentiating the integrated coordinate functions. The earlier precise source convention is TP III Remark 2.11, p. 9, including footnote 16 for scalar parameters: differentiate the formal expression in named hat coordinates, with deterministic limiting scalar parameters supplied separately. Derivative paths through other earlier matrix calls remain inside that expression. MFP makes this separation conspicuous and executable; it does not add a previously missing response correction.

### Singular sources and query Grams

TP IVb's main statement has no nonsingularity assumption. The proof of its scalar-free base theorem invokes TP III's rank stability in §4.7.1, pp. 74–75, removes exact limiting dependencies, and calculates on the remaining full-rank block. Its general program is then compared with the integrated scalar-free program in Lemma 4.8.2, pp. 78–79. It does **not** assume rank stability for the original scalar-feedback program.

TP III's formal-source rule is expression-dependent (Remark 2.11, p. 9), and its pseudoinverse description in Remark 2.12, p. 10, covers singular covariance. For clarity, the invariant fact is about the **contracted correction**, not individual derivative coefficients. If $C=E[UU^T]$ is the covariance of reverse hats $\zeta$, Stein's identity gives $E[\zeta f]=C E[\nabla f]$. Two smooth representatives agreeing on the Gaussian support can have expected derivative vectors differing in $\ker C$, but $U^Ta=0$ almost surely for $a\in\ker C$, since $E(U^Ta)^2=a^TCa=0$. Their corrections agree. Thus one must not infer coefficientwise equality to a chosen pseudoinverse representative at singularity.

MFP's distinct formal slot for every call is a particularly explicit implementation of this convention. It is not a new singular-Gaussian limit principle. For duplicate calls $y_1=W1$, $y_2=W1$, keeping two perfectly correlated hats and taking the two partial derivatives before evaluating on their support gives the same total correction as a correctly rewritten one-hat program. Premature identification *without* the corresponding chain rule is the error; elimination of duplicate variables itself is permissible.

MFP's proof by small independent query perturbations and covariance-square-root continuity is an alternative self-contained proof strategy. It is useful that it never takes a singular empirical inverse limit. TP IVb has a different mechanism for the same smooth Gaussian query class, so the absence of MFP's perturbation proof in TP IVb is not an absent coverage result.

## What finite derivative work remains

### Backpropagation and ordinary finite updates are already constructive

TP IVb Definition 2.9.14 constructs a backpropagation program for an arbitrary representable program. Its normalized vector adjoint is exactly $n\nabla_yO$, and its scalar adjoint is $\partial_cO$, matching MFP's $b_y$ and $a_c$. The adjoint of `MatMul` uses the same transposed matrix. Definition 2.9.16 concatenates the backward programs and shares initial parameters across samples. The general update construction, Theorem 2.9.25, Eqs. (2.45)–(2.47), pp. 35–36, sums contributions from shared occurrences. For the admitted gradient-descent case the matrix contribution is a finite sum of normalized rank-one factors.

Definition 2.9.14 itself constructs scalar and vector adjoints; it does not store a dense matrix gradient as a program vector. Matrix parameters are nevertheless trainable in TP IVb's architecture and update definitions. To expose their gradients as MFP's represented matrix objects, use the exact identity $dO=b_v^T(dW)u/n$, hence $\nabla_WO=b_vu^T/n$, summed over all occurrences (with the reversed factors for transpose calls). This rank representation and its subsequent contraction/lowering are necessary finite algebra, not an additional matrix-limit theorem. The earlier Golikov–Yang supplement is even more explicit about matrix reuse: Proposition K.2, pp. 39–40 in the available supplement, writes separate sums over appearances of $A$ and $A^T$ for the exact derivative with respect to $A_{ij}$. Thus MFP's ambient reverse table, including both orientations, has direct constructive antecedents.

These facts already cover much more than “one can hope to differentiate a TP.” They are explicit finite algorithms. TP IVb §2.9, p. 29, says that general-architecture *limit proofs* are omitted as adaptations of the MLP proof; that is not an omission of the backpropagation construction itself. There is a local typographical caution: Remark 2.9.15's displayed $r=0$ vector rule prints $y_\alpha\psi_0$, whereas the defining rule immediately above and the chain rule require the adjoint $(d_xy)_\alpha\psi_0$. This does not obstruct the construction when the defining formula is used, but the display should not be copied literally into code.

### The full directional and moving-flow contract needs a finite closure argument

TP IVb does not separately specify arbitrary fixed-order moving-flow jets, frozen physical seeds, ambient current-state gradients versus history pullbacks, or the whole MFP contraction grammar. MFP's Proposition `prp-mfp-derivative-closure` (line 1261) supplies these statements. They can be derived from TP's operations and reverse construction as follows.

For a scalar observable $O$, let $b_u=n\nabla_uO$, let $a_s=\partial_sO$, and express each matrix gradient as

\[
\nabla_WO=\sum_\nu b_\nu h_\nu^T/n.
\]

An admitted direction has vector components $V_u$, scalar components $V_s$, and matrix components $V_W=\sum_\mu d_\mu p_\mu q_\mu^T/n$. Then

\[
D_VO=\sum_u\frac{b_u^TV_u}{n}+\sum_s a_sV_s
+\sum_{W,\nu,\mu}d_\mu
\left(\frac{b_\nu^Tp_\mu}{n}\right)
\left(\frac{h_\nu^Tq_\mu}{n}\right).
\]

Every term is a TP primitive scalar after normalization. The same statement follows by forward AD with $\delta(Wh)=(\delta W)h+W\delta h$. Products/chain rules preserve polynomial smoothness, and derivatives of finite rank sums remain finite rank sums. This verifies direction and gradient-contraction closure, including all normalizations; an arbitrary dense matrix direction would not pass this argument and is excluded by MFP.

Now define the moving Lie derivatives $O^{(0)}=O$, $O^{(r+1)}=D_VO^{(r)}$. At each step, the expression $O^{(r)}$ already contains the state dependence of $V$, so the next derivative differentiates it. In particular

\[
O^{(2)}=D^2O[V,V]+DO[DV[V]].
\]

For every *fixed* $R$, this is a finite primitive program by induction. Along a local finite-width solution $\dot\theta=V(\theta)$, its value equals $d^rO(\theta(t))/dt^r|_{t=0}$; the factorial-normalized jet is $O^{(r)}/r!$. Equivalent truncated-polynomial coefficient recurrences are given explicitly by MFP. No common positive-time existence interval and no derivative of an infinite-width trajectory are needed. Applying TP IVb to the compiled program gives each coefficient's limit.

This is an additional exact closure theorem relative to TP IVb's written statements, but its proof is a short finite induction once TP's backpropagation and the admitted rank structure are available. Calling it a new general infinite-width principle would inflate the difference. Calling it unnecessary would be wrong: freezing $V$ deletes $DO[DV[V]]$, and a syntactic compiler must distinguish that request. MFP's example $\dot x=-x^3$, $O=\operatorname{Avg}(x^2)$ yields $O''=8\operatorname{Avg}(x^6)$, while the frozen straight direction gives $2\operatorname{Avg}(x^6)$; TP can evaluate either after the correct finite expression is supplied.

Ambient gradients after training need the same care. First differentiate the current-parameter loss template, then substitute a represented updated state. Differentiating the already substituted loss instead computes a pullback through training history. Both are finite TP queries, but TP IVb's existence theorem does not choose which the caller meant. MFP's explicit substitution and seed semantics make that choice reviewable.

### Restricted activation-moment form is a separate output theorem

MFP's Proposition `prp-mfp-initialization-normal-form` (line 1343) assumes every nonlinear argument in the compiled initialization program is literally an original feedforward preactivation. Under that restriction, its field algebra consists of sums of

\[
cP(Z)\prod_\nu\phi^{(r_\nu)}(Z_{a_\nu}),
\]

where $Z$ is a finite centered joint Gaussian family, $P$ is polynomial, and $c$ depends polynomially on earlier scalar expectations. Formal differentiation and the TP source rule preserve this class. Repeated Stein integration by parts

\[
E[Z_iF(Z)]=\sum_jK_{ij}E[\partial_jF(Z)]
\]

removes explicit Gaussian factors by induction on the degree of $P$, leaving covariance polynomials and moments of activation derivatives. Writing $Z=BG$ proves the identity without an invertibility assumption. The covariance coefficients are already specified by preceding expectations, so the result is a finite recursive normal form.

TP IVb's Gaussian calculus supplies the starting expressions and repeatedly uses Stein's identity, but it does not state this literal-preactivation subclass or prove this terminating output reduction. This is a real additional symbolic theorem. Its mechanism is elementary Gaussian integration by parts; the limited syntactic contract, termination proof and implementation are the added content. It does not apply to generic updated preactivations or arbitrary nested nonlinearities. Nor should “finite Gaussian expectation graph” be equated with evaluation in elementary functions: TP IVb p. 81 explicitly notes that its general expectations lack analytic closed forms, and MFP likewise retains generic integrals.

## Modes of convergence and proof status

Theorem 2.6.10, p. 23, states almost sure scalar convergence for Gaussian Setup 2.6.3 and almost sure plus every-finite-$L^p$ convergence for Setup 2.6.4. For initial scalar errors $\widetilde O(n^{-1/2})$, it also states that rate for generated scalar errors. Fixed deterministic inputs, after absorbing their values, have exactly zero error and meet this stronger assumption.

The relevant Gaussian proof is §§4.7–4.8, pp. 74–79. Lemma 4.8.2 supplies vectorwise distributional equivalence with iid ket samples. Independently, applying the scalar theorem to a countable determining set of bounded Lipschitz tests and to the squared norm yields weak empirical convergence plus second-moment convergence, hence empirical $\mathcal W_2$ convergence. This gives MFP's same-type empirical conclusion; no additional probability theorem specific to neural derivatives is needed.

Be careful with TP IVb's term “moment-bounded” in Definition 4.3.1, p. 60: it means an almost sure subpolynomial bound on empirical moments. **It is not by itself MFP's uniform bound on expected moments.** The latter follows instead from the raw-entry moment bounds: TP IVb Lemma 4.9.2, p. 80, with empty differentiation multiset, or directly Golikov–Yang Lemmas J.3 and J.6 in the locally available supplement, pp. 32–38. For an MFP vector (v), Jensen then gives

\[
E\left(\frac1n\sum_i|v_i|^p\right)^q
\le\frac1n\sum_iE|v_i|^{pq}\le C_{p,q}.
\]

The original Golikov–Yang lemma already permits scalar feedback, polynomial smoothness, arbitrary fixed derivative order in raw matrix entries, and variances only bounded above by $C/n$; its proof shrinks selected entries to zero and uses singleton cancellation. These are precisely the main features of MFP's adapted raw-entry proof. Combining the expected moment bounds with TP IVb's Gaussian convergence and uniform integrability proves every finite scalar $L^p$ conclusion directly. This route needs neither new nonlinear-outer-product interpolation nor the deferred slow-scalar theorem.

The following proof-status distinctions matter:

| TP IVb item | What the source actually supplies | Relevance to MFP |
| --- | --- | --- |
| Fast-initial-scalar Gaussian theorem | A detailed proof in §§4.7–4.8, using the earlier TP III master theorem and rank-stability result. | Directly applicable after exact finite derivative compilation. |
| Arbitrarily slowly converging initial scalars, §4.9.1, p. 79 | An asserted uniform local Lipschitz property and proposed sub-Weibull/chaining route; full details are explicitly deferred to a future paper. | Outside MFP's fixed deterministic initial scalar requirement. MFP does not repair a needed gap here. |
| Full non-Gaussian `OuterNonlin` theorem, §4.9.2, pp. 79–80 | Reduction to Golikov–Yang's interpolation proof and short adaptation arguments for expected-smoothness Lemmas 4.9.2–4.9.3; the entire adapted proof is not written out. | A genuine distinction between a theorem statement and a fully reproduced proof, but not a missing MFP Gaussian result. MFP's $r=0$ moment estimates already occur in the cited dependency. |
| General architecture limits, §2.9, p. 29 | Definitions, backpropagation and limit formulas; full general-architecture proofs are omitted as adaptations. | Does not erase the supplied finite backpropagation construction or the primitive master theorem. MFP need not invoke these broader training-limit statements. |
| Literal source derivatives at singularity | Formal-source semantics inherited from TP III and the invariant contracted response; the proof avoids singular inverse continuity through rank-stable integrated programs. | Same substantive smooth-source coverage; MFP offers a particularly explicit slot-preserving implementation and an alternative proof. |
| ReLU/general nonsmooth training extensions | Assumption 2.3.2 excludes the discontinuity of ReLU's derivative (p. 15); extension is an expectation, not a proof. | MFP also assumes smooth activations; no additional coverage. |
| Positive-time gradient-flow reconstruction | The continuous-time discussion in §2.4.1 is explicitly intuition; the stated training limits concern fixed discrete steps. | Neither this nor MFP's finite jet theorem justifies an infinite Taylor sum, a common flow horizon, or differentiation of a limiting trajectory. |

There are typographical and broader theorem issues in TP IVb that a full audit of all its optimizer classification claims would have to assess. They are not used to discount its Gaussian program theorem here. In particular, the broad classification and arbitrary-architecture NT claims are not premises of the reduction above.

## Counterfactual: what a reader with TP IVb must still do

Suppose the query is MFP's two-layer feature kernel

\[
K_{n,ab}(t)=\frac{h_a^{(2)}(t)^Th_b^{(2)}(t)}n,
\qquad
J_R=\lim_{n\to\infty}E\left[\frac1{R!}\frac{d^R}{dt^R}K_{n,ab}(0)\right],
\]

for fixed arbitrary $R$, half-mean squared loss, the specified shared first-layer columns, order-one stored readout, vector mobility $n$, and matrix mobility one. TP IVb does not print $J_R$ or supply MFP's `jets` call. The reader must:

1. Encode the actual finite forward model and loss, retaining the data normalization, shared columns and readout scale. Check that the physical metric matches the desired clock.
2. Use its backpropagation construction to form the finite physical vector field, with all shared matrix occurrences contributing. Express matrix velocities as normalized finite rank sums.
3. Apply the Lie-derivative recursion or truncated Taylor recurrence $R$ times, differentiating residuals, scalar averages, rank factors and the moving field. Prove by the finite induction above that this produces a finite $r=0$ TP. Frozen seeds require their separate physical convention.
4. Verify polynomial smoothness of every introduced expression, and represent the sampled Gaussian roots only after those physical derivatives have been fixed.
5. Apply Definition 2.6.5 chronologically, computing source Grams and response partials. Apply Theorem 2.6.10 with the expected moment bound to obtain convergence of the actual coefficient and its expectation.
6. If the query meets MFP's initialization restriction, perform the terminating Stein reduction to get only activation-derivative moments. Implement expression sharing, source naming, output formatting and tests if an executable reusable tool is desired.

Steps 1–3 and 6 are substantial work for a reliable general-purpose artifact, and they remove repeated derivations for users. Steps 3 and 6 also require correctness proofs, not just tests. They introduce no new unknown large-width law: after compilation, steps 4–5 are exactly the prior constructive TP machinery. No admitted MFP query identified in this review requires a new probabilistic mechanism beyond it.

## Dependency and verification record

Read completely: MFP `main.tex` (including the appendix and compiler material), `code/MFP_CALCULUS.md`, and TP IVb v2. Compared the complete independent v1/v2 text extractions; only the title page differs. No code was run or audited, and the correctness of the shipped implementation is not certified here.

Checked in TP III v2: Box 1 and Theorem 2.10, pp. 8–9; Remarks 2.11–2.12, pp. 9–10; the exact statement and complete proof of rank/zero stability in §L.5, pp. 67–69. The §L.5 proof depends on its earlier `CoreSet`, `Moments`, `Density` and `NullAvoid` induction. I did not re-audit every earlier page of TP III's master-theorem proof. TP IVb's dependence on that theorem is explicit (§4.7.1), and this report distinguishes that external dependency from TP IVb's own proof.

Checked in the available Golikov–Yang main paper: Setup 3.6 and Theorem 3.7, pp. 5–6, and the proof reduction and uniform-integrability argument in §5, pp. 8–9. Checked the complete moment argument in supplement Appendix J, pp. 31–38, its backpropagation and shared-matrix derivative construction in Appendix K.1 and Lemma K.6, pp. 38–41, and the $L^p$ upgrade in Appendix M, p. 43. TP IVb cites an earlier numbering: its I.3/J.6 corresponds to J.3/K.6 in this available supplement. The exact sharper scalar raw-entry derivative estimate is not needed for the MFP scalar-$L^p$ comparison; the empty-order vector/scalar bounds suffice. I did not audit the full non-Gaussian interpolation appendix, because no interpolation is needed for the Gaussian $r=0$ reduction used here.

I checked the elementary finite closure, normalization, source mapping, covariance factorization and Stein-reduction arguments explicitly above. I did not infer correctness of a derivative-of-limit or positive-time statement; none is needed. I did not inspect other studies, repository research history, or earlier findings. All extraction scratch is under `data/generated/mfp_literature_positioning_20261011/reassessment_tp4b/`.

## Coordinator provenance and presentation check

The coordinator read this report completely and repaired a malformed source link and inline delimiters inside two display equations; mathematical content is unchanged. SHA-256 values of the referenced frozen inputs:

- `paper_MFP/main.tex`: `a43acbc76e53a3437ed5136137fd8e5497a6d65826447c1ac95764a1cba8d38e`.
- `paper_MFP/code/MFP_CALCULUS.md`: `1c160b03f79e488a271923ed696f5871b054f88bd8fb6e3ec2c10c513fc2f5c2`.
- `data/generated/mfp_literature_positioning_20261011/tp4b/tp4b-v2.pdf`: `fb5653c418d4b35dbd5133810cc9313a75a2167b820dada18d6428b3bb0538b1`.
- `data/generated/mfp_literature_positioning_20261011/tp3/tp3v2.pdf`: `02c16245dc9ebb60ffdbe0c1076e52b045d7397680b3354e87c7440ce88e1a71`.
- `data/generated/mfp_literature_positioning_20261011/nongaus/appendix.pdf`: `d72e99b926952aa133d28f21216783f46ea652c5877a68bd5d765563a7f4adb8`.
