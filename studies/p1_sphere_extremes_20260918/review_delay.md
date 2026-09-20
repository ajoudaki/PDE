# Independent isolated review: initialized delay and necessary potential growth

## Verdict and frozen scope

**MINOR REVISION REQUIRED.** Every principal exact-closure claim in the
assignment is verified below: admissibility and balance, the complete physical
gradient metric, global characteristic existence, the moving-state
`Omega(epsilon^-2)` threshold delay, the strictly positive `Theta(epsilon^4)`
initial slope, the close-pair path-energy bound, and the differentiable-potential
growth implication. The sole required correction is that the optional Dini
derivative extension in `necessary_potential_growth.md`, lines 69–70, must
require continuity along the trajectory and specify the upper-right Dini
derivative. Without that qualification the scalar comparison claim is false.
This does not affect the ordinary differentiable-potential result or either
delay theorem. The unqualified frozen text does not receive an overall PASS.

This review was derived independently from the neutral assignment and only:

- `early_delay.md`, complete, SHA-256
  `33204d4e12dc00a9ef7325a5187637ac9ace52e9787ca5cd3ac60f2a6fc27a71`;
- `necessary_potential_growth.md`, complete, SHA-256
  `e7e9594ed6f23f233eca1fd763836f7c99bead519f99aee6fee3370e3e732ab7`;
- `docs/observable_p1.md`, complete, SHA-256
  `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba`;
- `docs/global_nonlinear.md`, C.4.7.9.3–4 and C.4.7.10.D.3 through its
  model/state/equations and energy/existence material;
- the required `solve-math-rigorously` and `investigate-conjectures` skills,
  including research-contract and adversarial-audit instructions.

No author startup, study history, other studies, other reviews, code, numerical
experiments, quadrature, or population approximation was used. The frozen
inputs were not edited. The target is the exact fixed-order population closure;
the established d=2 network-identification theorem is not being extended.

## 1. Initialization, parity, metric, and existence

Let `phi=tanh`, `q=phi'=sech^2`, and use the exact scalar coefficients of
`docs/observable_p1.md`, with ridge `eta=1/4096`. All scalar denominators are
positive. In particular `0<v,tau,s<1`, `alpha=1-tau>0`, `gamma=1-s>0`, and

\[
b^2=s+\eta-\frac{\beta^2}{v+\eta}
\ge \eta+\frac{s\eta}{v+\eta}>0.
\]

For positivity of `beta`, conditional on `G` the function
`E_Z phi(sqrt(tau) Z+alpha tanh G)` is odd in `tanh G`, vanishes at zero,
and has strictly positive derivative with respect to that argument. Therefore
its product with `tanh G` is strictly positive almost surely off zero. This
proves `beta>0`, and the source's two nonzero bands

\[
d_h=\frac{\alpha v}{a\sqrt{\tau+\eta}},\qquad
d_k=\frac{\alpha\beta\eta/(v+\eta)+\tau\gamma}
 {b\sqrt{\tau+\eta}}
\]

are both positive. The active matrix is `D=[d_h I_3, d_k I_3]`; hence
`||D||op=sqrt(d_h^2+d_k^2)`, as asserted in the potential note.

The lower pair `(b1,g)` retains the joint dependence through
`k_i=phi(sqrt(tau) Z_i+alpha phi(G_i))`. Conditioning on `G` later is an
integration identity and does not replace this joint population by independent
marks. The upper coordinates are independent symmetric nondegenerate variables
`b2_i=phi(sqrt(v) Ztilde_i)/sqrt(tau+eta)`, on a separate population space.

Deleting constants is legitimate for this initialized flow. Under simultaneous
lower mark negation, `g,w,b1` are odd and the lower gate is even, so the constant
pairing of `phi(w.u)` vanishes. Under simultaneous upper mark negation,
`b2,c,H` are odd and the upper gate is even, so the constant pairing of
`c q(z)` vanishes. Consequently the constant row and column of `M` have zero
velocity, while the row and readout velocities preserve oddness. This needs
no data symmetry. The inactive coordinates contribute zero to the full metric;
the active `3 by 6` matrix still evolves without an entrywise restriction.

For each full normalized feature column, direct use of the Cholesky identity
gives

\[
E[b_l b_l^T]=L_l^{-1}G_lL_l^{-T}
=I-\eta L_l^{-1}L_l^{-T}\preceq I.
\]

The active covariance is a principal block and has the same inequality. Thus
`U_l v=b_l^T v` and its adjoint are contractions. The stated feature envelopes
follow by `|h_i|,|k_i|,|H_i|<=1`:

\[
K_1^2\le \frac3{a^2}
+\frac{3(1+\beta/(v+\eta))^2}{b^2},\qquad
K_2^2\le\frac3{\tau+\eta}.
\]

To verify the metric without an imported factor, variation of the prediction
has the three components

\[
\delta_c f=E_2[\delta c\,H],\qquad
\delta_M f=d^T(\delta M)a,\qquad
\delta_w f=E_1[q(w\cdot u)Q(u)(\delta w\cdot u)].
\]

Multiplication by `2 mu_a r_a` and summation produces precisely the three
velocities in equation (1) of `early_delay.md`. These are negative gradients
for the two probability-weighted population L2 metrics and coefficient
Frobenius metric, so

\[
L'=-\|w'\|_2^2-\|M'\|_F^2-\|c'\|_2^2.
\]

No additional population weight or hidden layer mobility is missing. This also
verifies the factor four in the initial-slope formula below.

On bounded sets of `(w-g,c,M)` in `L-infinity x L-infinity x R^(3 by 6)`,
the right side is locally Lipschitz: frozen features are bounded, the data set
is finite with `|u|=1`, and `phi,q` are bounded Lipschitz functions. Frozen
unbounded `g` occurs inside those gates, not as an unbounded coefficient.
The Banach contraction construction in the supplied source therefore applies
in dimension three without changing a hypothesis. At a local solution,
`L(0)=1`, `L<=1`, and `sum mu_a |r_a|<=sqrt(L)<=1`. Consequently

\[
\|c(t)\|_\infty\le2t,\quad |a(u)|\le1,\quad
|d(u)|\le\|c(t)\|_2,\quad
\|M(t)-D\|_F\le2t^2,
\]
\[
\|w'(t)\|_\infty
\le2K_1\|M(t)\|_{op}\|c(t)\|_2
\le4tK_1(\|D\|_{op}+2t^2).
\]

All variables in the local existence space, and their velocities, remain
bounded on each finite interval. They have endpoints in that Banach space and
can be continued. This proves unique global characteristic existence on every
finite time interval. It does not assert uniqueness in a larger uncontrolled
distributional solution class. Differentiation of the loss and time integration
are justified in this bounded characteristic class.

## 2. Geometry and the moving-state delay

Write `a_epsilon=sqrt(1-epsilon^2-epsilon^4)`. For `0<epsilon<=1/2`, it is
real and positive. The three unit input rows are
`(a_epsilon,epsilon,epsilon^2)`, `(a_epsilon,-epsilon,epsilon^2)`, and
`(1,0,0)`. Expansion along the last row gives determinant `2 epsilon^3`,
so they are distinct and linearly independent at every positive member.
Multiplying by `sqrt(3)` gives the required input sphere and preserves
independence. The positive label has mass `1/4+1/4=1/2`; the negative label
has mass `1/2`. Initialization has zero prediction and loss exactly one.

For any current `w in L2`, the vector-valued function
`a(u)=E[b1 phi(w.u)]` is C2 on R3. Its first and second derivatives are
dominated by integrable multiples of `|w|` and `|w|^2`, respectively;
dominated convergence also gives continuity of those derivatives. Put
`W=||w||2`, `B=||M||op`. For unit `v`,

\[
|\partial_v a|\le W,\qquad
|\partial_v^2a|\le2K_1W^2.
\]

The first bound uses the analysis contraction and `|q|<=1`; the second uses
`|phi''|<=2` and the feature envelope. It needs no fourth moment of `w`.
For `z=b2^T M a`,

\[
\|\partial_vz\|_2\le BW,\quad
\|\partial_vz\|_\infty\le K_2BW,\quad
\|\partial_v^2z\|_2\le2K_1BW^2.
\]

The chain rule and the mixed L-infinity/L2 product estimate yield

\[
\|\partial_vH\|_2\le BW,\qquad
\|\partial_v^2H\|_2
\le2\|\partial_vz\|_\infty\|\partial_vz\|_2
+\|\partial_v^2z\|_2
\le2BW^2(K_1+K_2B).
\]

These bounds hold uniformly in `u`, including the off-sphere segments used
for the difference estimate. For `v_epsilon=(a_epsilon,0,epsilon^2)`,

\[
1-a_\varepsilon
=\frac{\varepsilon^2+\varepsilon^4}{1+a_\varepsilon}
\le\frac54\varepsilon^2,
\quad
|v_\varepsilon-e_1|\le\frac{\sqrt{41}}4\varepsilon^2
<2\varepsilon^2.
\]

The centered second difference of `H` over `+/-epsilon e2` has norm at most
`epsilon^2 sup ||partial_22 H||2`. Decomposing the signed feature into one
quarter of that centered difference plus one half of
`H(v_epsilon)-H(e1)` gives exactly

\[
\|m_\varepsilon(\theta)\|_2
\le\varepsilon^2
\left[BW+\tfrac12 BW^2(K_1+K_2B)\right].
\]

In particular, on the full raw ball
`R^2=||w-g||2^2+||M-D||F^2+||c||2^2<=1`, one may take
`W_*=sqrt(3)+1`, `B_*=||D||op+1`, and the exact `K,C=2K` in the note.
All are finite, positive, and independent of epsilon.

Expanding the unhalved loss gives, at any state,

\[
1-L=2\langle c,m_\varepsilon\rangle_2-\sum_a\mu_af(u_a)^2.
\]

Thus on a reached state with `R<=1`,

\[
0\le1-L\le C\varepsilon^2R.
\]

The integrated physical energy identity, with Hilbert-space
Cauchy–Schwarz in time, independently gives

\[
R(t)^2\le t\int_0^t\|\theta'(s)\|_{raw}^2ds=t(1-L(t)).
\]

This inequality makes no small-displacement assumption on intermediate
times. Combining the two estimates at a time with `R<=1`, and handling
`R=0` separately, proves

\[
R(t)\le C\varepsilon^2t,\qquad
1-L(t)\le C^2\varepsilon^4t.
\]

If `R` first reaches one at `t_*`, those same estimates at the first hitting
time give `t_*>=1/(C epsilon^2)`. Continuity therefore validates both bounds
on the entire claimed closed interval. For fixed `delta>0` and sufficiently
small epsilon with `C epsilon^2<delta`, loss `<=1-delta` is impossible on
the raw unit ball. Its hitting time must follow a first exit and is at least
`1/(C epsilon^2)`, with infinity allowed.

This controls the actual complete state, including arbitrary changes of all
eighteen middle entries and both moving populations. For
`t_epsilon=o(epsilon^-2)`, the interval condition eventually holds and the
complete raw displacement tends to zero. For every fixed finite `t`, it also
gives `L_epsilon(t)->1`. Hence a common loss upper envelope valid for all
positive epsilon must be at least one at every finite time, and cannot tend
to zero. No exchange with an infinite-time limit or initial-slope inference
is used.

## 3. Initial expansion and complete nonvanishing argument

The initialized conditional representation in the note is exact. Namely set

\[
\bar k(s)=E_Z\phi(\sqrt\tau Z+\alpha\phi(s)),\quad
F(s)=A\phi(s)+B\bar k(s),
\]
\[
A=d_h/a-d_k\beta/[b(v+\eta)],\qquad B=d_k/b>0.
\]

Multiplying the two active bands of `D` by the lower feature contraction
and then conditioning on `G` yields

\[
z_0(u)=\sum_{i=1}^3 b_{2i}E[F(G_i)\phi(G\cdot u)].
\]

Here `F` is odd, bounded, and smooth with bounded first derivative; Gaussian
integration by parts therefore has vanishing boundary terms. Define

\[
v_*=E[F(G)\phi(G)],\qquad
\kappa=E[q(G)]E[F'(G)],\qquad \rho=E[q(G)F'(G)].
\]

Independence and oddness give the following complete derivative list needed
for the expansion:

\[
z_0(e_1)=v_*b_{21},\quad
\partial_2z_0(e_1)=\kappa b_{22},\quad
\partial_3z_0(e_1)=\kappa b_{23},\quad
(\partial_{22}-\partial_1)z_0(e_1)=-\rho b_{21}.
\]

For the transverse first derivatives, the sole surviving coordinate uses
`E[G F(G)]=E[F'(G)]`. For the last identity, the sole surviving coordinate
uses

\[
E[F(G)(\phi''(G)-Gq(G))]=-E[F'(G)q(G)],
\]

obtained by integrating the derivative of `F q` against the Gaussian.
All other terms vanish by an odd independent factor; in particular, no
unlisted transverse derivative term survives.

Since
`u_+/-=e1 +/-epsilon e2+epsilon^2(e3-e1/2)+o(epsilon^2)`, the C2 expansion
in upper L2 yields

\[
m_\varepsilon=\varepsilon^2V+o_{L^2}(\varepsilon^2),\quad
V=\tfrac12\partial_3H_0(e_1)
+\tfrac14(\partial_{22}-\partial_1)H_0(e_1).
\]

Applying the chain rule gives precisely

\[
V=\frac\kappa2q(v_*b_{21})b_{23}
-\frac\rho4q(v_*b_{21})b_{21}
+\frac{\kappa^2}4\phi''(v_*b_{21})b_{22}^2.
\]

If `kappa!=0`, the part odd under the single-coordinate sign flip
`b23 -> -b23` is `(kappa/2) q(v_*b21)b23`. The other two terms are
independent of `b23`. The upper product law is invariant under that flip,
`q>0`, and `E b23^2>0`, so this odd part has strictly positive L2 norm.
It cannot cancel the even part.

For `kappa=0`, `E F'=0` since `E q>0`. With

\[
J(s)=E_Z q(\sqrt\tau Z+\alpha\phi(s)),
\qquad F'(s)=q(s)[A+B\alpha J(s)],
\]

both `q` and `J` are even and strictly decreasing in the positive absolute
argument. To check the latter assertion directly, let
`j(r)=E q(sqrt(tau) Z+r)`. Differentiation under the integrable Gaussian
integral is valid because `q'` is bounded. Pairing the positive and negative
integration variables gives, for `r>0`,

\[
j'(r)=\int_0^\infty q'(z)
[\varphi_\tau(z-r)-\varphi_\tau(z+r)]\,dz<0.
\]

Indeed `q'(z)<0` for `z>0`, and the density difference is strictly positive
because `(z-r)^2<(z+r)^2`. Composition with the strictly increasing
`alpha tanh(s)` gives the stated strict decrease of `J(s)` for `s>0`.

For the probability measure `dnu=q dGaussian/Eq`, the identity `E F'=0`
implies `A=-B alpha E_nu J`. Therefore

\[
\rho=B\alpha E[q]\{E_\nu[qJ]-E_\nu[q]E_\nu[J]\}
=B\alpha E[q]\operatorname{Cov}_\nu(q,J)>0.
\]

The final strict sign follows from half the expectation of
`(q(G)-q(G'))(J(G)-J(G'))`: independent nu variables have unequal absolute
values almost surely, and strict comonotonicity makes that product positive.
All variables are bounded, so this covariance computation is justified.
Thus in the `kappa=0` case, `V=-(rho/4)q(v_*b21)b21` is also nonzero.
No sign assumption on `A`, nor positivity assumption on `kappa`, was used.

At initialization `c=0`, hence `d=0`, `w'=0`, `M'=0`, and `c'=2m_epsilon`.
The exact energy identity now gives

\[
-L_\varepsilon'(0)=4\|m_\varepsilon\|_2^2
=4\|V\|_2^2\varepsilon^4+o(\varepsilon^4),\qquad \|V\|_2>0.
\]

This is genuinely `Theta(epsilon^4)` as epsilon tends to zero and excludes
initialized stationarity for every sufficiently small positive epsilon. The
note correctly does not claim this asymptotic argument excludes stationarity
for every epsilon up to one half.

## 4. General opposite-label close pairs

For any of the stated binary data laws, the same physical energy argument
gives `R^2<=t(1-L)<=t`. It bounds the three blocks separately by

\[
\|c\|_2\le\sqrt t,\quad
\|M\|_{op}\le d_*+\sqrt t,\quad
\|w\|_2\le\sqrt3+\sqrt t.
\]

Twice applying the dictionary contraction and using the Lipschitz constant
one of tanh proves

\[
|f_t(v)-f_t(v')|
\le\|c\|_2\|M\|_{op}\|w\|_2|v-v'|
\le h(t)|v-v'|,
\]

with exactly `h(t)=sqrt(t)(d_*+sqrt(t))(sqrt(3)+sqrt(t))`.
For a fixed opposite-label pair, weighted Cauchy–Schwarz gives

\[
|r_i-r_j|^2
\le(p_ir_i^2+p_jr_j^2)(1/p_i+1/p_j)
\le L(1/p_i+1/p_j).
\]

Consequently `L<=ell` forces the stated positive prediction gap
`b_ell=2-sqrt(ell(1/p_i+1/p_j))` when
`0<ell<4p_i p_j/(p_i+p_j)`. This threshold is automatically below one,
since `4p_i p_j/(p_i+p_j)<=p_i+p_j<=1`. Combining the upper and lower
prediction gaps yields `h(t)>=b_ell/delta` at every threshold attainment.
The polynomial in `sqrt(t)` defining `h` is continuous and strictly
increasing from zero to infinity, so its inverse is well defined. A finite
hitting time obeys the same inequality by continuity; infinity obeys it
trivially. Finally `h(t)/t^(3/2)->1`, so

\[
h^{-1}(b_\ell/\delta)\sim(b_\ell/\delta)^{2/3}
\]

for fixed positive masses and fixed allowed `ell`. The asserted
`Omega(delta^-2/3)` lower bound is correct. It asserts neither a matching
upper bound nor finite threshold attainment.

## 5. Potential comparison and the required Dini correction

For a nonnegative finite differentiable trajectory value `Phi(t)` with
`Phi'<=-lambda Phi`, the derivative of `e^(lambda t)Phi(t)` is nonpositive.
The ordinary mean value theorem therefore proves
`Phi(t)<=Phi(0)e^(-lambda t)` on each finite interval. Power domination
gives

\[
L(t)\le C_{dom}\Phi(0)^\alpha e^{-\alpha\lambda t}.
\]

If `tau_ell>=T`, every `t<T` has `L(t)>ell`. Combining these inequalities
and taking `t` up to `T` gives

\[
\Phi(0)\ge(\ell/C_{dom})^{1/\alpha}e^{\lambda T}.
\]

The exponent is `lambda T`, not `alpha lambda T`, after taking the
`alpha`th root. In particular, using the verified symmetric-family delay
with `ell=1-delta` gives, for sufficiently small epsilon,

\[
\Phi_\varepsilon(0)\ge
((1-\delta)/C_{dom})^{1/\alpha}
\exp\!\left(\frac{\lambda_\varepsilon}{C_{delay}\varepsilon^2}\right).
\]

This forces `exp(c epsilon^-2)` necessary initial growth when the rate has
a common positive lower bound and the domination constants are uniform.
The generic close-pair argument gives `exp(c delta^-2/3)` instead. Neither
assertion constructs a potential or establishes a matching upper growth order.

Under the differentiable hypotheses a positive threshold is necessarily
attained in finite time, since the displayed exponential upper bound tends
to zero. Substituting its actual hitting time yields exactly

\[
\lambda\tau_\ell\le\log\Phi(0)
+\frac1\alpha\log(C_{dom}/\ell).
\]

Thus geometry-dependent rate, initial size, and domination constant must
be tracked together. The monotone-transform example is also correct:
`L'=-L^2`, `Phi=exp(-1/L)` gives `Phi'=-Phi` but
`L=1/log(1/Phi)`. An exponential transformed quantity alone gives no power
domination of loss near zero.

**Required minor correction.** In the frozen potential note, lines 69–70
say a Dini derivative version suffices without a continuity hypothesis.
An upper-right Dini inequality by itself does not exclude upward jumps.
For example, with fixed `lambda>0`,

\[
P(t)=\exp[-\lambda(t-\lfloor t\rfloor)],\qquad t\ge0,
\]

has upper-right Dini derivative `D^+P(t)=-lambda P(t)` at every time,
including each nonnegative integer, but `P(n)=1` at every integer rather
than `P(n)<=e^(-lambda n)`. This falsifies the unqualified scalar integration
step. A current-state formulation does not supply continuity of an arbitrary
functional automatically.

It suffices to replace that sentence by: “The same conclusion holds if
`t -> Phi(theta(t))` is continuous and its upper-right Dini derivative
satisfies `D^+Phi(t)<=-lambda Phi(t)` at every time.” To verify this repair,
the continuous function `P(t)=e^(lambda t)Phi(t)` has `D^+P<=0`. If
`P(b)>P(a)`, choose `k=(P(b)-P(a))/(2(b-a))>0`. The continuous function
`P(t)-kt` has its minimum on `[a,b]` at some `t0<b`, because its value at
`b` exceeds its value at `a`. At this minimum its upper-right Dini derivative
is nonnegative, contradicting `D^+(P-kt)<=-k`. Thus `P` is nonincreasing,
and the original exponential comparison follows. Alternatively, local
absolute continuity and the ordinary inequality almost everywhere suffice.
No other correction is required by this review.

## 6. Adversarial and scope conclusions

| Attack | Independent check and outcome |
|---|---|
| Small slope is mistaken for a long delay | The delay uses the full energy and a raw-ball barrier; it does not infer a time scale from the initial derivative. |
| Hidden learning removes cancellation immediately | The second-difference bound holds at every raw-ball state, with the entire evolving matrix and populations. |
| An unproved L2 multiplication estimate controls derivatives | The second derivative explicitly uses bounded dictionary evaluation and an L-infinity/L2 product. |
| Canonical initialization is replaced by fresh independent lower marks | The conditional formula retains the exact joint `(b1,g)` law; both positive bands include the reused-action response term. |
| The leading slope coefficient might vanish | Independent parity and strict covariance arguments cover both possible values of kappa. |
| The examples are coincident or linearly dependent | Every positive epsilon has determinant `2 epsilon^3`; only the excluded limit is coincident. |
| The potential conclusion silently fixes a geometry-dependent rate | The exact constraint displays rate, domination constant, and initial size separately. |
| A discontinuous potential bypasses scalar comparison | This is the one surviving minor flaw in the optional Dini clause; continuity repairs it. |
| A d=2 trained-network result is silently generalized | The argument is an exact d=3 fixed-order closure theorem; no such identification is claimed. |

For the exactly coincident balanced limit, every state has
`L=1+f(v)^2>=1`. At canonical initialization the readout gradient cancels,
and the other two gradients vanish because `c=0`. It is stationary and
cannot satisfy the differentiable finite-potential conditions with positive
rate and power domination. This limit is correctly excluded as a genuine
three-independent-input example.

The strongest surviving behavior is eventual full fitting, possibly with an
exponential terminal rate for each fixed positive epsilon after a long
initial delay. Nothing in the audited proofs excludes it. No positive
asymptotic loss floor, matching hitting-time upper bound, `epsilon^-4`
hitting-time lower bound, fixed-order rotation invariance, or general-d
trained-network identification has been proved or inferred. All assigned
principal obligations are resolved analytically; the single textual Dini
qualification above remains required for a PASS of the complete frozen text.

## 7. Post-repair verification and superseding verdict

**PASS for the revised exact-closure claims within the scope above.** The
required Dini qualification is now present: the trajectory value is continuous,
and its upper-right Dini derivative satisfies the differential inequality at
every time. The added sentence correctly explains that an arbitrary
current-state functional need not supply continuity. The comparison proof in
Section 5 therefore applies, and the sole required correction is resolved.
This verdict supersedes the opening minor-revision verdict for the revised
input only; the original frozen review remains recorded above.

The revised `necessary_potential_growth.md` has SHA-256
`7c1dc0439cdde5c4e2d39edc91dae6e1d177f7e6af1dbb65ce8817b5f2096993`.
Replacing just the repaired passage by the original passage reproduces the
original reviewed SHA-256
`e7e9594ed6f23f233eca1fd763836f7c99bead519f99aee6fee3370e3e732ab7`,
which verifies that this is the sole change. `early_delay.md` remains unchanged
at SHA-256
`33204d4e12dc00a9ef7325a5187637ac9ace52e9787ca5cd3ac60f2a6fc27a71`.

This follow-up checked only the requested local edit and input hashes and
appended this verdict. No other study material, findings, or reviews were read,
and no numerical experiment was performed. PASS is an independent internal
mathematical review outcome, not promotion or general-d network identification.
