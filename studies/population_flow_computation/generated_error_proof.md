# Persistent representative solver: fixed-graph error bridge

Status: internally derived finite-graph result, not promoted. No experiment was
run for this note. It proves consistency of the specified generated-state
scheme at each fixed physical Euler mesh and fixed training-source noise
`s > 0`. It does not certify a simultaneous time-mesh/source-noise limit or a
physical-time-40 resource budget.

The inputs are the complete `directional_solver_spec.md` (including weighted
probes, removal of the current upper probe before estimating old responses,
and clean passive queries), III.F in `docs/special_data_limits.md`, and the
source equations and estimates C.4.7.N2--N18 in `docs/global_nonlinear.md`.
Only those scientific inputs were used. The argument below is new analysis;
III.F does not by itself state a sample-complexity theorem for this solver.

## 1. Statement and comparison process

Fix a finite law with positive masses, a finite positive-step mesh, its
physical horizon T, and s > 0. Zero-mass atoms are removed as specified. Write
J for the number of training source names and omega_p = h_k p_a for the mass
of a name p = (k,a). All histories remain in the state. A fixed finite list
of same-layer joint observables, including initial/current pairs and any
desired contractions, may be appended. The lower and upper representative
populations are separate.

Define the deterministic-coefficient comparison program causally by replacing
each empirical average in the specification by the expectation of its
already defined argument. Its training covariance matrices are the indicated
uncentered input Grams plus s^2 I. Its formal source derivatives freeze every
coefficient, residual, covariance and contraction. This defines the noisy
finite source process; it is not a definition by an unknown simultaneous
fixed point. At positive s no assertion that this modified process is an
exact retained initialized action is needed.

For each lower representative i take an independent primitive tuple
U_i^- consisting of its two Gaussian root coordinates, J standard Gaussian
innovations, and J independent Rademacher signs. For each upper representative
take U_i^+ consisting of J innovations and J signs. All these primitive tuples
are independent. Run both the empirical program and the deterministic-
coefficient comparison program using exactly these same primitives, preserving
every old innovation and sign. Denote their node tuples by X_i^P and bar X_i.
The bar X_i are iid within each population because their coefficients are
deterministic. The X_i^P are generally dependent. Independence of the latter,
even conditional on their feedback coefficients, is never asserted.

For every fixed same-layer tuple, in exact arithmetic,

    W2(P^{-1} sum_i delta_{X_i^P}, Law(bar X_1)) -> 0

in probability as P -> infinity. Every specified same-layer contraction
converges as well. Below is a computable high-probability bound proving this
claim. Mathematical consistency holds for arbitrary fixed real model
parameters; effectiveness of the numerical bound presupposes computable input
parameters with supplied bounds and a positive lower bound for s and each
retained omega_p.

Sections 3--6 give the quantitative bound for the retained training graph and
smooth observables of it. Section 7 appends clean passive source queries,
whose possibly singular covariance square root has a weaker continuity
modulus. The linear error modulus in (12) is not claimed for that last step.

## 2. The weighted response identity and its variance

In a deterministic-coefficient program, let F be a scalar node, let
a_p = partial_p F for its eligible source names, and let epsilon_p be the
independent signs used by its population. Its directional tangent is

    dot F = sum_p a_p epsilon_p / sqrt(omega_p).

The node F and its a_p depend on Gaussian primitives but not on these signs.
Consequently

    E[sqrt(omega_p) epsilon_p dot F] = E[a_p].                 (1)

This is the response coefficient required by III.F.9--10 and C.4.7.N4.
It differentiates named source expressions, including at singular clean
covariances; it does not differentiate a Cholesky factor or the feedback map.
Linear tangent propagation through the specified frozen-coefficient updates
proves the displayed expression for dot F by induction.

For an upper current output, the direct current contribution to its tangent
is exactly c phi''(Z) epsilon_current / sqrt(omega_current). Subtracting it
pointwise leaves only old source derivatives. The current coefficient is
estimated separately as the sample mean of c phi''(Z), with exact zero
off-diagonal current entries. Subtraction is an exact finite-array algebraic
operation even after feedback; its unbiasedness justification is used only
in the deterministic comparison program. There is only one distinguished
direct current name per output, as in C.4.7.N6.

Here is a useful variance bound for a frozen correction. Let z_p belong to a
fixed real Hilbert space, representing the opposite population's histories.
Use P iid copies of the derivative/sign tuple to form

    Ahat = P^{-1} sum_i (sum_p sqrt(omega_p) z_p epsilon_ip)
                                (sum_q a_iq epsilon_iq/sqrt(omega_q)),
    A = sum_p z_p E[a_p].

Then

    E ||Ahat-A||^2 <= (3/P)
       (sum_p omega_p ||z_p||^2)
       (sum_p E|a_p|^2/omega_p).                            (2)

To verify the constant, put u_p = sqrt(omega_p) z_p and
b_p = a_p/sqrt(omega_p). Conditional on the Gaussian primitives, expansion
of the four signs gives

    E_epsilon[||sum_p u_p epsilon_p||^2 (sum_q b_q epsilon_q)^2]
      = (sum_p ||u_p||^2)(sum_q b_q^2)
        + 2||sum_p b_p u_p||^2 - 2 sum_p b_p^2 ||u_p||^2
      <= 3(sum_p ||u_p||^2)(sum_q b_q^2).

Integrate and divide the variance of an iid sample mean by P. This proves
(2), without assuming orthogonality of histories. It is a Hilbert norm bound
for the whole contracted correction, rather than an entrywise error multiplied
by the number of source names.

Under the temporary backward-row cap B of C.4.7.N10--N18, lower old derivatives
obey ||partial_p H||_2 <= L_2(B) omega_p. The displayed single-pulse upper
recursions also yield the pointwise old-derivative bound

    |partial_p Delta| <= b_B omega_p.

Indeed N8 and the bounds preceding N17 give
|C_{k;p}| <= 2R_0 omega_p + 2R_0 sum_j h_j max_a |U_{ja;p}| and
|U_{ka;p}| <= f_B d_0 omega_p exp(f_B d_0 T). Thus
|V_{ka;p}| <= [2R_0+d_0^2 f_B exp(f_B d_0 T)] omega_p.
The direct current derivative is excluded here. For s-noisy training
covariances the same capped calculation replaces the Gaussian variance C_0^2
by C_0^2+s^2 in the exponential-moment estimates; all constants remain finite
and uniform over a bounded range of s.

Therefore the derivative factor in (2) is at most L_2(B)^2 T for a lower row
and b_B^2 T for an old upper row. The history factor is at most C_0^2 T for
upper histories and T for lower histories. These frozen contracted variances
have no inverse minimum atom mass or step. The separate current diagonal
sample mean has variance at most 4 C_0^2/P. Such estimates require the stated
cap; they do not establish it for every noisy or generated program.

## 3. The training Cholesky floor and quantitative stability

The pointwise readout bound holds for the empirical solver itself:

    max_i |c_{k+1,i}| <= (1+2h_k) max_i |c_{k,i}| + 2h_k Y,
    max_{k,i} |c_{k,i}| <= C_0 := Y(exp(2T)-1).              (3)

The first inequality uses |phi| <= 1, |f_{ka}| <= max_i |c_{k,i}|,
and sum_a p_a = 1. It needs neither independence nor a response cap.
It also holds for the deterministic comparison process. Hence |H| <= 1 and
|D| <= C_0 in both programs. Every entire retained covariance matrix K obeys

    s^2 I <= K <= Lambda I,
    Lambda := s^2 + J max(1,C_0^2).                         (4)

Here the upper bound follows from the Gram trace. Because saved histories
are immutable, the preserved block factor is the Cholesky factor of this
entire retained Gram. It is not a factor of a recomputed history.

For a partition of K into old and new names its Schur complement satisfies

    x^T Schur(K) x = min_y (y,x)^T K (y,x) >= s^2 |x|^2.   (5)

Thus every exact training extension is defined, regardless of the rank of
the empirical input matrix or the relation between P and J.

Let L = chol(K), with positive diagonal. Differentiating LL^T = K yields

    dL = L Phi(L^{-1} (dK) L^{-T}),

where Phi keeps the strictly lower triangular part and halves the diagonal
of a symmetric matrix. Since ||Phi(E)||_F <= ||E||_F,

    ||D chol(K)[E]||_F <= sqrt(Lambda) s^{-2} ||E||_F.

The segment between any two matrices satisfying (4) satisfies (4). Integration
along this segment therefore proves

    ||chol(K)-chol(Kbar)||_F
       <= sqrt(Lambda) s^{-2} ||K-Kbar||_F.                 (6)

This is a fixed-size positive-floor estimate. It does not claim continuity
of the chronological Cholesky construction uniformly as s -> 0. Source rows
are E_i L^T, so using the identical retained innovation row transfers (6)
directly to a rowwise source error bound.

## 4. Effective envelopes for the finite calculation

Let G_i collect all Gaussian primitives in a representative pair, and let
A_i = 1+sum_j |G_ij|. Rademacher magnitudes are one; weighted probe magnitudes
are the known constants omega_p^{-1/2}. Each node of the deterministic
comparison program and each scalar averaging integrand has a bound by a
polynomial in A_i with nonnegative, computable coefficients.

This can be constructed instruction by instruction, without knowing any
target trajectory. Sums add envelopes, products multiply them, tanh and its
first two derivatives have bounds 1, 1 and 2, respectively, and every source
row has magnitude at most sqrt(Lambda) ||G_i|| by (4). An expectation node is
bounded by the expectation of its already constructed polynomial envelope.
For coefficient sensitivity, tanh's third derivative is also bounded (the
conservative bound 6 suffices from differentiating -2 tanh(1-tanh^2)).
The tangent recursions are finite sums and products of these objects.

All needed polynomial moments have explicit upper bounds. If n is the number
of Gaussian primitive coordinates, then for every integer r >= 1,

    E A_i^r <= (n+1)^r max(1, E|N(0,1)|^r),
    E|N(0,1)|^r = 2^{r/2} Gamma((r+1)/2)/sqrt(pi).          (7)

The first bound is the convexity inequality for a sum of n+1 nonnegative
terms; the second is direct integration of the Gaussian density. Thus this
procedure bounds moments of every required order by finite arithmetic and
Gaussian moments. It invokes no unproved uniform moment estimate over
growing graphs.

A second, purely deterministic, envelope is useful for stability. On the
event max_{i,j}|G_ij| <= R, both complete programs have polynomial bounds
in R. For the empirical program, an average is bounded by the maximum of its
integrand envelope, so no independence is involved. Intermediate covariance
solves have bounds using s^{-1}; alternatively use the entire Cholesky map
(6). All non-averaging operations have computable Lipschitz bounds polynomial
in R, with constants depending on the fixed graph, s and the omega_p.
Products use their bounded input envelopes; gates use the derivative bounds;
covariance operations use (6). The same bounds hold between the two arguments
being compared, using their common bounded box and the convex covariance
domain (4).

For complete explicitness, expand the fixed program into an ordered finite
list of vector operations and scalar feedback operations. For each instruction
v choose a bound L_v(R) on its Lipschitz constant in the sum of its parent
norms. A vector norm is maximum absolute coordinate over representatives;
scalar and fixed matrix norms may be converted to this norm with their
explicit fixed dimensions. An averaging operation has norm at most one from
the maximum norm on its summands. Set a_v=0 for shared primitive nodes, and
recursively set

    a_v(R) = L_v(R) sum_{u in parents(v)} a_u(R) + 1.        (8)

The added one is deliberately included at every instruction to allow an
arithmetic residual, and at averaging instructions to allow a sampling
residual. Let C(R) be the maximum of these a_v over the required outputs and
all intervening instructions. This defines a computable polynomial majorant.
Matrix/vector dimensions and all constants are supplied by the fixed graph;
there is no factor P in these exact-arithmetic Lipschitz bounds because sums
over representatives occur only as averages.

## 5. The adaptive bridge and a sample bound

List every scalar sample average in the graph, adding any contractions to be
reported. Let Psi_v(bar X_i) be its integrand evaluated in the deterministic
comparison program, with its own population index. Set

    zeta_v = P^{-1} sum_i Psi_v(bar X_i) - E Psi_v(bar X_1),
    V_* = sum_v E |Psi_v(bar X_1)|^2.                       (9)

Equation (7) gives an explicit finite upper bound for V_*. Sample averages
at different instructions need not be independent. For each individual v,
the comparison rows are iid, so a union bound and Chebyshev give

    Pr(max_v |zeta_v| > eta) <= V_* /(P eta^2).             (10)

The essential decomposition at an empirical feedback instruction is

    P^{-1} sum_i Psi_v(X_i^P) - E Psi_v(bar X_1)
      = P^{-1} sum_i [Psi_v(X_i^P)-Psi_v(bar X_i)] + zeta_v. (11)

The first term is bounded deterministically by earlier paired errors and
the local Lipschitz envelope. Only the second term receives an iid estimate.
Equations (8) and (11), applied in causal order, give on the event that all
Gaussian primitives are bounded by R and max_v|zeta_v| <= eta,

    max_{i,v in training graph}|X_{iv}^P-bar X_{iv}|
       <= C(R) eta.                                     (12)

This also controls coefficient differences. It deals with reused samples,
probe-dependent generated coefficients, correlations between the two generated
populations, and every retained innovation. It never resamples a history or
conditions a retained population to be iid.

There are n_G = 2+2J Gaussian primitive coordinates per representative pair
before passive queries. The Gaussian exponential-moment bound and a union
bound show

    Pr(max_{i,j}|G_ij| > R) <= 2P n_G exp(-R^2/2).          (13)

For 0 < delta_1,delta_2 < 1 choose

    R = sqrt(2 log(2P n_G/delta_1)),
    eta = sqrt(V_* /(P delta_2)).                          (14)

Then (12) holds with probability at least 1-delta_1-delta_2.
Since C is a fixed polynomial, C(sqrt(log P))/sqrt(P) tends to zero.
This proves a genuine generated-state coupling rate for the fixed graph.
The high-degree polynomial and its constants may be extremely large; a finite
computable upper bound is not a claim of practical sample size.

For any included scalar contraction, suppose the comparison scalar-node
envelopes on the same event are bounded by B(R), and put e=C(R) eta.
Decomposing the two factors pointwise gives

    |P^{-1} sum_i U_i^P V_i^P - E[bar U bar V]|
       <= 2 B(R)e + e^2 + eta,                             (15)

where the contraction's comparison average is included in (9). Rank-factor
norms formed from finitely many such contractions and gamma coefficients are
controlled by their finite polynomial formula in the same way.

## 6. Explicit empirical joint W2 control

For a d-dimensional same-layer tuple let mu=Law(bar X_1), and let
M_4 >= E|bar X_1|^4 be supplied by (7). The coupling pairing representative
indices gives

    W2(P^{-1}sum_i delta_{X_i^P}, P^{-1}sum_i delta_{bar X_i})
       <= sqrt(d) e.                                     (16)

An elementary quantitative bound handles the remaining iid empirical law.
Clip each coordinate to [-B,B] and quantize the cube into K cells of diameter
at most a, with

    K <= (1+2B sqrt(d)/a)^d.

The expected squared clipping cost is at most M_4/B^2, and quantization costs
at most a^2. The discrete empirical masses have expected total absolute
error at most sqrt(K/P), since each cell frequency has variance
p_cell(1-p_cell)/P and Cauchy--Schwarz applies to the sum. Unmatched mass is
one half this absolute error and travels squared distance at most 4dB^2.
Using (x+y+z)^2 <= 3(x^2+y^2+z^2) for the two quantization transports and the
discrete transport gives

    E W2^2(P^{-1}sum_i delta_{bar X_i},mu)
       <= D_P(B,a)
       := 12 M_4/B^2 + 12a^2 + 6dB^2 sqrt(K/P).            (17)

Thus for any delta_3 > 0, combining Markov with (12)--(16),

    W2(P^{-1}sum_i delta_{X_i^P},mu)
       <= sqrt(d) C(R) sqrt(V_* /(P delta_2))
          + sqrt(D_P(B,a)/delta_3)                        (18)

with probability at least 1-delta_1-delta_2-delta_3. For example, choosing
B=P^{1/[4(d+2)]} and a=P^{-1/[4(d+2)]} makes every term of D_P tend to zero.
Alternatively choose B and a from a desired error and solve explicitly for P.
Initial/current fields belong to the same tuple and retain the same roots
and source innovations. This proves joint-law convergence and does not infer
it from separately estimated marginal laws.

## 7. Finite precision and clean passive queries

The exact-arithmetic bound has a corresponding precision statement in terms
of certified residuals. Compare the arithmetic implementation first to the
exact empirical program with the same ideal primitives. Expand its operations
into a finite scalar list, including the triangular solves and Schur-block
factorizations actually used. Every exact diagonal divisor in those solves
is at least s, and every exact Cholesky square-root argument is at least s^2,
by (5). Static denominators such as omega_p and P are also positive and known.
Choose a computable radius rho > 0 no greater than 1, s/2, s^2/2, and half
every other required positive denominator margin.

On the radius-rho tube about exact empirical intermediate values, reciprocals
and square roots have bounded derivatives, and all other operations have the
polynomial envelopes already described. Bound the derivative of reciprocal
on [s/2,infinity) by 4/s^2 and that of square root on [s^2/2,infinity) by
1/(sqrt(2)s). Form C_arith(R,P) by recursion (8) on this expanded list, taking
a_v=1 at rounded primitive/input nodes. It may depend on P because the
expanded arithmetic list includes the summations. If each primitive/input
error and each scalar operation residual is at most tau and

    C_arith(R,P) tau <= rho,                              (19)

induction keeps every operation within this tube and gives arithmetic error
at most C_arith(R,P) tau. Combining with the separately proved statistical
coupling yields

    max_{i,v}|X_{iv}^{P,arith}-bar X_{iv}|
       <= C(R) eta + C_arith(R,P) tau.                    (20)

Use the right side as e in (15), (16), and (18). This construction certifies
the actual block algorithm's intermediate pivots, not merely the definiteness
of a nearby full covariance. Equivalently, obtain a certified residual for a
matrix/average operation by grouping the corresponding expanded operations.
For example, an average of P products with bounded absolute terms B_0 and
unit roundoff u has a sequential-summation contribution at most
gamma_{P-1} B_0, where gamma_n=nu/(1-nu) for nu<1, in addition to product and
division residuals. This inequality follows by expanding the product of the
individual factors (1+delta_j), |delta_j|<=u. All operand bounds are furnished
by the tube envelopes. Certified tanh and square-root evaluations, triangular
solves, input rounding, and a specified coupling error for generated Gaussian
primitives must be included. This gives an effective sufficient precision
choice; a precision label or a covariance reconstruction diagnostic alone
does not establish these residual bounds. The stochastic statement models
the primitive draws as independent; a saved pseudorandom seed specifies a
realization, not an independent proof of that probabilistic model.

Passive queries require a separate last step because their clean conditional
covariance can be singular. For a finite query tuple, the covariance is

    S = Gram(h_queries) - cross^T K_train^{-1} cross,       (21)

with no added s^2 on its query diagonal. It is positive semidefinite: the
block matrix with K_train=Gram(H_train)+s^2I and clean query block is a Gram
matrix plus a positive semidefinite matrix supported on the training block.
Taking its Schur complement proves the assertion. Matrix inversion here has
the fixed floor s^2 and is Lipschitz with constant s^{-4} in operator norm.
Thus the same coupling controls the conditional mean, shift and covariance
entries of any fixed query tuple.

For a scalar variance, |sqrt(x)-sqrt(y)| <= sqrt(|x-y|) for x,y >= 0.
For a q-dimensional covariance the principal square root has an explicit
finite-dimensional modulus

    ||sqrt(A)-sqrt(B)||_F <= 2 q^{1/4} sqrt(||A-B||_F).      (22)

One proof adds epsilon I. If S=sqrt(A+epsilon I) and
T=sqrt(B+epsilon I), then S(S-T)+(S-T)T=A-B. Diagonalizing S on the left and
T on the right bounds ||S-T||_F by ||A-B||_F/(2sqrt(epsilon)). The two changes
from adding epsilon I each cost at most sqrt(q epsilon). Optimize epsilon
in their sum to obtain (22); equality A=B is immediate. Consequently joint
query draws coupled by the same fresh standard Gaussian vector have an
error tending to zero, generally with a square-root modulus. Appending those
primitives extends (13) by their fixed number. A marginal finite-order
Gauss--Hermite prediction has the same continuity bound, by |phi'|<=1 and
the finite weighted sum of absolute quadrature nodes. Its limit is the same
specified finite quadrature in the deterministic comparison program;
quadrature bias relative to the exact Gaussian integral is an additional error.

At time zero an initial/current repeated query has exactly the duplicated
clean Gram, so its two clean Gaussian coordinates can and must agree. Adding
independent s-noise to these passive coordinates would change this target.
The specification's clean query block avoids that error. Singular passive
covariances need the modulus (22), not an invented positive Cholesky floor.

## 8. What this does and does not close

The conclusion is a fixed-graph, fixed-s consistency theorem with a fully
specified recipe for sample and arithmetic bounds. Coefficients are computed
by the solver from its permitted empirical state. The deterministic program
is used only for analysis; the solver is not supplied its trajectory or its
expectations. The persistent generated populations are handled by (11), and
the retained history is part of the approximation state.

This argument does not supply uniform constants under mesh refinement:

1. The number of feedback instructions and the joint tuple dimension grow
   with J. The polynomial degree and coefficients in (8), the moment sum V_*,
   and the quantization cost in (17) grow with that graph.
2. The Cholesky estimate has an explicit s^{-2} factor, and passive covariance
   inversion has s^{-4}. Sending s to zero in these bounds is not justified.
3. The maximum-norm tangent envelopes contain omega_p^{-1/2}. Bound (2) removes
   this dependence for a frozen contracted estimator under source-density
   bounds, but it does not remove it from adaptive error propagation (8).
4. A mesh-uniform derivative cap and a mesh-uniform stability estimate for
   the generated empirical process have not been proved here. A source cap
   for a particular deterministic reference cannot simply be assigned to its
   noisy or empirical perturbations.
5. Time discretization, finite-law approximation when the data law changes,
   source-noise bias, passive quadrature bias, and sampling/precision errors
   are distinct. Controlling the last two at one graph controls none of the
   others automatically.

There is a useful quantifier distinction. Given any sequence of fixed graphs
and positive s values, this theorem supplies, graph by graph, a computable
P and precision making the empirical solver close to its corresponding noisy
finite source program. Thus an arbitrarily expensive diagonal choice is
available for this bridge alone. Identification and a useful resource bound
for a simultaneous physical limit require estimates for the deterministic
discretization and noise errors as well. No polynomial resource law in J,
inverse accuracy or inverse s is proved.

The highest-leverage remaining bridge is a weighted, contracted adaptive
stability bound whose amplification depends on physical T and controlled
source-density norms, rather than on the number of retained instructions or
the largest directional probe. Equation (2) supplies a suitable frozen error
source. Equation (11) shows exactly where its propagation must be established.
