# Convex slope: complete two-driver variational response

The requested sufficient bound holds for the prescribed two-driver system. In fact, its full first derivative with respect to both initial coordinates and both (L^1) drivers is bounded by

\[
C_e R^2\exp\bigl((e+L)P+eQ\bigr),\qquad
R=1+|M_0|+|V_0|+P+Q,\quad L=1+e\pi/2.
\]

The derivative is an operator into the space of continuous trajectories, so this also bounds every terminal-time derivative. Both drivers remain present throughout the proof. The exponent is linear, hence strictly subquadratic, in the stated variables. No control-loop counterexample to this bound is possible within the assumptions below.

The proof first verifies the proposed invariant and obtains polynomial state bounds. A second globally nonsingular coordinate, (H=M+M^3/3), then makes both control vector fields globally Lipschitz. This gives the full inhomogeneous variational bound, including a justification that the variation is the actual Fréchet derivative.

## 1. Setup and independent algebra check

Fix (e=1/10), a finite interval ([0,T]), real initial coordinates, and arbitrary signed real drivers (p,q\in L^1(0,T)). Write

\[
P=\int_0^T|p(t)|\,dt,\qquad Q=\int_0^T|q(t)|\,dt,
\qquad \ell=1-e\pi/2>0.
\]

All constants denoted (C_e) depend only on the fixed (e). The activation is

\[
\phi(M)=1+M+e\left[M\arctan M-\tfrac12\log(1+M^2)\right].
\]

Differentiation cancels the two terms (M/(1+M^2)), giving

\[
a(M)=\phi'(M)=1+e\arctan M,\qquad
b(M)=a'(M)=\frac{e}{1+M^2},\qquad
b'(M)=-\frac{2eM}{(1+M^2)^2}.
\]

Thus (\ell\le a\le L), (0<b\le e), and (b'/b=-2M/(1+M^2)). In particular the activation is smooth, strictly convex, and globally Lipschitz. Its positive-order derivatives are bounded: after the first derivative, differentiation produces rational functions with no real poles and bounded behavior at infinity. Its nonlinear part has linear, not bounded, growth. The activation and all constants here are independent of data.

The equations to be analyzed are exactly

\[
M'=a(M)p+Vb(M)q,\qquad V'=a(M)q. \tag{1}
\]

Define

\[
H(M)=M+M^3/3,\qquad
U(M)=\frac2e\int_0^M a(x)(1+x^2)\,dx.
\]

An explicit antiderivative, with (U(0)=0), is

\[
U(M)=\frac2e H(M)+2H(M)\arctan M
-\frac{M^2}{3}-\frac23\log(1+M^2). \tag{2}
\]

Indeed, integration by parts gives

\[
\int_0^M(1+x^2)\arctan x\,dx
=H(M)\arctan M-\frac{M^2}{6}-\frac13\log(1+M^2).
\]

Since

\[
U'(M)=\frac{2a(M)}{b(M)}\ge\frac{2\ell}{e},
\]

(U) is a smooth increasing bijection of the real line with a smooth inverse. For either sign of (M), integrating the positive integrand between (0) and (M) gives

\[
\frac{2\ell}{e}\left(|M|+\frac{|M|^3}{3}\right)
\le |U(M)|\le
\frac{2L}{e}\left(|M|+\frac{|M|^3}{3}\right). \tag{3}
\]

There is no coordinate singularity at zero or at any finite (M).

Set (I=U(M)-V^2) and define (k(u)=2a(m)^2/b(m)), where (m=U^{-1}(u)). Direct substitution into (1) yields

\[
\begin{aligned}
I'&=\frac{2a}{b}(ap+Vbq)-2Vaq=k(U(M))p,\\
V'&=a(M)q.
\end{aligned} \tag{4}
\]

Thus (I) is a forced invariant for general (p); its (q) contribution cancels exactly. The map ((M,V)\mapsto(I,V)) is a global smooth bijection, with inverse (M=U^{-1}(I+V^2)) and Jacobian determinant (2a/b>0).

The derivative of (k) must be taken with respect to (u). Computing numerator and denominator separately gives

\[
\frac{dk}{du}
=\frac{4a-2a^2b'/b^2}{2a/b}
=2b-a\frac{b'}b
=\frac{2e+2a(M)M}{1+M^2}. \tag{5}
\]

Consequently (k>0), (|k'|\le2e+L), and, by (3),

\[
k(u)\le C_k(1+|u|^{2/3}),\qquad
C_k=\frac{2L^2}{e}\max\left\{1,\left(\frac{3e}{2\ell}\right)^{2/3}\right\}. \tag{6}
\]

These independently computed identities agree with the supplied candidate note.

## 2. Polynomial state bounds

The following estimates hold on any existence interval; global existence is justified in the next section. First,

\[
|V(t)|\le K:=|V_0|+LQ. \tag{7}
\]

Let (I_0=U(M_0)-V_0^2), (D=1+K^2), and (W(t)=D+|I(t)|\ge1). The absolute value of an absolutely continuous function is absolutely continuous, with (|(|I|)'|\le|I'|) almost everywhere. Since (|U(M)|=|I+V^2|\le W-1), (4)–(6) imply

\[
W'\le C_k(1+|U(M)|^{2/3})|p|
\le2C_kW^{2/3}|p|
\]

almost everywhere. Division by (3W^{2/3}>0) and integration therefore give the explicit bound

\[
W(t)^{1/3}\le B:=(1+K^2+|I_0|)^{1/3}+\frac{2C_k}{3}P. \tag{8}
\]

In particular,

\[
\sup_t|M(t)|\le\left(\frac{3e}{2\ell}\right)^{1/3}B,
\qquad \sup_t|I(t)|\le B^3,\qquad
\sup_t|U(M(t))|\le B^3. \tag{9}
\]

Here the first inequality uses the cubic term in the lower bound (3). Also (|H(M)|\le e|U(M)|/(2\ell)).

For a simpler bound in the input coordinates, (3) gives

\[
1+K^2+|I_0|\le C_e(1+|M_0|^3+V_0^2+Q^2).
\]

Using ((x+y)^3\le4(x^3+y^3)) for nonnegative (x,y) in (8), we obtain

\[
\sup_t|M(t)|^3\le
C_e(1+|M_0|^3+V_0^2+Q^2+P^3). \tag{10}
\]

Thus, with (R=1+|M_0|+|V_0|+P+Q\ge1),

\[
\sup_t(|M(t)|+|V(t)|)\le C_eR,
\qquad
\sup_t(|H(M(t))|+|U(M(t))|+|I(t)|)\le C_eR^3. \tag{11}
\]

No state bound assumes a sign for either driver or a restriction on their ordering.

## 3. A second nonsingular coordinate controls both vector fields

The coordinate (H(M)=M+M^3/3) is a smooth increasing bijection, with (H'=1+M^2\ge1). Write (m(h)=H^{-1}(h)), and define

\[
f(h)=a(m(h))(1+m(h)^2),\qquad g(h)=a(m(h)).
\]

Equation (1) becomes exactly

\[
h'=f(h)p+eVq,\qquad V'=g(h)q,\qquad h=H(M). \tag{12}
\]

The factor ((1+M^2)b(M)=e) is the crucial cancellation. Differentiating with respect to (h), using (dm/dh=(1+M^2)^{-1}), gives

\[
\begin{aligned}
c(M):=f'(h)&=\frac{e+2a(M)M}{1+M^2},
&|c(M)|&\le e+L=:C_0,\\
d(M):=g'(h)&=\frac{e}{(1+M^2)^2},
&0<d(M)&\le e.
\end{aligned} \tag{13}
\]

In the vector norm (|(x,y)|_1=|x|+|y|), the two vector fields

\[
X(h,V)=(f(h),0),\qquad Y(h,V)=(eV,g(h))
\]

are globally Lipschitz with constants (C_0) and (e), respectively. Their values at the origin have norm one, so they also have at most linear growth. These statements follow directly from (13): the two column sums of (DY) are (d(M)) and (e).

For completeness, the integral map for (12) is a contraction on continuous paths on every subinterval where

\[
\int(C_0|p|+e|q|)<1.
\]

There is a finite partition into such intervals because this nonnegative integrand is integrable. Successive iteration on each interval converges geometrically in the complete supremum norm, providing a unique continuous solution, which is absolutely continuous by its integral equation. Concatenation gives the unique solution on all of ([0,T]). Applying the smooth inverse (m) gives a unique global solution of (1). This also validates (7)–(11) on the full interval.

## 4. Full initial and forcing response

Let ((\mu,\nu,r,s)\in\mathbb R^2\times L^1(0,T)^2) be an arbitrary perturbation of ((M_0,V_0,p,q)). Denote the first variations by ((\delta M,\delta V)), and set

\[
Z=(1+M^2)\delta M=\delta h,\qquad \eta=\delta V.
\]

The full variational equation in (12) is

\[
\begin{pmatrix}Z\\\eta\end{pmatrix}'
=A(t)\begin{pmatrix}Z\\\eta\end{pmatrix}
+\begin{pmatrix}f(h)r+eVs\\a(M)s\end{pmatrix},
\qquad
A(t)=\begin{pmatrix}c(M)p&e q\\d(M)q&0\end{pmatrix}, \tag{14}
\]

with initial value

\[
(Z(0),\eta(0))=((1+M_0^2)\mu,\nu). \tag{15}
\]

An independent check starting in the original variables gives

\[
\delta M'=(bp+Vb'q)\delta M+bq\delta V+ar+Vbs,
\qquad \delta V'=bq\delta M+as.
\]

When differentiating (Z=(1+M^2)\delta M), its diagonal (q) coefficient is

\[
V\left(b'+\frac{2Mb}{1+M^2}\right)q=0,
\]

while its diagonal (p) coefficient is

\[
\left(b+\frac{2aM}{1+M^2}\right)p=c(M)p.
\]

Its other coefficients are ((1+M^2)bq=eq), ((1+M^2)ar=f(h)r), and ((1+M^2)Vbs=eVs), exactly as in (14). In particular, the dangerous-looking (Vb'q) term has been canceled, not discarded or estimated by (|Vq|).

The induced matrix norm satisfies

\[
\|A(t)\|_1\le C_0|p(t)|+e|q(t)|. \tag{16}
\]

Let (Phi(t,\tau)) be its transition matrix. Iteration of the linear integral equation bounds its (n)-th iterated integral by ((\int_\tau^t\|A\|_1)^n/n!). Summing the convergent series gives

\[
\|\Phi(t,\tau)\|_1\le
\exp\left(C_0\int_\tau^t|p|+e\int_\tau^t|q|\right). \tag{17}
\]

The complete response is therefore

\[
\begin{pmatrix}Z(t)\\\eta(t)\end{pmatrix}
=\Phi(t,0)\begin{pmatrix}(1+M_0^2)\mu\\\nu\end{pmatrix}
+\int_0^t\Phi(t,\tau)
\begin{pmatrix}f(h(\tau))r(\tau)+eV(\tau)s(\tau)\\a(M(\tau))s(\tau)\end{pmatrix}\,d\tau. \tag{18}
\]

The right side satisfies (14) and (15) by differentiation almost everywhere; uniqueness follows from the same integral estimate. The transition matrix in both forcing terms contains the actual future evolution of **both** base drivers. In particular, the (q)-forcing response is not replaced by a propagator involving only (p).

Let (B_M=\sup_{[0,T]}|M|). Since (|f(h)|\le L(1+B_M^2)) and (|V|\le K), (17)–(18) yield

\[
\begin{aligned}
\sup_{t\le T}(|Z(t)|+|\eta(t)|)
\le{}&e^{C_0P+eQ}\bigl[
(1+M_0^2)|\mu|+|\nu|\\
&\hspace{19mm}+L(1+B_M^2)\|r\|_1+(eK+L)\|s\|_1\bigr].
\end{aligned} \tag{19}
\]

Because (|\delta M|=|Z|/(1+M^2)\le|Z|), (11) implies

\[
\sup_{t\le T}(|\delta M(t)|+|\delta V(t)|)
\le C_eR^2e^{(e+L)P+eQ}
\bigl(|\mu|+|\nu|+\|r\|_1+\|s\|_1\bigr). \tag{20}
\]

This controls the entire two-by-two initial Jacobian and both (L^1)-to-trajectory forcing derivative operators, as well as any simultaneous perturbation of them. No step sets a base driver equal to zero.

The auxiliary coordinates also have controlled responses:

\[
\delta H=Z,\qquad
\delta U=\frac{2a(M)}e Z,\qquad
\delta I=\frac{2a(M)}e Z-2V\eta. \tag{21}
\]

Thus their full first derivatives have the same exponential factor, with polynomial prefactors at most (C_eR^2) for (H,U) and (C_eR^3) for (I).

## 5. Why these are actual Fréchet derivatives

Consider the solution map from (mathbb R^2\times L^1(0,T)^2) into (C([0,T];\mathbb R^2)), with the sum norm on inputs and the supremum of the vector one-norm on outputs. The transformed vector fields have globally bounded first and second derivatives. For the only nonconstant second derivatives, direct differentiation gives

\[
f''(h)=\frac{2a(M)(1-M^2)}{(1+M^2)^3},\qquad
g''(h)=-\frac{4eM}{(1+M^2)^4}. \tag{22}
\]

Both are bounded. The initial map (M_0\mapsto H(M_0)) is smooth, and the inverse (m) has bounded first and second derivatives:

\[
m'(h)=\frac1{1+M^2},\qquad
m''(h)=-\frac{2M}{(1+M^2)^3}.
\]

Here is a remainder argument covering (L^1), rather than only smooth, driver perturbations. Put (\varepsilon=|\mu|+|\nu|+\|r\|_1+\|s\|_1\le1), and let (Delta x) be the exact transformed trajectory difference. The polynomial state estimate applied to the perturbed inputs gives a uniform bound depending on the base inputs but not on the perturbation. Subtracting the integral equations and using the global Lipschitz constants therefore gives

\[
\|\Delta x\|_\infty\le C_{\mathrm{base}}\varepsilon,
\]

by iteration of the integral inequality, with the same exponential-series argument as in (17).

Subtract from (Delta x) the solution of (14). Taylor's formula with bounded second derivatives shows that the remaining source has integral norm bounded by

\[
C_e(P+Q)\|\Delta x\|_\infty^2
+C_e(\|r\|_1+\|s\|_1)\|\Delta x\|_\infty.
\]

The initial remainder is (O_{\mathrm{base}}(\mu^2)), since

\[
H(M_0+\mu)-H(M_0)-(1+M_0^2)\mu=M_0\mu^2+\mu^3/3.
\]

Applying (17) once more bounds the full transformed remainder by (C_{\mathrm{base}}\varepsilon^2). Taylor's formula for (m) gives the same order for the physical-coordinate remainder. Equation (20) is consequently a bound for the genuine bounded linear Fréchet derivative of the full solution map, not merely for a formal variation equation.

## 6. Gaussian moments and scope

The exponent in (20) is

\[
\psi=(e+L)P+eQ\le C_eR,
\]

so (psi/R^2\to0) as (R\to\infty). This is the requested strictly subquadratic dependence.

To state the probabilistic implication precisely, suppose the random inputs satisfy

\[
\mathbb E\exp(\lambda R^2)<\infty
\quad\text{for some fixed }\lambda>0. \tag{23}
\]

For every finite (r>0), the function (x^{2r}\exp(rC_ex-\lambda x^2)) is bounded on (x\ge1), because its logarithm tends to minus infinity. Therefore

\[
\mathbb E\left[\left(C_eR^2e^{(e+L)P+eQ}\right)^r\right]<\infty. \tag{24}
\]

The same argument allows any fixed polynomial prefactor, including (21). No smallness of the fixed constants is required. Assumption (23) holds, for example, if each of (M_0,V_0,P,Q) has some positive square-exponential moment: use

\[
R^2\le5(1+M_0^2+V_0^2+P^2+Q^2)
\]

and Hölder's inequality with four equal exponents, choosing (lambda) small enough. Independence is unnecessary.

The deterministic coordinate identities, global existence, polynomial state bounds, and full first initial/forcing response bound are all closed here. The Gaussian-moment conclusion is conditional on the explicit input-tail hypothesis (23); having all polynomial moments alone would not imply (23) or justify the exponential moment step. Application-specific Gaussian tail bounds for incoming drivers, transport through trained operators, higher derivative orders, and network or population continuation are not established or assumed by this standalone result.

Only the full `solve-math-rigorously` skill and the supplied `CONVEX_SLOPE_ROUTE.md` were read as instructions/context. No agents, experiments, external sources, or edits to existing files were used.
