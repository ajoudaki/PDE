# Finite optimization and energy-compatible controls

This chapter proves finite-width optimization for the canonical three-hidden-layer
arctangent network: global gradient-flow coercivity and fitting, exact raw-GD
coercivity and fitting at step \(\eta_n=n^{-2}\), and convergence of every
parameter to a finite interpolating endpoint. It also proves a global
finite-dimensional theorem for an auxiliary metric projection, its integrated
\(L^1\) equation defect, and eventual exact agreement with the canonical flow
at each fixed width. All proof ingredients and Gaussian initial conditions are
given below.

The conventions agree with [NOTATION.md](NOTATION.md), the general identities
in [finite_dynamics.md](finite_dynamics.md), and the
[three-hidden-layer arctangent model](arctan_limits.md#l3-local).
The results here concern finite widths. They assert neither a global uncut
three-layer population flow nor a population limit or GD theorem for the
metric projection. No width limit is interchanged with infinite training time.

## 1. Canonical model, metric, and clocks

Fix a positive integer \(n\), one input \(x=1\), and one target \(y=1\).
Thus \(L=3\) and \(m=d=1\). Put \(c=\pi/2\) and
\(\phi(z)=\arctan z\). Coordinatewise,
\[
 |\phi|\le c,\qquad \phi(0)=0,\qquad
 \phi'(z)=\frac1{1+z^2},\qquad |\phi'|\le1,\qquad |\phi''|\le2.
 \tag{1.1}
\]
The raw state is
\(\theta=(z^{(1)},W^{(2)},W^{(3)},W^{(4)})\), where
\(z^{(1)}=W^{(1)}\) and the stored readout \(W^{(4)}\) are in
\(\mathbb R^n\), and the two middle matrices are in
\(\mathbb R^{n\times n}\). Define
\[
 h^{(1)}=\phi(z^{(1)}),\quad z^{(2)}=W^{(2)}h^{(1)},\quad
 h^{(2)}=\phi(z^{(2)}),\quad z^{(3)}=W^{(3)}h^{(2)},\quad
 h^{(3)}=\phi(z^{(3)}),
\]
\[
 f_n=\frac{(W^{(4)})^Th^{(3)}}n,\qquad
 r_n=f_n-1,\qquad \mathcal L_n=r_n^2.
 \tag{1.2}
\]
At a fixed width write \(f=f_n\), \(r=r_n\). The norm \(\|\cdot\|_2\) is the
ordinary Euclidean norm and \(\|v\|_\infty=\max_i|v_i|\). Matrix norms are
explicitly operator or Frobenius norms, and every factor \(1/n\) or
\(1/\sqrt n\) is displayed. For the diagonal
matrices \(D_\ell=\operatorname{diag}(\phi'(z^{(\ell)}))\), let
\[
 \delta^{(3)}=D_3W^{(4)},\qquad q^{(2)}=(W^{(3)})^T\delta^{(3)},\qquad
 \delta^{(2)}=D_2q^{(2)},\qquad
 \delta^{(1)}=D_1(W^{(2)})^T\delta^{(2)}.
 \tag{1.3}
\]
These are derivatives of the prediction:
\(\delta^{(\ell)}=n\,\partial f/\partial z^{(\ell)}\). They contain no
residual. In fact the chain rule, applied from the readout downwards, gives
\[
 df=\frac{(\delta^{(1)})^Tdz^{(1)}}n
    +\sum_{\ell=2}^3\frac{(\delta^{(\ell)})^T(dW^{(\ell)})h^{(\ell-1)}}n
    +\frac{(h^{(3)})^TdW^{(4)}}n.
\]
The block mobilities are \(n,1,1,n\), with all fixed
\(\kappa_\ell=1\); their parameter quadratic form is
\[
 \frac{\|dz^{(1)}\|_2^2}{n}
 +\|dW^{(2)}\|_{\rm F}^2+\|dW^{(3)}\|_{\rm F}^2
 +\frac{\|dW^{(4)}\|_2^2}{n}.
 \tag{1.4}
\]
Define the feature vector field
\[
 \mathcal G(\theta)=\left(
 \delta^{(1)},\ \frac{\delta^{(2)}(h^{(1)})^T}{n},\
 \frac{\delta^{(3)}(h^{(2)})^T}{n},\ h^{(3)}\right).
 \tag{1.5}
\]
The canonical physical gradient flow and exact simultaneous raw GD are
\[
 \frac{d\theta}{dt}=-2r\,\mathcal G(\theta),\qquad
 \theta_{k+1}=\theta_k-2\eta_n r_k\mathcal G(\theta_k),
 \qquad \eta_n=n^{-2},\quad t_k=k\eta_n.
 \tag{1.6}
\]
Every block on the right is evaluated before the update. Between GD nodes the
raw parameters are linearly interpolated and the hidden quantities recomputed.
The GD fitting inequalities proved below apply at the nodes.

Feature time \(s\) solves \(d\theta/ds=\mathcal G(\theta)\). Its relation
to physical gradient flow is \(ds/dt=2(1-f)=-2r\) while this is positive;
positivity will be proved. For GD, \(\alpha_k=2\eta_n(1-f_k)\) and
\(s_k=\sum_{j<k}\alpha_j\) are computational clock variables. They neither
change the raw update nor discretize a transformed coordinate. In particular,
the continuous identity for \(F(z)=z+z^3/3\) is not used as an exact GD rule.

## 2. Global feature flow and readout acceleration

**Lemma 2.1 (finite feature existence and exact action).** For every finite
initial state, (1.5) has a unique solution for all \(s\ge0\). Define
\[
 \mathsf A_2=\frac{\|h^{(1)}\|_2^2}{n}I+W^{(2)}D_1^2(W^{(2)})^T,
\]
\[
 \mathsf A_3=\frac{\|h^{(2)}\|_2^2}{n}I
       +W^{(3)}D_2\mathsf A_2D_2(W^{(3)})^T,
 \qquad P=D_3\mathsf A_3D_3.
 \tag{2.1}
\]
All three matrices are positive semidefinite. A prime on a state variable in
this section denotes \(d/ds\). Then
\[
 (z^{(2)})'=\mathsf A_2\delta^{(2)},\qquad
 (z^{(3)})'=\mathsf A_3\delta^{(3)},\qquad
 (W^{(4)})''=(h^{(3)})'=PW^{(4)},
 \tag{2.2}
\]
and the exact scalar kernel is
\[
 \begin{aligned}
 K_n=f'&=\frac{\|h^{(3)}\|_2^2}{n}+
                \frac{(W^{(4)})^TPW^{(4)}}{n}\\
 &=\frac{\|h^{(3)}\|_2^2}{n}
  +\frac{\|\delta^{(3)}\|_2^2\|h^{(2)}\|_2^2}{n^2}
  +\frac{\|\delta^{(2)}\|_2^2\|h^{(1)}\|_2^2}{n^2}
  +\frac{\|\delta^{(1)}\|_2^2}{n}\\
 &=\frac{\|(z^{(1)})'\|_2^2}{n}
   +\|(W^{(2)})'\|_{\rm F}^2+\|(W^{(3)})'\|_{\rm F}^2
   +\frac{\|(W^{(4)})'\|_2^2}{n}.
 \end{aligned}
 \tag{2.3}
\]

**Proof.** The raw vector field is smooth. On a sufficiently small closed ball,
its integral map on continuous paths is a contraction when the time interval
is smaller than the reciprocal of its Lipschitz constant and its bounded
speed keeps paths in the ball. This proves local existence and uniqueness.
To exclude finite escape, set
\(\varepsilon=\|W^{(4)}(0)\|_2/\sqrt n\) and
\(M_j=\|W^{(j)}(0)\|_{\rm op}\), \(j=2,3\). Successive integration of
(1.5), using \(\|uv^T/n\|_{\rm F}=\|u\|_2\|v\|_2/n\), gives
\[
 \frac{\|W^{(4)}(s)\|_2}{\sqrt n}\le\varepsilon+cs,
 \qquad
 \|W^{(3)}(s)\|_{\rm op}
 \le M_3+c\varepsilon s+\frac{c^2s^2}{2}=:\mathcal M_3(s),
\]
\[
 \|W^{(2)}(s)\|_{\rm op}
 \le M_2+c\int_0^s\mathcal M_3(u)(\varepsilon+cu)\,du
 =:\mathcal M_2(s),
\]
\[
 \frac{\|z^{(1)}(s)-z^{(1)}(0)\|_2}{\sqrt n}
 \le\int_0^s\mathcal M_2(u)\mathcal M_3(u)(\varepsilon+cu)\,du.
 \tag{2.4}
\]
The matrix increment bounds also hold in Frobenius norm. These are finite
polynomials on bounded intervals. At fixed \(n\), they bound all raw
parameters in a compact set; the smooth field is bounded there, so a solution
has a finite limit at a proposed finite endpoint. The local construction
extends it, proving global existence.

Differentiating \(h^{(1)}\) gives
\((h^{(1)})'=D_1^2(W^{(2)})^T\delta^{(2)}\). The two terms in the
product derivative of \(W^{(2)}h^{(1)}\) give \(\mathsf A_2\delta^{(2)}\).
Differentiating \(W^{(3)}h^{(2)}\), and then applying \(D_3\), gives (2.2).
Matrices of the form \(BB^T\), nonnegative scalar multiples of the identity,
and congruences of positive semidefinite matrices are positive semidefinite;
this verifies the positivity in (2.1). Differentiating (1.2) using (2.2)
proves the first line of (2.3). Expanding (2.1) gives its four kernel blocks.
The rank-one Frobenius identity above gives its squared-speed expression. ∎

In particular, wherever \(g(s)=\|W^{(4)}(s)\|_2/\sqrt n>0\),
\[
 g'=\frac f g,\qquad
 g''=\frac{\|h^{(3)}\|_2^2/n-(g')^2+(W^{(4)})^TPW^{(4)}/n}{g}\ge0.
 \tag{2.5}
\]
The first two numerator terms have nonnegative sum by Cauchy–Schwarz, and
the last is nonnegative by (2.1). This is convexity of the readout norm on
its nonzero intervals, with no assertion about individual coordinate signs.

## 3. Canonical gradient-flow coercivity, fitting, and endpoints

**Theorem 3.1 (zero and small stored readout).** There are two deterministic
initialization cases.

For zero readout \(W^{(4)}(0)=0\), assume
\(\mu=\|h^{(3)}(0)\|_2^2/n>0\). Then for all feature times,
\[
 \frac{\|W^{(4)}(s)\|_2}{\sqrt n}\ge s\sqrt\mu,
 \quad \frac{\|h^{(3)}(s)\|_2^2}{n}\ge\mu,
 \quad f(s)\ge\mu s,\quad K_n(s)\ge\mu.
 \tag{3.1}
\]

For nonzero readout fix \(0<b\le c\) and \(M_2,M_3\ge0\), and assume
\(\|h^{(3)}(0)\|_2/\sqrt n\ge b\) and
\(\|W^{(j)}(0)\|_{\rm op}\le M_j\) for \(j=2,3\). Define
\[
 L_3=M_3+c+c^2/2,\qquad L_2=M_2+cL_3(1+c/2),
 \qquad B=c^2+L_3^2(c^2+L_2^2),
\]
\[
 \sigma=\min\{1,\sqrt{b/(8cB)}\},\qquad
 \varepsilon_{\rm GF}=\min\{1,b\sigma/16\}.
 \tag{3.2}
\]
If \(\varepsilon=\|W^{(4)}(0)\|_2/\sqrt n\le\varepsilon_{\rm GF}\), then
\[
 \frac{\|h^{(3)}(s)\|_2^2}{n}\ge\mu:=b^2/4,
 \qquad K_n(s)\ge\mu\qquad(s\ge0).
 \tag{3.3}
\]
No coordinatewise initial readout bound is required.

In either case put \(f_0=f(0)\), \(e_0=1-f_0>0\). There is a unique
feature time \(s_*\in(0,e_0/\mu]\) with \(f(s_*)=1\). Physical gradient
flow exists for every \(t\ge0\), has \(s(t)\uparrow s_*\), and satisfies
\[
 0<e(t):=1-f(s(t))\le e_0e^{-2\mu t},\qquad
 \mathcal L_n(t)\le e_0^2e^{-4\mu t},
\]
\[
 s(t)\le\frac{e_0}{\mu}(1-e^{-2\mu t}),\qquad
 s_*-s(t)\le\frac{e(t)}\mu.
 \tag{3.4}
\]
There is a finite endpoint \(\theta_\infty=\theta(s_*)\) with prediction one,
and the following estimates display all four parameter blocks:
\[
 \begin{aligned}
 &\frac{\|z^{(1)}(s(t))-z^{(1)}(0)\|_2^2}{n}
  +\sum_{\ell=2}^3\|W^{(\ell)}(s(t))-W^{(\ell)}(0)\|_{\rm F}^2
  +\frac{\|W^{(4)}(s(t))-W^{(4)}(0)\|_2^2}{n}
  \le\frac{e_0^2}{\mu},\\
 &\left[\frac{\|z^{(1)}(s(t))-z^{(1)}_\infty\|_2^2}{n}
  +\sum_{\ell=2}^3\|W^{(\ell)}(s(t))-W^{(\ell)}_\infty\|_{\rm F}^2
  +\frac{\|W^{(4)}(s(t))-W^{(4)}_\infty\|_2^2}{n}\right]^{1/2}
  \le\frac{e(t)}{\sqrt\mu}.
 \end{aligned}
 \tag{3.5}
\]

**Proof.** In the zero-readout case, smoothness gives
\(W^{(4)}(s)=s h^{(3)}(0)+o(s)\) and \(g'(0+)=\sqrt\mu\).
Convexity (2.5) implies \(g'\ge\sqrt\mu\), \(g\ge s\sqrt\mu\) up to
any first later zero of \(g\); the latter bound excludes such a zero.
Now \(\|h^{(3)}\|_2/\sqrt n\ge g'\), \(f=gg'\), and (2.3) give (3.1).
If the excluded initial \(\mu\) is zero, all four velocities vanish and
the unique solution is stationary.

For small readout, (2.4) bounds the two matrix norms on \([0,1]\) by
\(L_2,L_3\), and (2.1) gives \(\|P\|_{\rm op}\le B\). Integrating
\((h^{(3)})'=PW^{(4)}\) once and twice yields
\[
 \frac{\|h^{(3)}(s)-h^{(3)}(0)\|_2}{\sqrt n}
 \le B(\varepsilon s+cs^2/2),
\]
\[
 \frac{\|W^{(4)}(s)-W^{(4)}(0)-s h^{(3)}(0)\|_2}{\sqrt n}
 \le B(\varepsilon s^2/2+cs^3/6).
 \tag{3.6}
\]
Since \(\varepsilon\le b\sigma/16\le c\sigma\) and
\(Bc\sigma^2\le b/8\), the first bound is at most \(3b/16\) for
\(s\le\sigma\). The second, including the initial readout, gives
\[
 \frac{\|W^{(4)}(\sigma)-\sigma h^{(3)}(0)\|_2}{\sigma\sqrt n}
 \le b/16+b/12=7b/48.
 \tag{3.7}
\]
In particular \(W^{(4)}(\sigma)\ne0\). For any nonzero Euclidean vector
\(x\), Cauchy–Schwarz and the triangle inequality give
\(x^Ty/\|x\|_2\ge\|y\|_2-2\|x-y\|_2\). Apply this with
\(x=W^{(4)}(\sigma)/(\sigma\sqrt n)\),
\(y=h^{(3)}(0)/\sqrt n\), and then use (3.6) for the feature change:
\[
 g'(\sigma)\ge b-2(7b/48)-3b/16=25b/48>b/2.
 \tag{3.8}
\]
Convexity (2.5) preserves this lower bound for later times and prevents a
later zero of \(g\). The initial feature estimate and
\(\|h^{(3)}\|_2/\sqrt n\ge g'\) prove (3.3).

In the small-readout case \(|f_0|\le c\varepsilon\le c^2/16<1\);
in the zero-readout case \(f_0=0\). The bound \(f'\ge\mu\) and continuity
give the unique \(s_*\), with \(s_*\le e_0/\mu\). The scalar equation
\(\dot s=2(1-f(s))\), \(s(0)=0\), has a locally Lipschitz right-hand
side. It is positive before \(s_*\). Uniqueness prevents reaching the
constant solution \(s=s_*\) in finite time. Its bounded state gives global
continuation; a limit below \(s_*\) would have positive clock speed and is
impossible. Differentiation gives \(\dot e=-2K_n(s(t))e\), hence (3.4)
by integration. The last bound in (3.4) also follows directly from
\(e(t)=\int_{s(t)}^{s_*}K_n(u)\,du\).

Integrating (2.3) shows that feature action between any \(s_1<s_2\) equals
\(f(s_2)-f(s_1)\). Cauchy–Schwarz applied jointly to the four weighted
parameter derivatives bounds the corresponding squared displacement by
\((s_2-s_1)[f(s_2)-f(s_1)]\). Take first \(s_1=0,s_2=s(t)\), and then
\(s_1=s(t),s_2=s_*\), to get (3.5). In fact the remaining path length,
computed by integrating the square root of the last line of (2.3), is at most
\(\sqrt{(s_*-s(t))e(t)}\le e(t)/\sqrt\mu\). The initial state determines
this endpoint; uniqueness among all interpolating network states is not
asserted. Finally \(|W_i^{(4)}(s(t))-W_i^{(4)}(0)|\le cs(t)\le ce_0/\mu\).
∎

**Corollary 3.2 (lower-layer moments and backward energy).** Let positive
\(\widehat M_2,\widehat M_3\) bound the matrix operator norms on this
physical trajectory, for instance
\(\widehat M_j=1+M_j+e_0/\sqrt\mu\). Then
\[
 \frac{\|h^{(2)}\|_2^2}{n}\ge\frac\mu{\widehat M_3^2},\qquad
 \frac{\|h^{(1)}\|_2^2}{n}
 \ge\frac\mu{\widehat M_2^2\widehat M_3^2},\qquad
 \int_0^{s_*}\frac{\|q^{(2)}(s)\|_2^2}{n}\,ds
 \le\frac{\widehat M_3^4e_0}{\mu}.
 \tag{3.9}
\]
Indeed \(|\phi(z)|\le|z|\) propagates the top feature lower bound through
the two forward matrices. The third-layer matrix kernel block in (2.3)
is at least \(\mu\|\delta^{(3)}\|_2^2/(n\widehat M_3^2)\); its integral
is at most the total action \(e_0\). Use
\(\|q^{(2)}\|_2\le\widehat M_3\|\delta^{(3)}\|_2\) to obtain (3.9).
These are second moments, not empirical variances or coordinate tail bounds.

## 4. Exact raw GD: coercivity and a finite endpoint

**Theorem 4.1 (exact GD at \(\eta_n=n^{-2}\)).** Fix \(M\ge0\) and
\(0<b\le c\). The explicit constants \(\varepsilon_{\rm GD}>0\),
\(N<\infty\), and \(V<\infty\) in (4.4)–(4.7) depend only on \(M,b\).
Suppose \(n\ge N\) and
\[
 \|W_0^{(2)}\|_{\rm op},\ \|W_0^{(3)}\|_{\rm op},\
 \frac{\|z_0^{(1)}\|_2}{\sqrt n}\le M,\qquad
 \frac{\|W_0^{(4)}\|_2}{\sqrt n}\le\varepsilon_{\rm GD},\qquad
 \frac{\|h_0^{(3)}\|_2}{\sqrt n}\ge b.
 \tag{4.1}
\]
Then every iteration of the simultaneous raw update (1.6) satisfies
\[
 f_k<f_{k+1}<1,\qquad
 \frac{\|h_k^{(3)}\|_2^2}{n}\ge b^2/4,\qquad K_{n,k}\ge b^2/4,
\]
\[
 0<1-f_k\le(1-f_0)(1-\eta_n b^2/4)^k
 \le(1-f_0)e^{-b^2t_k/4}.
 \tag{4.2}
\]
In particular the loss at node \(k\) is bounded by
\((1-f_0)^2e^{-b^2t_k/2}\). With the computational clock from §1,
\[
 \sum_{j\ge k}\alpha_j\le\frac{8(1-f_k)}{b^2}.
 \tag{4.3}
\]
The raw parameters converge to a finite \(\theta_\infty\) with prediction
one. Each of
\[
 \frac{\|z_k^{(1)}-z_\infty^{(1)}\|_2}{\sqrt n},\qquad
 \|W_k^{(\ell)}-W_\infty^{(\ell)}\|_{\rm F}\ (\ell=2,3),\qquad
 \frac{\|W_k^{(4)}-W_\infty^{(4)}\|_2}{\sqrt n}
\]
is at most \(8V(1-f_k)/b^2\). The same bound at \(k=0\) controls the
total movement of each block over all iterations. No coordinatewise initial
readout bound is assumed.

The proof bounds arbitrary positive-step paths of bounded computational
length, derives their exact feature increment with its remainder, and
controls the slope of a regularized readout norm. This gives coercivity
before the residual induction proves positivity of every GD step.

### 4.1 Constants and arbitrary positive-step paths

The following proof constants are scalars; \(P\) remains the matrix from (2.1).
Set
\[
 S=32/b^2,\quad Q=1+cS,\quad R_3=M+cQS,\quad R_2=M+cR_3QS,
\]
\[
 C_P=c^2+R_3^2(c^2+R_2^2),\qquad
 V=\max\{c,cQ,cR_3Q,R_2R_3Q\}.
 \tag{4.4}
\]
For derivative estimates set
\[
 v=R_2R_3Q,\quad a_2=cR_3Q,\quad a_3=cQ,\quad
 v_2=ca_2+R_2v,\quad u_2=2v_2^2+2a_2v+2R_2v^2,
\]
\[
 v_3=ca_3+R_3v_2,\quad
 B=v_3^2+a_3v_2+R_3u_2/2,\quad D=2cC_P+B,
\]
\[
 B_f=Q(cC_P+B),\qquad K_*=c^2+C_PQ^2,\qquad
 \tau=\min\{1,S/4,\sqrt{b/(384cC_P)}\},
\]
\[
 \lambda=b\tau/32,\qquad
 \varepsilon_{\rm GD}=\min\{1,(2c)^{-1},b\tau/32\}.
 \tag{4.5}
\]
Choose \(N\) so that, for all \(n\ge N\), \(A=4n^{-2}\) satisfies
\[
 \begin{gathered}
 A\le\min\{\tau,\lambda/c,S/2\},\qquad
 2B\tau A\sqrt n\le b/64,\qquad DSA\sqrt n\le b/4,\\
 B_fA\sqrt n\le\min\{b^2/8,1\},\qquad
 2n^{-2}(K_*+1)\le1/2.
 \end{gathered}
 \tag{4.6}
\]
An explicit choice is
\[
 N=\left\lceil\max\left\{
 1,\sqrt{4/\tau},\sqrt{4c/\lambda},\sqrt{8/S},
 (512B\tau/b)^{2/3},(16DS/b)^{2/3},
 (32B_f/b^2)^{2/3},(4B_f)^{2/3},2\sqrt{K_*+1}
 \right\}\right\rceil.
 \tag{4.7}
\]
These numbers are finite and positive where used in denominators because
\(b>0\), \(c>0\), and \(C_P\ge c^2\). The factors involving
\(A\sqrt n=4n^{-3/2}\) are the accumulated finite-width error controls.

Consider first any finite path
\(\theta_{j+1}=\theta_j+\alpha_j\mathcal G(\theta_j)\) with positive
\(\alpha_j\) and \(\sum_j\alpha_j\le S\); zero steps can simply be omitted.
Suppose its initial matrix bounds are at most \(M\) and its initial readout
RMS is at most one. The readout increment has RMS at most \(c\alpha_j\).
The third- and second-matrix increments have both operator and Frobenius
norm at most, respectively,
\(c\alpha_j\|W_j^{(4)}\|_2/\sqrt n\) and
\(c\alpha_j\|W_j^{(3)}\|_{\rm op}\|W_j^{(4)}\|_2/\sqrt n\).
Summing in that order gives
\[
 \frac{\|W_j^{(4)}\|_2}{\sqrt n}\le Q,\qquad
 \|W_j^{(3)}\|_{\rm op}\le R_3,\qquad
 \|W_j^{(2)}\|_{\rm op}\le R_2.
 \tag{4.8}
\]
The first-vector increment has RMS at most \(R_2R_3Q\alpha_j\).
These estimates hold also at all points on each straight raw segment with
clock at most \(S\). Each block increment in the norms used in the theorem
is at most \(V\alpha_j\), including the Frobenius matrix norms.

### 4.2 Exact directional identity and Taylor remainder

At any state, the chain rule calculation (2.2) is also the directional
identity
\[
 Dh^{(3)}(\theta)\mathcal G(\theta)=P(\theta)W^{(4)},\qquad
 P\succeq0,\qquad \|P\|_{\rm op}\le C_P
 \tag{4.9}
\]
on the region (4.8). This identity concerns the derivative at the start of a
raw segment, not an equality for its finite increment.

On a frozen segment \(\theta(u)=\theta_j+u\mathcal G(\theta_j)\), a prime
in this paragraph denotes \(d/du\). The raw matrix velocities have operator
norms at most \(a_2,a_3\), and \(\|(z^{(1)})'\|_2/\sqrt n\le v\).
For any Euclidean vector \(w\),
\[
 \frac{\|w\odot w\|_2}{\sqrt n}
 \le\frac{\|w\|_2^2}{\sqrt n}
 =\sqrt n\left(\frac{\|w\|_2}{\sqrt n}\right)^2.
 \tag{4.10}
\]
Using (1.1), the product rule, and (4.8), successively gives
\[
 \frac{\|(h^{(1)})'\|_2}{\sqrt n}\le v,\qquad
 \frac{\|(h^{(1)})''\|_2}{\sqrt n}\le2\sqrt n\,v^2,\qquad
 \frac{\|(z^{(2)})'\|_2}{\sqrt n}\le v_2,
\]
\[
 \frac{\|(h^{(2)})''\|_2}{\sqrt n}\le\sqrt n\,u_2,\qquad
 \frac{\|(z^{(3)})'\|_2}{\sqrt n}\le v_3,\qquad
 \frac{\|(h^{(3)})''\|_2}{\sqrt n}\le2B\sqrt n.
 \tag{4.11}
\]
For the middle second derivative, explicitly,
\((z^{(2)})''=2(W^{(2)})'(h^{(1)})'+W^{(2)}(u)(h^{(1)})''\).
The activation second derivative adds \(2\sqrt n v_2^2\), while these
two product terms contribute at most \(2a_2v+2\sqrt nR_2v^2\).
Since \(n\ge1\), their sum is bounded by \(\sqrt n u_2\).
At the next layer the same rule gives
\(2\sqrt n v_3^2+2a_3v_2+\sqrt n R_3u_2\le2B\sqrt n\), proving the
last estimate without an assumption on coordinate maxima.

Taylor's formula with integral remainder therefore gives an exact equality
\[
 h_{j+1}^{(3)}=h_j^{(3)}+\alpha_jP_jW_j^{(4)}+\xi_j,\qquad
 \frac{\|\xi_j\|_2}{\sqrt n}\le B\sqrt n\,\alpha_j^2.
 \tag{4.12}
\]
Multiplying this by the exactly updated readout yields
\[
 f_{j+1}-f_j=\alpha_jK_{n,j}+\rho_j,\qquad
 K_{n,j}=\frac{\|h_j^{(3)}\|_2^2}{n}
       +\frac{(W_j^{(4)})^TP_jW_j^{(4)}}n,
\]
\[
 \frac{\|h_j^{(3)}\|_2^2}{n}\le K_{n,j}\le K_*,
 \qquad |\rho_j|\le B_f\sqrt n\,\alpha_j^2.
 \tag{4.13}
\]
Indeed the scalar remainder is exactly
\[
 \rho_j=\frac{\alpha_j^2}{n}(h_j^{(3)})^TP_jW_j^{(4)}
          +\frac{(W_{j+1}^{(4)})^T\xi_j}{n}.
\]
Its first term has size at most \(\alpha_j^2cC_PQ\) and its second at most
\(QB\sqrt n\alpha_j^2\), which gives (4.13).

### 4.3 Coercivity on bounded positive-step paths

Assume now the initialization (4.1), \(n\ge N\), and \(\alpha_j\le A\)
on a positive-step path of total length at most \(S\). Interpolate its
readout by
\(W^{(4)}(s)=W_j^{(4)}+(s-s_j)h_j^{(3)}\) and set
\[
 g(s)=\sqrt{\|W^{(4)}(s)\|_2^2/n+\lambda^2}.
\]
On each open segment, Cauchy–Schwarz gives
\[
 g''(s)=
 \frac{(\|h_j^{(3)}\|_2^2/n)g(s)^2
       -((W^{(4)}(s))^Th_j^{(3)}/n)^2}{g(s)^3}\ge0.
 \tag{4.14}
\]
At a knot the jump in slope is, by (4.12),
\[
 g'(s_{j+1}+)-g'(s_{j+1}-)
 =\frac{(W_{j+1}^{(4)})^T(\alpha_jP_jW_j^{(4)}+\xi_j)}{n g(s_{j+1})}
 \ge-D\sqrt n\,\alpha_j^2.
 \tag{4.15}
\]
To see the inequality, expand \(W_{j+1}^{(4)}=W_j^{(4)}+\alpha_jh_j^{(3)}\).
The \(\alpha_j(W_j^{(4)})^TP_jW_j^{(4)}\) term is nonnegative.
The remainder term divided by \(ng\) is bounded in magnitude by
\(\|\xi_j\|_2/\sqrt n\). For the cross term use
\[
 \frac{\|W_j^{(4)}\|_2}{\sqrt n\,g(s_{j+1})}
 \le1+\frac{\alpha_jc}{\lambda}\le2
\]
from (4.6). Its size is at most \(2cC_P\alpha_j^2\), yielding (4.15).

For nodes with \(s_j\le2\tau\), telescoping (4.12) gives
\[
 \frac{\|h_j^{(3)}-h_0^{(3)}\|_2}{\sqrt n}
 \le C_Ps_j(\varepsilon_{\rm GD}+cs_j)+B\sqrt n A s_j
 \le6cC_P\tau^2+2B\tau A\sqrt n\le b/32.
 \tag{4.16}
\]
Here \(\varepsilon_{\rm GD}\le c\tau\), the definition of \(\tau\)
bounds the first term by \(b/64\), and (4.6) bounds the second by \(b/64\).
This proves the required feature lower bound at all these nodes.

If the path extends beyond \(2\tau\), let \(j_0\) be its first node with
\(s_{j_0}\ge\tau\). Because \(A\le\tau\),
\(\tau\le s_{j_0}\le2\tau\). The exact readout sum and (4.16) give
\[
 \frac{W_{j_0}^{(4)}}{s_{j_0}}=h_0^{(3)}+u,\quad
 \frac{\|u\|_2}{\sqrt n}\le b/16,\qquad
 h_{j_0}^{(3)}=h_0^{(3)}+w,\quad
 \frac{\|w\|_2}{\sqrt n}\le b/32,
 \qquad \frac\lambda{s_{j_0}}\le b/32.
 \tag{4.17}
\]
For \(u\), the initial readout contributes at most \(b/32\) after division
by \(s_{j_0}\), and the weighted average of the feature errors contributes
another \(b/32\). Set \(h_*=\|h_0^{(3)}\|_2/\sqrt n\). Expanding
the numerator using (4.17), and bounding the denominator by
\(g(s_{j_0})/s_{j_0}\le h_*+3b/32\), gives
\[
 g'(s_{j_0}+)
 \ge\frac{h_*^2-3h_*b/32-b^2/512}{h_*+3b/32}
 \ge\frac{463}{560}h_*\ge3b/4.
 \tag{4.18}
\]
Here \(h_*\ge b\), so the numerator is at least \((463/512)h_*^2>0\) and
the denominator at most \((35/32)h_*\).
Convexity on segments and (4.15) now imply at every later node
\[
 g'(s_j+)\ge3b/4-D\sqrt n\sum_i\alpha_i^2
 \ge3b/4-DSA\sqrt n\ge b/2.
\]
On the other hand,
\(g'(s_j+)=(W_j^{(4)})^Th_j^{(3)}/(ng(s_j))
\le\|h_j^{(3)}\|_2/\sqrt n\).
Together with (4.16), this proves \(\|h_j^{(3)}\|_2/\sqrt n\ge b/2\)
at every node of the path. At its final node the right slope means this
algebraic expression, so no additional update is assumed.

### 4.4 Closing the GD induction and taking the endpoint

Initially \(|f_0|\le c\varepsilon_{\rm GD}\le1/2\). Suppose a finite GD
prefix satisfies
\[
 f_0\le f_k<1,\qquad
 s_k\le\frac8{b^2}(f_k-f_0)
 \le\frac{8(1-f_0)}{b^2}\le S/2.
 \tag{4.19}
\]
This holds at \(k=0\). The next raw step has
\(0<\alpha_k=2n^{-2}(1-f_k)\le A\), and \(s_{k+1}\le S\).
The positive-step lemma thus applies to this extended prefix. Equations
(4.6) and (4.13) imply
\[
 \frac{b^2}{8}\alpha_k\le f_{k+1}-f_k
 \le\alpha_k(K_*+1)\le\frac{1-f_k}{2}.
 \tag{4.20}
\]
For the lower bound, subtract
\(|\rho_k|/\alpha_k\le B_fA\sqrt n\le b^2/8\) from
\(K_{n,k}\ge b^2/4\). For the upper bound the same error is at most one
and \(2n^{-2}(K_*+1)\le1/2\). Consequently \(f_k<f_{k+1}<1\).
Summing the lower bound proves (4.19) for \(k+1\), closing the induction.

Substituting \(\alpha_k=2\eta_n(1-f_k)\) in (4.20) gives the geometric
bound (4.2); its factor lies strictly between zero and one by (4.6).
Thus \(f_k\to1\). Sum the lower bound in (4.20) from \(k\) to infinity
to obtain (4.3). Each block increment is bounded by \(V\alpha_j\) in
its displayed norm, so the parameters are Cauchy in finite-dimensional
space and their tails obey the theorem's bound. Continuity of (1.2) gives
prediction one at the endpoint. The linear raw interpolant has the same
endpoint, since each interpolated state is a convex combination of its
two raw parameter endpoints.

Only \(\sum_k\eta_n(1-f_k)=\tfrac12\sum_k\alpha_k\) is summable;
\(\sum_k\eta_n=\infty\). The width threshold is part of the theorem:
the prescription \(\eta_n=n^{-2}\) alone does not rule out overshoot at
arbitrary small widths and arbitrary initial operator bounds. This proof
does not compare a GD endpoint to a gradient-flow endpoint. ∎

## 5. Energy-compatible metric projection

The remaining deterministic results concern an auxiliary continuous flow.
It retains all exact forward equations (1.2), both evolving matrices, and
the full derivatives (1.3). Only the two lower parameter velocities change.
Define
\[
 c_1=\|h^{(1)}\|_2^2/n,\qquad
 \mathsf M=c_1I+W^{(2)}D_1^2(W^{(2)})^T.
 \tag{5.1}
\]
For \(R>0\) and \(c_1>0\), let
\[
 u_R=\underset{u\in[-R,R]^n}{\operatorname{argmin}}\,
       \frac12(u-\delta^{(2)})^T\mathsf M(u-\delta^{(2)}).
 \tag{5.2}
\]
Thus the vector being projected is the full \(\delta^{(2)}\), not
\(q^{(2)}\). The feature-time equations are
\[
 \begin{aligned}
 (z^{(1)})'&=D_1(W^{(2)})^Tu_R,&
 (W^{(2)})'&=u_R(h^{(1)})^T/n,\\
 (W^{(3)})'&=\delta^{(3)}(h^{(2)})^T/n,&
 (W^{(4)})'&=h^{(3)}.
 \end{aligned}
 \tag{5.3}
\]
Since \(\mathsf M\succeq c_1I\), it is positive definite on the stated
domain. Compactness of the box and strict convexity prove existence and
uniqueness of (5.2). The metric is induced by the joint squared speeds of
the first vector and second matrix, as the next calculation verifies.

**Lemma 5.1 (projection inequality, local flow, and energy).** The projection
satisfies
\[
 (v-u_R)^T\mathsf M(u_R-\delta^{(2)})\ge0
 \quad(v\in[-R,R]^n),
 \tag{5.4}
\]
\[
 (\delta^{(2)})^T\mathsf M u_R
 \ge u_R^T\mathsf M u_R\ge c_1\|u_R\|_2^2,\qquad
 u_R^T\mathsf M u_R\le(\delta^{(2)})^T\mathsf M\delta^{(2)}.
 \tag{5.5}
\]
For each fixed \(n,R\), (5.3) has a unique local solution on \(c_1>0\).
Along it,
\[
 \begin{aligned}
 f'&=\frac{(\delta^{(2)})^T\mathsf M u_R}{n}
       +\frac{\|\delta^{(3)}\|_2^2\|h^{(2)}\|_2^2}{n^2}
       +\frac{\|h^{(3)}\|_2^2}{n}\\
 &=\frac{\|(z^{(1)})'\|_2^2}{n}
       +\|(W^{(2)})'\|_{\rm F}^2+\|(W^{(3)})'\|_{\rm F}^2
       +\frac{\|(W^{(4)})'\|_2^2}{n}
       +\frac{(\delta^{(2)}-u_R)^T\mathsf M u_R}{n}.
 \end{aligned}
 \tag{5.6}
\]
The last term is nonnegative, so \(f'\ge0\).

**Proof.** The one-sided derivative of the objective from its minimizer
toward \(v\) gives (5.4). Conversely, expansion of the quadratic objective
shows that (5.4) implies optimality. Taking \(v=0\) proves the first part
of (5.5). Cauchy–Schwarz in the positive definite form \(\mathsf M\) then
gives its last inequality, dividing by
\((u_R^T\mathsf M u_R)^{1/2}\) only if this is positive. If it is zero,
that inequality already holds.

For local dependence of the projection, let \(u\) and \(v\) project vectors
\(\zeta,\widetilde\zeta\in\mathbb R^n\) in positive definite matrices
\(\mathsf M,\mathsf N\succeq aI\)
onto the same fixed box, where \(a>0\). Use \(v\) as competitor for \(u\)
and \(u\) as competitor for \(v\). Adding gives
\((u-v)^T[\mathsf M(u-\zeta)-\mathsf N(v-\widetilde\zeta)]\le0\).
Expansion yields
\[
 a\|u-v\|_2\le\|\mathsf M\|_{\rm op}\|\zeta-\widetilde\zeta\|_2
       +\|\mathsf M-\mathsf N\|_{\rm op}\|v-\widetilde\zeta\|_2.
 \tag{5.7}
\]
For \(u=v\) no division is needed; otherwise divide the corresponding
quadratic inequality by \(\|u-v\|_2\). On a bounded set of vector and matrix
arguments the last factor is bounded, since \(\|v\|_2\le R\sqrt n\).
The remaining maps in (5.1)–(5.3) are smooth. Therefore the finite vector
field is locally Lipschitz on the open set \(c_1>0\). The integral-map
contraction construction in Lemma 2.1 applies there.

For the energy identity, differentiate the exact forward network. The
lower contributions to \(f'\) are
\[
 \frac{(\delta^{(1)})^TD_1(W^{(2)})^Tu_R}{n}
 +\frac{\|h^{(1)}\|_2^2}{n}\frac{(\delta^{(2)})^Tu_R}{n}
 =\frac{(\delta^{(2)})^T\mathsf M u_R}{n}.
\]
The upper blocks are unchanged and give the last two terms on the first
line of (5.6). The two lower squared speeds sum to
\(u_R^T\mathsf M u_R/n\); the upper squared speeds equal their kernel
contributions. This proves (5.6), including its work excess and every
normalization. ∎

The estimate (5.7) is local at fixed dimension. It supplies no
dimension-independent stability estimate for composition with the nonlinear
map \(\theta\mapsto\delta^{(2)}\).

## 6. Global finite projection theorem and its physical clock

**Theorem 6.1 (global auxiliary family).** Fix \(M_0\ge0\) and
\(\beta_1,\beta_3>0\). Suppose the same finite initial state, for every cap,
satisfies
\[
 \|W_0^{(2)}\|_{\rm op},\|W_0^{(3)}\|_{\rm op}\le M_0,\qquad
 \frac{\|z_0^{(1)}\|_2}{\sqrt n}\le2,\qquad \|W_0^{(4)}\|_\infty\le1,
\]
\[
 \frac{\|h_0^{(1)}\|_2^2}{n}\ge\beta_1,\qquad
 \frac{\|h_0^{(3)}\|_2^2}{n}\ge\beta_3,\qquad
 \frac{\|W_0^{(4)}\|_2}{\sqrt n}\le2/n.
 \tag{6.1}
\]
Define the positive constants \(a,f_*,k,S_\dagger\) below and suppose
\[
 n\ge\frac{16c}{\beta_3a},\qquad n>2c.
 \tag{6.2}
\]
For every \(R>0\), (5.3) then has a unique solution for all feature times.
On every finite feature interval \([0,S]\), all parameter RMS or matrix
operator bounds, matrix-increment Frobenius bounds, the positive lower bound
for \(c_1\), and all speed bounds (6.3)–(6.9) are independent of \(R,n\).
The prediction is strictly increasing and reaches one at a unique
\(s_\dagger\le S_\dagger\).

Its canonical scalar clock \(\dot s=2(1-f(s))\), \(s(0)=0\), exists for all
physical times, stays below \(s_\dagger\), and increases to it. The auxiliary
physical trajectory fits the target and converges to its finite endpoint.
In particular, with the uniform constant
\(\mu_{\rm aux}=\min\{\beta_3/4,k\}>0\),
\[
 0<1-f(s(t))\le(1-f_0)e^{-2\mu_{\rm aux}t},\qquad
 \mathcal L_n(t)\le(1-f_0)^2e^{-4\mu_{\rm aux}t}.
\]
This is a physical reparametrization of (5.3). Its lower updates differ from
canonical gradient flow when the projection is active.

**Proof.** We first obtain energy bounds before assuming that \(c_1\) stays
positive, then prove noncollapse and continuation, and finally control the
clock. For \(S>0\) define
\[
 B(S)=1+cS,\quad D(S)=cB(S)+c,\quad
 A_2(S)=M_0+\sqrt{SD(S)},\quad A_3(S)=M_0+cB(S)S.
 \tag{6.3}
\]
On the existing part of a solution with \(s\le S\), bounded activation and
the two upper equations imply
\[
 \|W^{(4)}(s)\|_\infty\le B(S),\quad
 \frac{\|\delta^{(3)}(s)\|_2}{\sqrt n}\le B(S),\quad
 \|W^{(3)}(s)\|_{\rm op}\le A_3(S),\quad |f(s)|\le cB(S).
\]
Since \(f_0\ge-c\), (5.6) bounds the integral of the sum of all four squared
speeds by \(D(S)\). Consequently, for \(s\le S\),
\[
 \|W^{(2)}(s)-W_0^{(2)}\|_{\rm F}\le\sqrt{sD(S)},\qquad
 \frac{\|z^{(1)}(s)-z_0^{(1)}\|_2}{\sqrt n}\le\sqrt{sD(S)},\qquad
 \|W^{(2)}(s)\|_{\rm op}\le A_2(S).
 \tag{6.4}
\]
These estimates hold before any possible exit from \(c_1>0\). They do not
use a prior bound for \(u_R\).

On this existing interval with \(s\le1\), the Lipschitz property of \(\phi\)
and the two exact forward products give
\[
 \begin{aligned}
 \frac{\|h^{(1)}(s)-h_0^{(1)}\|_2}{\sqrt n}
   &\le\sqrt{sD(1)},\\
 \frac{\|h^{(2)}(s)-h_0^{(2)}\|_2}{\sqrt n}
   &\le[A_2(1)+c]\sqrt{sD(1)},\\
 \frac{\|h^{(3)}(s)-h_0^{(3)}\|_2}{\sqrt n}
   &\le A_3(1)[A_2(1)+c]\sqrt{sD(1)}+c^2B(1)s
    \le C_h\sqrt s,
 \end{aligned}
 \tag{6.5}
\]
where \(C_h=A_3(1)[A_2(1)+c]\sqrt{D(1)}+c^2B(1)\).
For example, split
\(z^{(2)}(s)-z_0^{(2)}
=W^{(2)}(s)(h^{(1)}(s)-h_0^{(1)})
 +(W^{(2)}(s)-W_0^{(2)})h_0^{(1)}\).
The third-layer split is the same, using
\(\|W^{(3)}(s)-W_0^{(3)}\|_{\rm op}\le cB(1)s\).
This proves every bound in (6.5).

Set
\[
 a=\min\{1,\beta_1/[16D(1)],\beta_3/(16C_h^2)\},\qquad
 f_*=\beta_3a/8.
 \tag{6.6}
\]
For \(s\le a\), the first and third feature RMS changes are at most
\(\sqrt{\beta_1}/4\) and \(\sqrt{\beta_3}/4\), respectively. In particular,
\(c_1\ge\beta_1/4\) and \(\|h^{(3)}\|_2^2/n\ge\beta_3/4\) there.
The parameter bounds and this strict lower bound keep the finite state
in a compact subset of \(c_1>0\), so local continuation rules out an
endpoint at or before \(a\). Also \(|f_0|\le2c/n\), so (5.6) and (6.2) give
\[
 f(a)\ge-2c/n+\beta_3a/4\ge f_*>0.
\]
Monotonicity gives \(f(s)\ge f_*\) for every existing \(s\ge a\).
For \(a\le s\le S\), use \(|\phi(z)|\le|z|\) to get
\[
 f_*\le f(s)
 \le B(S)\frac{\|h^{(3)}(s)\|_2}{\sqrt n}
 \le B(S)A_3(S)A_2(S)\frac{\|h^{(1)}(s)\|_2}{\sqrt n}.
\]
Thus on \([0,S]\) the strictly positive lower bound for \(c_1\) is
\[
 \underline c_1(S)=
 \begin{cases}
 \beta_1/4,&0<S<a,\\
 \min\{\beta_1/4,[f_*/(B(S)A_3(S)A_2(S))]^2\},&S\ge a.
 \end{cases}
 \tag{6.7}
\]
Here \(A_2(S),A_3(S)>0\) for \(S>0\), even if \(M_0=0\).
At any proposed finite maximal endpoint choose \(S\ge a\) larger than
that endpoint. The bounds (6.3)–(6.4), including Frobenius bounds for
increments, and (6.7) keep all parameters in a finite-dimensional compact
subset of the open domain. The locally Lipschitz vector field is bounded
on this compact set, so the path has a limit there and extends. This
contradicts maximality and proves global feature existence.

For explicit speed bounds, (5.5), (6.7), and
\(\|\mathsf M\|_{\rm op}\le c^2+A_2(S)^2\) give
\[
 \frac{\|u_R(s)\|_2}{\sqrt n}\le
 U(S):=\sqrt{\frac{c^2+A_2(S)^2}{\underline c_1(S)}}\,A_3(S)B(S).
 \tag{6.8}
\]
We used \(\|\delta^{(2)}\|_2/\sqrt n\le A_3(S)B(S)\).
The four parameter speeds in their normalized-vector and Frobenius norms
are bounded, in order, by \(A_2(S)U(S),cU(S),cB(S),c\).
The forward definitions also bound the hidden preactivation RMS norms:
\[
 \frac{\|z^{(1)}(s)\|_2}{\sqrt n}\le2+\sqrt{SD(S)},\qquad
 \frac{\|z^{(2)}(s)\|_2}{\sqrt n}\le cA_2(S),\qquad
 \frac{\|z^{(3)}(s)\|_2}{\sqrt n}\le cA_3(S).
\]
Writing the constants in the next display at \(S\), differentiation gives
\[
 \begin{aligned}
 \frac{\|(z^{(2)})'\|_2}{\sqrt n}&\le(c^2+A_2^2)U,\\
 \frac{\|(z^{(3)})'\|_2}{\sqrt n}&\le c^2B+A_3(c^2+A_2^2)U,\\
 \frac{\|(q^{(2)})'\|_2}{\sqrt n}
 &\le cB^2+A_3\{c+2B[c^2B+A_3(c^2+A_2^2)U]\}.
 \end{aligned}
 \tag{6.9}
\]
The first bound follows from \((z^{(2)})'=\mathsf M u_R\); the second
from differentiating the third-layer product. For the last, differentiate
\(q^{(2)}=(W^{(3)})^T\delta^{(3)}\) and use
\[
 (\delta^{(3)})'=h^{(3)}\odot\phi'(z^{(3)})
  +W^{(4)}\odot\phi''(z^{(3)})\odot(z^{(3)})'.
\]
The term \(((W^{(3)})')^T\delta^{(3)}\) has RMS at most \(cB^2\);
the other term gives the bracket in (6.9). No derivative of the projection
is needed. Integration of these bounds gives time-Lipschitz estimates
for the hidden fields and for the full query in RMS, uniformly in the cap.

It remains to bound the clock. Put \(v=\|W^{(4)}\|_2^2/n\). Exactly
\(v'=2f\), and (5.6) and Cauchy–Schwarz give
\(f'\ge\|h^{(3)}\|_2^2/n\ge f^2/v\) wherever \(v>0\).
For \(s\ge a\), \(f\ge f_*>0\), so \(v>0\), and
\[
 (f^2/v)'=\frac{2f}{v}(f'-f^2/v)\ge0.
\]
Since \(v(a)\le B(1)^2\), define
\[
 k=f_*^2/B(1)^2>0,\qquad S_\dagger=a+1/k.
 \tag{6.10}
\]
Then \(f'(s)\ge k\) for all \(s\ge a\). Combined with the initial interval
bound, this proves \(f'\ge\mu_{\rm aux}>0\) on the entire feature half-line.
We have \(f_0<1\) by (6.2), and \(f\) eventually grows at least linearly.
Thus it crosses one exactly once. If the crossing is after \(a\), its
time is at most \(a+(1-f(a))/k\le S_\dagger\); a crossing before \(a\)
also meets this bound.

The scalar clock is locally Lipschitz since \(f\) is continuously
differentiable. It cannot hit its equilibrium \(s_\dagger\) at finite
physical time by uniqueness. Boundedness of its state gives continuation,
and a limit below \(s_\dagger\) would have positive speed. This proves the
claimed global clock and its limit. Along it,
\[
 \frac{d}{dt}(f-1)^2=-4(f-1)^2f'(s(t)),
 \tag{6.11}
\]
and integration gives the stated fitting rate. The feature solution is
defined at \(s_\dagger\), so \(\theta_\infty=\theta(s_\dagger)\) is finite.
More quantitatively, putting \(e(t)=1-f(s(t))\), (5.6) gives remaining
action at most \(e(t)\), and \(s_\dagger-s(t)\le e(t)/\mu_{\rm aux}\).
Cauchy–Schwarz proves
\[
 \left[
 \frac{\|z^{(1)}(s(t))-z_\infty^{(1)}\|_2^2}{n}
 +\sum_{\ell=2}^3\|W^{(\ell)}(s(t))-W_\infty^{(\ell)}\|_{\rm F}^2
 +\frac{\|W^{(4)}(s(t))-W_\infty^{(4)}\|_2^2}{n}
 \right]^{1/2}\le\frac{e(t)}{\sqrt{\mu_{\rm aux}}}.
 \tag{6.12}
\]
The same argument bounds total squared displacement from time zero by
\(S_\dagger(1-f_0)\). Every constant is common to all caps satisfying the
same initial conditions. ∎

## 7. Integrated defect and eventual exactness

**Theorem 7.1 (integrated \(L^1\) middle-equation defect).** Under Theorem 6.1
let
\[
 e_R=\mathsf M(\delta^{(2)}-u_R).
 \tag{7.1}
\]
For every \(S>0\),
\[
 (z^{(2)})'=\mathsf M\delta^{(2)}-e_R,\qquad
 \int_0^S\frac1n\sum_{i=1}^n|e_{R,i}(s)|\,ds\le\frac{D(S)}R.
 \tag{7.2}
\]
Thus every measurable vector test \(a(s)\) with \(|a_i(s)|\le1\), including
one chosen from the trajectory, satisfies
\[
 \left|\int_0^S\frac{a(s)^T[(z^{(2)})'-\mathsf M\delta^{(2)}]}n\,ds\right|
 \le D(S)/R.
 \tag{7.3}
\]
The canonical velocity in this formula is evaluated at the current
auxiliary state.

**Proof.** Coordinate variations in (5.4) give
\[
 e_{R,i}=0\text{ if }|u_{R,i}|<R,\qquad
 e_{R,i}\ge0\text{ if }u_{R,i}=R,\qquad
 e_{R,i}\le0\text{ if }u_{R,i}=-R.
 \tag{7.4}
\]
At an upper face the allowed negative variation forces
\([\mathsf M(u_R-\delta^{(2)})]_i\le0\); the lower face is the reverse,
and both signs are allowed in the interior. Therefore the excess work is
exactly
\[
 \frac{(\delta^{(2)}-u_R)^T\mathsf M u_R}{n}
   =\frac{u_R^Te_R}{n}=\frac Rn\sum_i|e_{R,i}|.
 \tag{7.5}
\]
All squared speeds in (5.6) are nonnegative, so integration bounds (7.5)
by \(f(S)-f_0\le D(S)\), proving the integral estimate. Differentiating
the exact second forward product gives
\[
 (z^{(2)})'=c_1u_R+W^{(2)}D_1^2(W^{(2)})^Tu_R
           =\mathsf M u_R=\mathsf M\delta^{(2)}-e_R.
\]
This proves (7.2). The triangle inequality proves (7.3), without any
independence condition on the test. In particular for any \(C^1\) function
\(\chi:\mathbb R\to\mathbb R\) with \(\|\chi'\|_\infty\le1\), the chain rule
gives the concrete consequence
\[
 \left|\frac1n\sum_i[\chi(z_i^{(2)}(S))-\chi(z_i^{(2)}(0))]
 -\int_0^S\frac1n\sum_i
       \chi'(z_i^{(2)}(s))[\mathsf M(s)\delta^{(2)}(s)]_i\,ds\right|
 \le D(S)/R.
 \tag{7.6}
\]
In physical time the subtracted defect is \(2(1-f)e_R\). Since the clock is
positive on every finite physical interval, substitution \(ds=2(1-f)\,dt\) yields
\[
 \int_0^T\frac1n\sum_i
 \left|\frac{dz_i^{(2)}}{dt}
       -2(1-f)[\mathsf M\delta^{(2)}]_i\right|dt
 \le\frac{D(S_\dagger)}R\qquad(T<\infty).
 \tag{7.7}
\]
Monotone convergence of these nonnegative integrals gives the same bound
over \(0\le t<\infty\). ∎

This is an integrated \(L^1\) estimate with normalized counting measure on
coordinates. It does not give a vanishing RMS defect. Indeed, (6.8) and
(7.4) bound its support at a fixed time by \(nU(S)^2/R^2\) coordinates,
but squared norm may concentrate on a small set. Nor does the operator
bound for \(\mathsf M^{-1}\) turn this \(L^1\) bound into a vanishing RMS
bound for \(\delta^{(2)}-u_R\). These estimates alone do not force the
excess work in (7.5) to vanish uniformly in width as \(R\) increases;
fixed-width exactness is addressed next. Unbounded tests, hidden-velocity
RMS comparison, raw kernel comparison, and a population passage do not
follow from (7.2).

**Theorem 7.2 (eventual exactness at fixed width).** Under Theorem 6.1, fix
\(S>0\). If
\[
 R\ge C(S)\sqrt n,\qquad C(S)=A_3(S)B(S),
 \tag{7.8}
\]
the entire auxiliary feature trajectory on \([0,S]\) equals the canonical
finite feature flow with the same initialization. In particular, if
\(R\ge C(S_\dagger)\sqrt n\), its physical trajectory equals the canonical
finite gradient flow for every \(t\ge0\), with the same endpoint.

**Proof.** The cap-independent bounds of Theorem 6.1 give, at every state
of every auxiliary trajectory in this interval,
\[
 \|\delta^{(2)}(s)\|_\infty
 \le\|\delta^{(2)}(s)\|_2
 \le\sqrt n\,A_3(S)B(S).
\]
Under (7.8), \(\delta^{(2)}\) is feasible in (5.2), where it gives the
minimum value zero. Positive definiteness makes it the unique minimizer.
Thus \(u_R=\delta^{(2)}\) throughout the interval; all four equations
(5.3) become (1.5). Uniqueness of the smooth canonical feature flow from
Lemma 2.1 identifies the whole paths. Their scalar physical clocks are
then identical by uniqueness. When \(S=S_\dagger\), these clocks remain
below their common first prediction-one time, so equality covers every
finite physical time and the endpoint. ∎

The sufficient cap is \(C(S)\sqrt n\), with its stated constant. It is
not a width-independent cap or a claim with constant one. The result
concerns each fixed finite width and does not justify exchanging the cap
and width limits. It makes no statement about a projected GD algorithm.

## 8. One Gaussian initial event for all finite conclusions

**Theorem 8.1 (canonical Gaussian initialization).** All coordinate entries
in the four initial blocks are independent, with
\[
 z_{0,i}^{(1)}\sim N(0,1),\qquad
 W_{0,ij}^{(2)},W_{0,ij}^{(3)}\sim N(0,1/n),\qquad
 W_{0,i}^{(4)}\sim N(0,n^{-2}).
 \tag{8.1}
\]
In particular the stored readout has standard deviation \(1/n\).
For a standard normal scalar \(G\), define
\[
 \nu_1=\mathbb E[\phi(G)^2],\qquad
 \nu_2=\mathbb E[\phi(\sqrt{\nu_1}G)^2],\qquad
 \nu_3=\mathbb E[\phi(\sqrt{\nu_2}G)^2].
 \tag{8.2}
\]
These constants belong to \((0,c^2]\). Let \(\mathcal E_n\) be the event
\[
 \begin{gathered}
 \|W_0^{(2)}\|_{\rm op},\|W_0^{(3)}\|_{\rm op}\le10,\qquad
 \|z_0^{(1)}\|_2/\sqrt n\le2,\\
 \|W_0^{(4)}\|_2/\sqrt n\le2/n,\qquad
 \|W_0^{(4)}\|_\infty\le1,\\
 \|h_0^{(1)}\|_2^2/n\ge\nu_1/2,\qquad
 \|h_0^{(3)}\|_2^2/n\ge\nu_3/2.
 \end{gathered}
 \tag{8.3}
\]
Then \(\mathbb P(\mathcal E_n)\to1\). On this same event, for every
sufficiently large deterministic width, all of the following hold
simultaneously for the given initial state:

- Theorem 3.1 applies with \(M_2=M_3=10\),
  \(b=\sqrt{\nu_3}/2\), and \(\mu=\nu_3/16\), giving canonical gradient-flow
  coercivity, fitting, and its finite endpoint for all physical time.
- Theorem 4.1 applies with \(M=10\) and the same \(b\). In particular,
  \(K_{n,k}\ge\nu_3/16\),
  \[
   0<1-f_k\le(1-f_0)(1-\eta_n\nu_3/16)^k,\qquad
   \sum_{j\ge k}\alpha_j\le32(1-f_k)/\nu_3,
  \]
  and all raw parameters converge to the finite GD endpoint.
- Theorems 6.1, 7.1, and 7.2 apply simultaneously to every \(R>0\),
  with \(M_0=10\), \(\beta_1=\nu_1/2\), and \(\beta_3=\nu_3/2\).

For precision, one sufficient common width threshold is
\[
 \max\left\{
 N(10,b),\
 \left\lceil2/\varepsilon_{\rm GF}\right\rceil,\
 \left\lceil2/\varepsilon_{\rm GD}\right\rceil,\
 \left\lceil16c/(\beta_3a)\right\rceil,\
 \lfloor2c\rfloor+1
 \right\},
 \tag{8.4}
\]
where all constants are given in (3.2), (4.4)–(4.7), and (6.3)–(6.6)
at these parameter values.

**Proof.** Nondegenerate normal variables are nonzero almost surely and
\(\phi(z)\ne0\) for \(z\ne0\). Boundedness of \(\phi\) and induction prove
positivity and finiteness in (8.2). The independent bounded variables
\(\phi(z_{0,i}^{(1)})^2\) have mean \(\nu_1\) and variance at most \(c^4\).
For a variable \(X\) of finite variance, applying Markov's inequality to
\((X-\mathbb EX)^2\) gives
\(\mathbb P(|X-\mathbb EX|>\epsilon)\le\operatorname{Var}(X)/\epsilon^2\).
The variance of this independent average is at most \(c^4/n\), so that
inequality gives
\(\|h_0^{(1)}\|_2^2/n\to\nu_1\) in probability.

Conditioned on \(h_0^{(1)}\), the rows of \(W_0^{(2)}\) are independent.
Hence the coordinates of \(z_0^{(2)}\) are conditionally independent
centered normals with common variance \(\|h_0^{(1)}\|_2^2/n\).
The conditional variance of their squared-activation average is at most
\(c^4/n\), and its conditional mean is
\[
 \Psi\!\left(\|h_0^{(1)}\|_2^2/n\right),\qquad
 \Psi(x)=\mathbb E[\phi(\sqrt x\,G)^2]\quad(x\ge0).
\]
The function \(\Psi\) is continuous: for \(x_j\to x\), its integrand
converges pointwise and is bounded by the integrable constant \(c^2\),
so bounded convergence applies. Conditional Chebyshev bounds the difference
between the average and this mean in probability; continuity of \(\Psi\)
then gives \(\|h_0^{(2)}\|_2^2/n\to\Psi(\nu_1)=\nu_2\).
The vector \(h_0^{(2)}\) is independent of \(W_0^{(3)}\), so the identical
conditional argument yields
\(\|h_0^{(3)}\|_2^2/n\to\nu_3\). Positivity of the limits proves the
two activation lower bounds in (8.3) with probability tending to one.
The independence used here concerns initialization only.

For an initial middle matrix \(W\), a maximal \(1/4\)-separated subset
of the Euclidean unit sphere is a \(1/4\)-net. Balls of radius \(1/8\)
about its points are disjoint and contained in the radius-\(9/8\) ball,
so volume comparison bounds its size by \(9^n\). Approximating the two
unit vectors in any bilinear form by net points bounds its approximation
error by \(\|W\|_{\rm op}/2\). Consequently
\[
 \|W\|_{\rm op}\le2\max_{u,v\ {\rm in\ the\ net}}|u^TWv|.
\]
Each fixed \(u^TWv\) is \(N(0,1/n)\). For completeness, the identity
\(\mathbb E e^{tG}=e^{t^2/2}\), obtained by completing the square in the
normal density, and Markov's inequality give
\(\mathbb P(|G|>x)\le2e^{-x^2/2}\) for \(x>0\).
A union bound therefore gives
\[
 \mathbb P(\|W\|_{\rm op}>M)
 \le2\,9^{2n}e^{-nM^2/8}.
 \tag{8.5}
\]
This tends to zero at \(M=10\); another union bound covers both matrices.

Integration by parts in the Gaussian density gives
\(\mathbb EG^{2j}=(2j-1)\mathbb EG^{2j-2}\) for \(j=1,2\);
the boundary terms vanish because a polynomial times \(e^{-x^2/2}\)
tends to zero at both ends. Thus \(\mathbb EG^2=1\) and
\(\mathbb EG^4=3\). The average of \(n\) independent standard normal squares
has mean one and variance \(2/n\). Apply Chebyshev's inequality first to
\(z_0^{(1)}\), and then to \(nW_0^{(4)}\), to prove respectively
\(\|z_0^{(1)}\|_2/\sqrt n\le2\) and
\(\|W_0^{(4)}\|_2/\sqrt n\le2/n\) with probability tending to one.
Also, by the same scalar normal tail bound,
\[
 \mathbb P(\|W_0^{(4)}\|_\infty>1)\le2n e^{-n^2/2}.
\]
The union bound now proves \(\mathbb P(\mathcal E_n)\to1\); no independence
among these final events is required.

On \(\mathcal E_n\), the top feature RMS is at least
\(\sqrt{\nu_3/2}\ge b\). The threshold (8.4) makes the readout RMS at most
each of the two required smallness constants and ensures both deterministic
width conditions. The initial first-vector bound two is at most the GD
bound ten. The projection conditions are exactly (6.1), with the parameters
specified above. The deterministic theorems therefore apply as claimed.
Their bounds hold for all indicated times and caps on this one event;
there is no union over time or over an uncountable set of caps. ∎

## 9. Proof dependencies and scope

The optimization statements use only finite differentiation, inequalities,
finite-dimensional ODE continuation, and the initialization calculation in §8.
Their precise dependencies within this chapter are:

1. Lemma 2.1 derives the canonical action and positive readout acceleration
   directly from (1.2)–(1.5). Theorem 3.1 uses this positivity to prove
   coercivity, fitting, and endpoint bounds; Corollary 3.2 uses its action.
2. Theorem 4.1 uses the directional identity (2.2), the positive matrix
   (2.1), and its own raw-segment estimates (4.8)–(4.18). It does not use a
   comparison with gradient flow to obtain discrete coercivity.
3. Lemma 5.1 proves the projection inequality and the auxiliary energy
   formula. Theorem 6.1 uses that formula, bounded activation, noncollapse,
   and the identity \((\|W^{(4)}\|_2^2/n)'=2f\) to obtain its global
   finite flow and physical endpoint.
4. Theorem 7.1 combines the coordinate optimality signs with the exact
   energy formula. Theorem 7.2 combines the cap-independent norm bounds
   with finite canonical uniqueness.
5. Theorem 8.1 verifies every required initial event and width threshold
   for the stored tiny Gaussian readout.

None of these arguments assumes a trained-state population limit. The
canonical finite GD and gradient-flow endpoints are each determined by
their initial state and algorithm; they need not agree. The auxiliary
projection results concern continuous finite dynamics only. In particular,
the \(L^1\) defect estimate and the sufficient cap \(C(S)\sqrt n\) supply
neither dimension-uniform state stability nor a population projection
theorem, global uncut population continuation, or interchange of infinite
width with infinite physical time.
