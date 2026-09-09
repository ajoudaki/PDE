# A zero-readout-reachable counterexample to the signed Hessian bound

Status: proved, exact deterministic finite-width construction. For every
fixed real kappa, the feature-time matrix `B' - kappa B^2` has an
unbounded positive Rayleigh quotient at states reached in uniformly
bounded positive time from exactly zero readout. The entire trajectory
segment has width-uniform hidden operator norms, readout RMS and first
preactivation RMS. The complete Hessian B has a width-uniform operator
bound at the terminal state; no such bound is asserted along the entire
segment. The analogous signed matrix bound also fails in physical time.

The initialization constructed here is deterministic and correlated,
not the prescribed independent Gaussian initialization. This result
does not disprove a Gaussian-typical estimate or any population limit.

Dependencies: the canonical equations in the first 35 lines of
`CONTRACT_AND_LEDGER.md`; the complete canonical gradient/Hessian
identities in `ACTUAL_HIDDEN_GRAPH_VOLUME.md`; and equations (1)-(5) of
`ACTUAL_SCHWARZIAN_MATERIAL_HESSIAN.md`. All calculations below use both
trained hidden matrices and the trained readout in the original scaling.
No experiment or numerical calculation is used.

## 1. Canonical coordinates and the exact claim

Write

    x=(z1,sqrt(n)W2,sqrt(n)W3),  c=W4,
    F=c^T h3,  b=grad F=(J^T c,h3),  J=D_x h3,
    B=Db=[A J^T; J 0],  A=D_x^2 F.

Feature time satisfies `(x,c)'=b`. All norms on the canonical state
space are ordinary Euclidean/Frobenius norms. The predictor is `f=F/n`.

Fix any two constants beta,gamma>0. There exists epsilon0>0, depending
only on beta,gamma, such that for every fixed 0<epsilon<=epsilon0 and
every even n>=4 there are a zero-readout initial state and a feature
time tau_n satisfying

    epsilon/(pi/2) <= tau_n <= epsilon/h_* ,

where h_*>0 is independent of n. On this segment all the stated primal
bounds are uniform in n. At its terminal state there is a unit vector
U_n such that

    ||B||op <= C,
    U_n^T(B' - kappa B^2)U_n >= c0 epsilon^2 n-C_kappa,

with c0>0 and C,C_kappa independent of n. Thus a pointwise upper bound
inferred only from these primal bounds is false even when restricted to
trajectories beginning at zero readout. No additional integral-Hessian
history bound is assumed or refuted.

## 2. Terminal state and uniform Hessian bound

Let `1` denote the all-ones vector. Choose any balanced sign vector e
with entries +/-1/sqrt(n), so ||e||=1 and e^T 1=0. Put

    a=pi/4,  m=a^2<1,  rho=(n-2)/n,
    w=e1+e2,  v=e1-2e2,  g=1-e1-e2,
    z1=1,
    W2=2 w e^T + beta/(a n) g 1^T,
    W3=1 v^T/sqrt(n) + gamma/n 1 g^T,
    c=epsilon 1.                                           (1)

Here beta is the fixed positive bulk preactivation (called b in the
candidate), and g is the bulk indicator. The images and domains of
the two summands of W2 are pairwise orthogonal, giving

    ||W2||op=max(2sqrt(2), beta sqrt(rho)/a),
    ||W3||op=sqrt(5+gamma^2 rho),
    ||z1||/sqrt(n)=1,  ||c||/sqrt(n)=epsilon.

With phi=arctan, define the scalar quantities

    t=phi(beta),  d=phi'(beta),
    Z=gamma rho t,  H=phi(Z),  D=phi'(Z),  k=epsilon D,
    L=beta gamma d rho/a,
    R=gamma d [m+beta^2 rho/(4a^2)],
    Q=rho t^2+5m+1+gamma rho d R.

The forward state is exactly

    h1=a1,  z2=beta g,  h2=tg,  z3=Z1,  h3=H1,
    f=epsilon H.

The exact backward fields and feature velocities are

    delta3=k1,
    q2=sqrt(n)k v+gamma k g,
    delta2=sqrt(n)k v+gamma d k g,
    q1=-2sqrt(n)k e+Lk1,
    nu1=-sqrt(n)k e+(Lk/2)1,
    nu2=sqrt(n)k(mv-w)+kR g,
    nu3=kQ1.                                                (2)

For example, `nu2=m delta2+W2 D1^2 W2^T delta2`, with D1=I/2.
The rare two-coordinate block of its middle operator is exactly
`mI+ww^T`. The bulk part contributes no rare-coordinate cross term
because g is orthogonal to w and e is orthogonal to 1.

To bound the full B, use the Hessian formula from the dependency. Its
three diagonal multiplication operators are

    M1=diag(phi''(1)q1),
    M2=diag(phi''(beta g)q2),
    M3=epsilon phi''(Z)I.

Since sqrt(n)|e_j|=1 and phi''(1)=-1/2,

    ||M1||op <= |k|(1+L/2),
    ||M2||op <= |phi''(beta)| gamma |k|,
    ||M3||op <= epsilon |phi''(Z)|.                         (3)

The rare entries of M2 vanish exactly. The operators T1,T2,T3,J are
uniformly bounded by the primal operator bounds, since |phi|<=pi/2
and |phi'|<=1. The two mixed-term maps obey

    ||S2||op <= ||delta2||/sqrt(n) <= ||W3||op epsilon,
    ||S3||op <= ||delta3||/sqrt(n) <= epsilon.

Substitution of these estimates and (3) into the complete Hessian
formula proves a width-uniform bound on ||A||op and hence ||B||op
at (1). Also `||b||^2/n<=||J||op^2 epsilon^2+(pi/2)^2` there.

## 3. Exact positive Rayleigh quotient

Take the unit full tangent `U=(u,0)` with hidden components

    u1=0,  E2=e1 1^T/sqrt(n),  E3=0.

For this fixed tangent, the exact response maps and their material
derivatives are

    T1u=0,
    T2u=a e1,              T2'u=(Lk/4)e1,
    T3u=a1/sqrt(n),        T3'u=(Lk/(4sqrt(n)))1.            (4)

For the last derivative, `W3'D2T2u=0` because `h2=tg` and
g_1=0, and `W3 D2'T2u=0` because phi''(z2_1)=phi''(0)=0.
Thus only `W3 D2 T2'u` remains. This retains the actual trained-W3
velocity rather than freezing that matrix.

Every bottom-layer contraction in `u^T A'u` vanishes because T1u=0.
Every mixed contraction involving S2 also contains T1u; every mixed
contraction involving S3 vanishes since E3=0 gives S3u=S3'u=0.
The cross term involving T2' and M2 vanishes because M2 e1=0.
The remaining diagonal derivatives are

    (M2')_11 = phi'''(0) nu2_1 q2_1
              = 2(1-m)n k^2,
    M3'=[phi'''(Z) epsilon k Q+phi''(Z)H] I.

Consequently the full material derivative has the exact value

    U^T B'U
      = 2m(1-m)n k^2
        +m[phi'''(Z) epsilon k Q+phi''(Z)H]
        +(aL/2)epsilon k phi''(Z).                         (5)

All terms after the first are uniformly bounded because beta,gamma,
epsilon are fixed and rho is in [1/2,1). Moreover

    D >= D_* := 1/[1+(gamma phi(beta))^2] > 0.

Since B is symmetric and ||B||op is uniformly bounded at (1),
`U^T B^2 U=||BU||^2` is uniformly bounded. Therefore (5) yields

    U^T(B'-kappa B^2)U
      >= 2m(1-m)D_*^2 epsilon^2 n-C_kappa.                 (6)

This proves the announced divergence for every fixed real kappa.

## 4. Uniform backward passage to zero readout

The following bounds are for the entire trajectory segment, not only
the terminal state. They do not assume a uniform operator bound on B.

At (1), the rows of W3 are identical and c is constant across its
coordinates. This property is invariant in both time directions:
if `W3=1 p^T` and `c=s1`, then `z3=y1` for `y=p^T h2`, and

    W3'=phi'(y)s 1 h2^T/n,  c'=phi(y)1.

The smooth finite-dimensional ODE has unique local solutions; the
displayed invariant subspace therefore contains its local forward and
backward solutions. In this subspace the scalar readout satisfies

    s'=phi(y).                                             (7)

Let P=pi/2 and choose the n-independent constants

    K2_0=max(2sqrt(2),beta/a),  K3_0=sqrt(5+gamma^2),
    N2=K2_0+1,  N3=K3_0+1,
    K=P^2+N3^2(P^2+N2^2),
    y_*=gamma phi(beta)/2,  h_*=phi(y_*/2)>0.

On any interval on which ||W2||op<=N2, ||W3||op<=N3 and
0<=s<=epsilon, the exact equations and |phi'|<=1 give

    ||delta3||/sqrt(n) <= s,
    ||delta2||/sqrt(n) <= N3 s,
    ||delta1||/sqrt(n) <= N2 N3 s,
    ||W3'||op <= P s,
    ||W2'||op <= P N3 s,
    ||nu2||/sqrt(n) <= (P^2+N2^2)N3 s,
    |y'|=||nu3||/sqrt(n) <= K s.                          (8)

For instance `nu2=delta2 ||h1||^2/n+W2 D1 delta1`, and
`nu3=delta3 ||h2||^2/n+W3 D2 nu2`; these give the last
two bounds directly, including all matrix-training effects.

Choose

    epsilon0 = min{1, 1/(4P),
                   sqrt[h_*/(4P N3)],
                   sqrt[y_* h_*/(4K)]}.                  (9)

Start at terminal state (1) at feature time 0 and integrate backward,
writing backward elapsed time as r>=0. Before the first zero of s,
bootstrap the conditions

    0<s<=epsilon,  y>=y_*/2,
    ||W2||op<N2,  ||W3||op<N3,
    r<=epsilon/h_*.

Initially y=Z>=y_*, and the matrix bounds hold with margin one.
While the bootstrap holds, (7) gives `ds/dr=-phi(y)<=-h_*`,
so s decreases and cannot leave through the upper boundary epsilon.
By (8)-(9), throughout this interval,

    ||W3(r)-W3(0)||op <= P epsilon^2/h_* <= 1/4,
    ||W2(r)-W2(0)||op <= P N3 epsilon^2/h_* <= 1/4,
    |y(r)-y(0)| <= K epsilon^2/h_* <= y_*/4.               (10)

The last three bootstrap boundaries consequently cannot be reached.
The first-layer normalized displacement is bounded by

    ||z1(r)-z1(0)||/sqrt(n)
       <= N2 N3 epsilon^2/h_*.                            (11)

At each fixed n, these bounds prevent escape to infinity in the
finite-dimensional state before the indicated horizon. Indeed they
bound z1 and c in Euclidean norm, and an operator bound controls each
matrix's Frobenius norm by sqrt(n) times that bound. The smooth ODE
therefore extends until s reaches zero or r=epsilon/h_*.
If the latter occurs first, integration of `ds/dr<=-h_*` gives
s<=0 there. Hence a first zero occurs at some tau_n<=epsilon/h_*.
Since |ds/dr|<=P, one also has tau_n>=epsilon/P.

Declare this backward endpoint to be the initial state, and translate
feature time so it is time zero. Then c(0)=0 exactly, the canonical
forward solution reaches (1) at tau_n, and (10)-(11) provide the
claimed uniform initial and whole-segment primal bounds. The initial
hidden variables are the ones obtained from this deterministic inverse
flow; there is no claim that they have the Gaussian initialization law.

## 5. Physical-time reachability and signed matrix failure

The exact feature-time predictor identity is

    f'=||b||^2/n >= 0.

The initial predictor is zero because c=0. On the whole constructed
segment it therefore satisfies

    0<=f<=f_terminal=epsilon H<=epsilon P<=1/4.

The physical clock `ds_feature/dt=alpha=2(1-f)` stays in [3/2,2].
Thus the same curve is an actual forward physical gradient trajectory,
with terminal physical time t_n obeying

    tau_n/2 <= t_n <= 2 tau_n/3.

For completeness, let C be the full physical vector-field Jacobian:

    G=alpha b,  C=DG=alpha B-(2/n)bb^T.

A dot denotes its material derivative along G, whereas B' retains
the feature-time derivative. Exact differentiation gives

    Cdot = alpha^2 B'
           -(2alpha/n)||b||^2 B
           -(2alpha/n)[(Bb)b^T+b(Bb)^T].                  (12)

At the terminal state, ||B||op and ||b||/sqrt(n) are uniformly
bounded. Every term after alpha^2 B' in (12) therefore has a uniform
operator bound; so do C and C^2. Combining (5)-(6) with alpha>=3/2
gives, for every fixed real kappa,

    U^T(Cdot-kappa C^2)U
       >= (9/4) 2m(1-m)D_*^2 epsilon^2 n-C'_kappa
       -> +infinity.                                     (13)

The clock corrections cannot remove the growing positive Rayleigh
quotient.

## 6. Exact research-state update and limitations

- Proved: the target-state material Hessian counterexample can be made
  reachable from exactly zero readout, in uniformly bounded positive
  feature and physical time, with the original primal norm bounds
  holding throughout the segment.
- Falsified: a pointwise upper bound for B'-kappa B^2 based only on
  those primal norms for all such zero-readout trajectories. The same
  statement fails for the full physical vector-field Jacobian.
- Unchanged: the canonical independent-Gaussian population theorem,
  Gaussian-typical Hessian bounds, projected-angle control and global
  hidden entropy estimates. This deterministic construction supplies
  no probability lower bound under the prescribed initialization.
- Not claimed: a uniform operator bound for B along the constructed
  segment, a bound failure under additional Hessian-history controls,
  or a fixed-time convergence failure. The terminal times tau_n,t_n
  may depend on width; all lie in fixed compact positive intervals.

The old zero-top-feature target has c'=0 and f=0 at a nonzero-readout
state and cannot supply the required zero-readout reachability. The
bulk channel repairs that specific obstruction by making the common
top feature uniformly positive while leaving the rare-coordinate
positive contribution in (5) intact. This strengthens the scope of
the deterministic proof-route obstruction, without changing the
initialization contract of the unresolved population problem.
