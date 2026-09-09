# An exact transverse coordinate for the actual softplus top layer

Root candidate, 2026-09-06. This is a structural lemma on EXISTING
opposite-label uncut gradient reference paths, not a global canonical
theorem. The sole imported mathematical premise is the common-space,
global symmetric reference construction and uniform before-fit bounds
of SOFTPLUS_ENERGY_PRESERVING_OPERATOR_REFERENCES.md, SHA256
464df3966e4d899f8615179968926edfe2b1e592fade50bbde08ba9fdcdd06f2.
Its local-assembly premise remains conditional here. No experiment,
external theorem or hidden freezing is used.

The purpose is to retain the ACTUAL moving second-layer Gram and lower
feature motion while cancelling the direct, potentially large readout
from one top-layer coordinate. A further identity isolates one scalar
transverse damping coefficient. Neither identity bounds the entire
network sensitivity or supplies its missing Gaussian tails.

## 1. Actual equations and admissible coefficient bounds

Set epsilon=1/10 and phi(z)=1+epsilon log(1+exp(z)). Labels are
y=(1,-1); simultaneous label reversal is obtained by reversing the
readout. Work at one bounded-kernel reference, on its feature interval
[0,s_N], where s_N<=S_max and g increases from 0 to 1. At fixed N all
calculations are classical. Population spaces remain separate.

Let

    U^(2)=(H^(2)_1+H^(2)_2)/2,
    V^(2)=(H^(2)_1-H^(2)_2)/2,
    A(s)=E_2[(U^(2))^2], kappa(s)=E_2[(V^(2))^2],
    w=W^(4),
    u=(Z^(3)_1+Z^(3)_2)/2,
    v=(Z^(3)_1-Z^(3)_2)/2.

Here A is a SCALAR Gram coefficient, not a weight operator. Symmetry
gives E_2[U^(2)V^(2)]=0. Define fields on population three

    P=[phi'(u+v)+phi'(u-v)]/2,
    D=[phi'(u+v)-phi'(u-v)]/2,
    F=[phi(u+v)-phi(u-v)]/2,
    b_a=W^(3)[(H^(2)_a)'],
    b_u=(b_1+b_2)/2, b_v=(b_1-b_2)/2.                 (1)

The field b_a is the FULL actual lower-motion forcing: (H^(2)_a)'
includes both the W^(2) update and first-layer motion. It is not
independent noise, a prescribed zero function, or a new model parameter.
The exact third matrix gradient is

    (W^(3))'=delta^(3)_- tensor U^(2)
                         +delta^(3)_+ tensor V^(2),
    delta^(3)_-=wD, delta^(3)_+=wP.

Consequently the ACTUAL equations imply

    u'=A wD+b_u,       v'=kappa wP+b_v,      w'=F.     (2)

This follows by applying the displayed matrix update to H^(2)_a,
then adding W^(3)(H^(2)_a)'. There is no dropped learned-memory term.
At finite width every tensor is the corresponding outer product/n;
we use (2) only on symmetric population references, not on individual
finite realizations that need not have equal sample Gram diagonals.

Uniform constants below may depend on the fixed configuration. Let
k_*>0 be a uniform lower bound on ||w'(s)||_2^2 on these references.
Such a bound follows in the imported construction from readout convexity
and convergence of the positive initial label-mode Gram. Since
||w'||_2=||V^(3)||_2 and phi is epsilon-Lipschitz,

    k_* <= ||V^(3)||_2^2
                <= epsilon^2 ||W^(3)||_op^2 kappa.

Thus kappa>=k_min>0, uniformly over the sufficiently large reference
indices and the before-fit interval. The import also bounds all raw,
forward and operator norms by M>=1, and gives
integral_0^s_N a(s)^2 ds=1, where a=||Theta'||_raw.

Because phi>=1,

    A-kappa=E_2[H^(2)_1 H^(2)_2]>=1.

Also A,kappa<=M^2 after enlarging M. Hence

    gamma=A/kappa satisfies 1+M^-2<=gamma<=M^2/k_min. (3)

These inequalities include the antiparallel input case: the lower
feature Gram is nonsingular, and no inverse input covariance is used
in this section. The top Gram coefficients are deterministic scalar
functions of time, not neuron-dependent quantities.

The curvewise forward chain rule gives
||(Z^(2)_a)'||_2<=C_M a and ||(H^(2)_a)'||_2<=C_M a.
Indeed Z2'=W2' H1+W2[phi'(Z1)Z1'], and evaluation of a first sample
has norm one in the first raw metric. Therefore

    |A'|+|kappa'|+|gamma'| <= C a,
    ||b_u||_2+||b_v||_2 <= C a,
    ||u||_2+||v||_2 <= C.                              (4)

Constants use (3) when differentiating gamma. In particular
integral |gamma'|<=C sqrt(S_max) and
integral (||b_u||_2+||b_v||_2)<=C sqrt(S_max).
These are actual global-reference estimates; they do not assume a
pointwise bound uniform in N or a whole-space Lp operator bound.

## 2. Cancellation of the direct readout term

Direct calculation with the logistic gate gives

    D/P = sinh(v)/(cosh(v)+exp(u)).                     (5)

The denominator and P are positive. For a fixed number gamma>1 define

    I_gamma(u,v)=exp(-u/gamma)
                       [cosh(v)-exp(u)/(gamma-1)].     (6)

Differentiation, with gamma held fixed, gives

    (I_gamma)_u=-(1/gamma)exp(-u/gamma)
                                      [cosh(v)+exp(u)],
    (I_gamma)_v=exp(-u/gamma)sinh(v).

Consequently

    (I_gamma)_u gamma D+(I_gamma)_v P=0.               (7)

Apply (7) with the ACTUAL gamma(s). Since A=gamma kappa, (2) gives
the exact identity

    d/ds I_(gamma(s))(u(s),v(s))
       =(I_gamma)_u b_u+(I_gamma)_v b_v
                                  +(partial_gamma I_gamma)gamma'.   (8)

The direct w term cancels for either sign of w, including at its
zeros. No division by w, v', or the label contrast is used. Both the
moving Gram term and the full lower-motion forcing remain in (8).
Thus this identity also applies when lower motion causes readout/
contrast misalignment or sign reversals. It does not assert either
that the right side is small in L2 or that I is conserved on training.

When b=0 and gamma is constant, (8) is a first integral for any common
scalar readout control, regardless of its sign changes. This restricted
observation is a check of the algebra, not a frozen-hidden substitute
for the desired model. One way to discover it is to divide the self
equations where v' is nonzero, obtaining
du/dv=gamma sinh(v)/(cosh(v)+exp(u)). With y=exp(u) and t=cosh(v),
dt/dy-t/(gamma y)=1/gamma, whose integrating factor is y^(-1/gamma).
The differentiated identity (7), not this division, proves (8) globally.

## 3. Inverse coordinate and logarithmic normal factor

For fixed v and gamma>1, u->I_gamma(u,v) is strictly decreasing,
with limits +infinity and -infinity as u tends respectively to
-infinity and +infinity. Thus it is a bijection R->R. Its inverse is
smooth by the displayed nonzero u derivative.

There is a global lower bound on the magnitude of that derivative,
uniform for gamma in the compact interval (3). To check this explicitly,
set t=cosh(v)>=1 and y=exp(u)>0. Then

    |(I_gamma)_u|=(1/gamma)(t y^(-1/gamma)+y^(1-1/gamma)).

Its minimum over y occurs at y=t/(gamma-1), and is

    t^(1-1/gamma)(gamma-1)^(-(gamma-1)/gamma).

This is bounded below by a positive constant depending only on (3).
At fixed gamma the inverse therefore satisfies

    |partial_I u|<=C,          |partial_v u|<=gamma,    (9)

the latter by -(I_gamma)_v/(I_gamma)_u and (5). These bounds concern
the inverse coordinate only. The forward derivative of I is unbounded.

Define the logarithm of its normal derivative by

    J_gamma(u,v)=log |(I_gamma)_u|
         =-log(gamma)-u/gamma+log(cosh(v)+exp(u)).       (10)

On the interval (3), J is bounded below by a constant, and

    |J_gamma(u,v)|<=C(1+|u|+|v|),
    partial_u J=-1/gamma+exp(u)/(cosh(v)+exp(u)),
    partial_v J=sinh(v)/(cosh(v)+exp(u)),
    partial_gamma J=-1/gamma+u/gamma^2.                (11)

The absolute values of its first two derivatives are at most a
configuration-dependent constant (in fact at most one here), and its
gamma derivative has at most linear growth in u.

Put

    chi=A [exp(u)/(cosh(v)+exp(u))] wD,
    E=(partial_u J)b_u+(partial_v J)b_v
                                      +(partial_gamma J)gamma'.

Substitution of (2) into (11) cancels -kappa wD against +kappa wD
and proves the further exact actual-path identity

    J'=chi+E.                                         (12)

Moreover (4) and (11) give

    ||E(s)||_2<=C a(s),
    integral_I ||E(s)||_2 ds
                    <=C sqrt(|I| integral_I a(s)^2 ds)               (13)

for every reference subinterval I. These bounds do NOT use a readout
supremum. Also ||chi||_2<=C||w||_2 because D and the bracket in chi
are bounded, so (12) is an L2 identity on the entire reference
interval. In particular J has uniform L2 bounds and a uniform L2
time modulus. All these claims are on the actual uncut references.

The scalar multiplier

    T(s,t)=exp(-integral_s^t chi(r)dr),     s<=t,

has the exact representation

    T(s,t)=exp(J(s)-J(t)+integral_s^t E(r)dr).           (14)

The lower bound for J(t), (11), and Minkowski's inequality give the
actual uniform estimate

    ||log^+ T(s,t)||_2
       <=C[1+||u(s)||_2+||v(s)||_2
                           +sqrt((t-s) integral_s^t a(r)^2 dr)]<=C.  (15)

It is also true with a supremum over t in [s,s_N] inside log^+:
use integral_s^s_N |E(r)|dr on the right of the pointwise (14).
Thus this scalar multiplier has a uniform logarithmic tail estimate,
P{T(s,t)>R}<=C/(log R)^2 for R>1. This estimate alone does NOT give
even its first moment, an exponential tail for a query, or the whole
source-response estimate needed for the target theorem.

To identify why chi is called transverse, temporarily hold gamma and
the scalar control w fixed in the TWO-coordinate self vector field,
with b=0. Put F_gamma=gamma D/P. A variation has transverse component
e=delta u-F_gamma delta v. Differentiate the two self equations, or
differentiate (7), to obtain

    e'=(partial_u F_gamma) v'_self e=-chi e.

Indeed partial_u F_gamma=-gamma exp(u)sinh(v)/(cosh(v)+exp(u))^2
and v'_self=kappa wP. A variation of the common scalar w contributes
parallel to (F_gamma,1), so it cancels from this transverse component.
For the ACTUAL full tangent system, variations of the lower forcing,
Gram, and matrices produce additional terms. Equation (15) bounds
only the scalar homogeneous multiplier, not those additional terms.

## 4. What is and is not gained

The large readout cancels exactly from (8), even with sign changes;
the actual lower-layer and moving-Gram terms are explicit. The inverse
coordinate is globally Lipschitz at fixed gamma, and the logarithmic
normal factor has bounded spatial derivatives and controlled actual
forcing (13). The scalar transverse multiplier admits (14)--(15).
These are new identities/estimates for the actual reference equations,
not assertions of independence or positivity of the full Hessian.

Two limitations prevent a global-convergence conclusion. First, the
derivatives of I in (8) grow exponentially in u and v. Primal L2 and
gradient action do not control the products (I_gamma)_u b_u or
(I_gamma)_v b_v in L2 uniformly in the reference index. One cannot use
(9) backwards to bound the forward coordinate. Second, logarithmic
tail control in (15) does not give integrability of T itself; nor does
it control the inhomogeneous full sensitivity sources.

At canonical Gaussian INITIAL top fields, (11) has Gaussian-linear
growth and hence its exponent has all finite moments. This statement
is only about the canonical initial law: arbitrary strong bounded-
kernel approximations need not inherit uniform exponential moments.
No uniform later forcing-exponential bound is established here. Closing
such an estimate using the actual lower dynamics is the next possible
use of the coordinate identity, not a premise silently supplied by it.

No conclusion in this note establishes canonical global existence,
global restartability, joint global GD/MF/GF convergence, or the full
user goal. The reference theorem remains only its explicit dependency.
