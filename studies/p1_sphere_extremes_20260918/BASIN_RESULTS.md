# Positive-loss basins: a proved thinness theorem and its exact limit

Date: 2026-09-18. This synthesizes the user's backward-basin proposal for
the same weighted three-input p=1 investigation. It does not claim complete
canonical initialized fitting. Complete component arguments are in the
named own-study reports; the integrated internal check is recorded in
review_basin_framework.md. No experiment or finite-particle substitution.

## 1. Exact target and scope

Fix any three independent x_i in sqrt(3) S^2, positive probability
weights p_i, and binary labels y_i. Keep the canonical correlated
Gaussian-derived marks, ridge 1/4096, phi=tanh, full trainable M and its
actual transpose, all trainable blocks, physical time and the unhalved
square loss. These data have no coincidence or antipodality conflict.

On the exact fixed carriers use displacement coordinates

\[
 \theta=(w-g,c,M),\qquad
 \mathcal H=L^2_{\rm odd}(\Omega_1;\mathbb R^3)
 \oplus L^2_{\rm odd}(\Omega_2)\oplus\mathbb R^{3\times6}.
\]

The Hilbert norm is the physical population norm. The exact field has
a global forward flow Phi_t on H, agreeing with the original flow for
bounded-field starts. This is proved directly from the same equations
and energy identity in basin_spectral_route.md, Section 2.

Distinguish

\[
 \mathcal B_+=\{\theta_0:\Phi_t(\theta_0)\to\theta_*
       \text{ in }\mathcal H,\quad 0<L(\theta_*)<1\}
                                                        \tag{1}
\]

from the positive-limit-loss problem within the initial sublevel L<1,

\[
 \mathcal P_+=\{\theta_0:L(\theta_0)<1,\quad
                    \lim_{t\to\infty}L(\Phi_t\theta_0)>0\}. \tag{2}
\]

Loss always has a limit. State convergence has not been proved for all
trajectories. The theorem below concerns (1), including limiting fields
which are square integrable but not essentially bounded.
Precisely, B_+ intersected with {L(theta_0)<1} is a subset of P_+.

## 2. What is proved

**Basin theorem.** B_+ is contained in a countable union T of closed
Lipschitz hypersurfaces in H. Thus B_+ is meagre and has probability zero
under an explicitly defined full-support Gaussian law on H, all its
translations and all its positive rescalings. T also has an arbitrarily
small compactly supported translation-null probability witness: it is
shy. Locally at each bad equilibrium the trapping graph has finite
positive codimension k with 1<=k<=48.

There are actual nonstationary trajectories in these bad basins. Near
each bounded-field bad equilibrium with 0<L_*<1 there is a positive-
dimensional strong stable graph. Small nonzero starts on it converge
exponentially to that equilibrium and their loss strictly decreases to
L_*. Such equilibria exist for every independent triple, every positive
weighting and every binary labeling by the prior exact construction.
These are different initial states, not canonical initialized failures.

There is also a nonempty open fitting region for every independent
triple in the same physical Hilbert space H. Every start in it fits
exponentially and converges in H to a fitted state. A separate open
region in the exact continuous-carrier space has convergence in the
stronger supremum/Frobenius norm. Both regions are constructed explicitly
and their forward invariance is proved; no future Gram or endpoint
hypothesis is assumed.

T is a thin **superset** of the convergent bad basin. Not every point of
T is asserted to converge badly. In contrast, the strong stable graphs
are actual subsets of bad basins with convergence proved.

## 3. Finite curvature in the exact population space

Write u_i=x_i/sqrt(3), a_i=E_1[b_1 phi(w.u_i)], v_i=Ma_i,
H_i=phi(b_2.v_i), r_i=E_2[cH_i]-y_i and
d_i=E_2[b_2c phi'(b_2.v_i)]. At an equilibrium, independent inputs,
positive lower gates, and the positive lower mark Gram give

\[
                         p_i r_i M^T d_i=0
                         \quad(i=1,2,3).                 \tag{3}
\]

This cancels the only local multiplication term in the lower Hessian.
The remaining curvature factors through 18 lower gate/mark functions,
12 upper feature/derivative functions, and 18 matrix coordinates. The
physical Hessian is self-adjoint with rank at most 48. Its nonzero
spectral spaces are finite dimensional; its kernel is infinite dimensional.

Every Hilbert equilibrium with 0<L<1 has negative curvature. The proof
in basin_hilbert_landscape.md uses dual inputs and
K_i=E[b_1b_1^T phi'(w.u_i)]>0 to change just one lower contraction in an
arbitrary direction by a bounded variation. Its upper derivative feature
lies outside the span of the current tanh features; a mixed lower/readout
perturbation gives strict negative curvature. No boundedness of the
limiting fields is required. A pure readout variation supplies positive
curvature, since some H_i is nonzero when L<1. M=0 is excluded at those
loss levels because it gives zero predictions and loss one.

Thus the gradient-flow linearization has both attracting and repelling
directions, together with infinitely many neutral directions. The latter
are real: any bounded readout function orthogonal to all H_i and all
b_{2,j} phi'(b_2.v_i) can be added to a critical state without changing
its predictions, backward vectors or stationarity. "Lower dimension"
therefore means positive codimension, not finite dimension.

## 4. Backward reconstruction of a thin basin cover

The nonlinear graph construction is contained in basin_spectral_route.md.
Near a critical point the exact field satisfies

\[
 \dot z=A z+N(z),\qquad
             \operatorname{Lip}(N\text{ on }B_r)\le C r.  \tag{4}
\]

This estimate is valid in H even though the lower gate map need not
be Frechet differentiable on an H-neighborhood. Equation (3) makes its
problematic gate variation multiply a finite coefficient vanishing at
the equilibrium. The resulting remainder has precisely the small
Lipschitz constant in (4).

Split into unstable and center-stable spectral coordinates. After a
small radial retraction of the remainder, solve

\[
 \begin{split}
 z_{cs}(t)&=e^{A_{cs}t}\xi+
       \int_0^t e^{A_{cs}(t-s)}N_{cs}(z(s))\,ds,\\
 z_u(t)&=-\int_t^\infty e^{A_u(t-s)}N_u(z(s))\,ds.
 \end{split}                                            \tag{5}
\]

In an exponentially weighted path norm this is a contraction. It defines
a Lipschitz graph z_u(0)=h_*(xi) with positive finite codimension. Every
orbit trapped in the original small neighborhood lies on this graph:
the terminal unstable term in variation of constants vanishes when
sent to infinite time. All constants and the fixed-point equation are
determined by the equilibrium and the actual vector field.

Choose countably many smaller neighborhoods covering all equilibria
with 0<L<1, with translated trapping graphs G_j on their larger
neighborhoods. Separability of H gives this cover even for an uncountable
equilibrium set. Any convergent bad trajectory eventually stays in one
larger neighborhood, so for an integer n,

\[
              \mathcal B_+\subseteq
              \bigcup_{j\ge1,\ n\ge0}\Phi_n^{-1}(G_j).    \tag{6}
\]

This is the backward construction as an outer bound. The endpoint
need not be the selected neighborhood's center. Finite inverse flow is
used only on its open image; global negative-time existence is unnecessary.

Each positive-codimension graph lies in a scalar Lipschitz hypersurface.
Their time-map preimages also admit countable hypersurface covers. The
last step uses the exact strong Gateaux regularity established in
basin_hilbert_null_extension.md: the time-map derivative is invertible
and continuous on each fixed direction. Along a chosen transverse
direction this implies a strict scalar slope on a small product
cylinder; local Lipschitzness controls the other coordinates. This
proves the pulled-back scalar graph property without falsely assuming
Frechet C1 regularity on H. The resulting countable closed hypersurface
union is T.

Using decaying path weights in (5), with stable rather than center-stable
coordinates prescribed, constructs actual strong stable trajectories.
Small nonzero stable coordinates stay in the original equation and
converge exponentially. Uniqueness prevents hitting an equilibrium at
a finite time. The energy identity therefore gives strict loss descent
to the chosen positive loss. At the explicitly constructed continuous
bad states this proof also runs in the continuous-carrier norm.

## 5. A legitimate meaning of probability zero

Choose bounded odd directions e_n with unit H norm, dense in the unit
sphere of H, including matrix directions. With the sum of the two
essential-supremum norms and Frobenius norm denoted by ||.||_b, define

\[
 a_n=\frac{2^{-n}}{1+\|e_n\|_b},\qquad
 Z=\sum_{n\ge1}a_n g_n e_n,\qquad
 g_n\text{ independent }N(0,1).                         \tag{7}
\]

The series converges absolutely in bounded-field norm almost surely,
and its law has full support in H. Every Lipschitz hypersurface has an
open cone of directions whose parallel lines meet it at most once.
Choose an e_n in that cone, and condition on all other coefficients.
An atomless scalar g_n hits the possible single intersection with
probability zero. Fubini and countable subadditivity give

\[
 \Pr\{\theta_{\rm ref}+\varepsilon Z\in\mathcal B_+\}=0
 \quad(\theta_{\rm ref}\in\mathcal H,\ \varepsilon>0).    \tag{8}
\]

Replacing g_n by independent uniforms on [-1,1] gives the compact
translation-null witness. Scaling makes that perturbation uniformly
arbitrarily small. No infinite-dimensional Lebesgue measure is presumed.
The measurable F_sigma hull T gives outer probability zero even if the
basin itself is not measurably specified. Conditioning the Gaussian on
a nonempty open Hilbert constraint such as L(theta_0)<1 retains nullity.
Complete proofs are in basin_probability_route.md Sections 1--5 and
basin_hilbert_null_extension.md; the former's activation-zero Section 6
is not used.

Canonical population initialization is the deterministic point (0,0,D).
Its neuron-level Gaussian marks have already been integrated into the
state. Equation (8) is a different experiment: it perturbs the population
fields themselves. Epsilon>0 cannot be replaced by zero. Randomizing only
M, or restricting the initialization to c=0, requires a separate verified
transversality argument and is not automatically covered.

## 6. A nonempty open fitting basin

The exact continuous-carrier space X is constructed in
basin_continuous_carrier.md. It is separable, contains canonical finite-
time states and the explicit bad states, and has the exact smooth flow.
It compactifies the frozen carrier without truncating the Gaussian law:
retain z_i^0=phi(g.u_i) and use the exact addition formula
phi((g+v).u_i)=(z_i^0+tanh(v.u_i))/(1+z_i^0 tanh(v.u_i)).

The moment-realization lemma constructs a bounded continuous displacement
with a_i=kappa e_i in R6. Set M=kappa^{-1}[I_3 0]; then the three
upper features are phi(b_{2,i}), independent, centered, and with common
positive variance beta. The readout c=beta^{-1} sum_i y_i phi(b_{2,i})
fits all labels. Call this complete state theta_*.

Explicit constants rho,C and gamma=beta min_i p_i in
basin_open_fitting.md prove throughout the known radius-rho ball

\[
 L'\le-2\gamma L,\qquad \|\dot\theta\|_X\le C\sqrt L.
\]

The nonempty open set

\[
 \mathcal U=\{\theta:\|\theta-\theta_*\|_X+
                         (C/\gamma)\sqrt{L(\theta)}<\rho\}
\]

is forward invariant by a first-exit argument. Every start in U satisfies

\[
 L(t)\le L(0)e^{-2\gamma t},\qquad
 \|\theta(t)-\theta_\infty\|_X
          \le(C/\gamma)\sqrt{L(0)}e^{-\gamma t},
 \qquad L(\theta_\infty)=0.
\]

The union of finite-time backward images of U is a larger open fitting
basin. No future Gram bound is assumed. This does not assert that U
exhausts the complement of T or contains canonical initialization.
The complete extension in basin_hilbert_fitting.md proves the same
inequalities with H replacing X and the same fitted center and constants.
The reason is explicit: the lower moment map is Lipschitz in L2,
||c||_2 controls every d_i, and the physical state speed is bounded by
the sum of the three block speed bounds. Thus

\[
 \mathcal U_H=\{\theta:\|\theta-\theta_*\|_H+
                         (C/\gamma)\sqrt{L(\theta)}<\rho\}
\]

is a nonempty H-open forward-invariant fitting region. Every start in
it fits exponentially and converges to a fitted endpoint in H. This
places open fitting attraction in the same topology as the thin bad
basin theorem. The X version additionally proves stronger endpoint
convergence and is retained separately.

## 7. Exact unresolved implications

The full positive-limit-loss set P_+ in (2) is not proved null. Its
trajectories with an H limit are covered, but positive-loss escape,
bounded nonprecompact motion, and approach to a continuum of equilibria
without point convergence remain unexcluded. A compact totally
disconnected bad set is covered when distance to it tends to zero:
precompactness and connectedness of the omega-limit then force a point
limit. An arbitrary compact continuum is not automatically covered.

The global dissipation budget does give displacement o(sqrt(t)); a
readout identity fixes time-averaged prediction norm and label correlation
at 1-L_infinity. These exact estimates in basin_escape_route.md still
permit unbounded subdiffusive escape. That report also constructs bounded,
noncompact families of stationary readouts, showing why bounded norms or
a finite dictionary alone do not supply population-state compactness.
Those families are not nonconvergent canonical trajectories.

Even proving P_+ null under (7) would not decide membership of the single
canonical point. A deterministic initialized-trajectory exclusion and
a no-limit/escape exclusion remain necessary for the original complete
configuration-only plateau classification.

## 8. Proof and checking record

Independent spectral, global-bound and probability routes froze before
comparison; the lead's continuous-carrier candidate also froze before
comparison. The Hilbert-landscape extension, strong Gateaux globalization
and open-fitting construction are explicitly recorded as follow-ups.
The complete source packets and hashes, component checks and final
integration verdict are in review_basin_framework.md and the README.
The global-bound report is separately lead checked; it is not a premise
of the basin thinness theorem. These are internally checked study
results, not promoted book material.
