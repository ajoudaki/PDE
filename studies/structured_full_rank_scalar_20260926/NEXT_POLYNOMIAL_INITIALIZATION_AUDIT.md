# Internal audit of polynomial deterministic initialization

2026-09-27. Read the complete `NEXT_POLYNOMIAL_INITIALIZATION.md` and the
complete revised polynomial-state construction. No numerical experiment
or training was run. This is a scoped same-study crosscheck, not promotion
review.

**Verdict:** no material mathematical gap found. At fixed structural
parameters and with polynomially computable input data, the proposed
initializer has polynomial work and bit precision in D and achieves
absolute error exp(-D) for every required initial moment. The polynomial
has the curse of seed dimension. No numerical ODE integration-work
conclusion follows from this initializer.

The following points were checked directly.

1. **The nonsmooth radial projection is removed exactly.** Splitting the
   Gaussian radial integral into q<=R and q>R leaves one analytic bounded
   interval integral and a boundary-sphere integral multiplied by the
   radial tail probability. The Gaussian mark tail is retained. The
   spherical Jacobian contains integer powers of sine, so coordinate
   poles introduce no analytic denominator. For k=1 the two-sign sum
   correctly replaces spherical coordinates.

2. **The first-weight truncation is uniformly controlled.** There are 2k
   standard Gaussian coordinates. With
   W^2=2[D+log(16k)], the stated elementary union bound is exp(-D)/4.
   Every real initial monomial has magnitude at most one, so this bounds
   the error simultaneously for every retained moment without a factor
   equal to their number.

3. **The complex neighborhood remains large enough.** After rescaling
   all integration variables, the first preactivation imaginary parts
   are O(W delta) and the second ones are O_k(R(1+W)delta).
   Choosing delta=c_k/[(1+W)(1+R)] with a sufficiently small explicit
   c_k keeps both tanh arguments strictly within their pole-free strips.
   The identity for |tanh(x+iy)| at |y|<=pi/4 gives a bound of one.
   The normalized mark coordinates are at most two after reducing c_k;
   hence the monomial norm is at most 2^D. Gaussian densities add
   exp(O_k(W^2 delta^2+R^2 delta^2)), which is bounded, and Jacobians
   add only polynomial factors. Thus log of the weighted complex norm
   is O_k(D), uniformly for R<=sqrt(log D).

4. **The quadrature error estimate does not rely on an unstated
   interpolation theorem.** The Chebyshev-Lobatto coefficient bound
   |a_l|<=2 max|F(t_j)| is valid. Also
   integral T_(2j)=-2/(4j^2-1) for j>=1, and its absolute tail telescopes
   to one; including the constant term gives total three. Therefore the
   quadrature operator norm is at most six. The tensor Chebyshev tail
   bound follows by geometric summation of Cauchy coefficient bounds.
   Polynomial exactness and the norm bound then give the stated tensor
   integration error. Taking p=O_k(D^(3/2)sqrt(log D)) makes that error
   exp(-D)/16 with a sufficiently large computable constant.

5. **Tail weights and precision do not hide an oracle.** For fixed
   integer r=k^2, integration by parts reduces the radial tail to
   elementary terms and, when needed, erfc at O_k(sqrt(log D)). Its
   supplied finite-integral Taylor construction uses polynomially many
   terms and O_k(D) bits. Real quadrature integrands and their first
   derivatives have polynomial bounds. Polynomially many evaluations,
   O(D+log D) working bits, and the bounded quadrature weight norm
   therefore suffice for the allocated absolute-error budgets. The
   note explicitly requires polynomially computable supplied data.

There are s=k^2+2k integration variables in the inner term, so the node
count is O_k(D^(3s/2)(log D)^(s/2)). Multiplying by the polynomial number
of retained moments, cutoffs and passive queries preserves polynomial
work at fixed k,m,H. This is a formal complexity guarantee; its exponent
can be prohibitive. Quadrature nodes are discarded after initialization,
so none becomes an evolving particle, density grid or initial-label field.
