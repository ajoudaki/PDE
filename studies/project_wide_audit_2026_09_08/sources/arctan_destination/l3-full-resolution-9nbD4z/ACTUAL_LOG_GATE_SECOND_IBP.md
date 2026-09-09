# Second log-gate integration by parts retains ordered response loops

Status: exact finite-width identities and a proved spatial log-amplitude
tail bound. The proposed second integration by parts does not currently
yield a response bound: it retains actual ordered gate products, a
lower-gate mobility derivative, and the original residual/memory terms.
This is not a negative theorem for the canonical response, nor a generic
operator counterexample.

Use the ACTUAL UNCUT trajectory, primitive, source, and kernel of
ACTUAL_BACKPROP_PRIMITIVE_RESPONSE.md and the off-diagonal identity in
ACTUAL_PRIMITIVE_OFFDIAGONAL_PAIR.md. Norms and probe expectations have
their conventions. In this note m1^{-1} is used, so impose the uncut
coercivity bound m1>=m_*>0 from the moving-range primal premises. No
extension of that premise to the clipped family is asserted.

## 1. Log amplitude has a stronger tail than log total variation

Put D=diag(phi'(z2)), ell=log D, and

    X_i=sup_(t<=S)|ell_i(t)|
       =log(1+sup_(t<=S)|z2_i(t)|^2).

The primal initial-state and velocity estimates imply

    mean_i sup_(t<=S)|z2_i(t)|^2<=C_S.

Indeed coordinatewise sup|z_i|^2 is at most
2|z_i(0)|^2+2S integral_0^S|z_i'|^2. Consequently

    mean_i exp(X_i)<=1+C_S,
    mean_i 1_(X_i>R)<=(1+C_S)exp(-R),
    mean_i X_i^2 1_(X_i>R)<=C'_S exp(-R/2).             (1)

For the last estimate use the finite supremum of x^2 exp(-x/2) on
[0,infinity). These are empirical spatial bounds on the same actual
path event, not statements that the response covariance is independent
of the large-X coordinates.

By contrast, since beta=phi''/phi' satisfies |beta|<=1,

    ell_i'=beta_i z2_i',
    V_i:=integral_0^S|ell_i'|dt,
    mean_i V_i^2<=S integral_0^S||z2'(t)||_n^2dt<=C_S.  (2)

Equation (2) does not give the exponential amplitude tail (1) for V.
Nor does (1) replace total variation by amplitude in a time integral.

## 2. Exact second integration and a provably invertible correction

Work with a=a_delta=Dc, so this calculation introduces no inverse-gate
coefficient. Retain the actual memory response

    v(t)=integral_0^t N0(t,s)a(s)ds.

Write

    K2=W2 D1^2 W2*,       A2=m1 I+K2,
    delta=Dq,             b=phi''(z2)q,
    r=K2 delta,           C=A2/m1,
    L(t)=ell(t)<=0.

The matrix C has bounded operator norm on the stated uncut premises.
The actual identities z2'=m1 delta+r and a'=D u+b(A2 a+v) give

    L'=m1 b+beta r,
    a'=M_(L') C a+F,
    F=D u-M_(beta r) C a+M_b v.                        (3)

Here M denotes a coordinate multiplication matrix. The complete
response-dependent residual and memory remain in F; only D u has the
previously proved source bound. In particular F is not declared bounded.

Set B=M_L C and eta=(I-B)a. Invertibility is actually proved here;
no small-log assumption is needed. Since C=A2/m1=I+K2/m1 is symmetric
positive definite with I<=C<=C_S I, and -L>=0 coordinatewise,

    I-B=I+M_(-L)C
       =C^{-1/2}[I+C^{1/2}M_(-L)C^{1/2}]C^{1/2}.

The bracket is symmetric with every eigenvalue at least one. Hence

    ||(I-B)^{-1}||_op<=sqrt(cond(C))<=sqrt(C_S),
    ||a||_n<=sqrt(C_S)||eta||_n.                         (4a)

The correction need not itself be symmetric, nor is its forward
operator norm asserted bounded. Its initial value satisfies eta(0)=0
because a(0)=0, although L(0) generally does not vanish. Since
B'=M_(L') C+M_L C', direct differentiation of (3) gives

    eta'=(I-B)F-M_L C'a-M_L C M_(L') C a.               (4)

Thus moving the log derivative off the first response factor creates
an ordered two-gate product. There is no commutation in (4).

## 3. The actual off-diagonal loop is not an endpoint derivative

Put B0=M_(L') C. The loop in (4) is B B0. Its exact decomposition is

    B B0=(1/2)(B^2)' +(1/2)[B,B0]
              -(1/2)[(M_L C')B+B(M_L C')].             (5)

Even integrating the first term against a creates a term containing
B^2 a'. The commutator in (5) remains explicitly. Its diagonal is

    [B,B0]_ii
       =sum_(j!=i) (K2_ij^2/m1^2)
                           (L_i L_j'-L_i' L_j).       (6)

This uses C_ij C_ji=K2_ij^2/m1^2 and the symmetry of the ACTUAL K2.
It is the ordered off-diagonal gate loop, with the actual time-varying
mobility coefficients retained. The quantities in parentheses are
antisymmetric iterated gate increments. The elementary available
bound is in terms of amplitude times TOTAL VARIATION, such as

    integral_0^S|L_i L_j'-L_i' L_j|dt
                            <=X_i V_j+X_j V_i,        (7)

because |L_i(t)|<=X_i. It is not an endpoint bound in X alone.
Equations (1)--(2) do not control these products acting on the actual
response in (4)--(5).

For n>=2 and Gaussian hidden initialization, K2_ij(0)!=0 almost surely
for each i!=j: conditional on the positive initial D1^2 and a nonzero
first row, the weighted inner product with the independent second row
has a nondegenerate continuous Gaussian law. Thus the coefficients
K2_ij(0)^2/m1(0)^2 in (6) are nonzero almost surely. This is NOT a claim
that the commutator itself is nonzero initially: for zero readout,
L'(0)=0, so it vanishes despite the generally nonzero absolute L(0).
No initial value of the commutator is prescribed for tiny readout, and
no nonzero or large accumulated loop on the canonical path is asserted.
The coefficient calculation only rules out silently replacing the
actual matrix ordering by commuting factors.

## 4. Mobility differentiation introduces another actual gate term

The other retained term in (4) is not controlled by boundedness of C.
To see its precise content, put q1=W2*delta and k=W2 D1^2 H1. The
actual primal equations give

    m1'=2<k,delta>_n,
    A2'=m1'I+delta tensor k+k tensor delta
           +W2 diag(2 D1^2 phi''(z1) q1) W2*,
    C'=A2'/m1-(m1'/m1)C.                              (8)

The rank and scalar parts in (8) have bounded operator norms under
the existing primal estimates. The displayed lower-gate multiplier
contains q1 and has no established width-uniform multiplication-operator
bound. Its contribution to M_L C'a in (4) is retained, not absorbed
into a constant. No initial-data derivative of a primal estimate has
been taken.

Equations (3)--(8) are the bounded pass's stopping point. They prove the
log-amplitude tail and the uniform inverse bound (4a), while identifying
the exact remaining ordered-gate, mobility-derivative, residual, and
memory terms. The factor (I-B) on F in (4) is also retained: its full
action on the response/source is not bounded merely by (4a). Thus
invertibility is not the obstruction in this choice of correction.
The identities still do not justify replacing the retained terms by
log amplitude or claiming a global response bound. No frozen proof
was changed by this note.
