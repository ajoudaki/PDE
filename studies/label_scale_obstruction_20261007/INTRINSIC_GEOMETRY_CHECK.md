# Internal check of the intrinsic geometry route

Checked 2026-10-11 by the scoped `intrinsic_geometry_check` agent. This is an
independent internal mathematical check, not a promotion review. The only
scientific input was the complete 354-line `INTRINSIC_GEOMETRY_ROUTE.md`, SHA-256
`33626db7dba86ff58b5bbbcdd0bcadb06766a6802dc47ab50d992a598709d327`.
No other study sources, author discussion, prior verdicts, external scientific
sources, code, or experiments were used. Required shared instructions and the
`solve-math-rigorously` and `explain-with-canonical-notation` skills, including
the neural-network reference, were read. Source text was not changed.

**Outcome:** all stated algebraic results and conditional estimates pass for
their stated scopes. No mathematical correction is required. Two scope
qualifiers must survive any subsequent summary: the curved-metric obstruction
is proved for metrics defined near the origin, and the coefficient-independent
estimate is excluded only when arbitrary signed forcing magnitudes are allowed.
The source neither proves nor disproves all-time fitting under actual Gaussian
initialization for general correlated data. It removes irrelevant ambient
coordinates; it does not complete the requested removal of an intrinsic-rank
restriction from an all-time fitting theorem.

## 1. Model, isometry, and mobility normalization

The source model has fixed data \(X\in\mathbb R^{D\times m}\), width \(n\),
parameters \(A\in\mathbb R^{n\times D}\), \(W\in\mathbb R^{n\times n}\),
and \(w\in\mathbb R^n\), with
\[
U=\tanh(AX),\quad H=\tanh(WU),\quad
f=H^\top w/n,\quad r=f-y,\quad \mathcal L=\|r\|^2/m.
\]
Its physical gradient flow has mobilities \((n,1,n)\) for \((A,W,w)\).
The initialization is independent standard Gaussian entries for \(A\),
independent \(N(0,1/n)\) entries for \(W\), independence between these
matrices, and \(w=0\).

Let \(d=\operatorname{rank}X\), let \(Q\in\mathbb R^{D\times d}\) have
orthonormal columns spanning the data, and set \(V=Q^\top X\) and
\(\Theta=AQ\). Then \(X=QV\), \(AX=\Theta V\), and the loss depends on
\(A\) only through \(\Theta\). The chain rule gives
\[
\nabla_A\mathcal L=(\nabla_\Theta\mathcal L)Q^\top,
\quad \dot A(I_D-QQ^\top)=0,
\quad \dot\Theta=-n\nabla_\Theta\mathcal L.
\]
Each Gaussian row of \(AQ\) has covariance \(Q^\top Q=I_d\); joint
Gaussianity gives independent standard coordinates, and the rows remain
independent. Independence from \(W\) is preserved. Thus both the dynamics
and the initialization law reduce exactly. This is invariance under an
isometric representation of the same data, not invariance under arbitrary
changes of data geometry or input scaling.

For completeness, the smooth finite-dimensional flow exists for all finite
times. The weighted energy identity is
\[
-\dot{\mathcal L}
=\|\dot A\|_F^2/n+\|\dot W\|_F^2+\|\dot w\|^2/n.
\]
Its integral and Cauchy--Schwarz bound the weighted parameter displacement
on every finite time interval by \(\sqrt{T\mathcal L(0)}\). A finite-time
escape to infinity is therefore impossible, which supplies the usual
continuation criterion for this smooth ODE.

Write \(u_a,h_a\) for column \(a\) of \(U,H\), \(v_a\) for column
\(a\) of \(V\), and
\[
s_{a,j}=\operatorname{sech}^2(v_a^\top\theta_j),\quad
b_a=w\odot(1-h_a^2),\quad B_a=W^\top b_a,
\]
where \(\theta_j\in\mathbb R^d\) is the transpose of row \(j\) of
\(\Theta\). Direct differentiation gives
\[
\nabla_{\theta_j}f_a=B_{a,j}s_{a,j}v_a/n,
\quad \nabla_W f_a=b_a u_a^\top/n,
\quad \nabla_w f_a=h_a/n.
\]
Combining the first formula with the loss factor \(2/m\) and the first-layer
mobility \(n\) verifies equation (1) exactly:
\[
\dot\theta_j=-\frac2m\sum_a r_aB_{a,j}s_{a,j}v_a.
\]

To make the tangent-kernel normalization explicit, define \(K\) by
\(\dot r=-(2/m)Kr\). If \(G=V^\top V\), the three contributions are
\[
\begin{aligned}
(K_A)_{ab}&=\frac{G_{ab}}n\sum_j
 B_{a,j}s_{a,j}B_{b,j}s_{b,j},\\
(K_W)_{ab}&=\frac{(b_a^\top b_b)(u_a^\top u_b)}{n^2},\\
(K_w)_{ab}&=h_a^\top h_b/n.
\end{aligned}
\]
These verify equation (5), including its factor \(1/n\). At initialization
\(b_a=B_a=0\), so both \(K_A\) and \(K_W\) vanish and only \(K_w\)
can initially reduce the residual. A sum of congruences of \(G\) can have
larger rank than \(G\), since their images need not coincide; a row-rank
bound is not a bound on the rank of their sum. No claim of strict positivity
of the actual evolving \(K\) follows from this observation alone.

## 2. The metric on the actual tangent space

For a single row, set \(z=V^\top\theta\),
\(s_a=\operatorname{sech}^2z_a\), \(D_s=\operatorname{diag}(s_a)\),
and \(u=\tanh z\). A thin singular value decomposition
\(V=P\Sigma R^\top\) gives
\[
G^\dagger=R\Sigma^{-2}R^\top,
\qquad VG^\dagger V^\top=I_d.
\]
Consequently, for \(\delta z=V^\top\delta\theta\),
\[
\delta z^\top G^\dagger\delta z=\|\delta\theta\|^2.
\]
Since every gate is positive at a finite state, the activation map is an
immersion, its tangent space is \(D_s\operatorname{range}G\), and
\(\delta z=D_s^{-1}\delta u\). This proves equations (2)--(3) and
positive definiteness on that tangent space. The displayed matrix need not
be positive definite on all of \(\mathbb R^m\); that is neither needed nor
claimed. With \(c_a=r_aB_{a,j}\), differentiation of the row equation gives
\[
\dot z=-(2/m)GD_sc,\qquad
\dot u=-(2/m)D_sGD_sc,
\]
verifying equation (4). Finite-state positivity does not imply a uniform
condition number along an unbounded trajectory.

If \(d=0\), the intrinsic space is zero dimensional and these identities
are vacuous. In that case all inputs, activations, and predictions are zero,
so arbitrary nonzero labels cannot be fitted. This edge case creates no
counterexample to the stated reduction or geometry claims.

## 3. Exact flat-chart classification

Define \(F_a(\theta)=s_av_a\) and use the source convention
\([F_a,F_b]=DF_bF_a-DF_aF_b\). Since
\[
DF_a=-2s_a\tanh(z_a)v_av_a^\top,
\]
substitution yields
\[
[F_a,F_b]
=2(v_a^\top v_b)s_as_b
\bigl(\tanh(z_a)v_a-\tanh(z_b)v_b\bigr).
\]
This checks equation (6), including the sign. Under a diffeomorphism, the
bracket of the pushed-forward fields is the pushforward of this bracket:
expansion produces two equal Hessian terms which cancel. Constant fields
commute, so simultaneous constancy forces every bracket to vanish.

For nonzero \(v_a,v_b\) with nonzero inner product, linear independence
would force \(z_a=z_b=0\) throughout the alleged open set, an impossibility.
In the dependent case write \(v_b=cv_a\), with \(c\ne0\). Vanishing
requires \(\tanh z=c\tanh(cz)\) on an interval. Differentiating and
substituting this identity gives
\[
1-c^2\tanh^2(cz)=c^2-c^2\tanh^2(cz),
\]
so \(c^2=1\). Orthogonal pairs and exact signed duplicates do commute;
zero sample vectors give identically zero fields.

For sufficiency, choose the mutually orthogonal nonzero signed-class
representatives \(v_1,\ldots,v_d\). They form a basis of the intrinsic
space. The scalar function
\(\zeta(z)=z/2+\sinh(2z)/4\) satisfies
\(\zeta'(z)=\cosh^2z>0\) and has limits \(\pm\infty\). Therefore
\[
\Phi_i(\theta)=\zeta(v_i^\top\theta)/\|v_i\|^2
\]
defines a global diffeomorphism. Direct differentiation gives
\(D\Phi F_a=\pm e_i\) when \(v_a=\pm v_i\). The classification is
both necessary and sufficient, including unequal sample norms and zero
samples. It is an obstruction to simultaneous cancellation of all sample
directions, even for some full-rank sample Grams; it is not an intrinsic-rank
criterion for neural fitting.

## 4. Curved metrics and arbitrary signed coefficients

For a positive definite \(C^2\) row metric \(M(\theta)\), define
\[
\mathcal L_FM=(F\cdot\nabla)M+(DF)^\top M+MDF.
\]
Along \(\dot\theta=\sum_a q_aF_a(\theta)\), a varied trajectory has
\(\dot\eta=\sum_aq_aDF_a\eta+\sum_a\delta q_aF_a\), where
\(\delta q_a\) is the total coefficient variation. Differentiating
\(\eta^\top M\eta\) gives equation (9). If coefficients depend on the
full network state, their induced row dependence belongs in \(\delta q_a\);
it has not been removed by the metric identity.

The Lie-derivative commutator identity used in the source requires no
additional geometric hypothesis. On scalar functions it is the definition
of the bracket. On exact one-forms, \(\mathcal L_F(df)=d(F\cdot\nabla f)\)
gives the same identity. Every covariant tensor is locally a sum of scalar
coefficients times products of coordinate differentials, and the Leibniz
rule extends the identity to such tensors. Hence a bracket of two Killing
fields is Killing.

For \(Z=[F_a,F_b]\), the explicit bracket gives
\[
Z(0)=0,\qquad
DZ(0)=J=2(v_a^\top v_b)(v_av_a^\top-v_bv_b^\top).
\]
Under condition (10), \(J\) is nonzero real symmetric and therefore has
a real eigenpair \(Je=\lambda e\), with \(e\ne0\), \(\lambda\ne0\).
If both fields were Killing on a neighborhood of zero, so would \(Z\), and
at zero the term \((Z\cdot\nabla)M\) vanishes. Thus
\[
0=e^\top(J^\top M(0)+M(0)J)e
 =2\lambda e^\top M(0)e,
\]
contradicting positive definiteness. This proves the claimed impossibility
for every fixed row metric defined near zero, including every global metric.
It does not by this argument exclude a metric on an arbitrary patch that
omits zero. The sufficiency claim is verified by the pullback
\(M=D\Phi^\top D\Phi\) of the flat chart above.

For an estimate of the form
\[
\sum_aq_a\eta^\top\mathcal L_{F_a}M\eta
\le C\,\eta^\top M\eta
\]
with \(C\) independent of arbitrary signed \(q\), fix a state and a
variation, set all but one coefficient to zero, and send the remaining
coefficient to both signs of infinity. Its quadratic-form coefficient must
vanish. Polarization then yields \(\mathcal L_{F_a}M=0\) for every \(a\),
which has just been excluded. This argument does not cover bounds depending
on forcing amplitude, one-sided coefficient restrictions, actual coupled
neural trajectories, or metrics depending on the full state.

## 5. Frozen-forcing stationary example

For \(v_1=e_1\), \(v_2=e_2\), \(v_3=(e_1+e_2)/\sqrt2\), and
\(\theta_*=(t,0)\), \(t>0\), the source coefficients satisfy
\[
q_1F_1(\theta_*)+q_2F_2(\theta_*)+q_3F_3(\theta_*)=0.
\]
Here the two components of the third summand are \(cs_3/\sqrt2\),
cancelled separately by the first two summands. The derivative of the
second field is zero because \(\tanh0=0\). The first and third derivative
contributions are respectively
\[
\sqrt2cs_3\tanh(t)\,e_1e_1^\top,
\qquad
-cs_3\tanh(t/\sqrt2)
\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]
Their sum verifies equation (13). Its determinant is
\(-\sqrt2c^2s_3^2\tanh(t)\tanh(t/\sqrt2)<0\), so this real symmetric
matrix has one positive and one negative eigenvalue for either sign of
\(c\ne0\).

At the stationary trajectory, \(M(\theta_*)\) is constant in time. For
a positive eigenpair \(DF(\theta_*)e=\lambda e\), the variational solution
is \(\eta(\tau)=e^{\lambda\tau}e\), giving
\[
\frac d{d\tau}(\eta^\top M\eta)
=2\lambda\eta^\top M\eta>0.
\]
Scaling the forcing scales the positive eigenvalue proportionally to its
absolute amplitude (with a fixed sign). Thus no positive fixed metric
removes this expansion. The example is exact for the forced subsystem;
neither realizability of these frozen coefficients by neural gradient flow
nor a positive-probability initialization event has been demonstrated.

## 6. Conditional metric transport, density, and finite-sample bridge

For a smooth flow map \(\Phi_t\) on its diffeomorphism domain, let
\(J_t=D\Phi_t\). The identity
\[
J_t^\top M_t(\Phi_t(\theta_0))J_t=M_0(\theta_0)
\]
proves equation (14) and constancy of the metric norm of transported
variations. Differentiating it yields
\(\partial_tM+\mathcal L_FM=0\). Uniform comparison with a fixed norm
still needs bounds on \(J_t\) and its inverse, as the source states.

Equation (15) is the change-of-variables formula. More explicitly, suppose
for a fixed compact \(K\subset\mathbb R^d\) that for all relevant times
and all \(\theta\in K\),
\[
\|\Phi_t^{-1}(\theta)\|\le R,
\qquad
|\det D\Phi_t(\Phi_t^{-1}(\theta))|\le J_*<\infty.
\]
Then the transported standard Gaussian density obeys
\[
\rho_t(\theta)\ge
\rho_*=(2\pi)^{-d/2}e^{-R^2/2}/J_*>0.
\]
For the feature vector \(F(\theta)=\tanh(V^\top\theta)\), if in addition
\(\int_KFF^\top d\theta\succeq\kappa I_m\) with \(\kappa>0\), then
\[
\int FF^\top\rho_t\,d\theta\succeq\rho_*\kappa I_m.
\]
This is a valid conditional all-time population estimate. Positive
definiteness of the compact-set feature integral is an additional premise;
it is not implied by the density formula. Density lower bounds are a
sufficient route, not a necessary condition for every possible covariance
lower-bound proof.

Finite-time invertibility alone is insufficient. For
\(\Phi_t(\theta)=e^{-t}\theta\) and a standard Gaussian vector \(g\),
\[
\mathbb E\|F(e^{-t}g)\|^2
\le e^{-2t}\mathbb E\|V^\top g\|^2
=e^{-2t}\|V\|_F^2\longrightarrow0,
\]
using \(|\tanh x|\le|x|\). This confirms the collapse example
quantitatively without confusing strict finite-time density positivity with
a uniform lower bound.

For unit \(c\in\mathbb R^m\), set
\(g_c(\theta)=(c^\top F(\theta))^2\). Its gradient is
\[
\nabla g_c=2(c^\top F)V D_sc,
\quad \|\nabla g_c\|\le2\sqrt m\|V\|_{\mathrm{op}}.
\]
If a common map \(\Phi_t\) is \(L\)-Lipschitz, then
\(g_c\circ\Phi_t\) is \(2\sqrt m\|V\|_{\mathrm{op}}L\)-Lipschitz.
Integrating its difference under any coupling of the initial empirical law
\(\mu_n\) and standard Gaussian law \(\gamma\), then taking the infimum
over couplings, bounds the absolute quadratic form of the covariance
difference by that constant times \(W_1(\mu_n,\gamma)\). Both laws have
finite first moments. The covariance difference is symmetric; taking the
supremum of its absolute quadratic form over unit \(c\) gives exactly its
operator norm, proving equation (16).

This argument is deterministic for each realized common map, including a
map depending on the initial empirical sample. Its reference measure is
then the pushforward of \(\gamma\) by that realized map; it is not, without
further justification, an unconditional trained-neuron distribution.
Neither a uniform \(L\) nor a common transport representing the network's
neuron-dependent reverse fields has been proved. No quantitative width or
intrinsic-dimension-free sampling rate is supplied by (16) alone.

## 7. Acceptance boundary and check provenance

The internally checked content consists of the exact isometry and tangent
metric, the exact simultaneous-chart classification, the near-origin
fixed-metric obstruction, the frozen-forcing expansion example, and the
explicitly conditional transport and Wasserstein estimates. Source claims
about earlier proved regimes or an orthogonal proof were not checked because
their sources were outside this assignment; none is needed for the checked
calculations above.

No actual Gaussian-gradient-flow failure is established. In particular,
\(q_a=-2r_aB_{a,j}/m\) are coupled network quantities and are initially
zero under the stated zero-readout initialization. An obstruction obtained
by allowing arbitrary coefficients cannot be substituted for an event in
that initialized neural dynamics. Conversely, the exact removal of \(D\)
and the absence of a rank bound on sums of row kernels do not prove uniform
kernel positivity or all-time fitting when \(m>d\).

The check was analytical: complete source reads, independent differentiations,
sign and mobility audits, boundary cases, an explicit eigenvalue argument,
and coupling inequalities. No numerical experiments or external theorem
dependencies were needed. Before writing, repository metadata was checked:
HEAD was `ef8362764b4eb8144d7af8d6f8db080fdaaf82ca`, the shared index was
empty, and unrelated working changes were left untouched. Only this assigned
report was added; no Git staging or commit was performed.
