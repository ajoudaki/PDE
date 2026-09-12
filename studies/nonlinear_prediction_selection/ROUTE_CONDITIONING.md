# Conditioning route: protected saturated rows and endpoint geometry

Status: independent candidate derivations, frozen for comparison; not a proof of
milestone A and not a promotion candidate. No experiments were run. The route
establishes strict endpoint conditioning, a robust family with nonzero projected
learning and hidden activation change, and the long-time slope of the established
infinitesimal response. Actual nonlinear changed-law capture on physical times of
order `1/epsilon` remains open.

## 1. Scope, model and source boundary

The model is bias-free, with two tanh hidden layers and normalized input `u in S1`:

\[
 h^1_n(u)=\tanh(W^1_nu),\qquad
 h^2_n(u)=\tanh(W^2_nh^1_n(u)),\qquad
 f_n(u)=(W^3_n)^Th^2_n(u)/n.
\]

Stored Gaussian variances are `(1,1/n,1/n^2)`, mobilities are `(n,1,n)`,
the loss is unhalved mean square, and every finite flow retains the actual initial
readout. The reference law is
`nu_*=(delta_(e1,1)+delta_(e2,-1))/2`; changed laws are
`mu_epsilon=(1-epsilon)nu_*+epsilon nu`, always from that same original
initialization. The requested nonlinear conclusion concerns a nonvanishing
change of added-law risk and a paired hidden representation observable as
`epsilon -> 0`, with whole-circle prediction and actual finite-GF capture.

Scientific input was restricted to the complete statements and proofs in
`docs/global_nonlinear.md`, C.4.5 and C.4.6 (lines 5269–8976), and the full
`docs/README.md` and `docs/NOTATION.md`. No other study, this study's README,
other route, task history, or external scientific source was read. No maintained
API was used or changed. The foundational A/B/III.F theorems cited by C.4.5–6
were not separately re-audited; the present deductions use the complete supplied
C.4.5–6 conclusions and their contained proofs, particularly the source-envelope
proof. C.4.7–8 are mentioned by the supplied guide but their scientific contents
were not read or used.

Required skills read: `solve-math-rigorously` and `investigate-conjectures`, with
the latter's research-contract, adversarial-audit and proof-search-orchestration
references. The shared AGENTS and complete workflow were read. The supervisor
confirmed the central pre-edit HEAD/index/status check; this worker made no Git
calls and owns only this report and its unused assigned scratch namespace.

Independence disclosure: before this file was frozen, the supervisor suggested
distinguishing parameter motion from a fixed-readout hidden-activation contrast,
then requested that suggestion be reserved for post-freeze work. The local
rank/hidden-gradient argument and its consequence for a paired squared upper
activation observable had already been derived before receipt of that suggestion.
This report retains that independently derived squared observable; it does not
add a separately named fixed-readout contrast on the basis of the suggestion.

## 2. Established inputs actually used

Write the population state as `theta=(w,A,c)`, with
`A=A0+K`, `K` Hilbert–Schmidt, and raw Hilbert increment space

\[
 \mathcal H=L^2(\Omega_1;\mathbb R^2)
       \oplus\mathcal S_2(H_1,H_2)\oplus L^2(\Omega_2).
\]

All norms below are these ordinary Hilbert norms. Both orientations of `A` are
the actual initialized action plus its trained increment and adjoint.

C.4.5.1 constructs the reference feature curve on `0<=s<=s_dagger<=10`,
with initial first row `g=(g1,g2)` consisting of independent standard normals.
Its endpoint `theta_infty` is the first state with reference prediction `(1,-1)`.
The exact scalar clock is

\[
 F(w_a(s))=F(g_a)+X_a(s),\qquad
 F(z)=z/2+\sinh(2z)/4,\qquad F'(z)=\cosh^2z.
 \tag{2.1}
\]

C.4.6.S40–S44, including their actual finite cavity proof and passage to the
canonical population, give one nonnegative random envelope `N` such that

\[
 \|N\|_p\le C_*\sqrt p\quad(p\ge2),\qquad
 \sup_{s\le s_\dagger}|X_a(s)|\le5N\quad(a=1,2).
 \tag{2.2}
\]

The envelope may depend on the Gaussian first row. No independence of `N` and
`g` is assumed or needed below. The countable-source representative construction
in S43 supplies the active clocks simultaneously through Fubini and their
absolutely continuous representatives; only these active clocks enter (2.2).

The endpoint has `||c_infty||_2<=sqrt(10)`, `||A_infty||<=2+sqrt(10)`,
`||w_infty||_2<=sqrt(2)+sqrt(10)`, and `||c_infty||_infty<=10`.
Its predictor is odd, is antisymmetric under coordinate swap, and is
76-Lipschitz in `u`. Its readout is nonzero because `f_infty(e1)=1`.
Reference physical time tends to this same endpoint, exponentially in raw norm.

For the established tangent response, C.4.6 gives

\[
 v_\sigma'=\mathcal L(t)v_\sigma+b_\sigma(t),\qquad v_\sigma(0)=0,
 \quad \mathcal L_\infty=-2S_\infty E_\infty,
 \tag{2.3}
\]

on its stronger clock/HS/readout space `V`. Its homogeneous propagator is
uniformly bounded. The perturbation
`mathcal B(t)=mathcal L(t)-mathcal L_infty` has the exponential bound in
C.4.6.P21, so both `integral ||mathcal B||` and
`integral t||mathcal B||` are finite. The forcing is continuous through the
feature endpoint by C.4.6.3 §7, hence `b_sigma(t)->b_sigma,infty` in `V`.
These statements concern the established linear response, not a nonlinear
changed-law population flow.

## 3. Saturated rows retain sign-separating input features

**Lemma 3.1 (surviving large Gaussian rows).** Fix `v in R2` with both
coordinates nonzero. For every sufficiently large real `r`, there is an event
of positive probability on which

\[
 |g-rv|_\infty\le1,\qquad N\le r^2,\qquad
 \sup_{s\le s_\dagger}|w(s)-g|_\infty\longrightarrow0
 \quad(r\longrightarrow\infty),
 \tag{3.1}
\]

where the last bound is deterministic and uniform over the event.

Proof. From (2.2), for `R>=e C_* sqrt(2)`, choose the real exponent
`p=(R/(e C_*))^2>=2` in Markov's inequality. It gives

\[
 \Pr(N>R)\le(C_*\sqrt p/R)^p
           =\exp[-R^2/(e^2C_*^2)].
 \tag{3.2}
\]

The independent two-dimensional Gaussian density gives

\[
 \Pr\{|g-rv|_\infty\le1\}
 \ge{2\over\pi}\exp[-(r|v|+\sqrt2)^2/2].
 \tag{3.3}
\]

Indeed the box has area four and every point in it has Euclidean norm at
most `r|v|+sqrt(2)`. Equations (3.2) with `R=r^2` and (3.3) show that
the box probability exceeds `Pr(N>r^2)` for every sufficiently large `r`.
Their intersection with `{N<=r^2}` therefore has positive probability,
without any conditional-independence assertion.

Put `rho=min(|v1|,|v2|)/2>0`. On that event and for large `r`,
`|g_a|>=rho r`. The minimum of `F'` between `g_a-1` and `g_a+1` is
at least `exp(2(|g_a|-1))/4`. This exceeds `5r^2`. Since `F` is strictly
increasing and `|X_a(s)|<=5r^2`, (2.1) puts `w_a(s)` between these two
endpoints. The mean value theorem then yields

\[
 |w_a(s)-g_a|\le20r^2e^{-2(|g_a|-1)}
             \le20e^2r^2e^{-2\rho r}.
 \tag{3.4}
\]

The right side tends to zero and is uniform in feature time. This proves
the lemma. The argument uses saturation to protect rows; an L2 state bound
alone would not give (3.4).

**Lemma 3.2 (first-feature independence).** Let `u1,...,um in S1` be
pairwise distinct modulo antipodes: `u_j != u_k` and `u_j != -u_k`
for `j!=k`. At every separately fixed reference feature time, including the
fitted endpoint, the functions

\[
 H_j^1=\tanh(w\cdot u_j)\in L^2(\Omega_1)
 \tag{3.5}
\]

are linearly independent. Thus their finite Gram matrix is strictly positive
definite. The assertion concerns every finite list; it is not a positive lower
bound for one infinite-dimensional integral operator.

Proof. Suppose `sum_j alpha_j H_j^1=0` almost surely. Choose `v` with
nonzero coordinates and with `v.u_j !=0` for every `j`. On the positive
probability event of Lemma 3.1,
`w.u_j=r v.u_j+O(1)+o(1)`, uniformly over the event. Therefore
`H_j^1->sign(v.u_j)` uniformly there. The assumed relation forces

\[
                 \sum_j\alpha_j\operatorname{sign}(v\cdot u_j)=0
 \tag{3.6}
\]

for every such `v`: otherwise its constant nonzero limit would contradict
the relation on these positive-probability events for large `r`.

Fix `k`. On the unit circle of possible `v`, cross the line `v.u_k=0`
at one of its intersection points. No other `v.u_j` vanishes there because
the inputs are distinct modulo antipodes. Choose points on its two nearby
sides with both coordinates nonzero; this is possible even when the crossing
lies on a coordinate axis. The signs for `j!=k` agree and the sign for `k`
changes. Subtracting their two identities (3.6) gives `2 alpha_k=0` up to
the irrelevant orientation sign. This holds for every `k`.

For fixed `m`, the Gram depends continuously on feature time and on its
input tuple, because `tanh` is one-Lipschitz and `w` is L2-continuous.
Consequently its smallest eigenvalue has a positive minimum on any compact
parameter set of pairwise nonantipodal tuples and feature times in
`[0,s_dagger]`. This minimum can be extremely small; no useful numerical
conditioning estimate is asserted.

## 4. Strict trained gradient conditioning from the middle block

At a state on the reference define, for an arbitrary input `u`,

\[
 H^1(u)=\tanh(w\cdot u),\quad Z^2(u)=AH^1(u),\quad
 H^2(u)=\tanh Z^2(u),\quad
 \delta(u)=c\operatorname{sech}^2 Z^2(u),\quad Q(u)=A^*\delta(u).
\]

The raw scalar prediction gradient is

\[
 g(u)=\big(u\operatorname{sech}^2(w\cdot u)Q(u),
                 \delta(u)\otimes H^1(u),\ H^2(u)\big)\in\mathcal H.
 \tag{4.1}
\]

Here `(a tensor b)z=a E[bz]`. At finite width its middle block is
`delta_n(u) h1_n(u)^T/n`, with its ordinary Frobenius norm.

**Lemma 4.1 (strict full and hidden Gram).** At any positive feature time
up to and including the endpoint, every finite list of `g(u_j)` at inputs
distinct modulo antipodes is linearly independent. Its middle gradient blocks
are already linearly independent. In particular the same is true of the
combined first-row/middle hidden-gradient blocks.

Proof. The reference calculation C.4.5.R12 gives
`||c(s)||_2>=s sqrt(m)>0` at every positive `s`. A tanh gate is strictly
positive at every finite argument. The field `Z^2(u_j)` is finite almost
surely because it belongs to L2. Hence
`delta_j=c sech^2 Z^2(u_j)` is nonzero in L2.

Lemma 3.2 supplies linearly independent `H_j^1`. For each `j`, invert their
finite Gram matrix to obtain `z_j` in their span with
`<H_k^1,z_j>=1_(k=j)`. If
`sum_k alpha_k delta_k tensor H_k^1=0`, apply this operator to `z_j`:
it gives `alpha_j delta_j=0`, hence `alpha_j=0`.

There is also an explicit positive reference-dependent bound. If `lambda_H`
is the smallest eigenvalue of the first-feature Gram, then

\[
 \left\|\sum_j\alpha_j\delta_j\otimes H_j^1\right\|_{HS}^2
 \ge\lambda_H\sum_j\alpha_j^2\|\delta_j\|_2^2
 \ge\lambda_H\min_j\|\delta_j\|_2^2\,|\alpha|^2.
 \tag{4.2}
\]

To verify the first inequality, at each second-layer coordinate apply the
Gram lower bound to the first-layer function
`sum_j alpha_j delta_j(omega2) H_j^1`, then integrate over that coordinate.
Its integrated squared norm is exactly the Hilbert–Schmidt norm on the left.

All these finite Grams are continuous. On any compact set of pairwise
nonantipodal input tuples and feature times bounded away from zero, (4.2)
has a uniform strictly positive right-hand coefficient. In particular the
two-by-two trained reference Gram in C.4.6 is nonsingular at the endpoint.
The weights `p1=p2=1/2` simply multiply its unweighted Gram by `1/2`.
This strengthens conditioning for this specific reference; it does not assert
nonsingularity for coincident or antipodal lists, or at zero limiting readout.

**Finite reference transfer.** Fix a finite input list as above. The actual
finite reference GF gradients at every fixed positive physical time have Gram
entries converging in probability to the population entries. C.4.6.3 §8
identifies the same-layer tuples of passive queries and forward fields with
second moments; bounded gates pass the first block, and middle pairings factor
as `(<delta_j,delta_k>/n)(<h1_j,h1_k>/n)`. Thus each finite Gram entry has
the asserted limit. Its smallest eigenvalue converges because
`|lambda_min(K)-lambda_min(K')|<=||K-K'||`, by the unit-vector Rayleigh
formula. Choosing physical time large enough to approach the strictly positive
endpoint Gram gives positive finite reference conditioning with probability
tending to one. The order is a fixed physical time followed by width; this
does not identify a finite-width parameter endpoint.

## 5. An explicit robust added-law family and a protected hidden direction

Let `u_+=(e1+e2)/sqrt(2)` and write `u(alpha)=(cos alpha,sin alpha)`.
The swap symmetry gives `f_infty(u_+)=0`. Set

\[
 a=1/1216,\qquad
 \left|\alpha_1-(\pi/4-a)\right|<a/4,\qquad
 \left|\alpha_2-(\pi/4+a)\right|<a/4,\qquad
 p\in(1/3,2/3),
 \tag{5.1}
\]

and use

\[
 \nu=p\delta_{(u(\alpha_1),1)}+(1-p)\delta_{(u(\alpha_2),1)}.
 \tag{5.2}
\]

This is open in its two positions and one weight; labels remain binary and
fixed. The two added inputs are distinct, nonorthogonal to each other and
to both original inputs, and all four inputs are distinct modulo antipodes.
The closed parameter box with weak inequalities has the same properties.
The 76-Lipschitz estimate gives, for either added input,

\[
 |f_\infty(u_j)|\le 76(5a/4)=5/64<1/8,
 \qquad |f_\infty(u_j)-1|>7/8.
 \tag{5.3}
\]

Consequently the added-law risk exceeds `49/64`. This risk is normalized by
the added law itself; using only the mixture risk would hide a mass-`epsilon`
unlearned task.

In this section all gradients are at `theta_infty`. Let `G:R2->H` have
columns `g(e1),g(e2)`, set `K_*=G^*G`, and define the raw orthogonal projector

\[
 P=I-GK_*^{-1}G^*.
 \tag{5.4}
\]

Lemma 4.1 makes the inverse legitimate. This `P` is the raw projector in
C.4.6.P31; including the reference weights in `G` gives the same projector.
Put `r_j=f_infty(u_j)-1`, `p_1=p`, `p_2=1-p`, and

\[
 q=-P\nabla R_\nu(\theta_\infty)
       =-2\sum_{j=1}^2p_jr_jP g(u_j).
 \tag{5.5}
\]

Then `G^*q=0`, so both original predictions are preserved to first order.
Moreover `q!=0`, and its combined hidden block `q_h` is nonzero. To see this,
write `q=sum_(j=1)^4 a_j g(v_j)` using the original inputs and the two added
inputs. The added coefficients are exactly `-2p_jr_j`, hence nonzero.
If either `q=0` or its middle block vanished, Lemma 4.1 would force all four
coefficients to vanish, a contradiction.

This proof grants the readout its best possible compensating change: even the
full projected gradient cannot become a readout-only vector. It does not
merely exhibit a hand-picked hidden parameter direction.

Write `J_j q_h=D H^2(v_j)[q_h]`, the strong directional upper-activation
derivative, where row and middle blocks vary and the readout is held fixed.
If all four `J_j q_h` were zero, then, by (4.1),

\[
 0=\sum_{j=1}^4a_j\langle c_\infty,J_jq_h\rangle
   =\left\langle\sum_{j=1}^4a_j g_h(v_j),q_h\right\rangle
   =\|q_h\|^2>0,
 \tag{5.6}
\]

a contradiction. Thus the direction changes an actual upper hidden activation
at at least one of the four inputs. No claim that both hidden layers must
move follows from this argument.

Give the four inputs weights `omega_1=omega_2=1/4` and
`omega_3=p/2, omega_4=(1-p)/2`, and set

\[
 C_H(\nu)=\sum_{j=1}^4\omega_j\|J_j q_h\|_2^2>0.
 \tag{5.7}
\]

The quantities `||q||`, `||q_h||`, and `C_H(nu)` are continuous in the
closed parameter box of (5.1). Its compactness and the strict arguments above
give positive minima. These are reference-defined constants, not evaluated
numerical certificates.

## 6. Exact fitted-constraint curves with finite risk and representation change

This section establishes geometry, not a substitute optimizer.

First, the scalar map `theta -> f_theta(u)` is continuously Fréchet
differentiable on the raw affine Hilbert state space, with gradient (4.1).
This scalar assertion does not say that a tanh superposition map is Fréchet
differentiable from L2 to L2, or that the raw vector field is locally Lipschitz.

Here is a direct proof of the scalar assertion. Along every straight state
segment, the strong L2 curve chain rule for tanh and the bounded-operator
product rule give the scalar derivative (4.1). If states converge in raw
norm, their forward fields converge in L2. The elementary fixed-vector rule

\[
 b_k\to b\text{ in probability},\quad\sup_k\|b_k\|_\infty<\infty,
 \quad v\in L^2
 \quad\Longrightarrow\quad\|(b_k-b)v\|_2\to0
 \tag{6.1}
\]

follows by truncating `v`, applying bounded convergence on its bounded part,
and controlling its L2 tail. This successively proves L2 convergence of
`delta`, `Q` and the row gradient in (4.1), and HS convergence of the middle
rank. Thus the raw gradient is continuous, jointly in state and input.
Integrating it on a segment gives

\[
 f_{\theta+h}(u)-f_\theta(u)-\langle g_\theta(u),h\rangle
 =\int_0^1\langle g_{\theta+th}(u)-g_\theta(u),h\rangle\,dt
 =o(\|h\|).
 \tag{6.2}
\]

Continuity makes this uniform in `u` on the compact circle near a fixed state.

For each `nu` in (5.1) consider states

\[
 \theta_\nu(s)=\theta_\infty+s q(\nu)+G z_\nu(s).
 \tag{6.3}
\]

The equation requiring original predictions `(1,-1)` is a two-dimensional
C1 equation `Phi_nu(s,z)=0`. At `(0,0)` its derivative in `z` is `K_*`,
and its derivative in `s` is zero because `G^*q=0`. For completeness this
equation has a local unique C1 solution: on a sufficiently small ball the
map `z -> z-K_*^{-1}Phi_nu(s,z)` has derivative norm at most `1/2` by
continuity, and maps that ball to itself for small `s` because its value at
zero tends to zero. Iterating the map gives its unique fixed point by the
geometric error bound. Subtracting fixed-point equations proves continuity;
the integral mean value formula and invertibility of nearby `D_z Phi` give
its derivative. Thus `z_nu(0)=0` and `z_nu'(0)=0`.

All estimates are uniform over the compact closed family in (5.1): the
dependence of `q` on that family is continuous, `K_*` is fixed, and the
relevant derivatives are jointly continuous on finite-dimensional compact
neighborhoods. Hence one small positive `s_0`, independent of `nu` and of
`epsilon`, can be chosen for all the following conclusions.

The risk derivative at zero is

\[
 {d\over ds}R_\nu(f_{\theta_\nu(s)})\big|_{s=0}
 =\langle\nabla R_\nu,q\rangle=-\|q\|^2<0.
 \tag{6.4}
\]

Consequently, after decreasing `s_0` if necessary,

\[
 R_\nu(f_\infty)-R_\nu(f_{\theta_\nu(s_0)})
      \ge (s_0/2)\min_\nu\|q(\nu)\|^2>0.
 \tag{6.5}
\]

Define the paired upper hidden displacement from the fitted state by

\[
 J_{2,\nu}(s)=\sum_{j=1}^4\omega_j
       \|H^2_{\theta_\nu(s)}(v_j)-H^2_{\theta_\infty}(v_j)\|_2^2.
 \tag{6.6}
\]

The finite-dimensional C1 state curve has strong L2 hidden derivatives by
the same curve chain rule. Therefore
`J_(2,nu)(s)=s^2 C_H(nu)+o(s^2)`. The remainder is uniform over the compact
law family, by continuity of the finitely parameterized hidden derivative.
Decrease `s_0` again to obtain

\[
 J_{2,\nu}(s_0)\ge(s_0^2/2)\min_\nu C_H(\nu)>0.
 \tag{6.7}
\]

Both original predictions are fitted exactly along (6.3). The states define
continuous whole-circle predictions through the actual learned action, and
their deviation from `f_infty` tends uniformly to zero as `s_0->0` by the
forward Lipschitz estimate and the bounded state norms. Equations (6.5)–(6.7)
prove a robust local family of geometrically admissible endpoint changes,
with a nonvanishing added-risk margin and a named representation observable.
They do not claim that `theta_nu(s_0)` is selected by changed-law GF. The
curve is used only as a witness that strict conditioning has a nonlinear
observable consequence; using it as the requested trajectory would change
the optimizer and would be invalid.

## 7. The actual infinitesimal response has this nonzero long-time slope

There is a further consequence for the already established response, with its
derivative-before-width convention unchanged. Let
`sigma=nu-nu_*` and `z=P_infty b_sigma,infty` in the clock tangent space.
Then

\[
                       v_\sigma(t)/t\longrightarrow z
                       \quad\hbox{strongly in }\mathcal V.
 \tag{7.1}
\]

Proof. The established response bound gives `||v_sigma(t)||<=C t`.
The frozen semigroup `V_infty(t)=exp(t mathcal L_infty)` is uniformly
bounded and converges in operator norm to `P_infty`, by C.4.6.P16–P30
and its finite matrix exponential. Variation of constants gives

\[
 v(t)=\int_0^tV_\infty(t-s)b_\infty\,ds
 +\int_0^tV_\infty(t-s)[b(s)-b_\infty]\,ds
 +\int_0^tV_\infty(t-s)\mathcal B(s)v(s)\,ds.
 \tag{7.2}
\]

After division by `t`, the first integral tends to `P_infty b_infty` by
the elementary Cesaro property of a norm-convergent bounded function. The
second has norm bounded by
`B_infty t^-1 integral_0^t ||b(s)-b_infty|| ds`, which tends to zero
because `b(s)->b_infty`. The third is at most
`B_infty C t^-1 integral_0^infty s||mathcal B(s)|| ds`, which tends to
zero by the exponential bound already quoted. This proves (7.1).

The raw image of `z` is exactly the vector in (5.5):

\[
                        R_\infty z=q.
 \tag{7.3}
\]

Indeed the reference residual is zero at the endpoint, so the raw image of
`b_sigma,infty` is `-nabla R_nu(theta_infty)`. C.4.6.P31 converts its
clock projection to the raw orthogonal projection (5.4). All passive raw
gradient directions used here lie in the clock domain by the weighted source
bound C.4.6.S7; an unbounded inverse conversion is not applied to an arbitrary
raw direction.

The joint state/input gradient continuity in §6 and the continuous source
fields through the feature endpoint imply uniform convergence of the
prediction evaluation fields on the compact circle. Combining this with
(7.1) and the strong raw conversion gives

\[
 \sup_{u\in S^1}\left|
 {\mathscr D_\sigma f(t,u)\over t}
                 -\langle g_\infty(u),q\rangle\right|\to0.
 \tag{7.4}
\]

For the raw conversion, write
`R(t)v(t)/t-R_infty z=R(t)(v(t)/t-z)+(R(t)-R_infty)z`.
The first term tends to zero because `||R(t)||<=1`; the second follows
from (6.1) applied to the fixed row vector of `z`. Uniform input evaluation
then uses the compact circle and joint gradient continuity. At each of the
four fixed inputs, the same bounded-multiplier rule in the directional hidden
maps gives

\[
 {D_\sigma H^2(t,v_j)\over t}\longrightarrow J_jq_h
 \quad\hbox{in }L^2(\Omega_2).
 \tag{7.5}
\]

In particular the original prediction slopes in (7.4) are zero, the added
risk directional slope equals `-||q||^2`, and

\[
 \sum_j\omega_j\|D_\sigma H^2(t,v_j)\|_2^2/t^2
                   \longrightarrow C_H(\nu)>0.
 \tag{7.6}
\]

C.4.6.F22 and its named-field consequence capture these hidden derivatives
by actual finite-GF right derivatives at every fixed physical `T`, with their
joint second moments. Thus the iterated limit of the actual finite quantity

\[
 {1\over T^2}\sum_j\omega_j{1\over n}
 \left\|\left.\partial_{\epsilon^+}
 h^2_{n,\mu_\epsilon}(T,v_j)\right|_{\epsilon=0}\right\|_2^2
 \tag{7.7}
\]

is `C_H(nu)>0`, first `n->infty` in probability at each fixed `T`, then
`T->infty`. The corresponding finite prediction derivatives obey the
whole-circle version from C.4.6.T10 followed by (7.4). This is an actual-GF
infinitesimal statement and supplies no remainder uniform for
`epsilon T` of order one.

## 8. Claim ledger, hostile checks and exact remaining obligation

| Claim | Status and precise limitation |
|---|---|
| Saturated first-row tails survive reference training | Candidate proved from the supplied all-p source envelope and exact tanh clock; no independence assumption for that envelope |
| Every finite nonantipodal input list has independent endpoint first features | Candidate proved by sign jumps; no infinite-operator spectral gap |
| Endpoint full and hidden gradient Grams are strictly positive | Candidate proved through the middle rank block; constants may be extremely small |
| Open two-added-atom family has a residual and projected-learning margin | Candidate proved, with explicit positions and risk bound; law topology is its finite-atom parameter topology |
| The protected direction changes a named upper hidden representation | Candidate proved by (5.6)–(5.7); does not establish first-hidden movement |
| Exact fitted-constraint curve has finite added-risk and paired-hidden change | Candidate proved as geometry only; it is not a GF trajectory |
| Established response grows with nonzero projected slope and has actual finite-GF derivative capture | Candidate proved in the order derivative, fixed-time width, then large time |
| Nonlinear changed-law flows converge on a nonvanishing slow interval from original initialization | Open; no assertion supplied |
| Actual nonlinear finite GF captures a selected whole-circle prediction after order-one added learning as epsilon tends to zero | Open; milestone A remains unresolved |

The rare-root argument survives the main conditioning attack: clocks can depend
on the roots, but the union bound compares an `exp(-O(r^2))` root event with an
`exp(-Omega(r^4))` envelope tail. It would fail with only unquantified L2 control.
The actual source theorem supplies the stronger estimate used.

The tensor argument avoids assuming that `A0` is injective, that the learned
action is invertible, or that an initialized fresh Gaussian component survives
as an independent trained field. No such properties are needed: positivity of
the output gate and nonzero trained readout make each `delta_j` nonzero, while
independence is carried by the first-layer factors.

Coincident or antipodal inputs are excluded for an essential reason: oddness
makes their features identical or negatives. At initialization the hidden
gradient vanishes with `c=0`, so the trained Gram argument is explicitly
restricted to positive feature times. The robust family avoids both exceptions.

A hidden parameter norm is not the named representation observable: (5.6)
establishes nonzero upper activation derivative, and (6.6)–(6.7) give a paired
activation displacement on an exact finite curve. Even these statements do
not establish the same displacement along the requested changed-law GF.

The highest-leverage unresolved step is a reached-state nonlinear theorem on a
fixed slow interval `0<=tau<=tau0`, with physical time of order `tau/epsilon`,
starting from the original Gaussian initialization and connecting the initial
reference relaxation to a unique continuation constrained by the two fitted
predictions. It must retain the actual forward/adjoint action, control the
off-support inverse-gate/query products and nonlinear remainders on that
interval, and identify actual finite GF in a stated width/epsilon order.
Strict endpoint conditioning now has a proof mechanism; it does not supply
those nonlinear product estimates, trajectory selection, or finite-width
capture. A reference derivative bound cannot be inserted into a Taylor formula
at `T=tau/epsilon` without a new remainder theorem.

This route should be retained as a conditioning and nonvacuity contribution.
Its reopen condition is a concrete nonlinear continuation/capture estimate
that can use the positive finite endpoint Gram and the protected hidden
direction proved here. No impossibility of milestone A is asserted.

## 9. Source versions, actual checks and freeze record

Every scientific line of C.4.5 and C.4.6 was read through consecutive complete
chunks: 5269–5670, 5671–6090, 6091–6500, 6501–6902, 6903–7330,
7331–7750, 7751–8170, 8171–8570, and 8571–8976. The first combined guide
read was truncated; `docs/README.md` was reread in full. Truncated skill-reference
output was repaired by focused reads. No code or empirical producer was run.

SHA-256 hashes at drafting:

| Input | SHA-256 |
|---|---|
| `docs/global_nonlinear.md` (whole file metadata; only assigned sections read) | `bda93ec446425c05f8c06ac3a67fa1505906dff309b74e13bab4effc1527bf05` |
| C.4.5 slice, `sed -n '5269,6902p'` | `4e35f6b1dc336083aaefc4cc8ad15a40e42af1e6b93eadc37da0a32a32b00933` |
| C.4.6 slice, `sed -n '6903,8976p'` | `0bcc4bdf9ea8a02fa7337b42b09395924097f109a56191354e4129806ba071eb` |
| `docs/README.md` | `5210ccd284ea79215d81c18f2fba93762538cfb1bb5b6b295c6e33e558225e1f` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| `solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `investigate-conjectures/SKILL.md` | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `references/research-contract.md` | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| `references/adversarial-audit.md` | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
| `references/proof-search-orchestration.md` | `6f288341eb90f9618ab9fa6fc8c37225f41230de6a40285761c17cc257edecdd` |

Checks performed by the route author: direct reconstruction of the Gaussian
tail comparison, exact clock saturation bound, sign-jump independence,
Hilbert–Schmidt rank inequality, projector signs and unhalved-loss factor two,
representation derivative identity, local two-constraint construction, and
the three terms of (7.2). All are theoretical checks. The result is a candidate
awaiting supervisor reconstruction and independent checking; no independent
review, formal proof verification, numerical certificate for new constants,
or nonlinear trajectory computation is claimed.
