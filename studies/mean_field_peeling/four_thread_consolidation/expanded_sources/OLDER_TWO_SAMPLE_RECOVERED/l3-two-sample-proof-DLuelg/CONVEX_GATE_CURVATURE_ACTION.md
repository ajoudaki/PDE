# A monotone-gate activation and an actual curvature-action estimate

Root candidate, 2026-09-06. This is an activation discriminator and an
estimate on an EXISTING opposite-label feature-gradient trajectory. It
does not construct the global population trajectory, remove reference
cuts, establish a finite-width limit, or prove every-time nonfreezing.
No numerical experiment or nonclassical external theorem is used.

Fix, for all layers and all configurations,

    phi(z)=1+(1/10) log(1+exp(z)).                         (1)

The change is only the activation. It retains a positive feature floor
and bounded first and second derivatives, but loses the bounded feature
ceiling used in the established short-response proof. That loss is
material: in particular that proof's pointwise readout bound and numerical
constants are not imported here.

## 1. The property obtained, and why the old bounded class cannot have it

Put p(z)=phi'(z) only for the scalar calculations of this section, and
let sigma(z)=exp(z)/(1+exp(z)). Direct differentiation gives

    p= sigma/10,   phi''=sigma(1-sigma)/10=p-10p^2,
    0<p<1/10,     0<phi''<=1/40,     phi>=1.             (2)

Consequently, for all real x,y,

    |phi''(x)-phi''(y)| <= |phi'(x)-phi'(y)|,             (3)
    phi''(x)<=phi'(x),
    |phi'(x)-phi'(y)| <= |phi(x)-phi(y)|.                 (4)

For (3), the derivative of u-10u^2 on [0,1/10] is 1-20u,
of absolute value at most one. For the last inequality in (4), if x<y,
integrate 0<phi''(z)<=phi'(z) between them; the other ordering follows
by symmetry. Thus these are global inequalities, with no restriction
to a range of attained preactivations and no configuration-dependent
activation parameter.

Here is a precise obstruction to obtaining (3) inside the old bounded
monotone activation class. Suppose psi is bounded, nondecreasing,
nonconstant and C2 on R, with bounded derivative p=psi'. There is NO
finite C for which

    |p'(x)-p'(y)| <= C |p(x)-p(y)|   for all x,y.         (5)

Indeed p>=0, and its integral on R is the difference of the two finite
endpoint limits of psi. If (5) held, fixing y would give a uniform bound
on |p'|, since p is bounded. Thus p is uniformly continuous. An integrable
nonnegative uniformly continuous function tends to zero at both ends:
otherwise disjoint fixed-radius intervals around a sequence of points
with p>=epsilon would each have an integral bounded below, contradicting
integrability. Nonconstancy supplies a point with p>0. Its positive global
maximum is therefore attained at some finite x0, and p'(x0)=0. By (5),

    |p'(x)| <= C |p(x)-p(x0)|.

For x>=x0 on any fixed finite interval, integration gives
|p(x)-p(x0)|<=C integral_(x0)^x |p(u)-p(x0)|du. If F is the latter
integral, then F(x0)=0 and F'<=CF, so differentiation of exp(-Cx)F
gives F=0. The same argument backwards from x0 applies to x<=x0.
Thus p is its positive maximum everywhere, contradicting integrability.
The argument also covers C=0 directly. This proves the obstruction.

For an even gate whose odd derivative is nonzero at x, the gates at
x and -x are equal while their curvatures are opposite and nonzero.
Relation (3) fails at that pair.
The obstruction just proved concerns (5), not global MF/GF existence.

## 2. Exact two-sample population setup for the new estimate

There are separate probability spaces Omega_1, Omega_2, Omega_3.
Expectation E_ell always means integration over its own population.
Let W^(2):L2(Omega_1)->L2(Omega_2) and W^(3):L2(Omega_2)->L2(Omega_3)
be bounded operators with Hilbert--Schmidt increments. Define

    H^(ell)_a=phi(Z^(ell)_a),
    Z^(2)_a=W^(2)H^(1)_a,  Z^(3)_a=W^(3)H^(2)_a,
    f_a=E_3[W^(4) H^(3)_a],       a=1,2.

The first population contains the pair of first preactivations with
input covariance C=[[1,rho],[rho,1]], -1<=rho<1. For |rho|<1 the first
field metric is E_1[v^T C^(-1)v]. At rho=-1 use one field (Z,-Z),
with metric E_1 v^2. Readout metric is L2 and hidden matrix increment
metrics are Hilbert--Schmidt. These are exactly the raw metrics induced
by RMS-normalized inputs and the specified hidden-matrix normalization.
The first fields and readout belong to their respective L2 spaces at
each time; the assumed regular path has the time regularity required
for the integrated chain rule (7).

Labels are y=(1,-1), and g=(f_1-f_2)/2. The reverse fields contain NO
residual:

    delta^(3)_a=W^(4) phi'(Z^(3)_a),
    q^(2)_a=(W^(3))*delta^(3)_a,
    delta^(2)_a=phi'(Z^(2)_a)q^(2)_a,
    q^(1)_a=(W^(2))*delta^(2)_a,
    delta^(1)_a=phi'(Z^(1)_a)q^(1)_a.

All displayed fields belong to their own L2 spaces: phi has linear
growth, its derivative is bounded, and the operators are bounded.

The estimate assumes an existing regular feature-gradient path on [0,S]
with zero initial readout, g(0)=0, g(s)<=1, and

    (W^(ell))'=(1/2) sum_a y_a delta^(ell)_a tensor H^(ell-1)_a,
                      ell=2,3,
    (Z^(1)_b)'=(1/2)sum_a C_ba y_a delta^(1)_a,
    (W^(4))'=(H^(3)_1-H^(3)_2)/2.                       (6)

Here (u tensor v)h=u E[vh], and a prime is feature time. At finite
width the corresponding matrix is uv^T/n, not uv^T. Along the assumed
path the gradient chain rule and energy identity are REQUIRED premises:

    g'(s)=||theta'(s)||_raw^2,  hence
    integral_0^S ||theta'(s)||_raw^2 ds=g(S)<=1.         (7)

They hold for classical finite-dimensional feature-gradient paths, but
population differentiability/existence for the unbounded activation is
not asserted merely by defining its fields. In particular, (6)--(7) are
not asserted for internally cut references or for each finite-width
physical trajectory's residuals. No finite-width scalar clock is used.

The only sample-symmetry premise needed for the estimate is

    E_ell[(H^(ell)_1)^2]=E_ell[(H^(ell)_2)^2], ell=1,2. (8)

This is imposed along the path, not inferred here from uniqueness of a
yet unconstructed population solution.

## 3. Integrated curvature controlled by actual hidden gradient action

For each layer set U^(ell)=(H^(ell)_1+H^(ell)_2)/2 and
V^(ell)=(H^(ell)_1-H^(ell)_2)/2, and write
kappa_ell=E_ell[(V^(ell))^2]. Use delta^(ell)_+ and delta^(ell)_-
for the corresponding half-sum and half-difference of the reverse fields.
These modes stay in their original neuron populations. For ell=1,2,
relation (8) gives E_ell[U^(ell)V^(ell)]=0, while (1) gives
U^(ell)>=1 pointwise at every layer.
Unrolling the two sample terms of (6) gives exactly

    (W^(ell))'=delta^(ell)_- tensor U^(ell-1)
                +delta^(ell)_+ tensor V^(ell-1),
    ||(W^(ell))'||_HS^2
       =||delta^(ell)_-||_2^2 ||U^(ell-1)||_2^2
          +kappa_(ell-1)||delta^(ell)_+||_2^2.           (9)

The cross term is zero by (8), without independence of any fields.
Without (8) there is the additional term
2 E_ell[delta_- delta_+] E_(ell-1)[UV]; it must not be deleted for an
arbitrary finite realization.

Define the actual top curvature modes

    M^(3)_+=W^(4)[phi''(Z^(3)_1)+phi''(Z^(3)_2)]/2,
    M^(3)_-=W^(4)[phi''(Z^(3)_1)-phi''(Z^(3)_2)]/2.

The same readout multiplies the two sample gates. Therefore (3)--(4)
give pointwise, including either sign of W^(4),

    |M^(3)_-|<=|delta^(3)_-|,
    |M^(3)_+|<=|delta^(3)_+|.                            (10)

The sum bound uses positivity of both gates; the difference bound uses
the specific curvature-difference inequality (3). Combining (7), (9),
(10), and ||U^(2)||_2>=1 proves the actual-trajectory estimate

    integral_0^S [ ||M^(3)_-||_2^2
                   +kappa_2 ||M^(3)_+||_2^2 ] ds
      <= integral_0^S ||(W^(3))'||_HS^2 ds <=g(S)<=1.    (11)

This bound does not grow with S or deteriorate as rho tends to one.
It is a bound on specified curvature fields of the trajectory, not an
assumed tail envelope, response-kernel norm, or positivity of a Hessian.
It is also not a statement that kappa_2 has a uniform positive lower
bound. In particular, the second integrand retains its contrast weight.

The remaining middle product is explicit rather than discarded. Put
r_a=1-sigma(Z^(2)_a), and r_+=(r_1+r_2)/2,
r_-=(r_1-r_2)/2. Since phi''=(1-sigma)phi',

    [phi''(Z^(2)_1)q^(2)_1-phi''(Z^(2)_2)q^(2)_2]/2
       =r_+ delta^(2)_-+r_- delta^(2)_+,
    r_-= -5[phi'(Z^(2)_1)-phi'(Z^(2)_2)],
    |r_-|<=10|V^(2)|.                                  (12)

There is no same-readout factor at this layer, so (10) cannot be copied
to it. The exact remainder is r_- delta^(2)_+, and |r_-|<=1/2, so it
does belong to L2. Bounding it by 10|V^(2) delta^(2)_+| does not give
an action estimate: the L2 norm of this auxiliary product cannot be
inferred from the two separate second moments. No other rewriting of
the exact remainder is excluded by this observation.

Likewise (11) does not control curvature times a correlated historical
source sensitivity. Cauchy--Schwarz would require an additional moment
of that sensitivity, or an appropriate signed coupled energy. This is
the exact limit of the estimate, not a global continuation argument.

## 4. Nonlinearity and label modes at initialization only

The activation is strictly convex at every finite real argument, by (2).
It cannot agree almost surely with an affine function of a nondegenerate
Gaussian: its positive density and continuity would force equality at
every real point, contradicting its strictly positive second derivative.

For the centered first Gaussian pair with covariance C, the feature Gram is
positive definite for every rho in [-1,1). If |rho|<1, a zero linear
combination of its two features would vanish on R^2 by positive density
and continuity; varying each coordinate and using strict monotonicity
forces both coefficients to be zero. At rho=-1 the two features are
phi(G),phi(-G), with G standard centered Gaussian. Their sum is at least 2, and

    phi(G)-phi(-G)=G/10,

because log(1+exp G)-log(1+exp(-G))=G. The feature pair is exchangeable,
so its Gram eigenvalues are half the second moments of this sum and
difference, respectively, both positive. Both moments are finite by
linear growth. Thus a next centered Gaussian pair whose covariance is this
uncentered feature Gram is nonsingular. Repeating the same positive-
density argument at layers two and three gives positive-definite feature
Grams and nonaffine activation laws at all three initial populations.
In particular both label vectors have a strictly positive initial
readout kernel in this population initialization.

These are assertions about the specified recursive Gaussian initial
law. They are not a new joint empirical-average convergence theorem.
Nor is nonlinearity at later times or all-layer feature motion proved
by the strict convexity of the activation alone. Those full-task
obligations remain open for (1).

The design removes a precisely identified curvature-difference failure
of bounded monotone activations. It sacrifices their uniform feature
ceiling, and leaves the middle correlated product and the complete
historical response unresolved. None of these distinctions is a
counterexample to the desired two-sample theorem.
