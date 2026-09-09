# Dense Euclidean continuous-depth \(\mu\)P: an audited response-PDE conjecture

## Executive conclusion

There is a strong, non-oracular PDE-existence conjecture for the standard
fully dense residual network trained by ordinary Euclidean \(\mu\)P gradient
flow.

The right closure variable is not a current neuron law, a finite list of
Gram matrices, or a training-time Taylor jet. It is a finite collection of
**oriented chronological response words**, with separate finite budgets for
dense-response grade and nonlinear expression complexity. Continuous depth
changes the unbounded discrete continuation tree into a Volterra/Dyson
hierarchy whose propagator tail, along every bounded trajectory, is
factorially small:

\[
R_K(\Lambda)
:=
\sum_{j>K}\frac{\Lambda^j}{j!}
\le
e^\Lambda\frac{\Lambda^{K+1}}{(K+1)!}.
\]

This factorial estimate is an exact theorem. The unresolved step is to show
that the terminating slow/fast compiler has a width-independent,
continuous-depth, globally stable Liouville PDE limit, including
current-state Markovization and a small **full outgoing residual**. That
statement is formulated precisely below.

The first response block retains one ordered dense-matrix continuation.
Its finite-matrix \(q/r\) projection is numerically excellent in the tested
standard-scale networks. The homogenized Liouville PDE itself has not been
implemented numerically and is not called a certified accuracy level.

The final status is therefore:

\[
\boxed{\text{The response mechanism and its factorial tail are proved.}}
\]

\[
\boxed{\text{Uniform convergence of the explicit finite PDEs is the conjecture.}}
\]

If the conjecture is proved, accuracy-dependent finite-PDE existence follows
immediately. It cannot be proved by fitting the already-solved loss curve,
packing an arbitrary ODE into a source variable, or silently retaining the
full \(n\times n\) matrix state.

---

## 1. Exact target model

### 1.1 Data

Fix input dimension \(d=3\) and \(m=3\) training samples. The central
instance is

\[
x_1=e_1,\qquad x_2=e_2,\qquad x_3=e_3,
\]

\[
y_*=(0.8,-0.55,0.35)^\top.
\]

To make non-oracularity an extensional mathematical condition rather than a
statement about how constants were obtained, require one compiler to work
uniformly on the compact neighborhood

\[
\text{with }X=[x_1\ x_2\ x_3],\qquad
\mathcal U=
\left\{
(X,y,\sigma_w,A,\gamma):
\begin{array}{l}
\|X^\top X-I_3\|_{\rm op}\le 0.05,\\
\|y-y_*\|_2\le0.05,\\
|\sigma_w-0.65|\le0.05,\\
|A-1|\le0.05,\\
|\gamma-1|\le0.05
\end{array}
\right\}.
\]

The conjecture has the same form for any fixed \(m\); this three-sample
neighborhood is the first concrete nontrivial laboratory.

### 1.2 Finite width and depth

For width \(n\), depth \(L\), and \(\Delta=L^{-1}\), define

\[
h_r^0=Bx_r,
\qquad
z_r^\ell=W_\ell h_r^\ell,
\]

\[
\boxed{
h_r^{\ell+1}
=h_r^\ell+\gamma\Delta\,\tanh(z_r^\ell),
\qquad 0\le\ell<L,
}
\tag{1}
\]

\[
\boxed{
f_r=\frac1n a^\top h_r^L,
\qquad
\mathcal L=\frac12\sum_{r=1}^m(f_r-y_r)^2.
}
\tag{2}
\]

Every \(W_\ell\in\mathbb R^{n\times n}\) is fully dense and unconstrained.
Every \(W_\ell\), \(B\), and \(a\) is trained.

Initialization is independent:

\[
(W_\ell)_{ij}\sim N\!\left(0,\frac{\sigma_w^2}{n}\right),
\qquad
B_{ij}\sim N(0,1),
\qquad
a_i\sim N(0,A^2).
\tag{3}
\]

The layers \(W_0,\ldots,W_{L-1}\) are iid. No orthogonality, projection,
normalization, low-rank parameterization, tied weight, frozen layer, or
state-dependent preconditioner is present.

### 1.3 Standard Euclidean \(\mu\)P flow

Put \(e=f-y\). The layerwise scalar learning-rate multipliers are

\[
\boxed{
\eta_{W_\ell}=L,\qquad
\eta_B=n,\qquad
\eta_a=n.
}
\tag{4}
\]

Thus

\[
\dot W_\ell=-L\nabla_{W_\ell}\mathcal L,
\qquad
\dot B=-n\nabla_B\mathcal L,
\qquad
\dot a=-n\nabla_a\mathcal L.
\]

These are constant scalar multiples of the ambient Euclidean metric. They
are the feature-learning \(\mu\)P rates in the effective coordinates
\(W_{ij}=O(n^{-1/2})\), \(a_i=O(1)\). If instead
\(W=\widehat W/\sqrt n\) with \(\widehat W_{ij}=O(1)\), the equivalent raw
rate is \(nL\). The raw readout is \(c=a/n=O(n^{-1})\).

The factor \(L\) is necessary for a nonvanishing **\(W\)-induced** feature
update on \(O(1)\) training time: each residual block carries one factor
\(L^{-1}\). With an \(O(1)\) \(W\)-rate that backbone contribution vanishes
as \(L\to\infty\), although the separately trained input map \(B\) can still
move features.

---

## 2. Exact finite-\((n,L)\) equations

Define the unit-output adjoints

\[
p_r^L=a,
\]

\[
D_r^\ell
=\operatorname{diag}\!\left(
\tanh'(z_r^\ell)
\right),
\qquad
\beta_r^\ell=D_r^\ell p_r^{\ell+1}.
\]

Backpropagation gives

\[
\boxed{
p_r^\ell
=
\left(
I+\gamma\Delta W_\ell^\top D_r^\ell
\right)p_r^{\ell+1}.
}
\tag{5}
\]

The exact Euclidean parameter flow is

\[
\boxed{
\dot W_\ell
=
-\frac{\gamma}{n}
\sum_{q=1}^m
e_q\,\beta_q^\ell(h_q^\ell)^\top,
}
\tag{6}
\]

\[
\boxed{
\dot a=-\sum_qe_qh_q^L,
\qquad
\dot B=-\sum_qe_qp_q^0x_q^\top.
}
\tag{7}
\]

Writing

\[
G^{u,\ell}_{rq}
:=\frac1n(u_r^\ell)^\top u_q^\ell,
\qquad
Q^x_{rq}=x_r^\top x_q,
\]

the output equation is exactly

\[
\boxed{\dot f=-\Theta^{n,L}e,}
\tag{8}
\]

where

\[
\boxed{
\Theta^{n,L}_{rq}
=
G^{h,L}_{rq}
+
Q^x_{rq}G^{p,0}_{rq}
+
\frac{\gamma^2}{L}
\sum_{\ell=0}^{L-1}
G^{h,\ell}_{rq}G^{\beta,\ell}_{rq}.
}
\tag{9}
\]

Every term is positive semidefinite. The last term is positive semidefinite
by the Schur product theorem.

Consequently

\[
\dot{\mathcal L}
=-e^\top\Theta^{n,L}e\le0.
\tag{10}
\]

This identity does not close the dynamics because \(\Theta\) itself contains
the dense forward/backward response hierarchy.

For each finite \(n,L\), global existence follows from the gradient-flow
energy identity. In the inverse \(\mu\)P metric,

\[
-\dot{\mathcal L}
=
\frac1n\|\dot a\|^2
+
\frac1n\|\dot B\|_F^2
+
\frac1L\sum_{\ell=0}^{L-1}\|\dot W_\ell\|_F^2.
\tag{11}
\]

No parameter can travel an infinite Euclidean distance in a finite time.

---

## 3. What “continuous depth” means here

It is incorrect to linearly interpolate the iid matrices \(W_\ell(0)\) and
assert convergence to an ordinary matrix field \(W(s,0)\).

With \(1/L\) residual scaling, every fixed smooth depth mode of that fast iid
field tends to zero, while nonlinear quantities such as
\(\mathbb E[\tanh'(Wh)]\) remain \(O(1)\). The correct object is a
homogenized Gaussian Young measure/cavity law.

Accordingly, the target order of limits is

\[
\boxed{
n\to\infty\ \text{at fixed }L,
\qquad\text{then}\qquad
L\to\infty.
}
\tag{12}
\]

The continuous-depth observable is defined by

\[
\mathcal O(t)
:=
\lim_{L\to\infty}\lim_{n\to\infty}\mathcal O_{n,L}(t),
\tag{13}
\]

where \(\mathcal O\) contains \(f\), all depthwise hidden Grams, and
\(\Theta\).

The finite-width response expansion below is performed **before** either
limit. This prevents a false replacement of the iid architecture by a
depth-correlated neural ODE and prevents formal high-grade Wick contractions
from being assumed small.

The resulting limiting equations can be represented as a forward/backward
path-space DMFT with two-training-time covariances and causal responses. A
one-time neuron law is not sufficient.

---

## 4. Why a one-time row law cannot be the PDE

Dense \(\mu\)P learning creates coherent matrix components of entry size
\(O(n^{-1})\) and operator norm \(O(1)\).

Two matrices can have the same limiting entry law, the same current forward
and backward neuron laws, and the same current Grams, yet differ by

\[
\delta W=\frac1nuv^\top,
\]

where
\[
\|u\|=\|v\|=\sqrt n,\qquad
v\perp\operatorname{span}\{h_s\}_{s=1}^m,\qquad
u\perp\operatorname{span}\{\beta_s\}_{s=1}^m.
\]
It leaves all current \(Wh_s\) and \(W^\top\beta_s\) unchanged and is
invisible to ordinary limiting row marginals. But for a future response
direction \(\xi\) with \(n^{-1}v^\top\xi\to c\ne0\),
\(\delta W\,\xi\to c\,u\) in normalized neuron norm. It can therefore
change the next Gram derivative by \(O(1)\).

The required state must retain:

- the orientation \(W\) versus \(W^\top\);
- the order in which dense matrices are reused;
- learned rank-one insertions;
- the finite continuation response of each tagged word.

Continuous depth does not make those objects disappear. It gives their
ordered sum a factorially controlled Volterra structure.

---

## 5. Exact chronological-response hierarchy

Let

\[
v_r^\ell:=\partial_t h_r^\ell,
\qquad
A_r^\ell:=\gamma D_r^\ell W_\ell.
\]

Differentiating (1) and using (6) gives

\[
\boxed{
v_r^{\ell+1}
=
(I+\Delta A_r^\ell)v_r^\ell
+
\Delta F_r^\ell,
}
\tag{14}
\]

where

\[
\boxed{
F_r^\ell
=
-\gamma^2
\sum_{q=1}^m
e_qD_r^\ell\beta_q^\ell G^{h,\ell}_{qr},
}
\tag{15}
\]

\[
\boxed{
v_r^0
=
-\sum_qe_qQ^x_{qr}p_q^0.
}
\tag{16}
\]

Separate the label channels and define

\[
q^{0,\ell+1}_{r\leftarrow q}
=q^{0,\ell}_{r\leftarrow q}
-\Delta\gamma^2
D_r^\ell\beta_q^\ell G^{h,\ell}_{qr},
\]

\[
q^{0,0}_{r\leftarrow q}=-Q^x_{qr}p_q^0,
\tag{17}
\]

and, for \(k\ge1\),

\[
q^{k,\ell+1}_{r\leftarrow q}
=
q^{k,\ell}_{r\leftarrow q}
+
\Delta A_r^\ell q^{k-1,\ell}_{r\leftarrow q},
\qquad
q^{k,0}_{r\leftarrow q}=0.
\tag{18}
\]

Then the exact identity is

\[
\boxed{
\partial_t h_r^\ell
=
\sum_qe_q
\sum_{k=0}^{\infty}
q^{k,\ell}_{r\leftarrow q}.
}
\tag{19}
\]

The index \(k\) is the number of ordered dense Jacobian continuations.

There is an analogous backward hierarchy for
\(w_r^\ell=\partial_t p_r^\ell\). Its exact discrete equation is

\[
\boxed{
w_r^\ell
=
\left(I+\Delta(A_r^\ell)^\top\right)w_r^{\ell+1}
+
\Delta(\dot A_r^\ell)^\top p_r^{\ell+1},
\qquad
w_r^L=-\sum_qe_qh_q^L.
}
\tag{20}
\]

Writing
\(\dot A_r^\ell=\sum_qe_q(\dot A_r^\ell)_{\leftarrow q}\), define

\[
\boxed{
r^{0,\ell}_{r\leftarrow q}
=
r^{0,\ell+1}_{r\leftarrow q}
+
\Delta
\left((\dot A_r^\ell)_{\leftarrow q}\right)^\top
p_r^{\ell+1},
\qquad
r^{0,L}_{r\leftarrow q}=-h_q^L,
}
\tag{21}
\]

\[
\boxed{
r^{k,\ell}_{r\leftarrow q}
=
r^{k,\ell+1}_{r\leftarrow q}
+
\Delta(A_r^\ell)^\top
r^{k-1,\ell+1}_{r\leftarrow q},
\qquad
r^{k,L}_{r\leftarrow q}=0,
\quad k\ge1.
}
\tag{22}
\]

Then
\[
w_r^\ell
=
\sum_qe_q\sum_{k\ge0}r^{k,\ell}_{r\leftarrow q}.
\tag{22a}
\]

Only after these discrete identities are fixed do we use
continuous-depth notation as shorthand for their ordered Riemann-sum limit.
Put

\[
A_r=\gamma D_rW,
\qquad
\partial_tA_r=\sum_qe_q(\partial_tA_r)_{\leftarrow q}.
\]

The label-separated backward responses obey

\[
-\partial_s r^0_{r\leftarrow q}
=
\left((\partial_tA_r)_{\leftarrow q}\right)^\top p_r,
\qquad
r^0_{r\leftarrow q}(1)=-h_q(1),
\tag{22b}
\]

\[
-\partial_s r^k_{r\leftarrow q}
=
A_r^\top r^{k-1}_{r\leftarrow q},
\qquad
r^k_{r\leftarrow q}(1)=0,
\quad k\ge1,
\tag{22c}
\]

\[
\partial_t p_r
=
\sum_qe_q\sum_{k\ge0}r^k_{r\leftarrow q}.
\tag{22d}
\]

### 5.1 Rigorous factorial tail

Use the normalized neuron norm
\(\|u\|_n=n^{-1/2}\|u\|_2\), and fix a finite training horizon \(T\).
Assume along a trajectory that

\[
\Lambda_T
:=
\sup_{\substack{r\\0\le t\le T}}
\frac1L\sum_{\ell=0}^{L-1}
\|A_r^\ell(t)\|_{\rm op}
<\infty.
\tag{23}
\]

Let

\[
B_{v,T}
:=
\sup_{\substack{r\\0\le t\le T}}
\left(
\|v_r^0(t)\|_n
+
\frac1L\sum_\ell\|F_r^\ell(t)\|_n
\right).
\]

Put
\[
\bar q_r^{k,\ell}
:=
\sum_qe_q q^{k,\ell}_{r\leftarrow q}.
\]

The ordered-product expansion gives, pathwise and before taking width,

\[
\boxed{
\sup_{\substack{0\le t\le T\\r,\ell}}
\left\|
v_r^\ell-\sum_{k=0}^K\bar q_r^{k,\ell}
\right\|_n
\le
B_{v,T}R_K(\Lambda_T),
}
\tag{24}
\]

\[
\boxed{
R_K(\Lambda_T)
\le
e^{\Lambda_T}\frac{\Lambda_T^{K+1}}{(K+1)!}.
}
\tag{25}
\]

The proof is the simplex-volume estimate: the sum of all ordered products of
\(j\) matrices is bounded by \(\Lambda^j/j!\). The same estimate holds for
the backward hierarchy when its source \(\dot A\) is held exact. More
precisely, put

\[
\bar r_r^{k,\ell}
:=
\sum_q e_q r_{r\leftarrow q}^{k,\ell},
\qquad
S_r^\ell
:=
(\dot A_r^\ell)^\top p_r^{\ell+1},
\]

\[
B_{w,T}
:=
\sup_{\substack{0\le t\le T\\r}}
\left(
\|w_r^L(t)\|_n
+
\frac1L\sum_{\ell=0}^{L-1}\|S_r^\ell(t)\|_n
\right).
\]

Then the same ordered-simplex argument gives the exact-source estimate

\[
\boxed{
\sup_{\substack{0\le t\le T\\r,\ell}}
\left\|
w_r^\ell-\sum_{k=0}^K\bar r_r^{k,\ell}
\right\|_n
\le
B_{w,T}R_K(\Lambda_T).
}
\tag{25a}
\]

This result is width-uniform on \([0,T]\) when
\[
\sup_{n,L}
\max\{B_{v,T},B_{w,T},\Lambda_T\}
<\infty.
\]
An all-time version requires the same bounds uniformly in \(T\).

There is a separate issue for the *coupled* truncation used in the
simulations, where \(\dot A\) is recomputed from the truncated forward
velocity. Define

\[
E_{A,K,T}
:=
\sup_{\substack{0\le t\le T\\r}}
\frac1L\sum_\ell
\left\|
\left(
\dot A_r^\ell-\dot A_{r,K}^\ell
\right)^\top p_r^{\ell+1}
\right\|_n .
\]

If \(w_{r,K,\mathrm{coup}}\) denotes that coupled approximation, variation
of constants gives

\[
\boxed{
\sup_{\substack{0\le t\le T\\r,\ell}}
\|w_r^\ell-w_{r,K,\mathrm{coup}}^\ell\|_n
\le
B_{w,T}R_K(\Lambda_T)
+
e^{\Lambda_T}E_{A,K,T}.
}
\tag{25b}
\]

The factorial theorem alone does not show
\(E_{A,K,T}\to0\). For example, the source difference contains

\[
\gamma W_\ell^\top
\left[
p_r^{\ell+1}\odot\tanh''(z_r^\ell)
\odot W_\ell(v_r^\ell-v_{r,K}^\ell)
\right],
\]

which needs additional operator and coordinate bounds. Equations
(24)–(25b) do not use training-time analyticity, Gaussian Taylor
coefficients, or positivity of Wick diagrams.

---

## 6. The finite PDE compiler

### 6.0 The exact homogenized hierarchy operator

The target operator is defined without postulating a smooth raw matrix
\(W(s)\).

For fixed \(L\), let \(Y_L(t)\) be the projective family of all finite joint
laws of the tagged coordinates obtained from (1), (5)–(7), including every
oriented \(W_\ell/W_\ell^\top\) word. Let
\(\mathcal V_L(\Xi;\mathcal M[Y_L])\) be their pointwise characteristic
drift. The corresponding law generator \(\mathscr G_L\) is defined on every
cylindrical test function \(\Psi\) by

\[
\left\langle\mathscr G_L(Y_L),\Psi\right\rangle
:=
\frac d{dt}\mathbb E_{Y_L(t)}[\Psi]
=
\mathbb E_{Y_L(t)}
\left[
\nabla\Psi\cdot
\mathcal V_L\bigl(\Xi;\mathcal M[Y_L(t)]\bigr)
\right],
\tag{26a}
\]

where \(\mathcal V_L\) is exactly the chain-rule vector field (5)–(7), and
\(\mathcal M[Y_L]\) replaces normalized coordinate contractions by their
expectations. At initialization these laws are uniquely fixed by Gaussian
conditioning of (3). This is the standard fixed-depth causal DMFT/tensor-
program generator, expressed as a projective law rather than as a finite
moment closure.

Let \(\mathcal H_L\) send the \(L\) depth slots to their empirical
Young-measure interpolation on \([0,1]\), retaining every nonlinear tag.
Because \(\mathcal H_L\) is not injective, no inverse is used. The exact
continuous-depth law generator is defined by the product-space graph limit

\[
\boxed{
\operatorname{Graph}(\mathscr G)
:=
\lim_{L\to\infty}
\left\{
\left(
\mathcal H_LY,\,
\mathcal H_L\mathscr G_L(Y)
\right):
Y\in\operatorname{Dom}(\mathscr G_L)
\right\}.
}
\tag{26b}
\]

Existence and single-valuedness of this graph limit on the observable
quotient are part of the proposed quantitative mechanism in Section 8.3,
not an extra clause in the core conjecture.
Equation (26b) is a definition of the target; it does not assume that
\(W_\ell\) itself has a classical depth limit.

### 6.1 Oriented response grammar

Two independent finite cutoffs are required:

- \(K\) bounds chronological dense-response grade;
- \(J\) bounds nonlinear expression-tree complexity.

The oriented operators are

\[
\mathsf F_{r,j}:u\mapsto
\operatorname{diag}\!\bigl(\tanh^{(j)}(z_r)\bigr)Wu,
\]

\[
\mathsf B_{r,j}:u\mapsto
W^\top
\operatorname{diag}\!\bigl(\tanh^{(j)}(z_r)\bigr)u,
\]

and the learned Euclidean insertions

\[
\mathsf U_q:u\mapsto
\beta_q\langle h_q,u\rangle_n,
\qquad
\mathsf V_q:u\mapsto
h_q\langle\beta_q,u\rangle_n.
\tag{26}
\]

The symbols \(\mathsf F\) and \(\mathsf B\) are never identified, and word
order is never commuted.

The finite seed list is

\[
\mathscr T^0_K
=
\left\{
a,\ h_r,\ p_r,\ q^k_{r\leftarrow q},\
r^k_{r\leftarrow q}:\
1\le r,q\le m,\ 0\le k\le K
\right\}.
\tag{26c}
\]

Tags \(h,p,q,r\) are **slow** depth fields. Tags such as

\[
z_r=W h_r,\qquad
\beta_r=D_rp_r,\qquad
Wq^k,\qquad W^\top r^k
\tag{26d}
\]

are **fast** iid-layer Young variables. They are never assigned depth
derivatives or Legendre coefficients.

The compiler has two sorts of retained objects:

1. particle-coordinate tags \(\tau\), such as (26c)–(26d);
2. deterministic population coefficients \(\kappa_\alpha(s,t)\), common to
   all particles.

A \(\kappa_\alpha\) is indexed by its entire finite query tuple: matrix
symbol, symbolic depth slot, orientation, retained query identifiers, and
derivative multi-index. Numerical depth nodes do not enter this symbolic
table; they are instantiated only after \(N\) is fixed. A coefficient is
either **algebraic**, and recomputed from current moments in a declared
topological order, or **historical**, with an emitted initial value and
autonomous label-separated ODE. These two types are disjoint.

Define response grade \(g\) and expression complexity \(c\) recursively:

\[
g(a)=g(h_r)=g(p_r)=0,\qquad
g(q^k)=g(r^k)=k,\qquad
c(\tau)=0\quad(\tau\in\mathscr T^0_K),
\]

\[
g(\mathsf F\tau)=g(\mathsf B\tau)
=g(\mathsf U\tau)=g(\mathsf V\tau)=g(\tau)+1,
\]

\[
c(\mathsf F_{r,j}\tau)
=c(\mathsf B_{r,j}\tau)
=1+j+c(\tau),
\qquad
c(\mathsf U_q\tau)
=c(\mathsf V_q\tau)
=1+c(\tau),
\]

\[
c(\tanh^{(j)}(\tau))=1+j+c(\tau),\qquad
c(\tau_1\odot\tau_2)
=1+c(\tau_1)+c(\tau_2),
\tag{26e}
\]

with every longer product parsed as a binary tree and inner products
assigned the same additive product complexity. For a population coefficient
defined by retained query tags \(\tau_1,\ldots,\tau_r\) and derivative
multi-index \(\nu\), set

\[
g(\kappa_\alpha)=\max_i g(\tau_i),
\qquad
c(\kappa_\alpha)
=1+|\nu|+\sum_{i=1}^r\bigl(1+c(\tau_i)\bigr).
\tag{26e'}
\]

Addition and multiplication by architecture constants take the maximum
complexity **only inside one of the finitely many emitted right-hand-side
templates**. The grammar is not independently closed under arbitrary
linear combinations. Architecture-only scalar expressions are evaluated
and canonicalized immediately, and records are keyed by tag/query type, not
by arbitrary symbolic coefficients. Thus repeated zero-cost sums or scalar
multiples cannot create new records.

Tags and \(\kappa\)'s are enumerated in one least-fixed-point construction.
Starting from \(\mathscr T^0_K\), maintain a queue containing:

- every budget-admissible chain-rule child generated by (5)–(7),
  (17)–(22), and (26h)–(26k);
- the finite row and column query list of each initialization-matrix symbol;
  and
- for each retained query tuple, only the conditional
  mean/covariance/transpose-response coefficient dictated by the
  conditioning rule below.

Each new record is retained only when \(g\le K\) and \(c\le J\).
Expressions are canonical DAGs modulo linearity and the
associativity/commutativity of scalar addition and product. Every non-seed
constructor consumes positive grade or complexity, the primitive alphabet
is finite, and query tuples use only retained DAG identifiers. Therefore
the queue reaches a least fixed point after finitely many rounds. Denote its
particle tags by \(\mathscr T_{K,J}\) and its population coefficients by
\(\mathscr K_{K,J}\). No semantic “add \(\kappa\) whenever needed” rule is
permitted after this construction.

At each round, form the finite dependency graph of the retained
conditioning coefficients. A singleton with no self-loop remains
algebraic. Every nontrivial strongly connected component, and every
self-loop, is deterministically promoted in lexicographic DAG order to
historical \(\kappa\)-coordinates; differentiating their displayed defining
moments supplies their ODE records and returns those records to the same
budgeted queue. Consequently the final algebraic dependency graph is
acyclic by construction. No root of a cyclic algebraic system is ever
selected.

For every historical \(\kappa_\alpha\), the table emits its static Gaussian
initial value, depth boundary convention, and finite DAGs
\(B_\alpha^{(q)}\) satisfying

\[
\dot\kappa_\alpha
=
\sum_{q=1}^m e_q B_\alpha^{(q)}.
\tag{26e''}
\]

These coefficients store the retained action of the accumulated learned
part of \(W(t)\). For every retained \(W(t)\)- or \(W(t)^\top\)-query,
\((\rho,\kappa)\) must determine its current conditional mean and covariance
without any past-time integral or unlisted two-time contraction. The
closure \(\mathsf C_{K,J}\) keeps exactly the two finite tables and sends
every other monomial to zero. Thus neither unrestricted activation
derivative order, arbitrary grade-zero products, nor infinitely many
zero-cost history coefficients are hidden in the word “finite.”

### 6.2 Order of compilation

For fixed \(K,J\ge0\) and \(N\ge2\), the compiler is the following terminating,
architecture-local algorithm.

Its output contract is finite and checkable:

\[
\operatorname{Compile}(K,J,N,\vartheta)
=
\left(
D_{K,J,N},
\ Q_{K,J,N},
\mathscr T_{K,J},
\mathscr K_{K,J},
\{\phi_\alpha\}_{\alpha=1}^{M_{K,J,N}},
\{b_i^{(q)}\},
\{B_\alpha^{(q)}\},
\Gamma_{K,J,N},
\mathcal R^{\rm obs}_{K,J,N},
\mathcal E_{K,J,N},
\rho_{K,J,N}(0),
\kappa_{K,J,N}(0),
\mathcal A_{K,J,N}
\right).
\tag{Compiler}
\]

Here \(M_\alpha[\rho]=\int\phi_\alpha(\xi)\,d\rho\), each
\(b_i^{(q)}(\xi;M,\vartheta)\) is a finite expression DAG, and the initial
law is a finite-dimensional Gaussian pushforward.
\(\mathcal A_{K,J,N}\) is the admissible restart set defined below. The DAG
may contain only arithmetic, the displayed \(\tanh\) derivatives, fixed
Legendre/Gauss–Legendre entries, inverses of matrices with the fixed ridge
defined below, principal positive-semidefinite projection and square root,
and finite-dimensional Gaussian integrals. It may not contain \(\mathscr
G\), a graph limit, an unevaluated tensor-program/DMFT rule, an unspecified
algebraic root, or positive-time target data.

The algorithm producing this tuple is:

1. Generate the joint finite tables
   \((\mathscr T_{K,J},\mathscr K_{K,J})\) by the least-fixed-point rule
   above.
2. Fix the depth scheme once and for all. Let
   \(L_0,\ldots,L_{N-1}\) be the first \(N\) orthonormal shifted
   Legendre polynomials and set
   \[
   \boxed{Q_{K,J,N}=2(K+J+N)+3.}
   \]
   Let \((s_\nu,w_\nu)_{\nu=1}^{Q_{K,J,N}}\) be the positive
   \(Q_{K,J,N}\)-point Gauss–Legendre rule and define the sole nonlinear
   projections used by the compiler:
   \[
   \bigl(\Pi^{\rm GL}_{r,Q}F\bigr)_a
   :=
   \sum_{\nu=1}^{Q_{K,J,N}}
   w_\nu L_a(s_\nu)F(s_\nu),
   \qquad 0\le a<r,\quad r\in\{N-1,N\}.
   \tag{Depth projection}
   \]
   A forward field is represented by the boundary lift
   \[
   u_N(s)=u_0+\int_0^s d_{N-1}(\sigma)\,d\sigma,
   \]
   and a backward field by
   \[
   u_N(s)=u_1-\int_s^1 d_{N-1}(\sigma)\,d\sigma,
   \]
   where \(d_{N-1}\in\operatorname{span}\{L_0,\ldots,L_{N-2}\}\)
   represents \(\partial_su\). Thus the endpoint plus \(N-1\) derivative
   coefficients give exactly \(N\) depth degrees of freedom and enforce
   the \(h,q^k\) data at \(s=0\) and the \(p,r^k\) data at \(s=1\)
   identically. The compiler emits each endpoint and its training-time
   drift. A slow field without a depth boundary equation uses the first
   \(N\) Legendre coefficients. A historical
   \(\kappa_\alpha(s,t)\) is projected in the same deterministic way,
   using its emitted boundary type or, if none is present, \(N\) ordinary
   Legendre coefficients. It is never put into a representative particle.
   Let
   \(\xi\in\mathbb R^{D_{K,J,N}}\) collect the particle-coordinate
   coefficients, and let \(\kappa\) collect all deterministic population
   coefficients.

   Define the blockwise map
   \(\mathsf P^{\rm depth}_{K,J,N}\) as follows. On a boundary-lifted field
   it sends a training velocity \(\dot u\) to
   \[
   \left(
   \dot u(s_{\rm end}),
   \Pi^{\rm GL}_{N-1,Q}\partial_s\dot u
   \right);
   \]
   on an unconstrained depth field it uses
   \(\Pi^{\rm GL}_{N,Q}\dot u\); and on a depthless scalar it is the
   identity. This fixes the dimension and endpoint evolution of every
   velocity block.
3. On the entire fixed \(Q_{K,J,N}\)-node grid, generate the
   joint fast-tag kernel, a deterministic \(\tanh\)-expression pushforward
   of one finite Gaussian base,
   \[
   \Gamma_{K,J,N}
   (d\zeta\mid\xi,\mathcal M,\kappa)
   \tag{26f}
   \]
   jointly over all nodes.

   The row/column conditioning rule is part of the definition, not an
   orientation label. For each initialization symbol \(W_j^0\), the query
   DAG emits a filtration
   \[
   \mathcal H_0\subset\mathcal H_1\subset\cdots\subset\mathcal H_R.
   \]
   Here \(\mathcal H_0\) contains all non-\(W_j^0\) randomness and current
   global coefficients, and \(\mathcal H_{r-1}\) contains the first
   \(r-1\) emitted row/column answers. The input vector and every coefficient
   of query \(r\) are \(\mathcal H_{r-1}\)-measurable. This ordering is the
   ancestor order of the finite expression DAG. A syntactically
   self-dependent matrix query is outside the retained DAG and is sent to
   the zero closure; it is never resolved by a fixed point.

   For the underlying unconditional symbol write
   \(w=\operatorname{vec}(W_j^0)\sim
   N(0,(\sigma_w^2/n)I_{n^2})\). A row query \(W_j^0u\) is
   \(C_{\rm row}(u)w\), with
   \[
   C_{\rm row}(u)=u^\top\otimes I_n,
   \]
   and a column query \((W_j^0)^\top v\) is
   \(C_{\rm col}(v)w\), with
   \(C_{\rm col}(v)=I_n\otimes v^\top\).
   Stack every previously emitted row and column query into
   \(Z_{\rm old}=C_{\rm old}w\) and every new query into
   \(Z_{\rm new}=C_{\rm new}w\). With the query matrices now measurable,
   the exact target conditioning identity is
   \[
   Z_{\rm new}\mid Z_{\rm old}
   \sim
   N\!\left(
   \Sigma_{\rm no}\Sigma_{\rm oo}^{\dagger}Z_{\rm old},
   \Sigma_{\rm nn}
   -
   \Sigma_{\rm no}\Sigma_{\rm oo}^{\dagger}\Sigma_{\rm on}
   \right).
   \tag{Exact Gaussian condition}
   \]
   To make every finite compiler single-valued across rank changes, fix
   \[
   \tau_{K,J,N}:=2^{-(K+J+N+1)}
   \]
   and emit instead
   \[
   \boxed{
   \begin{aligned}
   m_\tau
   &:=
   \Sigma_{\rm no}
   (\Sigma_{\rm oo}+\tau_{K,J,N}I)^{-1}Z_{\rm old},
   \\
   S_\tau
   &:=
   \left[
   \Sigma_{\rm nn}
   -
   \Sigma_{\rm no}
   (\Sigma_{\rm oo}+\tau_{K,J,N}I)^{-1}
   \Sigma_{\rm on}
   \right]_+
   +
   \tau_{K,J,N}I,
   \\
   Z_{\rm new}\mid Z_{\rm old}
   &\sim N(m_\tau,S_\tau),
   \end{aligned}
   }
   \tag{Compiled Gaussian condition}
   \]
   where \([S]_+\) is the principal spectral projection of the symmetric
   matrix \(S\) onto the positive-semidefinite cone. This fixed ridge is
   part of the \(K,J,N\) approximation and tends to zero along the diagonal
   schedule.
   Here
   \[
   \Sigma_{ab}
   =
   \frac{\sigma_w^2}{n}C_aC_b^\top.
   \]
   Equivalently, its only block identities are
   \[
   \operatorname{Cov}(W^0u,W^0u')
   =
   \sigma_w^2\langle u,u'\rangle_n I_n,
   \]
   \[
   \operatorname{Cov}((W^0)^\top v,(W^0)^\top v')
   =
   \sigma_w^2\langle v,v'\rangle_n I_n,
   \]
   \[
   \operatorname{Cov}(W^0u,(W^0)^\top v)
   =
   \frac{\sigma_w^2}{n}vu^\top.
   \tag{Row/column blocks}
   \]
   The vectorized formula is a semantic derivation, not an
   \(n^2\)-dimensional operation executed by the finite compiler. The
   compiler represents \(\Sigma_{\rm oo}\) as a query-count Gram matrix
   tensored with \(I\), plus the displayed finite-rank cross blocks, and
   eliminates those blocks by finite ridge/Woodbury identities.
   Only matrices whose dimension is bounded by the retained query count may
   enter the emitted DAG. Their normalized scalar entries are previously
   retained moments and \(\kappa\)'s.

   At distinct depth nodes,
   \[
   \operatorname{Cov}(W_j^0u,W_{j'}^0v)
   =
   \mathbf 1_{\{j=j'\}}\,
   \sigma_w^2\langle u,v\rangle_n
   \tag{26f'}
   \]
   before learned-history corrections.

   The exact rule automatically passes the transpose/Onsager identity. If \(h\) is
   independent of \(W^0\), \(\|h\|_n^2\to q\), \(\varphi\) is smooth and
   bounded, and \(Z\sim N(0,\sigma_w^2q)\), the emitted rule must give
   \[
   \left\|
   \mathbb E\!\left[(W^0)^\top\varphi(W^0h)\mid h\right]
   -
   \sigma_w^2\mathbb E[\varphi'(Z)]h
   \right\|_n
   \longrightarrow0.
   \tag{Onsager check}
   \]
   The compiled rule converges to the same identity as
   \(\tau_{K,J,N}\downarrow0\); its innovation covariance is
   \(S_\tau\). Thus transpose reuse cannot be replaced by an independent
   Gaussian tag.
   Gaussian conditioning applies only to \(W^0\). The historical
   \(\kappa\)-ODEs and the insertions \(\mathsf U_q,\mathsf V_q\) determine
   every retained query of \(W(t)-W^0\) from current state alone.

   The SCC-promotion rule above makes the emitted covariance/moment order
   acyclic: every conditioning block uses only prior algebraic blocks,
   current moments supplied as inputs, or historical \(\kappa\)-state. An
   implicit self-consistency root is not permitted.
4. Treat \(e_1,\ldots,e_m\) as formal independent symbols. Apply the
   displayed chain rules and the fixed zero closure, and verify
   symbolically that
   \[
   \mathscr D_{K,J}
   =
   \sum_{q=1}^m e_q\mathscr D_{K,J}^{(q)}
   \tag{26g'}
   \]
   with no constant or higher-degree remainder. This is an algebraic
   consequence of first-order gradient flow; coefficient extraction is
   performed before closure or Gaussian integration. Integrate each label
   coefficient against the fast kernel and use the fixed projection:
   \[
   \boxed{
   V^{(q)}_{K,J,N}(\xi;\mathcal M,\kappa)
   :=
   \mathsf P^{\rm depth}_{K,J,N}
   \int
   \mathsf C_{K,J}\mathscr D_{K,J}^{(q)}
   (\iota_N\xi,\zeta;\mathcal M,\kappa)
   \,\Gamma_{K,J,N}(d\zeta\mid\xi,\mathcal M,\kappa).
   }
   \tag{26g}
   \]
   The same operation emits every \(B_\alpha^{(q)}\).
   Here \(\mathscr D_{K,J}^{(q)}\) is a finite expression DAG, not an
   infinite hierarchy operator.
5. Replace every normalized contraction in \(\mathcal M\) by its current
   moment under the coefficient law. Use the same \(Q_{K,J,N}\) nodes and
   weights in the fast kernel, observable reconstruction, and tangent
   kernel. All projection/aliasing error is part of the \(N\)-defect.
6. Emit \(\mathcal A_{K,J,N}\), the set of pairs \((\rho,\kappa)\) having
   all moments called by the DAGs, satisfying the emitted depth boundary
   lifts and algebraic moment identities. Covariance matrices are evaluated
   by (Compiled Gaussian condition), so neither a rank stratum nor a
   separately selected covariance branch is restart data. The fast law is
   uniquely reconstructed as
   \(\Gamma_{K,J,N}(\,\cdot\mid\xi,\mathcal M[\rho],\kappa)\).
   This admissible set is common to the whole static neighborhood
   \(\mathcal U\), not chosen separately from a positive-time trajectory.
   It contains all compiled initial pairs
   \((\rho_{K,J,N}^\vartheta(0),
   \kappa_{K,J,N}^\vartheta(0))\) for \(\vartheta\in\mathcal U\).

The budgeted least-fixed-point enumeration, SCC promotion, zero closure,
fixed ridge, and PSD projection make every step total. Hence
\(\operatorname{Compile}(K,J,N,\vartheta)\) returns the displayed finite
tuple for every \(K,J\ge0\), \(N\ge2\), and
\(\vartheta\in\mathcal U\); “compilation succeeds” is not an additional
analytic conjecture.

No positive-time value of the exact network, exact loss curve, target hitting
time, or exact hierarchy tail is queried.

The important type distinction is now explicit:
\(V^{(q)}_{K,J,N}\) is the finite characteristic velocity produced by
(26g);
\(\mathscr G\) is the conjectural infinite law generator in (26b).
The finite PDE does not evaluate \(\mathscr G\), its graph limit, or an
inverse interpolation. Their difference appears only in the semantic
residual used to assess the already-defined PDE.

### 6.3 Autonomous Liouville PDE

The compiler produces the finite McKean–Vlasov PDE–ODE system

\[
\boxed{
\begin{aligned}
\partial_t\rho_{K,J,N}
&+
\nabla_\xi\!\cdot
\left[
\rho_{K,J,N}
\sum_{q=1}^m
e_q[\rho_{K,J,N}]
V^{(q)}_{K,J,N}
\left(
\xi;\mathcal M[\rho_{K,J,N}],\kappa_{K,J,N}
\right)
\right]
=0,
\\
\dot\kappa_{\alpha,K,J,N}
&=
\sum_{q=1}^m
e_q[\rho_{K,J,N}]
B_{\alpha,K,J,N}^{(q)}
\left(
\mathcal M[\rho_{K,J,N}],\kappa_{K,J,N}
\right).
\end{aligned}
}
\tag{PDE-\(K,J,N\)}
\]

This is literally one finite continuity equation if desired. Put
\(\bar\rho=\rho\otimes\delta_\kappa\) on the augmented coordinate
\(\bar\xi=(\xi,\kappa)\), and
\(\bar V^{(q)}=(V^{(q)},B^{(q)})\). Then

\[
\boxed{
\partial_t\bar\rho
+
\nabla_{\bar\xi}\!\cdot
\left[
\bar\rho
\sum_{q=1}^m e_q[\bar\rho]\,
\bar V^{(q)}
\left(
\bar\xi;\mathcal M[\bar\rho]
\right)
\right]
=0,
\qquad
\bar\rho(0)=\rho(0)\otimes\delta_{\kappa(0)}.
}
\tag{Augmented PDE}
\]

The Dirac \(\kappa\)-marginal is preserved because its velocity is common to
all particles. Arbitrarily spreading a population coefficient at restart
is therefore not admissible.

Here:

- \(\mathcal M[\rho]\) is the finite list of current contractions specified
  by the tagged grammar;
- \(e[\rho]=f[\rho]-y\);
- \(V^{(q)}_{K,J,N}\) and \(B^{(q)}_{K,J,N}\) are the label-separated
  finite expressions emitted in step 4, obtained by
  differentiating (1), (5)–(7), applying (17)–(22), and applying the
  zero closure \(\mathsf C_{K,J}\);
- the Legendre lifting, projection, and quadrature rule are exactly the
  matrices in step 2;
- \((\rho_{K,J,N}(0),\kappa_{K,J,N}(0))\) is computed from (3) by finite
  Gaussian conditioning, never by a positive-time fit.

The PDE is finite: its augmented source dimension is
\[
D_{K,J,N}+\dim\kappa_{K,J,N},
\]
and this dimension and the expression template depend only on
\((m,K,J,N)\), while emitted numerical coefficients depend explicitly on
\(\vartheta\). Neither dimension nor template depends on \(n\), \(L\), or a
requested training horizon.

It is autonomous on \(\mathcal A_{K,J,N}\): the restart datum is the pair
\((\rho,\kappa)\), and the fast kernel is reconstructed by (26f), not
supplied as an independent or history-dependent object. Global
well-posedness from the compiled initial family and the semigroup property
on its reachable subset are part of Clause B below.

For clarity, the chain-rule part hidden by no notation is

\[
\dot z_r^\ell
=
-\gamma\sum_qe_q\beta_q^\ell G^{h,\ell}_{qr}
+
W_\ell v_r^\ell,
\tag{26h}
\]

\[
\dot D_r^\ell
=
\operatorname{diag}
\left(
\tanh''(z_r^\ell)\odot\dot z_r^\ell
\right),
\tag{26i}
\]

\[
\dot A_r^\ell
=
\gamma\left(
\dot D_r^\ell W_\ell
+
D_r^\ell\dot W_\ell
\right),
\tag{26i'}
\]

\[
\dot\beta_r^\ell
=
\dot D_r^\ell p_r^{\ell+1}
+
D_r^\ell w_r^{\ell+1},
\tag{26j}
\]

\[
\frac d{dt}G^{u,\ell}_{rq}
=
\frac1n
\left[
(\dot u_r^\ell)^\top u_q^\ell
+
(u_r^\ell)^\top\dot u_q^\ell
\right].
\tag{26k}
\]

Every new term such as \(W_\ell q^k\) or
\(W_\ell^\top r^k\) is assigned its orientation and grade. Terms of grade at
most \(K\) are retained; every higher term, including every Gaussian
conditioning contraction returning it to a retained coordinate, is included
in the outgoing residual. Thus “mechanically generated” means the finite
rules (17)–(18), (20)–(22), and (26h)–(26k), not an unspecified closure
choice.

The theorem (24) controls the subfamily omitted solely because it contains
more than \(K\) chronological dense continuations. The quantitative
residual proposal (42) is deliberately stronger: it also counts nonlinear
chain-rule branches and every high-to-low Gaussian/cavity contraction. This
distinction prevents the factorial propagator estimate from being mistaken
for the unproved width-law closure.

### 6.4 Observable reconstruction

Outputs and hidden Grams are moments:

\[
f_{K,J,N,r}(t)
=
\int a\,h_r(1)\,d\rho_{K,J,N},
\tag{27}
\]

\[
G^{h,K,J,N}_{rq}(s,t)
=
\int h_r(s)h_q(s)\,d\rho_{K,J,N}.
\tag{28}
\]

Fast-tag moments are conditional moments, not Legendre reconstructions. For
example, at a quadrature node,

\[
\widehat G^\beta_{rq}(s_j)
=
\int_{\xi}
\int_{\zeta}
\beta_r\beta_q\,
\Gamma_{K,J,N}
(d\zeta\mid\xi,\mathcal M[\rho],\kappa)
\,\rho_{K,J,N}(d\xi).
\tag{28a}
\]

Use the fixed positive
\(Q_{K,J,N}\)-point Gauss–Legendre nodes \(s_j\) and weights \(w_j\) from
step 2 to reconstruct the tangent kernel:

\[
\boxed{
\widehat\Theta_{rq}^{K,J,N}
=
\widehat G^h_{rq}(1)
+
Q^x_{rq}\widehat G^p_{rq}(0)
+
\gamma^2
\sum_{j=1}^{Q_{K,J,N}}w_j
\widehat G^h_{rq}(s_j)
\widehat G^\beta_{rq}(s_j).
}
\tag{29}
\]

This is positive semidefinite by construction. A naive entrywise polynomial
projection would not guarantee that property.

Equations (27)–(29) define the compiler-emitted observable map

\[
\boxed{
\mathcal R^{\rm obs}_{K,J,N}(\rho,\kappa)
:=
\left(
f_{K,J,N},\
G^{h,K,J,N},\
\widehat\Theta^{K,J,N}
\right).
}
\tag{29a}
\]

It is a finite moment/conditional-moment formula and does not invoke the
infinite hierarchy space.

---

## 7. First nontrivial response block

The grade-zero model retains direct forcing but no propagated dense reuse.
Define the finite number
\[
J_*:=
\min\left\{
J:
\begin{array}{l}
\text{the joint least-fixed-point table at }(K,J)=(1,J)\\
\text{contains every tag, oriented query, and }\kappa\text{-record}\\
\text{required by one expansion of (30)–(35) and (26h)–(26k)}
\end{array}
\right\}.
\]
The first genuinely nontrivial finite compiler is \(K=1,J=J_*\): it keeps
one ordered dense continuation and every nonlinear chain-rule term required
by the displayed first-response block.

Its forward response block is

\[
\boxed{
\partial_sq^0_{r\leftarrow q}
=-\gamma^2D_r\beta_qG^h_{qr},
\qquad
q^0_{r\leftarrow q}(0)=-Q^x_{qr}p_q(0),
}
\tag{30}
\]

\[
\boxed{
\partial_sq^1_{r\leftarrow q}
=\gamma D_rWq^0_{r\leftarrow q},
\qquad
q^1_{r\leftarrow q}(0)=0,
}
\tag{31}
\]

\[
\boxed{
\partial_th_r
=
\sum_qe_q
\left(
q^0_{r\leftarrow q}
+
q^1_{r\leftarrow q}
\right).
}
\tag{32}
\]

Its backward response block is

\[
\boxed{
-\partial_sr^0_{r\leftarrow q}
=
\left((\partial_tA_r)_{\leftarrow q}\right)^\top p_r,
\qquad
r^0_{r\leftarrow q}(1)=-h_q(1),
}
\tag{33}
\]

\[
\boxed{
-\partial_sr^1_{r\leftarrow q}
=A_r^\top r^0_{r\leftarrow q},
\qquad
r^1_{r\leftarrow q}(1)=0,
}
\tag{34}
\]

\[
\boxed{
\partial_tp_r
=
\sum_qe_q
\left(
r^0_{r\leftarrow q}
+
r^1_{r\leftarrow q}
\right).
}
\tag{35}
\]

Equations (27)–(35), the chain-rule equations for
\((z,\beta)\), the current-moment substitutions, and the Liouville equation
\((\mathrm{PDE}\text{-}1,J_*,N)\) define the proposed first response PDE.
The displayed \(W\)-tags in (31) and (34) are fast variables integrated
against \(\Gamma_{1,J_*,N}\); they are not hidden matrix-valued source
fields.

Equations (30)–(35) alone are only the schematic response block: raw
\(W,A,\partial_tA\) notation is eliminated only when
\(\operatorname{Compile}(1,J_*,N,\vartheta)\) emits the finite tuple
(Compiler). Thus no claim of a closed PDE is made without the finite
expression DAG, moment and history tables, oriented fast Gaussian
pushforward, admissible restart set, and initial pair specified in Section
6.

All terms with two or more additional ordered \(W/W^\top\) continuations are
not hidden: they are the explicitly named outgoing residual.

For a fixed trajectory on \([0,T]\),

\[
\sup_{t\le T}\|v-v^{[1]}\|_n
\le
B_{v,T}e^{\Lambda_T}\frac{\Lambda_T^2}{2}.
\tag{36}
\]

At standard \(\gamma=1\), this bound is conservative and can exceed one.
Therefore \(K=1,J=J_*\) is a proposed first model, not a certified universal
accuracy level. The empirical audit below tests its finite-width \(q/r\)
response projection, not the homogenized Liouville limit.

---

## 8. The sharp conjecture

### 8.1 Hierarchy norm

Let
\[
\mathscr T_\infty
:=
\bigcup_{K,J\ge0}
\left(
\mathscr T_{K,J}\sqcup\mathscr K_{K,J}
\right)
=
\mathscr T_\infty^{\rm slow}
\sqcup
\mathscr T_\infty^{\rm fast},
\]
and fix an enumeration in nondecreasing \((g,c)\). A hierarchy state \(Y\)
is the consistent projective family of all finite joint laws of these tags.

For the first \(R\) tags and every integer \(p\ge1\), define the membership
seminorm

\[
\boxed{
[Y]_{R,p}
:=
\sum_{\substack{\omega\le R\\\omega\ {\rm slow}}}
\left(
\|Y_\omega\|_{L^\infty_sL^p}
+
\|\partial_sY_\omega\|_{L^1_sL^p}
\right)
+
\sum_{\substack{\omega\le R\\\omega\ {\rm fast}}}
\|Y_\omega\|_{L^p(ds\,dY)}.
}
\tag{37}
\]

Fast Young tags have no \(\partial_s\) term. Let \(\mathfrak X\) be the
projective all-moment space in which every \([Y]_{R,p}\) is finite, with
the Fréchet topology generated by these seminorms and finite-dimensional
Wasserstein distances. This fixes the Hölder direction correctly: a product
of \(r\) retained tags in \(L^p\) is controlled by their \(L^{rp}\)
seminorms, which are present because all \(p<\infty\) are required.

Fix the compatible metric

\[
d_{\mathfrak X}(Y,\widetilde Y)
:=
\sum_{R,p\ge1}
2^{-(R+p)}
\frac{d_{R,p}(Y,\widetilde Y)}
{1+d_{R,p}(Y,\widetilde Y)},
\tag{37b}
\]

where \(d_{R,p}\) is the \(p\)-Wasserstein distance between the first \(R\)
joint tag laws plus the \(L^1_s\) distance between their slow weak-depth
derivatives.

For a signed law-generator residual \(\nu\), use the cylindrical
bounded-Lipschitz dual seminorm

\[
\boxed{
\|\nu\|_{\mathfrak X_-}
:=
\sum_{R=1}^{\infty}2^{-R}
\sup_{\substack{\Psi\in C_b^1(\mathbb R^{d_R})\\
\|\Psi\|_\infty+\|\nabla\Psi\|_\infty\le1}}
\left|
\left\langle
\pi_R\nu,\Psi
\right\rangle
\right|,
}
\tag{37a}
\]

where \(\pi_R\) includes depth integration for fast tags and the slow
depth-field coordinates. This is a norm on cylindrical signed measures
modulo equality of all finite projections, which is exactly the level at
which (26a) defines the generator.

Let \(\mathscr G:Y\mapsto\partial_tY\) be the infinite law generator in
(26b). For the optional hierarchy residual only, define
\(\mathcal E_{K,J,N}(\rho,\kappa)\in\mathfrak X\) by reconstructing every
retained slow tag from its depth coefficients, every retained fast tag from
\(\Gamma_{K,J,N}\), and adjoining deterministic zero coordinates for every
omitted tag in the fixed enumeration of \(\mathscr T_\infty\). This
zero-extension gives a consistent projective joint law. It is distinct from
the observable map \(\mathcal R^{\rm obs}_{K,J,N}\) in (29a).

### 8.2 Conjecture

> **Dense Euclidean continuous-depth response-PDE conjecture.**
>
> For \(\vartheta=(X,y,\sigma_w,A,\gamma)\in\mathcal U\), use the standard
> iid dense initialization (3), full Euclidean \(\mu\)P flow (4), and the
> ordered limits (12). Let
> \((\rho^\vartheta_{K,J,N},\kappa^\vartheta_{K,J,N})\) be the solution of
> the explicitly compiled equation
> \((\mathrm{PDE}\text{-}K,J,N)\), with the finite zero closure
> \(\mathsf C_{K,J}\) and static Gaussian initial pair specified in
> Section 6.
>
> **A. Observable target.**  
> For every \(t\ge0\), the ordered width-then-depth limit of
> \[
> \mathcal O_{n,L}^\vartheta(t)
> :=
> \left(
> f_{n,L}^\vartheta(t),\
> G_{n,L}^{h,\vartheta}(\cdot,t),\
> \Theta_{n,L}^\vartheta(t)
> \right)
> \]
> exists in
> \(\mathbb R^m\times C([0,1],\mathbb R^{m\times m})\times
> \mathbb R^{m\times m}\); call it \(\mathcal O_\vartheta(t)\).
> This is an observable quotient statement and does not require uniqueness
> of hierarchy coordinates invisible to \(d_{\rm obs}\).
>
> **B. Finite PDE well-posedness and restart domain.**  
> Fix a priori the computable diagonal schedule
> \[
> \boxed{\iota_\ell=(K_\ell,J_\ell,N_\ell)=(\ell,\ell,\ell).}
> \]
> It is emitted before any positive-time data and is independent of
> \(\vartheta\). There is a finite \(\ell_0\) such that, for every
> \(\ell\ge\ell_0\),
> \(\operatorname{Compile}(\iota_\ell,\vartheta)\) returns for every
> \(\vartheta\in\mathcal U\), and the coupled characteristic system has a
> unique global solution from every compiled initial pair. Every reached
> pair lies in the common emitted set
> \(\mathcal A_{\iota_\ell}\), and the autonomous flow satisfies
> \[
> S^\vartheta_{\iota_\ell}(t+s)
> =
> S^\vartheta_{\iota_\ell}(t)S^\vartheta_{\iota_\ell}(s)
> \]
> for each fixed \(\vartheta\in\mathcal U\).
> Restart data are exactly an admissible pair \((\rho,\kappa)\); the fast
> kernel is reconstructed from that pair. In particular, restarting from
> any reached state uses the same semigroup and no past trajectory.
>
> **C. Direct finite-PDE convergence.**  
> With
> \[
> d_{\rm obs}(Y,\widetilde Y)
> :=
> \|f-\widetilde f\|_2
> +
> \sup_{s\in[0,1]}
> \|G^h(s)-\widetilde G^h(s)\|_F
> +
> \|\Theta-\widetilde\Theta\|_F,
> \]
> the explicitly displayed PDE family satisfies
> \[
> \boxed{
> \lim_{\ell\to\infty}
> \sup_{\vartheta\in\mathcal U}
> \sup_{t\ge0}
> d_{\rm obs}\!\left(
> \mathcal O_\vartheta(t),
> \mathcal R^{\rm obs}_{\iota_\ell}
> \left(
> \rho^\vartheta_{\iota_\ell}(t),
> \kappa^\vartheta_{\iota_\ell}(t)
> \right)
> \right)
> =0.
> }
> \tag{38}
> \]
>
> **D. Strong finite-network consistency (additional strengthening).**  
> For every \(\varepsilon>0\),
> \[
> \boxed{
> \lim_{\ell\to\infty}
> \limsup_{L\to\infty}
> \limsup_{n\to\infty}
> \sup_{\vartheta\in\mathcal U}
> \Pr\!\left[
> \sup_{t\ge0}\mathsf{Err}^{\vartheta}_{n,L;\iota_\ell}(t)
> >\varepsilon
> \right]
> =0,
> }
> \tag{39}
> \]
> where \(\mathsf{Err}\) is the same output/hidden-Gram/tangent-kernel
> distance used in (38), with the finite-depth Gram linearly interpolated
> in \(s\).

Equation (38)—not a particular proof technique or convergence rate—is the
core conjecture's irreducible content. Clauses A–C are exactly the requested
uniform, all-time, accuracy-dependent finite-PDE approximation. Thus a
failure of a proposed coercivity lemma or of the factorial rate below does
not make A–C false. To refute the core conjecture one must show that the
displayed architecture-derived PDEs fail along the fixed diagonal schedule,
or that the exact width-then-depth observable target does not exist. Clause
D is deliberately stronger: it additionally asserts an all-time uniform
identification with finite networks and can fail without refuting A–C.

### 8.3 Quantitative strengthening and proposed proof certificate

The evidence suggests the following stronger route to (38), but these
conditions are not additional clauses in the conjecture.

The graph limit (26b) should be single-valued on the observable quotient and
have a global solution \(Y_\vartheta\in C([0,\infty),\mathfrak X)\)
projecting to \(\mathcal O_\vartheta\). Every two-training-time or
causal-history quantity required by an equivalent fixed-depth DMFT
representation should either be eliminated by (14)–(22) or represented in
\(\mathscr T_\infty\) with autonomous current-time evolution. This is the
proposed Markovization theorem.

There should exist uniform
\(\lambda_*,\Lambda_*,\Lambda,C_{\rm stab}>0\) and a restart tube
\(\mathcal T\subset\mathfrak X\) such that

\[
\lambda_*I_m\preceq\Theta(t)\preceq\Lambda_*I_m,
\qquad
\sup_t\limsup_{L\to\infty}\limsup_{n\to\infty}
\frac1L\sum_\ell\|A_r^\ell(t)\|_{\rm op}
\le\Lambda,
\tag{40}
\]

and every absolutely continuous comparison path \(\widetilde Y\in\mathcal
T\) obeys

\[
\boxed{
\sup_{t\ge0}d_{\rm obs}(Y(t),\widetilde Y(t))
\le
C_{\rm stab}
\left[
d_{\mathfrak X}(Y(0),\widetilde Y(0))
+
\int_0^\infty
\|\partial_t\widetilde Y-\mathscr G(\widetilde Y)\|
_{\mathfrak X_-}dt
\right].
}
\tag{41}
\]

There should also be defects
\(\delta_{K,J,N}\downarrow0\) as \(\min(K,J,N)\to\infty\), for which
\(\mathcal E_{K,J,N}(\rho_{K,J,N}(t),\kappa_{K,J,N}(t))\in\mathcal T\)
for all \(t\), and the following **semantic residual target** holds:

\[
\boxed{
d_{\mathfrak X}\!\left(
Y(0),
\mathcal E_{K,J,N}(\rho_{K,J,N}(0),\kappa_{K,J,N}(0))
\right)
+
\int_0^\infty
\left\|
\partial_t\mathcal E_{K,J,N}(\rho_{K,J,N},\kappa_{K,J,N})
-
\mathscr G\!\left(
\mathcal E_{K,J,N}(\rho_{K,J,N},\kappa_{K,J,N})
\right)
\right\|_{\mathfrak X_-}
dt
\le
C_{\rm res}\left[R_K(\Lambda)+\delta_{K,J,N}\right].
}
\tag{42}
\]

Equation (42) is not itself an executable certificate: its integrand
contains the graph-limit operator \(\mathscr G\). It is the analytic
inequality a proof must establish. Equations (41)–(42) would imply the
quantitative estimate

\[
\sup_{t\ge0}d_{\rm obs}\!\left(
Y(t),
\mathcal E_{K,J,N}(\rho_{K,J,N}(t),\kappa_{K,J,N}(t))
\right)
\le
C_{\rm stab}C_{\rm res}\left[
e^\Lambda\frac{\Lambda^{K+1}}{(K+1)!}
+\delta_{K,J,N}
\right].
\tag{43}
\]

### 8.4 Direct implication

Clause (38) alone gives non-effective existence: for every
\(\varepsilon>0\), some finite index \(\ell\) on the fixed diagonal schedule
has all-time observable error below \(\varepsilon\). An effective accuracy
compiler would additionally require that the (Compiler) output contract be
augmented to return certified upper bounds for
\(C_{\rm stab},C_{\rm res},\Lambda\), an effective modulus for
\(\delta_{K,J,N}\), and a finite nonnegative DAG
\(\widehat\Delta_{K,J,N}(\rho,\kappa)\), together with a static bound
\(\widehat\Delta^0_{K,J,N}\) on the initial hierarchy defect. An independent
domination theorem would have to prove, throughout the restart tube,

\[
\left\|
\partial_t\mathcal E_{K,J,N}(\rho,\kappa)
-
\mathscr G(\mathcal E_{K,J,N}(\rho,\kappa))
\right\|_{\mathfrak X_-}
\le
\widehat\Delta_{K,J,N}(\rho,\kappa).
\tag{43a}
\]

Only then could the finite trajectory provide a checkable error certificate.
The executable selection rule would choose the first diagonal index
\(\ell\) for which

\[
\boxed{
C_{\rm stab}
\left[
\widehat\Delta^0_{\ell,\ell,\ell}
+
\int_0^\infty
\widehat\Delta_{\ell,\ell,\ell}
\left(
\rho_{\ell,\ell,\ell}(t),
\kappa_{\ell,\ell,\ell}(t)
\right)dt
\right]
\le\varepsilon.
}
\tag{44}
\]

The factorial expression in (43) may replace the bracket in (44) only after
a separate theorem certifies that it dominates this finite majorant and the
initial defect.

Then \((\mathrm{PDE}\text{-}\ell,\ell,\ell)\) is an
accuracy-\(\varepsilon\) finite PDE.
Its number of fields, source coordinates, and coefficient description are
finite and depend on \((m,\varepsilon)\), but not on width, original depth,
or physical training horizon.

This is precisely the desired accuracy-dependent approximate-PDE existence
statement.

---

## 9. Why the conjecture has no oracle loophole

The conjecture requires all of the following simultaneously.

1. **Uniform neighborhood.** One compiler works for every model in
   \(\mathcal U\), rather than one preselected scalar curve.
2. **Fixed grammar.** Its coefficients are generated from the displayed
   architecture, activation derivatives, Gaussian initialization, and
   current contractions only.
3. **No free constants, functions, or operators.** Every coefficient is a
   displayed architecture constant, a fixed Legendre/Gauss quadrature
   entry, or a finite Gaussian conditional moment determined by (3).
   Graph limits, unevaluated DMFT rules, and arbitrary source profiles are
   forbidden inside the finite drift.
4. **No future queries.** Exact positive-time outputs, Grams, response
   fields, target times, or trajectory samples are forbidden inputs.
5. **Fixed approximation schedule.** The diagonal
   \((K,J,N)=(\ell,\ell,\ell)\) is fixed before any target trajectory is
   observed; no oracle-selected subsequence is allowed.
6. **Restartability.** The same autonomous vector field works after restart
   from every reached state in the emitted admissible set
   \(\mathcal A_{K,J,N}\). Restart data contain \((\rho,\kappa)\), while
   the fast kernel is reconstructed rather than supplied.
7. **Oriented conditioning.** Every row/column query is jointly conditioned
   by (Compiled Gaussian condition), converges to (Onsager check), and uses
   an emitted topological order. An implicit covariance root is forbidden.
8. **Current-state learned history.** Every retained action of
   \(W(t)-W^0\) is carried by an enumerated, budgeted historical
   \(\kappa\)-coordinate with an emitted ODE; a hidden past-time integral is
   forbidden.
9. **Optional effective certification.** Any claimed computable error bar
   must come with a finite majorant such as
   \(\widehat\Delta_{K,J,N}\) and a proved domination theorem such as
   (43a). The semantic residual (42) is not itself executable. The
   non-effective convergence statement (38) does not presuppose this proof
   route.
10. **Multiple observables.** It predicts \(f\), every depthwise hidden Gram,
   and \(\Theta\), not only loss.
11. **Complexity accounting.** \(D_{K,J,N}\) and every operator used by the PDE
   are finite and independent of \(n,L\), and time horizon.
12. **No hidden matrix state.** Retaining an \(n\times n\) field, a
   width-growing source, or an exact trajectory table is outside the
   admissible class.
13. **Correct depth limit.** Galerkin projection is applied to homogenized
   order parameters after the fixed-\(L\) width limit, never to the raw iid
   matrices.
14. **PSD reconstruction.** The approximate kernel is a constructed
    positive-semidefinite Gram proxy, so convergence cannot be manufactured
    by an unstable negative kernel.

Under these clauses, an unrestricted two-state Bernstein playback of the
exact curve is inadmissible. Conversely, a negative resolution requires a
genuine failure of the direct convergence (38) or of the dense width/depth
target; a nonvanishing outgoing-residual lower bound is one admissible route.
A complaint about an unspecified coefficient is not, because the output
contract (Compiler) requires every finite coefficient to be emitted.

---

## 10. Theoretical evidence

### 10.1 Exact positive results

The following parts do not depend on the conjecture:

- equations (5)–(11);
- the necessity of the \(L\)-scaled hidden rate;
- the response recurrence (14)–(22);
- the exact-source factorial remainders (24)–(25a);
- positive-semidefinite tangent-kernel reconstruction (29).

### 10.2 Why the old quadratic obstruction is absent

The earlier two-hidden-layer quadratic model combined:

- unbounded polynomial feedback;
- Gaussian extreme-neuron tails;
- factorial Gaussian moments;
- a training-time Taylor compiler.

For every fixed expression budget \(J\), all activation derivatives that
appear in the compiled vector field are bounded on the real axis. Those
bounds are not uniform in \(J\): because the complex poles of \(\tanh\) are
at finite distance from the real axis, derivative bounds grow factorially
along a subsequence. Thus bounded activation prevents amplitude blow-up at
each fixed \(J\), but does not by itself prove decay of the nonlinear
expression residual \(\delta_{K,J,N}\).

More importantly, the response approximation is a real-axis,
finite-width-first Volterra truncation in **depth**, not a Taylor series in
training time. Its \(1/j!\) comes from ordered depth-simplex volume, not from
cancellation of divergent Wick coefficients.

### 10.3 Prelimit-first proof route

The most promising proof order is:

1. establish width/depth-uniform operator-norm and residual-arclength bounds;
2. truncate the finite-\((n,L)\) response propagator using (24);
3. prove a source-stability estimate controlling
   \(E_{A,K,T}\) in (25b);
4. discretize training time only after the pathwise truncation;
5. for fixed \(K,J,L\), evaluate the finite Gaussian-conditioning compiler
   and take its deterministic width limit with orientation tags;
6. take the homogenized \(L\to\infty\) limit;
7. remove the finite depth projection \(N\);
8. use (10), kernel coercivity, and (42) for all physical time.

The pathwise Dyson estimate controls omitted pure propagator continuations.
Before Gaussian conditioning, one must additionally control the induced
\(\dot A\)-source error and the non-propagator chain-rule branches.
High-grade nonlinear and cavity contractions remain part of the
conjectural full outgoing residual (42); (24) alone does not bound them.

### 10.4 Related rigorous and DMFT evidence

Existing work supports individual ingredients but does not prove this
conjecture:

- [Yang and Hu, *Feature Learning in Infinite-Width Neural
  Networks*](https://arxiv.org/abs/2011.14522) establishes the
  infinite-width feature-learning role of \(\mu\)P.
- [Bordelon et al., *Depthwise Hyperparameter Transfer in Residual
  Networks: Dynamics and Scaling
  Limit*](https://arxiv.org/abs/2309.16620) derives large-width/depth
  forward/backward DMFT and response equations for a related
  \(L^{-1/2}\) residual scaling.
- [Yao, Wu, and Gao, *Feature Learning Dynamics in Infinite-Depth Neural
  Networks*](https://arxiv.org/abs/2512.21075) proves a
  coupled forward/backward stochastic limit and depth-induced suppression of
  reused-weight coupling in a related one-layer depth-\(\mu\)P ResNet.
- [Chaintron, Chizat, and Maass, *ResNets of All Shapes and Sizes:
  Convergence of Training Dynamics in the Large-scale
  Limit*](https://arxiv.org/abs/2603.18168) obtains quantitative joint
  large-scale convergence for a different two-layer residual block using
  functional skeleton maps, after a bounded number of training steps.

These materially different scalings, blocks, and horizons support analogous
limits and the proposed proof strategy. They do not supply the global
all-time response residual (42) for the present fully dense \(1/L\) model.

---

## 11. Numerical audit

### 11.1 Protocol

Two distinct simulations were kept separate.

First, the exact finite network (1)–(7) was integrated directly with

\[
m=3,\quad y=(0.8,-0.55,0.35),\quad
\sigma_w=0.65,\quad A=\gamma=1,
\]

\[
n\in\{32,64,96\},
\qquad
L\in\{8,16,32\}.
\]

All \(W_\ell,B,a\) were unconstrained and trained. A finite-difference audit
of one \(a\), one \(B\), and one \(W\) coordinate agreed with the analytic
\(\mu\)P vector field to between \(2.6\times10^{-12}\) and
\(3.0\times10^{-11}\).

Second, a separate code differentiated the exact forward and backward
depth recurrences and implemented the coupled per-leg \(q^k/r^k\)
training-response cutoff (17)–(22). In this coupled cutoff, the backward
source \(\dot A_K\) is recomputed from the truncated forward velocity, as in
(25b). It evolved \(h,p,W,a\) with projected
\(\partial_th,\partial_tp\). This retains the full \(n\times n\) matrices,
so it tests the response truncation but not the finite Liouville PDE.

As an algebraic audit, setting \(K=L\) reproduced the exact
\(\partial_th\) and \(\partial_tp\) with maximum relative error
\(3.37\times10^{-16}\) over ten runs.

### 11.2 Instantaneous \(q/r\) response decay

Ten stored configurations covered \(n\in\{32,64\}\),
\(L\in\{8,16,32\}\), seed values \(1,\ldots,6\), and three positive-time
restarts. Seed \(1\) was reused across five width/depth configurations;
seeds \(4,5,6\) supplied the restarts. At the point of projection:

| Grade | Median relative \(\partial_th\) error | Range | Median coupled \(\partial_tp\) error | Range |
|---:|---:|---:|---:|---:|
| 0 | \(8.08\times10^{-2}\) | \(5.48\times10^{-2}\)–\(1.28\times10^{-1}\) | \(8.61\times10^{-2}\) | \(6.00\times10^{-2}\)–\(1.19\times10^{-1}\) |
| 1 | \(5.32\times10^{-3}\) | \(2.81\times10^{-3}\)–\(1.43\times10^{-2}\) | \(5.80\times10^{-3}\) | \(3.03\times10^{-3}\)–\(1.18\times10^{-2}\) |
| 2 | \(2.97\times10^{-4}\) | \(1.07\times10^{-4}\)–\(1.31\times10^{-3}\) | \(3.20\times10^{-4}\) | \(1.41\times10^{-4}\)–\(8.32\times10^{-4}\) |
| 3 | \(1.61\times10^{-5}\) | \(3.83\times10^{-6}\)–\(8.50\times10^{-5}\) | \(1.66\times10^{-5}\) | \(5.21\times10^{-6}\)–\(5.90\times10^{-5}\) |

An independent exact-source backward diagnostic, which held \(\dot A\)
exact as required by (25a), gave median errors
\(5.802\times10^{-3}\) at \(K=1\) and
\(3.198\times10^{-4}\) at \(K=2\). Thus the reported coupled values are
numerically close here, but they test the stronger source-substituted
approximation rather than the pure backward factorial tail.

For \(n=64\), seed \(1\), increasing depth improved the first-response
error:

| \(L\) | \(K=1\), \(\partial_th\) | \(K=1\), \(\partial_tp\) | \(K=2\), \(\partial_th\) | \(K=2\), \(\partial_tp\) |
|---:|---:|---:|---:|---:|
| 8 | \(1.19\times10^{-2}\) | \(1.04\times10^{-2}\) | \(8.60\times10^{-4}\) | \(8.17\times10^{-4}\) |
| 16 | \(6.41\times10^{-3}\) | \(5.04\times10^{-3}\) | \(4.03\times10^{-4}\) | \(3.06\times10^{-4}\) |
| 32 | \(2.81\times10^{-3}\) | \(3.03\times10^{-3}\) | \(1.26\times10^{-4}\) | \(1.41\times10^{-4}\) |

### 11.3 Integrated projected-hierarchy error

The \(K=1\) and \(K=2\) finite-matrix projected systems were run for another
\(0.8\) units and compared with exact training:

| Quantity | \(K=1\) median (range) | \(K=2\) median (range) |
|---|---:|---:|
| Output error | \(2.05\times10^{-4}\) \((1.60\times10^{-5},4.59\times10^{-4})\) | \(7.37\times10^{-6}\) \((2.83\times10^{-7},6.17\times10^{-5})\) |
| Mid-depth Gram error | \(4.36\times10^{-4}\) \((4.38\times10^{-5},2.40\times10^{-3})\) | \(2.86\times10^{-5}\) \((2.39\times10^{-6},1.20\times10^{-4})\) |
| Terminal Gram error | \(9.20\times10^{-4}\) \((1.03\times10^{-4},4.38\times10^{-3})\) | \(6.69\times10^{-5}\) \((9.54\times10^{-6},5.21\times10^{-4})\) |

For \(n=64,L=16\), halving the Heun step from \(0.01\) to \(0.005\)
changed the \(K=1\) terminal-Gram error from
\(8.180\times10^{-4}\) to \(8.181\times10^{-4}\), and the \(K=2\) value
from \(1.0182\times10^{-4}\) to \(1.0185\times10^{-4}\).

### 11.4 Positive-time restart audit

Three exact networks were trained to \(t=0.4\), then exact and projected
systems were restarted from the identical current \(h,p,W,a\) state for
another \(0.8\) units:

| Restart quantity | \(K=1\) median (range) | \(K=2\) median (range) |
|---|---:|---:|
| Output error | \(2.46\times10^{-5}\) \((1.60\times10^{-5},6.03\times10^{-5})\) | \(5.68\times10^{-7}\) \((2.83\times10^{-7},3.24\times10^{-6})\) |
| Mid-depth Gram error | \(1.75\times10^{-4}\) \((4.38\times10^{-5},1.91\times10^{-4})\) | \(7.73\times10^{-6}\) \((2.39\times10^{-6},1.19\times10^{-5})\) |
| Terminal Gram error | \(2.48\times10^{-4}\) \((1.03\times10^{-4},8.04\times10^{-4})\) | \(2.75\times10^{-5}\) \((9.54\times10^{-6},5.10\times10^{-5})\) |

This supports locality of the finite-matrix response projection; it does not
establish restartability of the limiting PDE.

### 11.5 Independent nonlazy and stability checks

Exact-network ensembles, independent of either approximation, showed
\(O(1)\) terminal-Gram motion. The \(\pm\) values below are standard errors,
and the kernel column is the value at the final sampled time \(t=0.8\), not
the minimum over the trajectory:

| Width \(n\), \(L=16\) | Terminal Gram motion | Final \(\lambda_{\min}(\Theta)\) |
|---:|---:|---:|
| 32 | \(0.567\pm0.021\) | \(2.67\pm0.20\) |
| 64 | \(0.584\pm0.009\) | \(2.96\pm0.09\) |
| 96 | \(0.589\pm0.013\) | \(2.98\pm0.12\) |

Across every recorded checkpoint in eleven exact runs, including two
\(\sigma_w=1.2\) stress runs, the smallest tangent-kernel eigenvalue was
at least \(1.569\). In a \(t=4\) exact run, loss fell from \(0.721\) to
\(8.95\times10^{-11}\), while mid-depth and terminal Gram motions were
\(0.397\) and \(0.578\).

### 11.6 What the simulations do and do not show

They directly support nonlazy feature motion, sampled kernel coercivity, and
rapid decay of the **finite-network \(q/r\) response projection**. They do
not numerically implement \((\mathrm{PDE}\text{-}1,J_*,N)\), test the
homogenized finite-state compiler, estimate the full outgoing residual
(42), prove global coercivity on \(\mathcal U\), or justify interchange of
the width, depth, response, and infinite-time limits.

---

## 12. Adversarial audit and exact status

| Claim | Status |
|---|---|
| Dense residual architecture and Euclidean \(\mu\)P scaling | Exact |
| Finite-\((n,L)\) adjoint, parameter flow, and tangent kernel | Exact |
| Current row-law/Gram closure | False in general |
| Raw iid \(W_\ell\) converges to a smooth \(W(s)\) under \(1/L\) scaling | False |
| Ordered response hierarchy | Exact |
| Fixed-trajectory factorial Dyson tail | Proved |
| \(K=1,J=J_*\) is a certified standard-scale accuracy level | Not proved |
| Fixed-\(K,J\), fixed-grid width limit | Related conditioning precedent; unproved and not directly simulated here |
| Continuous-depth homogenized tagged PDE | Conjectural for this model |
| Global \(A=1\) tangent-kernel floor | Positive at sampled checkpoints; global floor unproved |
| Uniform finite-PDE convergence (38) | Central conjecture |
| Width-independent outgoing residual (42) | Semantic quantitative proof target |
| Uniform all-time finite-PDE approximation | The conjecture's direct content |

The following shortcuts are explicitly rejected.

- Replacing iid layers by a smooth Gaussian \(W(s)\).
- Using an orthogonal matrix manifold.
- Projected or activation-natural descent.
- Freezing \(B\), \(W\), or \(a\).
- A low-rank residual block.
- A scalar bias or skip capable of fitting alone.
- Initialization-time Taylor/Wick truncation.
- A loss-only Bernstein playback.
- A finite PDE whose real constants contain positive-time samples.
- A “closure” whose source dimension or coefficients grow with width.
- Calling the fixed-trajectory Dyson estimate a proof of the width-law
  residual.

---

## 13. Final conjecture in one paragraph

For the iid fully dense residual-tanh network (1)–(3), trained in every
parameter by the standard Euclidean \(\mu\)P flow (4), the width-then-depth
observable limit \((f,G^h,\Theta)\) exists for all training time. The
non-oracular compiler defined by the oriented grammar (26), finite response
grade \(K\), nonlinear complexity \(J\), and homogenized depth Galerkin
order \(N\) produces the autonomous Liouville PDE
\((\mathrm{PDE}\text{-}K,J,N)\). Along the fixed computable diagonal
\((K,J,N)=(\ell,\ell,\ell)\), its output, every depthwise hidden Gram, and its
positive-semidefinite tangent kernel converge uniformly over
\(\mathcal U\times[0,\infty)\) to those of the standard dense network, as
stated exactly in (38). The stronger Clause D additionally asserts
agreement with finite networks in the ordered, all-time sense (39).

The proposed quantitative proof mechanism is the semantic outgoing-residual
bound (42), with factorial chronological tail
\(\sum_{j>K}\Lambda^j/j!\), together with a prospective finite majorant
(43a). The rate, the majorant, and the uniform tangent-kernel floor are
intentionally not part of the core conjecture: disproving any one of them
would not resolve the PDE-existence question.

Subject to the finite-compilation contract (Compiler), Clauses A–C are a
direct strong, uniform, all-time finite-PDE existence statement for this
standard dense model; Clause D is the finite-network strengthening.
Refuting the core response-PDE conjecture requires failure of the fixed
diagonal family itself, not the failure of one favored proof bound. Neither
direction can be settled by a scalar curve fit, a hidden width-growing
state, an oracle-selected subsequence, or a change of optimizer or backbone.
