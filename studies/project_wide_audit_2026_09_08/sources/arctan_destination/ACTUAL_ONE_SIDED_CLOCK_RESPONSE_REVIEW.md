# Independent adversarial audit: ACTUAL_ONE_SIDED_CLOCK_RESPONSE

## Verdict and audited inputs

**PASS as a finite-width response lemma. No required mathematical corrections.**
The candidate's one-sided estimate controls every expanding singular value at every finite physical time on one initialization event. Its two-sided estimate correctly excludes only the smallest singular value. The transformed-coordinate and conditional Gaussian covariance normalizations are correct. The added untrimmed regularized increment bounds (8a) and (8b) also pass. The full square physical propagator necessarily develops an unbounded contracting logarithm on this event. None of these statements establishes a global population theorem or a width-uniform response-amplitude bound.

I read /etc/codex/skills/solve-math-rigorously/SKILL.md and the complete five mathematical files below. The mathematical input directory was exclusively:

/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/

No ledgers, reviews, other candidates, other agent files, parent history, or additional mathematical dependencies were consulted. References to other files inside these inputs were not followed. No numerical experiments or external writes were performed. The sole output is this review; the candidate and dependencies were not edited.

The SHA256 values below identify the exact inputs. The candidate was revised during the audit; I reread its complete current 254-line version, including (8a) and (8b), and verified the user-supplied current hash. This review supersedes assessment of the earlier 221-line version and certifies only the current candidate below. The four dependency hashes remained unchanged.

| Input | Lines | Bytes | SHA256 |
| --- | ---: | ---: | --- |
| ACTUAL_ONE_SIDED_CLOCK_RESPONSE.md | 254 | 10207 | f5d813af3bb195ba6b5d1829f02556d6a57bf803e3f1d9b883ad3983929e4b5c |
| ACTUAL_SQUARED_LOG_RESPONSE.md | 347 | 10973 | d416464bf1b5e4a792bb6937f0f7eec0e5d19cd70ca05816d02f011bf64547f0 |
| ACTUAL_CLOCK_RANK_ONE_RESPONSE.md | 194 | 8288 | a3e093852f07d58b474197fd4781dfb69830203a21eda7e788d45af27f28f0bd |
| ACTUAL_LOG_RESPONSE_METRIC_TRANSFER.md | 171 | 6553 | 29304fb9771653257d3d638908ad4a08aca60690ce3ff4a9f2edfe73bf4bca0e |
| READOUT_COERCIVITY.md | 422 | 14558 | 0bd062da74fbde03d41a125561beee7345915ea6aa0578ed8e7b81d2c9f08c53 |

The argument below rederives the premises used from the dependencies. Their status language is not evidence for this verdict. All singular values are in decreasing order and all logarithms are natural.

## 1. The actual finite-width field and its metric

Write \(c=W^{(4)}\), \(a=\pi/2\), and
\[
\theta=(z^{(1)},\sqrt nW^{(2)},\sqrt nW^{(3)},c)
\in\mathbb R^N,\qquad N=2n^2+2n.
\]
The forward variables are the ones in the inputs, with \(\phi=\arctan\), and
\[
\mathcal P(\theta)=c^Th^{(3)}=nf,\qquad
b=\nabla_\theta\mathcal P.
\]
Direct differentiation gives the four blocks
\[
b=\left(\delta^{(1)},
 \frac{\delta^{(2)}(h^{(1)})^T}{\sqrt n},
 \frac{\delta^{(3)}(h^{(2)})^T}{\sqrt n},
 h^{(3)}\right).
\]
Thus the feature equation in these coordinates is \(\theta_s=b\).
Dividing the matrix-coordinate equations by \(\sqrt n\) gives exactly
\[
z^{(1)}_s=\delta^{(1)},\quad
W^{(2)}_s=\delta^{(2)}(h^{(1)})^T/n,\quad
W^{(3)}_s=\delta^{(3)}(h^{(2)})^T/n,\quad c_s=h^{(3)}.
\]
There is no mismatch between the raw Euclidean Hessian and the canonical parameter metric. In particular,
\[
\nabla_\theta f=b/n,\qquad
f_s=\|b\|_2^2/n=:\kappa.
\]
The physical equation specified by this model is
\[
\theta_t=\alpha b,\qquad \alpha=2(1-f).
\]
It is the squared-loss gradient flow in the canonical normalized parameter metric. Calling it the ordinary unrescaled Euclidean gradient flow of the loss in \(\theta\) would introduce a factor \(n\); the inputs do not make that substitution.

All these fields are smooth on the entire finite-dimensional parameter space. The finite-dimensional ODE facts needed below are local existence and uniqueness for locally Lipschitz fields, smooth dependence for smooth fields, and extension of a solution that stays bounded on each finite time interval. Here smoothness follows from \(\arctan\) and finite sums and products. The bounds in the next section verify the required extension hypotheses.

## 2. Independent reconstruction of the all-time primal event

This verifies the material taken from READOUT_COERCIVITY.md, especially lines 176–306 and 346–392, and the constants in ACTUAL_CLOCK_RANK_ONE_RESPONSE.md, lines 118–128.

### 2.1 Global feature existence and positive readout acceleration

Let \(\epsilon=\|c(0)\|_2/\sqrt n\), and initially let
\(M_j=\|W^{(j)}(0)\|_{\rm op}\). Since \(|\phi|\le a\) and
\(|\phi'|\le1\),
\[
\|c(s)\|_2/\sqrt n\le\epsilon+as,
\]
\[
\|W^{(3)}(s)\|_{\rm op}
\le M_3+a\epsilon s+a^2s^2/2=:\mathcal M_3(s),
\]
\[
\|W^{(2)}(s)\|_{\rm op}
\le M_2+a\int_0^s\mathcal M_3(u)(\epsilon+au)\,du
=:\mathcal M_2(s).
\]
The identical integrands bound the Frobenius norms of the matrix increments, because a rank-one update \(uv^T/n\) has Frobenius norm \(\|u\|\|v\|/n\). Also
\[
\frac{\|z^{(1)}(s)-z^{(1)}(0)\|_2}{\sqrt n}
\le\int_0^s\mathcal M_2(u)\mathcal M_3(u)(\epsilon+au)\,du.
\]
These are finite on every bounded feature interval. At each fixed \(n\), every parameter coordinate is therefore bounded there, proving global forward feature existence.

Put \(D_\ell=\operatorname{diag}(\phi'(z^{(\ell)}))\) and
\[
A_2=\frac{\|h^{(1)}\|^2}{n}I+W^{(2)}D_1^2(W^{(2)})^T,
\]
\[
A_3=\frac{\|h^{(2)}\|^2}{n}I+
W^{(3)}D_2A_2D_2(W^{(3)})^T.
\]
Both are positive semidefinite. Differentiating the forward equations,
\[
z^{(2)}_s=A_2\delta^{(2)},\qquad
z^{(3)}_s=A_3\delta^{(3)},\qquad
c_{ss}=h^{(3)}_s=Lc,\quad L=D_3A_3D_3\succeq0.
\]
For example, the trained \(W^{(3)}\) contribution to \(z^{(3)}_s\) is
\(\|h^{(2)}\|^2\delta^{(3)}/n\); propagation through the trained lower layers gives the other term in \(A_3\). Both trained matrices are retained.

Consequently
\[
\kappa=\frac{\|h^{(3)}\|^2+c^TLc}{n}
=\frac{\|h^{(3)}\|^2}{n}
 +\frac{\|\delta^{(3)}\|^2\|h^{(2)}\|^2}{n^2}
 +\frac{\|\delta^{(2)}\|^2\|h^{(1)}\|^2}{n^2}
 +\frac{\|\delta^{(1)}\|^2}{n}.
\]
For \(\rho(s)=\|c(s)\|/\sqrt n>0\),
\[
\rho'=\frac{c^Th^{(3)}}{n\rho},\qquad
\rho''=\frac{\|h^{(3)}\|^2/n-(\rho')^2+c^TLc/n}{\rho}\ge0.
\]
The last sign uses Cauchy–Schwarz and \(L\succeq0\). It does not require coordinatewise positivity of any backward field.

### 2.2 Small nonzero readout, including possible early zeros

Suppose \(\|h^{(3)}(0)\|/\sqrt n\ge b_0>0\), with \(b_0\le a\).
Use the constants in the dependency, writing its short feature time as \(\tau\) to avoid confusion with a starting physical time:
\[
L_3=M_3+a+a^2/2,\qquad
L_2=M_2+aL_3(1+a/2),
\]
\[
B_*=a^2+L_3^2(a^2+L_2^2),\qquad
\tau=\min\{1,\sqrt{b_0/(8aB_*)}\},\qquad
\epsilon_0=\min\{1,b_0\tau/16\}.
\]
For \(\epsilon\le\epsilon_0\), the preceding polynomial estimates imply
\(\|L(s)\|_{\rm op}\le B_*\) on \([0,1]\). Twice integrating \(c_{ss}=Lc\) gives
\[
\frac{\|h^{(3)}(s)-h^{(3)}(0)\|}{\sqrt n}
\le B_*(\epsilon s+as^2/2),
\]
\[
\frac{\|c(s)-c(0)-s h^{(3)}(0)\|}{\sqrt n}
\le B_*(\epsilon s^2/2+as^3/6).
\]
Here \(\epsilon\le a\tau\) and \(B_*a\tau^2\le b_0/8\), so
\[
\frac{\|h^{(3)}(s)-h^{(3)}(0)\|}{\sqrt n}\le3b_0/16
\quad(0\le s\le\tau),
\]
\[
\frac{\|c(\tau)-\tau h^{(3)}(0)\|}{\tau\sqrt n}
\le b_0/16+(2/3)B_*a\tau^2
\le7b_0/48.
\]
In particular \(c(\tau)\ne0\). For nonzero \(x\),
\[
\frac{x^Ty}{\|x\|}\ge\|x\|-\|x-y\|
\ge\|y\|-2\|x-y\|.
\]
Apply this with \(x=c(\tau)/(\tau\sqrt n)\) and
\(y=h^{(3)}(0)/\sqrt n\), and bound the change in \(h^{(3)}\), to obtain
\[
\rho'(\tau)\ge b_0-2(7b_0/48)-3b_0/16=25b_0/48>b_0/2.
\]
On the connected interval after \(\tau\) where \(\rho>0\), convexity makes \(\rho'\) positive and nondecreasing. Hence
\(\rho(s)\ge\rho(\tau)+(25b_0/48)(s-\tau)>0\), ruling out any later zero. Since
\(\|h^{(3)}(s)\|/\sqrt n\ge|\rho'(s)|\), this proves
\[
\frac{\|h^{(3)}(s)\|}{\sqrt n}\ge b_0/2,\qquad
\kappa(s)\ge k_0:=b_0^2/4\qquad(s\ge0).
\]
An early zero of \(c\) before \(\tau\) does not invalidate this proof: the estimates on \([0,\tau]\) never divide by \(\rho\). The zero-readout special case is also consistent, but is not used to replace the actual nonzero Gaussian initialization.

### 2.3 Physical clock, endpoint, and uniform displacement

The same smallness gives \(|f(0)|\le a\epsilon_0\le a^2/16<1\).
Set \(e_0=1-f(0)>0\). Since \(f_s=\kappa\ge k_0\), there is a unique
\[
0<s_*\le e_0/k_0,\qquad f(s_*)=1.
\]
The scalar clock \(s_t=2(1-f(s)),\ s(0)=0\) remains in \([0,s_*)\).
One way to verify the strict finite-time inequality is to differentiate
\(e(t)=1-f(s(t))\):
\[
e'(t)=-2\kappa(s(t))e(t),\qquad
e(t)=e_0\exp\left(-2\int_0^t\kappa(s(v))\,dv\right)>0.
\]
The integrand is continuous and bounded on the compact feature segment
\([0,s_*]\). This both prevents reaching \(s_*\) in finite physical time and gives global physical existence. Moreover,
\[
\frac{\alpha(t)}{\alpha(0)}=\frac{e(t)}{e_0}\le e^{-2k_0t},
\qquad s(t)\uparrow s_*.
\]
For the latter limit, any limit strictly below \(s_*\) would leave \(s_t\) bounded below by a positive constant.

In raw coordinates the action identity is
\[
\int_0^s\frac{\|\theta_u\|^2}{n}\,du=f(s)-f(0).
\]
Cauchy–Schwarz therefore gives, for \(0\le s\le s_*\),
\[
\frac{\|\theta(s)-\theta(0)\|^2}{n}
\le s[f(s)-f(0)]\le e_0^2/k_0.
\]
The left side is exactly the sum of the normalized squared vector displacements and the unnormalized squared Frobenius matrix displacements in READOUT_COERCIVITY.md. Thus it bounds both hidden operator increments as well.

With \(e_{\max}=1+a\epsilon_0\), define
\[
d_*=\frac{2e_{\max}}{b_0},\qquad
M=10+d_*,\quad R=\epsilon_0+d_*,\quad
S_*=\frac{4e_{\max}}{b_0^2},\quad R_1=2+d_*.
\]
Whenever the initial hidden operator norms are at most 10 and
\(\|z^{(1)}(0)\|/\sqrt n\le2\), these imply simultaneously on the entire reached feature segment, including its endpoint,
\[
\|W^{(2)}\|_{\rm op},\|W^{(3)}\|_{\rm op}\le M,\quad
\|c\|/\sqrt n\le R,\quad
\|z^{(1)}\|/\sqrt n\le R_1,\quad s_*\le S_*.
\]
These are precisely the constants needed by the candidate.

### 2.4 One Gaussian initialization event, before choosing times or subspaces

Define \(q(v)=\mathbb E[\arctan(\sqrt v\,G)^2]\) for \(v\ge0\) and
\(G\sim N(0,1)\). It is continuous by bounded convergence. Let
\(m_1=q(1)\), \(m_2=q(m_1)\), \(m_3=q(m_2)\), all strictly positive, and fix
\(b_0=\sqrt{m_3}/2\). Here \(m_3\) is the deterministic Gaussian constant, not a random empirical moment.

For the prescribed independent initialization, the first-layer empirical squared activation converges to \(m_1\). Conditional on \(h^{(1)}(0)\), the second-layer preactivations are independent centered Gaussians with variance
\(\|h^{(1)}(0)\|^2/n\). Their empirical squared activation has conditional variance at most \(a^4/n\) and conditional mean \(q(\|h^{(1)}(0)\|^2/n)\). Conditional Chebyshev and continuity of \(q\) give convergence in probability to \(m_2\). The same argument applies at layer three because \(W^{(3)}(0)\) is independent of \(h^{(2)}(0)\). Hence
\(\|h^{(3)}(0)\|^2/n\to m_3\), proving the required initial lower bound with probability tending to one.

For completeness, the operator-norm bound used in the dependency also has the claimed constants. A maximal \(1/4\)-separated subset of the unit sphere is a \(1/4\)-net with at most \(9^n\) points, by comparing the volumes of disjoint radius-\(1/8\) balls inside the radius-\(9/8\) ball. Approximating each of two unit vectors by net points changes its bilinear form by at most \(\|W\|_{\rm op}/2\). Thus
\(\|W\|_{\rm op}\le2\max_{u,v\text{ in nets}}|u^TWv|\).
Each fixed form is \(N(0,1/n)\), since the sum of the squared coefficients \(u_iv_j\) is one. Its Gaussian tail, obtainable from
\(\mathbb E e^{tG}=e^{t^2/2}\), yields
\[
\Pr(\|W\|_{\rm op}>M_0)\le
2\,9^{2n}e^{-nM_0^2/8}.
\]
At \(M_0=10\), this tends to zero. Also
\[
\mathbb E[\|c(0)\|^2/n]=n^{-2},\qquad
\Pr(\|c(0)\|/\sqrt n>\epsilon_0)\le n^{-2}/\epsilon_0^2.
\]
This Gaussian readout is nonzero with probability one. Finally,
\(\|z^{(1)}(0)\|^2/n\to1\), so the bound by \(2\sqrt n\) has probability tending to one.

Let \(\Omega_n\) be the intersection of these initial bounds (and, if desired, the probability-one nonzero-readout condition). Then
\(\Pr(\Omega_n)\to1\). Every conclusion in Sections 2.1–2.3 is deterministic on \(\Omega_n\). The constants are fixed before \(n\), times, or isometries are chosen. This is the required all-physical-time event, not a family of events for separate horizons.

## 3. Independent check of the raw Hessian and velocity bounds

This checks ACTUAL_SQUARED_LOG_RESPONSE.md, lines 103–193 and 255–260.
Let \(x\) denote the first three raw blocks. For a hidden variation
\(u=(u_1,E_2,E_3)\), the preactivation derivatives are
\[
T_1u=u_1,\qquad
T_2u=E_2h^{(1)}/\sqrt n+W^{(2)}D_1u_1,
\]
\[
T_3u=E_3h^{(2)}/\sqrt n+W^{(3)}D_2T_2u.
\]
The bounds \(\|h^{(\ell)}\|/\sqrt n\le a\) imply
\[
\|T_1\|_{\rm op}=1,\quad
\|T_2\|_{\rm op}\le K_2:=a+M,\quad
\|T_3\|_{\rm op}\le K_3:=a+MK_2.
\]
The derivative \(J=D_xh^{(3)}=D_3T_3\) has rank at most \(n\) and
\(\|J\|_{\rm op}\le K_3\).

Define \(S_2u=E_2^T\delta^{(2)}/\sqrt n\) and
\(S_3u=E_3^T\delta^{(3)}/\sqrt n\). Then
\[
\|q^{(1)}\|\le M^2R\sqrt n,\quad
\|q^{(2)}\|\le MR\sqrt n,\quad
\|S_2\|_{\rm op}\le MR,\quad \|S_3\|_{\rm op}\le R.
\]
Twice differentiating \(c^Th^{(3)}\) in the hidden variables gives
\[
\begin{aligned}
A_x:=D_x^2(c^Th^{(3)})
={}&T_1^T\operatorname{diag}(\phi''(z^{(1)})q^{(1)})T_1\\
&+T_2^T\operatorname{diag}(\phi''(z^{(2)})q^{(2)})T_2\\
&+T_3^T\operatorname{diag}(\phi''(z^{(3)})c)T_3\\
&+S_2^TD_1T_1+T_1^TD_1S_2\\
&+S_3^TD_2T_2+T_2^TD_2S_3.
\end{aligned}
\]
Products inside a diagonal are coordinatewise. The cross terms arise from
\[
d^2z^{(2)}[u,u]=2E_2D_1u_1/\sqrt n+
W^{(2)}[\phi''(z^{(1)})u_1^2]
\]
and
\[
d^2z^{(3)}[u,u]=2E_3D_2T_2u/\sqrt n+
W^{(3)}[\phi''(z^{(2)})(T_2u)^2+D_2d^2z^{(2)}[u,u]].
\]
Thus none of the trained-matrix terms is omitted.

Using \(|\phi''|\le2\) and
\(\|T^TDT\|_{\rm F}\le\|T\|_{\rm op}^2\|D\|_{\rm F}\), the three diagonal terms cost respectively
\[
2M^2R\sqrt n,\quad2K_2^2MR\sqrt n,\quad2K_3^2R\sqrt n.
\]
Each cross map has rank at most \(n\); the inequality
\(\|C\|_{\rm F}\le\sqrt{\operatorname{rank}C}\|C\|_{\rm op}\)
therefore bounds the two symmetric pairs by
\(2MR\sqrt n\) and \(2RK_2\sqrt n\).
Finally,
\[
Db=\begin{pmatrix}A_x&J^T\\J&0\end{pmatrix},\qquad
\left\|\begin{pmatrix}0&J^T\\J&0\end{pmatrix}\right\|_{\rm F}
=\sqrt2\|J\|_{\rm F}\le\sqrt{2n}K_3.
\]
The triangle inequality proves exactly
\[
\|Db\|_{\rm F}\le C_B\sqrt n,\qquad
C_B=2R(M^2+MK_2^2+K_3^2+M+K_2)+\sqrt2K_3.
\]
The four explicit blocks of \(b\) also give
\[
\frac{\|b\|^2}{n}\le
M^4R^2+a^2M^2R^2+a^2R^2+a^2=:K_b^2.
\]
Only Euclidean norms of \(c,q^{(1)},q^{(2)}\) were used. No maximum-coordinate backward-field hypothesis has entered.

## 4. Positive-log trace differentiation, including the threshold and multiplicities

This checks candidate lines 29–79. The variational generators here are continuous, indeed smooth along the finite-width trajectories, so \(V'=DV\) gives a \(C^1\) matrix path. A square fundamental solution \(U\) is invertible at each finite time: the solution of \(W'=-WD,\ W(t_0)=I\) satisfies \((WU)'=0\), so \(WU=I\). Consequently \(V=UV_0\) retains full column rank for every full-column-rank \(V_0\).

Set \(G=V^TV\), \(Q=VG^{-1/2}\). On any compact finite time interval,
\(G\) is positive definite with its spectrum in a compact interval
\([\ell,L]\subset(0,\infty)\), and \(Q^TQ=I_m\). Let
\[
g(\lambda)=\tfrac14(\log\lambda)_+^2.
\]
For \(\lambda<1\), \(g'=0\); for \(\lambda>1\),
\(g'(\lambda)=\log\lambda/(2\lambda)\). At \(\lambda=1\), the right difference quotient tends to zero because
\((\log(1+h))^2/h\to0\); the left quotient is zero. Hence
\[
g\in C^1((0,\infty)),\qquad
g'(\lambda)=\frac{(\log\lambda)_+}{2\lambda}
\]
also at 1. A second derivative at 1 is not needed.

Here is a complete justification of the trace identity without choosing differentiable eigenvectors. The scalar approximation fact required is that a continuous function on a compact interval admits uniformly approximating polynomials. It can be seen by rescaling to \([0,1]\) and using Bernstein polynomials: for a continuous \(h\), their value at \(x\) is \(\mathbb E[h(K/k)]\), where \(K\) is binomial with parameters \(k,x\). Uniform continuity and
\(\Pr(|K/k-x|>\delta)\le1/(4k\delta^2)\) prove uniform approximation. Apply this to \(g'\) on \([\ell,L]\), obtaining \(p_k\to g'\) uniformly, and define primitives \(g_k\) agreeing with \(g\) at a fixed point. Then
\[
\sup_{[\ell,L]}|g_k-g|
\le (L-\ell)\sup_{[\ell,L]}|p_k-g'|\longrightarrow0.
\]
For a matrix monomial, the product rule and cyclicity give
\[
\frac{d}{dt}\operatorname{Tr}G^r
=\sum_{j=0}^{r-1}\operatorname{Tr}(G^jG'G^{r-1-j})
=r\operatorname{Tr}(G^{r-1}G').
\]
Therefore polynomial trace differentiation and integration give
\[
\operatorname{Tr}g_k(G(t))-\operatorname{Tr}g_k(G(t_0))
=\int_{t_0}^t\operatorname{Tr}[p_k(G(u))G'(u)]\,du.
\]
The endpoint trace errors are bounded by \(m\sup|g_k-g|\).
The integral error is bounded by
\[
m\sup|p_k-g'|\int_{t_0}^t\|G'(u)\|_{\rm op}\,du\longrightarrow0.
\]
Polynomial approximation also shows that \(g'(G(u))\) is continuous in \(u\). Thus the limiting integral has a continuous integrand, and differentiating it proves
\[
\frac{d}{dt}\operatorname{Tr}g(G)
=\operatorname{Tr}[g'(G)G'].
\]
This argument is valid at any repeated eigenvalue, including repeated eigenvalues equal to 1, and at crossings through 1.

Since
\[
G'=2V^TD_{\rm sym}V
=2G^{1/2}Q^TD_{\rm sym}QG^{1/2},
\]
and \(G\) commutes with its own spectral functions, cyclicity now gives
\[
\mathcal E_+'=\operatorname{Tr}[(\log G)_+Q^TD_{\rm sym}Q].
\]
This is candidate (1), with all factors of two accounted for:
\(\|(\log G)_+\|_{\rm F}=2\sqrt{\mathcal E_+}\).

For \(D_{\rm sym}=A-P\), \(A=A^T\), \(P\succeq0\), put
\(X=Q(\log G)_+Q^T\succeq0\). Then
\(\operatorname{Tr}(XP)=\operatorname{Tr}(P^{1/2}XP^{1/2})\ge0\), even without commutation. Also multiplication by \(Q,Q^T\), which have operator norm one, cannot increase Frobenius norm. Hence
\[
\mathcal E_+'\le
\operatorname{Tr}[(\log G)_+Q^TAQ]
\le2\sqrt{\mathcal E_+}\,\|A\|_{\rm F}.
\]
For every \(\varepsilon>0\),
\[
\frac{d}{dt}\sqrt{\mathcal E_++\varepsilon}
\le\frac{\sqrt{\mathcal E_+}}{\sqrt{\mathcal E_++\varepsilon}}
\|A\|_{\rm F}\le\|A\|_{\rm F}.
\]
Integrating and letting \(\varepsilon\downarrow0\) proves candidate (2), including when the initial energy or an intermediate energy vanishes.

The inequality is only an upper derivative inequality. An absolute derivative inequality with the same right side would be false: for scalar \(V(t)=e^{L_0-ct}\), with \(L_0,c>0\), \(A=0\), \(P=c\), one has
\(\mathcal E_+'=-2c(L_0-ct)\) while \(t<L_0/c\).
Its negative derivative has nonzero magnitude although \(\|A\|=0\).
The candidate uses the correct sign throughout.

The two-sided feature estimate used from the dependencies follows by the same trace proof with \(g(\lambda)=(\log\lambda)^2/4\):
\[
\mathcal E'=\operatorname{Tr}[(\log G)Q^TBQ],\qquad
|\mathcal E'|\le2\sqrt{\mathcal E}\|B\|_{\rm F}.
\]
Writing \(\Lambda(V)=(\sum_j(\log\sigma_j(V))^2)^{1/2}\), regularization gives the useful version with arbitrary full-rank initialization:
\[
\Lambda(V(s))\le\Lambda(V(s_0))
 +\int_{s_0}^s\|B(u)\|_{\rm F}\,du.
\]
For an initial isometry and \(B=Db\), it yields
\(\Lambda(U_{\rm feat}(s,s_0)E)\le C_B\sqrt n(s-s_0)\).

## 5. The actual physical derivative and the expansion estimate

This checks candidate (3)–(4), lines 83–104. Since
\(\nabla_\theta\alpha=-2b/n\), differentiation at fixed physical time uses the generator
\[
D_{\rm phys}=D_\theta(\alpha b)
=\alpha Db+b(\nabla_\theta\alpha)^T
=\alpha Db-\frac2n bb^T.
\]
Both terms are symmetric. Thus the decomposition in Section 4 applies with
\(A=\alpha Db\) and \(P=2bb^T/n\succeq0\). The event gives
\(\alpha>0\) at every finite physical time, so
\[
\int_{t_0}^t\|A(u)\|_{\rm F}\,du
\le C_B\sqrt n\int_{t_0}^t\alpha(u)\,du
=C_B\sqrt n[s(t)-s(t_0)].
\]
Starting from \(V(t_0)=E\), all singular values are initially 1, so
\[
\mathcal E_+(U_{\rm phys}(t,t_0)E)
\le C_B^2n[s(t)-s(t_0)]^2\le C_B^2nS_*^2.
\]
This proves (4), including its largest singular value. It is not necessary, and would in general be impossible, to bound the integral over all physical time of the absolute size of the negative clock correction.

## 6. Exact clock comparison, rectangular interlacing, and the single exclusion

This independently checks ACTUAL_CLOCK_RANK_ONE_RESPONSE.md, lines 23–102, rather than inferring a finite-time rank bound from the rank of the instantaneous correction.

Fix a reached state \(x=\theta(t_0)\), and a finite duration \(\Delta t=t-t_0\).
Write \(\Phi_s\) for the autonomous feature flow and \(\Psi_t\) for the physical flow. For initial states near \(x\), let \(\tau(t,x)\) solve
\[
\partial_t\tau(t,x)=2[1-f(\Phi_{\tau(t,x)}(x))],
\qquad\tau(0,x)=0.
\]
The feature solution is globally defined forward, and smooth ODE dependence holds on a neighborhood covering any fixed finite segment of the reference physical trajectory. Such a neighborhood may depend on the chosen finite segment; no uniform neighborhood over infinite time is needed. Differentiating
\[
\Psi_{\Delta t}(x)=\Phi_{\tau(\Delta t,x)}(x)
\]
at the reference state gives
\[
U_{\rm phys}(t,t_0)
=U_{\rm feat}(s(t),s(t_0))
 +b(\theta(t))D_x\tau(\Delta t,x).
\]
The last expression is a column times a row, hence rank at most one.
The feature derivative in the first term holds the feature duration fixed. The second term retains the entire derivative of that duration. This is the correct endpoint rank-one statement; merely integrating a time-dependent rank-one matrix would not have proved it.

Restriction on the right by any \(N\)-by-\(m\) isometry \(E\) preserves the rank bound. Both resulting matrices have full column rank because the square propagators are invertible at finite times.

For arbitrary rectangular \(A_0,P_0\) with \(P_0-A_0=uv^T\), singular-value min–max in the common \(m\)-dimensional domain gives
\[
\sigma_{k+1}(P_0)\le\sigma_k(A_0),\qquad
\sigma_{k+1}(A_0)\le\sigma_k(P_0),\qquad1\le k<m.
\]
Specifically, the span of right singular vectors \(k,\ldots,m\) of \(A_0\) has dimension \(m-k+1\) and satisfies
\(\|A_0x\|\le\sigma_k(A_0)\|x\|\).
Its intersection with \(\ker v^T\) has dimension at least \(m-k\), and on that intersection \(P_0x=A_0x\).
Using
\[
\sigma_{k+1}(P_0)
=\min_{\dim L=m-k}\ \max_{\substack{x\in L\\\|x\|=1}}\|P_0x\|
\]
proves the first inequality; exchange the matrices for the second.
This works at repetitions without following singular vectors in time.

Take \(P_0=U_{\rm phys}E\), \(A_0=U_{\rm feat}E\).
The function \(u\mapsto(-\log u)_+\) is decreasing on \(u>0\). Thus
\[
\sum_{j=1}^{m-1}(-\log\sigma_j(P_0))_+^2
\le\sum_{j=2}^{m}(-\log\sigma_j(A_0))_+^2
\le\Lambda(A_0)^2\le C_B^2nS_*^2.
\]
Adding the positive energy bound from Section 5 and using
\(x^2=x_+^2+(-x)_+^2\) proves candidate (5):
\[
\frac1n\sum_{j=1}^{m-1}(\log\sigma_j(P_0))^2
\le2C_B^2S_*^2.
\]
The largest singular value is retained for \(m\ge2\); only the smallest is omitted. When \(m=1\), the two-sided sum is empty and the one-sided bound still controls the only singular value.

For \(r>0\), each counted term costs at least \(r^2\). This yields exactly (6):
\[
\#\{j:\log\sigma_j(P_0)\ge r\}\le C_B^2nS_*^2/r^2,
\]
\[
\#\{j:|\log\sigma_j(P_0)|\ge r\}
\le1+2C_B^2nS_*^2/r^2.
\]
No independence of \(E\) and the trajectory is needed. This is restriction of the domain of the full response, not projection of its codomain; a projection onto hidden blocks alone can lose rank and is not covered by these unregularized logarithms.

## 7. Transformed metric: both endpoint factors and the missing initial positive cost

This checks candidate (7)–(8), lines 137–168, and the needed metric-transfer dependency.

The scalar map \(F(z)=z+z^3/3\) is a smooth global bijection with
\(F'(z)=1+z^2>0\). For
\[
\eta=(F(z^{(1)})/\sqrt n,W^{(2)},W^{(3)},c/\sqrt n)
\]
its coordinate derivative is
\[
D_\theta\eta=n^{-1/2}H,\qquad
H=\operatorname{diag}(\operatorname{diag}(1+(z_i^{(1)})^2),I,I,I).
\]
Therefore the exact derivative conjugacy, at either fixed physical or feature times, is
\[
U_\eta=(n^{-1/2}H_t)U_\theta(\sqrt n H_{t_0}^{-1})
=H_tU_\theta H_{t_0}^{-1}.
\]
The common scalar cancels for the propagator, but it does not cancel when converting a raw Gaussian column response to its transformed output; that conversion is checked separately below.

Here \(H\succeq I\), so for any isometry \(E\),
\[
(H^{-1}E)^T(H^{-1}E)=E^TH^{-2}E\preceq I_m.
\]
All its singular values are positive and at most one. Hence its initial positive-log energy is zero, even though its full two-sided energy need not be zero.

For any symmetric positive definite \(H\), the auxiliary path
\(V_r=H^rV\), \(0\le r\le1\), satisfies
\(\partial_rV_r=(\log H)V_r\). Section 4 therefore gives
\[
\sqrt{\mathcal E_+(HV)}
\le\sqrt{\mathcal E_+(V)}+\|\log H\|_{\rm F},\qquad
\Lambda(HV)\le\Lambda(V)+\|\log H\|_{\rm F}.
\]
For the endpoint factors here,
\[
\|\log H\|_{\rm F}^2
=\sum_i[\log(1+(z_i^{(1)})^2)]^2\le4\|z^{(1)}\|^2.
\]
To verify the scalar bound, \(2\sqrt u-\log(1+u)\) has value zero at zero and derivative
\[
u^{-1/2}-(1+u)^{-1}
=\frac{1+u-\sqrt u}{\sqrt u(1+u)}>0\quad(u>0),
\]
because \(1+u-\sqrt u=(\sqrt u-1/2)^2+3/4\).

Apply the physical positive-energy estimate first to
\(U_{\rm phys}H_{t_0}^{-1}E\), whose initial positive energy is zero, then multiply by \(H_t\). This gives exactly (7):
\[
\sqrt{\mathcal E_+(U_{\eta,\rm phys}(t,t_0)E)}
\le C_B\sqrt n[s(t)-s(t_0)]+2\|z^{(1)}(t)\|.
\]
The absence of an initial endpoint term is justified by \(H_{t_0}^{-1}\preceq I\), not by treating the coordinate change as an isometry. On \(\Omega_n\), this is at most
\(\sqrt n(C_BS_*+2R_1)\).

For the full two-sided feature energy, both endpoints cost:
\[
\begin{aligned}
\Lambda(U_{\eta,\rm feat}(s,s_0)E)
&\le\|\log H_{s_0}\|_{\rm F}
 +C_B\sqrt n(s-s_0)+\|\log H_s\|_{\rm F}\\
&\le\sqrt n(C_BS_*+4R_1).
\end{aligned}
\]
Here the initial bound follows by applying the endpoint inequality to \(H_{s_0}^{-1}E\); \(\|\log H^{-1}\|_{\rm F}=\|\log H\|_{\rm F}\).

Conjugating the physical–feature difference by the same endpoint matrices, and then restricting to \(E\), preserves rank at most one. The negative-energy interlacing argument in Section 6 thus applies in the transformed coordinates as well. Adding it to (7) proves exactly (8):
\[
\frac1n\sum_{j=1}^{m-1}
[\log\sigma_j(U_{\eta,\rm phys}E)]^2
\le(C_BS_*+2R_1)^2+(C_BS_*+4R_1)^2.
\]
For a top-column seed the feature estimate can be sharpened because
\(H_{t_0}^{-1}E_i=E_i\), but the candidate's larger constant is valid.

## 8. Actual auxiliary Gaussian response and covariance normalization

This checks candidate lines 170–176. The matrix
\[
E_i u=(0,0,ue_i^T,0)
\]
is an isometry because \(\|ue_i^T\|_{\rm F}=\|u\|\). A perturbation of the original matrix column by \(g/\sqrt n\) is the raw-coordinate perturbation \(E_i g\). For a standard Gaussian \(g\in\mathbb R^n\) independent of the trajectory, put
\[
Y_i=U_{\rm phys}(t,t_0)E_i.
\]
Conditional on that trajectory and the chosen starting and ending times, the raw linear response is \(Y_i g\) with covariance \(Y_iY_i^T\). It is the derivative of the trained flow; coefficients of the trajectory have not been resampled or replaced.

The transformed response to the same column perturbation is
\[
\widetilde Y_i g=\frac1{\sqrt n}H_tU_{\rm phys}(t,t_0)E_i g
=\frac1{\sqrt n}U_{\eta,\rm phys}(t,t_0)E_i g.
\]
The equality uses \(H_{t_0}^{-1}E_i=E_i\), since \(E_i\) lies in the \(W^{(3)}\) block. It is valid at any reached starting time. Let
\(X_i=U_{\eta,\rm phys}E_i=\sqrt n\,\widetilde Y_i\).
Then
\[
\operatorname{Cov}_g(\widetilde Y_i g\mid\text{trajectory})
=\widetilde Y_i\widetilde Y_i^T=\frac1nX_iX_i^T.
\]
The nonzero eigenvalues are exactly
\[
\lambda_j=\frac{\sigma_j(X_i)^2}{n},\qquad 1\le j\le n.
\]
There are precisely \(n\) of them, since \(X_i\) has full column rank at finite times; the other \(N-n\) eigenvalues vanish. Consequently
\[
\log(n\lambda_j)=2\log\sigma_j(X_i),\qquad
(\log(n\lambda_j))_+^2=4(\log\sigma_j(X_i))_+^2.
\]
Likewise the squared two-sided logarithms have the factor four, with the same single exclusion as (8). Thus the candidate's covariance statement has the correct \(n\) and the correct factor four. At \(t=t_0\), the nonzero transformed covariance eigenvalues are \(1/n\), an immediate check that omitting the normalization would be wrong.

This is a conditional Gaussian law for an auxiliary derivative probe. It does not assert that an initialized column remains independent of its trained trajectory, that a reached trained column has its initial Gaussian law, or that an unconditioned random response is Gaussian. No unregularized logarithm of an ambient zero eigenvalue is taken.

## 9. New corollaries (8a) and (8b): untrimmed regularized increment bounds

This section audits the entire new paragraph, current candidate lines 178–209.

For a full-column-rank \(N\)-by-\(m\) matrix \(Y\) and an isometry \(E\) of the same size, every \(x\in\mathbb R^m\) satisfies
\[
\|(Y-E)x\|^2\le2\|Yx\|^2+2\|Ex\|^2
=2\|Yx\|^2+2\|x\|^2.
\]
Equivalently,
\[
(Y-E)^T(Y-E)\preceq2Y^TY+2I_m.
\]
Ordered-eigenvalue min–max applied to these symmetric matrices gives
\[
\sigma_j(Y-E)^2\le2\sigma_j(Y)^2+2,\qquad1\le j\le m.
\]
This step uses scalar monotonicity on ordered eigenvalues. It does not assert a generally invalid matrix monotonicity property of the squared logarithm.

For \(u>0\),
\[
3+2u^2\le5\max\{1,u^2\},\qquad
0\le\log(3+2u^2)\le\log5+2(\log u)_+.
\]
All the quantities being squared are nonnegative. Combining the previous two inequalities and \((a+b)^2\le2a^2+2b^2\) gives
\[
\begin{aligned}
\sum_{j=1}^m[\log(1+\sigma_j(Y-E)^2)]^2
&\le\sum_{j=1}^m[\log(3+2\sigma_j(Y)^2)]^2\\
&\le2m(\log5)^2+8\sum_{j=1}^m(\log\sigma_j(Y))_+^2\\
&=2m(\log5)^2+8\mathcal E_+(Y).
\end{aligned}
\]
No negative logarithmic energy and no interlacing exclusion have been used.

For the raw increment use \(Y=Y_i=U_{\rm phys}E_i\), \(E=E_i\), \(m=n\).
Then \(Y-E=Z_i=(U_{\rm phys}-I_N)E_i\). Formula (4) proves
\[
\frac1n\sum_{j=1}^n[\log(1+\sigma_j(Z_i)^2)]^2
\le2(\log5)^2+8C_B^2S_*^2,
\]
which is exactly (8a).

For the transformed increment use \(Y=X_i=U_{\eta,\rm phys}E_i\),
\(E=E_i\), \(m=n\). The definition in the candidate gives
\[
X_i-E_i=\sqrt n\,\widetilde Z_i,\qquad
\sigma_j(X_i-E_i)^2=n\sigma_j(\widetilde Z_i)^2.
\]
The positive energy estimate (7) therefore proves
\[
\frac1n\sum_{j=1}^n[\log(1+n\sigma_j(\widetilde Z_i)^2)]^2
\le2(\log5)^2+8(C_BS_*+2R_1)^2,
\]
exactly (8b). The terminal-coordinate factor is already included in (7), and the initial \(1/\sqrt n\) for this probe is explicitly retained.

These are the correct derivatives of state increments with respect to a seed at the starting state. More explicitly, for fixed duration \(\Delta t\), the derivative of
\(\Psi_{\Delta t}(x)-x\) along \(E_i g\) is \(Z_i g\).
In transformed coordinates the starting perturbation is \(E_i g/\sqrt n\), so differentiating the transformed state difference gives
\((U_{\eta,\rm phys}-I_N)E_i g/\sqrt n=\widetilde Z_i g\).
At \(t_0>0\) this is a restarted derivative at the reached state, as the candidate expressly says. A derivative of a later increment with respect to a column seed at the original time zero would instead include the propagation to \(t_0\); that different quantity is not silently substituted.

With the auxiliary independent Gaussian probe, the conditional increment covariances are \(Z_iZ_i^T\) and
\(\widetilde Z_i\widetilde Z_i^T\), respectively. Their ranks may be smaller than \(n\). Every zero singular value contributes \(\log(1+0)^2=0\), so rank loss is harmless, and ambient zero covariance eigenvalues could also be included in these regularized sums without changing them. At \(t=t_0\), both increments vanish and both left sides are zero.

Thus both new corollaries pass with exactly the stated constants, all \(n\) increment singular values included, and no extra event or independence assumption. The explicit auxiliary-probe wording correctly avoids assuming a Gaussian trained column at a reached state. There is no conflict with an unbounded negative logarithm of the full propagator: these increment observables are regularized and use only expansion-side control.

## 10. Necessity of a contracting extreme

This checks current candidate (9)–(10), lines 213–241.

Let \(v(\theta)=\alpha(\theta)b(\theta)\) be the autonomous physical field.
Differentiating the finite-time flow identity
\[
\Psi_t(\Psi_\varepsilon(\theta(0)))
=\Psi_{t+\varepsilon}(\theta(0))
\]
at \(\varepsilon=0\) gives
\[
U_{\rm phys}(t,0)v(\theta(0))=v(\theta(t)).
\]
All differentiations are finite-time derivatives of smooth flows. Since
\(\alpha(0)>0\), this is exactly
\[
U_{\rm phys}(t,0)b(\theta(0))
=\frac{\alpha(t)}{\alpha(0)}b(\theta(t)).
\]
The \(h^{(3)}(0)\) readout-gradient block gives
\(\|b(\theta(0))\|\ge b_0\sqrt n>0\), and Section 3 gives
\(\|b(\theta(t))\|\le K_b\sqrt n\). Applying the square minimum singular-value characterization to the unit vector
\(b(\theta(0))/\|b(\theta(0))\|\) yields
\[
\begin{aligned}
\sigma_N(U_{\rm phys}(t,0))
&\le\frac{\|U_{\rm phys}(t,0)b(\theta(0))\|}{\|b(\theta(0))\|}\\
&\le\frac{K_b}{b_0}\frac{\alpha(t)}{\alpha(0)}
\le\frac{K_b}{b_0}e^{-2k_0t}.
\end{aligned}
\]
Hence, for each fixed width and each initialization in \(\Omega_n\),
\[
\frac1n\sum_{j=1}^N[\log\sigma_j(U_{\rm phys}(t,0))]^2
\ge\frac1n\bigl(2k_0t-\log(K_b/b_0)\bigr)_+^2,
\]
whose supremum over finite \(t\) is infinite. Invertibility at every finite time is fully compatible with this statement: the singular value tends to zero only in the limit, and no zero is logged at a finite time.

This establishes necessity of an exclusion for a two-sided all-time theorem covering the full square propagator, and therefore for a theorem universally quantified over all isometries. It does not prove that every top-column restriction contains this contracting direction. The candidate explicitly maintains this distinction.

As an additional consistency check, the same fixed-width impossibility holds after the stated coordinate transformation. The trial direction proportional to
\(H_0b(\theta(0))\) gives a transformed minimum singular value at most
\[
(1+nR_1^2)(K_b/b_0)e^{-2k_0t},
\]
because \(\|H_t\|_{\rm op}\le1+\|z^{(1)}(t)\|^2\le1+nR_1^2\) and
\(\|H_0b(\theta(0))\|\ge\|b(\theta(0))\|\).
This prefactor need not be width independent to establish divergence of the negative logarithm at each fixed width. No such strengthening is needed for the candidate's raw-space claim.

## 11. Quantifiers, limits, and final assessment

The accepted probabilistic statement has the following order:
\[
\exists\, b_0,\epsilon_0,k_0,M,R,S_*,R_1>0
\quad\forall n\quad
\exists\Omega_n,\qquad \Pr(\Omega_n)\to1,
\]
with all constants independent of \(n\), such that on \(\Omega_n\) the displayed response inequalities hold simultaneously for every finite segment
\[
0\le t_0\le t<\infty,\qquad1\le m\le N,\qquad E^TE=I_m,
\]
and the column statements hold for every \(i=1,\ldots,n\).
The general deterministic inequalities cover isometries chosen using the trajectory. For the covariance interpretations the auxiliary Gaussian probe is independent, exactly as specified in the candidate.

The path bounds are established before any of these times or embeddings are chosen. No union bound over uncountably many times or subspaces is needed. No indicator of a probabilistic event is differentiated. Smooth local dependence around each finite reference trajectory segment suffices even if a nearby initial state is outside \(\Omega_n\). A supremum over finite times does not claim differentiability of an infinite-time endpoint map.

The statement is a sequence of high-probability finite-width events. It does not assert one almost-sure event for all widths, an infinite-width response flow, an exchange of width and time limits, or a population continuation result.

The remaining amplitude limitation is real. For the abstract \(n\)-direction matrix
\[
Y_n=\operatorname{diag}(e^{c\sqrt n},1,\ldots,1),\qquad c>0,
\]
the normalized positive-log energy is \(c^2\), while
\[
\frac1n\operatorname{Tr}(Y_n^TY_n)
=\frac{e^{2c\sqrt n}+n-1}{n}\longrightarrow\infty.
\]
The regularized increment squared-log energy of \(Y_n-I\) is likewise of order \(n\), while its normalized squared amplitude diverges. This analytic example illustrates a limitation of the inequalities; it is not asserted to be an actual canonical network trajectory or a counterexample to a population theorem. The candidate appropriately leaves response energy, source alignment, and population claims unresolved.

| Audit target in the current candidate | Finding |
| --- | --- |
| Raw Hessian and velocity constants, lines 11–25 | PASS; both trained-matrix cross terms and the Euclidean scaling are retained. |
| Positive-log trace differential, (1) | PASS at eigenvalue 1, repetitions, and crossings; \(C^1\) suffices. |
| Sign and integration, (2) | PASS; only an upper derivative bound is used. |
| Actual physical clock, (3)–(4) | PASS; the negative semidefinite correction is retained. |
| Rectangular interlacing and one exclusion, (5)–(6) | PASS, including \(m=1\), repeated singular values, and arbitrary starting times. |
| Transformed endpoint factors, (7)–(8) | PASS; initial contraction costs zero positive-log energy. |
| Gaussian covariance, lines 170–176 | PASS; conditional auxiliary probe, \(n\lambda_j=\sigma_j^2\), factor four, ambient zeros excluded from unregularized logs. |
| New raw increment bound, (8a) | PASS; no singular value excluded and rank-deficient increments allowed. |
| New transformed increment bound, (8b) | PASS; the \(n\sigma_j^2\) normalization and \(2R_1\) cost are correct. |
| Necessary contracting extreme, (9)–(10) | PASS for the full square propagator; no universal column-contraction claim is made. |
| Event and scope | PASS; one event per width covers all finite physical segments, with finite-width response scope only. |

**Final verdict: PASS for the current candidate with SHA256 f5d813af3bb195ba6b5d1829f02556d6a57bf803e3f1d9b883ad3983929e4b5c, including (8a) and (8b). Required corrections: none.**
