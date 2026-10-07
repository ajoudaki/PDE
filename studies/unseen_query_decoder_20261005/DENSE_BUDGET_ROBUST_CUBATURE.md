# Finite-seed robust cubature in covariance geometry

2026-10-06. Scoped author derivation. The numerical integration problem
has a finite-variance solution: independent median-of-means blocks, with
pairwise-independent Gaussian rows inside each block, give one retained-seed
event for all prescribed prefixes, sphere inputs and time patches. The row
functions need not satisfy a relative sub-Gaussian bound. Their large global
caps enter numerical precision, not the sample count.

The algorithm estimates the **unnormalized** capped-density integral.
There is no denominator to estimate. In the requested covariance norm its
clipping bias is at most \(B\sqrt e\), where \(|G|\le B\) and
\(e=\int(r-4)_+d\mu\le h/(\log4-1)\). Its numerical error can be
\(\varepsilon\) using
\(O(KRB^2\varepsilon^{-2}+K)\) row evaluations, where \(R\) is the
history dimension and \(K\) is logarithmic in a proof-only covering number.
For absolute-polylogarithmic parameters and root-width requested accuracy,
the complete work is \(n\operatorname{polylog}(n)=n^{1+o(1)}=o(n^2)\).
For a simpler assembly with fixed-depth propagation, the final specialization
uses numerical tolerance \(n^{-3/4}\): its work is
\(n^{3/2}\operatorname{polylog}(n)=o(n^2)\), with an absolute
polylogarithmic storage exponent. The uniform family includes all guarded
intermediate query moments, so the numerical event applies at seed-dependent
adaptive query arguments.

One numerical qualification remains explicit: applying an exact inverse
covariance norm requires a counted whitening/range representation. Known
real covariance moments alone do not certify that representation to the
required finite precision. The theorem below also works with a supplied
regularized covariance, with no new gap assumption on the unregularized
one. Its conclusion must then be stated in that regularized norm. The
supervisor's clarified interface supplies precisely \(A=Q+\tau I\),
with counted covariance precision and \(\log(1/\tau)\)
absolute-polylogarithmic. That interface resolves the whitening
qualification for this application's regularized geometry.

## 1. Measures, covariance and the target

Fix a current prefix and condition on its complete training tape. Let
\(\mu=N(0,I_D)\) be the Gaussian row law. A calibrated row law
\(\nu\ll\mu\) has density \(r\) and
\(D(\nu\Vert\mu)\le h\). Let \(F:\mathbb R^D\to\mathbb R^R\)
have a finite second-moment matrix under \(\nu\),

\[
                 Q=\int FF^T\,d\nu.
 \tag{1}
\]

Here \(Q\) is the **raw** second-moment matrix; no population or sample
centering is implicit. For a family of scalar tests \(G(z;\theta)\),
assume \(|G|\le B\), with \(B>0\). The parameter \(\theta\)
contains the unseen sphere query, a bounded physical-patch coordinate, and
**all** guarded intermediate query moments. Their number is at most the
absolute-polylogarithmic program size. The row and numerical bounds below
are required throughout this parameter set, not merely at exact moments.
The desired vector is

\[
                     v(\theta)=\int FG(\cdot;\theta)\,d\nu.
 \tag{2}
\]

For a positive-definite matrix \(A\succeq Q\), define
\(\|v\|_{A^{-1}}=\|A^{-1/2}v\|_2\). The exact covariance norm
is obtained by taking \(A=Q\) when \(Q\) is positive definite. If
\(Q\) is singular, use its positive range and its inverse there, subject
to a supplied counted range representation; Section 6 spells this out.

Set

\[
 w=\min(r,4),\qquad e=\int(r-w)d\mu,
 \qquad v_w(\theta)=\int wFG(\cdot;\theta)\,d\mu.
 \tag{3}
\]

The conditioning input proves
\(e\le h/(\log4-1)\). For completeness,
\(\int(r\log r-r+1)d\mu=D(\nu\Vert\mu)\), the integrand is
nonnegative, and on \(r>4\) it is at least \((\log4-1)r\).
Since \((r-4)_+\le r\mathbf1_{r>4}\), the asserted bound follows.

## 2. Clipping bias and weighted variance require only second moments

Put \(U=A^{-1/2}F\). Then
\(\int UU^T\,d\nu=A^{-1/2}QA^{-1/2}\preceq I_R\).
For any unit vector \(a\), Cauchy--Schwarz with the nonnegative measure
\((r-w)d\mu\) gives

\[
 \begin{aligned}
 |a^TA^{-1/2}(v-v_w)|
 &\le B\left[\int(r-w)d\mu\right]^{1/2}
           \left[\int(r-w)(a^TU)^2d\mu\right]^{1/2}\\
 &\le B\sqrt e.
 \end{aligned}
 \tag{4}
\]

The second inequality uses \(0\le r-w\le r\) and the covariance
bound for \(U\). Taking the supremum over unit \(a\) proves

\[
                \|v-v_w\|_{A^{-1}}\le B\sqrt e
                    \le B\sqrt{h/(\log4-1)}.
 \tag{5}
\]

This bias is dimension-free. It does not use a range bound for \(F\).
Normalization would introduce an additional, unnecessary error; (3) is
already a valid approximation to the desired probability-law expectation.

The whitened, weighted integrand is
\(Y(z;\theta)=w(z)U(z)G(z;\theta)\). Its raw second-moment matrix
under the easy prior satisfies

\[
 \int YY^T\,d\mu
 \preceq B^2\int w^2UU^T\,d\mu
 \preceq4B^2\int rUU^T\,d\mu
 \preceq4B^2I_R.
 \tag{6}
\]

The scalar inequality \(w^2\le4r\) proves the middle step. Therefore
every coordinate variance of \(Y\) is at most \(4B^2\), regardless
of the largest values of the whitened history functions. Neither an
empirical-Gram success event nor a relative sub-Gaussian condition is used.

## 3. Median-of-means with pairwise rows and independent blocks

First work with exact Gaussian rows. Take an odd number \(K\) of
independent blocks. In block \(j\), take \(s\) rows with marginal law
\(\mu\) that are pairwise independent. They need not be jointly
independent within the block. Set

\[
 M_j(\theta)=\frac1s\sum_{i=1}^sY(Z_{ji};\theta),\qquad
 m(\theta)=\int Y(\cdot;\theta)d\mu=A^{-1/2}v_w(\theta).
 \tag{7}
\]

Pairwise independence makes all distinct-row coordinate covariances zero.
By (6), for every coordinate \(a\),

\[
 \mathbb E|M_{j,a}(\theta)-m_a(\theta)|^2\le4B^2/s.
 \tag{8}
\]

For a specified net-point error \(\varepsilon_0>0\), choose

\[
                 s\ge64RB^2\varepsilon_0^{-2}.
 \tag{9}
\]

Chebyshev gives
\(\Pr\{|M_{j,a}-m_a|>\varepsilon_0/\sqrt R\}\le1/16\).
Take the median of the \(K\) block means separately in each coordinate;
call the resulting vector \(\widehat m\). If a coordinate median is
outside its required interval, at least \((K+1)/2\) independent blocks
are bad in that coordinate. A union over subsets of that many blocks bounds
this failure probability by

\[
 2^K(1/16)^{(K+1)/2}\le2^{-K}.
 \tag{10}
\]

Consequently, at any fixed \(\theta\),

\[
              \Pr\{\|\widehat m(\theta)-m(\theta)\|_2
                                  >\varepsilon_0\}\le R2^{-K}.
 \tag{11}
\]

At a finite family of \(J\) prefix/instruction/patch indices with
proof-only parameter nets of sizes \(M_1,\ldots,M_J\), choosing

\[
               R\left(\sum_{j=1}^J M_j\right)2^{-K}\le\beta/2
 \tag{12}
\]

controls all coordinate medians at all net points. There is no stored list
of these points. Each query stores only its \(K\) vectors of block means.

It is essential that **blocks** are independent. Merely making the whole
row sequence \(O(K)\)-wise independent does not justify independence of
bad-block indicators, since each indicator examines \(s\) rows. The
finite construction below supplies independent block seeds explicitly.

## 4. Finite seed, Gaussian coupling and a uniform query event

Choose an integer Gaussian cutoff \(T\ge1\) with

\[
                      T^2\ge2\log(4KsD/\beta).
 \tag{13}
\]

Let \(b\) be the number of uniform bits per Gaussian coordinate. Use
the input's binary field of degree
\(q=\max\{Db,\lceil\log_2(s+1)\rceil\}\). For each block
retain two independent uniform field elements \(A_j,B_j\), independently
over \(j\), and generate at row index \(i\)

\[
                         V_{ji}=A_ji+B_j.
 \tag{14}
\]

Any two distinct row values in a block are independent uniform field
elements: their evaluation map from \((A_j,B_j)\) is invertible because
the two indices differ. Different blocks are independent because their
seed pairs are independent. Use the first \(Db\) bits of each field
element as \(D\) uniform coordinate-cell indices. Evaluate the clipped
Gaussian quantile at each cell midpoint.

For a proof coupling only, append independent uniforms inside those cells
and apply the untruncated Gaussian quantile. The resulting exact rows are
pairwise independent Gaussians within each block and independent across
blocks. Thus (8)--(12) apply. Their chance that any one of the \(KsD\)
coordinates exceeds \(T\) in absolute value is at most \(\beta/2\)
by (13) and the Gaussian tail. These extra uniforms are not part of the
algorithm or its retained information.

On the complementary event the clipped quantile equals the exact quantile
at the coupled uniform. Its global Lipschitz constant is at most
\(\sqrt{2\pi}e^{T^2/2}\). The finite computed and exact Gaussian row
coordinates therefore differ by at most

\[
                         \sqrt{2\pi}e^{T^2/2}2^{-b}+\zeta,
 \tag{15}
\]

where \(\zeta\) is the quantile evaluation error. Supply uniform local
row-Lipschitz and amplitude bounds for the coordinates of \(Y\) on
\([-T-1,T+1]^D\). Choosing (15) sufficiently small controls every
block-mean coordinate to any specified tolerance. Function evaluation and
accumulation errors receive their own shares of that tolerance. Accumulating
\(s\) entries costs an additional \(O(\log s)\) precision bits.

Coordinate medians are one-Lipschitz under uniform perturbations of their
input lists: if every entry changes by at most \(a\), the two sorted
middle entries differ by at most \(a\), because at least half of each
list is below its median and at least half above it. Hence entrywise
block-mean rounding error at most \(\varepsilon/(8\sqrt R)\) changes
the vector median by at most \(\varepsilon/8\). The final small-matrix
multiplication is budgeted to the same requested whitened-output accuracy.

For uniformity between net points, assume a supplied common Hölder exponent
\(0<a\le1\) and bounds
\(|Y_b(z;\theta)-Y_b(z;\theta')|\le L_{\rm row}
\|\theta-\theta'\|^a\) on this Gaussian cube, and
\(|m_b(\theta)-m_b(\theta')|\le L_{\rm mean}
\|\theta-\theta'\|^a\). The median inherits the former coordinate
Hölder bound, by its one-Lipschitz property. A parameter mesh at most

\[
 \left[\frac{\varepsilon}
 {8\sqrt R(L_{\rm row}+L_{\rm mean})}\right]^{1/a}
 \tag{15a}
\]

makes the total vector extension error at most \(\varepsilon/8\).
For a sphere times a guarded box of dimension \(p\) and coordinate
ranges at most \(M\), a cube grid gives
\(\log M_{\rm net}\le C(d+p)\log(2+C\sqrt{d+p}M/h_{\rm mesh})\).
Thus \(p\) may itself be absolute-polylogarithmic: if the logarithms
of the ranges and Hölder constants are too, then the logarithm of the net
size remains an absolute power of \(\log n\). The net is proof-only.
A uniform row Hölder bound for \(G\) also gives an integral Hölder
bound by Cauchy--Schwarz and \(\int w(a^TU)^2d\mu\le1\).

The supervisor's query interface has the important nonsmooth case
\(\beta_q=\max\{0,c-b^TCb\}\) and a row response of the form
\(\chi(\mu_q+\sqrt{\beta_q}\,g)\), where \(\mu_q\) and
\(\beta_q\) are the scalar Gaussian mean and variance. On a guarded box, the quadratic map
inside the maximum is Lipschitz, with a counted constant; the positive
part is one-Lipschitz, and
\(|\sqrt u-\sqrt v|\le\sqrt{|u-v|}\) for \(u,v\ge0\).
For sampled \(|g|\le T\), a bounded derivative of \(\chi\) therefore
gives a row Hölder bound with exponent \(a=1/2\), including at zero
variance. Formula (15a) merely squares the mesh tolerance. Its logarithm
and the block count (12) remain absolute-polylogarithmic. Large row
Lipschitz/Hölder constants only affect these logarithms and precision.

Take \(\varepsilon_0=\varepsilon/2\) in (9). The sampling error,
Gaussian coupling, evaluation, accumulation, net extension and final
linear algebra can thus sum to at most \(\varepsilon\), after harmless
constant tightening. The resulting vector output satisfies

\[
 \sup_{j,\theta}
           \|\widehat v_j(\theta)-v_j(\theta)\|_{A_j^{-1}}
        \le\varepsilon+B\sqrt{h/(\log4-1)}
 \tag{16}
\]

on one seed event of probability at least \(1-\beta\). For nonsingular
\(A\), the exact recomposition is \(\widehat v=A^{1/2}\widehat m\).
Section 6 describes the singular version and precision requirements.

As in the earlier coupling lemma, (16) is ultimately a statement about
the finite seed alone. A seed whose implemented output is bad cannot be
paired with proof-only within-cell uniforms on which all the preceding
sufficient good events hold. Its failure probability is therefore at
most the joint seed/uniform failure probability. There is no population
Gaussian truncation bias: the block concentration concerns exact Gaussian
rows and their original means; the cutoff is used only to couple a finite
implementation to those rows on a high-probability event.

The seed is independent of the complete acquired tape, including its
tilt parameters, normalizers and covariance representation. Averaging the
conditional seed bound over training gives one joint event for every
prefix, sphere input, physical-time patch and guarded intermediate-moment
argument. Given the seed, answers are deterministic and repeatable. A
terminal frozen patch includes the endpoint if supplied by the existing
physical construction. Adaptive selection of later test inputs, and
seed-dependent intermediate query moments that remain in the guarded
domain, are covered directly by the same event.

## 5. Complete cost and storage accounting

There are \(Ks=O(K[1+RB^2\varepsilon^{-2}])\) row evaluations for
each vector integral. The seed contains \(2Kq\) random bits and the
fixed irreducible field polynomial. The latter can be chosen in the
already permitted preprocessing. Field evaluation in (14) costs
\(O(q^2)\) elementary bit operations using schoolbook multiplication.
Gaussian quantile generation has polynomial cost in \(T^2\), \(b\)
and its output precision, by the existing explicit numerical construction.
An entire Gaussian row, a vector integrand, and all small matrices count.

The live numerical state consists of the seed, \(K\) block means in
\(\mathbb R^R\), one current row, current small-matrix scratch, counters,
and accumulators. Coordinatewise sorting costs \(O(RK\log K)\)
comparisons and polynomial precision work. It requires neither all sampled
rows nor any parameter net to be stored.

Let \(W_n\) be a complete upper bound on one row evaluation, including
the finite-field/quantile work, whitening, evaluation of \(wFG\), every
activation call and the precision just specified. Let \(T_0\) count
coefficient construction, recomposition and sorting. Then

\[
 T_{\rm query}\le T_0+
             C K[1+RB^2\varepsilon^{-2}]W_n.
 \tag{17}
\]

For a polylogarithmic number of sequential query moment calls, include all
of them in \(W_n\) or sum their versions of (17); omitting this factor
would not count a whole query. The concentration events may share one seed.
Because their parameter nets cover every guarded intermediate-moment
argument, no fresh independence is needed when a later call uses earlier
seed-dependent numerical summaries. For an exact query operator \(T\),
the event gives \(\|\widehat T(u)-T(u)\|\le\varepsilon\)
simultaneously for all guarded \(u\). Hence it holds at computed
\(\widehat u\), and

\[
 \|\widehat T(\widehat u)-T(u)\|
 \le\varepsilon+\|T(\widehat u)-T(u)\|.
 \tag{17a}
\]

Only the stability of the exact expectation map is needed to propagate
errors in (17a). A large rowwise or empirical Lipschitz constant is not
inserted into that recurrence. Median stability is used for the numerical
net extension, where its logarithm affects the block count. Here \(T\)
is the exact capped-density integral being numerically evaluated. If one
instead uses the original \(\nu\)-integral in (17a), add its uniformly
bounded clipping error (5) to the local tolerance. This separates numerical
error from the statistical-scale bias.

Suppose \(D,R,B,K,W_n,T_0\), the relevant instruction counts and all
logarithmic precision parameters are bounded by absolute powers of
\(\log(en)\), and
\(\varepsilon^{-1}\le C\sqrt n\log^a(en)\) for an absolute
\(a\). Equation (17) is at most \(Cn\log^b(en)\) for an absolute
\(b\). Since \(\log^b(en)/n\to0\), this is strictly \(o(n^2)\),
and hence within \(O(Ln^2+dn)\) for the original fixed \(L,d\).
It is stronger than a bound with any fixed exponent between one and two.
Storage, including the seed and precision, is an absolute power of
\(\log n\). Constants may depend on the fixed admissible data and
confidence.

The cube/net/block choices can be ordered without a circular definition:
use the provisional total-row cap \(Ks\le n^2\) to select (13), then
the local bounds, net, \(K\), and \(s\). The estimate above verifies
that cap for all sufficiently large individual widths. Logarithms of local
Lipschitz and amplitude bounds on that cube must be included in this check.

As throughout the source theorem, primitive time counts the fixed
activation evaluation primitives. A bit-time statement additionally needs
polynomial-time activation, data and query-input precision interfaces.
The former polynomial-space interface does not alone establish this.

### A fixed tolerance that leaves quadratic slack after fixed-depth propagation

The clarified assembly may take \(\varepsilon=n^{-3/4}\), independent
of depth, and \(B\le C\log^{3/2}(en)\). With all other numerical
parameters in the displayed absolute-polylogarithmic class, (17) becomes

\[
                T_{\rm query}\le C n^{3/2}\log^b(en)=o(n^2),
 \tag{17b}
\]

where \(b\) is absolute. All finite prefix/layer/patch indices and all
guarded intermediate coordinates are already included in (12) and in the
complete per-query cost. The Gaussian cutoff satisfies \(T^2=O(\log n)\)
after using the eventual \(Ks\le n^2\) cap. A block-row index has at
most \(2\log_2 n+O(1)\) bits. Neither the number of samples nor the
depth-dependent amplification is stored as a table.

Here is the local Gaussian smoothing identity that distinguishes the exact
expectation map from a samplewise square-root map. For a twice continuously
differentiable scalar \(\chi\) with bounded first and second derivatives,
define
\(H(a,v)=\mathbb E_g\chi(a+\sqrt v\,g)\), \(g\sim N(0,1)\),
for \(v\ge0\). Gaussian integration by parts gives

\[
 \partial_v H(a,v)=\tfrac12\mathbb E_g\chi''(a+\sqrt v\,g)
                         \quad(v>0),
 \qquad
 |H(a,v)-H(a',v')|
 \le\|\chi'\|_\infty|a-a'|
                +\tfrac12\|\chi''\|_\infty|v-v'|.
 \tag{17c}
\]

Indeed differentiating at positive \(v\) gives
\(\mathbb E[g\chi'(a+\sqrt v g)]/(2\sqrt v)\), and integration
of the Gaussian density derivative turns its numerator into
\(\sqrt v\mathbb E\chi''(a+\sqrt v g)\). The boundary terms vanish
because \(\chi'\) is bounded. Integrate this derivative in \(v\);
continuity at zero follows from the bounded first derivative and
\(\mathbb E|g|<\infty\). The mean-coordinate bound follows by the
mean value theorem. Thus zero innovation variance does not cause a
square-root loss in the exact weak expectation. Multiplying by a
history-dependent factor and integrating the history preserves this
calculation whenever its displayed derivative bounds are integrable;
the covariance bounds above provide the required first-moment control
for the whitened factors.

The supervisor's proposed physical interface supplies a fixed-depth weak
propagation bound \(A_n\le C\log^{CL}(en)\) in the relevant covariance
norms. This global physical bound is an input to the present numerical
assembly, not a conclusion from the scalar identity alone. Once it holds,
(17a) and the uniform oracle guarantee make the final numerical error at
most

\[
 A_n n^{-3/4}\le C\log^{CL}(en)n^{-3/4}=o(n^{-1/2})
                                      \quad\hbox{for each fixed }L.
 \tag{17d}
\]

The implication follows because \(CL\log\log(en)-(1/4)\log n\to-\infty\).
The width threshold may depend on \(L\). Its influence on required
precision is \(\log A_n=O(L\log\log n)\), with \(L\) in the allowed
fixed-parameter constant, not in the absolute storage exponent. Choosing
the numerical tolerance independently of \(A_n\) avoids a sample count
containing \(\log^{2CL}n\); the full numerical count is (17b).

## 6. Covariance precision: the exact residual qualification

The statistical proof needs no lower eigenvalue bound. A finite numerical
implementation nevertheless has to produce the action of a whitening map
and its inverse to the assigned tolerances. Two fully specified interfaces
suffice:

* A supplied symmetric positive-definite \(A\succeq Q\), whose dimension,
  finite input precision, logarithmic norm and logarithmic inverse gap are
  absolute-polylogarithmic. The fast small-matrix procedures then evaluate
  \(A^{-1/2}\) and \(A^{1/2}\) at counted polynomial cost. The guarantee
  is in the explicitly displayed \(A^{-1}\) norm. If \(A\succeq\tau I\),
  an absolute Euclidean recomposition error at most
  \(\varepsilon\sqrt\tau/8\) contributes at most \(\varepsilon/8\)
  in that norm; this only adds logarithmic inverse-gap precision.
* For the exact singular covariance norm, a supplied rank-\(r_0\)
  factorization \(Q=TT^T\) with full-column-rank \(T\), a certified
  range containing \(F\) almost surely under \(\nu\), and a counted
  left-inverse action on that range. Set \(U=T^\dagger F\), so
  \(\mathbb E_\nu UU^T=I_{r_0}\), carry out the preceding estimator
  in \(r_0\) coordinates, and return \(T\widehat m\). Then
  \(\|T a\|_{Q^\dagger}=\|a\|_2\), giving the exact requested
  covariance norm. All range, factor and inverse precisions count.

In the singular case, the range condition follows mathematically from
(1): a null vector of \(Q\) annihilates \(F\) \(\nu\)-almost surely.
It also annihilates the weighted prior integrand \(wF\) because \(w\le r\).
What is not supplied by this identity is a numerically certified rank or
range basis. If the original tilt is strictly positive, the same range
condition holds \(\mu\)-almost surely as well.

A regularized choice \(A=Q+\tau I\), with a certified approximation
retaining a comparable positive margin, avoids imposing a gap on \(Q\).
For \(\log(1/\tau)\) absolute-polylogarithmic, its inverse and square
root have the required cost. This gives the regularized norm, not a silent
claim about \(Q^\dagger\). A comparison with the physical geometry
must use precisely that norm or prove an additional comparison.

For a supplied covariance with usable gap \(a>0\), one direct sufficient
rounding condition is \(\|\widehat Q-Q\|_{\rm op}\le\theta a\)
with fixed \(\theta<1\), after which an appropriate positive buffer
gives a Loewner-comparable matrix. The needed entrywise accuracy and all
matrix-function errors cost logarithmic inverse-gap bits. A relative
Loewner certificate or an already factored covariance can be a stronger
interface. Merely saying that the exact moments in (1) are known does not
provide any of these finite-precision certificates.

The large row caps do not otherwise obstruct this sampler. For a cached
tilt, \(w=\exp[\min(\lambda^TF-\psi,\log4)]\); the map from log
density to \(w\) is four-Lipschitz. Thus sufficiently accurate evaluation
of its log density controls the absolute weight error. To control the
whitened integrand, allocate its error after multiplication by the supplied
local bound on \(\|A^{-1/2}F\|\), not merely by the bound on \(G\).
If the logarithms of these local bounds are absolute-polylogarithmic,
the required precision is too. The magnitude of \(F\) is never charged
as a sampling-variance factor in (17).

## 7. Consequence and remaining physical work

For \(h=H/(\alpha n)\), the proved vector integration error is

\[
           \varepsilon+
                 B\sqrt{\frac{H}{\alpha n(\log4-1)}}.
 \tag{18}
\]

This is of root-width times polylogarithmic size when \(B\) and \(H\)
have the specified sizes. It is not automatically less than an arbitrarily
chosen smaller tolerance; clipping and numerical errors must both fit the
actual physical error budget. In particular it does not assert the old
literal additional remainder \(1/n\).

With the supervisor's fixed-depth weak propagation interface, the clipping
contribution is at most \(C\log^{C_L}(en)/\sqrt n\) for some finite
fixed-depth exponent \(C_L\), while (17d) makes numerical integration
error \(o(n^{-1/2})\). If the accompanying physical posterior-to-row
comparison has that same stated statistical scale, the assembled bound
is of the form

\[
 2b_n+\frac{C\log^{C_L}(en)}{\sqrt n}+o(n^{-1/2})=O(b_n).
 \tag{19}
\]

For each fixed nonzero admissible label size \(Y\), the inherited
certificate contains \(n^{-1/2}\exp(cY^2\sqrt{\log(en)})\) times
a logarithmic factor with a fixed positive \(c\). It eventually
dominates every fixed power of \(\log n\), since
\(C_L\log\log(en)-cY^2\sqrt{\log(en)}\to-\infty\).
Zero labels are handled by the original exact zero predictor. Thus this
absorption does not impose a new label restriction. Equation (19) changes
the displayed error constant and does not claim the exact old
\(2b_n+1/n\) remainder.

The finite-variance numerical integration mechanism is now explicit and
uniform. It does not need the empirical-Gram event used in
`DENSE_BUDGET_SELF_NORMALIZED.md`, because it returns a robust block
estimator rather than a single unrestricted empirical mean. It also avoids
clipping whitened rows at a leverage threshold. The original population
second moment already bounds each block variance, and independent blocks
supply confidence.

What remains outside this lemma is obtaining the calibrated law and its
covariance representation from the present acquired state, connecting the
collective posterior query to that row law, propagating these particular
covariance-norm errors through adaptive query instructions, and preserving
the whole physical trajectory with its original label allowance. No dense
oracle, scalar-training replay, or future-response table is supplied by
the cubature construction.

Status: (4)--(18) prove a conditional finite-seed covariance-norm cubature
theorem with counted resources and a precise covariance-interface
qualification. Scientific files read for this task were the complete
`DENSE_BUDGET_CONDITIONING.md` and the author's already read/written
`DENSE_BUDGET_SELF_NORMALIZED.md` and `DENSE_BUDGET_SAMPLING.md`; the
supervisor's explicit problem statement supplied the new target. Subsequent
supervisor messages supplied the regularized covariance interface, full
guarded moment box, fixed numerical tolerance and proposed weak physical
propagation bound used in the final conditional assembly. Required skills
remain current, with the already authorized notation fallback.
Only this new assigned note was written. No experiment, external source,
other study, or Git operation was used.
