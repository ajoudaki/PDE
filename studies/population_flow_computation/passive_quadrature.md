# A computable error bound for passive one-dimensional Gaussian quadrature

Coordinator proof draft; only the finite numerical process is considered here.
No error relative to the target population trajectory is bounded by this note.

Let Q=sum_i v_i delta_{z_i} be any positive probability quadrature for a
standard Gaussian, with strictly increasing nodes. Write cumulative weights
a_i=sum_{j<i}v_j, b_i=a_i+v_i, and standard Gaussian density/distribution
phi_G,Phi. Put l_i=Phi^{-1}(a_i), r_i=Phi^{-1}(b_i), with infinite endpoints,
and d_i=min(r_i,max(l_i,z_i)). Then the exact one-dimensional Wasserstein
distance is

  W1(Q,N(0,1)) = sum_i [
    z_i (2 Phi(d_i)-a_i-b_i)
    +2 phi_G(d_i)-phi_G(l_i)-phi_G(r_i)].                  (1)

The endpoint density at either infinity is zero. Couple the quantile interval
(a_i,b_i) of the Gaussian to z_i. Its cost is the integral of |x-z_i| phi_G(x)
between l_i and r_i. Splitting at d_i, using phi_G'=-x phi_G, gives (1).
This increasing quantile coupling minimizes absolute transportation cost:
uncross two pairs x<=x', y<=y' using
|x-y|+|x'-y'|<=|x-y'|+|x'-y|; finite partitions followed by integrable-tail
truncation prove the same assertion for these one-dimensional laws.
An upper bound alone needs only the explicit coupling, not optimality.

For the saved numerical state, the clean passive conditional Gaussian field
has upper-representative centers m_i(u), common standard deviation sigma(u),
and saved readouts c_i. Lipschitz continuity of tanh gives

  |P^{-1} sum_i c_i E[tanh(m_i+sigma G)]
       -P^{-1} sum_i c_i sum_j v_j tanh(m_i+sigma z_j)|
    <= (P^{-1} sum_i |c_i|) sigma(u) W1(Q,N(0,1)).        (2)

This bound is uniform in the conditional centers and uses only saved finite
state and one-dimensional Gaussian functions. It does not involve any unseen
trajectory, high-dimensional integration, or independence of the c_i.
For the entire circle, sigma(u)<=||H_u||_emp<=1 follows from the positive
conditional covariance, so mean|c_i| times (1) is a uniform bound. A finite
set of directions may instead use their computed smaller sigma values.

For positive Gauss-Hermite rules Q_q matching Gaussian moments up to degree
2q-1, W1(Q_q,N(0,1)) tends to zero. Here is a contained justification of the
needed moment argument. The second moment equals one for q>=2, hence the
laws are tight by Markov. Every subsequential weak limit, obtained by a
diagonal subsequence of distribution functions at rational points, has all
Gaussian moments: the next available even moment bounds the omitted tails
of each lower moment uniformly. Its even moments imply exponential
integrability, since monotone expansion of cosh(tX) gives exp(t^2/2).
The absolutely convergent exponential series consequently identifies its
characteristic function as exp(-t^2/2), so it is the Gaussian law. Uniqueness
of a law with that characteristic function follows, for example, by convolving
the finite measure difference with Gaussian densities and using their Fourier
inversion, then the Gaussian approximate identity. Thus all subsequences have
the Gaussian limit. On a bounded interval their distribution functions converge
almost everywhere; dominated convergence controls the integral difference.
Outside [-R,R], each absolute first-moment tail is at most 1/R by the second
moment. Sending R to infinity proves W1 convergence.

Therefore one can search q until the explicitly computable bound in (2)
meets any positive requested quadrature tolerance. Order q, the P*q*m_query
activation evaluations, node construction and node/weight precision must all
be counted. This addresses only passive conditional integration. Training
source sampling, response estimation, time, law and precision errors remain
separate. Comparing orders 16 and 32 is not itself this bound.

Formula (1) admits certified evaluation using interval approximations of the
Gaussian functions and quadrature nodes/weights, with scalar tail bounds.
The current implementation uses floating-point SciPy quadrature values and
does not include that interval calculation. Accordingly numerical evaluations
of (1) below are estimates of an exact-arithmetic bound, not end-to-end
certificates for the executed floating-point solver.

## Sharper small-variance component and its projection hypothesis

analytic_passive_quadrature.md gives a separate complete derivative/remainder
proof for tanh. The coordinator checked that proof and its source geometry.
At a fixed exact empirical history, put the training source vectors in
R^(P+J) as v_j=(H_j/sqrt(P),s e_j), and put a clean query vector there as
v_u=(h_u/sqrt(P),0). Their training Gram is C=H^T H/P+s^2 I, which is
positive definite. Orthogonal projection Pi onto the span of the v_j has
residual squared norm

    ||(I-Pi)v_u||^2 = ||h_u||_emp^2 - cross^T C^(-1) cross.

Indeed the least-squares coefficients solve C a=cross, and expansion of
||v_u-sum_j a_j v_j||^2 gives the identity. Pi is fixed while u varies.
Consequently the projection assumption and circle-grid Lipschitz estimate in
that note hold for this exact finite source process. No action norm between
unlike population spaces is asserted. An approximate stored Cholesky factor
still requires a numerical residual allowance before the same inequality
becomes a machine-verified certificate.

The new estimate is Cbar q! max(1,tan r) (sigma/r)^(2q), for 0<r<pi/2,
where Cbar=mean|c|. It can be very small at useful fixed orders when the
conditional variance is small. It need not improve as q tends to infinity;
the transport bound above supplies the no-floor quadrature refinement.
