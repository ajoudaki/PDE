# Uniform fitting and an explicit inactive top threshold

2026-10-01. Coordinator derivation. This is a result for a specified modified q=1 closure, not the ordinary dense gradient flow. The proof below is deterministic on an initialized operator/feature-Gram event. It does not prove a width-to-population rate.

## Exact model and reconciliation

Use two hidden tanh layers, m fixed samples, width n, inputs x_a in R^d, and u_a=x_a/sqrt(d). Let X=max_a ||u_a||. Set

\[
h_a=\tanh(Au_a),\quad B=W_0+\frac1{mn}\sum_a v_a k_a^T,
\quad z_a=Bh_a,\quad g_a=\tanh(z_a),\quad f_a=w^Tg_a/n.
\]

B is a derived action, never an independently trained matrix. From `paper/main.tex` equations (old-ode) and (old-recon), at q=1 exactly

\[
k_a=\bar h_{a,0}/\tau,\qquad v_a=-2\bar\delta_{a,0}.
\]

Thus k_a(0)=h_a(0), v_a(0)=0, w(0)=0, tau(0)=1, and the original q=1 equations have the normalizations below. A_0 has independent N(0,1) entries and W_0 independent N(0,1/n) entries when a probabilistic initialization is used. The proof itself only uses the event specified later.

For M>=0 let C_M be coordinatewise clipping to [-M,M]. Define recursive **post-gate** clipping:

\[
d_a=C_M(w\odot\operatorname{sech}^2z_a),\qquad
\ell_a=C_M(\operatorname{sech}^2(Au_a)\odot B^Td_a).
\]

The clipped d_a is used in the true transpose action B^T. Residuals are outside the clipping maps. With r_a=f_a-y_a and rho=(m^{-1}sum_a r_a^2)^{1/2}, the autonomous equations are

\[
\dot w=-\frac2m\sum_a r_ag_a,\quad
\dot A=-\frac2m\sum_a r_a\ell_a u_a^T,\quad
\dot v_a=-2r_ad_a,\quad
\dot k_a=\frac\rho\tau(h_a-k_a),\quad \dot\tau=\rho.
\]

This is the sole model in this note. M=0 is included in deterministic bounds but is excluded as an answer to a question requiring feature learning. Labels are arbitrary fixed real values with sufficiently small RMS Y; unit labels are not automatically covered.

## Theorem

Assume ||W_0||op<=K_0 and the initial readout feature Gram

\[
\Gamma_w(0)=G(0)^TG(0)/(mn)\succeq\lambda I_m,
\qquad G=[g_1,\ldots,g_m],\quad \lambda>0.
\]

Define

\[
D=K_0+2,\quad C_h=8+4X^2D^2,\quad
s_* = \min\{1,\sqrt{\lambda/(4C_h)}\}.
\]

If Y<=lambda s_*/2, then for every fixed M>=0 the above closure has a unique global solution, convergent A,w,v,k,tau, and

\[
\rho(t)\le Y e^{-\lambda t},\qquad
S(t):=\int_0^t\rho(s)\,ds\le Y/\lambda.
\]

All training examples interpolate at the limiting endpoint. Constants and the label restriction are independent of width and M. The threshold

\[
M\ge M_{\rm top}:=2Y/\lambda
\]

ensures that the top d_a clipping is never active. In particular M=1 suffices for top inactivity under the displayed label restriction. No corresponding conclusion is made about the lower ell_a clipping.

## Proof

The vector field is locally Lipschitz for tau>0, including at zero residual, and tau>=1. Work first on a maximal local solution stopped at S=s_*.

The key equation integrates exactly to

\[
k_a(t)=\frac{h_a(0)+\int_0^t\rho(s)h_a(s)\,ds}{1+S(t)},
\]

so every key coordinate has magnitude at most one. Since |g_ai|<=1 and m^{-1}sum_a|r_a|<=rho,

\[
\|w(t)\|_\infty\le2S(t),\qquad
\|d_a(t)\|_\infty\le2S(t).
\]

Consequently

\[
\|v_a(t)\|_\infty\le4\int_0^t |r_a(s)|S(s)\,ds
\le2\sqrt m S(t)^2,
\qquad
\frac1m\sum_a\|v_a(t)\|_\infty\le2S(t)^2.
\]

The rank-one identity ||v k^T/n||F=(||v||2/sqrt(n))(||k||2/sqrt(n)) gives

\[
\|B-W_0\|_F\le2S^2,\qquad \|B\|_{op}\le D
\]

while S<=1. Clipping decreases absolute values, so

\[
\frac{\|\ell_a\|_2}{\sqrt n}\le
\|B\|_{op}\frac{\|d_a\|_2}{\sqrt n}\le2DS,
\qquad
\frac{\|\dot A\|_F}{\sqrt n}\le4XD S\rho.
\]

Thus ||dot h_a||2/sqrt(n)<=4X^2D S rho. Also ||dot k_a||2/sqrt(n)<=2rho/tau. Differentiate the derived B directly to obtain

\[
\begin{aligned}
\|\dot B\|_F
&\le \frac1m\sum_a\left[
\frac{\|\dot v_a\|_2\|k_a\|_2}{n}
+\frac{\|v_a\|_2\|\dot k_a\|_2}{n}\right]\\
&\le4S\rho+4S^2\rho/\tau\le8S\rho.
\end{aligned}
\]

Both tanh maps are 1-Lipschitz. Their chain rule along the absolutely continuous trajectory and the preceding bounds give

\[
\max_a\frac{\|\dot g_a\|_2}{\sqrt n}
\le (8+4X^2D^2)S\rho=C_h S\rho.
\]

Integrating and using dot S=rho gives ||G(t)-G(0)||F/sqrt(mn)<=C_h S^2/2. Since ||G||op/sqrt(mn)<=1, subtraction of the two Gram products yields

\[
\|\Gamma_w(t)-\Gamma_w(0)\|_{op}\le C_h S^2.
\]

No positive-semidefinite full backpropagation Gram is asserted for this clipped system. Instead differentiate the prediction using the unchanged readout equation:

\[
\dot r=-2\Gamma_w r+e,\qquad e_a=w^T\dot g_a/n,
\qquad \|e\|_m\le2C_h S^2\rho.
\]

It follows, at positive rho, that

\[
\dot\rho\le[-2\lambda+4C_h S^2]\rho\le-\lambda\rho.
\]

The inequality also holds in the upper-derivative sense at zero. In fact zero residual is an equilibrium of the entire state equation, so there is no ambiguity there. Hence rho<=Y exp(-lambda t), and S<=Y/lambda<=s_*/2. This excludes the activity stop strictly.

The bounds above keep every finite-dimensional coordinate bounded on a finite time interval, tau away from zero, and every velocity integrable over [0,infinity). For individual sample v_a use |r_a|<=sqrt(m)rho; for k_a use ||dot k_a||<=2sqrt(n)rho. Therefore no finite maximal endpoint occurs and all state blocks converge. Continuity of prediction and rho->0 prove interpolation. If Y=0 the entire state is stationary.

Finally |w_i sech^2 z_ai|<=|w_i|<=2Y/lambda. Thus M>=2Y/lambda never clips d_a. This says nothing about B^Td_a, which contains a reused Gaussian transpose action. The theorem is proved.

## Why fixed clipping gives a genuine stability simplification

For g(z)=sech^2 z, |g'|<=2g. For each fixed p, the absolutely continuous map z->C_M(p g(z)) has derivative bounded by 2M almost everywhere: outside saturation |p|g<=M; inside saturation its derivative vanishes. Its p-Lipschitz constant is at most one. Therefore

\[
|C_M(p g(z))-C_M(p' g(z'))|
\le |p-p'|+2M|z-z'|.
\]

This provides a width-independent Lipschitz constant at both backward layers. It is special to activations whose gate has an appropriate relative derivative bound; it is not an assertion for every activation with merely bounded Lipschitz derivative.

These deterministic estimates do not construct an iid particle coupling, bound the finite-width mean's population bias, or prove a root-width population prediction theorem. Those obligations are addressed separately in the route notes.

## Check status and sources

The coordinator derived the proof from the current manuscript definitions and the readout-Gram method, then supplied it to the fresh threshold and concentration routes. The threshold route independently checked the inequalities and sharpened the sample-average v bound to the factor 2S^2 used above. The concentration route uses the same readout-dominance mechanism. These checks are internal and not promotion review.

Scientific inputs: `paper/main.tex`, Setting and old-clock/old-ode/old-recon definitions; `paper/proof_alltime.tex`, initialized Gram and original fitting proof; `docs/notation.qmd`. No other study is a proof dependency. No experiment was run.
