# What the initialized nonlinear-gate continuation tests

2026-10-07. Scoped analytical continuation. Scientific inputs read in full:
`PASSIVE_NONLINEARITY_DIAGNOSTICS.md` (SHA-256
`09a4f20f43fbd152471d2ec40be9c00cc67a957a95fad5261dc13fb02a19eb8c`)
and `ANALYTICAL_LEARNING_PROFILES.md` (SHA-256
`a6d454fc98c53de44b5bc989469649dcba671fa0b1717c02dddfa341ba5351a0`).
No other scientific sources, experiments, or global proofs are used.

The proposed continuation exactly preserves the initialized linear and cubic
passive coefficients. It adds upper activation curvature along one frozen
preactivation direction and propagates those features into the readout history.
Its first added output terms are fifth order. At that same order, the true
orbit also receives a contribution from its fourth-order preactivation motion,
which the continuation omits. Thus the useful question is whether activation
curvature along the initial direction explains a measured discrepancy, and
whether the remaining discrepancy comes from displacement amplitude, rotation,
readout history, or the physical clock.

## 1. Finite initialization and its exact local coefficients

Use the sources' two-hidden-layer model, with width \(n\), no biases,
\(v_1=e_1\), \(v_2=e_2\), and \(v_3=(2e_1+e_2)/\sqrt5\):

\[
z_{1,a}=Av_a,\quad h_{1,a}=T(z_{1,a}),\quad
z_{2,a}=Wh_{1,a},\quad h_{2,a}=T(z_{2,a}),\quad
f_a=\langle w,h_{2,a}\rangle_n,
\qquad T=\tanh,\quad \langle x,y\rangle_n=x^\top y/n.
\]

The loss is \(\mathcal L=\frac12\sum_{b=1}^2(y_b-f_b)^2\), with
\(y=Y(1,s)\), \(s=\pm1\), and block mobilities \((n,1,n)\).
There is no passive label. Set \(g=T'\),
\(\lambda_1=2/\sqrt5\), \(\lambda_2=1/\sqrt5\).
All activations and their derivatives act componentwise.

Fix one initialization \(A(0),G=W(0),w(0)=0\). Define

\[
X_a=A(0)v_a,\quad H_a=T(X_a),\quad Z_a=GH_a,\quad
h_{2,a}^0=T(Z_a),\quad Q=h_{2,1}^0+s h_{2,2}^0.
\]

The auxiliary residual-free orbit has derivative \(d/du\), not physical-time
derivative. With \(\ell=(1,s)\), its equations are

\[
\begin{aligned}
A'&=\sum_{b=1}^2\ell_b
 [g(z_{1,b})\odot W^\top(g(z_{2,b})\odot w)]v_b^\top,\\
W'&=\frac1n\sum_{b=1}^2\ell_b
 [g(z_{2,b})\odot w]h_{1,b}^\top,\\
w'&=h_{2,1}+s h_{2,2}.
\end{aligned}
\tag{1}
\]

These are the physical gradient equations with residuals replaced by
\((1,s)\). This finite-dimensional orbit is well defined locally even when
the finite physical trajectory does not remain in that residual mode.

At initialization \(A'=W'=0\) and \(w'=Q\). Consequently, writing
\(S_{ab}=v_a^\top v_b\) and \(C^1_{ab}(0)=\langle H_a,H_b\rangle_n\),

\[
\begin{aligned}
A''(0)&=\sum_{b=1}^2\ell_b
 [g(X_b)\odot G^\top(g(Z_b)\odot Q)]v_b^\top,\\
W''(0)&=\frac1n\sum_{b=1}^2\ell_b
 [g(Z_b)\odot Q]H_b^\top,\\
J_{1,a}:=h_{1,a}''(0)
 &=g(X_a)\odot\sum_{b=1}^2\ell_b S_{ab}
 [g(X_b)\odot G^\top(g(Z_b)\odot Q)],\\
L_a:=z_{2,a}''(0)
 &=\sum_{b=1}^2\ell_b C^1_{ab}(0)
 [g(Z_b)\odot Q]+GJ_{1,a},\\
J_{2,a}:=h_{2,a}''(0)&=g(Z_a)\odot L_a.
\end{aligned}
\tag{2}
\]

For example, differentiating \(z_{2,a}=Wh_{1,a}\) twice leaves
\(W''(0)H_a+GJ_{1,a}\); its cross term vanishes because both initial
velocities vanish. Differentiating the activation leaves \(g(Z_a)L_a\)
for the same reason. Thus (2) contains no unknown evolved state or fitted
coefficient, and its factors agree with the proposal.

The initialized continuation is

\[
\widehat h_{2,a}(u)=T(Z_a+u^2L_a/2),\qquad
\widehat w(u)=\int_0^u
 [\widehat h_{2,1}(v)+s\widehat h_{2,2}(v)]\,dv.
\tag{3}
\]

Define, with all vectors in the same upper population,

\[
\begin{aligned}
R&=J_{2,1}+sJ_{2,2},\\
q_2^0&=h_{2,3}^0-\lambda_1h_{2,1}^0-\lambda_2h_{2,2}^0,\\
q_J&=J_{2,3}-\lambda_1J_{2,1}-\lambda_2J_{2,2},\\
\widehat q_2(u)&=\widehat h_{2,3}(u)
 -\lambda_1\widehat h_{2,1}(u)-\lambda_2\widehat h_{2,2}(u).
\end{aligned}
\]

Taylor expansion and integration of (3) give

\[
\widehat h_{2,a}=h_{2,a}^0+\frac{u^2}{2}J_{2,a}+O(u^4),\qquad
\widehat w=uQ+\frac{u^3}{6}R+O(u^5).
\]

Therefore the exact finite-initialization coefficients of
\(\widehat\varepsilon_n(u)=\langle\widehat w,\widehat q_2\rangle_n\)
are

\[
\begin{aligned}
e_{1,n}&=\langle Q,q_2^0\rangle_n,\\
e_{3,n}&=\frac12\langle Q,q_J\rangle_n
       +\frac16\langle R,q_2^0\rangle_n,\\
\widehat\varepsilon_n(u)&=e_{1,n}u+e_{3,n}u^3+O(u^5).
\end{aligned}
\tag{4}
\]

The \(1/2\) coefficient comes from the current feature; \(1/6\) comes
from features accumulated in the readout. Neither contraction can generally
be replaced by the other for the passive input.

For direct finite coefficient checks, the individual auxiliary outputs have

\[
\begin{aligned}
\langle\widehat w,\widehat h_{2,a}\rangle_n
 &=k_{a,n}u+p_{a,n}u^3+O(u^5),\\
k_{a,n}&=\langle Q,h_{2,a}^0\rangle_n,\qquad
p_{a,n}=\tfrac12\langle Q,J_{2,a}\rangle_n
 +\tfrac16\langle R,h_{2,a}^0\rangle_n.
\end{aligned}
\tag{5}
\]

In particular, the trained mode \((f_1+s f_2)/2\) has coefficients

\[
\nu_n=\frac12\|Q\|_n^2,\qquad
\kappa_n=\frac13\langle Q,R\rangle_n
 =\frac13\left(\frac{\|A''(0)\|_F^2}{n}
                     +\|W''(0)\|_F^2\right)\ge0.
\tag{6}
\]

For the last equality, insert (2) into
\(\langle Q,R\rangle_n=\sum_a\ell_a
\langle g(Z_a)\odot Q,L_a\rangle_n\).
The learned-middle terms give \(\|W''(0)\|_F^2\); adjointness of
\(G,G^\top\) and \(S_{ab}=v_a^\top v_b\) turns the remaining terms
into \(\|A''(0)\|_F^2/n\). This checks the normalization and sign
without using population symmetry.

## 2. Cubic matching and the two distinct polynomial controls

In the population symmetry used by the source notes, let
\(F_3(u)=\nu u+\kappa u^3\) and
\(\lambda_s=(2+s)/\sqrt5\). The existing proposed physical clock is

\[
\dot u=Y-F_3(u),\qquad u(0)=0.
\tag{7}
\]

Here \(\nu=0.236450410504\), \(\kappa=0.181152636696\) are the
source's initialized population coefficients. Its passive cubic polynomial is
\(\lambda_sF_3(u)+e_1u+e_3u^3\), where

| Sign \(s\) | \(e_1\) | \(e_3\) |
|---|---:|---:|
| \(-1\) | \(0.003487192962\) | \(0.022445179955\) |
| \(+1\) | \(-0.013396124315\) | \(-0.059647423345\) |

These numbers are inherited input values, not recomputed numerical evidence.
With the corresponding joint population law in (3), (4) gives these
coefficients and \(\widehat f_3=\lambda_sF_3+\widehat\varepsilon\)
matches the source's passive cubic expansion.

A finite realization has different coefficients \(e_{1,n},e_{3,n}\).
Two fair comparisons are available, and their provenance should remain clear:

1. Compare the raw finite continuation with its own cubic control
   \(e_{1,n}u+e_{3,n}u^3\), using exactly the same realization and clock.
2. To retain the population cubic predictor, define the initialized remainder
   \(r_n(u)=\widehat\varepsilon_n(u)-e_{1,n}u-e_{3,n}u^3\) and use
   \[
   \widehat f_3^{\rm match}(u)
   =\lambda_sF_3(u)+e_1u+e_3u^3+r_n(u).
   \tag{8}
   \]

Equation (8) matches the population linear and cubic terms by construction;
all added terms still come from initialization. It corrects the first two
finite coefficient fluctuations, not the entire finite-width physical
trajectory or its higher-order fluctuations. Comparing the raw finite
continuation directly with the population cubic polynomial would confound
these coefficient fluctuations with the proposed nonlinear correction.

There is a second, useful control that is distinct from the cubic polynomial.
Linearize the activation in the displacement while preserving the readout
integral:

\[
h_{2,a}^{\rm lin}(u)=h_{2,a}^0+\frac{u^2}{2}J_{2,a},\qquad
w^{\rm lin}(u)=uQ+\frac{u^3}{6}R.
\]

Its defect is exactly

\[
\varepsilon_n^{\rm lin}(u)
=e_{1,n}u+e_{3,n}u^3
 +\frac{u^5}{12}\langle R,q_J\rangle_n.
\tag{9}
\]

Thus the difference from a cubic output polynomial includes a readout-feature
product even without further activation curvature. Comparing (3) with (9)
isolates nonlinear activation along the frozen preactivation direction more
specifically. A population-coefficient matched version of this control adds
the same fifth-order term to the population passive cubic polynomial.

## 3. Which fifth-order mechanism is retained and which is missing

Set \(B_a=T''(Z_a)\odot L_a^{\odot2}\), where the square is componentwise,
and \(q_B=B_3-\lambda_1B_1-\lambda_2B_2\). The continued feature has
quartic term \(u^4B_a/8\), and the readout has fifth-order term
\(u^5(B_1+sB_2)/40\). Hence

\[
\widehat e_{5,n}
=\frac18\langle Q,q_B\rangle_n
 +\frac1{12}\langle R,q_J\rangle_n
 +\frac1{40}\langle B_1+sB_2,q_2^0\rangle_n.
\tag{10}
\]

The middle term is already present in (9). The first and last terms are
upper activation curvature in the current feature and in readout history.

Along the true auxiliary orbit (1), hidden fields are even in \(u\) and
the readout is odd: replacing \(u\) by \(-u\) and \(w\) by \(-w\)
preserves (1) and its initial data. If
\(N_a=z_{2,a}^{(4)}(0)\), its local preactivation expansion is

\[
z_{2,a}(u)=Z_a+\frac{u^2}{2}L_a+\frac{u^4}{24}N_a+O(u^6).
\]

Relative to (10), the true fifth-order defect coefficient additionally
contains

\[
\frac1{24}\left\langle Q,
 g(Z_3)\odot N_3-\sum_{a=1}^2\lambda_a g(Z_a)\odot N_a
\right\rangle_n
 +\frac1{120}\left\langle
 g(Z_1)\odot N_1+s g(Z_2)\odot N_2,q_2^0
\right\rangle_n.
\tag{11}
\]

This follows by expanding the activation once more and integrating its
training combination. The continuation sets this fourth-order preactivation
motion to zero; it does not calculate it. Computing \(N_a\) is unnecessary
for the proposed controlled comparison. Formula (11) identifies precisely why
matching the cubic coefficients does not imply matching the first omitted
coefficient, and why a failed continuation need not refute the role of upper
activation curvature.

Equations (2), (4)--(6), and (9)--(11) are local finite-dimensional algebra.
An expectation version requires the joint initialization law and the moments
needed by those contractions. The two allowed sources provide an initialization
program, not a proved constant-storage population evaluation of that joint law.
No finite-time accuracy claim is inferred from these local formulas.

## 4. Displacement amplitude and rotation are separate diagnostics

For an actual finite physical trajectory, record its residuals
\(c_b(t)=y_b-f_b(t)\) and define the measured coordinates

\[
c_+(t)=\frac{c_1+s c_2}{2},\qquad
c_-(t)=\frac{c_1-s c_2}{2},\qquad
u_{\rm obs}(t)=\int_0^t c_+(\tau)\,d\tau.
\tag{12}
\]

This measured coordinate is a diagnostic; a prediction still solves (7).
Finite \(c_-\) drives the second vector field in
\(\dot\theta=c_+V_++c_-V_-\), where \(V_\pm\) are the physical
gradient fields with residuals replaced by \((1,\pm s)\).
Consequently substitution of \(u_{\rm obs}\) does not make a generic
finite physical trajectory an exact solution of (1).

At a recorded time, write \(u=u_{\rm obs}(t)\) and

\[
d_a=z_{2,a}(t)-Z_a,\qquad \widehat d_a=u^2L_a/2.
\]

For \(\|L_a\|_n>0\), resolve the actual displacement along the initial
preactivation direction:

\[
\begin{aligned}
\alpha_a(t)&=\frac{\langle L_a,d_a\rangle_n}{\|L_a\|_n^2},\\
d_{a,\perp}&=d_a-\alpha_aL_a,\\
\|d_a-\widehat d_a\|_n^2
 &=\left(\alpha_a-\frac{u^2}{2}\right)^2\|L_a\|_n^2
   +\|d_{a,\perp}\|_n^2.
\end{aligned}
\tag{13}
\]

The first term is displacement-amplitude error, the second motion outside
the initialized direction. Report both absolute RMS terms for all three
inputs. Ratios such as \(2\alpha_a/u^2\) or
\(\|d_{a,\perp}\|_n/\|d_a\|_n\) are useful only away from zero
denominators. If \(L_a=0\), report the full \(d_a\) as unexplained
displacement. At initialization, report zero absolute discrepancies and
leave directional ratios undefined.

Feature-space tangent diagnostics answer a different question. For
\(\|J_{2,a}\|_n>0\), decompose

\[
h_{2,a}(t)-h_{2,a}^0
=\frac{\langle J_{2,a},h_{2,a}(t)-h_{2,a}^0\rangle_n}
        {\|J_{2,a}\|_n^2}J_{2,a}
 +\Delta h_{2,a,\perp}.
\tag{14}
\]

Perform the same decomposition on \(\widehat h_{2,a}(u)-h_{2,a}^0\).
Even an exact frozen preactivation direction can create a feature displacement
orthogonal to \(J_{2,a}\). Indeed, with \(\tau=u^2/2\), its feature
tangent is \(g(Z_a+\tau L_a)\odot L_a\), which changes direction as
different neurons' gates change. Thus feature-space rotation alone does not
demonstrate a wrong preactivation direction. Compare it with the rotation
already predicted by (3), and use (13) to test preactivation rotation itself.

## 5. Exact error splitting at the same actual readout

For this section all predictions are evaluated at the chosen same coordinate
\(u=u_{\rm obs}(t)\). Define
\(q_2(t)=h_{2,3}(t)-\sum_a\lambda_a h_{2,a}(t)\) and
\(q_2^{\rm lin}(u)=q_2^0+u^2q_J/2\).
The actual passive defect is \(\varepsilon(t)=\langle w(t),q_2(t)\rangle_n\).

The comparison that holds the readout fixed is the exact identity

\[
\begin{aligned}
\varepsilon(t)-\langle w(t),q_2^{\rm lin}(u)\rangle_n
={}&\underbrace{\langle w(t),q_2(t)-\widehat q_2(u)\rangle_n}
              _{\text{wrong preactivation displacement}}\\
 &+\underbrace{\langle w(t),\widehat q_2(u)-q_2^{\rm lin}(u)\rangle_n}
              _{\text{activation curvature along the predicted displacement}}.
\end{aligned}
\tag{15}
\]

The second term tests whether the frozen-direction nonlinear activation
actually changes the feature component read by the trained network.
The first tests what remains after allowing that nonlinear activation.
These are signed current-state diagnostics, not differences of separately
trained models. Their order fixes a particular additive decomposition;
changing the comparison path would produce a different attribution.

The first term can be resolved into the two errors in (13) without
linearizing the activation. Define the componentwise secant

\[
\Gamma_a^{\rm err}
=\int_0^1 g\bigl(Z_a+\widehat d_a+\rho(d_a-\widehat d_a)\bigr)\,d\rho.
\]

Then

\[
h_{2,a}(t)-\widehat h_{2,a}(u)
=\Gamma_a^{\rm err}\odot
 \left[\left(\alpha_a-\frac{u^2}{2}\right)L_a+d_{a,\perp}\right].
\tag{16}
\]

Apply the passive combination with coefficients
\((-\lambda_1,-\lambda_2,1)\) and project both terms against the same
actual \(w(t)\). This gives exact signed amplitude and transverse
contributions to the first term of (15). Use the same secant in both terms;
it remains defined when the two preactivations coincide. RMS displacement
and its readout projection should both be retained: saturated coordinates
can have large displacement with a weak output effect, while smaller
displacements can align strongly with the readout.

The continuation also approximates the readout. Its total raw defect error
splits exactly as

\[
\varepsilon(t)-\widehat\varepsilon_n(u)
=\langle w(t),q_2(t)-\widehat q_2(u)\rangle_n
 +\langle w(t)-\widehat w(u),\widehat q_2(u)\rangle_n.
\tag{17}
\]

The second term need not be small merely because the current feature
displacement is accurate: the readout accumulates previous feature errors.
More precisely, let \(Q(t)=h_{2,1}(t)+s h_{2,2}(t)\) and
\(\widehat Q(u)=\widehat h_{2,1}(u)+s\widehat h_{2,2}(u)\). Directly
integrating \(\dot w=c_+Q+c_-(h_{2,1}-s h_{2,2})\) gives

\[
\begin{aligned}
w(t)-\widehat w(u_{\rm obs}(t))
={}&\int_0^t c_+(\tau)
 [Q(\tau)-\widehat Q(u_{\rm obs}(\tau))]\,d\tau\\
 &+\int_0^t c_-(\tau)[h_{2,1}(\tau)-s h_{2,2}(\tau)]\,d\tau.
\end{aligned}
\tag{18}
\]

No division by a residual or monotonicity of the observed clock is needed.
The terms distinguish accumulated feature-history error and excitation
of the other finite-width residual mode.

For the uncorrected predictor \(\widehat f_3=\lambda_sF_3+
\widehat\varepsilon_n\), the remaining output bookkeeping is

\[
\begin{aligned}
f_3(t)-\widehat f_3(u)
={}&\lambda_1f_1(t)+\lambda_2f_2(t)-\lambda_sF_3(u)\\
 &+\varepsilon(t)-\widehat\varepsilon_n(u).
\end{aligned}
\tag{19}
\]

For the matched predictor (8), subtract the explicit coefficient correction
\((e_1-e_{1,n})u+(e_3-e_{3,n})u^3\) from the right-hand side of (19).
Finally, if \(u_{\rm pred}\) solves (7),

\[
f_3(t)-\widehat f_3(u_{\rm pred}(t))
=[f_3(t)-\widehat f_3(u_{\rm obs}(t))]
 +[\widehat f_3(u_{\rm obs}(t))-
   \widehat f_3(u_{\rm pred}(t))].
\tag{20}
\]

This separates the measured-clock substitution from the remaining
same-coordinate discrepancy. The same identity holds for the matched
predictor. It does not convert a measured clock into a predictive input.

## 6. Mechanistic reading of the authorized comparison

The useful comparison keeps initialization, physical clock, sample sign,
and finite coefficient matching identical. Compare the cubic output,
the quadratic-feature/readout product (9), and the nonlinear continuation
(3), and then examine (13)--(20) on the full trajectory.

If (3) improves on (9), and the second term in (15) accounts for the observed
feature correction, that supports upper activation curvature along the
initialized direction as a useful mechanism. If (13) has mainly parallel
error, the frozen direction may remain informative while its \(u^2/2\)
amplitude law is inadequate. If the transverse contribution in (16) is
large, the initial direction is missing consequential feature motion.
If the first term of (17) is small but the second is large, current passive
geometry alone misses the accumulated readout history. A large \(c_-\)
limits interpretation through a single population residual mode.

Improvement over a cubic polynomial alone does not distinguish activation
curvature from the fifth-order product in (9). Failure to improve does not
show that gates are irrelevant: the omitted displacement motion (11), its
readout history, or a signed cancellation can dominate. The continuation
retains nonlinear gate evaluation along a frozen displacement; it does not
advance the full causal feature-response state. These alternatives are
resolvable by the stated diagnostics without reopening global proof work.

Status: the finite-initialization coefficients and error splits above are
derived identities/local expansions. Moderate-amplitude predictive accuracy
is untested in this note. The supervisor owns the authorized experiment and
the study README; this scoped contribution changes only this file.
