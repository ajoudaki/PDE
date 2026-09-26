# Internal contributor check: canonical training onset

**Outcome:** PASS for the gradient-flow onset calculation in equations
(2)–(8), the algebraic coordinate conversions in section 1, and the
mathematical scope restrictions in section 7. No correction to those
calculations is required. The canonical initialization and its attribution
to the book remain supplied inputs, as detailed below.

This is an internal contributor check, not an independent promotion review
or permission to promote the result. The checker first derived the onset
from a prompt specifying the closure and its gradient flow, and then checked
the frozen draft. No experiments or new research were performed.

## Frozen input and read coverage

- Input: `studies/closure_training_onset_20260921/ONSET.md`.
- Verified SHA256:
  `ff2e3d72e8ba601482fb6fe61f1ef6dc38d38b78e464a513b4b2534f74ee462a`.
- Read coverage: the complete supplied file; substantive audit coverage is
  complete sections 1–3, equations (1)–(8), and section 7.
  The initial complete read used hash
  `23d9c0885c39f8981f23c2a24102fe6392c5959327c82d6b6d03afca72195474`;
  the two subsequently reported local changes in sections 1 and 3 were
  reread and checked against the final hash above.
- Sections 4–6 were not mathematically audited by this check. Their specific
  Gaussian contractions, rank assertions, and polynomial-selection results
  receive no verdict here.
- The required rigorous-mathematics skill was read. No other repository
  research source was used, and only this report was written.

## Exact statement checked

For fixed finite feature dimensions, fixed bounded feature maps, bounded
labels, unit-circle inputs, the population metrics specified in section 1,
and the stated initial state `(G, 0, D_p)`, the closure's unhalved squared-loss
gradient flow has the uniform local expansion

\[
f_t=2t\mathcal Km-2t^2\mathcal K^2m
+t^3\left[\frac43\mathcal K^3m+
\mathcal Rm+\frac13\mathcal R^*m\right]+O(t^4),
\]

where `J = H''(0)` includes both first-hidden and middle-matrix motion,
and `R(u,v) = E_2[J(u)H_0(v)]`. The feature accelerations are exactly `W,N`
in equation (4). Relative to readout-only training with the same initialized
features, the unhalved training-loss difference is

\[
\mathcal L_{\rm full}(t)-\mathcal L_{\rm frozen}(t)
=-\frac23\left(\|W\|_{L^2(\Omega_1)}^2+\|N\|_F^2\right)t^3
+O(t^4).
\]

This is conditional on the stated closure and initialized mark law. It does
not identify an unspecified dense-network limit or establish a long-time
selection theorem.

## Checks and derivation

The positive ridge in (1) makes each raw second-moment matrix plus ridge
positive definite, so its Cholesky factor is invertible. With
`b_l = L_l^{-1} psi_l`, the raw and normalized bilinear expressions agree
precisely when `M = L_2^T K L_1`; this conversion is correct. Also,
`L_2^{-1} C_p L_1^{-T}` is the normalized contraction obtained from the raw
contraction `C_p` when the initialized action is linear. Neither this
algebra nor the supplied file alone independently verifies the asserted
book-specific value or provenance of that initialized action.

For the current forward map, its prediction derivatives in the three
parameter metrics are

\[
\nabla_cf(u)=H(u),\qquad
\nabla_Mf(u)=d(u)a(u)^T,\qquad
\nabla_wf(u)=(1-h(u)^2)q(u)u.
\]

Differentiating the unhalved loss therefore gives exactly (2), including
every factor of two. Replacing the label by its conditional mean is valid
because the prediction and its derivatives depend on the input and marks,
not on the sampled label. The unit input `u`, rather than the unnormalized
`x`, occurs consistently in both the forward map and its derivative.

At `c_0=0`, both `d_0` and `q_0` vanish. Hence

\[
c'_0=2S,\quad w'_0=M'_0=0,\quad H'_0=0,\quad f'_0=2\mathcal Km.
\]

The other two prediction-gradient blocks vanish at initialization, so
`mathcal K` is the entire initial tangent kernel in the stated metrics.
The loss slope is consequently
`-4 <m, mathcal K m> = -4 E_2[S^2]`, as asserted.

Since `d'_0=E_2[b_2 c'_0 g]=2B`, differentiating (2) gives

\[
M''_0=4\int mB a_0^T\,d\nu=N,
\qquad
w''_0=4\int ms(b_1^TD_p^TB)u\,d\nu=W.
\]

All omitted product terms contain a zero initial velocity, `d_0`, or `q_0`.
The first-hidden acceleration gives
`a_2=E_1[b_1 s(W dot u)]`. Because the preactivation velocities vanish,
the second derivative of the upper activation is exactly

\[
J=g\,b_2^T(Na_0+D_pa_2).
\]

In particular, no activation-second-derivative term survives at this order.
This verifies (4) and (5), with both moving feature blocks retained.

The readout derivatives in the draft then give

\[
f''_0=-4\mathcal K^2m,
\qquad
f'''_0=E_2[c'''_0H_0+3c'_0J]
=8\mathcal K^3m+2\mathcal R^*m+6\mathcal Rm.
\]

Dividing by `3!` confirms (6). The `R* / 3` term comes from the changed
features inside the readout update; the `R` term comes from the product
`3 c'_0 J`. Neither can generally be discarded. The adjoint is relative
to the same training measure `nu`, exactly as the draft specifies.

For (7), integrate `E_2[S J(u)]` against `m(u)`. The matrix contribution is

\[
\left\langle N,\int m(u)B(u)a_0(u)^T\,d\nu(u)\right\rangle_F
=\frac14\|N\|_F^2.
\]

The first-hidden contribution is

\[
E_1\left[W\cdot\int m(u)s(u)
(b_1^TD_p^TB(u))u\,d\nu(u)\right]
=\frac14\|W\|_{L^2(\Omega_1)}^2.
\]

These are all integrable bounded pairings. Since the kernel is real,
`<m,R* m> = <m,R m>`. Thus the pairing of `m` with the cubic feature
correction is `(||W||^2+||N||^2)/3`. Comparing squared losses introduces
the additional factor `-2`, proving the `-2/3` coefficient in (8).
The conditional label variance cancels between the two losses. A strictly
negative cubic loss difference requires at least one nonzero acceleration.

With frozen features, `f' = 2 K(m-f)`, giving
`f_frozen=(I-exp(-2tK))m` on `L^2(nu)`. Its power series starts with `K m`,
so it also has a unique kernel-defined extension to the entire input circle,
even when `nu` has finite support. This extension has the uniform expansion
used in the comparison.

The stated local remainder justification is adequate. On the Banach space
of bounded increments `w-G`, bounded `c`, and finite `M`, the vector field
is smooth and locally Lipschitz. Bounded features, inputs, labels, and real
activation derivatives give uniformly bounded derivatives of the required
orders on a local state ball. The resulting local smooth solution and
Taylor remainder are uniform over the circle. The argument correctly
avoids assuming that the Gaussian `G` itself is bounded, and asserts no
convergence of an infinite temporal Taylor series.

## Section 7 and limitations

Antipodal oddness follows directly from the bias-free forward map:
`h(-u)=-h(u)`, then `a(-u)=-a(u)`, and then `H(-u)=-H(u)`.
Consequently the initialized kernel is odd in each argument separately.
For the uniform circle, every even Fourier input column and output row
vanishes. The stated Fourier matrix action is valid; for each output mode,
the coefficient sum is justified by the `L^2` pairing. Antipodal oddness
does not imply rotation stationarity or a diagonal Fourier matrix.

The section correctly distinguishes initialization-based onset predictions
from endpoint or cross-order performance claims. The loss comparison is
only with the same closure's own frozen-feature flow. The result does not
require or imply a target-selected initial matrix. Dependence of the lower
fixed features on `G` must be retained; it was not replaced by independence
in this check.

No substantive correction was found. The final draft now says that the
feature-learning prediction term and order-`t^2` parameter motion are the
first possible such terms, and explicitly allows their coefficients to
vanish. This resolves the optional wording precision identified during
the check. Its section 1 revision also explicitly limits the H3.1
polynomial-core shortcut to `p <= 3` and refers new higher-order actions to
the full finite-source rule. This is a scope clarification of the supplied
model input; its book-specific correctness is outside this check.

Book-specific assertions in sections 1 and 7, including the correctness of
the canonical Gaussian action, its two orientations, the referenced H3.1
rule, and what the book does or does not assert, were not independently
verified: the assigned frozen input contains no complete underlying source.
This limitation does not affect the conditional gradient-flow calculation
above. It must not be represented as verification of those external inputs
or of sections 4–6.
