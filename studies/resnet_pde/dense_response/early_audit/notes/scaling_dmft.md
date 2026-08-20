# Scaling and causal-DMFT audit for the canonical dense Euclidean continuous-depth \(\mu\)P model

## Executive verdict

There are two distinct conclusions.

1. **The proposed learning-rate multipliers are correct for the stated
   parameterization**:
   \[
   \eta_B=n,\qquad \eta_a=n,\qquad \eta_{W_\ell}=L.
   \]
   With the loss \(\frac12\sum_r(f_r-y_r)^2\), there is no additional factor
   \(2\).  In particular, the hidden-matrix rate is \(L\), not \(nL\), \(L/n\),
   or \(1\).  The resulting learned change of an individual dense hidden
   weight is \(O(n^{-1})\), while its coherent rank-\(m\) action is \(O(1)\).

2. **The architecture and the requested classical neural-ODE initialization
   are not simultaneously well specified.**  If \(W_0,\ldots,W_{L-1}\) are
   independent Gaussian matrices as \(L\to\infty\), their piecewise-constant
   interpolation does not converge to an ordinary depth-regular matrix field
   \(W(s,0)\).  It converges, at best, weakly/through a Young measure or a
   homogenized depth law.  A classical equation
   \[
   \partial_s h=\phi(W(s,t)h)
   \]
   with a realized matrix-valued control requires depth-coherent
   initialization (for example, sampling a continuous Gaussian matrix
   process and discretizing it), which abandons independence across layers.
   Keeping iid layers instead leads naturally to a width-first DMFT followed
   by a rapid-depth-disorder/homogenization limit, not to the displayed
   matrix-field neural ODE.

For fixed \(L\), eliminating each trained dense matrix gives exact two-training-
time overlap identities.  The corresponding infinite-width causal
description is formally a path-space DMFT with forward and backward Gaussian
cavity fields, two-time covariance kernels, and two causal functional-response
kernels.  Reuse of \(W_\ell^0\) in both \(W_\ell h\) and
\(W_\ell^\top\beta\) produces reciprocal Onsager terms.  A one-time law of
\((h,q,\beta)\), the depthwise Grams, or even the fixed-time depth propagator
\(J(s,u,t)\) is not the full exact state.

The finite-\((n,L)\) algebra below is exact.  The continuum equations are exact
conditional on a convergent depth interpolation.  The positive-time
infinite-width DMFT and its global/restartable well-posedness are formal
without an additional theorem; none of the five supplied project records
proves that theorem.

---

## 1. Locked finite-\((n,L)\) model

Fix \(m,d,n,L\).  For sample \(r\in\{1,\ldots,m\}\), put
\[
u_r=Bx_r,\qquad h_r^0=\chi(u_r),
\]
\[
z_r^\ell=W_\ell h_r^\ell,\qquad
h_r^{\ell+1}=h_r^\ell+\frac1L\phi(z_r^\ell),
\quad 0\le \ell<L,
\]
\[
f_r=\frac1n a^\top h_r^L,\qquad
e_r=f_r-y_r,
\]
\[
\mathcal L=\frac12\sum_{r=1}^m e_r^2.
\]
The nonlinearities act coordinatewise.  The canonical bounded choice is
\(\chi=\phi=\tanh\).

Initialization is
\[
B_{ij}\stackrel{\rm iid}{\sim}N(0,d^{-1}),\qquad
(W_{\ell,ij})\stackrel{\rm iid}{\sim}N(0,n^{-1}),\qquad
a_i\stackrel{\rm iid}{\sim}N(0,1),
\]
with all parameter groups and, as written in the question, all layers
independent.

At initialization, coordinates of \(h,z,a\) are \(O(1)\), their vector norms
are \(O(\sqrt n)\), and \(f_r=O_{\mathbb P}(n^{-1/2})\), hence \(f_r\to0\) for
fixed \(m,L\).

### 1.1 Unit-output adjoint versus raw adjoint

Define the **unit-output adjoint**
\[
q_r^\ell:=n\,\frac{\partial f_r}{\partial h_r^\ell}.
\]
Then
\[
q_r^L=a
\]
and, with
\[
D_r^\ell:=\operatorname{diag}\phi'(z_r^\ell),
\qquad
\beta_r^\ell:=D_r^\ell q_r^{\ell+1},
\]
the exact backward recurrence is
\[
\boxed{
q_r^\ell=
\left(I+\frac1L W_\ell^\top D_r^\ell\right)q_r^{\ell+1}
=q_r^{\ell+1}+\frac1L W_\ell^\top\beta_r^\ell.
}
\tag{1}
\]
For the input block define
\[
\gamma_r:=\operatorname{diag}\chi'(u_r)\,q_r^0.
\tag{2}
\]

The **raw output adjoint**
\[
p_r^\ell:=\frac{\partial f_r}{\partial h_r^\ell}
\]
satisfies \(p_r^\ell=q_r^\ell/n\), so its terminal condition is
\[
p_r^L=\frac an.
\]
Confusing these two conventions is the main way an erroneous extra factor
\(n\) enters the hidden-weight flow.  A loss adjoint for sample \(r\) is
simply \(e_rp_r^\ell\).

### 1.2 Exact parameter gradients

Direct differentiation gives
\[
\boxed{
\frac{\partial f_r}{\partial a}=\frac1n h_r^L,
}
\tag{3}
\]
\[
\boxed{
\frac{\partial f_r}{\partial W_\ell}
=\frac1{nL}\,\beta_r^\ell(h_r^\ell)^\top,
}
\tag{4}
\]
\[
\boxed{
\frac{\partial f_r}{\partial B}
=\frac1n\,\gamma_r x_r^\top.
}
\tag{5}
\]
Therefore
\[
\nabla_a\mathcal L=\frac1n\sum_r e_r h_r^L,
\]
\[
\nabla_{W_\ell}\mathcal L
=\frac1{nL}\sum_r e_r\beta_r^\ell(h_r^\ell)^\top,
\]
\[
\nabla_B\mathcal L=\frac1n\sum_r e_r\gamma_r x_r^\top.
\tag{6}
\]

### 1.3 Learning-rate scaling

With Euclidean gradient flow and multipliers
\[
\eta_a=n,\qquad\eta_B=n,\qquad\eta_W=L,
\]
the exact dynamics are
\[
\boxed{
\dot a=-\sum_r e_r h_r^L,
}
\tag{7}
\]
\[
\boxed{
\dot B=-\sum_r e_r\gamma_r x_r^\top,
}
\tag{8}
\]
\[
\boxed{
\dot W_\ell
=-\frac1n\sum_r e_r\beta_r^\ell(h_r^\ell)^\top.
}
\tag{9}
\]

The scale can be audited in three equivalent ways.

* \(\nabla_af_r\) and each row of \(\nabla_Bf_r\) are \(O(n^{-1})\).
  Their squared Euclidean norms are \(O(n^{-1})\), so a multiplier \(n\)
  gives an \(O(1)\) tangent-kernel contribution and \(O(1)\) coordinate
  motion.
* For one hidden layer,
  \(\|\partial f_r/\partial W_\ell\|_F^2=O(L^{-2})\).  Summing \(L\)
  layers gives \(O(L^{-1})\), so the unique power-law multiplier yielding
  a nonzero finite total is \(L\).
* Equation (9) changes an entry of \(W_\ell\) by \(O(n^{-1})\), but
  \[
  \left\|\frac1n\beta h^\top\right\|_{\rm op}
  =\frac{\|\beta\|\,\|h\|}{n}=O(1).
  \]
  This is the standard dense feature-learning update: entrywise smaller
  than the \(n^{-1/2}\) initialization, but coherently \(O(1)\).

Using \(nL\) would make the hidden tangent kernel \(O(n)\) and the feature
velocity generically divergent.  Using \(1\) would make the total hidden
contribution vanish like \(L^{-1}\).

### 1.4 Exact tangent-kernel factor check

Let
\[
G^{h,\ell}_{rq}:=\frac1n(h_r^\ell)^\top h_q^\ell,\quad
G^{\beta,\ell}_{rq}:=\frac1n(\beta_r^\ell)^\top\beta_q^\ell,\quad
G^\gamma_{rq}:=\frac1n\gamma_r^\top\gamma_q.
\]
Then
\[
\dot f_r=-\sum_q\Theta^{(n,L)}_{rq}e_q
\]
with
\[
\boxed{
\Theta^{(n,L)}_{rq}
=G^{h,L}_{rq}
+(x_r^\top x_q)G^\gamma_{rq}
+\frac1L\sum_{\ell=0}^{L-1}
G^{h,\ell}_{rq}G^{\beta,\ell}_{rq}.
}
\tag{10}
\]
Consequently
\[
\dot{\mathcal L}=-e^\top\Theta^{(n,L)}e\le0.
\tag{11}
\]
Every term in (10) is positive semidefinite: the hidden term is a Schur
product of two Gram matrices.  Formula (10) is the cleanest complete audit of
all \(n\)- and \(L\)-factors.

The five supplied project records often use the loss \((1-f)^2\), not
\(\frac12(f-y)^2\); their physical-time equations contain an extra factor
\(2\).  That factor must not be imported into (7)--(11).

---

## 2. Classical continuum-depth equations

This subsection is conditional on a sequence of depth interpolants
\(W_{n,L}(\cdot,t)\) converging strongly enough to a matrix field
\(W_n(\cdot,t)\), and similarly for the forward and backward paths.

Put
\[
h_r(0,t)=\chi(B(t)x_r),\qquad
z_r(s,t)=W(s,t)h_r(s,t),
\]
\[
D_r(s,t)=\operatorname{diag}\phi'(z_r(s,t)).
\]
The forward equation is
\[
\boxed{
\partial_s h_r(s,t)=\phi(z_r(s,t))
=\phi(W(s,t)h_r(s,t)).
}
\tag{12}
\]

The unit-output adjoint and local backpropagated feature are
\[
\boxed{
-\partial_s q_r(s,t)=W(s,t)^\top\beta_r(s,t),
\qquad q_r(1,t)=a(t),
}
\tag{13}
\]
\[
\boxed{
\beta_r(s,t)=D_r(s,t)q_r(s,t).
}
\tag{14}
\]
Equivalently, if
\[
A_r(s,t):=D_r(s,t)W(s,t),
\]
then \(-\partial_sq_r=A_r^\top q_r\).

The Euclidean \(\mu\)P training equations are
\[
\boxed{
\partial_tW(s,t)
=-\frac1n\sum_{r=1}^m
e_r(t)\beta_r(s,t)h_r(s,t)^\top,
}
\tag{15}
\]
\[
\boxed{
\dot B(t)=-\sum_r e_r(t)\gamma_r(t)x_r^\top,\qquad
\gamma_r(t)=\operatorname{diag}\chi'(B(t)x_r)q_r(0,t),
}
\tag{16}
\]
\[
\boxed{
\dot a(t)=-\sum_r e_r(t)h_r(1,t),
}
\tag{17}
\]
\[
f_r(t)=\frac1n a(t)^\top h_r(1,t),\qquad e_r=f_r-y_r.
\tag{18}
\]

The factor \(L\) in the discrete hidden flow is precisely the Riemann-sum
conversion from the discrete Euclidean metric to the continuum
\(L^2(ds)\) metric:
\[
\frac1L\sum_\ell\|\delta W_\ell\|_F^2
\longrightarrow\int_0^1\|\delta W(s)\|_F^2\,ds.
\]

The continuum tangent kernel is
\[
\boxed{
\Theta_{rq}
=G^h_{rq}(1)
+(x_r^\top x_q)G^\gamma_{rq}
+\int_0^1G^h_{rq}(s)G^\beta_{rq}(s)\,ds.
}
\tag{19}
\]

### 2.1 Depth response and training-time feature velocity

The depth propagator is
\[
\partial_sJ_r(s,u,t)=A_r(s,t)J_r(s,u,t),
\qquad J_r(u,u,t)=I.
\tag{20}
\]
It gives \(q_r(u,t)=J_r(1,u,t)^\top a(t)\).

Let \(v_r=\partial_th_r\).  Differentiating (12) and using (15) gives
\[
\partial_sv_r
=A_rv_r-\sum_q e_qG^h_{qr}(s,t)D_r(s,t)\beta_q(s,t),
\tag{21}
\]
with
\[
v_r(0,t)
=-\sum_qe_q(t)(x_q^\top x_r)
\operatorname{diag}\chi'(B(t)x_r)\gamma_q(t).
\tag{22}
\]
Thus
\[
\boxed{
\begin{aligned}
v_r(s,t)
={}&J_r(s,0,t)v_r(0,t)\\
&-\sum_q e_q(t)\int_0^s
J_r(s,u,t)D_r(u,t)\beta_q(u,t)
G^h_{qr}(u,t)\,du .
\end{aligned}
}
\tag{23}
\]
Already \(\partial_tG^h(s,t)\) therefore needs contractions of \(J(s,u,t)\)
against features and adjoints at two depths.  One-depth Grams are not an
autonomous exact state.

---

## 3. The depth-initialization incompatibility

Define the natural piecewise-constant interpolation
\[
W_L(s,0)=W_{\lfloor Ls\rfloor}(0).
\]
With independent \(W_\ell(0)\), this sequence is not Cauchy in any strong
function topology.  A centered Gaussian object with independent nondegenerate
values at every continuum depth is not an ordinary measurable
matrix-valued path.  Weak depth averages can converge, but the realized field
does not.

The issue is visible even before training.  Conditional on a slowly varying
\(h\), for odd \(\phi=\tanh\),
\[
\frac1L\sum_{\ell<L}\phi(W_\ell h)
\]
has conditional mean zero and coordinate variance \(O(L^{-1})\).  Hence the
iid residual branches average away at initialization rather than converge to
a realized vector field \(\phi(W(s)h)\).  For a non-odd activation the limit
is an averaged drift.  In either case the limit is a homogenized law, not a
sampled depth control.

There are therefore two defensible, inequivalent limit programs.

### Program A: classical neural ODE

For each \(n\), sample a depth-regular Gaussian matrix process
\(W_n^0(s)\) whose entries have variance \(1/n\) and discretize it:
\(W_\ell^0=W_n^0(\ell/L)\).  Take
\[
L\to\infty\quad\text{at fixed }n
\]
on compact training-time intervals, and then take \(n\to\infty\).  A joint
limit is also possible under uniform operator-integrability and a convergent
depth discretization.  This yields (12)--(18), but the matrices are correlated
across layers, contrary to the stated independent initialization.

### Program B: iid-layer model as written

First take
\[
n\to\infty\quad\text{at each fixed }L,
\]
obtaining an \(L\)-layer causal DMFT, and only then take \(L\to\infty\).
This respects the initialization.  The second limit is a
rapid-depth-disorder/Young-measure or homogenization problem.  It may have
continuous macroscopic fields, but it does not retain a pointwise dense
matrix \(W(s,t)\).

A possible joint tightness condition for Gaussian operator norms is
\(\log L=o(n)\), since it keeps the maximum of \(L\) iid Gaussian matrix
operator norms \(O_{\mathbb P}(1)\).  This does not solve the lack of strong
depth convergence and is not, by itself, a joint-limit theorem.

Accordingly, no honest statement should simultaneously claim (i) independent
weights at every discrete layer, (ii) a classical realized matrix field in
the \(L\to\infty\) limit, and (iii) no additional homogenization or
depth-correlation assumption.

---

## 4. Exact dense-matrix memory identities

The following identities hold at every finite \(n,L\) and expose the exact
width-limit state.

Integrating (9),
\[
\boxed{
W_\ell(t)=W_\ell^0-\frac1n\sum_q\int_0^t
e_q(\tau)\beta_q^\ell(\tau)h_q^\ell(\tau)^\top\,d\tau.
}
\tag{24}
\]
Define two-training-time overlaps
\[
C^{h,\ell}_{qr}(\tau,t)
=\frac1n h_q^\ell(\tau)^\top h_r^\ell(t),
\]
\[
C^{\beta,\ell}_{qr}(\tau,t)
=\frac1n \beta_q^\ell(\tau)^\top\beta_r^\ell(t).
\tag{25}
\]
Then the forward and transposed fields are exactly
\[
\boxed{
\begin{aligned}
W_\ell(t)h_r^\ell(t)
={}&W_\ell^0h_r^\ell(t)\\
&-\sum_q\int_0^t
e_q(\tau)C^{h,\ell}_{qr}(\tau,t)\beta_q^\ell(\tau)\,d\tau,
\end{aligned}
}
\tag{26}
\]
\[
\boxed{
\begin{aligned}
W_\ell(t)^\top\beta_r^\ell(t)
={}&(W_\ell^0)^\top\beta_r^\ell(t)\\
&-\sum_q\int_0^t
e_q(\tau)C^{\beta,\ell}_{qr}(\tau,t)h_q^\ell(\tau)\,d\tau.
\end{aligned}
}
\tag{27}
\]

Thus eliminating \(W_\ell(t)\) does not produce a current-time Gram closure.
It produces two-time memories.  The remaining quenched fields
\(W_\ell^0h(t)\) and \((W_\ell^0)^\top\beta(t)\) are correlated with the
trajectories because the same initial matrix is reused.  Treating either as
fresh independent Gaussian noise omits the Onsager/response terms.

---

## 5. Formal fixed-\(L\) causal DMFT including reciprocal response

This section records the canonical dynamic-cavity closure suggested by
(24)--(27).  It is a formal limit description, not a theorem proved in the
supplied material.

For one layer \(\ell\), let capital letters denote a tagged coordinate:
\[
H_r^\ell(t),\quad Q_r^\ell(t),\quad
\mathsf B_r^\ell(t)=\phi'(Z_r^\ell(t))Q_r^{\ell+1}(t).
\]
Let \(A(t)\) be the tagged readout coordinate and \(b(t)\in\mathbb R^d\) the
tagged input row.  The tagged forward/backward equations are
\[
H_r^0(t)=\chi(b(t)^\top x_r),
\]
\[
H_r^{\ell+1}(t)=H_r^\ell(t)+\frac1L\phi(Z_r^\ell(t)),
\tag{28}
\]
\[
Q_r^L(t)=A(t),\qquad
Q_r^\ell(t)=Q_r^{\ell+1}(t)+\frac1L U_r^\ell(t),
\tag{29}
\]
\[
\mathsf B_r^\ell(t)
=\phi'(Z_r^\ell(t))Q_r^{\ell+1}(t).
\tag{30}
\]
The tagged input/readout training equations are
\[
\dot A=-\sum_r e_rH_r^L,\qquad
\dot b=-\sum_r e_r
\chi'(b^\top x_r)Q_r^0x_r.
\tag{31}
\]
The output and covariances are self-consistent expectations:
\[
F_r(t)=\mathbb E[A(t)H_r^L(t)],\qquad e_r=F_r-y_r,
\tag{32}
\]
\[
C^{h,\ell}_{rq}(t,t')
=\mathbb E[H_r^\ell(t)H_q^\ell(t')],
\]
\[
C^{\beta,\ell}_{rq}(t,t')
=\mathbb E[\mathsf B_r^\ell(t)\mathsf B_q^\ell(t')].
\tag{33}
\]

### 5.1 Gaussian cavity fields

For an iid nonsymmetric Gaussian \(W_\ell^0\), introduce two centered Gaussian
processes \(\xi^\ell,\zeta^\ell\), independent across layers, with
\[
\mathbb E[\xi_r^\ell(t)\xi_q^\ell(t')]
=C^{h,\ell}_{rq}(t,t'),
\]
\[
\mathbb E[\zeta_r^\ell(t)\zeta_q^\ell(t')]
=C^{\beta,\ell}_{rq}(t,t'),
\tag{34}
\]
and bare cross-covariance zero.  The latter follows because a row field
\(W h\) and a column field \(W^\top\beta\) share only one diagonal entry at a
tagged site, an \(O(n^{-1})\) covariance.  Their *effective* fields are not
independent after self-consistency.

Define causal functional responses
\[
R^{h,\ell}_{rq}(t,\tau)
=\lim_{n\to\infty}\frac1n\sum_j
\frac{\delta h_{r,j}^\ell(t)}
{\delta \upsilon_{q,j}^\ell(\tau)},
\tag{35}
\]
where \(\upsilon\) is an additive perturbation to the transposed/backward
field, and
\[
R^{\beta,\ell}_{rq}(t,\tau)
=\lim_{n\to\infty}\frac1n\sum_i
\frac{\delta \beta_{r,i}^\ell(t)}
{\delta \omega_{q,i}^\ell(\tau)},
\tag{36}
\]
where \(\omega\) perturbs the forward field.  Both vanish for
\(\tau>t\).  All residual factors, signs, and \(1/L\) factors generated by
the network equations are inside these response definitions.

The dynamic-cavity formulas are then
\[
\boxed{
\begin{aligned}
Z_r^\ell(t)
={}&\xi_r^\ell(t)
+\sum_q\int_0^t
R^{h,\ell}_{rq}(t,\tau)\mathsf B_q^\ell(\tau)\,d\tau\\
&-\sum_q\int_0^t
e_q(\tau)C^{h,\ell}_{qr}(\tau,t)
\mathsf B_q^\ell(\tau)\,d\tau ,
\end{aligned}
}
\tag{37}
\]
\[
\boxed{
\begin{aligned}
U_r^\ell(t)
={}&\zeta_r^\ell(t)
+\sum_q\int_0^t
R^{\beta,\ell}_{rq}(t,\tau)H_q^\ell(\tau)\,d\tau\\
&-\sum_q\int_0^t
e_q(\tau)C^{\beta,\ell}_{qr}(\tau,t)
H_q^\ell(\tau)\,d\tau .
\end{aligned}
}
\tag{38}
\]

The last lines of (37)--(38) are the exact learned-low-rank memories from
(26)--(27).  The middle lines are the two reciprocal Onsager terms generated
by reuse of \(W_\ell^0\):

* perturbing the column/backward field changes \(h\), which feeds back through
  the same row of \(W_\ell^0\);
* perturbing the row/forward field changes \(\beta\), which feeds back through
  the same column of \(W_\ell^0\).

Equations (28)--(38), together with the response definitions, are the natural
fixed-\(L\) causal DMFT.  Omitting either response term is equivalent to
resampling the dense matrix independently in the forward and backward uses
and gives the wrong model.

For a depth-correlated Gaussian matrix process, (34) acquires the depth
covariance \(K_W(s,u)\) and cross-depth overlaps, while (37)--(38) acquire
integrals over the coupled depth channel.  This makes the exact state larger,
not smaller.

### 5.2 Best exact macroscopic state

On a finite training interval \([0,T]\), the natural state is the law of the
tagged histories
\[
\bigl(b,A,H,Q,\mathsf B,Z,U\bigr)_{0\le t\le T}
\]
over all samples and depths, together with
\[
C^h,\ C^\beta,\ R^h,\ R^\beta
\]
on the causal two-time triangle.  Mixed contractions needed for chosen
observables are read from the joint path law.  A natural candidate topology
is a Wasserstein topology on continuous path space, augmented by uniform or
\(L^2\)-triangle norms for covariance and response kernels; moment weights are
needed for \(Q,\mathsf B\).

This state is causal and restartable only in a history sense: at time \(t_0\)
one must retain the kernels and path history on \([0,t_0]\), or equivalently
the accumulated memory forcings in (37)--(38).  The current one-time marginal
does not suffice.  The state grows as a function of the training-time
triangle and is not a finite PDE.

The fixed-time depth propagator \(J_r(s,u,t)\) controls sensitivity along
depth and is essential for Gram evolution, but it does not replace
\(R^h,R^\beta\), which are responses across **training time** caused by
quenched-matrix reuse.

---

## 6. What is proved, formal, and contradicted by the supplied notes

### Proved by direct finite-system algebra

* Equations (1)--(11), including every factor of \(n,L\).
* Global existence of each finite-\((n,L)\) gradient flow on finite time
  intervals follows from smooth finite-dimensional gradient flow and energy
  dissipation; no width-uniform bound is implied.
* The exact integrated-weight and memory identities (24)--(27).
* Conditional on a convergent depth interpolation, the formal Riemann-sum
  limit gives (12)--(19).

### Formal or requiring a new theorem

* Convergence at \(n\to\infty\) to (28)--(38), even for fixed \(L\), as a
  continuous-time dynamic mean field.
* Existence, uniqueness, and stability of that causal stochastic Volterra
  system on arbitrary training horizons.
* Passage \(L\to\infty\) through the two-time covariance and response system.
* Interchange or a joint limit in \(n,L\).
* A global restartable width-limit state with uniform moment/response bounds.

Bounded smooth \(\tanh\) removes the specific unbounded-polynomial Gaussian
moment catastrophe in the earlier project, but it does not by itself prove
these response estimates.

### Audit of the five project records

The records concern a different, two-hidden-layer quadratic model.  Their
useful transferable warnings are:

* fixed-order Wick/Taylor information is not positive-time DMFT;
* a non-oracular finite compiler needs a real-axis state and residual theorem;
* matrix reuse creates response/continuation data invisible to simple Grams;
* loss stability cannot substitute for a state-approximation theorem.

One supplied note correctly states that the full positive-time tagged
Volterra representation had not been independently established.  A later
note treats such a representation, positivity of its initial self-response,
and a relaxed instantaneous-fitting selection as canonical and proved.  Those
are additional assumptions, not consequences of the earlier calculations.
They must not be imported as a theorem.  In any event their Riccati mechanism
uses an unbounded quadratic activation/readout tail and does not apply to the
bounded residual-\(\tanh\) model here.

---

## 7. Concise answer to the scaling/DMFT assignment

1. The finite model is exactly (1)--(9), with raw terminal adjoint \(a/n\) or
   unit terminal adjoint \(a\).
2. The user's expected rates \(n,n,L\) are correct; the factor audit is the
   exact PSD kernel (10).
3. Conditional on depth-regular weights, the continuum equations are
   (12)--(18), and their response formula is (23).
4. Independent layer initialization does not produce a classical matrix
   field \(W(s,0)\).  The problem must choose between a depth-coherent
   neural-ODE limit and an iid-layer homogenized/DMFT limit.
5. At fixed \(L\), the strongest causal width-independent candidate is the
   path-space DMFT (28)--(38), containing two-time covariances and two
   reciprocal response kernels.  Its global well-posedness and the subsequent
   depth limit remain conjectural.

