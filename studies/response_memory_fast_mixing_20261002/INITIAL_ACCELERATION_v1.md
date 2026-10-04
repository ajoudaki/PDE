# Equal forward covariance, unequal initialized feature acceleration

Author derivation; separate internal audit pending. This is a local mechanism
result for the same two-layer q=1 tanh closure, with an explicitly introduced
initial mixer scale epsilon. It does not claim long-time fitting or explain
the magnitude of the epsilon=1 training experiment without further evidence.

## Actual initialized dynamics

Take one training input x with ||x||=sqrt(d), label y in {-1,1}, iid Gaussian
A0, w0=D0=0, H0=h0, tau0=1. All mobilities and raw moment equations are those
in TANH_TRANSFER.md. Write a=A0 x/sqrt(d), h=tanh(a), and W0=epsilon M, with
M independent of a. Thus a has independent N(0,1) coordinates. Define

    D_h = diag(1-h_i^2),       psi(z)=tanh(z) sech(z)^2.

At initialization dot A=0 and dot w=2y g. Since dot D=0 and D=0, the
reconstructed matrix has dot B=0. Differentiating the actual read-in velocity
once and then differentiating h gives the exact formula

    ddot h(0) = 4 epsilon D_h^2 M^T psi(epsilon M h).        (1)

The factors y cancel through y^2=1. The norm condition on x removes an extra
factor ||x||^2/d. Thus (1) is a response of an initialized trajectory, not an
arbitrarily specified internal credit signal. In particular

    lim_(t->0) ||h(t)-h(0)||^2/(n t^4) = ||ddot h(0)||^2/(4n)

for every fixed finite initialized system.

## Exact matrix-orientation identity

Let Z be standard normal, and define finite positive constants

    nu = E tanh(Z)^2,
    b  = E (1-tanh(Z)^2)^4,
    c  = E [(1-tanh(Z)^2)^4 tanh(Z)^2].

For S=M^T M, put mu4=tr(S^2)/n and beta=mean_i S_ii^2. Direct expansion,
using independent centered h_i, gives

    E ||D_h^2 S h||^2/n = beta c + (mu4-beta) nu b.          (2)

Indeed in row i the j=i squared term has expectation S_ii^2 c, each
j!=i squared term has expectation S_ij^2 nu b, and every cross term vanishes.
The coefficients distinguish the diagonal return to the same nonlinear neuron
from returns involving other neurons. The unweighted return energy is instead
E||S h||^2/n=mu4 nu and does not distinguish these orientations.

Choose positive singular values s with mean s_i^2=1 and mu4=mean s_i^4>1.
Let U be any fixed orthogonal matrix and V an orthogonal matrix with
|V_ij|=1/sqrt(n), such as normalized Hadamard with signs/permutations. Compare

    M_mix=U diag(s) V^T,       M_unmix=U diag(s).

Both have EXACTLY the same M M^T=U diag(s^2) U^T and singular values.
For any independent isotropic Gaussian input, their joint forward-vector law
and expected nonlinear transpose-return energy are identical. To see the
latter, its squared norm is psi(Mh)^T M M^T psi(Mh), determined in law by
that common covariance. No asymptotic argument is needed for this statement.

But beta_mix=1 whereas beta_unmix=mu4. Consequently (2) gives

    J_mix = c+(mu4-1)nu b,
    J_unmix = mu4 c,
    J_unmix-J_mix = (mu4-1)(c-nu b) < 0.                   (3)

Strictness follows because T=tanh(Z)^2 is nonconstant, and (1-T)^4 is strictly
decreasing on its support. For an independent copy T',

    c-nu b = 1/2 E[((1-T)^4-(1-T')^4)(T-T')] < 0.

The mixed matrix therefore produces greater initial first-layer feature
acceleration in this weak-second-layer limit, despite those identical forward
covariances and Gaussian-probe diagnostics. Greater motion alone is not a
claim of better task performance.

## Transfer to the actual tanh second layer

Define the exact initialized acceleration statistic

    J_epsilon(M)=E ||ddot h(0)||^2/(16 epsilon^4 n).

If ||M||<=C, with C independent of n, then

    J_epsilon(M) = beta c+(mu4-beta)nu b + O_C(epsilon^2),   (4)

uniformly in n and in the deterministic matrix M. The expectation is over A0;
the conclusion also holds conditionally on any independently sampled M with
that norm bound.

To prove (4), oddness and the bounded third derivative of psi give
|psi(u)-u|<=K|u|^3. For z=Mh let e=psi(epsilon z)/epsilon-z. Independent
centered bounded h_j are sub-Gaussian, so E|z_i|^6<=K_6 ||M_(i,:)||^6<=K_6 C^6.
Hence E||e||^2/n<=K' epsilon^4 C^6 and
E||D_h^2 M^T e||^2/n<=K' epsilon^4 C^8. Meanwhile
E||D_h^2 S h||^2/n<=C^4 nu. Expand the squared norm and apply Cauchy--Schwarz
to the cross term. This proves (4) for 0<epsilon<=1 with a finite constant
depending only on C.

For normalized quarter-circle quantiles, max s is eventually at most3 and
mu4 tends to2. Thus there exists epsilon0>0, independent of sufficiently
large n, such that for every fixed 0<epsilon<epsilon0 the exact initialized
tanh-q1 acceleration has the strict expected ordering in (3). This conclusion
requires neither an AMP theorem nor an exchange of width and time limits.

## Fixed numerical check, declared before running

One CPU float64 calculation will evaluate nu,b,c by Gauss--Hermite quadrature
at128 and256 nodes (agreement threshold1e-8). An illustrative paired Monte
Carlo check uses n=256,8192 Gaussian initial read-ins, seed20261002, U=V equal
to normalized Hadamard, and the normalized quarter-circle spectrum. Evaluate
the exact linear-return statistic and the exact (1) at epsilon in {0.1,0.3,1}.
Record means, paired standard errors and the analytic linear prediction;
do not select epsilon after seeing outcomes. The first two scales diagnose
the controlled limit; epsilon1 is descriptive only. No training/GPU and no
claim of a competitive architecture experiment. Reserve less than2 CPU minutes.
