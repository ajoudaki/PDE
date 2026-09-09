# Moving training range and a controlled exceptional probe return

## Scope and new bound

This note concerns the ACTUAL uncut finite-width Gaussian-probe
tangent, not a tangent of an independent copied bulk. It gives a
bounded moving-range decomposition and proves that the directly
forced normal response has uniformly bounded coordinate probe
variance. Consequently its contribution to the exceptional signed
curvature pairing, and its accumulated exceptional forcing, are
controlled without a q2-tail assumption.

The response recycled through the training range remains unbounded
by this argument. Neither all-horizon response moments nor global
population continuation are claimed.

Use the notation and exact equation of
ACTUAL_BULK_GAUSSIAN_TANGENT_ENERGY.md:

    y' = L_s y + R_s M_(b_s) T_s y + f_s,   y(0)=0,
    b = phi''(z2) q,     delta = D2 q,
    R_s v = (W2* v, v tensor H1, 0, 0),
    T_s y = A H1 + W2 D1^2 x.

Vector norms and inner products are normalized by n; matrix tangent
norms are ordinary Frobenius norms. The tensor u tensor v is uv*/n.
The tangent-state norm is the sum of squared component norms. Norms
on the independent probe xi~N(0,I_n) itself are ORDINARY Euclidean
norms. All probe expectations condition on the entire actual path.

Work on [0,S] with the established primal/operator bounds, including
bounded readout coordinates. Constants below are independent of n,
max|q|, and the realized probe xi.

## 1. Coercivity and every moving-frame derivative

Write H=H1, m=||H||_n^2, and introduce two different middle operators:

    Bcal = R* R = m I + W2 W2*,
    Acal = T R  = m I + W2 D1^2 W2* = A2.              (1)

There is a width-independent m_*>0 with m>=m_* on the finite feature
horizon under consideration. Here is the premise from the canonical
primal theorem, rather than an ambient nondegeneracy assumption.
READOUT_COERCIVITY.md proves a positive lower bound
||H3(s)||_n^2>=ell_3 on every feature horizon, for zero readout and
for the prescribed sufficiently small readout event. Its Gaussian
initialization argument supplies ell_3>0 uniformly with probability
tending to one. If M_2(S),M_3(S)>0 bound the two trained operators,
the Lipschitz activation and phi(0)=0 give

    ||H3||_n <= M_3(S)||H2||_n
              <= M_3(S)M_2(S)||H1||_n,

so m_*=ell_3/[M_2(S)^2 M_3(S)^2] is valid. This uses the actual
lower bound on H3, not merely a lower bound on the sum of all kernel
blocks. The bounds in this note concern uncut trajectories; no
clipped analogue of this coercivity is presumed.

Thus Bcal>=m_* I and Bcal, Bcal^(-1) have bounded operator norms.
The lower primal equations give

    W2' = delta tensor H,
    H' = D1^2 W2* delta,
    m' = 2 <H,H'>_n,

    R_s' v = (H <delta,v>_n, v tensor H', 0, 0),
    Bcal' = m' I + delta tensor z2 + z2 tensor delta.    (2)

Each operator in (2) has bounded norm using only primal L2 bounds.
In particular no derivative of T_s or of D1^2 as a multiplication
operator is needed.

Define the left inverse and the orthogonal state projector

    J = Bcal^(-1) R*,       P = R J,       Q = I-P.

Direct differentiation gives

    J' = -Bcal^(-1) Bcal' Bcal^(-1) R*
                            + Bcal^(-1) (R')*,
    P' = R' Bcal^(-1) R* + R Bcal^(-1) (R')*
                  - R Bcal^(-1) Bcal' Bcal^(-1) R*.     (3)

All these norms are bounded. In particular, P' R=Q R', obtained by
differentiating P R=R. This is a projector onto a state-space range,
not a projection onto a subset of middle coordinates.

## 2. Exact range equation and controlled normal transport

Put

    a = J y,                 w = Q y,
    y = R a+w,               R* w=0,
    Hcal = Q L-P',           Gcal = J'+J L,
    g = J f.

The exact equations are

    w' = Hcal w + Hcal R a + Q f,
    a' = M_b (Acal a+T w) + Gcal(R a+w) + g.            (4)

Every operator in (4) other than M_b is bounded by the established
primal constants. The entire middle-curvature forcing cancels from
the normal equation since Q R=0. If U_H(s,t) is the propagator of
Hcal, then exactly

    w = w_0+w_a,
    w_0(s) = integral_0^s U_H(s,t) Q_t f_t dt,
    w_a(s) = integral_0^s U_H(s,t) Hcal_t R_t a(t) dt.   (5)

Write Aprobe(s)=n E_xi||a(s)||_n^2. Since
n E_xi||f_s||^2<=C, (5) yields the actual transport estimate

    sqrt(n E_xi||w(s)||^2)
      <= C_S [s+integral_0^s sqrt(Aprobe(t)) dt].        (6)

Orthogonality also gives the exact energy identity

    Lambda = n E_xi[<a,Bcal a>_n+||w||^2].             (7)

Thus (6) controls transport out of the instantaneous lower-training
range, while (7) shows precisely which range amplitude is not
controlled. Equation (6) is not an estimate on a itself.

## 3. The normal direct source has a stronger 1/n operator scale

This is more than the bounded normal equation alone. Recall the
actual column-probe direction K=xi e_i*/sqrt(n), and set

    d_K = C phi''(z3) K H2,
    v_K = D2 [K* d+W3* d_K],
    f = R v_K+f_top,
    f_top = (0,0,d_K tensor H2,D3 K H2).               (8)

The top source is orthogonal to the lower-training range, so

    Q f = f_top,                  g=J f=v_K.           (9)

Let F_top(s) be the linear map xi -> f_top(s), from ordinary
Euclidean probe space to the normalized tangent-state Hilbert space.
Because K H2=H2_i xi/sqrt(n), bounded activation/readout gives

    ||F_top(s)||_op <= C/n.                             (10)

For example, the normalized vector norm of D3 K H2 is at most
|H2_i| ||xi||_Euclidean/n. The matrix component has Frobenius norm
||d_K||_n ||H2||_n and has the same 1/n operator scale. This is
distinct from the larger operator scale of the concentrated source
R v_K, which has been removed EXACTLY by Q.

All coefficients in U_H are independent of the auxiliary probe.
Thus (5), (9), (10), and ||U_H(s,t)||<=exp(C(s-t)) prove

    ||xi -> w_0(s)||_op <= C_S/n.                       (11)

The norm of evaluation at a middle coordinate, on the normalized
middle space, is sqrt(n). Applying this evaluation after T_s in
(11) gives, uniformly in j and s<=S,

    n E_xi |(T_s w_0(s))_j|^2 <= C_S.                  (12)

No covariance diagonalization of the actual response, or independence
of the original Gaussian weights from the actual trajectory, has
been used. Equation (12) follows from an operator estimate on a map
of the INDEPENDENT auxiliary probe.

Consequently the actual unbounded multiplier is controlled on this
part of the normal response:

    n E_xi ||b_s T_s w_0(s)||_n^2
       <= C_S ||b_s||_n^2 <= C_S.                      (13)

This holds on the entire layer and therefore on every measurable
adaptive subset, including the exceptional covariance support E_R(s)
of ACTUAL_PROBE_LEVERAGE_LOCALIZATION.md. In particular,

    sqrt(n E_xi ||integral_0^s U_L(s,t) R_t
                     1_(E_R(t)) b_t T_t w_0(t) dt||^2)
       <= C_S s.                                      (14)

Equation (14) controls a genuine part of the accumulated EXCEPTIONAL
forcing; no derivative of E_R is taken.

## 4. A controlled part of the exceptional signed covariance

Since gamma=R* y=Bcal a and zeta=T y, its exact covariance splits as

    Gamma = Gamma_range+Gamma_memory+Gamma_0,
    Gamma_range = n E_xi[(Bcal a) odot (Acal a)],
    Gamma_memory = n E_xi[(Bcal a) odot (T w_a)],
    Gamma_0 = n E_xi[(Bcal a) odot (T w_0)].            (15)

Conditional Cauchy--Schwarz and (12) give

    ||Gamma_0(s)||_n^2
       <= (C_S/n) sum_j n E_xi|(Bcal_s a)_j|^2
       <= C_S Aprobe(s).

For EVERY adaptive middle set E, including E_R(s), it follows that

    |<b_s,1_E Gamma_0(s)>_n|
        <= C_S sqrt(Aprobe(s))
        <= C_S(1+Lambda(s)).                           (16)

Thus this component of the actual signed exceptional covariance is
now controlled. The estimate is not limited to its complement.
The two other terms in (15) remain explicit and unestimated by
(12)--(16).

Substituting (5) in (4) gives a range equation whose additive source

    f_tilde = g+Gcal w_0+b T w_0

satisfies n E_xi||f_tilde||_n^2<=C_S. Its remaining unbounded terms
are exactly

    b_s Acal_s a(s),
    b_s integral_0^s N(s,t)a(t)dt,
    N(s,t)=T_s U_H(s,t) Hcal_t R_t,   ||N(s,t)||<=C_S.  (17)

All other instantaneous and memory terms in that equation are
bounded operators applied to a. This is a reduced equation for the
actual response, not a claim that its solutions obey a closed
energy inequality.

## 5. Exact learned-rank structure of the remaining normal feed

The map Hcal R is more specific than an arbitrary bounded map. For
a middle vector a, put

    u = D1^2 W2* a,          zeta = Acal a,
    d_a = C phi''(z3) W3 D2 zeta.

Substitute y=R a into the exact full tangent equation with K=0.
The term R D2 q_dot is killed by Q. The lower vector term
H1<a,delta>_n cancels the corresponding part of R' a. Therefore

    Hcal R a = Q S(a),
    S(a) = (0,
             delta tensor u-a tensor H1',
             d_a tensor H2+d tensor D2 zeta,
             D3 W3 D2 zeta).                           (18)

Every map in (18) is bounded on the current primal bounds, but the
first matrix term contains the actual backward vector delta.
One cannot multiply its later return by b and declare the resulting
product bounded from the L2 bounds on q and delta.

There is also an exact equal-time simplification. Put

    k = W2 D1^2 H1,          eta=<delta,k>_n=<H1',H1>_n.

Only the lower matrix component of S enters T Q S. Hence

    N(s,s) = (I-Acal Bcal^(-1))
                             (delta tensor k-eta I).   (19)

Indeed T S=R* S=delta<a,k>_n-eta a, and T R=Acal.
In particular N(s,s)delta=0. This is an instantaneous identity in
one direction, not a statement that the actual probe a is parallel
delta or that the two-time memory vanishes. No all-time signed
bound is inferred from (19).

## 6. All-horizon past-time regularity of the old return kernel

The same bounded R' gives a useful exact normal form without
differentiating T_s. For the original bounded-part kernel

    Kcal(s,t)=T_s U_L(s,t)R_t,

one has on the entire time triangle

    partial_t Kcal(s,t)
      =T_s U_L(s,t)(R_t'-L_t R_t),
    ||partial_t Kcal(s,t)||_op <= C_S.                  (20)

Define the actual curvature primitive

    a_b(t)=integral_0^t b_u T_u y(u)du,
    zeta_0(s)=T_s integral_0^s U_L(s,t) f_t dt.

Finite-width integration by parts in the past variable gives

    zeta(s)=zeta_0(s)+Acal_s a_b(s)
              -integral_0^s partial_t Kcal(s,t)a_b(t)dt.
                                                               (21)

The range coordinate differs from this primitive by a bounded
history, exactly

    a(s)-a_b(s)=integral_0^s [Gcal_t y(t)+g_t]dt,
    sqrt(n E_xi||a(s)-a_b(s)||_n^2)
      <= C_S [s+integral_0^s sqrt(Lambda(t))dt].         (22)

Thus the retarded kernel has a controlled past-time derivative on
every finite horizon, not merely a short-lag approximation. The
primitive a_b in (21) remains unknown; bounded kernel variation
does not estimate it.

## Remaining resolver

Equations (13)--(16) upgrade one actual exceptional contribution
from open to controlled. The remaining amplification is within the
range, with instantaneous term and recycled learned-rank memory
given in (17)--(19). Small-set scalar-return estimates can apply
to portions of these maps only with their stated full/pruned
distance premises. Primal SHARP_RARE bounds cannot be
differentiated to supply the missing tangent bound.

The directly forced normal component is covered by (12)--(16);
its subsequent amplification through the range is not. A successful
continuation argument must control the signed combination of
Gamma_range and Gamma_memory, or their accumulated effect, with
the actual recycled range response retained. That estimate is not
proved here.
