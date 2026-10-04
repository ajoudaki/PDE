# A solved q=1 example: fitting, boundary rotation, and test classification

Root derivation from the fully specified intrinsic q=1 equations and the scalar sign-cone argument also proved independently in ENERGY_ROUTE.md. No experiment or dense-training reference is used. This is a deliberately scoped theorem: one neuron in each of two hidden layers, one circle training point, and a named ground-truth classification rule. It is not a multi-sample or general-task theorem.

## 1. Statement

Use n=m=1, d=2, tanh, no biases, w0=v0=0, k0=h0, tau0=1. Rotate the circle so x_*=sqrt(2)(1,0) is the training input, with label y in {-1,1}. Write the initialized read-in as A0=(a0,beta), and assume a0 W0 !=0. This event has probability one under the specified independent nondegenerate Gaussian initialization.

For the whole circle x(theta)=sqrt(2)(cos(theta),sin(theta)), the q=1 flow has:

1. Exponential training MSE decay to zero, with rate at least 4 tanh(|W0 tanh(a0)|)^2.
2. A(t)=(a(t),beta), where sign(a(t))=sign(a0), |a(t)| increases strictly for t>0, and a(t) converges to a finite a_infinity with |a_infinity|>|a0|.
3. For every t>0, its classification rule is exactly

\[
\operatorname{sign}f_t(\theta)
=y\,\operatorname{sign}\!\left(\cos\theta+\frac{\beta}{a(t)}\sin\theta\right).
\tag{1}
\]

Take the specified test truth y_true(theta)=y sign(cos theta), with uniform angular input law. Then the classification disagreement probability is exactly

\[
\mathcal R_{\rm cls}(t)
=\frac1\pi\arctan\!\left(\frac{|\beta|}{|a(t)|}\right),\qquad t>0.
\tag{2}
\]

When beta!=0, it decreases strictly, and its endpoint is strictly below its right-hand limit at initialization. When beta=0, it is identically zero. It generally remains positive: one training point does not erase the random unobserved input component beta.

The ground truth above is an explicit additional task choice, with the training point at the center of a true class semicircle. It is not inferred from one label. Other target boundaries can reverse the test-risk conclusion. At t=0 the predictor is identically zero, so the comparison is with t down to zero from above, not an undefined zero-score classifier.

## 2. Proof of the dynamical assertions

Only the component of A along x_* changes, directly from its evolution equation. Thus its second component beta is exactly constant and h=tanh(a).

Put s=sign(a0), c=sign(W0), b=|W0|, H=s h, K=s k, vtilde=cs v and u=ycs w. Set

\[
\Gamma=\tanh((b+\widetilde v K)H),\qquad e=1-u\Gamma.
\]

Initially H=K=|tanh(a0)|>0, u=vtilde=0 and e=1. Substitution in the original q=1 equations gives

\[
\begin{aligned}
\dot u&=2e\Gamma,\\
\dot{\widetilde v}&=2eu(1-\Gamma^2),\\
\dot H&=2eu(b+\widetilde v K)(1-\Gamma^2)(1-H^2)^2,\\
\dot K&=\frac{|e|}{\tau}(H-K),\qquad \dot\tau=|e|.
\end{aligned}
\tag{3}
\]

The region e>=0, u,vtilde>=0, H>=K>0 is invariant. On e>=0 all the displayed population variables are nondecreasing, and at H=K the derivative of H-K is nonnegative. The face e=0 consists of equilibria; local uniqueness prohibits crossing or reaching it at a finite time from the nonstationary initial state. Consequently e>0 at every finite time, u>0 for t>0, and H increases strictly there. The absolute value |a| grows strictly as well, since tanh is strictly increasing.

Since Gamma is nondecreasing and Gamma>=Gamma0=tanh(|W0 tanh(a0)|)>0,

\[
\dot e=-2e\Gamma^2-u\dot\Gamma\le-2\Gamma_0^2e.
\]

Thus e(t)<=exp(-2 Gamma0^2 t), proving the squared-loss rate. Also u Gamma<=1 gives u<=1/Gamma0, while integration of vtilde_dot yields vtilde<=Gamma0^(-3). The training preactivation obeys

\[
|\dot a|\le\frac{2e}{\Gamma_0}(b+\Gamma_0^{-3}),
\]

which is integrable. All scalar states therefore have finite limits, and the strict positive movement gives |a_infinity|>|a0|. These bounds also rule out finite-time escape within the cone.

## 3. Whole-input classification and test risk

The effective scalar mixer is B=W0+v k=c(b+vtilde K), so sign(B)=c. At positive times sign(w)=ycs. Both tanh functions preserve signs. Therefore, for any query theta,

\[
\operatorname{sign}f_t(\theta)
=y s\operatorname{sign}(a(t)\cos\theta+\beta\sin\theta),
\]

which is (1), because sign(a(t))=s. Its oriented normal makes angle

\[
\delta(t)=\arctan(\beta/a(t))\in(-\pi/2,\pi/2)
\]

with the true oriented normal. Two semicircle classifiers whose normals differ by an angle |delta| disagree on two arcs of length |delta|, for total angular length 2|delta|. Division by 2pi proves (2). Since |a(t)| grows strictly, the risk decreases strictly for beta!=0.

The argument proves a concrete mechanism of useful feature learning for this named task: growth in the observed direction reduces the relative influence of the unobserved random component. The memory and readout remain fully coupled; none was frozen to obtain (3). Nevertheless a scalar two-layer odd network can only classify by a semicircle, so this theorem does not explain more complicated multi-boundary tasks.

## 4. The key remains a historical state even after fitting

Equation (3) and integrability of e imply finite tau_infinity. Integrating the key equation gives

\[
H_\infty-K_\infty
=\frac1{\tau_\infty}\int_0^\infty\tau(t)\dot H(t)dt
\ge\frac{H_\infty-H_0}{\tau_\infty}>0.
\]

The learner fits and its classification never worsens (strictly improves when beta!=0) while retaining a strictly positive gap between current feature and memory key. This demonstrates why key lag cannot simply be dismissed as failed learning or an error that must vanish. The all-time conclusion uses the proved scalar sign cone; it is not assumed for the general multi-input system.
