# Integrated comparison investigation: proved components and remaining gap

2026-10-04. Continuation of this study, following the user's authorization
to pursue the combined compact-compressor, Legendre-closure, and
independent-dense comparisons. This is the current synthesis for that
request. The components below have different scopes; they are not a
single theorem with the intersection of all desired improvements.

**The fully explicit general integrated theorem requested by the user
has not been proved.** In particular the general independent-dense upper
bound in the requested norm remains near-root rather than strict root,
and the sharp bounded-activation compression constants have not been
transferred to the unbounded-activation class. These are mathematical
gaps, not notation choices or additional assumptions being silently made.

The new actual nonlinear lower bounds, the whole-sphere upper-bound
extension, and the label-sensitive source count are proved components.
No trained-network experiment, manuscript change, promotion, or Git
mutation was performed. All results retain internal study status.

## 1. Common model and the exact comparison requirement

Write v=x/sqrt(d), so queries satisfy ||v||=1. With L hidden layers of
width n, the canonical dense model is

\[
 z^{(1)}=Av,\qquad z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\qquad
 h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad
 f_n=w^\top h^{(L)}/n.
\]

The entries of A_0 are independent N(0,1), entries of W_0^(ell) are
independent N(0,1/n), all initialized blocks are independent, and w_0=0.
The loss is m^(-1)sum_a(f_n(x_a)-y_a)^2, with physical mobilities
(n,1,...,1,n). Define the residual r_a=f_n(x_a)-y_a and the backward
signals by k_a^(L)=w, delta_a^(ell)=phi_ell'(z_a^(ell)) times
k_a^(ell), and k_a^(ell)=W^(ell+1)^T delta_a^(ell+1). Thus

\[
 \dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\quad
 \dot W^{(\ell)}=-\frac2{mn}\sum_a
 r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},\quad
 \dot w=-\frac2m\sum_a r_ah_a^{(L)}.
\]

For fixed training data, define

\[
 Q^{(0)}_{ab}=v_a^\top v_b,\qquad
 Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
 \quad Z\sim N(0,Q^{(\ell-1)}),
\]
\[
 Y=\|y\|_2/\sqrt m,\qquad
 \gamma=\lambda_{\min}(Q^{(L)})>0.
\]

There is no division by m in gamma. Compatible quotients of redundant
observations, when allowed by the inherited theorem, must be taken before
asserting a positive gap. Every upper comparison is at the same physical
time, using

\[
 \|f-g\|_*=
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|f(t,x)-g(t,x)|.
 \tag{1}
\]

The endpoint is included when the compared trajectories converge. A
finite-time lower bound also lower-bounds the supremum over finite times
without requiring endpoint convergence. One model cannot silently be
evaluated at another model's fitting or loss-matched time.

All asymptotic probability statements here concern each sufficiently
large width at fixed data, depth, labels, dimension and confidence. They
do not assert one event holding simultaneously over independently drawn
initializations at every integer width. Width thresholds remain
unquantified whenever inherited convergence or a CLT is used.

## 2. What is established, and what is still missing

| Comparison or quantity | Current rigorous conclusion | Limitation |
| --- | --- | --- |
| Compact autonomous model versus its realized dense run | Strict C/sqrt(n), in (1); polylogarithmic retained size | Sharp explicit constants/storage are available for bounded analytic activations; the unbounded extension still has qualitative constants and an older log exponent |
| Independent canonical dense runs | C_delta exp(K sqrt(log(e+n)))/sqrt(n), now in (1) | The unbounded subpolynomial multiplier has not been removed; general numerical constants and label cap are not newly quantified |
| Original RMS-clock Legendre closure versus its realized dense run | Strict C/sqrt(n) at the explicit order schedule in Section 5 | General physical/label constants and probability width threshold are inherited qualitatively |
| Actual dense variability during nonlinear training | Explicit lower scale sqrt(m)Y/sqrt(n) on an orthogonal-data construction | General-m result is at a specified finite time, not the fitted endpoint |
| Actual dense variability at the fitted endpoint | Explicit |y|/sqrt(n) lower bound for one-input, two-tanh model | Not an endpoint result for general data or arbitrary depth |
| Label dependence of compact size | Actual (Ym/gamma)^4 leading factor retained | Tanh scope; quadratic retained sample arrays remain; no linear-m theorem |

The broad inherited dense/Legendre upper scope allows C^3 activations
with bounded first three real derivatives and unbounded values. The
compact unbounded-value extension has a different analytic requirement:
a finite value at zero and a bounded holomorphic derivative on a strip.
The sharp numerical bounded-activation theorem cannot be enlarged merely
by deleting its activation-value bound. Forward normalization alone does
not justify that substitution.

## 3. New nonlinear variability lower bounds

Use two tanh hidden layers, d>=m+1, training inputs x_a=sqrt(d)e_a,
and query x_*=sqrt(d)e_(m+1). Labels may have any fixed signs. Put

\[
 Q=\mathbb E\tanh^2Z,\qquad
 \gamma_2=\mathbb E\tanh^2(\sqrt QZ),\qquad Z\sim N(0,1).
\]

The limiting training Gram is gamma_2 I_m. In particular this
construction has fixed, nondegenerate conditioning; its lower bound is
not produced by sending gamma to zero.

For 0<Y<=1/m and every fixed 0<delta<1, the actual independent dense
runs satisfy, for all sufficiently large n,

\[
 \Pr\!\left\{
 |f_n(t_\delta,x_*)-\widetilde f_n(t_\delta,x_*)|
 \ge\frac{\gamma_2^2\delta^{5/2}}{112000}
       \frac{\sqrt mY}{\sqrt n}\right\}\ge1-\delta,
 \qquad
 t_\delta=\frac{m\gamma_2\delta^{3/2}}{56000}.
 \tag{2}
\]

This is [INTEGRATED_LOWER_CONFIDENCE.md](INTEGRATED_LOWER_CONFIDENCE.md),
with a complete [internal check](INTEGRATED_LOWER_CONFIDENCE_CHECK.md).
The earlier [nonlinear lower proof](INTEGRATED_DENSE_LOWER_ROUTE.md)
also gives a smaller fixed-probability bound with fully explicit width
inequalities valid in a stated growing-m region. The confidence refinement
in (2) uses a fixed-dimensional CLT, so it does not inherit that quantified
growing-m region automatically.

The critical proof step is a bound on the complete nonlinear remainder,
not a formal Taylor series with width-independent error. The untrained
query column g=A_0 e_(m+1) remains Gaussian and independent of the whole
training path. Both the query predictor and its remainder are odd in g.
For t=m tau, their exact decomposition and the proved estimate are

\[
 f_n(m\tau,x_*)=2m\tau K_y(g)+R_n(m\tau,g),\qquad
 K_y(g)=\frac{(H_0^{(2)}y)^\top\tanh(W_0\tanh g)}{mn},
\]
\[
 \mathbb E[R_n(m\tau,g)^2\mathbf1_{\mathcal T}]
 \le7000^2\frac{mY^2\tau^4}{n}.
 \tag{3}
\]

Here T is the explicitly bounded training-only initialization event.
The initialized term fluctuates at scale sqrt(m)Y tau/sqrt(n), whereas
the full nonlinear remainder has an extra factor tau. This is why a
fixed positive physical time can be used, without shrinking it with
width. Choosing the time for the desired confidence and controlling its
actual remainder proves (2).

The m factor has a concrete origin. Under mean loss, fitting an
orthogonal collection takes a time of order m. Initial query correlations
with the m trained features then contribute independent leading
fluctuations weighted by the labels, with total size ||y||/sqrt(n).
This explains sqrt(m)Y. It does not prove that the general upper
coefficient Y(m/gamma)^(3/2) is sharp in m or gamma.

For one input the same method continues to the actual fitted endpoint.
The exact endpoint decomposition has a leading initialized interpolant
and a conditionally centered remainder of size at most
9000|y|^3/(g_0^4 sqrt(n)), where

\[
 g_0=\tfrac12\mathbb E\tanh^2(\sqrt{Q/2}Z)>0.
\]

Unlike an O(y^3) endpoint error, this remainder can be compared to
|y|/sqrt(n) uniformly in width. The explicit fixed-probability endpoint
theorem and its complete reconstruction are in the nonlinear lower proof
and [INTEGRATED_COMPARISON_CHECK.md](INTEGRATED_COMPARISON_CHECK.md).
The fixed-confidence refinement is recorded separately in
[INTEGRATED_ENDPOINT_CONFIDENCE.md](INTEGRATED_ENDPOINT_CONFIDENCE.md).
Explicitly, for every fixed 0<delta<1 and

\[
 0<|y|\le \frac{g_0^2\delta^{3/4}}{\sqrt{144000}},
 \qquad
 \Pr\!\left\{
 |f_n(\infty,x_*)-\widetilde f_n(\infty,x_*)|
 \ge\frac{\delta|y|}{4\sqrt n}
 \text{ and both runs converge and fit}\right\}\ge1-\delta
 \tag{3a}
\]

for sufficiently large n. The numerical constants and the nonlinear
endpoint construction pass the coordinator's complete reconstruction in
[INTEGRATED_ENDPOINT_COMPARISON_CHECK.md](INTEGRATED_ENDPOINT_COMPARISON_CHECK.md).
The width threshold's CLT part remains qualitative. No general-m
endpoint persistence is inferred from (2).

## 4. Initialization law and why it does not finish the general theorem

[INTEGRATED_INITIAL_VARIABILITY.md](INTEGRATED_INITIAL_VARIABILITY.md)
and its [complete check](INTEGRATED_INITIAL_VARIABILITY_CHECK.md) prove a
finite-depth initialized covariance CLT with an explicit covariance
recursion, for C^2 activations of linear growth with bounded first two
derivatives. They also compute the exact derivative of the fitted
predictor with respect to label amplitude at zero amplitude.

For orthogonal inputs, an independent orthogonal query, and odd
activations, write q_0=1,

\[
 q_\ell=\mathbb E\phi_\ell(\sqrt{q_{\ell-1}}Z)^2,\quad
 a_\ell=\mathbb E\phi_\ell'(\sqrt{q_{\ell-1}}Z),\quad
 \nu_0=0,\quad \nu_\ell=q_\ell^2+a_\ell^4\nu_{\ell-1}.
\]

The two-copy zero-label endpoint response has limiting Gaussian variance
2mY^2 nu_L/q_L^2 after multiplication by sqrt(n), and
1<=nu_L/q_L^2<=L whenever these variances are nonzero. For a common odd
forward-normalized activation, nu_L=sum_(j=0)^(L-1)a^(4j); a fixed
nonlinear activation has |a|<1, whereas identity has a=1.

These are distributional limits of initialized/linear-response objects.
They are not a claim that the actual fixed-label trained network has the
same Gaussian limit. Finite-width inverse-Gram moments need not even be
uniformly integrable for the broader smooth class; the check gives a
specific warning example. The actual nonlinear remainder estimates in
Section 3, rather than an exchange of width and label limits, supply the
valid finite-label lower bounds.

## 5. General Legendre order: the quarter power is reusable

[INTEGRATED_LEGENDRE_REUSE.md](INTEGRATED_LEGENDRE_REUSE.md) uses the
user-authorized prior DEPTH_EXTENSION_RESULT.md. That study proves the
same-width bound

\[
 \|f_{n,q}^{\rm Legendre}-f_n\|_*
 \le C e^{K\sqrt{\log(e+n)}}q^{-2}\sqrt{\log(e+q)}
 \tag{4}
\]

on an event common to every order q. The original RMS clock, original
prefix initialization, both forward and backward memories, fixed
Gaussian mixers and closure's own residual are retained. This is a
later internally checked study theorem; the current paper's theorem
still has a separate unquantified width remainder. They are not the
same statement. The [reuse check](INTEGRATED_LEGENDRE_REUSE_CHECK.md)
verifies this scope and the order/state arithmetic below.

An explicit schedule, without knowing K numerically, is

\[
 q_n=\left\lceil n^{1/4}
              \exp\{[\log(e+n)]^{3/4}\}\right\rceil
       =n^{1/4+o(1)}.
 \tag{5}
\]

It makes (4) at most C/sqrt(n), and in fact o(1/sqrt(n)), for sufficiently
large width. The probability threshold and C,K,label threshold in (4)
are still qualitative. Thus (5) is an explicit order schedule, not a
fully numerical version of all inherited constants. The same bound holds
for all q>=q_n on the same per-width event. The general quarter power
does not require extending the special two-tanh one-sixth result.

The moving-state and fixed-mixer counts are, respectively,

\[
 2(L-1)mnq_n+n(d+1)+1,\qquad (L-1)n^2.
 \tag{6}
\]

Consequently the general closure saves moving state. It does not save
total retained storage if the original Gaussian mixers are stored as
dense arrays.

## 6. Explicit Y in compact storage, without suppressing sample overhead

[INTEGRATED_LABEL_STORAGE_ROUTE.md](INTEGRATED_LABEL_STORAGE_ROUTE.md)
and its [complete check](INTEGRATED_LABEL_STORAGE_CHECK.md) improve the
ordinary-tanh source count at arbitrary fixed depth. All prior label
conditions and the corrected-readout error coefficient are retained.
Put u=Ym/gamma, S=16u, and ell_n=log(en). For d>=2,

\[
 A_n(Y)=\frac{2^{20}9^d}{d!}\frac{U(S)}a
              c_q(S)^{-(d-1)}u^2\ell_n^{3d/2+1},
 \qquad a=\tfrac12,
 \tag{7}
\]
\[
 \operatorname{size}(C)\le
 1020(L+1)[A_n(Y)+2m+d+1]^2+10m(d+1).
 \tag{8}
\]

U(S) and c_q(S) are finite explicitly defined activation/depth/dimension
recurrences in that proof's equations (9)--(12), not fitted constants.
The d=1 time-only count is supplied there separately. Equation (7)
retains the actual label RMS instead of substituting its maximum allowed
value. The leading squared term in (8) has a factor (Ym/gamma)^4.

The improvement follows from retaining Y in the physical speed: the
available complex-time radius has coefficient
a/[64YSU(S)], rather than capping that coefficient by an arbitrary
universal number. The actual radius still tends to zero as
1/sqrt(log n), so the short-contour argument applies eventually.
Its sufficient width deteriorates as Y decreases; in particular one
condition is

\[
 \log(en)\ge
 \frac{a^2(\gamma/m)^2}{16384Y^4U(S)^2}.
 \tag{9}
\]

This is a fixed-positive-label asymptotic refinement, not a uniform
shrinking-label theorem or a practical moderate-width guarantee.

At fixed activity u the leading coefficient has no extra separate m or
gamma factor. At fixed absolute Y it still has fourth powers of
m/gamma. Moreover the initialized source additions and retained dense
metrics/sample solves have quadratic sample storage. The current
construction requires a rank-m training feature matrix and stores
associated dense m-by-m arrays. Their removal would require a different
representation or solver, not a reinterpretation of (8). This is not a
universal lower bound against all autonomous encodings.

For two tanh hidden layers the inherited explicit certificate remains

\[
 Y\le2.8\times10^{-7}\gamma/m,\qquad
 \|f_C-f_n\|_*\le
 2.8\times10^5Y(m/\gamma)^{3/2}/\sqrt n.
 \tag{10}
\]

The label-sensitive storage improvement does not introduce an additional
small-label condition, but it also does not enlarge the activation class.
Its source and runtime proofs still use bounded tanh values.

## 7. What blocked the strict general dense upper bound

[INTEGRATED_DENSE_VARIABILITY_ROUTE.md](INTEGRATED_DENSE_VARIABILITY_ROUTE.md)
extends the inherited independent-copy estimate to the whole sphere and
all times, including the endpoint:

\[
 \Pr\left\{\|f_n-\widetilde f_n\|_*
 \le\frac{C_\delta e^{K\sqrt{\log(e+n)}}}{\sqrt n}\right\}
 \ge1-\delta.
 \tag{11}
\]

This part is checked in INTEGRATED_COMPARISON_CHECK.md. It handles
unbounded activation values in the inherited smooth class. The constants
and positive label threshold depend on the fixed problem; no fully
explicit version of them is claimed here. The factor in (11) is
unbounded, so (11) does not settle the strict root target.

Two routes were examined beyond that inherited estimate:

1. Prediction-directed variational energy. In normalized parameter
   coordinates Theta=(A,sqrt(n)W^(2),...,sqrt(n)W^(L),w), let p(s) be the
   backward adjoint of the final query gradient. The residual-weighted
   Hessian term contains mixed products of the form
   n^(-1)sum_i |k_(a,i)^(ell)| |D_Theta z_(a,i)^(ell)[p(s)]|^2.
   Existing marginal signal moments and averaged operator moments do not
   control this aligned product. Factoring it as though the trained
   signal and adjoint were independent would be invalid.
2. Independent-neuron replacement. The exact cavity expansion retains
   incoming and outgoing Gaussian roots, learned edges and each run's
   own residual. Its leading scalar influence again requires a
   prediction-directed response estimate. Existing vector remainder
   bounds are too large for the required 1/n single-neuron influence,
   and the inherited high-probability localization is not automatically
   enough to sum Efron--Stein errors over all neurons.

The complete second attempt is
[INTEGRATED_NEURON_REPLACEMENT_ROUTE.md](INTEGRATED_NEURON_REPLACEMENT_ROUTE.md).
It records the exact open inequalities instead of making them extra
theorem assumptions. Failure of these estimates supplies no slower-rate
counterexample. The new lower results are consistent with root-width
variability; they do not prove the general upper bound or resolve a
dense-to-population bias.

## 8. What accuracy-cost conclusions are justified

For fixed admissible problem parameters, the proved compact-versus-dense
root error yields sufficient compact retained size
O(log^(3d+2)(1/epsilon)) in the sharp bounded-analytic scope. The sharp
tanh label-sensitive coefficient is (7)--(8). The existing broader
unbounded analytic extension has the older log exponent
2[d(L+5)+1], not this sharpened one.

The general Legendre schedule gives sufficient moving size
epsilon^(-5/2+o(1)) at error epsilon versus the same dense run; retaining
its fixed mixers costs epsilon^(-4). Ordinary dense width n with an
error scale proportional to 1/sqrt(n) has storage of order epsilon^(-4).

The lower construction makes that last calibration necessary, in the
sufficiently-wide asymptotic regime, for independent canonical dense
variability at the probability levels proved in
INTEGRATED_LOWER_CONFIDENCE.md. For example its delta=1/4 statement
forces n>=c_*^2 mY^2/epsilon^2 for a dense-copy upper tolerance epsilon
with success probability greater than 1/4, where
c_*=gamma_2^2/3584000. A comparison of each run to a common deterministic
reference uses 2epsilon and one quarter of that width constant.

These statements justify asymptotic representation savings in their
stated scopes. They do not imply a universal lower bound on arbitrary
compressors, sharp constants in m/gamma, a general fitted-endpoint lower
bound, or the requested single fully explicit theorem for unbounded
activations with all previous asymptotic improvements retained.

There is also a concrete comparison against ACTUAL fitted dense
variability. For one input and two tanh layers, the completely stated
corollary in INTEGRATED_ENDPOINT_COMPARISON_CHECK.md intersects the
compressor upper event with the endpoint lower event. Under its explicit
label cap, with probability at least 1-delta it gives

\[
 \|f_C-f_n\|_*
 \le \frac{2.24\times10^6}{\delta\gamma^{3/2}}
             \|f_n-\widetilde f_n\|_*.
 \tag{12}
\]

The retained compressor size is polylogarithmic in n, with actual Y in
its explicit coefficient. This comparison uses a proved endpoint lower
bound, not an assumed dense upper rate or a population-bias estimate.
Its large constant prevents a practical near-one noise-ratio claim.
The scope remains one-input/two-tanh; (12) does not fill the missing
general theorem.

## 9. Provenance and checks

Scientific inputs were this study's own complete relevant proofs/checks,
the current manuscript and its mathematical includes, the maintained
notation contract, and the user-authorized
studies/dense_cutoff_population_rate_20261001 proofs. No unrelated study
was imported. Earlier chat-level promises were not treated as proofs.

Contributors to this continuation: coordinator (initialized covariance
CLT, confidence transfer, lower/upper reconstruction, Legendre schedule,
assembly); integrated_dense_lower (nonlinear trajectory/endpoint lower
proof); integrated_dense_spread (sphere upper transfer and adjoint audit);
integrated_storage_y (label-sensitive source radius); and
neuron_replacement_strict_root (alternative influence route).
Checks and refinements were performed by initial_variability_check,
integrated_storage_check, integrated_legendre_reuse_check, and
endpoint_lower_confidence, with exact input scopes recorded in their
reports. They are internal mathematical reconstructions, not independent
promotion reviews.
