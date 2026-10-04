# Reconstruction of the three strict-rate attempts

2026-10-03. Coordinator reconstruction of the complete three scoped
route notes, including their final additions. This is a collaborative
internal mathematical check, not an isolated promotion review.
The coordinator suggested the second-order Gaussian inequality, the
augmented adjoint cavity, and the near-root fallback, and exchanged
specific findings after the initial separate attempts.

| Complete checked source | SHA-256 |
|---|---|
| SELF_AVERAGING_FEEDBACK_ROUTE.md | b3709cac57c005b209dbcaf084848987ee4fe824de0f798d596db8caf6c3554a |
| SELF_AVERAGING_SENSITIVITY_ROUTE.md | e8854ee58b74f40b10f39e7610cd7c7a258222765f7867e503734897329b65c9 |
| SELF_AVERAGING_ENERGY_ATTEMPT.md | 7a8c34172cbd78b57d8a8fcd615a9e143f67fe22967e976d6b2709da03c656b1 |

**Outcome:** the stated exact identities and deterministic conditional
implications reconstruct. None of these notes closes the strict
general-data independent-copy root-width theorem. The separate
near-root theorem in GENERAL_SELF_AVERAGING.md has its own complete
check in SELF_AVERAGING_CHECK.md.

## 1. Coordinates, residual adaptation, and directed sensitivity

In mobility-Euclidean coordinates
\(\Theta=(W^1,\sqrt nW^2,\ldots,\sqrt nW^L,w)\),
write \(\mathcal F_a=nf_a\), \(g_a=\nabla\mathcal F_a\),
\(H_a=D^2\mathcal F_a\), and let the positive sample weights
\(p_a\) sum to one. The actual flow is
\[
 F(\Theta)=-2\sum_a p_a r_a g_a,\qquad
 DF=-{2\over n}\sum_a p_a g_ag_a^\top
                         -2\sum_a p_a r_aH_a.
\]
The factor \(1/n\) in the negative Gram is necessary and present.
It comes from \(D r_a=g_a/n\). The Gaussian root vector has
independent standard coordinates in every initialized block except
the exactly zero readout. For its isometric embedding \(P\),
\[
 \nabla_G f_x(t)=P^\top J(t,0)^\top g_x(t)/n.
\]
Consequently the root-width variance target needs an \(O(n)\)
squared norm for this particular vector before division by \(n^2\).
Normalized Hilbert--Schmidt or fixed Schatten norms of \(J-U_0\)
cannot replace this directed estimate. Both notes give valid abstract
rank-one examples, explicitly separated from actual neural
counterexamples.

## 2. First and second Gaussian derivatives

The extension of the residual-Hessian Dyson estimate to any fixed
Schatten exponent \(p\) is valid: \(h\) insertions use exponent \(ph\),
the ordered time simplex gives \(1/h!\), and the moment term is bounded
by a geometric series when \(CpS^2<1\). A finite choice such as
\(p=2,4,6\) permits one fixed positive label threshold.
The contraction itself must stay in operator norm; its identity part
has ambient dimension of order \(n^2\).

For the prediction Hessian, the chain rule has both
\[
 n^{-1}P^\top J^\top H_xJP
 \quad\hbox{and}\quad
 n^{-1}\int P^\top J_s^\top A_{v_s}J_sP\,ds,\qquad
 v_s=J(t,s)^\top g_x(t).
\]
The first has Hilbert--Schmidt norm \(O(n^{-1/2})\) under the
explicit additional query-carrier budget, by the \(2,4,6\) Schatten
bounds. That query budget is not assumed as a completed theorem.

Direct differentiation verifies the second term's coefficient:
\[
 A_v=-2\sum_a p_a\left[
 {g_a(H_av)^\top+(H_av)g_a^\top+(g_a^\top v)H_a\over n}
                  +r_aD^3\mathcal F_a[v,\cdot,\cdot]\right].
\]
In particular it contains a carrier multiplied by a forward directional
response. The mixed moment displayed in the source is necessary for
that bound and is not controlled by a marginal carrier budget.
The second-order Gaussian inequality also retains its mean-gradient
term. Thus no second-order completion is being claimed.

## 3. Adjoint energy and entropy

For \(q(s)=J(t,s)^\top g_x(t)\), the exact equation is
\(\partial_s q=-DF(s)^\top q\). Its integrated energy is
\[
 \|q(s)\|^2+2\int_s^t\|\mathsf L^\top q(u)\|^2\,du
 =\|g_x(t)\|^2
  -4\int_s^t\sum_a p_a r_a(u)q(u)^\top H_a(u)q(u)\,du,
\]
where \(\mathsf L=\sqrt{2/n}[\sqrt{p_a}g_a]_a\).
The Gram term is dissipative in backward elapsed time.
Projection onto initialized blocks creates the stated mixed Gram and
Hessian terms; it does not preserve this sign by itself.

For a layer response \(u\), write
\(\pi_i=u_i^2/\|u\|^2\) when \(u\ne0\).
The finite relative-entropy variational inequality gives exactly
\[
 \sum_i|k_i|u_i^2
 \le {S\|u\|^2\over\eta}
 \left[\log B+\sum_i\pi_i\log(n\pi_i)\right]
\]
from \(n^{-1}\sum_i e^{\eta|k_i|/S}\le B\).
This follows by comparing \(\pi\) with the probability vector
proportional to \(e^{\eta|k_i|/S}\); it is not a probabilistic
independence assertion. The zero vector is handled by zero contribution.
Its application to \(u=D_\Theta z_a^\ell q\) and backward Gronwall
proves the stated conditional energy bound.
The uniform entropy estimate remains unproved. An exchangeable
randomly located spike confirms that exchangeability alone is
insufficient.

Differentiating \(a_x=P^\top J^\top g_x\) gives
\[
 \dot a_x=-{2\over n}\sum_a p_a(g_a^\top g_x)a_a
          -2\sum_a p_a r_aP^\top J^\top(H_ag_x+H_xg_a).
\]
Both Hessian-gradient terms have the displayed sign. They do not
cancel. The first term requires damping of training sensitivities,
not just decay of the residual values.

## 4. Augmented deletion and its time qualification

The forward directional recursion \(\alpha=Dz\,v\), gate response
\(\eta=\phi'\alpha\), and reverse recursion \(\beta=D\delta\,v\)
are obtained by ordinary product differentiation. All factors
\(1/\sqrt n\) attached to \(v_H\) are correct. Differentiating the
omitted forward source \(x_i h_i\) and reverse source \(y_i\delta_i\)
produces both scalar response controls and the omitted response
row/column. The lower reverse source additionally has the stated
Hessian term with \(y_i\) held fixed and a separate derivative of
that row. No term can be omitted by calling the Gaussian roots
independent after training.

The omitted adjoint column has a terminal bound proportional to
\(n^{-1/2}|h_{x,i}|\,\|\delta_x\|_2/\sqrt n\).
Its subsequent equation contains a term
\(\chi_a\delta_a h_{a,i}/n\), with
\(\chi_a=g_a^\top v/n\), as well as the two residual-weighted
terms. The coordinator requested one qualification: a pointwise
bound on \(\chi_a\) is not enough to integrate this term uniformly
over arbitrarily long backward intervals.
The final source's equation (26a) now retains its integral explicitly,
and lists the needed integrability or damping as open.

The conditional small-label mechanism is correctly limited:
if a scalar estimate produced a factor \(e^{CSK_i}\), its fixed
\(p\)-th empirical moment would be bounded by the known carrier
budget when \(CpS^2<\eta\). The adapted mixing operations in the
actual response system have not been reduced to that scalar estimate.
The terminal-value cavity and its sources also require a new proof.
Possible extra activation derivatives in a naive Taylor construction
are acknowledged rather than silently assumed.

The resampling note correctly needs \(O(n^{-2})\) expected squared
prediction influence for each of \(O(n)\) independent row blocks.
A generic state remainder \(n^{-c}\), paired with a gradient of size
\(\sqrt n\) and divided by \(n\), gives only \(n^{-1/2-c}\)
prediction error. Its squared block sum is \(n^{-2c}\), which is
insufficient for \(c<1/2\). This is an insufficiency of that estimate,
not a neural lower bound.

## 5. Controlled feedback and the near-root input

The two-initialization proof subtracts two actual fitting paths.
Forward differences, one-reference backward differences, residual
damping, and Gronwall against finite residual activity give
\[
 \sup_t D(t)\le Ce^{CS(1+M)}D(0).
\]
No interpolating path is assumed good. The initialization scaling
\(D(0)\le C_L\|G-G'\|/\sqrt n\) and the linear query growth
are correct, including for unbounded activation values.
This proves the global good-set Lipschitz property used in the
near-root concentration theorem.

For controlled paths \(d\Theta=\sum_a g_a\,db_a\), integration by
parts gives the exact variation identity
\[
 \partial_\theta\Theta(t)=\sum_a g_a(t)e_a(t)
 -\sum_{a,c}\int_0^t J(t,s)
       (H_ag_c-H_cg_a)(s)e_a(s)\,db_c^\theta(s).
\]
The sign follows from
\(d_s(J(t,s)g_a(s))=\sum_cJ(H_ag_c-H_cg_a)\,db_c^\theta\).
The physical tube supplies the absolute cubic remainder and the
quadratic perturbation of the tangent pairing. It does not supply
the scalar commutator-response estimate needed for two-control
Lipschitz stability in general.
For one effective vector field, its self-commutator vanishes exactly,
so the claimed strict one-direction controlled-feedback special case
does follow. It is not an initialization-concentration theorem.

Finally, the Poincare/Minkowski all-time implication in both sensitivity
notes is correct under the explicitly stated global derivative and
integrability hypotheses. A pointwise variance estimate, a derivative
bound only on a good set, and the full-time supremum are distinguished
throughout. Those distinctions prevent these partial routes from being
misreported as the missing strict theorem.

No numerical experiment, manuscript edit, or Git write was part of this
reconstruction.
