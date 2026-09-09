# Independent synthesis audit B

## Bottom line

The three reports and the numerical archive support a narrower conclusion than
the requested all-time theorem.

1. The finite-\((n,L)\) normalization is settled:
   \[
   \eta_B=n,\qquad \eta_a=n,\qquad \eta_{W_\ell}=L.
   \]
2. For iid layers, the stated initialization does **not** converge to a
   realized depth-regular matrix field \(W(s,0)\). The only conservative
   canonical mean-field target is
   \[
   \boxed{\lim_{L\to\infty}\left(\lim_{n\to\infty}\right)}
   \]
   with \(L\) fixed in the inner width limit. The inner object is the
   fixed-\(L\) causal DMFT; the outer limit is a depth-homogenization or
   Young-measure limit. It is not, without a new theorem, the classical
   equation \(\partial_sh=\tanh(W(s,t)h)\) for one pointwise matrix field.
3. A classical neural-ODE version requires a **separate depth-regular
   initialization**, obtained by discretizing a continuous Gaussian matrix
   process. It remains dense and Euclidean, but it is not the iid-layer model
   stated in the question. Most of the successful continuous-depth numerical
   tests concern this separate variant.
4. The exact width-limit state is larger than the fixed-training-time depth
   propagator \(J(s,u,t)\). Dense matrix reuse produces two-training-time
   covariance and functional-response kernels. Truncating the depth Dyson
   series controls one component of this state, not the whole DMFT.
5. The numerical results strongly support finite depth-word truncation on
   the tested finite networks. They do not test a width-independent
   response/DMFT compiler, do not produce a residual certificate, and do not
   support a uniform all-time theorem on a nondegenerate problem family.
6. A horizon-independent \(M(\varepsilon)\) is therefore a legitimate sharp
   **conjecture**, but not a strongly supported conclusion. Finite-\(T\)
   approximation is the evidence-backed claim; the all-time strengthening
   still requires global coercivity or another finite-arclength/stability
   mechanism.

The recommended final statement below directly defines the admissible
non-oracular finite-PDE property. It does not hide the decisive tail or
stability estimate as a hypothesis. Its truth would resolve the desired
compression problem; at present its all-time clause is genuinely open.

---

## 1. Reconciliation of the three reports

### 1.1 Agreements

All three reports agree on the following.

- With the unit-output adjoint \(q_r^\ell=n\,\partial f_r/\partial h_r^\ell\),
  \[
  q_r^L=a,\qquad
  q_r^\ell=q_r^{\ell+1}+\frac1L W_\ell^\top\beta_r^\ell,
  \qquad
  \beta_r^\ell=D_r^\ell q_r^{\ell+1}.
  \]
- The exact Euclidean flows are
  \[
  \dot a=-\sum_re_rh_r^L,\qquad
  \dot B=-\sum_re_r\gamma_rx_r^\top,
  \]
  \[
  \dot W_\ell=-\frac1n\sum_re_r\beta_r^\ell(h_r^\ell)^\top.
  \]
- The exact finite-network tangent kernel is
  \[
  \Theta_{rq}
  =G^{h,L}_{rq}
  +(x_r^\top x_q)G^\gamma_{rq}
  +\frac1L\sum_\ell
  G^{h,\ell}_{rq}G^{\beta,\ell}_{rq}.
  \]
- One-depth forward/adjoint laws and Grams do not close exactly.
- Under
  \[
  C_A=\int_0^1\|D_r(s,t)W(s,t)\|_{\rm op}\,ds<\infty,
  \]
  the noncommutative chronological tail satisfies
  \[
  \left\|J-J_{\le M}\right\|_{\rm op}
  \le \sum_{k>M}\frac{C_A^k}{k!}.
  \]
  Nonnormality does not invalidate this bound.
- The full \(n\times n\) response cannot have width-independent matrix rank:
  \(J(u,u)=I_n\), and under an integrated generator bound all singular values
  remain bounded away from zero.
- PSD reconstruction is necessary but not sufficient for all-time stability.
- Squared-loss descent gives an \(L^2\)-speed budget, not automatically an
  \(L^1\) feature-arclength budget.

### 1.2 The main reconciliation

The response report studies the fixed-training-time depth response
\[
J_r(s,u,t).
\]
The scaling/DMFT report shows that eliminating the trained dense matrices
produces
\[
C^{h,\ell}_{rq}(t,t'),\quad
C^{\beta,\ell}_{rq}(t,t'),\quad
R^{h,\ell}_{rq}(t,t'),\quad
R^{\beta,\ell}_{rq}(t,t')
\]
on a two-training-time causal triangle. These are reciprocal Onsager/memory
objects created by reuse of the same \(W_\ell^0\).

There is no contradiction. The correct conclusion is:

\[
\boxed{
\text{depth response }J\text{ is necessary for Gram evolution, but is not the
complete exact dense width-limit state.}
}
\]

A finite compiler must approximate both:

1. chronological response in depth; and
2. the training-time covariance/response or equivalent path-law state.

The numerical program truncates only the backward depth word expansion while
retaining every finite \(n\times n\) matrix \(W_\ell\). It therefore tests the
first mechanism but not the second.

### 1.3 Hostile results that survive synthesis

The explicit coherent rank-one continuation pair proves that two states with
the same \(h,q,\beta\), one-depth laws, Grams, \(Wh\), and
\(W^\top\beta\) can have different immediate hidden-Gram velocities. This
rules out an exact one-depth quotient, but not a response-aware approximation.

The high-to-low examples prove that entrywise, row-law, normalized-Frobenius,
or unweighted \(L^2\) residuals are inadequate. A valid forcing norm must
control coherent operator actions, nonlinear contractions, and causal
traces.

The ill-conditioned PSD-kernel example proves that absolute finite-time kernel
accuracy does not imply uniform all-time output accuracy over a class with
vanishing learnable eigenvalues. Thus “compact nondegenerate” must be
quantitative, and an all-time proof needs more than PSD.

No report establishes a lower bound against every strong, response-aware,
proof-carrying finite compiler.

---

## 2. The only honest canonical limit for iid layers

For the architecture exactly as stated, all \(W_\ell^0\) are independent.
Their piecewise-constant interpolation is not tight in a strong path topology
as \(L\to\infty\). At initialization the bounded odd residual branches
self-average:

\[
\frac1L\sum_{\ell<L}\tanh(W_\ell h)
\to0
\]

coordinatewise in the elementary iid calculation, with fluctuations of order
\(L^{-1/2}\). A pointwise continuum field with independent nondegenerate
values at every \(s\) is not an ordinary measurable matrix path.

The recommended canonical target is therefore:

1. fix \(L\);
2. take \(n\to\infty\) and derive the \(L\)-layer causal DMFT, including both
   reciprocal response kernels;
3. take \(L\to\infty\) in that macroscopic system.

For every finite \(t\), define

\[
\mathcal O_{\mathrm{iid}}(t)
:=
\lim_{L\to\infty}
\left(
\lim_{n\to\infty}\mathcal O_{n,L}(t)
\right),
\tag{2.1}
\]

with local-uniform-in-\(t\) convergence required in the construction theorem.
No interchange with \(L\to\infty\) and no diagonal \(L=L(n)\) should be
claimed until proved.

The exact iid macroscopic state should be denoted abstractly by
\(Y_{\mathrm{iid}}\) until the outer limit is derived. It is expected to be a
depth-homogenized causal path law with covariance and response kernels, not a
realized \(W(s,t)\).

### Separate classical-depth variant

If the scientific target is specifically

\[
\partial_sh_r(s,t)=\tanh(W(s,t)h_r(s,t)),
\]

define a different initialization:

\[
\mathbb E[
W_{ij}^0(s)W_{kl}^0(u)
]
=\frac1n\delta_{ik}\delta_{jl}K_W(s,u),
\]

where \(K_W\) is continuous and the process has a depth-regular version.
Discretize this same process at \((\ell+1/2)/L\), take \(L\to\infty\) at
fixed \(n\), and then take \(n\to\infty\).

This depth-regular model is still fully dense and uses ordinary Euclidean
\(\mu\)P training. It is nevertheless a distinct initialization law and must
have a separate theorem and conjecture. Numerical evidence from it cannot be
reported as evidence for the iid-layer outer limit without a homogenization
equivalence theorem.

---

## 3. Numerical audit

### 3.1 What the computations genuinely establish

| Test | Numerical outcome | Valid conclusion |
|---|---:|---|
| Gradient/scaling finite differences | relative errors \(4.7\times10^{-10}\) to \(6.5\times10^{-9}\); kernel identity \(1.0\times10^{-8}\) | The finite-\((n,L)\) normalization and PSD kernel formula are correct |
| iid initialization, \(L=8\to128\) | terminal displacement \(0.118\to0.028\), approximately \(L^{-1/2}\) | iid residual branches self-average in depth |
| smooth initialization, \(L=8\to128\) | displacement \(0.288\to0.291\) | depth-coherent initialization has a nontrivial classical-depth limit |
| smooth depth convergence, \(L=12,24,48\) vs \(96\) | output error \(4.9\times10^{-3},2.1\times10^{-3},7.0\times10^{-4}\); Gram error \(2.34\times10^{-2},1.02\times10^{-2},3.44\times10^{-3}\) | the finite-depth discretization converges in this one smooth-field experiment |
| smooth generic, adjoint word \(M=4\) | output \(2.8\times10^{-5}\); Gram \(1.1\times10^{-4}\) | low depth-word order is accurate on this finite network |
| smooth nonnormal, \(M=4\) | output \(3.0\times10^{-5}\); Gram \(3.9\times10^{-4}\) | moderate nonnormality does not defeat depth-word truncation |
| iid generic, \(M=4\) | output \(1.9\times10^{-7}\); Gram \(3.0\times10^{-7}\) | the finite iid network's backward product is especially easy to truncate in this run |
| positive-time restarts, \(M=4\) | output about \(10^{-5}\); Gram about \(1.9\times10^{-5}\) | local robustness of the same finite-network truncation |

These are useful, reproducible positive results. No failed numerical case was
suppressed in the saved tables.

### 3.2 The important failed/qualified case

For nearly aligned samples:

\[
\lambda_{\min}(\Theta)\approx1.2\times10^{-3},\qquad
\mathcal L(1.6)\approx0.7203,
\]

while hidden-Gram and output motion are only about \(8.4\times10^{-3}\). The
response truncation is numerically accurate, but the network has barely
learned the difficult label direction.

This is not evidence for horizon-independent successful compression. It is
evidence that:

- the truncation can be accurate when the underlying dynamics are nearly
  frozen;
- conditioning materially controls the physical training horizon;
- a broad uniform all-time class cannot be justified by PSD alone.

In the parameter grid, every other recorded exact minimum kernel eigenvalue
is at least about \(0.66\). The grid therefore predominantly samples a
well-conditioned regime.

### 3.3 Why the horizon table is weak evidence

For the one generic smooth run, the prefix-sup errors plateau through
\(T=3.2\). For \(M=4\), the recorded sup output and Gram errors remain
approximately

\[
1.48\times10^{-5},\qquad 1.39\times10^{-4}.
\]

But:

1. all horizons are prefixes of the same trajectory;
2. the sup error is attained early and must remain constant after that;
3. the exact kernel stays strongly coercive, around \(1.5\);
4. the loss is already \(1.4\times10^{-6}\) by \(T=3.2\);
5. no \(C_A(t)\), outgoing residual, or required adaptive mode count is
   measured.

Thus the table shows that error stops accumulating after this easy trajectory
has fitted. It does not show that one \(M\) works on arbitrary horizons or on
the declared problem/restart family.

The \(M=1\) row is also instructive: final output error decays to
\(1.4\times10^{-4}\), while the final hidden-Gram error remains about
\(6.1\times10^{-2}\). Loss fitting does not erase hidden-state bias.

### 3.4 Singular-value plot

For the representative scalar two-depth contraction, the tenth singular
value is still \(3.2\%\) to \(4.2\%\) of the first. The decay is consistent
with a causal Volterra-like algebraic tail, not overwhelming low-rank
compression. The plotted kernel includes the raw causal lower-triangular
primitive; that primitive was not factored before the SVD.

The plot concerns one scalar contraction, not the full \(n\times n\)
response. It supplies no singular-value theorem for the DMFT response family.

### 3.5 Methodological limitations

The simulations do **not** yet implement the conjectured finite neural PDE:

- every full \(n\times n\) matrix \(W_\ell\) is retained;
- only the backward depth-word expansion is truncated;
- the truncated-adjoint trajectory is not the gradient flow of the separately
  reported reconstructed PSD kernel; that kernel is a structure-preserving
  diagnostic built from the truncated sensitivities, not an identity
  \(\dot f=-\Theta_M(f-y)\) for the approximate trajectory;
- the training-time DMFT/Onsager response is not approximated;
- no finite law/chaos/cubature state is constructed;
- no outgoing residual \(\rho_M\) is calculated;
- no response Galerkin model is evolved in place of the network;
- widths are only \(16\) to \(32\), with no width convergence table;
- \(L=96\) is called a smooth-depth reference without time-step or width
  extrapolation;
- the nonnormal test does not report transient amplification or the
  integrated operator budget \(C_A(t)\);
- initialization-law perturbations are not tested;
- restart tests use two nearby states, one label perturbation, and a short
  well-conditioned horizon.

Accordingly, the numerical evidence is strong for the factorial
**depth-word mechanism**, modest for finite-depth discretization, and absent
for a width-independent certified causal compiler.

---

## 4. Recommended sharp conjecture

### 4.1 Quantitative problem family

Fix \(m\), \(\chi=\phi=\tanh\), and constants
\(\kappa_x,K_x,Y>0\). Let

\[
\mathfrak D=
\left\{
(K,y):
K=K^\top,\ 
\kappa_xI_m\preceq K\preceq K_xI_m,\ 
K_{rr}=1,\ 
\|y\|_2\le Y
\right\}.
\tag{4.1}
\]

Use exactly the iid Gaussian initialization and Euclidean learning rates in
Section 1. The Gram lower bound is quantitative; “distinct” or
“nondegenerate” without \(\kappa_x\) is insufficient.

Let \(X_{\mathrm{iid}}\) be the causal history state space produced by the
width-first/depth-second construction. Its state must include enough
accumulated covariance/response information to be Markov and restartable.
Let \(S_t\) denote its semigroup and

\[
\mathcal O(Y)=
\bigl(f(Y),G^h_Y(\cdot)\bigr)
\in
E:=\mathbb R^m\times
C([0,1];\mathbb S^m),
\]

with norm

\[
\|(f,G)\|_E
=\|f\|_2+\sup_{s\in[0,1]}\|G(s)\|_F.
\tag{4.2}
\]

### 4.2 Admissible proof-carrying compiler

An admissible compiler is one fixed effective algorithm \(\mathcal C\). Given
\(M\), \(K\), \(y\), the initialization-law parameters, and an admissible
**current** restart state, it outputs:

\[
\dot z_M=F_M(z_M;K,y),\qquad
z_M\in\mathbb R^{d_M},
\tag{4.3}
\]

an initialization/projection \(P_M\), readouts
\[
\mathcal O_M(z_M)=(f_M,G_M(\cdot)),
\]
and a computable nonnegative certificate \(\rho_M\).

The following are part of admissibility.

1. \(F_M\) is autonomous. It has no positive-time samples, target time, or
   absolute-time playback coefficients.
2. \(d_M\), all source dimensions, and all retained modes are finite and may
   depend on \(M,m,\kappa_x,K_x,Y\), but not on \(n,L\), restart time, or a
   requested physical horizon.
3. Every coefficient is rational, algebraic, or interval-certified
   computable from the architecture, \(K,y\), initialization law, and the
   displayed local forward/adjoint/DMFT/response/contraction rules. Arbitrary
   unlabelled real constants are forbidden.
4. The compiler supplies a finite derivation/residual certificate checkable
   by a fixed verifier from those local equations and its approximate state.
   It may use Galerkin, cubature, chaos, finite elements, or another local
   construction; it may not query \(S_tY\) for \(t>0\).
5. Restart initialization uses only \(P_MY\) at the restart time, including
   the current accumulated causal memory. It never uses the future of \(Y\).
6. The approximate tangent kernel is produced as a sensitivity Gram
   \[
   \Theta_M=\mathcal S_M\mathcal S_M^\top
   \tag{4.4}
   \]
   or an exactly equivalent positive-weight factorization, so
   \(\Theta_M\succeq0\).
7. The same compiler and proof rules apply uniformly to an explicitly
   norm-bounded restart neighborhood \(\mathfrak R\subset X_{\mathrm{iid}}\)
   containing all canonical trajectories from \(\mathfrak D\). Membership
   and bounds for \(\mathfrak R\) may not be defined using future samples.

This definition deliberately gives no credit for writing an arbitrary ODE as
one source PDE. Structural provenance and the certificate, not syntax, are
the criterion.

### 4.3 Conjecture

> **Canonical iid dense Euclidean continuous-depth certified finite-PDE
> conjecture.**
>
> For the model and family (4.1):
>
> **(A) Exact target.** For every fixed \(L\), the \(n\to\infty\) dynamics
> converge locally uniformly in training time to a unique causal fixed-\(L\)
> DMFT. These DMFTs have a unique \(L\to\infty\) homogenized limit
> \(Y_{\mathrm{iid}}\in X_{\mathrm{iid}}\), defining a global restartable
> semigroup \(S_t\). Outputs and all depthwise hidden Grams are continuous
> readouts (4.2).
>
> **(B) Certified finite compression.** There is one admissible compiler
> \(\mathcal C\) and constants \(C<\infty\), independent of
> \(M,n,L\), instance, restart time, and physical horizon, such that
> \[
> \sup_{Y\in\mathfrak R}\sup_{t\ge0}
> \left\|
> \mathcal O_M\!\left(\Phi_M^tP_MY\right)
> -\mathcal O(S_tY)
> \right\|_E
> \le C\rho_M,
> \tag{4.5}
> \]
> where \(\Phi_M\) is the flow of (4.3), and
> \[
> \sup_{Y\in\mathfrak R}\rho_M(Y)\longrightarrow0.
> \tag{4.6}
> \]
> Every \(\rho_M\) is certified without querying the exact positive-time
> solution. In a response-Galerkin realization it must include, at minimum,
> current-state projection error, the depth-response residual and boundary
> defect, the outgoing training-time DMFT/law residual, quadrature/readout
> error, and the nonlinear high-to-low stability bound.

The order of limits is:

\[
\boxed{
n\to\infty\ \text{first at fixed }L,\qquad
L\to\infty\ \text{second},\qquad
M\to\infty\ \text{last}.
}
\tag{4.7}
\]

No diagonal or interchange is part of the conjecture.

### 4.4 Evidence-calibrated finite-time version

The currently better-supported statement replaces (4.5) by

\[
\sup_{Y\in\mathfrak R_T}\sup_{0\le t\le T}
\left\|
\mathcal O_M(\Phi_M^tP_MY)-\mathcal O(S_tY)
\right\|_E
\le C_T\rho_{M,T},
\tag{4.8}
\]

with \(M\) and \(C_T\) allowed to depend on \(T\). Bounded activation,
finite-\(T\) energy estimates, and the factorial depth-response tail give a
credible proof route to (4.8) once the exact DMFT state space is constructed.

Equation (4.8) does **not** resolve the horizon-independent research question.
Equation (4.5) does, but is not supported by the present computations beyond
one well-conditioned trajectory.

### 4.5 Separate depth-regular conjecture

For the continuous Gaussian matrix field variant, use the same compiler
definition but replace the target in (A) by

\[
\lim_{n\to\infty}\left(\lim_{L\to\infty}\right)
\]

of discretizations of the same depth-regular field. This is the proper home
for the classical forward equation and for the saved smooth-depth numerical
tables. It must be labeled as a different theorem and must not substitute for
the iid conjecture.

---

## 5. Why proving the conjecture directly proves finite neural-PDE existence

Fix \(\varepsilon>0\). By (4.6), choose finite \(M\) such that

\[
C\sup_{Y\in\mathfrak R}\rho_M(Y)\le\varepsilon.
\]

The compiler outputs the finite autonomous system (4.3), finite readouts, and
the PSD sensitivity factor (4.4). Its size is independent of width, discrete
depth, restart time, and requested horizon. Equation (4.5) gives

\[
\sup_{t\ge0}
\left[
\|f_M(t)-f(t)\|_2
+\sup_s\|G_M(s,t)-G(s,t)\|_F
\right]
\le\varepsilon.
\]

Thus this one finite system is the required accuracy-dependent neural PDE
(or ODE normal form) for all physical time.

Conversely, once “finite neural PDE” is defined to mean an admissible
proof-carrying local compiler, any claimed solution supplies exactly
\(\mathcal C,P_M,F_M,\mathcal O_M,\rho_M\) in (4.3)--(4.6). The conjecture is
therefore the desired existence statement itself, not an auxiliary tail or
stability lemma.

Without the admissibility definition, the converse is not meaningful:
“non-oracular” is an intensional restriction and cannot be recovered from the
input-output curve of a single fixed instance.

---

## 6. Anti-loophole assessment

- **Exact-curve fitting:** forbidden future queries cannot generate the
  coefficients, and a fitted curve does not pass the local residual verifier
  uniformly on \(\mathfrak R\).
- **Arbitrary real encoding:** every coefficient has an effective finite
  derivation and certified enclosure.
- **Time as a hidden source:** autonomy and restart covariance require the
  same future from the same current history state, regardless of its original
  absolute time.
- **Finite ODE packed as one PDE:** allowed only if the underlying finite ODE
  has local provenance and a valid certificate. Packing alone proves
  nothing.
- **One canonical trajectory:** uniformity over (4.1) and a restart
  neighborhood prevents a trajectory-specific playback table.
- **Full \(n\times n\) state retained:** \(d_M\) and every mode count are
  independent of \(n\); full matrices cannot appear in the finite state.
- **Unrestricted two-training-time function retained:** all training-time
  covariance/response objects must be represented by finitely many modes,
  with their outgoing law residual included in \(\rho_M\).
- **Formal Dyson truncation only:** its tail is one term in the certificate;
  the DMFT/law and nonlinear-feedback residuals are separately mandatory.
- **Weak high-mode norm:** the verifier's forcing norm must make the Gram and
  kernel contractions and causal trace continuous.
- **Indefinite approximate kernel:** (4.4) rules it out.
- **Dropped slow direction:** PSD alone does not certify (4.5); the all-time
  stability portion of the proof must detect conditioning or preserve the
  slow/null direction.
- **Finite-time result advertised as all-time:** (4.5) takes the supremum over
  \(t\ge0\), while (4.8) is explicitly a different statement.
- **Smooth-depth substitution:** the target and limit order in (4.7) prevent
  evidence from the correlated-field variant from silently replacing iid
  layers.

The only unavoidable philosophical limitation is that no finite syntactic
grammar can prove it contains every imaginable non-oracular idea. A fixed
proof-carrying verifier is the sharpest mathematically testable replacement
for the informal phrase “does not cheat.”

---

## 7. Ranked remaining lemmas

### Tier 1: defining the target

1. **Fixed-\(L\) dense causal-DMFT theorem.** Prove the width limit with both
   reciprocal Onsager responses and continuous-time Euclidean training.
2. **iid depth-homogenization theorem.** Take \(L\to\infty\) in that DMFT and
   identify \(X_{\mathrm{iid}}\), its topology, observables, and semigroup.
3. **Global restartable well-posedness.** Prove uniqueness and stability of
   the history-state evolution; current one-time marginals are insufficient.

### Tier 2: finite-time compression

4. **Strong state/forcing topology.** Make every local contraction, coherent
   rank-one action, causal trace, Gram, and tangent-kernel readout continuous.
5. **Depth-response residual theorem.** Combine the factorial word tail with
   a boundary-conforming depth approximation in the correct macroscopic
   variables.
6. **Training-time law/response Galerkin theorem.** Produce a finite
   approximation of \(C^h,C^\beta,R^h,R^\beta\) or an equivalent path law and
   compute its outgoing residual.
7. **Nonlinear feedback theorem.** Propagate those residuals through
   response \(\to\) feature \(\to\) adjoint/kernel \(\to\) new response,
   including high-to-low contractions.
8. **PSD discretize-then-adjoint theorem.** Build the finite kernel as a
   sensitivity Gram and bound its defect by the same certificate.

### Tier 3: the unsupported all-time step

9. **Uniform response envelope.** Bound
   \[
   \sup_{t\ge0,r}
   \int_0^1\|D_r(s,t)W(s,t)\|_{\rm op}\,ds
   \]
   or its correct iid-homogenized analogue.
10. **Finite feature-arclength/integrated stability.** Prove a kernel gap,
    integrated observability, or another mechanism giving a horizon-free
    residual budget on the full data/restart family.
11. **Terminal Gram stability.** Control neutral hidden directions and prove
    continuity of the all-depth terminal Gram map.
12. **Uniform conditioning theorem.** Relate the quantitative data class
    (4.1) to every learnable residual direction, or design a certificate that
    resolves slow modes without assuming a kernel floor.
13. **All-time restart tube.** Prove uniform bounds on an explicit
    current-state neighborhood, not only on one canonical trajectory.

### Tier 4: rates and numerics

14. Prove depth/time Sobolev or analytic regularity and resulting
    Kolmogorov-width rates after factoring the Volterra primitive.
15. Measure \(C_A(t)\), residual \(L^1\), outgoing law residual, slow kernel
    directions, and required \(M\) over much longer and ill-conditioned runs.
16. Demonstrate width convergence and replace the retained full matrices by
    an actual finite law/response surrogate.

---

## 8. Final classification

### Proved

- finite-\((n,L)\) scaling, gradients, and PSD tangent kernel;
- finite-time energy envelopes;
- the conditional noncommutative factorial depth-response tail;
- impossibility of exact one-depth closure and full neuron-space low rank.

### Strongly supported

- low depth-word order for the tested finite networks;
- a separate smooth-depth classical limit under depth-coherent
  initialization;
- a finite-\(T\) response-Galerkin program, conditional on constructing the
  exact causal DMFT state.

### Conjectural

- existence and global well-posedness of the iid width-first/depth-second
  causal limit;
- finite approximation of its training-time response/law state;
- any uniform-\(t\ge0\) compiler whose \(M\) is independent of the horizon.

### Falsified or unsupported

- iid layers converging to one classical realized \(W(s,t)\);
- exact closure by current forward/adjoint Grams or row laws;
- width-independent low matrix rank of \(J\);
- PSD alone implying all-time learnability;
- interpreting the current horizon table or raw response SVD as overwhelming
  evidence for horizon-independent compression.

The honest research verdict is:

> The standard iid dense Euclidean model has a credible finite-time causal
> compression mechanism, but the exact macroscopic target has not yet been
> constructed and the all-time horizon-independent compiler is not currently
> supported. The sharp conjecture (4.5)--(4.7) is the correct unresolved
> statement; the smooth-depth numerical success belongs to a separate
> depth-correlated variant.
