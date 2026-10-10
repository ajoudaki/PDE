# Scalar frozen-top NTH: a truncation-order lower bound

Status: complete author-derived argument; not independently reviewed or promoted.
Input scope: the supervisor's self-contained scalar-model assignment only.
Required process and mathematical-presentation instructions were read; no
other study, book passage, code, or external scientific source was used.

This result concerns the standard NTH closure that retains levels through
order \(q\) and freezes its top level. It is not a lower bound for every
autonomous reduced model. The example has one hidden layer, linear activation,
one scalar training example, and both layers trained in the mean-field metric.
It does not establish a result for nonlinear activations, multiple samples,
or deeper networks.

## Model and exact hierarchy

Let the width be \(n\), let the fixed target satisfy \(0<y\leq1\), and put

\[
f_n=\frac1n\sum_{i=1}^n u_i a_i,
\qquad
\mathcal L=\frac12(f_n-y)^2,
\qquad
a_i(0)\overset{\mathrm{iid}}\sim N(0,1),
\quad u_i(0)=0.
\]

Here \(a_i\) is the scalar hidden preactivation for input \(1\), the activation
is the identity, and \(u_i\) is the readout. Mobility \(n\) for both parameter
families gives physical gradient flow

\[
\dot u_i=(y-f_n)a_i,
\qquad
\dot a_i=(y-f_n)u_i.
\]

For scalar parameter functions \(A,B\), define the mobility pairing and the
unit-residual directional derivative by

\[
\langle\nabla A,\nabla B\rangle_n
=n\sum_i\left(\partial_{u_i}A\,\partial_{u_i}B
                 +\partial_{a_i}A\,\partial_{a_i}B\right),
\qquad
D=\sum_i\left(a_i\partial_{u_i}+u_i\partial_{a_i}\right).
\]

The NTH coefficients are

\[
K_2=\langle\nabla f_n,\nabla f_n\rangle_n
=\frac1n\sum_i(a_i^2+u_i^2),
\qquad K_{r+1}=D K_r\quad(r\geq2).
\]

Direct differentiation gives

\[
Df_n=K_2,\qquad DK_2=4f_n,
\qquad
K_{2k}=4^{k-1}K_2,
\quad K_{2k+1}=4^k f_n\quad(k\geq1).
\]

Consequently, \(\dot f_n=(y-f_n)K_2\) and
\(\dot K_r=(y-f_n)K_{r+1}\). Define the initial empirical second moment
and the exact residual clock by

\[
S_n=\frac1n\sum_i a_i(0)^2,
\qquad
\dot s=y-f_n,\quad s(0)=0.
\]

Solving \(du_i/ds=a_i\), \(da_i/ds=u_i\) gives

\[
u_i=a_i(0)\sinh s,\qquad a_i=a_i(0)\cosh s,
\qquad
f_n=F_{S_n}(s),\quad
F_S(s)=\frac S2\sinh(2s).
\]

Thus \(\dot s=y-F_{S_n}(s)\). For every \(S>0\), this equation has a unique
global solution increasing from zero to the unique positive root of
\(F_S(s)=y\). Indeed its vector field is smooth, positive before that root,
and zero at it; uniqueness prevents crossing the equilibrium. The corresponding
output is in \([0,y)\) at every finite time and converges to \(y\).

## The standard frozen-top closure has its own clock

For an integer \(q\geq2\), the closure variables are \(f_{n,q}\) and
\(K_{2,n,q},\ldots,K_{q,n,q}\), with equations

\[
\begin{aligned}
\dot f_{n,q}&=(y-f_{n,q})K_{2,n,q},\\
\dot K_{r,n,q}&=(y-f_{n,q})K_{r+1,n,q}
                       &&(2\leq r<q),\\
\dot K_{q,n,q}&=0.
\end{aligned}
\]

Its initial values are copied from the dense network:
\(f_{n,q}(0)=0\), \(K_{2k,n,q}(0)=4^{k-1}S_n\), and
\(K_{2k+1,n,q}(0)=0\), whenever those levels are retained.
Define the closure's own residual clock by

\[
\dot z=y-f_{n,q},\qquad z(0)=0.
\]

Successive integration in \(z\), starting at the frozen top coefficient,
gives, with \(p=\lfloor q/2\rfloor\),

\[
f_{n,q}=P_{S_n,q}(z),
\qquad
P_{S,q}(z)=\frac S2\sum_{k=0}^{p-1}
                    \frac{(2z)^{2k+1}}{(2k+1)!},
\qquad
\dot z=y-P_{S_n,q}(z).
\]

This is the Taylor polynomial of \(F_S\) of degree \(2p-1\). In particular,
orders \(2p\) and \(2p+1\) give the same output. The closure is global:
\(P_{S,q}\) is smooth, strictly increasing on \([0,\infty)\), vanishes at
zero, and grows without bound. Its clock increases towards the unique positive
root of \(P_{S,q}(z)=y\), and its output remains in \([0,y)\).

The clocks \(s\) and \(z\) are not equal. A Taylor remainder at a common
clock is therefore not itself a physical-time error bound.

## A physical-time error bound uniform in the order

Fix

\[
T=\frac18,\qquad a=\frac y8,
\qquad \nu_q=2\lfloor q/2\rfloor+1.
\]

For every \(S\in[1/2,2]\) and every integer \(q\geq2\), the dense and
closure outputs initialized with this same \(S\) satisfy

\[
f_S(T)-f_{S,q}(T)
\geq \frac18\frac{a^{\nu_q}}{\nu_q!}
\geq \frac18\frac{a^{q+1}}{(q+1)!}.                 \tag{1}
\]

Here \(f_S\) means the exact output for empirical moment \(S\); it is not an
infinite-width limit. All constants in (1) are independent of \(q,n\).

To prove (1), let

\[
R_{S,q}(v)=F_S(v)-P_{S,q}(v)
=\frac S2\sum_{k=p}^{\infty}
              \frac{(2v)^{2k+1}}{(2k+1)!}.
\]

Both clocks are nonnegative and obey \(s(t),z(t)\leq yt\). To verify
\(z(t)\geq s(t)\) directly, put \(\delta=z-s\) and subtract their equations:
\[
\dot\delta=R_{S,q}(s)
-\delta\int_0^1P_{S,q}'(s+\theta\delta)\,d\theta.
\]
The integral is continuous, and the forcing \(R_{S,q}(s)\) is nonnegative.
The integrating-factor formula with \(\delta(0)=0\) therefore gives
\(\delta(t)\geq0\).
On \([0,T]\),

\[
F_S(s(t))\leq F_S(yt)
\leq Syt\cosh(2yt)
\leq \frac y4\cosh(1/4)<\frac y2.
\]

The middle inequality follows from
\(\sinh x=\int_0^x\cosh v\,dv\leq x\cosh x\) for \(x\geq0\).
It follows that \(\dot s\geq y/2\), and hence \(s(T)\geq yT/2\).
Furthermore, throughout \([0,yT]\),

\[
0\leq P_{S,q}'(v)\leq F_S'(v)
=S\cosh(2v)\leq M,
\qquad M=2\cosh(1/4)<4.
\]

Subtracting the clock equations also gives the exact identity

\[
\dot\delta
=R_{S,q}(s)-[P_{S,q}(z)-P_{S,q}(s)].                \tag{2}
\]

Since \(z\geq s\), the bracket is nonnegative. Since \(R_{S,q}\) and \(s\)
are increasing, integrating (2) yields

\[
0\leq\delta(T)
\leq\int_0^T R_{S,q}(s(t))\,dt
\leq T R_{S,q}(s(T)).
\]

The physical-time output gap, including the clock change, consequently obeys

\[
\begin{aligned}
f_S(T)-f_{S,q}(T)
&=R_{S,q}(s(T))-[P_{S,q}(z(T))-P_{S,q}(s(T))]\\
&\geq R_{S,q}(s(T))-M\delta(T)\\
&\geq (1-MT)R_{S,q}(s(T))\\
&\geq\frac12\frac S2
                \frac{(2s(T))^{\nu_q}}{\nu_q!}\\
&\geq\frac18\frac{(yT)^{\nu_q}}{\nu_q!}.
\end{aligned}
\]

Here \(MT<1/2\), \(S\geq1/2\), and \(2s(T)\geq yT\).
Finally \(\nu_q\leq q+1\) and the sequence \(a^j/j!\) decreases for
\(0<a\leq1/8\), proving the second inequality in (1).

The proof also applies to any larger compact horizon: its supremum includes
the fixed time \(T=1/8\). For a prescribed shorter positive horizon, replace
\(T\) by that horizon; the same reasoning works for all \(0<T\leq1/8\),
with \(a=yT\).

## Concentration and the necessary growth of the NTH order

Let

\[
c=\min\left\{\frac{\log2}{2}-\frac14,
                  \frac{1-\log2}{2}\right\}>0.
\]

Gaussian integration gives
\(\mathbb E e^{\lambda a_i(0)^2}=(1-2\lambda)^{-1/2}\) for
\(\lambda<1/2\). Exponential Markov bounds with \(\lambda=-1/2\) and
\(\lambda=1/4\), respectively, therefore give

\[
\begin{aligned}
\mathbb P(S_n<1/2)
&\leq e^{n/4}2^{-n/2}\leq e^{-cn},\\
\mathbb P(S_n>2)
&\leq e^{-n/2}2^{n/2}\leq e^{-cn}.
\end{aligned}
\]

Thus, with probability at least \(1-2e^{-cn}\), inequality (1) holds
simultaneously for every \(q\geq2\). In particular, writing

\[
E_n(q)=\sup_{0\leq t\leq T}|f_n(t)-f_{n,q}(t)|,
\]

any deterministic order sequence \(q_n\geq2\) satisfying
\(E_n(q_n)=O_{\mathbb P}(n^{-1/2})\) must obey

\[
\log((q_n+1)!)+(q_n+1)\log(8/y)
\geq\frac12\log n-O(1).                           \tag{3}
\]

Indeed, the deterministic lower bound in (1) holds with probability tending
to one. Tightness of \(\sqrt n E_n(q_n)\) therefore requires that the same
lower bound, multiplied by \(\sqrt n\), stay bounded.

Using \(\log((q+1)!)\leq(q+1)\log(q+1)\), (3) implies

\[
\liminf_{n\to\infty}\frac{q_n\log q_n}{\log n}\geq\frac12,
\qquad
q_n\geq\left(\frac12-o(1)\right)
                 \frac{\log n}{\log\log n}.        \tag{4}
\]

For completeness, if the first assertion failed by some fixed positive
margin along a subsequence, then
\(q_n=O(\log n/\log\log n)=o(\log n)\) along that subsequence.
The linear term in (3), and the difference between
\((q_n+1)\log(q_n+1)\) and \(q_n\log q_n\), would both be
\(o(\log n)\), contradicting (3). The second assertion follows by comparing
with any fixed smaller constant times \(\log n/\log\log n\).

This is a necessary-order result; it does not assert sufficiency or optimality
outside this scalar closure. The target \(y>0\) and time horizon are fixed
as \(n\to\infty\). The constants are not uniform as \(y\downarrow0\).

## The actual discrepancy between two dense networks

The exact scalar dynamics also satisfy

\[
\dot f_S=(y-f_S)\sqrt{S^2+4f_S^2},\qquad f_S(0)=0, \tag{5}
\]

because \(K_2=S\cosh(2s)\) and
\(K_2^2-4f_S^2=S^2\). The positive square root is selected by
\(K_2>0\).

For \(S,R\in[1/2,2]\), solutions of (5) obey the all-time sensitivity bound

\[
\sup_{t\geq0}|f_S(t)-f_R(t)|
\leq\frac{12y}{e}|S-R|.                           \tag{6}
\]

To verify it directly, at every finite \(t\) the exact solution is below
\(y\), and separation of (5) gives

\[
t=\int_0^{f_S(t)}
\frac{dv}{(y-v)\sqrt{S^2+4v^2}}.
\]

Differentiation with respect to \(S\) is legitimate on this finite integration
interval: the integrand and its \(S\)-derivative are continuous for \(S>0\)
and \(v<y\). Implicit differentiation yields

\[
\partial_S f_S(t)
=(y-f_S)\sqrt{S^2+4f_S^2}
\int_0^{f_S}
\frac{S\,dv}{(y-v)(S^2+4v^2)^{3/2}}\geq0.
\]

Writing \(r=y-f_S\), and using
\(S/(S^2+4v^2)^{3/2}\leq S^{-2}\), gives

\[
0\leq\partial_S f_S(t)
\leq\frac{\sqrt{S^2+4y^2}}{S^2}
             r\log(y/r)
\leq\frac{12y}{e}.
\]

The last step uses \(S\geq1/2\), \(S,y\leq2,1\), respectively,
\(\sqrt{S^2+4y^2}<3\), and
\(\max_{0<r\leq y}r\log(y/r)=y/e\), obtained by differentiating in \(r\).
The mean value theorem, followed by the supremum in \(t\), proves (6).

Now let \(\widetilde f_n\) be an independent dense network with the same
width, target, metric, and initialization law, and let \(\widetilde S_n\)
be its initial empirical second moment. Define the actual pair discrepancy

\[
D_n=\sup_{t\geq0}|f_n(t)-\widetilde f_n(t)|.
\]

Since \(\operatorname{Var}(S_n)=2/n\), independence gives
\(\operatorname{Var}(S_n-\widetilde S_n)=4/n\). For every
\(0<\delta<1\), Chebyshev's inequality and (6) yield the explicit bound

\[
\mathbb P\!\left(D_n\leq
           \frac{24y}{e\sqrt{\delta n}}\right)
\geq1-\delta-4e^{-cn}.                            \tag{7}
\]

The exponential term covers the event that either empirical moment leaves
\([1/2,2]\). Thus the actual dense-pair discrepancy is
\(O_{\mathbb P}(n^{-1/2})\), even over the entire half-line.
The same statement holds for any compact-time supremum.

Combining the actual pair bound with (1), if

\[
q_n=o\!\left(\frac{\log n}{\log\log n}\right),
\]

then

\[
\frac{E_n(q_n)}{D_n}\longrightarrow\infty
\quad\text{in probability}.                     \tag{8}
\]

To see the probability statement without an anti-concentration assumption,
put \(b_n=\tfrac18 a^{q_n+1}/(q_n+1)!\). The order assumption implies
\(\log b_n=-o(\log n)\), so \(\sqrt n b_n\to\infty\).
For any fixed \(A>0\),

\[
\mathbb P(E_n(q_n)\leq A D_n)
\leq2e^{-cn}
   +\mathbb P(\sqrt n D_n\geq\sqrt n b_n/A)
\longrightarrow0
\]

by tightness from (7). The denominator is positive almost surely:
\(S_n=\widetilde S_n\) has probability zero, and distinct empirical moments
give distinct initial output derivatives \(yS_n\) and
\(y\widetilde S_n\). Using the dense-pair supremum only on \([0,T]\)
makes the denominator smaller, so (8) remains valid on the common compact
horizon. In fact the same argument works whenever
\(\limsup q_n\log q_n/\log n<1/2\).

The quantifier in (7) is fixed confidence. It does not claim a deterministic
constant times \(n^{-1/2}\) bounds independent fluctuations with probability
tending to one. Statement (8), which compares with the actual pair discrepancy,
does have probability tending to one for every fixed ratio threshold.

## Interpretation and limitations

The lower bound detects bias from the particular frozen-top hierarchy.
Its two clocks are treated separately, and the Gaussian event is independent
of the truncation order, so the argument covers growing \(q\).

The example is not lazy in the width limit: for fixed \(t>0\),
\(u_i(t)=a_i(0)\sinh s(t)\) and
\(a_i(t)-a_i(0)=a_i(0)(\cosh s(t)-1)\) do not acquire a vanishing
width factor. Nevertheless, it is a special scalar, linear-activation model.
It cannot establish nonlinear/deep/multisample claims without a separate
construction that preserves those requirements.

No universal storage lower bound follows. A direct implementation of this
scalar hierarchy has \(q\) evolving scalar entries, but its coefficients
are highly structured, and the exact dynamics already admit the two-coordinate
closure

\[
\dot f=(y-f)K_2,\qquad\dot K_2=4(y-f)f,
\qquad (f(0),K_2(0))=(0,S_n),
\]

or the single evolving coordinate in (5), together with the fixed initial
moment \(S_n\). Thus growing order is necessary for the stated frozen-top
NTH rule, while a different exact closure has constant state dimension.
The usual generic \(m^q\) dense-tensor accounting is inapplicable as a storage
lower bound here because \(m=1\). Even for \(m>1\), generic tensor storage
would not by itself rule out symmetry, compression, or alternative closures.

Author checks: the \(q=2,3\) closures both give \(P_{S,q}(z)=Sz\);
the \(q=4,5\) closures both give
\(P_{S,q}(z)=S(z+2z^3/3)\), as direct integration of their hierarchy confirms.
The proof explicitly controls the altered physical clock and derives its
concentration and sensitivity estimates without an external scientific theorem.
No numerical experiment or independent review was performed for this route.
