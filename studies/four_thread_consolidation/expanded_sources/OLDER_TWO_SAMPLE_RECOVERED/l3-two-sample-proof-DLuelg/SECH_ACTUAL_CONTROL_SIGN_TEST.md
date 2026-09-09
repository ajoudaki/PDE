# Actual sech-control initialization test: a nondegenerate cubic crossing law

2026-09-06. Bounded theory sidecar; no experiments. This document does not
audit the prescribed-control theorem in SECH_GATE_ACTIVATION_DESIGN.md.

## Conclusion and exact claim level

For the canonical two-sample, three-hidden-layer initialization with zero
population readout and

\[
 \phi(z)=1+\tfrac1{10}\arctan(\sinh z),\qquad
 p(z)=\phi'(z)=\tfrac1{10}\operatorname{sech}z,
\]

the static initial Gaussian query program below computes both the linear
and cubic control coefficients. For EACH layer \(\ell=1,2\), the resulting
pair \((R^{(\ell)},T^{(\ell)})\in\mathbb R^2\times\mathbb R^2\) has a
nondegenerate Gaussian conditional law given its forward root (and, at
layer two, one additional initial Gaussian source). In particular, each
\((R^{(\ell)}_a,T^{(\ell)}_a)\) has a density bounded below on a neighborhood
of \((0,1)\). A zero initial slope does NOT force the cubic coefficient
to vanish or to have either particular sign.

These are canonical INITIAL-law statements, proved here by repeated
conditioning of the SAME two initial matrices. They are not assertions
that trained fields are Gaussian, nor counterexamples with prescribed
external controls. They hold for either label mode and every
\(\rho\in[-1,1)\), including antiparallel inputs.

Here is the exact remaining bridge to an actual population crossing.
Suppose an actual population gradient flow with almost-sure continuous
scalar control paths exists locally,
and its controls have the identified initial coefficients with the
quantitative remainder (for some \(p_*>2\))

\[
 \left\|q^{(\ell)}_a(t)
 -\left(4t-4\kappa t^2+\tfrac83\kappa^2t^3\right)R^{(\ell)}_a
 -\tfrac{32}{3}t^3T^{(\ell)}_a\right\|_{L^{p_*}}
 \le C t^4.                                                   \tag{A}
\]

The positive constant \(\kappa\) is defined in Section 6. Then, for every
sufficiently small deterministic \(t>0\), separately for every \(\ell,a\),

\[
 \mathbb P\{q^{(\ell)}_a(t/2)<0<q^{(\ell)}_a(t)\}
 \ge c_{\ell,a}t^2>0.                                        \tag{B}
\]

Thus (A) rules out an almost-everywhere fixed-sign assertion for either
control field on any nontrivial trained interval starting at zero. The
population derivative identification and bound (A) are NOT proved in
this sidecar or imported from the permitted sources. Without that bridge,
the conclusion is an exact, nondegenerate initial cubic discriminator
and a conditional crossing theorem, NOT an unconditional population
sign-change theorem. No sign invariant is proved. Neither the conditional
route obstruction nor the static discriminator refutes the full theorem.

## 1. Dependencies, authorization, and model

The following files were read completely. SHA256 of the bytes read:

| File | SHA256 | Use |
|---|---|---|
| `/tmp/l3-two-sample-proof-DLuelg/CONTRACT_AND_LEDGER.md` | `c5827c6790b61b09145dd6fb968516a7ffa86a3e2cd9e1e8be6a21527b7fdfda` | Canonical initialization, raw GF normalization, target and scope. |
| `/tmp/l3-two-sample-proof-DLuelg/SECH_GATE_ACTIVATION_DESIGN.md` | `c0f67365fbe36af74db9708ce8a32018b30d8164e77c50b068f71299045e4f24` | Activation and the fixed-sign hypothesis being tested. Its prescribed-control proof is not audited or used. |
| `/tmp/l3-two-sample-proof-DLuelg/GAUSSIAN_BACKWARD_SIGN_TRANSFER.md` | `5ff166e2c9ab7faf504be74795d513d61fae14a1b8d789e3759606dba09670e8` | Only the initial double-transpose conditioning mechanism in Section 3. The arctan-specific integral identities and cone theorem are not used. |

All specialized mathematics needed below is derived here. In particular,
there is no recursive dependency on the arctan signed-response note.
The investigate-conjectures skill and its research-contract,
evidence-ledger, and adversarial-audit references supplied procedural
scope/claim-level instructions only; they are not mathematical premises.
For complete read provenance, their paths relative to
`/etc/codex/skills/investigate-conjectures/` and SHA256 values are:

| Procedural file | SHA256 |
|---|---|
| `SKILL.md` | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `references/research-contract.md` | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| `references/evidence-ledger.md` | `9e7573b37cbd954432236bdcb13f6b83b6325e0ff2653a198939842bc81c3a2e` |
| `references/adversarial-audit.md` | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |

No other research artifacts were read or edited. No numerical experiment,
external source, activation search, or finite-width sign-change example
is part of this result.

Write \(y=(1,\sigma)\), \(\sigma=\pm1\), \(Y=\operatorname{diag}y\),
and \(c=1/2\). Other choices of the first label follow by reversing the
readout and both queries. Let

\[
 C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\qquad
 Z_1\sim N(0,C),\quad H_j=\phi(Z_j),\quad
 K_j=\mathbb E[H_jH_j^T],
\]
\[
 Z_2\sim N(0,K_1),\qquad Z_3\sim N(0,K_2).
                                                               \tag{1}
\]

Vector functions act componentwise. Different layer subscripts denote
SEPARATE neuron populations. Expectations of tuples at one layer are
taken on that layer's probability space; neuron indices at different
layers are never identified. Define

\[
 P_j=\operatorname{diag}(p(Z_{j,1}),p(Z_{j,2})),\qquad
 G_j=\mathbb E[p(Z_j)p(Z_j)^T].                                \tag{2}
\]

The function \(\phi-1\) is odd, bounded, strictly increasing, and
nonconstant, and \(p>0\). Both \(K_1,K_2\) are positive definite. For
\(-1<\rho<1\), positive Gaussian density excludes a homogeneous linear
relation between the two nonconstant features. At \(\rho=-1\), their
constant and nonconstant odd parts are linearly independent. Induction
then gives a nondegenerate top Gaussian pair. All fixed derivatives of
\(\phi\) are bounded: differentiating \(\operatorname{sech}\) and
\(\tanh\) preserves polynomials in these bounded functions.

## 2. Exact finite algebra for the relevant Taylor coefficients

This section is algebra at zero readout, not a finite-width
initialization counterexample. Zero readout is the canonical population
initial condition. For the calculation, use equal finite widths and
write every empirical pairing explicitly as a sum divided by \(n\).
Write \(A=W^{(2)}_0\), \(B=W^{(3)}_0\), and \(w=W^{(4)}\).
Explicitly, the initial rows of \(z_1\) are iid \(N(0,C)\), and \(A,B\)
have iid \(N(0,1/n)\) entries, mutually independent and independent of
those rows. Set \(h_1=\phi(z_1)\), \(z_2=Ah_1\), \(h_2=\phi(z_2)\),
\(z_3=Bh_2\), \(h_3=\phi(z_3)\), and \(f_a=w^Th_{3,a}/n\).
Along the finite algebraic field,
\(\delta_{3,a}=w\odot p(z_{3,a})\),
\(q_{2,a}=(W^{(3)})^T\delta_{3,a}\),
\(\delta_{2,a}=p(z_{2,a})\odot q_{2,a}\), and
\(q_{1,a}=(W^{(2)})^T\delta_{2,a}\); residuals are not included.
The finite static programs below evaluate the zero-population-readout
jet using this canonical hidden initialization. No finite trajectory
with its readout artificially set to zero is used as a sign witness.

Here is the raw PHYSICAL normalization, stated within this document.
For fixed inputs \(x_a\in\mathbb R^d\), \(x_a^Tx_b/d=C_{ab}\),
let \(z^{(1)}_a=W^{(1)}x_a\), \(r_a=f_a-y_a\), and
\(L=r_1^2+r_2^2\). The metric is
\(d\|dW^{(1)}\|_F^2/n+\|dW^{(2)}\|_F^2+
\|dW^{(3)}\|_F^2+\|dW^{(4)}\|_2^2/n\). With the residual excluded
from each backward field, its negative loss gradient is

\[
 \dot W^{(1)}=-\frac2d\sum_b r_b\delta^{(1)}_b x_b^T,
 \qquad
 \dot z^{(1)}_a=-2\sum_b C_{ab}r_b\delta^{(1)}_b,
\]
\[
 \dot W^{(\ell)}=-\frac2n\sum_b r_b\delta^{(\ell)}_b
                    (h^{(\ell-1)}_b)^T\quad(\ell=2,3),
 \qquad \dot W^{(4)}=-2\sum_b r_bh^{(3)}_b.                 \tag{2a}
\]

These formulas follow by differentiating the two squared residuals and
inverting the stated constant metric factors. The chain rule gives
\(\dot f_a=-2\sum_b K_{ab}r_b\), where \(K\) is the sum of

\[
 K^{(1)}_{ab}=C_{ab}\frac{(\delta^{(1)}_a)^T\delta^{(1)}_b}{n},
 \qquad K^{(4)}_{ab}=\frac{(h^{(3)}_a)^Th^{(3)}_b}{n},
\]
\[
 K^{(\ell)}_{ab}=
 \frac{(\delta^{(\ell)}_a)^T\delta^{(\ell)}_b}{n}
 \frac{(h^{(\ell-1)}_a)^Th^{(\ell-1)}_b}{n}\quad(\ell=2,3).
                                                               \tag{2b}
\]

The first metric gives the displayed raw pair equation even when
\(C\) is singular; no inverse of \(C\) is used in (2a). Population
pairings below replace these explicit empirical sums by expectations.

It is convenient to first differentiate the autonomous ascent field of
\(J=(f_1+\sigma f_2)/2\) in its own parameter \(s\). The exact equations
with the metrics in the contract are

\[
 w_s=c\sum_b y_b h_{3,b},\quad
 (W^{(3)})_s=c\sum_b y_b\delta_{3,b}\otimes h_{2,b},\quad
 (W^{(2)})_s=c\sum_b y_b\delta_{2,b}\otimes h_{1,b},
\]
\[
 (z_{1,a})_s=c\sum_b C_{ab}y_b p(z_{1,b})q_{1,b}.               \tag{3}
\]

Here \((u\otimes v)x=u(v^Tx)/n\); the matrix update therefore
contains the required factor \(1/n\). No external control is introduced:
(3) is the gradient field used to calculate the original GF jet. Section
6 derives the physical-time coefficients directly from its residuals;
no trained-path label symmetry or global change of clock is assumed.

At zero readout set

\[
 V=c\,y^TH_3,\quad U=V p(Z_3),\quad
 R^{(2)}_a=B^TU_a,\quad D_a=p(Z_{2,a})R^{(2)}_a,\quad
 R^{(1)}_a=A^TD_a.                                            \tag{4}
\]

The notation in (4) initially denotes finite vectors for each sample;
its limiting single-neuron law is constructed in Section 3. Hidden
first derivatives vanish. Let \(X_j=(z_j)_{ss}(0)\) and
\(F_j=(h_j)_{ss}(0)=P_jX_j\). Differentiating (3) gives exactly

\[
 F_1=cP_1CY P_1R^{(1)},\qquad
 X_2=cK_1YD+AF_1,\qquad F_2=P_2X_2,\qquad
 X_3=cK_2YU+BF_2.                                            \tag{5}
\]

At finite width the \(K_j\)'s in these identities are empirical Grams.
Also

\[
 w_{sss}(0)=c\,y^TP_3X_3=:V_2,
\quad F_{3,*}=p(Z_3)V_2+3V\operatorname{diag}(p'(Z_3))X_3.
                                                               \tag{6}
\]

The symbol \(F_{3,*}\) is a reverse input, not \((h_3)_{ss}\).
Writing \(T^{(\ell)}=(q_\ell)_{sss}(0)\), the product rule gives

\[
 T^{(2)}=B^TF_{3,*}+3cS_3YH_2,\qquad S_3=\mathbb E[UU^T],
                                                               \tag{7}
\]
\[
 F_{2,*}=P_2T^{(2)}
       +3\operatorname{diag}(p'(Z_2)\odot X_2)R^{(2)},
\quad T^{(1)}=A^TF_{2,*}+3cS_2YH_1,\quad S_2=\mathbb E[DD^T].
                                                               \tag{8}
\]

Again the expectations in the finite identities are empirical inner
products. For example \(3(W^{(3)})_{ss}^TU\) is exactly the second term
of (7); it cannot be dropped. Both queries have zero second derivative
in the \(s\) field. Equivalently, the local finite equations are invariant
under \(s\mapsto-s,\ w\mapsto-w\), with hidden parameters unchanged.
The normalization is

\[
 q_\ell(s)=sR^{(\ell)}+\tfrac{s^3}{6}T^{(\ell)}+\cdots.        \tag{9}
\]

## 3. Canonical population law through the two new forward queries

Here and below every extra Gaussian source is an initialization-query
source; none describes a field at positive training time.

The initial double transpose has the following law:

\[
 \Gamma_3=\mathbb E[\nabla U(Z_3)],\quad S_3=\mathbb E[UU^T],
\quad R^{(2)}=\Gamma_3H_2+\zeta_2,
\quad \zeta_2\sim N(0,S_3),\quad \zeta_2\perp Z_2,
                                                               \tag{10}
\]
\[
 D=P_2R^{(2)},\quad S_2=\mathbb E[DD^T],\quad
 (\Gamma_2)_{ab}
 =\mathbb E\left[\delta_{ab}p'(Z_{2,a})R^{(2)}_a
                  +p(Z_{2,a})(\Gamma_3)_{ab}p(Z_{2,b})\right],
\]
\[
 R^{(1)}=\Gamma_2H_1+\zeta_1,\qquad
 \zeta_1\sim N(0,S_2),\quad \zeta_1\perp Z_1.                 \tag{11}
\]

In the derivative defining \(\Gamma_2\), hold \(\zeta_2\) and all
deterministic coefficients fixed. In particular,
\((\Gamma_3)_{ab}=c y_b(G_3)_{ab}
+\delta_{ab}\mathbb E[Vp'(Z_{3,a})]\). No arctan sign identity is used.

Both \(S_3,S_2\) are positive definite. If \(v^TU=0\) almost surely,
then on an open rectangle where \(V\ne0\),
\(v_1p(z_1)+v_2p(z_2)=0\). Varying either argument, since \(p\) is
not constant on any interval, forces \(v=0\). For \(S_2\), condition on
\(Z_2\): the covariance of \(D\) contains \(P_2S_3P_2\succ0\).

Compute \(F_1\) from (5),(11), and define the exact Gaussian integrals

\[
 A_1=\mathbb E[F_1H_1^T]K_1^{-1},\quad
 \Omega_1=\mathbb E[(F_1-A_1H_1)(F_1-A_1H_1)^T],
\quad L_1=K_1+C\odot G_1.                                   \tag{12}
\]

The symbol \(\odot\) between matrices denotes entrywise product.
The first new forward query has the exact limiting law

\[
 X_2=A_1Z_2+cL_1YD+\xi_2,\qquad F_2=P_2X_2,\qquad
 \xi_2\sim N(0,\Omega_1),\quad \xi_2\perp(Z_2,\zeta_2).
                                                               \tag{13}
\]

The response term in (13) follows from a useful exact computation:

\[
 \mathbb E[F_1\zeta_1^T]S_2^{-1}
 =c\,\mathbb E[P_1CY P_1]
 =c(C\odot G_1)Y.                                           \tag{14}
\]

Thus (13) includes the lower-matrix reuse contribution; it is not a
calculation with a frozen first layer. Notice that \(L_1\succ0\), because
\(C\odot G_1=\mathbb E[P_1CP_1]\succeq0\) and \(K_1\succ0\).

Next define

\[
 A_2=\mathbb E[F_2H_2^T]K_2^{-1},\quad
 \Omega_2=\mathbb E[(F_2-A_2H_2)(F_2-A_2H_2)^T],
\quad L_2=K_2+L_1\odot G_2.                                 \tag{15}
\]

The second new forward query is

\[
 X_3=A_2Z_3+cL_2YU+\xi_3,\qquad
 \xi_3\sim N(0,\Omega_2),\quad \xi_3\perp Z_3.                \tag{16}
\]

Indeed, conditioning (13) on \(Z_2\), using the independence of its two
Gaussian sources, gives

\[
 \mathbb E[F_2\zeta_2^T]S_3^{-1}=c(L_1\odot G_2)Y.           \tag{17}
\]

Crucially \(\Omega_2\) is positive definite, not just semidefinite. The
coefficient of \(\zeta_2\) in \(F_2\), conditional on \(Z_2\), is

\[
 N(Z_2)=cP_2L_1YP_2,
\]

which is invertible at every finite \(Z_2\). Subtracting \(A_2H_2\)
does not remove this conditional variance. Consequently

\[
 \Omega_2\succeq\mathbb E[N(Z_2)S_3N(Z_2)^T]\succ0.          \tag{18}
\]

All coefficients in (10)--(18) are specified finite Gaussian integrals;
all moments appearing here are finite. No quadrature values are needed.

## 4. The last reverse queries and the independent cubic innovations

Form the top reverse input (6) using (16). It is

\[
 F_{3,*}=M(Z_3)X_3,\qquad
 M(z)=c\,p(z)(Yp(z))^T+3V(z)\operatorname{diag}(p'(z)).         \tag{19}
\]

Let

\[
 D_3=\mathbb E[F_{3,*}U^T]S_3^{-1},\quad
 F_{3,\perp}=F_{3,*}-D_3U,\quad
 \Lambda_3=\mathbb E[F_{3,\perp}F_{3,\perp}^T].               \tag{20}
\]

Conditioning on \(Z_3\), the subtraction in (20) leaves the noise
\(M(Z_3)\xi_3\). Therefore

\[
 \Lambda_3\succeq\mathbb E[M(Z_3)\Omega_2M(Z_3)^T]\succ0.     \tag{21}
\]

For strictness, \(p'(0)=0\) and, at \(z_1=0,z_2=1\),

\[
 \det M(z)=3c\,y_1V(z)p(0)^2p'(1)\ne0.
\]

Here \(p'(1)\ne0\), and \(V(0,1)\ne0\) for either label mode.
Continuity gives an open set of invertibility; the top Gaussian has
positive density there. The determinant argument establishes full
positive definiteness, not merely nonzero coordinate variances.

The COMPLETE cubic law, including the regression terms, is as follows.
On layer two and layer three respectively set

\[
 \mathcal H_2=\binom{H_2}{F_2},\qquad
 \mathcal Z_3=\binom{Z_3}{X_3-cK_2YU},\quad
 \mathcal K_2=\mathbb E[\mathcal H_2\mathcal H_2^T],
\quad E_3=\mathbb E[F_{3,\perp}\mathcal Z_3^T]\mathcal K_2^{-1}.
                                                               \tag{22}
\]

The matrix \(\mathcal K_2\) is positive definite: its Schur complement
over \(K_2\) is precisely \(\Omega_2\). Then

\[
 T^{(2)}=D_3R^{(2)}+E_3\mathcal H_2+3cS_3YH_2+\eta_2,
 \quad\eta_2\sim N(0,\Lambda_3),\quad
 \eta_2\perp(Z_2,\zeta_2,\xi_2).                             \tag{23}
\]

For completeness the same calculation resolves the first-layer cubic
law. Form \(F_{2,*}\) using (8),(13),(23), and set

\[
 D_2=\mathbb E[F_{2,*}D^T]S_2^{-1},\quad
 F_{2,\perp}=F_{2,*}-D_2D,\quad
 \Lambda_2=\mathbb E[F_{2,\perp}F_{2,\perp}^T].               \tag{24}
\]

The fresh term \(P_2\eta_2\), independent of the preceding layer-two
tuple, survives the projection onto \(D\). Hence

\[
 \Lambda_2\succeq\mathbb E[P_2\Lambda_3P_2]\succ0.            \tag{25}
\]

Use \(J_1=I_2\) if \(-1<\rho<1\), and
\(J_1=(1,-1)/\sqrt2\) if \(\rho=-1\). Define

\[
 \mathcal H_1=\binom{H_1}{J_1F_1},\qquad
 \mathcal Z_2=\binom{Z_2}{J_1(X_2-cK_1YD)},\quad
 \mathcal K_1=\mathbb E[\mathcal H_1\mathcal H_1^T],
\quad E_2=\mathbb E[F_{2,\perp}\mathcal Z_2^T]\mathcal K_1^{-1}.
                                                               \tag{26}
\]

These inverses also exist. In the interior, conditional on \(Z_1\), the
coefficient \(cP_1CY P_1\) of \(\zeta_1\) in \(F_1\) is invertible.
At \(\rho=-1\), evenness of \(p\) gives equal gates and
\(F_{1,2}=-F_{1,1}\). Its retained component has strictly positive
conditional variance since \(S_2\succ0\). Thus the Schur complement
\(J_1\Omega_1J_1^T\) is positive definite in either case.

The resulting law is

\[
 T^{(1)}=D_2R^{(1)}+E_2\mathcal H_1+3cS_2YH_1+\eta_1,
 \quad\eta_1\sim N(0,\Lambda_2),\quad\eta_1\perp(Z_1,\zeta_1).
                                                               \tag{27}
\]

This is a statement on the layer-one population. No independence of
\(\eta_1\) and a coordinate of a differently indexed layer is asserted
or needed.

Conditional on \((Z_2,\xi_2)\), (10),(13),(23) express
\((R^{(2)},T^{(2)})\) as an affine function of the independent Gaussian
pair \((\zeta_2,\eta_2)\), with invertible block triangular coefficient
matrix. Conditional on \(Z_1\), (11),(27) give the identical conclusion
for layer one. Their conditional covariance matrices are positive
definite. This proves the announced full-support joint initial law.

More explicitly, restrict the conditioning variables to a bounded set
of positive probability. All relevant coefficients are continuous;
the nonzero Gaussian covariance matrices have a positive minimum
eigenvalue on the resulting compact set. Gaussian conditional densities
then have a uniform positive lower bound on any fixed compact box in
the \((R,T)\) variables. Integration proves the local density lower
bound used in Section 7. This reasoning also works with singular
\(Z_1\) or \(\xi_2\), by restricting to their Gaussian supports.

## 5. Why these are repeated-matrix population laws

Here is a derivation and convergence justification for the conditioning
used above. It also fixes which parts are exact static laws, as distinct
from the derivative/continuation assumptions in (A).

Let \(W\) have independent \(N(0,1/n)\) entries. At finite width let
\(H,Z,U,R\) be column arrays satisfying \(WH=Z\), \(W^TU=R\).
Expose these queries in that order, with each new input measurable in
the existing exposure and independent of the still-unexposed residual.
Use full-rank column bases and their orthogonal projections \(\Pi_H\),
\(\Pi_U\). Gaussian row/column conditioning gives

\[
 W=Z(H^TH)^{-1}H^T
   +U(U^TU)^{-1}R^T(I-\Pi_H)
   +(I-\Pi_U)\widetilde W(I-\Pi_H).                          \tag{28}
\]

The compatibility identity \(H^TR=Z^TU\) verifies both constraints;
orthogonal Gaussian projections give an independent Gaussian residual.
The formula remains valid for adaptive queries by conditioning on the
already revealed values before making the next query.

Initially, before exposing \(R\), the transpose law is

\[
 R=H K_H^{-1}(Z^TU/n)+(I-\Pi_H)b,
\quad b_i\mid\text{exposure}\ \text{iid}\ N(0,S_U),           \tag{29}
\]

where \(K_H=H^TH/n\) and \(S_U=U^TU/n\). The covariance is the uncentered
second moment of \(U\), with no regression covariance subtracted.
Integration by parts in the forward Gaussian gives the \(\Gamma\)
coefficients in (10),(11). It is legitimate because all the displayed
derivatives have at most polynomial Gaussian growth.

For a new forward input \(X\), (28) yields the population rule

\[
 WX\ \leadsto\ A_XZ+B_XU+\xi,\quad
 A_X=\mathbb E[XH^T]K_H^{-1},\quad
 B_X=\mathbb E[X\zeta^T]S_U^{-1},
\]
\[
 \operatorname{Cov}(\xi)
 =\mathbb E[(X-A_XH)(X-A_XH)^T],                              \tag{30}
\]

with a fresh Gaussian source independent of the local output tuple.
In (30) sample vectors are columns; the finite-array coefficients in
(28) are their transposes. Applying this to \((W,U,X)=(A,D,F_1)\) and
\((B,U,F_2)\) proves (13),(16), including (14),(17).

After exposing the enlarged forward input \(\mathcal H\) and output
\(\mathcal Z=W\mathcal H\), let \(F\) be a new reverse input and put
\(D_F=\mathbb E[FU^T]S_U^{-1}\), \(F_\perp=F-D_FU\).
The transpose of the remaining Gaussian residual gives

\[
 W^TF\ \leadsto\ D_FR+
 \mathbb E[F_\perp\mathcal Z^T]K_{\mathcal H}^{-1}\mathcal H
 +\eta,\quad
 \operatorname{Cov}(\eta)=\mathbb E[F_\perp F_\perp^T].        \tag{31}
\]

This proves (23),(27) when combined with the explicit learned-matrix
terms in (7),(8). All subtraction terms in (31) are required.

The query order is legitimate for both actual independent initial
matrices. First expose both forward pairs; then \(B^TU\); then
\(A^TD\); then \(AF_1\); then \(BF_2\); then \(B^TF_{3,*}\);
then \(A^TF_{2,*}\). When conditioning on one matrix, the other may
also be exposed. For example, \(D\) depends on \(A\) only through
\(AH_1=Z_2\); later \(F_{2,*}\) depends on \(A\) through just its
already exposed forward/reverse queries. Thus no independent resampling
of a reused matrix is being made.

To justify the empirical limits, every projection discarded in passing
from (28)--(31) to a local Gaussian source has fixed rank. For a fresh
Gaussian column array \(b\) with row covariance \(S\),

\[
 \mathbb E[\|\Pi b\|_F^2/n\mid\text{exposure}]
 =\operatorname{rank}(\Pi)\operatorname{tr}(S)/n.             \tag{32}
\]

The initial forward rows have bounded covariance. Conditional Gaussian
averaging gives convergence of their polynomial-growth moments. At
each subsequent step, the just-exposed Gaussian covariance and each
fixed-size Gram/response matrix converge by the same conditional
averaging. Inverses converge because their limiting Grams were proved
positive definite. At the antiparallel endpoint the exact redundant
column is removed by \(J_1\), so no unstable pseudoinverse is taken.

All new displayed fields are bounded smooth functions of the current
Gaussian root times polynomials of fixed degree in finitely many
Gaussian sources; consequently their moments of every fixed order
are finite. This also bounds the empirical moments inductively. In
particular, expanding each finite-rank projection in its exposed
columns shows its coefficients tend to zero at order \(n^{-1/2}\)
on events where covariance norms and inverse Grams are bounded; its
empirical moments of any fixed order therefore vanish. Conditional
variance bounds for averages of each newly generated Gaussian test
then tend to zero. Here are the explicit estimates behind that
higher-moment induction. For an exposed \(n\)-by-\(k\) column basis
\(L\), with fixed \(k\), and a fresh Gaussian array \(b\), write
\(\alpha=(L^TL)^{-1}L^Tb\), so \(\Pi_Lb=L\alpha\).
Conditionally its coefficient covariance is
\(S\otimes(L^TL)^{-1}\), up to vectorization order. On exposed
events where \(\lambda_{\min}(L^TL/n)\ge\delta>0\) and \(\|S\|\le M\),
for each fixed positive integer \(q\),

\[
 \mathbb E[\|\alpha\|^{2q}\mid\text{exposure}]
       \le C_{q,k,M,\delta}n^{-q},\qquad
 \frac1n\sum_i\|(\Pi_Lb)_i\|^{2q}
       \le\|\alpha\|^{2q}\frac1n\sum_i\|L_i\|^{2q}.       \tag{32a}
\]

Thus every such projection vanishes in each required empirical moment
norm, using tightness of the already exposed basis moments. For a
smooth polynomial-growth test \(\psi\) of an old row \(v_i\) and a fresh
row \(S_n^{1/2}g_i\), conditional independence yields, on bounded
covariance/coefficient events,

\[
 \operatorname{Var}\left(\frac1n\sum_i\psi(v_i,S_n^{1/2}g_i)
                  \,\middle|\,\text{exposure}\right)
 \le\frac Cn\left(1+\frac1n\sum_i\|v_i\|^{2m}\right)        \tag{32b}
\]

for some fixed \(m\). Its conditional expectation is an empirical
average of a smooth polynomial-growth function of the old row.
Replacing converging covariance square roots and regression coefficients
by their limits costs \(o_{\mathbb P}(1)\), by their continuity and
Gaussian moment bounds. Square roots are continuous also for singular
positive semidefinite covariances: every subsequential limit of bounded
positive roots is the unique positive root of the limiting matrix.
Earlier array errors remain negligible under each displayed map, since
bounded activation derivatives give an inequality of the form

\[
 \|\Phi(v)-\Phi(\widetilde v)\|
 \le C(1+\|v\|^m+\|\widetilde v\|^m)\|v-\widetilde v\|,
\]

and Holder's inequality uses the higher empirical moments and (32a).
Apply this induction in the specified finite query order. The limiting
Grams are proved positive definite before their inverse is used; at
the antiparallel endpoint the exactly redundant direction has already
been removed. Restrict first to bounded-moment/inverse-Gram events and
then increase their bounds. No inverse-Gram uniform integrability is
assumed. This proves joint empirical
convergence in probability, with the needed mixed and polynomial
moments, throughout this fixed finite query list.

Products in (6),(8) cause no exception: they have fixed polynomial
growth in those sources, so the same higher-moment argument applies.
This is the initial static-program law for (4)--(8). It proves neither
interchange of a width limit with time differentiation nor a
positive-time population flow.

## 6. Physical GF normalization, without a trained symmetry assumption

Let \(K_3=\mathbb E[H_3H_3^T]\) and

\[
 \kappa=(K_3)_{11}+\sigma(K_3)_{12}>0.                        \tag{33}
\]

Its equal diagonal entries follow from initial sample exchangeability;
its positive label eigenvalue follows as for the earlier feature
Grams. At zero population readout the three hidden kernel blocks
vanish, hidden velocities vanish, and \(K^{(4)}=K_3\).
The total kernel derivative is zero there: derivatives of hidden
blocks have a factor of the zero backward field, while the readout
block derivative has a factor of the zero hidden velocity.

The raw physical GF equation (2a) and kernel identity (2b) therefore
give, at initialization,

\[
 r(0)=-y,\qquad r'(0)=2\kappa y,\qquad
 r''(0)=-4\kappa^2y.                                        \tag{34}
\]

Through this order the actual vector field is the field (3) multiplied
by \(4-8\kappa t+8\kappa^2t^2\). This is an initial-jet calculation;
it does not assert that the residual stays in a label mode later.
Integrating that multiplier gives
\(s(t)=4t-4\kappa t^2+\frac83\kappa^2t^3\) through degree three.
Combining with (9) yields the exact candidate physical derivatives

\[
 q_\ell'(0)=4R^{(\ell)},\qquad
 q_\ell''(0)=-8\kappa R^{(\ell)},\qquad
 q_\ell'''(0)=16\kappa^2R^{(\ell)}+64T^{(\ell)}.              \tag{35}
\]

At finite width, these algebraic statements are made at zero readout,
with a general residual vector before taking the canonical static
limit; exchangeability makes its limiting Gram the one in (33).
They are not a sign-changing trajectory constructed with noncanonical
initial weights. In the stipulated population model, readout zero is
the actual initial condition. Identifying (35) with derivatives of an
existing population path still requires a valid derivative/limit
argument, explicitly included in (A).

## 7. Quantitative positive-probability crossing under (A)

Fix any \(\ell,a\) and abbreviate \(R=R^{(\ell)}_a\),
\(T=T^{(\ell)}_a\). The Gaussian conditioning result implies, for all
sufficiently small \(t\),

\[
 \mathbb P(E_t)\ge c_0t^2,\qquad
 E_t=\{-2t^2\le R\le-t^2,\ 1\le T\le9/8\}.                 \tag{36}
\]

Let \(a(u)=4u-4\kappa u^2+\frac83\kappa^2u^3\). For small positive
\(u\), \(15u/4\le a(u)\le17u/4\). On \(E_t\), the cubic approximant
\(Q(u)=a(u)R+\frac{32}{3}u^3T\) satisfies

\[
 Q(t)\ge\left(\tfrac{32}{3}-\tfrac{17}{2}\right)t^3
          =\tfrac{13}{6}t^3,
\quad Q(t/2)\le\left(-\tfrac{15}{8}+\tfrac32\right)t^3
          =-\tfrac38t^3.                                    \tag{37}
\]

By (A) and Markov's inequality, the probability that the approximation
error exceeds \(t^3/8\) at either \(t\) or \(t/2\) is at most
\(C't^{p_*}=o(t^2)\). Subtracting that exceptional probability from
(36) proves (B), with (for example) \(c_{\ell,a}=c_0/2\) after decreasing
the time interval. Continuity supplies a zero between these two
deterministic times. No conditioning on a zero-probability event is
used in this crossing argument.

Each sufficiently small \(t\) has its own positive-measure crossing
set. This does not assert that one neuron crosses infinitely often,
that all neurons cross, or that the probability is uniform in the
input angle. Since residuals start at the nonzero values \(-y_a\),
their signs also stay fixed on a sufficiently short continuous
population interval. Multiplying a query by its residual or its
constant label therefore does not remove these crossings.

## 8. Remaining assumptions and bounded stopping point

| Claim | Status and exact boundary |
|---|---|
| Algebra (4)--(8), (35) | Exact finite autonomous differentiation and canonical limiting static physical-jet coefficients under (2a); not scalar-kappa identities for every finite empirical Gram. |
| Initial Gaussian laws (10)--(27) | Proved static limiting query laws for the canonical Gaussian hidden initialization; both matrix reuses retained. |
| Positive definite cubic innovations at both layers | Proved by (18),(21),(25), including \(\rho=-1\). |
| Positive-probability crossing of the cubic approximant | Proved, with probability bounded below by a constant times \(t^2\). |
| Identification of these jets with an actual population flow | Unproved here. Static query convergence alone does not justify differentiation of a limiting trajectory. |
| Remainder (A) on that flow | Unproved here. A local \(C^4\) path into \(L^{p_*}\), \(p_*>2\), with bounded fourth derivative and the identified jets would suffice by the integral Taylor remainder. |
| Actual population sign changes | Proved conditional on (A) and continuity; not promoted to an unconditional population claim. |
| Fixed-sign hypothesis on the whole trained interval | Incompatible with the preceding conditional crossing result; no invariant supports it. Unconditional applicability remains blocked by the stated local bridge. |
| Full all-finite-time theorem | Unchanged/open; a failure of this fixed-sign proof route is not its refutation. |

A mere formal third-order coefficient, pointwise differentiability with
no control near zero-slope populations, or an \(o(t^3)\) remainder in
\(L^2\) does not give the probability comparison in (36)--(37). The
crossing set has mass of order \(t^2\), so a quantitative remainder or
an independently proved suitable conditional-continuity argument is
necessary. No such argument is silently assumed.

This completes the bounded new computation. The single unresolved
bridge for this discriminator is a local actual-population jet and
remainder theorem, not a further activation search, an exogenous-control
construction, or an audit of the prescribed sech-control estimate.
