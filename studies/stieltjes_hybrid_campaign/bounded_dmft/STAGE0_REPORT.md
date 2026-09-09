# Bounded-DMFT Stage-0 report

## Bottom line

The canonical two-hidden-layer quadratic network has now been mapped, with
all scale factors exposed, to a formal two-species dynamical mean-field system
containing the two reciprocal response kernels required by reuse of the
initial middle matrix.

Several nontrivial Stage-0 checks succeeded:

1. the generalized low-order MFP evaluator independently recovers the
   accepted Gaussian derivatives through \(F^{(5)}(0)\);
2. it supplies the correct finite-\(A\) references for the frozen conditional
   readout law \(A=3\);
3. the exact truncated initialization decomposition is established;
4. the full one-step pathwise responses pass their frozen contact tolerances;
5. setting the responses to zero fails those exact contact identities.

The positive-time DMFT run was **not launched**.  Two frozen unlock conditions
remain unmet:

- the \(S=4096\) Sobol initialization estimate missed the strict component
  tolerances;
- more fundamentally, an independent DMFT-side differentiation through
  \(F^{(3)}(0)\) and \(F^{(5)}(0)\) has not been implemented.

The second point cannot safely be bypassed by automatic differentiation
through a covariance square root: the initialization covariance is rank one,
and the square-root map is singular in the directions that generate new
time modes.  Running a smooth-looking positive-time solver before resolving
that issue would test an arbitrary regularization, not the declared DMFT.

The outcome is therefore a rigorous **Stage-0 lock**, not a negative result
about DMFT or the Stieltjes conjecture.

## 1. Exact object and bounded law

The feature-time network is

\[
z_i=n^{-1/2}\sum_jW_{ij}u_j^2,
\qquad
f_n=n^{-1}\sum_i a_i z_i^2,
\]

\[
\dot a_i=z_i^2,\qquad
\dot W_{ij}=2n^{-1/2}a_i z_i u_j^2,\qquad
\dot u_j=4n^{-1/2}u_j\sum_iW_{ij}a_i z_i.
\]

The primary bounded law is

\[
a_i(0)\sim N(0,1)\mid |a_i(0)|\le3,
\]

without variance renormalization.  The first-layer and middle-matrix
initializations remain standard Gaussian.

The full derivation is in [DERIVATION.md](DERIVATION.md).  Its core order
parameters are

\[
\Phi_1(t,s)=\mathbb E[U(t)^2U(s)^2],
\qquad
G_2(t,s)=4\mathbb E[A_r(t)Z(t)A_r(s)Z(s)],
\]

and the reciprocal responses

\[
A(t,s)=\mathbb E\!\left[
\frac{\delta U(t)^2}{\delta\Xi(s)}\right],
\qquad
B(t,s)=\mathbb E\!\left[
\frac{\delta(2A_r(t)Z(t))}{\delta H(s)}\right].
\]

The output and tangent kernel are read independently as

\[
F_A(t)=\mathbb E[A_r(t)Z(t)^2],
\]

\[
K_A(t)=
\mathbb E[Z(t)^4]
+4\mathbb E[(A_r(t)Z(t))^2]\mathbb E[U(t)^4]
+4\mathbb E[(U(t)Q(t))^2].
\]

A valid solution must satisfy \(F_A'=K_A\).

## 2. Exact finite-\(A\) initialization

For

\[
m_2(A)=\mathbb E[Z^2\mid |Z|\le A],
\]

the recurrence for the conditional even moments is

\[
m_{2k}(A)
=(2k-1)m_{2k-2}(A)
-\frac{2A^{2k-1}\varphi(A)}{2\Phi(A)-1}.
\]

At \(A=3\),

\[
m_2(3)=0.9733369246625414765881224869\ldots.
\]

Hence the exact infinite-width initialization components are

\[
K_a(0)=27,
\]

\[
K_W(0)=36m_2(3)
=35.040129287851493\ldots,
\]

\[
K_u(0)=48m_2(3)
=46.720172383801991\ldots,
\]

and

\[
\boxed{
K_{A=3}(0)=27+84m_2(3)
=108.760301671653484\ldots.
}
\]

The exact finite-width counterpart is

\[
\mathbb E K_{a,n}(0)=27+\frac{288}{n},
\]

\[
\mathbb E(K_{W,n}(0)+K_{u,n}(0))
=m_2(3)\left(84+\frac{1056}{n}\right).
\]

These formulae prevent the finite-\(A\) model from being incorrectly
calibrated against \(111\).

## 3. Generalized MFP references

The isolated reference evaluator changes only the moments of the row/readout
variables in the accepted decorated-forest calculation.  Middle-weight Wick
contractions and first-layer Gaussian moments are unchanged.

As a mandatory control, switching its row law back to a standard Gaussian
gives exactly

\[
\left(F'(0),F^{(3)}(0),F^{(5)}(0)\right)
=
\left(111,\ 1\,685\,184,\ 77\,400\,633\,120\right).
\]

For the frozen \(A=3\) conditional law it gives

\[
\boxed{
F'(0)=108.7603016716534840334\ldots,
}
\]

\[
\boxed{
F^{(3)}(0)=
1\,610\,470.7911171290733\ldots,
}
\]

\[
\boxed{
F^{(5)}(0)=
72\,197\,074\,701.385826246\ldots.
}
\]

Relative to the untruncated Gaussian values, these are lower by approximately
\(2.018\%\), \(4.434\%\), and \(6.723\%\), respectively.  A finite-\(A\)
solver must be tested against these values, not against the Gaussian
integers.

The source is [truncated_mfp_reference.py](truncated_mfp_reference.py), and
the durable output is
[truncated_mfp_A3_order5.json](truncated_mfp_A3_order5.json).

## 4. One-step response/contact audit

The frozen left-contact grid has

\[
h=\frac{0.005}{64}=7.8125\times10^{-5}.
\]

For the first-layer Euler step,

\[
U_1=U_0+2hU_0Q_0,
\]

so the raw derivative is \(R^x_{1,0}=4h\).  The stored response density is

\[
A_{1,0}=\frac{R^x_{1,0}}h=4.
\]

For the second-layer/readout step, differentiating the strict-subdiagonal
source while holding the next-time cavity coordinate fixed gives

\[
B_{1,0}\longrightarrow
12+28m_2(3)
=39.253433890551165\ldots.
\]

The frozen \(S=4096\) antithetic Sobol audit produced

\[
\widehat A_{1,0}
=3.99650392383384,
\]

\[
\widehat B_{1,0}
=39.234602342053236.
\]

Both pass the preregistered tolerances.  The response-free ablation gives
zero for both quantities, so it fails an architecture-specific identity
before any Stieltjes comparison.

This is positive evidence that the factor and orientation conventions in the
two response channels are correct.  It is not a positive-time fixed-point
validation.

An earlier, pre-freeze draft mixed raw discrete responses with response
densities and quoted \(12(1+m_2(3))\) for the second contact.  That value and
the corresponding provisional artifact were retracted.  With density
responses, \(A_{1,0}=4\) enters the forward coefficient already at the first
strict subdiagonal, so

\[
Z_1=H_1+2h(3+4)A_0H_0=H_1+14hA_0H_0,
\]

and the correct second response is \(12+28m_2(3)\).  Equivalently, the direct
initial finite-width drift is \(6az\) from trained-\(W\) motion plus \(8az\)
from reused-\(W\)/first-layer motion.

## 5. Preserved initialization-sampling failure

The same frozen Sobol population estimated

| component | exact | sampled | relative error |
|---|---:|---:|---:|
| \(K_a\) | \(27.0000000\) | \(26.8308975\) | \(0.6263\%\) |
| \(K_W\) | \(35.0401293\) | \(34.3943726\) | \(1.8429\%\) |
| \(K_u\) | \(46.7201724\) | \(46.4861982\) | \(0.5008\%\) |
| total | \(108.7603017\) | \(107.7114683\) | \(0.9644\%\) |

The component tolerance was \(0.5\%\), and the total tolerance was \(0.25\%\).
Both gates failed.  No seed or threshold was changed after observing this.

The top-\(0.1\%\) empirical contribution shares were \(5.93\%\) for \(Z^4\),
\(3.44\%\) for \((A_rZ)^2\), \(5.30\%\) for \(U^4\), and \(4.48\%\) for
\((UQ)^2\).  Thus the frozen sample was not caught by the coarse tail-stop
threshold, but it was still inadequate for the stringent fourth-moment
initialization gate.

This failure is best classified as a QMC/high-moment resolution failure.
It neither contradicts the exact initialization algebra nor bears on the
Stieltjes conjecture.

The complete machine output is
[stage0_contact_audit.json](stage0_contact_audit.json).

## 6. Why naive forward automatic differentiation is invalid

At \(h=0\), every time coordinate of each cavity process is the same static
initial Gaussian variable.  On an \(L+1\) grid,

\[
\Phi_1^{(0)}=3\,\mathbf 1\mathbf 1^\top,
\qquad
G_2^{(0)}=12m_2(3)\,\mathbf 1\mathbf 1^\top.
\]

Both matrices have rank one and an \(L\)-dimensional zero eigenspace.

A sampling implementation normally writes a driver as

\[
H=C^{1/2}\omega.
\]

However, \(C\mapsto C^{1/2}\) is not Fréchet differentiable at a singular
positive-semidefinite matrix in general directions that open its nullspace.
New covariance eigenvalues may appear at order \(h^{2r}\), while the
corresponding driver amplitudes appear at order \(h^r\).  Differentiating an
eigendecomposition or Cholesky factor at \(h=0\) therefore encounters:

- undefined rotations inside the degenerate zero eigenspace;
- eigenvector derivatives containing inverse eigenvalue gaps;
- square-root derivatives singular at zero eigenvalues;
- branch-dependent results if numerical jitter or clipping is introduced.

Adding positive jitter would make the code differentiable but would change
the formal jet being tested.  Fitting a positive-time curve would also be
circular: it would use the scientific trajectory to pass its own pre-run
gate.

For a future positive-time sampler, the frozen protocol separately requires
the unique symmetric principal covariance root.  That removes arbitrary
eigenvector signs and rotations from common-random-number proposals, but it
does not repair the missing derivative of the root at the singular
initialization.

Consequently, the DMFT-side \(F^{(3)}\)/\(F^{(5)}\) gate remains genuinely
open, and Stage 1 correctly remains locked.

## 7. Cholesky-free route to the missing jet gate

The most promising next method is a formal covariance-series/Wick recursion:

1. represent every covariance and response entry as a truncated formal power
   series in feature time;
2. treat the cavity drivers as abstract centered Gaussian symbols specified
   by those formal covariances, without constructing \(C^{1/2}\);
3. expand the causal Volterra updates and pathwise response derivatives
   coefficient by coefficient;
4. evaluate driver products by Wick contraction or Gaussian integration by
   parts,
   \[
   \mathbb E[X_iP(X)]
   =\sum_j C_{ij}\mathbb E[\partial_jP(X)];
   \]
5. close \(\Phi_1,G_2,A,B\) order by order;
6. compare the resulting \(F_3,F_5\) with the independent generalized-MFP
   values above.

This construction is Cholesky-free and naturally retains the Onsager
responses.  At order five it should be much smaller than a positive-time
population solver.  It must nevertheless be implemented as an independent
DMFT-side compiler before it can unlock Stage 1.

A formal pivoted \(LDL^\top\) factorization is a secondary possibility, but
zero leading pivots and order-dependent emerging ranks make it more fragile
than direct Wick recursion.

## 8. Reconciliation with the tagged-site Riccati analysis

The older tagged-site report proves a Riccati comparison conditional on a
one-kernel causal tagged equation with positive initial self-response and an
unbounded Gaussian readout.  The current derivation clarifies two limitations:

1. the canonical full DMFT has two reciprocal response channels before any
   projection to one tagged kernel;
2. the repository still lacks the theorem identifying that projected
   tagged equation with the fully coupled finite-width limit.

For the bounded law \(|a_0|\le3\), the extreme-\(a_0\) event used to force
arbitrarily short Riccati times is absent.  The current positive contact
responses show that the local feedback mechanism survives truncation, but
they do not imply instantaneous fitting.

Thus there is no mathematical contradiction:

- the tagged Riccati theorem remains exact under its stated tagged-DMFT and
  unbounded-tail assumptions;
- the present result is a bounded, coupled, Stage-0 calibration;
- cutoff removal and finite-width/DMFT identification remain separate open
  bridges.

## 9. Evidence ledger

| Claim | Status | Evidence / blocker |
|---|---|---|
| Exact finite-width two-species skeleton | proved | direct elimination of \(W(t)\) |
| Formal two-response DMFT mapping and kernel factors | exact under the standard DMFT saddle-point construction | equations in DERIVATION.md |
| \(A=3\) initialization and MFP references through order five | proved/computed exactly to stated precision | generalized forest evaluator plus Gaussian recovery |
| Response-free closure is the canonical DMFT | falsified as an exact architecture identity | it violates both nonzero contact responses |
| Frozen response estimator has correct first contact | empirically supported at one QMC population | both response gates pass |
| Frozen \(S=4096\) initialization sampling is adequate | falsified for the preregistered tolerances | component and total gates fail |
| Discrete DMFT reproduces \(F_3,F_5\) | open | Cholesky-free local jet compiler missing |
| Positive-time bounded DMFT is internally valid | untested | Stage 1 locked |
| Bounded DMFT equals the bounded finite-width limit | open | no width-limit theorem or matched experiment |
| Unbounded Gaussian regular curve exists | open | cutoff removal unauthorized and tagged-tail obstruction unresolved |
| Stieltjes conjecture | unchanged/open | no positive-time or new Hankel evidence generated |

## 10. Reproducibility and stopping decision

The frozen child protocol is [PROTOCOL.md](PROTOCOL.md).  It is bound to the
parent protocol hash

d1e75ad896a3572f77b9bc6ec68a7047219a075645b87d44c520d677fc3b153a.

The Stage-0 tests pass as tests of the preserved outcome: exact Gaussian
recovery, exact finite-\(A\) references, contact-response success, and the
expected frozen sampling failure are all asserted.

No positive-time DMFT result, unbounded Gaussian result, matched finite-width
result, or Stieltjes comparison was computed in this branch.  This respects
both the logical unlock gate and the hard compute budget.
