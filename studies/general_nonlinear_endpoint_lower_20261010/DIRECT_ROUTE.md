# Direct endpoint sensitivity: exact lemma and remaining gap

This bounded attempt does not prove or disprove the requested endpoint lower
bound. It proves a finite-width endpoint sensitivity lemma, including its rank,
and identifies the additional probabilistic nondegeneracy that this mechanism
would require. No frozen-feature conclusion is substituted for the trained
endpoint.

Scientific inputs were the complete `paper/compact.tex` and
`paper/compact_fitting.tex`. No study history or other agent findings were read.
The canonical-notation, rigorous-proof, and conjecture-investigation
instructions were applied. Everything below is derived directly; no external
theorem about neural-network limits is invoked.

## Target and model

Write $v=x/\sqrt d$, so queries and training directions lie on the unit
sphere. The network is

\[
h^{(1)}(v)=\phi_1(W^{(1)}v),\qquad
h^{(\ell)}(v)=\phi_\ell(W^{(\ell)}h^{(\ell-1)}(v)),\qquad
f_n(v)=n^{-1}w^\top h^{(L)}(v).
\]

All hidden matrices and the readout follow exactly the gradient flow in the
source, with mobilities $(n,1,\ldots,1,n)$, initial readout zero, and independent
Gaussian hidden initialization. Each activation is nonaffine and satisfies the
source strip assumptions. The training directions are pairwise neither parallel
nor antiparallel. The labels are fixed, nonzero, and satisfy the existing cap

\[
Y=\|y\|_2/\sqrt m\le (\gamma/m)\beta^{-30L}.
\]

Let $\mathcal X_\varepsilon$ denote the specified nonempty separated subset of
the sphere. The requested assertion is that some fixed $c,p>0$, allowed to
depend on the entire fixed problem, satisfy, at each sufficiently large width,

\[
\Pr\!\left\{\sup_{v\in\mathcal X_\varepsilon}
 |f_n(\infty,v)-\widetilde f_n(\infty,v)|\ge c/\sqrt n\right\}\ge p.
\]

Missing fitted limits count as failure. The following analysis concerns the
high-probability fitting event supplied by the source.

## Exact endpoint derivative

Use Euclidean mobility coordinates

\[
\vartheta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)
 \in\mathbb R^{N_n},\qquad
N_n=nd+(L-1)n^2+n.
\]

Here matrices are flattened with the Frobenius inner product. Define

\[
F(\vartheta)=(f_n(v_1),\ldots,f_n(v_m)),\quad
r=F(\vartheta)-y,\quad J(\vartheta)=DF(\vartheta).
\]

Thus $J$ is an $m\times N_n$ Euclidean Jacobian and the exact flow is

\[
\dot\vartheta=-\frac2mJ(\vartheta)^\top r.
\tag{1}
\]

**Lemma.** Fix a width and an initialization on the source's fitting event.
The endpoint map from an open neighborhood of this initialization in the full
Euclidean parameter space to the fitted parameter limit is continuously
differentiable. Its derivative $P_\infty$ satisfies

\[
\begin{aligned}
P_\infty&=\lim_{t\to\infty}P(t),&P(0)&=I,\\
\dot P(t)&=-A(t)P(t),&
A(t)&=\frac2m\left[J(t)^\top J(t)
              +\sum_{a=1}^m r_a(t)D^2F_a(\vartheta(t))\right],\\
\operatorname{range}P_\infty&=\ker J(\vartheta_\infty),&
\operatorname{rank}P_\infty&=N_n-m.
\end{aligned}
\tag{2}
\]

The full-space neighborhood permits small initial readout changes only to
define this derivative; the random ensemble under study still has readout
identically zero at initialization.

**Proof.** The readout columns of $J$ alone have Gram

\[
J_wJ_w^\top=\mathsf H^\top\mathsf H/n\succeq(\gamma/4)I_m
\]

throughout the fitting tube. The source also gives convergence of
$\vartheta(t)$ at an exponential rate. At this fixed width, smoothness of the
activations and compactness of a neighborhood of the convergent trajectory
bound all derivatives needed below. In particular,

\[
A(t)=A_\infty+B(t),\qquad
A_\infty=\frac2mJ_\infty^\top J_\infty,\qquad
\|B(t)\|\le C_n e^{-\kappa t}
\tag{3}
\]

for some $C_n<\infty$ and $\kappa>0$. The positive eigenvalues of
$A_\infty$ are at least $\gamma/(2m)$, and its kernel has dimension
$N_n-m$. Constants in this proof are finite-width constants; no uniformity in
$n$ is claimed.

First justify an open set of nearby fitted trajectories. Choose a sufficiently
small closed ball about $\vartheta_\infty$ on which
$JJ^\top\succeq(\gamma/8)I_m$ and $\|J\|\le M$. While a trajectory remains
inside it,

\[
\dot r=-\frac2mJJ^\top r,\qquad
\|r(T+s)\|\le\|r(T)\|e^{-\gamma s/(4m)},\qquad
\int_T^\infty\|\dot\vartheta(t)\|\,dt
\le\frac{8M}{\gamma}\|r(T)\|.
\]

For sufficiently large $T$, the original trajectory is near the center and
its residual makes the last bound smaller than the remaining radius. The same
strict inequalities hold for all sufficiently close initial parameters by
finite-time continuous dependence. A first-exit argument then keeps all these
trajectories inside the ball. They converge and fit exponentially, with uniform
constants on a smaller initial neighborhood. Their endpoints are continuous,
since their finite-time maps are continuous and their convergence is uniform.

Differentiating (1) at finite time gives the displayed equation for $P$.
If $u(t)=P(t)u(0)$, then

\[
\frac12\frac d{dt}\|u(t)\|^2
\le\frac2m\left\|\sum_a r_a(t)D^2F_a(\vartheta(t))\right\|\|u(t)\|^2.
\]

The coefficient is integrable, so $P(t)$ is uniformly bounded in time. This
bound also holds uniformly on the smaller neighborhood just constructed.
Let $\Pi$ be the orthogonal projection onto $\ker A_\infty$. From (3),

\[
\frac d{dt}(\Pi P)=-\Pi BP,
\]

which is integrable. Thus $\Pi P$ converges. The complementary component
satisfies

\[
(I-\Pi)P(t)
=e^{-A_\infty(t-T)}(I-\Pi)P(T)
 -\int_T^t e^{-A_\infty(t-s)}(I-\Pi)B(s)P(s)\,ds.
\]

The first term tends to zero by the spectral gap. Splitting the integral at
$s=t/2$, using the gap on the early half and exponential decay of $B$ on
the late half, shows that the second term also tends to zero. Hence $P(t)$
converges to $P_\infty$ with range contained in $\ker J_\infty$. These
estimates are uniform on the smaller neighborhood: the spectral gap, trajectory
convergence, derivative bounds, and bounds for $P$ are uniform there.
Uniform convergence of the differentiable finite-time maps and their
derivatives proves differentiability of the endpoint map, with derivative
$P_\infty$. This last assertion can also be checked directly by integrating
the finite-time derivative along any line segment in the neighborhood and
passing to the uniform limit.

It remains to prove the claimed rank; finite-time invertibility by itself is
insufficient. Let $U_T(t)$ solve the same linearized equation with
$U_T(T)=I$, and put $\eta_T=\int_T^\infty\|B(t)\|dt$. Since
$A_\infty\succeq0$,

\[
\|U_T(t)\|\le e^{\eta_T}.
\]

The preceding argument gives a limit $U_T(\infty)$ taking values in
$\ker A_\infty$. For $u\in\ker A_\infty$,

\[
\|U_T(\infty)u-u\|
=\left\|\int_T^\infty\Pi B(t)U_T(t)u\,dt\right\|
\le\eta_Te^{\eta_T}\|u\|.
\]

Choose $T$ so large that $\eta_Te^{\eta_T}<1$. The restriction of
$U_T(\infty)$ to this kernel is injective, hence has rank $N_n-m$.
The finite-time fundamental matrix $P(T)$ is invertible: its inverse solves
$\dot Q=QA$, $Q(0)=I$, and differentiation gives $QP=I$.
Finally $P_\infty=U_T(\infty)P(T)$. This proves the rank and the asserted
range. ∎

## What this says about the actual initialization randomness

Let $I_{\mathrm{hid}}:\mathbb R^{N_n-n}\to\mathbb R^{N_n}$ embed the hidden
coordinates with readout coordinates zero. All hidden mobility coordinates at
initialization are independent $N(0,1/n)$, so one can write exactly

\[
\vartheta_0=(G/\sqrt n,0),\qquad G\sim N(0,I_{N_n-n}).
\]

For a passive query define the row vector
$j_v=D_\vartheta f_n(\vartheta_\infty,v)$. The endpoint sensitivity to these
standard Gaussian coordinates is therefore

\[
D_G f_n(\infty,v)
=\frac1{\sqrt n}\,j_vP_\infty I_{\mathrm{hid}}.
\tag{4}
\]

This is a derivative of the actual fitted predictor at the fixed nonzero label
vector. It is not a derivative in labels or in training time. Moreover,

\[
\operatorname{rank}(P_\infty I_{\mathrm{hid}})\ge N_n-n-m,
\]

because $\ker P_\infty$ has dimension $m$. Thus many independent hidden
parameter directions survive fitting. But (4) can vanish if the passive
prediction annihilates those surviving directions. At training inputs it
vanishes exactly, since $J_\infty P_\infty=0$.

The source fitting estimates do not provide a positive lower bound for
$j_vP_\infty I_{\mathrm{hid}}$ at any separated query. Nor does the rank lemma
provide uniform-in-width bounds for $P_\infty$. Nonaffinity must be used in a
new argument at precisely this point.

As a check on the logical distinction, temporarily take all activations to be
the identity, $m=d\ge2$, and $v_a=e_a$. Then $Q^{(L)}=I_m$, and all source
fitting hypotheses hold for sufficiently small nonzero labels. Every fitted
network is a linear function $f_n(\infty,v)=y^\top v$, independent of its
initialization, although the rank lemma still preserves $N_n-m$ parameter
directions. This example is outside the requested nonaffine class and is not a
counterexample to the target. It proves that endpoint parameter rank and the
fitting gap alone cannot establish observable randomness, even with full-span
training and separated passive queries.

Even proving nonzero sensitivity at every fixed width would not settle the
rate or probability. A nonconstant observable such as $e^{-n}G_1$ has nonzero
derivative and nevertheless has negligible $n^{-1/2}$-scale variability.
Also, a gradient lower bound alone is not a variance lower bound: oscillatory
functions can have a large gradient and small amplitude.

## A precise sufficient endpoint probability bridge

The following elementary criterion states the remaining probabilistic
obligation without a frozen-model substitution. Let $E_n$ be the source
fitting event, with probability tending to one, and fix a deterministic query
$v_n\in\mathcal X_\varepsilon$. Set $U_n=f_n(\infty,v_n)$ on $E_n$.
Suppose there were constants $a,b>0$, independent of width, such that

\[
\operatorname{Var}(U_n\mid E_n)\ge a/n,\qquad
\mathbb E\!\left[
 |U_n-\mathbb E(U_n\mid E_n)|^4\mid E_n\right]\le b/n^2.
\tag{5}
\]

Then the target would hold with $c=\sqrt a$ and
$p=a^2/(32b)$ for every sufficiently large width.

Indeed, condition two independent runs on their respective events $E_n$.
For their difference $D=U_n-\widetilde U_n$, writing $v=\operatorname{Var}
(U_n\mid E_n)$ and $\mu_4$ for the centered fourth moment, independence gives

\[
\mathbb ED^2=2v,\qquad
\mathbb ED^4=2\mu_4+6v^2\le8b/n^2.
\]

For any nonnegative random variable $Z$, Cauchy--Schwarz applied on
$\{Z\ge\mathbb EZ/2\}$ gives

\[
\Pr\{Z\ge\mathbb EZ/2\}
\ge\frac{(\mathbb EZ)^2}{4\mathbb EZ^2}.
\]

Apply this to $Z=D^2$. The conditional probability of
$|D|\ge\sqrt v\ge\sqrt{a/n}$ is at least $a^2/(8b)$. For large width,
$\Pr(E_n)^2\ge1/4$, which gives the stated unconditional bound. A supremum
over the separated query set is at least the value at $v_n$.

Neither inequality (5) has been established in this attempt. In particular,
the first inequality requires a lower bound for randomness that survives both
the nonlinear training dynamics and the exact interpolation constraint. The
source's bounds for finite residual activity, small parameter movement, and
endpoint existence do not supply it.

**Conclusion.** The direct endpoint derivative and its rank are exact
finite-width facts. The conjectured $n^{-1/2}$ lower bound remains open under
the full stated nonaffine assumptions. The obstruction in this route is a
missing quantitative statement that a separated query detects surviving
initialization randomness, together with sufficiently controlled endpoint
fluctuation moments. This is a failure to complete the route, not a disproof
of the conjecture.
