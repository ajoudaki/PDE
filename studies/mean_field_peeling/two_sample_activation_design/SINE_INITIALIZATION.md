# Exact all-layer initialization geometry of the calibrated sine activation

This is an initialization lemma only, for the original independent Gaussian middle matrices. It does not assert a trained-flow theorem.

Use the activation and notation in `two_sample_activation_design/RELATIVE_NONLINEARITY.md`:

\[
 r(z)=\sin(\omega z)-\omega e^{-\omega^2/2}z,
\quad v=\mathbb E r(G)^2,
\quad \Phi(z)=\frac{z+b r(z)}{\sqrt{1+b^2v}}.
\]

Let `(G_1,G_2)` be standard Gaussians of correlation c in [-1,1], and put a=omega^2. The identity `sin u sin v=[cos(u-v)-cos(u+v)]/2` and the Gaussian characteristic function give

\[
\mathbb E[\sin(\omega G_1)\sin(\omega G_2)]
=e^{-a}\sinh(ac).
\]

Gaussian regression gives `E[G1 sin(omega G2)]=c omega exp(-a/2)`; at singular endpoints this follows directly from `G2=+/-G1`. Therefore

\[
R(c):=\mathbb E[r(G_1)r(G_2)]
=e^{-a}[\sinh(ac)-ac],\qquad v=R(1)>0.               \tag{1}
\]

The cross terms between the linear part and r vanish for every c, so the exact correlation update is

\[
F(c)=\mathbb E[\Phi(G_1)\Phi(G_2)]
=\frac{c+b^2R(c)}{1+b^2v}.                           \tag{2}
\]

This also proves `E Phi(G)^2=1`, so each subsequent initialized Gaussian preactivation has variance one. Hence all initialized marginal activation nonlinear fractions equal `b^2v/(1+b^2v)`, at all three hidden layers.

For 0<c<1, the absolutely convergent power series yields

\[
\frac{R(c)}c=e^{-a}\sum_{k\ge1}
               \frac{a^{2k+1}c^{2k}}{(2k+1)!}
<e^{-a}\sum_{k\ge1}\frac{a^{2k+1}}{(2k+1)!}=v.
\]

All terms are positive and `b>0`, so `0<F(c)<c`. Oddness gives `|F(c)|<|c|` for -1<c<0 as well; F(0)=0 and F(+/-1)=+/-1.

For the original initial pair with correlation rho, the top feature Gram is therefore

\[
K^4_0=\begin{pmatrix}1&F^{\circ3}(\rho)\\F^{\circ3}(\rho)&1\end{pmatrix},
\qquad
\lambda_{\min}(K^4_0)=1-|F^{\circ3}(\rho)|
\ge1-|\rho|.                                         \tag{3}
\]

For either binary label pair, the projected initial kernel satisfies

\[
\kappa_0=\frac14y^TK^4_0y
=\frac12[1+y_1y_2F^{\circ3}(\rho)]
\ge\frac12(1-|\rho|)\ge\delta/2.                    \tag{4}
\]

At population initialization the other raw kernel blocks vanish because C0=0. The usual fixed-depth Gaussian initialization induction suffices to identify these initialized laws: condition on the preceding feature matrix, use independence of the next centered Gaussian matrix, and pass its covariance entries by the law of large numbers at each of the fixed three layers. No growing-time transcript or trained Gaussianity is assumed.

For omega=2, b=2/5, this supplies one strictly increasing, moderately nonlinear activation, with the same approximately 6.4% nonlinear variance at every initialized layer and initial separation no worse than the input separation. The lemma does not prove that the trained preactivations stay Gaussian, that the initialized variance persists, or that the nonlinear fraction remains positive during training.
