# A convex affine-tail candidate: exact initial separation and finite dynamics

Root research note, 2026-09-06. Candidate activation, NOT a population
continuation theorem and not independently audited. No experiment.

The model, raw metric, initialization, loss normalization, and raw
GD step are exactly CONTRACT_AND_LEDGER.md. The single fixed activation
tested here is

  phi(z)=z+log(1+exp(z)).

This formula defines a mathematical function, not a suggested numerical
implementation. It is independent of the input angle and labels.
The reason for testing it is the combination of strictly positive
curvature, derivative bounded away from zero, and bounded logarithmic
gate range. These properties differ from the earlier affine-tail
candidate z+1+tanh(z)/2, whose curvature changes sign.

## 1. Elementary activation facts

Put p(z)=exp(z)/(1+exp(z)). Direct differentiation gives

  phi'(z)=1+p(z),       phi''(z)=p(z)(1-p(z)).

Thus 1<phi'<2, 0<phi''<=1/4, and

  0<log(phi'(z))<log 2,
  |phi(z)|<=2|z|+log 2.

All higher derivatives from order two onward are bounded: differentiate
a polynomial in p by the rule d/dz=p(1-p)d/dp on 0<=p<=1.
In particular the function is smooth, strictly increasing, strictly
convex, and not affine on any nonempty interval.

Two useful exact identities are

  phi(z)-phi(-z)=3z,
  phi(z)+phi(-z)=2 log(2 cosh(z/2)).

Also its Euler homogeneity defect has a sign and a uniform bound:

  phi(z)-z phi'(z)
       =-p(z) log p(z)-(1-p(z)) log(1-p(z))
       belongs to (0,log 2].

The last equality follows by substituting log p=z-log(1+exp z) and
log(1-p)=-log(1+exp z). The entropy expression is nonnegative and
has maximum log 2 by differentiation. No homogeneity or exact matrix
balance follows merely from this scalar identity.

## 2. Both initial label modes survive, including antiparallel inputs

At initialization, let (Z^(1)_1,Z^(1)_2) be the centered Gaussian pair
with covariance C. Set H^(1)_a=phi(Z^(1)_a). Recursively, for ell=2,3
let the centered Gaussian pair (Z^(ell)_1,Z^(ell)_2) have covariance

  E[H^(ell-1)_a H^(ell-1)_b],

and put H^(ell)_a=phi(Z^(ell)_a). This is the initial forward empirical
law, proved by conditioning on the preceding layer and averaging the
independent Gaussian rows. Gaussian moment bounds and the displayed
linear growth permit truncation of quadratic tests and convergence of
their empirical averages. Only initialization is being considered here;
no independence claim is made after matrix reuse or training.

All marginal variances are finite and positive. Finiteness follows
inductively from |phi(z)|<=2|z|+log 2. Positivity follows because a
nonconstant strictly increasing function of a nondegenerate Gaussian
cannot vanish almost surely. The two marginal laws are equal.

For any real u,v, the integral of phi' along the interval between them
gives

  |u-v| <= |phi(u)-phi(v)| <= 2|u-v|.

Writing D_0=2(1-rho) and D_ell=E|H^(ell)_1-H^(ell)_2|^2, the Gaussian
covariance definition therefore gives

  D_(ell-1) <= D_ell <= 4 D_(ell-1).

In particular the initial opposite-label readout-mode squared norm is

  (1-rho)/2 <= E|(H^(3)_1-H^(3)_2)/2|^2
             <= 32(1-rho).                              (1)

For a centered Gaussian Z, the preceding odd/even identities give

  E phi(Z)=E log(2 cosh(Z/2)) >= log 2.

Consequently the initial same-label readout-mode squared norm is at
least (log 2)^2. This is an INITIAL bound, not a pointwise positive
activation floor: phi is unbounded below.

Every initial feature second-moment matrix is positive definite.
For -1<rho<1, the root Gaussian pair has full support. If
c_1 phi(Z_1)+c_2 phi(Z_2)=0 almost surely, continuity and full support
make this identity hold for every real pair. Varying its first and
second coordinates and using strict monotonicity forces c_1=c_2=0.
At rho=-1 the asserted identity would instead read
c_1 phi(G)+c_2 phi(-G)=0 for every G. Its odd part, using the exact
identities above, forces c_1=c_2, and its nonzero even part then forces
both to vanish. Thus the first feature second-moment matrix is
positive definite even at the singular root. The same full-support
argument applies at subsequent centered Gaussian forward layers.

Strict distributional nonlinearity holds initially in every layer and
sample. Indeed, if phi(Z)=aZ+b almost surely for a nondegenerate
Gaussian Z, continuity and its full support imply this equality for
all real z, contradicting phi''>0. The best affine L2 approximation
exists (the span of 1,Z is finite dimensional), so its squared error
is strictly positive. This paragraph does not prove its persistence
after training.

## 3. Dimension-uniform finite-GF and exact-GD primal bounds

This section is a deterministic statement conditional only on the
initial primal bounds. It does not identify a population limit.
For a finite state write its primal size as the maximum of

  sqrt(d/n)||W^(1)||_F, ||W^(2)||_op, ||W^(3)||_op,
  ||W^(4)||_2/sqrt(n).

Suppose this size at initialization is at most M_0. Under the
prescribed independent Gaussian initialization this event has
probability tending to one for a sufficiently large fixed M_0
(depending on fixed d). The first and readout bounds follow from
Gaussian second moments and variance/averaging. For each hidden
matrix the elementary Gaussian sphere-net proof of the spectral norm
bound applies: take 1/4-nets of the two unit spheres of size at most
9^n, bound each scalar Gaussian bilinear form by its Gaussian tail,
and use the net approximation factor 2. A fixed sufficiently large
constant makes the resulting failure probability tend to zero.

An increment of raw Hilbert norm at most R raises every displayed
primal norm by at most R. For the hidden matrices use
||D W||_op<=||D W||_F. Hence the affine raw ball of radius R around
the initial state has primal size at most M=M_0+R.

On such a ball all sample forward and residual-free backward fields
have bounded RMS norms, with constants depending on M,d but not n.
For the forward direction use ||z^(1)_a||/sqrt(n)<=M and recurse with
H_1=2M+log 2, H_2=2M H_1+log 2, H_3=2M H_2+log 2.
For the backward direction use phi'<=2, the two operator bounds, and
the readout RMS bound. The exact raw gradient formulas then show

  |f_a|+|r_a|+||grad_raw L||_raw <= A(M)                 (2)

for a finite polynomially bounded A(M), enlarged when necessary.

The finite raw Hessian satisfies, on the same ball,

  ||Hess_raw L||_op <= B(M) sqrt(n), n>=1.              (3)

Here is a direct proof, including the dimension factor. For any raw
unit direction v, first forward directional derivatives have RMS norm
at most a constant depending on M: propagate
D z^(2)=D W^(2) h^(1)+W^(2)[phi'(z^(1)) D z^(1)]
and the analogous third-layer identity. For two raw unit directions
u,v, the mixed forward second derivative contains operator-direction
times first-derivative terms bounded in RMS without a dimension factor,
and activation terms phi''(z) D_u z D_v z. Their RMS norm is at most

  (1/4) sqrt(n) (||D_u z||/sqrt(n))(||D_v z||/sqrt(n)),

because ||D_u z||_infinity<=sqrt(n)||D_u z||/sqrt(n).
Propagation through bounded operators preserves a single sqrt(n)
factor; it does not introduce another product of two second
derivatives. The readout contraction is bounded by Cauchy--Schwarz
with its RMS norm. Thus |D_u D_v f_a|<=C(M)sqrt(n), whereas its first
derivative is bounded independently of n. Differentiate
L=sum_a(f_a-y_a)^2 to obtain (3). The raw metric is constant, so these
directional bounds are exactly the stated Hilbert-Hessian bound.

For finite GF, the exact identity

  dL/dt=-||grad_raw L||_raw^2

and Cauchy--Schwarz in time give raw path length at most
sqrt(T L(0)) on [0,T]. Equations (2) and the primal increment bound
prevent finite-dimensional escape, so the smooth finite GF exists
at every finite time, with dimension-uniform primal bounds on this
initial event.

For exact GD, eta=n^-2. Fix T. Choose a deterministic L_* bounding
L(0) on the initial event, and R>sqrt(2(T+1)L_*)+2. On the raw ball
of radius R, (2)--(3) hold with M=M_0+R. For all sufficiently large n,
eta A(M)<1 and eta B(M)sqrt(n)<=1. Taylor's integral remainder gives,
for every step whose segment stays in that ball,

  L(theta-eta grad L)
       <= L(theta)-(eta/2)||grad_raw L||_raw^2.        (4)

To remove the segment premise without circularity, induct up to the
first exit from the smaller ball of radius R-1. Its incoming step
has length at most eta A(M)<1 and so lies in the larger ball.
Summing (4) through that step and applying Cauchy--Schwarz gives

  sum_(j<k) eta ||grad_raw L(theta_j)||_raw
       <= sqrt(2 k eta L(0))
       <= sqrt(2(T+1)L_*),                            (5)

for k eta<=T+1. This is strictly below R-1, contradicting the first
exit. Thus (4)--(5) and the primal bound hold for every GD node
through time T, including its incoming segment when needed.
The raw interpolation shares the same bound.

Finally the differentiated forward maps have dimension-uniform RMS
operator bounds on these raw balls. Therefore the GF and recomputed
raw-GD hidden paths have uniformly bounded time-integrated squared
RMS velocities. At an interpolated GD point apply the forward
directional derivative at that point to its constant raw step slope;
this does not assign the current instantaneous gradient to that slope.
All four raw kernel blocks and predictions are likewise bounded by
(2) and Cauchy--Schwarz.

## 4. What this candidate has and has not achieved

This one activation preserves both initial label modes, has strict
initial nonlinearity, and has dimension-uniform finite GF/exact-GD
primal and path-action bounds without clipping. Its initial contrast
is not suppressed by the sixth power of a small nonlinear amplitude.
These are eligibility checks and finite-system estimates only.

The proposed new discriminator is SIGNED INTEGRATED curvature, using
phi''>=0 and the bounded range of log phi'. A separate frozen-top
calculation tests that mechanism. Its extension to the lower-layer
forcing of the actually trained network must be proved, not presumed.

This note proves neither uncut global population construction nor
unique restart, joint limit identification, global feature learning,
or every-finite-time distributional nonlinearity. RMS/action bounds
do not imply uniform query tails, and initial contrast positivity
does not discharge those missing obligations. The full two-label
target remains open.
