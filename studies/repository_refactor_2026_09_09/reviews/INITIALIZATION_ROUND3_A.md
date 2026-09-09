# Isolated adversarial review of Part V

## Verdict

**CORRECTION REQUIRED: one minor literal-hypothesis error in the final gain comparison.**

The sentence at PROOF.md line 1298 asserting that division by \(a+e\) changes the recursion needs an exception for \(a+e=1\), which the stated hypotheses permit. The accompanying scaling formulas are correct. This finding does not invalidate Theorem V.O.1, Theorem V.C.1, the calibrated finite-depth bounds, or the sequential limit.

I found no other mathematical gap, incorrect constant, endpoint failure, or unsupported nontrivial dependency in Part V. The verification below covers the complete supplied part, including its auxiliary proofs and scope statements. “Pass” means the written argument and its elementary implications were checked; it does not assert any result about training or simultaneous width/depth limits.

## Isolation, input identity, and complete read coverage

Only the following two source files were read:

| Input | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| /tmp/pde-initialization-round3.zWfKUzam/PROOF.md | 1337 | 48406 | 6d05666ef6101778febf2e95a73906672eb67dfdfd0a60e58693e6fc3749db45 |
| /tmp/pde-initialization-round3.zWfKUzam/NOTATION.md | 98 | 5110 | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |

Both were read fully to EOF, without truncated tool output. PROOF.md was read in the consecutive, exhaustive ranges 1–300, 301–600, 601–900, 901–1130, and 1131–1337. NOTATION.md was read in full, lines 1–98. Line references in this report refer to those exact inputs.

The hashes were checked at intake and again after the mathematical audit; both checks agreed. Neither input was edited.

No other project, study, history, prior-review, or skill source was read. No network, agent, numerical experiment, symbolic-computation program, or research computation was used. Tool operations were limited to displaying the two inputs, obtaining their line/byte counts and hashes, creating/checking the private output directory, and writing this report.

The output directory /tmp/pde-part-v-adversarial-review.w2m6SPqM was freshly created using an exclusive temporary-directory operation and its permissions were verified as 0700. The report was written using apply_patch.

## Required correction R1: identity normalization is allowed

**Location:** PROOF.md lines 1294–1305, particularly line 1298.

**Severity:** Minor wording/hypothesis error; not a theorem-level failure.

The paragraph assumes only \(a>e>0\) and an allowed shape \(\psi\), defines
\[
g(z)=a(1+z)+e\psi(z),\qquad \varepsilon=\frac{e}{a+e},
\]
and says:

> This division changes the recursion under the fixed matrix initialization.

As a statement under the displayed hypotheses, this has an exception. Take
\[
a=\frac34,\qquad e=\frac14,\qquad
\psi(z)=\frac14\arctan z.
\]
This is exactly an allowed nonconstant shape: its three required norms are \(\pi/8\), \(1/4\), and \(3\sqrt3/32\), all below one, as also checked in V.C. The strict inequality \(a>e>0\) holds, but \(a+e=1\). Therefore
\[
\frac{g}{a+e}=g.
\]
The activation, finite initialized features, and population recursion are unchanged at every depth. The later condition \(a-e>1\), introduced in a separate paragraph at line 1309, does not apply retroactively to this paragraph.

**Minimal required correction:** Replace the sentence by:

> If \(a+e\ne1\), this division changes the recursion under the fixed matrix initialization. In general, a scalar activation change cannot be accounted for by merely rescaling the final kernel.

When discussing the absence of a homogeneity identity in lines 1304–1305, explicitly restrict that assertion to nontrivial scalings \(\alpha\ne1\), or phrase it as a statement about general scaling rather than every \(\alpha>0\). The exact formulas at lines 1301–1303 may retain \(\alpha>0\), because they are valid also at \(\alpha=1\).

The proposed exception is sufficient. Indeed, \(\mathbb E g(\xi)\ge a-e>0\), so \(Q_1\) is nonzero. Dividing the activation by \(a+e\ne1\) changes \(Q_1\) to \((a+e)^{-2}Q_1\). The intended nontrivial-scaling distinction is consequently valid. No numerical constant or main theorem needs modification.

## 1. Model, metric, observables, and notation

**Coverage:** PROOF.md lines 1–142; NOTATION.md lines 1–98. **Result: pass.**

- The input normalization \(u_a=x_a/\sqrt d\) gives unit vectors and the stated input Gram. Realizability is explicit, and no invertibility is used. The later planar witnesses can be converted to the original inputs by \(x_a=\sqrt d\,u_a\).
- The stored first, hidden, and readout weights agree with the notation contract. In particular, the readout variance is \(n^{-2}\), not its standard deviation and not an order-one readout convention.
- Under \(W^{(1)}=\sqrt d\,V^{(1)}\), the first metric term becomes \(d\|dV^{(1)}\|_F^2/n\). This agrees with the claimed alternative storage and the unchanged first preactivations.
- The inverse metric multipliers are \(n\), then \(1\) for each square hidden matrix, then \(n\) for the readout. The loss factor \(2/3\) is correctly excluded from the predictor-gradient kernel.
- \(Q_\ell\) is the uncentered feature second-moment matrix. It is nevertheless the covariance of the next centered Gaussian preactivation, because the next matrix has independent, centered entries. In the offset family it must not be interpreted as centered feature covariance.
- Equal marginal variances propagate through a common activation. Thus the scalar variance recursion is independent of off-diagonal input geometry.
- For positive \(q_\ell\), \(C_\ell\) is positive semidefinite with trace three, so \(1\le\lambda_{\max}(C_\ell)\le3\). Both inequalities in V.M.7 follow, with the stated factor three.
- The affine regression formula V.M.9 follows by projection onto the orthonormal pair \(1,\xi\). Since \(q>0\), allowing the coefficient of \(\sqrt q\,\xi\) gives the same linear subspace. The minimum is attained and the relative denominator is consistently uncentered.
- Positivity of the relevant variances and denominators is established separately for each of the three families below; it is not assumed for an arbitrary Lipschitz activation.
- The references to other parts introduce no proof dependency here. The training conventions in NOTATION.md are not used as a substitute for any initialization argument.

## 2. Fixed-depth finite-width identification and raw kernel

**Coverage:** lines 144–260, V.F.1–V.F.6. **Result: pass.**

At layer one, the row triples are independent centered Gaussian vectors with covariance \(G\), including when \(G\) is singular. A Lipschitz activation has linear growth, so activated products have finite second moments. The stated Chebyshev argument applies.

At subsequent layers, conditioning on the preceding features gives independent row triples with covariance \(\widehat Q_{\ell-1}\). On the bounded-diagonal event, Gaussian fourth moments uniformly bound the variances of all nine activated products. The conditional Chebyshev bound \(A_{M,\phi}/(nv^2)\) is correct. Since each previous diagonal converges to a finite deterministic value, a fixed \(M\) strictly above those values makes the complement probability vanish. This suffices without an unconditional high-moment induction.

The continuity argument at singular covariances is valid. Positive square roots of a convergent sequence of positive semidefinite \(3\times3\) matrices are bounded; every convergent subsequence limit is the unique positive square root of the limit matrix. Finite-dimensional compactness supplies the required subsequences. Coupling with a common standard Gaussian vector gives \(L^2\) convergence after applying a Lipschitz activation, and Cauchy–Schwarz gives convergence of product expectations. Finite induction and a finite union establish the claimed joint convergence over entries and layers.

Direct differentiation gives the three kernel contributions:
\[
n\left\langle\frac{\delta_a x_a^T}{n\sqrt d},
                 \frac{\delta_b x_b^T}{n\sqrt d}\right\rangle_F
=G_{ab}\frac{\delta_a^T\delta_b}{n},
\]
\[
\left\langle\frac{\delta_a h_a^T}{n},
                 \frac{\delta_b h_b^T}{n}\right\rangle_F
=\frac{\delta_a^T\delta_b}{n}\frac{h_a^Th_b}{n},
\qquad
n\left\langle\frac{h_a}{n},\frac{h_b}{n}\right\rangle
=\frac{h_a^Th_b}{n}.
\]
Thus V.F.3 has no missing factor of \(d\), \(n\), or \(2/3\). The backward fields are residual-free, as required.

The elementary operator-norm estimate also checks:

- Radius-\(1/8\) disjoint balls around a \(1/4\)-separated spherical family give cardinality at most \(9^n\).
- Approximating the two unit vectors in the bilinear supremum loses at most \(\|W\|_{\mathrm{op}}/2\), giving the factor two.
- Each fixed bilinear form has variance \(1/n\). The two-sided tail at threshold five is \(2e^{-25n/2}\).
- The union over at most \(9^{2n}\) pairs gives V.F.4, whose exponent is negative. A finite union over hidden layers is legitimate because \(L\) is fixed.

The readout satisfies
\[
\mathbb E\frac{\|W^{(L+1)}\|_2^2}{n}=n^{-2}.
\]
Markov's inequality and the bounded hidden-matrix norms yield the backward RMS estimate \(O_{\mathbb P}(n^{-1})\). Therefore the first and middle kernel blocks are \(O_{\mathbb P}(n^{-2})\), using tight feature RMS values for the middle blocks, and vanish. The readout block tends to \(Q_L\). The bound on \(f_{n,a}\) is also valid and implies zero initial limiting predictions.

The statements remain explicitly at separately fixed finite depth. No width rate uniform in \(L\), trained recursion, or nonzero population backward field is inferred.

## 3. Gaussian/Hermite foundations and all correlation endpoints

**Coverage:** lines 262–361, V.F.7–V.F.11. **Result: pass.**

The generating-function calculation proves orthonormality with the stated normalization \(\mathsf h_j=\mathsf H_j/\sqrt{j!}\). Its coefficient comparisons are justified by Gaussian exponential integrability.

The completeness argument is contained:

1. At \(t=i\eta\), the squared Hermite coefficient norms sum to \(e^{\eta^2}\), so the partial sums are Cauchy in Gaussian \(L^2\).
2. Their pointwise entire-function limit identifies the \(L^2\) limit, for example by taking an almost-surely convergent subsequence of the \(L^2\)-convergent sequence.
3. Orthogonality to all polynomials therefore makes the Fourier transform of \(u(x)e^{-x^2/2}/\sqrt{2\pi}\) vanish. This density is integrable by Cauchy–Schwarz.
4. The text derives the Gaussian characteristic function and its scaled Fourier integral. Fubini in the convolution is justified by the displayed integrable bound.
5. Gaussian convolution converges to the original density in \(L^1\), using translation continuity and an approximate-identity argument. The stated reduction to interval step functions uses only elementary density in \(L^1\).

Consequently Fourier uniqueness, Hermite completeness, and Parseval do not rely on an omitted nontrivial external theorem.

The joint generating function yields the mixed Hermite identity for every \(\rho\in[-1,1]\). At the singular endpoints one has \(Y=X\) or \(Y=-X\); no nonsingular density is required. Polynomial approximation extends the identity to Gaussian \(L^2\) functions by marginal Cauchy–Schwarz. The covariance series is absolutely convergent at both endpoints because \(\sum a_j^2<\infty\).

For the derivative identities, at-most-linear growth of \(f\) and bounded \(f',f''\) eliminate the Gaussian boundary terms. Applying integration by parts twice gives
\[
\langle f',\mathsf h_{j-1}\rangle=\sqrt j\,a_j,\qquad
\langle f'',\mathsf h_{j-2}\rangle=\sqrt{j(j-1)}\,a_j.
\]
Completeness then gives the exact two weighted coefficient sums. Their finiteness implies uniform convergence of the differentiated series on the closed correlation interval. The text correctly distinguishes the unsigned values at \(+1\) from the alternating values at \(-1\), and correctly calls these endpoint derivatives one-sided.

The contraction proof does not lose negative correlations:
\[
1-\rho^j=(1-\rho)\sum_{k=0}^{j-1}\rho^k\le j(1-\rho)
\]
holds for the entire interval, including \(\rho=-1\). Applying Parseval to \(f(x)=\phi(\sigma x)\) supplies the factor \(\sigma^2\) in the derivative sum. This produces exactly V.F.11. At \(\rho=1\) both sides vanish; at \(\rho=-1\) the same inequality remains valid.

All three activation families satisfy the stated regularity for each use of these identities.

## 4. Cubic tensor floor

**Coverage:** lines 363–400, V.F.12–V.F.13. **Result: pass.**

The separation assumption ensures \(1-C_{ab}^2\ge\delta(2-\delta)>0\), so every tensor factor is well-defined. Each \(v_{ab}\) has unit norm, is orthogonal to \(v_b\), and has inner product \(\sqrt{1-C_{ab}^2}\) with \(v_a\).

Therefore \(T_a\) is a unit tensor, annihilates the other two cubic sample tensors, and pairs with its own tensor by at least \(s_\delta\). These tensors need not be symmetric or mutually orthogonal. The estimate uses only three separate Cauchy–Schwarz inequalities:
\[
s_\delta^2\sum_a b_a^2
\le\sum_a|\langle T_a,T\rangle|^2
\le3\|T\|^2.
\]
This proves precisely the factor \(s_\delta^2/3\), including when \(C\) is singular. The endpoint \(\delta=1\) is allowed whenever the corresponding orthogonal triple is realizable.

Every nonnegative integer entrywise power is a tensor Gram. The degree-zero convention is correctly the all-ones matrix. Limits of the later nonnegative sums remain positive semidefinite by elementary finite-dimensional closure.

## 5. Literal odd mixture: variance and nonlinear weights

**Coverage:** lines 402–551, V.O.1–V.O.11. **Result: pass.**

The theorem's range is \(L\ge1\) integral, \(0<\theta\le1\), \(0<\delta\le1/4\), and every \(d\ge2\). The strict admissible set is nonempty by the later witness, including its boundary value \(\delta=1/4\). No compactness or attainment of the infimum is assumed.

For \(0<q\le1\), integration by parts gives the stated arctangent linear projection. Jensen gives \(c(q)\ge1/2\); the projection bound then gives \(q_+\ge q/4\). The sign and strict pointwise shrinkage of the odd mixture imply \(0<q_+<q\).

Writing \(u=z-\arctan z\), the pointwise bounds \(u^2\le zu\) and the exact decrement identity give
\[
\theta(2-\theta)q(1-\mu)\le D(q)\le2\theta q(1-\mu).
\]
The Cauchy–Schwarz bound uses \(\mathbb E\xi^2=1\) and \(\mathbb E\xi^4=3\), giving
\[
\mathbb E\frac{\xi^2}{1+q\xi^2}\ge\frac1{1+3q}.
\]
Thus \(\theta q^2/4\le D(q)\le2\theta q^2\). Dividing by \(qq_+\), with \(q/4\le q_+\le q\), produces exactly the inverse-variance increments \(\theta/4\) and \(8\theta\).

Iteration proves V.O.6. For V.O.7:

- The lower bound is the integral of \((1+8\theta x)^{-2}\) from zero to \(L\), compared with its left-endpoint sum.
- The bound \(L\) uses \(q_k\le1\).
- The bound \(4/\theta\) follows by summing \((\theta/4)q_k^2\le q_k-q_{k+1}\).
- The final factor five follows from \(\min(1,4/x)\le5/(1+x)\), split at \(x=4\).

Oddness removes all even Hermite degrees. The normalized weights are nonnegative and sum to one. Hence \(|K_q(\rho)|\le|\rho|\), so absolute separation is preserved, including for negative input correlations.

The linear coefficient is \(\sqrt q\,c(q)\), and the remaining squared norm is exactly the affine-regression residual. The test using the identity function and \(|z-\arctan z|\le|z|^3/3\) gives \(R(q)\le(5/3)\theta^2q^3\). Since \(c^2\ge1/4\), the logarithmic linear-weight loss is at most \((20/3)\theta^2q^2\). Summing over any finite set of layers gives at most \(80/3\). Thus every needed consecutive product is at least \(p_*=e^{-80/3}\).

## 6. Odd-mixture cubic injection and lower constants

**Coverage:** lines 553–611, V.O.12–V.O.15. **Result: pass.**

Two integrations by parts give
\[
b_3(q)=-\sqrt{\frac23}\,q^{3/2}
  \mathbb E\frac{\xi^2}{(1+q\xi^2)^2}.
\]
The density \(\xi^2\) relative to Gaussian probability has total mass one and gives mean three to \(\xi^2\). Jensen applied under that measure therefore bounds the displayed expectation below by \((1+3q)^{-2}\ge1/16\). Squaring the coefficient yields \(q^3/384\), and dividing by \(q_+\le q\) yields \(w_3(q)\ge\theta^2q^2/384\).

The one-step matrix inequality is legitimate: it first discards other positive semidefinite Hermite terms, then applies the cubic tensor floor to the actual preceding normalized Gram. It does not assume that an entrywise nonlinear map preserves arbitrary Loewner inequalities.

Iteration of the remaining scalar-weight inequality propagates each cubic injection through a product bounded below by \(p_*\). Empty products are one. This gives the factor \(1/(3\cdot384)=1/1152\) in V.O.14. Multiplication by the lower bound for \(q_L\) gives V.O.15.

The theorem constants check exactly:

| Bound | Constant calculation |
|---|---|
| Normalized lower bound | \(1152\cdot8=9216\) |
| Absolute lower bound | \(1152\cdot8^2=73728\) |

Here \(s_\delta\ge\delta\) and \(1+8\theta L\le8(1+\theta L)\). The stronger preceding estimates apply to nonstrict absolute separation for every realizable \(0<\delta\le1\). Thus the claimed positive definiteness at finite depth, including singular input Grams, is justified.

## 7. Odd-mixture curvature and strict planar witness

**Coverage:** lines 613–726, V.O.16–V.O.22. **Result: pass.**

Composition preserves odd degrees, nonnegative coefficients, and total coefficient mass one. Nonnegative rearrangements on \([0,1)\), followed by monotone convergence at one, justify the construction; absolute convergence and oddness give the negative half of the interval.

The endpoint derivative formulas correctly include \(q_k\) and \(q_k^2\), respectively. Since
\[
\phi_\theta''(z)=-\frac{2\theta z}{(1+z^2)^2},
\]
one has \(\mathbb E\phi_\theta''(\sqrt q\,\xi)^2\le4\theta^2q\), and therefore \(b_k\le16\theta^2q_k^2\). The odd-degree restriction gives \(d_k\ge1\) and \(d_k-1\le b_k/3\).

Consequently \(\sum b_k\le64\), \(\sum(d_k-1)\le64/3\), and \(A_k\le e^{64/3}\). The endpoint chain rule is valid because the maps have continuous one-sided first and second derivatives and preserve the interval. Dividing the recurrence for \(B_k\) by \(A_k\) verifies
\[
B_L=A_L\sum_{k=0}^{L-1}(b_k/d_k)A_k.
\]
This yields the exact sufficient curvature bound
\[
F_L''(1)\le80e^{128/3}\frac{\theta^2L}{1+\theta L}.
\]
The second moment of the composed degree distribution equals this endpoint derivative: differentiate inside \([0,1)\), then use monotone convergence and continuity at one.

For the planar witness, \(c=1-2\delta\in[1/2,1)\) and \(r=2c^2-1\). All four strict margins have been checked:
\[
(1-\delta)-c=\delta,\quad c-(-1+\delta)=2-3\delta,
\]
\[
(1-\delta)-r=\delta(7-8\delta),\quad
r-(-1+\delta)=(1-4\delta)(2-2\delta)+\delta.
\]
They are strictly positive throughout \(0<\delta\le1/4\), not merely away from the upper endpoint. At that endpoint \(c=1/2\) and \(r=-1/2\), which remain strictly admissible. Zero-padding realizes the same witness in every larger input dimension.

The vector \((1,-2c,1)\) annihilates the input Gram and has squared norm at least three. Its degree-\(j\) tensor Rayleigh numerator is the stated \(E_j(c)\), which is nonnegative by the tensor Gram construction. The degree-one term vanishes exactly.

Differentiating twice gives the printed expression. On \([1/2,1]\), the absolute-value bound is
\[
8+8j+32j(j-1)+8j(j+1)=40j^2-16j+8.
\]
Its comparison to \(54j(j-1)\) has difference \(14j^2-38j-8\), positive at \(j=3\) and increasing thereafter. Taylor's integral remainder therefore gives \(27j(j-1)(1-c)^2\). After division by the squared norm, the factor is \(9(1-c)^2=36\delta^2\).

The upper constants consequently check:

| Bound | Constant calculation |
|---|---|
| Normalized upper bound | \(36\cdot80=2880\), multiplied by \(e^{128/3}\) |
| Absolute upper bound | \(4\cdot2880=11520\), multiplied by \(e^{128/3}\) |

The last factor four uses \(q_L\le4/(1+\theta L)\). The same witness works simultaneously for \(\delta,\theta,L\), so the stated joint orders, rather than just separate one-parameter orders, are established.

## 8. Odd-mixture nonaffinity, asymptotics, and boundary cases

**Coverage:** lines 728–816, V.O.23–V.O.26 and the regime discussion. **Result: pass.**

The residual lower bound retains the cubic coefficient after affine projection; the upper bound is the identity-function test already established. Division by \(q_+\) in the correct direction gives both relative bounds in V.O.23. Combining them with the variance bounds gives the stated uniform orders at input variance \(q_{\ell-1}\), with the layer shift correctly retained.

For fixed \(0<\theta\le1\), the variance tends to zero. Dominated convergence gives \((1-\mu(q))/q\to1\), and the remainder term in the decrement is \(O(q^3)\). Hence \(D(q)/q^2\to2\theta\), \(q_+/q\to1\), and the inverse-variance increments tend to \(2\theta\). Averaging these increments proves \(q_\ell\sim(2\theta\ell)^{-1}\).

The globally valid arctangent remainder bound gives an \(O_{L^2}(q^{5/2})\) error. Projection is an \(L^2\) contraction and removes the \(3\xi\) part of \(\xi^3\), leaving \(-q^{3/2}\mathsf H_3/3\). Its squared norm is \(6q^3/9\). Thus
\[
\mathcal R_{\arctan}(q)\sim\frac23q^3,\qquad
\mathcal R_{\phi_\theta}(q)=\theta^2\mathcal R_{\arctan}(q).
\]
Substituting \(q_{\ell-1}\) and dividing by \(q_\ell\) gives exactly \(1/(12\theta\ell^3)\) and \(1/(6\ell^2)\).

The depth-uniform normalized sample floor is consistent with vanishing per-layer relative scalar nonaffinity: V.O.14 has \(L/(1+8\theta L)\ge1/(1+8\theta)\). Absolute conditioning cannot have such a floor because \(\lambda_{\min}(Q_L)\le q_L\to0\).

Both entries of the two-regime table follow with universal constants on the theorem's stated parameter range. The text correctly distinguishes these uniform comparisons from fixed-\(\theta\) asymptotic equivalents.

Antipodal samples remain opposite through every odd layer, so their Gram is singular. At \(\theta=0\), the population recursion is exactly \(Q_L=G\). The equilateral planar Gram is strictly admissible for \(0<\delta<1/2\), has null vector \(\mathbf1\), and its input vectors sum to zero. The stated representational obstruction for a bias-free linear network follows directly and does not imply a nonlinear training theorem.

## 9. Convex offsets: collapse and persistent scalar nonaffinity

**Coverage:** lines 818–966, V.C.1–V.C.8. **Result: pass.**

The assumptions \(0<\varepsilon<1/2\), bounded nonconstant \(C^2\) shape, and all three norm bounds are used where needed. They give a positive lower derivative bound \(b_\varepsilon=1-2\varepsilon\), bounded derivatives for the Gaussian contraction, and exclusion of affine shapes for the residual argument.

The mean is at least \(b_\varepsilon\). Separating the linear term from the bounded offset gives the upper scalar recursion
\[
\sigma_{\ell+1}\le(1-\varepsilon)\sigma_\ell+1.
\]
The interval \([0,1/\varepsilon]\) is invariant and contains \(\sigma_1=1\); the mean gives the positive lower bound. Thus V.C.3 holds, including the preactivation variance at the first layer.

The derivative takes values in \([b_\varepsilon,1]\). Its squared Gaussian average is continuous in \(\sigma\). Equality to one at any positive \(\sigma\) would force the derivative to equal one everywhere by continuity and Gaussian full support, hence \(\psi'=1\), contradicting boundedness. A maximum over the compact positive variance interval is therefore strictly below one. This justifies a single \(\kappa\in(0,1)\) independent of depth and input Gram, even when the pointwise derivative supremum equals one.

The preactivation difference moment at layer \(\ell\) is exactly the preceding feature difference moment, despite nonzero feature means. V.F.11 therefore yields \(D_{\ell,ab}\le\kappa^2D_{\ell-1,ab}\) from \(D_{0,ab}=2(1-G_{ab})\).

All four factors in V.C.2 check:

- Testing against \((e_a-e_b)/\sqrt2\) gives \(\lambda_{\min}(Q_L)\le D_{L,ab}/2\).
- Dividing by \(q_L\ge b_\varepsilon^2\) gives the normalized bound.
- The all-ones Rayleigh vector and the common positive mean give \(\lambda_{\max}(Q_L)\ge3b_\varepsilon^2\), explaining the additional factor three in the ratio bound.

These arguments cover every realizable triple, including repeated and antipodal samples. Since \(C_{L,ab}=1-D_{L,ab}/(2q_L)\), the normalized Gram tends to the all-ones matrix. No convergence of the raw scalar variances is needed or asserted.

The scalar residual is positive at every positive variance: a zero residual would make the continuous shape affine everywhere; boundedness would then make it constant. The residual is continuous in \(\sigma\), so its minimum on \([b_\varepsilon,1/\varepsilon]\) is positive. Absorbing the affine part gives the exact factor \(\varepsilon^2\), and dividing by \(q_\ell\le\varepsilon^{-2}\) gives the relative floor \(\varepsilon^4r_{\varepsilon,\psi}\).

These constants are correctly limited to the fixed shape and mixture. Scaling an allowed shape toward zero shows why a shape-uniform positive residual floor would fail.

For the explicit example, maximizing \(x/[2(1+x^2)^2]\) gives \(x=1/\sqrt3\) and norm \(3\sqrt3/32\). The activation coefficient is indeed \(1/16\), and its derivative lies between \(3/4\) and \(13/16\). Thus the direct Lipschitz contraction with \(\kappa=13/16\) is valid.

## 10. Calibrated family: cancellation, variance, and finite-depth geometry

**Coverage:** lines 968–1085, V.D.1–V.D.9. **Result: pass.**

The shape is nonzero because \(w'(0)=e^{3/2}-1>0\), so \(v_*>0\). Boundedness of the trigonometric shape and all its derivatives is immediate; no unit bound is needed.

The Gaussian characteristic-function derivative gives the exact cancellation
\[
2c_*e^{-2}=e^{-1/2}.
\]
Oddness supplies zero mean, and the definition of \(v_*\) supplies unit second moment. Hence \(\chi\) is orthogonal to \(1,\xi\), and \(\mathbb E\phi_L(\xi)^2=1\). Starting from \(q_0=1\), induction gives \(q_k=1\) at every population layer.

The correlated Gaussian representation eliminates both cross terms in the covariance of \(X+\gamma\chi(X)\) and \(Y+\gamma\chi(Y)\). It remains valid at \(\rho=\pm1\). This proves the exact map V.D.4.

The sine-product identity gives the stated hyperbolic-sine formula. In particular,
\[
v_*=e^{-1}\left(\sinh1-\sinh2+\frac14\sinh4\right),
\]
and the odd-degree numerator is \(1-2^j+4^j/4=(2^{j-1}-1)^2\). Thus the degree-one term vanishes, \(p_3=3/(2N_*)>0\), and all remaining coefficients are nonnegative with sum one. The series and its derivatives converge on bounded intervals.

Consequently \(0\le K(\rho)\le\rho^3\) for \(0\le\rho\le1\), and oddness extends the absolute contraction to negative correlations. Separation is preserved. The tensor floor yields exactly
\[
\mu_\delta=\frac{p_3\delta^2(2-\delta)^2}{3}.
\]

With \(b=(1+\tau/L)^{-1}\), the scalar-weight matrix induction gives V.D.8 without applying any unjustified nonlinear Loewner monotonicity. Discarding the positive semidefinite term \(b^LG\) gives V.D.9. The binomial inequality \((1+\tau/L)^L\ge1+\tau\) is valid for every positive integer \(L\), giving the advertised uniform lower bound.

The hypotheses are every realizable separated triple with \(0<\delta\le1\), fixed \(\tau>0\), and the same activation \(\phi_L\) in all layers of the depth-\(L\) network. No small-\(\gamma_L\) assumption is needed for these finite-depth results.

## 11. Calibrated sequential limit and nonlinear planar witness

**Coverage:** lines 1087–1190, V.D.10–V.D.14. **Result: pass.**

The depth mesh is \(a_L=\tau/L\), while the exact update coefficient is \(a_L/(1+a_L)\). The proof retains this difference; it does not silently replace the finite recursion by exact Euler steps.

The function \(F=K-\mathrm{id}\) is bounded by \(B=2\) and is \(D\)-Lipschitz on \([-1,1]\). Clipping extends those bounds to the real line. The path-integral contraction argument supplies existence and uniqueness directly, on short intervals and then globally. Endpoint equilibria and uniqueness prevent exit from \([-1,1]\). The finite iteration stays there by convexity.

The local ODE remainder is at most \(DBa_L^2/2\). The coefficient discrepancy is at most \(a_L^2\). Thus the error recurrence has exactly the printed additive constant \(B(1+D/2)a_L^2\). Bounding its geometric sum by \(L e^{D\tau}\) gives
\[
\max_k e_k\le B(1+D/2)\tau^2e^{D\tau}/L.
\]
Interpolation adds at most \(B\tau/L\). The constants are uniform over all starting correlations, including the two singular endpoints.

Applying the scalar convergence to each entry gives a unit-diagonal matrix path. Its positive semidefiniteness follows from the positive semidefinite interpolants and finite-dimensional closure. The separated-input eigenvalue bound in V.D.13 is read with the separation hypothesis and \(\mu_\delta\) established in V.D.1; the scalar ODE convergence itself does not require separation.

The iterated limit has the claimed modes:

- At each fixed \(L\), \(n\to\infty\) gives convergence in probability to the population Gram for that fixed activation \(\phi_L\).
- Then \(L\to\infty\) is deterministic and yields \(Q(\tau)\).
- Taking the limit of V.D.9 gives \(\mu_\delta(1-e^{-\tau})\). The elementary logarithm estimate justifies the exponential limit.
- V.F.6 transfers the same sequential result to the initialized total raw kernel.

The deterministic ODE error bound supplies no finite-width estimate, and the text explicitly makes no such inference.

For the equilateral witness, equal initial off-diagonal entries evolve equally and remain \(-r(s)\). The inequalities
\[
-r\le r'\le r^3-r
\]
give \(r(s)\ge e^{-s}/2>0\), ruling out a first zero. On the positive interval the upper inequality makes \(r\) nonincreasing, so \(r\le1/2\). With \(u=r^{-2}\), the reversal from multiplying by a negative derivative factor is correctly handled:
\[
u'\ge2(u-1),\qquad u(0)=4.
\]
Hence \(u\ge1+3e^{2s}\). The eigenvalues of the resulting Gram are \(1-2r\) and \(1+r\) twice, giving exactly V.D.14 and strict positivity for \(s>0\). A scalar rescaling of the singular input Gram cannot have this property.

## 12. Calibrated nonaffinity and local scalar checks

**Coverage:** lines 1192–1270, V.D.15–V.D.19. **Result: pass.**

The inequality \(1-(1+\gamma^2)^{-1/2}\le\gamma^2/2\) gives all three bounds in V.D.15 with the stated factors. Values converge locally uniformly with the weighted global estimate. The unweighted difference has infinite supremum at every finite depth because its nonzero linear coefficient cannot be canceled by the bounded shape.

Orthogonality of \(\chi\) gives the exact residual \(\gamma_L^2/(1+\gamma_L^2)=\tau/(L+\tau)\). The output second moment is one, so the absolute and relative nonaffinities coincide. This concerns all initialized population layers of the depth-dependent family.

For the scalar variance map, Gaussian integration by parts gives \(\mathbb E[Z\chi(Z)]=q\,a(q)\), producing V.D.17. The trigonometric formula gives
\[
a(1)=0,\qquad a'(1)=-\frac{3e^{-1/2}}{2\sqrt{v_*}}.
\]
Differentiation of \(b(q)\) near one is justified by a constant multiple of \(|\xi|\); the same domination gives continuity of its derivative. Therefore
\[
V_\gamma'(1)
=\frac{1+2\gamma a'(1)+\gamma^2b'(1)}{1+\gamma^2}
=1-\frac{3e^{-1/2}}{\sqrt{v_*}}\gamma+O(\gamma^2).
\]
For sufficiently small positive \(\gamma\), its absolute value is strictly below one. Continuity supplies a neighborhood on which the mean-value theorem makes the map contract toward its fixed point one. The neighborhood and contraction factor may depend on \(L\); the statement does not promise uniform stochastic stability.

Finally, \(\mathbb E\chi'(\xi)=0\), so the derivative second moment is exactly \((1+\gamma_L^2M_2)/(1+\gamma_L^2)\). Dropping the denominator and using \(\log(1+x)\le x\) gives the bound \(e^{\tau M_2}\) for its \(L\)-fold product. This is only a product of scalar Gaussian expectations. The text correctly excludes network-Jacobian and trained-backward-field interpretations.

## 13. Final comparisons, gain estimates, and exact scope

**Coverage:** lines 1272–1337. **Result: pass except R1.**

The summary table reproduces the proved parameter ranges and distinctions:

- Odd-mixture sharp infima are for \(d\ge2\) and \(0<\delta\le1/4\); fixed-\(\theta\) scalar equivalents are not promoted to joint asymptotic equivalents.
- Convex-offset normalized Grams tend to rank one while their feature variances remain bounded away from zero; scalar residual floors depend on the fixed shape and mixture.
- Calibrated absolute and normalized conditioning coincide because the population diagonal is exactly one; their uniform floor coexists with residual \(\tau/(L+\tau)\).

The distinction between a numerical depth-uniform initialization floor and a trained theorem at each separately fixed finite depth is logically correct.

For a scalar activation scaling, both exact formulas are correct:
\[
\widetilde Q_1=\alpha^2Q_1,\qquad
\widetilde Q_2=\alpha^2
 \mathbb E[\phi(\alpha Z)\phi(\alpha Z)^T],
\quad Z\sim N(0,Q_1).
\]
They show where the altered activation scale re-enters the next nonlinear argument. R1 is specifically the omitted identity-scaling exception, not an error in these formulas.

For the gain family in this paragraph, nontrivial homogeneity cannot rescue a general recursion-rescaling argument: \(g(0)\ge a-e>0\), and \(g(z)/z\to a\) as \(z\to+\infty\). An identity \(g(\alpha z)=c\,g(z)\) would therefore give \(c=1\) at zero and then \(\alpha=1\) at infinity. This is an elementary check of the intended claim once the trivial case is separated.

The last gain/nonaffinity comparison, under its own assumptions \(a-e>1\) and \(0<e\le1\), is correct. Affine projection removes \(a(1+z)\), so
\[
\mathcal R_g(q)=e^2\mathcal R_\psi(q)\le e^2.
\]
The squared linear Hermite coefficient is
\[
q\bigl(a+e\,\mathbb E\psi'(\sqrt q\,\xi)\bigr)^2
\ge q(a-e)^2.
\]
It lower-bounds the uncentered output second moment. Starting from \(q_0=1\), this gives \(q_\ell\ge(a-e)^{2\ell}\). At layer \(\ell\), the residual is evaluated at \(q_{\ell-1}\) and divided by the output variance \(q_\ell\), producing exactly the upper bound
\[
\frac{\mathcal R_g(q_{\ell-1})}{q_\ell}
\le\frac{e^2}{(a-e)^{2\ell}}.
\]
There is no off-by-one error. The passage does not assert that every allowed shape has a positive absolute margin at arbitrarily large variance.

The closing scope restrictions match the proofs. All finite-width results hold with data, activation, and finite depth fixed. The calibrated family then takes a deterministic depth limit after the width limit. No simultaneous \(L=L(n)\) limit, interchange of limits, positive-training-time result, trained Gaussian recursion, or Jacobian bound is claimed or needed.

## Dependency audit and disposition

The nontrivial ingredients used by Part V are supplied within the two permitted inputs: the fixed-depth Gaussian conditioning induction, the operator-norm net bound, Hermite completeness with Fourier uniqueness, derivative/endpoint identities, the cubic tensor floor, composed-curvature control, strict planar witnesses, uniform Gaussian contraction on a compact variance interval, and the correlation ODE existence/error proof.

The remaining tools are elementary: finite-dimensional spectral decomposition and compactness, Cauchy–Schwarz, Jensen, Minkowski, Chebyshev and Markov inequalities, Gaussian integration by parts and moments, dominated/monotone convergence and Fubini with the stated integrability, elementary \(L^1/L^2\) approximation, Taylor remainders, and geometric/integrating-factor estimates. No unavailable training theorem or external research result is required.

**Disposition:** Correct the identity-normalization exception R1. Apart from that literal qualification, the complete Part V audit found the stated initialization theorems, constants, endpoint arguments, witnesses, and sequential-limit claims justified.
