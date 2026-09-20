# Polynomial upper gate and a complete candidate landscape proof

Date: 2026-09-19. Author: scoped independent agent `p2_polynomial_gate`.

Status: **candidate proof, self-audited; no independent review or promotion**.
This version was developed without seeing another route's proof or verdict.
Scientific inputs were exactly the supervisor's prompt. Process inputs were
`solve-math-rigorously`, `investigate-conjectures`, its research-contract,
adversarial-audit and proof-search references, and `RESEARCH_WORKFLOW.md`.
No other scientific repository file, study, chat, external source or experiment
was used. Git HEAD/index/status were inspected only for write coordination.
Only this assigned file was written; the index was not changed.

## 1. Contract and conclusions

Let `(Omega_1,nu_1)` be a nonatomic probability space and let
`b_1 : Omega_1 -> R^{p_1}` be bounded and measurable. Let
`b_2 : Omega_2 -> R^{p_2}` have coordinate span exactly

\[
 V=\mathcal P_d(X_1,X_2),\qquad
 X=(\tanh G_1,\tanh G_2),\qquad d\geq1,
\]

where `d` is a finite positive integer and `G` is a nondegenerate real Gaussian
vector. Here coordinate span means
equality of subspaces of real random variables modulo almost-sure equality;
redundant coordinates of `b_2` are allowed. In particular each coordinate is
a real polynomial in `X`, so `b_2` is bounded. The Gaussian mean is arbitrary.

Take any finite `n >= 1`, unit vectors `u_i in R^2` such that
`u_i != +/-u_j` for `i != j`, weights `mu_i > 0`, and real labels `y_i`.
The full trainable parameter space and predictions are

\[
 (w,M,c)\in L^2(\nu_1;\mathbb R^2)
 \times\mathbb R^{p_2\times p_1}\times L^2(\nu_2),
\]
\[
 a_i(w)=\mathbb E_1[b_1\tanh(w\cdot u_i)],\qquad
 z_i=b_2^TMa_i,\qquad
 f_i=\mathbb E_2[c\tanh z_i],
\]
\[
 L(w,M,c)=\sum_{i=1}^n\mu_i(f_i-y_i)^2.
\]

Local minima are taken in the product of the two stated `L^2` norm topologies
and the Euclidean matrix topology. No claim about convergence of gradient flow,
gradient descent, initialization, or an infinite-time limit is made.

The candidate proves:

1. **Requested upper gate, in a stronger form.** Let `W` be any real polynomial
   subspace containing a nonconstant polynomial, let `p in W`, and let
   `q_1,...,q_n` be any finite list of real polynomials. On any probability law
   with full support on an open set,
   \[
   \operatorname{sech}^2(p)W
   \not\subseteq\operatorname{span}\{\tanh q_1,\ldots,\tanh q_n\}.
   \tag{1}
   \]
   There is no degree bound, no requirement `1 in W`, and no distinctness
   assumption on the `q_j`. Constants among the `q_j` are allowed.
2. **Physical lower gate.** For every `C^1` function of the finite moment array
   `(a_i)`, a local minimum over the full `w` space forces every moment gradient
   to vanish in the effective mark span. The proof uses actual small-support
   changes of `w`; it does not replace `a_i` by freely trainable vectors.
3. **Landscape conclusion.** If `nu_1(|b_1|>0)>0`, every local
   minimum of `L` has `L=0`, and zero loss is attainable for every label vector.
   If `b_1=0` almost surely, the model is identically zero and every parameter
   is a global minimum with loss `sum_i mu_i y_i^2`.

The proof first establishes the polynomial gate, then obtains the physical
lower gate by a positive planar smoothing representation of `tanh`, and finally
uses exact readout-null paths. The cases where the effective upper image consists
only of constants or is zero are handled separately.

## 2. Polynomial upper gate

All polynomial identities below are identities in the ordinary variables
`x in R^m`; the application has `m=2`. A law with full support on a nonempty
open set `U` has the following elementary property: a continuous function that
vanishes almost surely vanishes on `U`. Otherwise its nonzero value at one
point persists in a small open ball, which has positive probability.

### 2.1 The pole argument

**Lemma.** For real polynomials `p,q_1,...,q_n` with `p` nonconstant, neither
`sech^2(p)` nor `p sech^2(p)` belongs to the real linear span of the functions
`tanh(q_j)` on any nonempty real open set.

**Proof.** Choose a real affine line `x=x_0+t v` intersecting the open set in
an interval on which `P(t)=p(x_0+t v)` is a nonconstant polynomial. Such a line
exists: the highest nonzero homogeneous part of `p` is nonzero at some real
direction `v`; translating the base point does not change that highest
coefficient. Write `Q_j(t)=q_j(x_0+t v)`.

Suppose one of the asserted relations holds, and let `R(t)=1` or `R(t)=P(t)`
respectively. On the real interval we would have

\[
 \frac{R(t)}{\cosh^2 P(t)}
   =\sum_{j=1}^n\alpha_j\frac{\sinh Q_j(t)}{\cosh Q_j(t)}.
 \tag{2}
\]

Multiplication by `cosh^2(P) prod_j cosh(Q_j)` makes (2) an identity between
entire functions of a complex variable. An entire function vanishing on a real
interval is zero everywhere: a nonzero analytic function has isolated zeros,
as seen by factoring out the first nonzero coefficient of its local power
series. Thus (2) is a meromorphic identity throughout the complex plane.

Let `E` be the union of the zeros of `P'` and the zeros of `Q_j'` for those
`Q_j` which are nonconstant. This is a finite set. For every integer `k`, the
nonconstant complex polynomial equation

\[
 P(t)=\mathrm i\pi(k+1/2)
\]

has a solution by the fundamental theorem of algebra. Solutions for distinct
`k` are distinct, so infinitely many such solutions exist. Choose one `t_0`
outside `E`, and write `P(t_0)=i pi(k+1/2)`.

The function `cosh(P(t))` has a simple zero at `t_0`, because

\[
 \frac{d}{dt}\cosh P(t_0)=\sinh(P(t_0))P'(t_0)\neq0.
\]

Also `R(t_0) != 0`: this is immediate for `R=1`, and every half-integer
imaginary multiple of `pi` is nonzero for `R=P`. The left side of (2) therefore
has a pole of exactly order two at `t_0`.

Every term on the right has at most a simple pole there. A constant `Q_j` is
a real constant and contributes an entire constant. For nonconstant `Q_j`,
either `cosh Q_j(t_0) != 0`, or its derivative at a zero is
`sinh(Q_j(t_0))Q_j'(t_0) != 0`, so its zero is simple. A finite sum of functions
with poles of order at most one cannot have a pole of order two: multiplication
by `(t-t_0)^2` gives limit zero for the sum and a nonzero limit for the left
side. This contradicts (2). QED.

No generic rank assertion enters the argument. Critical points are excluded
by a finite set, while there are infinitely many available poles.

### 2.2 Constant arguments and arbitrary polynomial subspaces

**Lemma.** A nonconstant real polynomial `v` cannot belong to the span of any
finite collection `tanh(q_j)` on a nonempty open set.

**Proof.** Restrict to an affine real line on which `v` is nonconstant and
which meets the open set in an interval. The alleged identity extends to
the whole real line: multiplication by `prod_j cosh(Q_j)` gives an entire
identity, and none of these denominators vanishes on the real line. Its
right side has absolute value at most `sum_j |alpha_j|`, because every
`Q_j` is real on that line. A nonconstant real polynomial is unbounded in
absolute value along the real line. QED.

Now prove (1). If `p` is nonconstant, choose `v=p in W` and apply Section 2.1.
If `p` is a real constant, choose any nonconstant `v in W`; multiplication
by the positive constant `sech^2(p)` preserves its nonconstant character, and
Section 2.2 applies. This proves the stronger subspace assertion.

For the requested `V=P_d`, one can choose `v=1` whenever `p` is nonconstant,
and `v=x_1` whenever `p` is constant. In particular the assertion covers
`p=0`, lists of zero arguments, repeated arguments, opposite arguments, and
nonzero constant functions in the right-hand span.

The nondegenerate Gaussian assumption supplies the required support in the
application: a nondegenerate Gaussian has positive density on `R^2`, and
coordinatewise `tanh` is a continuous bijection from `R^2` onto `(-1,1)^2`
with continuous inverse. Every open ball contained in the square consequently
has positive `X` probability. Thus almost-sure identities of the stated
polynomial/analytic functions imply their identities on the open square.

## 3. A physical lower gate on the circle

The following argument uses equal input norms and distinct input directions
modulo sign. It is specific to the physical first-layer input geometry in the
contract; it is not an assumption of independently trainable moment columns.

### 3.1 A positive radial smoothing kernel

Put

\[
 g(s)=\tfrac12\operatorname{sech}^2 s,
 \qquad
 \rho(r)=-\frac1\pi\int_r^\infty
       \frac{g'(s)}{\sqrt{s^2-r^2}}\,ds,
 \qquad r\geq0.
 \tag{3}
\]

Since `g'(s)=-sech^2(s)tanh(s)<0` for `s>0`, `rho(r)>0` for every finite
`r`. The integral is finite. At positive `r` the lower endpoint singularity
is integrable of order `(s-r)^(-1/2)`; at `r=0`, `-g'(s)/s` has finite limit
one; and the integrand decays exponentially at infinity.

The density `x -> rho(|x|)` on `R^2` has one-dimensional projection density
`g`. Indeed, for `t>=0`, polar substitution and interchange of nonnegative
integrands give

\[
\begin{aligned}
 \int_{\mathbb R}\rho(\sqrt{t^2+y^2})\,dy
 &=2\int_t^\infty\rho(r)\frac{r}{\sqrt{r^2-t^2}}\,dr\\
 &=-\frac2\pi\int_t^\infty g'(s)
   \left[\int_t^s
    \frac{r\,dr}{\sqrt{r^2-t^2}\sqrt{s^2-r^2}}\right]ds\\
 &=-\int_t^\infty g'(s)\,ds=g(t).
\end{aligned}
\tag{4}
\]

The bracketed integral equals `pi/2`: substitute
`q=(r^2-t^2)/(s^2-t^2)`, obtaining
`(1/2) int_0^1 [q(1-q)]^(-1/2)dq=pi/2`; the last equality follows by
`q=sin^2(theta)`. The same formula holds for negative `t` by symmetry.
Nonnegative integration is legitimate before any integrability conclusion;
the resulting marginal integrates to one, since the antiderivative of `g`
is `(1/2)tanh`. Thus (3) defines a probability density, strictly positive
everywhere, and rotational invariance gives the same marginal in every unit
direction.

Let `xi` have this planar density. The cumulative distribution of any unit
projection is `(1+tanh s)/2`, and therefore, for every unit vector `u`,

\[
 \mathbb E\operatorname{sign}((v+\xi)\cdot u)
   =\tanh(v\cdot u).
 \tag{5}
\]

The value of `sign(0)` is immaterial because the projection has a density.

### 3.2 No finite global extremum for a nonzero ridge combination

For real numbers `kappa_i`, define

\[
 H(v)=\sum_i\kappa_i\tanh(v\cdot u_i),
 \qquad
 T(x)=\sum_i\kappa_i\operatorname{sign}(x\cdot u_i).
\]

The finitely many distinct lines `x dot u_i=0` divide the plane into open
angular chambers, on each of which `T` is constant. If some `kappa_i != 0`,
`T` is nonconstant across these chambers: crossing the `i`th line at a
nonzero point changes only its sign, and changes `T` by either `2 kappa_i`
or `-2 kappa_i`. Let `m` and `M` be the minimum and maximum of
the finite chamber values; then `m<M`.

By (5), `H(v)=E T(v+xi)`. The shifted density is positive on every open
chamber, so

\[
 m<H(v)<M\quad\hbox{for every finite }v.
\]

If `theta` is a direction strictly inside a minimum chamber, then
`H(R theta) -> T(theta)=m` as `R -> infinity`, by the ordinary limits of
each of the finitely many hyperbolic tangents. Hence `inf H=m`, and it is
not attained at any finite point. The maximum statement is identical.

Consequently, if a function `sum_i kappa_i tanh(v dot u_i)` has a global
minimum at a finite vector, all its coefficients `kappa_i` must vanish.

### 3.3 Needle variations force all effective moment gradients to vanish

Define

\[
 G_1=\mathbb E_1[b_1b_1^T],\qquad B=\operatorname{range}G_1.
\]

Then `b_1 in B` almost surely and every `a_i in B`. To see this, the kernel
of `G_1` consists exactly of vectors `h` with `h dot b_1=0` almost surely,
because `h^T G_1 h=E(h dot b_1)^2`; a finite basis of this kernel gives the
simultaneous almost-sure statement. The range of a real symmetric matrix
is the orthogonal complement of its kernel.

**Needle lemma.** Let `F : (R^{p_1})^n -> R` be `C^1` on a neighborhood of
the current moment array `A=(a_1,...,a_n)`. If `w` is a local minimum of
`F(A(w))` in `L^2(nu_1;R^2)`, then

\[
 P_B\nabla_{a_i}F(A)=0\qquad\text{for every }i.
 \tag{6}
\]

**Proof.** Write `beta_i=grad_{a_i}F(A)`. For a fixed vector `v in R^2`, put

\[
 D_v(\omega)=\sum_i(\beta_i\cdot b_1(\omega))
 [\tanh(v\cdot u_i)-\tanh(w(\omega)\cdot u_i)].
\]

Suppose `D_v<0` on a set of positive measure. For some `epsilon>0` and
finite `R`, the set `E={D_v<=-epsilon, |w|<=R}` has positive measure: the
negative set is the countable union of such sets with `epsilon=1/k` and
integer `R`, up to the null set where `w` is not finite. Nonatomicity gives
measurable subsets `E_j` of `E` with positive measures tending to zero.
For completeness, successively split a positive-measure nonatomic set into
two positive-measure pieces and retain the smaller; its measure is at most
half its predecessor's measure.

Replace `w` by `v` on `E_j` and leave it unchanged elsewhere. The resulting
`w_j` is in `L^2` and

\[
 \|w_j-w\|_2\leq(|v|+R)\nu_1(E_j)^{1/2}\longrightarrow0.
\]

Boundedness of `b_1` gives `|A(w_j)-A(w)|=O(nu_1(E_j))`. First-order
differentiability of `F` therefore yields

\[
 F(A(w_j))-F(A(w))
   =\int_{E_j}D_v\,d\nu_1+o(\nu_1(E_j))
   \leq-\epsilon\nu_1(E_j)+o(\nu_1(E_j))<0
\]

for large `j`, contradicting local minimality. Hence `D_v>=0` almost surely
for each fixed `v`.

Apply this conclusion to the countable dense set `v in Q^2`, discard their
combined null set, and then use continuity in `v`. For almost every `omega`,
the finite vector `w(omega)` is a global minimizer over all real `v` of

\[
 \sum_i(\beta_i\cdot b_1(\omega))\tanh(v\cdot u_i).
\]

Section 3.2 forces `beta_i dot b_1(omega)=0` for every `i`. Equivalently
`beta_i in ker G_1=B^perp`, proving (6). QED.

This proof uses no pointwise differentiability of an `L^2` Nemytskii map and
no unproved claim of local surjectivity of the finite moment map.

## 4. The exact readout-null argument

Fix a local minimum `(w,M,c)` and put

\[
 r_i=\mu_i(f_i-y_i),\qquad
 S=\operatorname{span}\{\tanh z_1,\ldots,\tanh z_n\}
   \subset L^2(\nu_2).
\]

Define the **current effective image**, without enlarging it, by

\[
 W=\{b_2^TMh:h\in B\}\subset V.
 \tag{7}
\]

Since every `a_i in B`, every current `z_i` belongs to `W`.

For fixed `M,c`, the loss is a `C^1` function of the finite array `A`.
Differentiation under `E_2` is justified by boundedness of `b_2`, boundedness
of derivatives of `tanh`, and `E|c|<=||c||_2`. Its moment gradients are

\[
 \nabla_{a_i}L
   =2r_iM^T\mathbb E_2[c\,b_2\operatorname{sech}^2 z_i].
 \tag{8}
\]

Take any `k in S^perp`. For every real `epsilon`, replacing `c` by
`c+epsilon k` leaves every prediction and the loss exactly unchanged.
For sufficiently small `epsilon`, the new point is still in a local-minimum
neighborhood of the original point and is itself a local minimum. Explicitly,
if the original point minimizes on a ball of radius `delta`, every equal-loss
point in that ball minimizes on its own sufficiently small ball contained
in the original ball.

Apply (6) and (8) first at `c` and then at `c+epsilon k`, and subtract. For
every `h in B`,

\[
 r_i\,\mathbb E_2[
  k\operatorname{sech}^2(z_i)b_2^TMh]=0.
 \tag{9}
\]

The residuals and `z_i` are exactly the same at both points. No differentiation
of the orthogonality space `S^perp` is performed; that space is fixed at the
current arguments throughout this exact path.

If `r_i != 0`, equation (9), for all `k in S^perp`, implies

\[
 \operatorname{sech}^2(z_i)W\subseteq S.
 \tag{10}
\]

Indeed the functions on the left are bounded, hence in `L^2`, and the
orthogonal complement of `S^perp` is `S` because `S` is finite-dimensional
and therefore closed.

If `W` contains a nonconstant polynomial, (10) contradicts (1), with
`p=z_i in W` and `q_j=z_j`. Therefore **every residual is zero whenever
the current effective image contains a nonconstant polynomial**.

The following section proves the remaining cases without pretending that
`W` equals the full mark span `V`.

## 5. Constant and zero effective images

### 5.1 Nonzero constant image

Suppose `W` consists of constants and is not zero. There is then a unique
nonzero vector `ell in B` such that

\[
 b_2^TMh=\ell\cdot h\quad\text{almost surely for every }h\in B.
\]

This is just the representation of a linear functional on a finite-dimensional
Euclidean space. Consequently `z_i=s_i=ell dot a_i` are constants, and, with
`kappa=E_2 c`,

\[
 f_i=\kappa\tanh s_i.
\]

The physical needle lemma applied to the loss gives

\[
 2r_i\kappa\operatorname{sech}^2(s_i)\ell=0
 \qquad\text{for all }i.
 \tag{11}
\]

If `kappa != 0`, then `ell != 0` and `sech^2(s_i)>0` imply `r_i=0`.

Suppose instead `kappa=0`. At the fixed `M,c`, **every** first-layer function
`w'` gives zero predictions, since its moment columns still belong to `B`
and its upper arguments remain constants. Thus every sufficiently close
`(w',M,c)` has exactly the same loss and is a local minimum. Here
`r_i=-mu_i y_i` is independent of `w'`.

At each of these local minima, differentiate the loss along the allowed
readout shift `c -> c+t 1`. The derivative at zero must vanish, so

\[
 H(w')=\sum_i r_i\tanh(\ell\cdot a_i(w'))=0
 \tag{12}
\]

for every `w'` in an `L^2` neighborhood of `w`. Thus `w` is a local minimum
of the scalar function `H`, which is constant on that neighborhood. Apply
the needle lemma to its finite moment function. Its `i`th gradient is

\[
 r_i\operatorname{sech}^2(s_i)\ell\in B.
\]

This gradient must vanish; again `ell != 0` implies `r_i=0` for every `i`.

### 5.2 Zero effective image

Suppose `W={0}`. For the fixed matrix `M`, all first-layer functions and all
readouts give `z_i=0` and `f_i=0`. Every nearby pair `(w',c')` therefore
gives an equal-loss local minimum with this `M`, and `r_i=-mu_i y_i` stays
fixed.

Choose `c'` arbitrarily close to `c` such that

\[
 q=\mathbb E_2[c'b_2]\neq0.
\]

This is possible with a constant shift `c'=c+epsilon 1`: since `1 in V`,
some vector `d` satisfies `d^T b_2=1` almost surely, so
`d^T E b_2=1` and `E b_2 != 0`. The affine vector
`E[c b_2]+epsilon E b_2` can be zero for at most one value of `epsilon`.
Choose the shift within the original local-minimum neighborhood.

For every sufficiently close `w'`, stationarity in the full matrix direction
`Delta M=q h^T`, where `h in B`, gives

\[
 0=\frac12D_ML[\Delta M]
   =|q|^2\sum_i r_i\,h\cdot a_i(w').
 \tag{13}
\]

Here `tanh'(0)=1` was used. Thus the scalar function
`J_h(w')=sum_i r_i h dot a_i(w')` vanishes throughout a neighborhood of `w`.
Applying the needle lemma to `J_h` gives `r_i h=0` for all `i` and all
`h in B`. If `B != {0}`, choose one nonzero `h` to conclude that every
`r_i=0`.

Finally, `B={0}` is equivalent to `b_1=0` almost surely, in which case
`a_i=z_i=f_i=0` at every parameter, and the loss is constant globally.

This exhausts all possibilities for the exact current effective image (7).
Because every `mu_i>0`, vanishing of all `r_i` is equivalent to `f_i=y_i`
for every sample and hence to zero loss.

## 6. Zero loss is attainable when the lower marks are nonzero

This section prevents the landscape statement from hiding an interpolation
assumption or a nonexistent optimizer.

Suppose `B != {0}` and choose `h in B\setminus{0}`. The random variable
`h dot b_1` is not identically zero modulo null sets, so there is a measurable set `E` with

\[
 \gamma=\mathbb E_1[1_E\,h\cdot b_1]\neq0.
\]

For example choose its positive or negative set, one of which has nonzero
integral. Choose a vector `v in R^2` outside the finitely many lines

\[
 v\cdot u_i=0,\qquad
 v\cdot(u_i-u_j)=0,\qquad
 v\cdot(u_i+u_j)=0\quad(i\neq j).
\]

Every displayed line is proper by the input assumptions, so their finite
union cannot fill the plane. Set `w=v 1_E`, which is in `L^2`. Then

\[
 s_i=h\cdot a_i=\gamma\tanh(v\cdot u_i)
\]

are nonzero and have pairwise distinct absolute values. This uses strict
monotonicity of `tanh` and its oddness. Choose `d_x` with
`d_x^T b_2=X_1`, and set `M=d_x h^T`. Then `z_i=s_i X_1`.

The functions `tanh(s_i x)` are linearly independent on `(-1,1)`. To prove
this, take an alleged nonzero relation and choose the participating index
with largest `|s_i|`. At

\[
 t_0=\frac{\mathrm i\pi}{2|s_i|},
\]

its term has a simple pole, while every term with smaller absolute slope
is analytic, since the magnitude of its imaginary argument is strictly
less than `pi/2`. The meromorphic identity argument in Section 2.1 gives
a contradiction. Repetition removes all coefficients.

The law of `X_1` has full support on `(-1,1)`. Therefore the Gram matrix

\[
 K_{ij}=\mathbb E_2[\tanh(s_iX_1)\tanh(s_jX_1)]
\]

is positive definite: a vector in its nullspace would give an almost-sure
zero linear combination, hence a zero combination on the interval by
continuity, contradicting independence. For `alpha=K^{-1}y`, take

\[
 c=\sum_j\alpha_j\tanh(s_jX_1).
\]

This bounded readout belongs to `L^2` and gives `f_i=(K alpha)_i=y_i`.
Thus the global optimum zero is attained for arbitrary real labels.

## 7. Assumptions, checks, and exact scope

The argument is deterministic and exact; no numerical evidence or asymptotic
limit is used. Its elementary background facts are finite-dimensional linear
algebra, first-order differentiability, integration of nonnegative functions,
the fundamental theorem of algebra (a nonconstant complex polynomial takes
every prescribed complex value), and the elementary identity theorem explained
in Section 2.1. No specialized external theorem is imported.

The following possible failure points were checked explicitly:

- **Constant upper arguments:** handled by polynomial unboundedness for the
  upper gate and by Sections 5.1--5.2 for the landscape proof.
- **Critical polynomial poles:** only finitely many points are excluded;
  infinitely many distinct pole preimages remain.
- **Repeated/opposite upper arguments:** no independence assumption is used
  for the readout feature span or in the pole gate.
- **Redundant or singular marks:** the exact effective span `B` is used; no
  positive-definite covariance assumption on the given coordinate list is
  imposed.
- **Zero lower marks:** retained as an explicit globally constant model case.
- **Unbounded first-layer weights:** each adverse needle set is first restricted
  to `|w|<=R`; every actual perturbation is small in the stated `L^2` topology.
- **Finite matrix bottleneck:** the argument uses the image (7), not the full
  polynomial mark span. It never assumes generic full rank or `p_1>=n`.
- **Flat directions:** equal predictions are verified exactly before using
  neighboring points as local minima. The readout-null subspace is frozen at
  the current `z_i`; it is not moved implicitly.
- **Square-loss convention:** gradients retain the factor two appropriate to
  the unhalved loss; residuals are `r_i=mu_i(f_i-y_i)`.
- **Attainment and arbitrary labels:** Section 6 supplies an explicit finite-
  norm interpolant when the lower marks are nonzero.

The physical conditions doing substantive work are full freedom to change `w`
on small measurable sets, nonatomicity, bounded lower marks, unit planar inputs
distinct modulo sign, unrestricted finite matrix variations, unrestricted
`L^2` readout variations including constants, and an upper polynomial mark
space containing constants and a nonconstant coordinate under a law with open
support. Changing these conditions requires a new argument. In particular the
proof does not infer the same conclusion for frozen/readout-constrained training,
unequal input norms, duplicated antipodal samples with arbitrary labels, or
fixed finitely many first-layer particles.

The upper gate itself is more general: arbitrary polynomial degrees and any
number of variables work, provided the measure has open support and the chosen
subspace contains a nonconstant polynomial. The complete physical proof above
uses only degree one in its explicit interpolant and therefore applies in
particular to the requested degrees two and three.

Registry recommendation: **complete candidate awaiting independent audit**.
No unresolved implication remains within the stated contract in this attempt;
the entire chain is persisted here for adversarial reconstruction. This status
does not assert independent checking, formal verification, or establishment in
the repository's canonical material.
