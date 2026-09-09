# A positive limiting profile for the diagnostic rare Hardy hierarchies

## Scope

This is an elementary counterexample to two SCHEMATIC INEQUALITIES.
It is not a canonical-network trajectory, not a counterexample to any
proved finite-width rare estimate, and not a refutation of the target
global mean-field theorem. Neither schematic hierarchy is asserted here
to have been derived for the canonical flow.

The construction preserves the nested time integrals. It satisfies
both displayed hierarchies below with the single constant C=1, on the
whole time half-line, while having a strictly positive limit as p tends
to zero at every positive time.

## Definitions and the two diagnostic inequalities

Put
\[
 h(x)=x\bigl(1+\log_+(1/x)\bigr)\quad(x>0),\qquad h(0)=0.
\]
For a bounded nonnegative function J on (0,1] and 0<a<=1, define
\[
 H_a[J]=aJ(1)+a\int_a^1\frac{J(r)}{r^2}\,dr.
 \tag{1}
\]
All functions to which this operator is applied below are continuous,
bounded, and nonnegative. The trajectory-dependent inputs for which
cutoff monotonicity is invoked are also nondecreasing in r. At zero
one may use the extension H_0[J]=J(0+). The zero-time integrands below
are zero, so their convention at that single endpoint has no effect
on an integral.

The first requested schematic inequality is
\[
 \begin{split}
 U_p(t)\le{}&h(p)+\int_0^t h(U_p(s))\,ds\\
 &+\int_0^t H_{\min\{U_p(s),1\}}
       \left[r\longmapsto\int_0^s h(U_r(v))\,dv\right]ds.
 \end{split}
 \tag{2}
\]
The later square-root-history inequality is
\[
 \begin{split}
 y_p'(t)\le{}&h(p)+h(y_p(t))\\
 &+\left\{y_p(t)t\int_0^t
       H_{\min\{y_p(t),1\}}
          [r\longmapsto h(y_r(u))]\,du\right\}^{1/2},
 \qquad y_p(0)=0.
 \end{split}
 \tag{3}
\]
In (3), the Hardy cutoff is the CURRENT-TIME value y_p(t), as in
the requested hierarchy; it is not changed to y_p(u).

## One explicit family

For t>=0 and 0<p<=1, set
\[
 \theta(t)=\frac{t}{1+2t},\qquad
 F(x)=\exp(-300/x^5)\quad(x>0),\qquad F(0)=0,
 \tag{4}
\]
and define
\[
 y_p(t)=\theta(t)h(p)+F(\theta(t)),\qquad
 f(t)=F(\theta(t)).
 \tag{5}
\]
We use U_p=y_p when checking (2).

The extension of F at zero is continuously differentiable (indeed
smooth), since its exponential decay dominates every inverse power.
For t>0,
\[
 0<\theta(t)<\frac12,\qquad
 \theta'(t)=\frac1{(1+2t)^2}\le1,\qquad \theta(t)\le t.
 \tag{6}
\]
Since 0<h(p)<=1, the family is nonnegative, continuously differentiable
in time, nondecreasing in p, and satisfies
\[
 y_p(0)=0,\qquad
 y_p(t)<\frac12+e^{-9600}<1.
 \tag{7}
\]
It is therefore uniformly bounded over both p and t. Its limiting
profile is
\[
 \lim_{p\downarrow0}y_p(t)=f(t)
   =\exp\left[-300\left(\frac{1+2t}{t}\right)^5\right]>0
 \quad(t>0).
 \tag{8}
\]

## Elementary Hardy lower bound

First, H_a[J] is nondecreasing in a whenever J is nondecreasing.
Indeed, changing variables gives the exact identity
\[
 H_a[J]=\int_0^1 J\bigl(\min\{a/x,1\}\bigr)\,dx,
 \tag{9}
\]
where the integrand at x=0 can be assigned J(1). Pointwise
monotonicity in a proves the assertion. The operator is also positive
and linear in J.

Write L(r)=1+log(1/r) for 0<r<=1, so h(r)=rL(r)<=1.
For 0<b<=1,
\[
 \begin{split}
 h(bh(r))
 &=brL(r)\left[L(r)+\log(1/b)-\log L(r)\right]\\
 &\ge \frac b2 rL(r)^2.
 \end{split}
 \tag{10}
\]
Here log L<=L/2 for L>=1: the minimum of L/2-log L on that
interval occurs at L=2 and equals 1-log 2>0. The case b=0
follows by continuity.

The function h is nondecreasing. Since y_r(u)>=theta(u)h(r),
(10) implies
\[
 h(y_r(u))\ge\frac{\theta(u)}2 rL(r)^2.
 \tag{11}
\]
For 0<a<=1, direct integration yields
\[
 \begin{split}
 H_a[r\longmapsto rL(r)^2]
 &=a\left[1+\int_a^1\frac{L(r)^2}{r}\,dr\right]\\
 &=\frac a3\left[L(a)^3+2\right].
 \end{split}
 \tag{12}
\]
Combining (11) and (12) gives
\[
 H_a[r\longmapsto h(y_r(u))]
 \ge\frac{\theta(u)a}{6}\left[\log(1/a)\right]^3.
 \tag{13}
\]
We will also use the elementary time bound
\[
 \theta(u)=\frac{u}{1+2u}
 \ge\frac ut\theta(t)\quad(0\le u\le t),
 \qquad
 \int_0^t\theta(u)\,du\ge\frac{t\theta(t)}2.
 \tag{14}
\]

## Verification of the square-root-history inequality

Fix t>0 and abbreviate theta=theta(t), f=F(theta), and
ell=log(1/f)=300 theta^(-5). Denote the radical in (3) by R_p(t).
By (7), its cutoff is y_p(t)<1. Since y_p(t)>=f and the
functions r->h(y_r(u)) are nondecreasing, (9), (13), and (14) give
\[
 \begin{split}
 R_p(t)^2
 &\ge ft\int_0^t
           \frac{\theta(u)f}{6}\ell^3\,du\\
 &\ge\frac{f^2t^2\theta}{12}\ell^3.
 \end{split}
 \tag{15}
\]
Consequently, using t>=theta,
\[
 \begin{split}
 R_p(t)
 &\ge\frac{f\,t\sqrt\theta}{\sqrt{12}}\ell^{3/2}\\
 &\ge\frac{300^{3/2}}{\sqrt{12}}
                       f\theta^{-6}\\
 &=1500 f\theta^{-6}=F'(\theta).
 \end{split}
 \tag{16}
\]
The numerical equality uses sqrt(300/12)=5.
Differentiating (5) and using theta'<=1 now gives
\[
 y_p'(t)=\theta'(t)\bigl[h(p)+F'(\theta(t))\bigr]
       \le h(p)+R_p(t).
 \tag{17}
\]
This proves (3), even without its nonnegative h(y_p(t)) term.
At t=0, y_p'(0)=h(p), so the inequality holds at that endpoint
as well.

## Verification of the original doubly integrated inequality

For fixed s>0, put
\[
 J_s(r)=\int_0^s h(y_r(v))\,dv,
 \qquad \theta=\theta(s),\quad f=f(s),\quad
 \ell=\log(1/f)=300\theta^{-5}.
\]
This J_s is nondecreasing in r. Positivity and linearity of H,
(13), and (14) give
\[
 \begin{split}
 H_{y_p(s)}[J_s]
 &\ge H_f[J_s]
 \ge\frac{f\ell^3}{6}\int_0^s\theta(v)\,dv\\
 &\ge\frac{f\,s\theta\ell^3}{12}
 \ge\frac{300^3}{12}f\theta^{-13}.
 \end{split}
 \tag{18}
\]
These operations preserve both time integrals. Interchanging H
and the inner time integral is legitimate by nonnegativity (or
ordinary bounded integration with fixed positive cutoff f).

On the other hand,
\[
 f'(s)=1500\theta'(s)f\theta^{-6}
       \le1500 f\theta^{-6}.
 \tag{19}
\]
The last expression in (18), divided by the upper bound in (19),
is 1500 theta^(-7)>1. Hence H_{y_p(s)}[J_s]>=f'(s).
Integration, f(0)=0, and theta(t)<=1 yield
\[
 y_p(t)=\theta(t)h(p)+f(t)
 \le h(p)+\int_0^t H_{y_p(s)}[J_s]\,ds.
 \tag{20}
\]
Adding the nonnegative integral of h(y_p) proves (2) with U_p=y_p.

## Conclusion and interpretation

Both diagnostic hierarchies allow the positive common limiting
profile (8), despite zero initial values, monotonicity in p, and
uniform boundedness. Thus neither schematic inequality alone
forces small-p stability at positive times.

The baseline theta(t)h(r) matters: applying h to it gives a lower
profile proportional to r(1+log(1/r))^2. The Hardy operator then
produces the cubic logarithm in (13). Retaining the time history
does not eliminate the explicit flat positive profile; (15)--(17)
verify this without discarding that history.

This conclusion is confined to the two displayed inequalities.
Additional canonical-flow structure may rule out this family.
No such structure is tested or refuted here.
