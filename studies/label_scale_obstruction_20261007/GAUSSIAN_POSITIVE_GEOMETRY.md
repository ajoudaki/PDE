# Exact geometry for the Gaussian, zero-readout question

This is an independent theoretical route within the assigned study. The first round used only the supplied model. A subsequent supervisor instruction permitted the relevant maintained-book sections in `docs/09-trainability.qmd` and `docs/10-correlated-pairs.qmd`. No other study artifact, external scientific source, or simulation was used.

The strongest current result is the complete candidate proof in Section 13: for any fixed finite orthogonal dataset and any fixed common label magnitude, with arbitrary label signs, the canonical Gaussian, zero-readout tanh network fits exactly with probability tending to one. Strict finite-time capture also gives open label neighborhoods around these vectors. This awaits independent review. For nonorthogonal obtuse pairs, Section 10 proves endpoint diversity conditional on a strong scalar population construction; that construction remains open here. Neither result resolves arbitrary fixed mixed labels on a broadly nonorthogonal dataset.

## 1. Model and exact gradient geometry

The columns of \(X\in\mathbb R^{d\times m}\) are unit inputs. The stored weights and forward pass are

\[
A\in\mathbb R^{n\times d},\quad W\in\mathbb R^{n\times n},\quad
w\in\mathbb R^n,\qquad
U=\tanh(AX),\quad H=\tanh(WU),\quad f=H^\top w/n.
\]

The residual and loss are \(r=f-y\) and \(\mathcal L=\|r\|^2/m\). The physical metric has squared norm

\[
\|(\Delta A,\Delta W,\Delta w)\|_{\rm par}^2
=\|\Delta A\|_F^2/n+\|\Delta W\|_F^2+\|\Delta w\|^2/n.
\]

Its gradient flow is exactly the prescribed flow with mobilities \(n,1,n\). Initialization has independent \(A_{ij}\sim N(0,1)\), \(W_{ij}\sim N(0,1/n)\), and \(w=0\) exactly.

For sample \(a\), write \(u_a=\tanh(Ax_a)\), \(z_a=Wu_a\), \(h_a=\tanh z_a\), and define the actual backward vectors

\[
b_a=w\odot\operatorname{sech}^2z_a,\qquad
c_a=\operatorname{sech}^2(Ax_a)\odot W^\top b_a.
\]

Differentiating the forward pass gives the prediction kernel

\[
K_{ab}=\frac{h_a^\top h_b}{n}
+\frac{b_a^\top b_b}{n}\frac{u_a^\top u_b}{n}
+(x_a^\top x_b)\frac{c_a^\top c_b}{n}.
\]

Every displayed contribution is positive semidefinite, and

\[
\dot r=-\frac2mKr,\qquad
\dot{\mathcal L}=-\frac4{m^2}r^\top Kr.
\]

These are identities for the moving network, not a frozen-feature approximation.

## 2. Scalar ascent preserves its own readout-feature norm

Take two inputs with \(\rho=x_1^\top x_2\in(-1,1)\), and labels \((a,-a)\), \(a>0\). Define the scalar contrast and its feature

\[
g=\frac{f_1-f_2}{2}=\frac{w^\top h_-}{n},\qquad
h_-=\frac{h_1-h_2}{2}.
\]

Consider the auxiliary **exact scalar gradient ascent**

\[
\theta'=\operatorname{grad}_{\rm par}g,
\]

where the prime denotes feature time \(s\). This is the original physical training trajectory only when the physical residual lies in the contrast direction. At finite Gaussian width that is generally false.

Put \(R=\|w\|^2/n\), \(C=\|h_-\|^2/n\), and \(q_0=C(0)>0\). Readout linearity and the gradient identity give

\[
w'=h_-,\qquad R'=2g,\qquad
g'=\|\operatorname{grad}_{\rm par}g\|_{\rm par}^2\ge C,
\qquad g^2\le RC.
\]

At zero readout the hidden gradients vanish, so

\[
w(s)=s h_-(0)+o(s),\quad g(s)=q_0s+o(s),\quad
R(s)=q_0s^2+o(s^2).
\]

Consequently \(g>0\) initially, and on any interval where \(g>0\),

\[
\left(\frac{R}{g^2}\right)'
=-\frac{2(Rg'-g^2)}{g^3}\le0.
\]

The limit of this ratio at zero is \(1/q_0\). Thus

\[
R\le g^2/q_0,\qquad C\ge g^2/R\ge q_0,\qquad g'\ge q_0.
\]

This prevents a later zero of \(g\) and proves the inequalities throughout the interval of existence. Equivalently, \(\sqrt R\) is convex, with initial right derivative \(\sqrt{q_0}\). The feature norm \(C(s)\) need not be monotone; the proved assertion is \(C(s)\ge C(0)\).

At finite width this scalar ascent is global. Indeed \(\|w(s)\|_\infty\le s\), \(\|u_a\|/\sqrt n\le1\), and \(\|b_a\|/\sqrt n\le s\), so

\[
\|W'(s)\|_F\le s,\qquad
\|W(s)\|_{\rm op}\le\|W(0)\|_{\rm op}+s^2/2,
\qquad
\|A'(s)\|_F/\sqrt n\le s\|W(s)\|_{\rm op}.
\]

These bounds rule out a finite-time escape of the smooth finite-dimensional ODE. Therefore a unique scalar target \(g(s_*)=a\) is reached with \(s_*\le a/q_0\).

For a strong population gradient path the identical Hilbert-space calculation holds. It does **not** by itself construct that path. A continuous vector field on an infinite-dimensional Hilbert space is not enough for a local-existence assertion.

If an actual initialized trajectory obeys \(f_1=g\), \(f_2=-g\), then mean-loss flow has the exact clock

\[
\frac{ds}{dt}=2(a-g),\qquad
\frac{d}{dt}(a-g)=-2g'(s)(a-g).
\]

Provided the strong scalar path exists through its finite target endpoint,

\[
\mathcal L(t)=(a-g(t))^2\le a^2e^{-4q_0t}.
\]

The finite target state makes this a possible starting point for a finite-width capture proof; it does not supply that proof automatically.

## 3. What Gaussian exchange symmetry supplies

The reflection

\[
Q=I-2vv^\top,\qquad v=(x_1-x_2)/\|x_1-x_2\|
\]

interchanges the equal-norm inputs. The parameter transformation

\[
(A,W,w)\longmapsto(AQ,W,-w)
\]

is an isometry, preserves the initialized Gaussian law, and sends \((f_1,f_2)\) to \((-f_2,-f_1)\). Both opposite-label physical gradient flow and scalar contrast ascent are equivariant under it.

Thus their finite prediction paths have this symmetry **in law**. If those predictions converge to a deterministic population path, that path must satisfy \(f_2=-f_1\). An arbitrary random subsequential limit need not satisfy this identity pathwise. Nor does one finite Gaussian draw.

In an exactly symmetric population realization, sample exchange is represented by layerwise unitary involutions. The first-layer common and contrast features

\[
u_+=(u_1+u_2)/2,\qquad u_-=(u_1-u_2)/2
\]

are orthogonal, as are the corresponding top features \(h_+,h_-\). The readout is odd under exchange. These statements concern the complete population construction, not an engineered pairing of finite neurons.

## 4. Endpoint coercivity reduces to preventing total antipodal collapse

For an exactly symmetric scalar population path, use normalized layer inner products; finite expressions use \(n^{-1}\) times the Euclidean inner product. Let

\[
d_{2,+}=\frac{\operatorname{sech}^2z_1+\operatorname{sech}^2z_2}{2},\quad
d_{2,-}=\frac{\operatorname{sech}^2z_1-\operatorname{sech}^2z_2}{2},\quad
b_+=w d_{2,+},\quad b_-=w d_{2,-}.
\]

For the common prediction \(k=(f_1+f_2)/2\), its readout gradient is \(h_+\), and its middle-weight gradient is

\[
b_+\otimes u_+ +b_-\otimes u_-.
\]

Here \(b\otimes u\) is the population operator \(v\mapsto b\langle u,v\rangle\); its finite representative is \(bu^\top/n\). Symmetry makes the two displayed rank-one terms orthogonal. Consequently the common-direction squared gradient from readout and middle weights is

\[
\|h_+\|^2+\|b_+\|^2\|u_+\|^2+\|b_-\|^2\|u_-\|^2.
\]

At a scalar endpoint \(g=a>0\), the readout is nonzero. If \(h_+\ne0\), the common direction is already positive. If \(h_+=0\), oddness and strict monotonicity of tanh imply \(z_2=-z_1\), hence \(d_{2,-}=0\), \(b_-=0\), and \(b_+=w\operatorname{sech}^2z_1\ne0\) in \(L^2\). Therefore **\(u_+\ne0\) suffices for positivity of the common direction**.

The contrast readout direction is positive by Section 2. Exchange symmetry makes the common and contrast directions orthogonal in each parameter-block Gram. Thus \(u_+(s_*)\ne0\) proves positive definiteness of the full two-sample kernel using only the readout and middle-weight blocks. No first-layer kernel bound is needed for this endpoint criterion.

At finite width, the scalar auxiliary ODE cannot reach \(u_+=0\) at finite feature time from Gaussian initialization. The condition is equivalent to \(A(x_1+x_2)=0\). It defines an invariant submanifold: when \(u_+=0\), also \(h_+=0\), both derivative differences vanish, and the scalar-ascent first-layer common velocity is zero. Smooth ODE uniqueness forward and backward prevents entry from outside. Gaussian initialization lies outside almost surely because \(x_1+x_2\ne0\).

This last finite-dimensional argument supplies no width-uniform lower bound, no exact finite exchange symmetry, and no direct population backward-uniqueness theorem.

## 5. Exact common-feature equation and an Osgood criterion

The following identity does not require sample symmetry. It holds on every strong scalar contrast-ascent path. Put

\[
d_{1,+}=\frac{\operatorname{sech}^2(Ax_1)+\operatorname{sech}^2(Ax_2)}2,
\qquad
d_{1,-}=\frac{\operatorname{sech}^2(Ax_1)-\operatorname{sech}^2(Ax_2)}2,
\]

and \(B_+=W^*b_+\), \(B_-=W^*b_-\), with \(W^*=W^\top\) at finite width. Writing \(p=(Ax_1+Ax_2)/2\), \(q=(Ax_1-Ax_2)/2\), the first-layer ascent equation gives

\[
p'=\frac{1+\rho}{2}(d_{1,-}B_++d_{1,+}B_-),\qquad
q'=\frac{1-\rho}{2}(d_{1,+}B_++d_{1,-}B_-).
\]

Differentiate \(u_+=(\tanh(p+q)+\tanh(p-q))/2\). Substitution yields

\[
u_+'=d_{1,+}d_{1,-}B_+
+\frac{(1+\rho)d_{1,+}^2+(1-\rho)d_{1,-}^2}{2}B_-.
\]

Tanh has the exact identities

\[
d_{1,-}=-2u_+u_-,\qquad
b_-=-2w h_+h_-.
\]

For real \(z_+,z_-\), the map

\[
z_+\longmapsto\frac{\tanh(z_++z_-)+\tanh(z_+-z_-)}2
\]

vanishes at zero and has derivative at most one in absolute value. Therefore \( |h_+|\le |Wu_+|\). On a feature interval \(0\le s\le S\) where \(\|W(s)\|_{\rm op}\le M\), the readout bound \(\|w(s)\|_\infty\le S\) implies

\[
\|B_-\|_2\le2SM^2\|u_+\|_2.
\]

Both \(d_{1,+}\) and \(u_-\) have absolute value at most one, and the nonnegative coefficient of \(B_-\) in the equation for \(u_+'\) is at most one. Hence \(e(s)=\|u_+(s)\|_2^2\), with \(0\le e\le1\), satisfies

\[
e'\ge-4\mathbb E[u_+^2|B_+|]-4SM^2e.\tag{1}
\]

No fourth-moment assumption on the first preactivation is needed: \(u_+\) itself is bounded. For every \(p\ge2\), Hölder and \( |u_+|\le1\) give

\[
\mathbb E[u_+^2|B_+|]
\le\|B_+\|_{L^p}\|u_+\|_{L^{2p/(p-1)}}^2
\le\|B_+\|_{L^p}e^{1-1/p}.\tag{2}
\]

**Conditional nonextinction lemma.** Suppose on \([0,S]\) there is \(C\in L^1([0,S])\) and \(0\le\alpha\le1\) such that

\[
\|B_+(s)\|_{L^p}\le C(s)p^\alpha
\quad\text{for every real }p\ge2\text{ and almost every }s.\tag{3}
\]

Then \(e(0)>0\) implies \(e(s)>0\) for every \(s\le S\).

To prove this, take \(p=\max\{2,\log(1/e)\}\) while \(e>0\). Then \(e^{-1/p}\le \mathrm e\), so (1)–(3) imply, with a numerical constant \(c_\alpha\),

\[
e'\ge-[c_\alpha C(s)+4SM^2]
       e[1+\log(1/e)]^\alpha.
\]

Set \(v=1+\log(1/e)\). Up to a proposed first zero of \(e\),

\[
v'\le[c_\alpha C(s)+4SM^2]v^\alpha.
\]

If \(\alpha<1\), integrate the derivative of \(v^{1-\alpha}\); if \(\alpha=1\), integrate the derivative of \(\log v\). In both cases \(v\) stays finite through \(S\), contradicting a first zero of \(e\). This is the Osgood mechanism in an explicit differential form.

Gaussian-tail control, \(\|B_+\|_p\lesssim\sqrt p\), is more than sufficient. Growth at most linear in \(p\) is still sufficient. Merely knowing every fixed moment is finite, with no control of its growth in \(p\), does not establish this argument.

The assumption (3) is **not proved here for the actual two-tanh-layer Gaussian population flow at every fixed feature horizon**. In a valid source representation, a Gaussian term of bounded variance plus a bounded response shift would imply it. Proving a response shift bound uniformly as a time mesh is refined remains a real obligation; it cannot be inferred from bounded operator and \(L^2\) norms alone.

## 6. Why readout and middle-weight coercivity is sufficient for capture

This is an exact deterministic basin principle. For a smooth finite-width state \(\theta_T\), suppose a parameter ball of radius \(R\) around it has \(K(\theta)\succeq\kappa I\), \(\kappa>0\). If

\[
\|f(\theta_T)-y\|<R\sqrt\kappa,
\]

the subsequent physical gradient flow never leaves the ball and fits exponentially. Indeed, where the bound holds,

\[
-\frac{d}{dt}\|r\|=\frac{2r^\top Kr}{m\|r\|},\qquad
\|\dot\theta\|_{\rm par}=\frac2m\sqrt{r^\top Kr}
\le-\frac1{\sqrt\kappa}\frac{d}{dt}\|r\|.
\]

The remaining path length is at most \(\|r(T)\|/\sqrt\kappa<R\), which rules out a first exit. Also \(\|r(t)\|\le\|r(T)\|e^{-2\kappa(t-T)/m}\).

For a reference scalar endpoint with \(\|w\|_\infty\le S\) and bounded \(\|W\|_{\rm op}\), the two Jacobian blocks used in Section 4 have a dimension-independent local continuity estimate in the parameter metric. Forward differences obey

\[
\|\Delta u_a\|/\sqrt n\le\|\Delta A\|_F/\sqrt n,
\qquad
\|\Delta h_a\|/\sqrt n\le
\|\Delta W\|_F+M\|\Delta A\|_F/\sqrt n
\]

after enlarging \(M\) on the ball. For the upper backward vector, use the reference readout in the second term:

\[
b_a(\theta)-b_a(\theta_*)
=[w-w_*]\operatorname{sech}^2z_a
+w_*[\operatorname{sech}^2z_a-\operatorname{sech}^2z_{*,a}].
\]

Since \(\operatorname{sech}^2\) has bounded derivative, its normalized \(L^2\) norm is bounded by a constant depending on \(S,M\) times the parameter distance. The middle Jacobian is the normalized rank-one product \(b_a\otimes u_a\); the rank-one difference identity completes the same bound for that block. The readout block is just \(h_a\). Hence positive definiteness of these two blocks at a uniformly controlled reference endpoint gives a uniform nearby kernel bound. No first-layer backward \(L^\infty\) estimate is required for this local statement.

Applying the principle to iid Gaussian finite widths still needs an appropriate approximation/coupling theorem that puts their actual physical states into such a basin. Qualitative approximation of fixed-time predictions alone is insufficient to assert basin entry. The construction must control the relevant feature and Jacobian observations, or provide the corresponding reference-state coupling.

## 7. Maintained-source audit and exact remaining gap

The general Hilbert radial argument is already established in `docs/10-correlated-pairs.qmd`, D.4.3–6, and the reflection argument in D.4.2. Those sections explicitly distinguish a constructed strong uncut path from a merely continuous Hilbert vector field and a finite Gaussian law symmetry from pathwise symmetry. They support Sections 2–3 above, but do not themselves construct the requested canonical two-tanh-layer population dynamics.

The complete two-query response estimate in that chapter, II.B.1–6, gives Gaussian-plus-bounded-shift backward fields and sub-Gaussian tails. Its actual hypotheses are three hidden layers, activation \(1+\arctan(z)/10\), and feature horizon \(S\le3/2\). Its closed bounds use \(\|\phi'\|_\infty\le1/10\), \(\|\phi''\|_\infty\le1/5\), and the stated short horizon. It cannot be cited as a tanh, arbitrary-\(S\) estimate. The construction and cap-removal argument II.C.1–2 explicitly depends on those response-tail bounds.

Likewise, the depth-independent response estimate in `docs/09-trainability.qmd`, Section 6 of “Global nonlinear learning at every fixed hidden depth,” proves its envelope for the stated shifted activation and \(S\le3/2\). It is not an arbitrary-amplitude tanh extension. The fixed-order-closure scalar lemma near the end of that chapter concerns a different state model; only its readout-linearity algebra is shared.

The route's principal missing input is therefore concrete: construct/identify the actual correlated two-tanh-layer strong Gaussian feature flow through its target interval and control the actual first-layer backward field \(B_+\) by (3), or another estimate that excludes finite-time loss of the first-layer common mode. After that, the symmetry, scalar coercivity, common-mode endpoint geometry, and local capture calculations provide explicit bridges. A full finite-width high-probability theorem would still require verifying the stated approximation-to-basin bridge.

This is a correlated opposite-label pair route. Even completing it would not prove the original arbitrary mixed-label, multi-input target. It would give a substantive nonorthogonal, arbitrary-amplitude special family under the exact Gaussian initialization.

## 8. Independent full-rank-input landscape calculation

This secondary result does not depend on the pair reduction. Suppose \(X\) has column rank \(m\) and \(n\ge m\). Then every finite critical point of positive loss with \(w\ne0\) is a strict saddle.

Because \(X\) has full column rank and tanh has strictly positive derivative at finite arguments, arbitrary local variations of \(U=\tanh(AX)\) can be realized by varying \(A\). Thus one may check critical points in coordinates \((U,W,w)\). For a residual sample \(a\) with \(r_a\ne0\), criticality in \(U\) gives

\[
W^\top b_a=0.
\]

If \(U\) had column rank \(m\), criticality in each middle-weight row with \(w_i\ne0\) would imply \(r\odot\operatorname{sech}^2z_i=0\), hence \(r=0\). Therefore \(\operatorname{rank}U<m\), and there is a nonzero \(q\in\ker U^\top\).

Choose the two variations

\[
\Delta W=b_aq^\top,\qquad \Delta U=q e_a^\top,
\]

where \(e_a\) is the sample coordinate vector. Along a pure \(\Delta W\) variation, \(WU\) is unchanged because \(q^\top U=0\), so the loss is exactly constant. The first prediction variation along \(\Delta U\) is zero: only sample \(a\) changes, and its derivative is \(b_a^\top Wq/n=0\). The mixed second derivative of its prediction is

\[
\frac{\|b_a\|^2\|q\|^2}{n}>0.
\]

Consequently the mixed loss Hessian entry is

\[
\frac{2r_a}{mn}\|b_a\|^2\|q\|^2\ne0,
\]

while the pure \(\Delta W\) Hessian entry is zero. The Hessian restricted to these two variations has negative determinant and therefore a negative eigenvalue. At a critical point the change of coordinates from \(A\) to \(U\) preserves this negative second variation, proving the assertion.

An initialized path with nonzero initial feature-label projection decreases the loss strictly below \(\|y\|^2/m\). Such a path cannot converge to any finite state with \(w=0\), whose prediction is zero and whose loss is exactly the initial loss. Thus relevant finite positive-loss limits fall under the strict-saddle calculation.

This landscape statement does not prove boundedness of the trajectory or saddle avoidance from the singular initialization slice \(w=0\). A saddle-avoidance theorem assuming an absolutely continuous law in **all** parameters cannot simply be applied to that slice. Nor does it exclude escape to infinity with a positive limiting loss. These are substantive gaps, not consequences of the local Hessian calculation.

## 9. First-round claim status

* Exact: moving-kernel identities; scalar readout-feature protection; finite scalar target reachability; Gaussian exchange symmetry in law; the pair common-feature evolution equation; conditional Osgood nonextinction; the deterministic basin principle; the full-rank-input strict-saddle result.
* Exact conditional on a constructed symmetric strong path: contrast exponential fitting and reduction of endpoint readout-plus-middle coercivity to nonzero first-layer common features.
* Open here: canonical tanh population construction and sufficient backward-field tails through arbitrary fixed target amplitude; Gaussian finite-width basin transfer; arbitrary fixed mixed-label multi-input fitting.
* Not supplied: a fixed-data, fixed-label Gaussian event of nonvanishing probability with limiting loss bounded below by a positive constant.

Recommended route status: retain the pair/Osgood route as a concrete conditional mechanism; do not count it as a completed Gaussian fitting proof. The direct full-rank landscape route remains blocked at dynamical compactness and initialization-slice saddle avoidance.

## 10. Second attempt: tail-free common-coordinate protection for obtuse pairs

The supervisor authorized another bounded theory attempt and access to the complete same-study report GAUSSIAN_POPULATION_POSITIVE.md. No experiment was performed. The following improvement supersedes the need for the Osgood moment assumption in the endpoint nonextinction step when \(-1<\rho\le0\). It does not construct the nonorthogonal population path.

Keep \(p=(Ax_1+Ax_2)/2\), \(q=(Ax_1-Ax_2)/2\), and put

\[
\beta=\frac{1-\rho}{1+\rho}\ge1,\qquad
P=\cosh(2p),\quad Q=\cosh(2q),\quad D=|\sinh(2p)|.
\]

Here \(D\) is a scalar auxiliary function, not an activation derivative. Define

\[
I(p,q)=D^\beta Q+
\beta\int_1^P(v^2-1)^{\beta/2-1}\,dv,\qquad
F(p,q)=\operatorname{sgn}(p)I(p,q)^{1/\beta},
\]

with \(F(0,q)=0\). The lower endpoint is integrable because \(\beta/2-1>-1\). Moreover,

\[
|u_+|=\frac D{P+Q}\le D\le |F|.
\]

The two scalar vector fields multiplying \(B_+\) and \(B_-\) in Section 5 are

\[
V_+=\frac1{1+\beta}(d_{1,-},\,\beta d_{1,+}),\qquad
V_-=\frac1{1+\beta}(d_{1,+},\,\beta d_{1,-}),
\]

where

\[
d_{1,+}=\frac{2(1+PQ)}{(P+Q)^2},\qquad
d_{1,-}=-\frac{2\sinh(2p)\sinh(2q)}{(P+Q)^2}.
\]

For \(p\ne0\),

\[
I_p=2\beta\operatorname{sgn}(p)D^{\beta-1}(1+PQ),
\qquad I_q=2D^\beta\sinh(2q).
\]

Substitution gives \(V_+I=0\). The identity
\((1+PQ)^2-(P^2-1)(Q^2-1)=(P+Q)^2\) gives

\[
V_-I=\frac{4\beta}{1+\beta}\operatorname{sgn}(p)D^{\beta-1}.
\]

Therefore the exact scalar ascent obeys

\[
F'=\frac4{1+\beta}
 \left(\frac D{|F|}\right)^{\beta-1}B_-,
\qquad
\left|\frac4{1+\beta}
 \left(\frac D{|F|}\right)^{\beta-1}\right|\le\frac4{1+\beta}. \tag{4}
\]

The apparent zero denominator has a defined continuous extension. As \(p\to0\),
\(I=D^\beta(Q+1+o(1))\) and \(F=2p(Q+1)^{1/\beta}+o(p)\), locally uniformly in finite \(q\). Thus \(F\) is \(C^1\), and the coefficient in (4) extends as
\(4(Q+1)^{1/\beta-1}/(1+\beta)\). Its bound still holds because \(\beta\ge1\).

Let a strong path exist on \([0,S]\), with \(\|W\|_{\rm op}\le M\). Section 5 now implies

\[
\|F'\|_2\le\frac{8SM^2}{1+\beta}\|u_+\|_2
\le\frac{8SM^2}{1+\beta}\|F\|_2.                         \tag{5}
\]

Gaussian initial \((p,q)\) gives \(F(0)\in L^2\), since the definition has at most exponential growth in \(|p|+|q|\) for fixed \(\beta\). Also \(\|F(0)\|_2>0\), since \(p(0)\) is a nondegenerate Gaussian for \(\rho>-1\).

This chain rule does not assume later exponential moments. Strong first-layer paths have almost-everywhere absolutely continuous representatives. Apply the ordinary chain rule to those representatives. The coefficient in (4) is bounded and \(B_-\) is continuous in \(L^2\); integrating (4) from \(F(0)\in L^2\) proves strong absolute continuity of \(F\). Inequality (5) yields

\[
\|F(s)\|_2\ge\|F(0)\|_2
 \exp\!\left[-\frac{8SM^2s}{1+\beta}\right]>0.
\]

Since \(F=0\) exactly when \(u_+=0\), the first common feature cannot vanish at any finite feature time. For every constructed strong symmetric scalar path at an obtuse correlation, Sections 2 and 4 therefore give positive-definite readout-plus-middle kernel at its target endpoint, without backward-tail assumptions.

For \(0<\rho<1\), the same exact formula has \(\beta<1\), and its coefficient near \(p=0\) grows as \((Q+1)^{1/\beta-1}\). The bounded-coefficient proof no longer applies. This is a limitation of the estimate, not a fitting counterexample.

## 11. Candidate complete theorem for the orthogonal pair

The supervisor then explicitly authorized use of the complete generic Gaussian-program construction in the maintained book. The relevant source is docs/12-three-sample-learning.qmd, III.F.1–7, lines 316–728, together with its Hilbert–Schmidt and strong-chain-rule facts in III.F.8–11. These complete sections were read. The following argument uses their fixed-program theorem with its stated hypotheses; it does not import the activation-specific response-tail theorem.

**Candidate theorem, pending independent review.** Fix two orthogonal unit inputs, \(x_1^\top x_2=0\), and labels \(y=(a,-a)\), with any fixed \(a>0\). Use the exact two-hidden-layer tanh model and Gaussian initialization in Section 1, including exactly zero readout. Then

\[
\Pr\!\left(\lim_{t\to\infty}\mathcal L_n(t)=0\right)\longrightarrow1.
\]

There are deterministic constants \(T<\infty\) and \(c>0\), depending on \(a\) but not on width, such that, with probability tending to one,

\[
\mathcal L_n(t)\le\mathcal L_n(T)e^{-c(t-T)}
\qquad(t\ge T).
\]

This theorem is an orthogonal-pair special case. It does not resolve the requested nonorthogonal multi-input theorem.

### 11.1 Exact natural coordinates and a Lipschitz vector field

Define the increasing bijection

\[
\zeta(z)=\int_0^z\frac{dv}{\operatorname{sech}^2v}
=\frac z2+\frac{\sinh(2z)}4,\qquad
\psi(\xi)=\tanh(\zeta^{-1}(\xi)).
\]

It satisfies

\[
(\zeta^{-1})'=\operatorname{sech}^2z,\qquad
\psi'=\operatorname{sech}^4z,\qquad
\psi''=-4\tanh z\,\operatorname{sech}^6z,
\quad z=\zeta^{-1}(\xi).
\]

Thus \(\zeta^{-1}\) and \(\psi\) are globally Lipschitz, and \(\psi\) is bounded and \(C^2\) with bounded derivatives. Set \(\xi_a=\zeta(Ax_a)\) coordinatewise. Orthogonality makes the exact scalar-ascent equations

\[
\begin{aligned}
u_a&=\psi(\xi_a),\quad z_a=Wu_a,\quad h_a=\tanh z_a,\quad
b_a=w\operatorname{sech}^2z_a,\\
\xi_a'&=\frac{\sigma_a}{2}W^*b_a,\qquad
W'=\frac12\sum_{a=1}^2\sigma_a b_a\otimes u_a,\qquad
w'=\frac{h_1-h_2}{2},
\quad \sigma_1=1,\quad\sigma_2=-1.                       \tag{6}
\end{aligned}
\]

At finite width, \(W^*=W^\top\) and \(b\otimes u=bu^\top/n\). Recovering \(Ax_a=\zeta^{-1}(\xi_a)\) and applying the chain rule verifies the original scalar gradient equations exactly.

The actual two-residual physical equations, without imposing any symmetry, become

\[
\dot\xi_a=-r_aW^*b_a,\qquad
\dot W=-\sum_{a=1}^2r_a b_a\otimes u_a,\qquad
\dot w=-\sum_{a=1}^2r_a h_a.                              \tag{7}
\]

Again, these are the original mean-loss gradient flow in changed coordinates. No layer is frozen and no learning rate is changed.

The transformed state space is

\[
L^2(\Omega_1)^2\times
\bigl(W_0+\mathcal S_2(L^2(\Omega_1),L^2(\Omega_2))\bigr)
\times L^2(\Omega_2).
\]

For local existence, replace \(w\) only in \(b_a\) by a smooth scalar clip equal to \(w\) on \([-P,P]\), bounded in absolute value, with bounded derivative. Keep the readout in \(f_a=\langle w,h_a\rangle\) unchanged. This defines a vector field on an open \(L^2\) neighborhood; it avoids treating an \(L^\infty\) constraint as an open \(L^2\) set.

On a bounded state ball, forward fields are Lipschitz by bounded \(\|W\|_{\rm op}\), \(\|u_a\|_2\le1\), and the Lipschitz constants of \(\psi,\tanh\). The clipped product
\((w,z)\mapsto\operatorname{clip}_P(w)\operatorname{sech}^2z\)
is globally Lipschitz as a pointwise map. Reverse multiplication is Lipschitz in \(L^2\), and the rank-one difference inequality gives the Hilbert–Schmidt bound. Finally \(f_a=\langle w,h_a\rangle\) is locally Lipschitz by Cauchy–Schwarz. Both clipped vector fields (6), (7) are therefore locally Lipschitz, with constants independent of width on prescribed norm balls. Picard contraction supplies a unique strong local solution and the usual Euler error estimate.

For (6), fix any finite horizon \(S\) and choose \(P>S+1\). Since \(|w'|\le1\), the clip never acts. Also

\[
\|W(s)\|_{\rm op}\le\|W_0\|_{\rm op}+s^2/2,\qquad
\|\xi_a'(s)\|_2\le\tfrac12s(\|W_0\|_{\rm op}+s^2/2).
\]

These bounds and \(\|w\|_2\le s\) prove global continuation through \(S\). Since \(S\) was arbitrary, the uncut strong scalar path is global and unique.

For (7), fix a physical horizon \(T\), and choose \(P>2aT+1\). While the clip is inactive, the recovered original variables satisfy the exact loss dissipation identity, so \(\|r\|_2\le\sqrt2a\). Hence

\[
|\dot w|\le |r_1|+|r_2|\le2a,\qquad |w(t)|\le2at<P.
\]

The readout cannot reach the clipping threshold. The middle-weight velocity obeys \(\|\dot W\|_{\rm HS}\le2a\|w\|_2\le4a^2t\), and \(\dot\xi_a\) is bounded in \(L^2\) by the already bounded residual, action, and readout norms. These estimates rule out finite-time state escape before \(T\). This constructs the unique strong physical flow through every finite \(T\), with no assumption of residual symmetry.

### 11.2 The Gaussian width limit checks every fixed-program hypothesis

The initialized first-layer root tuple is

\[
(\xi_1(0),\xi_2(0))=(\zeta(G_1),\zeta(G_2)),
\qquad G_1,G_2\ \text{independent }N(0,1).
\]

It is iid across neurons, independent of \(W_0\), and has every finite moment. III.F.1 explicitly permits arbitrary iid root tuples with finite second moment; root tuples need not themselves be obtained by globally Lipschitz coordinate instructions. Thus the unbounded derivative of \(\zeta\) is not a violation of that theorem.

Apply III.F.1–7 with two layer types, this root tuple, a zero second-layer readout root, and one initialized matrix with entries \(N(0,1/n)\). The matrix and its transpose are reused exactly. The theorem constructs common generated layer spaces, a bounded action \(\|W_0\|_{\rm op}\le10\), and its actual adjoint, with deterministic limits of all fixed-program joint laws and contractions.

For a fixed Euler mesh of (6) or its readout-clipped version, every coordinate instruction is globally \(C^1\) with bounded first derivatives: \(\psi,\tanh\), the clipped readout times the top gate, and linear combinations. The learned matrix does not require a new random-matrix instruction. Unroll its rank-one updates:

\[
W_k v=W_0v+\frac{\Delta}{2}
 \sum_{j<k,b}\sigma_b b_{j,b}\langle u_{j,b},v\rangle,
\]

with the corresponding transposed identity. Thus every current action uses only the original Gaussian matrix, its transpose, scalar contractions, and linear combinations. III.F.6 explicitly handles such causal scalar feedback, including coefficients multiplying unbounded vectors.

For (7), the additional residuals are contractions \(\langle w,h_a\rangle-y_a\), again permitted causal feedback. On any fixed horizon use the readout clip already described. No division by a residual is used in this finite program.

The transformed ODE's norm bounds and Lipschitz constants give an Euler error \(C_S\Delta\) for (6), or \(C_T\Delta\) for (7), uniform over width on the event \(\|W_0\|_{\rm op}\le10\) and bounded initial normalized root norms. Both events have probability tending to one by III.F.2 and the iid root law of large numbers. A fixed mesh has finitely many steps, so III.F applies directly. First send width to infinity at that fixed mesh, then refine the mesh. The same Euler estimate on the common population spaces identifies the deterministic strong ODE just constructed.

This proves compact-time convergence in probability of predictions, loss, and all same-layer contractions needed for the readout-plus-middle kernel. Uniformity in time follows by a finite time net and the common norm/speed bounds. One may include both scalar and physical Euler programs in the same countable generated language. There is no application of the fixed-program theorem to a transcript whose length grows with width.

### 11.3 Symmetry, scalar fitting, and the endpoint margin

Exchange of the two independent root coordinates, together with \(w\mapsto-w\), preserves the finite initialized law and both vector fields. Since their prediction and kernel limits have just been proved deterministic, the population physical path satisfies \(f_2=-f_1\), and the population readout-plus-middle kernel has equal diagonal entries. The same identities hold for the scalar path. This inference concerns the full joint limit; it does not impose a finite neuron pairing.

Set

\[
q_1=\mathbb E[\tanh^2G],\qquad
q_2=\mathbb E[\tanh^2(\sqrt{q_1}G)],\qquad G\sim N(0,1).
\]

Both numbers are strictly positive. The initial first features on the two orthogonal inputs are independent and centered. The finite-program Gaussian forward calculation gives independent top preactivations of variance \(q_1\), so the scalar initial contrast norm is

\[
q_0=\|h_-(0)\|_2^2=q_2/2>0.
\]

Section 2 applies to the constructed strong scalar path and gives a unique target endpoint \(s_*\le a/q_0\). The physical population path is the scalar path under \(\dot s=2(a-g)\): substitution verifies (7), and its strong uniqueness identifies the two paths. In particular,

\[
\mathcal L_\infty(t)\le a^2e^{-4q_0t},\qquad
2\int_0^\infty\sqrt{\mathcal L_\infty(t)}\,dt=s_*<\infty.
\]

For the endpoint common feature one can use an even simpler coordinate than Section 10. Let \(c=\xi_1+\xi_2\). By (6),

\[
c'=B_-,\qquad
|u_+|=\tfrac12|\psi(\xi_1)-\psi(-\xi_2)|\le|c|/2.
\]

On \(0\le s\le s_*\), put \(S=s_*\) and \(M=10+S^2/2\). Then

\[
\|c'\|_2\le2SM^2\|u_+\|_2\le SM^2\|c\|_2,
\qquad
\|c(s)\|_2\ge\|c(0)\|_2e^{-SM^2s}>0.
\]

The initial norm is positive because the independent centered roots \(\zeta(G_1),\zeta(G_2)\) have positive variance. Since \(\psi\) is odd and injective, \(u_+=0\) would imply \(c=0\). Thus \(u_+(s_*)\ne0\). Section 4 proves that the endpoint readout-plus-middle kernel is positive definite. Call its least eigenvalue \(\kappa_*>0\).

All endpoint fields are strong limits in the transformed state space. The readout stays pointwise bounded by \(S\), so their readout-plus-middle kernel is continuous through the endpoint. No first-layer backward moment bound is required.

### 11.4 Uniform finite-width capture uses only a fixed physical time

Here is an explicit version of Section 6 for the two kernel blocks used above. At a finite snapshot \(T\), suppose

\[
\|w(T)\|_\infty\le p,\quad\|W(T)\|_{\rm op}\le b,\quad
K_{\rm readout+middle}(T)\succeq\lambda I_2.
\]

Write \(s=2\int_T^t\sqrt{\mathcal L(v)}\,dv\), and define

\[
\begin{aligned}
M_p(s)&=ps+s^2/2,\\
\alpha(s)&=\frac1{\sqrt2}[bM_p(s)+M_p(s)^2/2],\\
\delta(s)&=\sqrt2 M_p(s)+b\alpha(s),\\
\chi(s)&=\sqrt2s+2p\delta(s),\\
J(s)&=\bigl[\delta(s)^2+(p\alpha(s)+\chi(s))^2\bigr]^{1/2}.
\end{aligned}
\]

The exact velocity bounds give normalized first-feature displacement at most \(\alpha(s)\), top-feature displacement at most \(\delta(s)\), and upper-backward displacement at most \(\chi(s)\). For the last assertion split

\[
\Delta b_a=\Delta w\,\operatorname{sech}^2z_a
+w(T)[\operatorname{sech}^2z_a-\operatorname{sech}^2z_a(T)],
\]

and use \(|\Delta\operatorname{sech}^2z_a|\le2|\Delta h_a|\).
The rank-one difference bound then shows that the concatenated readout-plus-middle tangent feature matrix changes in operator norm by at most \(J(s)\). These estimates are the exact moving-feature bounds, including the motion of \(A\).

Since \(J(0)=0\), there is a positive width-independent residual radius such that

\[
J\!\left(\frac{4\sqrt2\|r(T)\|_2}{\lambda}\right)
<\frac{\sqrt\lambda}{2}.                                \tag{8}
\]

A first-exit argument on the least singular value now gives

\[
K_{\rm readout+middle}(t)\succeq(\lambda/4)I_2,\qquad
\mathcal L_n(t)\le\mathcal L_n(T)e^{-\lambda(t-T)/2}
\quad(t\ge T).
\]

Indeed while this lower bound holds the full kernel is at least as large, and loss decay bounds the remaining accumulated residual by \(4\sqrt2\|r(T)\|_2/\lambda\), strictly below the exit boundary by (8).

To enter this basin, take \(p=s_*+1\), \(b=10+p^2/2\), and \(\lambda=\kappa_*/2\). Choose a fixed, sufficiently large physical \(T\) so that the population readout-plus-middle kernel has least eigenvalue larger than \(3\kappa_*/4\), and the population residual is small enough to satisfy (8) with a strict margin. Compact-time loss convergence gives

\[
2\int_0^T\sqrt{\mathcal L_n(t)}\,dt
\longrightarrow
2\int_0^T\sqrt{\mathcal L_\infty(t)}\,dt\le s_*
\]

in probability. The elementary inequality
\(|\sqrt u-\sqrt v|\le\sqrt{|u-v|}\) justifies this step from uniform loss convergence. The exact finite readout bound gives \(\|w_n(T)\|_\infty\le p\), and the exact middle displacement bound gives \(\|W_n(T)\|_{\rm op}\le b\), jointly with probability tending to one. The previously proved kernel and prediction convergence supply the remaining snapshot conditions. Equation (8) then controls every later finite-width time, proving the candidate theorem.

Only one deterministic finite time is used for the width approximation. Exact finite-width inequalities control the infinite future. This is stronger than merely showing \(\mathcal L_n(\infty)\to0\) in probability.

## 12. Scope after the pair construction

The orthogonal-pair theorem in Section 11 is now a complete candidate proof using the maintained fixed-program/common-space theorem with checked hypotheses. It requires independent review before being treated as established. No extension to nonorthogonal inputs has been proved.

For \(-1<\rho<0\), Section 10 removes the endpoint common-feature extinction obstacle once a strong scalar path is constructed. The natural-coordinate equations for a nonzero correlation contain cross terms

\[
\xi_a'=\frac12\sum_b(x_a^\top x_b)\sigma_b
\frac{\operatorname{sech}^2(Ax_b)}
     {\operatorname{sech}^2(Ax_a)}\,B_b.
\]

These ratios are unbounded. The open-\(L^2\) Lipschitz argument used in Section 11 therefore does not extend directly. Bounded \(L^2\) action norms do not supply \(L^p\) bounds for adaptive reverse queries, and treating a reused initialized Gaussian matrix as independent of its trained query would omit the response terms.

This is the remaining exact obstruction in this route. It is not evidence of nonfitting. The original arbitrary mixed-label, broadly nonorthogonal multi-input question remains open.

## 13. General orthogonal datasets, arbitrary amplitude, and open label classes

This section supersedes the pair-only scope of Section 11. The following extension was proposed by the supervisor and checked against the exact transformed equations.

**General candidate theorem, pending independent review.** Fix \(m\ge2\), \(d\ge m\), orthonormal input columns \(X^\top X=I_m\), any \(a>0\), and any sign vector \(\sigma\in\{-1,1\}^m\). Let \(y=a\sigma\). Under the exact canonical Gaussian initialization and gradient flow of Section 1,

\[
\Pr\!\left(\lim_{t\to\infty}\mathcal L_n(t)=0\right)\to1.
\]

There is a deterministic \(c>0\), independent of width, for which, with probability tending to one,
\(\mathcal L_n(t)\le\mathcal L_n(0)e^{-ct}\) for all \(t\ge0\).
Moreover, there is an open neighborhood \(\mathcal U_{a,\sigma}\subset\mathbb R^m\) of \(a\sigma\) such that the same exact-fitting conclusion holds for every fixed \(y\in\mathcal U_{a,\sigma}\). The neighborhood may be chosen to preserve the signs of all label coordinates. Its radius is not asserted to cover arbitrary label ratios.

### 13.1 Sign absorption and strong construction

The network is odd in its input because both hidden activations are odd and there are no biases. Replace \(x_a\) by \(\sigma_a x_a\). Its prediction becomes \(\sigma_a f_a\); the loss against labels \(a\mathbf1_m\) is identically the original loss against \(a\sigma\), for every parameter state. Thus their parameter gradient fields are exactly the same, and the new input columns remain orthonormal. It suffices to prove the result for \(y=a\mathbf1_m\).

Use the natural coordinates \(\xi_a=\zeta(Ax_a)\) and \(\psi\) from Section 11, and define

\[
g=\frac1m\sum_{a=1}^m f_a,\qquad
\bar h=\frac1m\sum_{a=1}^m h_a.
\]

The exact scalar-ascent equations are

\[
\xi_a'=\frac1mW^*b_a,\qquad
W'=\frac1m\sum_{a=1}^m b_a\otimes u_a,\qquad
w'=\bar h.                                               \tag{9}
\]

The actual physical equations, without any imposed permutation symmetry, are

\[
\dot\xi_a=-\frac2m r_aW^*b_a,\qquad
\dot W=-\frac2m\sum_a r_a b_a\otimes u_a,\qquad
\dot w=-\frac2m\sum_a r_a h_a.                            \tag{10}
\]

For every fixed \(m\), the open-\(L^2\) clipping and Picard argument in Section 11.1 applies verbatim to the tuple \((\xi_1,\ldots,\xi_m)\). Scalar ascent has \(\|w\|_\infty\le s\), \(\|W\|_{\rm op}\le10+s^2/2\), and
\(\|\xi_a'\|_2\le s(10+s^2/2)/m\). For physical flow from these labels, loss dissipation gives \(\|r\|_2\le a\sqrt m\), hence
\(|\dot w|\le(2/\sqrt m)\|r\|_2\le2a\). These bounds remove the readout clip on each chosen finite horizon and give global strong continuation.

The Gaussian root tuple consists of \(m\) independent variables \(\zeta(G_a)\). III.F.1 permits any fixed finite tuple of iid-per-neuron roots with finite second moments. Each transformed Euler program remains a fixed finite program of globally Lipschitz \(C^1\) coordinate instructions, one reused Gaussian matrix and its transpose, and causal contractions. The same width-independent Euler estimate and fixed-program limit therefore identify both flows and their readout-plus-middle kernel observations on every fixed compact horizon. This argument also works for every fixed nonsymmetric label vector \(y\), although scalar fitting below uses the equal-label symmetry.

### 13.2 Population fitting and all pairwise feature differences

The initialized root law is invariant under every permutation of the \(m\) sample coordinates. The equal-label scalar and physical equations respect this symmetry. Their now-identified deterministic population predictions are therefore equal, \(f_a=g\), and every deterministic population sample-kernel block commutes with every sample permutation.

The initial top features are independent centered copies with second moment \(q_2\) defined in Section 11.3. Consequently

\[
q_0=\|\bar h(0)\|_2^2=q_2/m>0.
\]

The scalar argument of Section 2 applies with \(h_-\) replaced by \(\bar h\). It yields
\(\|\bar h(s)\|_2^2\ge q_0\), a unique scalar endpoint \(g(s_*)=a\), and \(s_*\le a/q_0=ma/q_2\). Permutation symmetry gives the exact physical clock \(\dot s=2(a-g)\); strong uniqueness of (10) identifies this reparameterization with the physical population path. Thus

\[
\mathcal L_\infty(t)\le a^2e^{-4q_0t},\qquad
2\int_0^\infty\sqrt{\mathcal L_\infty(t)}\,dt=s_*.
\]

Fix distinct samples \(a,b\), and set \(c_{ab}=\xi_a-\xi_b\). Equation (9), \(\|w\|_\infty\le S\), and the identities
\(|\operatorname{sech}^2z_a-\operatorname{sech}^2z_b|
\le2|h_a-h_b|\) give, on \(0\le s\le S\),

\[
\begin{aligned}
\|c_{ab}'\|_2
&\le\frac{\|W\|_{\rm op}}m\|b_a-b_b\|_2\\
&\le\frac{2S\|W\|_{\rm op}}m\|h_a-h_b\|_2\\
&\le\frac{2S\|W\|_{\rm op}^2}m\|u_a-u_b\|_2\\
&\le\frac{2SM^2}m\|c_{ab}\|_2,
\qquad M=\sup_{s\le S}\|W(s)\|_{\rm op}.
\end{aligned}
\]

Hence \(\|c_{ab}(s)\|_2\ge\|c_{ab}(0)\|_2e^{-2SM^2s/m}>0\). The initial norm is positive for independent nondegenerate roots. Since \(\psi\) is injective, \(u_a-u_b\ne0\) at every finite feature time.

### 13.3 Positive endpoint kernel in every sample direction

Let \(K_{\rm R+W}\) denote only the readout and middle-weight blocks. Permutation symmetry gives

\[
K_{\rm R+W}=\alpha I_m+\beta\mathbf1_m\mathbf1_m^\top
\]

for scalar coefficients \(\alpha,\beta\); this \(\beta\) is unrelated to Section 10's coordinate exponent. Its eigenspaces are the common direction and the subspace of vectors with zero coordinate sum.

The common direction is positive because its readout quadratic form is
\[
\frac1{m^2}\mathbf1_m^\top K_{\rm readout}\mathbf1_m
=\|\bar h\|_2^2\ge q_0.
\]

At every \(s>0\), scalar coercivity gives \(g(s)\ge q_0s>0\), so \(w\ne0\). To check any contrast, choose \(a\ne b\). If \(h_a-h_b\ne0\), the readout gradient of \(f_a-f_b\) is already nonzero. Otherwise strict monotonicity of tanh gives \(z_a=z_b\), hence \(b_a=b_b=w\operatorname{sech}^2z_a\ne0\). The middle-weight gradient of \(f_a-f_b\) is then

\[
b_a\otimes(u_a-u_b)\ne0,
\]

because the first-feature difference was proved nonzero. Therefore
\((e_a-e_b)^\top K_{\rm R+W}(e_a-e_b)>0\), which gives \(\alpha>0\). Both eigenspaces are positive, so
\[
K_{\rm R+W}(s)\succ0\qquad(s>0).
\]

At \(s=0\), the readout kernel is \(q_2 I_m\), also positive definite. Strong continuity of the fields, with the bounded readout on \(0\le s\le s_*\), makes this kernel continuous. Compactness therefore gives
\[
\kappa=\min_{0\le s\le s_*}\lambda_{\min}
      \bigl(K_{\rm R+W}(s)\bigr)>0.
\]

Only deterministic population permutation symmetry is used here. Individual finite networks need not have equal predictions or equal diagonal kernel entries.

### 13.4 General-\(m\) capture and open label neighborhoods

The capture proof in Section 11.4 extends with

\[
\begin{aligned}
M_p(s)&=ps+s^2/2,\\
\alpha(s)&=\frac1{\sqrt m}[bM_p(s)+M_p(s)^2/2],\\
\delta(s)&=\sqrt mM_p(s)+b\alpha(s),\\
\chi(s)&=\sqrt ms+2p\delta(s),\\
J(s)&=[\delta(s)^2+(p\alpha(s)+\chi(s))^2]^{1/2}.
\end{aligned}
\]

Orthogonality gives \(\|X\|_{\rm op}=1\), which explains the factor \(1/\sqrt m\) in the first-feature bound. If \(K_{\rm R+W}(T)\succeq\lambda I_m\) and

\[
J\!\left(\frac{4\sqrt m\|r(T)\|_2}{\lambda}\right)
<\frac{\sqrt\lambda}{2},
\]

then the exact full finite-width gradient flow satisfies

\[
\mathcal L_n(t)\le\mathcal L_n(T)e^{-\lambda(t-T)/m}
\qquad(t\ge T),
\]

and its limiting loss is zero. The proof uses the full loss dissipation and only the two indicated blocks as a kernel lower bound.

Take \(p=s_*+1\), \(b=10+p^2/2\), and \(\lambda\) below the least endpoint eigenvalue. Choose a single sufficiently late population physical time \(T\) with a strict capture margin. The compact-time convergence proved above and the exact finite accumulated-residual bounds put the actual finite network into this basin with probability tending to one.

The same compact-time kernel convergence and the margin \(\kappa\) also give \(K_{\rm R+W,n}(t)\succeq(\kappa/2)I_m\) simultaneously for \(0\le t\le T\), with probability tending to one. Hence the loss decays on that interval at rate \(2\kappa/m\). Combining this with the capture rate \(\lambda/m\) proves the stated all-time exponential estimate with
\[
c=\frac1m\min\{2\kappa,\lambda\}>0.
\]
As in Section 11.4, the width limit is used only through the single fixed horizon \(T\); the entire later interval is controlled by exact finite-width inequalities.

Finally, fix such a capture time for \(y_0=a\mathbf1_m\), taking conservative strict bounds on \(p,b,\lambda\) and the residual radius. On this finite horizon, the transformed physical vector field (10) is locally Lipschitz jointly in its state and in \(y\), after the fixed readout clip. For labels near \(y_0\), the bounds \(\|r\|_2\le\|y\|_2\) and \(\|w(t)\|_\infty\le2t\|y\|_2/\sqrt m\) make the same clip inactive. Subtracting the integral equations and applying Gronwall proves strong continuous dependence on \(y\). Predictions and \(K_{\rm R+W}\) therefore vary continuously as well.

The strict capture inequalities persist for every \(y\) in a sufficiently small open neighborhood of \(y_0\). For each such fixed label vector, the already-proved compact-time Gaussian width limit transfers that snapshot to the actual finite network, after which deterministic capture proves exact fitting. Undoing the exact sign absorption gives \(\mathcal U_{a,\sigma}\). This is a neighborhood of label vectors, not a neighborhood of input geometries.

## 14. Final claim boundary for review

Sections 11 and 13 provide a complete candidate proof, using the maintained and fully inspected Gaussian-program theorem, for orthogonal data with arbitrary fixed equal label magnitudes and for an open label neighborhood around each such vector. The actual activation is tanh at both layers, all parameters train with the prescribed mobilities, the hidden initialization is iid Gaussian, and the readout is exactly zero. No frozen-feature substitution, simulation, paired finite initialization, or positive-probability-only Gaussian support argument appears.

Section 10 separately proves a tail-free endpoint-diversity lemma for obtuse nonorthogonal pairs, conditional on a constructed strong scalar population path. The missing construction and identification for nonorthogonal tanh dynamics are not supplied by the orthogonal theorem. Arbitrary mixed-label ratios on arbitrary fixed nonorthogonal data remain unresolved, as does the requested strong negative alternative.
