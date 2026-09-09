# A joint width/gradient-flow limit for a three-hidden-layer nonlinear MLP

## 1. Statement

Fix integers \(p,d\ge1\).  Let

\[
\mathcal D=\{(x_a,y_a):1\le a\le p\},\qquad
x_a\in\mathbb R^d,\quad \|x_a\|^2=d,\quad y_a\in\{-1,1\},
\]

and assume that the \(x_a\)'s are pairwise distinct.  The dataset, \(p\), and
\(d\) are fixed while the common hidden width \(n\) tends to infinity.

Consider the bias-free three-hidden-layer network

\[
\begin{aligned}
U_i^a&=w_i^\top x_a, & H_{1,i}^a&=\phi(U_i^a),\\
S_{2,j}^a&=\sum_{i=1}^n B_{2,ji}H_{1,i}^a,
&H_{2,j}^a&=\phi(S_{2,j}^a),\\
S_{3,k}^a&=\sum_{j=1}^n B_{3,kj}H_{2,j}^a,
&H_{3,k}^a&=\phi(S_{3,k}^a),\\
f_{n,a}&=\sum_{k=1}^n c_kH_{3,k}^a,
&L_n&=\frac1p\sum_{a=1}^p(f_{n,a}-y_a)^2,
\end{aligned}
\tag{1.1}
\]

with the fixed non-affine activation

\[
\phi(z)=\sin z+\cos z.
\tag{1.2}
\]

Initialize all displayed coordinates independently by

\[
w_i(0)\sim N(0,I_d/d),\qquad
B_{2,ji}(0),B_{3,kj}(0)\sim N(0,1/n),\qquad
c_k(0)\sim N(0,n^{-4}).
\tag{1.3}
\]

Use exact full-batch gradient descent with base step

\[
\eta_n=n^{-2}
\tag{1.4}
\]

and layer mobilities

\[
\lambda_{w,n}=n/d,\qquad
\lambda_{B_2,n}=\lambda_{B_3,n}=1,
\qquad \lambda_{c,n}=1/n.
\tag{1.5}
\]

Thus every raw layer step tends to zero.  In particular,

\[
\eta_n\lambda_{w,n}=\frac1{dn}\longrightarrow0,
\qquad
\eta_n\lambda_{B_\ell,n}\longrightarrow0,
\qquad
\eta_n\lambda_{c,n}\longrightarrow0.
\]

Let \(C=nc\).  There is a deterministic number \(T_0(p)>0\), specified in
Lemma 5.4 below, and a unique autonomous three-sorted action-operator flow on
\([0,T_0]\) such that the following hold along the full sequence \(n\to\infty\).

1. The exact-GD interpolation at time \(t=k\eta_n\) converges in probability,
   uniformly on \([0,T]\) for every \(T\le T_0\), in the current-action
   topology defined in Section 4.
2. The empirical path laws of \(U,S_2,S_3\) converge in
   \(W_2(C([0,T];\mathbb R^p))\).
3. The four NTK blocks, the output vector, the loss, and all three hidden
   velocity energies converge uniformly or in the corresponding integrated
   topology.
4. There is a dataset-dependent \(T_*\in(0,T_0]\) such that on every
   \((0,T]\), \(T\le T_*\), all three hidden layers have finite positive
   variance, positive integrated velocity, and nonzero macroscopic
   displacement; all four parameter blocks have positive integrated NTK
   activity; the non-affine regression residual is positive in all three
   hidden layers; the full NTK matrix is nonconstant; and \(L(T)<L(0)\).

Here kernel motion means motion of the full \(p\times p\) NTK matrix.  The
proof will in fact show motion of its quadratic form in the fixed label
direction.  No assertion about motion of its trace is needed.

The proof has five parts.  Sections 2--3 derive the exact finite-width
dynamics and the fixed-mesh Gaussian response program.  Section 4 constructs
the limiting current action state and the cutoff flow.  Section 5 proves the
all-source response estimate that permits removal of both cutoffs.  Sections
6--7 establish the joint exact-GD limit and every strict activity property.

## 2. Exact finite-width equations

Write

\[
\langle u,v\rangle_n=\frac1n u^\top v,
\qquad
u\otimes_n v=\frac1nuv^\top,
\qquad
\gamma=\frac2p.
\]

For every sample define

\[
\begin{aligned}
D_3^a&=C\odot\phi'(S_3^a),
&P_2^a&=B_3^\top D_3^a,\\
D_2^a&=\phi'(S_2^a)\odot P_2^a,
&P_1^a&=B_2^\top D_2^a,\\
e_a&=f_a-y_a,
&f_a&=\langle C,H_3^a\rangle_n.
\end{aligned}
\tag{2.1}
\]

Direct differentiation of (1.1), with the mobilities (1.5), gives the exact
finite-width gradient-flow system

\[
\boxed{
\begin{aligned}
\dot w_i&=-\frac\gamma d\sum_{a=1}^p
 e_a\phi'(U_i^a)P_{1,i}^a x_a,\\
\dot B_2&=-\gamma\sum_{a=1}^p e_aD_2^a\otimes_nH_1^a,\\
\dot B_3&=-\gamma\sum_{a=1}^p e_aD_3^a\otimes_nH_2^a,\\
\dot C&=-\gamma\sum_{a=1}^p e_aH_3^a.
\end{aligned}}
\tag{2.2}
\]

Equivalently, with

\[
R_{ab}=\frac{x_a^\top x_b}{d},
\]

the first preactivation satisfies

\[
\dot U_i^a=-\gamma\sum_{b=1}^p
e_bR_{ab}\phi'(U_i^b)P_{1,i}^b.
\tag{2.3}
\]

The four exact NTK blocks are

\[
\Theta^{(1)}_{ab}
=R_{ab}\left\langle
\phi'(U^a)P_1^a,\phi'(U^b)P_1^b
\right\rangle_n,
\tag{2.4}
\]

\[
\Theta^{(2)}_{ab}
=\langle H_1^a,H_1^b\rangle_n
 \langle D_2^a,D_2^b\rangle_n,
\tag{2.5}
\]

\[
\Theta^{(3)}_{ab}
=\langle H_2^a,H_2^b\rangle_n
 \langle D_3^a,D_3^b\rangle_n,
\tag{2.6}
\]

\[
\Theta^{(4)}_{ab}=\langle H_3^a,H_3^b\rangle_n.
\tag{2.7}
\]

Every block is positive semidefinite.  If
\(\Theta=\sum_{r=1}^4\Theta^{(r)}\), the chain rule gives

\[
\dot f=-\gamma\Theta e,
\qquad
\dot L=-\gamma^2 e^\top\Theta e\le0.
\tag{2.8}
\]

The normalization is therefore balanced: all four metric gradients have
finite normalized squared norms whenever the fields in (2.1) have finite
second moments.

## 3. Fixed-mesh Gaussian program and reused-adjoint responses

Two temporary cutoffs are needed.  Let \(\tau_R\in C^\infty(\mathbb R)\)
satisfy

\[
\tau_R(z)=z\ (|z|\le R),\qquad
|\tau_R(z)|\le |z|,\qquad
|\tau_R(z)|\le R+1,\qquad
|\tau_R'(z)|\le1.
\tag{3.1}
\]

In the cutoff system replace

\[
D_2^a=\phi'(S_2^a)P_2^a
\quad\hbox{by}\quad
D_{2,R}^a=\phi'(S_2^a)\tau_R(P_2^a),
\tag{3.2}
\]

and replace \(P_1^a\) by \(\tau_R(P_1^a)\) only in (2.2)'s \(w\)-equation.
All other definitions are unchanged.  We suppress the subscript \(R\) until
Section 5.

Fix a mesh \(h>0\) and a finite number \(N\) of simultaneous Euler steps.
Summing the two matrix updates exactly gives, for \(\ell=2,3\),

\[
B_{\ell,k}=B_{\ell,0}
-\gamma h\sum_{r<k}\sum_{b=1}^p
 e_{r,b}D_{\ell,r}^b\otimes_nH_{\ell-1,r}^b.
\tag{3.3}
\]

Consequently,

\[
\begin{aligned}
S_{\ell,k}^a
={}&B_{\ell,0}H_{\ell-1,k}^a\\
&-\gamma h\sum_{r<k,b}e_{r,b}D_{\ell,r}^b
 \langle H_{\ell-1,r}^b,H_{\ell-1,k}^a\rangle_n,
\end{aligned}
\tag{3.4}
\]

and

\[
\begin{aligned}
P_{\ell-1,k}^a
={}&B_{\ell,0}^\top D_{\ell,k}^a\\
&-\gamma h\sum_{r<k,b}e_{r,b}H_{\ell-1,r}^b
 \langle D_{\ell,r}^b,D_{\ell,k}^a\rangle_n.
\end{aligned}
\tag{3.5}
\]

Thus every fixed \((R,h,N)\) trajectory is a finite computation using only
the two independent initial Gaussian matrices and their transposes,
coordinate maps, and normalized empirical moments.

We use the following finite-program lemma.  It is stated in exactly the form
needed below.

**Theorem 3.1 (the finite Tensor-Program master theorem).**  A finite program
has three sorts of variables: width-\(n\) vectors, scalars, and independent
matrices with iid \(N(0,\sigma_A^2/n)\) entries.  Its instructions are
matrix or transpose-matrix multiplication, coordinatewise `Nonlin`, and
normalized empirical `Moment`.  Initial vector coordinates are iid copies of
one fixed finite-dimensional Gaussian vector, and initial scalars converge
almost surely to deterministic limits.  Suppose every `Nonlin` and every
`Moment` having a vector argument is pseudo-Lipschitz jointly in its vector
and scalar arguments, and every scalar-only `Moment` is continuous.  Then,
for every fixed finite program, every finite joint empirical coordinate law
converges almost surely against every pseudo-Lipschitz test, and every scalar
in the program converges almost surely to the scalar prescribed by the
recursive \(Z\)-rules.

For a matrix instruction, those rules say that a product \(Ax\), after
\(A^\top\) has already been queried on vectors \(y_r\), has limiting
coordinate representation

\[
Z^{Ax}=\widehat Z^{Ax}
+\sum_r Z^{y_r}\,
\mathbb E\frac{\partial Z^x}
 {\partial\widehat Z^{A^\top y_r}},
\tag{3.6}
\]

where the hatted family is centered Gaussian with covariance
\(\sigma_A^2\mathbb E[Z^xZ^{x'}]\).  The analogous identity holds with
\(A,A^\top\) interchanged.  The derivative is the *syntactic* derivative:
one first writes the coordinate random variable as the deterministic function
of the named hatted sources generated by the actual program and then
differentiates that function.  Thus the rule does not invert a query Gram and
remains meaningful when hatted sources are linearly dependent.  Equivalently,
the derivative expectation can be defined by the Moore--Penrose/Stein formula;
both definitions give the same correction.

This is Theorem G.4 together with Setup G.2, Definition G.3, Remarks L.1--L.2,
and Assumption L.4 of Yang--Hu, *Tensor Programs IV* (2021).  The source states
the initialization rules, almost-sure pseudo-Lipschitz empirical convergence,
the syntactic derivative convention, the singular-covariance Stein formula,
and the regularity assumptions explicitly
([master theorem](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf#page=13),
[regularity and singular-source convention](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf#page=20)).

All hypotheses hold here.  The two matrices in (1.3) are independent and
have the prescribed variance; the columns of \(w(0)\), viewed across neurons,
are jointly Gaussian; and \(C(0)=n^{-1}g\), with \(g\) an independent standard
Gaussian vector, is an allowed initial vector multiplied by a scalar tending
to zero.  For fixed \((R,h,N)\), (3.3)--(3.5) replace every trained-matrix
product by the corresponding initial-matrix product, coordinate maps, and
`Moment` scalars.  The functions \(\phi,\phi',\tau_R\), finite sums, products,
and the squared-loss derivative are pseudo-Lipschitz; scalar-only operations
are continuous.  The program is finite.  Hence Theorem 3.1 applies.  Notice
that it asserts nothing uniform when \(N\to\infty\); that passage is proved
separately in Section 4.

Serialize a time step in the order

\[
H_1\to B_{2,0}H_1\to S_2,H_2
\to B_{3,0}H_2\to S_3,D_3
\to B_{3,0}^\top D_3\to P_2,D_2
\to B_{2,0}^\top D_2\to P_1.
\tag{3.7}
\]

Let \(\widehat S_{\ell,k}^a\) and
\(\widehat P_{\ell-1,k}^a\) denote the forward and adjoint hatted Gaussian
sources belonging to \(B_{\ell,0}\).  Lemma 3.1 gives the four exact limiting
representations

\[
\begin{aligned}
S_{2,k}^a={}&\widehat S_{2,k}^a
+\sum_{r<k,b}\alpha_{2;ka,rb}D_{2,r}^b
-\gamma h\sum_{r<k,b}e_{r,b}D_{2,r}^bq_{2;rb,ka},\\
P_{1,k}^a={}&\widehat P_{1,k}^a
+\sum_{r\le k,b}\beta_{2;ka,rb}H_{1,r}^b
-\gamma h\sum_{r<k,b}e_{r,b}H_{1,r}^br_{2;rb,ka},\\
S_{3,k}^a={}&\widehat S_{3,k}^a
+\sum_{r<k,b}\alpha_{3;ka,rb}D_{3,r}^b
-\gamma h\sum_{r<k,b}e_{r,b}D_{3,r}^bq_{3;rb,ka},\\
P_{2,k}^a={}&\widehat P_{2,k}^a
+\sum_{r\le k,b}\beta_{3;ka,rb}H_{2,r}^b
-\gamma h\sum_{r<k,b}e_{r,b}H_{2,r}^br_{3;rb,ka},
\end{aligned}
\tag{3.8}
\]

where

\[
q_{\ell;rb,ka}=\mathbb E[H_{\ell-1,r}^bH_{\ell-1,k}^a],
\quad
r_{\ell;rb,ka}=\mathbb E[D_{\ell,r}^bD_{\ell,k}^a],
\tag{3.9}
\]

and

\[
\begin{aligned}
\alpha_{2;ka,rb}&=\mathbb E\frac{\partial H_{1,k}^a}
 {\partial\widehat P_{1,r}^b},
&\beta_{2;ka,rb}&=\mathbb E\frac{\partial D_{2,k}^a}
 {\partial\widehat S_{2,r}^b},\\
\alpha_{3;ka,rb}&=\mathbb E\frac{\partial H_{2,k}^a}
 {\partial\widehat P_{2,r}^b},
&\beta_{3;ka,rb}&=\mathbb E\frac{\partial D_{3,k}^a}
 {\partial\widehat S_{3,r}^b}.
\end{aligned}
\tag{3.10}
\]

Every empirical moment scalar in (3.8) is held fixed in these formal source
derivatives.  The ranges \(r<k\) for \(\alpha\) and \(r\le k\) for \(\beta\)
are forced by the query order (3.7), and include the contemporaneous adjoint
response.

## 4. Current action state and the fixed-cutoff flow

There are three neuron populations.  For each one, enumerate the countable
grammar generated by its current marks, rational linear combinations, the
named bounded coordinate maps, normalized moments, and applications of
\(B_2,B_2^*,B_3,B_3^*\) when the types match.  Include all rational meshes and
integer cutoff radii.  For the first \(m\) probes of one type, write \(\nu_m\)
for their joint coordinate law and define

\[
d_{\mathfrak A}(\mathfrak S,\widetilde{\mathfrak S})
=\sum_{m\ge1}2^{-m}
\bigl(1\wedge W_2(\nu_m,\widetilde\nu_m)\bigr).
\tag{4.1}
\]

Lemma 3.1 is applied to every finite prefix; a countable intersection of the
probability-one events gives simultaneous convergence of the whole grammar.
Projective consistency realizes the three limiting coordinate grammars on
probability spaces \((\Omega_1,\mu_1),(\Omega_2,\mu_2),(\Omega_3,\mu_3)\).
Quotienting each probe span by its limiting \(L^2\)-null seminorm and
completing gives \(\mathcal H_1,\mathcal H_2,\mathcal H_3\).

The same Gaussian-net estimate used in Lemma 3.1 holds simultaneously for
\(B_{2,0},B_{3,0}\).  Therefore the finite-width inequalities

\[
\|B_{2,0}v\|_2\le10\|v\|_2,
\qquad
\|B_{3,0}u\|_2\le10\|u\|_2
\]

pass through the null quotients.  The normalized adjoint identities pass as
well.  Hence

\[
B_{2,0}:\mathcal H_1\to\mathcal H_2,qquad
B_{3,0}:\mathcal H_2\to\mathcal H_3
\tag{4.2}
\]

are actual bounded operators with actual Hilbert adjoints.  The coordinate
spaces are not asserted to be algebras.  Closure is used only for a bounded
coordinate multiplier times an \(L^2\) field, which remains in \(L^2\).

Each \(\Omega_r\) is retained with its probability measure, its distinguished
constant \(1\), and its bounded multiplication algebra acting on
\(L^2(\Omega_r)\).  This pointed diagonal data is essential: an abstract
Hilbert operator without the coordinate multiplication algebra would not
determine the nonlinear gates.  The current limiting state is the isomorphism
class

\[
\mathfrak S=(w,B_2,B_3,C;Omega_1,\Omega_2,\Omega_3),
\tag{4.3}
\]

where \(w\in L^2(\Omega_1;\mathbb R^d)\),
\(C\in L^\infty(\Omega_3)\), and the two current operators have the types in
(4.2).  Initial operators and past increments are construction devices, not
additional state variables.

We construct the fixed-cutoff flow before calling it an ODE on the limit
state.  At finite width use the norm

\[
 \|w\|_{2,n}+\|C\|_{2,n}
 +\|B_2\|_{\rm op}+\|B_3\|_{\rm op}.
\]

For fixed \(R\), the cutoff version of (2.1)--(2.2) is locally Lipschitz in
this norm, with constants independent of \(n\), on the event
\(\max_\ell\|B_{\ell,0}\|_{\rm op}\le10\).  To verify this, use successively

\[
\|Bv-\widetilde B\widetilde v\|_2
\le\|B-\widetilde B\|_{\rm op}\|v\|_2
+\|\widetilde B\|_{\rm op}\|v-\widetilde v\|_2,
\tag{4.4}
\]

\[
\|C\phi'(S)-\widetilde C\phi'(\widetilde S)\|_2
\le b\|C-\widetilde C\|_2
+b\|\widetilde C\|_\infty\|S-\widetilde S\|_2,
\tag{4.5}
\]

and

\[
\begin{aligned}
\|\phi'(S)\tau_R(P)-\phi'(\widetilde S)\tau_R(\widetilde P)\|_2
\le{}&b(R+1)\|S-\widetilde S\|_2\\
&+b\|P-\widetilde P\|_2.
\end{aligned}
\tag{4.6}
\]

The rank-one identity

\[
\|u\otimes v\|_{\rm op}=\|u\|_2\|v\|_2
\tag{4.7}
\]

then controls both matrix equations.  No \(L^\infty\) difference of two
\(C\)'s is used: only an a priori \(L^\infty\) bound on each trajectory is
needed.  With \(b=2\),

\[
\frac d{dt}\|C\|_\infty
\le2b(1+b\|C\|_\infty),
\qquad
\|C(t)\|_\infty\le\frac{e^{2b^2t}-1}{b}.
\tag{4.8}
\]

The same estimates bound \(w\), both operator norms, and the vector field on
every finite interval.  The Gaussian net estimate above makes the initial
operator event occur eventually almost surely.  Thus the finite-width cutoff
ODE has a unique solution, and its Euler approximation satisfies

\[
\sup_{kh\le T}\|\mathfrak S_R(kh)-\mathfrak S_R^h(kh)\|
\le C_{R,T}h.
\tag{4.9}
\]

Indeed, if a vector field is \(L\)-Lipschitz and bounded by \(M\) on the
reached region, one Euler local defect is at most \(LMh^2/2\); the recurrence
\(e_{k+1}\le(1+Lh)e_k+LMh^2/2\) gives (4.9).  The constants are independent of
width.  For two rational meshes \(h,h'\), encode both Euler schemes in one
finite program.  Theorem 3.1 and (4.9) imply, for every finite list of probes,
that their limiting laws are at distance at most \(C_{R,T}(h+h')\).  Hence the
fixed-mesh limiting action states are Cauchy as \(h\downarrow0\); call their
limit \(\mathfrak S_R(t)\).  Applying (4.9) once more proves that the actual
finite-width cutoff flows converge to it uniformly on compact time intervals.
The same estimate for two solutions proves uniqueness.  Only now do we call
\(\mathfrak S_R\) the autonomous cutoff ODE on the action state.  Theorem 3.1
was used only for finitely many steps at a time; no uniform-in-program-size
conclusion was imported.

## 5. Uniform all-source estimate and removal of the cutoffs

This section supplies the estimate not contained in a fixed-program theorem.
Let

\[
\|X\|_{\psi_2}
=\inf\{s>0:\mathbb E e^{X^2/s^2}\le2\}.
\tag{5.1}
\]

For the four response families define the stronger absolute derivative
masses

\[
\begin{aligned}
A_2&=\sup_{k,a}\mathbb E\sum_{r<k,b}
\left|\frac{\partial H_{1,k}^a}{\partial\widehat P_{1,r}^b}\right|,
&B_2&=\sup_{k,a}\mathbb E\sum_{r\le k,b}
\left|\frac{\partial D_{2,k}^a}{\partial\widehat S_{2,r}^b}\right|,\\
A_3&=\sup_{k,a}\mathbb E\sum_{r<k,b}
\left|\frac{\partial H_{2,k}^a}{\partial\widehat P_{2,r}^b}\right|,
&B_3&=\sup_{k,a}\mathbb E\sum_{r\le k,b}
\left|\frac{\partial D_{3,k}^a}{\partial\widehat S_{3,r}^b}\right|.
\end{aligned}
\tag{5.2}
\]

They dominate the row sums of the absolute coefficients in (3.10).  Put

\[
K_1=\sup_{k,a}\|P_{1,k}^a\|_{\psi_2},qquad
K_2=\sup_{k,a}\|P_{2,k}^a\|_{\psi_2},qquad
\mathcal R=A_2+A_3+B_2+B_3.
\tag{5.3}
\]

We next prove a finite-DAG path estimate.  Its purpose is to retain every
source history without writing an infinite list of separate inequalities.

**Lemma 5.1 (path-sum response estimate).**  Let

\[
D=2^{100}p^4.
\tag{5.4}
\]

For a cutoff Euler DAG on \([0,T]\), suppose

\[
D\{\mathcal R+DT(1+K_2^2)\}<1.
\tag{5.5}
\]

Define

\[
\mathcal E
=\frac{D\exp\{DT+D^2T^2(K_1^2+K_2^2)\}}
 {1-D\{\mathcal R+DT(1+K_2^2)\}}.
\tag{5.6}
\]

Then, uniformly in mesh size, number of steps, and cutoff radius,

\[
A_2+A_3\le T\mathcal E,
\qquad
B_3\le(\|C\|_\infty+T)\mathcal E,
\qquad
B_2\le(K_2+T)\mathcal E.
\tag{5.7}
\]

**Proof.**  Regard every formal source derivative as a directed path in the
serialized DAG (3.7).  At a coordinate node the only derivative rules are

\[
|\partial\phi(X)|\le b|\partial X|,
\tag{5.8}
\]

\[
|\partial(C\phi'(S_3))|
\le b|\partial C|+b|C|\,|\partial S_3|,
\tag{5.9}
\]

\[
|\partial(\phi'(S_2)\tau_R(P_2))|
\le b|P_2|\,|\partial S_2|+b|\partial P_2|,
\tag{5.10}
\]

and, for the first-layer update,

\[
|\partial U_{k+1}|
\le(1+6bh|P_{1,k}|)|\partial U_k|
+6bh|\partial P_{1,k}|.
\tag{5.11}
\]

The two parameter updates and the \(C\)-update contribute one factor \(h\),
one data sum, and bounded activation factors.  Empirical moments are constants
under the formal derivative.  A learned forward-memory edge has total
absolute coefficient at most

\[
6b^2T,
\tag{5.12}
\]

the learned \(B_3^*\)-memory has total coefficient at most

\[
6T\sup\mathbb E D_3^2\le6b^2T\|C\|_\infty^2,
\tag{5.13}
\]

and the learned \(B_2^*\)-memory has total coefficient at most

\[
6T\sup\mathbb E D_2^2\le6b^2TK_2^2.
\tag{5.14}
\]

Response edges have total coefficient at most \(\mathcal R\).  Remove all
response and learned-memory edges from a path.  In one serialized time slice
there are fewer than 24 remaining local edges and at most four data sums;
using \(b\le2\) and \(6\) for the residual sum, the total local branching
factor is smaller than \(2^{100}p^4=D\).  Re-inserting response and memory
edges gives a geometric path sum bounded by the denominator in (5.6), because
(5.12)--(5.14) are bounded by \(DT(1+K_2^2)\).

Every path contributing to an \(\alpha\)-coefficient must cross a parameter
update strictly after its adjoint source; hence it contains at least one time
edge.  Summing its first time edge gives the prefactor \(T\).  A path
contributing to \(B_3\) either starts with the direct derivative in (5.9),
whose size is at most \(b\|C\|_\infty\), or first crosses a time edge.  A path
contributing to \(B_2\) either starts with (5.10), whose only unbounded direct
factor is \(b|P_2|\), or first crosses a time edge.  This proves the three
prefactors in (5.7).

After the first time edge, time ordering gives, for \(q\) further time edges,
the simplex factor \(1/q!\).  Summing \(q\) therefore produces the pathwise
factor

\[
\exp\left\{Dh\sum_{k<N}
(1+Z_{1,k}+Z_{2,k})\right\},
\qquad
Z_{j,k}=\max_{a\le p}|P_{j,k}^a|.
\tag{5.15}
\]

Generalized Holder over the \(2N\) time-layer pairs and

\[
\mathbb E e^{s|X|}\le2e^{s^2\|X\|_{\psi_2}^2/4}
\tag{5.16}
\]

give

\[
\mathbb E\exp\left\{Dh\sum_k(Z_{1,k}+Z_{2,k})\right\}
\le4p\exp\{D^2T^2(K_1^2+K_2^2)\}.
\tag{5.17}
\]

The factor \(4p\) and the harmless first moments obtained from the direct
\(|P_2|\) factor are dominated by the deliberately large \(D\) in (5.4).
Combining the geometric, time-ordered, and Gaussian factors proves
(5.6)--(5.7).  Every source path is included, so the argument does not truncate
the source hierarchy. \(\square\)

The message tails now close in triangular order.

**Lemma 5.2 (message estimates).**  Under (5.5),

\[
K_2\le D\{T+B_3+T^3\},
\qquad
K_1\le D\{K_2+B_2+TK_2^2\}.
\tag{5.18}
\]

**Proof.**  From (4.8), \(\|C\|_\infty\le12T\) for sufficiently small
\(T\).  Thus the fresh Gaussian in the \(P_2\) representation has standard
deviation at most \(b\|C\|_\infty\).  Its response shift is bounded by
\(bB_3\), and its learned shift is bounded by
\(6b^3T\|C\|_\infty^2\).  The triangle inequality for \(\psi_2\), with a
factor four absorbing the Gaussian normalization, proves the first estimate.

The fresh Gaussian in \(P_1\) has standard deviation
\((\mathbb E D_2^2)^{1/2}\le bK_2\).  Its response shift is bounded by
\(bB_2\), while (5.14) bounds its learned shift by \(6b^3TK_2^2\).
Increasing the same universal constant to \(D\) proves the second estimate.
\(\square\)

**Lemma 5.3 (uniform closure).**  If

\[
0<T\le T_0:=10^{-6}D^{-8},
\tag{5.19}
\]

then the cutoff DAG satisfies

\[
\begin{aligned}
A_2+A_3&\le4DT,& B_3&\le5D^2T,\\
K_2&\le8D^3T,&B_2&\le32D^4T,\\
K_1&\le64D^5T.
\end{aligned}
\tag{5.20}
\]

**Proof.**  Use a first-crossing bootstrap with the bounds in (5.20).  They
imply

\[
\mathcal R\le42D^4T,qquad
D\{\mathcal R+DT(1+K_2^2)\}<\tfrac1{10},
\]

and

\[
DT+D^2T^2(K_1^2+K_2^2)<\tfrac1{10}
\]

by (5.19).  Consequently \(\mathcal E<2D\).  Lemma 5.1 gives

\[
A_2+A_3<2DT,qquad B_3<4D^2T,qquad
B_2<2D(K_2+T)<18D^4T.
\]

Lemma 5.2 then gives

\[
K_2<6D^3T,qquad K_1<26D^5T.
\]

Every inequality strictly improves its bootstrap value, so no first crossing
can occur.  At time zero all five quantities vanish, completing the proof.
\(\square\)

The estimates pass from discrete meshes to the limiting cutoff flow by
Fatou's lemma and (4.9).  In particular, both adjoint fields have cutoff- and
mesh-independent Gaussian tails in the limiting coordinate law.

To remove the cutoffs, compare an uncut flow with a cutoff flow on the same
finite-width initialization.  For the lower backpropagated field use the exact
decomposition

\[
\begin{aligned}
\phi'(S_2)P_2-\phi'(S_{2,R})\tau_R(P_{2,R})
={}&\phi'(S_2)(P_2-P_{2,R})\\
&+\phi'(S_2)(P_{2,R}-\tau_R(P_{2,R}))\\
&+(\phi'(S_2)-\phi'(S_{2,R}))\tau_R(P_{2,R}).
\end{aligned}
\tag{5.21}
\]

Use the identical decomposition for the first-layer factor involving
\(P_1\).  Successive application of (4.4)--(4.7) gives, in the sum of the
three hidden \(L^2\) distances, the \(C\)-distance, and the two operator
distances,

\[
E_{n,R}'(t)\le C_T(1+R)E_{n,R}(t)
+C_T\sum_{j=1}^2\sum_{a=1}^p
\|P_{j,R}^a-\tau_R(P_{j,R}^a)\|_{2,n}.
\tag{5.22}
\]

If \(\|X\|_{\psi_2}\le K\), integration of
\(\mathbb P(|X|>s)\le2e^{-s^2/K^2}\) gives

\[
\|X-\tau_R(X)\|_2
\le C(K+R)e^{-R^2/(2K^2)}.
\tag{5.23}
\]

For fixed \(R\), the function \((x-\tau_R(x))^2\) is pseudo-Lipschitz, so
fixed-cutoff convergence passes its empirical average to the limiting one.
Equations (5.20)--(5.23) and Gronwall therefore imply

\[
\lim_{R\to\infty}\limsup_{n\to\infty}
\sup_{t\le T}E_{n,R}(t)=0.
\tag{5.24}
\]

The quadratic Gaussian exponent in (5.23) dominates the linear \(R\)-factor
from Gronwall.  Hence the actual uncut finite-width flows converge to a
cutoff-independent limiting flow.  Comparing any two strong continuations by
truncating one of them gives the same estimate; the tail belongs only to the
canonical cutoff approximation.  Letting \(R\to\infty\) proves uniqueness.
Because the equations use only the current state (4.3), uniqueness also proves
restartability.
