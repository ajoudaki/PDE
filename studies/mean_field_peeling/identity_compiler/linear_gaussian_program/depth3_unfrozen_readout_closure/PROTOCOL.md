# Protocol: unfrozen-readout depth-three autonomous closure

Status: frozen before the final source construction and coefficient checks,
20 August 2026.

## Model

In normalized coordinates the one-sample, three-hidden-layer linear feature is

\[
f_n=a_n^{\mathsf T}R_nB_nx_n,
\]

where \(a_n,x_n\in\mathbb R^n\),
\(R_n,B_n\in\mathbb R^{n\times n}\), and every normalized entry is initially
independent \(N(0,1/n)\).  Feature time is

\[
\begin{aligned}
a_n'&=R_nB_nx_n,&
R_n'&=a_n(B_nx_n)^{\mathsf T},\\
B_n'&=(R_n^{\mathsf T}a_n)x_n^{\mathsf T},&
x_n'&=B_n^{\mathsf T}R_n^{\mathsf T}a_n.
\end{aligned}
\]

For the full squared loss, every right-hand side is multiplied by
\(2\eta e_n\), where \(e_n=y_\star-f_n\).

## Admissible result

The target may use a fixed finite number of one-time fields, kernels, or
operator-valued probability sources.  Their domains and laws must be explicit
and independent of width, Taylor order, elapsed time, and requested horizon.
The state must be autonomous and restartable, and prediction and loss must be
current-state readouts.

The following do not satisfy the target:

- a width-dependent matrix or atomic measure with \(n\) atoms;
- a response or correlation kernel carrying two training times;
- a Volterra playback of the past trajectory;
- a growing list of scalar moments or noncommutative words;
- a source fitted from the loss curve or an encoding of the future trajectory;
- agreement of finitely many Taylor coefficients without a positive-time
  width-limit proof.

A fixed noncommutative probability source is admissible only if it is given
constructively, its number is finite, and the evolving perturbation belongs to
a specified width-independent function/operator ideal.  An equivalent scalar
kernel IDE on a fixed source coordinate must be displayed.

## Claim ladder

1. Exact finite-width cyclic and central reductions.
2. One explicit deterministic initialization source.
3. A locally well-posed autonomous, restartable one-time ODE/IDE.
4. Direct formulas for \(f\), the feature kernel \(K\), residual, and loss.
5. Uniform-in-probability identification on every compact physical-time
   interval.
6. Global physical-time existence and convergence of the limiting loss to
   zero.
7. A sharp audit explaining why ordinary scalar spectral marginals do not
   replace the noncommutative source.

## Preregistered checks

- Direct finite-dimensional differentiation must give the four parameter
  gradients and \(f'=K\).
- The cyclic lift must satisfy
  \(\mathcal C'=(\mathcal C^{\mathsf T})^3\) and
  \(\mathcal C^{\mathsf T}\mathcal C-
    \mathcal C\mathcal C^{\mathsf T}=\text{constant}\).
- The independent limit construction must reproduce

\[
(F'(0),F^{(3)}(0),F^{(5)}(0))=(4,160,13888).
\]

- The final source and vector field must be frozen before comparison with the
  existing order-thirteen derivative table.

