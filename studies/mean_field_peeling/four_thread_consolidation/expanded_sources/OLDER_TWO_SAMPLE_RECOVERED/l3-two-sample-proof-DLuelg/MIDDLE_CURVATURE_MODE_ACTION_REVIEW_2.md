# Independent adversarial review: middle curvature mode action

Candidate: `/tmp/l3-two-sample-proof-DLuelg/MIDDLE_CURVATURE_MODE_ACTION.md`

Candidate SHA-256, computed from the complete file bytes:

```text
9f812d0d7ecc5196f699a338fc4f8d4b0b5db6a703e817bdf6ebfc2dae60634b
```

## Verdict

**PASS as a conditional estimate on the explicitly assumed existing regular path. No required mathematical correction was found.** Equations (3)--(8), the shared-adjoint step, and the top curvature inequalities are valid with the stated constants and normalizations. The claimed estimates require neither a positive lower bound on contrast nor global existence. They give the stated time-integrated second-moment bounds, with the average middle mode weighted by `kappa_2`.

This verdict accepts the candidate's existing-path, feature-equation, raw-energy, and two-population second-moment-symmetry hypotheses. It does not establish those hypotheses for another construction or prove any global theorem. The candidate itself respects that limitation.

The candidate was read in full (181 lines, 7,691 bytes). No other project, history, review, skill, or mathematical source was read. No experiments or agents were used. The audit below is direct algebra and analysis of this candidate alone. The candidate was not edited.

## Required findings

**None.** In particular, I found no missing independence assumption, lower contrast bound, bounded-field assumption, additional sample symmetry, or global-existence premise needed for the displayed estimates on the assumed path.

## Full audit

### 1. Fields, operators, and the regularity actually used

Write `H_j = L2(Omega_j)` for the real Hilbert spaces, only within this review. The operator types are

```text
W^(2): H_1 -> H_2,       (W^(2))*: H_2 -> H_1,
W^(3): H_2 -> H_3,       (W^(3))*: H_3 -> H_2.
```

The readout `W^(4)` is an `H_3` field. Thus `delta^(3)` lies in `H_3`, `q^(2)`, `delta^(2)`, and `M^(2)` lie in `H_2`, and `q^(1)` and `delta^(1)` lie in `H_1`. All adjoint applications have the correct domain and codomain.

For finite real `z`, the shifted softplus satisfies

```text
1 <= phi(z) <= 1 + e log(2) + e |z|,
0 < phi'(z) < e,
0 < phi''(z) <= e/4.
```

Because the populations are probability spaces, the constant function belongs to each `L2`. Consequently finite `L2` preactivations give finite `L2` features. Bounded forward operators give the next preactivations. Bounded gate multiplication and bounded adjoints give the indicated backward fields. For example,

```text
||delta^(3)_a||_2 <= e ||W^(4)||_2,
||q^(2)_a||_2 <= ||W^(3)||_op ||delta^(3)_a||_2,
||phi''(Z^(2)_a) q^(2)_a||_2 <= (e/4) ||q^(2)_a||_2.
```

The scalar output defining `g` is a finite `L2` pairing. Each matrix velocity in (1) is a sum of two well-defined rank-one Hilbert--Schmidt operators. These facts do not require any preactivation, query, readout, or curvature field to be in `L-infinity`.

It is enough that the *increments* of the middle operators are absolutely continuous in Hilbert--Schmidt norm. The initial operators themselves need not be Hilbert--Schmidt. Bounded initial operators plus these increments give the bounded trained operators used in the proof.

The time integrals are understood on the stipulated regular path, with its explicitly assumed chain rule and energy identity. The proof uses the expressly stated absolute continuity of the operator increments to integrate their derivatives. It does not prove a general Frechet-differentiability statement for the nonlinear map on the entire `L2` parameter space, nor does it need one to establish these conditional estimates. In particular, an `L2` curvature field is not being treated as a bounded multiplier on all of `L2`.

### 2. Scalar identity: both modes have exactly the same coefficients

Let `p_a = phi'(z_a)`. Direct differentiation gives

```text
p_a = e exp(z_a)/(1 + exp(z_a)),
phi''(z_a) = p_a - p_a^2/e.
```

For `A = 1 - (p_1+p_2)/e` and `B = p_1 p_2/e`, separately for `a=1` and `a=2`,

```text
A p_1 + B = p_1 - p_1^2/e,
A p_2 + B = p_2 - p_2^2/e.
```

Multiplying by the respective `q_a` proves `m_a = A delta_a + B q_a` before taking any modal combination. Therefore

```text
m_+ = A delta_+ + B q_+,
m_- = A delta_- + B q_-.
```

These are the same pointwise coefficients in both equations, even when `p_1 != p_2` and the queries have arbitrary signs. There is no hidden replacement of one mode by the other. Cancellation in `delta_+` or `delta_-` does not invalidate the identity; the corresponding same-mode query term remains present.

Since `0 < p_a < e`, we have `|A| <= 1` and `0 <= B <= e`. The pointwise triangle inequality gives (4). The coefficients may depend on and be correlated with every field in the equation: their uniform pointwise bounds suffice. There is no division by a gate and no probabilistic factorization.

### 3. Actual shared adjoint and inequality (5)

At each time, exactly one bounded operator `W^(3)` is used in both definitions of `q^(2)_a`. Hence

```text
q^(2)_+ = (W^(3))* delta^(3)_+,
q^(2)_- = (W^(3))* delta^(3)_-.
```

The equality concerns the actual trained fields and the actual adjoint. It requires no independence of the input and output populations or of the operator and the fields.

For either sign, (4), the triangle inequality in `L2`, and the adjoint norm bound give

```text
||M^(2)_sign||_2
  <= ||delta^(2)_sign||_2 + e ||q^(2)_sign||_2
  <= ||delta^(2)_sign||_2
       + e ||W^(3)||_op ||delta^(3)_sign||_2.
```

Squaring and applying `(a+b)^2 <= 2a^2+2b^2` gives precisely (5). The operator norm is squared, and the gate coefficient becomes `e^2`, as required. No multiplication of two uncontrolled `L2` fields occurs here.

### 4. Raw energy and normalization of every parameter block

The block expansion consistent with (1) and the stipulated raw-gradient chain rule is

```text
||theta'||_raw^2
  = ||(Z^(1))'||_first^2
      + ||(W^(2))'||_HS^2
      + ||(W^(3))'||_HS^2
      + ||(W^(4))'||_2^2.
```

This can also be checked directly from the factors in the equations. Differentiating the sample half-difference defining `g`, the contribution of a middle matrix variation `B` is the Hilbert--Schmidt pairing of `B` with

```text
(delta^(ell)_1 tensor H^(ell-1)_1
   - delta^(ell)_2 tensor H^(ell-1)_2)/2.
```

Setting `B = (W^(ell))'` gives its squared Hilbert--Schmidt norm. The readout contribution is `E_3[(W^(4))' V^(3)] = ||(W^(4))'||_2^2` by (1).

For `|rho| < 1`, let `d = (delta^(1)_1, -delta^(1)_2)^T/2` and `v = (Z^(1))' = C d`. The first-layer contribution to the derivative is

```text
E_1[d^T v] = E_1[v^T C^(-1) v] = ||v||_first^2.
```

There is no extra averaging factor of `1/2` in this displayed first-pair metric. For `rho=-1`, the reduced field has `Z' = (delta^(1)_1+delta^(1)_2)/2 = delta^(1)_+`; its contribution is exactly `E_1[(Z')^2]`, matching the stated reduced metric. Both cases give nonnegative first-block energy. The candidate does not specify a `rho=1` metric or assert that case.

Thus retaining only the two middle matrix blocks in the full energy is legitimate with coefficient one for each block. There is no missing factor from the two samples, the readout, or the first-layer metric.

The rank-one operator convention is also correct:

```text
(u tensor v)h = u E[vh],
||u tensor v||_HS^2 = ||u||_2^2 ||v||_2^2.
```

For a finite illustration of this normalization, with `n` uniformly weighted input coordinates and `m` uniformly weighted output coordinates, its coordinate matrix is `u v^T/n` and its adjoint has coordinate matrix `v u^T/m`. The two RMS metrics give the same norm product displayed above. For a general coordinate matrix `A` between these spaces, the adjoint is `(n/m) A^T`. With equal widths this is the ordinary transpose. The candidate's population proof uses the actual Hilbert-space adjoint throughout and does not depend on a finite-width limit or an unnormalized Frobenius norm.

### 5. Operator drift bound

Absolute continuity of the Hilbert--Schmidt increment and `||B||_op <= ||B||_HS` give, for `ell=2,3`,

```text
||W^(ell)(s)-W^(ell)(0)||_op
  <= integral_0^s ||(W^(ell))'(t)||_HS dt
  <= sqrt(s) (integral_0^s ||(W^(ell))'(t)||_HS^2 dt)^(1/2)
  <= sqrt(S) sqrt(g(S))
  <= sqrt(S).
```

Accordingly `||W^(ell)(s)||_op <= M_ell` with exactly the candidate's definition. This needs only the energy on the assumed interval, not continuation of the path. The energy identity gives `g(S) >= 0`; its assumed upper bound gives the final step. There is no omitted initial Hilbert--Schmidt norm or extra time factor.

### 6. Matrix mode decomposition, orthogonality, and (7)

Using `delta_1 = delta_+ + delta_-`, `delta_2 = delta_+ - delta_-`, `H_1 = U+V`, and `H_2 = U-V` in (1) gives

```text
W' = delta_- tensor U + delta_+ tensor V.
```

The factor `1/2` in (1) cancels the factor `2` from the expansion. Before using symmetry, the exact squared norm is

```text
||W'||_HS^2
  = ||delta_-||_2^2 ||U||_2^2
      + ||delta_+||_2^2 ||V||_2^2
      + 2 <delta_-,delta_+> <U,V>.
```

The stated equality of the two feature second moments gives

```text
<U,V> = (||H_1||_2^2-||H_2||_2^2)/4 = 0.
```

This proves (6). No equality of the two delta second moments is needed. The norm products follow from the rank-one operator geometry, not an independence assumption concerning the trained fields.

Because both sample features are at least one, `U >= 1` and `||U||_2^2 >= 1`. Applying (6) to `W^(2)` uses symmetry in population 1; applying it to `W^(3)` uses symmetry in population 2. These are exactly the two symmetry assumptions supplied. Symmetry in population 3 is unnecessary.

Adding the two matrix actions and dropping the other nonnegative raw-energy blocks proves (7), with all four terms sharing the single budget `g(S)`.

### 7. Contrast propagation and the squared integrated constants in (8)

The shared forward operator gives

```text
(Z^(2)_1-Z^(2)_2)/2 = W^(2) V^(1).
```

The pointwise `e`-Lipschitz bound for `phi`, followed by the operator norm bound between the two different populations, therefore gives

```text
||V^(2)||_2 <= e ||W^(2) V^(1)||_2
             <= e M_2 ||V^(1)||_2,
kappa_2 <= e^2 M_2^2 kappa_1.
```

The two factors of `1/2` from the feature and preactivation differences match; there is no additional factor of two.

To check the integrated constants without concealing the common energy budget, define the four nonnegative numbers

```text
I_2 = integral_0^S ||delta^(2)_-||_2^2 ds,
I_3 = integral_0^S ||delta^(3)_-||_2^2 ds,
J_2 = integral_0^S kappa_1 ||delta^(2)_+||_2^2 ds,
J_3 = integral_0^S kappa_2 ||delta^(3)_+||_2^2 ds.
```

Equation (7) says `I_2+I_3+J_2+J_3 <= g(S)`. Equation (5) consequently gives

```text
integral_0^S ||M^(2)_-||_2^2 ds
  <= 2 I_2 + 2 e^2 M_3^2 I_3
  <= 2(1+e^2 M_3^2) g(S),

integral_0^S kappa_2 ||M^(2)_+||_2^2 ds
  <= 2 integral_0^S kappa_2 ||delta^(2)_+||_2^2 ds
       + 2 e^2 M_3^2 J_3
  <= 2 e^2 M_2^2 J_2 + 2 e^2 M_3^2 J_3
  <= 2 e^2 (M_2^2+M_3^2) g(S).
```

Thus both constants in (8) are valid. They are conservative uses of the shared energy budget, not incorrectly squared constants. In the average estimate the weight is `kappa_2` throughout the left side; its first delta term is converted to the available `kappa_1` weight by the forward inequality. Its second delta term already has exactly the available `kappa_2` weight. No ratio of contrasts is taken.

These are integrals of squared spatial `L2` norms. If instead one wants the square of a time integral of a norm, Cauchy--Schwarz adds a factor `S`; for example,

```text
(integral_0^S ||M^(2)_-||_2 ds)^2
  <= S integral_0^S ||M^(2)_-||_2^2 ds.
```

The candidate's displayed (8) makes no contrary assertion.

### 8. Zero contrast and adversarial degeneracies

All contrast weights are nonnegative. If `kappa_1=0`, then `V^(1)=0` in `L2`, so the forward relation forces `kappa_2=0`. If `kappa_2=0`, the weighted average-mode integrand is zero, and every inequality used above remains valid. Neither a zero nor a small contrast introduces a denominator.

One can check the difference mode directly at zero second-layer contrast as well: strict monotonicity of `phi` implies `Z^(2)_1=Z^(2)_2` almost everywhere. The common forward operator then gives equal third-layer preactivations, hence equal third-layer deltas under the common readout. The shared adjoint gives equal middle queries, so `M^(2)_-=0`. This local check is consistent with the estimate and does not assume that a nontrivial path can actually reach such a state from the prescribed initialization.

I also checked the potential failure mechanisms suggested by unequal gates, signed queries, cancellation of a delta mode, sign-changing readout, very small contrast, and an initially bounded but non-Hilbert--Schmidt operator. The same-coefficient scalar identity, the actual adjoint bound, the absolute value of the common readout, and the increment formulation respectively handle these cases. None produces a counterexample under the stated assumptions.

The assumptions are doing specific work: without input-feature moment symmetry the matrix cross term can cancel part of the two diagonal terms; without a shared adjoint the modal query identity is unavailable; and without the positive feature floor the unweighted difference-mode energy estimate does not follow from (6). All three needed ingredients are present in this candidate.

### 9. Top curvature inequalities and their joint action bound

For `p_x=phi'(x)` and `p_y=phi'(y)`,

```text
phi''(x)-phi''(y)
  = (p_x-p_y) [1-(p_x+p_y)/e].
```

The bracket has absolute value at most one, proving the asserted difference inequality. Also `0 <= phi''(z) <= phi'(z)`. Let

```text
T_- = W^(4) [phi''(Z^(3)_1)-phi''(Z^(3)_2)]/2,
T_+ = W^(4) [phi''(Z^(3)_1)+phi''(Z^(3)_2)]/2.
```

Because the same readout field multiplies both samples,

```text
|T_-| <= |W^(4)| |phi'(Z^(3)_1)-phi'(Z^(3)_2)|/2
        = |delta^(3)_-|,
|T_+| <= |W^(4)| [phi'(Z^(3)_1)+phi'(Z^(3)_2)]/2
        = |delta^(3)_+|.
```

The final equality for the average uses the positivity of both gates, not a sign assumption on `W^(4)`. All these fields are in `L2` by bounded gate multiplication.

The precise joint top estimate is

```text
integral_0^S [||T_-||_2^2 + kappa_2 ||T_+||_2^2] ds
  <= integral_0^S [||delta^(3)_-||_2^2
                    + kappa_2 ||delta^(3)_+||_2^2] ds
  <= integral_0^S ||(W^(3))'||_HS^2 ds
  <= g(S).
```

Thus `g(S)` bounds the sum of the two weighted top actions, not merely each action separately. No extra factor two or additional population-3 symmetry is required.

### 10. Scope and unproved extensions

The result is conditional on an existing regular path on the assumed interval with (1), (2), and the stated feature-moment symmetry. Nothing in the argument supplies such a path, propagates symmetry from arbitrary initialization, removes cuts, or provides a global existence or continuation theorem.

Equation (8) controls the time integral of the squared `L2` norm of the middle difference mode and the corresponding `kappa_2`-weighted average mode. One cannot cancel `kappa_2` from this displayed estimate to claim an unweighted average-mode estimate. Likewise these estimates do not by themselves bound a product with an arbitrary correlated `L2` sensitivity, a multiplication-operator norm, exponential moments, or a retarded-response equation. The candidate expressly disclaims these extensions.

With `e=1/10` fixed, the stated upper constants depend only on `S` and the displayed initial operator norms. They do not contain an inverse contrast or inverse angle. The metric and path hypotheses still restrict which paths the conditional result covers; uniform-looking constants do not remove those hypotheses.

## Optional findings

These are expository improvements or stronger consequences, not conditions for the verdict.

1. **Display the full raw squared-speed decomposition.** The first-layer and readout metrics are specified, but the note does not write the block expansion used when retaining the middle matrix energies. The expansion in audit section 4 would make the coefficient-one Hilbert--Schmidt contributions explicit. Their normalization is consistent with the stipulated chain rule and (1), so this is not a missing mathematical estimate.

2. **Write the top action as an explicit integral of squared norms.** Replace the prose phrase “Their squared integral” with the displayed joint top estimate in audit section 9. This removes ambiguity between an integral of squares and the square of a time integral; the latter requires the additional time factor explained above.

3. **Tighten (8) if useful.** Since the four nonnegative delta actions share one energy budget, its two constants can be improved respectively to

   ```text
   2 max{1, e^2 M_3^2},
   2 e^2 max{M_2^2, M_3^2}.
   ```

   The same proof also yields the combined middle estimate

   ```text
   integral_0^S [||M^(2)_-||_2^2 + kappa_2 ||M^(2)_+||_2^2] ds
     <= 2 max{1, e^2 M_2^2, e^2 M_3^2} g(S).
   ```

   The larger constants actually printed in the candidate remain correct.

4. **Clarify the finite-coordinate aside if unequal widths are intended.** In `u v^T/n`, `n` is the source population size for that action. The reverse action has denominator equal to its own source size, as shown in audit section 4. Equal widths need no distinction. The candidate's population adjoint calculation is already correct.

No candidate edits are required for the stated conditional lemma.
