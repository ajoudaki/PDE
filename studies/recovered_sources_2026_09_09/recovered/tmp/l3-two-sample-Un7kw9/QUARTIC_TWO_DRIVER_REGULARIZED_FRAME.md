# Quartic gate: full two-driver response with a subquadratic exponent

Status: new main candidate, awaiting an isolated audit. This is a local
two-coordinate theorem, not a network continuation theorem. In particular,
the input-tail hypothesis below is not inferred from a population L2 bound.
The positive parameter h introduced below regularizes a proof weight only:
it does not clip a field, change the activation, or change any dynamics.

Fix e>0 once, for example e=1/10, and put

    phi(z)=1+z+e integral_0^z du/(1+u^4),
    a(z)=phi'(z)=1+e/(1+z^4),
    b(z)=phi''(z)=-4e z^3/(1+z^4)^2,
    L=1+e.

For arbitrary signed p,q in L1[0,T], consider

    M'=a(M)p+V b(M)q,       V'=a(M)q.                 (1)

Write P=integral|p|, Q=integral|q|, and

    R=1+|M0|+|V0|+P+Q.

Use the sum norm on R2 x L1 x L1 and the uniform sum norm on the
two-coordinate output paths. There is C_e<infinity such that the solution
map S of (1) is Frechet differentiable everywhere and

    ||DS(M0,V0,p,q)|| <= C_e R^12 exp(C_e R^(4/3)).     (2)

The constants depend only on the fixed e, not on T or the driver ordering.
The bound controls both initial-coordinate derivatives and both forcing
derivatives simultaneously. If random inputs obey E exp(lambda R^2)<infinity
for some lambda>0, the right side of (2) has every finite positive moment.
No smallness condition on lambda relative to e or T is imposed.

The mechanism is a nonsingular moving frame for the first variation. It
cancels the part of b' that is large away from zero, and bounds the remaining
part by h^2. Balancing the resulting P/h and h^2 Q(|V0|+LQ) terms yields the
strictly subquadratic exponent. Both base drivers remain in every equation.

## 1. Existence, state size, and differentiability

The field is smooth in M,V, 1<=a<=L, and |b|<=4e. Local integral-map
contraction works on a state ball on an interval where the integral of
|p|+|q| is sufficiently small. Indeed the state derivatives of the two
smooth coefficient fields are bounded on that ball, and their time-dependent
Lipschitz majorant is a fixed constant times |p|+|q|.

For every local solution and Q_t=integral_0^t |q|,

    |V(t)| <= |V0|+LQ_t,
    |M(t)| <= |M0|+LP+4e|V0|Q+2eLQ^2.               (3)

The last term follows by integrating Q_t |q(t)| and using that Q_t is
absolutely continuous with derivative |q|. Thus all solutions stay on a
fixed finite ball on [0,T]. At a finite endpoint, the integrable field bound
gives a limiting state; the local construction there extends the solution.
The same integrable Lipschitz estimate on a containing ball proves uniqueness
by subdividing into intervals with contraction constant less than one.

In particular,

    sup |V| <= L R,            sup |M| <= C_e R^2.     (4)

We also record why the derivative estimated below is an actual Frechet
derivative. Fix a base input. Formula (3) puts all inputs in its unit ball
into one common state ball. On this ball both coefficient vector fields
(a(M),0) and (Vb(M),a(M)) have bounded first and second derivatives. The
integral difference equation and its integrable Lipschitz majorant give a
uniform bound C_base epsilon on the trajectory difference for input
perturbations of sum norm epsilon<=1. Subtracting the linear variational
equation leaves Taylor remainders whose L1 norm is at most

    C_base [(P+Q) epsilon^2 + epsilon^2].

Here the second term includes the product of a driver perturbation's L1
norm and the uniform state difference. There is no requirement of pointwise
bounded or smooth driver perturbations. Iterating the same integral
inequality bounds the output remainder by C_base epsilon^2. This proves
joint Frechet differentiability into continuous trajectories. Below we
derive a quantitative bound for this derivative, rather than only its
existence. The initial conditions enter linearly in the original variables.

## 2. A positive frame at the zero-curvature point

Fix an auxiliary number 0<h<=1 for now. Define on the whole real line

    w_h(M)=(h^2+M^2)^(3/2)/(1+M^4)^2 > 0,
    l_h(M)=w_h'(M)/w_h(M)
          =3M/(h^2+M^2)-8M^3/(1+M^4).              (5)

There is no singularity at M=0. The following bounds hold for all M and h:

    |l_h(M)| <= 3/(2h)+8,
    w_h(M) <= 2^(3/2),
    1/w_h(M) <= 4 h^(-3)(1+|M|^5),
    |b(M)/w_h(M)| <= 4e,
    |b(M) w_h(M)| <= 4e 2^(3/2).                   (6)

For the first inequality, 2h|M|<=h^2+M^2 and |M|^3/(1+M^4)<=1
suffice. If |M|<=1 the numerator of w_h is at most 2^(3/2), while if
|M|>=1 it is at most 2^(3/2)|M|^3 and the denominator is at least
|M|^8. For its inverse, use the denominator of (h^2+M^2)^(3/2) at least
h^3 when |M|<=1, and at least |M|^3 when |M|>=1. The quotient b/w_h
is exactly -4e M^3/(h^2+M^2)^(3/2). The last bound also follows from
|b|<=4e and the upper bound on w_h.

The crucial identity, valid also at M=0, is

    b'(M)-l_h(M)b(M)
      =-12e h^2 M^2/[(h^2+M^2)(1+M^4)^2].          (7)

For M!=0 it follows by subtracting l_h from
b'/b=3/M-8M^3/(1+M^4), and inserting b. The displayed rational
identity extends continuously to zero, where both sides vanish. Therefore

    |b'-l_h b| <= 12e h^2.                         (8)

This is an algebraic cancellation, not an assumption on the signs of M,
V, p, or q. Crossings of zero are permitted throughout.

## 3. Full moving-frame variational equation

Let (u0,v0,r,s) denote an arbitrary simultaneous perturbation of
(M0,V0,p,q). Write the resulting first variation as (m,v), and put

    u(t)=m(t)/w_h(M(t)).

The original variational equations are

    m'=(b p+V b' q)m+b q v+a r+V b s,
    v'=b q m+a s.                                 (9)

Applying the product rule to u and using M'=a p+V b q gives EXACTLY

    u'=[(b-a l_h)p+V(b'-l_h b)q]u
         +(b/w_h)q v+(a/w_h)r+(Vb/w_h)s,
    v'=b w_h q u+a s.                            (10)

The initial value is (u0/w_h(M0),v0). In particular the base p term
survives: it is not replaced by a zero-forcing propagator. Both r and s
are arbitrary signed L1 directions, including late concentrated injections.
Every identity in (10) is valid almost everywhere along the AC base path.

The induced matrix one-norm of the homogeneous part of (10) is at most

    C_e [(1+h^(-1))|p|+(1+h^2 |V|)|q|].            (11)

For the first diagonal term use |b|+L|l_h|. For its q term use (8);
for both off-diagonal entries use (6). Thus (11) bounds the sum of
absolute values in each column and makes no sign or commutation assumption.

Set A=Q(|V0|+LQ). The integral of the right side of (11) is at most

    C_e [P+P/h+Q+h^2 A].                          (12)

The transition matrix on any subinterval therefore has norm at most the
exponential of (12): the m-fold ordered integral of the integrable
coefficient norm is bounded by its total integral to power m divided by m!.
Summing that convergent series proves this transition bound and the usual
variation-of-constants formula directly.

Using (4),(6) in both forcing terms of (10), and then multiplying u by
the bounded factor w_h(M) to recover m, proves

    sup_t (|m(t)|+|v(t)|)
      <= C_e h^(-3) R^10 exp(C_e[P+P/h+Q+h^2 A])
           [|u0|+|v0|+||r||_1+||s||_1].          (13)

Indeed a/w_h<=4L h^(-3)(1+sup|M|^5)<=C_e h^(-3)R^10;
|Vb/w_h|<=4e sup|V|<=C_e R, and a<=L. The initial inverse
weight is at most 4h^(-3)(1+|M0|^5), covered by the same prefactor.
The bound on w_h in (6) completes the conversion back to physical variables.

## 4. Balancing the proof weight, with no change to the model

Choose the constant weight parameter for the fixed base input to be

    h=min{1,[(1+P)/(1+A)]^(1/3)}.                  (14)

This choice is made after deriving (13) for every h. No derivative of this
choice is taken: the moving-frame equations use one fixed positive h while
varying the solution. It is only a proof device, not a model parameter.

If P<=A, the two quantities P/h and h^2 A are each at most
(1+P)^(2/3)(1+A)^(1/3). If P>A, h=1 and A<P. Thus in both cases

    P+P/h+Q+h^2 A
      <= C [P+Q+(1+P)^(2/3)(1+A)^(1/3)].          (15)

Since P,Q,|V0|<=R and R>=1, A<=C_e R^2. It follows that (15) is at
most C_e R^(4/3). Also

    h^(-3)=max{1,(1+A)/(1+P)} <= 1+A <= C_e R^2.

Substitution into (13) proves (2).

## 5. Moment implication and exact remaining scope

The maps P,Q and R are measurable for random L1 inputs, and the solution
derivative is given by the integral equation above. If E exp(lambda R^2)
is finite, then for any fixed k>0 the function

    R^(12k) exp(k C_e R^(4/3)-lambda R^2),   R>=1,

is bounded: its logarithm tends to negative infinity. Multiplication by
exp(lambda R^2) and expectation proves that the upper bound in (2) has
a finite k-th moment. Polynomial prefactors do not impose a threshold.
No independence among the input coordinates and drivers is needed.

The hypothesis holds if the four quantities |M0|, |V0|, P, Q each have
some positive square-exponential moment: R^2 is at most five times the
sum of their squares plus one, and Holder with four equal exponents applies
after reducing lambda. It does not follow from their ordinary L2 bounds or
from the assertion that each has all finite polynomial moments.

This proves the full arbitrary-p and arbitrary-q local response estimate
for the original quartic-flat activation. It does NOT claim a response
uniform over unbounded drivers using only the original initial state;
the known late-injection amplification is consistent with (2). It also
does not prove a finite-angle network transfer, source-driver tails,
trained-operator transport estimates, higher-order response, or nonlinear
removal of caps. Those remain separate proof obligations for the goal.
