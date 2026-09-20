# Fresh iid minibatches in canonical p=1: exact noise geometry and its limits

This is an independent, frozen theory route. Scientific inputs were the complete
`docs/observable_p1.md` and `docs/NOTATION.md`, plus the supervisor's neutral
assignment. No other study, own-study history, other route, external source,
experiment, or maintained implementation was consulted. Required research and
mathematical skills, their research-contract/adversarial references, and the
shared workflow were read. The arguments below are new derivations from the
supplied equations. They are author-checked study results, not promoted material
or independent review results.

Source version: HEAD `019e3630237e33f58b9636c0aa67a039bebf0182`;
SHA-256 of `docs/observable_p1.md`:
`0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba`;
SHA-256 of `docs/NOTATION.md`:
`199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b`.
Only this assigned report is written by this route; no Git operation is made.

## Contract and conclusion

The object is actual simultaneous Euler SGD for the stated p=1 physical
gradient, with fresh iid indices within and across batches. It is not Heun,
finite-network raw SGD, an additive-noise algorithm, or a diffusion. The data
are finitely many unit vectors u_a=x_a/sqrt(d), with weights mu_a>0 summing to
one, and scalar labels y_a. Zero-weight observations can be deleted. The
canonical exact-population features, initialization (w,c,M)=(g,0,D), and
sign-paired invariant class are those in the source. Finite population tables
obey the same gradient/noise identities; where feature independence is used,
their weighted feature Grams must be positive definite. There is no width,
population-count, quadrature, or closure-order limit in this report.

The strongest established conclusion is conditional: for steps bounded below
by a positive number, actual iid minibatch SGD almost surely exits every
sufficiently small neighborhood of a state with a nonzero individual sample
gradient. Any finite state limit must therefore be stationary for every sample
separately. However, canonical p=1 has positive-loss states where all sample
gradients vanish and every batch is exactly motionless. This includes a cubic
saddle inside the sign-paired state class, on an explicitly realizable
three-point sphere dataset. These are ambient states, not demonstrated limits
or reachable states from the prescribed initialization. Thus stochasticity
alone does not prove fitting from that initialization. Batch size three has
exactly the same covariance range as batch size one, with one third the
covariance.

## 1. Physical sample gradients

Use the Hilbert state

    H = L2(Omega_1; R^d) x L2(Omega_2) x R^(K2 x K1),

with the ordinary population L2 metrics and Frobenius matrix metric. In a finite
rule these are sum_i pi1_i |w_i|^2 and sum_j pi2_j c_j^2. Positive population
weights are assumed when interpreting the finite metric; zero-weight rows can
be omitted. Write, for a fixed observation a,

\[
h_{1,a}=\tanh(w\cdot u_a),\qquad
a_a=E_1[b_1h_{1,a}],\qquad
z_{2,a}=b_2^TMa_a,\qquad h_{2,a}=\tanh z_{2,a},
\]
\[
f_a=E_2[ch_{2,a}],\quad r_a=f_a-y_a,\quad
\upsilon_a=E_2[b_2c(1-h_{2,a}^2)],\quad
q_a=b_1^TM^T\upsilon_a.
\]

Differentiating f_a in a state variation (delta w,delta c,delta M) gives

\[
df_a=E_1[(1-h_{1,a}^2)q_a u_a\cdot\delta w]
 +E_2[h_{2,a}\delta c]
 +\langle\upsilon_a a_a^T,\delta M\rangle_F.
\]

Thus its physical gradient and that of the unhalved sample loss are

\[
J_a=((1-h_{1,a}^2)q_a u_a,\ h_{2,a},\ \upsilon_a a_a^T),
\qquad g_a=\nabla_H(r_a^2)=2r_aJ_a.
\tag{1}
\]

No residual is included inside J_a or inside the backward coordinates. The
population probabilities do not reappear as extra row mobilities in (1).
For L=sum_a mu_a r_a^2, the mean gradient is
g=sum_a mu_a g_a. This recovers the source's physical vector field -g.

The exact canonical b_1,b_2 are bounded. Consequently (1) defines continuous,
locally Lipschitz maps H to H: tanh and its derivative are globally Lipschitz,
the finite feature contractions are bounded, and products involving M,c are
bounded and Lipschitz on state balls. For example |f_a|<=||c||_2,
||upsilon_a||<=C||c||_2, and ||q_a||_infinity<=C||M||||c||_2.
The constants depend on the fixed feature tables/laws and finite dataset.
These observations justify the continuity and bounded-gradient hypotheses
used below also in the exact-population Hilbert state. No compactness of
Hilbert balls is claimed.

## 2. Exact iid minibatch covariance

For batch size B, let I_{k,1},...,I_{k,B} be iid with law mu, independent of
the past. The actual update, with deterministic step eta_k>0, is

\[
\theta_{k+1}=\theta_k-\eta_k\widehat g_k(\theta_k),\qquad
\widehat g_k=\frac1B\sum_{j=1}^B g_{I_{k,j}}.
\tag{2}
\]

Conditioned on the current state,

\[
E[\widehat g_k\mid\theta_k]=g(\theta_k),\qquad
\mathcal C_B(\theta)=\frac1B\sum_a\mu_a
 (g_a-g)\otimes_H(g_a-g).
\tag{3}
\]

The cross terms for different batch positions vanish by independence and
zero conditional means. In any direction v in H,

\[
\langle v,\mathcal C_Bv\rangle_H
=\frac4B\left\{\sum_a\mu_ar_a^2\langle J_a,v\rangle_H^2
-\left(\sum_a\mu_ar_a\langle J_a,v\rangle_H\right)^2\right\}.
\tag{4}
\]

The covariance range is the span of g_a-g, because the quadratic form of the
finite sum is zero precisely on their common orthogonal complement. Its rank
is at most m-1. Changing B changes only the factor 1/B, never this span. In
particular B=3 has no special rank or escape-direction advantage.

At a mean stationary state g=0, covariance vanishes if and only if every
g_a=0: its trace is B^{-1} sum_a mu_a ||g_a||^2. Away from mean stationarity,
zero covariance merely says all sample gradients coincide and need not mean
zero drift. These distinctions are essential.

## 3. Characterization of common sample-stationary states

The exact canonical feature Grams are positive definite, also after removing
the inactive constants in the sign-paired representation. For b_2 this follows
from tau>0 and independence of the centered H_i. For b_1, conditional on G_i,
k_i=tanh(sqrt(tau) Z_i+alpha h_i) has positive variance, since tau>0 and tanh
is strictly increasing. Thus any nonzero linear combination A h_i+B k_i has
positive second moment: condition on G_i when B is nonzero, and use v>0
otherwise. Independence and zero means across coordinate pairs, and then
the invertible ridge-normalization transform, prove the full statement.

Put v_c=E_2[b_2c]. At any finite state and any nonzero input u_a,

\[
g_a=0,\quad r_a\ne0
\quad\Longleftrightarrow\quad
y_a\ne0,\quad Ma_a=0,\quad v_ca_a^T=0,\quad M^Tv_c=0.
\tag{5}
\]

For the forward implication, the c component in (1) forces h_{2,a}=0 almost
surely. Injectivity of tanh and positive definiteness of the b_2 Gram give
Ma_a=0. Then f_a=0, r_a=-y_a, and upsilon_a=v_c. The M component gives
v_ca_a^T=0. The w component gives
(1-h_{1,a}^2)(b_1^TM^Tv_c)u_a=0 almost surely. An L2 state is finite almost
surely, so 1-h_{1,a}^2>0, and u_a is nonzero. Positive definiteness of the b_1
Gram now gives M^Tv_c=0. Conversely the displayed conditions make all three
components in (1) vanish and give residual -y_a nonzero. This proves (5).

Consequently, at a common sample-stationary state every training prediction is
either exactly its label or zero. Every incorrect prediction has a nonzero
label and satisfies (5). If v_c is nonzero, every incorrectly predicted sample
must additionally have a_a=0. If v_c=0, only Ma_a=0 remains for those samples.

There are large positive-loss absorbing sets. For example, M=0 and v_c=0
make every sample gradient zero for arbitrary w. Another example is w=0,c=0
with arbitrary M. At any such state, (2) is constant for every batch sequence,
every batch size, and every step schedule. These examples also have
sign-paired members. They are statements about the ambient p=1 state space;
they are not counterexamples to convergence from (g,0,D).

## 4. A realizable three-point cubic saddle with exactly zero SGD noise

This construction uses the exact canonical features with d=2. It respects
the odd sign-paired class, retaining only nonconstant feature indices. Let
a_den=sqrt(v+eta_r) and c_den=sqrt(tau+eta_r), with eta_r=1/4096. Select the
first h-coordinate of b_1 and the first H-coordinate of b_2, so those entries
are h_1/a_den and H_1/c_den. Let E_{11} denote the matrix sending that selected
lower coordinate to that selected upper coordinate, with all other entries
zero. Consider the path

\[
w_\varepsilon=\varepsilon h_1e_1,\qquad
c_\varepsilon=\varepsilon H_1,\qquad
M_\varepsilon=\varepsilon E_{11}.
\tag{6}
\]

Uniformly on a fixed finite sphere dataset, Taylor expansion of tanh at zero
gives

\[
(a_a)_1=\frac{\varepsilon v}{a_{\rm den}}(u_a)_1
 +O(\varepsilon^3),\qquad
f_a(\theta_\varepsilon)
=K\varepsilon^3(u_a)_1+O(\varepsilon^5),\quad
K=\frac{v\tau}{a_{\rm den}c_{\rm den}}>0.
\tag{7}
\]

Indeed the lower tanh argument is O(epsilon); the upper argument is
epsilon (H_1/c_den)(a_a)_1=O(epsilon^2); and multiplication by c_epsilon
adds the third factor epsilon. All variables h_1,H_1 are bounded, so the
remainders can be integrated without a limiting interchange issue.

Take the three distinct sphere inputs

\[
u_1=e_1,\qquad u_2=(e_1+e_2)/\sqrt2,\qquad
u_3=(e_1-e_2)/\sqrt2,
\]

with uniform weights. Define labels by the p=1 state theta_1 in (6),
y_a=f_a(theta_1). This is an exactly realizable dataset, not merely a
duplicate/antipodal-compatible one. Each y_a is positive: for t=(u_a)_1>0,
E[h_1 tanh(h_1 t)]/a_den>0, and then
E[H_1 tanh(H_1 A/c_den)]>0 when A>0. There are no duplicate or antipodal
consistency issues. Put S=sum_a mu_a y_a(u_a)_1>0.

At theta_0=(0,0,0), the loss is positive, the mean gradient and every sample
gradient are zero, and the Hessian of the loss is zero. The last assertion
holds because f has no state terms of degree less than three at the origin:
the lower feature contraction is O(w), the upper preactivation is O(Mw), and
the readout supplies c. Equation (7) gives the explicit descent

\[
\mathcal L(\theta_\varepsilon)
=\mathcal L(\theta_0)-2KS\varepsilon^3+O(\varepsilon^5)
<\mathcal L(\theta_0)
\]

for sufficiently small positive epsilon. Thus theta_0 is a genuine cubic
saddle on a realizable three-point sphere problem, yet fresh iid batch-three
SGD started exactly there stays there forever. Its covariance is the zero
operator. This directly refutes a uniform ambient claim that minibatch noise
must act in every cubic escape direction or remove every bad equilibrium.

The state theta_0 differs from canonical initialization (g,0,D), and no part
of this construction proves that canonical SGD reaches or approaches it.
An argument about its stable set or reachability is still required before
using it against a canonical-initialization fitting theorem.

## 5. Exact finite-step escape and exclusion of point limits

### Escape from a small neighborhood

Suppose g_a(theta_*) is nonzero for some a, and eta_k>=eta_min>0. Let
gamma=||g_a(theta_*)||. By continuity choose rho>0 such that

\[
||g_a(\theta)||\ge\gamma/2\quad
\text{when }||\theta-\theta_*||<\rho,
\qquad 2\rho<\eta_{\min}\gamma/2.
\]

If every batch index equals a, which has probability p=mu_a^B>0 conditional
on the past, then for a state inside this ball

\[
||\theta-\eta_k g_a(\theta)-\theta_*||
\ge\eta_{\min}\gamma/2-\rho>\rho.
\]

Hence the process leaves the ball on this event. Conditional on remaining
inside for n successive steps, the next-step exit probability is at least p.
Iterating conditional probabilities gives P(no exit for n steps)<=(1-p)^n.
Exit therefore occurs almost surely, and the expected first exit time is at
most 1/p steps. This result needs no Hessian, diffusion approximation, or
unstable-manifold theorem. The radius depends on the step lower bound.
It gives exit, not avoidance of all returns, loss decrease, or eventual fit.

### Necessary condition for a point limit

More generally suppose the deterministic steps satisfy limsup eta_k>0. Select
an infinite deterministic subsequence with eta_k>=eta_*>0. For each a the
events that all B indices equal a on that subsequence are independent with
probability mu_a^B. The probability of no success in any n specified trials
is (1-mu_a^B)^n; applying this to each tail proves infinitely many successes
almost surely. There are only finitely many a, so this holds for all of them
on one probability-one event.

On that event, if theta_k converges in H to a finite theta_*, then
theta_{k+1}-theta_k tends to zero. Along the repeated-a times,

\[
||g_a(\theta_k)||
=||\theta_{k+1}-\theta_k||/\eta_k\longrightarrow0.
\]

Continuity yields g_a(theta_*)=0 for every a. Combining with (5), each limiting
prediction is either its label or zero, with the latter incorrect only at
the collapsed configurations in (5). For constant steps this is strictly
stronger than mean stationarity. It still allows the absorbing bad states
already exhibited, and it does not imply that the state has a point limit.

This proof uses deterministic steps, or a fixed positive lower bound with
the corresponding conditional-trial argument. It must not be applied
unchanged to an adaptive step selected after seeing the current batch.

## 6. Decreasing steps and the actual scope of stochastic approximation

For eta_k tending to zero, the increment argument above disappears: small
increments no longer force individual sample gradients to be small. A useful
necessary condition remains under the Robbins--Monro step hypotheses

\[
\sum_k\eta_k=\infty,\qquad\sum_k\eta_k^2<\infty.
\tag{8}
\]

If theta_k converges in H to a finite theta_*, then g(theta_*)=0 almost surely.
Here is the complete noise/drift argument. Set
xi_k=hat g_k-g(theta_k), a conditionally centered increment. On any state ball,
||xi_k|| is uniformly bounded, by local boundedness of the finitely many
sample gradients. Stop its increments on the first exit of a deterministic
radius-R ball. The stopped martingale increments eta_k xi_k are orthogonal
in L2(H), and their squared norms have a summable expectation by (8).

For completeness, summable squared increments imply almost sure convergence
as follows. The martingale maximal bound

    P(sup_{n>=j} ||sum_{k=j}^n eta_k xi_k|| >= epsilon)
    <= epsilon^(-2) sum_{k>=j} E||eta_k xi_k||^2

is obtained by stopping the squared-norm submartingale on its first crossing
of epsilon and using orthogonality of later increments; first take a finite
terminal n and then increase it. Choose j_l so the variance tail is at most
2^(-4l), and take epsilon=2^(-l). The probability bounds are summable.
The elementary union-bound tail argument shows that only finitely many of
these events occur almost surely, so the partial sums are Cauchy. Completeness
of H gives convergence. Applying this to each integer R, on the event that
theta_k converges and is therefore bounded, some R has no exit and the
original martingale sum converges.

If g(theta_*)=v is nonzero, continuity gives
<v,g(theta_k)> >= ||v||^2/2 eventually. The exact summed update then has

\[
\langle v,\theta_n-\theta_N\rangle
=-\sum_{k=N}^{n-1}\eta_k\langle v,g(\theta_k)\rangle
 -\left\langle v,\sum_{k=N}^{n-1}\eta_k\xi_k\right\rangle.
\]

The first right-hand term tends to minus infinity by (8), while the second
converges. This contradicts theta_n converging and proves mean stationarity.
The vector v can be random: after vector martingale convergence has been
proved, this final projection is a pathwise argument.

This statement proves neither avoidance of bad mean stationary states nor
convergence of the iterates, and it imposes no common-sample-stationarity
condition. A separate nonconvergence proof would need excitation in the
relevant unstable directions and control of its rate relative to eta_k.
Equations (3)--(7) show that such excitation is not automatic in p=1.

With summable steps, fitting can fail from canonical initialization itself,
without constructing a special basin. The following argument establishes
positive-loss failure; it makes no claim about the limiting mean gradient.
For nonzero labels L(theta_init)>0. Continuity supplies a ball of radius rho
around theta_init with L>=L(theta_init)/2; all finitely many g_a have norm at
most K there. Choose a positive step schedule with total sum eta_k<rho/(2K)
(increase K to a positive bound if necessary). Induction in (2) keeps every
iterate within rho/2, for every batch sequence, so the loss remains positive.
This is an obstruction to claims without step assumptions, not evidence
against the usual nonsummable schedule (8).

## 7. Noise support, cubic directions, and diffusion are distinct questions

At any state with c=0, upsilon_a=q_a=0 and each g_a has only a readout
component. The initial covariance therefore lies entirely in the readout
block. Any movement in w or M must be induced by later states after c changes;
there is no direct instantaneous noise in those blocks. At the origin even
the readout component vanishes. Higher-order loss descent, including the
explicit cubic path (6), does not imply nonzero covariance in that direction.

There is also no general one-step loss decrease near a bad mean stationary
state. Suppose c=0 and sum_a mu_a y_a h_{2,a}=0. Then this is a full mean
stationary state, since all w and M gradients already vanish. One SGD step
changes only c. Holding w,M fixed makes every f_a linear in c, and the
linear cross term in the loss change is exactly zero by the displayed
stationarity condition. Therefore

\[
\mathcal L(\theta_{k+1})-\mathcal L(\theta_k)
=\sum_a\mu_a f_a(\theta_{k+1})^2\ge0
\]

for every batch and every step. This conditional identity concerns escape
geometry, not failure of eventual fitting; subsequent feature motion can
change the conclusion. If an individual y_a h_{2,a} is nonzero, choosing all
batch indices equal a gives a strictly positive increase, since its own
kernel diagonal E h_{2,a}^2 is positive.

At a fixed state the actual step has conditional mean -eta g and covariance
eta^2 C_1/B. A formal diffusion matching these moments on the clock t=k eta
has noise covariance eta C_1/B per unit time. It is not a diffusion with a
fixed, everywhere positive temperature. One can realize its noise columns as
sqrt(eta mu_a/B)(g_a-g), so at every common sample-stationary state both drift
and diffusion vanish. Local Lipschitz coefficients make the constant path
the unique local diffusion solution there as well. Substituting additive
nondegenerate Brownian noise changes the algorithm. Conversely a theorem
about that diffusion over infinite time is not a theorem about (2).

## 8. What has and has not been settled

| Claim | Status and exact scope |
| --- | --- |
| Physical sample gradients and iid batch covariance | Exact identities, all stated finite rules and exact-population p=1 |
| Batch size three opens new covariance directions | False: covariance is C_1/3 |
| Constant-step SGD can converge to a non-common stationary point | Excluded for finite H point limits, almost surely |
| Constant-step SGD exits a small neighborhood of a non-common state | Proved, with radius depending on the step lower bound |
| Every positive-loss p=1 equilibrium is shaken by minibatches | False in ambient state space, even inside the odd invariant class |
| A cubic descending direction guarantees sample-gradient excitation | False by the realizable three-point construction |
| Decreasing-step point limits must be sample stationary | Not implied; under (8) the proved conclusion is mean stationarity only |
| Canonically initialized SGD reaches the absorbing cubic saddle | Not shown |
| Canonically initialized SGD avoids every bad limit set and fits all finite compatible sphere data | Open after this route |

The central remaining bridge is a statement about the reachable process from
(g,0,D): either exclude convergence/approach to the collapsed common-stationary
sets in (5), and control nonconvergent or unbounded behavior, or construct a
canonical trajectory with positive-loss failure under an appropriate step
schedule. Ambient cubic instability and nonzero covariance at other states do
not supply that bridge. No theorem transferring this p=1 result to a trained
finite or infinite neural network has been used or established.

Author check: every displayed implication was rederived from (1), with the
physical metric, positive weights, nonzero sphere inputs, zero-residual cases,
and exact versus finite-population Gram assumptions checked explicitly.
The construction uses a realizable target and the canonical feature law but
does not claim canonical initialization. No numerical checks were necessary
or run. This is the frozen endpoint of one finite theory round.

## 9. Post-freeze strengthening: exactly realizable mixed binary labels

Provenance: after the independent route above was frozen at SHA-256
`47f949fbf20c97813e377268a08e8773ad141f085ec10a924066a055099edfc1`,
the supervisor requested this strengthening to both label values +1 and -1
and supplied the proposed three-point labels and scalar fitting direction.
This section is therefore an informed post-freeze extension, not part of the
independent discovery. No other route or study was read. The original prefix
is preserved except for repairing `g_a=0,quad` to `g_a=0,\quad` in (5); this
is a typesetting correction only. Sections 1--8 were reread completely before
making this extension. No experiment or external retrieval was performed.

Keep the three sphere inputs from Section 4 and uniform weights, but now set

\[
(y_1,y_2,y_3)=(1,1,-1).
\tag{9}
\]

The points are distinct and no two are antipodal, so these labels obey the
duplicate/antipodal compatibility constraints. They are also exactly
realizable in the same canonical p=1 feature law, as the following construction
proves; no fit by a different architecture is substituted.

Let ell=e_1+e_2/5, set w=h_1 ell and M=E_{11}, and retain the source's frozen
features. The three first-layer scalar arguments are h_1 t_a, where

\[
t_1=1,\qquad t_2=\frac6{5\sqrt2},\qquad
t_3=\frac4{5\sqrt2},\qquad 0<t_3<t_2<t_1.
\]

Define

\[
A(t)=\frac1{a_{\rm den}}E_1[h_1\tanh(h_1t)].
\]

Here A(0)=0 and, by differentiation under the expectation,

\[
A'(t)=\frac1{a_{\rm den}}
 E_1[h_1^2\operatorname{sech}^2(h_1t)]>0
\quad\text{for every finite }t.
\]

The derivative integrand is bounded by h_1^2/a_den, which is integrable, and
is positive almost surely except on h_1=0, a probability-zero event. Thus
lambda_a=A(t_a)/c_den are three positive distinct numbers. Because M selects
only the specified lower and upper coordinates, the upper activations are

\[
\psi_a(H_1)=\tanh(\lambda_a H_1).
\tag{10}
\]

Their three-by-three Gram Q_ab=E_2[psi_a(H_1)psi_b(H_1)] is positive definite.
To prove it, suppose q^TQq=0 for a real vector q. The nonnegative square
E_2[(sum_a q_a psi_a(H_1))^2] then vanishes. The law
H_1=tanh(sqrt(v) Z), with v>0 and Z standard normal, gives positive probability
to every nonempty open subinterval of (-1,1). The continuous function
sum_a q_a tanh(lambda_a x) must consequently vanish on that whole interval:
otherwise its nonzero value and continuity would give an open subinterval
with a positive squared integral. Using the first three odd Taylor terms

\[
\tanh x=x-\frac{x^3}3+\frac{2x^5}{15}+O(x^7)
\]

in this identity gives

\[
\sum_aq_a\lambda_a=0,\qquad
\sum_aq_a\lambda_a^3=0,\qquad
\sum_aq_a\lambda_a^5=0.
\]

After setting p_a=q_a lambda_a, this is the Vandermonde system with columns
(1,lambda_a^2,lambda_a^4)^T. Its determinant is
product_{i<j}(lambda_j^2-lambda_i^2), which is nonzero because the positive
lambda_a are distinct. Therefore p=0, then q=0, proving Q positive definite.

Set xi_fit=Q^{-1}y in R^3 and choose the readout

\[
c(H_1)=\sum_{a=1}^3(\xi_{\rm fit})_a\psi_a(H_1).
\tag{11}
\]

This readout is bounded by sum_a |(xi_fit)_a|, hence lies in L2. It is odd under
simultaneous mark negation. Together with w=h_1 ell and M=E_{11}, it belongs
to the same sign-paired state class as Section 4. Direct contraction yields
f_b=E_2[c psi_b]=(Q xi_fit)_b=y_b for each b. Thus the binary dataset (9) is
exactly fitted by an admissible state of the same p=1 system.

Finally use the original cubic path (6), not the fitting state (11). For
the binary labels,

\[
\sum_{a=1}^3\mu_a y_a(u_a)_1
=\frac13\left(1+\frac1{\sqrt2}-\frac1{\sqrt2}\right)=\frac13.
\]

At the all-zero state the loss is now exactly one, every sample gradient and
the covariance are zero, and the Hessian is zero as in Section 4. Equation
(7) gives

\[
\mathcal L(\theta_\varepsilon)
=1-\frac{2K}{3}\varepsilon^3+O(\varepsilon^5)<1
\]

for all sufficiently small positive epsilon. Hence the absorbing cubic saddle
counterexample applies even to three distinct, compatible, exactly realizable
sphere samples whose labels include both +1 and -1. It remains an ambient
state obstruction: neither the fitting construction nor the cubic path
proves reachability of the origin from the prescribed initialization (g,0,D).

## 10. Review correction record

The independent reviewer of the frozen strengthened report at SHA-256
`c7e974c6800abb194e4d68b86af1dd9b7f6facc6ae7631da869b9a2ebef56b46`
identified a mismatch in Section 6: the summable-step ball argument establishes
positive loss but does not establish failure of mean stationarity. The opening
of that paragraph is now narrowed to positive-loss failure from canonical
initialization and explicitly disclaims a conclusion about the limiting mean
gradient. Its proof and all other scientific content are unchanged. This is
the only additional alteration of the earlier prefix beyond the Section 9
typesetting repair. The strengthening's original-prefix hash verification
described in Section 9 refers to the version before this review correction.
