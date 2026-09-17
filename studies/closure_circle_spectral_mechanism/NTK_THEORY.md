# Initial tangent kernel and frozen dynamics on the circle

Status: exact derivation below; floating quadrature is separately checked by
`NTK_CHECK.py`. This is study material, not a promoted result. Scope is the
bias-free two-hidden-layer tanh model, unit mobility multipliers, and normalized
inputs `x(alpha)=sqrt(2)(cos(alpha),sin(alpha))`. The baseline freezes the full
initial population tangent kernel. It is consequently also the population
model obtained by freezing both hidden layers and training only the readout.
It does not approximate the moving nonlinear kernel at later times by theorem.

## Provenance and scope

The assigned scientific inputs read completely were
`code/pde/finite_network.py`, `docs/NOTATION.md`, `code/README.md`, and the
analytic body of `docs/global_nonlinear.md` C.5, from its heading through
“Finite clocks and limitations” (lines 21314–21967 in the inspected version).
C.5's later arithmetic certificate is not needed for this baseline and was
not read. The derivation here imports no risk-advantage theorem, nonlinear-flow
limit, or source-response theorem from C.5. Initialization convergence and
frozen dynamics are proved below directly from the finite definition.
Source hashes and current HEAD are retained in the fresh check record.
Required process instructions and the mathematical/research skills were read.
An initial overly broad filenames-only listing exposed other study names,
but no scientific contents, results, summaries, or prior verdicts were read.
No sibling analysis was seen before freezing these files.

## Why only the readout block remains

Write `A=W^(1)`, `B=W^(2)`, and `a=W^(3)` for the stored parameters at
width `n`. Their independent entry variances are `1`, `1/n`, and `1/n^2`.
For a direction `u(alpha)=(cos(alpha),sin(alpha))`, put

\[
 z^1_\alpha=A u(\alpha),\quad h^1_\alpha=\tanh(z^1_\alpha),\quad
 z^2_\alpha=B h^1_\alpha,\quad h^2_\alpha=\tanh(z^2_\alpha),\quad
 f_{n,\alpha}=a^T h^2_\alpha/n.
\]

The mobilities are `(n,1,n)`. With diagonal gate matrices
`D^ell_alpha=diag(tanh'(z^ell_alpha))`, define
`delta^2_alpha=D^2_alpha a` and
`delta^1_alpha=D^1_alpha B^T D^2_alpha a`. Differentiating the output and
contracting the same parameter block with its mobility gives, exactly,

\[
 K^{1}_{n,\alpha\beta}
 =\cos(\alpha-\beta)\frac{(\delta^1_\alpha)^T\delta^1_\beta}{n},
\qquad
 K^{2}_{n,\alpha\beta}
 =\frac{(h^1_\alpha)^Th^1_\beta}{n}
  \frac{(\delta^2_\alpha)^T\delta^2_\beta}{n},
\qquad
 K^{3}_{n,\alpha\beta}=\frac{(h^2_\alpha)^Th^2_\beta}{n}.
\]

Since every gate has operator norm at most one and `a` is independent of
all hidden fields, conditioning on `(A,B)` gives

\[
 E_a\|\delta^1_\alpha\|^2
 =n^{-2}\|D^1_\alpha B^T D^2_\alpha\|_F^2
 \le n^{-2}\|B\|_F^2,
 \qquad E_a\|\delta^2_\alpha\|^2\le n^{-1}.
\]

Here `E||B||_F^2=n`. Thus each hidden kernel diagonal has expectation at
most `n^-2`. Each block is a parameter-Jacobian Gram, so its off-diagonal
absolute value is bounded by the geometric mean of the corresponding
diagonals. Cauchy–Schwarz and Markov's inequality now show that all entries
of both hidden blocks vanish in probability for any fixed finite query set.
The initial output also vanishes: conditional on the hidden fields,
`E_a[f_n,alpha^2]=||h^2_alpha||^2/n^4<=n^-3`.

For the remaining block define, for `-1<=rho<=1` and `v>0`,

\[
 C_v(\rho)=E[\tanh(U)\tanh(V)],\qquad
 (U,V)\sim N\!\left(0,v\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\right),
 \qquad q=C_1(1)>0.
\]

Each first-layer row has the exact Gaussian pair with correlation
`cos(alpha-beta)`. Bounded iid row averaging therefore makes its empirical
Gram converge in probability to `C_1(cos(alpha-beta))`. Conditional on that
entire first layer, the second-layer rows are iid centered Gaussian vectors
with that empirical Gram as covariance. Their bounded product average has
conditional variance at most `1/n`. The conditional product expectation
converges to its limiting covariance integral: covariance square roots
converge in finite dimension, and coupling all Gaussians by one standard
normal vector permits bounded convergence. This argument also handles
coincident or antipodal inputs. Consequently the complete initial kernel is

\[
 \boxed{\quad k(\theta)=C_q\!\left(\frac{C_1(\cos\theta)}{q}\right).\quad}
\]

This establishes convergence in probability for each fixed finite set.
No width rate for a later nonlinear trajectory is inferred. The kernel is
stationary and even. Since tanh is odd, `C_v(-rho)=-C_v(rho)`, hence
`k(theta+pi)=-k(theta)` and all even Fourier modes vanish. Positivity of
every finite kernel Gram follows as a limit of the readout feature Grams.

## Weighted physical-time solution

For positive training probabilities `w_a`, summing to one, the full
squared loss is `L=sum_a w_a(f_a-y_a)^2`. Put `W=diag(w_a)`,
`K_ab=k(alpha_a-alpha_b)`, and `k_xa=k(x-alpha_a)`. The frozen flow is

\[
 \dot f_{\rm train}=-2KW(f_{\rm train}-y),\qquad
 \dot f(x)=-2k_xW(f_{\rm train}-y),\qquad f_0=0.
\]

The factor two is required by the unhalved loss. To solve without assuming
`K` and `W` commute, set `S=W^(1/2) K W^(1/2)=V diag(lambda_j) V^T` and
`b=W^(1/2)y`. Multiplying the residual equation by `W^(1/2)` gives the
ordinary symmetric system `dot z=-2Sz`, `z(0)=-b`. Therefore

\[
 f_t(x)=k_xW^{1/2}V\,\operatorname{diag}(h_t(\lambda_j))V^Tb,
 \qquad
 h_t(\lambda)=\begin{cases}
 (1-e^{-2\lambda t})/\lambda,&\lambda>0,\\2t,&\lambda=0.
 \end{cases}
\]

When `S` is singular, its zero eigenvectors have zero cross-kernel coupling.
Indeed, applying PSD to the Gram augmented by query `x` shows
`k_xW^(1/2)v=0` whenever `Sv=0`: the quadratic form in the additional
query coefficient must be nonnegative for both signs and all magnitudes.
Hence the formula remains bounded as `t` increases, and its infinite-time
limit replaces `h_t` by `1/lambda` on positive eigenvalues and zero on the
nullspace. It interpolates exactly iff `b` lies in the range of `S`.
If `K` is invertible the endpoint is simply `k_x K^-1 y`, independent of
the strictly positive sampling probabilities. Zero-probability data may
be deleted before forming this solution.

The implementation uses the symmetric decomposition, stable `expm1`, and
no ridge. Its documented rank and PSD tolerances are numerical limitations;
the exact formula does not truncate positive eigenvalues. It rejects an
inconsistent endpoint request rather than describing it as interpolation.

## Opposite labels at two angles

Place label `-1` at `-delta/2` and label `+1` at `+delta/2`, with equal
probabilities, and take `0<delta<=pi`. Write `D_delta=k(0)-k(delta)>0`.
Strict positivity has a direct proof. At the first layer,
`q-C_1(cos(delta))=E[(tanh U-tanh V)^2]/2` is positive unless
`U=V` almost surely, because tanh is injective; `delta>0` excludes this.
The same argument at the second layer proves `D_delta>0`.
The label vector is the antisymmetric eigenvector of `K`, of eigenvalue
`D_delta`. Since `2W=I` here,

\[
 f_\infty(\alpha)
 =\frac{k(\alpha-\delta/2)-k(\alpha+\delta/2)}{D_\delta},\qquad
 f_t(\alpha)=(1-e^{-D_\delta t})f_\infty(\alpha).
\]

The endpoint is mirror-odd, `f(-alpha)=-f(alpha)`, as well as antipodally
odd. At the training angles its values are exactly `(-1,+1)`.
The initial loss is one and `L(t)=exp(-2D_delta t)`.
At `delta=0` the opposite labels conflict at the same point: the predictor
stays zero and no interpolant exists.

Specify the Fourier convention before comparing coefficients. With

\[
 k(\theta)=\sum_{m\in\mathbb Z}\widehat k_m e^{im\theta},
 \qquad \widehat k_m=\frac1{2\pi}\int_0^{2\pi}k(\theta)e^{-im\theta}d\theta,
\]

the exact coefficient is

\[
 \widehat f_{\infty,m}
 =-\frac{2i\widehat k_m\sin(m\delta/2)}{D_\delta}.
\]

Equivalently, write `k(theta)=a_0+sum_(m>=1) a_m cos(m theta)`, so
`a_m=2*khat_m` for positive `m`. The real sine coefficient of the predictor
is `2*a_m*sin(m delta/2)/D_delta`, or
`4*khat_m*sin(m delta/2)/D_delta`. Thus a schematic expression proportional
to `k_m sin(m delta/2)/D_delta` requires its factor and Fourier convention
to be stated. Finite time multiplies every coefficient by the same scalar
`1-exp(-D_delta*t)` for this equal-weight two-point design.

In particular normalized spectral power of this frozen predictor is
independent of training time whenever it is nonzero. Its angular dependence
already includes both the stationary kernel spectrum and the sampling
factor `sin(m delta/2)`; an angular trend in a nonlinear method is not by
itself evidence that its feature learning caused that trend.

## Deterministic numerical method and precommitted checks

`NTK.py` uses normalized probabilists' Gauss–Hermite nodes. For a Gaussian
pair it sets `U=sqrt(v(1+rho)/2)*Z+sqrt(v(1-rho)/2)*Z'` and
`V=sqrt(v(1+rho)/2)*Z-sqrt(v(1-rho)/2)*Z'`, with independent standard
normals `Z,Z'`, then performs the tensor contraction. Endpoint, zero-
correlation and oddness identities are imposed directly. There is no finite
network, trained trajectory, empirical fitting, or random seed in the baseline.

The stable `kernel_decrement` uses the squared-increment identity twice.
At finite quadrature, the separately evaluated marginal variance can differ
from the two-dimensional marginal contraction. Accordingly its agreement
with a direct kernel difference is a check, not an imposed identity.

Before executing the retained check, the following gates are fixed:

- Use 48,96,128 nodes and an independent 192-node refinement, including
  separations `1e-4,1e-3,.02,.05,.2,.6,pi/2,pi-1e-4,pi`.
  Maximum absolute 128/192 kernel change must be below `2e-10`.
  The stable decrement at separations through `.02` must agree relatively
  within `2e-7` between 128 and 192 nodes. Direct subtraction's error is
  reported separately because near-coincident subtraction is ill-conditioned.
- On a 1024-point periodic panel, sampled imaginary/even kernel Fourier
  leakage, mirror/antipodal errors, and PSD failure must be below `2e-10`.
  This is a finite panel and quadrature diagnostic, not a continuum certificate.
- On two-, three-, and four-point designs, interpolation residual and
  weighted finite-time matrix-exponential discrepancy must be below `2e-9`.
  The pair closed form and its normalized DFT coefficient identity must agree
  below `2e-9`. Duplicate-consistent and antipodal-consistent labels must
  interpolate; conflicting duplicate labels must reject the endpoint request.
- The independent conditional-Gaussian parameterization at 192 nodes must
  agree with the symmetric 128-node evaluation below `2e-10` on its fixed
  comparison panel.

This is deterministic baseline verification, not a training experiment or a
test of nonlinear-closure superiority. One retained check run uses at most
60 CPU seconds, one thread, and 10 MiB of generated output in a fresh
study-owned `ntk_checks` directory. A validity failure remains recorded and
is reported; no scientific configuration is selected for favorable results.
The retained check includes source hashes, environment versions, command,
actual duration, numerical diagnostics, output hashes, and pass/fail status.
