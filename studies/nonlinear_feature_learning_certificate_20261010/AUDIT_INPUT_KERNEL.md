# Focused audit: initial kernel and four-point input witness

Date: 2026-10-10.

Scope: the complete frozen input `INPUT_NONLINEARITY_RESULT.md` was read. This
audit checks Sections 1 and 2 directly. The quoted feature-learning theorem,
compression guarantees, and the network's stated zero-readout velocity
normalization are supplied inputs. No other study artifact, prior check, or
book passage was read. The time bootstrap and compression transfer are outside
this focused verdict.

**Verdict: PASS for Sections 1 and 2 under their full stated setup.** The
nonnegative power-series argument works at arbitrary fixed finite depth, the
affine-residual kernels are positive semidefinite, their training Gram matrices
converge to the identity, and the resulting velocity is non-affine for every
nonzero label vector. The deterministic four-point witness exists, and four
distinct points are the minimum possible support. No substantive mathematical
flaw was found in these arguments. The dimensional qualification at the end of
this report must be retained when extracting the result from its full setup.

## 1. The variance-scaled Gaussian recursion has unbounded positive support

Let \(G,G'\) be standard real Gaussians with correlation \(r\in[-1,1]\), and
let \(H_k\) be the Gaussian Hermite polynomials normalized to have unit
\(L^2\) norm. For a positive variance \(q\), expand the real activation as

\[
 \phi_\ell(\sqrt q\,G)=\sum_{k\ge0}\alpha_{\ell,k}(q)H_k(G).
\]

The bounded derivative gives

\[
 |\phi_\ell(z)|\le |\phi_\ell(0)|+M_\ell|z|,
\]

so this is an \(L^2\) expansion. Its support is infinite: finite Hermite
support would imply equality almost everywhere with a polynomial; continuity
and the strictly positive Gaussian density imply equality everywhere. A
polynomial with bounded derivative on the real line has degree at most one,
contrary to nonaffinity. Scaling the argument by \(\sqrt q>0\) does not change
this conclusion.

For completeness, the completeness argument quoted in the candidate is valid.
If an \(L^2\) Gaussian function \(h\) is orthogonal to every polynomial, then

\[
 z\longmapsto \mathbb E[h(G)e^{zG}]
\]

is entire, by Cauchy--Schwarz and Gaussian exponential moments, with all
derivatives at zero equal to zero. It vanishes identically, including on the
imaginary axis; uniqueness of the Fourier transform of the finite measure
\(h\,d\gamma\) gives \(h=0\) Gaussian-almost everywhere. The required Fourier
uniqueness can also be obtained by convolving that measure with Gaussian
densities: Fourier inversion gives zero convolutions, and their approximate
identity limit gives the zero measure.

The exponential generating function gives

\[
 \mathbb E[H_j(G)H_k(G')]=\mathbf 1_{j=k}r^k.
\]

Passing from finite Hermite sums to the expansion is valid by
Cauchy--Schwarz, including \(r=\pm1\). Consequently

\[
 A_{\ell,q}(r)
 :=\mathbb E[\phi_\ell(\sqrt q\,G)\phi_\ell(\sqrt q\,G')]
 =\sum_{k\ge0}\alpha_{\ell,k}(q)^2r^k.
\]

These are uncentered second moments, as required for the feature Gram kernel.
The coefficients are nonnegative, have unbounded positive support, and sum
to the finite positive number \(\mathbb E\phi_\ell(\sqrt q\,G)^2\).
Positivity holds because a continuous nonaffine activation cannot vanish
Gaussian-almost everywhere.

To make the recursion's variance dependence explicit, set

\[
 F_0(s)=s,\qquad q_{\ell-1}=F_{\ell-1}(1),\qquad
 F_\ell(s)=A_{\ell,q_{\ell-1}}
      \!\left(\frac{F_{\ell-1}(s)}{q_{\ell-1}}\right).
\]

Here \(q_0=1\), and every subsequent \(q_\ell\) is positive and finite by the
previous paragraph. This is the Gaussian layer recursion invoked in the
candidate. Suppose

\[
 \frac{F_{\ell-1}(s)}{q_{\ell-1}}
       =\sum_{j\ge0}e_j s^j,\qquad e_j\ge0,\quad\sum_j e_j=1.
\]

After expanding each power in the outer series, all coefficients remain
nonnegative. Their total sum is \(A_{\ell,q_{\ell-1}}(1)=q_\ell<\infty\).
The total absolute sum for every \(|s|\le1\) is bounded by this same number;
thus the expansion, regrouping, and uniform absolute convergence on the
whole interval are justified even with nonzero constant coefficients.

If \(e_j>0\) for some \(j\ge1\), every outer index \(k\) with
\(\alpha_{\ell,k}(q_{\ell-1})^2>0\) contributes at least

\[
 \alpha_{\ell,k}(q_{\ell-1})^2 e_j^k>0
\]

to degree \(jk\). The seed \(F_0(s)=s\) has such a positive-degree coefficient,
and the outer positive support is unbounded at every layer. Induction proves
the candidate's claim

\[
 F_L(s)=\sum_{k\ge0}c_k s^k,\qquad c_k\ge0,
 \qquad\sum_kc_k<\infty,
\]

with unbounded positive support. No uniformity in depth is being claimed or
needed; depth is fixed. Analyticity is not used in this kernel argument.

## 2. Removing affine functions preserves kernel positivity

Let \(\sigma\) be normalized surface measure on \(S^{d-1}\), with \(d\ge2\).
Its first two moments are

\[
 \int u\,d\sigma(u)=0,\qquad
 \int uu^\top\,d\sigma(u)=I_d/d.
\]

They verify directly that the candidate's operator

\[
 (Ph)(v)=\int h(u)\,d\sigma(u)
      +d\,v^\top\int u h(u)\,d\sigma(u)
\]

is the orthogonal projection onto restrictions of affine functions.

For \(K_k(v,u)=(v^\top u)^k\), rotational symmetry gives

\[
 \int z(z^\top u)^k\,d\sigma(z)
     =u\int(z^\top u)^{k+1}\,d\sigma(z).
\]

Therefore projection in the first variable gives exactly

\[
 P_vK_k(v,u)=a_k+b_kv^\top u,
 \quad a_k=\int(z^\top u)^k\,d\sigma(z),
 \quad b_k=d\int(z^\top u)^{k+1}\,d\sigma(z).
\]

Both coefficients are independent of the unit vector \(u\). The same formula
holds for \(P_uK_k\). The displayed affine kernel is unchanged by projecting
in either variable, hence

\[
 (I-P)_v(I-P)_uK_k=K_k-a_k-b_kv^\top u=R_k.
\]

For a direct positivity check, equip the tensor space with the inner product
for which

\[
 \langle v^{\otimes k},u^{\otimes k}\rangle=(v^\top u)^k,
\]

and apply \(I-P\) separately to each coordinate of \(v\mapsto v^{\otimes k}\).
Writing the resulting tensor-valued feature as \(\Psi_k(v)\) gives

\[
 R_k(v,u)=\langle\Psi_k(v),\Psi_k(u)\rangle,
 \qquad
 \sum_{a,b}y_a y_bR_k(v_a,v_b)
   =\left\|\sum_a y_a\Psi_k(v_a)\right\|^2\ge0.
\]

This verifies positive semidefiniteness without assuming that subtracting an
arbitrary positive affine kernel preserves positivity. The specific double
orthogonal projection is essential. As checks, \(R_0=R_1=0\).

## 3. The residual training Gram becomes positive definite

For \(d\ge2\), the two points \(z=\pm u\) have zero surface measure. Thus
\(|z^\top u|<1\) almost everywhere, and dominated convergence gives

\[
 a_k\longrightarrow0,\qquad b_k\longrightarrow0.
\]

In fact \(a_k\ge0\) and \(b_k\ge0\): odd moments vanish and even moments are
nonnegative. For the fixed finite training set, put

\[
 \rho=\max_{a\ne b}|v_a^\top v_b|<1.
\]

The symmetric residual Gram matrix obeys the explicit estimate

\[
 \left\|[R_k(v_a,v_b)]_{a,b}-I_m\right\|_{\mathrm{op}}
 \le (m-1)\rho^k+m(a_k+b_k)\longrightarrow0.
\]

Indeed the right side bounds every absolute row sum; symmetry then bounds
the operator norm. In particular, there is a finite \(k_0\) such that

\[
 [R_k(v_a,v_b)]_{a,b}\succeq\tfrac12 I_m
 \quad\text{for every }k\ge k_0.
\]

For the supplied zero-readout population velocity

\[
 g(v)=\frac2m\sum_a y_a F_L(v^\top v_a),
\]

suppose \(g\) were affine on the sphere. The operator \(I-P\) would annihilate
it. Since \(\|Ph\|_\infty\le(1+d)\|h\|_\infty\), uniform absolute
convergence justifies applying this operator term by term. Evaluation at the
training inputs and pairing with \(y\) yields

\[
 0=\frac2m\sum_k c_k
           \sum_{a,b}y_a y_bR_k(v_a,v_b).
\]

Every term is nonnegative. Unbounded positive support supplies an index
\(k\ge k_0\) with \(c_k>0\), and its contribution is at least
\(c_k\|y\|_2^2/m>0\). This is a contradiction.

The proof does not assume that labels are non-affine on the training set.
It applies even when they are restrictions of an affine function there.
It proves nonaffinity of the full function on the sphere, which can require
passive queries to observe.

## 4. A great circle and four points suffice

The reduction to a great circle is valid for every \(d\ge2\). To check it,
suppose that a function \(g\) is affine on every great circle. On each such
circle its antipodal average

\[
 \frac{g(v)+g(-v)}2
\]

is constant. Any pair of sphere points lies on a common great circle, so
this average is one global constant, say \(b\). The function \(h=g-b\) is
odd. Define

\[
 H(0)=0,\qquad H(x)=\|x\|_2h(x/\|x\|_2)\quad(x\ne0).
\]

On every two-dimensional linear subspace, the circle representation for
\(g\) has constant term \(b\), so \(H\) is linear on that subspace. Every pair
of vectors belongs to such a subspace, including collinear pairs after
enlarging their span. Therefore \(H(x+y)=H(x)+H(y)\); the same argument gives
\(H(\lambda x)=\lambda H(x)\) for every real scalar \(\lambda\). It follows
that \(H\) is linear on \(\mathbb R^d\), making \(g\) affine on the sphere.
The contrapositive supplies the required great circle for the non-affine \(g\).

On that circle choose three distinct points \(u_1,u_2,u_3\). A line meets
the sphere in at most two points, so these three are affinely independent.
They determine a unique affine function on the circle's two-dimensional
plane matching their \(g\)-values. Because \(g\) is not affine on the circle,
there is a distinct fourth point \(u_4\) at which this interpolant fails.
Write its unique affine coordinates as

\[
 u_4=\sum_{i=1}^3\lambda_i u_i,
 \qquad\sum_{i=1}^3\lambda_i=1.
\]

The coefficient vector

\[
 (-\lambda_1,-\lambda_2,-\lambda_3,1)
\]

annihilates constants and coordinates but has a nonzero pairing with the
four values of \(g\). Dividing by its positive sum of absolute values and,
if necessary, reversing its sign gives exactly the candidate's coefficients:

\[
 \sum_i|c_i|=1,\quad\sum_i c_i=0,\quad\sum_i c_i u_i=0,
 \quad\delta=\sum_i c_i g(u_i)>0.
\]

For any affine \(a^\top u+b\),

\[
 \left|\sum_i c_i h(u_i)\right|
 =\left|\sum_i c_i\bigl(h(u_i)-a^\top u_i-b\bigr)\right|
 \le\max_i|h(u_i)-a^\top u_i-b|.
\]

Taking the infimum proves (5). Rescaling to the physical inputs
\(x_i=\sqrt d\,u_i\) preserves both annihilation identities and the bound.
No realized weights or future trajectory enters this choice: the fixed
function \(g\) is determined by the population kernel and the fixed training
inputs and labels.

Finally, any set of at most three distinct sphere points is affinely
independent. Thus no nonzero coefficient vector on fewer than four distinct
points can annihilate both constants and all linear coordinates. The claimed
minimality is exact.

## Exact qualifications

- The implication from the training geometry to \(d\ge2\) uses at least two
  training inputs. The complete candidate explicitly uses \(m\ge2\) in
  Section 4. Under that setup there is no dimensional gap. An isolated
  statement that only says “every distinct pair is nonparallel” must also
  retain \(m\ge2\) or explicitly assume \(d\ge2\): for \(m=1,d=1\), the
  pairwise condition is vacuous and every function on \(S^0=\{-1,1\}\) is
  affine.
- The pairwise absolute-inner-product restriction matters. For example,
  with odd activations the kernel is odd in its correlation argument;
  antipodal training inputs with equal nonzero labels cancel in (3), giving
  \(g=0\). The proof correctly excludes this geometry.
- The proof supplies a strictly positive problem-dependent witness margin,
  not a lower bound uniform over data, activations, dimension, depth, or
  labels. It makes no claim that an arbitrary existing four-point panel
  works or that the chosen points can be found cheaply.
- This verdict establishes deterministic nonaffinity of the supplied
  population initial velocity and its finite witness. Finite-width kernel
  convergence, the time remainder, the inherited feature-learning result,
  and compression transfer require their separate checks. In particular,
  these sections alone do not prove that the later departure from the frozen
  kernel has a non-affine input component.
