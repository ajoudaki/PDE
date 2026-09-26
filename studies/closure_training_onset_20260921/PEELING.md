# p=1 kernel reduced to elementary Gaussian moments

## Target and result

The target is the canonical two-hidden-tanh population closure at fixed p=1,
with neural width already sent to infinity, w=G, c=0, M=D_1, and the maintained
ridge eta=1/4096. Inputs are u_theta=(cos theta,sin theta). The observable is
the initialized readout/tangent kernel K(theta,phi)=E_2[H_0(theta)H_0(phi)].
The limits below are evaluation-degree limits for this same kernel, not neural
width, closure-order, time, or training limits.

The completed calculation removes all nested random nonlinearities from its
terminal expectations. It combines the book's finite Gaussian source/Stein
contraction of the initialized matrix actions with convergent expansions of
the remaining tanh functions. Each finite stage is a finite sum of products
of Gaussian activation/derivative moments. The full answer is the uniform
limit of these stages with explicit geometric remainder bounds. An exact
finite terminating identity for the complete tanh kernel is not established.
Non-Gaussianity of intermediate observables is not an obstruction used here.

## Explicit primitives and lower recursion

Write sigma=tanh. For scalar G~N(0,1), and a Gaussian pair (X,Y) with covariance
[[1,rho],[rho,1]], define the terminal atoms

    mu_j(q) = E[sigma(sqrt(q)G)^j],
    d_j(q) = E[sigma^(j)(sqrt(q)G)],
    C_j(rho) = E[sigma(X)^j sigma(Y)].

All arguments in these expectations are Gaussian; powers mean finite products
of activations at the same Gaussian argument. Set v=mu_2(1), tau=mu_2(v),
alpha=1-tau. The exact lower recursion is

    beta = sum_{j>=0} alpha^j d_j(tau) mu_{j+1}(1) / j!,
    B(rho) = sum_{j>=0} alpha^j d_j(tau) C_j(rho) / j!,
    gamma = sum_{j>=0} alpha^j d_{j+1}(tau) mu_j(1) / j!,
    s = 1-gamma,    A(rho) = C_1(rho).

These sums follow by expanding sigma(z+alpha h) in its bounded shift h. They
are absolutely and uniformly convergent: for alpha<r<pi/2 the degree-N tail
of the first two sums is at most

    max(1,tan r) (alpha/r)^(N+1) / (1-alpha/r).

The corresponding gamma bound replaces max(1,tan r) by sec^2(r). The full
proof is in PEEL_ATOMS.md Section 1; PEEL_DIRECT.md independently derives
the same sums from the maintained matrix/source definitions. This is a
convergent expansion in a bounded response shift, not a formal time series.

Put Delta=(v+eta)(s+eta)-beta^2 and

    q_A = [alpha(v(s+eta)-beta^2)-beta tau gamma]/[(tau+eta)Delta],
    q_B = [alpha beta eta+tau gamma(v+eta)]/[(tau+eta)Delta],
    Lambda(rho) = q_A A(rho)+q_B B(rho).

These are the exact canonical normalization/source coefficients. In
particular the reverse-response term tau gamma is retained.

## Upper contraction and exact limit

Let a_theta=Lambda(cos theta), b_theta=Lambda(sin theta), and
H_i=sigma(sqrt(v)G_i), for independent standard Gaussians G_1,G_2. The two
upper nonlinearities can be contracted after a deterministic polynomial
approximation P_m on a bounded interval containing a_theta H_1+b_theta H_2.
An angle-independent bound is

    R = sqrt(2v kappa),
    kappa = q_A^2 v+2q_A q_B beta+q_B^2 s.

The proof uses independence of the two lower coordinate pairs and
Cauchy--Schwarz; it is not a sampled angular maximum. Section 4 of
PEEL_ATOMS.md gives explicit cosine-sum coefficients for a Chebyshev
interpolation polynomial P_m(x)=sum_{r=0}^m p_r x^r. Its uniform error is

    e_m = 4 tan(1) rho_R^(-m)/(rho_R-1),
    rho_R = (1+sqrt(1+R^2))/R.

For H=(H_1,H_2), form the polynomial

    P_m(a_theta H_1+b_theta H_2)
      = sum_{i+j<=m} c_{theta,i,j} H_1^i H_2^j,
    c_{theta,i,j} = p_{i+j} binomial(i+j,i) a_theta^i b_theta^j.

The upper Gaussian contraction is then the finite formula

    K_m(theta,phi) = sum_{i,j,k,l}
      c_{theta,i,j} c_{phi,k,l} mu_{i+k}(v) mu_{j+l}(v).

No activation of a nonlinear random argument remains in this expression.
For exact lower coefficients, |K-K_m|<=2e_m+e_m^2, uniformly on the circle.
The fully finite construction also truncates the lower recursion at N;
PEEL_ATOMS.md Sections 1-2 use the same truncated random polynomial for all
Gram entries, preserving positive definiteness after adding eta I. Its
explicit scalar error bound ell_N propagates through the ridge inverse, and

    |K-K_{N,m}| <= 4 ell_N+2e_{m,R_N}+e_{m,R_N}^2 -> 0.

Thus K=lim_{N,m->infinity} K_{N,m}, uniformly in both circle angles. The
activation-derivative atoms themselves have a finite polynomial recursion:
Q_0(t)=t, Q_{j+1}(t)=(1-t^2)Q_j'(t), and
sigma^(j)(x)=Q_j(sigma(x)). Every prescribed truncation therefore reduces
to one- and two-dimensional Gaussian activation-power moments.

## Deterministic validation and scope

The driver peel_check.py compares two computational routes on the fixed
angles 0, pi/12, pi/6, pi/4, pi/3, pi/2, 2pi/3, pi, 7pi/6:
direct nested Gaussian integration of the original closure, and the lower
derivative expansion followed by an upper polynomial Gaussian-moment
contraction. The latter uses Chebyshev polynomial coordinates for numerical
stability; these are finite linear combinations of activation-power atoms.
Cauchy's coefficient formula evaluates Gaussian activation derivatives.

Reproduction from the repository root (choose a fresh output directory):

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python studies/closure_training_onset_20260921/peel_check.py --output data/generated/closure_training_onset_20260921/peel_check_02 --nodes 128 192 --atomic

That recorded run uses NumPy 1.26.4, SciPy 1.13.0, Python 3.10.12, float64,
positive Gauss--Legendre integration on [-10,10], separately refined at 128
and 192 nodes per scalar Gaussian. Its result JSON retains all coefficients,
81-entry kernel tables, truncation comparisons, source hash and source copy.
At 192 nodes and lower/upper degree 64, the maximum difference between the
two routes is 9.99e-16. The original kernel changes by 1.08e-13 when the
quadrature changes from 128 to 192 nodes. At matched lower/upper degrees
8,16,32,48 the maximum differences are approximately 3.55e-3, 2.93e-6,
1.74e-10, 1.61e-15. These are deterministic floating-point checks, not
interval certificates for quadrature, roundoff, or derivative extraction.
The analytic remainder bounds concern exact moment evaluation.

The initialized constants are approximately v=.394294490398,
tau=.236450410499, beta=.233226326099, s=.270731066474. The global bound R
is approximately 2.52513328472. The actual preactivation coefficient sum at
theta=pi/4 is approximately 1.72230817771, exceeding pi/2; this is why the
upper proof uses a bounded-interval polynomial construction instead of an
unjustified tanh Taylor expansion at zero.

The direct-source and atom-expansion contributors wrote separate derivations
before reconciliation. A fresh internal check of the frozen mathematics and
an independent execution of the validation are required before labelling the
result internally checked. This result is not promoted to established docs.
