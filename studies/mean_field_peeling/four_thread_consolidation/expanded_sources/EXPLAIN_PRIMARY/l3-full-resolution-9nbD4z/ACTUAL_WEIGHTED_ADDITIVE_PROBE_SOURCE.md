# The actual weighted additive probe source is controlled

Status: proved finite-width identity and width-uniform probe bound on
the controlled finite feature horizon. The directly forced normal
response is purely top-layer, so its apparent direct curvature return
vanishes exactly. Its range feed contains an exact middle activation
factor. Consequently the entire additive source in the signed range
coordinate is bounded after division by that factor.

This sharpens the source estimates in
ACTUAL_MOVING_RANGE_PROBE_NORMAL_FORM.md and narrows the source gap in
ACTUAL_SIGNED_RANGE_INTEGRATING_FACTOR.md. It does not control the
range-dependent instantaneous or recycled memory coefficients. There
is no global response or population-continuation claim.

All coefficients are those of the actual uncut finite-width trajectory;
expectation is only over the independent auxiliary Gaussian probe. The
proof applies to zero or prescribed tiny initial readout on the primal,
operator, bounded-readout-coordinate, and coercivity events used by the
moving-range note. It needs no zero initial value of the primal q and
no derivative of a primal norm estimate.

## 1. The direct weighted range source

Use D=D2, H=H1, d=D3 C, q=W3* d, delta=Dq, and
B3=diag(C phi''(z3)). The single-column probe is

    K=xi e_i*/sqrt(n),             xi~N(0,I_n).

The actual source decomposition is f=R v_K+f_top, where

    v_K=D[K* d+W3* d_K],          d_K=B3 K H2,
    f_top=(0,0,d_K tensor H2,D3 K H2).

Thus g=Jf=v_K and exactly

    D^{-1}g=K* d+W3* B3 K H2.                          (1)

With normalized vector norms,

    n E_xi||K* d||_n^2=||d||_n^2,
    n E_xi||K H2||_n^2=H2_i^2.

The boundedness of H2_i, B3, and W3 proves

    n E_xi||D^{-1}g||_n^2<=C_S.                       (2)

No inverse-gate moment is used.

## 2. An invariant subspace for the actual normal propagator

The tangent state is y=(x,A,B,c). Define the fixed pure-top subspace

    Z_top={(0,0,B,c)}.

Both R and R' take values in the lower two components, as follows
from their exact formulas in the moving-range note. Hence for any
w=(0,0,B,c) in Z_top,

    R* w=(R')*w=0,       Qw=w,       P'w=J'w=0,
    T w=0.                                               (3)

These are identities of linear maps at each actual time. In particular
P'w=0 follows directly from every term in the displayed derivative of
P=R(R*R)^{-1}R*, not from freezing the moving state-space projector.

For this pure-top input, the K=0 first-variation equations give

    d_dot_top(w)=D3 c+B3 B H2,
    q_dot_top(w)=B* d+W3* d_dot_top(w),

    Lw=R D q_dot_top(w)
                 +(0,0,d_dot_top(w) tensor H2,D3 B H2). (4)

Applying Hcal=Q L-P' kills exactly the first term in (4), so

    Hcal w=(0,0,d_dot_top(w) tensor H2,D3 B H2)
                                                   in Z_top. (5)

Therefore Z_top is invariant under the time-dependent normal equation.
Since f_top belongs to Z_top and the direct normal response solves

    w0'=Hcal w0+f_top,                 w0(0)=0,

finite-dimensional uniqueness implies

    w0(t)=(0,0,B0(t),c0(t)),           T_t w0(t)=0        (6)

for every t in the controlled horizon. This is the w0 component of
the actual moving-range decomposition. No independent-bulk trajectory
has replaced the coefficients in (4)--(6).

One can equivalently identify its nonzero components by the closed
linear equations along that actual coefficient path:

    B0'=[D3 c0+B3(B0+K)H2] tensor H2,
    c0'=D3(B0+K)H2,              B0(0)=c0(0)=0.          (7)

## 3. The geometric range feed also contains D

Equation (3) gives J'w0=0, while JR=I and J kills pure-top vectors.
Applying Gcal=J'+J L to (4) therefore gives exactly

    Gcal w0=D q_dot_top(w0),
    D^{-1}Gcal w0=B0* d+W3*[D3 c0+B3 B0 H2].          (8)

The right side is a bounded map of (B0,c0) in the normalized-vector /
ordinary-Frobenius state norm. For example,

    ||B0* d||_n<=||B0||_F ||d||_n,
    ||B0 H2||_n<=||B0||_F ||H2||_n.

The direct normal estimate already proves

    ||xi -> w0(t)||_op<=C_S/n,
    n E_xi||w0(t)||^2<=C_S,                              (9)

where the input probe norm is ordinary Euclidean. The second bound
also follows from the first because the input dimension is n:
E||A xi||^2=||A||_HS^2<=n||A||_op^2.
Combining (8) and (9) yields

    n E_xi||D^{-1}Gcal w0||_n^2<=C_S.                 (10)

For completeness, even the older coordinate-variance estimate alone
would control the other weighted additive term:

    D^{-1}(b T w0)=beta q T w0,
    n E_xi||beta q T w0||_n^2
       <=C_S||q||_n^2<=C_S,

using |beta|<=1 and n E_xi|(T w0)_j|^2<=C_S.
The stronger identity (6) makes this term identically zero.

## 4. Exact combined weighted source and revised remaining scope

Recall f_tilde=g+Gcal w0+b T w0. Equations (1), (6), and (8) give

    D^{-1}f_tilde
       =(K+B0)*d+W3*[D3 c0+B3(K+B0)H2],
    n E_xi||D^{-1}f_tilde(t)||_n^2<=C_S.              (11)

This is an actual source estimate for every middle subset as well,
because restriction decreases the norm and commutes with D^{-1}.
It requires neither z2 fourth moments nor a tail bound for q2.

In the signed-range note the full F is

    F=Gcal R a+Gcal w_a+f_tilde.

Thus the uncontrolled weighted source there can now be narrowed to
the RESPONSE-DEPENDENT terms

    D^{-1}Gcal R a,                 D^{-1}Gcal w_a.     (12)

The w_a component is driven by Hcal R a and need not belong to
Z_top: the exact formula for Hcal R a includes lower matrix terms.
Consequently the proof of (8) cannot be applied to w_a or to a
general normal tangent without additional calculation.

Likewise the previous directly forced mixed covariance
Gamma_0=n E_xi[(Bcal a) odot(T w0)] is now identically zero. Its
earlier absolute bound remains valid but is sharpened by (6). The
range covariance and the returned w_a covariance remain unchanged
and unestimated by this result.

The new established fact is the full weighted ADDITIVE source (11).
The signed response/action pairings, the weighted terms (12), and
the actual off-block and recycled-memory returns still require their
own estimates.

## 5. The recycled return has an autonomous lower-normal equation

There is a further exact reduction, without a new response bound.
Let lower tangent space consist of pairs (x,A), write R_l v=(W2*v,
v tensor H), and let P_l=R_l Bcal^{-1}R_l*, Q_l=I-P_l.
The full state projector is diag(P_l,0_top). Define the bounded map

    C_delta(x,A)=(A*delta,delta tensor D1^2 x).

For ANY full tangent w=(x,A,B,c), the lower part of Lw is

    (Lw)_lower=C_delta(x,A)+R_l D q_dot(w),             (13)

where q_dot(w) is its full K=0 top-backward variation. Thus every
top-to-lower variation enters in the range R_l and is killed by Q_l.
Since P' also acts only on lower components,

    (Hcal w)_lower=H_l(x,A),
    H_l=Q_l C_delta-P_l'.                              (14)

This lower equation does not depend on the top tangent components.
Its coefficients still include the ACTUAL delta and lower trained
fields; no independence from top initialization is inferred.

For a normal lower pair, W2 x+A H=0, set

    Omega(x,A)=Bcal^{-1}[
         W2 A*delta+A H'
                 +delta <H,(I+D1^2)x>_n].             (15)

On such a pair, P_l'(x,A)=R_l Bcal^{-1}(R_l')*(x,A),
where (R_l')*(x,A)=delta<H,x>_n+A H'. Substituting in (14)
gives the explicit autonomous lower-normal evolution

    x'=A*delta-W2* Omega(x,A),
    A'=delta tensor D1^2 x-Omega(x,A) tensor H.         (16)

All operators in (14)--(16) have bounded norms on the stated primal
events. Equation (16) is the homogeneous normal transport equation;
the recycled normal response also has its actual range-dependent
forcing.

For any normal full state w, its return is exactly

    T w=A H+W2 D1^2 x=W2(D1^2-I)x.                    (17)

In particular only the lower-normal bottom component x can return.
Let U_l(t,s) be the propagator of (14). Set

    F_l(s)a=Q_l(s)(0,
        delta_s tensor [D1_s^2 W2_s* a]-a tensor H_s'). (18)

This is the lower part of Hcal_s R_s a: in L_sR_sa-R_s'a,
the first lower-vector term cancels, and Q_l kills the term containing
D q_dot. The recycled kernel is consequently exactly

    N(t,s)=W2_t(D1_t^2-I) pi_x U_l(t,s) F_l(s),        (19)

where pi_x selects the lower vector component. To use (17) at the
final time, observe that F_l(s)a is normal at s and (14) transports
normal lower states to normal lower states: differentiating
R_l*(x,A)=0 with (14) makes its derivative zero.

Thus the kernel N can be constructed entirely from the bounded
lower-normal generator and its actual geometric forcing. The pure-top
components of Hcal R, although they occur in the full normal state,
never feed back into N. At equal time, (19) agrees with the previously
checked identity

    N(s,s)=(I-Acal Bcal^{-1})(delta tensor k-eta I),
    k=W2 D1^2 H,                 eta=<delta,k>_n.

The range feed of a GENERAL normal w is, consistently with (15),

    Gcal w=D q_dot(w)+Omega(x,A).                      (20)

For w0 its lower pair is zero, recovering the full D factor in (8).
For w_a, Omega may remain. Its gate-weighted contribution
D^{-1}Omega, and b times the return (19), are not bounded by this
triangular reduction. Those are retained actual geometric response
terms, not discarded top transport.
