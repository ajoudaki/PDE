# Finite floors do not close the scalar Hardy hierarchy

## Scope

This is a deterministic counterexample to inequality (19) in
ACTUAL_WEIGHTED_GATE_HARDY_BOUND.md considered AS AN INEQUALITY.
It respects its finite-width floor, monotonicity in deletion size,
zero initial values, boundedness, and zero initial time derivatives.
It works with width error exactly zero.

It is not a canonical-network trajectory, not a counterexample to
any of the proved actual-network estimates, and not a refutation of
the global mean-field target. Additional dynamics discarded when
passing to that scalar majorant may exclude the family constructed
here.

## The precise finite hierarchy

Put
\[
 h(p)=p\log(e/p)\quad(0<p\le1),\qquad h(0)=0,
 \]
\[
 \Phi(x)=x[1+\tfrac12\log_+(1/x)],\qquad \Phi(0)=0.
 \]
For a nonnegative nondecreasing \(J\) that is zero on \(r<1/n\),
let
\[
 H_{a,n}[J]
 =aJ(1)+a\int_{\max\{a,1/n\}}^1\frac{J(r)}{r^2}\,dr
 \quad(0<a\le1),\qquad H_{0,n}[J]=0.
 \tag{1}
\]
Fix any \(C_0\ge1\) and define \(K(x)=\min\{1,C_0x\}\).
For a family \(Y_{p,n}\), denote the radical in the actual hierarchy
by
\[
 R_{p,n}(t)=
 \left\{Y_{p,n}(t)t\int_0^t
 H_{K(Y_{p,n}(t)),n}
       [r\mapsto\Phi(Y_{r,n}(u))]\,du\right\}^{1/2}.
 \tag{2}
\]
We construct a family satisfying, with the single constant \(C=1\),
\[
 Y_{p,n}(t)\le
 \left[t h(p)+\int_0^t\Phi(Y_{p,n}(s))\,ds
                         +\int_0^tR_{p,n}(s)\,ds\right]
 \tag{3}
\]
for all \(n\ge2\), \(0\le p\le1\), and \(t\ge0\).
This is precisely the zero-width-error version of the indicated
hierarchy. A final paragraph also gives any prescribed positive
constant in place of 1.

## Construction and elementary bounds

Set
\[
 \theta(t)=\frac{t^2}{1+2t^2},\qquad
 \Lambda=1800,\qquad
 F(x)=e^{-\Lambda/x^5}\ (x>0),\quad F(0)=0.
 \tag{4}
\]
For \(p\ge1/n\), let \(p_n=\lfloor np\rfloor/n\) and put
\[
 Y_{p,n}(t)=\theta(t)h(p_n)+F(\theta(t)).
 \tag{5}
\]
For \(p<1/n\), set \(Y_{p,n}(t)=0\).

The family is nondecreasing in \(p\), constant between grid points,
and zero below the first nonempty deletion size. Each time path is
smooth at zero, with
\[
 Y_{p,n}(0)=Y_{p,n}'(0)=0.
 \tag{6}
\]
Indeed \(F\) is flat at zero and \(\theta(0)=\theta'(0)=0\).
For \(t>0\),
\[
 0<\theta(t)<\tfrac12,\qquad
 \theta(t)\le t,\qquad \theta'(t)\le\tfrac12,
 \tag{7}
\]
and
\[
 \int_0^t\theta(u)\,du\ge \frac{t\theta(t)}3.
 \tag{8}
\]
For (7), \(\theta\le t\) follows from \(1+2t^2-t>0\), while
\[
 (1+2t^2)^2-4t=(2t-1)^2+4t^4>0
 \]
proves the derivative bound. For (8), use
\(\theta(u)\ge(u/t)^2\theta(t)\).

Since \(h(p_n)\le1\),
\[
 0\le Y_{p,n}(t)\le\tfrac12+e^{-32\Lambda}<0.51<e^{-1/2}.
 \tag{9}
\]
All bounds are uniform in \(p,n,t\).

## A lower bound that respects the finite floor

Write \(L(r)=1+\log(1/r)\) on \(0<r\le1\).
For every \(r\ge1/n\),
\[
 \frac{\lfloor nr\rfloor}{n}\ge\frac r2,\qquad
 h(\lfloor nr\rfloor/n)\ge\frac12h(r).
 \tag{10}
\]
The first inequality holds already on \([1/n,2/n)\); the second
uses monotonicity and concavity of \(h\).

For \(0<b\le1\), elementary algebra gives
\[
 h(bh(r))
 =brL(r)[L(r)+\log(1/b)-\log L(r)]
       \ge\frac b2rL(r)^2,
 \tag{11}
\]
because \(\log L\le L/2\) for \(L\ge1\).
Also \(\Phi(x)\ge h(x)/2\) for \(0\le x\le1\).
By (9)--(11), for every \(r\ge1/n\),
\[
 \Phi(Y_{r,n}(u))
       \ge \frac{\theta(u)}8rL(r)^2.
 \tag{12}
\]
No such lower bound is claimed below \(1/n\), where the input
to the Hardy operator is exactly zero.

The finite-floor Hardy operator is nondecreasing in its cutoff
for nondecreasing \(J\): the exact representation is
\[
 H_{a,n}[J]=\int_0^1J(\min\{1,a/v\})\,dv.
 \tag{13}
\]
For \(a\ge1/n\), the lower integration endpoint in (1) is \(a\).
Using (12), including its endpoint at \(r=1\), gives
\[
 \begin{split}
 H_{a,n}[r\mapsto\Phi(Y_{r,n}(u))]
 &\ge\frac{\theta(u)}8
       a\left[1+\int_a^1\frac{L(r)^2}{r}\,dr\right]\\
 &=\frac{\theta(u)a}{24}[L(a)^3+2]\\
 &\ge\frac{\theta(u)a}{24}L(a)^3 .
 \end{split}
 \tag{14}
\]

## Case 1: the smallest positive profile lies above the floor

Fix \(t>0\), and abbreviate
\[
 \theta=\theta(t),\qquad f=F(\theta),\qquad
 x=Y_{1/n,n}(t)=\theta h(1/n)+f.
 \]
Suppose \(x\ge1/n\). For every \(p\ge1/n\),
\(Y_{p,n}(t)\ge x\) and \(K(Y_{p,n}(t))\ge x\).
Monotonicity, (8), and (14) yield
\[
 R_{p,n}(t)^2
 \ge x t\int_0^t\frac{\theta(u)x}{24}L(x)^3du
 \ge \frac{x^2t^2\theta}{72}L(x)^3.
 \tag{15}
\]
The function \(zL(z)^{3/2}\) is increasing for
\(0<z<e^{-1/2}\): its derivative is
\(L(z)^{1/2}[L(z)-3/2]>0\).
Thus \(x\ge f\), (7), and (9) imply
\[
 \begin{split}
 R_{p,n}(t)
 &\ge\frac{x\theta^{3/2}}{\sqrt{72}}L(x)^{3/2}\\
 &\ge\frac{f\theta^{3/2}}{\sqrt{72}}L(f)^{3/2}\\
 &\ge\frac{\Lambda^{3/2}}{\sqrt{72}}f\theta^{-6}
   =5\Lambda f\theta^{-6}
   =F'(\theta).
 \end{split}
 \tag{16}
\]
The numerical equality uses \(\Lambda=25\cdot72\).
Notice that \(f\) itself need NOT be above \(1/n\).
The Hardy lower bound was applied at \(x\), which is above the
floor; only the scalar increasing function was then compared
with its value at \(f\).

Consequently, in this case,
\[
 Y_{p,n}'(t)
 =\theta'(t)[h(p_n)+F'(\theta)]
 \le\tfrac12h(p)+\tfrac12R_{p,n}(t).
 \tag{17}
\]

## Case 2: the smallest positive profile lies below the floor

Now suppose \(x<1/n\). Let \(L_n=1+\log n\). Then
\(\theta L_n<1\), hence \(\theta<1/L_n\).
The function
\[
 F'(z)=5\Lambda z^{-6}e^{-\Lambda/z^5}
 \]
is increasing on \(0<z\le1\), since its logarithmic derivative
is \(z^{-6}(5\Lambda-6z^5)>0\).
Therefore
\[
 F'(\theta)\le5\Lambda L_n^6e^{-\Lambda L_n^5}
                         \le \frac{L_n}{n}=h(1/n).
 \tag{18}
\]
To verify the second inequality without an asymptotic argument,
put \(X=\Lambda L_n^5\). The ratio of its left side to \(L_n/n\)
is \(5X e^{-X+L_n-1}\). Since \(L_n-1\le X/2\) and
\(e^{X/2}\ge X^2/8\), that ratio is at most
\[
 5X e^{-X/2}\le40/X\le40/\Lambda<1.
 \]

For every \(p\ge1/n\), (7) and (18) now give
\[
 Y_{p,n}'(t)\le\tfrac12[h(p_n)+h(1/n)]\le h(p).
 \tag{19}
\]
This case requires no lower bound on the radical at all.
The flat profile's derivative is paid for by the baseline
forcing at the smallest nonempty deletion size.

## Verification of the hierarchy and the positive limiting profile

Combining the two cases gives, for \(p\ge1/n\),
\[
 Y_{p,n}'(t)\le h(p)+R_{p,n}(t).
 \tag{20}
\]
The inequality is also valid at zero and for \(p<1/n\), where
the left side is zero. Integrate (20), use (6), and add the
nonnegative \(\Phi\) integral. This proves (3).

For fixed \(p>0\), \(p_n\to p\) as \(n\to\infty\), so
\[
 \lim_{p\downarrow0}\lim_{n\to\infty}Y_{p,n}(t)
       =F(\theta(t))>0\qquad(t>0).
 \tag{21}
\]
Even along singleton deletion sizes,
\(Y_{1/n,n}(t)\to F(\theta(t))>0\).
Thus the actual finite-floor scalar hierarchy, not only its
continuum schematic version, permits failure of limit continuity.

## Arbitrary positive constants and an optional delayed start

The unit constant is not essential. If a prescribed constant \(C>0\)
is desired in (3), set
\(\kappa=\min\{1,C/2\}\) and replace \(\theta(t)\) everywhere
by \(\theta(\kappa t)\). Its time derivative is at most
\(\kappa\), and \(t\ge\theta(\kappa t)/\kappa\).
The Case 1 radical is then at least \(F'(\theta)/\kappa\).
Since \(\kappa^2\le C\), its derivative contribution
\(\kappa F'(\theta)\) is at most \(C R_{p,n}\).
The baseline derivative costs at most \(C h(p)\); Case 2 costs
at most \(2\kappa h(p)\le C h(p)\).
Integration proves the hierarchy with that same prescribed \(C\).

One may also delay the clock by replacing \(t\) in this construction
by \((t-t_0)_+\), for any \(t_0\ge0\). The family then vanishes on
\([0,t_0]\) and is still continuously differentiable there.
For \(t>t_0\), the history integral on \([t_0,t]\) gives the same
lower bound with elapsed time \(t-t_0\), while the outer factor
\(t\) in (2) is only larger. The preceding verification is
unchanged. Hence even requiring zero limiting error on a
previously controlled initial interval does not repair this
scalar hierarchy alone.

None of these artificial profiles is asserted to satisfy the
canonical state equations, their signed identities, or any
additional estimate not retained in (3).
