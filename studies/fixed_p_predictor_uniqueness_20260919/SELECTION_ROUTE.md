# Anchored variational selection with a noisy continuous optimizer

Status: frozen independent prompt-only construction, 2026-09-19, before cross-route comparison. This is a conditional abstract theorem, proved below without experiments. The supplied abstract feature-map assumptions are the only scientific inputs. Verification for a particular canonical feature map is outside this report's scope.

## Claim and contract

For every fixed label vector and every locally surjective feature map satisfying the assumptions below, one can choose an explicit finite anchoring coefficient and a current-state noisy optimizer, initialized at the prescribed hidden state and zero readout, with all of the following properties:

1. There is a unique selected fitted state in a specified neighborhood. Its existence is proved; the optimizer is not supplied that state.
2. Hidden variables optimize a data-dependent objective and need not remain at initialization.
3. Every admissible realization of a nontrivial, time-varying random forcing converges to the same selected state. Loss tends to zero, and passive predictions converge locally uniformly under the stated continuity hypothesis.
4. The readout equation includes the exact transport caused by moving features.

This is an optimizer-design result. The selected state depends on the anchor, its strength, and the chosen readout norm. It is not a uniqueness theorem for the unmodified gradient flow of training loss. Noise is a bounded continuous random forcing with a decaying envelope, rather than an Itô diffusion.

The state spaces may be infinite-dimensional real Hilbert spaces. No finite-dimensional compactness, width limit, discretization, inaccessible endpoint, future sample path, or experimental input is used. The only finite matrix inverses are current-state training Gram matrices of size equal to the number of training coordinates.

## 1. Assumptions and computable constants

Let \(E,H\) be real Hilbert spaces, \(m\geq1\), \(h_0\in E\), and \(Y\in\mathbb R^m\). The hidden state \(h\), which may be the pair \((w,M)\), determines

\[
A_h\in\mathcal L(H,\mathbb R^m),\qquad K_h=A_hA_h^*.
\]

Assume \(A\) is continuously Fréchet differentiable on an open neighborhood containing \(B_r(h_0)\), for a known \(r>0\), and that throughout this ball

\[
\|DA_h\|\leq d,\qquad
\|DA_h-DA_g\|\leq \ell\|h-g\|.
\]

The derivative norm is from \(E\) into \(\mathcal L(H,\mathbb R^m)\). These are local \(C^{1,1}\) bounds, not conclusions about a particular network. Assume \(K_{h_0}\) is positive definite, and write

\[
\lambda_0=\lambda_{\min}(K_{h_0})>0,\quad
s_0=\sqrt{\lambda_0},\quad a_0=\|A_{h_0}\|,\quad y=\|Y\|.
\]

Choose

\[
R=\begin{cases}
\min\{r/2,s_0/(2d)\},&d>0,\\
r/2,&d=0,
\end{cases}
\qquad a=a_0+dR,\qquad \lambda=\lambda_0/4.
\]

All subsequent hidden states lie in the closed ball \(\mathcal B=\overline B_R(h_0)\). For \(h\in\mathcal B\), the fundamental theorem of calculus on the segment from \(h_0\) to \(h\) gives

\[
\|A_h-A_{h_0}\|\leq d\|h-h_0\|,\qquad \|A_h\|\leq a.
\]

For every \(u\in\mathbb R^m\),

\[
\|A_h^*u\|\geq\|A_{h_0}^*u\|-dR\|u\|
\geq(s_0-dR)\|u\|\geq\tfrac12s_0\|u\|.
\]

Consequently \(K_h\succeq\lambda I\) throughout \(\mathcal B\). Define

\[
P_h=A_h^*K_h^{-1}:\mathbb R^m\longrightarrow H,
\qquad q(h)=\tfrac12Y^TK_h^{-1}Y.
\]

Thus \(A_hP_h=I\), \(\|P_h\|\leq\lambda^{-1/2}\), and \(P_hY\) is the minimum-norm readout interpolating \(Y\) at the current hidden state.

The following explicit bounds will suffice:

\[
G=\frac{ad\,y^2}{\lambda^2},
\qquad
L_q=y^2\left(\frac{d^2+a\ell}{\lambda^2}
+\frac{4a^2d^2}{\lambda^3}\right),
\qquad
C_P=\frac d\lambda+\frac{2a^2d}{\lambda^2}.
\tag{1}
\]

They satisfy, for \(h,g\in\mathcal B\),

\[
\|\nabla q(h)\|\leq G,\quad
\|\nabla q(h)-\nabla q(g)\|\leq L_q\|h-g\|,\quad
\|P_h-P_g\|\leq C_P\|h-g\|.
\tag{2}
\]

Here is the derivation, including the constants. Differentiating \(K\) gives

\[
DK_h[v]=(DA_h[v])A_h^*+A_h(DA_h[v])^*.
\]

Hence \(\|DK_h\|\leq 2ad\), while subtracting this expression at \(h\) and \(g\) gives

\[
\|DK_h-DK_g\|\leq(2d^2+2a\ell)\|h-g\|.
\]

Set \(u_h=K_h^{-1}Y\). The inverse identity
\(K_h^{-1}-K_g^{-1}=K_h^{-1}(K_g-K_h)K_g^{-1}\) gives

\[
\|u_h\|\leq y/\lambda,\qquad
\|u_h-u_g\|\leq(2ad\,y/\lambda^2)\|h-g\|.
\]

For a direction \(v\in E\),

\[
Dq(h)[v]= -\tfrac12\langle u_h,DK_h[v]u_h\rangle
=-\langle u_h,(DA_h[v])P_hY\rangle.
\tag{3}
\]

The first expression bounds the gradient by \(ad\,y^2/\lambda^2\). When subtracting it at two hidden states, the change in \(DK\) contributes at most
\((d^2+a\ell)y^2\|h-g\|/\lambda^2\); the two changes in \(u\) together contribute at most
\(4a^2d^2y^2\|h-g\|/\lambda^3\). This proves the first two bounds in (2). Finally,

\[
DP_h[v]z=(DA_h[v])^*K_h^{-1}z
-A_h^*K_h^{-1}DK_h[v]K_h^{-1}z,
\tag{4}
\]

whose norm is at most \(C_P\|v\|\|z\|\). Integration along a segment proves the third bound in (2).

## 2. A unique fitted target, without an endpoint oracle

Choose any fixed hidden forcing bound \(\eta>0\), readout forcing bound \(\rho>0\), and time scale \(\alpha>0\). Set

\[
\mu=L_q+\alpha+\frac{G+\eta}{R},\qquad
\kappa=\mu-L_q=\alpha+\frac{G+\eta}{R}>\alpha.
\tag{5}
\]

Consider the explicit constrained variational problem

\[
\min_{\substack{h\in\mathcal B,\ c\in H\\ A_hc=Y}}
J(h,c),\qquad
J(h,c)=\frac\mu2\|h-h_0\|^2+\frac12\|c\|^2.
\tag{6}
\]

For each feasible pair, write \(c=P_hY+n\). Then \(A_hn=0\), and
\(\langle P_hY,n\rangle=\langle K_h^{-1}Y,A_hn\rangle=0\). Therefore

\[
J(h,c)=F(h)+\tfrac12\|n\|^2,
\qquad F(h)=\frac\mu2\|h-h_0\|^2+q(h).
\tag{7}
\]

It remains to minimize \(F\). The map

\[
T(h)=h_0-\mu^{-1}\nabla q(h)
\]

sends \(\mathcal B\) into its interior, because \(\|T(h)-h_0\|\leq G/\mu<R\). Its Lipschitz constant is at most \(L_q/\mu<1\). To spell out the existence argument in an infinite-dimensional ball: starting with any \(h^{(0)}\in\mathcal B\), iterate \(h^{(j+1)}=T(h^{(j)})\). Successive differences are bounded by a geometric sequence. Thus the sequence is Cauchy, has a limit in the complete closed ball, and continuity makes that limit a fixed point. The contraction inequality makes the fixed point unique. Call it \(h_*\). It satisfies

\[
\nabla F(h_*)=0,\qquad \|h_*-h_0\|\leq G/\mu<R.
\tag{8}
\]

The gradient bound (2) gives

\[
\langle\nabla F(h)-\nabla F(g),h-g\rangle
\geq\kappa\|h-g\|^2.
\tag{9}
\]

Integrating \(\langle\nabla F(h_*+s(h-h_*)),h-h_*\rangle\) over \(0\leq s\leq1\) yields

\[
F(h)-F(h_*)\geq\tfrac\kappa2\|h-h_*\|^2.
\]

Consequently (6) has exactly one minimizer,

\[
(h_*,c_*),\qquad c_*=P_{h_*}Y,
\]

and it interpolates the labels exactly. This is existence and uniqueness within the explicitly selected ball; no claim about all distant hidden states is made. The contraction argument also supplies an endpoint-free deterministic procedure for computing the minimizer, although the continuous optimizer below does not need to run that procedure separately.

## 3. Noisy optimizer and exact feature transport

Let \(\xi:[0,\infty)\to E\) and \(\zeta:[0,\infty)\to\mathbb R^m\) be arbitrary continuous functions satisfying

\[
\|\xi(t)\|\leq1,\qquad\|\zeta(t)\|\leq1.
\tag{10}
\]

They will be random, but every assertion below holds for every pair of functions satisfying (10). In coordinates \((h,z)\in\mathcal B\times\mathbb R^m\), solve

\[
\begin{aligned}
\dot h&=-\nabla F(h)+\eta e^{-\alpha t}\xi(t),& h(0)&=h_0,\\
\dot z&=-2(z-Y)+\rho e^{-\alpha t}\zeta(t),&z(0)&=0,\\
c(t)&=P_{h(t)}z(t).
\end{aligned}
\tag{11}
\]

For uncomplicated explicit rates, choose \(0<\alpha<2\); \(\alpha=1\) is a concrete valid choice. The factor \(2\) is the gradient factor for the prescribed unhalved loss \(\|z-Y\|^2\). At every time,

\[
A_{h(t)}c(t)=z(t),\qquad c(0)=0.
\tag{12}
\]

There is genuine continuous temporal randomness, for example by fixing unit vectors \(e\in E\), \(v\in\mathbb R^m\), taking two independent standard real Brownian motions \(B_1,B_2\), and setting

\[
\xi(t)=\sin(B_1(t))e,\qquad \zeta(t)=\sin(B_2(t))v.
\tag{13}
\]

Use the canonical sample space of pairs of continuous paths starting at zero. Then (10) holds at every sample point, not just outside a probability-zero set. Equations (11) are ordinary differential equations with continuous random coefficients. At positive times their forcing distributions are nontrivial. If \(E=\{0\}\), omit the hidden forcing and use the nontrivial readout forcing; a claim of hidden learning would then have no content.

The physical readout derivative is not merely \(P_h\dot z\). With

\[
b_h=-\nabla F(h)+\eta e^{-\alpha t}\xi(t),
\]

the full equation is

\[
\begin{aligned}
\dot c={}&(DA_h[b_h])^*K_h^{-1}z
-A_h^*K_h^{-1}DK_h[b_h]K_h^{-1}z\\
&+P_h\big[-2(z-Y)+\rho e^{-\alpha t}\zeta(t)\big],
\qquad z=A_hc.
\end{aligned}
\tag{14}
\]

The first two terms are \(DP_h[b_h]z\); they are required when the hidden state moves. Differentiating \(A_hP_h=I\) gives
\((DA_h[b_h])P_h+A_hDP_h[b_h]=0\). Substituting (14) into
\(\dot z=(DA_h[b_h])c+A_h\dot c\) therefore cancels the feature-motion terms and recovers the second equation of (11) exactly.

All coefficients in (11) or (14) use the current hidden state, current readout, known labels, local constants, chosen hyperparameters, clock, and current noise. In particular, neither \(h_*\), \(c_*\), nor future randomness appears on their right-hand sides. The known clock can be appended as a state coordinate. With construction (13), appending the current two Brownian coordinates makes the system restartable with future Brownian increments.

There is also a precise gradient interpretation. Let

\[
\mathcal M=\{(h,P_hz):h\in\mathcal B,z\in\mathbb R^m\}.
\]

The coordinate map \((h,z)\mapsto(h,P_hz)\) is one-to-one and has inverse \((h,c)\mapsto(h,A_hc)\) on this set. The product-coordinate potential

\[
V(h,z)=F(h)+\|z-Y\|^2
\tag{15}
\]

has the unique minimizer \((h_*,Y)\). Its noiseless product-Hilbert gradient flow is precisely (11) without the forcing. On the interior of \(\mathcal M\), the corresponding metric on tangent vectors is

\[
g_{(h,c)}((\delta h,\delta c),(\widetilde h,\widetilde c))
=\langle\delta h,\widetilde h\rangle_E
+\left\langle DA_h[\delta h]c+A_h\delta c,
DA_h[\widetilde h]c+A_h\widetilde c\right\rangle_{\mathbb R^m}.
\tag{16}
\]

It is positive definite on these tangent vectors because it is the product norm in the one-to-one coordinates. Thus the changed metric and the readout constraint are explicit, and (14) contains the entire coordinate transport. No assertion of equality with the original Euclidean gradient is implicit.

## 4. Global existence and convergence for every forcing path

At a boundary point \(\|h-h_0\|=R\), the outward radial velocity obeys

\[
\left\langle\frac{h-h_0}{R},\dot h\right\rangle
\leq-\mu R+G+\eta
=-(L_q+\alpha)R<0.
\tag{17}
\]

Thus a solution starting at \(h_0\) cannot exit the ball. The vector field is continuous in time and locally Lipschitz in \(h\), and \(\nabla F\) has the uniform Lipschitz bound \(\mu+L_q\) on the ball. The usual local Hilbert-space ODE theorem applies: a continuous time-dependent vector field locally uniformly Lipschitz in the state has a unique local continuously differentiable solution, obtained by the contraction of its integral map on a sufficiently short interval. The required bounds here are exactly those above.

For completeness, global continuation does not rely on a bounded ball being compact. On the invariant ball, \(\|\dot h\|\leq\mu R+G+\eta\). If a maximal existence time were finite, this bound would make \(h(t)\) Cauchy as it approached that time. Its limit belongs to the complete closed ball, where \(K\) is still positive definite and the local vector field extends to an open neighborhood. Local existence from the limit extends the solution, a contradiction. The linear equation for \(z\) has a unique global solution, and (4) makes \(c=P_hz\) continuously differentiable. This establishes global well-posedness for every pair of paths in (10).

Subtract \(\nabla F(h_*)=0\) from the hidden equation. By (9),

\[
\frac12\frac d{dt}\|h-h_*\|^2
\leq-\kappa\|h-h_*\|^2
+\eta e^{-\alpha t}\|h-h_*\|.
\]

Scalar comparison, applied where the norm is nonzero and continued by its upper one-sided derivative at zero, yields

\[
\begin{aligned}
\|h(t)-h_*\|
&\leq e^{-\kappa t}\|h_0-h_*\|
+\eta\int_0^te^{-\kappa(t-s)}e^{-\alpha s}\,ds\\
&\leq \frac G\mu e^{-\kappa t}
+\frac\eta{\kappa-\alpha}
\big(e^{-\alpha t}-e^{-\kappa t}\big).
\end{aligned}
\tag{18}
\]

For \(r_z=z-Y\), direct integration gives

\[
r_z(t)=-e^{-2t}Y+
\rho\int_0^te^{-2(t-s)}e^{-\alpha s}\zeta(s)\,ds.
\]

Because \(0<\alpha<2\),

\[
\|r_z(t)\|\leq y e^{-2t}
+\frac\rho{2-\alpha}\big(e^{-\alpha t}-e^{-2t}\big).
\tag{19}
\]

Consequently the original training loss satisfies

\[
\mathcal L(h(t),c(t))=\|A_{h(t)}c(t)-Y\|^2
=\|r_z(t)\|^2\longrightarrow0.
\tag{20}
\]

Using (2),

\[
\|c(t)-c_*\|
\leq\lambda^{-1/2}\|r_z(t)\|
+C_Py\|h(t)-h_*\|\longrightarrow0.
\tag{21}
\]

Bounds (18)–(21) do not depend on the realized forcing paths. They prove strong convergence of the entire state to the same deterministic \((h_*,c_*)\), uniformly over the allowed forcing family. This is stronger than an almost-sure endpoint statement for the particular random forcing (13).

To pass to passive predictions, assume that for every compact input set \(X\), \(H_h\) is a bounded \(H\)-valued function on \(X\), and that

\[
\sup_{x\in X}\|H_h(x)-H_{h_*}(x)\|_H\longrightarrow0
\quad\text{as }h\longrightarrow h_*.
\tag{22}
\]

This states precisely the needed uniform-on-compact continuity. With
\(f_t(x)=\langle c(t),H_{h(t)}(x)\rangle\) and
\(f_*(x)=\langle c_*,H_{h_*}(x)\rangle\),

\[
\begin{aligned}
\sup_{x\in X}|f_t(x)-f_*(x)|
\leq{}&\|c(t)-c_*\|\sup_{x\in X}\|H_{h_*}(x)\|\\
&+\|c(t)\|\sup_{x\in X}\|H_{h(t)}(x)-H_{h_*}(x)\|\longrightarrow0.
\end{aligned}
\tag{23}
\]

The readout is bounded by (19) and \(\|P_h\|\leq\lambda^{-1/2}\), so both terms indeed vanish. The predictor limit is deterministic for every allowed forcing path.

## 5. Hidden learning, parameter dependence, and scope limits

**Hidden learning is permitted and can be nonzero.** The drift (3) depends on the labels and on how the feature map changes with the hidden state. In particular,

\[
h_*=h_0\quad\Longleftrightarrow\quad\nabla q(h_0)=0.
\]

With Brownian-based forcing (13), \(\xi(0)=0\); hence \(\dot h(0)=-\nabla q(h_0)\). Whenever this gradient is nonzero, even the initial hidden movement is data dependent. For a concrete scalar check, let \(E=H=\mathbb R\), \(m=1\), \(h_0=0\), and \(A_hc=(a+h)c\) on a ball of radius smaller than \(a>0\). Then

\[
q(h)=\frac{Y^2}{2(a+h)^2},\qquad
\mu h_* = \frac{Y^2}{(a+h_*)^3}.
\]

For \(Y\ne0\), the selected hidden state satisfies \(h_*>0\). The interpolation readout is \(Y/(a+h_*)\). There is no frozen-feature identity in the construction. It would nevertheless be false to promise nonzero hidden movement for every model and label: for example, constant feature maps or zero labels may make the data-dependent hidden gradient vanish.

**The selector is a design choice.** The selected state depends on \(h_0\), \(\mu\), the Hilbert norms, \(A\), and \(Y\); consequently so does its passive predictor. The radius specifies the region in which uniqueness is certified. Changing that radius while keeping \(\mu\) and a common interior stationary point fixed does not change that point. In the explicit safe recipe (5), \(\mu\) also depends on the derivative/Gram bounds, \(R\), \(\alpha\), and the chosen hidden-noise bound \(\eta\). It never depends on the noise realization. The readout-noise amplitude \(\rho\) does not affect the target. One may instead fix any \(\mu>L_q\) with \(\mu R>G+\eta\) and then vary the forcing paths or reduce their amplitudes while retaining the same selector; only the displayed rate formula needs the corresponding relation between \(\mu-L_q\) and \(\alpha\).

**This is not the original gradient flow.** For the unhalved original loss, writing \(r=A_hc-Y\), ordinary product-Hilbert gradient flow would be

\[
\dot c=-2A_h^*r,\qquad
\langle\dot h,v\rangle_E=-2\langle r,(DA_h[v])c\rangle_{\mathbb R^m}.
\]

At \(c=0\), its hidden velocity is zero, whereas the selector flow generally has hidden velocity \(-\nabla q(h_0)\ne0\). At every exact interpolant, the original gradient vanishes, whereas the selector still moves unless the chosen variational condition holds. The construction therefore cannot establish original-gradient-flow endpoint uniqueness, original implicit-bias equivalence, or optimality of the selected predictor for any unmentioned population loss.

**Noise and loss scope.** The noise is nontrivial and continues at all finite times but its envelope tends to zero. Training loss need not decrease monotonically along noisy paths; (19) is the asserted control. Persistent nonvanishing forcing is not covered. Calling (11) an Itô diffusion would be incorrect: its trajectories are continuously differentiable random-ODE trajectories. The all-realizations quantifier refers to the explicitly bounded forcing class (10); it is not a claim for arbitrary unbounded perturbations.

**Implementation and model-verification obligations.** Exact evaluation of \(A_h\), \(DA_h\), Gram inverses, and Hilbert gradients is part of the abstract optimizer. This proves a continuous mathematical construction, not a finite-cost implementation or convergence of a discretization. For a particular canonical model, one must separately verify an appropriate Hilbert domain, local operator-norm \(C^{1,1}\) regularity with usable bounds, positive definite initial Gram, and (22). If a claimed feature map is only pointwise differentiable, loses its Gram gap, or does not control passive predictions in this topology, the corresponding conclusion has not been proved by this report.

## Frozen claim ledger and audit

| Claim | Status and evidence | Limitation |
|---|---|---|
| Explicit uniformly positive Gram neighborhood | Exact under the stated assumptions; singular-value estimate in §1 | Canonical bounds and initial gap remain external verification obligations |
| Unique fitted variational minimizer | Proved within \(\mathcal B\); contraction plus orthogonal readout decomposition in §2 | Depends on the specified selector and its parameters |
| Current-state noisy optimizer with no endpoint oracle | Explicit equations (11), (14) | Uses exact current Gram solves and derivatives |
| Exact moving-feature transport | Identity (4), cancellation following (14) | Omitting either transport term breaks the asserted prediction equation |
| Global existence and identical full-state limit for every allowed path | Proved by (17)–(21) without compactness | Bounded continuous forcing with decaying envelope |
| Locally uniform deterministic passive predictor | Proved by (22)–(23) | Requires the stated passive-feature continuity |
| Nonfrozen data-dependent hidden learning is possible | Exact gradient (3), criterion and scalar example in §5 | Nonzero movement is not universal over degenerate data/maps |
| Identification with original gradient flow | Not claimed; initial-velocity discrepancy is explicit | This bridge would be false in general |
| Canonical-model verification | Outside this scoped input | Must be established independently before specializing the theorem |

The strongest surviving substantive qualification is optimizer dependence: uniqueness is obtained by adding a strictly selecting hidden objective and changing the readout dynamics/metric. The strongest structural checks are satisfied within the contract: the endpoint is obtained from a proven contraction rather than given as an oracle; global existence uses completeness rather than false infinite-dimensional compactness; the physical readout contains full transport; all-path convergence is proved by uniform deterministic bounds; and actual hidden learning is possible. No empirical or canonical-model claim is inferred from these abstract statements.
