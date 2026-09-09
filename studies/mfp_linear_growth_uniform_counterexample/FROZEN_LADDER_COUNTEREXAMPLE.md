# A smooth bounded-slope failure of every local fifth-remainder bound

## Statement and scope

Consider the exact scalar Euler recursion

\[
 a^+=a+h\phi(z),\qquad z^+=z+ha\phi'(z),
 \qquad (a_0,z_0)\sim N(0,I_2),
\]

and write

\[
 \bar F_N^\phi(h)=\mathbb E[a_N\phi(z_N)],\qquad
 \bar\Delta^\phi(h)=\bar F_2^\phi(h)-\bar F_1^\phi(2h).
\]

There is an RMS-normalized activation \(\phi\in C^\infty(\mathbb R)\)
such that

\[
 \|\phi'\|_\infty<\infty,
 \qquad |\phi(x)|\le C(1+|x|),
\]

all the displayed fixed-step expectations are finite for every fixed
\(h\), but

\[
 \sup_{0<|h|\le r}
 \frac{|\bar\Delta^\phi(h)-\kappa h^3|}{|h|^5}=\infty
 \tag{1}
\]

for every \(r>0\) and every \(\kappa\in\mathbb R\).  Thus global
Lipschitzness, linear growth, and smoothness do not by themselves imply a
uniform fifth-remainder theorem, even at horizon one of this exact frozen
subsystem.

This is not a counterexample for the full two-hidden-layer OMFP output.
The bottom-feature and reused-adjoint terms of the full DAG occur at the
same source order, and no sign or orthogonality theorem currently prevents
them from cancelling the scalar contribution.

## Exact finite-activation coefficients

Put \(p_r=\psi^{(r)}(Z)\), where \(Z\sim N(0,1)\).  For every smooth
\(\psi\) with bounded derivatives and at most linear growth, direct
Taylor expansion of the two displayed Euler steps gives

\[
 \bar\Delta^\psi(h)=\kappa(\psi)h^3+\beta(\psi)h^5+o(h^5),
 \tag{2}
\]

where \(\kappa(\psi)=\mathbb E K_3(\psi;Z)\),
\(\beta(\psi)=\mathbb E K_5(\psi;Z)\), and

\[
\begin{aligned}
K_3={}&6p_1^2p_2^2+\frac32p_1^3p_3+2p_1^4
 +\frac{11}{2}p_0p_1^2p_2+2p_0^2p_1^2,
\end{aligned}
\tag{3}
\]

\[
\begin{aligned}
K_5={}&\frac{45}{2}p_1^3p_2^2p_3
 +15p_1^4p_3^2+25p_1^4p_2p_4
 +\frac{21}{2}p_1^4p_2^2\\
&+\frac58p_1^5p_5+\frac{13}{2}p_1^5p_3
 +6p_0p_1^2p_2^3+\frac{69}{2}p_0p_1^3p_2p_3\\
&+\frac{45}{8}p_0p_1^4p_4+\frac72p_0p_1^4p_2
 +7p_0^2p_1^2p_2^2+6p_0^2p_1^3p_3
 +p_0^3p_1^2p_2.
\end{aligned}
\tag{4}
\]

For completeness, (2)--(4) follow by substituting

\[
\begin{aligned}
a_1&=a+h\psi(z),&z_1&=z+ha\psi'(z),\\
a_2&=a_1+h\psi(z_1),&z_2&=z_1+ha_1\psi'(z_1)
\end{aligned}
\]

into \(a_2\psi(z_2)-(a+2h\psi(z))
\psi(z+2ha\psi'(z))\), expanding through order five, and using
\(\mathbb E a^{2j+1}=0\), \(\mathbb E a^2=1\),
\(\mathbb E a^4=3\), and \(\mathbb E a^6=15\).  The exact sparse-rational
calculation is reproduced by `frozen_scalar_symbolic.py` in this folder.
The map \(a\mapsto-a, h\mapsto-h\) also proves that the discrepancy is
odd, so no even powers were suppressed by assumption.

## A transition with a negative singular fifth coefficient

Fix \(\rho\in C_c^\infty((-1/4,1/4))\), with
\(\rho\ge0\), \(\int\rho=1\), and \(\rho'\not\equiv0\).  Let

\[
 R(y)=\int_{-\infty}^y\rho(s)\,ds.
\]

Suppose that immediately to the left of a new transition the slope is
\(b\in[1,2]\).  Add

\[
 g_{x,\delta,w}(u)=\delta R((u-x)/w)
\]

to the derivative of the activation.  On the transition interval, write
\(y=(u-x)/w\).  The only terms of (4) with scale \(w^{-3}\) after
integration are

\[
15g^4(g'')^2+25g^4g'g'''
+\frac58g^5g^{(4)}+\frac{45}{2}g^3(g')^2g'',
\tag{5}
\]

where now \(g=\psi'\).  Dividing the constant-density integral of (5)
by \(\delta^2w^{-3}\) and then sending \(\delta\downarrow0\) gives

\[
 b^4\left(15\int(\rho')^2
+25\int\rho\rho''
+\frac{25}{8}\int R\rho'''\right)
=-\frac{55}{8}b^4\int(\rho')^2.
\tag{6}
\]

Indeed \(\int\rho\rho''=-\int(\rho')^2\) and
\(\int R\rho'''=\int(\rho')^2\).  The last term in (5) is
\(O(\delta^3w^{-3})\).  Consequently there are numbers
\(\delta_*>0,c_*>0\), depending only on \(\rho\), such that, uniformly
for \(b\in[1,2]\) and \(0<\delta\le\delta_*\), the coefficient of
\(w^{-3}\) is at most \(-c_*\delta^2\).

Let \(\gamma\) denote the standard Gaussian density and set

\[
 w=\delta\sqrt{\gamma(x)}.
\tag{7}
\]

As \(x\to\infty\), one has \(w\to0\), \(xw\to0\).  Hence
\(\gamma(x+wy)/\gamma(x)\to1\) uniformly on the support of \(\rho\).
The integrated leading term in (6) is therefore at most

\[
 -\frac{c_*}{\delta\sqrt{\gamma(x)}}.
\tag{8}
\]

For the term containing \(g^{(4)}\), this conclusion uses its cancellation
before taking an absolute value.  After division by the scale in (8), its
rescaled integral is

\[
 \frac58\delta^{-1}\int
 (b+\delta R(y))^5\rho'''(y)
 \frac{\gamma(x+wy)}{\gamma(x)}\,dy.
\]

The density ratio converges uniformly to one.  Its error after the factor
\(\delta^{-1}\) is \(O(xw/\delta)=O(x\sqrt{\gamma(x)})\), and the constant
term of the limiting integral vanishes because \(\int\rho'''=0\).

All remaining terms in (4) are negligible relative to (8).  This can be
checked without a hidden domination argument: after multiplication by the
Gaussian density and integration over an interval of length \(w\), their
ratios to \((\delta\sqrt{\gamma(x)})^{-1}\) are bounded by finite sums of

\[
 \delta,\quad x\sqrt{\gamma(x)},\quad
 x\delta\sqrt{\gamma(x)},\quad
 x^2\delta\gamma(x),\quad
 x^3\delta^2\gamma(x)^{3/2},
\]

all except the first tend to zero as \(x\to\infty\), while the first is
made uniformly smaller than half the negative constant in (6) by the
choice of \(\delta_*\).  Thus the new transition contribution to \(\beta\) tends to
\(-\infty\) as \(x\to\infty\).

There is no untracked contribution away from transition intervals: every
monomial in (4) contains at least one of \(g',g'',g''',g^{(4)}\), so it
vanishes wherever the activation is affine.  A transition placed to the
right of the previous ones does not alter the activation on their
supports.  Hence the fifth coefficient is exactly the sum of the local
transition contributions used in the recursion below.

In contrast, its change in the cubic coefficient tends to zero.  The only
singular cubic terms satisfy

\[
 \int |g'|^2\gamma=O(\delta\sqrt{\gamma(x)}),
 \qquad
 \int |g''|\gamma=O(\sqrt{\gamma(x)}),
\tag{9}
\]

and the remaining changes are
\(O(\delta(1+x^2)\gamma([x-1/4,\infty)))\).  Equations (8)--(9) are the
separation used below: the fifth coefficient can be made arbitrarily
large while the cubic change is arbitrarily small.

## Diagonal construction of one activation

Choose successively amplitudes \(0<\delta_n\le2^{-n}\delta_*\), centers
\(x_n\uparrow\infty\), and widths

\[
 w_n=\delta_n\sqrt{\gamma(x_n)}
\]

so that the transition intervals are disjoint.  Define

\[
 g_N(x)=1+\sum_{n=1}^N\delta_nR((x-x_n)/w_n),
 \qquad
 \Phi_N(x)=\int_0^xg_N(u)\,du.
\tag{10}
\]

The choices can be made recursively with the following four properties:

\[
 \beta(\Phi_N)\le-N,                                      \tag{11}
\]

\[
 |\kappa(\Phi_N)-\kappa(\Phi_{N-1})|\le e_N,             \tag{12}
\]

where \(\sum_{m>N}e_m\le h_N^2\), and, after choosing \(h_N>0\),

\[
 h_N<N^{-1},\qquad |\beta(\Phi_N)|h_N^2\le N^{-1},       \tag{13}
\]

\[
 \left|
 \frac{\bar\Delta^{\Phi_N}(h_N)-\kappa(\Phi_N)h_N^3}
 {h_N^5}-\beta(\Phi_N)
 \right|\le1.                                            \tag{14}
\]

Here is the complete recursion.  After \(h_j\) is fixed, let \(r_j>0\)
be a continuity radius in (15) which makes the output change at \(h_j\)
at most \(h_j^5\).  Once the first \(N-1\) stages are fixed, choose

\[
 0<\delta_N\le 2^{-N-2}\min\{\delta_*,1,r_1,\ldots,r_{N-1}\}.
\]

Then, for each fixed \(j\), the total amplitude chosen after stage \(j\)
is less than \(r_j/2\).  Choose \(x_N\) so large that (9) and
the Gaussian-tail bound make the left side of (12) at most

\[
 e_N=2^{-N}\min_{j<N}h_j^2,
\]

with the empty minimum at \(N=1\) defined to be one,

and then enlarge \(x_N\), if necessary, until (8) gives (11).  These two
requirements are compatible because the cubic change tends to zero while
the fifth change tends to minus infinity.  With \(\Phi_N\) fixed, (2)
allows a sufficiently small \(h_N\) satisfying (13)--(14).

It remains only to justify the stated continuity radii.  If \(\Psi\) is a
fixed smooth activation with bounded \(\Psi'\) and \(\Psi''\), then for
each fixed \(h\) the two-step formula above is continuous at \(\Psi\) in

\[
 d_1(\Psi,\widetilde\Psi)=
 \sup_x\frac{|\Psi(x)-\widetilde\Psi(x)|}{1+|x|}
 +\|\Psi'-\widetilde\Psi'\|_\infty.             \tag{15}
\]

To prove this, couple the two recursions with the same \((a,z)\).  The
first state difference is bounded by \(C\,d_1(1+|a|+|z|)\).  At the
second derivative evaluation, write

\[
 |\widetilde\Psi'(\widetilde z_1)-\Psi'(z_1)|
 \le \|\widetilde\Psi'-\Psi'\|_\infty
 +\|\Psi''\|_\infty|\widetilde z_1-z_1|.
\]

The terminal difference is therefore at most
\(C_{\Psi,h}d_1(1+|a|+|z|)^q\) for a fixed finite \(q\), which is
Gaussian-integrable.  Taking expectations proves (15).  A future sum of
transitions has \(d_1\)-distance at most twice the sum of its amplitudes.
The displayed amplitude recursion therefore ensures

\[
 |\bar\Delta^\Phi(h_N)-\bar\Delta^{\Phi_N}(h_N)|\le h_N^5,
 \tag{16}
\]

where \(g=1+\sum_n\delta_nR((x-x_n)/w_n)\) and
\(\Phi(x)=\int_0^xg\).  The same geometric budgeting of (12) gives

\[
 |\kappa_\infty-\kappa(\Phi_N)|\le h_N^2,
 \qquad \kappa_\infty=\lim_N\kappa(\Phi_N).     \tag{17}
\]

The series in (10) is locally finite.  Moreover
\(1\le g\le1+\sum_n\delta_n\le2\), so
\(\Phi\in C^\infty\), \(\|\Phi'\|_\infty\le2\), and
\(|\Phi(x)|\le2|x|\).  Thus every fixed-step scalar output is finite.

Combining (14), (16), and (17) yields, for
\(Q_\kappa(h)=(\bar\Delta^\Phi(h)-\kappa h^3)/h^5\),

\[
 |Q_{\kappa_\infty}(h_N)|\ge|\beta(\Phi_N)|-3\longrightarrow\infty.
\]

If \(\kappa\ne\kappa_\infty\), then by (13)

\[
 h_N^2Q_\kappa(h_N)
 =\kappa_\infty-\kappa+o(1),
\]

so this quotient also diverges.  This proves (1) for every \(\kappa\).

Finally let \(s=\|\Phi(G)\|_2\) and \(\phi=\Phi/s\).  Since
\(1\le\Phi'\le2\), one has \(0<s<\infty\).  The scaling identity

\[
 \bar\Delta^{c\Phi}(h)=c\,\bar\Delta^\Phi(ch)
\]

shows that property (1) is invariant under positive rescaling.  Hence the
RMS-normalized \(\phi\) has the asserted property.

## Full-OMFP transfer audit

The activation just constructed has bounded \(\phi'\) and linear growth,
so every fixed finite-width network chronology has finite moments of its
state and terminal output: the actual parameter update uses only
\(\phi\) and \(\phi'\).  This does **not** by itself prove that the
width-first full OMFP limit is finite.  Gaussian conditioning of a reused
connector introduces response expectations containing \(\phi''\), and
the spike construction was not designed to close every such generated
moment at every horizon.

Nevertheless, (1) is only a frozen-subsystem theorem.  In the actual
two-hidden-layer DAG, a lower-feature update changes the next top feature,
and reuse of the connector contributes aggregate adjoint responses.  The
terms involving these sources have the same Gaussian support and the same
singular derivative order as (5).  They are neither nonnegative nor
orthogonal after expectation.  Therefore one cannot delete them, compare
them monotonically with the frozen recursion, or infer a full-output lower
bound from (8).  A full counterexample requires additional theorems that
the full fixed-step DAG is well defined for this activation and that the
negative sector (6) survives the complete source sum.  Both statements are
currently open for this construction.
