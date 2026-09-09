## V. Initialization geometry: fixed mixtures and calibrated depth limits

This part compares initialized sample geometry for three explicitly different
activations in the same dense Gaussian network. It proves sharp joint
separation/mixture/depth orders for the literal odd arctangent mixture,
contraction for the literal convex-offset family, and a sequential
width-first, depth-second correlation limit for a calibrated activation
that depends on depth. Every assertion in this part concerns initialization.
There is no training horizon, optimizer approximation, continuation theorem,
or assumption about tails along a trained trajectory.

The proof first identifies the initialized finite-width kernel and establishes
the Gaussian identities needed for all three families. Cubic tensor features
then give a lower bound for odd mixtures; a planar triple and a bound on the
curvature of the composed correlation map give a matching upper bound. The
same Gaussian identities prove convex-offset contraction and identify the
calibrated correlation recursion and its depth limit.

### V.M. Model, observables, and the meaning of conditioning

There are three normalized inputs: \(m=3\), \(x_a\in\mathbb R^d\),

\[
 u_a=x_a/\sqrt d,\qquad \|u_a\|_2=1,\qquad
 G_{ab}=u_a^Tu_b,\qquad 1\le a,b\le3.
 \tag{V.M.1}
\]

Only realizable input Grams are considered, and singular Grams are allowed.
The hidden depth is \(L\ge1\) and the common hidden width is \(n\). In
canonical storage,

\[
 z_a^{(1)}=W^{(1)}x_a/\sqrt d,\qquad
 z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)}\ (\ell\ge2),\qquad
 h_a^{(\ell)}=\phi(z_a^{(\ell)}),\qquad
 f_{n,a}=\frac{(W^{(L+1)})^Th_a^{(L)}}n.
 \tag{V.M.2}
\]

All initialized entries and blocks are independent:

\[
 W^{(1)}_{ij}\sim N(0,1),\qquad
 W^{(\ell)}_{ij}\sim N(0,1/n)\ (2\le\ell\le L),\qquad
 W^{(L+1)}_i\sim N(0,n^{-2}).
 \tag{V.M.3}
\]

The alternative storage \(V^{(1)}=W^{(1)}/\sqrt d\) has entries
\(N(0,1/d)\) and gives exactly the same preactivations. The raw metric,
with unit mobility multipliers, is

\[
 \frac{\|dW^{(1)}\|_F^2}{n}
 +\sum_{\ell=2}^L\|dW^{(\ell)}\|_F^2
 +\frac{\|dW^{(L+1)}\|_2^2}{n}.
 \tag{V.M.4}
\]

Here \(dW^{(\ell)}\) denotes a parameter increment. The first term equals
\(d\|dV^{(1)}\|_F^2/n\) in alternative storage. The kernel below is the
Gram of predictor gradients in this metric; it contains no loss-dependent
factor. With the common loss \(\mathcal L_n=3^{-1}\sum_a(f_{n,a}-y_a)^2\),
the loss-gradient factor would be \(2/3\). Labels have no role in any
initialization statement here.

Write \(\xi\sim N(0,1)\) for a scalar Gaussian, to distinguish it from
the input Gram \(G\). For each fixed activation and depth set

\[
 Q_0=G,\quad q_0=1,\qquad
 Z^{(\ell)}\sim N(0,Q_{\ell-1}),\qquad
 H_a^{(\ell)}=\phi(Z_a^{(\ell)}),\qquad
 (Q_\ell)_{ab}=\mathbb E_\ell[H_a^{(\ell)}H_b^{(\ell)}],\qquad
 q_\ell=(Q_\ell)_{aa}.
 \tag{V.M.5}
\]

Each \(Z^{(\ell)},H^{(\ell)}\) lives on its own Gaussian population
space \(\Omega_\ell\); \(\mathbb E_\ell\) contracts within that space.
These marginal laws suffice here: (V.M.5) does not specify joint trained
actions or joint fields across layers. The common diagonal \(q_\ell\)
is independent of the sample and the off-diagonal input geometry.
The feature Gram \(Q_\ell\) is **uncentered**. In particular it is not
the centered covariance of \(H^{(\ell)}\) in the offset case. It is the
covariance of the next centered Gaussian preactivation. In this part
\(Q_\ell\) always means the raw feature Gram, not the gain-normalized
feature Gram used for estimates in Part III.

For \(q_\ell>0\), define the variance-normalized sample Gram and three
conditioning quantities by

\[
 C_\ell=Q_\ell/q_\ell,\qquad
 \lambda_{\min}(Q_\ell),\qquad
 \lambda_{\min}(C_\ell),\qquad
 \frac{\lambda_{\min}(Q_\ell)}{\lambda_{\max}(Q_\ell)}.
 \tag{V.M.6}
\]

The first eigenvalue is an absolute floor; the second removes the common
feature scale; the ratio is the reciprocal spectral condition number.
Since \(C_\ell\succeq0\) and has trace three,

\[
 1\le\lambda_{\max}(C_\ell)\le3,\qquad
 \frac{\lambda_{\min}(C_\ell)}3
 \le\frac{\lambda_{\min}(Q_\ell)}{\lambda_{\max}(Q_\ell)}
 \le\lambda_{\min}(C_\ell).
 \tag{V.M.7}
\]

Thus the two scale-free quantities are equivalent up to a factor three.
For an offset activation, \(C_\ell\) is not a centered Pearson correlation
matrix of the features.

For a continuous at-most-linear function \(g\) and \(q>0\), define its
absolute scalar nonaffinity and its fraction of feature second moment by

\[
 \mathcal R_g(q)=\inf_{\alpha,\beta\in\mathbb R}
       \mathbb E[(g(\sqrt q\,\xi)-\alpha-\beta\sqrt q\,\xi)^2],
 \qquad
 \frac{\mathcal R_g(q)}{\mathbb E g(\sqrt q\,\xi)^2}.
 \tag{V.M.8}
\]

The latter is defined when its denominator is positive, as it is for
all three families below, and is our convention for relative nonaffinity.
Its denominator is uncentered, matching \(Q_\ell\). Orthogonal projection
onto \(\operatorname{span}\{1,\xi\}\) gives the attained minimum

\[
 \mathcal R_g(q)=\mathbb E g(\sqrt q\,\xi)^2
  -(\mathbb E g(\sqrt q\,\xi))^2
  -(\mathbb E[\xi g(\sqrt q\,\xi)])^2.
 \tag{V.M.9}
\]

These scalar quantities and sample-Gram conditioning measure different
properties, as the proofs below demonstrate.

### V.F. Contained initialization and Gaussian foundations

#### V.F.1. Fixed-depth finite-width identification

For any fixed globally Lipschitz activation, the empirical feature Grams
at all layers converge jointly in probability to (V.M.5), with \(L,d\)
and the data fixed before \(n\to\infty\). All three families below have
this regularity, including the calibrated family with \(L\) held fixed.

At layer one the row triples are independent copies of \(N(0,G)\).
Their activated products have finite variance because
\(|\phi(z)|\le |\phi(0)|+D|z|\) for a finite Lipschitz constant \(D\).
Chebyshev's inequality proves convergence of their averages. Given the
preceding feature vectors, each row of the next independent Gaussian
matrix produces a centered Gaussian triple with covariance

\[
 \widehat Q_{\ell-1,ab}=
       (h_a^{(\ell-1)})^Th_b^{(\ell-1)}/n,
 \tag{V.F.1}
\]

independently across rows. On an event where the preceding diagonals are
at most \(M\), Gaussian fourth moments and the linear growth bound give
a uniform finite bound \(A_{M,\phi}\) on the variance of each activated
product. Conditional Chebyshev bounds its averaging error probability
at tolerance \(v>0\) by \(A_{M,\phi}/(nv^2)\). Induction makes the
bounded-diagonal event have probability tending to one for some fixed
\(M\) larger than the limiting diagonals.

The conditional expected product is continuous in the covariance, including
at singular matrices. To check the only matrix fact required, if positive
semidefinite matrices \(B_j\to B\), their positive square roots are bounded.
Every convergent subsequence of these roots has a positive semidefinite
limit \(A\) satisfying \(A^2=B\). The spectral decomposition gives a unique
positive semidefinite square root of \(B\), so all subsequential limits
agree and \(B_j^{1/2}\to B^{1/2}\). Coupling Gaussian vectors as
\(B_j^{1/2}\zeta,B^{1/2}\zeta\), with \(\zeta\sim N(0,I_3)\), gives
\(L^2\) convergence of their activated coordinates by Lipschitzness.
Cauchy--Schwarz gives convergence of the products' expectations. This
finishes the finite induction and the joint convergence of all entries.

For the initialized raw kernel assume in addition that \(\phi\) is
\(C^1\) with bounded derivative, as in all three families below.
Retain the residual-free backward fields

\[
 \delta_a^{(L)}=W^{(L+1)}\odot\phi'(z_a^{(L)}),\qquad
 \delta_a^{(\ell)}=\phi'(z_a^{(\ell)})\odot
             (W^{(\ell+1)})^T\delta_a^{(\ell+1)}.
 \tag{V.F.2}
\]

Direct differentiation of (V.M.2) and inversion of (V.M.4) give

\[
 \begin{aligned}
 K_{n,ab}^{(1)}&=G_{ab}\frac{(\delta_a^{(1)})^T\delta_b^{(1)}}n,\\
 K_{n,ab}^{(\ell)}&=
   \frac{(\delta_a^{(\ell)})^T\delta_b^{(\ell)}}n
   \frac{(h_a^{(\ell-1)})^Th_b^{(\ell-1)}}n,
                       &&2\le\ell\le L,\\
 K_{n,ab}^{(L+1)}&=\frac{(h_a^{(L)})^Th_b^{(L)}}n.
 \end{aligned}
 \tag{V.F.3}
\]

For example the first Euclidean derivative is
\(\delta_a^{(1)}x_a^T/(n\sqrt d)\); its metric inverse multiplies by
\(n\). The middle derivative is
\(\delta_a^{(\ell)}(h_a^{(\ell-1)})^T/n\), and the readout derivative
is \(h_a^{(L)}/n\), multiplied by \(n\) by the readout metric inverse.
Taking the corresponding pairings gives exactly (V.F.3).

Each initialized square hidden matrix has operator norm at most ten with
probability tending to one. Here is an elementary bound. A maximal
\(1/4\)-separated family on the Euclidean unit sphere is a \(1/4\)-net
of cardinality at most \(9^n\): its disjoint radius-\(1/8\) balls lie
in the radius-\(9/8\) ball. Approximating both vectors in a bilinear
supremum gives
\(\|W\|_{\rm op}\le2\max_{u,v\text{ in the net}}|u^TWv|\).
For each pair, \(u^TWv\sim N(0,1/n)\). The moment generating function
\(\mathbb E e^{t u^TWv}=e^{t^2/(2n)}\), optimized in \(t\), gives

\[
 \mathbb P(\|W\|_{\rm op}>10)
 \le2\,9^{2n}e^{-25n/2}\longrightarrow0.
 \tag{V.F.4}
\]

A finite union covers all hidden matrices. Moreover
\(\mathbb E\|W^{(L+1)}\|_2^2/n=n^{-2}\). If
\(D=\|\phi'\|_\infty<\infty\), backward induction bounds

\[
 \frac{\|\delta_a^{(\ell)}\|_2}{\sqrt n}
 \le D^{L-\ell+1}
       \prod_{j=\ell+1}^L\|W^{(j)}\|_{\rm op}
       \frac{\|W^{(L+1)}\|_2}{\sqrt n}
 =O_{\mathbb P}(n^{-1})
 \tag{V.F.5}
\]

at fixed depth. Feature RMS values are bounded in probability by the Gram
induction. Thus all initial hidden kernel blocks vanish in probability,
the readout block converges to \(Q_L\), and

\[
 \mathcal K_n(0):=\sum_{\ell=1}^{L+1}K_n^{(\ell)}(0)
       \longrightarrow Q_L\quad\hbox{in probability}.
 \tag{V.F.6}
\]

Also \(|f_{n,a}|\le(\|W^{(L+1)}\|_2/\sqrt n)
(\|h_a^{(L)}\|_2/\sqrt n)\to0\). The zero limiting readout makes
the population hidden backward fields zero, consistently with (V.F.6).
No estimate here is a width approximation uniform in growing \(L\).

#### V.F.2. Gaussian expansions, including endpoints

Define the probabilists' Hermite polynomials by

\[
 e^{tx-t^2/2}=\sum_{j\ge0}\mathsf H_j(x)t^j/j!,\qquad
 \mathsf h_j=\mathsf H_j/\sqrt{j!}.
 \tag{V.F.7}
\]

Gaussian integration of the product of two generating functions gives
\(\mathbb E[e^{s\xi-s^2/2}e^{t\xi-t^2/2}]=e^{st}\).
Comparing coefficients proves orthonormality of the \(\mathsf h_j\).
We include completeness to make the subsequent series identities contained.
If \(u\in L^2(N(0,1))\) is orthogonal to all polynomials, the generating
series at \(t=i\eta\) converges in Gaussian \(L^2\), because its squared
coefficient norms sum to \(e^{\eta^2}\). Its pointwise entire-function
sum identifies that limit. Pairing with \(u\) shows that the Fourier
transform of the integrable density
\(v(x)=u(x)e^{-x^2/2}/\sqrt{2\pi}\) is zero. Integrability follows
from Cauchy--Schwarz.

For completeness, the uniqueness fact just used can be verified directly.
Integration by parts in the Gaussian density gives its characteristic
function \(J'(t)=-tJ(t)\), \(J(0)=1\), hence \(J(t)=e^{-t^2/2}\).
The same Gaussian integral after scaling gives the Fourier integral
representation of the Gaussian density of variance \(s>0\).
Insert it in the convolution \(v*\gamma_s\). Fubini applies since
\(\|v\|_1\int e^{-s\eta^2/2}\,d\eta<\infty\); the zero Fourier
transform then gives \(v*\gamma_s=0\). These convolutions converge
to \(v\) in \(L^1\): write their difference as the integral of
\(v(\cdot-y)-v\), use translation continuity in \(L^1\), and split
the Gaussian mass at a fixed \(|y|\). Translation continuity holds
first for bounded interval step functions by lengths of interval
symmetric differences, and then for \(L^1\) functions by their density.
Thus \(v=0\), proving completeness.

For standard jointly Gaussian \(X,Y\) with correlation
\(\rho\in[-1,1]\), the joint Gaussian generating function is
\(\mathbb E[e^{sX-s^2/2}e^{tY-t^2/2}]=e^{\rho st}\).
Comparing coefficients gives

\[
 \mathbb E[\mathsf h_j(X)\mathsf h_k(Y)]
       =\mathbf1_{j=k}\rho^j.
 \tag{V.F.8}
\]

This includes \(Y=X\) and \(Y=-X\). Polynomial approximation and
Cauchy--Schwarz extend (V.F.8) to arbitrary Gaussian \(L^2\) functions.
Consequently, if \(f=\sum_j a_j\mathsf h_j\),

\[
 \mathbb E[f(X)f(Y)]=\sum_{j\ge0}a_j^2\rho^j.
 \tag{V.F.9}
\]

The sum is absolutely convergent even at both endpoints by Parseval.
If \(f\in C^2\) has at most linear growth and bounded first two
derivatives, Gaussian integration by parts also gives the first identity
below for \(j\ge1\) and the second for \(j\ge2\):

\[
 \langle f',\mathsf h_{j-1}\rangle=\sqrt j\,a_j,
 \qquad
 \langle f'',\mathsf h_{j-2}\rangle=\sqrt{j(j-1)}\,a_j.
 \tag{V.F.10}
\]

Indeed differentiating (V.F.7) gives
\(x\mathsf H_{j-1}-\mathsf H'_{j-1}=\mathsf H_j\); integrating
the derivative against the Gaussian density proves the first identity
with a zero boundary term, and repeating proves the second. Parseval
therefore identifies the sums \(\sum j a_j^2=\mathbb E f'(\xi)^2\)
and \(\sum j(j-1)a_j^2=\mathbb E f''(\xi)^2\). In particular the
corresponding differentiated covariance series converge uniformly on
\([-1,1]\). At \(\rho=1\), their values are the two unsigned Parseval
sums above. At \(\rho=-1\), the first and second derivatives are instead
\(\sum_{j\ge1}(-1)^{j-1}j a_j^2\) and
\(\sum_{j\ge2}(-1)^{j-2}j(j-1)a_j^2\), respectively.
These endpoint derivatives are one-sided on the correlation interval.

A useful consequence, valid for any correlation including negative ones,
is the following Gaussian contraction. Let \(X,Y\) be centered jointly
Gaussian, both with variance \(\sigma^2>0\) and correlation
\(\rho\in[-1,1]\). For an activation with the preceding regularity
and growth assumptions, put \(f(x)=\phi(\sigma x)\). Since
\(1-\rho^j=(1-\rho)\sum_{k=0}^{j-1}\rho^k\le j(1-\rho)\),

\[
 \begin{aligned}
 \mathbb E[(\phi(X)-\phi(Y))^2]
 &=2\sum_{j\ge1}a_j^2(1-\rho^j)\\
 &\le2(1-\rho)\sigma^2\mathbb E\phi'(\sigma\xi)^2
 =\mathbb E\phi'(\sigma\xi)^2\,\mathbb E(X-Y)^2.
 \end{aligned}
 \tag{V.F.11}
\]

The series argument establishes this also at singular covariance endpoints.

#### V.F.3. Cubic lifting of three separated samples

For any three-by-three unit-diagonal positive semidefinite matrix \(C\)
with \(|C_{ab}|\le1-\delta\) for every \(a\ne b\),
\(0<\delta\le1\), define
\(s_\delta=\delta(2-\delta)\). Then

\[
 C^{\circ3}\succeq\frac{s_\delta^2}{3}I_3.
 \tag{V.F.12}
\]

Here \(C^{\circ j}\) means entrywise power. Choose unit representatives
\(v_a\) realizing \(C\). For \(a\ne b\) set

\[
 v_{ab}=\frac{v_a-C_{ab}v_b}{\sqrt{1-C_{ab}^2}},\qquad
 T_a=v_a\otimes v_{ab}\otimes v_{ac},
              \quad\{a,b,c\}=\{1,2,3\}.
 \tag{V.F.13}
\]

These are ordinary finite-dimensional tensor products. Their product
inner product makes \(T_a\) a unit vector orthogonal to
\(v_b^{\otimes3},v_c^{\otimes3}\), with

\[
 \langle T_a,v_a^{\otimes3}\rangle
   =\sqrt{1-C_{ab}^2}\sqrt{1-C_{ac}^2}\ge s_\delta.
\]

For \(T=\sum_a b_av_a^{\otimes3}\), this implies
\(s_\delta^2\sum_a b_a^2\le\sum_a|\langle T_a,T\rangle|^2
\le3\|T\|^2\). Since \(\|T\|^2=b^TC^{\circ3}b\), (V.F.12)
follows without invertibility of \(C\). More generally every nonnegative integer
power \(C^{\circ j}\) is positive semidefinite, being the Gram of
the tensor powers \(v_a^{\otimes j}\); degree zero is the constant
Gram \(\mathbf1\mathbf1^T\).

### V.O. The literal odd mixture: sharp joint orders

Use exactly

\[
 \phi_\theta(z)=(1-\theta)z+\theta\arctan z,
                 \qquad0<\theta\le1.
 \tag{V.O.1}
\]

There is no offset, gain, or variance calibration. For \(d\ge2\), let
\(\Lambda_L^{\rm abs}(\theta,\delta;d)\) and
\(\Lambda_L^{\rm norm}(\theta,\delta;d)\) be the infima of
\(\lambda_{\min}(Q_L)\) and \(\lambda_{\min}(C_L)\), respectively,
over unit triples in \(\mathbb R^d\) satisfying the strict inequalities

\[
 -1+\delta<G_{ab}<1-\delta\qquad(a\ne b).
 \tag{V.O.2}
\]

**Theorem V.O.1.** For \(L\ge1\), \(0<\theta\le1\),
\(0<\delta\le1/4\), and every \(d\ge2\),

\[
 \begin{aligned}
 \frac{e^{-80/3}}{73728}
   \frac{\delta^2\theta^2 L}{(1+\theta L)^2}
 &\le\Lambda_L^{\rm abs}
 \le11520e^{128/3}
   \frac{\delta^2\theta^2 L}{(1+\theta L)^2},\\
 \frac{e^{-80/3}}{9216}
   \frac{\delta^2\theta^2 L}{1+\theta L}
 &\le\Lambda_L^{\rm norm}
 \le2880e^{128/3}
   \frac{\delta^2\theta^2 L}{1+\theta L}.
 \end{aligned}
 \tag{V.O.3}
\]

The constants are explicit sufficient comparison constants, not optimal
constants. The powers and joint orders are sharp. The lower bounds below
also show \(Q_L\succ0\) for every realizable separated triple with
\(0<\delta<1\) at each finite depth, even when \(G\) is singular.

#### V.O.1. Variance decay and summable nonlinear weights

Put \(u(z)=z-\arctan z\). For \(0<q\le1\), define

\[
 \mu(q)=\mathbb E(1+q\xi^2)^{-1},\quad
 c(q)=1-\theta+\theta\mu(q),\quad
 q_+=\mathbb E\phi_\theta(\sqrt q\,\xi)^2.
 \tag{V.O.4}
\]

Integration by parts gives
\(\mathbb E[\sqrt q\,\xi\arctan(\sqrt q\,\xi)]=q\mu(q)\).
Thus \(c(q)\) is the coefficient of projection of the activation onto
its preactivation. Jensen's inequality gives
\(c(q)\ge1-\theta+\theta/(1+q)\ge1/2\), and hence
\(q_+\ge qc(q)^2\ge q/4\). Also \(0<q_+<q\), since
\(0<|\phi_\theta(z)|<|z|\) for \(z\ne0\).

The decrement is

\[
 D(q)=q-q_+=2\theta\mathbb E[Zu(Z)]-\theta^2\mathbb E u(Z)^2,
                   \qquad Z=\sqrt q\,\xi.
\]

The inequalities \(0\le u(z)^2\le zu(z)\) and
\(\mathbb E[Zu(Z)]=q(1-\mu(q))\) imply

\[
 \theta(2-\theta)q(1-\mu(q))\le D(q)\le2\theta q(1-\mu(q)).
\]

Cauchy--Schwarz applied to
\(|\xi|/\sqrt{1+q\xi^2}\) and \(|\xi|\sqrt{1+q\xi^2}\)
gives \(\mathbb E[\xi^2/(1+q\xi^2)]\ge1/(1+3q)\).
Consequently

\[
 \frac{q}{1+3q}\le1-\mu(q)\le q,\qquad
 \frac\theta4q^2\le D(q)\le2\theta q^2,\qquad
 \frac\theta4\le q_+^{-1}-q^{-1}\le8\theta.
 \tag{V.O.5}
\]

The last bounds use \(q/4\le q_+\le q\). Iteration from \(q_0=1\)
and summation of \(D(q_k)=q_k-q_{k+1}\) yield

\[
 \frac1{1+8\theta\ell}\le q_\ell\le\frac1{1+\theta\ell/4},
 \tag{V.O.6}
\]

\[
 \frac{L}{1+8\theta L}
 \le\sum_{k=0}^{L-1}q_k^2
 \le\min\{L,4/\theta\}
 \le\frac{5L}{1+\theta L}.
 \tag{V.O.7}
\]

For the lower sum bound integrate \((1+8\theta x)^{-2}\) on
\([0,L]\) and compare it to its left endpoint sum. For the final
upper bound set \(x=\theta L\); \(\min\{1,4/x\}\le5/(1+x)\)
holds separately on \(x\le4\) and \(x\ge4\).

Expand \(f_q(x)=\phi_\theta(\sqrt qx)\) using V.F.2. Oddness gives
only odd degrees. The normalized correlation map is

\[
 K_q(\rho)=\frac{\mathbb E[f_q(X)f_q(Y)]}{q_+}
   =\sum_{j\ {\rm odd}}w_j(q)\rho^j,\qquad
 w_j(q)=\frac{a_j(q)^2}{q_+}\ge0,\quad\sum_jw_j(q)=1.
 \tag{V.O.8}
\]

In particular \(|K_q(\rho)|\le|\rho|\), and

\[
 (C_\ell)_{ab}=K_{q_{\ell-1}}((C_{\ell-1})_{ab}),\qquad
 |(C_\ell)_{ab}|\le|G_{ab}|.
 \tag{V.O.9}
\]

The constant Hermite coefficient is zero. The linear coefficient is
\(a_1(q)=\sqrt q\,c(q)\). Let \(R(q)=q_+-qc(q)^2\ge0\).
Since \(|u(z)|\le|z|^3/3\), testing projection with \(z\) gives

\[
 R(q)\le\frac53\theta^2q^3,\qquad
 -\log w_1(q)=\log\left(1+\frac{R(q)}{qc(q)^2}\right)
                 \le\frac{20}3\theta^2q^2.
 \tag{V.O.10}
\]

Here \(\mathbb E\xi^6=15\), obtained by successive integration by parts
from \(\mathbb E\xi^{2k}=(2k-1)\mathbb E\xi^{2k-2}\).
By (V.O.7), the sum of \(\theta^2q_k^2\) over any finite set of
layers is at most \(4\theta\le4\). Every product of linear weights
over consecutive layers is therefore at least

\[
 p_*:=e^{-80/3}.
 \tag{V.O.11}
\]

#### V.O.2. Cubic injection and the lower bounds

The cubic coefficient of arctangent is

\[
 b_3(q):=\mathbb E[\arctan(\sqrt q\,\xi)\mathsf h_3(\xi)]
 =-\sqrt{\frac23}\,q^{3/2}
           \mathbb E\frac{\xi^2}{(1+q\xi^2)^2}.
 \tag{V.O.12}
\]

Indeed first integrate \(\mathsf H_3\) by parts, leaving
\(\sqrt q(\xi^2-1)/(1+q\xi^2)\). Then use
\(\mathbb E[(\xi^2-1)r(\xi)]=\mathbb E[\xi r'(\xi)]\)
with \(r(x)=(1+qx^2)^{-1}\), and divide by \(\sqrt{3!}\).
All boundary terms vanish by Gaussian decay.

The measure with density \(\xi^2\) relative to Gaussian probability
is a probability measure under which \(\mathbb E\xi^2=3\).
Jensen's inequality for \((1+qt)^{-2}\) gives

\[
 \mathbb E\frac{\xi^2}{(1+q\xi^2)^2}
       \ge(1+3q)^{-2}\ge1/16,\qquad
 b_3(q)^2\ge q^3/384,\qquad
 w_3(q)\ge\theta^2q^2/384.
 \tag{V.O.13}
\]

The last inequality uses \(q_+\le q\). Applying the tensor Gram
identity and cubic bound V.F.3 to (V.O.8)--(V.O.9) proves

\[
 C_\ell\succeq w_1(q_{\ell-1})C_{\ell-1}
               +\frac{s_\delta^2}{3}w_3(q_{\ell-1})I_3.
\]

Iterate this inequality. Each injected scalar multiple of the identity
is multiplied by a subsequent product of linear weights bounded below
by \(p_*\); the propagated \(C_0\succeq0\) can be discarded. Thus

\[
 \lambda_{\min}(C_L)
 \ge\frac{p_*s_\delta^2\theta^2}{1152}
          \sum_{k=0}^{L-1}q_k^2
 \ge\frac{p_*s_\delta^2\theta^2L}{1152(1+8\theta L)},
 \tag{V.O.14}
\]

\[
 \lambda_{\min}(Q_L)
 \ge\frac{p_*s_\delta^2\theta^2L}{1152(1+8\theta L)^2}.
 \tag{V.O.15}
\]

These bounds require only realizability and \(|G_{ab}|\le1-\delta\)
for every \(a\ne b\), with \(0<\delta\le1\). Using \(s_\delta\ge\delta\) and
\(1+8\theta L\le8(1+\theta L)\) gives both lower constants in
(V.O.3).

#### V.O.3. Composed curvature and a matching strict planar triple

Define \(F_0(\rho)=\rho\) and
\(F_{k+1}=K_{q_k}\circ F_k\). Then

\[
 (C_L)_{ab}=F_L(G_{ab}),\qquad
 F_L(\rho)=\sum_{j\ {\rm odd}}p_{j,L}\rho^j,
       \quad p_{j,L}\ge0,\quad\sum_jp_{j,L}=1.
 \tag{V.O.16}
\]

Composition preserves these properties: expansion and rearrangement
use nonnegative terms for \(0\le\rho<1\), and passage to one uses
monotone convergence. The coefficient sum one then gives absolute
convergence on \([-1,1]\) and the same formula for negative arguments.

By (V.F.10),

\[
 d_k:=K_{q_k}'(1)
  =\frac{q_k\mathbb E\phi_\theta'(\sqrt{q_k}\xi)^2}{q_{k+1}},
 \qquad
 b_k:=K_{q_k}''(1)
  =\frac{q_k^2\mathbb E\phi_\theta''(\sqrt{q_k}\xi)^2}{q_{k+1}}.
 \tag{V.O.17}
\]

Since \(\phi_\theta''(z)=-2\theta z/(1+z^2)^2\) and
\(q_{k+1}\ge q_k/4\),

\[
 0\le b_k\le16\theta^2q_k^2,\qquad
 1\le d_k,\qquad d_k-1\le b_k/3.
 \tag{V.O.18}
\]

For the last inequality, use \(j-1\le j(j-1)/3\) for every odd
\(j\ge3\) in the nonnegative series; the degree-one term contributes
zero. Hence \(\sum b_k\le64\) and \(\sum(d_k-1)\le64/3\).
Writing \(A_k=F_k'(1)\), \(B_k=F_k''(1)\), the endpoint chain rule gives

\[
 A_{k+1}=d_kA_k,\quad B_{k+1}=b_kA_k^2+d_kB_k,
 \quad A_0=1,\ B_0=0,
 \qquad
 B_L=A_L\sum_{k=0}^{L-1}\frac{b_k}{d_k}A_k.
\]

The endpoint derivatives exist continuously by V.F.2 and finite
composition. Since \(A_k\le e^{64/3}\), (V.O.7) now gives

\[
 F_L''(1)\le16e^{128/3}\theta^2\sum_{k=0}^{L-1}q_k^2
       \le80e^{128/3}\frac{\theta^2L}{1+\theta L}.
 \tag{V.O.19}
\]

For a matching example take \(c=1-2\delta\in[1/2,1)\) and the
ordered planar triple

\[
 u_1=(c,\sqrt{1-c^2}),\quad u_2=(1,0),\quad
 u_3=(c,-\sqrt{1-c^2}).
 \tag{V.O.20}
\]

The off-diagonal Grams are \(c,c,r\), where
\(r=2c^2-1=1-8\delta+8\delta^2\). The upper and lower strict
separation margins for \(c\) are \(\delta\) and \(2-3\delta\).
For \(r\) they are

\[
 \delta(7-8\delta)>0,\qquad
 2-9\delta+8\delta^2=(1-4\delta)(2-2\delta)+\delta>0.
\]

This verifies admissibility even at \(\delta=1/4\). Embed the same
triple by zero coordinates for any \(d>2\).
The vector \(v=(1,-2c,1)^T\) satisfies \(Gv=0\) and
\(\|v\|_2^2=2+4c^2\ge3\). At each odd integer degree define

\[
 E_j(c)=v^TG^{\circ j}v
       =2+4c^2+2(2c^2-1)^j-8c^{j+1}\ge0.
 \tag{V.O.21}
\]

Nonnegativity is the tensor Gram property. For \(j=1\) this is zero.
For \(j\ge3\), \(E_j(1)=E_j'(1)=0\), and direct differentiation gives

\[
 E_j''(c)=8+8j(2c^2-1)^{j-1}
   +32j(j-1)c^2(2c^2-1)^{j-2}-8j(j+1)c^{j-1}.
\]

On \([1/2,1]\), its absolute value is at most
\(40j^2-16j+8\le54j(j-1)\). The final inequality is equivalent
to \(14j^2-38j-8\ge0\), which holds at \(j=3\) and increases
thereafter. Taylor's integral remainder gives
\(0\le E_j(c)\le27j(j-1)(1-c)^2\).
Using (V.O.16), its nonnegative coefficients, and the Rayleigh quotient,

\[
 \lambda_{\min}(C_L)
 \le\frac{\sum_jp_{j,L}E_j(c)}{2+4c^2}
 \le9(1-c)^2F_L''(1)
 =36\delta^2F_L''(1).
 \tag{V.O.22}
\]

Equation (V.O.19) proves the normalized upper bound in (V.O.3).
Multiplying by \(q_L\le4/(1+\theta L)\) proves its absolute upper
bound. This example matches all three parameters simultaneously.

#### V.O.4. Scalar nonaffinity and the depth regimes

For \(0<q\le1\), the cubic coefficient and projection onto the linear
function give the useful joint bounds

\[
 \frac{\theta^2q^3}{384}\le\mathcal R_{\phi_\theta}(q)
 \le\frac53\theta^2q^3,\qquad
 \frac{\theta^2q^2}{384}
 \le\frac{\mathcal R_{\phi_\theta}(q)}{q_+}
 \le\frac{20}3\theta^2q^2.
 \tag{V.O.23}
\]

For the first lower bound use the squared degree-three coefficient,
which remains after affine projection. The first upper bound is
(V.O.10); the relative bounds use \(q/4\le q_+\le q\).
Together with (V.O.6) they show, uniformly in \(\theta,\ell\),
absolute layer nonaffinity of order
\(\theta^2/(1+\theta(\ell-1))^3\) and relative nonaffinity of order
\(\theta^2/(1+\theta(\ell-1))^2\).

For precise large-depth equivalents fix \(\theta>0\). Dominated
convergence gives \(1-\mu(q)\sim q\) as \(q\downarrow0\), while
\(\mathbb E u(\sqrt q\xi)^2\le(5/3)q^3\). Therefore
\(D(q)/q^2\to2\theta\), \(q_+/q\to1\), and
\(q_{\ell+1}^{-1}-q_\ell^{-1}\to2\theta\). Averaging these
increments proves

\[
 q_\ell\sim\frac1{2\theta\ell}.
 \tag{V.O.24}
\]

The exact identity \((1+t^2)^{-1}=1-t^2+t^4/(1+t^2)\), integrated
between zero and \(z\), yields
\(|\arctan z-z+z^3/3|\le|z|^5/5\). Its Gaussian \(L^2\) remainder
is \(O(q^{5/2})\). Removing the projection onto \(1,\xi\) leaves
\(-q^{3/2}\mathsf H_3(\xi)/3+O_{L^2}(q^{5/2})\).
Since \(\mathbb E\mathsf H_3(\xi)^2=6\),

\[
 \mathcal R_{\arctan}(q)\sim\frac23q^3,\qquad
 \mathcal R_{\phi_\theta}(q)=\theta^2\mathcal R_{\arctan}(q).
 \tag{V.O.25}
\]

The exact equality absorbs the linear part into the regression slope.
At layer \(\ell\) the preactivation variance is \(q_{\ell-1}\), so
for fixed \(\theta>0\),

\[
 \mathcal R_{\phi_\theta}(q_{\ell-1})\sim
       \frac1{12\theta\ell^3},\qquad
 \frac{\mathcal R_{\phi_\theta}(q_{\ell-1})}{q_\ell}
       \sim\frac1{6\ell^2}.
 \tag{V.O.26}
\]

Thus scalar nonaffinity is positive at every finite layer but both its
absolute and relative versions tend to zero with depth. In contrast,
for fixed \(\theta>0\) and any realizable fixed separation \(\delta>0\),
normalized sample conditioning has a positive lower bound uniform over
\(L\ge1\). Indeed use (V.O.14) and
\(L/(1+8\theta L)\ge1/(1+8\theta)\).
Absolute sample conditioning cannot have such a floor, since
\(\lambda_{\min}(Q_L)\le\operatorname{tr}(Q_L)/3=q_L\to0\).

The sharp joint orders can also be expressed as follows:

| Regime | Worst absolute sample floor | Worst normalized sample floor |
|---|---|---|
| \(\theta L\le1\) | \(\asymp\delta^2\theta^2L\) | \(\asymp\delta^2\theta^2L\) |
| \(\theta L\ge1\) | \(\asymp\delta^2/L\) | \(\asymp\delta^2\theta\) |

These comparisons have universal constants and the parameter range of
(V.O.3). The equivalents in (V.O.24)--(V.O.26), unlike those comparisons,
hold with \(\theta\) fixed as depth tends to infinity.

Antipodal exclusion in (V.O.2) has mathematical content. If
\(u_b=-u_a\), oddness gives opposite features at every layer and a
singular sample Gram. At \(\theta=0\), \(\phi_0(z)=z\) and \(Q_L=G\)
for every \(L\). The equilateral planar triple, whose off-diagonal
entries are \(-1/2\), is strictly admissible for \(0<\delta<1/2\),
but \(G\mathbf1=0\). More generally any bias-free linear network has
\(\sum_a f_a=0\) on this triple, since \(\sum_a x_a=0\); it cannot
represent labels \((1,1,1)\). This is a representational obstruction
for the affine reference. It is not an obstruction to a positive-mixture
training theorem and supplies no such theorem.

### V.C. Literal convex offsets: contraction without loss of scalar nonaffinity

Fix \(0<\varepsilon<1/2\) and a bounded nonconstant
\(\psi\in C^2(\mathbb R)\) with
\(\|\psi\|_\infty,\|\psi'\|_\infty,\|\psi''\|_\infty\le1\). Use exactly

\[
 \phi_\varepsilon(z)=(1-\varepsilon)(1+z)+\varepsilon\psi(z),
 \qquad b_\varepsilon=1-2\varepsilon>0.
 \tag{V.C.1}
\]

The symbol \(b_\varepsilon\) is a scalar lower bound, not the sample
count \(m=3\). Neither a gain nor a normalization of the matrix
initialization is included.

**Theorem V.C.1.** There is a constant
\(\kappa=\kappa(\varepsilon,\psi)\in(0,1)\), independent of depth and
the input Gram, such that for every pair \(a\ne b\) and every \(L\ge1\),

\[
 \begin{aligned}
 D_{L,ab}&:=\mathbb E_L(H_a^{(L)}-H_b^{(L)})^2
       \le2(1-G_{ab})\kappa^{2L},\\
 \lambda_{\min}(Q_L)&\le(1-G_{ab})\kappa^{2L},\\
 \lambda_{\min}(C_L)&\le
       \frac{1-G_{ab}}{b_\varepsilon^2}\kappa^{2L},\\
 \frac{\lambda_{\min}(Q_L)}{\lambda_{\max}(Q_L)}
       &\le\frac{1-G_{ab}}{3b_\varepsilon^2}\kappa^{2L}.
 \end{aligned}
 \tag{V.C.2}
\]

These bounds hold for every realizable normalized triple, in particular
for every strictly separated triple. For each fixed
\((\varepsilon,\psi)\), both absolute and relative scalar nonaffinity
at initialization nevertheless have positive lower bounds uniform
over all layers.

**Proof.** Put \(\sigma_\ell=\sqrt{q_{\ell-1}}\), so
\(\sigma_1=1\) and
\(\sigma_{\ell+1}=\|\phi_\varepsilon(\sigma_\ell\xi)\|_{L^2}\).
The mean satisfies
\(\mathbb E\phi_\varepsilon(\sigma\xi)
=1-\varepsilon+\varepsilon\mathbb E\psi(\sigma\xi)\ge b_\varepsilon\).
Minkowski's inequality gives
\(\sigma_{\ell+1}\le(1-\varepsilon)\sigma_\ell+1\).
The interval \([0,1/\varepsilon]\) is preserved by this last upper
recursion and contains \(\sigma_1\). The lower bound from the mean,
and the initial value one, prove

\[
 b_\varepsilon\le\sigma_\ell\le1/\varepsilon,\qquad
 b_\varepsilon^2\le q_\ell\le\varepsilon^{-2}
                    \quad(\ell\ge1).
 \tag{V.C.3}
\]

The derivative belongs to \([b_\varepsilon,1]\). Define

\[
 \kappa^2=\max_{b_\varepsilon\le\sigma\le1/\varepsilon}
           \mathbb E\phi_\varepsilon'(\sigma\xi)^2.
 \tag{V.C.4}
\]

The expectation is continuous in \(\sigma\) by dominated convergence.
For any \(\sigma>0\), an expectation equal to one would force
\(\phi_\varepsilon'(\sigma\xi)=1\) almost surely, since the derivative
lies in the positive interval \([b_\varepsilon,1]\).
Its continuity and the strictly positive Gaussian density would force
\(\phi_\varepsilon'=1\) everywhere. Equation (V.C.1) would then imply
\(\psi'=1\) everywhere, contradicting boundedness of \(\psi\).
Compactness of the interval in (V.C.4) proves
\(b_\varepsilon\le\kappa<1\).

Apply (V.F.11) with variance \(\sigma_\ell^2\). In the recursion,
the preactivation squared difference at layer \(\ell\) is
\(2(q_{\ell-1}-Q_{\ell-1,ab})=D_{\ell-1,ab}\), with
\(D_{0,ab}=2(1-G_{ab})\). Hence
\(D_{\ell,ab}\le\kappa^2D_{\ell-1,ab}\).
Iteration proves the first inequality in (V.C.2). Testing \(Q_L\)
against \((e_a-e_b)/\sqrt2\) gives the second, and division by
\(q_L\ge b_\varepsilon^2\) gives the third. Finally

\[
 \lambda_{\max}(Q_L)\ge
 \mathbb E_L\left(\frac{H_1^{(L)}+H_2^{(L)}+H_3^{(L)}}{\sqrt3}\right)^2
 \ge3b_\varepsilon^2
 \tag{V.C.5}
\]

by the lower bound on each mean, which proves the fourth.
In fact \(C_{L,ab}=1-D_{L,ab}/(2q_L)\to1\) for every pair, so
\(C_L\to\mathbf1\mathbf1^T\). This is a loss of distinctions among
samples, with feature scale bounded away from zero.

To prove the scalar statement, (V.M.9) shows that
\(\mathcal R_\psi(\sigma^2)>0\) for every \(\sigma>0\).
Otherwise \(\psi(\sigma\xi)=\alpha+\beta\sigma\xi\) almost surely.
By continuity and Gaussian full support this equality would hold at
every real argument. Boundedness forces \(\beta=0\), contradicting
nonconstancy. The expression (V.M.9) is continuous in \(\sigma>0\):
boundedness of \(\psi\) dominates its first two expectations, and
\(\|\psi\|_\infty|\xi|\) dominates the last linear pairing.
It follows that

\[
 r_{\varepsilon,\psi}:=
 \min_{b_\varepsilon\le\sigma\le1/\varepsilon}
                     \mathcal R_\psi(\sigma^2)>0.
 \tag{V.C.6}
\]

Absorbing the affine term of (V.C.1) into the regression coefficients
gives the exact equality
\(\mathcal R_{\phi_\varepsilon}(q)=\varepsilon^2\mathcal R_\psi(q)\).
Thus, using (V.C.3),

\[
 \mathcal R_{\phi_\varepsilon}(q_{\ell-1})
       \ge\varepsilon^2r_{\varepsilon,\psi},\qquad
 \frac{\mathcal R_{\phi_\varepsilon}(q_{\ell-1})}{q_\ell}
       \ge\varepsilon^4r_{\varepsilon,\psi}>0.
 \tag{V.C.7}
\]

These constants are for the fixed shape and mixture, not uniform over
the whole allowed shape class or as \(\varepsilon\downarrow0\).
The distinction is necessary: scaling any allowed nonconstant shape
by a positive factor tending to zero scales its squared regression
residual by that factor squared. This completes the proof.

For an explicit contraction rate, take
\(\varepsilon=1/4\), \(\psi(z)=\arctan(z)/4\). The shape norms are
\(\pi/8,1/4,3\sqrt3/32\), respectively. For the last norm, maximize
\(x/[2(1+x^2)^2]\) at \(x=1/\sqrt3\). Thus all three bounds are below
one, and the literal activation is

\[
 \phi(z)=\tfrac34(1+z)+\tfrac1{16}\arctan z,\qquad
 \tfrac34\le\phi'(z)\le\tfrac{13}{16}.
 \tag{V.C.8}
\]

Its pointwise Lipschitz constant already proves (V.C.2) with
\(\kappa=13/16\), without a strictness argument for Gaussian derivative
averages. This is a concrete fixed activation with exponentially
collapsing normalized sample conditioning.

### V.D. A separate calibrated near-identity family

The next activation depends on \(L\) and is neither (V.O.1) nor (V.C.1).
It retains the dense architecture, matrix initialization, and metric
(V.M.2)--(V.M.4), but makes a deliberate scalar calibration inside the
activation. It therefore supplies a comparison family, not a result
for either literal fixed-mixture question.

Define fixed constants and a fixed smooth bounded odd shape by

\[
 c_*=\frac{e^{3/2}}2,\qquad
 w(z)=c_*\sin(2z)-\sin z,\qquad
 v_*=\mathbb E w(\xi)^2,\qquad \chi(z)=w(z)/\sqrt{v_*}.
 \tag{V.D.1}
\]

The derivative \(w'(0)=2c_*-1>0\); thus \(w\) is not zero and Gaussian
full support gives \(v_*>0\). All derivatives of \(\chi\) are bounded
fixed constants; they are not required to be bounded by one.
For a fixed total depth parameter \(\tau>0\), set

\[
 \gamma_L=\sqrt{\tau/L},\qquad
 \phi_L(z)=\frac{z+\gamma_L\chi(z)}{\sqrt{1+\gamma_L^2}}.
 \tag{V.D.2}
\]

At a given \(L\), this same \(\phi_L\) is used in all \(L\) layers.
The subscript does not designate different activations at successive
layers of one network.

#### V.D.1. Exact cancellation, unit variance, and finite-depth geometry

Differentiating the Gaussian characteristic function established in V.F.2
gives \(\mathbb E[\xi\sin(t\xi)]=t e^{-t^2/2}\). Therefore

\[
 \mathbb E\chi(\xi)=0,\qquad
 \mathbb E[\xi\chi(\xi)]
   =\frac{2c_*e^{-2}-e^{-1/2}}{\sqrt{v_*}}=0,\qquad
 \mathbb E\chi(\xi)^2=1.
 \tag{V.D.3}
\]

In particular \(\mathbb E\phi_L(\xi)^2=1\), so every \(q_k=1\).
For a standard Gaussian pair of correlation \(\rho\), representing
\(Y=\rho X+\sqrt{1-\rho^2}\,\xi'\) with an independent Gaussian
\(\xi'\) shows \(\mathbb E[Y\chi(X)]=0\); the other cross term is
zero as well. This representation also handles both endpoints. Hence

\[
 T_\gamma(\rho):=\mathbb E[\phi_L(X)\phi_L(Y)]
       =\frac{\rho+\gamma^2K(\rho)}{1+\gamma^2},
 \qquad K(\rho)=\mathbb E[\chi(X)\chi(Y)],\quad\gamma=\gamma_L.
 \tag{V.D.4}
\]

The sine product identity and Gaussian characteristic function give
\(\mathbb E[\sin(aX)\sin(bY)]
=e^{-(a^2+b^2)/2}\sinh(ab\rho)\). Substitution in (V.D.1) gives

\[
 \begin{aligned}
 N_*&=\sinh1-\sinh2+\tfrac14\sinh4=e\,v_*>0,\\
 K(\rho)&=\frac{\sinh\rho-\sinh(2\rho)+\tfrac14\sinh(4\rho)}{N_*}
      =\sum_{\substack{j\ge3\\j\ {\rm odd}}}p_j\rho^j,\\
 p_j&=\frac{(2^{j-1}-1)^2}{N_*j!},\qquad
 p_3=\frac3{2N_*}>0,\qquad\sum_jp_j=1.
 \end{aligned}
 \tag{V.D.5}
\]

Indeed the odd coefficient numerator is
\(1-2^j+4^j/4=(2^{j-1}-1)^2\); the degree-one coefficient vanishes.
The series is absolutely convergent on every bounded interval, and its
sum at one equals \(\mathbb E\chi(\xi)^2=1\).
In particular

\[
 0\le K(\rho)\le\rho^3\quad(0\le\rho\le1),\qquad
 |T_\gamma(\rho)|\le|\rho|\quad(|\rho|\le1).
 \tag{V.D.6}
\]

Suppose now \(|G_{ab}|\le1-\delta\) for every \(a\ne b\),
\(0<\delta\le1\), for a realizable triple. Every \(Q_k=C_k\) remains a unit-diagonal Gram
with the same absolute separation, by (V.D.4)--(V.D.6).
Entrywise application of \(K\), denoted \(K[C]\), satisfies

\[
 K[C]\succeq p_3 C^{\circ3}\succeq\mu_\delta I_3,\qquad
 \mu_\delta=\frac{p_3\delta^2(2-\delta)^2}{3},
 \tag{V.D.7}
\]

by the tensor identities in V.F.3. With \(b=(1+\tau/L)^{-1}\),
the exact recursion is \(Q_{k+1}=bQ_k+(1-b)K[Q_k]\), so induction gives

\[
 Q_k\succeq b^kG+(1-b^k)\mu_\delta I_3.
 \tag{V.D.8}
\]

In particular

\[
 \lambda_{\min}(Q_L)=\lambda_{\min}(C_L)
 \ge\mu_\delta[1-(1+\tau/L)^{-L}]
 \ge\mu_\delta\frac{\tau}{1+\tau}.
 \tag{V.D.9}
\]

The last step is the binomial inequality
\((1+\tau/L)^L\ge1+\tau\). The lower bound is uniform in finite
depth at fixed \(\tau,\delta\); the shape and \(\tau\) need not
depend on \(\delta\). Absolute and normalized conditioning coincide
because the diagonal is exactly one.

#### V.D.2. The sequential correlation limit and its proof

Fix an initial correlation \(\rho_0\in[-1,1]\). Let
\(a_L=\tau/L\). At each fixed depth the population iteration is

\[
 \rho_{k+1}=\rho_k+\frac{a_L}{1+a_L}
                      [K(\rho_k)-\rho_k],\qquad0\le k<L.
 \tag{V.D.10}
\]

Let \(s\in[0,\tau]\) denote an auxiliary depth coordinate, not physical
training time \(t\). The linear interpolation at \(s=k\tau/L\) of
(V.D.10) converges uniformly to the unique solution

\[
 \frac{d\rho}{ds}=K(\rho)-\rho,\qquad \rho(0)=\rho_0.
 \tag{V.D.11}
\]

Here is a direct existence and error proof. Put \(F(\rho)=K(\rho)-\rho\),
\(D=1+\max_{[-1,1]}|K'|\), and \(B=2\). Then \(|F|\le B\) and
\(F\) is \(D\)-Lipschitz on this interval. Extend it to the real line
by \(F(\max\{-1,\min\{1,x\}\})\), preserving these bounds. On an
interval of length \(h\) with \(Dh<1\), the integral map
\(u\mapsto\rho_0+\int_0^\cdot F(u(r))\,dr\) contracts the supremum
distance of continuous paths by \(Dh\). Its iterates are Cauchy,
because successive distances form a geometric bound, and completeness
of the continuous-path space gives a unique fixed point. Repeating
on successive intervals gives a global solution of the extended
equation and uniqueness. Since \(F(\pm1)=0\), uniqueness at a first
endpoint contact prevents a solution from crossing either endpoint.
Thus the solution stays in \([-1,1]\), proving (V.D.11) in its stated
domain. The iteration stays in that interval as a convex combination
of \(\rho_k\) and \(K(\rho_k)\).

The integral increment over a step \(a_L\), started at \(x=\rho(s)\),
differs from \(a_LF(x)\) by at most
\[
 \int_0^{a_L}D|\rho(s+r)-\rho(s)|\,dr
       \le DBa_L^2/2.
\]
Also \(0\le a_L-a_L/(1+a_L)\le a_L^2\). If
\(e_k=|\rho_k-\rho(ka_L)|\), subtraction of the increments gives

\[
 e_{k+1}\le(1+Da_L)e_k+B(1+D/2)a_L^2,\qquad e_0=0.
\]

Summing the geometric bound, using \(La_L=\tau\), proves

\[
 \max_{0\le k\le L}e_k
 \le\frac{B(1+D/2)\tau^2e^{D\tau}}{L}.
 \tag{V.D.12}
\]

At intermediate points, interpolate the two endpoint errors and use
\(|\rho(s)-\rho(s')|\le B|s-s'|\). This adds at most \(B\tau/L\)
and proves the claimed uniform convergence. The constants are uniform
over \(\rho_0\in[-1,1]\).

Applying this to each input-Gram entry gives a matrix \(Q(s)\) with
diagonal one. It is positive semidefinite for every \(s\), because
the interpolated \(Q_k\)'s are convex combinations of positive
semidefinite matrices and converge entrywise to it. Write
\(\widehat Q_{n,L}=((h_a^{(L)})^Th_b^{(L)}/n)_{a,b=1}^3\)
for the finite-width initialized top feature Gram. In particular

\[
 \lim_{L\to\infty}\ \lim_{n\to\infty}\widehat Q_{n,L}
       =Q(\tau),\qquad
 \lambda_{\min}(Q(\tau))\ge\mu_\delta(1-e^{-\tau}).
 \tag{V.D.13}
\]

The inner limit is convergence in probability with the entire
activation \(\phi_L\) and finite \(L\) fixed. The outer limit is
deterministic. The lower bound follows from (V.D.9) and
\((1+\tau/L)^{-L}\to e^{-\tau}\), which in turn follows by integrating
\((1+x)^{-1}\) to obtain \(\log(1+x)=x+O(x^2)\) near zero.
The same sequential initialized limit applies to the total raw kernel
by (V.F.6). No rate in (V.D.12) controls the finite-width error.

For a nonlinear geometric witness take the equilateral planar triple.
Its three off-diagonal entries initially equal \(-1/2\), and
\(G\mathbf1=0\). By oddness all equal \(-r(s)\), where
\[
 r'=K(r)-r,\qquad r(0)=1/2,\qquad -r\le r'\le r^3-r.
\]
Apply the inequalities up to the first putative zero of \(r\).
The first gives \(r(s)\ge e^{-s}/2>0\), by differentiating
\(e^sr(s)\), and therefore excludes that zero. Meanwhile (V.D.6) makes \(r\) nonincreasing and at most
\(1/2\). For \(u=r^{-2}\), the upper differential inequality yields
\(u'\ge2(u-1)\). Integrating gives \(u(s)\ge1+3e^{2s}\), hence

\[
 \lambda_{\min}(Q(s))=1-2r(s)
       \ge1-\frac2{\sqrt{1+3e^{2s}}}>0\qquad(s>0).
 \tag{V.D.14}
\]

The other two eigenvalues are \(1+r(s)\). A scalar multiple of the
singular input Gram cannot produce this positive smallest eigenvalue.

#### V.D.3. Per-layer nonaffinity and local scalar checks

Let \(B_\chi=\|\chi\|_\infty\), \(M_\chi=\|\chi'\|_\infty\).
Since \(0\le1-(1+\gamma^2)^{-1/2}\le\gamma^2/2\),

\[
 \|\phi_L'-1\|_\infty\le\gamma_LM_\chi+\gamma_L^2/2,\qquad
 \sup_z\frac{|\phi_L(z)-z|}{1+|z|}
       \le\gamma_LB_\chi+\gamma_L^2/2,\qquad
 \|\phi_L''\|_\infty\le\gamma_L\|\chi''\|_\infty.
 \tag{V.D.15}
\]

Thus the derivatives approach those of the identity, and the values
converge locally uniformly, with the stated weighted global bound.
For each finite \(L\), the unweighted supremum
\(\sup_z|\phi_L(z)-z|\) is infinite: its nonzero linear term at
infinity cannot be canceled by the bounded shape.
Orthogonality (V.D.3) also gives the exact absolute and relative
nonaffinity at every initialized layer:

\[
 \mathcal R_{\phi_L}(1)
 =\frac{\gamma_L^2}{1+\gamma_L^2}
 =\frac{\tau}{L+\tau}
 =\frac{\mathcal R_{\phi_L}(1)}{\mathbb E\phi_L(\xi)^2}.
 \tag{V.D.16}
\]

In particular the depth-uniform geometric floor in (V.D.9) coexists
with scalar nonaffinity tending to zero in every layer of this family.

The scalar variance calibration is locally attracting for sufficiently
large \(L\). To check precisely what this means, hold
\(\gamma=\gamma_L>0\) fixed and define, for \(q\) near one,

\[
 V_\gamma(q)=\mathbb E\phi_L(\sqrt q\,\xi)^2
   =\frac{q+2\gamma q a(q)+\gamma^2 b(q)}{1+\gamma^2},
 \quad a(q)=\mathbb E\chi'(\sqrt q\,\xi),\quad
 b(q)=\mathbb E\chi(\sqrt q\,\xi)^2.
 \tag{V.D.17}
\]

The cross term follows by one Gaussian integration by parts. The
trigonometric formula gives
\[
 a(q)=\frac{2c_*e^{-2q}-e^{-q/2}}{\sqrt{v_*}},
 \quad a(1)=0,\quad a'(1)=-\frac{3e^{-1/2}}{2\sqrt{v_*}}.
\]
Boundedness of \(\chi,\chi'\), and the integrable factor \(|\xi|\),
justify differentiating \(b(q)\) near one. Thus \(b'(1)\) is finite,
\(V_\gamma(1)=1\), and
\[
 V_\gamma'(1)=1-\frac{3e^{-1/2}}{\sqrt{v_*}}\gamma+O(\gamma^2).
 \tag{V.D.18}
\]
For sufficiently small positive \(\gamma\) this derivative has
absolute value less than one. Continuity of the derivative gives a
neighborhood of one with a Lipschitz constant less than one; the mean
value theorem then shows iterates starting sufficiently near one stay
there and converge to one. This is local scalar stability, without
any assertion on accumulated finite-width variance errors.

Finally integration by parts gives
\(\mathbb E\chi'(\xi)=\mathbb E[\xi\chi(\xi)]=0\).
For \(M_2=\mathbb E\chi'(\xi)^2<\infty\),

\[
 \mathbb E\phi_L'(\xi)^2
     =\frac{1+\gamma_L^2M_2}{1+\gamma_L^2},\qquad
 [\mathbb E\phi_L'(\xi)^2]^L
     \le (1+\tau M_2/L)^L\le e^{\tau M_2}.
 \tag{V.D.19}
\]

The last inequality follows from \(\log(1+x)\le x\).
This is a product of scalar Gaussian moments, not a norm estimate
for the network Jacobian or for any trained backward field.

### V.S. Comparison and exact scope

The following conclusions concern the width-limit initialized Grams.
The sharp odd-mixture orders have the range
\(0<\delta\le1/4\); the calibrated bound holds for every realizable
triple with \(|G_{ab}|\le1-\delta\) for every \(a\ne b\),
\(0<\delta\le1\).

| Activation, with its parameters fixed as specified | Absolute sample conditioning across depth | Variance-normalized sample conditioning | Scalar nonaffinity across depth |
|---|---|---|---|
| Literal odd mixture, fixed \(\theta>0\) | Sharp infimum \(\asymp\delta^2\theta^2L/(1+\theta L)^2\); tends to zero | Sharp infimum \(\asymp\delta^2\theta^2L/(1+\theta L)\); positive floor at fixed \(\theta,\delta\) | Absolute \(\sim1/(12\theta\ell^3)\), relative \(\sim1/(6\ell^2)\) at layer \(\ell\) |
| Literal convex offset, fixed \(\varepsilon,\psi\) | At most \((1-G_{ab})\kappa^{2L}\) | At most \((1-G_{ab})\kappa^{2L}/b_\varepsilon^2\); tends to rank one | Both have positive floors for the fixed \(\varepsilon,\psi\) |
| Calibrated \(\phi_L\), fixed \(\tau,\chi\) | At least \(\mu_\delta\tau/(1+\tau)\), uniformly in \(L\) | Identical to absolute conditioning because \(q_L=1\) | Both equal \(\tau/(L+\tau)\) at every layer |

These statements distinguish a numerical bound uniform over depth from
an assertion valid at each separately fixed depth. For example,
failure of a depth-uniform kernel floor for either literal mixture
does not refute the possibility of one positive mixture parameter
giving a qualitative trained theorem at every finite depth with
depth-dependent constants. Conversely, initialized positive definiteness
at every finite depth proves no such trained theorem.

For \(a>e>0\) and a shape \(\psi\) satisfying the assumptions of V.C,
consider the gain-based activation \(g(z)=a(1+z)+e\psi(z)\).
Setting \(\varepsilon=e/(a+e)\in(0,1/2)\) gives
\(g/(a+e)=(1-\varepsilon)(1+z)+\varepsilon\psi(z)\).
If \(a+e=1\), this division is the identity. Otherwise it changes even
the first Gram: its diagonal is positive because
\(\mathbb E g(\xi)\ge a-e>0\), and it is multiplied by \((a+e)^{-2}\).
In general, a scalar activation change cannot be accounted for by merely
rescaling the final kernel. To display where the scale re-enters, replace
a general \(\phi\) by \(\widetilde\phi=\alpha\phi\),
\(\alpha>0\). The first Gram is \(\widetilde Q_1=\alpha^2Q_1\),
whereas at layer two, with \(Z\sim N(0,Q_1)\), it is
\(\widetilde Q_2=\alpha^2\mathbb E[\phi(\alpha Z)\phi(\alpha Z)^T]\).
For the gain activation \(g\), a nontrivial argument scaling has no scalar
homogeneity identity: if \(g(\alpha z)=c g(z)\) for every \(z\), then
\(g(0)\ge a-e>0\) gives \(c=1\), and \(g(z)/z\to a\) as
\(z\to+\infty\) gives \(\alpha=1\). Thus homogeneity cannot remove
the changed inner argument for \(\alpha\ne1\).

Even a positive absolute scalar margin for a gain-based activation
would not be a relative margin. This can be seen within initialization
without invoking any dynamics from Part III. Suppose \(a-e>1\),
\(0<e\le1\), and \(\psi\) obeys the bounds in V.C.
Affine projection and Gaussian integration by parts give, at variance
\(q>0\),
\[
 \mathcal R_{a(1+\cdot)+e\psi}(q)=e^2\mathcal R_\psi(q)\le e^2,\qquad
 \mathbb E[(a(1+\sqrt q\,\xi)+e\psi(\sqrt q\,\xi))^2]
       \ge q(a+e\mathbb E\psi'(\sqrt q\,\xi))^2
       \ge q(a-e)^2.
\]
The lower bound is the squared linear projection coefficient, and
the upper residual bound tests the zero affine fit for \(\psi\).
Iteration from \(q_0=1\) gives \(q_\ell\ge(a-e)^{2\ell}\).
Thus the relative nonaffinity at layer \(\ell\) is at most
\(e^2/(a-e)^{2\ell}\), regardless of whether an absolute margin
has a positive depth-uniform lower bound for the selected shape.

All finite-width results proved in V.F hold with the activation, data,
and finite depth fixed. V.D then takes a deterministic depth limit
after that width limit, along its explicitly depth-dependent activation
family. No result asserts convergence for \(L=L(n)\to\infty\),
an interchange of limits, or a limit at a positive physical training
time. None identifies a canonical trained population flow, controls
forward/reverse response histories or incoming-field tails along
training, proves cap removal or continuation, establishes GF/raw-GD
path or velocity convergence, or proves persistent trained nonaffinity,
feature motion, or fitting. The Gaussian recursion and its cancellation
identities are justified by fresh independent Gaussian initialization;
they are not recursions for trained non-Gaussian laws.
