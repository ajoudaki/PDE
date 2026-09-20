# Necessary growth of a uniformly decaying loss-controlling potential

Status: direct analytic result for the exact initialized d=3, p=1 closure.
This note uses established initialization and dynamics only. It will also
apply any independently verified hitting-time bound obtained in this study.
It supplies necessary lower bounds, not a construction or an upper bound
on the size of an optimal potential.

## 1. A general close-pair delay from physical path energy

Write x_i=sqrt(3) v_i with |v_i|=1, positive probability masses p_i, and
y_i in {+1,-1}. On the fixed joint mark spaces, let theta=(w,c,M), with
theta_0=(g,0,D), using the full d=3 p=1 marks of docs/observable_p1.md.
The raw norm is the direct sum of the two population L2 norms and the
coefficient Frobenius norm. Let d_*=||D||op, an explicit fixed constant
sqrt(d_h^2+d_k^2) in that chapter's active-coordinate formula.

The physical gradient identity and L(0)=1 give

  ||theta(t)-theta_0||raw^2
      <= t integral_0^t ||theta'(s)||raw^2 ds = t(1-L(t)).       (1)

In particular ||c||2<=sqrt(t), ||M||op<=d_*+sqrt(t), and
||w||2<=sqrt(3)+sqrt(t). Both dictionary synthesis maps have norm at
most one: their covariance matrices are at most the identity by the
ridge-Cholesky normalization. Since phi=tanh is 1-Lipschitz, the exact
forward equations therefore imply

  |f_t(v)-f_t(v')|
    <= ||c||2 ||M||op ||w||2 |v-v'|
    <= sqrt(t)(d_*+sqrt(t))(sqrt(3)+sqrt(t)) |v-v'|.           (2)

Indeed a(v)-a(v') is the dictionary analysis of
phi(w.v)-phi(w.v'); the upper feature difference is bounded in L2 by
|M(a(v)-a(v'))|; the readout is its L2 pairing with c. This calculation
retains every trained block and the canonical metric.

Suppose y_i=-y_j and delta=|v_i-v_j|>0. For any

  0<ell<4p_i p_j/(p_i+p_j),
  b_ell=2-sqrt(ell(1/p_i+1/p_j))>0,

weighted Cauchy--Schwarz yields, whenever L(t)<=ell,

  |f_t(v_i)-f_t(v_j)|
    >=2-|r_i-r_j| >=2-sqrt(L(t)(1/p_i+1/p_j)) >=b_ell.

Consequently the hitting time tau_ell=inf{t:L(t)<=ell}, with infinity
allowed, satisfies

  tau_ell >= h^{-1}(b_ell/delta),
  h(t)=sqrt(t)(d_*+sqrt(t))(sqrt(3)+sqrt(t)).                  (3)

h is continuous and strictly increasing on [0,infinity). Because
h(t)/t^(3/2)->1, (3) gives tau_ell=Omega(delta^(-2/3)) as the
opposite-label pair collides while its masses stay fixed. This bound does
not assert that tau_ell is finite. Stronger cancellation-sensitive bounds
can and should replace (3) for special configurations.

## 2. What any stronger delay forces on a proposed potential

Fix one data law and suppose a current-state functional Phi, with fixed
data and initialization information permitted, satisfies along its actual
initialized trajectory

  Phi(t)>=0,   Phi'(t)<=-lambda Phi(t),
  L(t)<=C Phi(t)^alpha,                                    (4)

where lambda,C,alpha>0 and Phi(0)<infinity. The same conclusion holds if
t -> Phi(theta(t)) is continuous and its upper-right Dini derivative
satisfies D^+Phi(t)<=-lambda Phi(t) at every time. Continuity is required
for that variant; an arbitrary current-state functional need not have it.
Integrating (4) gives

  L(t)<=C Phi(0)^alpha exp(-alpha lambda t).

For any known lower bound tau_ell>=T, use t<T, when L(t)>ell, and let
t increase to T. The result is

  Phi(0)>=(ell/C)^(1/alpha) exp(lambda T).                   (5)

Thus a delay T growing as delta^(-q), for a fixed positive loss
threshold, forces at least exp(c delta^(-q)) initial growth if lambda
has a common positive lower bound across that family and C,alpha are
uniform. In particular (3) already forces a stretched exponential
necessary growth near a close opposite-label pair. A sharper delay
exponent yields a sharper necessary growth immediately.

There are essential qualifications:

* A geometry-dependent lambda may tend to zero instead. The invariant
  constraint is lambda tau_ell <= log(Phi(0))
  +(1/alpha)log(C/ell), not a preferred allocation to rate versus size.
* A geometry-dependent domination constant C can absorb part of the
  difficulty. Its dependence must be included in any comparison.
* This is a lower bound on necessary size; it neither maximizes an
  unknown functional nor establishes its correct asymptotic order.
* Exponential decay under an unrestricted monotone loss transformation
  does not imply exponential loss decay. For instance L'=-L^2 gives
  Phi=exp(-1/L) and Phi'=-Phi, but L=1/log(1/Phi). Formula (5) is for
  the stated power domination; analogous bounds use any declared
  inverse threshold of another monotone domination function.

These observations separate a slow beginning from a slow terminal tail.
A fixed-threshold lower bound along increasingly degenerate data does
not disprove an eventual exponential rate for each separately fixed
nondegenerate member.

## 3. Exact contradictory limit

If all v_i coincide and the binary labels have equal total mass, every
state makes the same prediction on those inputs and

  L=1+f(v)^2>=1.

At canonical initialization c=0, the readout gradient cancels and both
other gradients vanish. The initialized state is stationary. It cannot
admit a finite potential satisfying (4) with positive lambda. This
exactly contradictory limit is an architectural/data obstruction; it
must not be called a nondegenerate three-input failure.
