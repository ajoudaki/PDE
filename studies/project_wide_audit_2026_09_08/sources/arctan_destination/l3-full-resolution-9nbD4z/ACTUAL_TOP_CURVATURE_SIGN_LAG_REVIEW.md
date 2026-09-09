# Isolated adversarial audit: actual top curvature sign lag

**Verdict: PASS for all claims within the requested scope.** No mathematical gap was found in the candidate version identified below. The reconstruction verifies the trained vector first layer, common fixed-width existence and Taylor bounds, feature-time symmetry, the sign crossing and constants, the physical clock and full physical continuity, both Gaussian-support statements, and both deterministic uniform little-o obstructions.

Audited candidate:

    /tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/ACTUAL_TOP_CURVATURE_SIGN_LAG.md

Exact audited SHA256:

    3bc7787c0da406fe06503f5cc91ca350e53df918d4581dfb66eabfde596a0925

This matches the supplied hash and remained unchanged on rechecking after the proof reconstruction. The only source inputs read were this candidate and the complete solve-math-rigorously skill at /etc/codex/skills/solve-math-rigorously/SKILL.md. No other proof notes, reviews, ledgers, contextual sources, companion estimates, or experiments were used. The candidate was not edited.

This verdict does not certify a counterexample to a global population theorem or sharpness of a canonical Gaussian expectation. The dynamics audited are precisely the candidate's equations (1) and (22), including their layer-dependent factors.

The proof proceeds by deriving the fully trained acceleration, constructing a common interval with derivative bounds, proving the entire sign-lag interval, and then verifying the clock, perturbation, support, and uniform-rate arguments.

## 1. Canonical dynamics and fully trained acceleration

Fix \(n=2\), \(b=1/2\), and
\[
\phi(u)=\arctan u,\qquad
\phi'(u)=\frac1{1+u^2},\qquad
\phi''(u)=-\frac{2u}{(1+u^2)^2}.
\]
The canonical state is
\[
X=(z^{(1)},W^{(2)},W^{(3)},W^{(4)})\in\mathbb R^{12},
\qquad W^{(1)}=z^{(1)}\in\mathbb R^2.
\]
Both hidden matrices are \(2\times2\), and the readout is a vector in \(\mathbb R^2\). All vector norms are ordinary Euclidean norms, matrix norms are Frobenius norms, and derivative norms are induced operator norms for these spaces. Transposes are ordinary finite-dimensional transposes. No normalized inner product convention is used.

Define
\[
h^{(\ell)}=\phi(z^{(\ell)}),\qquad
z^{(2)}=W^{(2)}h^{(1)},\qquad z^{(3)}=W^{(3)}h^{(2)},
\]
\[
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\qquad
\delta^{(2)}=\operatorname{diag}(\phi'(z^{(2)}))(W^{(3)})^T\delta^{(3)},\qquad
\delta^{(1)}=\operatorname{diag}(\phi'(z^{(1)}))(W^{(2)})^T\delta^{(2)}.
\]
The stipulated feature-time equations are
\[
(z^{(1)})'=\delta^{(1)},\qquad
(W^{(2)})'=\frac1n\delta^{(2)}(h^{(1)})^T,\qquad
(W^{(3)})'=\frac1n\delta^{(3)}(h^{(2)})^T,\qquad
(W^{(4)})'=h^{(3)}.
\tag{A1}
\]

To check the loss scaling independently, direct differentiation of
\(f=n^{-1}(W^{(4)})^Th^{(3)}\) in the ordinary parameter coordinates gives
\[
\nabla_{z^{(1)}}f=\frac1n\delta^{(1)},\qquad
\nabla_{W^{(\ell)}}f=\frac1n\delta^{(\ell)}(h^{(\ell-1)})^T
\quad(\ell=2,3),\qquad
\nabla_{W^{(4)}}f=\frac1n h^{(3)}.
\]
For \(\mathcal L=(f-1)^2\), the candidate's physical equations are therefore the negative loss gradients with layer factors \(n,1,1,n\), respectively. Equivalently they are \(\dot X=2(1-f)F(X)\), with \(F\) defined by (A1). This is exactly the scaling fixed by the candidate, including the factor \(2\) from the loss and the absence of an extra \(1/n\) in the vector first-layer equation.

Differentiating \(z^{(2)}=W^{(2)}h^{(1)}\) gives
\[
\begin{split}
(z^{(2)})'
&=(W^{(2)})'h^{(1)}
 +W^{(2)}\operatorname{diag}(\phi'(z^{(1)}))(z^{(1)})'\\
&=\left[\frac{\|h^{(1)}\|^2}{n}I_2
 +W^{(2)}\operatorname{diag}(\phi'(z^{(1)})^2)(W^{(2)})^T\right]\delta^{(2)}.
\end{split}
\tag{A2}
\]
The second summand is the trained first-layer contribution. Differentiating \(z^{(3)}=W^{(3)}h^{(2)}\) and substituting (A2) gives
\[
\begin{split}
(z^{(3)})'={}&\left[\frac{\|h^{(2)}\|^2}{n}I_2
 +W^{(3)}\operatorname{diag}(\phi'(z^{(2)}))
 \left(\frac{\|h^{(1)}\|^2}{n}I_2
 +W^{(2)}\operatorname{diag}(\phi'(z^{(1)})^2)(W^{(2)})^T\right)
 \operatorname{diag}(\phi'(z^{(2)}))(W^{(3)})^T\right]\delta^{(3)}.
\end{split}
\tag{A3}
\]
Both identities hold at arbitrary feature time.

The proposed initial state is
\[
z^{(1)}(0)=\begin{pmatrix}\tan b\\\tan b\end{pmatrix},\quad
W^{(2)}(0)=2\tan(b)I_2,\quad
W^{(3)}(0)=\begin{pmatrix}1&-1-\epsilon/b\\-1&0\end{pmatrix},\quad
W^{(4)}(0)=0,\qquad 0\le\epsilon\le\tfrac14.
\tag{A4}
\]
Since \(b\in(-\pi/2,\pi/2)\) and \(2b=1\), these values yield
\[
h^{(1)}(0)=h^{(2)}(0)=(b,b)^T,\quad
z^{(2)}(0)=(\tan b,\tan b)^T,\quad
z^{(3)}(0)=(-\epsilon,-b)^T.
\]
All backpropagated vectors and all hidden parameter first derivatives vanish at time zero. Differentiating \(\delta^{(3)}\), however, gives
\[
(\delta^{(3)})'(0)
=\begin{pmatrix}
-\phi'(\epsilon)\phi(\epsilon)\\
-\phi'(b)\phi(b)
\end{pmatrix},
\tag{A5}
\]
because \((W^{(4)})'(0)=\phi(z^{(3)}(0))\) and the other product-rule term contains \(W^{(4)}(0)=0\).

Set
\[
\alpha=b^2+4\tan^2(b)\cos^4(b),\qquad
\kappa=\cos^4(b)\alpha>0.
\]
At initialization the bracket in (A2) is \(\alpha I_2\): its summands are \(b^2I_2\) and \(4\tan^2(b)\cos^4(b)I_2\). Each of the two additional diagonal factors in (A3) is \(\cos^2(b)I_2\). Differentiating (A3) at zero therefore yields exactly
\[
(z^{(3)})''(0)
=\left[b^2I_2+\kappa W^{(3)}(0)(W^{(3)}(0))^T\right]
\begin{pmatrix}
-\phi'(\epsilon)\phi(\epsilon)\\
-\phi'(b)\phi(b)
\end{pmatrix}.
\tag{A6}
\]
The differentiated bracket multiplies \(\delta^{(3)}(0)=0\), so it contributes nothing. The trained first layer has already contributed through \(\alpha\); it has not been dropped.

The Gram matrix is
\[
W^{(3)}(0)(W^{(3)}(0))^T
=\begin{pmatrix}1+(1+\epsilon/b)^2&-1\\-1&1\end{pmatrix}.
\]
Consequently
\[
L_\epsilon:=(z^{(3)}_1)''(0)
=L_0-\left[b^2+\kappa\bigl(1+(1+\epsilon/b)^2\bigr)\right]
\phi'(\epsilon)\phi(\epsilon),\qquad
L_0=\kappa\phi'(b)\phi(b)>0.
\tag{A7}
\]
For \(0\le\epsilon\le1/4\), the inequalities
\(1+(1+\epsilon/b)^2\le13/4\), \(0<\phi'(\epsilon)\le1\), and
\(0\le\phi(\epsilon)\le\epsilon\) prove
\[
0\le L_0-L_\epsilon\le C_L\epsilon,\qquad
C_L=b^2+\frac{13}{4}\kappa.
\tag{A8}
\]

Actual variation of every hidden parameter block follows from a separate differentiation:
\[
(\delta^{(2)})'(0)=\cos^2(b)
\begin{pmatrix}
\phi'(b)\phi(b)-\phi'(\epsilon)\phi(\epsilon)\\
(1+\epsilon/b)\phi'(\epsilon)\phi(\epsilon)
\end{pmatrix},
\qquad
(\delta^{(1)})'(0)=2\tan(b)\cos^2(b)(\delta^{(2)})'(0).
\]
For every \(\epsilon>0\), the second coordinate of \((\delta^{(2)})'(0)\) is positive. Hence
\[
(z^{(1)})''(0)\ne0,\qquad
(W^{(2)})''(0)=\frac1n(\delta^{(2)})'(0)(b,b)\ne0,\qquad
(W^{(3)})''(0)=\frac1n(\delta^{(3)})'(0)(b,b)\ne0.
\]
The last inequality uses the nonzero second coordinate in (A5). These nonzero second derivatives rule out constancy of the respective parameter blocks on any interval beginning at zero.

## 2. Common finite existence interval, symmetry, and remainders

The vector field \(F:\mathbb R^{12}\to\mathbb R^{12}\) is smooth, indeed real analytic: arctangent is real analytic at every real point, and the remaining operations preserve real analyticity. Only finitely many continuous derivatives are needed.

Let \(\mathcal K\) be the family (A4), including its closed range \([0,1/4]\), and retain the candidate's constants
\[
R=1+\max_{X\in\mathcal K}\|X\|,\qquad
\mathcal B=\{X:\|X\|\le R+1\},
\]
\[
M=1+\max_{\mathcal B}\|F\|,\qquad
\Lambda=1+\max_{\mathcal B}\|DF\|,\qquad
T=\min\left\{\frac1{4M},\frac1{2\Lambda},\frac1{\pi^2}\right\}>0.
\tag{A9}
\]
The family \(\mathcal K\) is a continuous image of a compact interval. The ball \(\mathcal B\) is compact in \(\mathbb R^{12}\); therefore these maxima exist and are finite. None depends on the individual \(\epsilon\).

For any \(\operatorname{dist}(\widetilde X(0),\mathcal K)\le1/4\), one has
\(\|\widetilde X(0)\|\le R-3/4\). The closed set of continuous paths on \([-T,T]\) with supremum distance at most \(1/2\) from \(\widetilde X(0)\) is complete in the supremum norm. Every such path takes values of norm at most \(R-1/4<R+1\), hence lies in \(\mathcal B\). On this set the integral map
\[
Y\longmapsto\left[s\longmapsto\widetilde X(0)+\int_0^sF(Y(u))\,du\right]
\]
has distance at most \(MT\le1/4\) from the constant initial path, so is a self-map. It has contraction factor at most \(\Lambda T\le1/2\), since the derivative bound on the convex ball implies that \(F\) is \(\Lambda\)-Lipschitz there.

The contraction fixed-point theorem gives one fixed point for a contraction self-map of a nonempty complete metric space; every hypothesis has just been checked. This fixed point solves the integral equation, is smooth by successive differentiation, and satisfies
\[
\|\widetilde X(s)-\widetilde X(0)\|\le M|s|\le\tfrac14
\quad(|s|\le T).
\tag{A10}
\]
The Lipschitz bound also proves uniqueness for overlapping solutions in \(\mathcal B\), on either side of zero. This establishes a common finite existence interval for the whole compact family and a neighborhood of it, without requiring global existence or any width limit.

For exactly zero initial readout, define
\[
\mathcal R(z^{(1)},W^{(2)},W^{(3)},W^{(4)})
=(z^{(1)},W^{(2)},W^{(3)},-W^{(4)}).
\]
Hidden components of \(F\) are linear in \(W^{(4)}\), while the readout component is independent of it. Therefore \(F(\mathcal RX)=-\mathcal RF(X)\). The path \(\mathcal RX(-s)\) solves the same equation, has the same initial value, and lies in the same path ball: \(\mathcal R\) is an isometry fixing that initial value. Uniqueness yields
\[
X(s)=\mathcal RX(-s).
\tag{A11}
\]
All hidden parameter blocks and hidden preactivations are even in feature time; the readout is odd. This assertion concerns feature time and exactly zero initial readout.

For a scalar state function \(G\), define \(D_FG=DG[F]\). Repeated chain rules identify its \(k\)-th derivative along a trajectory with \(D_F^kG\) at the current state. Let
\[
C_3=1+\frac1{24}\max_{\mathcal B}|D_F^4z^{(3)}_1|,\qquad
C_4=1+\frac1{120}\max_{\mathcal B}|D_F^5W^{(4)}_1|.
\tag{A12}
\]
These constants are finite by continuity on \(\mathcal B\), and the trajectories remain in that ball.

The needed form of Taylor's theorem is: a continuous \(m\)-th derivative bounded by \(A\) on the interval between \(0\) and \(s\) bounds the remainder after degree \(m-1\) by \(A|s|^m/m!\). Applying it with \(m=4\) and \(m=5\), using (A11), gives
\[
z^{(3)}_1(s)=-\epsilon+\frac12L_\epsilon s^2+R^{(3)}_\epsilon(s),
\qquad |R^{(3)}_\epsilon(s)|\le C_3|s|^4,
\tag{A13}
\]
\[
W^{(4)}_1(s)=-\arctan(\epsilon)s
 +\frac16\phi'(\epsilon)L_\epsilon s^3+R^{(4)}_\epsilon(s),
\qquad |R^{(4)}_\epsilon(s)|\le C_4|s|^5.
\tag{A14}
\]
Indeed, the linear readout coefficient is \(\phi(-\epsilon)\), and
\[
(W^{(4)}_1)'''(0)
=\phi''(-\epsilon)((z^{(3)}_1)'(0))^2
 +\phi'(-\epsilon)(z^{(3)}_1)''(0)
=\phi'(\epsilon)L_\epsilon.
\]
Parity removes precisely the other terms through the stated degrees. All bounds are uniform for \(0\le\epsilon\le1/4\) and \(|s|\le T\).

Applying Taylor's theorem directly to \((z^{(3)}_1)'\), through degree two, also gives
\[
|(z^{(3)}_1)'(s)-L_\epsilon s|
\le\frac{\max_{\mathcal B}|D_F^4z^{(3)}_1|}{6}|s|^3
\le4C_3|s|^3.
\tag{A15}
\]
This is a separate controlled-derivative estimate, not differentiation of a remainder bound.

## 3. Constants, the unique crossing, and the positive interval

Keep exactly
\[
K_3=\frac{2C_L}{L_0}+\frac{16C_3}{L_0^2},\qquad
K_4=1+\frac{2C_L}{3L_0}+\frac{16C_4}{L_0^2},
\]
\[
\epsilon_*=\min\left\{\frac14,\frac{L_0T^2}{64},
\frac1{2K_3},\frac1{6K_4}\right\}>0,\qquad
s_\epsilon=2\sqrt{\epsilon/L_0},\qquad 0<\epsilon\le\epsilon_*.
\tag{A16}
\]
All denominators are finite and positive. The second restriction gives \(s_\epsilon\le T/4\).

Substituting \(s_\epsilon^2=4\epsilon/L_0\) in (A13) gives
\[
z^{(3)}_1(s_\epsilon)-\epsilon
=\frac{2\epsilon}{L_0}(L_\epsilon-L_0)+R^{(3)}_\epsilon(s_\epsilon).
\]
Since \(s_\epsilon^4=16\epsilon^2/L_0^2\), (A8) and \(K_3\epsilon\le1/2\) prove
\[
|z^{(3)}_1(s_\epsilon)-\epsilon|\le K_3\epsilon^2,\qquad
\frac\epsilon2\le z^{(3)}_1(s_\epsilon)\le\frac{3\epsilon}{2}<1.
\tag{A17}
\]

The elementary bounds
\[
0\le\epsilon-\arctan\epsilon
=\int_0^\epsilon\frac{u^2}{1+u^2}\,du\le\frac{\epsilon^3}{3},
\qquad |\phi'(\epsilon)-1|\le\epsilon^2
\]
and the decomposition
\[
\phi'(\epsilon)L_\epsilon-L_0
=\phi'(\epsilon)(L_\epsilon-L_0)+L_0(\phi'(\epsilon)-1)
\]
give
\[
|\phi'(\epsilon)L_\epsilon-L_0|\le C_L\epsilon+L_0\epsilon^2.
\tag{A18}
\]
At \(s_\epsilon\), equation (A14) consequently implies
\[
\begin{split}
\left|\frac{W^{(4)}_1(s_\epsilon)}{s_\epsilon}+\frac\epsilon3\right|
&\le\frac{\epsilon^3}{3}
 +\frac{2\epsilon}{3L_0}(C_L\epsilon+L_0\epsilon^2)
 +\frac{16C_4}{L_0^2}\epsilon^2\\
&\le K_4\epsilon^2.
\end{split}
\tag{A19}
\]
The two cubic errors sum to \(\epsilon^3\le\epsilon^2\). Since \(K_4\epsilon\le1/6\),
\[
-\frac\epsilon2s_\epsilon
\le W^{(4)}_1(s_\epsilon)
\le-\frac\epsilon6s_\epsilon<0.
\tag{A20}
\]

For all \(0<s\le s_\epsilon\), (A8) and (A15) give
\[
(z^{(3)}_1)'(s)
\ge\left[L_0-C_L\epsilon-\frac{16C_3}{L_0}\epsilon\right]s
\ge\frac{L_0}{2}s>0,
\tag{A21}
\]
because \(C_L/L_0+16C_3/L_0^2\le K_3\).
Moreover
\(\phi'(\epsilon)L_\epsilon
=\phi'(\epsilon)L_0-\phi'(\epsilon)(L_0-L_\epsilon)\le L_0\).
Thus (A14) yields
\[
\begin{split}
\frac{W^{(4)}_1(s)}s
&\le-\epsilon+\frac{\epsilon^3}{3}+\frac{L_0s^2}{6}+C_4s^4\\
&\le-\frac\epsilon3+\frac{\epsilon^3}{3}
 +\frac{16C_4}{L_0^2}\epsilon^2
\le-\frac\epsilon6.
\end{split}
\tag{A22}
\]
The last two errors are at most \(K_4\epsilon^2\le\epsilon/6\). These computations verify all constants used to control the interval, not just the observation-time value.

The intermediate value theorem applies to the continuous \(z^{(3)}_1\), negative at zero and positive at \(s_\epsilon\), and gives a zero \(\tau_\epsilon\in(0,s_\epsilon)\). Strict monotonicity from (A21) makes that zero unique. The sign of \(\phi''(u)\) is opposite to that of \(u\), whereas (A22) keeps \(W^{(4)}_1\) negative. Therefore
\[
W^{(4)}_1(s)\phi''(z^{(3)}_1(s))
\begin{cases}
<0,&0<s<\tau_\epsilon,\\
=0,&s=\tau_\epsilon,\\
>0,&\tau_\epsilon<s\le s_\epsilon.
\end{cases}
\tag{A23}
\]
Since \((W^{(4)}_1)'=\arctan(z^{(3)}_1)\), the readout decreases until \(\tau_\epsilon\) and then increases, remaining negative through \(s_\epsilon\).

At the crossing, (A13) and \(\tau_\epsilon\le s_\epsilon\) imply
\[
\left|1-\frac{L_\epsilon\tau_\epsilon^2}{2\epsilon}\right|
\le\frac{16C_3}{L_0^2}\epsilon.
\]
Together with \(L_\epsilon\to L_0>0\), this proves
\[
\frac{\tau_\epsilon}{\sqrt{2\epsilon/L_0}}\longrightarrow1.
\tag{A24}
\]

For \(0<u\le1\), the explicit formula gives
\(-\phi''(u)=2u/(1+u^2)^2\ge u/2\).
By (A17) and (A20),
\[
W^{(4)}_1(s_\epsilon)\phi''(z^{(3)}_1(s_\epsilon))
\ge\frac{\epsilon s_\epsilon}{6}\frac\epsilon4
=\frac{\epsilon^{5/2}}{12\sqrt{L_0}}.
\tag{A25}
\]
The leading coefficient is also controlled:
\[
\frac{z^{(3)}_1(s_\epsilon)}\epsilon\to1,\qquad
\frac{W^{(4)}_1(s_\epsilon)}{\epsilon^{3/2}}\to-\frac2{3\sqrt{L_0}},\qquad
\frac{\phi''(z^{(3)}_1(s_\epsilon))}{\epsilon}\to-2,
\]
by (A17), (A19), and the formula for \(\phi''\). Their product proves the claimed limit \(4/(3\sqrt{L_0})\) after division of the curvature by \(\epsilon^{5/2}\).

## 4. Bounded parameters and the complete physical argument

Equation (A10) keeps the state in \(\mathcal B\). The activation bound yields
\[
\|h^{(\ell)}\|\le\frac{\pi\sqrt n}{2},\qquad
\|z^{(2)}\|,\ \|z^{(3)}\|\le(R+1)\frac{\pi\sqrt n}{2}.
\]
Here \(\|Av\|\le\|A\|_F\|v\|\) justifies the preactivation estimates. The vector \(z^{(1)}\) and all parameter blocks have ordinary norms at most \(R+1\). These are common bounds on the fixed finite feature-time interval.

For exactly zero initial readout, integration of (A1) gives
\[
\|W^{(4)}(s)\|\le\frac{\pi\sqrt n}{2}s,\qquad
|f(s)|\le\frac1n\|W^{(4)}(s)\|\|h^{(3)}(s)\|
\le\frac{\pi^2}{4}s\le\frac14
\quad(0\le s\le T).
\tag{A26}
\]
Thus \(2(1-f)\in[3/2,5/2]\). The function
\[
t(s)=\int_0^s\frac{du}{2(1-f(u))}
\]
is continuously differentiable, has derivative bounded away from zero, and satisfies
\[
\frac25s\le t(s)\le\frac23s.
\tag{A27}
\]
It therefore has an increasing inverse on \([0,t(T)]\), with derivative \(ds/dt=2(1-f)\). The chain rule shows that \(X(s(t))\) solves
\[
\dot z^{(1)}=2(1-f)\delta^{(1)},\qquad
\dot W^{(\ell)}=\frac{2(1-f)}n\delta^{(\ell)}(h^{(\ell-1)})^T
\quad(\ell=2,3),\qquad
\dot W^{(4)}=2(1-f)h^{(3)}.
\tag{A28}
\]
The smooth physical vector field also gives uniqueness on this interval through its local Lipschitz estimate.

For \(T_{\mathrm p}=T/4\) and \(t_\epsilon=t(s_\epsilon)\), equations (A16) and (A27) give
\[
0<t_\epsilon\le\frac23s_\epsilon\le\frac T6<T_{\mathrm p},\qquad
t(T)\ge\frac25T>T_{\mathrm p}.
\tag{A29}
\]
Thus the physical trajectory exists and remains bounded through the common horizon, and reaches the event before it. The positive interval (A23) becomes \((t(\tau_\epsilon),t(s_\epsilon)]\).

For perturbations in all twelve initial coordinates, fix one allowed \(\epsilon>0\). Subtracting the feature-time integral equations and using the Lipschitz bound gives
\[
\|\widetilde X(s)-X(s)\|
\le\|\widetilde X(0)-X(0)\|
 +\Lambda\int_0^s\|\widetilde X(u)-X(u)\|\,du.
\]
The needed integral inequality can be checked directly: if \(u\ge0\) is continuous and \(u(s)\le a+\Lambda\int_0^su(v)\,dv\), set \(v(s)=a+\Lambda\int_0^su(v)\,dv\). Then \(v'\le\Lambda v\), so \(v(s)\le ae^{\Lambda s}\), and the same bound holds for \(u\). Consequently
\[
\|\widetilde X(s)-X(s)\|
\le e^{\Lambda s}\|\widetilde X(0)-X(0)\|,
\qquad 0\le s\le T.
\tag{A30}
\]
The common existence argument applies whenever the initial distance from the reference state is at most \(1/4\).

Let
\[
C_f=1+\max_{\mathcal B}\|Df\|,\qquad
\eta_0=\min\left\{\frac14,\frac1{4C_fe^{\Lambda T}}\right\}.
\]
If \(\|\widetilde X(0)-X(0)\|<\eta_0\), the derivative bound on the convex ball and (A30) imply \(|\widetilde f(s)-f(s)|\le1/4\). Therefore \(|\widetilde f(s)|\le1/2\) for \(0\le s\le T\), and the perturbed inverse clock satisfies
\[
\frac13s\le\widetilde t(s)\le s,\qquad
\widetilde t(T)\ge T/3>T_{\mathrm p}.
\tag{A31}
\]
Every such perturbed physical trajectory exists through the same horizon and remains in \(\mathcal B\).

For \(G(X)=2(1-f(X))F(X)\), differentiation gives
\[
DG(X)[V]=2(1-f(X))DF(X)[V]-2Df(X)[V]F(X).
\]
It is continuous on \(\mathcal B\), so
\(\Lambda_{\mathrm p}=1+\max_{\mathcal B}\|DG\|<\infty\).
Both physical trajectories stay in the convex ball; subtracting their integral equations and applying the same inequality proves
\[
\|\widetilde X_{\mathrm{phys}}(t)-X_{\mathrm{phys}}(t)\|
\le e^{\Lambda_{\mathrm p}t}\|\widetilde X(0)-X(0)\|,
\qquad 0\le t\le T_{\mathrm p}.
\tag{A32}
\]
This compares trajectories at the same physical time, even though their feature clocks differ.

The open-neighborhood assertion can be made explicit. Define the smooth scalar state function
\[
H(X)=W^{(4)}_1\phi''(z^{(3)}_1(X)),\qquad
C_H=1+\max_{\mathcal B}\|DH\|,\qquad
m_\epsilon=\frac{\epsilon^{5/2}}{12\sqrt{L_0}}.
\]
The open ball about (A4) of radius
\[
\rho_\epsilon=\min\left\{
\eta_0,\frac{m_\epsilon}{2C_He^{\Lambda T}},
\frac{m_\epsilon}{2C_He^{\Lambda_{\mathrm p}T_{\mathrm p}}}
\right\}>0
\tag{A33}
\]
preserves \(H\ge m_\epsilon/2\) at the fixed feature time \(s_\epsilon\), by (A25) and (A30), and at the fixed physical time \(t_\epsilon\), by (A25) and (A32). The derivative bound for \(H\) is applicable because \(\mathcal B\) is convex. This ball is open in all twelve canonical coordinates, including the readout. It verifies the candidate's full continuity claim without relying on feature-time symmetry for the perturbed solutions.

## 5. Fixed-width Gaussian support and the exact-zero variation

At \(n=2\), the mutually independent canonical coordinates have variances
\[
\operatorname{Var}(z^{(1)}_i)=1,\qquad
\operatorname{Var}(W^{(2)}_{ij})=\operatorname{Var}(W^{(3)}_{ij})=\tfrac12,\qquad
\operatorname{Var}(W^{(4)}_i)=\tfrac14.
\]
Their twelve-dimensional joint density is the product of centered one-dimensional Gaussian densities of strictly positive variance. It is continuous and strictly positive everywhere on \(\mathbb R^{12}\). A nonempty open ball contains a smaller closed ball of positive radius. On this compact ball the density has a positive minimum, and its integral over the ball is strictly positive.

Apply this fact to (A33). Under the full canonical Gaussian law there is positive probability of trajectories existing through the common horizon and having strictly positive curvature at both fixed observation times. This argument uses the stated independent canonical coordinates and variances.

The full Gaussian readout assigns probability zero to the exact vector \(W^{(4)}(0)=0\). The preceding probability belongs to a full-dimensional neighborhood of that vector. For the separate variation with \(W^{(4)}(0)=0\) deterministically, the intersection of (A33) with that plane is a nonempty relatively open ball in the ten hidden coordinates. Their joint Gaussian density is positive everywhere on that ten-dimensional space, giving positive probability under the variation as well. This is a different initialization law; it does not assign positive full-Gaussian probability to the zero-readout slice.

Parity was used only for the exactly zero-readout construction. General readout perturbations were handled by full continuous dependence. These are finite-width, fixed-positive-time support conclusions: they provide no quantitative probability lower bound, no width-uniform probability, and no typical-population assertion.

## 6. Deterministic uniform fifth-order obstructions

For the compact family (A4), define
\[
P_\epsilon(s)=\frac1n\sum_{i=1}^n
\left[W^{(4)}_i(s;\epsilon)\phi''(z^{(3)}_i(s;\epsilon))\right]_+,
\qquad [a]_+=\max\{a,0\}.
\]
At \(s_\epsilon\), the first summand is strictly positive, and
\[
s_\epsilon^5=\frac{32\epsilon^{5/2}}{L_0^{5/2}}.
\]
Equation (A25) therefore implies
\[
\left[W^{(4)}_1(s_\epsilon;\epsilon)
\phi''(z^{(3)}_1(s_\epsilon;\epsilon))\right]_+
\ge\frac{L_0^2}{384}s_\epsilon^5.
\]
The other summands are nonnegative. With \(n=2\), this yields
\[
P_\epsilon(s_\epsilon)\ge\frac{L_0^2}{768}s_\epsilon^5.
\tag{A34}
\]
In particular, the factor \(1/n\) is correctly retained in the candidate's constant.

Suppose one function \(r(s)\), satisfying \(r(s)/s^5\to0\), and one common \(s_0>0\) obeyed \(P_\epsilon(s)\le r(s)\) for every \(\epsilon\in[0,1/4]\) and every \(0<s<s_0\). Taking \(\epsilon\downarrow0\) inside \((0,\epsilon_*]\) gives \(s_\epsilon\downarrow0\), eventually inside that interval. Equation (A34) then forces
\[
\frac{r(s_\epsilon)}{s_\epsilon^5}\ge\frac{L_0^2}{768}>0,
\]
contradicting the limit. The family is compact and its feature-time interval is common by Section 2. This proves precisely the asserted failure of a uniform \(o(s^5)\) upper bound.

In physical time let
\(P_\epsilon^{\mathrm{phys}}(t)=P_\epsilon(s(t;\epsilon))\), using each trajectory's own increasing clock. At \(t_\epsilon=t(s_\epsilon)\), equation (A27) gives \(s_\epsilon\ge(3/2)t_\epsilon\) and \(t_\epsilon\to0\). Hence
\[
P_\epsilon^{\mathrm{phys}}(t_\epsilon)
\ge\frac{L_0^2}{768}\left(\frac32\right)^5t_\epsilon^5.
\tag{A35}
\]
If one function \(r(t)=o(t^5)\) bounded every \(P_\epsilon^{\mathrm{phys}}(t)\) on one common interval \(0<t<t_0\le T_{\mathrm p}\), evaluation along \(t_\epsilon\) would contradict (A35). The direction of the clock inequality and the constant \((3/2)^5\) are correct.

These contradictions use an initialization varying with the shrinking observation time. They do not assert a nonzero fifth-order lower limit along one fixed initialization. Also, the support neighborhoods, for example (A33), depend on \(\epsilon\); their Gaussian probabilities have no uniform positive lower bound established here. An uncontrolled probability factor cannot turn these pointwise or deterministic-uniform conclusions into canonical Gaussian expectation sharpness. The candidate does not make that inference.

## Final scope determination

All scoped claims pass: the fully trained acceleration; compact fixed-width uniform existence and controlled remainders; feature-time symmetry; the unique crossing and positive interval with the displayed constants; the canonical loss clock and full physical continuity; the distinct full-Gaussian and deterministic-zero-readout support statements; and the deterministic uniform \(o(s^5)\) and \(o(t^5)\) obstructions.

The certified conclusions are finite-width sign-lag events and deterministic failures of a uniform fifth-order little-o improvement. No canonical expectation sharpness, width-uniform probability, global-in-time assertion, or counterexample to a global population theorem is certified.
