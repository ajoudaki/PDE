# Independent numerical and code review of the peeling check

Reviewed 2026-09-21 within the assigned frozen scope. **No blocking implementation defect found for the stated deterministic validation task.** This is an internal code/numerical check, not an interval certificate, proof of floating-point accuracy, or approval for promotion.

## Inputs and independent execution

I read the complete frozen `peel_check.py`, `PEELING.md`, and `PEEL_ATOMS.md`, plus the permitted established `docs/observable_p1.md`. The frozen input hashes were verified before execution:

| Input | SHA-256 |
|---|---|
| `peel_check.py` | `e696b7a5a6ae4231367ac75a0711fd0c72ad16160b928b1510d65fd07ed58584` |
| `PEELING.md` | `5eb8af10ae0d41f3af01de62deae06315519bf41b27142b71de9fa870ffac7d2` |
| `PEEL_ATOMS.md` | `65b67d9e39c93f00f0c739a00b3574f569a12830a23aaad687c646385459f43f` |

No previous run directory, another study, author history, or another reviewer's findings was consulted. I executed the frozen driver once, under a 120-second cap, using:

```text
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python studies/closure_training_onset_20260921/peel_check.py --output data/generated/closure_training_onset_20260921/peel_check_independent_03 --nodes 192 256 --atomic
```

It exited successfully. Its recorded compute time was 0.3235 seconds; Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0, float64. Evidence is in `data/generated/closure_training_onset_20260921/peel_check_independent_03/result.json`, the copied frozen source beside it, and `audit_summary.json`. The last file also records two cheap algebraic checks described below; these did not rerun the full driver or train a model.

## Mathematical implementation checks

**Same initialized target.** The direct route uses the canonical joint lower variables
\(h=\tanh G\), \(k=\tanh(\alpha h+\sqrt\tau Z)\), and independent upper variables \(H_i=\tanh(\sqrt v\widetilde Z_i)\). Its conditional integrations compute \(A_\rho=E[h\tanh G_\rho]\) and \(B_\rho=E[k\tanh G_\rho]\). With \(M=\bigl(\begin{smallmatrix}v+\eta&\beta\\\beta&s+\eta\end{smallmatrix}\bigr)\), the canonical row is
\[
(q_A,q_B)=(\tau+\eta)^{-1}(\alpha v,\alpha\beta+\tau\gamma)M^{-1}.
\]
Expanding this two-by-two inverse gives exactly both coefficient formulas in `direct_setup` and `normalization`; the reverse-response contribution \(\tau\gamma\) is retained. At zero readout, the other parameter blocks have zero instantaneous output derivatives, so this upper activation Gram is the initialized tangent/readout kernel specified by the assignment. Both routes share these target constants and normalization formulas. Their agreement is consequently not an independent test of the underlying maintained source rule; the source-row identification was checked against the allowed established document.

**Cauchy coefficients: direction and scale are correct.** For \(f(z)=\tanh z\), real center \(z_0\), and radius \(r=1.15<\pi/2\),
\[
f^{(j)}(z_0)/j!=r^{-j}(2\pi)^{-1}\int_0^{2\pi}f(z_0+re^{it})e^{-ijt}\,dt.
\]
The forward FFT has the required negative exponential, division by 512 supplies the averaging factor, and division by \(r^j\) supplies the radius factor. No extra factorial belongs in `powers @ derivative`. The finite FFT aliases coefficients of indices \(j+512\ell\), \(\ell\ge1\); it is not the exact Cauchy integral. Analyticity on a larger circle of any radius between 1.15 and \(\pi/2\) gives a geometric alias bound in exact arithmetic. The driver does not implement or certify that bound or floating-point error. Discarding the imaginary part is consistent with real derivatives, but its numerical residual is not logged. A cheap independent recurrence \(Q_{j+1}=(1-t^2)Q_j'\) at seven real centers and orders 0 through 8 agreed with extraction within **1.4052e-16** overall.

**Coherent finite lower Gram is implemented.** `truncated_k` is one common polynomial table used for \(\beta_N\), \(s_N\), and \(B_{N,\rho}\). In particular \(s_N\) is its weighted square, not a separately truncated derivative identity; \(\gamma_N=1-s_N\). Since the normalized quadrature weights are positive, the two-by-two table is a Gram matrix before ridge addition, in exact arithmetic for these discrete tables. Adding \(\eta I\) therefore retains positivity. The direct ridge minimum eigenvalues were 0.09148632591129857 and 0.09148632591129843, respectively. Explicit determinant arithmetic is not a numerically universal substitute for a stable solve, but these observed matrices are comfortably away from singularity.

**Upper cosine transform and polynomial map are correct.** Root nodes are \(\cos((k+1/2)\pi/(m+1))\). The factor \(2/(m+1)\) and halved zeroth transform row give Chebyshev coefficients with the convention used by `chebval`. The tensor transform computes the coefficients of \(P_{m,R}(aH_1+bH_2)\) in \(T_i(H_1)T_j(H_2)\): its degree in either variable is at most \(m\), so interpolation at \(m+1\) nodes in each variable is exact for that polynomial in real arithmetic. This avoids conversion to ill-conditioned monomials without changing the finite polynomial represented.

For \(\nu_j=E[T_j(H)]\), the implemented identity
\[
G_{ij}=E[T_i(H)T_j(H)]=(\nu_{i+j}+\nu_{|i-j|})/2
\]
is the cosine product identity, also valid when either index is zero. Independence gives
\(K_{\theta\phi}=\sum_{i,j,k,l}P_{\theta,ij}P_{\phi,kl}G_{ik}G_{jl}\).
Thus `gram @ p @ gram` followed by the displayed elementwise contraction has the correct index orientation. A separate degree-8 check using four weighted support points and three coefficient pairs compared this contraction with explicit polynomial evaluation under the same product rule; maximum difference was **1.1103e-16**.

## Fresh observed errors

All tabulated errors are maxima over the 81 entries of the prescribed nine-angle kernel table. They compare the atomic route with the direct route using the same quadrature resolution.

| Matched lower/upper degree | 192 nodes | 256 nodes |
|---:|---:|---:|
| 8 | 3.5540399990068583e-3 | 3.5540399990069693e-3 |
| 16 | 2.9271061225411010e-6 | 2.9271061227631456e-6 |
| 32 | 1.7438006594261424e-10 | 1.7437956634225316e-10 |
| 48 | 1.6098233857064770e-15 | 2.4980018054066022e-15 |
| 64 | 9.9920072216264090e-16 | 4.9960036108132040e-16 |

The maximum over all 25 degree pairs at either resolution is the degree-(8,8) entry above. The direct kernel refinement change, 192 to 256 nodes, is **2.7755575615628914e-16**. The corresponding degree-(64,64) atomic kernel change is **1.1102230246251565e-15**. Saturation and nonmonotonicity near machine precision should not be interpreted as further resolved convergence.

At degree 64, lower errors \((|\Delta\beta|,|\Delta s|,\max|\Delta\Lambda|)\) are `(2.7756e-17, 0, 2.2204e-16)` at 192 nodes and `(5.5511e-17, 5.5511e-17, 4.4409e-16)` at 256. At 256 nodes the upper-only polynomial comparison is 6.661338147750939e-16. The recorded exact-arithmetic upper analytic bound at that degree is about **4.82815e-10**, which is much larger than the observed discrepancy and excludes the lower truncation and numerical integration errors.

## Limits of the evidence

The exact lower expansion and upper polynomial constructions in the frozen mathematical dependency match the program. The global radius argument requires the exact Gaussian rotational marginal and centered independent lower pairs. The driver inserts quadrature approximations into that radius formula; it does not certify a global radius for the continuum problem. On the tested panel the observed maximum \(|a|+|b|\) is 1.7223081777121334, comfortably below the degree-64 radius 2.5251332847217256. This panel observation is not the mathematical all-angle proof.

The Gaussian rule is a positive, normalized Gauss–Legendre rule on [-10,10]. The omitted scalar Gaussian mass is 1.5239706048321186e-23, but this number alone does not bound the error of the nonlinear, ridge-normalized output. Refinement at fixed cutoff approaches a truncated distribution, and the two routes share quadrature and several algebraic components. The driver does not supply rigorous quadrature error, propagated tail error, roundoff bounds, or certified derivative extraction. Nine angles do not numerically establish uniform convergence on the circle. The reported `upper_kernel_bound_exact_arithmetic` covers upper interpolation only; the program does not evaluate the complete \(4\ell_N+2e+e^2\) bound. Uniform convergence and the full analytic remainder claims stand on the mathematical argument with exact moments, rather than these floating-point measurements.

Within those limits, the fresh execution and algebraic checks support the claimed implementation of a convergent Gaussian-atom evaluation hierarchy for the fixed initialized p=1 kernel. They establish neither a finite terminating identity nor a training or neural-width limit.
