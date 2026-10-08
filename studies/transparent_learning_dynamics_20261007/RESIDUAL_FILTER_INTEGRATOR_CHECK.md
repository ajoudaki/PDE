# Residual-filtered integration: bounded design and implementation check

2026-10-07. This is an independent local analysis and tiny deterministic code
check, not a global proof, a population-limit theorem, or a reproduction of
the scientific cohort. No numerical source was edited and no cohort was
launched by this check.

## Finding

For the finite dense full model, the proposed filter is a first-order
consistent integrator of the same canonical gradient flow. It exactly
contracts the residual of the current frozen linearization. It does not
unconditionally contract the actual nonlinear residual or control passive
predictions, features, response histories, or population quadrature error.

For the causal population program, replacing every label-driven write by
the filtered deficit gives a closed causal discrete program with the same
frozen-global-coefficient local-probe convention. The force replacement
tends to the original force as the step tends to zero on locally bounded
states. Convergence of the growing history/quadrature program to a regular
continuous flow remains a separate assumption, not a consequence of this
algebra. The finite-step program is changed; the intended continuous model
is not.

The frozen implementation matches this design on the full-model campaign
path. A minor off-campaign Boolean-validation loophole is recorded below.

## 1. Finite dense calculation

There are \(m\) training inputs and \(p-m\) passive inputs. The normalized
input rows are \(v_a\in\mathbb R^d\), and \(S_{ab}=v_a^\top v_b\).
For width \(n\), the implemented dense parameters are

\[
 A\in\mathbb R^{n\times d},\qquad W\in\mathbb R^{n\times n},
 \qquad w\in\mathbb R^n,
\]

with \(z_{1,a}=Av_a\), \(h_{1,a}=\tanh z_{1,a}\),

\[
 z_{2,a}=Wh_{1,a},\quad h_{2,a}=\tanh z_{2,a},\quad
 f_a=n^{-1}w^\top h_{2,a}.
\]

Set \(\delta_{2,a}=w\odot\tanh'(z_{2,a})\) and

\[
 \delta_{1,a}=\tanh'(z_{1,a})\odot W^\top\delta_{2,a}.
\]

Let \(\theta\) concatenate the entries of \(A,W,w\), and let \(J\) be the
Euclidean Jacobian of the training-output vector \(f_{1:m}\) with respect
to those raw parameters. Define the mobility

\[
 M=\operatorname{diag}(nI_A,I_W,nI_w),\qquad
 \|\Delta\theta\|_{M^{-1}}^2
 =n^{-1}\|\Delta A\|_F^2+\|\Delta W\|_F^2+n^{-1}\|\Delta w\|^2.
\]

For current deficits \(c=y-f_{1:m}\), the implemented physical flow is

\[
 \dot\theta=\frac2m MJ^\top c.
\]

Define the equal-time Grams, including passive rows when needed, by

\[
 C^\ell_{ab}=n^{-1}h_{\ell,a}^\top h_{\ell,b},\qquad
 D^\ell_{ab}=n^{-1}\delta_{\ell,a}^\top\delta_{\ell,b}.
\]

Direct differentiation gives

\[
 \partial_{A_{ir}}f_a=\delta_{1,ia}v_{ar}/n,\quad
 \partial_{W_{ij}}f_a=\delta_{2,ia}h_{1,ja}/n,\quad
 \partial_{w_i}f_a=h_{2,ia}/n.
\]

Consequently the training block of the canonical kernel is exactly

\[
 K=JMJ^\top
   =\bigl(C^2+C^1\odot D^2+S\odot D^1\bigr)_{1:m,1:m}.
 \tag{1}
\]

Here \(\odot\) is entrywise multiplication. All quantities in (1) are
computed at the current state, before any parameter block is updated.

For physical time step \(\Delta>0\), put \(h=2\Delta/m\). The proposed step is

\[
 (I+hK)q=c,\qquad \Delta\theta=hMJ^\top q.
 \tag{2}
\]

Since \(K\succeq0\), \(I+hK\) is positive definite even when \(K\) is
singular. No positive Gram-gap assumption or inverse of \(K\) is required.
Equation (2) is equivalently the unique minimizer of

\[
 \frac12\|c-J\Delta\theta\|^2
 +\frac1{2h}\|\Delta\theta\|_{M^{-1}}^2.
 \tag{3}
\]

Indeed, the normal equation for (3) is

\[
 J^\top(J\Delta\theta-c)+h^{-1}M^{-1}\Delta\theta=0;
\]

substitution of (2) reduces it to \(J^\top(hKq-c+q)=0\).
The regularization term makes the objective strictly convex.

The frozen-linearized new residual is therefore exactly

\[
 c-J\Delta\theta=c-hKq=q.
 \tag{4}
\]

In a \(K\)-eigenvector of eigenvalue \(\lambda\ge0\), (4) multiplies the
residual coordinate by \(1/(1+h\lambda)\). Thus \(\|q\|\le\|c\|\);
zero-eigenvalue coordinates are unchanged. This is not necessarily
componentwise contraction or preservation of individual deficit signs.

The actual new residual is instead

\[
 y-f_{1:m}(\theta+\Delta\theta)=q-r,\qquad
 r=f_{1:m}(\theta+\Delta\theta)-f_{1:m}(\theta)-J\Delta\theta.
 \tag{5}
\]

For example, if the Jacobian in the coordinates \(x=M^{-1/2}\theta\)
is Lipschitz with constant \(L\) along the step segment, the integral
Taylor remainder satisfies

\[
 \|r\|\le\tfrac L2\|\Delta\theta\|_{M^{-1}}^2,
 \qquad
 \|\Delta\theta\|_{M^{-1}}^2=h^2q^\top Kq.
\]

The first inequality follows by integrating the Jacobian difference
along that segment. Its constant is local and is not asserted uniform
in width, parameters, or training time. These facts do not establish
unconditional descent of the measured nonlinear loss.

Finally, \(q-c=-hKq\). On a bounded local set, \(q=c+O(h)\), so (2) equals
the ordinary Euler increment \(hMJ^\top c\) plus \(O(h^2)\). For fixed
\(m,n\), the smooth finite dense vector field therefore has the same
first-order continuous-time consistency. This does not make the method
second order or remove the need for step refinement.

## 2. Causal history writes and local responses

In the population equations, use equal-time expectations to define
\(D^1_{ab}=\mathbb E[\delta_{1,a}\delta_{1,b}]\), alongside the existing
\(C^1,C^2,D^2\), and use their training block in (1). Empirical versions
are positive semidefinite Grams; each entrywise product in (1) is
positive semidefinite as the Gram of tensor-product features. Therefore
the algebraic filter is well posed in exact arithmetic at finite
quadrature size too. This does not identify that matrix with the actual
Jacobian of the adaptive finite-particle sampling program.

Keep two different stored arrays:

- \(c^k=y-f_{1:m}^k\): the raw measured training deficit, used for loss.
- \(q^k=(I+hK^k)^{-1}c^k\): the effective force written at step \(k\).

Every label-driven occurrence of a past \(c_b^j\) in the lower-field,
readout, learned-forward-memory, and learned-backward-memory equations
must become \(q_b^j\). It is the filtered force at the historical write
time, not a newly filtered version of the past deficit at the current
state. In particular,

\[
 w^k=h\sum_{j<k,b\le m}q_b^j h_{2,b}^j,
 \qquad
 f_a^k=h\sum_{j<k,b\le m}q_b^j C^2_{ab}(k,j).
 \tag{6}
\]

The reciprocal \(R\) terms are not direct learned writes and are not
multiplied by an additional filter. Their values must nevertheless be
recomputed through the changed local circuit.

There is no current-step algebraic loop. Compute lower features, then
upper features and raw deficits, then the lower backward signal and
\(D^1(k,k)\). Only now is \(K^k\) complete and \(q^k\) available. The
current lower backward signal depends on strict-past learned writes and
the current reciprocal atom; it does not depend on the new \(q^k\).
Use \(q^k\) in the writes that advance to the next step.

For the canonical local Gaussian probes, hold all deterministic global
coefficients fixed, now including \(q\) and the Grams used to compute it.
Then \(\partial q=0\) in the probe circuit. The original first-tangent
recursions remain valid with the same substitutions \(c\mapsto q\) in
their write multipliers. This is why replay must freeze the stored
effective force rather than recomputing a filter after a primitive probe.

By contrast, differentiating the entire self-consistent finite algorithm
would introduce

\[
 dq=(I+hK)^{-1}\bigl(dc-h(dK)q\bigr).
\]

That derivative changes global coefficients and is not the local response
\(R^h\) or \(R^\delta\) defined in the candidate. Inserting it into those
responses would change their meaning. Dense autodifferentiation of an
entire filtered optimizer step is another legitimate calculation, but
would include this derivative and must not be confused with the local
population probe.

The formal consistency statement is limited: on regular bounded history
states, replacing \(c\) by \(q=c+O(h)\) changes a write by \(O(h^2)\).
Turning this into convergence of the complete growing-history system
requires stability and regularity estimates not supplied here. Moreover,
finite-particle same-seed mesh refinement is not a perfectly coupled
trajectory comparison: the sequence of Gaussian queries, retained rank,
and sampling basis can change. Its observed difference includes
discretization and Monte Carlo representation changes, not a rigorously
isolated time-discretization error.

## 3. Passive inputs and control variants

Only the \(m\times m\) training block is used in the solve. A
\(p\times p\) solve with zero padded passive deficits is not equivalent:
its off-diagonal blocks can change training forces. Passive observations
never supply labels or write directions. They still receive changes
through shared parameters and through their prescribed reciprocal terms.

For the dense frozen linearization, the passive output increment is

\[
 \Delta f_a^{\rm lin}=hK_{a,1:m}q,\qquad a>m.
\]

There is no passive target or passive contraction claim. The exact
population history predictor (6) remains valid for passive queries too.

The exact dense identity (1) must use only moving parameter blocks. For
a truly frozen middle matrix, its \(C^1\odot D^2\) block is absent. For
affine-gate controls, features and Jacobians must be those of the actual
affine model. A no-reciprocal or one-sided-memory causal ablation is not
automatically a dense gradient system. Although the same algebraic Gram
sum is still positive semidefinite, using it as a filter would not
justify the frozen-linearization claim for that ablated program. The
new campaign correctly restricts filtered runs to the full model.

At finite particle count, even in the full model,
`kernel_diagnostic_is_gradient_kernel` must be read as identifying the
nominal full-model kernel expression, not as certification that it is
the Jacobian kernel of the adaptive finite-particle implementation.

## 4. Frozen-source implementation check

The checked implementation has the following properties.

- `causal_filtered_integrator.py` forms the filter after recording
  current \(D^1\) and before current lower/readout writes. It uses
  `write_deficit` in both learned-memory histories and both write-tangent
  multipliers. Raw `c` remains separate.
- Its replay wrapper shallow-copies the result and maps replay's fixed
  `c` coefficient to `write_deficit`. It does not modify the original
  result or recompute the filter under probes.
- The dense implementation builds all three current training Gram
  blocks and applies \(h\) exactly once. Its \(W\) write has the required
  additional \(1/n\); its \(A,w\) writes do not.
- The frozen-feature diagnostic now uses the selected discrete
  integrator too and is renamed `frozen_feature_discrete_prediction`.
  It is not the old explicit-Euler baseline in filtered mode.
- `loss_derivative` inherited from the dense observer is the canonical
  instantaneous flow derivative at the saved state, not the measured
  finite filtered-step loss change.
- Dense `write_deficit` contains actual writes only (one fewer row than
  saved states); causal `write_deficit` also contains the unused final
  state's computed force. RK4 dense runs have an empty write array.
  Consumers must account for these different array lengths.
- The runner enumerates 16 dense and 8 causal calls, including the
  declared causal repeat. It was inspected, not executed by this check.
  Its `numerically_unstable` flag is a particular loss-increase
  threshold, not an exhaustive numerical-stability certificate.

Minor API defect, reported before any edit: the full-model guard tests
`learned_middle_memory is False` before the alias is converted with
`bool(...)`. Thus `np.bool_(False)` (or integer zero) bypasses that guard
and subsequently disables both learned-memory directions. Plain Python
`False` is correctly rejected. The frozen cohort uses the default
`None` and full flags, so this does not affect its specified runs.
No numerical source was changed. Future correction should normalize the
alias before checking the effective model flags and receive a new hash.

## 5. Deterministic checks, provenance, and limits

The two producer self-tests were rerun with one BLAS thread. The
population test has \(m=4,p=7,d=3,N=31\), four steps of physical size
0.2, hence \(T=0.8\). The dense self-test has width 23 and uses local
single-step/derivative comparisons, not a training cohort.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python studies/transparent_learning_dynamics_20261007/causal_filtered_integrator.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python studies/transparent_learning_dynamics_20261007/residual_filter_experiment.py selftest
```

Results: old Euler equivalence 0; frozen replay error 0; maximum local
primitive response error \(1.026\times10^{-12}\); readout-history error
\(9.98\times10^{-18}\). The dense directional frozen-linearized residual
error was \(5.33\times10^{-15}\), with passive-exclusion error 0. Local
velocity errors for \(h=10^{-3},5\times10^{-4},2.5\times10^{-4}\) were
0.0009433905, 0.0004720389, 0.0002361055, consistent with first-order
velocity perturbation on that state.

An additional independent test explicitly assembled the raw dense
Jacobian from the three derivative formulas above, rather than using
the producer's kernel expression. Reproducible setup: NumPy generator
seed 904 generates a \(7\times3\) standard-normal input array, normalized
rowwise; use \(m=4,n=19\), labels \((.3,-.2,.4,-.1)\), `initialize(19,3,71)`,
and replace its readout by `np.linspace(-.2,.3,19)`. At \(h=.2\)
(physical step 0.4), compare the directly assembled \(JMJ^\top\),
\(hMJ^\top q\), and \(c-J\Delta\theta\) against the implementation.
Their maximum errors were respectively \(5.56\times10^{-17}\),
\(1.07\times10^{-16}\), and \(5.56\times10^{-17}\). The actual nonlinear
residual differed from \(q\) by \(7.47\times10^{-5}\), illustrating the
distinction in (5). The Boolean guard test used the same inputs with
population size 7 and zero update steps; NumPy false bypassed the guard
and Python false raised `ValueError` as stated above.

The scientific input scope was the three original assigned sources,
then the three newly authorized implementation/runner files. No other
study, other agent's scientific notes, or campaign trajectory data was
read for this check. Required canonical-notation and rigorous-math
instructions governed presentation and separation of claim levels.

SHA-256 at inspection:

| Source | SHA-256 |
|---|---|
| `CANDIDATE_SYSTEM.md` | `6cbcf44784be275ee355d4ecccc80013de1f11605b6a4329b34b2dd51d0b0715` |
| `causal_panel_simulator.py` | `e3eec0c1e7f7692460c804dedc1cce2476324a9c2013b35123efe5db7afd522a` |
| `multisample_experiment.py` | `eb58b62ca466649989067cd1287aa199b99b41899b59536cec02baa186c78b2d` |
| `causal_filtered_integrator.py` | `0d053770e894a7cfd4f361a16cf415ef2ddfad939011d337d92a31c4bc11d4ba` |
| `residual_filter_experiment.py` | `1dceb072e71362eac0f1a5b8a96dddb45db826c4c1068ad99943e54b6e289e50` |
| `run_residual_filter_cohort.py` | `6d8764b2d0274cf5fb1168d2a3ec1ff7facd5b1a0dd238e3e6e34e4df866eb03` |

This audit supports the intended full-model implementation and its local
algebra. It does not establish global stability, mesh convergence,
population-to-dense accuracy, width-uniform bounds, or a resolved
continuous-time feature-learning trajectory.
