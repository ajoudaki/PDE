# Endpoint lower-bound route: a robust covariance lemma and the remaining gap

2026-10-10. Scoped independent derivation. This note is not an established
endpoint theorem. Inputs read in full were
`studies/integrated_general_compression_20261004/TANH_ENDPOINT_VARIABILITY_LOWER.md`
and `NONLINEAR_ENDPOINT_VARIABILITY_LOWER.md`; the model and label convention
were read in `paper/compact.tex`. No historical check, other study research,
experiment, or another route's findings were used. The rigorous-math and
canonical-notation skills, including the neural-network reference, were applied.

The active assignment concerns the fitted-endpoint supremum over separated
unit queries. An intermediate requirement about all training times was
explicitly withdrawn; it is not the task analyzed below. The endpoint target
has not been proved here.

## 1. What the old endpoint proofs actually preserve

For two hidden layers, write the first matrix as \(A\), the second as \(W\),
and the readout as \(w\). Let \(S=\operatorname{span}\{v_1,\ldots,v_m\}\),
where \(v_a=x_a/\sqrt d\). The first-layer training equation has the form

\[
\dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top.
\]

Thus \(A(t)|_{S^\perp}=A(0)|_{S^\perp}\) exactly. The complete training
trajectory depends on \(A(0)|_S,W(0)\), while the Gaussian block
\(A(0)|_{S^\perp}\) remains independent. For a unit query \(v\in S^\perp\),
the first preactivation \(Z=A(0)v\) is therefore an independent
\(N(0,I_n)\) vector even after conditioning on the whole training trajectory.

The identity--tanh source uses the exact endpoint representation
\(n^{-1}w_\infty^\top\tanh(W_\infty Z)\). The tanh--tanh source instead uses
\(n^{-1}w_\infty^\top\tanh(W_\infty\tanh Z)\). Each source proves a
conditional query-feature covariance lower bound, uses interpolation to force
readout energy of order \(n\), and controls the fourth moment by a Gaussian
gradient inequality. This gives order \(n^{-1/2}\) variability at the actual
endpoint.

This conditioning must use a fitting event measurable in the active training
initialization. A good event involving the unused first-layer block would
alter the conditional Gaussian law. Both source arguments explicitly handle
that issue. Their algebraic covariance and moment arguments do not assume
that trained matrices remain Gaussian. Their imported global fitting theorem
was outside this route's input list and was not independently rechecked here.

When \(S=\mathbb R^d\), there is no unused first-layer block. The old proof
then supplies no independent query coordinates. Changing a pointwise query
target to a supremum over queries does not create that missing block.

## 2. A robust covariance lemma for a Gaussian query

The following lemma replaces a single special Hermite coefficient by the full
high-order Hermite tail. It avoids making the permissible matrix movement
proportional to the size of one possibly tiny nonlinear coefficient.

Let \(\phi:\mathbb R\to\mathbb R\) be nonaffine, real analytic, and globally
Lipschitz. The activation assumptions in the assignment imply these properties.
Let \(W\in\mathbb R^{n\times n}\) have nonzero rows \(b_i^\top\), with

\[
s\le\|b_i\|_2\le S,
\qquad C_{ij}=\frac{b_i^\top b_j}{\|b_i\|_2\|b_j\|_2},
\qquad \|C\|_{\mathrm{op}}\le M,
\qquad |C_{ij}|\le\rho<1\quad(i\ne j),
\tag{1}
\]

where \(s,S,M,\rho\) are fixed positive constants with \(s\le S\). Choose
an integer \(K\ge2\) such that \(\rho^{K-2}M^2\le1/2\). There exists
\(c_{\phi,s,S,K}>0\), independent of \(n\), such that for \(Z\sim N(0,I_n)\),

\[
\operatorname{Cov}_Z[\phi(WZ)]\succeq c_{\phi,s,S,K}I_n.
\tag{2}
\]

Here \(\phi\) is applied coordinatewise. Its mean need not vanish.

To prove this, let \(H_k\) be the probabilists' Hermite polynomials and set

\[
a_k(\sigma)=\mathbb E\left[\phi(\sigma G)
                         \frac{H_k(G)}{\sqrt{k!}}\right],
\qquad G\sim N(0,1).
\]

The Lipschitz assumption implies Gaussian square integrability. The
orthonormal Hermite expansion and the Gaussian generating-function identity
\(\mathbb E[e^{tG-t^2/2}e^{uG'-u^2/2}]=e^{C_{ij}tu}\) give

\[
\operatorname{Cov}_Z[\phi(WZ)]
=\sum_{k\ge1}\operatorname{diag}(a_k(\|b_i\|))
  C^{\circ k}\operatorname{diag}(a_k(\|b_i\|)).
\tag{3}
\]

The superscript \(\circ k\) denotes entrywise powers. Each summand is positive
semidefinite because \(C^{\circ k}\) is the Gram matrix of the normalized
rows' \(k\)-fold tensor powers. The scalar square-integrable expansions
justify convergence of every quadratic form in (3).

For \(k\ge K\),

\[
\sum_{j\ne i}|C_{ij}|^k
\le\rho^{k-2}\sum_j C_{ij}^2
\le\rho^{k-2}\|C\|_{\mathrm{op}}^2
\le\frac12.
\]

Since the diagonal entries equal one, the inequality
\(2|u_i u_j|\le u_i^2+u_j^2\) gives \(C^{\circ k}\succeq I_n/2\).
Keeping only \(k\ge K\) in (3) therefore proves

\[
\operatorname{Cov}_Z[\phi(WZ)]
\succeq\frac12\operatorname{diag}\left(
               \sum_{k\ge K}a_k(\|b_i\|)^2\right).
\tag{4}
\]

For each \(\sigma>0\), the tail \(\sum_{k\ge K}a_k(\sigma)^2\) is strictly
positive. A zero tail would make \(\phi(\sigma G)\) equal almost everywhere
to a polynomial of degree below \(K\). Continuity then makes the equality
hold at every real argument. A polynomial with a globally bounded first
derivative is affine, contradicting the hypothesis.

Moreover, \(\sigma\mapsto\phi(\sigma G)\) is continuous in Gaussian
\(L^2\), since its squared distance at two scales is at most the squared
Lipschitz constant times \((\sigma-\sigma')^2\mathbb E G^2\). Subtracting
the finite sum of the first \(K\) coefficient squares from the full
\(L^2\) norm proves continuity of the tail. Its minimum on \([s,S]\) is
therefore positive. Equation (2) follows with half that minimum.

### A concrete matrix neighborhood

Suppose the initialized rows satisfy

\[
0.9\le\|b_{0,i}\|\le1.1,\qquad
\max_{i\ne j}|b_{0,i}^\top b_{0,j}|\le0.01,
\qquad \|W_0\|_{\mathrm{op}}\le9.
\]

For every perturbation \(E\) with \(\|E\|_F\le0.1\), the rows of
\(W=W_0+E\) have norms in \([0.8,1.2]\). Their unnormalized pairwise inner
products have magnitude at most
\(0.01+2(1.1)(0.1)+0.1^2=0.24\), so their correlations are at most
\(0.24/0.8^2<1/2\). Also

\[
\|C\|_{\mathrm{op}}
\le\frac{\|W\|_{\mathrm{op}}^2}{0.8^2}
\le\frac{9.1^2}{0.8^2}<144.
\]

Thus \(s=0.8,S=1.2,M=144,\rho=1/2,K=18\) satisfy (1) and the needed
tail inequality. This deterministic conclusion holds simultaneously for all
such perturbations, including trained perturbations depending arbitrarily
on \(W_0\).

The three displayed initialization conditions hold with probability tending
to one for independent \(N(0,1/n)\) entries. Chi-square exponential moments
give the row-norm event; conditioning on one row and applying scalar Gaussian
tails gives the inner-product event. For the loose operator bound, use a
\(1/4\)-net of each unit sphere with cardinality at most \(9^n\).
Approximating both maximizing vectors gives
\(\|W_0\|_{\mathrm{op}}\le2\max_{u,v\text{ in the nets}}|u^\top W_0v|\).
Each scalar in this maximum is \(N(0,1/n)\). A union bound at threshold
\(4.5\) gives failure probability at most
\(2\exp(2n\log9-4.5^2n/2)\), which tends to zero.

This lemma is stronger than a perturbation argument that compares the full
feature map against its initialized value. In particular, its permitted
matrix movement does not shrink with the nonlinearity amplitude in
\(\phi(z)=z+\eta\tanh z\), \(\eta>0\). Its lower-bound constant may shrink
with \(\eta\), as is appropriate for a problem-dependent conclusion.

It does not by itself solve the assignment: the all-nonlinear full-span
network has no established representation with a Gaussian \(Z\) independent
of its terminal training state. Nor does (2) automatically extend to a
non-Gaussian query passed through several trained nonlinear layers.

### The conditional endpoint consequence does not require oddness

Suppose a training-measurable event supplies the exact endpoint representation
\[
f_n(\infty,v)=n^{-1}w_\infty^\top\phi(W_\infty Z),
\qquad Z\sim N(0,I_n)
\]
with \(Z\) independent of the training sigma field, the covariance bound (2)
with constant \(c>0\), and \(\|W_\infty\|_{\mathrm{op}}\le B\). Write \(b\)
for the Lipschitz constant of \(\phi\). Suppose also that fitting and a
training-feature Gram comparison have supplied
\(\|w_\infty\|^2/n\ge E_y^2/2\), where \(E_y>0\) is fixed. These assumptions
are precisely conditional statements; this paragraph does not assert them
for the requested full-span network.

For two independent copies, condition on both training states and let
\[
D=f_n(\infty,v)-\widetilde f_n(\infty,v),\qquad
R=\frac{\|w_\infty\|^2+\|\widetilde w_\infty\|^2}{n^2}.
\]
The independent remaining Gaussian vectors give
\(\operatorname{Var}(D)\ge cR\), and \(D\) has joint Gaussian Lipschitz
constant at most \(bB\sqrt R\). Set \(\mu=\mathbb ED\) and \(\xi=D-\mu\).
Gaussian Poincare applied to \(\xi\) and \(\xi^2\) gives
\[
\mathbb E\xi^2\le(bB)^2R,\qquad
\mathbb E\xi^4\le5(bB)^4R^2.
\]
For this specialization, Poincare follows by expanding in orthonormal
Gaussian Hermites: the variance sums the squared coefficients of positive
degree, and the gradient energy weights those coefficients by their degree.
Lipschitz growth makes the displayed functions and gradients integrable;
smooth approximation supplies the same inequality if needed.

The elementary inequality \(|u+v|^4\le8(|u|^4+|v|^4)\) consequently yields
\[
\frac{\mathbb ED^4}{(\mathbb ED^2)^2}
\le
8\frac{\mu^4+5(bB)^4R^2}{\mu^4+c^2R^2}
\le8\max\{1,5(bB)^4/c^2\}.
\]
For completeness, if \(X\ge0\), Cauchy--Schwarz gives
\[
(1-\theta)\mathbb EX
\le\mathbb E[X1_{\{X\ge\theta\mathbb EX\}}]
\le\sqrt{\mathbb EX^2\,\Pr(X\ge\theta\mathbb EX)}
\]
for \(0<\theta<1\). Apply this to \(X=D^2,\theta=1/2\). The resulting
conditional probability is at least
\[
\frac{1}{32\max\{1,5(bB)^4/c^2\}}
\]
that
\[
|D|\ge\sqrt{cR/2}\ge \sqrt{c/2}\,\frac{E_y}{\sqrt n}.
\]
Thus arbitrary conditional means and unbounded activation values do not
obstruct the old final moment step. Independence and covariance are the
substantive missing ingredients.

## 3. Why an initial upper-layer nullspace is not unobserved by training

Here is an exact calculation within the admitted tanh--tanh architecture.
Take \(m=2,d=2,v_1=e_1,v_2=e_2\), and labels \(y_1\ne0,y_2=0\), with
\(|y_1|\) as small as the existing label cap requires. The training inputs
span the whole input space. Write initialized features and derivative matrices
as

\[
h_a=\tanh(A_0v_a),\quad z_a=W_0h_a,\quad g_a=\tanh z_a,
\quad D_a=\operatorname{diag}(\operatorname{sech}^2(A_0v_a)),
\quad E_a=\operatorname{diag}(\operatorname{sech}^2z_a).
\]

Initially every hidden-block velocity is zero, whereas
\(\dot w(0)=2y_1g_1/m\). Set \(u=E_1\dot w(0)\). Differentiating the
actual canonical equations, with all quantities on the right initialized,
gives

\[
\ddot W(0)=\frac{2y_1}{nm}u h_1^\top,
\qquad
\ddot h_1(0)=\frac{2y_1}{m}D_1^2W_0^\top u.
\]

The orthogonality of the two input directions was used in the second formula.
Consequently the top preactivation has

\[
\ddot z_1(0)
=\frac{2y_1}{nm}\|h_1\|^2u
 +\frac{2y_1}{m}W_0D_1^2W_0^\top u.
\tag{5}
\]

For \(n>2\), choose a unit vector \(q\) perpendicular to both \(h_1,h_2\)
using only \(A_0\), and decompose
\(W_0=B+s q^\top\), where \(Bq=0\). Conditional on \(A_0,B\), the vector
\(s=W_0q\) has independent \(N(0,1/n)\) coordinates. It is absent from
both initial training preactivations; in particular \(u\) is fixed under
this conditioning.

Nevertheless the quadratic term of (5), as a polynomial in \(s\), is

\[
\frac{2y_1}{m}(q^\top D_1^2q)\,s(s^\top u).
\tag{6}
\]

Every diagonal entry of \(D_1\) is strictly positive, so the first scalar
factor is nonzero. Also \(u\ne0\) almost surely: \(h_1\ne0\) almost surely,
and its Gaussian top preactivations do not all vanish. The polynomial (6)
is therefore nonzero. Thus the *training trajectory itself* depends on an
upper-layer Gaussian component that was invisible to training at time zero.
Conditioning on its full training state cannot preserve the initial
independence of that component. The same issue is present if \(q\) is chosen
from an initial query-feature residual whenever that residual is nonzero.

Even the training prediction, rather than just its hidden state, detects this
component. Initially \(g_a'=0\); also \(w''\) and \(r_a''\) depend only on
the initial training features. Differentiating
\(\dot w=-2\sum_a r_ag_a/m\) twice shows that the part of \(w'''(0)\) that
depends on \(s\) is \(2y_1E_1z_1''(0)/m\). Differentiating
\(f_n(t,v_1)=w(t)^\top g_1(t)/n\) three times and using
\(\dot w(0)=2y_1g_1/m\) therefore shows that its \(s\)-dependent part is
\(4u^\top z_1''(0)/n\). In particular, its quadratic term in \(s\) is
\[
\frac{8y_1}{mn}(q^\top D_1^2q)(s^\top u)^2,
\]
which is nonzero. Conditioning on the residual trajectory also generally
reveals this initially unobserved Gaussian component.

This calculation refutes an attempted conditioning argument, not the desired
endpoint lower bound. A different fluctuation theorem might still exploit
the weak effect of those coordinates, but their effect cannot be set to zero.

## 4. The exact endpoint bridge still needed

Fix a nonzero label direction and write the labels as \(s y\) for a scalar
amplitude \(s\). At a formal small-label level, the readout is order \(s\),
hidden movement is order \(s^2\), and the correction to frozen-feature
prediction is order \(s^3\). An absolute endpoint estimate of order
\(s^3\), even if proved uniformly in width, cannot transfer an order
\(s/\sqrt n\) random-feature lower bound at a fixed positive \(s\).

A sufficient transfer statement would instead control the *difference of
the corrections in two independent runs* at order \(s^3/\sqrt n\), with a
coefficient small relative to the leading fluctuation in a useful query norm.
No such estimate was available among this route's inputs. A fluctuation
central limit theorem for the actual trained endpoint, with a nonzero limiting
random function on the query sphere, would be another sufficient bridge.
Neither endpoint fitting alone nor ordinary trajectory concentration supplies
that result.

Even granting analytic dependence of a limiting fluctuation on \(s\), a
nonzero derivative at \(s=0\) does not prove nonvanishing at every permitted
positive amplitude. The elementary analytic function
\(s(1-s^2/s_0^2)\) has a nonzero derivative at zero and vanishes at any
prescribed \(s_0>0\). The same example multiplied by any fixed nonzero query
function shows why taking a query supremum does not repair that logical step.
This is an illustration of an insufficient inference, not a constructed
network counterexample.

The endpoint supremum would help after a nonzero random analytic query
function had been established: a nonzero analytic function on a connected
sphere cannot vanish on a relatively open query region. But establishing
that the trained fluctuation is nonzero, at the specified label amplitude,
is precisely the unresolved step. The robust covariance lemma above removes
one activation-specific obstacle from the old independent-query method; it
does not supply the missing independence or endpoint fluctuation theorem.
