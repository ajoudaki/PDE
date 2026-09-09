# Exact finite-width GD: uniform interpolation from small readout initialization

This is a deterministic, self-contained candidate theorem. It concerns exact GD and does not assert closeness of GD states to gradient flow, nor any mean-field limit.

Write \(\|v\|_n=\|v\|_2/\sqrt n\), \(\langle u,v\rangle_n=u^Tv/n\), \(a=\pi/2\), and \(\phi=\arctan\). The state is \(\theta=(z_1,W_2,W_3,C)\), with
\[
h_1=\phi(z_1),\quad z_2=W_2h_1,\quad h_2=\phi(z_2),\quad
z_3=W_3h_2,\quad h=h_3=\phi(z_3),\quad f=\langle C,h\rangle_n.
\]
Let \(D_\ell=\operatorname{diag}\phi'(z_\ell)\),
\[
\delta_3=D_3C,\qquad\delta_2=D_2W_3^T\delta_3,
\qquad\delta_1=D_1W_2^T\delta_2.
\]
For \(\eta=n^{-2}\), exact GD is
\[
\alpha_k=2\eta(1-f_k),\quad
z_{1,k+1}=z_{1,k}+\alpha_k\delta_{1,k},\quad
W_{\ell,k+1}=W_{\ell,k}+\frac{\alpha_k}{n}\delta_{\ell,k}h_{\ell-1,k}^T\ (\ell=2,3),\quad
C_{k+1}=C_k+\alpha_k h_k.
\]

**Theorem.** For every \(M<\infty\) and \(0<b\le a\), there are explicit constants \(\varepsilon_0(M,b)>0\), \(N(M,b)<\infty\), and \(V(M,b)<\infty\) with the following property. For every \(n\ge N\), assume
\[
\|W_{2,0}\|_{\rm op},\|W_{3,0}\|_{\rm op},\|z_{1,0}\|_n\le M,
\qquad \|C_0\|_n\le\varepsilon_0,
\qquad \|h_0\|_n\ge b.
\]
Then every iterate satisfies
\[
f_0<f_1<\cdots<1,\qquad \|h_k\|_n\ge b/2,
\qquad 0<1-f_k\le (1-f_0)(1-\eta b^2/4)^k.
\]
Moreover,
\[
\sum_{k\ge0}\alpha_k\le\frac{8(1-f_0)}{b^2},
\qquad \sum_{j\ge k}\alpha_j\le\frac{8(1-f_k)}{b^2}.
\]
The entire parameter sequence converges to a finite endpoint \(\theta_\infty\) with \(f(\theta_\infty)=1\). In the metric
\[
d(\theta,\widetilde\theta)=\max\{\|z_1-\widetilde z_1\|_n,
\|W_2-\widetilde W_2\|_{\rm op},\|W_3-\widetilde W_3\|_{\rm op},\|C-\widetilde C\|_n\},
\]
one has \(d(\theta_k,\theta_\infty)\le8V(1-f_k)/b^2\). All constants are independent of \(n\). An initial bound \(\|C_0\|_\infty\le\varepsilon_0\) may be imposed but is not needed for this theorem.

## Constants and bounded feature-action paths

Set
\[
S=32/b^2,\quad Q=1+aS,\quad R_3=M+aQS,\quad R_2=M+aR_3QS,
\quad L=a^2+R_3^2(a^2+R_2^2).
\]
On any sequence of the displayed Euler updates with nonnegative step lengths whose cumulative sum is at most \(S\), and initial \(\|C_0\|_n\le1\),
\[
\|C\|_n\le Q,\quad\|W_3\|_{\rm op}\le R_3,\quad\|W_2\|_{\rm op}\le R_2.
\]
Indeed, \(\|h_\ell\|_n\le a\), while the feature-time velocities of \(C,W_3,W_2\) have norms at most \(a,a\|C\|_n,a\|W_3\|_{\rm op}\|C\|_n\), respectively. The same bounds hold on each straight Euler segment if its feature time is at most \(S\). The velocity of \(z_1\) has normalized norm at most \(R_2R_3Q\). Take
\[
V=\max\{a,aQ,aR_3Q,R_2R_3Q\}.
\]

Here are explicit constants for the feature Taylor error. Set
\[
v=R_2R_3Q,\quad A_2=aR_3Q,\quad A_3=aQ,
\quad v_2=aA_2+R_2v,
\]
\[
u_2=2v_2^2+2A_2v+2R_2v^2,
\quad v_3=aA_3+R_3v_2,
\quad B=v_3^2+A_3v_2+(R_3/2)u_2.
\]
Also put
\[
D=2aL+B,\quad F=Q(aL+B),\quad K_*=a^2+LQ^2,
\]
\[
t_0=\min\{1,S/4,\sqrt{b/(384aL)}\},\quad d=bt_0/32,
\quad\varepsilon_0=\min\{1,1/(2a),bt_0/32\}.
\]
Choose \(N\) so that for all \(n\ge N\), with \(A=4n^{-2}\),
\[
A\le\min\{t_0,d/a,S/2\},\quad
2Bt_0A\sqrt n\le b/64,\quad
DSA\sqrt n\le b/4,
\]
\[
FA\sqrt n\le\min\{b^2/8,1\},\qquad
2n^{-2}(K_*+1)\le1/2.
\]
Such an \(N\) exists because \(A\sqrt n=4n^{-3/2}\).

## Exact directional identity and local defect

The feature vector field \(G\) is the vector multiplying \(\alpha\) in the Euler updates. Its directional derivative on \(h\) is
\[
Dh(\theta)G(\theta)=P(\theta)C,
\]
where, with \(m_\ell=\|h_\ell\|_n^2\),
\[
P=D_3\big[m_2I+W_3D_2(m_1I+W_2D_1^2W_2^T)D_2W_3^T\big]D_3.
\]
To see this, differentiate successively along \(G\):
\[
\dot h_1=D_1^2W_2^TD_2W_3^TD_3C,
\quad \dot z_2=(m_1I+W_2D_1^2W_2^T)D_2W_3^TD_3C,
\]
\[
\dot z_3=m_2D_3C+W_3D_2\dot z_2,\qquad\dot h=D_3\dot z_3.
\]
The displayed factorization gives \(P\succeq0\), and the bounds above give \(\|P\|_{\rm op}\le L\).

For one frozen Euler segment \(\theta(u)=\theta+uG(\theta)\), the derivatives satisfy
\[
\|h_1'\|_n\le v,\quad \|h_1''\|_n\le2\sqrt n\,v^2,
\quad\|z_2'\|_n\le v_2,\quad\|h_2''\|_n\le\sqrt n\,u_2,
\quad\|z_3'\|_n\le v_3.
\]
These follow by the product and chain rules, \(|\phi'|\le1\), \(|\phi''|\le2\), and
\(\|w\odot w\|_n\le\sqrt n\|w\|_n^2\). For example,
\(z_2''=2W_2'h_1'+W_2(u)h_1''\),
and the analogous identity at layer three yields
\[
\sup_u\|h''(u)\|_n\le2B\sqrt n.
\]
Taylor's formula with an integral remainder therefore gives the exact relation
\[
h_{k+1}=h_k+\alpha_kP_kC_k+e_k,
\qquad\|e_k\|_n\le B\sqrt n\,\alpha_k^2. \tag{1}
\]
Because \(C_{k+1}=C_k+\alpha_kh_k\),
\[
f_{k+1}-f_k=\alpha_kK_k+\rho_k,
\quad K_k=\|h_k\|_n^2+\langle C_k,P_kC_k\rangle_n,
\tag{2}
\]
\[
|\rho_k|\le F\sqrt n\,\alpha_k^2,\qquad
\|h_k\|_n^2\le K_k\le K_*.
\]
Indeed, the remainder equals
\(\alpha_k^2\langle h_k,P_kC_k\rangle_n+\langle C_{k+1},e_k\rangle_n\).

## The readout norm is almost convex in feature time

We prove a statement independent of the residual: on any finite positive-step Euler path with \(\alpha_k\le A\) and total feature time at most \(S\), one has \(\|h_k\|_n\ge b/2\).

Write \(s_k=\sum_{j<k}\alpha_j\), and interpolate \(C\) linearly on \([s_k,s_{k+1}]\). Its slope there is \(h_k\). Let
\[
q(s)=\sqrt{\|C(s)\|_n^2+d^2}.
\]
On each open segment,
\[
q''(s)=\frac{\|h_k\|_n^2q(s)^2-\langle C(s),h_k\rangle_n^2}{q(s)^3}\ge0.
\]
At a knot, (1) and \(P_k\succeq0\) imply
\[
q'(s_{k+1}+)-q'(s_{k+1}-)
=\frac{\langle C_{k+1},\alpha_kP_kC_k+e_k\rangle_n}{q(s_{k+1})}
\ge-D\sqrt n\,\alpha_k^2. \tag{3}
\]
For the last inequality expand \(C_{k+1}=C_k+\alpha_kh_k\). The term \(\alpha_k\langle C_k,P_kC_k\rangle_n/q\) is nonnegative, the error involving \(e_k\) is at least \(-\|e_k\|_n\), and
\[
\frac{\|C_k\|_n}{q(s_{k+1})}\le1+\frac{\alpha_ka}{d}\le2.
\]
Thus the remaining negative term is at most \(2aL\alpha_k^2\).

For every node with \(s_k\le2t_0\), (1) gives
\[
\|h_k-h_0\|_n
\le Ls_k(\varepsilon_0+as_k)+B\sqrt n\,A s_k
\le6aLt_0^2+2Bt_0A\sqrt n\le b/32. \tag{4}
\]
In particular, the claimed lower bound holds on this initial interval. If the path extends beyond \(2t_0\), let \(k_0\) be the first index with \(s_{k_0}\ge t_0\). Then \(t_0\le s_{k_0}\le2t_0\), and (4) and linear interpolation imply
\[
C_{k_0}/s_{k_0}=h_0+u,\quad \|u\|_n\le b/16,
\qquad h_{k_0}=h_0+w,\quad \|w\|_n\le b/32,
\quad d/s_{k_0}\le b/32.
\]
Writing \(H=\|h_0\|_n\ge b\), we obtain
\[
q'(s_{k_0}+)
\ge\frac{H^2-3Hb/32-b^2/512}{H+3b/32}
\ge\frac{463}{560}H\ge3b/4.
\]
Using (3), segmentwise convexity, and \(\sum\alpha_k^2\le A\sum\alpha_k\), at every later node
\[
q'(s_k+)\ge3b/4-D\sqrt n\sum_j\alpha_j^2
\ge3b/4-DSA\sqrt n\ge b/2.
\]
But \(q'(s_k+)=\langle C_k,h_k\rangle_n/q(s_k)\le\|h_k\|_n\), proving the required readout bound. At a final node the right derivative means the algebraic value \(\langle C_k,h_k\rangle_n/q(s_k)\), or equivalently the derivative obtained by extending just that final linear segment.

## Closing the exact GD bootstrap and taking the endpoint

Initially, \(|f_0|\le a\varepsilon_0\le1/2\), so \(e_0=1-f_0\in[1/2,3/2]\). Suppose a finite exact-GD prefix satisfies \(f_0\le f_k<1\) and
\[
s_k\le\frac8{b^2}(f_k-f_0)\le\frac{8e_0}{b^2}\le S/2.
\]
Then \(0<\alpha_k=2n^{-2}(1-f_k)\le A\), and \(s_{k+1}\le S\). The path bounds, the readout lemma, and (2) apply. The conditions defining \(N\) yield
\[
\frac{b^2}{8}\alpha_k\le f_{k+1}-f_k
\le\alpha_k(K_*+1)\le\frac{1-f_k}{2}. \tag{5}
\]
Consequently \(f_k<f_{k+1}<1\), and summing the lower bound gives
\(s_{k+1}\le8(f_{k+1}-f_0)/b^2\le S/2\).
This closes the induction for every iteration, so the feature horizon cannot escape the bounded region used in the proof.

The lower bound in (5), together with \(\alpha_k=2\eta(1-f_k)\), gives
\[
1-f_{k+1}\le(1-\eta b^2/4)(1-f_k),
\]
and hence \(f_k\to1\). Summing (5) from \(k\) to infinity proves the tail-action estimate. Each state increment in the metric \(d\) is at most \(V\alpha_k\). Since their norms are summable, the parameters converge in the finite-dimensional state space; the same tail estimate gives the stated convergence rate, and continuity of \(f\) gives \(f(\theta_\infty)=1\).

The summable quantity is the residual-weighted physical-time action \(\sum\eta(1-f_k)=\frac12\sum\alpha_k\), not the sum of the fixed physical-time steps \(\sum\eta\), which is infinite.

The width threshold matters: fixed \(\eta=n^{-2}\) need not prevent overshoot at every small width under arbitrary \(M\). No claim about correspondence of these endpoints across widths, gradient-flow/GD state closeness, or a mean-field endpoint has been used or proved.
