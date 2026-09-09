# Isolated adversarial mathematical audit — round 2

## Scope, isolation, and source integrity

Audit date: 2026-09-06.

The sole mathematical input was
`/tmp/l2-two-sample-proof-0ywjpp/SINGLE_FIRST_NEURON_CAVITY_TEST.md`.
I read the entire file: 1,024 lines, 45,883 bytes. I did not read its named
provenance dependencies, any previous review, ledger, history, other agent's
work, project mathematical file, or skill file. No external sources, heavy
theorem imports, experiments, numerical tests, or subagents were used. This
report was written with `apply_patch`; the source was not edited.

Expected SHA256:
`ad91fa72d361ebbb8f9e1be3d8a5e5ba9d0b6c3f186f9689e6380360555caebb`

Before-reading SHA256:
`ad91fa72d361ebbb8f9e1be3d8a5e5ba9d0b6c3f186f9689e6380360555caebb`

After-audit SHA256:
`ad91fa72d361ebbb8f9e1be3d8a5e5ba9d0b6c3f186f9689e6380360555caebb`

Both observed hashes match the expected hash. The after-audit hash was taken
after the complete source reading and mathematical verification.

The audit covers the stated finite-network gradient-flow (GF) identities,
simultaneous raw-gradient-descent (GD) identities at step size `eta = n^-2`,
raw interpolation, normalizations, deterministic bounds, Gaussian cavity
bound, finite-matrix lemma, fixed-index weak probability bounds, and the
scope and hypotheses of those assertions. It does not demand a global
mean-field/population theorem, identification of a population operator, a
Gaussian tail for the actual query, or a conditional/directional estimate
that the note expressly leaves open.

## Verdict and classification of findings

**No required mathematical correction was found to the stated finite-system
results.** The exact restoration identities, uniform component bounds,
normalized logarithmic singular-value estimate, and weak fixed-index path
tail survive independent verification. In particular, the new weak query
tail is obtained directly from averaged temporal regularity and permutation
symmetry; it does not depend on closing the cavity response estimate.

Several proofs in the source are compressed. The derivations below fill in
the principal places where a normalization, absorption argument, or
conditioning issue could otherwise hide an error. These checks did not
reveal a missing hypothesis within the prescribed setup.

There are two optional expository clarifications:

1. Section 11 should specify whether “tightness of the fixed-index paths”
   means tightness of their supremum norms or tightness of their laws in
   `C([0,T]; R^2)`. The displayed tail proves the former immediately. The
   latter also follows from the derivative estimates already proved, by
   the short modulus-of-continuity argument supplied below. Thus this is
   not an obstruction to either conclusion, but the implications should
   be distinguished.
2. Sections 9 and 13 could say more explicitly what a merely tight exposure
   integral would add. Scalar self-response tightness is already implied
   by (47c). Tightness of the exposure integral would additionally control
   the full rescaled bulk response `Y`; stronger deterministic, conditional,
   or quantitative tail conclusions require a correspondingly stronger
   exposure estimate. Equations (41) and (46) themselves are correct.

Neither optional clarification changes the established finite identities
or estimates. The directional exposure and stronger tail questions remain
open here, exactly as the note says.

## 1. Setup, raw gradient, and deterministic bounds: (1)–(8)

### Hypotheses and rates

The input conditions imply that the two inputs are linearly independent:
the matrix `C` is positive definite with eigenvalues `1 +/- rho`. In
particular, the prescribed geometry implicitly requires `d >= 2`. All uses
of `C^-1` and `C^-1/2` are legitimate for fixed `|rho| < 1`; no uniformity as
`rho` approaches either endpoint is asserted.

For a compactly supported smooth first derivative, its integral from zero
is bounded on the real line. Its first and second derivatives are bounded
as well. The same properties hold for arctan. The nonzero condition on the
compact first gate is needed for the positive active fraction in Section
12, not for the preceding finite estimates. Positivity or monotonicity of
that gate is not needed. Fixed, width-independent activations are essential
to the uniform constants.

For one sample the ordinary parameter gradients of the prediction are

\[
 \partial_{W^{(1)}}f_a=\frac1n\delta^{(1)}_a x_a^T,
 \qquad
 \partial_A f_a=\frac1n\delta^{(2)}_a(h^{(1)}_a)^T,
 \qquad
 \partial_w f_a=\frac1n h^{(2)}_a.
\]

The inverses of the three raw metric weights are `n/d`, `1`, and `n`.
Multiplying these gradients by `2 r_a` and negating gives exactly (3), with
`c_a = -2 r_a`. There is no missing sample average, factor of two, or neuron
normalization. Since the velocity is minus the raw gradient of the physical
loss, differentiation gives precisely (7), with no further factor.

The initialization variances in (2) are used consistently: an initial
column of `A` has covariance `I_n/n`, and an initial readout coordinate has
standard deviation `1/n`, not `1/sqrt(n)`.

### Uniform GF bounds and existence

On `E_n`, `|f_a(0)| <= B_2`, so
`||r(0)|| <= sqrt(2)(B_2+1) = R_0`. Loss dissipation bounds the residuals for
all subsequent GF times. Consequently, `sum_a |c_a|` is bounded. The update
of each readout coordinate has absolute value at most
`B_2 sum_a |c_a|`, giving the stated bound on `||w||_infinity`.

Each rank-one term in `dot A` has operator norm bounded by

\[
 \frac{|c_a|}{n}\|\delta^{(2)}_a\|\|h^{(1)}_a\|
 \le |c_a|P_2M_TB_1.
\]

Integration bounds `||A||_op`. The bounds on `delta^(2)/sqrt(n)` and
`q^(1)/sqrt(n)` in (6) then follow directly.

For completeness, the first-layer field equation is

\[
 \dot z^{(1)}_a
   =\sum_b C_{ab}c_b\bigl(\phi_1'(z^{(1)}_b)\odot q^{(1)}_b\bigr).
\]

It bounds `||dot z^(1)_a||/sqrt(n)`, hence
`||dot h^(1)_a||/sqrt(n)`. The displayed product rules in Section 2 now
bound `dot z^(2)`, `dot delta^(2)`, and `dot q^(1)` in RMS norm. This argument
does not require a maximum bound on individual reverse fields.

For a raw unit tangent `V`, the estimates

\[
 \|V^{(1)}x_a\|\le\sqrt n,
 \qquad \|V^{(2)}\|_F\le1,
 \qquad \|V^{(3)}\|\le\sqrt n
\]

give `|D_V f_a| <= C_T`. This bounds the raw norm of each prediction
gradient, and hence the raw loss gradient since the residuals are bounded.
Pairing with that gradient also bounds `dot c_a`. This justifies the last
line of (6) without circularly assuming a bound on the loss gradient.

At any fixed finite width and dimension, (7) implies that finite-time raw
parameter displacement is at most `sqrt(T L(0))`. The raw metric is positive
definite in that finite-dimensional space. Smooth local dynamics therefore
cannot escape every bounded parameter set in finite time. Local existence
and uniqueness extend globally. This reasoning also works for arbitrary
finite initial data, which is relevant when the note later discusses
qualitative tightness at finitely many exceptional widths.

### GD descent and recomputed segments

The stopping argument is valid. Before a first candidate exit of the
residual bound, the preceding updates control `w` and `A`; the single
candidate update controls those same parameters throughout its connecting
raw segment. Bounded activations then give bounded segment residuals and
prediction differentials.

For two raw unit tangents, the readout/hidden, top-curvature, and
second-layer/first-layer mixed Hessian terms are `O_T(1)`. The exceptional
first-layer curvature term satisfies

\[
 \left|\frac1n\sum_i q^{(1)}_{a,i}\phi_1''(z^{(1)}_{a,i})
          (U^{(1)}x_a)_i(V^{(1)}x_a)_i\right|
 \le L_1\|q^{(1)}_a\|_\infty
 \le C_T\sqrt n.
\]

Thus the loss Hessian on the raw segment has norm at most
`C_T(1+sqrt(n))`. Taylor's formula gives the stated descent inequality.
Because `eta C_T(1+sqrt(n))` tends to zero at `eta = n^-2`, every sufficiently
large width has a nonincreasing loss at nodes, contradicting the proposed
first exit. This is a direct GD proof, not an assumed GF approximation.

The bound is correctly qualified by sufficiently large `n`. Extending the
fixed horizon through `ceil(T/eta) eta` only requires constants for `T+1`.
Node product differences are `O_T(eta)` in the stated normalized norms.

### Row action and the compressed GD absorption argument

Write `p_{a,i} = c_a q^(1)_{a,i}` and
`d_{i,a} = p_{a,i} phi_1'(z^(1)_{a,i})`. Direct substitution yields

\[
 d\|\dot W^{(1)}_i\|^2=d_i^TCd_i
   =\sum_a p_{a,i}\dot h^{(1)}_{a,i},
 \qquad \dot z^{(1)}_i=Cd_i.
\]

The quantity `U_i` dominates `sum_a |p_{a,i}(t)|` at every time.
The initial RMS bounds and the product-rule derivative bounds imply
`n^-1 sum_i U_i^2 <= C_T` by the triangle inequality in Euclidean norm and
integration. Integration by parts against bounded features gives

\[
 \int_0^T d\|\dot W^{(1)}_i\|^2dt\le2B_1U_i.
\]

Since `C^2 <= 2C` as symmetric matrices,

\[
 \int_0^T|\dot z^{(1)}_i|^2dt\le4B_1U_i,
 \qquad \sup_t|\dot z^{(1)}_i|\le2P_1U_i.
\]

Multiplying these last two bounds proves the averaged cubic action bound.
The initial-value plus integrated-speed estimate, followed by
`(a+b)^4 <= 8(a^4+b^4)`, proves the fourth-moment path estimate in (8).

For GD, take `U_i` to be the analogous initial absolute value plus discrete
total variation through the relevant nodes. Its averaged square remains
bounded, so `max_i U_i <= C_T sqrt(n)`. At a step, let
`w_{i,k} = d_{i,k}^T C d_{i,k}`. The exact field increment is
`Delta z_i = eta C d_{i,k}`. Taylor expansion of each first feature gives

\[
 \sum_a p_{a,i,k}\Delta h^{(1)}_{a,i,k}
   =\eta w_{i,k}+\mathcal R_{i,k},
 \qquad
 |\mathcal R_{i,k}|
   \le\frac{L_1U_i}{2}|\Delta z_i|^2
   \le L_1U_i\eta^2w_{i,k}.
\]

Summation by parts bounds the sum of the left-hand side by `2B_1U_i`.
Thus, with `A_i = sum_k eta w_{i,k}`,

\[
 A_i\le2B_1U_i+\eta L_1U_i A_i.
\]

The coefficient to absorb is at most `C_T n^-3/2`. For large `n`,
`A_i <= 4B_1U_i`, and the same cubic and fourth-moment estimates follow
with enlarged constants. Since `z^(1)` is linear on raw segments, these
are estimates for the requested interpolation. The source's brief GD
action justification is therefore mathematically sufficient, although
this explicit absorption calculation would make it easier to check.

## 2. Deletion and exact restoration: (9)–(15)

The deletion is properly defined by permanently fixing column `j` at zero
and freezing the selected first row. All remaining updates have denominator
`n`, not `n-1`. Its initial matrix satisfies
`||A(0)P||_op <= ||A(0)||_op`, and deleting one feature cannot increase its
Euclidean norm. The preceding bounds therefore apply to the cavity on the
same actual-network event, and also on its own stated initialization event.

For deterministic `j`, Gaussian entry independence gives
`g ~ N(0,I_n/n)` independently of all the other initial data, including
`xi ~ N(0,C)`. The cavity depends only on those other data. Its complete
trajectory is consequently measurable with respect to the stated
deleted-column information and independent of `g`. The unused selected
first feature does not re-enter the cavity dynamics.

Projecting the actual matrix update onto column `j` gives exactly (10).
The bounds in (12) follow from
`||delta^(2)|| <= P_2 M_T sqrt(n)` and the bound on the selected feature.
In particular, learned-column displacement has norm `O_T(n^-1/2)`, while
the initial column has norm of order one. The omitted input has ordinary
norm `O_T(1)` on `E_n`, and RMS norm `O_T(n^-1/2)`; these are not being
confused.

Every product expansion in (13) is exact. In particular:

- The second-layer input uses `Delta B` against the actual feature, plus
  the cavity matrix against the feature difference, plus `e_a`.
- The backward field uses `Delta w` against the actual top gate, plus
  the cavity readout against the gate difference.
- The prediction difference includes both readout and feature changes,
  and `Delta c_a = -2 Delta f_a` has the correct sign.
- For `i != j`, the column term drops from the reverse field; hence the
  displayed `Delta B^T delta + Bhat^T Delta delta` is exact.
- Each three-factor update difference retains the residual difference,
  backward-field difference, and feature difference. In the first-row
  equation, the nonlinear gate difference multiplies the actual query,
  which is the factor later producing the maximum in (30).

Equation (14) is the actual selected-row equation because its reverse
field is `(g+ell)^T delta^(2)`. Together with the learned-column equation,
the bulk difference equations and the cavity, this is a closed finite
restoration system. It does not condition on or prescribe a future actual
trajectory.

At time zero only the bulk parameters agree. Substituting the omitted
input `g phi_1(xi_a)` into the top activation and top gate gives exactly
the initial backward-field and residual differences in (15). There is no
incorrect assumption of equal initial residuals.

## 3. Gaussian cavity and bounded direct responses: (16)–(23)

Conditional on the deleted-column information, every finite collection of
the cavity queries is a deterministic linear image of `g`. Equation (16)
therefore has exactly the factor `1/n`. The conditioning may retain `xi`,
since it is independent of `g` and unused by the cavity.

The learned-column readback (17) follows by inserting (10) into
`ell(t)^T delta^(2)_a(t)`. The product of the two backward-field norms
contributes `n(P_2M_T)^2`, canceling the denominator `n`. Thus the proved
bound is `O_T(1)` and contains no vanishing factor. All past residuals and
selected features remain inside the history integral.

For the direct response, the fundamental theorem of calculus applied to
the top gate with the bulk and readout fixed gives
`delta^(2)_a = delta^(2),0_a + D_a e_a`. The operator bound on `D_a` is
`M_T L_2`. Expanding

\[
 (g+\ell)^T\delta^{(2)}_a
 =g^T\widehat\delta^{(2)}_a+\ell^T\delta^{(2)}_a
   +g^TD_a b\,h^{(1)}_{a,j}
   +g^T(\delta^{(2),0}_a-\widehat\delta^{(2)}_a)
\]

verifies (18) without double counting: the entire learned-column term,
including its direct-gate part, is already in `M`. Cauchy--Schwarz gives
(19). At initialization the bulk discrepancy and learned column vanish,
giving the sharper bound (20) with the actual initial readout maximum.
The actual initial query is not asserted to be an independent Gaussian
projection.

On the measurable cavity event, (6) gives exactly the normalized amplitude
and Lipschitz bounds (21). Conditional Gaussian increments then have
standard deviation at most `D_1 |t-s|`. The dyadic proof of (22) checks out
including its constants. More explicitly, using threshold `u` for the
initial value and the endpoint increment, and the displayed thresholds
for all finer increments, the union bound over both samples is at most

\[
 \left(8+4\sum_{m\ge1}2^m e^{-2(m+1)}\right)e^{-u^2/2}
 <12e^{-u^2/2}.
\]

The increment thresholds sum to at most
`D_1T(u+6)` on a fine dyadic chain; allowing the endpoint increment gives
the safe bound `D_0 u + D_1T(2u+6)`, which is bounded by
`6(D_0+D_1T)(1+u)`. Continuity extends the result from the grids to the
whole interval. No independence between distinct increments is needed.

The distinction between `E_n` and its deleted-column counterpart is
correct and necessary. Conditioning on `E_n` would in general change the
law of `g`; instead, the note applies the conditional result on the
measurable cavity event and uses `E_n` only as a restriction afterward.

The numerical constants in (23) also check. A maximal `1/4`-separated
unit-sphere set is a `1/4`-net with at most `9^n` points: the disjoint
radius-`1/8` balls fit in the radius-`9/8` ball. Approximating each of two
unit vectors loses at most half the matrix norm. Thus `||A(0)||_op > 8`
implies a net bilinear form with absolute value greater than 4. Each such
form has variance `1/n`; two Gaussian tails and the `9^(2n)` pairs give
`2 exp(-(8-2 log 9)n)`. Each readout coordinate has variance `n^-2`, giving
`2n exp(-n^2/2)` after a union bound. For `A(0)P`, the bilinear variance
is at most `1/n`, which is enough for the same argument.

## 4. Raw bulk coordinates and forced response: (24)–(31)

For a row displacement in the input span, write
`Delta W_i^(1) = alpha_1 x_1^T + alpha_2 x_2^T`. Its field displacement is
`Delta z_i = d C alpha`, and

\[
 d\|\Delta W^{(1)}_i\|^2
   =d^2\alpha^TC\alpha
   =(\Delta z_i)^TC^{-1}\Delta z_i.
\]

The input-orthogonal row component is unchanged by both dynamics, and is
the same initially. This proves that (24) is an isometry for the moving
bulk raw metric. The dimension is
`2(n-1) + n(n-1) + n = n^2+2n-2`, as stated.

Holding `E` fixed while differentiating (25) is correct: the column `b`
and the selected first-row feature are outside these bulk coordinates.
Their contribution is an external input for the bulk partial derivative,
even though it is dynamically generated in the full system. Consequently,
both the actual and cavity bulk equations are the stated Euclidean
negative gradients in `X`.

The splitting

\[
 F(X,E)-F(\widehat X,0)
  =[F(X,0)-F(\widehat X,0)]+[F(X,E)-F(X,0)]
\]

gives the precise secants in (26). Multiplication by `sqrt(n)` yields
`dot Y = JY + Bcal e`, which is the source `v` in (27). Independently,

\[
 \delta^{(2),0}_a-\widehat\delta^{(2)}_a
  =\left(\int_0^1D_X\delta^{(2)}_a\,d\theta\right)\Delta X
  =L_aY.
\]

Thus `R = g^T L_a Y` is exact; its normalization has not lost or gained
a factor.

All secant points have bounded matrix operator norm and readout maximum
by convexity. Their residuals are bounded by bounded activations and
readout, without assuming that the secants themselves are trained paths.
The tangent bounds after (28) follow from the raw coordinate isometry.
Differentiating the top backward field gives a bound on `L_a`. The two
displayed mixed `X,E` derivatives of the prediction each have size
`O_T(||V|| ||H||)` because `D_V w` and `D_V z^(2)` have size `O(sqrt(n))`.
The first derivatives are bounded too. The residual term in the mixed
loss Hessian is therefore bounded, as is its gradient-product term.
This proves the bound on `Bcal`, including the residual derivative.
Applying it to the omitted input proves the source bound in (28).

Variation of constants with `Y(0)=0` gives (29). Its coefficient order
and the placement of `L_a(t)`, `Bcal_b(s)`, and `b(s)` are correct. They
may all depend on the same Gaussian column; no conditional isotropy is
being used.

For the direct difference estimate, residual and reverse-field
differences have exactly the RMS bounds stated after (30). The only
unbounded multiplier needed in this proof is the actual reverse-field
maximum multiplying the first-gate difference. This gives (30), including
the `1/sqrt(n)` scale of its forcing. At zeros of the norm the upper
derivative formulation is appropriate. Integrating the scalar inequality
and then using `R = sqrt(n) g^T L_a Delta X` gives (31).

The normalization loss described there is real. An `O(n^-1/2)` bound on
the bulk raw distance only yields an order-one scalar bound before the
growth factor. The available `Q_infinity <= C_T sqrt(n)` produces a
growing exponential; the hypothetical square-root-logarithmic maximum
would still produce a growing scalar bound while allowing the raw bulk
distance to vanish. Neither statement is promoted to a lower bound or
an impossibility claim.

## 5. Hessian split and finite-matrix lemma: (32)–(35)

### Sign, factors, and Frobenius normalization

At a secant point with `E=0`,

\[
 D_XF=-2\sum_a Df_a\otimes Df_a
       -2\sum_a r_aD^2f_a
      =-2\sum_a Df_a\otimes Df_a+\sum_a c_aD^2f_a.
\]

This verifies the positive `c_a` coefficient, with its existing sign
through `c_a=-2r_a`, in (33). All Hessian terms except the first-layer
activation curvature have bounded bilinear form norm. For example, the
second-layer/first-layer cross term is bounded by
`n^-1 ||delta^(2),0|| ||V^(2)||_F P_1 ||D_U z^(1)|| = O_T(1)`.
Top curvature uses the readout maximum and two `O(sqrt(n))` tangent
fields, again canceled by `1/n`.

The remaining bilinear term is

\[
 \frac1n\sum_{i,a}c_aq^{(1),0}_{a,i}\phi_1''(z^{(1)}_{a,i})
                  D_Uz^{(1)}_{a,i}D_Vz^{(1)}_{a,i}.
\]

Inserting `D_U z_i = sqrt(n) C^(1/2) U_i` gives the two-by-two block in
(33), with no surviving neuron factor. The remainder `J_0` is symmetric
and bounded, and `H` is symmetric and supported only on the first-neuron
blocks. Symmetry is inherited from the actual loss Hessian, not assumed
for a frozen-residual approximation.

For each secant point,
`||q^(1),0_a|| <= A_T P_2 M_T sqrt(n)`. Using
`||C^(1/2) D C^(1/2)||_F <= ||C||_op ||D||_F`, followed by
Cauchy--Schwarz in the secant parameter, gives
`sum_i ||H_i||_F^2 <= C_T n`. This verifies (34). It is the squared
Frobenius norm of the unbounded part, normalized by `n`; it is not a
uniform bound on its operator norm.

### Independent check of the matrix argument

Let `V' = (K+H)V`, with `K,H` symmetric, `K <= cI`, and the regularity
stated in the note. Solving the inverse equation gives an invertible `V`.
Set `S=VV^T`. Then

\[
 S'=(K+H)S+S(K+H).
\]

At a simple positive eigenvalue `lambda_nu` with unit eigenvector
`v_nu`, its derivative is `2 lambda_nu v_nu^T(K+H)v_nu`. Therefore the
logarithm of the corresponding singular value has derivative
`v_nu^T(K+H)v_nu`.

The treatment of repeated eigenvalues is adequate. The elementary min-max
formula bounds eigenvalue changes by the norm of the matrix change, so
ordered eigenvalues are locally Lipschitz. In a repeated eigenspace, the
complementary block is separated from the repeated eigenvalue. Its
eigenvector component for eigenvalues in that cluster is `O(h)` under a
time increment `h`. The first-order slopes within the cluster are thus
the eigenvalues of the compression of `S'` to that eigenspace. This
compression is `2 lambda` times the compression of `K+H`. Diagonalizing
it supplies an orthonormal basis giving the displayed log-derivative
formula almost everywhere. Positivity on a compact time interval also
makes the logarithms locally Lipschitz and absolutely continuous.

With `l_nu = log s_nu(V) - c(t-s)` and
`F = sum_nu (l_nu)_+^2`, it follows almost everywhere that

\[
 \frac12F'
 \le\sum_\nu(l_\nu)_+v_\nu^THv_\nu
 \le\sqrt F\left(\sum_\nu|v_\nu^THv_\nu|^2\right)^{1/2}
 \le\sqrt F\,\|H\|_F.
\]

The last step is a diagonal-square bound in an orthonormal basis, not an
assumption of simultaneous diagonalization at different times.
Differentiating `sqrt(F+epsilon)` gives an upper derivative bounded by
`||H||_F`; integrating from `F(s)=0` and then letting `epsilon` decrease
to zero proves

\[
 \sqrt{F(t)}\le\int_s^t\|H(u)\|_Fdu.
\]

Taking `K=J_0` and using (34) proves (35). Its normalization is correctly
`n`, even though `V` acts in dimension `m=n^2+2n-2`. A singular value
greater than `exp(C_T(t-s)+u)` contributes more than `u^2`, which proves
the stated counting bound. The argument works with noncommuting
time-dependent generators and with the finitely piecewise-continuous
coefficients later used for GD. At `t=s` both sides are zero.

The estimate constrains logarithmic singular-value magnitudes. It does
not constrain the alignment of the selected forcing and readback with
the singular vectors, which can depend on `g`. The source correctly
retains this distinction.

## 6. Directional remainder and exposure: (36)–(41)

The propagator of `J_0` has norm at most `exp(C_T(t-s))`. Variation of
constants relative to this propagator gives (36)–(37), and
`||Y_0|| <= C_T(||g||+n^-1/2)`. On `E_n`, `||g|| <= ||A(0)||_op <= 8`.
Therefore `M`, `S`, and `g^T L_a Y_0` are all bounded by deterministic
width-independent constants on that event.

The first-block extraction in (38) is exact because `H` vanishes on all
other coordinates. Applying the bilinear Frobenius bound to each block
and then Cauchy--Schwarz over the blocks gives

\[
 \left|\sum_i a_i^TH_iY_i\right|
 \le\left(\sum_i\|H_i\|_F^2\right)^{1/2}
      \left(\sum_i|a_i|^2|Y_i|^2\right)^{1/2}.
\]

This proves (39), including its `sqrt(n)` factor. An appropriately
integrated overlap of order `n^-1/2` would suffice here; the note does
not claim it has proved such an overlap.

The quantities in (40) are well-defined measurable functions of the
actual/cavity pair, including at `Y=0`, because their denominator is
`1+||Y||^2`. Summing `|Y_i^T H_i Y_i|` and using (34) proves
`kappa_j <= C_T Pi_j`. For `S_Y=1+||Y||^2`,

\[
 S_Y'=2Y^TJ_0Y+2Y^THY+2Y^Tv
       \le(C_T+2\kappa_j)S_Y
\]

on `E_n`: the bounded source is absorbed using
`2|Y^Tv| <= ||Y||^2+||v||^2`. Since `S_Y(0)=1`, integration yields
exactly (41).

This is a valid sufficient route to controlling `Y` and hence its scalar
readback. It does not establish an exposure estimate. In particular,
boundedness in probability of the exposure integral gives boundedness
in probability of `Y` by exponentiation, but does not by itself give a
Gaussian response tail or a conditional response bound. This is the
reason for optional clarification 2 above.

## 7. Exact GD restoration and matrix products: (42)–(46)

All algebraic field identities remain true at nodes because fields are
recomputed from the updated raw parameters. Each parameter update uses
the old node. Thus the learned column in (42) sums precisely `l<k`, and
its readback pairs the old backward field with the queried current one.
There is no extra current-node history term.

The same secant identity gives the exact recurrence (43). Iterating it
from zero initial discrepancy gives

\[
 Y_k=\eta\sum_{l<k}\mathcal U_{k,l+1}v_l.
\]

Inserting the source and the scalar readback proves (44). The product
index `l+1` is necessary and correct. The core product bound follows
from `||I+eta J_0|| <= 1+eta C_T <= exp(eta C_T)`. Rewriting the
recurrence relative to those core products gives (45), including its
exact split of `R` and its coefficient order.

Expanding the squared norm of the recurrence gives

\[
 1+\|Y_{k+1}\|^2
 =1+\|Y_k\|^2+2\eta Y_k^T(J_kY_k+v_k)
                       +\eta^2\|J_kY_k+v_k\|^2.
\]

Here `||J_k|| <= C_T(1+sqrt(n))`, since `||H_k||_op <= ||H_k||_F`.
The final square is at most `C_T n(1+||Y_k||^2)`. The linear term is
bounded using the same signed exposure as in GF. Multiplying the stated
one-step inequalities yields (46), since over `k eta <= T+eta` the
additional accumulated exponent is at most
`C_T k eta^2 n = O_T(1/n)`. No step-independent error has been silently
multiplied over `O(n^2)` updates.

For the discrete matrix estimate, symmetry of `J_k` and
`eta ||J_k|| <= 1/2` ensure that `I+eta J_k` is positive definite for
sufficiently large widths. Its real symmetric logarithm is therefore
defined. The scalar integral formula yields
`|log(1+x)-x| <= x^2` for `|x| <= 1/2`, including negative `x`. Hence

\[
 \|G_k-J_k\|_{op}
 \le\eta\|J_k\|_{op}^2\le C_T/n.
\]

The piecewise-constant generator `G_k` produces exactly the ordered GD
products at grid points, since `exp(eta G_k)=I+eta J_k` for each step.
Writing its bounded symmetric part as `J_{0,k}+G_k-J_k` retains the same
`H_k`. The matrix lemma from Section 8 applies with an enlarged constant.
This proves the node version of (35) without commuting different factors.

Finally, both bulk coordinate differences and learned columns are linear
on a raw segment. Their norm bounds extend from endpoints by convexity.
Recomputed nonlinear fields obey (18) at every segment point, and the
secant bound on `L_a` remains valid. The cavity backward field has RMS
derivative bounded by `C_T` on each segment: the old-node raw direction
is bounded, its readout direction is bounded coordinatewise, and its
field derivatives follow by the ordinary product rule. Its continuity
and piecewise derivative bound give (21) globally. Thus the conditional
Gaussian bound applies to the recomputed cavity process as well as to
the initially introduced node-linear process. The source does not
mistake raw interpolation for a GF trajectory.

## 8. Actual fixed-index path and remainder tails: (47)–(47c)

The tail reduction (47) follows by the exact decomposition on `E_n` and
the deterministic bound on its three non-Gaussian, non-remainder terms.
The Gaussian probability is bounded on the larger measurable cavity
event, using `E_n` contained in that event; the remainder event stays
explicit. A constant can absorb the bounded terms into `C_T(1+u)`.
This does not condition the Gaussian variable on `E_n`.

For the independent actual-network argument, absolute continuity gives,
for each coordinate and each sample,

\[
 \sup_{t\le T}|q^{(1)}_{a,i}(t)|^2
 \le2|q^{(1)}_{a,i}(0)|^2
    +2T\int_0^T|\dot q^{(1)}_{a,i}(t)|^2dt.
\]

Taking the sample maximum and bounding it by the sample sum proves the
first inequality in (47a). The RMS derivative bounds prove the second.
For raw GD the product rule for the recomputed `q^(1)` holds inside
each cell, its RMS derivative is uniformly bounded there, and the
path is continuous at the nodes. It is therefore absolutely continuous
on the finite interval and obeys the same estimate. This verifies (47a)
for the entire interpolation, not just its node maximum.

The first-neuron permutation maps in the note preserve the independent
initialization and the event `E_n`, including its matrix norm condition.
They leave predictions unchanged and permute the first reverse fields.
GF uniqueness and, respectively, induction for GD establish this
equivariance for whole paths. Thus the variables
`1_{E_n} Q_i^2` have identical expectations. Averaging them and applying
(47a) proves

\[
 \mathbb E[\mathbf1_{E_n}Q_j^2]\le C_T.
\]

Markov's inequality after separating `E_n^c` gives (47b). This is a
restricted second moment and an unconditional probability bound with
an explicit bad-event term. It is not an unrestricted second-moment
estimate on the actual query. It does not apply to a neuron selected
after seeing the initialization, the trajectory, or the query values,
and it does not bound the maximum over all neurons. A deterministic
choice of a valid index for each width is permitted by the same symmetry.

The bound implies asymptotic tightness of `Q_j`, since `Pr(E_n^c)` tends
to zero. The finite remaining widths can be included in qualitative
supremum-norm tightness because their GF paths are globally finite and
their GD paths involve finitely many finite updates. No quantitative
polynomial bound on those exceptional-width bad events is needed or
asserted.

If “path tightness” is intended in the continuous-function topology, a
slightly stronger consequence of the same argument makes it explicit.
Set

\[
 Z_i=\sum_a|q^{(1)}_{a,i}(0)|^2
       +\int_0^T\sum_a|\dot q^{(1)}_{a,i}(t)|^2dt.
\]

The already proved estimates give `n^-1 sum_i Z_i <= C_T` on `E_n`,
and symmetry gives `E[1_{E_n} Z_j] <= C_T`. For the two-sample path,

\[
 |q_j(t)-q_j(s)|^2\le |t-s|Z_j.
\]

Consequently, with the usual modulus of continuity `omega`,

\[
 \Pr\{\omega(q_j,\delta)>\varepsilon\}
 \le\Pr(E_n^c)+C_T\delta/\varepsilon^2.
\]

On bounded `Z_j` sets, both the initial values and the one-half-Hölder
constants are bounded. Their closure is compact in the uniform topology,
as can be seen by taking convergent subsequences on successively finer
finite time grids and using the shared modulus between grid points.
This supplies the additional equicontinuity step for tightness of path
laws, if that is the intended meaning. The optional clarification is
about specifying and justifying the topology, not about a counterexample
to the source's estimates.

Integrating the conditional Gaussian supremum bound gives
`E[1_{Ehat_n}(G_j^*)^2] <= C_T`. Near the origin one uses the trivial
probability bound 1; above the fixed Gaussian threshold the exponential
tail is integrable against `2v dv`. Since `E_n` is contained in `Ehat_n`,
the same upper bound applies with the smaller event as a restriction.

From the final exact split, on `E_n`,
`Gamma_j(T) <= Q_j + G_j^* + C_T`. The squared triangle inequality,
(47b), and the just established cavity second moment prove (47c).
There is no circular estimate of `Gamma` through itself: the bound on
`Q_j` came from the actual-network RMS temporal estimates alone.

For GD this last conclusion concerns the node remainder defined in
(45), as the note expressly states. The query bound (47b) already
concerns the complete raw interpolation. Neither restricted scalar
moment controls `Y`, the exposure integral, the fourth-order
participation, or the block overlap. Large response components can
cancel in scalar readback; the proof makes no contrary inference.

## 9. First-action comparison and compact gates: (48)–(49)

Multiplying the first bulk coordinates in (24) by `sqrt(n)` gives
exactly `Y_i=C^-1/2(z_i^(1)-zhat_i^(1))` in (48). Applying the fourth-
and third-power triangle inequalities to both trajectories, then their
individual action estimates, gives (49) on the stated initial-moment
event intersected with `E_n`. The constants may depend on fixed `rho`
through `||C^-1/2||`, but not on `n` or `d`. No independence between
actual and cavity trajectories is used.

For `xi ~ N(0,C)`, the fourth moment is

\[
 \mathbb E|\xi|^4
 =\mathbb E\xi_1^4+\mathbb E\xi_2^4
                   +2\mathbb E(\xi_1^2\xi_2^2)
 =3+3+2(1+2\rho^2)=8+4\rho^2\le12.
\]

The eighth-moment bound follows, for example, from
`(xi_1^2+xi_2^2)^4 <= 8(xi_1^8+xi_2^8)` and the one-dimensional
Gaussian eighth moment `105`, obtained by repeated integration by
parts in its density. It gives `1680`, as stated. The initial row pairs
are independent. The variance of their empirical fourth moment is
therefore at most `1680/n`; its mean is at most 12. Chebyshev gives the
stated probability bound for exceeding 13. No independence of this
moment event from `E_n` is needed when intersecting the bounds.

If `||Y||=O(1)`, bounded pointwise participation requires
`sum_i |Y_i|^4=O(1/n)`, whereas the supplied trajectory comparison only
gives an `O(n)` bound. This scale comparison is correct. For arbitrary
`Y`,

\[
 \sum_i|Y_i|^4\le\left(\sum_i|Y_i|^2\right)^2\le\|Y\|^4
\]

proves the universal `Pi_j <= sqrt(n)` estimate. Substitution into the
energy estimate produces the stated growing exponential. The note
does not claim that an averaged action bound rules out some different
way of proving the desired directional bound.

For the compact first gate, if both initial gate values of a bulk row
vanish, keeping that row fixed solves its two field equations for any
finite continuous surrounding trajectory. Uniqueness makes it the
actual solution. Equivalently, the gate's Lipschitz bound and the
integral equation force a zero displacement from that initial pair.
This applies in both the actual and cavity systems. Every GD update
of the same row is exactly zero, so induction proves the discrete
statement. Its block `Y_i` is therefore identically zero.

The set where the nonzero compact gate is nonzero is a nonempty open
bounded subset of the real line. Because `|rho|<1`, the initial pair
has strictly positive density throughout the plane. There is positive
probability of at least one active gate, and positive probability of
both coordinates lying outside the gate support. Thus the active-row
probability `p` lies strictly between zero and one. Independent initial
rows give a fraction converging in probability to `p`, with the stated
variance bound; deleting one deterministic row changes the fraction
by at most `1/n`. Arctan has a strictly positive derivative everywhere,
so it has no corresponding exactly frozen set.

## 10. Scope ledger and final assessment

| Claim | Audit result and scope |
|---|---|
| Raw GF and loss identity (1)–(7) | Correct at every finite width, with the stated metric and physical loss. |
| Uniform GD bounds and action (6), (8) | Correct for sufficiently large widths at `eta=n^-2`, including raw interpolation. |
| Cavity and restoration (9)–(15) | Exact; selected column and selected first root are treated separately, with denominator `n` retained. |
| Gaussian covariance and path tail (16), (21)–(23) | Correct conditional on deleted-column information on its measurable event; not conditional on the full actual event. |
| Direct response components (17)–(20) | Exact identities and uniform bounds on `E_n`; no unjustified small learned readback. |
| Bulk response and normalization (24)–(31) | Exact raw-coordinate representation and secants; scalar normalization loss is correctly identified. |
| Hessian and logarithmic singular values (32)–(35) | Correct normalized Frobenius estimate and matrix lemma, without commutativity or isotropy assumptions. |
| Directional formulas (36)–(41) | Exact decompositions and valid sufficient energy inequalities; exposure control is unproved. |
| GD restoration and propagators (42)–(46) | Exact node identities, correct source indices, controlled accumulated correction, and valid matrix-log reduction. |
| Weak actual query and remainder tails (47)–(47c) | Correct for deterministic indices with the specified event restrictions; interpolated query and node remainder scopes are distinguished. |
| Action comparison and compact gates (48)–(49) | Correct on the stated initial-moment event; does not provide the directional participation scale. |

The required-mathematical-fix list is empty. The note establishes its
advertised finite identities, positive component and matrix estimates,
and weak fixed-index path tail under the hypotheses actually stated.
It does not establish a stronger conditional or Gaussian actual-query
tail, a bound on the exposure integral or full `Y`, or a population
continuation/identification theorem. Those limits are explicit, and
none is a missing requirement for the finite claims audited here.
