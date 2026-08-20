# Independent numerical-code audit

Audited artifact:

* `run_dense_resnet_audit.py` (stored as `src/run_dense_resnet_audit.py` in
  the original release)
* SHA-256 at audit time:
  `9e23a3ff4cf235369de57b79d3705a5fcaa751de8a1aee4811152a1b200e8128`
* audited outputs: `results/` (stored as `results/final/` in the original
  release)

I did not edit the script.

## Executive verdict

The exact finite-\((n,L)\) implementation is algebraically correct.  In
particular:

* the unit adjoint has terminal value \(a\);
* the raw adjoint is \(Q/n\);
* the hidden adjoint step is
  \[
  Q^\ell=Q^{\ell+1}+\frac1L(D^\ell Q^{\ell+1})W_\ell;
  \]
* the Euclidean \(\mu\)P velocities implement rates
  \(\eta_B=n,\eta_a=n,\eta_W=L\);
* the exact tangent kernel has the correct readout, input, and
  \(L^{-1}\)-summed hidden contributions;
* the ordered-word adjoint truncation is correct and becomes exact when
  \(M\ge L\);
* the current depth interpolation and response-field indexing are correct.

There is one important dynamic-consistency distinction.  At finite truncation
order the code updates parameters with a truncated Jacobian \(J_M\), while the
reported network output still has the exact Jacobian \(J\).  Its actual output
velocity is therefore controlled by the generally nonsymmetric cross-kernel
\[
K_{E,M}=J\,\mathsf M\,J_M^\top,
\]
not by the separately reported PSD reconstruction
\[
K_{M,M}=J_M\,\mathsf M\,J_M^\top.
\]
Consequently, the minimum eigenvalue of \(K_{M,M}\) does not prove that
truncated training is a PSD kernel flow or even a loss-decreasing flow.  The
current column names correctly call it a
`reconstructed_psd_kernel` diagnostic rather than the operative trajectory
kernel.  The static approximation \(K_{M,M}\approx K_{E,E}\) is valid, but it
is not the kernel governing the implemented approximate trajectory.

No computation encodes future data in initial coefficients.  Several
diagnostics are nevertheless **post hoc**: the response SVD, exact snapshot
errors, and positive-time restart state are extracted from the exact
finite-width trajectory.  They are legitimate validation experiments, but
they are not a non-oracular compiler or an a priori residual certificate.

---

## 1. Exact algebra and scaling

Write arrays with samples in rows.  The implemented forward equations are
\[
H^0=\chi(XB^\top),\qquad
Z^\ell=H^\ell W_\ell^\top,
\]
\[
H^{\ell+1}=H^\ell+\frac1L\phi(Z^\ell),
\qquad
f=\frac1nH^La.
\]
The activation family
\[
\phi_g(z)=\frac{\tanh(gz)}g
\]
is smooth and bounded, and the implemented derivative
\[
\phi_g'(z)=1-\tanh^2(gz)
\]
is correct.  \(g=1\) is the requested \(\tanh\) baseline.

The exact backward code implements
\[
Q^L_{r,:}=a^\top,\qquad
\Beta^\ell=D^\ell\odot Q^{\ell+1},
\]
\[
Q^\ell=Q^{\ell+1}+\frac1L\Beta^\ell W_\ell.
\]
Thus \(Q^\ell/n=\partial f_r/\partial h_r^\ell\), as documented.

The vector field is
\[
\dot W_\ell
=-\frac1n(\Beta^\ell)^\top\operatorname{diag}(g)H^\ell,
\]
\[
\dot a=-\sum_rg_rh_r^L,
\qquad
\dot B=-\sum_rg_r\gamma_rx_r^\top.
\]
These are exactly the gradients multiplied by \(L,n,n\), respectively.
There is correctly no factor \(2\), since the loss is
\(\frac12\|f-y\|^2\).

The kernel code implements
\[
\Theta_{rq}
=G^h_{rq}(1)
+(x_r^\top x_q)G^\gamma_{rq}
+\frac1L\sum_\ell
G^{h,\ell}_{rq}G^{\beta,\ell}_{rq}.
\]
The stored exact scaling audit gives errors
\[
1.6\times10^{-11}\ (a),\quad
4.0\times10^{-11}\ (B),\quad
7.0\times10^{-11}\ (W),
\]
and the independently differenced identity
\[
\dot f=-\Theta(f-y)
\]
holds to \(1.04\times10^{-8}\).  Those magnitudes are consistent with the
chosen finite-difference steps.

### Ordered-word truncation

The list `pieces[k]` is the contribution containing exactly \(k\) residual
Jacobian insertions.  Copying the old list before each layer update correctly
preserves chronological order and prevents an insertion from being used
twice at one layer.  An independent check gave maximum adjoint discrepancy
\(8.9\times10^{-16}\) at \(M=L\).

### Depth response

The response snapshot propagates a column perturbation by
\[
v^{\ell+1}
=v^\ell+\frac1L D_r^\ell W_\ell v^\ell,
\]
which is the correct discrete forward Jacobian.  The contraction now uses
`cache.H[u][r]`, i.e. depth first and sample second.  The depth interpolation
also now moves the depth axis to the end before reshaping.  Both corrections
were verified with synthetic affine-in-depth Gram data.

---

## 2. Dynamic-kernel distinction: the PSD reconstruction does not govern truncated training

Let \(S_r^E\) denote the exact metric-weighted sensitivity of output \(r\),
and \(S_r^M\) the sensitivity obtained by the truncated adjoint.  The code's
approximate parameter update is
\[
\dot\theta_M=-\sum_qg_qS_q^M.
\]
But the recorded output is still the exact network function, so
\[
\dot f_r
=\langle S_r^E,\dot\theta_M\rangle
=-\sum_qK^{E,M}_{rq}g_q,
\]
where
\[
K^{E,M}_{rq}
=G^h_{rq}(1)
+(x_r^\top x_q)\frac{\gamma_r^E\cdot\gamma_q^M}{n}
+\frac1L\sum_\ell G^{h,\ell}_{rq}
\frac{\beta_r^{E,\ell}\cdot\beta_q^{M,\ell}}n.
\tag{1}
\]
In contrast, `forward_and_adjoint(..., adjoint_order=M).kernel` replaces both
superscripts in (1) by \(M\).  It is PSD by construction, but it is not the
implemented flow's tangent kernel.

Independent numerical checks found:

* finite differences of the actual truncated vector field agree with
  \(-K^{E,M}g\) to \(4\times10^{-8}\);
* in the production `smooth_generic` configuration,
  \[
  \|K^{E,M}-K^{M,M}\|_F
  \]
  was \(1.06\times10^{-2}\) at initialization and \(1.82\times10^{-1}\)
  at the exact final state for \(M=1\);
* the reported static “output velocity error” at initialization for
  \(M=1\) was \(5.18\times10^{-2}\), whereas the actual truncated-training
  velocity error was \(4.28\times10^{-2}\);
* a broader nonnormal random search found
  \[
  \lambda_{\min}\!\left(
  \frac{K^{E,M}+(K^{E,M})^\top}{2}
  \right)<0
  \]
  in an extreme case, even though \(K^{M,M}\succeq0\).

Required resolution **if** the experiment is used to claim PSD approximate
training:

1. either construct a consistent approximate forward/readout whose Jacobian
   is \(J_M\), so that \(K^{M,M}\) genuinely governs its output;
2. or retain the present truncated-gradient experiment but compute and report
   \(K^{E,M}\), the minimum eigenvalue of its symmetric part, and the actual
   loss derivative;

The current names
`min_reconstructed_psd_kernel_eigenvalue` and
`reconstructed_psd_kernel_action_error` correctly implement the necessary
semantic qualification.  If no claim is made that \(K^{M,M}\) generates the
trajectory, there is no remaining algebraic code defect here; the missing
cross-kernel is then a coverage caveat.

The existing output and Gram trajectory errors remain valid measurements of
the particular truncated-gradient vector field.  What fails is the
interpretation of its stored PSD kernel.

---

## 3. Error metrics and reference solvers

For histories on the same depth grid, the code correctly computes
\[
\max_{t_j}\|f_M(t_j)-f(t_j)\|_2
\]
and
\[
\max_{t_j}\max_{\ell}
\|G_M^\ell(t_j)-G^\ell(t_j)\|_F.
\]
For depth-resolution runs, the corrected interpolation computes the same Gram
norm after mapping the coarse depth grid to the \(L=96\) grid.

The word `sup` in the CSV headers means a maximum over recorded time points,
not a certified continuous-time supremum.  Most runs record every second
Heun step, so the spacing is \(0.05\).  In addition:

* training uses fixed \(dt=0.02\) or \(0.025\);
* no \(dt\)-refinement study is performed;
* the “continuous-depth reference” is \(L=96\), not an independently solved
  continuum ODE;
* all truncation orders share the same integrator, so their very small
  pairwise errors can be far below the unknown absolute time-discretization
  error.

These are not algebraic errors, but a high-resolution-reference claim should
add convergence in both \(dt\) and reference depth, and either record every
step or label the quantities `max_recorded_*`.

The depth-resolution output table uses a componentwise maximum, while the
other experiments use the sample-vector \(\ell_2\) norm.  The columns are
labelled differently, but a final comparison should standardize the norm.

---

## 4. Oracularity and compression audit

Nothing in `initialize`, `vector_field`, or the truncated training loop uses
future outputs, target-reaching times, or fitted coefficients.  The smooth
depth experiments couple different \(L\) values through the same finite
Fourier Gaussian field, which is an appropriate non-oracular convergence
coupling.

The following are validation-only, not compiler ingredients:

* `response_snapshot_audit` is evaluated at the exact positive-time final
  state and compares with the exact adjoint/kernel;
* its singular vectors/values come from the exact positive-time response
  matrix;
* restart experiments begin from the full finite-width state
  \((B,W,a)\), including all \(n^2L\) hidden weights;
* all residual errors are measured against the solved reference trajectory.

Thus the script contains no hidden future encoding, but it also does not test
restartability of a **compressed macroscopic state**, and it does not output
an a priori residual certificate.  Using the observed exact-trajectory SVD
basis or exact snapshot error to choose \(M\) would be oracular unless replaced
by a local, computable bound from the approximate state.

The truncated trainer retains the full \(W_\ell\), all width-\(n\) features,
and exact forward propagation.  As the module docstring correctly says, it is
not the desired width-independent PDE.

---

## 5. Spot-check of the frozen results

The entire current script was rerun independently.  Every CSV checksum matched
the original release's `results/final/` directory exactly; those files are now
exposed directly under `results/`.

### Depth initialization and convergence

The iid-depth terminal displacement has log-log slope
\[
-0.519,
\]
consistent with \(L^{-1/2}\) self-averaging.  The smooth-depth slope is
\(0.004\), consistent with a nonvanishing depth ODE.

After the interpolation correction, errors against \(L=96\) decrease:

| \(L\) | output error | maximum depth-Gram error |
|---:|---:|---:|
| 12 | \(4.87\times10^{-3}\) | \(2.34\times10^{-2}\) |
| 24 | \(2.08\times10^{-3}\) | \(1.02\times10^{-2}\) |
| 48 | \(7.01\times10^{-4}\) | \(3.44\times10^{-3}\) |

### Word truncation

For the chosen \(n=24,L=40\) examples, trajectory errors fall rapidly with
\(M\).  In `smooth_generic`, the maximum output error decreases from
\(2.11\times10^{-2}\) at \(M=1\) to \(7.83\times10^{-9}\) at \(M=8\).
The iid, nonnormal, and aligned cases show the same qualitative convergence.
The 12-point parameter sweep gives \(M=4\) output errors between
\(7.7\times10^{-8}\) and \(3.4\times10^{-4}\).

The horizon experiment shows finite-window stabilization on its one tested
trajectory: for \(M=1\), the maximum output discrepancy is already
\(3.07\times10^{-2}\) by \(T=0.4\) and does not increase through \(T=3.2\).
This is evidence on one finite horizon, not horizon-independent certification.

The positive-time restart and perturbed-state restart give nearly identical
error-versus-\(M\) curves.  This supports local robustness conditional on the
full state.

### Hostile cases and negative evidence

The nearly aligned case is not a successful fitting run:
\[
\mathcal L_{\rm ref}(1.6)=0.7203,\qquad
\lambda_{\min}(\Theta)\approx1.2\times10^{-3}.
\]
Its maximum depth-Gram motion is only \(8.39\times10^{-3}\), versus
\(0.68\)--\(1.06\) in the other three stress cases.  Its small surrogate
error therefore partly reflects very slow motion.  It should be
reported explicitly as a poorly conditioned/failed-to-fit case, not only as a
truncation success.

The scalar response matrices are numerically full rank (40 nonzero singular
values out of the 41-grid representation).  Their decay is modest rather
than spectral: in `smooth_generic`,
\[
\sigma_{20}/\sigma_1=1.71\times10^{-2},\qquad
\sigma_{40}/\sigma_1=9.51\times10^{-3},
\]
and the relative Frobenius tail after ranks \(4,8,16\) is approximately
\[
0.143,\quad0.100,\quad0.066.
\]
This does not establish low-rank response compression.  It is compatible
with the slow singular decay of a causal Volterra kernel.  No Galerkin
surrogate is actually built from these modes.

---

## 6. Coverage caveats

These are limitations rather than implementation errors.

* The parameter sweep varies \(n,L,m\), activation gain, labels, seed, and
  depth mode jointly.  It tests breadth but cannot establish convergence in
  any one variable.  A width-independence claim needs matched problems with
  only \(n\) varying.
* The hand-selected grid is called a “Latin-hypercube sweep,” but it is not a
  generated or stratification-verified Latin hypercube.
* The nonnormal stress adds a coherent rank-one nilpotent component, but the
  code does not measure transient gain, numerical abscissa, pseudospectra, or
  commutator size.  “Nonnormal” is a construction label, not a quantified
  response-growth test.
* The response SVD uses one scalar contraction, one sample/source pair, and
  one positive-time snapshot.  It is not an approximation of the full
  matrix-valued response family.
* Only one positive restart time is used, and the restart retains the full
  finite-width state.
* No approximate-kernel residual/stability theorem is tested, and no
  high-to-low mode feedback certificate is computed.
* Smooth-depth initialization intentionally changes the iid-across-layer
  canonical model.  It is appropriate for a classical matrix-field neural
  ODE, whereas the iid-depth results test the model as originally stated.

---

## Required fixes versus caveats

### Required before claiming a PSD approximate training system

1. Add the actual cross-kernel \(K_{E,M}\), its symmetric-part eigenvalue,
   and the actual loss/output derivative for the current truncated-gradient
   flow; or construct a consistent approximate model whose output Jacobian is
   \(J_M\).
2. Continue to keep the current `reconstructed_psd_*` qualifier.  Those
   columns are correct static diagnostics, not trajectory generators.

### Needed before describing the numerical evidence as a certified
continuous-depth/all-time approximation

1. Add \(dt\) and reference-\(L\) refinement.
2. Distinguish recorded-grid maxima from true time suprema.
3. Build and test an actual finite Galerkin response surrogate rather than
   only plotting an exact-trajectory scalar SVD.
4. Test restart from a compressed state and compute a non-oracular residual.

### Caveats that do not invalidate the current finite experiments

* limited seeds and confounded parameter sweep;
* full-width state retained throughout;
* one finite horizon and one restart time;
* unquantified nonnormality;
* slow, full-rank response singular-value decay;
* aligned case fails to fit on the tested horizon.
