# Finite optimization and energy-compatible controls

This chapter proves finite-width optimization for the canonical three-hidden-layer
arctangent network: global gradient-flow coercivity and fitting, exact raw-GD
coercivity and fitting at step \(\eta_n=n^{-2}\), and convergence of every
parameter to a finite interpolating endpoint. It also proves a global
finite-dimensional theorem for an auxiliary metric projection, its integrated
\(L^1\) equation defect, and eventual exact agreement with the canonical flow
at each fixed width. All proof ingredients and Gaussian initial conditions are
given below.

Sections 10–11 add a different, two-hidden-layer mixed-activation model at
every fixed interior correlation with opposite labels. They prove actual
finite-GF fitting and finite parameter limits, with explicit initialization
events and width-independent bounds on those events. A separately augmented
event gives permanent positive first-gate mass. These are not population/GD
results, and gate mass is not a certificate of nonzero feature velocity.

The conventions agree with [NOTATION.md](NOTATION.md), the general identities
in [finite_dynamics.md](finite_dynamics.md), and the
[three-hidden-layer arctangent model](arctan_limits.md#l3-local).
Sections 1–11 concern finite widths. Section 12 separately proves global
dissipative capped flows on prescribed Hilbert spaces and continuation under
an explicit exponential-tail premise. It assumes a bounded initial middle
operator on those spaces; it does not construct canonical Gaussian actions.
Section 13 returns to the finite L3 arctangent model, retaining exact trained
memories and proving time covers for four integrated initial-matrix queries
along a supplied path. It leaves causal approximation, nonlinear stability
and derivative/kernel convergence as separate requirements.
Section 14 derives the full finite tangent geometry: polynomial nuclear-norm
and intrinsic-volume bounds, their Gaussian expectations, an exact hidden
projection factor, and a deterministic reachable signed-Hessian obstruction.
The projection factor and Gaussian-typical signed control remain separate.
None of these control results asserts a global uncut three-layer population
flow or a population/GD limit for the finite metric projection. No width
limit is interchanged with infinite training time.

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

The optimization statements of Sections 1–8 use only finite differentiation, inequalities,
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

## 10. Correlated opposite labels: mixed-activation finite fitting

This section proves a finite-GF result, not a population limit or a raw-GD
theorem. Some first rows are frozen by the activation's own saturation under
the actual gradient, not by changing the optimizer. Other rows are not frozen
by prescription. Section 11 gives a separate positive unsaturated-mass result;
neither assertion alone proves nonzero hidden feature velocity.

### 10.1 Model, invariant rows and finite existence

Fix two deterministic inputs with \(\|x_a\|^2=d\),
\(G_{ab}=x_a^Tx_b/d\), \(G_{12}=\rho\in(-1,1)\), and labels
\((y_1,y_2)=(1,-1)\). In particular \(d\ge2\).
Fix \(R>0\) and an odd smooth activation \(\phi^{(1)}\), with
\(\phi^{(1)}(0)=0\), whose derivative is even, nonnegative, supported on
\([-R,R]\), and strictly positive on \((-R,R)\). Put
\[
 A=\int_0^R(\phi^{(1)})'(u)\,du>0,\qquad
 P=\|(\phi^{(1)})'\|_\infty,
 \qquad \phi^{(2)}(z)=z+\varepsilon\arctan z,\quad
 M=1+\varepsilon,\quad \varepsilon>0.
 \tag{10.1}
\]
Thus \(|\phi^{(1)}|\le A\), \(1\le(\phi^{(2)})'\le M\), and
\(|\phi^{(2)}(z)|\le M|z|\). The activations are fixed independently of
the input configuration; constants below may depend on that configuration.

Use the shared raw parameters and normalizations:
\[
 z_a^{(1)}=W^{(1)}x_a/\sqrt d,\quad
 h_a^{(1)}=\phi^{(1)}(z_a^{(1)}),\quad
 z_a^{(2)}=W^{(2)}h_a^{(1)},\quad h_a^{(2)}=\phi^{(2)}(z_a^{(2)}),
 \quad f_a=(W^{(3)})^Th_a^{(2)}/n,\quad r_a=f_a-y_a.
\]
Here both hidden widths are \(n\), and \(W^{(3)}\) is the stored readout.
With the unhalved sum loss \(\mathcal L_\Sigma=\|r\|^2=2\mathcal L_n\),
the exact flow is
\[
 \dot W^{(1)}=-\frac2{\sqrt d}\sum_a r_a\delta_a^{(1)}x_a^T,
 \quad \dot W^{(2)}=-\frac2n\sum_a r_a\delta_a^{(2)}(h_a^{(1)})^T,
 \quad \dot W^{(3)}=-2\sum_a r_a h_a^{(2)},
 \tag{10.2}
\]
where
\[
 \delta_a^{(2)}=W^{(3)}\odot(\phi^{(2)})'(z_a^{(2)}),\qquad
 \delta_a^{(1)}=(\phi^{(1)})'(z_a^{(1)})\odot
                         (W^{(2)})^T\delta_a^{(2)}.
\]
Mean-loss GF has half these velocities and takes twice the physical time
to traverse the same path. All statements here use (10.2).

Let \(\mathbf h^{(\ell)}=[h_1^{(\ell)},h_2^{(\ell)}]\), a finite
\(n\)-by-two array, and \(K^{(\ell)}\) the raw kernel block for parameter
\(W^{(\ell)}\). Direct differentiation gives
\[
 \dot r=-2Kr,\quad K=K^{(1)}+K^{(2)}+K^{(3)},
\]
\[
 K^{(1)}_{ab}=G_{ab}\frac{(\delta_a^{(1)})^T\delta_b^{(1)}}n,
 \quad K^{(2)}_{ab}=
 \frac{(h_a^{(1)})^Th_b^{(1)}}n
 \frac{(\delta_a^{(2)})^T\delta_b^{(2)}}n,
 \quad K^{(3)}=\frac{(\mathbf h^{(2)})^T\mathbf h^{(2)}}n.
 \tag{10.3}
\]
Each is a Gram matrix: the first uses the vectors
\(\delta_a^{(1)}x_a^T/\sqrt{nd}\), the second the matrices
\(\delta_a^{(2)}(h_a^{(1)})^T/n\), and the last the vectors
\(h_a^{(2)}/\sqrt n\). Consequently
\[
 -\frac{d}{dt}\mathcal L_\Sigma
 =4r^TKr
 =\frac{\|\dot W^{(1)}\|_F^2}n+
   \|\dot W^{(2)}\|_F^2+\frac{\|\dot W^{(3)}\|^2}n.
 \tag{10.4}
\]
The smooth finite vector field has a unique local solution. Integrating each
squared speed and applying Cauchy--Schwarz gives, for \(0\le s<t\),
\[
 \frac{\|W^{(1)}(t)-W^{(1)}(s)\|_F}{\sqrt n},\quad
 \|W^{(2)}(t)-W^{(2)}(s)\|_F,\quad
 \frac{\|W^{(3)}(t)-W^{(3)}(s)\|}{\sqrt n}
 \ \le\sqrt{(t-s)\mathcal L_\Sigma(0)}.
 \tag{10.5}
\]
At fixed width these bounds produce finite parameter limits at any finite
maximal endpoint. Local existence at that endpoint extends the solution.
Thus GF exists globally for every finite initial state, without any of the
success-event assumptions below.

A first row whose two initial preactivations lie outside \((-R,R)\)
remains fixed: its two gates vanish, fixing the row solves its equation, and
local uniqueness identifies this with its actual evolution. Let \(N_s,N_o\)
count these saturated rows with respectively equal and opposite signs.
Their constant contribution to the first-feature Gram is
\[
 \frac{(\mathbf h^{(1)}(t))^T\mathbf h^{(1)}(t)}n
 \succeq\frac{A^2}n
 \begin{pmatrix}N_s+N_o&N_s-N_o\\N_s-N_o&N_s+N_o\end{pmatrix}
 \succeq\gamma_n I_2,
 \quad \gamma_n=\frac{2A^2}n\min(N_s,N_o).
 \tag{10.6}
\]
The other rows add a positive semidefinite Gram. The eigenvectors
\((1,1)\) and \((1,-1)\) give the two displayed eigenvalues.

### 10.2 Fitting after an actual loss margin

Assume for now \(\gamma_n\ge\gamma>0\) and
\(\|W^{(2)}(0)\|_{\rm op}\le B_0\). Define the scalar quantities
\[
 e=\|r\|,\quad M_2=\|W^{(2)}-W^{(2)}(0)\|_F,\quad
 M_3=\|W^{(3)}\|/\sqrt n,\quad b_0=M_3(0),\quad
 S_w(t)=\int_0^t e(u)M_3(u)\,du.
 \tag{10.7}
\]
This weighted residual integral is not a replacement optimizer.
For each second neuron put
\(D_i=\operatorname{diag}((\phi^{(2)})'(z^{(2)}_{1,i}),
(\phi^{(2)})'(z^{(2)}_{2,i}))\). By (10.6), congruence of positive
matrices gives
\[
 K^{(2)}=\frac1n\sum_i(W_i^{(3)})^2D_i
 \frac{(\mathbf h^{(1)})^T\mathbf h^{(1)}}n D_i
 \succeq\gamma M_3^2 I_2.
\]
Therefore
\[
 \frac{d}{dt}\mathcal L_\Sigma\le-4\gamma M_3^2\mathcal L_\Sigma,
 \qquad e'\le-2\gamma M_3^2e\quad\hbox{where }e>0.
 \tag{10.8}
\]
At zero residual all velocities vanish and the solution stays constant.

The homogeneity defect of the top activation is bounded:
\[
 D(z)=z(\phi^{(2)})'(z)-\phi^{(2)}(z)
 =\varepsilon\left(\frac z{1+z^2}-\arctan z\right),\qquad
 \|D\|_\infty=\varepsilon\pi/2.
\]
Indeed \(D'(z)=-2\varepsilon z^2/(1+z^2)^2\), \(D(0)=0\), and its
two infinite limits are \(\mp\varepsilon\pi/2\). Set
\[
 C=2\sqrt2MA,\qquad D_0=4\sqrt2(\varepsilon\pi/2+MB_0A).
\]
The rank-one equation and \(\sum_a|r_a|\le\sqrt2e\) give
\(\|\dot W^{(2)}\|_F\le CeM_3\), hence \(M_2\le CS_w\).
Differentiating the two squared parameter norms, not the moving hidden
features, yields the exact centered balance
\[
 \frac{d}{dt}(M_2^2-M_3^2)
 =-\frac4n\sum_a r_a(W^{(3)})^T
 \left[D(z_a^{(2)})-
 (\phi^{(2)})'(z_a^{(2)})\odot W^{(2)}(0)h_a^{(1)}\right].
 \tag{10.9}
\]
For example, the first norm differentiates to
\(-4n^{-1}\sum_a r_a(W^{(3)})^T[
(\phi^{(2)})'(z_a^{(2)})\odot
(W^{(2)}-W^{(2)}(0))h_a^{(1)}]\); subtracting the readout norm
derivative supplies (10.9). Cauchy--Schwarz now proves
\[
 |M_2^2-M_3^2+b_0^2|\le D_0S_w,\quad
 M_2\le M_3+\sqrt{D_0S_w},\quad
 M_3^2\le C^2S_w^2+b_0^2+D_0S_w.
 \tag{10.10}
\]
Only the initial operator norm enters, not an initial Frobenius norm growing
with width. Also, using \(\|\mathbf h^{(1)}\|_F\le A\sqrt{2n}\),
\[
 \|f\|\le \sqrt2MA M_3(B_0+M_2)
 \le C M_3(B_0+M_3+\sqrt{D_0S_w}).
 \tag{10.11}
\]

Suppose the actual flow reaches \(\mathcal L_\Sigma(t_0)<2\) at finite
\(t_0\). Put \(e_0=e(t_0)\), \(\nu=\sqrt2-e_0>0\), and
\[
 c=\min\{1,\nu/[C(B_0+1+\sqrt{D_0})]\}>0.
\]
For \(t\ge t_0\), monotonicity and the reverse triangle inequality give
\(\|f(t)\|\ge\nu\). If \(M_3\le1\), (10.11) bounds it below by
\(c/(1+\sqrt{S_w})\); if \(M_3\ge1\), the same bound holds since
\(c\le1\). Let
\[
 F(x)=\int_0^x\frac{du}{1+\sqrt u}
 =2[\sqrt x-\log(1+\sqrt x)]\quad(x\ge0).
\]
Combining this lower bound with (10.8) and \(S_w'=eM_3\) gives
\[
 e(t)+2\gamma c[F(S_w(t))-F(S_w(t_0))]\le e_0.
 \tag{10.12}
\]
This integrates a time-domain differential inequality; it does not invert
the clock and remains valid through zero residual by constant continuation.
The inequality \(\log(1+u)\le u/2+\log2\), obtained by maximizing its
left side minus \(u/2\), implies \(F(x)\ge\sqrt x-2\log2\).
Thus, with
\[
 S_b=[F(S_w(t_0))+e_0/(2\gamma c)+2\log2]^2,\quad
 U=B_0+CS_b,\quad \beta=c/(1+\sqrt{S_b})>0,
\]
we have \(S_w(t)\le S_b\), \(\|W^{(2)}(t)\|_{\rm op}\le U\),
and an upper bound for \(M_3\) from (10.10), for every \(t\ge0\).
Moreover \(M_3(t)\ge\beta\) for \(t\ge t_0\). It follows that
\[
 \mathcal L_\Sigma(t)\le e_0^2e^{-4\gamma\beta^2(t-t_0)},\qquad
 \int_0^\infty e(t)\,dt
 \le t_0\sqrt{\mathcal L_\Sigma(0)}+e_0/(2\gamma\beta^2).
 \tag{10.13}
\]
The constants are noncircular: (10.5) already gives
\[
 S_w(t_0)\le \sqrt{\mathcal L_\Sigma(0)}b_0t_0
                   +\tfrac23\mathcal L_\Sigma(0)t_0^{3/2}.
\]
Finally, the exact equations imply
\[
 \|\dot W^{(2)}\|_F\le CeM_3,\quad
 \|\dot W^{(3)}\|/\sqrt n\le CUe,\quad
 \|\dot W^{(1)}\|_F/\sqrt n\le2\sqrt2PMUeM_3.
 \tag{10.14}
\]
All three speeds are integrable. Completeness in each finite-dimensional
parameter space gives finite endpoints, and continuity of the predictor plus
(10.13) makes their predictions exactly the two labels.

### 10.3 The actual Gaussian initialization supplies the margin

Initialize all entries independently with
\[
 W^{(1)}_{0,ij}\sim N(0,1),\quad W^{(2)}_{0,ij}\sim N(0,1/n),\quad
 W^{(3)}_{0,i}\sim N(0,n^{-2}).
 \tag{10.15}
\]
Let \((U_1,U_2)\sim N(0,G)\). Write \(p_s\) and \(p_o\) for its
probabilities of both coordinates having absolute value at least \(R\),
with respectively equal and opposite signs. Nondegenerate Gaussian density
is positive on all open corners, so
\(\gamma=A^2\min(p_s,p_o)>0\). Set \(\kappa=\gamma/2\), \(B_0=8\).
The event \(E_F=\{N_s/n\ge p_s/2,\ N_o/n\ge p_o/2\}\) gives
\(\gamma_n\ge\gamma\) and satisfies
\[
 \mathbb P(E_F^c)\le\frac4n
       \left(\frac{1-p_s}{p_s}+\frac{1-p_o}{p_o}\right).
 \tag{10.16}
\]
Each count has variance \(np(1-p)\); integrating the squared centered
count on its deviation event proves this bound, without independence between
the two counts.

Conditional on the first weights, second-preactivation row pairs are
independent centered Gaussians with covariance
\(Q=(\mathbf h^{(1)}(0))^T\mathbf h^{(1)}(0)/n\). On \(E_F\),
\(Q\succeq\gamma I_2\), \(Q_{aa}\le A^2\). Represent one pair as
\(Z=U+\sqrt\gamma\xi\), with independent Gaussian vectors of covariances
\(Q-\gamma I_2\) and \(I_2\). Conditional on \(U\), the transformed
coordinates \(\phi^{(2)}(Z_a)\) are independent. For a scalar random
variable \(T\) and independent copy \(T'\),
\[
 \operatorname{Var}(\phi^{(2)}(T))
 =\tfrac12\mathbb E(\phi^{(2)}(T)-\phi^{(2)}(T'))^2
 \ge\tfrac12\mathbb E(T-T')^2=\operatorname{Var}(T),
\]
since \((\phi^{(2)})'\ge1\). Conditional variance therefore shows that
the second-feature second-moment matrix is at least \(\gamma I_2\).
For its empirical version \(K^{(3)}(0)\), the fourth moment estimate
\[
 \mathbb E[\phi^{(2)}(Z_a)^2\phi^{(2)}(Z_b)^2\mid W^{(1)}_0]
 \le M^4\sqrt{3Q_{aa}^2\,3Q_{bb}^2}\le3M^4A^4
\]
and conditional row independence bound the expected squared Frobenius error
by \(12M^4A^4/n\). At error threshold \(\gamma/2\), this gives
\[
 \mathbb P\{K^{(3)}(0)\not\succeq\kappa I_2\mid W^{(1)}_0\}
 \le48M^4A^4/(n\gamma^2)\quad\hbox{on }E_F.
 \tag{10.17}
\]
The scalar Gaussian fourth moment is three times variance squared; it follows
by twice integrating the Gaussian density derivative by parts.

Two elementary norm bounds complete the event:
\[
 \mathbb P\{\|W^{(2)}_0\|_{\rm op}>8\}
 \le2e^{-(8-2\log9)n},\quad
 \mathbb P\{b_0>2/n\}\le e^{-(1-(\log2)/2)n}.
 \tag{10.18}
\]
For the first, a maximal 1/4-separated unit-sphere set has at most \(9^n\)
points by disjoint radius-1/8 ball volumes, and is a 1/4-net. Approximating
both unit test vectors shows that the norm is at most twice the largest
bilinear form on the two nets. Each form is \(N(0,1/n)\), whose tail beyond
four is at most \(2e^{-8n}\) by its exponential moment. The union bound gives
the first estimate. For the second, \(b_0^2=n^{-3}\sum_i\xi_i^2\), where
the \(\xi_i\) are independent standard Gaussians. Since
\(\mathbb E e^{\xi_i^2/4}=\sqrt2\), exponential Markov at \(4n\) gives
the second estimate. These exponential moments follow by integrating the
Gaussian density and completing its square.

Let \(E\) be the intersection of \(E_F\), the two norm events, and
\(K^{(3)}(0)\succeq\kappa I_2\). Then
\[
 \mathbb P(E)\ge\max(0,1-p_n),\quad
 p_n=\frac4n\left(\frac{1-p_s}{p_s}+\frac{1-p_o}{p_o}\right)
 +\frac{48M^4A^4}{n\gamma^2}
 +2e^{-(8-2\log9)n}+e^{-(1-(\log2)/2)n}\longrightarrow0.
 \tag{10.19}
\]
The conditional failure in (10.17) is integrated only over \(E_F\); no
independence between overlapping second-layer events is asserted.

It remains to prove an actual loss margin, not merely a negative initial
derivative. If initially \(\mathcal L_\Sigma(0)\le4\), energy and the
activation Lipschitz bounds give
\[
 \frac{\|\mathbf h^{(1)}(t)-\mathbf h^{(1)}(0)\|_F}{\sqrt n}
 \le P\sqrt{2t\mathcal L_\Sigma(0)},
\]
\[
 \frac{\|\mathbf h^{(2)}(t)-\mathbf h^{(2)}(0)\|_F}{\sqrt n}
 \le M\sqrt{2t\mathcal L_\Sigma(0)}
       [A+P(B_0+\sqrt{t\mathcal L_\Sigma(0)})].
 \tag{10.20}
\]
For the second inequality expand the preactivation difference as
\((W^{(2)}(t)-W^{(2)}(0))\mathbf h^{(1)}(0)+
W^{(2)}(t)(\mathbf h^{(1)}(t)-\mathbf h^{(1)}(0))\) and use (10.5).
Choose
\[
 \tau=\min\{1/4,\ \kappa/[32M^2(A+P(B_0+1))^2]\}>0.
\]
For \(t\le\tau\), (10.20) is at most \(\sqrt\kappa/2\).
Each unit sample-direction vector therefore has image under
\(\mathbf h^{(2)}(t)/\sqrt n\) of norm at least \(\sqrt\kappa/2\).
Thus \(K^{(3)}(t)\succeq\kappa I_2/4\) and (10.4) implies
\(\mathcal L_\Sigma(t)\le\mathcal L_\Sigma(0)e^{-\kappa t}\).

On the two norm events, (10.11) at zero gives \(\|f(0)\|\le2CB_0/n\).
Set
\[
 n_* =\left\lceil\max\left\{2,
 \frac{2CB_0}{\min(2-\sqrt2,\sqrt2(e^{\kappa\tau/4}-1))}
 \right\}\right\rceil.
\]
All constants are fixed and the denominator is positive. For \(n\ge n_*\),
\(\mathcal L_\Sigma(0)\le4\) and
\(\mathcal L_\Sigma(0)\le2e^{\kappa\tau/2}\). Hence the actual solution
satisfies
\[
 \mathcal L_\Sigma(\tau)\le2e^{-\kappa\tau/2}<2.
 \tag{10.21}
\]
Section 10.2 now applies. This proves global finite-GF fitting and finite
parameter endpoints on the explicit event \(E\) with probability tending to
one, for every fixed interior correlation. The nonzero Gaussian readout was
never replaced by zero.

All bounds can be chosen uniformly in width on \(E\), as follows. Set
\[
 e_* =\sqrt2e^{-\kappa\tau/4},\quad
 c_* =\min\{1,(\sqrt2-e_*)/[C(B_0+1+\sqrt{D_0})]\},\quad
 S_{\rm pre}=2\tau+\tfrac83\tau^{3/2},
\]
\[
 \overline S=[F(S_{\rm pre})+e_* /(2\gamma c_*)+2\log2]^2,
 \quad \overline U=B_0+C\overline S,
 \quad \beta_* =c_* /(1+\sqrt{\overline S}).
 \tag{10.22}
\]
Since \(b_0\le1\), the pre-margin bound gives \(S_w(\tau)\le S_{\rm pre}\).
Use the fixed lower bound \(c_*\) in (10.12) to obtain
\[
 S_w(\infty)\le\overline S,\quad
 \sup_t\|W^{(2)}(t)\|_{\rm op}\le\overline U,\quad
 \sup_t M_3(t)^2\le C^2\overline S^2+1+D_0\overline S,
\]
\[
 \mathcal L_\Sigma(t)\le e_*^2e^{-4\gamma\beta_*^2(t-\tau)}
 \quad(t\ge\tau),\qquad
 \int_0^\infty e(t)\,dt\le2\tau+e_* /(2\gamma\beta_*^2).
 \tag{10.23}
\]
These estimates do not bound individual readout coordinates uniformly in
width, or their products with top curvature. Outside \(E\) the proof asserts
global finite existence, not fitting. No constants are claimed uniform near
\(\rho=\pm1\).

## 11. Permanent first-gate mass on an augmented event

Retain exactly the model and event of Section 10. Put
\(\lambda_1=\|(\phi^{(1)})''\|_\infty>0\),
\(c_a=-2r_a\), and
\(q_a^{(1)}=(W^{(2)})^T\delta_a^{(2)}\), without a residual inside
the latter. The first-coordinate equations are
\[
 \dot z^{(1)}_{a,i}=\sum_{b=1}^2G_{ab}
       (\phi^{(1)})'(z^{(1)}_{b,i})c_b q^{(1)}_{b,i}.
 \tag{11.1}
\]
On \(E\), define
\[
 V_i=\int_0^\infty\sum_a|c_aq^{(1)}_{a,i}|\,dt,
 \qquad V_* =2\sqrt2M\overline U\overline S.
\]
Since \(\|q_a^{(1)}\|/\sqrt n\le M\overline U M_3\) and
\(\sum_a|c_a|\le2\sqrt2 e\), the Euclidean integral triangle inequality
on each finite interval, followed by the monotone limit, gives
\[
 \frac1n\sum_i V_i^2\le V_*^2.
 \tag{11.2}
\]
Every \(V_i\) is finite at each fixed width; independence from initialization
is neither assumed nor needed.

Let \(\Phi\) be the standard Gaussian distribution function and define
\[
 p_{\rm strip}=[2\Phi(R/2)-1]\,2[1-\Phi(3R/\sqrt{1-\rho^2})]>0,
\]
\[
 B_* =2V_* /\sqrt{p_{\rm strip}},\quad
 \delta_* =(R/2)e^{-\lambda_1B_*},\quad
 p_* =\min_{|z|\le R-\delta_*}(\phi^{(1)})'(z)>0.
 \tag{11.3}
\]
For each ordered pair \(a,b\) of distinct samples take the initial strip
\[
 I_a^0=\{i:|z^{(1)}_{a,i}(0)|\le R/2,
 \ |z^{(1)}_{b,i}(0)-\rho z^{(1)}_{a,i}(0)|\ge3R\}.
\]
Augment \(E\) by \(E_S=\{|I_1^0|/n,|I_2^0|/n\ge p_{\rm strip}/2\}\).
On \(E\cap E_S\), each sample has a fixed subset \(I_a\), of size at
least \(np_{\rm strip}/4\), for which
\[
 |z^{(1)}_{a,i}(t)|\le R-\delta_*\quad(t\ge0,i\in I_a),\qquad
 \inf_{t\ge0}\frac1n\sum_i[(\phi^{(1)})'(z^{(1)}_{a,i}(t))]^2
 \ge(p_{\rm strip}/4)p_*^2.
 \tag{11.4}
\]

To prove this, a row in \(I_a^0\) starts with its \(a\)-coordinate interior
and \(b\)-coordinate exterior. Before an exit from those strict conditions,
the \(b\) gate is zero and (11.1) gives
\[
 z_b^{(1)}-\rho z_a^{(1)}
   =z_b^{(1)}(0)-\rho z_a^{(1)}(0),\qquad
 \dot z_a^{(1)}=(\phi^{(1)})'(z_a^{(1)})c_aq_a^{(1)}
\]
for this row. The derivative vanishes at both endpoints and is
\(\lambda_1\)-Lipschitz, so
\(0\le(\phi^{(1)})'(z)\le\lambda_1(R-|z|)\) inside.
The absolutely continuous distance to the boundary satisfies
\((R-|z_a^{(1)}|)'\ge-\lambda_1|c_aq_a^{(1)}|(R-|z_a^{(1)}|)\)
almost everywhere. Multiplication by its integrating factor yields
\[
 R-|z_a^{(1)}(t)|\ge(R/2)e^{-\lambda_1V_i}>0,
 \qquad |z_b^{(1)}(t)|\ge3R-|\rho|R>2R.
\]
Continuity contradicts any finite first exit, and these time-independent
margins hold for every finite time. By (11.2), at most fraction
\(p_{\rm strip}/4\) of all rows have \(V_i>B_*\). Set
\(I_a=I_a^0\cap\{V_i\le B_*\}\). Subtraction of this worst-case count
from each strip count separately proves (11.4). The subsets may depend on
the entire trajectory, but are fixed in time; no selection from future data
is used in defining the actual dynamics.

For Gaussian first rows, \(z_a^{(1)}(0)\) and
\(z_b^{(1)}(0)-\rho z_a^{(1)}(0)\) are independent centered Gaussians,
of variances one and \(1-\rho^2\): their joint Gaussian characteristic
function factors because their covariance is zero. Thus each strip indicator
has mean \(p_{\rm strip}\), independently across neurons. The same count
variance argument as (10.16) gives
\[
 \mathbb P(E_S^c)\le8(1-p_{\rm strip})/(np_{\rm strip}).
\]
Consequently (11.4) holds simultaneously for both samples and all time with
probability at least
\(\max\{0,1-p_n-8(1-p_{\rm strip})/(np_{\rm strip})\}\), for
\(n\ge n_*\). No independence between the two events is assumed.

The extra event cannot simply be omitted. For even \(n\ge n_*\), choose
first rows realizing \(n/2\) preactivation pairs \((2R,2R)\) and
\(n/2\) pairs \((2R,-2R)\); the independent inputs permit this under the
displayed normalization. Choose \(W^{(2)}_0=I_n\) and
\(W^{(3)}_{0,i}=1/n\). All first gates vanish forever. Nevertheless
\(N_s=N_o=n/2\), \(\|W^{(2)}_0\|_{\rm op}=1<8\), \(b_0=1/n<2/n\),
and \(K^{(3)}(0)=\phi^{(2)}(A)^2I_2\succ\kappa I_2\).
All defining inequalities of \(E\) have strict margins. An open neighborhood
retains them and keeps every first row saturated; independent Gaussian
initialization has positive density on that neighborhood. Thus \(E\) alone
does not imply unsaturated mass, even almost surely at such fixed width.

The conclusion is gate mass, not force or motion. It supplies no lower bound
on residuals, reverse queries, hidden velocities or reverse-weighted kernels,
and no top-layer distributional nonaffinity. These two sections assert neither
a joint population limit nor a GD result, and do not cover antipodal inputs.

## 12. Dissipative caps on given operator spaces

This section concerns a different two-hidden-layer model, with three fixed
normalized inputs and the fixed activation
\[
 \phi(z)=\tfrac34(1+z)+\tfrac14\tanh z.
 \tag{12.1}
\]
It constructs global capped flows on prescribed Hilbert spaces. A separate
conditional theorem removes these caps if specified exponential tails hold.
Neither theorem constructs the Gaussian action spaces or identifies a
finite-width GF/GD limit. The cap is different from the coordinate-query cap
and the finite metric projection elsewhere in the book.

We use the half-sum loss \(E=\frac12\sum_{a=1}^3r_a^2\) and its physical
gradient-flow time throughout this section. The canonical mean squared loss
is \(\mathcal L=2E/3\). Consequently its uncapped gradient field is \(2/3\)
times the field here: evaluating an \(E\)-flow at time \(2t/3\) gives the
mean-loss flow at time \(t\). The same time rescaling applies if the entire
capped field is multiplied by \(2/3\). No raw-GD identity is inferred.

### 12.1. Spaces, fields and the loss chain rule

Let \((\Omega_\ell,\mathbb P_\ell)\), \(\ell=1,2\), be probability spaces
whose real Hilbert spaces \(\mathcal H_\ell=L^2(\Omega_\ell)\) are separable.
Give a bounded operator
\(W^{(2)}_0:\mathcal H_1\to\mathcal H_2\), together with its genuine
adjoint. It need not be Hilbert–Schmidt. This is an assumption on given
spaces, not a substitute construction of an initialized Gaussian operator.
For fixed inputs \(x_a\in\mathbb R^d\), put \(u_a=x_a/\sqrt d\) and assume
\(\|u_a\|_2=1\). The Gram \(G_{ab}=u_a^Tu_b\) may be singular; inputs
may coincide. Labels satisfy \(y_a\in\{-1,1\}\).

The state, its Hilbert norm, and initialization are
\[
 \Theta=(W^{(1)},U,W^{(3)})\in\mathcal H
 =L^2(\Omega_1;\mathbb R^d)\oplus
   \mathrm{HS}(\mathcal H_1,\mathcal H_2)\oplus\mathcal H_2,
\]
\[
 \|\Theta\|_{\mathcal H}^2
 =\mathbb E_1|W^{(1)}|^2+\|U\|_{\rm HS}^2+
   \mathbb E_2|W^{(3)}|^2,
 \qquad \Theta_0=(W^{(1)}_0,0,0),
 \tag{12.2}
\]
where \(\|W^{(1)}_0\cdot u_a\|_{L^2(\Omega_1)}=1\).
There is no distributional assumption on this first field. Set
\(W^{(2)}=W^{(2)}_0+U\).

For clarity, the Hilbert–Schmidt facts needed here can be obtained directly.
For an orthonormal basis \((e_j)\) of \(\mathcal H_1\), define
\(\|U\|_{\rm HS}^2=\sum_j\|Ue_j\|^2\) and use the corresponding sum
of inner products. Cauchy–Schwarz in the basis expansion of a vector gives
\(\|U\|_{\rm op}\le\|U\|_{\rm HS}\). Conversely any square-summable
family \((v_j)\) defines \(U\sum_j c_je_j=\sum_jc_jv_j\); this series
converges by Cauchy–Schwarz. The identification with
\(\ell^2(\mathcal H_2)\) proves completeness. Expanding in an orthonormal
basis of \(\mathcal H_2\) and interchanging nonnegative sums proves
basis independence by Parseval. In particular,
\[
 \|B\otimes H\|_{\rm HS}=\|B\|_{\mathcal H_2}\|H\|_{\mathcal H_1},
 \qquad
 \langle B\otimes H,U\rangle_{\rm HS}=\langle B,UH\rangle_{\mathcal H_2},
 \tag{12.3}
\]
where \((B\otimes H)V=B\mathbb E_1[HV]\).

Define the population fields, with all products taken on their own layer,
\[
 \begin{aligned}
 Z_a^{(1)}&=W^{(1)}\cdot u_a,& H_a^{(1)}&=\phi(Z_a^{(1)}),\\
 Z_a^{(2)}&=W^{(2)}H_a^{(1)},& H_a^{(2)}&=\phi(Z_a^{(2)}),\\
 f_a&=\mathbb E_2[W^{(3)}H_a^{(2)}],&r_a&=f_a-y_a,\\
 \Delta_a^{(2)}&=W^{(3)}\phi'(Z_a^{(2)}),&
 Q_a^{(1)}&=(W^{(2)})^*\Delta_a^{(2)},\\
 P_a&=r_aQ_a^{(1)},&P&=\bigl(\textstyle\sum_a P_a^2\bigr)^{1/2}.
 \end{aligned}
 \tag{12.4}
\]
The residual-free backward fields are \(\Delta_a^{(2)}\) and
\(\Delta_a^{(1)}=\phi'(Z_a^{(1)})Q_a^{(1)}\). The true loss directions
and the uncapped field are
\[
 \begin{aligned}
 g_1&=\sum_a\phi'(Z_a^{(1)})P_au_a,\\
 g_2&=\sum_a r_a\Delta_a^{(2)}\otimes H_a^{(1)},\\
 g_3&=\sum_a r_aH_a^{(2)},\qquad F(\Theta)=-(g_1,g_2,g_3).
 \end{aligned}
 \tag{12.5}
\]

The bounds \(|\phi(z)|\le1+|z|\), \(3/4\le\phi'(z)\le1\), and
\(|\phi''(z)|\le1/2\) follow from the displayed activation. They imply
that every field in (12.4) is in its indicated \(L^2\) space. On each
bounded state ball, all these norms, residuals and direction norms are
bounded by constants depending on the ball, the fixed data and
\(\|W^{(2)}_0\|_{\rm op}\). Forward fields and residuals are Lipschitz
there: expand each operator product into its operator difference and input
difference, use (12.3), and use the scalar activation's Lipschitz bound.
Backward fields are continuous there; local Lipschitzness is not assumed.

Here is the needed continuity argument. If \(A_j\to A\) and \(V_j\to V\)
in \(L^2\), and \(b\) is bounded and continuous, then
\[
 A_jb(V_j)\longrightarrow Ab(V)\quad\hbox{in }L^2.
 \tag{12.6}
\]
The part \((A_j-A)b(V_j)\) is bounded by
\(\|b\|_\infty\|A_j-A\|_2\). Every subsequence of \(V_j\) has a
further almost-surely convergent subsequence; dominated convergence against
\(|A|^2\) handles the other part. If the whole sequence failed to converge,
a subsequence separated from zero would contradict this conclusion.
Apply this argument to each gate product, then the operator and rank-one
estimates, to obtain continuity of all fields and of \(F\).

A strong solution is a \(C^1\) curve in \(\mathcal H\) satisfying the
indicated integral equation, hence its differential equation. For every
\(C^1\) state curve the loss satisfies
\[
 E'=\langle g_1,\dot W^{(1)}\rangle
     +\langle g_2,\dot U\rangle_{\rm HS}
     +\langle g_3,\dot W^{(3)}\rangle.
 \tag{12.7}
\]
To justify the chain rule in \(L^2\), the Bochner integral of a continuous
velocity gives coordinatewise absolutely continuous representatives on a
compact time interval. Indeed its time integral of \(L^1\) norms is
finite by Cauchy–Schwarz, so Fubini applies. The ordinary scalar chain rule
gives \(\dot H_a^{(1)}=\phi'(Z_a^{(1)})\dot Z_a^{(1)}\); (12.6) makes
this velocity continuous in \(L^2\). Its integrated identity therefore
also proves Hilbert-space differentiation. Next
\(\dot Z_a^{(2)}=\dot U H_a^{(1)}+W^{(2)}\dot H_a^{(1)}\), and the
same reasoning gives \(\dot H_a^{(2)}\). Differentiate \(f_a\), multiply
by \(r_a\), and use the genuine adjoint and (12.3) to obtain (12.7).
No Fréchet differentiability of the nonlinear activation on all of \(L^2\)
has been used.

### 12.2. Global dissipative approximants

Choose a smooth nonincreasing \(\eta:[0,\infty)\to[0,1]\), equal to one
on \([0,1]\) and zero on \([2,\infty)\). An explicit choice on \((1,2)\)
is \(\rho(2-s)/(\rho(2-s)+\rho(s-1))\), where
\(\rho(s)=e^{-1/s}\) for \(s>0\) and zero otherwise. In this section
\(\eta\) is a cutoff function, not a GD step. For \(R\ge1\), set
\[
 \tau_R(s)=\operatorname{sgn}(s)R\int_0^{|s|/R}\eta(v)\,dv,
 \quad \chi_R(s)=\begin{cases}\tau_R(s)/s&s\ne0,\\1&s=0,\end{cases}
 \quad C_R(p)=\chi_R(|p|)p\quad(p\in\mathbb R^3).
 \tag{12.8}
\]
Both \(\tau_R\) and \(C_R\) are smooth and 1-Lipschitz, equal to the
identity inside radius \(R\), and bounded in magnitude by
\(\min(|\text{input}|,2R)\). In fact their radial derivative is
\(\tau_R'\in[0,1]\); the radial map's tangential eigenvalues are
\(\tau_R(|p|)/|p|\in(0,1]\). Integrating the Jacobian on segments gives
the Lipschitz bound, and near zero the map is the identity. In particular,
\(0<\chi_R\le1\) and
\[
 |p-C_R(p)|\le|p|\mathbf1_{|p|>R},\qquad
 |s-\tau_R(s)|\le|s|\mathbf1_{|s|>R}.
 \tag{12.9}
\]

**Theorem 12.1.** For every \(R\ge1\), the equations
\[
 \dot W_R^{(1)}=-\sum_a\phi'(Z_{R,a}^{(1)})C_R((P_{R,b})_b)_a u_a
               =-\chi_R(P_R)g_{1,R},
 \quad \dot U_R=-g_{2,R},\quad
 \dot W_R^{(3)}=-\tau_R(g_{3,R})
 \tag{12.10}
\]
have a unique global strong solution from \(\Theta_0\). They satisfy
\[
 E_R(t)+\int_0^t\|\dot\Theta_R(s)\|_{\mathcal H}^2ds\le E_0=3/2,
 \quad \|\Theta_R(t)-\Theta_0\|_{\mathcal H}\le\sqrt{3t/2},
 \quad |W_R^{(3)}(t)|\le2Rt\quad\hbox{a.e.}
 \tag{12.11}
\]
On every finite horizon, all true field norms and \(\|F(\Theta_R)\|\)
are bounded uniformly in \(R\).

**Proof.** Fix a finite \(T>0\), and put \(M=1+2RT\). Temporarily replace
\(W^{(3)}\) by \(\tau_M(W^{(3)})\) only in
\(\Delta_a^{(2)}\) and the backward fields derived from it. Use these
modified backward fields in the first two equations of (12.10), retaining
the original forward fields, residuals and readout equation. This defines
an autonomous extension on all of \(\mathcal H\).

For two states in a fixed ball its top-gate difference is bounded by
\[
 \|\tau_M(W^{(3)})\phi'(Z_a^{(2)})
   -\tau_M(\bar W^{(3)})\phi'(\bar Z_a^{(2)})\|_2
 \le\|W^{(3)}-\bar W^{(3)}\|_2+M\|Z_a^{(2)}-\bar Z_a^{(2)}\|_2.
 \tag{12.12}
\]
The factor \(M\) uses \(|\tau_M|\le2M\) and
\(\operatorname{Lip}(\phi')\le1/2\). Apply the genuine adjoints and
\(\|U-\bar U\|_{\rm op}\le\|U-\bar U\|_{\rm HS}\) to compare
the incoming fields. Their residual-weighted differences obey
\[
 \|P_a-\bar P_a\|_2\le
 |r_a|\|Q_a^{(1)}-\bar Q_a^{(1)}\|_2
 +|r_a-\bar r_a|\|\bar Q_a^{(1)}\|_2.
 \tag{12.13}
\]
For the lower gate, apply the vector cap before estimating multiplication:
\[
 \|\phi'(Z_a^{(1)})C_R(p)_a-
       \phi'(\bar Z_a^{(1)})C_R(\bar p)_a\|_2
 \le\|p-\bar p\|_{L^2(\Omega_1;\mathbb R^3)}
     +R\|Z_a^{(1)}-\bar Z_a^{(1)}\|_2.
 \tag{12.14}
\]
Finally expand a rank-one difference and use
\[
 \|B\otimes H-\bar B\otimes\bar H\|_{\rm HS}
 \le\|B-\bar B\|_2\|H\|_2+\|\bar B\|_2\|H-\bar H\|_2.
 \tag{12.15}
\]
Together with the forward bounds and the readout cap's Lipschitz bound,
these estimates give a ball-wise Lipschitz constant \(K_{B,T}(1+R)\).
There is no product of the two cap sizes: the input Lipschitz constant in
(12.14) is one. The field norm on a fixed ball is bounded independently of
\(R,M\), since every cap decreases magnitude.

Choose a short interval whose length times the field bound keeps a closed
continuous-path ball inside the state ball, and whose length times its
Lipschitz constant is less than one. The integral map is a contraction on
this complete path space. Its iterates give a unique local strong solution.
The readout integral gives \(|W^{(3)}(t)|\le2Rt<M\) before \(T\), so
the auxiliary top cap is inactive. Substitution into (12.7) yields
\[
 E_R'=-\mathbb E_1[\chi_R(P_R)|g_{1,R}|^2]
      -\|g_{2,R}\|_{\rm HS}^2
      -\mathbb E_2[\chi_R(g_{3,R})|g_{3,R}|^2]
 \le-\|\dot\Theta_R\|_{\mathcal H}^2.
 \tag{12.16}
\]
The inequality is \(\chi_R^2\le\chi_R\). One common nonnegative scalar
multiplies the entire first-row gradient, so this remains valid when sample
directions cancel. Integration and time Cauchy–Schwarz prove (12.11).

If a maximal interval ended before \(T\), the energy estimate would keep
its states in a fixed ball. The bounded field makes the path Cauchy at its
endpoint. Completeness supplies a state there; its readout bound is preserved
by strong \(L^2\) convergence, by an almost-sure subsequence. The same local
extension continues the curve, a contradiction. Two choices of \(T\) agree
on overlaps: choose one auxiliary top cap larger than both readout bounds
and apply local uniqueness successively. Every strong solution of (12.10)
has that readout bound, so uniqueness applies to all such solutions. The
uniform true-field bounds follow from the energy ball bounds. \(\square\)

### 12.3. What an exponential-tail premise would give

**Theorem 12.2 (conditional continuation).** In addition to Theorem 12.1,
suppose that for every finite \(T>0\) there exist \(K_T,c_T>0\) with
\[
 \sup_{R\ge1,\,0\le t\le T}
 \left(\|P_R(t)\mathbf1_{P_R(t)>a}\|_{L^2(\Omega_1)}
 +\|g_{3,R}(t)\mathbf1_{|g_{3,R}(t)|>a}\|_{L^2(\Omega_2)}\right)
 \le K_T e^{-c_Ta}\quad(a\ge1).
 \tag{12.17}
\]
Then \(\Theta_R\) converges in \(C([0,T];\mathcal H)\), for each finite
\(T\), to a global strong solution of \(\dot\Theta=F(\Theta)\).
All fields in (12.4), and \(\Delta_a^{(1)}\), converge uniformly in their
strong \(L^2\) norms. The three true raw kernel blocks converge uniformly:
\[
 K^{(1)}_{ab}=G_{ab}\mathbb E_1[\Delta_a^{(1)}\Delta_b^{(1)}],\quad
 K^{(2)}_{ab}=\mathbb E_2[\Delta_a^{(2)}\Delta_b^{(2)}]
                  \mathbb E_1[H_a^{(1)}H_b^{(1)}],\quad
 K^{(3)}_{ab}=\mathbb E_2[H_a^{(2)}H_b^{(2)}].
 \tag{12.18}
\]
The limit has the exact loss energy identity. It is unique against strong
competitors with the same initial state on their common compact intervals,
and it restarts uniquely at every state reached by this initialized curve.
The premise (12.17) is not proved here.

**Proof.** First (12.17) gives readout tails. For \(a\ge1\),
\(\mathbb P_2(|g_{3,R}|>a)\le K_T^2a^{-2}e^{-2c_Ta}\); enlarge
constants to include smaller thresholds. The identity
\[
 \mathbb E|X|^j=j\int_0^\infty a^{j-1}\mathbb P(|X|>a)\,da
\]
and repeated integration by parts in the exponential integral give
\(\|g_{3,R}(t)\|_{L^j}\le D_Tj\) for integers \(j\ge2\), uniformly
in cap and time. Here \(j!\le j^j\) bounds the resulting factorial.
The readout integral and Minkowski give
\(\|W_R^{(3)}(t)\|_{L^j}\le TD_Tj\).
For sufficiently large \(a\), choose
\(j=\lfloor a/(eTD_T)\rfloor\ge2\) in Markov's inequality. The bound
\((TD_Tj/a)^j\le e^{-j}\) supplies an exponential probability tail.
Smaller \(a\) are covered by enlarged constants. Applying
\[
 \mathbb E[X^2\mathbf1_{|X|>a}]
 =a^2\mathbb P(|X|>a)+\int_a^\infty2v\mathbb P(|X|>v)\,dv
\]
and absorbing polynomial factors into a smaller exponential rate yields
\[
 \sup_{R,t\le T}\|W_R^{(3)}(t)\mathbf1_{|W_R^{(3)}(t)|>a}\|_2
 \le D'_T e^{-c'_Ta}\quad(a\ge1).
 \tag{12.19}
\]

We need tails only on a reference state. For bounded Lipschitz \(b\),
splitting at \(|A|=L\) proves
\[
 \|A[b(V)-b(\bar V)]\|_2
 \le\operatorname{Lip}(b)L\|V-\bar V\|_2
      +2\|b\|_\infty\|A\mathbf1_{|A|>L}\|_2.
 \tag{12.20}
\]
For two states in a common bounded ball, split their top-gate difference as
\[
 (W^{(3)}-\bar W^{(3)})\phi'(Z_a^{(2)})
 +\bar W^{(3)}[\phi'(Z_a^{(2)})-\phi'(\bar Z_a^{(2)})].
\]
Use (12.20) with the reference readout and (12.19). Apply the operator
difference estimate and (12.13) to bound the incoming differences. At the
lower gate split
\[
 g_1-\bar g_1=\sum_a\left\{
 \phi'(Z_a^{(1)})(P_a-\bar P_a)
 +\bar P_a[\phi'(Z_a^{(1)})-\phi'(\bar Z_a^{(1)})]\right\}u_a.
\]
Use (12.20) with \(\bar P_a\), whose tail is bounded by the reference
\(\bar P\) tail. The first term multiplies the already estimated incoming
difference by a bounded gate, so there is only one cutoff factor, not its
square. Equation (12.15) handles the matrix direction, and the readout
direction uses only forward differences. With \(s=\|\Theta-\bar\Theta\|\),
the result is
\[
 \|F(\Theta)-F(\bar\Theta)\|\le K(1+L)s+Ke^{-cL}.
 \tag{12.21}
\]
Constants may depend on the horizon and ball, but not the caps. Choose
\(L=\max(1,c^{-1}\log(1/s))\) for \(0<s<1\), and use bounded field
norms for larger distances. Enlarging constants gives
\[
 \|F(\Theta)-F(\bar\Theta)\|\le b_Ts\log(B_T/s).
 \tag{12.22}
\]
Take \(B_T\) larger than \(e\) times the ball's distance range, so this
modulus is increasing there. At zero it is interpreted as zero. It applies
between approximants, and against any other bounded state when the reference
alone has (12.17), (12.19).

The defects of (12.10) relative to the true field satisfy
\[
 \|\dot\Theta_R-F(\Theta_R)\|
 \le\sqrt3\|P_R\mathbf1_{P_R>R}\|_2
       +\|g_{3,R}\mathbf1_{|g_{3,R}|>R}\|_2
 \le Ke^{-cR}.
 \tag{12.23}
\]
The factor \(\sqrt3\) is Cauchy–Schwarz in the three unit input vectors;
there is no matrix defect. Comparing any two cap values \(R'\ge R\)
by their integral equations gives the absolutely continuous distance
inequality
\[
 s'\le b_Ts\log(B_T/s)+\delta_R,\quad s(0)=0,
 \qquad \delta_R=K'e^{-cR}.
 \tag{12.24}
\]
One can prove its comparison estimate directly. Start a positive scalar
majorant at \(Y(0)=\delta_R\), with
\(Y'=b_TY\log(B_T/Y)+\delta_R\). Before leaving the comparison range,
\(Y\ge\delta_R\) and \(\log(B_T/Y)\ge1\), whence
\(Y'\le(b_T+1)Y\log(B_T/Y)\). Differentiating
\(\log(B_T/Y)\) gives
\[
 Y(t)\le B_T(\delta_R/B_T)^{\exp(-(b_T+1)t)}.
 \tag{12.25}
\]
The distance is bounded by this majorant: away from zero the scalar right
side is locally Lipschitz, and the positive initial gap permits the usual
first-crossing comparison (or a strictly enlarged forcing followed by a
limit). For large \(R\), (12.25) stays inside the comparison range for all
\(t\le T\), by a first-exit argument. This proves uniform Cauchy convergence
of the full real-indexed cap family in the complete path space.

Continuity of a field map gives its uniform convergence on the paths, without
asserting compactness of a bounded Hilbert ball. Indeed, if uniform convergence
failed, choose \(R_j\to\infty\), \(t_j\in[0,T]\) witnessing a fixed
discrepancy and a subsequence with \(t_j\to t_*\). Uniform state convergence
implies both \(\Theta_{R_j}(t_j)\) and \(\Theta(t_j)\) tend to
\(\Theta(t_*)\), contradicting continuity. Apply this argument to all field
maps, using (12.6) also for \(\Delta_a^{(1)}\). Equations (12.23) and
the integral equations pass to
\(\Theta(t)=\Theta_0+\int_0^tF(\Theta(v))\,dv\). The integrand is
continuous, so the limit is strong. Cauchy–Schwarz and the uniform field
bounds give (12.18). The exact energy identity follows from (12.7).

At each time strong \(L^2\) convergence has an almost-sure subsequence.
On the event that the limit field exceeds threshold \(a\), its approximants
eventually exceed \(a/2\); Fatou bounds its squared tail by the uniform
approximating tails at \(a/2\). Adjust constants for \(1\le a<2\).
Thus the limit inherits (12.17), (12.19), uniformly in time, even though the
subsequence may depend on time. Compare a strong competitor to this reference
limit using (12.20)–(12.22). Every strong competitor is bounded on its compact
time intervals. Its distance has zero initial value and zero forcing in
(12.24). A positive initial majorant tending to zero in (12.25), now without
forcing, proves equality. The same comparison identifies overlapping horizons
and proves uniqueness starting at every reached state. The already constructed
global curve supplies existence of those continuations. \(\square\)

Theorem 12.1 supplies neither (12.17) nor a canonical Gaussian action.
Bounded \(L^2\) norms do not imply uniform square tails: on \((0,1)\),
\(A_j=\sqrt j\,\mathbf1_{(0,1/j)}\) has norm one, entirely above each
fixed amplitude threshold for large \(j\). This is an example about norms,
not a trained-path counterexample. The conditional theorem establishes
continuation on the specified spaces if its quantitative tails hold. Identifying
these spaces and comparing actual finite GF and simultaneous raw GD, including
the small random stored readout, remain separate obligations. No fitting or
persistent nonlinear feature-motion conclusion is supplied by either theorem.

## 13. Integrated initial-matrix queries with exact trained memory

This section gives a finite representation and a supplied-path approximation
bound for the three-hidden-layer arctangent network. It keeps both orientations
of both hidden matrices and all trained increments. It does not construct a
population space or a causal finite-query approximation to training.

### 13.1. Exact finite equations

Fix a width \(n\ge1\), one input \(x=1\), one label \(y=1\), and
\(\phi(z)=\arctan z\). All hidden vectors and the stored readout
\(a=W^{(4)}\) have length \(n\); the two middle matrices have size
\(n\times n\). Vector norms are ordinary Euclidean norms, and matrix
norms are ordinary operator norms; every width normalization is explicit. Define
\[
 h^\ell=\phi(z^\ell),\quad z^2=W^{(2)}h^1,\quad
 z^3=W^{(3)}h^2,\quad f=a^Th^3/n,
\]
\[
 \delta^3=a\odot\phi'(z^3),\quad q^2=(W^{(3)})^T\delta^3,
 \quad\delta^2=\phi'(z^2)\odot q^2,\quad
 \delta^1=\phi'(z^1)\odot(W^{(2)})^T\delta^2.
 \tag{13.1}
\]
Superscripts on vectors are layer indices. The feature-ascent equations are
\[
 (z^1)'=\delta^1,\qquad (W^{(2)})'=\delta^2(h^1)^T/n,
 \qquad (W^{(3)})'=\delta^3(h^2)^T/n,\qquad a'=h^3.
 \tag{13.2}
\]
The prime means feature time \(s\), with block mobilities \((n,1,1,n)\).
The physical full-square-loss velocity is \(-2(f-1)\) times (13.2).
When a physical orbit is represented by a feature orbit, its clock satisfies
\(ds/dt=-2(f-1)\). No clock or width convergence is used here.

The canonical initialization has independent \(z^1_{0,i}\sim N(0,1)\),
middle entries \(N(0,1/n)\), and \(a_{0,i}\sim N(0,n^{-2})\), all blocks
independent. Every following identity holds for arbitrary deterministic
initial values along a finite \(C^1\) solution on \([0,S]\). The estimates
are implications of their explicitly stated bounds, not new probability
estimates for those events.

Let \(F(z)=z+z^3/3\), applied coordinatewise, and \(X^1=F(z^1)\).
Its derivative \(F'=1/\phi'\) is positive, and its limits at the two ends
of the real line are infinite with the corresponding signs. It therefore
has a globally defined inverse. Put
\[
 b(s)=\int_0^s\delta^2(u)\,du,\quad
 M_2(s)=\int_0^s b'(u)(h^1(u))^T/n\,du,\quad
 M_3(s)=\int_0^s\delta^3(u)(h^2(u))^T/n\,du.
 \tag{13.3}
\]
The symbol \(b\) here denotes a primitive, not a backward sensitivity.
Then \(W^{(\ell)}=W^{(\ell)}_0+M_\ell\) for \(\ell=2,3\), and
\[
 \begin{split}
 X^1(s)&=X^1_0+(W^{(2)}_0)^Tb(s)+R_1(s),\\
 R_1(s)&=\int_0^s h^1(u)\frac{b'(u)^T[b(s)-b(u)]}{n}\,du,
 \qquad z^1=F^{-1}(X^1).
 \end{split} \tag{13.4}
\]
Indeed \((X^1)'=(W^{(2)})^T b'\). Substituting the integral for
\(M_2\) into \(\int_0^s M_2(v)^Tb'(v)\,dv\), and integrating first
over \(u\le v\le s\), gives (13.4). All integrands are continuous in
finite dimension, so this interchange is legitimate. The other equations are
\[
 \begin{aligned}
 z^2(s)&=W^{(2)}_0h^1(s)+\int_0^s b'(u)
                         \frac{h^1(u)^Th^1(s)}n\,du,\\
 z^3(s)&=W^{(3)}_0h^2(s)+\int_0^s\delta^3(u)
                         \frac{h^2(u)^Th^2(s)}n\,du,\\
 a(s)&=a_0+\int_0^s h^3(u)\,du,\\
 q^2(s)&=(W^{(3)}_0)^T\delta^3(s)+\int_0^s h^2(u)
                         \frac{\delta^3(u)^T\delta^3(s)}n\,du,\\
 b'(s)&=\phi'(z^2(s))\odot q^2(s).
 \end{aligned} \tag{13.5}
\]
Here \(h^\ell=\phi(z^\ell)\) and \(\delta^3=a\odot\phi'(z^3)\).
These equations follow by substituting the trained matrices into (13.1).
Conversely, a \(C^1\) solution of (13.3)–(13.5) with \(b(0)=0\)
and the stated initial data reconstructs (13.2): differentiation gives
\(R_1'=M_2^Tb'\), hence \((X^1)'=(W^{(2)})^Tb'\), while the
matrix and readout derivatives follow directly from their integrals.

There are precisely four initial-matrix actions in this representation:

| Initial action | Argument |
|---|---|
| \(W^{(2)}_0\) | \(h^1\) |
| \((W^{(2)}_0)^T\) | \(b\) |
| \(W^{(3)}_0\) | \(h^2\) |
| \((W^{(3)}_0)^T\) | \(\delta^3\) |

The lower backward vector \(\delta^2\) remains in the equation for
\(b'\). It is its primitive that enters the initial lower transpose.

### 13.2. A width-independent time net on a supplied path

Assume, on \([0,S]\),
\[
 \|W^{(2)}\|_{\rm op},\ \|W^{(3)}\|_{\rm op},\ \|a\|_\infty
 \le B,\qquad B\ge1. \tag{13.6}
\]
Write \(c=\pi/2\); then \(|\phi|\le c\), \(|\phi'|\le1\),
and \(|\phi''|\le2\). Thus
\(\frac{\|\delta^3\|_2}{\sqrt n}\le B\), \(\frac{\|q^2\|_2}{\sqrt n}\le B^2\), and
\(\frac{\|b'\|_2}{\sqrt n}=\frac{\|\delta^2\|_2}{\sqrt n}\le B^2\). Direct differentiation gives
\[
 \begin{aligned}
 (h^1)'&=\phi'(z^1)^2\odot(W^{(2)})^T\delta^2,\\
 (z^2)'&=\frac{\|h^1\|_2^2}{n}\delta^2+W^{(2)}(h^1)',\\
 (h^2)'&=\phi'(z^2)\odot(z^2)',\\
 (z^3)'&=\frac{\|h^2\|_2^2}{n}\delta^3+W^{(3)}(h^2)',\\
 (\delta^3)'&=h^3\odot\phi'(z^3)
                  +a\odot\phi''(z^3)\odot(z^3)'.
 \end{aligned} \tag{13.7}
\]
Consequently their Euclidean norms divided by \(\sqrt n\), in the same
order, are bounded by
\[
 B^3,\quad Z_2=(c^2+B^2)B^2,\quad Z_2,\quad
 Z_3=c^2B+BZ_2,\quad c+2BZ_3.
 \tag{13.8}
\]
In particular every argument in the table has \(\frac{\|v'\|_2}{\sqrt n}\le C\),
where \(C=\max\{1,B^2,B^3,Z_2,c+2BZ_3\}\) depends only on \(B\).
Integration proves \(\frac{\|v(s)-v(t)\|_2}{\sqrt n}\le C|s-t|\).

For \(\varepsilon>0\), choose a mesh of \([0,S]\) with gaps at most
\(\varepsilon/C\). It uses at most \(1+\lceil CS/\varepsilon\rceil\)
points when \(S>0\), and one when \(S=0\). If \(\pi(s)\) is the
last mesh point before \(s\), then for each table entry \((A,v)\),
\[
 \sup_{s\le S}\frac{\|A[v(s)-v(\pi(s))]\|_2}{\sqrt n}
 \le\|A\|_{\rm op}\varepsilon\le B\varepsilon.
 \tag{13.9}
\]
The last bound follows from (13.6) at time zero and equality of a matrix
and transpose operator norm. Thus each supplied trajectory admits a number
of sampled arguments per orientation independent of width. All trained
memory terms in (13.3)–(13.5) are still retained.

### 13.3. Continuity of the retained rank memories

For two \(C^1\) path pairs \((b,h)\), \((\widetilde b,\widetilde h)\)
with \(b(0)=\widetilde b(0)=0\), assume
\(\frac{\|h\|_2}{\sqrt n},\frac{\|\widetilde h\|_2}{\sqrt n}\le B_h\),
\(\frac{\|h'\|_2}{\sqrt n},\frac{\|\widetilde h'\|_2}{\sqrt n}\le L_h\), and
\(\frac{\|b'\|_2}{\sqrt n},\frac{\|\widetilde b'\|_2}{\sqrt n}\le L_b\).
Let \(e_b=\sup_s\frac{\|b-\widetilde b\|_2}{\sqrt n}\) and
\(e_h=\sup_s\frac{\|h-\widetilde h\|_2}{\sqrt n}\).
For \(M(s)=\int_0^s b'h^T/n\,du\), integration by parts gives
\[
 M-\widetilde M=(b-\widetilde b)h^T/n
 -\int_0^s(b-\widetilde b)(h')^T/n\,du
 +\int_0^s\widetilde b'(h-\widetilde h)^T/n\,du.
\]
The rank-one identity \(\|vw^T/n\|_{\rm op}=\|v\|_2\|w\|_2/n\)
follows by Cauchy–Schwarz, with equality in the direction of \(w\) when
both vectors are nonzero. Therefore
\[
 e_M:=\sup_s\|M-\widetilde M\|_{\rm op}
 \le(B_h+SL_h)e_b+SL_b e_h. \tag{13.10}
\]
For \(R(s)=\int_0^s M^Tb'\,du\), split its difference into
\(\int(M-\widetilde M)^Tb'\) and
\(\int\widetilde M^T(b'-\widetilde b')\).
Integrating the second term by parts, and using
\(\|\widetilde M\|_{\rm op}\le SL_bB_h\),
\(\|\widetilde M'\|_{\rm op}\le L_bB_h\), proves
\[
 \sup_s\frac{\|R-\widetilde R\|_2}{\sqrt n}
 \le SL_b e_M+2SL_bB_h e_b. \tag{13.11}
\]
These are the lower-memory bounds for \(h=h^1\). For top memory,
if both \(h^2\) paths satisfy \(\|h^2\|_2/\sqrt n\le B_2\) and both
\(\delta^3\) paths satisfy \(\|\delta^3\|_2/\sqrt n\le D_3\), the direct difference
of its two rank-one integrands gives
\[
 \sup_s\|M_3-\widetilde M_3\|_{\rm op}
 \le SB_2\sup_s\frac{\|\delta^3-\widetilde\delta^3\|_2}{\sqrt n}
       +SD_3\sup_s\frac{\|h^2-\widetilde h^2\|_2}{\sqrt n}. \tag{13.12}
\]
No convergence of \(b'\) was needed for (13.10)–(13.11); its uniform
bound and the regularity of \(h\) supplied the integration by parts.
The mesh estimate controls the residuals obtained by changing only the four
initial responses in the integral equations along the given path. It does
not estimate the difference of solutions of those changed equations.

### 13.4. What the representation still requires

A sampled actual query has been generated using all earlier matrix actions,
including actions at arguments absent from the retained mesh. Its value is
therefore not shown measurable from a transcript containing only the retained
calls. A proposed algorithm can use its own frozen responses and queries;
(13.9) proves consistency along the actual path, not stability of that
algorithm or legitimacy of conditioning its queries as independent Gaussian
innovations. No such conditioning is used in this section.

The nonlinear stability term is explicit. With the same zero primitive,
\[
 b(s)-\widetilde b(s)=\int_0^s\!
 \{\phi'(z^2)\odot(q^2-\widetilde q^2)
  +[\phi'(z^2)-\phi'(\widetilde z^2)]\odot\widetilde q^2\}\,du.
 \tag{13.13}
\]
The first summand has Euclidean norm divided by \(\sqrt n\) at most \(\frac{\|q^2-\widetilde q^2\|_2}{\sqrt n}\).
Splitting the second at any \(Q>0\) gives
\[
 \frac{\|[\phi'(z^2)-\phi'(\widetilde z^2)]\odot\widetilde q^2\|_2}{\sqrt n}
 \le 2Q\frac{\|z^2-\widetilde z^2\|_2}{\sqrt n}
    +2\frac{\|\widetilde q^2\mathbf1_{|\widetilde q^2|>Q}\|_2}{\sqrt n}.
 \tag{13.14}
\]
The mean value theorem bounds the first part and \(|\phi'|\le1\)
bounds the second. An RMS bound alone gives no uniform tail decay: the
vectors \(\sqrt n e_1\) have RMS one and tail RMS one for every
\(n>Q^2\). Taking \(z=e_1\), \(\widetilde z=0\), and
\(\widetilde q=\sqrt n e_1\) also makes the left side of (13.14) equal
to \(1/2\), although \(\frac{\|z-\widetilde z\|_2}{\sqrt n}=1/\sqrt n\).
These deterministic arrays refute a bound based only on those norms; they
are not asserted to be states reached by the initialized network.

Temporal Lipschitz bounds alone also give no strong Hilbert-space compactness.
In \(\ell^2\), the paths \(s\mapsto s e_j\) are uniformly bounded and
Lipschitz on \([0,S]\), but at fixed \(s>0\) distinct values are separated
by \(\sqrt2s\). No norm-convergent subsequence exists there.
Finally the lower backward response is
\[
 (W^{(2)})^T\delta^2
   =\frac{d}{ds}[(W^{(2)}_0)^Tb]+M_2^Tb'. \tag{13.15}
\]
Uniform approximation of the integrated response need not control its
derivative. For nonzero fixed \(v\), \(j^{-1}\sin(js)v\) tends uniformly
to zero and has bounded derivative, while the squared time-\(L^2\) norm of
its derivative is
\(\|v\|^2(S/2+\sin(2jS)/(4j))\), tending to \(S\|v\|^2/2\)
when \(S>0\). Hidden velocities and raw first-kernel convergence therefore
need additional control. None of these examples asserts a canonical network
counterexample. They identify the exact missing inferences between the finite
representation, causal approximation, state convergence and derivative
observables. Cap removal and autonomous population restart remain separate.

## 14. Exact tangent geometry and a reached signed-Hessian obstruction

Sections 14.1–14.5 give a deterministic finite-width counterexample to a specific
pointwise matrix estimate. It uses the original three-hidden-layer arctangent
network with all blocks trained, one sample `d=m=1`, `x_1=y_1=1`, the full
loss \(\mathcal L_n=(f_n-1)^2\), and stored block mobilities \((n,1,1,n)\).
The constructed hidden initialization is correlated and deterministic. It is
not an independent Gaussian initialization or a typical-Gaussian obstruction.

The result separates two kinds of control. The first preactivation and
readout RMS and both hidden-matrix operator norms stay bounded on the whole
constructed trajectory segment. The complete Hessian is bounded in operator
norm at its terminal state. Its material derivative nevertheless has a
positive Rayleigh quotient growing linearly with width, even after subtracting
any fixed real multiple of the Hessian square. No bound on the Hessian along
the whole segment is assumed or established.

Sections 14.6–14.7 also prove a positive full tangent-volume bound, including
its expectation under the prescribed independent Gaussian initialization.
The exact hidden-projection formula identifies an additional angle factor;
the full-volume estimate alone does not bound that factor from below.

### 14.1 The metric, potential and exact statement

Let \(\phi(z)=\arctan z\), and retain the forward equations

\[
 h^{(\ell)}=\phi(z^{(\ell)}),\qquad
 z^{(2)}=W^{(2)}h^{(1)},\qquad z^{(3)}=W^{(3)}h^{(2)},\qquad
 f_n=\frac{c^Th^{(3)}}n,\quad c=W^{(4)}.
\]

The parameter coordinate used for all Hessians in this section is

\[
 \vartheta=(z^{(1)},\sqrt n W^{(2)},\sqrt nW^{(3)})
       \in\mathbb R^{N_h},\qquad N_h=n+2n^2,\qquad
 \Theta=(\vartheta,c)\in\mathbb R^{N_h+n}.             \tag{14.1}
\]

Matrix coordinates have their ordinary Frobenius metric; vector coordinates
have their ordinary Euclidean metric. Define the scalar potential
\(\mathscr F(\vartheta,c)=c^Th^{(3)}(\vartheta)=nf_n\),
\(J=D_\vartheta h^{(3)}\), and its Euclidean gradient and Hessian

\[
 b=\nabla_\Theta\mathscr F=(J^Tc,h^{(3)}),\qquad
 \mathsf B=Db=\begin{pmatrix}A&J^T\\J&0\end{pmatrix},
 \qquad A=D_\vartheta^2\mathscr F.                    \tag{14.2}
\]

Feature time \(s\) is defined by \(\Theta'=b\), where a prime denotes
\(d/ds\). In stored variables this is exactly

\[
 (z^{(1)})'=\delta^{(1)},\qquad
 (W^{(\ell)})'=\frac1n\delta^{(\ell)}(h^{(\ell-1)})^T
       \quad(\ell=2,3),\qquad c'=h^{(3)}.             \tag{14.3}
\]

Indeed the derivatives of \(\mathscr F\) with respect to
\(\sqrt nW^{(\ell)}\) are
\(\delta^{(\ell)}(h^{(\ell-1)})^T/\sqrt n\).
Thus (14.2) retains every trained block and the actual transpose.
It also gives

\[
 f_n'=\frac{\|b\|_2^2}{n}\ge0.                       \tag{14.4}
\]

Physical full-loss GF on a segment where \(f_n<1\) is the same curve
with \(ds/dt=\alpha=2(1-f_n)=-2r_n\). The counterexample below constructs
such a segment; feature time is not a change to the optimizer.

**Reachable signed-Hessian obstruction.** Fix any \(\beta,\gamma>0\).
There is \(\varepsilon_0>0\), depending only on these two constants, such
that for every fixed \(0<\varepsilon\le\varepsilon_0\) and every even
\(n\ge4\) there is a deterministic initial state with \(c(0)=0\) and a
feature time \(\tau_n\) satisfying

\[
 \frac{\varepsilon}{\pi/2}\le\tau_n\le
       \frac{\varepsilon}{h_*},\qquad h_*>0,           \tag{14.5}
\]

where \(h_*\) is independent of width. All four primal norms specified
above stay bounded independently of width on \([0,\tau_n]\). At its
terminal state \(\|\mathsf B\|_{\mathrm{op}}\le C\), and there is a
unit vector \(U_n\in\mathbb R^{N_h+n}\) such that, for every fixed
\(\kappa\in\mathbb R\),

\[
 U_n^T(\mathsf B'-\kappa\mathsf B^2)U_n
      \ge c_0\varepsilon^2 n-C_\kappa,\qquad c_0>0.   \tag{14.6}
\]

Here \(\mathsf B'=D\mathsf B[b]\) is the material derivative along the
full feature field, not a coordinatewise activation derivative. Constants
in (14.5)–(14.6) do not depend on width. The analogous conclusion holds for
the Jacobian of the full physical vector field and its physical material
derivative, as proved in Section 14.5.

The proof first gives the complete trained-block Hessian identities. It
then constructs a terminal state with a positive bulk feature and a
concentrated two-coordinate middle response, and integrates backward a
uniformly controlled short distance until the common readout is zero.

### 14.2 Complete Hessian and material derivative

Write \(D_\ell=\operatorname{diag}(\phi'(z^{(\ell)}))\), and define

\[
 \delta^{(3)}=D_3c,\quad q^{(2)}=(W^{(3)})^T\delta^{(3)},\quad
 \delta^{(2)}=D_2q^{(2)},\quad q^{(1)}=(W^{(2)})^T\delta^{(2)},\quad
 \delta^{(1)}=D_1q^{(1)}.
\]

For a fixed hidden tangent \(u=(u_1,E_2,E_3)\), where the matrices vary the
scaled coordinates in (14.1), let

\[
 \begin{aligned}
 T_1u&=u_1,\\
 T_2u&=E_2h^{(1)}/\sqrt n+W^{(2)}D_1u_1,\\
 T_3u&=E_3h^{(2)}/\sqrt n+W^{(3)}D_2T_2u,\\
 S_2u&=E_2^T\delta^{(2)}/\sqrt n,\qquad
 S_3u=E_3^T\delta^{(3)}/\sqrt n.
 \end{aligned}                                        \tag{14.7}
\]

These are linear maps from \(\mathbb R^{N_h}\) to \(\mathbb R^n\), and
\(J=D_3T_3\). Set

\[
 M_1=\operatorname{diag}(\phi''(z^{(1)})q^{(1)}),\quad
 M_2=\operatorname{diag}(\phi''(z^{(2)})q^{(2)}),\quad
 M_3=\operatorname{diag}(\phi''(z^{(3)})c),
\]

where the products inside the diagonals are coordinatewise. The full hidden
Hessian is determined by the quadratic form

\[
 u^TAu=\sum_{\ell=1}^3(T_\ell u)^TM_\ell T_\ell u
       +2(S_2u)^TD_1T_1u+2(S_3u)^TD_2T_2u.            \tag{14.8}
\]

For verification, the first variation of \(z^{(\ell)}\) is \(T_\ell u\).
Along the straight parameter line \(\vartheta+\lambda u\), the second variations
of the two upper preactivations at \(\lambda=0\) are

\[
 \begin{aligned}
 \partial_\lambda^2 z^{(2)}
  &=2E_2D_1u_1/\sqrt n
      +W^{(2)}\{\phi''(z^{(1)})\odot u_1^{\odot2}\},\\
 \partial_\lambda^2 z^{(3)}
  &=2E_3D_2T_2u/\sqrt n
      +W^{(3)}\{\phi''(z^{(2)})\odot(T_2u)^{\odot2}
                     +D_2\partial_\lambda^2z^{(2)}\}.
 \end{aligned}
\]

Differentiating the final activation twice and pairing with \(c\) gives
(14.8), including both mixed matrix terms. Polarization determines the
symmetric operator \(A\) from this quadratic form.

For its material derivative put \(\nu_\ell=(z^{(\ell)})'\). Equations
(14.3) give the exact identities

\[
 \begin{aligned}
 \nu_1&=\delta^{(1)},\\
 \nu_2&=\frac{\|h^{(1)}\|_2^2}{n}\delta^{(2)}
                            +W^{(2)}D_1\nu_1,\\
 \nu_3&=\frac{\|h^{(2)}\|_2^2}{n}\delta^{(3)}
                            +W^{(3)}D_2\nu_2,\\
 D_\ell'&=\operatorname{diag}(\phi''(z^{(\ell)})\nu_\ell),\\
 (\delta^{(3)})'&=D_3'c+D_3h^{(3)},\\
 (q^{(2)})'&=((W^{(3)})')^T\delta^{(3)}
                              +(W^{(3)})^T(\delta^{(3)})',\\
 (\delta^{(2)})'&=D_2'q^{(2)}+D_2(q^{(2)})',\\
 (q^{(1)})'&=((W^{(2)})')^T\delta^{(2)}
                              +(W^{(2)})^T(\delta^{(2)})'.
 \end{aligned}                                        \tag{14.9}
\]

For the same fixed tangent \(u\), differentiating (14.7) gives

\[
 \begin{aligned}
 T_1'&=0,\\
 T_2'u&=E_2D_1\nu_1/\sqrt n
           +(W^{(2)})'D_1u_1+W^{(2)}D_1'u_1,\\
 T_3'u&=E_3D_2\nu_2/\sqrt n+(W^{(3)})'D_2T_2u
           +W^{(3)}D_2'T_2u+W^{(3)}D_2T_2'u,\\
 S_2'u&=E_2^T(\delta^{(2)})'/\sqrt n,\qquad
 S_3'u=E_3^T(\delta^{(3)})'/\sqrt n,\\
 J'&=D_3'T_3+D_3T_3'.
 \end{aligned}                                        \tag{14.10}
\]

The diagonal derivatives are

\[
 \begin{aligned}
 M_1'&=\operatorname{diag}\{
       \phi'''(z^{(1)})\nu_1q^{(1)}+\phi''(z^{(1)})(q^{(1)})'\},\\
 M_2'&=\operatorname{diag}\{
       \phi'''(z^{(2)})\nu_2q^{(2)}+\phi''(z^{(2)})(q^{(2)})'\},\\
 M_3'&=\operatorname{diag}\{
       \phi'''(z^{(3)})\nu_3c+\phi''(z^{(3)})h^{(3)}\}.
 \end{aligned}                                        \tag{14.11}
\]

Products in (14.11) are again coordinatewise. Differentiating (14.8),
with \(u\) fixed, is consequently the complete formula

\[
 \begin{aligned}
 u^TA'u={}&\sum_{\ell=1}^3\left\{
       2(T_\ell'u)^TM_\ell T_\ell u+(T_\ell u)^TM_\ell'T_\ell u\right\}\\
 &+2(S_2'u)^TD_1T_1u+2(S_2u)^TD_1'T_1u\\
 &+2(S_3'u)^TD_2T_2u+2(S_3u)^TD_2'T_2u
                              +2(S_3u)^TD_2T_2'u.
 \end{aligned}                                        \tag{14.12}
\]

There is no omitted derivative of a trained transpose or readout. In
particular \(\mathsf B'=\left(\begin{smallmatrix}A'&(J')^T\\J'&0\end{smallmatrix}\right)\),
and for a full tangent \(U=(u,\xi)\), with \(\xi\in\mathbb R^n\),

\[
 \begin{aligned}
 U^T(\mathsf B'-\kappa\mathsf B^2)U
  =u^TA'u+2\xi^TJ'u
       -\kappa\left(\|Au+J^T\xi\|_2^2+\|Ju\|_2^2\right).
 \end{aligned}                                        \tag{14.13}
\]

### 14.3 The terminal state and its positive Rayleigh quotient

Let \(\mathbf1\in\mathbb R^n\) be the all-ones vector, and choose a
balanced unit vector \(e\) with entries \(\pm1/\sqrt n\), so that
\(e^T\mathbf1=0\). Let \(e_1,e_2\) be the first two coordinate vectors.
Define

\[
 a_0=\pi/4,\quad \mu=a_0^2<1,\quad \rho=(n-2)/n,\quad
 w=e_1+e_2,\quad v=e_1-2e_2,\quad g=\mathbf1-e_1-e_2.
\]

For fixed \(\beta,\gamma,\varepsilon>0\), prescribe the terminal state

\[
 \begin{aligned}
 z^{(1)}&=\mathbf1,\qquad c=\varepsilon\mathbf1,\\
 W^{(2)}&=2we^T+\frac{\beta}{a_0n}g\mathbf1^T,\\
 W^{(3)}&=\frac{\mathbf1v^T}{\sqrt n}
                               +\frac\gamma n\mathbf1g^T.
 \end{aligned}                                        \tag{14.14}
\]

The ranges and domains of the two summands of \(W^{(2)}\) are orthogonal.
Also \(v^Tg=0\), \(\|v\|_2^2=5\), and \(\|g\|_2^2=n\rho\). Hence

\[
 \|W^{(2)}\|_{\mathrm{op}}
       =\max\{2\sqrt2,\beta\sqrt\rho/a_0\},\qquad
 \|W^{(3)}\|_{\mathrm{op}}=\sqrt{5+\gamma^2\rho},
\]

while \(\|z^{(1)}\|_2/\sqrt n=1\) and \(\|c\|_2/\sqrt n=\varepsilon\).
Introduce the following scalars, used only in this construction:

\[
 \begin{aligned}
 t_\beta&=\phi(\beta),\quad d_\beta=\phi'(\beta),\quad
 Z=\gamma\rho t_\beta,\quad H=\phi(Z),\quad D=\phi'(Z),
       \quad k=\varepsilon D,\\
 \Lambda&=\beta\gamma d_\beta\rho/a_0,\\
 R_\beta&=\gamma d_\beta\left(\mu+
                                  \frac{\beta^2\rho}{4a_0^2}\right),\\
 Q_\beta&=\rho t_\beta^2+5\mu+1+\gamma\rho d_\beta R_\beta.
 \end{aligned}
\]

The complete forward and backward quantities at (14.14) are

\[
 \begin{aligned}
 h^{(1)}&=a_0\mathbf1,\quad z^{(2)}=\beta g,\quad
 h^{(2)}=t_\beta g,\quad z^{(3)}=Z\mathbf1,\quad h^{(3)}=H\mathbf1,\\
 f_n&=\varepsilon H,\qquad \delta^{(3)}=k\mathbf1,\\
 q^{(2)}&=\sqrt n k v+\gamma k g,\qquad
 \delta^{(2)}=\sqrt n k v+\gamma d_\beta k g,\\
 q^{(1)}&=-2\sqrt n k e+\Lambda k\mathbf1,\\
 \nu_1&=-\sqrt n k e+(\Lambda k/2)\mathbf1,\\
 \nu_2&=\sqrt n k(\mu v-w)+kR_\beta g,\qquad
 \nu_3=kQ_\beta\mathbf1.
 \end{aligned}                                        \tag{14.15}
\]

These identities follow by matrix multiplication and (14.9). In particular
\(D_1=I/2\), and

\[
 \nu_2=\left\{\mu I+W^{(2)}D_1^2(W^{(2)})^T\right\}\delta^{(2)}.
\]

Its first two coordinates see the block \(\mu I+ww^T\); the bulk cross
terms vanish by the orthogonalities just stated. This gives its rare part
\(\sqrt n k(\mu v-w)\). The bulk term is
\(k(\mu\gamma d_\beta+\beta\Lambda/(4a_0))g=kR_\beta g\).
Substituting into \(\nu_3\) gives \(Q_\beta\), because
\(v^T(\mu v-w)=5\mu+1\).

The Hessian itself is uniformly bounded at this state. Indeed,
\(\phi''(1)=-1/2\), \(\phi''(0)=0\), and (14.15) give

\[
 \|M_1\|_{\mathrm{op}}\le |k|(1+\Lambda/2),\quad
 \|M_2\|_{\mathrm{op}}\le |\phi''(\beta)|\gamma|k|,\quad
 \|M_3\|_{\mathrm{op}}\le\varepsilon|\phi''(Z)|.       \tag{14.16}
\]

For \(P=\pi/2\), the bounds \(|\phi|\le P\), \(|\phi'|\le1\) imply
from (14.7) that

\[
 \|T_1\|_{\mathrm{op}}\le1,\quad
 \|T_2\|_{\mathrm{op}}\le P+\|W^{(2)}\|_{\mathrm{op}},\quad
 \|T_3\|_{\mathrm{op}}
        \le P+\|W^{(3)}\|_{\mathrm{op}}\|T_2\|_{\mathrm{op}},
 \quad\|J\|_{\mathrm{op}}\le\|T_3\|_{\mathrm{op}}.
\]

Also
\(\|S_2\|_{\mathrm{op}}\le\|\delta^{(2)}\|_2/\sqrt n
\le\|W^{(3)}\|_{\mathrm{op}}\varepsilon\) and
\(\|S_3\|_{\mathrm{op}}\le\varepsilon\).
For a symmetric matrix \(A\), its operator norm is the supremum of
\(|u^TAu|\) over unit \(u\). Thus (14.8) and (14.16) bound \(A\), and
(14.2) bounds \(\mathsf B\), independently of width. Furthermore,

\[
 \frac{\|b\|_2^2}{n}\le
       \|J\|_{\mathrm{op}}^2\varepsilon^2+P^2.         \tag{14.17}
\]

Now take the unit hidden tangent and full tangent

\[
 u_1=0,\qquad E_2=e_1\mathbf1^T/\sqrt n,\qquad E_3=0,
 \qquad U_n=(u,0).
\]

Its matrix Frobenius norm is one. Equations (14.7), (14.10), and balance
of \(e\) give

\[
 T_1u=0,\quad T_2u=a_0e_1,\quad T_2'u=(\Lambda k/4)e_1,
 \quad T_3u=\frac{a_0}{\sqrt n}\mathbf1,
 \quad T_3'u=\frac{\Lambda k}{4\sqrt n}\mathbf1.       \tag{14.18}
\]

For the last derivative, the trained term \((W^{(3)})'D_2T_2u\) vanishes
because \(h^{(2)}=t_\beta g\) has first coordinate zero. The term
\(W^{(3)}D_2'T_2u\) vanishes because \(\phi''(z_1^{(2)})=\phi''(0)=0\).
The remaining \(W^{(3)}D_2T_2'u\) gives the displayed value. Thus the
third matrix has been differentiated, not frozen.

In (14.12), the bottom terms and every \(S_2\) term contain \(T_1u=0\).
Both \(S_3u\) and \(S_3'u\) vanish since \(E_3=0\). The cross term with
\(T_2'\) and \(M_2\) vanishes since \(M_2e_1=0\). Finally,
\(\phi'''(0)=-2\) and (14.11), (14.15) give

\[
 (M_2')_{11}=2(1-\mu)n k^2,\qquad
 M_3'=\{\phi'''(Z)\varepsilon kQ_\beta+\phi''(Z)H\}I.
\]

Substitution of all remaining terms yields the exact full-field identity

\[
 \begin{aligned}
 U_n^T\mathsf B'U_n
   ={}&2\mu(1-\mu)n k^2
      +\mu\{\phi'''(Z)\varepsilon kQ_\beta+\phi''(Z)H\}\\
      &+(a_0\Lambda/2)\varepsilon k\phi''(Z).
 \end{aligned}                                        \tag{14.19}
\]

All terms after the first are bounded independently of width, since
\(\rho\in[1/2,1)\) and \(\beta,\gamma,\varepsilon\) are fixed. Moreover

\[
 D\ge D_*:=\frac1{1+\{\gamma\phi(\beta)\}^2}>0.
\]

The Hessian bound gives
\(U_n^T\mathsf B^2U_n=\|\mathsf BU_n\|_2^2\le C^2\).
Equation (14.6) follows from (14.19) with
\(c_0=2\mu(1-\mu)D_*^2>0\), for every fixed real \(\kappa\).

This also explains why a scalar arctangent sign is insufficient. Direct
substitution of
\(\phi'=1/(1+z^2)\), \(\phi''=-2z/(1+z^2)^2\), and
\(\phi'''=(6z^2-2)/(1+z^2)^3\) gives the negative scalar identity
\(\phi'''\phi'-(3/2)(\phi'')^2=-2(\phi')^4\).
But the positive-semidefinite middle mobility in (14.15) has off-diagonal
entries. Here \(\nu_{2,1}q_1^{(2)}=(\mu-1)nk^2<0\). At the same
coordinate \(M_2\) vanishes, while \(M_2'\) is positive of order \(n\).
The complete calculation (14.19) shows that the other trained blocks and
\(\mathsf B^2\) do not supply a compensating order-\(n\) term.

### 14.4 Uniform backward passage to exactly zero readout

It remains to make (14.14) a reached state. Its third-matrix rows are
identical and its readout coordinates are equal. The subspace

\[
 W^{(3)}=\mathbf1p^T,\qquad c=\chi\mathbf1
\]

is invariant in both feature-time directions: with
\(y=p^Th^{(2)}\), equations (14.3) become

\[
 z^{(3)}=y\mathbf1,\qquad
 (W^{(3)})'=\frac{\chi\phi'(y)}n\mathbf1(h^{(2)})^T,
 \qquad \chi'=\phi(y).                                \tag{14.20}
\]

The full finite vector field is smooth. Local uniqueness ensures that its
solutions starting in this invariant subspace agree with the restricted
solutions in either time direction.

Choose constants independent of width:

\[
 \begin{aligned}
 K_{2,0}&=\max\{2\sqrt2,\beta/a_0\},\quad
 K_{3,0}=\sqrt{5+\gamma^2},\quad
 N_2=K_{2,0}+1,\quad N_3=K_{3,0}+1,\\
 K&=P^2+N_3^2(P^2+N_2^2),\quad
 y_*=\gamma\phi(\beta)/2,\quad h_*=\phi(y_*/2)>0,\\
 \varepsilon_0&=\min\left\{1,\frac1{4P},
       \sqrt{\frac{h_*}{4PN_3}},
       \sqrt{\frac{y_*h_*}{4K}}\right\},\qquad P=\pi/2.
 \end{aligned}                                        \tag{14.21}
\]

On an interval where \(\|W^{(2)}\|_{\mathrm{op}}\le N_2\),
\(\|W^{(3)}\|_{\mathrm{op}}\le N_3\), and \(0\le\chi\le\varepsilon\),
the exact forward/backward formulas give

\[
 \begin{aligned}
 \|\delta^{(3)}\|_2/\sqrt n&\le\chi,&
 \|\delta^{(2)}\|_2/\sqrt n&\le N_3\chi,&
 \|\delta^{(1)}\|_2/\sqrt n&\le N_2N_3\chi,\\
 \|(W^{(3)})'\|_{\mathrm{op}}&\le P\chi,&
 \|(W^{(2)})'\|_{\mathrm{op}}&\le PN_3\chi,\\
 \|\nu_2\|_2/\sqrt n&\le(P^2+N_2^2)N_3\chi,&
 |y'|=\|\nu_3\|_2/\sqrt n&\le K\chi.
 \end{aligned}                                        \tag{14.22}
\]

The matrix inequalities follow by the rank-one norm formula. For \(\nu_2\)
and \(\nu_3\), substitute the first line and \(\|h^{(\ell)}\|_2/\sqrt n\le P\)
into (14.9). The last equality holds since all coordinates of \(z^{(3)}\)
are the same. No Hessian bound is used in (14.22).

Start at (14.14), assign it feature time zero temporarily, and integrate
backward with elapsed time \(\sigma\ge0\). Before the first zero of \(\chi\),
consider the conditions

\[
 0<\chi\le\varepsilon,\quad y\ge y_*/2,\quad
 \|W^{(2)}\|_{\mathrm{op}}<N_2,\quad
 \|W^{(3)}\|_{\mathrm{op}}<N_3,\quad \sigma\le\varepsilon/h_*.
\]

Initially \(y=Z\ge y_*\), since \(\rho\ge1/2\), and both matrix bounds
have margin at least one. While these conditions hold, (14.20) gives
\(d\chi/d\sigma=-\phi(y)\le-h_*\), so \(\chi\) cannot cross its upper
boundary. Integrating (14.22) and using (14.21) gives

\[
 \begin{aligned}
 \|W^{(3)}(\sigma)-W^{(3)}(0)\|_{\mathrm{op}}
       &\le P\varepsilon^2/h_*\le1/4,\\
 \|W^{(2)}(\sigma)-W^{(2)}(0)\|_{\mathrm{op}}
       &\le PN_3\varepsilon^2/h_*\le1/4,\\
 |y(\sigma)-y(0)|&\le K\varepsilon^2/h_*\le y_*/4,\\
 \|z^{(1)}(\sigma)-z^{(1)}(0)\|_2/\sqrt n
       &\le N_2N_3\varepsilon^2/h_*.
 \end{aligned}                                        \tag{14.23}
\]

Thus neither a matrix boundary nor the lower \(y\) boundary can be reached.
For each fixed width the same bounds preclude finite-time escape in all
parameter coordinates: the vector Euclidean norms are bounded, and a matrix
operator bound implies a Frobenius bound at most \(\sqrt n\) times as
large. A smooth finite-dimensional ODE extends while its state remains in
a bounded set, because on a slightly larger closed ball its field is bounded
and Lipschitz, so the integral equation has a local continuation at any
finite limiting endpoint. Hence the backward solution extends until
\(\chi=0\) or \(\sigma=\varepsilon/h_*\). The latter cannot occur first with
\(\chi>0\), since integration of \(d\chi/d\sigma\le-h_*\) would give
\(\chi\le0\) there. The first zero occurs at some
\(\tau_n\le\varepsilon/h_*\). Since \(|d\chi/d\sigma|\le P\), it also
satisfies \(\tau_n\ge\varepsilon/P\).

Declare this zero-readout endpoint to be feature time zero and run the
same smooth solution forward. It reaches (14.14) at \(\tau_n\).
Equations (14.22)–(14.23) prove the claimed whole-segment primal bounds.
The initial hidden weights are obtained by this deterministic inverse
flow; no distributional identification with independent Gaussian weights
is made.

### 14.5 Physical time and the exact scope of the obstruction

By (14.4), the predictor increases from zero to \(\varepsilon H\) along
the constructed segment. The choice (14.21) gives

\[
 0\le f_n\le\varepsilon H\le\varepsilon P\le1/4.
\]

Therefore \(\alpha=2(1-f_n)\in[3/2,2]\), and the same curve is a full
physical-loss GF trajectory with terminal time \(t_n\) satisfying
\(\tau_n/2\le t_n\le2\tau_n/3\). Both feature and physical terminal
times lie in fixed positive compact intervals when \(\varepsilon\) is
fixed, but need not be identical at different widths.

The physical vector field in coordinates (14.1) is \(\mathcal V=\alpha b\).
Since \(\nabla_\Theta f_n=b/n\), its complete Jacobian is the symmetric
matrix

\[
 \mathsf C=D\mathcal V=\alpha\mathsf B-\frac2n bb^T.
\]

A dot now denotes the physical material derivative. Using
\(\dot\alpha=-2\alpha\|b\|_2^2/n\),
\(\dot b=\alpha\mathsf Bb\), and \(\dot{\mathsf B}=\alpha\mathsf B'\),
exact differentiation gives

\[
 \dot{\mathsf C}=\alpha^2\mathsf B'
   -\frac{2\alpha}{n}\|b\|_2^2\mathsf B
   -\frac{2\alpha}{n}\{(\mathsf Bb)b^T+b(\mathsf Bb)^T\}. \tag{14.24}
\]

At the terminal state, \(\|\mathsf B\|_{\mathrm{op}}\) and
\(\|b\|_2/\sqrt n\) are bounded by (14.16)–(14.17). The two correction
terms in (14.24) thus have bounded operator norm. The same holds for
\(\mathsf C\) and \(\mathsf C^2\). Applying (14.19) to the same unit
vector and using \(\alpha\ge3/2\) gives, for every fixed real \(\kappa\),

\[
 U_n^T(\dot{\mathsf C}-\kappa\mathsf C^2)U_n
    \ge\frac94c_0\varepsilon^2 n-C_\kappa'
      \longrightarrow+\infty.                         \tag{14.25}
\]

This disproves a width-independent upper bound for either signed matrix
in (14.6) or (14.25) inferred only from the stated primal bounds, even
on trajectories begun at exactly zero readout. The residual-clock terms
are fully included. It does not disprove a bound that assumes additional
Hessian-history or response information, a Gaussian-typical estimate, or
an integrated-in-time signed estimate. No probability lower bound under
the prescribed independent Gaussian initialization, no fixed-time
convergence failure, and no failure of the nonlinear population limit
are consequences of this deterministic construction.

### 14.6 Positive intrinsic-volume bounds for the full trained flow

There is also a positive uniform statement for transported tangent volumes.
It concerns the full Hessian \(\mathsf B\), rather than its signed material
derivative. The same arctangent architecture, coordinates (14.1), potential
and full-loss clock are used throughout. The deterministic bounds first allow
arbitrary finite initial parameters. The expectation conclusions then use the
specified independent Gaussian initialization

\[
 z_j^{(1)}(0)\sim N(0,1),\quad
 W_{ij}^{(2)}(0),W_{ij}^{(3)}(0)\sim N(0,1/n),\quad
 c_i(0)\sim N(0,n^{-2}).                              \tag{14.26}
\]

Here the stored readout is small, unlike the deterministic terminal witness
in Section 14.3. No Gaussian hypothesis is imposed on the evolved state.

We prove global existence in both feature-time directions and give an
explicit polynomial bound

\[
 \sup_{|s|\le S}\|\mathsf B(s)\|_*
      \le n\,\mathcal P_S(M,R_0),\qquad
 M=\max_{\ell=2,3}\|W^{(\ell)}(0)\|_{\mathrm{op}},\quad
 R_0=\|c(0)\|_2/\sqrt n,                              \tag{14.27}
\]

where \(\|\cdot\|_*\) is the nuclear norm, the sum of singular values.
For every full-column-rank tangent response
\(\mathcal T(s)\in\mathbb R^{(N_h+n)\times q}\),
\(1\le q\le N_h+n\), satisfying \(\mathcal T'=\mathsf B\mathcal T\),
let

\[
 V_{\mathcal T}(s)=\sqrt{\det(\mathcal T(s)^T\mathcal T(s))}.
\]

It remains positive, and simultaneously for every such initial tangent plane
and every \(|s|\le S\),

\[
 \left|\log\frac{V_{\mathcal T}(s)}{V_{\mathcal T}(0)}\right|
       \le n|s|\mathcal P_S(M,R_0).                   \tag{14.28}
\]

Under (14.26), this implies
\(\mathbb E\sup_{|s|\le S}|\log(V_{\mathcal T}(s)/V_{\mathcal T}(0))|
\le C_S n\). The analogous full physical tangent response has expected
absolute log-volume change at most \(C_Tn\), uniformly over \([0,T]\).
The constants are independent of width and tangent dimension. Initial
tangent planes may depend measurably on the initial parameters, since the
underlying bounds are pathwise and simultaneous.

**Primal bounds and complete finite flow.** Put \(P=\pi/2\). For
\(u\ge0\), define the nonnegative polynomials

\[
 \begin{aligned}
 R(u)&=R_0+Pu,\\
 K_3(u)&=M+PR_0u+P^2u^2/2,\\
 K_2(u)&=M+P\int_0^u K_3(v)R(v)\,dv.
 \end{aligned}                                        \tag{14.29}
\]

The integral in the last line is a polynomial in \(u,M,R_0\), since its
integrand is a product of the two displayed polynomials. For either sign
of feature time, integrating (14.3) with absolute values gives

\[
 \|c(s)\|_2/\sqrt n\le R(|s|),\qquad
 \|W^{(3)}(s)\|_{\mathrm{op}}\le K_3(|s|),\qquad
 \|W^{(2)}(s)\|_{\mathrm{op}}\le K_2(|s|).             \tag{14.30}
\]

Indeed \(\|c'\|_2/\sqrt n\le P\),
\(\|(W^{(3)})'\|_{\mathrm{op}}\le P\|c\|_2/\sqrt n\), and
\(\|(W^{(2)})'\|_{\mathrm{op}}
\le P\|W^{(3)}\|_{\mathrm{op}}\|c\|_2/\sqrt n\).
These follow from \(|\phi'|\le1\) and the rank-one norm formula. Likewise,

\[
 \frac{\|z^{(1)}(s)\|_2}{\sqrt n}
 \le\frac{\|z^{(1)}(0)\|_2}{\sqrt n}
       +\int_0^{|s|}K_2(v)K_3(v)R(v)\,dv.             \tag{14.31}
\]

At each fixed width these estimates bound every Euclidean parameter
coordinate on every bounded feature-time interval. The smooth vector field
therefore continues in both directions by the bounded-state argument used
in Section 14.4. Denote its complete flow by \(\Phi_s\). Uniqueness gives
\(\Phi_{-s}\Phi_s=I\).

Smooth dependence on initial data follows by differentiating the integral
equation on bounded parameter sets: difference quotients satisfy the linear
variational integral equation plus a remainder tending to zero uniformly,
because the field has a continuous derivative on the relevant compact set.
The integral inequality \(e(t)\le a+L\int_0^t e(v)\,dv\) gives
\(e(t)\le ae^{Lt}\), by iteration of its integral operator, and removes
that remainder. Higher derivatives follow by differentiating the same
finite-dimensional equation repeatedly. Thus \(\Phi_s\) is smooth, with
invertible full derivative. One may check the latter directly: if
\(Y'=\mathsf BY\), \(Y(0)=I\), and \(Z'=-Z\mathsf B\), \(Z(0)=I\),
then \((ZY)'=0\), so \(ZY=I\). All these linear equations have continuous
coefficients on the bounded trajectory interval.

**Elementary nuclear inequalities.** For a finite matrix
\(H=\sum_i\sigma_i u_iv_i^T\) in a singular-value decomposition,

\[
 |\operatorname{Tr}(Q^TH)|\le\|Q\|_{\mathrm{op}}\sum_i\sigma_i.
\]

Taking \(Q=\sum_i u_iv_i^T\) shows that the supremum over
\(\|Q\|_{\mathrm{op}}\le1\) equals \(\|H\|_*\). This dual formula
proves the nuclear triangle inequality. It also gives
\(\|H\|_*\le\operatorname{rank}(H)\|H\|_{\mathrm{op}}\).
A rank-one matrix \(uv^T\) has nuclear norm \(\|u\|_2\|v\|_2\), so
decomposing a diagonal matrix into coordinate rank-one matrices gives

\[
 \|T^T\operatorname{diag}(d)T\|_*
     \le\|T\|_{\mathrm{op}}^2\sum_i|d_i|.             \tag{14.32}
\]

For any orthogonal projector \(\Pi\), the trace inequality also gives
\(|\operatorname{Tr}(\Pi H)|\le\|H\|_*\).

To apply these facts to the complete Hessian (14.8), fix \(S\ge0\) and
write \(R=R(S)\), \(K_2=K_2(S)\), \(K_3=K_3(S)\). Let

\[
 t_2=P+K_2,\qquad t_3=P+K_3t_2.
\]

On \(|s|\le S\), (14.7) gives
\(\|T_1\|_{\mathrm{op}}\le1\),
\(\|T_2\|_{\mathrm{op}}\le t_2\),
\(\|T_3\|_{\mathrm{op}},\|J\|_{\mathrm{op}}\le t_3\),
\(\|S_2\|_{\mathrm{op}}\le K_3R\), and
\(\|S_3\|_{\mathrm{op}}\le R\).
The backward fields satisfy

\[
 \|q^{(1)}\|_2/\sqrt n\le K_2K_3R,\qquad
 \|q^{(2)}\|_2/\sqrt n\le K_3R.
\]

Since \(|\phi''|\le2\), the sums of absolute diagonal entries of
\(M_1,M_2,M_3\) are bounded by
\(2nK_2K_3R,2nK_3R,2nR\), respectively. This uses only
\(\sum_i|v_i|\le\sqrt n\|v\|_2\), not a maximum coordinate bound.
Each symmetric mixed operator in (14.8) has rank at most \(2n\) and
operator norm at most twice the product of its two map norms. Thus

\[
 \|A\|_*\le2nR(K_2K_3+t_2^2K_3+t_3^2)
                       +4nR(K_3+t_2).
\]

The off-diagonal block
\(\left(\begin{smallmatrix}0&J^T\\J&0\end{smallmatrix}\right)\)
has rank at most \(2n\) and operator norm at most \(t_3\). Adding its
nuclear norm to that of \(\operatorname{diag}(A,0)\) proves (14.27) with

\[
 \mathcal P_S(M,R_0)
 =2R(K_2K_3+t_2^2K_3+t_3^2)+4R(K_3+t_2)+2t_3.        \tag{14.33}
\]

This is an explicit polynomial with nonnegative coefficients in \(S,M,R_0\).
In particular \(|\operatorname{Tr}\mathsf B|\le n\mathcal P_S\), while
no width-independent operator bound on \(\mathsf B\) is inferred.
The same estimates yield the additional useful bound

\[
 \frac{\|b\|_2^2}{n}\le\mathcal Q_S(M,R_0)
           :=t_3^2R^2+P^2.                            \tag{14.34}
\]

**Tangent volumes.** Write \(\mathcal T(s)=Y(s)\mathcal T(0)\), using
the invertible full derivative just proved. Thus its Gram matrix is positive
definite for all finite times. For any differentiable invertible matrix
\(G(s)\), multilinearity of the determinant gives
\(\det(I+hH)=1+h\operatorname{Tr}H+O(h^2)\), and consequently
\((\log\det G)'=\operatorname{Tr}(G^{-1}G')\) when \(G\) is positive
definite. Applying this identity to \(\mathcal T^T\mathcal T\), using
symmetry of \(\mathsf B\), gives

\[
 \frac{d}{ds}\log V_{\mathcal T}
   =\operatorname{Tr}(\Pi_{\mathcal T}\mathsf B),\qquad
 \Pi_{\mathcal T}=\mathcal T(\mathcal T^T\mathcal T)^{-1}\mathcal T^T.
                                                               \tag{14.35}
\]

The displayed \(\Pi_{\mathcal T}\) is the orthogonal projector onto the
current tangent range: it is symmetric, squares to itself, and fixes that
range. The nuclear trace bound therefore implies
\(|(\log V_{\mathcal T})'|\le n\mathcal P_S\). Integration in either
time direction proves (14.28).

**Gaussian expectations.** We supply the moment estimates needed to take
expectations of the polynomial in (14.33). A maximal \(1/4\)-separated
set on the unit sphere of \(\mathbb R^n\) is a \(1/4\)-net of at most
\(9^n\) points: disjoint radius-\(1/8\) balls about its points lie in the
radius-\(9/8\) ball, and comparison of volumes gives the cardinality.
For a matrix \(W\) with independent \(N(0,1/n)\) entries, each fixed
bilinear form \(y^TWx\) at unit vectors has law \(N(0,1/n)\). Completing
the square gives \(\mathbb E e^{t y^TWx}=e^{t^2/(2n)}\); exponential
Markov with \(t=na\) for each sign gives
\(\Pr\{|y^TWx|>a\}\le2e^{-na^2/2}\). Approximating a maximizing pair
of vectors by the two nets gives
\(\|W\|_{\mathrm{op}}\le2\max_{x,y\text{ in the net}}|y^TWx|\).
The union bound therefore yields

\[
 \Pr\{\|W\|_{\mathrm{op}}>u\}
     \le2\,81^n e^{-nu^2/8}\le2e^{-u^2/16}
       \qquad(u\ge10).                               \tag{14.36}
\]

For the last inequality, \(\log81<5\le u^2/16\) and \(n\ge1\).
Integrating this tail gives, for every fixed \(p>0\),

\[
 \mathbb E\|W\|_{\mathrm{op}}^p
    \le10^p+2p\int_{10}^\infty u^{p-1}e^{-u^2/16}\,du<\infty,
\]

uniformly in width. A union bound treats the maximum of the two initial
hidden norms \(M\).

For independent standard Gaussians \(g_i\), put
\(R_n^{\mathrm{std}}=(n^{-1}\sum_i g_i^2)^{1/2}\). If \(p\ge2\), convexity gives
\(\mathbb E(R_n^{\mathrm{std}})^p\le\mathbb E|g_1|^p\); if \(0<p<2\), concavity gives
\(\mathbb E(R_n^{\mathrm{std}})^p\le\{\mathbb E(R_n^{\mathrm{std}})^2\}^{p/2}=1\).
These Gaussian moments
are finite by their density integral. Under (14.26),
\(R_0\) has law \(R_n^{\mathrm{std}}/n\), so

\[
 \mathbb ER_0^p\le C_pn^{-p},\qquad
 \mathbb E(\|z^{(1)}(0)\|_2/\sqrt n)^p\le C_p.       \tag{14.37}
\]

Hölder's inequality bounds every mixed monomial in \(M,R_0\) by their
higher moments; hence \(\mathbb E\mathcal P_S(M,R_0)\le C_S\).
Equations (14.28) and (14.33) prove the stated expected intrinsic-volume
bound, also with the supremum over \(|s|\le S\).

**Forward physical time.** The argument must retain the residual clock even
when the initial residual has either sign. A local physical trajectory has
\(\dot\Theta=\alpha b\), \(\alpha=2(1-f_n)\), and

\[
 \dot r_n=-2r_n\frac{\|b\|_2^2}{n}.
\]

Solving this scalar linear equation along the existing trajectory gives
\(|r_n(t)|\le|r_n(0)|\le1+PR_0\). The physical path therefore equals
\(\Phi_{s(t)}(\Theta(0))\), where its signed feature clock satisfies

\[
 |\alpha(t)|\le2(1+PR_0),\qquad
 \int_0^T|\alpha(t)|\,dt\le S_T:=2T(1+PR_0).         \tag{14.38}
\]

The equality of paths follows first locally by the chain rule and uniqueness.
The complete feature flow and (14.30)–(14.31) keep the physical state bounded
on each finite forward interval, extending the physical solution and this
identity to all \(t\ge0\). If \(r_n(0)=0\), it is the stationary solution.
Backward physical completeness is not needed.

For a derivative taken at fixed physical time, the full Jacobian is
\(\mathsf C=\alpha\mathsf B-2bb^T/n\), as in Section 14.5. The rank-one
nuclear norm is exactly \(2\|b\|_2^2/n\), so (14.27), (14.34) and
(14.38) give

\[
 \sup_{0\le t\le T}\|\mathsf C(t)\|_*
    \le n\widetilde{\mathcal P}_T(M,R_0),\quad
 \widetilde{\mathcal P}_T
    =2(1+PR_0)\mathcal P_{S_T}+2\mathcal Q_{S_T}.      \tag{14.39}
\]

We used \(n\ge1\) for the last term. Since \(S_T\) is itself polynomial
in \(T,R_0\), the right side is a polynomial envelope of the same type.
The full physical variational equation is
\(\dot{\mathcal T}=\mathsf C\mathcal T\); its fundamental matrix is
invertible by the same inverse linear equation used above. Repeating
(14.35) with \(\mathsf C\) yields

\[
 \sup_{0\le t\le T}
 \left|\log\frac{V_{\mathcal T}(t)}{V_{\mathcal T}(0)}\right|
    \le nT\widetilde{\mathcal P}_T(M,R_0),\qquad
 \mathbb E\sup_{0\le t\le T}
 \left|\log\frac{V_{\mathcal T}(t)}{V_{\mathcal T}(0)}\right|
    \le C_Tn.                                         \tag{14.40}
\]

The expectation uses the original full Gaussian law (14.26), without
conditioning on a norm event. These are intrinsic volumes of full transported
tangent subspaces. They control neither the largest response singular value
by a width-independent constant nor the volume of a specified projection.

### 14.7 Exact hidden projection and its additional angle factor

Fix the initial readout \(c_0\), and differentiate the feature flow with
respect to its hidden initial coordinate \(\vartheta_0\). Let

\[
 \mathsf P=D_{\vartheta_0}\vartheta_s\in\mathbb R^{N_h\times N_h},
 \qquad \mathsf R=D_{\vartheta_0}c_s\in\mathbb R^{n\times N_h},
 \qquad
 \mathcal T=\begin{pmatrix}\mathsf P\\\mathsf R\end{pmatrix},
 \qquad \mathcal T(0)=\begin{pmatrix}I_{N_h}\\0\end{pmatrix}.
\]

The full derivative is invertible, so \(\mathcal T\) has full column rank
and \(V_{\mathcal T}>0\), with \(V_{\mathcal T}(0)=1\).
The positive-definite Gram matrix has a unique positive-definite square root,
obtained by diagonalizing it. The matrix

\[
 Q=\mathcal T(\mathcal T^T\mathcal T)^{-1/2}
       =\begin{pmatrix}Q_H\\Q_C\end{pmatrix}
\]

has orthonormal columns. In particular,
\(Q_H^TQ_H=I_{N_h}-Q_C^TQ_C\). Let \(a_1,\ldots,a_n\in[0,1]\) be
the singular values of the \(n\)-by-\(N_h\) matrix \(Q_C\), including
zeros. The upper bound one follows from \(Q_C^TQ_C\le I_{N_h}\).
Since
\(\mathsf P=Q_H(\mathcal T^T\mathcal T)^{1/2}\), taking determinants
of the Gram matrices gives exactly

\[
 |\det\mathsf P|
   =V_{\mathcal T}\sqrt{\det(I_n-Q_CQ_C^T)}
   =V_{\mathcal T}\prod_{j=1}^n\sqrt{1-a_j^2}.         \tag{14.41}
\]

This identity includes singular \(\mathsf P\): both sides then vanish.
To justify changing determinant dimension, a singular-value decomposition
of \(Q_C\) shows that \(Q_C^TQ_C\) and \(Q_CQ_C^T\) have the same
nonzero eigenvalues, with only extra zeros in the larger matrix. Thus the
determinants of their identity-minus forms agree.

Equation (14.41) places all loss of projected volume in at most \(n\)
directions, even though the hidden parameter dimension is \(N_h=n+2n^2\).
It gives \(|\det\mathsf P|\le V_{\mathcal T}\). The intrinsic bound
(14.28) supplies no estimate on how close the \(a_j\) are to one, and
therefore supplies no lower bound for the projected determinant.

On any interval where \(\mathsf P\) is invertible, define its readout
slope \(\mathsf K=\mathsf R\mathsf P^{-1}\). Factoring
\(\mathcal T=\left(\begin{smallmatrix}I\\\mathsf K\end{smallmatrix}\right)\mathsf P\)
and using the same singular-value argument gives

\[
 \log|\det\mathsf P|
     =\log V_{\mathcal T}
       -\frac12\log\det(I_n+\mathsf K\mathsf K^T).    \tag{14.42}
\]

The subtracted quantity is nonnegative. The full block variational equation
from (14.2) is

\[
 \mathsf P'=A\mathsf P+J^T\mathsf R,\qquad
 \mathsf R'=J\mathsf P.
\]

Differentiating \(\mathsf K=\mathsf R\mathsf P^{-1}\), with
\((\mathsf P^{-1})'=-\mathsf P^{-1}\mathsf P'\mathsf P^{-1}\), proves
its exact Riccati equation

\[
 \mathsf K'=J-\mathsf K A-\mathsf KJ^T\mathsf K.       \tag{14.43}
\]

This is a derivative at one fixed initial readout. It is not a conditional
covariance or the derivative of a conditional mean after averaging over
initial readouts.

The determinant identities (14.41)–(14.42) apply as well at fixed physical
time to its full derivative and the same hidden initial plane. The feature
Riccati equation (14.43) must then be replaced by its physical block equation.
Writing \(\mathsf C\) in hidden/readout blocks, it is

\[
 \dot{\mathsf K}=\mathsf C_{CH}+\mathsf C_{CC}\mathsf K
      -\mathsf K\mathsf C_{HH}-\mathsf K\mathsf C_{HC}\mathsf K,
\]

on each interval where \(\mathsf P\) is invertible. The full expression
\(\mathsf C=\alpha\mathsf B-2bb^T/n\) specifies every block, including
the clock terms. No feature-time derivative is substituted at fixed physical
time.

These exact identities and the positive intrinsic-volume bounds do not
establish hidden-projection nonsingularity, a projected lower-volume or
entropy bound, a response covariance estimate, or control of an adaptive
Gaussian query. Those require estimates beyond the full tangent-volume
bound proved here.


## Further finite response and physical controls

The following fragments S, I, C and E have separate model and clock
contracts, and locally prefixed equation numbers. Their associated integrated
query and adaptive Gaussian results Q2–Q7 and G are in
[Gaussian calculus](gaussian_calculus.md), under “Integrated queries and
adaptive Gaussian comparison”. Section 13 above supplies the exact query
memory identities used by that comparison.

## S. Squared-logarithmic response

The datum is one normalized scalar input, label one, three arctangent hidden
layers, unit block mobilities, and loss \(\mathcal L=(f_n-1)^2\).
The raw parameter metric is
\[
 n^{-1}\|dz^{(1)}\|_2^2+\|dW^{(2)}\|_F^2+
 \|dW^{(3)}\|_F^2+n^{-1}\|dW^{(4)}\|_2^2.
\]
The Euclidean coordinates used below multiply this metric by the common factor
\(n\); the readout is the stored readout, without Gaussian whitening.
The result controls squared logarithms of singular values of the actual full
response and of every transported initial subspace.

### Canonical coordinates and the bound

Let the width be \(n\ge1\), and let \(a=\pi/2\). All vector norms are
ordinary Euclidean norms, all matrix Frobenius norms are ordinary
Frobenius norms, and all transposes are finite transposes. The network is

\[
h^{(\ell)}=\phi(z^{(\ell)}),\quad \phi=\arctan,\quad
z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},\quad
f_n=(W^{(4)})^T h^{(3)}/n.
\]

Here \(W^{(4)}\) is the stored readout. The backward fields, without
the residual, are

\[
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\quad
q^{(2)}=(W^{(3)})^T\delta^{(3)},\quad
\delta^{(2)}=\phi'(z^{(2)})\odot q^{(2)},\quad
q^{(1)}=(W^{(2)})^T\delta^{(2)},\quad
\delta^{(1)}=\phi'(z^{(1)})\odot q^{(1)}.
\]

Use the Euclidean coordinates

\[
x=(z^{(1)},\sqrt n W^{(2)},\sqrt n W^{(3)})\in\mathbb R^{N_h},
\qquad c=W^{(4)}\in\mathbb R^n,\qquad N_h=n+2n^2.
\]

These use the raw first preactivation, without replacing it by the nonlinear primitive \(F(z)=z+z^3/3\). With

\[
\mathcal P(x,c)=c^T h^{(3)}(x),\qquad b=\nabla\mathcal P,
\]

the feature-time equations are exactly \((x,c)'=b(x,c)\). In particular,
the two hidden matrix blocks of \(b\) are

\[
\delta^{(2)}(h^{(1)})^T/\sqrt n,
\qquad \delta^{(3)}(h^{(2)})^T/\sqrt n.
\]

Let \(B=Db=D^2\mathcal P\). At any state obeying

\[
\|W^{(2)}\|_{\rm op},\|W^{(3)}\|_{\rm op}\le M,
\qquad \|c\|_2/\sqrt n\le R,
\tag{S.1}
\]

put \(K_2=a+M\), \(K_3=a+MK_2\), and

\[
C_B(M,R)=2R(M^2+MK_2^2+K_3^2+M+K_2)+\sqrt2 K_3.
\]

Then the full state-space Frobenius norm satisfies

\[
\|B\|_{\rm F}\le C_B(M,R)\sqrt n.
\tag{S.2}
\]

This needs neither a maximum-coordinate readout bound nor a spatial
tail bound on either backward query.

Let \(U(s,s_0)\) be the full derivative propagator along an actual
finite-width feature flow, and let \(E:\mathbb R^k\to\mathbb R^{N_h+n}\)
be any isometric linear embedding, \(E^TE=I_k\). If (S.1) holds throughout
\([s_0,s]\), then, for the \(k\) positive singular values of \(U(s,s_0)E\),

\[
\sum_{j=1}^k\bigl(\log\sigma_j(U(s,s_0)E)\bigr)^2
\le C_B(M,R)^2 n(s-s_0)^2.
\tag{S.3}
\]

The estimate holds for every embedding on the same pathwise event;
independence between the embedding and the trajectory is unnecessary.
In particular,

\[
\#\{j:|\log\sigma_j(U(s,s_0)E)|\ge r\}
\le C_B(M,R)^2 n(s-s_0)^2/r^2\qquad(r>0).
\tag{S.4}
\]

The analogous physical-time conclusions are given below.

### Complete Frobenius calculation

For a hidden variation \(u=(u_1,E_2,E_3)\), where \(E_2,E_3\) vary
the coordinates \(\sqrt n W^{(2)},\sqrt n W^{(3)}\), define

\[
T_1u=u_1,
\]
\[
T_2u=E_2h^{(1)}/\sqrt n+
 W^{(2)}[\phi'(z^{(1)})\odot u_1],
\]
\[
T_3u=E_3h^{(2)}/\sqrt n+
 W^{(3)}[\phi'(z^{(2)})\odot T_2u].
\]

Thus \(\|T_1\|_{\rm op}=1\), \(\|T_2\|_{\rm op}\le K_2\), and
\(\|T_3\|_{\rm op}\le K_3\). The derivative of the output feature
vector is \(J=\operatorname{diag}(\phi'(z^{(3)}))T_3\), so
\(\|J\|_{\rm op}\le K_3\) and \(\operatorname{rank}J\le n\).

Also define

\[
S_2u=E_2^T\delta^{(2)}/\sqrt n,
\qquad S_3u=E_3^T\delta^{(3)}/\sqrt n.
\]

The norm assumptions give

\[
\|q^{(2)}\|_2\le MR\sqrt n,\quad
\|q^{(1)}\|_2\le M^2R\sqrt n,\quad
\|S_2\|_{\rm op}\le MR,\quad \|S_3\|_{\rm op}\le R.
\tag{S.5}
\]

Twice differentiating \(c^Th^{(3)}\) along the straight hidden
parameter line gives, with \(A=D_x^2[c^Th^{(3)}]\),

\[
\begin{split}
u^TAu={}&(T_1u)^T\operatorname{diag}(\phi''(z^{(1)})\odot q^{(1)})T_1u\\
&+(T_2u)^T\operatorname{diag}(\phi''(z^{(2)})\odot q^{(2)})T_2u\\
&+(T_3u)^T\operatorname{diag}(\phi''(z^{(3)})\odot c)T_3u\\
&+2(S_2u)^T[\phi'(z^{(1)})\odot T_1u]\\
&+2(S_3u)^T[\phi'(z^{(2)})\odot T_2u].
\end{split}
\tag{S.6}
\]

For completeness, the second preactivation variations are

\[
d^2z^{(2)}[u,u]=2E_2[\phi'(z^{(1)})\odot u_1]/\sqrt n
 +W^{(2)}[\phi''(z^{(1)})\odot u_1^2],
\]
\[
d^2z^{(3)}[u,u]=2E_3[\phi'(z^{(2)})\odot T_2u]/\sqrt n
 +W^{(3)}[\phi''(z^{(2)})\odot(T_2u)^2
              +\phi'(z^{(2)})\odot d^2z^{(2)}[u,u]].
\]

The second derivative of the last activation and contraction with \(c\)
give (S.6), including both trained-matrix cross terms.

For any \(T\) and diagonal \(D\),
\(\|T^TDT\|_{\rm F}\le\|T\|_{\rm op}^2\|D\|_{\rm F}\).
Since \(|\phi''|\le2\), (S.5) bounds the three diagonal terms in (S.6)
respectively by

\[
2M^2R\sqrt n,\qquad 2K_2^2MR\sqrt n,
\qquad 2K_3^2R\sqrt n.
\]

Each map \(S_2^T\operatorname{diag}(\phi'(z^{(1)}))T_1\) has rank at
most \(n\), hence Frobenius norm at most \(MR\sqrt n\); adding its
transpose costs at most twice this. The corresponding \(S_3,T_2\)
pair costs at most \(2RK_2\sqrt n\). Finally,

\[
B=\begin{pmatrix}A&J^T\\J&0\end{pmatrix},\qquad
\left\|\begin{pmatrix}0&J^T\\J&0\end{pmatrix}\right\|_{\rm F}
=\sqrt2\|J\|_{\rm F}\le\sqrt{2n}K_3.
\]

The triangle inequality proves exactly (S.2). This calculation uses
the Euclidean coordinate metric specified above, not the unrescaled
matrix entries with a different gradient metric.

### Logarithms of all singular values, including repeated values

We prove the matrix implication without a singular-vector differentiability
assumption. Let \(D(t)\) be any continuous real square matrix, let
\(V'=DV\), and assume \(V(s_0)^TV(s_0)=I_m\). The fundamental square
solution is invertible, so the rectangular \(V(t)\) retains full column
rank. Put

\[
G=V^TV>0,\qquad Q=VG^{-1/2},\qquad Q^TQ=I_m,
\qquad \mathcal E=\tfrac14\operatorname{Tr}[(\log G)^2].
\]

Then \(\mathcal E=\sum_j(\log\sigma_j(V))^2\). To differentiate without
any assumption of simple singular values, use the convergent resolvent formula
\[
 \log G=\int_0^\infty[(1+t)^{-1}I-(G+tI)^{-1}],dt,
 \quad
 D\log G[G']=\int_0^\infty(G+tI)^{-1}G'(G+tI)^{-1}\,dt.
\]
On a compact time interval the eigenvalues of \(G\) stay in a compact subset
of \((0,\infty)\), so differentiating under this integral is justified by a
constant bound near zero and an integrable \(O(t^{-2})\) bound at infinity.
The product rule and cyclicity of trace give
\(\mathcal E'=\tfrac12\operatorname{Tr}[(\log G)D\log G[G']]\).
Since \(\log G\) commutes with its resolvents and
\(\int_0^\infty(G+tI)^{-2}dt=G^{-1}\), this proves the first equality below,
including repeated eigenvalues. With \(D_{\rm sym}=(D+D^T)/2\),

\[
\begin{split}
\mathcal E'
&=\tfrac12\operatorname{Tr}[(\log G)G^{-1}G']\\
&=\operatorname{Tr}[(\log G)Q^TD_{\rm sym}Q].
\end{split}
\]

Cauchy--Schwarz for Frobenius products, together with
\(\|Q^TD_{\rm sym}Q\|_{\rm F}\le\|D_{\rm sym}\|_{\rm F}\), gives

\[
|\mathcal E'|\le2\sqrt{\mathcal E}\,\|D_{\rm sym}\|_{\rm F}.
\]

To avoid division at zero, differentiate \(\sqrt{\mathcal E+\epsilon}\)
for \(\epsilon>0\), integrate from \(s_0\), and let \(\epsilon\downarrow0\).
Because \(\mathcal E(s_0)=0\),

\[
\left(\sum_j(\log\sigma_j(V(s)))^2\right)^{1/2}
\le\int_{s_0}^s\|D_{\rm sym}(u)\|_{\rm F}\,du.
\tag{S.7}
\]

No normality, commutation in time, or selected smooth eigenbasis is
required. Taking \(D=B\) and \(V=U(\cdot,s_0)E\) proves (S.3)--(S.4).

### Physical time and canonical Gaussian initialization

The exact physical field is \(2(1-f_n)b\). Since
\(\nabla f_n=b/n\), its Jacobian is

\[
B_{\rm phys}=2(1-f_n)B-(2/n)bb^T.
\tag{S.8}
\]

All clock derivatives are retained in the second term. The elementary
bound

\[
\|b\|_2^2/n\le M^4R^2+a^2M^2R^2+a^2R^2+a^2=:K_b^2
\]

follows by evaluating its four blocks. Also \(|f_n|\le aR\). Thus,
using \(n\ge1\),

\[
\|B_{\rm phys}\|_{\rm F}
\le[2(1+aR)C_B(M,R)+2K_b^2]\sqrt n=:C_{\rm phys}(M,R)\sqrt n.
\tag{S.9}
\]

Consequently (S.3)--(S.4) apply at fixed physical times with \(C_B\)
replaced by \(C_{\rm phys}\) and \(s-s_0\) by \(t-t_0\). These are
derivatives at fixed physical time, not derivatives obtained by
silently holding a state-dependent feature clock fixed.

The canonical independent initialization is
\(z^{(1)}_{0,i}\sim N(0,1)\),
\(W^{(2)}_{0,ij},W^{(3)}_{0,ij}\sim N(0,1/n)\),
and \(W^{(4)}_{0,i}\sim N(0,n^{-2})\).
Here is a direct proof of the needed probability and primal bounds. Put
\(\beta=1/(2a)\). A maximal \(1/4\)-separated sphere net has at most
\(9^n\) points (disjoint radius-\(1/8\) balls fit inside the ball of
radius \(9/8\)); two such nets give
\(\|W\|_{op}\le2\max_{u,v}|u^TWv|\). Each bilinear form is
\(N(0,1/n)\), so the probability either hidden norm exceeds 10 is at
most \(4\exp((2\log9-100/8)n)\). Markov's inequality gives
\(\mathbb P(\|c_0\|_2/\sqrt n>\beta)\le4a^2/n^2\).
On the complementary event define, for \(u\ge0\),
\[
 P_3(u)=10+a\beta u+a^2u^2/2,\qquad
 P_2(u)=10+a\int_0^uP_3(v)(\beta+av)\,dv.
\]
The four feature equations imply successively
\[
 \|c(u)\|_2/\sqrt n\le\beta+au,\quad
 \|W^{(3)}(u)\|_{op}\le P_3(u),\quad
 \|W^{(2)}(u)\|_{op}\le P_2(u),\quad
 \|(z^{(1)})'(u)\|_2/\sqrt n\le P_2(u)P_3(u)(\beta+au).
\]
The same rank-one estimates bound both learned Frobenius increments. These
finite polynomials prevent finite feature-time escape; the smooth ODE therefore
exists on every nonnegative finite feature interval. Moreover
\(f_n'=\|b\|_2^2/n\ge0\). Along the physical flow the residual obeys
\(\dot r=-2(\|b\|_2^2/n)r\). Since \(|f_n(0)|\le1/2\), the clock is
nonnegative and \(0\le s(t)\le3t\). Solving this scalar clock over the
complete feature solution proves physical existence on every fixed \([0,T]\)
and the asserted bounds with constants obtained at \(u=3T\). Their event
has probability at least
\(1-4e^{(2\log9-100/8)n}-4a^2/n^2\). Substitution into (S.3)--(S.4) and (S.9)
proves the Gaussian finite-horizon corollary. The deterministic estimates above do not assume a Gaussian
draw and also allow exactly zero readout. They do not transfer a
zero-readout population limit to the tiny-readout population limit.

### Actual top-column probe and the unresolved amplitude

Fix a middle neuron \(i\). In the raw coordinates above the embedding

\[
E_i u=(0,0,ue_i^T,0)
\]

is isometric. It corresponds to perturbing the original top matrix
column by \(u/\sqrt n\). If \(g\sim N(0,I_n)\) is an independent
derivative probe and \(Y_i=U(s,0)E_i\), then \(Y_i g\) is the full
canonical column response, conditional on the trained trajectory.
Its conditional covariance is \(Y_iY_i^T\); its nonzero eigenvalues
are \(\sigma_j(Y_i)^2\). Hence (S.3) gives explicitly \(\sum_j(\log\lambda_j)^2\le4C_B(M,R)^2ns^2\) for that actual covariance spectrum. It is not a hypothesis on a
surrogate response.

For the trained-increment response \(Z_i=Y_i-E_i\),

\[
Z_i^TZ_i\preceq2Y_i^TY_i+2I_n.
\]

Writing the eigenvalues in decreasing order and using the variational
characterization of ordered eigenvalues gives

\[
\begin{split}
\sum_{j=1}^n[\log(1+\sigma_j(Z_i)^2)]^2
&\le\sum_{j=1}^n[\log(3+2\sigma_j(Y_i)^2)]^2\\
&\le2n(\log5)^2+8\sum_{j=1}^n(\log\sigma_j(Y_i))^2\\
&\le n[2(\log5)^2+8C_B(M,R)^2s^2].
\tag{S.10}
\end{split}
\]

The scalar inequality used is \(3+2u^2\le5\max(1,u^2)\).
The same conclusion holds with the physical propagator and its constant.

The estimates do not supply a width-uniform bound on the normalized
trace \(\operatorname{Tr}(Z_i^TZ_i)/n\), nor on the response energy required
by the global stability proof. For example,
the abstract matrix path generated by
\(D_n=\operatorname{diag}(\sqrt n,0,\ldots,0)\) has
\(\|D_n\|_{\rm F}=\sqrt n\) and satisfies (S.7) with equality, while
one singular value is \(e^{s\sqrt n}\). Its mean squared amplification
over \(n\) directions diverges at every fixed positive \(s\). This
abstract example is not claimed to be a canonical network trajectory.
It shows precisely why (S.2)--(S.10) alone do not close the amplitude bound.

The count \(O(n/r^2)\) in the stated raw metric is an actual-response
constraint. No transfer to the nonlinear first-layer coordinate is claimed. It leaves the
canonical alignment and amplitude problem open. A complete global
proof still requires a further estimate controlling those quantities.



## I. Initial Gaussian middle curvature

The following initialization lemma supplies the joint empirical law used in
fragment C. It is an initialization result for the same one-input arctangent
model, with all displayed hidden matrices independent. It does not require a
readout draw.
### Statement

For each integer \(n\geq1\), let
\[
z_{0,i}^{(1)}\overset{\mathrm{iid}}{\sim}N(0,1),\qquad
(W_0^{(2)})_{ij},(W_0^{(3)})_{ij}
\overset{\mathrm{iid}}{\sim}N(0,1/n),
\qquad 1\leq i,j\leq n,
\]
with all these variables independent. Define, coordinatewise,
\[
\phi(x)=\arctan x,\qquad
h_0^{(\ell)}=\phi(z_0^{(\ell)}),\qquad
z_0^{(2)}=W_0^{(2)}h_0^{(1)},\qquad
z_0^{(3)}=W_0^{(3)}h_0^{(2)}.
\]
All vectors here belong to \(\mathbb R^n\); \(\|\cdot\|\) is the ordinary Euclidean norm, and \(T\) denotes transpose. Set
\[
g(x)=\phi'(x)\phi(x)=\frac{\arctan x}{1+x^2},
\qquad
u_n^{(2)}=(W_0^{(3)})^T
\bigl[\phi'(z_0^{(3)})\odot\phi(z_0^{(3)})\bigr]
=(W_0^{(3)})^T g(z_0^{(3)}).
\]
Thus \(u_n^{(2)}\) is determined by the displayed canonical initialization.

Let \(G_1,G_2,G_3,G\) be independent \(N(0,1)\) population variables, and define
\[
\begin{aligned}
m_1&=\mathbb E[\phi(G_1)^2],
&Z^{(2)}&=\sqrt{m_1}\,G_2,\\
m_2&=\mathbb E[\phi(Z^{(2)})^2],
&Z^{(3)}&=\sqrt{m_2}\,G_3,\\
\beta&=\frac{\mathbb E[Z^{(3)}g(Z^{(3)})]}{m_2},
&\sigma^2&=\mathbb E[g(Z^{(3)})^2],\qquad
U^{(2)}=\beta\phi(Z^{(2)})+\sigma G,
\end{aligned}
\]
where \(\sigma\) is the positive square root. Then
\(m_1,m_2,\sigma^2>0\) and \(0<\beta\leq1\).

For every continuous \(F:\mathbb R^2\to\mathbb R\) satisfying
\[
|F(z,v)|\leq C_F(1+z^2+v^2)
\quad\text{for some finite }C_F,
\]
the joint empirical-average law is
\[
\frac1n\sum_{i=1}^n F(z_{0,i}^{(2)},u_{n,i}^{(2)})
\longrightarrow \mathbb E[F(Z^{(2)},U^{(2)})]
\quad\text{in probability and in }L^1.
\tag{I.1}
\]
In particular, with \([a]_+=\max(a,0)\),
\[
c_n=\frac1n\sum_{i=1}^n
\bigl[u_{n,i}^{(2)}\phi''(z_{0,i}^{(2)})\bigr]_+
\longrightarrow
c_*=\mathbb E\!\left[\bigl[U^{(2)}\phi''(Z^{(2)})\bigr]_+\right]>0
\quad\text{in probability and in }L^1.
\tag{I.2}
\]
Consequently \(\mathbb E c_n\to c_*\).

The proof first derives the exact conditional law after reuse of
\(W_0^{(3)}\), then removes its projection term in root mean square.
A coupling with independent population pairs gives empirical convergence.
Uniform fourth moments justify the unbounded tests and convergence of
expectations; an explicit conditional Gaussian event gives strict positivity.

### Proof

Write \(H=\pi/2\). The elementary bounds used below are
\[
|\phi(x)|\leq H,\quad |\phi(x)|\leq|x|,\quad
0<\phi'(x)=\frac1{1+x^2}\leq1,\quad
\phi''(x)=-\frac{2x}{(1+x^2)^2},\quad |\phi''(x)|\leq2,
\tag{I.3}
\]
and
\[
|g(x)|\leq H,\qquad |g(x)|\leq|x|,\qquad
0\leq xg(x)\leq x^2,\qquad |xg(x)|\leq H/2.
\tag{I.4}
\]
For the last bound use \(|x|/(1+x^2)\leq1/2\).
The function \(g\) vanishes exactly at zero, and \(xg(x)>0\) for \(x\ne0\).
Since a nondegenerate Gaussian has probability zero of being zero,
these facts successively give \(m_1>0\), \(m_2>0\),
\(\sigma^2>0\), and \(\mathbb E[Z^{(3)}g(Z^{(3)})]>0\).
All expectations are finite by (I.3)--(I.4).
Also \(\mathbb E[Z^{(3)}g(Z^{(3)})]\leq\mathbb E (Z^{(3)})^2=m_2\), proving
\(0<\beta\leq1\).

### Exact finite-dimensional conditioning

Define the empirical second moments
\[
m_{1,n}=\frac{\|h_0^{(1)}\|^2}{n},\qquad
m_{2,n}=\frac{\|h_0^{(2)}\|^2}{n}.
\]
Almost surely \(m_{1,n}>0\): its vanishing would require all
\(z_{0,i}^{(1)}=0\). Given the first layer, the rows of \(W_0^{(2)}\)
give independent coordinates \(z_{0,i}^{(2)}\sim N(0,m_{1,n})\).
Thus, conditionally on \(m_{1,n}>0\), the probability that \(h_0^{(2)}=0\)
is zero. In particular \(m_{2,n}>0\) almost surely.
Given the variables in the first two layers, the \(z_{0,j}^{(3)}\) are independent
\(N(0,m_{2,n})\). Hence \(z_0^{(3)}\ne0\) and \(\|g(z_0^{(3)})\|>0\) almost surely.
Both random variances lie in \([0,H^2]\).

For a fixed nonzero \(h_0^{(2)}\), define the orthogonal projection
\[
P_n^{(2)}=\frac{h_0^{(2)}(h_0^{(2)})^T}{\|h_0^{(2)}\|^2}.
\]
Writing \((W_0^{(3)})_{j,:}\) for row \(j\), the exact decomposition is
\[
(W_0^{(3)})_{j,:}^T
=\frac{h_0^{(2)}\,z_{0,j}^{(3)}}{\|h_0^{(2)}\|^2}
+(I-P_n^{(2)})(W_0^{(3)})_{j,:}^T,\qquad
z_{0,j}^{(3)}=(W_0^{(3)})_{j,:}h_0^{(2)}.
\]
Conditionally on \(h_0^{(2)}\), the scalar \(z_{0,j}^{(3)}\) and vector
\((I-P_n^{(2)})(W_0^{(3)})_{j,:}^T\) are jointly Gaussian,
and their cross covariance is
\[
\mathbb E\!\left[
(I-P_n^{(2)})(W_0^{(3)})_{j,:}^T z_{0,j}^{(3)}
\mid h_0^{(2)}\right]
=\frac1n(I-P_n^{(2)})h_0^{(2)}=0.
\]
They are therefore independent: the characteristic function of a centered
joint Gaussian with zero cross covariance factors into its two marginal
characteristic functions. The residual vectors for distinct rows are
independent, have covariance \((I-P_n^{(2)})/n\), and are independent of the
entire vector \(z_0^{(3)}\). Since \(W_0^{(3)}\) is independent of all lower-layer
variables, the same statements hold after additionally conditioning on
those variables.

Multiplying row \(j\) by \(g(z_{0,j}^{(3)})\) and summing proves that, conditionally
on the lower layers and \(z_0^{(3)}\),
\[
u_n^{(2)}\ \overset{\mathrm{law}}{=}
\beta_n h_0^{(2)}+\sigma_n(I-P_n^{(2)})\xi,\qquad
\beta_n=\frac{(z_0^{(3)})^Tg(z_0^{(3)})}{\|h_0^{(2)}\|^2},\qquad
\sigma_n^2=\frac{\|g(z_0^{(3)})\|^2}{n},
\tag{I.5}
\]
where \(\xi\sim N(0,I_n)\) can be chosen independent of the lower layers
and \(z_0^{(3)}\). Indeed, the conditional mean is \(\beta_n h_0^{(2)}\), and the
conditional covariance is
\[
\sum_{j=1}^n g(z_{0,j}^{(3)})^2\,\frac{I-P_n^{(2)}}{n}
=\sigma_n^2(I-P_n^{(2)}).
\]
The square root \(\sigma_n\) is nonnegative and is positive almost surely.
If \(h_0^{(2)}=0\), then \(z_0^{(3)}=0\), \(g(z_0^{(3)})=0\), and the original \(u_n^{(2)}=0\).
On this null event set \(\beta_n=0\) and \(P_n^{(2)}=0\);
then \(\sigma_n=0\) and (I.5) remains valid. These conventions resolve
every zero denominator in (I.5).

Equation (I.5) is a conditional-law representation of the original
matrix-derived vector. It does not change the initialization or introduce
an independent network output. In particular, it retains the correlation
created by using the same matrix in \(z_0^{(3)}=W_0^{(3)}h_0^{(2)}\) and
\(u_n^{(2)}=(W_0^{(3)})^Tg(z_0^{(3)})\).

### Random variances and coefficients

For independent identically distributed variables of finite variance \(v\),
their sample average has variance \(v/n\); Chebyshev's inequality therefore
gives convergence in probability to their mean. We use this fact also
conditionally, integrating the conditional variance bound.

Applied to the bounded first-layer variables it gives
\[
m_{1,n}\longrightarrow m_1
\quad\text{in }L^2\text{ and in probability}.
\tag{I.6}
\]
Let \(G'\sim N(0,1)\) be a dummy variable in expectations and define on
\([0,H^2]\)
\[
f(q)=\mathbb E[\phi(\sqrt q\,G')^2],\qquad
a(q)=\mathbb E[\sqrt q\,G' g(\sqrt q\,G')],\qquad
b(q)=\mathbb E[g(\sqrt q\,G')^2].
\]
Each function is continuous, including at zero: its integrand is
pointwise continuous in \(q\), and (I.3)--(I.4) bound the integrands
respectively by \(H^2,H/2,H^2\), so dominated convergence applies.
Conditionally on the first layer,
\[
\mathbb E[m_{2,n}\mid z_0^{(1)}]=f(m_{1,n}),\qquad
\mathbb E[(m_{2,n}-f(m_{1,n}))^2\mid z_0^{(1)}]\leq H^4/n.
\]
Continuity of \(f\), (I.6), and this variance bound give
\[
m_{2,n}\longrightarrow f(m_1)=m_2
\quad\text{in probability}.
\tag{I.7}
\]
For example, continuity at \(m_1\) says that sufficiently small
\(|m_{1,n}-m_1|\) makes \(|f(m_{1,n})-f(m_1)|\) arbitrarily small;
the complementary event has probability tending to zero by (I.6).

Set \(A_n=(z_0^{(3)})^Tg(z_0^{(3)})/n\). Conditionally on the lower layers, (I.4) gives
\[
\begin{aligned}
\mathbb E[A_n\mid z_0^{(1)},W_0^{(2)}]&=a(m_{2,n}),&
\mathbb E[(A_n-a(m_{2,n}))^2\mid z_0^{(1)},W_0^{(2)}]
&\leq H^2/(4n),\\
\mathbb E[\sigma_n^2\mid z_0^{(1)},W_0^{(2)}]&=b(m_{2,n}),&
\mathbb E[(\sigma_n^2-b(m_{2,n}))^2\mid z_0^{(1)},W_0^{(2)}]
&\leq H^4/n.
\end{aligned}
\]
Using (I.7) and continuity of \(a,b\), we obtain
\[
A_n\longrightarrow a(m_2)=\mathbb E[Z^{(3)}g(Z^{(3)})],\qquad
\sigma_n^2\longrightarrow b(m_2)=\sigma^2
\quad\text{in probability}.
\]
Since \(m_2>0\), the event \(m_{2,n}\geq m_2/2\) has probability tending
to one. Division on this event and continuity of the square root yield
\[
\beta_n=A_n/m_{2,n}\longrightarrow\beta,\qquad
\sigma_n\longrightarrow\sigma
\quad\text{in probability}.
\tag{I.8}
\]
The ratio at zero uses the convention in (I.5). No deterministic lower
bound on the finite random variances was assumed.

### Projection correction and joint empirical convergence

The successive forward conditional Gaussian laws and (I.5) permit the
following exact construction in distribution. Draw the first layer and
three mutually independent standard Gaussian vectors
\(\eta,\zeta,\xi\), independent also of the first layer, and set
\[
z_{0,i}^{(2)}=\sqrt{m_{1,n}}\,\eta_i,\qquad
h_0^{(2)}=\phi(z_0^{(2)}),\qquad
z_0^{(3)}=\sqrt{m_{2,n}}\,\zeta,\qquad
u_n^{(2)}=\beta_n h_0^{(2)}+\sigma_n(I-P_n^{(2)})\xi.
\tag{I.9}
\]
The coefficients and variances in (I.9) are computed from the vectors
already drawn, exactly as above. Successively conditioning on the first
layer, on \(z_0^{(2)}\), and on \(z_0^{(3)}\) shows that (I.9) has the original
joint law of \((z_0^{(1)},z_0^{(2)},z_0^{(3)},u_n^{(2)})\). This equality includes
all dependencies needed below; it does not assert independence of the
original coordinate pairs.

For the projection correction, independence of \(\xi\) and \((h_0^{(2)},z_0^{(3)})\) gives,
on \(h_0^{(2)}\ne0\),
\[
\mathbb E\left[\left.
\frac{\|\sigma_nP_n^{(2)}\xi\|^2}{n}\right|h_0^{(2)},z_0^{(3)}\right]
=\frac{\sigma_n^2}{n}
\mathbb E\left[\left.\frac{((h_0^{(2)})^T\xi)^2}{\|h_0^{(2)}\|^2}\right|h_0^{(2)},z_0^{(3)}\right]
=\frac{\sigma_n^2}{n}\leq\frac{H^2}{n}.
\tag{I.10}
\]
On \(h_0^{(2)}=0\) the left side is zero by the stated conventions.
Thus \(\|\sigma_nP_n^{(2)}\xi\|/\sqrt n\) tends to zero in \(L^2\) and in
probability. This also covers \(n=1\), when \(P_n^{(2)}=I\) for \(h_0^{(2)}\ne0\).

On the representation space define the comparison coordinates
\[
\bar z_i^{(2)}=\sqrt{m_1}\,\eta_i,\qquad
\bar u_i^{(2)}=\beta\phi(\bar z_i^{(2)})+\sigma\xi_i.
\]
These comparison pairs are independent and identically distributed with
law \((Z^{(2)},U^{(2)})\). Since
\[
\frac1n\sum_i|z_{0,i}^{(2)}-\bar z_i^{(2)}|^2
=(\sqrt{m_{1,n}}-\sqrt{m_1})^2\,\frac1n\sum_i\eta_i^2,
\tag{I.11}
\]
the left side tends to zero in probability by (I.6) and
\(n^{-1}\sum_i\eta_i^2\to1\). The latter convergence follows from
\(\mathbb E\eta_i^2=1\), \(\operatorname{Var}(\eta_i^2)=2\) and
the sample-average variance bound. The same reasoning gives
\(\|\xi\|/\sqrt n\to1\) in probability.

The bound \(\phi'\leq1\) makes \(\phi\) Lipschitz with constant one.
Subtracting the comparison vector from (I.9) and using the triangle
inequality consequently gives
\[
\begin{split}
\frac{\|u_n^{(2)}-\bar u^{(2)}\|}{\sqrt n}
&\leq |\beta_n-\beta|\sqrt{m_{2,n}}
+|\beta|\frac{\|z_0^{(2)}-\bar z^{(2)}\|}{\sqrt n}\\
&\quad+|\sigma_n-\sigma|\frac{\|\xi\|}{\sqrt n}
+\frac{\|\sigma_nP_n^{(2)}\xi\|}{\sqrt n}
\longrightarrow0
\quad\text{in probability},
\end{split}
\tag{I.12}
\]
by (I.8)--(I.11) and \(m_{2,n}\leq H^2\).
In particular,
\[
D_n^2:=\frac1n\sum_i
\left(|z_{0,i}^{(2)}-\bar z_i^{(2)}|^2+|u_{n,i}^{(2)}-\bar u_i^{(2)}|^2\right)
\longrightarrow0
\quad\text{in probability}.
\tag{I.13}
\]

If \(F\) is bounded and uniformly continuous, let
\(\omega_F(\delta)=\sup_{\|x-x'\|\leq\delta}|F(x)-F(x')|\),
using the ordinary Euclidean norm on \(\mathbb R^2\).
At most a fraction \(D_n^2/\delta^2\) of the paired points have
distance exceeding \(\delta>0\), so
\[
\left|\frac1n\sum_i F(z_{0,i}^{(2)},u_{n,i}^{(2)})
-\frac1n\sum_i F(\bar z_i^{(2)},\bar u_i^{(2)})\right|
\leq\omega_F(\delta)+2\|F\|_\infty D_n^2/\delta^2.
\tag{I.14}
\]
First choosing \(\delta\) so that \(\omega_F(\delta)\) is small and then
using (I.13) proves that this difference tends to zero in probability.
The comparison average converges to \(\mathbb E F(Z^{(2)},U^{(2)})\) by
the sample-average variance bound, since its summands are bounded and
independent. We next justify the larger test class in (I.1).

### Uniform moments, unbounded tests, and \(L^1\)

The following moment bounds are uniform over every \(n\geq1\).
Gaussian integration by parts gives
\(\mathbb E(G')^{2k}=(2k-1)\mathbb E(G')^{2k-2}\):
integrate \(x^{2k-1}x e^{-x^2/2}\), whose boundary term vanishes.
Thus \(\mathbb E(G')^4=3\) and \(\mathbb E(G')^8=105\).
The forward conditional law gives
\[
\mathbb E|z_{0,i}^{(2)}|^4=3\mathbb E m_{1,n}^2\leq3H^4.
\tag{I.15}
\]
On \(m_{2,n}>0\), (I.4) and (I.9) give
\[
0\leq\beta_n
\leq\frac{\|z_0^{(3)}\|^2}{nm_{2,n}}
=\frac1n\sum_j\zeta_j^2.
\]
Convexity of \(t\mapsto t^4\) on \([0,\infty)\) therefore yields
\[
\mathbb E\beta_n^4
\leq\mathbb E\left(\frac1n\sum_j\zeta_j^2\right)^4
\leq\frac1n\sum_j\mathbb E\zeta_j^8=105.
\tag{I.16}
\]
The null-event convention satisfies the same moment bound.
Conditionally on \(h_0^{(2)},z_0^{(3)}\), each coordinate
\(\sigma_n((I-P_n^{(2)})\xi)_i\) is a centered Gaussian of variance at most
\(\sigma_n^2\leq H^2\), and hence of fourth moment at most \(3H^4\).
Using \(|r+s|^4\leq8(|r|^4+|s|^4)\) in (I.5), together with
\(|h_{0,i}^{(2)}|\leq H\) and (I.16), proves
\[
\mathbb E|u_{n,i}^{(2)}|^4\leq8H^4\mathbb E\beta_n^4+24H^4
\leq864H^4.
\tag{I.17}
\]
This is a direct moment estimate for the reused Gaussian matrix;
it requires no independence between its original output coordinates.
The population variables likewise have finite fourth moments because
\(Z^{(2)}\) is Gaussian and
\(|U^{(2)}|\leq|\beta|H+\sigma|G|\).
Since \((z^2+v^2)^2\leq2(z^4+v^4)\), (I.15)--(I.17) in particular imply
\[
\sup_n\mathbb E\left[\frac1n\sum_i
\bigl((z_{0,i}^{(2)})^2+(u_{n,i}^{(2)})^2\bigr)^2\right]<\infty.
\tag{I.18}
\]

Now let \(F\) have the continuous, at most quadratic growth in (I.1).
For \(R\geq1\), choose a continuous function
\(\chi_R:\mathbb R^2\to[0,1]\) equal to one on the ball of radius \(R\)
and zero outside the ball of radius \(R+1\); for example
\(\chi_R(x)=\max(0,\min(1,R+1-\|x\|))\).
Then \(F_R=\chi_RF\) is continuous with compact support and is bounded
and uniformly continuous, so (I.14) applies. For \(r=(z^2+v^2)^{1/2}\),
\[
|F(z,v)-F_R(z,v)|
\leq C_F(1+r^2)\mathbf1_{\{r>R\}}
\leq \frac{2C_F}{R^2}r^4.
\tag{I.19}
\]
By (I.18), the expectation of the empirical average of (I.19) is bounded
by a constant times \(R^{-2}\), uniformly in \(n\).
The analogous population expectation has the same bound, because the
population fourth moment is finite. Markov's inequality therefore
makes the empirical truncation error small in probability uniformly
in \(n\). First taking \(n\to\infty\) for \(F_R\), and then
\(R\to\infty\) in these bounds, proves the probability convergence
in (I.1).

For completeness, write
\(X_n=n^{-1}\sum_iF(z_{0,i}^{(2)},u_{n,i}^{(2)})\) and
\(\mu=\mathbb E F(Z^{(2)},U^{(2)})\), which is finite by the population
moment bound. Jensen's inequality and (I.18) give
\[
\sup_n\mathbb E|X_n|^2
\leq C_F^2\sup_n\mathbb E\left[\frac1n\sum_i
\bigl(1+(z_{0,i}^{(2)})^2+(u_{n,i}^{(2)})^2\bigr)^2\right]<\infty.
\tag{I.20}
\]
Here \((1+r^2)^2\leq2(1+r^4)\). In particular the averages are
uniformly integrable, since
\(\mathbb E[|X_n|\mathbf1_{\{|X_n|>K\}}]\leq\mathbb E|X_n|^2/K\).
More explicitly, for every \(\varepsilon>0\), Cauchy--Schwarz gives
\[
\mathbb E|X_n-\mu|
\leq\varepsilon+
\bigl(\mathbb E|X_n-\mu|^2\bigr)^{1/2}
\mathbb P(|X_n-\mu|>\varepsilon)^{1/2}.
\]
The second moments are bounded by (I.20), and the probabilities tend
to zero. Taking a limit superior and then \(\varepsilon\downarrow0\)
proves \(L^1\) convergence in (I.1). All probability and expectation
statements transfer from (I.9) to the canonical network by equality
of the joint laws for each \(n\).

### The curvature average and strict positivity

The test
\[
F(z,v)=[v\phi''(z)]_+
\]
is continuous. By (I.3),
\(0\leq F(z,v)\leq2|v|\leq1+v^2\), so it is in the class of (I.1).
This proves both convergences in (I.2) and finiteness of \(c_*\).

To prove strict positivity explicitly, on \(1\leq z\leq2\) we have
\[
-\phi''(z)=\frac{2z}{(1+z^2)^2}\geq\frac{2}{25}.
\]
Consider the event
\[
1\leq Z^{(2)}\leq2,\qquad
G\leq-\frac{|\beta|H+1}{\sigma}.
\tag{I.21}
\]
On (I.21), \(U^{(2)}=\beta\phi(Z^{(2)})+\sigma G\leq-1\), so
\([U^{(2)}\phi''(Z^{(2)})]_+\geq2/25\).
Conditionally on any \(Z^{(2)}=z\in[1,2]\), the second event in (I.21)
has the same strictly positive probability, since \(G\) is independent
of \(Z^{(2)}\) and \(\sigma>0\).
Writing \(\Phi\) for the standard Gaussian distribution function gives
\[
c_*\geq\frac{2}{25}
\left[\Phi\!\left(\frac2{\sqrt{m_1}}\right)
-\Phi\!\left(\frac1{\sqrt{m_1}}\right)\right]
\Phi\!\left(-\frac{|\beta|H+1}{\sigma}\right)>0.
\tag{I.22}
\]
The bracket is positive because \(m_1>0\) and the Gaussian density
is strictly positive on every finite interval; the last factor is
positive because its argument is finite.

This proves the claimed initial hidden-layer empirical law and curvature
limit. The Gaussian representation was exact at finite \(n\); only the
explicit projection correction and empirical averages were passed to
their limits. No central limit approximation or independence assertion
for the original finite coordinate pairs is involved. \(\square\)


## C. Positive middle curvature at small feature times

For the canonical tiny-readout initialization, the actual middle coefficient
\(q_i^{(2)}\phi''(z_i^{(2)})\) has a positive-part mean of linear size at small
fixed feature times. A positive fraction of the coefficients have that size.
The proof differentiates the actual trained query and controls its remainder;
it does not replace the trajectory by an evolved zero-readout solution.
The datum, raw metric and loss are those in S; clipped variants are expressly
defined below and are not asserted to be loss gradients.

### 1. Exact dynamics and deterministic path bounds

Let \(\phi=\arctan\), \(c=\pi/2\), and fix a feature horizon \(S>0\).
The first layer is the vector \(z^{(1)}=W^{(1)}\); the hidden matrices
are \(W^{(2)},W^{(3)}\); \(W^{(4)}\) is the stored readout vector.
Use ordinary Euclidean vector norms, ordinary matrix operator and
Frobenius norms, and finite transpose \(T\). Define
\[
h^{(\ell)}=\phi(z^{(\ell)}),\quad
z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},
\]
\[
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\quad
q^{(2)}=(W^{(3)})^T\delta^{(3)},\quad
\delta^{(2)}=\phi'(z^{(2)})\odot\tau(q^{(2)}).
\]
Here \(\tau\) is any fixed prescribed map with
\(|\tau(v)|\le|v|\) and \(|\tau(v)-\tau(w)|\le|v-w|\).
The identity gives the exact uncut model. There is no pruning mask.
Every trained block obeys its actual feature equation:
\[
\begin{gathered}
(z^{(1)})'=\phi'(z^{(1)})\odot(W^{(2)})^T\delta^{(2)},\\
(W^{(2)})'=\delta^{(2)}(h^{(1)})^T/n,\quad
(W^{(3)})'=\delta^{(3)}(h^{(2)})^T/n,\quad
(W^{(4)})'=h^{(3)}.
\end{gathered}
\tag{C.1}
\]
The estimates are in feature time \(s\), not physical time. The canonical
uncut physical flow is (C.1) times \(2(1-f)\), for
\(f=(W^{(4)})^Th^{(3)}/n\) and loss \((f-1)^2\).
No physical-clock or exact-GD convergence assertion is made here.

For arbitrary finite initial data put
\[
M=\max_{\ell=2,3}\|W^{(\ell)}(0)\|_{\rm op},\qquad
\varepsilon=\frac{\|W^{(4)}(0)\|_2}{\sqrt n},\qquad
\alpha=\|W^{(4)}(0)\|_\infty.
\]
These definitions impose no upper bound on \(\varepsilon,\alpha\).
In particular \(\varepsilon\le\alpha\le\sqrt n\,\varepsilon\).
Define the finite nonnegative constants
\[
\begin{gathered}
K_3=M+c(\varepsilon S+cS^2/2),\\
K_2=M+cK_3(\varepsilon S+cS^2/2),\\
J=K_3(c^2+K_2^2),\qquad K=c^2+K_3J.
\end{gathered}
\tag{C.2}
\]
They are polynomials in \(M,\varepsilon\), with coefficients depending
only on \(S\). The readout equation and \(|\phi|\le c\), \(|\phi'|\le1\)
give
\[
\frac{\|\delta^{(3)}(s)\|_2}{\sqrt n}
\le\frac{\|W^{(4)}(s)\|_2}{\sqrt n}\le\varepsilon+cs,\qquad
\|W^{(4)}(s)\|_\infty\le\alpha+cs.
\tag{C.3}
\]
Using \(\|uv^T/n\|_{\rm F}=\|u\|_2\|v\|_2/n\) in (C.1) yields
\[
\|W^{(3)}(s)-W^{(3)}(0)\|_{\rm F}
\le c(\varepsilon s+cs^2/2),\quad
\|W^{(3)}(s)\|_{\rm op}\le K_3,
\]
\[
\frac{\|\delta^{(2)}(s)\|_2}{\sqrt n}\le K_3(\varepsilon+cs),
\quad
\|W^{(2)}(s)-W^{(2)}(0)\|_{\rm F}
\le cK_3(\varepsilon s+cs^2/2),\quad
\|W^{(2)}(s)\|_{\rm op}\le K_2.
\tag{C.4}
\]
The first-layer velocity divided by \(\sqrt n\) is at most
\(K_2K_3(\varepsilon+cs)\).
At each fixed width, the vector field is locally Lipschitz, including
the Lipschitz clipping. Local existence and uniqueness follow from the
contraction of its integral equation on a sufficiently short interval
in a finite-dimensional ball. The displayed bounds keep every parameter
entry in a bounded set on a prescribed finite horizon. A hypothetical
finite endpoint then has a state limit, since the vector field is
bounded on that compact set, and local existence extends it.
Thus (C.1) has a unique trajectory through \([0,S]\).

Differentiating only the forward factors gives the exact identities
\[
(z^{(2)})'=
\left[\frac{\|h^{(1)}\|_2^2}{n}I+
W^{(2)}\operatorname{diag}(\phi'(z^{(1)})^2)(W^{(2)})^T\right]\delta^{(2)},
\]
\[
(z^{(3)})'=\frac{\|h^{(2)}\|_2^2}{n}\delta^{(3)}
+W^{(3)}\operatorname{diag}(\phi'(z^{(2)}))(z^{(2)})'.
\tag{C.5}
\]
No derivative of \(\tau\) is used. Consequently
\[
\frac{\|(z^{(2)})'(s)\|_2}{\sqrt n}\le J(\varepsilon+cs),\qquad
\frac{\|(z^{(3)})'(s)\|_2}{\sqrt n}\le K(\varepsilon+cs).
\tag{C.6}
\]
Integration bounds the corresponding displacements by
\(J(\varepsilon s+cs^2/2)\) and \(K(\varepsilon s+cs^2/2)\).

### 2. A direct Duhamel remainder for the actual middle query

Let \(g(v)=\phi'(v)\phi(v)\) and define the initial hidden-block query
\[
u_n^{(2)}=(W^{(3)}(0))^T g(z^{(3)}(0)).
\tag{C.7}
\]
This is a function only of the original hidden initialization, not an
extra random readout seed. We use
\[
|g|\le c,\quad |g'|=|(\phi')^2+\phi\phi''|\le1+2c,\quad
|\phi''|\le2,\quad
|\phi'''(v)|=\frac{|-2+6v^2|}{(1+v^2)^3}\le8.
\tag{C.8}
\]
In particular \(\|u_n^{(2)}\|_2/\sqrt n\le Mc\).

Differentiate the actual query, retaining the trained \(W^{(3)}\):
\[
\begin{split}
(q^{(2)})'
={}&h^{(2)}\frac{\|\delta^{(3)}\|_2^2}{n}
+(W^{(3)})^Tg(z^{(3)})\\
&+(W^{(3)})^T
\bigl[W^{(4)}\odot\phi''(z^{(3)})\odot(z^{(3)})'\bigr].
\end{split}
\tag{C.9}
\]
The first term is exactly \(((W^{(3)})')^T\delta^{(3)}\); the other
terms come from
\((\delta^{(3)})'=g(z^{(3)})+
W^{(4)}\odot\phi''(z^{(3)})\odot(z^{(3)})'\).
Thus (C.9) also holds for merely Lipschitz clipping.

For \(A=c^2+M(1+2c)K\), (C.4), (C.6), and (C.8) give
\[
\frac{\|(W^{(3)}(s))^Tg(z^{(3)}(s))-u_n^{(2)}\|_2}{\sqrt n}
\le A(\varepsilon s+cs^2/2).
\tag{C.10}
\]
Indeed the trained-matrix increment contributes at most
\(c^2(\varepsilon s+cs^2/2)\); the change of \(g\) contributes at most
\(M(1+2c)K(\varepsilon s+cs^2/2)\).
The other two terms of (C.9) have norms divided by \(\sqrt n\) bounded by
\[
c(\varepsilon+cs)^2,\qquad
2K_3K(\alpha+cs)(\varepsilon+cs).
\]
Also \(\|q^{(2)}(0)\|_2/\sqrt n\le M\varepsilon\).
Integrating (C.9)--(C.10) therefore proves, for every \(0\le s\le S\),
\[
\frac{\|q^{(2)}(s)-s u_n^{(2)}\|_2}{\sqrt n}\le R(s),
\tag{C.11}
\]
where the explicit nonnegative remainder is
\[
\begin{split}
R(s)={}&M\varepsilon+
c\left(\varepsilon^2s+\varepsilon c s^2+\frac{c^2s^3}{3}\right)\\
&+A\left(\frac{\varepsilon s^2}{2}+\frac{cs^3}{6}\right)\\
&+2K_3K\left(\alpha\varepsilon s+
\frac{c(\alpha+\varepsilon)s^2}{2}+\frac{c^2s^3}{3}\right).
\end{split}
\tag{C.12}
\]
The initial readout has not been set to zero or hidden in a
width-dependent Taylor remainder.

Define the empirical positive parts
\[
B_n(s)=\frac1n\sum_i[q_i^{(2)}(s)\phi''(z_i^{(2)}(s))]_+,\qquad
c_n=\frac1n\sum_i[(u_n^{(2)})_i\phi''(z_i^{(2)}(0))]_+.
\tag{C.13}
\]
The map \(x\mapsto[x]_+\) is 1-Lipschitz. Separate the query change
from the change of \(\phi''\), then use Cauchy--Schwarz and (C.6), (C.8):
\[
\begin{split}
|B_n(s)-s c_n|
&\le 2\frac{\|q^{(2)}(s)-s u_n^{(2)}\|_2}{\sqrt n}\\
&\quad+8s\frac{\|u_n^{(2)}\|_2}{\sqrt n}
\frac{\|z^{(2)}(s)-z^{(2)}(0)\|_2}{\sqrt n}\\
&\le 2R(s)+8McJ\,s(\varepsilon s+cs^2/2).
\end{split}
\tag{C.14}
\]
These inequalities are pathwise, simultaneous in \(s\), and use
constants independent of the choice of allowed fixed clipping.
For \(M\le M_*,\varepsilon\le1,\alpha\le1\), collecting the explicit
terms in (C.12)--(C.14) yields
\[
|B_n(s)-s c_n|\le C_{S,M_*}
(\varepsilon+\alpha s^2+s^3),\qquad 0\le s\le S.
\tag{C.15}
\]
For example, \(\alpha\varepsilon s\le S\varepsilon\),
\(\varepsilon^2s\le S\varepsilon\), and
\(\varepsilon s^2\le S^2\varepsilon\); every remaining term has one
of the two displayed time powers. Equations (C.2) bound all coefficients
uniformly under these restrictions.

### 3. Canonical initialization and the required initial law

The canonical initial blocks are mutually independent:
\[
z_i^{(1)}(0)\sim N(0,1),\quad
W_{ij}^{(\ell)}(0)\sim N(0,1/n)\ (\ell=2,3),\quad
W_i^{(4)}(0)=G_i^{(4)}/n,\quad G_i^{(4)}\sim N(0,1).
\tag{C.16}
\]
Independence and identical distribution here concern initialization
only, not trained or reused-matrix coordinate outputs.

Fragment I proves the following initialization law. For independent standard
Gaussians \(G_1,G_2,G_3,G\), put
\[
m_1=\mathbb E\phi(G_1)^2,\quad
Z^{(2)}=\sqrt{m_1}G_2,\quad m_2=\mathbb E\phi(Z^{(2)})^2,\quad
Z^{(3)}=\sqrt{m_2}G_3,
\]
\[
\beta=\frac{\mathbb E[Z^{(3)}g(Z^{(3)})]}{m_2},\qquad
\sigma^2=\mathbb E[g(Z^{(3)})^2],\qquad
c_*=\mathbb E\left[
\left[\phi''(Z^{(2)})(\beta\phi(Z^{(2)})+\sigma G)\right]_+\right].
\tag{C.17}
\]
Then \(m_1,m_2,\sigma,c_*>0\) and \(c_n\to c_*\) in probability
and in \(L^1\). The expectation in the last definition means expectation
of the positive part. The independent \(G\) describes unexplored
conditional Gaussian randomness in the reused hidden matrix, not a
change of the readout initialization.
The full proof, including its moment and positivity arguments, is in fragment I.

Here are the probability and integrability details for applying (C.14)
directly to (C.16). On the initial event
\[
\Omega_n=\{M\le10,\ \|G^{(4)}\|_2/\sqrt n\le2\},
\tag{C.18}
\]
one has \(\varepsilon\le2/n\), \(\alpha\le2/\sqrt n\).
For \(n\ge4\), (C.15) therefore gives
\[
|B_n(s)-s c_n|\le C_S
(n^{-1}+n^{-1/2}s^2+s^3),\quad 0\le s\le S,
\tag{C.19}
\]
on the same event for every allowed fixed clipping.
Moreover
\[
\mathbb P(\Omega_n^c)\le
4e^{-(25/2-2\log9)n}+e^{-(1-\frac12\log2)n}.
\tag{C.20}
\]
To check this directly, a maximal \(1/4\)-separated
spherical set is a \(1/4\)-net with at most \(9^n\) points by disjoint
radius-\(1/8\) ball packing. Approximate both arguments of a bilinear
form using this net; the two errors are at most half the operator norm,
so that norm is at most twice the net maximum. For a fixed pair of unit
vectors a canonical Gaussian matrix bilinear form has variance \(1/n\),
and its two-sided tail at \(r/2\) is at most \(2e^{-nr^2/8}\), by its
Gaussian exponential moment and Markov's inequality. Union over both
matrices and both nets gives
\[
\mathbb P(M>r)\le4e^{2n\log9-nr^2/8}.
\]
Use \(r=10\) for (C.20). For the readout,
\(\mathbb E e^{\|G^{(4)}\|_2^2/4}=2^{n/2}\);
Markov's inequality at squared norm \(4n\) gives its stated error.

For \(r\ge10\), the same matrix bound is at most \(4e^{-r^2/16}\);
tail integration thus bounds every fixed moment of \(M\) uniformly in
width. Differentiating the Gaussian squared-norm exponential moment
at zero gives, for integers \(k\ge1\),
\[
\mathbb E\varepsilon^{2k}
=n^{-3k}\prod_{j=0}^{k-1}(n+2j)\le C_k n^{-2k},\qquad
\mathbb E\alpha^{2k}\le n^k\mathbb E\varepsilon^{2k}
\le C_k n^{-k}.
\tag{C.21}
\]
Differentiation is justified by domination with a squared-norm
exponential moment at a fixed positive parameter less than \(1/2\).
All fixed moments of the polynomial constants in (C.2), (C.10) and (C.14)
are consequently uniformly bounded, using Cauchy--Schwarz for their
mixed moments.

For any such polynomial factor \(P\), Cauchy--Schwarz gives
\[
\mathbb E[|P|\varepsilon]\le C_S/n,\quad
\mathbb E[|P|\varepsilon^2]\le C_S/n^2,\quad
\mathbb E[|P|\alpha]\le C_S/\sqrt n.
\]
Also \(\alpha\varepsilon\le\sqrt n\,\varepsilon^2\) gives
\(\mathbb E[|P|\alpha\varepsilon]\le C_S n^{-3/2}\).
Apply these estimates to the unrestricted (C.12)--(C.14), not just on
\(\Omega_n\), to obtain
\[
\mathbb E|B_n(s)-s c_n|\le
C_S(n^{-1}+n^{-1/2}s^2+s^3),\qquad 0\le s\le S.
\tag{C.22}
\]
This holds uniformly over prescribed clippings, including any
measurably selected fixed clipping, because the same measurable
initial-data polynomial dominates (C.14). No uncountable supremum is
interchanged with expectation.

### 4. Actual positive-time consequences and their limits

Take \(S=1\), and let \(C_1\) be the deterministic constant in (C.19).
The initialization law’s \(c_*>0\) permits a fixed \(s_0\in(0,1]\) with
\(C_1s_0^2\le c_*/8\). For any fixed \(a\in(0,s_0]\), on the measurable
initial event \(\Omega_n\cap\{c_n\ge3c_*/4\}\), equation (C.19) gives
\[
\frac{B_n(s)}s\ge\frac{3c_*}{4}
-C_1(n^{-1}/a+n^{-1/2}s_0+s_0^2),
\qquad a\le s\le s_0.
\]
For all sufficiently large \(n\), depending on \(a\), the two
width-dependent terms times \(C_1\) sum to at most \(c_*/8\).
The event has probability tending to one. On it, simultaneously for
every allowed fixed clipping and every \(s\in[a,s_0]\),
\[
B_n(s)\ge\frac{c_*}{2}s.
\tag{C.23}
\]
This is an actual common positive interval after the width limit,
not a width-dependent Taylor neighborhood. It does not assert (C.23)
down to arbitrarily small \(s\) uniformly in \(n\).

The positive part is not carried by a vanishing fraction of middle
coordinates on these events. For \(S=1\), set
\[
D=2(1+c)[10+c(1+c/2)].
\]
Increasing the deterministic width threshold so that \(2/n\le a\),
(C.3)--(C.4) give for \(a\le s\le s_0\)
\[
\left(\frac1n\sum_i
|q_i^{(2)}(s)\phi''(z_i^{(2)}(s))|^2\right)^{1/2}
\le 2K_3(\varepsilon+cs)\le Ds.
\]
Let \(p_n(s)\) be the fraction of indices with
\(q_i^{(2)}(s)\phi''(z_i^{(2)}(s))\ge c_*s/4\).
The positive-part mean on its complementary indices is at most
\(c_*s/4\). Cauchy--Schwarz on the selected indices, together with
(C.23), therefore yields
\[
\frac{c_*s}{2}\le B_n(s)\le\frac{c_*s}{4}
+Ds\sqrt{p_n(s)},\qquad
p_n(s)\ge\left(\frac{c_*}{4D}\right)^2>0.
\tag{C.23a}
\]
This is simultaneous in the same time prefixes and allowed fixed
clippings. It is a positive fraction of scalar curvature coefficients,
not a claim about eigenvalues of a full parameter Hessian.

The expectation version follows with the explicit error:
\[
\mathbb E|B_n(s)-s c_*|
\le C_S(n^{-1}+n^{-1/2}s^2+s^3)+s\,\mathbb E|c_n-c_*|.
\tag{C.24}
\]
In particular, for each fixed \(s>0\),
\[
c_*s-C_Ss^3\le\liminf_{n\to\infty}\mathbb E B_n(s)
\le\limsup_{n\to\infty}\mathbb E B_n(s)\le c_*s+C_Ss^3.
\tag{C.25}
\]
The constants are uniform over allowed fixed clippings; (C.25) also
allows a prescribed width-dependent sequence of such maps.
Taking \(n\to\infty\) first and then \(s\downarrow0\) proves
\[
\lim_{s\downarrow0}\liminf_{n\to\infty}\frac{\mathbb E B_n(s)}s
=\lim_{s\downarrow0}\limsup_{n\to\infty}\frac{\mathbb E B_n(s)}s
=c_*>0.
\tag{C.26}
\]
Equation (C.25) alone does not assert convergence in \(n\) at fixed
positive time; its nonzero \(s^3\) error must not be discarded.

Consequently neither coordinatewise nonpositivity of the middle
coefficient nor a canonical mean positive-part bound of fifth order
can be obtained by transplanting the top-layer sign-lag argument.
For any fixed finite proposed coefficient of \(s^5\), choose a small
fixed \(s\le s_0\) where it is less than \(c_*s/2\); (C.23) contradicts
that bound with probability tending to one. The expectation version
is likewise contradicted by (C.25) for sufficiently small fixed \(s\).

This does not rule out a positive Gronwall constant, cancellation with
other signed work, or stronger actual response estimates. The coefficient's
positive part is not the Hessian quadratic form of an actual response.
No transported covariance bound, uniform tail envelope, population
restartability, full joint limit, or negative canonical resolution
is established here.

The clause concerning a measurably selected fixed clipping has a precise
interpretation. Give the set of 1-Lipschitz maps dominated by the identity the
compact-open metric \(\sum_{j\ge1}2^{-j}(1\wedge\sup_{|x|\le j}|\tau(x)-\nu(x)|)\).
At fixed width, finite initial data and finite horizon, the polynomial primal
bounds confine all solutions with nearby data to a common finite-dimensional
compact set. Their vector fields have a common local Lipschitz constant in
state and converge uniformly there when the maps converge compact-open.
Subtracting their integral equations and applying scalar Gronwall proves
continuous dependence on the data and map. Evaluations of all fields, and hence
the errors above, are measurable under a measurable selection of a map that is
then held fixed in time. The initial-data polynomial bounds already dominate
all those paths, so no supremum over random Gaussian events is required.


## E. Moderate-sine physical controls

#### E.1. Activation and exact finite model

Put

\[
 v=(1-e^{-8})/2-4e^{-4},\qquad N=\sqrt{1+4v/25},
\qquad \Phi(z)=az+b\sin(2z),
\]
\[
 a=(1-4e^{-2}/5)/N,\qquad b=2/(5N).
\]

For \(G\sim N(0,1)\), the Gaussian Fourier integral and its derivative give
\(\mathbb E\sin^2(2G)=(1-e^{-8})/2\) and
\(\mathbb E[G\sin(2G)]=2e^{-2}\). Hence \(v\) is the squared \(L^2\) norm
of \(\sin(2G)-2e^{-2}G\), which is orthogonal to \(G\) and is not zero.
Thus \(v>0\), \(N>1\), and writing
\(\Phi(G)=[G+(2/5)(\sin(2G)-2e^{-2}G)]/N\) also shows
\(\mathbb E\Phi(G)^2=1\). The exact derivatives are

\[
 \Phi'(z)=a+2b\cos(2z),\qquad
 \Phi''(z)=-4b\sin(2z).
\]

Since `e^2>4`,

\[
 0<m:=(1/5-4e^{-2}/5)/N\le\Phi'(z)<2,
 \qquad |\Phi''(z)|<2,
 \qquad \Phi(0)=0,\quad |\Phi(z)|\le2|z|.       \tag{E.1}
\]

No small coefficient or condition on the observation horizon is used in (E.1). The lemmas below in fact apply to any C2 activation with `phi(0)=0`, `||phi'||_infinity<=2` and `||phi''||_infinity<=2`; the lower slope is not needed for them. They hold for any input correlation in `[-1,1]`, so in particular for any fixed separated pair.

### 2. Raw norm and estimates on a primal ball

Use two fixed samples \((x_a,y_a)\), \(a=1,2\), with
\(x_a\in\mathbb R^d\), \(\|x_a\|_2^2=d\), \(y_a\in\{-1,1\}\), and any
\(\rho=x_1^Tx_2/d\in[-1,1]\). The activation above is used in all three hidden
layers. Write \(C=W^{(4)}\) for the stored finite readout and define
\[
 z_a^{(1)}=W^{(1)}x_a/\sqrt d,\quad
 z_a^{(2)}=W^{(2)}h_a^{(1)},\quad z_a^{(3)}=W^{(3)}h_a^{(2)},\quad
 h_a^{(\ell)}=\Phi(z_a^{(\ell)}),\quad f_a=C^Th_a^{(3)}/n,
 \quad r_a=f_a-y_a,
 \quad\mathcal L=(r_1^2+r_2^2)/2.
\]
The backward fields have no residual factor:
\[
 \delta_a^{(3)}=C\odot\Phi'(z_a^{(3)}),\quad
 q_a^{(2)}=(W^{(3)})^T\delta_a^{(3)},\quad
 \delta_a^{(2)}=\Phi'(z_a^{(2)})\odot q_a^{(2)},\quad
 q_a^{(1)}=(W^{(2)})^T\delta_a^{(2)},\quad
 \delta_a^{(1)}=\Phi'(z_a^{(1)})\odot q_a^{(1)}.
\]
All blocks train in physical time with unit multipliers and raw metric
\[
 \|d\Theta\|_{raw}^2=n^{-1}\|dW^{(1)}\|_F^2+
 \|dW^{(2)}\|_F^2+\|dW^{(3)}\|_F^2+n^{-1}\|dC\|_2^2.
\]
Thus the exact vector field \(V=-\nabla_{raw}\mathcal L\) is
\[
 \dot W^{(1)}=-\sum_{a=1}^2r_a\delta_a^{(1)}x_a^T/\sqrt d,\qquad
 \dot W^{(\ell)}=-\sum_{a=1}^2r_a\delta_a^{(\ell)}(h_a^{(\ell-1)})^T/n
 \quad(\ell=2,3),\qquad
 \dot C=-\sum_{a=1}^2r_ah_a^{(3)}.
\]
Raw GD means \(\Theta_{k+1}=\Theta_k+\eta_nV(\Theta_k)\),
\(\eta_n=n^{-2}\), simultaneously in these weights; weights are linearly
interpolated and all hidden fields are recomputed. No feature clock is used.
The canonical initialization has independent entries
\(W^{(1)}_{ij}\sim N(0,1)\), \(W^{(2)}_{ij},W^{(3)}_{ij}\sim N(0,1/n)\),
\(C_i\sim N(0,n^{-2})\), with independence between all blocks. Initial sample
preactivations are correlated according to \(\rho\), not independently
redrawn for the two samples.

All vector estimates below use the displayed Euclidean RMS factors. Suppose

\[
 \max_i\frac{\|z_i^{(1)}\|_2}{\sqrt n},\quad \|W^{(2)}\|_{op},\quad
 \|W^{(3)}\|_{op},\quad\frac{\|C\|_2}{\sqrt n}\le B,\qquad B\ge1.      \tag{E.2}
\]

The following bounds follow successively from (E.1):

| Field | Norm bound |
|---|---:|
| `h^{(1)}` | `2B` |
| `z^{(2)},h^{(2)}` | `2B^2,4B^2` |
| `z^{(3)},h^{(3)}` | `4B^3,8B^3` |
| `delta^{(3)},q^{(2)}` | `2B,2B^2` |
| `delta^{(2)},q^{(1)},delta^{(1)}` | `4B^2,4B^3,8B^3` |

Each table entry bounds the displayed field’s Euclidean norm divided by \(\sqrt n\), maximized over the two samples. Since the labels have modulus one,

\[
 \sum_i|r_i|\le16B^4+2\le18B^4.                  \tag{E.3}
\]

Let `V=-grad_raw L` be the actual physical vector field. Each of its four parameter blocks has raw norm at most `144B^7`, and hence

\[
 \|V\|_{raw}\le576B^7.                           \tag{E.4}
\]

For a middle block this uses

\[
 \|uh^T/n\|_F=\frac{\|u\|_2}{\sqrt n}\frac{\|h\|_2}{\sqrt n}.
\]

For the first block,

\[
 n^{-1/2}\|u x_i^T/\sqrt d\|_F=\|u\|_2/\sqrt n
\]

because `||x_i||^2=d`. Thus no dimension or width factor enters (E.4). The same argument applies to population fields, with Hilbert--Schmidt norms of the learned increments.

### 3. A dimension-explicit raw Lipschitz estimate

At width n, let two states both satisfy (E.2), and let `d_0` be their raw distance. Forward differences satisfy

\[
 \frac{\|\Delta z^{(1)}\|_2}{\sqrt n}\le d_0,\quad
 \frac{\|\Delta h^{(1)}\|_2}{\sqrt n}\le2d_0,\quad
 \frac{\|\Delta z^{(2)}\|_2}{\sqrt n}\le4Bd_0,\quad
 \frac{\|\Delta h^{(2)}\|_2}{\sqrt n}\le8Bd_0,
\]
\[
 \frac{\|\Delta z^{(3)}\|_2}{\sqrt n}\le12B^2d_0,\quad
 \frac{\|\Delta h^{(3)}\|_2}{\sqrt n}\le24B^2d_0,\quad
 \sum_i|\Delta r_i|\le64B^3d_0.                    \tag{E.5}
\]

For example,

`Delta z^{(2)}=W^{(2)} Delta h^{(1)}+Delta W^{(2)} h_tilde^1`,

and `||Delta W^{(2)}||op<=||Delta W^{(2)}||F<=d_0`. The last inequality in (E.5) uses

`|Delta f_i| <= (||Delta C||_2 ||h_i^{(3)}||_2 + ||C_tilde||_2 ||Delta h_i^{(3)}||_2)/n <=32B^3 d_0`.

For the backward gates, use

\[
 \frac{\|\Phi'(z)q-\Phi'(\widetilde z)\widetilde q\|_2}{\sqrt n}
 \le2\frac{\|q-\widetilde q\|_2}{\sqrt n}
       +2\frac{\|\widetilde q\|_\infty\|z-\widetilde z\|_2}{\sqrt n},
 \quad \|u\|_\infty\le\|u\|_2.
\]

Substitution of (E.5) and the field bounds gives, in causal order,

\[
 \frac{\|\Delta\delta^{(3)}\|_2}{\sqrt n}\le26\sqrt n B^3d_0,\quad
 \frac{\|\Delta q^{(2)}\|_2}{\sqrt n}\le28\sqrt n B^4d_0,\quad
 \frac{\|\Delta\delta^{(2)}\|_2}{\sqrt n}\le72\sqrt n B^4d_0,
\]
\[
 \frac{\|\Delta q^{(1)}\|_2}{\sqrt n}\le76\sqrt n B^5d_0,\quad
 \frac{\|\Delta\delta^{(1)}\|_2}{\sqrt n}\le160\sqrt n B^5d_0.         \tag{E.6}
\]

For instance the middle gate difference is at most

`2(28 sqrt(n) B^4)d_0 + 2(sqrt(n) 2B^2)(4B)d_0 <=72 sqrt(n) B^4 d_0`.

Expanding each rank-one update and its residual then gives respective raw block Lipschitz bounds

\[
 3392\sqrt n B^9,\quad3248\sqrt n B^9,\quad
 2672\sqrt n B^9,\quad944\sqrt n B^9.
\]

These four coefficients come respectively from
\(512+2880\), \(512+2592+144\), \(512+1872+288\), and \(512+432\):
the first summand in each case differentiates the residual, the second the
backward field (or the readout update's feature), and the third, when present,
the rank-one feature factor. For example the first-block bound is
\((64B^3)(8B^3)+(18B^4)(160\sqrt n B^5)
 \le3392\sqrt n B^9\).
Their sum is 10256. Consequently the conservative bound

\[
 \|V(\Theta)-V(\widetilde\Theta)\|_{raw}
 \le11000\sqrt n B^9\|\Theta-\widetilde\Theta\|_{raw}        \tag{E.7}
\]

holds whenever the two states satisfy (E.2). The primal set (E.2) is convex in the raw parameters, so the same bound controls the entire segment joining them. This is a finite-width estimate; its `sqrt(n)` factor is not dropped in a population argument.

### 4. Unconditional finite-time raw-GD energy

Fix an observation horizon T and an initialization with primal bounds at most `b_0>=1` and loss `E_0`. Put

\[
 R=\sqrt{2(T+1)E_0}+2,\qquad B=b_0+R+1,
 \qquad h=n^{-2}.
\]

Assume n is sufficiently large that

\[
 11000B^9n^{-3/2}\le1,\qquad576B^7n^{-2}\le1.      \tag{E.8}
\]

Then the actual simultaneous raw GD iterates through time T, and one additional endpoint if necessary, satisfy

\[
 \mathcal L(\Theta_k)\le E_0,\qquad
 \sum_{j<k}h\|V(\Theta_j)\|_{raw}^2\le2E_0,
\]
\[
 \|\Theta_k-\Theta_0\|_{raw}
 \le\sqrt{2khE_0}\le\sqrt{2(T+1)E_0}.             \tag{E.9}
\]

Proof. Stop provisionally before raw distance R from initialization. A raw displacement of size R changes either initial operator norm, the readout norm, or a first-layer sample norm by at most R, so (E.2) holds with room to spare. The second inequality in (E.8) and (E.4) keep the next Euler segment inside the larger primal ball B. Taylor's formula for the scalar loss and (E.7) give

\[
 \mathcal L(\Theta+hV)\le\mathcal L(\Theta)
      -h\|V\|_{raw}^2+\tfrac12(11000\sqrt n B^9)h^2\|V\|_{raw}^2
 \le\mathcal L(\Theta)-\tfrac12h\|V\|_{raw}^2.
\]

Summing proves the first two claims in (E.9). Cauchy--Schwarz for the sum of raw increments proves the third, which is strictly below R. This closes the induction and removes the stop. No population flow, tail bound, convergence theorem, or fixed-width comparison with continuous GF was assumed.

For the stated initialization one may take \(b_0=10\) and \(E_0\le2\)
on events with probability tending to one. For each sample, the first
preactivations are iid \(N(0,1)\) over neurons, so Chebyshev's inequality
applied to their squares proves RMS convergence to one; union over the two
samples suffices even when they are correlated. The sphere-net argument in
fragment S bounds both hidden operator norms by 10 with probability tending
to one. Also \(\mathbb E\|C_0\|_2^2/n=n^{-2}\), so its RMS vanishes in
probability. On the hidden-operator/first-field event, the field table bounds
\(\|h_a^{(3)}(0)\|_2/\sqrt n\) by a deterministic constant. Conditional on
these hidden fields, independence of \(C_0\) gives
\(\mathbb E[f_a(0)^2\mid h_a^{(3)}(0)]=\|h_a^{(3)}(0)\|_2^2/n^4=O(n^{-3})\).
Thus both predictions converge to zero in probability and \(E_0\to1\).
The initial hidden RMS bounds used below follow from the same field table.
For each fixed \(T\), (E.8)–(E.9) consequently hold with constants uniform in
width on events of probability tending to one.

This proves stable finite-horizon raw GD at the prescribed step; it does not identify its strong population limit.

### 5. Finite GF and weak path-law tightness

At every fixed width the finite-dimensional smooth vector field is locally Lipschitz. Its true gradient-flow energy identity is

\[
 \mathcal L(t)+\int_0^t\|\dot\Theta(s)\|_{raw}^2ds=E_0,
 \quad
 \|\Theta(t)-\Theta(0)\|_{raw}\le\sqrt{tE_0}.       \tag{E.10}
\]

It therefore cannot escape in finite time and is global. This is finite-dimensional existence only.

On any primal ball B, for a differentiable raw path write `s(t)=||dot Theta(t)||raw`. Successive forward differentiation gives

\[
 \frac{\|\dot z^{(1)}\|_2}{\sqrt n}\le s,\quad\frac{\|\dot h^{(1)}\|_2}{\sqrt n}\le2s,
 \quad\frac{\|\dot z^{(2)}\|_2}{\sqrt n}\le4Bs,\quad\frac{\|\dot h^{(2)}\|_2}{\sqrt n}\le8Bs,
\]
\[
 \frac{\|\dot z^{(3)}\|_2}{\sqrt n}\le12B^2s,\qquad
 \frac{\|\dot h^{(3)}\|_2}{\sqrt n}\le24B^2s.                        \tag{E.11}
\]

These inequalities hold almost everywhere also for linearly interpolated raw GD, with hidden fields recomputed from the interpolated parameters from the interpolated weights. Equations (E.9)-(E.11), together with initialized second-moment bounds, uniformly bound the average squared H1([0,T]) norm of the joint same-layer neuron paths \((z_{1,j}^{(\ell)},h_{1,j}^{(\ell)},z_{2,j}^{(\ell)},h_{2,j}^{(\ell)})\), \(j=1,\ldots,n\), for each \(\ell=1,2,3\).

Closed bounded H1 balls on a finite one-dimensional time interval have compact images in C([0,T]); this follows directly from the pointwise bound and the modulus `|x(t)-x(s)|<=sqrt(|t-s|)||x'||_L2`, and a diagonal subsequence on rational time points: the common modulus
upgrades convergence on that dense set to uniform convergence. The weak
lower-semicontinuity of the \(H^1\) norm keeps the limit inside the same ball. Markov's inequality for the empirical average H1 norm therefore gives tightness of the empirical path measures on \(C([0,T];\mathbb R^4)\) in
probability: on the same high-probability events, for every \(\varepsilon>0\)
a common compact set carries at least \(1-\varepsilon\) of each empirical
measure.

This is not W2 compactness: a bounded mean squared H1 norm does not by itself make squared path norms uniformly integrable. It does not identify a deterministic subsequential law, kernels, adjoints, or velocity laws.

### E.6. Strong endpoints on specified population action spaces

For this statement, suppose probability spaces \((\Omega_\ell,\mathcal A_\ell,
\mathbb P_\ell)\), \(\ell=1,2,3\), with separable real
\(\mathcal H_\ell=L^2(\Omega_\ell)\), and bounded initial operators
\(W_0^{(2)}:\mathcal H_1\to\mathcal H_2\),
\(W_0^{(3)}:\mathcal H_2\to\mathcal H_3\), are already specified.
They and their adjoints are fixed throughout. This conditional analytic result
does not construct Gaussian action spaces or identify them from finite width.
The complete affine raw state space is
\[
 \mathfrak X=L^2(\Omega_1;\mathbb R^d)\times
 HS(\mathcal H_1,\mathcal H_2)\times
 HS(\mathcal H_2,\mathcal H_3)\times\mathcal H_3,
\]
with state \(\Theta=(W^{(1)},M^{(2)},M^{(3)},W^{(4)})\),
\(W^{(\ell)}=W_0^{(\ell)}+M^{(\ell)}\) for \(\ell=2,3\), and product norm
using \(\mathbb E_1\|dW^{(1)}\|_{\mathbb R^d}^2\), the two squared HS norms,
and \(\mathbb E_3|dW^{(4)}|^2\). Population fields are
\[
 Z_a^{(1)}=W^{(1)}x_a/\sqrt d,\quad
 Z_a^{(\ell)}=W^{(\ell)}H_a^{(\ell-1)},\quad H_a^{(\ell)}=\Phi(Z_a^{(\ell)}),
 \quad f_a=\mathbb E_3[W^{(4)}H_a^{(3)}],
\]
\[
 \Delta_a^{(3)}=W^{(4)}\Phi'(Z_a^{(3)}),\quad
 Q_a^{(\ell)}=(W^{(\ell+1)})^*\Delta_a^{(\ell+1)},\quad
 \Delta_a^{(\ell)}=\Phi'(Z_a^{(\ell)})Q_a^{(\ell)}
 \quad(\ell=1,2).
\]
Products of fields are pointwise within the indicated layer. The physical
field is the negative raw gradient of \(\mathcal L=(r_1^2+r_2^2)/2\):
\[
 \dot W^{(1)}=-\sum_ar_a\Delta_a^{(1)}x_a^T/\sqrt d,\quad
 \dot M^{(\ell)}=-\sum_ar_a\Delta_a^{(\ell)}\otimes H_a^{(\ell-1)},\quad
 \dot W^{(4)}=-\sum_ar_aH_a^{(3)}.
\]
Here \((U\otimes H)g=U\mathbb E_{\ell-1}[Hg]\). Its HS norm is
\(\|U\|_{L^2(\Omega_\ell)}\|H\|_{L^2(\Omega_{\ell-1})}\).
The theorem permits any initial state in this affine space. In particular it
applies to an existing canonical strong flow with Gaussian first mark and zero
limiting readout, if its action spaces have been constructed; it does not replace
the finite tiny Gaussian readout by zero in a convergence theorem.

**Continuity and the scalar chain rule.** The fields just displayed and their
raw vector field are continuous in the raw norm and are polynomially bounded
on every bounded raw set. Forward continuity follows from the global
Lipschitz bound for \(\Phi\), operator continuity, and
\(\|M\|_{op}\le\|M\|_{HS}\). For the only nontrivial backward step,
if \((Z_j,Q_j)\to(Z,Q)\) in \(L^2\times L^2\),
\[
 \|\Phi'(Z_j)Q_j-\Phi'(Z)Q\|_{L^2}
 \le2\|Q_j-Q\|_{L^2}
   +\|[\Phi'(Z_j)-\Phi'(Z)]Q\|_{L^2}\longrightarrow0.       \tag{E.12}
\]
The second term converges by convergence in measure, continuity and boundedness
of \(\Phi'\), and integrability of \(16Q^2\): every subsequence admits an
a.e. convergent subsubsequence to which dominated convergence applies. Backward
induction and continuity of rank-one maps into HS prove the assertion.

The scalar prediction is continuously Fréchet differentiable with the displayed
backpropagation formula even though the full activation map need not be
Fréchet differentiable \(L^2\to L^2\). For fixed \(Q\in L^2\), Taylor's formula
and the two derivative bounds give
\[
 |\Phi(Z+U)-\Phi(Z)-\Phi'(Z)U|\le\min(|U|^2,4|U|).
\]
Pair the remainder with \(Q\). On \(|Q|\le K\) its integral is at most
\(K\|U\|_{L^2}^2\), and on the complement it is at most
\(4\|Q\mathbf1_{|Q|>K}\|_{L^2}\|U\|_{L^2}\). Divide by \(\|U\|_{L^2}\),
first send \(U\to0\) with \(K\) fixed, then send \(K\to\infty\).
To telescope layers explicitly, replace the top activation increment by its
linear term paired with the fixed current readout; pass the fixed linear term
through \((W^{(3)})^*\), repeat at layer two, then at layer one.
Each preactivation increment is \(O(\|d\Theta\|_{raw})\). Terms involving a
perturbed operator times a perturbed field are \(O(\|d\Theta\|_{raw}^2)\),
as is the perturbed-readout/perturbed-feature pairing. This accounts for every
remainder and gives the stated derivative; (E.12) makes it continuous.
The scalar loss is therefore \(C^1\) with gradient \(-V\).

**Strong endpoint theorem.** Let \(\Theta\) be an already existing strong
physical solution \(\dot\Theta=V(\Theta)\) on \([0,T_*)\), \(T_*<\infty\),
in the stated complete affine Hilbert space. Here a strong solution is a
norm-continuous, locally absolutely continuous path satisfying the equation
a.e.; continuity of \(V\) then makes it \(C^1\). The scalar chain rule gives
\[
 \mathcal L(\Theta(t))+\int_0^t\|V(\Theta(u))\|_{raw}^2du
 =\mathcal L(\Theta(0)).
\]
Thus for \(s<t<T_*\),
\[
 \|\Theta(t)-\Theta(s)\|_{raw}
 \le\sqrt{(t-s)[\mathcal L(\Theta(s))-\mathcal L(\Theta(t))]}.
                                                               \tag{E.13}
\]
The nonnegative decreasing loss has a limit; this inequality makes the path
Cauchy at \(T_*\). Completeness gives \(\Theta_*\in\mathfrak X\).
Continuity of \(V\) and of all field maps proves
\[
 \Theta(t)\to\Theta_*\text{ in raw norm},\qquad
 V(\Theta(t))\to V(\Theta_*)\text{ in raw norm}.                 \tag{E.14}
\]
Every \(Z,H,Q,\Delta\) converges strongly in its indicated \(L^2\) space.
For any converging probe \(g_t\to g_*\) in the domain of an action,
\[
 \|W(t)g_t-W_*g_*\|\le\|W(t)\|_{op}\|g_t-g_*\|
                  +\|M(t)-M_*\|_{HS}\|g_*\|\to0,
\]
and the identical inequality for adjoints gives both orientations. Integrating
the convergent velocity proves that the extension at \(T_*\) is differentiable
from the left with derivative \(V(\Theta_*)\).

Each extended incoming-field path has compact image in \(L^2\). Hence, for
every one of the finitely many sample/layer incoming fields,
\[
 \lim_{R\to\infty}\sup_{0\le t\le T_*}
 \|Q(t)\mathbf1_{|Q(t)|>R}\|_{L^2}=0.                         \tag{E.15}
\]
Indeed cover the compact image by finitely many balls of radius \(\varepsilon\)
centered at fields \(F\). The inequality
\(\|Q\mathbf1_{|Q|>R}\|_{L^2}
 \le2\|Q-F\|_{L^2}+2\|F\mathbf1_{|F|>R/2}\|_{L^2}\)
follows by splitting at \(|F|>R/2\). Send \(R\to\infty\) for the finitely
many centers and then \(\varepsilon\to0\). This is a qualitative tail bound
for this one existing path, with no uniform rate over widths or restarts.

### E.7. Exact limitation of the endpoint theorem

Bounded positive slope does not make the ambient backward multiplication map
locally Lipschitz. On a standard Gaussian probability space take \(Z=Q=G\)
and \(\mathcal B(Z,Q)=\Phi'(Z)Q\). Choose disjoint fixed-length intervals
\(I_j\) tending to positive infinity, inside regions where \(\sin(2z)\ge3/4\).
A fixed sufficiently small \(u>0\) keeps every segment \([z,z+u]\),
\(z\in I_j\), inside a region where \(\sin(2z)\ge1/2\).
Set \(E_j=\{G\in I_j\}\) and \(Z_j=G+u\mathbf1_{E_j}\). The mean-value theorem
and \(\Phi''=-4b\sin(2z)\) give
\[
 \|\mathcal B(Z_j,G)-\mathcal B(G,G)\|_{L^2}
 \ge2b(\inf I_j)u\mathbb P(E_j)^{1/2},\qquad
 \|Z_j-G\|_{L^2}=u\mathbb P(E_j)^{1/2}\to0.
\]
Their ratio diverges. This is an ambient continuity-versus-Lipschitz example;
it makes no claim that the perturbations are generated network trajectories.

The endpoint theorem establishes neither local existence nor uniqueness from
\(\Theta_*\) in the infinite-dimensional space. A continuation and finite-width
identification theorem still needs a quantitative response/tail estimate at
reached states with the same retained Gaussian histories. Neither (E.15), the
finite GD energy inequality, nor weak path-law tightness supplies that estimate.
