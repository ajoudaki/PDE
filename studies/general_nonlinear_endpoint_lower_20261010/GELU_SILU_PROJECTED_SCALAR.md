# Projected-Gaussian scalar fluctuations with adaptive biases and readouts

2026-10-11. Scoped theoretical continuation. The scientific inputs remain
`paper/compact.tex`, `paper/compact_fitting.tex`, `NONODD_SCALAR_ROUTE.md`,
`NONODD_INNOVATION_ROUTE.md`, and `POSITIVE_ROUTE.md`, read completely in
the preceding route. The supervisor supplied the projected-Gaussian
construction studied here. No experiment, other study, prior review, or
additional repository source was used. The rigorous-math,
conjecture-investigation, and canonical-notation skills were applied.

This note proves the requested scalar covariance lemma and a uniform
conditional Gaussian approximation. Its hypotheses permit arbitrary
transcript-dependent biases and readouts after conditioning on a
transcript. It does not construct or justify the training transcript, an
endpoint integrator, or its approximation error. Those are separate
obligations. The rank defect only needs to be \(o(n)\), and the empirical
fourth-moment bound below must be independent of width.

## 1. Statement with finite constants

Let \(\phi\) be continuous, globally Lipschitz and nonaffine, with two
continuous derivatives whose first and second derivatives are bounded.
These hypotheses hold for every nonaffine activation in the compact
paper's strip-analytic class. Write
\[
s=\sup_{x\in\mathbb R}|\phi'(x)|,
\qquad t=\sup_{x\in\mathbb R}|\phi''(x)|.
\]
Both constants are finite by assumption. In the paper's class this is
immediate on the real axis from the strip bounds used in the definition of
\(\beta\) (with the second-derivative bound also following from Cauchy's
formula). No bound on \(\phi\) itself is assumed.

Fix constants
\[
E>0,\quad M_4<\infty,\quad 0\le B<\infty,\quad
0<\sigma_-\le\sigma_+<\infty.
\tag{1}
\]
At width \(n\), let \(P\in\mathbb R^{n\times n}\) be an orthogonal
projection with rank defect \(r=\operatorname{rank}(I-P)\), and let
\(b,w\in\mathbb R^n\) and \(\sigma\in[\sigma_-,\sigma_+]\) satisfy
\[
\frac{\|b\|^2}{n}\le B^2,\qquad
\frac{\|w\|^2}{n}\ge E^2,\qquad
\frac1n\sum_iw_i^4\le M_4.
\tag{2}
\]
All these objects are fixed when the only remaining randomness
\(g\sim N(0,I_n)\) is sampled. In particular, they may be arbitrary
functions of a previously conditioned transcript.

Define the normalized scalar and its variance by
\[
F(g)=\frac1{\sqrt n}w^\top\phi(b+\sigma Pg),\qquad
v_F=\operatorname{Var}_g F.
\tag{3}
\]
Let
\[
R=\max\{1,4B\sqrt{M_4}/E^2\},
\]
and, for a one-dimensional standard Gaussian \(G\), define
\[
d_R=\min_{\substack{|a|\le R\\u\in[\sigma_-/2,\sigma_+]}}
\left\{\operatorname{Var}\phi(a+uG)
             -\bigl(\mathbb E[G\phi(a+uG)]\bigr)^2\right\}.
\tag{4}
\]
Then \(d_R>0\). For any \(0<\tau\le1/8\), put
\[
\alpha=\sqrt{M_4}\sqrt{\frac{r}{n\tau}}.
\]
If
\[
\alpha\le\min\left\{\frac{E^2}{4},
                 \frac{d_RE^2}{16s^2\sigma_+^2}\right\},
\tag{5}
\]
then the following explicit variance bounds hold:
\[
v_0:=\frac{d_RE^2}{16}\le v_F
\le s^2\sigma_+^2\sqrt{M_4}.
\tag{6}
\]
If \(r_n=o(n)\), the choice
\(\tau_n=\sqrt{(r_n+1)/n}\) satisfies \(\tau_n\le1/8\) and (5)
eventually. All constants in (6) are independent of width.
Asymptotic uniformity throughout this note is over objects obeying one
fixed deterministic rank envelope \(r_n=o(n)\), and a second such
envelope for the additional projection in Section 4. No uniform onset
over all individually sublinear rank sequences is asserted.

There is also a uniform Gaussian approximation:
\[
\sup_{z\in\mathbb R}
\left|\Pr\{F-\mathbb EF\le z\}
     -\Phi\left(\frac z{\sqrt{v_F}}\right)\right|
\le \frac{3s t\sigma_+^3\sqrt{M_4}}{2v_0}\,n^{-1/4}.
\tag{7}
\]
The proof of (7) is self-contained in Section 3. Thus an arbitrary
transcript-dependent mean need not be controlled. For every \(a\in\mathbb R\)
and \(c>0\), (7) implies
\[
\Pr\{|F-a|\le c\}
\le\frac{2c}{\sqrt{2\pi v_0}}
   +\frac{3s t\sigma_+^3\sqrt{M_4}}{v_0}\,n^{-1/4}.
\tag{8}
\]
The estimate remains valid at interval endpoints without an atom
assumption: use a left limit of the distribution function for the lower
endpoint. In particular, the predictor \(F/\sqrt n\) has a conditional
small-ball bound at radius \(c/\sqrt n\), uniformly over all centers.

## 2. Proof of the covariance lower bound

Write \(Q=I-P\) and \(q_i=Q_{ii}\). Its diagonal entries lie in
\([0,1]\) and sum to \(r\). Split the indices into
\[
I=\{i:q_i\le\tau\},\qquad J=\{i:q_i>\tau\}.
\tag{9}
\]
Only the high-leverage indices \(J\) will be discarded, and
\(|J|\le r/\tau\). Large-bias indices in \(I\) remain in the
covariance calculation.

For \(i\in I\), the variance of \((Pg)_i\) is
\(P_{ii}=1-q_i\ge1-\tau\). The normalized Gaussian correlations on
these indices are
\[
C_{ij}=\frac{P_{ij}}{\sqrt{P_{ii}P_{jj}}},\qquad i,j\in I.
\]
Since \(P^2=P\),
\[
\sum_{j\ne i}P_{ij}^2=P_{ii}-P_{ii}^2=q_i(1-q_i).
\]
It follows that
\[
\sum_{j\in I,\,j\ne i}|C_{ij}|^2
\le\frac{\tau}{(1-\tau)^2}=:\eta<\frac12.
\tag{10}
\]
Every correlation has absolute value at most one. Thus for every integer
\(k\ge2\), the same upper bound applies to the sum of
\(|C_{ij}|^k\). The diagonal entries of \(C^{\circ k}\) equal one,
so \(2|u_i u_j|\le u_i^2+u_j^2\) gives
\[
C^{\circ k}\succeq(1-\eta)I\succeq\tfrac12I,
\qquad k\ge2.
\tag{11}
\]

Expand each scalar function in normalized probabilists' Hermite
polynomials:
\[
a_{k,i}=\mathbb E\left[
\phi(b_i+\sigma\sqrt{P_{ii}}G)\frac{H_k(G)}{\sqrt{k!}}\right].
\]
The Gaussian generating-function identity proves the exact covariance
formula
\[
\operatorname{Cov}_g[\phi(b+\sigma Pg)_I]
=\sum_{k\ge1}\operatorname{diag}(a_{k,i})
 C^{\circ k}\operatorname{diag}(a_{k,i}).
\tag{12}
\]
Here every summand is positive semidefinite: \(C^{\circ k}\) is the
Gram matrix of tensor powers of Gaussian correlation vectors. Lipschitz
growth gives square integrability and justifies the Hermite expansion
and convergence of the scalar quadratic forms.

The sum of coefficient squares for \(k\ge2\) is the expression in
braces in (4). It is positive at every \((a,u)\) with \(u>0\), because
a zero tail would make \(\phi(a+uG)\) affine in \(G\) almost surely.
Continuity and full Gaussian support would then make \(\phi\) affine
on the entire real line. Continuity of that tail in \((a,u)\) follows
from Lipschitz continuity in Gaussian \(L^2\) and subtraction of the
degree-zero and degree-one coefficient squares. Its compact minimum
in (4) is therefore positive. For \(i\in I\), the scale
\(\sigma\sqrt{P_{ii}}\) belongs to
\([\sigma_-/2,\sigma_+]\). Equations (11)--(12) consequently give
\[
\operatorname{Cov}_g[\phi(b+\sigma Pg)_I]
\succeq\frac{d_R}{2}
       \operatorname{diag}_{i\in I}(\mathbf1_{|b_i|\le R}).
\tag{13}
\]
No large-bias coordinate in \(I\) has been dropped from the left-hand
side. Thus correlations with those coordinates cannot cancel this bound.

For any set \(A\) of indices, the fourth-moment bound in (2) gives
\[
\frac1n\sum_{i\in A}w_i^2
\le\sqrt{M_4}\sqrt{|A|/n}.
\tag{14}
\]
The bias bound implies
\(|\{i:|b_i|>R\}|/n\le B^2/R^2\). Therefore the readout energy
on large-bias indices is at most \(E^2/4\) after division by \(n\),
by the definition of \(R\). Equations (9) and (14) bound the energy on
\(J\) by \(\alpha\). Under (5),
\[
\frac1n\sum_{i\in I,\,|b_i|\le R}w_i^2\ge E^2/2.
\tag{15}
\]

Split the normalized scalar in (3) as \(F=F_I+F_J\), according to the
two index sets. Equation (13) yields
\[
\sqrt{\operatorname{Var}F_I}\ge\sqrt{d_R}\,E/2.
\tag{16}
\]
The scalar \(F_J\) has Gaussian Lipschitz constant at most
\(s\sigma_+\|w_J\|/\sqrt n\), since \(\|P\|_{\rm op}\le1\).
Gaussian Poincare therefore gives
\[
\sqrt{\operatorname{Var}F_J}\le s\sigma_+\sqrt\alpha
\le\sqrt{d_R}\,E/4.
\tag{17}
\]
Gaussian Poincare here follows by expanding a smooth function in
multivariate Gaussian Hermites: its variance sums all positive-degree
coefficient squares, while its expected squared gradient weights those
coefficients by their degree. Approximation extends the inequality to
Lipschitz functions.

The reverse triangle inequality in centered Gaussian \(L^2\), applied
to (16)--(17), proves
\(\sqrt{\operatorname{Var}F}\ge\sqrt{d_R}E/4\). This is the lower
bound in (6). The entire scalar \(F\) has Lipschitz constant at most
\(s\sigma_+\|w\|/\sqrt n\), and
\(\|w\|^2/n\le\sqrt{M_4}\). Poincare gives the upper bound.

The argument controls all possible cross-cancellation with \(J\) by
its vanishing scalar \(L^2\) contribution. The discarded proportion
is \(o(1)\); no comparison between \(d_R\) and a fixed, nonvanishing
large-bias truncation error was made.

## 3. A self-contained second-order Gaussian and Stein estimate

The following general estimate is enough for (7). Let \(f:\mathbb R^n
\to\mathbb R\) be twice continuously differentiable, centered under
standard Gaussian measure, and suppose
\[
\sup_x\|\nabla f(x)\|\le A,\qquad
\sup_x\|D^2f(x)\|_{\rm op}\le D,\qquad
v=\mathbb Ef(g)^2>0.
\tag{18}
\]
Then
\[
\sup_z\left|\Pr\{f(g)\le z\}-\Phi(z/\sqrt v)\right|
\le\frac{3AD}{2v}.
\tag{19}
\]

For completeness, define the Gaussian Ornstein--Uhlenbeck semigroup by
\[
(P_tf)(x)=\mathbb E_{g'}f(e^{-t}x+\sqrt{1-e^{-2t}}g'),
\qquad g'\sim N(0,I_n),
\]
and set \(Rf=\int_0^\infty P_tf\,dt\). Centering and Lipschitz
continuity make this integral converge at every \(x\): coupling the
Gaussian in \(P_tf\) to the one in \(\mathbb Ef(g')=0\) bounds
\(|P_tf(x)|\) by an integrable constant times
\(e^{-t}\|x\|+e^{-2t}\mathbb E\|g'\|\). Differentiating the Gaussian
convolution and using (18) gives
\[
\|\nabla Rf\|\le A\int_0^\infty e^{-t}dt=A,
\qquad
\|D^2Rf\|_{\rm op}\le D\int_0^\infty e^{-2t}dt=D/2.
\tag{20}
\]
The generator is \(L=\Delta-x^\top\nabla\); differentiation and
Gaussian integration by parts give \(\partial_tP_tf=LP_tf\).
Integrating in time therefore gives \(-LRf=f\). Equivalently, first
integrate to a finite time \(T\), obtaining
\(-L\int_0^T P_tf\,dt=f-P_Tf\), and then let \(T\to\infty\).
The preceding coupling bound gives \(P_Tf\to0\) in Gaussian \(L^2\),
and (20) justifies the derivative limits.

Define the scalar random coefficient
\[
\Gamma(x)=\nabla f(x)^\top\nabla Rf(x).
\tag{21}
\]
Gaussian integration by parts, applied coordinatewise to \(-LRf\),
gives, for smooth functions \(\psi\) with bounded derivative,
\[
\mathbb E[f(g)\psi(f(g))]
=\mathbb E[\psi'(f(g))\Gamma(g)].
\tag{22}
\]
The boundary terms vanish by Gaussian decay, linear growth of \(f,Rf\),
and their bounded gradients. Taking \(\psi(x)=x\), by truncation if
desired, gives \(\mathbb E\Gamma=v\). Differentiating (21) and using
(18)--(20) gives the dimension-independent bound
\[
\|\nabla\Gamma\|
\le\|D^2f\|_{\rm op}\|\nabla Rf\|
  +\|D^2Rf\|_{\rm op}\|\nabla f\|
\le\tfrac32AD.
\]
Poincare consequently yields
\[
\mathbb E|\Gamma-v|\le\sqrt{\operatorname{Var}\Gamma}
\le\tfrac32AD.
\tag{23}
\]

Here is the needed indicator Stein bound, with its normalization checked.
For the standard-normal indicator at \(a\), a solution of
\(\psi'(x)-x\psi(x)=\mathbf1_{x\le a}-\Phi(a)\) is
\[
\psi_a(x)=
\begin{cases}
(1-\Phi(a))\Phi(x)/\varphi(x),&x\le a,\\
\Phi(a)(1-\Phi(x))/\varphi(x),&x>a,
\end{cases}
\tag{24}
\]
where \(\varphi\) is the standard normal density. Its one-sided
derivatives have absolute value at most one. To verify this, differentiating
the left branch gives
\((1-\Phi(a))(1+x\Phi(x)/\varphi(x))\), which lies in \([0,1]\);
differentiating the right branch gives
\(\Phi(a)(-1+x(1-\Phi(x))/\varphi(x))\), which lies in \([-1,0]\).
For \(x>0\), the required inequality
\(x(1-\Phi(x))\le\varphi(x)\) follows by integrating
\(x\varphi(u)\le u\varphi(u)\) over \(u\ge x\). The corresponding
inequality for \(x<0\) follows by reflection. Substituting these
inequalities verifies both branch bounds, including the cases where the
sign of \(x\) makes the additional term nonpositive.

For variance \(v\), rescale
\(\psi(x)=v^{-1/2}\psi_{z/\sqrt v}(x/\sqrt v)\). It solves
\[
v\psi'(x)-x\psi(x)=\mathbf1_{x\le z}-\Phi(z/\sqrt v),
\qquad \|\psi'\|_\infty\le1/v.
\]
Use smooth monotone approximations of the indicator, or equivalently
mixtures of (24), to apply (22). The same derivative bound is retained.
Dominated convergence then permits the indicator itself, with no
assumption about atoms in the law of \(f(g)\). Subtracting (22) from
the Stein identity and applying (23) proves (19).

Apply (19) to \(f=F-\mathbb EF\). Direct differentiation of (3) gives
\[
\nabla F=\frac\sigma{\sqrt n}
 P\bigl(w\odot\phi'(b+\sigma Pg)\bigr),
\qquad
D^2F=\frac{\sigma^2}{\sqrt n}
 P\operatorname{diag}\bigl(w\odot\phi''(b+\sigma Pg)\bigr)P.
\tag{25}
\]
The assumptions imply the deterministic bounds
\[
A\le s\sigma_+M_4^{1/4},\qquad
D\le t\sigma_+^2\frac{\max_i|w_i|}{\sqrt n}
\le t\sigma_+^2M_4^{1/4}n^{-1/4}.
\tag{26}
\]
Combining (6), (19), and (26) proves (7). No Gaussian approximation of
\(b,w,P\), nor independence among these objects, was used.

## 4. Retaining a fresh query innovation through another low-rank projection

The following auxiliary statement can supply a positive variance scale at
successive deferred-decision query layers. It has the same fixed bounds
on \(b,\sigma\) as above but does not require a readout. Let
\[
h=\phi(b+\sigma Pg),
\]
and let \(T\) be any fixed orthogonal projection whose rank defect
\(k=\operatorname{rank}(I-T)\) is \(o(n)\). Assume also \(r=o(n)\).
Then there is a constant \(c>0\), depending only on
\(\phi,B,\sigma_-,\sigma_+\), such that
\[
\Pr\{\|Th\|^2/n\ge c\}\longrightarrow1,
\tag{27}
\]
uniformly over the stated deterministic objects. Thus neither projection
has to be independent of the previously conditioned transcript.

To prove this, let \(R_0=\max(1,2B)\), and define
\[
v_*=
\min_{\substack{|a|\le R_0\\u\in[\sigma_-/2,\sigma_+]}}
\operatorname{Var}\phi(a+uG)>0.
\]
Continuity, nonconstancy, and Gaussian full support prove positivity.
For \(\tau_n=\sqrt{(r+1)/n}\), the high-leverage set in (9) has
\(o(n)\) indices. At most \(n/4\) indices have \(|b_i|>R_0\).
Thus at least \(n/2\) coordinates eventually have marginal feature
variance at least \(v_*\), so
\(\operatorname{tr}(\operatorname{Cov}h)\ge v_*n/2\).
Gaussian Poincare, applied to every scalar linear combination of \(h\),
also gives
\[
\operatorname{Cov}h\preceq s^2\sigma_+^2 I.
\]
Writing \(A_0=s\sigma_+\), it follows that
\[
\mathbb E\|Th\|^2
\ge\operatorname{tr}(T\operatorname{Cov}h)
\ge v_*n/2-kA_0^2\ge v_*n/4
\tag{28}
\]
eventually. The function \(g\mapsto\|Th\|\) is \(A_0\)-Lipschitz,
so its variance is at most \(A_0^2\). Consequently
\((\mathbb E\|Th\|)^2\ge v_*n/8\) eventually. Chebyshev gives
\[
\Pr\left\{\|Th\|<\sqrt{v_*n/32}\right\}
\le\frac{32A_0^2}{v_*n}.
\]
This proves (27) with \(c=v_*/32\). For every activation under the stated
hypotheses, the elementary bound
\[
 \|h\|\le\sqrt n\,|\phi(0)|
        +s(\|b\|+\sigma_+\|g\|)
\]
supplies a width-independent upper RMS bound with probability tending to
one.

## 5. Scope of the endpoint consequence

Suppose a separately justified approximation to the trained endpoint has,
conditional on its active transcript and the preceding query layers, the
exact final-query representation
\[
f_{\rm app}(\sqrt d\,v)=\frac1n
w^\top\phi(b+\sigma Pg),
\qquad g\sim N(0,I_n)
\]
with (1)--(2) on events whose probabilities tend to one, rank defect
\(o(n)\), and fresh \(g\) under that conditioning. Then (8) gives a
conditional small-ball bound uniform over arbitrary centers. Conditioning
further on an independent run's complete prediction and averaging yields
the same bound for their difference. For every \(\delta>0\), a fixed
positive choice of \(c=c(\delta)\) small enough in (8) therefore gives
eventual independent-run separation at scale \(c/\sqrt n\) with
probability at least \(1-\delta\), allowing a suitable split of the
failure budget.

If the approximation error for the actual endpoint is
\(o_{\mathbb P}(n^{-1/2})\) at this query, the same conclusion transfers
to the actual endpoint by reducing \(c\) and using the triangle
inequality. This last sentence is a conditional implication, not an
assertion that such an integrator or transcript has been constructed here.
The proved contribution is that arbitrary adaptive biases, arbitrary
readouts satisfying a fixed empirical fourth-moment bound, and a
sublinear projection rank defect do not obstruct the needed scalar
anti-concentration once the exact projected-Gaussian representation is
available.
