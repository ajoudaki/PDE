# Within-study cross-audit of the finite-critical-state candidate

Status: completed internal cross-audit, 2026-09-18. **No substantive defect
found in the central theorem or the six requested supporting arguments.**
Two scope/wording clarifications are recommended below. This is not a fresh
isolated review, not a promotion review, and not an authorization to promote.
No experiment was run and no frozen candidate was edited.

Target read in full: `plateau_finite_critical.md`.

Target SHA256:

`c39efcc8ed4b553b7a0b3bca06a21bbb743593911730168152e96d887159906d`

The scientific sources were restricted to the supervisor's original packet
and this target. The research and rigorous-mathematics skills remain the
process instructions. Before seeing this target, I independently froze
`plateau_global_convergence.md`, whose strict-saddle theorem required
independent inputs. Its proof varied one lower coefficient vector using
dual input vectors, then coupled that perturbation to a readout direction
orthogonal to the current feature span. The target's Gaussian-tail lower
separation, simultaneous upper derivative separation, dependent-input
extension, zero-middle classification, and critical-value gap were newly
read for this cross-audit. Agreement with my narrower theorem is not used
as a substitute for checking the stronger proof.

## 1. Lower separation: checked

The target's Section 3 lower lemma is valid for arbitrary finite states
in its declared initialized odd sector, with directions distinct modulo
sign. It does not assume an injective, continuous, or invertible lower
transport.

For a finite set of pairwise nonantipodal distinct unit directions, the
conditions `e dot u_i=0` and `|e dot u_i|=|e dot u_j|` exclude finitely
many proper hyperplanes. Thus e with a unique smallest positive absolute
projection exists. On `|g-te|<1`, the bound on `w-g` gives

`t|e dot u_i|-C <= |w dot u_i| <= t|e dot u_i|+C`.

Combining these inequalities with the displayed upper and lower bounds
on sech squared gives exactly the factor `4 exp(4C)` and the exponent
in target equation (10). The ratios for all competing indices tend to
zero uniformly on that event. Dividing R by its smallest gate leaves
a vector uniformly approaching `alpha_j u_j`, which is nonzero. A ball
centered at any finite `te` has positive Gaussian probability, however
small. This proves the positive-probability assertion without a hidden
uniform-in-state constant.

The separate nonvanishing of `Mb_1` is also valid. In one coordinate,
the map

`(G,Z) -> (tanh G, tanh(alpha tanh G+sqrt(tau)Z))`

is a smooth bijection from R2 to `(-1,1)^2` with nonzero Jacobian. Its
joint density is positive there. The coordinate products and the
invertible linear Cholesky normalization therefore give an absolutely
continuous full-dimensional lower feature law. For nonzero M, its kernel
has Lebesgue measure zero, hence `Mb_1!=0` almost surely. Intersecting this
full-probability event with `{R(w)!=0}` makes
`E[|Mb_1|^2 |R(w)|^2]>0`; at least one coordinate gives the strict
positivity in (12).

The proposed perturbation is bounded because the marks and R are bounded.
It is odd because `Mb_1` is odd while R(w), composed of even gates, is
even under simultaneous mark negation. These observations establish both
admissibility and the nonzero weighted effective-vector variation needed
later. The identity version used in the M=0 argument is equally valid.

## 2. Upper derivative separation: checked

The target's stronger simultaneous separation statement is valid. A
putative L2 identity is a pointwise identity on the open upper support
cube: the function is continuous and the density is strictly positive.
The generic choice of e can meet all the stated conditions simultaneously,
including a nonzero projection of at least one nonzero z vector.

Restriction to `b=te` first proves a real-analytic identity near zero.
All restricted functions are analytic on the entire real line; extension
over overlapping analytic neighborhoods gives the asserted identity for
all real t. The use of large t is therefore legitimate even when te is
outside the mark-support cube.

Boundedness first forces beta_0=0. The subsequent limit removes the sum
of constant tanh terms. At the smallest remaining positive decay rate,
multiplication by its exponential yields a term `4 beta_j t` on the
left and `-2 A_j sign(a_j)` on the right, up to terms tending to zero
after the appropriate division. Dividing by t forces beta_j=0; taking
the limit without division then forces A_j=0. Removing this index
exactly removes all of its higher harmonics before proceeding to the
next rate. Thus possible harmonic coincidences do not invalidate the
induction. The linear-only case m=0 is covered directly.

Unlike my independently derived radial-feature lemma, this establishes
the needed separation for several groups' derivative vectors at once.

## 3. Strict-saddle theorem without input independence: checked

For a group J with a nonzero residual, target equations (11)--(12)
provide a bounded odd lower perturbation with

`z_J=sum_(i in J) rho_i M delta a_i != 0`.

The perturbation need not isolate one input. It may change every other
group as well. This causes no gap: the simultaneous upper lemma applies
to all resulting z_G together and proves that the complete function S
in (16) has a nonzero component outside the current readout span.

The orientation signs have been handled correctly. For effective vectors
`v_i=sigma_i v_G`, the derivative gate is `sech^2(b dot v_G)` regardless
of sigma_i. Each individual vector variation remains inside the signed
residual-weighted sum defining z_G. No additional sign belongs in (16).

Let `k=S-P_H S`. Its first prediction variation is zero for every input,
and its pure readout second loss derivative vanishes because prediction
is linear in c. In the mixed loss derivative, the term formed by products
of first prediction derivatives is zero for the same reason. The remaining
mixed term is precisely `2 <k,S>=2||k||^2`. Consequently the joint
quadratic form contains `4s||k||^2`, as in (18), with the correct factor
for the unhalved loss. Choosing s negative gives strictly negative
curvature, regardless of the finite pure-lower term.

All perturbations remain bounded and odd. Differentiation along these
fixed directions is justified by bounded marks, bounded state increments,
and bounded tanh derivatives. This proves negative second variation in
an admissible direction of the full physical state space. It does not
require a global twice-Frechet-smooth Hilbert-space gradient theorem or a
stable-manifold theorem; neither stronger result is used by the target.

This proof genuinely removes input independence. The lower argument in
my frozen candidate cannot do so because its dual input vectors would
not exist for a dependent triple.

## 4. M=0 classification and cubic descent: checked

At M=0 all features h_i and predictions vanish, and the only potentially
nonzero first derivative of the loss is the matrix derivative
`-2 d_0 A_y^T`. A rank-one outer product is zero precisely when one of
its factors is zero. The criticality criterion is therefore exact.

If `d_0=0`, `A_y!=0`, the pure matrix quadratic term vanishes as well
as the pure readout term; a nonzero readout/matrix mixed term supplies
negative curvature. If `A_y=0`, `d_0!=0`, the pure lower term vanishes;
the nonzero lower/matrix mixed term can dominate the possibly positive
pure matrix term. The available lower and readout variations claimed in
the target follow respectively from the checked lower lemma and positive
definiteness of the upper mark Gram.

If both factors vanish, the prediction differential vanishes and every
second loss term is zero: the two mixed contractions contain respectively
A_y and d_0, and the pure upper second derivative uses `tanh''(0)=0`.
Thus this case has zero Hessian and should not be described as a strict
saddle. The target correctly makes that distinction.

For the cubic claim, expand `a_i(w+epsilon v)` to second order. The
contribution of c times the term linear in the upper argument vanishes
exactly, at every perturbed w, because d_0=0. The readout perturbation
contributes

`epsilon^2 K z^T N a_i + epsilon^3 K z^T N Da_i[v]`.

After label weighting, the epsilon-squared term vanishes because A_y=0.
The original c contributes the stated cubic term with coefficient -1/3
from tanh. This gives target (20), with each individual prediction of
order epsilon squared. Their squared contribution to loss is therefore
order epsilon fourth. Selecting the finite constant K makes the cubic
loss coefficient negative for positive epsilon and positive for negative
epsilon. The uniform remainder is justified by bounded perturbations
and marks, although the unperturbed Gaussian g is unbounded.

The planar example (21) also checks: its directions have norm one, are
pairwise distinct modulo sign, sum to zero, and each coordinate takes
the values r,-r,0 once. At w=g each normalized lower feature pairing is
an odd function of that coordinate of the input; the correlated reverse
mark preserves this property after conditioning on its Gaussian G.
Thus A_y(g)=0 exactly. With c=M=0 this realizes the zero-Hessian case
inside the declared finite-state class. It is not claimed to be the
canonical initialization or a reached state.

## 5. Critical values and the positive gap: checked

The signed feature independence makes the readout stationarity condition
equivalent to the signed residual sums. Solving one such weighted sum
gives the group mean m_G, and completing the square yields (7). Zero
effective vectors contribute their full weights. For a mixed group,

`4 W_+ W_-/(W_++W_-) >= 2 min(W_+,W_-) >= 2 mu_min`.

The first inequality follows by assuming, without loss of generality,
`W_+<=W_-` and multiplying through the positive denominator. Each nonempty
oriented-label class includes at least one active atom, giving the second
inequality. Hence every positive finite critical value is at least
mu_min. For fixed weights, the finitely many zero sets and signed
partitions do give a finite necessary list of critical values. The target
correctly avoids claiming that every listed value is realizable.

The conditional certificate after crossing `L<mu_min` is sound: a finite
accumulation point must have the common limiting loss, and the critical
gap then forces that loss to be zero. Existence of an accumulation point
is a substantive hypothesis and is retained explicitly.

## 6. Finite accumulation and the correction to my own candidate: checked

The finite-accumulation proof does not need global precompactness. At a
finite state with nonzero vector field, continuity in the declared
supremum/Frobenius norm gives a neighborhood with physical speed bounded
below. Local boundedness of the vector field in the stronger state norm
gives a common positive time during which every sufficiently close visit
remains in that neighborhood. Arrivals along a sequence tending to
infinity have a subsequence separated by this duration. Each visit then
uses a fixed positive amount of the finite dissipation budget, a
contradiction. Thus every specified finite accumulation point is critical.

The topology is important: the assertion uses convergence of `w-g` and c
in L-infinity and of M in Frobenius norm, on the fixed canonical carriers.
It does not infer this convergence from boundedness in a weaker topology.
Loss is continuous in those norms, so an accumulation point has loss
L_infinity.

I independently confirm the supervisor's sharpening of my frozen
candidate. Strict initialized descent gives a time t_0 with
`L(t_0)<1`, hence `L_infinity<=L(t_0)<1`. At any finite strong limit
or finite accumulation point with `M_*=0`, bounded finite c_* gives
`h_i=0`, `f_i=0`, and therefore `L_*=1`. This contradicts continuity
of loss and the preceding inequality. **M_*=0 is already excluded at
every finite accumulation point of a nonstationary initialized
trajectory.** My frozen candidate's list of remaining finite-endpoint
obstructions was therefore unnecessarily broad on this point.

This correction does not exclude a sequence with `M(t)->0` and an
unbounded readout, or another failure of finite accumulation. Such a
sequence belongs to the escaping/noncompact case and must not be
identified with a finite state having M=0.

## 7. Recommended wording clarifications and disposition

1. In Section 2, retain the independent-input qualifier explicitly in the
   sentence beginning “More generally the complete nullspace ...”. The
   per-index condition `lambda_i M^T d_i=0` was justified there using
   independent inputs. The next sentence explains that “more generally”
   means arbitrary finite states rather than fitting states, but a reader
   could misread it as removing input independence. The central stronger
   saddle theorem does not need that condition and is unaffected.
2. Replace the final phrase “must approach the finite strict-saddle set”
   with “every finite accumulation point is a strict saddle”. The proof
   establishes the latter. If the former is intended to assert convergence
   in distance of the entire trajectory to that set, it would require an
   additional argument when the trajectory also has noncompact portions.

Subject to these wording clarifications, the checked mathematical content
is internally sound. The strongest supported synthesis is: every finite
nonoptimal critical state of a compatible law with at most three distinct
unoriented inputs is a saddle; those with nonzero M have negative second
variation, and the remaining M=0 cases have either negative second
variation or the exhibited cubic descent. Every finite positive-loss
accumulation point of the canonical trajectory lies in the nonzero-M
strict-saddle class, with its loss in the stated finite positive list.
Deterministic saddle avoidance and existence of finite accumulation remain
unproved. This cross-audit supplies neither bridge.

## Post-repair check

Checked the repaired target on 2026-09-18, SHA256
`3aa693f975862230fec875ab787de48f56116814afd37f52be6b66a042f54ffd`.
The nullspace statement now explicitly assumes independent inputs. The
final conclusion now states that every finite accumulation point is a
strict saddle and expressly disclaims whole-trajectory distance
convergence. Both scope clarifications are correct and resolve the two
wording observations above.

As a text-integrity check, reversing exactly these two wording changes
and their header record reconstructs the original reviewed hash
`c39efcc8ed4b553b7a0b3bca06a21bbb743593911730168152e96d887159906d`.
Thus the mathematical argument, formulas, and inequalities are unchanged.
The internal cross-audit disposition remains: no substantive defect found
in the checked result; initialized saddle avoidance and finite accumulation
remain open. No source edit, experiment, or additional research was done
in this post-repair check.
