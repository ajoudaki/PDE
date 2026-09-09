# Polynomial tangent bound for the two-input constant-control arctangent flow

## Result and exact scope

Let
\[
\phi(z)=1+\frac{\arctan z}{10},\qquad
p(z)=\phi'(z)=\frac{1}{10(1+z^2)},\qquad
C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\quad |\rho|<1.
\]
For an arbitrary **constant** vector \(u\in\mathbb R^2\), let \(z(t;z_0,u)\) solve
\[
\dot z=C\operatorname{diag}(p(z_1),p(z_2))u,\qquad z(0)=z_0.
\]
All vector and operator norms below are Euclidean unless indicated otherwise.
Put
\[
k=|\rho|,\qquad \delta=1-k,\qquad
\kappa=\frac{1+k}{1-k},\qquad R=1+|z_{0,1}|+|z_{0,2}|.
\]
Then, uniformly over all constant \(u\) and all \(t\geq0\),
\[
\|D_{z_0}z(t;z_0,u)\|_{2\to2}
\leq \sqrt\kappa\,
\exp\!\left(\frac{10R}{\delta}\right)
(1+t\|u\|_2)^{120R/\delta}. \tag{1}
\]
The constants are deliberately loose. In particular, neither the exponent nor
the prefactor depends on the direction or relative sizes of the components of
\(u\). Zero control components are included. The same statement holds for real
\(t\) with \(|t|\) in place of \(t\), by replacing \(u\) by \(-u\).

Thus the requested pointwise polynomial estimate holds globally. Its dependence
on \(z_0\) permits integration of every finite moment against every Gaussian law;
an explicit bound is given below. This does not assert polynomial growth after
Gaussian averaging, a bound for time-dependent controls, or a bound for trained
or coupled parameter dynamics.

The proof first isolates the part of the activation derivative that can enlarge
the tangent vector. A scalar potential controls this part when the control
components have comparable sizes. If one component is too small for that
argument, an elementary invariant region forces traversal into a tail where
the same growth integral is logarithmic. No specialized external theorem,
simulation, or numerical experiment is used.

## 1. Reduction and the tangent energy

The vector field is smooth, bounded, and globally Lipschitz for fixed \(u\):
\(p\) and \(p'\) are bounded. The local solution therefore extends for all real
times, since its speed is bounded and it cannot escape to infinity in a finite
time. Differentiating its integral equation with respect to the initial condition
gives the variational equation used below. These are the elementary existence
and differentiable-dependence facts for smooth Lipschitz ordinary differential
equations; no asymptotic theorem for dynamical systems is needed.

Choose signs \(\sigma_i\in\{-1,1\}\) so that
\(\sigma_i u_i=|u_i|\), choosing either sign when \(u_i=0\). Reflect the
coordinates by these signs and rescale time by \(\tau=t/10\). Because \(p\) is
even, the resulting equation, with primes denoting \(\tau\)-derivatives, is
\[
\begin{pmatrix}x\\y\end{pmatrix}'
=C_r\begin{pmatrix}A\\B\end{pmatrix},\qquad
C_r=\begin{pmatrix}1&r\\r&1\end{pmatrix},\qquad
r=\rho\sigma_1\sigma_2,
\tag{2}
\]
where
\[
a=|u_1|,\quad b=|u_2|,\quad
A=\frac{a}{1+x^2},\quad B=\frac{b}{1+y^2}.
\]
Reflections, and coordinate permutations used later, preserve the Euclidean
propagator norm and \(R\).

Define the continuously differentiable potential and its nonnegative negative
derivative by
\[
H(v)=\log(1+v_-^2),\quad v_-=\max\{-v,0\},\qquad
f(v)=-H'(v)=\begin{cases}-2v/(1+v^2),&v<0,\\0,&v\geq0.\end{cases}
\]
In particular, \(0\leq f(v)\leq1\). Set
\[
h(\tau)=A f(x)+B f(y),\qquad
I(\tau)=\int_0^\tau h(s)\,ds.
\tag{3}
\]
For a tangent vector \(\eta\), write
\(E=\eta^TC_r^{-1}\eta\). The variational equation from (2) gives
\[
E'=2\left[-\frac{2ax}{(1+x^2)^2}\eta_1^2
           -\frac{2by}{(1+y^2)^2}\eta_2^2\right].
\]
Each coordinate satisfies \(\eta_i^2\leq E\). For example,
\[
E=\eta_1^2+\frac{(\eta_2-r\eta_1)^2}{1-r^2},
\]
and interchanging coordinates proves the other inequality. Dropping negative
terms in \(E'\) consequently yields \(E'\leq2hE\). Multiplication by
\(\exp(-2I)\) and integration, followed by the eigenvalue bounds
\(1-k\leq\lambda(C_r)\leq1+k\), gives
\[
\|D_{(x_0,y_0)}(x(\tau),y(\tau))\|_{2\to2}
\leq\sqrt\kappa\,e^{I(\tau)}. \tag{4}
\]
Only a bound on the scalar growth integral \(I\) remains.

If \(r\geq0\), then \(x'\geq A\) and \(y'\geq B\), so
\[
\frac{d}{d\tau}[H(x)+H(y)]\leq-h.
\]
It follows that
\[
I(\tau)\leq H(x_0)+H(y_0)
\leq2(|x_0|+|y_0|)\leq2R. \tag{5}
\]
Here we used \(\log(1+v^2)\leq2|v|\). This already proves a
time-independent bound in this sign configuration, including \(\rho=0\).

## 2. Negative effective correlation: elementary path bounds

It remains to consider \(r=-k\), where \(0<k<1\). If \(u=0\), the propagator
is the identity. Otherwise, permute the two coordinates if necessary so that
\(0\leq a\leq b\) and \(b>0\). Then
\[
x'=A-kB,\qquad y'=B-kA.
\tag{6}
\]
Introduce
\[
L(\tau)=\int_0^\tau(A+B)\,ds,\qquad w=x+y.
\]
Since \(|x'|,|y'|\leq A+B\), we have
\[
|x-x_0|,\ |y-y_0|\leq L,\qquad
|x|,|y|\leq R+L,\qquad
w=w_0+\delta L,\qquad L\leq\tau(a+b).
\tag{7}
\]
In particular, \(w\) increases strictly. Also \(h\leq A+B\). The part of a
trajectory with \(w<0\), if present, therefore contributes at most
\[
\frac{(-w_0)_+}{\delta}\leq\frac{R}{\delta} \tag{8}
\]
to \(I\). At the beginning of the part with \(w\geq0\), both coordinate
magnitudes are at most \(2R/\delta\). At any such point at most one coordinate
is negative, so
\[
H(x)+H(y)\leq\log\left(1+(2R/\delta)^2\right)
\quad\text{at that beginning time}. \tag{9}
\]
If the trajectory has not yet reached \(w=0\), (8) alone bounds its entire
growth integral.

The following threshold will split the remaining argument:
\[
L_0=\frac{8R}{k},\qquad M=R+L_0,\qquad
\varepsilon=\frac{k}{4(1+M^2)}. \tag{10}
\]
Although these auxiliary quantities contain \(1/k\), the final estimate does
not acquire such a singularity.

## 3. Comparable controls: a telescoping potential

Assume \(\varepsilon\leq a/b\leq1\). Both controls are positive, and both
ratios \(a/b\) and \(b/a\) are at least \(\varepsilon\). Let
\(\mathcal H=H(x)+H(y)\). Equation (6) gives the exact identity
\[
h+2\mathcal H'
=f(x)(2kB-A)+f(y)(2kA-B). \tag{11}
\]
We claim that on \(w\geq0\),
\[
h\leq-2\mathcal H'
   +K\frac{A+B}{\sqrt{1+w^2}},\qquad
K=4k\sqrt{\frac{2k}{\varepsilon}}. \tag{12}
\]
To verify this, suppose first that \(x<0\). Then \(y=w+|x|\geq w\geq0\),
so the second term on the right side of (11) vanishes. If \(2kB-A\leq0\),
(12) holds immediately. Otherwise \(A<2kB\), which implies
\[
1+x^2>\frac{a}{2kb}(1+y^2)
\geq\frac{\varepsilon}{2k}(1+y^2).
\]
Consequently,
\[
f(x)\leq\frac{2}{\sqrt{1+x^2}}
\leq\frac{2\sqrt{2k/\varepsilon}}{\sqrt{1+w^2}},
\]
and \(f(x)(2kB-A)\leq K B/\sqrt{1+w^2}\). If \(y<0\), the identical
argument with the coordinates exchanged uses \(b/a\geq\varepsilon\) and
gives \(K A/\sqrt{1+w^2}\). If neither coordinate is negative, both terms
in (11) vanish. These cases prove (12).

Integrate (12) over the portion with \(w\geq0\), use \(\mathcal H\geq0\),
(9), and \(w'=\delta(A+B)\). Write \(S=\tau(a+b)\) for the final time
under consideration. The remaining integral is bounded by
\[
\int\frac{A+B}{\sqrt{1+w^2}}\,ds
=\frac{\operatorname{arsinh}(w_{\rm end})
       -\operatorname{arsinh}(w_{\rm start})}{\delta}
\leq\frac{\log(1+2S)}{\delta}. \tag{13}
\]
Indeed, \(w_{\rm start}\geq0\); the function \((1+w^2)^{-1/2}\) decreases
there, so an increment of length \(d\) has integral at most
\(\operatorname{arsinh}d\). Here \(d\leq\delta S\leq S\), and
\(\operatorname{arsinh}d=\log(d+\sqrt{1+d^2})\leq\log(1+2d)\).

Combining (8), (9), and (13), and using
\(\log(1+v^2)\leq2v\) for \(v\geq0\), gives
\[
I(\tau)\leq\frac{9R}{\delta}
             +\frac{K}{\delta}\log(1+2S). \tag{14}
\]
The threshold in (10) makes the coefficient linear in \(R\):
\[
K=8\sqrt2\,k\sqrt{1+M^2}
\leq8\sqrt2\,[k+(k+8)R]
\leq80\sqrt2\,R<120R. \tag{15}
\]
This argument uses a telescoping potential and requires no assumption about
the number of coordinate turning points.

## 4. A small control component: entry into an invariant tail region

Assume \(0\leq a/b\leq\varepsilon\). This case includes \(a=0\).
While \(L\leq L_0\), (7) gives \(|y|\leq M\), hence
\[
\frac AB=\frac ab\frac{1+y^2}{1+x^2}
\leq\varepsilon(1+M^2)=\frac k4. \tag{16}
\]
During this part of the path,
\[
y'=B-kA\geq\frac34B>0.
\]
The contribution of \(Af(x)\) is at most
\(\int A\,ds\leq(k/4)L_0=2R\). Monotonicity of \(y\), together with
\(f=-H'\), bounds the other contribution by
\[
\int Bf(y)\,ds\leq\frac43\int f(y)y'\,ds
\leq\frac43 H(y_0)\leq\frac43\log(1+y_0^2). \tag{17}
\]

If the observation time occurs before \(L=L_0\), these estimates already
suffice. Otherwise, at \(L=L_0\) the trajectory has entered
\[
\mathcal K=\{(x,y): y\geq0,\ x+(k/2)y\leq0\}. \tag{18}
\]
Here is a direct verification. Since \(L'=A+B>0\), parameterize this initial
part by \(L\) and set \(g=x+(k/2)y\). From (16),
\[
\frac{dy}{dL}=\frac{1-k(A/B)}{1+A/B}\geq\frac35,
\]
and
\[
\frac{dg}{dL}
=\frac{(1-k^2/2)(A/B)-k/2}{1+A/B}
\leq-\frac k5.
\]
Using \(y_0\geq-R\), \(g_0\leq R\), and \(L_0=8R/k\) proves
\[
y(L_0)\geq-R+\frac{24R}{5k}>0,\qquad
g(L_0)\leq-\frac35R<0.
\tag{19}
\]

The region \(\mathcal K\) is forward invariant. In fact, throughout that region
\(|x|\geq(k/2)y\), and therefore
\[
\frac AB\leq\frac{4\varepsilon}{k^2}
=\frac{1}{k(1+M^2)}\leq\frac k{64}<\frac k4,
\tag{20}
\]
where \(M\geq8/k\) was used. Thus \(y'>0\) and
\(g'\leq-kB/4<0\). At either boundary the vector field points strictly into
\(\mathcal K\), which excludes a first exit by continuity. This proves the
claimed invariance without a trajectory classification.

After entry, \(y>0\), \(x<0\), and (20) implies
\[
-x'=kB-A\geq3A.
\]
Only the first coordinate contributes to \(h\), and its integral is
logarithmic:
\[
\int_{\rm entry}^{\tau}h\,ds
\leq\frac13\int_{\rm entry}^{\tau}f(x)(-x')\,ds
=\frac13\log\frac{1+x(\tau)^2}{1+x_{\rm entry}^2}
\leq\frac13\log\bigl(1+(R+S)^2\bigr). \tag{21}
\]
Combining (17) and (21), or using just (17) if entry has not yet occurred,
gives
\[
\begin{aligned}
I(\tau)
&\leq2R+\frac43\log(1+y_0^2)
         +\frac13\log\bigl(1+(R+S)^2\bigr)\\
&\leq2R+\frac{10}{3}\log(1+R)+\frac23\log(1+S)\\
&\leq6R+\frac23\log(1+S).
\end{aligned} \tag{22}
\]
For the second inequality, use
\(1+(R+S)^2\leq(1+R+S)^2\leq(1+R)^2(1+S)^2\).

## 5. Returning to the raw coordinates

Let \(T=t\|u\|_2\). Since \(\tau=t/10\),
\[
2S=\frac t5(a+b)\leq\frac{\sqrt2}{5}T\leq T.
\]
Each of (5), (14)--(15), and (22) is consequently bounded by
\[
I(\tau)\leq\frac{10R}{\delta}
       +\frac{120R}{\delta}\log(1+T). \tag{23}
\]
Substituting into (4), and undoing the orthogonal coordinate changes, proves
(1) for every constant control and every initial point.

## 6. Explicit Gaussian integrability and its limitation

Suppose \(Z_0\) has a Gaussian law on \(\mathbb R^2\) with mean \(m\) and
covariance \(\Sigma\), which may be singular. Fix a deterministic constant
control \(u\), a finite time \(t\), and a moment order \(q>0\). Define
\[
\lambda=\frac{q}{\delta}\bigl(10+120\log(1+t\|u\|_2)\bigr).
\]
Equation (1) gives
\[
\mathbb E\|D_{Z_0}z(t;Z_0,u)\|_{2\to2}^{q}
\leq\kappa^{q/2}\,\mathbb E\exp\bigl(\lambda(1+\|Z_0\|_1)\bigr).
\]
For any \(v\in\mathbb R^2\),
\[
e^{\lambda\|v\|_1}
\leq\sum_{s\in\{-1,1\}^2}e^{\lambda s^Tv}.
\]
Completing the square in the one-dimensional Gaussian integrals gives
\(\mathbb E e^{\lambda s^TZ_0}
=\exp(\lambda s^Tm+\lambda^2s^T\Sigma s/2)\).
The same calculation applies to a singular covariance by writing
\(Z_0=m+BG\), where \(G\) has independent standard Gaussian coordinates and
\(BB^T=\Sigma\). Since \(s^T\Sigma s\leq2\|\Sigma\|_{2\to2}\),
\[
\mathbb E\|D_{Z_0}z(t;Z_0,u)\|_{2\to2}^{q}
\leq4\kappa^{q/2}
\exp\!\left(
\lambda(1+\|m\|_1)+\lambda^2\|\Sigma\|_{2\to2}
\right)<\infty. \tag{24}
\]
Thus there is no Gaussian-integrability cutoff in time or in the finite moment
order. On bounded sets of initial conditions, (1) is a uniform polynomial in
\(1+t\|u\|_2\). After Gaussian averaging, (24) instead supplies an upper bound
of the form \(\exp(O((1+\log(1+t\|u\|_2))^2))\), with the constant depending
on \(\rho,q,m,\Sigma\). Whether that averaged estimate can be improved to a
polynomial is not resolved here and is not needed for the pointwise claim.

The pointwise constant-control question is fully resolved by (1). The argument
uses the constancy of the signs and component ratio of \(u\), especially in
(10), (16), and (20). It makes no assertion about varying controls, a common
Killing metric, or any full trained dynamics.
