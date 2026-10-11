# Arbitrary-label fitting with a nonlinear top activation

2026-10-10. Scoped derivation and audit of the supervisor's proposed positive route. The permitted scientific source was the complete `TWO_LAYER_PERSISTENCE.md`, whose Section 2 supplies the Gaussian negative-subspace construction reproduced below.

**Result:** the logarithmic bootstrap closes for a linear first activation and a genuinely nonlinear second activation with a derivative floor and bounded homogeneity defect. It gives high-probability Gaussian fitting of every fixed label vector. This does not prove the tanh/tanh target, does not cover linearly dependent input columns, and supplies no compression theorem.

An initially proposed matrix balance was incorrect: the off-diagonal entries of the top balance contain different neurons' activation derivatives. A scalar trace balance, combined with the exact first-layer matrix invariant, repairs the argument and gives the required operator bounds.

## Precise theorem

Let \(X\in\mathbb R^{d\times m}\) have linearly independent unit columns, with \(m\ge2\). Let \(n\ge d+1\), and consider

\[
 U=AX,\qquad Z=WU,\qquad H=\phi(Z),\qquad
 f=H^\top w/n,\qquad r=f-y,\qquad
 \mathcal L=\|r\|^2/m,
\]

where \(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\), and \(w\in\mathbb R^n\). Assume the real-analytic activation \(\phi\) satisfies, for finite constants \(c_\phi,L_\phi,M_\phi\) with \(c_\phi>0\),

\[
 c_\phi\le\phi'(z)\le L_\phi,
 \qquad
 |\phi(z)-z\phi'(z)|\le M_\phi
 \qquad(z\in\mathbb R).
\]

There is no requirement that \(\phi(0)=0\). A concrete nonlinear example is \(\phi(z)=z+\varepsilon\arctan z\) with \(\varepsilon>0\).

All three parameter blocks are trained by gradient flow of \(\mathcal L\) with mobilities \(n,1,n\). Initialize the entries of \(A\) as independent \(N(0,1)\), those of \(W\) as independent \(N(0,1/n)\), independently of \(A\), and set \(w=0\).

There is an initialization event, independent of the labels, of probability at least

\[
 1-\frac{524304(d^2+d)}n
   -2\exp\bigl((2n-d)\log9-8n\bigr),
\tag{1}
\]

on which, simultaneously for every finite \(y\in\mathbb R^m\), the trajectory exists for all finite times, converges to finite parameters, and fits:

\[
 \lim_{t\to\infty}\mathcal L(t)=0.
\]

For each such trajectory with \(y\ne0\), there are finite \(t_0\), positive \(c\), and finite \(C\) such that \(\mathcal L(t)\le C e^{-ct}\) for \(t\ge t_0\). These constants can initially be chosen from the realized initialization. The final section strengthens this: for every fixed nonzero label vector, deterministic positive decay constants independent of width hold on events whose probabilities tend to one. No uniformity over unbounded label vectors is claimed. The lower bound in (1) is informative only when positive; for fixed \(d\), it tends to one as \(n\to\infty\).

The concrete example is nonlinear for \(\varepsilon>0\), and its derivatives are bounded on every closed horizontal strip of width strictly less than one. Its values are unbounded. On the real axis,

\[
 1\le\phi'(z)=1+\frac{\varepsilon}{1+z^2}\le L_\phi:=1+\varepsilon,
 \qquad |\phi(z)|\le L_\phi|z|.
\tag{2}
\]

Its homogeneity defect is bounded:

\[
 \psi(z):=\phi(z)-z\phi'(z)
 =\varepsilon\left(\arctan z-\frac{z}{1+z^2}\right),
 \qquad |\psi(z)|\le M_\phi:=\frac{\varepsilon\pi}{2}.
\tag{3}
\]

For the last bound, the expression in parentheses is odd, has derivative \(2z^2/(1+z^2)^2\), and tends to \(\pi/2\) as \(z\to\infty\).

A second example is \(\phi(z)=z+\varepsilon\tanh z\), again with \(\varepsilon>0\). Here \(c_\phi=1\), \(L_\phi=1+\varepsilon\), and

\[
 \psi(z)=\varepsilon(\tanh z-z\operatorname{sech}^2z),
 \qquad |\psi(z)|\le\varepsilon.
\]

The defect is odd and increasing on the positive half-line, because its derivative there is \(2\varepsilon z\operatorname{sech}^2z\tanh z\ge0\); its positive limit is \(\varepsilon\). Derivatives of this activation are bounded on every closed horizontal strip strictly inside the tanh poles. The linear term prevents the top derivative from vanishing in the tails.

## Exact equations and global existence

Write \(D=\phi'(Z)\in\mathbb R^{n\times m}\). The physical-time equations are

\[
\begin{aligned}
 \dot w&=-\frac2m Hr,\\
 \dot W&=-\frac{2}{mn}\operatorname{diag}(w)D
                    \operatorname{diag}(r)X^\top A^\top,\\
 \dot A&=-\frac2m W^\top\operatorname{diag}(w)D
                    \operatorname{diag}(r)X^\top.
\end{aligned}
\tag{4}
\]

For \(\theta=(A,W,w)\), the mobility norm is

\[
 \|\theta\|_{M^{-1}}^2
 =\|A\|_F^2/n+\|W\|_F^2+\|w\|^2/n.
\]

The exact energy identity is

\[
 \dot{\mathcal L}=-\|\dot\theta\|_{M^{-1}}^2.
\tag{5}
\]

Set \(Y=\|y\|/\sqrt m\). On any local solution, integrating (5) and applying Cauchy–Schwarz gives

\[
 \|\theta(t)-\theta(s)\|_{M^{-1}}\le Y\sqrt{t-s}.
\tag{6}
\]

At a hypothetical finite maximal existence time, this makes the parameters Cauchy, hence convergent to a finite state. Smooth local existence at that state extends the solution, a contradiction. Thus the solution exists for all finite times. The same argument applies without bounded activation values.

## First invariant and the Gaussian geometry event

Define

\[
 C_0=W(0)^\top W(0)-A(0)A(0)^\top/n.
\]

Equation (4) can be written as \(\dot A=W^\top F\), \(\dot W=FA^\top/n\), where

\[
 F=-\frac2m\operatorname{diag}(w)D\operatorname{diag}(r)X^\top.
\]

Differentiating the two quadratic products shows that

\[
 W(t)^\top W(t)-A(t)A(t)^\top/n=C_0
\tag{7}
\]

for all time. If \(C_0\) has a \(d\)-dimensional subspace on which its quadratic form is at most \(-\kappa\) times squared norm, spectral decomposition gives a fixed \(d\)-dimensional spectral subspace \(V\) with the same bound. For \(v\in V\), (7) implies

\[
 \|A(t)^\top v\|^2/n
 =\|W(t)v\|^2-v^\top C_0v\ge\kappa\|v\|^2.
\]

Taking an orthonormal basis matrix \(P\) of \(V\), the square matrix \(A^\top P/\sqrt n\) has all singular values at least \(\sqrt\kappa\). Hence

\[
 A(t)^\top A(t)/n\succeq
 A(t)^\top PP^\top A(t)/n\succeq\kappa I_d.
\tag{8}
\]

Here is the Gaussian certificate from the permitted source, with its ingredients made explicit. In an orthogonal basis whose first \(d\) directions span \(A(0)\), write

\[
 A(0)A(0)^\top/n=\begin{pmatrix}D_0&0\\0&0\end{pmatrix},
 \qquad W(0)=[B_0,E_0],
 \qquad S_0=B_0^\top E_0E_0^\top B_0.
\]

Conditional on \(A(0)\), \(B_0\) and \(E_0\) are independent Gaussian matrices with entry variance \(1/n\). Their shapes are \(n\times d\) and \(n\times(n-d)\). The event

\[
 \|B_0^\top B_0-D_0\|_{\mathrm{op}}\le1/256,
 \quad \tfrac12 I_d\preceq S_0\preceq2I_d,
 \quad\|E_0\|_{\mathrm{op}}\le8
\tag{9}
\]

has probability at least (1). In detail, Gaussian second and fourth moments give

\[
 \mathbb E\|A(0)^\top A(0)/n-I_d\|_F^2
 =\mathbb E\|B_0^\top B_0-I_d\|_F^2=(d^2+d)/n,
\]

and, writing \(k=n-d\),

\[
\begin{aligned}
 \mathbb E\|S_0-I_d\|_F^2
 &=(d^2+d)\frac{k(n+k+1)}{n^3}
   +d\left(\frac{2k}{n^3}+\frac{d^2}{n^2}\right)\\
 &\le\frac{4(d^2+d)}n.
\end{aligned}
\]

Markov's inequality at tolerances \(1/512,1/512,1/2\) gives total failure probability at most \(524304(d^2+d)/n\) for the first two conditions of (9). For the last, \(1/4\)-nets of the two unit spheres have sizes at most \(9^n\) and \(9^{n-d}\), by the disjoint-ball volume argument. Approximating both arguments of a bilinear form shows that its operator norm is at most twice the largest net pairing. Each pairing has law \(N(0,1/n)\); the Gaussian exponential-moment bound and a union bound give failure probability at most \(2\exp((2n-d)\log9-8n)\).

For \(u\in\mathbb R^d\), take

\[
 v=\begin{pmatrix}u\\-E_0^\top B_0u/64\end{pmatrix}.
\]

On (9), direct expansion gives

\[
\begin{aligned}
 v^\top C_0v
 &=u^\top\left[B_0^\top B_0-D_0-S_0/32
       +B_0^\top(E_0E_0^\top)^2B_0/4096\right]u\\
 &\le-\|u\|^2/256,
 \qquad \|v\|^2<2\|u\|^2.
\end{aligned}
\]

The inequality uses \(E_0E_0^\top\preceq64I\), so the last two terms are at most \(-S_0/64\preceq-I/128\). Thus there is a \(d\)-dimensional subspace with Rayleigh quotient at most \(-1/512\). A diagonalization and dimension-intersection argument gives the required spectral subspace. Equation (8) therefore holds with

\[
 \kappa=1/512
\tag{10}
\]

on event (9), independently of the labels.

## The scalar balance that replaces the false matrix balance

Set

\[
 a^2=\|A\|_F^2/n,\qquad q^2=\|w\|^2/n,
 \qquad\rho=\sqrt{\mathcal L}=\|r\|/\sqrt m,
 \qquad S(t)=\int_0^t q(u)\rho(u)\,du.
\]

Taking traces in (7) makes \(\|W\|_F^2-a^2\) constant. Let \(\Psi_{ja}=\psi(Z_{ja})\). Directly from (4),

\[
 \frac d{dt}(a^2-q^2)
 =\frac d{dt}(\|W\|_F^2-q^2)
 =\frac4{mn}w^\top\Psi r.
\tag{11}
\]

Since \(\|\Psi\|_F\le M_\phi\sqrt{nm}\), Cauchy–Schwarz yields

\[
 \left|\frac d{dt}(a^2-q^2)\right|
 \le4M_\phi q\rho,
 \qquad
 a^2(t)\le q^2(t)+a^2(0)+4M_\phi S(t).
\tag{12}
\]

This is the only approximate balance needed. Define the finite constant

\[
 R_0=1+a^2(0)+\|C_0\|_{\mathrm{op}}+\frac{|\phi(0)|}{L_\phi}.
\]

The exact matrix invariant (7), followed by (12), gives

\[
 \frac{\|A\|_{\mathrm{op}}^2}{n}\le a^2
 \le q^2+R_0+4M_\phi S,
 \qquad
 \|W\|_{\mathrm{op}}^2\le\|C_0\|_{\mathrm{op}}+a^2
 \le q^2+R_0+4M_\phi S.
\tag{13}
\]

The derivative bound gives \(|\phi(z)|\le|\phi(0)|+L_\phi|z|\). More precisely, (7) and (12) give

\[
 \frac{\|W\|_{\mathrm{op}}\|A\|_{\mathrm{op}}}{\sqrt n}
 \le\sqrt{a^2(a^2+\|C_0\|_{\mathrm{op}})}
 \le a^2+\frac12\|C_0\|_{\mathrm{op}}.
\]

Using this bound, \(\|X\|_F=\sqrt m\), and the definition of \(R_0\),

\[
 \frac{\|H\|_F}{\sqrt n}
 \le\sqrt m\,|\phi(0)|+L_\phi\frac{\|WAX\|_F}{\sqrt n}
 \le L_\phi\sqrt m\,(q^2+R_0+4M_\phi S),
\]

and therefore

\[
 \|f\|\le L_\phi\sqrt m\,q(q^2+R_0+4M_\phi S).
\tag{14}
\]

For clarity, the unused matrix \(WW^\top-ww^\top/n\) does not satisfy an operator estimate obtained merely by replacing its derivative with \(\psi\). Its \(i,j\) derivative contains terms \(w_i\phi'(Z_{ia})Z_{ja}-w_i\phi(Z_{ja})\), with mismatched neuron indices. Equation (11) is valid because the trace matches these indices.

## Kernel lower bound and the logarithmic bootstrap

Let \(\lambda_X=\lambda_{\min}(X^\top X)>0\). The tangent kernel \(K\), normalized by \(\dot r=-2Kr/m\), includes its positive semidefinite middle-layer term

\[
 K_W=\frac1n\sum_{j=1}^n w_j^2
       \operatorname{diag}(D_{j,:})
       \left(\frac{U^\top U}{n}\right)
       \operatorname{diag}(D_{j,:}).
\]

On the geometry event, (8) and \(D_{ja}\ge c_\phi\) give

\[
 K\succeq K_W\succeq\kappa\lambda_X c_\phi^2 q^2 I_m.
\tag{15}
\]

When \(\rho>0\), loss dissipation consequently implies

\[
 \dot\rho\le-bq^2\rho,
 \qquad b=\frac{2\kappa\lambda_X c_\phi^2}{m}>0.
\tag{16}
\]

The readout starts at zero, so a separate argument must produce a lower bound for \(q\). Almost surely, \(H(0)\) has column rank \(m\): \(A(0)X\) has column rank \(m\), and conditionally on it the rows of \(W(0)A(0)X\) are independent nondegenerate Gaussians. The strictly increasing bijection \(\phi:\mathbb R\to\mathbb R\) maps their support onto all of \(\mathbb R^m\). Independent samples from this smooth positive-density distribution have full column rank almost surely for \(n\ge m\). This full-rank event is independent of the labels in the required sense: it holds for every label direction at once.

If \(y=0\), the initial state is already fitted and stationary. For \(y\ne0\),

\[
 \dot{\mathcal L}(0)
 =-\frac4{m^2n}\|H(0)y\|^2<0.
\]

Choose a finite \(t_0>0\) such that

\[
 \delta:=Y-\rho(t_0)>0.
\]

Loss monotonicity and the reverse triangle inequality yield, for every \(t\ge t_0\),

\[
 \|f(t)\|\ge\|y\|-\|r(t)\|\ge\sqrt m\,\delta.
\]

Combining with (14) gives

\[
 \delta\le L_\phi q(q^2+R_0+4M_\phi S).
\]

Define

\[
 c_0=\min\left\{1,
 \frac{\delta}{L_\phi(1+R_0+4M_\phi)}\right\}>0.
\]

If \(q\le1\), the preceding display gives \(q\ge c_0/(1+S)\); if \(q>1\), the same bound holds since \(c_0\le1\). Thus

\[
 q(t)\ge\frac{c_0}{1+S(t)}\qquad(t\ge t_0).
\tag{17}
\]

If \(\rho\) reaches zero, fitting is already complete. Otherwise \(S'=q\rho>0\) on \([t_0,\infty)\). Dividing (16) by this positive derivative and using (17) yields

\[
 \frac{d\rho}{dS}\le-bq\le-\frac{bc_0}{1+S}.
\]

Integration, with \(S_0=S(t_0)\), gives

\[
 0\le\rho(t)
 \le\rho(t_0)-bc_0\log\frac{1+S(t)}{1+S_0}.
\]

Therefore

\[
 S(t)\le S_{\max}:=
 (1+S_0)\exp\!\left(\frac{\rho(t_0)}{bc_0}\right)-1<\infty.
\tag{18}
\]

Now (17) gives the positive all-time lower bound

\[
 q(t)\ge q_{\min}:=\frac{c_0}{1+S_{\max}}>0
 \qquad(t\ge t_0).
\]

Returning to (16),

\[
 \rho(t)\le\rho(t_0)
       e^{-bq_{\min}^2(t-t_0)}.
\tag{19}
\]

Squaring proves exponential loss decay and the fitting conclusion. This argument takes the infinite-time limit at each finite width before invoking the Gaussian probability bound; there is no width/time interchange.

## Finite parameter convergence

The same proof rules out escape to infinity. The exact readout identity is

\[
 \frac d{dt}q^2=-\frac4m f^\top r.
\]

Since \(\|f\|\le\|y\|+\|r\|\le2\|y\|\),

\[
 \left|\frac d{dt}q^2\right|\le8Y\rho.
\]

Equation (19) makes the right side integrable after \(t_0\), so \(q\) is bounded. Equations (12), (13), and (18) then bound \(a\), \(\|A\|_{\mathrm{op}}/\sqrt n\), \(\|W\|_{\mathrm{op}}\), and \(\|H\|_F/\sqrt n\). Using \(D_{ja}\le L_\phi\) in (4) shows that each of

\[
 \|\dot w\|/\sqrt n,\qquad
 \|\dot W\|_F,\qquad
 \|\dot A\|_F/\sqrt n
\]

is at most a finite trajectory-dependent constant times \(\rho\). They are integrable over \([t_0,\infty)\), so all three parameter blocks converge to finite limits. Continuity and (19) identify their limiting predictions as \(y\).

## Deterministic decay constants with probability tending to one

Fix \(X,\phi,y\) with \(Y>0\), independently of width. Define the deterministic population matrix

\[
 G_* =\mathbb E[\phi(Z)\phi(Z)^\top],
 \qquad Z\sim N(0,X^\top X).
\]

The covariance is positive definite, and \(\phi\) is a coordinatewise increasing bijection with derivative bounded below. Thus \(\phi(Z)\) has full support in \(\mathbb R^m\), and \(G_*\) is positive definite: for nonzero \(v\), the continuous function \(v^\top\phi(z)\) is nonzero on some open set of positive Gaussian probability. Put \(\lambda=\lambda_{\min}(G_*)/2>0\).

Choose fixed constants \(a_*,w_*>0\) such that the following event has probability tending to one:

\[
 a(0)\le a_*,\qquad\|W(0)\|_{\mathrm{op}}\le w_*,
 \qquad H(0)^\top H(0)/n\succeq\lambda I_m,
\tag{20}
\]

together with the geometry event (9). Here is the required probability justification. The average \(\|A(0)\|_F^2/n\) converges in probability to \(d\), by its Gaussian second and fourth moments. The same net argument as above allows \(w_*=8\). Finally, conditionally on \(A(0)\), the initial preactivation rows are independent Gaussians with covariance

\[
 \Sigma_n=X^\top A(0)^\top A(0)X/n\longrightarrow X^\top X
\]

in probability. On a fixed bounded neighborhood of this positive-definite covariance, the activation's linear growth gives uniformly bounded fourth moments of all feature entries. Conditional variance estimates therefore make the empirical Gram converge in probability to its conditional expectation. The latter converges to \(G_*\): write the Gaussian vector as \(\Sigma_n^{1/2}g\), use continuity of the positive square root near a positive-definite matrix, and dominate by a constant times \(1+\|g\|^2\), whose Gaussian expectation is finite. These facts prove the top-Gram condition in (20) with probability tending to one.

By (6), for every \(0\le t\le t_*\),

\[
 \frac{\|H(t)-H(0)\|_F}{\sqrt n}
 \le L_\phi\sqrt m\,Y\sqrt t\,(a_*+w_*+Y\sqrt t).
\tag{21}
\]

Indeed, factor \(W(t)A(t)-W(0)A(0)\) as \([W(t)-W(0)]A(t)+W(0)[A(t)-A(0)]\), use the Lipschitz bound for \(\phi\), \(\|X\|_{\mathrm{op}}\le\sqrt m\), and (6). Choose a deterministic \(t_*>0\) so small that the right side of (21) at \(t=t_*\) is at most \(\sqrt\lambda/2\). The smallest singular value of \(H(t)/\sqrt n\) is then at least \(\sqrt\lambda/2\), so \(K(t)\succeq\lambda I_m/4\) on this initial interval. Consequently

\[
 \rho(t_*)\le Y e^{-\lambda t_*/(2m)},
 \qquad
 Y-\rho(t_*)\ge\delta_*:=Y(1-e^{-\lambda t_*/(2m)})>0.
\tag{22}
\]

Equation (6) also gives \(q(t)\le Y\sqrt t\), and hence

\[
 S(t_*)\le S_*:=\frac23Y^2t_*^{3/2}.
\]

On (20), \(\|C_0\|_{\mathrm{op}}\le w_*^2+a_*^2\), so

\[
 R_0\le R_*:=1+2a_*^2+w_*^2+\frac{|\phi(0)|}{L_\phi}.
\]

Define the deterministic constants

\[
 c_* =\min\left\{1,
 \frac{\delta_*}{L_\phi(1+R_*+4M_\phi)}\right\},
 \qquad
 \overline S=(1+S_*)e^{Y/(bc_*)}-1,
 \qquad
 \overline q=\frac{c_*}{1+\overline S}>0,
\]

where \(b=2\kappa\lambda_Xc_\phi^2/m\) is already fixed. Repeating (17)--(19) with these bounds gives, throughout (9) and (20),

\[
 \mathcal L(t)\le
 Y^2\exp\!\bigl(-2b\overline q^{\,2}(t-t_*)\bigr)
 \qquad(t\ge t_*).
\tag{23}
\]

All constants in (23) depend only on the fixed data, labels, activation, and the fixed Gaussian bounds \(a_*,w_*\). They do not depend on width. The certificate is quantitatively poor, especially for large labels, but strictly positive and uniform in time. The probability of its event tends to one as \(n\to\infty\).

## Scope and audit conclusions

The proof uses four substantive features: a linear first activation supplies (7); full column rank of \(X\) turns its protected input geometry into a sample-space gap; the top derivative floor gives (15); and the bounded top homogeneity defect gives (12). The nonlinear activation \(z+\varepsilon\arctan z\) satisfies all four requirements relevant to it.

The tanh/tanh model has neither the first invariant used here nor a positive global derivative floor. Even linear/tanh fails the latter requirement. This positive theorem therefore does not settle the original tanh question or the full analytic activation class. It is a nonlinear, fully trained, Gaussian, arbitrary-label subclass result with an explicit high-probability event.

Real analyticity is not used by the fitting argument beyond ensuring smoothness; the real-axis derivative and defect hypotheses are the operative conditions. Analyticity and the strip bounds put the explicit nonlinear example within the permitted activation class. The theorem includes nonzero \(\phi(0)\), whose only effect on the estimates is the additional constant in \(R_0\).
