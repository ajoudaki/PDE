# Positive bounded operators do not imply uniform integrability of the gated backward field

This is a deterministic counterexample to a proposed general localization lemma. It is not a trajectory of the canonical Gaussian network and does not refute a network-specific localization theorem.

Let a probability space contain a set E of measure epsilon in (0,1/2], and put

    u = 1_E / sqrt(epsilon),
    v = 1_(E^c) / sqrt(1-epsilon).

These vectors are orthonormal in normalized L2. In the finite-width setting, take the uniform probability space on n >= 2 points and E a single point, so epsilon = 1/n.

Define a time-independent self-adjoint operator A by

    A u = 2u - 2v,
    A v = -2u + 3v,

and let A be the identity on the orthogonal complement of span{u,v}. Its two nontrivial eigenvalues are

    lambda_- = (5-sqrt(17))/2 > 0,
    lambda_+ = (5+sqrt(17))/2.

Consequently lambda_- I <= A <= lambda_+ I uniformly in epsilon. In particular A(u+v)=v.

For t in a fixed interval [0,S], set

    delta(t) = t(u+v),
    z(t) = (t^2/2)v,
    D(z) = 1/(1+z^2),
    q(t) = (1+z(t)^2) delta(t).

All products and the definition of D are pointwise. Since u and v have disjoint support,

    q(t) = t u + [t + t^5/(4(1-epsilon))]v,
    q'(t) = u + [1 + 5t^4/(4(1-epsilon))]v.

Thus delta = D(z)q and the required equation holds exactly:

    z'(t) = t v = A delta(t) = A D(z(t))q(t).

Both z(0) and q(0) are zero; all trajectories are smooth. The feature h=arctan(z) is bounded pointwise by pi/2.

## Uniform bounds

For epsilon <= 1/2 and t <= S,

    ||z(t)||_2 = t^2/2 <= S^2/2,
    ||q(t)||_2^2 <= S^2 + (S+S^5/2)^2,
    ||q'(t)||_2^2 <= 1 + (1+5S^4/2)^2,
    ||delta(t)||_2^2 = 2t^2,
    integral_0^S ||delta(t)||_2^2 dt = 2S^3/3.

The associated positive quadratic action also stays bounded:

    <delta(t), A delta(t)> = t^2,
    integral_0^S <delta(t), A delta(t)> dt = S^3/3.

Every bound is independent of width. The same is true of the operator A and all its time derivatives, since A is constant.

## Failure of uniform integrability

For each fixed t > 0,

    integral_E |delta(t)|^2 = t^2,

although measure(E)=epsilon tends to zero. Therefore the squared gated fields are not uniformly integrable at any positive fixed time. They are not uniformly integrable in space-time either, because

    measure([0,S] x E) = S epsilon -> 0,
    integral_0^S integral_E |delta(t)|^2 dt = S^3/3 > 0.

On E the cancellation is exact: (A delta)|_E=0, hence z|_E=0 and D(z)|_E=1. Positivity controls the total pairing <delta,A delta>, not its restriction to E. The off-diagonal contribution cancels the positive rare-coordinate contribution and transfers motion to the bulk.

## Instantaneous algebraic factorization

Even the algebraic form A = m_1 I + W D_1^2 W* does not by itself rule this out. On a copy of the same finite-dimensional probability space choose

    z_1 = tan(1/2) pointwise,
    h_1 = arctan(z_1) = 1/2,
    m_1 = ||h_1||_2^2 = 1/4,
    D_1 = cos(1/2)^2 I,
    W = cos(1/2)^(-2) (A - I/4)^(1/2).

The positive square root exists because lambda_- > 1/4, and direct multiplication gives

    W D_1^2 W* = A - I/4.

Moreover ||W||_op = sqrt(lambda_+ - 1/4)/cos(1/2)^2 is width-independent. This factorization respects the arctan relation between h_1 and D_1, but it does NOT enforce z=W h_1, a Gaussian law for W, learned-weight flow equations, or the coupled evolution of z_1. It is an algebraic observation only.

If a zero initial derivative q'(0) is also desired, replace t in delta by t^2 and replace t^2/2 in z by t^3/3. The same argument and uniform bounds on every fixed interval hold, and both q(0) and q'(0) then vanish.

Conclusion: uniform operator positivity, bounded normalized-L2 q and q', bounded normalized-L2 z, zero initial q, and bounded total action do not imply uniform integrability of |D(z)q|^2. Additional structure from canonical Gaussian initialization and the exact coupled dynamics is essential.
