# Single-row cavity route for the fixed practical depth-two model

2026-09-08. This is a theoretical route note under ../CONTRACT.md. The activation is exactly

    phi(z) = (3/4)(1+z) + (1/4)tanh(z).

The model, independent Gaussian initialization, actual small random readout, and raw metric are those of the contract. No experiment was performed. This note establishes finite-array comparison and initialization identities. It does **not** establish the global canonical population flow or the uncapped finite-width limit.

The new useful conclusions are: a one-row cavity forcing has a dimension-independent Gaussian moment bound; its bulk influence is small under a one-reference incoming-field bound; and its return through the same row is order one already at the second derivative. A further finite-array construction shows why energy-ball bounds and exchangeability cannot supply the missing incoming-field tail estimate by themselves.

## 1. Coordinates and energy bounds

Write w=sqrt(d)W, u_i=x_i/sqrt(d), and use the normalized row norm for w and vectors. The raw distance between two states is

    D(Theta,Theta_tilde)^2
      = ||w-w_tilde||_n^2 + ||A-A_tilde||_F^2
        + ||C-C_tilde||_n^2.

The first norm includes the Euclidean norm of each d-dimensional row. The initialized A is not declared small in Frobenius norm. Its operator norm and the Frobenius norm of its learned increment are the quantities used below.

The exact finite true-GF identity gives

    E(t) + integral_0^t ||Theta_dot(s)||raw^2 ds = E(0),
    D(Theta(t),Theta(0)) <= sqrt(t E(0)).                 (1.1)

Consequently, on initial events bounding E(0), ||w(0)||_n, ||A(0)||op and ||C(0)||_n, all primal norms are bounded on [0,T] by a constant depending on T and those initial bounds, independently of n. Such initial events have probability tending to one when the bounds are sufficiently large. The fixed d is allowed in these bounds.

Since |phi(z)|<=1+|z|, |phi'|<=1 and |phi''|<=1/2, these primal bounds imply dimension-independent normalized L2 bounds for every z_i,h_i,v_i,k_i,b_i,q_i,d_i and for the residual. They do not imply uniformly integrable squared coordinate tails for q_i.

## 2. An exact one-reference stability estimate

Consider two finite states with their primal norms bounded by M>=1. Suppose only the reference state additionally obeys

    ||C_tilde||infinity <= R,
    max_i ||q_i,tilde||infinity <= R.                    (2.1)

Here q_i,tilde denotes the reference incoming field. Then the full raw GF vector field G satisfies

    ||G(Theta)-G(Theta_tilde)||raw
       <= K_M(1+R) D(Theta,Theta_tilde),                 (2.2)

where K_M is a finite polynomial bound depending only on M and the fixed number of samples, not on n. No incoming maximum is assumed for the first state.

Proof. Forward differences obey

    ||Delta z_i||_n <= ||Delta w||_n,
    ||Delta h_i||_n <= ||Delta z_i||_n,
    ||Delta v_i||_n
       <= ||A||op ||Delta h_i||_n
          + ||Delta A||_F ||h_i,tilde||_n,
    ||Delta k_i||_n <= ||Delta v_i||_n.

The scalar residual differences have the same bound with a constant polynomial in M. Group the backward differences asymmetrically:

    Delta b_i = phi'(v_i) Delta C
                   + [phi'(v_i)-phi'(v_i,tilde)] C_tilde,
    Delta q_i = A^T Delta b_i + (Delta A)^T b_i,tilde,
    Delta d_i = phi'(z_i) Delta q_i
                   + [phi'(z_i)-phi'(z_i,tilde)] q_i,tilde.

Thus

    ||Delta b_i||_n <= ||Delta C||_n+(R/2)||Delta v_i||_n,
    ||Delta q_i||_n <= M||Delta b_i||_n
                          + ||Delta A||_F ||b_i,tilde||_n,
    ||Delta d_i||_n <= ||Delta q_i||_n+(R/2)||Delta z_i||_n.

Insert these inequalities into the three exact update formulas. For the middle block use

    ||a b^T/n||_F = ||a||_n ||b||_n.

All remaining factors are primal L2 bounds or residual bounds depending only on M. This proves (2.2). In particular, no product of two incoming maxima, and no factor growing with width, is introduced.

## 3. The cavity is a forced copy of the same physical GF

Fix a top-layer row j and write a_j for row j of A(0). Define the cavity by imposing C_j^-(t)=0 for all t, keeping all other initial coordinates unchanged, and following the constrained true gradient flow of the same squared loss. The row A_j^-(t)=a_j is then constant because b_{ij}^-=0. All lower fields h_i^-(t), all active upper fields, and the residual r^-(t) are independent of a_j and of the deleted initial readout coordinate C_j(0).

This is an auxiliary comparison, not a replacement of the target algorithm. The actual target still starts from its specified nonzero random C_j(0).

Embedded into the unconstrained raw parameter space, the cavity path satisfies the exact identity

    Theta_dot^-(t) = G(Theta^-(t)) + e_j^C s_j^-(t),
    s_j^-(t) = sum_i r_i^-(t) phi(a_j h_i^-(t)),          (3.1)

where e_j^C is a unit coordinate vector in the readout block. Its raw norm is n^(-1/2). At a state with C_j=0, the only removed component of the full gradient is the readout update at j: the W update and the middle-matrix update already have zero contribution from that row.

Both the constrained cavity and the full flow have the exact energy identity in their respective subspaces. Bound their primal norms by M on an interval and stop additionally when the reference cavity violates (2.1). From (2.2), (3.1), and the integral Gronwall inequality,

    sup_(s<=t) D(Theta(s),Theta^-(s))
      <= exp[K_M(1+R)t]/sqrt(n)
           [ |C_j(0)| + integral_0^t |s_j^-(s)| ds ].     (3.2)

This retains the actual initial readout mismatch. Since C_j(0) has standard deviation n^(-1), that initial term has raw size n^(-3/2).

### Gaussian bound on the forcing

The active cavity path, and any stop defined using only its active primal fields, residual, C^- and q_i^-, are independent of a_j. Conditional on all the other initial data, a_j h_i^-(s) is a centered Gaussian with variance ||h_i^-(s)||_n^2. Hence, on an active-primal stop ensuring ||r^-||_2<=M and max_i||h_i^-||_n<=H,

    || integral_0^(T wedge stop) |s_j^-(s)| ds ||_(Lp | other data)
        <= sqrt(3) M T [1+H ||G_standard||_p]
        <= c M T(1+H) sqrt(p),   p>=2.                 (3.3)

The first bound is Minkowski's inequality and the pointwise Gaussian moment bound; it does not require independence between different times. An active stop is important: a stop involving the inactive field a_j h_i^- would depend on the deleted row.

Equations (3.2)--(3.3) give a genuine small bulk-influence estimate when R=o(log n), on the corresponding stopped interval. They do not show that the actual uncapped trajectory reaches no such stopping time.

## 4. The self-return is order one and cannot be discarded

The normalized bulk distance in (3.2) does not justify treating the tagged field as an independent Gaussian. Indeed

    |a_j (h_i-h_i^-)|
       <= ||a_j||_2 sqrt(n) ||h_i-h_i^-||_n,             (4.1)

which is only order one at the cavity scale. The following exact acceleration identity shows this is a real effect.

First compute at the explicitly named zero-readout initial state C(0)=0. This is an initialization diagnostic; the actual small-readout correction is handled below. Put

    s_j = sum_a y_a phi(v_aj(0)).

Both full and cavity W and A first derivatives vanish at zero. Their readout derivatives agree except that the cavity has zero derivative at j. Therefore, with all fields on the right evaluated at initialization,

    h_i''(0)-h_i^-''(0)
      = sum_a y_a Gamma_ia phi'(z_i) phi'(z_a)
                   a_j^T phi'(v_aj) s_j.              (4.2)

Coordinate products are taken in the lower layer. Applying the same row gives

    a_j [h_i''(0)-h_i^-''(0)]
      = sum_a y_a Gamma_ia phi'(v_aj) s_j
           sum_k a_jk^2 phi'(z_ik)phi'(z_ak).           (4.3)

Conditional on the first-layer roots, the final quadratic sum has mean

    (1/n) sum_k phi'(z_ik)phi'(z_ak)

and variance at most 2/n. The law of large numbers for the first-layer roots therefore gives

    sum_k a_jk^2 phi'(z_ik)phi'(z_ak)
         -> m_ia := E[phi'(Z_i)phi'(Z_a)]              (4.4)

in probability, jointly for the fixed sample indices. Its correlation with v_aj causes no difficulty: convergence in probability to a constant and tightness of the other factors suffice.

For admissible orthogonal inputs in d>=3, Gamma=I. Then (4.3) has limit

    y_i m_ii phi'(V_i) sum_a y_a phi(V_a).              (4.5)

Here m_ii>=9/16, phi'(V_i)>=3/4, and the final sum is nonzero almost surely. To see the last assertion, the initialized Gaussian upper triple has nonsingular covariance (its first-layer feature Gram is positive definite for orthogonal inputs); conditioned on two coordinates, the sum is a strictly monotone function of the remaining coordinate, with nonzero derivative y_a phi'. Thus its zero set has probability zero.

The self-return in (4.5) is order one already at the second derivative. It is the effect a valid response/Onsager term must retain. Only the returned contribution (4.3) is being isolated; other learned-A contributions to the full upper acceleration are not suppressed or equated to this one.

### Why the actual tiny Gaussian readout does not remove (4.5)

At the common initialized W,A, compare derivatives at zero for a general readout c with those for zero readout. On an event bounding ||A||op, ||w||_n and all initialized feature L2 norms, if ||c||_n<=M/n, direct differentiation gives normalized L2 errors O_M(n^(-1)) in h_i''(0). This assertion follows from the following dimension-dependent bounds, which are sufficient at this single time:

    ||z_i'(0)||_n, ||h_i'(0)||_n, ||v_i'(0)||_n = O_M(n^(-1)),
    ||A'(0)||_F = O_M(n^(-1)),
    ||c||infinity, ||q_i(0)||infinity,
       ||z_i'(0)||infinity, ||v_i'(0)||infinity
         = O_M(n^(-1/2)).

The readout derivative differs from the zero-readout value by O_M(n^(-1)) in L2, since the initial residual differs by that amount. In

    b_i' = phi'(v_i) C' + phi''(v_i) v_i' C,
    q_i' = (A')^T b_i + A^T b_i',
    d_i' = phi''(z_i) z_i' q_i + phi'(z_i)q_i',
    h_i'' = phi''(z_i)(z_i')^2 + phi'(z_i)z_i'',

the displayed maximum bounds control each product remainder. They give the claimed O_M(n^(-1)) normalized error. The same argument applies to the cavity. Multiplication by a tagged row of bounded Euclidean norm raises that error by at most sqrt(n), yielding o(1) in (4.3).

For the prescribed Gaussian readout, n||C(0)||_n tends to one in probability. Thus the leading tagged self-return survives the actual random initialization. This derivative-at-zero estimate is not claimed uniformly on a positive training interval.

## 5. A finite-array obstruction to a generic exchangeability argument

The following construction is not an actual GF trajectory and is not a counterexample to the target theorem. It disproves the implication that bounded raw displacement, exchangeability, and good moments of the top backward inputs alone guarantee squared-tail control of the returned lower field.

Keep initialized W,A fixed. Let J be uniform on {1,...,n}, independent of them, and write a=A e_J. For one fixed sample i set

    b = sqrt(n) a/||a||_2,
    C_k = b_k / phi'(v_ik),
    q = A^T b.                                         (5.1)

The denominator lies in [3/4,1]. Therefore ||C||_n<=4/3. These are raw states at bounded distance from the target initialization, with no hidden-matrix displacement. All fixed coordinate moments of b and C are bounded uniformly in n: sqrt(n)a/||a|| is a uniform spherical vector of radius sqrt(n), and division by phi' multiplies its absolute value by at most 4/3.

Yet

    q_J = sqrt(n)||A e_J||_2,

and for every fixed R,

    (1/n) sum_k q_k^2 1_(|q_k|>R)
       >= ||A e_J||_2^2 1_(sqrt(n)||A e_J||_2>R)
       -> 1                                             (5.2)

in probability. The whole returned vector still has bounded normalized L2 norm on the usual bounded-operator event. The construction is equivariant under lower-coordinate permutations because J is uniform, and under upper-coordinate permutations because all formulas transform together. Thus exchangeability does not repair this failure.

The actual GF may well exclude these states. Showing how its physical path excludes concentration of this kind is precisely additional reachability information that a successful cavity proof must supply.

## 6. Remaining bridge and next use

The exact statements above preserve the one Gaussian matrix, its repeated forward/backward use, the learned rank updates, physical residuals, all raw metric factors, and the actual small readout.

What is now available:

1. Dimension-independent Gaussian forcing moments for a deleted top row, with no temporal independence assumption.
2. A raw path comparison with only one reference incoming maximum, growing linearly in that maximum inside the stability exponent.
3. An explicit nonvanishing tagged self-return that any cavity limiting equation must reproduce.
4. A finite-array adapted-state example ruling out a generic exchangeability-plus-energy-ball inference.

What remains unresolved is a cap-independent estimate on the actual returned q_i (or a direct comparison principle bypassing its maxima), together with controlled identification of the tagged self-return beyond the initialization expansion. A fresh-row approximation that drops (4.3) would identify the wrong canonical action. A theorem proved only up to the incoming-field stop in Section 3 is still a stopped theorem. No claim about full-sequence GF/GD limits, velocity laws, or global population uniqueness follows from the present note alone.

The finite program foundations can be used once such a comparison estimate is available; this note does not assume that finite-program convergence is uniform in a transcript length increasing with width. Existing global fitting or finite total residual-clock estimates are not used or required by the compact-horizon goal.

## 7. What the new energy-dissipating caps change

The subsequently supplied ENERGY_ROUTE.md constructs genuine canonical-space approximants by multiplying the whole first-row gradient by one scalar chi_R(Q), clipping the whole readout velocity, and leaving the adjacent-matrix update equal to its true gradient. That construction supplies its own global raw energy bound. It removes the need to assume a separately justified primal stopping bound for those reference paths.

It does not, by its pointwise invariants alone, remove the tagged return in Section 4. In particular, the new bounds |C(t)|<=2RT and |w(t)-w(0)|<=constant(T)R are not bounds on A(0)^T b(t). The next section gives a stronger finite-array test of a proposed replacement of the incoming maximum by its average. This is a test of a deterministic comparison principle, not a claim that the capped trajectories reach the constructed states.

## 8. Bounded readout, energy-compatible endpoints, and unbounded negative curvature

Here is an exact-model obstruction to a width-independent pointwise or one-sided Lipschitz bound based only on primal bounds, averaged q, bounded readout, row displacement, and the numerical endpoint energy inequality.

Take three orthogonal inputs (d>=3), all labels +1, and retain initialized W,A. Select a uniformly random lower index J, independent of the initial arrays. Fix one sample i. Put G_k=sqrt(n) A_kJ and define the new readout state by

    C_k = 2/3 - (1/4) tanh(G_k)/phi'(v_ik).             (8.1)

All v in (8.1) are evaluated with initialized W,A. Since 3/4<=phi'<=1,

    1/3 <= C_k <= 1,
    ||C||_n <= 1,     w=w(0),     U=0.                (8.2)

Thus this example has a width-independent pointwise readout bound, stronger than the moment bound in Section 5. Its first-row displacement is zero. All incoming L2 norms are bounded on the initialized bounded-operator event.

For the selected sample,

    b_ik = (2/3)phi'(v_ik) - (1/4)tanh(G_k),
    q_iJ = (2/3)sum_k A_kJ phi'(v_ik)
                   - (1/(4 sqrt(n)))sum_k G_k tanh(G_k).

Conditional on W, the first sum is O_P(1). Its summands are independent across upper rows, have mean zero by the simultaneous sign change A_k -> -A_k (phi' is even), and have total variance at most one. The ordinary law of large numbers for G_k gives

    q_iJ/sqrt(n) -> -kappa/4,
    kappa = E[G tanh(G)] > 0.                         (8.3)

The other q fields are bounded in normalized L2 because ||b_a||_n<=||C||_n<=1 and ||A||op is bounded. The random-index construction is equivariant under both layer permutations.

### Predictions and the endpoint energy check

For every sample a, f_a -> 1/2 in probability. Indeed, conditional on W, the upper rows are independent centered Gaussian triples, and E phi(V_a)=3/4 at every variance. Hence the constant part of (8.1) contributes 1/2 in the limit.

The other contribution is

    -(1/(4n))sum_k tanh(G_k) phi(v_ak)/phi'(v_ik).      (8.4)

Decompose v_ak=V_ak^(-J)+h_aJ G_k/sqrt(n), where the Gaussian triple V^(-J) is independent of G_k. If the shifts h_aJ G_k/sqrt(n) are removed, the expectation in (8.4) is zero because E tanh(G)=0. The removed shifts change the expectation by O(n^(-1/2)) when the finitely many h_aJ and empirical feature second moments are bounded: the quotient phi(v_a)/phi'(v_i) has at most linear growth, derivative in v_a bounded by 4/3, and derivative in v_i bounded by a constant times 1+|v_a|. The mean-value formula and Gaussian second moments give this bound. Its second moment is bounded uniformly, so the variance of the row average is O(n^(-1)). Conditioning on successively larger bounds handles the random first-layer data.

Thus r_a -> -1/2 and E -> 3/8. The actual initialized readout tends to zero in normalized norm and its initial loss tends to 3/2. The raw displacement of (8.1) from that actual initialization is at most 1+o_P(1). Consequently, at T=1 these states even satisfy

    raw displacement squared <= T [E(initial)-E(state)]

with probability tending to one: the right side tends to 9/8 while the left side is at most 1+o_P(1). This numerical compatibility is not construction of a dissipative path, much less a true gradient-flow path.

### Exact Hessian direction

Consider a unit-raw variation supported only at lower row J,

    delta w_J = sqrt(n)u_i,
    delta w_k = 0 for k != J,
    delta A = delta C = 0.                            (8.5)

Orthogonality of the inputs gives delta z_iJ=sqrt(n) and delta z_a=0 for a!=i. Therefore the exact loss Hessian in this direction is

    D^2 E[delta,delta]
      = phi'(z_iJ)^2 q_iJ^2/n
        + r_i q_iJ phi''(z_iJ)
        + r_i phi'(z_iJ)^2
                 sum_k C_k phi''(v_ik) A_kJ^2.        (8.6)

The first term is the complete Gauss-Newton contribution; the last is the upper activation curvature. The first is O_P(1) by (8.3), and the last is O_P(1) because |C_k|<=1, |phi''|<=1/2, and ||A e_J||_2^2 -> 1.

On the positive-probability event z_iJ in [1/2,1], phi''(z_iJ) is at most a fixed strictly negative number. By (8.3) and r_i -> -1/2, the middle term in (8.6) is at most -c sqrt(n), for a constant c>0 and with conditional probability tending to one. Thus the smallest raw loss-Hessian eigenvalue is unbounded below on these states, despite all the preceding bounds.

This excludes a dimension-independent one-sided Lipschitz estimate for the true raw vector field on the whole class specified by those bounds. An estimate replacing R in Section 2 by merely ||q||_n cannot hold on that class. The example even keeps z_iJ in the curved part of phi, so division by 1+|z_iJ| does not remove this particular instantaneous obstruction.

It does **not** exclude an integrated-curvature estimate along actual physical paths. The large q in this example also drives the corresponding z rapidly through the curved region. A residence time of order n^(-1/2) could compensate the instantaneous curvature of order sqrt(n). Nor does it exclude a comparison exploiting correlation between the cavity perturbation and the incoming field.

### Why instantaneous cap dissipation does not settle this tail

At the same states, the first-row q tuple has Q_J of order sqrt(n), and the true first-row gradient has magnitude of order sqrt(n), since the inputs are orthogonal, |r_a| approaches 1/2, and phi'>=3/4. For a fixed cap R, the energy approximation's scalar satisfies chi_R(Q_J)<=2R/Q_J. The selected row's contribution to its dissipation is therefore at most constant times R/sqrt(n), while the squared raw norm of the missing first-row direction at J stays bounded below by a positive constant.

This is an instantaneous algebraic example. It shows why the cap energy identity alone does not bound its L2 direction defect: a rare large gradient can have small capped dissipation. It is not evidence that such a defect survives over a time interval in the actual cap construction.

## 9. An averaged-q estimate that does hold for a fresh cavity direction

There is a useful restricted replacement of an incoming maximum. Condition on all cavity data and let a=(a_1,...,a_n) be the independent deleted row with a_k~N(0,n^(-1)). Let v be any deterministic cavity vector, and let S be any scalar function of that row and additional randomness with finite conditional fourth moment. Independence of S and a is not required. Then

    E[ ||v times a times S||_n^2 | cavity ]
       <= (sqrt(3)/n) ||v||_n^2
                    ||S||_(L4 | cavity)^2.            (9.1)

Proof: for each k, Cauchy-Schwarz and E a_k^4=3/n^2 give

    E[a_k^2 S^2 | cavity]
       <= (sqrt(3)/n) (E[S^4 | cavity])^(1/2).

Multiply by v_k^2/n and sum. Bounded cavity gates can be absorbed into v. A fixed sum of the three sample terms costs only a fixed numerical factor.

Thus a fresh Gaussian cavity forcing can be multiplied by a reference incoming field using its averaged L2 norm, provided its scalar amplitude has an appropriate conditional fourth-moment bound. This precisely covers a fresh lower-layer kick of the form a_j^T times a bounded gate and tagged scalar amplitude. Under the new cap family a tagged readout amplitude is bounded at each fixed R, so this conditional estimate is directly available at that level.

The propagated cavity difference is not itself a fresh Gaussian direction: repeated returns change its dependence on the same row, and its linear response can become concentrated on coordinates with large incoming values. Applying (9.1) to the entire propagated discrepancy without retaining that dependence would be an unjustified substitution. A successful next lemma would propagate a weighted estimate of the form (9.1) through the actual returned response, with constants independent of the cap; that lemma is not proved here.

## 10. Status after the cap-family follow-up

The new global cap construction is compatible with the exact cavity identities and supplies global reference paths. The current cavity analysis neither removes its caps nor disproves their removability.

The sharper conclusions are: an averaged-field bound suffices for a genuinely fresh Gaussian kick, but fails as a universal pointwise stability bound for arbitrary states satisfying even the natural cap invariants and endpoint energy inequality. The distinction isolates the remaining mathematical work to physical reachability, controlled tagged response, or integrated curvature. No old coefficient-box assumption, an independent reverse matrix, or a Gaussian law for the trained incoming field is used to close that gap.
