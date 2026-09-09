# Independent isolated mathematical audit

## Verdict

**CLEAN.** I found no concrete mathematical correction required for Theorem EC8, Lemma EC9, Theorems EC10 and EC11, or the agreements and scope restrictions in Section 12, at the exact input versions identified below. The Gaussian source, continuous-time width transfers, trace-norm assertions, perturbed spectral measure, and physical continuation arguments have the necessary proofs in the supplied chapter.

This verdict concerns the statements actually made: the shallow characteristic population, separately fixed-depth linear operator gradient flow, the two-hidden-layer spectral gradient flow, and their stated observables and overlaps. It does not add gradient-descent, arbitrary-data, depth-uniform, growing-time, or general spectral-restart conclusions. Section 8 does not assert fitting for its whole activation class; Section 10 does not assert fitting for all depths. These distinctions matter to the verdict.

The audit below records the mathematical checks, including the possible failure mechanisms that were tested and why they do not invalidate these statements. There are no required corrections or unresolved proof obligations for the audited claims.

## 1. Isolation, exact inputs, and complete read coverage

Only these two source files were read:

| Input | Bytes | Lines | SHA-256 |
| --- | ---: | ---: | --- |
| `/tmp/pde-exact-capture-isolated.eYCeHCYW/PROOF.md` | 94,998 | 2,452 | `03a6ce55bda3e7c2eb27b1d80f53a081729137c1a4fce26bf42158733affee32` |
| `/tmp/pde-exact-capture-isolated.eYCeHCYW/NOTATION.md` | 5,110 | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

Both hashes were computed before reading and recomputed after the substantive audit; they agreed exactly. Line references in this report refer to these versions.

`PROOF.md` was read completely, without truncated output, in the consecutive ranges 1–240, 241–500, 501–760, 761–1020, 1021–1300, 1301–1580, 1581–1860, 1861–2160, and 2161–2452. `NOTATION.md` was read completely through its final line 98. A subsequent heading search was confined to these same files.

| Portion of `PROOF.md` | Lines read in full | Audit role |
| --- | --- | --- |
| Preamble | 1–12 | Chapter-level scope |
| Section 1 | 13–143 | Existing model, normalization, and comparison theorem |
| Section 2 | 144–368 | Existing cyclic algebra, Wick proof, rooted source |
| Section 3 | 369–545 | Trace ideals, Banach continuation, existing fitting proof |
| Section 4 | 546–718 | Existing cutoff/Picard transfer and the separately scoped GD result |
| Section 5 | 719–828 | Restrictions on the existing nonclosure assertion |
| Section 6 | 829–1058 | Entire graph-independence and nonclosure proof |
| Section 7 | 1059–1167 | Entire unrestricted-field construction and scope examples |
| Section 8 | 1168–1382 | Entire shallow theorem and proof |
| Section 9 | 1383–1543 | Entire generalized Gaussian source lemma and proof |
| Section 10 | 1544–1859 | Entire fixed-depth theorem, continuation, transfer, and tail proof |
| Section 11, setup and theorem | 1860–1980 | Entire spectral theorem and stated normalization |
| Section 11.1 | 1981–2059 | Entire finite invariant reduction |
| Section 11.2 | 2060–2264 | Entire spectral-source derivation |
| Section 11.3 | 2265–2322 | Entire physical existence and fitting proof |
| Section 11.4 | 2323–2412 | Entire uniform finite-width identification |
| Section 12 | 2413–2452 | Entire overlap and scope discussion |

The notation contract was checked throughout: preamble 1–7; network/data/layers 8–43; populations/operators/norms 44–69; initialization/clocks 70–89; limit scope 90–98.

No projects, studies, histories, prior audits, internet sources, skill files, agent files, or additional mathematical sources were consulted. No experiments, builds, installations, Git operations, or input edits were performed. The output directory `/tmp/pde-math-audit.j0ig8urI` was created by a genuine `mktemp -d /tmp/pde-math-audit.XXXXXXXX` call. This `REPORT.md`, created with `apply_patch`, is the only output file.

## 2. Dependency and containment audit

The new arguments do not require an external adaptive Gaussian-program theorem or an unproved random-matrix spectral law.

* EC8 uses its own characteristic construction, dominated differentiation, fourth-moment empirical estimate, finite-net argument, and scalar-clock comparison.
* EC9 supplies the fixed-word Gaussian moment and variance calculation and a coarse operator-norm bound. Its argument was checked independently of the similar existing Lemma 2.
* EC10 uses EC9, elementary trace-class estimates, a Banach-space integral contraction, energy control, and a fully described finite-word Picard transfer. The proof includes its own singular-value continuity and trace-tail arguments.
* EC11 uses EC9 for the Gaussian inputs and the EC10 physical energy argument for the projected finite network. It derives the initial scalar measure, including the negative atom, and proves its own physical spectral continuation and time-uniform transfer.
* Section 12 uses the actual common finite flows and uniqueness of a deterministic limit. Its comparison to Sections 1–4 requires the old rooted-source and varying-space arguments, which were read and checked in full.

The two mentions of `gaussian_calculus.md` do not create an unresolved dependency. At line 1469 the reference is an alternative to the moment-generating-function derivation already given immediately above it. At lines 2451–2452 the external fixed-program theorem is expressly not being used as a continuous-time theorem. Neither reference was followed or needed.

The ordinary underlying tools—finite-dimensional spectral decomposition, singular-value expansions for trace-class maps, completeness, dominated convergence, and elementary integral inequalities—are used in their standard domains. The nontrivial ingredients specific to these limits are developed in the chapter. In particular, the proof does not silently require strong asymptotic freeness, a sharp largest-singular-value limit, resolvent inversion, or convergence of an adaptive program with growing word length.

## 3. Normalization, mobility, and clock checks

The stored readout has variance one in every new model. Dividing an endpoint by `sqrt(n)` is a proof embedding, not a change to that initialization. This agrees with the explicit exception to the small-readout convention in `NOTATION.md`.

For Section 8,

\[
\partial_{a_i}(f_n-y)^2=2r_n\phi(u_i)/n,\qquad
\partial_{u_i}(f_n-y)^2=2r_na_i\phi'(u_i)/n.
\]

Multiplying by the two mobilities `n kappa` yields EC8.2 exactly. Differentiating the prediction gives the two block contributions to `K_n` with the stated factor `1/n`. Thus the physical clock is `ds/dt=-2 kappa r`, and not the clock for a half-squared loss.

For Section 10 the normalized endpoint derivatives are `-2 kappa r b_1` and `-2 kappa r x_L`. A stored middle derivative is

\[
-2\kappa r\,\delta^{(\ell+1)}(z^{(\ell)})^T/n
=-2\kappa r\,b_{\ell+1}x_\ell^T.
\]

There is therefore no additional `1/n` in the Hilbert rank-one representative. Its norm is the product of the two normalized vector norms. Endpoint and middle contributions to EC10.3 are the squared gradient norms for these exact mobilities.

For Section 11, projecting the first matrix onto the single input introduces the factor `x_1^T x_1/d=1` in the projected equation. The unused input directions remain fixed. Gaussian row projections have variance one before division by `sqrt(n)`, independently across rows, so the projected `u_n` has the distribution used in the proof. The stated alternative storage `mathsf A=sqrt(n) B_n` changes the middle mobility from `kappa` to `n kappa`, as a linear parameter rescaling must. The prediction `n^(-3/2) a_raw^T mathsf A u_raw` is consistent with that change.

All residuals have sign `prediction minus label`. No backward vector absorbs the residual. In particular, finite initial residuals are not replaced by `-y`: they are `F_n(0)-y` in EC8, `f_n(0)-y` in EC10, and `f_n(0)-y` in EC11. The finite spectral imbalance `delta_n` is also retained until convergence is proved.

## 4. Section 8: shallow marked characteristics

### 4.1 Existence and growth on both signs of feature time

Under EC8.1 the vector field `(phi(U), A phi'(U))` is locally Lipschitz. On a bounded set its derivatives involve only `phi'`, `phi''`, and the bounded local value of `A`. Its magnitude is bounded by a constant times `1+|A|+|U|`. Applying the integral estimate also to the reversed vector field gives EC8.7 for positive and negative feature times. This is sufficient to rule out finite escape of every marked characteristic.

The growth estimate does not assert a global Lipschitz constant uniform over all marks, which would generally fail because of the `A phi''(U)` derivative. The argument uses local uniqueness and a linear growth bound instead; that distinction is handled correctly.

For `J=1+|a_0|+|u_0|`, the prediction integrand and both kernel terms have a compact-feature-time bound `C_S J^2`. Direct differentiation gives

\[
\partial_s(A\phi(U))=\phi(U)^2+A^2\phi'(U)^2,
\]

\[
\partial_s H
=4A\phi(U)\phi'(U)^2
 +2A^3\phi'(U)^2\phi''(U).
\]

The second expression has an integrable `C_S J^3` envelope. There is no missing third derivative of the activation. The stated C2 assumptions suffice for all differentiation and feature-time continuity used here.

### 4.2 Consistency, physical continuation, and restart

The centered readout mark is independent of the first-layer mark, so `F(0)=0` even without a normalization of `E phi(G)^2`. Dominated differentiation yields `F'=K>=0`. The scalar clock is locally unique because `F` is continuously differentiable.

Along the clock,

\[
\frac{d}{dt}(F(s(t))-y)
=-2\kappa(F(s(t))-y)K(s(t)).
\]

It follows that `|r(t)|<=|y|` and `|s(t)|<=2 kappa |y|t`. Hence finite physical time stays inside a compact feature-time interval even if `F` never reaches `y`. Evaluating the characteristic growth estimate there proves all compact-time moment bounds and continuation.

The converse uniqueness argument is also valid. For a marked classical solution in the stated compact-time moment class, integrating its scalar residual defines a clock. Pointwise uniqueness of the nonautonomous characteristic equation identifies the fields at that clock, and dominated differentiation preserves `E[A phi(U)]-r=y`. Scalar-clock uniqueness then identifies the entire solution.

The same argument works for a consistent restart pair with every finite moment: the envelope becomes `1+|A_*|+|U_*|`, and the clock bound uses `|r_*|`. Independence or Gaussianity of restart fields is not required. The restart state must retain the marked fields, as the theorem specifies.

### 4.3 Empirical and physical-time limits

The derivatives of the separate kernel summands have the claimed cubic envelope. Under the Gaussian initialization, the integrands and this envelope have finite fourth moments. EC8.12 is the correct fourth-moment expansion: only the all-equal index term and pair-pair index terms survive centering, with coefficient `3 n(n-1)` in the latter.

The resulting `O(n^-2)` probability bound is summable. It does not require independence between different widths. Applied to the nested iid sequence, it proves almost-sure convergence at each point of countably many finite nets and for the envelope. EC8.13 then proves uniform convergence in feature time. This includes the two block energies individually, rather than only their sum.

The finite clock uses the same marked characteristics and the actual initial residual. Since `F_n'=K_n>=0`, the finite clock has the bound `2 kappa |F_n(0)-y|t` and is global. Eventual control of `F_n(0)` puts both clocks in a common deterministic compact interval. In EC8.14, the comparison can use the Lipschitz constant of the limiting `F`; a uniform derivative estimate for random `F_n` is not needed. Uniform empirical convergence and continuity of the limiting readouts then give EC8.5 at these clocks.

### 4.4 Degenerate cases and actual scope

`kappa=0` gives stationary fields and a purely initial empirical limit, as claimed. `y=0` makes the initialized population stationary while allowing a nonzero finite initial residual. Negative labels are covered by the two-sided characteristic construction.

The activation `phi=0` is allowed: then `K=0` and a nonzero target is not fitted. This is not a counterexample to EC8 because no general shallow fitting conclusion is stated. No positivity of the initial kernel, normalization `E phi(G)^2=1`, or empirical path-law theorem is being assumed.

**Section 8 finding: clean.**

## 5. Section 9: Wick counts, free indices, concentration, and Fock source

### 5.1 Operator-norm event

A maximal 1/4-separated sphere set has at most `9^n` points by the stated volume comparison. Approximating each argument of a bilinear form loses at most half the operator norm in total, giving the factor two. Each Gaussian bilinear form has variance `1/n`; the threshold six therefore has two-sided tail at most `2 exp(-18n)`. Taking the union over at most `81^n` pairs proves EC9.5. A finite number of matrix labels and the two vector squared-norm laws yield EC9.4.

No step requires the optimal spectral edge two. The coarse bound twelve suffices everywhere it is used later.

### 5.2 Mean trace law and transpose orientations

For a trace word with `2k` matrix occurrences, each nonzero Wick pair contributes `n^-1` and imposes equality of the raw row indices and of the raw column indices. These raw indices correctly account for transpose markers. With `v` equivalence classes of trace indices, summing assignments contributes exactly `n^v`; assignments are not required to be injective. Together with trace normalization, the term is `n^(v-k-1)`.

The quotient walk is connected and has `k` paired edges counted with multiplicity. Therefore `v<=k+1`. Loops, parallel edges, and accidental identifications cannot increase this bound. Equality forces a tree.

On a tree the closed walk traverses each paired edge once in each direction. Because the covariance identifies raw rows with rows and columns with columns, this forces opposite transpose markers. Removing a leaf removes adjacent paired occurrences; repeated deletion yields a noncrossing pairing. Conversely, restoring the adjacent pairs of a noncrossing, label-matching, oppositely oriented pairing adds one free index per pair. This establishes both necessity and sufficiency for the surviving power of `n`.

Thus real Gaussian transpose pairings that are not of this orientation can occur at finite width, but their contribution is suppressed. The proof has not accidentally replaced a real matrix by a complex Gaussian matrix at finite width.

### 5.3 Variance and rooted concentration

In the second-moment expansion, pairings internal to the separate trace walks cancel against the product of means. Any remaining pairing joins the walks, so their quotient is connected. With `k` paired edges, the two normalizations give `n^(v-k-2)<=n^-1`. The finite number of pairings at a fixed word length proves the claimed L2 convergence. Odd words have zero mean but their second moments are still controlled by this two-walk argument.

For a root independent of a possibly nonsymmetric real matrix `T`, the exact conditional quadratic-form variance is `2 ||sym T||_HS^2/n^2`; for two independent roots the cross-form second moment is `||T||_HS^2/n^2`. The operator-norm bounds in EC9.7–EC9.8 follow. With `T=P_n^T Q_n`, conditioning on the matrices keeps the norm event measurable and preserves root independence. This avoids conditioning incorrectly on an event involving the same roots being averaged.

### 5.4 The limiting operator representation

In the expansion of `c_j=ell_(j,+)+ell_(j,-)^*` and its actual adjoint, a nonzero vacuum term pairs an annihilator with a matching creation nested inside the surrounding operations. For either orientation of a given pair, the available letter is determined by the transpose markers. Every surviving Wick pairing contributes exactly one, and every nonzero vacuum term gives such a pairing.

The direct sum of two Fock copies ensures orthogonality of the entire two generated root spaces. Merely choosing orthogonal roots in one arbitrary representation would not imply the vanishing cross-root formulas, but the construction here does. Typed copies preserve these identities for compatible paths. For `q=0`, the construction reduces to two orthonormal vectors in `R^2`, which is precisely what EC10 needs for `L=1`.

There is no degree growing with width, no assumption that a transpose is an independent random matrix, and no inference of operator-norm convergence between spaces.

**Section 9 finding: clean.**

## 6. Section 10: fixed-depth operator gradient flow

### 6.1 State space, consistency, and initial values

For fixed `L`, the product of the two endpoint Hilbert spaces, the finitely many trace-class spaces, and the real residual coordinate is a Banach space with the stated sum norm. Sources are bounded and immutable. The identity

\[
\|v\otimes w\|_1=\|v\|\|w\|
\]

and its two-term difference bound prove that the operator velocities lie in the required trace-class spaces. Product telescoping controls every forward/backward vector, residual field, and kernel on a state ball. Constants may depend on `L`, as permitted.

Inserting the velocity of each factor into `f=<a,B_(L-1)...B_1 u>` gives exactly the two endpoint squares and all middle products in `K`. Hence `dot f=dot r`, so consistency follows from the initial state; it is not assumed independently at later times.

Different root sectors give `f(0)=0`. Each initial forward or backward path uses distinct matrix labels, making all annihilation terms vanish at its successive applications. All its vector norms are one. There are two endpoint contributions and `L-1` middle contributions, giving `K(0)=L+1`. At `L=1` the middle list is empty and this calculation still gives two.

### 6.2 Physical energy estimate and global continuation

The residual equation gives

\[
\int_0^T r^2 K\,dt\le r(0)^2/(4\kappa),\qquad |r(t)|\le|r(0)|.
\]

For each individual block, its squared feature-velocity norm is a term of `K`; for a middle block this is also the square of its trace norm. Consequently

\[
\int_0^T\|\dot\theta\|\,dt
\le 2\kappa\sqrt{T}\left(\int_0^T r^2K\,dt\right)^{1/2}
\le |r(0)|\sqrt{\kappa T}.
\]

This bounds the sum state norm after summing over the fixed number of blocks. No Hilbert–Schmidt assumption on the source operators is needed. At a hypothetical finite maximal time, boundedness of the vector field makes the state Cauchy in this Banach norm; completeness supplies a limiting state and local existence extends it. Merely bounding a norm without this Cauchy/extension step would not suffice, but that step is present.

The same estimate applies to consistent restart states and to the finite projected model using its actual residual. It proves continuation, not fitting for every depth.

### 6.3 Cutoff and fixed-iteration transfer

The source event and the physical energy estimate give the deterministic radius EC10.11. The cutoff has a strict margin beyond it. Multiplication by the cutoff of the full state norm produces a globally bounded, globally Lipschitz field. For an inside point and an outside point, the segment meets the support boundary; the vanishing cutoff and its distance bound control the difference there. This addresses the boundary case of the claimed global Lipschitz estimate.

Picard iteration starts with the actual initial state in each space, including its residual. At a fixed iteration number, endpoints are finite sums of source words and increments are finite sums of rank-one maps between such words. Every source action appends a letter; multiplication of rank-one maps only adds Gram contractions. The norm cutoff contributes a scalar coefficient and does not enlarge the vector alphabet. Time integration changes coefficient paths, not the finite word list.

For column maps `V,W` and a coefficient matrix `D`, the partial-isometry factorizations give the nonzero singular values of `VDW^*` as those of `G_V^(1/2) D G_W^(1/2)`. This remains valid when either Gram matrix is singular. The proof's square-root and singular-value continuity arguments use finite-dimensional compactness and do not invert a Gram matrix. Thus endpoint norms, increment trace norms, and the cutoff itself have the required finite-Gram continuity.

For a fixed iteration, this continuity holds for coefficient paths uniformly in time: finite continuous operations preserve uniform convergence on bounded paths, and integration is a bounded map in the supremum norm. EC9 therefore transfers each fixed numerical description.

The factorial remainder EC10.13 follows by summing Picard increments bounded by `M_T H_T^(h-1) t^h/h!`. Its constants are common to all relevant widths. The correct limiting order is used: choose a finite iteration number to control the remainder, and only then let width tend to infinity. At no point is a Gaussian fixed-word theorem applied to the completed adaptive trajectory as if it were a fixed polynomial.

### 6.4 Observable and increment assertions

The three-term comparison EC10.14 subtracts operators only within their own ambient spaces. Its middle term compares scalar numerical descriptions. Rooted readouts built from the stated finite operations are polynomial expressions in their current factors and have the needed within-space Lipschitz bounds on the common ball.

The trace norm is 1-Lipschitz in trace norm. The ordered singular-value bound follows from approximation numbers, with the rank argument valid also on the limiting Hilbert spaces. A fixed singular-value index therefore transfers. Maps formed from a fixed finite vector list have uniformly bounded rank, so the rank-one estimates also control their Schatten norm readouts. None of this requires convergence of the source operators in operator norm across widths.

### 6.5 Uniform trace-tail control

The tail assertion is stronger than convergence of finitely many singular values, and the proof supplies a separate reason for it. On the source event, the actual state is Lipschitz in time with a deterministic bound and its vector field is Lipschitz on the containing ball. Thus each `h_ell,n=dot P_ell,n` is Lipschitz in trace norm with a common constant `C_T`.

The integral of these rank-one velocities is uniformly approximated by a left Riemann sum on `N` cells. Summing the integral of `C_T(v-v_left)` over full and partial cells gives the error `C_T T^2/(2N)`. The number of rank-one summands is at most the stated `N+1` (that upper bound is harmlessly loose).

For an approximant `R` of rank at most `N+1`, adding `R` to a rank-`<j` approximation of `P-R` gives

\[
s_{j+N+1}(P)\le s_j(P-R).
\]

Summing proves that the entire nuclear tail beyond `N+1` is at most `||P-R||_1`. This bounds the supremum over time before taking probability, so there is no erroneous interchange of a supremum and a pointwise tail limit. Removing the common source event gives EC10.7 in the stated order of limits. The same estimate applies to the population increment.

**Section 10 finding: clean, including the trace-norm and trace-tail claims.**

## 7. Section 11: exact reduction and explicit spectral source

### 7.1 Finite invariants and retained finite corrections

With `g_n=-2 kappa r_n`, direct differentiation gives

\[
\frac d{dt}(BB^T-aa^T)=0,\qquad
\frac d{dt}(\|a\|^2-\|u\|^2)=0.
\]

Writing `v=Bu`, `q=||a||^2`, and `delta=||a||^2-||u||^2`, the velocity is

\[
\dot v=g_n[a\|u\|^2+BB^Ta]
=g_n[C+(2q-\delta)I]a.
\]

Consequently differentiating `a^T v` gives EC11.10, including the `-delta q` term. Expanding `C=BB^T-aa^T` reduces it to the three original nonnegative block energies. This check is essential: `C` is not positive semidefinite, but the exact finite kernel is nonnegative for the network state.

The matrix-valued spectral measure is positive because every scalar quadratic combination equals the spectral measure of the corresponding combination of the two initial vectors. Its off-diagonal entry is retained at finite width. The real two-channel mode equations are therefore an exact representation, with the functional calculus using one fixed `C_n`. The actual `f_n(0)-y` is used in the residual equation. Neither `delta_n=0` nor a zero initial cross measure is imposed prematurely.

### 7.2 Base measure and its transform

For the alternating word `(BB^T)^k`, each noncrossing pair joins opposite parities, so every noncrossing pairing has the required transpose orientation. Splitting at the first pair yields the Catalan recursion in EC11.15.

The density proposed for `rho_0` has exactly the Catalan moments. After `lambda=4t`, the integral recurrence has ratio `(k+1/2)/(k+2)` before the additional factor four in successive moments. The base integral is `pi/2`, so EC11.16 has both the correct mass and factorial formula. The matching recursion identifies every moment.

The norm event places the empirical spectrum in `[0,144]`. Bernstein approximation is proved explicitly with the binomial variance bound, so polynomial moment convergence does give weak convergence on that event. An unproved sharp support limit is not being used.

For negative `z`, the sign convention is `m(z)=int (z-lambda)^(-1) d rho_0`, making `m(z)<0`. Its large-negative-`z` moment series gives

\[
z m(z)(1-m(z))=1.
\]

The trigonometric substitution and elementary integral in the proof extend the displayed branch to every negative `z` and give `m(-1/2)=-1`. Thus using this particular negative argument does not rely on an unstated analytic continuation theorem.

### 7.3 Rank-one perturbation, atom, and continuous density

Conditioning on `M_n` makes the quadratic resolvent form in `a_n(0)` concentrate about the normalized trace. The resolvent bound `1/|z|` holds because `M_n>=0`. Solving `(z-M_n+aa^T)w=a` gives the denominator `1+h_n(z)`, not `1-h_n(z)`. On the norm event, `C_n>=-4I`, so the use of real `z<-4` is legitimate.

The proposed continuous part of `rho_a` is

\[
\frac{\lambda}{1+2\lambda}\,d\rho_0(\lambda).
\]

From `m(-1/2)=-1`, its auxiliary integral satisfies `int (1+2lambda)^(-1) d rho_0=1/2`, making the continuous mass `1/4`. Adding the proposed mass `3/4` at `-1/2` gives total mass one.

For `z<-4`, partial fractions yield

\[
\int\frac{d\rho_a(\lambda)}{z-\lambda}
=\frac{3}{4(z+1/2)}
 +\frac{z m(z)-1/2}{1+2z}
=\frac{z m(z)+1}{1+2z}
=\frac{m(z)}{1+m(z)}.
\]

The last equality follows directly from the quadratic equation for `m`. This verifies the density and the negative atom with the correct sign and normalization. As an independent numerical-constant check by differentiation of the explicit formula, `m'(-1/2)=-4/3`, so the simple pole of `m/(1+m)` has coefficient `(-1)/(-4/3)=3/4`, agreeing with the displayed atom. This is an algebraic check, not an additional inversion assumption.

The conversion from transform convergence to moments is also sound. For a fixed moment order `k`, multiply the finite resolvent expansion by `z^(k+1)`. The remaining error is bounded by a common mass times `144^(k+1)/(|z|-144)`. Choose a sufficiently negative fixed `z` first. Then transform convergence and convergence of the lower moments control the rest as `n` grows. The large coefficients of those lower moments are finite because `z` is fixed during that limit. This induction proves each moment without interchanging a width limit with an uncontrolled limit in the spectral parameter. Bernstein approximation then proves weak convergence.

### 7.4 The second channel and the cross entry

Although `v_n(0)=B_n(0)u_n(0)` and `C_n` are dependent, conditioning on `(B_n(0),a_n(0))` leaves `u_n(0)` independent Gaussian. The quadratic-form concentration in EC11.22 is therefore justified. The norm event used for that conditional estimate can be chosen measurable in precisely those conditioning variables.

For each fixed polynomial, telescoping powers of `C_n` and `M_n` gives a trace-norm difference of order one on that event, because `C_n-M_n` is rank one with bounded trace norm. The additional normalization `1/n` makes its contribution vanish in EC11.23. The limiting second diagonal measure is consequently `lambda rho_0`, whose mass is one.

The cross entry is conditionally centered and has the `O(1/n)` conditional variance in EC11.24. For arbitrary continuous tests, its total variation is controlled by `||a|| ||v||`, using a spectral partition and Cauchy–Schwarz. Thus polynomial convergence extends to weak convergence for this signed measure as well; pointwise cancellation of a few moments alone would not suffice.

On the common event, the support interval `[-4,144]` and the diagonal-mass bounds `4` and `576` are valid. The same estimates control the cross variation. Finally `delta_n` tends to zero by the two root norm laws, and the independent Gaussian averages give exactly `E f_n(0)^2=1/n`.

### 7.5 Scalar encoding and initial constants

Adding the two diagonal measures gives exactly

\[
\nu=\tfrac34\delta_{-1/2}
 +\frac{(1+\lambda)\sqrt{\lambda(4-\lambda)}}{\pi(1+2\lambda)}
   \mathbf1_{(0,4)}\,d\lambda.
\]

Its mass is two. The stated `alpha` and `beta` are square roots of the two Radon–Nikodym densities: `alpha^2 nu=rho_a` and `beta^2 nu=rho_v`, including the atom where `beta=0`. No expectation with an unintended probability normalization is used.

The complex encoding of the two real channels has the identities

\[
|\alpha c_1+i\beta c_2|^2=\alpha^2c_1^2+\beta^2c_2^2,
\]

\[
\operatorname{Re}[(\alpha c_1-i\beta c_2)(\alpha d_1+i\beta d_2)]
=\alpha^2c_1d_1+\beta^2c_2d_2.
\]

They justify the scalar readouts without assuming that the finite cross measure was zero. At initialization `q=1`, `F=0`, and `||pi||^2=1`. The continuous first moment of `rho_a` is `3/8`, canceled by the atom's `-3/8`; hence `K(0)=1+0+2=3`. The three initial block-energy limits are individually one.

**Finite reduction and spectral-source finding: clean.**

## 8. Section 11: global L2 dynamics, fitting, and uniform identification

### 8.1 Physical continuation despite the negative atom

Multiplication by `lambda` is bounded in `L2(nu)`. Treating the complex fields as real pairs, the readouts and vector field are continuous polynomials on the stated Hilbert product and are locally Lipschitz on balls. Differentiating its pairings is justified in Hilbert norm and gives

\[
\dot F=\dot r=-2\kappa rK,\qquad
\dot q=-4\kappa rF.
\]

The initialized identity `F-r=y` is preserved. The lower support endpoint gives

\[
K\ge 2q^2-q/2.
\]

The proof first restricts to `q>1/2`, where this bound is positive; it does not assume global positivity for arbitrary spectral states. There the residual formula gives `r=-y vartheta`, `F=y(1-vartheta)`, with `0<vartheta<=1`. Therefore

\[
0\le\dot q=4\kappa y^2\vartheta(1-\vartheta)\le\kappa y^2.
\]

Starting from `q=1`, the trajectory cannot exit this region through its lower boundary. This closes the bootstrap and proves `q>=1` and `K>=3/2` throughout the maximal existence interval.

The upper bound on `q` controls `||psi||`, and EC11.28 bounds `||dot pi||` on every finite horizon. Together with the residual bound, these bound the whole state. The same complete-space continuation argument as in EC10 then rules out a finite maximal physical time. This proof does not infer physical continuation from completeness of a feature clock.

The residual equation now yields `|r(t)|<=|y| exp(-3 kappa t)` and fitting for this initialized spectral population. If `r!=0`, `dot r!=0` because `K>=3/2`; if `r=0`, every displayed velocity vanishes. At `y=0` the canonical state is stationary. These are exactly the stationarity claims made.

The argument proves forward restart along the canonical trajectory. It does not prove global existence for all unrelated triples in the ambient L2 product, and the theorem does not claim that stronger restart domain.

### 8.2 Uniform weak-test transfer on the larger interval

Extending the real mode coefficients to `J=[-4,144]` is legitimate: with the limiting bounded physical `q,r`, these are linear equations in each spectral parameter with coefficients uniformly bounded on `J x [0,T]`. Their integral equations give both boundedness and continuity in `lambda,t`. Linear uniqueness identifies their scalar encoding with the already constructed L2 solution.

The finite modes can likewise be extended using their actual finite network coefficients. Finite physical continuation was already established by EC10's energy argument. No assertion of positivity of `lambda+2q_n-delta_n` on all of `J` is necessary for these linear extensions.

Each family of tests in EC11.29 is compact in `C(J)`, as the continuous image of a compact time interval. Finite uniform nets, weak convergence for each net point, and common total-variation bounds prove uniform-in-time convergence of their measure integrals. This is the required step from weak initial measures to moving observables; the argument does not equate weak convergence with convergence for arbitrary varying tests.

Before the first stopping time where the mode/residual error reaches one, both mode systems stay in a common bounded ball. Expanding the quadratic readouts one factor at a time gives EC11.30; the nonlinear `2q_n-delta_n` term is controlled by the same `q` difference and the retained `delta_n` error. Subtracting the integral equations has initial residual error exactly `|f_n(0)|`, as in EC11.31.

The scalar integral inequality bounds the entire stopped error by a deterministic constant times `|f_n(0)|+epsilon_n(T)+|delta_n|`. This tends to zero in probability. On the resulting event where that bound is less than one, continuity excludes a stopping time before `T`. The proof consequently gives the unstopped uniform convergence stated in EC11.7.

Finally, EC11.32 correctly identifies the individual block energies. In particular `BB^T=C+aa^T` gives the second one as the `lambda` integral plus `q_n^2`; the third is `q_n(q_n-delta_n)`. Their limits sum to the spectral kernel and are each controlled by the same transfer argument. This avoids claiming convergence only of an aggregate that might conceal compensating block errors.

**Global spectral and finite-width finding: clean.**

## 9. Existing dependencies and overlap of the new descriptions

The portions of the old chapter actually used by the new comparisons have the needed estimates. In the cyclic construction, every length-three path crosses a rank-one endpoint, so `rank C^3<=4`; the fourth-power trace is four times the output. Thus the physical vector field is trace class even though its fixed middle sources need not be Hilbert–Schmidt. The old trace-ideal bounds, derivative identity, residual energy estimate, and trace-norm continuation are consistent with the individual-block arguments in EC10.

The old Gaussian word proof uses the same valid tree/free-index and joining-variance mechanism checked in Section 5 of this report. Its terminal root letters preserve orthogonality of generated spaces. The old Q-space cutoff, finite-rank Gram formula, and factorial Picard remainder also give an actual varying-space transfer, rather than an invalid subtraction of source operators. Thus Section 12 does not invoke an unproved old width-limit assertion.

The existing L3 fitting argument was also checked: both endpoint squared norms have derivative `-4 kappa r f`, are equal and at least one along the initialized trajectory, and give `K>=2|f|`. Since `K(0)=4`, a nonzero label creates a nonzero output immediately, after which the residual has the stated exponential bound. This is a depth-specific existing conclusion, not a proof of fitting at arbitrary depth.

Sections 5–7 were read completely. Their state-universal bounded-contraction obstruction does not apply to an unrestricted operator field or the special initialized spectral fields. Its hypotheses fix an encoder alphabet and demand an open-state identity across sufficiently large widths. The unrestricted transport example makes this distinction explicit. Consequently the new field representations do not contradict that negative result, nor do they establish a forbidden finite scalar closure.

For the actual new overlaps:

* At `L=1`, `phi(z)=z`, the characteristic solution gives `F(s)=sinh(2s)` and `K(s)=2cosh(2s)` because the two initial Gaussian marks are centered, independent, and have unit variance. The two orthonormal Hilbert roots give the same pairings and the same physical clock. The comparison is on their common positive-mobility parameter range; EC8 additionally permits zero mobility.
* At `L=2`, `x_1=1`, EC10 and EC11 have exactly the same finite distribution, flow, residual convention, and block observables. If two deterministic proposed limits differed by a positive amount on a compact horizon, the two convergence-in-probability errors against the same finite process could not both tend to zero. This proves the stated agreement. It does not reconstruct every operator-rooted signature from the spectral fields.
* At `L=3`, the old final-letter Fock sectors and EC9's two direct-sum sectors have identical rooted Grams. Together with the common finite flow and the validated width limits, this gives the asserted agreement of rooted readouts. Extra unused directions in a Hilbert representation do not affect this conclusion.

The old Section 4 GD proof is separately scoped to its existing L3 theorem. Its presence supplies no additional new GD statement. The new comparisons are all in continuous physical gradient flow, and Section 12 says so explicitly.

## 10. Final disposition

All new sections and all existing internal dependencies used by them were read and audited. The tested failure points—Gaussian orientations and free-index counts, joining-pairing variance, full rooted orthogonality, singular Gram matrices, cutoff boundaries, Picard limit order, nuclear tails, finite residual and imbalance corrections, negative spectral mass, physical continuation, fitted-population versus finite-horizon limits, and common clocks—are resolved by the supplied arguments.

**Required corrections: none. Verdict: CLEAN for the stated theorem scopes at the recorded hashes.**
