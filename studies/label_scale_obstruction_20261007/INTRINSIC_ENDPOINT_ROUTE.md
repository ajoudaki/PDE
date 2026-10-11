# Conditional rank-free endpoint coercivity

Status: two complete conditional lemmas from a bounded theoretical attempt, pending independent review. Neither lemma constructs or identifies the correlated Gaussian population dynamics. The required root-conditional bound in Lemma 1 is not proved for the actual trained network. Lemma 2 removes that bound from the endpoint-coercivity step for permutation-symmetric regular-simplex reference states, but does not construct those reference paths or establish finite-width fitting. No experiments were used, and no frozen earlier file was modified.

Scientific inputs were the supervisor's model and the previously authorized complete same-study notes `GAUSSIAN_NONORTHOGONAL_EXTENSION.md` and `GAUSSIAN_POSITIVE_GEOMETRY.md`. The qualitative analytic-minor statement at each fixed deterministic finite-width time is recorded separately in `INTRINSIC_DIMENSION_RESULT.md`, Section 3; it is not a width-uniform lower bound and is not used below.

## 1. Conditional backward energy preserves a spanning set of saturated features

Let \(x_1,\ldots,x_m\in\mathbb R^d\) be distinct, nonantipodal unit vectors. Fix a finite scalar-ascent horizon \(S>0\). Let \(\alpha(s)\in\mathbb R^d\) be an almost surely absolutely continuous first-neuron path with \(\alpha(0)\sim N(0,I_d)\). Let \(B(s)\in\mathbb R^m\) be its jointly defined backward field. No independence between \(B\) and \(\alpha(0)\), and no Markov property, is assumed. Suppose the exact first-neuron scalar-ascent equation holds almost everywhere:
\[
\alpha'(s)=\frac1m\sum_{b=1}^m
 \operatorname{sech}^2(\alpha(s)^\top x_b)B_b(s)x_b.
\tag{1}
\]
For the canonical network, (1) is the first-layer equation for ascent of
\(g=m^{-1}\sum_b f_b\), and \(B_b\) is the relevant coordinate of
\(W^\top[w\odot(1-h_b^2)]\), or the corresponding adjoint action in a constructed population model.

Assume the following stronger-than-unconditional energy bound: there is a finite deterministic \(C_S\) such that
\[
\mathbb E\left[
 \left(\int_0^S\|B(s)\|_2\,ds\right)^2
 \mathrel{\big|}\alpha(0)\right]\le C_S^2
\quad\text{almost surely}.
\tag{2}
\]
Then the endpoint first-feature Gram
\[
(Q_U(S))_{ab}=\mathbb E[
 \tanh(\alpha(S)^\top x_a)\tanh(\alpha(S)^\top x_b)]
\]
is strictly positive definite. A deterministic quantitative lower bound follows from the proof below. This assertion concerns the endpoint law; applying it to finite-width empirical Grams additionally requires an appropriate concentration or convergence statement.

### Spanning sign patterns

The vectors
\[
\bigl(\operatorname{sgn}(v^\top x_b)\bigr)_{b=1}^m,
\qquad v^\top x_b\ne0\text{ for every }b,
\]
span \(\mathbb R^m\). For \(d\ge2\), fix \(a\) and choose a point on the hyperplane \(x_a^\perp\) that belongs to no other \(x_b^\perp\). Such a point exists because nonantipodal distinct inputs give distinct hyperplanes, and finitely many proper hyperplanes within \(x_a^\perp\) cannot cover it. Small perturbations to the two sides of \(x_a^\perp\) change only sign \(a\). The difference of the two sign vectors is therefore \(2e_a\) up to sign. Any vector orthogonal to all sign vectors must consequently have every coordinate zero. When \(d=1\), the assumptions permit only \(m=1\), where the claim is immediate.

Select unit vectors \(v_1,\ldots,v_m\) giving linearly independent sign vectors \(\varepsilon_1,\ldots,\varepsilon_m\in\{-1,1\}^m\). Let \(E\) be the matrix with rows \(\varepsilon_k^\top\), and define
\[
\gamma=\sigma_{\min}(E)>0,
\qquad \delta=\min_{k,b}|v_k^\top x_b|>0.
\]
Choose \(L\ge1\) large enough that
\[
\frac{16C_S^2}{mL^2}e^{-4L}\le\frac12,
\qquad 2\sqrt m\,e^{-2L}\le\frac{\gamma}{2\sqrt m}.
\tag{3}
\]
Set \(R=(2L+1)/\delta\), and let
\[
p_k=\Pr\{\alpha(0)\in B(Rv_k,1)\}>0,
\qquad p_{\min}=\min_kp_k>0.
\]
Every initial point in that ball has each signed sample margin at least \(2L\):
\(\varepsilon_{k,b}\alpha(0)^\top x_b\ge R\delta-1=2L\).

### Protection of each sign pattern

Fix one of these root balls. Until \(\|\alpha(s)-\alpha(0)\|_2\) first reaches \(L\), every signed margin remains at least \(L\). Therefore
\[
\operatorname{sech}^2(\alpha(s)^\top x_b)\le4e^{-2L},
\qquad
\|\alpha'(s)\|_2\le\frac4{\sqrt m}e^{-2L}\|B(s)\|_2.
\]
A first exit before or at \(S\) thus requires
\[
\int_0^S\|B(s)\|_2\,ds
\ge\frac{\sqrt m L}{4}e^{2L}.
\]
Conditional Markov inequality and (2) bound the probability of exit, uniformly for almost every root in the ball, by the first expression in (3). Consequently the event consisting of this root ball and no exit has probability at least \(p_k/2\). On this event the endpoint feature vector differs from \(\varepsilon_k\) in Euclidean norm by at most \(2\sqrt m e^{-2L}\), since
\(1-\tanh z\le2e^{-2z}\) for \(z\ge L\).

For any unit \(q\in\mathbb R^m\), \(\|Eq\|_2\ge\gamma\), so some \(k\) satisfies
\(|\varepsilon_k^\top q|\ge\gamma/\sqrt m\). On its protected event, (3) gives
\[
|q^\top\tanh(X^\top\alpha(S))|\ge\frac{\gamma}{2\sqrt m}.
\]
Taking expectations proves the explicit bound
\[
Q_U(S)\succeq\frac{p_{\min}\gamma^2}{8m}I_m\succ0.
\tag{4}
\]
Thus a uniform second-moment bound conditional on the Gaussian first-neuron root is sufficient; a total-variation bound on the entire response history is not logically necessary for this lemma. However, no argument here proves (2) for the actual correlated-input Gaussian training flow. The known unconditional normalized \(L^2\) bound does not imply (2).

## 2. A tail-free endpoint lemma for a regular simplex

Fix \(m\ge3\), and let \(v_1,\ldots,v_m\) be unit regular-simplex vertices in \(\mathbb R^d\), where \(d\ge m-1\). Thus
\[
\sum_a v_a=0,\qquad
v_a^\top v_b=-\frac1{m-1}\quad(a\ne b).
\]
Their input Gram has rank \(m-1\), so the input columns are not independent.

Consider a finite state, or an already constructed population state, of the same two-tanh-layer network. In the population case the first layer is a linear map \(A:\mathbb R^d\to L^2(\Omega_1)\), the middle layer is a bounded operator \(W:L^2(\Omega_1)\to L^2(\Omega_2)\), and \(w\in L^2(\Omega_2)\). The fields are
\[
u_a=\tanh(Av_a),\quad h_a=\tanh(Wu_a),\quad
b_a=w\odot(1-h_a^2),\quad f_a=\langle w,h_a\rangle.
\]
Finite-state inner products use \(n^{-1}\) normalization. The readout-plus-middle kernel is
\[
(K_{\mathrm{R+W}})_{ab}
=\langle h_a,h_b\rangle
 +\langle b_a,b_b\rangle\langle u_a,u_b\rangle.
\tag{5}
\]
Assume this deterministic kernel is invariant under every sample permutation. Assume also that the scalar mean prediction
\[
g=\frac1m\sum_a f_a
\]
is strictly positive. Then
\[
K_{\mathrm{R+W}}\succ0.
\tag{6}
\]
No full-support assumption, backward-field tail assumption, or full-rank first-feature Gram is needed.

To prove (6), permutation invariance implies
\(K_{\mathrm{R+W}}=\eta I_m+\beta\mathbf1\mathbf1^\top\). Its common direction is positive: with \(\bar h=m^{-1}\sum_a h_a\), one has \(g=\langle w,\bar h\rangle>0\), hence \(\bar h\ne0\), and the readout contribution alone has strictly positive common-direction energy.

If the contrast eigenvalue \(\eta\) were zero, then every pair contrast would have zero energy. The readout term in (5) first gives \(h_a=h_b\) for all \(a,b\). Therefore their top preactivations and top gates coincide, because tanh is injective at finite arguments. Write \(b\) for the resulting common backward vector. Since \(g>0\), \(w\ne0\); the top gates are strictly positive almost everywhere, so \(b\ne0\).

The middle-layer contrast gradient is then
\(b\otimes(u_a-u_b)\). Its squared norm equals
\(\|b\|_2^2\|u_a-u_b\|_2^2\), and zero contrast energy forces all \(u_a\) equal. Injectivity of tanh forces all \(Av_a\) equal. But
\(\sum_a Av_a=A\sum_a v_a=0\), so every \(Av_a=0\). It follows that \(U=H=0\), contradicting \(g>0\). Thus \(\eta>0\), proving (6).

For an already constructed deterministic permutation-symmetric scalar-ascent path from the canonical Gaussian initialization, the established scalar radial argument yields \(g(s)>0\) for every \(s>0\). Consequently (6) applies at every positive finite feature time. If its kernel is continuous on a fixed compact feature interval and positive definite at initialization, compactness yields a positive minimum eigenvalue on that interval. These are conditional endpoint and compact-path statements: this lemma does not establish the existence, uniqueness, identification, or finite-width approximation of the correlated population path.

### Exact extension to mixed label signs

Let \(\sigma\in\{-1,1\}^m\), put \(x_a=\sigma_a v_a\), and use labels \(y_a=c\sigma_a\), with any fixed \(c>0\). The bias-free two-tanh-layer network is odd in its input for every parameter state:
\[
u(x_a)=\sigma_a u(v_a),\quad
h(x_a)=\sigma_a h(v_a),\quad
f(x_a)=\sigma_a f(v_a).
\]
Therefore the signed-data loss is identically the unsigned-simplex loss with constant labels:
\[
\frac1m\sum_a[f(x_a)-c\sigma_a]^2
=\frac1m\sum_a[f(v_a)-c]^2.
\]
Their parameter gradients, with the prescribed mobilities, are identical at every state. Starting from the same canonical Gaussian weights and zero readout gives exactly the same parameter trajectory. This is an exact conjugacy and does not alter the initialization distribution.

The signed scalar contrast also agrees identically:
\[
\frac1m\sum_a\sigma_a f(x_a)=\frac1m\sum_a f(v_a).
\]
Hence the corresponding scalar-ascent vector fields agree. With \(D_\sigma=\operatorname{diag}(\sigma)\), the signed readout-plus-middle kernel is
\[
K_{\mathrm{R+W},x}=D_\sigma K_{\mathrm{R+W},v}D_\sigma.
\]
This follows directly because top and first features gain their sample signs while top backward vectors do not. The conjugation preserves eigenvalues, so (6) transfers unchanged. The signed input Gram is also a diagonal-sign conjugate of the simplex Gram and still has rank \(m-1\).

## 3. Why unconditional backward L2 does not supply an inverse flow

Finite-horizon unconditional \(L^2\) control gives almost sure integrability of the rowwise driving field and finite rowwise displacement. It controls neither the drive uniformly conditional on a rare initial root nor the derivative of the trained drive with respect to that root. Those quantities are needed for the proposed characteristic-inverse argument. In the actual network the backward field depends on the coupled network and its history, so it cannot be treated as an exogenous common Eulerian vector field.

The failure of the abstract inference from bounded gates and unconditional \(L^2\) can be shown exactly. This example is **only a forced-path example, not a trajectory of the Gaussian gradient-flow model**. With one scalar coordinate, define
\[
\zeta(z)=\int_0^z\cosh^2v\,dv
=z/2+\sinh(2z)/4.
\]
For \(G\sim N(0,1)\), set
\[
\alpha(s)=\zeta^{-1}((1-s/S)\zeta(G)),
\qquad B(s)=-\zeta(G)/S,
\qquad 0\le s\le S.
\]
Then \(\alpha(0)=G\), \(\alpha(S)=0\), and
\(\alpha'=\operatorname{sech}^2(\alpha)B\) exactly. The backward field has a finite, time-uniform unconditional second moment, since \(\zeta(G)\) has every finite moment. Nevertheless the endpoint distribution is a point mass. Its conditional backward energy grows like \(\zeta(G)^2\), so it violates (2).

This example disproves only a generic transport implication based on the listed estimates. It is not evidence that the actual gradient flow collapses. Additional structural identities of the actual flow could still prevent collapse; Lemma 2 provides such an identity for the regular-simplex symmetric endpoint. For general geometries, deriving an actual root-conditional estimate such as (2), or another sufficient structural invariant, remains open here.

## 4. Scope at freeze

Lemma 1 gives an alternative explicit sufficient root-conditional energy hypothesis for endpoint feature diversity, without requiring a total-variation response representation. No logical ordering of the two hypothesis packages is asserted. The root-conditional hypothesis remains unproved for the actual network. Lemma 2 proves endpoint readout-plus-middle coercivity for an already constructed permutation-symmetric regular-simplex scalar state, including the exact mixed-sign conjugacy. Neither lemma establishes a correlated Gaussian population construction, finite-width capture, or all-time fitting. No actual-Gaussian-flow counterexample has been produced.
