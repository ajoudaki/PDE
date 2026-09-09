# Isolated adversarial review of Part V

## Verdict

**MINOR STATEMENT CORRECTIONS REQUIRED; substantive proof passes.**

I found three local precision defects: missing off-diagonal qualifiers on several separation hypotheses, an unqualified claim about “every integer power” that must be restricted to nonnegative integers, and unstated gain assumptions in the final normalization comparison. These are specified and corrected below. None requires changing the principal theorems, numerical constants, asymptotic orders, witnesses, or sequential limit under their intended hypotheses.

I found no substantive gap in the initialized finite-width identification, Gaussian/Hermite arguments (including singular endpoints), cubic tensor floor, sharp odd-mixture bounds, convex-offset contraction and nonaffinity bounds, or calibrated width-first/depth-second limit. This verdict is not a claim about training.

## Input identity, isolation, and complete read coverage

Only the following two source files were accessed:

| Input | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| /tmp/pde-initialization-round2.oESDjqeW/PROOF.md | 1329 | 47916 | df2ce22964bfc0f835d59764f9a9ef589e1597350c8d7b385a7f204a9db3589f |
| /tmp/pde-initialization-round2.oESDjqeW/NOTATION.md | 98 | 5110 | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |

Both files were read fully through EOF. The complete proof reading covered lines 1–340, 341–680, 681–1020, and 1021–1329. A combined tool display truncated part of the 681–1020 range; that entire range was subsequently reread separately without truncation. NOTATION.md was read in one complete display, lines 1–98. The final proof line ends with “they are not recursions for trained non-Gaussian laws.” The final notation line ends with “finite-dimensional scalar state.”

The hashes above were obtained before reading and independently checked again after the mathematical review; they agreed exactly. No input edits were made. No other project, study, history, prior-review, or skill source was accessed. No network, agents, numerical experiments, symbolic computation software, or research computations were used. The mathematical checks below are analytic checks of the supplied text.

The report directory was genuinely created during this review by a successful fresh temporary-directory creation:

    /tmp/pde-part-v-adversarial-review.CgoGLY5K

This report was written with apply_patch. All line references below refer to the exact hashed PROOF.md, unless NOTATION.md is named explicitly.

NOTATION.md was used as the supplied convention contract. The review verifies all statements and steps of Part V, including its final comparison paragraphs; it does not purport to establish unrelated training results mentioned in the notation contract.

## Findings and precise corrections

### F1. Separation hypotheses omit the off-diagonal quantifier

**Severity:** minor statement/quantifier defect; the intended interpretation is clear.

**Locations:** lines 362–364 (V.F.3), 604–605 (scope of the odd lower bounds), 1049–1051 (calibrated separated geometry), and 1270–1272 (comparison scope).

The phrases imposing \(|C_{ab}|\le1-\delta\) or \(|G_{ab}|\le1-\delta\) do not explicitly restrict the indices. For a unit-diagonal matrix and \(\delta>0\), imposing the inequality on all entries would require \(1\le1-\delta\), which is impossible. Read literally with unrestricted indices, these hypotheses have no instances.

The intended off-diagonal meaning is supported by the explicitly correct quantifier in (V.O.2), lines 414–415, and by the tensor construction, which only uses distinct samples. The intended lower bounds are valid, as checked below. This is a vacuity/precision issue, not a counterexample to those intended bounds.

**Precise correction:** in each listed hypothesis, write

\[
 |C_{ab}|\le1-\delta\quad\text{for all }a\ne b,
 \qquad\text{or}\qquad
 |G_{ab}|\le1-\delta\quad\text{for all }a\ne b,
\]

as appropriate. Alternatively, state once before V.F.3 that all separation inequalities in Part V apply only to distinct samples, while retaining the explicit qualifier in theorem statements.

No numerical bound changes.

### F2. “Every integer power” is too broad

**Severity:** minor wording defect with a false literal extension.

**Location:** lines 393–396.

The text says that “every integer power” \(C^{\circ j}\) is positive semidefinite because it is the Gram of tensor powers. This argument and conclusion apply to nonnegative integer powers. They do not apply to negative integers.

For an elementary counterexample to the unrestricted wording, take the three-by-three correlation matrix with diagonal 1 and every off-diagonal entry \(1/2\). It is

\[
 C=\tfrac12 I_3+\tfrac12\mathbf1\mathbf1^T,
\]

with eigenvalues \(2,1/2,1/2\). Its entrywise reciprocal is

\[
 C^{\circ(-1)}=2\mathbf1\mathbf1^T-I_3,
\]

with eigenvalues \(5,-1,-1\). Thus it is not positive semidefinite. Negative powers would also be undefined at zero entries in other allowed matrices.

**Precise correction:** replace “every integer power” by “every nonnegative integer power.” Keep the explicit degree-zero convention \(C^{\circ0}=\mathbf1\mathbf1^T\), including when some entries of \(C\) vanish.

Every use in Part V already has nonnegative degree, so this correction affects no subsequent derivation.

### F3. The gain-to-convex comparison needs local parameter assumptions

**Severity:** minor self-containment/scope defect in the comparison paragraph.

**Location:** lines 1288–1290.

The assertion that dividing \(a(1+z)+e\psi(z)\) by \(a+e\) creates a literal convex activation needs assumptions on \(a,e\). Those assumptions have not been stated at this point in the supplied inputs. Merely referring to Part III cannot supply them in this isolated review.

Algebraically the proposed mixture parameter is

\[
 \varepsilon=\frac{e}{a+e}.
\]

A positive convex combination follows from \(a>0,e>0\). To place it specifically within V.C's stated range \(0<\varepsilon<1/2\), one needs \(a>e>0\). Without suitable restrictions, the denominator can vanish or the coefficients can fail to be convex. For example, \(a=1,e=-1\) makes the division undefined. This example diagnoses the missing local assumptions; it does not assert that such gains were allowed in the uninspected Part III.

The stronger assumptions \(a-e>1\), \(0<e\le1\) do appear later, at lines 1301–1302, but are introduced for the subsequent growth argument.

**Precise replacement for the opening comparison:**

> For \(a>e>0\) and a shape \(\psi\) satisfying the assumptions of V.C, consider \(g(z)=a(1+z)+e\psi(z)\). Setting \(\varepsilon=e/(a+e)\in(0,1/2)\) gives \(g/(a+e)=(1-\varepsilon)(1+z)+\varepsilon\psi(z)\). This division changes the Gaussian recursion under the fixed matrix initialization.

If only a convex combination with parameter in \((0,1)\) is intended, \(a,e>0\) suffices, but V.C's theorem should then only be invoked when \(a>e\). The later gain-growth estimates are already correctly qualified.

## Complete verification ledger

The ledger accounts for the entire proof, including unnumbered arguments and comparison statements. “Pass” below uses the explicit off-diagonal interpretation from F1 and the nonnegative-degree interpretation from F2; the final gain comparison uses the correction in F3.

### 1. Model, metrics, and observables — lines 1–142

**Pass.**

The dimensions and storage in (V.M.1)–(V.M.3) agree with NOTATION.md, lines 10–24 and 72–75. The first preactivation is \(W^{(1)}u_a\), so its covariance is exactly \(G\), with no missing factor of \(d\). Alternative storage \(V^{(1)}=W^{(1)}/\sqrt d\) gives both the advertised variance \(1/d\) and \(dW^{(1)}=\sqrt d\,dV^{(1)}\). Consequently the first metric term becomes \(d\|dV^{(1)}\|_F^2/n\), as stated.

The inverse metric multiplies first-layer and readout Euclidean gradients by \(n\), and leaves middle-layer gradients unchanged. The loss derivative factor \(2/3\) is correctly excluded from the gradient Gram itself.

The common diagonal in (V.M.5) depends only on the previous common diagonal and the fixed activation: every preactivation marginal is \(N(0,q_{\ell-1})\). A nonzero feature mean does not become a preactivation mean, since the next matrix is independently centered. Its preactivation covariance is the uncentered feature second moment \(Q_\ell\).

For a unit-diagonal positive semidefinite three-by-three matrix, trace three gives \(1\le\lambda_{\max}\le3\). This proves every inequality in (V.M.7), including the factor three relating the two scale-free quantities. The matrices being called normalized Grams are not incorrectly identified as centered feature Pearson correlations.

For \(q>0\), the spans of \(\{1,\sqrt q\,\xi\}\) and \(\{1,\xi\}\) agree. These two latter coordinates are orthonormal in Gaussian \(L^2\), which gives the attained minimum (V.M.9). Continuity and at-most-linear growth ensure the required second moments. Positive denominators for all three activation families follow from the variance arguments below.

### 2. Fixed-depth width limit and initialized raw kernel — lines 144–260

**Pass.**

At the first layer, rows are independent Gaussian triples even when \(G\) is singular. Linear growth and Gaussian fourth moments make the variance of each activated product finite. Chebyshev applies entry by entry.

At a later layer, conditioning on preceding features gives independent Gaussian rows with covariance exactly \(\widehat Q_{\ell-1}\) in (V.F.1). On a bounded-diagonal event, Cauchy–Schwarz and fourth-moment bounds control all activated-product second moments uniformly; no lower eigenvalue bound is needed. The conditional Chebyshev estimate is therefore valid at singular covariances as well.

Inductive convergence makes the preceding diagonals bounded by some fixed \(M\) with probability tending to one. The conditional expectation converges because the positive square root is continuous on the entire positive semidefinite cone. The supplied bounded-subsequence argument proves that continuity: any subsequential root limit is positive semidefinite and squares to the same limit matrix, whose positive square root is unique. Gaussian coupling then gives activated-coordinate \(L^2\) convergence, and Cauchy–Schwarz gives product-expectation convergence. Finitely many entries and layers give the claimed joint convergence in probability.

Direct differentiation gives the three parameter derivatives stated at lines 211–215. Their metric pairings yield exactly (V.F.3):

\[
 K^{(1)}_{n,ab}=G_{ab}\frac{\delta_a^T\delta_b}{n},
 \qquad
 K^{(\ell)}_{n,ab}
 =\frac{\delta_a^T\delta_b}{n}\frac{h_a^Th_b}{n},
 \qquad
 K^{(L+1)}_{n,ab}=\frac{h_a^Th_b}{n}.
\]

There is no residual in the backward derivative and no hidden loss factor.

For the operator-norm bound, a maximal \(1/4\)-separated spherical set is a \(1/4\)-net. The disjoint radius-\(1/8\) balls fit in a radius-\(9/8\) ball, giving cardinality at most \(9^n\). Approximating each of the two vectors in a bilinear form incurs at most \(\|W\|_{\mathrm{op}}/2\), giving the factor two. Each fixed bilinear form has variance \(1/n\); threshold five has two-sided tail at most \(2e^{-25n/2}\). Union over at most \(9^{2n}\) pairs gives (V.F.4), whose exponent is strictly negative.

The readout moment is exactly

\[
 \mathbb E\|W^{(L+1)}\|_2^2/n=n^{-2}.
\]

Thus its RMS is \(O_{\mathbb P}(n^{-1})\). Bounded derivatives and finitely many hidden operator norms give (V.F.5) without requiring backward fields to be independent of the forward fields. Hidden kernel blocks are \(O_{\mathbb P}(n^{-2})\), since feature RMS values are bounded in probability. Only the readout block survives, proving (V.F.6). The displayed Cauchy–Schwarz bound also proves \(f_{n,a}\to0\).

For \(L=1\), the empty hidden-matrix product is one and the argument still applies. No estimate is uniform in a growing number of layers. The comment about zero limiting backward fields is consistent with the zero readout; no unspecified trained population operator is needed for the kernel proof.

### 3. Gaussian completeness, differentiation, and endpoints — lines 262–358

**Pass.**

The generating-function product has expectation \(e^{st}\), establishing Hermite orthonormality with the stated normalization. In the completeness proof, the complex generating series at \(i\eta\) is Cauchy in Gaussian \(L^2\), because

\[
 \sum_{j\ge0}\frac{|\eta|^{2j}}{j!}=e^{\eta^2}<\infty.
\]

Its entire pointwise sum identifies the \(L^2\) limit, for example by taking an almost-everywhere convergent subsequence. Pairing with a function orthogonal to all polynomials makes its Gaussian-weighted integrable density have zero Fourier transform.

The Fourier uniqueness argument is contained. Gaussian integration by parts gives the characteristic function; scaling gives the Gaussian Fourier integral. The stated absolute-integrability bound justifies Fubini when convolving the \(L^1\) density with a Gaussian. Translation continuity, obtained from interval step functions and \(L^1\) approximation, proves the approximate-identity convergence. Therefore the density is zero and completeness follows. No external harmonic-analysis theorem is left as an essential unproved dependency.

The joint generating function gives (V.F.8) even at \(\rho=1\) and \(\rho=-1\), where the pair is singular. Polynomial approximation and Cauchy–Schwarz legitimately extend the covariance formula to \(L^2\) functions. Parseval gives absolute convergence at both endpoints.

For the stated \(C^2\), bounded-derivative, at-most-linear class, the Gaussian integration-by-parts boundary terms vanish. The degree-lowering coefficient formulas in (V.F.10) have factors \(\sqrt j\) and \(\sqrt{j(j-1)}\), respectively. Applying Parseval to the derivatives gives finite sums \(\sum j a_j^2\) and \(\sum j(j-1)a_j^2\). These dominate the differentiated covariance series uniformly on the closed correlation interval.

The text correctly distinguishes the endpoint signs:

\[
 C_f'(-1)=\sum_{j\ge1}(-1)^{j-1}j a_j^2,
 \qquad
 C_f''(-1)=\sum_{j\ge2}(-1)^{j-2}j(j-1)a_j^2.
\]

It does not substitute the unsigned values at \(+1\) at the negative endpoint. Endpoint derivatives are correctly one-sided.

For (V.F.11), \(1-\rho^j\le j(1-\rho)\) remains true for negative \(\rho\): every summand of \(\sum_{k=0}^{j-1}\rho^k\) is at most one. The derivative of \(f(x)=\phi(\sigma x)\) contributes \(\sigma^2\) to its squared derivative moment. Finally \(\mathbb E(X-Y)^2=2\sigma^2(1-\rho)\), proving exactly the stated contraction factor. All three applications meet the supplied regularity assumptions; no endpoint approximation or nondegeneracy assumption is missing.

### 4. Cubic tensor floor — lines 360–396

**Pass after F1 and F2.**

For distinct indices, separation gives \(1-C_{ab}^2\ge\delta(2-\delta)>0\). Thus \(v_{ab}\) is well-defined, unit length, perpendicular to \(v_b\), and has pairing \(\sqrt{1-C_{ab}^2}\) with \(v_a\).

The nonsymmetric tensor \(T_a=v_a\otimes v_{ab}\otimes v_{ac}\) is a valid unit test tensor. It annihilates both other cubic sample tensors; symmetry of \(T_a\) is unnecessary. Its pairing with its own sample tensor is at least \(s_\delta=\delta(2-\delta)\).

Consequently, for \(T=\sum_a b_av_a^{\otimes3}\),

\[
 s_\delta^2\sum_a b_a^2
 \le \sum_a|\langle T_a,T\rangle|^2
 \le 3\|T\|^2.
\]

The final inequality uses three separate unit-vector Cauchy–Schwarz estimates, not an incorrect claim that the \(T_a\)'s are orthogonal. Since \(\|T\|^2=b^TC^{\circ3}b\), the floor \(s_\delta^2/3\) is correct. The original Gram can be singular, and \(\delta=1\) is allowed whenever the input is realizable.

### 5. Odd-mixture statement and variance bounds — lines 398–547

**Pass.**

The theorem explicitly quantifies \(L\ge1\), \(0<\theta\le1\), \(0<\delta\le1/4\), and every \(d\ge2\). Its strict admissible set is nonempty by the later planar witness. The lower argument actually covers the closed off-diagonal separation condition up to \(\delta=1\), as stated.

Writing \(\phi_\theta(z)=z-\theta u(z)\), integration by parts gives
\(\mathbb E[Z\arctan Z]=q\mu(q)\). The linear projection coefficient is therefore \(c(q)\). Jensen gives \(c(q)\ge1/(1+q)\ge1/2\), hence \(q_+\ge qc(q)^2\ge q/4\). Strict shrinkage for nonzero inputs gives \(0<q_+<q\).

The decrement identity is exact. Since \(u(z)\) has the sign of \(z\) and \(|u(z)|\le|z|\), one has \(0\le u(z)^2\le zu(z)\), giving both decrement bounds before (V.O.5). The weighted Cauchy–Schwarz calculation has numerator \((\mathbb E\xi^2)^2=1\) and second factor \(\mathbb E[\xi^2(1+q\xi^2)]=1+3q\). It follows that

\[
 \frac{q}{1+3q}\le1-\mu(q)\le q,\quad
 \frac{\theta}{4}q^2\le D(q)\le2\theta q^2,\quad
 \frac{\theta}{4}\le\frac{D(q)}{qq_+}\le8\theta.
\]

This proves every constant in (V.O.5) and the reciprocal-variance bounds (V.O.6).

The lower bound on \(\sum_{k<L}q_k^2\) is the integral of the decreasing function \((1+8\theta x)^{-2}\), namely \(L/(1+8\theta L)\). The upper bounds are respectively \(q_k\le1\) and the telescoping estimate
\((\theta/4)\sum_{k<L}q_k^2\le q_0-q_L\le1\). The elementary split at \(\theta L=4\) proves the final factor five in (V.O.7).

Oddness eliminates all even Hermite degrees. The coefficients \(w_j\) are nonnegative and sum to one, giving both the correlation recursion and \(|K_q(\rho)|\le|\rho|\) for the full interval, not just positive correlations.

The residual \(R(q)\) is exactly the nonlinear Hermite mass. Testing against the identity and using \(|u(z)|\le|z|^3/3\) gives \(R(q)\le(15/9)\theta^2q^3=(5/3)\theta^2q^3\). Since \(c(q)^2\ge1/4\), the logarithmic linear-weight bound is \(20\theta^2q^2/3\). Summing over any finite layer set gives at most \((20/3)4\theta\le80/3\); thus all the stated linear-weight products, including an empty product, are bounded below by \(p_*=e^{-80/3}\).

### 6. Cubic injection and the explicit lower constants — lines 549–607

**Pass, with F1's explicit off-diagonal qualifier.**

The two integration-by-parts steps in (V.O.12) give

\[
 \frac{\sqrt q}{\sqrt6}\,
 \mathbb E\frac{\xi^2-1}{1+q\xi^2}
 =-\sqrt{\frac23}\,q^{3/2}
 \mathbb E\frac{\xi^2}{(1+q\xi^2)^2}.
\]

The size-biased measure \(\xi^2\,d\mathbb P\) is a probability measure and has mean three for the variable \(\xi^2\). Jensen for \((1+qt)^{-2}\) gives the lower bound \(1/16\) on the expectation for \(q\le1\). Squaring gives \(b_3(q)^2\ge q^3/384\), and dividing the mixture's cubic mass by \(q_+\le q\) gives \(w_3(q)\ge\theta^2q^2/384\).

Every other nonnegative-degree tensor Gram contributes a positive semidefinite matrix. Separating the degree-one and degree-three terms gives exactly

\[
 C_\ell\succeq w_1(q_{\ell-1})C_{\ell-1}
       +\frac{s_\delta^2}{3}w_3(q_{\ell-1})I_3.
\]

Iteration only propagates each scalar injection through subsequent linear weights; no unjustified matrix-monotonicity property of the nonlinear correlation map is used. Those products are at least \(p_*\), giving denominator \(3\cdot384=1152\). The sum bound and then the variance lower bound prove (V.O.14) and (V.O.15).

Finally \(s_\delta\ge\delta\) and \(1+8\theta L\le8(1+\theta L)\) give

\[
 1152\cdot8=9216,\qquad 1152\cdot64=73728,
\]

which are exactly the two stated theorem denominators. The strict input inequalities pose no difficulty, since the proof applies to the larger closed admissible set.

### 7. Composed curvature and strict planar witness — lines 609–722

**Pass.**

Composition of odd probability generating series preserves nonnegative odd coefficients. On \([0,1)\), rearrangement is justified by nonnegative terms; monotone convergence at one gives total coefficient mass one. Oddness and absolute convergence extend the same identity to negative arguments.

The endpoint derivative formulas (V.O.17) include the correct scaling powers \(q_k\) and \(q_k^2\). From
\(\phi_\theta''(z)=-2\theta z/(1+z^2)^2\) and \(q_{k+1}\ge q_k/4\), one obtains
\(b_k\le16\theta^2q_k^2\).
Since only odd degrees occur, \(d_k\ge1\) and
\(d_k-1\le b_k/3\). The sums are at most \(64\) and \(64/3\), respectively.

The chain rule gives \(A_{k+1}=d_kA_k\) and \(B_{k+1}=b_kA_k^2+d_kB_k\). Dividing the second recurrence by the first and summing yields the displayed exact formula
\(B_L=A_L\sum_{k<L}(b_k/d_k)A_k\).
With \(A_k\le e^{64/3}\), it gives

\[
 F_L''(1)\le16e^{128/3}\theta^2\sum_{k<L}q_k^2
 \le80e^{128/3}\frac{\theta^2L}{1+\theta L}.
\]

Finite composition has continuous one-sided endpoint derivatives. The identification \(F_L''(1)=\sum_jj(j-1)p_{j,L}\) is valid: differentiate the power series in the open interval and pass to one by nonnegative monotone convergence and continuity of the second derivative.

For the witness, \(c=1-2\delta\in[1/2,1)\) and \(r=2c^2-1\). Both separation margins for \(c\) are positive. The margins for \(r\) are exactly

\[
 \delta(7-8\delta),\qquad
 2-9\delta+8\delta^2=(1-4\delta)(2-2\delta)+\delta.
\]

Both remain positive at \(\delta=1/4\), where \(c=1/2\) and \(r=-1/2\). The same witness embeds in every \(d\ge2\).

The input-vector combination \(u_1-2cu_2+u_3\) vanishes, so \(Gv=0\) for \(v=(1,-2c,1)\). Its norm squared is \(2+4c^2\ge3\). The stated formula for \(E_j(c)\), both zero conditions at \(c=1\), and its second derivative are correct. On the whole interval, including where \(r<0\), the absolute derivative bound is

\[
 8+8j+32j(j-1)+8j(j+1)
 =40j^2-16j+8\le54j(j-1)
\]

for all integers \(j\ge3\). At \(j=3\), the difference polynomial is \(14j^2-38j-8=4>0\), and it increases thereafter.

Taylor's integral remainder thus gives \(E_j(c)\le27j(j-1)(1-c)^2\). Its nonnegativity separately follows from the tensor Gram, so all summations are justified. Dividing by the norm squared and using \(1-c=2\delta\) gives \(36\delta^2 F_L''(1)\). Therefore the normalized upper constant is \(36\cdot80=2880\), and multiplying by \(q_L\le4/(1+\theta L)\) gives the absolute upper constant \(11520\). Both carry the stated factor \(e^{128/3}\).

This single strictly admissible witness works jointly in all three parameters. The sharp orders are consequently proved uniformly in \(d\ge2\), rather than separately for three incompatible limiting examples.

### 8. Odd scalar nonaffinity, equivalents, and degenerate references — lines 724–812

**Pass.**

The squared cubic coefficient survives affine projection and gives the lower bound in (V.O.23). The earlier residual estimate gives its upper bound; \(q/4\le q_+\le q\) gives both relative constants. Substituting the two uniform bounds for \(q_{\ell-1}\) proves the stated joint layer orders, including the first layer.

For fixed \(\theta>0\), (V.O.6) ensures \(q_\ell\to0\). Dominated convergence gives \((1-\mu(q))/q\to1\), while \(\mathbb E u(\sqrt q\,\xi)^2=O(q^3)\). Hence the reciprocal-variance increments tend to \(2\theta\). Their arithmetic averages yield \(q_\ell\sim(2\theta\ell)^{-1}\); no summable remainder is required.

The integrated rational identity gives a global remainder bound \(|z|^5/5\), so the Gaussian \(L^2\) remainder really is \(O(q^{5/2})\). Orthogonal projection is a contraction. Removing its affine component replaces \(\xi^3\) by \(\mathsf H_3=\xi^3-3\xi\); the remaining leading squared norm is \(6q^3/9=2q^3/3\). Absorbing the mixture's linear term gives the exact factor \(\theta^2\).

Substituting \(q_{\ell-1}\sim(2\theta\ell)^{-1}\) gives exactly

\[
 \mathcal R_{\phi_\theta}(q_{\ell-1})\sim\frac1{12\theta\ell^3},
 \qquad
 \frac{\mathcal R_{\phi_\theta}(q_{\ell-1})}{q_\ell}
 \sim\frac1{6\ell^2}.
\]

The text correctly restricts these equivalents to fixed \(\theta\). The regime table instead follows from uniform two-sided comparison bounds: when \(\theta L\ge1\), the absolute order is \(\delta^2/L\) and the normalized order is \(\delta^2\theta\); when \(\theta L\le1\), both are \(\delta^2\theta^2L\).

The normalized floor is uniform in depth at fixed positive \(\theta,\delta\), because \(L/(1+8\theta L)\ge1/(1+8\theta)\). The absolute floor must vanish since \(\lambda_{\min}(Q_L)\le q_L\to0\). There is no inconsistency with vanishing scalar nonaffinity.

Antipodal samples do have exactly opposite features under every odd layer, forcing a singular Gram. At \(\theta=0\), the population recursion preserves \(G\). The equilateral planar triple is strictly admissible for \(0<\delta<1/2\) and satisfies \(G\mathbf1=0\). A bias-free linear network respects the same linear relation among outputs, so it cannot realize all-one labels on that triple. This is a valid representational observation and is not used as a trained theorem.

### 9. Convex-offset variance, contraction, and nonaffinity — lines 814–945

**Pass.**

The conditions \(0<\varepsilon<1/2\), bounded nonconstant \(C^2\) shape, and all three norm bounds are explicit. The centered Gaussian preactivation mean is zero, so the feature mean is at least \(1-2\varepsilon=b_\varepsilon>0\). Minkowski gives
\(\sigma_{\ell+1}\le(1-\varepsilon)\sigma_\ell+1\).
The interval \([0,1/\varepsilon]\) is preserved and contains \(\sigma_1=1\); the mean lower bound supplies the positive lower endpoint. Thus (V.C.3) holds, also covering the first preactivation used in later residual bounds.

The derivative lies in the positive interval \([b_\varepsilon,1]\). At any positive variance, equality of its squared Gaussian average with one would force it to equal one everywhere by continuity and full support. This would imply \(\psi'=1\) everywhere, contradicting boundedness. Dominated convergence makes the average continuous over the compact variance interval, so its attained maximum satisfies \(b_\varepsilon\le\kappa<1\). Strictness is therefore uniform over all layers and input Grams for the fixed shape and mixture.

The input to each pairwise contraction has equal variance, even when the previous feature law has an offset. Its squared difference is exactly \(2(q_{\ell-1}-Q_{\ell-1,ab})\), which equals the previous feature squared difference. Applying (V.F.11) and iterating gives \(D_{L,ab}\le2(1-G_{ab})\kappa^{2L}\), valid for negative and singular correlations too.

The unit contrast vector gives \(\lambda_{\min}(Q_L)\le D_{L,ab}/2\); dividing by \(q_L\ge b_\varepsilon^2\) gives the normalized bound. Testing with \(\mathbf1/\sqrt3\) and using the common positive feature means gives \(\lambda_{\max}(Q_L)\ge3b_\varepsilon^2\). This verifies the additional factor three in the reciprocal condition-number bound. All four inequalities of (V.C.2) hold for every pair, including a duplicated pair with \(G_{ab}=1\).

The identity \(C_{L,ab}=1-D_{L,ab}/(2q_L)\) proves entrywise convergence to \(\mathbf1\mathbf1^T\). This is a statement about normalized uncentered geometry. It neither asserts convergence of \(q_L\) to a specified value nor requires scalar residuals to vanish.

At every positive variance, a zero residual for \(\psi\) would make it an affine function everywhere by continuity and full support. A bounded affine function is constant, excluded by assumption. The residual is continuous in \(\sigma>0\) by the displayed projection formula and dominated convergence. Its minimum over the compact interval is therefore strictly positive. Exact removal of the activation's affine term gives the factor \(\varepsilon^2\); the upper bound \(q_\ell\le\varepsilon^{-2}\) then gives the relative factor \(\varepsilon^4\).

The text correctly does not make these lower bounds uniform over all allowed shapes or as \(\varepsilon\downarrow0\). Scaling a nonconstant allowed shape by a small positive factor preserves admissibility and scales its squared residual by that factor squared.

### 10. Explicit convex-offset example — lines 947–962

**Pass.**

For \(\psi(z)=\arctan(z)/4\), the three stated suprema are \(\pi/8\), \(1/4\), and \(3\sqrt3/32\). In particular
\(|\psi''(x)|=|x|/[2(1+x^2)^2]\) is maximized at \(|x|=1/\sqrt3\). With \(\varepsilon=1/4\), the activation is exactly \((3/4)(1+z)+(1/16)\arctan z\), and its derivative lies between \(3/4\) and \(13/16\). The pointwise Lipschitz constant therefore supplies the claimed contraction with \(\kappa=13/16\).

### 11. Calibrated cancellation and finite-depth geometry — lines 964–1081

**Pass, with F1's explicit off-diagonal qualifier.**

The activation depends on the total depth \(L\), and the same activation is used at each layer of that network. It is correctly distinguished from both literal fixed families.

The fixed trigonometric shape is nonzero because \(w'(0)=e^{3/2}-1>0\); Gaussian full support gives \(v_*>0\). Bounded trigonometric derivatives give all required smoothness and moments.

Differentiating the already established Gaussian characteristic function gives \(\mathbb E[\xi\sin(t\xi)]=te^{-t^2/2}\). With \(c_*=e^{3/2}/2\), the linear Gaussian coefficient vanishes exactly:
\(2c_*e^{-2}=e^{-1/2}\). Oddness gives zero mean and normalization gives unit second moment. These prove \(q_k=1\) at every population layer. Gaussian conditional expectation kills both cross terms in (V.D.4), including at \(\rho=\pm1\).

The sine-product formula gives

\[
 v_*=e^{-1}\bigl(\sinh1-\sinh2+\tfrac14\sinh4\bigr),
\]

which verifies \(N_*=ev_*>0\). The odd coefficient numerator
\(1-2^j+4^j/4=(2^{j-1}-1)^2\) vanishes at degree one and is positive at every odd degree at least three. Thus \(p_3=3/(2N_*)\), the coefficient mass is one, and \(0\le K(\rho)\le\rho^3\) on \([0,1]\). Oddness gives the absolute-correlation contraction on the full interval.

The entrywise map \(K[C]\) is a positive combination of tensor Grams. Its cubic term gives \(K[C]\succeq\mu_\delta I_3\) with exactly \(\mu_\delta=p_3\delta^2(2-\delta)^2/3\). For \(b=(1+\tau/L)^{-1}\), induction in the exact affine matrix recursion yields
\(Q_k\succeq b^kG+(1-b^k)\mu_\delta I_3\).
Dropping \(b^kG\succeq0\) is valid even for singular input Grams. The binomial inequality gives
\(1-(1+\tau/L)^{-L}\ge\tau/(1+\tau)\), proving (V.D.9) for every finite \(L\ge1\), \(\tau>0\), and realizable separated triple. No tuning of the fixed shape to the separation is required.

### 12. Sequential depth limit, error, and planar witness — lines 1083–1185

**Pass.**

The population step in (V.D.10) is \(a_L/(1+a_L)\), whereas the interpolation mesh is \(a_L=\tau/L\). The proof explicitly accounts for this difference instead of silently equating the two clocks.

The supplied clipped extension has the same global Lipschitz constant \(D\) and bound \(B=2\). On a short interval, the integral-map iterates converge by the given geometric Cauchy estimate in the complete continuous-path space. Repeating provides global existence and uniqueness. Since the endpoint values of the vector field vanish, uniqueness prevents escape from \([-1,1]\). The discrete iteration remains in the interval as a convex combination.

The exact integral step has defect at most \(DBa_L^2/2\), and replacing \(a_L\) by \(a_L/(1+a_L)\) adds at most \(Ba_L^2\). Therefore the displayed error recurrence and the bound

\[
 \max_{k\le L}e_k\le
 B(1+D/2)\frac{\tau^2e^{D\tau}}{L}
\]

are correct. Interpolation adds at most \(B\tau/L\), so the convergence is uniform in depth coordinate and initial correlation. These constants require fixed \(\tau\), as stated.

Applying the scalar flow entrywise preserves positive semidefiniteness because it is obtained as the limit of linearly interpolated positive semidefinite matrices. This supplies the matrix compatibility that independent scalar ODE existence alone would not establish.

At each fixed \(L\), the fixed activation \(\phi_L\) meets V.F's assumptions and gives the inner limit in probability. The outer deterministic limit has top value \(Q(\tau)\). Passing the finite-depth floor to the limit gives \(\mu_\delta(1-e^{-\tau})\); continuity of the smallest eigenvalue in finite dimension follows directly from its Rayleigh-quotient characterization. The same inner limit for the total raw kernel is already established by (V.F.6).

For the equilateral triple, symmetry and oddness keep the off-diagonals equal to \(-r(s)\). The scalar solution stays nonnegative: zero is an equilibrium and uniqueness prevents crossing it, just as for the earlier endpoint argument. Then \(0\le K(r)\le r^3\) gives
\(-r\le r'\le r^3-r\), and \(r(s)\le1/2\).
Integrating the lower inequality gives \(r(s)\ge e^{-s}/2>0\). For \(u=r^{-2}\), the upper inequality gives
\(u'\ge2(u-1)\), hence \(u(s)\ge1+3e^{2s}\).
The eigenvalues are \(1-2r(s)\) and \(1+r(s)\) twice, proving exactly (V.D.14), with strict positivity for every \(s>0\).

This witness proves that the resulting geometry is not a scalar multiple of the singular input Gram. It does not assert trained feature motion. No width/depth interchange or simultaneous limit is needed.

### 13. Calibrated nonaffinity and local scalar checks — lines 1187–1265

**Pass.**

Writing the difference from the identity as a linear coefficient plus a bounded shape gives all three estimates in (V.D.15), using
\(0\le1-(1+\gamma^2)^{-1/2}\le\gamma^2/2\).
The weighted global bound and local uniform convergence are correct. For finite \(L\) and \(\tau>0\), the nonzero linear coefficient at infinity makes the unweighted difference supremum infinite; the text explicitly acknowledges this.

The shape is orthogonal to the constant and linear Gaussian coordinates, so its entire variance survives affine projection. This gives the exact residual \(\gamma_L^2/(1+\gamma_L^2)=\tau/(L+\tau)\). The denominator of relative nonaffinity is one, making the absolute and relative values identical at all initialized population layers.

For scalar variance perturbations, Gaussian integration by parts supplies the cross term \(q\,a(q)\) in (V.D.17). The explicit formula for \(a\) gives
\(a(1)=0\) and \(a'(1)=-3e^{-1/2}/(2\sqrt{v_*})\).
Differentiating \(b\) near one is justified by a bound proportional to \(|\xi|\), with \(q\) bounded away from zero. Thus

\[
 V_\gamma'(1)=
 \frac{1+2\gamma a'(1)+\gamma^2b'(1)}{1+\gamma^2}
 =1-\frac{3e^{-1/2}}{\sqrt{v_*}}\gamma+O(\gamma^2).
\]

For sufficiently small positive \(\gamma\), its absolute value is less than one. Continuity of the derivative gives an interval around the fixed point on which the mean-value theorem proves invariance and contraction. At fixed \(\tau\), this applies for all sufficiently large \(L\). Neither a uniform attraction neighborhood as \(L\) changes nor control of accumulated finite-width errors is asserted.

Finally \(\mathbb E\chi'(\xi)=0\) kills the derivative cross term. The denominator \(1+\gamma_L^2\) in (V.D.19) is present, and discarding it gives the valid upper bound
\((1+\tau M_2/L)^L\le e^{\tau M_2}\).
This is only a product of scalar derivative moments. The text correctly does not identify it with a network Jacobian norm or a trained backward-field estimate.

### 14. Final comparisons and scope — lines 1267–1329

**Pass after F1 and F3.**

The table preserves the distinct parameter conventions: fixed positive \(\theta\) for the odd mixture, fixed \(\varepsilon,\psi\) for the offset family, and depth-varying \(\phi_L\) with fixed \(\tau,\chi\) for the calibrated family. Its entries reproduce the verified formulas. The calibrated and sharp odd bounds retain their different separation ranges.

The distinction between a depth-uniform numerical floor and a theorem at each separately fixed depth is logically correct. Failure of a uniform initialized absolute floor does not rule out fixed-depth trained results, and initialized positive definiteness does not prove them.

Under F3's local gain assumptions, division by \(a+e\) has the claimed algebraic mixture form. For a general positive activation multiplier \(\alpha\), the first Gram scales by \(\alpha^2\). At the second layer, the centered Gaussian input scales by \(\alpha\), producing exactly

\[
 \widetilde Q_2=\alpha^2\mathbb E[\phi(\alpha Z)\phi(\alpha Z)^T],
 \qquad Z\sim N(0,Q_1).
\]

Thus there is no general homogeneous-rescaling rule for these nonlinear activations. The statement is properly understood as absence of a general reduction, rather than exclusion of trivial special cases such as \(\alpha=1\).

The subsequent gain-growth paragraph is self-contained under its explicitly stated assumptions \(a-e>1\), \(0<e\le1\), and the V.C shape bounds. Removing the affine component gives
\(\mathcal R_{a(1+\cdot)+e\psi}(q)=e^2\mathcal R_\psi(q)\le e^2\).
The squared linear Gaussian projection gives a second moment at least
\(q(a+e\mathbb E\psi')^2\ge q(a-e)^2\), where \(a-e>1\) ensures the coefficient is positive before squaring. Iteration yields \(q_\ell\ge(a-e)^{2\ell}\), so the relative layer residual is at most \(e^2/(a-e)^{2\ell}\). No positive absolute margin for this gain family is assumed or proved by that upper-bound argument.

The closing scope paragraph is accurate: V.F is fixed-depth, V.D takes width first, the auxiliary depth coordinate is not physical time, and no statement proves a limit for \(L=L(n)\), an interchange of limits, a trained Gaussian recursion, a population training flow, continuation, optimizer convergence, persistent trained nonaffinity, or fitting.

## Dependency and quantifier audit

The essential non-elementary-looking ingredients are proved in the supplied text: Hermite completeness, the covariance expansion and differentiated endpoint formulas, the Gaussian contraction, the cubic tensor bound, the needed Gaussian operator-norm probability bound, and the scalar ODE existence/error argument.

The remaining dependencies are elementary finite-dimensional linear algebra, Gaussian integration by parts and moments, Cauchy–Schwarz, Jensen, Markov/Chebyshev, dominated and monotone convergence, elementary \(L^1/L^2\) approximation, compactness, and elementary single-variable calculus. No theorem from another project part is needed after making the local assumptions in F3 explicit.

The following delicate quantifiers were checked:

- Width limits fix the data, \(d\), activation, and finite \(L\) before \(n\to\infty\).
- The calibrated outer limit fixes \(\tau\) and the shape, then varies the entire activation with \(L\); it does not vary the activation by layer within a given network.
- Odd sharp comparison constants are uniform jointly in \(0<\theta\le1\), \(0<\delta\le1/4\), \(L\ge1\), and \(d\ge2\).
- Odd large-depth equivalents fix \(\theta>0\); they are not asserted uniformly along \(\theta=\theta_L\).
- The lower tensor-based estimates allow singular Grams and closed off-diagonal separation, including \(\delta=1\) when realizable.
- The odd upper witness satisfies the strict inequalities, including the endpoint \(\delta=1/4\).
- The convex contraction constant and scalar residual floors fix \(\varepsilon,\psi\) and are uniform in depth and input Gram, not over the entire shape class.
- The calibrated local variance stability is for sufficiently large \(L\) at fixed \(\tau\), with no finite-width robustness conclusion.
- Negative and singular Gaussian correlations are covered, and scalar nonaffinity is consistently normalized by uncentered second moment.

**Final disposition:** correct F1–F3 locally. With those precision corrections, all mathematical conclusions of Part V reviewed here pass; no change to the substantive proof or its constants is indicated.
