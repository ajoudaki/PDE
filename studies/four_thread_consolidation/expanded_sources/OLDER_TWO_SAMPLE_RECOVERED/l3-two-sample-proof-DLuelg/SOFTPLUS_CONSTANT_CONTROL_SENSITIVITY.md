# Softplus constant-control sensitivity: an exponential counterexample and signed bounds

## Result and scope

Let
\[
\phi(z)=1+\varepsilon\log(1+e^z),\qquad
p(z)=\varepsilon f(z),\qquad
f(z)=\frac{e^z}{1+e^z},\qquad \varepsilon=\frac1{10},
\]
and let \(C_\rho=\left(\begin{smallmatrix}1&\rho\\\rho&1\end{smallmatrix}\right)\),
where \(|\rho|<1\). For a constant \(q\in\mathbb R^2\), write
\[
\frac{dz}{ds}=C_\rho\operatorname{diag}(p(z_1),p(z_2))q,
\qquad z(0)=z_0,\qquad J(s)=D_{z_0}z(s;z_0,q).
\]
All norms below are Euclidean vector or induced operator norms, and \(s\geq0\).

There is **no global pointwise polynomial or subexponential bound** in
\(T=\|q\|_2s\), even allowing arbitrary finite constants depending on the fixed
initial point and on \(\rho\). For every \(\rho=-k\in(-1,0)\), the constant
control \(q=(1,1)\) has a rigorously constructed fixed initial point such that
\[
\|J(s)\|\geq \exp(\varepsilon c_k s),\qquad
c_k=\min\left\{\frac{k}{2}\left(1-\frac{k}{2}\right),\ k(1-k)\right\}>0.
\tag{1}
\]
In particular, for \(\rho=-1/2\) this initial point belongs to
\([ -\log3,0]\times\{\log3\}\), and
\[
\|J(s)\|\geq e^{3s/160}
=\exp\left(\frac{3T}{160\sqrt2}\right).
\tag{2}
\]
The initial point is independent of the observation time. Section 4 defines it
uniquely by a convergent shooting construction; no numerical approximation or
frozen-coordinate substitution is involved.

The sign distinction matters. For opposite signs of the two nonzero controls,
there is a polynomial bound, including the configuration in which the
cross-balanced coordinate is driven toward the zero-gate tail. Put
\[
k=|\rho|,\qquad \kappa=\frac{1+k}{1-k},\qquad
H(v)=\log(1+e^{-v}),\qquad r_+=\max\{r,0\}.
\]
In the mixed-sign cases, relabel the coordinates so that \(q=(a,-b)\), with
\(a,b>0\), and write \(z_0=(x_0,y_0)\). The following bounds hold uniformly
over the indicated constant controls:

| Control and correlation | Bound for \(\|J(s)\|\) |
| --- | --- |
| \(q_1,q_2\leq0\), any \(\rho\) | \(\sqrt\kappa\) |
| \(q_1,q_2\geq0\), \(\rho\geq0\) | \(\sqrt\kappa\,e^{H(z_{0,1})+H(z_{0,2})}\) |
| \(q=(a,-b)\), \(\rho\leq0\) | \(\sqrt\kappa\,e^{H(x_0)}\) |
| \(q=(a,-b)\), \(\rho=k>0\) | \(\sqrt\kappa\,\exp\{H(x_0)+k+\frac{k}{1-k}(y_0-x_0)_+\}(1+\varepsilon b s)^{k/(1-k)}\) |
| One positive control, the other zero, any \(\rho\) | \(\sqrt\kappa\,e^{H(x_0)}\), with \(x_0\) the actively controlled coordinate |

These estimates and the counterexample cover every sign configuration; the
counterexample row does not assert failure for every positive control direction
or every initial point when \(\rho<0\).

The mixed-sign polynomial has an exponent independent of the initial point and
of the control ratio. Its displayed prefactor specifies its tail dependence;
it is uniform on bounded initial sets, not claimed uniform on all of
\(\mathbb R^2\). Since \(\varepsilon b s\leq T\), it is also a polynomial
bound in \(1+T\). In contrast, (2) rules out a bound even at one fixed finite
initial point in the remaining sign configuration.

The proof below is self-contained. The permitted arctangent note was read for
comparison, and the route registry was read to check scope. Neither is used as
authority for a logistic estimate. There are no experiments, auxiliary agents,
or claims about trained dynamics or time-dependent controls.

## 1. Flow, tangent equation, and energy

Use the rescaled time \(\tau=\varepsilon s\), and let a dot denote its
derivative. Then
\[
\dot z=C_\rho\begin{pmatrix}q_1f(z_1)\\q_2f(z_2)\end{pmatrix},
\qquad f'(v)=f(v)(1-f(v)),\qquad 0<f<1,\quad 0<f'\leq\frac14.
\tag{3}
\]
The vector field \(F\) is bounded by \((1+k)\|q\|_2\), and its derivative
is bounded by \(L=(1+k)\|q\|_\infty/4\). These facts give a complete smooth
flow; the elementary justification needed here is as follows. Starting with
the constant function \(z^{(0)}(\tau)=z_0\), iterate
\(z^{(n+1)}=z_0+\int_0^\tau F(z^{(n)}(r))\,dr\). On an interval of length
\(R\), successive differences are bounded by
\(M L^nR^{n+1}/(n+1)!\), where \(M=(1+k)\|q\|_2\).
Their series converges uniformly, and its limit satisfies the integral
equation. Iterating the difference inequality for two solutions proves
uniqueness and the bound \(e^{LR}\) times their initial separation. This
argument works on every finite interval (also for \(-F\)); bounded speed
excludes finite escape.

For completeness, differentiability in \(z_0\) follows from the same integral
argument. Here \(f''=f'(1-2f)\) is bounded, so \(DF\) is globally Lipschitz.
If \(\Delta\) is the difference of solutions initially separated by \(h\),
then \(\sup_{[0,R]}|\Delta|\leq e^{LR}|h|\). Taylor's formula with the
Lipschitz bound on \(DF\) gives
\[
\Delta(\tau)=h+\int_0^\tau DF(z(r))\Delta(r)\,dr+\mathcal R(\tau),
\qquad \sup_{[0,R]}|\mathcal R|\leq K_R|h|^2
\]
for a finite \(K_R\). The linear integral equation with the remainder removed
has a solution by the same convergent iteration. Subtracting the two equations
and iterating the difference inequality bounds the error by
\(K_Re^{LR}|h|^2\). This proves the derivative and its equation:
\[
\dot\eta=C_\rho\operatorname{diag}
\bigl(q_1f'(z_1),q_2f'(z_2)\bigr)\eta.
\tag{4}
\]
For any tangent vector define \(E=\eta^TC_\rho^{-1}\eta\). Direct calculation
gives
\[
\dot E=2\sum_{i=1}^2q_if'(z_i)\eta_i^2,
\qquad
E=\eta_1^2+\frac{(\eta_2-\rho\eta_1)^2}{1-\rho^2}.
\tag{5}
\]
Exchanging the coordinates also shows \(\eta_2^2\leq E\). Thus, with
\[
I(\tau)=\int_0^\tau\sum_{i:q_i>0}q_if'(z_i(r))\,dr,
\]
we have \(\dot E\leq2\dot I E\). Differentiating \(Ee^{-2I}\) and
integrating yields the energy estimate. The eigenvalues \(1\pm\rho\) of
\(C_\rho\) then give
\[
\|J(s)\|\leq\sqrt\kappa\,e^{I(\varepsilon s)}.
\tag{6}
\]
In particular, if both controls are nonpositive, \(E\) is nonincreasing.
If \(q=0\), the exact tangent is the identity.

## 2. The configurations with bounded positive-curvature integral

Write \(g=1-f\), so \(H'=-g\) and \(f'=fg\).
If both controls are nonnegative and \(\rho\geq0\), then
\(\dot z_i\geq q_if(z_i)\), and hence
\[
-\frac{d}{d\tau}\bigl(H(z_1)+H(z_2)\bigr)
\geq\sum_i q_if'(z_i).
\]
Integration and \(H\geq0\) prove the second row of the table.

For mixed signs write \(q=(a,-b)\). If \(\rho\leq0\), the positive-control
coordinate satisfies \(\dot x=af(x)+kbf(y)\geq af(x)\). Therefore
\(-\dot H(x)\geq af'(x)\), proving the third row. If the other control
is zero, \(\dot x=af(x)\) for either sign of \(\rho\), proving the last
row. These arguments do not assume the other coordinate is monotone.

## 3. Opposite controls and positive correlation: the zero-tail estimate

Let \(q=(a,-b)\), \(a,b>0\), and \(\rho=k\in(0,1)\). Define
\(A=af(x)\), \(B=bf(y)\). The complete equations are
\[
\dot x=A-kB,\qquad \dot y=kA-B.
\tag{7}
\]
The gap \(w=x-y\), rather than either coordinate separately, is strictly
increasing:
\[
\dot w=(1-k)(A+B)>0.
\tag{8}
\]
The positive-curvature integral satisfies the exact identity
\[
I(\tau)=H(x_0)-H(x(\tau))
       +k\int_0^\tau B(r)g(x(r))\,dr.
\tag{9}
\]
The logistic factors have the useful product bound
\[
f(y)g(x)=\frac{e^y}{(1+e^y)(1+e^x)}\leq e^{y-x}=e^{-w}.
\tag{10}
\]
Fix the final rescaled time \(\tau\), and set \(W=\log(1+b\tau)\).
On the part of the path with \(w\leq W\), use \(Bg(x)\leq B\) and (8).
Because \(w\) is increasing, this part is an initial interval, possibly empty,
and its contribution is at most
\[
\int_{\{w\leq W\}}B\,dr
\leq\frac{(W-w_0)_+}{1-k}.
\]
On the remainder, (10) gives \(Bg(x)\leq b e^{-W}\). Consequently,
\[
\int_0^\tau Bg(x)\,dr
\leq\frac{(W-w_0)_+}{1-k}+\frac{b\tau}{1+b\tau}
\leq\frac{\log(1+b\tau)+(-w_0)_+}{1-k}+1.
\tag{11}
\]
Combining (9)--(11), discarding only the nonpositive term \(-H(x(\tau))\),
and using (6) proves exactly the mixed-sign polynomial in the table.
No restriction on the sign of \(\dot x\) or \(\dot y\) was imposed.

Here is a direct check of why a persistent finite balance cannot be inserted
into (7). At an instantaneous balance \(A=kB\),
\[
\dot y=-(1-k^2)B<0,\qquad
\ddot x=k(1-k^2)B^2g(y)>0.
\tag{12}
\]
The first coordinate is at a strict local minimum, and the second coordinate
is moving toward the gate's zero tail. More generally, the positive-control
coordinate cannot remain in any fixed compact interval for all sufficiently
large times. Indeed,
\[
y(\tau)-kx(\tau)
=y(\tau_0)-kx(\tau_0)-(1-k^2)\int_{\tau_0}^\tau B(r)\,dr.
\tag{13}
\]
If \(x\in[m,M]\) forever after \(\tau_0\) and the integral in (13) is
finite, then \(y\) is bounded, making \(B=bf(y)\) bounded below by a
positive constant, a contradiction. If the integral is infinite, then
\(y\to-\infty\) and \(B\to0\). In that case
\(\dot x\geq af(m)/2>0\) eventually, again a contradiction. Thus the
finite-balance mechanism used next is unavailable here. The quantitative
replacement is the fully proved logarithmic estimate (11).

## 4. Two positive controls and negative correlation: an actual trajectory

Fix \(k\in(0,1)\), \(\rho=-k\), and \(q=(1,1)\). Now
\[
\dot x=f(x)-kf(y),\qquad \dot y=f(y)-kf(x).
\tag{14}
\]
Define the explicit constants
\[
L_k=\log\frac{k}{2-k},\qquad
U_k=\log\frac{k}{1-k},\qquad
Y_k=\log\frac{1+k}{1-k},\qquad
d_k=\frac{1+k}{2}-k^2=\frac{(1-k)(1+2k)}2>0.
\tag{15}
\]
Thus \(f(L_k)=k/2\), \(f(U_k)=k\), and \(f(Y_k)=(1+k)/2\).
In the strip
\[
L_k\leq x\leq U_k,\qquad y\geq Y_k,
\tag{16}
\]
the second equation of (14) satisfies
\(d_k\leq\dot y\leq1\). We may therefore use \(y\) as the independent
variable and consider
\[
\frac{dX}{dy}=G(X,y),\qquad
G(X,y)=\frac{f(X)-kf(y)}{f(y)-kf(X)}.
\tag{17}
\]
The denominator is at least \(d_k\) throughout the strip. At its two
horizontal boundaries,
\[
G(L_k,y)<0,\qquad G(U_k,y)>0
\quad\text{for every finite }y\geq Y_k.
\tag{18}
\]
For the lower sign the numerator is at most \(-k^2/2\); for the upper sign
it equals \(k(1-f(y))>0\).

For each positive integer \(n\), solve (17) backward from
\(X_n(Y_k+n)=U_k\) down to \(Y_k\). This solution exists throughout that
interval and stays in \([L_k,U_k]\). To verify this assertion, reverse the
independent variable: (18) makes the vector field point strictly into the
interval at both endpoints. A first exit would have to cross an endpoint in
the opposite direction to its derivative there, which is impossible. Inside
the strip, \(G\) and \(\partial_XG\) are bounded; the integral-iteration
argument of Section 1 gives local existence and uniqueness, and these bounds
allow extension across every finite subinterval. The solution is strictly
inside the interval at all times before its terminal endpoint.

If \(m>n\), then \(X_m(Y_k+n)<U_k=X_n(Y_k+n)\). Uniqueness prohibits
two scalar solutions from meeting, so
\(X_m(Y_k)<X_n(Y_k)\). The sequence
\(\alpha_n=X_n(Y_k)\) is decreasing and bounded below by \(L_k\). Define
\[
\alpha_k=\lim_{n\to\infty}\alpha_n.
\tag{19}
\]
This is a precise initial coordinate, with no dependence on \(s\).

To verify that its solution stays in the strip forever, compute
\[
\partial_XG(X,y)
=\frac{(1-k^2)f'(X)f(y)}{(f(y)-kf(X))^2}.
\tag{20}
\]
This derivative is at most \(M_k=(1-k^2)/(4d_k^2)\). On any fixed interval
\([Y_k,Y_k+R]\), solutions with \(m,n\geq R\) therefore satisfy
\[
\sup|X_m-X_n|\leq e^{M_kR}|\alpha_m-\alpha_n|.
\]
For example, this inequality follows by iterating
\(|X_m(y)-X_n(y)|\leq|\alpha_m-\alpha_n|+
M_k\int_{Y_k}^y|X_m-X_n|\); the resulting exponential series converges.
Thus \(X_n\) converge uniformly on every such interval. Passing to the
integral equation gives a solution \(X\) of (17) with \(X(Y_k)=\alpha_k\)
and \(L_k\leq X(y)\leq U_k\) for all \(y\geq Y_k\).

This bounded graph is unique. On the strip \(f'(X)\geq c_k\), where
\(c_k\) is defined in (1): the function \(u(1-u)\) is concave, so its
minimum for \(u\in[k/2,k]\) occurs at an endpoint. Since the denominator
in (20) is at most one and \(f(y)\geq(1+k)/2\),
\[
\partial_XG\geq (1-k^2)c_k(1+k)/2>0.
\]
The positive difference of two distinct solutions would grow at least
exponentially in \(y-Y_k\), by integrating this differential inequality,
contradicting their common bounded interval. This proves uniqueness in (19).
Also \(L_k<\alpha_k<U_k\), since either endpoint at \(Y_k\) would
immediately leave the strip in forward \(y\).

Return to actual rescaled time by setting
\[
\tau(y)=\int_{Y_k}^y\frac{dr}{f(r)-kf(X(r))}.
\tag{21}
\]
Its derivative is between \(1\) and \(1/d_k\), so it is strictly increasing
onto \([0,\infty)\). Its inverse \(y(\tau)\), together with
\(x(\tau)=X(y(\tau))\), satisfies both equations in (14) exactly, with
\[
z_0=(\alpha_k,Y_k),\qquad
L_k\leq x(\tau)\leq U_k,\qquad
Y_k+d_k\tau\leq y(\tau)\leq Y_k+\tau.
\tag{22}
\]

In fact \(x(\tau)\to U_k\). To see this, fix
\(0<h<U_k-L_k\) and let \(r_h=k-f(U_k-h)>0\). Since \(y\to\infty\),
eventually \(kf(y)\geq k-r_h/2\). At any later point with
\(x\leq U_k-h\), the first equation of (14) would give
\(\dot x\leq-r_h/2\). At the boundary \(x=U_k-h\) it also points
strictly downward, preventing exit upward. The trajectory would then fall
below \(L_k\) in finite time, contradicting (22). Hence
\(x>U_k-h\) eventually, proving the limit.

The mechanism is therefore a finite first coordinate balanced by a second
coordinate escaping into the **nonzero positive tail**:
\[
f(x)\to k,\qquad f(y)\to1,\qquad
\dot x\to0,\qquad \dot y\to1-k^2.
\tag{23}
\]
There is no finite equilibrium being silently substituted here. Indeed, at
any finite point, invertibility of \(C_\rho\) and positivity of both gates
imply \(F(z)=0\) only when \(q=0\).

## 5. Exponential growth of the full tangent on that trajectory

On (22), the tangent equation is
\[
\dot\eta=
\begin{pmatrix}f'(x)&-kf'(y)\\-kf'(x)&f'(y)\end{pmatrix}\eta.
\]
Take the unit initial tangent \(\eta(0)=(1,0)\) and set
\(v=(\eta_1,-\eta_2)\). This is an orthogonal reflection, and its equation
is
\[
\dot v=
\begin{pmatrix}f'(x)&kf'(y)\\kf'(x)&f'(y)\end{pmatrix}v,
\qquad v(0)=(1,0).
\tag{24}
\]
All entries of this matrix are nonnegative. The successive integral expansion
for its fundamental solution is the identity plus integrals of products of
these matrices; every term has nonnegative entries. On a finite interval the
series converges, since its terms are bounded by \(M^n\tau^n/n!\) for a
bound \(M\) on the matrix norm. It follows directly that \(v_1,v_2\geq0\).
Using \(f'(x)\geq c_k\) from the strip,
\[
\dot v_1=f'(x)v_1+kf'(y)v_2\geq c_kv_1,
\qquad v_1(\tau)\geq e^{c_k\tau}.
\]
Since \(|\eta|=|v|\geq v_1\), this proves (1). At \(k=1/2\), (15)
gives \(L_k=-\log3\), \(U_k=0\), \(Y_k=\log3\), and \(c_k=3/16\),
proving (2). As an additional consequence of (23) and
\(v_1\geq\exp(\int_0^\tau f'(x(r))\,dr)\),
\[
\liminf_{s\to\infty}\frac1s\log\|J(s)\|
\geq\varepsilon k(1-k)>0.
\tag{25}
\]
This last inequality uses only that the average of a convergent function has
the same limit: split its integral at a time after which its deviation from
the limit is less than an arbitrary positive number.

## 6. Initial-point uniformity and exact disposition

For the fixed \(\rho=-1/2\), \(q=(1,1)\), and single initial point
\((\alpha_{1/2},\log3)\) defined in (19), every proposed finite bound
\(K(z_0,\rho)(1+T)^{N(z_0,\rho)}\) fails as \(T\to\infty\).
More generally, it fails with \((1+T)^N\) replaced by any positive function
\(B(T)\) satisfying \(\limsup_{T\to\infty}T^{-1}\log B(T)\leq0\).
This follows by taking logarithms in (2): its lower bound has strictly
positive linear rate. Allowing the prefactor also to depend on this fixed
control does not change the contradiction. Scaling the control to
\(q=\lambda(1,1)\), \(\lambda>0\), simply replaces \(s\) by \(\lambda s\)
on the same trajectory, so the counterexample also applies with elapsed time
fixed and amplitude increasing.

Thus tail-dependent constants cannot repair a universal pointwise
subexponential claim: the obstruction already has one fixed finite initial
point in an explicitly bounded set. This is not a lower bound for a set of
initial points of positive measure, and it does not by itself decide any
Gaussian-averaged sensitivity estimate.

The proved mixed-sign bound resolves the zero-tail concern within the stated
constant-control subproblem. The positive-positive, negative-correlation
trajectory gives the requested discriminator and closes this bounded sidecar.
No estimate for arbitrary control histories, no trained-network theorem, and
no transfer to coupled parameter dynamics is asserted.

## Appendix: independent verification of the suggested balanced-control invariant

The author subsequently suggested an invariant for \(q=(1,-1)\) and
\(0\leq\rho<1\). The following calculation verifies it directly, within the
constant-control scope of this note. Set
\[
u=\frac{z_1+z_2}{2},\qquad v=\frac{z_1-z_2}{2},\qquad
\gamma=\frac{1+\rho}{1-\rho}\geq1.
\]
In rescaled time the exact equations are
\[
\dot u=\frac{1+\rho}{2}\bigl(f(u+v)-f(u-v)\bigr),\qquad
\dot v=\frac{1-\rho}{2}\bigl(f(u+v)+f(u-v)\bigr)>0.
\]
Writing the logistic functions over a common denominator gives
\[
f(u+v)-f(u-v)=\frac{\sinh v}{\cosh u+\cosh v},\qquad
f(u+v)+f(u-v)=\frac{\cosh v+e^u}{\cosh u+\cosh v}.
\]
Division is permitted because the sum is positive. Hence
\[
\frac{du}{dv}=\gamma\frac{\sinh v}{\cosh v+e^u}.
\tag{26}
\]
For \(\gamma>1\), define
\[
\mathcal I_\gamma(u,v)
=e^{-u/\gamma}\left(\cosh v-\frac{e^u}{\gamma-1}\right).
\]
Direct differentiation gives
\[
(\mathcal I_\gamma)_u
=-\frac1\gamma e^{-u/\gamma}(\cosh v+e^u),\qquad
(\mathcal I_\gamma)_v=e^{-u/\gamma}\sinh v.
\]
Substituting (26) shows
\((\mathcal I_\gamma)_u\,du/dv+(\mathcal I_\gamma)_v=0\), proving exact
invariance. For each fixed \(v\), its derivative in \(u\) is strictly
negative, and its limits as \(u\to-\infty,+\infty\) are respectively
\(+\infty,-\infty\). Thus every \(I\in\mathbb R\) has a unique inverse
\(u=U(I,v)\).

The inverse derivatives follow by differentiating
\(\mathcal I_\gamma(U(I,v),v)=I\):
\[
|U_I|=\frac{\gamma e^{u/\gamma}}{\cosh v+e^u},\qquad
U_v=\gamma\frac{\sinh v}{\cosh v+e^u},\qquad |U_v|\leq\gamma.
\tag{27}
\]
For an explicit global bound in the first formula, put \(c=\cosh v\geq1\)
and \(t=e^u>0\). The derivative of \(\gamma t^{1/\gamma}/(c+t)\) has the
sign of \(c-(\gamma-1)t\). Its maximum is therefore attained at
\(t=c/(\gamma-1)\), with value
\[
|U_I|\leq
\left(\frac{\gamma-1}{\cosh v}\right)^{(\gamma-1)/\gamma}
\leq(\gamma-1)^{(\gamma-1)/\gamma}.
\tag{28}
\]
Existence of these derivatives also follows directly from the one-variable
difference quotient: the derivative of \(\mathcal I_\gamma\) in \(u\)
never vanishes, so solving its first-order increment for the increment of
\(u\) gives (27).

At \(\gamma=1\), use
\(\mathcal I_1(u,v)=e^{-u}\cosh v-u\). Its derivatives are
\((\mathcal I_1)_u=-e^{-u}\cosh v-1<0\) and
\((\mathcal I_1)_v=e^{-u}\sinh v\). Equation (26) again makes the derivative
along the path vanish. The same endpoint limits prove it is onto, and its
inverse satisfies \(|U_I|\leq1\), \(|U_v|\leq1\).

The invariant describes the state-space trajectories. An endpoint derivative
at fixed elapsed time also involves the evolution of \(v\). That dependence
is already included in the full tangent estimate of Section 3: for balanced
controls and \(\rho>0\), its polynomial exponent is
\(\rho/(1-\rho)=(\gamma-1)/2\). No additional claim about a changing Gram
matrix or forcing is inferred from the invariant.
