# A signed Hessian bound already fails at the canonical Gaussian initialization

Root candidate, 2026-09-06. UNREVIEWED. This is an initial-state theorem
for the actual finite random model, not a counterexample to existence or
convergence of its population flow. No experiment or external theorem is
used. It tests one proposed deterministic stability estimate only.

Fix d, two inputs x_a in R^d with x_a^T x_a/d=1 and
C_ab=x_a^T x_b/d, rho=C_12 in [-1,1). Fix y_a in {-1,1}. Use

  phi(z)=1+0.1 atan(sinh z).

There are three hidden layers, all of width n. W^(1) is n by d;
W^(2),W^(3) are n by n; the RESCALED output vector is W^(4).
Initialize independently with entries

  W^(1)_ij ~ N(0,1/d),  W^(2)_ij,W^(3)_ij ~ N(0,1/n),
  W^(4)_i ~ N(0,n^(-2)).

Let z^(1)_a=W^(1)x_a, z^(ell)_a=W^(ell)h^(ell-1)_a for ell=2,3,
h^(ell)_a=phi(z^(ell)_a), f_a=(W^(4))^T h^(3)_a/n and
L=(f_1-y_1)^2+(f_2-y_2)^2. The raw metric squared is

  d||dW^(1)||_F^2/n + ||dW^(2)||_F^2 + ||dW^(3)||_F^2
                                      + ||dW^(4)||_2^2/n.       (1)

Run the actual negative gradient flow of L in this constant metric,
with physical time t. In particular its readout equation is
dot W^(4)=-2 sum_a(f_a-y_a)h^(3)_a; neither the residual nor the
initial small readout is deleted from the actual dynamics.

Let J_n(theta) be the Jacobian of this full negative-gradient vector
field, interpreted as a self-adjoint operator in (1). Let dot J_n(0)
be its material derivative along the actual physical flow. For each
fixed real kappa and each fixed M,

  P{lambda_max[dot J_n(0)-kappa J_n(0)^2]>M} -> 1.       (2)

At the same time all initial primal norms in (1) for the first weights
and readout, and the operator norms of both hidden matrices, are bounded
in probability. The initial ||J_n(0)||_op is bounded in probability.
Thus an upper bound in (2)'s operator order by a finite function of
these bounded primal norms and the initial Jacobian norm cannot hold
uniformly in width on the canonical initialized laws, if that function
is bounded on bounded sets. No statement against a bound involving
additional history, averaged norms, or a distributional response is made.

## 1. Elementary initial norm and forward-law facts

The activation is bounded between 5/6 and 7/6, its first derivative is
positive and at most 1/10, and its first three derivatives are bounded.
Its second derivative is -0.1 sech(z)tanh(z), nonzero on (1,2).
These assertions follow by differentiating atan(sinh z); boundedness
also follows from |atan|<pi/2 and pi<10/3.

Both initial hidden matrix norms are at most 10 with probability tending
to one. One direct verification uses a 1/4-net of the unit sphere with
at most 9^n points, obtained from a maximal separated set and disjoint
ball volumes. For two such nets, each u^T W v is centered Gaussian of
variance 1/n. Its tail at 5 is at most 2 exp(-25n/2), by the Gaussian
exponential-moment bound. The union bound over at most 81^n pairs tends
to zero, and approximation of both unit arguments gives
||W||_op<=2 max_net |u^T W v|<=10.

Also ||W^(4)_0||_2/sqrt(n)<=2/n with probability tending to one,
because n||W^(4)_0||_2^2 is an average of n squared standard Gaussians,
with mean one and variance 2/n. The first-weight metric norm is bounded
in probability by the same elementary squared-Gaussian averaging; d is
fixed. Denote by E_n these norm events together with the converging
feature Gram events below. They have probability tending to one.

At layer one the initialized neuron pairs are iid N(0,C). Set, on
separate population spaces,

  (Z^(1)_1,Z^(1)_2) ~ N(0,C),
  K^(ell)=E[H^(ell)(H^(ell))^T], H^(ell)=phi(Z^(ell)),
  Z^(2) ~ N(0,K^(1)), Z^(3) ~ N(0,K^(2)).                 (3)

The feature second-moment matrices K^(1), K^(2) are positive definite.
For an interior rho, a homogeneous linear relation between two features
would extend by positive Gaussian density and continuity to all pairs
of real arguments. Strict monotonicity then forces both coefficients
to vanish. At rho=-1 the two features are 1+b(G),1-b(G), with nonconstant
odd b. Their constant and odd parts are linearly independent. This
proves positive definiteness first at layer one, then at layer two by
the nonsingular Gaussian argument. The same argument applies at layer
three. In particular each scalar variance is positive.

The empirical feature Grams K^(ell)_n converge in probability to (3).
Indeed, given the preceding feature array, new Gaussian rows are iid
with covariance its empirical second moment. Conditional variances of
bounded continuous test averages are O(1/n). Their means are continuous
in the covariance, including singular covariances, by coupling through
the positive matrix square root and bounded convergence. Induction
proves the claims and their jointness by a finite union bound. The
needed polynomial moments of Gaussian forward rows follow by the same
conditional Gaussian moments. All neuron populations remain separate.

## 2. One actual reused-matrix initialization query

Define the following statistic using the initialized hidden parameters:

  V_n=(1/2)sum_a y_a h^(3)_(0,a),
  U_(n,a)=V_n phi'(z^(3)_(0,a)),
  R_(n,a)=(W^(3)_0)^T U_(n,a).                            (4)

This statistic does not replace the actual initialized readout. It is
the derivative of a zero-readout auxiliary feature field used to expose
the leading material-Hessian term; Section 5 controls the actual small
readout and actual physical velocity explicitly.

The joint empirical law of (z^(2)_(0,i),R_(n,i)) converges in probability
to

  (Z^(2), R),  R=Gamma H^(2)+zeta,
  zeta ~ N(0,S), zeta independent of Z^(2),
  V=(1/2)sum_a y_a phi(Z^(3)_a),
  U_a=V phi'(Z^(3)_a), S=E[UU^T], Gamma=E[Jacobian U(Z^(3))]. (5)

Here is the direct conditioning proof. Write H for the n-by-2 array
h^(2)_0 and Z=W^(3)_0 H. Conditional on the preceding arrays and Z,

  W^(3)_0=Z(H^T H)^(-1)H^T + G(I-Pi_H),
  R_n=H(K^(2)_n)^(-1)(Z^T U_n/n)+(I-Pi_H)b,

where G is a fresh independent Gaussian matrix with entry variance 1/n,
Pi_H is orthogonal projection onto the columns of H, and b has independent
Gaussian rows with covariance U_n^T U_n/n. This follows by splitting
isotropic Gaussian rows into their orthogonal projections. The input
U_n is a bounded smooth function of the already revealed Z; it does not
depend on the remaining Gaussian residual.

Conditional averaging of the Gaussian Z rows gives convergence of the
two empirical coefficients. The rank-two projection error obeys

  E[||Pi_H b||_F^2/n | H,Z] = 2 tr(U_n^T U_n/n)/n -> 0.

Before that projection, conditional row averaging of a bounded Lipschitz
test of (z^(2)_(0,i),b_i) has variance O(1/n). Its mean converges by the
old empirical law and the converging Gaussian covariance. This proves
joint empirical averages, not just a tagged-coordinate law. The L2
projection error preserves that convergence. Finally Gaussian density
integration by parts gives E[U(Z^(3))(Z^(3))^T]=Gamma K^(2);
the bounded functions and derivatives justify the vanished boundary
terms. This proves the coefficient in (5).

For either label configuration S_aa>0. The top pair has positive density
on the plane, and V is nonzero on a nonempty open set: for equal labels
it never vanishes, and for opposite labels strict monotonicity gives
V!=0 when its two arguments differ. Its multiplication by positive
phi' cannot vanish on that set. Thus, conditionally on Z^(2), R_a has
a Gaussian variance S_aa>0 and a bounded mean.

Consequently the real variable

  y_a phi''(Z^(2)_a) R_a                                (6)

has both unbounded tails. For example, restrict Z^(2)_a to a compact
subinterval of (1,2), where |phi''| has a positive lower bound, and
restrict the other coordinate to a compact interval. That event has
positive probability. The conditional Gaussian variance in (5) remains
strictly positive; arbitrarily positive or negative values in (6) then
have positive probability. For each fixed tail level one may choose a
bounded open rectangle inside the event and a nonnegative Lipschitz
bump supported there. Its limiting empirical average is positive.
Thus with probability tending to one at least one neuron exceeds any
prescribed fixed level in (6), in either direction. This uses (5), not
an iid assertion about the finite reused queries or an extreme-value
approximation with a growing threshold.

## 3. Uniform derivative bounds in the raw metric

Let alpha denote the three hidden raw parameter blocks, with the hidden
part of metric (1), and write

  V(alpha)=(1/2)sum_a y_a h^(3)_a(alpha),
  g(alpha,w)=w^T V(alpha)/n, w=W^(4).

Gradients and Hessians are always computed in (1). On the event that
both hidden operator norms are at most 10, the following multilinear
bounds hold at the initialized hidden parameters:

  ||D^j V[eta_1,...,eta_j]||_2/sqrt(n)
     <= C_j n^((j-1)/2) product_b ||eta_b||_raw, j=1,2,3. (7)

The same bounds hold for either single-sample top feature map. Constants
do not depend on n. To verify them, the first raw variation satisfies
||dW^(1)x_a||_2/sqrt(n)<=sqrt(d/n)||dW^(1)||_F, since ||x_a||=sqrt(d).
For coordinate products,

  ||v_1 ... v_j||_2/sqrt(n)
     <= n^((j-1)/2) product_b (||v_b||_2/sqrt(n)),

by bounding j-1 factors by their Euclidean norm. The first three scalar
chain rules, bounded activation derivatives, and this inequality give
the asserted powers for the first features. At each later layer,
d(W h)=(dW)h+W dh, and higher derivatives add only terms with one dW
and one lower derivative of h. Use ||dW||_op<=||dW||_F and the bounded
initial operator norm. Induction proves (7) for every mixed variation.

Let B=Hessian g. Its readout/readout block is zero; its hidden/readout
blocks have norm at most C by (7), and its hidden/hidden block has norm
at most C sqrt(n) ||w||_2/sqrt(n). Thus on E_n,

  ||B||_op<=C, ||Hessian f_a||_op<=C,
  ||gradient f_a||_raw<=C.                               (8)

We will also use the exact bounds on pure hidden variations

  |D^2 g[v,v]|<= C sqrt(n)(||w||_2/sqrt(n))||v||_raw^2,
  |D^3 g[e,v,v]|<= C n (||w||_2/sqrt(n))
                                  ||e||_raw ||v||_raw^2. (9)

These bounds do not assert a width-uniform third derivative. Their
explicit n-dependence is needed to handle the actual tiny readout.

## 4. A unit matrix direction exposes the unbounded scalar coefficient

Fix a sample a, for example a=1. Let H_1 be the initial n-by-2 first
feature array and K^(1)_n=H_1^T H_1/n. Put

  v_row=H_1(K^(1)_n)^(-1)e_a
                 /sqrt(n[(K^(1)_n)^(-1)]_aa).

It is a unit Euclidean vector, and
v_row^T h^(1)_(0,b)=sqrt(n) 1_(a=b)/sqrt([(K^(1)_n)^(-1)]_aa).
For each neuron i choose a raw variation v_i whose only nonzero block
is row i of W^(2), equal to v_row. Its raw norm is exactly one.
Let d_a^2=1/[(K^(1)_n)^(-1)]_aa. It converges to a strictly positive
constant and is bounded above by (K^(1)_n)_aa<=a_0^2, a_0=7/6.

For this variation only sample a has a nonzero second-layer variation:

  dz^(2)_(0,b)=sqrt(n)d_a e_i 1_(a=b),
  dz^(3)_(0,a)=sqrt(n)d_a phi'(z^(2)_(0,i,a)) W^(3)_(0,:,i),
  d^2z^(3)_(0,a)=n d_a^2 phi''(z^(2)_(0,i,a)) W^(3)_(0,:,i).

Define S_i=V_n^T D^2 V(alpha_0)[v_i,v_i]/n. Differentiating phi at
layer three gives the EXACT decomposition

  S_i=(y_a d_a^2/2) phi''(z^(2)_(0,i,a))R_(n,i,a)+E_i,
  E_i=(y_a d_a^2/2) phi'(z^(2)_(0,i,a))^2
              sum_k V_(n,k) phi''(z^(3)_(0,k,a))
                                           (W^(3)_(0,k,i))^2. (10)

There is no residual in R_n. The second term has |E_i|<=C uniformly
in i and n on E_n, since V_n and the derivatives are bounded and the
column's squared norm is at most ||W^(3)_0||_op^2. By (5)-(6),

  max_i S_i -> +infinity in probability,
  min_i S_i -> -infinity in probability.                (11)

For clarity, convergence here means exceeding every fixed threshold
with probability tending to one. The direction v_i may depend on the
initial array, as is permitted in an operator Rayleigh-quotient test.

## 5. Restore the actual small readout and the exact physical field

Write b_n=||w_0||_2/sqrt(n). On E_n, b_n<=2/n. At initialization
|f_a|<=a_0 b_n, and the actual physical velocity satisfies

  dot w_0=4V_n+e_w,  ||e_w||_infinity<=C b_n,
  ||dot alpha_0||_raw<=C b_n.                           (12)

Indeed dot w=-2 sum_a(f_a-y_a)h^(3)_a, and the hidden gradient of f_a
is (D h^(3)_a)^*w, of norm at most C b_n by (7). The residuals are
uniformly bounded. These are equations for the actual independent
Gaussian readout, not for a changed initial condition.

The raw metric is constant, so the material derivative of B is its
third derivative contracted with the actual velocity. On a pure hidden
unit direction v_i it is

  dot B(0)[v_i,v_i]
    =dot w_0^T D^2 V[v_i,v_i]/n
           +w_0^T D^3 V[dot alpha_0,v_i,v_i]/n
    =4S_i+O(sqrt(n)b_n+n b_n^2)=4S_i+O(n^(-1/2)).        (13)

The error is uniform in i. The first estimate uses (7), (12), and
Cauchy--Schwarz in the explicit pairing divided by n. The second uses
(7) with j=3. In particular (8), (11), (13) already imply divergence
of lambda_max(dot B-kappa B^2) for every fixed kappa.

To check the actual vector-field Jacobian as well, the identity
L=sum_a f_a^2-4g+2 gives

  J=4B-2 sum_a gradient f_a tensor gradient f_a
                         -2 sum_a f_a Hessian f_a,       (14)

where these rank-one operators use the raw metric. Equation (8) and
|f_a|<=C b_n give ||J(0)||_op<=C. On a pure hidden unit direction,
|D f_a[v_i]|<=C b_n. The derivative of the first rank-one sum in (14)
therefore has Rayleigh quotient O(b_n), using the bounded Hessian and
bounded physical velocity. Also |dot f_a|<=C and
|D^2f_a[v_i,v_i]|<=C sqrt(n)b_n. Finally,

  |(d/dt)D^2 f_a[v_i,v_i]|
                          <=C(sqrt(n)+n b_n^2)

by the single-sample version of (7) and (12). Differentiating (14)
therefore yields, uniformly over i on E_n,

  dot J(0)[v_i,v_i]=16S_i+O(n^(-1/2)).                  (15)

Every discarded term is bounded respectively by C b_n,
C sqrt(n)b_n, or C b_n(sqrt(n)+n b_n^2); all tend to zero on E_n.
Because J is self-adjoint, |J^2[v_i,v_i]|<=||J||_op^2<=C^2.
Equations (11),(15), and the Rayleigh variational bound now prove (2).
Finite smooth ODE existence suffices to define these derivatives at zero;
no population flow or interchange of time and width limits is assumed.

## 6. Logical boundary

This result, if its isolated audit is clean, is a typical-canonical-
initialization obstruction to a primal-only pointwise signed material-
Jacobian estimate. It strengthens an arbitrary-state diagnostic in a
specific way: the actual independent Gaussian initialization, including
the prescribed nonzero tiny readout, and the exact physical gradient
flow have been retained. It does not show a fixed positive-time failure,
an integrated response divergence, or loss of population existence or
uniqueness. Gaussian scalar tails can have finite moments of every order
despite their maximum over n neurons diverging. The global two-label
joint MF/GF/GD target remains open.
