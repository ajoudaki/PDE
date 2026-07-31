# Hostile audit of the standard dense Euclidean continuous-depth \(\mu\)P finite-response-PDE claim

## Executive verdict

I tried to falsify the proposed accuracy-dependent finite compiler rather than to improve a preferred construction. The outcome is mixed and fairly sharp.

1. **Exact closure by the current forward state, adjoint, one-depth row laws, and their Gram fields is false.** There is an explicit \(O(n^{-1})\)-per-entry coherent rank-one perturbation of a dense weight matrix that is invisible to all of those quantities but changes the immediate training-time derivative of a hidden Gram by \(O(1)\). The missing datum is precisely a causal response action.
2. **A width-independent low-rank approximation of the full neuron-space Jacobian \(J(s,u)\) is impossible.** Since \(J(u,u)=I_n\) and \(J\) is invertible, all of its singular values stay bounded below whenever the depth-integrated generator norm is bounded. Any rank \(M<n\) approximation then has \(O(1)\) operator-norm error. Any positive result must compress only the finitely many normalized contractions of \(J\), or its dependence on depth/path variables, not \(J\) as an \(n\times n\) operator.
3. **Nonnormality does not invalidate the genuine operator-norm Dyson bound.** If
   \[
   C_A=\sup_{r,t}\int_0^1\|D_r(s,t)W(s,t)\|_{\rm op}\,ds<\infty,
   \]
   then the chronological tail is bounded by
   \[
   \sum_{k>M}C_A^k/k!
   \]
   without any commutativity or normality assumption. Nonnormal examples invalidate eigenvalue-based, average-Gram-based, and naive singular-decay arguments, but not this norm-based estimate. The real unproved issue is a horizon-independent certificate for \(C_A\) and stability of the nonlinear feedback loop.
4. **Weak Galerkin residuals are unsafe.** Vanishing entrywise, row-law, normalized-Frobenius, or unweighted \(L^2\) error can contract with coherent feature/adjoint directions to produce an \(O(1)\) Gram or kernel error. High depth modes can also multiply back into the constant mode. The residual norm must control the actual dynamically generated contractions, diagonal traces, and outgoing nonlinear flux.
5. **Positive semidefiniteness is not enough for all-time accuracy.** A sequence of PSD tangent kernels can converge in absolute norm while losing a small but essential eigenvalue. On a family whose smallest learnable eigenvalue approaches zero, the finite-time error vanishes but the uniform-in-time output error remains \(O(1)\). A uniform all-time theorem requires quantitative coercivity, an equivalent integrated-observability condition, or an exact preservation of nullspaces and slow directions.
6. **The quadratic/Gaussian rare-tail catastrophe in the project notes does not transfer to residual \(\tanh\) by the same argument.** Bounded forward activations remove the Riccati branch used there. I found no analogous rare-neuron blow-up for the stated bounded model. Gaussian tails still prevent deterministic pathwise bounds over the entire support and make the \(L,n\) joint regime and restart topology important, but they are not presently a no-go theorem.
7. **The proposed all-time compiler statement is currently both under-specified and, over a natural broad data class, too strong.** “Constructive,” “non-oracular,” “compact nondegenerate,” “finite PDE,” and “residual certificate” need effective definitions. Without them, exact-curve coefficients or an arbitrary finite ODE can satisfy the syntax. Without a uniform learnability/finite-arclength condition, the all-time estimate is false uniformly even for elementary PSD kernel dynamics.
8. **I did not obtain an obstruction to every admissible accuracy-dependent finite compiler.** The continuation witness refutes exact one-depth summaries; the high-to-low examples refute particular norms and projections; the conditioning example refutes overly broad uniform classes. None gives a lower bound on the Kolmogorov widths of every observable-relevant causal state in a strong stability norm. Under a genuinely uniform operator bound, response regularity, coercivity, and a computed outgoing residual, a response-Galerkin theorem remains mathematically plausible.

The correct hostile conclusion is therefore:

\[
\boxed{
\begin{array}{c}
\text{naive one-depth closure and neuron-low-rank response are false;}\\
\text{the all-time certified response-Galerkin claim is open, not disproved,}\\
\text{but only after substantial anti-oracle and stability repairs.}
\end{array}}
\]

---

## 1. Scope inherited from the five project records

The five supplied records establish several audit principles that remain relevant, but their model-specific negative theorems must not be transplanted indiscriminately.

- A known small residual-compatible defect can be converted into a uniform physical-time loss error under squared-loss clock contraction.
- Fixed-order Wick/Taylor existence does not imply real-axis convergence.
- In the earlier quadratic Gaussian model, the positive Wick branch has zero Taylor radius, and positive polynomial time-steppers inherit the divergence.
- Weak moment convergence and initial Gaussian tail truncation can be dynamically singular.
- One-source syntax is vacuous unless the compiler and coefficient provenance are restricted.
- Exact finite continuation semantics fail because matrix-reuse words that agree now can have different tagged continuations.

For the present residual-\(\tanh\) model, however:

- \(\phi,\phi'\) are bounded;
- the forward depth increment is bounded;
- the positive polynomial cone used in the old zero-radius proof is absent;
- the old Riccati comparison for \(a z^2\) is absent;
- signed cancellations are unavoidable.

Thus the earlier results justify hostile tests and topology requirements, not a negative conclusion for this model.

---

## 2. Equations used in the hostile tests

The following is the normalization needed for the arguments below. Let

\[
g_r=f_r-y_r,\qquad
D_r(s,t)=\operatorname{diag}\phi'(W(s,t)h_r(s,t)).
\]

Use the scaled unit-output adjoint

\[
q_r(s,t)=n\,\frac{\partial f_r}{\partial h_r(s,t)},\qquad q_r(1,t)=a(t),
\]

so that

\[
-\partial_s q_r=W^\top D_rq_r,\qquad
\beta_r=D_rq_r.
\]

The Euclidean continuum training equations corresponding to
\(\dot W_\ell=-L\nabla_{W_\ell}\mathcal L\),
\(\dot a=-n\nabla_a\mathcal L\), and
\(\dot B=-n\nabla_B\mathcal L\) are

\[
\partial_tW(s,t)
=-\frac1n\sum_{r=1}^m g_r(t)\,\beta_r(s,t)h_r(s,t)^\top,
\tag{2.1}
\]

\[
\partial_ta(t)=-\sum_{r=1}^m g_r(t)h_r(1,t),
\tag{2.2}
\]

\[
\partial_tB(t)
=-\sum_{r=1}^m g_r(t)
\bigl(\operatorname{diag}\chi'(Bx_r)q_r(0,t)\bigr)x_r^\top.
\tag{2.3}
\]

The forward linear response is generated by

\[
A_r(s,t)=D_r(s,t)W(s,t),
\]

\[
\partial_sJ_r(s,u,t)=A_r(s,t)J_r(s,u,t),
\qquad J_r(u,u,t)=I.
\tag{2.4}
\]

None of the counterexamples below uses orthogonal weights, a projected metric, frozen features, or a low-rank parameterization. A low-rank matrix appears only as an adversarial perturbation at the natural learned-entry scale \(O(n^{-1})\).

---

## 3. A model-lock problem that must be repaired, but should not be used as a cheap disproof

The statement

\[
W_{\ell,ij}(0)\stackrel{\rm iid}{\sim}N(0,n^{-1})
\]

for every discrete layer does not by itself define a regular matrix field
\(W(s,0)\) as \(L\to\infty\). Piecewise-constant interpolants of independent
layers do not converge strongly to a measurable Gaussian matrix-valued path.
With residual size \(1/L\), independent centered layer fluctuations can instead
self-average in depth. At initialization, for odd \(\tanh\), the random
forward residuals have conditional mean zero and cumulative variance of order
\(L(1/L)^2=1/L\). The initial forward path therefore tends toward the identity
path rather than toward an ODE driven by one pointwise iid field.

After training starts, each layer's matrix becomes correlated with its own
activation derivative, so the natural \(L\to\infty\) state may be a depth-indexed
Young measure or a law of matrix “types,” not a samplewise \(W(s,t)\).

There are three legitimate repairs:

1. specify a coupling in \(L\) that samples a depth-regular Gaussian matrix
   field with a fixed correlation kernel;
2. take a layer-particle/Young-measure continuum limit of the iid layers;
3. define the target by an explicit iterated limit, for example \(n\to\infty\)
   at fixed \(L\), followed by \(L\to\infty\), and derive the resulting causal
   state before naming it \(W(s,t)\).

The iterated limits need not be assumed to commute. A joint regime also needs
a quantitative condition. This is an avoidable formulation defect, not
evidence against finite compression, so I do not count it as a falsification.

---

## 4. Exact continuation witness

### 4.1 Construction

Take one sample, \(\chi=\phi=\tanh\), and a restart state at some training time.
Choose vectors \(h,\beta\in\mathbb R^n\) satisfying

\[
h^\top\beta=0,\qquad
\frac1n\|h\|^2=c^2,\qquad
\frac1n\|\beta\|^2=1,
\qquad 0<c<1.
\]

The entries of \(h\) may be chosen as \(\pm c\), so \(h=\tanh(Bx)\) is realizable
and \(\chi'(Bx)=1-c^2\) coordinatewise. Let \(K\) be any dense matrix satisfying

\[
Kh=K\beta=K^\top\beta=0.
\]

It can be dense on the orthogonal complement of
\(\operatorname{span}\{h,\beta\}\). Define

\[
W_0=K,\qquad
W_1=K+\Delta,\qquad
\Delta=\frac1n h\beta^\top.
\tag{4.1}
\]

Then

\[
W_0h=W_1h=0,\qquad
W_0^\top\beta=W_1^\top\beta=0.
\]

Consequently both systems have the same depth profiles

\[
h(s)=h,\qquad q(s)=\beta,\qquad \beta(s)=\beta,
\]

the same preactivation \(Wh=0\), the same forward and backward Grams, the same
output, the same loss, and the same Euclidean weight velocity

\[
W_t=-\frac gn\beta h^\top.
\tag{4.2}
\]

The perturbation has

\[
\|\Delta\|_{\rm op}=c,\qquad
\|\Delta\|_F=c,
\]

but every entry is \(O(n^{-1})\), each row perturbation has Euclidean norm
\(O(n^{-1/2})\), and every fixed-coordinate row law has the same limit in the
two systems. This is exactly the coherent scale created by (2.1).

### 4.2 Different immediate Gram velocities

Let \(v(s)=\partial_th(s)\). Since \(\phi'(0)=1\),

\[
\partial_sv=Wv+W_th.
\]

Put

\[
\kappa_x=\|x\|^2(1-c^2)^2.
\]

The trained input layer gives the same boundary velocity in both systems:

\[
v(0)=-g\kappa_x\beta.
\]

Also,

\[
W_th=-gc^2\beta.
\]

For \(W_0\),

\[
v_0(s)=-g(\kappa_x+c^2s)\beta.
\]

For \(W_1\), note that

\[
W_1\beta=h,\qquad W_1h=0
\]

on the relevant two-dimensional subspace. Hence

\[
v_1(s)
=-g(\kappa_x+c^2s)\beta
-g\left(\kappa_xs+\frac{c^2s^2}{2}\right)h.
\]

For the hidden Gram \(G(s)=n^{-1}h(s)^\top h(s)\),

\[
\partial_tG_0(s)=0,
\]

whereas

\[
\boxed{
\partial_tG_1(s)
=-2gc^2\left(\kappa_xs+\frac{c^2s^2}{2}\right).
}
\tag{4.3}
\]

Thus the discrepancy is \(O(1)\) at every fixed \(s>0\).

### 4.3 What this proves, and what it does not

It proves that no exact autonomous state consisting only of

- \(h,q,\beta\);
- their one-depth empirical laws;
- forward/backward Grams;
- \(Wh\), \(W^\top\beta\);
- or finitely many analogous current one-depth contractions

can be restart-faithful on a neighborhood containing these states.

It also explains why a weak row-law topology is insufficient: a coherent
rank-one component disappears from that topology but survives in a future
message.

It does **not** refute a response-aware finite approximation. In fact the two
states are immediately separated by

\[
J_1(s,u)\beta-J_0(s,u)\beta=(s-u)h.
\]

Nor does it prove a lower bound against every possible finite compiler. To do
that one would need a quantitative noncompactness theorem for the whole
restart class in the observable-stability norm, not merely one collision for a
particular summary.

The construction generalizes to any proposal using finitely many explicit
probe directions: at width larger than the probe span, a coherent rank-one
operator can be placed in an unprobed pair of directions and arranged to appear
after the next local attachment. This remains a counterexample to that probe
family, not to all nonlinear finite encodings.

---

## 5. Nonnormality audit

### 5.1 The genuine Dyson tail survives nonnormality

For (2.4), let

\[
C(s,u)=\int_u^s\|A_r(v,t)\|_{\rm op}\,dv.
\]

The ordered Dyson series gives

\[
J_r(s,u)
=I+\sum_{k\ge1}
\int_{u<v_1<\cdots<v_k<s}
A_r(v_k)\cdots A_r(v_1)\,dv_1\cdots dv_k.
\]

Submultiplicativity and simplex volume imply

\[
\boxed{
\|J_r-J_{r,\le M}\|_{\rm op}
\le
\sum_{k>M}\frac{C(s,u)^k}{k!}.
}
\tag{5.1}
\]

No normality, commutativity, diagonalizability, or spectral gap is used. A
hostile nonnormal example cannot defeat (5.1) while keeping the same bound on
\(C\).

Therefore any report claiming that “nonnormality invalidates the factorial
Dyson tail” is incorrect. What nonnormality invalidates are replacements of
\(C\) by:

- the spectral radius;
- the maximum real part of the eigenvalues;
- an average entry variance;
- a forward Gram norm that does not dominate \(\|\cdot\|_{\rm op}\);
- or a pointwise commutator statistic.

### 5.2 Explicit spectral failure

The perturbation in (4.1) satisfies

\[
\Delta^2=0,\qquad \operatorname{spec}(\Delta)=\{0\},
\]

but

\[
e^{\tau\Delta}=I+\tau\Delta
\]

has nontrivial transient amplification and maps \(\beta\) to
\(\beta+\tau h\). Thus an eigenvalue-only certificate predicts no response
while the relevant contraction changes by \(O(1)\).

Longer nilpotent shifts give the same warning. For orthogonal macroscopic
directions \(u_0,\ldots,u_k\), a coherent shift satisfying
\[
Nu_j=u_{j+1}
\]
has only zero eigenvalues but produces every chronological order through
\(N^ku_0\).

If \(\|N\|_{\rm op}\) is uniformly bounded, however, the high orders still have
the factorial weights in (5.1). To make order \(k\) remain \(O(1)\) as
\(k\to\infty\), one must let the operator-norm budget grow. The unresolved
issue is consequently the uniform norm budget, not nonnormality by itself.

### 5.3 The circular global bound

For bounded \(\phi'\),

\[
\|q_r(s,t)\|
\le
\exp\!\left(\int_s^1\|W(v,t)\|_{\rm op}\,dv\right)\|a(t)\|.
\tag{5.2}
\]

Equation (2.1) then gives schematically

\[
\|\partial_tW(s,t)\|_{\rm op}
\lesssim
\|g(t)\|\,e^{C_W(t)}
\]

after normalized feature and readout bounds, where

\[
C_W(t)=\int_0^1\|W(s,t)\|_{\rm op}\,ds.
\]

Loss descent controls a squared parameter speed, but by itself does not
control its \(L^1\)-in-time arclength. Without a uniform tangent-kernel floor or
another integrability mechanism, (5.2) and the weight-speed estimate form a
circular inequality. This is the main gap behind a horizon-independent
Dyson order.

---

## 6. The full \(n\times n\) response cannot be width-independently low rank

Suppose

\[
\int_u^s\|A_r(v,t)\|_{\rm op}\,dv\le C.
\]

The fundamental matrix is invertible and

\[
\|J_r(s,u)^{-1}\|_{\rm op}\le e^C.
\]

Therefore

\[
\sigma_{\min}(J_r(s,u))\ge e^{-C}.
\tag{6.1}
\]

For every rank-\(M\) matrix \(R_M\) with \(M<n\), the Eckart--Young lower bound
gives

\[
\boxed{
\|J_r(s,u)-R_M\|_{\rm op}
\ge \sigma_{M+1}(J_r(s,u))
\ge e^{-C}.
}
\tag{6.2}
\]

Near the causal diagonal this is even more obvious: \(J(u,u)=I_n\).

Consequences:

- singular values of the **neuron-space** response should not exhibit a
  width-independent decaying tail;
- an error-versus-rank plot for full \(J\) is not evidence for the desired
  compression unless the rank grows with \(n\);
- a valid finite compiler must approximate response contractions on the
  finite sample/message subspace, scalar covariance/response kernels in the
  width-limit state, or separability in the depth/time variables;
- numerical papers must state which axes are being factorized.

This is a genuine no-go theorem for one proposed mechanism, not for finite
observable compression.

---

## 7. High-to-low feedback

### 7.1 Vanishing normalized-Frobenius error can have \(O(1)\) effect

Let \(u,v\in\mathbb R^n\) have norm \(\sqrt n\) and define

\[
R_n=\frac1nuv^\top.
\]

Then

\[
\frac1{\sqrt n}\|R_n\|_F=\frac1{\sqrt n}\longrightarrow0,
\]

but

\[
R_nv=u,\qquad
\frac1n u^\top R_nv=1.
\tag{7.1}
\]

Thus a response residual that vanishes in normalized Frobenius norm can create
an \(O(1)\) normalized Gram contraction. Entrywise convergence and fixed-row
weak convergence fail for the same reason.

Any stability norm must either dominate operator action on all dynamically
generated feature/adjoint directions or directly include the normalized
contractions used by the observable equations.

### 7.2 Two discarded depth modes can make a retained constant mode

On \(s\in[0,1]\), let

\[
e_N(s)=\sqrt2\cos(2\pi Ns).
\]

Then \(\|e_N\|_{L^2}=1\), while

\[
e_N(s)^2=1+\cos(4\pi Ns).
\]

The product of two modes entirely outside every fixed low-frequency Galerkin
space has constant projection equal to one. The exact response/adjoint
feedback contains state-dependent products and contractions, so smallness of
each retained low-mode defect does not imply small outgoing low-mode flux.

A valid spectral proof needs one of:

- an algebra norm with a controlled multiplication map;
- sufficient Sobolev regularity and a dealiased product estimate;
- a computed outgoing residual after all nonlinear contractions;
- or a structural cancellation proved for the actual DMFT equations.

Observed singular-value decay of one isolated response snapshot is not such a
proof.

### 7.3 Causal diagonal and trace loss

Let

\[
r_N(s,u)=\psi(N(s-u)),
\]

where \(\psi(0)=1\) and \(\psi\) is supported near zero. Then

\[
\|r_N\|_{L^2(\{u\le s\})}\to0,
\]

but

\[
r_N(u,u)=1.
\]

The response equation has the boundary condition \(J(u,u)=I\), and differentiated
feedback equations can use diagonal traces. Unweighted \(L^2\) control on the
causal triangle does not control those traces. A response space must have a
bounded trace map, preserve the causal boundary exactly, or include the
boundary defect separately.

### 7.4 What would constitute a universal obstruction

To refute every admissible finite response compiler, one would need, for an
explicit regular restart class \(\mathfrak R\), a bound such as

\[
\inf_{\dim V\le M}
\sup_{Y\in\mathfrak R}
\inf_{v\in V}
\|{\cal R}(Y)-v\|_{\rm stab}
\ge c_0>0
\]

for all \(M\), or a nonvanishing lower bound on every finite outgoing residual.
The examples above show that several weak candidate norms are invalid; they do
not establish this noncompactness in the correct strong norm.

---

## 8. Rare tails and operator norms

### 8.1 What bounded \(\tanh\) fixes

For \(\chi=\phi=\tanh\),

\[
|h_{r,i}(0,t)|\le1,
\qquad
|\partial_sh_{r,i}(s,t)|\le1,
\]

so on the unit depth interval

\[
|h_{r,i}(s,t)|\le2.
\tag{8.1}
\]

The readout velocity also has bounded coordinates up to the residual:

\[
|\partial_ta_i|
\le2\sum_r|g_r|.
\tag{8.2}
\]

Unlike the quadratic model, a large initial \(a_i\) does not create a local
\(a'=z^2,\ z'=az\) Riccati loop with unbounded \(z\). The adjoint is linear in
the Gaussian readout and is bounded by (5.2) on any operator-norm-controlled
tube. I found no valid transfer of the old instantaneous-fitting theorem or
Gaussian-tail truncation counterexample to this bounded model.

### 8.2 What Gaussian tails still prevent

There cannot be a deterministic bound valid for every finite-width Gaussian
draw. A theorem should be one of:

- a deterministic theorem for the already-averaged infinite-width state;
- a high-probability finite-\((n,L)\) theorem with a stated failure probability;
- or a theorem in an explicit sub-Gaussian/Orlicz law topology.

Weak convergence of initialization laws is too weak. An arbitrarily small tail
mass can carry a large coherent readout or operator action while remaining
invisible to bounded test functions. Robustness should be measured in a
uniform sub-Gaussian norm, a sufficiently strong Wasserstein-plus-moment norm,
or an explicit family of Gaussian covariance parameters.

For iid Gaussian \(W_\ell\), typical operator norms are \(O(1)\), but a
statement involving the maximum over \(L\) layers needs a joint regime. The
depth-integrated average
\[
\frac1L\sum_\ell\|W_\ell\|_{\rm op}
\]
is less fragile than the maximum and is the natural quantity in (5.1).
Nonetheless, training-time control of its all-time supremum remains open.

### 8.3 Rare coherent directions are more dangerous than rare entries

The continuation perturbation (4.1) has no large entry at all. It is dangerous
because \(n^2\) small entries align. A tail audit that checks only coordinate
maxima will miss the learned \(O(n^{-1})\) coherent operator. Operator/action
tests on the sample-message subspace are mandatory.

---

## 9. Ill-conditioned tangent kernels and the failure of a broad all-time theorem

Consider the exact residual dynamics

\[
\dot r=-\Theta r,
\qquad
\Theta_\delta=
\begin{pmatrix}
1&0\\0&\delta
\end{pmatrix},
\qquad \delta>0,
\]

with \(r(0)=(0,1)\). Let the approximate PSD kernel be

\[
\widehat\Theta_\delta=
\begin{pmatrix}
1&0\\0&0
\end{pmatrix}.
\]

Then

\[
\|\Theta_\delta-\widehat\Theta_\delta\|_{\rm op}=\delta,
\]

both kernels are positive semidefinite, and on every fixed time interval

\[
\sup_{t\le T}\|\widehat r(t)-r(t)\|
\le\delta T.
\]

But

\[
r_2(t)=e^{-\delta t},\qquad
\widehat r_2(t)=1,
\]

so

\[
\boxed{
\sup_{t\ge0}\|\widehat r(t)-r(t)\|=1.
}
\tag{9.1}
\]

If a compact data class permits \(\delta\downarrow0\), then for any certificate
size \(\rho_M\) one may choose an instance with
\(\delta<\rho_M\). No stability estimate
\[
\sup_{t\ge0}{\rm error}\le C\rho_M
\]
can hold with \(C\) uniform over that class.

This example establishes four points.

1. PSD reconstruction alone is insufficient.
2. Absolute kernel error is insufficient near a small learnable eigenvalue.
3. Finite-time convergence does not imply all-time convergence uniformly over
   problem instances.
4. “Nondegenerate dataset Gram” is not enough unless it is proved to imply a
   quantitative lower bound for the **trained tangent kernel** in every label
   direction.

Nearly aligned samples and antisymmetric labels are the canonical numerical
stress test. The data Gram may be invertible while its smallest eigenvalue,
and the corresponding tangent-kernel eigenvalue, are arbitrarily small.

For one fixed instance with \(\delta>0\), an approximation sequence can
eventually resolve the slow mode; (9.1) is not a pointwise no-go. It refutes
uniformity over an inadequately separated class.

### 9.1 Hidden Grams require more than loss stability

Gradient descent gives

\[
\frac{d}{dt}\mathcal L=-g^\top\Theta g\le0.
\]

This controls a squared speed. It does not automatically give
\[
\int_0^\infty\|g(t)\|\,dt<\infty,
\]
which is the natural budget for accumulated feature and Gram motion. If
\(\Theta\succeq\lambda_*I\), exponential decay supplies this \(L^1\) budget.
Without coercivity, a residual-compatible local error can act for arbitrarily
large feature time.

Moreover, the zero-loss set has many neutral hidden directions. Loss
contraction alone does not make the terminal Gram map Lipschitz. An all-time
Gram theorem needs finite feature arclength plus stability transverse to the
observable terminal manifold, or a direct observable estimate.

### 9.2 Label and data perturbations

Near a kernel null direction, a small data or label perturbation can:

- change the fitting time by \(O(\delta^{-1})\);
- activate a direction absent in the unperturbed problem;
- change the limiting residual if the approximate kernel drops that direction;
- or move the trajectory across a basin/separatrix in a nonconvex state space.

Restart and neighborhood tests are therefore not optional decorations. They
are what distinguish a causal compression from a fit to one benign trajectory.

---

## 10. Finite-time versus all-time status

The two claims should be separated.

### Finite-time claim

For fixed \(T<\infty\), bounded activation, a well-posed causal width-limit
state, a bound
\[
\sup_{t\le T}\int_0^1\|A_r(s,t)\|_{\rm op}\,ds<\infty,
\]
and a stable Galerkin forcing norm make convergence plausible by ordinary
Volterra/Galerkin arguments. Nonnormality is not a fundamental obstruction.

### All-time claim

To make the approximation order independent of the requested physical
horizon, one still needs to prove, uniformly on the stated data/restart class:

1. global well-posedness of the exact causal macroscopic state;
2. a horizon-independent response-generator budget;
3. a quantitative learnability/coercivity or integrated-observability bound;
4. finite \(L^1\) feature arclength;
5. continuity of every depthwise Gram and the terminal Gram map in the chosen
   forcing topology;
6. the same bounds for the approximate PSD system;
7. a computed outgoing Galerkin residual whose integral is controlled by the
   residual/feature clock.

None follows merely from bounded \(\tanh\), loss monotonicity, or the formal
factorial Dyson tail.

Thus an honest final statement should either:

- make a finite-time conjecture first and label the all-time extension as a
  separate coercivity/finite-arclength conjecture; or
- include both properties as explicit assertions to be proved for a
  quantitatively separated canonical data class.

It should not assume the crucial all-time constants as unexplained hypotheses
and then count the resulting conditional theorem as resolution.

---

## 11. A tight anti-oracle admissible class

Purely extensional wording cannot ban an oracle for one fixed problem: the
architecture and exact real parameters determine a single future curve, which
can always be hidden in arbitrary real coefficients. Non-oracularity must be
made effective and robust.

### 11.1 Input family

Use a genuinely varying, effectively described family, not a singleton:

\[
\mathfrak D=
\left\{
(K_x,y,\nu):
\kappa_x I\preceq K_x\preceq K_x^{\max}I,\ 
\|y\|\le Y,\ 
\nu\in\mathfrak N
\right\}.
\tag{11.1}
\]

Here:

- \(K_x\) is the sample Gram matrix;
- \(\kappa_x>0\) is quantitative, not merely “nondegenerate”;
- \(\mathfrak N\) is a compact, finitely parameterized class of centered
  Gaussian or uniformly sub-Gaussian initialization laws with covariance
  eigenvalues in fixed intervals;
- the depth initialization convention and the \(L,n\) limit order are part of
  the input specification.

Data nondegeneracy alone may not imply tangent-kernel coercivity. The final
conjecture should additionally assert, rather than silently assume, that the
canonical trajectories generated from (11.1) enter an explicit regular
restart class \(\mathfrak R\).

### 11.2 Restart class

Let \(X\) be the exact causal macroscopic state space and \(S_t\) its
semigroup. An explicit regular class \(\mathfrak R\subset X\) should have
quantitative constants for:

- forward feature bounds;
- sub-Gaussian/Orlicz adjoint and readout bounds;
- depth-integrated operator control;
- causal response regularity and a bounded trace;
- continuity of output and Gram readouts;
- either \(\Theta(Y)\succeq\lambda_*I\) or an explicitly stated robust
  integrated-observability substitute;
- finite feature arclength.

The substantive model theorem must prove that every canonical initialization
from \(\mathfrak D\) generates a trajectory in \(\mathfrak R\), and that a
neighborhood of each \(S_{t_0}Y_0\) remains in the same certified tube. Merely
defining \(\mathfrak R\) by the desired conclusion would be circular.

Restartability should mean:

\[
\sup_{\tau\ge0}
\bigl\|
{\cal O}(\Phi_M^\tau P_MY)
-{\cal O}(S_\tau Y)
\bigr\|
\le C\rho_M
\qquad
\text{for every }Y\in\mathfrak R,
\tag{11.2}
\]

where \(P_MY\) uses only the current state at restart, never its future.

This rules out an absolute-time playback curve.

### 11.3 Compiler and coefficient grammar

An admissible compiler is one fixed Turing-computable algorithm
\({\cal C}\). Given \(M\), the finite description of
\((K_x,y,\nu)\), and the declared basis dictionary, it outputs:

1. a finite response-Galerkin state \(z_M\in\mathbb R^{d_M}\), equivalently
   finitely many fields restricted to finite declared bases;
2. an autonomous vector field
   \[
   \dot z_M=F_M(z_M);
   \]
3. fixed readouts \(f_M,G_M(s)\);
4. a reconstruction \(R_Mz_M\) into the exact causal-state grammar;
5. a machine-checkable derivation DAG showing that every term of \(F_M\)
   comes from the local forward, adjoint, response, contraction, and Galerkin
   rules;
6. rational, algebraic, or interval-certified computable coefficients only;
7. a residual/stability certificate.

Permitted operations can include:

- finite arithmetic and differentiation;
- certified quadrature of the fixed activation and initialization law;
- projection onto a computable causal basis;
- finite matrix factorization with interval error bounds;
- validated integration of the **finite** approximate system;
- a posteriori residual evaluation using the displayed local exact equations.

Forbidden inputs include:

- samples of \(f,G,J\), or the exact causal state at positive time;
- the exact target-reaching time;
- arbitrary unlabelled real constants;
- coefficients depending explicitly on absolute physical time;
- a clock variable used only to index a precomputed future table;
- an unverifiable “tail constant” whose definition contains the exact
  positive-time solution.

An arbitrary ODE packed into one PDE source is not disallowed merely because
of syntax; it is rejected if it lacks the projection provenance and residual
certificate. Conversely, a legitimate projected ODE remains legitimate if it
is written as an ODE rather than cosmetically packed into a PDE.

### 11.4 Residual certificate

For the exact local evolution
\[
\dot Y=F(Y),
\]
the reconstructed approximate state
\[
\widetilde Y_M=R_Mz_M
\]
has outgoing residual
\[
r_M=\partial_t\widetilde Y_M-F(\widetilde Y_M).
\tag{11.3}
\]

A useful certificate has the form

\[
\rho_M
=\eta_M
+\|r_M\|_{\mathcal F}
+\zeta_M,
\tag{11.4}
\]

where:

- \(\eta_M\) is a certified current-state projection error;
- \(\mathcal F\) is a fixed forcing norm strong enough to control coherent
  contractions, nonlinear high-to-low flux, and causal traces;
- \(\zeta_M\) bounds readout/quadrature defects;
- the infinite-time part of \(\|r_M\|_{\mathcal F}\) is bounded from the
  approximate Lyapunov/residual clock and an a priori invariant tube, not by
  querying the exact trajectory.

The certificate must be independently checkable from the input, compiler
output, and finite approximate solution. The theorem to be proved is a
uniform stability estimate

\[
\sup_{t\ge0}
\left[
\|f_M(t)-f(t)\|
+\sup_s\|G_M(s,t)-G(s,t)\|_F
\right]
\le C_{\mathfrak R}\rho_M
\tag{11.5}
\]

and
\[
\sup_{Y\in\mathfrak R}\rho_M(Y)\to0.
\tag{11.6}
\]

The constant may depend on the explicitly declared class constants, but not
on \(M,n,L\), the instance inside \(\mathfrak D\), the restart time, or a
requested horizon.

### 11.5 PSD reconstruction

The approximate tangent kernel should be built as a Gram:

\[
\Theta_M
=S_{a,M}S_{a,M}^\top
+S_{B,M}S_{B,M}^\top
+\int_0^1S_{W,M}(s)S_{W,M}(s)^\top\,ds.
\tag{11.7}
\]

This guarantees \(\Theta_M\succeq0\). For all-time accuracy, the certificate
must additionally prove either
\[
\Theta_M\succeq\lambda_*/2
\]
on the certified tube or exact preservation of every slow/null direction.
PSD alone does not pass the example in Section 9.

### 11.6 Why this blocks the listed loopholes

- **Curve fitting:** future samples are not legal inputs, coefficients are
  effectively represented, and a fitted observable curve does not certify
  the full local outgoing residual on a restart neighborhood.
- **Arbitrary real encoding:** all constants have a finite certified
  derivation from current input data.
- **Absolute-time source encoding:** autonomy and (11.2) require the same
  future from the same current state, independent of the original clock
  phase.
- **Finite-ODE packing:** source syntax carries no credit; provenance,
  residual, and restart intertwining are the test.
- **One canonical trajectory only:** (11.2) and uniformity on
  \(\mathfrak D,\mathfrak R\) require neighborhood robustness.
- **Assumed tail estimate:** the outgoing residual is evaluated from the
  reconstructed finite state and local equations, with a checkable bound.
- **Negative approximate kernel:** (11.7) prevents it.
- **Dropped small kernel direction:** the coercivity/nullspace clause detects
  it.

No purely verbal use of “constructive” proves these properties. They need to
be part of the formal definition.

---

## 12. Assessment of the conjecture proposed in the user request

As written, the proposed statement has four vulnerabilities.

1. **“Universal constructive compiler” is not formal.** With unrestricted
   real coefficients it can hide exact future samples.
2. **“Finite PDE or ODE fields” is syntactic.** Every finite ODE can be packed
   into one source field.
3. **“Compact nondegenerate class” lacks quantitative learnability.** It can
   include a sequence of nearly singular tangent kernels, making the proposed
   uniform all-time constant impossible.
4. **The residual is not tied to a forcing topology.** A small weak residual
   can have the \(O(1)\) coherent effects in Section 7.

There is also a quantifier issue. If \(C\) is allowed to depend on the
individual dataset or hidden exact trajectory, uniformity is lost and an
oracle constant can reappear. If \(C\) is uniform over a broad class without a
coercivity/separation constant, Section 9 disproves it.

The repaired formulation in Section 11 is sharp enough to be non-oracular,
but it is stronger than what current evidence proves. It directly states the
compression property; it is not an auxiliary lemma. Establishing it would
resolve the desired approximate-PDE question for the declared standard
Euclidean model and class.

---

## 13. Ranked hostile lemmas that remain

1. **Canonical limit lemma.** Specify and prove the \(L,n\) limit, including
   the iid-depth initialization issue and whether the exact state is a
   matrix-field law, causal DMFT, or path law.
2. **Uniform learnability/finite-arclength lemma.** Derive a quantitative
   all-time residual budget from the standard Euclidean model on a nontrivial
   data class; do not assume it.
3. **Response-generator bound.** Prove
   \[
   \sup_{t\ge0,r}\int_0^1\|D_rW\|_{\rm op}\,ds<\infty
   \]
   or a weaker bound sufficient for the chronological tail.
4. **Strong forcing-space lemma.** Construct a state/forcing topology that
   controls coherent rank-one actions, causal traces, and high-to-low
   multiplication while containing the canonical Gaussian state.
5. **Outgoing Galerkin residual lemma.** Compute a residual tending to zero in
   that topology without exact positive-time data.
6. **Observable stability lemma.** Close the full loop
   \[
   \text{response}\to\text{feature}\to\text{adjoint/kernel}
   \to\text{new response}
   \]
   with a constant independent of horizon.
7. **Terminal Gram stability lemma.** Show that neutral zero-loss directions
   do not make the all-time hidden-Gram readout discontinuous.
8. **Uniform restart lemma.** Prove the same estimates on an explicit
   neighborhood of positive-time states.
9. **PSD plus coercivity lemma.** Realize the approximate kernel as a Gram and
   retain every quantitatively learnable direction.
10. **Depth-regularity/width lemma.** Prove the claimed separable-rank or
    spectral decay in the actual axes being compressed. Full neuron-space
    low rank is impossible by (6.2).

---

## 14. Final hostile classification

| Claim | Hostile status |
|---|---|
| Exact closure by forward/adjoint one-depth laws and Grams | **Falsified** by (4.3) |
| Full \(n\times n\) Jacobian has width-independent low rank | **Falsified** by (6.2) |
| Eigenvalues control the response | **Falsified** by nilpotent coherent perturbations |
| Operator-norm Dyson tail survives nonnormality | **Proved**, conditional only on the displayed norm budget |
| Weak \(L^2\), row-law, or normalized-Frobenius residual is sufficient | **Falsified** by Section 7 |
| PSD approximate kernel alone gives all-time accuracy | **Falsified** by (9.1) |
| Uniform all-time theorem on a class with vanishing kernel eigenvalues | **Falsified** |
| Quadratic Gaussian instantaneous-tail theorem transfers to \(\tanh\) | **Not valid; no transfer found** |
| Finite-time response-Galerkin approximation under strong regularity | **Plausible, unproved for the exact dense width limit** |
| Horizon-independent all-time response-Galerkin approximation | **Open; requires the ranked lemmas** |
| Every admissible finite compiler is impossible | **Not proved and not supported by the present counterexamples** |

The most defensible verdict is:

> Continuous depth gives a real approximation mechanism—the chronological
> operator-norm tail—but it does not supply exact one-depth closure, neuron-space
> low rank, a strong residual norm, or all-time stability for free. The
> proposed all-time dense Euclidean finite-response-PDE conjecture remains
> viable only after a precise limit construction, a quantitative learnable
> restart class, a non-oracular proof-carrying compiler, and a uniform
> high-to-low stability theorem. The current evidence is enough to reject
> several tempting proofs, but not enough to reject every admissible
> accuracy-dependent finite compiler.
