## Three Gaussian queries and the failure of uniform higher moments

This is a statement about initial Gaussian matrix actions with reused
transposes. It is not a claim about queries reached during neural training.
The width limit is taken separately for each fixed coordinate map; only
then does a localization parameter tend to zero.

Fix a smooth even \(\psi:\mathbb R\to[0,1]\), equal to one on
\([-1/2,1/2]\) and zero outside \([-1,1]\). Such a function is obtained
by integrating and rescaling a smooth compactly supported bump on each
transition interval and reflecting evenly. For \(0<\epsilon\le1\), set

\[
 v_\epsilon=\mathbb E\psi(G/\epsilon)^2>0,\qquad
 c=\mathbb E\operatorname{sech}^2G>0,\qquad
 \sigma^2=\mathbb E\tanh^2G>0,
 \quad G\sim N(0,1).
 \tag{A.1}
\]

For \(W_n\) with independent \(N(0,1/n)\) entries, perform exactly
three calls:

\[
 y=W_n\mathbf1,\quad e=\psi(y/\epsilon),\quad
 q=W_n^Te,\quad h=\tanh(q/\sqrt{v_\epsilon}),\quad T=W_nh.
 \tag{A.2}
\]

The scalar constant \(v_\epsilon\) is fixed before the calculation.
Each coordinate map is bounded, smooth and globally Lipschitz for fixed
\(\epsilon\). Its Lipschitz bound need not be uniform in \(\epsilon\).

The same-column empirical law of \((q,h)\) converges in probability in
\(\mathcal W_2\) to \((\sqrt{v_\epsilon}G,\tanh G)\).
The same-row empirical law of \((y,e,T)\) converges in the same sense to

\[
 \left(Y,\psi(Y/\epsilon),
         \sigma H+\frac{c}{\sqrt{v_\epsilon}}\psi(Y/\epsilon)\right),
 \qquad Y,H\text{ independent standard Gaussians}.
 \tag{A.3}
\]

The row and column populations are separate; no neuron pairing between them
is asserted. We now prove all the required matrix-reuse and empirical steps.

### A.1 Two exact conditioning steps

Write
\(a_n=y^Te/n\), \(v_n=e^Te/n\), and
\(P_0=I-\mathbf1\mathbf1^T/n\). The row sums \(y_i\) are independent
standard Gaussians. Conditional Gaussian projection gives
\(W_n=y\mathbf1^T/n+Z_nP_0\), with independent Gaussian \(Z_n\) of the
original law. Consequently

\[
 q\mid y\ \overset d=\ a_n\mathbf1+\sqrt{v_n}P_0g,
 \qquad g\sim N(0,I_n),\quad g\text{ independent of }y.
 \tag{A.4}
\]

On \(v_n>0\), conditioning again on \(q\) gives

\[
 W_n\mid(y,q)\ \overset d=
 \frac{y\mathbf1^T}{n}+
 \frac{e(q-a_n\mathbf1)^T}{nv_n}+
 P_{e^\perp}\widetilde W_nP_0,
 \quad P_{e^\perp}=I-\frac{ee^T}{nv_n}.
 \tag{A.5}
\]

To verify the law, the first two terms obey the two observed linear
constraints, and their sum is orthogonal in Frobenius inner product to the
homogeneous subspace \(\{M:M\mathbf1=0,M^Te=0\}\). The last term is
the orthogonal projection of an isotropic Gaussian onto that subspace.
In an orthonormal basis adapted to the subspace, Gaussian coordinates on
it and its orthogonal complement are independent; conditioning fixes the
latter coordinates and leaves the former unchanged. This proves (A.5),
including its covariance, without an independent-transpose assumption.

The event \(v_n=0\) has probability at most
\((1-\mathbb P(|G|\le\epsilon/2))^n\), tending to zero. On it the
actual \(e,q,h,T\) are all zero. Auxiliary ratios may be set to zero
there without affecting convergence in probability.

Put \(m_n=\mathbf1^Th/n\),
\(s_n=\|P_0h\|_2/\sqrt n\), and
\(b_n=(q-a_n\mathbf1)^Th/(nv_n)\). Multiplying (A.5) by \(h\) yields

\[
 T\mid(y,q)\ \overset d=\ m_n y+b_n e+s_nP_{e^\perp}g',
 \qquad g'\sim N(0,I_n)\text{ independent of the transcript}.
 \tag{A.6}
\]

### A.2 Joint empirical laws

The law of large numbers gives \(a_n\to0\) by evenness of \(\psi\),
and \(v_n\to v_\epsilon>0\). In the coupling (A.4),

\[
 \frac{\|q-\sqrt{v_\epsilon}g\|_2}{\sqrt n}
 \le |a_n|+|\sqrt{v_n}-\sqrt{v_\epsilon}|\frac{\|g\|_2}{\sqrt n}
              +\sqrt{v_n}|\mathbf1^Tg/n|\longrightarrow0.
 \tag{A.7}
\]

The Lipschitz constant \(v_\epsilon^{-1/2}\) transfers this to
\(\|h-\tanh g\|_2/\sqrt n\to0\). Thus
\(m_n\to0\), \(s_n^2\to\sigma^2\). Moreover Cauchy–Schwarz bounds

\[
 \left|\frac{(q-a_n\mathbf1)^Th}{n}
       -\frac{\sqrt{v_\epsilon}}n\sum_i g_i\tanh g_i\right|
\]

by
\(\|q-a_n\mathbf1-\sqrt{v_\epsilon}g\|_2\|h\|_2/n+
\sqrt{v_\epsilon}\|g\|_2\|h-\tanh g\|_2/n\), which tends to zero.
Gaussian integration by parts gives
\(\mathbb E[G\tanh G]=\mathbb E\operatorname{sech}^2G=c\): the
boundary term is zero because \(\tanh\) is bounded. Therefore
\(b_n\to c/\sqrt{v_\epsilon}\).

In (A.6), the removed Gaussian projection has conditional normalized
squared expectation \(1/n\). Since \(s_n\le1\), its effect tends to
zero in probability. The triangle inequality then couples \(T\) in
normalized mean square to
\(t_i^0=\sigma g'_i+(c/\sqrt{v_\epsilon})\psi(y_i/\epsilon)\):

\[
 \frac{\|T-t^0\|_2}{\sqrt n}\le
 |m_n|\frac{\|y\|_2}{\sqrt n}
 +|b_n-c/\sqrt{v_\epsilon}|\sqrt{v_n}
 +|s_n-\sigma|\frac{\|g'\|_2}{\sqrt n}
 +s_n\frac{\|(I-P_{e^\perp})g'\|_2}{\sqrt n}\longrightarrow0.
\]

The ideal tuples are iid with finite second moments. Their empirical laws
converge in \(\mathcal W_2\) in probability: restrict to a large bounded
ball, partition it into finitely many small cells, use the law of large
numbers for cell masses, and bound the discarded quadratic cost by the
second-moment tail. Coupling corresponding coordinates bounds the squared
\(\mathcal W_2\) error by the normalized squared errors just proved.
This establishes (A.3) and the column law. It establishes no higher-moment
convergence merely from \(\mathcal W_2\).

### A.3 Higher moments and the scope of the obstruction

Let \(T_\epsilon\) denote the third coordinate of (A.3). Every fixed
\(\epsilon\) gives all finite moments, since it is a Gaussian plus a
bounded shift. Conditional Jensen and the density
\(\gamma_0(x)=(2\pi)^{-1/2}e^{-x^2/2}\) give, for every finite \(p>2\),

\[
 \mathbb E|T_\epsilon|^p
 \ge c^p v_\epsilon^{-p/2}\mathbb E\psi(Y/\epsilon)^p,
\]
\[
 v_\epsilon\le2\gamma_0(0)\epsilon,\qquad
 \mathbb E\psi(Y/\epsilon)^p\ge\gamma_0(1)\epsilon,
\]
\[
 \|T_\epsilon\|_{L^p}\ge
 \frac{c\gamma_0(1)^{1/p}}{\sqrt{2\gamma_0(0)}}
                \epsilon^{1/p-1/2}\longrightarrow\infty.
 \tag{A.8}
\]

Meanwhile the input law is always \(h_\epsilon\overset d=\tanh G\),
so its essential supremum is one and its \(L^p\) norm is a fixed positive
number less than one. Its output second moment is exactly
\(\mathbb E T_\epsilon^2=\sigma^2+c^2\), independently of \(\epsilon\).
Thus a bounded \(L^2\) action is compatible with this divergence.

Equivalently, in any common population realization with bounded actual
\(L^2\) action \(W\), its adjoint, constants and the displayed finite
Gaussian-program laws, the generated inputs
\(h_\epsilon=\tanh(W^*\psi(W\mathbf1/\epsilon)/\sqrt{v_\epsilon})\)
violate every finite \(L^\infty\to L^p\) or \(L^p\to L^p\) bound for
\(W\). It suffices that the realization contains the countable scales
\(\epsilon=1/k\). No new coordinate roots are needed: the Gaussian
innovation in (A.3) is the random variable
\((Wh_\epsilon-c\psi(W\mathbf1/\epsilon)/\sqrt{v_\epsilon})/\sigma\)
on its existing row space. No independence between different scales is
required. The same argument applies to the reverse orientation because
\(W_n^T\) has the same initial matrix law.

These conclusions concern the uniform class of bounded generated inputs
whose coordinate sensitivities may grow with \(\epsilon^{-1}\).
They give no counterexample to bounds with controlled sensitivities or
to tails on an actual reached training family. Width is sent to infinity
at fixed \(\epsilon\) before (A.8); no width-dependent bump scale or
positive-time training limit is asserted.
