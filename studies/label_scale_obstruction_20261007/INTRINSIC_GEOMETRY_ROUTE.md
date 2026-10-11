# Intrinsic geometry: exact reductions and limits of gate cancellation

Status: theoretical route candidate, derived and algebraically self-checked by
the scoped geometry agent; not independently reviewed or promoted. No
experiments. The all-time fitting theorem remains open outside the previously
proved regimes.

Input scope: the supervisor's canonical-model assignment only for the first
round. After returning the bracket obstruction, the supervisor authorized
reading `GAUSSIAN_NONORTHOGONAL_EXTENSION.md`, which was read completely, and
asked whether a curved row metric could repair its variational estimate. No
other scientific sources were read. Required proof, research, and canonical
notation instructions were applied. The separate feature and symmetry routes
were not consulted.

## 1. Exact removal of the ambient dimension

Let the fixed data matrix be \(X\in\mathbb R^{D\times m}\), with rank
\(d\). The network and its physical gradient flow are
\[
U=\tanh(AX),\qquad H=\tanh(WU),\qquad
f=H^\top w/n,\qquad r=f-y,\qquad
\mathcal L=\|r\|_2^2/m,
\]
\[
\dot A=-n\nabla_A\mathcal L,\qquad
\dot W=-\nabla_W\mathcal L,\qquad
\dot w=-n\nabla_w\mathcal L.
\]
Here \(A\in\mathbb R^{n\times D}\), \(W\in\mathbb R^{n\times n}\),
and \(w\in\mathbb R^n\). Initially the entries of \(A\) are independent
\(N(0,1)\), those of \(W\) are independent \(N(0,1/n)\), the two
matrices are independent, and \(w=0\).

Choose \(Q\in\mathbb R^{D\times d}\) with orthonormal columns spanning
the data, and put
\[
V=Q^\top X\in\mathbb R^{d\times m},\qquad
\Theta=AQ\in\mathbb R^{n\times d}.
\]
Then \(X=QV\), \(AX=\Theta V\), and the initialization of \(\Theta\)
again has independent standard Gaussian entries. Since every first-layer
gradient row belongs to the column space of \(Q\),
\[
\frac d{dt}\bigl(A(I_D-QQ^\top)\bigr)=0,\qquad
\dot\Theta=-n\nabla_\Theta\mathcal L.
\]
Thus the network's complete output trajectory is exactly the trajectory of
the same canonical network on \(V\). Neither the output dynamics nor their
initial law depends on \(D\). This is an isometric reduction, with no
optimizer or mobility change.

Write \(v_a\in\mathbb R^d\) for column \(a\) of \(V\), and consider
row \(\theta\in\mathbb R^d\) of \(\Theta\). Define
\[
z_a=v_a^\top\theta,\qquad s_a=\operatorname{sech}^2 z_a,
\qquad b_a=w\odot(1-h_a^2),\qquad B_a=W^\top b_a.
\]
The subscript \(j\) below selects this first-layer neuron. Its exact flow is
\[
\dot\theta=-\frac2m\sum_{a=1}^m r_a B_{a,j}\,s_a v_a.
\tag{1}
\]
In particular, setting \(G=V^\top V=X^\top X\), the sample
preactivation vector lies in \(\operatorname{range}G\) and satisfies
the equation given in the assignment.

## 2. The correct intrinsic metric does not require inverting the sample Gram

For \(z=V^\top\theta\), the Euclidean squared length of an intrinsic
variation is
\[
\|\delta\theta\|_2^2=\delta z^\top G^\dagger\delta z,
\qquad \delta z\in\operatorname{range}G.
\tag{2}
\]
Here \(G^\dagger\) is its Moore--Penrose inverse. To verify (2), take a
singular value decomposition \(V=P\Sigma R^\top\) with positive
diagonal \(\Sigma\). Then \(G^\dagger=R\Sigma^{-2}R^\top\) and
\(VG^\dagger V^\top=I_d\).

For the activation vector \(u=\tanh z\), let
\(D_s=\operatorname{diag}(s_1,\ldots,s_m)\). Its tangent space is
\(D_s\operatorname{range}G\), its induced metric is
\[
\|\delta\theta\|_2^2
=\delta u^\top D_s^{-1}G^\dagger D_s^{-1}\delta u,
\tag{3}
\]
and its mobility under sample forcing \(c_a=r_aB_{a,j}\) is exactly
\[
\dot u=-\frac2m D_sGD_s c.
\tag{4}
\]
Every \(s_a\) is positive at a finite state. Thus this metric is
nonsingular on the actual \(d\)-dimensional tangent space even when
\(m>d\). The small eigenvalues created by saturation have not disappeared;
they occur in the metric coefficients rather than in an invalid inverse of
\(G\).

The rank of one row's mobility is not a bound on the rank of the whole
network tangent kernel. For example its first-layer contribution is
\[
K_A=\frac1n\sum_{j=1}^n
\operatorname{diag}(s_{1,j}B_{1,j},\ldots,s_{m,j}B_{m,j})\,
G\,
\operatorname{diag}(s_{1,j}B_{1,j},\ldots,s_{m,j}B_{m,j}).
\tag{5}
\]
The summands can have different ranges. Equation (5) is a sum of positive
semidefinite matrices and need not have rank at most \(d\). At the specified
zero-readout initialization, however, \(B_a=0\), so \(K_A=0\); initial
fitting power must then come from the readout kernel.

## 3. Classification of exact row charts that remove every first tanh gate

Define the smooth sample vector fields on intrinsic row space by
\[
F_a(\theta)=\operatorname{sech}^2(v_a^\top\theta)v_a=s_a v_a.
\]
A data-dependent coordinate map \(\Phi\) would exactly extend the
orthogonal gate cancellation if every pushforward \(D\Phi F_a\) were
constant. This demands cancellation for each sample forcing direction,
independently of its evolving coefficient in (1).

For the convention \([F_a,F_b]=DF_bF_a-DF_aF_b\), differentiation gives
\[
DF_a=-2s_a\tanh(z_a)v_av_a^\top,
\]
\[
[F_a,F_b]
=2(v_a^\top v_b)s_as_b
 \bigl(\tanh(z_a)v_a-\tanh(z_b)v_b\bigr).
\tag{6}
\]
If a smooth diffeomorphism makes both fields constant, their bracket must
vanish: apply the chain rule to the two pushed-forward derivatives; the
second derivatives of \(\Phi\) cancel by symmetry, leaving
\(D\Phi[F_a,F_b]\).

For nonzero samples, the bracket vanishes on a nonempty open set if and only
if the pair is orthogonal or \(v_b=\pm v_a\). Indeed, when their inner
product is nonzero and they are linearly independent, the two coefficients
inside the parentheses in (6) would both have to vanish throughout that
open set, which is impossible. If \(v_b=cv_a\), its vanishing would require
\(\tanh z=c\tanh(cz)\) on an interval. Differentiating and using the
original identity gives
\[
1-c^2\tanh^2(cz)=c^2\bigl(1-\tanh^2(cz)\bigr),
\]
so \(c^2=1\). Zero sample vectors are identically zero fields and impose
no condition.

The condition is also sufficient. Choose one representative \(v_i\) from
each exact signed-duplicate class; these representatives are orthogonal.
Because they span intrinsic row space, their number is \(d\). With
\[
\zeta(z)=z/2+\sinh(2z)/4,
\qquad
\Phi_i(\theta)=\frac{\zeta(v_i^\top\theta)}{\|v_i\|_2^2},
\tag{7}
\]
one has \(D\Phi F_a=\pm e_i\) for \(v_a=\pm v_i\).
Here \(\zeta'(z)=\cosh^2z>0\), and \(\zeta\) is onto
\(\mathbb R\), so (7) is a global diffeomorphism.

Consequently, for a dataset without exact signed duplicates, simultaneous
gate removal exists precisely when the nonzero samples are pairwise
orthogonal. Correlated nonsingular sample Grams already obstruct this
particular chart, and generic data with \(m>d\) cannot satisfy its
condition. This is a theorem about simultaneous gate removal, not a theorem
against fitting or against all coordinate-based estimates.

## 4. Curvature cannot provide exact cancellation in a fixed row metric

Let \(M(\theta)\) be any positive definite \(C^2\) Riemannian metric
matrix, not assumed flat or induced by a chart. For a vector field \(F\),
define its metric variation by
\[
\mathcal L_F M=(F\cdot\nabla)M+(DF)^\top M+MDF.
\tag{8}
\]
Vanishing of (8) says that the field's flow preserves infinitesimal squared
lengths; such a field is called Killing for this metric.

Suppose \(\dot\theta=\sum_a q_aF_a(\theta)\), and let \(\eta\) be a
variation that also changes the coefficients by \(\delta q_a\). Direct
differentiation gives
\[
\frac d{dt}(\eta^\top M\eta)
=\sum_a q_a\eta^\top\mathcal L_{F_a}M\eta
 +2\eta^\top M\sum_a\delta q_aF_a.
\tag{9}
\]
In the network, \(q_a=-2r_aB_{a,j}/m\). Thus making all sample fields
Killing would cancel precisely the gate-variation terms responsible for
unbounded reverse-field multipliers, leaving the coefficient-variation
terms to be estimated as in the orthogonal proof.

Such a metric does not exist if one pair satisfies
\[
v_a^\top v_b\ne0,
\qquad v_av_a^\top\ne v_bv_b^\top.
\tag{10}
\]
To prove this, put \(Z=[F_a,F_b]\). Equation (6) gives
\[
Z(0)=0,\qquad
DZ(0)=2(v_a^\top v_b)(v_av_a^\top-v_bv_b^\top)=J.
\tag{11}
\]
The matrix \(J\) is real symmetric and nonzero. If both fields preserve
the metric, their bracket does too. This follows either by differentiating
their flow commutator or by expanding the identity
\(\mathcal L_{[F_a,F_b]}=[\mathcal L_{F_a},\mathcal L_{F_b}]\)
on matrix-valued covariant tensors. At \(0\), equations (8) and (11)
therefore require
\[
J^\top M(0)+M(0)J=0.
\tag{12}
\]
Choose a real eigenvector \(e\ne0\) with nonzero eigenvalue
\(\lambda\) of the symmetric matrix \(J\). Evaluating (12) on \(e\)
gives \(2\lambda e^\top M(0)e=0\), contradicting positivity.

This rules out every positive fixed intrinsic-row metric defined in a
neighborhood of the origin, including curved metrics. The same pairwise
orthogonality/signed-duplicate condition from Section 3 is sufficient,
because the pullback of the Euclidean metric by (7) works.

There is also no fixed row metric yielding an upper bound in (9) independent
of arbitrary signed coefficient magnitudes while leaving the
\(\delta q\) term aside. For each \(a\), take the other coefficients
zero and let \(q_a\) tend to either sign of infinity. The bound forces
\(\eta^\top\mathcal L_{F_a}M\eta=0\) for every \(\eta\), hence
\(\mathcal L_{F_a}M=0\), already contradicted by (10).

The qualifier “arbitrary signed coefficients” is essential. This does not
exclude a probabilistic bound exploiting the actual joint law of
\(r,B,\Theta,W,w\), a one-sided estimate using a dynamically proved sign
condition, or a metric depending on the full network state. It closes only
the direct replacement of the orthogonal row norm by a fixed curved row
metric with exact cancellation.

## 5. A stationary forced-row example explains the one-sided difficulty

The obstruction is present for three distinct unit samples in two
dimensions. Let
\[
v_1=e_1,\qquad v_2=e_2,\qquad v_3=(e_1+e_2)/\sqrt2,
\qquad \theta_*=(t,0),\quad t>0.
\]
Write \(s_1=\operatorname{sech}^2t\) and
\(s_3=\operatorname{sech}^2(t/\sqrt2)\). For a nonzero scalar \(c\),
freeze coefficients at
\[
q_3=c,\qquad q_1=-\frac{cs_3}{\sqrt2s_1},\qquad
q_2=-\frac{cs_3}{\sqrt2}.
\]
The field \(F=\sum_a q_aF_a\) vanishes at \(\theta_*\). Its derivative is
\[
DF(\theta_*)=cs_3
\begin{pmatrix}
\sqrt2\tanh t-\tanh(t/\sqrt2)&-\tanh(t/\sqrt2)\\
-\tanh(t/\sqrt2)&-\tanh(t/\sqrt2)
\end{pmatrix}.
\tag{13}
\]
Its determinant equals
\(-\sqrt2c^2s_3^2\tanh t\tanh(t/\sqrt2)<0\), so it has a positive
eigenvalue. At this stationary point, motion of any fixed row metric is
zero. A corresponding eigenvector therefore has positive metric-norm
growth, arbitrarily large after scaling \(|c|\).

This example concerns the forced row subsystem and is not asserted to be an
actual network training trajectory. It demonstrates why a proof that treats
reverse coefficients as arbitrary bounded-time controls cannot obtain a
coefficient-independent one-sided estimate by changing the row metric.

## 6. What a transport approach would still have to prove

A metric can always be transported along a prescribed smooth row flow to
cancel its linearized growth. If its flow map is \(\Phi_t\), then
\[
M_t(\Phi_t(\theta_0))
=D\Phi_t(\theta_0)^{-\top}M_0(\theta_0)
 D\Phi_t(\theta_0)^{-1}
\tag{14}
\]
solves the metric transport equation. Formula (14) alone is not a sensitivity
bound: comparison with a fixed norm requires bounds on the very derivative
and inverse derivative being estimated. It also depends on the actual
trajectory and does not provide an autonomous row-only construction.

Likewise, transport of an initially Gaussian population does not by itself
give persistent quantitative feature diversity. For a common diffeomorphism
\(\Phi_t:\mathbb R^d\to\mathbb R^d\), the transported density is
\[
\rho_t(\theta)=
\frac{(2\pi)^{-d/2}\exp(-\|\Phi_t^{-1}(\theta)\|_2^2/2)}
 {|\det D\Phi_t(\Phi_t^{-1}(\theta))|}.
\tag{15}
\]
Uniform bounds on the inverse image and the Jacobian determinant over a
fixed compact set \(K\) would imply a uniform positive lower bound for
\(\rho_t\) on \(K\). Only then would a positive feature Gram integral
over \(K\) provide a quantitative, all-time population lower bound.
Finite-time invertibility and positivity of the density do not supply these
uniform estimates: even \(\Phi_t(\theta)=e^{-t}\theta\) transports a
Gaussian to a law collapsing at zero as \(t\to\infty\).

There is a deterministic finite-sample bridge if those stronger transport
hypotheses were obtained. Let
\(F(\theta)=\tanh(V^\top\theta)\in\mathbb R^m\), let \(\gamma\)
be the standard Gaussian law, and let \(\mu_n\) be its empirical
initial row law. For every unit \(c\in\mathbb R^m\), the function
\((c^\top F)^2\) has Lipschitz constant at most
\(2\sqrt m\|V\|_{\rm op}\). If a common transport has Lipschitz
constant at most \(L\), coupling the initial laws yields
\[
\left\|\int FF^\top\,d(\Phi_t)_\#\mu_n
-\int FF^\top\,d(\Phi_t)_\#\gamma\right\|_{\rm op}
\le 2\sqrt m\|V\|_{\rm op}L\,W_1(\mu_n,\gamma).
\tag{16}
\]
Here \(W_1\) is the infimum of the expected Euclidean distance over
couplings. To verify (16), apply the Lipschitz bound inside any coupling,
take its infimum, and then take the supremum over unit \(c\).
This inequality even permits a data-dependent common map, since it is a
deterministic comparison for each realized map. No post-training
independence is required for this conditional implication.

The actual first-layer neurons, however, have neuron-dependent reverse
fields \(B_{a,j}\). Equations (1) do not presently furnish a common
transport with uniform distortion bounds. Establishing that structure or a
replacement estimate is a substantial missing lemma, not a consequence of
initial full rank.

## 7. Route outcome

The ambient-dimension restriction is removed exactly. The singular sample
Gram admits a regular intrinsic interpretation, and does not itself prevent
the network kernel from having full rank. Exact gate cancellation by either
a fixed row chart or a fixed curved row metric is nevertheless impossible
for general correlated inputs, under the precise simultaneous-forcing
requirement proved above.

The proposed next mechanism must use restrictions imposed by actual network
training: a full-state metric, a probabilistic variational estimate, or a
quantitative transport/capture argument. The bracket and metric obstructions
do not disprove high-probability finite-width all-time fitting. This route is
closed for exact row-only cancellation and remains open for those broader
mechanisms; no Gaussian sensitivity or strong-flow theorem for arbitrary
correlated data has been proved here.
