# A common Hilbert realization of all finite response programs

2026-10-07. Lead construction. This supplies a consistency bridge between
the finite Gaussian-response laws and a potential continuous-time theory.
It does not assert existence, uniqueness, or approximation for a continuous
flow. It is not proposed as the final explanatory model: its bounded
operators are a mathematical realization of the response law, not new
mechanistically transparent state variables.

## 1. Inputs and the exact claim

Fix finitely many neuron populations, Gaussian matrix interfaces, activations
with bounded real derivative and bounded Lipschitz derivative gate, and a
finite input dimension. Use the qualitative finite-program law established
in UNCLIPPED_FINITE_HISTORY.md. Its inner-product limits are deterministic
and its row operations include scalar linear combinations, Lipschitz
functions and bounded Lipschitz gates times row fields.

There exist probability spaces for the neuron populations and bounded
operators between their \(L^2\) spaces which realize every prescribed finite
neural response program in one common model. Each Gaussian interface is
realized by an operator \(G\), its transpose by the Hilbert adjoint \(G^*\),
and \(\|G\|\le8\). Scalar activations and derivative gates act pointwise.
Initial first-layer Gaussian linear fields satisfy
\[
\langle A_0v,A_0u\rangle=v^\top u.
\]
For every finite program, the realized inner products and outputs equal the
deterministic limits of its finite-width counterparts.

The operator norm eight is a safe elementary Gaussian bound, not an optimal
spectral-edge assertion. The claim covers a countable generating program
family and its continuous \(L^2\) extensions. It does not posit a finite
description of the resulting infinite-dimensional spaces or operators.

## 2. Countable joint construction

Start with the finitely many scalar initial Gaussian root coordinates in
each population and constant-one fields. Close a countable formal instruction
list under rational linear combinations, the designated activations and
gates, bounded piecewise-linear scalar functions with finitely many rational
breakpoints and values and bounded tails, and the named matrix/transpose queries. Include gated products
with these bounded scalar functions. Include the finite collection of
actual data constants and coefficient maps needed by any specifically
prescribed neural program. Enumerate instructions so that every instruction's
dependencies precede it; interleave the countably many finite constructions.
Registers and their dependencies are named and immutable; different neural
runs have distinct state registers but share the named initialized matrices.
Thus inserting another run's instructions does not change a preceding
instruction's scalar coefficient map or its declared arguments.

Execute the scalar Gaussian-history recursion on this infinite enumeration.
At every finite prefix there are only finitely many retained histories;
its deterministic moment coefficients are already defined by preceding
laws. A fresh standard Gaussian innovation is available for every retained
query in its target population. Thus all row fields are concrete measurable
functions of one countable independent Gaussian sequence for that population.
Only finite prefixes are evaluated to define any one row field.

For each finite prefix, the finite-program theorem identifies all its joint
empirical laws and moments with those concrete variables. If two constructions
compute the same finite-width field by different algebraic paths, their
joint limiting squared difference is zero. Adding unrelated intermediate
instructions cannot change the limiting joint law of earlier fields: the
underlying finite-width computation of those fields is unchanged, and its
limit is unique. This proves the consistency needed below; no unjustified
order independence of the regression coefficients is assumed.

Let \(H_\ell\) be the closed linear span of all generated scalar fields in
population \(\ell\), with norm \(\|u\|^2=\mathbb E u^2\). Null fields are
identified. It is enough initially to work with these closed subspaces of
the Gaussian probability spaces.

## 3. Why initialized actions extend to bounded adjoint operators

For finite rational linear combinations \(u,v\) in a source population, include the
queries \(Gu,Gv,G(u+v)\) in one finite program. The finite-width identity
\(G_n(u_n+v_n)=G_nu_n+G_nv_n\) implies
\[
\mathbb E|G(u+v)-Gu-Gv|^2=0.
\]
Scalar linearity follows the same way, first for rational coefficients.
Thus the formal action is linear in \(L^2\).

The elementary Gaussian net bound gives
\(\mathbb P(\|G_n\|_{\rm op}\le8)\to1\). The finite-program theorem gives
deterministic limits for both squared norms in
\[
\|G_nu_n\|_{2,n}^2\le64\|u_n\|_{2,n}^2.
\]
Consequently \(\|Gu\|^2\le64\|u\|^2\): if the limiting inequality failed,
convergence in probability would contradict its finite-width high-probability
version. In particular a null input has a null image. The action therefore
descends to the quotient by null fields and extends uniquely, with norm
at most eight, to the complete space \(H_{\ell-1}\). Its image is in
\(H_\ell\) by construction.
Real linearity follows on this completion by approximating each real scalar
by rationals.

For generated fields \(u,v\) on adjacent populations, the exact identity
\[
\langle G_nu_n,v_n\rangle_n
=\langle u_n,G_n^\top v_n\rangle_n
\]
passes to deterministic limits. Boundedness and density extend it to all
\(u,v\), so the transpose-query realization is exactly the adjoint \(G^*\).
This does not require any history inverse or positive history gap.

Similarly the first-layer root fields are a standard Gaussian vector with
\(d\) coordinates. Their scalar linear combinations give the isometry
\(A_0:\mathbb R^d\to H_1\) stated in Section 1.

## 4. Pointwise nonlinear operations extend consistently

If \(\phi\) is Lipschitz, then
\[
\|\phi(u)-\phi(v)\|_2\le\operatorname{Lip}(\phi)\|u-v\|_2.
\]
It therefore extends from generated fields to their \(L^2\) closure, with
the same pointwise meaning. Constants belong to the space, so nonzero
activation intercepts present no problem.

For a bounded Lipschitz gate \(a\), the map \((u,v)\mapsto u a(v)\) is
continuous from \(L^2\times L^2\) to \(L^2\), though generally not globally
Lipschitz. To see this, use the one-sided inequality
\[
\begin{aligned}
\|u a(v)-\widetilde u a(\widetilde v)\|_2
\le{}&\|a\|_\infty\|u-\widetilde u\|_2\\
&+R\operatorname{Lip}(a)\|v-\widetilde v\|_2
+2\|a\|_\infty\|\widetilde u\mathbf1_{|\widetilde u|>R}\|_2.
\end{aligned}
\]
For approximation of a fixed target \((\widetilde u,\widetilde v)\), first
fix \(R\), then pass to the \(L^2\) limit, then let \(R\to\infty\).
The reference square tail tends to zero by integrability. Thus the gated
product belongs to the closure and agrees with its pointwise definition.

One can identify \(H_\ell\) with the whole \(L^2\) space of the sigma-field
generated by its scalar fields. Here is why the needed density is available.
Clip finitely many generated fields using the included bounded piecewise-linear
maps. Finite products of the clipped fields belong to \(H_\ell\), because
the identity on a bounded interval has a bounded Lipschitz extension and
each product is an allowed gated product. Polynomial approximations on
compact cubes, for example their explicit Bernstein approximants, then
approximate continuous functions of any finite clipped list. Approximating
indicator functions of intervals outside their arbitrarily small boundary
strips gives the associated cylinder indicators in \(L^2\), choosing interval
endpoints outside atoms. Finite-coordinate cylinder functions are dense in
the generated sigma-field, by successive conditional expectations or the
elementary monotone-class argument. This supplies the claimed identification.
No pointwise multiplication of two arbitrary unbounded \(L^2\) functions
is asserted to remain in \(L^2\).

The construction also identifies a prescribed finite program with new real
constants not in the initial countable language. Enlarge that language by
its finitely many constants and instructions. Finite-prefix compatibility
gives an isometry between the old generated spans in the two realizations.
It preserves the bounded operators and continuous pointwise operations.
The old completed space already contains real multiples of its constant
field and is closed under these operations. Induction places every new
program field in its image, with the finite-width limit identified by the
enlarged construction. No uncountable syntactic enumeration is claimed.

## 5. Interpretation for the nonlinear training equations

In this realization the width normalization is absorbed into the probability
inner products. A learned hidden increment is a Hilbert--Schmidt operator
\(B_\ell\), added to its fixed initialized operator \(G_\ell\). The readout
\(w\) belongs to the top population's \(L^2\) space, and the first layer is
an operator \(A:\mathbb R^d\to H_1\). On the declared panel,
\[
\begin{aligned}
z_{1,a}&=Av_a,&h_{\ell,a}&=\phi_\ell(z_{\ell,a}),\\
z_{\ell,a}&=(G_\ell+B_\ell)h_{\ell-1,a},&
f_a&=\langle w,h_{L,a}\rangle,\\
\delta_{L,a}&=w\phi'_L(z_{L,a}),&
\delta_{\ell,a}&=\phi'_\ell(z_{\ell,a})
(G_{\ell+1}+B_{\ell+1})^*\delta_{\ell+1,a}.
\end{aligned}
\]
Only \(a\le m\) has \(c_a=y_a-f_a\). The candidate continuous equations are
\[
\dot A=\frac2m\sum_{a\le m}c_a\,\delta_{1,a}\otimes v_a,\qquad
\dot B_\ell=\frac2m\sum_{a\le m}c_a\,\delta_{\ell,a}\otimes h_{\ell-1,a},
\qquad
\dot w=\frac2m\sum_{a\le m}c_a h_{L,a}.
\tag{1}
\]
Here \(u\otimes v\) maps \(z\) to \(u\langle v,z\rangle\); its
Hilbert--Schmidt norm is \(\|u\|_2\|v\|_2\). Initially \(B_\ell=0,w=0\).

Every fixed finite Euler computation of (1) exists algebraically and is
exactly the scalar aggregate law already proved. All quantities are obtained
by the finite allowed operations. In particular, this gives a common
bounded-operator realization of the finite laws as the mesh is refined:
one does not have to assume separately compatible unrelated limiting laws
for each mesh.

Equation (1) is not claimed here to be a well-posed continuous ODE.
Its vector field is continuous in the natural Hilbert norm, but continuity
alone neither guarantees existence in an infinite-dimensional space nor
uniqueness. The gated product estimate shows precisely the missing modulus.
Uniform sub-Gaussian carrier control could supply an Osgood modulus and a
controlled Euler limit; proving that control on the full admitted label range
remains separate.

Eliminating the increments \(B_\ell\) from (1) gives the two-time
feature/backward memory identities. Their Gaussian response formulation is
the intended interpretable description. The operators in this note are a
consistency tool, not hidden finite matrices supplied by an oracle, and not
a substitute for proving the autonomous observable closure and its all-time
comparison theorem.

Scoped internal audit: RESPONSE_HILBERT_AUDIT.md checked the original frozen
construction. The finite-description, named-register, rational-linearity and
real-constant extension clarifications above incorporate its recommendations.
Its verdict does not cover a continuous-time theorem.
