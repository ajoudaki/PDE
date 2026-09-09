# Signed-response and Hessian-energy boundaries for the original L3 problem

2026-09-08. This note investigates two proposed replacements for absolute source-response rows. It proves two new obstruction statements for *the proposed proof hypotheses*, not a counterexample to the requested trained trajectory or to any positive activation coefficient.

The activation remains exactly `phi_theta(z)=a z+theta atan(z)`, `a=1-theta`, `0<theta<=1/2`. No overall gain, offset, frozen-layer algorithm or changed initialization is substituted for the target. The source-transport construction in Section 1 is an abstract finite-program diagnostic; Section 2 uses actual raw parameter states of the original three-hidden-layer model. Neither construction is asserted to be reachable by its GF from canonical initialization.

## 1. Smooth bounded-time queries and signed Gaussian projection still permit focusing

The earlier Walsh example did not include time regularity. The following construction shows that all of these stronger assumptions together are still insufficient for exponential-moment transport:

- a fixed time interval [0,1];
- three sample-query paths with Gram exactly I at every time;
- uniformly bounded smooth query fields;
- uniform H1([0,1];L2) bounds on query paths;
- a causal smooth Gaussian observation using the exact phi_theta, with uniform subGaussian values and uniform H1([0,1];L2) norm;
- covariance-weighted/RKHS norm at most one for its signed expected Gaussian derivative;
- even a uniform H1([0,1];L2) norm of the transported response itself.

Nevertheless the transported response's psi1 norm diverges. Thus temporal H1 regularity and causality do not alone eliminate the query-span focusing identified previously.

### Construction of the query path

Let N>=2 be even, epsilon=1/N, and let the neuron probability space be the four-dimensional unit cube with coordinates `(x,v_1,v_2,v_3)` and uniform measure. Put

\[
 \chi_j(x)=\sqrt2\cos(2\pi jx),\quad 1\le j\le N,
 \qquad b_i(v_i)=\sqrt2\sin(2\pi v_i),\quad 1\le i\le3.
\]

The chi_j are orthonormal in L2. Each b_i has mean zero and L2 norm one; the b_i are mutually orthogonal and orthogonal to every chi_j. All these functions are smooth and bounded. If Gaussian coordinates are desired, compose x and v_i with the standard Gaussian cumulative distribution function applied to four independent Gaussian roots; the same laws result, with smooth bounded functions of those roots.

Fix a smooth bump eta supported in (-1/2,1/2), with eta(0)=1 and 0<=eta<=1. Let

\[
 t_j=(j-1/2)/(2N),\qquad p_j(t)=\eta(4N(t-t_j)).
\]

The supports are disjoint and lie in (0,1/2). Define

\[
 u_1(t)=\frac{b_1+\epsilon\sum_jp_j(t)\chi_j}
 {\sqrt{1+\epsilon^2\sum_jp_j(t)^2}},
 \qquad u_2(t)=b_2,\quad u_3(t)=b_3.
 \tag{1}
\]

At every time these three queries are orthonormal. In particular their spatial correlations are zero, satisfying every pairwise absolute-separation condition with 0<delta<=1. Their L-infinity norms are at most three. The paths are smooth, start and finish at their baseline fields, and have uniformly bounded time H1 norms.

For the derivative estimate, at a point where p_j is the only active pulse, u_1 moves on the unit circle spanned by b_1 and chi_j. Direct differentiation gives

\[
 \|u_1'(t)\|_2^2
 =\frac{\epsilon^2 p_j'(t)^2}{(1+\epsilon^2p_j(t)^2)^2}
 \le\epsilon^2p_j'(t)^2.
\]

Consequently

\[
 \int_0^1\|u_1'(t)\|_2^2\,dt
 \le4\epsilon^2N^2\int\eta'(s)^2ds
 =4\int\eta'(s)^2ds.
 \tag{2}
\]

At the query times,

\[
 u_j:=u_1(t_j)=\frac{b_1+\epsilon\chi_j}{\sqrt{1+\epsilon^2}},
 \qquad
 \langle u_j,u_k\rangle
 =\frac{1+\epsilon^2\mathbf1_{j=k}}{1+\epsilon^2}.
 \tag{3}
\]

### Gaussian source and causal observation

Let G_0,G_1,...,G_N be independent standard Gaussians. The named source vector with the covariance in (3) is

\[
 X_j=\frac{G_0+\epsilon G_j}{\sqrt{1+\epsilon^2}}.
\]

It may be embedded in the smooth Gaussian source process obtained by using the coefficients in (1). Its marginal variances are one and its mean-square H1 bound equals (2), by equality of covariance Grams.

Set alpha_j=(-1)^j. Since N is even, `sum_j alpha_j=0`. Thus

\[
 S_N=\frac{\sqrt{1+\epsilon^2}}{\epsilon\sqrt N}
           \sum_j\alpha_jX_j
     =\frac1{\sqrt N}\sum_j\alpha_jG_j
 \sim N(0,1).
 \tag{4}
\]

Let lambda be a fixed smooth function with values in [0,1], equal to zero on [0,1/2] and equal to one near t=1. Define the observation

\[
 F_N(t)=\phi_\theta(\lambda(t)S_N).
 \tag{5}
\]

This is causal: before all the queries have been collected its value is zero; when it uses their values all t_j are strictly in the past. Because `|phi_theta(z)|<=|z|` and `|phi_theta'|<=1`,

\[
 \sup_t\|F_N(t)\|_p\le C\sqrt p,
 \qquad
 E\int_0^1|F_N'(t)|^2dt\le\int_0^1|\lambda'(t)|^2dt,
 \tag{6}
\]

with constants independent of N. Its derivative in the whitened Gaussian vector `(G_1,...,G_N)` has Euclidean norm at most one, so even Gaussian-space Lipschitzness is uniform.

### Exact signed response and focusing

Put

\[
 m_\theta(\lambda)=E\phi_\theta'(\lambda G)\in[a,1],
 \qquad \beta(t)=\lambda(t)m_\theta(\lambda(t)).
\]

The expected named-source derivative is exactly

\[
 d_j(t)=E\partial_{X_j}F_N(t)
 =\frac{\sqrt{1+\epsilon^2}}{\epsilon\sqrt N}
       \alpha_j\beta(t).
\]

Transporting it to the actual query fields gives

\[
 V_N(t)=\sum_jd_j(t)u_j
       =\frac{\beta(t)}{\sqrt N}\sum_{j=1}^N\alpha_j\chi_j.
 \tag{7}
\]

Both the covariance-weighted derivative norm and the transported L2 norm are beta(t): if Sigma is the covariance in (3), then

\[
 d(t)^T\Sigma d(t)=\beta(t)^2=\|V_N(t)\|_2^2\le1.
 \tag{8}
\]

In particular the exact inverse-free Gaussian projection bound is fully respected. Since `|g'|<=1`, differentiation of m_theta gives `|m_theta'|<=theta E|G|<=1/2`. Hence `|beta'|<=3|lambda'|/2`; (7) and orthonormality show that the transported response also has uniformly bounded H1([0,1];L2) norm.

At t=1, beta(1)>=a>=1/2. For `|x-1/2|<=1/(6N)`, each summand satisfies

\[
 \alpha_j\cos(2\pi jx)=\cos(2\pi j(x-1/2))\ge1/2.
\]

That interval has probability 1/(3N), and therefore

\[
 V_N(1)\ge\beta(1)\sqrt{N/2}
 \quad\text{on a set of probability }1/(3N).
 \tag{9}
\]

For every fixed p>2 this yields

\[
 \|V_N(1)\|_p\ge
 \frac{\beta(1)}{\sqrt2\,3^{1/p}}N^{1/2-1/p}\longrightarrow\infty.
 \tag{10}
\]

If the psi1 norm is defined by `E exp(|V|/K)<=2`, (9) gives

\[
 \|V_N(1)\|_{\psi_1}
 \ge\frac{\beta(1)\sqrt{N/2}}{\log(6N)}
 \longrightarrow\infty.
 \tag{11}
\]

There is no uniform integrability of squared magnitudes either: after the threshold in (9) exceeds any fixed cutoff, the squared tail expectation is at least beta(1)^2/6.

### What the causal time-step factor does and does not add

The final source response only uses strictly past query slots. On mesh intervals of length h=1/(2N), write d_j=h k_j. This is a literal causal step-factor representation, but `|k_j|` has order N^(3/2). Merely displaying h_j in a source derivative is therefore not a uniform density estimate.

If instead one assumes a uniform absolute density bound `|k_j|<=K`, then the uniformly bounded query values would immediately give `|sum h_j k_j u_j|<=3KS`. That stronger assumption does exclude this construction. It is exactly the kind of response estimate that the covariance/RKHS replacement was trying to avoid proving.

The observation uses the exact admissible phi_theta, and all source coordinate maps in this finite construction are smooth with bounded derivatives at each fixed N. Nevertheless the query path was designed rather than derived from the neural GF. Equations (9)-(11) therefore disprove a source-tail theorem based solely on the listed regularity/covariance/causality hypotheses. They do not show focusing of the canonical trained neural queries. A successful replacement theorem must use additional restrictions imposed by the actual training equations.

## 2. The positive Hessian term does not close raw-ball response energy

For a finite smooth gradient system, or wherever a variational equation and the required second directional derivatives are justified, let `J` be the sample predictor differential and let v be a homogeneous tangent perturbation. The loss Hessian decomposes as

\[
 D^2L=J^*J+\sum_i r_iD^2f_i,
\]

and the linearized GF energy obeys

\[
 \frac12\frac{d}{dt}\|v\|_{\rm raw}^2
 =-\|Jv\|_2^2-\sum_i r_iD^2f_i[v,v].
 \tag{12}
\]

Thus the first term provides real damping. The second term cannot be bounded below using only the actual network's raw L2 ball, even when the three inputs are perfectly separated. The following example is inside the original canonical raw state space.

### Original-L3 counterexample to a raw-ball Hessian lower bound

Take d>=3 and three orthogonal RMS-unit inputs, so Gamma=I_3 and every pairwise absolute correlation is zero. Keep all hidden parameters at their canonical initialization. Let q_2>0 be the common second-layer feature variance. Oddness and the fresh initialized Gaussian forward rules give

\[
 \langle h_i^2,h_j^2\rangle=q_2\mathbf1_{i=j},
 \qquad(Z_1^3,Z_2^3,Z_3^3)\sim N(0,q_2I_3).
\]

Here `a^4<=q_2<=1`. For arbitrarily small epsilon>0, choose a measurable set E_epsilon of probability epsilon contained in `{-2<=Z_1^3<=-1}` and depending only on Z_1^3. Such sets exist because this Gaussian interval has positive nonatomic measure. Set

\[
 u_\epsilon=\epsilon^{-1/2}\mathbf1_{E_\epsilon},
 \qquad C=u_\epsilon.
\]

This modifies only the readout and has raw distance exactly one from canonical initialization. Every primal L2 norm and every initialized action norm remains bounded independently of epsilon. Take labels `(1,1,1)` and consider the unit Hilbert--Schmidt perturbation of the final hidden action

\[
 \Delta B=u_\epsilon\otimes \frac{h_1^2}{\sqrt{q_2}},
 \qquad\|\Delta B\|_{\rm HS}=1.
 \tag{13}
\]

The other parameter directions are zero. Orthogonality implies

\[
 \Delta z_1^3=\sqrt{q_2}\,u_\epsilon,
 \qquad\Delta z_2^3=\Delta z_3^3=0.
\]

Along the one-dimensional raw line `B+s Delta B`, differentiating twice under the integral is justified for each fixed epsilon: C and Delta z are bounded fields and phi has bounded first two derivatives. No global twice-Frechet-differentiable Hilbert loss is assumed. The predictor derivatives obey

\[
 |Df_1[\Delta B]|
 =\sqrt{q_2}\,\epsilon^{-1}
       E[\mathbf1_E\phi_\theta'(Z_1^3)]\le\sqrt{q_2},
\]

\[
 D^2f_1[\Delta B,\Delta B]
 =q_2\epsilon^{-3/2}
       E[\mathbf1_E\phi_\theta''(Z_1^3)]
 \ge q_2\frac{4\theta}{25}\epsilon^{-1/2}.
 \tag{14}
\]

The last inequality uses
`phi_theta''(z)=-2theta z/(1+z^2)^2>=4theta/25` for -2<=z<=-1. The other two predictor derivatives vanish. On E the activation is negative, so `f_1=E[C phi_theta(Z_1^3)]<0` and `r_1=f_1-1<-1`. Consequently

\[
 D^2L[\Delta B,\Delta B]
 \le q_2\left[1-\frac{4\theta}{25}\epsilon^{-1/2}\right]
 \longrightarrow-\infty.
 \tag{15}
\]

The positive `J^*J` part in this calculation is at most q_2, whereas negative residual curvature is unbounded. This proves that the full original loss has no raw-ball lower Hessian bound of the form `D^2 L>=-C_R I`, even on the radius-one ball and with Gamma=I.

In a tangent-energy argument based on (12), a uniform bound using only primal L2 sizes therefore cannot hold. One must control the specific reachable readout/cotangent tails, the correlation between those fields and tangent directions, or some smaller admissible tangent class. Equation (15) is not a reachable trajectory counterexample: canonical population C starts at zero, and no claim is made that GF produces these concentrated readouts.

## 3. Outcome of these two attempts

The nonperturbative same-array value lemma from `three_hard_nonlinear_20260908.md` remains valid: actual finite response bounds plus actual primal L2 bounds imply Gaussian source values on arbitrary finite intervals, without amplitude smallness.

The proposed shortcuts for obtaining or avoiding those response bounds now have precise negative tests:

1. Covariance/RKHS control, temporal H1 regularity, bounded spatial query values, smooth finite programs and causality still permit transport focusing, even when all three spatial query Grams are perfectly conditioned at every time.
2. True-gradient Hessian damping does not yield raw-ball tangent-energy control in the actual L3 model; negative curvature can diverge on a fixed primal ball.

These results do not make the requested theorem false or show every signed-response proof impossible. They identify additional reachable-state structure that such a proof must actually establish. I have not established that structure or a sufficient positive theta_delta in this bounded search.
