# Removing the label threshold for one sample, at arbitrary fixed depth

28 September 2026. Continuation of the width/order and all-time question.
This is a new internal research result, not a change to the paper or maintained
book. The canonical architecture and the original autonomous learning-speed
closure are unchanged. The proof uses the activity/projection identities in
`OLD_CLOCK_ROUTE.md` and `LOSS_DECAY_ACTIVITY_BOOTSTRAP.md`, the endpoint
kernel lemma proved in `SMALL_LABEL_SPECTRAL_SLACK.md`, and the residual-damping
comparison from `SMALL_LABEL_ENERGY.md`. The scalar alignment argument was
derived independently in the scoped dense route; its transfer to the closure
and small-readout extension are derived here.

Internal verification: the coordinator checked the full dense invariant and
compact-horizon derivations. The scoped scalar checker independently checked
the zero-readout closure argument and then checked Sections 4--5 below,
including the initial-residual sign, the never-reached initial activity
branch, and the strict global-cap margin. Its complete zero-readout proof is
`UNIT_LABEL_SCALAR_CHECK.md`. These are internal checks, not promotion reviews.

## 1. Statement, including the joint quantifiers

There is one training pair `(x,y)`, any fixed number `L>=2` of hidden layers,
width `n`, tanh activation, and the manuscript's canonical gradient flow.
Write

\[
 h_1=\tanh(W_1x/\sqrt d),\qquad
 h_\ell=\tanh(W_\ell h_{\ell-1}),\qquad
 f=w^Th_L/n,
 \qquad \rho=|f-y|.
\]

The old-clock closure uses its own responses and residual throughout, with
`tau=1+integral rho`, constant initial forward prefix, zero backward prefix,
and degree-below-`P` Legendre projections. It retains every initialized hidden
matrix exactly. There is no dense-driven oracle in this statement.

Fix `X,K,lambda>0` and assume

\[
 \|x\|/\sqrt d\le X,\qquad
 \max_{2\le\ell\le L}\|W_{0,\ell}\|_{\rm op}\le K,\qquad
 H_0:=\|h_L(0)\|_2^2/n\ge\lambda.
 \tag{1}
\]

Necessarily `lambda<=1`. There exist positive constants `b_*,P_0,A,a,S_*`,
depending only on `L,X,K,lambda`, such that, for every width, every
initialization satisfying (1), every `B_0=||w_0||_2/sqrt(n)<=b_*`, every
`|y|<=1`, and every integer `P>=P_0`, both dense and closure solutions exist
globally, have finite residual activity and finite parameter limits, and
interpolate the training pair. Uniformly in these parameters,

\[
 \int_0^\infty\rho_D\,dt+\int_0^\infty\widehat\rho_P\,dt\le 2S_*.
 \tag{2}
\]

In the sum of normalized parameter-block norms

\[
 d_n=\frac{\|\widehat W_1-W_{1,D}\|_F}{\sqrt n}
 +\sum_{\ell=2}^L\|\widehat W_\ell-W_{\ell,D}\|_F
 +\frac{\|\widehat w-w_D\|_2}{\sqrt n},
\]

the following estimate holds:

\[
 \sup_{t\ge0}d_n(t)
 \le A e^{a(1+\sqrt n)}
 \left\{\frac{B_0}{P^{3/2}}+
                   \frac{1+\sqrt n}{P^2}\right\}.
 \tag{3}
\]

In particular, with `v=1+sqrt(n)`,

\[
 P\ge\max\{P_0,\ B_0^2e^{2av},\ ve^{av}\}
 \quad\Longrightarrow\quad
 \sup_{t\ge0}d_n(t)\le\frac{2A}{P}.
 \tag{4}
\]

The constant in (4) is independent of width, order, time and label within
`|y|<=1`. Zero initial readout removes the middle condition in (4). For all
readouts bounded by `b_*<=1`, the simpler sufficient condition
`P>=max(P_0,e^{2av},ve^{av})` applies.

The constants can also be chosen so that on this joint region
`rho_hat(t)<=rho_hat(0)exp(-gamma t)` for a positive width-independent
`gamma`. In fact, after the small-readout threshold is fixed, this decay
requires only `P>=max(P_0,C(1+sqrt(n)))`; the much larger order in (4)
is needed for the current tracking estimate, not for this fitting rate.

This is an **all-time, joint-width/order theorem without a small-label
restriction, for one training sample and arbitrary fixed depth**. It is not
yet the arbitrary-multi-input theorem. The certified order is very large;
it does not certify useful low-rank compression as width tends to infinity.
The same proof treats any prescribed finite label bound in place of 1,
with constants allowed to depend on that bound.

## 2. Activity estimates used below

Use `||u||_H=||u||_2/sqrt(n)`. For a cap
`s(t)=integral_0^t rho<=S`, put

\[
 A_S=1+S,\qquad B_S=B_0+2S,\qquad
 \beta_L=B_S,\quad D_\ell=K+2A_S\beta_\ell,
 \quad\beta_{\ell-1}=D_\ell\beta_\ell.
 \tag{5}
\]

The exact moment representation and projection contraction give
`||W_l||op<=D_l`, `||delta_l||_H<=beta_l`, and `||w||_H<=B_S`, uniformly
over `P,n` on the cap. The dense history integral has the same bounds.
The readout estimate follows directly from `||dot w||_H<=2rho`.

For the forward clock derivatives define

\[
 Z_1=4SX^4\beta_1^2,\qquad
 Z_\ell=3\{4S\beta_\ell^2+
              (D_\ell^2+2A_S^2\beta_\ell^2)Z_{\ell-1}\}.
 \tag{6}
\]

They bound `integral_0^tau ||partial_xi h_l||_H^2 dxi`. If `E` denotes the
exact physical velocity defect, it has only hidden-matrix blocks, and

\[
 \dot{\widehat\theta}=F(\widehat\theta)+E,\qquad
 \int_0^t e_E\,du\le \frac{C_E(S,B_0)}{\sqrt{P(P+1)}},\qquad
 C_E=A_S\sum_{\ell=2}^L\beta_\ell\sqrt{S Z_{\ell-1}},
 \tag{7}
\]

where `e_E=sum_(l>=2)||E_l||_F`. These are unconditional stopped-path
estimates; they do not assume fitting or a Gram lower bound. The prefix
makes the forward history continuous and its derivative square integrable.

For clarity, (7) follows from two exact projection identities. If `D_h,D_b`
are squared Hilbert-valued history tails at the moving endpoint, then

\[
 \dot D_h=\rho\|h-h^*\|_H^2,\qquad
 \dot D_b=\rho\|b-b^*\|_H^2,
\]
\[
 E_\ell=2\rho\,(b_\ell-b_\ell^*)\otimes
                   (h_{\ell-1}-h_{\ell-1}^*),\qquad
 \int_0^t\|E_\ell\|_F\,du\le2\sqrt{D_b(t)D_h(t)}.
 \tag{8}
\]

Here `u tensor v=uv^T/n`, `b=(r/rho)delta`, and a star means evaluation of
the history projection at the current endpoint. Bounding `D_b<=S beta_l^2`
and using the Legendre derivative tail
`D_h<=A_S^2 Z_(l-1)/(4P(P+1))` proves (7). The recursive proof of (6)
uses the exact defect in (8); its squared integral cancels the endpoint
projection amplification, as detailed in the cited old-clock proof.

The output differential on hidden blocks also satisfies the stronger
instantaneous bound

\[
 |JE|\le B(t)M(S,B_0)e_E,
 \qquad B(t)=\|w(t)\|_H,
 \qquad M=\max_{\ell\ge2}\prod_{j=\ell+1}^L D_j.
 \tag{9}
\]

Indeed `||delta_l(t)||_H<=B(t)prod_(j>l)D_j` by backpropagation, and
`|delta_l^T E_l h_(l-1)/n|<=||delta_l||_H||E_l||_F`.
This uses the instantaneous readout norm, so division by `B(t)` will not
introduce a singular constant at zero readout.

Finally,

\[
 |H(t)-H_0|\le2\sqrt{S Z_L},\qquad H=\|h_L\|_H^2.
 \tag{10}
\]

This follows by integrating the forward derivative and using `||h_L||_H<=1`.
When `B_0<=S` and `S` tends to zero, the displayed recursions give
`beta_l=O(S)`, `Z_l=O(S^3)`, `C_E=O(S^3)`, and `M=O(1)`, with constants
depending only on the fixed data in (1).

## 3. The nonperturbative scalar alignment identity

If the initial residual is zero, dense and closure dynamics are stationary
and (3) is immediate. Otherwise put `sigma=sign(y-f(0))`. Their residuals
keep this sign at every finite time: a zero-residual state is an equilibrium
of the raw locally Lipschitz ODE, and backward uniqueness excludes hitting
such a state from a nonstationary path. Global finite-time continuation is
provided by the old-clock bounds (or, on a stopped activity interval, by (5)).

Let `g=sigma f`, `B=||w||_H`, and, whenever `B>0`, `q=g/B`. The scalar
canonical tangent Gram is

\[
 \Gamma=H+X_x^2\|\delta_1\|_H^2+
       \sum_{\ell=2}^L\|\delta_\ell\|_H^2\|h_{\ell-1}\|_H^2,
 \qquad X_x=\|x\|/\sqrt d.
\]

Consequently `Gamma>=H>=q^2`. The readout and output equations give exactly

\[
 \dot B^2=4\rho g,\qquad
 \dot g=2\rho\Gamma+\sigma JE,\qquad
 \dot q=\frac{2\rho}{B}(\Gamma-q^2)+\frac{\sigma JE}{B}.
 \tag{11}
\]

For dense flow, `E=0`: once `q` is positive it cannot decrease. For the
closure, (9) gives, on any activity cap,

\[
 q(t)\ge q(t_0)-M\int_{t_0}^t e_E\,du.
 \tag{12}
\]

This is an approximate monotonicity law, not an estimate that the features
remain near their initial values. It is the new reason large labels can be
handled for one sample.

At exactly zero initial readout and nonzero label,

\[
 w(t)=2\sigma |y|h_L(0)t+o(t),\qquad
 g(t)=2|y|H_0t+o(t),\qquad
 q(0+)=\sqrt{H_0}.
 \tag{13}
\]

These expansions hold for the closure too: all backward responses and all
weight velocities except the readout initially vanish. A positive lower
bound on `q` makes `dot B=2rho q>0`, so the denominator in (11) cannot
subsequently disappear. For the dense zero-readout flow, (11)--(13) yield
`Gamma>=H>=H_0` for all time, hence

\[
 \rho_D(t)\le |y|e^{-2H_0t},\qquad
 \int_0^\infty\rho_D\,dt\le |y|/(2H_0).
 \tag{14}
\]

This dense statement holds for arbitrary finite label magnitude.

## 4. Short initial interval for small nonzero readout

This step extends the closure argument to the actual vanishing random
readout convention; it does not restrict the labels. Choose `s_b>0` small
enough that the cap constants computed with `S=s_b` and `B_0=s_b` satisfy

\[
 2\sqrt{s_b Z_L}\le\lambda/2,
 \qquad B_S M C_E/\sqrt2\le\lambda s_b/4.
 \tag{15}
\]

Such a choice exists: the left sides are respectively `O(s_b^2)` and
`O(s_b^4)`. Set

\[
 b_*\le\min\{1,s_b,\lambda s_b/4\}.
\]

Until accumulated activity reaches `s_b`, (10) gives `H>=lambda/2` for
every order. If it reaches `s_b` at time `t_b`, integrate (11), use
`g(0)>=-B_0`, `Gamma>=lambda/2`, and (7), (9), (15), to get

\[
 g(t_b)\ge-B_0+\lambda s_b-\lambda s_b/4
              \ge\lambda s_b/2,
 \qquad B(t_b)\le B_0+2s_b\le3s_b.
\]

Therefore

\[
 q(t_b)\ge\lambda/6.
 \tag{16}
\]

If this activity level is never reached, the initial Gram lower bound
persists for the entire path. The argument allows `y=0`, either initial
residual sign, and a readout not aligned with the initial features. It uses
smallness only of the initialized readout, as in the canonical convention.

## 5. Closing the activity cap without small labels

Put `gamma=lambda^2/144` and choose
`S_*=max(2s_b,2/gamma)`. Form (5)--(9) at this cap with `B_0=b_*`;
all resulting constants are finite and independent of `n,P,y`.
Choose `P_0` large enough that

\[
 M C_E/P_0\le\lambda/12,
 \qquad B_{S_*}M C_E/P_0\le1.
 \tag{17}
\]

After `t_b`, (12), (16) and (17) keep `q>=lambda/12`, hence `H>=gamma`.
The continuation of this assertion is justified by stopping additionally
at the first zero of `B`; while `q>0`, (11) implies `B` is increasing, so
that stopping event cannot occur. Before `t_b`, `H>=lambda/2>=gamma`.

Since `rho(0)<=|y|+B_0<=2`, the exact residual equation gives, up to first
attainment of the cap,

\[
 \rho(t)+2\gamma s(t)
 \le\rho(0)+\int_0^t|JE|\,du\le3.
 \tag{18}
\]

Thus `s(t)<=3/(2gamma)<S_*`. First activity exit is impossible. The moment
integral representation bounds all internal state variables on this cap;
local continuation excludes any finite maximal endpoint. This proves global
existence, a uniform Gram lower bound, and finite activity for the closure.
The same reasoning with `E=0` applies to dense flow. Dense residuals in fact
obey `rho_D(t)<=rho_D(0)e^(-2gamma t)`.

The physical velocity has the bound
`||dot theta||_mob<=C rho+e_E`. Both terms have finite integrals by (7)
and (18), so the parameters converge. Prediction continuity gives a residual
limit, and finite integral of the residual forces that limit to be zero.
This proves interpolation. No closure exponential-decay assumption was used.

## 6. The stronger all-time defect for one sample

The scalar residual direction is constant, so `b=-sigma delta`; there is
no differentiated residual direction. This removes the terminal-history
difficulty present for multiple samples.

We first bound velocities in the clock coordinate independently of `P`.
On an interval of clock length at most `A=1+S_*`, the endpoint estimates are

\[
 \|h-h^*\|_H\le C\sqrt{A/P}\|h'\|_{L^2},\qquad
 \|b^*\|_H\le C\sqrt P\|b\|_{L^\infty}.
 \tag{19}
\]

The first is integration by parts against the Legendre endpoint kernel;
the second is its `L1` bound `||K_P||_1<=C sqrt(P)`. The proof, including the
square-root kernel bound, is in Section 2 of `SMALL_LABEL_SPECTRAL_SLACK.md`.
Equations (6), (8), and (19) cancel the powers of `P` and give

\[
 e_E(t)\le C\rho(t),\qquad
 \|\partial_\xi W_1\|_F/\sqrt n+
 \sum_{\ell=2}^L\|\partial_\xi W_\ell\|_F+
 \|\partial_\xi w\|_H\le C.
 \tag{20}
\]

The forward chain rule now gives `||partial_xi z_l||_H<=C` and
`||partial_xi h_l||_H<=C` pointwise. All constants here are uniform in
time, width and order, after (18).

Differentiating backpropagation incurs at most one width factor. At the top,

\[
 \delta_L'=w'\odot\tanh'(z_L)+
                w\odot\tanh''(z_L)\odot z_L'.
\]

Use `||w||infty<=sqrt(n)B_S`, `|tanh''|<=2`, and (20). At lower layers,

\[
 \delta_\ell'=
 \tanh''(z_\ell)\odot z_\ell'\odot W_{\ell+1}^T\delta_{\ell+1}
 +\tanh'(z_\ell)\odot
       \{(W_{\ell+1}')^T\delta_{\ell+1}
                             +W_{\ell+1}^T\delta_{\ell+1}'\}.
\]

The undifferentiated carrier has supremum norm at most
`sqrt(n)D_(l+1)beta_(l+1)`; the derivative terms use (20) and the next-layer
bound. Downward induction proves

\[
 \|\delta_\ell'\|_H\le C(1+\sqrt n).
 \tag{21}
\]

At zero readout the backward prefix is continuous. More generally write
`b=b_cont+b(1+)1_[1,tau]`. The continuous part has derivative given by
(21), while `||b(1+)||_H<=CB_0`. The `L2` projection error of this step is
at most `CB_0/sqrt(P)`: approximate it by a ramp of width `tau/P`; the ramp
approximation costs `O(B_0/sqrt(P))`, and the Legendre derivative bound
for that ramp costs the same. Projection contraction controls the remaining
step-minus-ramp term, also if the final history interval is shorter than
the ramp. Thus, uniformly in the endpoint,

\[
 \|(I-\Pi_P)h\|_{L^2}\le C/P,\qquad
 \|(I-\Pi_P)b\|_{L^2}\le C\{B_0/\sqrt P+(1+\sqrt n)/P\}.
 \tag{22}
\]

Apply the exact absolute-defect pairing (8), then take increasing endpoints:

\[
 \int_0^\infty e_E\,dt\le
 C\{B_0/P^{3/2}+(1+\sqrt n)/P^2\}=:\varepsilon_{n,P}.
 \tag{23}
\]

This uses finite activity, not an assumed terminal residual rate. The
constant residual direction is what makes the stronger tail estimate
available for all time here.

### Exponential closure fitting as a further consequence

This can be deduced after, rather than assumed in, the activity proof.
Apply the first endpoint inequality in (19) to the continuous part of
`b`, and the second to its prefix step. Together with (21), this gives

\[
 \|b-b^*\|_H\le
 C\{B_0\sqrt P+(1+\sqrt n)/\sqrt P\}.
\]

The forward endpoint error is at most `C/sqrt(P)`. Equation (8), followed
by (9) and the bounded readout, therefore proves

\[
 |JE(t)|\le C\rho(t)
              \{B_0+(1+\sqrt n)/P\}.
 \tag{23a}
\]

Freeze this `C` at the already established cap and readout threshold.
Reduce `b_*` further so that `C b_*<=gamma/2`. On the existing
`P>=P_0` fitting regime, impose also `P>=2C(1+sqrt(n))/gamma`.
Since `Gamma>=gamma`, the exact residual equation then yields
`dot rho<=-gamma rho`. Constants are frozen before decreasing `b_*`,
so there is no circular choice. At zero readout no additional readout
restriction is needed. Enlarging `a` in (4) makes its joint order condition
imply this linear-in-sqrt(n) threshold. This establishes the decay assertion
in Section 1.

## 7. Feedback comparison and the joint order bound

On the common operator/readout/activity bounds just proved, forward response
differences are bounded by `C d_n`. Backpropagation differences obey

\[
 \max_\ell\|\widehat\delta_\ell-\delta_{\ell,D}\|_H
          \le C(1+\sqrt n)d_n.
 \tag{24}
\]

To verify the width factor, subtract each gate-times-carrier expression.
The carrier difference is propagated through matrices of bounded operator
norm. The gate difference is bounded in RMS by twice the preactivation
difference, and its dense carrier has supremum norm at most
`sqrt(n)D beta`. A single downward induction gives (24); no product of
width factors arises because the differentiated gate terms are added.
Consequently `|Gamma_hat-Gamma_D|<=C(1+sqrt(n))d_n`.

Let `v=|f_hat-f_D|`. Subtracting residual equations and using the closure
Gram lower bound gives

\[
 D^+v\le-2\gamma v+C(1+\sqrt n)\rho_D d_n+C e_E.
\]

Both trajectories start together. Integrating, and dropping the nonnegative
terminal `v`, yields

\[
 \int_0^t v\,du\le
 C(1+\sqrt n)\int_0^t\rho_D d_n\,du+C\varepsilon_{n,P}.
 \tag{25}
\]

In every parameter equation split a product difference with the closure
response multiplying the residual difference and the dense residual
multiplying response differences. Bounds (24) then give

\[
 d_n(t)\le C\int_0^t v\,du+
 C(1+\sqrt n)\int_0^t\rho_D d_n\,du+\varepsilon_{n,P}.
\]

Insert (25) and apply integral Gronwall in the measure `rho_D dt`, whose
total mass is at most `S_*`. This proves

\[
 \sup_{t\ge0}d_n(t)\le C\varepsilon_{n,P}e^{C(1+\sqrt n)},
\]

which is (3). Multiplication by `P` shows immediately why (4) suffices:
its two terms are respectively
`B_0 e^(av)/sqrt(P)<=1` and `v e^(av)/P<=1`.

For inputs with `||x_test||/sqrt(d)<=R`, tanh's Lipschitz property and the
same operator bounds imply

\[
 \sup_{t\ge0}\sup_{\|x_{test}\|/\sqrt d\le R}
       |\widehat f(t,x_{test})-f_D(t,x_{test})|
       \le C_R\sup_{t\ge0}d_n(t).
 \tag{26}
\]

Therefore (4) also controls whole-input-set prediction error, test RMS
discrepancy for any probability measure on that set, and the difference of
test RMSEs to any square-integrable target, by the reverse triangle inequality.

## 8. What this does and does not settle

For one sample, the small-label threshold has been removed without changing
the canonical dynamics, at any fixed depth, including the vanishing random
readout once `B_0<=b_*`. The latter condition and (1) hold with probability
tending to one under the canonical Gaussian initialization and a fixed
nonzero input: the fixed-depth initial feature variance is positive,
empirical variances concentrate, and the initialized hidden operator norms
are bounded with high probability. The deterministic implication above
does not require Gaussian independence along training.

For several samples, the scalar `sigma` is replaced by a rotating residual
direction. The monotone ratio in (11) is no longer the ratio controlling
loss descent. Also differentiating `b_a=(r_a/rho)delta_a` introduces that
direction's derivative. Neither problem is solved by increasing `P` alone
in this argument. The separate multi-input compact-horizon result is in
`UNIT_LABEL_JOINT_ORDER.md`. An arbitrary-multi-input, all-time theorem at
`Y<=1` remains open; the one-sample theorem is not a substitute for it.
