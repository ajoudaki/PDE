# Independent isolated adversarial audit

Date: 2026-09-06.

Candidate: `/tmp/l3-two-sample-proof-DLuelg/SECH_ACTUAL_CONTROL_SIGN_TEST.md`.

Candidate SHA256:

`0687a11f279d5b6c2436f127fc48f7e7b73bfd51a6c0fa73c7814aaf242da336`

All 657 candidate lines were read. Line references below refer to those bytes.
The candidate was the sole mathematical input. No project history, ledger,
historical dependency, other proof, other review, or external mathematical
source was inspected. The rigorous-math skill supplied procedural instructions
only. No experiments were performed, and the candidate was not edited.

## 1. Verdict and exact scope

**The static initialization law and the implication (A) => (B) withstand this
audit.** I find no incorrect coefficient in the finite autonomous Taylor
calculation (4)--(9), no missing repeated-matrix regression or covariance term
in (10)--(31), and no degeneracy overlooked at rho = -1. The joint empirical
moment argument in Section 5 is compressed, but it can be completed by the
elementary conditional estimates given below; no specialized Gaussian-program
theorem is needed. The density and crossing arguments are valid.

**The candidate is not fully self-contained as a derivation of the physical
gradient-flow normalization.** Its raw physical gradient-flow equation is
never stated: lines 566--570 appeal to the unread contract. The asserted
factors in (34)--(35) are consistent with the explicit raw equation identified
in Section 8 of this report, but (3), by itself, does not select that physical
time scale. This requires the local correction R1 below. It does not defeat
the implication (A) => (B), since (A) explicitly stipulates the physical-time
polynomial to which that implication applies.

This audit does **not** establish existence of an actual population flow,
interchange of differentiation and width limits, identification of population
derivatives, or the population remainder (A). These remain unproved premises,
exactly as stipulated by the candidate and the audit request. It does not
establish an unconditional population sign-change theorem or assess any
historical theorem or prescribed-control argument.

## 2. Required correction

### R1. State the raw physical flow within the candidate

Relevant lines: 142--159, 550--593, especially 566--570; also the normalization
status claimed at line 637.

Equation (3) defines ascent of J in the auxiliary time s. A factor 4 between
this field and physical time cannot be derived from that definition alone.
Multiplying a physical loss, or its gradient flow, by a positive constant
changes that factor while leaving the static initialization and (3) intact.
The phrase “raw GF formula in the contract” supplies no auditable equation
under the stated isolation restriction.

To make the normalization derivation self-contained, state r = f - y and the
raw physical equations, including their factor -2 and the same normalized
outer-product convention as (3). Equivalently, state

\[
 \dot\theta=-2\sum_b r_b g_b(\theta),\qquad
 (f_a)'=-2\sum_b K_{ab}r_b,
\]

where g_b is the metric gradient of f_b with the metrics that produce (3).
The componentwise version and the resulting calculation are given in
Section 8 below. If a different physical convention is intended, its factors
must instead be propagated through (34), (35), and (A).

Severity: a missing normalization premise/definition for the asserted
self-contained physical-jet derivation, not an error in the proved static
Gaussian law or in the conditional probability argument. No further
required correction to those latter arguments was found.

## 3. Activation, feature Grams, and finite Taylor algebra

### 3.1 Activation and the endpoint

Put g = phi - 1. Direct differentiation gives

\[
 \phi'(z)=\tfrac1{10}\frac{\cosh z}{1+\sinh^2 z}
 =\tfrac1{10}\operatorname{sech}z=p(z),\qquad
 p'(z)=-\tfrac1{10}\operatorname{sech}z\tanh z.
\]

Thus g is odd, bounded, and strictly increasing; p is positive and even and
is not constant on any interval. All fixed derivatives used in the candidate
are bounded, since subsequent differentiations preserve polynomials in sech
and tanh. In particular, the differentiations and polynomial moment bounds
below do not encounter a singular activation derivative.

For -1 < rho < 1, a homogeneous relation
v_1 phi(Z_{1,1}) + v_2 phi(Z_{1,2}) = 0 almost surely extends, by continuity
and the positive Gaussian density, to every point of R^2. Varying the first
coordinate gives v_1 = 0, and then v_2 = 0. Hence K_1 is positive definite.

At rho = -1, write Z_1 = (G,-G). The features are (1+g(G),1-g(G)). The two
functions 1 and g(G) are linearly independent. More explicitly, if
m = E[g(G)^2] > 0, then

\[
 K_1=\begin{pmatrix}1+m&1-m\\1-m&1+m\end{pmatrix}
\]

has eigenvalues 2 and 2m. The same full-density argument, now applied to
Z_2 with covariance K_1 and then Z_3 with covariance K_2, proves positive
definiteness of K_2 and K_3. No inverse of the singular input covariance C
is taken. This verifies lines 113--120 and the Gram assertion in Section 6.

### 3.2 Differentiating the auxiliary field

All assertions in this subsection are finite-width identities at w = 0,
conditional on the explicitly supplied field (3). The Grams and second
moments in these identities must be empirical ones, as the candidate says.

The normalized outer product is uv^T/n. Therefore (3) really does include
the necessary 1/n in both hidden matrix updates. At initialization,

\[
 w_s=V,\quad (\delta_3)_s=U,\quad(q_2)_s=B^TU=R^{(2)},
 \quad(\delta_2)_s=D,\quad(q_1)_s=A^TD=R^{(1)}.
\]

The hidden velocities vanish because their backward fields vanish. The
second derivatives of the two trained matrices are

\[
 (W^{(3)})_{ss}=c\sum_b y_b U_b\otimes h_{2,b},\qquad
 (W^{(2)})_{ss}=c\sum_b y_b D_b\otimes h_{1,b}.
\]

Differentiating z_1 and then h_1 gives
F_1 = c P_1 C Y P_1 R^{(1)}. Differentiating z_2 = W^{(2)}h_1 twice gives
X_2 = c K_1 Y D + AF_1. Differentiating z_3 similarly gives
X_3 = c K_2 Y U + BF_2. There are no additional mixed terms: each would
contain an initial hidden first derivative. These verify all factors and
matrix orders in (5).

Next,

\[
 w_{sss}=c y^TP_3X_3=V_2,\qquad
 (\delta_3)_{sss}=p(Z_3)V_2+3V\operatorname{diag}(p'(Z_3))X_3.
\]

The factor 3 is the product-rule coefficient multiplying w_s times the
second s-derivative of p(z_3); that latter derivative is p'(Z_3)X_3.
Consequently

\[
 (q_2)_{sss}=B^TF_{3,*}+3(W^{(3)})_{ss}^TU.
\]

For its component a, the second term is
3c sum_b y_b h_{2,b} <U_b,U_a>, which is exactly 3c S_3 Y H_2, with the
sample-index order used in (7). It is not an optional matrix-update term.

The identical differentiation at layer two gives

\[
 (\delta_2)_{sss}
 =P_2T^{(2)}+3\operatorname{diag}(p'(Z_2)\odot X_2)R^{(2)},
\]

and the derivative of A^T supplies exactly 3c S_2 Y H_1. This verifies (8).
The second derivatives of both queries are zero. Equivalently, the local
solution has w odd and hidden variables even in s, since the readout
velocity is even and hidden velocities are odd under w -> -w.

Thus q(s) = sR + s^3 T/6 + higher-order terms has the stated normalization.
No factor of c, 3, 6, or n is missing in (4)--(9).

## 4. Repeated Gaussian conditioning, including all regression terms

Here arrays have n rows, while a single-neuron sample vector is a column,
as in the candidate. This distinction accounts for transposes in the
finite-array formulas.

### 4.1 The exact conditional matrix law

Fix the exposure immediately before a fresh query. Conditional on it, all
input arrays for that query are fixed. If WH = Z and W^TU = R have already
been exposed, the conditional mean in (28) is

\[
 W_0=Z(H^TH)^{-1}H^T
       +U(U^TU)^{-1}R^T(I-\Pi_H).
\]

It satisfies W_0H = Z. Its transpose on U is
H(H^TH)^{-1}Z^TU + (I-Pi_H)R = R, using H^TR = Z^TU. The space of
homogeneous perturbations satisfying both constraints is precisely

\[
 \{(I-\Pi_U)V(I-\Pi_H):V\in\mathbb R^{n\times n}\}.
\]

Both summands of W_0 are Frobenius-orthogonal to that space. The vector of
initial matrix entries is an isotropic Gaussian with variance 1/n, so its
orthogonal components are independent Gaussians: this follows directly by
factoring their joint Gaussian characteristic function when the cross
covariance is zero. Projecting onto the homogeneous space therefore gives
exactly the residual in (28), with a fresh independent Gaussian matrix.

For adaptive queries, condition on the previous transcript first. The next
input is then fixed, and revealing its output is a linear conditioning of
the current Gaussian residual. Induction gives the same statement with
enlarged input spans. No conditioning on an arbitrary nonlinear function of
an unexposed residual is permitted or needed here.

### 4.2 First reverse queries

Before R has been exposed, direct transposition of the forward-conditioned
matrix gives (29), with

\[
 b_i\mid\text{exposure}\sim N(0,U^TU/n)
\]

independently over its rows. This covariance is an uncentered second
moment, not Cov(U), and not the covariance of a regression residual of U
against Z. The candidate gets this distinction right.

The limiting conditional mean is
E[UZ^T] K_H^{-1} H. For a centered nondegenerate Gaussian Z with covariance
K_H, integration of the Gaussian density derivative gives

\[
 E[F(Z)Z^T]=E[\nabla F(Z)]K_H.
\]

Indeed, differentiate the density, whose gradient is -K_H^{-1}z times
that density, and integrate each component by parts. The boundary term
vanishes for the smooth polynomial-growth functions here because Gaussian
decay dominates their growth. Independent auxiliary Gaussian variables can
first be held fixed, and then integrated. Thus no specialized external
identity is being assumed.

Applying this calculation first to U and then to D gives exactly

\[
 (\Gamma_3)_{ab}=c y_b E[p(Z_{3,a})p(Z_{3,b})]
              +\delta_{ab}E[Vp'(Z_{3,a})],
\]

and the displayed formula for Gamma_2. In the latter derivative zeta_2 is
held fixed because it is an independent local source in the already
identified limiting layer-two law. All deterministic coefficients are
also held fixed. Equations (10)--(11), including both noise covariances,
are correct.

### 4.3 New forward queries

For a finite new forward input X, define

\[
 A_n=(X^TH/n)K_H^{-1},\qquad
 B_n=(X^T(I-\Pi_H)R/n)S_U^{-1},\qquad
 X_\perp=(I-\Pi_H)X.
\]

Multiplying (28) by X gives the exact conditional representation

\[
 WX=ZA_n^T+UB_n^T+(I-\Pi_U)b_X,
\quad
 (b_X)_i\mid\text{exposure}\sim N(0,X_\perp^TX_\perp/n)
\]

with independent rows before the left projection. In the limit,
E[H zeta^T] = 0, and the old reverse field is its H-regression plus zeta.
It follows that B_n converges to E[X zeta^T]S_U^{-1}. This proves all three
parts of (30).

In particular, its noise covariance is E[(X-A_XH)(X-A_XH)^T]. One must not
subtract a second regression covariance against zeta: the reverse
constraint acts through the left projection onto the output-space span U,
whose local contribution vanishes as explained in Section 5 below.

For F_1 the cross moment is

\[
 E[F_1\zeta_1^T]S_2^{-1}
 =cE[P_1CYP_1]=c(C\odot G_1)Y.
\]

For F_2, conditional on Z_2, the coefficient of zeta_2 is
cP_2L_1YP_2, and xi_2 is independent of zeta_2. Hence

\[
 E[F_2\zeta_2^T]S_3^{-1}
 =cE[P_2L_1YP_2]=c(L_1\odot G_2)Y.
\]

Adding the explicit cK_jY backward-field terms from (5) gives precisely
(13) and (16). The placement of Y on the right in (14) and (17) is correct.

### 4.4 Final reverse queries

Let the enlarged forward arrays be Hhat and Zhat = WHhat. At finite width,
set D_n = (F^TU/n)S_U^{-1} and Fperp = F - UD_n^T. Transposing the exact
conditional matrix formula and using the compatibility constraint gives

\[
 W^TF=RD_n^T
 +\widehat H K_{\widehat H}^{-1}(\widehat Z^TF_\perp/n)
 +(I-\Pi_{\widehat H})b_F,
\]

where the fresh rows of b_F have covariance Fperp^TFperp/n. In particular,
the subtraction from F is its regression against the already queried U;
the subtraction from the conditional mean is then absorbed by replacing
F with Fperp in the Zhat cross moment. This is exactly (31).

The Gram in that mean is the Gram of the forward **inputs** Hhat. It need
not equal the second-moment matrix of the adaptively obtained outputs
Zhat. Equations (22) and (26) use the correct Gram.

For B, the additional forward output is BF_2 = X_3-cK_2YU. For A, it is
AF_1 = X_2-cK_1YD, with its redundant sample direction removed at rho = -1.
Consequently (22)--(27) are the direct specializations of this exact
formula, together with the learned-matrix terms already checked in (7)
and (8). The covariances Lambda_3 and Lambda_2 and the regressions D_3,
E_3, D_2, and E_2 contain the needed subtraction terms. No additional
reverse regression is missing.

### 4.5 Legitimacy of the two-matrix exposure order

The order in lines 504--510 is valid when interpreted as a common query
transcript for the two matrices. Starting from the independent initial
matrices, each input is measurable in that transcript:

1. The forward passes produce Z_2 and Z_3.
2. U is a function of Z_3, so B^TU may be exposed.
3. D is a function of Z_2 and B^TU, so A^TD may be exposed.
4. F_1 is a function of Z_1 and A^TD, so AF_1 may be exposed.
5. F_2 is determined by the preceding outputs, so BF_2 may be exposed.
6. F_{3,*} uses Z_3 and BF_2, so B^TF_{3,*} may be exposed.
7. F_{2,*} now uses only exposed outputs, so A^TF_{2,*} may be exposed.

At each step the queried matrix's residual is independent of the other
matrix's remaining residual, conditionally on the transcript. Revealing
a linear query of the former preserves that factorization. This is the
appropriate justification for adaptivity; it does not require revealing
both entire matrices and then pretending a residual is still fresh.

## 5. Finite-array joint empirical moments: explicit closure of the sketch

Lines 513--545 need more than a per-coordinate Gaussian heuristic. The
following estimates justify their stated conclusion for the actual fixed
query list. They also describe the strength of convergence being used:
convergence in probability of the empirical mixed moments, jointly over
the finitely many layer-local tuples and tests needed in the computation.
They do not identify neuron indices across layers or assert an unrelated
cross-layer independence law.

### 5.1 Removing projections in every needed moment

Let L be an exposed n by k full-rank column basis, k fixed, and let the
fresh Gaussian array b have independent rows with covariance S conditional
on the exposure. Put

\[
 \alpha=(L^TL)^{-1}L^Tb,\qquad \Pi_Lb=L\alpha.
\]

Conditionally, the covariance of vec(alpha) is, up to the vectorization
convention, S tensor (L^TL)^{-1}. On an exposed event where
lambda_min(L^TL/n) >= delta > 0 and ||S|| <= M, fixed-dimensional Gaussian
moments therefore give, for every fixed integer q >= 1,

\[
 E[\|\alpha\|^{2q}\mid\text{exposure}]\le C_{q,k,M,\delta}n^{-q}.
\]

Also, deterministically,

\[
 \frac1n\sum_i\|(\Pi_Lb)_i\|^{2q}
 \le\|\alpha\|^{2q}\frac1n\sum_i\|L_i\|^{2q}.
\]

Thus tightness of the exposed basis's empirical 2q-th moment makes the
projection negligible in that same empirical moment norm, with norm of
order O_P(n^{-1/2}) on the stated events. This verifies the higher-moment
claim behind line 535; the Frobenius estimate (32) alone would not have
been enough to justify all the later products.

Every discarded projection has this form. Its basis is H, U, or an
enlarged forward-input basis, all already exposed before the fresh
Gaussian is generated. The relevant limiting Grams are positive definite;
their endpoint reduction is checked in Section 6 below. Consequently the
bounded-inverse events can be made to have probability tending to one.
No uniform integrability of inverse finite Grams is silently required.

### 5.2 Conditional row averaging and preservation of old joint laws

Suppose the old local rows x_i already have convergent empirical smooth
mixed moments of all fixed orders needed at the next step. Given the
exposure, a fresh row source can be represented as S_n^{1/2}g_i, with g_i
independent standard Gaussian vectors. S_n converges in probability to
the deterministic covariance S, possibly singular.

For a smooth test psi of polynomial growth, with polynomially bounded
derivatives, conditional independence gives the bound

\[
 \operatorname{Var}\left(\frac1n\sum_i
 \psi(x_i,S_n^{1/2}g_i)\,\middle|\,\text{exposure}\right)
 \le\frac{C}{n}\left(1+\frac1n\sum_i\|x_i\|^{2m}\right)
\]

on bounded-covariance and bounded-coefficient events, for some fixed m.
The right side tends to zero in probability. The conditional expectation
is the empirical average of
x -> E[psi(x,S_n^{1/2}g)]. With S_n replaced by S, this is another smooth
polynomial-growth test of the old rows, so the induction hypothesis
applies. The replacement costs o_P(1): matrix square roots are continuous
on positive semidefinite matrices, and the mean-value inequality and
Gaussian moment bounds control the test difference. Strict positive
definiteness of S is unnecessary for this step.

The same argument handles each converging random regression coefficient.
It proves independence of the new source from the *whole previously
tracked local tuple*, not merely from its forward root. This is the
independence needed for xi_2 and eta_2 in (13) and (23).

Finally, errors in earlier arrays and the projection errors remain
negligible under every displayed rowwise transformation: for these maps
one has a mean-value bound of the form

\[
 \|\Phi(x)-\Phi(x')\|
 \le C(1+\|x\|^m+\|x'\|^m)\|x-x'\|.
\]

Hölder's inequality, the higher empirical moments, and the projection
estimate just proved give the required error convergence. This is the
stability step that turns local source descriptions into mixed-moment
convergence for the finite arrays themselves.

### 5.3 Applying the induction without circular Gram assumptions

The initial Z_1 averages converge by independence and the elementary
variance bound Var(n^{-1}sum_i psi(Z_{1,i})) = Var(psi(Z_1))/n. Each
initial forward pass has conditionally independent Gaussian rows with
its empirical input Gram as covariance, so the same conditional averaging
argument initializes the laws of Z_2 and Z_3.

The subsequent induction is in precisely the query order in Section 4.5.
K_1 and K_2 are already known positive definite when used in the first
reverse regressions; S_3 and then S_2 are identified before their inverse
regressions are used. The new forward queries do not require inversion of
Omega_1 or Omega_2. Their limiting laws establish the strict Schur
complements before the enlarged Grams are inverted in the final reverse
queries. This avoids a circular convergence/invertibility argument.

All row transformations actually needed here have the stated smooth
polynomial-growth property. In particular, F_{2,*} contains products of
X_2 and R^{(2)}, but these have fixed degree in the local Gaussian sources.
There is no discontinuity, varying query count, or time-dependent limit in
this induction. Applying the estimates at finitely many steps and using a
finite union bound gives the claimed simultaneous convergence.

Accordingly Section 5 supplies a valid argument once its terse
“higher-moment argument” is expanded as above. I do not classify the
absence of these displayed elementary bounds as an additional unproved
specialized theorem or an extra population-flow premise.

## 6. All strict covariance and Gram checks

The following checks are for each fixed allowed rho and either label mode;
none asserts a bound uniform as rho approaches 1.

**S_3.** If v^TU vanishes almost surely, positive density and continuity
make V(z)(v_1p(z_1)+v_2p(z_2)) vanish everywhere. There is an open rectangle
on which V is nonzero for either label mode. Varying one coordinate on
that rectangle, and using nonconstancy of p on any interval, forces both
coefficients to vanish. Thus S_3 is positive definite.

**S_2.** Conditional on Z_2, D has covariance P_2S_3P_2, positive definite
because each gate is strictly positive. Its uncentered second moment
S_2 is therefore positive definite as well.

**L_1 and L_2.** The identity C odot G_1 = E[P_1CP_1] proves positive
semidefiniteness even when C is singular. Adding K_1 gives L_1 positive
definite. Also L_1 odot G_2 = E[P_2L_1P_2] is positive definite, so L_2
is positive definite. No sign assumption on the off-diagonal entries is
needed for either assertion.

**Omega_1 and the first enlarged Gram.** For interior rho the conditional
coefficient cP_1CYP_1 of zeta_1 is invertible. Subtracting A_1H_1 is
deterministic given Z_1, so Omega_1 is then positive definite. At rho = -1,
put e = (1,-1)^T and write P_1 = p(G)I. Exactly,

\[
 F_1=c p(G)^2 e e^TYR^{(1)},\qquad J_1=e^T/\sqrt2,
\]

and

\[
 \operatorname{Var}(J_1F_1\mid Z_1)
 =2c^2p(G)^4 e^TYS_2Ye>0.
\]

The discarded direction is identically zero, including at finite width.
The retained direction reconstructs all of F_1. Thus J_1Omega_1J_1^T is
strictly positive and is exactly the Schur complement of K_1 in the
retained enlarged Gram. This verifies (26) without an unstable
pseudoinverse. Omega_1 itself is allowed to be singular at this endpoint.

**Omega_2 and the second enlarged Gram.** Conditional on Z_2,

\[
 F_2=\text{conditional mean}
       +N(Z_2)\zeta_2+P_2\xi_2,\qquad
 N(Z_2)=cP_2L_1YP_2.
\]

Every factor in N is invertible. Independence of the two noises makes
their conditional covariances add. Subtracting A_2H_2 cannot remove
N S_3 N^T. This proves (18), and the Schur complement of K_2 in
mathcal K_2 is exactly Omega_2. Both claims remain strict at rho = -1.

**Lambda_3.** From (6), the first term of M is c p(Yp)^T, so its sample
index order in (19) is correct. Conditional on Z_3, F_{3,perp} retains
M(Z_3)xi_3. At z = (0,1), p'(0) = 0 and direct two-by-two expansion gives

\[
 \det M(0,1)=3c y_1 V(0,1)p(0)^2p'(1).
\]

For sigma = +1, V(0,1) = c(2+g(1)) > 0. For sigma = -1,
V(0,1) = -c g(1) != 0. Also p'(1) != 0. Thus M is invertible on an open
set of positive top-Gaussian probability, proving
E[M Omega_2 M^T] positive definite and hence (21). This uses the full
matrix determinant, not merely a nonzero variance for each coordinate.

**Lambda_2.** Conditional on the preceding layer-two tuple, the fresh
term in F_{2,*} is exactly P_2eta_2. D is measurable in that preceding
tuple, so subtracting D_2D leaves that term. Its conditional covariance
is P_2Lambda_3P_2, strictly positive definite at every finite Z_2. This
proves (25).

Every inverse displayed in (10)--(31) is therefore justified, including
the retained endpoint basis. All its entries and the other coefficients
are finite: the limiting fields have moments of every fixed order by the
explicit Gaussian-source construction. These are uncentered second-moment
regressions throughout; adding an intercept or replacing them by centered
covariances would change the formulas and would be incorrect.

## 7. Conditional Gaussian laws and density lower bounds

Partition E_3 according to H_2 and F_2. Given (Z_2,xi_2), the coefficient
of zeta_2 in T^{(2)} is

\[
 B_2(Z_2)=D_3+(E_3)_{F_2}\,cP_2L_1YP_2.
\]

Thus, with m_2 denoting the conditional mean,

\[
 \binom{R^{(2)}}{T^{(2)}}
 =m_2+\begin{pmatrix}I&0\\B_2&I\end{pmatrix}
              \binom{\zeta_2}{\eta_2}.
\]

Given Z_1, the same representation holds at layer one, with

\[
 B_1(Z_1)=D_2+(E_2)_{J_1F_1}\,J_1cP_1CYP_1
\]

and source covariances S_2 and Lambda_2. In the interior J_1 is simply I.
The source covariances at layer two are S_3 and Lambda_3. All four are
positive definite, and both block triangular maps are invertible. This
proves the asserted nondegenerate four-dimensional conditional laws.

For completeness, a compact-set argument really does give the required
uniform density bound. Restrict the conditioning tuple to a compact ball
in its Gaussian support with positive probability. The conditional means
and the matrices B_l are continuous, so their norms are bounded there.
Writing the covariance as L diag(S,Lambda)L^T, the inverse block matrix
is [[I,0],[-B_l,I]]. Hence for constants 0 < lambda <= L_0 < infinity,

\[
 \lambda I\preceq\Sigma\preceq L_0 I
\]

uniformly on the chosen conditioning set. The conditional means have a
uniform norm bound M_0. On any fixed four-dimensional box of radius R_0,
the Gaussian density is consequently at least

\[
 (2\pi)^{-2}L_0^{-2}
 \exp\!\left(-\frac{(R_0+M_0)^2}{2\lambda}\right)>0.
\]

Integrate over that conditioning set to get an unconditional lower bound.
Integrating the other two coordinates over a fixed positive-volume box
then gives a lower bound for the requested scalar pair (R_a,T_a). One
can choose a box covering a neighborhood of
{0} times [1,9/8], so the exact strip used in (36) is covered, not just an
unspecified possibly smaller neighborhood of (0,1).

This argument requires neither a Lebesgue density for Z_1 at rho = -1 nor
one for the possibly singular xi_2. It integrates their probability
measures on their supports. The claim in lines 425--432 is therefore
valid. This is an ordinary mixture-density argument; no conditioning on
the event R_a = 0 is used for the crossing estimate.

## 8. Physical-time normalization: checked conditionally on its missing equation

Here is the raw equation consistent with the candidate's factors, which
R1 asks the candidate to state rather than obtain from an external file:

\[
 \dot w=-2\sum_b r_bh_{3,b},\qquad
 \dot W^{(3)}=-2\sum_b r_b\delta_{3,b}\otimes h_{2,b},
\]
\[
 \dot W^{(2)}=-2\sum_b r_b\delta_{2,b}\otimes h_{1,b},\qquad
 \dot z_{1,a}=-2\sum_b C_{ab}r_bp(z_{1,b})q_{1,b},\qquad r=f-y.
\]

Under precisely this convention, r' = -2Kr. At w = 0 all hidden tangent
kernel blocks vanish, since their feature gradients contain a backward
field linear in w. Their first time derivatives also vanish, since the
kernel blocks are quadratic in those gradients. The readout block has
zero derivative because the hidden first velocities vanish. Therefore
K(0) = K_3 and K'(0) = 0 at the stated population initialization.

Initial exchangeability makes K_3 have equal diagonal entries, so y is
its eigenvector with eigenvalue kappa. The positive-definite Gram check
above gives kappa > 0. Hence

\[
 r(0)=-y,\qquad r'(0)=2K_3y=2\kappa y,\qquad
 r''(0)=-4K_3^2y=-4\kappa^2y,
\]

which verifies (34) under the explicitly stated raw convention. Through
second order in the field multiplier, r = -lambda(t)y with
lambda(t) = 1-2kappa t+2kappa^2t^2. Comparing -2r with cy, where c = 1/2,
gives 4-8kappa t+8kappa^2t^2. Integration yields

\[
 s(t)=4t-4\kappa t^2+\tfrac83\kappa^2t^3.
\]

Substitution into q(s) = sR+s^3T/6 gives the coefficients in (A) and

\[
 q'(0)=4R,\qquad q''(0)=-8\kappa R,\qquad
 q'''(0)=16\kappa^2R+64T.
\]

The factor 32/3 in (A) is 4^3/6, and the factor 16 in the third derivative
is 3! times 8/3. No trained-path label symmetry is required: only the
initial residual jet has been used.

There is an important finite/population distinction, already acknowledged
in lines 586--593. A finite random K_{3,n} need not have y as an
eigenvector. Under the same raw equation, its exact finite residual
derivatives are 2K_{3,n}y and -4K_{3,n}^2y. For fixed initialization let
R[v] denote the static linear query with label vector v and T[y] the
static third derivative for y. The exact finite physical derivatives are

\[
 q'(0)=4R[y],\quad q''(0)=-8R[K_{3,n}y],\quad
 q'''(0)=16R[K_{3,n}^2y]+64T[y].
\]

One can see the last identity directly from q = L(hidden)w: hidden first
derivatives vanish, hidden second physical derivatives are 16 times
their s-derivatives, and w'_t = 4V. The cubic product-rule contribution
is therefore 64 times its s-field counterpart, while the r'' term gives
16R[K_{3,n}^2y]. The scalar-kappa expressions describe the canonical
limiting static coefficients, not identities for every empirical Gram.

This algebra does not establish that a limiting population path has
these derivatives. Nor does it give any population remainder estimate.
Assumption (A) continues to bear both obligations in the conditional
claim under review.

## 9. Crossing probability and the scope of continuity

Let d > 0 be the scalar-pair density lower bound on a box containing the
strip in (36). Its width in R is t^2 and its width in T is 1/8, so

\[
 P(E_t)\ge(d/8)t^2=:c_0t^2.
\]

For sufficiently small u > 0, a(u)/u lies between 15/4 and 17/4.
Because R is negative on E_t, the correct lower bound at t uses the
upper bound on a(t) and R >= -2t^2. The correct upper bound at t/2 uses
the lower bound on a(t/2), R <= -t^2, and T <= 9/8. Thus

\[
 Q(t)\ge(32/3-17/2)t^3=(13/6)t^3,
\]
\[
 Q(t/2)\le(-15/8+3/2)t^3=-(3/8)t^3.
\]

All signs and constants in (37) are correct. Write e(u) = q(u)-Q(u).
Assumption (A), at the two deterministic times, and Markov's inequality
give the explicit union bound

\[
 P\{|e(t)|>t^3/8\text{ or }|e(t/2)|>t^3/8\}
 \le (8C)^{p_*}(1+2^{-4p_*})t^{p_*}=o(t^2).
\]

On its complement within E_t,

\[
 q(t)\ge(49/24)t^3>0,\qquad q(t/2)\le-(1/4)t^3<0.
\]

Subtracting the exceptional probability proves (B), with c_0/2 after
shrinking the time interval. No independence between the remainder and
(R,T), no conditional remainder estimate on E_t, and no uniformity in
rho are needed. The condition p_* > 2 is exactly sufficient for this
comparison; an O(t^4) L^2 estimate alone would only bound the bad-event
probability by O(t^2) and would not give the asserted conclusion for an
arbitrary constant C.

The strict opposite signs at the two deterministic times already rule
out an almost-everywhere fixed-sign property on any interval containing
them. A zero between them additionally uses almost-sure continuity of
the scalar control paths. The candidate's continuity assumption should
be understood in this sense for its intermediate-value sentence.
Continuity merely in an unspecified function-space topology is not,
by itself, a pointwise intermediate-value hypothesis. This distinction
does not affect (B).

For the example stronger premise mentioned at line 642, a C^4 path into
L^{p_*} with the identified derivatives and a bounded fourth derivative
does give (A) by integrating the fourth derivative, with norm bound
t^4 sup ||q^{(4)}||/24. A C^1 Banach-space path also has the absolutely
continuous representative obtained by integrating its L^{p_*}
derivative, when scalar paths are represented through that integral.
None of those regularity facts proves that the actual population flow
possesses the stipulated regularity.

The statements about different crossing sets at different t, lack of a
uniform input-angle constant, and preservation of sign changes upon
multiplication by a continuous nonzero residual or a fixed label are
all consistent with this argument. It makes no claim about infinitely
many crossings by the same neuron.

## 10. Optional improvements, separated from R1

1. **Expand Section 5's moment proof.** Inserting the projection-coefficient
   covariance, the conditional averaging variance bound, and the
   polynomial stability inequality from Section 5 of this report would
   make the finite-array justification substantially easier to check.
   The existing ingredients are sufficient for this fixed program; this
   is an exposition improvement, not a demand for a new external theorem.

2. **Qualify the “alternatively” sentence at lines 349--350.** Nonzero
   off-diagonal entries establish nonzero individual rows, but that fact
   alone does not imply positive definiteness of a vector covariance:
   a matrix with both rows equal can have nonzero off-diagonal entries.
   The preceding determinant/open-set proof is valid and already proves
   the needed full matrix assertion. Deleting the alternative or limiting
   it to coordinatewise variance would remove a misleading shortcut.

3. **Specify the continuity used for the intermediate value theorem.**
   Say that the scalar controls have almost-sure continuous paths when
   claiming a zero between t/2 and t. The quantitative opposite-sign
   event itself needs only (A), not continuity.

4. **Clarify the status-table wording around (35).** Call these the
   canonical limiting static physical-jet coefficients, under the stated
   raw normalization, rather than leave room to read them as exact
   scalar-kappa identities for every finite empirical Gram. Lines
   586--593 already contain the necessary substantive caveat.

5. **Keep the zero-slope wording probabilistically precise.** The full
   conditional Gaussian law shows that no almost-sure sign or vanishing
   restriction on the cubic coefficient follows from a slope constraint.
   A literal event R_a = 0 has probability zero; if a conditional law
   exactly at that value is discussed, specify the density-based regular
   conditional version. The actual crossing proof correctly avoids this
   issue altogether.

Final scope/verdict: the finite static algebra, the two-matrix limiting
Gaussian law, all required positive-definiteness statements, the local
density bound, and the conditional implication (A) => (B) are verified.
The missing raw physical-flow equation requires the local self-containment
correction R1. The actual population derivative/remainder bridge remains
unproved and was not discharged by this audit.
