# What is proved about a configuration-only plateau classification

The subsequent backward-basin investigation is synthesized in
[BASIN_RESULTS.md](BASIN_RESULTS.md). For independent triples it proves
thinness and specified-randomization nullity of the complete basin of
Hilbert convergence to equilibria with loss in (0,1), actual nonstationary
stable trajectories to such equilibria from other starts, and nonempty
open fitting basins. Canonical initialized fitting and positive-loss
behavior without a state limit remain unresolved, so the missing iff
below is unchanged.

Date: 2026-09-18. This is the authoritative synthesis of the terminal
continuation. The requested necessary-and-sufficient condition is **not
proved**. The conclusions are a complete finite-state landscape theorem
for compatible triples, restrictions on every finite initialized
accumulation point, an upper-parameter escape alternative that needs no
full-state endpoint, and a constructive obstruction to deducing input
conflicts from three-rank-one cancellation. The exact gaps are retained below.

All statements concern the same canonical full p=1 closure, d=3,
phi=tanh, x_i in sqrt(3) S^2, binary labels, positive probability weights,
joint canonical marks, ridge 1/4096, w_0=g, c_0=0, M_0=D, and the
unhalved loss in the population L2/L2/Frobenius physical metric. All
entries of M train and its actual transpose is used. These are exact
population statements, with no numerical, width, or closure-order limit.
Only this study's artifacts and established docs were used.

## 1. The exact desired iff and the part already proved

Call a law a descending-plateau law when its canonical trajectory has

\[
                  L'(0)<0,\qquad L_\infty>0.
\]

The limiting loss always exists by monotonicity. Its existence does not
assert convergence of the complete state.

Group raw inputs by equality up to sign. Choose a representative v_G per
group, write x_i=sigma_i v_G, and define

\[
 W_G=\sum_{i\in G}p_i,\quad
 m_G=W_G^{-1}\sum_{i\in G}p_i\sigma_i y_i,
 \qquad L_{\rm odd}=\sum_G W_G(1-m_G^2).                  \tag{1}
\]

The previously proved architectural result states, for every state,

\[
 L(S)=L_{\rm odd}+\sum_G W_G(f_S(v_G)-m_G)^2,
 \qquad \min_S L(S)=L_{\rm odd}.                        \tag{2}
\]

The minimum is attained by a bounded readout with the initialized hidden
features. Also L'(0)=0 iff L_odd=1. These facts use the complete canonical
initialization, not merely input first moments.

The sharp conjecture sought by the user is

\[
 \text{descending positive plateau}\quad\Longleftrightarrow\quad
                         0<L_{\rm odd}<1.               \tag{3}
\]

The right-to-left implication is proved unconditionally for every weighted
triple. If 0<L_odd<1, initial descent is strict and the loss stays at least
L_odd. Local uniqueness prevents a nonstationary trajectory from reaching
a stationary state at finite time: otherwise backward local uniqueness
would identify its whole finite prefix with the constant trajectory.
Therefore L'(t)<0 at every finite time and

\[
                 0<L_{\rm odd}\le L_\infty<1.           \tag{4}
\]

If L_odd=1, initialization is stationary forever, which is excluded by
the definition of a descending plateau. If L_odd=0, every compatible law
starts learning strictly, but its terminal loss is not yet classified.
Thus the missing left-to-right implication in (3) is exactly the statement
that **every compatible initialized triple fits**. It does not require
proving that every incompatible law reaches its architectural minimum;
that latter assertion is stronger and remains separate.

For three distinct raw inputs, L_odd>0 occurs exactly when there is a
same-label antipodal pair. For laws allowing repeated raw inputs,
opposite labels at a coincident point are the other architectural
conflict. With three distinct positive-weight inputs and such an
antipodal pair, the third input ensures L_odd<1, so strict descent followed
by a positive limit is automatic, regardless of its angle or weight.
The earlier reflection example additionally determined the exact limit.

## 2. New landscape theorem: no finite bad local minima on compatible data

A finite state here means w-g and c are bounded functions on the fixed
canonical mark spaces and M is finite. Work in the exact initialized
odd-mark sector. This includes every finite-time state of the original
flow. It does not presume a uniform all-time bound.

**Theorem.** For every compatible weighted triple, including linearly
dependent triples, every finite positive-loss critical state with M!=0
has a bounded admissible direction of strictly negative second variation.
It is therefore a strict saddle. At M=0, every positive-loss critical
state also has arbitrarily nearby lower-loss states; in one precisely
classified case the Hessian is zero and the descent first appears at
third order. Consequently every finite local minimum has zero loss.

Compatible repeated/antipodal copies can first be combined, keeping their
consistent labels and total weights. The theorem requires no uniform
geometry conditioning, no full row rank of M, and no assumed positivity
of an evolved feature Gram. It uses both the first hidden layer and the
readout. Full proofs are in `plateau_finite_critical.md`; an independently
derived proof for independent inputs is in `plateau_global_convergence.md`.

### The mechanism of the proof

Write a_i=E_1[b_1 phi(w.x_i/sqrt(3))], v_i=Ma_i, and
H_i(b_2)=phi(b_2.v_i). At a critical state, a nonzero residual can survive
readout stationarity only when some v_i is zero or some effective vectors
coincide up to sign with incompatible oriented targets. This statement
concerns current representations, not the original inputs.

Take a group of such effective vectors carrying nonzero residuals. Let
u_i=x_i/sqrt(3) just in this proof description and rho_i=p_i(f_i-y_i).
The lower residual-weighted gate field is

\[
               R(w)=\sum_{i\in G}\rho_i\phi'(w\cdot u_i)u_i.
\]

It cannot vanish almost surely when the underlying inputs are distinct
modulo sign. Choose a Gaussian-tail direction with distinct absolute input
projections. Because w-g is bounded, one of these tanh gates decays slower
than all the others on a sufficiently far, positive-probability Gaussian
ball. Its nonzero coefficient prevents cancellation. Full-dimensional
support of the correlated lower marks then supplies a bounded odd lower
perturbation changing a residual-weighted effective vector, whenever M!=0.

The resulting residual-weighted upper feature derivative is a nonzero
combination of functions (b_2.z) phi'(b_2.v), possibly with a linear
term from a zero vector. Such a combination cannot lie in the span of the
current tanh features. Restricting a putative analytic identity to a
generic line and comparing successive exponential tails proves this
separation, including multiple feature groups.

Project that derivative off the current feature span and use the remaining
bounded odd function as a readout perturbation k. Then k changes none of
the current predictions to first order, so its pure readout loss curvature
is zero. Its mixed curvature with the lower perturbation is nonzero.
For a suitable scaling s the full second variation has the form

\[
                   A+4s\|k\|_2^2<0.
\]

This supplies an actual descending direction of the complete state.
The argument does not freeze M or posit a hypothetical missing feature.
Gaussian tails are used to prove existence of a direction, not a uniform
lower bound on its size. Thus this theorem does not provide an exponential
fitting rate or saddle-escape time.

### Consequence for actual initialized trajectories

Every finite accumulation point in the bounded-increment/readout/Frobenius
topology is critical. A nonzero speed near such a point would consume a
fixed positive amount of the finite dissipation budget on each sufficiently
late visit; infinitely many separated visits are impossible.

For compatible data, strict initial descent gives L_infinity<1. A finite
state with M=0 has predictions zero and loss one, so it cannot be such an
accumulation point. Therefore:

\[
 \begin{gathered}
 L_\infty>0\text{ on compatible data}\ \Longrightarrow\
 \text{every finite accumulation point is a strict saddle.}
 \end{gathered}                                          \tag{5}
\]

No existence of an accumulation point, or whole-trajectory convergence
in distance to the saddle set, is inferred. A finite positive-loss point
cannot attract an entire neighborhood: arbitrarily nearby states of lower
loss cannot converge to it under loss-decreasing flow. This rules out an
attracting finite bad minimum as the plateau mechanism on compatible data.
It does not rule out approach along a saddle's stable directions.

## 3. Positive plateau levels or growth of upper parameters

There is a second necessary restriction that needs no full-state endpoint.
Let V(p) be the finite list

\[
 \{0,1,p_i,p_i+p_j,
   4p_ip_j/(p_i+p_j),
   p_k+4p_ip_j/(p_i+p_j),4p_i(1-p_i)\},                  \tag{6}
\]

with distinct indices where appropriate. If ||c(t_n)||_2 and ||M(t_n)||_F
are bounded on any sequence t_n tending to infinity, then

\[
                         L_\infty\in V(p).               \tag{7}
\]

Equivalently, L_infinity outside this list forces
||c(t)||_2+||M(t)||_F to tend to infinity. Every positive listed value is
at least p_min=min_i p_i. In particular any plateau with
0<L_infinity<p_min requires that upper-parameter escape. With equal
thirds, a nonstationary positive plateau with a bounded upper-parameter
sequence must have loss 1/3, 2/3, or 8/9. No reachability of these levels
is asserted.

The proof in `plateau_upper_escape.md` first shows that the readout velocity
tends to zero along every such sequence, using local time regularity and
the finite energy budget. The finitely many v_i=Ma_i have convergent
subsequences because |a_i|<=1. Bounded readout norm enforces identical or
opposite limiting predictions at identical or opposite limiting features,
and zero prediction at a zero feature. Readout stationarity then fixes
each group's prediction to its weighted oriented label mean. Completing
the square gives exactly (6). No population compactness theorem or assumed
limiting density is used.

## 4. Why these results still do not prove the iff

Finite bad critical states actually exist on compatible data. For example,
on equally weighted positive coordinate-axis inputs with labels (+,+,-),
the exact canonical architecture admits a finite state with w=g, full-row-
rank M, vanishing full gradient, and loss 8/9. The bounded readout is
constructed by removing the radial derivative feature from one tanh
feature. The complete construction and negative second variation are in
`plateau_ambient_counterexample.md`.

The prescribed initialization on those very same data is proved to fit.
Thus this example falsifies an ambient no-bad-critical-point argument,
but supplies no initialized counterexample. It exposes the remaining
issue as selection of the trajectory, rather than expressivity or an
absence of descending directions at a hypothetical endpoint.

The user's subsequent rank-one proposal sharpens this obstruction. Three
nonzero rank-one matrices summing to zero do share either their column
line or their row line. This is proved, including all zero-term cases and
quantitative near-cancellation bounds, in `rank_one_geometry.md`. For
independent inputs, the exact first-layer stationarity equations also give
p_i r_i M^T d_i=0 separately. The nonlinear route
`rank_one_joint_stationarity.md` combines this with the complete readout
feature grouping and middle-gradient conditions.

Nevertheless **for every independent input triple, every positive weighting,
and every binary labeling**, there exists a finite compatible nonfitting
critical state with all three middle-gradient terms nonzero rank one.
The complete constructive proof is `rank_one_nonlinear_obstruction.md`.
It retains the canonical correlated lower marks. A coercive convex
Gaussian expectation realizes any three sufficiently small lower moments
a_i by an actual bounded-displacement odd field w. Choose
a_i=sigma_i a and M=e_1 a^T/|a|^2. A bounded odd readout can be chosen so that

\[
 H_i=\sigma_i H,\quad f_i=\sigma_i m,\quad
 d_i=\delta e_2\ne0,\quad M^Td_i=0,
 \qquad \sum_i p_i(f_i-y_i)\sigma_i=0.
\]

The readout and middle gradients then cancel and the lower gradient
vanishes individually, despite all residuals and all rank-one terms being
nonzero. Specifically choose k with p_k<1/2, reverse only the kth label in
sigma, and set m=1-2p_k. The loss is 4p_k(1-p_k), strictly between zero and
one. For balanced weights (1/4,1/4,1/2), labels (+,+,-), and k=1, the
predictions are (-1/2,1/2,-1/2) and the loss is 3/4.

The upper construction is possible because phi(B_1) and B_1 phi'(B_1)
are linearly independent functions. Orthogonal projection gives a readout
that responds to the former but not the latter; an independent odd
component in B_2 supplies the nonzero backward direction. Thus all
nonlinear equations are satisfied, rather than merely their rank bounds.
Omitting that independent component gives another positive-loss critical
state with every d_i=0 and M of full row rank. The independent nonlinear
route also gives an explicit rank-two M version with nonzero d_i.

These constructions impose no input conflict: the collapse is in learned
representations. They are strict saddles and are not asserted reachable
from initialization. They therefore refute the static proof implication,
not the desired initialized fitting conjecture. A proof using the proposed
rank-one structure still needs a property proved along the initialized
trajectory that excludes these otherwise exact critical states.

The checked addendum `rank_one_nonlinear_extensions.md` removes two further
possible algebraic shortcuts. The nonzero-term example can have both
rank M=2 and rank[a_1 a_2 a_3]=2: only the left factors align. The
zero-backward example can have both ranks equal to three. Thus full row
rank of M and independence of the lower contractions, even together, are
insufficient. Their product may still collapse signed upper vectors.
All of these variants are realized on the same exact nonlinear mark laws.

Strict saddle geometry does not by itself exclude a deterministic
trajectory approaching the saddle. For a contained logical counterexample,
the ordinary gradient flow of E(x,y)=x^2+(y^2-1)^2 from (1,0) has
(x(t),y(t))=(exp(-2t),0), energy 1+exp(-4t), and a strict-saddle endpoint.
This example is not the population closure; it demonstrates the missing
logical implication. The canonical population initialization is fixed, so
a generic random-initialization slogan cannot close that implication.

Symmetry alone did not provide a compatible failure. The separate route
`plateau_symmetry_counter.md` proves that every canonical signed-coordinate
symmetry sector of compatible data contains an exact fit at the initialized
hidden state. Transitive three-point symmetries fit along their actual
full flow by the protected scalar clock. A weighted reflection family
with two residuals remains an unresolved candidate; its necessary feature
collisions were derived, but none was proved reachable.

The unresolved dynamical alternatives are therefore precise:

* A compatible prescribed trajectory may approach a nonoptimal strict
  saddle along its stable directions. This has not been constructed or
  excluded for this closure.
* A positive-loss trajectory may have no finite accumulation point.
  The upper-parameter theorem restricts this case but does not exclude it.

Proving these alternatives impossible would establish the missing
necessity in (3). Proving one occurs would disprove that proposed iff
and require a larger configuration class. Neither result is presently
claimed. This synthesis does not replace a configuration-only condition
with an assumption about an unknown future kernel or endpoint.

## 5. Verification and provenance

The independent convergence and finite-critical routes developed different
lower perturbation arguments before reading each other's files. The finite
route's scope record discloses an earlier supervisor sketch of the ambient
8/9 construction, which it did not use. After freeze, the complete proofs
were checked against one another and by the lead author. These are
within-study cross-audits, not fresh isolated promotion reviews.

`review_plateau_finite_critical.md` checks the stronger theorem and all its
supporting arguments. `review_plateau_global_ambient.md` checks the
independent-input theorem, both explicit ambient constructions, and strict
finite-time descent. Their wording repairs retain the independent-input
scope of one auxiliary nullspace criterion, restrict the accumulation
claim to what was proved, and remove M=0 from the list of possible finite
initialized endpoints. Review records preserve original hashes and record
post-repair versions.

`review_plateau_upper_escape.md` checks the upper-parameter theorem against
the exact equations. The study README records current checks and scope.
No numerical experiment was run in this continuation, and no established
book or maintained code was modified.

The subsequent rank-one continuation has a fresh isolated internal review,
`review_rank_one_nonlinear_obstruction.md`. It passes the complete frozen
universal stationary-state construction, the exact canonical carrier and
moment realization, every gradient and loss calculation, and the
full-row-rank variants. Its separately scoped addendum passes both rank
extensions and the bounded nonlinear readout replacement. Full hashes,
source coverage, direct fitting and negative-curvature checks, and the
reachability limitation are retained in that review. The lead checked the
complete independent algebraic and nonlinear routes and all review content.
The necessary initialized implication in (3) remains open.
