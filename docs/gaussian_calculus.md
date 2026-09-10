# Gaussian reuse and finite-order flow calculus

This chapter develops Gaussian matrix reuse and finite-order flow calculus.
It includes conditioning and fixed-program width identification, moving
physical-flow jets, forest expectation factorization, and small exact rational
certificates, quantitative fixed-program step doubling, and exact finite
loss-GD pullback words with a separate conditional comparison bound. It also
proves an existential positive-metric Stieltjes obstruction and canonical
factorial growth for a specified quadratic annealed initialization jet, with
non-Cauchy behavior of its prescribed Taylor losses.
Section 11 gives a sharp shallow feature-step bound uniform in update count,
with explicit activation-only constants and a short-interval dyadic
terminal-output consequence under its order-one-readout initialization.
Use [the shared notation](NOTATION.md). The statements distinguish
finite derivatives, formal coefficients and actual width limits; they do not
assert convergence of an infinite Taylor series or a width-dependent number
of adaptive matrix calls.

## 1. One forward call followed by a transpose

Let `W=W^(2)(0)` have independent `N(0,1/n)` entries and let `1` be the
length-`n` vector of ones. Put `y=W 1`. Its entries are independent standard
Gaussians. Take a continuous real function `g` of polynomial growth and define

\[
q=W^T g(y),\qquad
a_n=\frac1n\sum_i y_i g(y_i),\qquad
\sigma_n^2=\frac1n\sum_i g(y_i)^2,\qquad
P=I-\frac{\mathbf1\mathbf1^T}{n}.
\]

Conditional on `y`, the exact matrix law is

\[
W\ \overset{d}{=}\ \frac{y\mathbf1^T}{n}+\widetilde W P,
\qquad
q\ \overset{d}{=}\ a_n\mathbf1+\sigma_n P\gamma,
\tag{1}
\]

where `tilde W` has the original Gaussian matrix law and `gamma` is a standard
Gaussian vector, each independent of `y` in its corresponding representation.
For the first equality, decompose each Gaussian row into its component along
`1` and its perpendicular component. Their covariance vanishes, so they are
independent; the first component is determined by the observed row sum.
Multiplying the conditional matrix by `g(y)` on the left gives the second
equality, because `tilde W^T g(y)` has conditional covariance `sigma_n^2 I`.
In particular

\[
\mathbb E[q\mid y]=a_n\mathbf1,\qquad
\operatorname{Cov}(q\mid y)=\sigma_n^2P.
\tag{2}
\]

The random coefficient `a_n` is not replaced by its expectation at finite
width. If `G` is a standard scalar Gaussian, the elementary law of large
numbers gives

\[
a_n\longrightarrow a=\mathbb E[Gg(G)],\qquad
\sigma_n^2\longrightarrow\sigma^2=\mathbb E[g(G)^2]
\quad\text{in probability}.
\tag{3}
\]

All moments used here are finite by polynomial growth and Gaussian tails.
On the coupling in (1), compare `q` with `a 1+sigma gamma`. Their RMS distance
is at most

\[
|a_n-a|+|\sigma_n-\sigma|\frac{\|\gamma\|_2}{\sqrt n}
+\sigma_n\left|\frac1n\sum_i\gamma_i\right|,
\tag{4}
\]

which tends to zero in probability. This remains valid when `sigma=0`.
The empirical law of `a+sigma gamma_i` converges in quadratic Wasserstein
distance to the law of `a+sigma G`: weak convergence follows by applying the
law of large numbers to a countable dense family of bounded Lipschitz tests,
and the second moment converges by the same law. On the real line, weak
convergence together with convergence of second moments yields quadratic
Wasserstein convergence. One direct verification truncates at a fixed radius,
couples the bounded laws using their quantiles, and lets the radius grow;
convergence of second moments makes the two squared-tail contributions vanish.
Matching corresponding coordinates and using (4) proves the same convergence
for the empirical law of `q_i`.

If `g` is also continuously differentiable and `g'` has polynomial growth,
integration by parts in the Gaussian density gives

\[
a=\frac1{\sqrt{2\pi}}\int xg(x)e^{-x^2/2}dx
=\frac1{\sqrt{2\pi}}\int g'(x)e^{-x^2/2}dx.
\tag{5}
\]

The boundary term is zero because a polynomial times the Gaussian density
tends to zero. The transpose output therefore contains a response
`E[g'(G)]` forced by the preceding forward call, in addition to fresh Gaussian
randomness. Treating the transpose as a new independent matrix would erase
that response. The two neuron populations remain distinct; pairing row `i`
with column `i` is not part of this empirical-law statement.

## 2. Exact conditioning after both directions have been used

Suppose past calls have revealed `W V=Y` and `W^T U=R`. Columns of `V` are
input vectors in the first population; columns of `U` are input vectors in the
second. Assume both lists are linearly independent, allowing either list to be
empty. All matrix dimensions are finite. Define

\[
P_V=V(V^TV)^{-1}V^T,\qquad P_U=U(U^TU)^{-1}U^T,
\]
\[
M=Y(V^TV)^{-1}V^T+U(U^TU)^{-1}R^T(I-P_V).
\]

Conditional on the complete transcript, the exact remaining matrix law is

\[
W\ \overset d=\ M+(I-P_U)\widetilde W(I-P_V).
\tag{6}
\]

To verify the mean, use the compatibility identity `U^T Y=R^T V`, which
holds because both lists were observed from the same matrix. It gives
`MV=Y` and `M^T U=R`. A homogeneous perturbation preserves both observations
exactly when `A V=0` and `A^T U=0`, equivalently
`A=(I-P_U)A(I-P_V)`. The displayed `M` is Frobenius-orthogonal to every such
perturbation: its first summand has right support in `span(V)`, and its second
has left support in `span(U)`. Thus it is the minimum-norm point of the affine
constraint set. Orthogonal components of an isotropic finite Gaussian vector
are independent. Applying this fact to the vector of all matrix entries proves
(6), including the scale `1/n` of the remaining covariance.

This reasoning also holds for a finite adaptive transcript when every new input
is a measurable function of roots independent of `W` and of earlier answers,
and is chosen before its own answer is seen. Condition on the roots first.
Inductively, the next query is fixed by the past, and conditioning its Gaussian
answer adds a linear constraint to the remaining Gaussian subspace. The
orthogonal-decomposition argument applies there. Derived variables measurable
from these recorded roots and answers add no further information. This induction
does not allow an unrecorded observation of `W` or an input chosen using its
future answer.

Dependent query columns can be discarded: each is an exactly known linear
combination of retained columns and its answer is the same combination of
retained answers. This does not justify taking limits of ill-conditioned Gram
inverses. Infinite-width arguments with nearly dependent directions require an
additional stability argument.

For a new input `v`, (6) explicitly yields

\[
Wv\ \overset d=\ Y\alpha+U\beta+
\frac{\|(I-P_V)v\|_2}{\sqrt n}(I-P_U)\gamma,
\quad
\alpha=(V^TV)^{-1}V^Tv,\quad
\beta=(U^TU)^{-1}R^T(I-P_V)v.
\tag{7}
\]

The first response preserves previous forward answers, the second restores
the overlap demanded by previous transpose answers, and the random part
preserves both sets of constraints. Exchanging the two populations gives the
transpose formula. This is a finite exact identity, not an iid assertion about
coordinates after reuse.

## 3. Derivatives along the gradient direction

Let `F:R^p->R` be `C^3` on an open set. At a point write `g=grad F`,
`H=grad^2 F` and `T=grad^3 F`. For a differentiable scalar function `u`, define
the directional differential operator `mathcal D_F u=<g,grad u>`.
Repeated application gives

\[
\mathcal D_F F=\|g\|_2^2,\qquad
\mathcal D_F^2F=2\langle g,Hg\rangle,\qquad
\mathcal D_F^3F=2T[g,g,g]+4\|Hg\|_2^2.
\tag{8}
\]

The first formula is the definition. Differentiating `||g||^2` in direction
`g` uses `d g[g]=Hg` and gives the second formula. To differentiate
`<g,Hg>`, differentiate its three factors. The derivative of `H` contributes
`T[g,g,g]`. The two derivatives of `g` contribute
`<Hg,Hg>` and `<g,H^2g>`, both equal to `||Hg||^2` because the Hessian is
symmetric. Multiplication by two gives the last identity.

For a constant positive definite learning metric `D`, change coordinates to
`theta=D^(1/2) q` and apply (8) to `F(D^(1/2) q)`. Its Euclidean gradient
flow in `q` is exactly the metric gradient flow in `theta`. This supplies the
metric version without confusing raw gradients, mobilities and residuals.

If `theta(s)` follows `theta'=grad F(theta)`, the chain rule identifies
`d^j F(theta(s))/ds^j` with `mathcal D_F^j F` whenever the stated derivatives
exist. For squared loss the physical velocity has the additional residual
factor, so conversion to physical derivatives also differentiates that factor.
Finite-order identities alone provide neither an analytic Taylor expansion
nor permission to exchange width limits and time differentiation.

## 4. Exact polynomial Gaussian expectations

Let `Sigma` be a finite symmetric positive semidefinite matrix and `X` a
centered Gaussian vector with that covariance. For a vector `alpha` of
nonnegative integer powers, put `M(alpha)=E[prod_j X_j^(alpha_j)]`.
The zero-degree moment is one; every odd-total-degree moment is zero by the
symmetry `X` and `-X`. If `alpha_i>0`, Gaussian integration by parts gives

\[
M(\alpha)=\sum_{j=1}^p(\alpha_j-\mathbf1_{j=i})\Sigma_{ij}
 M(\alpha-e_i-e_j),
\tag{9}
\]

where terms with zero coefficient are omitted, so negative exponents never
occur. To prove the integration-by-parts identity even for singular covariance,
write `X=A G`, where `G` is a standard Gaussian vector and `A A^T=Sigma`.
Such a square root exists by diagonalizing the finite symmetric matrix.
For any polynomial `P`, integrate each component of `G` against its Gaussian
density. Polynomial growth makes all boundary terms zero, and the chain rule
gives

\[
\mathbb E[X_iP(X)]
=\sum_{k,j}A_{ik}A_{jk}\mathbb E[\partial_jP(X)]
=\sum_j\Sigma_{ij}\mathbb E[\partial_jP(X)].
\]

Apply this identity to `P(X)=prod_j X_j^(alpha_j-1_(j=i))` to obtain (9).
Every nonzero summand reduces total degree by two. Induction therefore proves
termination and correctness of the moment recurrence. With rational covariance
all its arithmetic is rational, and linearity evaluates every polynomial with
rational coefficients. The exact API `pde.gaussian_moment` implements this
recurrence using integer and `Fraction` inputs; it does not approximate a
nonpolynomial activation by a polynomial or identify a training limit.

For completeness, its covariance validation also has an exact finite proof.
At a symmetric block matrix

\[
\begin{pmatrix}a&b^T\\ b&C\end{pmatrix},
\]

a negative `a` contradicts nonnegativity on the first basis vector. If `a=0`,
positive semidefiniteness forces `b=0`: otherwise the quadratic form on
`(t,v)` with `b^T v` nonzero changes sign for a suitable large positive or
negative `t`. The remaining condition is then exactly that `C` is positive
semidefinite. If `a>0`, completing the square gives

\[
a t^2+2t b^Tv+v^TCv
=a\left(t+\frac{b^Tv}{a}\right)^2
+v^T\left(C-\frac{bb^T}{a}\right)v.
\]

Thus the condition is exactly positive semidefiniteness of the Schur complement.
Recursing proves the rational validator without a floating tolerance, matrix
inverse at a zero pivot, or a nonsingularity assumption. This validates a finite
covariance; it is not a proof about the stability of adaptive query inverses.

## 5. Fixed-program width limits for exact feature-ascent steps

This section gives the complete width-first identification at every
separately fixed depth, step count and nonzero feature-ascent step.
The initialization, optimizer and order of limits are stated explicitly
below. No Taylor expansion in the step and no physical-time limit is used.

### 5.1. The theorem

Fix integers \(L\ge1\) and \(N\ge1\), and a real scalar step
\(h\ne0\). Here \(L\) counts hidden layers, \(N\) is the number of
simultaneous feature-ascent updates, and \(k=0,\ldots,N\) is a step
index. The scalar \(h\) is distinct from a hidden feature \(h^{(\ell)}\);
it is neither a physical loss-GD step \(\eta_n\) nor an auxiliary
continuum mesh \(\Delta\). There is one scalar input, \(m=d=1\), \(x_1=1\).
No target or loss is used in these updates. Assume, for a fixed \(M<\infty\),

\[
 \phi\in C^2(\mathbb R),\qquad
 |\phi(x)|\le M(1+|x|),\qquad
 \|\phi'\|_\infty+\|\phi''\|_\infty\le M,                 \tag{5.1.1}
\]
\[
 \mathbb E\phi(G)^2=1,\qquad G\sim N(0,1).                \tag{5.1.2}
\]

**Theorem (fixed-program width limit).** For the exact network in
Section 5.2, let \(f_{n,L}^N\) be its output after the \(N\) updates.
The stored readout has independent order-one \(N(0,1)\) initial
coordinates. If \(\phi\) is nonconstant, every population history Gram
used by the \((2N+1)(L-1)\)-action conditioning chronology is positive
definite, and
\[
 \lim_{n\to\infty}\mathbb E f_{n,L}^N=F_{N,L}(h).        \tag{5.1.3}
\]
Here \(F_{N,L}(h)\) is the output of the finite inverse-free Gaussian
program in Section 5.5. More precisely, one joint coupling identifies
every raw initialization-matrix action, preactivation, feature, incoming
backsignal and cotangent with its ideal coordinate array. For every such
finite vector \(v_n\in\mathbb R^n\), let \(\bar v\in\mathbb R^n\) denote
the coupled iid coordinate copies of its population field. For all
\(1\le p,P<\infty\),
\[
 \left(\mathbb E\left[
    \left(\frac1n\sum_{i=1}^n|v_{n,i}-\bar v_i|^p\right)^{P/p}
                       \right]\right)^{1/P}\longrightarrow0.
\]
All empirical Grams and raw response cross-moments converge jointly
in every finite scalar moment. The regression coefficients, extended
predictably as in Section 5.9, also converge in every finite moment;
the terminal outputs are uniformly integrable.

If \(\phi\) is constant, (5.1.2) gives \(\phi\equiv c\in\{-1,1\}\).
All hidden cotangents vanish and only the readout changes:
\(W^{(L+1)}_{N}=W^{(L+1)}_0+Nhc\,\mathbf1\).
Consequently
\[
 \mathbb E f_{n,L}^N=Nh.                                \tag{5.1.4}
\]
Thus (5.1.3) also holds in that branch, without a cotangent Gram
inversion.

The theorem is pointwise for every fixed \(h\ne0\), including negative
steps. Its constants may depend on \((L,N,h,M)\). It asserts neither
a depth-uniform nor a step-count-uniform conditioning gap, and does
not take a small-step or continuous-time limit.

For \(L=1\), there is no reused matrix. The exact coordinate recursion is
\[
 \begin{aligned}
 W^{(2)}_{k+1,j}
   &=W^{(2)}_{k,j}+h\phi(z^{(1)}_{k,j}),\\
 z^{(1)}_{k+1,j}
   &=z^{(1)}_{k,j}+hW^{(2)}_{k,j}\phi'(z^{(1)}_{k,j}),
 \end{aligned}                                         \tag{5.1.5}
\]
and
\[
 f_{n,1}^N=\frac1n\sum_{j=1}^n
             W^{(2)}_{N,j}\phi(z^{(1)}_{N,j}).           \tag{5.1.6}
\]
The coordinate pairs remain iid for every finite \(N\). Iterating
linear growth and bounded \(\phi'\) bounds the summand by a finite
polynomial in \(|W^{(2)}_{0,j}|+|z^{(1)}_{0,j}|\), so it has every
finite moment. Hence
\(\mathbb E f_{n,1}^N=\mathbb E[W^{(2)}_{N,1}\phi(z^{(1)}_{N,1})]\)
for every \(n\); the ideal coordinate recursion is the same scalar
recursion, and its identification is exact. The rest of the proof treats
\(L\ge2\).

The proof first unrolls the exact finite updates and their predictable
matrix-call chronology. Gaussian conditioning and integration by parts
identify the inverse-free population program. Strict rank, including
the affine activation case, then supplies a positive fixed-program
conditioning gap. A finite even-moment induction constructs the joint
coupling; a raw-network polynomial bound removes the predictable stopping
and proves convergence of the terminal expectation.

### 5.2. Exact finite-width network and updates

There are no biases. Each hidden layer has width \(n\).
The finite first weight \(W^{(1)}_k\in\mathbb R^{n\times1}\) is
identified with its column, every middle stored weight
\(W^{(\ell)}_k\in\mathbb R^{n\times n}\), \(2\le\ell\le L\),
and the stored readout \(W^{(L+1)}_k\in\mathbb R^n\).
All initialization entries are independent, with
\[
 W^{(1)}_{0,i}\sim N(0,1),\qquad
 W^{(\ell)}_{0,ij}\sim N(0,1/n)\ (2\le\ell\le L),\qquad
 W^{(L+1)}_{0,i}\sim N(0,1).                            \tag{5.2.1}
\]
In particular the readout is not in the small-readout regime.

The explicitly related unscaled middle matrices are
\(\mathsf A^{(\ell)}_k=\sqrt n\,W^{(\ell)}_k\); their initial
entries are \(N(0,1)\). Thus the two exactly equivalent forward
expressions are
\(W^{(\ell)}_kh^{(\ell-1)}_k
=\mathsf A^{(\ell)}_kh^{(\ell-1)}_k/\sqrt n\).
All network formulas below use the stored \(W^{(\ell)}\) convention.

At step \(k\), recompute
\[
 z^{(1)}_k=W^{(1)}_k,\qquad h^{(1)}_k=\phi(z^{(1)}_k),    \tag{5.2.2}
\]
\[
 z^{(\ell)}_k=W^{(\ell)}_kh^{(\ell-1)}_k,\qquad
 h^{(\ell)}_k=\phi(z^{(\ell)}_k)\quad(2\le\ell\le L).     \tag{5.2.3}
\]
The output and residual-free backward fields are
\[
 f_{n,L}^k=\frac1n(W^{(L+1)}_k)^Th^{(L)}_k,\qquad
 \delta^{(L)}_k=W^{(L+1)}_k\odot\phi'(z^{(L)}_k),        \tag{5.2.4}
\]
\[
 q^{(\ell-1)}_k=(W^{(\ell)}_k)^T\delta^{(\ell)}_k,\qquad
 \delta^{(\ell-1)}_k=q^{(\ell-1)}_k\odot\phi'(z^{(\ell-1)}_k),
 \quad \ell=L,L-1,\ldots,2.                            \tag{5.2.5}
\]
Here \(q^{(\ell)}_k,\delta^{(\ell)}_k\in\mathbb R^n\).
For the tuple \(\Theta_k\) of stored parameters, one exact update is
\[
 \Theta_{k+1}=\Theta_k+hD_n\nabla_\Theta f_{n,L}(\Theta_k),
 \qquad D_n=\operatorname{diag}(nI,I,\ldots,I,nI).      \tag{5.2.6}
\]
The middle identity blocks act on matrix entries with the ordinary
Frobenius metric. Thus the fixed mobility multipliers are
\(\kappa_\ell=1\). In the tuple consisting of the first weight,
the unscaled \(\mathsf A^{(\ell)}\), and the stored readout, the same
update is \(\theta_{k+1}=\theta_k+hn\nabla_\theta f_{n,L}(\theta_k)\):
the change of variables divides the middle gradient and middle
increment each by \(\sqrt n\), producing middle mobility one in
(5.2.6).

Direct differentiation, evaluating every right-hand side at step \(k\),
gives
\[
 \begin{aligned}
 W^{(L+1)}_{k+1}&=W^{(L+1)}_k+h\,h^{(L)}_k,\\
 W^{(\ell)}_{k+1}&=W^{(\ell)}_k+
       \frac h n\delta^{(\ell)}_k(h^{(\ell-1)}_k)^T
                    \quad(2\le\ell\le L),\\
 z^{(1)}_{k+1}&=z^{(1)}_k+h\delta^{(1)}_k.
 \end{aligned}                                         \tag{5.2.7}
\]
Indeed,
\[
 \nabla_{W^{(\ell)}}f_{n,L}(\Theta_k)
       =\frac1n\delta^{(\ell)}_k(h^{(\ell-1)}_k)^T,\qquad
 \nabla_{W^{(1)}}f_{n,L}(\Theta_k)=\frac1n\delta^{(1)}_k. \tag{5.2.8}
\]
These are simultaneous raw feature-ascent updates followed by
recomputation, not loss GD, frozen-feature updates, or a GF discretization
whose mesh is being sent to zero.

Retain only initialization matrices in the raw action vectors
\[
 x^{(\ell)}_k=W^{(\ell)}_0h^{(\ell-1)}_k,\qquad
 v^{(\ell-1)}_k=(W^{(\ell)}_0)^T\delta^{(\ell)}_k.        \tag{5.2.9}
\]
The auxiliary \(x^{(\ell)}_k,v^{(\ell-1)}_k\in\mathbb R^n\)
are outputs of initialization actions, not the sample input or the full
current preactivation and backsignal. Define the finite history moments
\[
 Q_{\ell,jk}^{(n)}=\frac1n(h^{(\ell)}_j)^Th^{(\ell)}_k,\qquad
 K_{\ell,jk}^{(n)}=\frac1n(\delta^{(\ell)}_j)^T\delta^{(\ell)}_k.
                                                               \tag{5.2.10}
\]
Here \(Q,K\) are auxiliary history Grams, not parameter-gradient kernel
blocks. Summing (5.2.7) before substitution into (5.2.3) and (5.2.5)
gives the exact identities
\[
 z^{(\ell)}_k=x^{(\ell)}_k+
       h\sum_{j<k}Q_{\ell-1,jk}^{(n)}\delta^{(\ell)}_j
                    \quad(2\le\ell\le L),              \tag{5.2.11}
\]
\[
 q^{(\ell-1)}_k=v^{(\ell-1)}_k+
       h\sum_{j<k}K_{\ell,jk}^{(n)}h^{(\ell-1)}_j
                    \quad(2\le\ell\le L),              \tag{5.2.12}
\]
\[
 W^{(L+1)}_k=W^{(L+1)}_0+h\sum_{j<k}h^{(L)}_j,\qquad
 z^{(1)}_k=z^{(1)}_0+h\sum_{j<k}\delta^{(1)}_j.          \tag{5.2.13}
\]
Every sum uses strictly earlier steps; no current-step term is inserted.

### 5.3. The exact \((2N+1)(L-1)\) chronology

For \(0\le k<N\), first reveal the forward actions

\[
 \mathsf F_{k,2},\mathsf F_{k,3},\ldots,\mathsf F_{k,L},
 \qquad \mathsf F_{k,\ell}:=x^{(\ell)}_{k},                    \tag{5.3.1}
\]

then the backward actions

\[
 \mathsf B_{k,L},\mathsf B_{k,L-1},\ldots,\mathsf B_{k,2},
 \qquad \mathsf B_{k,\ell}:=v^{(\ell-1)}_{k}.               \tag{5.3.2}
\]

After the \(N\)-th update reveal only the terminal forward sweep

\[
 \mathsf F_{N,2},\ldots,\mathsf F_{N,L}.                  \tag{5.3.3}
\]

Thus the number of initialization-matrix actions is exactly

\[
 N\{2(L-1)\}+(L-1)=(2N+1)(L-1).                         \tag{5.3.4}
\]

An explicit action index is

\[
 \begin{aligned}
 \iota(\mathsf F_{k,\ell})
   &=2k(L-1)+(\ell-1), &&0\le k<N,\\
 \iota(\mathsf B_{k,\ell})
   &=2k(L-1)+(L-1)+(L-\ell+1), &&0\le k<N,\\
 \iota(\mathsf F_{N,\ell})
   &=2N(L-1)+(\ell-1).
 \end{aligned}                                             \tag{5.3.5}
\]

At \(\mathsf F_{k,\ell}\), the query \(h^{(\ell-1)}_{k}\) is known because
the forward sweep has already reached layer \(\ell-1\).  At
\(\mathsf B_{k,\ell}\), the query \(\delta^{(\ell)}_{k}\) is known because the
backward sweep has already reached layer \(\ell\).  Each query may depend
on every earlier action of every matrix.  In particular,
\(h^{(\ell-1)}_{k}\) contains all preceding descending passes through
\((W^{(\ell)}_0)^T\), including the reused-column actions of the same matrix.
This is predictable dependence, not independence.

For connector \(\ell\), immediately before \(\mathsf F_{k,\ell}\), the
old row and column query blocks are

\[
 h^{(\ell-1)}_{<k}=(h^{(\ell-1)}_{0},\ldots,h^{(\ell-1)}_{k-1}),
 \qquad \delta^{(\ell)}_{<k}=(\delta^{(\ell)}_{0},\ldots,\delta^{(\ell)}_{k-1}),       \tag{5.3.6}
\]

and immediately before \(\mathsf B_{k,\ell}\) they are

\[
 h^{(\ell-1)}_{\le k},\qquad \delta^{(\ell)}_{<k}.                  \tag{5.3.7}
\]

Empty blocks at \(k=0\) are omitted.

### 5.4. Adaptive conditioning for all reused matrices

**Lemma 5.4.1 (predictable multi-matrix Gaussian conditioning).**
Let \(M_2,\ldots,M_L\) be independent \(n\times n\) standard Gaussian
matrices, independent of an external sigma-field.  Consider any finite
interlacing of actions \(M_\ell q/\sqrt n\) and
\(M_\ell^Tc/\sqrt n\), where the matrix label and the next query are
measurable with respect to all preceding queries and actions.  For a fixed
matrix, collect its old row and column queries in \(V,U\), and set

\[
 Y=MV/\sqrt n,\qquad D=M^TU/\sqrt n.                      \tag{5.4.1}
\]

Conditionally on the global revealed filtration,

\[
 M=P_UM+MP_V-P_UMP_V+P_U^\perp\widetilde M P_V^\perp,    \tag{5.4.2}
\]

where the residual matrices \(\widetilde M_2,\ldots,\widetilde M_L\)
are conditionally independent standard Gaussian matrices and independent
of the revealed filtration.

Put

\[
 Q=V^TV/n,\qquad K=U^TU/n,\qquad
 \mathcal R=U^TY/n=D^TV/n.                               \tag{5.4.3}
\]

If \(Q,K\) are invertible, a new column query \(c_*\) satisfies

\[
 {M^Tc_*\over\sqrt n}
 =DK^{-1}k+VQ^{-1}(\omega-\mathcal R^TK^{-1}k)
   +\tau_cP_V^\perp g,                                   \tag{5.4.4}
\]

\[
 k=U^Tc_*/n,\quad \omega=Y^Tc_*/n,\quad
 \tau_c^2=c_*^Tc_*/n-k^TK^{-1}k.                         \tag{5.4.5}
\]

A new row query \(q_*\) satisfies

\[
 {Mq_*\over\sqrt n}
 =YQ^{-1}q+UK^{-1}(v-\mathcal RQ^{-1}q)
   +\tau_qP_U^\perp g,                                   \tag{5.4.6}
\]

\[
 q=V^Tq_*/n,\quad v=D^Tq_*/n,\quad
 \tau_q^2=q_*^Tq_*/n-q^TQ^{-1}q.                         \tag{5.4.7}
\]

Here \(V,U\) are finite query-column matrices and \(Y,D\) their
finite answer-column matrices. The local symbols \(q,k,v,\omega\) are
finite history-coordinate vectors, not step indices or network fields.
The fresh \(g\in\mathbb R^n\) has independent standard Gaussian entries.
The projector \(P_V\) is the ordinary orthogonal projection onto the
column span of \(V\), and similarly for \(U\). The displayed random
identities are conditional representations on a common coupling.
Empty blocks are omitted. For a singular Gram, diagonalize it, invert
only its positive eigenvalues, and set the other eigenvalues to zero.
This Moore--Penrose inverse gives the same orthogonal projector and the
same conditional identities, because dependent query directions add no
new observation.

**Proof.**  Induct on the global action number.  Suppose (5.4.2) holds
before a row query to \(M_j\).  Decompose
\(q_*=P_{V_j}q_*+q_\perp\).  All terms in the action except
\(P_{U_j}^\perp\widetilde M_jq_\perp\) are already measurable.  If
\(q_\perp\ne0\), put \(e=q_\perp/\|q_\perp\|_2\).  The Gaussian projections

\[
 \widetilde M_jee^T,\qquad \widetilde M_j(I-ee^T)          \tag{5.4.8}
\]

are independent.  Revealing the first leaves

\[
 P_{U_j}^\perp\widetilde M_j
 P_{\operatorname{span}(V_j,q_*)}^\perp                   \tag{5.4.9}
\]

fresh and independent of every other matrix residual.  If \(q_\perp=0\),
no residual is revealed.  A transpose action is the same argument with
left and right projections exchanged.  This proves (5.4.2) after every
adaptive, cross-matrix-dependent action in (5.3.1)--(5.3.3).

For (5.4.4), write \(c_*=UK^{-1}k+c_\perp\).  The first term contributes
\(DK^{-1}k\).  The projection of \(M^Tc_\perp/\sqrt n\) onto
\(\operatorname{span}(V)\) is

\[
 VQ^{-1}{Y^Tc_\perp\over n}
 =VQ^{-1}(\omega-\mathcal R^TK^{-1}k),                         \tag{5.4.10}
\]

and its remaining conditional covariance is
\(\tau_c^2P_V^\perp\).  This proves (5.4.4)--(5.4.5).
Transposition proves (5.4.6)--(5.4.7). For the network, apply this
lemma with \(M_\ell=\mathsf A^{(\ell)}_0=\sqrt n\,W^{(\ell)}_0\);
then its scaled actions are exactly (5.2.9). \(\square\)

### 5.5. The population inverse-free Gaussian DAG

All assignments below are chronological. Each layer has its own
probability space \((\Omega_\ell,\mathcal F_\ell,\mathbb P_\ell)\);
write \(E_\ell\) for its expectation. The fields
\(Z^{(\ell)}_k,H^{(\ell)}_k,\Delta^{(\ell)}_k,q^{(\ell)}_k\)
are real population random variables on layer \(\ell\), whenever the
indicated field is used. The population stored readout
\(W^{(L+1)}_k\) is a real random variable on layer \(L\).
All have every finite moment by the finite construction below.
Finite coordinate arrays, including iid sampled copies denoted by bars,
retain lowercase \(z,h,\delta,q\).

This theorem constructs the finitely queried population action laws;
it does not posit a bounded population weight operator on an entire
function space. The source blocks encode both directions of each reused
matrix and their responses. In generic identities \(\mathbb E\) means
expectation on the stated probability space; in a layer contraction it
means that layer's \(E_\ell\).  For every connector
\(2\le\ell\le L\), introduce centered Gaussian source blocks

\[
 \xi_\ell=(\xi_{\ell,0},\ldots,\xi_{\ell,N}),\qquad
 \chi_\ell=(\chi_{\ell,0},\ldots,\chi_{\ell,N-1}),        \tag{5.5.1}
\]

and independent \(U,A\sim N(0,1)\).  All source blocks, including the
\(\xi\)- and \(\chi\)-blocks belonging to the same connector, are mutually
independent.  Their within-block covariances are

\[
 \mathbb E\xi_{\ell,j}\xi_{\ell,k}
   =Q_{\ell-1,jk}:=E_{\ell-1}[H^{(\ell-1)}_{j}H^{(\ell-1)}_{k}],   \tag{5.5.2}
\]

\[
 \mathbb E\chi_{\ell,j}\chi_{\ell,k}
   =K_{\ell,jk}:=E_\ell[\Delta^{(\ell)}_{j}\Delta^{(\ell)}_{k}].             \tag{5.5.3}
\]

Each new source coordinate is adjoined only after the covariance on the
right is known. Section 5.7 proves that every covariance used here is
positive definite for nonconstant \(\phi\), including the terminal forward
covariances; hence an ordinary Gaussian
regression plus an independent innovation constructs it.  Equivalently,
one may simply take the unique centered Gaussian law with the displayed
finite covariance.  No covariance inverse appears in the DAG assignments
below.

Start with

\[
 Z^{(1)}_{0}=U,\qquad H^{(1)}_{k}=\phi(Z^{(1)}_{k}).                        \tag{5.5.4}
\]

For each \(k=0,\ldots,N\), perform the ascending sweep.  For
\(\ell=2,\ldots,L\), define

\[
 \rho_{\ell,kj}
 :=E_{\ell-1}[\partial_{\chi_{\ell,j}}H^{(\ell-1)}_{k}],
 \qquad 0\le j<k,                                        \tag{5.5.5}
\]

\[
 Z^{(\ell)}_{k}=\xi_{\ell,k}
  +\sum_{j<k}(\rho_{\ell,kj}+hQ_{\ell-1,jk})\Delta^{(\ell)}_{j},
 \qquad H^{(\ell)}_{k}=\phi(Z^{(\ell)}_{k}).                         \tag{5.5.6}
\]

If \(k<N\), set

\[
 W^{(L+1)}_{k}=A+h\sum_{j<k}H^{(L)}_{j},\qquad
 \Delta^{(L)}_{k}=W^{(L+1)}_{k}\phi'(Z^{(L)}_{k}),                                  \tag{5.5.7}
\]

and descend from \(\ell=L\) to \(2\).  Define

\[
 \sigma_{\ell,kj}
 :=E_\ell[\partial_{\xi_{\ell,j}}\Delta^{(\ell)}_{k}],
 \qquad 0\le j\le k,                                    \tag{5.5.8}
\]

\[
 q^{(\ell-1)}_{k}=\chi_{\ell,k}
   +\sum_{j\le k}\sigma_{\ell,kj}H^{(\ell-1)}_{j}
   +h\sum_{j<k}K_{\ell,jk}H^{(\ell-1)}_{j},                 \tag{5.5.9}
\]

\[
 \Delta^{(\ell-1)}_{k}=q^{(\ell-1)}_{k}\phi'(Z^{(\ell-1)}_{k}).          \tag{5.5.10}
\]

At the bottom set

\[
 Z^{(1)}_{k+1}=Z^{(1)}_{k}+h\Delta^{(1)}_{k}.                                 \tag{5.5.11}
\]

After the terminal forward sweep,

\[
 W^{(L+1)}_{N}=A+h\sum_{j<N}H^{(L)}_{j},\qquad
 F_{N,L}(h)=E_L[W^{(L+1)}_{N}H^{(L)}_{N}].                 \tag{5.5.12}
\]

This is a finite DAG, not a fixed-point definition.  At a given time,
the current \(\xi\)-coordinate is extended in ascending layer order; the
current \(\chi\)-coordinate is then extended in descending layer order.
The source derivative in (5.5.5) or (5.5.8) is computed by initializing its
own source derivative to one, all other source derivatives to zero, and
propagating through earlier assignments while holding all deterministic
response coefficients and covariance entries fixed, with

\[
 D\phi(X)=\phi'(X)DX,\quad D\phi'(X)=\phi''(X)DX,\quad
 D(XY)=XDY+YDX.                                           \tag{5.5.13}
\]

There are finitely many nodes.  Linear growth of \(\phi\), bounded
\(\phi',\phi''\), and Gaussian moments give polynomial Gaussian envelopes
for every value and derivative field.  Therefore all responses in
(5.5.5),(5.5.8) are finite, and the derivative expectations are justified by
dominated convergence.

### 5.6. Response cancellation at every action

Fix one connector and suppress its layer label.  Before an action collect
the old row queries, old column queries, and their raw actions into random
vectors \(\mathsf h,\mathsf c,\mathsf y,\mathsf d\).
These are finite lists of population scalar fields: \(\mathsf h,\mathsf d\)
belong to the input population and \(\mathsf c,\mathsf y\) to the output
population. Their superscript \(T\) transposes only a finite history list;
it is not an adjoint of a population weight operator. The matrices
\(P,S,Q,K,\mathcal R\) below act on these finite history coordinates.
Inductively the
population actions have the form

\[
 \mathsf y=\xi+P\mathsf c,\qquad
 \mathsf d=\chi+S\mathsf h,                               \tag{5.6.1}
\]

where \(P\) is strictly causal and \(S\) is causal.  Put

\[
 Q=\mathbb E[\mathsf h\mathsf h^T],\qquad
 K=\mathbb E[\mathsf c\mathsf c^T].                       \tag{5.6.2}
\]

For any centered, possibly singular Gaussian vector \(X\) and any
\(C^1\) map \(g\) for which both \(g\) and its derivative have
polynomial growth,

\[
 \mathbb E[Xg(X)^T]=\operatorname{Cov}(X)\,
                    \mathbb E[Dg(X)^T].                  \tag{5.6.3}
\]

To prove (5.6.3), write \(X=BZ\) with \(Z\) standard Gaussian, apply
one-dimensional integration by parts to each coordinate of \(Z\), and
use \(BB^T=\operatorname{Cov}(X)\).  The polynomial envelope justifies
the integration by parts even when \(B\) is singular.

Applying (5.6.3) separately to the independent \(\xi\)- and \(\chi\)-blocks
gives the old cross block

\[
 \mathcal R:=\mathbb E[\mathsf c\mathsf y^T]=SQ+KP^T.     \tag{5.6.4}
\]

For a new row query \(H_*\), let

\[
 q=\mathbb E[\mathsf hH_*],\qquad
 \rho=\mathbb E[\nabla_\chi H_*].                        \tag{5.6.5}
\]

Then

\[
 v:=\mathbb E[\mathsf dH_*]=K\rho+Sq.                    \tag{5.6.6}
\]

The population limit of (5.4.6) is

\[
 \mathsf y^TQ^{-1}q+
 \mathsf c^TK^{-1}(v-\mathcal RQ^{-1}q)
 +\text{orthogonal innovation}.                          \tag{5.6.7}
\]

Equations (5.6.4)--(5.6.6) imply

\[
 K^{-1}(v-\mathcal RQ^{-1}q)
 =\rho-P^TQ^{-1}q.                                       \tag{5.6.8}
\]

The \(\mathsf c^TP^TQ^{-1}q\) part of the first term in
(5.6.7) cancels the last term in (5.6.8).  Gaussian regression combines the
remaining old-source regression and orthogonal innovation into the new
source coordinate.  Hence

\[
 x^{(\ell)}_{k}\ \Longrightarrow\
 \xi_{\ell,k}+\sum_{j<k}\rho_{\ell,kj}\Delta^{(\ell)}_{j}.          \tag{5.6.9}
\]

After adjoining that row action, consider a new column query \(C_*\).  Put

\[
 k=\mathbb E[\mathsf cC_*],\qquad
 \sigma=\mathbb E[\nabla_\xi C_*].                       \tag{5.6.10}
\]

Gaussian integration by parts gives

\[
 \omega:=\mathbb E[\mathsf yC_*]=Q\sigma+Pk.                  \tag{5.6.11}
\]

The population limit of (5.4.4) is

\[
 \mathsf d^TK^{-1}k+
 \mathsf h^TQ^{-1}(\omega-\mathcal R^TK^{-1}k)
 +\text{orthogonal innovation}.                          \tag{5.6.12}
\]

Now

\[
 Q^{-1}(\omega-\mathcal R^TK^{-1}k)
 =\sigma-S^TK^{-1}k.                                     \tag{5.6.13}
\]

The last term cancels the \(\mathsf h^TS^TK^{-1}k\) part of
\(\mathsf d^TK^{-1}k\), so

\[
 v^{(\ell-1)}_{k}\ \Longrightarrow\
 \chi_{\ell,k}+\sum_{j\le k}\sigma_{\ell,kj}
                                  H^{(\ell-1)}_{j}.           \tag{5.6.14}
\]

Adding the exact learned terms (5.2.11)--(5.2.12) gives (5.5.6) and (5.5.9).
Lemma 5.4.1 allows every query here to depend on all earlier actions of all
connectors.  Thus (5.6.9)--(5.6.14) include, rather than discard, the dependence
of \(h^{(\ell-1)}_{k}\) on every reused column of \(W^{(\ell)}_0\).

### 5.7. Strict rank for every finite history

Write

\[
 Q_\ell^{[k]}=(\mathbb E H^{(\ell)}_{j}H^{(\ell)}_{q})_{0\le j,q\le k},
 \qquad
 K_\ell^{[k]}=(\mathbb E \Delta^{(\ell)}_{j}\Delta^{(\ell)}_{q})_{0\le j,q\le k}.
                                                                    \tag{5.7.1}
\]

At a forward action, the inverted old-query Grams are
\(Q_{\ell-1}^{[k-1]}\) and \(K_\ell^{[k-1]}\), with the \(Q\)-block
empty at \(k=0\); its row-query Schur complement extends
\(Q_{\ell-1}^{[k-1]}\) to \(Q_{\ell-1}^{[k]}\).  At the subsequent
transpose action, the inverted blocks are \(Q_{\ell-1}^{[k]}\) and
\(K_\ell^{[k-1]}\), and its column-query Schur complement extends
\(K_\ell^{[k-1]}\) to \(K_\ell^{[k]}\).  These statements apply for
\(2\le\ell\le L\); empty blocks are omitted.

We prove the stronger collection needed by the layer-time induction:

\[
 Q_\ell^{[k]}>0\quad(1\le\ell\le L,\ 0\le k\le N),       \tag{5.7.2}
\]

\[
 K_\ell^{[k]}>0\quad(1\le\ell\le L,\ 0\le k<N).        \tag{5.7.3}
\]

Here \(K_1\) is not inverted; including it makes the bottom induction
transparent.

#### 5.7.1. Two elementary facts

If \(g:\mathbb R\to\mathbb R\) is continuous and nonconstant, then

\[
 \operatorname{Var}(g(x+\tau G))>0
 \quad\text{for every }x\in\mathbb R,\ \tau>0.           \tag{5.7.4}
\]

Indeed, zero variance would make \(g\) constant almost everywhere for a
law with a strictly positive density; continuity would make it constant
everywhere.

Second, suppose \(X_0,\ldots,X_{k-1}\) are measurable with respect to
\(\mathcal F\), their second-moment Gram is positive definite, and

\[
 \mathbb E\operatorname{Var}(X_k\mid\mathcal F)>0.        \tag{5.7.5}
\]

Then the Gram of \(X_0,\ldots,X_k\) is positive definite.  For if the
coefficient of \(X_k\) in a linear combination is nonzero, conditioning
leaves strictly positive mean-square residual by (5.7.5); if it is zero, use
the old positive Gram.

#### 5.7.2. Initialization

Let

\[
 \mu_{\phi'}=\mathbb E\phi'(G)^2.                                  \tag{5.7.6}
\]

If \(\phi\) is nonconstant, then \(\mu_{\phi'}>0\).  At time zero every forward
preactivation is standard Gaussian and, by (5.1.2),

\[
 Q_{\ell,00}=1\qquad(1\le\ell\le L).                     \tag{5.7.7}
\]

The time-zero response coefficients vanish by centering of the independent
top weight and the descending centered Gaussian carriers.  Descending from
the top gives

\[
 K_{\ell,00}=\mu_{\phi'}^{L-\ell+1}>0,\qquad 1\le\ell\le L.         \tag{5.7.8}
\]

Also

\[
 \mathbb P\{\phi'(Z^{(1)}_{0})\ne0\}>0                         \tag{5.7.9}
\]

because \(Z^{(1)}_{0}=U\) has full support and \(\phi'\not\equiv0\).

#### 5.7.3. The layer-time induction

Assume at the beginning of forward time \(k\) that
\(Q_1^{[k]}>0\), all \(K_\ell^{[k-1]}>0\) when \(k\ge1\), and

\[
 \mathbb P\{\phi'(Z^{(1)}_{k})\ne0\}>0.                        \tag{5.7.10}
\]

For \(k=0\), these are (5.7.7)--(5.7.9), with the old \(K\)-condition empty.

Ascend through \(\ell=2,\ldots,L\).  Once
\(Q_{\ell-1}^{[k]}>0\), Gaussian regression realizes

\[
 \xi_{\ell,k}=\mu_{\ell,k}(\xi_{\ell,<k})+
                     \tau_{\ell,k}G^{F}_{\ell,k},\qquad
 \tau_{\ell,k}>0,                                       \tag{5.7.11}
\]

Here \(G^{F}_{\ell,k}\sim N(0,1)\) is a scalar innovation independent
of every source revealed earlier, and \(\mu_{\ell,k}\) is the
deterministic linear Gaussian regression map.
All terms in (5.5.6) other than \(\tau_{\ell,k}G^{F}_{\ell,k}\) are measurable
without this innovation.  All older \(H^{(\ell)}_{j}\), \(j<k\), are measurable
there as well.  Conditional on that sigma-field,

\[
 H^{(\ell)}_{k}=\phi(x+\tau_{\ell,k}G^{F}_{\ell,k}).                \tag{5.7.12}
\]

Equations (5.7.4)--(5.7.5) prove \(Q_\ell^{[k]}>0\).  This ascending induction
establishes (5.7.2) at time \(k\) for every layer.  It also shows, for every
\(\ell\ge2\),

\[
 \mathbb P\{\phi'(Z^{(\ell)}_{k})\ne0\}>0,                     \tag{5.7.13}
\]

because conditionally \(Z^{(\ell)}_{k}\) has full support and the nonempty open
set \(\{x:\phi'(x)\ne0\}\) has positive Gaussian probability.

Suppose now \(k<N\).  We first extend the top cotangent Gram.  If \(\phi'\)
is nonconstant, use the same fresh innovation in \(\xi_{L,k}\).  The
quantity \(W^{(L+1)}_{k}\) is measurable without it, and

\[
 \Delta^{(L)}_{k}=W^{(L+1)}_{k}\phi'(x+\tau_{L,k}G^{F}_{L,k}).                     \tag{5.7.14}
\]

Moreover,

\[
 \mathbb P\{W^{(L+1)}_{k}\ne0\}>0.                                 \tag{5.7.15}
\]

For \(k=0\), \(W^{(L+1)}_{0}=A\).  For \(k\ge1\), condition on the chronological
sigma-field immediately before the fresh \(\xi_{L,k-1}\) innovation is
adjoined.  Then

\[
 W^{(L+1)}_{k}=W^{(L+1)}_{k-1}+h\phi(x+\tau_{L,k-1}G^{F}_{L,k-1})               \tag{5.7.16}
\]

has positive conditional variance by (5.7.4), since \(h\ne0\).
On the positive-probability event in (5.7.15), (5.7.4) applied to \(\phi'\)
and (5.7.5) show \(K_L^{[k]}>0\).

The remaining possibility for a nonconstant \(C^1\) activation is that
\(\phi'\) is constant.  Then

\[
 \phi(x)=px+c,\qquad p\ne0.                               \tag{5.7.17}
\]

The scalar \(K_{L,00}=p^2\) is positive.  For \(k\ge1\), condition as in
(5.7.16).  Since \(\Delta^{(L)}_{k}=pW^{(L+1)}_{k}\), its fresh innovation is

\[
 hp^2\tau_{L,k-1}G^{F}_{L,k-1},                               \tag{5.7.18}
\]

whose conditional variance is \(h^2p^4\tau_{L,k-1}^2>0\).
All old \(\Delta^{(L)}_{j}\), \(j<k\), exclude this innovation.  Thus (5.7.5) again
proves \(K_L^{[k]}>0\).  This is the affine branch; it is not covered by
an appeal to nonconstancy of \(\phi'\).

Now descend through \(\ell=L-1,L-2,\ldots,1\).  Once
\(K_{\ell+1}^{[k]}>0\), write the current source as

\[
 \chi_{\ell+1,k}=\widetilde \mu_{\ell,k}(\chi_{\ell+1,<k})
                   +\upsilon_{\ell,k}G_{\ell,k},\qquad
 \upsilon_{\ell,k}>0.                                   \tag{5.7.19}
\]
Here \(G_{\ell,k}\sim N(0,1)\) is the fresh descending innovation and
\(\widetilde\mu_{\ell,k}\) is a deterministic linear regression map.

The current forward field \(Z^{(\ell)}_{k}\), every old \(\Delta^{(\ell)}_{j}\), and all
other terms in \(q^{(\ell)}_{k}\) are measurable without \(G_{\ell,k}\).
Consequently

\[
 \Delta^{(\ell)}_{k}=(x+\upsilon_{\ell,k}G_{\ell,k})
                           \phi'(Z^{(\ell)}_{k}).               \tag{5.7.20}
\]

The multiplier is nonzero with positive probability by (5.7.13) for
\(\ell\ge2\), and by (5.7.10) for \(\ell=1\).  Therefore

\[
 \mathbb E\operatorname{Var}(\Delta^{(\ell)}_{k}\mid\mathcal F)>0,
\]

and (5.7.5) proves \(K_\ell^{[k]}>0\).  This completes the backward rank
induction.

Finally, use the current \(\chi_{2,k}\) innovation in
\(Z^{(1)}_{k+1}=Z^{(1)}_{k}+h\Delta^{(1)}_{k}\).  Without that innovation,

\[
 H^{(1)}_{k+1}
 =\phi\!\left(x+h\upsilon_{1,k}\phi'(Z^{(1)}_{k})G_{1,k}\right).
                                                                    \tag{5.7.21}
\]

On the event in (5.7.10), the Gaussian coefficient is nonzero.  Equations
(5.7.4)--(5.7.5) give \(Q_1^{[k+1]}>0\).  On the same event the argument of
\(\phi\) in (5.7.21) has full support, so the nonempty open set
\(\{x:\phi'(x)\ne0\}\) is hit with positive conditional probability.
Hence

\[
 \mathbb P\{\phi'(Z^{(1)}_{k+1})\ne0\}>0.                    \tag{5.7.22}
\]

This supplies the induction hypotheses at time \(k+1\).  Starting from
Section 5.7.2 and iterating for \(k=0,\ldots,N-1\) proves (5.7.2)--(5.7.3).
Every Schur complement used to create a new source coordinate is therefore
strictly positive.  The proof is pointwise on the entire punctured
\(h\)-line and uses no small-step expansion.

### 5.8. Complete empirical conditioning ledger

For connector \(\ell\), distinguish the cross block before the forward
action from the enlarged block before the backward action:

\[
 \mathcal R_{\ell,k}^{F,(n)}
 ={1\over n}(\delta^{(\ell)}_{<k})^Tx^{(\ell)}_{<k}
 ={1\over n}(v^{(\ell-1)}_{<k})^Th^{(\ell-1)}_{<k}.           \tag{5.8.1}
\]

The equality is the exact matrix identity
\((\delta^{(\ell)}_{<k})^TW^{(\ell)}_0 h^{(\ell-1)}_{<k}/n\)
written in two ways.  After \(\mathsf F_{k,\ell}\), the row-query block
has one additional column, so

\[
 \begin{aligned}
 \mathcal R_{\ell,k}^{B,(n)}
 &={1\over n}(\delta^{(\ell)}_{<k})^Tx^{(\ell)}_{\le k}
   ={1\over n}(v^{(\ell-1)}_{<k})^Th^{(\ell-1)}_{\le k}\\
 &=\left[\mathcal R_{\ell,k}^{F,(n)},
 {1\over n}(v^{(\ell-1)}_{<k})^Th^{(\ell-1)}_{k}\right].       
 \end{aligned} \tag{5.8.1a}
\]

Thus the extra column in the backward cross block is exactly the second
query cross-moment already formed for the forward action; it is not
dropped.

At \(\mathsf F_{k,\ell}\), the full list of new regression data is

\[
 {1\over n}(h^{(\ell-1)}_{<k})^Th^{(\ell-1)}_{k},\qquad
 {1\over n}(v^{(\ell-1)}_{<k})^Th^{(\ell-1)}_{k},\qquad
 {1\over n}\|h^{(\ell-1)}_{k}\|_2^2,\qquad
 \mathcal R_{\ell,k}^{F,(n)},                            \tag{5.8.2}
\]

together with the old feature and cotangent Grams.  At
\(\mathsf B_{k,\ell}\), it is

\[
 {1\over n}(\delta^{(\ell)}_{<k})^T\delta^{(\ell)}_{k},\qquad
 {1\over n}(x^{(\ell)}_{\le k})^T\delta^{(\ell)}_{k},\qquad
 {1\over n}\|\delta^{(\ell)}_{k}\|_2^2,\qquad
 \mathcal R_{\ell,k}^{B,(n)},                            \tag{5.8.3}
\]

together with \(Q_{\ell-1}^{[k]}\) and \(K_\ell^{[k-1]}\).  Equations
(5.8.2)--(5.8.3), over precisely the index set (5.3.1)--(5.3.3), contain every
empirical quantity in (5.4.4)--(5.4.7).  No mixed-connector Gram is inverted.

### 5.9. Joint coupling, concentration, and stopping

Set

\[
 \mathcal A=(2N+1)(L-1),\qquad \Lambda=3\mathcal A+1.     \tag{5.9.1}
\]

The following explicit micro-ledger has at most \(\Lambda\) entries.
First construct the initialization marks, \(h^{(1)}_{0}\), and their empirical
moments.  For each action in (5.3.5), in order:

1. perform the Gaussian matrix action;
2. perform every coordinate assignment made possible by it (including
   the top cotangent after \(\mathsf F_{k,L}\), the lower update after
   \(\mathsf B_{k,2}\), and the terminal output after
   \(\mathsf F_{N,L}\));
3. form every pair moment in (5.8.2)--(5.8.3) needed by the next action.

Empty bundles count as one harmless entry.  Thus there are at most one
initial entry plus three for each of the exactly \(\mathcal A\) actions,
which proves (5.9.1).

#### 5.9.1. Ideal coordinate arrays

For each physical layer use iid coordinate copies of the following scalar
marks:

\[
 \begin{array}{c|c}
 \text{physical layer}&\text{marks}\\
 \hline
 1&U,\chi_2\\
 1<\ell<L&\xi_\ell,\chi_{\ell+1}\\
 L&\xi_L,A.
 \end{array}                                               \tag{5.9.2}
\]

Arrays belonging to different physical layers are independent.  Within a
layer, the same coordinate is reused through time with the covariance in
(5.5.2)--(5.5.3).  This retains every within-coordinate temporal dependence,
while coordinates within one physical population are iid.

Here is the action-by-action extension, including the alternating physical
layers.  At \(\mathsf F_{k,\ell}\), after the ideal query
\(\bar h^{(\ell-1)}_{k}\) and \(Q_{\ell-1}^{[k]}\) have been formed, write

\[
 \begin{cases}
 \alpha_{\ell,0}^{\xi}=0,\quad
       (\tau_{\ell,0}^{\xi})^2=Q_{\ell-1,00},&k=0,\\[2mm]
 \alpha_{\ell,k}^{\xi}
 =Q_{\ell-1,k,<k}(Q_{\ell-1}^{[k-1]})^{-1},\quad
 (\tau_{\ell,k}^{\xi})^2
 =Q_{\ell-1,kk}
  -Q_{\ell-1,k,<k}(Q_{\ell-1}^{[k-1]})^{-1}
     Q_{\ell-1,<k,k},&k\ge1.
 \end{cases}                                             \tag{5.9.2a}
\]

For the \(i\)-coordinates of physical layer \(\ell\), take a fresh iid Gaussian vector
\(g_{\mathsf F_{k,\ell}}\) and set

\[
 \bar\xi_{\ell,k}
 =\alpha_{\ell,k}^{\xi}\bar\xi_{\ell,<k}
   +\tau_{\ell,k}^{\xi}g_{\mathsf F_{k,\ell}}.             \tag{5.9.2b}
\]

Use this coordinate in (5.5.6), then make the coordinate and moment bundles
before the next action.  At \(\mathsf B_{k,\ell}\), after
\(\bar \delta^{(\ell)}_{k}\) and \(K_\ell^{[k]}\) have been formed, put

\[
 \begin{cases}
 \alpha_{\ell,0}^{\chi}=0,\quad
       (\tau_{\ell,0}^{\chi})^2=K_{\ell,00},&k=0,\\[2mm]
 \alpha_{\ell,k}^{\chi}
 =K_{\ell,k,<k}(K_\ell^{[k-1]})^{-1},\quad
 (\tau_{\ell,k}^{\chi})^2
 =K_{\ell,kk}
  -K_{\ell,k,<k}(K_\ell^{[k-1]})^{-1}K_{\ell,<k,k},&k\ge1.
 \end{cases}                                             \tag{5.9.2c}
\]

For the \(j\)-coordinates of physical layer \(\ell-1\), take a fresh iid vector
\(g_{\mathsf B_{k,\ell}}\) and set

\[
 \bar\chi_{\ell,k}
 =\alpha_{\ell,k}^{\chi}\bar\chi_{\ell,<k}
   +\tau_{\ell,k}^{\chi}g_{\mathsf B_{k,\ell}}.            \tag{5.9.2d}
\]

Use it in (5.5.9), then make the next coordinate and moment bundles.
All vectors \(g_{\mathsf F_{k,\ell}},g_{\mathsf B_{k,\ell}}\), over the
exact order (5.3.5), are mutually independent and independent of the initial
arrays.  At the matching raw action use that same fresh vector for the
conditional residual in Lemma 5.4.1.  Conditional independence of the
remaining matrix residuals makes this simultaneous even when the next
action belongs to another connector or the opposite physical layer.
Induction over (5.3.5), integrating the exact next-action kernel against the
already matched past law, proves that the raw side of this one coupling has
exactly the joint law of the network in Section 5.2.

#### 5.9.2. Spectral stopping

By Section 5.7, the finite list of population old-query Grams and
query Schur complements is strictly positive.  Define

\[
 4\gamma_{L,N,h}=\min\{1,\lambda_{\min}(G),v:\
 G\text{ is inverted and }v\text{ is a source Schur complement in the
 chronology}\}>0.                                        \tag{5.9.3}
\]

The terminal forward innovations are included.  Immediately before an
action, first test that every required empirical old Gram has least
eigenvalue at least \(2\gamma_{L,N,h}\).  Only on that branch evaluate its
Schur formula, then test that every new empirical innovation variance is at
least \(2\gamma_{L,N,h}\).  This defines a predictable good event and
never evaluates the inverse of a failed Gram.

On the good event use the exact coefficients and projected residual in
(5.4.4) or (5.4.6).  Off it, replace all coefficients and innovation scales by
their deterministic population values and replace the residual projection
by the identity.  These are the *extended* actions.  The raw network is not
altered.  Formally, set \(\mathcal G_{-1}=\Omega\) and let
\(\mathcal G_q\) be \(\mathcal G_{q-1}\) intersected with the tests first
needed at action \(q\).  On \(\mathcal G_{q-1}\), the raw and extended
histories agree before the tests, so the event is simultaneously an event
of either history. Generate the raw action on every event from the exact
Moore--Penrose conditional kernel in Lemma 5.4.1, sharing the fresh Gaussian
vector with the extended and ideal actions as specified above. Thus the
extension is only a coupling device and never changes the raw law.

#### 5.9.3. Three estimates

Every finite vector norm \(\|\cdot\|_p\) is the ordinary
Euclidean-coordinate \(\ell^p\) norm, not a normalized norm. For
\(x\in\mathbb R^n\) and \(p\ge1\), its explicitly scaled value is

\[
 \frac{\|x\|_{p}}{n^{1/(p)}}=\left(\frac1n\sum_{i=1}^n|x_i|^p\right)^{1/p}.
 \tag{5.9.3a}
\]

We need only even integer moment orders. Let \(\nu\ge2\) be even,
and let \(Y_1,\ldots,Y_n\) be iid centered real variables with
\(\mathbb E|Y_1|^\nu<\infty\). Expand
\[
 \mathbb E\left|\frac1n\sum_{i=1}^nY_i\right|^\nu
 =n^{-\nu}\sum_{i_1,\ldots,i_\nu=1}^n
                 \mathbb E\prod_{a=1}^{\nu}Y_{i_a}.
\]
A summand with an index occurring exactly once is zero by independence
and centering. Every remaining index tuple has at most \(\nu/2\)
distinct indices. Partitioning the \(\nu\) positions into their equal-index
classes shows that there are at most
\(\sum_{b=1}^{\nu/2}C_{\nu,b}n^b\le C_\nu n^{\nu/2}\)
such tuples. For a tuple with class sizes \(a_1,\ldots,a_b\), independence
and the moment inequality
\(\mathbb E|Y_1|^{a_j}\le(\mathbb E|Y_1|^\nu)^{a_j/\nu}\)
bound the absolute expectation by \(\mathbb E|Y_1|^\nu\), since
\(\sum_j a_j=\nu\). Thus the expansion is at most
\(C_\nu n^{-\nu/2}\mathbb E|Y_1|^\nu\). Taking its \(\nu\)-th root proves

\[
 \left\|{1\over n}\sum_{i=1}^nY_i\right\|_{L^\nu}
 \le C_{\nu}n^{-1/2}\|Y_1\|_{L^\nu}.                            \tag{5.9.4}
\]

If finite fields \(x_n,y_n\in\mathbb R^n\) are coupled to the iid
coordinate arrays \(\bar x,\bar y\), coordinate Cauchy--Schwarz,
Holder on the coupling probability space, and (5.9.4) give

\[
 \begin{aligned}
 &\left\|{1\over n}x_n^Ty_n-\mathbb E\bar x_1\bar y_1
       \right\|_{L^\nu}\\
 &\quad\le
 \left\|\frac{\|x_n-\bar x\|_{2\nu}}{n^{1/(2\nu)}}\right\|_{L^{2\nu}}
 \left\|\frac{\|y_n\|_{2\nu}}{n^{1/(2\nu)}}\right\|_{L^{2\nu}}\\
 &\qquad+
 \left\|\frac{\|\bar x\|_{2\nu}}{n^{1/(2\nu)}}\right\|_{L^{2\nu}}
 \left\|\frac{\|y_n-\bar y\|_{2\nu}}{n^{1/(2\nu)}}\right\|_{L^{2\nu}}
 +C_{\nu}n^{-1/2}\|\bar x_1\bar y_1\|_{L^\nu}.                
 \end{aligned} \tag{5.9.5}
\]

Thus field errors \(O(n^{-1/2})\) at order \(2\nu\) imply the same rate for
every empirical entry in (5.8.2)--(5.8.3) at order \(\nu\).

For a matrix action, on the good event the inverse identity

\[
 A^{-1}-B^{-1}=A^{-1}(B-A)B^{-1}                          \tag{5.9.6}
\]

gives the following explicit coefficient estimate.  Let \(\delta_n\) be
the maximum error of all Gram and cross-moment entries in (5.8.2) or (5.8.3),
and let \(\mathcal Z_n\) be one plus the sum of their absolute values and
their population counterparts.  Expanding (5.4.4) or (5.4.6), replacing one
factor at a time, and using the good-event inverse bound gives

\[
 \max_j|\alpha_{j,n}-\alpha_j|
   +|\tau_n^2-\tau^2|
 \le C_{L,N,h}\mathcal Z_n^2\delta_n.                    \tag{5.9.6a}
\]

For example, the longest coefficient is
\(K_n^{-1}\mathcal R_nQ_n^{-1}q_n\); its difference is the sum of the
four terms obtained by replacing \(K_n^{-1},\mathcal R_n,Q_n^{-1},q_n\)
in turn, with each inverse replacement controlled by (5.9.6).  The other
coefficients have fewer factors.  The Schur expression for
\(\tau_n^2\) has at most two unbounded moment factors.  On the good event
both inverse factors are bounded deterministically, so no term contains
more than two factors from \(\mathcal Z_n\); this proves (5.9.6a), rather
than leaving the replacement implicit.  Since empirical and population
innovation variances are at least \(2\gamma_{L,N,h}\),

\[
 |\sqrt{x}-\sqrt y|
 \le {1\over2\sqrt{2\gamma_{L,N,h}}}|x-y|.                \tag{5.9.7}
\]

The Schur complement is a squared orthogonal-residual norm, so
\(0\le\tau_n^2\le n^{-1}\|q_*\|_2^2\) (and similarly for a column
query).  Thus preceding query moments also bound every moment of
\(\tau_n\); no upper spectral stopping is required.

If \(V\) has at most \(N+1\) old query columns,
\(\lambda_{\min}(V^TV/n)\ge2\gamma_{L,N,h}\), and
\(g\sim N(0,I_n)\) is conditionally fresh, then

\[
 \left(\mathbb E_g\frac{\|P_Vg\|_{\nu}^{\nu}}{n}\right)^{1/\nu}
 \le C_{\nu,N,\gamma}n^{-1/2}
              \sum_j\frac{\|V_j\|_{\nu}}{n^{1/(\nu)}}.                       \tag{5.9.8}
\]

Indeed, the coefficient vector in
\(P_Vg=V(V^TV/n)^{-1}(V^Tg/n)\) is conditionally Gaussian with covariance
\((V^TV/n)^{-1}/n\).  It remains to combine these estimates without
hiding any field-error term.

To display every error term, write either row or column action on the good
event in the common form

\[
 T_n=\sum_{j=1}^J\alpha_{j,n}V_{j,n}
             +\tau_nP_{\mathcal S_n}^{\perp}g,\qquad
 \bar T=\sum_{j=1}^J\alpha_j\bar V_j+\tau g,              \tag{5.9.8a}
\]

where \(J<\infty\) is the number of old-span fields, distinct from the
input dimension \(d=1\), and the finite vectors \(V_j\) include the old raw actions and old
queries appearing in (5.4.4) or (5.4.6), and
\(\mathcal S_n\) is the old opposite-query span.  With the same fresh
\(g\),

\[
 \begin{aligned}
 T_n-\bar T
 ={}&\sum_j\alpha_{j,n}(V_{j,n}-\bar V_j)
   +\sum_j(\alpha_{j,n}-\alpha_j)\bar V_j\\
  &+(\tau_n-\tau)g-\tau_nP_{\mathcal S_n}g.              
 \end{aligned} \tag{5.9.8b}
\]

The first line contains, separately, the preceding-query/old-action errors
and the old-span coefficient errors.  The second line contains the scale
error and the removed finite-dimensional projection.  Holder, (5.9.6a),
(5.9.7), and (5.9.8) bound the four terms in (5.9.8b), respectively, by
\(Cn^{-1/2}\), \(Cn^{-1/2}\), \(Cn^{-1/2}\), and \(Cn^{-1/2}\) in
the explicit mixed quantity
\(\left(\mathbb E[n^{-1}\sum_{i=1}^n|T_{n,i}-\bar T_i|^\nu]\right)^{1/\nu}\),
provided the preceding field and empirical
errors and moments are available at order \(8\nu\).  Thus

\[
 \text{input errors at order }8\nu
 \quad\Longrightarrow\quad
 \text{new action error at order }\nu\text{ is }O(n^{-1/2}). \tag{5.9.9}
\]

Off the good event, the extended and ideal Gaussian terms use identical
population coefficients and the same full \(g\); their difference contains
only preceding extended-field errors.  Hence (5.9.9) holds globally for the
extended action, without an empirical inverse off the good event.

#### 5.9.4. The finite moment tower

For any requested terminal moment order, choose an even integer
\(\nu_*\ge2\) at least as large as that order, and set

\[
 R_\Lambda=\nu_*,\qquad R_{j-1}=8R_j\quad(1\le j\le\Lambda).
                                                                    \tag{5.9.10}
\]

Thus \(R_0=8^\Lambda \nu_*<\infty\), and every order in the tower is
even. The factors \(2,4,8\) used below preserve evenness, so the
even-moment expansion (5.9.4) applies at every invocation.  A coordinate bundle consumes at most
order \(4\nu\): its nonlinear products are an empirical scalar times a
field, and a scalar coordinate \(u\) times \(\phi'(z)\).
For the latter use
\[
 |u\phi'(z)-\widetilde u\phi'(\widetilde z)|
 \le M|u-\widetilde u|+M|\widetilde u|\,|z-\widetilde z|;
\]
the coordinate \(u\) here is either a readout or an incoming backsignal,
not a separate network parameter. For an empirical-scalar product use
\(cv-\widetilde c\widetilde v
=c(v-\widetilde v)+(c-\widetilde c)\widetilde v\).
Holder bounds these products using the preceding moments at order
\(4\nu\); the remaining activation assignments are Lipschitz by (5.1.1).
The terminal readout-times-feature average is also a pair product and is
bounded by coordinate Cauchy--Schwarz followed by Holder at these orders.
A pair-moment bundle consumes order \(2\nu\)
by (5.9.5), and a matrix action consumes order \(8\nu\) by (5.9.9).  Therefore
(5.9.10) supplies every moment used by each of the at most \(\Lambda\)
microsteps.

At the initial microstep the marks are Gaussian and \(\phi\) has linear
growth, so moment \(R_0\) is finite.  Applying, in the exact order of the
micro-ledger, the coordinate estimate, (5.9.5), and (5.9.9) proves for every
microstep \(j\), every fixed even \(\nu\ge2\),

\[
 \sup_n\mathcal M_{j,\nu}(n)<\infty,
 \qquad \mathcal E_{j,\nu}(n)\le C_{j,\nu}n^{-1/2},           \tag{5.9.11}
\]

where \(\mathcal M\) is the maximum moment of all extended fields and
observables already constructed and \(\mathcal E\) is their maximum
extended-to-ideal error.  This is a literal induction over the explicitly
indexed list of at most \(3(2N+1)(L-1)+1\) entries; (5.9.10) shows that it
terminates and does not hide an all-orders assumption. Smaller real
orders follow by Holder: both the coordinate averaging measure
\(n^{-1}\sum_i\delta_i\) and the coupling law are probability measures.
Choosing \(\nu_*\ge\max\{p,P,2\}\) therefore controls every requested
mixed order \(p,P\).

On the good branch every empirical regression coefficient is one of the
finite rational expressions (5.4.4)--(5.4.7); off it the extended coefficient
is its population value.  Equations (5.9.6)--(5.9.11), at arbitrary finite
moment order, therefore also prove convergence of every extended
coefficient in every finite \(L^\nu\).  Taking any larger order than one
gives its uniform integrability.

For a requested integer failure exponent \(b\ge1\), run (5.9.10) with
\(\nu_*=2b\). For symmetric finite matrices,
\(|\lambda_{\min}(A)-\lambda_{\min}(B)|\le\|A-B\|_{\rm op}\):
write the least eigenvalue as the minimum of the quadratic form over
unit vectors and bound each difference by the operator norm.
The matrix dimensions in the history list are fixed, so entry errors
bound this operator-norm error. Before the first failed test, a Gram
whose population eigenvalue is at least \(4\gamma_{L,N,h}\) can fall
below \(2\gamma_{L,N,h}\) only if a Gram error exceeds a fixed positive
threshold. If the Gram tests pass, (5.9.6a) gives the analogous estimate
for the new Schur variance. Equation (5.9.11) at order \(2b\) and
Markov's inequality therefore bound the probability of each first
failure by \(C_b n^{-b}\).  A union bound over the exactly
\(\mathcal A\) actions gives

\[
 \mathbb P(\text{stopping occurs})
 \le C_{L,N,h,M,b}n^{-b}.                                \tag{5.9.12}
\]

The largest initialization moment used for this assertion is explicitly

\[
 2b\,8^{3(2N+1)(L-1)+1}.                                \tag{5.9.13}
\]

### 5.10. Removing stopping and terminal uniform integrability

We now bound the original raw network on every event, without any
empirical Gram inverse. The hats below are nonnegative scalar polynomial
majorants, not new names for normalized norms or population fields. They
will satisfy
\[
 \frac{\|W^{(L+1)}_k\|_2}{\sqrt n}\le\widehat a_k,\qquad
 \frac{\|z^{(1)}_k\|_2}{\sqrt n}\le\widehat u_k,\qquad
 \|W^{(\ell)}_k\|_{\rm op}\le\widehat m_{\ell,k}.        \tag{5.10.1}
\]
Put \(h_{\rm abs}=|h|\). Form the following finite deterministic
majorant recursion for \(0\le k<N\):

\[
 \widehat h_{1,k}=M(1+\widehat u_k),                      \tag{5.10.2}
\]

\[
 \widehat z_{\ell,k}=\widehat m_{\ell,k}
                         \widehat h_{\ell-1,k},\qquad
 \widehat h_{\ell,k}=M(1+\widehat z_{\ell,k}),
 \quad \ell=2,\ldots,L,                                  \tag{5.10.3}
\]

\[
 \widehat c_{L,k}=M\widehat a_k,                         \tag{5.10.4}
\]

\[
 \widehat b_{\ell-1,k}=\widehat m_{\ell,k}
                         \widehat c_{\ell,k},\qquad
 \widehat c_{\ell-1,k}=M\widehat b_{\ell-1,k},
 \quad \ell=L,\ldots,2,                                  \tag{5.10.5}
\]

\[
 \begin{aligned}
 \widehat a_{k+1}&=\widehat a_k+h_{\rm abs}\widehat h_{L,k},\\
 \widehat u_{k+1}&=\widehat u_k+h_{\rm abs}\widehat c_{1,k},\\
 \widehat m_{\ell,k+1}&=\widehat m_{\ell,k}
      +h_{\rm abs}\widehat c_{\ell,k}\widehat h_{\ell-1,k}.
 \end{aligned}                                             \tag{5.10.6}
\]

Initialize

\[
 \widehat a_0=\widehat u_0=\widehat m_{\ell,0}=\mathfrak R_n,
 \qquad 2\le\ell\le L,                                  \tag{5.10.7a}
\]

where

\[
 \mathfrak R_n=1+\frac{\|W^{(L+1)}_{0}\|_{2}}{\sqrt n}+\frac{\|z^{(1)}_{0}\|_{2}}{\sqrt n}
       +\sum_{\ell=2}^L\|W^{(\ell)}_{0}\|_{\mathrm{op}}, \tag{5.10.7}
\]

and after the last update perform only the terminal forward recursion
(5.10.2)--(5.10.3) at \(k=N\).  Let \(P_{L,N,h,M}(\mathfrak R_n)\) be one plus
the sum of every hatted variable in this finite list.  It is an explicitly
constructed polynomial with nonnegative coefficients.  Direct use of
Cauchy--Schwarz, \(\frac{\|\phi(x)\|_{2}}{\sqrt n}\le M(1+\frac{\|x\|_{2}}{\sqrt n})\), and

\[
 \left\|{h\over n}xy^T\right\|_{\mathrm{op}}
 \le h_{\rm abs}\frac{\|x\|_{2}}{\sqrt n}\frac{\|y\|_{2}}{\sqrt n}                             \tag{5.10.8}
\]

proves, inductively in the displayed order, that
\(\widehat h_{\ell,k},\widehat z_{\ell,k},
\widehat c_{\ell,k},\widehat b_{\ell,k}\)
bound the corresponding finite field's ordinary Euclidean norm divided
by \(\sqrt n\). The weight bounds are (5.10.1).
The same polynomial bounds the initialization actions (5.2.9):
\(\|W^{(\ell)}_0\|_{\rm op}\le\widehat m_{\ell,k}\),
so the forward and backward action bounds are already dominated by
\(\widehat z_{\ell,k}\) and \(\widehat b_{\ell-1,k}\).

For a standard Gaussian vector \(g\), Jensen gives
\(\mathbb E(\|g\|_2/\sqrt n)^q\le\mathbb E|G|^q\) for \(q\ge2\);
smaller positive orders follow by Holder. All scalar Gaussian moments
are finite by direct integration against \(e^{-x^2/2}\).

The ordinary operator norm of a matrix with iid \(N(0,1/n)\) entries
also has every uniform moment. To see this, let \(G_n\) have iid
\(N(0,1)\) entries. A maximal \(1/4\)-separated subset of the unit sphere
is a \(1/4\)-net with at most \(9^n\) points: its disjoint radius-\(1/8\)
balls lie in a radius-\(9/8\) ball, and comparison of volumes gives the
bound. Approximating both unit vectors in a bilinear form yields
\(\|G_n\|_{\rm op}\le2\max_{u,v\text{ in the net}}|u^TG_nv|\).
Each fixed bilinear form is a standard Gaussian. Its tail is bounded
by \(2e^{-t^2/2}\), obtained from
\(\mathbb E e^{\lambda G}=e^{\lambda^2/2}\), Markov's inequality and
\(\lambda=t\), then applying the same argument to \(-G\).
A union bound therefore gives

\[
 \mathbb P\{\|G_n\|_{\mathrm{op}}/\sqrt n>y\}
 \le2\exp\{n\log81-ny^2/8\},                             \tag{5.10.9}
\]

For \(y^2\ge16\log81\) the last bound is at most
\(2e^{-ny^2/16}\le2e^{-y^2/16}\). Integrating
\(q\int_0^\infty y^{q-1}\mathbb P\{X>y\}\,dy=\mathbb E X^q\)
for the nonnegative norm \(X\) proves the uniform moment claim.
Consequently, since the majorant is a fixed finite polynomial,

\[
 \sup_n\mathbb E\mathfrak R_n^q<\infty
 \quad\text{and}\quad
 \sup_n\mathbb E P_{L,N,h,M}(\mathfrak R_n)^q<\infty
 \qquad(q<\infty).                                       \tag{5.10.10}
\]

For \(p\ge2\),

\[
 \frac{\|x\|_{p}}{n^{1/(p)}}\le n^{1/2-1/p}\frac{\|x\|_{2}}{\sqrt n};                \tag{5.10.11}
\]

For \(1\le p\le2\), the coordinate probability-measure inequality
instead gives \(\|x\|_p/n^{1/p}\le\|x\|_2/\sqrt n\).
Fix desired mixed orders \(1\le p,P<\infty\), choose an even integer
\(\nu\ge\max\{p,P,2\}\), and use (5.9.12) with the integer
\(b=2\nu\). Holder,
(5.10.10)--(5.10.11), and \(1/2-1/p\le1/2\) give, for every raw field,

\[
 \begin{aligned}
 \left\|\frac{\|x_n\|_{p}}{n^{1/(p)}}\mathbf1_{\{\mathrm{stop}\}}
       \right\|_{L^P}
 &\le C n^{(1/2-1/p)_+}
       \mathbb P(\mathrm{stop})^{1/(2P)}\\
 &\le Cn^{(1/2-1/p)_+-\nu/P}=o(1).                         
 \end{aligned} \tag{5.10.12}
\]

On the complement, raw and extended fields agree.  Extended and ideal
fields have the required moments by (5.9.10)--(5.9.11), so their stopped-event
pieces also vanish by Holder and the vanishing event probability.
This removes stopping from every field. The finite inequality
\(|x^Ty|/n\le(\|x\|_2/\sqrt n)(\|y\|_2/\sqrt n)\)
and the same polynomial majorant remove it from all Grams
and cross-moments in (5.8.2)--(5.8.3).

Finally,

\[
 |f_{n,L}^N|
 \le \frac{\|W^{(L+1)}_{N}\|_{2}}{\sqrt n}\frac{\|h^{(L)}_{N}\|_{2}}{\sqrt n}
 \le P_{L,N,h,M}(\mathfrak R_n)^2.                         \tag{5.10.13}
\]

Equation (5.10.10) bounds the right side in every finite moment, so the
terminal outputs are uniformly integrable.  The coupled field convergence
and an iid law of large numbers for the ideal top-layer coordinates give

\[
 f_{n,L}^N-\frac1n\sum_{i=1}^n
          \overline W^{(L+1)}_{N,i}\,\bar h^{(L)}_{N,i}
 \longrightarrow0\quad\text{in }L^1.                    \tag{5.10.14}
\]

The ideal summands are iid and have expectation \(F_{N,L}(h)\).  Taking
expectations proves (5.1.3).  Every empirical Gram and raw cross-moment is
bounded by a product of two explicitly scaled Euclidean field norms
\(\|x\|_2/\sqrt n\) and \(\|y\|_2/\sqrt n\), hence is uniformly
integrable as well.

### 5.11. Conclusion of the fixed-program proof

For every fixed finite \((L,N)\) and every fixed \(h\ne0\), Sections
5.2--5.10 establish the following for the exact finite-step feature-ascent network:

1. the exact \((2N+1)(L-1)\) predictable action chronology;
2. the adaptive reused-row/reused-column Gaussian conditional law across
   all independently initialized matrices;
3. every response cancellation, including current features that depend on
   earlier transpose actions of the same reused matrix;
4. strict full history rank for every nonconstant activation, with the
   affine top-cotangent branch treated separately;
5. convergence and uniform integrability of every empirical conditioning
   quantity and terminal output, with the explicit finite moment tower
   (5.9.10)--(5.9.13);
6. pointwise fixed-\(h\) identification with the inverse-free Gaussian program.

The proof uses no finite-width Taylor expansion, no interchange of the
width and step-size limits, and no unproved state-evolution induction.

## 6. Scope and obstructions to stronger calculus claims

**No full same-norm product closure with an unbounded atom.** Let
\(\mathfrak X\) be a normed space of random variables containing an
essentially unbounded \(X\) and all its powers. Suppose, for fixed
\(1\le p<\infty\) and \(A,C>0\),
\(\|V\|_{L^p}\le A\|V\|_{\mathfrak X}\) and
\(\|UV\|_{\mathfrak X}\le C\|U\|_{\mathfrak X}\|V\|_{\mathfrak X}\).
Iteration and the identity
\(\|X^k\|_{L^p}=\|X\|_{L^{kp}}^k\) give
\[
 \|X\|_{L^{kp}}
 \le A^{1/k}C^{1-1/k}\|X\|_{\mathfrak X}.               \tag{6.1}
\]
The right side is bounded. For any \(B>0\), essential unboundedness gives
\(\mathbb P(|X|>B)>0\), and
\(\|X\|_{L^q}\ge B\,\mathbb P(|X|>B)^{1/q}\).
Letting \(q\to\infty\), then \(B\to\infty\), contradicts (6.1).
In particular a nondegenerate Gaussian atom cannot belong to such a full same-space
algebra. For a derivative-sum norm containing constants, the zero-order
weight must be positive; if its exponent is finite it supplies the
embedding used here, and if it is infinity it already excludes the
unbounded atom. This obstruction does not apply to the finite,
order-consuming moment estimates of Section 5.

**Independent coefficientwise jet obstruction.** On the unrestricted
space of finitely supported ordinary-derivative jets
\(u=(u_j)_{j\ge0}\), let
\(\|u\|_w=\sum_{j\ge0}w_j|u_j|\), with every \(w_j>0\).
Suppose both the shift \((Su)_j=u_{j+1}\) and the Leibniz product
\((u\star v)_j=\sum_{i=0}^j\binom ji u_i v_{j-i}\)
have fixed bounds \(C_S\) and \(C_P\) in this same norm.
Testing the shift on the unit jet \(e_j\), and the product on
\(e_1,e_{j-1}\), gives, for every \(j\ge2\),
\[
 w_{j-1}\le C_Sw_j,\qquad
 j w_j\le C_Pw_1w_{j-1},\qquad
 j\le C_PC_Sw_1,                                      \tag{6.2}
\]
which is impossible. For factorial-normalized derivatives the product
loses its binomial factor but the shift becomes
\((Su)_j=(j+1)u_{j+1}\); the same tests again give (6.2)'s final
contradiction. This statement concerns unrestricted positive
coefficientwise majorants, not an arbitrary restricted class of
expressions with cancellations.

**Zero Taylor radius does not exclude a smooth nonsingular ODE.** For
a standard Gaussian \(G\), put \(g(t)=\mathbb E(1+t^2G^2)^{-1}\).
Every derivative of \(\psi(u)=(1+u^2)^{-1}\) is bounded on the real
line: repeated differentiation gives a rational function without a
real pole that tends to zero at infinity. The integrable bound
\(|G|^j\|\psi^{(j)}\|_\infty\) therefore justifies every derivative
under the expectation, so \(g\in C^\infty(\mathbb R)\). At zero,
\[
 \frac{g^{(2k)}(0)}{(2k)!}
   =(-1)^k\mathbb E G^{2k}=(-1)^k(2k-1)!!,\qquad
 g^{(2k+1)}(0)=0.                                     \tag{6.3}
\]
The even derivative identity follows from the finite geometric expansion
of \((1+u^2)^{-1}\); the Gaussian moment recurrence follows by integration
by parts, as in Section 4. Consecutive nonzero Taylor terms at \(t\ne0\)
have absolute ratio \((2k+1)t^2\), so the Taylor series has radius zero.
Nevertheless the autonomous smooth system
\[
 \dot s=1,\qquad \dot q=g'(s),\qquad s(0)=0,\quad q(0)=1 \tag{6.4}
\]
has the exact solution \(s(t)=t,\ q(t)=g(t)\); integration of the two
equations also proves uniqueness. Its vector field never vanishes,
because its first component is one. Here \(s,q\) are auxiliary scalar
ODE coordinates, not network feature time or backward fields.
Thus failure of analyticity alone is not an obstruction to a smooth
finite-dimensional realization. Conversely, this example does not
supply a network closure, a convergent flow Taylor series, or a
depth- or time-uniform extension of the fixed-program theorem.

## 7. Reusable finite calculus and exact certificates

### 7.1. A finite moving-flow Taylor recurrence through order three

#### Specification and claim

Fix hidden depth \(L=2\), one sample \(m=1\), positive integers \(n,d\),
an input \(x_1\in\mathbb R^d\), a label \(y_1\in\mathbb R\), and constant
positive multipliers \(\kappa_1,\kappa_2,\kappa_3\). The input Gram entry is
\(G_{11}=x_1^Tx_1/d\); it need not be one or positive. Both hidden layers
use the same scalar activation \(\phi\in C^3(\mathbb R)\). No distributional
assumption is imposed on the finite initial weights.

The stored weights are \(W^{(1)}\in\mathbb R^{n\times d}\),
\(W^{(2)}\in\mathbb R^{n\times n}\), and
\(W^{(3)}\in\mathbb R^n\). For the sole sample, suppress the sample index
on hidden and backward fields. Use first-layer neuron index \(j\),
second-layer neuron index \(i\), and input-coordinate index \(\alpha\):

\[
\begin{aligned}
z_j^{(1)}&=\frac1{\sqrt d}\sum_{\alpha=1}^d W_{j\alpha}^{(1)}x_{1,\alpha},
&h_j^{(1)}&=\phi(z_j^{(1)}),\\
z_i^{(2)}&=\sum_{j=1}^n W_{ij}^{(2)}h_j^{(1)},
&h_i^{(2)}&=\phi(z_i^{(2)}),\\
f_{n,1}&=\frac1n\sum_{i=1}^n W_i^{(3)}h_i^{(2)},
&r_1&=f_{n,1}-y_1,\qquad \mathcal L_n=r_1^2.
\end{aligned}                                                    \tag{J1}
\]

In particular no extra width factor occurs in the hidden forward action.
The residual-free backward fields are

\[
\delta_i^{(2)}=W_i^{(3)}\phi'(z_i^{(2)}),\qquad
\delta_j^{(1)}=\phi'(z_j^{(1)})\sum_{i=1}^n W_{ij}^{(2)}\delta_i^{(2)}.
                                                               \tag{J2}
\]

The same entry \(W_{ij}^{(2)}\) in (J1) appears in (J2); the two actions
are \(W^{(2)}\) and its actual transpose. No identification of first- and
second-layer neurons is made even though their cardinalities agree.

Let \(t\) be physical time, with all raw blocks moving according to
\(\dot\theta=-D\nabla\mathcal L_n\), where the first, middle, and readout
blocks of the constant mobility \(D\) are multiplication by
\(n\kappa_1,\kappa_2,n\kappa_3\), respectively. Then

\[
\begin{aligned}
\dot W^{(1)}&=-\frac{2\kappa_1}{\sqrt d}\,r_1\delta^{(1)}x_1^T,\\
\dot W^{(2)}&=-\frac{2\kappa_2}{n}\,r_1\delta^{(2)}(h^{(1)})^T,\\
\dot W^{(3)}&=-2\kappa_3 r_1h^{(2)}.
\end{aligned}                                                    \tag{J3}
\]

For an integer \(0\le R\le3\), the recurrence below computes the
ordinary coefficients \(v_k=v^{(k)}(0)/k!\), \(0\le k\le R\), of all
three weight blocks, both forward preactivations and activations, and the
output along (J3). Here the expansion point is any supplied finite state;
calling its time zero does not require it to be a random initialization.
Backward coefficients are needed only through \(R-1\).

All identities in this specification concern real arithmetic. Their
evaluation with floating-point arrays is a numerical oracle for these
coefficients, not exact arithmetic, a population law, or an exact
positive-time solution.

#### Elementary algebra of ordinary coefficients

Write \(v(t)=\sum_{k=0}^R v_k t^k+o(|t|^R)\) for a \(C^R\) field,
with the usual continuous-value interpretation when \(R=0\). For any
fixed bilinear operation \(B\) between finite-dimensional spaces,

\[
[B(u,v)]_k=\sum_{p=0}^k B(u_p,v_{k-p}).                          \tag{J4}
\]

Indeed multiply the two finite expansions: the products of powers with
total degree \(k\) have exactly the displayed indices. Their remainders
are \(o(|t|^R)\), because the retained polynomials are locally bounded.
The rule applies entrywise to scalar multiplication, Hadamard products,
matrix products, outer products, and row-vector pairings. Finite sums
commute with coefficient extraction, and
\([(W^{(2)})^T]_k=(W_k^{(2)})^T\).

For a scalar function \(\psi\in C^q\), \(0\le q\le3\), use the following
coordinatewise composition coefficients only at degrees at most \(q\):

\[
\begin{aligned}
\mathcal C_0(\psi,z)&=\psi(z_0),\\
\mathcal C_1(\psi,z)&=\psi'(z_0)\odot z_1,\\
\mathcal C_2(\psi,z)&=\psi'(z_0)\odot z_2
 +\tfrac12\psi''(z_0)\odot z_1^{\odot2},\\
\mathcal C_3(\psi,z)&=\psi'(z_0)\odot z_3
 +\psi''(z_0)\odot z_1\odot z_2
 +\tfrac16\psi'''(z_0)\odot z_1^{\odot3}.
\end{aligned}                                                    \tag{J5}
\]

To verify (J5), put \(e(t)=z(t)-z_0\). Scalar Taylor expansion gives
\(\psi(z_0+e)=\psi(z_0)+\psi'(z_0)e+\psi''(z_0)e^2/2
+\psi'''(z_0)e^3/6+o(|e|^3)\). At positive truncation order,
\(e=O(|t|)\). The degree-two and degree-three terms of \(e^2\) are
\(z_1^{\odot2}\) and \(2z_1\odot z_2\), and the degree-three term of
\(e^3\) is \(z_1^{\odot3}\). Substitution proves each line, including
the lower-order versions obtained by truncation. Applying (J5) to
\(\psi=\phi'\) only for degrees at most two requires derivatives of
\(\phi\) through order three, not four.

#### Recurrence

Initialize \(W_0^{(1)},W_0^{(2)},W_0^{(3)}\) to the supplied raw state.
At each degree \(k=0,\ldots,R\), do the following forward sweep:

\[
\begin{aligned}
z_k^{(1)}&=W_k^{(1)}x_1/\sqrt d,
&h_k^{(1)}&=\mathcal C_k(\phi,z^{(1)}),\\
z_k^{(2)}&=\sum_{p=0}^k W_p^{(2)}h_{k-p}^{(1)},
&h_k^{(2)}&=\mathcal C_k(\phi,z^{(2)}),\\
f_{n,1;k}&=\frac1n\sum_{p=0}^k (W_p^{(3)})^Th_{k-p}^{(2)}.
\end{aligned}                                                    \tag{J6}
\]

If \(k=R\), stop. Otherwise form
\(r_{1;k}=f_{n,1;k}-\mathbf1_{\{k=0\}}y_1\), and compute

\[
\begin{aligned}
\delta_k^{(2)}
 &=\sum_{p=0}^k W_p^{(3)}\odot\mathcal C_{k-p}(\phi',z^{(2)}),\\
\delta_k^{(1)}
 &=\sum_{a+b+c=k}
   \mathcal C_a(\phi',z^{(1)})\odot (W_b^{(2)})^T\delta_c^{(2)}.
\end{aligned}                                                    \tag{J7}
\]

All indices in a sum of degrees are nonnegative integers. With these
coefficients, update the next degree of every weight block:

\[
\begin{aligned}
W_{k+1}^{(1)}
 &=-\frac{2\kappa_1}{(k+1)\sqrt d}
       \sum_{a+b=k} r_{1;a}\delta_b^{(1)}x_1^T,\\
W_{k+1}^{(2)}
 &=-\frac{2\kappa_2}{(k+1)n}
       \sum_{a+b+c=k} r_{1;a}\delta_b^{(2)}(h_c^{(1)})^T,\\
W_{k+1}^{(3)}
 &=-\frac{2\kappa_3}{k+1}
       \sum_{a+b=k} r_{1;a}h_b^{(2)}.
\end{aligned}                                                    \tag{J8}
\]

There is no circular dependence at a given degree. The weight coefficients
through \(k\) are available before (J6); the first layer of (J6) precedes
the second. Equation (J7) uses that forward sweep and already available
weights. Equation (J8) then creates the next weight coefficients. When
\(R=0\) only (J6)'s values are computed. For \(R>0\), (J7)'s largest
degree is \(R-1\), so its largest activation derivative is \(\phi^{(R)}\).
The terminal (J6) also uses derivatives only through \(\phi^{(R)}\).

In coordinates, the transpose contribution in (J7) is explicitly

\[
(\delta_k^{(1)})_j
=\sum_{a+b+c=k}\mathcal C_a(\phi',z^{(1)})_j
                    \sum_{i=1}^n (W_b^{(2)})_{ij}(\delta_c^{(2)})_i.
                                                               \tag{J9}
\]

Terms with \(b>0\) retain trained-weight contributions. Replacing this
matrix by \(W_0^{(2)}\), using an independent reverse matrix, or deleting
positive-degree residual coefficients changes the recurrence.

#### Proof that these are moving physical-flow coefficients

First verify (J3). Differentiating (J1) with respect to the final
preactivation gives \(\partial f_{n,1}/\partial z_i^{(2)}
=\delta_i^{(2)}/n\). Differentiating through the second layer gives
\(\partial f_{n,1}/\partial z_j^{(1)}=\delta_j^{(1)}/n\) by (J2).
Consequently the ordinary matrix and vector gradients are

\[
\nabla_{W^{(1)}}f_{n,1}=\delta^{(1)}x_1^T/(n\sqrt d),\quad
\nabla_{W^{(2)}}f_{n,1}=\delta^{(2)}(h^{(1)})^T/n,\quad
\nabla_{W^{(3)}}f_{n,1}=h^{(2)}/n.
\]

The derivative of \(r_1^2\) is \(2r_1\nabla f_{n,1}\). Multiplying each
gradient by its negative mobility proves (J3), including every width,
input, and loss factor.

For completeness, a local \(C^3\) solution exists and is unique without
any probabilistic argument. The finite vector field \(V\) in (J3) is
\(C^2\), since its factors involve \(\phi\) and \(\phi'\). On a small
closed Euclidean ball around the initial state its norm is bounded by
\(B\) and its first derivative by \(M\). Integration along a segment in
the ball gives \(\|V(u)-V(v)\|\le M\|u-v\|\). Choose a time radius
\(a>0\) with \(aB\) smaller than the ball radius and \(aM<1\).
For curves in the ball, the map
\(u\mapsto\theta_0+\int_0^t V(u(s))\,ds\), \(|t|\le a\), stays in
the ball and decreases the sup norm of differences by a factor at most
\(aM\). Iterating from the constant curve gives successive differences
bounded by a geometric series, hence a uniformly convergent curve. The
Lipschitz bound permits passage through the integral; its limit solves
the integral equation. Two solutions have sup norm difference at most
\(aM\) times that difference, hence agree. The integral equation first
gives a \(C^1\) solution. Substituting into the \(C^2\) vector field and
using the chain rule twice gives a \(C^3\) solution. The forward fields
and output are \(C^3\) by composition.

We now prove correctness by induction on degree. At degree zero, (J6)
is the defining network evaluation (J1). Assume that the algorithm has
the true coefficients of every weight through degree \(k\), and all
previously computed fields. The first equation of (J6) is a linear
contraction of the weight and fixed input, so has the true degree-\(k\)
coefficient. Equation (J5) proves the first activation coefficient.
Equation (J4) applied to \(W^{(2)}h^{(1)}\) proves the next
preactivation coefficient, and (J5) proves its activation coefficient.
Finally (J4) applied to the readout pairing proves \(f_{n,1;k}\).
Subtracting the fixed label only at degree zero gives the true residual
coefficient.

If \(k<R\), apply (J4) to (J2) and (J5) to its two activation derivatives.
This yields precisely (J7), including the derivative coefficients of the
transpose. Apply (J4) again to each product on the right of (J3); its
degree-\(k\) coefficient is the corresponding numerator of (J8). The
left side has degree-\(k\) coefficient \((k+1)W_{k+1}^{(\ell)}\).
Equating coefficients proves (J8). Thus all newly created weights are
correct, closing the induction up to \(R\). No higher derivative is
needed to justify the last step: when \(R=3\) the vector field is
expanded only through degree two.

In particular these coefficients have the finite Taylor interpretation
\(v(t)=\sum_{k=0}^R v_k t^k+o(|t|^R)\). A stronger
\(O(|t|^{R+1})\) remainder, a convergent infinite series, and a uniform
bound in width do not follow from this proof.

#### Relation to feature ascent and raw normalization

Feature ascent with these same mobilities is the separately defined flow
\(d\theta/ds=D\nabla f_{n,1}(\theta)\). Its raw equations are

\[
\frac{dW^{(1)}}{ds}=\kappa_1\delta^{(1)}x_1^T/\sqrt d,\quad
\frac{dW^{(2)}}{ds}=\kappa_2\delta^{(2)}(h^{(1)})^T/n,\quad
\frac{dW^{(3)}}{ds}=\kappa_3h^{(2)}.
                                                               \tag{J10}
\]

The scalarized first coordinate obeys
\(dz^{(1)}/ds=\kappa_1G_{11}\delta^{(1)}\). Its factor \(G_{11}\) is
forced by the raw first matrix and input, and is not an independent
normalization parameter. If one instead stores the auxiliary matrix
\(\widehat W^{(2)}=\sqrt n W^{(2)}\), then
\(z^{(2)}=\widehat W^{(2)}h^{(1)}/\sqrt n\) and
\(d\widehat W^{(2)}/ds=\kappa_2\delta^{(2)}(h^{(1)})^T/\sqrt n\).
This is a coordinate change; it introduces no extra factor into (J1).
With unit multipliers, the mobility in the coordinates
\((W^{(1)},\widehat W^{(2)},W^{(3)})\) is multiplication by \(n\) in
every block.

Physical time satisfies \(ds/dt=-2r_1\). On intervals where this is
positive it is the increasing feature-time change. At \(r_1=0\),
(J3) has zero vector field; the unique local physical solution is
constant, and all its positive-order coefficients vanish. The recurrence
handles this case directly without dividing by \(r_1\).

It is not sufficient to rescale the \(k\)-th feature derivative by the
\(k\)-th power of the initial clock speed. To see the missing terms,
let \(F(s)=f_{n,1}(\theta(s))\), and write \(b=-2r_1(0)\).
At the expansion point, \(s'=b\), \(s''=-2bF'\), and
\(s'''=-2b^2F''+4b(F')^2\), obtained by differentiating
\(s'=-2(F(s)-y_1)\) twice. The chain rule gives physical derivatives

\[
\begin{aligned}
\dot f_{n,1}&=bF',\\
\ddot f_{n,1}&=b^2F''-2b(F')^2,\\
f_{n,1}^{(3)}&=b^3F'''-8b^2F'F''+4b(F')^3.
\end{aligned}                                                    \tag{J11}
\]

Equation (J8) incorporates these clock effects by retaining the moving
residual before every coefficient update. It also retains acceleration
and higher weight coefficients; evaluating the network on the straight
line \(\theta_0+t\dot\theta_0\) would discard them.

#### Numerical interface and claim boundary

`pde.finite_jets.flow_jet(parameters, inputs, labels,
activation_derivative, order=R, kappas=...)` implements (J6)--(J8).
`inputs` has shape `(d,1)` and `labels` has shape `(1,)`. Its result has
`parameter_coefficients[k]` in raw `Parameters` storage; each array in
`preactivation_coefficients` and `hidden_coefficients` has shape
`(R+1,n,1)`, with tuple positions zero and one corresponding to layers
one and two. `output_coefficients[k,0]` is \(f_{n,1;k}\), and
`output_derivatives[k,0]` is its factorial multiple.

The derivative callback receives `(j,z)` with \(0\le j\le R\), and
must return the true coordinatewise \(\phi^{(j)}(z)\) as a real finite
array of the same shape `(n,1)`. Each call receives a private copy of
the initial preactivation; its returned array is copied immediately.
This permits in-place callbacks and reusable output buffers without
altering the initial coordinates or earlier derivatives. Consistency,
coordinatewise semantics, and \(C^3\) regularity cannot be certified
by shape and finiteness checks; they are requirements on the caller.
Callbacks must not mutate unrelated external state of the calculation.

Parameter and argument validation follows the finite numerical contract.
Only the evaluated degrees are required to be representable: no terminal
backward field, loss value, or unused residual is constructed. Raw first
matrix contraction precedes division by \(\sqrt d\). Scalar mobility,
normalization, and degree factors are combined using mantissa/exponent
multiplication. This avoids premature range loss for those factors but
does not protect raw matrix products, convolution sums, or composition
powers from overflow, underflow, or cancellation. Nonfinite evaluated
coefficients are rejected. An unrepresentable factorial multiple is
rejected when output derivatives are requested. There is no
correct-rounding or universal extreme-range guarantee.

For bounded \(R\le3\), storage and algebraic work are \(O(nd+n^2)\),
in addition to callback costs, with constants depending on the degree. No
Gaussian initialization, expectation, width extrapolation, population
closure, infinite-order calculus, or positive-time error estimate is
part of this result. In particular the finite deterministic recurrence
applies both to order-one and small stored readouts without identifying
their different population initialization regimes.

### 7.2. Forest factorization and small exact certificates

The following is a reusable, finite algebraic part of the calculus. It is
not a claim that a high-order compiler, an infinite Taylor series, or a
positive-time population evolution has been verified. The implementation
`pde.exact_calculus` supplies a canonical forest key, rational finite-series
reversion, rational determinants, and one completely specified certificate.
No retained table is an input to these operations.

#### Decorated forests and the leading Gaussian factorization

Take independent standard Gaussian variables \(a_i,u_j,g_{ij}\), for
\(1\le i,j\le n\), with the two neuron populations kept separate. A finite
bipartite forest has second-layer vertices decorated by powers of \(a_i\),
first-layer vertices decorated by powers of \(u_j\), and an edge for each
factor \(g_{ij}\). Decorations are nonnegative integers, and edges are simple.
Sum its monomial over all neuron labels, with no restriction that different
vertices have different labels. If it has \(e\) edges and \(r\) connected
components, normalize this sum by \(n^{-e/2-r}\). Let its expectation be
\(T_n\). All graph sizes and decorations in this paragraph are fixed while
\(n\) grows.

**Finite-forest factorization.** The limit of \(T_n\) exists. It equals the
product of the limits of its separately normalized connected components.
A component with an odd number of edges has zero limit. The assertion
concerns expectation; it does not alone prove concentration or empirical-law
convergence.

Here is a direct proof. If the total edge count is odd, Gaussian symmetry
makes the expectation zero. Otherwise write \(e=2p\). Expanding the Gaussian
edge expectation into pairings, as proved in Section 4, identifies both
endpoints of every pair of edges. Collapse each pair to a single edge in
the resulting multigraph. Let \(v\) be its number of vertices and \(c\)
its number of connected components. A connected multigraph with \(v_0\)
vertices needs at least \(v_0-1\) edges: begin with one vertex and add an
edge each time the reachable vertex set grows. Consequently
\[
 v\le p+c,\qquad c\le r.
 \tag{7.F1}
\]
For this fixed pairing, labelings with no extra equality among distinct
vertices in either neuron population number
\((n)_{v_1}(n)_{v_2}=n^v+O(n^{v-1})\), where \(v_1+v_2=v\) and
\((n)_b=n(n-1)\cdots(n-b+1)\). Their decoration expectation is the product
of the Gaussian moments at the quotient vertices. Labelings with an extra
equality number \(O(n^{v-1})\): choose an equal vertex pair and then all
remaining labels freely. Their Gaussian decoration moments are bounded by
a constant depending only on the fixed decorations. Thus this pairing
contributes a constant times \(n^{v-p-r}\), with an error one power smaller.
There are finitely many pairings. By (7.F1) none diverges.

Only \(v=p+r\) can survive. It requires \(c=r\) and equality in the
connected edge bound, so no pairing joins two original components and each
quotient component is a tree. Conversely the independently chosen surviving
pairings of the original components give exactly these surviving full-forest
pairings. Their decoration factors multiply, and the leading coefficient
of each free-label count is one. Summing proves the product assertion. If
an original component has odd edge count there is no internal complete
pairing, so the limit is zero. This also handles odd total edge count and
isolated vertices. No independence of trained coordinates has been asserted.

For example a two-edge component \(g_{ij}g_{ik}u_j^2u_k^2\), with its
three labels summed and normalization \(n^{-2}\), has only one edge
pairing. It forces \(j=k\), leaving two free labels and moment
\(E u_j^4=3\). Two disjoint copies have limit \(9\): pairings between
the copies identify their components and lose at least a factor \(1/n\).
An isolated second-layer decoration \(a_i^2\), normalized by \(1/n\),
has limit one and can be multiplied into this example. This factorization
is the reason connected objects can be computed once and reused.

To make that reuse independent of arbitrary vertex names, give vertex \(v\)
the color \((\ell_v,b_v)\), its layer in \(\{1,2\}\) and decoration.
For a rooted tree define its key recursively to be its root color followed
by the sorted tuple of its children's keys. The key of an unrooted tree
is the lexicographically smallest rooted key over all possible roots.
The key of a forest is the sorted tuple of its component keys, retaining
repetitions. The empty forest has the empty tuple.

Induction on tree size proves that rooted keys agree exactly when a
color-preserving rooted isomorphism exists: equal sorted lists match the
children with multiplicity and invoke the induction on each subtree;
the reverse implication follows from the same decomposition. Equal minima
for two unrooted trees give roots with equal rooted keys and hence an
unrooted isomorphism. An unrooted isomorphism maps the whole list of rooted
keys onto the other, proving the converse. The same component argument
proves the forest assertion. Therefore this immutable key can safely index
a caller's memoization of any genuinely isomorphism-invariant calculation.
It does not by itself compute that calculation or certify a coefficient
generator. Edge validation by successively merging connected components
rejects a duplicate or cycle exactly when its two endpoints were already
connected. This proves the validation and key logic in `forest_key`.

#### A fully specified quadratic initialization-jet obstruction

This example uses a different metric and initialization from the main
nonlinear training theorem. It is a negative test of a proposed universal
representation, not a recommended model for feature learning. There is one
sample \(x=y=1\), \(d=1\), \(L=2\), quadratic activations, and
\[
 W^{(1)}_j=u_j,\quad W^{(2)}_{ij}=g_{ij}/\sqrt n,
 \quad W^{(3)}_i=a_i,\qquad
 z_i^{(2)}=\frac1{\sqrt n}\sum_j g_{ij}u_j^2,
 \quad f_n=\frac1n\sum_i a_i(z_i^{(2)})^2.
 \tag{7.C1}
\]
All the displayed initialization Gaussians are independent standard normals;
the stored readout is order one. Freeze only the first parameter block and
use feature ascent, with hidden stored-block mobility one and readout
mobility \(n\). Thus, in the auxiliary unscaled matrix coordinates,
\[
 \frac{da_i}{ds}=(z_i^{(2)})^2,\qquad
 \frac{dg_{ij}}{ds}=\frac2{\sqrt n}a_i z_i^{(2)}u_j^2,
 \qquad \frac{du_j}{ds}=0.
 \tag{7.C2}
\]
These equations follow by differentiating (7.C1); they are not loss GD or
physical-time GF. Put \(q_n=n^{-1}\sum_j u_j^4\). Differentiating the
preactivation gives \(dz_i^{(2)}/ds=2q_n a_i z_i^{(2)}\). Therefore the
exact finite initialization derivative of order \(k\) is
\[
 \left.\frac{d^k f_n}{ds^k}\right|_{s=0}
 =\frac1n\sum_i \mathscr D_{q_n}^{k}(a_i(z_i^{(2)})^2),
 \quad \mathscr D_q=z^2\partial_a+2qaz\partial_z.
 \tag{7.C3}
\]
Here \(a,z\) are the two scalar arguments of a polynomial; the superscript
on \(\mathscr D\) is repeated application, not a weight-layer index.
Repeated chain rule proves (7.C3), since \(q_n\) is constant along (7.C2).
Smooth finite equations have a local solution at every initial state; no
positive-time uniform existence is needed to define these derivatives.

Conditional on all \(u_j\), the pairs \((a_i,z_i^{(2)})\) at initialization
are independent, with laws \(N(0,1)\otimes N(0,q_n)\). Set
\(z=\sqrt q\,\xi\). Then
\(\mathscr D_q=q(\xi^2\partial_a+2a\xi\partial_\xi)\) and
\(az^2=qa\xi^2\). Conditional expectation of (7.C3) is consequently
\(c_k q_n^{k+1}\), for a fixed finite constant \(c_k\).

To pass to the unconditional limit without a probabilistic black box, note
that \(E u^4=3\) and independence imply \(E(q_n-3)^2=\operatorname{Var}(u^4)/n\).
For every positive integer \(b\), convexity gives
\(E q_n^{2b}\le E|u|^{8b}<\infty\), uniformly in \(n\).
For a nonnegative \(x\), factorization of \(x^b-3^b\) bounds its absolute
value by \(b|x-3|\max(x,3)^{b-1}\). Cauchy--Schwarz and the preceding
moment bound show \(E|q_n^b-3^b|\to0\). Hence all fixed-order annealed
initialization derivatives have the exact limit
\[
 d_k=E\mathscr D^k(AZ^2),\qquad
 \mathscr D=z^2\partial_a+6az\partial_z,\quad
 A\sim N(0,1),\ Z\sim N(0,3)\text{ independent}.
 \tag{7.C4}
\]
The expectation is of the polynomial after substitution \((a,z)=(A,Z)\).
This proves the probabilistic interpretation of this particular coefficient
recurrence. It does not interchange an infinite series with a width limit.

The elementary monomial rules are
\[
 \mathscr D(a^p z^q)=p a^{p-1}z^{q+2}+6q a^{p+1}z^q,
 \qquad E[A^pZ^q]=
 \begin{cases}(p-1)!!(q-1)!!3^{q/2},&p,q\text{ even},\\0,&\text{otherwise}.
 \end{cases}
 \tag{7.C5}
\]
Use \((-1)!!=1\). The moment rule follows by integrating the Gaussian
density derivative by parts, starting with moment zero equal to one;
independence multiplies the two moments. Each application changes the
parity of the \(a\) exponent and preserves the parity of the \(z\) exponent.
Thus all even \(d_k\) vanish. Starting from the single monomial \(az^2\),
(7.C5) through order thirteen gives
\[
 (d_1,d_3,d_5,d_7,d_9,d_{11},d_{13})=
 (63,77760,274547232,2141006515200,31149221916487680,
 759035131220036321280,28719223368439752070594560).
 \tag{7.C6}
\]
For instance the first differentiated polynomial is \(z^4+12a^2z^2\),
whose expectation is \(27+36=63\). The finite recurrence (7.C5), not a
table read from another source, specifies every other integer in (7.C6).

Form the formal series \(F(s)=\sum_{k\ge0}d_k s^k/k!\). This is a
formal algebraic object; no convergence is presumed. Its zero constant and
nonzero linear coefficient give a unique formal inverse \(B(y)\).
Define \(K(y)=F'(B(y))\). Since \(F\) is odd, uniqueness makes \(B\)
odd and \(K\) even. Define the coefficients \(\mu_j\) by
\[
 K(y)=63+y^2\sum_{j\ge0}(-1)^j\mu_j y^{2j}.
 \tag{7.C7}
\]
Only (7.C6) is needed for \(\mu_0,\ldots,\mu_5\). There is no use
of a specialized inversion theorem: if \(a_k=d_k/k!\), let \(b_0=0\),
\(b_1=1/a_1\), and successively set
\[
 b_k=-\frac1{a_1}[y^k]\sum_{j=2}^k a_j
                  \left(\sum_{i=1}^{k-1}b_i y^i\right)^j.
 \tag{7.C8}
\]
The only degree-\(k\) term involving the unknown \(b_k\) in \(F(B(y))\)
is \(a_1b_k\); thus induction proves both existence and uniqueness and
the formula. Ordinary convolution gives each product coefficient.
Substitution in \(F'(B(y))\) gives exactly
\[
 (\mu_0,\ldots,\mu_5)=\left(
 \frac{480}{49},\frac{43756}{151263},\frac{7214528}{200120949},
 \frac{12545175968}{2402451992745},
 \frac{171752915595136}{200241971143303005},
 \frac{2199776554157960896}{14570607030242443158825}\right).
 \tag{7.C9}
\]

These six coefficients cannot be moments of a nonnegative measure on
\([0,\infty)\). Indeed the shifted moment matrix
\(M_{ij}=\mu_{i+j+1}\), \(0\le i,j\le2\), satisfies
\[
 \det M=-\frac{86245462994269879146938487857152}
 {200150589172828762588730609071155193161975}<0.
 \tag{7.C10}
\]
There is also a direct polynomial witness, avoiding a definiteness criterion.
Let \(p(\lambda)=v_0+v_1\lambda+\lambda^2\), where
\[
 v_0=\frac{40042013405871059816}{2310453239160606810795},\qquad
 v_1=-\frac{14165989123115588}{49896409440894219}.
\]
Direct rational multiplication of (7.C9) gives
\[
 \sum_{i,j=0}^2v_i v_j\mu_{i+j+1}
 =-\frac{673792679642733430835456936384}
 {329714727520793070279653295504327135}<0,
 \qquad v_2=1.
 \tag{7.C11}
\]
If such a representing measure \(\nu\) existed, this finite sum would
equal \(\int\lambda p(\lambda)^2\nu(d\lambda)\ge0\). This is the
contradiction. All relevant moments are finite by the representation being
tested. The result refutes a representation demanded uniformly over metrics
including this zero first-block mobility. It does not settle the unit-metric
case, any strictly positive first mobility, or an actual positive-time
population equation. Nonexistence of this moment representation is not
nonexistence of a nonlinear feature-learning limit.

#### Implementation and independent checking routes

`revert_series` accepts ordinary rational coefficients and implements (7.C8)
by truncated composition in Horner order. Multiplication is the finite
convolution \((ab)_k=\sum_{i=0}^k a_i b_{k-i}\). It returns all inverse
coefficients to the same length, without mutating its input. A nonzero
constant or zero linear coefficient is rejected. `determinant` eliminates
successive columns using a nonzero pivot, swapping rows when necessary and
tracking the determinant sign. Subtracting multiples of one row from another
preserves the determinant; each pivot multiplies the remaining triangular
determinant. If no pivot exists, the remaining first column is zero and the
determinant is zero. The empty determinant is one. This proves its algorithm
over the rational field, including singular matrices.

`quadratic_axis_certificate()` generates (7.C6) directly from (7.C5), reverts
the ordinary series using (7.C8), composes its derivative to produce (7.C9),
and constructs the witness by solving the leading two-by-two shifted system:
\[
 v_0=\frac{\mu_2\mu_4-\mu_3^2}{\mu_1\mu_3-\mu_2^2},\qquad
 v_1=\frac{\mu_2\mu_3-\mu_1\mu_4}{\mu_1\mu_3-\mu_2^2}.
\]
The positive denominator is checked before division. Tests independently
compare the six displayed fractions and evaluate (7.C11) from the displayed
witness; a Leibniz-permutation determinant checks the elimination route.
Series tests compose both directions of reversion, and forest tests check
relabelling, edge order, component multiplicity, invalid graphs and changed
decorations. They do not validate an unimplemented general-depth generator.

All scalar arithmetic in this module is integer or `fractions.Fraction`;
floating values and booleans are rejected by its rational interfaces.
Graph indices and colors are nonnegative Python integers, with layer one or
two. Inputs are finite lists or tuples. Results are freshly constructed;
there is no cross-call cache, sampling or file output. Rational bit sizes and
the all-roots tree-key cost can grow, so these are small transparent reference
primitives, not performance claims for large-order campaigns. Python recursion
limits still apply to the recursive tree key.

The established unit-test command in the code guide regenerates all displayed
coefficient and witness checks. No generated data, historical coefficient
array, symbolic package or external source is required. Exact arithmetic
certifies these finite computations, while (7.C1)--(7.C5) supply the separate
initialization-jet interpretation. Neither part supplies a positive-time
identification bridge.

## 8. Quantitative step doubling for the exact fixed-program limit

This section uses the fixed-program width theorem in Section 5 at its
stated scope and supplies the additional finite-order calculus. Its
conclusion concerns separately fixed integers \(L,N\), with width sent
to infinity at each fixed nonzero feature-ascent step before the two
population outputs are compared. It supplies an exact Gaussian-integral
formula for the cubic coefficient and a fully explicit fifth-order
remainder. The number of steps does not grow in any limit here.

### 8.1. Model, coefficient, and quantitative statement

Use exactly the one-input, one-sample network, independent initialization,
and simultaneous stored-parameter updates (5.2.1)--(5.2.8). In particular,
\(m=d=1\), \(x_1=1\), the stored readout has independent \(N(0,1)\)
coordinates, and the mobility matrix in stored coordinates is
\(D_n=\operatorname{diag}(nI,I,\ldots,I,nI)\). There is no residual or
loss in these feature-ascent updates. The scalar \(h\) below is the
feature-ascent step of Section 5. It is not physical training time \(t\),
a loss-GD step \(\eta_n\), or the proof mesh \(\Delta\). The index
\(k\) always counts updates; the hidden features retain their layer
superscripts \(h^{(\ell)}\) and \(H^{(\ell)}\).

Strengthen the activation hypothesis to
\[
 \phi\in C^{12}(\mathbb R),\qquad E\phi(G)^2=1,
 \qquad G\sim N(0,1),                                      \tag{8.1.1}
\]
\[
 M_\phi=\max\left\{1,\sup_x\frac{|\phi(x)|}{1+|x|},
       \max_{1\le j\le12}\|\phi^{(j)}\|_\infty\right\}<\infty,
 \qquad B_\phi=\max\{4,M_\phi\}.                           \tag{8.1.2}
\]
The expectation \(E\) in a one-dimensional activation integral is over
the displayed standard Gaussian. All population contractions elsewhere
are \(E_\ell\) on the physical layer \(\Omega_\ell\), as in Section 5.5.

Let \(F_{N,L}(h)\) be the inverse-free population output (5.5.12).
Sections 8.2--8.4 define its finite exact compiler, including at zero
step. Write \(\mathcal J^{\mathrm{cmp}}_{j,N,L}\) for the number returned
by the order-\(j\) terminal compiler, defined by (8.4.8) below before any
identification with an output derivative. Set
\[
 \mathcal C^{\mathrm{cmp}}_{\phi,L,N}
   =\frac{8\mathcal J^{\mathrm{cmp}}_{3,N,L}
                 -\mathcal J^{\mathrm{cmp}}_{3,2N,L}}6.      \tag{8.1.3}
\]
This notation leaves \(\kappa_\ell\) reserved for mobility multipliers.
The integer \(E_{L,N}\) is explicitly defined in (8.5.1)--(8.5.4),
(8.5.13); it depends only on \(L,N\).

**Theorem 8.1 (fixed-depth, fixed-step-count quantitative doubling).**
Under (8.1.1)--(8.1.2), for every fixed \(L,N\ge1\),
\[
 F_{N,L}\in C^5([-1,1]),\qquad
 \sup_{|h|\le1}|F_{N,L}^{(5)}(h)|\le B_\phi^{E_{L,N}},    \tag{8.1.4}
\]
and
\[
 \left|F_{N,L}(2h)-F_{2N,L}(h)
                  -\mathcal C^{\mathrm{cmp}}_{\phi,L,N}h^3\right|
       \le B_\phi^{E_{L,2N}}|h|^5,
       \qquad |h|\le\tfrac12.                            \tag{8.1.5}
\]
For each fixed \(h\ne0\) in this interval, both outputs in (8.1.5)
are the actual width-first expectations:
\[
 F_{N,L}(2h)=\lim_{n\to\infty}E f_{n,L}^{N}(2h),\qquad
 F_{2N,L}(h)=\lim_{n\to\infty}E f_{n,L}^{2N}(h).          \tag{8.1.6}
\]
The argument in parentheses specifies the common step of that finite
program. At \(h=0\), the finite-width expectation and the population
output are both zero, by the separate argument in Section 8.7.

If \(E\phi'(G)^2=0\), then \(\phi\equiv1\) or \(-1\),
\(F_{N,L}(h)=Nh\), and the difference in (8.1.5) is identically zero.
Its coefficient and remainder can both be taken to be zero for all real
\(h\). The other branch includes nonconstant affine activations.

To prove the theorem, first express every population expectation as a
chronological Gaussian call on a single layer. A density calculation and
regularization prove the needed Price formula even at singular
covariance. Exact differentiation and polynomial envelopes then provide
both the coefficient and its explicit error bound. Finally, parity and
a direct first-order calculation cancel the lower-order terms. The
only width-limit input is the theorem already proved in Section 5.

### 8.2. Layerwise calls and their exact chronology

Keep \(Z^{(\ell)}_k,H^{(\ell)}_k,\Delta^{(\ell)}_k,
q^{(\ell)}_k,W^{(L+1)}_k,Q_{\ell,jk},K_{\ell,jk},
\rho_{\ell,kj},\sigma_{\ell,kj},\xi_{\ell,k},\chi_{\ell,k}\)
with precisely the types and definitions in (5.5.1)--(5.5.13).
In particular, \(q^{(\ell)}_k\) is the incoming population backsignal,
\(H^{(\ell)}_k=\phi(Z^{(\ell)}_k)\) is the feature, and source
derivatives hold every deterministic covariance and response coefficient
fixed. Neither a transpose nor a response is an independent replacement
for a reused initialization matrix.

For the finite compiler introduce only the deterministic full response
coefficients
\[
 R_{\ell,kj}=\rho_{\ell,kj}+hQ_{\ell-1,jk}\quad(j<k),
                                                               \tag{8.2.1}
\]
\[
 T_{\ell,kj}=\sigma_{\ell,kj}+hK_{\ell,jk}\quad(j<k),
 \qquad T_{\ell,kk}=\sigma_{\ell,kk}.                      \tag{8.2.2}
\]
These are scalar history coefficients, not operators, times, or kernels.
Thus the relevant assignments from Section 5.5 read
\[
 Z^{(\ell)}_k=\xi_{\ell,k}
       +\sum_{j<k}R_{\ell,kj}\Delta^{(\ell)}_j\quad(\ell\ge2),
 \qquad H^{(\ell)}_k=\phi(Z^{(\ell)}_k),                  \tag{8.2.3}
\]
\[
 q^{(\ell-1)}_k=\chi_{\ell,k}
             +\sum_{j\le k}T_{\ell,kj}H^{(\ell-1)}_j,
 \qquad
 \Delta^{(\ell-1)}_k=q^{(\ell-1)}_k\phi'(Z^{(\ell-1)}_k). \tag{8.2.4}
\]
The bottom update and readout are still (5.5.7), (5.5.11)--(5.5.12).
Every sum proportional to an update uses strictly earlier steps.

Write \(Q_\ell^{[k]}=(Q_{\ell,ij})_{0\le i,j\le k}\) and similarly
for \(K_\ell^{[k]}\); a history with upper index \(-1\) is empty.
For \(L\ge2\), start with \(Q_{1,00}=1\). At each
\(k=0,\ldots,N-1\), make the following calls in the displayed order.
Each call reconstructs the local history with already known scalar
coefficients, then integrates all its new scalar outputs against the
indicated finite Gaussian law.

1. For \(\ell=2,\ldots,L-1\) in increasing order, use the layer-\(\ell\)
   source vector
   \((\xi_{\ell,0:k},\chi_{\ell+1,0:k-1})\), with covariance
   \(Q_{\ell-1}^{[k]}\oplus K_{\ell+1}^{[k-1]}\).
   Reconstruct old cotangents and the current forward field. Return the
   new row of \(Q_\ell^{[k]}\), the responses
   \(\rho_{\ell+1,kj}\), \(j<k\), and their full coefficients.
2. On layer \(L\), use \((A,\xi_{L,0:k})\), with covariance
   \([1]\oplus Q_{L-1}^{[k]}\). Form the current feature, readout,
   and cotangent. Return the new row of \(K_L^{[k]}\),
   \(\sigma_{L,kj}\), \(j\le k\), their full coefficients, and
   \(E_L[W^{(L+1)}_kH^{(L)}_k]\) if wanted.
3. For \(\ell=L-1,\ldots,2\) in decreasing order, use
   \((\xi_{\ell,0:k},\chi_{\ell+1,0:k})\), with covariance
   \(Q_{\ell-1}^{[k]}\oplus K_{\ell+1}^{[k]}\).
   Reconstruct the local history and current cotangent. Return the new
   row of \(K_\ell^{[k]}\), \(\sigma_{\ell,kj}\), \(j\le k\),
   and their full coefficients.
4. On layer 1 use \((U,\chi_{2,0:k})\), with covariance
   \([1]\oplus K_2^{[k]}\). Form the current cotangent and
   \(Z^{(1)}_{k+1}=Z^{(1)}_k+h\Delta^{(1)}_k\). Return the new row
   of \(Q_1^{[k+1]}\), \(\rho_{2,k+1,j}\), \(j\le k\), and
   their full coefficients.

At \(k=N\), perform only the ascending interior calls and the top call;
the latter stops after the terminal readout-times-feature expectation.
No terminal cotangent is needed. Empty layer ranges are omitted. Every
input covariance and response used inside a call has therefore been
constructed before that call. New Gram entries and responses computed
in the same call are parallel outputs; none is an input to its own
integrand or covariance.

The call dimensions are
\[
 \begin{array}{c|c}
 \text{call}&\text{source dimension}\\ \hline
 \text{interior forward at }k&2k+1\\
 \text{top at }k&k+2\\
 \text{interior backward at }k&2k+2\\
 \text{bottom at }k&k+2\\
 \text{terminal interior}&2N+1\\
 \text{terminal top}&N+2.
 \end{array}                                                \tag{8.2.5}
\]
They are all at most \(D_N=2N+2\). There are
\(2(L-1)\) nonterminal calls per update and \(L-1\) terminal calls,
hence exactly \((2N+1)(L-1)\) calls. This equals the number of raw
initialization-matrix actions in Section 5.3; a call here is a
layerwise expectation bundle, not an additional matrix observation.

For \(L=1\), there is instead one expectation on independent
\((A,U)\sim N(0,I_2)\). In that one call unroll
\[
 Z^{(1)}_0=U,\quad W^{(2)}_0=A,\qquad
 \begin{aligned}
 W^{(2)}_{k+1}&=W^{(2)}_k+h\phi(Z^{(1)}_k),\\
 Z^{(1)}_{k+1}&=Z^{(1)}_k+hW^{(2)}_k\phi'(Z^{(1)}_k),
 \end{aligned}                                             \tag{8.2.6}
\]
and integrate \(W^{(2)}_N\phi(Z^{(1)}_N)\). Both updates use the old
state. No fictitious connector or history inverse is introduced.

All these calls are also defined at \(h=0\). Indeed a matrix of
second moments is positive semidefinite: its quadratic form at \(b\)
is the expectation of the square of the corresponding linear
combination. Chronological construction therefore supplies a Gaussian
law for each covariance, using the finite square-root construction in
Section 4. No strict-rank assertion is needed to define these calls.

### 8.3. Price differentiation, with the singular case proved

**Lemma 8.2.** Let \(I=[-1,1]\), and let
\(C\in C^5(I;\mathbb S_+^{b})\), where \(b\) is a source dimension
and is unrelated to the network input dimension \(d=1\). Suppose
\(\psi(h,x)\) has jointly continuous mixed derivatives
\[
 \partial_h^j D_x^\alpha\psi,
       \qquad j+\left\lceil|\alpha|/2\right\rceil\le5,       \tag{8.3.1}
\]
all bounded in absolute value by \(A_*(1+\|x\|_2)^{p_*}\), uniformly
on \(I\). If \(Y_h\sim N(0,C(h))\), then
\(\mathcal T(h)=E\psi(h,Y_h)\) belongs to \(C^5(I)\), and
\[
 \mathcal T^{(r)}(h)=E\Psi_r(h,Y_h),\qquad
 \Psi_0=\psi,\qquad
 \Psi_{r+1}=\partial_h\Psi_r+\tfrac12 C'(h):D_x^2\Psi_r,
       \quad 0\le r<5.                                    \tag{8.3.2}
\]
The contraction is \(C':D_x^2=\sum_{a,c=1}^{b}C'_{ac}\partial_a\partial_c\);
off-diagonal ordered pairs are both included. On a closed interval
\(C^5\) means that the derivatives through order five extend
continuously to the endpoints.

**Proof.** First suppose \(C(h)>0\). Its Gaussian density \(p_h\)
satisfies, by differentiating its determinant and quadratic exponent,
\[
 \partial_h p_h(x)=\tfrac12
  \left(x^TC^{-1}C'C^{-1}x-\operatorname{tr}(C^{-1}C')\right)p_h(x).
                                                               \tag{8.3.3}
\]
On the other hand,
\[
 \partial_a\partial_c p_h(x)
  =\left((C^{-1}x)_a(C^{-1}x)_c-(C^{-1})_{ac}\right)p_h(x).
\]
Contracting this identity with \(C'_{ac}/2\) gives (8.3.3).
Differentiation under the integral and two integrations by parts now
give
\[
 \frac{d}{dh}\int\psi(h,x)p_h(x)\,dx
 =\int\left(\partial_h\psi+\tfrac12 C':D_x^2\psi\right)p_h\,dx.
                                                               \tag{8.3.4}
\]
On a compact parameter interval with positive minimum covariance
eigenvalue, the density and its differentiated factors have polynomial
times Gaussian bounds. Together with (8.3.1), these bounds justify the
differentiation and make the boundary terms vanish, for instance by
first inserting compact cutoffs and then sending their radius to infinity.

Each iteration either applies one \(h\)-derivative to an integrand
or covariance coefficient, or adds two spatial derivatives with one
factor of \(C'\). After \(r\) iterations, only covariance derivatives
through order \(r\) and integrand derivatives with
\(j+\lceil|\alpha|/2\rceil\le r\) occur. Thus (8.3.4) iterates
through order five using exactly (8.3.1).

For a possibly singular \(C\), put \(C_\epsilon=C+\epsilon I_b\),
\(0<\epsilon\le1\). Its positive definiteness permits the preceding
argument. Its derivatives of positive order equal those of \(C\),
so the derived expressions \(\Psi_r\) are unchanged. Couple
\(Y_{\epsilon,h}=C_\epsilon(h)^{1/2}G_b\) and
\(Y_h=C(h)^{1/2}G_b\) with a standard Gaussian \(G_b\).
Diagonalize \(C(h)\). The two square roots have the same eigenvectors,
and, for every eigenvalue \(\lambda\ge0\),
\[
 0\le\sqrt{\lambda+\epsilon}-\sqrt\lambda\le\sqrt\epsilon.
\]
Consequently
\[
 \sup_{h\in I}\|C_\epsilon(h)^{1/2}-C(h)^{1/2}\|_{\rm op}
       \le\sqrt\epsilon.                                  \tag{8.3.5}
\]
Let \(v=\sup_{h\in I}\sum_{a,c}|C_{ac}(h)|<\infty\).
Both coupled vectors have norm at most \(\sqrt{v+1}\|G_b\|_2\).
Every \(\Psi_r\) is a finite sum of the mixed derivatives in (8.3.1)
times bounded covariance-derivative coefficients, so it has a common
polynomial envelope. On \(\{\|G_b\|_2\le R\}\), (8.3.5) and
uniform continuity on compact sets give uniform convergence in \(h\)
of its coupled values. Outside that event, a fixed polynomial in
\(\|G_b\|_2\) dominates their difference and has a tail expectation
tending to zero as \(R\to\infty\). Hence
\[
 E\Psi_r(h,Y_{\epsilon,h})\longrightarrow E\Psi_r(h,Y_h)
 \quad\text{uniformly on }I,\quad 0\le r\le5.             \tag{8.3.6}
\]
The limiting expectations are continuous by the same compact-and-tail
argument. For each \(r<5\), pass to the limit in
\[
 \mathcal T_\epsilon^{(r)}(v_1)
 -\mathcal T_\epsilon^{(r)}(u_1)
       =\int_{u_1}^{v_1}\mathcal T_\epsilon^{(r+1)}(s)\,ds.
\]
Uniform convergence shows successively that each limiting function has
the next as its derivative. This proves (8.3.2), including at changes
of rank. No derivative of a singular covariance square root, and no
inverse of the original covariance, has been used. \(\square\)

### 8.4. Exact compiler, envelope compiler, and derivative budget

An envelope \((A,p)\), with \(A\ge0\) and integer \(p\ge0\), means
\(|g(x)|\le A(1+\|x\|_2)^p\), uniformly for \(|h|\le1\).
Use the two operations
\[
 (A,p)\oplus(B,q)=(A+B,\max\{p,q\}),\qquad
 (A,p)\odot(B,q)=(AB,p+q).                                 \tag{8.4.1}
\]
The leaves \(1,h,x_a\) have envelopes \((1,0),(1,0),(1,1)\).
A real constant has envelope \((|c|,0)\). If \(g\) has envelope
\((A,p)\), assign
\[
 \mathcal E(\phi(g))=(M_\phi(1+A),p),\qquad
 \mathcal E(\phi^{(j)}(g))=(M_\phi,0),\quad1\le j\le12.   \tag{8.4.2}
\]
Sums, products, and derivatives are expanded by their exact rules.
An earlier scalar node \(S(h)\), with bounds \(\bar S_j\) through
order five, supplies formal tokens
\[
 \partial_h S^{[j]}=S^{[j+1]},\qquad
 \partial_{x_a}S^{[j]}=0,
 \qquad\mathcal E(S^{[j]})=(\bar S_j,0).                  \tag{8.4.3}
\]
All ambient source derivatives in a response also hold these tokens
fixed. Only total \(h\)-differentiation advances their order.

Consider a call \(\mathcal T(h)=E_{N(0,C(h))}\psi(h,Y)\) in dimension
\(b\le D_N\). Available covariance bounds are
\(\bar c_j\ge\sup_{|h|\le1}\sum_{a,c}|C^{(j)}_{ac}(h)|\),
\(0\le j\le5\). For ordered spatial index lists \(\mathbf i\) of
length \(q\), initialize
\[
 P^{(0)}_{j,q}
   =\bigoplus_{\mathbf i\in\{1,\ldots,b\}^{q}}
       \mathcal E(\partial_h^j\partial_{Y_{\mathbf i}}\psi),
       \qquad j+\lceil q/2\rceil\le5.                     \tag{8.4.4}
\]
There is one empty list when \(q=0\). Whenever
\(r+j+\lceil q/2\rceil<5\), recurse by
\[
 P^{(r+1)}_{j,q}=P^{(r)}_{j+1,q}
    \oplus\bigoplus_{a=0}^{j}
      \left[(\tfrac12\tbinom ja\bar c_{a+1},0)
                          \odot P^{(r)}_{j-a,q+2}\right].  \tag{8.4.5}
\]
This follows by applying \(\partial_h^jD_Y^q\) to (8.3.2): Leibniz's
rule differentiates \(C'\) exactly \(a\) times. Aggregating absolute
values over all ordered indices, then multiplying by the entrywise
covariance bound, can only increase the bound. In particular it includes
both off-diagonal covariance entries. The strict guard ensures that
every child is available, that \(a+1\le5\), and that no
\(S^{[5]}\) is differentiated.

If \(P^{(r)}_{0,0}=(A_r,p_r)\), return
\[
 \overline{\mathcal J}_r(\mathcal T)
       =A_r\mu_{b,p_r}(\bar c_0),\qquad
 \mu_{b,p}(v)=\sum_{q=0}^{p}\binom pq v^{q/2}2^{q/2}
              \frac{\Gamma((b+q)/2)}{\Gamma(b/2)}.          \tag{8.4.6}
\]
Indeed, \(\|C^{1/2}G_b\|_2\le\sqrt{\bar c_0}\|G_b\|_2\).
Polar coordinates in the Gaussian integral give
\(E\|G_b\|_2^q=2^{q/2}\Gamma((b+q)/2)/\Gamma(b/2)\):
the angular factor cancels in the ratio of the radial integrals
\(\int_0^\infty r^{b+q-1}e^{-r^2/2}dr\) and
\(\int_0^\infty r^{b-1}e^{-r^2/2}dr\), and the substitution
\(u=r^2/2\) gives the stated ratio. Expansion of
\((1+\sqrt v\|G_b\|_2)^p\) proves (8.4.6). At \(v=0\), its
\(q=0\) term is one and its positive-order terms are zero.

Assemble each covariance by summing the bounds on its entries. For the
full coefficients (8.2.1)--(8.2.2), use
\[
 \bar R_j=\bar\rho_j+\bar Q_j+j\bar Q_{j-1},\qquad
 \bar T_j=\bar\sigma_j+\bar K_j+j\bar K_{j-1},             \tag{8.4.7}
\]
with negative-index terms zero and the diagonal \(\bar T_j=\bar\sigma_j\).
These formulas use the exact identity
\((hQ)^{(j)}=hQ^{(j)}+jQ^{(j-1)}\), including \(j=0\).

For the exact compiler use the same chronological calls and the exact
expressions \(\Psi_r\) in (8.3.2). Initialize jets of genuinely constant
scalar nodes by their values at order zero and zero at higher orders.
In each subsequent call, substitute the already computed jets for
earlier scalar tokens and define
\[
 \mathcal J_r(\mathcal T)
   =E_{Y\sim N(0,C(0))}\Psi_r(0,Y),\qquad0\le r\le5,
 \qquad
 S^{[j]}\big|_{h=0}=\mathcal J_j(S).                      \tag{8.4.8}
\]
Exact coefficient assembly uses
\(\mathcal J_j(R)=\mathcal J_j(\rho)+j\mathcal J_{j-1}(Q)\)
at zero, and the corresponding formula for \(T\), with zero
negative-index jets. Equations (8.2.1)--(8.2.6), (8.3.2), and (8.4.8)
therefore determine the terminal numbers
\(\mathcal J^{\mathrm{cmp}}_{r,N,L}\) without referring to an unknown
output derivative.

Here is the full regularity check that justifies both compilers. An
undifferentiated local state, Gram product, or output integrand contains
activation atoms of order at most one. A response first applies one
ambient source derivative, so its maximum atom order is at most two.
Within the guarded array at Price level \(r\), the additional number
of ordinary formal derivatives falling on an integrand is at most
\[
 2r+j+q\le10
       \quad\text{if }r+j+\lceil q/2\rceil\le5.           \tag{8.4.9}
\]
The response's one preliminary derivative is already included in its
atom order two. Thus \(\phi^{(12)}\) is sufficient, and
\(\phi^{(13)}\) is never requested. A scalar token needs at most five
\(h\)-derivatives; a covariance needs at most five as well. Higher
spatial derivatives do not differentiate scalar tokens.

At the first call, all coefficient and covariance inputs are constant
functions of \(h\). Suppose all earlier scalar outputs have continuous
derivatives and bounds through order five. Finite local syntax, the
chain and product rules, and (8.4.1)--(8.4.3) then supply jointly
continuous mixed derivatives (8.3.1) with one common polynomial
envelope. Its covariance is \(C^5\), by the earlier scalar outputs,
and is positive semidefinite by its Gram construction. Lemma 8.2 applies
and supplies the next scalar outputs and bounds. This is a finite
induction in Section 8.2's chronology, including the single call when
\(L=1\). It proves
\[
 |\mathcal T^{(r)}(h)|\le\overline{\mathcal J}_r(\mathcal T),
 \qquad \mathcal J_r(\mathcal T)=\mathcal T^{(r)}(0),
 \quad |h|\le1,\quad0\le r\le5.                          \tag{8.4.10}
\]

To make the activation-integral content of (8.4.8) explicit, put
\(\mu_{\phi'}=E\phi'(G)^2\). At zero step all responses vanish,
all time copies of a forward source on a layer coincide, and
\[
 Q_{\ell,jk}(0)=1,\qquad
 K_{\ell,jk}(0)=\mu_{\phi'}^{L-\ell+1}.                   \tag{8.4.11}
\]
These facts also follow from the zero-step calculation in Section 8.6.
One joint representation uses independent standard Gaussians
\(A,G_1,\ldots,G_L,B_1,\ldots,B_{L-1}\), with \(U=G_1\),
\(\xi_{\ell,k}=G_\ell\), and
\(\chi_{\ell,k}=\mu_{\phi'}^{(L-\ell+1)/2}B_{\ell-1}\).
Different physical layers retain their own independent marks.

Differentiate in the ambient source coordinates before making these
identifications. After substitution, every expanded term in (8.4.8)
is a product of ordinary Gaussian monomials and activation atoms at
individual standard Gaussians. Independence reduces its expectation to
finite products of ordinary Gaussian moments and integrals
\[
 I_{a,\boldsymbol\beta}(\phi)
   =E\left[G^a\prod_{j=0}^{12}
                    \phi^{(j)}(G)^{\beta_j}\right],
 \quad a,\beta_j\in\{0,1,2,\ldots\},\quad\phi^{(0)}=\phi.\tag{8.4.12}
\]
All are finite by (8.1.2). Carrier powers with odd Gaussian expectation
vanish; even powers of their standard deviations are integer powers of
\(\mu_{\phi'}\). Thus the coefficient (8.1.3) is an explicitly
terminating activation-integral expression. No reduction to a prescribed
small list of moments is asserted.

### 8.5. The explicit exponent and all its majorant obligations

The following constants are specified independently of any trajectory or
output supremum. For \(D=D_N=2N+2\), set
\[
 R_{N,0}=1,\qquad
 R_{N,k+1}=16(N+2)(R_{N,k}+1),
                  \quad0\le k<8(N+1),                    \tag{8.5.1}
\]
\[
 c_{N,0}=4(R_{N,8(N+1)}+1),\qquad
 c_{N,j+1}=64(D+1)^{10}(c_{N,j}+1)^2,
                  \quad0\le j<24,\qquad C_N=c_{N,24},    \tag{8.5.2}
\]
\[
 \nu_N=\mu_{D,C_N}((D+1)^2),\qquad
 \alpha_N=\left\lceil\log_2(2^{C_N}\nu_N)\right\rceil,
 \qquad p_N=2C_N,\quad r_N=C_N+\alpha_N.                  \tag{8.5.3}
\]
Here \(\mu_{b,p}\) is the explicit Gaussian moment expression
(8.4.6). Every recurrence has a finite displayed terminal index;
\(\nu_N\) is a positive finite number given by a finite sum,
\(\alpha_N\) is a specified nonnegative integer, and \(p_N>1\).
Finally the number of calls is
\[
 M_{L,N}=\begin{cases}(2N+1)(L-1),&L\ge2,\\1,&L=1.
                    \end{cases}                         \tag{8.5.4}
\]

**Lemma 8.3 (one-call bound).** Suppose every incoming scalar token and
its derivatives through order five have magnitude at most \(S\ge2\)
on \([-1,1]\), and every covariance entry has the same derivative
bounds. Every new scalar bound returned by one call, including full
coefficient assembly and covariance entrywise-bound assembly, is at most
\[
 B_\phi^{r_N}S^{p_N}.                                    \tag{8.5.5}
\]

**Proof.** Give a leaf size one, a unary activation node size one plus
its child size, and a binary sum or product size one plus its two child
sizes. Before counting, expand integer coefficients into signed unit
summands, expand every binomial multiplicity, and expand every covariance
contraction and ordered spatial-index sum. Factors of magnitude at most
one, such as \(1/2\), may be retained with their exact values and
bounded by one. Thus no large combinatorial constant is treated as a
unit-size bounded scalar token.

If the available expressions have size at most \(R\), a product of
at most three has size at most \(3R+2\). A sum of \(J\le2N+3\)
such products has size at most \(J(3R+3)-1\), which is bounded by
\(16(N+2)(R+1)\). This also dominates a single activation
assignment and the affine source-plus-history assignments. In a local
interior history there are at most the four assignments
\(Z^{(\ell)}_k,H^{(\ell)}_k,q^{(\ell)}_k,\Delta^{(\ell)}_k\)
per time slice. At the top replace \(q\) by \(W^{(L+1)}\);
at the bottom use the bottom state update. Thus \(4(N+1)\)
assignments suffice for every \(L\ge2\) call. The scalar unrolling
(8.2.6), including its terminal activation, uses fewer than
\(4(N+1)+2\le8(N+1)\) assignments. Equation (8.5.1) covers them
all. A terminal or Gram product has size at most twice the terminal
raw size plus one; a pre-response expression has no larger bound.
Both are below \(c_{N,0}\).

For a formal derivative in any one source coordinate or in \(h\),
structural induction gives
\[
 |\partial e|\le2(|e|+1)^2.                               \tag{8.5.6}
\]
For a sum use the sum of its two differentiated children and one sum
node. For a product use two product nodes and one sum node, containing
one differentiated and one unchanged child in each term. For an
activation use \(\phi^{(j+1)}(g)\partial g\), with the unchanged
child \(g\) and its differentiated copy. Substitution of the child
bounds in these three cases proves (8.5.6); leaves differentiate to a
leaf or zero. Token advancement changes no tree size.

There are at most ten mixed-derivative levels, one extra ambient
derivative for a response, one aggregation of at most \(D^{10}\)
ordered spatial lists, and five levels of (8.4.5). At one Price level
the expanded expression has at most
\[
 1+D^2\sum_{a=0}^{j}\binom ja\le1+32D^2                 \tag{8.5.7}
\]
summands, since \(j\le5\). Multiplication by a covariance token
and addition of these terms, or addition of \(D^{10}\) expressions,
are each bounded by one application of
\(c\mapsto64(D+1)^{10}(c+1)^2\). Equation (8.5.6) is bounded
by that map as well. The guard (8.4.9) limits the actual derivative
order; counting ten base derivative levels and five combination levels
is only a conservative size count, not a request for extra derivatives.

Two more applications cover full coefficient and covariance-bound
assembly: the former adds at most seven signed-unit terms at derivative
order at most five, and the latter adds at most \(D^2\) entry bounds.
Old entries in such an assembly are incoming tokens. The maximum size
along any branch therefore needs at most
\[
 10+1+1+5+2=19<24
\]
applications. In particular, \(C_N\) bounds syntax size, the number
of incoming-token occurrences, and polynomial-envelope degree, including
all integer and dimension multiplicities. For the degree assertion,
spatial leaves contribute degree one, sums take a maximum, products
add, and a zeroth activation preserves degree by (8.4.2); a positive
activation derivative has degree zero. Induction bounds degree by
the number of nodes.

The envelope coefficient of a tree of size at most \(C_N\) is at most
\[
 (2B_\phi)^{C_N}S^{C_N}.                                 \tag{8.5.8}
\]
Here each scalar leaf costs at most \(S\), each activation costs at
most \(B_\phi\), and the factor two per node absorbs the
\(1+A\) in (8.4.2) and sums. A formal structural induction can take
the common leaf/node base \(2B_\phi S\): for a sum of children the
extra node bounds their sum by the product of their bases times
\(2B_\phi S\); products multiply the child bounds; and
\(B_\phi(1+A)\le2B_\phi\max\{1,A\}\) handles an activation.

There is only one Gaussian-moment cost per returned bound. To see this
also for assembly after integration, regard an incoming scalar as a
constant integrand in the current call. A sum of bounds
\(A_i\mu_{b,p_i}(v)\) is at most
\((\sum_i A_i)\mu_{b,\max_i p_i}(v)\). Thus sums for (8.4.7)
and for entrywise covariance bounds can be assembled before applying
one common Gaussian-moment majorant. They do not cause a second
independent factor of \(\nu_N\).

The covariance used by the call has entrywise norm at most
\((D+1)^2S\). For \(b\le D\), couple \(G_b\) to the first
\(b\) coordinates of \(G_D\). Since \(S\ge1\),
\[
 \begin{aligned}
 \mu_{b,C_N}((D+1)^2S)
 &=E[1+(D+1)\sqrt S\|G_b\|_2]^{C_N}\\
 &\le S^{C_N/2}E[1+(D+1)\|G_D\|_2]^{C_N}
  =S^{C_N/2}\nu_N.\end{aligned}                          \tag{8.5.9}
\]
Combining (8.5.8)--(8.5.9), enlarging
\(S^{3C_N/2}\) to \(S^{2C_N}\), and using
\[
 2^{C_N}\nu_N\le2^{\alpha_N}\le B_\phi^{\alpha_N}
\]
gives (8.5.5). \(\square\)

Initialization supplies only genuinely constant functions of \(h\)
as free scalar inputs: units, zeros, the normalized initial forward
variance, and, if precomputed, the initial cotangent variances
\(\mu_{\phi'}^j\), \(0\le j\le L\). Their derivatives of positive
order are zero and their values are at most \(B_\phi^{2L}\), since
\(\mu_{\phi'}\le M_\phi^2\). This initialization bound is not applied
to derivatives of a nonconstant history node merely because its value
at zero step equals an initial variance. Every such node must first
pass through its chronological compiler call.

Starting at \(S_0=B_\phi^{2L}\), write \(S_j=B_\phi^{a_j}\) and use
Lemma 8.3 to obtain
\[
 a_0=2L,\qquad a_{j+1}=r_N+p_Na_j,
               \quad0\le j<M_{L,N}.                      \tag{8.5.10}
\]
The map increases positive inputs, so the new bound also bounds every
retained older token. Induction solves this scalar recurrence as
\[
 a_j=2L p_N^j+r_N\sum_{i=0}^{j-1}p_N^i.                  \tag{8.5.11}
\]
The terminal order-five bound is consequently
\[
 \overline{\mathcal J}_5(F_{N,L})\le B_\phi^{E_{L,N}},     \tag{8.5.12}
\]
where the promised explicit exponent is
\[
 E_{L,N}=2L p_N^{M_{L,N}}
           +r_N\frac{p_N^{M_{L,N}}-1}{p_N-1}.             \tag{8.5.13}
\]
The quotient is the finite integer geometric sum in (8.5.11).
There is no unspecified multiplicative constant in (8.5.12).

For later use, \(E_{L,N}\) is nondecreasing in \(N\). Increasing
\(N\) increases the multiplier and the number of iterations in
(8.5.1), and then the initial value and multiplier in (8.5.2).
Thus \(D_N,C_N\) are nondecreasing. Couple standard Gaussians by
initial coordinates as above; because \(1+(D+1)\|G_D\|_2\ge1\),
\(\nu_N\) is nondecreasing in both \(D_N\) and \(C_N\).
So are \(\alpha_N,p_N,r_N\). The number \(M_{L,N}\) increases
for \(L\ge2\) and stays one for \(L=1\). Finally (8.5.10)
iterates an increasing map that increases positive inputs. Increasing
its parameters and applying it no fewer times proves the assertion.

### 8.6. Parity and an explicit first-order cancellation calculation

The following symmetry holds without any parity assumption on \(\phi\).
Change \(h\) to \(-h\), change the top root \(A\) and every
backward source \(\chi_{\ell,k}\) to their negatives, and leave
\(U\) and every \(\xi_{\ell,k}\) fixed. Chronological induction
in (5.5.4)--(5.5.12) gives even transformation for
\(Z^{(\ell)},H^{(\ell)},Q_\ell,K_\ell\), and odd transformation
for \(W^{(L+1)},q^{(\ell)},\Delta^{(\ell)},\rho,\sigma,R,T\).
For a response, differentiating an even transformed feature with
respect to the sign-reversed backward coordinate supplies a minus sign;
differentiating an odd transformed cotangent with respect to an unchanged
forward coordinate retains its minus sign. Thus the response definitions
respect the induction. Gram entries are unchanged, so at the next call
the Gaussian covariance is unchanged; simultaneous negation of its
backward block preserves its centered Gaussian law. This proves the
law-level induction and, for all \(h\in[-1,1]\),
\[
 F_{N,L}(-h)=-F_{N,L}(h),\quad
 Q_\ell(-h)=Q_\ell(h),\quad K_\ell(-h)=K_\ell(h).         \tag{8.6.1}
\]
For \(L=1\), the same assertion follows immediately from (8.2.6)
under \((h,A)\mapsto(-h,-A)\).

In particular all responses vanish at zero, and all covariance matrices
in the calls have \(C'(0)=0\). At \(h=0\), the bottom state is
\(U\), all higher states equal their current forward sources, and
all forward variances equal one by normalization. A backward source
has the initialization cotangent variance of its upper layer. Descending
from \(\Delta^{(L)}=A\phi'(G_L)\) gives exactly (8.4.11).
In the coalesced representation, define the initial upper carrier on
layer \(\ell\) by
\[
 V_L=A,\qquad
 V_\ell=\mu_{\phi'}^{(L-\ell)/2}B_\ell\quad(\ell<L).
                                                               \tag{8.6.2}
\]
It is independent of \(G_\ell\), has second moment
\(\mu_{\phi'}^{L-\ell}\), and
\(\Delta^{(\ell)}_k(0)=V_\ell\phi'(G_\ell)\) for every
applicable \(k\).

Here is a direct computation of the first terminal jet, which also
checks that no covariance term is missing. A dot in the next calculation
means the explicit \(h\)-derivative of a local integrand at zero,
including earlier scalar-token derivatives and holding its ambient
Gaussian coordinates fixed. At first order, Lemma 8.2 reduces to
expectation of this dot, since \(C'(0)=0\).

For \(j<k\), define the deterministic numbers
\(b_{\ell,kj}=\rho_{\ell,kj}'(0)\), \(2\le\ell\le L\).
From the exact bottom identity
\(Z^{(1)}_k=U+h\sum_{j<k}\Delta^{(1)}_j\), differentiation
before collapsing the backward source coordinates gives
\[
 \partial_{\chi_{2,j}}\dot H^{(1)}_k=\phi'(U)^2,
 \qquad b_{2,kj}=\mu_{\phi'}.                            \tag{8.6.3}
\]
Indeed at zero the ambient bottom cotangent at time \(j\) is
\(\chi_{2,j}\phi'(U)\); other times use their own ambient coordinates.

For \(2\le\ell<L\), the analogous ambient calculation from
(8.2.3) gives
\[
 \dot H^{(\ell)}_k
   =\phi'(\xi_{\ell,k})
       \sum_{j<k}(1+b_{\ell,kj})
                      \chi_{\ell+1,j}\phi'(\xi_{\ell,j}).\tag{8.6.4}
\]
The factor one is \(Q_{\ell-1,jk}(0)\). Terms differentiating an
old cotangent are multiplied by \(R(0)=0\) and vanish. The
numbers \(b_{\ell,kj}\) are scalar tokens, hence are held fixed
by the ambient derivative. Take \(\partial_{\chi_{\ell+1,j}}\)
of (8.6.4), and only then set
\(\xi_{\ell,k}=\xi_{\ell,j}=G_\ell\). The first-jet Price formula
for the response gives
\[
 b_{\ell+1,kj}=\mu_{\phi'}(1+b_{\ell,kj}).                \tag{8.6.5}
\]
Together with (8.6.3), this finite layer induction yields
\[
 b_{\ell,kj}=\sum_{a=1}^{\ell-1}\mu_{\phi'}^a.
                                                               \tag{8.6.6}
\]
The result is independent of \(j,k\); no derivative of a backward
response was needed for this forward first-order calculation.

At the top, (8.2.3), (8.6.6), and the coalesced source law give
\[
 \dot H^{(L)}_N
    =N\left(\sum_{a=0}^{L-1}\mu_{\phi'}^a\right)
                       A\phi'(G_L)^2,
 \qquad
 \dot W^{(L+1)}_N=N\phi(G_L).                            \tag{8.6.7}
\]
For \(L=1\), these two equations follow directly from (8.2.6), with
the sum reduced to one and \(G_L=U\). Apply the first-jet Price
formula to the terminal product and use \(EA^2=1\),
\(E\phi(G_L)^2=1\). It gives
\[
 \mathcal J^{\mathrm{cmp}}_{1,N,L}
 =F_{N,L}'(0)
 =N+N\mu_{\phi'}\sum_{a=0}^{L-1}\mu_{\phi'}^a
 =N\sum_{a=0}^{L}\mu_{\phi'}^a.                          \tag{8.6.8}
\]
Thus every first-order contribution, including the effect of forward
reuse responses, has been evaluated inside the population compiler.
There was no differentiation of a finite-width limit. By oddness and
\(C^5\) regularity,
\[
 F_{N,L}(0)=F_{N,L}^{(2)}(0)=F_{N,L}^{(4)}(0)=0.          \tag{8.6.9}
\]

### 8.7. Taylor remainder, width identification, and scope

The elementary integral Taylor formula follows by repeated integration
of the fifth derivative:
\[
 F_{N,L}(u)=u\mathcal J^{\mathrm{cmp}}_{1,N,L}
        +\frac{u^3}{6}\mathcal J^{\mathrm{cmp}}_{3,N,L}
        +\frac1{4!}\int_0^u(u-v)^4F_{N,L}^{(5)}(v)\,dv,
        \qquad |u|\le1.                                 \tag{8.7.1}
\]
For negative \(u\), reverse the integration orientation to bound its
absolute value. In either direction the integral has magnitude at most
\(\overline{\mathcal J}_5(F_{N,L})|u|^5/120\).
Apply (8.7.1) at \(u=2h\) for \(N\) updates and at \(u=h\)
for \(2N\) updates. Equation (8.6.8) cancels the two linear terms,
and (8.1.3) is exactly the remaining cubic coefficient. Therefore
\[
 \begin{aligned}
 &|F_{N,L}(2h)-F_{2N,L}(h)
                      -\mathcal C^{\mathrm{cmp}}_{\phi,L,N}h^3|\\
 &\qquad\le
   \frac{32\overline{\mathcal J}_5(F_{N,L})
                   +\overline{\mathcal J}_5(F_{2N,L})}{120}|h|^5,
       \qquad |h|\le\tfrac12.\end{aligned}                \tag{8.7.2}
\]
Monotonicity of \(E_{L,N}\), (8.5.12), and \(33/120<1\) prove
(8.1.5). Equations (8.4.10) and (8.5.12) prove (8.1.4).

It remains to verify the network interpretation at exactly the scope
available internally. Conditions (8.1.1)--(8.1.2) imply (5.1.1)--(5.1.2),
for example with \(M=2M_\phi\). For each separately fixed
\(h\ne0\), apply the fixed-program theorem of Section 5.1 once to
\((L,N,2h)\) and once to \((L,2N,h)\). Its initialization and
stored-coordinate mobilities are precisely those in Section 8.1, and
its output program is the one reorganized in Section 8.2. For a
nonconstant activation its strict-rank proof includes the affine case;
its joint coupling and terminal uniform integrability establish the
convergence of expectations in (8.1.6). No new uniform-in-\(h\)
conditioning gap is inferred from that theorem. For \(L=1\), its
separate iid coordinate argument applies directly.

At \(h=0\) every finite update is the identity. The initialized hidden
features are independent of the centered stored readout, so conditioning
on those features gives \(E f_{n,L}^{N}(0)=0\) for every finite
\(n,L,N\). These expectations exist by the Gaussian initialization
and finite linear-growth network. The population program has the
zero-step law in (8.4.11), with terminal product
\(A\phi(G_L)\) (or \(A\phi(U)\) if \(L=1\)); its expectation
is zero as well. This separate calculation establishes agreement at
zero without applying Section 5's punctured-step rank theorem there.

If \(\mu_{\phi'}=0\), continuity of \(\phi'\) and the strictly
positive standard Gaussian density imply \(\phi'\equiv0\): any
nonzero derivative value would have a neighborhood with positive
integral of its square. Normalization then gives \(\phi\equiv c\)
with \(c\in\{-1,1\}\). Every cotangent is zero and the stored
readout is \(W^{(L+1)}_N=W^{(L+1)}_0+Nhc\,\mathbf1\).
Its prediction expectation is \(Nh\), at every width and in the
population program. This proves the constant branch of Theorem 8.1.
\(\square\)

An optional shared activation-only radius base is
\(h_\phi=(2B_\phi)^{-1}\). Since \(B_\phi\ge4\) and
\(E_{L,2N}\ge1\), the smaller explicit domain
\(|h|\le h_\phi^{E_{L,2N}}\) is contained in \(|h|\le1/2\)
and satisfies the same bound (8.1.5). For \(L=3\), substitution gives
\[
 M_{3,2N}=8N+2,\qquad
 E_{3,2N}=6p_{2N}^{8N+2}
       +r_{2N}\frac{p_{2N}^{8N+2}-1}{p_{2N}-1}.           \tag{8.7.3}
\]
For every \(\varepsilon>0\), a fully explicit cubic comparison is
\[
 |F_{N,L}(2h)-F_{2N,L}(h)|
       \le (|\mathcal C^{\mathrm{cmp}}_{\phi,L,N}|+\varepsilon)|h|^3
                                                               \tag{8.7.4}
\]
whenever
\[
 |h|\le\min\left\{\tfrac12,
           \sqrt{\frac{\varepsilon}{1+B_\phi^{E_{L,2N}}}}\right\}.
                                                               \tag{8.7.5}
\]
Indeed the fifth-order error divided by \(|h|^3\), for \(h\ne0\),
is then at most
\(\varepsilon B_\phi^{E_{L,2N}}/(1+B_\phi^{E_{L,2N}})\le\varepsilon\);
the zero-step case is already established.

All conclusions are for fixed finite \(L,N\), the specified order-one
stored readout, and exact feature-ascent updates. The equality of the
two accumulated feature-step lengths, \(N(2h)=(2N)h\), is the
comparison used here; it does not identify either scheme with an exact
physical-time loss-gradient flow. The coefficient is the full finite
compiler (8.4.8), with no compact nine-moment identity substituted for
it. The exponent is allowed to grow with \(N\). Nothing here proves
a growing-step-count width limit, a bound proportional to \(N^4|h|^5\)
on a domain proportional to \(1/N\), convergence of an infinite Taylor
series, or a continuous-time limit.

## 9. Finite loss-GD pullback calculus

This section concerns a finite-dimensional Euler map at a supplied
state. It complements the moving continuous-flow jets and the fixed-program
Gaussian feature-ascent theorem: here the scalar residual is recomputed in
every raw loss-GD update. The result requires no initialization distribution,
Gaussian parity, population metric, or width-limit identification.

### 9.1. Raw mobilities, full square loss, and the Euler map

Flatten the finite stored parameters into a Euclidean vector \(\theta\).
Let \(D\) be a fixed positive-definite symmetric mobility matrix. For the
canonical width-\(n\), depth-\(L\) network, its blocks are
\[
 D=\operatorname{diag}
 (n\kappa_1 I,\kappa_2 I,\ldots,\kappa_L I,
                      n\kappa_{L+1}I),                 \tag{9.P1}
\]
with identities of the corresponding flattened block sizes. These are
ordinary Euclidean/Frobenius coordinates and the actual raw mobilities.
Put \(x=D^{-1/2}\theta\), and write the predictor in these coordinates as
\(f(x):=f_n(D^{1/2}x)\). This notation is restricted to this section.
For one sample with arbitrary label \(y\), use exactly the shared convention
\[
 r(x)=f(x)-y,\qquad \mathcal L(x)=r(x)^2,
 \qquad P(x)=-\mathcal L(x),\qquad v(x)=\nabla P(x).
                                                               \tag{9.P2}
\]
The chain rule gives
\(\nabla_x\mathcal L=D^{1/2}\nabla_\theta\mathcal L_n\).
Consequently the raw update and its coordinate representation are
\[
 \theta^+=\theta-\eta D\nabla_\theta\mathcal L_n,
 \qquad x^+=E_\eta x:=x+\eta v(x),
 \qquad v=-2r\nabla f.                                  \tag{9.P3}
\]
Thus \(\eta\) is the actual loss-GD step, and \(N\) below counts updates;
neither is physical time. The change of coordinates is linear and hence
preserves this exact Euler update. The residual in (9.P3) moves with the state.
The same coordinate argument applies to a fixed-batch mean-square loss
\(m^{-1}\sum_a(f_a-y_a)^2\), with \(P=-\mathcal L\); only the
one-sample specialization below uses the scalar factor in (9.P3).

We first allow any scalar observable \(u\) and vector field \(v\) on an
open subset of a finite-dimensional Euclidean space. Suppose both are
\(C^6\). For a fixed integer \(N\ge1\), choose an interval of steps
containing zero on which all iterates in
\[
 d_N^u(\eta)=u(E_\eta^{2N}x_0)-u(E_{2\eta}^{N}x_0)       \tag{9.P4}
\]
are defined in that open set. Such an interval exists locally for each
fixed \(N\), by continuity and the fact that every zero-step state is
\(x_0\). The paired scalar map is \(C^6\) on this interval by finite
composition. For \(v=\nabla P\), the sufficient hypothesis \(P\in C^7\)
ensures this regularity; the assumption is on the finite function, not on
an unidentified population state.

### 9.2. Exact finite operator words and their coefficient recursion

For an integer \(k\ge1\), define
\[
 \mathcal T_k u(x)=\frac1{k!}D^k u(x)[v(x),\ldots,v(x)].  \tag{9.P5}
\]
The vector \(v(x)\) is held fixed inside the displayed derivative of
\(u\). The resulting function \(\mathcal T_k u\) still depends on the
state; an outer operator differentiates that dependence. For example,
\[
 \mathcal T_1^2u=D^2u[v,v]+Du[Dv\,v],
 \qquad \mathcal T_2u=\tfrac12D^2u[v,v].                \tag{9.P6}
\]
Thus replacing a moving vector field by its initial value would already
lose a term at order two.

For integers \(1\le q\le j\), set
\[
 \mathcal W_{j,q}=
 \sum_{\substack{k_1+\cdots+k_q=j\\ k_i\ge1}}
       \mathcal T_{k_1}\cdots\mathcal T_{k_q},
 \qquad \Lambda_{j,q}=(\mathcal W_{j,q}u)(x_0).          \tag{9.P7}
\]
Products act from right to left. The finite recurrence is
\[
 U_{0,0}=u,\qquad U_{j,0}=0\ (j>0),\qquad
 U_{j,q}=0\ (j<q),
\]
\[
 U_{j,q}=\sum_{k=1}^{j-q+1}\mathcal T_kU_{j-k,q-1},
 \qquad \Lambda_{j,q}=U_{j,q}(x_0).                     \tag{9.P8}
\]
Partitioning the compositions in (9.P7) by their first part proves (9.P8);
every recursive call decreases the total order. This recurrence is a
finite derivative prescription, not a convergent infinite series.

Writing \([\eta^j]\) for the ordinary Taylor coefficient at zero, we have
\[
 [\eta^j]u(E_\eta^M x_0)
       =\sum_{q=1}^j\binom Mq\Lambda_{j,q},
 \qquad j\ge1,                                      \tag{9.P9}
\]
provided \(u,v\in C^j\) near \(x_0\) for that fixed order; the present
\(C^6\) hypotheses cover all orders needed below. Here \(M\) is any
nonnegative integer and \(\binom Mq=0\)
when \(q>M\). At order zero the coefficient is \(u(x_0)\).

To prove (9.P9), let \(\mathcal P_\eta u=u\circ E_\eta\).
The exact operator \(\mathcal B_\eta=\mathcal P_\eta-I\) satisfies
\[
 \mathcal P_\eta^M=(I+\mathcal B_\eta)^M
             =\sum_{q=0}^M\binom Mq\mathcal B_\eta^q.   \tag{9.P10}
\]
This binomial formula uses the single operator \(\mathcal B_\eta\);
it does not assume that different \(\mathcal T_k\)'s commute.
Taylor differentiation of \(u(x+\eta v(x))\) at zero gives
\([\eta^k]\mathcal B_\eta u=\mathcal T_k u\).
At a finite target degree \(j\), apply the product and chain rules to
the finite product in (9.P10): every factor must contribute positive order,
and the choices \(k_1+\cdots+k_q=j\) contribute precisely (9.P7).
No term with \(q>j\) contributes. For \(j\le5\), this operation
differentiates \(u\) at most \(j\) times and \(v\) at most \(j-1\)
times, within the stated regularity. Equivalently one may work with finite
Taylor polynomials modulo degree \(j+1\); no convergent infinite
operator expansion or operator-norm remainder is used. Evaluation at
\(x_0\) proves (9.P9).

Subtracting the coarse update in (9.P4) now gives
\[
 [\eta^j]d_N^u=\sum_{q=1}^jQ_{j,q}(N)\Lambda_{j,q},
 \qquad Q_{j,q}(N)=\binom{2N}q-2^j\binom Nq.          \tag{9.P11}
\]
The zero and first coefficients vanish. Every polynomial \(Q_{j,q}\)
has degree at most \(j-1\): if \(q<j\) this follows from its degree
\(q\), while if \(q=j\) the two leading coefficients are both
\(2^j/j!\) and cancel. This is a term-by-term cancellation and does not
require relations between the \(\Lambda_{j,q}\)'s.

### 9.3. The complete temporal table through degree five

The rows of (9.P11), in increasing \(q\), are
\[
\begin{array}{c|lllll}
j\backslash q&1&2&3&4&5\\ \hline
2&-2N&N\\
3&-6N&-2N^2+3N&2N(N-1)\\
4&-14N&-6N^2+7N&-\frac43N^3+6N^2-\frac{14}3N
 &2N^3-\frac{11}2N^2+\frac72N\\
5&-30N&-14N^2+15N&-4N^3+14N^2-10N
 &-\frac23N^4+6N^3-\frac{77}6N^2+\frac{15}2N
 &\frac43N^4-7N^3+\frac{35}3N^2-6N.
\end{array}                                                   \tag{9.P12}
\]
Each entry is obtained by multiplying the finite factors in
\(\binom Nq=N(N-1)\cdots(N-q+1)/q!\) and applying (9.P11).
Thus (9.P7)--(9.P8) and (9.P12) specify every coefficient through order five,
including every operator ordering, without a stored neural coefficient
table or an unspecified derivative compiler.

Taylor's integral formula yields the exact equality
\[
 d_N^u(\eta)=\sum_{j=2}^5\eta^j
             \sum_{q=1}^jQ_{j,q}(N)\Lambda_{j,q}
 +\frac{\eta^6}{5!}\int_0^1(1-s)^5
                    (d_N^u)^{(6)}(s\eta)\,ds.         \tag{9.P13}
\]
The superscript denotes the sixth derivative of the scalar function with
respect to its own step argument, evaluated at \(s\eta\). The entire
segment between zero and \(\eta\) lies in the chosen step interval,
so the stated \(C^6\) hypothesis verifies the integral formula's
assumption. This is a fixed-\(N\) identity; it supplies no uniform bound
on that derivative as \(N\) grows.

### 9.4. Generic cubic loss formula at arbitrary residual

For \(v=\nabla P\) and \(u=\mathcal L=-P\), put, at \(x_0\),
\[
 b=\nabla P,\quad H_P=\nabla^2P,\quad
 T_P=\langle b,H_Pb\rangle,\quad
 S_P=\|H_Pb\|_2^2,\quad U_P=D^3P[b,b,b].             \tag{9.P14}
\]
Then
\[
 d_N^{\mathcal L}(\eta)
 =-NT_P\eta^2-\frac{N(2N-1)}2(4S_P+U_P)\eta^3
                                  +O_N(\eta^4).       \tag{9.P15}
\]
Here is a direct derivation independent of the temporal table. For a
general \(v,u\), let \(a=Dv\,v\),
\(b_2=Dv(Dv\,v)\), and \(b_3=D^2v[v,v]\), all at \(x_0\).
Insertion of a cubic series in the Euler recurrence gives
\[
 E_\eta^M x_0=x_0+M\eta v+\binom M2\eta^2a
 +\eta^3\left\{\binom M3b_2+
            \frac{M(M-1)(2M-1)}{12}b_3\right\}
 +O_M(\eta^4).                                       \tag{9.P16}
\]
Indeed the quadratic increment at update \(k\) is \(k a\), and
the cubic increment is \(\binom k2 b_2+k^2 b_3/2\).
Summing uses
\(\sum_{k<M}k=\binom M2\),
\(\sum_{k<M}\binom k2=\binom M3\), and
\(\sum_{k<M}k^2/2=M(M-1)(2M-1)/12\). Taylor expansion of
\(u\) along (9.P16) shows that the quadratic paired coefficient is
\(N Du[a]\), and the cubic paired coefficient is
\[
 2N(N-1)Du[b_2]+\frac{N(2N-1)}2Du[b_3]
                       +2N^2D^2u[v,a].                \tag{9.P17}
\]
The terms \(M^2D^2u[v,v]/2\) at order two and
\(M^3D^3u[v,v,v]/6\) at order three cancel at equal elapsed time.
For \(v=\nabla P\), symmetry of \(H_P\) gives, in the order used
in (9.P17),
\[
 Du[a]=-T_P,\quad Du[b_2]=-S_P,\quad
 Du[b_3]=-U_P,\quad D^2u[v,a]=-S_P.
\]
For example \(\langle b,H_P^2b\rangle=\|H_Pb\|_2^2\),
and \(\langle b,D^2(\nabla P)[b,b]\rangle=D^3P[b,b,b]\).
Substitution proves (9.P15).

For the one-sample full square loss in (9.P2), additionally assume that
the predictor \(f\) is \(C^3\) near the supplied state for (9.P18)–(9.P21).
This is separate from the loss-field regularity used for the remainder:
a smooth squared loss alone need not make its predictor \(C^3\). Define
at the same arbitrary state
\[
 g=\nabla f,\quad H_f=\nabla^2f,\quad K=\|g\|_2^2,
 \quad B=\langle g,H_fg\rangle,\quad
 S=\|H_fg\|_2^2,\quad U=D^3f[g,g,g].                 \tag{9.P18}
\]
Since \(P=-r^2\),
\[
 b=-2rg,\qquad H_P=-2g\otimes g-2rH_f,
 \qquad H_Pb=4rK g+4r^2H_fg.
\]
Here \(g\otimes g\) is the ordinary Euclidean outer product on these
finite parameter coordinates. Taking the pairing and squared norm gives
\[
 T_P=-8r^2K^2-8r^3B,\qquad
 S_P=16r^2K^3+32r^3KB+16r^4S.                          \tag{9.P19}
\]
The product rule gives
\[
 D^3P[a_1,a_2,a_3]
 =-2rD^3f[a_1,a_2,a_3]
 -2\sum_{\mathrm{cyc}}Df[a_1]D^2f[a_2,a_3].           \tag{9.P20}
\]
Putting \(a_1=a_2=a_3=-2rg\) yields
\(U_P=16r^4U+48r^3KB\). Therefore
\[
\begin{aligned}
 d_N^{\mathcal L}(\eta)={}&8N(r^2K^2+r^3B)\eta^2\\
 &-8N(2N-1)
       (4r^2K^3+11r^3KB+4r^4S+r^4U)\eta^3
       +O_N(\eta^4).                                  \tag{9.P21}
\end{aligned}
\]
No parity or zero-output assumption was used. If \(r=0\) or \(g=0\)
at the supplied state, \(v=0\) there, every Euler iterate stays there,
and the entire paired difference is zero. For an affine predictor,
\(K\) is constant and \(B=S=U=0\); the exact expression is
\[
 r(x_0)^2\{(1-2K\eta)^{4N}-(1-4K\eta)^{2N}\},
\]
which has precisely the quadratic and cubic coefficients in (9.P21).

### 9.5. A convex-tube bound and the fixed-order boundary

Assume separately that a convex set \(C\) lies in the open domain of
\(C^1\) functions \(v,u\), with
\[
 \|v(x)\|_2\le M_T,\qquad \|Dv(x)\|_{\rm op}\le L_T,
 \qquad \|Du(x)\|_{\rm op}\le R_T\quad(x\in C).       \tag{9.P22}
\]
Take \(\eta\ge0\), \(2N\eta\le T\). Write
\(A=E_\eta^2\), \(B_0=E_{2\eta}\). Require that every composition
of at most \(N\) maps chosen from \(A,B_0\), starting at \(x_0\),
and every intermediate \(E_\eta\) state within such a composition,
lies in \(C\). This explicitly includes both Euler paths and all
hybrid paths used to compare them. Convexity includes the straight
segments needed for the derivative estimates; endpoint bounds on just two
paths would not suffice.

For such a starting state, the exact local defect is
\[
 Ax-B_0x=\eta\{v(x+\eta v(x))-v(x)\},
 \qquad \|Ax-B_0x\|_2\le L_TM_T\eta^2.                \tag{9.P23}
\]
Indeed, integrate \(Dv\) on the segment from \(x\) to
\(x+\eta v(x)\) and use (9.P22). Integrating \(Dv\) on a segment
between any two points of \(C\) also gives
\(\|E_\eta x-E_\eta y\|_2\le(1+\eta L_T)\|x-y\|_2\).
The same estimate twice bounds each fine macro-step by
\((1+\eta L_T)^2\) on the relevant pairs of states.

Telescope the \(N+1\) endpoints
\(A^{N-i}B_0^i x_0\), \(0\le i\le N\).
The difference between consecutive endpoints first creates one local
defect (9.P23), then propagates through at most \(N-1\) fine macro-steps.
Thus
\[
 \|E_\eta^{2N}x_0-E_{2\eta}^{N}x_0\|_2
 \le L_TM_T\eta^2\sum_{i=0}^{N-1}(1+\eta L_T)^{2i}
 \le L_TM_TN\eta^2e^{2L_TN\eta}.                       \tag{9.P24}
\]
Integrating \(Du\) between the two endpoints proves
\[
 |d_N^u(\eta)|\le R_TL_TM_TN\eta^2e^{2L_TN\eta},
 \qquad
 |d_N^u(T/(2N))|\le
       \frac{R_TL_TM_TT^2e^{L_TT}}{4N}.                \tag{9.P25}
\]
These expressions remain valid when any bound is zero. If (9.P22) and the
tube inclusion hold with the same constants for all dyadic refinements,
then (9.P25) is summable and the terminal scalar Euler sequence is Cauchy.
Equation (9.P24) gives the corresponding terminal state assertion.
This is a conditional finite-dimensional estimate, not a population
existence, identification, or arbitrary-partition theorem.

By contrast, the degree bound following (9.P11) says only that each individual
fixed-order term is \(O_{j,T}(N^{-1})\) at \(\eta=T/(2N)\).
The coefficient \(\Lambda_{j,q}\) remains fixed because the state,
observable, and vector field are fixed. That algebra does not control
the remainder in (9.P13) or the sum over increasing orders, and does not
verify the tube assumption (9.P22). In particular it cannot replace either
a width-uniform estimate or identification of a common population state.

### 9.6. Exact rational interface and independent checks

The existing `pde.exact_calculus` module supplies two small operations:

- `euler_pullback_words(order, steps)` returns a fresh dictionary from
  positive composition tuples `(k1,...,kq)` of `order` to the exact
  `Fraction` weight `binom(steps,q)`. Products act right to left as in
  (9.P7). Zero weights are omitted. Order zero returns `{(): Fraction(1)}`;
  a positive order with zero steps returns `{}`.
- `paired_euler_weights(order)` returns the `order` rows in (9.P11), each
  an immutable tuple of `order` rational coefficients in increasing powers
  of `N`. The degree-`order` coefficient cancels and is omitted. Order zero
  returns `()`; order one returns `((Fraction(0),),)`.

Both inputs must be nonnegative Python integers; booleans, floats and
`Fraction` inputs are rejected. No derivatives, network states, activation
moments or Gaussian expectations are evaluated by either operation.

For the first operation, a finite stack appends every possible positive
next part until the remaining degree is zero or the allowed word length
is exhausted. Every composition is reached once, proving completeness
and uniqueness; choosing its \(q\) active update slots gives the weight
\(\binom Mq\) in (9.P9). At degree \(j\ge1\), unrestricted compositions
number \(2^{j-1}\): the \(j-1\) gaps between unit symbols are independently
cut or not cut. Tuple construction therefore costs at most
\(O(j2^j)\) operations and storage; the degree is a caller-chosen finite
bound, not a promised efficient high-order regime.

The second operation recursively multiplies
\(\binom Nq=\binom N{q-1}(N-q+1)/q\) and multiplies its degree-\(k\)
coefficient by \(2^k-2^j\). This proves the emitted coefficient rows
directly from (9.P11). It uses \(O(j^2)\) rational operations and storage.
Both routines use exact integer/rational arithmetic; bit lengths can grow,
and neither retains a cache, mutates inputs, draws samples, or writes files.

The deterministic tests independently enumerate active update slots, check
every displayed rational polynomial, and compare differential-word evaluation
with direct scalar polynomial Euler composition for \(v(x)=1+x^2\),
\(u(x)=2x+x^3\), at \(x_0=1/3\) through degree six. That last comparison
checks moving-field differentiation and operator ordering using a different
construction. Domain rejection and return ownership are also checked. These checks do not establish a neural width limit or an analytic remainder bound.

## 10. Positive-metric and Taylor obstructions for the quadratic formal jet

This section uses the one-sample, two-hidden-layer raw-square model of
Section 7.2, with independent standard Gaussian initialization and an
order-one stored readout. It proves two statements about its formal annealed
initialization jet: the negative moment witness persists when every block
has positive mobility, and the canonical positive Taylor closures fail to
converge uniformly on a time interval containing initialization. Neither
statement identifies a positive-time population trajectory.

### 10.1. Model and normalized derivative forests

Take the single input and label to be \(x=y=1\), input dimension \(d=1\),
both hidden widths \(n\), and activation \(\phi(v)=v^2\). Write the stored
parameters as
\[
 W^{(1)}_j=u_j,\qquad W^{(2)}_{ij}=g_{ij}/\sqrt n,
 \qquad W^{(3)}_i=a_i,
\]
where all \(a_i,u_j,g_{ij}\) are independent \(N(0,1)\) initially. Thus
\[
 z_i=\frac1{\sqrt n}\sum_j g_{ij}u_j^2,\qquad
 f_n=\frac1n\sum_i a_i z_i^2
     =\frac1{n^2}\sum_{i,j,l}a_i g_{ij}g_{il}u_j^2u_l^2.
 \tag{10.1}
\]
The mobility multipliers in the stored first, second, and readout blocks
are respectively \(n\alpha,\beta,n\). Equivalently, in the coordinates
\((u,g,a)\), define the feature-ascent derivation
\[
 D_{\alpha,\beta,n}
 =n\left(\nabla_a f_n\cdot\nabla_a
       +\alpha\nabla_u f_n\cdot\nabla_u
       +\beta\nabla_g f_n\cdot\nabla_g\right),
 \qquad \alpha,\beta\ge0.
 \tag{10.2}
\]
Indeed \(\partial_{W^{(2)}}=\sqrt n\,\partial_g\) and
\(dg/ds=\sqrt n\,dW^{(2)}/ds\), giving the stated factor \(n\beta\).
The canonical block metric here is \((\alpha,\beta)=(1,1)\); the frozen
first-block boundary in Section 7.2 is \((0,1)\).

Direct differentiation of (10.1) gives the primitive rules
\[
\begin{aligned}
 D_{\alpha,\beta,n}a_i
   &=\frac1n\sum_{j,l}g_{ij}g_{il}u_j^2u_l^2,\\
 D_{\alpha,\beta,n}u_j
   &=\frac{4\alpha}{n}\sum_{i,l}a_i g_{ij}g_{il}u_j u_l^2,\\
 D_{\alpha,\beta,n}g_{ij}
   &=\frac{2\beta}{n}\sum_l a_i g_{il}u_j^2u_l^2.
\end{aligned}
 \tag{10.3}
\]
No trained variables have been replaced by independent copies in these
identities.

For completeness, define the finite objects to which the forest
factorization applies. Let \(H\) be a finite simple bipartite forest, with
row vertices \(R\), column vertices \(C\), edge set \(E\), \(e=|E|\), and
\(r\) connected components, including isolated vertices. A row \(v\) has
decoration \(p_v\ge0\); a column \(w\) has decoration \(2q_w\ge0\).
Its normalized random sum is
\[
 S_{H,n}=n^{-e/2-r}
 \sum_{i:R\to\{1,\ldots,n\}}
 \sum_{j:C\to\{1,\ldots,n\}}
 \prod_{v\in R}a_{i(v)}^{p_v}
 \prod_{w\in C}u_{j(w)}^{2q_w}
 \prod_{(v,w)\in E}g_{i(v),j(w)}.
 \tag{10.4}
\]
Both maps in these sums are unrestricted. Distinct abstract vertices may
receive the same numerical neuron label. The initial output (10.1) is the
sum for the three-vertex tree with one row of decoration one, two columns
of decoration two, and the two incident edges.

Applying (10.3) and the product rule to (10.4) gives exactly the following
three rewrites.

1. At a row with \(p_v>0\), lower \(p_v\) by one and attach two fresh column
   leaves, each of decoration two, to that row. Multiply by \(p_v\).
2. At a column with \(q_w>0\), retain its decoration, add a fresh row of
   decoration one joined to that column, and join the new row to a fresh
   column of decoration two. Multiply by \(8\alpha q_w\).
3. At an edge \((v,w)\), remove that edge, increase \(p_v\) by one and
   \(2q_w\) by two, and attach a fresh column of decoration two to \(v\).
   Multiply by \(2\beta\).

In the first two cases \(e\) increases by two and \(r\) is unchanged. In the
third case the removed edge is a bridge: \(r\) increases by one, while
removing one edge and adding one leaf edge leaves \(e\) unchanged. Every
result is again a simple forest. In all cases its exponent \(e/2+r\)
increases by one, exactly accounting for \(1/n\) in (10.3). The stated
multiplicities are the ordinary derivatives of the decorations or of the
single edge factor. Numerical coincidences among the summed labels do not
invalidate the product rule; they are included separately in each
unrestricted sum before and after differentiation.

It follows by induction that, for each fixed \(k\),
\(D_{\alpha,\beta,n}^k f_n\) is a finite linear combination of these
normalized forests. The combination is independent of \(n\), and its
coefficients are polynomials in \(\alpha,\beta\) of total degree at most
\(k\), with nonnegative coefficients. This assertion gives a finite
algebraic description; it does not require enumeration of that description.

Here is the expectation argument, also proved in Section 7.2. For a fixed
forest, an odd edge count gives expectation zero by Gaussian symmetry.
If \(e=2b\), expand the expectation of its edge factors into Gaussian
pairings. The pairing formula follows by repeatedly applying
\(E[G P(G)]=E[P'(G)]\) to a Gaussian coordinate; the identity itself is
integration by parts against the Gaussian density for a polynomial \(P\),
whose boundary term vanishes. Pairing two edge occurrences forces equality
of their row labels and equality of their column labels.

Identify those endpoints and replace each pair by one covariance edge.
The resulting multigraph has \(b\) edges, say \(v\) vertices and \(c\)
components. Identifications cannot increase the number of components, so
\(c\le r\). Each connected graph on \(v_0\) vertices has at least \(v_0-1\)
edges: grow its reachable vertex set from one vertex, using one distinct
edge for each new vertex. Summing this bound over components gives
\[
 v\le b+c\le b+r.
 \tag{10.5}
\]
If its two populations have \(v_R,v_C\) vertices, labelings with no further
equality within either population number
\((n)_{v_R}(n)_{v_C}=n^v+O(n^{v-1})\). For those labelings the decoration
expectation is the product of the Gaussian moments at the quotient
vertices. Labelings with an additional equality number \(O(n^{v-1})\),
by choosing an equal pair and then all remaining labels. Their decoration
moments are bounded by a fixed constant, because the total decorations
are fixed. This pairing therefore contributes
\[
 C_H n^{v-b-r}+O(n^{v-b-r-1})
\]
for a fixed nonnegative Gaussian-moment product \(C_H\). There are finitely
many pairings, and (10.5) makes all their exponents nonpositive. Thus
\(E S_{H,n}\) has a finite limit.

Only \(v=b+r\) survives. It forces \(c=r\), so no surviving edge pairing
joins two original components, and each quotient component has one fewer
edge than vertices. The surviving pairings are consequently exactly the
independent choices of surviving pairings for the original components.
Their moments multiply, proving expectation factorization. This proof also
includes isolated vertices and components with odd edge count, which have
no internal complete pairing.

Applying this result to the finite derivative expansion proves existence of
\[
 d_k(\alpha,\beta)
 :=\lim_{n\to\infty}E[D_{\alpha,\beta,n}^k f_n],
 \qquad k\text{ fixed}.
 \tag{10.6}
\]
Each \(d_k\) is a polynomial of total degree at most \(k\) in the two
mobility multipliers. Its coefficients are nonnegative. Also \(d_{2j}=0\):
\(f_n\) has total primitive degree seven, and (10.3) has degree six, so
every nonzero \(k\)-fold derivative has degree \(7+5k\). This degree is
odd for even \(k\); simultaneous Gaussian sign reversal makes its
expectation zero.

The assertions here concern the annealed quantities (10.6), with \(k\)
fixed before the width limit. No concentration assertion, infinite-order
limit exchange, or trajectory-identification statement is used below.

### 10.2. A strictly positive metric with a negative moment witness

Fix \(\beta=1\) and form the formal series
\[
 F_\alpha(s)=\sum_{k\ge0}d_k(\alpha,1)\frac{s^k}{k!}.
\]
The series is odd. At \(\alpha=0\), Section 7.2 proves \(d_1(0,1)=63\).
Polynomial dependence therefore makes \(d_1(\alpha,1)\) nonzero on some
open real interval containing zero. On this interval the formal inverse
\(B_\alpha=F_\alpha^{-1}\) exists. Define the coefficients \(\mu_j(\alpha)\)
by the formal identity
\[
 F_\alpha'(B_\alpha(y))
 =d_1(\alpha,1)+y^2\sum_{j\ge0}(-1)^j\mu_j(\alpha)y^{2j}.
 \tag{10.7}
\]
Oddness of \(F_\alpha\) and uniqueness of its inverse make \(B_\alpha\)
odd, so the composed derivative in (10.7) is even. These definitions use
no convergence of \(F_\alpha\).

To verify the required continuity, write \(a_k=d_k(\alpha,1)/k!\) and
\(B_\alpha(y)=\sum_{k\ge1}b_k y^k\). The coefficient equation for
\(F_\alpha(B_\alpha(y))=y\) is
\[
 b_1=1/a_1,\qquad
 b_k=-\frac1{a_1}[y^k]\sum_{j=2}^k a_j
               \left(\sum_{l=1}^{k-1}b_l y^l\right)^j\quad(k\ge2).
 \tag{10.8}
\]
Only the linear term can involve the unknown \(b_k\), proving this formula
and uniqueness inductively. Thus every fixed \(b_k\), and every fixed
\(\mu_j\) obtained by substitution in (10.7), is a rational function of
finitely many \(a_k\), whose possible denominators are powers of \(a_1\).
In particular \(\mu_1,\ldots,\mu_5\) are continuous near \(\alpha=0\),
using only the jet through \(d_{13}\).

The exact boundary calculation in Section 7.2, equations (7.C3)--(7.C11),
supplies the fixed polynomial
\[
 p(\lambda)=v_0+v_1\lambda+\lambda^2,\qquad
 v_0=\frac{40042013405871059816}{2310453239160606810795},\quad
 v_1=-\frac{14165989123115588}{49896409440894219}.
 \tag{10.9}
\]
If \(L_\alpha(\lambda^j)=\mu_j(\alpha)\), its boundary value is
\[
 L_0(\lambda p(\lambda)^2)
 =-\frac{673792679642733430835456936384}
 {329714727520793070279653295504327135}<0.
 \tag{10.10}
\]
This is the sole finite numeric certificate used here. The complete
boundary dependency is Section 7.2 from (7.C1) through (7.C11): its exact
frozen-row reduction, Gaussian-moment limit, monomial recurrence, formal
reversion, six moments, and witness multiplication. The existing
`pde.exact_calculus.quadratic_axis_certificate()` regenerates that
calculation from its monomial rule, without reading retained arrays.

The function
\(L_\alpha(\lambda p^2)=\sum_{i,j=0}^2v_i v_j\mu_{i+j+1}(\alpha)\),
with \(v_2=1\), is continuous at zero. Its strictly negative value in
(10.10) implies that some \(\varepsilon\in(0,1)\) satisfies
\[
 L_\alpha(\lambda p^2)<0\qquad(0\le\alpha<\varepsilon).
 \tag{10.11}
\]
For any nonnegative measure \(\nu\) on \([0,\infty)\) representing all
these formal moments, the same expression would be
\(\int\lambda p(\lambda)^2\,\nu(d\lambda)\ge0\). It is finite because
only moments through degree five occur. This contradiction proves that
every metric \((\alpha,1)\), \(0<\alpha<\varepsilon\), fails this
Stieltjes moment representation while all three blocks train.

The interval is existential. This proof supplies neither a numerical
endpoint nor a sharp transition. It does not settle the unit metric
\((1,1)\), and a negative formal moment witness is not nonexistence of a
nonlinear population evolution.

### 10.3. Factorial growth at the canonical metric

Now fix \((\alpha,\beta)=(1,1)\) and set
\[
 c_k=\frac{d_k(1,1)}{k!}.
 \tag{10.12}
\]
These coefficients exist by (10.6), are nonnegative, and vanish for even
\(k\). We will prove, for odd \(k\ge1\) and \(m=(k+3)/2\),
\[
 c_k\ge m!\,4^{-m}6^{k+1}\binom{k+2}{2}.
 \tag{10.13}
\]
This is derived directly in the raw-square coordinates (10.1); there is no
change of activation, initialization, or metric convention.

Let \(D_{0,1,n}\) be the frozen-first-block derivation and
\(D_{u,n}=n\nabla_u f_n\cdot\nabla_u\) its omitted first-block term.
In the independent
primitive coordinates, \(f_n\) and every component of (10.3) have
nonnegative polynomial coefficients. Each block derivation preserves this
cone: differentiating a monomial multiplies by a nonnegative exponent, and
its replacement component has nonnegative coefficients. Expanding
\((D_{0,1,n}+D_{u,n})^k\) into its ordered words retains
\(D_{0,1,n}^k\) as one word, with every other word in the same cone after
application to \(f_n\). Independence and Gaussian symmetry give
nonnegative expectation to every monomial in the cone. Consequently
\[
 E[D_{1,1,n}^k f_n]\ge E[D_{0,1,n}^k f_n].
 \tag{10.14}
\]
This is an expectation comparison of polynomial histories, not a
componentwise comparison of trained trajectories.

In the frozen system put \(q_n=n^{-1}\sum_j u_j^4\). Equations (10.3)
give exactly
\[
 a_i'=z_i^2,\qquad z_i'=2q_n a_i z_i,\qquad q_n'=0.
\]
For fixed \(q\ge0\), let
\[
 \mathscr D_q=z^2\partial_a+2qaz\partial_z,\qquad
 P_k(a,z;q)=\frac1{k!}\mathscr D_q^k(az^2).
 \tag{10.15}
\]
Repeated chain rule gives
\(D_{0,1,n}^k f_n/k!=n^{-1}\sum_iP_k(a_i,z_i;q_n)\).
Conditionally on \(u\), the pairs \((a_i,z_i)\) are independent with law
\(N(0,1)\otimes N(0,q_n)\). The conditional expectation of this average is
therefore a fixed polynomial in \(q_n\), because \(P_k\) is a polynomial
in \(a,z,q\) and the Gaussian moments of \(z\) are zero or a constant
times an integer power of \(q_n\).

All fixed polynomial moments of \(q_n\) converge to those of \(3\).
Indeed \(E(q_n-3)^2=\operatorname{Var}(u_1^4)/n\to0\). For each integer
\(b\ge1\), convexity gives \(E q_n^{2b}\le E|u_1|^{8b}<\infty\).
The factorization of \(x^b-3^b\) yields
\[
 |x^b-3^b|\le b|x-3|\max(x,3)^{b-1}\quad(x\ge0).
\]
Cauchy--Schwarz with the preceding bounds proves
\(E|q_n^b-3^b|\to0\). Applying this to the finitely many powers in the
conditional polynomial proves
\[
 \lim_{n\to\infty}\frac{E[D_{0,1,n}^k f_n]}{k!}
 =E[P_k(A,Z;3)],\qquad
 A\sim N(0,1),\quad Z\sim N(0,3),\quad A\perp Z.
 \tag{10.16}
\]
Together with (10.14) and existence of (10.12), this gives
\(c_k\ge E[P_k(A,Z;3)]\).

For fixed \(q>0\), the monomial rule
\[
 \mathscr D_q(a^p z^l)
 =p a^{p-1}z^{l+2}+2ql a^{p+1}z^l
 \tag{10.17}
\]
shows that \(P_k\) has nonnegative coefficients and total degree \(k+3\)
in \(a,z\). The exponent of \(z\) remains even, and each derivative flips
the parity of the exponent of \(a\). For odd \(k\),
\[
 P_k(a,z;q)=\sum_{u+v=m}p_{uv}(q)a^{2u}z^{2v},
 \qquad p_{uv}(q)\ge0.
 \tag{10.18}
\]
The ray \(z=\sqrt{2q}\,a\) is invariant under (10.15): both equations
reduce to \(a'=2qa^2\). Starting from \(a(0)=1\), direct substitution
gives \(a(s)=(1-2qs)^{-1}\) and
\(az^2=2q(1-2qs)^{-3}\) for \(s<1/(2q)\) near zero. Repeated
chain rule, or differentiating this rational function \(k\) times at zero,
therefore gives
\[
 \sum_{u+v=m}p_{uv}(q)(2q)^v
 =P_k(1,\sqrt{2q};q)
 =(2q)^{k+1}\binom{k+2}{2}.
 \tag{10.19}
\]
This scalar solution is used only to evaluate a polynomial identity at
initialization.

For independent \(A\sim N(0,1)\), \(Z_q\sim N(0,q)\), Gaussian
integration by parts gives
\(E A^{2u}=(2u-1)!!\) and \(E Z_q^{2v}=(2v-1)!!q^v\), with
\((-1)!!=1\). Each factor \(2j-1\ge j\) gives
\((2u-1)!!\ge u!\), including \(u=0\). Since
\(\binom m u\le\sum_{j=0}^m\binom m j=2^m\),
\[
\begin{aligned}
 E[A^{2u}Z_q^{2v}]
 &\ge u!v!q^v
 \ge m!2^{-m}q^v
 \ge m!4^{-m}(2q)^v,
 \qquad u+v=m.
\end{aligned}
 \tag{10.20}
\]
The last inequality uses \(v\le m\). Multiply (10.20) by the
nonnegative \(p_{uv}(q)\), sum, and use (10.19) at \(q=3\). Equations
(10.14)--(10.16) give exactly (10.13).

The factorial lower bound implies
\[
 \limsup_{k\to\infty}c_k^{1/k}=\infty.
 \tag{10.21}
\]
No asymptotic factorial formula is needed: for \(m\ge2\), the last
\(\lfloor m/2\rfloor\) factors of \(m!\) are at least \(m/2\), so
\((m!)^{1/k}\ge(m/2)^{\lfloor m/2\rfloor/k}\to\infty\) along the
odd \(k\), since \(m=(k+3)/2\). The \(k\)-th root of
\(4^{-m}6^{k+1}\) tends to \(3>0\), and the binomial factor is at least
one. Thus the formal series \(\sum c_k s^k\) has radius zero: at every
\(s>0\) its terms fail to tend to zero along the odd subsequence.

### 10.4. The prescribed Taylor losses are not uniformly Cauchy

The physical loss is the full squared error \(\mathcal L_n=(1-f_n)^2\),
without a factor \(1/2\). At finite width its negative metric gradient is
exactly \(2(1-f_n)\) times the feature-ascent vector field. Accordingly,
whenever a finite-width feature orbit is being followed, its physical
clock obeys \(ds/dt=2(1-f_n)\). This finite identity motivates the same
clock for a prescribed formal Taylor model, but does not identify the
formal model with a width limit.

For \(M\ge1\), define the deterministic polynomial
\[
 F_M(s)=\sum_{k=0}^M c_k s^k.
 \tag{10.22}
\]
Here \(c_0=0\), and \(c_1\ge63>0\): the frozen first derivative has
expectation \(E[Z^4+12A^2Z^2]=27+36=63\), and (10.14) applies.
Thus \(F_M(0)=0\), \(F_M'(s)\ge c_1\) for \(s\ge0\), and \(F_M(s)\)
tends to infinity as \(s\to\infty\). For \(y\in(0,1]\), denote by
\(r_M(y)>0\) its unique positive solution to \(F_M(r_M(y))=y\).

The residual clock and its output are
\[
 \tau_M'=2(1-F_M(\tau_M)),\quad \tau_M(0)=0,
 \qquad f_M(t)=F_M(\tau_M(t)),\quad
 \mathcal L_M(t)=(1-f_M(t))^2.
 \tag{10.23}
\]
These define a global continuous loss. To establish this directly, put
\(r=r_M(1)\) and
\[
 T_M(s)=\int_0^s\frac{dv}{2(1-F_M(v))},\qquad 0\le s<r.
\]
It is continuously differentiable, strictly increasing, and \(T_M(0)=0\).
If \(B=\max_{[0,r]}F_M'<\infty\), then
\(1-F_M(v)\le B(r-v)\). Consequently \(T_M(s)\to\infty\) as
\(s\uparrow r\), by the divergent integral of \(1/(r-v)\). Its inverse
is a differentiable function \(\tau_M:[0,\infty)\to[0,r)\) satisfying
(10.23). Separation of variables proves uniqueness while \(\tau_M<r\);
the same divergent integral prevents reaching \(r\) in finite time. In
particular \(0\le f_M(t)<1\), \(f_M\) is increasing, and
\(\mathcal L_M(0)=1\).

Equivalently this is precisely the polynomial source model
\[
 \partial_tU_M(t,s)=2(1-U_M(t,0))\partial_sU_M(t,s),\qquad
 U_M(0,s)=F_M(s),\qquad U_M(t,s)=F_M(s+\tau_M(t)).
 \tag{10.24}
\]
Substitution proves the PDE and its trace \(U_M(t,0)=f_M(t)\). Within
polynomials of degree at most \(M\), setting \(u_j(t)=\partial_s^jU_M(t,0)\)
gives the finite system \(u_j'=2(1-u_0)u_{j+1}\) for \(j<M\),
\(u_M'=0\), and \(u_j(0)=j!c_j\). Its right side is polynomial and
Lipschitz on every bounded set, as follows from its bounded Jacobian
there. For two solutions with identical initial data on a common compact
time interval, their difference \(e(t)\) therefore satisfies
\(\|e(t)\|\le C\int_0^t\|e(v)\|\,dv\). Set
\(V(t)=\int_0^t\|e(v)\|\,dv\); then
\((e^{-Ct}V(t))'\le0\), while \(V(0)=0\) and \(V\ge0\).
Thus \(V=0\) and the solutions agree. Formula
(10.24) supplies the global solution of this finite prescribed family.

By positivity and (10.21), for every fixed \(s>0\),
\[
 F_M(s)\longrightarrow+\infty\quad(M\to\infty).
 \tag{10.25}
\]
Indeed the partial sums are nondecreasing in \(M\), and some individual
terms \(c_k s^k\) become arbitrarily large. Thus \(r_M(y)\to0\) for each
\(y\in(0,1)\): given \(s>0\), (10.25) eventually gives \(F_M(s)>y\),
which forces \(r_M(y)<s\).

The physical time at which (10.23) reaches \(y\) is
\[
 t_M(y)=T_M(r_M(y))
 \le\frac{r_M(y)}{2(1-y)}\longrightarrow0.
 \tag{10.26}
\]
The inequality uses \(F_M(v)\le y\) on that integration interval. For
each fixed \(t>0\), monotonicity then implies \(f_M(t)\ge y\) for all
sufficiently large \(M\). Letting \(y\uparrow1\), while \(f_M(t)<1\),
proves
\[
 \mathcal L_M(0)=1,\qquad
 \lim_{M\to\infty}\mathcal L_M(t)=0\quad(t>0).
 \tag{10.27}
\]

For every \(T>0\), these continuous losses are not uniformly Cauchy on
\([0,T]\). Otherwise pointwise completeness of the real numbers and the
uniform Cauchy property would give a uniform limit there. A uniform limit
of continuous functions is continuous: approximate it within one third
of a requested tolerance by one fixed member, and use continuity of that
member. But (10.27) fixes its putative limit to be discontinuous at zero.

This also rules out the following precise common-target shadowing claim,
without assuming existence of a limiting network curve. For arbitrary
random comparison curves \(H_n\) for which the expectations below are
defined, let
\[
 d_T(g,h)=\min\{1,\sup_{0\le t\le T}|g(t)-h(t)|\}.
\]
If \(\lim_{M\to\infty}\limsup_{n\to\infty}E d_T(\mathcal L_M,H_n)=0\),
then the metric triangle inequality would imply
\[
 d_T(\mathcal L_M,\mathcal L_{M'})
 \le\limsup_n E d_T(\mathcal L_M,H_n)
    +\limsup_n E d_T(H_n,\mathcal L_{M'})\longrightarrow0
\]
as \(M,M'\to\infty\). This would make the family uniformly Cauchy,
a contradiction. In particular the prescribed iterated shadowing claim
cannot hold with finite-width network losses as \(H_n\).

The order of limits throughout is fixed derivative order, then width,
then Taylor truncation order. The result concerns this positive polynomial
family and uniform error on intervals containing zero. It does not analyze
a coupled order \(M=M(n)\), establish an actual network step loss, or
exclude other finite descriptions using signed or non-Taylor constructions.

## 11. A sharp uniform shallow feature-step estimate

At one hidden layer the feature-ascent coordinates remain independent.
This permits a bound uniform in the update count that is stronger than
the fixed-program estimate of Section 8. The result concerns exact Euler
steps for feature ascent, with order-one stored readout. It does not
replace the residual by a constant in physical loss GD.

### 11.1. Model and quantitative statement

Take \(L=m=d=1,x_1=1\), and write the stored parameters as
\(a_i=W_i^{(2)},u_i=W_i^{(1)}\). All initial \(a_i,u_i\) are independent
standard Gaussians. Both block mobilities for feature ascent are \(n\).
For a real feature step \(h\), the simultaneous raw updates and output are

\[
 a_i^{j+1}=a_i^j+h\phi(u_i^j),\qquad
 u_i^{j+1}=u_i^j+ha_i^j\phi'(u_i^j),\qquad
 f_{n,1}^j=\frac1n\sum_{i=1}^na_i^j\phi(u_i^j).
 \tag{SD1}
\]

The index \(j\) counts steps. The scalar \(h\) is neither physical time
\(t\), the physical loss-GD step \(\eta_n\), nor a hidden feature vector.
There is no loss or residual multiplier in (SD1). Assume

\[
 \phi\in C^{12}(\mathbb R),\quad E\phi(G)^2=1,\quad
 M=\max\left\{1,\sup_z\frac{|\phi(z)|}{1+|z|},
                \max_{1\le q\le12}\|\phi^{(q)}\|_\infty\right\}<\infty,
 \qquad G\sim N(0,1).
 \tag{SD2}
\]

On the single mark space \(\Omega_1=(\mathbb R^2,\gamma_2)\), let
\(a_0,u_0\) be its independent standard Gaussian coordinates. Define
population coordinates \(A_j=W_j^{(2)},U_j=Z_j^{(1)}\) by the same
two-dimensional recursion, starting from \(A_0=a_0,U_0=u_0\), and set

\[
 F_{N,1}(h)=E_1[A_N\phi(U_N)],\qquad
 J_\phi=E\left[3\phi'(G)^3\phi'''(G)
       +11\phi(G)\phi'(G)^2\phi''(G)
       +4\phi'(G)^4+4\phi(G)^2\phi'(G)^2
       +12\phi'(G)^2\phi''(G)^2\right].
 \tag{SD3}
\]

The one-dimensional expectation in \(J_\phi\) uses the displayed \(G\);
\(E_1\) contracts the mark population. Set \(c_\phi=(16M)^{-1}\).
Section 11.2 defines a finite, explicit constant \(B_\phi^{\rm sh}\)
using only \(M\) and two Gaussian integrals.

**Theorem SD.** For every integer \(k\ge1\) and every
\(|h|\le c_\phi/k\),

\[
 \left|F_{k,1}(2h)-F_{2k,1}(h)
        +\frac{k(2k-1)}2J_\phi h^3\right|
 \le B_\phi^{\rm sh}k^4|h|^5.
 \tag{SD4}
\]

For each fixed finite \(N,h\), \(E f_{n,1}^N(h)=F_{N,1}(h)\) at
every width \(n\); thus these are also the width-first expected outputs.
The constant and the radius do not use a trained trajectory, an output
derivative, or a continuity modulus. The power \(k^4\) is sharp within
the activation class (SD2).

The proof first factors each coarse/fine Euler defect by \(h^2\).
Three step derivatives of each transported defect cost at most \(k^3\),
and there are \(k\) defects. A Gaussian-integrable envelope justifies
averaging those derivatives. Readout-sign symmetry then removes the
even terms, and a direct Gaussian calculation identifies the cubic term.

### 11.2. The explicit activation-only constant

All quantities in this subsection are nonnegative scalar envelopes, not
network coordinates or kernels. For a real \(R\ge1\), set

\[
 c=c_\phi,\qquad \Lambda=12MR,\qquad
 P=\exp(4c\Lambda)=e^{3R}.
 \tag{SD5}
\]

In the following order define

\[
 \begin{aligned}
 X_1&=4P\Lambda,\\
 X_2&=P(8\Lambda X_1+4c\Lambda X_1^2),\\
 X_3&=P\{12\Lambda(X_1^2+X_2)
                  +4c\Lambda(X_1^3+3X_1X_2)\},
 \end{aligned}
 \tag{SD6}
\]

\[
 \begin{aligned}
 \mathcal G_0&=\Lambda,&\mathcal G_1&=\Lambda X_1,\\
 \mathcal G_2&=\Lambda(X_2+X_1^2),&
 \mathcal G_3&=\Lambda(X_3+3X_1X_2+X_1^3),\\
 \mathcal B_q&=\sum_{v=0}^q\binom qv\mathcal G_v\mathcal G_{q-v}
       &&(0\le q\le3).
 \end{aligned}
 \tag{SD7}
\]

With \(\mathcal B_{-1}=\mathcal B_{-2}=0\), put

\[
 \mathcal Z_q=X_q+c^2\mathcal B_q+2qc\mathcal B_{q-1}
                         +q(q-1)\mathcal B_{q-2}\quad(1\le q\le3),
 \tag{SD8}
\]

\[
 \begin{aligned}
 T_1&=P(\mathcal Z_1+2\Lambda),\\
 T_2&=P(\mathcal Z_2+4\Lambda T_1+2c\Lambda T_1^2),\\
 T_3&=P\{\mathcal Z_3+6\Lambda(T_1^2+T_2)
                         +2c\Lambda(T_1^3+3T_1T_2)\}.
 \end{aligned}
 \tag{SD9}
\]

Next define

\[
 \begin{aligned}
 \mathcal H_0&=\Lambda,&\mathcal H_1&=\Lambda T_1,\\
 \mathcal H_2&=\Lambda(T_2+T_1^2),&
 \mathcal H_3&=\Lambda(T_3+3T_1T_2+T_1^3).
 \end{aligned}
 \tag{SD10}
\]

Finally, starting at \(V_0=P\mathcal B_0\), define successively for
\(q=1,2,3\)

\[
 V_q=P\left\{\mathcal B_q
      +2c\sum_{v=1}^q\binom qv\mathcal H_vV_{q-v}
      +2q\sum_{v=0}^{q-1}\binom{q-1}v\mathcal H_vV_{q-1-v}\right\},
 \qquad
 \mathcal C_M(R)=\frac16\sum_{v=0}^3\binom3v\mathcal H_vV_{3-v}.
 \tag{SD11}
\]

The claimed constant is

\[
 B_\phi^{\rm sh}=E_1\mathcal C_M(1+|a_0|+|u_0|).
 \tag{SD12}
\]

Every sum has at most four terms, and all right sides use previously
defined quantities. Finiteness of this fully specified integral is
proved below; no numerical quadrature or stored array is a premise.

### 11.3. Exact width identification and transported defect

For \(z=(a,u)\in\mathbb R^2\), define

\[
 \psi(z)=a\phi(u),\quad
 g(z)=(\phi(u),a\phi'(u))=\nabla\psi(z),\quad
 E_hz=z+hg(z),\quad R(z)=1+|a|+|u|.
 \tag{SD13}
\]

All derivative operator norms below are induced by ordinary Euclidean
norms. \(R(z)\) is a scalar growth envelope. Direct substitution gives

\[
 R(E_{\alpha h}z)\le(1+\alpha M|h|)R(z),\qquad 0\le\alpha\le2.
 \tag{SD14}
\]

For fixed \(N,h\), this bounds the terminal summand in (SD1) by
\(M(1+M|h|)^{2N}(1+|a_0|+|u_0|)^2\), which is integrable.
Each neuron is a function only of its own independent initial pair, so
the neurons remain iid and expectation of their average is exactly
\(F_{N,1}(h)\). This proves width identification before any step
derivative is taken.

Write \(C_h=E_{2h},B_h=E_h\circ E_h\). The fundamental theorem of
calculus gives

\[
 B_hz=C_hz+h^2b_h(z),\qquad
 b_h(z)=\int_0^1Dg(z+\tau hg(z))[g(z)]\,d\tau.
 \tag{SD15}
\]

For \(q=0,\ldots,k-1\), put \(x_q=C_h^{k-1-q}z\) and
\(v_q=\psi\circ B_h^q\). Consecutive hybrids
\(\psi(B_h^q(C_h^{k-q}z))\) differ by
\(v_q(C_hx_q)-v_q(B_hx_q)\). Summation and a segment integral give
the exact, signed identity

\[
 \psi(C_h^kz)-\psi(B_h^kz)=h^2Q_k(h,z),
 \qquad
 Q_k(h,z)=-\sum_{q=0}^{k-1}\int_0^1
 Dv_q(C_hx_q+\tau h^2b_h(x_q))[b_h(x_q)]\,d\tau.
 \tag{SD16}
\]

This uses no commutation of the two Euler maps.

### 11.4. Uniform derivative envelopes

Fix an initial \(z_0\), put \(R=R(z_0)\), and assume \(|h|k\le c\).
Every pre-defect Euler path in (SD16), including
\(x+\tau hg(x)\) in (SD15), has total Euler coefficient at most \(4k\).
The interpolation point is

\[
 C_hx+\tau h^2b_h(x)=(1-\tau)C_hx+\tau B_hx.
 \tag{SD17}
\]

Both endpoints obey (SD14). Convexity of \(R(z)\) bounds their
interpolation by \(e^{4M|h|k}R\). Starting at that point, at most
\(2k\) further fine steps remain. Thus every relevant point obeys

\[
 R(z)\le e^{6M|h|k}R\le e^{3/8}R<2R.
 \tag{SD18}
\]

The interpolation has not been treated as an Euler step. The larger
coefficient allowance \(4k+2k\) avoids any need to identify its path
with a single unbroken Euler trajectory.

For \(0\le q\le4\) and \(1\le j\le4\), respectively,

\[
 \|D^qg(z)\|\le6MR(z),\qquad
 \|D^j\psi(z)\|\le5MR(z).
 \tag{SD19}
\]

For \(q\ge1\), the second coordinate of \(D^qg\) consists of
\(a\phi^{(q+1)}(u)\) times all \(u\)-directions and \(q\) terms
with one \(a\)-direction and \(\phi^{(q)}(u)\). Unit Euclidean
directions have coordinate magnitudes at most one; summing these terms
and the first coordinate gives the first bound. The same count, with
one fewer activation derivative, gives the second; its first derivative
uses the linear-growth bound on \(\phi\). The case \(q=0\) follows
directly from (SD13). By (SD18), all these derivative bounds are at
most \(\Lambda=12MR\).

Consider a pre-defect path \(y_{j+1}=y_j+\alpha_jhg(y_j)\) starting
at \(z_0\), where \(0\le\alpha_j\le2\) and
\(\sum_j\alpha_j\le4k\). Its homogeneous tangent products have norm
at most

\[
 \prod_j(1+\alpha_j|h|\Lambda)
 \le e^{\Lambda|h|\sum_j\alpha_j}\le P.
 \tag{SD20}
\]

A prime denotes \(d/dh\). Differentiating one step gives

\[
 \begin{aligned}
 y_{j+1}'&=(I+\alpha_jhDg)y_j'+\alpha_jg,\\
 y_{j+1}''&=(I+\alpha_jhDg)y_j''+2\alpha_jDg[y_j']
                             +\alpha_jhD^2g[y_j',y_j'],\\
 y_{j+1}'''&=(I+\alpha_jhDg)y_j'''
       +3\alpha_j\{D^2g[y_j',y_j']+Dg[y_j'']\}\\
       &\quad+\alpha_jh\{D^3g[y_j',y_j',y_j']
                                  +3D^2g[y_j',y_j'']\}.
 \end{aligned}
 \tag{SD21}
\]

Iterating in \(j\) and summing the inhomogeneous terms gives

\[
 \|y_j^{(q)}\|_2\le X_qk^q,\qquad q=1,2,3.
 \tag{SD22}
\]

In detail, the first recurrence gives \(4P\Lambda k=X_1k\).
After division by \(k^2\), the second's source sum is bounded by
\(8\Lambda X_1+4c\Lambda X_1^2\), then multiplied by \(P\).
After division by \(k^3\), the third's source sum is bounded by
\(12\Lambda(X_1^2+X_2)+4c\Lambda(X_1^3+3X_1X_2)\),
then multiplied by \(P\). These are exactly (SD6). The initial
derivatives vanish because \(z_0\) is independent of \(h\).

The curve \(x_q+\tau hg(x_q)\) in (SD15) is the path to \(x_q\)
with one coefficient \(\tau\le1\) appended; its total is still below
\(4k\). The chain rule, (SD19), and (SD22) bound the derivatives
of \(g(x_q)\) and \(Dg(x_q+\tau hg(x_q))\) through order three by
\(\mathcal G_jk^j\). For example the third derivative of a composition
is the sum of the terms with \(y'''\), \(3y'y''\), and \((y')^3\),
which explains \(\mathcal G_3\). Leibniz's rule inside (SD15) yields

\[
 \|\partial_h^jb_h(x_q)\|_2\le\mathcal B_jk^j,
 \qquad 0\le j\le3.
 \tag{SD23}
\]

Since

\[
 \partial_h^j(h^2b_h)
 =h^2\partial_h^jb_h+2jh\partial_h^{j-1}b_h
                         +j(j-1)\partial_h^{j-2}b_h,
 \tag{SD24}
\]

Terms with negative derivative order are omitted. For \(j=1,2,3\),
the derivatives of the point (SD17) are bounded by
\(\mathcal Z_jk^j\). Here \(C_hx_q\) itself is a pre-defect path
covered by (SD22); use \(k\ge1,|h|k\le c\) in (SD24).
Starting from this interpolation point and repeating (SD21) for the
remaining at most \(2k\) fine steps proves bounds \(T_jk^j\).
The corresponding normalized source sums now have coefficients
\(2,4,6\) and \(2c\), and their initial contributions are
\(\mathcal Z_j\). This gives exactly (SD9), with the same upper
bound \(P\) for homogeneous amplification. Derivatives through order
three of \(Dg\) and \(D\psi\) along this last path are consequently
bounded by \(\mathcal H_jk^j\), as in (SD10).

It remains to transport the initial direction \(b_h(x_q)\) through
these fine steps. If that direction is denoted by \(\omega\), then

\[
 \omega^+=\omega+hDg(z)\omega,
 \quad
 (\omega^+)^{(j)}=\omega^{(j)}
  +h\sum_{v=0}^j\binom jv(Dg(z))^{(v)}\omega^{(j-v)}
  +j\sum_{v=0}^{j-1}\binom{j-1}v(Dg(z))^{(v)}\omega^{(j-1-v)}.
 \tag{SD25}
\]

The \(v=0\) term in the first sum is the homogeneous tangent factor.
The other terms are summed over at most \(2k\) fine steps. Starting
from (SD23), induction on \(j=0,1,2,3\) proves
\(\|\omega^{(j)}\|_2\le V_jk^j\): after dividing by \(k^j\),
the two source sums are bounded by the \(2c\) and \(2j\) sums in
(SD11), respectively, followed by amplification \(P\).

The transported integrand in (SD16) is now \(D\psi(z)[\omega]\).
For every \(0\le j\le3\), its \(j\)-th derivative has magnitude at
most

\[
 k^j\sum_{v=0}^j\binom jv\mathcal H_vV_{j-v}.
 \tag{SD26}
\]

Integration in \(\tau\) has mass one and there are \(k\) summands.
In particular,

\[
 \sup_{|h|\le c/k}|\partial_h^3Q_k(h,z_0)|
 \le6\mathcal C_M(R)k^4.
 \tag{SD27}
\]

All envelopes (SD6)--(SD11) are finite polynomials with nonnegative
coefficients in \(c,\Lambda,P\). Since \(c\le1,\Lambda=12MR\),
\(P=e^{3R}\), each is bounded by a polynomial in \(R\) times
\(e^{C R}\), with finite constants depending only on the displayed
finite recursion and \(M\). Such functions are integrable at
\(R=1+|a_0|+|u_0|\): for any finite \(p,\lambda\ge0\),

\[
 E[(1+|G|)^pe^{\lambda|G|}]<\infty,
 \tag{SD28}
\]

because \(\lambda|x|-x^2/2\le -x^2/4\) outside a finite interval.
Apply this one-dimensional integral estimate to both independent marks.
It proves finiteness of (SD12) and, using (SD26) for all four derivative
orders, an integrable envelope for \(Q_k\) and its first three
derivatives at each fixed \(k\). Integrating the fundamental theorem of
calculus and applying dominated convergence successively therefore
justifies all three differentiations under \(E_1\).

### 11.5. Parity, cubic coefficient, and sharpness

Set \(\overline Q_k(h)=E_1Q_k(h,(a_0,u_0))\). The preceding proof gives

\[
 D_k(h):=F_{k,1}(2h)-F_{2k,1}(h)=h^2\overline Q_k(h),
 \qquad
 \sup_{|h|\le c/k}|\overline Q_k'''(h)|
 \le6B_\phi^{\rm sh}k^4.
 \tag{SD29}
\]

Replacing \((h,a_0,u_0)\) by \((-h,-a_0,u_0)\) preserves the law,
negates each \(A_j\), and leaves each \(U_j\) unchanged. Thus each
\(F_{N,1}\), and hence \(D_k\), is odd. The factorization shows that
\(\overline Q_k\) is odd away from zero; continuity extends this to
zero, so \(\overline Q_k(0)=\overline Q_k''(0)=0\). Repeated
integration of its third derivative gives

\[
 \overline Q_k(h)-h\overline Q_k'(0)
   =\frac12\int_0^h(h-v)^2\overline Q_k'''(v)\,dv.
 \tag{SD30}
\]

The same estimate applies to negative \(h\) by reversing orientation.
Multiplication by \(h^2\) proves a remainder at most
\(B_\phi^{\rm sh}k^4|h|^5\).

To identify its coefficient without any Gaussian compiler input, evaluate
all derivatives at the initial \(z\) and write
\(b=Dg[g],c_1=Dg[b],c_2=D^2g[g,g]\). Direct differentiation of
\(z_{j+1}=z_j+hg(z_j)\) at \(h=0\) and summation give

\[
 z_N'(0)=Ng,\quad z_N''(0)=N(N-1)b,\quad
 z_N'''(0)=6\binom N3c_1+\frac{N(N-1)(2N-1)}2c_2.
 \tag{SD31}
\]

Indeed the third-derivative increment is
\(3j(j-1)c_1+3j^2c_2\); the finite sums of \(j(j-1)\) and \(j^2\)
are \(2\binom N3\) and \(N(N-1)(2N-1)/6\). Since \(g=\nabla\psi\),
symmetry of the Hessian gives

\[
 D\psi[c_1]=D^2\psi[g,b]=\|b\|_2^2,\qquad
 D\psi[c_2]=D^3\psi[g,g,g].
 \tag{SD32}
\]

Define \(\mathsf S=E_1D^3\psi[g,g,g]\) and
\(\mathsf H=E_1\|Dg[g]\|_2^2\). The third derivative of the
observable in (SD31) has the three terms
\(D\psi[z_N''']+3D^2\psi[z_N',z_N'']+
D^3\psi[z_N',z_N',z_N']\), and consequently

\[
 F_{N,1}^{(3)}(0)=\frac{N(4N^2-3N+1)}2\mathsf S
                  +2N(N-1)(2N-1)\mathsf H.
 \tag{SD33}
\]

These derivatives may be averaged: for fixed \(N\), (SD18)--(SD22)
apply in a neighborhood of zero, and the chain rule for \(\psi\)
gives the same polynomial-times-linear-exponential Gaussian envelope.

At \(z=(a_0,u_0)\), put \(p=\phi'(u_0),q=\phi''(u_0)\). Then

\[
 g=(\phi(u_0),a_0p),\qquad
 Dg[g]=(a_0p^2,\phi(u_0)p+a_0^2pq),
 \tag{SD34}
\]

and
\(D^3\psi[g,g,g]=3a_0^2\phi(u_0)p^2q+
a_0^4p^3\phi'''(u_0)\).
Independence and \(E a_0^2=1,E a_0^4=3\) give

\[
 \begin{aligned}
 \mathsf S&=3E[\phi\phi'^2\phi''+\phi'^3\phi'''],\\
 \mathsf H&=E[\phi'^4+\phi^2\phi'^2
                          +2\phi\phi'^2\phi''+3\phi'^2\phi''^2],
 \end{aligned}
 \tag{SD35}
\]

where all activation factors are evaluated at \(G\sim N(0,1)\).
Thus \(\mathsf S+4\mathsf H=J_\phi\). Substitution of \(N=k,2k\)
in (SD33) yields

\[
 \overline Q_k'(0)
 =\frac{8F_{k,1}^{(3)}(0)-F_{2k,1}^{(3)}(0)}6
 =-\frac{k(2k-1)}2J_\phi.
 \tag{SD36}
\]

Together with (SD29)--(SD30), this proves (SD4).

For the constant branch \(\phi\equiv\pm1\), one has
\(F_{N,1}(h)=Nh,J_\phi=0\), and the discrepancy vanishes exactly.
For \(\phi(z)=z\), diagonalize one step using
\((a+u)/\sqrt2,(a-u)/\sqrt2\), whose multipliers are \(1+h,1-h\).
Both initial coordinates have variance one, so

\[
 F_{N,1}(h)=\frac{(1+h)^{2N}-(1-h)^{2N}}2,\qquad J_\phi=8.
 \tag{SD37}
\]

Its discrepancy has cubic coefficient \(-4k(2k-1)\) and fifth
coefficient

\[
 32\binom{2k}5-\binom{4k}5
 =-\frac43k(k-1)(2k-1)(8k-9).
 \tag{SD38}
\]

If (SD4) held with \(Ck^p|h|^5\) for some fixed \(p<4\) and
positive radius proportional to \(1/k\), divide by \(|h|^5\) and
take \(h\to0\) at each fixed \(k\). Equation (SD38) would be bounded
in magnitude by \(Ck^p\), which is impossible as \(k\to\infty\).
This proves sharpness. \(\square\)

### 11.6. A restricted dyadic terminal-output consequence

For a real accumulated feature time \(s\), set
\(G_N(s)=F_{N,1}(s/N)\). Fix \(0<S\le2c_\phi\). Substituting
\(h=s/(2k)\) in (SD4) gives

\[
 \sup_{|s|\le S}|G_{2k}(s)-G_k(s)|
 \le\frac{|J_\phi|S^3}{8k}
                   +\frac{B_\phi^{\rm sh}S^5}{32k}.
 \tag{SD39}
\]

For \(k=2^j\), the right side is summable in \(j\). Telescoping,
completeness of \(\mathbb R\), and
\(\sum_{j=p}^\infty2^{-j}=2^{1-p}\) give a uniform limit
\(G_\infty\) on \([-S,S]\), with

\[
 \sup_{|s|\le S}|G_\infty(s)-G_{2^p}(s)|
 \le2^{-p}\left(\frac{|J_\phi|S^3}{4}
                         +\frac{B_\phi^{\rm sh}S^5}{16}\right).
 \tag{SD40}
\]

Each fixed \(G_N\) is continuous by its finite smooth recursion and
the Gaussian envelope (SD14); uniform convergence preserves continuity.
The consequence is only about the terminal expected output on this
explicit short feature-time interval. It supplies no restart state,
partition independence, hidden-state convergence, or growing-program
width theorem. Physical loss GD includes a moving residual in every
raw step, so it is a different discretization. Neither (SD4) nor
(SD40) establishes its continuous-time limit or any corresponding result
with reused inter-hidden-layer matrices.

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

## Finite contraction, observable and physical-loss calculus

The following finite algebra separates parameter-contraction trees, Gaussian
neuron forests, moving loss jets and held-fixed preactivation curvature.

## A. Weighted derivative trees in a constant metric

Let \(f:U\to\mathbb R\), where \(U\subset\mathbb R^d\) is open, let
\(M\) be a constant symmetric positive semidefinite \(d\times d\) matrix,
and put \(D=(M\nabla f)\cdot\nabla\). For an unrooted finite tree \(T\),
define \(C_T(f,M)\) by placing \(\nabla^{\deg(v)}f\) at vertex \(v\),
placing \(M\) on each edge, and summing the two incident tensor indices
against that matrix. A one-vertex tree means \(f\), including its rank-zero
tensor. Explicitly, give each incident vertex-edge pair an index in
\(\{1,\ldots,d\}\), multiply the indicated tensor entries and edge entries,
and sum every index. Tensor symmetry makes this independent of the ordering
of edges at a vertex. This is a scalar contraction in parameter space;
vertices do not denote neurons or Gaussian sources.

For \(k\ge0\) and \(f\in C^{k+1}(U)\),
\[
 D^kf=\sum_{|T|=k+1}w_k(T)C_T(f,M).                         \tag{A1}
\]
The integer weights have a finite constructive definition. Start with the
one-vertex tree of weight one. From every weighted tree attach one new leaf
at each of its vertices, carrying its old weight to each resulting tree;
then add weights of isomorphic unrooted trees. Every vertex is counted,
including vertices in the same symmetry orbit.

To prove (A1), differentiate one contraction. The matrix factors are
constant. Hitting the tensor at vertex \(v\) raises its derivative order by
one; contraction of the new index with \(M\nabla f\) attaches exactly one
leaf at \(v\). The product rule sums precisely over all vertices. Induction
proves both the identity and the weight recursion. Every tree occurs,
because repeatedly removing a leaf reduces it to the singleton. The sum of
the weights at order \(k\) is \(k!\): an order-\(k\) tree has \(k+1\)
possible next attachments. For example, at order three the four-vertex
star and path have weights two and four; at order five the six weights,
as a multiset, are \(2,14,16,22,30,36\).

Canonicalization can use the lexicographically least rooted parenthesis
code over every root, sorting child codes recursively. Equal rooted codes
give an isomorphism by matching child subtrees inductively; taking minima
proves the unrooted assertion. Thus this recursion computes coefficients,
not just abstract shape counts. It terminates at every prescribed finite
order. No estimate on its high-order cost, width limit or Taylor radius is
part of (A1). For a state-dependent metric an additional derivative of every
metric factor would be necessary, so (A1) is not that formula.

## B. Normalized Gaussian forests: exact evaluation and concentration

For each \(n\ge1\), take mutually independent standard real Gaussians
\(a_i,u_j,g_{ij}\), \(1\le i,j\le n\). Row and column indices belong to
different populations, even when they have the same numerical label. A
decorated simple bipartite forest \(H\) has row decorations \(p_v\in\mathbb Z_{\ge0}\),
column decorations \(q_w\in\mathbb Z_{\ge0}\), \(e\) edges and \(r\) components, including
isolated vertices. Define
\[
 S_{H,n}=n^{-e/2-r}\sum_{i:R\to[n],\ j:C\to[n]}
   \prod_{v\in R}a_{i(v)}^{p_v}
   \prod_{w\in C}u_{j(w)}^{q_w}
   \prod_{(v,w)\in E}g_{i(v),j(w)}.                         \tag{B1}
\]
The label maps are unrestricted. The empty forest has value one. All
forests, exponents and finite lists in this section are fixed before
\(n\to\infty\).

Write \(m(b)=0\) for odd \(b\), \(m(0)=1\), and
\(m(2b)=(2b-1)!!\). These are Gaussian moments: integration by parts against
\(e^{-x^2/2}\) gives \(m(b)= (b-1)m(b-2)\), with zero boundary term and
odd moments zero by reflection.

An exact finite-width evaluator needs only equality partitions. Enumerate
all set partitions \(\pi_R,\pi_C\) of the row and column vertices. For a
row block \(A\), let \(p_A=\sum_{v\in A}p_v\); define \(q_B\) similarly.
Let \(e_{AB}\) count raw edges between blocks \(A,B\). With
\((n)_b=n(n-1)\cdots(n-b+1)\), and \((n)_0=1\),
\[
 \mathbb E S_{H,n}=n^{-e/2-r}
 \sum_{\pi_R,\pi_C}(n)_{|\pi_R|}(n)_{|\pi_C|}
 \prod_A m(p_A)\prod_Bm(q_B)\prod_{A,B}m(e_{AB}).            \tag{B2}
\]
Indeed, each labeling has a unique equality partition. Assigning distinct
labels to its blocks has the displayed falling-factorial count. All
remaining factors are independent Gaussians of the indicated powers.
This proves (B2), including \(n\) smaller than the number of blocks.

There is a more economical leading evaluator. If \(e\) is odd, the edge
expectation is zero. Otherwise put \(e=2b\) and pair the labeled edge
occurrences by Gaussian integration by parts. Each pair identifies both
row endpoints and both column endpoints. Replace each pair by a covariance
edge. The quotient multigraph has \(b\) edges, say \(v\) vertices and \(c\)
components. Identifications cannot increase component count, and each
connected graph on \(v_0\) vertices needs at least \(v_0-1\) edges. Hence
\[
 v\le b+c\le b+r.                                        \tag{B3}
\]
For that pairing, labelings with no further equalities number
\(n^v+O(n^{v-1})\); extra equalities number \(O(n^{v-1})\). Their decoration
moments are bounded constants, since all degrees are fixed. After
normalization the contribution is \(O(n^{v-b-r})\), so it never diverges.
Its limit survives only when \(v=b+r\). Equality in (B3) then forces
\(c=r\): no leading pairing joins original components, and every quotient
component is a tree. Consequently
\[
 \chi(H):=\lim_n\mathbb ES_{H,n}
       =\prod_{C\text{ component of }H}\chi(C).             \tag{B4}
\]
A component with an odd number of edges has value zero. Isolates contribute
their scalar Gaussian moment.

For a connected component with \(2b\) edges, one can instead enumerate
exactly the bipartition-respecting vertex partitions with \(b+1\) total
blocks and every occupied cell containing two raw edges. Each such
partition determines one edge pairing, namely pairing the two occurrences
in each cell. Conversely a leading paired quotient is a tree: a parallel
covariance edge would create a cycle, so its occupied cells have precisely
two raw edges. Its vertex identifications are the stated partition. For
completeness, the identifications forced by its cell pairs cannot define
a finer partition: that would have more than \(b+1\) vertices in a connected
graph with \(b\) covariance edges, contradicting (B3). Multiply the Gaussian
moments of the summed decorations and sum these partitions. This proves
the alternative evaluator, without a rank test over a finite field.

The same identities also supply concentration of these scalar sums. The
exact product identity is
\[
 S_{H,n}S_{J,n}=S_{H\sqcup J,n}.                          \tag{B5}
\]
Use distinct abstract vertices in the union; numerical labels may still
coincide. Normalization exponents add. Repeated use of (B4) therefore gives
\(\mathbb ES_{H,n}^{k}\to\chi(H)^k\) for every integer \(k\ge0\).
Expanding the nonnegative even power gives
\[
 \mathbb E|S_{H,n}-\chi(H)|^{2k}
 =\sum_{j=0}^{2k}{2k\choose j}(-\chi(H))^{2k-j}
                       \mathbb ES_{H,n}^{j}\longrightarrow0.       \tag{B6}
\]
For any finite real \(p\ge1\), choose \(2k\ge p\) and use
\(\mathbb E|X|^p\le(\mathbb E|X|^{2k})^{p/(2k)}\).
Thus every finite linear combination of forest sums converges in every
finite \(L^p\) to the same linear combination of \(\chi(H)\). Products
converge too, by (B5) or Hölder. This proves uniform integrability at each
fixed finite degree, as well as convergence in probability. It makes no
assertion about coordinatewise vector limits or orders growing with width.

## C. Weighted quadratic generator, connected recursion and hidden roots

Take \(d=m=1\), \(x=y=1\), two hidden layers, activations \(z\mapsto z^2\),
stored weights \(u_j,g_{ij}/\sqrt n,a_i\), and the independent Gaussian
initialization in B. Thus the stored readout is order one. Define
\[
 z_i=n^{-1/2}\sum_jg_{ij}u_j^2,\qquad
 f_n=n^{-1}\sum_i a_i z_i^2.
\]
Use feature ascent with block mobilities \(n\alpha,\beta,n\), where
\(\alpha,\beta\ge0\). In the auxiliary coordinates \((u,g,a)\),
\(D=n(\alpha\nabla_u f_n\cdot\nabla_u+
\beta\nabla_g f_n\cdot\nabla_g+\nabla_a f_n\cdot\nabla_a)\).
The primitive identities are
\[
 Da_i=n^{-1}\sum_{j,l}g_{ij}g_{il}u_j^2u_l^2,\quad
 Du_j=4\alpha n^{-1}\sum_{i,l}a_i g_{ij}g_{il}u_ju_l^2,\quad
 Dg_{ij}=2\beta n^{-1}\sum_l a_i g_{il}u_j^2u_l^2.           \tag{C1}
\]

For the forest subalgebra with column decorations \(2q_w\), these give:

* A row hit lowers \(p_v\) by one and attaches two new column leaves,
  each of decoration two; its multiplier is \(p_v\).
* A column hit retains its decoration, adds a new row of decoration one
  joined to that column, and adds a new column leaf of decoration two to
  the new row; its multiplier is \(8\alpha q_w\).
* An edge hit removes the edge, raises its row decoration by one and its
  column decoration by two, and attaches a new column leaf of decoration
  two to that row; its multiplier is \(2\beta\).

New vertices always have new abstract labels. In the first two cases the
edge number increases by two and the component count is unchanged. In the
last case a bridge is deleted and one leaf is attached, so the edge number
is unchanged and the component count increases by one. In every case
\(e/2+r\) increases by one, accounting for the \(1/n\) in (C1).
The product rule proves the rewrites even for labelings where several
abstract vertices have the same numerical index.

Let \(A_k(C;\alpha,\beta)=\chi(D^k S_C)\), with \(C\) connected and
normalized as in (B1). Here \(D^k S_C\) denotes the finite rewrite
combination. Set \(A_0(C)=\chi(C)\). For \(k\ge1\), each row/column hit
gives its stated multiplier times \(A_{k-1}\) of the child tree. Each
edge hit splits the child into \(C_1,C_2\) and contributes
\[
 2\beta\sum_{j=0}^{k-1}{k-1\choose j}
        A_j(C_1;\alpha,\beta)A_{k-1-j}(C_2;\alpha,\beta). \tag{C2}
\]
This is an equality: the remaining derivations distribute by the Leibniz
rule, and their leading expectations factor by (B4). Each call has smaller
remaining derivative order, so the recursion terminates and canonical tree
keys safely memoize it. Polynomial arithmetic in \(\alpha,\beta\) retains
every block grade. Equivalently the coefficient with \(u\)-hit count \(a\)
and edge-hit count \(b\) uses coefficient convolution in both grades in
(C2), with one edge hit already consumed. No commutation of the block
derivations is assumed.

For the output root, initially there is one row of decoration one and two
column leaves of decoration two. After \(k\) derivatives, if the counts of
row, column and edge hits are \(x,y,w\), then
\[
 x+y+w=k,\quad e=2+2(x+y),\quad r=1+w,\quad
 P=e/2=k+1-w,\quad A=1-x+y+w=k+1-2x,\quad
 H=2+2x+y+2w=2k+3+x-P.                                  \tag{C3}
\]
Here \(A\) is total row decoration and \(H\) is half the total column
decoration. These equations follow by adding the changes of each rewrite.
At the unit metric the sum of next-hit multipliers is
\(L=A+8H+2e\). A row, column or edge hit increases \(L\) respectively by
\(19,13,17\), so the exact sum for two ordered further hits is
\[
 A(L+19)+8H(L+13)+2e(L+17)=L^2+19A+104H+34e.              \tag{C4}
\]
This counts rewrite coefficients only; contraction values are not bounded
by this count times the parent's value. For example, an isolated row with
decoration one has expectation zero but its row derivative has leading
expectation three. A zero base expectation is therefore not a valid
derivative-recursion prune.

Safe pruning of a partially paired connected base can use: too few or too
many possible final index classes; a current cell with more than two raw
edges, since further identifications only merge cells; or an odd decoration
in a class which no unpaired edge can ever merge. Each follows directly
from the leading-tree condition. They are conditions on a particular base
contraction, not grounds to delete a derivative prefix. The unrestricted
binary-rank shortcut is false. For rows decorated \((2,1,1)\), columns
decorated \((2,2,2,2)\), and edges
\[
 (0,0),(0,1),(0,2),(0,3),(1,0),(2,0),
\]
the leading equality-partition value is \(27\). In particular the row
partition \(\{0\},\{1,2\}\) and column partition
\(\{0,1\},\{2,3\}\) is a legitimate contribution of \(9\), although
the two row-block parity signatures have rank one. Formula (B2) or the
zero-or-two-cell rule counts it without any rank premise.

The same compiler accepts independent observable roots:
\[
 Q_{1,n}=n^{-1}\sum_j u_j^2,\quad
 Q_{2,n}=n^{-1}\sum_i z_i^2,\quad
 Q^{\rm act}_{1,n}=n^{-1}\sum_j u_j^4,\quad
 Q^{\rm act}_{2,n}=n^{-1}\sum_i z_i^4.                     \tag{C5}
\]
They are respectively an isolated column of decoration two; a two-edge
row star with column decorations two and row decoration zero; an isolated
column of decoration four; and a four-edge row star with all column
decorations two. Their normalizations are exactly (B1). Hence their every
fixed derivative converges in all finite \(L^p\) by B and (C1). The first
two are squared preactivation RMS; the last two are squared activation RMS.
Initially their deterministic limits are \(1,3,3,27\), respectively.

Directly from (C1),
\[
 DQ_{1,n}=8\alpha f_n,\qquad
 D\bigl(n^{-1}\|a\|_2^2\bigr)=2f_n.                     \tag{C6}
\]
For instance \(DQ_1=(2/n)\sum_j u_jDu_j\); insertion of (C1) produces
eight times \(\alpha n^{-2}\sum_{i,j,l}a_i g_{ij}g_{il}u_j^2u_l^2\).
This proves the first identity, and \(Da=z^2\) proves the second. Thus
all fixed derivative limits obey \(Q_1^{(k)}(0)=8\alpha F^{(k-1)}(0)\).
These are feature-clock and coefficient identities; physical full-loss
flow multiplies their right sides by \(-2(f_n-y)\).

## D. A contained quadratic physical-loss width theorem

This section takes both activations to be \(\phi(v)=c v^2\), with fixed
\(c>0\), independent standard \(u,g,a\), stored connector \(g/\sqrt n\),
and mobilities \(n,n,n\) in \((u,g,a)\), equivalently \(n,1,n\) in stored
coordinates. There is one input \(x=1\), one label \(y=1\), and full loss
\(\mathcal L_n=(f_n-1)^2\). The output is \(c^3\) times the raw-square
output in C, and its feature field is \(c^3\) times (C1) at unit metric.
The normalization \(c=1/\sqrt3\) is included.

For every fixed finite sequence of real raw GD steps
\(\eta_0,\ldots,\eta_{N-1}\), the output, squared loss, the four hidden
observables (C5) with their actual \(c\) factors, and the mobility-weighted
kernel converge in probability and every finite \(L^p\) to deterministic
scalars. Explicitly these four observables are
\(n^{-1}\sum u_j^2,\ n^{-1}\sum z_i^2,\ c^2n^{-1}\sum u_j^4,\
c^2n^{-1}\sum z_i^4\), where
\(z_i=c n^{-1/2}\sum_jg_{ij}u_j^2\).
The limit is computed by finite simultaneous substitution in
forests followed by \(\chi\). The same holds for any fixed finite list of
normalized-forest observables. There is no assertion uniform in \(N\).

Here is the complete substitution argument. Use a formal feature step
\(s\). Replace every original factor by its value plus \(s\) times its
primitive field in (C1), multiplied by \(c^3\). Expand powers by the binomial
theorem. For a row factor \(a^p\), choosing \(j\) update factors attaches
\(j\) disjoint pairs of fresh leaves and lowers the old decoration by \(j\),
with multiplier \(\binom pj(sc^3)^j\). For a column factor \(u^{2q}\),
write its update as \(u(1+4sc^3 n^{-1}\sum a g g u^2)\). Choosing \(j\)
update factors attaches \(j\) fresh row/column pairs at that column and
retains its decoration, with multiplier \(\binom{2q}j(4sc^3)^j\).
Each original edge either remains or is replaced by its update gadget,
with multiplier \(2sc^3\). An edge is replaced at most once. All additions
are fresh and every removed original edge was a bridge. The final graph
is therefore a forest. Every selected update factor increases \(e/2+r\)
by one, accounting for its \(1/n\). These statements remain true when
several factors at the same original vertex are selected. Crucially the
newly attached factors are not substituted again within that step: this
is simultaneous Euler, not sequential block updating.

Thus the feature-step pullback of any forest scalar is a finite sum
\[
 S_H\circ E_s^{\rm feat}=\sum_{j=0}^{J}s^j P_{H,j},        \tag{D1}
\]
where each \(P_{H,j}\) is a width-independent finite linear combination
of forests. Raw loss GD is exactly the substitution
\(s=2\eta(1-f_n)\). Since \(f_n\) is a forest scalar, (B5) shows that
every \((1-f_n)^jP_{H,j}\) remains a finite forest combination. Iteration
proves the assertion for the complete loss program. B proves its scalar
limits and all moments, including terminal loss uniform integrability.
The kernel is the feature derivative \(Df_n\), already a finite forest
combination, so the same argument covers it. This proof uses neither an
inverse Gram matrix nor a rank-stability assumption.

Let \(\mathcal F_k(s_0,\ldots,s_{k-1})\) denote the deterministic output
limit for prescribed feature steps. As a polynomial in the steps, its
coefficients are limits of forest scalars. Consequently evaluation at random scalar steps converging in probability
preserves convergence in probability. If the steps converge in every finite
\(L^p\), the same is true of the evaluated polynomial: expand its finitely
many monomials and use Hölder and B for their products. The actual residual
steps have this stronger convergence inductively by the finite forest
closure. For the constant-step specialization \(\eta_k=\eta\), the loss
limits therefore satisfy exactly
\[
 F_k^{\eta}=\mathcal F_k(s_0,\ldots,s_{k-1}),\qquad
 s_k=2\eta(1-F_k^{\eta}).                                \tag{D2}
\]
This proves the adaptive residual identification, not merely convergence
of expected feature outputs. Also
\(\mathbb E\mathcal L_{n,k}\to(1-F_k^{\eta})^2\), because \(L^2\)
output convergence makes its variance vanish.

### D.1. Width-first loss initial layer for the normalized pure square

Set \(c=1/\sqrt3\). For every \(T>0\), \(0<\delta<1\), and
\(\eta_N=T/N\), define
\[
 \tau_N(\delta)=\eta_N\min\{k:F_k^{\eta_N}\ge\delta\}.
                                                               \tag{D3}
\]
Then \(\tau_N(\delta)\to0\). Width is taken first separately for each
finite loss program, as proved above; only then does \(N\to\infty\).

We prove the required all-order comparison rather than infer it from a
finite Taylor jet. Every finite feature update and the output are
polynomials with nonnegative coefficients in the raw Gaussian variables
and in nonnegative steps. Gaussian expectation annihilates an odd raw
monomial and is positive on an even one. Thus \(\mathcal F_k\) is
coordinatewise nondecreasing on nonnegative schedules. Deleting the first
parameter update retains a coefficientwise sub-polynomial of the fully
trained feature output: composition and addition of polynomials with
nonnegative coefficients preserve coefficientwise order. This comparison
is made before Gaussian expectation; it does not assert a samplewise order
on signed Gaussian states.

For the frozen first layer put \(q_n=n^{-1}\sum_j\phi(u_j)^2\).
Conditionally on \(u\), the rows have independent
\(a_0\sim N(0,1)\), \(z_0\sim N(0,q_n)\), and
\[
 a^+=a+scz^2,\qquad z^+=z+2scq_naz.                       \tag{D4}
\]
Every fixed update output is a polynomial. The empirical mean \(q_n\to1\)
in every finite \(L^p\): expand a centered even moment of an iid average,
where a surviving index occurs at least twice, and count at most half as
many free indices as factors. Jensen gives uniform higher moments. Hence
the frozen expected output converges to (D4) at \(q=1\), with independent
standard \(a_0,z_0\).

Use a constant feature step \(s=\rho/k\) for \(2k\) steps. The largest
step degree of either row coordinate after \(j\) steps is
\(d_j=2^j-1\). Select recursively only the quadratic top-degree terms
\(cz^2,2caz\). Their coefficients are positive integers times \(c^{d_j}\).
Their initial-variable exponent pairs start at \((1,0),(0,1)\), and update
by \((r,s)\mapsto2(u,v)\), \((u,v)\mapsto(r+u,s+v)\).
The selected output \(ca_jz_j^2\) at \(j=2k\) consequently has exponents
\((4^k,2\cdot4^k)\), step degree \(3(4^k-1)\), and coefficient at least
\(c^{3(4^k-1)+1}\). Both exponents are even. Positivity gives
\[
 \mathcal F_{2k}(\rho/k,\ldots,\rho/k)
 \ge c^{3(4^k-1)+1}(\rho/k)^{3(4^k-1)}
                          (4^k/e)^{4^k}\longrightarrow+\infty.   \tag{D5}
\]
Here \(\mathbb EG^{2b}=(2b-1)!!\ge b!\ge(b/e)^b\); the last inequality
follows by integrating \(\log x\) from \(1\) to \(b\). The logarithm of
the displayed bound, divided by \(4^k\), is
\(k\log4-3\log k+O_{c,\rho}(1)\), which tends to infinity.

Before the first \(\delta\)-hit, (D2) has
\(s_j>2(1-\delta)\eta_N\). Fix \(0<\varepsilon<T\), put
\(k_N=\lfloor\varepsilon/(2\eta_N)\rfloor\), and choose
\(\rho=(1-\delta)\varepsilon/2\). Eventually
\(\rho/k_N\le2(1-\delta)\eta_N\). If no hit occurred by \(2k_N\),
schedule monotonicity and (D5) would give \(F_{2k_N}^{\eta_N}\to+\infty\),
contradicting \(F_{2k_N}^{\eta_N}<\delta\). Thus
\(\tau_N(\delta)\le\varepsilon\) eventually, proving (D3).

The initial output limit is zero. Any continuous interpolation of these
grid predictors crosses \(\delta\) at times tending to zero and therefore
cannot converge uniformly on \([0,T]\) to a continuous initialized
predictor. The same obstruction holds for the squared loss evaluated from
that continuous predictor: at a crossing it equals \((1-\delta)^2\ne1\).
In particular this applies to raw-parameter interpolation followed by
recomputation, whose fixed-cell limit is a finite polynomial in the cell
fraction by (D1), and to polygonal predictor interpolation followed by
squaring. It does not assert the same crossing identity for independently
polygonally interpolated loss values after an arbitrarily large overshoot.

No post-hit comparison is used: residuals can change sign there. Thus this
theorem gives no terminal fine/coarse loss limit, no finite-width GF initial
layer, and no assertion for an arbitrary joint \(N=N(n)\) diagonal.

## E. Reusable finite depth jets and observable heads

Fix finite \(L,m,d,n\), arbitrary deterministic data \((x_a,y_a)\), and
the stored-weight model and full mean loss
\(\mathcal L_n=m^{-1}\sum_a(f_{n,a}-y_a)^2\). For this subsection only,
\([k]\) denotes the ordinary coefficient of \(t^k\), not a derivative.
Given coefficients of a scalar series \(z\), define
\[
 [\phi^{(r)}(z)]_{[k]}=
 \sum_{b=0}^{k}\frac{\phi^{(r+b)}(z_{[0]})}{b!}
 \sum_{i_1+\cdots+i_b=k,\ i_j\ge1}
             z_{[i_1]}\cdots z_{[i_b]}.                  \tag{E1}
\]
The inner sum for \(b=0\) is one for \(k=0\) and zero otherwise.
Use coordinatewise multiplication in (E1). At each degree \(k\), compute
\[
 \begin{aligned}
 z^{(1)}_{a,[k]}&=W^{(1)}_{[k]}x_a/\sqrt d,\\
 z^{(\ell)}_{a,[k]}&=\sum_{i+j=k}W^{(\ell)}_{[i]}
                                      h^{(\ell-1)}_{a,[j]},\\
 h^{(\ell)}_{a,[k]}&=[\phi^{(\ell)}(z^{(\ell)}_a)]_{[k]},\\
 \delta^{(L)}_{a,[k]}&=\sum_{i+j=k}W^{(L+1)}_{[i]}
                           \odot[(\phi^{(L)})'(z^{(L)}_a)]_{[j]},\\
 b^{(\ell)}_{a,[k]}&=\sum_{i+j=k}(W^{(\ell+1)}_{[i]})^T
                                            \delta^{(\ell+1)}_{a,[j]},\\
 \delta^{(\ell)}_{a,[k]}&=\sum_{i+j=k}
       [(\phi^{(\ell)})'(z^{(\ell)}_a)]_{[i]}\odot b^{(\ell)}_{a,[j]},\\
 f_{a,[k]}&=n^{-1}\sum_{i+j=k}(W^{(L+1)}_{[i]})^Th^{(L)}_{a,[j]},
 \qquad r_{a,[k]}=f_{a,[k]}-y_a\mathbf1_{k=0}.
 \end{aligned}                                                   \tag{E2}
\]
The forward degrees are computed bottom to top, and the reverse degrees
top to bottom, always using the actual transpose. With block mobilities
\(n\kappa_1,\kappa_2,\ldots,\kappa_L,n\kappa_{L+1}\), integrate
the exact physical field coefficientwise:
\[
 \begin{aligned}
 W^{(1)}_{[k+1]}&=-\frac{2\kappa_1}{m(k+1)\sqrt d}
             \sum_a\sum_{i+j=k}r_{a,[i]}\delta^{(1)}_{a,[j]}x_a^T,\\
 W^{(\ell)}_{[k+1]}&=-\frac{2\kappa_\ell}{mn(k+1)}
     \sum_a\sum_{i+j+b=k}r_{a,[i]}\delta^{(\ell)}_{a,[j]}
                                         (h^{(\ell-1)}_{a,[b]})^T,\\
 W^{(L+1)}_{[k+1]}&=-\frac{2\kappa_{L+1}}{m(k+1)}
             \sum_a\sum_{i+j=k}r_{a,[i]}h^{(L)}_{a,[j]}.
 \end{aligned}                                                   \tag{E3}
\]
Equations (E1)–(E3) form a triangular finite derivative algorithm through
any prescribed positive integer order \(q\), provided every activation is \(C^{q+1}\) near
the supplied finite state. For example one may restrict the implementation
to \(q\le5\); order zero simply returns the supplied state.
A finite \(C^1\) field has a local solution by contraction of
its integral equation on a small bounded ball; repeated differentiation
gives the stated finite jets. Taylor's finite composition rule proves (E1),
ordinary products prove (E2), and comparing \(t^k\) coefficients in the
raw gradient equations proves (E3). This establishes every factor of
\(n,m,k+1\). It imposes no distributional initialization, data orthogonality
or population limit. It is a finite derivative algorithm, not time stepping
by a truncated series.

The same stored parameter jets can serve any \(C^q\) observable \(O\):
substitute the finite series in its multivariate Taylor polynomial. Writing
\(v=\dot\theta\), \(p_1=D_vv,p_2=D_v^2v,p_3=D_v^3v\), the first four
derivatives are
\[
 \begin{aligned}
 O'&=O_1[v],\\
 O''&=O_2[v,v]+O_1[p_1],\\
 O'''&=O_3[v,v,v]+3O_2[v,p_1]+O_1[p_2],\\
 O^{(4)}&=O_4[v,v,v,v]+6O_3[v,v,p_1]+3O_2[p_1,p_1]
                              +4O_2[v,p_2]+O_1[p_3].
 \end{aligned}                                                   \tag{E4}
\]
These follow by differentiating the preceding line and using symmetry of
the derivative tensors. They reuse parameter derivatives but do not claim
that averaged observable contractions have a fixed scalar closure.

For either an activation or a preactivation vector \(X(t)\), now use actual
derivatives \(X_j=X^{(j)}(0)\). Its squared RMS \(Q=\|X\|_2^2/n\) has
\[
 Q^{(k)}(0)=\sum_{j=0}^k{k\choose j}\Gamma_{j,k-j},\quad
 \Gamma_{ij}=X_i^TX_j/n;\qquad
 Q''=2\Gamma_{02}+2\Gamma_{11},\quad
 Q^{(4)}=2\Gamma_{04}+8\Gamma_{13}+6\Gamma_{22}.            \tag{E5}
\]
Product differentiation proves this exactly. For a hidden affine map
\(z=W h\), the fourth moving derivative is
\[
 z_4=W h_4+4W_1h_3+6W_2h_2+4W_3h_1+W_4h_0,
\]
and the activation derivative is
\[
 h_4=\phi^{(4)}(z)z_1^4+6\phi'''(z)z_1^2z_2
                   +3\phi''(z)z_2^2+4\phi''(z)z_1z_3+\phi'(z)z_4. \tag{E6}
\]
Each product here is coordinatewise. A straight parameter line freezes the
direction and sets its higher parameter derivatives to zero; the moving
flow generally does neither. Thus its fourth contraction must be computed
by (E2)–(E6), not borrowed from a straight-line fourth derivative.

For feature ascent of one scalar predictor with constant block metric,
readout reflection \(S\) satisfies \(f(S\theta)=-f(\theta)\) and
\(v(S\theta)=-Sv(\theta)\). Uniqueness of the finite local ODE gives
\(\theta(s;S\theta_0)=S\theta(-s;\theta_0)\). Hidden vectors are
unchanged by \(S\) at a fixed state, so their \(j\)-th jets change by
\((-1)^j\). Under a reflection-invariant initial law with the requisite
finite moments, odd annealed hidden Gram derivatives vanish and the
annealed output jet is odd. Neither vanishing statement is seedwise.

For a deterministic even coefficient germ
\(Q(s)=q_0+q_2s^2/2+q_4s^4/24+\cdots\), \(q_0>0\), its formal RMS is
\[
 (\sqrt Q)''(0)=q_2/(2\sqrt{q_0}),\qquad
 (\sqrt Q)^{(4)}(0)=q_4/(2\sqrt{q_0})-3q_2^2/(4q_0^{3/2}). \tag{E7}
\]
Squaring the Taylor polynomial proves this; more generally its ordinary
coefficients satisfy \(r_0=\sqrt{q_0}\),
\(r_k=(q_{[k]}-\sum_{i=1}^{k-1}r_i r_{k-i})/(2r_0)\).
This is the square root of a deterministic coefficient germ. It is not an
exchange of square root with annealed expectation of finite-width jets.

If \(F\) is an odd deterministic germ with \(F'(0)=A,F'''(0)=B\), define
the label-one full-loss formal clock \(s'=2(1-F(s)),s(0)=0\).
With a general constant \(c_0\) in place of \(2\), substitution gives
\(s_1=c_0,s_2=-c_0^2A,s_3=c_0^3A^2,
s_4=-c_0^4(A^3+B)\). Inserting these into \(Q(s(t))\) gives
\[
 Q_t''=c_0^2q_2,\quad Q_t'''=-3c_0^3Aq_2,\quad
 Q_t^{(4)}=c_0^4(q_4+7A^2q_2),\quad
 Q_t^{(5)}=-5c_0^5\{(3A^3+B)q_2+2Aq_4\}.                 \tag{E8}
\]
For example the \(s^2\) coefficient at order five is
\(-c_0^5(3A^3+B)/12\), and the \(s^4\) coefficient is
\(-2c_0^5A\), proving the last line after the factorial factors. These
are finite formal identities after any needed coefficient limits; they
do not make loss GD an exact constant-step feature scheme.

### E.1. A local Gaussian fourth-order hidden head

Supply a centered jointly Gaussian vector \((Z,U_1,U_2,U_3,U_4)\),
with \(\mathbb EZ^2=1\), a centered jointly Gaussian vector
\((V_0,V_1,V_2,V_3)\) independent of the first, and their full positive
semidefinite covariance matrices. Degenerate matrices are allowed.
Supply constants \(\lambda_1,\lambda_2,\lambda_{30},\lambda_{32},
\lambda_{41},\lambda_{43},c_{10},d_{21},d_{30},d_{32}\).
For an actual expectation assume \(\phi\) is polynomial, or smooth with
polynomial bounds for all derivatives used below. The polynomial case
already gives a complete exact finite contract. Put \(p_j=\phi^{(j)}(Z)\)
and define, in order,
\[
\begin{aligned}
d_0&=p_1V_0,&z_1&=U_1+\lambda_1d_0,&h_0&=p_0,&h_1&=p_1z_1,\\
r_1&=V_1+c_{10}h_0,&
d_1&=p_2z_1V_0+p_1r_1,&z_2&=U_2+\lambda_2d_1,\\
h_2&=p_2z_1^2+p_1z_2,&r_2&=V_2+d_{21}h_1,\\
d_2&=p_3z_1^2V_0+p_2z_2V_0+2p_2z_1r_1+p_1r_2,\\
z_3&=U_3+\lambda_{30}d_0+\lambda_{32}d_2,&
h_3&=p_3z_1^3+3p_2z_1z_2+p_1z_3,\\
r_3&=V_3+d_{30}h_0+d_{32}h_2,\\
d_3&=p_4z_1^3V_0+3p_3z_1z_2V_0+p_2z_3V_0
       +3p_3z_1^2r_1+3p_2z_2r_1+3p_2z_1r_2+p_1r_3,\\
z_4&=U_4+\lambda_{41}d_1+\lambda_{43}d_3,\\
h_4&=p_4z_1^4+6p_3z_1^2z_2+3p_2z_2^2+4p_2z_1z_3+p_1z_4 .
\end{aligned}                                                    \tag{E9}
\]
These are a finite directed algebra. The \(h_j\) are the literal Bell
polynomials for the \(j\)-th derivative of \(\phi(z(s))\) with supplied
jets \(z_j\); the \(d_j\) are the product derivatives of
\(\phi'(z(s))r(s)\), with \(r(0)=V_0\) and the supplied \(r_j\).
This proves every integer coefficient in (E9). The additional linear
rules defining \(z_j,r_j\) are explicit inputs to this local model;
their origin in a trained network is not presumed.

The observable and response outputs are
\[
 \gamma_{\rm out}=\mathbb E[h_0h_4],\qquad
 A_{41,\rm out}=\mathbb E[\partial_{V_1}h_4],\qquad
 A_{43,\rm out}=\mathbb E[\partial_{V_3}h_4].               \tag{E10}
\]
These partial derivatives hold all other Gaussian coordinates and supplied
constants fixed, before expectation. They are not derivatives of covariance
data or of a trained trajectory. The additional Gram outputs
\(\mathbb Eh_1h_3,\mathbb Eh_2^2\) combine with \(\gamma_{\rm out}\)
by (E5) to give the local fourth squared-RMS head.

All Gaussian eliminations have a finite constructive proof. For a
non-\(Z\) Gaussian coordinate \(X\), remove one factor from a monomial
\(XP\) and use
\[
 \mathbb E[XP]=\sum_Y\operatorname{Cov}(X,Y)
                                  \mathbb E[\partial_Y P].       \tag{E11}
\]
The sum includes \(Z\); its partial derivative replaces one \(p_j\)
factor by \(p_{j+1}\), with multiplicity. Other partials remove a
Gaussian factor. Write the full Gaussian vector as a deterministic linear
image of independent standard Gaussians and integrate each density by
parts to prove (E11). Polynomial bounds kill all boundary terms; no
covariance inverse is used, so singular matrices are included.
Every recursion removes at least one non-\(Z\) factor and terminates at
\[
 M_{k_0,\ldots,k_J}
 =\mathbb E\prod_{j=0}^J\phi^{(j)}(Z)^{k_j}.               \tag{E12}
\]
For polynomial \(\phi\), expansion and B evaluate these atoms exactly.
Otherwise they are explicit one-dimensional integrals. A formal evaluator
may instead return a polynomial in covariance symbols and \(M\)-atoms.
That mode asserts no Gaussian law for arbitrary symbols. In particular,
an omitted covariance is not permission to set it to zero if the resulting
matrix is not positive semidefinite. The actual derivative ceiling must
be computed for the supplied covariance pattern; no universal ceiling of
five is asserted for arbitrary Gaussian data.

Only \(r_3\) contains \(V_3\), so (E9) directly gives
\[
 \partial_{V_3}h_4=\lambda_{43}p_1^2,\qquad
 A_{43,\rm out}=d\lambda_{43},\quad d=\mathbb E\phi'(Z)^2.  \tag{E13}
\]
For a layer iteration with constant \(d\),
\(\lambda_{43,\ell}=1+A_{43,\ell-1}\), and \(A_{43,0}=0\),
induction yields \(1+A_{43,\ell}=\sum_{j=0}^{\ell}d^j\).
This coordinate needs no dynamic state; the remaining head stores
\((\gamma,A_{41})\), with all lower-order inputs supplied.
Layer-dependent \(d_\ell\) instead gives
\(\tau_\ell=1+d_\ell\tau_{\ell-1}\), \(\tau_0=1\).
This is an exact algebraic elimination. It supplies neither a neural
population interpretation of the input covariance data nor a bridge from
initialization derivatives to positive-time dynamics.

## F. Typed curvature words and their finite derivative meaning

Fix a finite feedforward network at one supplied state, with arbitrary
widths \(n_1,\ldots,n_L\), stored readout \(a\in\mathbb R^{n_L}\),
matrices \(W^{(\ell)}:\mathbb R^{n_{\ell-1}}\to\mathbb R^{n_\ell}\),
and componentwise \(C^2\) activations. Write
\(f=a^Th^{(L)}/n_L\). No initialization or optimizer is assumed here.

For each layer define the downstream scalar function \(F_\ell(z)\) by
replacing only its preactivation by the independent variable \(z\), then
recomputing every downstream activation with all downstream matrices and
the readout held fixed. Put
\[
 \delta_\ell=n_L\nabla_zF_\ell(z^{(\ell)}),\quad
 R_\ell=n_L\nabla_z^2F_\ell(z^{(\ell)}),\quad
 D_\ell=\operatorname{diag}(\phi_\ell'(z^{(\ell)})).
                                                               \tag{F1}
\]
Thus \(R_\ell:\mathbb R^{n_\ell}\to\mathbb R^{n_\ell}\) is symmetric.
Define \(b_L=a\), \(b_\ell=(W^{(\ell+1)})^T\delta_{\ell+1}\) for
\(\ell<L\), and the actual local Hessian source
\[
 E_\ell=\operatorname{diag}\bigl(\phi_\ell''(z^{(\ell)})
                                                    \odot b_\ell\bigr).
                                                               \tag{F2}
\]
The exact recursions are
\[
 \delta_\ell=D_\ell b_\ell,\qquad R_L=E_L,\qquad
 R_\ell=E_\ell+D_\ell(W^{(\ell+1)})^T
                  R_{\ell+1}W^{(\ell+1)}D_\ell.           \tag{F3}
\]
To verify the Hessian formula, the map from \(z^{(\ell)}\) to
\(z^{(\ell+1)}\) is \(T(z)=W^{(\ell+1)}\phi_\ell(z)\).
Its first variation is \(W^{(\ell+1)}D_\ell v\), and its second variation
is \(W^{(\ell+1)}(\phi_\ell''\odot v\odot w)\). The scalar second
chain rule gives one term contracting two first variations against
\(R_{\ell+1}\), and one contracting the second variation against
\(\delta_{\ell+1}\). The latter is \(v^TE_\ell w\). This proves (F3)
for every \(v,w\), including all normalization factors.

Let \(J_{\ell\leftarrow1}\) be the Jacobian of \(z^{(\ell)}\) with
respect to \(z^{(1)}\), with the weights fixed:
\[
 J_{1\leftarrow1}=I,\qquad
 J_{\ell\leftarrow1}=W^{(\ell)}D_{\ell-1}\cdots W^{(2)}D_1.
\]
Repeated substitution in (F3) yields
\[
 R_1=\sum_{\ell=1}^L J_{\ell\leftarrow1}^TE_\ell
                                      J_{\ell\leftarrow1}.       \tag{F4}
\]
Induction proves the expansion and provides a type check for each product.
For layer three its term is exactly
\(D_1(W^{(2)})^TD_2(W^{(3)})^TE_3W^{(3)}D_2W^{(2)}D_1\).
Erasing the diagonal factors gives the matrix-orientation word
\((2^-,3^-,3^+,2^+)\). Counting distinct matrix labels records how many
different stored matrices occur. It is a syntactic attribute of a term
whose finite semantics has now been specified; it is no theorem about
independence, nonclosure, probability or convergence.

If \(\phi_\ell''\equiv0\), its local source is identically zero, so that
source term can be omitted. This may be specified layer by layer. When
all activations are affine, every \(R_\ell\) is zero because \(F_\ell\)
is affine in its independent preactivation. The full parameter Hessian
need not vanish: even \(f(a,u)=au\) has mixed derivative one. In particular
\(R_1/n_L\) is the first-preactivation Hessian only, not the full parameter
Hessian and not the material derivative of a trained backward field.
Differentiating along training also varies all downstream weights and
requires their explicit first variations. This held-fixed contract is
part of the API, not something a string emitter can infer.

## G. Additional shallow comparisons

### G.1. Identity: exact raw-GD closure, joint compact-time limit and moments

Take one input \(x=1\), one hidden layer, identity activation, arbitrary
label \(y\in\mathbb R\), full loss \((f_n-y)^2\), and equal mobilities
\(n\kappa\), \(\kappa>0\), for first weights \(u\) and stored readout
\(a\). Both initial vectors have independent standard Gaussian entries.
At a finite state put
\[
 f_n=a^Tu/n,\quad q_n=(\|a\|_2^2+\|u\|_2^2)/n,\quad
 d_n=(\|a\|_2^2-\|u\|_2^2)/n.
\]
If \(b=-2\kappa\eta(f_n-y)\), simultaneous raw GD gives
\[
 a^+=a+bu,\quad u^+=u+ba,\qquad
 f_n^+=(1+b^2)f_n+bq_n,\quad
 q_n^+=(1+b^2)q_n+4bf_n,\quad d_n^+=(1-b^2)d_n.            \tag{G1}
\]
These equations follow by multiplying the two updated vectors and
expanding their squared norms. They are an exact three-scalar update at
every width. The kernel before a step is \(\kappa q_n\), and the separate
kernel blocks are \(\kappa(q_n-d_n)/2\) and
\(\kappa(q_n+d_n)/2\).

Finite physical GF has
\[
 \dot f_n=-2\kappa(f_n-y)q_n,\quad
 \dot q_n=-8\kappa(f_n-y)f_n,\quad \dot d_n=0,\quad
 q_n^2-4f_n^2=\text{constant}.                            \tag{G2}
\]
The derivative of the last expression is zero by direct substitution.
Gaussian sample averages give \((f_n,q_n,d_n)(0)\to(0,2,0)\) in probability
and every finite \(L^p\). One direct proof for centered averages is the
even-moment index count used after (D4); Gaussian moments of all orders
exist. The deterministic limit solves
\[
 \dot f=-4\kappa(f-y)\sqrt{1+f^2},\quad f(0)=0,\qquad
 q=2\sqrt{1+f^2},\quad d=0.                              \tag{G3}
\]
Local existence follows from a locally Lipschitz scalar field. Its residual
has constant sign and
\[
 |f(t)-y|=|y|\exp\left(-4\kappa\int_0^t\sqrt{1+f(v)^2}\,dv\right)
                                  \le|y|e^{-4\kappa t}.          \tag{G4}
\]
Thus \(f\) remains between zero and \(y\), which prevents escape and proves
global existence and uniqueness. Equation (G4) also proves fitting.

For every deterministic sequence \(\eta_n>0\), \(\eta_n\to0\), raw GD
with weights linearly interpolated and predictor/kernel recomputed obeys,
on every fixed \([0,T]\),
\[
 \sup_{t\le T}\bigl(|f_n(t)-f(t)|+|q_n(t)-q(t)|+|d_n(t)|\bigr)
                                  \xrightarrow{\mathbb P}0.     \tag{G5}
\]
Here is a direct proof that includes the growing number of updates. The
exact scalar scheme (G1) has the form
\(x^+=x+\eta V(x)+\eta^2R(x)\), with polynomial \(V,R\) independent of
width. Choose a closed rectangular box containing the compact limiting curve
with distance at least one from its boundary. On that box,
\(V\) is Lipschitz with some finite constant \(L_T\), \(R\) is bounded,
and the exact limiting step has error at most \(C_T\eta^2\), obtained by
integrating \(V(x(t+s))-V(x(t))\). Until first exit from the box, the
grid error therefore satisfies
\(e_{k+1}\le(1+L_T\eta)e_k+C_T\eta^2\), hence
\(e_k\le e^{L_T(T+1)}(e_0+C_T(T+1)\eta)\).
When \(e_0\) and the step are sufficiently small, the right side is less than
half the box margin, ruling out a first exit. Convergence
in probability of \(e_0\) proves the grid assertion. Within a raw
interpolation cell, replace \(b\) by \(\lambda b\) in (G1),
\(0\le\lambda\le1\); the same bounded polynomials give a uniform
\(O_T(\eta)\) cell displacement, proving (G5). The output loss and both
kernel blocks follow by continuous finite formulas on the box. There is
no rate condition coupling \(\eta_n\) to \(n\), and no conclusion for a
growing physical horizon.

In feature time \(s\), the exact characteristics are
\[
 A_s=a_0\cosh s+u_0\sinh s,\qquad
 U_s=u_0\cosh s+a_0\sinh s.
\]
Gaussian expectation gives \(F(s)=\sinh(2s)\). The physical clock is
\(s'=-2\kappa(F(s)-y)\), and its endpoint is
\(s_*=(\operatorname{arsinh}y)/2\). Indeed monotonicity and (G4) give
\(s(t)\to s_*\); the displayed linear combinations then converge in every
finite mark-space \(L^p\). This endpoint assertion concerns the canonical
population physical flow, separately from compact-time joint GD convergence.

The exact output-coordinate feature kernel is
\(K(v)=2\sqrt{1+v^2}\). Therefore
\[
 (K(\sqrt x)-2)/x=\sum_{j\ge0}(-1)^j\mu_jx^j,\qquad
 \mu_j=\frac{1}{4^j(j+1)}{2j\choose j}.                   \tag{G6}
\]
These coefficients follow from the binomial expansion, valid near zero or
formally. They are the moments of
\[
 d\nu(t)=\frac2\pi\sqrt{(1-t)/t}\,\mathbf1_{0<t<1}\,dt.  \tag{G7}
\]
To verify without a special-function import, set \(t=\sin^2\theta\).
The \(j\)-th moment is
\((4/\pi)\int_0^{\pi/2}\sin^{2j}\theta\cos^2\theta\,d\theta\).
Integration by parts gives
\(I_j=\int_0^{\pi/2}\sin^{2j}\theta\,d\theta
=(2j-1)I_{j-1}/(2j)\),
\(I_0=\pi/2\); subtracting \(I_{j+1}\) from \(I_j\) yields exactly (G6).
For any nonzero polynomial \(p\), both
\(\int p(t)^2d\nu(t)\) and \(\int t p(t)^2d\nu(t)\) are strictly positive,
since the density is positive on an interval. Thus every ordinary and
shifted Hankel matrix of \((\mu_j)\) is positive definite. This all-order
statement is specific to this identity model.

### G.2. Raw-square shallow characteristics and the metric-boundary reduction

For one hidden layer, \(f_n=n^{-1}\sum_i a_i v_i^2\), independent standard
Gaussian \(a_i,v_i\), and feature mobilities \(n,n\), the exact neurons solve
\[
 a'=v^2,\qquad v'=2av.                                    \tag{G8}
\]
The invariant is \(c_*=a_0^2-v_0^2/2\). Let
\(B''=4c_*B,B(0)=1,B'(0)=-2a_0\). Before its first zero,
\[
 a=-B'/(2B),\quad v=v_0/B,\quad
 B(s)=\begin{cases}
 \cosh(2\sqrt{c_*}s)-(a_0/\sqrt{c_*})\sinh(2\sqrt{c_*}s),&c_*>0,\\
 1-2a_0s,&c_*=0,\\
 \cos(2\sqrt{-c_*}s)-(a_0/\sqrt{-c_*})\sin(2\sqrt{-c_*}s),&c_*<0.
 \end{cases}                                                   \tag{G9}
\]
Indeed \(B'^2-4c_*B^2=2v_0^2\) is constant. Differentiating the two
quotients and using that identity gives (G8) and their initial values.
This includes \(v_0=0\), where the solution is stationary. The finite
feature output is \(-\frac1{2n}\sum_i v_{i0}^2B_i'/B_i^3\).
For full squared loss and arbitrary label \(y\), physical time obeys
\(s'=2(y-f_n(s))\) wherever the feature characteristic is available;
on a branch with nonzero residual it is equivalently
\(t(s)=\frac12\int_0^s(y-f_n(u))^{-1}du\). These are maximal-interval
statements, not a positive-time Gaussian population construction.

Freezing the first block of the two-hidden-layer raw-square network gives
\(q_n=n^{-1}\sum_j u_j^4\) and \(z_i'=2q_na_iz_i\). Conditional on \(u\),
\(v_i=z_i/\sqrt{q_n}\) are iid standard Gaussians independent of \(a\),
and their conditional law is independent of \(u\). Hence they are also
independent of \(q_n\). The reduced output is
\(q_n n^{-1}\sum_i a_i v_i^2\), with feature equations
\(a_i'=q_nv_i^2,v_i'=2q_na_iv_i\). Since \(q_n\to3\) with every finite
moment, every fixed derivative has the limiting scaling
\[
 F_{\rm red}^{(k)}(0)=3^{k+1}F_{\rm sh}^{(k)}(0).           \tag{G10}
\]
For example the conditional derivative expectation is exactly a constant
times \(q_n^{k+1}\); Jensen bounds its higher moments by a fixed Gaussian
moment. This proves the limit without a trajectory interchange.

For any fixed deterministic multiplier \(b>0\), formally
\(F_b(s)=bF_1(bs)\), \(K_b(v)=b^2K_1(v/b)\). Thus if
\((K_b(\sqrt x)-7b^2)/x=\sum_j(-1)^j\mu_j^{(b)}x^j\),
\[
 \mu_j^{(b)}=b^{-2j}\mu_j^{(1)},\qquad
 \det(\mu_{i+j+1}^{(b)})_{i,j=0}^2
       =b^{-18}\det(\mu_{i+j+1}^{(1)})_{i,j=0}^2.          \tag{G11}
\]
The diagonal congruence has entries \(b^{-2i}\), with the extra common
factor \(b^{-2}\), proving the determinant factor.

For completeness a finite scalar regeneration of the conventional shallow
certificate is: apply
\(X(a^pv^q)=p a^{p-1}v^{q+2}+2q a^{p+1}v^q\) repeatedly to \(av^2\),
then evaluate by \(m(p)m(q)\) from B. Divide the result at order \(k\) by
\(k!\), solve \(F(G(y))=y\) coefficientwise, and form \(F'(G(y))\).
Through order thirteen this gives the six moments
\[
 \left(\frac{480}{49},\frac{43756}{16807},
 \frac{7214528}{2470629},\frac{37635527904}{9886633715},
 \frac{171752915595136}{30520038278205},
 \frac{2199776554157960896}{246754509479287425}\right),
\]
and direct rational elimination gives
\[
 \det(\mu_{i+j+1})_{i,j=0}^2
 =-\frac{86245462994269879146938487857152}
         {516623655319449980325461333747775}<0.             \tag{G12}
\]
The two monomial recursions just specified determine every displayed
number using integers and rational arithmetic; their correctness follows
from (G8), Gaussian integration by parts, and triangular coefficient
comparison. If these were nonnegative-measure moments on \([0,\infty\)),
the matrix in (G12) would have quadratic form
\(\int t p(t)^2d\nu(t)\ge0\), which contradicts its negative determinant.
Equivalently (G11) transfers the same certificate from the multiplier-three
boundary. No centered or Hermite-normalized quadratic, different initial
law, or multiple-input model is included.

For every prescribed positive feature time there is an open Gaussian
initial-data set with a pole earlier: at \(c_*=0,a_0>0\) the denominator
zero is \(1/(2a_0)\), and it is transverse when \(v_0\ne0\). Take large
\(a_0\) and use continuity of that transverse zero under nearby initial
data. Gaussian density is positive on the open set. Thus the maximal
characteristic formula cannot itself define a common positive-time ordinary
Gaussian pushforward for all marks. The finite coefficients and the
Stieltjes obstruction remain valid independently of that obstruction.

## H. Finite coefficient certificates and proposed interfaces

Let \(F(s)=a_1s+a_3s^3+\cdots\) be a formal odd series over a characteristic
zero field with \(a_1\ne0\). Its inverse \(G(y)=\sum b_jy^j\) is uniquely
determined by
\[
 b_1=a_1^{-1},\qquad
 b_j=-a_1^{-1}[y^j]\sum_{l=2}^{j}a_l
                         \left(\sum_{i<j}b_i y^i\right)^l.       \tag{H1}
\]
Only the linear term contains \(b_j\), proving existence and uniqueness
by induction. The inverse is odd, by applying uniqueness to \(-G(-y)\).
For \(K=F'\circ G\) and
\((K(\sqrt x)-a_1)/x=\sum_{r\ge0}(-1)^r\mu_rx^r\),
\(\mu_r\) depends only on \(F\) through order \(2r+3\), and its dependence
on the highest derivative is affine with coefficient
\[
 [F^{(2r+3)}(0)]\mu_r
       =\frac{(-1)^r}{(2r+2)!a_1^{2r+2}}.                 \tag{H2}
\]
Indeed the only new coefficient at that order in \(F'(G(y))\) is
\((2r+3)a_{2r+3}(y/a_1)^{2r+2}\); the other nonconstant derivative
terms require inverse coefficients only through order \(2r+1\).
Thus output order seventeen determines eight kernel moments. It does not
determine the next output derivative.

For the quadratic first hidden root with (C6), put
\(N(y)=Q_1(G(y))\). Formal chain differentiation gives
\[
 \frac{d}{dx}N(\sqrt x)=\frac{4\alpha}{K(\sqrt x)}.
                                                               \tag{H3}
\]
If \(1/K(\sqrt x)=\sum_{r\ge0}(-1)^rh_rx^r\), integration in the
formal variable gives the first-hidden companion moments
\(\rho_r=4\alpha h_r/(r+1)\). Therefore an output jet through order
seventeen determines nine such hidden moments, the last using the Ward
identity \(Q_1^{(18)}=8\alpha F^{(17)}\). This is a dependency statement,
not a claim that a high-order numerical prefix has been generated.

For a supplied symmetric block matrix
\(H=\begin{pmatrix}A&b\\b^T&c\end{pmatrix}\) with \(A\) positive
definite, completing the square gives
\[
 (v,t)^TH(v,t)=(v+tA^{-1}b)^TA(v+tA^{-1}b)
                         +t^2(c-b^TA^{-1}b).              \tag{H4}
\]
Thus \(H\succeq0\) exactly when \(c\ge b^TA^{-1}b\); strict inequality
means positive definiteness, and
\(\det H=\det A(c-b^TA^{-1}b)\) follows by the same triangular change of
variables. If \(A\) is singular positive semidefinite, replace the inverse
by its inverse on the range, require \(b\in\operatorname{ran}A\), and
the same proof applies after orthogonal splitting into range and kernel.
Necessity of the range condition follows by testing \(v\in\ker A\) with
both signs of \(t\). These give exact next-moment thresholds without
recomputing earlier moments. Finite positive gates do not establish an
infinite moment representation.

Interval certificates likewise have a small contained algebra. For a
polynomial \(P\) of degree at most \(d\), write
\(P(a+(b-a)t)=\sum_{k=0}^{d}c_kt^k\), \(a<b\). Its Bernstein coefficients
on this interval are
\[
 \beta_j=\sum_{k=0}^j c_k\frac{{j\choose k}}{{d\choose k}},\qquad
 P(a+(b-a)t)=\sum_{j=0}^d\beta_j{d\choose j}t^j(1-t)^{d-j}. \tag{H5}
\]
The identity follows from
\({d\choose j}{j\choose k}={d\choose k}{d-k\choose j-k}\)
and the binomial theorem. The basis functions are nonnegative and sum to
one for \(0\le t\le1\). All negative \(\beta_j\) therefore prove strict
negativity on the closed interval; all nonpositive coefficients prove the
weak version. Alternatively \(P''\ge0\) and negative endpoint values
imply negativity by the convex chord bound, proved by monotonicity of
secant slopes. For a rational witness \(P/Q\), first prove \(Q>0\) on
the entire interval. These tests certify a supplied polynomial; they do
not verify its neural coefficient provenance or a numerical interval
endpoint without that polynomial's regeneration.

The finite-calculus modules provide the following bounded interfaces. The
implementation guide specifies their exact input types, floating arithmetic
limits and deterministic checks:

| Operation | Input and output contract |
|---|---|
| `gradient_tree_terms(order)` | Nonnegative integer order; exact integer weights and canonical unrooted parameter-contraction trees from A. |
| `forest_expectation(forest, width=None)` | Explicit nonnegative integer row/column decorations and simple acyclic edges; exact Gaussian value from (B2) at positive integer width, or leading value from B when omitted. For odd edge count the expectation is zero. |
| `quadratic_forest_derivatives(root, order, alpha, beta)` | A root forest, finite order and nonnegative rational block multipliers; finite derivative polynomial from C, with grades and normalizations retained. |
| `quadratic_euler_pullback(root, step, loss=False, label=1)` | One simultaneous substitution (D1) restricted to raw squares \(c=1\) and unit block multipliers, or the full-squared-loss substitution with an explicit label; exact forest polynomial, never a population trajectory. |
| `finite_flow_jets(state, inputs, labels, activations, order, kappas)` | Supplied finite raw state and derivative callbacks through the declared ceiling; ordinary parameter/forward coefficients through order five and reverse coefficients through one lower order from E and an explicit `clock="physical_full_mean_loss"` tag. |
| `hidden_gram_jet(jets, layer, kind)` | One-based layer and explicit activation/preactivation choice; float64 ordinary same-layer Gram coefficients. |
| `gaussian_hidden_head(covariance, responses, activation)` | Actual-Gaussian polynomial case of (E9)–(E13), complete rational covariance data, fixed-coordinate partials, and polynomial activation derivatives zero through four. No formal-symbolic or nonpolynomial integration mode is implemented. |
| `preactivation_hessian_words(layer_shapes, affine_flags)` | Typed factors in (F4), shapes, orientation and local source layer; valid source elimination only for declared identically affine activations. |
| `preactivation_hessians(state, inputs, activations)` | Numeric \(R_\ell,E_\ell\) and fixed-variable contract (F1)–(F3), with actual transpose checks; no full-parameter-Hessian label. |
| `identity_shallow_step(f, q, d, label, mobility, step)` | Exact scalar update (G1), with stated full-loss convention and supplied finite scalar state. |
| `next_hankel_threshold(A,b)` / `bernstein_coefficients(P,a,b)` | Exact finite matrix/polynomial operations (H4)–(H5), with explicit singular-range and interval validation. |

Integers used as counts must reject booleans and nonintegral types rather
than coercing them silently. Floating implementations must state that
roundoff and intermediate overflow can invalidate numerical evaluation;
an exact symbolic identity is not an exact floating-point certificate.
Inputs and outputs should be owned independently, and no operation should
load retained coefficients, run a campaign, mutate a supplied state or
write files. The graph evaluators have combinatorial cost at caller-chosen
finite size; no efficient general high-order promise is made.


## Integrated queries and adaptive Gaussian comparison

The exact integrated-query memories called Section 13 in these fragments
are proved in [finite controls](finite_optimization_and_controls.md).
That chapter also contains the associated response and physical-control
fragments S, I, C and E. The local prefixes Q2–Q7 and G below refer only
to this comparison package. Fixed histories, actual adaptive transcripts,
finite feature clocks and growing but still clipped comparisons have
separately stated conclusions.

## Q2. Euler perturbations and slow-history compression


Consider the following completely specified triangular Gaussian perturbations,
with no mixture or complex parameter.

**Exact frozen-history lemma.** Let \(n,m,K\) be positive integers,
\(\eta,\sigma>0\), and \(T=K\eta\). Fix deterministic columns
\(\theta_l\in\mathbb R^n,\omega_l\in\mathbb R^m\) for
\(1\le l\le K\), and let \(\Gamma\in\mathbb R^{K\times K}\)
have independent standard real Gaussian entries. Put
\(\Theta=[\theta_1,\ldots,\theta_K]\),
\(\Omega=[\omega_1,\ldots,\omega_K]\), and take upper Cholesky
factors with positive diagonal:
\[
A_\theta^TA_\theta=\Theta^T\Theta+\sigma^2I,\qquad
A_\omega^TA_\omega=\Omega^T\Omega/m+\sigma^2I.
\]
Set \(t_i=(\Theta A_\theta^{-1})_i\) and
\(s_i=(\Omega A_\omega^{-1})_i/\sqrt m\), for column index \(i\).
Define the two triangular covariance-matching terms by
\[
g_l=\frac1{\sqrt m}\sum_{i\le l}t_i(\Gamma A_\omega)_{il},\qquad
k_l=\frac1{\sqrt m}\sum_{i<l}s_i(\Gamma^TA_\theta)_{il},
\]
where \(k_l\) is the perturbation of \(p_l/\sqrt m\).

Then the following identities and estimates hold. They evaluate the added
forcing, not the difference between two adaptive solutions.
\[
\mathbb E\left\|\eta\sum_{l=1}^K g_l\right\|^2
=\frac{\eta^2}{m}\sum_{i=1}^K\|t_i\|^2
\left[\frac1m\left\|\sum_{l=i}^K\omega_l\right\|^2
+\sigma^2(K-i+1)\right],                                      \tag{Q2.A}
\]
\[
\mathbb E\left\|\eta\sum_{l=1}^K k_l\right\|^2
=\frac{\eta^2}{m}\sum_{i=1}^{K-1}\|s_i\|^2
\left[\left\|\sum_{l=i+1}^K\theta_l\right\|^2
+\sigma^2(K-i)\right].                                       \tag{Q2.B}
\]
**Proof of the identities.** Group each independent \(\Gamma_{ij}\) in (Q2.A):
its coefficient is \(\eta t_i\sum_{l\ge i}(A_\omega)_{jl}/\sqrt m\).
Summing over \(j\) produces the suffix quadratic form of
\(A_\omega^TA_\omega\). For (Q2.B), the coefficient of
\(\Gamma_{ji}\) is
\(\eta s_i\sum_{l>i}(A_\theta)_{jl}/\sqrt m\), giving the
strict suffix and (Q2.B). Cross terms between distinct Gaussian entries
have zero expectation. The strict inequality in (Q2.B) is essential.

For repeated queries \(\theta_l=\theta,\omega_l=\omega\), put
\(a=\|\theta\|>0,b=\|\omega\|/\sqrt m>0\). The regularized upper
Cholesky factor of \(a^2\mathbf1\mathbf1^T+\sigma^2I\) satisfies
\[
(A_a)_{ii}=\sigma\sqrt{\frac{\sigma^2+ia^2}{\sigma^2+(i-1)a^2}},
\quad
(A_a)_{ij}=\frac{a^2\sigma}
 {\sqrt{(\sigma^2+(i-1)a^2)(\sigma^2+ia^2)}}\quad(i<j).
\]
Consequently \(t_i=\theta d_i(a)\), where
\[
d_i(a)=\frac{\sigma}
 {\sqrt{(\sigma^2+(i-1)a^2)(\sigma^2+ia^2)}},\qquad
\sum_{i=1}^l d_i(a)^2=\frac{l}{\sigma^2+la^2}.
\]
Substitution gives
\[
\mathbb E\left\|\eta\sum_lg_l\right\|^2
=\frac{a^2\eta^2}{m}\sum_{i=1}^Kd_i(a)^2
 [b^2(K-i+1)^2+\sigma^2(K-i+1)]
\le\frac{b^2T^2+\sigma^2T\eta}{m}.                            \tag{Q2.C}
\]
The analogous bound for \(\eta\sum_lk_l\) is
\((a^2T^2+\sigma^2T\eta)/m\), using \(i<K\) and \(K-i\).
In the fixed-\(K\), \(\sigma\downarrow0\) limit,
\(g_l\to(\theta/a)(b/\sqrt m)\Gamma_{11}\) for every \(l\),
whereas \(k_1=0\) and
\(k_l\to(\omega/(b\sqrt m))(a/\sqrt m)\Gamma_{11}\) for \(l\ge2\).
The forcing is coherent in time: Euler integration yields \(T/\sqrt m\),
not a \(\sqrt K\) growth. Inequality (Q2.C) is already uniform in both
\(K\) and \(\sigma\), so this conclusion does not exchange limits.

More generally, with \(\|\omega_l\|/\sqrt m\le B\), (Q2.A) is bounded by
\[
\frac{T^2B^2+\sigma^2T\eta}{m}\,
r_{\rm eff}(\Theta,\sigma),\qquad
r_{\rm eff}=\operatorname{tr}\!\left[
\Theta^T\Theta(\Theta^T\Theta+\sigma^2I)^{-1}\right].           \tag{Q2.D}
\]
A deterministic finite-rank path has bounded effective rank, including
an affine slowly changing history. This follows because
\(\sum_i\|t_i\|^2=r_{\rm eff}\), by cyclicity of the trace and
\(A_\theta^{-1}A_\theta^{-T}=(\Theta^T\Theta+\sigma^2I)^{-1}\).
The reverse orientation has the analogous estimate with
\(r_{\rm eff}(\Omega/\sqrt m,\sigma)\) and
\(A=\max_l\|\theta_l\|\).

These estimates also give convergence in the supremum norm of the
integrated path, not merely convergence at its last time. Specifically,
\[
\mathbb E\max_{1\le j\le K}
 \left\|\eta\sum_{l=1}^j g_l\right\|^2
\le \frac{T^2(B^2+\sigma^2)}m\,r_{\rm eff}(\Theta,\sigma),      \tag{Q2.E}
\]
and the reverse orientation has bound
\(T^2(A^2+\sigma^2)r_{\rm eff}(\Omega/\sqrt m,\sigma)/m\).
Indeed, pathwise Cauchy–Schwarz bounds the maximum by
\(T\eta\sum_l\|g_l\|^2\), while Gaussian isometry gives
\(\mathbb E\|g_l\|^2=(\|\omega_l\|^2/m+\sigma^2)
 \sum_{i\le l}\|t_i\|^2/m\).

The unintegrated frozen queries also admit a uniform maximum bound:
\[
\mathbb E\max_{1\le l\le K}\|g_l\|^2
\le\frac{4(B^2+\sigma^2)}m\,
 r_{\rm eff}(\Theta,\sigma)\log(2K),                           \tag{Q2.F}
\]
with the analogous reverse-orientation estimate. To verify this without
any independence between times, let \(Z_l\) be centered Gaussian
vectors with \(\mathbb E\|Z_l\|^2\le v^2\). For \(v>0\), the
covariance eigenvalues \(\lambda_j\) are at most \(v^2\), and
\[
\log\mathbb E e^{\|Z_l\|^2/(4v^2)}
=-\tfrac12\sum_j\log(1-\lambda_j/(2v^2))\le\tfrac12.
\]
Here \(-\log(1-x)\le2x\) for \(0\le x\le1/2\) was used.
Jensen's inequality and \(\max_l e^{x_l}\le\sum_l e^{x_l}\)
give \(\mathbb E\max_l\|Z_l\|^2\le4v^2\log(2K)\).
The case \(v=0\) is immediate. Apply this with
\(v^2=(B^2+\sigma^2)r_{\rm eff}/m\), using the per-query identity
above. Thus (Q2.F) also includes arbitrarily correlated frozen query times.

**Slow-history bound, including integer choices.** Assume only the discrete
Lipschitz estimate
\(\|\theta_l-\theta_j\|\le M\eta|l-j|\). Then
\[
r_{\rm eff}\le r+\frac{KM^2T^2}{\sigma^2r^2}\quad(1\le r\le K).
\]
To prove this, partition the indices into the nonempty blocks
\(\lfloor(j-1)K/r\rfloor<l\le\lfloor jK/r\rfloor\),
\(1\le j\le r\), replacing each column by the first column of its
block. Each block spans at most \(\eta(\lceil K/r\rceil-1)\le T/r\)
in physical time. This rank-at-most-\(r\) matrix approximation therefore
has squared Frobenius error at most \(K(MT/r)^2\). The sum of squared
singular values after the first \(r\) is no larger than that error;
the first \(r\) terms of the effective rank are at most one each, and
the rest are at most their squared singular values divided by
\(\sigma^2\). This proves the estimate.

Set \(x=(KM^2T^2/\sigma^2)^{1/3}\) and choose
\(r=\min\{K,\max\{1,\lceil x\rceil\}\}\). If \(x\le K\),
the estimate is at most \(1+2x\); if \(x>K\), use
\(r_{\rm eff}\le K\) directly. Thus
\[
r_{\rm eff}\le\min\{K,1+2(KM^2T^2/\sigma^2)^{1/3}\}.
\]
For \(K=O(m^2)\), uniformly bounded \(M,T\), and
\(\sigma\gg m^{-1/2}\), this proves \(r_{\rm eff}/m\to0\).
Choosing additionally \(\sigma\to0\), for example
\(\sigma=m^{-\beta}\), \(0<\beta<1/2\), removes the added
regularization forcing below. The reverse orientation needs the same
Lipschitz control of \(\omega_l/\sqrt m\).

For the direct additive noises, introduce mutually independent
\(U_l\sim N(0,I_n)\) and \(V_l\sim N(0,I_m)\), \(1\le l\le K\),
independent across calls and also independent of \(\Gamma\) and the fixed
histories. In the two normalized output spaces define
\[
 u_l^{\rm add}=\sigma U_l/\sqrt m,\qquad
 v_l^{\rm add}=\sigma V_l/\sqrt m.
\]
The second is the raw reverse noise \(\sigma V_l\) divided by \(\sqrt m\),
just as in the definition of \(k_l\). Independence gives the exact
Euler-integrated mean-square norms
\[
 E\left\|\eta\sum_{l=1}^K u_l^{\rm add}\right\|^2
   =\sigma^2(n/m)T\eta,\qquad
 E\left\|\eta\sum_{l=1}^K v_l^{\rm add}\right\|^2
   =\sigma^2T\eta.
\]
Their partial sums are square-integrable vector martingales. Their expected
squared maxima are at most four times the displayed terminal moments.
Indeed the first-crossing inequality for the norm submartingale gives
\(\lambda\Pr\{M_*\ge\lambda\}\le
 E[\|M_K\|\mathbf1_{M_*\ge\lambda}]\). Integrating in \(\lambda\)
and applying Cauchy--Schwarz yields
\(EM_*^2\le2E[\|M_K\|M_*]\le2\|M_K\|_{L^2}\|M_*\|_{L^2}\),
which proves the factor four (or first truncate the maximum and then pass
to its limit).
The same Gaussian maximum argument bounds the expected squared maximum
of their unintegrated query values by
\(4\sigma^2(n/m)\log(2K)\) and \(4\sigma^2\log(2K)\).

Thus, for deterministic histories with uniformly bounded
\(A,B,T,n/m\) and both discrete Lipschitz constants,
\(K\asymp m^2\), and \(\sigma=m^{-1/4}\), each expected squared
supremum of the integrated covariance perturbation is \(O(m^{-1/6})\).
Each additive-noise bound is \(O(m^{-5/2})\). Both orientations of the
full frozen primitive consequently vanish in \(L^2\) of the supremum
norm. This is a consequence of (Q2.E), without a union bound or logarithmic
loss; it is not a statement about the unfrozen dynamics.
Furthermore, (Q2.F) gives expected squared raw-query maxima
\(O(m^{-1/6}\log m)\), and the additive terms contribute
\(O(m^{-1/2}\log m)\). Hence the unintegrated frozen perturbations
also vanish uniformly over the mesh.

The implication is scoped. Simple deterministic histories resolve the
raw Gaussian-matrix-size concern, even with \(K\asymp m^2\).
However, in the actual comparison dynamics the Cholesky factors and
queries depend on \(\Gamma\); conditioning on those histories does not
preserve the independent Gaussian law used in (Q2.A)–(Q2.B) or (Q2.F). The actual
preactivation/backprop perturbations enter nonlinear queries before their
effect reaches an Euler update. An actual causal covariance estimate and
propagation bound are still required. The canonical middle multiplier
\(\operatorname{diag}(\phi''(z)b)\) is one unresolved propagation term;
this calculation does not show it is the only remaining obligation.

### Which actual network histories satisfy the temporal premise?

This section concerns the canonical finite three-hidden-layer flow in
feature time \(s\), not an extra claim about the perturbed comparison
process. All hidden vectors and the stored readout \(W^{(4)}\) have
length \(n\), and \(W^{(2)},W^{(3)}\) are \(n\) by \(n\). Write
\[
h^{(\ell)}=\phi(z^{(\ell)}),\quad
z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},\quad
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),
\]
\[
q^{(2)}=(W^{(3)})^\top\delta^{(3)},\qquad
\delta^{(2)}=\phi'(z^{(2)})\odot q^{(2)},\qquad
\phi(z)=\arctan z.
\]
Here \(q^{(2)}\) names the repeatedly used ungated backward result.
One can instead use common \(C^1\) clipping
\(\delta^{(2)}=\phi'(z^{(2)})\odot\tau_R(q^{(2)})\), with
\(|\tau_R(a)|\le |a|\), \(|\tau_R(a)|\le2R\), and
\(|\tau_R'(a)|\le1\).
The feature-time equations, with or without this clipping, are
\[
(z^{(1)})'=\phi'(z^{(1)})\odot(W^{(2)})^\top\delta^{(2)},\quad
(W^{(2)})'=\frac{\delta^{(2)}(h^{(1)})^\top}{n},\quad
(W^{(3)})'=\frac{\delta^{(3)}(h^{(2)})^\top}{n},\quad
(W^{(4)})'=h^{(3)}.
\]
Assume on \(0\le s\le S\) that the two matrix operator norms and
\(\|W^{(4)}\|_\infty\) are at most \(B_S\), independently of \(n,R\).
These are the already available primal bounds; the following implication
can also be read simply as a deterministic statement on that event.
Throughout this section \(C_S\) depends only on \(S,B_S\) and arctangent.

Because \(h^{(\ell)},\phi'\), and \(\phi''\) are bounded,
\(\|\delta^{(3)}\|_2/\sqrt n\), \(\|q^{(2)}\|_2/\sqrt n\), and
\(\|\delta^{(2)}\|_2/\sqrt n\) are bounded by \(C_S\).
Differentiating the actual forward equations gives
\[
(h^{(1)})'=\phi'(z^{(1)})^2\odot(W^{(2)})^\top\delta^{(2)},
\]
\[
(z^{(2)})'
=\frac{\|h^{(1)}\|_2^2}{n}\delta^{(2)}
 +W^{(2)}\!\left[
   \phi'(z^{(1)})^2\odot(W^{(2)})^\top\delta^{(2)}
 \right],
\]
\[
(h^{(2)})'=\phi'(z^{(2)})\odot(z^{(2)})',\qquad
(z^{(3)})'=\frac{\|h^{(2)}\|_2^2}{n}\delta^{(3)}
 +W^{(3)}(h^{(2)})',
\]
\[
(\delta^{(3)})'
=h^{(3)}\odot\phi'(z^{(3)})
 +W^{(4)}\odot\phi''(z^{(3)})\odot(z^{(3)})'.
\]
Every derivative displayed has Euclidean norm divided by \(\sqrt n\)
at most \(C_S\). Therefore \(h^{(1)}/\sqrt n\),
\(h^{(2)}/\sqrt n\), and \(\delta^{(3)}/\sqrt n\) have the
uniform time-Lipschitz property used in the frozen-history lemma.

This also yields an exact distinction for the lower backward query:
\[
(q^{(2)})'
=h^{(2)}\frac{\|\delta^{(3)}\|_2^2}{n}
 +(W^{(3)})^\top(\delta^{(3)})',
\]
so \(\|(q^{(2)})'\|_2/\sqrt n\le C_S\). In the uncut flow,
\[
(\delta^{(2)})'
=\phi''(z^{(2)})\odot(z^{(2)})'\odot q^{(2)}
 +\phi'(z^{(2)})\odot(q^{(2)})'.
\]
Cauchy--Schwarz gives
\[
\frac1n\sum_i|(\delta_i^{(2)})'|
\le \|\phi''\|_\infty
 \frac{\|(z^{(2)})'\|_2\|q^{(2)}\|_2}{n}
 +\frac{\|(q^{(2)})'\|_2}{\sqrt n}\le C_S.
\]
It does not supply a uniform Euclidean derivative bound for the product
\((z^{(2)})'\odot q^{(2)}\). For the clipped flow the same product
contains \(\tau_R(q^{(2)})\), and direct differentiation instead gives
\(\|(\delta^{(2)})'\|_2/\sqrt n\le C_S(1+R)\).
Thus all required lower-matrix frozen histories are time-Lipschitz for
fixed \(R\), but this argument is not uniform as \(R\) grows.

The scaling into the comparison lemma is explicit. For the top matrix
use \(m=n\), \(G=\sqrt n\,W_0^{(3)}\),
\(\theta_l=\delta_l^{(3)}/\sqrt n\), and \(\omega_l=h_l^{(2)}\).
Then its initial-matrix responses are
\[
G\omega_l/n=W_0^{(3)}h_l^{(2)}/\sqrt n,\qquad
G^\top\theta_l=(W_0^{(3)})^\top\delta_l^{(3)}.
\]
The lower matrix uses \(G=\sqrt n\,W_0^{(2)}\),
\(\theta_l=\delta_l^{(2)}/\sqrt n\), and \(\omega_l=h_l^{(1)}\).
The trained-matrix corrections remain present in the histories; they
are not being identified with these initialization-only responses.

Freeze an unperturbed flow path and sample the auxiliary \(\Gamma,U,V\)
independently of its initialization. Conditional on that path, the
frozen-history lemma applies. The top-matrix temporal constants just
proved are uniform in \(R\), while the lower-matrix backward constant
above is not. On any fixed primal-bounded event the resulting conditional
estimates have uniform constants. This is a forcing estimate along the
frozen path, not along the solution after adding that forcing.
Nothing here permits conditioning on a \(\Gamma\)-dependent perturbed
trajectory, removing clipping, or concluding unique autonomous restart.


## Q3. A contained rectangular martingale bound

Let \((Y_k)_{k=0}^J\) be a real \(d_1\)-by-\(d_2\) matrix
martingale, \(Y_0=0\), for a filtration \((\mathcal F_k)\). Write
\(X_k=Y_k-Y_{k-1}\). Suppose almost surely, for deterministic \(c,v\ge0\),
\[
 \|X_k\|_{op}\le c,\qquad
 \sum_{i\le k}\mathbb E_{i-1}X_iX_i^T\preceq vI_{d_1},\qquad
 \sum_{i\le k}\mathbb E_{i-1}X_i^TX_i\preceq vI_{d_2}
 \quad(0\le k\le J).
\]
Here \(\mathbb E_{i-1}\) denotes conditional expectation. Then for \(x>0\),
\[
 \mathbb P\{\max_{k\le J}\|Y_k\|_{op}\ge x\}
 \le(d_1+d_2)\exp\!\left(-\frac{x^2}{2(v+cx/3)}\right).
 \tag{Q3.1}
\]
If the denominator vanishes the probability is zero. This is the finite-horizon
rectangular Freedman inequality. The full proof, including the matrix
trace-concavity step, follows. The statement agrees with
[Tropp, Corollary 1.3](https://tropp.caltech.edu/papers/Tro11-Freedmans-Inequality.pdf).

**Inverse Jensen and logarithms.** For positive definite self-adjoint operators
\(T_i\) on a finite-dimensional Hilbert space and linear maps \(U_i\) satisfying
\(\sum_iU_i^*U_i=I\), the block matrix
\[
 \begin{pmatrix}T_i&I\\I&T_i^{-1}\end{pmatrix}\succeq0
\]
is positive by completing a square. Sandwich by
\(\operatorname{diag}(U_i,U_i)\), sum, and take the Schur complement to obtain
\[
 \left(\sum_iU_i^*T_iU_i\right)^{-1}
 \preceq\sum_iU_i^*T_i^{-1}U_i.
\]
Apply this to \(T_i+tI\) and integrate the scalar spectral identity
\[
 -\log T=\int_0^\infty[(T+tI)^{-1}-(1+t)^{-1}I],dt.
\]
It gives
\[
 -\log\left(\sum_iU_i^*T_iU_i\right)
 \preceq\sum_iU_i^*(-\log T_i)U_i.                 \tag{Q3.2}
\]
All integrals converge in operator norm in finite dimension. The same integral
and the inverse-order implication \(A\preceq B\Rightarrow B^{-1}\preceq A^{-1}\)
prove that the logarithm preserves positive-definite order. Inverse order
itself follows by congruence with \(A^{-1/2}\) and diagonalization.

**Joint convexity of matrix relative entropy.** For positive definite matrices,
put \(D_0(A,B)=\operatorname{tr}[A(\log A-\log B)]\). Given positive weights
\(p_i\) summing to one, set \(A=\sum_ip_iA_i\) and \(B=\sum_ip_iB_i\).
On the Hilbert space of matrices with inner product
\(\langle X,Y\rangle=\operatorname{tr}(X^*Y)\), define
\[
 T_iX=B_iXA_i^{-1},\qquad
 U_iX=\sqrt{p_i}\,XA^{-1/2}A_i^{1/2}.
\]
Left and right multiplication here commute; \(T_i\) is positive definite
and self-adjoint on this Hilbert space. Direct multiplication gives
\[
 \sum_iU_i^*U_i=I,\qquad
 \sum_iU_i^*T_iU_i:X\mapsto BXA^{-1},\qquad
 U_iA^{1/2}=\sqrt{p_i}A_i^{1/2}.
\]
The logarithm of the operator \(X\mapsto BXA^{-1}\) is
\(X\mapsto(\log B)X-X\log A\), as is verified on the rank-one basis formed
from eigenvectors of \(A\) and \(B\). Pairing (Q3.2) with \(A^{1/2}\) therefore
proves
\[
 D_0(A,B)\le\sum_ip_iD_0(A_i,B_i).                \tag{Q3.3}
\]
This contains the full joint-convexity argument needed here.

The modified entropy
\(D(A,B)=D_0(A,B)-\operatorname{tr}A+\operatorname{tr}B\) is nonnegative.
Indeed, diagonalize \(A\) and \(B\) with eigenvalues \(a_i,b_j>0\); the squared
overlaps \(w_{ij}\) of their orthonormal eigenvectors have all row and column
sums one. Then
\[
 D(A,B)=\sum_{i,j}w_{ij}
 [a_i\log(a_i/b_j)-a_i+b_j]\ge0,
\]
by \(u\log u-u+1\ge0\). Equality holds at \(A=B\).
Consequently for each self-adjoint \(H\),
\[
 \operatorname{tr}e^H
 =\max_{X\succ0}\operatorname{tr}(XH-X\log X+X),
\]
with maximizer \(X=e^H\). Replacing \(H\) by \(H+\log A\) expresses
\(\operatorname{tr}\exp(H+\log A)\) as the maximum over \(X\succ0\) of
\(\operatorname{tr}(XH)-D_0(X,A)+\operatorname{tr}X\). This expression is jointly
concave in \((X,A)\) by (Q3.3). To verify concavity after maximizing, take the
maximizers at two arguments and evaluate at their convex combination; joint
concavity supplies the required lower bound. Thus
\[
 A\longmapsto\operatorname{tr}\exp(H+\log A)
 \quad\hbox{is concave on }A\succ0.              \tag{Q3.4}
\]
This entropy-to-trace step follows the variational argument in
[Tropp, Theorem 1 and Lemma 6](https://tropp.caltech.edu/papers/Tro12-Joint-Convexity.pdf);
(Q3.2)–(Q3.3) provide its joint-convexity dependency explicitly.

**Conditional exponential estimate.** First consider self-adjoint increments
\(X_k\) of size \(d\), with \(\|X_k\|_{op}\le c\) and
\(\mathbb E_{k-1}X_k=0\). For \(0<\theta c<3\), put
\(g=\theta^2/[2(1-\theta c/3)]\). The power series and
\(j!\ge2\,3^{j-2}\) for \(j\ge2\) imply, for \(|u|\le c\),
\(e^{\theta u}\le1+\theta u+gu^2\). Spectral calculus and conditional
expectation give, with \(V_k=\mathbb E_{k-1}X_k^2\),
\[
 \log\mathbb E_{k-1}e^{\theta X_k}
 \preceq\log(I+gV_k)\preceq gV_k.                \tag{Q3.5}
\]
The first inequality uses the order preservation of log just proved; the
second uses \(\log(1+u)\le u\) on the eigenvalues of \(gV_k\).
For self-adjoint \(A\preceq B\), the min–max characterization orders every
eigenvalue, so \(\operatorname{tr}e^A\le\operatorname{tr}e^B\).

Set \(W_k=\sum_{i\le k}V_i\). Conditional Jensen using (Q3.4), with the
predictable matrix \(H=\theta Y_{k-1}-gW_k\), gives
\[
 \begin{split}
 \mathbb E_{k-1}\operatorname{tr}e^{\theta Y_k-gW_k}
 &\le\operatorname{tr}\exp\left(H+
              \log\mathbb E_{k-1}e^{\theta X_k}\right)\\
 &\le\operatorname{tr}e^{\theta Y_{k-1}-gW_{k-1}}.
 \end{split}                                                   \tag{Q3.6}
\]
Jensen is legitimate for these bounded positive definite random matrices;
approximate them by simple matrices in their compact spectral range and use
continuity. Hence the displayed nonnegative trace process is a supermartingale
starting at \(d\).

Stop at the first \(k\le J\) with \(\lambda_{max}(Y_k)\ge x\), or at \(J\)
if there is no such time. Conditional induction for this bounded stopping time
bounds its expected trace by \(d\). If \(W_k\preceq vI\), the trace on the
crossing event is at least \(\exp(\theta x-gv)\), because
\(\lambda_{max}(\theta Y_k-gW_k)\ge\theta x-gv\). Thus the crossing probability
is at most \(d\exp(-\theta x+gv)\). For \(v>0\) take
\(\theta=x/(v+cx/3)\), giving \(d\exp[-x^2/(2(v+cx/3))]\).
If \(v=0\), every increment has zero conditional squared norm and is zero
almost surely, so the assertion follows directly. The case \(c=0\) is the
same; otherwise the chosen \(\theta\) lies in the required range.

Finally replace each rectangular increment by its self-adjoint dilation
\[
 \mathscr D(X_k)=\begin{pmatrix}0&X_k\\X_k^T&0\end{pmatrix}.
\]
Its norm is \(\|X_k\|_{op}\), its squared conditional variation has exactly
the two stated rectangular variation blocks, and
\(\lambda_{max}(\mathscr D(Y_k))=\|Y_k\|_{op}\). Taking \(d=d_1+d_2\)
proves (Q3.1) with all dependencies contained.



## Q4. Adaptive Gram martingale

The hypotheses here permit adaptive query vectors. Fragment Q5 checks them for
each of its two interacting initial matrices and proves the rank premise.

### 1. Causal setup and exact identities

Fix \(n,m,K\ge1\) and \(\sigma>0\). Let \(\Gamma\in
\mathbb R^{K\times K}\) have independent standard Gaussian entries.
Let \(\mathcal H\) contain all other random arrays and seeds, jointly
independent of \(\Gamma\). In the perturbed-original process these
include the original Gaussian matrix and its direct-noise arrays;
revealing their entire arrays initially does not
reveal any entry of \(\Gamma\).

Use finite-valued measurable causal query maps in the order
\(\theta_l\to p_l\to\omega_l\to q_l\). Define
\[
\mathcal F_l=\mathcal H\vee\sigma(\Gamma_{ij}:i,j\le l),\qquad
\mathcal F_{l-1/2}=\mathcal F_{l-1}\vee
 \sigma(\Gamma_{lj}:j<l).
\]
Here \(\theta_l\in\mathbb R^n\) is \(\mathcal F_{l-1}\)-measurable,
\(p_l,\omega_l\in\mathbb R^m\) are
\(\mathcal F_{l-1/2}\)-measurable, and \(q_l\) is
\(\mathcal F_l\)-measurable. The assertions are the causal hypothesis on the queries, satisfied by the
explicit oracle in fragment Q5: its reverse strict-triangular term uses the fresh row
\(\Gamma_{lj},j<l\); its forward triangular term subsequently uses
the fresh column \(\Gamma_{il},i\le l\). The other terms are already
measurable from the queries and \(\mathcal H\).

For each leading history take the positive-diagonal upper Cholesky
factors
\[
A_\theta^TA_\theta=\Theta^T\Theta+\sigma^2I,\qquad
A_\omega^TA_\omega=\Omega^T\Omega/m+\sigma^2I.
\]
The leading blocks of these factors and their inverses agree between
prefixes. Thus the columns
\[
t_i=(\Theta A_\theta^{-1})_i\in\mathbb R^n,\qquad
s_i=(\Omega A_\omega^{-1})_i/\sqrt m\in\mathbb R^m
\]
never change when later queries arrive. In particular \(t_l\) is
known before the fresh row and \(s_l\) before the fresh column.
An arbitrary horizon-dependent Cholesky sign convention is not allowed.

Put
\[
\mathsf T_l=\sum_{i\le l}t_it_i^T\preceq I_n,\qquad
\mathsf S_l=\sum_{i\le l}s_is_i^T\preceq I_m,
\quad \rho_{\theta,l}=\operatorname{tr}\mathsf T_l,
\quad \rho_{\omega,l}=\operatorname{tr}\mathsf S_l.              \tag{Q4.1}
\]
Indeed \(\mathsf T_l=\Theta_l(\Theta_l^T\Theta_l+
\sigma^2I)^{-1}\Theta_l^T\), and the singular-value decomposition
gives eigenvalues \(d_j^2/(d_j^2+\sigma^2)\le1\); the same
calculation applies to \(\Omega_l/\sqrt m\). These traces are the
regularized effective ranks. They increase with the prefix, and
\(\|t_i\|,\|s_i\|\le1\).

Define the rectangular matrices
\[
B_{l-1/2}=\sum_{i\le l,j<l}t_i\Gamma_{ij}s_j^T,\qquad
B_l=\sum_{i,j\le l}t_i\Gamma_{ij}s_j^T,\qquad B_0=0.
\]
Their half-step increments are
\[
B_{l-1/2}-B_{l-1}=t_l a_l^T,
\quad a_l=\sum_{j<l}s_j\Gamma_{lj},\qquad
B_l-B_{l-1/2}=b_l s_l^T,
\quad b_l=\sum_{i\le l}t_i\Gamma_{il}.                        \tag{Q4.2}
\]
The first fresh vector is conditionally \(N(0,\mathsf S_{l-1})\),
and the second is conditionally \(N(0,\mathsf T_l)\), at their
respective preceding half-steps. Hence \(B\) is a rectangular matrix
martingale. Its increments have finite moments at every fixed finite
\(n,m,K\), by (Q4.1) and the Gaussian moments. No bound on the raw
query norms is needed for this assertion.

At each prefix define the triangular perturbations
\[
 g_l=\frac1{\sqrt m}\sum_{i\le l}t_i(\Gamma A_\omega)_{il},\qquad
 k_l=\frac1{\sqrt m}\sum_{i<l}s_i(\Gamma^TA_\theta)_{il}.
\]
All products use the leading \(l\)-by-\(l\) matrices. These formulas are the
adaptive versions of Q2; \(k_l\) uses a strict reverse triangle.
The exact decompositions are
\[
g_l=\frac{B_l\omega_l}{m}
 +\frac{\sigma^2}{\sqrt m\,A_{\omega,ll}}b_l,\qquad
k_l=\frac{B_{l-1/2}^T\theta_l}{\sqrt m}
 +\frac{\sigma^2}{\sqrt m\,A_{\theta,ll}}a_l.                  \tag{Q4.3}
\]
For \(j\le l\), the Gram identity gives
\[
\frac{s_j^T\omega_l}{\sqrt m}
=\big[A_\omega-\sigma^2A_\omega^{-T}\big]_{jl},
\]
so \(A_{\omega,jl}=s_j^T\omega_l/\sqrt m\) for \(j<l\),
and the diagonal has the additional \(\sigma^2/A_{\omega,ll}\).
The same identity holds for \(A_\theta\). Substitution into the two
triangular terms just displayed proves (Q4.3), including the strict reverse sum.
Furthermore, each diagonal obeys \(A_{ll}\ge\sigma\): its squared
Schur complement is
\(\sigma^2+x_l^T[I-X_{l-1}(X_{l-1}^TX_{l-1}+
\sigma^2I)^{-1}X_{l-1}^T]x_l\ge\sigma^2\).
Thus both residual coefficients in (Q4.3), apart from \(m^{-1/2}\),
are at most \(\sigma\).

### 2. Quantitative adaptive bound

Take deterministic \(R_\theta,R_\omega\ge0\),
\(r=\max(R_\theta,R_\omega)>0\), and \(0<\alpha<1\). Set
\[
E_R=\{\rho_{\theta,K}\le R_\theta,
       \rho_{\omega,K}\le R_\omega\},\quad
u=\log(4K/\alpha),\quad c=\sqrt{2r+4u},
\quad v=\log(2(n+m)/\alpha),
\quad L=2\sqrt{rv}+\tfrac23cv.                               \tag{Q4.4}
\]
Then
\[
\mathbb P\left(E_R\cap
 \left\{\max_h\|B_h\|_{\rm op}>L
 \ \text{or}\ \max_l(\|a_l\|\vee\|b_l\|)>c\right\}\right)
\le\alpha,                                                  \tag{Q4.5}
\]
where \(h\) runs over all half and full steps through \(K\).
If additionally
\(\max_l\|\theta_l\|\le A\),
\(\max_l\|\omega_l\|/\sqrt m\le C\), then outside the same
exceptional event, on \(E_R\),
\[
\max_l\|g_l\|\le\frac{CL+\sigma c}{\sqrt m},\qquad
\max_l\|k_l\|\le\frac{AL+\sigma c}{\sqrt m}.                 \tag{Q4.6}
\]
These norm bounds may instead be imposed on an event and intersected
with \(E_R\). If \(r=0\), both Gram contractions are zero on
\(E_R\), and the claimed perturbations are zero there.

### Proof, including localization and truncation

First stop accepting increments permanently before a rank threshold
would be exceeded. Before row \(l\), both \(\rho_{\theta,l}\)
and \(\rho_{\omega,l-1}\) are known; accept the row only while they
are within their thresholds. Before column \(l\),
\(\rho_{\omega,l}\) is also known; accept the column only if its
threshold has not been exceeded. These acceptance indicators are
predictable at their respective half-steps. The accepted process agrees
with \(B\) on \(E_R\). Its coefficients still refer to the original
adaptive histories; this construction does not alter the query dynamics.

For an accepted untruncated row increment \(X=t_la_l^T\), its two
conditional second-moment matrices are
\[
\mathbb E[XX^T\mid\mathcal F_{l-1}]
 =\rho_{\omega,l-1}t_lt_l^T,\qquad
\mathbb E[X^TX\mid\mathcal F_{l-1}]
 =\|t_l\|^2\mathsf S_{l-1}.
\]
For an accepted column increment \(Y=b_ls_l^T\), they are
\[
\mathbb E[YY^T\mid\mathcal F_{l-1/2}]
 =\|s_l\|^2\mathsf T_l,\qquad
\mathbb E[Y^TY\mid\mathcal F_{l-1/2}]
 =\rho_{\theta,l}s_ls_l^T.
\]
Summing along each realized path, (Q4.1) and the threshold rule imply
\[
W_{\rm left}\preceq
 R_\omega\sum_{\rm accepted\ rows}t_lt_l^T
 +\sum_{\rm accepted\ columns}\|s_l\|^2I_n
 \preceq2R_\omega I_n,
\]
\[
W_{\rm right}\preceq
 \sum_{\rm accepted\ rows}\|t_l\|^2I_m
 +R_\theta\sum_{\rm accepted\ columns}s_ls_l^T
 \preceq2R_\theta I_m.                                      \tag{Q4.7}
\]
In particular both predictable quadratic variations have norm at most
\(2r\). The unequal left/right constants matter: no factor \(K\)
has been introduced.

To bound increments without an unjustified Gaussian boundedness
assumption, multiply each accepted row increment by
\(\mathbf1_{\{\|a_l\|\le c\}}\), and each accepted column
increment by \(\mathbf1_{\{\|b_l\|\le c\}}\). Conditional
Gaussian symmetry makes the truncated increments centered. Their
conditional second moments are bounded in positive-semidefinite order
by the untruncated ones, so (Q4.7) remains valid. Their operator norms are
at most \(c\), since \(\|t_l\|,\|s_l\|\le1\).

At every accepted half-step the fresh Gaussian vector \(Z\) has
covariance at most the identity and trace at most \(r\). Its covariance
eigenvalues \(\lambda_j\in[0,1]\) give
\[
\mathbb E[e^{\|Z\|^2/4}\mid\text{past}]
=\prod_j(1-\lambda_j/2)^{-1/2}\le e^{r/2},\qquad
\mathbb P(\|Z\|>c\mid\text{past})\le e^{-u}.
\]
The product estimate uses \(-\log(1-x)\le2x\) for \(x\le1/2\).
A union bound over at most \(2K\) accepted half-steps costs at most
\(2Ke^{-u}=\alpha/2\). On its complement and \(E_R\), no
truncation or stopping occurred, and the truncated martingale agrees
with \(B\) at every half-step; all residual vectors have norm at most
\(c\).

Apply the rectangular martingale bound proved in fragment Q3.
For an \(n\times m\) matrix martingale with increment norms at most
\(c\) and both predictable quadratic variations at most \(2r\),
that bound controls the probability its norm ever exceeds \(x\) by
\[
(n+m)\exp\left[-\frac{x^2}{2(2r+cx/3)}\right].
\]
The truncated process starts at zero, is adapted and centered, has bounded
increments and thus is integrable, and satisfies (Q4.7); these verify every
hypothesis. For \(x=L\),
\(L^2\ge2v(2r+cL/3)\), so the bound is at most \(\alpha/2\).
Combining it with the truncation failure probability proves (Q4.5).
Finally (Q4.3), \(A_{ll}\ge\sigma\), and the query norm bounds prove
(Q4.6). None of these steps conditions on adaptive histories as though
their Gaussian law were unchanged.



## Q5. The causal filtered recursion and its own ranks

This is a finite auxiliary recursion, with canonical Gaussian non-matrix and
initial-matrix seeds plus independent oracle noise. Its slow histories are
produced by its own perturbed dynamics. The proof uses Q4 twice; no frozen-query
Gaussian estimate is applied to an adaptive history.

Fix a feature-time horizon \(S>0\), and, for integers \(n\ge2\), put
\[
 \eta=n^{-2},\qquad N=\lceil Sn^2\rceil,\qquad
 T=N\eta\le S+1,\qquad K=N+1,
 \qquad \sigma=n^{-1/4},\qquad \gamma=1/8,\qquad \epsilon=n^{-\gamma},
 \qquad \ell_n=\log(e+n).
 \tag{Q5.1}
\]
Here \(N\) counts updates and \(K\) counts query pairs **per matrix**, including
one warmup. \(T\) is a feature-time horizon, not an established physical-time
horizon. Fix one deterministic scalar map \(\tau:\mathbb R\to\mathbb R\)
satisfying
\[
 |\tau(u)|\le |u|,\qquad |\tau(u)-\tau(v)|\le |u-v|.
 \tag{Q5.2}
\]
Apply it coordinatewise. Identity and any fixed clipping map satisfying
(Q5.2) are allowed. The constants below depend only on \(S\), not on the
clipping level or on which such map was fixed. The probability assertion
is for each fixed map; it does not assert a single event valid
simultaneously for all maps. A deterministic choice of map at each width
also satisfies the same estimates.

All vector norms below are ordinary Euclidean norms, with each factor
\(1/\sqrt n\) displayed explicitly. For a history
matrix \(X\in\mathbb R^{n\times k}\), define
\[
 \rho(X)=\operatorname{tr}\!\left[
 XX^T(XX^T+\sigma^2I_n)^{-1}\right].
 \tag{Q5.3}
\]
This equals the effective-rank expression using \(X^TX\), including when
\(k>n\). The four histories will be the lower and upper reverse arguments
divided by \(\sqrt n\), and the lower and upper forward arguments divided
by \(\sqrt n\), including their warmups.

**Auxiliary theorem.** The recursion in Sections 1--2 is finite and
measurable almost surely for every finite \(n,N\). There are deterministic
constants \(C_S<\infty\) and events \(\mathcal E_n^\tau\) such that
\[
 \mathbb P(\mathcal E_n^\tau)
 \ge 1-4e^{-(8-2\log9)n}-2n e^{-n^2/2}-5n^{-2},
 \tag{Q5.4}
\]
and, on these events, every prefix of every one of the four actual
histories satisfies
\[
 \rho\le C_S n^{11/12}\ell_n^{4/3}.
 \tag{Q5.5}
\]
For both matrices and both orientations, including warmups, let \(e_l\)
be the raw perturbed output minus the exact initial-matrix action on
that same actual query argument. Then, on the same event,
\[
 \max_l \frac{\|e_l\|_2}{\sqrt n}
 \le C_S n^{-1/24}\ell_n^{8/3}+C_S n^{-1/4}.
 \tag{Q5.6}
\]
Both terms tend to zero. This comparison is on the auxiliary algorithm's
own arguments, not on arguments imported from an unperturbed trajectory.

The proof first uses the universal ceiling \(\rho\le n\) in the adaptive
theorem. This gives logarithmic state bounds without assuming slow
histories. Relaxation then bounds increments of the actual histories.
A deterministic column approximation proves (Q5.5), after which a second,
localized application of the adaptive theorem proves (Q5.6). Neither pass
conditions on the realized histories as if their Gaussian law were
unchanged.

### 1. Exact oracle, canonical seeds, and causal warmup

Let \(\phi(z)=\arctan z\), \(F(z)=z+z^3/3\), and
\(\psi=\phi\circ F^{-1}\). These act coordinatewise. \(F\) is a
bijection of \(\mathbb R\), since \(F'(z)=1+z^2\ge1\) and its limits
at the two ends of the line are infinite with opposite signs. In particular,
\[
 |\phi|\le c_\phi:=\pi/2,\quad 0<\phi'\le1,\quad
 \|\phi''\|_\infty\le2,\quad
 \psi'(x)=\frac{1}{(1+(F^{-1}x)^2)^2}\le1.
 \tag{Q5.7}
\]

Sample the independent canonical initial blocks
\[
 z^{(1)}_{0,i}\sim N(0,1),\quad
 W^{(2)}_{0,ij},W^{(3)}_{0,ij}\sim N(0,1/n),\quad
 W^{(4)}_{0,i}\sim N(0,n^{-2}).
 \tag{Q5.8}
\]
Set \(x^{(1)}_0=F(z^{(1)}_0)\) and \(h^{(1)}_0=\phi(z^{(1)}_0)\).
The notation \(W^{(4)}_0\) will also denote the initial readout register.
For each \(b\in\{2,3\}\), set \(G^{(b)}=\sqrt n W^{(b)}_0\) and
sample independent arrays
\[
 \Gamma^{(b)}\in\mathbb R^{K\times K},\qquad
 U^{(b)}_l,V^{(b)}_l\in\mathbb R^n\quad(1\le l\le K),
 \tag{Q5.9}
\]
all with independent standard Gaussian entries. These two collections
are mutually independent and independent of (Q5.8).

Here is the exact paired oracle for either matrix; suppress \(b\)
temporarily. At call \(l\), the raw reverse argument is \(v_l\in\mathbb R^n\)
and the raw forward argument is \(h_l\in\mathbb R^n\). Its normalized variables
are
\[
 \theta_l=v_l/\sqrt n,\qquad\omega_l=h_l,\qquad
 p_l^{\rm src}=G^T\theta_l=W_0^Tv_l,\qquad
 q_l^{\rm src}=G\omega_l/n=W_0h_l/\sqrt n.
 \tag{Q5.10}
\]
For each leading history \(\Theta_l=[\theta_1,\ldots,\theta_l]\),
\(\Omega_l=[\omega_1,\ldots,\omega_l]\), take the positive-diagonal
upper Cholesky factors
\[
 A_{\theta,l}^TA_{\theta,l}=\Theta_l^T\Theta_l+\sigma^2I_l,
 \qquad
 A_{\omega,l}^TA_{\omega,l}=\Omega_l^T\Omega_l/n+\sigma^2I_l.
 \tag{Q5.11}
\]
Their leading blocks, including inverse leading blocks, agree as calls
are appended. Define the permanent columns
\[
 t_i=(\Theta_l A_{\theta,l}^{-1})_i,\qquad
 s_i=(\Omega_l A_{\omega,l}^{-1})_i/\sqrt n\quad(i\le l).
 \tag{Q5.12}
\]
The exact Gamma perturbations are
\[
 \begin{split}
 g_l&=\frac1{\sqrt n}\sum_{i\le l}
 t_i(\Gamma_{[l]\times[l]}A_{\omega,l})_{il},\\
 k_l&=\frac1{\sqrt n}\sum_{i<l}
 s_i(\Gamma_{[l]\times[l]}^T A_{\theta,l})_{il}.
 \end{split}
 \tag{Q5.13}
\]
In particular, the reverse sum is strict. Define the raw outputs, which
are the quantities actually used by the recursion, by
\[
 \begin{split}
 \mathcal R_l&=W_0^Tv_l+\sqrt n\,k_l+\sigma U_l,\\
 \mathcal F_l&=W_0h_l+\sqrt n\,g_l+\sigma V_l.
 \end{split}
 \tag{Q5.14}
\]
Thus the perturbed reverse output is \(\widehat p_l=\mathcal R_l\),
while its perturbed normalized forward output is
\(\widehat q_l=\mathcal F_l/\sqrt n=q_l^{\rm src}+g_l+\sigma V_l/\sqrt n\).
The raw query errors and their normalized sizes are consequently
\[
 e_l^{\rm rev}=\sqrt n\,k_l+\sigma U_l,\qquad
 e_l^{\rm for}=\sqrt n\,g_l+\sigma V_l,
 \tag{Q5.15}
\]
\[
 \frac{\|e_l^{\rm rev}\|_2}{\sqrt n}\le\|k_l\|_2+\sigma\frac{\|U_l\|_2}{\sqrt n},
 \qquad
 \frac{\|e_l^{\rm for}\|_2}{\sqrt n}\le\|g_l\|_2+\sigma\frac{\|V_l\|_2}{\sqrt n}.
 \tag{Q5.16}
\]
Both raw direct noises in (Q5.14) have coordinate variance \(\sigma^2\).
Their contributions to RMS errors are \(\sigma U_l/\sqrt n\) and
\(\sigma V_l/\sqrt n\). The Gaussian maximum bound is derived in Section 4.

Initialize the auxiliary registers
\[
 a^{(2)}_0=R^{(1)}_0=0,\qquad
 M^{(2)}_0=M^{(3)}_0=0,\qquad
 x^{(1)}_0=F(z^{(1)}_0),\qquad W^{(4)}_0\text{ as in (Q5.8)}.
 \tag{Q5.17}
\]
Here \(a^{(2)},R^{(1)},x^{(1)},W^{(4)},z^{(2)},z^{(3)}\) are vectors of
length \(n\), and \(M^{(2)},M^{(3)}\) are \(n\)-by-\(n\) matrices. The
preactivation registers \(z^{(2)}_0,z^{(3)}_0\) are obtained only by these
two warmup calls:

1. Lower call \(l=1\): use \(v^{(2)}_1=0\),
   \(h^{(2),\mathrm{query}}_1=h^{(1)}_0\), and set
   \(z^{(2)}_0=\mathcal F^{(2)}_1\).
2. Upper call \(l=1\): use \(v^{(3)}_1=0\),
   \(h^{(3),\mathrm{query}}_1=\phi(z^{(2)}_0)\), and set
   \(z^{(3)}_0=\mathcal F^{(3)}_1\).

Discard both warmup reverse outputs. For either warmup, \(\theta_1=0\)
implies \(t_1=0\), so (Q5.13) gives \(g_1=k_1=0\). The forward direct noise
does not vanish. In particular, the exact identities for these declared
oracle outputs are
\[
 z^{(2)}_0=W^{(2)}_0h^{(1)}_0+\sigma V^{(2)}_1,
 \qquad
 z^{(3)}_0=W^{(3)}_0\phi(z^{(2)}_0)+\sigma V^{(3)}_1.
 \tag{Q5.18}
\]
There are no other initial-matrix calls in initialization. Formula (Q5.18)
describes the two noisy calls; it is not an instruction to evaluate their
exact parts separately. The seeds have the canonical distribution (Q5.8),
but these warmup registers are not canonical exact network initialization.

### 2. All actual updates and their causal measurability

At each mesh state \(j=0,\ldots,N-1\), first form, entirely from that
pre-step state,
\[
 h^{(1)}_j=\psi(x^{(1)}_j),\qquad
 h^{(2)}_j=\phi(z^{(2)}_j),\qquad
 h^{(3)}_j=\phi(z^{(3)}_j),\qquad
 \delta^{(3)}_j=W^{(4)}_j\odot\phi'(z^{(3)}_j).
 \tag{Q5.19}
\]
At call index \(l=j+2\), use
\[
 \begin{array}{c|cc}
   &\theta_l&\omega_l\\\hline
 \text{lower }(b=2)&a^{(2)}_j/\sqrt n&h^{(1)}_j\\
 \text{upper }(b=3)&\delta^{(3)}_j/\sqrt n&h^{(2)}_j.
 \end{array}
 \tag{Q5.20}
\]
Execute the lower reverse/forward pair and then the upper reverse/forward
pair. Both arguments of both pairs have already been selected before
these outputs arrive. From the current upper reverse output form
\[
 q^{(2)}_j=\mathcal R^{(3)}_{j+2}
             +(M^{(3)}_j)^T\delta^{(3)}_j,
 \qquad
 \delta^{(2)}_j=\phi'(z^{(2)}_j)\odot\tau(q^{(2)}_j).
 \tag{Q5.21}
\]
Now update all registers simultaneously, using exactly the old factors
displayed on the right:
\[
 \begin{split}
 a^{(2)}_{j+1}&=a^{(2)}_j+\eta\delta^{(2)}_j,\\
 M^{(2)}_{j+1}&=M^{(2)}_j+
       \frac\eta n\delta^{(2)}_j(h^{(1)}_j)^T,\\
 M^{(3)}_{j+1}&=M^{(3)}_j+
       \frac\eta n\delta^{(3)}_j(h^{(2)}_j)^T,\\
 R^{(1)}_{j+1}&=R^{(1)}_j+\eta(M^{(2)}_j)^T\delta^{(2)}_j,\\
 W^{(4)}_{j+1}&=W^{(4)}_j+\eta h^{(3)}_j,\\
 x^{(1)}_{j+1}&=x^{(1)}_j+
    \frac\eta\epsilon
      [x^{(1)}_0+\mathcal R^{(2)}_{j+2}+R^{(1)}_j-x^{(1)}_j],\\
 z^{(2)}_{j+1}&=z^{(2)}_j+
    \frac\eta\epsilon
      [\mathcal F^{(2)}_{j+2}+M^{(2)}_j h^{(1)}_j-z^{(2)}_j],\\
 z^{(3)}_{j+1}&=z^{(3)}_j+
    \frac\eta\epsilon
      [\mathcal F^{(3)}_{j+2}+M^{(3)}_j h^{(2)}_j-z^{(3)}_j].
 \end{split}
 \tag{Q5.22}
\]
The memories retain every earlier increment. In particular, \(R^{(1)}\)
uses pre-step \(M^{(2)}_j\), not \(M^{(2)}_{j+1}\). The histories in the
theorem are the matrices \(\Theta^{(2)}_l,\Omega^{(2)}_l/\sqrt n,
\Theta^{(3)}_l,\Omega^{(3)}_l/\sqrt n\) actually generated by (Q5.17)--(Q5.22).

More explicitly, the finite-step memory identities are
\[
 \begin{split}
 M^{(2)}_j&=\frac\eta n\sum_{i<j}
                    \delta^{(2)}_i(h^{(1)}_i)^T,\\
 M^{(3)}_j&=\frac\eta n\sum_{i<j}
                    \delta^{(3)}_i(h^{(2)}_i)^T,\\
 R^{(1)}_j&=\eta\sum_{i<j}(M^{(2)}_i)^T\delta^{(2)}_i
       =\frac{\eta^2}{n}\sum_{0\le u<i<j}
           h^{(1)}_u(\delta^{(2)}_u)^T\delta^{(2)}_i\\
       &=\frac\eta n\sum_{u<j}h^{(1)}_u(\delta^{(2)}_u)^T
                         [a^{(2)}_j-a^{(2)}_{u+1}].
 \end{split}
 \tag{Q5.22a}
\]
The last identity uses
\(a^{(2)}_j-a^{(2)}_{u+1}=\eta\sum_{u<i<j}\delta^{(2)}_i\).
Thus \(R^{(1)}\) is the Euler, pre-step accumulated full rank memory;
at finite \(\eta\) it is not literally the continuous integral in the
integrated equations in Section 13 of the finite-controls chapter. The strict time triangle is part of the specified
Euler convention. No trained term or earlier memory update is dropped.

Finiteness and measurability do not require a probability estimate.
All Gaussian entries are finite almost surely. Every regularized Gram
matrix in (Q5.11) is positive definite with smallest eigenvalue at least
\(\sigma^2>0\). Positive-diagonal Cholesky factorization and inversion
are continuous on this domain: the recursive diagonal square roots have
positive arguments and their denominators do not vanish. Formula (Q5.13)
therefore gives finite measurable outputs at every finite prefix. The
inverse \(F^{-1}\), arctangent, and \(\tau\) are continuous; finite sums
and products in (Q5.22) preserve finiteness. Induction over the two warmups
and the \(N\) updates proves the claim. No uniform bound is needed to
perform this induction.

For completeness, the adaptive filtration applies separately to each
matrix despite their interaction. For matrix \(b\), let
\(\mathcal H^{(b)}\) contain all canonical initial blocks, all \(U,V\),
and the other matrix's whole Gamma array. These primitive arrays are
jointly independent of \(\Gamma^{(b)}\). Set
\[
 \mathscr F^{(b)}_l=\mathcal H^{(b)}\vee
  \sigma(\Gamma^{(b)}_{ij}:i,j\le l),\qquad
 \mathscr F^{(b)}_{l-1/2}=\mathscr F^{(b)}_{l-1}\vee
  \sigma(\Gamma^{(b)}_{lj}:j<l).
 \tag{Q5.23}
\]
In the warmup, the upper forward argument depends only on the lower
warmup output, which is \(\mathcal H^{(3)}\)-measurable. Its own reverse
argument is zero. At each later call \(l=j+2\), the state at \(j\) uses
only calls through \(l-1\) of both matrices. Inductively it is
\(\mathscr F^{(b)}_{l-1}\)-measurable for each \(b\); the other matrix's
past calculations are measurable functions of the own past prefix and
the arrays already in \(\mathcal H^{(b)}\).

Consequently \(\theta_l\) and \(\omega_l\) in (Q5.20) are known before
the own fresh row. The reverse formula (Q5.13) uses only that row and the
old prefix. The forward formula then uses the own fresh column,
including the diagonal. The lower current call, when viewed in the
upper filtration, is also measurable before the upper fresh row,
because its arguments were pre-step arguments and its Gamma array is
in \(\mathcal H^{(3)}\). Thus the prescribed
\(\theta\to\widehat p\to\omega\to\widehat q\) order is valid.

The algorithm's query maps themselves need only its initial \(z^{(1)}_0,
W^{(4)}_0\) and its finite transcript of declared outputs. The larger
\(\mathcal H^{(b)}\) is a device for proving the adaptive estimate; it
does not authorize unrecorded matrix calls or supply an external network
trajectory. Nor does it include the other matrix's realized adaptive
transcript as an independent random array: that transcript is generated
by the just-verified measurable recursion.

### 3. The adaptive estimate in the exact form used

Here is the specialization of fragment Q4 to \(m=n\). For
either matrix set
\[
 \begin{split}
 B_{l-1/2}&=\sum_{i\le l,\,j<l}t_i\Gamma_{ij}s_j^T,
 &B_l&=\sum_{i,j\le l}t_i\Gamma_{ij}s_j^T,\\
 \mathfrak a_l&=\sum_{j<l}s_j\Gamma_{lj},
 &\mathfrak b_l&=\sum_{i\le l}t_i\Gamma_{il}.
 \end{split}
 \tag{Q5.24}
\]
The different font distinguishes these fresh Gaussian residual vectors
from the primitive register \(a^{(2)}\). The exact identities are
\[
 \begin{split}
 g_l&=B_l\omega_l/n+
       \frac{\sigma^2}{\sqrt n A_{\omega,ll}}\mathfrak b_l,\\
 k_l&=B_{l-1/2}^T\theta_l/\sqrt n+
       \frac{\sigma^2}{\sqrt n A_{\theta,ll}}\mathfrak a_l.
 \end{split}
 \tag{Q5.25}
\]
For example, (Q5.11)--(Q5.12) give
\[
 s_i^T\omega_l/\sqrt n
   =(A_\omega-\sigma^2A_\omega^{-T})_{il}.
\]
For \(i<l\) this is \(A_{\omega,il}\); on the diagonal it is
\(A_{\omega,ll}-\sigma^2/A_{\omega,ll}\). Substitution into (Q5.13)
gives the forward identity in (Q5.25); the same identity for \(t_i^T\theta_l\)
gives the strict reverse identity. Each diagonal is at least \(\sigma\):
its squared Schur complement is
\[
 \sigma^2+y^T[I-X(X^TX+\sigma^2I)^{-1}X^T]y\ge\sigma^2,
\]
where \(X\) comprises the previous normalized query columns. The matrix
in brackets is positive semidefinite, since its eigenvalues are
\(\sigma^2/(d^2+\sigma^2)\) on singular directions and one on the
orthogonal complement.

For a deterministic ceiling \(r>0\) and \(0<\alpha<1\), define
\[
 u=\log(4K/\alpha),\quad v=\log(4n/\alpha),\quad
 c(r)=\sqrt{2r+4u},\quad
 L(r)=2\sqrt{rv}+\tfrac23c(r)v.
 \tag{Q5.26}
\]
Let \(E_r^{(b)}\) be the event that both final effective ranks for matrix
\(b\) are at most \(r\). The adaptive theorem states
\[
 \mathbb P\left(E_r^{(b)}\cap\left\{
    \max_h\|B^{(b)}_h\|_{\rm op}>L(r)
    \ \text{or}\
    \max_l(\|\mathfrak a^{(b)}_l\|_2\vee
           \|\mathfrak b^{(b)}_l\|_2)>c(r)
 \right\}\right)\le\alpha.
 \tag{Q5.27}
\]
Here \(h\) ranges over all half and full steps, so no additional union
over query times is necessary. On \(E_r^{(b)}\), outside that exceptional
event, (Q5.25) implies for every call
\[
 \begin{split}
 \|g_l\|_2&\le
       \frac{L(r)\|h_l\|_2}{n}+\frac{\sigma c(r)}{\sqrt n},\\
 \|k_l\|_2&\le
       \frac{L(r)\|v_l\|_2}{n}+\frac{\sigma c(r)}{\sqrt n}.
 \end{split}
 \tag{Q5.28}
\]
These are pointwise inequalities; the query norms can subsequently be
bounded on an intersected event.

All hypotheses are satisfied: dimensions and horizon are deterministic
and finite, \(\sigma>0\), (Q5.9) supplies independent standard Gamma
entries and an independent \(\mathcal H^{(b)}\), (Q5.23) supplies the
required causal order, and (Q5.11) uses the required consistent Cholesky
choice. In fragment Q4, localization uses the actual histories and
does not modify their dynamics. The fresh conditional covariances are
\(\sum_{j<l}s_js_j^T\) and \(\sum_{i\le l}t_it_i^T\), each bounded by
the identity, with traces the corresponding effective ranks. In
particular \(\rho\le n\) always, regardless of raw query magnitudes.
Thus the first application of (Q5.27) with \(r=n\) has an automatic rank
premise. The second application below has a deterministic smaller
ceiling proved for these very histories.

### 4. Initial and direct-noise events; first adaptive pass

Let
\[
 E_0=\{\|W^{(2)}_0\|_{\rm op},\|W^{(3)}_0\|_{\rm op}\le8,
                   \ \|W^{(4)}_0\|_\infty\le1\}.
 \tag{Q5.29}
\]
We record elementary bounds for its probability instead of assuming a
primal bound for the new recursion. For a standard scalar Gaussian \(Z\),
completion of the square gives \(\mathbb E e^{tZ}=e^{t^2/2}\). Markov's
inequality, with \(t=a\) and then \(t=-a\), gives
\(\mathbb P(|Z|>a)\le2e^{-a^2/2}\). Hence the readout part fails with
probability at most \(2n e^{-n^2/2}\).

The Euclidean unit sphere has a \(1/4\)-net of size at most \(9^n\): take
a maximal separated set, whose disjoint radius-\(1/8\) balls lie in the
radius-\(9/8\) ball, and compare volumes. Maximality gives the net
property. For unit \(x,y\), approximate both by net points \(x_0,y_0\).
The error in \(x^TWy-x_0^TWy_0\) is at most
\(\frac12\|W\|_{\rm op}\), so
\(\|W\|_{\rm op}\le2\max_{x_0,y_0}|x_0^TWy_0|\).
For fixed net points and a matrix from (Q5.8), this bilinear form is a
Gaussian of variance \(1/n\). A union bound gives
\[
 \mathbb P(\|W\|_{\rm op}>8)
 \le2\,9^{2n}e^{-8n}.
\]
Applying it to both initial hidden matrices proves
\[
 \mathbb P(E_0^c)\le
 p_0(n):=4e^{-(8-2\log9)n}+2n e^{-n^2/2}.
 \tag{Q5.30}
\]
The first-layer Gaussian vector is finite almost surely. No norm bound
on its polynomial transform \(x^{(1)}_0\) will be needed; we bound the
displacement \(x^{(1)}_j-x^{(1)}_0\).

From now on choose \(\alpha=n^{-2}\) in (Q5.26), so
\[
 u=\log(4Kn^2),\qquad v=\log(4n^3),\qquad
 D_n=\sqrt{2+4u/n}=c(n)/\sqrt n.
 \tag{Q5.31}
\]
For a standard Gaussian vector \(Z\in\mathbb R^n\), integrating its
Gaussian density gives \(\mathbb E e^{\|Z\|_2^2/4}=2^{n/2}\le e^{n/2}\).
Therefore
\[
 \mathbb P(\|Z\|_2^2>2n+4u)\le e^{-u}.
\]
There are exactly \(4K\) direct-noise vectors across two orientations
and two matrices. The event
\[
 E_D=\left\{\max_{b,l}
   \frac{\|U^{(b)}_l\|_2\vee\|V^{(b)}_l\|_2}{\sqrt n}\le D_n\right\}
 \tag{Q5.32}
\]
satisfies \(\mathbb P(E_D^c)\le4Ke^{-u}=\alpha\), without any assumption
on the histories those vectors generate.

For each matrix let \(E_C^{(b)}\) be the event that all the bounds inside
(Q5.27) hold with \(r=n\). Since the rank premise is automatic,
\(\mathbb P((E_C^{(b)})^c)\le\alpha\). Define
\[
 E_C=E_0\cap E_D\cap E_C^{(2)}\cap E_C^{(3)}.
 \tag{Q5.33}
\]
No independence between these events is asserted or needed. Equations
(Q5.30)--(Q5.33) give \(\mathbb P(E_C^c)\le p_0(n)+3\alpha\).

The deterministic inequalities \(K\le(S+2)n^2\) and \(n\ge2\) imply
\[
 u,v\le C_S\ell_n,\qquad
 D_n\le C_S,\qquad
 c(n)\le C_S\sqrt n,\qquad
 L(n)/\sqrt n\le C_S\ell_n.
 \tag{Q5.34}
\]
For example, \(\ell_n/n\) is bounded for \(n\ge2\), and the two terms
in \(L(n)/\sqrt n\) are \(2\sqrt v\) and
\((2/3)D_nv\). Thus (Q5.14), (Q5.16), (Q5.28), and \(E_0\) show, on \(E_C\),
for either oracle and every actual call,
\[
 \frac{\|\mathcal R_l\|_2}{\sqrt n}\le C_S\ell_n\frac{\|v_l\|_2}{\sqrt n}+C_S\sigma,
 \qquad
 \frac{\|\mathcal F_l\|_2}{\sqrt n}\le C_S\ell_n\frac{\|h_l\|_2}{\sqrt n}+C_S\sigma.
 \tag{Q5.35}
\]
This conclusion does not presuppose any bound on \(v_l\).

In particular, the warmup identities (Q5.18) and \(|\phi|\le c_\phi\)
give
\(\|z^{(2)}_0\|_2/\sqrt n,\|z^{(3)}_0\|_2/\sqrt n
  \le8c_\phi+\sigma D_n\le C_S\).
For orientation only, define the mathematical reference values
\(z^{(2),\mathrm{can}}_0=W^{(2)}_0h^{(1)}_0\) and
\(z^{(3),\mathrm{can}}_0=W^{(3)}_0\phi(z^{(2),\mathrm{can}}_0)\).
They are not evaluated by the algorithm. Their initial differences obey
\[
 \frac{\|z^{(2)}_0-z^{(2),\mathrm{can}}_0\|_2}{\sqrt n}\le\sigma D_n,
 \qquad
 \frac{\|z^{(3)}_0-z^{(3),\mathrm{can}}_0\|_2}{\sqrt n}\le9\sigma D_n,
 \tag{Q5.36}
\]
because the upper initial operator norm is at most eight and \(\phi\)
is 1-Lipschitz. This proves small initial discrepancies without hiding
any exact initialization calls.

### 5. Noncircular bounds for the actual states

All bounds in this section are deterministic on \(E_C\), uniform through
state \(N\), and uniform in the fixed choice of \(\tau\). Constants may
increase from line to line. For a rank-one increment,
\[
 \left\|uv^T/n\right\|_F=\frac{\|u\|_2\|v\|_2}{n},\qquad
 \frac{\|Av\|_2}{\sqrt n}\le\|A\|_{\rm op}\frac{\|v\|_2}{\sqrt n}\le\|A\|_F\frac{\|v\|_2}{\sqrt n}.
 \tag{Q5.37}
\]

First the readout update alone, independent of every other bound, gives
\[
 \|W^{(4)}_j\|_\infty\le1+j\eta c_\phi
        \le B_4:=1+(S+1)c_\phi,
 \qquad \frac{\|\delta^{(3)}_j\|_2}{\sqrt n}\le B_4.
 \tag{Q5.38}
\]
The upper matrix memory therefore satisfies
\[
 \|M^{(3)}_j\|_F
 \le\eta\sum_{i<j}\frac{\|\delta^{(3)}_i\|_2\|h^{(2)}_i\|_2}{n}
 \le T B_4c_\phi\le C_S.
 \tag{Q5.39}
\]
The upper reverse query in (Q5.20) has raw argument \(\delta^{(3)}_j\).
Using (Q5.35), (Q5.38), and (Q5.39) in (Q5.21) gives
\[
 \frac{\|q^{(2)}_j\|_2}{\sqrt n}
 \le C_S\ell_n B_4+C_S\sigma+
          \|M^{(3)}_j\|_F B_4
 \le C_S\ell_n,
 \qquad \frac{\|\delta^{(2)}_j\|_2}{\sqrt n}\le\frac{\|q^{(2)}_j\|_2}{\sqrt n}\le C_S\ell_n.
 \tag{Q5.40}
\]
The last inequality uses just (Q5.2) and \(\phi'\le1\). Summing the first
two updates in (Q5.22) yields
\[
 \frac{\|a^{(2)}_j\|_2}{\sqrt n}\le C_ST\ell_n\le C_S\ell_n,
 \qquad
 \|M^{(2)}_j\|_F\le C_STc_\phi\ell_n\le C_S\ell_n.
 \tag{Q5.41}
\]
The pre-step memory formula for \(R^{(1)}\) then yields
\[
 \frac{\|R^{(1)}_j\|_2}{\sqrt n}
 \le\eta\sum_{i<j}\|M^{(2)}_i\|_F\frac{\|\delta^{(2)}_i\|_2}{\sqrt n}
 \le C_S\ell_n^2.
 \tag{Q5.42}
\]
In particular, the lower reverse output and the two forward outputs
satisfy
\[
 \frac{\|\mathcal R^{(2)}_{j+2}\|_2}{\sqrt n}\le C_S\ell_n^2,
 \qquad
 \frac{\|\mathcal F^{(2)}_{j+2}\|_2}{\sqrt n},
 \frac{\|\mathcal F^{(3)}_{j+2}\|_2}{\sqrt n}\le C_S\ell_n,
 \tag{Q5.43}
\]
by (Q5.35), (Q5.41), and the uniform bound on every activation.

Set \(y_j=x^{(1)}_j-x^{(1)}_0\) and
\(\lambda=\eta/\epsilon=n^{-15/8}\in(0,1]\). The last three updates
in (Q5.22) are convex combinations of the current register and its target:
\[
 \begin{split}
 y_{j+1}&=(1-\lambda)y_j+
     \lambda[\mathcal R^{(2)}_{j+2}+R^{(1)}_j],\\
 z^{(2)}_{j+1}&=(1-\lambda)z^{(2)}_j+
     \lambda[\mathcal F^{(2)}_{j+2}+M^{(2)}_jh^{(1)}_j],\\
 z^{(3)}_{j+1}&=(1-\lambda)z^{(3)}_j+
     \lambda[\mathcal F^{(3)}_{j+2}+M^{(3)}_jh^{(2)}_j].
 \end{split}
 \tag{Q5.44}
\]
The targets have normalized norms at most \(C_S\ell_n^2,C_S\ell_n,
C_S\ell_n\), respectively, by (Q5.39)--(Q5.43). Since \(y_0=0\) and the
warmup preactivations are bounded, the triangle inequality and induction
in (Q5.44) give
\[
 \max_{j\le N}\frac{\|x^{(1)}_j-x^{(1)}_0\|_2}{\sqrt n}\le C_S\ell_n^2,
 \qquad
 \max_{j\le N}
 \frac{\|z^{(2)}_j\|_2\vee\|z^{(3)}_j\|_2}{\sqrt n}\le C_S\ell_n.
 \tag{Q5.45}
\]
There was no feedback bootstrap in this chain: bounded activations give
the readout and \(\delta^{(3)}\) bounds first, then the upper memory,
then \(\delta^{(2)}\), the lower memories, and finally the relaxed
registers. It uses neither a small effective-rank premise nor bounds
borrowed from an unperturbed network.

### 6. Actual slow histories and the warmup column

Taking differences in (Q5.44), and using both the target and state bounds,
gives
\[
 \begin{split}
 \frac{\|x^{(1)}_{j+1}-x^{(1)}_j\|_2}{\sqrt n}
      &\le C_S\eta\ell_n^2/\epsilon,\\
 \frac{\|z^{(2)}_{j+1}-z^{(2)}_j\|_2}{\sqrt n}
  \vee \frac{\|z^{(3)}_{j+1}-z^{(3)}_j\|_2}{\sqrt n}
      &\le C_S\eta\ell_n/\epsilon.
 \end{split}
 \tag{Q5.46}
\]
The Lipschitz bounds in (Q5.7) transfer these estimates to the first two
activation histories. For the upper reverse history, use the exact
difference identity
\[
 \begin{split}
 \delta^{(3)}_{j+1}-\delta^{(3)}_j
 ={}&(W^{(4)}_{j+1}-W^{(4)}_j)\odot\phi'(z^{(3)}_{j+1})\\
 &+W^{(4)}_j\odot
       [\phi'(z^{(3)}_{j+1})-\phi'(z^{(3)}_j)].
 \end{split}
\]
It and (Q5.38), (Q5.46) imply
\[
 \frac{\|\delta^{(3)}_{j+1}-\delta^{(3)}_j\|_2}{\sqrt n}
 \le\eta c_\phi+2B_4\frac{\|z^{(3)}_{j+1}-z^{(3)}_j\|_2}{\sqrt n}
 \le C_S\eta\ell_n/\epsilon.
\]
Finally \(\frac{\|a^{(2)}_{j+1}-a^{(2)}_j\|_2}{\sqrt n}\le C_S\eta\ell_n\) follows
directly from (Q5.40). Summing adjacent increments proves the discrete
Lipschitz bounds on mesh indices, with constants
\[
 \begin{array}{c|c}
 \text{normalized mesh history}&\text{Lipschitz constant in feature time}\\\hline
 h^{(1)}_j/\sqrt n&C_S\ell_n^2/\epsilon\\
 h^{(2)}_j/\sqrt n&C_S\ell_n/\epsilon\\
 \delta^{(3)}_j/\sqrt n&C_S\ell_n/\epsilon\\
 a^{(2)}_j/\sqrt n&C_S\ell_n.
 \end{array}
 \tag{Q5.47}
\]
Choose once a deterministic constant \(C_*(S)\ge1\) large enough that
\[
 M_*:=C_*(S)\ell_n^2/\epsilon
 \tag{Q5.48}
\]
dominates all four constants in (Q5.47), for all \(n\ge2\). Such a choice
is possible because every preceding constant was deterministic and
independent of \(\tau\).

The warmup needs separate treatment. For the lower reverse history its
warmup and first mesh column are both zero. For the two forward
histories the warmup repeats the first mesh argument. For the upper
reverse history, however, the warmup column is zero while the first
mesh column is \(\delta^{(3)}_0/\sqrt n\), generally nonzero, at the
same physical and feature time. We do **not** assert (Q5.47) across this
pair. We keep the warmup column exactly in a column approximation,
costing at most one additional rank direction for each history.

Here is the deterministic estimate, including integer and dimension
choices. Let \(X\) be any one of the \(n\)-by-\(K\) normalized full
histories, comprising one warmup and \(N\) mesh columns. For any integer
\(1\le d\le N\), partition the mesh-column indices \(1,\ldots,N\) into
the nonempty blocks
\[
 \lfloor (a-1)N/d\rfloor< i\le\lfloor aN/d\rfloor,
       \qquad a=1,\ldots,d.
\]
Replace each mesh column by its block's first column, and retain the
warmup exactly, to obtain \(Y\). Then
\[
 \operatorname{rank}Y\le d+1,\qquad
 \|X-Y\|_F^2\le N(M_*T/d)^2.
 \tag{Q5.49}
\]
Indeed, each block spans at most
\(\eta(\lceil N/d\rceil-1)\le\eta N/d=T/d\) in feature time,
and (Q5.47)--(Q5.48) bound each column error by \(M_*T/d\).

To verify the effective-rank implication without a spectral-tail
assumption, let \(P\) be the orthogonal projection onto the column space
of \(Y\), and let \(Q=XX^T(XX^T+\sigma^2I)^{-1}\). Eigenvalues give
\(0\preceq Q\preceq I\) and \(Q\preceq XX^T/\sigma^2\). Consequently
\[
 \begin{split}
 \rho(X)&=\operatorname{tr}(PQ)+\operatorname{tr}((I-P)Q)\\
 &\le d+1+\sigma^{-2}\|(I-P)X\|_F^2\\
 &\le d+1+\frac{NM_*^2T^2}{\sigma^2d^2}.
 \end{split}
 \tag{Q5.50}
\]
The last line uses \((I-P)Y=0\). Independently \(\rho(X)\le\min(n,K)\).

Put
\[
 x_*=(NM_*^2T^2/\sigma^2)^{1/3},\qquad
 d=\min\{N,\max\{1,\lceil x_*\rceil\}\}.
 \tag{Q5.51}
\]
If \(0<x_*\le N\), then \(d\le x_*+1\), \(d\ge x_*\), and (Q5.50) is
at most \(2+2x_*\). If \(x_*=0\), choose \(d=1\), and (Q5.50) is at most
two. If \(x_*>N\), take the exact \(K\)-column rank bound; in this case
\(K=N+1\le2+2x_*\). Thus, in every case,
\[
 \rho(X)\le r_n:=\min\{n,K,2+2x_*\}.
 \tag{Q5.52}
\]
The ceiling \(r_n>0\) is deterministic; the adaptive theorem permits real
ceilings. The integer \(d\) used to prove it has been specified in (Q5.51).
For the chosen parameters,
\[
 \begin{split}
 x_*&=C_*(S)^{2/3}
  (NT^2\epsilon^{-2}\sigma^{-2})^{1/3}\ell_n^{4/3}\\
 &\le C_S\big(n^2 n^{1/4}n^{1/2}\big)^{1/3}\ell_n^{4/3}
  =C_S n^{11/12}\ell_n^{4/3}.
 \end{split}
 \tag{Q5.53}
\]
This proves (Q5.5) for final histories on \(E_C\), with the extra two
absorbed in \(C_S\). Prefix effective ranks cannot exceed the final
rank: the consistent Cholesky columns express them as
\(\sum_{i\le l}\|t_i\|_2^2\) or \(\sum_{i\le l}\|s_i\|_2^2\).
This also proves (Q5.5) for every prefix. Every matrix in (Q5.49)--(Q5.53) is
the realized perturbed history; no frozen-history probabilistic
calculation was used.

### 7. Second adaptive pass and raw perturbation size

Apply (Q5.27) again to each matrix, now with the deterministic ceiling
\(r=r_n\), the same \(K,\sigma\), and failure allowance \(\alpha=n^{-2}\).
For \(b=2,3\), let
\[
 F_b=E_{r_n}^{(b)}\cap\left\{
    \max_h\|B^{(b)}_h\|_{\rm op}>L(r_n)
    \ \text{or}\
    \max_l(\|\mathfrak a^{(b)}_l\|_2\vee
           \|\mathfrak b^{(b)}_l\|_2)>c(r_n)
 \right\}.
 \tag{Q5.54}
\]
The theorem gives \(\mathbb P(F_b)\le\alpha\) unconditionally. Section 6
proved \(E_C\subseteq E_{r_n}^{(2)}\cap E_{r_n}^{(3)}\). Therefore on
\[
 \mathcal E_n^\tau=E_C\setminus(F_2\cup F_3)
 \tag{Q5.55}
\]
all the refined bounds hold for both matrices. The union bound gives
(Q5.4). In particular, we have not conditioned the second martingale
argument on the first pass, nor resampled any arrays, nor assumed
independence of the two matrices' resulting bad events.

From (Q5.26), (Q5.31), and (Q5.34),
\[
 \frac{L(r_n)}{\sqrt n}
 \le C_S\left(\sqrt{r_n/n}\,\ell_n+
                  n^{-1/2}\ell_n^{3/2}\right).
 \tag{Q5.56}
\]
Here \(\sqrt{r_nv}/\sqrt n\le C_S\sqrt{r_n/n}\ell_n\), and
\(c(r_n)\le\sqrt{2r_n}+2\sqrt u\) bounds the other term. Using (Q5.53)
in (Q5.56) yields
\[
 \frac{L(r_n)}{\sqrt n}
 \le C_S n^{-1/24}\ell_n^{5/3}
       +C_S n^{-1/2}\ell_n^{3/2}.
 \tag{Q5.57}
\]
Also \(r_n\le n\) implies
\[
 \sigma c(r_n)/\sqrt n\le\sigma c(n)/\sqrt n\le C_S\sigma.
 \tag{Q5.58}
\]
All forward raw arguments obey \(\frac{\|h_l\|_2}{\sqrt n}\le c_\phi\), including
warmups. All upper reverse raw arguments have normalized norm at most
\(B_4\), including the zero warmup. All lower reverse raw arguments have
normalized norm at most \(C_S\ell_n\) by (Q5.41), again including the zero
warmup. Thus a common upper bound for every query norm occurring in
(Q5.28) is \(C_S\ell_n\). Combining (Q5.16), (Q5.28), (Q5.32), and (Q5.57)--(Q5.58) gives
\[
 \max_{b,l}
 \frac{\|e_l^{(b),\rm rev}\|_2\vee\|e_l^{(b),\rm for}\|_2}{\sqrt n}
 \le C_S n^{-1/24}\ell_n^{8/3}
    +C_S n^{-1/2}\ell_n^{5/2}+C_S\sigma.
 \tag{Q5.59}
\]
For \(n\ge2\), the middle term is bounded by the first after enlarging
the constant, since their ratio is \(n^{-11/24}\ell_n^{-1/6}\le1\).
Substitution of \(\sigma=n^{-1/4}\) proves (Q5.6).

The rank bound also gives
\(r_n\ell_n^2/n\le C_S n^{-1/12}\ell_n^{10/3}\to0\), consistent
with the adaptive theorem's criterion. For any one of these errors,
its mesh primitive satisfies the purely deterministic bound
\[
 \max_{j\le N}\frac{\left\|\eta\sum_{i<j}e_{i+2}\right\|_2}{\sqrt n}
       \le T\max_{l\ge2}\frac{\|e_l\|_2}{\sqrt n}.
 \tag{Q5.60}
\]
Neither (Q5.59) nor (Q5.60) is a nonlinear trajectory comparison. The theorem
is proved for each prescribed \(\tau\). Its constants and failure
allowances are uniform in clipping level, but its adaptive events may
depend on \(\tau\). No union over all clipping maps has been taken.

For the degenerate horizon \(S=0\), there are no updates and \(K=1\):
the reverse histories are zero, each forward history has effective rank
at most one, the Gamma terms vanish, and the same asymptotic claims
follow directly from the Gaussian maximum for the four warmup noise
vectors. The main proof above treats the nonempty-update case \(S>0\).


## Q6. Deterministic filtered/unfiltered clipped stability

Compare the exact auxiliary recursion in Q5 with the unfiltered, algebraically
constrained finite-width feature flow below. Both use the same initial bottom
vector, hidden matrices and stored readout, and the same bounded clipping map.
The query errors are evaluated at the actual perturbed arguments.

### Statement and exact comparison

Fix \(S,M\ge1\), \(R\ge1\), \(n\ge1\), and a scalar map \(\tau\) with
\[
 |\tau(v)|\le |v|,\qquad |\tau(v)|\le R,\qquad
 |\tau(v)-\tau(w)|\le |v-w|.
 \tag{Q6.1}
\]
Take \(0<\eta\le1\), an integer \(N\ge1\) with \(N\eta\le S+1\),
and \(\eta\le\varepsilon\le1\).
Every vector norm below is an ordinary Euclidean norm.
Suppose the two initial matrices have operator norm at most \(M\)
and \(\|W^{(4)}_0\|_\infty\le1\).
There is no bound needed on individual coordinates of \(z^{(1)}_0\).

The reference is the canonical finite-width feature flow with
\[
 h^{(\ell)}=\phi(z^{(\ell)}),\quad \phi(z)=\arctan z,\quad
 z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},
\]
\[
 \delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\quad
 q^{(2)}=(W^{(3)})^{\mathsf T}\delta^{(3)},\quad
 \delta^{(2)}=\phi'(z^{(2)})\odot\tau(q^{(2)}),
\]
\[
 (z^{(1)})'=\phi'(z^{(1)})\odot(W^{(2)})^{\mathsf T}\delta^{(2)},
 \quad (W^{(2)})'=\delta^{(2)}(h^{(1)})^{\mathsf T}/n,
 \quad (W^{(3)})'=\delta^{(3)}(h^{(2)})^{\mathsf T}/n,
 \quad (W^{(4)})'=h^{(3)}.
 \tag{Q6.2}
\]
All initial parameters equal the stated initial values. A prime in
this fragment means differentiation in feature time.
Put \(F(z)=z+z^3/3\), \(x^{(1)}=F(z^{(1)})\), and
\[
 a^{(2)}(s)=\int_0^s\delta^{(2)}(t)\,dt,\qquad
 M^{(\ell)}=W^{(\ell)}-W^{(\ell)}_0\quad(\ell=2,3),\qquad
 R^{(1)}(s)=\int_0^s (M^{(2)}(t))^{\mathsf T}\delta^{(2)}(t)\,dt.
 \tag{Q6.3}
\]
These identities retain every learned matrix term. Exactly,
\[
 x^{(1)}=x^{(1)}_0+(W^{(2)}_0)^{\mathsf T}a^{(2)}+R^{(1)}.
 \tag{Q6.4}
\]
Indeed \(F'=1/\phi'\) turns the first equation in (Q6.2) into
\((x^{(1)})'=(W^{(2)}_0+M^{(2)})^{\mathsf T}\delta^{(2)}\);
integrating proves (Q6.4).

Hats denote the filtered recursion at \(s_k=k\eta\).
At the start of each step set
\[
 \widehat h_k^{(1)}=\phi(F^{-1}(\widehat x_k^{(1)})),\quad
 \widehat h_k^{(2)}=\phi(\widehat z_k^{(2)}),\quad
 \widehat h_k^{(3)}=\phi(\widehat z_k^{(3)}),\quad
 \widehat\delta_k^{(3)}
   =\widehat W_k^{(4)}\odot\phi'(\widehat z_k^{(3)}).
\]
Let the four queried outputs be
\[
 \widehat T_k^{(2)}
  =(W^{(2)}_0)^{\mathsf T}\widehat a_k^{(2)}+e_{T,k}^{(2)},
 \qquad
 \widehat F_k^{(2)}
  =W^{(2)}_0\widehat h_k^{(1)}+e_{F,k}^{(2)},
\]
\[
 \widehat T_k^{(3)}
  =(W^{(3)}_0)^{\mathsf T}\widehat\delta_k^{(3)}+e_{T,k}^{(3)},
 \qquad
 \widehat F_k^{(3)}
  =W^{(3)}_0\widehat h_k^{(2)}+e_{F,k}^{(3)}.
 \tag{Q6.5}
\]
Here the query errors may depend arbitrarily on all previous states.
Assume only
\[
 \max_{\ell=2,3;\,0\le k<N}
 \frac{\|e_{T,k}^{(\ell)}\|_2+\|e_{F,k}^{(\ell)}\|_2}{\sqrt n}
 \le b,\qquad 0\le b\le1.
 \tag{Q6.6}
\]
Form \(\widehat q_k^{(2)}=\widehat T_k^{(3)}
       +(\widehat M_k^{(3)})^{\mathsf T}\widehat\delta_k^{(3)}\)
and \(\widehat\delta_k^{(2)}
       =\phi'(\widehat z_k^{(2)})\odot\tau(\widehat q_k^{(2)})\).
Every right side in the following simultaneous updates uses step \(k\):
\[
\begin{aligned}
 \widehat a_{k+1}^{(2)}
  &=\widehat a_k^{(2)}+\eta\widehat\delta_k^{(2)},\\
 \widehat M_{k+1}^{(2)}
  &=\widehat M_k^{(2)}
      +\eta\widehat\delta_k^{(2)}(\widehat h_k^{(1)})^{\mathsf T}/n,\\
 \widehat M_{k+1}^{(3)}
  &=\widehat M_k^{(3)}
      +\eta\widehat\delta_k^{(3)}(\widehat h_k^{(2)})^{\mathsf T}/n,\\
 \widehat R_{k+1}^{(1)}
  &=\widehat R_k^{(1)}
      +\eta(\widehat M_k^{(2)})^{\mathsf T}\widehat\delta_k^{(2)},\\
 \widehat W_{k+1}^{(4)}
  &=\widehat W_k^{(4)}+\eta\widehat h_k^{(3)},\\
 \widehat x_{k+1}^{(1)}
  &=(1-\eta/\varepsilon)\widehat x_k^{(1)}
       +(\eta/\varepsilon)
       [x_0^{(1)}+\widehat T_k^{(2)}+\widehat R_k^{(1)}],\\
 \widehat z_{k+1}^{(2)}
  &=(1-\eta/\varepsilon)\widehat z_k^{(2)}
       +(\eta/\varepsilon)
       [\widehat F_k^{(2)}+\widehat M_k^{(2)}\widehat h_k^{(1)}],\\
 \widehat z_{k+1}^{(3)}
  &=(1-\eta/\varepsilon)\widehat z_k^{(3)}
       +(\eta/\varepsilon)
       [\widehat F_k^{(3)}+\widehat M_k^{(3)}\widehat h_k^{(2)}].
\end{aligned}
 \tag{Q6.7}
\]
Initially \(\widehat a^{(2)},\widehat R^{(1)},\widehat M^{(2)},
\widehat M^{(3)}\) are zero,
\(\widehat x_0^{(1)}=x_0^{(1)}\), and
\(\widehat W_0^{(4)}=W_0^{(4)}\).
Allow warmup errors satisfying
\[
 d_0:=\frac{\|\widehat z_0^{(2)}-z_0^{(2)}\|_2+
                 \|\widehat z_0^{(3)}-z_0^{(3)}\|_2}{\sqrt n}\le1.
 \tag{Q6.8}
\]
Then a constant \(C_{S,M,R}\), independent of \(n,\eta,\varepsilon,b,d_0\)
and of the particular map in (Q6.1), satisfies
\[
\begin{split}
 \max_{0\le k\le N}\bigg\{
 &\frac{\|\widehat x_k^{(1)}-x^{(1)}(s_k)\|_2+
          \|\widehat z_k^{(2)}-z^{(2)}(s_k)\|_2+
          \|\widehat z_k^{(3)}-z^{(3)}(s_k)\|_2}{\sqrt n}\\
 &+\frac{\|\widehat a_k^{(2)}-a^{(2)}(s_k)\|_2+
          \|\widehat R_k^{(1)}-R^{(1)}(s_k)\|_2+
          \|\widehat W_k^{(4)}-W^{(4)}(s_k)\|_2}{\sqrt n}\\
 &+\|\widehat M_k^{(2)}-M^{(2)}(s_k)\|_{\rm F}
   +\|\widehat M_k^{(3)}-M^{(3)}(s_k)\|_{\rm F}\bigg\}
 \le C_{S,M,R}(\varepsilon+\eta+b+d_0).
\end{split}
 \tag{Q6.9}
\]
Thus there is no \(\exp(C/\varepsilon)\) stability loss here.
The constant is not claimed uniform as \(R\) increases.

### Uniform bounds and reference quadrature

Write \(c=\pi/2\) and \(T=S+1\). For either the reference or the
recursion, the readout coordinate bound is \(1+cT\), since each
readout derivative or increment is bounded by \(c\).
Consequently the normalized size of \(\delta^{(3)}\) is bounded
by \(1+cT\). The rank-one inequality
\(\|uv^{\mathsf T}/n\|_{\rm F}=\|u\|_2\|v\|_2/n\)
bounds \(\|M^{(3)}\|_{\rm F}\) and \(\|\widehat M^{(3)}\|_{\rm F}\)
by \(cT(1+cT)\).
Equation (Q6.5), (Q6.6), and the initial operator bound give
\(\|\widehat q_k^{(2)}\|_2/\sqrt n\le C_{S,M}\);
the same estimate, without query error, holds for the reference.
Domination in (Q6.1) gives the bound for both \(\delta^{(2)}\).
Their integrals and rank updates bound \(a^{(2)},M^{(2)},R^{(1)}\)
and their hatted versions, with vector norms divided by \(\sqrt n\)
and matrix Frobenius norms, by \(C_{S,M}\).
This reasoning is sequential: no state-error bound has been used.

The filter coefficient \(\eta/\varepsilon\) is in \([0,1]\).
Thus (Q6.7) bounds \(\|\widehat x^{(1)}-x_0^{(1)}\|_2/\sqrt n\)
by the maximum size of its bounded targets, and bounds the two
hatted preactivations similarly. Both their initial normalized sizes
are at most \(Mc+d_0\), by the initial operator bound and (Q6.8).
All these bounds are \(C_{S,M}\). The reference preactivations
are bounded by the two trained operator norms times \(c\).

The reference field is locally Lipschitz at each finite \(n\):
\(\tau\) is Lipschitz, the other coordinate functions are smooth,
and its products are locally Lipschitz in finitely many parameters.
The preceding polynomial readout and trained-matrix bounds prevent
escape. Its bottom derivative has normalized size at most
\(\|W^{(2)}\|_{\rm op}\|\delta^{(2)}\|_2/\sqrt n\),
which also prevents bottom escape. Hence its unique local solution
continues throughout \([0,T]\).

The reference velocities \(x^{(1)\prime},z^{(2)\prime},
z^{(3)\prime},h^{(1)\prime},h^{(2)\prime},h^{(3)\prime}\)
have normalized size bounded by \(C_{S,M}\).
For example,
\[
 x^{(1)\prime}=(W^{(2)})^{\mathsf T}\delta^{(2)},\qquad
 h^{(1)\prime}=\phi'(z^{(1)})^2\odot
                       (W^{(2)})^{\mathsf T}\delta^{(2)},
\]
\[
 z^{(2)\prime}
 =\frac{\|h^{(1)}\|_2^2}{n}\delta^{(2)}
       +W^{(2)}h^{(1)\prime},\qquad
 z^{(3)\prime}
 =\frac{\|h^{(2)}\|_2^2}{n}\delta^{(3)}
       +W^{(3)}h^{(2)\prime}.
 \tag{Q6.10}
\]
Use \(|\phi'|\le1\) and the established bounds.
Also
\[
 \delta^{(3)\prime}
 =h^{(3)}\odot\phi'(z^{(3)})
       +W^{(4)}\odot\phi''(z^{(3)})\odot z^{(3)\prime},
\]
\[
 q^{(2)\prime}
 =h^{(2)}\frac{\|\delta^{(3)}\|_2^2}{n}
       +(W^{(3)})^{\mathsf T}\delta^{(3)\prime}.
 \tag{Q6.11}
\]
These have the same normalized bounds because \(|\phi''|\le2\)
and the readout coordinates are bounded.
For the possibly nondifferentiable clipping, the difference quotient
bound from (Q6.1), followed by (Q6.10)--(Q6.11), gives
\[
 \frac{\|\delta^{(2)}(s)-\delta^{(2)}(t)\|_2}{\sqrt n}
 \le \frac{\|q^{(2)}(s)-q^{(2)}(t)\|_2}{\sqrt n}
       +2R\frac{\|z^{(2)}(s)-z^{(2)}(t)\|_2}{\sqrt n}
 \le C_{S,M,R}|s-t|.
 \tag{Q6.12}
\]
All five reference slow right sides
\[
 \delta^{(2)},\quad
 \delta^{(2)}(h^{(1)})^{\mathsf T}/n,\quad
 \delta^{(3)}(h^{(2)})^{\mathsf T}/n,\quad
 (M^{(2)})^{\mathsf T}\delta^{(2)},\quad h^{(3)}
 \tag{Q6.13}
\]
are therefore time-Lipschitz with constant \(C_{S,M,R}\) in their
respective norms. For a product, subtract one factor at a time and
use the uniform bounds above and the rank-one inequality.
Integrating its difference from the left endpoint over one step
gives a quadrature error at most \(C_{S,M,R}\eta^2/2\)
for each equation in (Q6.13).

### Filter contraction and the slow-state error

Let \(E_k\) be the sum of the last five errors in (Q6.9), namely
those in \(a^{(2)},M^{(2)},M^{(3)},R^{(1)},W^{(4)}\), and put
\(D_k=\max_{0\le j\le k}E_j\).
Let \(A_k,B_k,C_k\) be the normalized errors in
\(x^{(1)},z^{(2)},z^{(3)}\), respectively; these are nonnegative
scalars, not matrices. Initially \(E_0=A_0=0\) and \(B_0+C_0=d_0\).
The maps \(F^{-1}\) and \(\phi\circ F^{-1}\) are 1-Lipschitz,
because \(F'\ge1\) and
\((\phi\circ F^{-1})'=(\phi'\circ F^{-1})^2\le1\).

For \(p=\eta/\varepsilon\), (Q6.4)--(Q6.7) and the reference velocity
bound give
\[
 A_{k+1}\le(1-p)A_k+p(ME_k+E_k+b)+C_{S,M}\eta.
 \tag{Q6.14}
\]
The last term is the reference increment
\(x^{(1)}(s_{k+1})-x^{(1)}(s_k)\); its reference target at step
\(k\) equals \(x^{(1)}(s_k)\) exactly, not its next value.
Iterating (Q6.14) and using
\(\sum_{j=0}^{k-1}p(1-p)^j\le1\) gives
\[
 \max_{j\le k}A_j\le C_{S,M}(D_k+b+\varepsilon).
 \tag{Q6.15}
\]
Here \(\eta\sum_{j\ge0}(1-p)^j=\eta/p=\varepsilon\);
this is why there is no inverse-filter exponential.

Subtract the two layer-two targets. Their normalized difference is
at most
\[
 (M+\|\widehat M_k^{(2)}\|_{\rm op})A_k
       +c\|\widehat M_k^{(2)}-M^{(2)}(s_k)\|_{\rm F}+b.
\]
In this expression use the decomposition with the hatted matrix on
the activation difference and the reference activation on the matrix
difference. The same geometric-sum argument and (Q6.10) yield
\[
 \max_{j\le k}B_j
 \le B_0+C_{S,M}\big(\max_{j\le k}A_j+D_k+b+\varepsilon\big).
 \tag{Q6.16}
\]
For layer three replace \(A_k,M^{(2)}\) by \(B_k,M^{(3)}\):
\[
 \max_{j\le k}C_j
 \le C_0+C_{S,M}\big(\max_{j\le k}B_j+D_k+b+\varepsilon\big).
 \tag{Q6.17}
\]
The feedforward order of (Q6.15)--(Q6.17) gives, without a circular
instantaneous estimate,
\[
 \max_{j\le k}(A_j+B_j+C_j)
 \le C_{S,M}(D_k+b+\varepsilon+d_0).
 \tag{Q6.18}
\]

The ordinary top query difference is bounded by
\[
 \frac{\|\widehat q_k^{(2)}-q^{(2)}(s_k)\|_2}{\sqrt n}
 \le C_{S,M}(E_k+C_k)+b.
 \tag{Q6.19}
\]
Indeed the top backward difference is at most the readout error
plus \(2(1+cT)C_k\); expand the two factors in
\((W^{(3)}_0+\widehat M^{(3)})^{\mathsf T}\widehat\delta^{(3)}\)
and then add the reverse query error. The bounded clipping gives
\[
 \frac{\|\widehat\delta_k^{(2)}-\delta^{(2)}(s_k)\|_2}{\sqrt n}
 \le C_{S,M}(E_k+C_k)+b+2RB_k.
 \tag{Q6.20}
\]
Subtracting each slow right side in (Q6.13), one factor at a time,
therefore bounds its difference by
\(C_{S,M,R}(E_k+A_k+B_k+C_k+b)\).
For the memory right side specifically, use
\[
 \frac{\|(\widehat M_k^{(2)})^{\mathsf T}\widehat\delta_k^{(2)}
              -(M^{(2)}(s_k))^{\mathsf T}\delta^{(2)}(s_k)\|_2}{\sqrt n}
 \le
 \|\widehat M_k^{(2)}-M^{(2)}(s_k)\|_{\rm F}
       \frac{\|\widehat\delta_k^{(2)}\|_2}{\sqrt n}
 +\|M^{(2)}(s_k)\|_{\rm op}
       \frac{\|\widehat\delta_k^{(2)}-\delta^{(2)}(s_k)\|_2}{\sqrt n}.
 \tag{Q6.21}
\]
Thus the full returned memory is included.

The quadrature estimate after (Q6.13) and (Q6.18) imply
\[
 E_{k+1}\le E_k+
 C_{S,M,R}\eta(D_k+b+\varepsilon+d_0+\eta).
 \tag{Q6.22}
\]
Summing and maximizing,
\[
 D_k\le C_{S,M,R}(S+1)(b+\varepsilon+d_0+\eta)
       +C_{S,M,R}\eta\sum_{j<k}D_j.
 \tag{Q6.23}
\]
If \(H=C_{S,M,R}(S+1)(b+\varepsilon+d_0+\eta)\) and
\(L=C_{S,M,R}\), induction on (Q6.23) gives
\(D_k\le H(1+L\eta)^k\le H e^{L(S+1)}\).
This proves (Q6.9) together with (Q6.18).

### What this bridge does and does not remove

For a warmup of the form
\[
 \widehat z_0^{(2)}=W_0^{(2)}h_0^{(1)}+e_0^{(2)},\qquad
 \widehat z_0^{(3)}=W_0^{(3)}\phi(\widehat z_0^{(2)})+e_0^{(3)},
\]
one has \(d_0\le (1+M)\|e_0^{(2)}\|_2/\sqrt n+
\|e_0^{(3)}\|_2/\sqrt n\). Thus vanishing warmup errors are
covered, without pretending the noisy initial fields equal the
canonical fields. On any events where fragment Q5 establishes
\(b\to0\), its vanishing \(\varepsilon,\eta\) gives (Q6.9) for every
fixed clipping satisfying (Q6.1). The reference and the approximation
use the same original hidden matrices and the same prescribed tiny
readout; no comparison to a zero-readout evolved trajectory occurs.

One may reconstruct the forward fields from the approximate raw
parameters instead of from the registers. For example their layer-two
constraint discrepancy is bounded by
\[
 \frac{\|\widehat z_k^{(2)}
 -(W_0^{(2)}+\widehat M_k^{(2)})
      \phi(F^{-1}(\widehat x_k^{(1)}))\|_2}{\sqrt n}
 \le B_k+C_{S,M}(A_k+E_k).
 \tag{Q6.24}
\]
The layer-three discrepancy then follows using (Q6.24) and the bounded
trained operator norms. Hence the register constraint error also
vanishes under (Q6.9); it is not silently set to zero in (Q6.7).

For the uncut map \(\tau(v)=v\), (Q6.20) is not available with a fixed
constant \(R\). Its exact replacement retains
\[
 [\phi'(\widehat z_k^{(2)})-\phi'(z^{(2)}(s_k))]
       \odot q^{(2)}(s_k).
 \tag{Q6.25}
\]
The normalized Euclidean bound on \(q^{(2)}\) alone does not control
this term by \(B_k\), uniformly in width. Small query forcing,
vanishing filter scale, and causal low-rank histories do not discharge
that missing stability step. No uniformity as \(R\to\infty\), uncut
population existence, restartability, or exact raw-GD convergence is
proved here.

The estimate concerns states and the explicitly bounded clipped
queries in (Q6.19)--(Q6.20). Derivatives of the filter registers have a
factor \(1/\varepsilon\); (Q6.9) alone does not imply convergence of
those derivatives. All hidden velocity/kernel and physical-clock
convergence claims must still be justified separately.


## Q7. Growing-cap filtered/unfiltered comparison

The reference in this statement remains clipped. Increasing the cap establishes
a comparison between two width-dependent clipped systems; it does not identify
an uncut or common population limit.

Fix \(S>0\). For each \(n\ge2\), choose a deterministic clipping bound
\(R_n\ge1\) and one deterministic scalar map \(\tau_n\) such that
\[
 |\tau_n(v)|\le\min\{|v|,R_n\},\qquad
 |\tau_n(v)-\tau_n(w)|\le|v-w|,\qquad R_n=o(\log n).
 \tag{Q7.1}
\]
In particular, \(R_n\to\infty\) is permitted. The identity map is
not covered by a finite \(R_n\); no assertion about it is hidden in (Q7.1).
Examples of admissible bounds include
\(R_n=\max\{1,\sqrt{\log(e+n)}\}\), with any common clipping satisfying
the displayed bounds. No condition of simultaneous Gaussian events
over all maps is imposed.

Let \(E_n(S)\) be exactly the maximum in equation (Q6.9) of fragment Q6 for the algorithm and its reference at all mesh states through
\(N=\lceil Sn^2\rceil\). Thus it sums the Euclidean errors, divided
by \(\sqrt n\), in \(x^{(1)},z^{(2)},z^{(3)},a^{(2)},R^{(1)},W^{(4)}\)
and the ordinary Frobenius errors in \(M^{(2)},M^{(3)}\).
The reference is clipped with \(\tau_n\), and its initial fields
are computed exactly from the original canonical Gaussian seeds;
the algorithm's noisy warmup is compared to them, not identified
with them.

There exist events with probability tending to one and a deterministic
sequence \(d_n(S)\to0\) such that
\[
 E_n(S)\le n^{-1/24+d_n(S)}.
 \tag{Q7.2}
\]
The events have the same lower probability bound as equation (Q5.4) of
fragment Q5, after ignoring finitely many widths. Consequently
\(E_n(S)\to0\) in probability for every fixed finite \(S\).

### The clipping dependence is explicit, not assumed uniform

We first extract a quantitative constant from the deterministic
stability proof. With \(S,M\) fixed, its preceding uniform state,
operator, readout-coordinate and filter bounds are independent of \(R\).
Call a common larger constant \(C_0(S,M)\ge1\).
Its reference middle-backward time difference in (Q6.12) is bounded by
\(C_0(1+R)|s-t|\). Each of its five reference slow right sides
therefore has time-Lipschitz constant at most \(C_1(1+R)\):
the only new \(R\) factor enters through \(\delta^{(2)}\), and in
each product one subtracts one factor at a time. All other factors
already have \(R\)-independent bounds. Thus the sum of one-step
quadrature errors is at most \(C_2(1+R)\eta^2\).

Likewise the difference of the two top backward fields is bounded
by the readout error and a constant times the layer-three state error,
independently of \(R\). The ordinary query difference has the same
property, together with its query error. The sole extra clipping
factor in the middle backward difference is
\[
 2R\,\frac{\|\widehat z_k^{(2)}-z^{(2)}(s_k)\|_2}{\sqrt n}.
 \tag{Q7.3}
\]
Each of the five slow right-side differences is thus bounded by
\(C_3(1+R)\) times the sum of current state and query errors.
There is no product of two middle backward differences.

In the notation of that proof, filter contraction gives
\[
 \max_{j\le k}(A_j+B_j+C_j)
 \le C_4(D_k+b+\varepsilon+d_0),
 \tag{Q7.4}
\]
with \(C_4\) independent of \(R\). Substitution into its slow-state
inequality therefore yields
\[
 E_{k+1}\le E_k+
 C_5(1+R)\eta(D_k+b+\varepsilon+d_0+\eta).
 \tag{Q7.5}
\]
Here \(E_k,D_k\) are respectively the slow-state error and its
running maximum; they are not \(E_n(S)\).
Summing and using the same elementary discrete Gronwall calculation
as in the fragment Q6 gives, after combining (Q7.4)--(Q7.5),
\[
 E_n(S)\le C_6(1+R)\exp(C_6(1+R))
                    (b+\varepsilon+d_0+\eta),
 \tag{Q7.6}
\]
whenever the hypotheses of that deterministic theorem hold.
All \(C_i\) depend only on \(S,M\), not on the map within its stated
bounds, width, mesh or filter scale. Increasing \(S\) to
\(\max\{1,S\}\) handles the fragment Q6's harmless \(S\ge1\)
normalization. This proves (Q7.6) with linear, not unspecified, clipping
dependence in the exponential.

### Apply the bound to the actual perturbed histories

The rank theorem applies to each prescribed \(\tau_n\), since its
constants and probability allowances are uniform in that deterministic
choice. It supplies a single event for this choice on which
\[
 \|W^{(2)}_0\|_{\rm op},\|W^{(3)}_0\|_{\rm op}\le8,\qquad
 \|W^{(4)}_0\|_\infty\le1,
\]
and every raw query error, divided by \(\sqrt n\), is at most
\[
 B_n=C_S n^{-1/24}\log(e+n)^{8/3}+C_S n^{-1/4}.
 \tag{Q7.7}
\]
The fragment Q6 uses a sum of two orientation errors at each
layer, so take \(b=2B_n\), not \(B_n\). Eventually \(b\le1\).
The direct-noise event in the rank theorem bounds the warmup errors
and gives \(d_0\le C_S n^{-1/4}\), by its equation (Q5.36) or direct
1-Lipschitzness of \(\phi\). Eventually \(d_0\le1\).
No conditional independence after selecting this event is used.

Its remaining parameters are
\(\varepsilon=n^{-1/8}\), \(\eta=n^{-2}\), and
\(N\eta\le S+1\), with \(0<\eta\le\varepsilon\le1\).
Thus all deterministic hypotheses are checked on the same event.
Apply (Q7.6) with \(M=8\) and \(R=R_n\). Since every other error is
bounded by a constant times the first term of (Q7.7), it follows that
\[
 E_n(S)\le
 C_S(1+R_n)\exp(C_S(1+R_n))
 n^{-1/24}\log(e+n)^{8/3}.
 \tag{Q7.8}
\]
The logarithm of the prefactor on the right, divided by \(\log n\),
tends to zero: \(R_n=o(\log n)\),
\(\log(1+R_n)=o(\log n)\), and
\(\log\log(e+n)=o(\log n)\). Enlarging a nonnegative deterministic
sequence \(d_n(S)\to0\) to absorb the constant in (Q7.8) proves (Q7.2).
The event probability tends to one by the rank theorem, which proves
the convergence in probability without any exchange of expectation,
clipping supremum or infinite-time limit.

### What remains after this diagonal transfer

Both processes in (Q7.2) still depend on the clipping \(\tau_n\).
The theorem says they are close to each other. It does not show that
either is close to the uncut canonical finite-width flow, nor that
their common asymptotic law exists. In particular, \(R_n\to\infty\)
alone does not prevent backward-field mass from reaching the cutoff.

The estimate has not proved a uniform clipped-tail envelope, uncut
uniqueness or autonomous restart, a limiting action-space construction,
or physical-clock/exact-GD convergence. The layer-register derivatives
and all required kernel/velocity observables still require their own
arguments. This diagonal bridge is stronger than holding the clipping
level fixed, but is not a substitute for any of these missing conclusions.


## G. Exact coupled two-matrix Gaussian transcript law

Use the fully specified algorithm in Q5. All learned increments, query outputs,
filters and memories are retained, together with the non-matrix roots. The
original initialized matrices themselves are not part of the retained joint
transcript. The finite equality in distribution below follows from the complete
covariance and sequential conditioning proof; no asymptotic Gaussian comparison
theorem is assumed.

### 1. The two declared query rules

Fix \(n,K\ge1\) and \(\sigma>0\). For the moment consider a single
matrix. Its raw reverse and forward query vectors are \(v_l,h_l\)
at calls \(1\le l\le K\). Set
\[
 \theta_l=v_l/\sqrt n,\qquad \omega_l=h_l,\qquad
 \Theta_l=[\theta_1,\ldots,\theta_l],\quad
 \Omega_l=[\omega_1,\ldots,\omega_l].
\]
Use the positive-diagonal upper Cholesky factors
\[
 A_{\theta,l}^TA_{\theta,l}=\Theta_l^T\Theta_l+\sigma^2I_l,\qquad
 A_{\omega,l}^TA_{\omega,l}=\Omega_l^T\Omega_l/n+\sigma^2I_l.
 \tag{G.1}
\]
Leading blocks agree across prefixes. The columns
\[
 t_i=(\Theta_l A_{\theta,l}^{-1})_i,\qquad
 s_i=(\Omega_l A_{\omega,l}^{-1})_i/\sqrt n
 \quad(i\le l)
 \tag{G.2}
\]
therefore do not change with later calls. In particular
\[
 \sum_{i\le l}t_it_i^T\preceq I_n,\qquad
 \sum_{i\le l}s_is_i^T\preceq I_n.
 \tag{G.3}
\]
For example the first sum equals
\(\Theta_l(\Theta_l^T\Theta_l+\sigma^2I)^{-1}\Theta_l^T\);
its singular-direction eigenvalues are \(d^2/(d^2+\sigma^2)\).

For the original perturbed rule, let \(G_0\) be an \(n\)-by-\(n\)
standard Gaussian matrix, let \(\Gamma\) be \(K\)-by-\(K\) standard
Gaussian, and let \(U_l,V_l\in\mathbb R^n\) be standard Gaussian.
All entries and arrays are independent. With \(W_0=G_0/\sqrt n\),
the two raw outputs are
\[
 \begin{split}
 {\cal R}_l&=G_0^T\theta_l+
       \sum_{i<l}s_i(\Gamma^TA_\theta)_{il}+\sigma U_l,\\
 {\cal F}_l&=G_0\omega_l/\sqrt n+
       \sum_{i\le l}t_i(\Gamma A_\omega)_{il}+\sigma V_l.
 \end{split}
 \tag{G.4}
\]
Each product at call \(l\) uses its leading \(l\)-by-\(l\) blocks.
These are exactly the raw outputs of fragment Q5: in its notation
the two displayed Gamma sums are \(\sqrt n\,k_l,\sqrt n\,g_l\).
The reverse sum is strict.

For the replacement rule, sample mutually independent standard
Gaussian matrices \(Z^{\rm for},Z^{\rm rev}\in\mathbb R^{n\times K}\)
and \(\Lambda\in\mathbb R^{K\times K}\). Write \(Z_i^{\rm for}\) and
\(Z_i^{\rm rev}\) for their columns. With the same query maps and the
same factors (G.1)--(G.2), but evaluated on this rule's own transcript,
set
\[
 \begin{split}
 {\cal R}_l^{\rm alt}
 &=\sum_{i\le l}Z_i^{\rm rev}A_{\theta,il}
       +\sum_{i<l}s_i\big((Z_i^{\rm for})^T\theta_l+
                                      \sigma\Lambda_{li}\big),\\
 {\cal F}_l^{\rm alt}
 &=\sum_{i\le l}Z_i^{\rm for}A_{\omega,il}
       +\sum_{i\le l}t_i\big((Z_i^{\rm rev})^T\omega_l/\sqrt n+
                                      \sigma\Lambda_{il}\big).
 \end{split}
 \tag{G.5}
\]
All vector/matrix dimensions and raw width factors are explicit.
In particular both kinds of output are raw \(n\)-vectors, with the normalized forward quantity equal to \(\mathcal F_l/\sqrt n\).

Assume that \(\theta_l\) is a finite measurable function of past
outputs, and \(\omega_l\) is a finite measurable function of past
outputs and possibly the current reverse output. Thus the order is
\(\theta_l\), reverse output, \(\omega_l\), forward output.
Both (G.4) and (G.5) are explicit causal recursions.
The strict reverse triangle means its factors only require earlier
forward queries; a future forward query is not needed to define it.
Positive Gram regularization ensures finite Cholesky factors and
inverses at every finite history.

The claim is equality in law of the entire output transcript, and
hence every measurable state computed from that transcript. The claim
does not preserve \(G_0\) itself as a jointly observed variable.

### 2. Covariance at an arbitrary fixed history

In this section the query vectors are deterministic arbitrary vectors.
This is a calculation of Gaussian processes at a fixed argument, not
conditioning an adaptive transcript and assuming its primitives remain
independent.

For calls \(l,k\), write
\[
 V_\theta(l,k)=\theta_l^T\theta_k+\sigma^2{\bf1}_{\{l=k\}},
 \quad
 V_\omega(l,k)=\omega_l^T\omega_k/n+\sigma^2{\bf1}_{\{l=k\}},
\]
and \(T_m=\sum_{i\le m}t_it_i^T\),
\(S_m=\sum_{i\le m}s_is_i^T\), with \(T_0=S_0=0\).
The Cholesky identities give
\[
 \sum_{i\le \min(l,k)}A_{\theta,il}A_{\theta,ik}
       =V_\theta(l,k),
 \quad
 \sum_{i\le \min(l,k)}A_{\omega,il}A_{\omega,ik}
       =V_\omega(l,k).
 \tag{G.6}
\]

For (G.4), independence and equality of the two indices of a common
Gamma entry give
\[
 \operatorname{Cov}({\cal F}_l,{\cal F}_k)
       =V_\omega(l,k)(I_n+T_{\min(l,k)}),
 \tag{G.7}
\]
\[
 \operatorname{Cov}({\cal R}_l,{\cal R}_k)
       =V_\theta(l,k)(I_n+S_{\min(l,k)-1}).
 \tag{G.8}
\]
For (G.7), the \(G_0\) contribution plus the direct noise is
\(V_\omega(l,k)I_n\); the Gamma contribution is
\(\sum_{i\le\min(l,k)}t_it_i^T
  \sum_{j\le\min(l,k)}A_{\omega,jl}A_{\omega,jk}\).
For (G.8), the outer-product sum is over \(i<\min(l,k)\)
while the \(A_\theta\) sum includes the diagonal. This proves both
identities and their strict/inclusive endpoints.

Define the two vectors, only for the following cross-covariance,
\[
 a_{l,k}=\sum_{i\le\min(l,k)}t_iA_{\theta,ik},\qquad
 b_{l,k}=\sum_{j\le\min(l,k-1)}s_jA_{\omega,jl}.
\]
Then direct index matching in (G.4) gives
\[
 \operatorname{Cov}({\cal F}_l,{\cal R}_k)
       =\theta_k\omega_l^T/\sqrt n+a_{l,k}b_{l,k}^T.
 \tag{G.9}
\]
The first term comes from \(G_0\), and the second uses precisely the
common entries \(\Gamma_{ij}\) with
\(i\le\min(l,k)\), \(j\le\min(l,k-1)\).

For (G.5), the forward-forward covariance of the \(Z^{\rm for}\)
parts is \(V_\omega(l,k)I_n\). The \(Z^{\rm rev}\) parts give
\((\omega_l^T\omega_k/n)T_{\min(l,k)}\), and the Lambda parts give
\(\sigma^2{\bf1}_{\{l=k\}}T_l\). The three arrays are independent,
so their sum is (G.7). The same calculation in reverse, with its
strict sums, gives (G.8).

There are two nonzero cross-covariances in (G.5):
the first forward term against the second reverse term, and the
second forward term against the first reverse term. Their sum is
\[
 \operatorname{Cov}({\cal F}_l^{\rm alt},{\cal R}_k^{\rm alt})
       =\theta_k b_{l,k}^T+a_{l,k}\omega_l^T/\sqrt n.
 \tag{G.10}
\]
There is no Lambda cross term: matching \(\Lambda_{il}\) with
\(\Lambda_{kj}\) would require \(i=k\le l=j<k\), an impossibility.
For \(l<k\), (G.2) implies \(b_{l,k}=\omega_l/\sqrt n\).
For \(l\ge k\), it implies \(a_{l,k}=\theta_k\).
These two cases prove that (G.9) and (G.10) agree for every \(l,k\),
including \(l=k\).

Thus the full stacked raw output vectors of (G.4) and (G.5) have identical
centered Gaussian covariances at every deterministic query history.
That common covariance is strictly positive definite. Indeed the
stacked direct noises \(\sigma U_l,\sigma V_l\) in (G.4) are independent
of all other terms and give \(\sigma^2 I_{2nK}\) to its covariance.
This argument concerns fixed arguments; it does not assert that the
actual adaptive output vector is jointly Gaussian.

### 3. Sequential covariance matching implies equality in law

Here is the finite Gaussian-conditioning fact needed to pass from the
preceding computation to actual adaptive histories.

Let \(g\) be a finite-dimensional standard Gaussian vector. Suppose
successive vector observations have the form
\[
 y_j=L_j(y_1,\ldots,y_{j-1})g,\qquad 1\le j\le m,
 \tag{G.11}
\]
where all coefficient matrices are finite measurable functions.
For a prescribed prefix \(y_1,\ldots,y_{j-1}\), stack the
first \(j\) row blocks into \(L_{\le j}(y)\), and suppose
\(K_{\le j}(y)=L_{\le j}(y)L_{\le j}(y)^T\) is positive definite.
The last row block depends on the prefix but not on \(y_j\).
This convention is used in every entry of \(K_{\le j}\).

The conditional distribution of the next observation is Gaussian
with mean and covariance
\[
 K_{j,<j}(y)K_{<j,<j}(y)^{-1}y_{<j},
 \quad
 K_{j,j}(y)-K_{j,<j}(y)K_{<j,<j}(y)^{-1}K_{<j,j}(y).
 \tag{G.12}
\]
For \(j=1\), the mean is zero.

To prove this, for deterministic \(L\) of full row rank decompose
\[
 g=L^T(LL^T)^{-1}Lg+
       [I-L^T(LL^T)^{-1}L]g.
\]
The two Gaussian terms have zero cross covariance and hence are
independent; this follows, for example, by factorization of their
joint Gaussian characteristic function. Therefore conditioning on
\(Lg=y\) gives a Gaussian with mean
\(L^T(LL^T)^{-1}y\) and covariance
\(I-L^T(LL^T)^{-1}L\).

Apply this argument first to the first observation. Inductively,
given the previous observations, the next matrix \(L_j(y_{<j})\)
is fixed, so conditioning the current Gaussian posterior on this
next linear observation gives (G.12). The same update gives posterior
mean \(L_{\le j}^TK_{\le j}^{-1}y_{\le j}\) and covariance
\(I-L_{\le j}^TK_{\le j}^{-1}L_{\le j}\): these identities can be
checked using the block inverse of
\[
 K_{\le j}=
 \begin{pmatrix}K_{<j,<j}&K_{<j,j}\\K_{j,<j}&K_{j,j}\end{pmatrix}
\]
and its Schur complement appearing in (G.12).
All inverses are measurable, and the positive Schur complements give
ordinary Gaussian conditional densities. This constructs the
conditional kernels inductively, including outside any particular
realized prefix. No assumption of independence of \(g\) from past
observations was used at the inductive step.

Consequently two recursions of the form (G.11), possibly with Gaussian
vectors of different dimensions, have the same transcript law whenever
their fixed-argument covariance matrices \(K_{\le j}(y)\) agree for
every prefix. Their first conditional kernels agree; (G.12) makes every
subsequent kernel agree, so iterated integration gives the same joint
law. Independent non-Gaussian initialization can be retained jointly
by first fixing its value and then integrating this equality.

This lemma needs only measurable causal coefficient matrices. It does
not infer a frozen Gaussian isometry for an adaptive output norm.

### 4. Apply the lemma to both interacting matrices

Run the full filtered recursion of fragment Q5. Its independent
non-matrix seeds are \(z^{(1)}_0\) and \(W^{(4)}_0\), with exactly their
canonical laws. For each matrix label \(b=2,3\), supply an independent
copy of (G.4), or an independent copy of (G.5). The two collections of
primitive Gaussian arrays are independent of one another and of these
non-matrix seeds.

Order the output blocks as follows: lower reverse/forward warmup,
upper reverse/forward warmup, and then at each update the lower
reverse/forward pair followed by the upper reverse/forward pair.
The algorithm counts discarded reverse warmup outputs in this list
although its state does not use them.

For each fixed full hypothetical transcript and fixed non-matrix seeds,
the algorithm determines every query by its previous outputs. At
each update all four arguments are selected from the pre-step state.
The upper warmup forward argument is the activation of the earlier
lower warmup output, so it also obeys this ordering. Every learned
matrix and the returned memory is a finite sum of earlier factors.
There is no direct access to \(W^{(2)}_0,W^{(3)}_0\) outside the
declared calls. This is the measurability property already proved
in fragment Q5; it holds for every hypothetical finite transcript,
not only for realized outputs.

At a fixed transcript, every output block is a linear function of
the finite vector of all primitive Gaussian entries, with coefficients
depending only on preceding blocks. For (G.4), the extra direct noise
has coefficient \(\sigma I_n\); for (G.5), expand the displayed linear
sums. The two matrices' cross covariances are zero at that fixed
argument because their primitive arrays are independent.
Within either matrix, equations (G.7)--(G.10) give identical covariances.
These equalities persist for every leading chronological prefix.

The stacked covariance of the original perturbed rule is at least
\(\sigma^2 I\), also on every prefix. The sequential lemma therefore
applies in the combined output space, without pretending that one
matrix's adaptive transcript is an independent seed for the other.
It proves equality in law of the ENTIRE coupled output transcript
for the all-original and all-replacement algorithms, jointly with
\(z^{(1)}_0,W^{(4)}_0\).

Every state register, learned increment, forward activation and middle
backward query computed from this transcript has the same joint law.
In particular both learned matrices and the strict pre-step returned
memory are preserved as computed states. The INITIAL hidden matrices
themselves are not asserted to survive as observed coordinates in the
replacement law. Nor are cross-process pathwise equalities asserted.

The result holds for every finite \(n,K,\sigma>0\) and every fixed
allowed clipping map, even if \(K\) grows with width. No limit or
width-uniform differentiability constant enters this exact equality.
It includes fragment Q5's identity map at this distributional
level, without asserting its uncut stability.

### 5. The actual conditional innovation in the middle query

Now work in the all-replacement realization. Use matrix label three
in (G.1)--(G.5). At a mesh step \(j\), its call is \(l=j+2\), and
\(\theta_l=\delta_j^{(3)}/\sqrt n\),
\(\omega_l=h_j^{(2)}\), exactly as in fragment Q5.

Let the past immediately before this upper reverse call contain the
non-matrix seeds, both matrices' earlier revealed primitives, and
the already computed current lower pair. The current upper queries
were pre-step queries. Reveal upper primitives at each reverse call
by taking \(Z_l^{\rm rev}\) and the row entries \(\Lambda_{li},i<l\);
at each forward call reveal \(Z_l^{\rm for}\) and
\(\Lambda_{il},i\le l\). This is an acyclic reveal order.
The current lower pair depends on upper primitives only through
earlier upper outputs, so it reveals no fresh upper primitive.

Set
\[
 \begin{split}
 m_l^{(2)}
 &=\sum_{i<l}Z_i^{{\rm rev},(3)}A_{\theta,il}^{(3)}
       +\sum_{i<l}s_i^{(3)}
                  (Z_i^{{\rm for},(3)})^T\theta_l^{(3)},\\
 \nu_l^{(2)}
 &=A_{\theta,ll}^{(3)}Z_l^{{\rm rev},(3)}
                 +\sigma\sum_{i<l}s_i^{(3)}\Lambda_{li}^{(3)}.
 \end{split}
 \tag{G.13}
\]
All coefficients and the first vector in (G.13) are measurable from
this past. The second vector is conditionally centered Gaussian with
\[
 \operatorname{Cov}(\nu_l^{(2)}\mid\text{past})
 =(A_{\theta,ll}^{(3)})^2 I_n
             +\sigma^2\sum_{i<l}s_i^{(3)}(s_i^{(3)})^T.
 \tag{G.14}
\]
This is a statement about joint conditional covariance, not iid
coordinates: the second term need not be diagonal.

The raw reverse output is \(m_l^{(2)}+\nu_l^{(2)}\). Including all
learned upper memory, the middle query is exactly
\[
 q_j^{(2)}
 =m_{j+2}^{(2)}+(M_j^{(3)})^T\delta_j^{(3)}
                    +\nu_{j+2}^{(2)}.
 \tag{G.15}
\]
There is no omission of the trained part of \(W^{(3)}\).

For \(T=N\eta\le S+1\), on the non-matrix initial event
\(\|W^{(4)}_0\|_\infty\le1\), bounded activation alone gives
\[
 \|W^{(4)}_j\|_\infty\le B_4:=1+(S+1)\pi/2,\qquad
 \|\delta_j^{(3)}\|_2/\sqrt n\le B_4.
 \tag{G.16}
\]
The Schur-complement diagonal satisfies
\[
 (A_{\theta,ll}^{(3)})^2
 \le\|\theta_l^{(3)}\|_2^2+\sigma^2\le B_4^2+\sigma^2.
\]
Together with (G.3), this gives the actual innovation bound
\[
 \operatorname{Cov}(\nu_l^{(2)}\mid\text{past})
       \preceq(B_4^2+2\sigma^2)I_n.
 \tag{G.17}
\]
For every coordinate \(i\), every real \(\lambda\), and every such
past, the Gaussian characteristic/density calculation therefore yields
\[
 \mathbb E[e^{\lambda\nu_{l,i}^{(2)}}\mid\text{past}]
 \le\exp\!\big((B_4^2+2\sigma^2)\lambda^2/2\big),
 \tag{G.18}
\]
and Markov's inequality optimized in \(\lambda\) gives, for \(x\ge0\),
\[
 \mathbb P(|\nu_{l,i}^{(2)}|>x\mid\text{past})
 \le2\exp\!\left(-\frac{x^2}{2(B_4^2+2\sigma^2)}\right).
 \tag{G.19}
\]
The constants are independent of clipping, mesh, filter scale and
query count for a fixed feature horizon and bounded \(\sigma\).
The initial event has probability at least \(1-2ne^{-n^2/2}\).

The learned term in (G.15) also has a pointwise bound:
\[
 (M_j^{(3)})^T\delta_j^{(3)}
 =\frac{\eta}{n}\sum_{r<j}h_r^{(2)}
                         (\delta_r^{(3)})^T\delta_j^{(3)},
\]
so, for every coordinate,
\[
 \left|[(M_j^{(3)})^T\delta_j^{(3)}]_i\right|
 \le (S+1)(\pi/2)B_4^2.
 \tag{G.20}
\]
This uses the actual trained update and actual bounded top backward
fields; it is not a frozen-weight replacement.

Conditional on the enlarged primitive past used in (G.13), the complete query
(G.15) is Gaussian with the displayed mean, including its learned term, and
innovation covariance (G.14). After averaging over that past it need not be
Gaussian. The mean \(m_l^{(2)}\) has no bound here: its coefficients depend on
earlier Gaussian outputs. Therefore (G.17)–(G.20) give neither unconditional
Gaussianity nor coordinate independence nor a clipping-uniform tail bound for
the complete query.
A union bound over all calls would also introduce the growing call
count; a fixed-call innovation tail is not a uniform path-tail theorem.

### 6. Consequence for canonical clipped trajectories

Take now exactly the parameters of fragments Q5–Q7:
\(\eta=n^{-2}\), \(N=\lceil Sn^2\rceil\),
\(\sigma=n^{-1/4}\), \(\varepsilon=n^{-1/8}\), and a prescribed
deterministic common map with cap \(R_n\ge1\), \(R_n=o(\log n)\).
Let the reference be the canonical CLIPPED finite-width feature flow
with the original independent Gaussian matrices and tiny readout.

Fragment Q7 gives a coupling of this reference with the
all-original perturbed algorithm whose mesh-state distance tends to
zero in probability, with good-event error \(n^{-1/24+o(1)}\).
The deterministic stability proof also gives, at each \(0\le j<N\),
\[
 \frac{\|\widehat q_j^{(2)}-q^{(2)}(s_j)\|_2}{\sqrt n}
 \le C_S\big(E_j+C_j\big)+b,
 \tag{G.21}
\]
where \(E_j\) is its slow-state error, \(C_j\) its layer-three error,
and \(b\) its raw query-error bound. Its constant is independent of
\(R_n\): only the subsequent middle gate subtraction introduces the
clipping factor. Thus the same coupling controls the state distance
augmented by the maximum of (G.21), still at rate
\(n^{-1/24+o(1)}\) on the good event.

Define this augmented distance as the sum of the mesh-state distance
in fragment Q7 and the maximum middle-query error over
\(j<N\), with ordinary vector norms divided by \(\sqrt n\) and
ordinary Frobenius norms for learned matrices. The non-matrix seeds
may also be retained as jointly identical coordinates.

For every test of these augmented arrays that is bounded in absolute
value by one and 1-Lipschitz for this distance, the difference between
its canonical-clipped expectation and its all-replacement expectation
is at most
\[
 n^{-1/24+o(1)}
 +2\big(4e^{-(8-2\log9)n}+2ne^{-n^2/2}+5n^{-2}\big).
 \tag{G.22}
\]
Indeed compare reference and all-original paths on the proved coupling.
On its good event the test difference is bounded by the distance;
on the complement it is at most two. Section 4 identifies the
all-original expectation with the all-replacement expectation exactly.
Constants can be absorbed into the \(o(1)\) exponent.
No unbounded test, uniform integrability, or exchange of limits is
needed for this conclusion.

Thus the replacement process gives a rigorously connected
finite-width Gaussian-array representation of the canonical CLIPPED
state and middle query on the full growing training mesh.
This does not imply convergence to a fixed population law as \(n\)
changes. In particular (G.22) does not carry conditional law statements
or arbitrary discontinuous tail indicators to the canonical flow.

The identity map is allowed in the exact finite law and innovation
bounds, but not in the canonical-clipped comparison (G.22).
This identity supplies no bound on the predictable response
\(m_l^{(2)}\), no uncut clipping removal, no population uniqueness or
autonomous restart, and no physical-time/exact-GD/kernel/velocity
convergence. These are separate mathematical conclusions.

## Every fixed identity depth: uniform step doubling and local feature time

Sections 1–8 and the IU equation numbers below are local to this identity comparison. Named references to the linear chapter refer to that separate chapter.

### 1. Scope, normalization, and the two limits

Fix an integer \(L\ge1\), independently of width and step count. There is
one input, \(d=m=1,x_1=1\), and every activation is the identity. All
blocks are trained. Write the stored endpoint vectors as \(U_n,A_n\in
\mathbb R^n\), and the stored connectors as \(B_{a,n}\in\mathbb
R^{n\times n}\), \(2\le a\le L\). Initially the endpoint entries are
independent \(N(0,1)\), the connector entries are independent
\(N(0,1/n)\), and all blocks are independent. The output is

\[
 f_n=\frac1n A_n^TB_{L,n}\cdots B_{2,n}U_n.
 \tag{IU1}
\]

An empty connector product is the identity. The raw parameter metric is

\[
 \frac{dA_n^Td\widetilde A_n}{n}
 +\frac{dU_n^Td\widetilde U_n}{n}
 +\sum_{a=2}^L\operatorname{Tr}
       (dB_{a,n}^Td\widetilde B_{a,n}).
 \tag{IU2}
\]

Thus its mobilities in stored coordinates are
\((n,1,\ldots,1,n)\). The updates below are simultaneous feature ascent
for \(f_n\). They contain no label, loss, or residual multiplier; their
step \(h\in\mathbb R\) is signed feature time.

For the finite proof representation put
\(u_n=U_n/\sqrt n, a_n=A_n/\sqrt n\). Define

\[
 x_{1,n}=u_n,\quad x_{a,n}=B_{a,n}x_{a-1,n},\qquad
 r_{L,n}=a_n,\quad r_{a-1,n}=B_{a,n}^Tr_{a,n}.
 \tag{IU3}
\]

All finite vector norms and pairings in this representation are ordinary
Euclidean ones. The exact Euler update is

\[
 \begin{split}
 a_n^+&=a_n+h x_{L,n},\\
 u_n^+&=u_n+h r_{1,n},\\
 B_{a,n}^+&=B_{a,n}+h r_{a,n}x_{a-1,n}^T,
                  \qquad 2\le a\le L.
 \end{split}
 \tag{IU4}
\]

All fields on the right are evaluated before any block is changed.
For example, the last line is the stored update
\(B_{a,n}^+=B_{a,n}+h\delta_{a,n}z_{a-1,n}^T/n\), with
\(\delta_{a,n}=\sqrt n\,r_{a,n}\) and
\(z_{a-1,n}=\sqrt n\,x_{a-1,n}\).

For each fixed integer \(N\ge0\) and fixed real \(h\), the width limit
of the output after \(N\) updates will be denoted \(F_{N,L}(h)\).
Section 3 proves its existence in probability and in every fixed finite
\(L^p\) over initialization. In particular it is also the limit of the
finite-width expected output. Only after taking this fixed-program
width limit do we let \(N\) increase and \(h\) decrease.

Here is the uniform estimate. Set \((d)_r=d(d-1)\cdots(d-r+1)\), with
\((d)_0=1\) and \((d)_r=0\) for \(r>d\), and define

\[
 K_L=\max\left\{1,\quad
  \max_{0\le r\le4}(L+1)(L)_r3^{L-r},\quad
  \max_{1\le r\le4}(L+1)_r3^{L+1-r}\right\}.
 \tag{IU5}
\]

Terms with zero falling factorial mean zero. In particular
\(K_1=6, K_2=27, K_3=108\). The explicit finite recurrence in
Section 5 defines \(C_K\) for every \(K\ge1\).

**Theorem IU.** For every integer \(t\ge1\) and
\(|h|\le1/(16K_Lt)\),

\[
 \left|F_{t,L}(2h)-F_{2t,L}(h)
 +\frac{t(2t-1)L(L+1)^2(L+2)}{3}h^3\right|
 \le C_{K_L}t^4|h|^5.
 \tag{IU6}
\]

The fixed-program limits are Euler iterates of the trace-class operator
state constructed below. On the signed interval
\(|T|\le T_L:=1/(8K_L)\) they converge, as the mesh decreases, to its
unique local feature-ascent flow, in the sum of the endpoint Hilbert
norms and connector trace norms. The convergence is uniform in feature
time on this interval. These statements hold for each separately fixed
\(L\); they assert neither a joint depth limit nor global feature-time
existence.

### 2. A fixed Hilbert source and a complete parameter space

The maintained dependency for the Gaussian identification is Section 9,
“A Gaussian source lemma with contained norm and Wick proofs,” of
`linear_dynamics.md`. Its hypotheses are exactly the independent
\(N(0,1/n)\) connectors and two independent \(N(0,I_n/n)\) endpoint
vectors in (IU3). It applies to any fixed finite number of labels and
to typed compatible words. We spell out the source it supplies.

Let \(\mathcal F\) be the real Hilbert space with orthonormal basis the
finite words on letters \(a,+\) and \(a,-\), \(2\le a\le L\), including
the empty word \(\Omega\). For \(L=1\), \(\mathcal F=\mathbb R\Omega\).
The creation map \(\ell_{a,\pm}\) prepends its letter. Its actual
Hilbert adjoint deletes that first letter when it matches, and otherwise
returns zero. On

\[
 \mathcal H=\mathcal F\oplus\mathcal F,
 \qquad U=(\Omega,0),\qquad A=(0,\Omega),
 \tag{IU7}
\]

put

\[
 \Gamma_a=(\ell_{a,+}+\ell_{a,-}^*)
               \oplus(\ell_{a,+}+\ell_{a,-}^*).
 \tag{IU8}
\]

Both roots have norm one; \(\|\Gamma_a\|\le2\), because a creation
map is an isometry and its adjoint has norm one. Each hidden layer has
a typed copy \(\mathcal H_a\) of \(\mathcal H\). The connector
\(\Gamma_a:\mathcal H_{a-1}\to\mathcal H_a\) uses label \(a\);
transpose actions use its actual adjoint. The two entire rooted word
subspaces are orthogonal and are preserved by every source action.
In the word formulas below, a creation map also denotes its diagonal
action on \(\mathcal H\) and on the indicated typed copies.

Explicitly, the Gaussian lemma says that for every fixed finite list of
initial compatible words \(P,Q\) and root choices \(i,j\in\{1,2\}\),

\[
 (P(B_n)g_{i,n})^TQ(B_n)g_{j,n}
 \longrightarrow
 \langle P(\Gamma)g_i,Q(\Gamma)g_j\rangle
 \quad\hbox{in probability},
 \tag{IU9}
\]

where \(g_{1,n}=u_n(0),g_{2,n}=a_n(0)\) and \(g_1=U,g_2=A\).
The cited section proves this by finite Wick pairings, the connected
graph count for the trace variance, Gaussian conditioning on the roots,
and the creation/annihilation word rule. Consequently (IU9) uses neither
a claim about arbitrary coordinate nonlinearities nor an unproved
simultaneous Gaussian-operator realization.

Write a current connector as \(B_a=\Gamma_a+P_a\), with
\(P_a\in\mathfrak S_1(\mathcal H_{a-1},\mathcal H_a)\). Here
\(\mathfrak S_1\) is the trace-class space: the trace norm is the sum of
the singular values. Section 2.A, “Compact operators and the complete
trace-norm space,” of `linear_dynamics.md` supplies its complete-space
construction, the inequalities

\[
 \|P\|\le\|P\|_{\mathfrak S_2}\le\|P\|_{\mathfrak S_1},
 \qquad
 \|v\otimes w\|_{\mathfrak S_1}=\|v\|\|w\|,
 \tag{IU10}
\]

and the operator ideal inequalities. The tensor convention is
\((v\otimes w)z=v\langle w,z\rangle\). In particular rank-one
increments belong to this complete space even though the fixed
\(\Gamma_a\) need not be compact.

Use the Banach space

\[
 \mathcal X_L=\mathcal H_L\oplus\mathcal H_1\oplus
   \bigoplus_{a=2}^L
       \mathfrak S_1(\mathcal H_{a-1},\mathcal H_a),
 \quad
 \|\theta\|_{\mathcal X_L}
 =\|a\|+\|u\|+\sum_{a'=2}^L\|P_{a'}\|_{\mathfrak S_1}.
 \tag{IU11}
\]

Its initial state is \(\theta_0=(A,U,0,\ldots,0)\). Define

\[
 \begin{aligned}
 x_1&=u,&x_a&=B_ax_{a-1},\\
 r_L&=a,&r_{a-1}&=B_a^*r_a,\\
 f(\theta)&=\langle a,x_L\rangle,&
 g(\theta)&=(x_L,r_1,(r_a\otimes x_{a-1})_{a=2}^L).
 \end{aligned}
 \tag{IU12}
\]

The notation \(a\) for the endpoint in this formula is distinct from
an integer connector index. All population norms and pairings are the
displayed Hilbert and operator ones. These representatives describe
normalized rooted geometry, rather than individual neuron coordinates.

The maps \(f:\mathcal X_L\to\mathbb R\) and
\(g:\mathcal X_L\to\mathcal X_L\) are continuous polynomials. On
the unit ball about \(\theta_0\), endpoint norms are at most two and
connector operator norms at most three. Each of the \(L+1\) components
of \(g\) is a product with exactly \(L\) parameter factors; \(f\) has
\(L+1\). In each product a block occurs at most once. Differentiating
\(r\) times assigns the ordered differentiated factors in at most
\((L)_r\), respectively \((L+1)_r\), ways. Every direction component is
bounded by its \(\mathcal X_L\) norm; for a matrix output use (IU10).
It follows, in the multilinear operator norms induced by (IU11), that

\[
 \|D^rg(\theta)\|\le(L+1)(L)_r3^{L-r},\qquad
 \|D^rf(\theta)\|\le(L+1)_r3^{L+1-r}.
 \tag{IU13}
\]

The first bound is for \(0\le r\le4\), the second for \(1\le r\le4\).
This proves all the hypotheses represented by \(K_L\) in (IU5).

For gradient identities only, replace the trace-class factors by
Hilbert--Schmidt factors and the sum norm by the Hilbert direct-sum
norm; call the resulting Hilbert space \(\mathcal Y_L\). The same
products are continuous polynomials there because operator norm is
bounded by Hilbert--Schmidt norm. The reverse chain rule gives

\[
 Df(\theta)[v]=\langle g(\theta),v\rangle_{\mathcal Y_L}.
 \tag{IU14}
\]

For example, the connector derivative is
\(\langle r_a,\dot P_ax_{a-1}\rangle\), whose
Hilbert--Schmidt representative is \(r_a\otimes x_{a-1}\).
Thus (IU14) is a gradient identity on a Hilbert space; it is not an
identification of the Banach trace norm with a Hilbert metric.

### 3. Identification of every fixed Euler program

Let \(E_h\theta=\theta+h g(\theta)\). We prove

\[
 F_{N,L}(h)=f(E_h^N\theta_0).
 \tag{IU15}
\]

At every fixed finite step, expand each learned connector into its
initial connector plus the finite sum of rank-one updates. Applying
such an increment to a vector replaces that action by a scalar inner
product times a previously generated vector. Induction over the finite
forward, backward, and update operations therefore expresses every
generated vector as a finite sum of initial rooted words. Its scalar
coefficients are polynomials in a finite list of initial rooted Gram
entries. The list and polynomial degrees can depend on \(L,N,h\), but
are finite and independent of \(n\). No Gram inverse is used. The same
expansion is valid with the fixed \(\Gamma_a,U,A\). Applying (IU9) and
continuity to these finite polynomials proves convergence in probability
of every scalar contraction in the program, including its terminal
output, to the value in (IU15).

For completeness this also gives convergence of expected outputs; no
unjustified passage from probability to expectation is needed. The
Gaussian net argument in Section 9 of `linear_dynamics.md`, with its
threshold left variable, gives

\[
 \mathbb P\{\|B_{a,n}(0)\|>y\}
 \le2\exp(n\log81-ny^2/8).
 \tag{IU16}
\]

Indeed the same \(1/4\)-net has at most \(9^n\) points, the norm is
at most twice the largest net bilinear form, and each such form is
\(N(0,1/n)\). For \(y^2\ge16\log81\), the right side is at most
\(2e^{-y^2/16}\), uniformly in \(n\ge1\). Integrating this tail gives
uniform bounds for every finite moment of the initial connector norms.
For a normalized Gaussian endpoint and integer \(p\ge1\), convexity
gives

\[
 \mathbb E\|u_n(0)\|^{2p}
 =\mathbb E\left(\frac1n\sum_{i=1}^n U_{n,i}^2\right)^p
 \le\mathbb E|G|^{2p}<\infty,
 \qquad G\sim N(0,1).
 \tag{IU17}
\]

The same holds for \(a_n(0)\). At a finite step put

\[
 M_k=1+\|u_{n,k}\|+\|a_{n,k}\|
            +\sum_{a=2}^L\|B_{a,n,k}\|.
\]

The rank-one norm formula and (IU4) imply

\[
 M_{k+1}\le M_k+|h|(L+1)M_k^L,
 \qquad |f_{n,k}|\le M_k^{L+1}.
 \tag{IU18}
\]

At fixed \(N,h\), iteration gives a finite polynomial bound in \(M_0\)
with nonnegative coefficients. Equations (IU16)--(IU18) consequently
bound every finite moment of the output uniformly in width. Convergence
in probability to (IU15), followed by truncation and a higher moment
bound for the tails, proves convergence in every finite \(L^p\), in
particular \(L^1\). The same reasoning applies to each fixed program
scalar or vector Gram entry.

There is also an operator-state interpretation of this identification.
Each learned connector after \(N\) steps is the sum of \(N\) outer
products \(h r_{a,k}\otimes x_{a-1,k}\). All Gram entries of this fixed
list converge. For a finite-rank map \(VCW^*\), its nonzero squared
singular values are those of
\(G_V^{1/2}CG_WC^*G_V^{1/2}\), where \(G_V=V^*V,G_W=W^*W\).
Continuity of the positive square root and of the eigenvalues of a
finite symmetric matrix proves convergence of each singular value and
of the trace norm. This statement does not compare vectors from
different widths in a common norm. It identifies their fixed finite
rooted geometry with the unique state \(E_h^N\theta_0\in\mathcal X_L\).

Finally, the finite program is odd in the common step after averaging.
Let \(S\) negate only the readout endpoint. Directly from (IU12),

\[
 f(S\theta)=-f(\theta),\qquad
 Sg(\theta)=-g(S\theta),\qquad
 SE_h=E_{-h}S.
 \tag{IU19}
\]

The law of the finite initial state is invariant under \(S\); its
expected output is therefore odd in \(h\). The \(L^1\) identification
just proved yields

\[
 F_{N,L}(-h)=-F_{N,L}(h).
 \tag{IU20}
\]

This argument uses symmetry of the initial law; it does not assert
that the deterministic representative \(\theta_0\) is fixed by \(S\).

### 4. The identity cubic coefficient from orthogonal words

All quantities in this section are evaluated at \(\theta_0\) unless an
argument is displayed. Write \(g_0=g(\theta_0)\),

\[
 H_0^{\rm vec}=Dg[g_0],\qquad
 K_0^{\rm vec}=Dg[H_0^{\rm vec}],\qquad
 R_0^{\rm vec}=D^2g[g_0,g_0],
 \quad
 S_0=D^3f[g_0,g_0,g_0],\quad
 H_0^{\rm sc}=\|H_0^{\rm vec}\|_{\mathcal Y_L}^2.
 \tag{IU21}
\]

These temporary scalar and vector names will not be used for the
majorants in the next section. Symmetry of the derivatives of the
Hilbert gradient (IU14) gives

\[
 Df[K_0^{\rm vec}]=H_0^{\rm sc},\qquad
 D^2f[H_0^{\rm vec},g_0]=H_0^{\rm sc},\qquad
 Df[R_0^{\rm vec}]=S_0.
 \tag{IU22}
\]

For example, the first equality is
\(\langle g_0,Dg[H_0^{\rm vec}]\rangle
=\langle Dg[g_0],H_0^{\rm vec}\rangle\), since \(Dg\) is
self-adjoint on \(\mathcal Y_L\). The third is the differentiated
gradient identity.

Let \(\theta_N(h)=E_h^N\theta_0\). At zero step all its intermediate
states equal \(\theta_0\). Differentiating its recurrence successively
and summing gives

\[
 \begin{split}
 \theta_N'(0)&=Ng_0,\\
 \theta_N''(0)&=N(N-1)H_0^{\rm vec},\\
 \theta_N'''(0)&=6\binom N3K_0^{\rm vec}
       +\frac{N(N-1)(2N-1)}2R_0^{\rm vec}.
 \end{split}
 \tag{IU23}
\]

To check the last sum, its increment at step \(k\) is
\(3k(k-1)K_0^{\rm vec}+3k^2R_0^{\rm vec}\); sum over
\(0\le k<N\). The third scalar chain rule and (IU22) now give

\[
 F_{N,L}'''(0)
 =\frac{N(4N^2-3N+1)}2S_0
     +2N(N-1)(2N-1)H_0^{\rm sc}.
 \tag{IU24}
\]

It remains to calculate just \(S_0,H_0^{\rm sc}\) for the explicit
source. At initialization the forward and reverse vectors are unit
words

\[
 X_a=\ell_{a,+}\cdots\ell_{2,+}U,\qquad
 R_a=\ell_{a+1,-}\cdots\ell_{L,-}A.
 \tag{IU25}
\]

The factors absent at an endpoint are identities. The equality with
the forward and backward recursion follows because distinct labels
cannot annihilate the first letter in these words. They lie in the
orthogonal \(U\)- and \(A\)-rooted sectors, respectively.

Consider the straight parameter line \(\theta_0+s g_0\). Its connector
increment is \(s(R_a\otimes X_{a-1})\), which maps the \(U\)-sector
into the \(A\)-sector and annihilates the \(A\)-sector. Source connectors
preserve both sectors. Thus two such increments in a forward product
give zero; an increment applied after the endpoint variation \(sR_1\)
also gives zero. The forward state on this line is exactly

\[
 x_a(s)=X_a+sV_a,\qquad
 V_1=R_1,\quad V_a=\Gamma_aV_{a-1}+R_a,
 \tag{IU26}
\]

where \(V_a\) belongs to the \(A\)-sector. The readout is \(A+sX_L\).
Orthogonality implies that
\(\langle A+sX_L,X_L+sV_L\rangle\) is linear in \(s\).
Consequently

\[
 S_0=0.
 \tag{IU27}
\]

We next evaluate the norms in (IU26), retaining the returns created
by reuse of the same connector. For \(1\le k\le a\), set

\[
 e_{a,k}=\ell_{a,+}\cdots\ell_{k+1,+}R_k.
 \tag{IU28}
\]

When \(k=a\), this is \(R_a\). These are distinct unit words in the
\(A\)-sector, hence orthonormal. For \(k<a-1\), applying \(\Gamma_a\)
to \(e_{a-1,k}\) merely creates its first \(a,+\) letter and yields
\(e_{a,k}\). For the last word,

\[
 \Gamma_aR_{a-1}=e_{a,a-1}+R_a,
 \tag{IU29}
\]

because the annihilator deletes its initial \(a,-\). Induction in
(IU26) proves

\[
 V_a=\sum_{k=1}^a k e_{a,k},\qquad
 \|V_a\|^2=\sum_{k=1}^a k^2.
 \tag{IU30}
\]

The reverse variation on the same straight line obeys

\[
 T_L=X_L,\qquad T_{a-1}=\Gamma_a^*T_a+X_{a-1}.
 \tag{IU31}
\]

Indeed the derivative of \(B_a^*r_a\) adds
\((X_{a-1}\otimes R_a)R_a=X_{a-1}\). For an explicit orthogonal
expansion, define

\[
 \widetilde e_{a,j}=\ell_{a+1,-}\cdots\ell_{j,-}X_j,
                         \qquad a\le j\le L.
\]

These are distinct \(U\)-sector unit words. The creation term of
\(\Gamma_a^*\) prepends \(a,-\), while its annihilation term deletes
the initial \(a,+\) of \(X_a\). Exactly as in (IU29), the last return
adds to the direct \(X_{a-1}\) term. Backward induction in (IU31)
therefore gives

\[
 T_a=\sum_{j=a}^L(L-j+1)\widetilde e_{a,j},\qquad
 \|T_a\|^2=\sum_{q=1}^{L-a+1}q^2.
 \tag{IU32}
\]

The endpoint components of \(Dg[g_0]\) are \(V_L,T_1\); its connector
component is

\[
 T_a\otimes X_{a-1}+R_a\otimes V_{a-1}.
 \tag{IU33}
\]

The two terms are Hilbert--Schmidt orthogonal, since their range
vectors belong to orthogonal root sectors. Their squared norms are
\(\|T_a\|^2\) and \(\|V_{a-1}\|^2\), since \(X_{a-1},R_a\)
are unit vectors. Equations (IU30)--(IU33) yield

\[
 \begin{split}
 H_0^{\rm sc}
 &=\|V_L\|^2+\|T_1\|^2
      +\sum_{a=2}^L(\|T_a\|^2+\|V_{a-1}\|^2)\\
 &=2\sum_{q=1}^L(L-q+1)q^2
   =\frac{L(L+1)^2(L+2)}6.
 \end{split}
 \tag{IU34}
\]

For the last equality expand the sum as
\(2[(L+1)\sum q^2-\sum q^3]\), and use
\(\sum_{q=1}^Lq^2=L(L+1)(2L+1)/6\) and
\(\sum_{q=1}^Lq^3=L^2(L+1)^2/4\); both identities follow by
induction on \(L\).

Subtracting the two cubic coefficients in (IU24), including the
factor \(2^3\) for the coarse step, proves

\[
 \begin{split}
 \frac{8F_{t,L}'''(0)-F_{2t,L}'''(0)}6
 &=-\frac{t(2t-1)}2(S_0+4H_0^{\rm sc})\\
 &=-\frac{t(2t-1)L(L+1)^2(L+2)}3.
 \end{split}
 \tag{IU35}
\]

This derivation is specific to the identity activation and the stated
independent Gaussian initialization.

### 5. The explicit uniform transported-defect theorem

We prove the numerical estimate on a Banach space, so that its dependence
on the step count is visible. Let \(f\in C^4(\mathcal X;\mathbb R)\),
\(g\in C^4(\mathcal X;\mathcal X)\), and suppose on the unit ball about
\(\theta_0\) that

\[
 \|D^rg\|\le K\quad(0\le r\le4),\qquad
 \|D^rf\|\le K\quad(1\le r\le4),\qquad K\ge1.
 \tag{IU36}
\]

It suffices that the maps be defined on a neighborhood of the ball.
Put \(E_hx=x+hg(x)\), \(C_h=E_{2h}\), and \(B_h=E_h^2\). Suppose
\(d_t(h)=f(C_h^t\theta_0)-f(B_h^t\theta_0)\) is odd in \(h\).
For \(c=1/(16K)\), the following finite recurrence defines the constant.
The letters in this recurrence are numerical majorants only:

\[
 \begin{split}
 X_1&=8K,\\
 X_2&=2\{8KX_1+4cKX_1^2\},\\
 X_3&=2\{12K(X_1^2+X_2)+4cK(X_1^3+3X_1X_2)\},\\
 G_0&=K,\quad G_1=KX_1,\quad G_2=K(X_2+X_1^2),\\
 G_3&=K(X_3+3X_1X_2+X_1^3),\\
 A_r&=\sum_{q=0}^r\binom rqG_qG_{r-q}\quad(0\le r\le3),\\
 A_{-1}&=A_{-2}=0,\\
 Z_r&=X_r+c^2A_r+2rcA_{r-1}+r(r-1)A_{r-2}
                                      \quad(1\le r\le3),\\
 T_1&=2(Z_1+2K),\\
 T_2&=2\{Z_2+4KT_1+2cKT_1^2\},\\
 T_3&=2\{Z_3+6K(T_1^2+T_2)+2cK(T_1^3+3T_1T_2)\},\\
 H_0&=K,\quad H_1=KT_1,\quad H_2=K(T_2+T_1^2),\\
 H_3&=K(T_3+3T_1T_2+T_1^3).
 \end{split}
 \tag{IU37}
\]

Starting with \(W_0=2A_0\), define successively for \(r=1,2,3\),

\[
 W_r=2\left\{A_r
 +2c\sum_{q=1}^r\binom rqH_qW_{r-q}
 +2r\sum_{q=0}^{r-1}\binom{r-1}qH_qW_{r-1-q}\right\},
 \qquad
 C_K=\frac16\sum_{q=0}^3\binom3qH_qW_{3-q}.
 \tag{IU38}
\]

All indices are fixed finite ranges; these formulas terminate and
produce a number depending only on \(K\).

**Transported-defect estimate.** Under (IU36) and the oddness assumption,
for \(t\ge1, |h|\le c/t\),

\[
 \left|d_t(h)-\frac{d_t'''(0)}6h^3\right|
 \le C_Kt^4|h|^5.
 \tag{IU39}
\]

**Proof.** The exact local defect, with no Taylor truncation, is

\[
 B_hx=C_hx+h^2a_h(x),\qquad
 a_h(x)=\int_0^1Dg(x+s h g(x))[g(x)]\,ds.
 \tag{IU40}
\]

For a scalar map \(v\), write \(P_Mv=v\circ M\), and set

\[
 R_hv(x)=-\int_0^1
 Dv(C_hx+s h^2a_h(x))[a_h(x)]\,ds.
 \tag{IU41}
\]

Then \(P_{C_h}-P_{B_h}=h^2R_h\). The noncommutative telescoping
identity \(A^t-B^t=\sum_{j=0}^{t-1}A^{t-1-j}(A-B)B^j\) gives

\[
 d_t(h)=h^2Q_t(h),\qquad
 Q_t(h)=\sum_{j=0}^{t-1}
   (P_{C_h}^{t-1-j}R_hP_{B_h}^jf)(\theta_0).
 \tag{IU42}
\]

For each summand this means: first take \(t-1-j\) coarse steps,
then one coarse step and interpolate across its local defect, then
take \(2j\) fine steps, transporting the tangent direction
\(a_h(x)\) through these last fine steps. The order in (IU42) is
essential and follows from the displayed operator identity.

We give bounds for all its parameter derivatives through order three.
Consider any variable-step path from \(\theta_0\) of the form

\[
 x_{m+1}=x_m+\alpha_mh g(x_m),\qquad
 0\le\alpha_m\le2,\qquad \sum_m\alpha_m\le4t.
 \tag{IU43}
\]

As long as it lies in the unit ball its displacement is at most
\(K|h|\sum_m\alpha_m\le4cK=1/4\). The same bound at the first
putative exit rules out that exit. All interpolation points in (IU40)
are further variable-step points. In (IU41), the extra displacement is
at most \(|h|^2K^2\le c^2K^2=1/256\). The trajectory before that
point uses at most \(2t\) Euler weight and the trajectory after it uses
at most \(2t\); their total displacement is bounded by
\(1/4+1/256<1\). A first-exit argument again justifies using (IU36)
everywhere in (IU40)--(IU42), also for negative \(h\).

Primes now denote differentiation in \(h\). With all \(g\)-derivatives
evaluated at \(x_m\), differentiating one step of (IU43) gives

\[
 \begin{split}
 x_{m+1}'&=(I+\alpha_mhDg)x_m'+\alpha_mg,\\
 x_{m+1}''&=(I+\alpha_mhDg)x_m''
       +2\alpha_mDg[x_m']+\alpha_mhD^2g[x_m',x_m'],\\
 x_{m+1}'''&=(I+\alpha_mhDg)x_m'''
       +3\alpha_m\{D^2g[x_m',x_m']+Dg[x_m'']\}\\
 &\hspace{18mm}+\alpha_mh\{D^3g[x_m',x_m',x_m']
                                      +3D^2g[x_m',x_m'']\}.
 \end{split}
 \tag{IU44}
\]

The product of any consecutive homogeneous factors has norm at most

\[
 \prod_m(1+\alpha_m|h|K)
 \le\exp(K|h|\sum_m\alpha_m)\le e^{4cK}<2.
 \tag{IU45}
\]

Iterating each affine recurrence in (IU44) bounds it by twice the sum
of its inhomogeneous terms. Divide the derivative of order \(r\) by
\(t^r\) and use \(\sum\alpha_m/t\le4, |h|t\le c\).
The first derivative is at most \(8K t=X_1t\). The second derivative
is at most twice
\((8KX_1+4cKX_1^2)t^2\). The third derivative is at most twice
\(\{12K(X_1^2+X_2)+4cK(X_1^3+3X_1X_2)\}t^3\).
These are exactly the first three recurrences in (IU37); hence

\[
 \sup_m\|x_m^{(r)}\|\le X_rt^r\quad(1\le r\le3).
 \tag{IU46}
\]

For \(a_h(x(h))\) in (IU40), both \(x(h)\) and
\(x(h)+s h g(x(h))\) are paths covered by (IU46). In the actual
telescoping expression their total Euler weights, including this extra
coefficient \(s\in[0,1]\), are less than \(4t\). The chain rule for
\(g(x(h))\) and \(Dg(x(h)+s h g(x(h)))\), through order three,
gives respectively the four bounds \(G_rt^r\) in (IU37). For the
second function this uses \(D^{r+1}g\), so \(D^4g\) is indeed needed.
Leibniz's rule, followed by integration over a unit interval, gives

\[
 \left\|\frac{d^r}{dh^r}a_h(x(h))\right\|
 \le A_rt^r\quad(0\le r\le3).
 \tag{IU47}
\]

For the interpolation in (IU41), its base \(C_hx(h)\) is also a
path covered by (IU46). Since

\[
 (h^2a_h)^{(r)}=h^2a_h^{(r)}+2rh a_h^{(r-1)}
                              +r(r-1)a_h^{(r-2)},
\]

the interpolated initial point of the remaining fine path has derivative
norm at most \(Z_rt^r\), using \(|h|t\le c\) and \(t\ge1\) to enlarge
the bounds. Apply (IU44) to at most \(2t\) fine microsteps, now with
these nonzero initial derivatives. The homogeneous product is still
less than two. At first order this gives \(T_1=2(Z_1+2K)\).
At second and third order the inhomogeneous sums give precisely the
\(T_2,T_3\) in (IU37). Thus the final and intermediate post-interpolation
states \(z(h)\) satisfy

\[
 \|z^{(r)}(h)\|\le T_rt^r\quad(1\le r\le3).
 \tag{IU48}
\]

By the chain rule, derivatives through order three of \(Dg(z(h))\)
and \(Df(z(h))\) have norms at most \(H_rt^r\) with \(H_r\) from
(IU37). The latter bound uses \(D^4f\).

It remains to bound the transported tangent \(w(h)\), initially
\(a_h(x(h))\). A fine step has tangent recurrence

\[
 w^+=w+hDg(z)w.
 \tag{IU49}
\]

Writing \(Dg(z)^{(q)}\) for its total derivative in \(h\), the exact
Leibniz formula is

\[
 \begin{split}
 (w^+)^{(r)}=w^{(r)}
 &+h\sum_{q=0}^r\binom rqDg(z)^{(q)}w^{(r-q)}\\
 &+r\sum_{q=0}^{r-1}\binom{r-1}q
                         Dg(z)^{(q)}w^{(r-1-q)}.
 \end{split}
 \tag{IU50}
\]

The \(q=0\) term in the first sum is the homogeneous factor.
Its product is bounded by (IU45). For \(r=0\), (IU47) therefore
gives \(\|w\|\le2A_0=W_0\). Inductively suppose the lower
derivatives satisfy \(\|w^{(q)}\|\le W_qt^q\). Sum the other
terms of (IU50) over at most \(2t\) fine steps, divide by \(t^r\),
and use \(|h|t\le c\). The first sum contributes at most
\(2c\sum_{q=1}^r\binom rqH_qW_{r-q}\); the second contributes
\(2r\sum_{q=0}^{r-1}\binom{r-1}qH_qW_{r-1-q}\).
The initial derivative is bounded by \(A_rt^r\). Multiplication by
the homogeneous bound two is exactly (IU38), so

\[
 \|w^{(r)}\|\le W_rt^r\quad(0\le r\le3).
 \tag{IU51}
\]

The scalar integrand of each transported defect is \(Df(z)[w]\).
A final Leibniz rule gives

\[
 \left|\frac{d^3}{dh^3}\bigl(Df(z(h))[w(h)]\bigr)\right|
 \le t^3\sum_{q=0}^3\binom3qH_qW_{3-q}=6C_Kt^3.
 \tag{IU52}
\]

Differentiation under the interpolation integral is justified by these
continuous, uniformly bounded derivatives on its compact interval.
There are exactly \(t\) defects, so

\[
 \sup_{|h|\le c/t}|Q_t'''(h)|\le6C_Kt^4.
 \tag{IU53}
\]

The expression (IU42) defines \(Q_t\in C^3\) also at zero. Because
\(d_t=h^2Q_t\) is odd, \(Q_t\) is odd, and consequently
\(Q_t(0)=Q_t''(0)=0\). The integrated third-order Taylor identity is

\[
 Q_t(h)-Q_t'(0)h
 =\frac12\int_0^h(h-s)^2Q_t'''(s)\,ds.
 \tag{IU54}
\]

Also \(Q_t'(0)=d_t'''(0)/6\), directly from \(d_t=h^2Q_t\).
Taking absolute values in (IU54), including negative \(h\), and
multiplying by \(h^2\) proves (IU39). This argument removes the exact
factor \(h^2\) before differentiating: three derivatives of each of
\(t\) local defects give \(t^4\). It uses no fifth derivative of an
unknown limiting output. \(\square\)

Apply (IU39) to the complete space (IU11), using (IU13), the parity
(IU20), and the explicit coefficient (IU35). This proves (IU6).

### 6. The unique local operator-state flow

Let \(K=K_L, T_L=1/(8K)\). We construct the solution of

\[
 \dot\theta(T)=g(\theta(T)),\qquad \theta(0)=\theta_0,
 \quad |T|\le T_L,
 \tag{IU55}
\]

in the Banach space (IU11). On continuous paths with
\(\sup_{|T|\le T_L}\|\theta(T)-\theta_0\|_{\mathcal X_L}\le1/2\),
the map

\[
 (\mathcal P\theta)(T)=\theta_0+\int_0^Tg(\theta(s))\,ds
 \tag{IU56}
\]

maps into the radius-\(1/8\) path ball. The integral is the Banach
integral of a continuous function, obtained by limits of Riemann sums
in the complete space. The mean-value integral and (IU13) bound the
Lipschitz constant of \(g\) on the convex unit ball by \(K\).
Consequently \(\mathcal P\) contracts the supremum path distance by
at most \(KT_L=1/8\). Iteration is a geometric Cauchy sequence in
the closed complete path ball, its limit is a fixed point, and the
same contraction proves uniqueness there. The fundamental theorem for
the continuous integral makes the limit \(C^1\) and proves (IU55).
Any other solution starting at \(\theta_0\) cannot leave the radius
\(1/2\) ball on this interval: before a first exit its displacement is
at most \(K|T|\le1/8\). Thus uniqueness has no extra path-ball
hypothesis for solutions on the stated interval.

In components this is the autonomous operator system

\[
 \dot a=x_L,\qquad \dot u=r_1,\qquad
 \dot P_a=r_a\otimes x_{a-1}\quad(2\le a\le L),
 \tag{IU57}
\]

with fields recomputed by (IU12). In particular its readout satisfies

\[
 \frac{d}{dT}f(\theta(T))
 =\|x_L\|^2+\|r_1\|^2
     +\sum_{a=2}^L\|r_a\|^2\|x_{a-1}\|^2.
 \tag{IU58}
\]

This is feature time for the metric (IU2); no physical-loss clock is
part of this construction.

For an explicit convergence argument, first take the positive uniform
grid \(h=T_L/m\). All Euler iterates through step \(m\) lie within
distance \(Kmh\le1/8\) of \(\theta_0\), by the same first-exit
argument. The local integral defect of the exact flow is bounded by

\[
 \left\|\theta(T+h)-\theta(T)-h g(\theta(T))\right\|
 \le\int_0^h K\|\theta(T+s)-\theta(T)\|\,ds
 \le K^2h^2/2.
 \tag{IU59}
\]

If \(e_k=\|E_h^k\theta_0-\theta(kh)\|\), then

\[
 e_{k+1}\le(1+Kh)e_k+K^2h^2/2,
 \qquad
 e_k\le\frac{Kh}{2}\{(1+Kh)^k-1\}
       \le\frac{Kh}{2}(e^{KT_L}-1).
 \tag{IU60}
\]

For negative time apply the same argument to the field \(-g\), or
replace \(h\) by \(|h|\) in the error recurrence. Linear interpolation
between Euler states changes the comparison by at most \(2K|h|\):
both the Euler segment and the exact flow move by at most \(K|h|\).
Thus the piecewise linear Euler paths on the positive and negative
grids converge uniformly on \([-T_L,T_L]\) in \(\mathcal X_L\).
The same estimate with \(h=T/m\) proves

\[
 E_{T/m}^m\theta_0\longrightarrow\theta(T)
                  \quad\hbox{in }\mathcal X_L,
             \qquad |T|\le T_L.
 \tag{IU61}
\]

By (IU15), these are precisely the operator representatives obtained
after the width limit for each fixed \(m,T/m\). The output and every
fixed polynomial contraction of the fields converge along this mesh
limit by continuity. The connector convergence in (IU61) is trace-norm
convergence in the fixed population spaces. No uniform-in-width bound
with a growing number of finite-width steps is asserted.

### 7. The scalar dyadic consequence

There is a useful summability statement directly from the sharper
step-doubling estimate. For \(|T|\le T_L\), put
\(G_t(T)=F_{t,L}(T/t)\), and abbreviate
\(D_L=L(L+1)^2(L+2)\). In (IU6) take \(h=T/(2t)\), which meets
its radius condition. Since \(t(2t-1)\le2t^2\),

\[
 |G_{2t}(T)-G_t(T)|
 \le\frac1t\left\{\frac{D_L|T|^3}{12}
                      +\frac{C_{K_L}|T|^5}{32}\right\}.
 \tag{IU62}
\]

The sum over \(t,2t,4t,\ldots\) is finite, uniformly for \(T\) on the
stated compact interval. Hence the scalar dyadic approximations are
uniformly Cauchy, with the explicit tail estimate

\[
 \left|f(\theta(T))-G_t(T)\right|
 \le\frac2t\left\{\frac{D_L|T|^3}{12}
                      +\frac{C_{K_L}|T|^5}{32}\right\}.
 \tag{IU63}
\]

The identification of the limit in (IU63) uses the already proved
operator-state convergence (IU61). Scalar summability by itself would
not supply existence or uniqueness of that state flow.

### 8. Boundary: bounded slopes do not give energy-ball activation stability

The positive theorem above uses the identity activation. A distinct
finite-dimensional obstruction explains why bounded activation slopes
alone cannot replace its polynomial Banach estimates.

Consider two hidden layers, one input \(x_1=1\), stored endpoint vectors
\(u,a\in\mathbb R^n\), and stored connector \(M\). For a common
activation \(\psi\), let

\[
 H=\psi(u),\qquad z=MH,\qquad
 f_\psi=\frac1n a^T\psi(z).
 \tag{IU64}
\]

Use the same raw metric as (IU2), so all blocks undergo simultaneous
feature ascent. Its first bottom Euler update, evaluated at the old
state, is exactly

\[
 u^+=u+h\,\psi'(u)\odot
             M^T\bigl(a\odot\psi'(M\psi(u))\bigr).
 \tag{IU65}
\]

Here \(\odot\) is coordinatewise multiplication. Define a distance
between activations by

\[
 d_1(\psi,\widetilde\psi)
 =\sup_{x\in\mathbb R}
       \frac{|\psi(x)-\widetilde\psi(x)|}{1+|x|}
       +\|\psi'-\widetilde\psi'\|_\infty.
 \tag{IU66}
\]

Take

\[
 \psi(x)=x+\arctan x,\qquad
 \widetilde\psi_n(x)=\psi(x)+n^{-1/2},\qquad
 u=0,\quad a=\sqrt n\,e_1,\quad
 M=\frac{e_1\mathbf1^T}{\sqrt n}.
 \tag{IU67}
\]

Both activations are smooth with the same positive slope
\(\psi'(x)=1+(1+x^2)^{-1}\in(1,2]\), and uniform linear-growth
and derivative bounds. Their distance is exactly \(n^{-1/2}\).
The initial energy quantities are fixed:

\[
 \frac{\|u\|_2}{\sqrt n}=0,\qquad
 \frac{\|a\|_2}{\sqrt n}=1,\qquad
 \|M\|_{\mathrm{op}}=1,\qquad
 1+\frac{\|u\|_2+\|a\|_2}{\sqrt n}+\|M\|_{\mathrm{op}}=3.
 \tag{IU68}
\]

For \(\psi\), \(H=z=0\); hence
\(M^T(a\odot\psi'(z))=2\mathbf1\) and
\(u^+=4h\mathbf1\). For \(\widetilde\psi_n\),
\(\widetilde H=n^{-1/2}\mathbf1\) and
\(\widetilde z=e_1\). The only coordinate selected by \(a\) has
\(\psi'(1)=3/2\), so

\[
 M^T(a\odot\widetilde\psi_n'(\widetilde z))
       =\tfrac32\mathbf1,\qquad
 \widetilde u^+=3h\mathbf1,\qquad
 \frac{\|\widetilde u^+-u^+\|_2}{\sqrt n}=|h|.
 \tag{IU69}
\]

Consequently, for any fixed nonzero feature step \(h\), no finite
constant depending only on the displayed energy bound, that step, and
the common activation bounds can control this first state difference
by \(d_1(\psi,\widetilde\psi_n)\), uniformly over widths and all states
in that energy ball. In particular a bound of the form
\(d_1 P(3)\), with a width-independent polynomial \(P\), tends to zero
and contradicts (IU69).

The failure occurs in the product of the readout and a slope difference.
The latter has Euclidean norm divided by \(\sqrt n\) of order
\(n^{-1/2}\), while multiplication by the concentrated readout makes
that norm order one. The connector operator-norm bound does not
remove this product.

This is a deterministic statement on an energy ball with a
width-dependent activation perturbation. It supplies no assertion
about Gaussian-typical initial states, expected-output continuity, or
a single final bounded-slope activation's uniform time remainder.
An averaged stability statement needs its own probabilistic argument.
