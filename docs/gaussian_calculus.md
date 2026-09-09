# Gaussian reuse and finite-order flow calculus

This chapter establishes two elementary building blocks for calculations of
deep-network dynamics: the response retained when a Gaussian matrix is reused,
and exact derivatives along a gradient direction. Use [the shared notation](NOTATION.md).
These statements do not assert convergence of an infinite Taylor series or a
width-dependent number of adaptive matrix calls.

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
