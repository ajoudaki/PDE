# Exact two-sample geometry and the label-mode reduction

Root candidate, 2026-09-06. This is a reduction and route-obstruction
note, NOT a global two-sample theorem. No existence of an uncut population
flow is assumed in order to assert that it has already been constructed.
The sample-symmetry statements below have explicitly stated existence
and uniqueness premises.

## 1. Raw gradient, metric, and four kernel matrices

For self-contained scope, let n,d be positive integers,
W^(1) in R^(n by d), W^(2),W^(3) in R^(n by n), and W^(4) in R^n.
The initialization blocks are independent and have independent entries:
W^(1)_(ij)~N(0,1/d), W^(2)_(ij),W^(3)_(ij)~N(0,1/n),
and the rescaled W^(4)_i~N(0,n^-2). The zero-readout auxiliary
initialization, when specified below, replaces only W^(4)_0 by zero.
The intended population readout starts identically at zero.
Labels y_1,y_2 belong to {-1,1}.
Let x_1,x_2 in R^d obey ||x_a||^2=d, and set
C_ab=x_a^T x_b/d. Then C=[[1,rho],[rho,1]], with -1<=rho<1.
For each sample define z^(1)_a=W^(1)x_a,
z^(2)_a=W^(2)h^(1)_a, z^(3)_a=W^(3)h^(2)_a,
h^(ell)_a=phi(z^(ell)_a), and
f_a=(W^(4))^T h^(3)_a/n. The output weights are rescaled throughout.

For raw variations use the squared metric

  d||dW^(1)||_F^2/n + ||dW^(2)||_F^2 + ||dW^(3)||_F^2
                                      + ||dW^(4)||_2^2/n.

Define the residual-free backward fields for each sample by

  delta^(3)_a=W^(4) phi'(z^(3)_a),
  q^(2)_a=(W^(3))^T delta^(3)_a,
  delta^(2)_a=phi'(z^(2)_a)q^(2)_a,
  q^(1)_a=(W^(2))^T delta^(2)_a,
  delta^(1)_a=phi'(z^(1)_a)q^(1)_a.

Ordinary coordinate differentiation, in reverse layer order, gives

  df_a = (delta^(1)_a)^T dW^(1)x_a/n
       + (delta^(2)_a)^T dW^(2)h^(1)_a/n
       + (delta^(3)_a)^T dW^(3)h^(2)_a/n
       + (h^(3)_a)^T dW^(4)/n.

Therefore the metric gradient of f_a has blocks

  delta^(1)_a x_a^T/d,
  delta^(2)_a (h^(1)_a)^T/n,
  delta^(3)_a (h^(2)_a)^T/n,
  h^(3)_a.

For L=sum_a(f_a-y_a)^2, the raw update is exactly -eta_n grad L,
eta_n=n^-2. Multiplying the first update by x_b gives

  z^(1)_{b,+}-z^(1)_b
       =-2 eta_n sum_a C_ba(f_a-y_a)delta^(1)_a.             (1)

The gradient pairings give the four kernel entries

  K^(1)_ab=C_ab (delta^(1)_a)^T delta^(1)_b/n,
  K^(ell)_ab=[(delta^(ell)_a)^T delta^(ell)_b/n]
             [(h^(ell-1)_a)^T h^(ell-1)_b/n], ell=2,3,
  K^(4)_ab=(h^(3)_a)^T h^(3)_b/n.                           (2)

Every block matrix is positive semidefinite because it is a Gram matrix
of the corresponding parameter gradients. Thus, writing K=sum_ell K^(ell),

  dot f=-2K(f-y),     dot L=-4(f-y)^T K(f-y)<=0.             (3)

Here dots refer to finite GF dot theta=-grad L in physical time
t=k eta_n, not to an exact discrete prediction update. Differentiability
of phi suffices for the identities along an existing differentiable
solution. For a unique finite GF solution map we assume phi is C^2
(as for the shifted arctan below), hence the finite field is locally
Lipschitz, and restrict to its existence interval. At the population
level the formulas remain identities whenever the
displayed products and derivatives are justified in the raw Hilbert
parameter space; they are not substitutes for that justification.

The update to W^(1) has its row vectors in span{x_1,x_2}. Orthogonal
row components never move. For -1<rho<1, a first-layer variation with
sample values v_1,v_2 and no orthogonal component has squared metric

  (1/n) sum_i (v_{1,i},v_{2,i}) C^(-1) (v_{1,i},v_{2,i})^T. (4)

Indeed the unique in-span row is (v_1,v_2)(X^T X)^(-1)X^T,
where X has columns x_1,x_2 and X^T X=dC. Its ordinary squared norm
is (v_1,v_2)C^(-1)(v_1,v_2)^T/d. This proves (4) after multiplying
by d/n and summing. At rho=-1, x_2=-x_1 and z^(1)_2=-z^(1)_1
exactly; the in-span squared metric is ||v_1||^2/n.

## 2. Exact exchange symmetry, and what it does not assert

By the global label/readout sign symmetry it suffices in law to consider
y=(1,sigma), sigma in {1,-1}. Specifically, negating both labels and
W^(4) preserves the loss and all hidden raw updates, and negates the
readout update. The centered Gaussian readout initialization has this
symmetry. No finite realization is asserted to equal its sign transform.

Let v=(x_1-x_2)/||x_1-x_2||, and let R=I-2vv^T. Equality of input norms
gives R x_1=x_2 and R x_2=x_1. Define the parameter isometry

  S(W^(1),W^(2),W^(3),W^(4))
     =(W^(1)R,W^(2),W^(3),sigma W^(4)).                    (5)

The first three hidden fields on sample a at S(theta) are exactly the
fields on sample 3-a at theta. Therefore

  f_a(S(theta))=sigma f_{3-a}(theta),    L(S(theta))=L(theta).

Because S is a linear isometry of the raw metric, differentiating the
last equality gives grad L(S(theta))=S grad L(theta). Thus raw GD and
the unique finite GF solution map commute with S on their existence
intervals. The jointly independent initialization law specified above
is invariant under S:
isotropic Gaussian first-layer rows are unchanged by R, the two hidden
matrices are unchanged, and the independent centered readout is
unchanged in law by its optional sign.

Consequently the finite prediction paths obey the equality IN LAW

  (f_1(t),f_2(t))_t  =_law  (sigma f_2(t),sigma f_1(t))_t.  (6)

This is not a pathwise identity at finite width. If a deterministic
population prediction limit exists, (6) forces f_2=sigma f_1.
For random non-deterministic subsequential limits, symmetry in law alone
would not force that pathwise relation.

There is also a useful intrinsic population formulation. Write J_ell
also for the pullback on L^2 of a measure-preserving involution of
neuron space ell. It is a self-adjoint isometry and commutes with
coordinate functions. Suppose
J_ell W^(ell)_0=W^(ell)_0 J_(ell-1) for ell=2,3,
J_1 Z^(1)_{1,0}=Z^(1)_{2,0}, and
J_3 W^(4)_0=sigma W^(4)_0; the last condition holds for zero readout.
Consider the full state transformation

  Z^(1)_a -> J_1 Z^(1)_(3-a),
  W^(ell) -> J_ell W^(ell) J_(ell-1), ell=2,3,
  W^(4) -> sigma J_3 W^(4).

Assume the equations and uniqueness class are invariant under this
transformation and the constructed initial-value problem is unique
in that class. The listed premises fix its ENTIRE initial state, so
the transformed solution has the same initial data. Uniqueness proves

  Z^(ell)_2=J_ell Z^(ell)_1,
  J_ell W^(ell)=W^(ell)J_(ell-1), ell=2,3,
  J_3 W^(4)=sigma W^(4),     f_2=sigma f_1.                (7)

Building such common spaces is compatible with symmetric finite-program
laws, but that construction and the required flow uniqueness are separate
obligations. In particular (7) cannot assume the still-open uncut
uniqueness theorem.

## 3. The normalized label-mode feature field

On a population path satisfying (7), put

  g=(f_1+sigma f_2)/2=f_1.

Since r_1=g-1 and r_2=sigma(g-1), the physical parameter field is

  dot theta=4(1-g) grad g.                                (8)

This is an identity of the full parameter gradient, not merely the
gradient of a scalar restriction in an unspecified metric. With feature
time s defined by ds/dt=4(1-g), the reparameterization is valid only
where 1-g is nonzero and is increasing where g<1. For the intended
zero population readout g(0)=0. On an existing regular symmetric
physical trajectory, the chain rule gives

  1-g(t)=(1-g(0))exp{-4 integral_0^t ||grad g(theta(u))||^2 du}.

Thus g<1 persists on each compact interval on which that integral is
finite. Division by the clock there gives the feature field

  theta'=grad g,
  (z^(1)_b)'=(1/2)sum_a C_ba y_a phi'(z^(1)_a)q^(1)_a,
  (W^(ell))'=(1/2)sum_a y_a delta^(ell)_a
                                     (h^(ell-1)_a)^T/n, ell=2,3,
  (W^(4))'=(h^(3)_1+sigma h^(3)_2)/2.                    (9)

The population versions use the same factors 1/2, expectation rank-one
operators in place of outer products/n, and adjoints in place of
transposes. They have

  g'=||grad g||^2=(1/4)y^T K y.                           (10)

Thus a scalar clock can indeed be recovered after establishing symmetry.
To use it globally one must construct the feature flow up to its level
g=1 (or otherwise for the required clocks), not merely invoke symmetry.
At finite width the physical residual vector is not exactly in this
mode. Raw GD/GF comparison must control its other component separately;
one cannot assign the finite process the scalar clock (8) as an identity.

## 4. Why the one-input first-coordinate cancellation fails

For phi(z)=1+epsilon arctan z, epsilon>0 fixed, define
F(z)=(z+z^3/3)/epsilon. Then F'=1/phi'. Along (9), exactly,

  (F(z^(1)_b))'
    =(1/2)sum_a C_ba y_a
          [phi'(z^(1)_a)/phi'(z^(1)_b)] q^(1)_a.          (11)

For a=b the ratio is one. For a!=b it is
(1+(z^(1)_b)^2)/(1+(z^(1)_a)^2), which is not bounded on R^2.
For -1<rho<1, the initial two-dimensional Gaussian has full support.
The problematic ratios are therefore not removed simply by calling
the inputs normalized.

Nor can a different smooth invertible chart flatten both forcing
directions to two constant vectors when 0<|rho|<1. More precisely,
there is no C^2 local diffeomorphism on all of R^2 with constant invertible
matrix B such that

  D Psi(z) C diag(phi'(z_1),phi'(z_2))=B.                 (12)

To prove it, multiply Psi on the left by B^(-1). The Jacobian would be
diag(F'(z_1),F'(z_2)) C^(-1). In its first row, equality of mixed partials
requires

  0 = [C^(-1)]_12 F''(z_1)
    = -rho F''(z_1)/(1-rho^2).

For shifted arctan F''(z)=2z/epsilon, this fails on any open set
containing a point with z_1!=0. In fact the same calculation rules out
this constant-forcing flattening for every C^2 activation with positive
derivative and nonconstant F'=1/phi'. This is only a chart obstruction,
not an obstruction to the limiting dynamics.

At rho=0 the original componentwise cancellation does work. At rho=-1,
z^(1)_2=-z^(1)_1 and the shifted-arctan derivative is even, so (11)
instead reduces to

  (F(z^(1)_1))'=(q^(1)_1-sigma q^(1)_2)/2.              (13)

The generic correlated case must not be inferred from either exception.

## 5. The initial contrast signal is strictly positive, but small

This section uses only the initial forward Gaussian laws, which can be
proved without matrix reuse. In the POPULATION initialization limit,
for each hidden layer the initial sample
pair is a centered Gaussian pair with covariance equal to the preceding
feature second-moment matrix (and first-layer covariance C). This follows
by conditioning on the preceding features: distinct rows of the fresh
Gaussian matrix give independent Gaussian pairs with the empirical
feature covariance. At finite width the pairs are only conditionally
Gaussian at the second and third layers; their unconditional laws can
be Gaussian mixtures. The ordinary law of large numbers at the first
layer and conditional averaging at each later layer give convergence
of the covariance and of joint empirical averages. Bounded Lipschitz
activation transfers convergence through the three finite instructions.

Take phi=1+epsilon arctan and 0<epsilon<=1/10. We may use
m=5/6, a=7/6, so m<phi<a and |phi'|<=epsilon.
Let D_0=2(1-rho), and let

  D_ell=E[(H^(ell)_{1,0}-H^(ell)_{2,0})^2], ell=1,2,3.

The variance of the difference of the Gaussian preactivations in layer
ell is D_(ell-1). Each marginal preactivation variance is at most a^2.
For any such centered Gaussian pair U,V, put D=E(U-V)^2. Lipschitzness
gives the upper bound epsilon^2 D. For a lower bound set M=4a.
On {|U|,|V|<=M}, the mean-value formula gives

  |arctan U-arctan V| >= |U-V|/(1+M^2).

The scalar Gaussian tail bound gives
P(max(|U|,|V|)>M)<=4 exp(-M^2/(2a^2)).
As U-V is centered Gaussian, E(U-V)^4=3D^2. Cauchy--Schwarz therefore
bounds its squared-difference expectation on that exceptional event by
2 sqrt(3) exp(-4) D. This proof also holds for singular Gaussian pairs;
if D=0 both sides are zero. Define the explicit positive constant

  c=[1-2 sqrt(3) exp(-4)]/(1+16a^2)^2.

Then at every initial hidden layer

  c epsilon^2 D_(ell-1) <= D_ell <= epsilon^2 D_(ell-1).

In particular the initial opposite-mode readout kernel is

  (1/4)E[(H^(3)_{1,0}-H^(3)_{2,0})^2]=D_3/4,

and lies between

  (c^3 epsilon^6/2)(1-rho)
       and (epsilon^6/2)(1-rho).                          (14)

It is strictly positive for every rho<1, including rho=-1.
For the same-label mode, (H^(3)_{1,0}+H^(3)_{2,0})/2>=m,
so its initial readout kernel is at least m^2.
Equation (14) is an initial estimate only, not a lower bound along
training.

## 6. No angle-uniform short-feature-time fitting argument

Here is a deterministic fact explaining why simply retuning the old
small feature interval cannot handle the opposite-label case.
Suppose phi is bounded by a and Lipschitz with constant b, with
|phi'|<=b. Consider ANY finite uncut feature flow (9) for sigma=-1
on [0,S], from zero readout, with initial hidden operator norms <=M_0
and d||W^(1)_0||_F^2/n<=M_1^2. Constants below are uniform in rho.

Readout speed has norm/sqrt(n)<=a, so its norm/sqrt(n)<=aS.
The bounds on delta^(3), the rank-one updates, and then delta^(2) give

  sup||W^(3)||_op <= M_0+a^2 b S^2,
  sup||W^(2)||_op <= M_0+a^2 b^2 S^2
                                    (M_0+a^2 b S^2).

These deliberately loose bounds follow by bounding every integrand
by its maximum on [0,S]; the factor 1/2 and two samples cancel.
Let their right sides be M_3(S),M_2(S). Then
||delta^(1)_a||/sqrt(n)<=b^3 M_2(S)M_3(S)aS.
The first-weight metric speed is at most the average of these two
norms: the metric norm of delta_a x_a^T/d is ||delta_a||/sqrt(n).
Therefore

  sup sqrt(d)||W^(1)||_F/sqrt(n)
        <= M_1+a b^3 M_2(S)M_3(S)S^2 =: M_1(S).

Since ||x_1-x_2||=sqrt(2d(1-rho)), it follows that

  ||z^(1)_1-z^(1)_2||/sqrt(n)<=M_1(S)sqrt(2(1-rho)).

Two bounded matrix actions and three Lipschitz activations now yield

  |g(s)| <= (aS/2)b^3 M_3(S)M_2(S)M_1(S)
                                           sqrt(2(1-rho)), s<=S. (15)

All finite feature flows exist on every bounded [0,S] by these same
primal bounds and finite-dimensional smoothness, if phi is smooth.
For completeness, a nonzero initial readout with
||W^(4)_0||/sqrt(n)<=R_0 is covered as follows. Set

  B(S)=R_0+aS,
  Mtilde_3(S)=M_0+ab S B(S),
  Mtilde_2(S)=M_0+ab^2 S Mtilde_3(S)B(S),
  Mtilde_1(S)=M_1+b^3 S Mtilde_2(S)Mtilde_3(S)B(S).

The same sequential velocity bounds give these three parameter bounds
and

  |g(s)| <= [B(S)/2]b^3 Mtilde_3(S)Mtilde_2(S)Mtilde_1(S)
                                             sqrt(2(1-rho)).

At R_0=0 these are exactly the preceding bounds. For the stated Gaussian
initialization, d||W^(1)_0||_F^2/n converges to d in probability,
and E||W^(4)_0||^2/n=n^-2, so M_1>sqrt(d) and R_0=1 work with
probability tending to one. The two initial operator norms are at most
10 with probability tending to one: a 1/4-net on the unit sphere has
at most 9^n points, the operator norm is at most twice the maximum
bilinear form on two such nets, and Gaussian tails give
P(||W||_op>10)<=2*9^(2n) exp(-100n/8). The right side tends to zero.

Thus, for angle families in fixed dimension d>=2, the feature time
required to attain g=1 cannot be bounded uniformly as rho approaches
one under these angle-independent initial norm bounds. When d=1 only
rho=-1 is admissible, so this angle-family assertion is vacuous.

This does NOT violate the user's target: constants are allowed to depend
on rho. It disproves only the proposed strategy of reaching all
configurations' targets in one angle-independent short feature interval.
Neither (14) nor (15) rules out a long, globally stable nonlinear limit.

## Remaining obligations

The exact normalization and symmetry identities are available.
The two-sample local/clipped proof, a global actual-response estimate,
finite-width control of the off-mode residual, and all nontriviality
and full-limit/audit obligations are still open. No claim in this note
has been externally audited yet.
