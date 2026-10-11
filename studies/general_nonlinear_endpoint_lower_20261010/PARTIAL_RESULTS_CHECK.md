# Independent check of the endpoint partial lemmas

2026-10-10. Independent isolated mathematical review of the four frozen inputs
listed below. **Verdict: the four requested partial results are correct with
the hypotheses and scope stated below. They do not prove an endpoint lower
bound for a network whose hidden weights are trained.** No experiment or
paper edit was performed.

The complete inputs read were `paper/compact.tex`,
`paper/compact_fitting.tex`, `LINEAR_RESPONSE_ROUTE.md`, and
`POSITIVE_ROUTE.md`. Required rigorous-math and canonical-notation instructions,
including the neural-network reference, were also read. No study README,
historical source, previous review, or other reviewer's findings was read.
In particular, the descriptions of older arguments in Section 1 of
`POSITIVE_ROUTE.md` are not independently certified by this review; those
older arguments are outside the supplied input boundary. The included TeX
dependencies other than `compact_fitting.tex` were not inputs.

The SHA-256 hashes of the reviewed files are:

| Input | SHA-256 |
| --- | --- |
| `paper/compact.tex` | `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `LINEAR_RESPONSE_ROUTE.md` | `6a3908239553f21875241bfad6592e7bf2e266f27b9bac6c85d1a3010e75f89f` |
| `POSITIVE_ROUTE.md` | `878feb73cf04c9e2240f05b04bc86f81e9180ba93470f2b45802d9c215ea273f` |

## 1. Population augmented Gram: correct, with explicit nonaffinity

Write the unit training directions as \(v_a=x_a/\sqrt d\),
\(a=1,\ldots,m\), and fix a unit query \(v_*\ne\pm v_a\).
The augmented index set is \(I=\{1,\ldots,m,*\}\). Its population Grams are
\[
Q^{(0)}_{ab}=v_a^\top v_b,
\qquad
Q^{(\ell)}_{ab}
=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
\qquad Z\sim N(0,Q^{(\ell-1)}).
\]
These are uncentered feature second moments; their later use as covariances
of fresh Gaussian preactivations is part of this recursion.

For the claim that every augmented \(Q^{(\ell)}\), \(\ell\ge1\), is
positive definite, the route assumes all directions in \(I\) are distinct
modulo sign and every activation is nonaffine, analytic, and globally
Lipschitz. A globally Lipschitz polynomial is affine, so these activations
are nonpolynomial.

Here is the decisive first-layer step. Suppose
\(\sum_j c_j\phi(w^\top v_j)=0\) in Gaussian \(L^2\).
Continuity and the full support of the standard Gaussian imply this identity
at every \(w\). For an index \(k\) with \(c_k\ne0\), define
\(b_j=v_k-(v_k^\top v_j)v_j\), \(j\ne k\). The derivative
\(D_{b_j}\) annihilates the \(j\)-th ridge function. Since these constant
directional derivatives commute, applying their product leaves
\[
c_k\prod_{j\ne k}\bigl[1-(v_k^\top v_j)^2\bigr]
\phi^{(|I|-1)}(w^\top v_k)=0.
\]
The coefficient is nonzero. As \(w^\top v_k\) ranges over the real line,
this would make \(\phi\) a polynomial. Thus the ridge functions are
linearly independent, proving strict positivity of their uncentered Gram.

At every subsequent layer, a positive-definite input covariance gives a
Gaussian density positive everywhere. If a linear combination
\(\sum_j c_j\phi(z_j)\) vanishes almost surely, continuity makes it vanish
everywhere. Varying one coordinate at a time forces its coefficient to zero
because \(\phi\) is nonconstant. This proves the induction.

The optional weaker argument in Section 3 of `LINEAR_RESPONSE_ROUTE.md`
is also correct. Without separating the training directions from one another,
the query remains outside their feature span at layer 1: apply the product
of the \(m\) directional derivatives orthogonal to the training directions
but not the query direction to any alleged exact representation of the query
feature. A vanishing innovation would force \(\phi_1^{(m)}\equiv0\).
This is a contradiction. The finite-dimensional feature span is closed, so
failure of exact representation means a strictly positive squared distance.

For any later Gaussian vector, write its training covariance and query
cross-covariance as \(S\) and \(q\). Positive semidefiniteness gives
\(q\in\operatorname{range}(S)\): if \(Sc=0\), the Gaussian variable
\(c^\top Z_{\rm train}\) vanishes almost surely, so \(c^\top q=0\).
Gaussian regression therefore gives
\[
Z_*=q^\top S^\dagger Z_{\rm train}+\sigma\xi,
\qquad \sigma>0,
\qquad \xi\sim N(0,1),
\]
where \(\xi\) is independent of the possibly degenerate training vector.
The positive innovation from the preceding layer is exactly \(\sigma^2\).
For a continuous nonconstant activation,
\(\operatorname{Var}(\phi(\mu+\sigma\xi))>0\) for every real \(\mu\).
Conditional variance then bounds from below the squared error of every
linear prediction of the new query feature by the new training features.
Innovation consequently propagates. If the final training block is positive
definite, its positive query Schur complement makes the final augmented Gram
positive definite, even if some earlier training blocks are singular.

Scope qualifications:

- Nonaffinity is an added hypothesis of these partial lemmas. The displayed
  activation assumptions in `compact.tex` itself permit affine activations.
  No claim of strict augmented positivity follows for that larger class.
- The matrices proved strictly positive are population Grams. An empirical
  augmented feature Gram has rank at most \(n\), and cannot be positive
  definite when \(n<m+1\). Convergence gives positive definiteness with
  probability tending to one as \(n\to\infty\) for a fixed positive
  population gap.
- The last Gaussian preactivation has positive query innovation because
  \(L\ge2\). A first-layer query lying in the input span need not have
  Gaussian innovation before the first nonlinearity.

## 2. Frozen-feature and finite-depth initialization endpoints: correct

Let \(H\in\mathbb R^m\) and \(H_*\in\mathbb R\) be the top-layer
population training and query features. Define
\[
Q=\mathbb E HH^\top\succ0,
\quad q=\mathbb E HH_*,
\quad b=Q^{-1}q,
\quad \alpha=Q^{-1}y,
\quad y\ne0.
\]
The influence in the note is
\[
\Psi=(H_*-b^\top H)(H^\top\alpha),
\qquad V=\mathbb E\Psi^2.
\]
It has mean zero because \(q-Qb=0\), and all its finite moments exist by
linear activation growth and Gaussian moments. Conditional on the training
preactivations, the query feature has strictly positive conditional variance
by Section 1. Hence
\[
V\ge
\mathbb E\left[(H^\top\alpha)^2
  \operatorname{Var}(H_*\mid Z_{\rm train})\right]>0,
\]
where strictness uses
\(\mathbb E(H^\top\alpha)^2=y^\top Q^{-1}y>0\).
No sign, centering, or label-direction exception was omitted.

For iid copies \((H_i,H_{*,i})\), set
\(Q_n=n^{-1}\sum_iH_iH_i^\top\),
\(q_n=n^{-1}\sum_iH_iH_{*,i}\), and
\(F_n=q_n^\top Q_n^{-1}y\). With fixed hidden features, the paper's
readout flow is
\[
\dot w_i=-\frac2m\sum_a(f_{n,a}-y_a)H_{a,i},
\qquad f_{n,a}=\frac1n\sum_iw_iH_{a,i},
\qquad w(0)=0.
\]
Therefore the training prediction obeys
\(\dot f_n=-(2/m)Q_n(f_n-y)\), and direct integration gives the query
endpoint \(F_n\) when \(Q_n\) is invertible. The zero readout and factors
of \(n,m\) match the canonical paper exactly.

Writing \(R_i=H_{*,i}-b^\top H_i\), the identity
\[
F_n-q^\top Q^{-1}y
=\left(\frac1n\sum_iR_iH_i\right)^\top Q_n^{-1}y
\]
is exact. Both empirical deviations on the right are of order
\(n^{-1/2}\) in probability. On the event
\(\lambda_{\min}(Q_n)\ge\lambda_{\min}(Q)/2\), the inverse identity
\[
Q_n^{-1}-Q^{-1}=-Q_n^{-1}(Q_n-Q)Q^{-1}
\]
makes the replacement of \(Q_n^{-1}y\) by \(\alpha\) cost
\(O_{\mathbb P}(n^{-1})\). Thus
\[
\sqrt n\,(F_n-q^\top Q^{-1}y)
\Longrightarrow N(0,V),
\qquad
\sqrt n\,(F_n-\widetilde F_n)\Longrightarrow N(0,2V)
\]
for independent runs. The empirical singularity event has probability
tending to zero by the law of large numbers and the positive population gap.

The actual finite-depth initialization extension has no missing independence
step. Given the lower-layer features, the top preactivation rows are iid
Gaussian with covariance their empirical augmented Gram \(S_n\).
Their conditional distribution depends on those features only through
\(S_n\), so conditioning on \(S_n\) alone also gives the stated iid law.
Independent runs remain independent after conditioning on their respective
lower-layer covariances.

The induction \(S_n\to S_0=Q^{(L-1)}\) in probability is valid even for
singular intermediate covariances. On bounded covariance sets, conditional
feature-product variances are bounded, so conditional Chebyshev controls
the empirical error. Coupling the Gaussian inputs by \(S^{1/2}g\), continuity
of the positive square root and linear activation growth prove continuity
of the population feature map, including at singular covariances.

For a deterministic covariance sequence \(S_n\to S_0\), write \(Q(S)\)
and \(q(S)\) for the corresponding top population blocks and
\(F(S)=q(S)^\top Q(S)^{-1}y\). The inverse stays bounded near \(S_0\).
The influences have convergent variances and uniformly bounded absolute
third moments: their third powers require at most sixth feature moments,
which are uniformly bounded by Gaussian moments. Expanding the characteristic
function therefore proves the triangular central limit theorem with limit
variance \(V\). The inverse remainder remains
\(O_{\mathbb P}(n^{-1})\) uniformly near \(S_0\).

Uniform convergence of the distribution functions follows from continuity
of the limiting normal distribution. Its local uniformity in \(S\) follows
by contradiction: a failing sequence of widths and covariances approaching
\(S_0\) would contradict the just-proved triangular theorem. Consequently
the conditional distribution-function error tends to zero in probability
for the random covariances, and in mean because the error is bounded.

For two runs, centering by \(F(S_n)-F(\widetilde S_n)\) leaves a conditional
limiting \(N(0,2V)\) fluctuation. The uncentered scaled difference includes
an arbitrary shift. A centered normal distribution gives its largest mass
among intervals of length \(2c\) to \([-c,c]\): differentiating the mass
of a translated interval shows it decreases as the center moves away from
zero. Thus the arbitrary lower-layer shift cannot invalidate
\[
\limsup_{n\to\infty}
\Pr\left(\sqrt n\,|F_n^{\rm init}-\widetilde F_n^{\rm init}|\le c\right)
\le 2\Phi\left(\frac{c}{\sqrt{2V}}\right)-1.
\]
The argument needs no central limit theorem for the lower-layer shift.
Choosing \(c=c_\delta>0\) with the right side strictly below \(\delta\)
gives the claimed eventual confidence \(1-\delta\) at each sufficiently
large individual width.

The result is about the **initialization-kernel interpolation endpoint**.
At zero readout, hidden-parameter derivatives of the output vanish, so this
kernel is indeed the canonical initial tangent kernel with its specified
mobilities. It is not the kernel of the later trained network. A fixed
admissible query supplies a witness for a supremum over a deterministic set
containing that query, but the proof gives neither a simultaneous bound at
every query nor a single positive coefficient with probability tending to
one in the iid fixed-query central limit theorem.

The near-affine example in Section 7 correctly proves
\(V_\varepsilon\to0\) with training gap exactly one and a common regularity
envelope. Its conclusion should be read as concerning this fixed-query iid
influence coefficient. Vanishing of this particular last-layer contribution
alone would not establish vanishing of all possible lower-layer contributions
to a full finite-depth fluctuation, and it does not refute a supremum bound.
The note explicitly acknowledges the supremum limitation.

## 3. High-Hermite-tail covariance and perturbation neighborhood: correct

Let \(W\in\mathbb R^{n\times n}\) have rows \(b_i^\top\), with
\(s\le\|b_i\|\le S\), and define the correlation matrix
\(C_{ij}=b_i^\top b_j/(\|b_i\|\|b_j\|)\).
Assume \(\|C\|_{\rm op}\le M\) and
\(|C_{ij}|\le\rho<1\) for \(i\ne j\).
For a nonaffine globally Lipschitz analytic activation, let
\[
a_k(\sigma)=\mathbb E\left[\phi(\sigma G)
                    \frac{H_k(G)}{\sqrt{k!}}\right],
\qquad G\sim N(0,1),
\]
where \(H_k\) are the probabilists' Hermite polynomials. Gaussian generating
functions give the cross-correlation identity for the normalized Hermites.
Their complete orthonormal expansion in Gaussian \(L^2\) yields
\[
\operatorname{Cov}(\phi(WZ))
=\sum_{k\ge1}\operatorname{diag}(a_k(\|b_i\|))
  C^{\circ k}\operatorname{diag}(a_k(\|b_i\|)),
\qquad Z\sim N(0,I_n).
\]
Each \(C^{\circ k}\) is a tensor-power Gram and is positive semidefinite.
The finite-dimensional quadratic forms converge by the scalar \(L^2\)
expansions. No centering or oddness assumption is needed; the covariance
simply removes the degree-zero term.

For \(k\ge K\), where \(\rho^{K-2}M^2\le1/2\),
\[
\sum_{j\ne i}|C_{ij}|^k
\le\rho^{k-2}\sum_jC_{ij}^2
\le\rho^{k-2}M^2\le\frac12.
\]
Combining the unit diagonal with
\(2|u_i u_j|\le u_i^2+u_j^2\) gives
\(C^{\circ k}\succeq I/2\), including odd \(k\) and negative
correlations. Consequently
\[
\operatorname{Cov}(\phi(WZ))\succeq
\frac12\operatorname{diag}\left(\sum_{k\ge K}a_k(\|b_i\|)^2\right).
\]
A zero tail at a positive scale would make \(\phi\) a polynomial on the
real line by continuity, and therefore affine by its global Lipschitz bound.
The tail is continuous in scale: the full squared \(L^2\) norm and each of
the finitely many removed coefficient squares are continuous under the
Lipschitz coupling \(\phi(\sigma G)\). Thus
\[
c_{\phi,s,S,K}
=\frac12\min_{\sigma\in[s,S]}\sum_{k\ge K}a_k(\sigma)^2>0.
\]
This is a dimension-independent constant for fixed displayed parameters.

The concrete perturbation arithmetic is correct. If initialized row norms
are in \([0.9,1.1]\), their pairwise inner products have magnitude at most
\(0.01\), and \(\|W_0\|_{\rm op}\le9\), then every
\(\|E\|_F\le0.1\) gives
\[
0.8\le\|b_i\|\le1.2,
\quad |b_i^\top b_j|\le0.24,
\quad |C_{ij}|\le0.24/0.64=0.375<1/2,
\quad \|C\|_{\rm op}\le9.1^2/0.8^2<144.
\]
With \(\rho=1/2\), \(M=144\), and \(K=18\), the required quantity is
\(144^2/2^{16}=0.31640625<1/2\). The conclusion is simultaneous over all
such perturbations; no independence between \(E\) and \(W_0\) is required.

For iid \(N(0,1/n)\) entries, all three initialization conditions hold
with probability tending to one. Row-norm deviations have exponentially
small chi-square tails, even after the union bound over rows. Conditional
on a row of norm at most \(1.1\), its inner product with another row is
Gaussian of variance at most \(1.1^2/n\), giving an exponentially small
tail at \(0.01\) after the union bound over row pairs. A pair of
\(1/4\)-nets of size at most \(9^n\) gives
\(\|W_0\|_{\rm op}\le2\max|u^\top W_0v|\); a Gaussian union bound at
\(4.5\) has probability at most
\(2\exp((2\log9-4.5^2/2)n)\), which tends to zero.

The conditional endpoint consequence in `POSITIVE_ROUTE.md` also checks.
Condition on training states that provide the exact representation
\(n^{-1}w_\infty^\top\phi(W_\infty Z)\) with an independent standard
Gaussian \(Z\), covariance at least \(cI\), operator norm at most \(B\),
and readout energy \(\|w_\infty\|^2/n\ge E_y^2/2\).
For the difference \(D\) of two runs, put
\(R=(\|w_\infty\|^2+\|\widetilde w_\infty\|^2)/n^2\).
Its variance is at least \(cR\), and its Gaussian Lipschitz constant is
at most \(bB\sqrt R\), where \(b\) is the activation Lipschitz constant.
For \(\xi=D-\mathbb ED\), Gaussian Poincare applied to \(\xi\) and
\(\xi^2\) gives
\[
\mathbb E\xi^2\le(bB)^2R,
\qquad
\mathbb E\xi^4
\le4(bB)^2R\mathbb E\xi^2+(\mathbb E\xi^2)^2
\le5(bB)^4R^2.
\]
Keeping the possibly nonzero conditional mean in both moments gives exactly
the fourth-to-second moment ratio and the positive Paley--Zygmund probability
stated in the note. The threshold is
\(\sqrt{cR/2}\ge\sqrt{c/2}\,E_y/\sqrt n\).
This conditional implication is valid, but its independent Gaussian
representation remains an assumption and is not supplied by the covariance
lemma or by fitting.

## 4. Hidden-nullspace derivative calculation: correct canonical factors

Use the note's admitted tanh--tanh model with \(m=d=2\),
\(v_1=e_1\), \(v_2=e_2\), labels \((y_1,0)\) with \(y_1\ne0\), first
matrix \(A\), second matrix \(W\), and readout \(w\). At initialization,
define
\[
h_a=\tanh(A_0v_a),\quad z_a=W_0h_a,\quad g_a=\tanh z_a,
\quad D_a=\operatorname{diag}(\operatorname{sech}^2(A_0v_a)),
\quad E_a=\operatorname{diag}(\operatorname{sech}^2z_a).
\]
The initialized hidden velocities vanish because the backward responses
contain \(w(0)=0\). The canonical readout velocity is
\(\dot w(0)=2y_1g_1/m\). Set \(u=E_1\dot w(0)\).
Differentiating the actual flow, rather than a rescaled direction, gives
\[
\ddot W(0)=\frac{2y_1}{nm}u h_1^\top,
\qquad
\ddot A(0)=\frac{2y_1}{m}D_1W_0^\top u\,e_1^\top.
\]
The input orthogonality implies
\(\ddot h_1(0)=(2y_1/m)D_1^2W_0^\top u\), and hence
\[
\ddot z_1(0)=\frac{2y_1}{nm}\|h_1\|^2u
 +\frac{2y_1}{m}W_0D_1^2W_0^\top u.
\]
Both factors of \(n\) agree with the paper: there is \(1/n\) in the
second-layer flow, and no \(1/n\) in the first-layer flow.

For \(n>2\), choose a measurable unit \(q\), using only \(A_0\),
orthogonal to \(h_1,h_2\). Decompose
\(W_0=B+s q^\top\) with \(B=W_0(I-qq^\top)\) and \(s=W_0q\).
Conditional on \(A_0,B\), Gaussian orthogonal projections make the entries
of \(s\) independent \(N(0,1/n)\). Also \(W_0h_a=Bh_a\), so the initial
training features and \(u\) are fixed under that conditioning. The degree-two
term of \(\ddot z_1(0)\) as a polynomial in \(s\) is
\[
\frac{2y_1}{m}(q^\top D_1^2q)s(s^\top u).
\]
Here \(q^\top D_1^2q>0\), and \(u\ne0\) almost surely: \(h_1\ne0\)
almost surely, its Gaussian second-layer preactivations are not all zero,
and tanh has positive derivative at every finite real argument. Thus the
polynomial is nonconstant. It cannot be independent of \(s\) conditional
on \(A_0,B\), because it is a nonconstant measurable function of that
Gaussian vector. Training already observes this initially invisible block.

The scalar prediction refinement is also correct. At zero time,
\(\dot g_a=0\), and \(\ddot w\) and \(\ddot r_a\) depend only on
the initial training features. Differentiating the readout equation twice
shows that the part of \(w^{(3)}(0)\) depending on \(s\) is
\((2y_1/m)E_1\ddot z_1(0)\). Since
\[
f_n^{(3)}(0,v_1)
=\frac1n\left[w^{(3)}(0)^\top g_1
              +3\dot w(0)^\top E_1\ddot z_1(0)\right],
\]
its part depending on \(s\) is \(4u^\top\ddot z_1(0)/n\). Its quadratic
term is exactly
\[
\frac{8y_1}{mn}(q^\top D_1^2q)(s^\top u)^2,
\]
which is nonzero. Therefore even observing the training prediction trajectory,
together with \(A_0,B\), prevents treating the entire original \(s\) block
as an unchanged independent Gaussian block. The calculation does not exclude
other independent components, weaker asymptotic independence, or a different
endpoint fluctuation proof.

## 5. Actual implications and remaining proof obligation

No incorrect proof was found among the four requested partial claims. Their
precise usable conclusions are: strict population feature innovation under
the extra nonaffinity assumptions; a positive frozen-feature influence
variance; eventual independent-run anti-concentration for the actual
finite-depth **initialization-kernel** endpoint; a robust deterministic
covariance lemma for an independent Gaussian query; and an exact obstruction
to preserving a whole initial upper-layer nullspace as unobserved Gaussian
randomness during hidden-layer training.

None supplies a width-uniform fluctuation theorem or an independent Gaussian
query representation for the actual trained endpoint in the full-span case.
The fitting estimates in the supplied manuscript give convergence and
absolute parameter/feature control; they do not provide those missing
probabilistic statements. If the labels are multiplied by a scalar amplitude
\(s>0\), an absolute small-label remainder of order \(s^3\) cannot transfer
a fluctuation of order \(s/\sqrt n\) at fixed \(s\). One needs control of its
fluctuations at the width scale or
another argument excluding cancellation. A nonzero derivative at zero
label amplitude also cannot establish nonvanishing at every permitted
positive amplitude. Both candidate notes correctly retain these as open
obligations.
