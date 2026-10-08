# The current bounded packet network cannot inherit logarithmic compression

## Result and precise scope

The ideal, exact-arithmetic Gaussian version of the current
`BoundedGaussianPackets` initializer has a counterexample to the proposed
logarithmic-state guarantee. The example uses the implemented activation
`tanh`, two hidden layers, two spanning sphere inputs, a positive initial
population feature-Gram gap, and a fixed nonzero label vector within the paper's
small-label allowance. It does not change the optimizer or freeze features.

For this one fixed admissible problem, let \(n\) be the source and ordinary
dense-reference width, and \(q\ge2\) the packet network width. The packet
network stores exactly \(q^2+3q\) real weights. Let \(b_n\) be the paper's
99.99-percent quantile of the all-time, whole-sphere discrepancy of two
independent ordinary dense runs. Using the normalized input \(v=x/\sqrt d\),
the common error norm is

\[
\|f-g\|_*=
\sup_{t\in[0,\infty]}\sup_{\|v\|_2=1}|f(t,v)-g(t,v)|.
\]

The endpoint is included when it exists; as in the paper's benchmark,
lacking a required fitted limit makes the discrepancy infinite. The proof
only uses finite positive times. Then, for any deterministic choice

\[
q^2+3q=O((\log n)^K),\qquad K<\infty,
\]

the current packet construction satisfies

\[
\Pr\!\left\{\|f_{\rm packet}-f_n\|_*\le3b_n\right\}
\longrightarrow0.
\tag{1}
\]

Thus the requested 99-percent guarantee is false for this construction,
not merely unproved. This statement is about the current small-network
initializer followed by ordinary gradient flow. It does not refute the
paper's different Logarithmic decoder, Harmonic compression, or the
existence of another bounded-state construction.

There is also a stronger width-exponent consequence. For every fixed
\(0<\eta<1\), (1) still holds if

\[
q^2+3q=O(n^{1-\eta}).
\tag{2}
\]

Consequently a choice within this specific packet family that meets the
old contract at every sufficiently large width must have retained-weight
exponent at least one: for every fixed \(\eta>0\), its weight count must
eventually exceed \(n^{1-\eta}\). This is a necessary lower exponent,
not a sufficiency result or a sharp complexity characterization.

The witness is during early training, on a training input that belongs to
the sphere in the stated supremum. It is not an endpoint lower bound.
Both models may ultimately fit that training label exactly. Nor is it a
claim about the observed finite-width RMS on a finite held-out dataset.
Removing the two training inputs from the circle leaves the same supremum:
at each finite time the predictions are continuous and the remaining circle
is dense. This does not imply a statement about a finite held-out sample.

### Logical dependency

The new proof below is self-contained apart from elementary scalar limit
theorems and finite-dimensional ODE existence/continuation, whose needed
forms and hypotheses are stated when used. Its standalone conclusion is:
for this example, for every positive deterministic tolerance
\(\varepsilon_n\) and integer sequence \(q\ge2\),

\[
\frac qn\longrightarrow0,\qquad
q\varepsilon_n\longrightarrow0
\quad\Longrightarrow\quad
\Pr\!\left\{\|f_{\rm packet}-f_n\|_*\le\varepsilon_n\right\}
\longrightarrow0.
\tag{3}
\]

To specialize (3) to the old benchmark, the sole imported research result
is the existing dense upper theorem in `paper/results.tex`, equation
`eq:dense-variability`: at fixed admissible data and confidence,

\[
b_n\le C Y\left(\frac m\gamma\right)^5
\sqrt{\frac dn}\,\log(en)e^{\sqrt{\log(en)}}.
\tag{4}
\]

Here \(C\) depends only on the fixed activation and depth, as in that
supplied theorem. This study does not reprove or audit the paper's complete
dense upper theorem. The independent obstruction (3) does not need that
theorem. The comparison with the requested contract uses it exactly as
the already stated dense benchmark; no new propagation or decoder lemma
is assumed. The dense lower theorem is not used.

## 1. One fixed admissible problem and the exact algorithm

Set \(m=d=L=2\), take

\[
x_1=\sqrt2\,e_1,\qquad x_2=\sqrt2\,e_2,\qquad
y=(\sqrt2Y,0),\qquad \phi(z)=\tanh z.
\tag{5}
\]

The code receives the normalized inputs \(v_a=x_a/\sqrt d=e_a\).
For a standard normal scalar \(G\), define the fixed numbers

\[
\alpha=\mathbb E\tanh^2G\in(0,1),\qquad
\gamma=\mathbb E\tanh^2(\sqrt\alpha G)\in(0,1).
\tag{6}
\]

Independence of the two coordinates and oddness of `tanh` give exactly

\[
Q^{(0)}=I_2,\qquad Q^{(1)}=\alpha I_2,\qquad
Q^{(2)}=\gamma I_2.
\]

Thus the paper's gap is precisely the positive \(\gamma\) in (6). The
inputs span the space and \(m\ge d\), including the decoder's extra
geometric qualification. Orthogonal inputs are used as an admissible
example inside the general class, not imposed as a new theorem hypothesis.

The activation is holomorphic on \(|\operatorname{Im}z|<1/2\).
Indeed its nearest poles have imaginary part \(\pm\pi/2\), and

\[
|\cosh(x+iy)|^2=\sinh^2x+\cos^2y\ge\cos^2(1/2).
\]

Consequently \(|\tanh'|<2\) on this strip. Also

\[
|\tanh(x+iy)|^2
=\frac{\sinh^2x+\sin^2y}{\sinh^2x+\cos^2y}\le1
\quad (|y|\le1/2),
\]

so \(|\tanh''|\le4\) there. The appendix's activation envelope for strip
half-width \(1/2\) is therefore \(\beta=32\). Fix any

\[
0<Y\le\frac\gamma2\,32^{-60}.
\tag{7}
\]

This is exactly within \(Y\le(\gamma/m)\beta^{-30L}\). Labels are fixed
once and do not shrink with \(n\) or \(q\). Their extreme possible smallness
does not remove the obstruction.

For any width \(p\), the network and loss are

\[
\begin{aligned}
h^{(1)}(t,v)&=\tanh(W^{(1)}(t)v),\\
h^{(2)}(t,v)&=\tanh(W^{(2)}(t)h^{(1)}(t,v)),\\
f(t,v)&=w(t)^\top h^{(2)}(t,v)/p,\\
\mathcal L(t)&=\frac1m\sum_a(f(t,v_a)-y_a)^2.
\end{aligned}
\tag{8}
\]

The block mobilities for \((W^{(1)},W^{(2)},w)\) are \((p,1,p)\), and
\(w(0)=0\). These are precisely `dense_fields` and `dense_rhs`, with
code state order `(first, readout, hidden)`.

The ordinary reference uses \(p=n\), independent \(N(0,1)\) first weights
and independent \(N(0,1/n)\) hidden weights. For the packet model, draw
\(W^{(1)}_{ia}(0)\) independently from \(N(0,1)\), and let
\(H\in\mathbb R^{q\times2}\) contain its initialized first features:
\(H_{ia}=\tanh(W^{(1)}_{ia}(0))\). The packet first layer, Gaussian mixer,
Haar frame and source draws are mutually independent. Independently generate
\(n\) ordinary
first-feature rows \(H_{\rm source}\), and set

\[
K=H_{\rm source}^\top H_{\rm source}/n,
\qquad RR^\top=K,
\qquad Z=\sqrt q\,U R^\top.
\tag{9}
\]

Here \(R\) is the lower Cholesky factor and \(U\in\mathbb R^{q\times2}\)
is Haar-uniform with orthonormal columns, independent of the source.
The sign-corrected Gaussian QR in the code has this distribution: the
Gaussian law is unchanged by left orthogonal transformations, and QR
with positive diagonal is equivariant under those transformations. Its
first column is, directly, a Gaussian vector divided by its norm.

Writing \(H^\dagger=(H^\top H)^{-1}H^\top\), the actual initialized mixer
is

\[
W^{(2)}(0)=G_q+(Z-G_qH)H^\dagger
=G_q(I-HH^\dagger)+ZH^\dagger,
\tag{10}
\]

where \(G_q\) has independent \(N(0,1/q)\) entries. This is the code's QR
and triangular solve, not an alternative initializer. The Gaussian-derived
entries of \(H\) and \(H_{\rm source}\) have continuous densities on
\((-1,1)\), so their first two rows are nonsingular almost surely. Thus
all inverses exist for \(q,n\ge2\) in exact arithmetic. Equations (9)--(10)
give exactly

\[
W^{(2)}(0)H=Z,\qquad Z^\top Z/q=K.
\tag{11}
\]

Crucially, (11) does not also give an exact Gram identity for \(\tanh Z\).

## 2. A nonzero fluctuation survives the next activation

Since the initial readout vanishes, both hidden-weight velocities vanish
at time zero, whereas

\[
\dot w(0)=\frac2m\sum_a y_a h^{(2)}(0,v_a).
\]

At the first input, (5) therefore gives the exact identity

\[
\dot f(0,v_1)=\sqrt2Y\,
\frac1p\sum_{i=1}^p h^{(2)}_i(0,v_1)^2.
\tag{12}
\]

Put \(K_{11}=n^{-1}\sum_{i=1}^n\tanh^2 V_i\), where the \(V_i\) are
independent standard normals. Then
\(K_{11}-\alpha=O_{\mathbb P}(n^{-1/2})\), because the summands are bounded.
Here \(O_{\mathbb P}(r_n)\) means bounded in probability after division by
\(r_n\), and \(o_{\mathbb P}(r_n)\) means convergence to zero in probability
after that division.

The first column of \(R^\top\) is \((\sqrt{K_{11}},0)^\top\). Hence,
with \(u\) uniform on the unit sphere in \(\mathbb R^q\), the packet model's
average in (12) is distributed exactly as

\[
\frac1q\sum_{i=1}^q\tanh^2(\sqrt{qK_{11}}\,u_i).
\tag{13}
\]

We prove its fluctuation rather than assuming independent packet rows.
Write \(u_i=X_i/\sqrt{\sum_jX_j^2}\), with independent standard normal
\(X_i\), and let \(s_q=q^{-1}\sum_iX_i^2\). Uniform angular distribution
follows from the radial Gaussian density in polar coordinates. Define the
bounded smooth function \(g(x)=\tanh^2(\sqrt\alpha x)\), and the constant

\[
\kappa=\tfrac12\mathbb E[Gg'(G)]
=\mathbb E[\sqrt\alpha G\tanh(\sqrt\alpha G)
                         \operatorname{sech}^2(\sqrt\alpha G)]>0.
\tag{14}
\]

Taylor expansion in \(s_q\), around one, gives

\[
\begin{split}
\sqrt q\left[\frac1q\sum_i g(X_i/\sqrt{s_q})-\gamma\right]
={}&\frac1{\sqrt q}\sum_i
 \left[g(X_i)-\gamma-\kappa(X_i^2-1)\right]
 +o_{\mathbb P}(1).
\end{split}
\tag{15}
\]

Here are the remainder checks. For \(f(z)=\tanh^2z\), both
\(\sup_z|zf'(z)|\) and \(\sup_z|z^2f''(z)|\) are finite by exponential
decay of the derivatives. For \(F(s,x)=f(\sqrt{\alpha/s}\,x)\),

\[
F_s=-\frac{zf'(z)}{2s},\qquad
F_{ss}=\frac{3zf'(z)+z^2f''(z)}{4s^2},
\qquad z=\sqrt{\alpha/s}\,x.
\]

Thus the second derivative is uniformly bounded for \(1/2\le s\le3/2\).
Since \(\operatorname{Var}(s_q)=2/q\), the averaged Taylor remainder is
\(O_{\mathbb P}(q^{-1})\). The empirical first-derivative coefficient
converges in probability to \(-\kappa\), since it is a bounded iid average;
multiplication by \(\sqrt q(s_q-1)=O_{\mathbb P}(1)\) proves (15).

Replacing \(\alpha\) by \(K_{11}\) in (13) costs
\(O_{\mathbb P}(n^{-1/2})\), uniformly in \(q\). Indeed

\[
\left|\frac{\partial}{\partial k}f(\sqrt{qk}\,u_i)\right|
=\frac{|zf'(z)|}{2k},
\]

which is uniformly bounded when \(k\ge\alpha/2\); that event has probability
tending to one for \(K_{11}\). Therefore this replacement is negligible
in (15) whenever \(q/n\to0\).

The summands in (15) are iid, centered, and have finite variance

\[
\sigma^2=\operatorname{Var}\!\left(g(G)-\kappa(G^2-1)\right)>0.
\tag{16}
\]

To verify strict positivity, zero variance would force the continuous
identity \(g(x)-\gamma=\kappa(x^2-1)\) for every real \(x\), because a
Gaussian density is positive on every interval. Its left side is bounded
and its right side is unbounded, with \(\kappa>0\), a contradiction.
The scalar iid central limit theorem applies to these centered finite-
variance summands: their sum divided by \(\sqrt q\) converges to
\(N(0,\sigma^2)\). Adding terms that tend to zero in probability preserves
this limit. These elementary limit theorems are used only with the explicit
summands and checked moments above, not as an independence assumption on
the packet rows.

For the ordinary dense network, condition on its first layer. Its second
preactivations at \(v_1\) are independent \(N(0,K'_{11})\), with
\(K'_{11}-\alpha=O_{\mathbb P}(n^{-1/2})\). The average of their squared
`tanh` values has conditional variance at most \(1/(4n)\). Its conditional
mean differs from \(\gamma\) by \(O_{\mathbb P}(n^{-1/2})\), using the
same bounded radius derivative. Consequently its whole average is
\(\gamma+O_{\mathbb P}(n^{-1/2})\).

Combining this observation with (12)--(16), if \(q\to\infty\) and
\(q/n\to0\),

\[
\sqrt q\,[\dot f_{\rm packet}(0,v_1)-\dot f_n(0,v_1)]
\ \Longrightarrow\ N(0,2Y^2\sigma^2).
\tag{17}
\]

The variance is strictly positive. No coupling to the target can cancel
it while the target retains its ordinary dense marginal: the target's
fluctuation becomes zero in probability at this scale. In particular the
independent-reference contract is covered.

## 3. Uniform control of actual nonlinear evolution

We must not mistake (17) for a prediction lower bound. This section proves
the required width-uniform remainder for the actual gradient flow.

For (8), write \(r_a=f(t,v_a)-y_a\), and let \(D_a^{(\ell)}\) be the
diagonal matrix of derivatives \(1-(h_a^{(\ell)})^2\), whose operator norm
is at most one. Exact differentiation yields

\[
\begin{aligned}
\dot w&=-\frac2m\sum_a r_a h_a^{(2)},\\
\dot W^{(2)}&=-\frac2{pm}\sum_a r_a
                  D_a^{(2)}w\,h_a^{(1)\top},\\
\dot W^{(1)}&=-\frac2m\sum_a r_a
                  D_a^{(1)}W^{(2)\top}D_a^{(2)}w\,v_a^\top.
\end{aligned}
\tag{18}
\]

Loss dissipation is

\[
\dot{\mathcal L}
=-\|\dot W^{(1)}\|_F^2/p
 -\|\dot W^{(2)}\|_F^2-\|\dot w\|_2^2/p\le0.
\]

Because \(\mathcal L(0)=Y^2\), it follows that
\(m^{-1}\sum_a|r_a(t)|\le Y\). If
\(\|W^{(2)}(0)\|_{\rm op}\le M\), equations (18) and bounded tanh give

\[
\begin{aligned}
\|w(t)\|_2/\sqrt p&\le2Yt,\\
\|W^{(2)}(t)-W^{(2)}(0)\|_F&\le2Y^2t^2,\\
\|\dot W^{(1)}(t)\|_F/\sqrt p
&\le4Y^2t(M+2Y^2t^2).
\end{aligned}
\tag{19}
\]

For example, the hidden-matrix derivative is bounded by
\(2Y\|w\|_2/\sqrt p\), because each forward feature has Euclidean norm
at most \(\sqrt p\). The first-layer bound uses only
\(\|W^{(2)\top}D_a^{(2)}w\|_2\le\|W^{(2)}\|_{\rm op}\|w\|_2\);
no coordinatewise backward-signal bound is required.

The smooth finite-dimensional vector field has a unique local solution.
The bounds (19) keep every parameter in a finite closed ball on each
finite time interval. A maximal solution to a locally Lipschitz ODE can
end at a finite time only if it leaves every compact set. Since finite-
dimensional closed bounded sets are compact, (19) rules that out. Thus
the exact flow exists at all finite times, including the times used below.

Set \(S=1+(M+2Y^2)^2\) locally in this section. For \(0\le t\le1\),
differentiating both forward layers at any \(\|v\|_2\le1\) and using
\(|\tanh'|\le1\) and (19) gives

\[
\|\dot h^{(2)}(t,v)\|_2/\sqrt p\le4Y^2 S t,
\qquad
\|h^{(2)}(t,v)-h^{(2)}(0,v)\|_2/\sqrt p\le2Y^2S t^2.
\tag{20}
\]

To spell out the first bound, the second-layer preactivation derivative
has terms \(\dot W^{(2)}h^{(1)}\) and \(W^{(2)}\dot h^{(1)}\).
Their Euclidean norms divided by \(\sqrt p\) are bounded by
\(4Y^2t\) and \(4Y^2t(M+2Y^2)^2\), respectively.

Subtract the initial readout derivative in (18):

\[
\dot w(t)-\dot w(0)
=-\frac2m\sum_a f(t,v_a)h^{(2)}(t,v_a)
 +\frac2m\sum_a y_a[h^{(2)}(t,v_a)-h^{(2)}(0,v_a)].
\]

Since \(|f(t,v_a)|\le2Yt\), (20) implies

\[
\|w(t)-t\dot w(0)\|_2/\sqrt p
\le2Yt^2+\frac43Y^3S t^3.
\]

Finally expand the actual prediction as

\[
\begin{split}
f(t,v)-t\dot f(0,v)
={}&\frac{[w(t)-t\dot w(0)]^\top h^{(2)}(t,v)}p\\
&+t\frac{\dot w(0)^\top[h^{(2)}(t,v)-h^{(2)}(0,v)]}p.
\end{split}
\]

The second term is at most \(4Y^3S t^3\), since
\(\|\dot w(0)\|_2/\sqrt p\le2Y\). Therefore

\[
|f(t,v)-t\dot f(0,v)|
\le 2Yt^2+\frac{16}{3}Y^3[1+(M+2Y^2)^2]t^3
\quad(0\le t\le1).
\tag{21}
\]

This estimate includes hidden feature learning; nothing has been replaced
by a frozen-feature flow.

### Why the initial operator bound is width-uniform

Let \(P=HH^\dagger\). The two summands in (10) act on orthogonal input
subspaces, giving the exact identity

\[
W^{(2)}(0)W^{(2)}(0)^\top
=G_q(I-P)G_q^\top+Z(H^\top H)^{-1}Z^\top.
\]

Consequently

\[
\|W^{(2)}(0)\|_{\rm op}^2
\le\|G_q\|_{\rm op}^2
 +\frac{\|K\|_{\rm op}}{\lambda_{\min}(H^\top H/q)}.
\tag{22}
\]

Bounded features give \(\|K\|_{\rm op}\le\operatorname{tr}K\le2\),
uniformly in source width. The entries of \(H^\top H/q\) converge in
probability to those of \(\alpha I_2\): their means are the indicated
entries and each has variance at most \(1/q\). Thus its smallest eigenvalue
is at least \(\alpha/2\) with probability tending to one.

Here is an elementary Gaussian operator bound. A maximal \(1/4\)-separated
set on the unit sphere in \(\mathbb R^p\) is a \(1/4\)-net of size at most
\(9^p\), by comparing disjoint radius-\(1/8\) balls with a radius-\(9/8\)
ball. Approximating each of two unit test vectors by this net gives
\(\|G_p\|_{\rm op}\le2\max_{u,v\text{ in net}}|u^\top G_pv|\).
For fixed \(u,v\), the latter scalar is \(N(0,1/p)\); its Gaussian
moment-generating function and Markov's inequality yield
\(\Pr\{|u^\top G_pv|>4\}\le2e^{-8p}\). The union bound therefore gives

\[
\Pr\{\|G_p\|_{\rm op}>8\}
\le2e^{-p(8-2\log9)}\longrightarrow0.
\tag{23}
\]

It follows from (22)--(23) that both the packet and ordinary dense initial
mixers have norm at most \(M=\sqrt{64+4/\alpha}\), with probability
tending to one when \(q,n\to\infty\). For bounded \(q\ge2\), (22) still
gives tight operator norms uniformly in \(n\): each fixed-\(q\) matrix
\(H^\top H\) is positive definite almost surely, and the source norm is
bounded by two. A finite collection of such almost-surely finite bounds
is tight. Equation (21) consequently has a constant bounded in probability
uniformly over every sequence \(q,n\ge2\).

## 4. From the derivative fluctuation to failure of the actual contract

First suppose \(q\to\infty\), \(q/n\to0\), and
\(q\varepsilon_n\to0\). Set \(t_n=\sqrt{\varepsilon_n}\), which tends
to zero. Apply (21) separately to the two exact flows, then use the tight
initial norms:

\[
\begin{split}
\frac{\sqrt q}{t_n}
 [f_{\rm packet}(t_n,v_1)-f_n(t_n,v_1)]
={}&\sqrt q[\dot f_{\rm packet}(0,v_1)-\dot f_n(0,v_1)]\\
&+O_{\mathbb P}(\sqrt q\,t_n)
\ \Longrightarrow\ N(0,2Y^2\sigma^2).
\end{split}
\tag{24}
\]

The remainder tends to zero because \(\sqrt q\,t_n=\sqrt{q\varepsilon_n}\).
If the full trajectory error were at most \(\varepsilon_n\), the absolute
value of the left side of (24) would be at most

\[
\frac{\sqrt q}{t_n}\varepsilon_n=\sqrt{q\varepsilon_n}\longrightarrow0.
\]

A nondegenerate Gaussian has no atom at zero. More explicitly, for any
fixed \(a>0\), convergence in distribution bounds the limiting probability
of a shrinking interval around zero by the Gaussian probability of
\([-a,a]\); this probability tends to zero as \(a\downarrow0\).
Thus the full-contract success probability tends to zero.

For a direct witness not using a requested tolerance, taking \(t_n=1/q\)
in (21) instead gives

\[
q^{3/2}[f_{\rm packet}(1/q,v_1)-f_n(1/q,v_1)]
\ \Longrightarrow\ N(0,2Y^2\sigma^2).
\tag{25}
\]

This already excludes polylogarithmic \(q\) at the dense benchmark.
The tolerance-dependent witness (24) supplies the stronger exponent
consequence (2). Neither witness is a parameter of the algorithm.

### Fixed or oscillating packet widths do not provide a loophole

For each fixed \(q\ge2\), the observable in (13) with \(K_{11}=\alpha\)
has no atoms. Here is an elementary verification. Let
\(h(s)=\tanh^2(\sqrt{q\alpha s})\) for \(s\ge0\). For \(s>0\),

\[
h'(s)=q\alpha\,
\frac{\tanh z}{z}\operatorname{sech}^2z,
\qquad z=\sqrt{q\alpha s}.
\]

This derivative is strictly decreasing. Both displayed positive factors
are strictly decreasing in \(z>0\); for the first, the numerator in the
negative derivative is \(\tanh z-z\operatorname{sech}^2z>0\), since it is
zero at zero and has derivative \(2z\operatorname{sech}^2z\tanh z>0\).
The derivative extends continuously at \(s=0\), so \(h\) is strictly
concave on the nonnegative axis.

Represent the sphere point by normalized Gaussians and condition on the
radius of its first two Gaussian coordinates and on the remaining
coordinates. The angle \(\theta\) is still uniform. The first two terms
in the sum (13) are then proportional to

\[
h(s\cos^2\theta)+h(s\sin^2\theta),\qquad 0<s\le1,
\]

while the remaining terms are fixed. The function
\(u\mapsto h(su)+h(s(1-u))\) is strictly increasing for \(u<1/2\) and
strictly decreasing for \(u>1/2\), by the strict decrease of \(h'\).
Every level has at most two such \(u\)'s and finitely many corresponding
angles. A uniform angle assigns them probability zero. Averaging the
conditional probabilities proves the absence of atoms, including \(q=2\).

For fixed \(q\), radius convergence and the dense law of large numbers
therefore give a nonatomic limit for
\(\dot f_{\rm packet}(0,v_1)-\dot f_n(0,v_1)\). With
\(t_n=\sqrt{\varepsilon_n}\), (21) implies

\[
\frac{f_{\rm packet}(t_n,v_1)-f_n(t_n,v_1)}{t_n}
=\dot f_{\rm packet}(0,v_1)-\dot f_n(0,v_1)
 +O_{\mathbb P}(t_n).
\]

The right side has the same nonatomic limit; success would require its
absolute value to be at most \(\sqrt{\varepsilon_n}\to0\). Its probability
again tends to zero. Finally, every subsequence of integers \(q\ge2\)
has a further subsequence on which \(q\) is constant or tends to infinity.
The two preceding arguments exclude a positive limiting success
probability along either type. This proves the standalone statement (3)
for arbitrary such \(q(n)\).

## 5. Storage consequence and what must change

At the fixed example (5)--(7), (4) is \(b_n\le n^{-1/2+o(1)}\), with
all constants fixed. If \(q^2+3q=O(n^{1-\eta})\), then
\(q/n\to0\) and \(q(3b_n)\le n^{-\eta/2+o(1)}\to0\). Apply (3) with
\(\varepsilon_n=3b_n\), or any positive upper envelope of that quantity,
to prove (2) and (1). Using a positive upper envelope also covers any
degenerate zero value of \(b_n\); the proof does not require the dense
lower theorem. For a choice claimed successful eventually at every width,
apply this reasoning on any subsequence where the state is at most
\(n^{1-\eta}\). Such a subsequence is impossible, proving the stated
necessary exponent.

The mechanism is specific. Balancing \(\frac1q Z^\top Z\) removes a
quadratic fluctuation. In (15) this removes the Gaussian component
\(\kappa(G^2-1)\). The nonlinear remainder has the strictly positive
variance (16). Since the current readout and optimizer use ordinary
equal-weight averages over \(q\) actual neurons, that remainder enters
the prediction velocity. The finite numerical experiments can still show
a useful constant-factor reduction of error at moderate widths; such a
reduction is consistent with (17) and does not imply the width-\(n\)
accuracy scale at polylogarithmic \(q\).

The paper's Logarithmic decoder is a different object: it retains finite
packets, a metric, seeds and scalar information while regenerating width-\(n\)
empirical interactions. Its small storage is not obtained by replacing
every such interaction with an unweighted average over \(q\) actual
neurons. The initial identities of the bounded packet network do not
implement that mechanism.

Matching the post-activation training Gram as well would remove this
particular first-derivative obstruction, but would not by itself prove
control of later nonlinear or backward responses. That would be a changed
construction with new proof obligations, not a proof of the present model.

## Source, checks and limitations

The exact code inputs are `dense_fields`, `dense_rhs`, `Dense`, and
`BoundedGaussianPackets` in `paper/figures/capture_trajectory.py`, source
SHA256 `bbb53b4e473be7efa079bc7d46fe5a4564e0625630c701fa7a3dd5152e8f69b2`.
The original sphere normalization, mobility and benchmark are read from
`paper/main.tex` and `paper/results.tex`; activation and label formulas
are in the shared-setup and label-allowance sections of
`paper/integrated_appendix.tex`. The decoder distinction is documented in
`paper/methods.tex`. No other study or empirical result is a premise.

Independent scoped derivations are retained as `PROBABILITY_LEMMA.md` and
`FLOW_LEMMA.md`; `CONTRACT_AUDIT.md` checks the original qualifications
and the implication conditional on those two ingredients. The assembled
argument above incorporates the ingredients and the fixed-width case.
Final reconstruction reports and their precise isolation qualifications
are recorded in the study README.

This is an exact-real, ideal-Gaussian mathematical obstruction. No claim
about rounding, rank-rejection rates or an arbitrary finite-word PRNG is
needed or proved. No experiments were run, and no implementation or
paper theorem was changed. This study is not promotion to established theory.
