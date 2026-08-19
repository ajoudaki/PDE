# Exact positive-alpha block-metric jet

This note derives the complete fixed-order width-limit jet through order
thirteen for

\[
D_{\alpha,1}=D_a+\alpha D_u+D_W.
\]

It is a formal fixed-order statement.  It does not assume existence of a
global infinite-width trajectory or interchange a width limit with an
infinite Taylor series.

## 1. Eliminate the moving middle matrix

At width \(n\), put

\[
X_j=u_j^2,\qquad Z=n^{-1/2}WX,\qquad B=A\odot Z,
\qquad \langle v,w\rangle_n=n^{-1}v^Tw,
\]

where \(A=(a_i)\).  Feature ascent for \(D_{\alpha,1}\) is

\[
\dot A=Z^2,\qquad
\dot W=2n^{-1/2}BX^T,\qquad
\dot X=8\alpha X\odot R,
\qquad R=n^{-1/2}W^TB.
\]

Here and below products and powers of coordinate vectors are coordinatewise.
Writing \(W_0=W(0)\), exact integration of the rank-one middle-layer update
gives

\[
W(t)=W_0+\frac2{\sqrt n}\int_0^tB(s)X(s)^T\,ds.
\]

Consequently, with

\[
Y=n^{-1/2}W_0X,\qquad Q=n^{-1/2}W_0^TB,
\]

we have the two exact finite-width identities

\[
Z(t)=Y(t)+2\int_0^tB(s)\langle X(s),X(t)\rangle_n\,ds,
\tag{1}
\]

\[
R(t)=Q(t)+2\int_0^tX(s)\langle B(s),B(t)\rangle_n\,ds.
\tag{2}
\]

Thus all later uses of the random matrix are through the fixed Gaussian
matrix \(W_0\) and its transpose.

## 2. Finite-order Gaussian detransposition lemma

The following standard Gaussian-matrix fact is stated here in the precise
form used by the calculation.  A *fixed finite acyclic program* below has the
interlaced schedule

\[
G_nx_0,\ G_n^Tb_0,\ G_nx_1,\ G_n^Tb_1,\ldots,
\qquad G_n=W_0/\sqrt n.
\]

At query \(r\), every coordinate of \(x_r\) is a polynomial of uniformly
bounded degree in the column base variable and the backward fields exposed
before \(G_nx_r\); every coordinate of \(b_r\) is the analogous row
polynomial in the row base variable and the forward fields exposed through
\(G_nx_r\).  Their coefficients are finitely many empirical polynomial
averages from earlier stages.  This is exactly the dependency order of the
Taylor-coefficient program in Section 3.

**Lemma.**  Let the entries of \(W_0\) be iid standard Gaussians.  For the
fixed program just described, every empirical polynomial moment converges in
probability and in expectation to the following scalar recursion.

On the row side introduce centered jointly Gaussian symbols \(\eta_r\), and
on the column side introduce centered jointly Gaussian symbols \(\xi_r\).
The two families live on their respective scalar probability spaces and are
independent of the corresponding iid base variable.  Their covariances and
the two matrix-product rules are

\[
\mathbb E_R[\eta_r\eta_s]=\mathbb E_C[x_rx_s],\qquad
G_nx_r\ \rightsquigarrow\
\eta_r+\sum_{s<r}\mathbb E_C[\partial_{\xi_s}x_r]\,b_s,
\tag{3}
\]

\[
\mathbb E_C[\xi_r\xi_s]=\mathbb E_R[b_rb_s],\qquad
G_n^Tb_r\ \rightsquigarrow\
\xi_r+\sum_{s\le r}\mathbb E_R[\partial_{\eta_s}b_r]\,x_s.
\tag{4}
\]

Only products that precede the product being constructed occur in the sums;
the displayed index bounds are those of the interlaced order used below.

**Proof.**  Induct on the displayed query schedule, with the invariant that
every joint empirical polynomial moment of the fields constructed so far
converges in every fixed \(L^p\) needed later to the corresponding scalar
moment, and that all such moments have an \(n\)-uniform bound.  The base case
is the ordinary law of large numbers for iid polynomial Gaussian
coordinates.

Consider a forward query \(G_nx_r\); the transpose case is identical.  Write
the empirical orthogonal decomposition
\(x_r=\sum_{j<r}p_{n,j}x_j+\widetilde x_r\).  Multiplication of the projected
part by \(G_n\) gives already exposed forward fields.  Before stacking the
previous opposite-orientation inputs, replace them by a maximal nonsingular
basis in their limiting \(L^2\) quotient.  Null combinations and their
\(G_n^T\)-images vanish by the same bounded-operator-norm argument used
below, and response sums are invariant under this basis change.  Relabel
this basis as \(\mathsf B=(b_0,\ldots,b_{m-1})\), and put

\[
H_n=\langle\mathsf B,\mathsf B\rangle_n,
\qquad
(c_n)_s=\langle G_n^Tb_s,\widetilde x_r\rangle_n.
\]

Gaussian regression conditioned on the already exposed linear queries gives
the remaining conditional mean

\[
\mathsf B H_n^{-1} c_n.                                      \tag{3a}
\]

The limiting Gram matrix on the quotient basis is positive definite, so
\(H_n\) is eventually uniformly invertible.  Formula (3a) is then the
elementary conditional-normal formula applied column by column to \(G_n\).

By the induction hypothesis, \(H_n\to H\), where
\(H_{st}=\mathbb E_R[b_sb_t]\), and
\(G_n^Tb_s\rightsquigarrow\xi_s+\sum_j e_{sj}x_j\).  Empirical orthogonality
of \(\widetilde x_r\) to every prior \(x_j\) kills the displayed response sum,
so
\[
(c_n)_s\longrightarrow\mathbb E_C[\xi_s\widetilde x_r].
\]
Finite-dimensional Gaussian integration by parts,

\[
\mathbb E[\gamma_i\Phi(\gamma)]
=\sum_j\operatorname{Cov}(\gamma_i,\gamma_j)
  \mathbb E[\partial_j\Phi(\gamma)],
\]

gives

\[
c_n\longrightarrow H d,
\qquad d_t=\mathbb E_C[\partial_{\xi_t}\widetilde x_r],       \tag{3b}
\]

because
\(\mathbb E_C[\xi_s\widetilde x_r]
=\sum_{t<m}H_{st}\mathbb E_C[\partial_{\xi_t}\widetilde x_r]\).

Derivatives of an empirical coefficient of \(x_r\) with respect to one
coordinate contribute only \(O(n^{-1})\): there are finitely many such
coefficients, their degrees are fixed, and the induction moment bounds are
uniform.  They therefore vanish in (3b).  Substituting (3b) into (3a) gives
\(\sum_{s<m}d_sb_s\), the response of the residual query.  The limits
\(p_j=\lim p_{n,j}\) are deterministic functions of earlier scalar moments
when the limiting forward-input Gram matrix is nonsingular.  In the singular
case, choose a maximal nonsingular basis in the limiting \(L^2\) quotient and
discard its null combinations.  Their empirical \(L^2\) norms vanish, and so
do their \(G_n\)-images because the Gaussian \(G_n\) operator norm is bounded
in every fixed moment.  The projection coefficients converge on this quotient
basis, and every response sum is invariant modulo the discarded null
combinations.  Adding back the projected earlier queries and using their
inductively known responses turns the residual derivative into
\(\mathbb E_C[\partial_{\xi_s}x_r]\), which is exactly the response in (3).
Lifting from the quotient basis to the original \(b_s\)'s gives the same
response modulo null query combinations.  Thus no nonsingularity or
limiting-regularization assumption is needed.  Conditioning on \(\mathsf B\)
deletes the fixed-rank row projection \(P_{\mathsf B}\) from the residual
Gaussian covariance.  Since its rank \(m\) is fixed, normalized traces and
all fixed-degree Wick expansions change by \(o(1)\); mixed normalized
overlaps with \(\mathsf B\) vanish as well.

The centered innovation of the residual query is orthogonal to the earlier
same-orientation innovation span and has variance
\(\mathbb E_C[\widetilde x_r^2]\).  Recombining it with the projected earlier
Gaussian fields defines \(\eta_r\) and gives the full covariance
\(\mathbb E_R[\eta_r\eta_s]=\mathbb E_C[x_rx_s]\).  At a backward query,
\(b_r\) may depend on the just-exposed forward field \(\eta_r\); repeating
the calculation therefore includes \(s=r\) and gives exactly (4).

For completeness, the same argument can be read without conditional
notation by expanding a fixed joint moment and applying Wick's rule.  A
leading pairing of a new matrix entry with a same-orientation occurrence
produces an input overlap and hence the Gaussian covariance term.  A leading
pairing with an opposite-orientation occurrence identifies the two indices
and differentiates the coordinate polynomial carried by that occurrence,
producing the response term.  Any other identification loses at least one
free normalized index and is \(O(n^{-1})\).  Since the program is fixed and
finite, only finitely many pairings occur.  For a program variable of fixed
degree \(d\), Wick's formula and Hölder bound every fixed \(p\)-th moment by a
constant depending only on \(d,p\), and the finite program length; empirical
averages do not enlarge this bound.  This closes the induction invariant,
gives uniform integrability, and upgrades convergence to convergence in
expectation.  \(\square\)

The lemma is a finite-order statement.  Its proof does not require a
trajectory limit.

## 3. The exact scalar coefficient recurrence

Use ordinary Taylor coefficients,

\[
A(t)=\sum_{k\ge0}A_kt^k,\quad X(t)=\sum_{k\ge0}X_kt^k,
\quad\hbox{and similarly for }Y,Z,B,Q,R.
\]

Let \(a,u\) be independent standard Gaussians on the row and column scalar
spaces.  Set

\[
A_0=a,\qquad X_0=u^2.
\]

For \(k\ge0\), introduce the row Gaussian \(\eta_k\) and column Gaussian
\(\xi_k\) with

\[
\mathbb E_R[\eta_k\eta_j]=\mathbb E_C[X_kX_j],qquad
\mathbb E_C[\xi_k\xi_j]=\mathbb E_R[B_kB_j].
\tag{5}
\]

The detransposed fixed-matrix products are

\[
Y_k=\eta_k+
\sum_{j=0}^{k-1}\mathbb E_C[\partial_{\xi_j}X_k]B_j,
\tag{6}
\]

\[
Q_k=\xi_k+
\sum_{j=0}^{k}\mathbb E_R[\partial_{\eta_j}B_k]X_j.
\tag{7}
\]

Coefficient extraction from the two differential equations and (1)--(2)
gives

\[
A_k=\frac1k\sum_{p+q=k-1}Z_pZ_q,
\qquad
X_k=\frac{8\alpha}{k}\sum_{p+q=k-1}X_pR_q
\quad(k\ge1),
\tag{8}
\]

\[
B_k=\sum_{p+q=k}A_pZ_q,
\tag{9}
\]

\[
Z_k=Y_k+2
\sum_{p+q+r+1=k}
\frac{B_p\,\mathbb E_C[X_qX_r]}{p+q+1},
\tag{10}
\]

\[
R_k=Q_k+2
\sum_{p+q+r+1=k}
\frac{X_p\,\mathbb E_R[B_qB_r]}{p+q+1}.
\tag{11}
\]

There is no circular definition.  Having constructed through \(R_{k-1}\),
first (8) constructs \(A_k,X_k\).  Equations (5)--(6) then construct
\(\eta_k,Y_k\).  Equation (10) uses only \(B_p\) with \(p<k\), so it constructs
\(Z_k\), after which (9) constructs \(B_k\).  Equations (5) and (7) then
construct \(\xi_k,Q_k\), and finally (11) constructs \(R_k\); its memory sum
also contains only earlier \(X\)- and \(B\)-coefficients.

Since \(f_n=\langle A,Z^2\rangle_n\), the required fixed-order limit is

\[
F_\alpha^{(k)}(0)
=k!\,\mathbb E_R
\left[\sum_{p+q+r=k}A_pZ_qZ_r\right].
\tag{12}
\]

Apply the lemma to the finite program needed through order \(k\).  Equations
(1)--(12), induction over \(k\), and uniform integrability prove that (12)
equals

\[
\lim_{n\to\infty}\mathbb E[D_{\alpha,1,n}^{k}f_n]
\]

for every fixed \(k\le13\) (indeed, for every fixed \(k\) for which the
recurrence is run).

Each application of the generator contributes at most one factor of
\(\alpha\), so \(F_\alpha^{(k)}(0)\) has degree at most \(k\).  Also, under
simultaneous sign reversal of all initial parameters, the feature vector
field is even while \(f_n\) is odd.  Hence
\(F_\alpha(t)=-F_\alpha(-t)\) after averaging and every even jet vanishes.

## 4. Complete exact jet through order thirteen

Write

\[
F_\alpha^{(k)}(0)=\sum_r c_{k,r}\alpha^r.
\]

The nonzero coefficient rows \((c_{k,0},c_{k,1},\ldots,c_{k,k})\), in
ascending powers of \(\alpha\), are

\[
\begin{aligned}
c_1={}&(63,48),\\
c_3={}&(77760,625536,754560,227328),\\
c_5={}&(274547232,4596735744,21436337664,31088738304,\\
&\qquad17024090112,2980184064),\\
c_7={}&(2141006515200,51717526548480,443633644707840,\\
&\qquad1617194490200064,2564438160015360,1911736087216128,\\
&\qquad647577990070272,77429527805952),\\
c_9={}&(31149221916487680,926397280733921280,11228797008295759872,\\
&\qquad68120013107843407872,216157343459495804928,\\
&\qquad360293373996617170944,325383748411160788992,\\
&\qquad157873329654523232256,37777979806259871744,\\
&\qquad3369009878554116096),\\
c_{11}={}&(759035131220036321280,25594965804374979379200,\\
&\qquad383019483677094369755136,3183862200286963804176384,\\
&\qquad15561308094860120107253760,45191839708552427406360576,\\
&\qquad77732833310661790408900608,80037321953103213886439424,\\
&\qquad49156411552814847636799488,17330750388205451118379008,\\
&\qquad3157236628947852268142592,221895065540516313563136),\\
c_{13}={}&(28719223368439752070594560,1049927070983648807603404800,\\
&\qquad17931688202114583797612298240,182535682557908834998152560640,\\
&\qquad1185389301689487145264541073408,4995568087297667723007295488000,\\
&\qquad13644399097739494223476842037248,23988792318732344423548176039936,\\
&\qquad27175238485927648131807568723968,19766556153143784452713000992768,\\
&\qquad9044046194292861476093351165952,2471574150367421186553069699072,\\
&\qquad359712824603649166641664622592,20689648397930917159577321472).
\end{aligned}
\]

All rows \(c_0,c_2,c_4,c_6,c_8,c_{10},c_{12}\) are zero.  In particular,

\[
F_1^{(13)}(0)=102853512279246664353620526022656.
\]

## 5. Exact implementation and independent gates

[`block_metric_positive_alpha_jet.py`](block_metric_positive_alpha_jet.py)
implements (5)--(12) using sparse multivariate polynomials and exact Wick
recursion.  Its full gate evaluates the recurrence independently at the
fourteen integer nodes \(\alpha=0,1,\ldots,13\), reconstructs every power-basis
coefficient by exact Newton interpolation, and compares the result with the
retained coefficient table.

The following independent overlaps are also enforced:

1. every \(\beta=1\) coefficient through order nine agrees with the frozen
   125-sector Campaign-4 compiler artifact;
2. the complete \(\alpha=0\) jet through order thirteen agrees with the
   independently reduced two-variable axis recurrence;
3. the value at \(\alpha=1\) through order eleven agrees with the accepted
   canonical certificates, including
   \(F_1^{(11)}(0)=291982832387585872335470592\);
4. all even rows vanish and every row obeys the degree bound.

The machine-readable retained output is
[`BLOCK_METRIC_POSITIVE_ALPHA_JET.json`](BLOCK_METRIC_POSITIVE_ALPHA_JET.json).
