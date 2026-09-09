# Dense Euclidean continuous-depth \(\mu\)P

## The current finite-neural-PDE conjecture after the direct PDE experiment

**Date:** 23 July 2026  
**Scope:** standard fully dense residual-tanh network, ordinary Euclidean
\(\mu\)P gradient flow, fixed finite training set, width first and residual
depth second.

> **Later cutoff-audit note.** The \(P=5\to15\) interpretation in this dated
> report is superseded. Exact parity makes the added even-degree shell inert,
> so the recorded difference is cubature symmetry leakage rather than a
> physical hierarchy step. The correct ladder and current convergence status
> are in
> [`pde_convergence/03_bridgeability`](../../pde_convergence/03_bridgeability/)
> and
> [`pde_convergence/05_tail_and_compactness`](../../pde_convergence/05_tail_and_compactness/).

---

## Executive answer

Yes—the genuine-PDE experiment changed the conjecture in a meaningful way,
although it did not change the canonical network or the ultimate
accuracy-dependent existence claim.

Before the experiment, the strongest construction was a proposed
chronological response-word compiler. Its finite-network response algebra
and factorial depth-response bound were real, but the purported finite
Liouville compiler never emitted all of its tag tables, history
coordinates, conditional Gaussian kernel, and drift expressions. The
finite-matrix \(q/r\) simulations were therefore evidence for a compression
mechanism, not simulations of the claimed width-independent PDE.

The new experiment supplies the missing concrete object: an explicit
Hermite/isonormal **operator–Galerkin conditional Liouville PDE**. For every
finite Hermite degree it has:

- a completely displayed finite-dimensional source coordinate and finite
  field list;
- an explicit initialization and drift;
- no network width, original layer count, or \(n\times n\) matrix;
- the same coefficients for the forward operator and its transpose;
- an autonomous restart state;
- direct output and hidden-Gram readouts; and
- an exact projected Euclidean-gradient and positive-semidefinite tangent
  kernel identity.

At the first complete nonconstant level, \(P=5\), this literal PDE predicts
\(O(1)\) nonlazy feature motion and tracks the tested dense-network Gram
evolution to about \(1.14\%\) of that motion through the fitting transient.
The same fixed PDE then remains at its plateau through \(t=32\).

This is strong direct evidence for the central neural-PDE thesis. Later exact
parity analysis proved that \(P=5\) and \(P=15\) are the same physical PDE in
this model, so their recorded numerical difference is not cutoff evidence.
On the correct odd-degree ladder, later common-reference tests still did not
show aggregate contraction. Consequently:

\[
\boxed{\text{The experiment strongly supports a useful low-order finite PDE.}}
\]

\[
\boxed{\text{It does not establish arbitrary-accuracy Hermite convergence.}}
\]

The most accurate current formulation therefore has two logically distinct
parts:

1. the **project-level finite-PDE existence conjecture**, which quantifies
   over a tightly defined anti-oracular class of architecture-local finite
   Liouville compilers and is exactly the desired compression claim; and
2. the **operator–Galerkin conjecture**, which asserts that the explicit
   Hermite family written below is a witness to that project-level claim.

The second implies the first. Its failure would rule out this particular
compiler, not every possible response-enriched finite PDE.

---

## 1. Canonical dense model

### 1.1 Data and non-oracular parameter family

Fix a finite input dimension \(d\), a finite number \(m\) of training
samples, inputs \(x_1,\ldots,x_m\in\mathbb R^d\), and targets
\(y_1,\ldots,y_m\in\mathbb R\). Write

\[
X=[x_1\ \cdots\ x_m],\qquad y=(y_1,\ldots,y_m)^\top.
\]

The numerical laboratory used

\[
d=m=3,\qquad X=I_3,\qquad
y_*=(0.8,-0.55,0.35)^\top,
\]

\[
\sigma_w=0.65,\qquad A=1,\qquad \gamma=1.
\]

To rule out a PDE tailored to a single already-known curve, the
mathematical conjecture is uniform on the fixed compact neighborhood

\[
\mathcal U=
\left\{
(X,y,\sigma_w,A,\gamma):
\begin{array}{l}
\|X^\top X-I_3\|_{\mathrm{op}}\le 0.05,\\
\|y-y_*\|_2\le 0.05,\\
|\sigma_w-0.65|\le 0.05,\\
|A-1|\le 0.05,\\
|\gamma-1|\le 0.05
\end{array}
\right\}.
\tag{1}
\]

This near-orthogonal neighborhood is a concrete nontrivial laboratory, not
a claim that input nondegeneracy is fundamentally necessary for PDE
compression. A later theorem may enlarge \(\mathcal U\).

### 1.2 Finite width and residual depth

For width \(n\), residual depth \(L\), and \(\Delta=L^{-1}\), let

\[
h_r^0=Bx_r,\qquad z_r^\ell=W_\ell h_r^\ell,
\]

\[
\boxed{
h_r^{\ell+1}
=h_r^\ell+\frac{\gamma}{L}\tanh(z_r^\ell),
\qquad 0\le \ell<L,
}
\tag{2}
\]

\[
\boxed{
f_r=\frac1n a^\top h_r^L,\qquad
\mathcal L=\frac12\sum_{r=1}^m(f_r-y_r)^2.
}
\tag{3}
\]

Here

\[
B\in\mathbb R^{n\times d},\quad
W_\ell\in\mathbb R^{n\times n},\quad
a\in\mathbb R^n.
\]

Every \(W_\ell\) is fully dense and unconstrained. All of \(B\),
\(W_0,\ldots,W_{L-1}\), and \(a\) train. Initialization is independent:

\[
(W_\ell)_{ij}\sim N\!\left(0,\frac{\sigma_w^2}{n}\right),
\qquad B_{ij}\sim N(0,1),
\qquad a_i\sim N(0,A^2).
\tag{4}
\]

There is no orthogonality constraint, projected optimizer, activation-
natural metric, normalization layer, low-rank block, tied matrix, or frozen
parameter.

### 1.3 Ordinary Euclidean \(\mu\)P flow

With \(e=f-y\), the scalar Euclidean learning-rate multipliers are

\[
\boxed{
\eta_{W_\ell}=L,\qquad \eta_B=n,\qquad \eta_a=n.
}
\tag{5}
\]

Thus

\[
\dot W_\ell=-L\nabla_{W_\ell}\mathcal L,\qquad
\dot B=-n\nabla_B\mathcal L,\qquad
\dot a=-n\nabla_a\mathcal L.
\]

The factor \(L\) compensates for the \(L^{-1}\) residual branch and keeps
the \(W\)-induced feature update nonvanishing on \(O(1)\) training time. In
raw coordinates \(W=\widehat W/\sqrt n\), the equivalent multiplier for
\(\widehat W\) is \(nL\).

### 1.4 Exact adjoint, gradients, and tangent kernel

Define the unit-output adjoint

\[
p_r^L=a,\qquad
D_r^\ell=\operatorname{diag}\sech^2(z_r^\ell),\qquad
\beta_r^\ell=D_r^\ell p_r^{\ell+1}.
\]

Then

\[
p_r^\ell=
\left(I+\frac{\gamma}{L}W_\ell^\top D_r^\ell\right)
p_r^{\ell+1},
\tag{6}
\]

and the exact Euclidean \(\mu\)P flow is

\[
\boxed{
\dot W_\ell
=-\frac{\gamma}{n}\sum_qe_q\,
\beta_q^\ell(h_q^\ell)^\top,
}
\tag{7}
\]

\[
\boxed{
\dot a=-\sum_qe_qh_q^L,\qquad
\dot B=-\sum_qe_qp_q^0x_q^\top.
}
\tag{8}
\]

For \(G^{u,\ell}_{rq}=n^{-1}(u_r^\ell)^\top u_q^\ell\) and
\(Q^x_{rq}=x_r^\top x_q\),

\[
\boxed{\dot f=-\Theta^{n,L}e,}
\tag{9}
\]

\[
\boxed{
\Theta^{n,L}_{rq}
=G^{h,L}_{rq}
+Q^x_{rq}G^{p,0}_{rq}
+\frac{\gamma^2}{L}\sum_{\ell=0}^{L-1}
G^{h,\ell}_{rq}G^{\beta,\ell}_{rq}.
}
\tag{10}
\]

Every block is positive semidefinite, so

\[
\dot{\mathcal L}=-e^\top\Theta^{n,L}e\le0.
\tag{11}
\]

For every finite \(n,L\), the inverse-metric energy identity is

\[
-\dot{\mathcal L}
=\frac1n\|\dot a\|^2
+\frac1n\|\dot B\|_F^2
+\frac1L\sum_{\ell=0}^{L-1}\|\dot W_\ell\|_F^2.
\tag{12}
\]

It gives finite parameter travel on every finite time interval and hence
global finite-\((n,L)\) gradient flow.

---

## 2. The correct width/depth target

### 2.1 Why the raw matrices do not become a smooth neural ODE

The initialization matrices are iid across residual depth. Under \(1/L\)
residual scaling, their smooth depth modes average away, while nonlinear
statistics such as

\[
\mathbb E[\sech^2(Wh)]
\]

remain \(O(1)\). It is therefore incorrect to interpolate the raw
\(W_\ell\)'s and posit a smooth matrix field \(W(s)\).

The correct depth object is a fast Gaussian Young/cavity law coupled to
slow forward and backward fields. A numerical quadrature label reused at
several depth nodes is only a deterministic integration device; it is not a
physical tied noise path across depth.

### 2.2 Ordered limit

The target order is

\[
\boxed{
n\to\infty\ \text{at fixed }L,\qquad
L\to\infty\ \text{second}.
}
\tag{13}
\]

For a finite network define the core observable

\[
\mathcal O_{n,L}^\vartheta(t)
=
\left(
f_{n,L}^\vartheta(t),
G_{n,L}^{h,\vartheta}(\cdot,t)
\right),
\tag{14}
\]

where the finite-depth Gram is interpolated in \(s=\ell/L\).

The ordered target sought—whose existence is itself conjectural—is a
deterministic pair

\[
\mathcal O_\vartheta(t)
=
\left(f_\vartheta(t),G_\vartheta^h(\cdot,t)\right)
\tag{15}
\]

defined as a global continuous path in
\(\mathbb R^m\times C([0,1],\mathbb R^{m\times m})\), such that, for every
\(T<\infty\) and \(\delta>0\),

\[
\lim_{L\to\infty}\lim_{n\to\infty}
\Pr\!\left[
\sup_{0\le t\le T}
\left(
\|f_{n,L}^\vartheta(t)-f_\vartheta(t)\|_2
+
\sup_{s\in[0,1]}
\|G_{n,L}^{h,\vartheta}(s,t)-G_\vartheta^h(s,t)\|_F
\right)>\delta
\right]=0.
\tag{16}
\]

Existence of this ordered target for the fully trained dense model is
itself part of the conjecture.

Loss is already determined by \(f\). The tangent kernel is an important
additional readout, but it is not placed in the irreducible approximation
norm: a failure to approximate \(\Theta\) should not, by itself, refute
finite-PDE prediction of the requested output and Gram curves.

---

## 3. What counts as an accuracy-dependent finite neural PDE

A family is **admissible** only if it satisfies all of the following.

1. **Finite source-coordinate dimension and finite field count.** At
   approximation index \(k\), it is a continuity/Liouville PDE on a
   finite-dimensional source coordinate, coupled to only finitely many
   depth fields and auxiliary ODEs. Its law-valued state remains
   infinite-dimensional, as a PDE state should. Its source dimension and
   field count may depend on \(m,d,k\), but not on \(n\), original depth
   \(L\), or a requested time horizon.
2. **Architecture-local compilation.** A fixed finite program produces its
   drift, initialization, and readouts from (2)–(5), the activation,
   Gaussian initialization, the current finite moments, and the static
   model parameters. There are no free positive-time functions or
   uncomputed “DMFT operators.”
3. **No microscopic state.** No \(n\times n\) matrix, width-indexed vector,
   finite-network checkpoint, or source dimension growing with \(n\) is
   permitted.
4. **No trajectory oracle.** The compiler cannot read exact positive-time
   outputs, Grams, kernels, fitting times, raw trajectories, or fitted
   closure constants. One fixed family must work on all of \(\mathcal U\).
5. **Autonomy and restartability.** The current finite PDE state determines
   its future under the same equations. A hidden past-time integral or
   replay table is not part of the state.
6. **Fixed approximation family.** Its basis ordering and approximation
   indices are fixed before positive-time reference data are observed.
7. **Direct observables.** Outputs and hidden Grams are current moments of
   the PDE state, not separately fitted decoders.
8. **Correct depth semantics.** Any projection is applied after the width
   limit to the Gaussian operator/order parameters, never as a low-rank
   replacement of the finite dense architecture.

The compiler in item 2 is an effective finite expression-DAG program. Its
allowed primitives are:

- rational constants and the static entries of
  \((X,y,\sigma_w,A,\gamma)\);
- arithmetic, \(\tanh\), and its finitely requested derivatives;
- a declared polynomial/orthogonal basis fixed by the initialization law;
- finite-dimensional Gaussian expectations and conditional expectations;
- current moments from an emitted finite moment list;
- finite linear algebra whose dimensions are bounded by the approximation
  index; and
- the displayed finite depth boundary and transport operations.

Every non-rational constant must be generated from these static inputs and
declared operations to a prescribed computable precision. Arbitrary real
literals, calls to a finite or infinite dense-network solver, unevaluated
DMFT/graph-limit operators, external result files, and nested target
trajectory simulations are forbidden. The compiler emits the complete
source-coordinate list, moment list, drift DAG, initial law, boundary
equations, and readout DAG. These syntactic and provenance requirements are
what make the broader existential statement auditably anti-oracular.

For two observable paths define

\[
d_{\mathrm{obs}}(\mathcal O,\widetilde{\mathcal O})
=
\|f-\widetilde f\|_2
+
\sup_{s\in[0,1]}
\|G^h(s)-\widetilde G^h(s)\|_F.
\tag{17}
\]

The project-level statement is:

> **Finite-neural-PDE existence conjecture.**  
> The ordered target (15) exists, and there is one admissible,
> architecture-local family \(\{\mathsf P_k\}_{k\ge1}\) with unique global
> solutions from its compiled initial states and an autonomous semigroup on
> every reached state, such that
> \[
> \inf_{k\ge1}
> \sup_{\vartheta\in\mathcal U}
> \sup_{t\ge0}
> d_{\mathrm{obs}}
> \left(
> \mathcal O_\vartheta(t),
> \mathcal O_{\mathsf P_k,\vartheta}(t)
> \right)
> =0.
> \tag{18}
> \]

Equation (18) is exactly the non-effective, accuracy-dependent existence
claim: for every \(\varepsilon>0\), a finite, width/depth/horizon-independent
neural PDE in the predeclared family has all-time error below
\(\varepsilon\). A computable map \(\varepsilon\mapsto k\) and a certified
error bound are stronger, effective claims.

The restrictions above are part of the statement. Without them, (18) could
be satisfied by a trajectory playback, a universal ODE containing
precomputed answers in real constants, or a hidden width-growing state.

---

## 4. The explicit operator–Galerkin Liouville family

The experiment changes the conjecture most clearly here: this is now the
leading concrete compiler.

### 4.1 Immutable neuron type and fixed Hermite schedule

Let

\[
\theta=(b^0,\alpha^0)
=
\left(B_i(0),\frac{a_i(0)}A\right)
\sim\mu=N(0,I_{d+1})
\tag{19}
\]

be the immutable base-neuron label.

For total Hermite degree \(r\), take **all** normalized multivariate Hermite
functions

\[
\{\phi_\nu:|\nu|\le r\}\subset L^2(\mu).
\]

Their number is

\[
\boxed{
P_r=\binom{d+1+r}{r}.
}
\tag{20}
\]

For \(d=3\),

\[
P_1=5,\qquad P_2=15,\qquad P_3=35.
\]

This complete-degree ordering is fixed in advance. No basis rotation is fit
to dense-network trajectories.

### 4.2 Cylindrical dense-row projection

For a slow neuron field \(v(\theta)\), define

\[
\langle\phi_\nu,v\rangle_\mu
=\int\phi_\nu(\theta)v(\theta)\,d\mu(\theta).
\]

The degree-\(r\) action of one initial dense row is

\[
(W_r^0v)(\theta,\varepsilon)
=
\sigma_w\sum_{|\nu|\le r}
\varepsilon_\nu\langle\phi_\nu,v\rangle_\mu,
\qquad
\varepsilon\sim N(0,I_{P_r}).
\tag{21}
\]

For any two queried slow fields,

\[
\mathbb E_\varepsilon[(W_r^0v)(W_r^0v')]
=
\sigma_w^2
\langle\Pi_rv,\Pi_rv'\rangle_\mu.
\tag{22}
\]

This is the cylindrical projection used in the candidate post-width-limit
model; it has not been identified with the actual trained width limit. It is
not a rank-\(P_r\) finite network. Completeness is on finite query families;
the infinite iid Gaussian coefficient sequence is cylindrical and is not
claimed to be an \(\ell^2\)-valued operator.

### 4.3 Shared forward and transpose operator

Let \(w=(w_\nu)_{|\nu|\le r}\in\mathbb R^{P_r}\) denote the current total
row coefficient. Define

\[
(W_rv)(\theta,w)
=
\sum_{|\nu|\le r}w_\nu
\langle\phi_\nu,v\rangle_\mu.
\tag{23}
\]

For a fast test field \(\psi(\theta,w)\), define

\[
(W_r^\ast\psi)(\theta)
=
\sum_{|\nu|\le r}\phi_\nu(\theta)
\int\mu(d\theta')
\int w_\nu\psi(\theta',w)\,
\rho_{s,t}^{\theta'}(dw).
\tag{24}
\]

Then, exactly at every finite \(r\),

\[
\langle W_rv,\psi\rangle_{\mu\otimes\rho}
=
\langle v,W_r^\ast\psi\rangle_\mu.
\tag{25}
\]

Thus the backward operator cannot use an independent Gaussian copy. The
finite-\(r\) transpose pairing is exact. The corresponding elementary
Gaussian Stein/Onsager identity is exact at Gaussian initialization.
Identifying the projected shared-transpose term with the surviving trained
dense conditional Onsager mean is still a theorem gap.

### 4.4 Conditional Liouville PDE

For each depth \(s\in[0,1]\), time \(t\), and base type \(\theta\), let
\(\rho_{s,t}^{\theta}\) be a conditional law on
\(w\in\mathbb R^{P_r}\). Write

\[
H_{\nu q}(s,t)
=
\int\phi_\nu(\theta)h_q(s,\theta,t)\,d\mu(\theta),
\tag{26}
\]

\[
z_q(s,\theta,w,t)
=
\sum_{|\nu|\le r}w_\nu H_{\nu q}(s,t),
\tag{27}
\]

\[
\beta_q(s,\theta,w,t)
=
\sech^2(z_q(s,\theta,w,t))\,p_q(s,\theta,t).
\tag{28}
\]

The row-law characteristic velocity is

\[
\boxed{
V_\nu(s,\theta,w,t)
=
-\gamma\sum_{q=1}^m
e_q^{(r)}(t)\,\beta_q(s,\theta,w,t)H_{\nu q}(s,t).
}
\tag{29}
\]

where

\[
e^{(r)}(t)=f^{(r)}(t)-y.
\tag{29a}
\]

The finite-\(P_r\) neural PDE is

\[
\boxed{
\partial_t\rho_{s,t}^{\theta}
+
\nabla_w\cdot
\left(\rho_{s,t}^{\theta}V\right)
=0.
}
\tag{30}
\]

It is coupled to the forward depth equation

\[
\boxed{
\partial_sh_q(s,\theta,t)
=
\gamma\int
\tanh(z_q(s,\theta,w,t))
\rho_{s,t}^{\theta}(dw),
}
\tag{31}
\]

\[
h_q(0,\theta,t)=b(\theta,t)^\top x_q,
\tag{32}
\]

and the shared-transpose adjoint equation

\[
\boxed{
-\partial_sp_q(s,\theta,t)
=
\gamma\sum_{|\nu|\le r}\phi_\nu(\theta)
\int\mu(d\theta')
\int w_\nu\beta_q(s,\theta',w,t)
\rho_{s,t}^{\theta'}(dw),
}
\tag{33}
\]

\[
p_q(1,\theta,t)=a(\theta,t).
\tag{34}
\]

The trained input and output fields obey

\[
\boxed{
\dot b(\theta,t)
=-\sum_qe_q^{(r)}(t)p_q(0,\theta,t)x_q,
}
\tag{35}
\]

\[
\boxed{
\dot a(\theta,t)
=-\sum_qe_q^{(r)}(t)h_q(1,\theta,t).
}
\tag{36}
\]

Initialization is completely specified:

\[
b(\theta,0)=b^0,\qquad
a(\theta,0)=A\alpha^0,
\tag{37}
\]

\[
\boxed{
\rho_{s,0}^{\theta}
=N(0,\sigma_w^2I_{P_r}),
}
\tag{38}
\]

with the same marginal law for every \(s,\theta\). At finite residual depth,
the layer matrices are independent across the discrete depth slots; the
Young-measure PDE records their local marginal rather than an independence
relation over an uncountable \(s\)-domain.

The readouts are current moments:

\[
\boxed{
f_q^{(r)}(t)
=
\int a(\theta,t)h_q(1,\theta,t)\,d\mu(\theta),
}
\tag{39}
\]

\[
\boxed{
G_{qk}^{h,(r)}(s,t)
=
\int h_q(s,\theta,t)h_k(s,\theta,t)\,d\mu(\theta).
}
\tag{40}
\]

The complete current state is

\[
\left(
b(\cdot,t),a(\cdot,t),
\{\rho_{s,t}^{\theta}\}_{s,\theta}
\right).
\]

The forward and adjoint fields are recomputed from that state by
(31)–(34). No past trajectory is needed, so the displayed equation is
structurally autonomous and restartable whenever its boundary-value problem
and transport flow are well posed.

For fixed \(r\), the conditional phase coordinate \((\theta,w)\) has
dimension \(d+1+P_r\). Including physical depth, the full PDE source
\((s,\theta,w)\) has dimension \(d+2+P_r\), and there are finitely many
coupled fields. These dimensions are independent of \(n\), \(L\), and
training horizon. Numerical depth nodes \(N\), base cubature points \(M\),
fast cubature points \(R\), and time step are solver resolutions of
(30)–(38), not additional network or closure dimensions.

### 4.5 Exact finite-\(P_r\) gradient identity

Define

\[
G^h_{qk}(s)
=\int h_q(s,\theta)h_k(s,\theta)\,d\mu(\theta),
\]

\[
G^p_{qk}(0)
=\int p_q(0,\theta)p_k(0,\theta)\,d\mu(\theta),
\]

\[
G^\beta_{qk}(s)
=
\int\mu(d\theta)\int
\beta_q(s,\theta,w)\beta_k(s,\theta,w)
\rho_s^\theta(dw),
\]

\[
G^{h,r}_{qk}(s)
=
\sum_{|\nu|\le r}H_{\nu q}(s)H_{\nu k}(s).
\]

Then the finite PDE obeys the exact same-system identity

\[
\boxed{
\dot f^{(r)}=-\Theta_r e^{(r)},
}
\tag{41}
\]

\[
\boxed{
(\Theta_r)_{qk}
=
G^h_{qk}(1)
+(x_q^\top x_k)G^p_{qk}(0)
+\gamma^2\int_0^1
G^{h,r}_{qk}(s)G^\beta_{qk}(s)\,ds.
}
\tag{42}
\]

Every block is positive semidefinite. Hence

\[
\dot{\mathcal L}_r
=-(e^{(r)})^\top\Theta_re^{(r)}
\le0.
\tag{43}
\]

At finite \(r\), the backbone block must use the projected Gram
\(G^{h,r}\), not the full \(G^h\). This identity proves that the finite PDE
is a projected Euclidean gradient system; it does not prove that it is the
dense-model limit.

---

## 5. The current sharp operator–Galerkin conjecture

Let

\[
E_r
:=
\sup_{\vartheta\in\mathcal U}
\sup_{t\ge0}
\left[
\|f_\vartheta^{(r)}(t)-f_\vartheta(t)\|_2
+
\sup_{s\in[0,1]}
\|G_\vartheta^{h,(r)}(s,t)-G_\vartheta^h(s,t)\|_F
\right].
\tag{44}
\]

Set \(E_r=\infty\) if either the ordered target does not exist or the
degree-\(r\) PDE lacks a unique global solution from its compiled
initialization.

> **Sharp operator–Liouville approximation conjecture.**
> \[
> \boxed{\inf_{r\ge1}E_r=0.}
> \tag{45}
> \]

Equation (45) is exactly equivalent to accuracy-dependent finite-PDE
existence **inside this predeclared operator–Galerkin family**:
for every \(\varepsilon>0\), some completely displayed finite
operator–Liouville PDE has uniform all-time output/Gram error at most
\(\varepsilon\).

By design, (45) permits a nonmonotone sequence of successful degrees. The
family and every degree are fixed in advance, but this non-effective
existence statement does not itself supply a computable degree selector.

The natural canonical Galerkin strengthening is

\[
\boxed{\lim_{r\to\infty}E_r=0.}
\tag{46}
\]

This says every sufficiently high complete Hermite degree works; it allows
nonmonotone low-order errors but forbids an oracle-selected subsequence.
Equation (46) is the cleanest convergence theorem to seek, but it is
strictly stronger than the irreducible accuracy-dependent existence claim
(45), and the present operator-order experiment does not positively support
its asymptotic direction.

Further strengthenings, deliberately excluded from the truth-value of
(45), include:

- a computable degree \(r(\varepsilon)\);
- an a posteriori residual certificate;
- uniform approximation of a full neighborhood of restarted dense states;
- convergence of \(\Theta_r\);
- a specified factorial or spectral rate; and
- a uniform positive lower bound on \(\Theta_r\).

Failure of any one proposed proof device would not refute (45).

Finally, (45) is sufficient but not logically necessary for the broader
project-level statement (18). If the static label \(\theta\) omits a
surviving trained fast-history variable, a response-enriched finite PDE
could satisfy (18) even though the pure Hermite family fails. This logical
qualification is essential.

---

## 6. The theoretical case for the conjecture

### 6.1 The projected row dynamics are exactly the Euclidean gradient

At finite width, define the empirical projected row coefficient and hidden
coefficient exactly by

\[
w_{\ell i,\nu}^{n}
:=
\sum_{j=1}^nW_{\ell,ij}\phi_\nu(\theta_j)
=
\frac1{\sqrt n}\sum_{j=1}^n
\widehat W_{\ell,ij}\phi_\nu(\theta_j),
\qquad W_\ell=\widehat W_\ell/\sqrt n,
\tag{47a}
\]

\[
H_{\nu q}^{n,\ell}
:=
\frac1n\sum_{j=1}^n
\phi_\nu(\theta_j)h_{q,j}^\ell.
\tag{47b}
\]

Because the immutable \(\theta_j\)'s do not train, equation (7) gives the
exact finite-width identity

\[
\dot w_{\ell i,\nu}^{n}
=
-\gamma\sum_qe_q\,
\beta_{q,i}^\ell H_{\nu q}^{n,\ell}.
\tag{47}
\]

Once the fixed-\(L\) width law and the relevant empirical convergence are
established, (47) formally yields (29). There is no missing width factor or
residual-depth factor. Thus the candidate Liouville velocity is the direct
projected ordinary Euclidean \(\mu\)P gradient, not a fitted curve law; its
identification as the canonical dense limiting velocity remains
conjectural.

### 6.2 Hermite completeness is the canonical cylindrical approximation

The normalized Hermites form a complete orthonormal basis of
\(L^2(\mu)\). Therefore, for every fixed finite collection of square-
integrable slow queries,

\[
\langle\Pi_rv,\Pi_rv'\rangle_\mu
\longrightarrow
\langle v,v'\rangle_\mu.
\tag{48}
\]

Through (22), the finite Gaussian row covariances converge on those query
families. This gives a natural finite approximation axis that is tied to
the initialization law rather than to an empirically chosen low-rank
network.

What remains nontrivial is uniform control of the evolving query family and
of high-to-low feedback. Parseval convergence on fixed queries is not
operator-norm convergence of an infinite Gaussian matrix.

### 6.3 Shared transpose removes a fatal independence error

Dense learning repeatedly reuses \(W\) and \(W^\top\). Treating the backward
action as independent Gaussian noise destroys its conditional/Onsager
component. Equations (23)–(25) use the same \(w_\nu\)'s and preserve the
exact finite-\(r\) pairing. This is the correct algebraic structure for a
candidate dense closure.

The missing theorem must show that, after the ordered width/depth limit,
the centered column-cavity innovation averages away while the shared
conditional mean retained by (24) survives.

### 6.4 Continuous residual depth suppresses centered fast noise

Each residual slice contributes \(1/L\). If centered fast innovations are
approximately independent across depth, their accumulated variance is

\[
L\left(\frac1L\right)^2=O(L^{-1}),
\]

so their RMS size is \(O(L^{-1/2})\). Conditional means and learned coherent
components can remain \(O(1)\).

This is the homogenization mechanism behind (30)–(33). The difficult part
is showing that training-induced global feedback does not create
cross-depth correlations large enough to defeat the cancellation.

### 6.5 Exact chronological response gives a separate accuracy mechanism

At finite \(n,L\), differentiating the forward recurrence gives

\[
v_r^{\ell+1}
=
\left(I+\frac1L A_r^\ell\right)v_r^\ell
+\frac1L F_r^\ell,
\qquad
A_r^\ell=\gamma D_r^\ell W_\ell.
\tag{49}
\]

The ordered continuation with \(k\) dense Jacobian actions has a
simplex-volume factor. If

\[
\Lambda_T
=
\sup_{r,t\le T}
\frac1L\sum_{\ell=0}^{L-1}\|A_r^\ell(t)\|_{\mathrm{op}}
<\infty,
\]

use the normalized neuron norm
\(\|u\|_n=n^{-1/2}\|u\|_2\), and set

\[
B_T
:=
\sup_{r,t\le T}
\left(
\|v_r^0(t)\|_n
+
\frac1L\sum_{\ell=0}^{L-1}\|F_r^\ell(t)\|_n
\right).
\]

then the pure propagator tail satisfies the exact prelimit estimate

\[
\sup_{r,\ell,t\le T}
\left\|
v_r^\ell-\sum_{k=0}^Kv_r^{[k],\ell}
\right\|_n
\le
B_T
\sum_{j>K}\frac{\Lambda_T^j}{j!}
\le
B_Te^{\Lambda_T}
\frac{\Lambda_T^{K+1}}{(K+1)!}.
\tag{50}
\]

This is a real-axis Volterra/Dyson expansion in residual depth, not a
Taylor series in training time. The backward hierarchy has the same bound
when its differentiated source is exact. A coupled truncation has an
additional source-error term, so (50) alone is not a proof of full closure.

The response result remains valuable after the new experiment: it supplies
a plausible causal stability mechanism and a principled fallback set of
extra coordinates if the static Hermite label is insufficient. It is no
longer presented as an already emitted finite PDE.

### 6.6 Bounded activation and dissipative loss remove earlier pathologies

The earlier quadratic/Gaussian examples in this project had unbounded
polynomial feedback, extreme-neuron tails, and zero-radius training-time
Wick–Taylor expansions. Here \(\tanh\) and each fixed collection of its
real-axis derivatives are bounded, while the depth response is a Volterra
expansion.

In addition, (11) and (43) make both the exact network and every finite
operator PDE dissipative. If one can prove an integrable residual,
eventual kernel coercivity, or another all-time stability estimate, a
finite-time closure may extend through the plateau without increasing its
state dimension.

Neither bounded \(\tanh\) nor monotone loss alone proves uniform Hermite
tails or a global kernel floor. Those remain proof obligations, not hidden
assumptions.

---

## 7. Empirical evidence

No new experiment was run for this report. All numbers below come from the
already frozen genuine-PDE, dense-reference, response-hierarchy, and audit
artifacts.

### 7.1 The literal PDE gates passed

The implemented degree-one system is a genuine PDE rather than a relabeled
finite network:

- its mathematical state has no width \(n\), original layer count \(L\),
  or two-neuron-index weight matrix;
- its drift does not import or read dense-reference trajectories;
- shared \(W_r/W_r^\ast\) pairing holds to roundoff;
- coordinate-gradient and energy identities pass finite-difference tests;
- \(\dot f^{(r)}=-\Theta_re^{(r)}\) holds to numerical precision and
  \(\Theta_r\succeq0\);
- direct and split/restarted integration agree to roundoff;
- changed targets alter the positive-time drift only through the current
  residual;
- wrong-seed, same-shape restart states are rejected by the static
  compiler/cubature identity; and
- two independently written characteristic implementations agree to
  numerical precision when given the same deterministic cubature.

The numerical characteristic count can be large because it approximates
integrals over \((\theta,w)\). That is solver resolution, not a hidden dense
matrix or physical network width.

These dense/PDE comparisons concentrate on the central parameter point.
The changed-target continuation is an internal autonomy test; it is not a
dense/PDE validation uniformly over the full neighborhood \(\mathcal U\).

### 7.2 Direct PDE versus dense-network curves

The primary PDE used

\[
r=1,\quad P=5,\quad N=16,\quad M=256,\quad R=128.
\]

Against the pooled \(n=256,L=32\), 128-seed dense reference:

| Quantity | Observed value |
|---|---:|
| PDE feature motion | \(0.633801\) |
| Dense feature motion | \(0.639909\) |
| Maximum output gap | \(1.0753\times10^{-2}\) |
| Maximum loss-of-ensemble-mean gap | \(1.8457\times10^{-3}\) |
| Maximum absolute Gram gap | \(1.9408\times10^{-2}\) |
| Maximum Gram-increment surface gap | \(7.2433\times10^{-3}\) |
| Gram-increment gap / PDE feature motion | \(1.1428\%\) |

The increment comparison subtracts each system's own initialization and is
the cleanest finite-width measure of learned feature evolution. The
mathematical conjecture nevertheless concerns the absolute ordered-limit
Grams; initialization subtraction is not built into its target.

The \(7.2433\times10^{-3}\) finite-reference discrepancy is statistically
resolved for this 128-seed reference
(\(p\approx0.0030\) under the pooled curvewise bootstrap). The correct
description is **close but distinguishable**, not “indistinguishable” or
“below the noise floor.”

### 7.3 Width and residual-depth diagnostics

At \(L=32\), the \(P=5\) Gram-increment gaps were

| Width / ensemble | Gap |
|---|---:|
| \(n=64,\ S=64\) | \(2.464\times10^{-2}\) |
| \(n=128,\ S=96\) | \(9.255\times10^{-3}\) |
| \(n=256,\ S=128\) | \(7.243\times10^{-3}\) |
| \(n=512,\ S=16\) | \(9.897\times10^{-3}\) |

The decrease through \(n=256\) is encouraging. The smaller \(n=512\)
ensemble is sampling-limited and does not continue a monotone curvewise
trend.

The preregistered exact-network Cauchy diagnostics were

\[
\|\Delta G_{256,32}-\Delta G_{512,32}\|_{\infty}
=9.350\times10^{-3},
\]

\[
\|\Delta G_{256,32}-\Delta G_{256,64}\|_{\infty}
=4.226\times10^{-3}.
\]

Neither Cauchy gap was statistically resolved at the predeclared 5% rule.
This is useful finite-grid stability evidence, especially in depth, but it
does not identify the ordered limit.

### 7.4 The PDE predicts a genuine plateau, not a local Taylor segment

The primary PDE was integrated through the active transient to \(t=8\),
serialized, and continued by the same autonomous equations to \(t=32\).
Over \(8\le t\le32\):

| Plateau quantity | Maximum |
|---|---:|
| output drift from \(t=8\) | \(4.996\times10^{-13}\) |
| all-depth Gram drift | \(4.236\times10^{-13}\) |
| tangent-kernel drift | \(4.168\times10^{-13}\) |
| residual norm | \(4.996\times10^{-13}\) |
| \(|\dot{\mathcal L}|\) | \(8.253\times10^{-25}\) |

Thus the PDE success is not a short-time Taylor fit. Dense references were
compared directly only through \(t=8\), where they were already operationally
flat. This supports global-through-plateau prediction in the simulated
regime, not a theorem of uniform accuracy on \([0,\infty)\).

### 7.5 Numerical resolution of the PDE

The main relevant solver errors were:

| Refinement | Output difference | All-depth Gram difference |
|---|---:|---:|
| RK4 \(dt=.02\) vs. \(.01\) | \(6.83\times10^{-8}\) | \(1.09\times10^{-7}\) |
| \(N=16\) vs. \(N=32\) | \(2.05\times10^{-4}\) | \(8.45\times10^{-4}\) |
| \(M=512,R=128\) vs. primary | \(1.53\times10^{-4}\) | \(7.83\times10^{-4}\) |
| \(M=256,R=256\) vs. primary | \(1.12\times10^{-4}\) | \(1.16\times10^{-3}\) |

Independent QMC scrambles had pairwise all-depth Gram spread about
\(2.1\times10^{-3}\). Time integration is negligible at the observed
dense/PDE gap scale; depth and cubature errors are smaller but not entirely
negligible.

### 7.6 Direct evidence for depth homogenization

Paired dense runs shared \(B(0)\) and \(a(0)\) but independently redrew all
\(W_\ell\). Across \(L=8,16,32,64\), the fitted log–log slopes of conditional
variance were

| Field | initialization | after training to \(t=0.5\) |
|---|---:|---:|
| hidden field | \(-1.0193\) | \(-1.0039\) |
| input adjoint | \(-0.9993\) | \(-0.9924\) |

Variance therefore scales almost exactly as \(1/L\), or RMS
\(L^{-1/2}\), before and after learning begins. This is well-targeted
evidence for the homogenization step. It is not a trained propagation-of-
chaos proof.

### 7.7 Earlier response-hierarchy evidence

The corrected finite-matrix \(q/r\) hierarchy retains every dense
\(W_\ell\), so it is not the finite PDE. It nevertheless gives independent
evidence that causal training response is compressible. Across 16
long-horizon runs:

| Response grade | Output error, median / max | All-depth Gram error, median / max |
|---:|---:|---:|
| \(K=0\) | \(8.51\times10^{-3}/1.58\times10^{-2}\) | \(2.50\times10^{-2}/5.19\times10^{-2}\) |
| \(K=1\) | \(2.38\times10^{-4}/1.40\times10^{-3}\) | \(1.88\times10^{-3}/3.62\times10^{-3}\) |
| \(K=2\) | \(1.42\times10^{-5}/5.71\times10^{-5}\) | \(1.18\times10^{-4}/5.52\times10^{-4}\) |
| \(K=3\) | \(9.77\times10^{-7}/6.25\times10^{-6}\) | \(6.08\times10^{-6}/5.93\times10^{-5}\) |

All exact and fixed-\(K\) trajectories passed the operational plateau test
through \(t=32\), and no new prefix error maximum appeared after \(t=16\).
This strongly supports bounded chronological response, while leaving the
width-independent closure theorem open.

### 7.8 Superseded even-shell comparison and current interpretation

The following historical measurements are reproducible numerical outputs, but
they do not compare successive physical cutoffs:

| PDE level | Gram-increment gap to \(n=256,L=32,S=128\) | Fraction of PDE feature motion |
|---|---:|---:|
| refined QMC \(P=5\) | \(7.243\times10^{-3}\) | \(1.143\%\) |
| refined QMC \(P=15\) | \(9.202\times10^{-3}\) | \(1.457\%\) |
| hybrid \(P=15,R=256\) | \(9.223\times10^{-3}\) | \(1.460\%\) |
| hybrid \(P=35,R=128\) stress | \(1.373\times10^{-2}\) | \(2.192\%\) |

Exact sign equivariance makes every even Hermite shell dynamically inert, so
\(P=5\) and \(P=15\) are the same exact PDE. Their nonzero numerical
difference came from unpaired cubature symmetry leakage. The \(P=35\) stress
point also lacked the resolution needed for a clean hierarchy conclusion.
The later parity-correct common-reference study replaces this comparison: it
finds small observables but no contraction of the aggregate state or
observable Cauchy gaps at the last tested rung. Thus arbitrary-accuracy
\(P\to\infty\) convergence remains open; neither this table nor the corrected
finite experiment proves convergence or divergence.

---

## 8. Exactly what the experiment changed

| Issue | Before the genuine-PDE run | Current best view |
|---|---|---|
| Canonical network | Dense residual-tanh, Euclidean \(\mu\)P | Unchanged |
| Ordered target | \(n\to\infty\), then \(L\to\infty\) | Unchanged |
| Concrete finite compiler | Proposed \(K/J/N\) response grammar with un-emitted tables | Explicit complete-degree operator–Liouville PDE |
| Role of response words | Claimed finite-PDE state | Auxiliary causal bound and possible enrichment |
| Numerical evidence | Finite matrices retained | Literal width-independent PDE integrated |
| Global-time evidence | Fixed-\(K\) matrix surrogate through plateau | Same fixed PDE itself through plateau |
| Arbitrary-accuracy evidence | Rapid \(K\)-decay suggested it | Still open; the old \(P=5\to15\) comparison is parity-confounded, and corrected aggregate tests do not contract |
| Main theorem gap | Full outgoing response residual | Trained depth homogenization plus Hermite/high-to-low control |

The earlier claim that the \(K/J/N\) note already defined an executable
compiler should be retired. Its exact finite-network algebra and Dyson
bound remain valid where stated, but unspecified tag/history tables and
conditional kernels cannot be treated as generated code.

The experiment therefore has an asymmetric effect:

- it **substantially raises confidence** that a scientifically useful,
  non-oracular finite neural PDE exists; but
- it **does not raise comparable confidence** in arbitrary-accuracy
  convergence of the simplest pure Hermite hierarchy.

---

## 9. Remaining mathematical obligations

A proof of the operator–Galerkin conjecture still needs four core
ingredients, followed by an optional effective/restart strengthening.

### 9.1 Ordered dense-limit existence

Prove deterministic width convergence at each fixed \(L\), then a
continuous residual-depth limit for the trained observable path, uniformly
on compact training intervals and in the depthwise Gram topology.

### 9.2 Trained iid-depth homogenization

Separate each reused row/column action into:

- the conditional shared-transpose/Onsager mean retained by (24); and
- a centered innovation.

Then prove the centered part accumulates as \(O(L^{-1/2})\), uniformly on
the relevant trained trajectory. The observed variance slopes are exactly
the diagnostic this theorem predicts.

### 9.3 Sufficiency of the base type and Hermite tail control

Show that the immutable label

\[
\theta=(B_i(0),a_i(0)/A)
\]

and the conditional row-coefficient law retain every slow variable that
survives homogenization. Establish tightness and uniform integrability of
the evolving cylindrical projections, and control contractions in which
discarded high modes feed back into low observables.

If this fails, the likely repair is not a return to a dense matrix but a
finite set of oriented response/history coordinates. That repair could
prove the broader project conjecture (18), but it would mean the pure
operator-family conjectures (45)–(46) are false.

### 9.4 All-time stability

Upgrade finite-time approximation to

\[
\sup_{t\ge0}d_{\mathrm{obs}}<\varepsilon.
\]

Promising mechanisms are loss dissipation, integrable residual arclength,
eventual contraction, and the factorial causal response bound. A global
kernel floor is sufficient but should not be assumed as part of the
conjecture.

### 9.5 Optional strengthening: robust restart and a residual certificate

The finite PDE is structurally restartable from its own state. A stronger
theorem should show that the same finite state approximates nearby positive-
time dense restarts over a uniform tube and should bound every omitted
Hermite/response contribution by a finite, computable residual. Neither
property has yet been proved, and neither is a clause of (45).

---

## 10. Proposed proof order

The most economical route is:

1. Prove the full fixed-\(L\) causal/DMFT width limit and the exact
   cylindrical coefficient identities. Do not close it to the
   operator–Liouville PDE yet: the centered column innovation survives at
   fixed \(L\).
2. Prove trained depth homogenization, retaining the conditional transpose
   mean and suppressing centered fast innovations.
3. Establish finite-time stability of the operator–Liouville flow under
   cylindrical Hermite truncation.
4. Combine Parseval convergence with explicit high-to-low contraction
   estimates. If the static type is not closed, branch to a
   response-enriched compiler; that branch targets (18), not the pure
   statements (45)–(46).
5. Use dissipation and tail arclength to extend compact-time convergence
   uniformly through \(t=\infty\).

This route keeps the exact architecture and optimizer fixed. It does not
need orthogonal weights, a specially chosen metric, or a low-rank residual
block.

---

## 11. Final status

The following statements are now exact or directly verified:

- the dense model, \(\mu\)P scaling, gradients, and finite-network tangent
  kernel;
- the fully specified finite-\(P_r\) candidate equations and their exact
  internal identities;
- their shared transpose and projected Euclidean-gradient structure;
- their autonomy at the level of the displayed current state;
- successful numerical integration of a literal finite-cutoff PDE with no
  network-width coordinate;
- \(O(1)\) nonlazy feature motion and close dense-curve agreement at
  \(P=5\);
- operational plateau behavior of the simulated PDE through \(t=32\); and
- finite-network factorial control of pure ordered depth-response tails
  under an operator envelope.

The following remain conjectural:

- existence of the canonical ordered trained dense limit for all time;
- identification of the operator PDE with that limit;
- sufficiency of the static neuron label;
- trained depth homogenization with the correct Onsager mean;
- arbitrary-accuracy Hermite or response-enriched closure; and
- uniform all-time and restart-neighborhood error bounds.

The most defensible final conclusion is therefore:

\[
\boxed{
\begin{array}{l}
\textbf{Direct evidence: }
\text{a finite-cutoff candidate neural PDE closely matches the tested dense}\\
\text{feature-learning transient and operational plateau through }t=8,\\
\text{and the same PDE independently remains flat through }t=32;\\[1mm]
\textbf{Best concrete conjecture: }
\inf_r E_r=0\text{ for the explicit complete-degree}\\
\text{operator–Liouville family;}\\[1mm]
\textbf{Open theorem: }
\text{ordered dense-limit identification and arbitrary accuracy.}
\end{array}
}
\]

This is a meaningful strengthening of the project’s evidentiary position,
but not a resolution of the conjecture. The direct PDE experiment makes the
central thesis substantially more credible; the parity-correct aggregate
noncontraction makes the remaining mathematical question sharper and
prevents overstatement.

---

## Reproducibility map

The compact source bundle accompanying this report contains:

- the operator–Galerkin PDE and exact dense-reference source;
- both unit-test suites and the independent characteristic
  implementation;
- the frozen protocol and full regeneration script;
- compact processed CSV/JSON evidence;
- the two central figures;
- the statistical and hostile audit code and reports; and
- exact environment and source-integrity metadata.

The large raw numerical arrays are deliberately omitted. The full protocol
regenerates them locally before running the raw-evidence verifier.
