# Audit of the generic analytic source-rank construction

The construction is sound. It obstructs a uniform low-rank approximation theorem for the stated class of analytic vector curves. It does not establish that a neural training trajectory belongs to this counterexample family. This scoped audit uses only the supplied construction and the required mathematical presentation instructions.

Let \(n\) tend to infinity through positive integers, and put

\[
\ell=\log(en),\qquad r=\ell^{-1/2},\qquad
h=\frac{8\pi r}{\ell}=8\pi\ell^{-3/2},\qquad
J=\left\lfloor\frac{\ell}{8h}\right\rfloor
 =\left\lfloor\frac{\ell^{5/2}}{64\pi}\right\rfloor.
\]

For sufficiently large \(n\), \(1\le J\le n\). Equip \(\mathbb C^n\) with the Hermitian inner product \(\langle v,w\rangle_n=n^{-1}\sum_{k=1}^n v_k\overline{w_k}\), and its norm \(\|v\|_n=\|v\|_2/\sqrt n\). The real vectors \(v_j=\sqrt n\,e_j\), where \(e_j\) are the coordinate unit vectors, form an orthonormal family. Define

\[
\operatorname{sinc}(w)=
\begin{cases}\sin(w)/w,&w\ne0,\\1,&w=0,\end{cases}
\qquad
a=h\exp\!\left(-\frac{\pi r}{h}\right)=h e^{-\ell/8},
\]
\[
u_n(z)=a e^{-z}\sum_{j=1}^{J}v_j
\operatorname{sinc}\!\left(\pi\left(\frac zh-j\right)\right),
\qquad z\in\mathbb C.
\]

This finite sum defines an entire vector-valued function. Its values on the real axis are real vectors.

For the norm estimates, use the Hilbert space \(L^2([-\pi,\pi],d\xi/(2\pi))\). The functions \(\xi\mapsto e^{ij\xi}\), for integer \(j\), are orthonormal because the integral of \(e^{i(j-k)\xi}\) against this measure equals \(\delta_{jk}\). Direct integration gives

\[
\operatorname{sinc}\!\left(\pi\left(\frac zh-j\right)\right)
=\frac1{2\pi}\int_{-\pi}^{\pi}
 e^{i\xi z/h}e^{-ij\xi}\,d\xi.
\]

For any finite orthonormal family, the sum of the squared inner products with a vector is at most its squared norm: subtract its orthogonal projection onto the family's span and use nonnegativity of the remaining squared norm. Applying this inequality to \(\xi\mapsto e^{i\xi z/h}\), which is square-integrable on the finite interval for every \(z\), yields

\[
\sum_{j=1}^{J}
\left|\operatorname{sinc}\!\left(\pi\left(\frac zh-j\right)\right)\right|^2
\le\frac1{2\pi}\int_{-\pi}^{\pi}e^{-2\xi\operatorname{Im}(z)/h}\,d\xi
\le e^{2\pi|\operatorname{Im}(z)|/h}.
\]

Orthonormality of the \(v_j\) and \(|e^{-z}|=e^{-\operatorname{Re}(z)}\) therefore give

\[
\|u_n(z)\|_n
\le h e^{-\ell/8}e^{-\operatorname{Re}(z)}
e^{\pi|\operatorname{Im}(z)|/h}
\le h e^r
\quad\text{if}\quad
|\operatorname{Im}(z)|\le r,\quad \operatorname{Re}(z)\ge-r.
\]

Here \(\pi r/h=\ell/8\) gives the cancellation. Since \(\ell\ge1\), the last bound is at most \(8\pi e\), uniformly in \(n\). For each coordinate \(k\),

\[
|(u_n(z))_k|\le\sqrt n\,\|u_n(z)\|_n\le\sqrt n\,h e^r.
\]

The norm on the complex domain is the Hermitian norm, so no bilinear square or cancellation between complex coordinates is being used. The coordinate bound is allowed to grow with \(n\); a stronger coordinatewise hypothesis is not verified by this estimate.

For real \(t\), the exponential integrand has unit modulus before differentiation, giving a squared coefficient sum at most one. Differentiating under the integral is valid on each compact set in \(z\), since the interval is finite and the integrand and its derivative have an integrable uniform bound there. Applying the orthogonal-projection inequality to \((i\xi/h)e^{i\xi t/h}\) gives

\[
\sum_{j=1}^{J}
\left|\frac{d}{dt}
\operatorname{sinc}\!\left(\pi\left(\frac th-j\right)\right)\right|^2
\le\frac1{2\pi}\int_{-\pi}^{\pi}\frac{\xi^2}{h^2}\,d\xi
=\frac{\pi^2}{3h^2}.
\]

The product rule and triangle inequality now imply, for every \(t\ge0\),

\[
\|u_n(t)\|_n\le a e^{-t},\qquad
\|u_n'(t)\|_n
\le a e^{-t}\left(1+\frac{\pi}{\sqrt3 h}\right)
=e^{-\ell/8}\left(h+\frac\pi{\sqrt3}\right)e^{-t}.
\]

In particular, the first derivative is uniformly bounded, both displayed quantities decay exponentially, and the total length satisfies

\[
\int_0^\infty\|u_n'(t)\|_n\,dt
\le e^{-\ell/8}\left(h+\frac\pi{\sqrt3}\right).
\]

For the rank lower bound, let \(E\subseteq\mathbb R^n\) be a fixed linear subspace with orthogonal projection \(P_E\) in the normalized inner product. Define \(\operatorname{dist}_n(v,E)=\inf_{w\in E}\|v-w\|_n=\|(I-P_E)v\|_n\), where \(I\) is the identity operator, and assume

\[
\sup_{t\ge0}\operatorname{dist}_n(u_n(t),E)\le\eta_n,
\qquad \eta_n=n^{-1/2}.
\]

The same proof works for a complex subspace of \(\mathbb C^n\), with complex dimension. At the sampling times \(t_j=jh\), \(1\le j\le J\), the cardinal identity \(\operatorname{sinc}(\pi(j-k))=\delta_{jk}\) gives

\[
u_n(t_j)=a e^{-t_j}v_j,\qquad
t_j\le\frac\ell8,\qquad
a e^{-t_j}\ge h e^{-\ell/4}.
\]

Linearity of \(E\) permits division by the positive amplitude, so

\[
\|(I-P_E)v_j\|_n^2
\le\left(\frac{\eta_n}{h e^{-\ell/4}}\right)^2.
\]

If \(w_1,\ldots,w_m\) is an orthonormal basis of \(E\), where \(m=\dim E\), the orthogonal-projection inequality applied to the family \(v_1,\ldots,v_J\) gives

\[
\sum_{j=1}^{J}\|P_Ev_j\|_n^2
=\sum_{k=1}^{m}\sum_{j=1}^{J}|\langle v_j,w_k\rangle_n|^2
\le m.
\]

Since \(\|P_Ev_j\|_n^2=1-\|(I-P_E)v_j\|_n^2\),

\[
\dim E\ge J\left[1-
\left(\frac{\eta_n}{h e^{-\ell/4}}\right)^2\right],
\qquad
\left(\frac{\eta_n}{h e^{-\ell/4}}\right)^2
=\frac{e^{1/2}\ell^3}{64\pi^2\sqrt n}=o(1).
\]

Consequently \(\dim E\ge(1-o(1))J\), with \(J=\Theta(\log(en)^{5/2})\). In fact, the product of \(J\) and the last error ratio is \(O(\ell^{11/2}/\sqrt n)=o(1)\). Integrality then gives \(\dim E\ge J\) for all sufficiently large \(n\). The span of \(v_1,\ldots,v_J\) attains this dimension and contains the entire trajectory.

Finally, if a time parametrization \(\psi:\mathcal I\to[0,\infty)\), defined on an interval \(\mathcal I\), is onto, then

\[
\{u_n(\psi(s)):s\in\mathcal I\}=\{u_n(t):t\ge0\}.
\]

Thus the supremum of the distance to any fixed \(E\) is unchanged. Monotonicity is compatible with this statement but surjectivity alone supplies the set equality. A clock that omits times or an approximation objective weighted by time would require a different argument.

The verified conclusion is that the shrinking strip width \(r\asymp1/\sqrt{\log(en)}\), a uniform complex RMS bound, and the stated exponential real decay and derivative bound alone cannot guarantee fixed linear source rank \(O(\log n)\), or even \(o(\log(n)^{5/2})\), for uniform normalized error \(n^{-1/2}\). No neural equation has been imposed or realized. The argument does not bound arbitrary nonlinear representations, moving subspaces, observable-only approximations, or storage for a structured metric or kernel. It is an information-adequacy obstruction for those source estimates, conditional on the fixed-linear-subspace approximation model.

## Strengthening with uniformly bounded coordinates

The supplied follow-up replaces the coordinate vectors by a discrete cosine family. For sufficiently large \(n\), \(2J<n\). Index the \(n\) coordinates by \(k=0,\ldots,n-1\), and instead define

\[
(v_j)_k=\sqrt2\cos\!\left(\frac{2\pi jk}{n}\right),
\qquad 1\le j\le J.
\]

For an integer \(p\), summing a finite geometric series shows that
\[
\frac1n\sum_{k=0}^{n-1}e^{2\pi i pk/n}
=
\begin{cases}1,&p\text{ is divisible by }n,\\0,&p\text{ is not divisible by }n.\end{cases}
\]
The product-to-sum identity therefore gives
\[
\langle v_j,v_m\rangle_n
=\frac1n\sum_{k=0}^{n-1}
\left[
\cos\!\left(\frac{2\pi(j-m)k}{n}\right)
+\cos\!\left(\frac{2\pi(j+m)k}{n}\right)
\right]
=\delta_{jm}.
\]
Indeed, \(|j-m|<n\), so the first frequency is divisible by \(n\) exactly when \(j=m\), whereas \(0<j+m\le2J<n\) excludes divisibility for the second. Thus every Hilbert-norm estimate and the rank proof above remain valid with this replacement.

Moreover, \(|(v_j)_k|\le\sqrt2\), so for any complex coefficients \(c_1,\ldots,c_J\), Cauchy–Schwarz gives
\[
\left|\sum_{j=1}^{J}c_j(v_j)_k\right|
\le\sqrt{2J}\left(\sum_{j=1}^{J}|c_j|^2\right)^{1/2}.
\]
Using the coefficient estimates already proved, throughout the same complex domain,
\[
\max_k|(u_n(z))_k|
\le\sqrt{2J}\,h e^r
\le\sqrt{2\pi}\,e^r\ell^{-1/4}.
\]
On the real half-line,
\[
\max_k|(u_n'(t))_k|
\le\sqrt{2J}\,e^{-\ell/8}
\left(h+\frac{\pi}{\sqrt3}\right)e^{-t}.
\]
The factor before \(e^{-t}\) is \(O(\ell^{5/4}e^{-\ell/8})\), hence is uniformly bounded and tends to zero. This strengthening removes the growth of the coordinate envelope in the original basis. It still supplies no neural realizability theorem or lower bound on storage for a structured representation.
