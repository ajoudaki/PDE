# Check of the finite-time activation extension

Scoped proof check, 28 September 2026. The scientific inputs were the complete
`UNIT_LABEL_JOINT_ORDER.md`, `ACTIVATION_EXTENSION.md`,
`ACTIVATION_SMALL_LABEL_ROUTE.md`, and `ACTIVATION_LOCAL_MODULUS.md` in this
study, together with the supervisor's proposed finite-time route. The
`solve-math-rigorously` skill was applied. No other study, book, manuscript,
code, literature, or experiment was consulted. This is an internal proof
dependency, not an independent promotion review.

**Finding.** The proposed route is valid with a strict tube margin and the
qualifications below. It gives a width-independent `C_T/P` bound and closure
continuation on a sufficiently large joint width/order region for all
`Y<=1`, without a Gram gap or successful-fitting assumption. Its source
bound is exactly of the proposed form. Unbounded activation values introduce
fixed feature-RMS factors, but no additional power of width. The only spatial
loss is `sqrt(n)` times the local Lipschitz constant of the gates.

The route does **not** establish closure continuation for every order. This
distinguishes it from the supplied tanh theorem. In particular, its
horizon-independent `P>=exp(n)` corollary cannot automatically be asserted
for every width by enlarging a constant over finitely many exceptional
widths: existence at the exceptional orders has not been proved.

## 1. Precise hypotheses and dense reference bounds

Use the canonical network, loss `L=rho^2`, block mobilities
`(n,1,...,1,n)`, and unchanged raw old-clock closure stated in the supplied
activation extension. Let

\[
 a_\ell=|\phi_\ell(0)|,\qquad
 M_\ell=\|\phi_\ell'\|_\infty<\infty,\qquad
 \phi_\ell\in C^{1,1}_{\rm loc}(\mathbb R).
\]

The activation functions and the finite depth and data are fixed. Assume

\[
 \max_{\ell\ge2}\|W_{0,\ell}\|_{\rm op}\le K,\qquad
 \max_a\|W_{1,0}x_a/\sqrt d\|_2/\sqrt n\le R_0,
 \qquad B_0=\|w_0\|_2/\sqrt n\le1,\qquad Y\le1.
 \tag{1}
\]

Every individual initialized matrix is finite. The first-layer condition
may instead be obtained from a bound on `||W_(1,0)||_F/sqrt(n)` and the fixed
input radius `X=max_a ||x_a||_2/sqrt(d)`. Unlike the tanh theorem, arbitrary
training-visible first-layer RMS is not covered by this proof. No relation
`B_0<=Y` is needed.

For a parameter increment `v`, let

\[
 |v|_n^2=\|v_1\|_F^2/n+
       \sum_{\ell=2}^L\|v_\ell\|_F^2+\|v_w\|_2^2/n.
\]

Put `eta=rho(0)`. Linear growth `|phi_l(u)|<=a_l+M_l|u|` and (1)
give uniform initial feature-RMS bounds, and hence

\[
 \eta\le B_0\max_a\|h_{L,a}(0)\|_2/\sqrt n+Y\le \bar\eta,
 \tag{2}
\]

where `bar eta` depends only on the fixed bounds. Dense gradient flow obeys
the exact identity

\[
 \frac d{dt}\rho_D^2=-|F(\theta_D)|_n^2.
\]

Indeed `F=-D_mob grad L`, and the displayed parameter norm is the norm
defined by `D_mob^(-1)`. Cauchy--Schwarz therefore gives

\[
 d_n(\theta_D(t),\theta_0)
 \le\int_0^t|F(\theta_D)|_n\,ds\le\eta\sqrt t
 \le\bar\eta\sqrt T\qquad(t\le T).
 \tag{3}
\]

At fixed width, this bounds every physical coordinate on each finite
interval. The dense field is locally Lipschitz by the assumed activation
regularity. It is bounded on each resulting compact parameter set, so a
finite maximal endpoint has a limiting state and can be extended by local
existence. This proves dense continuation, before any use of the closure.

## 2. A noncircular stopped region

Start the locally unique raw closure at the prescribed initial moments.
Until time `T`, stop when

\[
 d_n(\widehat\theta(t),\theta_D(t))=1
 \tag{4}
\]

or at its maximal existence endpoint, whichever comes first. Let
`D_T=K+bar eta sqrt(T)+1`,
`B_T=1+bar eta sqrt(T)+1`, and
`R_(1,T)=R_0+X(bar eta sqrt(T)+1)`.
Before the stop, both paths lie in the convex region

\[
 \|W_\ell\|_{\rm op}\le D_T\quad(\ell\ge2),\qquad
 \|w\|_2/\sqrt n\le B_T,\qquad
 \max_a\|W_1x_a/\sqrt d\|_2/\sqrt n\le R_{1,T}.
 \tag{5}
\]

The region is convex because every displayed bound is a norm bound on a
linear function of its own parameter block. All joining parameter segments
therefore remain in this region. Define recursively

\[
 H_1=a_1+M_1R_{1,T},\qquad
 H_\ell=a_\ell+M_\ell D_T H_{\ell-1},\qquad
 \beta_L=M_LB_T,\qquad
 \beta_\ell=M_\ell D_T\beta_{\ell+1}.
 \tag{6}
\]

Thus throughout the region the feature RMS is at most `H_l` and the
backward-response RMS is at most `beta_l`, for every sample. All
preactivation RMS values are at most a fixed `R_T>=1`, obtained by taking
the maximum of `R_(1,T)` and `D_T H_(l-1)`. Choose these numbers using
the full region (5), rather than just the two realized trajectories.

The residual and clock on the stopped closure satisfy

\[
 \rho\le q_T:=B_TH_L+1,\qquad
 0\le\tau-1\le S_T:=Tq_T,\qquad 1\le\tau\le A_T:=1+S_T.
 \tag{7}
\]

All constants in (2)--(7) depend on values at zero and global slopes, not
on any local derivative modulus. No conclusion about proximity is assumed
here beyond the stopping condition (4).

If `eta=0`, all raw velocities, including the clock velocity, vanish, and
both paths are stationary. Otherwise local backward uniqueness prevents
the raw solution from reaching a zero-residual equilibrium at a regular
finite time. Its clock is strictly increasing on each compact pre-stop
interval. This justifies all subsequent clock formulas before a uniform
relative lower bound has been established.

## 3. Forward energy precedes the relative defect estimate

Use the closure's own clock histories, constant forward prefix and zero
backward prefix. Write `b_(l,a)=(r_a/rho)delta_(l,a)` on the physical
part. Use the sample Hilbert norm
`||q||_H^2=(mn)^(-1) sum_a ||q_a||_2^2`, and set

\[
 Z_\ell(t)=\int_0^{\tau(t)}\|\partial_\xi h_\ell\|_H^2\,d\xi,
 \qquad e_E=\sum_{\ell=2}^L\|E_\ell\|_F.
\]

The activation-independent projection identities supplied in the inputs
are

\[
 \dot D_{q,a}=\rho\|q_a-q_a^*\|_2^2,\qquad
 \dot{\widehat\theta}=F(\widehat\theta)+E,
\]
\[
 E_\ell=\frac{2\rho}{mn}\sum_a
 (b_{\ell,a}-b_{\ell,a}^*)(h_{\ell-1,a}-h_{\ell-1,a}^*)^T,
 \qquad E_1=E_w=0.
 \tag{8}
\]

They hold for the actual raw moment ODE, including its original prefix.
The backward array has norm at most `beta_l`. Polynomial endpoint
evaluation has norm `P/sqrt(tau)`; because the backward prefix is zero,
its endpoint error has norm at most `(P+1)beta_l`. The weighted Legendre
tail inequality and the first identity in (8) give

\[
 \int_0^t\rho\|E_\ell/\rho\|_F^2\,ds
 \le2A_T^2\beta_\ell^2 Z_{\ell-1}(t).
 \tag{9}
\]

For clarity, the square of (8) is bounded by
`4(P+1)^2 beta_l^2` times the forward endpoint-error square; its integral
is the forward tail square, at most
`A_T^2 Z_(l-1)/(4P(P+1))`. The ratio `(P+1)/P<=2` proves (9).

The first-layer clock speed is at most `2M_1 X^2 beta_1` in RMS.
At a later layer use
`h_l'=phi_l'(z_l) odot [(F_l/rho+E_l/rho)h_(l-1)+W_l h_(l-1)']`.
Since `||F_l/rho||_F<=2 beta_l H_(l-1)`, (9) and the squared
three-term triangle inequality yield the explicit recursion

\[
 Z_1\le4S_T M_1^2X^4\beta_1^2=:Z_1^*,
\]
\[
 Z_\ell\le Z_\ell^*:=3M_\ell^2\left[
 4S_T\beta_\ell^2H_{\ell-1}^4+
 (D_T^2+2A_T^2\beta_\ell^2H_{\ell-1}^2)Z_{\ell-1}^*\right].
 \tag{10}
\]

These are uniform in width and order. The feature factors `H^4` and
`H^2` are essential for unbounded activations. The recursion uses no
backward derivative and no pointwise estimate on `E/rho`.

The supplied endpoint inequalities, valid also in the sample Hilbert
space, are

\[
 \|h(\tau)-(\Pi_Ph)(\tau)\|_H
 \le C\sqrt{\tau/P}\,\|h'\|_{L^2(H)},\qquad
 \|(\Pi_Pb)(\tau)\|_H\le C\sqrt P\,\|b\|_{L^\infty(H)}.
\]

Using (10), their product in (8) gives

\[
 e_E(t)\le C_T\rho(t).
 \tag{11}
\]

The powers `sqrt(P)` and `1/sqrt(P)` cancel. This remains true for
`P=1` and is derived entirely on the stopped interval.

The canonical updates, (5)--(6), and (11) now give

\[
 |\dot{\widehat\theta}|_n\le C_T\rho,\qquad
 \max_{\ell,a}
 \frac{\|\dot z_{\ell,a}\|_2+\|\dot h_{\ell,a}\|_2}{\sqrt n}
 \le C_T\rho.
 \tag{12}
\]

The prediction Jacobian is bounded from `|.|_n` to sample RMS by `C_T`:
each hidden-block pairing uses
`||u v^T/n||_F=(||u||_2/sqrt(n))(||v||_2/sqrt(n))`, and the outer
blocks have the corresponding explicit normalization. Consequently

\[
 \|\dot r\|_m\le C_T\rho,\qquad |\dot\rho|\le C_T\rho,
\]
\[
 c_T\eta\le\rho(t)\le C_T\eta,
 \qquad\int_0^t\rho\,ds\le C_T\eta,
 \qquad \|\dot c\|_m\le C_T\quad(c=r/\rho).
 \tag{13}
\]

The last assertion follows from
`dot c=(dot r-c dot rho)/rho` and `||c||_m=1`. The lower bound in
(13) is derived, independent of `eta`; it is not a residual-floor
hypothesis. This order of reasoning has no forward-energy/relative-defect
circularity.

## 4. Local curvature and the exact small-residual cancellation

Define, using the previously fixed region radius,

\[
 \ell_{n,T}=\max_\ell\operatorname{Lip}
 (\phi_\ell';[-R_T\sqrt n,R_T\sqrt n]),\qquad
 s_{n,T}=1+\sqrt n\,\ell_{n,T}.
 \tag{14}
\]

Each modulus is finite. A Lipschitz scalar function composed with an
absolutely continuous coordinate is absolutely continuous and has speed
bounded almost everywhere by its Lipschitz constant times coordinate
speed. Thus gate differentiation is legitimate without a classical
second derivative everywhere.

Refining the readout estimate with (13) gives

\[
 \|w(t)\|_2/\sqrt n\le B_0+C_T\eta,
 \qquad \max_{\ell,a}\|\delta_{\ell,a}\|_2/\sqrt n
 \le C_T(B_0+\eta).
 \tag{15}
\]

Each full carrier is `w` or `W_(l+1)^T delta_(l+1)`; its supremum
norm is at most `C_T sqrt(n)(B_0+eta)`. A differentiated gate term
therefore has RMS at most
`C_T ell_(n,T) sqrt(n)(B_0+eta) rho`. The operator-derivative term
has RMS at most `C_T(B_0+eta)rho`; the remaining derivative propagates
through a bounded operator. Using `B_0+eta<=1+bar eta`, induction gives

\[
 \max_{\ell,a}\|\dot\delta_{\ell,a}\|_2/\sqrt n
 \le C_Ts_{n,T}\rho\quad\hbox{a.e.},
\]
\[
 \|\dot b_\ell\|_H
 \le C_T(B_0+\eta+s_{n,T}\rho)
 \le C_T(B_0+s_{n,T}\rho).
 \tag{16}
\]

The final step uses the lower estimate in (13). There is exactly one
RMS-to-coordinate conversion here, on the carrier. No activation
coordinate is bounded independently of width or used as such.

The initial backward jump has Hilbert norm at most `C_T B_0`. Subtract
`b_0 1_[1,tau(t)]` from the history on each terminal interval; the
remainder joins its zero prefix continuously. On a compact physical
interval, (13) and (16) prove that this remainder belongs to `H^1` and
that

\[
 \int_0^{\tau(t)}\|\partial_\xi\widetilde b_\ell\|_H^2\,d\xi
 =\int_0^t\frac{\|\dot b_\ell\|_H^2}{\rho}\,ds
 \le C_T(B_0^2/\eta+s_{n,T}^2\eta).
 \tag{17}
\]

By (12)--(13), the sharper forward energy is

\[
 Z_\ell(t)\le C_T\int_0^t\rho\,ds\le C_T\eta.
 \tag{18}
\]

Let `Q_h,Q_b` be the corresponding Hilbert-valued `L^2` projection
tails. The Legendre derivative tail and the scalar step tail
`||(I-Pi_P)1_[1,tau]||_2<=C sqrt(tau/P)` give

\[
 Q_{h,\ell}\le C_T\sqrt\eta/P,
\]
\[
 Q_{b,\ell}\le C_T\left[
 B_0/\sqrt P+(B_0/\sqrt\eta+s_{n,T}\sqrt\eta)/P\right].
 \tag{19}
\]

The step bound is uniform even when the active clock interval is short:
for `P>=2` place a linear ramp of width `tau/P` on a side of the join
with sufficient room; one side has length at least `tau/2`. Its direct
approximation error is `O(sqrt(tau/P))`, and the derivative-tail estimate
has the same size. For `P=1`, projection contraction suffices.

Integrating (8), using its exact energy identity before Cauchy--Schwarz,
gives

\[
 \int_0^t\|E_\ell\|_F\,ds\le2Q_{b,\ell}Q_{h,\ell-1}.
\]

Multiplying the two estimates in (19) **before** suppressing residual
factors therefore proves

\[
 \int_0^t e_E\,ds\le C_T\left[
 \frac{B_0\sqrt\eta}{P^{3/2}}
 +\frac{B_0+s_{n,T}\eta}{P^2}\right]
 \le C_T\left[\frac{B_0}{P^{3/2}}
                         +\frac{s_{n,T}}{P^2}\right].
 \tag{20}
\]

This verifies the proposed source bound with no inverse residual left.
At `eta=0`, the stationary argument applies instead; no division is
performed there. At `B_0=0`, the prefix jump and its `P^(-3/2)`
contribution vanish. Affine activations have `ell_(n,T)=0` and
`s_(n,T)=1`, which creates no singular case.

## 5. Stability, strict margin, and raw-state continuation

For two parameter points in (5), forward subtraction gives

\[
 \max_{\ell,a}(\|\Delta z_{\ell,a}\|_2+
                    \|\Delta h_{\ell,a}\|_2)/\sqrt n
 \le C_T d_n(\theta,\vartheta).
 \tag{21}
\]

In a backward difference, put the full reference carrier in the gate
difference term. Its RMS is uniformly bounded and its supremum is at
most `C_T sqrt(n)`. Equation (14), (21), the bounded slope, and the
bounded operator terms give inductively

\[
 \max_{\ell,a}\|\Delta\delta_{\ell,a}\|_2/\sqrt n
 \le C_Ts_{n,T}d_n(\theta,\vartheta).
 \tag{22}
\]

No second width loss enters at a lower layer: its recurrence adds one
term of this size and multiplies the next backward difference only by
a fixed operator norm. Subtracting each canonical update as a sum of
one-factor differences, and using (21)--(22), gives

\[
 |F(\theta)-F(\vartheta)|_n
 \le C_Ts_{n,T}d_n(\theta,\vartheta).
 \tag{23}
\]

This finite-difference proof is preferable to an everywhere-defined
classical `DF`: under `C^{1,1}_loc`, the latter need not exist everywhere.
An almost-everywhere segment derivative argument would also suffice if
its absolute-continuity justification is supplied.

Subtracting the physical equations and applying the elementary integral
Gronwall inequality to (20), (23), yields, up to the stop,

\[
 \sup_{s\le t}d_n(\widehat\theta(s),\theta_D(s))
 \le C_*e^{a_0s_{n,T}}
      [B_0P^{-3/2}+s_{n,T}P^{-2}],
 \tag{24}
\]

for fixed `C_*,a_0` depending on `T` and the stated bounds. For example,
replace the nondecreasing source integral by its terminal value, and
differentiate its integral majorant to obtain the exponential factor.

Choose `a>=max(1,a_0)` so large that `exp(a)>=4C_*`, put
`H=exp(a s_(n,T))`, and impose

\[
 P\ge\max\{B_0^2H^2,\ s_{n,T}H\}.
 \tag{25}
\]

Then (24) is at most `2C_*/P<=1/2`, because both terms of (24)
multiplied by `P` are at most `C_*`, and
`P>=s_(n,T)H>=exp(a)>=4C_*`. Thus (25) contains the fixed
continuation threshold in its exponent; alternatively state a separate
lower order floor `P>=4C_*`. Omitting both devices would leave a
strict-margin gap in the stopped argument.

There can now be no first exit through (4). On the stopped interval
the physical variables are bounded at each fixed width, including the
full first matrix by (3)--(4) and its finite initialization. The clock is
in `[1,A_T]`. The exact raw moment integral formulas bound each forward
moment by a constant times `A_T sqrt(n) H_l`, and each backward moment
by a constant times `A_T sqrt(mn) beta_l`; the number of moments is
finite at fixed `n,P`. Thus the full raw state lies in a compact subset
of `tau>0`. Its locally Lipschitz field is bounded there, so a finite
maximal endpoint has a limiting state and extends by local existence.
The strict distance bound persists by continuity. This excludes the
other stopping mechanism and proves continuation through `T` under (25).

Consequently (24) holds through `T` on the joint region (25), and there
the parameter discrepancy is at most `2C_*/P`. Convenient sufficient
conditions are

\[
 P\ge e^{2a s_{n,T}}\quad(B_0\le1),\qquad
 P\ge s_{n,T}e^{a s_{n,T}}\quad(B_0=0),
 \tag{26}
\]

because `exp(a s)>=s` for `s>=1,a>=1`.

## 6. Scope checks and qualifications to preserve

1. Dense continuation is all-order-independent; closure continuation from
   this proof is restricted to (25). For orders outside it, (24) is only
   a stopped estimate. A claim of unrestricted all-order continuation
   would require another argument.
2. The fixed first-preactivation RMS bound is a new hypothesis needed by
   this extension route. Constants must list it, the activation values at
   zero, and global slopes. It is not implied by a finite but otherwise
   arbitrary first-layer initialization uniformly over widths.
3. The radius defining `ell_(n,T)` must cover the whole convex comparison
   region or otherwise explicitly cover every needed preactivation
   segment. The construction (5)--(6) supplies this without using the
   local modulus itself.
4. For globally Lipschitz gate derivatives, `s_(n,T)<=1+H sqrt(n)`.
   Then `P(n)>=exp(n)` eventually satisfies (26) for each fixed `T`,
   giving the desired bound for all sufficiently large widths. It does
   not by itself establish the all-width statement in the supplied tanh
   theorem, since finitely many exceptional widths can contain orders
   whose closure continuation is unproved. A `T`-dependent order floor
   repairs this; so does an independent all-order continuation theorem.
   With only local derivative Lipschitzness, even eventual sufficiency
   of `exp(n)` is not automatic because `ell_(n,T)` may grow rapidly.
5. Training feature and prediction discrepancies follow from (21) and
   the bounded training Jacobian. Uniform prediction comparison on an
   arbitrary bounded test-input set additionally needs uniform initial
   test preactivation RMS, for example an initial first-layer Frobenius
   bound divided by `sqrt(n)`. A training-only bound does not control
   first-layer directions invisible to the training inputs.
6. No positive Gram gap, fitting, sign condition on labels, activation
   boundedness, nonzero lower residual floor, or derivative-curvature
   bound uniform in width is used. No assertion of optimality, useful
   memory compression, or unrestricted width/order convergence follows.

The dependency order is: dense energy and continuation; stopped geometric
bounds; forward clock energy; pointwise relative defect; relative residual
bounds; actual backward source regularity; cancellation in the tail product;
finite-width stability; strict tube margin; raw-state continuation. Each
stage uses only preceding stages or the supplied exact projection identities.

Input SHA-256 values at the check:

| Input | SHA-256 |
| --- | --- |
| `UNIT_LABEL_JOINT_ORDER.md` | `dd9dae39d97da1100092407e4c8a20793ef13f97c104e3679adeeaeaf32b5083` |
| `ACTIVATION_EXTENSION.md` | `b4a3752a88829a02e7ecf75bbd56a2770628bd84946a6feeb3fc95d87811097f` |
| `ACTIVATION_SMALL_LABEL_ROUTE.md` | `ed4baec1cd4a322747fe076068d2308857ae6694e853b2dd9db4f379f32b8b56` |
| `ACTIVATION_LOCAL_MODULUS.md` | `953fc38db089066243286c4d2d81b43c4e819ac10eb0d62fba79cb6f95031732` |

## 7. Supplemental check of the completed finite-time proof

The supervisor subsequently supplied the complete
`ACTIVATION_UNIT_LABEL_FINITE_TIME.md` for review. I read its entire text;
the SHA-256 of that version was
`930eb5c01d97f52f16d51ad6fde3be851543d8327b4a75c80ac8fe8a0ff804e1`.
This supplemental source was explicitly added to the scope. The findings
below concern that concrete version, rather than only the proposed route.

The theorem and proof are valid subject to the minor constant-dependency
clarification below. No mathematical gap was found in the source estimate,
local-gate comparison, or continuation bootstrap.

* The theorem is restricted explicitly to its joint condition (7), and its
  last paragraph states only eventual-in-width sufficiency of orders with
  `log(P(n))/sqrt(n)->infinity` when gate derivatives are globally
  Lipschitz. Thus it avoids the all-order and finite-exception scope errors
  identified above.
* Its (40)--(41) choose
  `Lambda_T>=max{1,a_T,log(4C_*)}`. Because `s_(n,T)>=1`, this gives
  `H>=4C_*` and `H>=s_(n,T)`. Under its (7), both terms of its stopped
  estimate times `P` are at most `C_*`, and `P>=sH>=4C_*`.
  Therefore the strict `d_n<=1/2` margin is correct even when the initial
  readout vanishes or the local gate modulus is zero.
* The proof fixes its convex comparison region and `R_T` before defining
  the modulus. Both actual endpoints and their comparison segments are
  covered. Its (38)--(39) use finite differences, which is the correct
  formulation for locally Lipschitz gate derivatives.
* Its backward remainder estimate (35) and tail product (36)--(37) retain
  the residual factors until their cancellation. The stationary
  zero-residual case is separated. The initial backward step, including
  the nonzero-readout case, is included with its correct `P^(-1/2)` tail.
* At a possible finite raw-state endpoint, the first-layer matrix is
  bounded by its finite initial value, dense displacement, and the tube
  radius; a training-preactivation bound is not improperly substituted
  for a bound on the full raw state. Fixed-width moment coordinates are
  bounded by their exact history integrals. Local raw continuation is
  consequently justified.

The finite-second-moment prediction corollary in its Section 8 is also
correct. Here is its explicit calculation. The additional assumption
`||W_(1,0)||_F/sqrt(n)<=A_1`, together with the dense displacement and
the tube margin, bounds the first matrix on both paths and every joining
segment. Put `u=||x||_2/sqrt(d)`. Uniformly on that segment,

\[
 \|z_1(x)\|_2/\sqrt n\le C_Tu,
 \qquad\|h_1(x)\|_2/\sqrt n\le a_1+C_Tv_1u.
\]

Linear growth and the bounded hidden operators propagate this bound as
`||h_l(x)||_2/sqrt(n)<=C_T(1+u)` through every layer. For a parameter
increment `v`, the first preactivation differential has RMS at most
`u|v|_n`; at later layers

\[
 Dz_\ell[v]=v_\ell h_{\ell-1}+W_\ell Dh_{\ell-1}[v],
 \qquad
 Dh_\ell[v]=\phi_\ell'(z_\ell)\odot Dz_\ell[v].
\]

Using the globally bounded slope at each step gives
`||Dh_l[v]||_2/sqrt(n)<=C_T(1+u)|v|_n`. The readout differential is
`v_w^T h_L/n+w^T Dh_L[v]/n`, so its absolute value is bounded by the
same quantity. Integrating along the parameter segment proves the
manuscript's (42). No local gate-derivative modulus on test inputs is
needed, because this calculation differentiates the activation once only.

For a probability measure `mu`, squaring and integrating (42) gives

\[
 \sup_{t\le T}\|\widehat f(t,\cdot)-f_D(t,\cdot)\|_{L^2(\mu)}
 \le\frac{C_T}{P}
       \left(\int(1+\|x\|_2/\sqrt d)^2\,d\mu(x)\right)^{1/2}.
\]

The right side is finite from a second input moment, since
`(1+u)^2<=2(1+u^2)`. The individual predictors have the same linear
growth bound and are also in `L^2(mu)`. Thus for any square-integrable
target, both RMSEs are finite, and the claimed reverse-triangle-inequality
comparison is justified.

One minor precision edit is recommended: Section 8 should state that its
prediction constants may additionally depend on `A_1`, and that the
measure-dependent constant depends on the displayed second input moment.
The theorem's initial dependency list for `C_T` excludes `A_1`, so using
the same symbol in (42) without this convention leaves that dependence
implicit. This does not change the result or any order threshold.
