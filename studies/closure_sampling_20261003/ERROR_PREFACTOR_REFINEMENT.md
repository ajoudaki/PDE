# Polynomial dataset dependence of the all-time prediction prefactor

2026-10-04. **Internally checked continuation** of the same autonomous
neuron-compression study. The frozen geometric derivation, its separate
reconstruction, and the source/assembly audit have passed; the coordinator
also reconstructed the complete new argument. No manuscript,
maintained-book, algorithm, or Git change is part of this result. The source theorem remains an
internally checked study input, not an established book theorem.

## 1. The improved statement

Fix the input dimension \(d\ge2\), hidden depth \(L\ge2\), and a finite
training set \((x_a,y_a)_{a=1}^m\), with
\(\|x_a\|=\sqrt d\). Each reference hidden layer has width \(n\).
The reference is the same realized canonical Gaussian dense network,
trained by the physical-time equations in
[INPUT_DEPTH_REFINEMENT.md](INPUT_DEPTH_REFINEMENT.md), equation (1).
Its readout starts at zero. Activations are real on the real axis and
bounded and holomorphic on a fixed horizontal strip, as in that theorem.

For clarity, the limiting initialized feature covariance is defined by

\[
Q^{(0)}_{ab}=x_a^\top x_b/d,\qquad
Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
\quad Z\sim N(0,Q^{(\ell-1)}).
\]

Write

\[
\gamma=\lambda_{\min}(Q^{(L)})>0,\qquad
\lambda=\min(1,\gamma/m),\qquad
Y=\left(\frac1m\sum_a y_a^2\right)^{1/2}.
\tag{1}
\]

The label condition remains \(0<Y\le c\lambda\), with a sufficiently
small structural constant \(c\). There is no new power of sample count
or gap in this condition. Zero labels give the stationary zero predictor.
The compressed predictor \(f_C\) uses exactly the fixed metrics, moving
hidden matrices, internal residual, and corrected readout of
[STORAGE_QUADRATIC_IMPROVEMENT.md](STORAGE_QUADRATIC_IMPROVEMENT.md),
equations (6)--(11). In particular, the reduced optimizer is autonomous
and is not asserted to be ordinary reduced-network gradient flow.

On the inherited source event, the new bound is

\[
\boxed{
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
|f_C(t,x)-f_n(t,x)|
\le \frac{CY}{\lambda^{3/2}\sqrt n}
\le \frac{C}{\sqrt{\lambda n}}.
}
\tag{2}
\]

The sharper first bound retains the label scale; Section 4 derives it
from the checked geometric estimate. Constants denoted by \(C\) depend
on fixed depth, dimension, and activation bounds, but not on
\(m,\gamma,Y,n\), or time. The original fixed-confidence quantifier is
unchanged: for each fixed dataset and confidence \(1-\eta\), the event
has that probability for every sufficiently large width. Confidence may
be kept in its width threshold, or in a displayed \(C_\eta\) under the
alternative convention. This is not one simultaneous event over
independently initialized widths or a growing-dataset theorem.

For tanh the cap is inactive, so (2) reads

\[
C_{\rm data}\le C Y(m/\gamma)^{3/2}
                  \le C\sqrt{m/\gamma}.
\tag{3}
\]

Thus the explicit sample-count dependence is at most a square root at
fixed conditioning. A dataset whose \(\gamma\) becomes very small can
still have a large constant; no bound on conditioning by sample count
alone is asserted. Neither (2) nor (3) is an optimality claim.

The retained-state bound is unchanged, including all fixed and moving
coordinates and solve caches. With \(\ell_n=\log(en)\), its explicit form
is

\[
C\lambda^{-2}\ell_n^{d+2}
 [\ell_n+\log(e/\lambda)]^{2d}+Cm(d+1).
\tag{4}
\]

For \(\ell_n\ge\log(e/\lambda)\), this is
\(C\lambda^{-2}\ell_n^{3d+2}+Cm(d+1)\). No source family is added,
and the coordinate tolerance remains \(n^{-1}\). The exact-real
preprocessing and precision qualifications are unchanged.

## 2. What changed in the proof

The former scalar comparison supplied the sufficient prefactor

\[
C\lambda^{-1/2}\exp(CY/\lambda^{5/2}).
\]

It bounded residual and raw readout errors separately in norm. This
lost a cancellation: the residual discrepancy that changes the raw
readout is simultaneously damped by the current training-feature Gram.

Here is the exact cancellation. Neuron space carries the compressed
top-layer metric \(H_L\), and a star denotes the corresponding adjoint.
Let \(V_C\) have columns \(h_{C,a}^{(L)}/\sqrt m\), and let \(V_R\)
have columns equal to the actual selected reference features divided by
\(\sqrt m\). The selected reference readout is \(w_R\). Write

\[
e=(c_C-c_n)/\sqrt m,\qquad z=w_C-w_R,\qquad
T_C=V_C(V_C^*V_C)^{-1},\qquad p=T_Ce,\qquad \zeta=z+p.
\tag{5}
\]

Here \(c_C,c_n\) are label minus prediction, and \(w_C\) is the raw
compressed readout. The vector \(p\) is the smallest-norm readout
correction that realizes the normalized residual discrepancy, since
\(V_C^*p=e\). It is a proof variable, not extra stored state.

Let \(\mathcal J_C\) be the operator whose columns are the specified
hidden-parameter update directions divided by \(\sqrt m\). Its Gram,
together with \(V_C^*V_C\), is the runtime's exact residual damping
matrix \(\mathcal K_C=K_C/m\). Set
\(\Delta V=V_C-V_R\) and \(\Delta\mathcal K=\mathcal K_C-K_n/m\).
Then

\[
\begin{aligned}
\dot e&=-2(V_C^*V_C+\mathcal J_C^*\mathcal J_C)e
          -2\Delta\mathcal K(c_n/\sqrt m),\\
\dot z&=2V_Ce+2\Delta V(c_n/\sqrt m).
\end{aligned}
\]

In \(\dot\zeta\), the terms \(+2V_Ce\) and
\(-2T_CV_C^*V_Ce=-2V_Ce\) cancel exactly. What remains is

\[
\dot\zeta=2\Delta V(c_n/\sqrt m)+\dot T_Ce
 -2T_C\mathcal J_C^*\mathcal J_Ce
 -2T_C\Delta\mathcal K(c_n/\sqrt m).
\tag{6}
\]

The companion energy estimate for \(p\) keeps the negative term
\(-2\|e\|_2^2\). Hidden responses have norm \(O(Y/\sqrt\lambda)\),
so their possible contribution to this energy is only
\(O((Y/\lambda)^2)\|e\|_2^2\) and is absorbed under the existing
small-label condition.

One further factor must be retained: the feature-Gram difference is
factorized into \(V_C^*\Delta V+\Delta V^*V_R\), rather than bounded
as an arbitrary matrix. Reference energy and source-space isometry give

\[
\int_0^T\|V_R(c_n/\sqrt m)\|\,dt
                          \le CY/\sqrt\lambda.
\tag{7}
\]

This controls the second term at its actual readout-velocity scale.
Bounding that velocity only by residual RMS would lose an unnecessary
inverse square-root gap and reinstate an exponential dataset constant.

The full argument, including all source defects and the non-diagonal
metric, is in
[ERROR_PREFACTOR_GEOMETRIC_ROUTE.md](ERROR_PREFACTOR_GEOMETRIC_ROUTE.md).
It never treats the specified backward directions as true gradients of
the output under \(H_L\), and never differentiates a source approximation.

## 3. Raw quantitative estimate and endpoint

Let \(s=Y/\lambda\), \(\epsilon\) be the source coordinate error,
and \(M\ge1\) the actual reference carrier maximum through the source
horizon \(T=C\lambda^{-1}\ell_n\). The new raw comparison is

\[
\sup_{t\le T,x}|f_C-f_n|
\le C\lambda^{-1/2}\epsilon
          \exp\{Cs(1+M)\},\qquad
M\le1+Cs\sqrt{\ell_n}.
\tag{8}
\]

The exponent depends on the bounded dimensionless label ratio \(s\),
not on an extra inverse power of \(\lambda\). At unchanged tolerance
\(\epsilon=n^{-1}\), completing the square gives

\[
Cs^2\sqrt{\ell_n}\le\ell_n/2+C's^4,
\qquad
\frac{e^{Cs+Cs^2\sqrt{\ell_n}}}{n}
\le\frac{C}{\sqrt n}.
\tag{9}
\]

This holds directly with a structural constant for bounded \(s\);
it does not ask \(\log n\) to dominate a power of \(m/\gamma\).

For both flows the integrated motion beyond \(T\) is at most

\[
CY\lambda^{-3/2}e^{-c\lambda T}.
\tag{10}
\]

For the compressed readout, this follows by differentiating its
orthogonal-projection formula and using
\(\|\dot T_C\|\le C\lambda^{-1}\|\dot V_C\|\) and
\(\|\dot P_C\|\le C\lambda^{-1/2}\|\dot V_C\|\).
A structural horizon multiplier makes (10) at most
\(CY\lambda^{-3/2}/n\). Comparing each trajectory with its value at
\(T\) controls the supremum over every later time, not just the limit.
Both fitted endpoints are included.

The stochastic/analytic source construction still has its inherited
dataset-dependent sufficiently-large-width threshold. This continuation
does not prove that that entire threshold is polynomial. It removes the
runtime's exponential error prefactor without introducing a replacement
exponential threshold or a finer source accuracy. The mild condition
\(n^{-1}\le Y\), used to retain small reference-response norms, is
explicit; zero labels are handled separately.

## 4. Retaining the label factor in the constant

The geometric proof records the reference readout pairing defect as
\(\|d_R\|\le Cs\epsilon\). Its exact readout identity therefore gives,
before discarding \(s\),

\[
\|\widehat w_C-w_R\|
\le C\{b+s(a+\epsilon)+s\epsilon/\sqrt\lambda\},
\tag{11}
\]

where \(a\) is the hidden-parameter error and
\(b=\|p\|+\|\zeta\|\). Both start at zero. Write \(E=a+b\).
Equation (30) of the geometric proof is an integral inequality with
forcing \(\epsilon/\sqrt\lambda\), so its zero initial condition gives
the sharper version of equation (32),

\[
E(t)\le\frac\epsilon{\sqrt\lambda}(e^{B}-1),\qquad
B\le C_1s+C_2s^2\sqrt{\ell_n}.
\tag{12}
\]

The query readout-pairing error is also \(Cs\epsilon\). Hence (11)--(12)
give

\[
\sup_{t\le T,x}|f_C-f_n|
\le\frac{C\epsilon}{\sqrt\lambda}
          \{s+e^{C_1s+C_2s^2\sqrt{\ell_n}}-1\}.
\tag{13}
\]

This last step does not alter any source space or differential equation.
For \(0\le s\le c\), the elementary inequality \(e^u-1\le ue^u\)
for \(u\ge0\) bounds the braces by

\[
Cs(1+s\sqrt{\ell_n})
                 e^{C_1s+C_2s^2\sqrt{\ell_n}}.
\]

Put \(q=\sqrt{\ell_n}\ge1\). The continuous function

\[
(1+cq)\exp(C_1c+C_2c^2q-q^2/2)
\]

has a finite supremum on \([1,\infty)\), depending only on structural
constants. Thus, at \(\epsilon=n^{-1}\), (13) is at most
\(Cs/(\sqrt\lambda\sqrt n)\). The tail (10) has the same label
factor. This proves the first inequality in (2).

## 5. Evidence and supersession

Three independent bounded routes were frozen before exchanging findings:

- [ERROR_PREFACTOR_SCALED_ROUTE.md](ERROR_PREFACTOR_SCALED_ROUTE.md)
  separated small readout, hidden, and residual scales, reducing but not
  eliminating the exponential gap dependence.
- [ERROR_PREFACTOR_COST_ROUTE.md](ERROR_PREFACTOR_COST_ROUTE.md)
  derived a polynomial prefactor by a finer source tolerance and counted
  its extra storage. That more costly fallback is unnecessary here.
- [ERROR_PREFACTOR_GEOMETRIC_ROUTE.md](ERROR_PREFACTOR_GEOMETRIC_ROUTE.md)
  retained vector cancellation and closed the target with unchanged
  source accuracy, runtime, and retained-state count.

The last route is the operative proof. Its frozen SHA-256 is
`2cf92bcfb35729374b607c348b69ab80ae8e741878155012980ed3ffa580879c`.
The complete separate mathematical reconstruction is
[ERROR_PREFACTOR_GEOMETRIC_CHECK.md](ERROR_PREFACTOR_GEOMETRIC_CHECK.md).
Its final report SHA-256 is
`1238193e77ec198a4493104d0142b21c455c7ab928d2e0c9b530c98587126bf6`.
Its Section 8 also checks the coordinator's sharper label-dependent
corollary in Section 4 above. The independent source-transfer, storage,
time-tail, probability and width-qualification audit is
[ERROR_PREFACTOR_ASSEMBLY_CHECK.md](ERROR_PREFACTOR_ASSEMBLY_CHECK.md),
SHA-256 `3c7dd710943795a326c720ebd3387d4cdb8d847e94a0b25533f80ffa7797ebf4`.
The coordinator read both reports completely and reconstructed the source
isometry transfer, factorized forcing, zero-norm regularization, vector
cancellation, tail, and label-factor conversion.

The earlier exponential prefactor was a sufficient upper bound, not a
demonstrated dynamical instability. These are internal collaborative
checks of the new comparison and its assembly, not promotion reviews or
fresh independent reviews of the entire inherited stochastic-source chain.
No experiments were required for the exact algebraic cancellation.
