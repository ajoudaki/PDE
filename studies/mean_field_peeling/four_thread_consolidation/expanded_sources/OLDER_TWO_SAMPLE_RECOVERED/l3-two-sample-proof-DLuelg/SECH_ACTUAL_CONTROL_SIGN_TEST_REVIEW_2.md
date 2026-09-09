# Independent adversarial mathematical audit

Audited file: `/tmp/l3-two-sample-proof-DLuelg/SECH_ACTUAL_CONTROL_SIGN_TEST.md`

Exact SHA256 of the audited 744-line file:

`43c2e8422f3973a883e4dcab86509bfe97b91a5a001c8189b198c69642f53e51`

Audit date: 2026-09-06. Line references below refer exclusively to these bytes.

## 1. Scope, verdict, and required versus optional findings

The mathematical input to this audit was the entire specified file, lines
1–744. None of the dependencies named inside it, earlier versions or reviews,
project ledgers, other research documents, or prior research conversation was
consulted. A procedural rigorous-mathematics skill was read; it supplied no
mathematical premise. No experiment, numerical evaluation, candidate edit, or
external theorem was used. The conditioning facts needed for the audit are
derived below directly from the finite Gaussian matrices.

**Verdict: PASS at the document's explicitly conditional claim level.** I found
no blocking mathematical error in the finite autonomous jets, their limiting
physical-time coefficients, the two-matrix static query laws, the simultaneous
empirical-moment argument, the antiparallel endpoint, the positive definite
cubic innovations, or the deduction of (B) from (A). This is not a certification
of an actual-population Taylor theorem or an unconditional sign-change theorem.

The distinction between an unresolved hypothesis and a defect in a conditional
proof is essential here:

| Finding | Classification | Consequence |
|---|---|---|
| No additional missing assumption or incorrect term was found in the static-law and conditional-crossing claims as stated. | No required correction identified. | Those claims survive this audit. |
| Existence of the relevant population flow, identification of its coefficients with this static program on the same probability space, and the quantitative remainder (A) have not been proved. | Required for an **unconditional** population conclusion; already expressly excluded from the document's proved claims. | The population conclusion must remain conditional. Static moment convergence does not supply this bridge. |
| The exact finite-width physical derivative formulas can be written using a general label vector before specializing its limiting Gram to the label eigenmode. | Optional exposition; formulas and justification are supplied in Section 3 below. | Makes the distinction at lines 673–680 and 724 immediately checkable. It does not change (35). |
| The scope of “joint empirical convergence” can be stated as convergence in probability for every fixed finite collection of the required tests, with arbitrary fixed moment order. | Optional precision; this is the scope supported by lines 551–628. | No almost-sure convergence, uniformity over all tests, inverse-Gram integrability, or trajectory convergence is needed or established. |

There is no recommendation here to weaken the covariance statements or to
remove the endpoint. In particular, subtracting an additional regression
covariance from (29), (30), or (31) would generally make the stated laws wrong.
Their different projections are justified in Section 4.

## 2. Setup, activation, and initial nondegeneracy

The audit uses exactly the model and metric stated at lines 90–179. Write
\(\langle u,v\rangle_n=u^Tv/n\). All population sample vectors have two
components; rows at different hidden layers belong to different neuron
populations. No cross-layer matching of neuron indices is used.

Set \(g(z)=\phi(z)-1\). Direct differentiation gives

\[
 \phi'(z)=\frac{\cosh z}{10(1+\sinh^2z)}
          =\frac1{10}\operatorname{sech}z,
 \qquad p'(z)=-\frac1{10}\operatorname{sech}z\tanh z.
\]

Thus \(g\) is odd, bounded and strictly increasing; \(p\) is even and
strictly positive at every finite argument. It is nonconstant on every open
interval, although its derivative vanishes at zero. Repeated differentiation
produces polynomials in the bounded functions \(\operatorname{sech}\) and
\(\tanh\), so the bounded-derivative assertion at lines 119–121 is valid.

For \(-1<\rho<1\), a continuous homogeneous relation
\(v_1\phi(Z_{1,1})+v_2\phi(Z_{1,2})=0\) almost surely would hold everywhere:
otherwise continuity and the positive Gaussian density give an open set on
which it fails with positive probability. Varying the first argument forces
\(v_1=0\), and varying the second forces \(v_2=0\). Consequently \(K_1\succ0\).

At \(\rho=-1\), write \(Z_1=(X,-X)\). The same relation becomes

\[
 (v_1+v_2)+(v_1-v_2)g(X)=0.
\]

Since \(g\) is nonconstant, both coefficients vanish. Hence \(K_1\succ0\)
also at this endpoint. The next Gaussian pair is therefore nondegenerate,
and the preceding positive-density argument proves \(K_2\succ0\) and
\(K_3\succ0\). The excluded endpoint \(\rho=1\) would not have this property.

Sample exchangeability is preserved by each initial Gaussian covariance and
the componentwise activation. Thus each \(K_j\) has equal diagonal entries.
For \(y=(1,\sigma)\),

\[
 K_3y=\kappa y,
 \qquad
 \kappa=(K_3)_{11}+\sigma(K_3)_{12}>0.
\]

This verifies the initial eigenmode assertion without assuming that the
trained flow preserves that eigenmode.

## 3. Finite jets and physical-time coefficients

### 3.1 Metric normalization

The Euclidean derivative of \(f_a\) with respect to a hidden matrix is
\(\delta_a h_a^T/n\), with the corresponding input vector at the first layer.
The Euclidean readout derivative is \(h_{3,a}/n\). Multiplication by the
inverse metric factors \(n/d,1,1,n\), and by the loss derivative \(2r_a\),
gives precisely (2a). At the first layer,
\(x_b^Tx_a/d=C_{ab}\), so the pair equation uses \(C\), never \(C^{-1}\).
This remains valid at \(\rho=-1\).

Taking the differential of \(f_a\) against these velocities gives (2b).
In particular, both empirical pairings in the middle-layer kernel blocks
carry their own factor \(1/n\). The factor \(-2\) in the physical residual
equation is correct. Applying the same metric to ascent of
\(J=c\sum_b y_bf_b\), \(c=1/2\), gives (3), with
\(u\otimes v=uv^T/n\). No normalization discrepancy was found.

### 3.2 Autonomous linear and hidden second derivatives

At zero readout all backward fields vanish. Hence all hidden first
derivatives vanish, while \(w_s=V\). Differentiating the backward fields once
gives

\[
 (\delta_3)_s=Vp(Z_3)=U,\qquad
 (q_2)_s=B^TU=R^{(2)},\qquad
 (\delta_2)_s=P_2R^{(2)}=D,\qquad
 (q_1)_s=A^TD=R^{(1)}.
\]

The first-layer equation then gives
\(X_1=cCY P_1R^{(1)}\), hence
\(F_1=cP_1CY P_1R^{(1)}\). Also

\[
 (W^{(2)})_{ss}=c\sum_b y_bD_b\otimes h_{1,b},
 \qquad
 (W^{(3)})_{ss}=c\sum_b y_bU_b\otimes h_{2,b}.
\]

Differentiating \(z_2=W^{(2)}h_1\) and \(z_3=W^{(3)}h_2\), with their
vanishing first derivatives, now yields exactly

\[
 X_2=cK_1YD+AF_1,\quad F_2=P_2X_2,\quad
 X_3=cK_2YU+BF_2.
\]

At finite width these are empirical Grams, as the document specifies.

### 3.3 Cubic derivatives and the learned-matrix terms

Since \(w_s=c\sum_b y_bh_{3,b}\),
\(w_{sss}=c\,y^TP_3X_3=V_2\). The product rule for
\(\delta_3=wp(z_3)\) gives

\[
 (\delta_3)_{sss}
 =p(Z_3)V_2+3V\operatorname{diag}(p'(Z_3))X_3=F_{3,*}.
\]

The coefficient 3 comes from choosing which one of the three derivatives
hits \(w\), while the other two hit the hidden preactivation. Terms involving
\(w(0)\) or \((z_3)_s(0)\) vanish. For the matrix product,

\[
 (q_2)_{sss}=B^TF_{3,*}+3(W^{(3)})_{ss}^TU.
\]

Its second term at sample \(a\) is
\(3c\sum_b y_bH_{2,b}\langle U_b,U_a\rangle_n\), namely
\(3cS_3YH_2\) in sample-column notation. This verifies both its order and
its factor in (7).

Likewise,

\[
 (\delta_2)_{sss}
 =P_2T^{(2)}
   +3\operatorname{diag}(p'(Z_2)\odot X_2)R^{(2)}=F_{2,*},
\]

and
\((q_1)_{sss}=A^TF_{2,*}+3cS_2YH_1\). Thus (6)–(8) are correct,
including both contributions from the evolving matrices. All autonomous
query second derivatives vanish: \(w_{ss}(0)=0\), hidden first velocities
are zero, and every remaining term in the second product rule contains one
of those vanishing factors. Consequently (9) has the correct factorial.

### 3.4 Physical clock and the finite-width qualification

At zero readout the hidden kernel blocks and their first derivatives vanish.
The derivative of the readout block vanishes because hidden velocities are
zero. If \(K_{3,n}\) is the finite initial readout Gram, the exact finite
residual identities are therefore

\[
 r(0)=-y,\qquad r'(0)=2K_{3,n}y,\qquad
 r''(0)=-4K_{3,n}^2y.
\]

Only after taking the static population limit do these become (34).

Here is an explicit verification that this distinction does not conceal a
physical coefficient error. Let \(R_n^{(\ell)}(b)\) denote the initial linear
query in (4) with \(V=c\,b^TH_3\); it is linear in \(b\). Let
\(T_n^{(\ell)}(y)\) be the cubic autonomous query already computed. Direct
physical differentiation gives the exact finite identities

\[
 \begin{aligned}
 q_{\ell,n}'(0)&=4R_n^{(\ell)}(y),\\
 q_{\ell,n}''(0)&=-8R_n^{(\ell)}(K_{3,n}y),\\
 q_{\ell,n}'''(0)&=16R_n^{(\ell)}(K_{3,n}^2y)
                       +64T_n^{(\ell)}(y).
 \end{aligned}
\]

To check the last formula explicitly, physical hidden second derivatives
are 16 times their autonomous counterparts: differentiating a hidden update
once leaves only \(-2r(0)\delta'(0)\), and
\(\delta'(0)\) is four times its autonomous value. The physical readout
third derivative is

\[
 w'''(0)=8(K_{3,n}^2y)^TH_3+64V_2.
\]

Combining it with the hidden second derivatives in the product rules above
gives the displayed formula for either query. Residual first derivatives do
not create an extra cubic term: the putative terms multiply zero initial
hidden velocities or backward fields.

The finite Gaussian estimates below also give moment-tight linear-query
coefficients for the two deterministic vectors \(b=e_1,e_2\). Since the map
\(b\mapsto R_n^{(\ell)}(b)\) is linear, convergence
\(K_{3,n}\to K_3\) therefore permits replacing its random coefficients by
their limits in every fixed empirical moment norm. This verifies the
limiting specialization of these finite formulas, not just formal scalar
algebra.

Equivalently, the physical field through the required order has multiplier
\(4-8\kappa t+8\kappa^2t^2\) against (3). Its integrated clock is

\[
 s(t)=4t-4\kappa t^2+\frac83\kappa^2t^3.
\]

Since \(s(t)^3/6=(32/3)t^3+O(t^4)\), (35) is correct:

\[
 q_\ell'(0)=4R^{(\ell)},\quad
 q_\ell''(0)=-8\kappa R^{(\ell)},\quad
 q_\ell'''(0)=16\kappa^2R^{(\ell)}+64T^{(\ell)}.
\]

These are static limiting jet coefficients. No argument in this section
identifies them with derivatives of an existing limiting trajectory.

## 4. Gaussian conditioning, every projection, and both matrices

### 4.1 Finite conditioning identity

Consider the Euclidean matrix space with Frobenius inner product. A matrix
with iid \(N(0,1/n)\) entries has characteristic function
\(\exp(-\|Q\|_F^2/(2n))\) when tested against \(Q\). Decomposition into
orthogonal subspaces makes this characteristic function factor, proving
independence of the corresponding Gaussian projections.

With full-rank column arrays \(H,U\), the matrices satisfying both homogeneous
constraints \(EH=0\), \(E^TU=0\) are exactly

\[
 E=(I-\Pi_U)E(I-\Pi_H).
\]

Assuming compatibility \(H^TR=Z^TU\), define

\[
 W_0=Z(H^TH)^{-1}H^T
       +U(U^TU)^{-1}R^T(I-\Pi_H).
\]

Multiplication verifies \(W_0H=Z\) and \(W_0^TU=R\). Its first summand
has right support in \(\operatorname{span}H\); its second has left support
in \(\operatorname{span}U\). Both are orthogonal to the homogeneous
constraint space. Therefore conditioning the isotropic Gaussian on the two
constraints leaves exactly the independent residual
\((I-\Pi_U)\widetilde W(I-\Pi_H)\). This proves (28), including its mean,
without importing a matrix-conditioning theorem.

With only \(WH=Z\) exposed, transposing the residual against \(U\) gives

\[
 W^TU=H(H^TH)^{-1}Z^TU+(I-\Pi_H)b,
 \qquad b_i\mid\text{history}\ \text{iid }N(0,U^TU/n).
\]

This proves (29). The covariance is the **uncentered** second moment of
\(U\). Conditioning on \(WH\) projects the matrix on the right; it does
not subtract a regression of \(U\) on \(Z\) from this covariance.

### 4.2 The Gaussian integration by parts used for the means

For a nondegenerate centered Gaussian \(Z\) of covariance \(K\), its density
\(\gamma\) satisfies
\(\partial_b\gamma(z)=-(K^{-1}z)_b\gamma(z)\). Integration of
\(\partial_b(F_a\gamma)\) gives

\[
 \mathbb E[FZ^T]=\mathbb E[\nabla F]K.
\]

The boundary terms vanish by Gaussian decay for the polynomial-growth
functions and derivatives used here; one may integrate over expanding
rectangles to see this directly. Additional independent Gaussian sources
are first held fixed and then integrated, with the same moment bounds.
This is the full identity needed for the two initial means.

It yields
\(\mathbb E[UZ_3^T]K_2^{-1}=\Gamma_3\). Differentiating
\(U_a=Vp(Z_{3,a})\) gives

\[
 (\Gamma_3)_{ab}=c\,y_b(G_3)_{ab}
             +\delta_{ab}\mathbb E[Vp'(Z_{3,a})].
\]

For the second transpose, with \(\zeta_2\) held fixed,

\[
 \partial_bD_a
 =\delta_{ab}p'(Z_{2,a})R^{(2)}_a
   +p(Z_{2,a})(\Gamma_3)_{ab}p(Z_{2,b}).
\]

Thus the means and covariances in (10) and (11) have the stated orientation
and values. The integrations by parts use the nondegenerate roots \(Z_3\)
and \(Z_2\); they never require inverting the possibly singular covariance
of \(Z_1\).

### 4.3 New forward inputs

For an adaptive input array \(X\), multiplication of (28) gives, in finite
array notation,

\[
 WX=Z(H^TH)^{-1}H^TX
 +U(U^TU)^{-1}R^T(I-\Pi_H)X
 +(I-\Pi_U)\widetilde W(I-\Pi_H)X.
\]

The first coefficient converges to the transpose of
\(A_X=\mathbb E[XH^T]K_H^{-1}\). The exact residual
\((I-\Pi_H)R\) in the second coefficient has local limit \(\zeta\), so
the second coefficient gives \(B_X=\mathbb E[X\zeta^T]S_U^{-1}\).

Before the left projection, the new Gaussian array has row covariance
\(X^T(I-\Pi_H)X/n\), whose limit is

\[
 \mathbb E[(X-A_XH)(X-A_XH)^T].
\]

The left projection is a fixed-rank row-array error, handled quantitatively
in Section 5. It does not remove an order-one part of that local covariance.
This verifies every term in (30).

For the first new forward input,

\[
 \mathbb E[F_1\zeta_1^T]S_2^{-1}
 =c\,\mathbb E[P_1CY P_1]
 =c(C\odot G_1)Y.
\]

Adding the direct matrix-update term \(cK_1YD\) gives (13). In particular,
the lower matrix's reuse contribution is present, with the correct sign
and sample-matrix order. Since
\(C\odot G_1=\mathbb E[P_1CP_1]\succeq0\), \(L_1\succ0\).

Conditional on \(Z_2\), the coefficient of \(\zeta_2\) in \(F_2\) is
\(cP_2L_1YP_2\). Independence of \(\xi_2\) from \((Z_2,\zeta_2)\) gives

\[
 \mathbb E[F_2\zeta_2^T]S_3^{-1}
 =c\,\mathbb E[P_2L_1YP_2]
 =c(L_1\odot G_2)Y.
\]

Adding \(cK_2YU\) yields (16), with exactly the residual covariance
\(\Omega_2\) in (15). There is no missing mean or centered-covariance
correction in either forward query.

### 4.4 Last reverse inputs

After the enlarged forward query \(W\mathcal H=\mathcal Z\), transpose
(28) with \(H\) replaced by \(\mathcal H\). At finite width write
\(D_{F,n}=F^TU(U^TU)^{-1}\) and
\(F_{\perp,n}=F-UD_{F,n}^T\). The two deterministic terms combine exactly as

\[
 W^TF
 =R D_{F,n}^T
 +\mathcal H(\mathcal H^T\mathcal H)^{-1}
       \mathcal Z^TF_{\perp,n}
 +\text{projected fresh Gaussian array}.
\]

Indeed, the subtraction in the second term uses
\(\mathcal H^TR=\mathcal Z^TU\). Before its right-space projection,
the fresh transpose array has row covariance
\(F^T(I-\Pi_U)F/n=F_{\perp,n}^TF_{\perp,n}/n\). This proves (31).

The three operations must be distinguished: regress the reverse input on
the old reverse input \(U\), retain the resulting multiple of \(R\), and
regress the remaining input against the **actual enlarged forward
output** \(\mathcal Z\). The document does all three.

For \(B\), that output is
\(\mathcal Z_3=\binom{Z_3}{X_3-cK_2YU}\), the stacked sample-column
notation for \(BH_2\) and \(BF_2\). Thus (22)
and (23) have exactly the appropriate response and projection terms.
For \(A\), the output is similarly \(Z_2\) together with
\(J_1(X_2-cK_1YD)\). This verifies (26) and (27), subject to the rank checks
in Section 6. The explicit learned-matrix terms from (7) and (8) must then
be added, and are added in the document.

### 4.5 Adaptive exposure of two independent matrices

The admissibility question is substantive: the conditioning formula would
not generally apply if a new input inspected the unexposed residual of the
matrix being queried. Here a
valid common history is

\[
 z_1;\quad AH_1;\quad BH_2;\quad B^TU;\quad A^TD;
 \quad AF_1;\quad BF_2;\quad B^TF_{3,*};\quad A^TF_{2,*}.
\]

At each step the next input is a function of this history before its next
matrix product is exposed. In particular:

- \(D=P_2R^{(2)}\) is known before \(A^TD\).
- \(F_1\) is known after \(A^TD\), before \(AF_1\).
- \(F_2\) is known after \(AF_1\), before \(BF_2\).
- \(F_{3,*}\) is known after \(BF_2\), before its reverse query.
- \(F_{2,*}\) is known after that reverse query, before the final \(A\)
  reverse query.

Conditional on any realized preceding history, each new observation is a
linear constraint on the residual of just one matrix with now-fixed
coefficients. Initially the two matrix laws factor. Inductively, imposing
such a constraint updates only that matrix's conditional Gaussian factor;
the other residual remains independent. This proves that the two residual
laws continue to factor, while their deterministic means and projectors
can depend on the common history. It also justifies conditioning on the
other matrix when useful. Thus the stated query order passes the adaptive
measurability check and never replaces a reused matrix by an independent one.

## 5. Simultaneous empirical polynomial-moment convergence

The estimates at lines 551–628 suffice for the claimed fixed finite program.
The following expands the proof obligations and explains why covariance
convergence alone is not the justification being used.

For any row array \(v\), define
\(\|v\|_{n,q}=(n^{-1}\sum_i\|v_i\|^q)^{1/q}\). The induction maintains
convergence of empirical tests of each population's entire previously
exposed row tuple, and tightness of \(\|v\|_{n,q}\) for every fixed finite
\(q\). The necessary tests are smooth functions with polynomial bounds on
their values and the derivatives used in perturbation estimates. All
coordinate products, Gram entries, response entries, and maps in this
program belong to this class because the activation derivatives are bounded.

### 5.1 Removing projections in every fixed moment norm

Condition on an exposed full-rank \(n\)-by-\(k\) basis \(L\). If \(b\)
has fresh independent Gaussian rows with covariance \(S\), then

\[
 \alpha=(L^TL)^{-1}L^Tb,
 \qquad
 \operatorname{Cov}(\operatorname{vec}\alpha)
       =S\otimes(L^TL)^{-1}
\]

up to vectorization convention. When
\(\lambda_{\min}(L^TL/n)\ge\delta\) and \(\|S\|\le M\), represent this
fixed-dimensional Gaussian as a linear image of a standard Gaussian vector.
Its covariance norm is at most \(M/(n\delta)\), so

\[
 \mathbb E[\|\alpha\|^{2q}\mid\text{history}]\le C n^{-q}.
\]

Also
\(\|L\alpha\|_{n,2q}^{2q}\le\|\alpha\|^{2q}\|L\|_{n,2q}^{2q}\).
Tightness of the already exposed basis moments therefore gives
\(\|\Pi_Lb\|_{n,2q}\to0\) in probability on these events. The limiting
Grams have positive eigenvalues, so these bounded-inverse and bounded-moment
events can be chosen to have probability arbitrarily close to one.
No bound on the expectation of an inverse Gram is required.

This proves the stronger estimate (32a), not just the normalized quadratic
estimate (32). It is enough to control products of the reverse fields and
all finite polynomial moments used later.

### 5.2 Conditional averaging and random coefficients

For a fresh representation \(S_n^{1/2}g_i\), the \(g_i\)'s are independent
conditional on the old arrays. Polynomial bounds on a fixed test \(\psi\)
give

\[
 \begin{aligned}
 \operatorname{Var}\left(
   \frac1n\sum_i\psi(v_i,S_n^{1/2}g_i)
   \,\middle|\,\text{history}\right)
 &\le\frac1{n^2}\sum_i
   \mathbb E[|\psi(v_i,S_n^{1/2}g_i)|^2\mid\text{history}]\\
 &\le\frac Cn\left(1+\frac1n\sum_i\|v_i\|^{2m}\right).
 \end{aligned}
\]

This is (32b). The right side tends to zero in probability after the
stated localization. Conditional Chebyshev bounds, with probabilities
capped by one outside the localized event, then show convergence to the
conditional mean. At fixed limiting coefficients the conditional mean is
an empirical average of the Gaussian-integrated test of \(v_i\), to which
the preceding induction applies.

The covariance matrices and regression matrices at every step are finite
collections of such empirical moments. Their limits are deterministic.
Matrix inversion is continuous at a positive definite matrix: the identity
\(A_n^{-1}-A^{-1}=A_n^{-1}(A-A_n)A^{-1}\), on a lower-eigenvalue event,
proves this directly. Positive semidefinite square roots are continuous
even when the limit is singular: bounded roots have convergent
subsequences, every limit is positive semidefinite and squares to the
limiting matrix, and orthogonal diagonalization gives uniqueness of that
positive semidefinite root. These observations justify the coefficient and
covariance replacements used in the document, including singular
\(\Omega_1\) at the endpoint.

### 5.3 Earlier errors, products, and simultaneous statements

For every nonlinear row map actually used here, bounded activation
derivatives and finite-degree products imply

\[
 \|\Phi(v)-\Phi(\widetilde v)\|
 \le C(1+\|v\|^m+\|\widetilde v\|^m)\|v-\widetilde v\|.
\]

Applying Hölder's inequality in the empirical measure bounds the error in
any fixed moment norm by a higher moment norm of
\(v-\widetilde v\) times tight higher moments of the old tuples. Thus the
projection errors just proved remain negligible through (6) and (8), even
though those maps include products of random fields. Each matrix product
is handled by its conditional formula above; one need not assert that an
arbitrary small input error stays small after multiplication by an
uncontrolled matrix.

The initial iid Gaussian rows start the induction by the same variance
bound. Subsequent initial forward covariances are empirical feature Grams,
so the random-coefficient argument starts the next population. Applying
these steps in the finite common exposure order proves convergence of all
needed mixed moments in each layer's entire tuple. A union bound then gives
joint convergence for any fixed finite family of tests and stages.

If “all polynomial moments simultaneously” is expressed using a countable
enumeration \(M_{n,j}\) of monomials, this also gives convergence in
probability in the metric
\(\sum_{j\ge1}2^{-j}\min(1,|M_{n,j}-M_j|)\): truncate the uniformly
bounded tail and use the finite-family result for the rest. It does not
assert a uniform error bound across unbounded degrees.

Accordingly, the simultaneous empirical statement passes. It uses no
almost-sure convergence, exchange of width and time limits, or unproved
inverse-Gram uniform integrability. The stopping point stated at lines
632–634 is correct.

## 6. Endpoint and positive definite innovations

### 6.1 Initial reverse covariances

For \(S_3\), suppose \(v^TU=0\) almost surely. Since \(Z_3\) has positive
density and the functions are continuous, on any open rectangle where
\(V\ne0\) one has
\(v_1p(z_1)+v_2p(z_2)=0\). Such a rectangle exists for either label mode.
Varying one argument and using nonconstancy of \(p\) forces both
coefficients to vanish. Thus \(S_3\succ0\).

Conditional on \(Z_2\), \(D\) has covariance \(P_2S_3P_2\succ0\), so its
uncentered second moment \(S_2\) is positive definite as well. Positivity
here does not depend on an assertion that the conditional mean vanishes.

### 6.2 The first enlarged forward Gram, including \(\rho=-1\)

The Gaussian coefficient of \(\zeta_1\) in \(F_1\) is
\(B_1(Z_1)=cP_1CY P_1\). In the interior, every factor is invertible.
Therefore \(\Omega_1\), the second moment after subtracting a deterministic
function of \(Z_1\), contains a positive definite conditional covariance.

At \(\rho=-1\), equal gates give
\(B_1=c p(X)^2CY\) and \(F_{1,2}=-F_{1,1}\) exactly, including at finite
width. With \(J_1=(1,-1)/\sqrt2\),

\[
 J_1B_1=2c p(X)^2J_1Y,
\]

which is a nonzero row vector. Its covariance against \(S_2\succ0\) is
strictly positive at every finite \(X\). Hence
\(J_1\Omega_1J_1^T>0\). The removed component is an exact algebraic
redundancy, not a small random eigenvalue.

For completeness, the Schur-complement assertion can be checked as a
quadratic minimization: for coefficients \(u,v\), subtracting the best
linear prediction of \(v^TJ_1F_1\) from the span of \(H_1\) leaves
second moment \(v^TJ_1\Omega_1J_1^Tv\), while the remaining feature
quadratic form is governed by \(K_1\succ0\). Thus
\(\mathcal K_1\succ0\). No pseudoinverse or inverse of \(C\) is needed.

### 6.3 The second enlarged forward Gram

Conditional on \(Z_2\),
\(F_2\) contains the independent term
\(N(Z_2)\zeta_2\), where \(N=cP_2L_1YP_2\). Since \(L_1\succ0\) and
the diagonal factors are invertible, \(N\) is invertible everywhere.
Subtracting \(A_2H_2\) cannot remove that conditional covariance, so

\[
 \Omega_2\succeq
 \mathbb E[N(Z_2)S_3N(Z_2)^T]\succ0.
\]

The same quadratic decomposition over \(K_2\) proves
\(\mathcal K_2\succ0\). Thus every Gram inverted in the final reverse
queries has the claimed nonsingular limit. This also completes the rank
justification needed for the empirical induction.

### 6.4 Top cubic innovation

The matrix in (19) follows from the already checked formula for
\(F_{3,*}\). Given \(Z_3\), the residual after projection onto \(U\)
contains \(M(Z_3)\xi_3\). Consequently

\[
 \Lambda_3\succeq\mathbb E[M(Z_3)\Omega_2M(Z_3)^T].
\]

At \(z=(0,1)\), the vanishing of \(p'(0)\) cancels the two rank-one
determinant terms, leaving exactly

\[
 \det M(0,1)=3c\,y_1V(0,1)p(0)^2p'(1).
\]

Here \(p'(1)<0\). For equal labels, \(V(0,1)>0\); for opposite labels,
\(V(0,1)=(1-\phi(1))/2<0\). The determinant is nonzero in both cases.
It remains nonzero on an open neighborhood, to which \(Z_3\) assigns
positive probability. For every nonzero \(v\), on that neighborhood
\((M^Tv)^T\Omega_2(M^Tv)>0\). Its expectation is therefore positive.
This proves the full matrix inequality \(\Lambda_3\succ0\), not just
positive individual variances.

### 6.5 Lower cubic innovation

After the top reverse query, \(\eta_2\) is independent of the preceding
layer-two tuple. In \(F_{2,*}\) it appears as \(P_2\eta_2\). Both \(D\)
and the term subtracted in \(F_{2,\perp}=F_{2,*}-D_2D\) depend only on
that preceding tuple. The independent noise therefore survives, giving

\[
 \Lambda_2\succeq\mathbb E[P_2\Lambda_3P_2]\succ0.
\]

The final strict inequality follows since \(P_2v\ne0\) for every
nonzero \(v\) at every finite root. This proves the lower innovation's
positive definiteness for both label modes and throughout the stated
range of \(\rho\).

## 7. Conditional Gaussian law and density lower bound

For layer two, fix \((Z_2,\xi_2)\). Then \(R^{(2)}\) is a deterministic
mean plus \(\zeta_2\), and \(F_2\) is affine in \(\zeta_2\). Equation
(23) consequently has the form

\[
 \binom{R^{(2)}}{T^{(2)}}
 =m+\begin{pmatrix}I&0\\L&I\end{pmatrix}
       \binom{\zeta_2}{\eta_2}.
\]

Here the independent source covariances are \(S_3\succ0\) and
\(\Lambda_3\succ0\), and the displayed triangular matrix is invertible
for any \(L\). For layer one, conditional on \(Z_1\), the identical
argument uses the affine dependence of \(F_1\) on \(\zeta_1\), with source
covariances \(S_2\succ0\) and \(\Lambda_2\succ0\). This verifies exactly
the conditioning stated at lines 457–462. It does not claim joint
independence of noises belonging to different neuron populations.

Choose a compact subset of the conditioning variables' Gaussian support
having positive probability. Conditional means and covariance matrices
are continuous on it. Their covariance eigenvalues are bounded between
some \(m_0>0\) and \(M_0<\infty\). On any fixed compact box of target
coordinates, \(\|x-\mu\|\le D_0\), so the Gaussian density in dimension
\(d\) is bounded below by

\[
 (2\pi)^{-d/2}M_0^{-d/2}
     \exp\!\left(-\frac{D_0^2}{2m_0}\right)>0.
\]

Integrating over that conditioning set gives a strictly positive density
lower bound. The same argument applies directly to each two-dimensional
coordinate marginal \((R_a^{(\ell)},T_a^{(\ell)})\). It applies when the
conditioning root or \(\xi_2\) is singular because the compact set is
taken in its support; the **conditional target covariance** remains
positive definite. In fact it gives the lower bound on any fixed compact
target box, sufficient for the full interval \(1\le T\le9/8\) used next.

The statement about a zero slope is therefore a property of the regular
conditional initial law, not a claim that the event \(R=0\) itself has
positive probability. The crossing proof appropriately avoids conditioning
on that null event.

## 8. Conditional crossing and the undisclosed-bridge check

Fix a layer and sample. The density lower bound on a compact box containing
\([-\varepsilon,0]\times[1,9/8]\) gives

\[
 \mathbb P\{-2t^2\le R\le-t^2,\ 1\le T\le9/8\}
 \ge c_0t^2
\]

for sufficiently small \(t>0\): its horizontal length is \(t^2\) and
its vertical length is \(1/8\).

The physical linear coefficient
\(a(u)=4u-4\kappa u^2+(8/3)\kappa^2u^3\) satisfies
\(15u/4\le a(u)\le17u/4\) on a sufficiently small deterministic interval,
because \(a(u)/u\to4\). On the event above, the extremal choices of
\(R\) and \(T\), with their correct signs, give

\[
 \begin{aligned}
 Q(t)&\ge-2t^2\frac{17t}{4}+\frac{32}{3}t^3
                =\frac{13}{6}t^3,\\
 Q(t/2)&\le-t^2\frac{15t}{8}
          +\frac{32}{3}\frac{t^3}{8}\frac98
                =-\frac38t^3.
 \end{aligned}
\]

All numerical factors in (36)–(37) check.

Now, and only now, assume (A) for an actual population control coupled to
these coefficients. Write \(e(u)=q(u)-Q(u)\). From
\(\|e(u)\|_{p_*}\le Cu^4\), the elementary bound
\(\mathbb P(|e|>b)b^{p_*}\le\mathbb E|e|^{p_*}\) gives

\[
 \begin{aligned}
 \mathbb P\bigl(|e(t)|>t^3/8\text{ or }|e(t/2)|>t^3/8\bigr)
 &\le\bigl((8C)^{p_*}+(C/2)^{p_*}\bigr)t^{p_*}\\
 &=o(t^2),\qquad p_*>2.
 \end{aligned}
\]

No independence from the coefficient event is used. Subtracting this
exceptional probability leaves at least \((c_0/2)t^2\) probability for
small enough \(t\). On the remaining event,
\(q(t)>0\) and \(q(t/2)\le-(1/4)t^3<0\). This proves (B) with the
claimed quantifiers. Almost-sure path continuity then gives an intervening
zero and opposite-sign intervals around the two selected times.

For any sufficiently short deterministic interval beginning at zero,
selecting one such \(t\) inside it yields a positive-population-measure
set of crossing paths. This contradicts an assertion that almost every
path keeps one sign throughout that interval. It does not prove that a
single path crosses infinitely often, simultaneous crossing at both
layers, or a probability bound uniform as \(\rho\to1\). The document
does not claim these stronger conclusions.

Multiplication by a continuous residual that remains nonzero near its
initial value \(-y_a\), or by a nonzero constant label, preserves the
existence of a sign change, possibly reversing its direction. This last
observation uses residual continuity; it is not needed to prove (B).

The bridge remains unproved. Neither the finite derivative
calculation nor the empirical static convergence identifies population
time derivatives. Even identification of three derivatives without the
stated quantitative control would not justify comparing an exceptional
probability against a shrinking event of mass \(t^2\). A path into
\(L^{p_*}\) with the identified derivatives and bounded fourth derivative
would imply (A), because its remainder is

\[
 \frac16\int_0^t(t-u)^3q^{(4)}(u)\,du,
 \qquad
 \|\text{remainder}\|_{p_*}
 \le\frac{t^4}{24}\sup_{0\le u\le t}\|q^{(4)}(u)\|_{p_*}.
\]

But such a population regularity and identification theorem has not been
established here. The source explicitly acknowledges this at lines 52–59,
632–634, 678–680, and 728–739, and this audit supplies no substitute for it.

## 9. Final disposition

All requested static and conditional checks have been completed against the
specified hash. No required repair to the stated conditional result was
identified. The optional clarifications above concern presentation and the
scope of convergence, not a changed covariance, missing term, or excluded
endpoint.

The defensible result is a nondegenerate limiting initial cubic law at both
layers, together with the positive-probability crossing implication **if (A)
and the stipulated population continuity hold**. The actual-population
identification and remainder theorem remains an essential open obligation.
No unconditional population sign-change theorem, sign invariant, or
refutation of the broader theorem has been established by this audit.
