# Internal check of SOURCE_GEOMETRY.md

Date: 2026-09-30. This is an internal mathematical check, not an independent promotion review. The entire assigned source was read. No outside scientific inputs or other study artifacts were used in this check.

Checked source: `studies/adaptive_functional_population_20260930/SOURCE_GEOMETRY.md`.

Checked SHA256: `d0aea8c39e1b2729c3d0c3a8598766b95ec7b4df44f9b64976d62d0270d88d72`.

## Outcome

**The central rank-2p source lemma, its canonical deep-flow specialization, the intrinsic-geometry rate, and the numerical exponent comparisons are correct under the assumptions identified below.** There is no fatal error in the source theorem. Two local qualifications should be corrected before the note is treated as a fully self-contained statement: the abstract lemma needs an integrability qualification, and the learned-state formula should retain its p-squared term until an explicit domination condition is imposed. If “strictly subquadratic” describes total learned state including the first layer, it also requires d=o(n).

The source correctly labels the autonomous trajectory rate and the dense-width approximation rate as unproved additional bridges. This check does not upgrade either bridge.

## 1. Rank-2p Frobenius lemma: verified

For a finite measurable p-cell partition, write \(\bar b=E[b\mid\mathrm{cell}]\). The identity

\[
 E[a\bar b^T]=\sum_jP(C_j)E[a\mid C_j]E[b\mid C_j]^T
\]

is exact even if a and b are strongly correlated within each cell; it has rank at most p. Empty cells can be assigned arbitrary conditional means because they have zero weight.

The conditional mean minimizes squared error among cell-constant vectors. Therefore the proposed center assignment implies

\[
 E\|b-\bar b\|^2\le L_b^2E\min_jd_X(x,c_j)^2.
\]

For \(R=E[a(b-\bar b)^T]\), triangle inequality for the nuclear norm and scalar Cauchy-Schwarz give

\[
 \|R\|_*\le E\|a\|\|b-\bar b\|
 \le A_2L_b\left(E\min_jd_X(x,c_j)^2\right)^{1/2}.
\]

If \(R_p\) is a rank-p singular-value truncation, then

\[
 \sum_{j>p}\sigma_j(R)^2
 \le \sigma_{p+1}(R)\sum_{j>p}\sigma_j(R)
 \le\frac{\|R\|_*^2}{p+1}.
\]

This establishes the claimed inequality by taking \(G_{2p}=E[a\bar b^T]+R_p\). The case 2p>=n is trivially exact. If center distortion approaches an unattained infimum, the best rank-2p approximation error of the fixed matrix G is bounded by each corresponding right-hand side and hence by its limit. No convergence of the constructed center sets or factors is required.

The proof correctly distinguishes this spectral approximation from p-center quadrature. The extra p^{-1/2} factor cannot be assigned to the p-center gradient itself.

**Qualification requested:** the abstract lemma currently assumes only a in L2 and Lipschitz b on an unrestricted metric space. These do not ensure that G=E[ab^T] exists when Q_p is infinite. Add, for example, “assume b is square-integrable” or state the nontrivial lemma for Q_p<infinity, which implies b is square-integrable. Indeed, for any finite-distortion center set, b is bounded at its finitely many centers and its deviation from the assigned center is square-integrable. Measurability of a and the input law is also implicit in all expectations. The intended bounded-activation application already satisfies b in L2, so this is a standalone-statement issue rather than a failure of the application.

## 2. Finite laws and general labels: verified

No step differentiates a, the teacher, or the residual. If the target law is over (x,y), the cells depend only on x, while the conditional expectations of a average both x and y within each cell. Equations (4)--(6) remain valid without deterministic labels or within-cell independence.

In this case Q_p should be understood as the quantization distortion of the x marginal. Naming that marginal explicitly would remove a notation ambiguity, but no mathematical change is needed.

For the canonical factor \(a=r\delta_l/\sqrt n\), the bound

\[
 E\|a\|^2\le D_l^2E r^2
\]

needs only the uniform-in-x normalized backward bound and finite squared residual. Zero readout gives initial squared loss E y^2=Y^2, so loss dissipation yields E r(t)^2<=Y^2. Labels need only have finite second moment; their differentiability and pointwise boundedness are unnecessary here.

Finite empirical laws of arbitrary size and with arbitrary probability weights are therefore covered. The constants do not directly involve sample count. A finite law does not automatically satisfy a favorable p-rate with constants independent of its geometry: for p at least the support size, Q_p=0; for smaller p, the quantitative claim still uses its actual quantization distortion. The source does not conceal this dependence.

## 3. Canonical normalization and deep forward Lipschitz bounds: verified

The correct parameter norm is

\[
 \|\theta\|^2=\|w\|_2^2/n+\|A_1\|_F^2/n+
 \sum_{l=2}^L\|A_l\|_F^2.
\]

In this metric the supplied training equations are the negative gradient of the squared loss. Consequently

\[
 \int_0^T\|\dot\theta\|^2dt
 =\mathcal R(0)-\mathcal R(T)\le Y^2,
 \qquad
 \int_0^T\|\dot\theta\|dt\le Y\sqrt T.
\]

Each component displacement is bounded by this common path length. The operator-norm bounds (8) therefore follow from the Frobenius bounds, with the first layer divided by sqrt(n) as stated.

For the first layer,

\[
 \frac{\|W_1(x-x')/\sqrt d\|_2}{\sqrt n}
 \le\frac{\|W_1\|_{op}}{\sqrt n}
       \frac{\|x-x'\|_2}{\sqrt d}.
\]

Multiplication by the activation Lipschitz constant A gives the j=1 case of (9). Each later layer multiplies the bound by A Q, proving

\[
 L_{b,j}=A^jQ^{j-1}(K_1+V).
\]

Backward propagation gives one factor A per activation and one Q per intervening hidden matrix, proving

\[
 D_l=A^{L-l+1}Q^{L-l}V.
\]

Thus (10) and substitution into (3) establish (11), with no missing n factor and no coordinatewise response bound.

The width-uniformity claim is appropriately conditional on the initialization operator bounds. For the usual first-layer Gaussian variance one, its normalized operator bound depends on sqrt(d/n); the note acknowledges this dependence. Retaining the exact realized initial matrices is consistent with imposing such an event. No Gaussian approximation of the trained responses is used.

Minor wording correction: “through the L-Lipschitz activation” should read “through the A-Lipschitz activation,” since L denotes depth.

## 4. Intrinsic-geometry rate: verified

If the support lies in the Lipschitz image of a fixed s-dimensional cube, divide the parameter cube into k^s cells. One image point per cell gives normalized-metric radius at most a constant times k^{-1}. With k=floor(p^{1/s}), k^s<=p and, for p>=1, k is at least p^{1/s}/2. Hence Q_p^{1/2}<=D p^{-1/s}. Finitely many charts can be handled by allocating centers among charts; the chart count and finitely many small-p cases enter D.

No density regularity is used: the bound is pointwise on the support before averaging. The geometry and its Lipschitz constants must be measured in the stated normalized input metric. The note makes D and s explicit data-class parameters.

Combining this with the spectral tail gives beta=1/2+1/s. Replacing a rank-2k estimate by a rank-p estimate uses k=floor(p/2) for p>=2; the p=1 case can be covered by increasing the constant using \(\|G_l\|_F\le B_0D_l\rho\). Thus (13) is valid with an adjusted constant. Its examples and its caveat concerning smooth teachers on high-dimensional input laws are correct.

## 5. Conditional exponent criterion: algebra verified; accounting correction requested

Assuming the unproved common-constant trajectory estimate (15), put a=1/beta and b=1/alpha. The state count stated earlier in the note gives, before any domination argument,

\[
 S_{\rm learned}
 =O\left(Ln\varepsilon^{-(a+b)}+nd+
          L\varepsilon^{-2a}\right).
\]

**Correction requested:** equation (16) drops the last term without yet stating a condition that absorbs it. It can be absorbed whenever p<=nq, because p^2<=npq. In particular, q>=1 and pq=o(n) imply p=o(n), and therefore p^2=o(npq). The simplest repair is to retain +L epsilon^{-2/beta} in (16), then explain why it is dominated in the stated strict-compression regime.

For fixed depth, pq=o(n) ensures that the hidden-factor state is o(n^2), and it also ensures p^2=o(n^2). If total learned state includes nd, one must additionally assume d=o(n). With d fixed this is automatic. With d comparable to n, the first layer alone already occupies order n^2, even if pq is small. The initialization condition n>=d in Section 3 is not enough to make total state strictly subquadratic.

Under the separately assumed n asymptotic to epsilon^{-2}, and with d fixed or otherwise o(n), the strict exponent condition is indeed

\[
 1/\beta+1/\alpha<2.
\]

For alpha=2 this means beta>2/3 and, with beta=1/2+1/s, means s<6. For alpha=1 it means beta>1, equivalently s<2; among the stated integer-dimensional examples this includes the curve case. Equality gives no strict asymptotic saving from this power count. All of these are feasibility calculations conditioned on the missing trajectory theorem and width rate, exactly as the note says.

## 6. Scope of this check

This check verifies a source-rank theorem and the stated conditional arithmetic. It does not verify the separate interaction-basis artifact, prove that a matrix-free adaptive factorization attains the optimal tail, control factor regularity near spectral degeneracies, prove width-uniform deep trajectory stability, or establish all-time or infinite-width convergence. The checked source explicitly identifies these limitations, and they remain open after this check.
