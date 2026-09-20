# Exact architectural loss floor for weighted three-input laws

Status: analytic candidate, independently derived by the lead author during
the weighted-classification continuation. No trajectory or quadrature is
used as input. Sources are the exact canonical initialization in
docs/observable_p1.md, this study's complete initialization_positivity.md,
and the elementary three-feature dependence argument in terminal_geometry.md.

Inputs x_i have norm sqrt(3), labels y_i are +/-1, and p_i>=0 sum to one.
Discard zero-weight atoms. Repeated and antipodal inputs are allowed in this
statement so that its obstruction set is complete. Actual positive-weight,
distinct-input laws are a subcase. The full closure is bias-free and odd
in x at every state; all initialization, ridge and metric conventions are
unchanged.

## 1. The initialized coefficient distinguishes every input modulo sign

The previously proved exact initialization formula is

  D a_0(x)=(T(x_1/sqrt(3)),T(x_2/sqrt(3)),T(x_3/sqrt(3))),

where, using independent standard Gaussians G,V,

  T(r)=E[Psi(phi(G)) phi(rG+sqrt(1-r^2)V)], phi=tanh.

The complete canonical conditional coefficient Psi, including the actual
reverse response and ridge subtraction, is odd and strictly positive on
(0,1]; this is proved in initialization_positivity.md, not a numerical
premise. The subscripts x_j in this paragraph denote vector coordinates.

In fact T is strictly increasing on [-1,1]. To prove this, fix g>0 and
0<=r<1 and put

  m_r(g)=E_V phi(rg+sqrt(1-r^2)V).

Differentiation and Gaussian integration by parts give

  partial_r m_r(g)
    =g E phi'(rg+sqrt(1-r^2)V)-r E phi''(rg+sqrt(1-r^2)V)
    =g E phi'(rg+sqrt(1-r^2)V)
       +2r E[phi(rg+sqrt(1-r^2)V)phi'(rg+sqrt(1-r^2)V)]>0.  (1)

The last expectation is positive for r>0. Its integrand is odd and
positive on the positive half-line, and pairing positive and negative
arguments leaves the positive density difference of a Gaussian shifted
by rg>0. At r=0 the second term is zero and the first is strictly positive.
Every integration by parts has bounded integrands and a Gaussian boundary
term tending to zero. Differentiation of T on compact subintervals of
(-1,1) is justified; after (1) the derivative is bounded by a constant
times |G|+2, an integrable function.

m_r(g) is odd in g. Multiplication by Psi(phi(g)), which has its sign,
and integration therefore give T'(r)>0 for 0<=r<1. Oddness of T gives
strict increase also for negative r. Continuity at +/-1 follows from
dominated convergence, and extends strict increase to the closed interval.

Consequently D a_0(x) is nonzero on the sphere and

  D a_0(x)=+/-D a_0(x')  iff  x=+/-x'                      (2)

with the same selected sign. This excludes a hidden initialized collision
of different input directions caused by the finite dictionary.

## 2. Arbitrary values can be assigned on distinct antipodal pairs

Choose one representative v_G on the raw sphere from each equivalence
class x~(-x) among the active data. There are at most three classes.
By (2), the coefficient vectors z_G=D a_0(v_G) are nonzero and distinct
modulo sign. Define initialized upper features

  H_G(b2)=phi(b2^T z_G).

These functions are linearly independent in the upper population L2
space. Indeed its mark law has positive density on an open cube about
zero. An almost-sure linear relation is therefore an identity on that
cube by continuity. Choose a vector e such that t_G=e.z_G are nonzero
with distinct squares, avoiding a finite collection of proper hyperplanes.
Restrict the identity to b2=t e for small t. The first m<=3 nonzero odd
Taylor coefficients of tanh give the Vandermonde system

  sum_G a_G t_G^(2n+1)=0, 0<=n<m,

whose determinant is nonzero. Thus all coefficients vanish. This proof
uses only the coefficients 1,-1/3,2/15 of tanh.

The Gram matrix K_GH=E2[H_G H_H] is positive definite. For any prescribed
real values m_G, choose

  c_*(b2)=sum_G (K^(-1)m)_G H_G(b2), w=g, M=D.             (3)

This is a bounded legitimate readout on the unchanged canonical mark
space, and its prediction at v_G is exactly m_G. The same state predicts
the negative value at -v_G. It lies in the initialized odd parity sector.
Equation (3) is an expressivity construction, not a claim that training
selects it or that hidden layers stay frozen during actual training.

## 3. Exact minimum and its compatibility condition

Write x_i=sigma_i v_G in each class, sigma_i in {+1,-1}, and define

  W_G=sum_(i in G) p_i,
  m_G=(1/W_G) sum_(i in G) p_i sigma_i y_i.

For every current state, oddness and completion of the square give

  L(S)=L_odd+sum_G W_G(f_S(v_G)-m_G)^2,
  L_odd=sum_G W_G(1-m_G^2).                               (4)

All terms are finite; W_G>0 by the active-class definition. The readout
construction (3) attains all m_G simultaneously. Thus L_odd is exactly
the global minimum over closure states, already achievable with the
initialized hidden coordinates. In particular

  L_odd=0 iff y_i=sigma_i m_G for all active i,
                with m_G in {+1,-1} for each class.         (5)

Equivalently, coincident inputs must have equal labels and antipodal
inputs must have opposite labels. If no two active inputs coincide up
to sign, the data can always be fitted exactly by this closure, regardless
of input linear dependence or label-weighted first-moment cancellation.

No dynamics conclusion for every compatible law follows from (3)--(5).
A positive initialized plateau above L_odd would be an optimization
failure. Reaching a positive L_odd is instead convergence to the best
prediction permitted by the architecture.

## 4. Exact initial stationarity has no available fitting signal

At initialization c=0, so the w and M velocities vanish and

  c'(0)=2 sum_i p_i y_i H_0(x_i)
       =2 sum_G W_G m_G H_G.

The linear independence proved in Section 2 implies

  L'(0)=0 iff every m_G=0 iff L_odd=1.                     (6)

For such a law all three velocities vanish at the initialized state,
and uniqueness makes it stationary forever. Formula (4) shows that
there is no lower-loss odd predictor to learn: L(S)>=1 for every state.
Every law with L_odd<1 has strict initial loss descent, even if its
long-time optimization behavior is otherwise unknown.

This explains why the asymptotic slow-start set is more restrictive
than zero label-weighted input mean. Zero initial signal annihilates
the full family of initialized nonlinear features, rather than only
their first input moment.
