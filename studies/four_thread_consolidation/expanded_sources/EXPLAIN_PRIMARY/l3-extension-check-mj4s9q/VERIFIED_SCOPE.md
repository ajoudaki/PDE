# Three hidden layers: exact scope of the verified findings

This note does not claim the full infinite-width, continuous-time theorem. It proves global finite-width existence and shows that the width-uniform local-Lipschitz estimate used for two hidden layers fails near natural three-hidden-layer Euler states. Failure of this estimate is not a counterexample to existence or uniqueness of the desired limit.

## Model and finite-width bounds

The input and target are both 1, and \(\phi(s)=\arctan s\). At width \(n\), \(z^{(1)},W^{(4)}\in\mathbb R^n\), \(W^{(2)},W^{(3)}\in\mathbb R^{n\times n}\), and
\[
h^{(\ell)}=\phi(z^{(\ell)}),\quad
z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},\quad
f_n=(W^{(4)})^\top h^{(3)}/n,\quad r_n=f_n-1.
\]
The symbol \(W^{(4)}\) denotes the rescaled readout throughout. Independently,
\[
z_{0,i}^{(1)}\sim N(0,1),\quad W_{0,ji}^{(2)},W_{0,kj}^{(3)}\sim N(0,1/n),\quad W_{0,k}^{(4)}\sim N(0,n^{-2}).
\]
Define
\[
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\quad
\delta^{(2)}=\phi'(z^{(2)})\odot(W^{(3)})^\top\delta^{(3)},\quad
\delta^{(1)}=\phi'(z^{(1)})\odot(W^{(2)})^\top\delta^{(2)}.
\]
The normalized finite gradient flow is
\[
\dot z^{(1)}=-2r_n\delta^{(1)},\quad
\dot W^{(\ell)}=-\frac{2r_n}{n}\delta^{(\ell)}(h^{(\ell-1)})^\top\ (\ell=2,3),\quad
\dot W^{(4)}=-2r_n h^{(3)}.
\]
The chain rule gives
\[
\dot f_n=-2r_n\Theta_n,\quad
\Theta_n=\frac{\|\delta^{(1)}\|_2^2}{n}
+\frac{\|h^{(1)}\|_2^2\|\delta^{(2)}\|_2^2}{n^2}
+\frac{\|h^{(2)}\|_2^2\|\delta^{(3)}\|_2^2}{n^2}
+\frac{\|h^{(3)}\|_2^2}{n}\ge0.
\]
Thus \(\frac{d}{dt}r_n^2=-4r_n^2\Theta_n\le0\). Write \(R=|r_n(0)|\), \(c=\pi/2\), \(a(t)=\|W^{(4)}(t)\|_2/\sqrt n\), and \(M_\ell(t)=\|W^{(\ell)}(t)\|_{\rm op}\). Direct integration gives
\[
\begin{aligned}
a(t)&\le a(0)+2Rc t,\\
M_3(t)&\le M_3(0)+2Rc\int_0^t a(s)\,ds,\\
M_2(t)&\le M_2(0)+2Rc\int_0^t M_3(s)a(s)\,ds,\\
\frac{\|z^{(1)}(t)\|_2}{\sqrt n}
&\le\frac{\|z^{(1)}(0)\|_2}{\sqrt n}+2R\int_0^t M_2(s)M_3(s)a(s)\,ds.
\end{aligned}
\]
For example, \(\|\delta^{(3)}\|_2/\sqrt n\le a\), \(\|\delta^{(2)}\|_2/\sqrt n\le M_3a\), and the operator norm of a rank-one update is the product of the two vector norms divided by \(n\). Also \(\|W^{(4)}(t)\|_\infty\le\|W^{(4)}(0)\|_\infty+2Rc t\). These bounds prevent escape in any fixed finite dimension; the smooth finite-dimensional vector field therefore has a unique solution for all \(t\ge0\). The constants are width-uniform when the initial normalized vector norms and the two initial operator norms are bounded. These initial bounds hold with probability tending to one. Gaussian operator bounds follow, for example, from a fixed-radius sphere net and a Gaussian tail union bound.

## A precise failure of width-uniform stability

For this argument only, set the readout exactly to zero initially, as in the population oracle. Keep exactly the Gaussian first layer and hidden matrices specified above. After one Euler step of size \(\Delta>0\), the hidden parameters have not changed and
\[
W_1^{(4)}=2\Delta\phi(z_0^{(3)}),\quad
\delta_1^{(3)}=2\Delta\phi(z_0^{(3)})\odot\phi'(z_0^{(3)}).
\]
Choose \(0<\Delta<1/(4c^2)\). Then the residual at this state lies in \([-1,-1/2]\), because \(f_{n,1}=2\Delta\|h_0^{(3)}\|_2^2/n\le2\Delta c^2<1/2\).

Conditioning Gaussian rows of \(W_0^{(3)}\) on \(W_0^{(3)}h_0^{(2)}=z_0^{(3)}\) gives the exact conditional law
\[
(W_0^{(3)})^\top\delta_1^{(3)}
\overset d=
\frac{(z_0^{(3)})^\top\delta_1^{(3)}}{\|h_0^{(2)}\|_2^2}h_0^{(2)}
+\frac{\|\delta_1^{(3)}\|_2}{\sqrt n}
\left(I-\frac{h_0^{(2)}(h_0^{(2)})^\top}{\|h_0^{(2)}\|_2^2}\right)\gamma,
\]
where \(\gamma\sim N(0,I_n)\) is independent of that history.

The following elementary averaging details show that this backward field has arbitrarily large coordinates where \(z_0^{(2)}\in[1,2]\). Let \(Z_0^{(1)}\sim N(0,1)\), \(H_0^{(1)}=\phi(Z_0^{(1)})\); let \(Z_0^{(2)}\) be centered Gaussian of variance \(\mathbb E[(H_0^{(1)})^2]>0\), and set \(H_0^{(2)}=\phi(Z_0^{(2)})\). Let \(Z_0^{(3)}\) be centered Gaussian of variance \(\mathbb E[(H_0^{(2)})^2]>0\), and \(D=2\Delta\phi(Z_0^{(3)})\phi'(Z_0^{(3)})\). Conditional laws of large numbers for the two fresh forward calls give
\[
\frac{(z_0^{(3)})^\top\delta_1^{(3)}}{\|h_0^{(2)}\|_2^2}\longrightarrow
\frac{\mathbb E[Z_0^{(3)}D]}{\mathbb E[(H_0^{(2)})^2]}=:b,\qquad
\frac{\|\delta_1^{(3)}\|_2^2}{n}\longrightarrow\mathbb E[D^2]=:\sigma^2>0.
\]
The removed projection has normalized squared norm converging to zero: its conditional expectation is \(1/n\). Conditional averaging over \(\gamma\) therefore proves joint empirical convergence of
\[
\left(z_{0,j}^{(2)},\big[(W_0^{(3)})^\top\delta_1^{(3)}\big]_j\right)
\quad\hbox{to}\quad
\left(Z_0^{(2)},b\phi(Z_0^{(2)})+\sigma G\right),
\]
where \(G\sim N(0,1)\) is independent of \(Z_0^{(2)}\). Every set
\(\{1\le Z_0^{(2)}\le2,\ b\phi(Z_0^{(2)})+\sigma G>A\}\), for fixed \(A>0\), has positive probability and boundary probability zero. Consequently, for every fixed \(A\), with probability tending to one there is an index \(j\) in this set's finite-coordinate counterpart.

Localize to the event that both hidden operator norms are at most a fixed \(M\), and \(\|h_0^{(1)}\|_2/\sqrt n\) is bounded above and bounded away from zero. Its probability tends to one for sufficiently large fixed \(M\). Choose such an index \(j\), take \(A\ge1\), and perturb only the second weight matrix by
\[
\Delta W^{(2)}=\frac{A^{-1}e_j(h_0^{(1)})^\top}{\|h_0^{(1)}\|_2^2}.
\]
This changes \(z^{(2)}\) by exactly \(A^{-1}e_j\) and has operator norm
\[
\|\Delta W^{(2)}\|_{\rm op}=\frac{1}{A\|h_0^{(1)}\|_2}.
\]
On \([1,3]\), \(-\phi''\) is bounded below by a positive constant \(m\). Keeping the old backward field in the gate difference yields a coordinate of magnitude at least
\[
m A^{-1}\big[(W_0^{(3)})^\top\delta_1^{(3)}\big]_j\ge m.
\]
The backward field itself changes by at most \(C/(A\sqrt n)\) in normalized Euclidean norm. Indeed its expression is
\[
(W_0^{(3)})^\top\left[W_1^{(4)}\odot\phi'\!\left(W_0^{(3)}\phi(z^{(2)})\right)\right],
\]
and \(W_1^{(4)}\) is bounded coordinatewise, both activations are Lipschitz, and the operator norm of \(W_0^{(3)}\) is bounded. Therefore
\[
\frac{\|\delta^{(2)}_{\rm perturbed}-\delta^{(2)}_{\rm original}\|_2}{\sqrt n}
\ge\frac{m-C/A}{\sqrt n}.
\]
The residual changes by at most \(C/(A\sqrt n)\), and the normalized norm of the original \(\delta^{(2)}\) is bounded. Since \(|r_{n,1}|\ge1/2\), the second-matrix velocity difference consequently satisfies
\[
\|\dot W^{(2)}_{\rm perturbed}-\dot W^{(2)}_{\rm original}\|_{\rm op}
\ge\frac{c_1-C_1/A}{\sqrt n},
\]
with \(c_1>0\) independent of \(A,n\). Dividing by \(\|\Delta W^{(2)}\|_{\rm op}\) gives a lower bound \(c_2 A-C_2\). The constants depend on the fixed localization and \(\Delta\), not on \(A,n\).

Given any proposed width-independent Lipschitz constant, first choose \(A\) large enough, then let \(n\to\infty\). The perturbation tends to zero and the displayed ratio exceeds that constant with probability tending to one. Thus no width-uniform local-Lipschitz estimate in the state distance
\[
\frac{\|\Delta x^{(1)}\|_2}{\sqrt n}
+\|\Delta W^{(2)}\|_{\rm op}
+\|\Delta W^{(3)}\|_{\rm op}
+\frac{\|\Delta W^{(4)}\|_2}{\sqrt n},\qquad x^{(1)}=z^{(1)}+(z^{(1)})^3/3,
\]
can hold on these neighborhoods. This is a precise obstruction to reusing the two-hidden-layer proof's Lipschitz lemma. It is not a failure of finite-dimensional smoothness, and it does not imply nonuniqueness or failure of the infinite-width limit.

## What remains unproved

The full requested theorem still requires convergence as the number of Euler steps tends to infinity, unique autonomous population continuation on every fixed finite interval, and transfer to the prescribed joint regime \(\eta_n=n^{-2}\). Fixed finite-program convergence does not by itself prove these statements. The findings above neither prove nor refute them. A separate short-time response calculation has been explored, but it is not used or certified as a full theorem in this note.
