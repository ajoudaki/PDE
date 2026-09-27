# Polynomial deterministic initialization by polar splitting and analytic quadrature

2026-09-27. Scoped theoretical addendum to `NEXT_POLYNOMIAL_ROUTE.md`.
Inputs: its initial monomial family and cutoff schedule, the normalized
gate lift in `NEXT_GAUSSIAN_ROUTE.md`, and the supervisor's proposed polar
integration construction. No numerical experiment or training was run.
This is an internal derivation, not a promotion review.

**Result.** At fixed block size k and fixed training/memory parameters, all
initial aggregate moments required by the polynomial-state construction
can be computed deterministically to absolute error exp(-D) with polynomial
arithmetic work and polynomial bit precision in D. The polynomial exponent
depends on the seed dimension k^2+2k and is large. This removes the former
exponential-in-D Lipschitz-grid initialization bound; it does not establish
polynomial numerical ODE integration time or practical complexity.

The key is to split the Gaussian radial integral at each mark cutoff before
using analytic quadrature. The radial projection is not analytic across
its cutoff surface. No analyticity of that unsplit map is assumed.

## 1. Initial integrands and the exact polar split

Let r=k^2 and s=r+2k. Flatten G into r independent Gaussian coordinates of
variance 1/k. Write G=q S, where q=||G||F, and S is an independent uniform
direction on the unit sphere in R^r, reshaped as a k-by-k matrix. The radial
density is

    p_r(q)=2(k/2)^(r/2)/Gamma(r/2)
                      q^(r-1) exp(-kq^2/2),    q>=0.         (1)

For cutoff R>=1, G^[R]=min(q,R)S. The initial nonzero local coordinates
used by the monomial family are

    G^[R]/R,
    x_a=tanh(w_0 v_a),
    h_a=tanh(G^[R] x_a),
    beta_(0,b)=x_b.

Every coordinate zeta, alpha, or beta_j with j>0 is initially zero. A
monomial containing one of those factors is therefore initialized exactly
to zero. Other initial monomials are products of degree at most D of the
displayed factors, with training inputs and at most one passive query.
Their real values have magnitude at most one, uniformly over all unit
inputs and all seeds. Repeated label indices pose no issue: these are
ordinary labeled-coordinate monomials in the current block state.

Denote one such integrand by P_R(w,q,S), with the notation already including
radial clipping. Independence of w, q and S gives the exact identity

    E P_R
     = integral_w integral_S integral_0^R
             P(w,qS) p_r(q) dq dnu(S) dgamma(w)
       +p_tail(R) integral_w integral_S
             P(w,RS) dnu(S) dgamma(w),                       (2)

where the normalized mark inside P is qS/R or S respectively and
p_tail(R)=integral_R^infinity p_r(q)dq. The second integrand is independent
of the original radius q. This removes the projection kink exactly.

For r>=2, use the usual global spherical parametrization

    phi_1,...,phi_(r-2) in [0,pi],
    phi_(r-1) in [0,2pi],

with components cos(phi_1), sin(phi_1)cos(phi_2), and so on, ending in
products of sines times the last cosine and sine. Its surface Jacobian is

    J(phi)=product_(j=1)^(r-2) sin(phi_j)^(r-1-j).             (3)

All exponents are nonnegative integers. Hence the parametrization and
Jacobian are entire functions of the angles. The coordinate singularities
at the poles do not introduce denominators or nonanalytic factors in the
integral. On real angles J is nonnegative and the parametrization covers
the sphere with the usual measure-zero endpoint identifications. Divide
by its known surface area to obtain dnu.

For k=1, r=1 and the sphere is the two-point set S=+1,-1 with weights 1/2.
Use that finite sum, and the half-normal density (1), with no angular
coordinates. This case does not require a nonexistent spherical chart.

## 2. Truncating only the first-weight tail

There are 2k independent standard Gaussian entries of w. Set

    W_D=sqrt(2[D+log(16k)]).

The elementary Gaussian tail estimate P(|Z|>W)<=2 exp(-W^2/2), followed
by a union bound, gives

    P(max |w_iell|>W_D)<=exp(-D)/4.                          (4)

Since the initial monomial integrands have magnitude at most one, omitting
this part of the w integral changes every required moment by at most the
same bound. The Gaussian mark tail is not omitted: it remains the exact
second term of (2). Set the degree-zero moment to one exactly.

Rescale every remaining integration coordinate affinely to [-1,1]: the
2k first weights have scale W=W_D, q in [0,R] has scale R/2, and each angle
has scale at most pi. The inner term has s=r+2k scalar variables. The outer
term has s-1 variables, or 2k variables and a two-sign sum when k=1.

## 3. A polynomially small complex neighborhood

There is a computable c_k>0 such that both integrands, including their
Gaussian densities, radial density, and angular Jacobian, are holomorphic
on the product Bernstein ellipses of parameter rho=exp(delta/2), where

    delta=c_k/[(1+W)(1+R)] <=1/4.                            (5)

Here a Bernstein ellipse is the image of |z|=rho under
t=(z+z^(-1))/2. Its imaginary extent is at most delta and its real extent
is within O(delta^2) of [-1,1]. The following estimates verify (5), rather
than assuming that composition of analytic functions gives a uniform strip.

For each complex first-weight entry, its imaginary part is at most W delta.
For any real unit query v, the imaginary part of (wv)_i is at most a fixed
constant times W delta. On |Im z|<=pi/4,

    |tanh z|^2
       =[sinh^2(Re z)+sin^2(Im z)]
         /[sinh^2(Re z)+cos^2(Im z)] <=1,
    |sech^2 z|<=2.                                          (6)

Choose c_k small enough that every first preactivation stays in a narrower
strip, for instance |Im z|<=pi/8. In particular x is bounded by one there
and differs from the corresponding real gate by at most C_k W delta.

The complex spherical direction differs from its value at the real angles
by at most C_k delta in Frobenius norm. The affine complex q differs from
its real part by at most R delta/2 and has magnitude at most 2R. Therefore,
relative to the real matrix G_0=(Re q) S(Re phi),

    ||q S-G_0||F<=C_k R delta,
    ||G_0||F<=2R.

For the outer integral replace q by the real constant R. Comparing the
complex second preactivation Gx with the real one G_0 x_0 gives

    ||Gx-G_0 x_0||_infinity<=C_k R(1+W)delta.                 (7)

After reducing c_k again, every second preactivation also stays in
|Im z|<=pi/8. Thus tanh has no pole in the specified neighborhood, and
both first and second gates have magnitude at most one. Normalized mark
components G/R have magnitude at most two. Every degree-D initial
monomial consequently has magnitude at most 2^D.

The weighted integrands also have controlled norm. The complex Gaussian
factor from w is bounded by exp(C_k W^2 delta^2), since the negative square
of the real part only decreases its magnitude. Its affine Jacobian adds
W^(2k). The radial density adds at most C_k R^r exp(C_k R^2 delta^2).
The spherical sine/cosine factors and (3) have bounded magnitude depending
only on k for delta<=1/4. Thus one common sufficient bound is

    M_(D,R)<=C_k(1+W)^(2k)(1+R)^r 2^D.                     (8)

The same bound covers the outer integral. It includes all normalization
constants and affine Jacobians. Its logarithm is O_k(D) for
1<=R<=sqrt(log D), as in the parallel-cutoff construction. In particular
there is no exp(D^2) density factor hidden by the rescaling.

## 4. Elementary analytic quadrature with computable nodes and weights

The following explicit quadrature avoids requiring a separate complexity
theorem for Gauss-Legendre nodes and weights. It is enough that a quadrature
rule is polynomial-exact and has bounded absolute weight sum; positivity is
not necessary.

For one variable, use the p+1 Chebyshev-Lobatto nodes
t_j=cos(j pi/p), 0<=j<=p. Interpolate the sampled values by a polynomial
I_p F=sum_(ell=0)^p a_ell T_ell. Finite cosine orthogonality gives the
discrete cosine formulas for a_ell and the bound

    |a_ell|<=2 max_j |F(t_j)|.                               (9)

Indeed the formula is a weighted cosine sum divided by p, with half
weights at the two endpoints and total absolute sampling weight at most
two. Define Q_p F as the exact integral of that interpolation polynomial.
The elementary substitution t=cos(theta) gives

    integral_(-1)^1 T_ell(t)dt
       =0 for odd ell,
       =2/(1-ell^2) for even ell.                           (10)

The sum of absolute values in (10), over all ell>=0, is three: its positive
ell=0 contribution is two and the even tail telescopes to one. Hence
||Q_p||<=6 as an operator on bounded nodal data. Equivalently, its absolute
weight sum is at most six. The rule is exact on all polynomials of degree
at most p. Its nodes and weights are given by explicit cosine sums and
rational numbers, without root finding.

For a function F holomorphic and bounded by M on a product of s ellipses
with rho=exp(delta/2), Cauchy's coefficient formula applied to
t_i=(z_i+z_i^(-1))/2 bounds the tensor Chebyshev coefficient of index n by

    |a_n|<=2^s M rho^(-|n|_1).

Truncate every coordinate's degree at p. Since |T_n|<=1 on [-1,1], summing
the geometric coefficient tails gives a polynomial P_p with

    ||F-P_p||_infinity
        <=C_s M delta^(-s) exp[-(p+1)delta/2].                (11)

For clarity, the omitted indices have at least one n_i>p. Sum that
coordinate's geometric tail and all other coordinates' full geometric
series, then use 1-rho^(-1)>=c delta. This proves (11) without an
unverified interpolation-rate theorem.

Use the tensor product of Q_p. It is exact on P_p and has norm at most
6^s; the exact integral has norm 2^s. Consequently

    |integral F-Q_p^(tensor s)F|
      <=(2^s+6^s) C_s M delta^(-s)
                                       exp[-(p+1)delta/2].   (12)

Substitute (5) and (8). A sufficiently large computable fixed constant
C_k gives simultaneous error at most exp(-D)/16 for all relevant initial
monomials with the single choice

    p_D=ceil(C_k D(1+W_D)(1+sqrt(log D)))
                   =O_k(D^(3/2)sqrt(log D)),    D>=9.         (13)

Here the terms log M, s log(1/delta), and fixed normalization constants
are included when choosing C_k. The same p_D works for every cutoff
R_j=sqrt(j), j<=floor(log D), and every passive query on the unit circle.
Uniformity follows from the degree and unit-input bounds, not from a
union-bound probability argument. The deterministic quadrature error is
an absolute simultaneous bound.

The number of quadrature nodes per inner integral is at most

    (p_D+1)^s
       =O_k(D^(3s/2)(log D)^(s/2)).                          (14)

The outer integral requires no more nodes. Sphere endpoint degeneracies
do not affect the estimate; all corresponding Jacobians are analytic.

## 5. Radial tail weights, finite precision, and arithmetic cost

The radial tail factor in (2) is computable to exp(-D)/16 with polynomial
work and precision. Let z=sqrt(k/2) R. Integration by parts expresses the
tail of q^(r-1)exp(-kq^2/2) in terms of exp(-z^2) times a fixed polynomial
when r is even, or erfc(z) plus such terms when r is odd. Here r is fixed
and z=O_k(sqrt(log D)). To avoid assuming a special-function oracle,

    erfc(z)=1-(2/sqrt(pi)) integral_0^z exp(-t^2)dt.

The exponential Taylor series integrated termwise approximates this
finite integral with polynomially many terms at precision O(D) bits. For
example, taking a Taylor degree larger than a fixed multiple of
D+z^2 and using n!>=(n/e)^n makes the remainder smaller than exp(-D)
after fixed-factor adjustments. Intermediate cancellation costs at most
O(z^2+D)=O_k(D) guard bits. The half-integer/integer Gamma and sphere
normalization constants reduce to factorials and pi at fixed r.

All actual quadrature evaluation is at real nodes. At those nodes,
the local gate and normalized mark factors have magnitude at most one.
Their first derivatives with respect to the rescaled coordinates are
bounded by a polynomial in W and R. Differentiating a degree-D product
therefore costs a factor at most D times that polynomial. The Gaussian
density and angular Jacobian derivatives also have polynomial bounds in
W,R for fixed k. Thus the real weighted integrands and their first
derivatives have polynomial-in-D bounds. This allows node, weight, and
elementary-factor errors to be made collectively <=exp(-D)/16 using
O_k(D+log D) working bits, with a fixed extra factor if needed for guards.

The quadrature's absolute weight sum is <=6^s. The number of nodes is
polynomial in D, so accumulation and finite weight errors need only
O(log D) additional guard bits at fixed dimension. Products of at most D
bounded factors amplify elementary evaluation errors by at most a
polynomial factor if those errors are chosen <=exp(-D)/poly(D).
Elementary sin, cos, exp, square root and tanh evaluations to this precision
have polynomial algorithms directly from Taylor series, range reduction,
and arithmetic; their arguments here have polynomial magnitude. Constants
such as pi can likewise be computed, for example from convergent rational
arctangent series. This does not depend on exact real-number oracles.
As usual for a bit-cost statement, the supplied training inputs must be
finite data or computable to the requested precision in polynomial work;
arbitrary noncomputable real inputs cannot support any such statement.

Allocate exp(-D)/4 to the omitted first-weight tail, exp(-D)/16 to each
quadrature contribution and radial tail weight, and the remaining budget
to arithmetic errors. The total initialization error is then <=exp(-D)
in every retained coordinate. Clip the final computed moments to [-1,1]
if desired; projection cannot increase their error relative to exact
moments in that interval. Initialize all cutoff clocks and the constant
moment exactly.

For a conservative work bound, let d be the local monomial dimension and
N_D=O_d(D^(d+1)log D) the whole-circle, parallel-cutoff scalar count in
`NEXT_POLYNOMIAL_ROUTE.md`. Evaluating each required monomial at every
node by at most O_d(D) scalar operations gives the bound

    O_(k,m,H)(N_D D (p_D+1)^s)

elementary evaluations/arithmetic operations, plus polynomial rule-generation
work. This is polynomial in D at fixed structural parameters. Computing
powers and common gates once per node can reduce that bound, but is not
needed for the theorem. The required O(D) bit precision leaves total
bit work polynomial under the ordinary integer-arithmetic model as well.

The cubature nodes and seed arrays are temporary initialization data. Only
their accumulated scalar moments remain. No initial-label dictionary,
particle trajectory, density representation, or quadrature law evolves.

## 6. What this establishes and what it does not

This addendum supersedes the exponential-work Lipschitz-quadrature bound as
the best available initialization certificate for the specific bounded
monomial family and parallel radial cutoffs. Together with its algebraic
error-versus-D theorem, it gives polynomial inverse-accuracy initialization
work for each fixed k,m,H,T. The exponent includes the curse of seed and
local dimensions, and its constants and accuracy exponent may be enormous.
It is not a practical complexity guarantee for the tested small models.

It does not prove polynomial work to integrate the scalar ODE through a
given horizon at its certified output accuracy. Clipping introduces
nonsmooth switching surfaces, degree produces stiffness, and coarse
full-state error propagation bounds can be much worse than the exact
hierarchy's low-observable convergence estimate. A numerical integration
error theorem remains a distinct obligation. Equation generation and
per-RHS work can be counted separately from the number of solver steps.

The result applies to any subset of these degree-D monomials, in particular
an observable-reachable selection which expands all dependencies. It does
not give the inexpensive nonexhaustive output-only selection the missing
feedback-convergence property.
