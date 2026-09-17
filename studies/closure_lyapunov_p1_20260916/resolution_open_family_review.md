# Independent analytical review of the open three-input family

2026-09-16. **Verdict: PASS within the precise scope stated below.** No
blocking mathematical flaw was found. No experiment was performed. This is an
internal analytical review, not promotion or a trained-network identification.

## Frozen inputs and isolation

The reviewed candidate is `resolution_open_family.md`, SHA-256
`6c949bdec4e78fb895ae71281edd328623a662cba433fba618d65e82055fe337`.
The checksum was verified before and after reading. The complete 711-line
dependency `three_coordinate_candidate.md` was read and checked; its SHA-256 is
`531b1cb1fe5e5844fcc6da25486e6ee52450860030dd770246e3ee78592521ce`.

The other inputs were the complete `docs/README.md`, `docs/NOTATION.md`,
`docs/observable_p1.md`, and the complete permitted sections of
`docs/global_nonlinear.md`: C.4.7.9 and C.4.7.10 B, C.1, D.3. Required skills
and their research-contract/adversarial-audit instructions were read. No study
README, history, prior audit, other review, experiment, or other study was read.
In particular, the prior independent audit mentioned by the candidate was not
an input. Its verdict is unnecessary: the mathematical arguments needed here
are supplied in the permitted complete candidate and are checked below. No
missing scientific input blocks this review.

## Exact claim that passes

The result concerns the exact population, general-dimensional **p=1 closure
in d=3**, with ridge eta=1/4096, the specified complete correlated Gaussian
initialization, zero population readout, full evolving 4-by-7 matrix and its
actual transpose, and the fixed population-L2/population-L2/Frobenius metric.
The loss is the unhalved mean of three squared residuals. Labels and masses
remain (1,1,-1) and (1/3,1/3,1/3); only the three unit input directions vary.

For every sufficiently small fixed e>0, a positive neighborhood of the signed
seed directions exists on which the initialized physical flow has a uniform
positive lower bound on its full normalized tangent Gram for all t>=0. This
gives the displayed exponential loss bound, the finite tail-length bound,
strong full-state convergence, and complete-joint-law W2 convergence. After
possibly shrinking that neighborhood, the displayed mixed potential also
satisfies a uniform strict exponential differential inequality from t=0.

The neighborhood and rates can depend on e; none is asserted uniform as e
tends to zero. The theorem does not cover arbitrary three-input geometries,
varying labels or masses, the original d=2 circle problem, finite integration
rules, or actual neural-network limits. These limitations are essential and
are stated in the candidate.

## 1. Canonical initialization and the supplied symmetric theorem

The normalized columns and the two initialized matrix bands agree exactly
with the general-d identities in `observable_p1.md`. In particular, the
tau*gamma reverse-response contribution is retained, lower G and k marks
remain correlated, and the right Cholesky transpose is correct. The identity

    E[b_l b_l^T] = I - eta L_l^(-1)L_l^(-T) <= I

establishes the contraction bounds used throughout. The feature envelopes are
finite. Positivity of all normalization denominators follows from eta>0 and
beta^2<=v*sigma. No higher-dimensional bound on an uncompressed Gaussian
action is silently imported.

Direct variation of f gives exactly the three gradient blocks in the
candidate. The fixed metric and equal masses consequently give

    X_dot = -(2/3) sum_i r_i grad f_i,
    L_dot = -||X_dot||^2.

The dependency's finite-time continuation proof applies to all the perturbed
unit-input triples: it uses only bounded labels, unit input norms, feature
contractions and the dissipated loss. Its auxiliary-flow bounds are likewise
uniform in these directions. Existence is therefore available before using
the fitting or trapping arguments.

I checked the dependency's initialized scalar map, rather than assuming its
monotonicity. The bounds on the conditional gate imply the positive derivative
in its equation (29), including when its coefficient A is negative. Gaussian
integration by parts then gives equation (30), and continuity handles the
correlation endpoints. For the seeds used here a>b>0, so
kappa(a)>kappa(b)>0. The three initialized upper-field coefficient vectors
are therefore linearly independent, and the positive-density argument proves
that their readout Gram is positive definite. The dependency's exceptional
case kappa(a)+2*kappa(b)=0 is also correctly handled by its cubic derivative,
although that case is not needed for this open-family construction.

The normalized permutation isometries are correctly specified. Their
invariance preserves equal signed predictions for the symmetric seed without
equating individual tangent vectors. The scalar auxiliary argument uses only
C_0>0, F_s=||grad F||^2 and q_s=2F. Cauchy-Schwarz gives q*F_s>=F^2,
which proves q/F^2<=1/C_0 and F_s>=C_0 after taking the justified initial
limit. The mixed-potential derivative in that dependency includes the full
readout-dependent term. These facts also apply to coincident compatible
directions, once their C_0>0 is checked. No rank-three claim is needed at the
coincident limit.

## 2. Hilbert continuity and the normalized initial-time limit

Section 3's Hilbert estimates are valid on bounded sets of (w-G,c,M).
The frozen Gaussian appears in input changes only through

    ||w_tilde||_2 |u-u_tilde|,

which is uniformly bounded on such a set. In particular there is no false
claim of uniform pointwise continuity of a Gaussian ridge in its input.
Contraction first controls a, finite bounded features then control z2 in
L-infinity, and the displayed Cauchy-Schwarz bound controls d. Consequently
Q is bounded and Lipschitz in L-infinity. Multiplying by the bounded lower
gate gives the claimed L2 gradient control, including the vector factor u.
The other gradient blocks, predictions and full Gram follow by subtraction.

The scalar finite-feature contractions are Frechet differentiable in the
Hilbert variables; the lower-gate Taylor remainder after contraction is
bounded by a constant times ||delta w||_2^2. Thus the gradients used for
the potential are legitimate even though a general nonlinear Nemytskii map
L2 to L2 need not have the corresponding stronger differentiability property.

Subtracting the integral equations and applying an integrating factor gives
uniform finite-interval dependence. The auxiliary bounds provide a common
ball independent of e. Upper preactivations converge in L-infinity because
their finite coefficient vectors converge. Hence

    c_e(s)/s = integral_0^1 U_e(sv) dv

converges uniformly for 0<=s<=S_*, with the continuous value U_e(0) at
s=0. Substituting this formula into d_e(s)/s and using convergence of the
upper gate proves the required uniform normalized convergence. Merely
knowing d_e converges would not justify this step; the candidate supplies
the necessary stronger argument.

## 3. The compatible-coincident reference

The global mark-negation invariant subspace has odd w,c and zero constant
row/column of M; its invariance is supplied explicitly by `observable_p1.md`.
Together with permutation invariance this yields z2=p(s)S, where
S=Z_1+Z_2+Z_3. The initialized scalar-map calculation gives p(0)>0.

While p remains positive, c(s,S)=integral_0^s tanh(p(r)S)dr has the sign
of S for s>0. The upper reverse coefficient is therefore h(s)*1 with

    h(s) = E[S c(s,S) sech^2(p(s)S)]/(3 RZ) > 0.

The integrand is positive except on S=0, and S has a positive density on
(-3,3). The same argument gives the stated strictly positive value of h/s
at s=0.

There is no circular persistence assumption: for the single input, direct
differentiation gives a_s=B M^T d, with
B=E[b1 b1^T sech^4(w.v_*)] positive semidefinite. Therefore

    3 RZ p_s = h(s) [3|a|^2 + 1^T M B M^T 1] >= 0

on every interval where p>0. A first zero would contradict p>=p(0).
Finite auxiliary existence excludes escape through an infinite value at
finite s. Thus p>0 and h(s)>0 on every finite auxiliary interval.

The six active lower features are linearly independent. Conditioning a
putative relation on G gives a sum of independent conditional variances of
the k coordinates, all strictly positive, so their coefficients vanish.
Independence and positive variances of tanh(G_j) remove the remaining
coefficients. Cholesky normalization preserves this conclusion. Also
Ma=RZ*p*1 implies M^T*1 cannot vanish. Continuity on [0,S_*] now gives
both strictly positive compact minima used in section 5, including h(s)/s
at the initial endpoint.

## 4. Full tangent rank for the nearby symmetric seeds

The permutation commutant on each active three-coordinate block is exactly
the span of P_parallel and P_perp. Hence the candidate's decomposition and
the identity

    |M^T d_i|^2 = d_parallel^2 |m_parallel|^2/3
                  + 2 d_perp^2 |m_perp|^2/3

are correct. Uniform normalized convergence preserves nonzero
m_parallel and positive d_parallel/s for all sufficiently small positive
e on the entire fixed interval. Thus Q_i is nonzero in lower L2 for s>0.
The lower gate is positive almost surely at every finite state, proving
R_i(s)>0.

The first-layer estimate is pointwise before expectation: if
t_i=z_i sech^2(w.v_i)Q_i, then

    |sum_i t_i v_i|^2 >= lambda_min(G_input) sum_i t_i^2.

For the seed,
lambda_min(G_input)=e^2/(3+2e+e^2)>0. Integration proves that the
first-layer Gram alone is positive definite for every s>0. Dividing by
three gives its contribution to the candidate's normalized K. At s=0 that
block vanishes, but the independently proved initialized readout Gram is
positive definite. Continuity of the full K on the compact auxiliary
interval therefore proves mu_e>0. The argument does not require a uniform
lower bound on R_i as s tends to zero, and does not assume persistent upper
hidden-feature separation.

## 5. Infinite-time capture and state convergence

The auxiliary seed curve, including its fitting endpoint, is compact in the
Hilbert state space. Local uniform Lipschitz control of K on a surrounding
bounded ball gives a positive state-tube radius and a positive data radius
with K>=kI, k=mu_e/2. This uses compactness of a continuous curve, not the
false assertion that an infinite-dimensional bounded ball is compact.

The seed's scalar fitting theorem supplies a finite time T with sufficiently
small loss. Finite-time data dependence puts perturbed trajectories within
r/4 of the seed on [0,T] and gives sqrt(L(T)/k)<r/8. With the prescribed
normalization z=r_residual/sqrt(3), the exact identities are

    L=|z|^2,   L_dot=-4 z^T K z,
    ||X_dot||^2=4 z^T K z.

Inside the tube these imply

    -d sqrt(L)/dt >= sqrt(k) ||X_dot||.

Thus the path after T, up to any proposed exit, has length below r/8.
Its distance to the fixed curve point X_seed(T) stays below 3r/8, which
contradicts reaching the radius-r boundary. Finite-time global existence and
continuity are already proved independently. A zero-loss state is stationary
by the displayed gradient equation, so it introduces no exception.

This establishes coercivity from t=0 for the actual perturbed flows. The
loss estimate has no missing entry-time prefactor. The same length argument
from any t gives the asserted tail bound. Hilbert completeness gives a
strong state limit; continuity of predictions and loss gives exact fitting.
Coupling frozen (b1,G) and b2 identically bounds the squared joint-law W2
costs by the lower-state and readout L2 errors, respectively. Their second
moments are finite. No cross-population law coupling is inserted.

## 6. Mixed-potential derivative on the whole trajectory

For the actual perturbed dataset, C_0 is a fixed positive number. The formula
for grad W is the exact derivative of
W=1+C_0(1+q)/(C_0+F^2). Together with the exact physical vector field it
gives

    Phi_dot = W L_dot + L <grad W,X_dot>.

A bounded ball containing the closed tube has bounded c,M and gradients.
After shrinking the data radius, C_0 is bounded below by half the seed value.
Hence finite uniform B and Lambda exist as claimed. The remainder satisfies

    L |<grad W,X_dot>| <= 2 B sqrt(Lambda) L^(3/2).

When sqrt(L)<=k/(B sqrt(Lambda)), this is at most 2kL<=2kPhi,
which proves Phi_dot<=-2kPhi. No monotonicity of W, q or F is needed.

There is no circular choice of T: fix the tube and these constants first,
then enlarge T to meet both the capture and residual conditions, and finally
choose the finite-time data neighborhood for that fixed T. On [0,T], the
seed has Phi>0 with a positive compact minimum and
Phi_dot/Phi<=-4*C_seed. Uniform dependence and continuity of the exact
derivative preserve the weaker bound -2*C_seed in a positive neighborhood.
The loss is decreasing after T, preserving the tail condition. Taking the
minimum of the two rates proves the claimed all-time inequality. At
initialization F=q=0 and L=1, so Phi(0)=2 exactly; W>=1 gives L<=Phi.

## Required repairs and remaining scope

**Required mathematical repairs: none.** The mention of an earlier audit
could be removed from the dependency sentence for a cleaner self-contained
presentation, but this is editorial: none of the proof relies on its verdict
or on an unavailable scientific result.

The adversarial possibilities examined—loss of reverse response at the
coincident reference, nonuniform division by s, initial vanishing of the
first-layer tangent block, input-continuity failure from Gaussian tails,
escape after a finite comparison interval, and a missing derivative of the
mixed potential—are closed by the supplied arguments at the stated scope.
No numerical radius, uniform e-limit, arbitrary-geometry result, d=2 theorem,
network-identification theorem, or uniqueness of the fitted state follows.
The passing conclusion is an exact open-family all-time fitting and
mixed-potential theorem for the specified initialized d=3 p=1 closure.
