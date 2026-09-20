# Independent internal audit of initialized p=1 geometry

Date: 2026-09-18. Reviewer: scoped agent `p1_audit_initial`.
Verdict: **PASS within the stated initialization and finite-data scope.**
This is an internal mathematical review, not a promotion review or approval.
No numerical experiment or numerical coefficient evaluation was performed.

## Frozen inputs and scope

The reviewer read the following scientific inputs, without reading the study
README, other studies, study history, other reports, or prior verdicts:

1. `studies/p1_three_input_geometry_20260918/initial_geometry.md`, complete,
   SHA256 `6856fb3d2cca5d59d1b00c4bd3cf87dd74f87315999e244b42dd1662647f091d`.
2. `docs/observable_p1.md`, complete, as the canonical initialized-coefficient
   and finite-equation dependency,
   SHA256 `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba`.
3. After explicit supplementary authorization from the supervisor,
   `docs/global_nonlinear.md`, C.4.7.9.4 and the energy/existence/restart
   portion of C.4.7.10.D.3. The actual displayed windows were lines
   12290–12390 and 15305–15390, including surrounding boundary context;
   no scientific conclusion from that boundary context was used.
   Full-file SHA256
   `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c`.

Required process inputs were the rigorous-mathematics skill, the
conjecture-investigation skill, and its adversarial-audit reference.
The initial absence of the cited uniqueness dependency was reported to the
supervisor and resolved by the supplementary authorized reading. It is not
an outstanding gap.

The object audited is the exact population closure in dimension two, with
unit input directions, prescribed positive ridge, the full correlated lower
initialization, zero initial readout, and the full evolving middle matrix.
Canonical coefficient identities are checked against the supplied canonical
dependency; no finite-width identification or numerical approximation is
part of the verdict.

## Claim-specific findings

| Claim | Verdict | Decisive check |
|---|---|---|
| Exact active dictionary and two initialized matrix bands, including `tau gamma` | PASS | They agree with the canonical inverse-Cholesky normalization and right-transpose contraction. |
| Coordinate formula `V(u)=(F(u_1),F(u_2))` on the unit circle | PASS | Multiplication of both bands and conditional expectation over the reverse Gaussian produce the displayed `A`, `B`, and `ell`. |
| Analytic `alpha < 6/7 < arsinh(1)` | PASS | The Cauchy–Schwarz bound gives `v>1/4`, then `tau>1/7`; the signed Taylor remainder proves the stated rational bound for `arsinh(1)`. |
| Uniform bounds for `j` and `cosh²(alpha)<2` | PASS | Gaussian interval probabilities give the upper bound and strict decrease; the symmetric hyperbolic identity gives the lower bound. |
| `0<B<1/j_L` | PASS | Conditional Gaussian integration by parts supplies the needed conditional variance, and the ridge supplies a strict positive margin. |
| Strict increase and oddness of `F` on `[-1,1]` | PASS | The affine minimization gives a strictly positive derivative of `ell`; correlation differentiation has an exact integration-by-parts cancellation. |
| Injectivity of `V`, including equality up to sign | PASS | Coordinatewise strict increase and oddness suffice on the stated unit circle. |
| Strict positive definiteness for every finite family without equal or antipodal directions | PASS | Positive upper density reduces to analytic ridge-function independence; the exponential-tail elimination works also for collinear unequal-length vectors. |
| Exact rank with duplicates and antipodal pairs | PASS | The only relations are the explicit signed identifications within unoriented direction classes. |
| Initial velocities, physical energy identity, and stationary classification | PASS | Factors and signs agree with the canonical vector field; zero signed mass in every class is necessary and sufficient. Characteristic uniqueness makes the stationary trajectory constant. |
| Every-angle equilateral-triple conclusions and uniform initial lower bound | PASS | No equal or antipodal directions occur; positivity and compactness give the uniform bound. The coefficient `13/8` is correct. |
| Positivity on a short initial time interval for each fixed admissible configuration | PASS | The characteristic solution makes each trained feature, hence the finite Gram, continuous in time. |
| Signed-permutation covariance | PASS | The displayed feature, mark, characteristic, and matrix transformations preserve every contraction and the physical metric. |
| Failure of full orthogonal covariance of `V` and generic rotational invariance of the lower span | PASS | `F'''(0)>0` precludes a linear `F`; conditional variance followed by a mixed derivative excludes a generic rotated lower feature. |

## Details of the delicate analytic steps

### Coefficients and monotonicity

Writing `q=v+eta`, multiplication of the two initialized bands gives the
coefficient of `E[h_j tanh(G dot u)]` as

\[
\frac1{c_*}\left(\frac{\alpha v}{q}-\frac{L\beta}{b_*^2q}\right)
=\frac A{c_*},
\]

and that of `E[k_j tanh(G dot u)]` as `B/c_*`. Conditioning on `G_j`
replaces `k_j` by `kappa(h_j)`. Since `|u|=1`, the two Gaussian arguments
have unit variances and correlation `u_j`. This verifies the formula without
an independence substitution or removal of the response term.

For `X=sigma² G²`, Cauchy–Schwarz applied to
`sqrt(X/(1+X))` and `sqrt(X(1+X))` gives

\[
E\frac X{1+X}\ge\frac{(EX)^2}{E[X(1+X)]}
=\frac{\sigma^2}{1+3\sigma^2}.
\]

The strict pointwise comparison with `tanh²(sigma G)` gives the strict
bounds on `v` and `tau`. Taylor's theorem applies on the whole integration
interval because the fourth derivative of `(1+x)^(-1/2)` is positive for
`x>=0`. The integral of the cubic polynomial is `1451/1680`, exceeding
`6/7=1440/1680`. Hence `cosh²(alpha)<2` follows exactly, without a decimal
coefficient estimate.

For each nontrivial symmetric interval, translation by `a>0` has probability
derivative `phi_tau(r+a)-phi_tau(r-a)<0`. The density bound permits
differentiation under the level-set integral. The stated hyperbolic identity
is algebraically correct and gives `j(z)>=j(0) sech²(alpha)` on `|z|<=1`.

The conditional variance estimate is especially important. Conditional on
`h`, integration by parts gives

\[
\operatorname{Cov}(Z,k\mid h)=\sqrt\tau\,j(h),
\quad \operatorname{Var}(k\mid h)\ge\tau j(h)^2.
\]

Combining this with `E[kappa(h)^2]>=beta²/v` proves equation (7), with
`E[j(h)^2]` understood as the expectation of the square. Since
`j(h)>=j_L`, `beta<=alpha v j_U`, and
`alpha²(v/(v+eta))j_Uj_L<1`,

\[
Lj_L\le\tau E[j(h)^2]
  +\alpha^2\frac v{v+\eta}\eta j_Uj_L
<\tau E[j(h)^2]+\eta\le b_*^2.
\]

Thus the upper bound on `B` retains the full `tau gamma` term and is strict.
The endpoint values of the affine lower estimate for `ell'/alpha` on
`0<=B<=1/j_L` are exactly `lambda` and
`1-lambda(r_*-1)`. Both are positive because `0<lambda<1` and `r_*<2`.
No positivity of `A` is assumed. This argument also verifies the stated
extension to any positive ridge with the same raw constants; it does not
assert the zero-ridge endpoint.

For `Y_t=tX+sqrt(1-t²)Z`, differentiation initially produces

\[
E\left[\psi(X)\tanh'(Y_t)
\left(X-\frac{tZ}{\sqrt{1-t^2}}\right)\right].
\]

Integration by parts in `X` gives
`E[psi'(X)tanh'(Y_t)]+t E[psi(X)tanh''(Y_t)]`; the `Z` term cancels
the second summand. The derivatives are bounded and the Gaussian first
moments are finite on each compact correlation interval. This checks all
limit exchanges needed for (9). Bounded convergence supplies endpoint
continuity, and strict increase inside the interval gives strict endpoint
inequalities by inserting an intermediate interior point.

### Finite Gram and stationary cases

The upper law has positive density on a full open square containing zero.
An almost-sure vanishing finite feature combination therefore vanishes
throughout this square by continuity. The excluded hyperplanes for the
test direction `e` are proper because `V(u_i)` is nonzero and no two such
vectors are equal up to sign. They can be avoided simultaneously.

After restriction to the resulting line, analyticity extends the identity
to all real arguments. If the distinct positive slopes are ordered, the
slowest exponential tail isolates its own coefficient after subtracting
the limit at positive infinity. Repetition proves independence. Neither a
dimension count nor noncollinearity is required. The rank statement follows
by collecting coefficients in each class `{u,-u}` before applying this
argument.

At zero readout, the backward contraction vanishes. Thus only the readout
velocity is initially nonzero, with sign `+2 sum p_i y_i T_i`. Differentiating
the predictions yields `2Kt`; differentiating the unhalved loss yields
`-4t^T Kt`, in agreement with the physical gradient metric. Grouping the
readout force by unoriented direction proves both directions of the
stationary classification, including zero weights and signed cancellations.

The supplementary canonical existence argument applies: initialized feature
envelopes are bounded, the Gaussian base is fixed and square-integrable,
the characteristic increment and readout are initially bounded, the middle
matrix is finite, the inputs have unit norm, and finitely many finite labels
have finite second moment. The vector field is locally Lipschitz in the
declared supremum/Frobenius norms. A zero vector field at this state therefore
gives the unique constant characteristic trajectory. No uniqueness claim
for arbitrary uncontrolled distributional solutions is needed.

For the equilateral triple, `|t|²=13/32`; hence the uniform initial estimate
is exactly `L'(0)<=-(13/8) kappa_eq`. Compactness is used only over rotations
of this fixed triple and unit coefficient vectors. It gives no uniform
spectral gap over all possible finite input sets or over training time.

### Symmetry obstruction

The strict decrease of `j` for positive arguments makes `ell'` positive
and strictly decreasing there. Consequently `psi'` is positive, even,
and strictly decreasing in `|x|`. Two Gaussian integrations by parts give

\[
E\psi'''(G)=E[(G^2-1)\psi'(G)]<0.
\]

The strict sign follows from the independent-copy covariance formula:
the differences in `G²` and in `psi'(G)` have opposite signs almost surely
when the squared magnitudes differ. The same reasoning applies to `tanh`.
All required finite-order derivatives are bounded, so the iterated
correlation identity at zero gives `F'''(0)>0`. Full orthogonal covariance
on the circle would instead force `F(t)=F(1)t` on `[-1,1]`, a contradiction.

For the separate lower-span argument, conditional independence of the two
reverse noises makes the conditional variance of any proposed `k` part a
sum of strictly positive conditional variances times squared coefficients.
Its coefficients must vanish. Positive Gaussian density then upgrades the
remaining identity to a pointwise identity, whose mixed second derivative
contradicts `u_1u_2!=0`. This is a valid obstruction to invariance of the
fixed lower feature span. It is correctly not presented as a proof that the
upper Gram itself has no accidental rotational identity.

## Gaps and limits

No fatal, major, conditional, or minor mathematical defect was found in the
audited claims under their stated assumptions. The cited characteristic
dependency is supplied and its hypotheses hold. The report appropriately
leaves later-time injectivity, an all-time Gram gap, convergence to zero
loss, attainment of a scalar invariant manifold, arbitrary signed continuum
data, and identification with the full neural population flow unproved.
The present PASS supplies no bridge to any of those stronger statements.
