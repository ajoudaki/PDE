# Trained first and second sphere variations of the three-input p=1 flow

2026-09-16. Scoped analytic report, frozen for comparison. No experiments,
network-limit extension, or promotion are claimed.

Scientific inputs: the established `docs/README.md`, `docs/NOTATION.md`,
complete `docs/observable_p1.md`, `docs/global_nonlinear.md` C.4.7.9 and
C.4.7.10 B/C.1/D.3, and the complete study-owned
`three_coordinate_candidate.md` and `perturbation_modes.md`. References in
those study reports to other research artifacts were not followed. The
investigate-conjectures and solve-math-rigorously skills govern this report.

The result is an exact finite-horizon differentiability theorem and a complete
bilinear second-variation system for all six input tangent coordinates. It
retains the canonical frozen dictionary, Gaussian marks, initial matrix,
physical metric, and evolution of every entry of the middle matrix. It also
gives a global obstruction to a Hessian of one sign. That obstruction does
not refute local perturbative stability or the candidate's symmetric
Lyapunov inequality.

## 1. Contract and theorem

Use the exact d=3 p=1 initialization in the candidate: bounded normalized
columns b_1 in R^7 and b_2 in R^4, the joint lower Gaussian mark g in R^3,
the prescribed eta=1/4096, and the prescribed 4-by-7 matrix D. These marks
and D are independent of the training data and remain fixed when the data
vary. Explicitly, for a standard scalar Gaussian G set

\[
 \mathfrak v=E\tanh^2G,\quad
 \tau=E\tanh^2(\sqrt{\mathfrak v}G),\quad \alpha=1-\tau.
\]

On the lower population let g_i be independent standard Gaussians and
zeta_i be independent N(0,tau), independent of g. On the separate upper
population let xi_i be independent N(0,mathfrak v). Put

\[
 h_i^0=\tanh g_i,\quad k_i^0=\tanh(\zeta_i+\alpha h_i^0),
 \quad Z_i^0=\tanh\xi_i,\quad
 \beta=E[h_i^0k_i^0],\quad\sigma=E[(k_i^0)^2],\quad\gamma=1-\sigma,
\]
\[
 R_h=\sqrt{\mathfrak v+\eta},\quad
 R_k=\sqrt{\sigma+\eta-\beta^2/(\mathfrak v+\eta)},\quad
 R_Z=\sqrt{\tau+\eta},\qquad\eta=1/4096,
\]
\[
 b_1=\left((1+\eta)^{-1/2},h^0/R_h,
       [k^0-\beta h^0/(\mathfrak v+\eta)]/R_k\right)^T,
 \quad b_2=\left((1+\eta)^{-1/2},Z^0/R_Z\right)^T.
\]

The only nonzero entries of D are

\[
 D_{Z_i,h_i}=\frac{\alpha\mathfrak v}{R_hR_Z},\qquad
 D_{Z_i,k_i}=\frac{\alpha\beta\eta/(\mathfrak v+\eta)+\tau\gamma}
                    {R_kR_Z}.
\]

Thus the lower forward/reverse correlation and the reverse-response term
tau gamma are retained. Write B_l=ess sup |b_l| and d_0=||D||op. The normalization gives
||E_l[b_l V]||<=||V||_2. Both populations and their expectations are separate.

The original unit inputs u_i have labels y=(1,1,-1), weights 1/3, and
physical inputs x_i=sqrt(3)u_i. Put v_i=y_i u_i. Oddness gives signed
predictions m_i=y_i f(u_i)=f(v_i), all with target one. This change preserves
all three input degrees of freedom. The reference is

\[
 v_1=(a,b,b),\quad v_2=(b,a,b),\quad v_3=(b,b,a),
 \qquad a^2+2b^2=1,\quad a\ne b.
\]

The state X=(w,c,M) has physical metric

\[
 \|\dot X\|^2=E_1|\dot w|^2+E_2|\dot c|^2+\|\dot M\|_F^2,
 \qquad X(0)=(g,0,D).
\]

For a triple V=(v_1,v_2,v_3), define along its own trained solution

\[
 F=\tfrac13\sum_i m_i,\quad q=E_2c^2,\quad
 \mathcal L=\tfrac13\sum_i(m_i-1)^2,\quad
 U_0(V)=\tfrac13\sum_i H^2_{X(0)}(v_i),\quad
 C_0(V)=E_2U_0(V)^2,
\]
\[
 A(F,q,C_0)=1+\frac{C_0(1+q)}{C_0+F^2},\qquad
 \Phi(t,V)=\mathcal L(t,V)A(F(t,V),q(t,V),C_0(V)).       \tag{1}
\]

Here C_0 is constant in physical time for each dataset, but changes under
data variation. In contrast, Section 3 of `perturbation_modes.md` held the
reference C_0 fixed while changing the dataset. Those are two distinct
functions away from the reference; Section 5 below includes the additional
terms for (1).

**Theorem.** For every finite T, the characteristic solution map from
(S^2)^3 to C([0,T];L^2(Omega_1;R^3) x L^infinity(Omega_2) x R^(4x7))
is twice continuously differentiable. In any bounded local sphere chart its
second-order Taylor remainder is O_T(|epsilon|^3) in this displayed norm.
Its first and mixed second derivatives are the unique solutions of
(5)–(11) below, with zero initial state derivatives. All predictions,
the tangent Gram, and (1) are twice continuously differentiable, and their
derivatives are (12)–(17). The second chart derivative at the chart center
is the Riemannian Hessian for the product of ordinary unit-sphere metrics.

The theorem holds at every unit triple, not only at the symmetric reference.
Moreover C_0(V)>0 for every V, so (1) is globally defined. The differentiability
and remainder bounds concern each fixed T; their constants are not asserted
uniform as T tends to infinity. No C^2 map from an unrestricted L^2 state
ball into itself is assumed. Sections 6–7 prove the regularity and the
strict positivity assertion.

## 2. Six independent tangent coordinates and sphere curvature

Choose any orthonormal basis e_{i1},e_{i2} of T_{v_i}S^2. For the original
inputs the corresponding basis is y_i e_{i1},y_i e_{i2}. Define the six
independent coordinates by

\[
 v_i(\epsilon)=\frac{v_i+\epsilon_{i1}e_{i1}+
                        \epsilon_{i2}e_{i2}}
 {|v_i+\epsilon_{i1}e_{i1}+\epsilon_{i2}e_{i2}|}.       \tag{2}
\]

For arbitrary tangent directions eta=(eta_i) and theta=(theta_i), use
the two-parameter restriction epsilon=s eta+t theta, interpreting these
as tangent vectors in the selected bases. At s=t=0,

\[
 v_{i,\eta}=\eta_i,\qquad v_{i,\theta}=\theta_i,\qquad
 v_{i,\eta\theta}=\kappa_i:=-(\eta_i\cdot\theta_i)v_i.  \tag{3}
\]

Thus eta and theta supported at different samples give kappa_i=0 for
every i; directions within one sample include its normal curvature.
An exponential chart has the same two derivatives. The tangential part
of the acceleration in (3) vanishes, so these are normal coordinates
to second order and scalar mixed derivatives equal the intrinsic Hessian.
Dropping kappa_i computes an ambient affine-input Hessian instead.

## 3. Full forward, backward, and gradient variations

Use subscripts eta, theta, eta theta for total data derivatives, including
the response of X. All unadorned quantities are evaluated at the base data
and its trained state at the same physical time. Let phi=tanh and put

\[
 p_i=w\cdot v_i,\quad h_i=\phi(p_i),\quad t_i=\phi'(p_i),
 \quad a_i=E_1[b_1h_i],
\]
\[
 Z_i=b_2^TMa_i,\quad H_i=\phi(Z_i),\quad s_i=\phi'(Z_i),
 \quad d_i=E_2[b_2c s_i],\quad Q_i=b_1^TM^Td_i,
 \quad m_i=E_2[cH_i].                                    \tag{4}
\]

For explicit gates, phi''(z)=-2 phi(z)phi'(z) and
phi'''(z)=4 phi(z)^2 phi'(z)-2 phi'(z)^2. These and all other fixed-order
tanh derivatives used below are bounded on the real line.

The lower preactivation derivatives retain input/state mixed terms:

\[
 p_{i,\eta}=w_\eta\cdot v_i+w\cdot\eta_i,
\]
\[
 p_{i,\eta\theta}=w_{\eta\theta}\cdot v_i
       +w_\eta\cdot\theta_i+w_\theta\cdot\eta_i
       +w\cdot\kappa_i.                                  \tag{5}
\]

The complete lower-layer rules are

\[
 h_{i,\eta}=t_i p_{i,\eta},\qquad
 h_{i,\eta\theta}=t_i p_{i,\eta\theta}
                   +\phi''(p_i)p_{i,\eta}p_{i,\theta},
\]
\[
 t_{i,\eta}=\phi''(p_i)p_{i,\eta},\qquad
 t_{i,\eta\theta}=\phi''(p_i)p_{i,\eta\theta}
                   +\phi'''(p_i)p_{i,\eta}p_{i,\theta},
 \qquad a_{i,J}=E_1[b_1h_{i,J}].                           \tag{6}
\]

Here and below J can be eta, theta, or eta theta whenever the displayed
operation is linear. The upper-layer rules are

\[
 Z_{i,\eta}=b_2^T(M_\eta a_i+M a_{i,\eta}),
\]
\[
 Z_{i,\eta\theta}=b_2^T(M_{\eta\theta}a_i
       +M_\eta a_{i,\theta}+M_\theta a_{i,\eta}
       +M a_{i,\eta\theta}),
\]
\[
 H_{i,\eta}=s_iZ_{i,\eta},\qquad
 H_{i,\eta\theta}=s_iZ_{i,\eta\theta}
                    +\phi''(Z_i)Z_{i,\eta}Z_{i,\theta},
\]
\[
 s_{i,\eta}=\phi''(Z_i)Z_{i,\eta},\qquad
 s_{i,\eta\theta}=\phi''(Z_i)Z_{i,\eta\theta}
                    +\phi'''(Z_i)Z_{i,\eta}Z_{i,\theta}.
                                                               \tag{7}
\]

The reverse rules, with the actual transpose of that same M, are

\[
 d_{i,\eta}=E_2[b_2(c_\eta s_i+c s_{i,\eta})],
\]
\[
 d_{i,\eta\theta}=E_2[b_2(c_{\eta\theta}s_i
       +c_\eta s_{i,\theta}+c_\theta s_{i,\eta}
       +c s_{i,\eta\theta})],
\]
\[
 Q_{i,\eta}=b_1^T(M_\eta^Td_i+M^Td_{i,\eta}),
\]
\[
 Q_{i,\eta\theta}=b_1^T(M_{\eta\theta}^Td_i
       +M_\eta^Td_{i,\theta}+M_\theta^Td_{i,\eta}
       +M^Td_{i,\eta\theta}),
\]
\[
 m_{i,\eta}=E_2[c_\eta H_i+cH_{i,\eta}],
\]
\[
 m_{i,\eta\theta}=E_2[c_{\eta\theta}H_i
       +c_\eta H_{i,\theta}+c_\theta H_{i,\eta}
       +cH_{i,\eta\theta}].                              \tag{8}
\]

In the physical metric the prediction gradient g_i has blocks
g_i^c=H_i, g_i^M=d_i a_i^T, g_i^w=t_iQ_i v_i. Product differentiation gives

\[
 g_{i,\eta}^c=H_{i,\eta},\qquad
 g_{i,\eta}^M=d_{i,\eta}a_i^T+d_i a_{i,\eta}^T,
\]
\[
 g_{i,\eta}^w=(t_{i,\eta}Q_i+t_iQ_{i,\eta})v_i+t_iQ_i\eta_i,
\]
\[
 g_{i,\eta\theta}^c=H_{i,\eta\theta},
\]
\[
 g_{i,\eta\theta}^M=d_{i,\eta\theta}a_i^T
       +d_{i,\eta}a_{i,\theta}^T+d_{i,\theta}a_{i,\eta}^T
       +d_i a_{i,\eta\theta}^T,
\]
\[
 \begin{split}
 g_{i,\eta\theta}^w={}&(t_{i,\eta\theta}Q_i
       +t_{i,\eta}Q_{i,\theta}+t_{i,\theta}Q_{i,\eta}
       +t_iQ_{i,\eta\theta})v_i\\
 &+(t_{i,\eta}Q_i+t_iQ_{i,\eta})\theta_i
  +(t_{i,\theta}Q_i+t_iQ_{i,\theta})\eta_i+t_iQ_i\kappa_i.
 \end{split}                                               \tag{9}
\]

For residual r_i=m_i-1 the actual flow and both response equations are

\[
 \dot X=-\tfrac23\sum_i r_i g_i,
 \qquad
 \dot X_\eta=-\tfrac23\sum_i(m_{i,\eta}g_i+r_i g_{i,\eta}),
 \qquad X_\eta(0)=0,                                     \tag{10}
\]
\[
 \dot X_{\eta\theta}=-\tfrac23\sum_i
  (m_{i,\eta\theta}g_i+m_{i,\eta}g_{i,\theta}
      +m_{i,\theta}g_{i,\eta}+r_i g_{i,\eta\theta}),
 \qquad X_{\eta\theta}(0)=0.                             \tag{11}
\]

Although the recurrences contain X_eta and X_eta theta on their right
sides, (10) is affine linear in X_eta, and (11) is affine linear in
X_eta theta once the base and first responses are known. Thus this is a
triangular response system, not a prescription to differentiate unknown
solutions. Taking the six basis directions gives six first responses and
21 symmetric second responses, including every mixed-sample entry.
Neither M nor its variations are constrained to their initialized bands.

## 4. Observable derivatives and the frozen-state distinction

All pairings in this section are physical-metric pairings. For the full
tangent Gram G_ij=<g_i,g_j>,

\[
 G_{ij,\eta}=\langle g_{i,\eta},g_j\rangle
                  +\langle g_i,g_{j,\eta}\rangle,
\]
\[
 G_{ij,\eta\theta}=\langle g_{i,\eta\theta},g_j\rangle
       +\langle g_{i,\eta},g_{j,\theta}\rangle
       +\langle g_{i,\theta},g_{j,\eta}\rangle
       +\langle g_i,g_{j,\eta\theta}\rangle.              \tag{12}
\]

The scalar derivatives needed for (1) are

\[
 F_J=\tfrac13\sum_i m_{i,J},\qquad
 q_\eta=2E_2[c c_\eta],\qquad
 q_{\eta\theta}=2E_2[c_\eta c_\theta+c c_{\eta\theta}],
\]
\[
 \mathcal L_\eta=\tfrac23\sum_i r_i m_{i,\eta},\qquad
 \mathcal L_{\eta\theta}=\tfrac23\sum_i
      (m_{i,\eta}m_{i,\theta}+r_i m_{i,\eta\theta}).      \tag{13}
\]

For C_0, use only the initialized hidden-field derivatives, computed by
(5)–(7) with w=g, M=D, and every state variation set to zero. Write
U_{0,J}=sum_i H_{i,J}(0)/3. Then

\[
 C_{0,\eta}=2E_2[U_0U_{0,\eta}],\qquad
 C_{0,\eta\theta}=2E_2[U_{0,\eta}U_{0,\theta}
                                  +U_0U_{0,\eta\theta}]. \tag{14}
\]

These are initialization integrals available before training. No D or
dictionary derivative is added: those canonical objects do not depend
on the input triple.

For comparison, the *fixed-state* sphere derivatives at an arbitrary
current X set every state variation to zero in (5)–(9). For one input,
put

\[
 A_\eta=E_1[b_1t(w\cdot\eta)],\quad
 A_{\eta\theta}=E_1[b_1\{t(w\cdot\kappa)
                +\phi''(w\cdot v)(w\cdot\eta)(w\cdot\theta)\}],
 \quad z_\eta=b_2^TM A_\eta.
\]

Its frozen-state prediction Hessian is exactly

\[
 \operatorname{Hess}_{v}f[\eta,\theta]
  =E_2[c\{s b_2^TM A_{\eta\theta}
                 +\phi''(Z)z_\eta z_\theta\}].          \tag{15}
\]

The first term includes the sphere's normal acceleration. This Hessian is
block diagonal in the sample index for the individual outputs. The trained
output Hessian (8) also includes w_eta theta, c_eta theta, M_eta theta,
both cross terms between first state responses, and both state/input mixed
terms. It is generally not block diagonal. Even a sign or norm estimate for
(15) alone therefore does not estimate the trained Hessian.

## 5. Complete Hessian of the mixed potential

In this section let C stand for the scalar argument C_0, and d=C+F^2.
Partial derivatives of the multiplier A in (1) are

\[
 A_F=-\frac{2C(1+q)F}{d^2},\quad A_q=\frac C d,
 \quad A_C=\frac{(1+q)F^2}{d^2},
\]
\[
 A_{FF}=\frac{2C(1+q)(3F^2-C)}{d^3},\quad
 A_{Fq}=-\frac{2CF}{d^2},\quad
 A_{FC}=\frac{2(1+q)F(C-F^2)}{d^3},
\]
\[
 A_{qq}=0,\qquad A_{qC}=\frac{F^2}{d^2},\qquad
 A_{CC}=-\frac{2(1+q)F^2}{d^3}.                          \tag{16}
\]

Write z=(F,q,C_0). With these partials and (13)–(14), the complete
first and second derivatives are

\[
 A_\eta=\sum_j A_j z_{j,\eta},\qquad
 A_{\eta\theta}=\sum_j A_j z_{j,\eta\theta}
                      +\sum_{j,k}A_{jk}z_{j,\eta}z_{k,\theta},
\]
\[
 \Phi_\eta=A\mathcal L_\eta+\mathcal L A_\eta,
\]
\[
 \operatorname{Hess}\Phi[\eta,\theta]
  =A\mathcal L_{\eta\theta}
    +\mathcal L_\eta A_\theta+\mathcal L_\theta A_\eta
    +\mathcal L A_{\eta\theta}.                         \tag{17}
\]

Every C_0 derivative and every mixed F/q/C_0 term is present. Setting
C_{0,eta}=C_{0,eta theta}=0 gives the distinct convention of holding the
reference normalization fixed. Formula (17), evaluated on all six tangent
basis pairs, gives the complete symmetric 6-by-6 matrix.

## 6. Why these are actual derivatives with unbounded Gaussian marks

The following proof supplies the differentiability used above; formal
product rules alone would not suffice.

First, bounded b, bounded tanh gates and their Lipschitz constants give
local existence in bounded (w-g,c,M), by contraction of the integrated
vector field on a sufficiently short interval. Direct gradient
differentiation gives dot L=-||dot X||^2. Since L(0)=1, the mean absolute
residual is at most one. The contraction property of the feature maps then
gives, for all unit triples,

\[
 \|c(t)\|_\infty\le2t,\quad
 \|M(t)\|_{op}\le d_0+2t^2,\quad
 \|w(t)-g\|_\infty\le B_1(2d_0t^2+2t^4).              \tag{18}
\]

Indeed |a_i|<=1, |d_i|<=||c||_2, and
|Q_i|<=B_1||M||op||c||_2. Integrating the c, M, and w speed bounds in that
order proves (18). Bounded speeds give a Cauchy limit at any putative
finite maximal endpoint; local contraction at that limit continues the
solution. This proves global characteristic existence, with bounds uniform
over the compact input space on each fixed horizon.

Put rho(g)=1+|g| and, for integers k>=1, introduce only for the proof

\[
 \|(W,C,N)\|_{E_k}
 =\operatorname*{ess\,sup}_{\Omega_1}\frac{|W|}{\rho^k}
                 +\|C\|_\infty+\|N\|_F.                \tag{19}
\]

These are complete weighted supremum spaces. Every moment E_1 rho^j is
finite: radial integration of a polynomial times exp(-|g|^2/2) converges.
Thus E_k embeds continuously in the physical Hilbert space, and a lower
field bounded by C rho^k is integrable at every finite power.

Let B(X,V) denote the right side of the base equation (10). On a region
where c and M are bounded, and for fixed V, subtracting each factor in
(4) shows

\[
 \|B(X,V)-B(\widetilde X,V)\|_{E_k}
                    \le L_{T,k}\|X-\widetilde X\|_{E_k}. \tag{20}
\]

The constant does not require a supremum bound on w. For example the
lower gate difference is at most 2|w-w_tilde|, while
|a_i-a_i_tilde|<=B_1 E_1|w-w_tilde|
<=B_1 E_1 rho^k ||w-w_tilde||_{E_k}. Upper quantities are finite
contractions of this difference; Q_i and Q_i_tilde are bounded because
c and M are bounded. The row product t_iQ_i therefore satisfies (20).
The same argument handles residuals and the c/M equations.

Allowing V to vary in a bounded chart, (18) gives
|w dot (v_i-v_i_tilde)|<=C_T rho |V-V_tilde|.
Integral comparison using (20) for k=1 proves

\[
 \sup_{t\le T}\|X(t,V)-X(t,\widetilde V)\|_{E_1}
                                      \le C_T|V-\widetilde V|. \tag{21}
\]

The candidate linear first-response equation has coefficients bounded on
every E_k: the only pointwise multipliers of its unknown row field are
bounded gates and Q_i, and the remaining row dependence is integrated
against bounded b_1. Its input source is bounded by C_T rho. Successive
integration of this affine linear equation converges on short intervals
as in the base contraction argument; the exponential integrating-factor
estimate extends it through T. The resulting bound is

\[
 |w_\eta(t,g)|\le C_T\rho(g)|\eta|,\quad
 \|c_\eta(t)\|_\infty+\|M_\eta(t)\|_F\le C_T|\eta|.
                                                               \tag{22}
\]

The second-response equation has that same homogeneous state operator.
All its new sources are either curvature terms w dot kappa_i, products
of two first preactivation variations, or products of bounded upper
responses. By (18),(22) they are bounded in E_2 by C_T|eta||theta|.
The same linear integral argument therefore gives

\[
 |w_{\eta\theta}(t,g)|\le C_T\rho(g)^2|\eta||\theta|,
 \quad\|c_{\eta\theta}(t)\|_\infty+
       \|M_{\eta\theta}(t)\|_F\le C_T|\eta||\theta|.     \tag{23}
\]

To identify these candidate derivatives with actual ones, form the degree
two state polynomial in the six chart coordinates from (22)–(23), denoted
X_hat(epsilon). Its row increment over X is at most
C_T(|epsilon|rho+|epsilon|^2 rho^2). The lower preactivation increment has
the same bound, including the chart's Taylor terms. The ordinary scalar
Taylor theorem, with bounded third derivatives of tanh and its gate,
bounds the discarded gate terms by
C_T|epsilon|^3 rho^6 for |epsilon|<=1. The chart remainder contributes
at most this amount as well. Every lower contraction integrates this
bound using E_1 rho^6<infinity; all upper factors and the approximating
c/M blocks remain bounded. Subtracting finite products then proves the
actual equation defect

\[
 \sup_{t\le T}\|\partial_tX_{hat}(t,\epsilon)
             -B(X_{hat}(t,\epsilon),V(\epsilon))\|_{E_6}
                                  \le C_T|\epsilon|^3.  \tag{24}
\]

The coefficients of degree zero, one, and two cancel precisely by
(10)–(11). Both the true and approximating c/M blocks lie in one bounded
set. Apply (20) with k=6 to their integral equations, noting their equal
initial states. Multiplication by exp(-L_{T,6}t), followed by integration,
gives sup_t||X-X_hat||_{E_6}<=C_T|epsilon|^3. Embedding E_6 into L^2
proves the stated Taylor remainder. This is a proof estimate; it does
not change the metric or truncate any Gaussian marks.

Continuity of the derivatives is also needed. Subtract the first-response
equations at nearby base data and use (21): a changed lower gate contributes
O(|V-V_tilde|rho), multiplying a first row response O(rho), hence belongs
to E_2 with norm O(|V-V_tilde|). The remaining contractions obey the same
bound. The integral inequality gives continuity of first responses in E_2.
In the second-response subtraction, multiplying a second row response
O(rho^2) by the changed gate costs at most rho^3. Differences of products
of two first responses also cost at most rho^3. Thus the same estimate
gives continuity of second responses in E_3. These spaces embed in L^2;
finite-dimensional chart directions give continuous bilinear derivatives.
This proves C^2, not just directional differentiability at one point.

Finally, (22)–(23), bounded b, and finite Gaussian moments dominate every
integrand in (6)–(17), including products in (12). Differentiation under
expectation and uniform-time passage follow from the displayed bounds
and the integral remainders. At no step is multiplication of two arbitrary
L^2 functions asserted to be bounded in L^2.

## 7. Structural consequences and precise obstructions

### 7.1 Positive C_0 does not prevent a disagreement obstruction

The candidate proves the exact initialized representation

\[
 H_0(v)=\tanh(Z\cdot k(v)),\qquad
 k(v)=(\kappa(v_1),\kappa(v_2),\kappa(v_3)),             \tag{25}
\]

where the raw upper mark Z has positive density on (-1,1)^3 and kappa is
odd and strictly increasing. Consequently k(v) is nonzero for every unit v.
If C_0(V)=0, continuity and positive density imply
sum_i tanh(Z dot k(v_i))=0 throughout that cube. Choose a vector z outside
the three planes k(v_i) dot z=0. On a small interval of real r the function
sum_i tanh(r z dot k(v_i)) vanishes. It is real analytic on the real line,
so it vanishes there: at any finite endpoint of an interval of equality
all derivatives vanish by continuity, and its convergent local power
series extends the interval. But as r tends to positive infinity its
limit is a sum of three numbers in {+1,-1}, which cannot be zero.
This contradiction proves C_0(V)>0 for every unit triple. Dominated
convergence gives continuity in V, so compactness supplies a positive
minimum over (S^2)^3. No numerical lower bound for this minimum is claimed.

This globally positive scalar normalization does not control every residual
mode. At the admissible triple (v,v,-v), any odd predictor has predictions
(z,z,-z), hence

\[
 \mathcal L=\tfrac13\{2(z-1)^2+(-z-1)^2\}
                  =(z-\tfrac13)^2+\tfrac89\ge\tfrac89. \tag{26}
\]

The scalar C_0 is still positive. Thus an all-data fitting theorem or an
all-data inequality dot Phi<=-lambda Phi with lambda>0 is impossible.
This obstruction uses a finite, large data change; it does not exclude
fitting in a small neighborhood of the non-antipodal symmetric triple.

### 7.2 The trained Hessian has no global semidefinite sign

Initially c=0 and all state data derivatives vanish. The base velocities
are dot c(0)=2U_0, dot w(0)=dot M(0)=0. Therefore

\[
 F(0,V)=q(0,V)=0,\quad \mathcal L(0,V)=1,\quad
 \Phi(0,V)=2,\quad \partial_t\Phi(0,V)=-8C_0(V).         \tag{27}
\]

The response equations also give dot c_eta(0)=2U_0,eta and
dot c_eta theta(0)=2U_0,eta theta. Differentiating (27) using the
proved response regularity yields, at every fixed V,

\[
 \operatorname{Hess}_V\Phi(t,V)
             =-8t\operatorname{Hess}_V C_0(V)+o(t).       \tag{28}
\]

The little-o is in the ordinary finite-dimensional bilinear norm.
It follows by integrating the continuous time derivative of the response
formula at t=0. No all-time Taylor series is asserted.

For a unit v, C_0(v,v,v)=E_2H_0(v)^2, whereas
C_0(v,v,-v)=E_2H_0(v)^2/9. These are unequal. Equation (27) makes
Phi(t,.) nonconstant for every sufficiently small positive t. A C^2
nonconstant scalar function on (S^2)^3 cannot have an everywhere positive
semidefinite or everywhere negative semidefinite Hessian. To prove this
directly, hold two inputs fixed and restrict the third to a unit-speed
great circle. Its second derivative equals the relevant Hessian value.
A periodic twice differentiable function with nonnegative second
derivative has zero integral of that derivative and is constant; the
nonpositive case is identical. If the Hessian had either sign everywhere,
the function would be constant on every such circle and therefore
independent of each of its three inputs, a contradiction.

Consequently at every sufficiently small positive time there is a
positive sphere-Hessian direction somewhere and a negative direction
somewhere. Each can be chosen to perturb just one input. This refutes
global data convexity/concavity of this witness, not its time dissipation.
It does not determine the sign at the selected symmetric reference.

### 7.3 What symmetry removes, and what survives at second order

At the symmetric triple, simultaneous coordinate and sample permutations
act on tangent matrices eta=(eta_{ij}) by eta -> P eta P^T. The candidate's
measure-preserving permutation isometries fix initialization and preserve
the full physical flow. Thus F,q,C_0,L,Phi are invariant scalar functions
of the data under this action, including their trained state response.

The invariant tangent matrices have common diagonal x and common off-diagonal
y, with ax+2by=0. This is a one-dimensional space. Let Pi be the average
over all six permutation actions. For every invariant scalar J,

\[
 DJ[\eta]=DJ[\Pi\eta].                                  \tag{29}
\]

Hence first variations of F,q,C_0,L,Phi vanish on the five-dimensional
kernel of Pi. They need not vanish on the remaining direction. In
particular a generic independent perturbation has a first-order mean
effect; describing every perturbation as purely transverse is incorrect.

For completeness, the invariant direction is spanned by the matrix with
diagonal -2b and off-diagonal a. A distinct one-dimensional alternating
direction is spanned by

\[
 \begin{pmatrix}0&1&-1\\-1&0&1\\1&-1&0\end{pmatrix}.     \tag{30}
\]

It is tangent because each row's off-diagonal entries sum to zero, and
conjugation by P multiplies it by det P. Averaging with the sign character
projects onto this line: a matrix transforming by that character has zero
diagonal, since a transposition fixes each chosen diagonal position; the
same transpositions force opposite off-diagonal entries and equate the
three cyclic entries. Any Hessian of an invariant scalar has no cross
terms between this line, the invariant line, and their orthogonal
four-dimensional complement: average the corresponding bilinear pairing
over permutations. No sign follows for any of these restrictions. This
block separation does not impose arbitrary rotational invariance of the
dictionary.

Write e=1-F and delta_i=m_i-F. At the symmetric state delta=0. Put
D_{eta,i}=m_{i,eta}-F_eta. From L=e^2+|delta|^2/3 one obtains

\[
 \mathcal L_{\eta\theta}
 =2F_\eta F_\theta-2eF_{\eta\theta}
                       +\tfrac23\sum_i D_{\eta,i}D_{\theta,i}. \tag{31}
\]

For eta,theta in ker Pi, all first invariant scalar variations vanish.
Combining (16)–(17) with (31) gives the particularly informative exact
restriction

\[
 \begin{split}
 \operatorname{Hess}\Phi[\eta,\theta]
 ={}&\tfrac{2A}{3}\sum_i D_{\eta,i}D_{\theta,i}
       +(-2Ae+e^2A_F)F_{\eta\theta}\\
    &+e^2 A_q q_{\eta\theta}+e^2 A_C C_{0,\eta\theta}.
 \end{split}                                               \tag{32}
\]

The first term is positive semidefinite: it is the newly produced
disagreement. The remaining terms involve the second trained mean and
readout responses, and the sphere Hessian of initialization. They have
no sign supplied by the Gram's positivity. Even a purely non-invariant
first perturbation can therefore feed back into mean observables at
second order. Ignoring the second state response deletes precisely this
effect.

## 8. Claim boundary

Proved here: actual C^2 finite-horizon trained dependence with a controlled
second-order remainder; all first, second, mixed, curvature, and C_0
terms; strict positivity of C_0 over all three-input sphere data; exact
symmetry cancellations; and the stated global fitting and Hessian-sign
obstructions. No experiment was used.

Not proved: an all-time bound on these response fields, transverse tangent
coercivity along nearby training paths, a sign for (32) at the reference,
or a perturbed Lyapunov inequality. The compact-time Taylor constants can
grow with T, so these derivatives cannot by themselves justify a fixed
perturbation radius valid for infinite training time. A data Hessian
controls variation across datasets; a Lyapunov derivative controls motion
in physical time. Converting one into the other requires an additional
uniform dynamical estimate. None of these p=1 conclusions identifies a
general-d trained-network limit or supplies closure-order accuracy.
