# All-time sample compression: exact sufficient statistics and a geometric obstruction

This bounded route does not establish the proposed all-time compression theorem for general nonlinear strip-analytic activations and a continuous latent generator. It proves two exact sufficient-statistic statements and an obstruction to extending exact duplicate aggregation by an absolute cluster-diameter estimate. The obstruction uses the actual evolving two-hidden-layer network, normalized inputs, Gaussian initialization on an event of positive probability, constant labels, and fixed test points. It is a failure of geometric point merging, not a lower bound against all admissible compression schemes.

The scientific inputs for this scoped route were the supervisor's prompt and its correction that inputs satisfy \(\|x\|=\sqrt d\). No other studies, prior conclusions, experiments, or external results were used. The canonical-notation, rigorous-proof, and conjecture-investigation instructions were applied.

Check status: the scoped author checked the expansions, gradient equations, invariants, compactness argument, and lower bound algebraically. No independent review, formal verification, or numerical experiment has been performed. The statements marked proved below are claim types supported by the displayed arguments; they have not been marked internally checked or promoted by the study.

## Model and exact compression criterion

For input \(x\in\mathbb R^d\), width \(n\), and depth \(L\ge2\), write

\[
z^{(1)}(x)=W^{(1)}x/\sqrt d,\qquad
h^{(\ell)}(x)=\phi(z^{(\ell)}(x)),\qquad
z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x)\quad(\ell\ge2),
\]
\[
f_\theta(x)=\frac1n w^\top h^{(L)}(x),\qquad
\mathcal L_D(\theta)=\frac1m\sum_{a=1}^m(f_\theta(x_a)-y_a)^2.
\]

Here \(W^{(1)}\in\mathbb R^{n\times d}\), hidden matrices are in \(\mathbb R^{n\times n}\), \(w\in\mathbb R^n\), and \(\theta\) denotes all their entries. The training flow is

\[
\dot\theta=-D\nabla\mathcal L_D(\theta),
\]

where the positive diagonal matrix \(D\) applies block mobilities \((n,1,\ldots,1,n)\). Initially \(w=0\), the first-layer entries are independent centered Gaussians of variance \(1\), and hidden entries are independent centered Gaussians of variance \(1/n\). Compression changes the retained data representation and preserves this parameterization, initialization, and flow.

If a retained representation gives a loss \(\widetilde{\mathcal L}\) with

\[
\mathcal L_D(\theta)-\widetilde{\mathcal L}(\theta)
=\text{a constant independent of }\theta,
\tag{1}
\]

then both parameter trajectories agree for all time. This follows from equality of their locally Lipschitz vector fields and uniqueness, not from a frozen-kernel argument. The flows are global: with \(\|u\|_{D^{-1}}^2=u^\top D^{-1}u\),

\[
\frac{d}{dt}\mathcal L_D(\theta(t))
=-\|\dot\theta(t)\|_{D^{-1}}^2,
\qquad
\|\theta(t)-\theta(0)\|_{D^{-1}}
\le\sqrt{t\mathcal L_D(\theta(0))}.
\]

Consequently, a solution cannot escape every bounded set at a finite time; the smooth vector field extends it. This also verifies that the all-time statements below refer to globally defined dynamics.

## Exact data condition for any permitted activation

Suppose the initial dataset has at most \(Q\) distinct inputs \(\xi_1,\ldots,\xi_Q\), with no condition on labels within an input class. For each nonempty class let

\[
p_j=\frac{\#\{a:x_a=\xi_j\}}m,
\qquad
\bar y_j=\frac{1}{mp_j}\sum_{a:x_a=\xi_j}y_a.
\]

Then

\[
\mathcal L_D(\theta)
=\sum_{j=1}^Qp_j(f_\theta(\xi_j)-\bar y_j)^2
+\frac1m\sum_{j=1}^Q\sum_{a:x_a=\xi_j}(y_a-\bar y_j)^2.
\tag{2}
\]

To check (2), substitute
\(f_\theta(\xi_j)-y_a=f_\theta(\xi_j)-\bar y_j+\bar y_j-y_a\)
and sum: the mixed term vanishes by the definition of \(\bar y_j\). The last term does not depend on parameters, so (1) applies. Retaining \((\xi_j,p_j,\bar y_j)_{j=1}^Q\) gives exactly the original trajectory and all test predictions, for every initialization and every time. Storage is \(O(Q(d+2))\) numbers; the sample counts require \(O(\log m)\) bits each. The label variance is needed only to reconstruct the numerical value of the original loss, not its dynamics.

This is an unconditional initial-data sufficient condition, but it is finite support, not the desired continuous-manifold theorem. A small diameter in place of equality of inputs does not inherit its all-time conclusion, as shown below.

## Exact moment compression for the affine activation subclass

Let \(\phi(z)=\alpha z+\beta\), with fixed real constants \(\alpha,\beta\). These activations satisfy the stated strip-analytic and bounded-derivative assumptions. Every dense network above then has the exact form

\[
f_\theta(x)=a_\theta^\top x+b_\theta.
\]

For completeness, write \(h^{(\ell)}(x)=A^{(\ell)}x+c^{(\ell)}\). The defining recursions are

\[
A^{(1)}=\alpha W^{(1)}/\sqrt d,\quad c^{(1)}=\beta\mathbf1,
\]
\[
A^{(\ell)}=\alpha W^{(\ell)}A^{(\ell-1)},\quad
c^{(\ell)}=\alpha W^{(\ell)}c^{(\ell-1)}+\beta\mathbf1,
\]
\[
a_\theta=A^{(L)\top}w/n,\qquad b_\theta=w^\top c^{(L)}/n.
\]

Define the initial-data moments

\[
\Sigma=\frac1m\sum_a x_ax_a^\top,\quad
\mu=\frac1m\sum_a x_a,\quad
\nu=\frac1m\sum_a y_ax_a,\quad
\bar y=\frac1m\sum_a y_a.
\]

Expanding the loss gives

\[
\mathcal L_D(\theta)
=a_\theta^\top\Sigma a_\theta
+2b_\theta a_\theta^\top\mu+b_\theta^2
-2a_\theta^\top\nu-2b_\theta\bar y
+\frac1m\sum_a y_a^2.
\tag{3}
\]

Thus \((\Sigma,\mu,\nu,\bar y)\), accumulated in one pass, determine the exact parameter vector field for every \(n,L,m\). Fixed sample-dependent storage is \(O(d^2)\) real numbers. The dense parameter state is still retained; this theorem establishes only the sample axis. The parameter dynamics remain nonlinear and all layers train; replacing them by linear-model parameter dynamics would not preserve the specified optimizer.

There is also an exact weighted coreset. On the sphere \(\|x\|^2=d\), define

\[
\Psi(x,y)=(\operatorname{vech}(xx^\top),x,yx,y)
\in\mathbb R^p,
\qquad p=\frac{d(d+1)}2+2d+1.
\]

Here \(\operatorname{vech}\) lists each upper-triangular entry once. All vectors \(\Psi(x_a,y_a)\) lie in an affine hyperplane because \(\operatorname{tr}(x_ax_a^\top)=d\). Their mean is a convex combination of at most \(p\) of these vectors. One can prove this directly: if a representation has more than \(p\) positive weights, affine dependence gives coefficients \(\gamma_a\), not all zero, with \(\sum_a\gamma_a=0\) and \(\sum_a\gamma_a\Psi_a=0\). Subtract \(t\gamma_a\) from each weight, taking \(t\) to be the minimum weight-to-\(\gamma_a\) ratio over \(\gamma_a>0\). The weights remain nonnegative, their sum and moment vector are preserved, and one positive weight disappears. Iteration terminates with at most \(p\) weights. These retained weighted examples match the four moments in (3), hence the entire parameter trajectory. With a constant label, the redundant \(yx\) and \(y\) coordinates can be dropped, yielding at most \(d(d+1)/2+d\) retained examples.

This is a complete all-time theorem for a permitted but special activation subclass. It does not answer the generic nonlinear activation question. In particular, an unknown nonlinear \(k\)-dimensional latent generator does not bound the affine span of its image by \(k\), so one cannot replace \(d\) by \(k\) in this moment count without an additional affine-span assumption.

## A sphere-normalized, constant-label obstruction to geometric merging

Fix label \(y_*>0\), \(d=2\), \(n=1\), \(L=2\), and \(\phi(z)=1+z\). Write
\(W^{(1)}=(a,b)\), \(W^{(2)}=v\), and use scalar readout \(w\). The actual network is

\[
f_\theta(x)
=w\left[v\left(1+\frac{a x_1+b x_2}{\sqrt2}\right)+1\right].
\tag{4}
\]

All mobilities equal one at width one. Take \(a_0,b_0,v_0>0\), an event of probability \(1/8\) under the specified Gaussian initialization, and \(w_0=0\). For \(0<\delta<1\), put \(c=\sqrt{1-\delta^2}\) and choose the two training examples

\[
x_\pm=\sqrt2(c,\pm\delta),\qquad y_\pm=y_*.
\]

These points lie on the canonical sphere. They are samples of the fixed real-analytic, Lipschitz pair generator

\[
u\longmapsto\big(\sqrt2(\cos u,\sin u),y_*\big)
\]

at \(u=\pm\arcsin\delta\). The latent dimension is one and the labels are constant. Repeating each example the same number of times gives arbitrarily large \(m\) without changing the flow. Use the fixed test set

\[
Y=\{\sqrt2 e_2,-\sqrt2 e_2\},
\]

independent of \(\delta\).

Let \(q=1+ca\) and \(r=w(vq+1)-y_*\). The full two-point loss and its exact gradient flow are

\[
\mathcal L_\delta=r^2+\delta^2(wvb)^2,
\tag{5}
\]
\[
\begin{aligned}
\dot a&=-2cwv r,&
\dot b&=-2\delta^2w^2v^2b,\\
\dot v&=-2wq r-2\delta^2w^2vb^2,&
\dot w&=-2(vq+1)r-2\delta^2wv^2b^2.
\end{aligned}
\tag{6}
\]

The region \(w,v\ge0\), \(q\ge1\), \(b\ge0\), \(r\le0\) is forward invariant. At \(w=0\), \(\dot w=2(vq+1)y_*>0\); at \(v=0\), \(\dot v=-2wqr\ge0\); and \(\dot q=-2c^2wv r\ge0\). The equation for \(b\) preserves its sign. Finally,

\[
\dot r=-2\big[(vq+1)^2+w^2q^2+c^2w^2v^2\big]r
-2\delta^2wv^2b^2(vq+1)-2\delta^2w^3vb^2q,
\]

whose last two terms are nonpositive on \(r=0\). These boundary inequalities establish invariance from the given initial point.

All parameters remain bounded. First \(w(vq+1)\le y_*\), so \(w\le y_*\). Direct differentiation gives

\[
\frac d{dt}(v^2-w^2)=4wr\le0,
\qquad
q^2-c^2v^2+c^2b^2=q_0^2-c^2v_0^2+c^2b_0^2.
\tag{7}
\]

Hence \(v^2\le v_0^2+y_*^2\), \(0\le b\le b_0\), and
\(q^2\le q_0^2+c^2(y_*^2+b_0^2)\). Since \(c>0\), \(a=(q-1)/c\) is bounded as well.

Energy dissipation gives \(\int_0^\infty\|\nabla\mathcal L_\delta\|^2dt<\infty\). The trajectory is in a compact set and the loss is polynomial, so the derivative of \(\|\nabla\mathcal L_\delta\|^2\) is bounded. A nonnegative integrable function with a bounded derivative tends to zero: otherwise disjoint intervals around points where it exceeds a fixed positive threshold would each contribute a fixed positive integral. Thus every accumulation point is stationary. At a stationary point in this compact invariant region, \(w\ne0\), since \(w=0\) would give \(\dot w>0\). The equation for \(b\) then forces \(vb=0\), and the equation for \(v\) forces \(r=0\). It follows that

\[
w(t)v(t)b(t)\longrightarrow0,
\qquad
f_{\theta(t)}(\sqrt2e_2)-f_{\theta(t)}(-\sqrt2e_2)
=2w(t)v(t)b(t)\longrightarrow0.
\tag{8}
\]

The argument requires neither convergence of all parameters nor identification of the common limiting test value.

Now retain only the actual point \(x_+\), with weight one and label \(y_*\), using the same initialization. Introduce the first-layer coordinates

\[
A=ca+\delta b,\qquad B=-\delta a+cb.
\]

This is an orthogonal change of coordinates, so their mobility remains one. For the one-point flow, \(B(t)=B_0\), and the loss is
\([w(v(1+A)+1)-y_*]^2\). Denote its residual by \(\widetilde r\). Starting from \(A_0>0\), \(v_0>0\), \(w_0=0\), one has \(\widetilde r<0\), and \(A,v,w\) increase until their finite limits. Indeed,

\[
\dot{\widetilde r}
=-2\big[(v(1+A)+1)^2+w^2(1+A)^2+w^2v^2\big]\widetilde r,
\]

so \(|\widetilde r(t)|\le y_*e^{-2t}\). The identities

\[
\frac d{dt}(v^2-w^2)=4w\widetilde r\le0,
\qquad (1+A)^2-v^2=(1+A_0)^2-v_0^2
\]

give \(w\le y_*\), \(v\le\sqrt{v_0^2+y_*^2}\), and
\(1+A\le\sqrt{(1+A_0)^2+y_*^2}\). The exponentially decaying residual and bounded coefficients make all velocities integrable. In particular,

\[
w_\infty[v_\infty(1+A_\infty)+1]=y_*,\qquad v_\infty\ge v_0>0.
\]

For all sufficiently small positive \(\delta\), \(c\ge1/2\) and \(B_0=-\delta a_0+cb_0\ge b_0/2\). Reconstructing the original coordinate gives
\(b_\infty=\delta A_\infty+cB_0\ge b_0/4\).
Since \(A_0\le a_0+b_0\), the retained-point flow satisfies the uniform bound

\[
w_\infty v_\infty b_\infty\ge C_0,
\qquad
C_0=
\frac{y_*v_0b_0}{4\left[1+\sqrt{v_0^2+y_*^2}\sqrt{(1+a_0+b_0)^2+y_*^2}\right]}>0.
\tag{9}
\]

For any two numbers \(u,v\), \(\max(|u|,|v|)\ge|u-v|/2\). Apply this to the full-minus-retained prediction errors at the two test points and combine (8)–(9). With \(\widetilde\theta(t)\) denoting the retained-point flow,

\[
\sup_{t\ge0}\max_{x\in Y}
|f_{\theta(t)}(x)-f_{\widetilde\theta(t)}(x)|
\ge C_0
\tag{10}
\]

for every sufficiently small \(\delta>0\). Yet the training-pair diameter is \(2\sqrt2\delta\to0\), and collapsing the two examples to \(x_+\) changes the input measure by at most this amount in any coupling-based distance with Euclidean cost.

The lower bound can be made uniform on an initialization event of positive probability by restricting \(a_0,b_0,v_0\) to \([1,2]\). Then a single positive lower bound for \(C_0\) and a single sufficiently small upper bound on \(\delta\) work throughout that event. The counterexample therefore does not rely on a probability-zero initialization.

## Consequence for the remaining proof obligation

Equation (5) identifies the missing structural quantity. The transverse loss curvature is proportional to \(\delta^2\), but its nonzero value eventually eliminates a transverse prediction that survives when the mode is deleted. Absolute approximation of the empirical measure, even for a fixed analytic one-dimensional generator and constant labels, does not control that effect uniformly over physical time.

An all-time argument based on approximate quotienting must therefore control what it does to weak data modes, for example by a relative moment or conditioning certificate that preserves their effect, or by a proved mechanism making their eventual test contribution small. The example does not prove that any particular relative certificate is sufficient for general nonlinear networks. Nor does it refute sample compression: the affine model in the example has the exact moment compression (3).

The current status is consequently:

- **Proved:** exact all-time compression for finite input support with arbitrary permitted activation, using (2).
- **Proved:** exact all-time sample compression by \(O(d^2)\) statistics for affine activations, with the original feature-learning flow, using (3).
- **Proved:** geometric merging has no all-time error modulus tending to zero with cluster diameter over the stated activation class, even under normalized inputs, analytic one-dimensional latent geometry, constant labels, and a fixed two-point test set, using (10).
- **Open:** a nondegenerate initial-data condition for a continuous latent manifold and genuinely nonlinear activation that yields the desired all-time, sample-independent retained state without assuming future response regularity. Low latent dimension, generator analyticity, and simple labels alone do not close this particular proof route.

The highest-leverage next obligation is a precise relative treatment of weak modes, tied to a verifiable initial-data certificate and the actual nonlinear feature flow. A claim that merely assumes uniform future conditioning or response regularity would restate the unresolved issue.
