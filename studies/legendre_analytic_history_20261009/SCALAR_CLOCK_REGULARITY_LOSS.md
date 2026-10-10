# Scalar residual-clock regularity loss

This is a scalar regularity counterexample, not a construction of a neural
trajectory or an obstruction to a theorem with additional dynamical hypotheses.
Analyticity and conormal regularity below concern the active trajectory; the
zero prefix is an artificial extension of its history.

Fix \(d>0\), \(0<\alpha<1/4\), and write

\[
A_*=1+d,\qquad \beta=1+\alpha\in(1,5/4).
\]

Let \(\Pi_q\) be orthogonal projection in \(L^2(0,A_*)\) onto polynomials of
degree less than \(q\), and let \(Q_q=I-\Pi_q\). Define \(b=h=0\) on
\(0\leq\xi\leq1\), and, on \(1<\xi\leq A_*\), define

\[
\begin{aligned}
b(\xi)&=(A_*-\xi)^\alpha-d^\alpha,\\
h(\xi)&=(A_*-\xi)^\beta-d^\beta
        +\beta d^\alpha(\xi-1).
\end{aligned}
\]

Then

\[
\int_0^{A_*}(Q_qb)(\xi)(Q_qh)(\xi)\,d\xi
=-c_{\alpha,d}\,q^{-4-4\alpha}(1+o(1)),
\qquad
c_{\alpha,d}
=\frac{A_*^{2\beta}}{2\beta^3}
 \left(\frac{\Gamma(\beta+1)}{\Gamma(-\beta)}\right)^2>0.
\]

In particular, this signed cross term is not \(O(q^{-5})\). The proof first
reduces the cross term to endpoint errors of \(h\), then separates its endpoint
power singularity from the smooth prefix correction.

## Physical time and the onset

For physical time \(t\geq0\), set

\[
\xi(t)=1+d(1-e^{-t}),\qquad A_*-\xi(t)=de^{-t}.
\]

Direct substitution gives

\[
\begin{aligned}
b(\xi(t))&=d^\alpha(e^{-\alpha t}-1),\\
h(\xi(t))&=d^\beta
 \bigl(e^{-\beta t}-\beta e^{-t}+\beta-1\bigr).
\end{aligned}
\]

Both expressions extend to entire functions of complex \(t\). Each of their
physical-time derivatives is bounded on \(t\geq0\). On the active clock
interval \(1<\xi<A_*\), define the conormal derivative

\[
D=(A_*-\xi)\frac{d}{d\xi}.
\]

Since \(d\xi/dt=A_*-\xi\), this is exactly physical-time differentiation
along the trajectory. For every integer \(m\geq1\),

\[
\begin{aligned}
D^m b&=(-\alpha)^m(A_*-\xi)^\alpha,\\
D^m h&=(-\beta)^m(A_*-\xi)^\beta
       -\beta d^\alpha(-1)^m(A_*-\xi).
\end{aligned}
\]

These derivatives are bounded, for each fixed \(m\), uniformly on the active
interval. The defining formulas also give \(h'=-\beta b\) on the full history
interval, with the derivative interpreted classically at the onset for \(h\).
Writing \(u=\xi-1\downarrow0\), the active-side expansions are

\[
b(1+u)=-\alpha d^{\alpha-1}u+O(u^2),\qquad
h(1+u)=\frac{\beta\alpha}{2}d^{\alpha-1}u^2+O(u^3).
\]

Thus the extended \(b\) is continuous with a first-derivative jump at the onset,
and the extended \(h\) is \(C^1\) with a second-derivative jump. The construction
does **not** assert all-order conormal regularity across the artificial prefix
junction, or physical-time analyticity of a trajectory that is identically
zero for negative time and equals these formulas for positive time.

## Exact reduction to endpoint errors

The function \(h\) is absolutely continuous and \(h'=-\beta b\in L^2(0,A_*)\).
Orthogonality of \(Q_qh\) to polynomials of degree less than \(q\), including
\((\Pi_qh)'\), yields

\[
\begin{aligned}
\int_0^{A_*}Q_qb\,Q_qh\,d\xi
&=-\frac1\beta\int_0^{A_*}h'Q_qh\,d\xi\\
&=-\frac1\beta\int_0^{A_*}(Q_qh)'Q_qh\,d\xi\\
&=-\frac{(Q_qh)(A_*)^2-(Q_qh)(0)^2}{2\beta}.
\end{aligned}
\]

This identity uses orthogonality, not commutation of differentiation and
projection.

## The endpoint power

Write \(f(\xi)=(A_*-\xi)^\beta\). Let \(P_j\) denote the Legendre polynomial
normalized by \(P_j(1)=1\). With \(u=\xi/A_*\), write

\[
f(A_*u)=\sum_{j=0}^\infty a_jP_j(2u-1).
\]

The exact moment identity supplied for this calculation is

\[
M_j(\beta):=\int_0^1u^\beta P_j(2u-1)\,du
=\frac{\prod_{r=0}^{j-1}(\beta-r)}
       {\prod_{r=1}^{j+1}(\beta+r)}
=\frac{\Gamma(\beta+1)^2}
       {\Gamma(\beta-j+1)\Gamma(\beta+j+2)}.
\]

For completeness, the product formula follows from shifted Rodrigues'
formula and \(j\) integrations by parts when \(\beta>j-1\). Both sides are
rational functions of \(\beta\): expand the polynomial inside the integral
to see this on the left. Their equality therefore extends to every
\(\beta>-1\) for which the displayed denominators are nonzero, which includes
the present noninteger \(\beta\in(1,5/4)\).

Changing \(u\) to \(1-u\) gives
\(a_j=A_*^\beta(2j+1)(-1)^jM_j(\beta)\). The gamma reflection identity then
gives, for \(j\geq2\),

\[
a_j=A_*^\beta\kappa_\beta(2j+1)
 \frac{\Gamma(j-\beta)}{\Gamma(j+\beta+2)},
\qquad
\kappa_\beta=\frac{\Gamma(\beta+1)}{\Gamma(-\beta)}>0.
\]

Indeed \(\Gamma(-\beta)>0\) for \(1<\beta<2\), by applying
\(\Gamma(z+1)=z\Gamma(z)\) twice to \(z=-\beta\).
The fixed-shift form of Stirling's formula,
\(\Gamma(j+a)/\Gamma(j+b)=j^{a-b}(1+O(j^{-1}))\), applies here to fixed
real shifts \(a=-\beta\), \(b=\beta+2\). It gives

\[
a_j=2A_*^\beta\kappa_\beta j^{-2\beta-1}(1+O(j^{-1})).
\]

Consequently the series is absolutely and uniformly convergent, using
\(|P_j(z)|\leq1\) on \(z\in[-1,1]\). Completeness in \(L^2\) identifies its
continuous sum with \(f\), so both endpoint tails can be evaluated termwise.
The elementary telescoping identity

\[
\beta(2j+1)\frac{\Gamma(j-\beta)}{\Gamma(j+\beta+2)}
=j\frac{\Gamma(j-\beta)}{\Gamma(j+\beta+1)}
 -(j+1)\frac{\Gamma(j+1-\beta)}{\Gamma(j+\beta+2)}
\]

therefore yields the exact right-endpoint tail, for \(q\geq2\),

\[
(Q_qf)(A_*)
=\sum_{j=q}^\infty a_j
=\frac{A_*^\beta\kappa_\beta}{\beta}
 q\frac{\Gamma(q-\beta)}{\Gamma(q+\beta+1)}
=\frac{A_*^\beta\kappa_\beta}{\beta}
 q^{-2\beta}(1+O(q^{-1})).
\]

At the other endpoint, the tail alternates. Its positive terms decrease since

\[
\frac{a_{j+1}}{a_j}
=\frac{(2j+3)(j-\beta)}{(2j+1)(j+\beta+2)}<1
\qquad(j\geq2),
\]

where denominator minus numerator is \(2(2\beta+1)(j+1)>0\). The alternating
series estimate gives

\[
|(Q_qf)(0)|=\left|\sum_{j=q}^\infty(-1)^ja_j\right|
\leq a_q=O(q^{-2\beta-1}).
\]

## The prefix correction

On the whole interval define

\[
H(\xi)=f(\xi)-d^\beta+\beta d^\alpha(\xi-1),\qquad
r(\xi)=
\begin{cases}
-H(\xi),&0\leq\xi\leq1,\\
0,&1<\xi\leq A_*.
\end{cases}
\]

Then \(h=H+r\), and \(Q_qH=Q_qf\) for \(q\geq2\). We prove

\[
(Q_qr)(0)=O(q^{-5/2}),\qquad (Q_qr)(A_*)=O(q^{-5/2}).
\]

Set \(z=2\xi/A_*-1\), \(s=2/A_*-1\in(-1,1)\), and
\(F(z)=r(A_*(z+1)/2)\). This \(F\) is smooth on the closed interval
\([-1,s]\), is zero on \((s,1]\), and satisfies \(F(s)=F'(s)=0\).
Here derivatives of \(F\) are with respect to \(z\), and \(F''(s)\) below is
the derivative from the left. The orthogonal projection is unchanged by
the constant measure factor in this affine coordinate transformation.

The endpoint projection kernels telescope as

\[
\begin{aligned}
\sum_{j=0}^{q-1}(2j+1)P_j(z)&=P_q'(z)+P_{q-1}'(z),\\
\sum_{j=0}^{q-1}(-1)^j(2j+1)P_j(z)
&=(-1)^{q-1}\bigl(P_q'(z)-P_{q-1}'(z)\bigr).
\end{aligned}
\]

An integration by parts, using \(P_j(-1)=(-1)^j\), gives the endpoint errors

\[
\begin{aligned}
(Q_qF)(1)&=\frac12\int_{-1}^{s}F'(z)
                  \bigl(P_q(z)+P_{q-1}(z)\bigr)\,dz,\\
(Q_qF)(-1)&=\frac{(-1)^{q-1}}2\int_{-1}^{s}F'(z)
                  \bigl(P_q(z)-P_{q-1}(z)\bigr)\,dz.
\end{aligned}
\]

In the second formula, the boundary term in the projection itself equals
\(F(-1)\), which cancels when the projection error is formed.
For \(n\geq3\), define the two Legendre antiderivatives

\[
\begin{aligned}
R_n(z)&=\frac{P_{n+1}(z)-P_{n-1}(z)}{2n+1},\\
T_n(z)&=\frac1{2n+1}
 \left(\frac{P_{n+2}(z)-P_n(z)}{2n+3}
       -\frac{P_n(z)-P_{n-2}(z)}{2n-1}\right).
\end{aligned}
\]

They satisfy \(R_n'=P_n\), \(T_n'=R_n\), and
\(R_n(\pm1)=T_n(\pm1)=0\). Two integrations by parts therefore give

\[
\int_{-1}^{s}F'P_n\,dz
=-F''(s)T_n(s)+\int_{-1}^{s}F'''(z)T_n(z)\,dz.
\]

The Legendre estimate supplied for this calculation states that, for an
absolute constant \(C\), every integer \(k\geq1\), and \(-1<z<1\),

\[
|P_k(z)|\leq Ck^{-1/2}(1-z^2)^{-1/4}.
\]

Applied to the four terms in \(T_n\), it gives

\[
|T_n(z)|\leq C' n^{-5/2}(1-z^2)^{-1/4}
\qquad(n\geq3).
\]

Because \(s\) is fixed in the interior, \(F''(s)\) is finite, \(F'''\) is
bounded on \([-1,s]\), and \((1-z^2)^{-1/4}\) is integrable there. Hence
\(\int_{-1}^{s}F'P_n\,dz=O(n^{-5/2})\). Substitution with \(n=q,q-1\)
in the two endpoint kernel formulas proves both prefix bounds for \(q\geq4\).
All constants may depend on the fixed \(\alpha,d\).

## Combining the endpoints

Since \(2\beta<5/2\), the prefix correction is smaller than the right-endpoint
singular tail. The preceding results give

\[
\begin{aligned}
(Q_qh)(A_*)&=\frac{A_*^\beta\kappa_\beta}{\beta}
               q^{-2\beta}(1+o(1)),\\
(Q_qh)(0)&=O(q^{-5/2})=o(q^{-2\beta}).
\end{aligned}
\]

The exact endpoint identity now gives the asserted negative asymptotic with
\(c_{\alpha,d}=A_*^{2\beta}\kappa_\beta^2/(2\beta^3)\). Finally,

\[
q^5\left|\int_0^{A_*}Q_qb\,Q_qh\,d\xi\right|
\sim c_{\alpha,d}q^{1-4\alpha}\longrightarrow\infty.
\]

Thus physical-time analyticity, bounded active-interval conormal derivatives
of every fixed order, the relation \(h'=-\beta b\), and the stated onset orders
do not by themselves imply the signed \(O(q^{-5})\) estimate. Any extension of
this example to a particular dynamical model would require a separate
realizability argument, which is not provided here.
