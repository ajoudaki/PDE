# Arctangent depth two: an autonomous pointed-action IDE

Status: proved and independently audited, 21 August 2026.

## 1. Result

Consider one unit-normalized sample, scalar label \(y_\star\), equal hidden
width \(n\), and the activation

\[
\phi(x)=\arctan x
\]

at both hidden layers.  On \(H_n=\mathbb R^n\), use
\(\langle v,w\rangle_n=n^{-1}v^{\mathsf T}w\).  Let the coordinates of
\(A_0,u_0\) and the entries of \(W_0\) be mutually independent standard
Gaussians, and put \(G_0=W_0/\sqrt n\).  The predictor is

\[
 f_n(A,u,G)=\langle A,\arctan\{G\arctan(u)\}\rangle_n.    \tag{1.1}
\]

The parameter metric is part of the model.  The \(A\)- and \(u\)-blocks use
the normalized \(H_n\) metric, while the \(G\)-block uses the ordinary
Frobenius metric \(\operatorname{tr}(M^{\mathsf T}N)\).  Equivalently, the
three layerwise learning-rate scalings have already been absorbed into these
metrics.  This is the mean-field feature-learning scaling used throughout;
using the ordinary Euclidean metric on all three blocks would give a
different collection of powers of \(n\).

There is a deterministic, autonomous, restartable infinite-width system with
two current vector fields, one trace-class operator perturbation, one scalar
residual, and one immutable pointed Gaussian action source.  It contains no
second training time and no history kernel.  Its current state directly gives
the predictor, tangent kernel, residual, and loss.

The source is specified in Section 4 by the deterministic master law of every
finite marked straight-line program in one Ginibre action and its adjoint.
This is stronger than an ordinary free \(*\)-law and is not an ordinary
graphon kernel.

### Theorem 1.1

The feature system (5.1) below has a unique global feature-time solution in
the Gaussian-envelope class of Definition 6.1 and a unique global physical
MSE trajectory for every \(\eta>0\) and \(y_\star\in\mathbb R\).  For every
finite \(T\),

\[
\sup_{0\le t\le T}
\left\{|f_n(t)-f(t)|+|K_n(t)-K(t)|
+|(y_\star-f_n(t))^2-e(t)^2|\right}
\xrightarrow[n\to\infty]{\mathbb P}0.                  \tag{1.2}
\]

The limiting readouts obey

\[
 f(t)=y_\star-e(t),\qquad \mathcal L(t)=e(t)^2,
 \qquad \dot{\mathcal L}=-4\eta K\mathcal L.             \tag{1.3}
\]

The theorem remains true after multiplying \(\arctan\) by any fixed positive
constant, including the constant that makes its Gaussian output variance
one.  Section 10 keeps the unscaled activation because its formulas are
cleanest.

## 2. Exact natural-coordinate algebra

Define

\[
 \Theta(u)=u+\frac{u^3}{3},\qquad r=\Theta(u),
 \qquad \iota=\Theta^{-1}.                               \tag{2.1}
\]

The inverse is global and explicit:

\[
 \iota(r)=2\sinh\left\{\frac13\operatorname{arsinh}
 \left(\frac{3r}{2}\right)\right\}.                    \tag{2.2}
\]

For \(U\sim N(0,1)\), the transformed seed is square integrable:

\[
 \mathbb E\Theta(U)^2
 =\mathbb E\left(U^2+\frac23U^4+\frac19U^6\right)
 =\frac{14}{3}.                                         \tag{2.2a}
\]

Set

\[
 \Psi(r)=\arctan\iota(r),\qquad
 c(r)=\frac1{1+\iota(r)^2},\qquad
 d(z)=\frac1{1+z^2}.                                    \tag{2.3}
\]

All three maps are bounded and globally Lipschitz.  Moreover,

\[
 \Psi'(r)=c(r)^2.                                       \tag{2.4}
\]

Given \((A,r,G)\), define the current fields

\[
 X=\Psi(r),\quad Z=GX,\quad Y=\arctan Z,
 \quad B=A\odot d(Z),\quad Q=G^*B.                      \tag{2.5}
\]

For \((b\otimes x)v=b\langle x,v\rangle_n\), exact feature ascent is

\[
\boxed{A'=Y,\qquad r'=Q,\qquad G'=B\otimes X.}          \tag{2.6}
\]

Indeed, the original input equation is
\(u'=\phi'(u)G^*B\), while \(\Theta'=1/\phi'\); hence
\(r'=G^*B\).  This is an exact invertible change of parameter, not a modified
gradient rule.

For completeness, if \(dG\) is a matrix variation, then

\[
 df=\langle Y,dA\rangle_n+\langle B,dG\,X\rangle_n
       +\langle c(r)Q,du\rangle_n,
\]

and

\[
 \langle B,dG\,X\rangle_n
 =\operatorname{tr}\!\left[\left(n^{-1}BX^{\mathsf T}\right)^{\mathsf T}
 dG\right].                                             \tag{2.6a}
\]

Thus \(B\otimes X=n^{-1}BX^{\mathsf T}\) is exactly the Frobenius gradient,
not an unnormalized outer product.  Also, \(r'=Q\) is the coordinate transform
of the \(u\)-gradient flow; it is not gradient ascent in the Euclidean
\(r\)-metric.

Differentiating the forward fields gives

\[
 X'=c(r)^2Q,
 \qquad Z'=B\langle X^2\rangle_n+G\{c(r)^2Q\}.           \tag{2.7}
\]

Consequently

\[
 \boxed{f_n=\langle A,Y\rangle_n,}                       \tag{2.8}
\]

and

\[
 \boxed{
 K_n=\langle Y^2\rangle_n
 {}+\langle B^2\rangle_n\langle X^2\rangle_n
 {}+\langle c(r)^2Q^2\rangle_n=f_n'.}                   \tag{2.9}
\]

Every term is a squared parameter-gradient norm.  In particular \(K_n\ge0\).
The finite identity has also been checked by central differentiation at
independent random states; that test is only a check on (2.6)--(2.9), not
evidence for the width limit.

## 3. Dimension-free a-priori bounds

Let \(a=\pi/2\).  Since

\[
 |X|,|Y|\le a,\qquad |B|\le|A|,
\]

every feature trajectory on \([-S,S]\) satisfies

\[
 \|A(s)\|_2\le \|A_0\|_2+a|s|,                          \tag{3.1}
\]

\[
 \|G(s)-G_0\|_1
 \le a\left\{\|A_0\|_2|s|+\frac a2s^2\right\},         \tag{3.2}
\]

and

\[
 \|r(s)\|_2\le\|r_0\|_2
 +\int_0^{|s|}\|G(\sigma)\|_{\rm op}
 \{\|A_0\|_2+a\sigma\}\,d\sigma.                     \tag{3.3}
\]

The same inequalities hold at finite width, with the normalized vector norm
and the operator trace norm.  They exclude finite feature-time escape and
are uniform on the usual high-probability initialization event

\[
 \|A_0\|_2+\|r_0\|_2+\|G_0\|_{\rm op}\le C.             \tag{3.4}
\]

The kernel is finite on every compact interval because

\[
 0\le K\le a^2+a^2\|A\|_2^2
 +\|G\|_{\rm op}^2\|A\|_2^2.                            \tag{3.5}
\]

There is also a pointwise fact that will be decisive for uniqueness:

\[
 |A_i(s)-A_i(0)|\le a|s|.                                \tag{3.6}
\]

Thus training translates, but never degrades, the Gaussian tail of the
readout field.

## 4. The immutable pointed Gaussian action source

An ordinary kernel limit cannot represent \(G_0\).  If the finite matrix is
written as a kernel on the uniform \(n\)-point probability space, its kernel
\(L^2\) norm is the matrix Frobenius norm, of order \(\sqrt n\), while its
operator action remains order one.  We instead use the following marked
action source.

### 4.1 Finite programs

A two-sorted source program starts with an independent row Gaussian mark
\(a_0\), a column Gaussian mark \(u_0\), and constants.  It permits:

1. application of one matrix letter \(g\) from columns to rows and its
   adjoint \(g^*\);
2. finite linear combinations whose scalar coefficients are previous
   normalized inner products;
3. coordinatewise pseudo-Lipschitz functions (of any fixed finite degree);
   and
4. normalized inner products of same-sort fields.

At width \(n\), substitute \((A_0,u_0,G_0)\).  Only a fixed finite number of
operations is permitted in one program.

### Lemma 4.1 (finite two-sided program theorem)

Let \(v_n^1,\ldots,v_n^m\) be any same-sort vector list produced by one fixed
finite source program, and let

\[
 \mu_n=\frac1n\sum_{i=1}^n
 \delta_{(v^1_{n,i},\ldots,v^m_{n,i})}.
\]

There is a deterministic probability law \(\mu\) such that, for each fixed
pseudo-Lipschitz test \(\zeta\), almost surely,

\[
 \int \zeta\,d\mu_n\longrightarrow\int\zeta\,d\mu       \tag{4.1}
\]

for every pseudo-Lipschitz \(\zeta\) of arbitrary fixed polynomial degree.
Every program scalar also converges almost surely to a deterministic limit.
In particular, the empirical vector laws converge in \(W_p\) for every fixed
finite \(p\).  The conclusion includes adaptive alternating reuse of
\(G_0\) and \(G_0^*\), and it does not require the limiting query Gram matrix
to be invertible.

#### Proof and verification of the imported theorem

This is Theorem B.4 (the \(\textsc{Netsor}^{\mathsf T+}\) Master Theorem) in
Yang--Littwin, specialized to one square Gaussian matrix.  That theorem
allows MATMUL by a matrix and its transpose, coordinatewise NONLIN
operations, and MOMENT scalars that may parameterize later operations.  It
concludes (4.1) for every pseudo-Lipschitz test, not merely bounded tests.
Its Gaussian-regression definition uses the Moore--Penrose inverse when an
earlier-query covariance is singular.  The extended core-set/rewrite theorem
in the proof of the underlying Tensor Programs III Master Theorem handles
degenerate limiting query Grams; Moore--Penrose notation alone is not being
used as a proof of rank stability.

Every hypothesis is met here:

1. \((A_0,u_0)\) has iid centered Gaussian coordinate pairs and is independent
   of \(G_0\), whose entries are iid \(N(0,1/n)\).
2. The initialization \(r_0=\Theta(u_0)\) is a cubic NONLIN operation.
   The maps \(\Psi,c,d,\arctan\), and every readout cutoff are Lipschitz;
   \((a,z)\mapsto a d(z)\), finite linear combinations, products used in
   inner products, and the moment tests below are pseudo-Lipschitz of finite
   degree.
3. Every scalar-only dependence is continuous, and the program is finite
   before the width limit is taken.

For intuition, if earlier right queries are the columns of \(V\), earlier
left queries are the columns of \(P\), and one conditions on \(G_0V\) and
\(G_0^*P\), Gaussian conditioning gives

\[
 G_0=M+P_{\operatorname{span}(P)^\perp}\,\widetilde G\,
             P_{\operatorname{span}(V)^\perp},          \tag{4.2}
\]

where \(M\) is the minimum-Frobenius-norm compatible mean and
\(\widetilde G\) is an independent Ginibre matrix.  The mean term is the
non-vanishing transpose-memory contribution; replacing it by a fresh
Gaussian response would be wrong.  The cited theorem iterates (4.2),
including rank-degenerate cases.  Finally, (4.1) for \(|x|^p\), together
with weak convergence, is the moment criterion for \(W_p\) convergence.
\(\square\)

### 4.2 Deterministic realization

Restrict first to programs with rational constants and a countable family of
pseudo-Lipschitz scalar functions containing

\[
 \Theta,\iota,\Psi,c,d,\arctan,
\]

and all integer readout cutoffs, and dense under uniform convergence on
compact sets among bounded Lipschitz cylinder functions.  This is one
countable universal program language.  Couple the triangular arrays for all
widths on one product probability space; this changes none of their
finite-width laws and lets the almost-sure statements be intersected.
Lemma 4.1 gives a deterministic law for every finite same-sort tuple.  These
laws are projectively consistent: put any two finite expression sets into
their finite union program and take the exact finite-width marginals.  The
countable intersection of its probability-one events gives simultaneous convergence
of every finite program in this language.  Kolmogorov extension
therefore realizes all row expressions on a probability space
\((\Omega_R,\mathcal F_R,\mathbb P_R)\) and all column expressions on
\((\Omega_C,\mathcal F_C,\mathbb P_C)\).  Exact finite program identities
hold almost surely in these realizations because their squared errors have
zero limiting moment.

Let \(\mathcal D_R,\mathcal D_C\) be the linear spans of the resulting
program fields, quotient their zero-norm subspaces, and close them.  Bounded
Lipschitz cylinder functions are dense in the corresponding generated
\(L^2\) spaces, so these closures may and will be taken as

\[
 H_R=L^2(\Omega_R),\qquad H_C=L^2(\Omega_C).             \tag{4.3}
\]

The associated commutative probability algebras are
\(\mathcal A_R=L^\infty(\Omega_R)\) and
\(\mathcal A_C=L^\infty(\Omega_C)\); unbounded marks such as \(a_0,r_0\)
are understood as affiliated measurable variables in \(L^0\), lying in
\(L^2\) when used as Hilbert fields.  Bounded functional calculus acts on all
of \(L^2\); an unbounded coordinate map is used only on its natural
integrability domain.  Thus coordinatewise nonlinearities are part of the
source structure and are not inferred from an operator's
unitary-equivalence class.

On the dense program domains define

\[
 \Gamma[p]=[gp],\qquad \Gamma^\dagger[q]=[g^*q].         \tag{4.4}
\]

These maps are well defined.  Indeed, for every finite linear combination
\(p\) and its finite-width representative \(p_n\), the finite inequality

\[
 \|G_0p_n\|_2\le\|G_0\|_{\rm op}\|p_n\|_2
\]

and the standard Gaussian spectral-norm theorem
\(\|G_{0,n}\|_{\rm op}\to2\) almost surely give

\[
 \|\Gamma p\|_2\le2\|p\|_2.                            \tag{4.5}
\]

This spectral-norm input is separate from Lemma 4.1; empirical program laws
alone cannot detect an exceptional singular direction.

Thus a zero-norm formal input has a zero-norm output, and \(\Gamma\) extends
uniquely to a bounded map \(H_C\to H_R\).  The identical argument applies to
\(\Gamma^\dagger\).  Passing the exact finite identity
\(\langle G_0p,q\rangle_n=\langle p,G_0^*q\rangle_n\) to the limit shows
that \(\Gamma^\dagger=\Gamma^*\).  Bounded Lipschitz coordinate functional
calculus extends by \(L^2\) continuity.  Multiplication by a bounded field
also preserves \(L^2\), which covers \(A d(Z)\).

This constructs the deterministic source

\[
 \boxed{\mathfrak G=(H_R,H_C;a_0,r_0,\Gamma),
 \qquad r_0=u_0+u_0^3/3.}                                \tag{4.6}
\]

It is a projective law of current *actions*, not a projective law of all
time-indexed trajectories.  Its definition is independent of the label,
learning rate, and future solution.

The generated source is canonical up to the only equivalence that matters: a pair of
probability-algebra isometries preserving \(a_0,r_0\), coordinatewise
functional calculus, and intertwining \(\Gamma\).  Any two realizations with
the master laws of Lemma 4.1 are isometric on their dense program fields and
hence on the completions.  Consequently every IDE trajectory and readout
below is realization-independent and is a full-sequence deterministic
limit, not a selected ultralimit.

We call convergence of all finite-program empirical laws in every finite
\(W_p\), together with their MOMENT scalars, **strong pointed-action
convergence**.  Lemma 4.1 proves that the finite marked sources converge to
\(\mathfrak G\) in this topology.  This statement concerns the countable
convergence-determining class; weak convergence plus convergence of every
integer moment then yields each requested finite \(W_p\) statement.  No operator-norm convergence of embedded
finite matrices is claimed or needed; such convergence would be impossible
because finite-rank operators cannot converge in operator norm to the
noncompact Ginibre action.

## 5. The autonomous IDE

Let \(q\in\mathfrak S_1(H_C,H_R)\), put \(G=\Gamma+q\), and use (2.5) with
the source probability-space functional calculus.  Feature time is

\[
\boxed{
 A'=Y,\qquad r'=Q,\qquad q'=B\otimes X.}                 \tag{5.1}
\]

Equivalently,

\[
 q(s)=\int_0^s B(\sigma)\otimes X(\sigma)\,d\sigma,     \tag{5.1a}
\]

as a Bochner integral in trace norm.  This is the integral part of the IDE:
all past rank-one updates are compressed into the single current operator
\(q(s)\), so no two-time field is retained.

The physical full-MSE system is

\[
\boxed{
\begin{aligned}
 \dot A&=2\eta eY,\\
 \dot r&=2\eta eQ,\\
 \dot q&=2\eta e\,B\otimes X,\\
 \dot e&=-2\eta eK,
\end{aligned}}                                           \tag{5.2}
\]

initialized by

\[
 A(0)=a_0,\qquad r(0)=r_0,
 \qquad q(0)=0,\qquad e(0)=y_\star.                     \tag{5.3}
\]

Lemma 4.1 gives \(f(0)=0\): the centered row mark \(a_0\) is independent of
\((u_0,G_0)\) before the first program operation.  Hence the residual in
(5.3) is exactly \(y_\star-f(0)=y_\star\).

The readouts are (2.8)--(2.9), with the source expectations in place of
finite empirical averages, and \(\mathcal L=e^2\).

## 6. Existence and uniqueness

### Definition 6.1 (Gaussian-envelope solution)

On a compact feature interval \(I\), a solution of (5.1) belongs to the
Gaussian-envelope class if

\[
 A(s)=a_0+\alpha(s),\qquad
 \sup_{s\in I}\|\alpha(s)\|_\infty<\infty,              \tag{6.1}
\]

and \(A,r\) are strongly continuous in \(L^2\), \(q\) is strongly continuous
in trace norm, and the integral equations associated with (5.1) hold.  This
class is stable under restart because the source mark \(a_0\) is immutable.

### Lemma 6.2 (Gaussian multiplier modulus)

Let \(a\) have a bounded sub-Gaussian Orlicz norm and let \(h\) be bounded
and Lipschitz.  On every bounded range of \(\|z\|_2+\|\widetilde z\|_2\),

\[
 \|a\{h(z)-h(\widetilde z)\}\|_2
 \le C\,\omega(\|z-\widetilde z\|_2),                   \tag{6.2}
\]

where, for small \(\delta\),

\[
 \omega(\delta)=\delta\sqrt{\log(e/\delta)},
 \qquad \int_{0^+}\frac{d\delta}{\omega(\delta)}=\infty. \tag{6.3}
\]

#### Proof

The Orlicz assumption implies \(\|a\|_{2p}\le C\sqrt p\).  Put
\(w=h(z)-h(\widetilde z)\).  Then
\(\|w\|_2\le L\delta\), while \(\|w\|_\infty\le2\|h\|_\infty\).
For \(p\ge2\), Hölder and interpolation give

\[
 \|aw\|_2
 \le C\sqrt p\,\|w\|_{2p/(p-1)}
 \le C\sqrt p\,(L\delta)^{1-1/p}
 (2\|h\|_\infty)^{1/p}.                                 \tag{6.4}
\]

Choose \(p\) comparable to \(\log(e/\delta)\).  The reciprocal-integral
claim follows after the substitution \(x=\log(e/\delta)\).  \(\square\)

### Proposition 6.3 (global feature well-posedness)

System (5.1) has a unique global Gaussian-envelope solution.

#### Proof

First replace \(a_0\) by its coordinatewise cutoff \(a_0^{(M)}\).  On
\([-S,S]\), (3.6) gives

\[
 \|A^{(M)}(s)\|_\infty\le M+aS.                          \tag{6.5}
\]

Clip the occurrence of \(A\) in the vector field just outside this bound.
The resulting vector field on

\[
 H_R\oplus H_C\oplus\mathfrak S_1(H_C,H_R)
\]

is locally Lipschitz: \(\Psi,\arctan,d\) are Lipschitz, multiplication by
the clipped \(A\) is bounded, and

\[
 \|b\otimes x\|_1=\|b\|_2\|x\|_2.                      \tag{6.6}
\]

Picard--Lindelof gives a unique local solution, the clip is inactive by
(6.5), and (3.1)--(3.3) continue it for all feature time.

Now compare two cutoff solutions, or two putative Gaussian-envelope
solutions.  On an a-priori ball let

\[
 \Delta=\|A-\widetilde A\|_2
 +\|r-\widetilde r\|_2+\|q-\widetilde q\|_1.             \tag{6.7}
\]

The bounded Lipschitz maps give

\[
 \|X-\widetilde X\|_2+\|Z-\widetilde Z\|_2
 +\|Y-\widetilde Y\|_2\le C\Delta.                     \tag{6.8}
\]

The only non-Lipschitz-looking term is

\[
 B-\widetilde B=(A-\widetilde A)d(Z)
 +\widetilde A\{d(Z)-d(\widetilde Z)\}.                 \tag{6.9}
\]

Equation (3.6) and Lemma 6.2 therefore give

\[
 \|B-\widetilde B\|_2\le C\{\Delta+\omega(C\Delta)\}.  \tag{6.10}
\]

Applying \(G^*\), and using (6.6) for the operator equation, yields

\[
 \Delta(s)\le\Delta(0)
 +C_S\int_0^{|s|}\{\Delta(\sigma)+
 \omega(C_S\Delta(\sigma))\}\,d\sigma.                \tag{6.11}
\]

Bihari--Osgood proves uniqueness and continuous dependence.  It also makes
the cutoff solutions Cauchy because
\(\|a_0^{(M)}-a_0\|_2\to0\).  Their limit solves (5.1), satisfies (6.1), and
is global by (3.1)--(3.3).

There is also a quantitative cutoff check which does not rely on a slogan
about Gaussian tails.  Comparing levels \(N>M\), write the analogue of
(7.11) with the level-\(M\) solution in the multiplier position.  Ordinary
Gronwall gives, on \([-S,S]\),

\[
 d(U^{(N)},U^{(M)})\le C_Se^{C_SM}
 \|a_0^{(N)}-a_0^{(M)}\|_2.                             \tag{6.12}
\]

The Gaussian clipping tail is \(O((1+M)e^{-M^2/4})\), which beats the
exponential factor in (6.12).  This independently verifies cutoff existence
and will be used uniformly in width in Section 7.3.  \(\square\)

### Proposition 6.4 (kernel regularity)

Along the solution, \(f\) is continuously differentiable, \(K\) is finite
and continuous, and \(f'=K\).

#### Proof

All chain rules first hold for the bounded cutoffs.  The state and \(B,Q\)
converge strongly in \(L^2\) when the readout cutoff is removed.  If
\(r_j\to r\) and \(Q_j\to Q\) in \(L^2\), then

\[
 c(r_j)Q_j\to c(r)Q\quad\hbox{in }L^2:                  \tag{6.13}
\]

the term containing \(Q_j-Q\) is immediate, while bounded convergence in
measure, dominated by \(Q^2\), treats the other term.  Thus all three terms
of (2.9) converge and the identity passes from the cutoffs.  The same
argument with time increments gives continuity.  \(\square\)

## 7. Positive-time width identification

### 7.1 Fixed readout cutoff

Fix \(M,S<\infty\) and initialize with \(A_{0,n}^{(M)}\).  On the event
(3.4), with \(\|G_{0,n}\|_{\rm op}\le L\), the finite and limiting vector
fields have bounds and Lipschitz constants depending only on \(M,S,L\).
The Gaussian norm theorem and the laws of large numbers for \(A_0,r_0\)
make the complements of these events tend to zero.  Approximate the finite
and limiting integral equations by the same Euler scheme with mesh \(h\).

Eliminating the current matrix at mesh step \(k\) gives exactly

\[
 G^kX^k=G_0X^k
 +\sum_{\ell<k}hB^\ell\langle X^\ell,X^k\rangle,         \tag{7.1}
\]

\[
 (G^k)^*B^k=G_0^*B^k
 +\sum_{\ell<k}hX^\ell\langle B^\ell,B^k\rangle.        \tag{7.2}
\]

Thus every fixed mesh is one finite source program.  Lemma 4.1 identifies
all of its vector laws, all moments of fixed order, and all Gram data.  Its
trained operator is a fixed finite sum of rank-one maps; the nonzero singular
values and trace norm of such a sum are continuous functions of the two
finite Gram matrices.  They therefore converge as well.

The standard Euler estimate on the common Lipschitz ball is dimension free:
indeed, writing tildes for a second cutoff state,

\[
\begin{aligned}
 \|X-\widetilde X\|_2
 &\le L_\Psi\|r-\widetilde r\|_2,\\
 \|Z-\widetilde Z\|_2
 &\le \|G\|_{\rm op}\|X-\widetilde X\|_2
   +\|q-\widetilde q\|_1\|\widetilde X\|_2,\\
 \|B-\widetilde B\|_2
 &\le \|A-\widetilde A\|_2
   +(M+aS)L_d\|Z-\widetilde Z\|_2,\\
 \|Q-\widetilde Q\|_2
 &\le \|G\|_{\rm op}\|B-\widetilde B\|_2
   +\|q-\widetilde q\|_1\|\widetilde B\|_2,\\
 \|B\otimes X-\widetilde B\otimes\widetilde X\|_1
 &\le \|B-\widetilde B\|_2\|X\|_2
   +\|\widetilde B\|_2\|X-\widetilde X\|_2.
                                                               \tag{7.3}
\end{aligned}
\]

The a-priori bounds make every coefficient on the right a function only of
\(M,S,L\).  The vector field is also uniformly bounded there, so its value
along a solution is Lipschitz in time.  The usual discrete Gronwall proof for
explicit Euler therefore gives, for a deterministic \(C=C(M,S,L)\),

\[
 \sup_{|s|\le S}d\{U_{n,M}(s),U^h_{n,M}(s)\}\le Ch       \tag{7.3a}
\]

on that event, where \(d\) uses the two vector \(L^2\) norms and the trace
norm of \(q\).  The same estimate holds in the source space.  Choose \(h\)
first, send \(n\to\infty\) by Lemma 4.1, and then send \(h\downarrow0\).
This proves compact-time convergence of every fixed finite set of current
actions in the joint \(W_2\)/Gram action topology and uniform convergence of
\(f_n\).  It does not yet pass an arbitrary unbounded polynomial readout;
the one additional raw readout claimed here, \(K_n\), is handled explicitly
next.

### 7.2 Energy tightness for the kernel

The only additional issue for uniform convergence of \(K_n\) is the square
of

\[
Q_n=G_n^*B_n.                                           \tag{7.4}
\]

Let \(Q^h_{n,M}(s)\) be the value obtained from the Euler state at the nearest
mesh point.  It belongs to a finite set of finite-program fields.  For any
fixed \(\varepsilon>0\), Lemma 4.1 applied to
\(\zeta(q)=|q|^{2+\varepsilon}\) gives, in probability,

\[
 \max_{s\in h\mathbb Z\cap[-S,S]}
 \langle |Q^h_{n,M}(s)|^{2+\varepsilon}\rangle_n\le C_{h,M,S}
                                                               \tag{7.5}
\]

outside an event whose probability tends to zero.  The common Euler estimate
and local Lipschitz bound for \(Q\) give

\[
 \lim_{h\downarrow0}\limsup_{n\to\infty}
 \Pr\left\{\sup_{|s|\le S}
 \|Q_{n,M}(s)-Q^h_{n,M}(s)\|_2>Ch\right\}=0.             \tag{7.6}
\]

This really implies square uniform integrability; it is stronger than an
\(L^2\) bound.  Pointwise, for arbitrary \(q,v\) and \(R>0\),

\[
 q^2\mathbf1_{\{|q|>R\}}
 \le4(q-v)^2+2v^2\mathbf1_{\{|v|>R/2\}}.                \tag{7.7}
\]

Apply (7.7) with \(q=Q_{n,M}(s)\), \(v=Q^h_{n,M}(s)\),
then use (7.5)--(7.6) and Markov's inequality.  It follows that

\[
 \lim_{R\to\infty}\limsup_{n\to\infty}
 \Pr\left\{\sup_{|s|\le S}
 \langle Q_{n,M}(s)^2\mathbf1_{\{|Q_{n,M}(s)|>R\}}\rangle_n
 >\delta\right\}=0                                    \tag{7.8}
\]

for every \(\delta>0\).  Thus adaptive column concentration is excluded for
the actual cutoff trajectory, rather than assumed away.

The quantifier order is: fix \(M\), choose \(h\) so that (7.6) is small,
take \(n\to\infty\) for that finite program, and then take \(R\to\infty\)
using (7.5).  Only after the continuous cutoff theorem is established is
\(M\to\infty\) taken in Section 7.3.  No moment bound is asserted uniformly
over an increasing number of program steps.

At fixed mesh the complete scalar

\[
 \langle c(r^h_{n,M})^2(Q^h_{n,M})^2\rangle_n
\]

is itself a MOMENT output; Lemma 4.1 supplies the required *joint* empirical
law of \((r^h,Q^h)\) and convergence of this polynomially growing test.  To
remove the mesh, one must not combine (7.5) with a direct Hölder estimate:
the moment constant \(C_{h,M,S}\) is allowed to diverge as \(h\downarrow0\).
Instead first use (7.7)--(7.8) to obtain square-tail tightness for the exact
continuous trajectory, and then truncate the multiplier estimate.

More precisely, put

\[
 D_h^Q=\sup_{|s|\le S}\|Q_{n,M}(s)-Q^h_{n,M}(s)\|_2,
 \qquad
 D_h^r=\sup_{|s|\le S}\|r_{n,M}(s)-r^h_{n,M}(s)\|_2 .
\]

Both are \(O_{\mathbb P}(h)\), uniformly in \(n\), by (7.3a).  Since \(c\)
is bounded and globally Lipschitz, for every fixed truncation level \(R\),

\[
\begin{aligned}
 &\sup_{|s|\le S}
 \|\{c(r_{n,M})-c(r^h_{n,M})\}Q^h_{n,M}\|_2^2\\
 &\quad\le L_c^2R^2(D_h^r)^2
 +\sup_{|s|\le S}
 \langle (Q^h_{n,M})^2
 \mathbf1_{\{|Q^h_{n,M}|>R\}}\rangle_n\\
 &\quad\le L_c^2R^2(D_h^r)^2+4(D_h^Q)^2
 +2\sup_{|s|\le S}
 \langle Q_{n,M}^2
 \mathbf1_{\{|Q_{n,M}|>R/2\}}\rangle_n .              \tag{7.9}
\end{aligned}
\]

Choose \(R\) first using (7.8), and then let \(h\downarrow0\).  Together
with

\[
 \|c(r_{n,M})Q_{n,M}-c(r^h_{n,M})Q^h_{n,M}\|_2
 \le D_h^Q+
 \|\{c(r_{n,M})-c(r^h_{n,M})\}Q^h_{n,M}\|_2,
\]

and the uniform \(L^2\) bounds on \(Q\), this proves uniform-in-time
convergence of the weighted squared norm.  Notice the two different
quantifier orders: (7.8) is proved by choosing one auxiliary \(h\) and then
letting \(R\to\infty\); after (7.8) has been established, (7.9) chooses
\(R\) before sending the comparison mesh to zero.  No estimate uniform in
the number of Euler steps is asserted or needed.

Consequently

\[
 c(r_n)^2Q_n^2
\]

passes to the limit uniformly in time.  The other two kernel terms are
easier: \(X,Y\) are bounded and \(|B|\le|A|\).
This proves, at fixed cutoff,

\[
 \sup_{|s|\le S}\{|f_{n,M}(s)-f_M(s)|
 +|K_{n,M}(s)-K_M(s)|\}\xrightarrow{\mathbb P}0.         \tag{7.10}
\]

### 7.3 Remove the cutoff

There is a simpler width-uniform comparison than a direct cavity estimate.
Write \(U_n=(A_n,r_n,q_n)\), let \(U_{n,M}\) start from
\(A_{0,n}^{(M)}=\operatorname{clip}(A_{0,n},[-M,M])\), and decompose

\[
 A_nd(Z_n)-A_{n,M}d(Z_{n,M})
 =(A_n-A_{n,M})d(Z_n)
 +A_{n,M}\{d(Z_n)-d(Z_{n,M})\}.                         \tag{7.11}
\]

On \([-S,S]\), \(\|A_{n,M}\|_\infty\le M+aS\).  On the
high-probability a-priori event (3.4), all remaining coefficients are bounded
independently of \(n,M\).  Ordinary Gronwall applied to (7.11) and the other
two equations therefore gives

\[
 \sup_{|s|\le S}\left\{d(U_n(s),U_{n,M}(s))
 +\|Q_n(s)-Q_{n,M}(s)\|_2\right}
 \le C_S e^{C_SM}\|A_{0,n}-A_{0,n}^{(M)}\|_2.           \tag{7.12}
\]

For \(N\sim N(0,1)\),

\[
 \left\{\mathbb E|N-\operatorname{clip}(N,[-M,M])|^2\right\}^{1/2}
 \le C(1+M)e^{-M^2/4}.                                  \tag{7.13}
\]

The expectation of the squared empirical norm on the right of (7.12) is
exactly the scalar expectation in (7.13).  Since
\(e^{C_SM-M^2/4}\to0\), Markov's inequality and the vanishing complement of
the a-priori event yield

\[
 \lim_{M\to\infty}\limsup_{n\to\infty}
 \Pr\left\{\sup_{|s|\le S}
 \left(\|A_n-A_{n,M}\|_2+\|r_n-r_{n,M}\|_2
 +\|G_n-G_{n,M}\|_1+\|Q_n-Q_{n,M}\|_2\right)
 >\varepsilon\right\}=0.                                \tag{7.14}
\]

The same comparison holds for the limiting cutoff solutions.  It gives
uniform convergence of \(f\).  It also transfers the square-energy tightness
of Section 7.2 from a fixed large cutoff to the original \(Q_n\): the
elementary tail inequality (7.7) applies with \(Q_n,Q_{n,M}\).  Estimate
(7.9) then passes the weighted square term, with the cutoff level in place
of the mesh.  Explicitly, if
\(\Delta_{n,M}^Q=\sup_s\|Q_n-Q_{n,M}\|_2\), then

\[
\begin{aligned}
 &\sup_s\|\{c(r_n)-c(r_{n,M})\}Q_{n,M}\|_2^2\\
 &\quad\le L_c^2R^2\sup_s\|r_n-r_{n,M}\|_2^2
 +4(\Delta_{n,M}^Q)^2
 +2\sup_s\langle Q_n^2\mathbf1_{\{|Q_n|>R/2\}}\rangle_n . \tag{7.15}
\end{aligned}
\]

First establish the uncut square-tail statement from (7.7), (7.8), and
(7.14); then choose \(R\) in (7.15), and only afterwards let \(M\to\infty\).
Thus every term of \(K_n\) converges uniformly.  Combining
(7.5)--(7.15) proves the
feature-time form of Theorem 1.1.

## 8. Physical time and the loss

Let \(F(s)\) and \(K(s)=F'(s)\) denote the limiting feature readouts.  Since
\(K\ge0\), define the physical clock by

\[
 \dot s=2\eta\{y_\star-F(s)\},\qquad s(0)=0.             \tag{8.1}
\]

The right side is locally Lipschitz because \(F\in C^1\).  If
\(e=y_\star-F(s)\), then

\[
 \dot e=-2\eta eK(s),
 \qquad e(t)=y_\star\exp\left\{-2\eta\int_0^tK(s(\tau))d\tau\right\}. \tag{8.2}
\]

Thus \(|e(t)|\le|y_\star|\), so

\[
 |s(t)|\le2\eta|y_\star|t.                              \tag{8.3}
\]

The global feature trajectory therefore supplies a unique global physical
trajectory.  The chain rule gives (5.2), and

\[
 f+e=y_\star                                             \tag{8.4}
\]

because the derivative vanishes and the source initialization has
\(f(0)=0\).

Conversely, for any Gaussian-envelope solution of (5.2), set
\(s(t)=2\eta\int_0^t e(\tau)d\tau\).  Feature-flow uniqueness identifies its
three state fields with the feature solution at \(s(t)\); differentiating
\(f+e\) gives zero, so its clock is exactly (8.1).  This proves uniqueness of
the autonomous physical system itself, including the case in which \(e\)
reaches zero and the state becomes stationary.

At finite width use \(e_n(0)=y_\star-f_n(0)\).  Conditional on the other
initial fields,

\[
 \mathbb E\{f_n(0)^2\mid u_0,G_0\}
 \le\frac{a^2}{n},                                      \tag{8.5}
\]

so \(f_n(0)\to0\) in probability.  The finite clocks have a common compact
feature-time image on every finite physical interval with probability tending
to one.  Uniform feature convergence and scalar ODE stability identify the
clocks, and composition proves (1.2).

Equation (8.4) also proves the internal constraint without treating the clock
as externally supplied.  The current quadruple \((A,r,q,e)\), together with
the immutable source, determines its own future.

## 9. Why arctangent is the selected sweet spot

The natural-coordinate observation applies to every strictly monotone
activation with a global map

\[
 \Theta(u)=\int_0^u\frac{d\xi}{\phi'(\xi)}.              \tag{9.1}
\]

It removes the inner back-propagated multiplier exactly.  The remaining
outer multiplier can be controlled if the output is bounded, because then
the Gaussian readout changes by a bounded pointwise amount.

Arctangent is the minimal algebraic member of this class.  If one asks for

\[
 \phi'(u)=\frac1{P(u)}                                   \tag{9.2}
\]

with a positive polynomial \(P\), boundedness of \(\phi\) requires degree at
least two.  The lowest-degree even choice is \(P(u)=1+u^2\), which gives
\(\phi=\arctan\) and the cubic seed (2.1).

More precisely, degree zero gives an affine unbounded activation, and a
nonconstant odd-degree polynomial cannot be positive on both tails.  Every
strictly positive quadratic has the form
\(a\{(u-h)^2+s^2\}\), so integrating its reciprocal gives an affine input/
output transform of arctangent.  Thus arctangent is the unique
minimal-degree member of the reciprocal-positive-polynomial class, up to
those affine equivalences; it is not claimed to be the unique viable
activation among all functions.

The alternatives fail or cost more:

* \(x^2\) has a very short polynomial contract, but unbounded forward and
  derivative fields permit rare-coordinate kernel concentration.
* tanh has the same bounded-output mechanism, but (9.1) gives
  \(\Theta(u)=u/2+\sinh(2u)/4\), an exponentially transformed Gaussian seed.
  Although that seed has finite polynomial moments under a Gaussian input,
  the transform is not pseudo-Lipschitz of finite degree and therefore falls
  outside the finite-program theorem used in Section 4.
* sine is bounded and entire, but \(\phi'\) vanishes, so (9.1) is not a global
  coordinate.
* a residual activation \(x+\lambda\tanh x\) has a good global coordinate,
  but its unbounded forward channel no longer gives (3.6).
* genuine piecewise-linear activations avoid smooth multiplier growth but
  introduce attracting and repelling kink surfaces.  A fixed choice of the
  derivative at a kink can give nonexistence or nonuniqueness already at
  finite width; a Filippov selection is a different model and can make the
  raw kernel selection-dependent.
* softsign, \(u/(1+|u|)\), is a genuine close competitor: it is bounded,
  \(C^{1,1}\), and has the piecewise-polynomial natural coordinate
  \(u+u|u|+u^3/3\).  It is not demonstrably easier, because its cusp requires
  an extra regularity case, whereas arctangent is smooth.

This comparison does not claim that arctangent is the only admissible
activation.  It proves that it meets the contract with the lowest-complexity
global conjugacy found in the audited classes.

## 10. Optional unit-variance scaling

Let

\[
 \sigma^2=\mathbb E\{\arctan(G)^2\},\qquad G\sim N(0,1),
\]

and take \(\phi(x)=\arctan(x)/\sigma\).  Then
\(\mathbb E\phi(G)^2=1\).  The natural coordinate becomes

\[
 \Theta_\sigma(u)=\sigma\left(u+\frac{u^3}{3}\right).   \tag{10.1}
\]

Every proof above is unchanged after inserting the fixed factors
\(\sigma^{\pm1}\).  In particular, \(r=\Theta_\sigma(u)\) is required to
retain \(r'=G^*B\); keeping the unscaled \(r\) instead would insert a factor
\(1/\sigma\).  Because the scaled activation occurs in both layers, every
feature and derivative occurrence must be rescaled consistently—the kernel
does not acquire one single global power of \(\sigma\).  Unit-variance
normalization is therefore a convention, not a separate convergence
assumption.

## 11. Claim boundary

The theorem proves an O(1)-field autonomous closure, not a finite-dimensional
scalar ODE.  The fixed pointed action source contains the full one-time
Ginibre action law needed by all future adaptive queries.  It is more
structured than a single spectral measure and less compressed than the
linear network's cyclic trace-class equation.

The result is specific to the canonical iid-Gaussian initialization and its
Gaussian-envelope restart class.  It does not claim continuous dependence
for every ambient \(L^2\) sequence; deterministic spike states can defeat
such a universal statement.  It does not use formal Taylor convergence,
DMFT, a response function, or a two-time kernel.

Five qualifications are essential.

1. The three initialization families \(A_0,u_0,G_0\) are mutually
   independent.  Correct one-dimensional marginals with cross-family
   correlations do not satisfy Lemma 4.1.
2. The source topology is the strong marked program topology of Section 4,
   including the cubic mark \(r_0\) and moments above order two.  Weak action,
   ordinary operator-moment, or operator/trace-norm bounds alone do not
   control adaptive coordinate spikes or the raw kernel.
3. Restartability means restarting \((A,r,q,e)\) while retaining the same
   immutable \(\mathfrak G\).  Refreshing or forgetting \(\Gamma\) discards
   the transpose memory and is a different evolution.
4. The convergence proof uses permutation-equivariant queries generated by
   the displayed network.  It does not assert square-energy tightness for an
   arbitrary adversarial bounded query of a Ginibre matrix; Section 7.2
   proves it for this trajectory through finite-program approximation.
5. Global well-posedness and monotone loss do not by themselves assert
   interpolation as \(t\to\infty\).  The theorem is a compact-time width
   limit; it makes no claim that \(e(t)\to0\) without an additional
   long-time lower bound on the accumulated kernel.

## References used for the finite-program source lemma

* Greg Yang, *Tensor Programs II: Neural Tangent Kernel for Any Architecture*,
  arXiv:2006.14548.
* Greg Yang and Etai Littwin, *Tensor Programs IIb: Architectural
  Universality of Neural Tangent Kernel Training Dynamics*, PMLR 139 (2021),
  Supplement, Theorem B.4.
* Greg Yang and Edward J. Hu, *Tensor Programs IV: Feature Learning in
  Infinite-Width Neural Networks*, PMLR 139 (2021), 11727--11737.
* Greg Yang, *Tensor Programs III: Neural Matrix Laws*,
  arXiv:2009.10685.

Only the fixed finite-program master law is imported.  The continuous-time
passage, Gaussian cutoff removal, kernel-energy tightness, and physical-clock
argument are Sections 6--8 above.
