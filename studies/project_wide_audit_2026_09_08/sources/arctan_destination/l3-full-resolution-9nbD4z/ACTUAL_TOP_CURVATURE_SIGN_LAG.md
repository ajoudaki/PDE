# Actual top curvature: a fully trained, width-two sign-lag construction

Status: corrected candidate proof, pending isolated independent audit. This document contains a theoretical construction only; no experiments are used.

The assertion that every coordinate of the actual top curvature
\(W^{(4)}_i(s)\phi''(z^{(3)}_i(s))\) remains nonpositive from exactly zero readout is false for the stipulated feature-time dynamics. With all three hidden layers trained, the family below has a positive first coordinate at
\[
s_\epsilon=2\sqrt{\epsilon/L_0},
\]
for every sufficiently small positive \(\epsilon\). Here \(L_0>0\) is defined explicitly below. The construction gives a lower bound
\[
W^{(4)}_1(s_\epsilon)\phi''(z^{(3)}_1(s_\epsilon))
\ge \frac{\epsilon^{5/2}}{12\sqrt{L_0}}.
\]
All existence intervals and Taylor bounds are uniform over a compact family at the fixed width \(n=2\). The canonical physical trajectory for loss \((f-1)^2\) reaches the event within a common finite time. The strict event persists on an open set of initial conditions, including perturbations of the zero readout.

The proof first derives the exact top acceleration with the first-layer contribution included. A common compact neighborhood supplies uniform existence and derivative bounds. Time-reversal symmetry then supplies Taylor expansions with controlled remainders, which establish the sign lag. Finally, the canonical physical clock and continuous dependence give the trajectory and probability statements, followed by a deterministic obstruction to a uniform fifth-order little-o bound.

## 1. Canonical parameters and feature-time dynamics

Throughout, \(n=2\), \(b=1/2\), and
\[
\phi(u)=\arctan u,\qquad
\phi'(u)=\frac1{1+u^2},\qquad
\phi''(u)=-\frac{2u}{(1+u^2)^2}.
\]
The activation and its derivatives act coordinatewise. Vectors use the ordinary Euclidean norm, matrices the Frobenius norm, and derivatives of maps the induced operator norm between these Euclidean spaces. The notation \(\odot\) denotes coordinatewise multiplication, \(\operatorname{diag}(v)\) is the diagonal matrix with diagonal \(v\), and superscript \(T\) denotes the ordinary finite-dimensional transpose. Every occurrence of \(\phi'\) means the derivative explicitly displayed above.

For the single scalar input \(1\), the canonical first-layer parameter is the vector \(W^{(1)}=z^{(1)}\in\mathbb R^2\). The readout \(W^{(4)}\in\mathbb R^2\) is also a column vector, and \(W^{(2)},W^{(3)}\in\mathbb R^{2\times2}\). The complete canonical parameter tuple is
\[
X=(z^{(1)},W^{(2)},W^{(3)},W^{(4)})\in\mathbb R^{12},\qquad
\|X\|^2=\|z^{(1)}\|^2+\|W^{(2)}\|_F^2+\|W^{(3)}\|_F^2+\|W^{(4)}\|^2.
\]
Define
\[
h^{(\ell)}=\phi(z^{(\ell)})\quad(\ell=1,2,3),\qquad
z^{(2)}=W^{(2)}h^{(1)},\qquad z^{(3)}=W^{(3)}h^{(2)},
\]
\[
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\qquad
q^{(2)}=(W^{(3)})^T\delta^{(3)},\qquad
\delta^{(2)}=\phi'(z^{(2)})\odot q^{(2)},\qquad
\delta^{(1)}=\phi'(z^{(1)})\odot((W^{(2)})^T\delta^{(2)}).
\]
The feature-time equations, with prime denoting \(d/ds\), are exactly
\[
(z^{(1)})'=\delta^{(1)},\qquad
(W^{(2)})'=\frac1n\delta^{(2)}(h^{(1)})^T,\qquad
(W^{(3)})'=\frac1n\delta^{(3)}(h^{(2)})^T,\qquad
(W^{(4)})'=h^{(3)}.                                                   \tag{1}
\]

The first layer is trained by \((z^{(1)})'=\delta^{(1)}\), with no extra \(1/n\) factor. The two hidden matrices retain the explicit \(1/n\) factors shown in (1).

## 2. Initial family and exact acceleration

For \(0\le\epsilon\le1/4\), initialize
\[
z^{(1)}(0)=\begin{pmatrix}\tan b\\\tan b\end{pmatrix},\qquad
W^{(2)}(0)=2\tan(b)I_2,\qquad
W^{(3)}(0)=\begin{pmatrix}1&-1-\epsilon/b\\-1&0\end{pmatrix},\qquad
W^{(4)}(0)=0.                                                     \tag{2}
\]
Here \(I_2\) is the two-dimensional identity matrix. Since \(2b=1\), these initial values give
\[
h^{(1)}(0)=h^{(2)}(0)=\begin{pmatrix}b\\b\end{pmatrix},\qquad
z^{(2)}(0)=\begin{pmatrix}\tan b\\\tan b\end{pmatrix},\qquad
z^{(3)}(0)=\begin{pmatrix}-\epsilon\\-b\end{pmatrix}.
\]

Direct differentiation of (1), at arbitrary feature time, gives
\[
(z^{(2)})'
=\left[\frac{\|h^{(1)}\|^2}{n}I_2
 +W^{(2)}\operatorname{diag}\bigl(\phi'(z^{(1)})^2\bigr)(W^{(2)})^T\right]\delta^{(2)}
                                                               \tag{3}
\]
and
\[
\begin{split}
(z^{(3)})'={}&\left[\frac{\|h^{(2)}\|^2}{n}I_2
 +W^{(3)}\operatorname{diag}(\phi'(z^{(2)}))
 \left(\frac{\|h^{(1)}\|^2}{n}I_2
       +W^{(2)}\operatorname{diag}\bigl(\phi'(z^{(1)})^2\bigr)(W^{(2)})^T\right)
 \operatorname{diag}(\phi'(z^{(2)}))(W^{(3)})^T\right]\delta^{(3)}.
\end{split}                                                    \tag{4}
\]
For example, the second term in (3) is
\(W^{(2)}\operatorname{diag}(\phi'(z^{(1)}))(z^{(1)})'
=W^{(2)}\operatorname{diag}(\phi'(z^{(1)})^2)(W^{(2)})^T\delta^{(2)}\).
This is precisely the contribution of the trained first layer.

Define the positive scalar constants
\[
\alpha=b^2+4\tan^2(b)\cos^4(b),\qquad
\kappa=\cos^4(b)\alpha.
\]
At (2), the bracket in (3) is \(\alpha I_2\), because
\(\|h^{(1)}(0)\|^2/n=b^2\) and \(\phi'(\tan b)=\cos^2 b\).
Also \(\|h^{(2)}(0)\|^2/n=b^2\) and
\(\operatorname{diag}(\phi'(z^{(2)}(0)))=\cos^2(b)I_2\).

At feature time zero all hidden derivatives in (1) vanish, while
\[
(\delta^{(3)})'(0)=\phi'(z^{(3)}(0))\odot\phi(z^{(3)}(0)).
\]
Differentiating (4), its bracket-derivative term vanishes because \(\delta^{(3)}(0)=0\). Consequently the exact acceleration is
\[
(z^{(3)})''(0)=\left[b^2I_2+\kappa W^{(3)}(0)(W^{(3)}(0))^T\right]
          \bigl[\phi'(z^{(3)}(0))\odot\phi(z^{(3)}(0))\bigr].          \tag{5}
\]
For \(\epsilon>0\), the first-layer vector and both hidden matrices actually vary along this trajectory. Indeed,
\[
(\delta^{(2)}_2)'(0)
=\cos^2(b)(1+\epsilon/b)\phi'(\epsilon)\phi(\epsilon)>0,
\qquad
(\delta^{(1)})'(0)=2\tan(b)\cos^2(b)(\delta^{(2)})'(0).
\]
Since the initial backpropagated vectors vanish,
\[
(z^{(1)})''(0)=(\delta^{(1)})'(0)\ne0,\qquad
(W^{(2)})''(0)=\frac1n(\delta^{(2)})'(0)(h^{(1)}(0))^T\ne0,\qquad
(W^{(3)})''(0)=\frac1n(\delta^{(3)})'(0)(h^{(2)}(0))^T\ne0.
\]
The last inequality uses \((\delta^{(3)}_2)'(0)=-\phi'(b)\phi(b)\ne0\).

In particular, define
\[
L_\epsilon:=(z^{(3)}_1)''(0)
=\kappa\phi'(b)\phi(b)
 -\left[b^2+\kappa\bigl(1+(1+\epsilon/b)^2\bigr)\right]
   \phi'(\epsilon)\phi(\epsilon),
\]
\[
L_0:=\kappa\phi'(b)\phi(b)>0,\qquad
C_L:=b^2+\frac{13}{4}\kappa>0.
\]
Since \(0\le\epsilon/b\le1/2\), \(\phi'(\epsilon)\le1\), and \(0\le\phi(\epsilon)\le\epsilon\),
\[
0\le L_0-L_\epsilon\le C_L\epsilon
\qquad(0\le\epsilon\le1/4).                                  \tag{6}
\]
The positive limiting term in (5) comes from the off-diagonal entry \(-1\) of \(W^{(3)}(0)(W^{(3)}(0))^T\), multiplied by the negative second coordinate \(-\phi'(b)\phi(b)\).

## 3. A common finite interval and uniform Taylor bounds

Let \(F:\mathbb R^{12}\to\mathbb R^{12}\) be the vector field in (1), with all intermediate layer quantities defined above. It is real analytic on all of \(\mathbb R^{12}\): arctangent is real analytic at every real argument, and the remaining operations are finite sums and products. Only finitely many continuous derivatives will be needed.

Let \(\mathcal K\) be the set of initial states (2) for \(0\le\epsilon\le1/4\), a compact set by continuity of (2). Define
\[
R:=1+\max_{X\in\mathcal K}\|X\|,\qquad
\mathcal B:=\{X:\|X\|\le R+1\},
\]
\[
M:=1+\max_{X\in\mathcal B}\|F(X)\|,\qquad
\Lambda:=1+\max_{X\in\mathcal B}\|DF(X)\|,
\]
\[
T:=\min\left\{\frac1{4M},\frac1{2\Lambda},\frac1{\pi^2}\right\}>0.
                                                               \tag{7}
\]
These constants are finite and independent of \(\epsilon\).

Here are explicit existence and uniqueness checks. For any initial state \(\widetilde X(0)\) whose distance from \(\mathcal K\) is at most \(1/4\), consider continuous paths on \([-T,T]\) with supremum distance at most \(1/2\) from \(\widetilde X(0)\). Their states lie in \(\mathcal B\), since
\(\|\widetilde X(0)\|\le R-3/4\). The integral map
\[
Y(s)\longmapsto\widetilde X(0)+\int_0^sF(Y(u))\,du
\]
maps this complete closed path space into itself: its distance from the initial state is at most \(MT\le1/4\). It is a contraction with factor at most \(\Lambda T\le1/2\), because the convex ball \(\mathcal B\) and the derivative bound imply that \(F\) is \(\Lambda\)-Lipschitz there. The contraction fixed-point theorem therefore provides a unique solution in this space; the same Lipschitz estimate gives uniqueness wherever these solutions overlap in \(\mathcal B\). The integral equation and the smoothness of \(F\) give smooth solutions. In particular,
\[
\|\widetilde X(s)-\widetilde X(0)\|\le M|s|\le1/4
\quad (|s|\le T).                                             \tag{8}
\]
Thus the entire compact family, and a neighborhood of it, have bounded solutions on the same finite interval.

For a smooth scalar state function \(G\), write
\(D_FG(X)=DG(X)[F(X)]\), and define \(D_F^k\) by iteration. Along a solution, the \(k\)-th time derivative of \(G\) is \(D_F^kG\), by repeated application of the chain rule. Regard \(z^{(3)}_1\) and \(W^{(4)}_1\) as scalar functions of the canonical state, and set
\[
C_3:=1+\frac1{24}\max_{X\in\mathcal B}|D_F^4z^{(3)}_1(X)|,
\qquad
C_4:=1+\frac1{120}\max_{X\in\mathcal B}|D_F^5W^{(4)}_1(X)|.
                                                               \tag{9}
\]
These maxima are finite by continuity on the compact ball. They bound the required derivatives of the actual trajectories uniformly, without any width limit or formal-series assumption.

For the exactly zero readout family, the hidden states are even in \(s\), and the readout is odd. To verify this, define the linear involution
\[
\mathcal R(z^{(1)},W^{(2)},W^{(3)},W^{(4)})=(z^{(1)},W^{(2)},W^{(3)},-W^{(4)}).
\]
The hidden components of \(F\) are linear in \(W^{(4)}\), and the readout component is independent of \(W^{(4)}\). Hence
\(F(\mathcal RX)=-\mathcal RF(X)\).
The path \(\mathcal RX(-s)\) therefore solves the same equation as \(X(s)\), with the same initial state. Both paths are in the uniqueness neighborhood above, so \(X(s)=\mathcal RX(-s)\) on \([-T,T]\). In particular, \(z^{(1)}(s),W^{(2)}(s),W^{(3)}(s)\), and \(z^{(3)}(s)\) are even.

Taylor's theorem with its bounded-derivative remainder now gives, for \(|s|\le T\),
\[
z^{(3)}_1(s)=-\epsilon+\frac12L_\epsilon s^2+R^{(3)}_\epsilon(s),
\qquad |R^{(3)}_\epsilon(s)|\le C_3|s|^4,                       \tag{10}
\]
\[
W^{(4)}_1(s)=-\arctan(\epsilon)s
 +\frac16\phi'(\epsilon)L_\epsilon s^3+R^{(4)}_\epsilon(s),
\qquad |R^{(4)}_\epsilon(s)|\le C_4|s|^5.                      \tag{11}
\]
For (11), \((W^{(4)}_1)'(0)=\phi(-\epsilon)\), and differentiating \((W^{(4)}_1)'=\phi(z^{(3)}_1)\) twice gives
\((W^{(4)}_1)'''(0)=\phi'(\epsilon)L_\epsilon\), since \((z^{(3)}_1)'(0)=0\). Parity removes the other terms through degree four. Taylor's theorem applied directly to \((z^{(3)}_1)'\), using the same fourth derivative bound, also gives
\[
|(z^{(3)}_1)'(s)-L_\epsilon s|\le4C_3|s|^3.                     \tag{12}
\]
This last inequality is not obtained by differentiating an uncontrolled remainder.

## 4. Strict sign lag and the curvature lower bound

Define positive scalar constants
\[
K_3:=\frac{2C_L}{L_0}+\frac{16C_3}{L_0^2},\qquad
K_4:=1+\frac{2C_L}{3L_0}+\frac{16C_4}{L_0^2},
\]
\[
\epsilon_*:=\min\left\{\frac14,\frac{L_0T^2}{64},
                         \frac1{2K_3},\frac1{6K_4}\right\}>0.
                                                               \tag{13}
\]
Fix \(0<\epsilon\le\epsilon_*\). Then \(s_\epsilon=2\sqrt{\epsilon/L_0}\le T/4\). Equations (6) and (10) imply
\[
|z^{(3)}_1(s_\epsilon)-\epsilon|\le K_3\epsilon^2,
\qquad
\frac\epsilon2\le z^{(3)}_1(s_\epsilon)\le\frac{3\epsilon}{2}.
                                                               \tag{14}
\]
Indeed, the quadratic term differs from \(2\epsilon\) by at most \(2C_L\epsilon^2/L_0\), and the remainder is at most \(16C_3\epsilon^2/L_0^2\).

The elementary integral identity
\(\epsilon-\arctan\epsilon=\int_0^\epsilon u^2/(1+u^2)\,du\)
and the formula for \(\phi'\) give
\[
|\arctan\epsilon-\epsilon|\le\epsilon^3/3,\qquad
|\phi'(\epsilon)-1|\le\epsilon^2,
\]
\[
|\phi'(\epsilon)L_\epsilon-L_0|
\le C_L\epsilon+L_0\epsilon^2.
\]
Substituting these inequalities and \(s_\epsilon^2=4\epsilon/L_0\) into (11) yields
\[
\left|W^{(4)}_1(s_\epsilon)+\frac\epsilon3s_\epsilon\right|
\le K_4\epsilon^2s_\epsilon.
                                                               \tag{15}
\]
Here the two arctangent-derivative errors together contribute at most \(\epsilon^3s_\epsilon\), the acceleration error contributes at most \(2C_L\epsilon^2s_\epsilon/(3L_0)\), and the Taylor remainder contributes at most \(16C_4\epsilon^2s_\epsilon/L_0^2\). Thus
\[
-\frac\epsilon2s_\epsilon
\le W^{(4)}_1(s_\epsilon)
\le-\frac\epsilon6s_\epsilon<0.                              \tag{16}
\]

There is also a whole interval of sign lag. For \(0<s\le s_\epsilon\), (6), (12), and (13) show
\[
(z^{(3)}_1)'(s)
\ge\left[L_0-C_L\epsilon-\frac{16C_3}{L_0}\epsilon\right]s
\ge\frac{L_0}{2}s>0,                                        \tag{17}
\]
where \(C_L/L_0+16C_3/L_0^2\le K_3\). Also \(\phi'(\epsilon)L_\epsilon\le L_0\), so (11) implies
\[
\begin{split}
\frac{W^{(4)}_1(s)}s
&\le-\epsilon+\frac{\epsilon^3}{3}
          +\frac{L_0s^2}{6}+C_4s^4\\
&\le-\frac\epsilon3+\frac{\epsilon^3}{3}
          +\frac{16C_4}{L_0^2}\epsilon^2
\le-\frac\epsilon6.                                        \tag{18}
\end{split}
\]
For the last inequality use \(\epsilon\le1\) and \(K_4\epsilon\le1/6\).

By (14), (17), and \(z^{(3)}_1(0)=-\epsilon\), there is a unique
\(\tau_\epsilon\in(0,s_\epsilon)\) with \(z^{(3)}_1(\tau_\epsilon)=0\).
Throughout \((0,s_\epsilon]\), (18) keeps the readout coordinate negative. Therefore the actual curvature is negative on \((0,\tau_\epsilon)\), zero at \(\tau_\epsilon\), and positive on \((\tau_\epsilon,s_\epsilon]\). Since \((W^{(4)}_1)'=\phi(z^{(3)}_1)\), this coordinate of the readout decreases until \(\tau_\epsilon\), then increases but remains negative through \(s_\epsilon\). This is the asserted sign lag.

For completeness, (10) at \(\tau_\epsilon\), with
\(|R^{(3)}_\epsilon(\tau_\epsilon)|\le16C_3\epsilon^2/L_0^2\), gives
\[
\frac{\tau_\epsilon}{\sqrt{2\epsilon/L_0}}\longrightarrow1
\quad\text{as }\epsilon\downarrow0.                          \tag{19}
\]
Indeed, dividing that equation by \(\epsilon\) and using \(L_\epsilon\to L_0>0\) gives \(\tau_\epsilon^2/\epsilon\to2/L_0\).

At the specified observation time, (14) puts \(z^{(3)}_1\) in \([\epsilon/2,3\epsilon/2]\subset(0,1)\). For \(0<z\le1\),
\[
-\phi''(z)=\frac{2z}{(1+z^2)^2}\ge\frac z2.
\]
Combining this with (16) proves
\[
\begin{split}
W^{(4)}_1(s_\epsilon)\phi''(z^{(3)}_1(s_\epsilon))
&\ge\frac{\epsilon s_\epsilon}{6}\,\frac\epsilon4\\
&=c\epsilon^{5/2}>0,\qquad c:=\frac1{12\sqrt{L_0}}.           \tag{20}
\end{split}
\]
The leading coefficient is also determined by the controlled estimates:
\[
\frac{W^{(4)}_1(s_\epsilon)\phi''(z^{(3)}_1(s_\epsilon))}
     {\epsilon^{5/2}}
\longrightarrow\frac4{3\sqrt{L_0}}.                         \tag{21}
\]
In fact, (14) gives \(z^{(3)}_1(s_\epsilon)/\epsilon\to1\), (15) gives \(W^{(4)}_1(s_\epsilon)/\epsilon^{3/2}\to-2/(3\sqrt{L_0})\), and the explicit formula for \(\phi''\) gives \(\phi''(z^{(3)}_1(s_\epsilon))/\epsilon\to-2\).

## 5. Bounded canonical parameters and the physical clock

The canonical state stays in \(\mathcal B\) for \(|s|\le T\). Since \(\|h^{(\ell)}\|\le\pi\sqrt n/2\) for every hidden layer \(\ell\),
\[
\|z^{(2)}(s)\|,\ \|z^{(3)}(s)\|
\le(R+1)\frac{\pi\sqrt n}{2}.
\]
In particular, the first-layer vector satisfies \(\|z^{(1)}(s)\|\le R+1\), and \(W^{(2)},W^{(3)},W^{(4)}\) have their corresponding ordinary norms bounded by \(R+1\). All canonical parameters and preactivations are therefore bounded on the common finite feature-time interval.

The canonical output and loss are
\[
f=\frac1n(W^{(4)})^Th^{(3)},\qquad \mathcal L=(f-1)^2.
\]
With dot denoting physical time derivative, the canonical physical equations are directly
\[
\dot z^{(1)}=2(1-f)\delta^{(1)},\qquad
\dot W^{(\ell)}=\frac{2(1-f)}n\delta^{(\ell)} (h^{(\ell-1)})^T
\quad(\ell=2,3),\qquad
\dot W^{(4)}=2(1-f)h^{(3)}.                                         \tag{22}
\]
Thus the complete physical vector field is \(2(1-f)F\), and the feature clock satisfies
\[
\frac{ds}{dt}=2(1-f),\qquad s(0)=0.
\]

For the exactly zero readout family, \((W^{(4)})'=h^{(3)}\) implies
\[
\|W^{(4)}(s)\|\le\frac{\pi\sqrt n}{2}s,\qquad
|f(s)|\le\frac{\pi^2}{4}s\le\frac14
\quad(0\le s\le T),                                         \tag{23}
\]
using (7). The clock therefore has the explicit strictly increasing inverse
\[
t(s):=\int_0^s\frac{du}{2(1-f(u))},\qquad
\frac25s\le t(s)\le\frac23s.                                \tag{24}
\]
Composing the feature-time solution with the inverse of (24) and applying the chain rule proves that it solves (22). Define the finite common physical horizon
\(T_{\mathrm p}:=T/4\) and the observation time \(t_\epsilon:=t(s_\epsilon)\). Then
\[
0<t_\epsilon\le\frac23s_\epsilon\le\frac T6<T_{\mathrm p},
\qquad t(T)\ge\frac25T>T_{\mathrm p}.
\]
The bounded canonical physical trajectory is therefore defined through \(T_{\mathrm p}\), and (20) holds on it at \(t_\epsilon\). The positive-curvature interval is \((t(\tau_\epsilon),t(s_\epsilon)]\). No infinite-time claim is needed.

## 6. Open neighborhoods and the canonical Gaussian law

Fix one \(\epsilon\in(0,\epsilon_*]\); the observation times are now fixed positive numbers. For canonical initial states in the neighborhood used in Section 3, the integral equation, the \(\Lambda\)-Lipschitz bound, and Gronwall's inequality give
\[
\|\widetilde X(s)-X(s)\|
\le e^{\Lambda s}\|\widetilde X(0)-X(0)\|
\quad(0\le s\le T).                                         \tag{25}
\]
The version of Gronwall used here says that a nonnegative continuous function satisfying \(u(s)\le a+\Lambda\int_0^su(v)\,dv\), with \(a\ge0\), is bounded by \(ae^{\Lambda s}\). The difference of the two integral equations has exactly this form.

The function \(X\mapsto W^{(4)}_1\phi''(z^{(3)}_1)\) is smooth. Thus (20) and (25) imply that on some open neighborhood of (2), its value at the same feature time \(s_\epsilon\) is at least \(c\epsilon^{5/2}/2>0\). This neighborhood is open in all canonical coordinates, including the readout.

The same conclusion holds at the fixed physical time \(t_\epsilon\), after shrinking the neighborhood. To verify that the clock remains valid, define
\[
C_f:=1+\max_{X\in\mathcal B}\|Df(X)\|,\qquad
\eta_0:=\min\left\{\frac14,\frac1{4C_fe^{\Lambda T}}\right\}>0.
\]
If \(\|\widetilde X(0)-X(0)\|<\eta_0\), then (23), (25), and the derivative bound for \(f\) yield \(|\widetilde f(s)|\le1/2\) on \([0,T]\). Its inverse clock obeys
\[
\frac13s\le\widetilde t(s)\le s,
\]
so \(\widetilde t(T)\ge T/3>T_{\mathrm p}=T/4\), and the perturbed canonical physical trajectory also exists through \(T_{\mathrm p}\). The physical vector field is \(2(1-f)F\), whose derivative is bounded on \(\mathcal B\). More explicitly, the finite constant
\[
\Lambda_{\mathrm p}:=1+\max_{X\in\mathcal B}\|D(2(1-f)F)(X)\|
\]
gives the counterpart of (25) with \(e^{\Lambda_{\mathrm p}t}\) for \(0\le t\le T_{\mathrm p}\). Continuity of the same curvature function then preserves a lower bound \(c\epsilon^{5/2}/2\) at the fixed time \(t_\epsilon\) on a sufficiently small open neighborhood. Intersecting these neighborhoods preserves both the feature-time and physical-time statements.

This neighborhood is a nonempty open set in the complete canonical parameter space \((z^{(1)},W^{(2)},W^{(3)},W^{(4)})\in\mathbb R^{12}\).

At initialization, the canonical Gaussian law is
\[
z^{(1)}_i(0)\overset{\mathrm{iid}}{\sim}\mathcal N(0,1),\qquad
W^{(\ell)}_{ij}(0)\overset{\mathrm{iid}}{\sim}\mathcal N(0,1/n)
\quad(\ell=2,3),\qquad
W^{(4)}_i(0)\overset{\mathrm{iid}}{\sim}\mathcal N(0,n^{-2}),
\]
where all entries across all displayed layers are mutually independent and \(\mathcal N(0,v)\) denotes mean zero and variance \(v\). At \(n=2\), every variance is strictly positive. The resulting joint density on the canonical parameter space is continuous and positive everywhere. Every nonempty open set contains a closed ball of positive radius; the density has a positive minimum on that ball, so the open set has positive probability. Applied directly to the neighborhood just constructed, this proves a positive probability of the strict curvature event under the full canonical law, at the fixed feature time \(s_\epsilon\) and fixed physical time \(t_\epsilon\). This uses canonical readout values in a neighborhood of zero; it does not assign positive probability to an exactly zero Gaussian readout.

There is a distinct zero-readout variation: keep the canonical hidden Gaussian laws but set \(W^{(4)}(0)=0\) deterministically. The intersection of the neighborhood with \(W^{(4)}(0)=0\) is nonempty and open in the ten hidden coordinates. Their joint Gaussian density is positive everywhere, so this variation also gives the event positive probability. The time-reversal argument applies to exactly zero readout; the full canonical-law conclusion uses continuous dependence.

For each fixed positive \(\epsilon\), these are finite-width, finite-time support statements. They assert neither typical-population behavior nor a quantitative probability lower bound nor a nonvanishing probability as width grows.

## 7. Deterministic fifth-order sharpness consequence

For a real scalar \(a\), define its positive part by \([a]_+:=\max\{a,0\}\). In this paragraph display the family dependence explicitly as \(X_\epsilon\), and define
\[
P_\epsilon(s):=\frac1n\sum_{i=1}^n
 \left[W^{(4)}_i(s;\epsilon)\phi''(z^{(3)}_i(s;\epsilon))\right]_+.
\]
Because
\[
s_\epsilon^5=\frac{32\epsilon^{5/2}}{L_0^{5/2}},
\]
the one-coordinate estimate (20) gives
\[
\left[W^{(4)}_1(s_\epsilon;\epsilon)
       \phi''(z^{(3)}_1(s_\epsilon;\epsilon))\right]_+
\ge \frac{L_0^2}{384}s_\epsilon^5.
\]
The other positive parts are nonnegative. Hence at \(n=2\),
\[
P_\epsilon(s_\epsilon)\ge\frac{L_0^2}{768}s_\epsilon^5.        \tag{26}
\]
This rules out a uniform \(o(s^5)\) upper bound over the displayed compact zero-readout family \(\mathcal K\): a bound \(P_\epsilon(s)\le r(s)\) for every family member and every sufficiently small common \(s>0\), with \(r(s)/s^5\to0\), would contradict (26) as \(\epsilon\downarrow0\).

For physical time, let \(s(t;\epsilon)\) be the increasing feature clock of \(X_\epsilon\) and define \(P_\epsilon^{\mathrm{phys}}(t):=P_\epsilon(s(t;\epsilon))\). The physical observation times satisfy \(t_\epsilon\to0\) and \(t_\epsilon\le2s_\epsilon/3\) by (24). Thus
\[
P_\epsilon^{\mathrm{phys}}(t_\epsilon)
\ge\frac{L_0^2}{768}\left(\frac32\right)^5t_\epsilon^5.        \tag{27}
\]
If a single function \(r(t)\) with \(r(t)/t^5\to0\) bounded \(P_\epsilon^{\mathrm{phys}}(t)\) above for all family members on a common physical interval \(0<t<t_0\le T_{\mathrm p}\), then for small \(\epsilon\), (27) would imply
\[
\frac{r(t_\epsilon)}{t_\epsilon^5}
\ge\frac{L_0^2}{768}\left(\frac32\right)^5>0,
\]
a contradiction. This is a deterministic obstruction to a uniform \(o(t^5)\) positive-part upper bound; the witnessing initialization varies with the shrinking observation time. It does not establish power optimality for a canonical Gaussian expectation.

The construction refutes coordinatewise nonpositivity of the actual top curvature from exactly zero readout and gives the stated deterministic uniform-rate obstruction. It makes no claim that an entire canonical theorem fails.
