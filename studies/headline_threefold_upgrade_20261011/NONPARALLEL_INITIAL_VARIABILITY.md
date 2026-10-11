# Fixed nonparallel test: initial variability and a common near-zero interval

2026-10-11. Scoped independent derivation from the model in
`paper/compact.tex`, its fitting/source modules, and the initial
derivative/small-ball calculation recorded in `WIDTH_UPGRADE.md`.
No other new route file, other study, experiment, or Git history was used.

## Statement and exact quantifiers

The proposed route is valid. Assume the paper's Gaussian initialization and
physical gradient flow, with \(L\ge2\), a nonaffine first activation,
and nonconstant later activations. All activations satisfy the paper's
strip analyticity and bounded-derivative conditions. Fix finitely many unit
directions that are pairwise nonparallel: neither equal nor opposite.

1. Every augmented population feature Gram, starting at layer one, is
   strictly positive definite. At every finite width at least the number
   of these directions, every initialized hidden-feature matrix has full
   column rank almost surely.
2. Fix \(m\) of the directions as training inputs and another direction
   \(v_q\) as a test. For every deterministic nonzero label vector
   \(y\in\mathbb R^m\), put \(Y=\|y\|_2/\sqrt m\). For each
   \(0<\delta<1\), there are \(c_\delta>0\) and a finite width
   threshold such that two independent dense runs satisfy

   \[
   |\dot f_n(0,\sqrt d\,v_q)
       -\dot{\widetilde f}_n(0,\sqrt d\,v_q)|
   \ge c_\delta Y/\sqrt n
   \tag{1}
   \]

   with probability at least \(1-\delta/2\). The test is fixed before
   initialization; it is not an adaptively selected training index.
3. Under the paper's original small-label/source assumptions, there is an
   explicit deterministic \(t_n>0\), tending to zero, for which the actual
   two gradient flows satisfy, on one event of probability at least
   \(1-\delta\),

   \[
   |f_n(t,\sqrt d\,v_q)-\widetilde f_n(t,\sqrt d\,v_q)|
   \ge\frac{c_\delta}{2}\frac{Yt}{\sqrt n}
   \quad\text{for every }0<t\le t_n.
   \tag{2}
   \]

The rank and initial derivative assertions need no small-label assumption.
The simultaneous-time assertion retains the paper's original label cap.
Section 6 gives \(t_n\asymp(\lambda\sqrt n\log(en))^{-1}\), with
its constant displayed below. No polynomial width onset is asserted or
needed.

Constants in (1) can depend on the fixed augmented geometry and
activations, and can be chosen uniformly over deterministic unit label
directions. The probability event is nevertheless for **each fixed label
vector**, not simultaneously for every label vector. At one test query,
the initial derivative difference is a linear functional of \(y\);
for \(m\ge2\) it always has a nontrivial label nullspace. Labels chosen
after seeing initialization would therefore invalidate such a simultaneous
claim.

## 1. Strict positivity at the first layer

Let \(v_1,\ldots,v_N\in S^{d-1}\) be pairwise nonparallel and
\(g\sim N(0,I_d)\). Define the population Gram

\[
Q^{(1)}_{ij}
=\mathbb E[\phi_1(g^\top v_i)\phi_1(g^\top v_j)].
\tag{3}
\]

The linear-growth bound from the bounded derivative makes every entry
finite. The activation \(\phi_1\) is not a polynomial: if its Taylor
series at zero terminated, the analytic identity theorem on the connected
strip would identify it with that polynomial; bounded derivative on the
real axis would then make it affine, contrary to the assumption.
Consequently there is a nonzero Taylor coefficient of some degree
\(k\ge N-1\).

Suppose \(b^\top Q^{(1)}b=0\). The continuous function
\(g\mapsto\sum_i b_i\phi_1(g^\top v_i)\) vanishes almost surely
under a Gaussian of everywhere-positive density, so vanishes everywhere.
Its homogeneous Taylor term of degree \(k\) gives

\[
\sum_i b_i v_i^{\otimes k}=0.
\tag{4}
\]

These tensors are linearly independent. Indeed, for each fixed \(i\)
and each \(j\ne i\), nonparallelism permits a linear form
\(\ell_{ij}\) with \(\ell_{ij}(v_j)=0\) and
\(\ell_{ij}(v_i)\ne0\). Choose another linear form \(\ell_i\)
nonzero at \(v_i\). The homogeneous polynomial

\[
p_i(x)=\prod_{j\ne i}\ell_{ij}(x)\,
             \ell_i(x)^{k-(N-1)}
\]

has degree \(k\), is zero at all other \(v_j\), and is nonzero at
\(v_i\). Contracting its symmetric coefficient tensor with (4) gives
\(b_i p_i(v_i)=0\). Thus all \(b_i=0\), proving
\(Q^{(1)}\succ0\). This argument does not assume that the input
Gram itself has full rank, or that \(N\le d\).

## 2. Later population Grams and exact finite-width rank

If \(C\succ0\) and \(Z\sim N(0,C)\), its density is positive
everywhere in \(\mathbb R^N\). For a nonconstant continuous activation
\(\phi\), the Gram \(\mathbb E[\phi(Z)\phi(Z)^\top]\) is
strictly positive definite. Otherwise some nonzero \(b\) obeys
\(\sum_i b_i\phi(z_i)=0\) for all real \(z\). Varying a coordinate
with \(b_i\ne0\) contradicts nonconstancy. Apply this inductively to
the population covariance recursion to obtain \(Q^{(j)}\succ0\) at
every layer \(j\ge1\).

For finite width, the first-layer row functions
\(g\mapsto(\phi_1(g^\top v_i))_{i=1}^N\) span \(\mathbb R^N\):
otherwise a nonzero vector annihilating their span would contradict the
preceding linear-independence proof. Hence there are \(N\) deterministic
row locations giving an invertible evaluation matrix. Its determinant,
viewed as a real-analytic function of these \(N\) row locations, is
therefore not identically zero. The zero set of a nonzero real-analytic
function has Lebesgue measure zero, so the first \(N\) independent
Gaussian rows already form an invertible minor almost surely.

For clarity, the zero-set fact follows locally by induction on dimension:
expand in one coordinate, choose a nonidentically zero analytic coefficient
in the remaining coordinates, discard its measure-zero zero set by the
induction hypothesis, and use isolated zeros of each remaining nonzero
one-dimensional analytic section. Fubini and a countable box cover finish
the argument. Analytic uniqueness excludes an identically zero open box.

Condition on a full-rank \(n\times N\) feature matrix at layer \(j-1\).
The next preactivation rows are independent Gaussian vectors with covariance
\(H_{j-1}^\top H_{j-1}/n\succ0\). The same determinant argument
applies to the nonconstant analytic coordinate functions
\((\phi_j(z_i))_{i=1}^N\), which span \(\mathbb R^N\) by the
coordinate-variation argument above. Conditional rank failure has probability
zero. Induction proves full column rank at every hidden layer whenever
\(n\ge N\).

Neither conclusion is valid with a constant later activation. Pairwise
nonparallelism is a genuine uniform sufficient assumption: an even first
activation identifies opposite inputs, while an odd one gives opposite
feature columns. Nonaffineness at layer one is also substantive; affine
ridge features have bounded rank as the number of directions grows.

## 3. Conditional final-row covariance is nondegenerate

Apply the preceding results to the \(N=m+1\) training-and-test list.
Initialized empirical Grams converge in probability to their corresponding
population Grams. This is the fixed-finite-query initialization argument
in the fitting proof, and it does not require a label condition: conditional
on a preceding layer, the next Gram is an average of independent rows;
linear activation growth uniformly bounds its entry variances on bounded
covariance sets. Conditional Chebyshev makes its difference from its
conditional mean vanish. The mean covariance map is continuous, by coupling
Gaussians through the continuous matrix square root and using Gaussian
moment domination. Induction proves the assertion, even when the input
Gram is singular.

Let \(C_*=Q^{(L-1)}\succ0\) on this augmented list. For
\(Z\sim N(0,C)\), \(U=\phi_L(Z)\), define

\[
\Sigma(C)=\operatorname{Cov}
  (U_qU_1,\ldots,U_qU_m).
\tag{5}
\]

This is a **centered** covariance, not the uncentered feature Gram.
It is strictly positive definite whenever \(C\succ0\).
If a nonzero \(e\in\mathbb R^m\) gave zero variance, then continuity
and positive Gaussian density would make

\[
\phi_L(z_q)\sum_{a=1}^m e_a\phi_L(z_a)
\tag{6}
\]

a constant function on \(\mathbb R^{m+1}\). There are training-coordinate
values for which the sum in (6) is nonzero: varying a coordinate with
\(e_a\ne0\) proves this. With those values fixed, varying \(z_q\)
contradicts nonconstancy of \(\phi_L\). Thus \(\Sigma(C)\succ0\).

The entries of (5) are continuous in \(C\), by the same Gaussian
coupling and the polynomial growth of the fourth moments. Put
\(\kappa=\lambda_{\min}(\Sigma(C_*))/2>0\).
Choose a fixed bounded neighborhood \(\mathcal U\) of \(C_*\),
small enough that \(C\succ0\) and \(\Sigma(C)\succeq\kappa I\)
throughout it. Let \(D\) bound all covariance diagonals in that
neighborhood. Write \(b=|\phi_L(0)|\), let \(s\) bound its real
derivative, and set

\[
F_6=b+s\sqrt D\,15^{1/6},\qquad
M_3=8m^{3/2}F_6^6.
\tag{7}
\]

For every unit \(e\in\mathbb R^m\), the scalar
\(X=U_q\sum_a e_aU_a\) then satisfies

\[
\operatorname{Var}(X)\ge\kappa,\qquad
\mathbb E|X-\mathbb EX|^3\le M_3.
\tag{8}
\]

Indeed \(\|U_a\|_6\le F_6\),
\(\|\sum e_aU_a\|_6\le\sqrt mF_6\), and Hölder followed by
centering proves (7)–(8). No independence between coordinates is used.
The constants are uniform over \(e\), but need not have a quantitative
lower bound in terms of the training gap alone.

## 4. Actual small-ball estimate

Here is the finite lemma used, including its proof. If centered iid
\(V_i\) have variance \(\sigma^2>0\) and third absolute moment
at most \(M\), then for every \(h>0\),

\[
\sup_a\Pr\left\{\left|n^{-1/2}\sum_iV_i-a\right|\le h\right\}
\le \frac{3h}{\sigma}
+4\exp\left(-\frac{9h^2\sigma^4n}{128M^2}\right).
\tag{9}
\]

For an independent copy \(V'\), the cosine Taylor inequality gives
\(|\mathbb Ee^{itV}|^2
\le1-\sigma^2t^2+(4/3)M|t|^3\), since
\(\mathbb E|V-V'|^3\le8M\). Therefore
\(|\mathbb Ee^{itV}|\le e^{-\sigma^2t^2/4}\) for
\(|t|\le3\sigma^2/(8M)\).
Majorize the interval indicator by
\(e^{1/2}\exp[-(x-a)^2/(2h^2)]\), use its Gaussian Fourier integral,
and split at \(3\sigma^2\sqrt n/(8M)\). On the inner interval the
characteristic function of the normalized sum is bounded by
\(e^{-\sigma^2t^2/4}\), giving at most
\(\sqrt2e^{1/2}h/\sigma<3h/\sigma\). On the complement discard
that characteristic function and bound the Gaussian integral tail by
\(4\exp[-9h^2\sigma^4n/(128M^2)]\). The shift contributes only a
unit-modulus Fourier factor. This proves (9) without a CLT or an
inference from variance alone.

Now condition on the first run through layer \(L-1\) and the entire
second initialization. On the event that the first run's augmented empirical
covariance \(C_n\) is in \(\mathcal U\), its final-layer rows are
conditionally iid with the law in Section 3. This event has probability
at least \(1-\delta/4\) for all sufficiently large individual widths.
Let \(e=y/(\sqrt mY)\). Zero readout initialization and the physical
readout equation give exactly

\[
\dot f_n(0,\sqrt d\,v_q)
=\frac2{mn}\sum_{i=1}^nU_{i,q}\sum_a y_aU_{i,a}
=\frac{2Y}{\sqrt m\,n}\sum_{i=1}^nX_i.
\tag{10}
\]

The independent second run's derivative value in (1), and the first run's conditional mean
in (10), together give an arbitrary shift in (9). There is no need to
match the two conditional means. Set

\[
h_\delta=\delta\sqrt\kappa/24,\qquad
c_\delta=2h_\delta/\sqrt m
=\frac{\delta\sqrt\kappa}{12\sqrt m}.
\tag{11}
\]

For

\[
n\ge\frac{8192M_3^2}{\delta^2\kappa^3}
             \log\frac{32}{\delta},
\tag{12}
\]

the two terms in (9) are at most \(\delta/8\) each, uniformly on
\(C_n\in\mathcal U\). Including the covariance-event failure gives
probability at most \(\delta/2\) that the derivative gap is smaller
than (1). Thus (1) is proved with a genuine finite small-ball bound.
The qualifying covariance-convergence width remains problem-dependent;
no polynomial dependence on \(\kappa^{-1}\) or geometry is claimed.

## 5. A simultaneous-time transfer, not a single witness time

Let the scalar difference at the fixed test be \(g(t)\). Suppose it is
holomorphic near \(|t|\le R\), \(|g(t)|\le M\) there, \(g(0)=0\),
and \(|g'(0)|\ge a_n>0\). Cauchy's coefficient estimate gives, for
\(0<t\le R/2\),

\[
|g(t)-g'(0)t|
\le M\sum_{k\ge2}(t/R)^k
\le2Mt^2/R^2.
\]

Consequently

\[
|g(t)|\ge a_nt/2\quad\text{simultaneously for all }\quad
0<t\le\min\{R/2,a_nR^2/(4M)\}.
\tag{13}
\]

Apply this with \(a_n=c_\delta Y/\sqrt n\). The interval is
deterministic once deterministic Cauchy bounds are supplied, and the bound
holds on the same event for every positive time in it. At time zero both
predictions are zero; no positive denominator is asserted there. Nothing
in (13) asserts a lower bound at a later fixed time or near infinity.

## 6. Interval on the paper's admissible source event

Now impose the paper's training gap and label conditions, with
\(\lambda=\gamma/m\le1\), \(Y/\lambda\le\beta^{-30L}\),
and \(\ell=\log(en)\). Apply its finite-query analytic source to
the fixed training-and-test list in both runs. At every fixed confidence,
eventually the two predictions are holomorphic on a neighborhood of
\(|t|\le r_n\), with

\[
r_n=\frac1{\lambda\sqrt\ell},\qquad
|f_n|,|\widetilde f_n|\le16\beta^{6L}Y/\lambda.
\tag{14}
\]

Thus (13) applies with \(R=r_n\) and
\(M=32\beta^{6L}Y/\lambda\), and permits

\[
t_n=\min\left\{\frac1{2\lambda\sqrt\ell},
       \frac{c_\delta}{128\beta^{6L}\lambda\sqrt n\,\ell}\right\}.
\tag{15}
\]

Eventually the second member is smaller. Allocate \(\delta/4\) to
each source event and \(\delta/2\) to the derivative event; no
independence between these events is needed. This proves the sharper
version of (2) on one common event. It is an initial-time result for the
actual flows, not a frozen-feature substitution.

## 7. Initial innovation and the conditioning boundary

Let \(H\) be the initialized final-layer matrix on training inputs and
the test, and let \(H_{\rm tr}\) contain its training columns. For
\(n\ge m+1\), full column rank gives

\[
\frac1n\|(I-P_{H_{\rm tr}})h_q\|_2^2
=G_{qq}-G_{q,\rm tr}G_{\rm tr,tr}^{-1}G_{\rm tr,q}>0,
\qquad G=H^\top H/n.
\tag{16}
\]

It converges in probability to the strictly positive Schur complement
of the augmented population Gram \(Q^{(L)}\). This is a linear
feature-space innovation, uniform away from zero with high probability
for the fixed geometry.

At the last preactivation row, conditioning on all preceding layers and
that row's training preactivations leaves a Gaussian test innovation of
variance
\(C_{qq}-C_{q,\rm tr}C_{\rm tr,tr}^{-1}C_{\rm tr,q}>0\).
Nonconstancy of \(\phi_L\) makes the corresponding conditional activated
variance positive as well. No uniform lower bound for every possible
conditioning value is inferred.

Neither (16) nor this row-wise conditioning statement asserts independence
from, or nondegeneracy after conditioning on, an entire future training
transcript. Such a transcript may reveal additional initialization
information. The small-ball proof conditions only on the first run through
layer \(L-1\) and the independent second run, exactly as stated. A
future-transcript claim would require a separate argument.

## Frozen source inputs

SHA-256 of the scoped inputs used in this derivation:

| File | SHA-256 |
| --- | --- |
| `paper/compact.tex` | `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `paper/compact_foundations.tex` | `6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0` |
| `WIDTH_UPGRADE.md` | `8f8f0a672cdb948cbe84ba01afc8d9b0fd8f504441dc2daa30a7dea40cfb99d9` |
