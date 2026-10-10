# Label superposition and compression: a conditional corollary

This note uses only the scientific hypotheses supplied in the scoped assignment. It does not establish the population acceleration limit, the population Taylor remainder, or the three compression theorems. Conditional on those inputs, it gives a label-nonlinearity certificate that excludes approximation by any single map linear in the labels, including a label-independent kernel predictor initialized at zero. The certificate passes to each of the three compressed prediction trajectories without modifying its storage requirement.

## Setup and the inputs used

Fix training inputs \(x_1,\ldots,x_m\). For a label vector \(z\in\mathbb R^m\), write \(f_{n,z}(t)\in\mathbb R^m\) for the network's training predictions at physical time \(t\). The readout is

\[
f_n(x)=\frac1n w^\top h^{(L)}_n(x),
\qquad
\mathcal L_z=\frac1m\|f_{n,z}-z\|_2^2,
\]

where \(h^{(L)}_n(x)\in\mathbb R^n\) is the last hidden feature vector of the prescribed architecture. The first-layer weights have independent \(N(0,1)\) entries, the subsequent hidden weights have independent \(N(0,1/n)\) entries, and \(w(0)=0\). The mobilities for \((W^{(1)},W^{(2)},\ldots,W^{(L)},w)\) are \((n,1,\ldots,1,n)\): a parameter block of mobility \(\mu\) follows \(\dot W=-\mu\nabla_W\mathcal L_z\). The activation and its analytic assumptions are not specified in this assignment; the acceleration and convergence statements below are inputs, rather than claims derived here for an unspecified activation.

Use the same draw of the initial hidden weights for every label vector under comparison. In hidden mobility coordinates, define

\[
\theta_{\mathrm{hid},n}
=\bigl(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)}\bigr),
\qquad
A_n(z)=\|\ddot\theta_{\mathrm{hid},n}(0;z)\|^2,
\]

where the squared norm sums the squared Frobenius norms of its blocks. The assumed acceleration is homogeneous of degree two in the labels, so

\[
\ddot\theta_{\mathrm{hid},n}(0;\alpha z)
=\alpha^2\ddot\theta_{\mathrm{hid},n}(0;z),
\qquad A_n(\alpha z)=\alpha^4 A_n(z).
\]

Let \(f_{\mathrm{NTK},n,z}\) be training with the initial mobility-weighted tangent kernel frozen. If \(J_n(0)\) is the Jacobian of the training prediction vector in the original parameters and \(M_n\) is the diagonal mobility operator, then its kernel is \(K_n(0)=J_n(0)M_nJ_n(0)^\top\). The loss convention gives

\[
\dot f_{\mathrm{NTK},n,z}
=-\frac2mK_n(0)(f_{\mathrm{NTK},n,z}-z),
\qquad
f_{\mathrm{NTK},n,z}(0)=0,
\]

and therefore

\[
f_{\mathrm{NTK},n,z}(t)
=\bigl(I-e^{-2tK_n(0)/m}\bigr)z.
\]

The supplied finite-width identity is

\[
z^\top\bigl(f_{n,z}(t)-f_{\mathrm{NTK},n,z}(t)\bigr)
=\frac m3 A_n(z)t^3+o_n(t^3)
\qquad(t\downarrow0).
\tag{1}
\]

Fix an admissible \(y\) for which \(y/2\) is also admissible and suppose the population acceleration limit is the deterministic number

\[
A(y)=\lim_{n\to\infty}A_n(y)>0.
\]

The limit may be in probability; only its deterministic value and the justified population expansion are used below. In particular, \(y\ne0\), and homogeneity gives \(A(y/2)=A(y)/16\). Let \(F_z(t)\) and \(F_{\mathrm{NTK},z}(t)\) denote the deterministic population training predictions for \(z\in\{y,y/2\}\). Assume convergence in probability at every fixed sufficiently small time and the separately justified population expansions

\[
z^\top\bigl(F_z(t)-F_{\mathrm{NTK},z}(t)\bigr)
=\frac m3 A(z)t^3+o_z(t^3).
\tag{2}
\]

The same-initialization frozen-kernel relation passes to the limit:
\(F_{\mathrm{NTK},y}(t)=2F_{\mathrm{NTK},y/2}(t)\).
Only this relation is needed; no kernel formula beyond it enters the population argument.

## The cubic superposition defect

Define the training prediction defect

\[
D(t)=F_y(t)-2F_{y/2}(t).
\]

The frozen-kernel terms cancel. In the term with labels \(y/2\), pairing with \(y\) contributes another factor of two. Thus (2) gives

\[
\begin{aligned}
y^\top D(t)
&=y^\top\bigl(F_y-F_{\mathrm{NTK},y}\bigr)
 -4(y/2)^\top\bigl(F_{y/2}-F_{\mathrm{NTK},y/2}\bigr)\\
&=\frac m3\left(A(y)-4\frac{A(y)}{16}\right)t^3+o(t^3)\\
&=\frac m4 A(y)t^3+o(t^3).
\end{aligned}
\tag{3}
\]

The finite-width version holds with \(D_n=f_{n,y}-2f_{n,y/2}\), \(A_n(y)\), and a width-dependent little-o remainder. Equation (3), rather than that finite-width statement alone, supplies a time interval independent of width.

For the maximum norm on training points, \(\|v\|_\infty=\max_a|v_a|\), the inequality \(|y^\top v|\le\|y\|_1\|v\|_\infty\) yields

\[
\liminf_{t\downarrow0}\frac{\|D(t)\|_\infty}{t^3}
\ge \frac{mA(y)}{4\|y\|_1}.
\tag{4}
\]

For the root-mean-square training norm
\(\|v\|_{\mathrm{tr}}=\|v\|_2/\sqrt m\), Cauchy--Schwarz gives instead

\[
\liminf_{t\downarrow0}\frac{\|D(t)\|_{\mathrm{tr}}}{t^3}
\ge \frac{A(y)}{4\|y\|_{\mathrm{tr}}}.
\tag{5}
\]

In particular, \(D(t)\ne0\) for every sufficiently small positive time. This certifies a nonlinear dependence of the prediction trajectory on the labels.

## Every common label-linear predictor has a nonzero error

At a fixed time, any map linear in the labels has the form \(z\mapsto Bz\), with \(B\in\mathbb R^{m\times m}\). Its matrix may depend on the inputs, time, width, and shared initialization. The condition is that the same matrix is used for the two label vectors. Set

\[
e_y=F_y-By,
\qquad
e_{y/2}=F_{y/2}-B(y/2).
\]

Linearity gives the exact identity \(D=e_y-2e_{y/2}\). Consequently, in any norm,

\[
\max\{\|e_y\|,\|e_{y/2}\|\}
\ge\frac13\|D\|.
\tag{6}
\]

This factor is sharp even for vector-valued predictions and arbitrary norms. Indeed, put \(b=\tfrac23(F_y+F_{y/2})\) and choose \(B=by^\top/\|y\|_2^2\), so that \(By=b\). Then \(e_y=D/3\) and \(e_{y/2}=-D/3\). Thus

\[
\inf_{B\in\mathbb R^{m\times m}}
\max_{z\in\{y,y/2\}}\|F_z(t)-Bz\|
=\frac13\|D(t)\|.
\tag{7}
\]

The matrix used to establish sharpness is an oracle construction for this two-point approximation problem, not a proposed label-independent training rule. The lower bound holds even when the comparison is allowed this oracle choice of a single matrix.

Combining (4)--(7) gives the constants

\[
\liminf_{t\downarrow0}\frac1{t^3}
\inf_B\max_{z\in\{y,y/2\}}\|F_z(t)-Bz\|_\infty
\ge\frac{mA(y)}{12\|y\|_1},
\tag{8}
\]

\[
\liminf_{t\downarrow0}\frac1{t^3}
\inf_B\max_{z\in\{y,y/2\}}\|F_z(t)-Bz\|_{\mathrm{tr}}
\ge\frac{A(y)}{12\|y\|_{\mathrm{tr}}}.
\tag{9}
\]

Under a label cap \(\|y\|_\infty\le M\), with \(M>0\), the right side of (8) is at least \(A(y)/(12M)\). The sharper form uses the actual \(\|y\|_1\). These are absolute errors; the assertion is that at least one of the two admissible label runs has the stated error. It does not identify the harder label uniformly over comparison matrices.

For comparison, any fixed label-independent kernel matrix \(K\), with zero initial predictions, produces
\(B(t)=I-e^{-2tK/m}\) under this squared-loss flow. Kernel ridge prediction is also linear in the training labels when its kernel and regularization are selected independently of those labels. Such predictors are subsets of the matrices covered by (8)--(9). The argument even permits an arbitrary common matrix at each time; imposing a particular kernel trajectory cannot improve the two-point lower bound.

The choice \(y/2\) maximizes the leading constant within comparisons of \(y\) and \(\alpha y\), \(0<\alpha<1\). Indeed,

\[
y^\top\bigl(F_y-\alpha^{-1}F_{\alpha y}\bigr)
=\frac m3(1-\alpha^2)A(y)t^3+o(t^3),
\]

while the triangle inequality for two approximation errors costs \(1+\alpha^{-1}\). Their ratio is \(\alpha(1-\alpha)\), whose maximum is \(1/4\) at \(\alpha=1/2\). This statement concerns the constant certified by the supplied scalar identity; it is not an assertion that other information about the network cannot give a stronger lower bound.

## Inheritance by all three compressed trajectories

For compression scheme \(j\in\{1,2,3\}\), let \(g^{(j)}_{n,z}(t)\in\mathbb R^m\) be its training prediction vector. All limits below refer to the approximation regime in its supplied compression theorem; any additional approximation parameters are suppressed in the notation. Suppose that, for each of the two labels, its complete-trajectory guarantee implies

\[
\varepsilon^{(j)}_{n,z}
:=\sup_{0\le s\le T}
\|g^{(j)}_{n,z}(s)-f_{n,z}(s)\|_\infty
\xrightarrow{\mathbb P}0.
\tag{10}
\]

The two dense runs use the same initialization. If a compression uses auxiliary randomness, couple its label runs through a common prescribed label-independent seed when viewing it as a map of labels; no independence is needed for the argument. The two individual guarantees in (10) imply their joint convergence by a finite union bound. The same applies simultaneously to all three schemes.

Define
\(D^{(j)}_n(t)=g^{(j)}_{n,y}(t)-2g^{(j)}_{n,y/2}(t)\). Deterministically,

\[
\|D^{(j)}_n(t)-D_n(t)\|_\infty
\le \varepsilon^{(j)}_{n,y}+2\varepsilon^{(j)}_{n,y/2}.
\tag{11}
\]

Fixed-time convergence of the dense trajectories and (10)--(11) imply
\(D^{(j)}_n(t)\to D(t)\) in probability, jointly over the three schemes. Hence the same cubic population defect is inherited by their outputs.

The following form makes the probability, time, and comparison quantifiers explicit. For every \(\eta\in(0,1)\), there is \(t_0>0\) such that, for every fixed \(t\in(0,\min\{t_0,T\}]\),

\[
\lim_{n\to\infty}\mathbb P\left[
\min_{1\le j\le3}\ 
\inf_{B\in\mathbb R^{m\times m}}
\max_{z\in\{y,y/2\}}
\|g^{(j)}_{n,z}(t)-Bz\|_\infty
\ge (1-\eta)\frac{mA(y)}{12\|y\|_1}\,t^3
\right]=1.
\tag{12}
\]

To verify the constants in this statement, use (3) to choose \(t_0\) so that the population left side in (8), before dividing by \(t^3\), is at least \((1-\eta/2)mA(y)t^3/(12\|y\|_1)\). At any chosen fixed positive time, convergence of the three defects makes the norm error at most \(\eta mA(y)t^3/(8\|y\|_1)\) with probability tending to one. Dividing that error by three in (7) leaves a margin \(\eta mA(y)t^3/(24\|y\|_1)\), exactly the difference between the two thresholds. Formula (7) applies directly to each pair of compressed prediction vectors, so the event holds for every common linear comparison matrix at once, including random matrices coupled to the compression.

The root-mean-square version of (12) has constant \(A(y)/(12\|y\|_{\mathrm{tr}})\). More generally, at finite width the deterministic transfer bound is

\[
\inf_B\max_{z\in\{y,y/2\}}
\|g^{(j)}_{n,z}(t)-Bz\|_\infty
\ge\frac13\left(
\|D_n(t)\|_\infty-
\varepsilon^{(j)}_{n,y}-2\varepsilon^{(j)}_{n,y/2}
\right).
\tag{13}
\]

The lower bound also holds for the complete-trajectory approximation error of any label-linear comparison procedure: its supremum over \([0,T]\) is at least the error at the fixed time in (12). No extra state is introduced into any predictor: each compression retains its original per-run storage requirement. The comparison uses two conceptual label runs and is a consequence about the schemes' existing output guarantees.

## Limits of the conclusion

The population remainder assumption is essential. The finite-width expansion (1) and convergence of \(A_n(y)\) alone do not justify (3). For example, the scalar functions \(t^3e^{-nt}\) have the same positive cubic coefficient for every \(n\), but converge to zero at every fixed \(t>0\). The proof uses a justified population expansion first, then chooses a positive time, then passes to large width. It supplies no rate for a joint limit \(t=t_n\downarrow0\), and no uniform finite-width assertion over an entire shrinking-time interval.

The obstruction applies to a single predictor linear in labels across the two runs. A kernel or its hyperparameters selected using the labels can give a nonlinear overall map of labels and is not excluded. Neither is an arbitrary affine map \(z\mapsto Bz+b\) excluded by just two label vectors: an affine map can interpolate any two points on this label ray. If zero labels and their convergence guarantees are also included, the defect \(F_y-2F_{y/2}+F_0\), with \(F_0=0\), excludes common affine maps on the three-label set at the weaker maximum-norm leading constant \(mA(y)/(16\|y\|_1)\); this additional three-label statement is not needed for (12).

The argument proves separation on training predictions at early positive times. It does not imply lower endpoint test risk, superiority in fitting or generalization, separation at every later time, or an inability of a kernel method to match the single observed-label run. Likewise, the positive hidden acceleration pertains to the dense network. Prediction approximation transfers its output superposition defect to a compression, but does not establish that the compression's own internal features or stored coordinates move in an analogous way.

The strongest conclusion supported here is therefore: under the supplied positive-acceleration and population-limit hypotheses, each trajectory-faithful compression retains an order-\(t^3\) nonlinearity in the labels, and with probability tending to one no common label-linear predictor can approximate both admissible label runs below the explicit order-\(t^3\) error in (12), at any chosen sufficiently small positive time.
