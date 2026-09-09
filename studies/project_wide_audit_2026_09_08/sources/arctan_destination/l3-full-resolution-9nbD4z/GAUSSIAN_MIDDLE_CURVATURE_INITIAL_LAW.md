# Exact Gaussian conditioning for the initial middle-layer curvature

Status: frozen candidate pending a fresh isolated combined audit. This lemma concerns only the initial hidden-layer law. It makes no positive-time, readout, Duhamel-remainder, or full-theorem claim.

## Statement

For each integer \(n\geq1\), let
\[
z_{0,i}^{(1)}\overset{\mathrm{iid}}{\sim}N(0,1),\qquad
(W_0^{(2)})_{ij},(W_0^{(3)})_{ij}
\overset{\mathrm{iid}}{\sim}N(0,1/n),
\qquad 1\leq i,j\leq n,
\]
with all these variables independent. Define, coordinatewise,
\[
\phi(x)=\arctan x,\qquad
h_0^{(\ell)}=\phi(z_0^{(\ell)}),\qquad
z_0^{(2)}=W_0^{(2)}h_0^{(1)},\qquad
z_0^{(3)}=W_0^{(3)}h_0^{(2)}.
\]
All vectors here belong to \(\mathbb R^n\); \(\|\cdot\|\) is the ordinary Euclidean norm, and \(T\) denotes transpose. Set
\[
g(x)=\phi'(x)\phi(x)=\frac{\arctan x}{1+x^2},
\qquad
u_n^{(2)}=(W_0^{(3)})^T
\bigl[\phi'(z_0^{(3)})\odot\phi(z_0^{(3)})\bigr]
=(W_0^{(3)})^T g(z_0^{(3)}).
\]
Thus \(u_n^{(2)}\) is determined by the displayed canonical initialization.

Let \(G_1,G_2,G_3,G\) be independent \(N(0,1)\) population variables, and define
\[
\begin{aligned}
m_1&=\mathbb E[\phi(G_1)^2],
&Z^{(2)}&=\sqrt{m_1}\,G_2,\\
m_2&=\mathbb E[\phi(Z^{(2)})^2],
&Z^{(3)}&=\sqrt{m_2}\,G_3,\\
\beta&=\frac{\mathbb E[Z^{(3)}g(Z^{(3)})]}{m_2},
&\sigma^2&=\mathbb E[g(Z^{(3)})^2],\qquad
U^{(2)}=\beta\phi(Z^{(2)})+\sigma G,
\end{aligned}
\]
where \(\sigma\) is the positive square root. Then
\(m_1,m_2,\sigma^2>0\) and \(0<\beta\leq1\).

For every continuous \(F:\mathbb R^2\to\mathbb R\) satisfying
\[
|F(z,v)|\leq C_F(1+z^2+v^2)
\quad\text{for some finite }C_F,
\]
the joint empirical-average law is
\[
\frac1n\sum_{i=1}^n F(z_{0,i}^{(2)},u_{n,i}^{(2)})
\longrightarrow \mathbb E[F(Z^{(2)},U^{(2)})]
\quad\text{in probability and in }L^1.
\tag{1}
\]
In particular, with \([a]_+=\max(a,0)\),
\[
c_n=\frac1n\sum_{i=1}^n
\bigl[u_{n,i}^{(2)}\phi''(z_{0,i}^{(2)})\bigr]_+
\longrightarrow
c_*=\mathbb E\!\left[\bigl[U^{(2)}\phi''(Z^{(2)})\bigr]_+\right]>0
\quad\text{in probability and in }L^1.
\tag{2}
\]
Consequently \(\mathbb E c_n\to c_*\).

The proof first derives the exact conditional law after reuse of
\(W_0^{(3)}\), then removes its projection term in root mean square.
A coupling with independent population pairs gives empirical convergence.
Uniform fourth moments justify the unbounded tests and convergence of
expectations; an explicit conditional Gaussian event gives strict positivity.

## Proof

Write \(H=\pi/2\). The elementary bounds used below are
\[
|\phi(x)|\leq H,\quad |\phi(x)|\leq|x|,\quad
0<\phi'(x)=\frac1{1+x^2}\leq1,\quad
\phi''(x)=-\frac{2x}{(1+x^2)^2},\quad |\phi''(x)|\leq2,
\tag{3}
\]
and
\[
|g(x)|\leq H,\qquad |g(x)|\leq|x|,\qquad
0\leq xg(x)\leq x^2,\qquad |xg(x)|\leq H/2.
\tag{4}
\]
For the last bound use \(|x|/(1+x^2)\leq1/2\).
The function \(g\) vanishes exactly at zero, and \(xg(x)>0\) for \(x\ne0\).
Since a nondegenerate Gaussian has probability zero of being zero,
these facts successively give \(m_1>0\), \(m_2>0\),
\(\sigma^2>0\), and \(\mathbb E[Z^{(3)}g(Z^{(3)})]>0\).
All expectations are finite by (3)--(4).
Also \(\mathbb E[Z^{(3)}g(Z^{(3)})]\leq\mathbb E (Z^{(3)})^2=m_2\), proving
\(0<\beta\leq1\).

### Exact finite-dimensional conditioning

Define the empirical second moments
\[
m_{1,n}=\frac{\|h_0^{(1)}\|^2}{n},\qquad
m_{2,n}=\frac{\|h_0^{(2)}\|^2}{n}.
\]
Almost surely \(m_{1,n}>0\): its vanishing would require all
\(z_{0,i}^{(1)}=0\). Given the first layer, the rows of \(W_0^{(2)}\)
give independent coordinates \(z_{0,i}^{(2)}\sim N(0,m_{1,n})\).
Thus, conditionally on \(m_{1,n}>0\), the probability that \(h_0^{(2)}=0\)
is zero. In particular \(m_{2,n}>0\) almost surely.
Given the variables in the first two layers, the \(z_{0,j}^{(3)}\) are independent
\(N(0,m_{2,n})\). Hence \(z_0^{(3)}\ne0\) and \(\|g(z_0^{(3)})\|>0\) almost surely.
Both random variances lie in \([0,H^2]\).

For a fixed nonzero \(h_0^{(2)}\), define the orthogonal projection
\[
P_n^{(2)}=\frac{h_0^{(2)}(h_0^{(2)})^T}{\|h_0^{(2)}\|^2}.
\]
Writing \((W_0^{(3)})_{j,:}\) for row \(j\), the exact decomposition is
\[
(W_0^{(3)})_{j,:}^T
=\frac{h_0^{(2)}\,z_{0,j}^{(3)}}{\|h_0^{(2)}\|^2}
+(I-P_n^{(2)})(W_0^{(3)})_{j,:}^T,\qquad
z_{0,j}^{(3)}=(W_0^{(3)})_{j,:}h_0^{(2)}.
\]
Conditionally on \(h_0^{(2)}\), the scalar \(z_{0,j}^{(3)}\) and vector
\((I-P_n^{(2)})(W_0^{(3)})_{j,:}^T\) are jointly Gaussian,
and their cross covariance is
\[
\mathbb E\!\left[
(I-P_n^{(2)})(W_0^{(3)})_{j,:}^T z_{0,j}^{(3)}
\mid h_0^{(2)}\right]
=\frac1n(I-P_n^{(2)})h_0^{(2)}=0.
\]
They are therefore independent: the characteristic function of a centered
joint Gaussian with zero cross covariance factors into its two marginal
characteristic functions. The residual vectors for distinct rows are
independent, have covariance \((I-P_n^{(2)})/n\), and are independent of the
entire vector \(z_0^{(3)}\). Since \(W_0^{(3)}\) is independent of all lower-layer
variables, the same statements hold after additionally conditioning on
those variables.

Multiplying row \(j\) by \(g(z_{0,j}^{(3)})\) and summing proves that, conditionally
on the lower layers and \(z_0^{(3)}\),
\[
u_n^{(2)}\ \overset{\mathrm{law}}{=}
\beta_n h_0^{(2)}+\sigma_n(I-P_n^{(2)})\xi,\qquad
\beta_n=\frac{(z_0^{(3)})^Tg(z_0^{(3)})}{\|h_0^{(2)}\|^2},\qquad
\sigma_n^2=\frac{\|g(z_0^{(3)})\|^2}{n},
\tag{5}
\]
where \(\xi\sim N(0,I_n)\) can be chosen independent of the lower layers
and \(z_0^{(3)}\). Indeed, the conditional mean is \(\beta_n h_0^{(2)}\), and the
conditional covariance is
\[
\sum_{j=1}^n g(z_{0,j}^{(3)})^2\,\frac{I-P_n^{(2)}}{n}
=\sigma_n^2(I-P_n^{(2)}).
\]
The square root \(\sigma_n\) is nonnegative and is positive almost surely.
If \(h_0^{(2)}=0\), then \(z_0^{(3)}=0\), \(g(z_0^{(3)})=0\), and the original \(u_n^{(2)}=0\).
On this null event set \(\beta_n=0\) and \(P_n^{(2)}=0\);
then \(\sigma_n=0\) and (5) remains valid. These conventions resolve
every zero denominator in (5).

Equation (5) is a conditional-law representation of the original
matrix-derived vector. It does not change the initialization or introduce
an independent network output. In particular, it retains the correlation
created by using the same matrix in \(z_0^{(3)}=W_0^{(3)}h_0^{(2)}\) and
\(u_n^{(2)}=(W_0^{(3)})^Tg(z_0^{(3)})\).

### Random variances and coefficients

For independent identically distributed variables of finite variance \(v\),
their sample average has variance \(v/n\); Chebyshev's inequality therefore
gives convergence in probability to their mean. We use this fact also
conditionally, integrating the conditional variance bound.

Applied to the bounded first-layer variables it gives
\[
m_{1,n}\longrightarrow m_1
\quad\text{in }L^2\text{ and in probability}.
\tag{6}
\]
Let \(G'\sim N(0,1)\) be a dummy variable in expectations and define on
\([0,H^2]\)
\[
f(q)=\mathbb E[\phi(\sqrt q\,G')^2],\qquad
a(q)=\mathbb E[\sqrt q\,G' g(\sqrt q\,G')],\qquad
b(q)=\mathbb E[g(\sqrt q\,G')^2].
\]
Each function is continuous, including at zero: its integrand is
pointwise continuous in \(q\), and (3)--(4) bound the integrands
respectively by \(H^2,H/2,H^2\), so dominated convergence applies.
Conditionally on the first layer,
\[
\mathbb E[m_{2,n}\mid z_0^{(1)}]=f(m_{1,n}),\qquad
\mathbb E[(m_{2,n}-f(m_{1,n}))^2\mid z_0^{(1)}]\leq H^4/n.
\]
Continuity of \(f\), (6), and this variance bound give
\[
m_{2,n}\longrightarrow f(m_1)=m_2
\quad\text{in probability}.
\tag{7}
\]
For example, continuity at \(m_1\) says that sufficiently small
\(|m_{1,n}-m_1|\) makes \(|f(m_{1,n})-f(m_1)|\) arbitrarily small;
the complementary event has probability tending to zero by (6).

Set \(A_n=(z_0^{(3)})^Tg(z_0^{(3)})/n\). Conditionally on the lower layers, (4) gives
\[
\begin{aligned}
\mathbb E[A_n\mid z_0^{(1)},W_0^{(2)}]&=a(m_{2,n}),&
\mathbb E[(A_n-a(m_{2,n}))^2\mid z_0^{(1)},W_0^{(2)}]
&\leq H^2/(4n),\\
\mathbb E[\sigma_n^2\mid z_0^{(1)},W_0^{(2)}]&=b(m_{2,n}),&
\mathbb E[(\sigma_n^2-b(m_{2,n}))^2\mid z_0^{(1)},W_0^{(2)}]
&\leq H^4/n.
\end{aligned}
\]
Using (7) and continuity of \(a,b\), we obtain
\[
A_n\longrightarrow a(m_2)=\mathbb E[Z^{(3)}g(Z^{(3)})],\qquad
\sigma_n^2\longrightarrow b(m_2)=\sigma^2
\quad\text{in probability}.
\]
Since \(m_2>0\), the event \(m_{2,n}\geq m_2/2\) has probability tending
to one. Division on this event and continuity of the square root yield
\[
\beta_n=A_n/m_{2,n}\longrightarrow\beta,\qquad
\sigma_n\longrightarrow\sigma
\quad\text{in probability}.
\tag{8}
\]
The ratio at zero uses the convention in (5). No deterministic lower
bound on the finite random variances was assumed.

### Projection correction and joint empirical convergence

The successive forward conditional Gaussian laws and (5) permit the
following exact construction in distribution. Draw the first layer and
three mutually independent standard Gaussian vectors
\(\eta,\zeta,\xi\), independent also of the first layer, and set
\[
z_{0,i}^{(2)}=\sqrt{m_{1,n}}\,\eta_i,\qquad
h_0^{(2)}=\phi(z_0^{(2)}),\qquad
z_0^{(3)}=\sqrt{m_{2,n}}\,\zeta,\qquad
u_n^{(2)}=\beta_n h_0^{(2)}+\sigma_n(I-P_n^{(2)})\xi.
\tag{9}
\]
The coefficients and variances in (9) are computed from the vectors
already drawn, exactly as above. Successively conditioning on the first
layer, on \(z_0^{(2)}\), and on \(z_0^{(3)}\) shows that (9) has the original
joint law of \((z_0^{(1)},z_0^{(2)},z_0^{(3)},u_n^{(2)})\). This equality includes
all dependencies needed below; it does not assert independence of the
original coordinate pairs.

For the projection correction, independence of \(\xi\) and \((h_0^{(2)},z_0^{(3)})\) gives,
on \(h_0^{(2)}\ne0\),
\[
\mathbb E\left[\left.
\frac{\|\sigma_nP_n^{(2)}\xi\|^2}{n}\right|h_0^{(2)},z_0^{(3)}\right]
=\frac{\sigma_n^2}{n}
\mathbb E\left[\left.\frac{((h_0^{(2)})^T\xi)^2}{\|h_0^{(2)}\|^2}\right|h_0^{(2)},z_0^{(3)}\right]
=\frac{\sigma_n^2}{n}\leq\frac{H^2}{n}.
\tag{10}
\]
On \(h_0^{(2)}=0\) the left side is zero by the stated conventions.
Thus \(\|\sigma_nP_n^{(2)}\xi\|/\sqrt n\) tends to zero in \(L^2\) and in
probability. This also covers \(n=1\), when \(P_n^{(2)}=I\) for \(h_0^{(2)}\ne0\).

On the representation space define the comparison coordinates
\[
\bar z_i^{(2)}=\sqrt{m_1}\,\eta_i,\qquad
\bar u_i^{(2)}=\beta\phi(\bar z_i^{(2)})+\sigma\xi_i.
\]
These comparison pairs are independent and identically distributed with
law \((Z^{(2)},U^{(2)})\). Since
\[
\frac1n\sum_i|z_{0,i}^{(2)}-\bar z_i^{(2)}|^2
=(\sqrt{m_{1,n}}-\sqrt{m_1})^2\,\frac1n\sum_i\eta_i^2,
\tag{11}
\]
the left side tends to zero in probability by (6) and
\(n^{-1}\sum_i\eta_i^2\to1\). The latter convergence follows from
\(\mathbb E\eta_i^2=1\), \(\operatorname{Var}(\eta_i^2)=2\) and
the sample-average variance bound. The same reasoning gives
\(\|\xi\|/\sqrt n\to1\) in probability.

The bound \(\phi'\leq1\) makes \(\phi\) Lipschitz with constant one.
Subtracting the comparison vector from (9) and using the triangle
inequality consequently gives
\[
\begin{split}
\frac{\|u_n^{(2)}-\bar u^{(2)}\|}{\sqrt n}
&\leq |\beta_n-\beta|\sqrt{m_{2,n}}
+|\beta|\frac{\|z_0^{(2)}-\bar z^{(2)}\|}{\sqrt n}\\
&\quad+|\sigma_n-\sigma|\frac{\|\xi\|}{\sqrt n}
+\frac{\|\sigma_nP_n^{(2)}\xi\|}{\sqrt n}
\longrightarrow0
\quad\text{in probability},
\end{split}
\tag{12}
\]
by (8)--(11) and \(m_{2,n}\leq H^2\).
In particular,
\[
D_n^2:=\frac1n\sum_i
\left(|z_{0,i}^{(2)}-\bar z_i^{(2)}|^2+|u_{n,i}^{(2)}-\bar u_i^{(2)}|^2\right)
\longrightarrow0
\quad\text{in probability}.
\tag{13}
\]

If \(F\) is bounded and uniformly continuous, let
\(\omega_F(\delta)=\sup_{\|x-x'\|\leq\delta}|F(x)-F(x')|\),
using the ordinary Euclidean norm on \(\mathbb R^2\).
At most a fraction \(D_n^2/\delta^2\) of the paired points have
distance exceeding \(\delta>0\), so
\[
\left|\frac1n\sum_i F(z_{0,i}^{(2)},u_{n,i}^{(2)})
-\frac1n\sum_i F(\bar z_i^{(2)},\bar u_i^{(2)})\right|
\leq\omega_F(\delta)+2\|F\|_\infty D_n^2/\delta^2.
\tag{14}
\]
First choosing \(\delta\) so that \(\omega_F(\delta)\) is small and then
using (13) proves that this difference tends to zero in probability.
The comparison average converges to \(\mathbb E F(Z^{(2)},U^{(2)})\) by
the sample-average variance bound, since its summands are bounded and
independent. We next justify the larger test class in (1).

### Uniform moments, unbounded tests, and \(L^1\)

The following moment bounds are uniform over every \(n\geq1\).
Gaussian integration by parts gives
\(\mathbb E(G')^{2k}=(2k-1)\mathbb E(G')^{2k-2}\):
integrate \(x^{2k-1}x e^{-x^2/2}\), whose boundary term vanishes.
Thus \(\mathbb E(G')^4=3\) and \(\mathbb E(G')^8=105\).
The forward conditional law gives
\[
\mathbb E|z_{0,i}^{(2)}|^4=3\mathbb E m_{1,n}^2\leq3H^4.
\tag{15}
\]
On \(m_{2,n}>0\), (4) and (9) give
\[
0\leq\beta_n
\leq\frac{\|z_0^{(3)}\|^2}{nm_{2,n}}
=\frac1n\sum_j\zeta_j^2.
\]
Convexity of \(t\mapsto t^4\) on \([0,\infty)\) therefore yields
\[
\mathbb E\beta_n^4
\leq\mathbb E\left(\frac1n\sum_j\zeta_j^2\right)^4
\leq\frac1n\sum_j\mathbb E\zeta_j^8=105.
\tag{16}
\]
The null-event convention satisfies the same moment bound.
Conditionally on \(h_0^{(2)},z_0^{(3)}\), each coordinate
\(\sigma_n((I-P_n^{(2)})\xi)_i\) is a centered Gaussian of variance at most
\(\sigma_n^2\leq H^2\), and hence of fourth moment at most \(3H^4\).
Using \(|r+s|^4\leq8(|r|^4+|s|^4)\) in (5), together with
\(|h_{0,i}^{(2)}|\leq H\) and (16), proves
\[
\mathbb E|u_{n,i}^{(2)}|^4\leq8H^4\mathbb E\beta_n^4+24H^4
\leq864H^4.
\tag{17}
\]
This is a direct moment estimate for the reused Gaussian matrix;
it requires no independence between its original output coordinates.
The population variables likewise have finite fourth moments because
\(Z^{(2)}\) is Gaussian and
\(|U^{(2)}|\leq|\beta|H+\sigma|G|\).
Since \((z^2+v^2)^2\leq2(z^4+v^4)\), (15)--(17) in particular imply
\[
\sup_n\mathbb E\left[\frac1n\sum_i
\bigl((z_{0,i}^{(2)})^2+(u_{n,i}^{(2)})^2\bigr)^2\right]<\infty.
\tag{18}
\]

Now let \(F\) have the continuous, at most quadratic growth in (1).
For \(R\geq1\), choose a continuous function
\(\chi_R:\mathbb R^2\to[0,1]\) equal to one on the ball of radius \(R\)
and zero outside the ball of radius \(R+1\); for example
\(\chi_R(x)=\max(0,\min(1,R+1-\|x\|))\).
Then \(F_R=\chi_RF\) is continuous with compact support and is bounded
and uniformly continuous, so (14) applies. For \(r=(z^2+v^2)^{1/2}\),
\[
|F(z,v)-F_R(z,v)|
\leq C_F(1+r^2)\mathbf1_{\{r>R\}}
\leq \frac{2C_F}{R^2}r^4.
\tag{19}
\]
By (18), the expectation of the empirical average of (19) is bounded
by a constant times \(R^{-2}\), uniformly in \(n\).
The analogous population expectation has the same bound, because the
population fourth moment is finite. Markov's inequality therefore
makes the empirical truncation error small in probability uniformly
in \(n\). First taking \(n\to\infty\) for \(F_R\), and then
\(R\to\infty\) in these bounds, proves the probability convergence
in (1).

For completeness, write
\(X_n=n^{-1}\sum_iF(z_{0,i}^{(2)},u_{n,i}^{(2)})\) and
\(\mu=\mathbb E F(Z^{(2)},U^{(2)})\), which is finite by the population
moment bound. Jensen's inequality and (18) give
\[
\sup_n\mathbb E|X_n|^2
\leq C_F^2\sup_n\mathbb E\left[\frac1n\sum_i
\bigl(1+(z_{0,i}^{(2)})^2+(u_{n,i}^{(2)})^2\bigr)^2\right]<\infty.
\tag{20}
\]
Here \((1+r^2)^2\leq2(1+r^4)\). In particular the averages are
uniformly integrable, since
\(\mathbb E[|X_n|\mathbf1_{\{|X_n|>K\}}]\leq\mathbb E|X_n|^2/K\).
More explicitly, for every \(\varepsilon>0\), Cauchy--Schwarz gives
\[
\mathbb E|X_n-\mu|
\leq\varepsilon+
\bigl(\mathbb E|X_n-\mu|^2\bigr)^{1/2}
\mathbb P(|X_n-\mu|>\varepsilon)^{1/2}.
\]
The second moments are bounded by (20), and the probabilities tend
to zero. Taking a limit superior and then \(\varepsilon\downarrow0\)
proves \(L^1\) convergence in (1). All probability and expectation
statements transfer from (9) to the canonical network by equality
of the joint laws for each \(n\).

### The curvature average and strict positivity

The test
\[
F(z,v)=[v\phi''(z)]_+
\]
is continuous. By (3),
\(0\leq F(z,v)\leq2|v|\leq1+v^2\), so it is in the class of (1).
This proves both convergences in (2) and finiteness of \(c_*\).

To prove strict positivity explicitly, on \(1\leq z\leq2\) we have
\[
-\phi''(z)=\frac{2z}{(1+z^2)^2}\geq\frac{2}{25}.
\]
Consider the event
\[
1\leq Z^{(2)}\leq2,\qquad
G\leq-\frac{|\beta|H+1}{\sigma}.
\tag{21}
\]
On (21), \(U^{(2)}=\beta\phi(Z^{(2)})+\sigma G\leq-1\), so
\([U^{(2)}\phi''(Z^{(2)})]_+\geq2/25\).
Conditionally on any \(Z^{(2)}=z\in[1,2]\), the second event in (21)
has the same strictly positive probability, since \(G\) is independent
of \(Z^{(2)}\) and \(\sigma>0\).
Writing \(\Phi\) for the standard Gaussian distribution function gives
\[
c_*\geq\frac{2}{25}
\left[\Phi\!\left(\frac2{\sqrt{m_1}}\right)
-\Phi\!\left(\frac1{\sqrt{m_1}}\right)\right]
\Phi\!\left(-\frac{|\beta|H+1}{\sigma}\right)>0.
\tag{22}
\]
The bracket is positive because \(m_1>0\) and the Gaussian density
is strictly positive on every finite interval; the last factor is
positive because its argument is finite.

This proves the claimed initial hidden-layer empirical law and curvature
limit. The Gaussian representation was exact at finite \(n\); only the
explicit projection correction and empirical averages were passed to
their limits. No central limit approximation or independence assertion
for the original finite coordinate pairs is involved. \(\square\)
