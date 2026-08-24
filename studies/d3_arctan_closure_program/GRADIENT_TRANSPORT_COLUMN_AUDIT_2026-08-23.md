# Audit: gradient transport and one-column quasi-invariance

## Verdict

In raw standard-Gaussian coordinates the feature flow is an ordinary
Euclidean gradient flow.  Its global likelihood distortion is only
\(e^{O_T(n)}\), despite an ambient dimension of order \(n^2\).  This is too
coarse for empirical \(\psi _1\), which can fail through an event of
probability \(e^{-o(n)}\).

Localizing the change of measure to one initial middle column gives an exact
tilted moment-generating-function identity.  It closes at two target-specific
column-response contractions.  The column marginal continuity equation
recreates the same response through its conditional-score covariance.
Thus transport supplies a sharp sufficient lemma, not a bypass of the
response problem.

## 1. Exact Euclidean gradient structure

Put \(W_\ell=\sqrt nG_\ell\), let

\[
 \Phi_n(A,u,W_1,W_2)=A^{\mathsf T}X_3=nf_n,
\]

and use ordinary Euclidean coordinates.  The mixed-metric feature ascent is
exactly

\[
 \dot Z=\nabla\Phi_n(Z).
\]

If \(T_t\) is its flow and \(U(t,s)=DT_{t-s}(Z_s)\), then

\[
 \partial_tU=\nabla^2\Phi_n(Z_t)U,
 \qquad U(t,s)\nabla\Phi_n(Z_s)=\nabla\Phi_n(Z_t),
\]

and

\[
 \det U(t,0)=\exp\!\left\{\int_0^t\Delta\Phi_n(Z_s)\,ds\right\}.
\]

For \(\mu_t=(T_t)_\#\gamma\), change of variables gives

\[
 \log {d\mu_t\over d\gamma}(Z_t)
 =\int_0^t\{Z_s\cdot\nabla\Phi_n(Z_s)-\Delta\Phi_n(Z_s)\}\,ds.
\]

The radial term is

\[
 A^{\mathsf T}X_3+u^{\mathsf T}B_1+H_2^{\mathsf T}B_2
 +H_3^{\mathsf T}B_3.
\]

Using \(|x\phi'(x)|\le1/2\), the normalized state-energy bounds, and the
operator bounds for \(G_1,G_2\), it is \(O(n)\).  Direct blockwise
differentiation shows \(\Delta\Phi_n=O(n)\) as well; its terms are traces of
the two tangent Gram blocks weighted by \(A\phi''(H_3)\) or
\(R_2\phi''(H_2)\).  Hence, on the localized compact-time good event,

\[
 {d\mu_t\over d\gamma}\le e^{C_Tn}.
\]

The action identity also gives

\[
 \int_0^T\|\dot Z_t\|^2dt
 =\Phi_n(Z_T)-\Phi_n(Z_0)=O(n).
\]

## 2. Why the global estimate cannot imply empirical tails

One coordinate of size \(K\log(2n)\) can violate

\[
 n^{-1}\sum_j e^{|R_j|/K}\le2.
\]

Such a Gaussian event can have probability \(e^{-O(\log^2n)}\), so an
\(e^{C_Tn}\) density comparison says nothing.  More concretely, conditioning
half of an exchangeable Gaussian mixture on
\(\max_j|Y_j|\ge\sqrt n\) gives density, entropy, and quadratic transport
cost of order \(e^{O(n)},O(n),O(n)\), respectively, while its empirical
\(\psi _1\) norm is at least \(c\sqrt n/\log n\) with probability at least
one half.

The transported-velocity identity is also too low-rank.  In the \(W_2\)
block the velocity is \(n^{-1/2}B_3X_2^{\mathsf T}\), while a raw-column
perturbation contains \(n\) transverse directions.  The relevant two-by-two
top Hessian block has negative determinant

\[
 -c^2\phi'(H_{3,i})^2<0,
\]

so neither convex gradient-map contraction nor a Brascamp--Lieb argument is
available.

## 3. Exact tilted one-column identity

Fix one initial raw column

\[
 w=W_{2,0,:,j}\sim N(0,I_n),\qquad B(t)=B_3(t).
\]

The learned part is explicit:

\[
 R_{2,j}(t)
 ={w^{\mathsf T}B(t)\over\sqrt n}
 +{1\over n}\int_0^tX_{2,j}(s)B(s)^{\mathsf T}B(t)\,ds.
\]

The integral is uniformly bounded on compact time.  Put

\[
 S={w^{\mathsf T}B(t)\over\sqrt n},
 \qquad \mathcal D_{j,t}=D_wB(t).
\]

For \(\psi(\lambda)=\log\mathbb Ee^{\lambda S}\), Gaussian integration by
parts gives the exact formula

\[
 \boxed{
 \psi'(\lambda)=\mathbb E_\lambda\!\left[
 {\operatorname{tr}\mathcal D_{j,t}\over\sqrt n}
 +{\lambda\over n}\left{\|B(t)\|^2
 +w^{\mathsf T}\mathcal D_{j,t}B(t)\right}\right],}
\]

where \(\mathbb E_\lambda\) is the \(e^{\lambda S}\)-tilted law.  Therefore
the following target-specific condition is sufficient: for some
\(\lambda_0>0\),

\[
 \sup_{t\le T,j,|\lambda|\le\lambda_0}
 \mathbb E_\lambda\!\left[
 {|\operatorname{tr}\mathcal D_{j,t}|\over\sqrt n}
 +{\|B(t)\|^2+|w^{\mathsf T}\mathcal D_{j,t}B(t)|\over n}
 \right]\le C_T. \tag{CR}
\]

Then \(\log\mathbb Ee^{\lambda S}\le C_T(|\lambda|+\lambda^2)\) and the
static query is uniformly subexponential.  Condition (CR) is strictly more
targeted than an ambient tangent-operator bound; it retains only one trace
and one bilinear column response under the relevant tilt.

## 4. The marginal likelihood closes at the same place

Let \(m_t(w)\) be the current marginal density of this column and
\(\bar v(w)=\mathbb E[v_j\mid w]\), with
\(v_j=n^{-1/2}X_{2,j}B_3\).  Then

\[
 \partial_tm_t+\operatorname{div}_w(m_t\bar v)=0.
\]

For \(r_t=m_t/\gamma_n\), along the marginal characteristic,

\[
 {d\over dt}\log r_t(w_t)=w_t^{\mathsf T}\bar v-operatorname{div}\bar v.
\]

Although the direct divergence is only

\[
 \operatorname{div}_wv_j
 ={X_{2,j}^2\over n}\sum_iA_i\phi''(H_{3,i})=O(1),
\]

marginalization adds

\[
 \operatorname{Cov}\!\left(v_j,\nabla_w\log\rho_t\mid w\right),
\]

which contains the conditional score, equivalently the inverse tangent
response.  A local Renyi or BMO estimate therefore requires the same
column-response information as (CR).  Moreover, the column marginal alone
does not control \(w^{\mathsf T}B\), because \(B\) belongs to the integrated
environment.

The transport route is consequently reduced to (CR), a joint local
likelihood estimate of equivalent strength, or a BMO bound for the same
conditional-score covariance.  None follows from global action, entropy,
or state energy alone.
