# C-X3 reference sources: first independent route

Frozen first-round author derivation, 2026-09-20. This report does **not**
prove depth-three substantial-training continuation. It identifies the
remaining response estimate, supplies exact conditional reference bounds,
and rules out two proposed norm-based shortcuts. It is not an independent
review or a promoted result. No computation, experiment, or Git operation
was performed.

## 1. Assignment and actual read coverage

The assigned question is continuation of the orthogonal, equal-weight,
opposite-label tanh reference at three hidden layers, then at every fixed
depth, through feature level b=1 or the physical fitting horizon
T=log(8)/(4m_L), with m_L=q_L/2. All actions and reverse actions must be
the actual initialized Gaussian actions and their adjoints.

Read completely:

* `CONTRACT.md`, all 333 lines;
* `CH3_LOCAL_PROOF.md`, all 777 lines;
* maintained `docs/global_nonlinear.md`, C.1–C.2, lines 2454–3440;
* maintained `docs/global_nonlinear.md`, C.4.5.1, lines 5475–6103;
* the solve-math-rigorously and investigate-conjectures skills, including
  the latter's adversarial-audit and proof-search-orchestration references.

No other study, route report, maintained scientific section, or external
scientific source was consulted. The scoped assignment replaced author
startup reading. All notation needed below was supplied by these inputs,
so `docs/NOTATION.md` was not needed. An initially combined read was
truncated; the scientific files/ranges were subsequently read in complete
separate chunks. No claim below relies on content hidden by truncation.

## 2. Exact feature dynamics and conditional all-depth bounds

Write phi=tanh, y_1=1, y_2=-1, H_a^ell=phi(Z_a^ell), and use the contract's
raw Hilbert space with one full-row L2 component, L-1 HS increments, and
one readout L2 component. For the orthogonal inputs, the feature equation
is

\[
 c_s=h:=\tfrac12\sum_a y_aH_a^L,\qquad
 (w_a)_s=\tfrac12y_a\Delta_a^1,\qquad
 (K_\ell)_s=\tfrac12\sum_a y_a\Delta_a^\ell\otimes H_a^{\ell-1}.
 \tag{1}
\]

Here P_a^L=c, Delta_a^ell=phi'(Z_a^ell)P_a^ell, and
P_a^ell=A_(ell+1)^* Delta_a^(ell+1). In particular the two initialized
edge labels at depth three are never combined or replaced by independent
reverse maps.

The local construction in CH3 applies to (1): in the weighted equations
of C.2 take weights 1/2 and deterministic residual coefficients
r_a=-y_a/2. Its proof permits these deterministic coefficients. Thus the
feature equation starts on a positive interval. This use does not extend
the local interval.

There are elementary finite bounds on **every already existing** feature
interval [0,S]. Choose M=10, the action bound used in CH3, and define
continuous increasing polynomials, starting at the top, by

\[
 B_L(s)=M+s^2/2,\qquad
 B_\ell(s)=M+\int_0^s v\prod_{j=\ell+1}^L B_j(v)\,dv
                 \quad(2\le\ell<L).
 \tag{2}
\]

Since |h|<=1, |c(s)|<=s coordinatewise. Downward backpropagation gives

\[
 \|P_a^\ell(s)\|_2,\ \|\Delta_a^\ell(s)\|_2
       \le s\prod_{j=\ell+1}^L B_j(s),\qquad
 \|A_\ell(s)\|_{op}\le B_\ell(s).
 \tag{3}
\]

The last inequality follows by integrating (1), using
||a tensor b||HS=||a||2||b||2 and ||H||2<=1, in descending layer order.
For the row,

\[
 \|w_s\|_{L^2(\mathbb R^2)}
 \le 2^{-1/2}s\prod_{j=2}^L B_j(s).
 \tag{4}
\]

For depth three the explicit first bounds are
B_3=M+s^2/2 and B_2=M+Ms^2/2+s^4/8. Corresponding mesh-independent
bounds hold for finite feature Euler programs: the discrete positive sums
are bounded by right-endpoint Riemann sums of the same increasing
polynomials on any fixed slightly enlarged horizon. These bounds have
no response coefficients in their definitions.

Consequently finite-time escape of the **raw norms** is excluded, and an
existing strong feature curve has a strong raw limit at any finite
terminal time: (3)–(4) bound its velocity on that interval. Continuity of
the raw vector field also gives its limiting velocity. Neither statement
constructs a continuation from that endpoint in an infinite-dimensional
space. In particular it does not establish the hypotheses needed to
restart the local Gaussian-source theorem there.

For completeness, the conditional fitting mechanism is valid at every
fixed depth. Let J be the directional derivative of h with respect to
all hidden parameters. Successive bounded-gate curve chain rules and
actual adjunction give hidden_s=J*c and

\[
 h_s=JJ^*c,\qquad
 b_s=\|h\|_2^2+\|J^*c\|_{hidden}^2=\|\theta_s\|_{raw}^2,
 \qquad b=\langle c,h\rangle.
 \tag{5}
\]

No derivative of J is taken. These are statements about a strong curve,
not Frechet differentiability of the L2-valued activation map. For
g=||c||2>0,

\[
 g_s=b/g,\qquad
 g_{ss}=\{\|h\|_2^2-g_s^2+\|J^*c\|_{hidden}^2\}/g\ge0.
 \tag{6}
\]

The inequality is Cauchy–Schwarz. Initially the two features at every
layer have diagonal Gram q_ell I: oddness and the independent orthogonal
first roots start the induction, and the independent fresh **forward**
edge at initialization preserves independent centered Gaussian input
coordinates. Thus

\[
 q_0=1,\quad q_\ell=E\tanh^2(\sqrt{q_{\ell-1}}G)>0,
 \qquad m_L=\|h(0)\|_2^2=q_L/2>0.
 \tag{7}
\]

As c(s)=s h(0)+o_L2(s), g_s(0+)=sqrt(m_L). Convexity implies
g_s>=sqrt(m_L) and g>=s sqrt(m_L); therefore g cannot return to zero.
Also ||h||2>=g_s. Hence b_s>=m_L wherever the strong continuation exists.

The initialized action law and the feature equation are invariant under
swapping the two input coordinates and changing c to -c. Local uniqueness
therefore yields f_1=b=-f_2. On any uniquely continued symmetric branch
below b=1 the physical clock is ds/dt=2(1-b), so

\[
 (1-b)_t=-2b_s(1-b),\qquad
 R_*(t)=(1-b)^2\le e^{-4m_Lt}.
 \tag{8}
\]

If continuation through first level b=1 were proved, (5)–(8) would give
that level at s_dagger<=1/m_L, global physical dynamics, and a strong
endpoint. Indeed the bounded continuous b_s makes the clock integral
diverge at the first level; and

\[
 \|\theta(s_2)-\theta(s_1)\|_{raw}
 \le\sqrt{(s_2-s_1)(b(s_2)-b(s_1))},\qquad
 \|\theta(s(t))-\theta(s_\dagger)\|_{raw}
 \le(1-b(t))/\sqrt{m_L}.
 \tag{9}
\]

Whole-circle prediction is Lipschitz in raw state on the bounded set (2),
by finite-depth forward subtraction. These observations would then yield
the endpoint prediction estimate. They remain conditional here because
the continuation premise has not been proved. In particular (8) does
not by itself authorize evaluation at T=log(8)/(4m_L).

## 3. Exact depth-three source equations

For a fixed finite feature Euler program with step lengths h_s and
weights omega_b=1/2, freeze deterministic contractions, response
coefficients, and source covariance laws when differentiating, exactly
as in C.2. Define

\[
 C^{\ell}_{ak,bs}=E\,\partial_{\eta^{\ell}_{b,s}}
                         H^{\ell-1}_{a,k},\qquad
 Q^{\ell}_{ak,bs}=E\,\partial_{\xi^{\ell}_{b,s}}
                         \Delta^{\ell}_{a,k}.
 \tag{10}
\]

The letter Q avoids confusing these response coefficients with the
actual weight actions A. For ell=2,3 the exact reused-action equations
are

\[
 Z^\ell_{a,k}=\xi^\ell_{a,k}
                 +\sum_{b,s<k}F^\ell_{ak,bs}\Delta^\ell_{b,s},
 \quad
 P^{\ell-1}_{a,k}=\eta^\ell_{a,k}
                 +\sum_{b,s\le k}D^\ell_{ak,bs}H^{\ell-1}_{b,s},
 \tag{11}
\]
\[
 F^\ell_{ak,bs}=C^\ell_{ak,bs}
       +h_s\omega_b y_b E[H^{\ell-1}_{b,s}H^{\ell-1}_{a,k}],
\]
\[
 D^\ell_{ak,bs}=Q^\ell_{ak,bs}
       +1_{s<k}h_s\omega_b y_b E[\Delta^\ell_{b,s}\Delta^\ell_{a,k}].
 \tag{12}
\]

The forward covariance is E[H H] and the reverse covariance is
E[Delta Delta], on the appropriate source population. Oriented Gaussian
source families are independent; times and anchors within each family
need not be. Equations (11)–(12) retain both the response and learned-rank
terms, with the feature-clock sign and probability-weight factors.

On a fixed horizon S, let J>=1 dominate all squared delta RMS bounds in
(3). Suppose one could bound

\[
 |C^\ell_{ak,bs}|\le c_\ell h_s\omega_b,\qquad
 \sum_{b,s\le k}|Q^\ell_{ak,bs}|\le a_\ell.
 \tag{13}
\]

Then |F^ell|<=f_ell h_s omega_b with f_ell=c_ell+J, and the D row sums
are at most d_ell=a_ell+JS. Bounded activations yield the useful
**pointwise** estimates

\[
 |P^2_{a,k}|\le|\eta^3_{a,k}|+d_3,\qquad
 |P^1_{a,k}|\le|\eta^2_{a,k}|+d_2.
 \tag{14}
\]

The Gaussian variances in (14) are already bounded by (3). Thus finite
caps (13), uniformly over meshes, give the required subGaussian source
tails immediately. For bounded tanh it is unnecessary to bootstrap
subGaussian forward activations: they are bounded by one. The missing
part is precisely uniform control of the **responses** in (13), not
ordinary RMS control or the variance of the Gaussian innovations.

The middle differentiation is

\[
 \partial\Delta^2=\phi''(Z^2)P^2\partial Z^2
                    +\phi'(Z^2)\partial P^2.
 \tag{15}
\]

At the top, |c|<=S controls the analogous coefficient. At the middle,
(15) contains the unbounded reverse field eta^3 plus its response. The
readout bound does not remove this term.

## 4. A strengthened clock attempt, and its precise limitation

The first-layer clock can remove its own unbounded multiplicative
coefficient. Let j_X=phi'(j), j(0,g)=g, and write
w_a=j(X_a,g_a). Then (phi(j))_X=phi'(j)^2 lies in [0,1] and the exact
continuous equation is (X_a)_s=y_a P^1_a/2. To test the stronger route,
use finite programs that Euler-update X, K_2, K_3, and c and recompute
w=j(X,g). Their source representation remains (11)–(12); only the
coordinate rule at layer one changes. This is a proposed construction
of the same continuous raw feature equation, not a claim that its finite
steps equal actual raw GD. A completed convergence/identification proof
would still be needed after closing its bounds.

A single eta^2 pulse at time s has X-size h_s/2=h_s omega_b. Since the
derivative of phi(j) is at most one and the D^2 row sum is at most d_2,
discrete Gronwall gives

\[
 |C^2_{ak,bs}|/(h_s\omega_b)\le e^{Sd_2/2}.
 \tag{16}
\]

This estimate is deterministic and contains no random P^1. It improves
the direct C.2 estimate at the first layer, but does not close the middle
response problem.

The remaining bounds can be written explicitly. For top forward-slot
derivatives let V^3_k be the maximal full derivative-row sum of Z^3 up to
time k. Differentiating c's time sum costs at most S V^3_k. Differentiating
Delta^3=phi'(Z^3)c costs at most 3S V^3_k, because |phi''|<=2 and |c|<=S.
Therefore

\[
 \sum|Q^3|\le3S\exp(3f_3S^2).
 \tag{17}
\]

For middle derivatives, both a full xi^2 derivative row and an eta^3
single pulse have subsequent coefficient at most
2|P^2|+d_3<=2|eta^3|+3d_3. Put
W= sum_(u,b) h_u omega_b |eta^3_(b,u)| on the preceding times. Every
eta^3 marginal has variance at most S^2. Jensen with total weight at
most S and the elementary Gaussian bound E exp(lambda|G|)<=2 exp(lambda^2/2)
gives

\[
 E e^{\lambda W}\le2e^{\lambda^2S^4/2}.
 \tag{18}
\]

No temporal independence or maximum of Gaussian coordinates is used.
The full row is bounded by exp(3f_2d_3S+2f_2W). The single pulse starts
with f_2 h_s omega_b and has the same subsequent growth. Taking expectation,
and applying Cauchy–Schwarz to the full row's last delta derivative, yields

\[
 |C^3_{ak,bs}|/(h_s\omega_b)
 \le2f_2\exp(3f_2d_3S+2f_2^2S^4),
 \tag{19}
\]
\[
 \sum|Q^2|\le\sqrt2(2S+3d_3)
                  \exp(3f_2d_3S+4f_2^2S^4).
 \tag{20}
\]

These estimates are all finite for already fixed caps. To use them as
one uniform self-preserving cap argument one would have to choose c_2,
c_3,a_3,a_2 at least their right sides (16)–(20), with f_ell=c_ell+J
and d_ell=a_ell+JS. That sufficient cap system has **no finite solution
for S>=1/2**. Indeed its weaker consequences are

\[
 c_2\ge e^{Sa_2/2},\qquad c_3\ge2c_2,\qquad
 a_3\ge3S e^{3c_3S^2},\qquad a_2\ge3\sqrt2 a_3.
\]

Writing x=c_2, they imply for S>=1/2

\[
 x\ge\exp\!\left(\frac{9\sqrt2}{8}e^{3x/2}\right)>e^x>x.
 \tag{21}
\]

The first strict inequality follows from
(9sqrt(2)/8)e^(3x/2)>x for x>=0; for example e^(3x/2)>=1+3x/2 makes
it immediate. This is a contradiction. It concerns this **sufficient
uniform-cap method**, not the actual responses, and its numerical
threshold is not intrinsic. Sharper signed estimates or time-dependent
controls could invalidate the obstruction to this particular method.

It nevertheless pinpoints why simply enlarging the onset constants,
even after applying the useful first-layer clock, does not prove the
desired horizon. Before b=1, |c|<=s and ||h||2<=1 give b<=s. Reference
risk <=1/8 requires b>=1-1/sqrt(8)>1/2, so a feature interval covered by
these caps cannot reach that fitting level. An interval-by-interval
application would additionally have to control the accumulated response
of the **same** initialized actions; it cannot reset source histories to
independent Gaussians or silently reuse initialization independence.

## 5. Actual Gaussian-adjoint counterexample to the bounded-source shortcut

There is no tail bound depending only on a Gaussian action's L2 operator
norm and the supremum norm of an adaptive source, even on its canonical
generated space. The following one-edge calculation uses its actual
adjoint and does not replace it by an independent Gaussian call.

Let G be a lower-population Gaussian root independent of A_0. Choose an
event E in its sigma-field with probability p in (0,1), and set H=1_E.
The forward source Z=A_0H is N(0,p) on the upper population. Define

\[
 U=\tanh(Z/\sqrt p),\quad
 a=E[G\tanh G]>0,\quad v=E\tanh^2G>0.
 \tag{22}
\]

Then ||U||infinity<=1, and the exact one-query transpose reuse formula is

\[
 A_0^*U=\frac{a}{\sqrt p}\,1_E+\Gamma,
 \qquad \Gamma\sim N(0,v),\quad\Gamma\perp G.
 \tag{23}
\]

Here is a finite conditional derivation. For a lower input vector h with
||h||^2/n tending to p, condition on z=A_0h. The conditional matrix mean
is z h^T/||h||^2. Its transpose applied to u=tanh(z/sqrt(p)) is
h(z^T u)/||h||^2, whose coefficient tends to
E[Z tanh(Z/sqrt(p))]/p=a/sqrt(p). The unused matrix is an independent
Gaussian matrix with its lower input direction h projected away.
Its transpose applied to u has asymptotic coordinate variance v. Removing
the one h-direction changes normalized squared norm by O(1/n), because
the associated scalar projection has O(1) variance. This yields the
independent Gaussian term in (23), with the same lower-root coordinates.
It is the one-source case of the maintained conditional reuse calculation.

Indicators are admissible L2 limits of smooth bounded root functions.
For each fixed p the forward action, tanh instruction and reverse action
are L2-continuous, so the calculation also holds on the generated
completion. One may instead use smooth approximations throughout and
pass to this limit. The scalar 1/sqrt(p) is fixed before any width limit.

In (23), ||A_0^*U||2^2=a^2+v<=2, while R_p=a/(2sqrt(p)) tends to infinity.
On E intersect {Gamma>=0}, whose probability is p/2, the field is at least
a/sqrt(p)>R_p. Therefore

\[
 \|(A_0^*U)1_{|A_0^*U|>R_p}\|_2^2\ge a^2/2.
 \tag{24}
\]

In particular neither uniformly vanishing L2 cutoff tails nor a uniform
subGaussian constant follows from those bounded-input/operator/RMS
conditions. For any fixed gamma>0,
E exp(gamma|A_0^*U|^2)>= (p/2) exp(gamma a^2/p), which diverges as p->0.
This construction also shows why covariance-normalized response estimates
cannot be replaced by a rank-free operator-norm argument.

This is **not** a reached-state counterexample for (1). The normalization
in (22) need not be produced by the prescribed finite-time reference
training. Its force is narrower: a proof using only bounded readout,
bounded tanh, bounded action norm, and bounded raw energy omits exactly
the adaptive-response information that distinguishes a reached training
state from this example.

## 6. Exact remaining claim and route status

The local C.2 source theorem and CH3's local raw flow remain usable. The
new exact points established here are the all-depth polynomial norm
bounds (2)–(4), the depth-three signed source equations (10)–(12), the
improved first-clock attempt (16)–(20), its stated uniform-cap limitation,
and the actual-adjoint diagnostic (22)–(24). Equations (5)–(9) verify the
conditional fitting and endpoint implications, without converting them
into existence statements.

The missing theorem is a mesh-uniform reached-source estimate for the
actual feature reference on both edges through the fitting level. One
sufficient version is finite response caps (13) on a horizon reaching
b>=1-1/sqrt(8), or directly uniform subGaussian bounds for all required
backward fields and the corresponding Euler/source construction. A
weaker tail class could also work if its comparison modulus is proved
strong enough for uniqueness and approximation; arbitrary vanishing L2
tails do not suffice in the exponential Gronwall bound of CH3.

Even a completed reference estimate would leave transfer to a positive
supported law neighborhood and approximation of each admitted law to be
proved. No statement here supplies that transfer or the closure and
actual-GD bridges on the long horizon.

| Claim | Status | Decisive reason |
|---|---|---|
| Fixed-depth reference exists initially | Available locally | C.2 with r_a=-y_a/2 and CH3 construction |
| Raw norms cannot diverge on finite feature intervals | Proved conditionally on existence | Descending polynomial bounds |
| Strong raw limit at a finite existing endpoint | Proved | Uniform velocity bound |
| Continuation from that endpoint | Open | Reached source/response control absent |
| Bounded readout and action norms alone yield reference tails | Invalid inference | Actual Gaussian reuse diagnostic |
| The displayed clock plus one uniform cap scheme reaches fitting | Refuted for this scheme | Inconsistent sufficient caps for S>=1/2 |
| The prescribed reference cannot continue | Not claimed | Neither diagnostic is a reached-reference counterexample |
| L=3 substantial-training branch, then all fixed L | Open | Source bottleneck unresolved before law transfer |

Route recommendation: stop enlarging these uniform caps. Reopen this
route for a signed-response estimate, a quantitative bound on accumulated
response that survives interval continuation, or another mechanism
specific to the reached two-anchor trajectory. No result in this report
licenses local Picard on an arbitrary raw L2 ball, reinitialization of a
Gaussian edge, or a claim that the substantial-training branch is proved.

## 7. Second round: covariance-weighted response and signed cancellation

Second-round frozen derivation, 2026-09-20. The supervisor requested this
specific refinement after the first round was frozen: replace absolute
response row sums by the combined response, and use the actual top
operand Delta^3=c sech^2(Z^3), the readout equation, and swap symmetry.
No additional scientific source or another route's findings were read.
The first-round conclusions are preserved; this section records a
stronger reduction and the precise bridge still absent.

### 7.1 The exact Hilbert-space contraction

Fix any finite top-edge source program. Denote its lower source vectors
H^2_(a,k) by V_i and its top forward Gaussian sources xi^3_(a,k) by xi_i,
where i abbreviates the anchor/time index. The source covariance identity
defines an isometry

\[
 I:\overline{\operatorname{span}\{V_i\}}
       \longrightarrow\overline{\operatorname{span}\{\xi_i\}},
 \qquad I V_i=\xi_i.
 \tag{25}
\]

Indeed the squared norms of every finite linear combination are equal.
Relations of zero covariance are quotiented out automatically; no
covariance inverse or rank assumption is involved. Let Pi_1 be the
orthogonal projection in the upper-population L2 space onto this Gaussian
linear span. For U_i=Delta^3_i, the actual combined reverse response is

\[
 R_i=\sum_j Q^3_{ij}V_j=I^{-1}\Pi_1 U_i,
 \qquad \|R_i\|_2\le\|U_i\|_2.
 \tag{26}
\]

To verify (26), Gaussian integration by parts with frozen covariances
gives E[xi_j U_i]=sum_r E[xi_j xi_r] E[partial_(xi_r) U_i].
Thus U_i-I R_i is orthogonal to every xi_j. Every fixed program has the
required named-source derivatives by C.2. Enlarging the source family
does not change this projection for an operand measurable in the earlier
Gaussian family: its centered future Gaussian innovations are independent
of that family. This also defines the contraction on the completed
carrier of any already constructed source limit.

Consequently, on every interval where the actual source representation
has been constructed (in particular the proved local interval),

\[
 \|R^3_a(s)\|_2\le\|\Delta^3_a(s)\|_2\le s.
 \tag{27}
\]

This replaces a possibly large absolute response sum by an exact bound
with constant one. It retains all signed cancellations and all covariance
degeneracies. But I is an L2 isometry between two different coordinate
populations, not a pointwise map or an isometry of Orlicz norms. The upper
random variable Pi_1 U_i is Gaussian; its image I^{-1}Pi_1 U_i need not
be Gaussian. This distinction is essential.

### 7.2 A time-envelope improvement and the one remaining tail

The actual top operand has stronger time regularity than a general
bounded adaptive source. Use the polynomials in (2) on an already
constructed depth-three interval [0,S], and set

\[
 C_Z=1+B_3(S)^2\{1+B_2(S)^2/2\},\qquad
 D_S=1+2S^2 C_Z.
 \tag{28}
\]

Equation (1) gives ||(w_a)_s||2<=s B_2(S)B_3(S)/2,
||K_2,s||HS<=s B_3(S), and ||K_3,s||HS<=s. Forward differentiation gives

\[
 \|H^2_{a,s}\|_2
 \le s B_3(S)\{1+B_2(S)^2/2\},\qquad
 \|Z^3_{a,s}\|_2\le s C_Z.
\]

Since |c|<=s, ||c_s||2<=1 and |phi''|<=2, the actual top gate product is
strongly C1 in L2 and

\[
 \|\Delta^3_{a,s}\|_2
 \le 1+2s\|Z^3_{a,s}\|_2\le D_S.
 \tag{29}
\]

The product rule is legitimate here because c and its velocity are
pointwise bounded; the gate multiplier is bounded and strongly continuous
on each fixed L2 vector. This argument would not automatically justify
an L2 derivative of the middle product phi'(Z^2)P^2.

On the fixed source carrier, (26) is a bounded linear operator. Therefore
R^3_a is strongly C1 and ||R^3_(a,s)||2<=D_S. A coordinatewise absolutely
continuous version satisfies

\[
 \sup_{s\le S}|R^3_a(s)|\le V_a:=\int_0^S|R^3_{a,s}(v)|\,dv,
 \qquad \|V_a\|_2\le S D_S.
 \tag{30}
\]

Thus the combined response has a square-integrable temporal envelope.
This is a concrete strengthening of its separate-time L2 bound.

For comparison, its Gaussian reverse innovation admits the stronger
envelope that is actually needed. Let eta_a(s) be the isonormal image of
Delta^3_a(s), so its covariance is the required E[Delta^3_a(s)Delta^3_b(t)].
Its mean-square derivative is Gaussian with variance at most D_S^2.
Fubini provides an absolutely continuous version with eta_a(0)=0 and
sup_(s<=S)|eta_a(s)|<=G_a:=integral_0^S |eta_(a,s)(v)|dv. Cauchy–Schwarz
in time and Jensen give, for 0<=gamma<1/(2S^2D_S^2),

\[
 E e^{\gamma G_a^2}
 \le\frac1S\int_0^S E e^{\gamma S^2\eta_{a,s}(v)^2}\,dv
 \le(1-2\gamma S^2D_S^2)^{-1/2}.
 \tag{31}
\]

No independence of times is assumed. The learned-rank part is bounded
coordinatewise as well:

\[
 |K_3(s)^*\Delta^3_a(s)|
 \le\tfrac12\sum_b\int_0^s
       \|\Delta^3_b(v)\|_2\|\Delta^3_a(s)\|_2\,dv
 \le s^3/2.
 \tag{32}
\]

The complete actual reverse field consequently has the envelope

\[
 \sup_{s\le S}|P^2_a(s)|\le G_a+V_a+S^3/2.
 \tag{33}
\]

The Gaussian part G_a has the proved subGaussian bound (31), and the
learned part is deterministic. The sole uncontrolled tail in this
decomposition is V_a, the envelope of the transported first-chaos
response. Estimate (30) does not establish an exponential Orlicz bound
for V_a. In particular (31) cannot be transferred through I^{-1}.

These are estimates on each constructed source interval, with constants
depending only on S and the polynomial bounds. They expose the missing
estimate needed for a uniform long-interval construction; they do not
assume such a construction already exists.

### 7.3 The actual signed top derivative and its feedback remainder

There is an exact way to separate the bounded direct derivative of the
true top operands from the lower-layer feedback. In a finite source
program let U_i=Delta^3_i, Z_i=Z^3_i, and
t_j=h_s omega_b y_b when j=(b,s). The readout is
c_k=sum_(time(j)<k) t_j phi(Z_j). Define the random causal matrix

\[
 B_{ij}=c_k\phi''(Z_i)\,1_{i=j}
  +1_{\operatorname{time}(j)<k}
            \phi'(Z_i)t_j\phi'(Z_j),\qquad i=(a,k).
 \tag{34}
\]

It is the derivative of U with respect to the full Z transcript. Its
absolute row sum is at most 3S, although its entries retain their signs.
Write X_ij=partial_(xi_j) U_i, and let F be the strictly causal top
forward-memory matrix in (11). The exact finite triangular identities are

\[
 X=B(I+FX),\qquad X=(I-BF)^{-1}B.
 \tag{35}
\]

The inverse is a finite causal sum: BF is strictly lower in time. Thus
(35) is an identity, with no convergence assumption about an infinite
Neumann series. The derivative here is precisely C.2's named-source
derivative: all deterministic expectations, source covariances, and
response coefficients in F are frozen. The lower population's dependence
on the reverse sources is already represented by C^3 in F. Its expected
coefficients are not differentiated again with respect to one upper
coordinate's xi slot. There is no omitted pathwise lower-population
derivative: populations have distinct coordinate spaces, and the fixed
program's upper coordinate equation is exactly Z=xi+F U. Differentiating
the full law or perturbing a deterministic response coefficient would be
a different derivative, to which (35) does not claim to apply. Split

\[
 F=C^3+T,\qquad
 T_{ij}=h_s\omega_b y_b E[H^2_jH^2_i],\quad |T_{ij}|\le h_s\omega_b.
 \tag{36}
\]

For a lower coordinate omega, let
Y_i(upper,omega)=sum_j X_ij(upper)V_j(omega). Then

\[
 Y=B(V+TY+C^3Y),\qquad R_i=E_{upper}Y_i.
 \tag{37}
\]

The direct term E[BV] is bounded pointwise by 3S. The true readout
integral and the fixed tanh gate therefore do prevent the arbitrary
normalization used in the first-round diagnostic from appearing as a
direct top derivative.

More strongly, if C^3=0, the actual operand and readout identities imply
an all-horizon estimate without any covariance inverse. Since |V_j|<=1
and |T_ij|<=h_s omega_b, (37) gives

\[
 \max_{a,u\le k}|Y_{a,u}|
 \le3S+3S\sum_{s<k}h_s\max_b|Y_{b,s}|.
\]

Discrete Gronwall yields

\[
 \|R_i\|_\infty\le3S e^{3S^2}.
 \tag{38}
\]

Thus bounded sources that do not depend on the top edge's reverse
sources have a complete top-tail estimate at every finite horizon. The
actual reference has C^3 generally nonzero: layer two learns from
A_3^*Delta^3. Equation (38) is not a theorem for that reference.

Taking expectation in the actual (37) leaves terms

\[
 \sum_{j,r} C^3_{jr}\,E_{upper}[B_{ij}Y_r].
 \tag{39}
\]

The covariance-weighted bound (26) controls E Y, not E[B Y], E|Y|, or
the samplewise tangent operator X. In (39), B and Y depend on the same
Gaussian source history, so replacing E[B Y] by E[B]E[Y] is invalid.
The Bessel bound for the opposite combined response C^3 Delta^3 likewise
controls a value-space L2 norm; it does not bound the operator taking
Delta-history values to their Gaussian derivatives in (35). No reverse
Poincare inequality for that evolving history span has been proved.
These are the exact unclosed terms of this sharper strategy.

### 7.4 What the signed symmetry actually gives

Let U denote the measure-preserving involution swapping the two anchor
roots and c to -c. It intertwines the Gaussian source isometry in (25).
Consequently

\[
 U R^3_1=-R^3_2,\qquad U R^3_2=-R^3_1.
 \tag{40}
\]

The average (R^3_1+R^3_2)/2 is odd and the difference
(R^3_1-R^3_2)/2 is even under this involution, so those two components
are L2-orthogonal. This is a genuine cancellation, already retained in
(26). It supplies no bound on the magnitudes within either parity space.

For example, on a probability space with an independent sign epsilon and
an event E of mass p preserved by U, the paths
R_1(s)=R_2(s)=s epsilon 1_E/sqrt(p), with U epsilon=-epsilon, obey (40),
||R_a(s)||2=s, and ||R_(a,s)||2=1. Their temporal envelopes have no
uniform exponential moment as p decreases. Their normalized direction
lies in the span of the bounded functions epsilon 1_E and
-epsilon 1_E. This example tests only parity, covariance-weighted norm,
and temporal L2 regularity. It is not asserted to be a reached reference
or to satisfy its forward equation. It shows exactly why these newly
proved constraints still need a dynamical bridge to Orlicz control.

Nor is the random diagonal term of (34) pointwise dissipative. Let
Y_1,Y_2 be the independent initial top Gaussians, each of variance q_2,
and h_0=(phi(Y_1)-phi(Y_2))/2. On the actual local reference,

\[
 s^{-1}c(s)\phi''(Z^3_1(s))
                  \longrightarrow h_0\phi''(Y_1)\quad\hbox{in L2}.
 \tag{41}
\]

The limit is negative when Y_1>Y_2>0, and positive when Y_2>Y_1>0.
Choose compact rectangles inside either region to keep its magnitude
away from zero; Gaussian full support gives each positive probability.
Convergence in probability then implies both signs occur in the actual
coefficient at all sufficiently small positive times. Thus a proposed
signed contraction in (39) cannot be justified by claiming that the
gate term c phi''(Z) always damps perturbations. A more delicate averaged
inequality could still hold, but none has been established here.

### 7.5 An actual initial combined-response expansion

The stronger method does give a bounded leading response for the
prescribed operands, without any absolute row-sum estimate. The
polynomial velocity bounds imply Z^3_a(s)-Y_a=O_L2(s^2),
c(s)-s h_0=O_L2(s^3), and hence

\[
 \Delta^3_a(s)=s h_0\phi'(Y_a)+O_{L^2}(s^3).
 \tag{42}
\]

Use (26) and the contraction of Pi_1. The Gaussian linear projection of
h_0 phi'(Y_a) uses only the initial Y_1,Y_2, regardless of how many
later correlated sources have been adjoined. Put

\[
 \alpha=\tfrac12 E[(\phi\phi')'(Y)]
       =\frac{E[Y\phi(Y)\phi'(Y)]}{2q_2}>0,
 \qquad \beta=\tfrac12(E\phi'(Y))^2>0,
 \quad Y\sim N(0,q_2).
 \tag{43}
\]

Gaussian integration by parts gives the equality for alpha. The
integrand in its numerator is positive away from zero. Differentiating
the bounded smooth operand in (42) with respect to Y_1,Y_2 gives the
coefficient rows (alpha,-beta) and (beta,-alpha). Therefore

\[
 R^3_1(s)=s\{\alpha H^2_1(0)-\beta H^2_2(0)\}+O_{L^2}(s^3),
\]
\[
 R^3_2(s)=s\{\beta H^2_1(0)-\alpha H^2_2(0)\}+O_{L^2}(s^3).
 \tag{44}
\]

The leading terms are bounded, explicitly signed, and obey (40).
For instance alpha<=1/2 because (phi phi')'<=1 pointwise, while
beta<=1/2. An L2 remainder in (44) does not inherit their supremum or
Orlicz bounds; a small L2 error can be concentrated on a very rare set.
Thus (44) confirms the benign actual initial response but is not a
continuation theorem.

### 7.6 Second-round conclusion

The covariance-weighted strategy proves more than the first-round
absolute-cap argument: the top combined response is an exact L2
contraction, it has a square-integrable temporal envelope with explicit
polynomial constants, and both the Gaussian innovation and learned shift
have the stronger envelopes (31)–(32). It also yields the actual local
signed expansion (44), and an all-horizon bound when the lower reverse
response C^3 vanishes.

For the actual reference, the missing step is now specific: bound the
envelope V_a in (30) in an exponential Orlicz class, or obtain another
stability-sufficient estimate for the correlations (39). Swap parity,
bounded gate derivatives, the actual readout integral, and Bessel's
inequality do not yet provide that bound. The direct top terms are
controlled; the response of the learning middle layer to its own reused
reverse source is still the unresolved feedback. No inference from
conditional time regularity to long-horizon existence is made. This
second route therefore strengthens the reduction but leaves the
substantial-training continuation theorem open.
