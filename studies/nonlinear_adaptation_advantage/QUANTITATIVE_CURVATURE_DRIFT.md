# Quantitative drift of the reached prediction-kernel derivative

Root continuation, 2026-09-12. Status: frozen candidate for internal check.
This supplements, without changing, the frozen initial routes and families.
It addresses the unevaluated time modulus in G20. It supplies no favorable
curvature sign and is not a successful E₀ theorem.

Inputs are the complete already read C.4.9–C.4.10, C.4.5.1 reference,
C.4.5.2 and III.F source construction, and the frozen study geometry report.
Source hashes remain those in SOURCE_AND_CHECK_RECORD.md. The additional
argument below uses an appended forward query and the existing *first*
named-source pulse bounds. It makes no Lp operator assertion about A0,
does not replace its actual adjoint, and never restarts finite training.

## 1. A fourth-moment bound for upper directional preactivations

Use the book's H=L_src, source-row cap B, and q4 from NSC17, uniformly
over the source-admissible histories under consideration. The cap B applies
to every historical and current backward row, not just the endpoint row.
Set q2=q4 as a
conservative L2 bound for every historical or current backward query, and
put

    D=B+H³,
    E_p=2^(1/p) exp(3DH+2pH⁴),      p=1,2,
    C_alpha=1+4H E_2 q2+D H E_1,
    U4=H+3^(1/4)q2+H C_alpha+H²q2.                         (Q1)

These constants are finite, independent of support size and time mesh,
and potentially extremely impractical. B is the source cap furnished by
C.4.9 proof unit A, not a newly assumed bound on a differentiated program.

At any reached state let b be a deterministic linear combination of its
full raw gradients, with sum/integral of absolute coefficients at most M.
This includes anchor-projected gradient combinations: their two anchor
coefficients are included in M. For |u|=1 define

    F_u(b)=phi'(w.u)(b_w.u),
    V_u(b)=b_K H1(u)+A F_u(b),       A=A0+K.

Then the new estimate is

    ||V_u(b)||4 <= M U4.                                   (Q2)

Here M=0 gives zero. The statement is homogeneous in b and applies to
signed coefficients. No special residual or label sign is used.

### Finite-program derivation with all named sources retained

First take a finite raw Euler history. Append all current forward/reverse
queries needed for b, with their distinct names, and then the single new
forward query with input F_u(b). The coefficients of b are deterministic
at this program and are held fixed in named differentiation. They are not
random coordinate functions or derivatives of feedback coefficients.

For an old reverse-source name p, CT29 gives

    max_j |partial_(zeta_p) w_j| <= |gamma_p| E,
    E=exp(DH+2Z),       Z=sum_old |gamma_j||Q_j|.

CT28 gives ||E||p<=E_p in (Q1). Current backward answers have no effect
on the already constructed w. In the source formula

    Q_i=zeta_i+sum_j D_ij H1_j,

the row sum of |D_ij| is at most D; all deterministic coefficients and
covariances are frozen in the named derivative. Differentiating b_w
therefore has precisely three kinds of terms: its outside first-layer
gate, the direct current zeta_i injection, and the past-feature memory.
Summing expectations of their absolute values over source names bounds
them respectively by

    2 M H E_2 q2,       M,       M D H E_1.

The first bound is Cauchy–Schwarz on the pulse envelope and Q_i followed
by the deterministic sums of update/coefficient masses. The last uses
the D-row sum before summing past pulse masses. In particular, the many
current direct injections cost sum_i |a_i|<=M, not the number of queries.

Differentiating the additional outside gate in F_u(b) costs a further
2 M H E_2 q2, since ||b_w||2<=M q2. Hence

    sum_p |E partial_(zeta_p) F_u(b)| <= M C_alpha.          (Q3)

III.F and the fixed-program extension A.2 give exactly

    A0 F_u(b)=xi_F+sum_p alpha_(F,p) delta_p,
    Var(xi_F)=||F_u(b)||2² <= M²q2²,
    alpha_(F,p)=E partial_(zeta_p) F_u(b).

Every reverse input here is an ordinary old or current delta_p, bounded
pointwise by H. There is no differentiated reverse query. Thus (Q3) and
the Gaussian fourth moment give

    ||A0 F_u(b)||4 <= M[3^(1/4)q2+H C_alpha].              (Q4)

The original initialized middle action is still the same A0. Its bounded
operator norm alone would not prove (Q4); the named-source calculation is
essential. The explicit learned increment has a rank integral with total
historical coefficient mass at most H, bounded upper factors |delta|<=H,
and lower factors of L2 norm at most one. Consequently

    |K F_u(b)| <= H² ||F_u(b)||2,
    |b_K H1(u)| <= MH

pointwise on the upper probability space. Adding these estimates proves
(Q2) at the finite program.

### Passage to reached curves and arbitrary coefficient measures

Use the same source-admissible Euler refinements and spatial quadratures
that construct the actual selected curve. At fixed states, continuous
gradient queries converge in raw L2, and their uniform higher moments make
first-row directions converge in L4 by interpolation. Multiplication by
bounded phi' then makes F_u(b) converge in L2. The common bounded action
and convergence of K and b_K give convergence of V_u(b) in L2. The
uniform fourth-moment bound passes by an almost-sure subsequence and Fatou.

For a coefficient v in L2(p rho), first approximate it by bounded continuous
functions in that measure and then by spatial quadratures. This density
follows, for the bounded positive densities of the fixed families, by step
approximation and continuous ramps on finitely many intervals. Signed
coefficient mass is bounded by ||v||_(L2(p rho)); use Cauchy–Schwarz.
The same L2 passage applies and preserves (Q2). No L4 convergence of the
upper directional query is presumed. Its L4 *bound* is the conclusion.

## 2. Constants for all projected force directions

Fix a member of one of the declared families and its common selected episode.
Let mathsf H=L2(p rho), and define the full projected force map

    D_t v=integral v(u) Pi_(theta_t) g_(theta_t)(u) p d rho.

The symbol D_t in this formula is an operator, not NSC26's scalar constant.
Below write Z_dot, Delta_dot, Q_dot for NSC26's Z_t,D_t,Q_t respectively.
All other constants retain the book's names. Put

    m_d=1+2L/sqrt(k),
    J=A_s T_g(1+4L/sqrt(k)),
    Z2f=(1+a_b)L,       Z4f=m_d U4,       W4f=m_d q4,
    Vw2=A_s a_b c_b,    Vw4=A_s q4,       VK=A_s c_b,
    Vc=A_s,            Vz=A_s Z_dot,
    Vdelta=A_s Delta_dot,                VQ=A_s Q_dot,
    VF=J+2 Vw4 W4f,
    VV=J+L Vw2+VK L+a_b VF.                               (Q5)

For any fixed v in mathsf H with ||v||<=1, write x_t=D_t v. Since
||GM^-1||<=sqrt(2/k), the anchor multiplier beta_t(v) satisfies

    ||beta_t(v)||1<=2L/sqrt(k).

Thus x_t is a gradient combination of coefficient mass at most m_d.
The book's first derivative estimates and the exact projector derivative
give the following uniform bounds, for h=|t-s|:

    ||x_t||raw<=L,              ||x_t-x_s||raw<=J h,
    ||x_(t,c)||infty<=m_d,      ||x_(t,w)||4<=W4f,
    ||V_u(x_t)||2<=Z2f,         ||V_u(x_t)||4<=Z4f,
    ||F_u(x_t)-F_u(x_s)||2<=VF h,
    ||V_u(x_t)-V_u(x_s)||2<=VV h.                          (Q6)

The penultimate bound follows by subtracting the direction and the gate,
using ||w_t-w_s||4<=Vw4 h. For the last bound subtract the four factors in
x_K H1+A F: the costs are J, L Vw2, VK L and a_b VF. The raw derivative
bound J is G9; it requires no second derivative. The state differences
in w, K, c, Z2, delta and Q are bounded by the corresponding V constants
in (Q5) times h, directly from NSC25–NSC28. In particular the c difference
is bounded in supremum norm even though no L-infinity derivative theorem
is invoked: integrate its bounded pointwise velocity.

## 3. Lipschitz variation of scalar Hessian forms on force directions

For gradient-combination directions x,y, the exact scalar directional
Hessian of the prediction is

    H_u[x,y]
      =<x_c,phi'(Z2)V_u(y)>+<y_c,phi'(Z2)V_u(x)>
       +<c,phi''(Z2)V_u(x)V_u(y)>
       +<delta,x_K F_u(y)+y_K F_u(x)>
       +<Q,phi''(w.u)(x_w.u)(y_w.u)>.                      (Q7)

This is the polarization of G12, with the last term rewritten using the
actual adjoint. It is a scalar form on the specified directions, not a
bounded ambient L2 Hessian. All terms are finite by (Q2),(Q6) and the
book's state bounds.

Use |phi'|<=1, |phi''|<=2 and the conservative |phi'''|<=4. Define

    C_H=2L Z2f+2H Z2f²+2c_b L²+2q2 W4f²,

    L_H=2[J Z2f+2m_d Vz Z2f+L VV]
        +2Vc Z2f²+4H Vz Z4f²+4H VV Z2f
        +2[Vdelta L²+c_b J L+c_b L VF]
        +2VQ W4f²+4Vw4 q4 W4f²+4q4 J W4f.                (Q8)

Then for fixed v,w in mathsf H and x_t=D_t v,y_t=D_t w,

    |H_(theta_t,u)[x_t,y_t]|<=C_H ||v|| ||w||,
    |H_(theta_t,u)[x_t,y_t]-H_(theta_s,u)[x_s,y_s]|
        <=L_H |t-s| ||v|| ||w||.                          (Q9)

Here is a term-by-term justification for the nontrivial products. In the
upper curvature term, changing phi'' costs at most

    4H ||Z2_t-Z2_s||2 ||V_u(x_s)V_u(y_s)||2
       <=4H Vz Z4f² h.

This is exactly where (Q2) is needed. Changing c costs 2Vc Z2f² h, and
changing either V factor costs in total 4H VV Z2f h. In the row curvature
term, a Q difference pairs its L2 bound with the product of the two L4
directions. A row-gate difference uses four L4 factors: w_t-w_s, Q, x_w
and y_w. A direction difference uses its L2 bound and the L4 bounds of
Q and the other direction. These give the last line of (Q8). The first
and third lines of (Q8) are direct two-factor Cauchy–Schwarz subtractions
of the mixed readout and middle terms. Thus no missing higher-moment
estimate of a backward *derivative* is used.

## 4. An explicit bound replacing G20

For fixed v define its signed projected coefficient measure

    mu_t(v)=v p rho-sum_a beta_(t,a)(v) delta_(e_a),
    beta_t(v)=M_t^-1 G_t* integral v g_t p d rho.

Its total variation is at most m_d||v||. NSC28 gives

    ||beta_t(v)-beta_s(v)||1<=L_beta |t-s| ||v||,
    L_beta=sqrt(2) A_s[T_B L+sqrt(2/k)T_g].                (Q10)

Set

    C_t(v;x,y)=integral H_(theta_t,u)[D_t x,D_t y] dmu_t(v),
    C_C=m_d C_H,             L_C=m_d L_H+L_beta C_H.

Equations (Q9)–(Q10) prove |C_t(v;x,y)|<=C_C||v||||x||||y||
and a time Lipschitz bound with constant L_C in the same product norm.

Let r_t=P_nu(t)-q and mathsf K_t=D_t*D_t. The exact raw projector
derivative, paired with tangent vectors, gives

    <v,mathsf K'_t w>
      =-2[C_t(v;r_t,w)+C_t(w;r_t,v)].                     (Q11)

Indeed the normal part of (D_t v)' is orthogonal to D_t w. Its tangent
part is Pi times the signed Hessian applied to theta'=-2D_t r_t. This
proves (Q11) directly from the established strong first derivative; it
does not require K'' or a derivative of the Hessian.

Risk dissipation and bounded K imply ||r_t||<=R and
||r_t-r_s||<=2L² R|t-s|, where the law-independent choice
R=sqrt(10)+1 bounds all initial residuals for |q|<=1. Consequently

    ||mathsf K'_t-mathsf K'_s||op<=Lambda_1 |t-s|,
    Lambda_1=4R[L_C+2C_C L²].                             (Q12)

This follows by testing (Q11) on all unit v,w and using the trilinearity
of C_t. It is an operator-norm assertion in the common prediction space,
proved only along the selected curve. All constants are uniform over the
fixed bounded-label families and independent of n, epsilon and sample count.

In particular the formerly unevaluated G20 modulus can be bounded by

    Omega(t)<=Lambda_1 t.                                 (Q13)

The constants contain the unevaluated reference/source conditioning and
the very large exponent in (Q1). This is a formula in established constants,
not a claim that those constants have been numerically enclosed or that
the resulting episode is practical.

## 5. Consequence for a prospective positive sign certificate

Let Gamma=2LJ as in the frozen reports. Substitution into G22 gives the
actual finite-time estimate

    |Delta E(t)+8 C_p(r0)t²|
      <=R² t²[(2Lambda_1+8L²Gamma)t+Gamma²t²].             (Q14)

Thus, IF a separate neural-specific proof establishes C_p(r0)<=-c_*<0
uniformly on an unchanged declared family, the explicit choice

    0<T<=min{T_c,1,
      4c_*/[R²(2Lambda_1+8L²Gamma+Gamma²)]}

would yield the positive matched-clock risk margin 4c_* T². This
conditional implication includes its full interaction remainder and
requires no assumed positive Taylor radius. Substituting (Q13) in G24
likewise makes the independently defined scalar-clock/component remainder
explicit; its favorable component coefficient still needs a separate proof.

No c_* or beneficial component sign has been established here. The result
removes a finite-time-control gap in the initial route, while leaving the
decisive actual-neural sign question open. No computational training or
numerical neural endpoint evaluation was performed.
