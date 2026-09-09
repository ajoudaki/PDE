# The unfrozen-readout theorem: one free source and one current kernel

Status: proved, 20 August 2026.

## 1. Result in one line

The fully trained three-hidden-layer linear network does have an exact
width-independent, one-time, restartable closure.  The most compressed
explicit packaging obtained here is one fixed pointed free-circular source,
one evolving trace-class operator
\(Q(t)\), and one scalar residual \(e(t)\):

\[
\boxed{
\begin{aligned}
\dot Q&=2\eta e\,(\mathcal C_0^*+Q^*)^3,\\
\dot e&=-2\eta e\,
 \operatorname {Tr}\!\left[
 (\mathcal C_0+Q)^3(\mathcal C_0^*+Q^*)^3
 \right].
\end{aligned}}
\tag{1.1}
\]

The prediction and full squared loss are

\[
\boxed{
f=\frac14\operatorname {Tr}(\mathcal C_0+Q)^4=y_\star-e,
\qquad \mathcal L=e^2.}
\tag{1.2}
\]

All traces in (1.1)--(1.2) are ordinary canonical Hilbert-space traces on
trace-class operators, not normalized bulk traces and not the vacuum state
\(\tau\).  There is no second training time and no history integral.  The
present pair \((Q,e)\), together with the fixed source \(\mathcal C_0\),
determines the future.

An equivalent and more interpretable version uses two vector fields, one
self-adjoint trace-class kernel, two scalars, and one fixed free product of two
Marchenko--Pastur laws.  It is given in Section 6.

## 2. Finite-width algebra

Let

\[
f_n=a^{\mathsf T}RBx,
\qquad a,x\in\mathbb R^n,\quad R,B\in\mathbb R^{n\times n}.
\tag{2.1}
\]

Feature time is ordinary gradient ascent on this multilinear feature:

\[
\begin{aligned}
a'&=RBx,&R'&=a(Bx)^{\mathsf T},\\
B'&=(R^{\mathsf T}a)x^{\mathsf T},&
x'&=B^{\mathsf T}R^{\mathsf T}a.
\end{aligned}
\tag{2.2}
\]

These are the normalized \(\mu\)P equations.  Physical full-MSE time multiplies
the four right-hand sides by \(2\eta e_n\), where
\(e_n=y_\star-f_n\).

### 2.1 One cyclic matrix

On

\[
\mathscr H_n=\mathbb R\oplus(\mathbb R^n)^{\oplus3}
\]

define

\[
\mathcal C_n=
\begin{pmatrix}
0&0&0&a^{\mathsf T}\\
x&0&0&0\\
0&B&0&0\\
0&0&R&0
\end{pmatrix}.
\tag{2.3}
\]

Every nonzero block of \((\mathcal C_n^*)^3\) is one of the four gradients in
(2.2), with the correct orientation.  Therefore

\[
\boxed{\mathcal C_n'=(\mathcal C_n^*)^3.}
\tag{2.4}
\]

Every three-step path around the four-cycle passes through the scalar node.
Consequently

\[
\operatorname {rank}\mathcal C_n^3\le4.
\tag{2.5}
\]

The four diagonal blocks of \(\mathcal C_n^4\) have the same trace, namely
\(f_n\).  Hence

\[
\boxed{f_n=\frac14\operatorname {Tr}\mathcal C_n^4.}
\tag{2.6}
\]

The squared Hilbert--Schmidt norm of (2.4) is the complete feature kernel:

\[
\begin{aligned}
K_n
&=\|(\mathcal C_n^*)^3\|_{\rm HS}^2\\
&=\|RBx\|^2+\|a\|^2\|Bx\|^2
  +\|R^{\mathsf T}a\|^2\|x\|^2
  +\|B^{\mathsf T}R^{\mathsf T}a\|^2\\
&=\operatorname {Tr}
 \bigl[\mathcal C_n^3(\mathcal C_n^*)^3\bigr].
\end{aligned}
\tag{2.7}
\]

Cyclicity of the trace gives

\[
f_n'=K_n.
\tag{2.8}
\]

### 2.2 The moment-map invariant

The self-adjoint operator

\[
\mathcal D_n=\mathcal C_n^*\mathcal C_n-
             \mathcal C_n\mathcal C_n^*
\tag{2.9}
\]

is constant.  Indeed, both Gram derivatives equal
\(\mathcal C_n^4+(\mathcal C_n^*)^4\).  Its diagonal blocks are

\[
\begin{aligned}
\|x\|^2-\|a\|^2,&\qquad B^*B-xx^*,\\
R^*R-BB^*,&\qquad aa^*-RR^*.
\end{aligned}
\tag{2.10}
\]

Thus the usual three adjacent balancedness invariants are the four blocks of
one conserved self-commutator.

## 3. The fixed source

Let

\[
\mathcal F=\mathbb C\Omega\oplus
\bigoplus_{k\ge1}(\mathbb C^6)^{\otimes k}
\tag{3.1}
\]

be full Fock space, and let \(\ell_1,\ldots,\ell_6\) be the left creation
isometries.  The first four colors encode the two matrix bulks and the last
two encode the two independent endpoint roots.  Put

\[
b=\ell_1+\ell_2^*,\qquad
r=\ell_3+\ell_4^*,\qquad
\xi_x=\ell_5\Omega,\qquad
\xi_a=\ell_6\Omega.
\tag{3.2}
\]

With the vacuum state
\(\tau(T)=\langle\Omega,T\Omega\rangle\), \(b,r\) are freely independent
variance-one circular elements.  They are the joint \(*\)-limit of the two
independent normalized real Ginibre matrices.

On

\[
\mathscr H_\infty=\mathbb C\oplus\mathcal F^{\oplus3}
\]

define the single deterministic source

\[
\boxed{
\mathcal C_0=
\begin{pmatrix}
0&0&0&\langle\xi_a,\cdot\rangle\\
|\xi_x\rangle&0&0&0\\
0&b&0&0\\
0&0&r&0
\end{pmatrix}.}
\tag{3.3}
\]

Left words in the four matrix colors preserve the final tail letter.  Hence,
for every matrix \(*\)-polynomial \(P\),

\[
\langle\xi_x,P(b,r)\xi_x\rangle
=\langle\xi_a,P(b,r)\xi_a\rangle=\tau(P),
\qquad
\langle\xi_a,P(b,r)\xi_x\rangle=0.
\tag{3.3a}
\]

Thus (3.3) records the two endpoint Gaussian vectors as genuinely orthogonal
rooted sectors, while each sector carries the same tracial circular law.

This is bounded, with \(\|\mathcal C_0\|=2\).  Its third and fourth powers
have rank at most four.  In particular, the ordinary traces used below are
well defined even though \(\mathcal C_0\) itself is not compact.

The initialization readouts are

\[
\frac14\operatorname {Tr}\mathcal C_0^4
=\langle\xi_a,rb\xi_x\rangle=0,
\qquad
\operatorname {Tr}\bigl[\mathcal C_0^3(\mathcal C_0^*)^3\bigr]=4.
\tag{3.4}
\]

The second identity has a transparent interpretation: each of the four
parameter blocks contributes one to the initial feature kernel.

### 3.1 Pointed source convergence

Let \(B_n(0),R_n(0)\) have independent \(N(0,1/n)\) entries, and let the two
endpoint vectors be independent with the same entry law.  For every fixed
compatible rooted word, its finite-width inner products converge in
probability to the corresponding vacuum inner products generated by (3.2).
The reason is as follows.

1. Independent normalized Ginibre matrices converge jointly in normalized
   \(*\)-moments and operator norm to a free circular family.
2. Conditional on the matrices, a same-root quadratic form differs from its
   normalized trace by \(o_{\mathbb P}(1)\), while a cross-root bilinear form is
   \(o_{\mathbb P}(1)\).
3. The matrix operator norms and the endpoint norms are bounded with
   probability tending to one.

The assertion is genuinely two-root pointed convergence.  If \(g_{x,n}\)
and \(g_{a,n}\) denote the two endpoint roots, then for every pair of fixed
compatible matrix words \(P_n,Q_n\) and \(i,j\in\{x,a\}\),

\[
\langle P_ng_{i,n},Q_ng_{j,n}\rangle
\longrightarrow
\langle P\xi_i,Q\xi_j\rangle.
\tag{3.4a}
\]

The right side is the appropriate same-tail vacuum moment when \(i=j\) and
zero when \(i\ne j\).  Thus this is stronger than merely giving each root
the correct marginal law; it also fixes their relative orthogonality.

For example, if \(P_n\) is a fixed bounded matrix word and \(g_n,h_n\) are
independent normalized Gaussian roots, then

\[
\operatorname {Var}
\left(g_n^*P_ng_n-\frac1n\operatorname {Tr}P_n\mid P_n\right)
\le \frac{2\|P_n\|^2}{n},
\tag{3.5}
\]

and

\[
\mathbb E\left(|g_n^*P_nh_n|^2\mid P_n\right)
\le\frac{\|P_n\|^2}{n}.
\tag{3.6}
\]

One convenient theorem supplying these matrix inputs is the
finite-fourth-moment strong-convergence result of Xiang and Zhang, *Strong
Convergence for a General Class of Random Matrix Models*, Theorem 3.3,
<https://arxiv.org/abs/2608.04824>.  Gaussian entries satisfy all its
hypotheses.  The proof below actually uses only joint fixed-word moments and
high-probability bounds on the individual matrix norms; no word degree grows
with width.
The displayed complex Fock representation is used on its canonical real
form; complex adjoints therefore represent the real transposes in the
finite model.

## 4. Autonomous trace-class theorem

Let \(\mathfrak S_1(\mathscr H_\infty)\) denote the trace-class ideal and set

\[
\mathcal C=\mathcal C_0+Q,
\qquad Q\in\mathfrak S_1.
\tag{4.1}
\]

### Theorem 4.1

For every \(\eta>0\) and \(y_\star\in\mathbb R\), the physical system

\[
\begin{aligned}
\dot Q&=2\eta e(\mathcal C^*)^3,\\
K&=\operatorname {Tr}\bigl[\mathcal C^3(\mathcal C^*)^3\bigr],\\
\dot e&=-2\eta eK,
\end{aligned}
\qquad Q(0)=0,\quad e(0)=y_\star,
\tag{4.2}
\]

has a unique global solution in
\(\mathfrak S_1(\mathscr H_\infty)\times\mathbb R\).  It preserves the cyclic
block form.  Along this solution,

\[
f=\frac14\operatorname {Tr}\mathcal C^4=y_\star-e,
\qquad \mathcal L=e^2,
\tag{4.3}
\]

and

\[
\dot f=2\eta eK,\qquad
\dot{\mathcal L}=-4\eta K\mathcal L.
\tag{4.4}
\]

The state is autonomous and restartable at every physical time.

### Proof

The map

\[
Q\longmapsto(\mathcal C_0^*+Q^*)^3
\]

takes trace class to trace class: \((\mathcal C_0^*)^3\) has rank at most
four, and every other term in the cubic expansion contains a trace-class
factor.  The trace ideal inequality and a telescoping expansion give, on
every trace-norm ball,

\[
\|A^3-B^3\|_1
\le
(\|A\|^2+\|A\|\|B\|+\|B\|^2)\|A-B\|_1.
\tag{4.5}
\]

Thus (4.2) is locally Lipschitz.  The block-cycle subspace is invariant, so
\(\operatorname {rank}\mathcal C^3\le4\) throughout the solution.
Moreover, on that subspace

\[
|K(Q)-K(\widetilde Q)|
\le \bigl(\|\mathcal C^3\|_{\rm HS}
          +\|\widetilde{\mathcal C}^{\,3}\|_{\rm HS}\bigr)
   \|\mathcal C^3-\widetilde{\mathcal C}^{\,3}\|_{\rm HS}.
\tag{4.5a}
\]

The rank-eight difference on the right is controlled by (4.5).  Hence the
coupled \((Q,e)\) vector field, not only its first component, is locally
Lipschitz with constants independent of a finite-dimensional realization.

Differentiate (4.3).  Cyclicity of the trace gives

\[
\dot f
=\operatorname {Tr}(\mathcal C^3\dot{\mathcal C})
=2\eta e\operatorname {Tr}
  [\mathcal C^3(\mathcal C^*)^3]
=2\eta eK.
\tag{4.6}
\]

Since \(f(0)=0\), equations (4.2) and (4.6) imply \(f+e=y_\star\).

It remains to exclude physical-time escape.  From (4.2),

\[
\frac d{dt}e^2=-4\eta e^2K,
\qquad
\int_0^T e^2K\,dt\le\frac{y_\star^2}{4\eta}.
\tag{4.7}
\]

Rank at most four implies

\[
\|(\mathcal C^*)^3\|_1
\le2\|(\mathcal C^*)^3\|_{\rm HS}=2\sqrt K.
\tag{4.8}
\]

Consequently

\[
\begin{aligned}
\|Q(T)\|_1
&\le4\eta\int_0^T|e|\sqrt K\,dt\\
&\le4\eta\sqrt T
  \left(\int_0^T e^2K\,dt\right)^{1/2}
\le2|y_\star|\sqrt{\eta T}.
\end{aligned}
\tag{4.9}
\]

The same calculation from any restart time \(t_0\) gives

\[
\|Q(t)-Q(t_0)\|_1
\le2\sqrt\eta\,|e(t_0)|\sqrt{t-t_0}.
\tag{4.10}
\]

Thus neither state component can escape on a finite physical interval, and
the local solution continues globally.  Uniqueness supplies the restart
semigroup property.  This proves the theorem. \(\square\)

## 5. Positive-time width identification

### Theorem 5.1

Let the finite network start from mutually independent normalized Gaussian
blocks, initialize its exact residual by
\(e_n(0)=y_\star-f_n(0)\), and let it follow full-MSE \(\mu\)P flow.  (The
limiting residual starts at \(y_\star\), because \(f_n(0)\to0\).)  For every
finite \(T\),

\[
\sup_{0\le t\le T}
\left(
|f_n(t)-f(t)|+|K_n(t)-K(t)|
+|(y_\star-f_n(t))^2-e(t)^2|
\right)
\xrightarrow{\mathbb P}0.
\tag{5.1}
\]

### Lemma 5.2: finite-root coefficient lift

At every fixed Picard depth \(m\), the iterate \(Q_n^{[m]}(t)\) is a finite
sum of rank-one operators

\[
Q_n^{[m]}(t)
=\sum_{\alpha,\beta}c_{\alpha\beta,n}^{[m]}(t)
 |w_{\alpha,n}\rangle\langle w_{\beta,n}|,
\tag{5.2}
\]

where every \(w_{\alpha,n}\) is a fixed source word in
\(B_n(0),R_n(0)\) and their transposes applied to one of the two endpoint
roots.  The word list depends on \(m\), but not on \(n\) or \(t\).  Every
coefficient is obtained from the finite two-root Gram matrix of that list by
finitely many additions, multiplications, time integrations, and—after
cutoff—continuous scalar compositions.

To prove this, note first that \((\mathcal C_n(0)^*)^3\) is a sum of four
rank-one maps between source-word vectors.  Suppose (5.2) holds at Picard
depth \(m\).  Expand
\((\mathcal C_n(0)^*+Q_n^{[m]*})^3\).  Multiplying a rank-one operator on
either side by a bulk source block appends a matrix letter to one of its word
vectors; an endpoint source block instead contributes a root contraction.
In either case the result remains in a finite two-root word span.  Multiplying
two rank-one operators contracts their adjacent word vectors to one Gram
entry and again leaves a rank-one operator.  The trace readouts contract the
remaining endpoints to further Gram entries, and time integration changes
only the scalar coefficients.  This proves the induction and, in particular,
the no-leakage statement: applying the current kernel creates no direction
outside a finite enlarged two-root word span.

The identical argument applies to the limiting Fock source.  Therefore the
two-root convergence (3.4a), rather than an unpointed normalized-trace limit,
is exactly the input needed for every fixed Picard iterate.

### Proof

Write

\[
Q_n(t)=\mathcal C_n(t)-\mathcal C_n(0).
\]

The finite and limiting equations have the same polynomial form.  On the
high-probability event where the two initialized matrix norms and endpoint
norms are bounded and \(|f_n(0)|\le1\), the finite analogue of
(4.7)--(4.9), with \(|e_n(0)|\le|y_\star|+1\), places all finite and limiting
physical states in a common deterministic trace-norm ball on \([0,T]\).
Cut the vector fields off just outside this ball.  Their bounds and Lipschitz
constants are independent of \(n\).

Fix a Picard depth \(m\).  The \(m\)-th iterate of \(Q_n\) has rank bounded by
a number depending on \(m\), not on \(n\).  Its range and co-range are spanned
by finitely many rooted words in \(B_n(0),R_n(0)\) and their transposes applied
to the two endpoint roots.  Before cutoff, every coefficient is a polynomial
in finitely many inner products of those words; after cutoff it is a
continuous function of the same finite Gram data.  Section 3.1 identifies
those Gram matrices with the Fock-space Gram matrices.  The trace norm of a
fixed finite-rank operator is likewise a continuous function of its
coefficient matrix and its two finite Gram matrices.  It follows inductively
that every fixed Picard iterate and all its \(f,K,e\) readouts converge
uniformly on \([0,T]\).

Concretely, if \(A=\sum_{ij}c_{ij}|u_i\rangle\langle v_j|\), its nonzero
singular values are those of
\(G_u^{1/2} C G_v^{1/2}\), after deleting null directions, where
\((G_u)_{ij}=\langle u_i,u_j\rangle\) and similarly for \(G_v\).  This makes
the trace-norm continuity assertion independent of any identification of the
ambient finite- and infinite-dimensional Hilbert spaces.

For a vector field with common bound \(M\) and Lipschitz constant \(H\), the
Picard tail has the dimension-free estimate

\[
\sup_{t\le T}\|z(t)-z^{[m]}(t)\|
\le MT e^{HT}\frac{(HT)^m}{(m+1)!}.
\tag{5.3}
\]

Choose \(m\) first so that (5.3) is arbitrarily small, send \(n\to\infty\),
and then remove the cutoff.  The energy bound ensures that the cutoff was
inactive with probability tending to one.  Continuity of the two trace
readouts proves (5.1). \(\square\)

This is pointed/GNS convergence, not a claim that matrices acting on
different finite-dimensional spaces converge literally in trace norm.

## 6. Equivalent free-Wishart IDE

The cyclic equation has the leaner field count of the two equivalent
constructions.  The following exact reduction makes the initialization source
and the role of the compact field more transparent.

At finite width define, on the middle hidden space,

\[
z=Bx,\qquad p=R^*a,\qquad
L=BB^*+\|x\|^2I,\qquad
M=R^*R+\|a\|^2I.
\tag{6.1}
\]

Direct differentiation gives

\[
\boxed{
z'=Lp,\qquad p'=Mz,\qquad
L'=M'=zp^*+pz^*+2\langle z,p\rangle I.}
\tag{6.2}
\]

In particular, \(M-L\) is constant and

\[
f=\langle z,p\rangle,\qquad
K=\langle p,Lp\rangle+\langle z,Mz\rangle=f'.
\tag{6.3}
\]

These formulas are on the canonical real form of the GNS/Fock spaces.  If
one merely complexifies that real system, \(f\) should be read as
\(\operatorname {Re}\langle z,p\rangle\); the trajectory itself remains in
the real form.

At finite width the two endpoint norm shifts
\(h_x=\|x\|^2-1\) and \(h_a=\|a\|^2-1\) need not be equal; their difference
is conserved and tends to zero in probability at Gaussian initialization.
Equivalently, the exact finite-width decomposition uses

\[
L=X_n+S_n+(1+h_x)I,\qquad
M=Y_n+S_n+(1+h_a)I,
\tag{6.3a}
\]

where \(X_n=B_n(0)B_n(0)^*\), \(Y_n=R_n(0)^*R_n(0)\), and the common
perturbation satisfies \(S_n'=|z_n\rangle\langle p_n|+
|p_n\rangle\langle z_n|\).  The single scalar \(h\) in the limiting IDE is
the common limit of \(h_x,h_a\), not an asserted finite-width equality.

Let \(X,Y\) be freely independent Marchenko--Pastur variables of parameter
one, whose common law is

\[
d\mu_{\rm MP}(\lambda)
=\frac1{2\pi}\sqrt{\frac{4-\lambda}{\lambda}}
 \mathbf1_{(0,4)}(\lambda)d\lambda.
\tag{6.4}
\]

Let \((\mathcal A,\tau)\) be the reduced free product of the two copies of
\(L^\infty(\mu_{\rm MP})\), and put

\[
\mathcal H=L^2(\mathcal A,\tau)\oplus L^2(\mathcal A,\tau).
\tag{6.5}
\]

The two summands record the asymptotic orthogonality of the two independent
endpoint-rooted families.  Let \(X,Y\) act by left multiplication on both
summands and initialize

\[
z_0=(X^{1/2}\Omega,0),\qquad
p_0=(0,Y^{1/2}\Omega).
\tag{6.6}
\]

For every noncommutative polynomial \(P\), these vectors obey exactly the
pointed limits

\[
\begin{aligned}
\langle z_0,Pz_0\rangle&=\tau(PX),\\
\langle p_0,Pp_0\rangle&=\tau(PY),\\
\langle z_0,Pp_0\rangle&=0.
\end{aligned}
\tag{6.7}
\]

The complete feature-time closure is

\[
\boxed{
\begin{aligned}
z'&=(I+X+hI+S)p,\\
p'&=(I+Y+hI+S)z,\\
h'&=2\langle z,p\rangle,\\
S'&=|z\rangle\langle p|+|p\rangle\langle z|,
\end{aligned}}
\tag{6.8}
\]

with \(h(0)=0\) and \(S(0)=0\).  Here

\[
S(s)\in\mathfrak S_1(\mathcal H)_{\rm sa}.
\]

The readouts are (6.3), with

\[
L=I+X+hI+S,\qquad M=I+Y+hI+S.
\tag{6.9}
\]

Multiplying the first four right-hand sides by \(2\eta e\) and adjoining
\(e'=-2\eta eK\) gives the physical-time IDE.  It has two vector fields, one
trace-class kernel field, and the two scalars \(h,e\), all on one fixed source.

The initialization in (6.7) follows directly from conditional Gaussian
concentration.  For instance,

\[
(Bx)^*P(Bx)
=x^*B^*PBx
\longrightarrow\frac1n\operatorname {Tr}(PBB^*)
\longrightarrow\tau(PX).
\tag{6.10}
\]

### 6.1 Positivity lift

The lower bounds used below are intrinsic, rather than an assumption on the
kernel solution.  On the same two-copy Hilbert space set

\[
x_0=(\Omega,0),\qquad a_0=(0,\Omega),\qquad
B_0=X^{1/2},\qquad R_0=Y^{1/2},
\tag{6.11}
\]

where the two positive multiplication operators act diagonally on the two
copies.  Evolve

\[
a'=RBx,\qquad R'=|a\rangle\langle Bx|,\qquad
B'=|R^*a\rangle\langle x|,\qquad x'=B^*R^*a.
\tag{6.11a}
\]

Its reduced variables have exactly the initialization and vector field
(6.8).  Uniqueness therefore identifies this lift with the solution of
(6.8), while the definitions in (6.1) give

\[
L=BB^*+\|x\|^2I\ge(1+h)I,
\qquad
M=R^*R+\|a\|^2I\ge(1+h)I.
\tag{6.12}
\]

Here \(\|x\|^2=\|a\|^2=1+h\), because the two norms start equal and both
have derivative \(2f\) in feature time.  This also proves that (6.8) retains
the positivity hidden by its affine \(I+X+hI+S\) notation.

### 6.2 Explicit scalar-kernel coordinates

The free product in (6.5) is a fully explicit fixed spatial domain.  Let

\[
H_X^0=H_Y^0=L^2(\mu_{\rm MP})\ominus\mathbb C1.
\]

Then

\[
L^2(\mathcal A,\tau)
=\mathbb C\Omega\oplus
\bigoplus_{\ell\ge1}\;
\bigoplus_{c_1\ne\cdots\ne c_\ell}
H_{c_1}^0\otimes\cdots\otimes H_{c_\ell}^0,
\tag{6.13}
\]

where \(c_j\in\{X,Y\}\).  With two colors, reduced words alternate.
Choosing the orthonormal MP polynomials \(p_k\),

\[
\lambda p_0=p_0+p_1,\qquad
\lambda p_k=p_{k+1}+2p_k+p_{k-1}\quad(k\ge1),
\tag{6.14}
\]

makes \(X,Y\) fixed sparse nearest-neighbor/tree operators.  Writing the
coefficients of \(z,p\) as fields \(Z(w),P(w)\) and the coefficients of
\(S\) as a kernel \(S(w,w')\), equation (6.8) is the scalar IDE

\[
\begin{aligned}
\partial_s Z(w)
 &=[(I+X+hI)P](w)+\sum_{w'}S(w,w')P(w'),\\
\partial_s P(w)
 &=[(I+Y+hI)Z](w)+\sum_{w'}S(w,w')Z(w'),\\
\partial_s h&=2\sum_w Z(w)P(w),\\
\partial_sS(w,w')&=Z(w)P(w')+P(w)Z(w').
\end{aligned}
\tag{6.15}
\]

There are two copies of the word domain for the two endpoint colors.  The
sums are Hilbert-space and trace-class contractions.  The domain, source
operators, and field count never grow with width, Taylor order, or elapsed
time.

Equivalently, (1.1) itself is a one-kernel IDE on a four-matrix-letter Fock
tree with two fixed endpoint-tail sectors.  If \(A\star B\) denotes kernel
composition and \(A^\dagger\) the adjoint kernel, then

\[
\partial_tQ=2\eta e(\mathcal C_0^\dagger+Q^\dagger)^{\star3},
\tag{6.16}
\]

with the trace readouts (1.1)--(1.2).  This displays explicitly that the
operator notation packages one current spatial kernel, not a temporal
memory.

## 7. Global loss convergence

The physical solution in Theorem 4.1 satisfies

\[
e(t)\longrightarrow0,\qquad f(t)\longrightarrow y_\star.
\tag{7.1}
\]

For \(y_\star=0\), the limiting state is stationary.  Suppose first that
\(y_\star>0\).  In the positive lift underlying (6.8),

\[
L,M\ge(1+h)I.
\tag{7.2}
\]

Consequently, with \(f=\langle z,p\rangle\),

\[
K\ge(1+h)(\|z\|^2+\|p\|^2)
\ge2|f|.
\tag{7.3}
\]

Indeed, \(e(t)=y_\star\exp(-2\eta\int_0^tK)\) and
\(f=y_\star-e\), so \(ef\ge0\).  Since
\(\dot h=4\eta ef\), one has \(h\ge0\), which justifies the last inequality
for either sign of the label.

The output obeys

\[
\dot f=2\eta(y_\star-f)K,
\qquad f(0)=0,\quad \dot f(0)=8\eta y_\star>0.
\tag{7.4}
\]

After any positive time, comparison with the logistic equation using (7.3)
gives \(f(t)\to y_\star\).  For \(y_\star<0\), put \(g=-f\) and \(E=-e\).
Then \(E=|y_\star|-g>0\), while the lift gives
\(K\ge2|f|=2g\); hence \(g\) obeys the same logistic comparison.  Once
\(|f|\ge|y_\star|/2\), this bound gives an exponential upper bound on
\(|e|\).  Thus the loss tends to zero exponentially after a finite transient.

On its maximal feature-time interval, the feature curve is strictly
increasing and its range is all of \(\mathbb R\).  This is a range statement,
not a claim of global existence in feature time.  Indeed,

\[
f'=K>0,\qquad q'=2f,\qquad
K\ge2q|f|,\quad q=\|a\|^2=\|x\|^2.
\tag{7.5}
\]

For positive time \(f>0\) and grows at least exponentially after any
\(s_0>0\); the reversed-time argument treats negative time.  The conserved
Gram differences bound the middle operator norms in terms of \(q\), so a
finite feature endpoint with bounded \(f,q\) would be continuable.  Hence
the feature curve reaches every finite label before any feature-time
singularity.  Physical time approaches the unique point where \(f=y_\star\)
and never reaches the feature singularity.

## 8. Why the source cannot be made into ordinary marginal spectra

The need for a noncommutative spatial source is real; it is not caused by the
proof method.

At initialization the two bulk operators in (6.8) are \(I+X\) and \(I+Y\),
where \(X,Y\) are free MP variables.  Their commutator has order-one size:

\[
\tau([X,Y]^*[X,Y])=2.
\tag{8.1}
\]

Indeed,

\[
\tau(X^2Y^2)=4,\qquad \tau(XYXY)=3.
\tag{8.2}
\]

For commuting classically independent variables with the same marginals,
both quantities would equal four.  Thus separate MP spectra, or a commuting
joint eigenvalue law, already gives a wrong ordered fourth moment.

Even the ordinary spectrum of the cyclic matrix is insufficient.  At width
one, the two states

\[
(a,R,B,x)=(1,1,1,1),\qquad
(a,R,B,x)=(2,1,1,1/2)
\]

both have cyclic characteristic polynomial \(\lambda^4-1\), but their
feature kernels are respectively

\[
4\qquad\text{and}\qquad25/4.
\tag{8.3}
\]

Separate layer Gram spectra fail just as concretely.  Let
\(a=x=e_1\), \(R=\operatorname {diag}(1,2,3)\), and let \(B_2,B_3\) be
rotations through the same angle \(\theta\), respectively in the
\(1\!-\!2\) and \(1\!-\!3\) planes.  Both choices have
\(B_j^*B_j=B_jB_j^*=I\), the same remaining Gram data and endpoint norms,
and the same output \(f=\cos\theta\).  Writing
\(c=\cos\theta\), \(s=\sin\theta\), however,

\[
K(B_2)=3+c^2+4s^2,
\qquad
K(B_3)=3+c^2+9s^2.
\tag{8.3a}
\]

Thus even the instantaneous loss derivative depends on relative orientation,
or equivalently on a mixed noncommutative word not contained in the marginal
spectra.

There is also a sharp finite-moment no-go statement.  Let a classical
word-moment closure consist of finitely many finite linear combinations of
same-time contraction graphs, with a polynomial or analytic state-universal
vector field and no Borel encoding.  No such finite scalar closure containing
\(f\) is invariant.  To see this, put

\[
C=B^*R^*RB.
\]

In the formal feature derivation, \(\delta^{2m-1}f\) contains with positive
coefficient the connected word

\[
x^*C^m x,\qquad m=1,2,\ldots.
\tag{8.4}
\]

It is obtained by differentiating the left endpoint once and then
alternating the two endpoint derivatives while leaving the two matrices
undifferentiated.  Products and analytic functions of finitely many scalar
contraction coordinates produce disjoint unions of only the finitely many
connected graphs already present; they cannot produce the infinitely many
linearly independent connected paths in (8.4).  Hence a finite scalar moment
list cannot close state-universally.

This does not claim an impossibility against pathological encodings of an
entire law into one real number.  It proves the relevant point: ordinary
spectral marginals and every finite polynomial/Krylov moment list fail.  The
fixed free source plus the one current trace-class field in (1.1) retains
exactly the missing ordered information.

If the trace-class field is eliminated from (6.8), then

\[
S(s)=\int_0^s
\bigl(|z(r)\rangle\langle p(r)|+|p(r)\rangle\langle z(r)|\bigr)dr.
\tag{8.5}
\]

Substitution creates terms involving
\(\langle z(r),z(s)\rangle\) and
\(\langle p(r),p(s)\rangle\).  Those are precisely forbidden two-time
kernels.  Keeping \(S(s)\) as a present-time spatial field is the Markovian
compression of that information.

## 9. Independent coefficient audit

The free-Wishart recurrence (6.8), constructed before comparison, gives

\[
F(s)=4s+\frac{80}{3}s^3+\frac{1736}{15}s^5+O(s^7).
\tag{9.1}
\]

Therefore

\[
\boxed{F'(0)=4,\qquad F^{(3)}(0)=160,\qquad
F^{(5)}(0)=13888.}
\tag{9.2}
\]

This agrees exactly with the independent Gaussian-program table.  The local
test suite verifies the two orthogonal Fock root sectors, (2.4),
(2.6)--(2.10), (6.2)--(6.3), and (9.2).

## 10. Exact scope

Proved here:

- the finite-width cyclic and central reductions;
- the explicit one-source trace-class ODE and scalar-kernel IDE;
- local and global physical-time well-posedness;
- direct output, kernel, residual, and loss readouts;
- compact-physical-time finite-width convergence in probability;
- convergence of the limiting loss to zero;
- failure of ordinary spectral marginals and finite scalar moment lists.

Not claimed:

- finite numerical storage rather than a finite number of continuum fields;
- a one-dimensional commuting spectral quadrature like the depth-two result;
- global existence of the unscaled feature-time factor flow;
- uniformity when width and physical time tend to infinity jointly;
- an all-order Stieltjes theorem.

The new phenomenon at the unfrozen readout is therefore completely isolated:
depth two has one commuting spectral source, whereas depth three needs one
fixed noncommutative source.  It still admits an exact, autonomous, O(1)-field,
one-time closure.
