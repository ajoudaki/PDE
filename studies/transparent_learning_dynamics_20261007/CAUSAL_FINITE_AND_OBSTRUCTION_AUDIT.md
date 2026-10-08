# Scoped audit: finite response memory and the fixed-time Gram obstruction

Date: 2026-10-07. Reviewer: causal-Gaussian route agent. This report audits two distinct frozen candidates; their verdicts are separate. No source file was edited.

## Inputs, coverage and method

I read every line of both assigned files:

| Input | Complete read coverage | SHA-256 |
|---|---|---|
| FINITE_RESPONSE_MEMORY.md | Lines 1–315 | bc4037f3e95d5a0587b01ec5d8e4ccbcfe990d4391c820e318f1dec45789fc09 |
| TYPICAL_GRAM_FIXED_TIME.md | Lines 1–398 | 5c79d98cef458782103f674b73a447e76c62e38959e60a4a32c9dae51a4dc4be |

The only additional scientific context available to me was my own causal-Gaussian route and its rank-robust finite-program continuation, as explicitly allowed. I did not read any integrated source, earlier obstruction note, other route, book, code, other study, literature, or another reviewer's findings. The required mathematical, research and notation instructions were already read and applied.

Checks were analytic reconstruction of the displayed identities, conditioning argument, resource counts, cubic derivative, conditional-pair construction, stability estimate, fourth-derivative construction, block variance bound and fixed-time probability constants. Shell calls only read the assigned sources, counted lines and computed hashes. No experiment or numerical test was run.

This is a scoped research check, not a promotion review. In particular, the finite-memory note uses a conditioning result I helped derive, so this report is not an independent author-free review of that dependency. I was not an author of the fixed-time obstruction and received only its complete frozen candidate.

## 1. Finite response memory

**Verdict: the finite-step equality in joint law, posterior formulas, force-memory identities and storage counts pass.** The interpretation needs one qualification about eventual full-rank query histories. The integrated numerical and replay certificate remains outside this audit and cannot inherit this verdict.

### Exact finite-step algebra

The mobility factors in equations (1)–(3) are consistent with the assigned physical flow. For example,

\[
\left[\frac{2h}{mn}
\sum_{s<k,b\leq m}c_b^s\delta_{\ell,b}^s
(h_{\ell-1,b}^s)^\top\right]h_{\ell-1,a}^k
=\frac{2h}{m}\sum_{s<k,b\leq m}
c_b^s C_{\ell-1;ba}^{s,k}\delta_{\ell,b}^s.
\]

Transposing the same rank-one history gives its backward term with $D_{\ell;ba}^{s,k}h_{\ell-1,b}^s$. The first-layer update uses the fixed input inner product $S_{ba}$ with no extra factor of $n$. The readout update and its current-feature contraction give the last two equations of (3). The source and evaluated sample indices are correctly asymmetric. Only training samples write to the histories.

### Adaptive posterior and its causal use

For retained constraints $GH=F$ and $G^\top D=B$, the homogeneous Gaussian remainder is exactly the doubly projected space

\[
\{(I-P_D)M(I-P_H):M\in\mathbb R^{n\times n}\}.
\]

The mean in equation (5) satisfies both constraints, using $D^\top F=B^\top H$, and is orthogonal to this space. Applying that posterior to $u$ gives

\[
Gu=Fa+D\langle D,D\rangle_n^\dagger
\langle B,u_\perp\rangle_n
+\frac{\|u_\perp\|}{\sqrt n}(I-P_D)\xi.
\]

Thus the normalization of the cross-direction mean and of the noise in (4) is correct. Moore–Penrose inverses handle empty or dependent history columns; the zero-innovation case causes no division. A full opposite-direction span correctly removes all fresh noise through its projection.

The chronological forward/backward ordering makes every query predictable from already observed fields. Conditioning on earlier scalar reductions adds no information beyond that transcript because they are its deterministic functions. Reuse of a matrix in either direction is therefore permitted. Other initialized matrices retain independent conditional remainders. The induction establishes the complete finite Euler transcript law, not merely individual marginal Gaussian laws.

Initializing the first-layer panel with independent Gaussian rows of covariance $S$ is exactly equivalent to its construction from $A^0$. The coupling formulation is valid as an existence statement. It does not say that arbitrary independently chosen short seeds reproduce a particular supplied dense initialization pathwise; the note does not claim that stronger statement.

### Counts and interpretation

For positive finite $N$, each interface has at most order $pN$ forward and backward calls. Its forward, backward and mixed contractions therefore have at most order $p^2N^2$ entries. Summing across the fixed depth gives the stated $O(LpN)$ call fields and $O(Lp^2N^2)$ scalar-pairing and coefficient storage. If the initial and final evaluations are both counted, replacing $N$ by $N+1$ makes the convention explicit without changing these orders for $N\geq1$.

The first-layer covariance has rank at most $\min(d,p)$. One can generate it using that many independent Gaussian roots per neuron. At most one additional $n$-component Gaussian innovation is needed per call. This proves the random-record bound

\[
O\!\left(n[\min(d,p)+LpN]\right).
\]

The account explicitly distinguishes this width-dependent real record from a short finite-bit seed, and it charges a restartable random oracle as information. There is no implicit exact short-seed assumption in the finite-step theorem.

One interpretation sentence at lines 227–230 is too absolute: “It is not an invertible renaming of all the dense weights.” If the retained forward inputs span $\mathbb R^n$, then their responses determine $G=FH^+$, and the response memory does encode the entire initial matrix. More generally, the unobserved subspace can shrink to zero. The correct qualification is:

> The algorithm stores only the response information revealed by its queries. When those queries leave a nonzero Gaussian remainder, it does not encode that unobserved matrix component; after sufficiently many spanning queries, the histories may determine the whole matrix.

This does not affect the theorem or the stated storage count. It prevents a fixed-finite-query reduction from being described as a uniform information reduction for arbitrarily long query histories.

### Offline table selection is disclosed, not causally free

Equation (6) is correct. Choosing a column basis and an invertible row restriction produces $C$ with $V=CV_I$ and $C_I=I$. Multiplication gives $V^\top V/n=V_I^\top(C^\top C/n)V_I$. The zero-rank case has the corresponding empty-matrix interpretation. The storage bound $qR+q^2=O(R^2)$ follows.

That identity preserves only the completed table's pairings. It neither proves a causal initial-data selection rule nor supplies finite-precision prefix replay by itself. The source explicitly discloses:

* dependence of the selected rows and metric on the completed future table;
* lack of counterfactual-label or new-field guarantees;
* the need to keep the future-dependent metric out of the Gaussian conditioning transcript;
* the distinction between proving the original posterior law and subsequently replaying the realized table.

Those qualifications are mathematically essential and are correctly stated. Omitting future scalar answers does not remove future information already present in the selected metric. The note does not conceal that information or claim that this table identity alone solves the autonomous-closure problem.

The assertions about the integrated document's noisy posterior, Sylvester solve, finite rounding and prefix replay are source-specific claims whose dependency was not among my allowed inputs. I neither verified nor contradicted them. Likewise, the all-time transfer in Section 6 is valid only under its explicitly stated numerical/coupling premise and exact replay premise; this audit verifies neither premise. The existing caveats at lines 287–301 prevent an unconditional all-time conclusion.

### Notation correction

Only $a\leq m$ has a label. In the forward-pass display, write $c_a=y_a-f_a$ explicitly for $a\leq m$. The later formulas already use residuals only for those indices, so this is a definition-scope correction, not a mathematical change.

## 2. Fixed-time Gram-information obstruction

**Verdict: PASS for the stated one-layer sine model and initialization-information class.** I found no proof-breaking gap. The fixed positive time and all measurable Gram-estimator quantifiers are supported by the argument. There is one harmless TeX correction listed below.

### Cubic identity

Let $U=\sin X$, $V=\sin Y$, and $S=\eta(U+V)$ for a neuron. At zero readout,

\[
\dot h_a(0)=0,\quad \dot w(0)=S,\quad
\ddot h_a(0)=\eta S\cos^2z_a(0).
\]

The initial output derivatives are therefore

\[
\dot f(0)=\eta G\mathbf1,\qquad
\ddot f(0)=-\eta G^2\mathbf1.
\]

In the third derivative, the non-Gram part comes from
$\eta\sum_b\ddot h_b\,U+3S\ddot h_1$. Dividing by $\eta^3$ gives

\[
U(U+V)(2-U^2-V^2)+3(U+V)^2(1-U^2),
\]

which expands exactly to

\[
5U^2+3V^2+8UV-4U^4-7U^3V-UV^3-4U^2V^2.
\]

The remaining term is $\eta(G^3\mathbf1)_1$. Thus the stated cubic polynomial and label factors are correct.

### Equal-Gram conditional pair and positive conditional variance

The eight trigonometric summaries are exactly equivalent to the full Gram information, using the double-angle and sum/difference identities. For example,

\[
\cos(x\pm y)=\cos x\cos y\mp\sin x\sin y,
\]

and the corresponding two sine identities recover the mixed feature/derivative entries. Constants in the diagonal identities are known.

The coefficient of $\cos4x$ in $J$ is $-1/2$, coming from $-4\sin^4x$. None of the other terms cancels that frequency, and it is absent from the eight Gram functions. Those eight sine/cosine functions and the constant are linearly independent Fourier modes. Hence $1,t_1,\ldots,t_8,J$ are independent.

If all derivatives of $(t,J)$ lay in a proper subspace of $\mathbb R^9$, an orthogonal nonzero coefficient vector would produce a function with both first derivatives identically zero, hence a constant on $\mathbb R^2$. This contradicts that independence. One may therefore choose nine independent derivative vectors and place their points in the nine different neurons of one block, obtaining rank nine for the block map to $(T_j,B_j)$.

The density step is valid even though the domain has dimension eighteen: retain nine domain coordinates complementary to the nine selected derivative columns and append them to the map $(T_j,B_j)$. Its eighteen-dimensional Jacobian is invertible locally. Change of variables and positive Gaussian density give a nonzero absolutely continuous component for $(T_j,B_j)$. If $\mathbb E\operatorname{Var}(B_j\mid T_j)=0$, then $B_j$ is almost surely a measurable function of $T_j$; that graph has nine-dimensional Lebesgue measure zero. The two facts contradict each other. Thus $\kappa>0$.

Conditional independent resampling within each block preserves the full original Gaussian block marginal in each network, not merely its summary. Independent paired blocks then preserve iid Gaussian neurons in each marginal network. Shared leftovers preserve exact total-Gram equality. Conditional centering gives variance $2\kappa$ for a block difference. The classical iid central limit theorem applies because these differences are bounded, independent and identically distributed. With $\lfloor n/b\rfloor$ blocks, its variance normalization is precisely $2\kappa/b$ after division by $\sqrt n$.

### Bounded phase coordinates and average-distance stability

The sine/cosine equations preserve each circle constraint. Differentiating the output yields the stated positive semidefinite feature Gram plus diagonal term. Thus loss decreases, $\|c\|_2\leq\sqrt2\eta$, and $|\dot w_i|\leq2\eta$. At $T_0=1/[2(\eta+1)]$, this gives $|w_i|\leq\eta/(\eta+1)<1$. Every marginal trajectory used in block replacement stays in the same box.

The bound $|f_a-\widetilde f_a|\leq2d_n$ follows by subtracting $wu_a$. Within the box, subtracting the three-factor activation velocities gives

\[
2d_n+3(\eta+1)\Delta_i,
\]

and subtracting the two readout terms gives

\[
4d_n+2(\eta+1)\Delta_i.
\]

Their maximum is at most $4d_n+3(\eta+1)\Delta_i$. Averaging produces the stated constant $L=7+3\eta$. The Grönwall argument therefore has no width-dependent constant and applies to arbitrary feasible block replacements.

### Fourth derivative and paired-block variance

The moment derivations $\mathcal A_a$ reproduce the exact coordinate flow, including the feedback through $c_a=\eta-\langle wu_a\rangle_n$. Four applications of the product rule starting from $\langle wu_1\rangle_n$ produce a finite polynomial in finitely many empirical moments. Its list and coefficients do not depend on $n$. Every constituent moment is Lipschitz in $d_n$ on the fixed box; the outer polynomial has bounded derivatives on the bounded range of those moments. This proves the required width-independent $L_4$, boundedness and continuity of $f_1^{(4)}$. No unproved truncation of the moment hierarchy is involved: only four derivatives are being constructed.

Replacing one independent paired block changes each marginal initial average distance by at most $2b/n$. The resulting change in the difference of fourth derivatives is therefore at most $4bL_4e^{LT_0}/n$. There are at most $2n/b$ independent blocks when $n\geq b$. The martingale bounded-difference proof gives

\[
\operatorname{Var}(D_n^{(4)}(s))
\leq\frac{32bL_4^2e^{2LT_0}}n.
\]

The global exchange of the two marginal networks leaves the paired law invariant and negates this observable. Its mean is consequently zero, so the variance bound is also the needed squared $L^2$ bound. This centering step is essential and is present.

### Fixed-time remainder and estimator quantifiers

Taylor's formula and Minkowski's inequality give

\[
\|\mathcal R_n(t)\|_{L^2}
\leq\frac{C_4t^4}{24\sqrt n}.
\]

At the chosen positive deterministic $t_*$, Chebyshev bounds the event
$|\mathcal R_n|>\eta^3\sigma t_*^3/(12\sqrt n)$ by

\[
\frac{C_4^2t_*^2}{4\eta^6\sigma^2}
\leq\frac{p_0C_4^2}{16(1+C_4)^2}
\leq\frac{p_0}{16}.
\]

Combining it with the cubic central-limit event leaves pair separation at least
$\eta^3\sigma t_*^3/(12\sqrt n)$ with lower-limit probability at least
$15p_0/16$. The identical Gram means both networks receive the same value from every measurable $F_n$. At least one prediction error must exceed half the separation. Equal marginal laws and the union bound give lower-limit probability at least $15p_0/32$ for a single network's error. The claimed $p=p_0/4$ is conservative. Sharing an independent predictor seed preserves the same argument for independently randomized estimators.

The selected time is positive for every fixed $\eta>0$ and $T>0$ and is independent of width and estimator. No uniformity as $\eta$ tends to zero is claimed or needed. A single fixed-time lower bound suffices for the stated supremum-in-time obstruction.

### Scope and notation

The result excludes $o_p(n^{-1/2})$ prediction from this specified initialization Gram, at the realized dense fluctuation scale. It does not exclude population predictions, errors of order $n^{-1/2}$, extra initialization observables, or more general finite aggregate states. The source keeps those distinctions explicit.

At line 338, change the TeX token $min$ to $\min$. This has no mathematical effect. The dependence of $a_\eta$ on $T$ is expressly disclosed, so its shortened subscript is not an omitted uniformity claim.

## Final disposition

Retain both mathematical results with their stated scopes. Qualify the finite-memory sentence about never encoding all dense weights, and make the two small notation corrections. Do not attach an all-time, compressed-storage, finite-word or short-seed certificate to the finite-step theorem on the basis of this audit; those dependencies were not inspected and the note itself treats them conditionally.
