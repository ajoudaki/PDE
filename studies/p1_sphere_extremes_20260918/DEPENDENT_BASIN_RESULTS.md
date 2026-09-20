# Removing input independence from the population basin theorem

Date: 2026-09-18. Authoritative continuation of `BASIN_RESULTS.md` for
the same study. This concerns the exact fixed-order p=1 population flow,
not a finite network, particle approximation, or order limit. Complete
new proofs are in `dependent_hilbert_geometry.md`,
`dependent_basin_functional.md`, and `dependent_finite_fitting.md`.
The existing graph/probability arguments are in `basin_spectral_route.md`
and `basin_hilbert_null_extension.md`. The integrated internal review is
`review_dependent_extension.md`; checking and promotion remain distinct.

## 1. Main improvement

The original physical-Hilbert, point-convergence, probability-zero theorem
extends to **every equally weighted compatible three-input configuration**
on a normalized sphere, including every three distinct non-antipodal circle
points. There is no linear-independence, angle-separation, or bounded-limit
field premise in this statement.

For arbitrary positive weights the same theorem holds for generic triples,
including generic circle triples. The exact sufficient data criterion below
is weaker than requiring genericity: it also covers many reflected triples.
For every weighted triple, including the exceptional reflected ones, a
specified loss sublevel and a separate bounded-lower-endpoint theorem survive.
The unqualified arbitrary-weight/all-H-endpoint extension is not claimed.

For any finite number of compatible inputs in any fixed dimension, an
additional theorem gives an explicit fit and a nonempty physical-Hilbert-open
basin with exponential loss decay and a fitted endpoint. This last conclusion
is about a nonempty basin, not almost-everywhere fitting.

## 2. Exact model, state and probability

Fix d>=2, x_i in sqrt(d) S^(d-1), p_i>0, sum_i p_i=1 and y_i in {+1,-1}.
Keep the canonical p=1 joint initialization and ridge 1/4096 from
`docs/observable_p1.md`: frozen lower marks (b_1,g), upper marks b_2,
b_1 in R^(2d), b_2 in R^d after exact odd-parity reduction. The moving
matrix M is full d by 2d and uses its actual transpose. Write phi=tanh,
u_i=x_i/sqrt(d), and

\[
\begin{gathered}
 a_i=E_1[b_1\phi(w\cdot u_i)],\quad v_i=Ma_i,\quad
 H_i=\phi(b_2\cdot v_i),\quad f_i=E_2[cH_i],\quad r_i=f_i-y_i,\\
 d_i=E_2[b_2c\phi'(b_2\cdot v_i)],\qquad
 L=\sum_i p_i r_i^2.
\end{gathered}\tag{1}
\]

The exact physical flow is

\[
\begin{split}
 \dot w&=-2\sum_i p_i r_i\phi'(w\cdot u_i)
                       (b_1^TM^Td_i)u_i,\\
 \dot c&=-2\sum_i p_i r_iH_i,\qquad
 \dot M=-2\sum_i p_i r_i d_i a_i^T.
\end{split}\tag{2}
\]

Use displacement coordinates theta=(w-g,c,M) in

\[
 \mathcal H_d=L^2_{\rm odd}(\Omega_1;\mathbb R^d)
 \oplus L^2_{\rm odd}(\Omega_2)\oplus\mathbb R^{d\times2d}.
\tag{3}
\]

Its norm is exactly the physical L2/L2/Frobenius norm. The bounded-mark
proof gives a unique global forward flow Phi_t on H_d, with C1 loss and
L'=-||dot theta||_H^2. It agrees with canonical bounded-displacement
characteristics at every finite time from those states. All estimates and
finite-time directional flow regularity in the preceding basin proofs
extend to fixed d and any finite input count; independence was used only
at their critical-point cancellation step, replaced below.

The specified randomization is the same one as before. Choose bounded odd
H_d-unit directions e_n dense in the H_d-unit sphere, including matrix
directions, put ||.||_b equal to the sum of the two essential-supremum
norms and the Frobenius norm, and let

\[
 Z=\sum_{n\ge1}\frac{2^{-n}}{1+\|e_n\|_b}\,g_ne_n,
 \qquad g_n\text{ independent }N(0,1),\qquad
 \theta_0=\theta_{\rm ref}+\varepsilon Z,\quad\varepsilon>0.
\tag{4}
\]

This randomizes population fields, not individual Gaussian marks already
integrated into the fixed carriers. It has full support in H_d and bounded
increments almost surely. All probability-zero assertions include every
fixed translation theta_ref and positive scale epsilon; conditioning on a
positive-probability open initial-state constraint preserves them.
There is no infinite-dimensional Lebesgue measure assertion. The canonical
point (w,c,M)=(g,0,D) itself is deterministic and is not covered by taking
epsilon=0 in (4).

## 3. The exact geometric criterion for three inputs

Assume three representatives are pairwise distinct modulo sign. Compatible
coincident or antipodal copies can first be merged, adding their masses and
orienting labels consistently. With at most two representatives the vectors
are independent and the old argument applies directly. With three, their
rank is either three or two.

For a rank-three triple define E to be empty. For a rank-two triple, define
E as follows. For each unordered pair {i,j} with remaining index k, include
(i,j;k) in E precisely when all three conditions hold:

\[
 |u_i\cdot u_k|=|u_j\cdot u_k|,\qquad
 y_i=-\sigma y_j,\qquad p_i\ne p_j,\tag{5}
\]

where n is either unit vector in the two-dimensional input span perpendicular
to u_k and sigma=sign[(u_i dot n)(u_j dot n)]. Neither projection vanishes,
so sigma is well-defined and independent of the choice n versus -n. The
first condition describes a reflection of the two unoriented directions.
The second concerns their labels after orientation by this perpendicular
projection, not an architectural contradiction between the raw inputs.

**Full Hilbert basin theorem.** If E is empty, the set

\[
 \{\theta_0:\Phi_t\theta_0\to\theta_*\text{ in }\mathcal H_d,
                          \quad 0<L(\theta_*)<1\}\tag{6}
\]

lies in a countable union of closed Lipschitz hypersurfaces in H_d.
It is meagre, has a shy Borel hull, and has probability zero under (4).
In particular, under (4) conditioned on L(theta_0)<1,

\[
 \Pr\{\theta_t\text{ converges in }\mathcal H_d
                       \text{ and }L_\infty>0\}=0.\tag{7}
\]

If state convergence additionally holds almost surely, loss tends to zero
almost surely. State convergence itself has not been proved.

Two useful sufficient cases of E empty are:

* p_1=p_2=p_3=1/3, with every pairwise nonparallel normalized triple and
  every binary labeling, including arbitrary circle angles.
* Arbitrary positive weights and labels, with
  (u_i dot u_k)^2 != (u_j dot u_k)^2 for every remaining-index choice k
  in the rank-two case. No restriction beyond independence is needed in
  rank three. The displayed rank-two exclusions are proper angle equations,
  so their complement is open, dense and of full angular measure among
  nonparallel circle triples: in angular coordinates they fix finitely many
  values of one angle after the other two are fixed.

For a reflected pair, equal pair masses or y_i=sigma y_j suffices to stop
that pair from belonging to E. Thus (5) is sharper than geometric asymmetry.
Neither near alignment nor near reflection is excluded; no uniform local
spectral gap as data approach these sets is asserted.

## 4. Why the nonlinear geometry replaces input independence

At an equilibrium put rho_i=p_i r_i and T_i=rho_i M^Td_i. The old proof
used independent u_i to deduce T_i=0 from the lower equation. For a dependent
triple, let sum_i alpha_i u_i=0 be its unique relation, with alpha_i all
nonzero. Lower stationarity instead gives

\[
 \phi'(w\cdot u_i)\left(b_1\cdot\frac{T_i}{\alpha_i}\right)
                   \quad\text{independent of }i\quad\text{a.s.}\tag{8}
\]

If one T_i vanishes, all vanish. Otherwise positivity of the gates makes
all three linear forms in b_1 have the same sign. The exact joint lower
mark marginal is absolutely continuous and positive on a neighborhood of
zero. Two nonzero linear forms with the same sign there are positive
multiples: independent forms take opposite prescribed signs on an open
set, and negative proportionality also contradicts sign agreement.
Therefore T_i/alpha_i=kappa_i q with kappa_i>0 and q!=0. The hyperplane
b_1 dot q=0 has probability zero, and (8) forces fixed ratios among the
three derivative gates.

The new geometric lemma in `dependent_hilbert_geometry.md` says that, on
three distinct projective directions of a unit circle, these ratios determine
a vector in the input plane up to sign:

\[
 \phi'(s\cdot u_i)=a\phi'(t\cdot u_i)\ (i=1,2,3),\ a>0
                       \quad\Longrightarrow\quad s=\pm t.\tag{9}
\]

Its proof is complete and elementary. For independent s,t, the map
u -> (s dot u,t dot u) sends the unit circle to a centered ellipse. A
nontrivial proportionality in (9) would put three distinct projective points
of that ellipse on cosh(x)=K cosh(y), K>1. With F(y)=arcosh(K cosh y),
the proved inequality F-yF'>(y^2/2)F'' makes Q(F(y),y) strictly convex
for every positive quadratic form Q. It has at most two intersections
with Q=1, a contradiction. The proportional-vector and K=1 cases reduce
to the elementary fact that three distinct projective circle directions
cannot have the same absolute projection on a nonzero vector.

Consequently, if some T_i is nonzero, the input-plane projection of the
lower field must equal +/-s_0 almost surely, for one nonzero fixed s_0.
Thus for a sign field epsilon,

\[
 a_i=\phi(s_0\cdot u_i)A,\qquad
 A=E_1[b_1\epsilon],\qquad
 v_i=\phi(s_0\cdot u_i)MA.\tag{10}
\]

All rho_i are nonzero. Upper tanh features with distinct nonzero effective
vectors modulo sign are linearly independent (restrict their analytic
identity to a generic line and separate exponential rates). Upper
stationarity sum_i rho_i H_i=0 thus permits no nonzero singleton feature.
A three-way equal nonzero magnitude contradicts the circle-projection fact.
The only remaining pattern is a signed pair and a zero singleton:

\[
 v_j=\sigma v_i\ne0,\qquad v_k=0.\tag{11}
\]

Equation (10) makes s_0 perpendicular to u_k, with equal absolute projections
on u_i,u_j, giving the first condition in (5). The readout equation gives

\[
 f_i=\frac{p_i y_i+p_j\sigma y_j}{p_i+p_j},\quad
 f_j=\sigma f_i,\quad f_k=0.
\]

Consistent oriented labels would fit the pair and make rho_i=0. Thus they
must conflict. In that case the critical loss equals

\[
 \ell_{ij;k}=p_k+\frac{4p_ip_j}{p_i+p_j}
            =1-\frac{(p_i-p_j)^2}{p_i+p_j}.\tag{12}
\]

It is below one only if p_i!=p_j. This proves that E empty forces T_i=0
at every Hilbert equilibrium with 0<L<1, without any endpoint norm bound.

## 5. Negative curvature and the entire basin argument

The second new ingredient is stronger than the data criterion: **every**
nonaligned triple equilibrium with 0<L<1 has negative bounded directional
curvature, even when E is nonempty. To see the mechanism, group the current
effective vectors v_i by equality modulo sign, including one zero group.
For each group J use

\[
 R_J(w)=\sum_{i\in J}\rho_i\phi'(w\cdot u_i)u_i.\tag{13}
\]

If R_J is nonzero on positive lower probability, some bounded odd variation
h=(Mb_1)_ell R_J has nonzero residual-weighted effective-vector change in
that group. Its residual-weighted upper derivative S contains terms
(b_2 dot z_G)phi'(b_2 dot v_G), or a nonzero linear term for the zero group.
Analytic restriction to a line and separation of exponential rates prove
S is outside span{H_i}. Let k be its orthogonal complement to that span.
Then k is bounded, odd and nonzero, its first prediction variation vanishes,
and the mixed lower/readout loss variation is

\[
 D^2_{\rm dir}L[(h,sk,0),(h,sk,0)]=Q_h+4s\|k\|_2^2.\tag{14}
\]

A finite negative s gives strict descent curvature. Pair or singleton groups
have R_J nonzero by independence of any two nonparallel inputs. A possible
three-way group with R_J=0 almost surely would force the two-point structure
(10) by (9), contradicting three equal nonzero projection magnitudes. All
pairings are legitimate with c in L2 and bounded variations. This proves
the needed negative direction without assuming an H Hessian exists everywhere.

At T_i=0 equilibria the H Hessian does exist. Write
G_i(w)t=phi'(w dot u_i)(b_1 dot t)u_i. The finite coefficient T_i is locally
C^(1,1), and G_i is Lipschitz into lower L2. Vanishing T_i at the equilibrium
makes the lower nonlinear remainder a product of two O(r) factors on a
radius-r ball, with Lipschitz constant O(r). The upper and matrix blocks
are locally C^(1,1). Consequently

\[
 F(\theta_*+z)=Az+N(z),\qquad
 \operatorname{Lip}(N|_{B_r})\le Cr.\tag{15}
\]

The multiplier involving phi'' times T_i vanishes. The remaining derivative
is self-adjoint finite rank, at most (3d+1)3+2d^2. Its range consists of
bounded fields and matrix coordinates. Equation (14) now supplies a positive
eigenvalue of the flow linearization A; pure readout variation also supplies
a negative one. The first gives a finite nonzero unstable subspace.

For completeness, the exact local trapping construction has no extra data
hypothesis. Split z into unstable and center-stable coordinates, let lambda
be the smallest unstable eigenvalue, retract N to a small ball so its global
Lipschitz constant epsilon satisfies 4epsilon/lambda<1/2, and solve

\[
\begin{split}
 z_{cs}(t)&=e^{A_{cs}t}\xi+
       \int_0^t e^{A_{cs}(t-s)}N_{cs}(z(s))ds,\\
 z_u(t)&=-\int_t^\infty e^{A_u(t-s)}N_u(z(s))ds.
\end{split}\tag{16}
\]

The path norm sup_(t>=0)e^(-lambda t/2)(||z_cs||+||z_u||) makes the
sum of integral Lipschitz constants at most 4epsilon/lambda. Contraction
therefore gives a Lipschitz graph z_u(0)=h(xi). Every orbit trapped in the
original ball lies on it: variation of constants from a terminal time T
has an unstable terminal term tending to zero as T tends to infinity.
The graph has positive codimension and is contained in a scalar Lipschitz
hypersurface.

Any H-convergent trajectory has an equilibrium as its limit. Otherwise,
continuity of F supplies a continuous linear functional whose value on the
velocity is eventually bounded below by a positive constant; integrating
it contradicts convergence of that functional of the state.

Cover all regular bad equilibria by their smaller trapping neighborhoods
and use H separability to choose a countable subcover. Any point-convergent
bad orbit eventually stays in one selected larger neighborhood, so its
state at some integer time lies on its trapping graph. Every finite time
map is locally Lipschitz with invertible norm-Gateaux derivative, continuous
on each fixed direction. The full proof in `basin_hilbert_null_extension.md`
uses dominated convergence for lower gates, C^(1,1) moment maps, and the
linear variational integral equation; it uses no input independence.

A time-map preimage of a Lipschitz hypersurface has a countable hypersurface
cover. Indeed, at any preimage point choose a direction whose derivative
image is transverse to the hypersurface. Strong directional continuity gives
a uniformly positive scalar slope along nearby parallel lines; local
Lipschitzness controls variation across these lines. The zero-set coordinate
is a Lipschitz function on its domain, extended by the scalar infimum
extension to a global hypersurface. Second countability and the integer-time
cover finish the countable closed hypersurface hull.

Each such hypersurface has an open cone of line directions meeting it at
most once. Some e_n in (4) belongs to that cone. Condition on all other
Gaussian coefficients: the remaining atomless coordinate hits that possible
single point with probability zero. Countable subadditivity proves nullity.
Uniform[-1,1] coefficients give the compactly supported translation-null
witness for shyness. This verifies all obligations of (6)--(7).

## 6. What is proved for every weighted triple

No assumption (5) is needed for the nullity of the basin of regular bad
endpoints, meaning T_i=0 for every i. The preceding argument covers them
individually even when singular endpoints coexist for the same data.
The cancellation classification proves that every remaining endpoint must
have (11), the two-point lower projection (10), and loss in the finite set

\[
 \{\ell_{ij;k}:(i,j;k)\in E\}.\tag{17}
\]

Thus under (4), almost surely every point-convergent trajectory with limiting
loss below one either fits or has loss in (17). This statement does not say
that any of the latter alternatives has a basin of positive probability.

A complete fitting implication for arbitrary weighted nonaligned triples
holds in a specified initial sublevel. Define from the data alone

\[
 \ell_* =\min\big(\{1\}\cup\{\ell_{ij;k}:(i,j;k)\in E\}\big)>0.\tag{18}
\]

Under (4) conditioned on L(theta_0)<ell_*, convergence in H implies fitting
almost surely. This follows from monotonicity: a positive limit below
ell_* cannot belong to (17). The conditioning event has positive probability,
because an explicit fit and an open fitting neighborhood exist by Section 7.
It supplies no proof that the canonical loss-one trajectory enters this
sublevel. For balanced binary class masses, each possible exceptional value
is at least 1/2: writing the two positive masses as a,1/2-a and the negative
mass as 1/2 verifies this directly in (12), for either a same-label or a
mixed-label pair. Thus L(theta_0)<1/2 is one sufficient balanced sublevel
for every nonaligned triple.

A separate extension keeps every positive weighting and every nonaligned
triple and allows arbitrary H initial states and H convergence, but asks only
that the limiting lower displacement w_*-g be essentially bounded. Its bad
basin is null by `dependent_basin_functional.md`; c_* may be merely L2.
For triples this also follows from (10): a two-point input-plane projection
cannot differ by a bounded amount from the Gaussian projection. This is an
endpoint restriction, not a conclusion of H convergence or finite-time bounds.

The functional report additionally proves this bounded-lower-endpoint basin
theorem for any finite input list in R^d with at most one independent linear
relation, dim ker[u_1 ... u_m]<=1. On the relation's support the same sign
argument gives a fixed ratio of two gates; Gaussian tail balls contradict it
under bounded lower displacement. Outside the support all coefficients
vanish directly. Its complete finite-family negative-curvature proof and
rank bound (3d+1)m+2d^2 verify the remaining graph hypotheses. It includes
m=d+1 configurations and is not restricted to three samples.

## 7. Arbitrarily many finite samples: an open exponential fitting basin

`dependent_finite_fitting.md` proves, for every finite compatible law and
fixed d>=2, initialized effective-vector injectivity modulo sign and linear
independence of its upper nonlinear features. The scalar coordinate map
D a_0(x)=(T(u_1),...,T(u_d)) is strictly increasing coordinatewise, retaining
the full reverse response and actual ridge. Hence

\[
 K_{ij}=E_2[H_i^0H_j^0]\succ0,\quad
 c_*=\sum_i(K^{-1}y)_iH_i^0,\quad \theta_*=(0,c_*,D)
\tag{19}
\]

is an explicit fitted state for any finite number of samples, even m>d.
With gamma=lambda_min(P^(1/2)KP^(1/2))>0, that report gives explicit positive
rho,C and the nonempty H-open forward-invariant region

\[
 U=\{\theta:\|\theta-\theta_*\|_H+(C/\gamma)\sqrt{L(\theta)}<\rho\}.
\]

Every exact full-flow trajectory in U obeys

\[
 L(t)\le L(0)e^{-2\gamma t},\qquad
 \|\theta(t)-\theta_\infty\|_H
 \le(C/\gamma)\sqrt{L(0)}e^{-\gamma t},\qquad L(\theta_\infty)=0.
\tag{20}
\]

The proof protects the current readout Gram by a first-exit/finite-length
argument; it does not assume its future conditioning. All blocks are trained.
The same initialized nonlinear-feature proof extends the exact attained odd
architectural floor to every finite law. No raw input-rank obstruction to
finite fitting remains. The center c_* differs from canonical c=0, so (20)
is not a global initialized convergence result.

## 8. Genuine remaining issues and a checked obstruction

The unrestricted unequal-weight reflection case remains open at the
point-convergent basin level. The difficulty is concrete. Section 4 of
`dependent_hilbert_geometry.md` constructs exact 0<L<1 equilibria with

\[
 u_1=(C,S),\ u_2=(C,-S),\ u_3=(0,1),\quad C,S>0,\ C^2+S^2=1,
\]

binary labels (+1,-1,+1), p_1!=p_2, and projected lower field
w=a sign(q dot b_1)e_1. A bounded readout realizes three explicit moments,
all three block gradients vanish, and the loss is (12). The individual T_i
are nonzero. Concentrated odd lower perturbations give a loss remainder of
order ||delta w||_2^2 that does not approach its directional quadratic form;
the loss has no second Frechet differential there. The state still has a
negative bounded directional variation. This rules out simply asserting the
old finite-rank Hilbert Hessian everywhere, not a possible stronger null-basin
theorem by a different argument. These are ambient states, not proved reached
from the canonical initialization or from a positive-probability set.

For many finite inputs with several independent relations, an unrestricted
bad-basin theorem is still open. The finite open fitting theorem (20) does
not settle it. For genuinely infinite-support input laws, even positivity
of all finite feature Grams does not supply an infinite-dimensional spectral
gap or an exact square-integrable interpolant. No limit in sample count is
used to assert either property.

As before, all null-basin statements require a full state limit; they do not
exclude positive-loss escape or nonconvergent population motion. They do not
place the deterministic canonical state outside a null exceptional set.
No exponential rate is inferred merely from almost-sure conditional fitting;
the explicit exponential assertion is for the separately constructed U.
