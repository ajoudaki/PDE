# Revised C-H3: persistent Gaussian clouds and an enriched H2 dictionary

Candidate frozen on 2026-09-13 before receiving or discussing any other route.
Author: scoped route agent `h3v2_route_gaussian`. Status: a candidate construction
and convergence argument, not independently checked or promoted. No trajectory
experiment, implementation change, or Git write was performed.

The useful construction is a causal Monte Carlo compiler with persistent sample
clouds, a strictly positive auxiliary source covariance ridge, and complete
same-population joint sampling. It avoids tensor Gaussian quadrature. Source
regularization is removed after the sample limit, at each fixed dictionary order.
Three small explicit dictionaries have strictly increasing spans on both
populations. Subsequent orders have a dense, linearly growing dictionary schedule.
The runtime dynamics are the nonlinear H2 particle equations, with a single
stored matrix and its transpose. No Gaussian-program invocation occurs during
training.

## Scope and source record

Scientific inputs read completely within the assignment:

- `docs/global_nonlinear.md`, C.4.7.8 and C.4.7.9, lines 11441–12554;
- `docs/NOTATION.md`;
- `code/pde/observable_closure.py` and `code/tests/test_observable_closure.py`.

Process inputs: root `AGENTS.md`, `RESEARCH_WORKFLOW.md`, both required skills
`/etc/codex/skills/{solve-math-rigorously,investigate-conjectures}/SKILL.md`, and
the latter skill's research-contract, adversarial-audit, and proof-search
references. No study README/history, other route, or other study was read.
The allowed sections' established H6 Gaussian law and H2 convergence conclusions
are dependencies; their external proof bodies were outside this scoped input.
The supervisor must check those dependencies before accepting the candidate.

Input HEAD was `c45e04d4efd0ff52e1c2f32b633fb9e8682157bd`. SHA-256:

| Input | SHA-256 |
| --- | --- |
| AGENTS.md | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| RESEARCH_WORKFLOW.md | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| docs/NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| docs/global_nonlinear.md | `947eb52f10a8ebcd4970fa2acb1d26cba25dc5d73e8839893d5d2f4e3f688161` |
| code/pde/observable_closure.py | `f8dc5d16e5de1737444c44aae737ee1c9b4d664188d72f59acd0bb92f457c137` |
| code/tests/test_observable_closure.py | `ecc60bfd7eec882c8ae05140d756f6ec8cf90909b6317aab2c126b3c27439635` |

The contract is exactly H1–H3 and C.4.7.9: two hidden tanh layers, normalized
circle inputs, bounded labels, Gaussian stored variances `(1,1/n,1/n^2)`, block
mobilities `(n,1,n)`, unhalved mean-square physical GF, limiting readout zero,
`T=1/200`, and every separately fixed law in the fixed ball `U_rho` there.
Both nonorthogonal and nonatomic laws remain included. The errors are
uniform-time whole-circle prediction errors and Euclidean W2 errors of every
separately fixed finite admissible same-population observation tuple. There is
no width parameter in any numerical array dimension below.

## 1. Three practical dictionaries and a dense continuation

All fields in this section are frozen initialized words. Set

```
u1=(1,0), u2=(0,1), u3=(3/5,4/5),
ha=tanh(g·ua), za=A0 ha, sa=tanh(za), pa=A0* sa,
d12=s1(1-s2^2), d21=s2(1-s1^2),
p12=A0* d12, p21=A0* d21,
v12=(1-h2^2) T2(p12), v21=(1-h1^2) T2(p21),
T2(v)=2 tanh(v/2).
```

The following lists are cumulative; every listed product has bounded operands.
Use shared DAG nodes and exact rational coefficients, not expanded expression
trees. There is no data-dependent choice or target trajectory in the lists.

| Order | Population-1 additions | Population-2 additions | `(d1,d2)` |
| --- | --- | --- | --- |
| 1 | `1,h1,h2,tanh(p1),tanh(p2)` | `1,s1,s2` | `(5,3)` |
| 2 | `h3,tanh(p3),tanh(p12),tanh(p21)` | `s3,d12,d21` | `(9,6)` |
| 3 | `v12,v21,sin(g1+g2),cos(g1+g2)` | `tanh(A0 v12),tanh(A0 v21),s1*s2,sin(z1+z2),cos(z1+z2)` | `(13,11)` |

The dictionary programs alone require respectively 4, 8, and 10 distinct action
calls. Adding both terminal contraction lists `A0 psi1` and `A0* psi2`, with
identical action words memoized, requires respectively 8, 15, and 24 distinct
named sources. Population dimensions and action dimensions are independent.
The runtime matrices have 15, 54, and 143 entries. These counts concern these
specific dictionaries, before any later dense-enumeration additions.

For orders `j>=4`, retain the preceding lists and add:

1. `sin(j g1),cos(j g1)` on population 1, and `sin(j z1),cos(j z1)` on population 2;
2. `tanh(A0 psi1,i)` and `tanh(A0* psi2,k)`, where the deterministic indices are
   `i=1+((j-4) mod d1(j-1))`, `k=1+((j-4) mod d2(j-1))`;
3. all bounded valid outputs among grammar codes `0,...,j` of H2 part 2.

Suppress only identical symbolic words, never a numerically small Gram mode.
The grammar's unbounded dependencies remain initialization DAG nodes even when
not retained features. At order 4 the only possible new bounded prefix word
not already a constant is code 4. Thereafter at most one new code is introduced
per order. Thus `d1(j)+d2(j)<=24+7(j-3)` for `j>=3`. Shared DAG size and named
source count, including contraction calls, are `O(j)`. Scanning the stated
finite grammar prefix has its explicit finite cost; no rank test is used.

Let `psi_l,j` denote the resulting raw feature column. Use the same ridge rule
as H2, `eta_j=2^(-j)` and

```
G_l,j=E_l[psi_l,j psi_l,j^T],
b_l,j=(G_l,j+eta_j I)^(-1/2) psi_l,j.
```

Every H2 bounded rational word eventually belongs to a retained list. The
bounded Fourier-cylinder density proof in the supplied H1 section and the H2
ridge-filter argument therefore apply without change. In particular the raw
spans are nested, the filters are contractions converging strongly to identity,
and both filtered action orientations converge strongly. H2's error-production
and one-reference-tail comparison then prove canonical convergence for these
new dictionaries. No assumption that their normalized coordinates are nested
is made.

### The first three orders really increase both spans

At order 1, `z1,z2` are independent nondegenerate centered Gaussians, because
`h1,h2` are independent centered nonzero functions of the independent seeds.
The reverse source vector in `(p1,p2)` has positive definite covariance and is
independent of `g`; its deterministic response shifts depend on `g`. A linear
combination of `tanh(p1),tanh(p2)` that is a function of `g` alone must have both
coefficients zero: condition on `g`, use the Gaussian density on all of R2,
and vary one source coordinate at a time.

Consequently `h3` could belong to the first lower span only if it belonged to
`span(1,h1,h2)`. All mixed partial derivatives of the latter functions vanish;
the mixed derivative of `tanh(3g1/5+4g2/5)` does not vanish identically. Almost
sure equality would be equality everywhere by continuity and positive Gaussian
density. Thus `h3` is new. It also does not belong to `span(h1,h2)`, so the
Gaussian covariance of `(z1,z2,z3)` is positive definite. Conditional on
`z1,z2`, `z3` has positive variance, making `s3` new in the upper span.

For the next step, the five reverse operands
`s1,s2,s3,s1(1-s2^2),s2(1-s1^2)` are linearly independent. The vector
`(s1,s2,s3)` has density with full support on `(-1,1)^3`; a linear relation is
a polynomial identity there. Its coefficients of `s1*s2^2`, `s2*s1^2`, `s3`,
`s1`, and `s2` all vanish. Hence their reverse Gaussian covariance is positive
definite. Conditioning on `g` and varying each reverse source again shows that
a deterministic function in the lower order-2 span must be in
`span(1,h1,h2,h3)`. On the line `g2=-3g1/4`, every function in that span has a
limit as `g1` tends to positive infinity; `sin(g1+g2)=sin(g1/4)` has no limit.
Thus the lower order-3 span increases.

Every function in the upper order-2 span has a limit on the line
`z1=z2=t,z3=0` as `t` tends to positive infinity, whereas `sin(z1+z2)` does not.
Full Gaussian support and continuity again convert a hypothetical almost-sure
linear relation into an everywhere relation. The upper order-3 span increases.
This proves enrichment; it does not claim monotone prediction error improvement.

## 2. Why an auxiliary source ridge is useful

The maintained prototype uses tensor Hermite rules. It extends a previously
stored covariance using new empirical cross moments, and refreshes the tensor
cloud as independent source dimension increases. Its present tests cover
particular small programs, exact singular examples, and static equations.
They do not prove consistency for arbitrary growing joint programs. In a
general numerical integrator, recomputing old operands on a changed cloud while
retaining their old covariance entries need not produce a positive Gram
extension. Independently estimating the two orientations has the same problem.

The proposed compiler uses two fixed, persistent Gaussian sample banks and a
strictly positive source variance parameter `gamma=2^(-q)`, separate from the
feature ridge `eta_j`. All moments belonging to a source covariance extension
use the same input cloud, whose previously computed operand values never
change. Consequently every finite-sample covariance matrix is a Gram matrix
plus `gamma I`, exactly in real arithmetic.

The auxiliary gamma program is an approximation to H6, not a new assertion
about the initialized neural action. At gamma greater than zero, distinct
linearly dependent query words may acquire separate artificial innovations;
it would be false to call that program the exact Gaussian action. This
perturbation is removed before taking dictionary order to infinity. At every
numerical order the compressed runtime action and its reverse are already one
matrix and its actual weighted adjoint. These two assertions are distinct.

## 3. Exact gamma program and its singular limit

Fix the entire finite union of dictionary and both contraction programs before
initialization, and choose a deterministic topological order. Keep all named
source slots, including zero and dependent operands. Identical action words are
shared DAG nodes. Define the exact gamma program by the supplied H6 responses

```
A0,gamma b = xi_b + sum_earlier_reverse d_k E1[partial_zeta_k b],
A0,gamma* d = zeta_d + sum_earlier_forward b_i E2[partial_xi_i d],
```

and by the source covariances

```
Cov(xi_bi,xi_bk)=E1[bi bk]+gamma*1_(i=k),
Cov(zeta_di,zeta_dk)=E2[di dk]+gamma*1_(i=k).
```

The two Gaussian source groups and `g` are independent. Expectations and named
derivatives freeze all previously selected deterministic coefficients and
covariances. A derivative is with respect to a formal named source coordinate,
not with respect to an innovation or a covariance factor. Additional future
source coordinates have zero derivative in old expressions.

Every new source covariance is a principal extension of its predecessor. It
is the Gram of the full old/new operand vector plus gamma identity and is
positive definite. Cholesky extension therefore defines the law causally.
For gamma zero the supplied H6 pseudoinverse construction defines the law,
including singular cases.

**Finite-program continuity claim.** As gamma decreases to zero, the joint laws
of all finite outputs and the required response coefficients, raw Grams, and
both directional contractions converge to the canonical H6 quantities. Output
convergence is in W2 for all L nodes; bounded-output products and all required
named derivatives converge in expectation.

Proof: induct on the ordered action calls. Finite output expressions are
functions of their population's named Gaussian source vector, `g` when
applicable, and previously fixed coefficients. In a compact neighborhood of
the coefficients, these functions have a common finite polynomial envelope in
the Gaussian coordinates. The same holds for their named derivatives.
For action outputs this follows from a Gaussian source plus finitely many
bounded operand terms; for elementary gates it follows from bounded derivatives;
for bounded products use their syntax envelopes and the product rule. Thus
the new Gram and response entries are continuous functions of the preceding
coefficients and Gaussian covariance matrices.

For clarity, covariance continuity remains valid at singular matrices. For
positive semidefinite finite matrices `C_m -> C`, their positive square roots
converge. One elementary justification is uniform polynomial approximation of
the continuous function `sqrt(x)` on a bounded interval containing all spectra;
matrix polynomial evaluation is continuous, and the spectral theorem bounds
the polynomial approximation error in operator norm. Couple Gaussian vectors
as `C_m^(1/2) G` and `C^(1/2) G` using one finite standard Gaussian vector.
They converge pointwise with an integrable common bound for every fixed
polynomial moment. Dominated convergence therefore proves all the expectations
just listed. At the next source call the newly enlarged full covariance matrix
has convergent entries and is positive semidefinite, so the induction continues.
The scalar coefficient lists converge as well. The final same-source coupling
gives output L2 convergence, hence W2 convergence of each complete tuple.

This argument never takes a limit of inverse matrices or triangular factors
at a singular covariance. Singular named coordinates remain present in the
expressions and derivative rules. Duplicated and identically zero operands are
covered. Strictly positive gamma is used only for the finite-sample compiler;
the convergence proof at zero uses square-root continuity of full laws.

## 4. Persistent-cloud compiler

For fixed order j and gamma greater than zero, preallocate independent standard
normal clouds of sizes `P1,P2`. Population 1 has two seed columns and as many
innovation columns as the program has reverse calls; population 2 has one
innovation column per forward call. Future columns are unused until their call.
Keep all rows and all previous output values unchanged when adding a source.

At a new forward call with input b, let `V` be the P1-by-k array of all old
forward operand values and let `v` be b evaluated on that same cloud. Use

```
C = V^T V/P1 + gamma I,
a = V^T v/P1,
s = v^T v/P1 + gamma.
```

The old covariance C is already this matrix: all old operand arrays are
persistent. If its Cholesky factor is L, append the row obtained from
`ell=L^(-1) a`, with innovation standard deviation
`sqrt(s-ell^T ell)`. The Schur complement is at least gamma. For example the
quadratic form of the enlarged Gram plus gamma identity at
`(-C^(-1)a,1)` is at least gamma, and equals that Schur complement. Multiply
the new row by this population's stored independent-normal columns. Add the
H6 response, replacing every expectation by the empirical average of the
named-source derivative on the persistent input cloud. Reverse calls use the
identical rule with populations exchanged.

Named derivatives can be computed by reverse AD on the existing scalar DAG.
Treat each named source as a separate leaf, seed the input operand's batched
outputs with weights `1/P_l`, and sum each source-leaf adjoint. Propagate through
the frozen response links of action outputs. Do not differentiate Cholesky
factors, empirical covariance formation, or coefficient estimation. This
computes precisely the required empirical frozen-source partials.

There is no independence claim for output particles at finite P: empirical
coefficients depend on both clouds. The exact gamma program has deterministic
coefficients, and its two Gaussian groups are independent. The following
induction handles the finite-P feedback explicitly.

**Consistency at fixed gamma.** Use fixed infinite independent normal arrays
and their first P_l rows. For every fixed finite union, all empirical
coefficients converge almost surely to the exact gamma coefficients. The full
empirical output laws converge in W2, and the output product averages used
below converge.

Proof: at the first call this is the strong law of large numbers, in the form
that averages of iid integrable real variables converge almost surely to their
expectation. At a later call assume the finite preceding coefficient/factor
list converges. Cholesky is continuous on positive definite matrices; here
every matrix has lower spectral bound gamma, so the new factor also converges.
On a compact neighborhood of the limiting coefficient list, each finite
expression and required derivative is locally Lipschitz in that list with a
finite polynomial envelope in the independent normal row. Split an empirical
average into its random-coefficient/fixed-coefficient difference and the
fixed-coefficient average. The first is bounded by the coefficient error times
the empirical envelope average, which stays bounded by the strong law; the
second converges by that law. Normal polynomial moments are finite because
`integral |x|^k exp(-x^2/2) dx` is finite for each fixed k. This proves the next
Gram and response entries and completes the finite induction.

Apply the same argument to squared output differences under the shared normal
rows. Their empirical average tends to zero. The iid ideal output empirical
measure converges in W2: truncate outside a large ball using the integrable
second moment; partition the ball into finitely many cells of small diameter;
the strong law gives each cell mass convergence; couple cell masses and then
remove the truncation and partition. The triangle inequality gives the claimed
W2 convergence for the actual interacting output cloud. All joint coordinates
use the same rows in this argument.

Increasing gamma precision or sample size means rerunning the complete finite
union from its frozen specification. Do not patch one source coefficient into
an old downstream program. The finite-P exact Gram identity above depends on
persistence within a run.

## 5. Normalization, both contractions, and finite-state initialization

After the entire union is compiled, evaluate raw feature arrays `Psi1,Psi2`
and all terminal action output arrays on the final clouds. Use uniform
probabilities, or the same positive probability weights everywhere if a
weighted integrator is substituted. Define

```
Ghat_l=Psi_l^T Psi_l/P_l,
Rhat_l=(Ghat_l+eta_j I)^(-1/2),
B_l=Psi_l Rhat_l,
Cplus=Psi2^T [A0,gamma Psi1]/P2,
Cminus=[A0,gamma* Psi2]^T Psi1/P1,
Dpre=Rhat2 (Cplus+Cminus)/2 Rhat1,
Dhat=clip_op_2(Dpre).
```

Here both `Cplus,Cminus` have shape d2-by-d1. The arrays on each side of every
product are joint evaluations on the same population cloud. `clip_op_2` changes
each singular value s to `min(s,2)`; it is a continuous finite-matrix operation.
It is not a truncation of dictionary modes. Use `M=Dhat`, `w=g`, and `c=0`.
The saved D is Dhat. The transpose, not a separately estimated reverse matrix,
is used for every subsequent reverse contraction.

At finite P and gamma the two raw contraction estimates need not agree;
averaging makes the initializer symmetric between the orientations. This is
not an assertion of exact empirical Gaussian adjunction. For fixed j, first
P tends to infinity and then gamma to zero. Sections 3–4 imply convergence of
both contractions to the same canonical value by actual H6 adjunction. Ridge
normalization is continuous because eta_j is positive. At the canonical limit
`||D_j||op<=2`, so the clipping does not alter that limit. Thus

```
(joint mark laws, Dhat) -> (lambda_1,j,lambda_2,j,D_j)
```

in the required W2/finite-matrix senses, with P before gamma removal. Repeated
or zero dictionary columns need no exception. For every finite run,

```
B_l^T B_l/P_l = Ghat_l(Ghat_l+eta_j I)^(-1) <= I,
||Dhat||op<=2.
```

These are exact-real algebraic properties, useful for uniform numerical-model
energy bounds. They do not certify floating-point evaluation error. Every
normalized feature is bounded by the raw syntax envelopes times eta_j^(-1/2),
uniformly over clouds and gamma at the fixed order. All static/current
coordinates remain in one joint row; initialization does not resample g or an
individual feature column independently.

## 6. Actual finite-particle equations

Let training nodes be `(u_a,y_a)` with nonnegative weights `omega_a` summing to
one, with `|u_a|=1`, `|y_a|<=Y`. This can be any atomic approximation to an
admitted law; it need not have orthogonal inputs. At every current state use

```
h1_ia=tanh(w_i·u_a),
a_a=P1^(-1) sum_i b1_i h1_ia,
z2_ka=b2_k^T M a_a, h2_ka=tanh(z2_ka),
d_a=P2^(-1) sum_k b2_k c_k (1-h2_ka^2),
q_ia=b1_i^T M^T d_a,
f_a=P2^(-1) sum_k c_k h2_ka, r_a=f_a-y_a,
w_i'=-2 sum_a omega_a r_a (1-h1_ia^2) q_ia u_a,
c_k'=-2 sum_a omega_a r_a h2_ka,
M'=-2 sum_a omega_a r_a d_a a_a^T.
```

The equations are exactly the H2 characteristic equations for empirical mark
populations. They use the current nonlinear features and both updated action
directions. No initialized source derivative is a temporal derivative.

The weighted adjunction identity is exact for every finite state:

```
(1/P2) sum_k u_k [b2_k^T M (sum_i b1_i v_i/P1)]
 = (1/P1) sum_i v_i [b1_i^T M^T (sum_k b2_k u_k/P2)].
```

The finite loss has the exact energy identity

```
L'=-sum_i |w_i'|^2/P1-sum_k |c_k'|^2/P2-||M'||F^2.
```

Differentiate the displayed f with respect to each moving coordinate; the
derivative with respect to a particle w or c carries its population probability,
which cancels in the characteristic velocity under the weighted population
metric. The M derivative is `d_a a_a^T`. This derives every sign, weight and
factor of two in the identity. Since initially `L<=Y^2`, the exact finite ODE
has the H2 bounds `||c||infty<=2Yt`, `||M-Dhat||F<=2Y^2 t^2` and
`||M||op<=2+2Y^2 t^2`. Its bounded feature envelopes and these bounds prevent
finite-time escape of w. The local Picard argument in supplied H2 part 4
therefore gives a unique global characteristic solution.

For a finite solver, use simultaneous explicit Euler steps with
`h_k=T/2^k`, and linearly interpolate moving coordinates. Recompute all gates,
predictions, and contractions after each step. At fixed finite arrays, the
ODE field is smooth and is Lipschitz on a compact neighborhood of its bounded
trajectory. The exact trajectory has uniformly continuous velocity there.
The one-step consistency error is at most h times that velocity's modulus of
continuity; telescoping the Lipschitz error recursion gives uniform convergence
as h tends to zero. A first-exit argument keeps sufficiently fine Euler paths
inside that neighborhood. No discrete energy inequality or claimed coarse-step
stability is needed. This is population-closure integration, not finite-neural
GD or a width/GD interchange.

The saved numerical state consists of the two complete weighted joint clouds,
their g and b marks, current w,c, M and Dhat, plus the fixed data representation.
It contains no source program at runtime, historical trajectory, elapsed-time
forcing, P2-by-P1 middle array, or reference prediction. An Euler restart needs
its current state and chosen future step sizes. A same-step partition restart
has exactly the same algebraic continuation in exact arithmetic.

## 7. Fixed-order particle and data-law convergence

The following stability argument bridges empirical initialization to the H2
population equations; iid particles after compilation are not assumed.

Fix j. Normalized marks have a common finite supremum bound because eta_j is
positive. Couple two initial joint mark laws in W2, retaining their g-b
correlation, and carry each coupled pair under its own characteristic flow.
Let e be the sum of the L2 differences of w,c and the Frobenius difference
of M. The frozen mark coupling error is e_b, with seed error included at t=0.
On the common finite-horizon energy ball, subtract the displayed field formulas.
For example

```
|a-a_tilde| <= C(e_b+||w-w_tilde||2),
||z2-z2_tilde||2 <= C(e_b+e),
||d-d_tilde|| <= C(e_b+e),
||q-q_tilde||2 <= C(e_b+e).
```

The first uses the bounded b envelope and the 1-Lipschitz tanh gate. The second
subtracts b2, M and a successively. The third additionally uses bounded c and
the Lipschitz upper gate. The fourth subtracts b1, M and d. Unlike the
order-removal comparison, q is pointwise bounded by the fixed feature envelope
times `||M|| ||d||`; the changed lower gate therefore gives an ordinary L2
Lipschitz bound. Subtract residuals and integrate to get
`e'<=C_j(e+e_b)` with initial matrix error included in e(0). Integration gives
uniform convergence whenever the initial joint laws and matrix converge.

For changing data laws, the same proof has an added term `C_j W1(mu,mu_tilde)`.
Indeed every velocity integrand is Lipschitz as an L2-valued function of
`(u,y)`: `||tanh(w·u)-tanh(w·v)||2<=||w||2 |u-v|`; the preceding bounded-mark
subtractions propagate this estimate to a,z2,d,q and the velocities, and labels
enter affinely in residuals. The row L2 norms have a common bound when the
coupled g laws converge in W2. Integrate against a coupling of the two data laws
and take its infimum. This verifies continuity for nonatomic law approximation,
without requiring atomic approximations to lie in U_rho themselves.

For an arbitrary Borel law, the input interface is a supplied sequence of
positive atomic laws converging in W1, as permitted in H1. Compact partitions
with exact cell masses establish existence. This is not a claim that an
unspecified Borel-law oracle supports computable cell masses or useful rates.
For a concrete density or sampling interface, an implemented approximation must
state which interface it uses. No numeric certificate or tolerance selector is
required here.

Finite observation graphs are handled by the same couplings. Frozen upper
seeds use Dhat and the frozen joint cloud. Each action uses the factorized
kernel b2^T M b1 and its transpose. Affine and Lipschitz unary nodes propagate
L2 convergence; bounded products use their uniform syntax envelopes; action
contractions use bounded marks and the matrix convergence. Thus every fixed
same-population tuple converges in W2, including initial/current joints,
quadratic pairings, and nested actions. The hidden and prediction maps are
uniformly continuous in u with the same bounded coefficient and row L2
estimates, giving the whole-circle claim.

## 8. Precise limit order and finite precision

Let p be arithmetic precision, k the Euler refinement, P the two-cloud sample
refinement, m the positive data-law approximation index, q the source-ridge
refinement (`gamma_q=2^(-q)`), and j the dictionary order. For every fixed law
in U_rho and every fixed declared finite observation collection, the candidate
claim is

```
lim_j lim_q lim_m lim_P lim_k lim_p
  [ uniform-time prediction error + declared joint W2 errors ] = 0.
```

The order is read from right to left. At fixed finite j,q,m,P,k, refine
arithmetic; then refine time; then the clouds; then the data law; then remove
the source ridge; finally increase the dictionary. Counts P1,P2 both tend to
infinity. Other interleavings need their own argument. With fixed infinite
normal banks the sample assertions hold almost surely on the countable
intersection over j,q,m; convergence in probability is available if fresh
clouds are used instead.

At fixed gamma and eta all source and ridge matrix operations are positive
definite. In exact arithmetic every new Schur complement is at least gamma.
Increasing-precision elementary arithmetic, Cholesky, positive inverse square
roots, and continuous singular-value clipping therefore converge without
deciding whether a true canonical eigenvalue is zero. Gaussian rows can be
generated from independent uniform bit streams by convergent inverse-normal
evaluation; almost surely no sampled uniform is an endpoint. Refining p uses
the same streams, so it approximates fixed samples, rather than changing the
probabilistic input at every precision.

This establishes a route to arbitrary-accuracy refinement with explicit
separate indices. It does not give an error rate, a stopping certificate, a
tolerance-to-resources map, or convergence along the diagonal `p=k=P=m=q=j`.
None of the proof's target-dependent errors or continuity constants is an
input to initialization or evolution.

## 9. Counts and an implementation boundary

Let L be the number of ordinary program nodes and S the number of named action
calls in the full union. Let E count ordinary DAG edges plus frozen-response
links; `E=O(L+S^2)`. Let `P=P1+P2`, d=d1+d2, and let m now denote the number
of data atoms in a fixed numerical law.

- The source compiler uses `O(P S E + S^3)` scalar operations with one reverse
  AD pass per new source and dense Cholesky extensions. This conservative bound
  allows response links to be dense. Cached operand products cost at most
  `O(P S^2)` and fit that bound. It uses `O(P(L+S)+S^2)` memory with batched
  reverse adjoints, discarding each derivative pass after its coefficient
  averages. A full P-by-L-by-S Jacobian is unnecessary.
- Final feature Grams and both contractions cost
  `O(P(d1^2+d2^2+d1*d2)+d^3)` operations, including normalization and clipping.
  The Gaussian dimension is O(S); there is no quadrature factor of the form
  `quadrature_order^S`.
- One nonlinear RHS evaluation costs
  `O(m(P1*d1+P2*d2+d1*d2))` arithmetic operations. All three blocks move.
  With K time steps multiply by K, or by the number of stages for another
  fixed integrator.
- Saved state storage is
  `P1(d1+4)+P2(d2+1)+2*d1*d2+P1+P2+4m` real scalars, counting b,g,w,c,
  both matrices, population probabilities, and two input coordinates, label,
  and probability for each data atom. An atom-batched RHS with batch B needs
  `O(B(P1+P2+d1+d2))` additional scratch.

For the linear-growth continuation above, L,S,d are O(j), so the conservative
initialization count is `O(P j^3+j^3)`, state storage is `O(Pj+j^2+m)`, and each
RHS is `O(m(Pj+j^2))`. These are arithmetic counts, not bit complexity or
claimed accuracy costs. At p-bit precision multiply by the relevant
arithmetic/elementary-function costs. The feature ridge can force high
precision as j grows; no numerical conditioning claim is hidden.

The natural maintained-code boundary is: keep typed Word/DAG semantics and the
current finite-state/RHS/observation/restart conventions; add an explicit
enriched-dictionary selector, a persistent Monte Carlo Gaussian compiler,
source gamma distinct from feature eta, two-direction contraction assembly,
optional operator-norm clipping, and an actual simultaneous time integrator.
The current `apply_action` helper may remain a factorized operation on declared
particle arrays. It must not materialize a P2-by-P1 kernel, accept a raw neural
matrix, or serve as an external canonical action oracle.

## 10. Exact claim status and remaining work

| Claim | Candidate status / dependency |
| --- | --- |
| Three orders increase both retained spans | Argument supplied in section 1; no empirical claim |
| Dense linear-size dictionary schedule is H2-compatible | Uses supplied H1 density and H2 strong-filter/convergence proof |
| Positive-gamma persistent covariance extension is always positive definite | Exact Gram-plus-ridge argument supplied |
| Both populations and all coordinates are jointly sampled consistently | One union, persistent same-population rows; finite-P dependence handled explicitly |
| Gamma removal handles singular canonical covariance | Finite-prefix full-law square-root continuity proof supplied |
| Particle and data-law convergence at fixed order | Coupling/subtraction proof supplied; no order-uniform Lipschitz claim |
| Nonlinear finite solver converges under time and precision refinement | Fixed finite-system argument supplied; no coarse-step guarantee |
| Canonical nonlinear GF identification at j infinity | Relies on the permitted H2 theorem, whose dictionary proof extends as shown |
| Practical accuracy at the first three orders | Open; no trajectory was run |
| Implemented robust arbitrary-precision sampler, compiler, and solver | Not supplied by this route; must be implemented and tested |
| A single effective diagonal or tolerance selector | Not claimed or needed for the revised qualitative target |

The construction's main remaining scientific audit is the complete adaptive
sample-cloud induction, especially frozen named-source differentiation through
response links, and its interface with the exact H6 law. A false claim that
finite-P output rows are iid would break that proof. A false claim that gamma
positive gives the exact initialized neural action would change the model.
The artifact makes neither claim. The exact singular limit is taken after
sample convergence, never through a noisy pseudoinverse.

Useful deterministic implementation checks, without training experiments, are:
duplicated/scaled/zero operands with all named derivative slots preserved;
forward-reverse-forward programs; the analytic sine pilot from maintained
tests; nonorthogonal initial query Grams; exact persistence of old operand rows;
positive Schur complements; convergence of both contractions as gamma is
removed; weighted adjunction and all-block gradient identities; full same-row
frozen/current observation joins; and restart equality for one supplied state.
Trajectory accuracy and resource measurements would require a separately
authorized, precommitted run. This route does not infer them from the counts.
