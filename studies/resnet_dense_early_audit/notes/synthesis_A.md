# Independent synthesis audit A

## Executive conclusion

The constructive and hostile reports are substantially consistent once three
different questions are separated:

1. the literal residual network with weights iid across discrete layers;
2. a different, depth-correlated model whose weights discretize a classical
   matrix field \(W(s)\); and
3. finite-\((n,L)\) truncation of the depth adjoint, which is what the current
   simulations actually implement.

The strongest rigorous positive fact is the operator-norm chronological tail

\[
\left\|J-J_{\le M}\right\|_{\rm op}
\le \sum_{k>M}\frac{C_A^k}{k!},
\qquad
C_A=\int_0^1\|D(s)W(s)\|_{\rm op}\,ds.
\tag{1}
\]

It is noncommutative, survives nonnormality, and has an exact discrete-layer
analogue.  Loss dissipation supplies a width/depth-uniform bound for \(C_A\)
on every fixed training interval.  This gives a serious finite-time
approximation mechanism.

It does **not** yet give the requested finite neural PDE.  Each Dyson word
still contains the dense neuron-space operator; the exact iid-width limit
also has training-time covariance and response memory not contained in the
fixed-time depth propagator \(J\).  A finite compiler must approximate that
full path-space/DMFT state in a strong outgoing-residual norm.

The all-time, horizon-independent claim is much less supported.  Squared
loss gives an \(L^2\)-in-time metric-speed bound, not finite \(L^1\)
feature arclength.  PSD gives monotonic loss, not a uniform tangent-kernel
gap.  The hostile slow-mode example is decisive: absolute kernel errors that
vanish can still cause \(O(1)\) uniform-in-time output error when a learnable
eigenvalue tends to zero.

The numerical study is useful but narrower than its most optimistic reading.
It verifies the scaling, directly confirms iid-depth self-averaging, and
shows striking finite-\((n,L)\), finite-horizon convergence of truncated
backpropagation words.  It neither constructs the width-limit DMFT nor a
finite macroscopic compiler.  Its reconstructed PSD kernel is correctly
labelled as a diagnostic and must not be confused with the cross-kernel that
actually drives the truncated-adjoint trajectory.  The near-aligned run
remains at loss \(0.72\) with a reconstructed kernel
eigenvalue near \(10^{-3}\); it tests a short interval before the slow mode
has learned, not uniform all-time fidelity.

My final assessment is:

> **Finite-time response compression is strongly motivated and has a
> credible theorem route.  The canonical iid-depth all-time finite-PDE
> statement remains a sharp open conjecture.  Current evidence is not
> “overwhelming” for the all-time statement, but it is materially positive
> for the local chronological mechanism.**

## 1. Model lock: the first unavoidable fork

The finite model and learning rates are now audited:

\[
h_r^{\ell+1}
=h_r^\ell+\frac1L\tanh(W_\ell h_r^\ell),\qquad
f_r=\frac1n a^\top h_r^L,
\]

\[
\dot a=-n\nabla_a\mathcal L,\qquad
\dot B=-n\nabla_B\mathcal L,\qquad
\dot W_\ell=-L\nabla_{W_\ell}\mathcal L.
\tag{2}
\]

For \(\mathcal L=\frac12\sum_r(f_r-y_r)^2\), there is no extra factor two.
With the unit-output adjoint \(q_r^L=a\),

\[
q_r^\ell=
\left(I+\frac1LW_\ell^\top D_r^\ell\right)q_r^{\ell+1},
\qquad
\beta_r^\ell=D_r^\ell q_r^{\ell+1},
\tag{3}
\]

and

\[
\dot W_\ell
=-\frac1n\sum_r(f_r-y_r)\beta_r^\ell(h_r^\ell)^\top.
\tag{4}
\]

The finite-difference audit gives relative gradient errors below
\(6.5\times10^{-9}\) and an output-kernel identity error
\(1.04\times10^{-8}\).  There is no remaining normalization disagreement
among the reports.

### 1.1 Literal iid layers do not converge to a realized \(W(s)\)

The user-specified initialization has independent

\[
W_{\ell,ij}\sim N(0,n^{-1})
\]

at every layer.  Its piecewise interpolation is not Cauchy in a strong depth
topology and does not define a classical measurable Gaussian matrix path
with independent nondegenerate values at every \(s\).

For odd \(\tanh\), the initialization residual increments have conditional
mean zero and their cumulative variance is \(O(L^{-1})\).  The final
simulation confirms exactly this:

\[
\begin{array}{c|ccccc}
L&8&16&32&64&128\\ \hline
\|h^L-h^0\|_{\rm rms},\ {\rm iid}
&0.1183&0.0814&0.0562&0.0396&0.0281
\end{array}
\]

and multiplying by \(\sqrt L\) gives approximately

\[
0.335,\ 0.326,\ 0.318,\ 0.317,\ 0.318.
\]

By contrast, the depth-smooth initialization converges to displacement
approximately \(0.291\), not zero.

This resolves a conflict in the requested setup:

\[
\boxed{
\text{iid discrete layers}
\ne
\text{a sampled classical matrix-field neural ODE}.
}
\tag{5}
\]

It would be a technical loophole to “disprove” finite compression merely
because of (5), but it would be equally wrong to silently replace the model.

### 1.2 Two separate legitimate targets

**Literal canonical target.**  Keep iid layers and specify

\[
n\to\infty\ \text{at fixed }L,
\qquad\text{then}\qquad L\to\infty.
\tag{6}
\]

The first limit is a fixed-\(L\) dense causal DMFT.  The second is a
rapid-depth-disorder/Young-measure or homogenization limit.  A pointwise
dense \(W(s)\) is not retained.

**Classical-ODE target.**  Sample one depth-regular Gaussian matrix process
\(W^0(s)\), discretize it, take \(L\to\infty\), and then \(n\to\infty\).
This gives

\[
\partial_sh=\tanh(W(s,t)h)
\tag{7}
\]

but changes the initialization dependence across layers.

The final conjecture below uses the literal target (6).  The smooth-depth
model is a valuable control experiment and a separate conjecture, not
evidence that the literal iid model has a realized matrix-field limit.

## 2. Exact state: what is agreed and what remains formal

At finite \(n,L\),

\[
W_\ell(t)
=W_\ell^0-\frac1n\sum_q\int_0^t
g_q(\tau)\beta_q^\ell(\tau)h_q^\ell(\tau)^\top\,d\tau.
\tag{8}
\]

Therefore

\[
\begin{aligned}
W_\ell(t)h_r^\ell(t)
={}&W_\ell^0h_r^\ell(t)\\
&-\sum_q\int_0^t
g_q(\tau)C^{h,\ell}_{qr}(\tau,t)
\beta_q^\ell(\tau)\,d\tau,
\end{aligned}
\tag{9}
\]

and the transposed field has the reciprocal identity involving
\(C^{\beta,\ell}(\tau,t)\) and \(h_q^\ell(\tau)\).

This proves that the exact state cannot be only:

- current forward and adjoint profiles;
- one-depth tagged laws;
- \(G^h(s,t)\) and \(G^\beta(s,t)\); or
- the fixed-training-time depth propagator \(J(s,u,t)\).

Reuse of \(W_\ell^0\) produces two-training-time covariances and reciprocal
functional responses.  The best exact candidate at fixed \(L\) is the joint
law of tagged histories

\[
(b,A,H,Q,\beta,Z,U)_{0\le\tau\le t}
\]

together with

\[
C^h(t,\tau),\quad C^\beta(t,\tau),\quad
R^h(t,\tau),\quad R^\beta(t,\tau).
\tag{10}
\]

The fixed-time depth response \(J\) is a useful derived component but is not
a substitute for the training-time response kernels in (10).

The reports call (10) a causal path-space DMFT.  That is the correct
structural candidate, but its positive-time derivation, global uniqueness,
restartable history phase space, and \(L\to\infty\) homogenized limit have
not been proved.  The displayed cavity equations in the scaling report
should therefore be labeled **formal candidate equations**, not an
established theorem.

### 2.1 Restartability is history restartability

After eliminating \(W_\ell\), the current one-time marginal is not Markov.
At a restart time \(t_0\), one must retain the causal history or equivalent
accumulated memory variables.  A proper state can be Markov only on an
augmented history phase space.

The numerical restart test initializes from the full finite-width
\((B,W,a)\) state at \(t_0=0.6\).  This is a valid local robustness test for
the finite response truncation.  It does **not** show that a finite
macroscopic state contains enough memory to restart the iid-depth DMFT.

## 3. Constructive and hostile response claims reconciled

### 3.1 The Dyson tail is genuinely rigorous

For either the discrete product or a depth-regular conditional continuum
problem, define

\[
C_A(t)=\int_0^1\|D_r(s,t)W(s,t)\|_{\rm op}\,ds
\]

or its discrete average.  Then (1) follows by submultiplicativity and simplex
volume.  It uses neither commutativity nor normality.

The nonnormal examples in the hostile report refute estimates based on
eigenvalues, average entry variance, or forward Grams.  They do not refute
(1).  There is no contradiction here.

The finite-system energy identity

\[
-\dot{\mathcal L}
=\frac{\|\dot a\|^2}{n}
+\frac{\|\dot B\|_F^2}{n}
+\frac1L\sum_\ell\|\dot W_\ell\|_F^2
\tag{11}
\]

implies on \(t\le T\)

\[
\frac1L\sum_\ell
\|W_\ell(t)-W_\ell(0)\|_{\rm op}
\le\sqrt{T\mathcal L(0)}.
\tag{12}
\]

Thus \(C_A\) is controlled on each finite horizon with constants independent
of \(n,L\), subject to the usual high-probability initialization envelope.
The available bound grows with \(T\), so it does not give a
horizon-independent Dyson order.

### 3.2 Nonnormality

A Jordan or nilpotent coherent direction can have zero eigenvalues and
nontrivial response action.  The experiment with an added nonnormal
rank-one component shows that word truncation still converges for that
particular case:

\[
\begin{array}{c|ccc}
M&2&4&8\\ \hline
\sup_t\|f_M-f\|_2
&2.32{\times}10^{-3}&2.97{\times}10^{-5}&1.10{\times}10^{-8}\\
\sup_{t,s}\|G_M-G\|_F
&1.53{\times}10^{-2}&3.92{\times}10^{-4}&2.81{\times}10^{-8}.
\end{array}
\]

This supports the norm-based Dyson analysis.  It does not audit every
nonnormal generator, and the code does not record \(C_A(t)\) or compare the
observed error with the certified bound (1).

### 3.3 Full neuron-space low rank is impossible

Since \(J(u,u)=I_n\), and under \(C_A\le C\)

\[
\sigma_{\min}(J(s,u))\ge e^{-C},
\]

every rank \(M<n\) approximation has operator error at least \(e^{-C}\).
The numerical SVD is not an SVD of full \(J\); it is an SVD of one scalar
two-depth contraction.  That is the correct potentially compressible axis.

Its normalized singular values are, for example,

\[
1,\ 0.194,\ 0.119,\ 0.086,\ldots,0.030
\]

through index ten in the smooth generic case, and

\[
1,\ 0.272,\ 0.159,\ 0.117,\ldots,0.037
\]

for iid generic.  This is useful decay, but it is not spectacularly
low-rank and is consistent with the \(1/k\) singular values of the causal
Volterra primitive.  Exponential rank claims require factoring that primitive
and then proving regularity of the remaining amplitude.

### 3.4 High-to-low feedback

The hostile examples are valid:

\[
R_n=\frac1nuv^\top,\qquad
\frac{\|R_n\|_F}{\sqrt n}\to0,\qquad
R_nv=u,
\tag{13}
\]

and two discarded high depth modes can multiply into a retained constant
mode.  A weak row-law, normalized-Frobenius, or unweighted \(L^2\) residual
is therefore insufficient.

The constructive response theorem avoids this only conditionally: its
operator/forcing norm must make all Gram, trace, and Onsager contractions
continuous, and the finite system must have a computed outgoing residual in
that norm.  No such norm or residual theorem has yet been constructed for the
actual dense path-space DMFT.

## 4. Nonlinear stability and the all-time gap

A useful abstract residual-gated form is

\[
\dot g=-\Theta(Z)g,\qquad
\dot Z=V(Z)g.
\tag{14}
\]

Under a proved gap

\[
\Theta(Z)\succeq\lambda I,
\tag{15}
\]

Lipschitz bounds, and a residual

\[
\|r_Z(t)\|\le\rho_M\|\widehat g(t)\|,
\tag{16}
\]

the constructive report gives a complete horizon-independent Gronwall
estimate.  This is a correct conditional theorem: the error budget is
integrated against

\[
\int_0^\infty\|\widehat g(t)\|dt
\le\frac{2\|\widehat g(0)\|}{\lambda}.
\tag{17}
\]

The hostile report does not contradict this.  It shows that (15), or a
genuinely equivalent integrated-observability statement, is indispensable.

For

\[
\Theta_\delta=\operatorname{diag}(1,\delta),\qquad
\widehat\Theta_\delta=\operatorname{diag}(1,0),
\]

the kernel error is \(\delta\), fixed-horizon error is \(O(\delta T)\), but

\[
\sup_{t\ge0}\|\widehat g(t)-g(t)\|=1.
\tag{18}
\]

Consequently:

- PSD is not coercivity;
- “nondegenerate data” must be quantitative;
- an all-time theorem cannot be uniform over a class allowing learnable
  eigenvalues to approach zero;
- loss stability alone does not control all hidden Grams.

The final conjecture must make the all-time stability/certificate part of the
claim to be proved.  It must not assume (15) as an unexplained hypothesis and
then count the conditional theorem as resolution.

## 5. PSD audit: theory sound, reconstructed kernel is diagnostic

The exact tangent kernel has the factorization

\[
\Theta
=G^h(1)+G^x\circ G^\gamma
+\int_0^1G^h(s)\circ G^\beta(s)\,ds,
\tag{19}
\]

so positive quadrature and Gram/Schur reconstruction preserve PSD.  A finite
compiler should preferably be constructed “discretize forward, then take the
exact adjoint of that same finite model.”

The snapshot code constructs a PSD matrix from truncated adjoints.  The
frozen rerun explicitly names it the **reconstructed PSD kernel**, which is
the correct terminology.  The code does not claim that the
truncated-adjoint trajectory is gradient flow of this kernel.

The distinction is mathematically important.  The truncated-training
experiment updates the unchanged full forward network using the truncated
adjoint.  Let \(S\) be the exact metric-scaled Jacobian of that forward
network and \(S_M\) the truncated sensitivity used for the update.  Then

\[
\dot\theta_M=-S_M^\top g,
\]

but the actual output derivative is

\[
\dot f=S\dot\theta_M=-SS_M^\top g,
\tag{20}
\]

not

\[
-S_MS_M^\top g.
\tag{21}
\]

The recorded reconstructed kernel

\[
\Theta_M=S_MS_M^\top\succeq0
\]

therefore does **not** govern the recorded approximate trajectory unless
\(S_M=S\) or \(S_M\) is the exact Jacobian of a separately defined
approximate forward model.

This is not merely semantic for interpreting the evidence.  An independent
directional check at the
initial states gives

\[
\|\dot f+\Theta_Mg\|_2
\approx 9.1\times10^{-3}
\]

for smooth generic at \(M=1\), and approximately

\[
8.9\times10^{-2}
\]

for the nonnormal case at \(M=1\).  The mismatch becomes tiny at high order,
as expected from \(S_M\to S\).

Thus:

- the positive eigenvalues reported in the tables verify PSD of the
  reconstructed surrogate, exactly as the frozen column labels now state;
- they are not evidence that the actual cross-kernel in (20) is PSD or that
  the truncated-adjoint training flow is structurally a gradient flow;
- the trajectory-convergence results remain meaningful empirical tests of
  sensitivity truncation;
- a corrected structure-preserving experiment must use an approximate
  forward model with its exact discrete adjoint, or evolve the finite
  macroscopic state and outputs consistently with its Gram kernel.

This is an evidentiary qualification, not a claim that the rerun is
mislabelled.

## 6. Numerical evidence: exact evidentiary weight

### 6.1 What is directly established

1. **Scaling.**  The multipliers \(n,n,L\) and tangent-kernel factorization
   for the exact finite model are numerically verified to near finite-
   difference precision.

2. **Depth model distinction.**  Iid-depth initialization self-averages as
   \(L^{-1/2}\), while the smooth-depth model has a nonzero classical limit.
   This is some of the strongest evidence in the study because it directly
   falsifies the silent identification of the two models.

3. **Smooth discretization.**  Relative to \(L=96\), smooth-depth errors
   decrease:

   \[
   \begin{array}{c|ccc}
   L&12&24&48\\ \hline
   \sup_t|f_L-f_{96}|
   &4.87{\times}10^{-3}&2.08{\times}10^{-3}&7.01{\times}10^{-4}\\
   \sup_{t,s}\|G_L-G_{96}\|_F
   &2.34{\times}10^{-2}&1.02{\times}10^{-2}&3.44{\times}10^{-3}.
   \end{array}
   \]

   This supports the separate classical-ODE discretization, not the iid
   limit.

4. **Finite response truncation.**  Across generic, iid, nonnormal, and
   aligned examples, depth-adjoint word truncation converges rapidly on
   \(T=1.6\).  At \(M=4\):

   \[
   \begin{array}{c|cc}
   \text{case}&\sup_t\|f_M-f\|_2&
   \sup_{t,s}\|G_M-G\|_F\\ \hline
   \text{smooth generic}&2.82{\times}10^{-5}&1.06{\times}10^{-4}\\
   \text{iid generic}&1.86{\times}10^{-7}&3.01{\times}10^{-7}\\
   \text{smooth nonnormal}&2.97{\times}10^{-5}&3.92{\times}10^{-4}\\
   \text{smooth aligned}&1.58{\times}10^{-6}&1.17{\times}10^{-5}.
   \end{array}
   \]

   The generic runs are not numerically lazy: the maximum depth-Gram motions
   are approximately \(1.03\) (smooth), \(0.676\) (iid), and \(1.06\)
   (nonnormal), while their output motions are \(1.15\), \(1.07\), and
   \(1.19\).  The aligned run is the exception: its Gram and output motions
   are both only about \(8.4\times10^{-3}\) on the tested interval.

5. **Finite-state restart robustness.**  From the full finite state at
   positive time, with changed labels and a small state perturbation,
   \(M=4\) errors are about \(10^{-5}\) in output and
   \(1.9\times10^{-5}\) in Grams.  This is a useful anti-playback test for
   the local truncation rule.

6. **Modest parameter sweep.**  Twelve order-four runs over
   \(n=16\)--\(32\), \(L=16\)--\(64\), \(m=2\)--\(4\), two depth modes, gains,
   labels, and seeds have maximum output and Gram errors
   \(3.38\times10^{-4}\) and \(8.70\times10^{-4}\), respectively.

### 6.2 What the data do not establish

1. **No width-limit test.**  The largest width is \(40\) in the
   initialization audit and \(32\) in the parameter sweep.  There is no
   convergence study to a dense DMFT.

2. **No iid homogenized reference.**  The only depth convergence study uses
   smooth correlated weights.  The iid runs remain finite \(L\).

3. **No finite macroscopic state.**  Every truncated trajectory retains the
   full \(B\), all \(L\) dense \(n\times n\) matrices, and \(a\).  Its state
   size grows with \(n,L\).

4. **No training-time memory approximation.**  Only the fixed-time
   depth-adjoint product is truncated.  The two-time DMFT covariance/response
   system is not approximated.

5. **No Galerkin residual certificate.**  Errors are computed against the
   exact finite reference trajectory.  There is no outgoing residual
   \(\rho_M\) evaluated from the approximate state alone and no rigorous
   stability constant.

6. **No all-time horizon.**  Horizon tests stop at \(T=3.2\) and use prefixes
   of the same run.  In the tested generic case the reconstructed PSD kernel
   eigenvalue stays above approximately \(1.54\), and the reference residual
   integral
   \[
   \int_0^T\|f(t)-y\|_2\,dt
   \]
   rises only from \(0.311\) at \(T=0.4\) to \(0.497\) at \(T=3.2\).
   This is precisely the benign finite-residual-budget behavior under which
   early stabilization is expected.

7. **The aligned stress test is finite-time masked.**  Its reconstructed
   kernel eigenvalue is about \(1.15\times10^{-3}\), its reference loss is
   still \(0.7203\) at \(T=1.6\), and its residual integral is already
   \(1.92\).  The slow learning scale is of order \(10^3\).
   Tiny truncation error before that scale does not answer the all-time
   slow-mode objection.

8. **Limited tail/nonnormal stress.**  One nonnormal strength and small
   Gaussian samples do not test rare coherent directions uniformly.

9. **No time-step convergence.**  The Heun step is \(0.025\).  Extremely
   small differences at \(M=6,8\) compare two trajectories using the same
   integrator; they are not certified errors relative to the exact
   continuous-time flow.

10. **SVD decay is not a theorem.**  It concerns one scalar response
    contraction per case and includes the causal triangular structure.

### 6.3 Horizon stabilization interpreted correctly

For orders \(M=1,2,4,6,8\), the prefix suprema stop increasing by
\(T\le3.2\).  At \(M=4\), for example,

\[
\sup\|f_M-f\|=1.48\times10^{-5},\qquad
\sup\|G_M-G\|=1.39\times10^{-4}
\]

at every listed horizon after the early maximum.

This is good evidence that, on one well-conditioned fitting trajectory, most
approximation error is created early and the residual gate later freezes it.
It is not evidence that the same \(M\) works uniformly over all
\(t\ge0\), restarts, and quantitatively nondegenerate problem instances.

## 7. Anti-oracle compiler: repaired grammar

For one fixed dataset, arbitrary real coefficients can encode the exact
future.  “Finite PDE,” “constructive,” and “one source” do not prevent this.
The final statement needs an effective compiler over a varying input and
restart family.

An admissible compiler is one fixed Turing-computable algorithm
\(\mathcal C\).  Its legal inputs are:

- the integer accuracy index \(M\);
- \(m\) and interval/computable descriptions of the data Gram and labels;
- the fixed activation and architecture;
- a finite description of the Gaussian/sub-Gaussian initialization class;
- at restart, only prescribed finite projections of the current augmented
  causal history state.

It may use:

- finite arithmetic and automatic differentiation;
- certified activation/Gaussian quadrature;
- the local forward, adjoint, DMFT covariance/response, and homogenization
  rules;
- prescribed causal bases and Galerkin projection;
- finite positive quadrature and Gram factorization;
- validated integration and interval residual bounds for its own finite
  system.

It may not use:

- samples of the exact positive-time output, Gram, response, or path law;
- the exact target-reaching time;
- arbitrary unlabelled real constants;
- an absolute-time playback table or clock;
- an asserted tail constant defined by the unknown exact trajectory.

The output is a finite autonomous system

\[
\dot z_M=F_M(z_M),\qquad z_M\in\mathbb R^{d_M},
\tag{22}
\]

or finitely many fields restricted to declared finite bases.  Here \(d_M\)
may depend on \(M,m\), and fixed class constants, but not on \(n,L\), restart
time, or requested training horizon.  Writing (22) as a PDE earns no credit;
its local projection provenance and residual certificate are what matter.

## 8. Exact phase space and residual required by the final conjecture

Let \(\mathcal Y_L\) be the fixed-\(L\) augmented causal DMFT candidate (10).
For the iid-depth limit, let \(\mathcal Y\) additionally contain the
depth-indexed type/Young-measure needed by the \(L\to\infty\) homogenization.

A suitable history phase space must control:

- a Wasserstein-2 distance on tagged path laws, with a uniform
  sub-Gaussian/Orlicz envelope for readout and adjoint coordinates;
- the two-time covariance and response remainders in a weighted causal
  Sobolev norm stronger than one derivative on the two-dimensional causal
  triangle, so multiplication and causal traces are continuous;
- the known Volterra/diagonal primitive separately, rather than asking a
  smooth norm to represent its jump;
- depthwise observable sup norms;
- coherent operator actions on every dynamically generated sample/message
  direction.

Concretely, the conjecture below asks for some \(p>1\), \(\delta>0\), and
weight

\[
\omega(\tau)=(1+|\tau|)^{-p}
\]

such that the covariance/response remainder belongs to

\[
H^{1+\delta}_\omega
\]

on the shifted history triangle and the tagged law has uniformly bounded
\(\psi_2\) moments.  Denote the resulting product history space by
\(\mathcal X_{\omega,\delta}\).  The causal boundary trace is an explicit
component of its norm.  This choice is strong enough to reject the weak
high-to-low examples; whether the canonical DMFT actually belongs to it is
part of the conjecture, not an assumption already established.

For projection \(P_M\), reconstruction \(R_M\), and finite solution \(z_M\),
the reconstructed local residual is

\[
\mathfrak r_M
=\partial_tR_Mz_M-\mathcal F(R_Mz_M),
\tag{23}
\]

where \(\mathcal F\) includes:

- tagged forward/backward equations;
- both covariance self-consistency equations;
- both reciprocal training-time response equations;
- iid-depth homogenization;
- causal boundary and trace conditions.

The forcing norm \(\|\cdot\|_{\mathcal F_\omega}\) must dominate all Gram,
Onsager, trace, and coherent-direction contractions.  A valid certificate is

\[
\rho_M
=\eta_M+\|\mathfrak r_M\|_{\mathcal F_\omega}+\zeta_M,
\tag{24}
\]

where \(\eta_M\) is a certified current-state projection error and
\(\zeta_M\) contains finite quadrature/readout defects.  Bounds are computed
from the input class, the local equations, and the finite approximate
trajectory, never from the exact positive-time solution.

The approximate tangent kernel must be constructed as a Gram with positive
quadrature:

\[
\Theta_M
=S_{a,M}S_{a,M}^\top
+S_{B,M}S_{B,M}^\top
+\sum_jw_jS_{W,M}(s_j)S_{W,M}(s_j)^\top,
\qquad w_j>0.
\tag{25}
\]

The certificate must additionally verify a horizon-independent stability
gain.  It may do so through a class-uniform coercivity bound, a relative
spectral estimate preserving all slow modes, or another proved
integrated-observability/finite-arclength mechanism.  Merely reporting
\(\Theta_M\succeq0\) is insufficient.

## 9. Sharp final conjecture

The following statement uses the literal iid-across-depth model and is the
desired compression assertion itself.

> ### Canonical iid-depth dense Euclidean \(\mu\)P certified causal-compression conjecture
>
> Fix \(m\), \(d\), \(\chi=\phi=\tanh\), and constants
> \[
> 0<\kappa_x<K_x<\infty,\qquad Y<\infty.
> \]
> Let \(\mathfrak D\) be the compact family of computably represented sample
> Gram matrices and labels satisfying
> \[
> \kappa_x I_m\preceq G_x\preceq K_xI_m,\qquad
> \|y\|_2\le Y,
> \tag{26}
> \]
> together with the standard independent Gaussian laws
> \(B_{ij}\sim N(0,d^{-1})\), \(W_{\ell,ij}\sim N(0,n^{-1})\),
> \(a_i\sim N(0,1)\).  Train the exact finite network by the Euclidean rates
> \(n,L,n\) in (2).
>
> **Exact target.**  For every \(D=(G_x,y)\in\mathfrak D\), first
> \(n\to\infty\) at fixed \(L\), then \(L\to\infty\).  These limits exist on
> every finite training interval and define a unique global causal
> homogenized DMFT semigroup \(S_t\) on an augmented history phase space
> \(\mathcal X_{\omega,\delta}\) of the form described above.  Its state
> consists of the tagged path law, \(C^h,C^\beta,R^h,R^\beta\), the
> iid-depth type law, and the factored depth-response contractions needed by
> the local equations.  Its readouts are
> \[
> f_D(t)\in\mathbb R^m,\qquad
> G_D(\cdot,t)\in C([0,1];\mathbb S_+^m).
> \tag{27}
> \]
>
> **Restart family.**  Let \(\mathfrak R\) contain every canonical state
> \(S_{t_0}Y_D^0\), \(D\in\mathfrak D,t_0\ge0\), together with a fixed
> \(\mathcal X_{\omega,\delta}\)-neighborhood of dynamically consistent
> histories.  Restarting from \(Y\in\mathfrak R\) means supplying its current
> augmented history/memory state, not its future and not merely its one-time
> marginal.
>
> **Finite compiler.**  There exists one admissible algorithm
> \(\mathcal C\), with the effective grammar in Section 7, such that for
> every \(M\) it outputs:
>
> 1. an autonomous finite system \(z_M'=F_M(z_M)\) with
>    \(d_M<\infty\);
> 2. prescribed projection/reconstruction maps \(P_M,R_M\);
> 3. output and depth-Gram readouts \(f_M,G_M\);
> 4. a PSD tangent kernel of the factorized form (25);
> 5. machine-checkable interval bounds \(\rho_M\) for (24) and
>    \(\Gamma\) for the full nonlinear stability gain.
>
> The number of states, modes, fields, source coordinates, and description
> length may depend on \(M,m,d,\kappa_x,K_x,Y\), but not on \(n,L\), the
> restart time, or any requested physical horizon.  The compiler never
> queries the exact positive-time solution or inserts arbitrary real
> coefficients.
>
> **Certified convergence.**  Uniformly over \(D\in\mathfrak D\) and
> \(Y\in\mathfrak R\),
> \[
> \rho_M\longrightarrow0
> \tag{28}
> \]
> and
> \[
> \boxed{
> \sup_{\tau\ge0}
> \left[
> \|f_M(\tau;P_MY)-f(\tau;Y)\|_2
> +\sup_{s\in[0,1]}
> \|G_M(s,\tau;P_MY)-G(s,\tau;Y)\|_F
> \right]
> \le \Gamma\rho_M,
> }
> \tag{29}
> \]
> where \(\Gamma<\infty\) depends only on the declared class constants and
> not on \(M,D,Y,n,L,t_0\), or the physical horizon.

### 9.1 Quantifier and limit order

The target is formed in the order

\[
\boxed{
n\to\infty\text{ at fixed }L
\quad\longrightarrow\quad
L\to\infty
\quad\longrightarrow\quad
M\to\infty.
}
\tag{30}
\]

\(M\) approximates the already-defined macroscopic target.  The conjecture
does not assume that the \(n,L\) limits commute or that convergence is uniform
over all physical time.  Those would be additional theorems.  The final
macroscopic compression error itself is uniform over \(\tau\ge0\).

### 9.2 Why this statement is the PDE-existence claim, not an auxiliary lemma

For every \(\varepsilon>0\), (28)--(29) give a finite

\[
M(\varepsilon)
\quad\text{with}\quad
\Gamma\rho_{M(\varepsilon)}\le\varepsilon.
\]

The corresponding compiler output is exactly the requested
accuracy-dependent, width/depth/horizon-independent neural PDE/ODE system.
No additional closure theorem is needed.

Conversely, a claimed finite neural PDE does not satisfy this conjecture
unless it has:

- the declared local projection provenance;
- a residual in the strong exact-state forcing norm;
- PSD-consistent dynamics;
- the restart intertwining in (29); and
- uniform observable accuracy.

Thus an oracle curve, arbitrary ODE packing, exact-trajectory coefficients,
or a weak residual cannot prove the statement.  A negative result aimed only
at one-depth Grams, matrix low rank, or one Galerkin basis cannot disprove it.
Resolving (29) within the declared compiler grammar resolves the intended
compression question.

## 10. Qualifications required before using the conjecture

### 10.1 The data class may still be too broad

The quantitative data-Gram floor in (26) excludes nearly identical inputs,
but it does not automatically prove a trained tangent-kernel gap.  If the
class still contains canonical trajectories with arbitrarily slow learnable
directions, the uniform \(\Gamma\) in (29) is false.  This is a substantive
possible falsification of the conjecture, not an avoidable wording trick.

A weaker but defensible first theorem would restrict to a quantitatively
defined small-residual basin in which initial coercivity and kernel
Lipschitzness imply a bootstrap gap.  That would not by itself settle the
desired \(O(1)\) feature-learning class.

### 10.2 Phase-space regularity is part of the conjecture

The weighted \(H^{1+\delta}\)/Orlicz choice is not known to contain the exact
DMFT.  It is proposed because weaker \(L^2\) and row-law topologies fail the
hostile coherent-action and trace tests.  If the exact state lacks this
regularity, one must find a different strong space; silently weakening the
norm until residuals vanish would reopen the high-to-low loophole.

### 10.3 “PDE” is structural, not syntactic

The conjecture permits an ODE Galerkin system.  A finite field on a source
domain is acceptable only through a declared finite basis or another
effectively finite representation.  Packing arbitrary states into one source
variable gives no evidence of compression.

## 11. Ranked synthesis of the remaining mathematical tasks

1. **Iid-depth canonical-limit theorem.**  Prove the fixed-\(L\) dense DMFT,
   including both reciprocal response terms, then its \(L\to\infty\)
   homogenized/Young-measure limit.

2. **Global history-phase well-posedness.**  Construct
   \(\mathcal X_{\omega,\delta}\), prove uniqueness and global restartability,
   and prove the output/Gram readouts and all local contractions are
   continuous.

3. **Uniform all-time stability or its falsification.**  Derive a
   class-uniform coercivity, relative slow-mode control, or finite feature
   arclength from the standard Euclidean dynamics.  Do not assume it.

4. **Uniform response budget.**  Prove a horizon-independent bound replacing
   \(C_A(T)=C_0+O(\sqrt T)\).

5. **Full outgoing-residual compiler.**  Approximate both training-time
   response kernels, the depth type law, and depth-response contractions;
   prove (24) tends to zero without exact positive-time data.

6. **PSD-consistent finite dynamics.**  Build an approximate forward system
   and take its exact adjoint, repairing (20)--(21).

7. **High-to-low stability theorem.**  Close response \(\to\) feature
   \(\to\) adjoint/kernel \(\to\) response in the strong forcing norm.

8. **Uniform restart theorem.**  Prove the same estimates on a neighborhood
   of positive-time augmented history states.

9. **Approximation rates.**  After factoring the Volterra primitive, establish
   Sobolev/analytic regularity and Kolmogorov-width decay in the actual scalar
   macro axes.

10. **Limit-to-finite-network comparison.**  Only after the target and
    compiler are established, quantify finite \(n,L\) deviations and any
    admissible joint regime.

## 12. Final classification

### Proved

- The finite model scaling \(n,n,L\) and exact tangent-kernel formula.
- Exact dense-matrix memory identities (8)--(9).
- Iid depth is not a classical sampled \(W(s)\) field; initialization
  self-averages.
- Operator-norm Dyson tails survive noncommutativity and nonnormality under a
  displayed integrated norm budget.
- Full neuron-space \(J\) has no width-independent low-rank approximation.
- Weak row-law/Frobenius/\(L^2\) residuals and PSD alone are insufficient.
- Conditional on coercivity and a strong residual, the nonlinear feedback
  has a horizon-independent stability estimate.

### Strongly supported numerically

- Rapid finite-horizon convergence of depth-adjoint word truncation in the
  tested finite networks.
- Robustness of that local rule to one positive-time full-state restart,
  small perturbations, one nonnormal construction, and a modest parameter
  sweep.
- Convergence of the separate smooth-depth discretization.

### Conjectural

- Existence and global uniqueness of the literal iid-depth homogenized DMFT.
- A finite Galerkin/cubature approximation of its full two-training-time
  causal state.
- A uniform all-time response budget and finite feature arclength on a
  nontrivial \(O(1)\) data/label class.
- The certified convergence statement (29).

### Falsified or requiring explicit qualification

- Identifying iid layers with a classical realized \(W(s)\) field.
- Exact closure by current one-depth laws and Grams.
- Width-independent low rank of full \(J\).
- Eigenvalue-only response bounds.
- Exponential singular-value decay of the unfactored causal kernel.
- Conflating the correctly labelled reconstructed PSD surrogate with the
  cross-kernel governing the truncated-adjoint training implementation.
- Reading \(T\le3.2\) horizon stabilization, especially the unfitted aligned
  case, as all-time evidence.

The conjecture is therefore scientifically worthwhile and tightly
formulated, but the correct final verdict is not “proved” or “nearly
proved.”  It is a well-defined frontier statement with one compelling local
mechanism, several successful finite-system stress tests, and three central
open fronts: the literal iid-depth DMFT limit, a non-oracular strong residual
compiler, and all-time stability.
