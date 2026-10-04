# Signed geometry and initial representation selection in intrinsic q1

First independent note frozen 2026-09-30 after the instruction to stop pursuing compression. This note concerns fitting, conflicts, initial symmetry breaking, and circle classification. It uses only the supplied q1 equations, contains no experiments, and makes no compression claim. Results are internally derived and not independently reviewed or promoted.

The central mechanism is exact: the bias-free odd architecture converts binary labels into input orientation. The resulting signed-input law determines both unavoidable antipodal conflicts and the sole signal that can initiate representation motion from the prescribed zero readout. When that signal is present, the input representation and memory first move in directions that increase feature–label correlation. This is an initial-time selection result, not a convergence or asymptotic classifier theorem.

## 1. Object and exact signed-input symmetry

Let \(\|x\|_2=\sqrt d\), \(y\in\{-1,1\}\), and let expectations be with respect to the empirical or population data law. The q1 flow is
\[
\begin{gathered}
h(x)=\tanh(Ax/\sqrt d),\quad M=\mathbb E[vk^T]/n,
\quad B=W_0+M,\quad g(x)=\tanh(Bh(x)),\quad f(x)=w^Tg(x)/n,\\
r=f-y,\quad d=w\odot(1-g^2),\quad
\ell=(1-h^2)\odot B^Td,\quad
\rho=(\mathbb E r^2)^{1/2},\\
\dot\tau=\rho,\quad\dot k=(\rho/\tau)(h-k),\quad
\dot v=-2rd,\quad\dot w=-2\mathbb E[rg],\quad
\dot A=-2\mathbb E[r\ell x^T/\sqrt d].
\tag{1}
\end{gathered}
The fixed mixer \(W_0\), both tanh nonlinearities, and moving \(A\) are retained. Initial conditions are \(w=v=0\), \(\tau=1\), \(k=h_0\), with the supplied Gaussian initial \(A_0,W_0\).

Every realized predictor is odd:
\[
h(-x)=-h(x),\quad g(-x)=-g(x),\quad f(-x)=-f(x).
\tag{2}
\]
Consequently \(d(-x)=d(x)\) and \(\ell(-x)=\ell(x)\).

**Exact label gauge.** Set
\[
u=yx,\qquad \widetilde k=yk,\qquad \widetilde v=yv,
\qquad \lambda=(x,y\mapsto yx)_\#\mathbb P.
\tag{3}
\]
Give every transformed input target \(+1\). Then \(A,w,\tau,M\) obey exactly the same flow, with the same initial conditions and mixer. Indeed
\[
\widetilde v\widetilde k^T=vk^T,\quad
\widetilde r(u)=f(yx)-1=yr,
\quad \widetilde r^2=r^2,
\]
and
\[
\widetilde r g(u)=rg(x),\qquad
\widetilde r\ell(u)u^T=r\ell(x)x^T.
\]
Multiplying the memory equations by \(y\) verifies their transformed equations as well. Thus \(\lambda\) is sufficient data for the entire flow, not merely for its initial derivative or objective value.

Opposite-label antipodal original samples become one signed input and are compatible. Same-label antipodal original samples become opposite signed inputs, each requesting positive output, and conflict with (2). Equal labels alone do not identify inputs or forces.

Below, all targets are \(+1\), residual is \(r(u)=f(u)-1\), and expectations use \(\lambda\).

## 2. Exact fitting obstruction and the odd-regression target

Let \(R(u)=-u\), and decompose the signed-input probability law into
\[
\lambda_{\rm e}=\tfrac12(\lambda+R_\#\lambda),\qquad
\lambda_{\rm o}=\tfrac12(\lambda-R_\#\lambda).
\tag{4}
\]
The first is a symmetric probability measure; the second is an antisymmetric signed measure. Since \(0\le\lambda\le2\lambda_{\rm e}\), define
\[
\eta=\frac{d\lambda_{\rm o}}{d\lambda_{\rm e}}
=\frac{d\lambda}{d\lambda_{\rm e}}-1.
\tag{5}
\]
Then \(|\eta|\le1\) and \(\eta(-u)=-\eta(u)\) almost everywhere.

**Proposition 1 (the exact target within odd functions).** For every square-integrable odd predictor,
\[
\begin{aligned}
\mathcal L(f)&=\int(f-1)^2\,d\lambda\\
&=1+\int f^2\,d\lambda_{\rm e}-2\int f\eta\,d\lambda_{\rm e}\\
&=1-\int\eta^2\,d\lambda_{\rm e}
+\int(f-\eta)^2\,d\lambda_{\rm e}.
\end{aligned}
\tag{6}
\]
Thus the infimum among all measurable odd square-integrable predictors is
\(1-\|\eta\|_{L^2(\lambda_{\rm e})}^2\), attained by \(f=\eta\). This is an architectural lower bound for q1, not a claim that its finite-width flow reaches or represents this optimizer.

**Proof.** For every even integrable function \(a\), \(\int a\,d\lambda_{\rm o}=0\); for every odd integrable function \(b\), \(\int b\,d\lambda_{\rm e}=0\), by the change of variables \(u\mapsto-u\). Apply these to \(f^2\) and \(f\), respectively, and complete the square. \(\square\)

For classification, count a zero margin as half an error. Define \(s=\operatorname{sgn}f\), including \(s=0\) at zero. Since \(s\) is odd,
\[
\operatorname{Err}(f)
=\tfrac12\left(1-\int s\eta\,d\lambda_{\rm e}\right)
\ge\tfrac12\left(1-\int|\eta|\,d\lambda_{\rm e}\right).
\tag{7}
\]
The lower bound is attained in the unrestricted measurable odd class by \(s=\operatorname{sgn}\eta\), with half-error ties where \(\eta=0\). Without this explicit tie convention, a deterministic global rule at \(f=0\) need not be odd and its tie errors have to be handled separately.

**A single conflicting pair.** If signed inputs \(u,-u\) have masses \(a,b>0\), their loss contribution at output \(s=f(u)\) is
\[
a(s-1)^2+b(-s-1)^2
=(a+b)\left(s-\frac{a-b}{a+b}\right)^2+\frac{4ab}{a+b}.
\tag{8}
\]
Their optimal odd output chooses the majority orientation, their irreducible squared loss is \(4ab/(a+b)\), and their minimum classification error mass is \(\min(a,b)\). No motion of \(A\), adaptation of \(M\), larger width, or longer training removes this obstruction while (1) is retained.

Zero squared loss in the unrestricted odd class requires \(|\eta|=1\) almost everywhere, equivalently mutual singularity of \(\lambda\) and its antipodal reflection. This removes the parity obstruction only; continuity, finite-width representation, and dynamics can impose additional restrictions.

## 3. The exact criterion for initiating learning from zero readout

Let
\[
h_0(u)=\tanh(A_0u/\sqrt d),\qquad
g_0(u)=\tanh(W_0h_0(u)),\qquad
b=\int g_0(u)\,d\lambda(u).
\tag{9}
\]
In the original labeled representation, \(b=\mathbb E[y g_0(x)]\). Thus \(b\) is precisely initial hidden-feature correlation with the labels.

**Proposition 2 (exact frozen-state criterion).** The q1 trajectory has
\[
w(t)=0,\quad v(t,u)=0,\quad A(t)=A_0,
\quad k(t,u)=h_0(u),\quad \rho(t)=1,\quad\tau(t)=1+t
\tag{10}
\]
for all \(t\ge0\) if and only if \(b=0\).

**Proof.** Necessity follows from \(\dot w(0)=2b\). If \(b=0\), substituting (10) into every equation verifies a solution: \(d=\ell=0\), \(r=-1\), and \(\dot w=2\int g_0\,d\lambda=0\). Uniqueness identifies it as the trajectory. For completeness, uniqueness holds because the finite system, or the corresponding continuous-field integral system on the compact sphere, is locally Lipschitz on \(\tau>0\); the residual norm is Lipschitz by the reverse triangle inequality. Here the displayed solution stays in that domain for all time. \(\square\)

If \(\lambda\) is centrally symmetric, \(b=0\) for **every** realized initialization by oddness of \(g_0\). Conversely, nonsymmetry alone need not imply \(b\ne0\) for a specified finite feature set. When \(b=0\), q1 cannot first move its representation and subsequently discover a hidden signal: the representation-driving terms themselves require the readout to move.

Writing \(F_0=\|b\|_2^2/n\), the exact initial loss derivative is
\[
\mathcal L'(0)=-4F_0.
\tag{11}
\]
Indeed \(f'(0,u)=2b^Tg_0(u)/n\), \(r_0=-1\), and differentiating the loss gives (11). If \(\|\lambda_{\rm o}\|_{\rm TV}\) denotes the total mass of the absolute signed measure, then
\[
\|b\|_2/\sqrt n
=\left\|\int g_0\,d\lambda_{\rm o}\right\|_2/\sqrt n
\le\|\lambda_{\rm o}\|_{\rm TV},
\qquad
0\le-\mathcal L'(0)\le4\|\lambda_{\rm o}\|_{\rm TV}^2.
\tag{12}
\]
Thus proximity to antipodal symmetry imposes slow initial learning, without any approximation to the nonlinear model.

### Fixed finite data: nonsymmetry initiates learning almost surely

**Proposition 3.** Fix a finite signed-input empirical law independently of the Gaussian initialization. If it is not centrally symmetric, then \(b\ne0\) with probability one under the stated Gaussian laws, for every \(n\ge1\).

**Proof.** Group support points into distinct unoriented antipodal pairs, choose representatives \(u_j\), and let \(c_j\) be the mass at \(u_j\) minus the mass at \(-u_j\). Nonsymmetry means some \(c_j\ne0\). Choose \(\xi\) avoiding the finitely many hyperplanes on which \(\xi^Tu_j=0\) or \((\xi^Tu_j)^2=(\xi^Tu_k)^2\) for different pairs. Such a choice exists since representatives of different pairs are neither equal nor opposite. Then \(t_j=\xi^Tu_j/\sqrt d\) are nonzero and have distinct squares.

The analytic function \(\sum_jc_j\tanh(st_j)\) cannot vanish identically. To see this, write \(\tanh z=\sum_{k\ge0}(-1)^ka_kz^{2k+1}\) near zero. Its differential equation \(t'=1-t^2\) gives \(a_0=1\) and
\[
(2k+1)a_k=\sum_{i+j=k-1}a_ia_j>0\quad(k\ge1).
\]
Identical vanishing would therefore imply \(\sum_jc_jt_j^{2k+1}=0\) for the first as many indices \(k\) as there are pairs. The Vandermonde matrix on the distinct numbers \(t_j^2\) is invertible, forcing \(c_jt_j=0\) for every \(j\), a contradiction. Hence one first-layer ridge has a nonzero mean: \(\int\tanh(a^Tu/\sqrt d)\,d\lambda\ne0\) for some \(a\).

Choose an illustrative parameter point with the first row of \(A\) equal to \(a^T\), all other rows zero, and only \(W_{11}=s\) nonzero. At sufficiently small nonzero \(s\),
\[
\int g_1(u)\,d\lambda=s\int\tanh(a^Tu/\sqrt d)\,d\lambda+O(s^3)\ne0.
\]
Thus the scalar \(b_1\), viewed as a function of all entries of \(A,W\), is a real analytic function that is not identically zero. A nonzero real analytic function on a connected open Euclidean domain has a zero set of Lebesgue measure zero. The theorem applies on the full parameter space because the sum is finite, tanh is real analytic on the real line, and compositions preserve real analyticity. The Gaussian joint law has a density, so \(\mathbb P(b_1=0)=0\), which implies \(\mathbb P(b=0)=0\). \(\square\)

This is qualitative. It gives no lower bound on \(F_0\), convergence rate, eventual fit, or favorable scaling with width. It also fixes the data before the initialization; reversing that order permits the next counterexample.

### A nonsymmetric population can be invisible to a specified initial representation

On the circle, fix any realized \(n\)-component \(g_0(\theta)\). Consider the \((n+1)\)-dimensional real span of
\(\cos\theta,\cos3\theta,\ldots,\cos((2n+1)\theta)\).
The \(n\) linear constraints
\[
\int_0^{2\pi}\psi(\theta)g_{0,i}(\theta)\,\frac{d\theta}{2\pi}=0,
\qquad i=1,\ldots,n,
\]
have a nonzero solution \(\psi\) in this span. Rescale it so \(\|\psi\|_\infty=1\). For \(0<\varepsilon<1\), the probability density
\[
q(\theta)=1+\varepsilon\psi(\theta)
\tag{13}
\]
relative to uniform angle is strictly positive and not antipodally symmetric. Yet \(b=0\), since the uniform mean of the odd feature vector is zero and the perturbation is orthogonal to every coordinate. The q1 flow is frozen by Proposition 2.

Here \(\lambda_{\rm e}\) is uniform and \(\eta=\varepsilon\psi\), so the unrestricted odd-function optimal loss is \(1-\varepsilon^2\int\psi^2<1\), while q1 stays at loss one. Thus parity alone does not explain the failure to initiate learning. The law in (13) depends on the realized initialization, so this does not contradict Proposition 3. No finite-width expressivity claim is needed for this counterexample to a uniform initialization-independent onset guarantee.

## 4. The first representation motion increases feature–label correlation

Define \(s_h(u)=1-h_0(u)^2\), \(s_g(u)=1-g_0(u)^2\), and the deterministic initial quantities
\[
\begin{aligned}
G&=\int g_0g_0^T\,d\lambda/n,\\
C_A&=\int\left[s_h\odot W_0^T(b\odot s_g)\right]u^T/\sqrt d\,d\lambda,\\
C_B&=\int(b\odot s_g)h_0^T\,d\lambda/n.
\end{aligned}
\tag{14}
\]
The dimensions are \(G,C_B\in\mathbb R^{n\times n}\), \(C_A\in\mathbb R^{n\times d}\). All are computed from the supplied initial state and data.

**Proposition 4 (initial expansion).** As \(t\downarrow0\),
\[
\begin{aligned}
w(t)&=2tb-2t^2Gb+O(t^3),\\
A(t)&=A_0+2t^2C_A+O(t^3),\\
v(t,u)&=2t^2[b\odot s_g(u)]+O(t^3),\\
M(t)&=2t^2C_B+O(t^3),\\
k(t,u)&=h_0(u)+O(t^3),\\
\tau(t)&=1+t-F_0t^2+O(t^3).
\end{aligned}
\tag{15}
\]
The field remainders are uniform on the sphere for each fixed finite initialization and width.

**Proof.** Initially \(d=\ell=v=w=0\), \(\dot A=\dot k=\dot v=\dot M=0\). Thus \(\dot h=\dot g=0\), while \(\dot w=2b\). Differentiating,
\[
\dot d(0,u)=2b\odot s_g(u),\quad
\dot\ell(0,u)=2s_h(u)\odot W_0^T[b\odot s_g(u)].
\]
Since \(r_0=-1\), these imply
\(\ddot v(0,u)=4b\odot s_g(u)\) and \(\ddot A(0)=4C_A\). Twice differentiating \(M=\int vk^T/n\) leaves only \(\int\ddot v h_0^T/n=4C_B\). Also
\[
\ddot w(0)=-2\int\dot r(0,u)g_0(u)\,d\lambda
=-4Gb.
\]
The \(k\) equation gives \(\dot k(0)=\ddot k(0)=0\). Finally \(\rho(0)=1\) and \(\dot\rho(0)=\mathcal L'(0)/2=-2F_0\), giving the clock expansion. Smoothness and uniform Taylor remainders near zero hold because the sphere is compact and \(\rho(0)=1\), so the square root defining the clock is smooth in a neighborhood of the initial state. \(\square\)

Now define a correlation functional for general matrices \(A,B\):
\[
\mathcal F(A,B)
=\frac1n\left\|\int\tanh\!\left(B\tanh(Au/\sqrt d)\right)d\lambda(u)\right\|_2^2.
\tag{16}
\]
It measures squared correlation of hidden features with the original labels. Ordinary Frobenius gradients at \((A_0,W_0)\) satisfy
\[
\nabla_A\mathcal F=\frac2nC_A,\qquad
\nabla_B\mathcal F=2C_B.
\tag{17}
\]
These formulas follow by differentiating tanh and moving the finite integral through the derivative; compactness and bounded local derivatives justify that exchange. Comparing (15) and (17),
\[
\ddot A(0)=2n\nabla_A\mathcal F,
\qquad \ddot M(0)=2\nabla_B\mathcal F.
\tag{18}
\]
Thus the first movement of both representations is an ascent direction for the **same supervised correlation functional**, in their respective scalings. Along the actual intrinsic q1 path,
\[
\mathcal F(A(t),W_0+M(t))
=F_0+4t^2\left(\frac{\|C_A\|_F^2}{n}+\|C_B\|_F^2\right)+O(t^3).
\tag{19}
\]
The displayed coefficient is strictly positive if at least one of \(C_A,C_B\) is nonzero. If both vanish, (19) asserts no increase at this order. Equation (19) does **not** establish monotonicity at later times, nor does it identify the full q1 flow with a gradient flow in \(A,B\).

Output selection begins one order earlier than representation feedback. Define the realized initial kernel
\[
K_0(u,u')=g_0(u)^Tg_0(u')/n.
\]
Then
\[
f'(0,u)=2\int K_0(u,u')\,d\lambda(u'),
\qquad
f(t,u)=\frac{2t}{n}b^Tg_0(u)
-\frac{2t^2}{n}(Gb)^Tg_0(u)+O(t^3).
\tag{20}
\]
Representation changes start at order \(t^2\), and influence output at order \(t^3\) because they are multiplied by a readout of order \(t\). This gives an exact initial ordering of mechanisms without extending a fixed-feature approximation to a nonzero time interval.

## 5. Circle classification: exact parity selection and its limits

Write \(u(\theta)=\sqrt2(\cos\theta,\sin\theta)\). For every time and realization,
\[
f(\theta+\pi)=-f(\theta).
\tag{21}
\]
Therefore every even angular Fourier coefficient of \(f\), including its constant coefficient, is zero. To verify this, split its coefficient integral into two half-circles; for harmonic index \(k\), the second half contributes \(-(-1)^k\) times the first, which cancels when \(k\) is even. The model can produce odd harmonics of arbitrarily high order; (21) is not a low-frequency or single-separator selection rule.

If signed law \(\lambda\) has density \(q\) relative to uniform angle, its odd-regression target is
\[
\eta(\theta)=\frac{q(\theta)-q(\theta+\pi)}{q(\theta)+q(\theta+\pi)}
\tag{22}
\]
where the denominator is positive. The unrestricted optimal odd classifier chooses the larger signed-input mass on each antipodal pair. For the original labeled law, this compares the label imbalance at \(\theta\) with the opposite label imbalance at \(\theta+\pi\), because negative labels reverse input orientation in (3).

Concrete consequences for a uniform original input angle:

* If \(y(\theta+\pi)=y(\theta)\), the signed-input law is centrally symmetric. The q1 trajectory is frozen for every initialization, and every odd predictor has squared loss at least one and classification error at least one half. The task \(y(\theta)=\operatorname{sgn}(\cos2\theta)\) is an explicit four-sector example. Zero-measure boundary ties do not affect the claim.
* If \(y(\theta+\pi)=-y(\theta)\), antipodal labels are compatible and the signed law has no antipodal overlap except possible boundaries. The parity lower bound permits zero loss and zero classification error. This includes both \(\operatorname{sgn}(\cos\theta)\) and the higher-frequency task \(\operatorname{sgn}(\cos3\theta)\). It does not guarantee that q1 reaches either target.
* A nontrivial continuous odd predictor must have at least two antipodal zeros: values at \(\theta\) and \(\theta+\pi\) have opposite signs, so the intermediate value theorem gives a zero between them and oddness gives its antipode. More decision boundaries are allowed.

The early choice among allowed odd directions is set by (20), then reinforced or modified by the correlation-ascent accelerations (18)-(19). A fixed realized Gaussian mixer does not provide exact rotational averaging; random rotation invariance in distribution cannot replace the realized kernel. Nothing proved here selects a maximum-margin separator, a lowest harmonic, a universal orientation, or a unique eventual classifier.

## 6. Proven mechanisms and remaining gaps

| Statement | Status | Scope |
|---|---|---|
| Labels can be absorbed into signed input orientation | Exact | Full finite or population q1 flow, including clock and moving features |
| Antipodal signed overlap creates irreducible conflict | Proved | Exact squared-loss and classification lower bounds (6)-(8) |
| Centrally symmetric signed law is a frozen state | Proved | Every realized initialization |
| Vanishing initial hidden-feature correlation is exactly the frozen-state criterion | Proved | Prescribed zero readout and memories |
| Fixed nonsymmetric finite data begin learning almost surely | Proved | Data independent of Gaussian initialization; no rate bound |
| Nonsymmetry uniformly guarantees onset for all population laws and realizations | False | Construction (13), which chooses the law after the realization |
| First representation acceleration ascends squared supervised feature correlation | Proved | Exact order-\(t^2\) identities (18)-(19) |
| Circle output excludes even harmonics | Exact | All times and widths |
| q1 eventually achieves the best odd predictor or selects a canonical odd classifier | Open | Neither global loss decrease nor convergence was proved |

The next learning question is whether the correlation reinforcement in (19) persists into a controlled nonlocal-in-time mechanism and overcomes small initial signal on compatible tasks. A valid answer must account for the evolving memory lag and the realized mixer. The local identities alone do not justify a global descent law, a margin principle, or an asymptotic classification-selection claim.
