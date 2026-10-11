# A uniform nonzero trained-probe readout under the original cap

2026-10-11. Targeted second round of the circle transport route. Scientific
inputs are exactly those listed in `CIRCLE_TRANSPORT_ROUTE.md`, together
with that route's own derivations. No experiments, external scientific
sources, manuscript edits, or Git operations were used. The required
research, rigorous-proof, and canonical-notation instructions remain in
force.

**Proposition.** With probability tending to one over a top-neuron cavity,
the independent Gaussian trained probe satisfies

\[
\|a_\infty\|_{L^2(g)}\ge\frac{Y}{6H}>0.
\tag{1}
\]

Here \(H\) is exactly the fitting lemma's constant, the Gaussian root is
\(g\sim N(0,I_n)\), and the cavity retains the original width \(n\)
in every variance and flow normalization. The estimate uses the original
cap \(0<Y\le(\gamma/m)\beta^{-30L}\), with no additional restriction.
It applies at any of the fixed depths in the assignment and does not
depend on a test query. It establishes a uniform signal in the direct
probe readout; it does not establish a lower bound for the compensated
circle influence or for two actual fitted networks.

The key is to compare all readout paths with the minimum-norm interpolant
at initialization. Bounding every intermediate quantity by
\(Y/\sqrt\lambda\), independently of the particular label direction,
would lose unnecessary powers of the training gap.

## 1. The cavity and its initialization event

Delete one top hidden neuron and its readout coordinate. Let
\(w(t)\in\mathbb R^{n-1}\) be the retained readout and define

\[
b(t)=w(t)/\sqrt n,\qquad
A(t)=\frac1{\sqrt n}
\begin{bmatrix}
h^{(L)}(t,v_1)^\top\\ \vdots\\h^{(L)}(t,v_m)^\top
\end{bmatrix}\in\mathbb R^{m\times(n-1)}.
\]

Thus the fitted training prediction is \(A(t)b(t)\), the residual is
\(r(t)=A(t)b(t)-y\), and the exact readout equation is

\[
\dot b=-\frac2m A(t)^\top r(t),\qquad b(0)=0.
\tag{2}
\]

Write \(\lambda=\gamma/m\), \(\rho=\|r\|/\sqrt m\), and let
\(F=F_L\) be the coefficient in the supplied fitting proof. On its
cavity fitting event,

\[
\begin{gathered}
A_0A_0^\top\succeq(\gamma/2)I_m,\qquad
\rho(t)\le Ye^{-\lambda t/2},\\
H\ge1,\qquad 8H\sqrt F\le\beta^{5L},\qquad
\max_a\|h^{(\ell)}(t,v_a)\|/\sqrt n\le B:=2H.
\end{gathered}
\tag{3}
\]

For both \(\ell=L\) and \(\ell=L-1\), the forward velocity recursion
in that proof gives

\[
\frac{\|\dot h^{(\ell)}(t,v_a)\|}{\sqrt n}
\le2F\rho(t)\|b(t)\|.
\tag{4}
\]

This uses \(F_{L-1}\le F_L\); deleting one top neuron leaves the same
bounds valid with the original normalization.

For the independent root \(g\), put
\(H_a(t)=h^{(L-1)}(t,v_a)/\sqrt n\). Define the conditional Gaussian
feature Gram

\[
(C_0)_{ab}=\mathbb E_g[
\phi_L(g^\top H_a(0))\phi_L(g^\top H_b(0))].
\tag{5}
\]

We also impose the initialization event

\[
\tfrac12 A_0A_0^\top\preceq C_0\preceq2A_0A_0^\top.
\tag{6}
\]

Its probability tends to one. Indeed the fitting proof gives
\(A_0A_0^\top\to Q^{(L)}\) in probability. The lower initialized
Gram converges to \(Q^{(L-1)}\), and continuity of the Gaussian
activation covariance map, established in that same proof, gives
\(C_0\to Q^{(L)}\). Since \(Q^{(L)}\succeq\gamma I_m\), on
the event that each matrix differs from \(Q^{(L)}\) by at most
\(\gamma/4\) in operator norm, their relative comparison constants
are \(3/5\) and \(5/3\), which imply (6). The top-neuron deletion
preserves these limits. No independence between the two matrices is needed.

Fix any cavity satisfying (3) and (6) for the rest of the proof. Define

\[
b_*=A_0^\top(A_0A_0^\top)^{-1}y,\qquad B_*=\|b_*\|>0.
\tag{7}
\]

This is the minimum-Euclidean-norm initialized readout fitting the labels:
\(A_0b_*=y\). The initial feature bounds and (3) give

\[
\frac{2Y}{3H}\le B_*\le\frac{\sqrt2Y}{\sqrt\lambda}.
\tag{8}
\]

For the lower bound, \(\|A_0\|\le(3H/2)\sqrt m\), while
\(\|y\|=\sqrt mY\). For the upper bound, use the least singular
value in (3).

## 2. All actual readouts are controlled by the initialized interpolant

Define the accumulated residual activity and readout maximum by

\[
\alpha(t)=\int_0^t2\rho(s)\,ds,\qquad
\alpha=\alpha(\infty)\le4Y/\lambda,\qquad
S_t=\sup_{0\le s\le t}\|b(s)\|.
\]

Equation (4) gives

\[
\|A(t)-A_0\|\le\sqrt m F\alpha(t)S_t.
\tag{9}
\]

Differentiate the squared distance to (7), using (2):

\[
\begin{aligned}
\frac d{dt}\|b-b_*\|^2
&=-\frac4m r^\top A(t)(b-b_*)\\
&=-\frac4m\|r\|^2
 +\frac4m r^\top[A(t)-A_0]b_*\\
&\le4F\rho(t)\alpha(t)S_tB_*.
\end{aligned}
\]

Fixing a terminal time \(T\), replacing \(S_t\) by \(S_T\), and
using \(d\alpha=2\rho\,dt\), one obtains for every \(t\le T\)

\[
\|b(t)-b_*\|^2
\le B_*^2+F\alpha(T)^2S_TB_*.
\]

Therefore
\(S_T\le B_*+\sqrt{B_*^2+F\alpha^2S_TB_*}\).
If \(S_T\ge B_*\), squaring after subtracting \(B_*\) gives
\(S_T\le(2+F\alpha^2)B_*\); if \(S_T<B_*\), the same bound
already holds. Set \(\varepsilon=F\alpha^2\). Then

\[
S:=\sup_{t\ge0}\|b(t)\|\le(2+\varepsilon)B_*\le3B_*.
\tag{10}
\]

The final inequality will follow from the original-cap checks below.

Introduce the integrated residual coefficient

\[
c(t)=-\frac2m\int_0^t r(s)\,ds\in\mathbb R^m.
\tag{11}
\]

Integrating (2) and subtracting \(A_0^\top c(t)\), equations (9)
and \(m^{-1}\sum_a|r_a|\le\rho\) give

\[
\begin{aligned}
\|b(t)-A_0^\top c(t)\|
&\le\frac2m\int_0^t
 \|A(s)-A_0\|\,\|r(s)\|\,ds\\
&\le\frac F2\alpha(t)^2S_t
\le\varepsilon S.
\end{aligned}
\tag{12}
\]

This error is relative to \(B_*\) through (10), rather than to the
coarser upper bound \(Y/\sqrt\lambda\).

Final fitting supplies a lower bound of the same scale. From (9), for
each \(z\in\mathbb R^m\),

\[
\|(A_\infty-A_0)^\top z\|
\le\eta\|A_0^\top z\|,\qquad
\eta:=\sqrt{2/\lambda}\,F\alpha S
\le24F(Y/\lambda)^2.
\tag{13}
\]

The last inequality uses (8) and (10). Hence
\(A_\infty A_\infty^\top\preceq
(1+\eta)^2A_0A_0^\top\). Both matrices are positive definite by
the fitting event. Inverting this positive-definite inequality gives

\[
\|b_\infty\|
\ge\|A_\infty^\top(A_\infty A_\infty^\top)^{-1}y\|
\ge\frac{B_*}{1+\eta}.
\tag{14}
\]

The first inequality holds because \(A_\infty b_\infty=y\) and the
displayed vector is its minimum-norm solution. Combining (10), (12),
and (14),

\[
\|A_0^\top c(\infty)\|
\ge[1/(1+\eta)-3\varepsilon]B_*.
\tag{15}
\]

## 3. The Gaussian probe has only a relative quadratic remainder

The probe equations are exactly

\[
\begin{aligned}
\dot a&=-\frac2m\sum_b r_b\phi_L(U^\top H_b),\\
\dot U&=-\frac2m\sum_b r_ba\phi_L'(U^\top H_b)H_b,
\qquad a(0)=0,\quad U(0)=g.
\end{aligned}
\tag{16}
\]

Define its initialized-feature comparison, using (11), by

\[
a_{\rm lin}(t,g)=\sum_b c_b(t)\phi_L(g^\top H_b(0)).
\tag{17}
\]

This is a comparison function, not a replacement of the trained probe.
By (5)--(6), for every possibly cavity-dependent vector \(c(t)\),

\[
\frac1{\sqrt2}\|A_0^\top c(t)\|
\le\|a_{\rm lin}(t)\|_{L^2(g)}
\le\sqrt2\|A_0^\top c(t)\|.
\tag{18}
\]

For a finite terminal time \(T\), put

\[
P_T=\sup_{t\le T}\|a(t)\|_{L^2(g)},\qquad
D_T=\sup_{t\le T}\|U(t)-g\|_{L^2(g;\mathbb R^n)}.
\]

These quantities are finite before the following inequalities are solved:
the pointwise probe bounds (8) of `CIRCLE_TRANSPORT_ROUTE.md` and its
Gaussian moment bound (4) already give their finiteness, uniformly in
finite terminal time. Thus no moment assumption is inferred circularly
from the inequality for \(P_T\).

The second equation of (16) and \(\|H_b\|\le B\) imply

\[
D_T\le\alpha\beta B P_T.
\tag{19}
\]

For the lower feature path, (4) gives
\(\|H_b(t)-H_b(0)\|\le F\alpha S\). Since this path is
deterministic conditional on the cavity,

\[
\|g^\top[H_b(t)-H_b(0)]\|_{L^2(g)}
=\|H_b(t)-H_b(0)\|\le F\alpha S.
\tag{20}
\]

Use (19)--(20) and the real Lipschitz bound \(|\phi_L'|\le\beta\)
in the integrated first equation of (16). Minkowski's inequality gives

\[
\begin{aligned}
\sup_{t\le T}\|a(t)-a_{\rm lin}(t)\|_{L^2(g)}
&\le\alpha\beta(F\alpha S+BD_T)\\
&\le\varepsilon_1S+\varepsilon_2P_T,
\end{aligned}
\tag{21}
\]

where
\(\varepsilon_1=\alpha^2\beta F\) and
\(\varepsilon_2=\alpha^2\beta^2B^2\).
No \(\sqrt n\) factor occurs: the Gaussian projection in (20) is
evaluated in its actual one-dimensional variance.

By (12), (18), and the constants checked below,

\[
\sup_t\|a_{\rm lin}(t)\|_{L^2(g)}
\le\sqrt2(1+\varepsilon)S\le2S.
\]

It follows from (21) that

\[
P_T\le\frac{2+\varepsilon_1}{1-\varepsilon_2}S\le3S.
\tag{22}
\]

This bound is independent of \(T\). Equation (19) then bounds the
incoming displacement in \(L^2\). Linear growth of \(\phi_L\),
the Gaussian projection bound \(\|g^\top H_b(t)\|_2\le B\), and
integrability of \(\rho\) show
\(\int_0^\infty\|\dot a(t)\|_{L^2}\,dt<\infty\).
Therefore \(a(t)\to a_\infty\) in \(L^2\), consistently with
the pointwise probe endpoint. Passing to the limit in (21)--(22) yields

\[
\|a_\infty-a_{\rm lin}(\infty)\|_{L^2(g)}
\le(\varepsilon_1+3\varepsilon_2)S
\le3(\varepsilon_1+3\varepsilon_2)B_*.
\tag{23}
\]

## 4. The original cap closes every estimate

From (3), \(H\ge1\), and \(\alpha\le4Y/\lambda\),

\[
F\le\beta^{10L}/64,\qquad
\alpha\le4\beta^{-30L},\qquad
B\le\beta^{2L}.
\]

The last bound follows from
\(B=2H\le2(2\beta)^L\le\beta^{2L}\), for
\(\beta\ge10\), \(L\ge2\). Consequently

\[
\begin{aligned}
\varepsilon&\le\tfrac14\beta^{-50L}<1/100,\\
\eta&\le\tfrac38\beta^{-50L}<1/4,\\
\varepsilon_1&\le\tfrac14\beta^{-50L+1}<1/100,\\
\varepsilon_2&\le16\beta^{-56L+2}<1/100.
\end{aligned}
\tag{24}
\]

There is no circular use of these bounds: \(\varepsilon<1\) first
proves (10), then (8) and (10) prove (13), after which the stated bound
for \(\eta\) follows.

Finally (15), (18), and (23) give

\[
\begin{aligned}
\|a_\infty\|_{L^2(g)}
&\ge\left\{
\frac{1/(1+\eta)-3\varepsilon}{\sqrt2}
-3(\varepsilon_1+3\varepsilon_2)\right\}B_*\\
&\ge\left(\frac{77}{100\sqrt2}-\frac{12}{100}\right)B_*
>\frac14 B_*\ge\frac{Y}{6H}.
\end{aligned}
\]

This proves (1) on an initialization/fitting event of probability tending
to one, with a bound independent of width.

The conclusion supplies a uniform nonzero readout norm, not a claim about
its centered variance. The direct probe field still undergoes the exact
training compensation in `ENDPOINT_SEPARATION_CAVITY.md`; this argument
does not bound that compensated field away from zero. It therefore
advances the signal-size component of the transport route while leaving
the actual fitted-circle fluctuation theorem open.
