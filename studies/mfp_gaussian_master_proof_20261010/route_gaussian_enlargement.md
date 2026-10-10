# Gaussian enlargement route and feedback clipping audit

This is a scoped independent proof route, using only the supervisor's stated
program. No Tensor Programs theorem or external research source was read for
this route. The conclusions below distinguish proved reductions from required
inputs.

The program has finitely many vector and scalar lines. Each vector has length
\(n\); roots are neuronwise independent copies of fixed Gaussian tuples.
Independent matrices have entries \(N(0,1/n)\), and a matrix and its transpose
may be reused. Coordinate functions and scalar functions are smooth, with
polynomial growth of every derivative. Scalar reductions are normalized means.
All constants and the instruction list are independent of \(n\).

Write
\[
 \|v\|_{n,q}=\left(\frac1n\sum_{i=1}^n |v_i|^q\right)^{1/q}.
\]

## 1. A proved upgrade from weak tightness to all moments

**Required premise for this route.** For every vector line \(v\) and every
finite \(q\geq1\), the family \(\|v\|_{n,q}\) is tight; every scalar line is
tight. This premise must cover the actual program, including its feedback.
The conclusion is that every such norm and scalar has uniformly bounded
moments of every finite order. Any scalar convergence in probability to a
finite deterministic limit therefore holds in every finite \(L^p\).

Represent all Gaussian inputs by a standard Gaussian vector \(\xi_n\).
Each matrix is a reshaping of a block of \(\xi_n/\sqrt n\), and each root tuple
is a fixed linear image of a block of \(\xi_n\). Singular root covariance is
allowed. The dimension of \(\xi_n\) is \(O(n^2)\).

Fix a desired norm exponent \(q\geq2\), a large exponent \(r\geq q\), and
a constant \(B\). A good input is one for which every vector line has
\(\|v\|_{n,r}\leq B\), every scalar has absolute value at most \(B\), and
every matrix has operator norm at most \(B\). Tightness allows \(B\) to be
chosen so that this good set has Gaussian probability at least \(1/2\) for
all sufficiently large \(n\). At a good input,
\[
 \|v\|_\infty\leq B n^{1/r},\qquad \|v\|_2\leq B\sqrt n.
\]

Compare this input with any \(\xi'_n\) satisfying
\(\|\xi'_n-\xi_n\|_2\leq t\), without requiring the second input to be good.
The matrix perturbation has operator norm at most \(t/\sqrt n\), and each
root perturbation has ordinary Euclidean norm at most \(Ct\).
Measure vector errors by ordinary Euclidean norm and scalar errors by
\(\sqrt n\) times their absolute value. Let \(E\) dominate the errors in all
previous lines. The next error obeys the following bounds.

* For a matrix line \(Wv\), or its transposed counterpart,
  \[
  \|W'v'-Wv\|_2
   \leq (B+t/\sqrt n)E+Bt.
  \]
* For a coordinate map with derivative growth degree \(d\), the fundamental
  theorem of calculus gives
  \[
  \|F(v',s')-F(v,s)\|_2
   \leq C(1+B n^{1/r}+E)^d E.
  \]
  Here the finite tuple of vector arguments is denoted by \(v\), and scalar
  arguments by \(s\). Broadcasting a scalar error contributes
  \(\sqrt n|s'-s|\leq E\). Constants absorb the finite number of arguments.
* For a normalized mean,
  \[
  \sqrt n\left|\frac1n\sum_i(v_i'-v_i)\right|\leq\|v'-v\|_2.
  \]
* A smooth scalar operation obeys the same polynomial error bound as a
  coordinate operation after multiplying its error by \(\sqrt n\).

Induction through the finite instruction list therefore gives an integer
\(K\), depending only on the program and its derivative growth degrees, such
that every final or intermediate error is bounded by
\[
 E\leq C_B n^{K/r}(1+t)^K.                                      \tag{1}
\]
One explicit induction rule is to replace a bound
\(C n^{a/r}(1+t)^b\) after a coordinate operation by a bound with exponents
\((d+1)\max(a,1)\) and \((d+1)\max(b,1)\); matrix operations only enlarge
these finite exponents. Thus (1) makes no unstated uniform regularity claim.

For \(q\geq2\),
\[
 \|v'-v\|_{n,q}\leq n^{-1/q}\|v'-v\|_2.
\]
Choose \(r>2Kq\), and take \(t=\sqrt{2D\log n}\) for any fixed \(D>0\).
Equation (1) then implies that all these normalized \(q\)-norm errors tend
to zero; scalar errors tend to zero as well. For exponents below two, use
\(\|v'-v\|_{n,q}\leq\|v'-v\|_{n,2}\).

The exact Gaussian enlargement inequality used here is: if a measurable set
\(A\) in a standard Gaussian space has probability at least \(1/2\), then
\[
 \mathbb P\{\operatorname{dist}(\xi,A)>t\}
 \leq 1-\Phi(t)\leq e^{-t^2/2},
\]
where \(\Phi\) is the standard normal distribution function. Applying it to
the good set proves, for sufficiently large \(n\),
\[
 \mathbb P\{\max_v\|v\|_{n,q}>B+1
       \text{ or }\max_s|s|>B+1\}\leq n^{-D}.                  \tag{2}
\]
This uses no quantitative rate in the tightness premise.

To justify moments on the exceptional set, define \(R_n\) as one plus the
sum of matrix operator norms and normalized Euclidean norms of all roots.
Every finite moment of \(R_n\) is bounded uniformly in \(n\). For roots this
follows from Gaussian moments and Jensen's inequality. For matrices, a
\(1/4\)-net of each unit sphere with at most \(9^n\) elements gives
\[
 \mathbb P\{\|W\|_{\rm op}>2u\}
 \leq 2\,9^{2n}e^{-nu^2/2};
\]
integration above any sufficiently large constant bounds every operator-norm
moment uniformly in \(n\).

Polynomial growth of the program's functions, ordinary Euclidean norm
bounds, and the finite instruction count give the global envelope
\[
 Z_n:=\max_v\|v\|_{n,q}+\max_s|s|
       \leq C n^A(1+R_n)^A                                  \tag{3}
\]
for some finite \(A\). For example, a coordinate map of growth degree \(d\)
is bounded in ordinary Euclidean norm by
\(C\sqrt n(1+\sum_v\|v\|_2+\sum_s|s|)^d\); this and the matrix operator
bound establish (3) recursively. Consequently
\(\mathbb E Z_n^{2p}\leq C_p n^{2Ap}\). By Cauchy--Schwarz, the contribution
of the exceptional set in (2) to \(\mathbb E Z_n^p\) is at most
\(C_p n^{Ap-D/2}\). Taking \(D>2Ap\) proves the asserted uniform moment
bound. The finitely many excluded widths have finite moments by (3).

Permutation equivariance also yields, for any fixed coordinate of a vector
line,
\[
 \mathbb E|v_i|^p=\mathbb E\|v\|_{n,p}^p,
\]
so coordinate moments are uniformly bounded. If a scalar \(s_n\) converges
in probability to \(s\), the uniform \((p+1)\)-moment bound gives uniform
integrability of \(|s_n-s|^p\), hence convergence in \(L^p\).

This also proves overwhelming-probability convergence at every fixed error
tolerance: add \(|s_n-s|\leq\varepsilon/2\) to the good set before applying
enlargement. It does not give a rate for the deterministic convergence bias.

## 2. What a deterministic-coefficient law alone does not yet settle

The preceding argument cannot start from a weak law for fixed deterministic
coefficients unless feedback tightness has first been proved. The tempting
step of freezing convergent random scalars and propagating normalized
Euclidean errors fails without further work: an unbounded coordinate
derivative needs higher empirical error norms, while a reused dense matrix
has no dimension-independent operator bound on normalized \(\ell^q\) for
\(q>2\).

A sufficient additional premise is a deterministic law stable under every
convergent deterministic coefficient sequence, for all finite coefficient
derivative programs, with locally bounded limiting moments. It implies
uniform tightness on compact coefficient sets by a subsequence contradiction.
The enlargement proof is then uniform on those sets and supplies uniform
moment bounds for the derivative programs.

These bounds yield the missing stochastic continuity directly. Put all
frozen coefficient slots in a finite-dimensional parameter vector \(\theta\).
Every mixed parameter derivative of an empirical output is another finite
program, because all activation derivatives have polynomial growth. On a
fixed parameter cube, repeated one-dimensional fundamental theorems of
calculus bound the supremum of a smooth function by a constant times the
integrals of all mixed derivatives using at most one derivative in each
coordinate. Applying this bound to the first derivatives of an empirical
output, and taking expectations, bounds its random Lipschitz constant in
probability. Therefore evaluation at \(\theta_n\to\theta_*\) in probability
has the same limit as evaluation at \(\theta_*\), even when \(\theta_n\)
depends on all matrices. A chronological induction freezes every feedback
slot. The corresponding Banach-valued bound for vector outputs supplies
their empirical norm tightness.

Pointwise laws at fixed \(\theta\), by themselves, do not justify the compact
uniformity or integration in this argument. This is an exact missing premise
of this route, not a proved consequence of such a pointwise law.

## 3. Audit of the proposed clipping route

The supervisor proposed a separate all-moment lemma, obtained by finite-entry
Taylor expansion, and a Gaussian limit theorem for globally Lipschitz
programs. Their proofs were not supplied within this route's input scope.
The following reduction is valid conditional on these two inputs.

For every coordinate or scalar map \(F\), let
\(F_B(x)=\chi(x/B)F(x)\), where \(B\geq1\), \(\chi\) is smooth, equals one
on the unit ball, and vanishes outside the ball of radius two. Clip the whole
finite program, including polynomial coordinate products and scalar feedback
maps, and couple the original and clipped programs using the same roots and
matrices. For each fixed \(B\), all clipped maps are bounded and globally
Lipschitz. Their polynomial derivative growth profiles can be chosen
independently of \(B\): Leibniz's rule introduces factors \(B^{-k}\leq1\),
and derivatives of the cutoff are bounded uniformly.

**Necessary uniformity of the all-moment input.** For every finite exponent,
the moment bound must hold uniformly in both \(n\) and \(B\), for every
original and clipped vector and scalar line. In particular, constants must
depend only on the common polynomial derivative profiles and architecture,
not on the clipped maps' growing global Lipschitz constants.

Let \(\mu_n\) be the product of the randomness law and uniform measure on
the neuron index. If an input error tends to zero in \(L^2(\mu_n)\) uniformly
in \(n\) as \(B\to\infty\), then it tends to zero in \(L^4(\mu_n)\):
interpolate the \(L^2\) norm with any uniformly bounded \(L^r\) norm for
\(r>4\). For a coordinate instruction, write
\[
 F(x)-F_B(x_B)
  =[F(x)-F(x_B)]+[1-\chi(x_B/B)]F(x_B).
\]
The polynomial Lipschitz bound and Hölder's inequality give
\[
 \|F(x)-F(x_B)\|_{L^2(\mu_n)}
 \leq C\|x-x_B\|_{L^4(\mu_n)}
       \|(1+|x|+|x_B|)^d\|_{L^4(\mu_n)}\longrightarrow0.
\]
The second term tends to zero uniformly by higher moments of \(x_B\): for
any chosen power, Markov's inequality bounds its squared expectation by that
negative power of \(B\), using a sufficiently high uniform moment. Scalar
arguments are broadcast in \(\mu_n\), so exactly the same bound handles
coordinate maps with scalar feedback inputs.

For a matrix instruction and its input error \(e\), no independence between
\(W\) and \(e\) is needed:
\[
 \begin{aligned}
 \mathbb E\|We\|_{n,2}^2
 &\leq (\mathbb E\|W\|_{\rm op}^4)^{1/2}
        (\mathbb E\|e\|_{n,2}^4)^{1/2}\\
 &\leq C\left(\mathbb E\frac1n\sum_i|e_i|^4\right)^{1/2}
 \longrightarrow0.
 \end{aligned}
\]
The second inequality is Jensen's inequality, and the convergence is the
interpolation just established. Normalized scalar means contract \(L^2\)
by Jensen's inequality. Smooth scalar instructions use the same
polynomial-Lipschitz argument with the randomness measure alone.

Induction through the fixed instruction list therefore proves
\[
 \sup_n\mathbb E\|v_n-v_{n,B}\|_{n,2}^2\longrightarrow0,
 \qquad
 \sup_n\mathbb E|s_n-s_{n,B}|^2\longrightarrow0.
\]
Higher \(L^p\) versions follow by interpolation with uniform higher moments.
This reduction has no rank-stability requirement.

For scalar convergence, let \(s_B\) be the deterministic limit supplied by
the clipped-program theorem. The uniform comparison makes \((s_B)\) Cauchy
and proves convergence of the original scalar to \(\lim_B s_B\). The final
identification of this limit with a stated, explicit, unclipped Gaussian
source-response recursion still needs to be supplied. If that recursion is
written using Gaussian covariances and derivative expectations without
matrix inverses, it can be audited by finite induction: couple finite
Gaussian vectors through continuous positive-semidefinite square roots, and
pass derivative expectations using uniform higher moments. A recursion using
pseudoinverses cannot be declared continuous merely because the clipped
programs converge.
