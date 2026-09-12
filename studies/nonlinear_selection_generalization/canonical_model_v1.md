#### C.4.10. Generalization during a finite added-data episode

The selected nonlinear predictor can learn a family specified independently of
the network, from finitely many noisy added observations. The family below has
full-circle input support and independently varying Fourier coefficients. A
finite-mode contraction connects that structure to an explicit approximation
floor, sampling and noise errors, and a positive stopping time. The hidden
features evolve throughout the episode. All quantitative constants are defined
from the class and the established reference; their numerical practicality is
not asserted.

##### C.4.10.1. Model, target family and observations

Retain exactly the bias-free two-hidden-layer tanh network
\[
 u=x/\sqrt2\in S^1,\qquad h^1_n=\tanh(W^1_nu),\qquad
 h^2_n=\tanh(W^2_nh^1_n),\qquad f_n=(W^3_n)^Th^2_n/n.
 \tag{NG1}
\]
Every stored entry and block is initialized independently, centered Gaussian
with variances \((1,1/n,1/n^2)\); the mobilities are \((n,1,n)\). Training is
physical GF of the unhalved mean square loss. The actual finite Gaussian
readout is retained. Every physical run starts from these initial arrays and
uses its fixed training law throughout.

Write
\[
 \nu_*={1\over2}\delta_{(\sqrt2e_1,1)}
                 +{1\over2}\delta_{(\sqrt2e_2,-1)},\qquad
 \mu_{\varepsilon,\nu}=(1-\varepsilon)\nu_*+\varepsilon\nu.
 \tag{NG2}
\]
Use C.4.9's full first-row state \(\theta=(w,K,c)\), raw Hilbert metric,
initialized Gaussian action \(A_0\), actual adjoint, and \(A=A_0+K\). Only
\(K\) is Hilbert–Schmidt. Its endpoint \(\theta_\dagger\), determined by the
complete reference feature flow from \((g,0,0)\), and
\(F_*(\sqrt2u)=f_{\theta_\dagger}(u)\) are those of C.4.9. In particular
\(F_*\) is odd, fits the two anchors, and changes sign under swapping the
two coordinates. The raw gradient and constraint projection are exactly
\[
 g_\theta(u)=\bigl(\phi'(w\cdot u)A^*[c\phi'(AH^1(u))]u,
          [c\phi'(AH^1(u))]\otimes H^1(u),H^2(u)\bigr),
 \quad \phi=\tanh,
\]
\[
 G_\theta=(g_\theta(e_1),g_\theta(e_2)),\quad
 M_\theta=G_\theta^*G_\theta,\quad
 \Pi_\theta=I-G_\theta M_\theta^{-1}G_\theta^*.
 \tag{NG3}
\]
Here \(H^1(u)=\phi(w\cdot u)\), \(H^2(u)=\phi(AH^1(u))\). No action,
adjoint, readout or feature is replaced by an independent surrogate.

Let \(\rho\) be normalized arc measure, with angle \(\alpha\) modulo
\(2\pi\) and \(u_\alpha=(\cos\alpha,\sin\alpha)\). Densities belong to
the fixed class
\[
 \mathcal P_D=\{p:\tfrac12\le p\le2,\ \int p\,d\rho=1,
                    \operatorname{Lip}_{\rm circle}(p)\le D\},\qquad D\ge0.
 \tag{NG4}
\]
In circle integrals, a function of physical input \(x\) is also written as
its pullback at \(x=\sqrt2u_\alpha\); this applies to \(q,F_*,P_\nu\) and
the sampled inputs in the force formulas.
Thus every input distribution has the entire circle as support. Neither its
support nor these bounds depend on width, sample size or contamination.
Fix \(s\ge1\), \(0\le R\le1/8\), and set
\[
 q_0(\alpha)=\cos^3\alpha-\sin^3\alpha,\qquad h(\alpha)=\sin^2(2\alpha),
 \qquad q=q_0+h v,
\]
\[
 v(\alpha)=\sum_{k\ge0}\{a_k\cos((2k+1)\alpha)+b_k\sin((2k+1)\alpha)\},
 \qquad \sum_{k\ge0}(2k+1)^s(|a_k|+|b_k|)\le R.
 \tag{NG5}
\]
Finite coefficient cap \(N\ge0\) means all coefficients with \(k>N\) are
zero; the resulting target's harmonic degree is at most \(2N+5\). Infinite
series are admitted with the same summability bound. This is a family of
targets specified without using any trained prediction. They are odd and
agree with the known anchor labels, so these constraints have no target
approximation cost. Other targets are not covered by the theorem.

For \(X=\sqrt2u_\alpha\) with density \(p\in\mathcal P_D\), labels obey
\[
 Y=q(X)+\xi,\qquad \mathbb E[\xi\mid X]=0,\qquad
 |\xi|\le h(\alpha)/8,\qquad \mathbb E[\xi^2\mid X]\le\sigma^2,
 \quad 0\le\sigma\le1/8.
 \tag{NG6}
\]
These laws have \(|Y|\le1\), and so are admitted for any prescribed label
bound at least one. Indeed, if \(a=|\cos\alpha|\), \(b=|\sin\alpha|\),
and \(t=ab\le1/2\), then
\((a^3+b^3)^2=1-3t^2+2t^3\le1-2t^2\le(1-t^2)^2\).
Consequently \(|q_0|\le1-h/4\); the perturbation and noise each use at most
\(h/8\) of this margin. Also \(\|v\|_\infty,\|v'\|_\infty\le R\), so
the series and derivative are uniformly convergent and the targets are
uniformly Lipschitz. Nonzero centered noise is permitted on arcs where
\(h>0\).

Draw \((X_i,Y_i)_{i=1}^m\) independently from \(\nu\), independently of
the Gaussian initialization, and train on
\[
 \widehat\nu_m={1\over m}\sum_{i=1}^m\delta_{(X_i,Y_i)},\qquad
 \widehat\mu_{\varepsilon,m}=(1-\varepsilon)\nu_*+
                                      \varepsilon\widehat\nu_m.
 \tag{NG7}
\]
Only the added observations are sampled. The anchor weights remain exactly
\((1-\varepsilon)/2\); no random rare-component count occurs in this design.
For an independent test input with law \(\nu_X\), use excess risk
\[
 \mathcal E_\nu(f)=\|f-q\|_{L^2(p\rho)}^2
                   =R_\nu(f)-\mathbb E\xi^2.
 \tag{NG8}
\]
Predictions are nevertheless retained on the entire circle.

The next three subsections prove the theorem package: common nonlinear
selection and original-GF capture for bounded added laws; continuum separation
and finite target-mode conditioning; then approximation, separated sampling
and noise, a class-determined positive stop, and robust unseen-risk and paired
upper-hidden margins. The limits are width first at each fixed positive
\(\varepsilon\) and each fixed sample, then \(\varepsilon\downarrow0\),
then increasing sample size. Nothing below invokes the time-40 sampling
theorem, a simultaneous rate, raw GD, or an all-time changed-law endpoint.
