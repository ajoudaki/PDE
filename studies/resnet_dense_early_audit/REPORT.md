# Standard dense Euclidean continuous-depth \(\mu\)P

## Audited causal state, response compression evidence, and the sharp finite-neural-PDE conjecture

> **Program-scope note.** This is the finite-matrix precursor phase. Sections
> 8--11 formulate a conjectural future width-independent compiler and its
> proof obligations; they are not results established by the executed
> simulations.

### Executive verdict

The audit resolves the normalization and identifies a real compression
mechanism, but it does **not** prove the requested all-time finite neural PDE.

The main conclusions are:

1. For
   \[
   f_r=\frac1n a^\top h_r^L,\qquad
   h_r^{\ell+1}=h_r^\ell+\frac1L\tanh(W_\ell h_r^\ell),
   \]
   and loss
   \[
   \mathcal L=\frac12\sum_{r=1}^m(f_r-y_r)^2,
   \]
   the correct Euclidean feature-learning powers are
   \[
   \eta_B\asymp n,\qquad \eta_a\asymp n,\qquad
   \eta_{W_\ell}\asymp L.
   \]
   With the locked unit-time, equal-block-metric convention used throughout,
   the multipliers are exactly
   \[
   \boxed{\eta_B=n,\qquad \eta_a=n,\qquad \eta_{W_\ell}=L.}
   \]
   The half-squared loss introduces no forced factor \(2\). Fixed positive
   block constants are conventional; unequal constants change the relative
   block metric.

2. The initialization requested in the problem and the requested classical
   neural ODE are not the same limit. If the \(W_\ell(0)\) are independent
   across layers, their piecewise-constant interpolants do not converge
   strongly in depth \(L^2\) (nor in \(C\)) to a nondegenerate realized matrix
   path \(W(s,0)\). With a \(1/L\) residual branch and odd \(\tanh\), the
   random initialization contribution has normalized RMS at most
   \(L^{-1/2}\) (and showed that rate numerically in the tested nondegenerate
   cases).

3. This report defines the literal canonical \(\mu\)P target by
   \[
   \boxed{n\to\infty\text{ at fixed }L,\quad\text{then }L\to\infty.}
   \]
   Its expected exact state is a depth-homogenized causal DMFT/path law with
   two-training-time covariance and response kernels. It is not a classical
   pointwise matrix-field ODE merely by interpolation. A depth-coherent
   coupling guarantees the classical construction; any emergent effective
   matrix-field representation for iid depth would require a separate
   theorem. An \(L\)-first mean-ODE/Young-measure limit or a joint limit may
   also exist; equality of those limits with the chosen target is open.

4. For a separate depth-regular Gaussian matrix-field initialization, the
   classical continuum equations are unambiguous. Its depth response has a
   rigorous, noncommutative and nonnormal-safe Dyson tail
   \[
   \left\|J-J_{\le M}\right\|_{\rm op}
   \le
   \sum_{k>M}\frac{C_A^k}{k!},
   \qquad
   C_A=\int_0^1\|D(s)W(s)\|_{\rm op}\,ds.
   \]
   This is a genuine real-axis approximation result and is qualitatively
   different from the divergent training-time Wick--Taylor expansions in the
   earlier project.

5. This tail does not by itself give a finite neural PDE. Every Dyson word
   still contains dense matrices, the full \(n\times n\) response has no
   width-independent matrix-rank approximation, and eliminating the matrices
   creates two-training-time Onsager/memory kernels.

6. The finite computations strongly support low **depth-word order** over the
   tested horizons. At order \(M=4\), generic, nonnormal, iid-depth, restart,
   and parameter-sweep errors were small while the generic hidden Grams moved
   by \(O(1)\). But every truncated trajectory retained all dense matrices,
   so it was not the desired width-independent compiler.

7. The all-time, horizon-independent conclusion remains genuinely open.
   Positive semidefiniteness and squared-loss descent give an
   \(L^2\)-in-time speed budget, not a uniform tangent-kernel gap or finite
   feature arclength. The nearly aligned numerical case makes this gap
   concrete: its kernel floor was about \(1.2\times10^{-3}\), its loss was
   still \(0.72\) at \(T=1.6\), and its hidden-Gram motion was only \(0.0084\).

The final conjecture below is consequently a strong frontier conjecture, not
a disguised theorem. Its formulation is the desired certified finite-PDE
existence statement itself. It cannot be satisfied by curve fitting, arbitrary
real coefficients, time playback, a renamed finite network, or a formal
Dyson truncation.

---

## 1. Audit structure and inherited project results

The five supplied project records were read in full. Their transferable
lessons are:

- fixed-order Wick or Taylor coefficients are not a positive-time
  approximation theorem;
- the earlier quadratic/Gaussian Wick--Taylor compiler has zero radius and is
  false;
- squared loss propagates a **known** residual-compatible error, but does not
  make an unproved hierarchy tail small;
- matrix reuse creates continuation/response data invisible to simple
  moments;
- “one source” and “finite PDE” are syntactic unless coefficient provenance,
  restartability, and a residual norm are fixed;
- the earlier unbounded quadratic rare-tail/Riccati obstruction does not
  automatically transfer to bounded residual \(\tanh\).

Three independent research tracks covered the requested roles:

- scaling, continuum depth, and causal DMFT;
- response/Dyson, Galerkin, nonlinear stability, long time, and approximation
  theory;
- continuation, nonnormality, high-to-low feedback, rare tails, and
  anti-oracle attacks.

Two further independent synthesis passes compared all three reports and the
numerical archive. A separate code audit checked every finite-\((n,L)\)
gradient, the adjoint truncation, the tangent-kernel identity, depth
interpolation, and the interpretation of the PSD diagnostic.
After the first complete draft, three fresh independent audits rechecked
(i) scaling and limit order, (ii) long-time/nonnormal/PSD claims, and
(iii) the conjecture's topology, effectiveness, and oracle loopholes. Their
counterexamples forced the compact restart class, distributional law
residual, residual-gated certificate, and typed provenance clauses in
Section 8.

---

## 2. Locked finite-\((n,L)\) model and scaling

Fix \(m,d,n,L\). For sample \(r\), define

\[
u_r=Bx_r,\qquad h_r^0=\chi(u_r),
\]

\[
z_r^\ell=W_\ell h_r^\ell,\qquad
h_r^{\ell+1}
=h_r^\ell+\frac1L\phi(z_r^\ell),
\qquad 0\le\ell<L,
\]

\[
f_r=\frac1n a^\top h_r^L,\qquad
e_r=f_r-y_r,
\]

\[
\mathcal L=\frac12\sum_{r=1}^m e_r^2.
\]

The locked activation is

\[
\chi=\phi=\tanh.
\]

Initialization is independent:

\[
B_{ij}\sim N(0,d^{-1}),\qquad
W_{\ell,ij}\sim N(0,n^{-1}),\qquad
a_i\sim N(0,1).
\]

All layers and parameter groups are independent in the literal model.

### 2.1 Adjoint convention

Define the unit-output adjoint

\[
q_r^\ell:=n\,\frac{\partial f_r}{\partial h_r^\ell}.
\]

Then

\[
q_r^L=a.
\]

With

\[
D_r^\ell=\operatorname{diag}\phi'(z_r^\ell),
\qquad
\beta_r^\ell=D_r^\ell q_r^{\ell+1},
\]

the exact recurrence is

\[
\boxed{
q_r^\ell
=q_r^{\ell+1}
+\frac1L W_\ell^\top\beta_r^\ell.
}
\tag{2.1}
\]

For the input block,

\[
\gamma_r
=\operatorname{diag}\chi'(Bx_r)\,q_r^0.
\tag{2.2}
\]

The raw adjoint \(\partial f_r/\partial h_r^\ell\) is \(q_r^\ell/n\)
and ends at \(a/n\). Confusing the raw and unit-output adjoints is the main
source of an erroneous extra factor \(n\).

### 2.2 Exact gradients

Direct differentiation gives

\[
\frac{\partial f_r}{\partial a}=\frac1n h_r^L,
\]

\[
\frac{\partial f_r}{\partial W_\ell}
=\frac1{nL}\beta_r^\ell(h_r^\ell)^\top,
\]

\[
\frac{\partial f_r}{\partial B}
=\frac1n\gamma_r x_r^\top.
\]

Hence the exact Euclidean gradient flow is

\[
\boxed{
\dot a=-\sum_r e_r h_r^L,
}
\tag{2.3}
\]

\[
\boxed{
\dot B=-\sum_r e_r\gamma_r x_r^\top,
}
\tag{2.4}
\]

\[
\boxed{
\dot W_\ell
=-\frac1n\sum_r e_r\beta_r^\ell(h_r^\ell)^\top.
}
\tag{2.5}
\]

Equations (2.3)--(2.5) are exactly

\[
\dot a=-n\nabla_a\mathcal L,\qquad
\dot B=-n\nabla_B\mathcal L,\qquad
\dot W_\ell=-L\nabla_{W_\ell}\mathcal L.
\]

This locks the unit-time convention. More generally the same \(\mu\)P powers
are \(c_an,c_Bn,c_WL\) for fixed positive constants; a common constant only
rescales training time, while unequal constants alter the relative
contributions of the parameter blocks.

When \(\|\beta\|,\|h\|=O(\sqrt n)\), as in the intended scaling regime, the
rank-one update has Frobenius norm \(O(1)\), hence RMS entry
\(O(n^{-1})\), but coherent operator action
\[
\left\|\frac1n\beta h^\top\right\|_{\rm op}
=\frac{\|\beta\|\,\|h\|}{n}=O(1),
\]
which is the dense feature-learning scale. No maximum-entry or tagged-entry
delocalization bound is asserted.

### 2.3 Exact tangent kernel

Define

\[
G^{h,\ell}_{rq}=\frac1n(h_r^\ell)^\top h_q^\ell,
\qquad
G^{\beta,\ell}_{rq}
=\frac1n(\beta_r^\ell)^\top\beta_q^\ell,
\]

\[
G^\gamma_{rq}=\frac1n\gamma_r^\top\gamma_q.
\]

Then

\[
\dot f=-\Theta^{(n,L)}e,
\]

where

\[
\boxed{
\Theta^{(n,L)}_{rq}
=G^{h,L}_{rq}
+(x_r^\top x_q)G^\gamma_{rq}
+\frac1L\sum_{\ell=0}^{L-1}
G^{h,\ell}_{rq}G^{\beta,\ell}_{rq}.
}
\tag{2.6}
\]

Every block is PSD. The hidden term is a Schur product of two Gram
matrices. Therefore

\[
\dot{\mathcal L}=-e^\top\Theta^{(n,L)}e\le0.
\tag{2.7}
\]

The scaled metric also gives

\[
-\dot{\mathcal L}
=\frac{\|\dot a\|^2}{n}
+\frac{\|\dot B\|_F^2}{n}
+\frac1L\sum_{\ell=0}^{L-1}\|\dot W_\ell\|_F^2.
\tag{2.8}
\]

This identity supplies finite-time energy envelopes, but not an all-time
\(L^1\) arclength bound.

---

## 3. The continuum-depth model fork

### 3.1 Classical depth-regular neural ODE

Suppose, separately from the literal iid-layer model, that for each \(n\) a
centered depth-regular Gaussian matrix process \(W_n^0(s)\), independent of
\(B\) and \(a\), is specified by

\[
\mathbb E\!\left[
W^0_{ij}(s)W^0_{kl}(u)
\right]
=\frac1n\delta_{ik}\delta_{jl}K_W(s,u),
\qquad K_W(s,s)=1,
\]

where \(K_W\) is a declared continuous positive-semidefinite kernel and the
process has almost-sure continuous (for example Hölder) paths. Couple every
finite depth to the same process by
\[
W_{\ell,L}^0=W_n^0(\ell/L).
\]
On each finite training interval, standard Euler/gradient-flow stability for
this coupled discretization gives, as \(L\to\infty\) at fixed \(n\),

\[
h_r(0,t)=\chi(B(t)x_r),
\]

\[
\boxed{
\partial_s h_r(s,t)
=\phi(W(s,t)h_r(s,t)).
}
\tag{3.1}
\]

Let

\[
z_r=Wh_r,\qquad
D_r=\operatorname{diag}\phi'(z_r),
\qquad
\beta_r=D_rq_r.
\]

The continuum adjoint is

\[
\boxed{
-\partial_s q_r(s,t)
=W(s,t)^\top\beta_r(s,t),
\qquad q_r(1,t)=a(t).
}
\tag{3.2}
\]

The Euclidean training equations are

\[
\boxed{
\partial_tW(s,t)
=-\frac1n\sum_r e_r(t)\beta_r(s,t)h_r(s,t)^\top,
}
\tag{3.3}
\]

\[
\boxed{
\dot B(t)
=-\sum_r e_r(t)
\operatorname{diag}\chi'(B(t)x_r)q_r(0,t)x_r^\top,
}
\tag{3.4}
\]

\[
\boxed{
\dot a(t)=-\sum_r e_r(t)h_r(1,t).
}
\tag{3.5}
\]

The continuum kernel is

\[
\boxed{
\Theta_{rq}
=G^h_{rq}(1)
+(x_r^\top x_q)G^\gamma_{rq}
+\int_0^1G^h_{rq}(s)G^\beta_{rq}(s)\,ds.
}
\tag{3.6}
\]

For this separate model, the finite-\(n\) classical matrix-field equation is
defined by the order

\[
L\to\infty\text{ at fixed }n,
\qquad
n\to\infty\text{ second}.
\]

No claim is made that this order is uniquely correct or commutes with a
joint limit.

### 3.2 Literal iid-across-layer model

For the model stated in the request,

\[
W_\ell(0)\ \text{are independent over }\ell.
\]

The interpolant

\[
W_L(s,0)=W_{\min\{\lfloor Ls\rfloor,L-1\}}(0)
\]

does not converge strongly to an ordinary matrix-valued path. At
initialization the residual increments are martingale differences:
\(h_r^\ell\) is measurable with respect to the preceding layers, whereas
\(W_\ell\) is independent and symmetric, so oddness gives

\[
\mathbb E\!\left[
\tanh(W_\ell h_r^\ell)
\mid W_0,\ldots,W_{\ell-1},B
\right]=0.
\]

Consequently,

\[
\mathbb E\frac{\|h_r^L-h_r^0\|^2}{n}
=
\frac1{L^2}\sum_{\ell=0}^{L-1}
\mathbb E\frac{\|\tanh(W_\ell h_r^\ell)\|^2}{n}
\le\frac1L.
\]

The terminal residual displacement therefore vanishes in mean square in the
normalized neuron norm, with RMS at most \(L^{-1/2}\), rather than approaching
\(\int_0^1\tanh(W(s)h(s))\,ds\) for a depth-regular realized field. The iid
step interpolants also fail the depth-translation tightness required for a
strong \(L^2_s\) or continuous-path limit; their natural limit object is a
Young/type law.

For example, for one entry \(w_L(s)\), any fixed
\(0<\delta<1\) gives

\[
\mathbb E\int_0^{1-\delta}
|w_L(s+\delta)-w_L(s)|^2\,ds
\longrightarrow\frac{2(1-\delta)}n,
\]

whereas every fixed \(\psi\in L^2[0,1]\) obeys

\[
\mathbb E\left|\int_0^1\psi(s)w_L(s)\,ds\right|^2
\le\frac{\|\psi\|_{L^2}^2}{nL}.
\]

Thus the iid paths weakly average to zero but are not strongly
translation-compact. Their nonlinear type information is naturally
represented by a Gaussian Young/type measure; whether that measure is needed
in a minimal observable state is open.

We choose the standard width-first \(\mu\)P iterated target:

\[
\boxed{
n\to\infty\ \text{at each fixed }L,
\qquad
L\to\infty\ \text{in the resulting causal DMFT}.
}
\tag{3.7}
\]

The second limit is a depth-homogenization, layer-type, or Young-measure
problem. Calling its limit \(W(s,t)\) before deriving it would conflate two
different models.

This is a definition of the conjecture's target, not a theorem excluding an
\(L\)-first mean-ODE limit or a controlled joint regime. Existence and
equality of those alternatives remain open.

This distinction is consistent with current rigorous large-depth work:
shared or depth-coherent weights lead to classical neural ODEs, while iid
blocks can converge by stochastic approximation to a mean ODE rather than a
realized pointwise control. See
[Avelin--Nyström](https://arxiv.org/abs/1906.12183) and
[Chizat](https://arxiv.org/abs/2509.10167).

No joint or commuting \(n,L\) limit is asserted here. A condition such as
\(\log L=o(n)\) can control the maximum Gaussian operator norm, but it does
not create strong depth convergence.

---

## 4. Exact causal information before finite approximation

### 4.1 Depth response

For the classical depth-regular equations, define

\[
A_r(s,t)=D_r(s,t)W(s,t)
\]

and

\[
\boxed{
\partial_sJ_r(s,u,t)
=A_r(s,t)J_r(s,u,t),
\qquad J_r(u,u,t)=I.
}
\tag{4.1}
\]

Then

\[
q_r(u,t)=J_r(1,u,t)^\top a(t).
\]

Let \(v_r=\partial_t h_r\). Differentiating the forward equation gives

\[
\partial_sv_r
=A_rv_r
-\sum_q e_qG^h_{qr}(s,t)D_r(s,t)\beta_q(s,t),
\tag{4.2}
\]

with boundary value

\[
v_r(0,t)
=-\sum_q e_q(x_q^\top x_r)
\operatorname{diag}\chi'(Bx_r)\gamma_q.
\tag{4.3}
\]

Thus

\[
\boxed{
\begin{aligned}
v_r(s,t)
={}&J_r(s,0,t)v_r(0,t)\\
&-\sum_qe_q(t)\int_0^s
J_r(s,u,t)D_r(u,t)\beta_q(u,t)
G^h_{qr}(u,t)\,du.
\end{aligned}
}
\tag{4.4}
\]

Consequently, \(\partial_tG^h(s,t)\) depends on two-depth response
contractions. One-depth Grams do not form an exact autonomous state.

### 4.2 Exact dense-matrix memory identities

At every finite \(n,L\),

\[
W_\ell(t)
=W_\ell^0
-\frac1n\sum_q\int_0^t
e_q(\tau)\beta_q^\ell(\tau)h_q^\ell(\tau)^\top\,d\tau.
\tag{4.5}
\]

Define

\[
C^{h,\ell}_{qr}(\tau,t)
=\frac1n h_q^\ell(\tau)^\top h_r^\ell(t),
\]

\[
C^{\beta,\ell}_{qr}(\tau,t)
=\frac1n\beta_q^\ell(\tau)^\top\beta_r^\ell(t).
\]

Then

\[
\boxed{
\begin{aligned}
W_\ell(t)h_r^\ell(t)
={}&W_\ell^0h_r^\ell(t)\\
&-\sum_q\int_0^t
e_q(\tau)C^{h,\ell}_{qr}(\tau,t)
\beta_q^\ell(\tau)\,d\tau,
\end{aligned}
}
\tag{4.6}
\]

\[
\boxed{
\begin{aligned}
W_\ell(t)^\top\beta_r^\ell(t)
={}&(W_\ell^0)^\top\beta_r^\ell(t)\\
&-\sum_q\int_0^t
e_q(\tau)C^{\beta,\ell}_{qr}(\tau,t)
h_q^\ell(\tau)\,d\tau.
\end{aligned}
}
\tag{4.7}
\]

Eliminating \(W_\ell\) therefore produces two-training-time memory, not a
current-time Gram closure.

### 4.3 Best exact width-independent state

For fixed \(L\), the formal dense causal DMFT requires:

- a tagged path law for the input row, readout coordinate, forward features,
  adjoints, preactivations, and backpropagated messages;
- covariance kernels \(C^h,C^\beta\);
- reciprocal functional-response kernels \(R^h,R^\beta\);
- Gaussian forward and backward cavity fields whose covariances are
  \(C^h,C^\beta\);
- the learned memory terms in (4.6)--(4.7).

Schematically the effective forward and backward fields have the form

\[
Z=\xi+\mathcal R^h[\beta]-\mathcal M^h[\beta],
\]

\[
U=\zeta+\mathcal R^\beta[h]-\mathcal M^\beta[h],
\]

where \(\mathcal M^h,\mathcal M^\beta\) are the explicit learned memories and
\(\mathcal R^h,\mathcal R^\beta\) are the Onsager responses caused by reuse of
the same initial dense matrix in forward and transposed directions.

Treating the cavity fields as fresh at each use deletes these reciprocal
responses and changes the model.

For the iid-depth outer limit, a conservative candidate description also
retains the depth-indexed type or Young measure generated by homogenization.
Its necessity or minimality is not asserted before the homogenization
theorem exists.

### 4.4 Topology and restartability

On a finite training interval, a natural candidate phase space is a product
of:

- a Wasserstein-2 path-law space with uniform sub-Gaussian/Orlicz control;
- strong causal Sobolev spaces for the covariance and response remainders;
- explicit causal boundary/trace components;
- depthwise sup norms for observable Grams;
- a norm controlling coherent operator actions on all dynamically generated
  sample/message directions.

An all-time version may use a shifted-history weight

\[
\omega(\tau)=(1+\tau)^{-p},\qquad p>1,
\]

while retaining unweighted output and Gram readouts. The response remainder
must be stronger than \(H^1\) on the causal triangle so that multiplication
and traces are continuous. The known Volterra/Heaviside primitive should be
factored explicitly rather than forced into a smooth remainder.

Restartability is **history restartability**. At time \(t_0\), the current
augmented memory state is supplied and the system evolves in relative time.
A one-time marginal is not enough. An absolute-time curve table is not a
restart state.

The construction, global uniqueness, and continuity of this state remain
conjectural. The five supplied project notes do not prove them.

---

## 5. Constructive approximation mechanisms

### 5.1 Dyson truncation

For measurable \(A\) with

\[
C(s,u)=\int_u^s\|A(v)\|_{\rm op}\,dv<\infty,
\]

the chronological series is

\[
J(s,u)
=I+\sum_{k\ge1}
\int_{u<s_1<\cdots<s_k<s}
A(s_k)\cdots A(s_1)\,ds_1\cdots ds_k.
\]

Submultiplicativity and simplex volume give

\[
\boxed{
\|J-J_{\le M}\|_{\rm op}
\le
R_M(C):=
\sum_{k>M}\frac{C^k}{k!}
\le e^C\frac{C^{M+1}}{(M+1)!}.
}
\tag{5.1}
\]

No commutativity, normality, diagonalizability, or spectral gap is used.

The discrete residual network obeys the same estimate with

\[
C_{r,L}(t)
=\frac1L\sum_{\ell=0}^{L-1}
\|D_{r,\ell}(t)W_\ell(t)\|_{\rm op}.
\]

The recursive terms

\[
Z_0=I,\qquad
\partial_sZ_k=A Z_{k-1},\qquad
Z_k(u,u)=0
\]

give \(J_{\le M}=\sum_{k=0}^MZ_k\) and local residual

\[
\partial_sJ_{\le M}-AJ_{\le M}=-AZ_M.
\]

This is a non-oracular depth-response certificate **once** an a priori
operator budget is known.

### 5.2 Finite-time operator envelope

From (2.8),

\[
\frac1L\sum_\ell
\|W_\ell(t)-W_\ell(0)\|_{\rm op}
\le
\sqrt{T\mathcal L(0)}
\qquad (t\le T).
\tag{5.2}
\]

Since \(|\tanh|\le1\),

\[
\sup_{r,s,t}\frac{\|h_r(s,t)\|}{\sqrt n}\le2.
\]

The adjoint satisfies

\[
\frac{\|q_r(s,t)\|}{\sqrt n}
\le
\left(
\frac{\|a(0)\|}{\sqrt n}
+\sqrt{T\mathcal L(0)}
\right)
\exp\!\left(
\int_0^1\|W(u,0)\|_{\rm op}\,du
+\sqrt{T\mathcal L(0)}
\right),
\qquad 0\le t\le T,
\]

because
\[
\frac{\|a(t)-a(0)\|}{\sqrt n}
\le\sqrt{T\mathcal L(0)}
\]
and
\[
\int_0^1\|W(u,t)-W(u,0)\|_{\rm op}\,du
\le\sqrt{T\mathcal L(0)}.
\]
Thus all response/source terms have finite-\(T\),
width/depth-uniform high-probability envelopes whenever the normalized
initial readout, integrated initial operator norm, and initial loss have such
envelopes. For compact data/label classes these follow from the declared
Gaussian initialization, but the probability level must be carried into any
quantitative theorem.

The available upper envelope is
\[
C_0+\sqrt{T\mathcal L(0)},
\qquad
C_0=\int_0^1\|W(u,0)\|_{\rm op}\,du.
\]
It is not horizon-independent and therefore does not yield a fixed all-time
Dyson order.

### 5.3 Causal Galerkin

On

\[
\Delta_2=\{(s,u):0\le u\le s\le1\},
\]

use boundary-conforming finite elements or a basis such as

\[
J_N(s,u)
=I+(s-u)\sum_{i+j\le N}c_{ij}
P_i(2u-1)
P_j\!\left(2\frac{s-u}{1-u}-1\right).
\]

For approximate generator \(A_N\), define

\[
r_{J,N}=\partial_sJ_N-A_NJ_N,
\qquad
b_{J,N}=J_N(u,u)-I.
\]

Duhamel gives the a posteriori estimate

\[
\boxed{
\sup_{u\le s}\|J(A_N;s,u)-J_N(s,u)\|
\le
e^{C_N}
\left[
\sup_u\|b_{J,N}(u)\|
+\sup_u\int_u^1\|r_{J,N}(s,u)\|\,ds
\right].
}
\tag{5.3}
\]

Replacing \(A_N\) by the unknown exact \(A\) introduces
\(\|A-A_N\|\), which is not a certificate unless it is absorbed into the
outgoing residual of the complete approximate macroscopic system.

Uniform \(H^p\) regularity gives algebraic depth approximation. Uniform
analyticity could give spectral rates. Neither follows from an \(L^1\)
operator bound alone.

### 5.4 PSD tangent-kernel reconstruction

With positive quadrature weights \(w_j\), define

\[
\boxed{
\Theta_M
=G^h_M(1)
+G^x\circ G^\gamma_M
+\sum_jw_j
\left(G^h_M(s_j)\circ G^\beta_M(s_j)\right).
}
\tag{5.4}
\]

If every approximate Gram is built from feature factors or positive cubature,
then \(\Theta_M\succeq0\) exactly.

The safest construction is:

1. discretize the approximate forward macroscopic model;
2. take the exact adjoint of that same finite model;
3. define \(\Theta_M\) as the Gram of its sensitivities.

Adding a ridge would change the optimizer and is not allowed.

### 5.5 Full feedback stability, conditional theorem

Write the exact macroscopic dynamics abstractly as

\[
\dot e=-\Theta(Z)e,\qquad
\dot Z=V(Z)e.
\tag{5.5}
\]

Suppose on a restartable invariant tube that:

\[
\Theta(Z)\succeq\lambda I,\qquad
\Theta_M(Z_M)\succeq\lambda I/2,
\]

\[
\Theta,V\ \text{are Lipschitz in a strong forcing norm},\qquad
\|V(Z)\|\le V_0,
\]

and the approximate system and its consistency defects obey

\[
\dot e_M=-\Theta_M(Z_M)e_M,
\]

\[
\dot Z_M=V_M(Z_M)e_M+r_M,\qquad
\|r_M(t)\|\le\rho_M\|e_M(t)\|.
\]

Assume also, throughout the common tube,

\[
\|\Theta_M(Z)-\Theta(Z)\|\le\beta_\Theta,\qquad
\|V_M(Z)-V(Z)\|\le\beta_V.
\]

Then

\[
\int_0^\infty\|e_M(t)\|\,dt
\le\frac{2\|e_M(0)\|}{\lambda},
\]

and Gronwall is taken over this finite residual budget, not over infinite
physical time. More explicitly, with
\[
I_M=\frac{2\|e_M(0)\|}{\lambda},
\]
and
\[
E_Z(t)=\|Z(t)-Z_M(t)\|,\qquad
E_e(t)=\|e(t)-e_M(t)\|,
\]
the state error satisfies

\[
\begin{aligned}
\sup_{t\ge0}\|Z(t)-Z_M(t)\|
\le{}&
\left[
E_Z(0)+\frac{V_0}{\lambda}E_e(0)
+\left(
\beta_V+\rho_M+\frac{V_0\beta_\Theta}{\lambda}
\right)I_M
\right]\\
&\times
\exp\!\left[
\left(L_V+\frac{V_0L_\Theta}{\lambda}\right)I_M
\right].
\end{aligned}
\]

Variation of constants for the residual then gives

\[
\sup_{t\ge0}\|e(t)-e_M(t)\|
\le
E_e(0)
+\left(
L_\Theta\sup_tE_Z(t)+\beta_\Theta
\right)I_M.
\]

In particular, one obtains

\[
\boxed{
\sup_{t\ge0}
\left(\|e(t)-e_M(t)\|+\|Z(t)-Z_M(t)\|\right)
\le
\Gamma\left(
\text{initial error}
+\rho_M+\beta_\Theta+\beta_V
\right),
}
\tag{5.6}
\]

with horizon-independent \(\Gamma\).

This closes

\[
\text{response error}
\to\text{feature/adjoint error}
\to\text{kernel error}
\to\text{new response error}
\]

under explicit hypotheses. The missing problem-specific theorem is that the
standard Euclidean model and its compiler satisfy those hypotheses uniformly.

---

## 6. Hostile results and failed approaches

### 6.1 Exact continuation witness

Take one sample and choose \(h,\beta\in\mathbb R^n\) with

\[
h^\top\beta=0,\qquad
\|h\|^2=c^2n,\qquad
\|\beta\|^2=n.
\]

Let a dense matrix \(K\) annihilate \(h,\beta\) in the required forward and
transposed directions, and put

\[
W_0=K,\qquad
W_1=K+\frac1n h\beta^\top.
\]

Both states have the same \(h,q,\beta\), preactivations, forward/backward
Grams, \(Wh\), \(W^\top\beta\), output, loss, and Euclidean weight velocity.
The perturbation has \(O(n^{-1})\) entries and is invisible to fixed-row
limits.

Yet

\[
W_1\beta=h,\qquad W_0\beta=0,
\]

so their feature velocities and immediate hidden-Gram derivatives differ by
\(O(1)\). The missing datum is a response action.

This refutes exact closure by current one-depth laws and Grams on any restart
class containing the witness. It does not refute every response-aware
approximation, and reachability from the single canonical initialization
would require a separate argument.

### 6.2 Full \(J\) cannot be width-independently low rank

Since

\[
J(u,u)=I_n
\]

and

\[
\|J^{-1}(s,u)\|_{\rm op}\le e^{C(s,u)},
\]

all singular values obey

\[
\sigma_{\min}(J(s,u))\ge e^{-C(s,u)}.
\]

Therefore every rank \(R<n\) approximation has

\[
\|J-\widetilde J_R\|_{\rm op}\ge e^{-C}.
\]

A valid compiler must compress:

- scalar or sample-indexed response contractions;
- depth/time dependence after factoring the causal primitive;
- or a finite law/chaos representation.

It cannot compress \(J\) itself in neuron coordinates to width-independent
rank.

### 6.3 Nonnormality

A nilpotent coherent perturbation can have all eigenvalues zero while mapping
\(\beta\) to \(\beta+\tau h\). Eigenvalue-only stability is false.

Nonnormality does **not** invalidate (5.1). The operator norm or logarithmic
norm already accounts for transient amplification.

### 6.4 Weak residuals and high-to-low feedback

An error with vanishing normalized Frobenius norm can act on coherent
\(\sqrt n\)-norm feature/adjoint directions and create an \(O(1)\)
contraction. Two discarded high depth modes can also multiply into a retained
constant mode.

Therefore the residual norm must control:

- coherent operator actions;
- nonlinear outgoing products;
- causal diagonal/trace evaluation;
- all Gram and kernel contractions.

Entrywise, row-law, normalized-Frobenius, or unweighted \(L^2\) smallness is
not sufficient.

### 6.5 PSD without coercivity

Consider

\[
\Theta_\delta=\operatorname{diag}(1,\delta),
\qquad
\widehat\Theta_\delta=\operatorname{diag}(1,0).
\]

Both are PSD and

\[
\|\Theta_\delta-\widehat\Theta_\delta\|_{\rm op}=\delta.
\]

For any fixed horizon the residual trajectories are close as
\(\delta\to0\), but

\[
\sup_{t\ge0}
\|\widehat e(t)-e(t)\|=1
\]

for an initial residual in the second direction. Thus a broad all-time
stability argument cannot follow from PSD plus a small **absolute**
operator-norm kernel defect when learnable eigenvalues approach zero.
Relative spectral control or exact preservation of slow modes can evade the
example, and the example is not asserted to be a reachable canonical network
state.

### 6.6 Rare tails

Bounded \(\tanh\) removes the earlier quadratic Riccati/explosion branch.
No comparable rare-neuron no-go was found.

Gaussian tails still prevent deterministic uniform bounds over the entire
support and can create rare coherent readout/operator directions. They
necessitate high-probability or Orlicz-weighted statements, but they are not
currently an obstruction to every strong compiler.

### 6.7 Raw causal low rank and raw polynomial projection

Even the Volterra integration operator has singular values

\[
\sigma_k=\frac{2}{(2k-1)\pi}.
\]

Thus the unfactored causal kernel has only algebraic low-rank decay.

The numerical scalar response contractions showed the same slow trend:
the tenth singular value remained roughly \(3\%\)--\(4\%\) of the first.

A predetermined total-degree Legendre projection on the raw causal triangle
was also a poor approximation-theory diagnostic. With 66 coefficients, its
relative Frobenius errors were approximately:

| case | relative error |
|---|---:|
| iid generic | \(8.5\times10^{-2}\) |
| smooth generic | \(1.28\times10^{-2}\) |
| smooth nonnormal | \(1.66\times10^{-2}\) |

Those coefficients were fitted to exact finite-width snapshots and therefore
are not a compiler. The failure reinforces the need to factor the causal
boundary/Volterra primitive and certify the outgoing equation residual.

---

## 7. Numerical methodology and results

### 7.1 What was simulated

The reproducible CPU implementation trained every entry of
\[
B,\quad W_0,\ldots,W_{L-1},\quad a
\]
by the Euclidean flows (2.3)--(2.5).

The main ranges were:

- \(n=16,\ldots,40\);
- \(L=8,\ldots,128\);
- \(m=2,3,4\);
- multiple seeds and label scales;
- \(\phi_\alpha(z)=\tanh(\alpha z)/\alpha\) with
  \(\alpha=0.7,\ldots,1.4\);
- iid-depth and depth-regular Gaussian initializations;
- generic, nearly aligned, and coherent nonnormal cases;
- positive-time restarts, perturbed states, and perturbed labels.

Training used a second-order Heun method, usually with
\(\Delta t=0.025\). The response truncation retained chronological words in
the exact discrete adjoint product. Every numerical “sup” below is a maximum
over the recorded time/depth grid (time spacing \(0.05\)), not a certified
continuous-time supremum.

For each of the four main stress cases, the archive also exports the full
final-depth profiles of
\[
G^h(s),\qquad G^q(s),\qquad G^\beta(s)
\]
entry by entry in `gram_fields_*_final.csv`.

### 7.2 Scaling audit

| derivative | relative finite-difference error |
|---|---:|
| \(a\) | \(4.7\times10^{-10}\) |
| \(B\) | \(6.5\times10^{-9}\) |
| \(W_\ell\) | \(6.3\times10^{-9}\) |

The independent identity

\[
\dot f=-\Theta(f-y)
\]

matched to \(1.0\times10^{-8}\).

### 7.3 Depth initialization fork

| \(L\) | iid displacement | smooth-field displacement |
|---:|---:|---:|
| 8 | 0.1183 | 0.2879 |
| 16 | 0.0814 | 0.2897 |
| 32 | 0.0562 | 0.2906 |
| 64 | 0.0396 | 0.2911 |
| 128 | 0.0281 | 0.2913 |

The fitted iid exponent was \(-0.519\), consistent with \(L^{-1/2}\); the
smooth-field exponent was \(0.004\).

![Depth initialization scaling](results/depth_initialization_scaling.png)

### 7.4 Smooth-depth reference convergence

Against \(L=96\):

| \(L\) | \(\sup_t\|f_L-f_{96}\|\) | \(\sup_{t,s}\|G_L-G_{96}\|_F\) |
|---:|---:|---:|
| 12 | \(4.87\times10^{-3}\) | \(2.34\times10^{-2}\) |
| 24 | \(2.08\times10^{-3}\) | \(1.02\times10^{-2}\) |
| 48 | \(7.01\times10^{-4}\) | \(3.44\times10^{-3}\) |

This is consistent with convergence of the separate depth-regular
neural-ODE discretization in one seed and three resolutions. It is not an
iid-depth homogenization test, and \(L=96\) is a numerical reference rather
than a certified continuum solution.

### 7.5 Truncated-response training

The following are grid-maximum errors on \(0\le t\le1.6\), measured against
the full finite network. Every truncated run still retained the dense
matrices.

| case | order \(M\) | output error | all-depth Gram error |
|---|---:|---:|---:|
| smooth generic | 2 | \(1.47\times10^{-3}\) | \(6.05\times10^{-3}\) |
| smooth generic | 4 | \(2.82\times10^{-5}\) | \(1.06\times10^{-4}\) |
| smooth generic | 6 | \(9.11\times10^{-7}\) | \(1.41\times10^{-6}\) |
| iid generic | 4 | \(1.86\times10^{-7}\) | \(3.01\times10^{-7}\) |
| smooth nonnormal | 4 | \(2.97\times10^{-5}\) | \(3.92\times10^{-4}\) |
| smooth nonnormal | 6 | \(2.05\times10^{-6}\) | \(4.75\times10^{-6}\) |
| smooth aligned | 4 | \(1.58\times10^{-6}\) | \(1.17\times10^{-5}\) |

The generic trajectories were not lazy:

| case | maximum hidden-Gram motion | output motion |
|---|---:|---:|
| smooth generic | 1.028 | 1.147 |
| iid generic | 0.676 | 1.067 |
| smooth nonnormal | 1.064 | 1.189 |
| smooth aligned | 0.0084 | 0.0084 |

For the coherent nonnormal run,
\[
\max_{r,t}\frac1L\sum_\ell
\|D_{r,\ell}(t)W_\ell(t)\|_{\rm op}
\approx1.981.
\]
The safe order-four factorial tail is then about \(0.369\), enormously
larger than the observed \(2.97\times10^{-5}\) output error. Thus the
experiment demonstrates successful low word order, not a quantitatively
sharp a priori Dyson certificate.

![Truncated response training errors](results/truncated_training_errors.png)

### 7.6 Parameter sweep

Twelve order-four runs varied width, depth, sample count, seed, label scale,
activation gain, and depth initialization. The largest recorded errors were

\[
\max_{\rm recorded}\|f_M-f\|_2=3.38\times10^{-4},
\]

\[
\max_{\rm recorded}\|G_M-G\|_F=8.70\times10^{-4}.
\]

This is robustness evidence for the finite depth-word rule, not width
convergence.

### 7.7 Restarts

At a positive-time full-state restart with perturbed labels:

| \(M\) | output error | Gram error |
|---:|---:|---:|
| 2 | \(7.23\times10^{-4}\) | \(1.71\times10^{-3}\) |
| 4 | \(1.02\times10^{-5}\) | \(1.89\times10^{-5}\) |
| 6 | \(6.61\times10^{-8}\) | \(2.12\times10^{-7}\) |

A small perturbation of \(B,W\) produced essentially the same table. This
tests local-rule robustness, but it restarts from the full finite network
state rather than a compressed DMFT state.

### 7.8 Horizon test

For one well-conditioned smooth run, order \(M=4\) gave:

| horizon | output sup error | Gram sup error | residual \(L^1\) budget |
|---:|---:|---:|---:|
| 0.4 | \(1.48\times10^{-5}\) | \(1.39\times10^{-4}\) | 0.311 |
| 0.8 | \(1.48\times10^{-5}\) | \(1.39\times10^{-4}\) | 0.426 |
| 1.6 | \(1.48\times10^{-5}\) | \(1.39\times10^{-4}\) | 0.483 |
| 3.2 | \(1.48\times10^{-5}\) | \(1.39\times10^{-4}\) | 0.497 |

The plateau is encouraging: most error was created early and later frozen by
the small residual. It is also a prefix-sup effect on one coercive trajectory,
not evidence for every training horizon and restart. The displayed residual
\(L^1\) budget is a post-hoc trapezoidal integral along the reference
trajectory, not an a priori certificate.

### 7.9 Response singular values and raw Galerkin

![Response singular values](results/response_singular_value_decay.png)

![Triangular Galerkin diagnostic](results/triangular_galerkin_projection.png)

The raw contraction is full rank with slow decay. The raw polynomial
projection improves the smooth cases but largely stalls for iid depth. These
are explicit failed cases, not suppressed plots.

### 7.10 PSD diagnostic qualification

The code constructs a factorized PSD kernel from truncated sensitivity
features. It is correctly labelled `reconstructed_psd_kernel`.

The truncated-adjoint trajectory itself updates the unchanged full forward
network using an approximate adjoint. If \(S\) is the exact forward Jacobian
and \(S_M\) the truncated sensitivity, its actual instantaneous output rate
uses the cross-kernel

\[
SS_M^\top,
\]

not the reconstructed Gram

\[
S_MS_M^\top\succeq0.
\]

Therefore the positive eigenvalues in the archive verify the structural PSD
reconstruction mechanism; they do not prove that the diagnostic
truncated-adjoint flow is itself a gradient flow. A genuine compiler should
discretize the forward model and use its exact discrete adjoint.

### 7.11 What the simulations did not test

- no width convergence to the dense DMFT;
- no iid-depth homogenized reference;
- no finite approximation of \(C^h,C^\beta,R^h,R^\beta\);
- no outgoing macroscopic residual;
- no width-independent law/chaos/cubature state;
- no all-time operator budget \(C_A\);
- no direct transient-gain or pseudospectral measure for the nonnormal case;
- no time-step refinement;
- no certified continuous-depth solver;
- no long ill-conditioned run on its natural \(10^3\)-scale.

The computations are strong evidence for the chronological response mechanism,
not for the complete conjecture.

---

## 8. The final sharp conjecture

### 8.1 Quantitative input family

Fix \(m\le d\), \(\chi=\phi=\tanh\), and constants

\[
0<\kappa_x\le1\le K_x<\infty,\qquad
0<Y_{\max}<\infty.
\]

Let \(\mathfrak D_{m,d}\) be the nonempty, computably represented compact
family

\[
\mathfrak D_{m,d}=
\left\{
(G,y):
\begin{array}{l}
G=XX^\top\text{ for some }X\in\mathbb R^{m\times d},\\
\operatorname{diag}G=\mathbf1,\quad
\kappa_xI_m\preceq G\preceq K_xI_m,\\
\|y\|_2\le Y_{\max}
\end{array}
\right\}.
\tag{8.1}
\]

The entries of \(G,y\) are supplied by standard Cauchy names, and every
computability statement below is uniform relative to those names. Use
exactly the independent Gaussian initialization and unit-convention
Euclidean rates in Section 2.

### 8.2 Exact causal state and topology

The exact state is fixed before \(M\) is mentioned. Write training history in
age coordinates \(a=t-\tau\ge0\). Fix \(p>3\), \(q>4\), and
\(\omega(a)=(1+a)^{-q}\). Factor the known Heaviside/Volterra primitives from
every causal response before measuring its remainder.

Let
\[
\mathcal H_\omega
=L^2\!\left([0,1]\times\mathbb R_+,
\omega(a)\,ds\,da;\mathbb R^{k_m}\right)
\]
be the tagged-history space, where \(k_m<\infty\) lists the input-row,
readout, \(m\) forward coordinates, \(m\) adjoints, preactivations, and
messages. Let \(\mathcal H_\omega^+\) be weighted \(H^p\) with tail seminorm
\[
\|u\|_{\rm tail,\sigma}
=\sup_{R\ge1}R^\sigma
\|u\|_{H^p_\omega(\{a>R\})},
\qquad \sigma>0.
\]
On bounded sets with this tail seminorm,
\(\mathcal H_\omega^+\Subset\mathcal H_\omega\).

Let \(\mathscr H_\omega^0\) be the weighted \(L^2\) product on the explicit
domains
\[
[0,1]\times\mathbb R_+^2
\quad\text{for }C^h,C^\beta,
\]
\[
[0,1]\times\{0\le a\le b<\infty\}
\quad\text{for }R^h,R^\beta,
\]
and ordered depth simplices times their declared age variables for
\(\mathcal J\). Let \(\mathscr H_\omega^+\) replace each factored remainder
by weighted \(H^p\); for a \(k\)-word contraction on a growing-dimensional
simplex use dominating mixed smoothness \(H_{\rm mix}^p\), with \(p>2\) in
each physical coordinate. Include causal traces as explicit coordinates and
impose the analogous tail restriction norm in the sum of age variables. Let
\(\mathscr H_\omega^-\) be the corresponding negative-order extrapolation
product.

Enumerate the word, sample-label, and endpoint tuple by \(j\), with
\(|j|\) dominating both chronological length and label-word length. The base
contraction norm is
\[
\|\mathcal J\|_{\ell^2_\vartheta}^2
=\sum_j\vartheta^{2|j|}
\|\mathcal J_j\|_{\mathscr H_\omega^0}^2,
\qquad \vartheta>1,
\]
whereas the strong norm uses \(H_{\rm mix}^p\) and
\(\vartheta_+>\vartheta\). This strict weight gap prevents mass from escaping
to increasing response-word order and absorbs dimension-dependent
mixed-product constants.

For each \(D=(G,y)\), define the physical state

\[
Y=
\left(
\Pi,\,
C^h,\,
C^\beta,\,
R^h,\,
R^\beta,\,
\mu_{\rm depth},\,
\mathcal J,\,
\mathcal T
\right).
\tag{8.2}
\]

Here:

- \(\Pi\in\mathcal P_2(\mathcal H_\omega)\) is the tagged path law, with a
  declared uniform exponential moment;
- \(C^h,C^\beta\) are the two-training-time covariance kernels;
- \(R^h,R^\beta\) are both reciprocal causal Onsager responses;
- \(\mu_{\rm depth}\) is the homogenized iid-depth type/Young law,
  unconditionally included and allowed to be a degenerate point law;
- \(\mathcal J=(\mathcal J_{k,\alpha})\) is the \(M\)-independent
  chronological contraction sector defined as follows. Let
  \(\mathfrak A_m\) be the finite endpoint alphabet
  \[
  \{h_r,q_r,\beta_r,D_r\beta_q,\gamma_r:1\le r,q\le m\}.
  \]
  At fixed \(L\), set \(A_{r,\ell}=D_r^\ell W_\ell\). For every \(k\ge0\),
  endpoint pair, and finite sample-label word \(\alpha\), form every
  normalized discrete contraction
  \[
  \frac1n X^\top
  A_{\alpha_k,\ell_k}\cdots A_{\alpha_1,\ell_1}Y,
  \qquad
  0\le\ell_1<\cdots<\ell_k<L,
  \]
  and its two-training-time cavity/Onsager analogue. The component
  \(\mathcal J_{k,\alpha}\) is the \(n\to\infty\), then homogenized
  \(L\to\infty\), limit of the associated \(L^{-k}\) ordered-layer sums and
  type-marked contractions. No realized pointwise \(W(s)\) is introduced.
  This recursively enumerates every term generated by the discrete response
  and local Onsager equations; no subfamily is selected after seeing a
  trajectory;
- \(\mathcal T\) is exactly
  \[
  \bigl(f,G^h,G^\beta,G^\gamma,
  \operatorname{tr}_{a=b}R^h,
  \operatorname{tr}_{a=b}R^\beta,
  \operatorname{tr}_{s=u}\mathcal J\bigr).
  \]

At the canonical start, histories are padded for \(\tau<0\) by holding the
initial forward/adjoint variables constant, setting pre-zero learned-memory
integrals and causal responses to zero, and deriving covariances from that
padding. Restarting transports the full padded history; it does not repad at
the restart time.

The layer-type space is the Polish Hilbert product
\[
\mathsf T_{\rm layer}
=\mathbb R^{d_{\rm type}}
\times\ell^2(2^{-j}),
\qquad
\|(v,g)\|_{\mathsf T}^2
=\|v\|_2^2+\sum_{j\ge1}2^{-j}|g_j|^2,
\]
which carries the finite local marks and a countable Gaussian cavity seed.
Its compactly embedded strong space replaces \(2^{-j}\) by \(2^{-j/2}\).
The map \(s\mapsto\mu_{{\rm depth},s}\) is Borel measurable into
\(\mathcal P_2(\mathsf T_{\rm layer})\), and the strong class has the
analogous \((2+\delta)\)-moment bound in the strong type norm.

For the Young law use
\[
d_{\rm Young}(\mu,\widetilde\mu)^2
=\int_0^1W_2(\mu_s,\widetilde\mu_s)^2\,ds.
\]
The trace norm is
\[
\begin{aligned}
\|\mathcal T-\widetilde{\mathcal T}\|_{\rm trace}
:={}&
\|f-\widetilde f\|_2
+\sup_s\left(
\|G^h(s)-\widetilde G^h(s)\|_F
+\|G^\beta(s)-\widetilde G^\beta(s)\|_F
\right)\\
&+\|G^\gamma-\widetilde G^\gamma\|_F
+\sum_{\text{covariance/Onsager faces}}
\|\operatorname{tr}K-\operatorname{tr}\widetilde K\|_
{H^{p-1/2}_\omega}\\
&+\left[
\sum_j\vartheta^{2|j|}
\|\operatorname{tr}\mathcal J_j
-\operatorname{tr}\widetilde{\mathcal J}_j\|_
{H_{\rm mix}^{p-1/2}}^2
\right]^{1/2}.
\end{aligned}
\]

The base metric is

\[
\begin{aligned}
d_{\mathcal X_D}(Y,\widetilde Y)
:={}&
W_2(\Pi,\widetilde\Pi)
+\|C^h-\widetilde C^h\|_{\mathscr H_\omega^0}
+\|C^\beta-\widetilde C^\beta\|_{\mathscr H_\omega^0}\\
&+\|R^h-\widetilde R^h\|_{\mathscr H_\omega^0}
+\|R^\beta-\widetilde R^\beta\|_{\mathscr H_\omega^0}
+d_{\rm Young}(\mu_{\rm depth},\widetilde\mu_{\rm depth})\\
&+\|\mathcal J-\widetilde{\mathcal J}\|
_{\ell^2_\vartheta(\mathscr H_\omega^0)}
+\|\mathcal T-\widetilde{\mathcal T}\|_{\rm trace}.
\end{aligned}
\tag{8.3}
\]

The strong space \(\mathcal X_D^+\) uses
\(\mathscr H_\omega^+\), the \(\vartheta_+\)-weighted contraction norm, and
the exponential-moment and tail moduli; the
kernel extrapolation components use \(\mathscr H_\omega^-\).

To place law and kernel velocities in one linear space, let
\(\mathcal B_\alpha\) be the completion of smooth cylinder functions
\(\psi\) on \(\mathcal H_\omega\) under
\[
\|\psi\|_{\mathcal B_\alpha}
=
\sup_z e^{-\alpha\|z\|_{\mathcal H_\omega}^2}
\left(
|\psi(z)|+\|D\psi(z)\|_{\mathcal H_\omega^*}
\right),
\]
and use the separating dual norm for an arbitrary continuous linear
functional \(\ell\),
\[
\|\ell\|_{\mathcal B_\alpha^*}
=
\sup_{\|\psi\|_{\mathcal B_\alpha}\le1}
\left|\ell(\psi)\right|.
\]
Signed-measure differences are a subclass. Transport velocities are the
order-one distributions
\[
\ell_v(\psi)=\int D\psi(u)[v(u)]\,d\Pi(u).
\]
Require
\[
\int e^{\beta\|u\|_{\mathcal H_\omega}^2}\,d\Pi(u)\le B,
\qquad \beta>\alpha,
\]
and the corresponding weighted \(L^2(\Pi)\) bound on \(v\), ensuring
\(\ell_v\in\mathcal B_\alpha^*\). Use the analogous depth-integrated dual for
the Young law. The common linear extrapolation product is
\[
\mathbb X_D^-
=
\mathcal B_\alpha^*
\times\mathscr H_\omega^-
\times\mathscr H_\omega^-
\times\cdots,
\]
including the explicit trace/coherent-contraction coordinates. Law
equations are interpreted weakly against \(\mathcal B_\alpha\).

The strong law class additionally requires, for fixed \(\delta,\sigma>0\),
\[
\int\left(
\|u\|_{\mathcal H_\omega^+}^{2+\delta}
+\|u\|_{\rm tail,\sigma}^{2+\delta}
\right)d\Pi(u)\le B_{\rm law},
\tag{8.4a}
\]
and the analogous compactly coercive moment/tail bound for
\(\mu_{\rm depth}\). Since
\(\mathcal H_\omega^+\Subset\mathcal H_\omega\), (8.4a) gives uniform
tightness plus uniform integrability of second moments, hence
\(W_2\)-precompactness. Combined with the kernel tail bounds, bounded strong
classes are compact in \(\mathcal X_D\). This compact embedding, rather than
an open ball in an infinite-dimensional norm, is the approximation
compactness used below.

The exact local generator is data-fibred,

\[
\mathcal F_D:D(\mathcal F_D)\subset\mathcal X_D
\longrightarrow\mathbb X_D^-,
\]

and contains the age-shift generator, the local forward/adjoint equations,
both learned memories (4.6)--(4.7), reciprocal response equations, and the
depth-homogenization equation. The universal causal shift/trace primitive is
kept explicit. In age coordinates the generator is decomposed as
\[
\mathcal F_D(Y)
=\mathcal K_D(Y)
+\mathcal N_D(Y)\bigl(f(Y)-y\bigr),
\]
where \(\mathcal K_D\) is the exact kinematic history shift and boundary
injection for a frozen current state. The compiler represents
\(\mathcal K_D\) exactly; only the residual-gated physical update is
approximated. The state (8.2) is independent of \(M\). Appending a decoupled
infinite coordinate is declared the same physical representation and cannot
alter the norm or conjecture; conversely, continuation-relevant response
coordinates cannot be quotiented away.

### 8.3 Admissible finite systems and provenance

Fix once and for all a typed finite-expression grammar \(\mathscr G\) and a
sound finite verifier \(V\). Its base symbols are the entries of \(D\), the
Gaussian initialization law, \(\tanh\) and its derivatives, the components
of (8.2), rational/algebraic constants, and interval enclosures. The finite
abstract syntax is
\[
\begin{aligned}
\mathrm{Type}::={}&
\mathrm{Sample}[m]\mid\mathrm{Depth}\mid\mathrm{Age}\mid
\mathrm{LayerType}\mid\mathrm{Word}[0{:}K]\mid
\mathrm{Mode}[0{:}N],\\
\mathrm{Expr}::={}&
\mathrm{FixedConst}\mid\mathrm{CertifiedScalar}[\pi]
\mid D[i,j]\mid\mathrm{InitMoment}[\alpha]\mid
\mathrm{Field}[\mathrm{typed\ coordinates}]\\
&\mid\tanh^{(r)}(\mathrm{Expr})
\mid \mathrm{Expr}\pm\mathrm{Expr}
\mid \mathrm{Expr}\,\mathrm{Expr}\\
&\mid\partial_{\mathrm{Depth/Age}}\mathrm{Expr}
\mid\int_{\mathrm{Depth/Age/LayerType}}\mathrm{Expr}\\
&\mid\mathrm{PositiveQuadrature}(\mathrm{Expr})
\mid\mathrm{Galerkin}_{\mathcal B_N}(\mathrm{Expr})
\mid\mathrm{AutoDiff}(\mathrm{Expr}).
\end{aligned}
\tag{8.4b}
\]
Here \(K,N<\infty\) in every artifact emitted at accuracy \(M\), and
\(\mathcal B_N\) is a finitely listed member of the public catalogue of
Legendre/Hermite polynomials and rational finite elements. Conditional
Gaussian expectations and interval-certified finite linear solves are
derived macros with finite expression trees. Continuum coordinates may only
have the physical types Depth, Age, or LayerType; no synthetic coding
coordinate is present. A coordinate change is admissible only if it is
type-preserving, arity-preserving, computably bi-Lipschitz, and verifier
certified.

The grammar assigns provenance types—sample, depth, age, layer type, response
word, and basis mode—to every index. It rejects:

- arbitrary real constants or opaque callable code;
- exact positive-time solution queries or positive-time finite-network
  samples used as future training data;
- target-generated bases, modes, decoders, or readouts;
- an absolute-time playback clock without a projected macroscopic
  coordinate;
- a free dynamic block with two accuracy-dependent microscopic/neuron
  indices, even after flattening.

No field may carry an undeclared infinite coefficient sequence or an
unbounded Word/Mode range. All emitted artifacts—not only scalar
coefficients—must be finite syntax trees in \(\mathscr G\) with a checked
provenance derivation. `FixedConst` is the finite architecture vocabulary
\(\{0,\pm1,2\}\). Every other rational/algebraic literal, interval endpoint,
basis index, mesh, mode count, branch, and AST node must be the conclusion of
a checked provenance inference rule. Its derivation DAG may use only
\(M,D\), initialization moments, declared class constants, local generator
evaluations, residual/tube estimates, and previously certified
reduced-system quantities. There is no unconstrained literal or structural
choice rule, and the verifier checks the complete DAG rather than only the
final expression's type.

A single parametric call

\[
\mathcal C(M,\cdot)
\]

emits a symbolic \(D\)-parametric family of restart-independent, globally
well-posed autonomous templates \(\mathcal P_M^D\); specializing the frozen
parameter gives the template for a Cauchy-named \(D\). It consists of finitely
many scalar states and finitely many finite-order PDE/integral fields on
explicitly declared finite-dimensional, rationally compactified source
domains. ODEs and finite-basis Galerkin systems are special cases. It also
emits

\[
P_M^D:\mathcal X_D\to\mathcal Z_M^D,\qquad
R_M^D:\mathcal Z_M^D\to D(\mathcal F_D),
\]

and a state-only readout
\[
\widehat{\mathcal O}_M^D:
\mathcal Z_M^D\to
E:=\mathbb R^m\times C([0,1];\mathbb S_+^m),
\quad
\|(f,G)\|_E=\|f\|_2+\sup_s\|G(s)\|_F.
\]

The projection consists only of declared local moment, marginal, basis, and
response-contraction operations. \(P_M^D\), \(R_M^D\), and the readout are
uniformly continuous with verified moduli; \(R_M^D\) is \(C^1\) into the
ambient linear product \(\mathbb X_D^-\), has image in the generator domain,
and has a verified derivative bound. The template, maps, basis, and
certificate depend on \((M,D)\), never on a restart state or restart time.
Restarting from \(Y\) only sets \(z(0)=P_M^DY\).

The number of fields, source coordinates, modes, scalar states, and the
description length may depend on
\(M,m,d,\kappa_x,K_x,Y_{\max}\), but not on \(n,L\), restart time, or a
requested training horizon.

### 8.4 Outgoing residual, PSD kernel, and certificate

Write the reduced generator as \(F_M^D\). On a compiler-certified invariant
tube \(\mathfrak T_M^D\), and for the restart sets \(K_D\) specified in Part
B below, define

\[
\eta_M
=\sup_{D\in\mathfrak D_{m,d}}
\sup_{Y\in K_D}
d_{\mathcal X_D}(R_M^DP_M^DY,Y),
\tag{8.4}
\]

\[
\mathfrak r_M^D(z)
=D R_M^D(z)F_M^D(z)
-\mathcal F_D(R_M^Dz)
\in\mathbb X_D^-.
\tag{8.5}
\]

The known age-shift/causal primitive is represented exactly. The law
component of (8.5) is a continuous distributional velocity in
\(\mathcal B_\alpha^*\); no subtraction of points in a Wasserstein space is
used. The remaining outgoing residual is required to be residual-gated:

\[
\|\mathfrak r_M^D(z)\|_{\mathbb X_D^-}
\le
\bar r_M\,
\|\widehat f_M^D(z)-y\|_2,
\qquad z\in\mathfrak T_M^D,
\tag{8.6}
\]

with zero residual when the right side is zero. The
\(\mathbb X_D^-\) norm is unweighted in future relative time and retains
the explicit trace/coherent-contraction coordinates; a delayed \(O(1)\)
pulse cannot be hidden by an age weight.

Because \(R_M^D\) maps into \(D(\mathcal F_D)\), all causal boundary and
trace conditions hold exactly. Covariance, response, type-law, nonlinear
high-to-low, and depth-tail errors are components of the single outgoing
residual (8.5), measured in their declared dual/Sobolev/trace coordinates.
For example, a Dyson implementation may use \(R_K(C_*)\), with a
verifier-certified horizon-independent \(C_*\), to bound the corresponding
response component of \(\bar r_M\). No separate defect is allowed to act as
an ungated persistent forcing.

The state-only readout defect is defined by
\[
\sup_{D\in\mathfrak D_{m,d}}
\sup_{z\in\mathfrak T_M^D}
\left\|
\widehat{\mathcal O}_M^D(z)
-\mathcal O_D(R_M^Dz)
\right\|_E
\le\bar\zeta_M.
\tag{8.6a}
\]

The compiler also proves the unweighted residual budget
\[
\sup_{D\in\mathfrak D_{m,d}}\sup_{Y\in K_D}
\int_0^\infty
\|\widehat f_M^D(\Phi_{M,t}^DP_M^DY)-y\|_2\,dt
\le B_e
\tag{8.6b}
\]
and an interval-certified common invariant tube. No term in these
inequalities is a distance to the unknown exact positive-time law. The
verifier bounds \(\eta_M\) from the declared compact regularity class rather
than sampling exact future states.

The finite forward surrogate and its adjoint must be the same system. If
\(\mathsf S_M\) is its exact output Jacobian and \(\mathsf A_M\succeq0\) is
the Galerkin pullback of the locked Euclidean block metric, then

\[
\Theta_M
=\mathsf S_M\mathsf A_M\mathsf S_M^\top
\succeq0.
\tag{8.7}
\]

Positive depth quadrature is part of \(\mathsf A_M\). The same reduced output
must obey

\[
D\widehat f_M^D(z)F_M^D(z)
=-\Theta_M(z)(\widehat f_M^D(z)-y)
\tag{8.8}
\]

exactly. A free Cholesky factor unrelated to the reduced dynamics does not
qualify.

The exact certificate is the rational bound

\[
\boxed{
\rho_M
=
\bar\eta_M+\bar\zeta_M+B_e\bar r_M.
}
\tag{8.9}
\]

Here \(\bar\eta_M\ge\eta_M\), and every quantity is verifier-certified from
legal inputs, local equations, the approximate invariant tube, and the
strong class constants. Verifier soundness must prove the
residual-to-observable inequality
\[
\sup_{D\in\mathfrak D_{m,d}}\sup_{Y\in K_D}\sup_{\tau\ge0}
\left\|
\widehat{\mathcal O}_M^D
(\Phi_{M,\tau}^DP_M^DY)
-\mathcal O_D(S_\tau^DY)
\right\|_E
\le\bar\Gamma\rho_M,
\tag{8.9a}
\]
not merely emit a number called a stability gain. The compiler emits a
parametric finite proof \(\pi_M\), rational bounds
\(B_e,\bar\Gamma\ge1\), a
class-uniform rational \(q_M\ge\rho_M\), and an effective modulus
\[
N:\mathbb Q_{>0}\to\mathbb N,\qquad
M\ge N(\epsilon)\Longrightarrow q_M\le\epsilon.
\tag{8.10}
\]
Verifier soundness is the formal implication
\[
V(M,\pi_M,q_M)=\mathrm{accept}
\Longrightarrow
\text{(8.9a) holds for all }
D\in\mathfrak D_{m,d},\ Y\in K_D,\ \tau\ge0.
\tag{8.10d}
\]

### 8.5 Conjecture

> **Canonical iid-depth dense Euclidean \(\mu\)P certified
> finite-causal-PDE conjecture.**
>
> Fix the model, data family, state representation, and admissibility
> semantics in Sections 8.1--8.4.
>
> **A. Exact target.** Define the finite responses operationally by adding
> deterministic source fields
> \[
> z_r^\ell(t)\mapsto z_r^\ell(t)+\varepsilon\xi_{r,\ell}^h(t),
> \qquad
> W_\ell^\top\beta_r^\ell(t)
> \mapsto
> W_\ell^\top\beta_r^\ell(t)
> +\varepsilon\xi_{r,\ell}^\beta(t)
> \]
> to the forward preactivation and backward field. At \(\varepsilon=0\),
> take the normalized trace Fréchet derivatives
> \[
> R^{h,\ell}_{rq}(t,\tau)
> =\frac1n\sum_i
> \frac{\delta h_{r,i}^\ell(t)}
> {\delta\xi_{q,\ell,i}^h(\tau)},
> \qquad
> R^{\beta,\ell}_{rq}(t,\tau)
> =\frac1n\sum_i
> \frac{\delta\beta_{r,i}^\ell(t)}
> {\delta\xi_{q,\ell,i}^\beta(\tau)}.
> \tag{8.10e}
> \]
> They are zero for \(t<\tau\), and the causal diagonal is the right trace
> determined by the direct source insertion. Let \(\mathcal E_{n,L}\) map a
> finite-network history, together with (8.10e), to its empirical tagged
> law, two-time covariances, responses, the discrete ordered contractions
> defining \(\mathcal J^{(L)}\), and trace fields in
> \(\mathcal X_D^{(L)}\). For every fixed \(L,T,\epsilon>0\),
> there is a unique fixed-\(L\) causal DMFT \(Y_{L,D}\), containing both
> reciprocal Onsager responses, such that
> \[
> \lim_{n\to\infty}
> \Pr\!\left[
> \sup_{0\le t\le T}
> d_{\mathcal X_D^{(L)}}
> \bigl(\mathcal E_{n,L}(t),Y_{L,D}(t)\bigr)
> >\epsilon
> \right]=0.
> \tag{8.10a}
> \]
> Let \(\mathcal I_L\) be the declared piecewise-depth interpolation plus
> type-law embedding. There is a unique homogenized state \(Y_D\) such that
> \[
> \sup_{0\le t\le T}
> d_{\mathcal X_D}
> \bigl(\mathcal I_LY_{L,D}(t),Y_D(t)\bigr)
> \longrightarrow0,
> \tag{8.10b}
> \]
> and the corresponding output/Gram readouts converge in \(C([0,T];E)\).
> For each \(D\), \(\mathcal F_D\) defines a unique global
> history-restartable semigroup \(S_t^D\), and
> \(\mathcal O_D(Y)=(f(Y),G_Y(\cdot))\) is continuous
> \(\mathcal X_D\to E\).
>
> **B. Restart class.** There are class constants and an explicitly
> described physically consistent set \(K_D\subset\mathcal X_D^+\),
> uniformly compact in \(\mathcal X_D\), invariant under \(S_t^D\), and
> containing every canonical state \(S_{t_0}^DY_D^0\). It also contains a
> fixed-radius class of perturbations measured in the stronger
> \(\mathcal X_D^+\) norm, subject to the DMFT covariance, response,
> boundary, type-law, moment, and tail identities. It is not an open ball in
> \(\mathcal X_D\). More precisely, a fixed separable physical perturbation
> space \(U_D\) contains independent smooth cylinder pushforwards of
> \(\Pi\), covariance/response basis perturbations, and current-trace
> perturbations. For every canonical \(Y\) there is a chart
> \[
> \Psi_{D,Y}:B_{U_D}(0,r)\to K_D,\qquad r>0,
> \tag{8.10c}
> \]
> with \(\Psi_{D,Y}(0)=Y\), injective derivative, and uniform upper/lower
> bounds in the strong norm. The embedding of the chart image into
> \(\mathcal X_D\) is compact. Thus the restart test is nonvacuous but does
> not demand impossible uniform approximation of an open weak-norm ball.
>
> **C. Finite compiler.** There exists one admissible compiler
> \(\mathcal C\) and one sound verifier \(V\) that produce
> (8.4)--(8.10). The verifier accepts every emitted proof, the constants
> \(B_e,\bar\Gamma\) depend only on the declared class constants, and
> \(q_M\to0\) effectively.
>
> **D. Certified convergence.** Uniformly over
> \(D\in\mathfrak D_{m,d}\), restart states \(Y\in K_D\), and relative
> training time \(\tau\ge0\),
> \[
> \boxed{
> \sup_{\tau\ge0}
> \left\|
> \widehat{\mathcal O}_M^D
> \bigl(\Phi_{M,\tau}^D(P_M^DY)\bigr)
> -
> \mathcal O_D(S_\tau^DY)
> \right\|_E
> \le \bar\Gamma q_M .
> }
> \tag{8.11}
> \]
> The finite template and proof are compiled before \(Y\) and \(t_0\) are
> supplied. The rational stability bounds \(B_e,\bar\Gamma\) do not depend on
> \(n,L,M,D,Y,t_0\), or a physical horizon. The finite template depends on
> \(M,D\), and the certified error \(q_M\) depends on \(M\).

The order of limits is

\[
\boxed{
n\to\infty\text{ at fixed }L
\quad\longrightarrow\quad
L\to\infty
\quad\longrightarrow\quad
M\to\infty.
}
\tag{8.12}
\]

No commutation or diagonal joint limit is part of the conjecture.

### 8.6 Evidence-backed finite-time and classical variants

The presently better-supported statement replaces (8.11) by

\[
\sup_{0\le\tau\le T}
\|\mathcal O_M(\tau)-\mathcal O(\tau)\|_E
\le\Gamma_T\rho_{M,T},
\tag{8.13}
\]

where \(M,\Gamma_T\) may depend on \(T\). Bounded activation, finite-time
energy estimates, and the Dyson tail give a credible route to (8.13) after
the exact causal state is constructed.

Equation (8.13) does not resolve the horizon-independent question.

If the intended object is specifically (3.1)--(3.5), replace iid layer
initialization by a depth-regular Gaussian matrix process with declared
covariance \(K_W(s,u)\). Use the same compiler definition but the order

\[
L\to\infty\text{ first},\qquad n\to\infty\text{ second}.
\]

This remains fully dense and Euclidean. It is a different initialization law
and must not be substituted for the canonical iid conjecture.

---

## 9. Equivalence to the desired certified finite-PDE claim

Define the **certified local macroscopic finite-PDE property** to be the
existence of the exact restartable state and an admissible compiler satisfying
Sections 8.1--8.4 and (8.11). This is the non-oracular
accuracy-dependent-PDE claim studied here; bare finite-curve approximation is
not.

If the conjecture holds, given rational \(\varepsilon>0\), the effective
modulus returns finite
\[
M\ge N(\varepsilon/\bar\Gamma).
\]

The compiler then returns one finite autonomous system, finite readouts, and
a sensitivity-consistent PSD kernel whose fields and source dimensions are
independent of \(n,L\), restart time, and requested horizon. Equation (8.11)
gives

\[
\sup_{\tau\ge0}
\|\widehat{\mathcal O}_M(\tau)-\mathcal O(\tau)\|_E
\le\varepsilon.
\]

Conversely, any proof of the certified local macroscopic finite-PDE property
instantiates Parts A--D verbatim. Therefore the conjecture is the desired
certified existence claim itself, not an auxiliary response-tail lemma.

A bare statement that “some finite system approximates one fixed curve” does
not imply this property and is intentionally excluded: it need not be
computable, local, restartable, residual-certified, or
sensitivity-consistent. A disproof based only on one basis, one moment
hierarchy, or one raw matrix-rank notion likewise does not negate (8.11).
Admissibility is invariant under certified typed bi-Lipschitz coordinate
changes, so a mere choice of notation or flattening cannot settle the
conjecture.

---

## 10. Mandatory anti-loophole audit

| Loophole | Clause that excludes it |
|---|---|
| Orthogonal, quotient, natural-gradient, or projected optimizer | The exact generator is the Euclidean target (2.3)--(2.5); a changed vector field has nonzero outgoing residual |
| Frozen, ridge-particle, diagonal, low-rank, or full microscopic surrogate | Provenance types reject accuracy-dependent neuron-pair blocks; flattening preserves their type |
| Full \(n\times n\) \(W\) or \(J\) retained | Every emitted field/source type and description is independent of \(n,L\) |
| Infinite DMFT renamed a finite PDE | Word/Mode ranges are finite, continuum sources come only from the physical whitelist, and undeclared coefficient sequences are forbidden |
| Future hidden in constants, modes, decoder, initial real, or callable code | The grammar and verifier cover every artifact, permit no opaque code/arbitrary real, and compile before the restart |
| Absolute time or target-reaching time used as playback | No unprojected clock has a provenance type; the same autonomous template must restart from every \(Y\in K_D\) |
| Arbitrary ODE packed into one PDE field | Local \(P_M,R_M\), outgoing residual (8.5)--(8.6), and verifier soundness are coordinate-invariant obligations |
| One canonical initialization curve | Uniformity covers \(\mathfrak D_{m,d}\) and a physically consistent strong-regularity perturbation class |
| Impossible open infinite-dimensional restart ball | \(K_D\) is uniformly compact in the approximation metric through \(\mathcal X_D^+\hookrightarrow\mathcal X_D\) |
| Formal Dyson or finitely many Taylor coefficients | Their error must enter the full law/Onsager outgoing residual (8.5), the gated bound (8.6), and the stability proof |
| Weak row/Frobenius/\(L^2\) defect with high-to-low leakage | The extrapolation norm retains trace and coherent-contraction coordinates, and the defect is residual-gated with an unweighted \(L^1\) budget |
| Free PSD matrix unrelated to the evolution | Equations (8.7)--(8.8) require the exact Jacobian/adjoint of the same surrogate |
| Assumed coercivity, tail, or stability | \(V\) accepts interval proofs of the invariant tube, residual budget, and rational \(\bar\Gamma\); these are not premises supplied by the user |
| Fixed finite-time theorem advertised as all-time | The main statement takes \(\sup_{\tau\ge0}\); (8.13) is separately labelled weaker |
| Smooth-depth variant substituted for iid depth | The stochastic limit mode and order (8.12) fix the literal iid target |
| Irrelevant decoupled state appended to defeat projection | The physical state is fixed by (8.2); decoupled augmentations are representation-equivalent and ignored |

Universal computation cannot be prohibited by the syntax of a finite ODE
alone. The combination of typed local provenance, continuous
projection/reconstruction, a compact restart class, an outgoing residual, and
one restart-independent proof-carrying template is what closes the oracle
loophole.

---

## 11. Ranked remaining mathematical lemmas

### Tier 1: define the canonical target

1. **Fixed-\(L\) dense causal-DMFT theorem.** Prove the continuous-training
   width limit with both reciprocal Onsager responses.
2. **Iid depth-homogenization theorem.** Take \(L\to\infty\) in that DMFT and
   identify \(\mu_{\rm depth}\), the topology, and the local equations.
3. **Global history-state well-posedness.** Prove uniqueness, semigroup
   restartability, and continuity of output/Gram readouts.

### Tier 2: finite-time compression

4. **Strong state/forcing topology.** Make every causal trace, coherent
   action, contraction, Gram, and kernel locally continuous.
5. **Depth-response residual theorem.** Combine the factorial word tail with
   a boundary-factored causal approximation.
6. **Training-time law/response Galerkin theorem.** Approximate
   \(C^h,C^\beta,R^h,R^\beta,\mu_{\rm depth}\) and compute
   their components of the outgoing bound \(\bar r_M\) without exact future
   data.
7. **Nonlinear feedback theorem.** Close response
   \(\to\) feature \(\to\) adjoint/kernel \(\to\) response in the same norm.
8. **PSD discretize-then-adjoint theorem.** Build one consistent approximate
   forward model and prove that its sensitivity Gram has the certified kernel
   defect.

### Tier 3: all-time step

9. **Uniform response budget.** Prove
   \[
   \sup_{t\ge0,r}
   \int_0^1\|D_r(s,t)W(s,t)\|_{\rm op}\,ds<\infty
   \]
   or the correct iid-homogenized analogue.
10. **Finite feature arclength or integrated observability.** Derive a
    horizon-free residual budget from the standard Euclidean dynamics.
11. **Slow-mode/conditioning theorem.** Prove a uniform kernel gap, a
    relative spectral approximation, or exact preservation of every
    learnable null/slow direction.
12. **Terminal hidden-Gram stability.** Control neutral zero-loss directions.
13. **Uniform restart tube.** Prove the same estimates on the explicit
    compact strong-regularity perturbation class \(K_D\).

### Tier 4: quantitative rates and stronger numerics

14. Establish Sobolev/analytic regularity after factoring the causal
    primitive and derive Kolmogorov-width rates.
15. Measure \(C_A(t)\), actual outgoing residuals, and adaptive required mode
    counts over long, ill-conditioned trajectories.
16. Demonstrate width convergence and replace all retained dense matrices by
    an actual finite law/response surrogate.
17. Add time-step and continuum-solver refinement and test initialization-law
    perturbations.

The first eight lemmas are needed even for a convincing finite-\(T\) theorem.
Lemmas 9--13 are the decisive horizon-independent frontier.

---

## 12. Final classification

| Status | Result |
|---|---|
| **Proved** | finite-\((n,L)\) gradients, rates \(n,n,L\), PSD kernel, energy identity |
| **Proved** | exact dense-matrix memory identities (4.5)--(4.7) |
| **Proved** | at fixed width, the raw iid step-weight interpolants fail strong depth-\(L^2\) translation compactness; the initialization displacement has normalized RMS at most \(L^{-1/2}\) |
| **Proved** | operator-norm Dyson tail under the stated integrated norm budget, including nonnormal/noncommuting cases |
| **Proved** | no width-independent neuron-coordinate operator-norm low-rank approximation of full \(J\) under a finite integrated generator budget; this does not obstruct observable contractions |
| **Proved with scope** | the continuation witness defeats one-depth exact closure on restart classes containing it; unweighted weak norms fail for traces/coherent contractions; eigenvalues alone miss nonnormal growth; PSD plus absolute kernel error gives no all-time modulus near vanishing slow modes |
| **Strongly supported numerically** | low finite depth-word order for the tested finite networks, including \(O(1)\) feature motion and one coherent rank-one nonnormal perturbation |
| **Numerically consistent** | convergence of the separate depth-regular discretization in one seed and three resolutions |
| **Plausible but conditional** | a finite-\(T\) response/DMFT Galerkin theorem after constructing the exact causal state |
| **Conjectural** | existence and global uniqueness of the literal iid-depth homogenized DMFT |
| **Conjectural** | a non-oracular finite approximation of its full training-time law/response state |
| **Conjectural and not yet strongly supported** | one \(M(\varepsilon)\) working uniformly for all training time and all declared restarts |
| **Unjustified/falsified literally** | raw iid step weights converge strongly to a nondegenerate realized pointwise control; an emergent effective representation is not ruled out |
| **Falsified/qualified** | raw causal response is exponentially low rank |
| **Falsified/qualified** | current short-horizon plateau or unfitted aligned case is overwhelming all-time evidence |

The final research verdict is:

\[
\boxed{
\begin{array}{c}
\text{Continuous depth supplies a compelling finite-horizon chronological}\\
\text{response-compression mechanism for dense Euclidean feature learning,}\\
\text{but the canonical iid-depth DMFT, its finite law/response compiler,}\\
\text{and the all-time stability budget remain unresolved.}
\end{array}
}
\]

The conjecture in Section 8 is tight enough that proving it gives the desired
accuracy-dependent finite neural PDE, while disproving only a moment closure,
one basis, low matrix rank, or a finite-time scheme does not.

---

## 13. Reproducibility map

The accompanying archive contains:

- `REPRODUCE.md` and `requirements.txt`;
- `src/run_dense_resnet_audit.py` — finite model, exact adjoint, response-word
  truncation, training, restarts, horizon tests, and parameter sweep;
- `src/run_response_galerkin_projection.py` — raw triangular projection
  diagnostic;
- `results/scaling_audit.json`;
- convergence and robustness CSV tables;
- response singular values;
- all generated plots;
- the independent theory, hostile, code-audit, and synthesis reports.

The numerical archive is evidence, not a proof certificate for (8.7).
