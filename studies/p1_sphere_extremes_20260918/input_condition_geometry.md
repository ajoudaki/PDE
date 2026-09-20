# Data-only residual-field independence: a basin criterion and a dependent four-input class

Independent first candidate, 2026-09-18. Scoped theoretical continuation;
internally derived, not independently reviewed or promoted. Scientific
inputs read completely: `docs/observable_p1.md`, and this study's
`DEPENDENT_BASIN_RESULTS.md`, `dependent_hilbert_geometry.md`,
`dependent_basin_functional.md`, `finite_basin_geometry.md`,
`finite_basin_tail.md`, and `finite_critical_loss_gap.md`. No other study,
current sibling route, experiment, or numerical calculation was used.
The investigate-conjectures and solve-math-rigorously skills and the
research-contract, evidence-ledger, and adversarial-audit references were
applied. This file is the route's only output.

## 1. Conclusion and contract

There is an explicit data-only sufficient condition that closes both the
negative-curvature and physical-Hilbert regularity obligations. It is a
finite list of specified finite-dimensional nonlinear rank tests. A stronger
version is decidable by finitely many linear feasibility problems. The
stronger condition holds on an open family of linearly dependent four-input
data in dimension three: after orienting inputs by their binary labels, the
unique input relation has two positive and two negative coefficients.

For this class, the full positive-loss point-basin conclusion of the
three-input result extends without an endpoint boundedness assumption.
This is not an unrestricted generic-data theorem: the four-input class is
open and nonempty, but not dense for fixed labels. The nonlinear criterion
has not been proved generic at arbitrary finite input count. The stronger
linear-feasibility certificate is too restrictive for five or more dependent
inputs; Section 6 proves that limitation.

Use exactly the canonical order-one odd state space

\[
\mathcal H_d=L^2_{\rm odd}(P_1;\mathbb R^d)
 \oplus L^2_{\rm odd}(P_2)\oplus\mathbb R^{d\times2d},
\qquad \theta=(w-g,c,M),
\]

with the physical L2/L2/Frobenius norm, correlated lower marks, actual
transpose, full trained matrix, all trained blocks and unhalved square
loss. Inputs are unit vectors u_i distinct modulo sign; p_i>0 sum to one;
y_i are binary. No experiment, approximation, change of randomization,
or finite-network assertion enters the result.

## 2. A finite family of data maps

Enumerate every signed partition P: a possibly empty zero group Z, together
with nonempty groups G and signs sigma_i in {+1,-1} for each i in G.
Repeated choices related by reversing every sign in one group cause no
problem. Define entirely from the data

\[
 W_G=\sum_{i\in G}p_i,\quad A_G=\sum_{i\in G}p_i\sigma_i y_i,
 \quad F_G=A_G/W_G,
\]
\[
 f_i^P=\begin{cases}0&i\in Z,\\ \sigma_i F_G&i\in G,\end{cases}
 \quad \rho_i^P=p_i(f_i^P-y_i),
 \quad \ell_P=\sum_i p_i(f_i^P-y_i)^2.
\tag{1}
\]

Call Z active when nonempty. A nonzero group G is active precisely when
its oriented labels sigma_i y_i include both signs. If it is inactive,
all its residuals vanish. If it is active, |F_G|<1 and all its residuals
are nonzero. Consequently every active residual has sign

\[
                         \operatorname{sign}\rho_i^P=-y_i.
\tag{2}
\]

Keep only the finitely many P with 0<ell_P<1. Let J_1,...,J_K be their
active groups. For s in R^d set

\[
 R_{J}(s)=\sum_{i\in J}\rho_i^P\operatorname{sech}^2(s\cdot u_i)u_i,
 \qquad \mathcal R_P(s)=[R_{J_1}(s)\ \cdots\ R_{J_K}(s)].
\tag{3}
\]

**Nonlinear data condition (NR).** For every retained P and every s in
R^d, the matrix R_P(s) has column rank K.

Equivalently, det(R_P(s)^T R_P(s))>0 for every finite s. This condition
uses only finitely many specified analytic functions of finitely many
variables and the given data. It quantifies over s, not over unknown
Hilbert equilibria or future trajectories. No uniform lower singular-value
bound as |s| tends to infinity is required. It is a sufficient condition,
not asserted necessary for basin nullity.

At an actual equilibrium, independence of distinct signed upper tanh
features gives exactly the predictions (1), as proved in the complete
`finite_critical_loss_gap.md`. Thus its signed grouping is one of the
listed partitions whenever 0<L<1. This is the bridge from the finite data
enumeration to the exact physical system.

## 3. Why (NR) gives the full Hilbert theorem

At an equilibrium write a_i=E_1[b_1 tanh(w dot u_i)], v_i=M a_i,
d_i=E_2[b_2 c sech^2(b_2 dot v_i)]. Within an effective group J the
vectors d_i coincide, since the upper derivative gate is even. This is
also true in the zero group. Put q_J=M^T d_J. The exact lower stationarity
equation becomes

\[
       \sum_{J\ {m active}} (b_1\cdot q_J)R_J(w)=0
                   \quad P_1\hbox{-almost surely}.
\tag{4}
\]

Every L2 lower field has finite values almost surely. Apply (NR) at its
value w: (4) gives b_1 dot q_J=0 almost surely for every active J. The
canonical b_1 law is absolutely continuous with positive density on a
neighborhood of zero, so a linear form vanishing almost surely has zero
coefficient. Hence q_J=0. Inactive groups already have zero residuals.
Thus the individual coefficients cancel:

\[
                       T_i=\rho_i M^T d_i=0\quad\hbox{for every }i.
\tag{5}
\]

This verifies the regularity premise, not just an unstable direction.
The bounded-mark estimates in `dependent_basin_functional.md`, equations
(13)--(16), apply without endpoint boundedness once (5) holds: the finite
coefficients T_i are locally C^(1,1); the lower gate operators G_i(w)
are Lipschitz from lower L2 to operators from R^(2d) to lower L2. At a
center with T_i=0, the remainder after subtraction of the linearization
is a product of two O(r) factors plus a C^(1,1) coefficient remainder.
Therefore the exact physical field satisfies

\[
 F(\theta_*+z)=Az+N(z),\qquad
 \operatorname{Lip}(N|_{B_r})\le C r.
\tag{6}
\]

The bounded self-adjoint operator A=-D^2L has finite rank at most
(3d+1)m+2d^2 and bounded-field range, as in that source.

Positive loss means at least one active group exists; (NR) makes each of
its R_J(w) nonzero almost surely. Loss below one forces M!=0. Absolute
continuity of b_1 gives M b_1!=0 almost surely. For some coordinate l,
the bounded odd lower direction

\[
                h=(M b_1)_l R_J(w)
\]

therefore gives

\[
 \left[\sum_{i\in J}\rho_i M Da_i[h]\right]_l
       =E_1[(M b_1)_l^2|R_J(w)|^2]>0.
\tag{7}
\]

The exact finite-family upper derivative-feature separation argument in
the same source, equations (35)--(38), supplies a bounded odd readout
direction k orthogonal to the current upper-feature span with

\[
 D^2L[(h,t k,0),(h,t k,0)]=Q_h+4t\|k\|_2^2,
 \qquad k\ne0.
\tag{8}
\]

A sufficiently negative finite t yields negative curvature. The actual
Hilbert Hessian exists by (5)--(6), so this is a nonzero positive spectral
subspace for A. It is not merely a directional assertion at a singular
endpoint.

The full graph argument of `dependent_basin_functional.md`, Sections
4--5, now has all its hypotheses: the finite nonzero unstable subspace,
self-adjoint splitting, (6), global forward physical flow, locally
Lipschitz time maps with invertible strongly continuous directional
derivatives, and separability of H. Its contraction constructs a local
trapping graph at each bad endpoint; a countable neighborhood cover and
integer-time pullbacks give a countable union of closed Lipschitz
hypersurfaces containing the entire set

\[
 \{\theta_0:\Phi_t\theta_0\to\theta_*\text{ in }\mathcal H_d,
                       \quad0<L(\theta_*)<1\}.
\tag{9}
\]

Consequently this set is meagre, has a shy Borel hull, and has outer
probability zero under every translation and positive rescaling of the
specified full-support bounded-increment Gaussian series in
`DEPENDENT_BASIN_RESULTS.md`, equation (4). Conditioning that law on a
positive-probability initial sublevel L(theta_0)<1 preserves the conclusion:
almost surely, a trajectory with a physical-H state limit must fit. State
convergence itself and the deterministic canonical point remain untreated.

## 4. A stronger, finitely checkable certificate

Replace the linked derivative gates in (3) by arbitrary independent
positive numbers t_i. Require, for every retained P,

\[
 \left[\sum_{i\in J_1}\rho_i^P t_i u_i\ \cdots\
       \sum_{i\in J_K}\rho_i^P t_i u_i\right]
                 \quad\hbox{has column rank K for all }t_i>0.
\tag{10}
\]

Call this condition (PR). It implies (NR). It is equivalent to failure of
each of finitely many linear feasibility systems. For every nonzero
assignment epsilon=(epsilon_J) in {-1,0,1}^K, ask whether beta in R^m
satisfies

\[
 U\beta=0,\qquad
 \beta_i=0\quad\hbox{outside groups with }\epsilon_J\ne0,
\]
\[
              \epsilon_J\rho_i^P\beta_i\ge1
                 \quad(i\in J,\ \epsilon_J\ne0).
\tag{11}
\]

Condition (PR) holds exactly when every such system is infeasible.
Indeed a rank failure produces a nonzero column relation z and
beta_i=z_J rho_i^P t_i on each active group. Set epsilon_J=sign z_J;
then all nonzero constrained products have strictly positive sign. A
common rescaling of beta makes them at least one. Conversely a feasible
beta gives a column relation with z_J=epsilon_J and positive
t_i=beta_i/(epsilon_J rho_i^P) in the nonzero groups; the values in
zero-coefficient groups can be any positive numbers. This proves both
directions. All variables and matrices in (11) are finite dimensional
and known from the data, with no endpoint oracle.

## 5. An open class of dependent four-input data

Let m=4, let every triple of u_i be independent, and let the four vectors
have rank three. Let alpha be their unique relation, U alpha=0. Every
alpha_i is nonzero. Assume equal data weights and

\[
  \#\{i:\alpha_i y_i>0\}=\#\{i:\alpha_i y_i<0\}=2.
\tag{12}
\]

The choice alpha versus -alpha does not change (12). This is a purely
finite condition on inputs and labels. It implies (PR), hence the complete
physical-H basin conclusion (9).

To prove it, suppose (10) has a rank failure for a retained P. Its induced
beta is a nonzero multiple of alpha. Thus no beta_i is zero: every input
is in an active group and every group coefficient z_J is nonzero. Since
sign rho_i=-y_i, within each group

\[
        \operatorname{sign}(\alpha_i y_i)
          \quad\hbox{is constant as i ranges over J}.
\tag{13}
\]

The two sign classes in (12) have size two. Therefore every active group
has at most two members. A nonzero-feature active group cannot be a
singleton; if it is a pair, its oriented labels conflict and its equal
weights give F_G=0. The zero group also has zero predictions. There are
no inactive fitted groups because beta has full support. Every prediction
is consequently zero, so ell_P=1, contrary to retention of P. This proves
(PR). Notice that no actual sech gate values were used.

One concrete instance in dimension three has all labels +1 and

\[
 u_1=(C,S,0),\quad u_2=(C,-S,0),\quad
 u_3=(C,0,S),\quad u_4=(C,0,-S),\quad
 C,S>0,\ C^2+S^2=1.
\tag{14}
\]

Every triple is independent and the relation is
u_1+u_2-u_3-u_4=0. No two inputs are parallel. All sufficiently small
independent perturbations on the unit sphere retain nonzero three-column
minors and the two-versus-two relation signs. Thus the family contains an
open set in (S^2)^4, with positive angular measure, and its members are
necessarily linearly dependent. Formula (14)'s symmetry is dispensable.
For any prescribed binary labels replace u_i in (14) by y_i u_i; the same
open-family assertion then holds for those labels.

For arbitrary positive weights, the same proof works if the two weights
within each sign class in (12) are equal; the weights of the two classes
may differ. In any active pair permitted by (13), the two masses are then
equal and force F_G=0. Arbitrary unequal weights without this restriction
are not covered by this elementary certificate.

The condition is label-aware. It is not a theorem uniform over every
binary labeling of one fixed geometric configuration. For fixed labels
the other circuit sign patterns also occur on open sets, so the admitted
family is not dense. This scope should not be called generic input data
without qualification.

## 6. Exact limitation of the stronger certificate

For equal weights and nonparallel inputs, (PR) cannot hold for any
linearly dependent family with m>=5. More generally, it fails whenever
there is a nonzero input relation beta supported on a proper subset S.

To verify the latter assertion, split S by the sign of beta_i y_i. If
only one sign occurs, use S as the zero group and put all remaining
indices into fitted singleton groups. If both signs occur and both sign
classes have size at least two, use them as nonzero-feature active groups,
choosing the sigma_i in each class so its oriented labels include both
signs; put all remaining indices into fitted singletons. If one sign class
is a singleton, use it as Z and the other as an active nonzero group.
The other class has size at least two because a relation supported on
one or two nonparallel nonzero inputs is impossible. In every case the
partition has positive loss at most |S|/m<1, and beta has constant sign
relative to rho on every active group. Positive t_i and nonzero column
coefficients therefore realize rank failure as in (11).

If there is no proper-support relation, the kernel must have dimension
one: two independent kernel vectors can be linearly combined to cancel
one coordinate while retaining a nonzero vector. Its generator alpha has
full support. For m>=5, one sign class of alpha_i y_i has at least three
members (or all entries have the same sign). Use that class as a nonzero
active group and choose its oriented labels with unequal counts, so its
forced mean F_G is nonzero. Handle the other sign class as a zero group
if it is a singleton, or as another active group if it has at least two
members. If it is absent, the first group is the whole dataset. Every
index is active; at least one prediction is nonzero, and the stationary
partition identity ell_P=1-sum_G W_G F_G^2 yields 0<ell_P<1. Again alpha
has the required within-group relative signs, so (PR) fails.

This is a limitation of replacing nonlinear gates by independent positive
variables. It does not disprove (NR) for those data, and does not refute
the desired basin theorem. The nonlinear linkage t_i=sech^2(s dot u_i)
can rule out the artificial conic configurations allowed in (10).

## 7. Claim ledger and unresolved issue

| Claim | Status | Evidence or limitation |
|---|---|---|
| (NR) is a data-only sufficient condition for full physical-H point-basin nullity | Proved candidate | Finite forced residual enumeration, (4)--(8), complete existing graph argument |
| (PR) is a finite linear-feasibility certificate for (NR) | Proved candidate | Exact equivalence with (11) |
| An open dependent four-input class satisfies the full theorem | Proved candidate | Balanced oriented circuit (12), proof (13), open example (14) |
| The four-input class is dense for fixed labels | False | Other circuit sign patterns occur on open sets |
| (PR) can cover dependent equal-weight data with m>=5 | False | Section 6 |
| (NR) is generic for arbitrary finite m | Open | No transversality, root-exclusion, or genericity proof supplied |
| Each R_J(s) nonzero alone implies the full Hilbert theorem | Unsupported | It supplies curvature but does not force (5) or verify (6) |
| Excluding the seven-input moment matching by itself suffices | Open | Other singular or degenerate configurations have not been classified |

The adversarial check is explicit: the known seven-input construction
violates (NR), since its sole active R_J vanishes at the two-point lower
support. The criterion does not smuggle in bounded endpoint displacement,
independent lower marks and g, or an assumed Hilbert Hessian. It does use
a stronger rank condition than necessary, and that strength has a proved
scope cost. A generic arbitrary-m answer still needs a weaker cancellation
mechanism or a proof of the nonlinear data rank condition on a substantial
larger class.
