# Width-rate obstruction with exact zero readout

Status: internally derived mathematical route, not independently reviewed or promoted. This is a scoped route, not a proof of a width upper bound for general nonlinear activations. Inputs are `paper/results.tex`, `paper/proof_tracking.tex`, `paper/proof_alltime.tex`, and the setting in `paper/main.tex`. No other study inputs or experiments were used.

The first independent result was derived before discussion: an orthogonal unused Gaussian first-layer column gives a conditional Gaussian trained test prediction; the two-hidden-layer case additionally admits an unconditional all-time root-mean-square bound through elementary deep-linear invariants. A subsequent supervisor message independently supplied the same unused-column construction and the conditional total-variation bound; the common-event general-depth formulation below records that shared observation.

## Contract and conclusion

Keep the paper's exact canonical mobilities, independent Gaussian initialization, fixed depth, fixed nonzero small label, and exactly zero initial readout. Take identity activation in every layer, which satisfies the theorem's bounded and Lipschitz derivative assumptions. This is an admissible special case used to obstruct a universal faster prediction rate. It is not substituted for the intended nonlinear upper-bound problem.

For every fixed depth, a one-input linear training problem has all-time test discrepancy of order `n^{-1/2}` in probability. For two hidden layers the same example has unconditional all-time RMS discrepancy bounded above and below by positive constants times `n^{-1/2}`. Thus a universal `n^{-1}` RMS or `O_P(n^{-1})` rate for the paper's population-prediction remainder is false. This does not obstruct `n^{-1}` mean *squared* error, or an `n^{-1}` rate for the distinct closure-to-dense tracking remainder.

## Exact unused-column identity, all fixed depths

Take `d=2`, `m=1`, training input `x_1=sqrt(2)e_1`, label `y>0`, and test input `x_*=sqrt(2)e_2`. The label can be any fixed sufficiently small positive value. Write

\[
a(t)=W^{(1)}(t)e_1,\qquad \beta=W^{(1)}(0)e_2,
\qquad k(t)=(W^{(2)}(t))^\top\cdots(W^{(L)}(t))^\top w(t).
\]

Only the first column of the first matrix is updated. Consequently the full training path, including `a` and `k`, is measurable with respect to the initial first column and the hidden matrices, while `beta ~ N(0,I_n)` remains independent of that path. Exactly,

\[
f_n(t,x_1)=\frac{k(t)^\top a(t)}n,
\qquad f_n(t,x_*)=\frac{k(t)^\top\beta}n,
\qquad k(0)=0.
\tag{1}
\]

The initialization Gram limit is `1`, so the required positive gap holds. Let `E_n` be a training-measurable event on which the paper's fitting, parameter, and speed bounds hold for this linear training path. Such events have probability tending to one: the theorem's original good event implies those training-only path properties, so taking the event defined by the properties themselves removes any dependence on `beta`. On `E_n`, for fixed constants independent of width,

\[
f_n(\infty,x_1)=y,\quad
\sup_t\frac{\|a(t)\|}{\sqrt n}\le C,
\quad \sup_t\frac{\|k(t)\|}{\sqrt n}\le Cy,
\quad \frac1{\sqrt n}\int_0^\infty\|\dot k(t)\|\,dt\le Cy.
\tag{2}
\]

For the last bound differentiate the finite product defining `k`. The readout derivative has normalized norm at most `C rho`; every hidden derivative has operator norm at most `Cy rho`, the other hidden operators are bounded, and the readout normalized norm is at most `Cy`. The sum of the fixed number of product terms is at most `C rho`; integrate the paper's `int rho <= Cy`. This uses constant gates; it does not make an analogous claim for nonlinear gate derivatives.

Cauchy--Schwarz in the fitted training identity gives

\[
\frac{\|k(\infty)\|}{\sqrt n}\ge \frac yC.
\tag{3}
\]

Conditionally on the training path, the endpoint test prediction is exactly centered Gaussian with variance `||k(infinity)||^2/n^2`. Therefore, on `E_n`, its conditional standard deviation lies between `cy/sqrt(n)` and `Cy/sqrt(n)`.

The entire test path has the conditional estimate

\[
\begin{aligned}
\left(\mathbb E_\beta\sup_{t\ge0}|f_n(t,x_*)|^2\right)^{1/2}
&\le \frac1n\int_0^\infty
      \left(\mathbb E_\beta|\beta^\top\dot k(t)|^2\right)^{1/2}dt\\
&=\frac1n\int_0^\infty\|\dot k(t)\|\,dt
\le \frac{Cy}{\sqrt n}.
\end{aligned}
\tag{4}
\]

The first inequality is the integral triangle inequality in `L^2(beta)` after bounding each partial integral by the integral of the absolute integrand. The equality is the Gaussian covariance identity. Thus the all-time test error is `O_P(n^{-1/2})`. Its population limit is the zero test trajectory. Conversely (3) and the conditional Gaussian law give constants `c_0,p_0>0` such that

\[
\liminf_{n\to\infty}\Pr\!\left\{
\sup_{t\ge0}|f_n(t,x_*)-f_\infty(t,x_*)|\ge c_0 n^{-1/2}
\right\}\ge p_0.
\tag{5}
\]

This rules out `o_P(n^{-1/2})` and hence `O_P(n^{-1})`. Equations (2)--(4) alone give a mean-square upper bound on `E_n`, not unconditionally: the exceptional event must not be silently discarded when claiming an expectation bound.

For the uniform measure on the radius-`sqrt(2)` circle, the fitted linear predictor is exactly `y cos(theta) + Z_n sin(theta)`, where `Z_n=f_n(infinity,x_*)`. Its population endpoint is `y cos(theta)`, and its circle RMS discrepancy is `|Z_n|/sqrt(2)`. The same obstruction therefore holds on an entire compact input domain, not only for a point-mass test law.

## Unconditional sharp all-time RMS for two hidden layers

Here `L=2`. Set

\[
u=a/\sqrt n,\quad v=w/\sqrt n,\quad A=W^{(2)},
\quad z=\beta/\sqrt n,\quad f=v^\top Au.
\]

Then `u(0) ~ N(0,I_n/n)`, the entries of `A(0)=A_0` are independent `N(0,1/n)`, `v(0)=0`, and the passive vector `z ~ N(0,I_n/n)` is independent. Canonical training gives

\[
\dot u=2(y-f)A^\top v,\qquad
\dot A=2(y-f)vu^\top,\qquad
\dot v=2(y-f)Au.
\tag{6}
\]

Use the increasing activity parameter `s(t)=2 int_0^t(y-f(r)) dr`. Before interpolation the residual is positive, since

\[
\dot f=2(y-f)K,\quad
K=\|Au\|^2+\|A^\top v\|^2+\|u\|^2\|v\|^2\ge0,
\quad y-f(t)=y\exp\!\left(-2\int_0^tK\right).
\tag{7}
\]

In `s` time, (6) is `u'=A^T v`, `A'=v u^T`, `v'=Au`. Differentiation gives exact invariants

\[
AA^\top-vv^\top=A_0A_0^\top,
\qquad \|u\|^2-\|v\|^2=\|u_0\|^2.
\tag{8}
\]

Let `b=||v||^2` and `r=||u_0||^2`. Then `b'=2f`, and

\[
\|A^\top v\|^2
=v^\top A_0A_0^\top v+b^2\ge b^2,
\qquad f'=K\ge b^2.
\]

Consequently `(f^2-b^3/3)'=2f(K-b^2)>=0`, starting from zero. While `0<=f<=y`,

\[
b\le B:=(3y^2)^{1/3},\qquad
\|u\|^2\le r+B,\qquad
\|A\|_{\rm op}^2\le\|A_0\|_{\rm op}^2+B.
\tag{9}
\]

These bounds prevent finite-time blowup. They also imply `K>=sigma_min(A_0)^2 r>0` almost surely, because `AA^T>=A_0A_0^T` and a square Gaussian `A_0` is nonsingular almost surely. Therefore the residual decays exponentially, with a sample-dependent positive rate, and all three factors converge as `t->infinity`. In particular `f(infinity)=y`.

Write `k=A^T v` in normalized coordinates. The exact conditional endpoint variance is `||k(infinity)||^2/n`. Its lower and upper bounds from (8)--(9) are

\[
\frac{y^2}{r+B}\le \|k(\infty)\|^2
\le B\|A_0\|_{\rm op}^2+B^2.
\tag{10}
\]

The lower bound uses `y=k(infinity)^T u(infinity)`. Since `E r=1`, Jensen's inequality yields

\[
\mathbb E|f_n(\infty,x_*)|^2
\ge \frac{y^2}{n(1+B)}.
\tag{11}
\]

For an all-time upper bound, one needs a bound on the length of `k`, not just its norm. Let `q=||A_0u_0||^2>0`. Use an SVD of `A_0` to rotate `u,v,A`; paired sign changes make the rotated `u_0` coordinatewise nonnegative while leaving the initial middle matrix diagonal and nonnegative. The rotated `v_0` is zero. The `s`-time differential equations preserve nonnegativity and make all coordinates nondecreasing. In particular `||Au||^2>=q` throughout the path. Hence `f'=K>=q` and

\[
s(\infty)\le y/q.
\]

This is an exact structural argument for a single middle matrix; it is not asserted for several independent middle matrices. Differentiating `k` in `s` and applying (9) gives

\[
k'=b u+A^\top A u,\qquad
\int_0^\infty\|\dot k(t)\|\,dt
\le\frac yq\bigl(\|A_0\|_{\rm op}^2+2B\bigr)\sqrt{r+B}.
\tag{12}
\]

Conditional Gaussian integration as in (4) now proves

\[
\mathbb E\sup_{t\ge0}|f_n(t,x_*)|^2
\le \frac{y^2}{n}\,
\mathbb E\!\left[
q^{-2}(\|A_0\|_{\rm op}^2+2B)^2(r+B)
\right]\le\frac{C_y}{n},\qquad n\ge16.
\tag{13}
\]

Here is an elementary verification that the last constant is uniform in `n`. Conditionally on `u_0`, the entries of `A_0u_0` are independent `N(0,r/n)`. Thus `q=r xi`, where `r` and `xi` are independent normalized chi-squares `chi_n^2/n`. Direct integration of their gamma densities gives

\[
\mathbb E r^{-4}
=\frac{n^4}{(n-2)(n-4)(n-6)(n-8)}\le16\quad(n\ge16),
\qquad \mathbb E q^{-4}=(\mathbb E r^{-4})^2\le256.
\]

All fixed positive moments of `r` are uniformly bounded as well. To control operator moments, take `1/4` nets of both unit spheres of cardinality at most `9^n` (the volume packing bound). For any matrix its operator norm is at most twice the maximum absolute bilinear form over those nets. Each such form for `A_0` is `N(0,1/n)`. A Gaussian tail bound and union bound yield

\[
\Pr\{\|A_0\|_{\rm op}>R\}
\le2\exp(2n\log9-nR^2/8)
\le2e^{-nR^2/16}\quad(R^2\ge32\log9).
\]

Integrating this tail bounds every fixed operator-norm moment uniformly. Cauchy--Schwarz first separates `q^{-2}` from the remaining factor, and a second application separates the operator and `r` moments; no independence between these factors is assumed. This proves (13).

Together (11) and (13) give the unconditional sharp rate

\[
\frac{y}{\sqrt{1+B}}\,n^{-1/2}
\le
\left(\mathbb E\sup_{t\ge0}|f_n(t,x_*)-0|^2\right)^{1/2}
\le\sqrt{C_y}\,n^{-1/2}.
\tag{14}
\]

The reference zero is indeed the deterministic population test trajectory: (13) itself proves uniform-in-time convergence in mean square to zero. Thus this conclusion does not rely on interchanging finite-time and endpoint limits from another theorem. For the endpoint circle metric described above, the expectation is exactly half the endpoint test mean square and has the same root rate.

The expected absolute error also has the same lower rate: conditional Gaussianity and convexity of `r -> (r+B)^{-1/2}` give `E |f_n(infinity,x_*)| >= sqrt(2/pi) y / sqrt(n(1+B))`; (13) supplies the matching upper bound. The signed expected test prediction is exactly zero and is not an accuracy metric.

## What this says about the two paper remainders

The proof defines the prediction remainder as `b_{n,mu}=C_mu b_n+d_{n,mu}`, with `d_{n,mu}` the all-time dense-to-population test error. Equations (5) and (14) obstruct a universal `n^{-1}` root-error rate for that construction, and more generally for any order-uniform prediction bound `E_mu(fhat_{n,q},f_infinity)<=C_mu omega(q)+b_{n,mu}` that holds for all `q` on the common events. At each fixed width, let `q->infinity` on any finite physical horizon using the paper's fixed-width closure convergence; the bound then implies `|f_dense(t,x_*)-f_infinity(t,x_*)|<=b_{n,mu}` for every `t`, and then at the fitted endpoint by continuity. The lower bound survives removal of events whose probabilities tend to zero.

By contrast, `b_n=C Phi(a_n)` in the tracking proof measures a sufficient carrier-tail transfer error in a closure-to-dense estimate. Both models share the same Gaussian initialization. The unused-column population fluctuation does not supply a lower bound for `a_n` or `b_n`. In the linear case changed-gate products vanish and the cutoff argument can be simplified; no nonlinear rate for `a_n` is proved here.

## Honest rate conversion through Phi

The tracking proof uses

\[
\Phi(u)=u\exp\!\{K\sqrt{\log(e+1/u)}\},\quad \Phi(0)=0.
\]

For any `alpha>0`, if `a_n=O_P(n^{-alpha})`, then

\[
\Phi(a_n)=O_P\!\left(n^{-\alpha}
       e^{K\sqrt{\alpha\log n+O(1)}}\right)
=O_P(n^{-\alpha+\epsilon})\quad\hbox{for every }\epsilon>0.
\tag{15}
\]

To justify the first statement, `Phi` is increasing on a sufficiently small interval: its logarithmic derivative in `u` is

\[
1-\frac{K}{2(eu+1)\sqrt{\log(e+1/u)}},
\]

which tends to `1` as `u->0`. On a probability-`1-delta` event, bound `a_n<=C_delta n^{-alpha}` and apply that local monotonicity. The ratio between `Phi(C_delta n^{-alpha})` and `n^{-alpha} exp(K sqrt(alpha log n))` stays bounded. Global monotonicity is not needed and need not hold for large `K`.

Probability rates do not by themselves imply expectation rates, even if `a_n` is uniformly bounded. For example, let `a_n=1` with probability `1/log(n+2)` and zero otherwise. Then `a_n=O_P(n^{-alpha})` for every fixed `alpha`, whereas `E Phi(a_n)=Phi(1)/log(n+2)`.

If instead an actual moment bound `E a_n^p<=C n^{-alpha p}` is supplied for a fixed `p>=1`, even the precise subpolynomial factor transfers. For `r_n=(E a_n^p)^{1/p}->0`, local monotonicity gives `Phi(a_n)<=Phi(r_n)` on `a_n<=r_n`; on `a_n>r_n`, the globally decreasing ratio `Phi(u)/u` gives `Phi(a_n)<=a_n Phi(r_n)/r_n`. Splitting these two events proves

\[
\|\Phi(a_n)\|_{L^p}\le2^{1/p}\Phi(\|a_n\|_{L^p})
=O\!\left(n^{-\alpha}e^{K\sqrt{\alpha\log n+O(1)}}\right).
\tag{16}
\]

The case `r_n=0` is immediate. No boundedness assumption on `a_n` is needed for this argument. A weaker but convenient power-only conversion also follows from, for every `eta in (0,1)`,

\[
\Phi(u)\le C_{\eta,A}u^{1-\eta}\quad(0\le u\le A).
\]

For bounded `a_n<=A`, taking powers and applying the concavity inequality to `a_n^p` gives

\[
\bigl(\mathbb E\Phi(a_n)^p\bigr)^{1/p}
\le C_{\eta,A}\bigl(\mathbb E a_n^p\bigr)^{(1-\eta)/p}
\le C' n^{-\alpha(1-\eta)}.
\tag{17}
\]

Thus quantitative moments suffice for the precise factor, whereas a probability rate alone does not. Likewise, a high-probability width estimate for the dense predictor cannot be called an unconditional RMS estimate without controlling its exceptional event.

## Remaining scope

This route proves an admissible zero-readout prediction obstruction and a sharp explicit linear example. It does not prove an upper rate for general nonlinear activations, a rate for the dense carrier excess `a_n`, or a lower bound for the distinct tracking remainder `b_n`. The general nonlinear upper-rate question remains open in this route.
