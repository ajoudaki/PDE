# Independent alternative route: sample count versus the initial Gram gap

This is a prompt-only, independent theoretical investigation. Its inputs are the
network and assumptions supplied in the assignment. No scientific repository
sources, other agents' findings, or numerical experiments were used. The route
was frozen before exchange of substantive results with peers.

## Conclusion and scope

The proposed analytic-kernel route is valid under a quantitative analytic tail
bound, with a sample-count bound of order
\(\log(1/\gamma)^{d-1}\). Such a tail bound does **not** follow from the assigned
activation assumptions. In fact, one fixed, bounded, infinitely differentiable
activation, with every derivative bounded, produces a Gaussian initialized
network for which

\[
\lambda_{\min}(Q_0)\ge
\frac{c_L}{m}\exp\{-2\lceil\log_2m\rceil^2\}
\]

with arbitrarily high probability at sufficiently large finite width. Here
\(c_L>0\) depends only on the fixed depth and activations. Consequently no
universal implication
\(m\le C[\log(C/\gamma)]^p\), for fixed \(C,p\), follows from the stated
assumptions, even when \(d=2\) and the initialized hidden operator norms are
bounded by a numerical constant.

This is a proof-route obstruction, not a counterexample to global fitting or to
a sharper small-label theorem. It also does not rule out a subpolynomial bound
with a slower, activation-dependent rate. No improved global fitting theorem
is claimed here.

## 1. Exact network and the question tested

There are \(m\) unit inputs \(v_a\in\mathbb R^d\), labels \(y_a\), fixed depth
\(L\ge2\), and width \(n\). With \(A\in\mathbb R^{n\times d}\),
\(W^{(\ell)}\in\mathbb R^{n\times n}\), and \(w\in\mathbb R^n\), the forward
pass is

\[
z_a^{(1)}=Av_a,\qquad h_a^{(1)}=\phi_1(z_a^{(1)}),\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),\qquad
f_a=\frac1n w^\top h_a^{(L)}.
\]

The activations act coordinatewise. Initialization has independent standard
normal entries in \(A_0\), independent \(N(0,1/n)\) entries in the hidden
matrices, and \(w_0=0\). Write

\[
H_0=[h_{1,0}^{(L)},\ldots,h_{m,0}^{(L)}],\qquad
Q_0=\frac1nH_0^\top H_0,\qquad
Y=\left(\frac1m\sum_a y_a^2\right)^{1/2}.
\]

The assigned flow is gradient flow of
\(\mathcal L=m^{-1}\sum_a(y_a-f_a)^2\), with mobility \(n\) for \(A,w\) and
mobility \(1\) for each \(W^{(\ell)}\). The present route tests whether a
sufficient condition of the form \(Y\le c\gamma/m\), with
\(\lambda_{\min}(Q_0)\ge\gamma>0\), can be expressed using only a
polylogarithmic loss beyond \(\gamma\) by exploiting fixed input dimension.
It concerns initialization only and makes no concentration assumption along
training.

## 2. A complete conditional analytic-kernel argument

Let \(Q\) be any random positive semidefinite \(m\times m\) matrix satisfying

\[
\mathbb E Q_{ab}=\kappa(v_a^\top v_b),\qquad
\kappa(t)=\sum_{k=0}^\infty a_k t^k,\qquad a_k\ge0,
\qquad \sum_{k>p}a_k\le C e^{-bp}.
\tag{2.1}
\]

Here \(C,b>0\) are independent of \(m,n\), and \(p\) is any nonnegative
integer. This explicitly states the extra analytic-tail hypothesis; it is not
inferred from smoothness. For example, nonnegative coefficients and a finite
value \(\kappa(R)\) at some \(R>1\) imply such a bound, since
\(\sum_{k>p}a_k\le\kappa(R)R^{-(p+1)}\).

Define the polynomial Gram matrix

\[
(K_p)_{ab}=\sum_{k=0}^p a_k(v_a^\top v_b)^k.
\]

It is positive semidefinite. Its rank is at most

\[
R_p=\binom{p+d-1}{d-1}+\binom{p+d-2}{d-1}
\le\frac{2(p+d-1)^{d-1}}{(d-1)!},\qquad d\ge2,
\tag{2.2}
\]

where the second binomial is zero at \(p=0\). To see the rank bound, every
polynomial of degree at most \(p\), restricted to the unit sphere, is a linear
combination of monomials containing the last coordinate to power zero or one:
replace every factor \(x_d^2\) by \(1-\sum_{i<d}x_i^2\). The two monomial
counts give (2.2). Each column of \(K_p\) belongs to the resulting evaluation
space.

Let \(P\) be the orthogonal projection onto the nullspace of \(K_p\). If
\(m\ge2R_p\), then \(\operatorname{tr}P\ge m/2\), and

\[
\begin{aligned}
\lambda_{\min}(Q)\operatorname{tr}P
&\le\operatorname{tr}(PQ),\\
\mathbb E\operatorname{tr}(PQ)
&=\operatorname{tr}\bigl(P(\mathbb EQ-K_p)\bigr)
\le\operatorname{tr}(\mathbb EQ-K_p)
\le mCe^{-bp}.
\end{aligned}
\]

The middle inequality uses that the remainder is positive semidefinite, not
just entrywise small. Markov's inequality now gives, with probability at least
\(1-\eta\),

\[
\lambda_{\min}(Q)\le\frac{2C}{\eta}e^{-bp}.
\tag{2.3}
\]

For a direct count bound, set

\[
a=\left(\frac{(d-1)!m}{4}\right)^{1/(d-1)},\qquad
p=\lfloor a\rfloor-d+1.
\]

If \(a\ge d\), then \(p\ge0\), \(m\ge2R_p\), and \(p\ge a-d\). Thus,
on the probability-\(1-\eta\) event in (2.3), the additional condition
\(\lambda_{\min}(Q)\ge\gamma\) implies

\[
m\le\frac4{(d-1)!}
\left[d+\frac1b\log\left(\frac{2C}{\eta\gamma}\right)\right]^{d-1}.
\tag{2.4}
\]

The case \(a<d\) already bounds \(m\) by
\(4d^{d-1}/(d-1)!\). For \(d=1\), the unit sphere has two points and positive
definiteness forces \(m\le2\).

This proof applies to finite width if (2.1) holds for the **actual expected
finite-width Gram matrix**, with uniform constants. Analyticity of a limiting
infinite-width kernel alone does not verify that premise. For a deterministic
population Gram matrix, the same proof omits Markov's inequality and takes
\(\eta=1\).

Combining (2.4) with an already proved condition \(Y\le c\gamma/m\) gives a
sufficient label condition of order
\(\gamma/[\log(1/(\eta\gamma))]^{d-1}\). This is a reparameterization using
a forced relation between \(m\) and \(\gamma\); it does not enlarge the
admissible labels for a fixed dataset by itself.

## 3. A smooth activation that defeats every such polylogarithmic count bound

Fix the activations once, independently of \(m,n\):

\[
\phi_1(x)=\sum_{j=1}^{\infty}e^{-j^2}
\bigl(\sin(2^jx)+\cos(2^jx)\bigr),\qquad
\phi_\ell(x)=\sin x+\cos x\quad(2\le\ell\le L).
\tag{3.1}
\]

For every nonnegative integer \(r\), the differentiated series for \(\phi_1\)
is uniformly absolutely convergent because

\[
\sup_x|\phi_1^{(r)}(x)|
\le2\sum_{j\ge1}\exp(-j^2+rj\log2)<\infty.
\tag{3.2}
\]

Thus these activations are bounded and infinitely differentiable, with bounded
derivatives of every order. In particular they satisfy the assigned bounds on
the first three derivatives, with constants independent of sample count.

Use the equally spaced inputs on a circle in \(\mathbb R^d\), for any fixed
\(d\ge2\):

\[
v_a=\bigl(\cos(2\pi a/m),\sin(2\pi a/m),0,\ldots,0\bigr),
\qquad a=0,\ldots,m-1.
\]

For standard jointly Gaussian variables \(G,G'\) with correlation \(t\), the
first-layer population covariance is

\[
\begin{aligned}
\kappa_1(t)
&=\mathbb E[\phi_1(G)\phi_1(G')]\\
&=\sum_{p,q\ge1}e^{-p^2-q^2}
\exp\left[-\frac{4^p+4^q}{2}\right]
\exp(2^{p+q}t).
\end{aligned}
\tag{3.3}
\]

The mixed sine-cosine expectations vanish by Gaussian sign symmetry, while
the sine-sine and cosine-cosine terms sum to the displayed exponential.
Absolute convergence justifies the exchanges. Let \(q_1=\kappa_1(1)\).

The subsequent population covariance recursion is exact:

\[
\kappa_2(t)=e^{-q_1+\kappa_1(t)},\qquad
\kappa_\ell(t)=e^{-1+\kappa_{\ell-1}(t)}\quad(3\le\ell\le L).
\tag{3.4}
\]

Indeed, for centered jointly Gaussian \(X,Y\),

\[
\mathbb E[(\sin X+\cos X)(\sin Y+\cos Y)]
=e^{-(\operatorname{Var}X+\operatorname{Var}Y)/2+\operatorname{Cov}(X,Y)}.
\]

In particular \(\kappa_\ell(1)=1\) for \(\ell\ge2\).

### 3.1 A lower bound for all angular Fourier coefficients needed by the grid

All Fourier coefficients of \(\theta\mapsto\kappa_1(\cos\theta)\) are
nonnegative. This follows directly from (3.3) and the expansion

\[
e^{s\cos\theta}
=e^{(s/2)e^{i\theta}}e^{(s/2)e^{-i\theta}}.
\]

For \(k\ge0\), the coefficient at frequency \(k\) is
\(\sum_{q\ge0}(s/2)^{2q+k}/[q!(q+k)!]\). Consequently the diagonal term
\(p=q=j\) in (3.3) contributes at least

\[
e^{-2j^2}e^{-s}
\sum_{q\ge0}\frac{(s/2)^{2q+k}}{q!(q+k)!},
\qquad s=4^j.
\tag{3.5}
\]

For completeness, this coefficient has the elementary lower bound

\[
e^{-s}\sum_{q\ge0}\frac{(s/2)^{2q+k}}{q!(q+k)!}
\ge\frac{e^{-4}}s,
\qquad 0\le k\le\sqrt s,\quad s=4^j.
\tag{3.6}
\]

To prove it, retain only \(q=r=s/2\). The elementary Stirling upper estimate
\(r!\le e\sqrt r(r/e)^r\) and its counterpart for \(r+k\) give this term at
least

\[
\frac{e^{-2}}{\sqrt{r(r+k)}}
\exp\{k-(r+k)\log(1+k/r)\}.
\]

Since \(\log(1+x)\le x\), the exponent is at least \(-k^2/r\ge-2\).
Also \(r\ge2\), \(k\le\sqrt{2r}\le r\), and
\(\sqrt{r(r+k)}\le\sqrt2r\le s\). This proves (3.6).

Exponentiation preserves nonnegative Fourier coefficients. In (3.4), retaining
the linear term of each exponential therefore shows that the Fourier
coefficient of \(\kappa_L(\cos\theta)\), denoted \(a_k^{(L)}\), obeys

\[
a_k^{(L)}\ge
e^{-q_1-(L-2)}\frac{e^{-4}e^{-2j^2}}{4^j},
\qquad |k|\le2^j.
\tag{3.7}
\]

There is no cancellation in any of these inequalities.

### 3.2 The population Gram gap

Let \(K^{(L)}_{ab}=\kappa_L(v_a^\top v_b)\). This is circulant. Its eigenvalue
for residue class \(r\) modulo \(m\) is

\[
\lambda_r(K^{(L)})
=m\sum_{q\in\mathbb Z}a_{r+qm}^{(L)}.
\tag{3.8}
\]

For each residue class select its representative with absolute value at most
\(m/2\). Set \(j=\lceil\log_2m\rceil\), so \(m\le2^j<2m\). Equations
(3.7)--(3.8) give

\[
\lambda_{\min}(K^{(L)})\ge
\frac{c_L}{m}e^{-2\lceil\log_2m\rceil^2},
\qquad
c_L=\frac14e^{-q_1-L-2}>0.
\tag{3.9}
\]

Every constant here belongs to the one fixed activation family and fixed
depth. It is independent of \(m,n,d\) for all \(d\ge2\).

### 3.3 Passing to the actual finite-width Gaussian initialization

For each fixed finite dataset and depth,

\[
Q_0\longrightarrow K^{(L)}\quad\text{in probability as }n\to\infty.
\tag{3.10}
\]

Here is the direct argument, without a training-time concentration premise.
At the first layer the rows of the activation matrix are independent bounded
random vectors, so every empirical covariance entry converges by the law of
large numbers to (3.3). Conditional on all previous-layer activations, each
next-layer preactivation row is an independent centered Gaussian vector with
covariance equal to that previous empirical covariance. Boundedness of the
activations gives a conditional variance of order \(1/n\) for each new
empirical covariance entry. Its conditional mean is the Gaussian covariance
map evaluated at the previous covariance. That map is continuous: if
covariances converge, their nonnegative square roots converge, so a common
standard Gaussian vector and bounded continuous activations give convergence
by dominated convergence. Induction over the fixed depth proves (3.10), first
entrywise and then in operator norm because \(m\) is fixed in this limit.

Therefore, for any prescribed \(\eta>0\) and each \(m\), sufficiently large
finite width gives, with probability at least \(1-\eta\),

\[
\lambda_{\min}(Q_0)\ge\gamma_m,
\qquad
\gamma_m=\frac{c_L}{2m}e^{-2\lceil\log_2m\rceil^2}.
\tag{3.11}
\]

The initialized hidden operator norm bound can hold simultaneously. One
elementary verification uses a \(1/4\)-net of the unit sphere with at most
\(9^n\) points. For a matrix with independent \(N(0,1/n)\) entries,
\(\|W\|_{\mathrm{op}}\le2\max_{u,v\text{ in the net}}|u^\top Wv|\).
The scalar Gaussian tail and a union bound give

\[
\mathbb P(\|W\|_{\mathrm{op}}>8)
\le2\exp\{n(2\log9-8)\}\longrightarrow0.
\]

A union bound covers all \(L-1\) hidden matrices. The same argument with
rectangular nets bounds \(\|A_0\|_{\mathrm{op}}/\sqrt n\) by \(8\) with
probability tending to one when \(d\) is fixed. Thus the counterexample also
meets a deterministic initial operator norm event of the sort permitted in
the assignment. No assertion about how large the required width is has been
used or needed.

### 3.4 Failure of every fixed polylogarithmic count bound

Equation (3.11) yields

\[
\log(1/\gamma_m)
=\log(2/c_L)+\log m+2\lceil\log_2m\rceil^2
=O_L((\log m)^2).
\]

Hence, for every fixed finite \(C,p>0\),

\[
C[\log(C/\gamma_m)]^p=O_{C,p,L}((\log m)^{2p})<m
\]

for all sufficiently large \(m\). This contradicts any claimed universal
polylogarithmic implication under the assigned assumptions. Using the actual
minimum eigenvalue instead of the specified lower bound cannot repair it:
on the event (3.11) that eigenvalue is at least \(\gamma_m\), which only
decreases the logarithm in the proposed bound.

## 4. Why this kernel is not analytic at unit correlation

The counterexample does not dispute the conditional argument in Section 2.
It violates its analytic-tail hypothesis. From the positive diagonal terms in
(3.3), for every derivative order \(r\),

\[
\kappa_1^{(r)}(1)\ge
\sum_{j\ge1}\exp(-2j^2+2rj\log2).
\]

Choosing the integer nearest \(r\log2/2\), for large \(r\), gives

\[
\kappa_1^{(r)}(1)
\ge\exp\left(\frac{(\log2)^2}{2}r^2-\frac12\right).
\]

These derivatives cannot satisfy any analytic estimate
\(C r!R^{-r}\) with \(R>0\). The derivative series is finite at every fixed
order, so the kernel is smooth up to \(t=1\), but not analytic there. The same
positive-coefficient domination used in (3.7) transfers this obstruction to
every fixed depth. Analyticity on the open interval \((-1,1)\) therefore does
not supply the endpoint tail control needed by Section 2.

## 5. Audit and remaining scope

The construction retains Gaussian initialization, fixed depth at least two,
bounded smooth activations and derivatives, unit inputs, and a bounded
initial hidden operator norm event. It uses no label-dependent geometry,
changed optimizer, or concentration premise during training. The population
kernel is used only as an intermediate object; (3.10)--(3.11) explicitly return
to finite width.

What is proved: an explicit obstruction to replacing the stated smoothness
assumptions by a quantitative analytic sphere-kernel premise, and a complete
conditional analytic count lemma with dimension dependence.

What remains open in this route: a sharper global fitting/bounded-motion
theorem; an activation-dependent, slower-than-polylogarithmic count bound;
and any way to exploit the evolving label direction to reduce the actual
\(m\)-dependence of the sufficient label condition. The counterexample is
not evidence that such dynamical improvements are impossible.
