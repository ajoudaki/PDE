# Informed internal review of the no-bad-local-minima candidate

2026-09-19. Reviewer: the scoped `cubic_order_check` route.

**Verdict: the central theorem and its proof pass this informed internal
mathematical check.** Every local minimum in the stated odd, exact-population
p=1 L2/L2/Frobenius state space has zero loss, for every finite normalized
input set with no parallel or antiparallel pair and the stated positive
weights and binary labels. I found no missing hypothesis or incorrect step
in the paired variations, stationarity cancellation, derivative-ridge
lemma, flat readout perturbation, or zero-matrix argument.

There are minor presentation/provenance changes to make before treating the
whole report as a self-contained checked result: supply or omit its final
exact-fit existence claim, clarify one straight-line quantifier, and label
this check as informed internal review rather than fresh isolated review.
None changes the no-bad-local-minima proof. A direct exact-fit proof is
included below so the existence claim can be repaired without another input.

## Scope, prior exposure, and source versions

This is **not a fresh isolated review** and does not satisfy the repository's
independent promotion-review gate. Before this assignment I authored the
same study's independent collapsed-state cubic criterion and fifth-order
counterexample. That earlier work read `four_input_noise_geometry.md` and
`sgd_geometry.md`, in addition to the established model and notation.
After freezing that route, the supervisor informed me that their separate
collapsed-state argument agreed and also addressed quartic and finite-order
descent at some collapsed states. I did not read that other argument.
The current assignment explicitly requested this informed internal check
because the fresh reviewer spawn was blocked by the agent thread limit.

Current scientific inputs are the complete 303-line frozen lead candidate
and the two complete established sources listed below. I read every line
of the candidate, including its final existence and scope statements,
and checked against the complete model and notation already read in this
context. The established-source hashes are unchanged since that complete
reading. I did not read another proof, history, study, review, or agent
finding during this review. The earlier frozen report is unchanged.

| Input | SHA-256 |
| --- | --- |
| `studies/p1_stochastic_escape_20260918/no_bad_local_minima.md` | `702ef38dbb7c03c5d09979d7247f3c9eab1b35da30f98d9159bdf948b2cdedb4` |
| `docs/observable_p1.md` | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

Shared instructions and the mathematical/research skills were applied.
The check consists of direct algebraic rederivation and adversarial analysis;
there were no simulations, experiments, symbolic-computation or numerical
tests, external scientific sources, implementation changes, or Git writes.
Only this review report was written. Commands read the complete candidate,
verified source hashes, recorded line numbers, and inspected index/path
metadata before the assigned write.

## 1. Model, carrier, and differentiation checks

The candidate uses the exact folded odd model from `docs/observable_p1.md`,
with all entries of the d-by-2d matrix free, actual transpose M^T, finite
weighted unhalved square loss, and the physical population norms. Removing
the inactive constants is valid in this state class. Using absolute w
instead of w-g gives the same local topology because translation by the
fixed L2 field g is an isometry. Arbitrary odd L2 fields are legitimate
ambient states; canonical reachability is not an additional constraint in
the theorem.

Direct differentiation gives

\[
 \delta f_i=d_i^T(\delta M)a_i+d_i^TM(\delta a_i),
\]

and therefore exactly the two derivatives in candidate equation (2).
For fixed finite M and c in L2, the map of the finitely many a_i is C2:
each differentiated upper integrand is bounded by a constant times |c|,
which is integrable. Its Hessian is locally bounded in that finite
space, giving a remainder bounded by a constant times
`sum_i ||delta a_i||^2`. No C2 or C3 assumption on the full lower L2
Nemytskii map is needed.

Both canonical feature Grams are positive definite. For the lower raw
features, conditioning on all forward Gaussians makes any nontrivial
combination with a reverse coefficient have positive conditional variance;
if all reverse coefficients vanish, independent nondegenerate forward
features give positive variance. The invertible normalization preserves
positive definiteness. The upper coordinates are independent nondegenerate
transformed Gaussians with positive density throughout their open support
cube. These arguments use exact population laws, not a possibly singular
finite sampled table.

The carrier negation is measure preserving and acts on every lower Gaussian
coordinate, so it negates the normalized features. The half-carrier
`{G_1>0}` has a disjoint reflected partner modulo a null set. For any
measurable B in that half, the distribution function
`P(B intersect {G_1<=t})` is continuous because every hyperplane
`{G_1=t}` has probability zero. Thus positive B admits arbitrarily small
positive-measure subsets even if B is otherwise irregular.

## 2. Independence and the derivative-ridge lemma

Candidate Section 2 correctly obtains input ridge independence without an
m<=d condition. Pairwise distinct unoriented unit directions make every
excluded hyperplane proper. A vector outside their finite union has
nonzero input projections with distinct squares. Comparing the first m
odd powers on that line gives an invertible Vandermonde system, since the
displayed recurrence proves every corresponding tanh coefficient nonzero.
Negative projections merely contribute a nonzero diagonal factor.

I attacked Section 3 with zero, repeated, collinear, antiparallel, and
commensurate hidden slopes. None invalidates the argument. An L2 relation
between the continuous functions must hold on the entire open support
cube: otherwise continuity gives a positive-measure region on which the
squared difference is positive. A real line with `r dot z != 0` and,
when v is nonzero, `r dot v != 0`, then gives equation (4).

Multiplying by all displayed cosh factors gives an entire identity.
Equality on a real interval makes all derivatives at zero equal, and the
entire Taylor series then agree globally. When v=0, the resulting real
identity contradicts the boundedness of the finite tanh sum. When v is
nonzero, at `t_0=i*pi/(2a)` the left side has exactly q zeros, counted
with multiplicity, whereas every right term has at least q+1. Repeated
slopes are correctly counted repeatedly in q. A zero slope contributes
the constant cosh factor one and a zero sinh term. Removing a term's own
denominator factor removes at most one zero, and summation can only
increase the vanishing order. Thus the contradiction is sound for every
allowed hidden degeneracy.

The orthogonal projection exists onto the actual finite-dimensional span
even when its list of generators has singular Gram. J and every H_i
are bounded odd functions of b_2, so `k=J-Proj_H J` is an admissible
bounded odd readout. Section 3 proves k is nonzero, not merely generically
nonzero.

## 3. Paired variations and matrix cancellation

The step from Hilbert local minimality to pointwise global minimization
is valid because large finite changes on sufficiently small carrier sets
have arbitrarily small L2 norm. It is not a conclusion from ordinary
pointwise first derivatives alone.

Failure of pointwise minimization is detected by a countable union over
rational trial vectors, positive rational margins, and integer bounds
on |w|. This yields one fixed trial s, fixed positive margin delta,
and a positive-measure set B where w is bounded. If failure occurs on
the opposite half-carrier, the identity

\[
                 F_{-\omega}(-s)=F_\omega(s)
\]

reflects it to the designated half. Replacing w by s on E and by -s
on -E preserves oddness. Both feature and tanh differences negate on
reflection, making their product even; hence the exact factor two in
delta a_i. The physical squared displacement is at most
`2 P(E)(|s|+R)^2`, while each moment change is O(P(E)).
The finite-moment Taylor remainder is therefore O(P(E)^2), and the
linear change is at most `-4 delta P(E)`. This proves the contradiction
for sufficiently small positive P(E).

Pointwise global minimization gives F_omega(w)<=F_omega(0)=0.
M is an unconstrained finite matrix, so local minimality gives its
ordinary matrix gradient zero. Pairing that gradient with the same M
produces equation (7) with the correct factor one half. The bounded
nonpositive random variable F_omega(w) with zero expectation is zero
almost surely. At each such mark, the odd function F_omega has global
minimum zero, forcing F_omega(s)=0 for every s. Ridge independence then
eliminates every coefficient, and the positive lower Gram converts
`b_1^T(r_i M^T d_i)=0` almost surely into `r_i M^T d_i=0`.
All quantifiers and null sets can be shared over the finite sample set.

## 4. Exactly flat readout changes for M nonzero

If one residual r_i is nonzero and M is nonzero, a lower vector q with
Mq nonzero exists regardless of the rank of M. Section 3 supplies an
odd k orthogonal to every current H_j but with

\[
 E_2[k(b_2^TMq)\phi'(b_2^Tv_i)]=\|k\|_2^2>0.
\]

Readout linearity means c+t k preserves every prediction for every t,
not just to first order. A same-loss point within half the local-minimum
radius inherits local minimality on the half-radius ball, by the triangle
inequality. Applying the Section 4 lemma there and at the original point
and subtracting is therefore legitimate. The unchanged nonzero residual
can be divided out. Pairing the resulting vector identity with q gives
zero equal to the strictly positive displayed square norm, a contradiction.
This argument remains valid if all current effective vectors or features
coincide, vanish, or are antiparallel.

## 5. Zero-matrix case

At M=0, all predictions are zero independently of w and c; hence every
odd change of those fields is exactly loss preserving. A small feature
perturbation of c can make `v_c=E_2[b_2c]` nonzero because the upper
Gram is positive definite. This is possible arbitrarily close to the
original c, including when v_c initially vanishes.

The function `Q(s)=sum_i mu_i y_i tanh(s dot u_i)` is nonzero by
input ridge independence and positivity of the weights. If A_y initially
vanishes, the proposed countable-selection argument finds a fixed trial
s and component of `b_1[Q(s)-Q(w)]` with one sign bounded away from
zero on a positive-measure set where w is bounded. Otherwise a common
full-measure set would satisfy that vector identity for every rational
s, hence every real s. Since b_1 is nonzero almost surely, Q would be
constant, contradicting its oddness and nonzero character. A paired
replacement on an arbitrarily small subset then makes that component
of A_y nonzero with arbitrarily small L2 displacement.

The w and c adjustments are independent and retain M=0, so they can
both be made within any prescribed smaller neighborhood. Finally
`N=v_c A_y^T` has loss derivative

\[
                 \langle-2v_c A_y^T,N\rangle_F
                   =-2|v_c|^2|A_y|^2<0.
\]

A sufficiently small positive matrix step lowers loss while staying in
the original neighborhood. Thus no M=0 state is a local minimum.
Together with Section 4 of this review, this completes the theorem check.

## 6. Minor corrections and exact-fit completion

1. **Candidate lines 300--301: support or omit the separate existence claim.**
   The allowed packet does not contain the other study proof referenced
   there. This is a self-containment issue in a secondary statement, not
   a gap in the theorem that local minima must have zero loss. It can
   be repaired directly as follows.

   Choose r as in candidate Section 2, so the nonzero t_i=r dot u_i
   have distinct squares. Let e=sign(G_1), let q select the first
   normalized lower forward feature, and put
   `A=E_1[b_1e]`, `kappa=q^T A>0`. Choose w=e r and
   `M=e_1 q^T`. Then `Ma_i=z_i e_1` with
   `z_i=kappa tanh(t_i)`, which are nonzero with distinct squares.
   Write B=b_{2,1}. The functions `psi_i(B)=tanh(z_i B)` have positive
   definite Gram by positive density and the same Taylor/Vandermonde
   argument as candidate Section 2. If that Gram is Q, the bounded odd
   readout `c=sum_i (Q^{-1}y)_i psi_i` gives `f_j=y_j` exactly.
   This proves the existence assertion for the theorem's entire input
   class, using only the allowed canonical carrier and odd fields.

2. **Candidate lines 48--49: clarify the direction quantifier.** Replace
   “condition about the leading coefficient on every line” by
   “existence, at each bad equilibrium, of a fixed straight direction
   with a negative leading Taylor coefficient.” The beginning of the
   paragraph states this correctly. The polynomial example is valid:
   every line through the origin either increases to leading order or
   is flat, while s=t^2 decreases. It supplies a logical distinction,
   not a p=1 counterexample to straight-line escape.

3. **Candidate line 303: record the actual review status.** This completed
   check is informed internal review. It must not be relabeled as the
   fresh isolated review that could not be started, or used to satisfy
   the independent promotion-review requirements.

## Limits and completion

The positive-loss local-minimum exclusion is exact in the stated ambient
nonatomic odd population state space, and the above check found no
mathematical correction required for that theorem. It depends essentially
on available paired sets of arbitrarily small probability, the freedom
of the whole matrix block, and unrestricted odd L2 readout perturbations.
It is not established here for fixed finite populations, finite-width
networks, restricted parameterizations, or an L-infinity topology.

The proof does not imply a fixed straight-line descent expansion at every
bad equilibrium, any basin probability, canonical reachability, SGD
excitation, boundedness, or eventual fitting. In particular, concentration
of a perturbation onto smaller and smaller carrier sets need not produce
one fixed Taylor direction. All of these limitations agree with the
candidate's principal scope statements.

Review coverage is complete for the frozen candidate and stated model
dependencies. The original candidate was not changed during this review;
the earlier independent report remains frozen. The theorem can be recorded
as internally checked by this informed review, with the separate provenance
and presentation corrections above retained. No promotion status follows.

## Supplement 1: real labels and the exact floor for conflicting data

2026-09-19. This is an informed follow-up check requested by the supervisor,
with the same prior-exposure disclosure and limits as the original review.
The original review prefix, frozen at SHA-256
`9f1796c95b2fab5a80d74df046ec4312fe394f628dfa64cd856f6511629c453c`,
is preserved. The new scientific input is the supervisor's explicitly
stated extension and grouping identity; no other source was read. This
supplement checks those statements, not a revised lead document. The two
established source hashes remain unchanged. No experiments were performed.

**Verdict: both extensions are correct without additional structural
hypotheses.** Retain d>=2, finitely many nonzero inputs on
`sqrt(d) S^(d-1)`, positive weights of total mass one, and precisely the
same ambient odd population state space and topology. Real labels may be
arbitrary finite numbers, including zero. The corollary additionally allows
repeated and antipodal inputs. If zero weights are allowed, they can first
be discarded; no zero-weight group should be assigned a quotient average.

### A. Arbitrary real labels on distinct unoriented input directions

Every argument for M nonzero depends on labels only through the residuals
`r_i=f_i-y_i`. Positive loss provides at least one nonzero residual.
The moment derivatives, paired variations, matrix cancellation, and exact
flat readout contradiction therefore apply unchanged to arbitrary real
labels.

At M=0 the loss is the constant `L_0=sum_i mu_i y_i^2` as w and c vary.
If all labels are zero, this state already has zero loss, so it cannot
contradict the asserted characterization of local minima. If at least
one label is nonzero, the coefficient vector `(mu_i y_i)_i` is nonzero.
Input ridge independence gives the nonzero odd function

\[
                   Q(s)=\sum_i\mu_i y_i\tanh(s\cdot u_i).
\]

The original Section 6 argument then makes `v_c` and `A_y` nonzero by
arbitrarily small, exactly loss-preserving odd changes in c and w.
The matrix direction `N=v_c A_y^T` still has strictly negative derivative
`-2|v_c|^2|A_y|^2`. Replace the number one by L_0 throughout that
argument; nothing else changes. Thus every local minimum has zero loss
also for arbitrary real labels.

The exact-fit construction in Section 6 of this review likewise accepts
any real target vector y: its positive-definite Gram Q depends on the
chosen hidden features, and `c=sum_i (Q^{-1}y)_i psi_i` is bounded and
odd for every finite real y. Hence zero loss is attained throughout this
extended class. If y is identically zero, c=0 is already an exact fit.

### B. Duplicate and antipodal inputs

Partition the finite normalized input set into classes modulo sign.
For each class g choose an actual representative x_g and write uniquely

\[
 x_i=s_i x_g,\qquad s_i\in\{-1,+1\},\qquad
 p_g=\sum_{i\in g}\mu_i>0,\qquad
 \bar y_g=\frac1{p_g}\sum_{i\in g}\mu_i s_i y_i.
\]

Uniqueness of s_i uses x_g nonzero, which follows from the sphere
assumption. Representatives have no parallel or antiparallel pair,
because equal-length parallel vectors differ only by sign and would
belong to the same class. Their weights satisfy `sum_g p_g=1`.

For every state in the model, prediction is odd as a function of input:
lower tanh gives `a(-x)=-a(x)`, the linear middle map and upper tanh
preserve that sign change, and the readout expectation is linear.
Therefore `f(x_i)=s_i f(x_g)`, and

\[
 \begin{aligned}
 \sum_{i\in g}\mu_i(f(x_i)-y_i)^2
 &=\sum_{i\in g}\mu_i(f(x_g)-s_i y_i)^2\\
 &=p_g(f(x_g)-\bar y_g)^2
   +\sum_{i\in g}\mu_i(s_i y_i-\bar y_g)^2.
 \end{aligned}
\]

The cross term vanishes because
`sum_{i in g} mu_i(s_i y_i-ybar_g)=0`. Summing yields the exact identity

\[
 L=C+L_{\rm red},\qquad
 L_{\rm red}=\sum_g p_g(f(x_g)-\bar y_g)^2,\qquad
 C=\sum_g\sum_{i\in g}\mu_i(s_i y_i-\bar y_g)^2\ge0.
\]

C is independent of the state. Consequently a state is a local minimum
of L in the original physical topology if and only if it is a local
minimum of L_red in that same topology. Applying part A to the reduced
real-label dataset gives L_red=0 at every local minimum, hence L=C.
The exact-fit construction fits every representative to bar y_g, so this
bound is attained and is the global minimum of the original loss.
The original conflicting observations are then predicted as
`f(x_i)=s_i bar y_g`; individual conflicting labels need not be fitted.

C vanishes exactly when all signed labels s_i y_i agree within each
class. Otherwise it is the unavoidable squared-error cost of requiring
one odd prediction on each unoriented input direction. This is the exact
architectural floor for the stated p=1 class, because the representative
targets are all simultaneously attainable.

Both extensions are landscape statements only. They add no conclusion
about canonical reachability, fixed straight-line Taylor descent, basin
probability, stochastic excitation, or fitting by any training algorithm.
In the conflicting case, any zero-loss training claim must in particular
be replaced by the attainable floor C; the theorem itself proves no
convergence to that floor.

## Supplement 2: exclusion of a full local point basin for a bad equilibrium

2026-09-19. Informed follow-up verification of the supervisor's proposed
consequence; the earlier provenance and scientific scope remain unchanged.
No additional source or experiment is used. The complete report through
Supplement 1, SHA-256
`9dd2903a6f658f101f322ac939ee4624f06e07800029ec56347a71304d3ebfc2`,
is preserved as the exact prefix of this supplemented report.

**The consequence is correct.** Let S_* be an equilibrium with
`L(S_*)>C`, where C is the attainable architectural floor in Supplement 1.
In the stated physical L2/L2/Frobenius topology, no neighborhood of S_*
can be contained in its point basin for exact gradient flow.

Indeed, every such neighborhood contains a state S with
`L(S)<L(S_*)`: otherwise S_* would be a local minimum, contrary to the
checked theorem. Along any exact physical gradient-flow solution starting
from S, the gradient identity gives

\[
 \frac{d}{dt}L(S(t))=-\|\nabla L(S(t))\|^2\le0,
 \qquad L(S(t))\le L(S)<L(S_*),
\]

on its interval of existence. Loss is continuous in the physical topology,
because the canonical marks are bounded, tanh is Lipschitz, and the finitely
many predictions are continuous contractions of the L2 fields and finite
matrix. Therefore a global solution from S cannot converge in that topology
to S_*: such convergence would force its losses to tend to L(S_*), in
contradiction with the displayed bound. A nonglobal solution does not give
the asserted convergence either. No global-existence theorem is needed
to rule out a neighborhood from which all solutions converge to S_*.

For every global solution from the selected S, its loss is nonincreasing
and bounded below by C. Consequently its limiting loss exists and satisfies

\[
                 C\le\lim_{t\to\infty}L(S(t))
                         \le L(S)<L(S_*).
\]

This excludes a full neighborhood of S_* from its point basin. It does
not prove that the basin has empty interior elsewhere, that it has zero
measure under any specified law, or that canonical initialization avoids
it. It neither proves convergence of arbitrary trajectories nor transfers
this monotonicity argument to discrete or stochastic updates whose loss
need not decrease at every step.
