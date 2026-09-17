# Independent audit of the three-coordinate candidate

2026-09-16. Independent isolated mathematical review. No experiments,
quadrature, simulations, author discussion, study README, earlier verdicts,
other route reports, or other studies were consulted. The only write made by
this review is this report.

**Verdict: PASS at the candidate's stated scope.** The frozen candidate proves
the asserted all-time convergence and mixed-potential bounds for the exact
population order-one closure in three input coordinates, with the specified
permutation-symmetric three-input family, equal weights, signed unit labels,
and prescribed initialization. I found no blocking algebraic, analytic, or
logical gap in that theorem. This verdict does not treat the change from the
original two-coordinate circle problem as approved, does not solve that
problem, and does not establish a trained-network limit or closure accuracy.
It is an internal mathematical review, not promotion approval.

## Frozen inputs and actual coverage

The candidate was read completely, all 711 lines, including its provenance,
statement, all eight sections, and equations (1)--(43). Its SHA256 exactly
matches the assigned frozen hash:

`531b1cb1fe5e5844fcc6da25486e6ee52450860030dd770246e3ee78592521ce`.

Scientific source coverage was:

| Source | Actual reading |
| --- | --- |
| `docs/NOTATION.md` | Complete, 98 lines |
| `docs/observable_p1.md` | Complete, 332 lines |
| `docs/global_nonlinear.md` | Complete C.4.7.9 sections 1--4, including its subsection heading, lines 12084--12377; complete C.4.7.10 B, lines 13161--13430; complete C.1, lines 13431--13786; complete D.3, lines 15146--15528 |
| `arbitrary_pair_local.md` in this study | Complete sections 1--4 and preamble, lines 1--331; no later sections |
| `scalar_margin_extension.md` in this study | Complete, 146 lines |

Whole-file SHA256 identifiers are recorded below. A whole-file hash identifies
the source file; it does not assert reading or re-proving its unassigned parts.

| Source | SHA256 |
| --- | --- |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/observable_p1.md` | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` |
| `docs/global_nonlinear.md` | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |
| `arbitrary_pair_local.md` | `4bdb878378518455ca4e0cf7ea2ded8281d056b7aec98cef36c5ebf337c47b9a` |
| `scalar_margin_extension.md` | `3bbf89335a49f9b9c97e4aab8ace450f62d16fc2febe59eaa068b61fcf1dd5e7` |

For reproducibility, the complete consumed excerpts have these additional
SHA256 values, computed from the indicated inclusive lines with original line
endings retained:

| Excerpt | SHA256 |
| --- | --- |
| C.4.7.9, lines 12084--12377 | `51ca77b939a1608207bbb08aaf66009453624b0d505df4407dd74307da021f3d` |
| C.4.7.10 B, lines 13161--13430 | `b77fb96abfbf592faa64e401d4456f52c087723737df667abe834f6eea217380` |
| C.4.7.10 C.1, lines 13431--13786 | `20c0590f399064f42ee8aa2ec51b72779e4dc889802caab7be6361d1446063ec` |
| C.4.7.10 D.3, lines 15146--15528 | `3815d81705fac51fcd5b5489b6f6f961021cba525acf88e74bdc82fe818ae386` |
| `arbitrary_pair_local.md`, lines 1--331 | `fda05e5fd8bba5bb8a45226a541fa25db557302be9f81880a219bc314d631214` |

The solve-math-rigorously and investigate-conjectures skills, including the
latter's adversarial-audit reference, were read and applied. The candidate's
provenance paragraph also names `all_angles_result.md` and an initialization
audit. Neither was read: they were outside the permitted scientific inputs,
and no missing premise from either is needed because this candidate supplies
the relevant monotonicity, dimension transfer, symmetry, and existence proofs
itself. No missing dependency request is necessary.

## Exact object and source compatibility

The object checked is the continuum characteristic evolution on two separate
mark probability spaces, with a full evolving matrix in
`R^(4 x 7)`. It retains the correlated lower marks `(G_i,k_i)` and the exact
ridge `eta=1/4096`. Its physical inputs are `sqrt(3) u_i`, so first-layer
preactivation is `w dot u_i`, exactly as required by the notation contract.
The physical metric is population L2 on rows/readout and ordinary Frobenius
on the coefficient matrix. The loss is the unhalved probability-weighted
square loss; this fixes every factor of two and the decay rate below.

The general-dimensional initialized algebra in `observable_p1.md` supports
the coefficient specialization used here. The candidate does not import a
three-dimensional trained-network theorem from the two-dimensional global
chapter. Instead it proves existence for its own three-dimensional closure.
The latter is a finite-type population system, not a finite number of scalar
state variables; no such stronger finite-dimensional claim is needed.

## Complete claim-by-claim check

### 1. Initialized coefficients, contraction bounds, and gradient: (6)--(13)

The lower raw Gram has blocks `1`, `v I_3`, `sigma I_3`, and cross-block
`beta I_3`; the upper raw Gram is `diag(1,tau I_3)`. These follow from
independence of coordinate pairs and simultaneous oddness within a pair.
Inverse lower-Cholesky normalization gives exactly (6). Positivity of
`R_k^2` follows from

`sigma + eta - beta^2/(v+eta) >= eta + sigma eta/(v+eta) > 0`.

The raw contraction row is `(alpha v, alpha beta + tau gamma)` in each
coordinate. Right multiplication by the inverse transpose of the lower
Cholesky factor gives

`(alpha beta + tau gamma) - alpha v beta/(v+eta)`
`= alpha beta eta/(v+eta) + tau gamma`,

which checks both nonzero bands in (7), their denominators, and the retained
reverse-response term. Cross-coordinate and constant entries vanish only at
initialization; none is removed from the evolving matrix.

Equation (8) is the identity
`L^-1 G L^-T = I - eta L^-1 L^-T`. It gives both contraction estimates,
`|a(u)| <= 1` and `|d(u)| <= ||c||_2`, used later. Every feature coordinate
is bounded, so the claimed finite envelopes exist.

Direct variation of (9) gives

`delta_M f = d^T(delta M)a`,

and the row variation contracts `delta a` with `M^T d`, giving precisely
`sech^2(w dot u) Q(u)u`. The readout gradient is `H^2(u)`. There is no
missing normalization, particle factor, or replacement adjoint in (11).
This verifies (12) and the energy identity (13) in the full ambient metric.

The differentiability assertion is sufficient in the Hilbert metric, not
only for bounded perturbations. For example bounded `b_1` and bounded
`tanh''` bound the integrated remainder in `a(w+delta w)` by a constant
times `||delta w||_2^2`. The finite coefficient vector then controls the upper
field uniformly because `b_2` is bounded; readout cross terms are bounded by
Cauchy--Schwarz. This justifies the chain rules at the characteristic states.

### 2. Existence and restart: (14)--(16)

The vector field is locally Lipschitz in the declared Banach space of bounded
`w-g`, bounded `c`, and finite `M`. The unbounded frozen Gaussian enters only
bounded gates, so it does not compromise the Lipschitz estimates. The local
integral-map construction has a complete path space, a preserved closed
ball, and contraction constant less than one on a sufficiently short time
interval; hence it supplies the claimed local existence and uniqueness.

Energy yields `average |r_i| <= sqrt(L) <= 1`. Thus
`||c_dot||_infinity <= 2`, `||M_dot||_F <= 4t`, and
`||w_dot||_infinity <= 4 B_1 t(d_0+2t^2)`.
Integration gives exactly (15)--(16), including the coefficients of `t^2`
and `t^4`. The same bounds control speeds at any putative finite maximal
endpoint, giving a Cauchy limit in the local existence space and allowing
continuation. This is a global result for the initialized characteristic
solution, without an assertion about uncontrolled distributional solutions.

The saved laws contain all lower `(b,g,w)` and upper `(b,c)` correlations.
Every future velocity is a function of these current laws, the fixed data,
and `M`; reconstructing characteristics from a reached law needs no lost
history. The bounded-increment and readout bounds remain available at a
reached state, so the same uniqueness argument gives own-state restart.

### 3. Full-state permutation symmetry: (17)--(22)

Input oddness is valid for every ambient state, including a matrix with
nonzero constant blocks, because `a(-u)=-a(u)` and both activation functions
are odd. It makes the negative-label absorption in (17) an equality of
ambient loss functions, not just of their restrictions to a trajectory.

The coordinate permutation acts on each complete lower pair and on the
upper Gaussian coordinates. These maps preserve the two population laws.
The block-scalar Cholesky factors commute with the displayed orthogonal
`Q_1,Q_2`, and `Q_2^T D Q_1=D`. Therefore (20) fixes the initialized full
state and is an isometry in both the Hilbert metric and the bounded-increment
existence class.

The transpose placements in (21) also hold for a three-cycle, not only a
self-inverse transposition. Changing lower variables by `G'=PG` gives
`b_1(G)=Q_1^T b_1(G')`, hence `a_T(u)=Q_1^T a(Pu)`.
Multiplication by `Q_2^T M Q_1` then gives the upper field composed with
`S_2`; changing upper variables gives `f_T(u)=f(Pu)`.

The permutation group preserves the data set and acts transitively on its
three label-absorbed inputs. Invariance of the ambient loss and orthogonality
give equivariance of its full gradient. Uniqueness therefore fixes the entire
trajectory under each permutation, proving equal label-absorbed predictions.
Differentiating the ambient loss yields (22) with the average of the three
full gradients. The proof never assumes equality of individual gradient
blocks and never freezes a matrix entry.

### 4. Scalar initialized map and its strict monotonicity: (23)--(30)

Eliminating the two Cholesky factors yields the raw-Gram expression stated
after (25); solving its two-by-two normal equations gives exactly (23).
Conditional averaging over each reverse noise gives `j`, and the Gaussian
pair `(g_i,g dot u)` has correlation `u_i` in three coordinates. Thus
(24)--(25) follow also when `u_i=+1` or `-1`; only the conditional Gaussian
variance becomes zero. This transfer does not rotate the dictionary.

The monotonicity proof correctly allows `A<0`. Its complete inequality chain
checks as follows:

* `tanh^2 z >= z^2/(1+z^2)` and Cauchy--Schwarz give
  `v>=1/4`, `tau>=1/7`, and `0<alpha<=6/7`.
* The centered Gaussian interval-probability argument proves the upper
  convolution bound. The paired addition formula proves the lower bound.
  The factorial estimate gives `cosh(6/7)<=32/23`, hence exactly
  `q_*=529/1024>1/2` in (26).
* Conditional integration by parts gives covariance `tau b_*(x)` and
  conditional variance at least `tau b_*(x)^2`. Total variance,
  `E m(h)^2>=beta^2/v`, and `gamma=E b_*(h)` prove (27).
* Since `m` is odd and has positive derivative, `beta>0`; the bounds on its
  derivative give both `beta<=alpha v` and `beta<=alpha b_* v`.
  These give (28), including `B<=1/gamma<=1/(q_* b_*)`.
* `R_eta>=1024/1025>q_*` makes the coefficient multiplying the upper bound
  on `B` negative in (29), so the inequality direction is correct. The
  resulting lower bound is `alpha(2-1024/529)=34 alpha/529>0`.

Consequently `j'(g)>=34 alpha sech^2(g)/529`. Differentiating the Gaussian
correlation expression on each compact interior interval and integrating by
parts cancels the two terms containing `tanh''`. This proves (30). Its
integrand is bounded and has pointwise endpoint limits, so dominated
convergence extends the derivative expression to both endpoints. Together
with continuity of (24), integration proves strict increase on the closed
interval. Oddness follows by Gaussian symmetry. There is no unverified sign
test or numerical premise.

### 5. Rank three, including the singular coefficient matrix: (31)--(32)

Strict increase gives `p!=z` when `a!=b`. Positive density of the upper raw
marks on the open cube extends an almost-sure continuous field identity to
an identity throughout that cube. Differentiating at zero gives `V^T t=0`.

If `p+2z!=0`, the three displayed eigenvalues prove independence. If
`p+2z=0`, the kernel consists exactly of multiples of `(1,1,1)`, with
`z!=0`. On the line `Z=(r,0,0)` the remaining identity would be

`t_0[tanh(pr)+2 tanh(zr)] = 0`.

Its third derivative at zero is
`-2 t_0(p^3+2z^3)=12 t_0 z^3`, which forces `t_0=0`.
Thus nonlinear field rank is three even in this singular case; a rank-two
linearized coefficient matrix is not an obstruction. The sign reversal of
the third original input preserves Gram rank. The sum of three independent
fields cannot vanish, so `C_0>0` follows.

Coordinate-zero cases (`b=0` or `a=0`), mixed signs, and linearly dependent
input vectors are included. Coincidence requires the excluded `a=b`.
Antipodality between two `v_i` forces first `b=0` and then `a=0`, contradicting
unit norm; sign reversal of the third input cannot create a new duplicate
or antipodal pair. The stated correlated example has inner products
`5/6,-5/6,-5/6` and nonsingular input matrix, as claimed.

### 6. Auxiliary flow and noncollapse: (33)--(40)

The auxiliary flow is the full physical-metric gradient of the current-state
function `F`; no endpoint or target trajectory is supplied to it. Its local
existence proof uses the same valid Lipschitz estimates. Successively
integrating `||c_s||_infinity<=1`, `||M_s||_F<=s`, and
`||w_s||_infinity<=B_1(d_0+s^2/2)s` gives precisely (34), proving existence
for every finite feature time.

Linearity in the readout gives `q_s=2F`, and the Hilbert chain rule gives
`F_s=K=C+||grad_h F||^2`. At initialization the hidden gradient is zero and
the readout gradient is `U_0`, which proves all three expansions in (36).
They justify the limit `q/F^2 -> 1/C_0` rather than assuming it.

For positive feature time, `F>0` and `q>0`. Cauchy--Schwarz gives
`F^2<=qC<=qK`, so direct differentiation yields (37). Integration away from
zero followed by the verified one-sided limit proves (38); continuity covers
zero. No later-time coercivity of the full three-by-three feature Gram is
needed or claimed.

Differentiating `(1+q)/(C_0+F^2)` gives exactly (39), and the splitting in
(40) is exact with both terms nonnegative. This proves the claimed decrease
without asserting monotonicity of `C` itself or strict hidden improvement.

### 7. Physical clock, potential at zero, and full-state endpoint: (1)--(5), (41)--(43)

Since `F_s>=C_0`, finite-feature-time existence gives a unique crossing
`F(s_*)=1`, with `0<s_*<=1/C_0`. On this compact segment the gradient norm
`K` is continuous and bounded above as well as below. The scalar clock is
locally Lipschitz, and its residual solves (41). The upper bound on `K`
prevents reaching the fitted endpoint in finite physical time; the lower
bound forces `s(t)` to tend to that endpoint. Composition solves every
physical block equation, and the already established physical uniqueness
identifies the composition with the original flow.

This proves `0<=F<1`, the signed prediction identities, and the loss bound
with prefactor one in (4). Equations (38) also give the claimed readout bound
and `C>=C_0`. The constant `C_0` is a fixed initialized Gaussian integral,
not endpoint information.

The proposed potential is nonsingular at every ambient state because
`C_0+F^2>=C_0>0`. Along the reached path,
`C_0(1+q)<=C_0+F^2`, so `0<C_0 Psi<=1` and
`L<=Phi<=2L`. The physical clock factor converts (39) exactly into (42).
Differentiating the entire product gives (43), including the derivative of
the readout-dependent factor, and its last term is nonpositive because
`e,F,qK-F^2,K-C_0` have the required signs. Therefore
`Phi_dot<=-4C_0 Phi`, with `lambda=4C_0` and `h(z)=z`.

The time-zero check can be made directly, without dividing by `F`:

`F(0)=q(0)=0`, `K(0)=C_0`, `F_dot(0)=2C_0`, `q_dot(0)=0`,

`Psi(0)=1/C_0`, `Psi_dot(0)=0`, `L_dot(0)=-4C_0`,

`Phi(0)=2`, `Phi_dot(0)=-8C_0=-4C_0 Phi(0)`.

Thus the claimed differential inequality includes initialization literally;
the earlier ratio limit is used only to prove the noncollapse bound.

Finally `||X_dot||=2e sqrt(K)<=-e_dot/sqrt(C_0)`. Integrating to infinity
proves (5), hence a Cauchy limit in the complete full Hilbert state space,
including every matrix entry. The finite-feature-time endpoint identifies
that limit and, through the bounded speeds in (34), also proves convergence
of `w-g,c` in essential-supremum norm and `M` in Frobenius norm.

Coupling identical frozen marks at time `t` and at the endpoint bounds the
two squared Euclidean W2 costs by `E_1|w(t)-w_*|^2` and
`E_2|c(t)-c_*|^2`. Frozen features are bounded, the frozen Gaussian has a
finite second moment, and moving increments are bounded. These are therefore
legitimate finite-second-moment couplings of the complete saved laws, with
no unrecorded cross-population law. The endpoint fits all three labels.

## Gaps, edge cases, and limits of the verdict

No fatal, major, conditional, or minor mathematical correction is required
for the theorem as stated. The potentially decisive failure modes were
checked explicitly: negative `A`, singular `p+2z`, three-cycle transpose
placement, the unrestricted middle matrix, the ambient rather than restricted
gradient, time-zero singularities, finite-time endpoint escape, full-state
versus output-only convergence, and saved-law restart.

The surviving limitation is structural and already stated by the candidate:
the exact data/dictionary permutation symmetry forces one signed residual
direction. Rank three at initialization shows the constraints are independent;
it does not make this a theorem for generic three-input configurations or
generic labels. The proof permits hidden-state learning but establishes
neither strict feature improvement nor a comparison against frozen features.
It gives no uniform rate over unspecified input families, no arbitrary
rotation invariance, no three-dimensional network identification, and no
closure-order approximation guarantee. The original two-dimensional target
remains unsettled by this artifact.
