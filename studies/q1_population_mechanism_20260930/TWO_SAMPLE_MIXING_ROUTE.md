# First population mixing response for the two-sample q=1 closure

Status: frozen scoped derivation, 2026-09-30. This report concerns the direct
infinite-width population model. It constructs no trained finite network and
uses no particle experiment. It is not a proof of the fixed-q population-limit
conjecture or of a global training claim.

The first reverse source has a Gaussian innovation **and** a response to its
previous forward use. The response strictly expands the common-input
first-layer mode and contracts the difference mode, in conditional mean.
Consequently, for every input correlation c in (-1,1), first-layer
preactivation correlation has strictly positive second derivative at zero
feature time. This is a local population feature-learning mechanism, conditional
only on a local strong symmetric q=1 population trajectory realizing the stated
initialized operator law.

## Scope and initialization

There are two separate neuron probability spaces, Omega_1 and Omega_2, with
expectations E_1 and E_2. Let u_1,u_2 be unit signed inputs with
u_1 dot u_2=c in (-1,1), and let both signed labels be +1. All activation
functions are tanh and all mobilities are one. On Omega_1, let A_0 be the
standard Gaussian first-layer row and put

\[
 a_a=A_0\cdot u_a,\qquad H_a=\tanh a_a,\qquad
 d_a=\operatorname{sech}^2 a_a,\qquad
 G=\begin{pmatrix}1&c\\c&1\end{pmatrix}.
\]

Thus (a_1,a_2) has law N(0,G). Write T:L^2(Omega_1)->L^2(Omega_2)
for the initialized Gaussian operator on the generated population spaces,
with its true adjoint T*. The forward fields

\[
 Z_a=T H_a,\qquad
 C_{ab}=E_1[H_aH_b],\qquad
 g_a=\tanh Z_a,\qquad k_a=\operatorname{sech}^2 Z_a,\qquad
 g_+=(g_1+g_2)/2
\]

have (Z_1,Z_2)~N(0,C) on Omega_2. Exchangeability gives

\[
 C=\begin{pmatrix}v&\kappa\\\kappa&v\end{pmatrix},\qquad
 v=E[\tanh^2 N(0,1)]>0,\qquad |\kappa|<v.
\]

For the strict inequality, (a_1,a_2) has a positive density on R^2 and
tanh a_1 cannot equal either tanh a_2 or minus tanh a_2 almost surely;
equality in Cauchy--Schwarz is therefore impossible. C is nonsingular.

The readout W on Omega_2 starts at zero. Sample exchange symmetry gives the
common prediction F on a symmetric population trajectory. Near zero F<1,
and use feature time

\[
 s=2\int_0^t(1-F(r))\,dr.
\]

Every prime below denotes differentiation in s; all initial fields displayed
without a time argument are at s=0. A local strong q=1 solution is assumed
only for interpreting the following initialization calculation as a trajectory
jet. The generated Gaussian initialization and its finitely many source calls
are separate from that existence assumption. No interchange of trained-width
limits and time differentiation is used.

## Why the q=1 first acceleration uses these sources

For clarity, write the q=1 forward memory as P_a and the negative of its
backward memory as Q_a. The learning-speed-clock q=1 population equations
from the assigned definition become

\[
 \tau=1+s/2,\qquad P_a'=h_a/2,\qquad Q_a'=\delta_a^{(2)}/2,
 \qquad P_a(0)=H_a,\quad Q_a(0)=0,
\]

\[
 K=T+\tau^{-1}\sum_{a=1}^2 Q_a\otimes P_a,
 \qquad (Q\otimes P)V=Q E_1[PV],
\]

\[
 h_a=\tanh(A\cdot u_a),\quad z_a=K h_a,\quad
 W'=(\tanh z_1+\tanh z_2)/2,
\]

\[
 \delta_a^{(2)}=W\operatorname{sech}^2z_a,\qquad
 \delta_a^{(1)}=\operatorname{sech}^2(A\cdot u_a)K^*\delta_a^{(2)},
 \qquad A'=\tfrac12\sum_a\delta_a^{(1)}u_a.
\]

Here K is the reconstructed operator; T is a fixed initialized source.
The normalization follows directly from m=2, r_a=F-1, and
ds/dt=2(1-F). In particular,

\[
 W'(0)=g_+,\qquad A'(0)=0,\qquad K'(0)=0,\qquad
 (\delta_a^{(2)})'(0)=U_a:=g_+k_a.
\]

Writing R_a=T^*U_a gives the first nonzero reverse response and first-layer
acceleration:

\[
 (K^*\delta_a^{(2)})'(0)=R_a,\qquad
 A''(0)=\frac12\sum_{b=1}^2d_bR_bu_b,
 \qquad
 a_a''(0)=\frac12\sum_{b=1}^2G_{ab}d_bR_b.                 \tag{1}
\]

These initial derivatives do not require assuming a convergent Taylor series.
Indeed continuity of a local strong solution gives W(s)/s->g_+ in L^2.
Boundedness and continuity of sech^2 then give delta_a^(2)(s)/s->U_a
in L^2, followed by delta_a^(1)(s)/s->d_a T*U_a in L^2. Integrating
A' proves A(s)=A_0+s^2 A''(0)/2+o_{L^2}(s^2). Multiplication by a bounded
gate is continuous in this argument: split off the convergent L^2 factor,
then apply dominated convergence to the fixed remaining L^2 factor.

Likewise

\[
 Q_a(s)=\tfrac14s^2U_a+o_{L^2}(s^2),\qquad
 K(s)=T+\tfrac14s^2\sum_aU_a\otimes H_a+o_{\mathrm{op}}(s^2),
\]

so K''(0)=sum_a U_a tensor H_a/2. This calculation explicitly uses the q=1
memory equations. It does not substitute another training model.

## Canonical joint law of the first reverse response

The required Gaussian-reuse law is

\[
 R_a=\sum_{b=1}^2 M_{ab}H_b+\Xi_a,
 \qquad M_{ab}=E_2[\partial_b U_a(Z)],
 \qquad (\Xi_1,\Xi_2)\sim N(0,\Sigma),                 \tag{2}
\]

\[
 \Sigma_{ab}=E_2[U_aU_b],\qquad \Xi\text{ is independent of }A_0.
                                                               \tag{3}
\]

Both reverse answers share the **same jointly Gaussian** innovation vector.
In particular Sigma is the full source second-moment matrix. It is not a
conditional variance of U given Z (which would vanish), and it is not obtained
by subtracting the linear projection of U onto Z.

Here is the specialization of the assigned conditioning identities that
identifies this law. Conditioning the initialized source on the two forward
answers gives the reverse conditional mean in their input span, with
coefficients

\[
 C^{-1}E_2[Z U_a].
\]

The remaining Gaussian source is projected only off that forward input span;
the joint reverse-source covariance is E_2[U_aU_b]. In the generated
population law its coordinate innovation is Gaussian, independent of the
first-layer roots, with that covariance. The finite-rank input projection
enforces the same orthogonality encoded by this independence. This is a
fixed-computation Gaussian initialization fact supplied by the conditioning
construction, not a trained-network convergence argument.

Gaussian integration by parts yields

\[
 E_2[Z_jU_a]=\sum_b C_{jb}E_2[\partial_bU_a].
\]

To see this without an external theorem, write Z=C^(1/2)N with independent
standard normal coordinates, integrate each N-coordinate against its Gaussian
density, and apply the chain rule. U and all its first derivatives are
bounded, so the boundary terms vanish and all integrals are finite. This
turns the conditional-mean coefficients into M and proves (2).

The same calculation checks adjunction exactly:

\[
 E_1[H_bR_a]=\sum_j C_{bj}M_{aj}=E_2[Z_bU_a].           \tag{4}
\]

This constraint relates two distinct populations; it does not pair an Omega_1
neuron with an Omega_2 neuron.

The coefficients are explicit Gaussian integrals:

\[
 M_{ab}=\frac12E_2[k_ak_b]-2\mathbf 1_{a=b}E_2[g_+g_ak_a],
 \qquad
 \Sigma_{ab}=E_2[g_+^2k_ak_b].                         \tag{5}
\]

Exchangeability gives

\[
 M=\begin{pmatrix}m&n\\n&m\end{pmatrix},\qquad
 n=\tfrac12E_2[k_1k_2]>0,\qquad
 \Sigma=\begin{pmatrix}\sigma&\eta\\\eta&\sigma\end{pmatrix}.
\]

Moreover 0<eta<sigma. Positivity of eta follows from g_+^2 k_1k_2>0 almost
surely. Strict sigma-eta>0 follows from

\[
 \sigma-\eta=\tfrac12E_2[g_+^2(k_1-k_2)^2]>0:
\]

the Gaussian pair has full support, and the integrand is positive on an open
set. Thus Sigma is positive definite for every c in (-1,1).

## Conditional acceleration law and what independent mixing loses

Let H=(H_1,H_2)^T and D=diag(d_1,d_2). Equation (1) and (2) give

\[
 \begin{pmatrix}a_1''\\a_2''\end{pmatrix}
 =\tfrac12GD(MH+\Xi).
\]

Consequently, conditional on the entire first-layer root A_0,

\[
 E[a''\mid A_0]=\tfrac12GDMH,\qquad
 \operatorname{Cov}(a''\mid A_0)=\tfrac14GD\Sigma DG.   \tag{6}
\]

This is an exact conditional Gaussian law. Its covariance is positive definite
almost surely because G and Sigma are positive definite and d_1,d_2>0.
For the vector first-layer weight A, the corresponding covariance is
one quarter times sum_{b,j} d_b d_j Sigma_{bj} u_b u_j^T, positive definite
on span{u_1,u_2} and zero on its orthogonal complement.

In particular,

\[
 \operatorname{Cov}(a_1'',a_2''\mid A_0)
 =\tfrac14\{c\sigma(d_1^2+d_2^2)+(1+c^2)\eta d_1d_2\}. \tag{7}
\]

For c>=0 this conditional covariance is strictly positive: the Gaussian
innovation also produces correlated accelerations of the two samples.

There are three distinct inadequate replacements:

1. A fresh independent reverse source R=Xi drops MH and violates (4).
   In particular it misses the strict mean signal effect proved below.
2. A deterministic reverse source R=MH drops the positive conditional
   covariance (6).
3. Independent innovations for the two samples drop eta>0 and give the wrong
   covariance in (6), even if both separate innovation variances are matched.

Nonzero innovation alone does **not** prove that every description by population
laws is impossible. For this first jet, one joint first-population law containing
(A_0,H,Xi,R), together with the second-population source law (Z,g,U) and the
matrices C,M,Sigma, is sufficient. What fails is retaining separate marginal
densities and imposing independent mixing between reused calls or sample
sources. A full initialized operator T, or an equivalent consistent source
calculus, is allowed fixed information in the q=1 population model.

For later calls the required information includes prior same-population source
overlaps, forward/reverse compatibility (4), and their joint innovation
covariances. For example, even the next second-layer acceleration contains

\[
 z_a''(0)=\tfrac12\sum_b C_{ba}U_b+T[d_a a_a''(0)],
\]

whose last term reuses T on a source built using T*. Its distribution cannot
be obtained by declaring another independent Gaussian draw. The assigned
two-direction conditioning formula describes which additional transcript
constraints must be honored. This report does not claim a finite law-only
closure for all later source calls.

## Strict common-mode amplification and correlation increase

Let lambda_+=m+n and lambda_-=m-n be the eigenvalues of M on the sample sum
and difference directions. They obey

\[
 \lambda_+>0,\qquad \lambda_-<0.                       \tag{8}
\]

Both signs hold for every c in (-1,1), including negatively correlated inputs.
To prove them, apply (4) in the sum and difference directions:

\[
 (v+\kappa)\lambda_+
 =E_2[(Z_1+Z_2)U_1]
 =\tfrac12E_2[(Z_1+Z_2)g_+(k_1+k_2)]>0.
\]

The last product is positive almost surely: tanh Z_1+tanh Z_2 has the
same sign as Z_1+Z_2 and k_1+k_2>0. For the difference direction,

\[
 (v-\kappa)\lambda_-
 =\tfrac12E_2[(Z_1-Z_2)(U_1-U_2)].
\]

Since k_1-k_2=-(g_1-g_2)(g_1+g_2),

\[
 U_1-U_2=-2g_+^2(g_1-g_2),\qquad
 (v-\kappa)\lambda_-
 =-E_2[(Z_1-Z_2)g_+^2(g_1-g_2)]<0.
\]

Strictness again follows from full support and strict monotonicity of tanh.

Now put S_+=a_1+a_2 and S_-=a_1-a_2. The identities
d_1-d_2=-(H_1-H_2)(H_1+H_2) and (6) give

\[
 E[S_+''\mid A_0]
 =\frac{1+c}{4}(H_1+H_2)
 \{\lambda_+(d_1+d_2)-\lambda_-(H_1-H_2)^2\},           \tag{9}
\]

\[
 E[S_-''\mid A_0]
 =\frac{1-c}{4}(H_1-H_2)
 \{\lambda_-(d_1+d_2)-\lambda_+(H_1+H_2)^2\}.           \tag{10}
\]

The brace in (9) is strictly positive and the brace in (10) strictly
negative. Also H_1+H_2 has the sign of S_+, and H_1-H_2 the sign of S_-.
Therefore

\[
 S_+ E[S_+''\mid A_0]>0,\qquad
 S_- E[S_-''\mid A_0]<0
\]

almost surely. This is a conditional-mean statement, not a pointwise assertion
about the random acceleration: (6) supplies fluctuations in both directions.

Let V_+(s)=E_1[(a_1(s)+a_2(s))^2] and
V_-(s)=E_1[(a_1(s)-a_2(s))^2]. The L^2 second-order expansion already
proved gives

\[
 V_+'(0)=V_-'(0)=0,\qquad
 V_+''(0)=2E_1[S_+S_+'']>0,\qquad
 V_-''(0)=2E_1[S_-S_-'']<0.                           \tag{11}
\]

Thus the first-layer common-input variance expands while the difference
variance contracts at the first nontrivial order. The innovation has zero
conditional mean and hence makes no contribution to these second derivatives;
its nonzero conditional variance is nevertheless part of the population jet.

On a symmetric trajectory the first-layer preactivations are centered and
exchangeable. Centering and exchangeability through this order also follow
directly from the displayed initialization law. Their correlation is

\[
 r(s)=\frac{V_+(s)-V_-(s)}{V_+(s)+V_-(s)},\qquad r(0)=c.
\]

Since V_+(0)=2(1+c), V_-(0)=2(1-c), and both first derivatives vanish,

\[
 r''(0)=\frac{(1-c)V_+''(0)-(1+c)V_-''(0)}4>0.          \tag{12}
\]

In particular r(s)>c for all sufficiently small positive s. At c=0 this
creates positive first-layer correlation; at c>0 it strengthens the existing
correlation. The raw cross moment has positive second derivative as well,
because (E_1[a_1a_2])''(0)=(V_+''(0)-V_-''(0))/4>0. Since ds/dt=2 at
zero and these observables have zero first derivative, their physical-time
second derivatives are four times the displayed feature-time values.

This is the positive mechanism obtained here. It neither asserts monotonicity
at later times nor establishes successful fitting. Its dependence on the
forward-induced reverse response is exact: replacing R by a root-independent
centered innovation makes both expectations in (11) vanish.

## Claim boundary and frozen provenance

Proved from the supplied generated initialization and q=1 equations: the
first-source law (2)--(5), its nondegenerate conditional acceleration law (6),
the response eigenvalue signs (8), and the conditional-mean amplification and
initial correlation conclusions (9)--(12). Their interpretation along time is
conditional on the specified local strong symmetric population solution.

Open here: existence/uniqueness and trained-width identification of that
fixed-q solution, a law-only finite closure of all later reused sources,
positive-horizon control beyond the local expansion, global convergence, and
any q-dependent approximation theorem. A correct first population jet proves
none of those bridges. No experiments or external retrieval were performed.

Actual scientific inputs were the supervisor's assignment and exactly the
following inclusive line ranges. SHA-256 hashes are of the concatenated raw
bytes of each range, preserving line endings, at the time of reading:

| Source | Lines | SHA-256 |
|---|---:|---|
| docs/02-gaussian-reuse.qmd | 1--170 | 1da78af8a55e0d00589209fc2137a3bba3f920783da83335cc4999c9a955c64d |
| docs/03-local-population.qmd | 174--278 | a23dce9b5d2a3de98f274f51cf31cff5426546318c35a3a8208671883ea9e13d |
| paper/main.tex | 178--443 | ac3b1ea9c36571f11d388efbf143cbcd6be7ea64c9a07389231c100ef5fe3fea |
| paper/main.tex | 498--525 | 8d7f6f9ece5b75c074991ed63451e4aa64e2ae8d084e2e462ad62c6d0c4ea553 |

Required process reading: /etc/codex/skills/solve-math-rigorously/SKILL.md;
/etc/codex/skills/investigate-conjectures/SKILL.md and its
references/research-contract.md and references/adversarial-audit.md. No other
study, prior result, agent finding, or scientific repository passage was read.
Only this report was written.
