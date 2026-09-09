# R5: weighted first-chaos response bridge

Analytic sidecar, 2026-09-06. One mechanism test; no experiments or
subagents. The two-sample theorem remains OPEN.

The first-chaos quadratic form and the contrast action budget give a
useful new bound on the actual learned response shift, and on the part
of the expected-derivative shift represented by the current two sample
features. They do not, by themselves, give uniform stronger-than-L2
tails for the temporal-innovation part. Below is an explicit obstruction
to that particular inference: smooth shifted-arctan feature histories
with uniformly coercive two-sample Grams and bounded action admit
Gaussian expected-derivative response rows whose actual evaluation on
those histories has no uniform Lp bound for any p>2, or even a uniform
exponential-absolute moment.

The obstruction is to an inequality using the stated covariance,
action, and gate premises alone. The constructed rows are not identified
with rows attained by the coupled two-query Euler law. Thus this does
not disprove tails for the actual training trajectory, or rule out a
proof that uses the causal equations to restrict its response rows.
Sections 1--3 give identities/inequalities for those actual rows; Section
4 tests exactly what can be inferred after retaining only the proposed
weighted first-chaos/energy controls.

## Scope, sources, and conventions

Read in full:

- CONTRACT_AND_LEDGER.md;
- SHIFTED_ARCTAN_CONTRAST_ROUTE.md;
- TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md;
- /etc/codex/skills/solve-math-rigorously/SKILL.md;
- /etc/codex/skills/investigate-conjectures/SKILL.md and its references
  research-contract.md, evidence-ledger.md, and adversarial-audit.md.

The research-contract and audit instructions determine the narrow
claim tested here and the distinction between an algebraic obstruction
and an attained-trajectory counterexample. No external theorem about
the network is imported. Gaussian integration by parts is proved in the
form used below. The fixed activation is

\[
 \phi(z)=1+\gamma\arctan z,\qquad \gamma=1/10,
 \quad m=5/6,\quad a=7/6,\quad b=1/6.
\]

Thus m<phi<a, 0<phi'<=gamma, and any sample feature contrast has
absolute value less than b. Only opposite labels (+1,-1) are used in
the learned-shift calculation. Same-label assembly is outside scope.
All source derivatives keep deterministic coefficients and covariance
parameters fixed, including at singular covariances, as in the short
response note.

There are two different premises throughout:

1. The finite Gaussian scalar response law yields the first-chaos
   identities below, including for its internal two-query clips.
2. The bound on the contrast action is available on an existing uncut
   contrast-ascent trajectory with the stated symmetry and regularity.

Premise 2 is NOT established for the internally clipped law. Their
combination below is conditional on both premises holding for the same
objects. Neither a passage to a continuum response representation nor
an energy-preserving reference construction is supplied here.

## 1. The exact quadratic form retains all times and both samples

Fix a reverse layer ell in {2,3}, an output time t, and a finite list
of source slots i=(s,c), s<=t and c in {1,2}. Write

\[
 h_i=H^{(\ell-1)}_{sc},\qquad
 K_{ij}=\mathbb E[h_i h_j],\qquad \xi\sim N(0,K).
\]

These are uncentered feature second moments, as required by the scalar
law. Let delta_c=delta^(ell)_{tc}, delta_+/-=(delta_1+/-delta_2)/2,
and define the deterministic rows and their actual response evaluations

\[
 d_{\pm,i}=\mathbb E[\partial_{\xi_i}\delta_\pm],
 \qquad R^0_\pm=\sum_i d_{\pm,i}h_i.                 \tag{1}
\]

For ell=2 these are exactly the middle expected-derivative contribution
to B^(2), evaluated on the actual first-layer features in q^(1).
For ell=3 the same statement concerns B^(3) and q^(2). The other source
groups are independent of xi; the features h_i in (1) can depend on
their own reverse sources. No independence of R^0 and its eventual
query's Gaussian source is asserted or used.

The precise first-chaos bound is the matrix inequality

\[
 \big(\mathbb E[R^0_\mu R^0_\nu]\big)_{\mu,\nu\in\{-,+\}}
   =\big(d_\mu Kd_\nu^T\big)_{\mu,\nu\in\{-,+\}}
   \preceq \operatorname{Cov}(\delta_-,\delta_+).       \tag{2}
\]

Here is a proof that also covers singular K. Factor K=LL^T with L of
full column rank and write xi=LZ, where Z has independent standard
normal coordinates. If F is any linear combination of delta_- and
delta_+, and eta denotes the remaining independent source groups,
one-dimensional integration by parts gives

\[
 \mathbb E[Z_jF(LZ,\eta)]
   =\mathbb E[\partial_{Z_j}F(LZ,\eta)]
   =(L^T\mathbb E\nabla_\xi F)_j.
\]

For the finite smooth capped programs, the required integrability
follows from the finite derivative bounds and Gaussian moments; the
boundary term is zero because the Gaussian density decays. More
generally the identity requires exactly these integrability and
boundary conditions. The Z_j are orthonormal in L2 and orthogonal to
constants. Expanding the nonnegative square after subtracting
sum_j E[Z_j F]Z_j from F-EF proves

\[
 (\mathbb E\nabla F)^T K(\mathbb E\nabla F)
       \le\operatorname{Var}(F).
\]

Applying this to every linear combination proves (2). In particular,
large formal derivatives in a null direction of K do not matter:
the same linear combination of h_i is zero in L2.

Put U(s)=(H^(ell-1)_{s1}+H^(ell-1)_{s2})/2,
V(s)=(H^(ell-1)_{s1}-H^(ell-1)_{s2})/2,
u(s)^2=E U(s)^2, and kappa(s)=E V(s)^2. Under equal sample second
moments, E[U(s)V(s)]=0. Consequently (2) yields the new weighted
actual-response estimate

\[
 u(t)^2\|R^0_-(t)\|_2^2+\kappa(t)\|R^0_+(t)\|_2^2
 \le u(t)^2\|\delta_-(t)\|_2^2
                  +\kappa(t)\|\delta_+(t)\|_2^2.       \tag{3}
\]

This is a bound on evaluated responses, not a bound on an absolute
coefficient row. It can be summed with arbitrary nonnegative time
weights. If a continuous response representation and the uncut action
budget hold on the same trajectory, integration gives

\[
 \int_0^T\sum_{\ell=2}^3
 \left[u_{\ell-1}^2\|R^{0,(\ell)}_-\|_2^2
       +\kappa_{\ell-1}\|R^{0,(\ell)}_+\|_2^2\right]ds
 \le \int_0^T\sum_{\ell=2}^3
       \|(W^{(\ell)})'(s)\|_{\rm HS}^2ds\le1.         \tag{4}
\]

The last inequality is conditional on the existing pre-fit uncut
ascent. For the internally clipped finite law, (2)--(3) still hold,
but replacing the corresponding sum of backward energies by 1 is
unjustified.

## 2. A bounded envelope for the actual learned shift

The opposite-label learned part of the reverse response, with the
normalization in the short note, is exactly

\[
 R^L_\mu(t,\omega)=\int_0^t
 \left[\langle\delta_\mu(t),\delta_-(s)\rangle U(s,\omega)
       +\langle\delta_\mu(t),\delta_+(s)\rangle V(s,\omega)
 \right]ds,\qquad\mu\in\{-,+\}.                       \tag{5}
\]

The factor 1/2 in the two sample sum has already been used in (5):
(delta_1 tensor H_1-delta_2 tensor H_2)/2
=delta_- tensor U+delta_+ tensor V. The discrete statement replaces
the integral by Delta times the strictly past sum.

Define, for this layer,

\[
 A_t=\int_0^t[u(s)^2\|\delta_-(s)\|_2^2
                        +\kappa(s)\|\delta_+(s)\|_2^2]ds,
 \qquad D_\mu(t)=\|\delta_\mu(t)\|_2.
\]

Cauchy--Schwarz first on the output neuron space, then on the two
sample modes and time, gives the pointwise inequality

\[
 |R^L_\mu(t,\omega)|
 \le D_\mu(t)\sqrt{A_t}
 \left(\int_0^t
    \left[\frac{U(s,\omega)^2}{u(s)^2}
              +\frac{V(s,\omega)^2}{\kappa(s)}\right]ds
 \right)^{1/2}.                                      \tag{6}
\]

Indeed the integrand after the first inequality is at most D_mu times
the inner product of the two vectors
(u||delta_-||_2, sqrt(kappa)||delta_+||_2) and
(|U|/u, |V|/sqrt(kappa)). This proves (6) without splitting delta_-
into its possibly cancelling gate terms.

If kappa(s)>0, put

\[
 L_s=\frac{a^2}{m^2}+\frac{b^2}{\kappa(s)}.
\]

Then the actual learned shift satisfies

\[
 \|R^L_\mu(t)\|_\infty
       \le D_\mu(t)\sqrt{A_t\int_0^t L_s\,ds}.        \tag{7}
\]

Thus a bounded action and a contrast floor do produce an L-infinity
envelope for this part of the actual shift, on any such feature
interval. In a pre-fit uncut trajectory A_t<=1; the floors (13) of
the contrast note make the right side finite on every already existing
finite interval, with rho-dependent constants. This statement neither
constructs that trajectory nor imports its budget into internal clips.

## 3. Current sample coercivity leaves an exact temporal remainder

For the expected-derivative part R^0_mu in (1), project onto the
two-dimensional current-feature span. Set

\[
 c_U=\mathbb E[\delta_\mu\xi_U],\quad
 c_V=\mathbb E[\delta_\mu\xi_V],\quad
 \xi_U=(\xi_{t1}+\xi_{t2})/2,\quad
 \xi_V=(\xi_{t1}-\xi_{t2})/2.
\]

Integration by parts and the matching source covariance give
E[R^0_mu U(t)]=c_U and E[R^0_mu V(t)]=c_V. Therefore

\[
 R^0_\mu=\frac{c_U}{u(t)^2}U(t)
                +\frac{c_V}{\kappa(t)}V(t)+I_\mu,
 \quad I_\mu\perp\operatorname{span}\{U(t),V(t)\}.     \tag{8}
\]

Writing e_mu=c_U^2/u(t)^2+c_V^2/kappa(t), (2) implies

\[
 e_\mu\le\operatorname{Var}(\delta_\mu),\qquad
 \|I_\mu\|_2^2\le\operatorname{Var}(\delta_\mu)-e_\mu,
\]
\[
 \left|\frac{c_U}{u(t)^2}U(t,\omega)
                  +\frac{c_V}{\kappa(t)}V(t,\omega)\right|
                    \le D_\mu(t)\sqrt{L_t}.           \tag{9}
\]

This identifies the covariance missed by an instantaneous Gram floor.
Let J=E[h(U(t),V(t))], a matrix with two columns. The exact temporal
innovation Gram and its response quadratic form are

\[
 K_I=K-J\operatorname{diag}(u(t)^{-2},\kappa(t)^{-1})J^T,
 \qquad \|I_\mu\|_2^2=d_\mu K_I d_\mu^T.             \tag{10}
\]

K_I is positive semidefinite: it is the Gram matrix of each historical
feature after subtracting its projection onto the current features.
An instantaneous contrast floor controls the two denominators in
(8)--(10); it supplies no lower bound on this remaining Gram.

Combining (7)--(9) gives the following inequality for the full actual
response shift R_mu=R^0_mu+R^L_mu:

\[
 |R_\mu(t,\omega)-I_\mu(t,\omega)|
 \le D_\mu(t)\left[\sqrt{L_t}
                  +\sqrt{A_t\int_0^tL_sds}\right].    \tag{11}
\]

It is useful to make the tail consequence precise. Denote the bracket
by B_t. In the scalar law q_mu=zeta_mu+R_mu and zeta_mu is a centered
Gaussian of variance D_mu^2. For D_mu>0, (11) and the Gaussian integral
give, without any independence between zeta_mu and the shift,

\[
 \mathbb E\exp\!\left(
   \frac{(q_\mu-I_\mu)^2}{8D_\mu^2(1+B_t^2)}\right)
       \le\sqrt2 e^{1/4}<2.                           \tag{12}
\]

To check this, use (z+r)^2<=2z^2+2r^2, |r|<=D_mu B_t, and
E exp(zeta_mu^2/(4D_mu^2))=sqrt(2). If D_mu=0, all the evaluated
responses and the Gaussian source vanish in L2. Formula (12) controls
the actual query after subtracting exactly I_mu. It is not a tail
claim for q_mu itself. The next calculation tests whether the proposed
first-chaos/action mechanism can also bound I_mu.

## 4. Explicit obstruction within the proposed covariance/gate controls

This section constructs an auxiliary finite Gaussian response map,
not a solution of the coupled training equations. Its purpose is to
test the putative implication from: the first-chaos quadratic form,
instantaneous common/contrast Gram coercivity, bounded contrast-weighted
backward action, bounded smooth arctan feature paths, and the relative
gate estimate. All these controls will hold uniformly. The evaluated
expected-derivative response will nevertheless have unbounded higher
moments. The coefficients are calculated as Gaussian expectations;
no arbitrary L2 operator is substituted for a response row.

### 4.1 A single smooth two-sample history with a contrast floor

Let G_1,G_2,X_1,X_2 be independent standard Gaussians and, for 0<=s<=1,
set

\[
 Z_a(s)=G_a+s\phi'(G_a)X_a,\qquad H_a(s)=\phi(Z_a(s)),
 \quad U(s)=(H_1(s)+H_2(s))/2,\quad
 V(s)=(H_1(s)-H_2(s))/2.                              \tag{13}
\]

The initial pair is exactly the admissible rho=0 first-layer Gaussian
pair. The samples have identical independent laws. Simultaneously
reversing G_a,X_a negates Z_a, so E H_a(s)=1. Hence

\[
 \mathbb E[U(s)V(s)]=0,\quad u(s)^2\ge1,\quad
 \kappa(s)=\tfrac12\operatorname{Var}(H_a(s)).
\]

On the event 1<=G_a<=2 and |X_a|<=1, Z_a(s)>=9/10 for all s<=1.
It follows that the fixed positive number

\[
 \kappa_*=
 \frac{\gamma^2}{2}\mathbb P(1\le G\le2,\ |X|\le1)
                         (\arctan(9/10))^2            \tag{14}
\]

is a lower bound for every kappa(s). The preactivation kinetic action
and feature velocities also have uniform bounds:

\[
 \int_0^1\sum_a\mathbb E|Z_a'(s)|^2ds\le2\gamma^2,
 \qquad |H_a'(s)|\le\gamma^2|X_a|.                    \tag{15}
\]

The relative gate estimate holds exactly on this history:
|[phi'(Z_1)-phi'(Z_2)]/2|<=|V|. No claim is made that (13) solves the
full gradient flow. In particular, (15) is a kinetic bound for these
paths, not an application of the contrast-ascent energy identity to
an auxiliary dynamics.

### 4.2 Temporal differences evade every fixed stronger moment bound

For an odd integer r>=3 and 0<h<=1/r, define the bounded feature
combination

\[
 f_{r,h}=\sum_{j=0}^r(-1)^{r-j}{r\choose j}V(jh),
 \qquad v_{r,h}=\mathbb E f_{r,h}^2.
\]

Repeated use of the fundamental theorem of calculus gives

\[
 h^{-r}f_{r,h}\longrightarrow
 Y_r=\tfrac12\big[A_r(G_1)X_1^r-A_r(G_2)X_2^r\big],
 \qquad A_r(g)=\phi^{(r)}(g)\phi'(g)^r.                \tag{16}
\]

The convergence is almost sure and in every finite Lp. Indeed the
divided difference is the average of V^(r) over an r-dimensional
cube of side h, and its absolute value is at most a fixed C_r times
|X_1|^r+|X_2|^r. The derivatives phi^(r) are bounded for each fixed r.
This supplies an integrable domination for each p. A_r is not
identically zero, so ||Y_r||_2>0 and v_{r,h}>0 for sufficiently small h.

Because r is odd, each summand in Y_r has mean zero. Independence and
conditional Jensen, for p>2, give

\[
 \frac{\|Y_r\|_p}{\|Y_r\|_2}
 \ge\frac1{\sqrt2}\,
       \frac{\|A_r(G)\|_p}{\|A_r(G)\|_2}
       \frac{\|X^r\|_p}{\|X^r\|_2}
 \ge\frac1{\sqrt2}\frac{\|X^r\|_p}{\|X^r\|_2}.      \tag{17}
\]

For example, without any asymptotic estimate,

\[
 \left(\frac{\|X^r\|_4}{\|X^r\|_2}\right)^4
   =\frac{(4r-1)!!}{((2r-1)!!)^2}
   =\prod_{j=1}^r\frac{2r+2j-1}{2j-1}\ge2^r.         \tag{18}
\]

For every fixed p>2 the same ratio diverges: the Gaussian integral
E|X|^q=2^(q/2)Gamma((q+1)/2)/sqrt(pi), together with the elementary
Stirling asymptotic Gamma(x+1/2)~sqrt(2 pi)x^x exp(-x) as x tends
to positive infinity, applied at x=rp/2 and x=r, gives

\[
 \frac{\|X^r\|_p}{\|X^r\|_2}
 \sim 2^{1/(2p)-1/4}(p/2)^{r/2}.                     \tag{19}
\]

Thus the L2-normalized combinations f_{r,h}/sqrt(v_{r,h}) have no
uniform Lp bound, for any p>2, although the underlying history (13),
its kinetic bound, and every two-sample Gram floor stay fixed.

Even r=3 rules out mesh-uniform exponential-absolute tails. There
is an event of positive probability on which |A_3(G_1)|>=c>0 and the
second summand in Y_3 is bounded by a constant. On this event, for
large |X_1|, |Y_3|>=c'|X_1|^3. Independence and the one-dimensional
Gaussian density then imply, for every lambda>0,

\[
 \mathbb E e^{\lambda |Y_3|}=\infty,
 \qquad \mathbb E e^{\lambda Y_3^2}=\infty.            \tag{20}
\]

For precision, restrict G_1 to a set where |A_3|>=c and restrict
|X_2| to a bounded interval; A_3(G_2) is globally bounded. The integral
over X_1 contains exp(c''|X_1|^3-X_1^2/2), which is divergent.
Fatou's lemma applied to (16), including convergence of the L2
normalizer, shows that each of the corresponding exponential moments
of f_{3,h}/sqrt(v_{3,h}) tends to infinity as h decreases to zero.

### 4.3 An arctan-gated Gaussian derivative produces that actual shift

Index the history by (j,a), 0<=j<=r, and let
K=E[(H_a(jh))_(j,a)(H_a(jh))_(j,a)^T]. Choose the deterministic row c
with

\[
 c_{j1}=\tfrac12(-1)^{r-j}{r\choose j},\qquad
 c_{j2}=-c_{j1}.
\]

Take the output time to be 1. If rh<1, append its two current source
slots with zero coefficients. One may restrict to h=1/N and append
all other mesh slots with zero coefficients as well. This retains a
fixed unit horizon and the full source Gram, without changing any
calculation below.

Then f_{r,h}=c h_history and cKc^T=v_{r,h}. Take a Gaussian source
xi with precisely this covariance and put

\[
 X_* =\frac{c\xi}{\sqrt{v_{r,h}}}\sim N(0,1),\qquad
 \widetilde Z_1=1+X_*,\quad \widetilde Z_2=1-X_*.
\]

Use the common backward query q_1=q_2=1 and the raw middle gates

\[
 \delta_1=\phi'(1+X_*),\qquad
 \delta_2=\phi'(1-X_*),\qquad
 d(x)=\tfrac12[\phi'(1+x)-\phi'(1-x)].                \tag{21}
\]

The common/contrast gate identity is retained literally:
q_+=1, q_-=0, delta_-=p_-q_+=d(X_*). Moreover

\[
 |\delta_-|\le|\widetilde V|,
 \quad \widetilde V=
       \tfrac12[\phi(1+X_*)-\phi(1-X_*)],
 \quad |\delta_-|\le\gamma/2,\quad |\delta_+|\le\gamma.
\]

The tilde sample pair has equal second moments by X_* -> -X_*, and
E tilde-V^2>0 independently of r,h. At every input-history time its
contrast-weighted backward energy integrand satisfies

\[
 u(s)^2\mathbb E\delta_-^2+\kappa(s)\mathbb E\delta_+^2
       \le\gamma^2(a^2/4+b^2)<1.                     \tag{22}
\]

Thus the numerical action control over a unit interval is uniform,
even pointwise in time. This verifies an energy-bound premise; it
does not assert the gradient identity producing that bound in R2.

For x>0, (1+x)^2>(1-x)^2, so d(x)<0; also d is odd. Consequently

\[
 c_0=\mathbb E[X_*d(X_*)]<0.
\]

This is a fixed nonzero constant. Differentiation with c and v fixed,
then one-dimensional Gaussian integration by parts, gives the exact
expected-source-derivative rows

\[
 \mathbb E\nabla_\xi\delta_-
       =\frac{c_0c}{\sqrt{v_{r,h}}},\qquad
 \mathbb E\nabla_\xi\delta_+=0.                       \tag{23}
\]

The second equality uses that delta_+ is an even function of X_*.
In particular the first-chaos quadratic form is uniformly bounded,

\[
 (\mathbb E\nabla\delta_-)K
                   (\mathbb E\nabla\delta_-)^T
       =c_0^2\le\mathbb E\delta_-^2.                  \tag{24}
\]

But its actual response evaluation on the bounded feature histories is

\[
 R^0_-=c_0\frac{f_{r,h}}{\sqrt{v_{r,h}}},\qquad R^0_+=0.\tag{25}
\]

Equations (16)--(20) now give unbounded Lp norms for every p>2 and
unbounded exponential-absolute and exponential-square moments in
this family of evaluated expected responses. Every single finite
combination is bounded; it is uniformity in the number/spacing of
historical queries that fails. Subtracting the current-feature
projection cannot repair this: (9), (14), and the fixed law of delta
bound that projection uniformly in L-infinity. Hence the same failure
is present in I_-. Adding a learned shift bounded as in (7) also cannot
remove it; (14) and (22) make that bound uniform in this example.

This construction is more specific than an arbitrary L2-to-Lp operator
counterexample. The first-chaos row is obtained from a bounded arctan
gate, the forcing term is exactly p_-q_+, the common and contrast
sample modes are preserved, the Gaussian source covariance is the
feature-history Gram, and the historical features follow one fixed smooth
arctan path with Gaussian initialization and bounded kinetic action.
What it does NOT preserve is the full causal recursion forcing these
particular preactivations and response rows to arise during training.
An argument exploiting that additional recursion is therefore still
possible; an argument using only (2), the scalar action budget, the
instantaneous Gram floor, and the relative gate estimate is not.

In particular this family is not a counterexample to the established
short-interval estimate: that estimate controls the rows selected by
its causal recursion and excludes (23) at a unit horizon. The present
test shows why retaining only its first-chaos quadratic inequality,
even supplemented by the contrast energy and gate estimates, loses
information needed to extend that control.

## 5. Research disposition

| Claim | Status and exact scope |
|---|---|
| First-chaos matrix inequality (2) and weighted actual-response inequality (3) | Proved for the finite scalar source law under its stated derivative convention; both sample modes and all temporal covariances retained |
| Learned-shift envelope (6)--(7) | Proved from the actual learned covariance formula; a uniform bound requires an action bound for those same fields |
| Current-feature/temporal-innovation split (8)--(11) | Exact; isolates the Schur-complement covariance that the instantaneous contrast floor does not control |
| Gaussian tail bound (12) | Proved for the actual query with precisely the temporal expected-response remainder removed; not a tail bound for the whole query |
| Uniform stronger-than-L2 response tails from the proposed covariance/action/gate premises alone | Falsified by the explicit expected-derivative construction (13)--(25) |
| Those adverse rows are attained by the two-query Euler law | Not claimed; no such identification is proved |
| Long-interval tails for the actual internally clipped or uncut trajectory | Open |
| Full-gradient positive-contraction energy condition for internal two-query clipping | Open and unused |

No existing result is superseded. This test narrows the missing bridge:
the action controls the learned shift and the first-chaos L2 norm, and
the contrast floor controls the current two-feature projection. A
long-interval proof must additionally restrict the temporal-innovation
response rows using the actual causal dynamics. Merely reweighting the
first-chaos form by the instantaneous contrast cannot supply that
restriction, even with the exact relative-gate estimate.
