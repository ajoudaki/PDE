# Independent audit of the nonlinear-reference partial claims

2026-09-08. Reviewed `/tmp/three_nonlinear_reference_20260908.md`, SHA-256 `b97aafbac18a9966ed6cffe1c0d31e108fafef91202dde1b24c1a5c060e40a68`. This is an audit of the new algebraic/conditional claims, not a certificate for a complete three-input global theorem.

**Verdict: PASS for the complete-kernel null-direction upper bound with constant 256, the Gram-nonmonotonicity example, and their stated limited implications.** No substantive mathematical correction is required. The differentiability details that justify the potentially delicate steps are supplied below.

## 1. Exact raw null-direction estimate

For fixed sample coefficients `v in ker Gamma`, `sum_i v_i x_i=0`. Successively using `phi(z)=az+e atan(z)` gives, at every raw state,

\[
 v^Tf=e\langle C,a^2BA T_1+aBT_2+T_3\rangle=eN_v.
\]

The identity is exact, not a Taylor expansion in e. With `U=11+R`, each initialized/projected size and each learned action increment is bounded as stated. In particular `||z_i^1||<=U`, `||h_i^1||<=U`, `||h_i^2||<=U^2`, and `||C||,||A||,||B||<=U`.

For a fixed raw perturbation direction, the scalar Nemytskii maps `atan` and `phi` have strong L2 directional derivatives given by their bounded pointwise derivatives. This follows by pointwise differentiation and dominated convergence, with the square-integrable dominating function `K|dz|`. Iterating along the raw straight line uses the ordinary product rule for bounded actions and their HS perturbations. Thus the displayed `dT_l` bounds are legitimate strong directional bounds even though the full feature map is not asserted Frechet differentiable on all of L2.

The actual scalar predictor is continuously Frechet differentiable by the weighted scalar argument of Part F. Therefore `N_v=(v^Tf)/e`, for fixed e>0, is also scalar C1. The computed directional derivative is its Frechet derivative. There is no inference from a nonexistent vector-valued Frechet derivative.

Writing `q=||v||_1`, the block coefficients of `|dN_v|` can be checked directly:

- `p_w`: three terms, each at most `q U^3 p_w`, total `3qU^3 p_w`.
- `p_A`: the derivative of the explicit A contributes `(pi/2)qU^2 p_A`; the derivatives of `T_2,T_3` contribute at most `qU^3 p_A` each. Replacing `U^2` by `U^3` gives `(pi/2+2)qU^3 p_A`.
- `p_B`: the explicit B derivatives contribute `(pi/2)q(U^2+U)p_B`, and the `T_3` derivative contributes `qU^3p_B`. This is at most `(pi+1)qU^3p_B`.
- `p_C`: the bound is `(pi/2)q(U^2+U+1)p_C <=(3pi/2)qU^2p_C`.

Each block norm is at most the full raw norm. Summing and using `U>=1` gives

\[
 |dN_v|\le(6+3\pi)qU^3\|d\Theta\|_{\rm raw}
 <16qU^3\|d\Theta\|_{\rm raw}.
\]

The full kernel is the Gram of the four-block raw gradients, so

\[
 v^TKv=\|\nabla_{\rm raw}(v^Tf)\|^2
       =e^2\|\nabla_{\rm raw}N_v\|^2
       \le256e^2\|v\|_1^2(11+R)^6.
\]

For `||v||_2=1` in three-dimensional sample space, `||v||_1^2<=3`, giving 768 as stated. All four raw blocks, including the first projected-weight block with its factor d, are accounted for. The estimate is an upper bound and supplies no lower coercivity or positive-e failure claim.

## 2. Initial acceleration and Gram differentiation

On an already-existing strong solution the forward features possess strong derivatives along that trajectory by the bounded multiplier/strong chain rule. Consequently differentiating `||Hc||^2` gives the claimed Gram identity, without a sign conclusion.

The use of a second derivative at `C(0)=0` requires a little care because a global Hessian of the L2 feature map is not assumed. It is nevertheless justified at this special state. Write the hidden gradient of a scalar prediction as `J_i(v)^* C`, where `J_i(v)` is the bounded directional feature derivative at fixed hidden state. The existing bounded-multiplier argument implies that `(v,C)->J_i(v)^* C` is jointly strongly continuous. Since

\[
 C(t)/t\to H_0y,\qquad r_i(t)\to-y_i,\qquad v(t)\to v_0,
\]

one obtains directly from the true raw equations

\[
 \dot v(t)/t\to\sum_i y_i J_i(v_0)^*H_0y
   =D(Hy)_0^*H_0y=:V.
\]

Thus the right second derivative of v at zero exists and equals V. The scalar map `v->(1/2)||H(v)y||^2` is C1 by the same weighted scalar chain rule, with gradient `D(Hy)^*Hy`. Differentiating along the strong trajectory and using the above limit proves

\[
 \left.\frac{d^2}{dt^2}\|H(v(t))y\|^2\right|_{0+}
 =2\|V\|^2.
\]

This proves the claimed initial identity with exactly the available regularity. It is conditional on existence of the true strong trajectory, as the note states.

## 3. Gram-nonmonotonicity example

For the finite-dimensional model
`H_1(v)=(1+v,0)`, `H_2(v)=(0,1-2v)`, `y=(1,1)`,
the smooth gradient equations give `C_1'(0)=C_2'(0)=1` and

\[
 \dot v=-r_1C_1+2r_2C_2=-t+o(t).
\]

Hence `v(t)=-t^2/2+o(t^2)`. Because Q is diagonal, its entries are exactly `(1+v)^2` and `(1-2v)^2`, yielding

\[
 Q_{11}(t)=1-t^2+o(t^2),\qquad
 Q_{22}(t)=1+2t^2+o(t^2).
\]

The minimum eigenvalue therefore decreases for all sufficiently small positive t. This is a valid counterexample to inferring Gram monotonicity solely from readout linearity, zero initial readout, and gradient flow. The manuscript correctly does not label it a counterexample within the specific Gaussian-initialized L3 architecture.

## 4. Other checked boundaries

The residual-direction formula follows by differentiating `r/||r||` while `r!=0` and using `r'=-Kr`. The Lie-bracket formula uses the convention `[X,Y]=DY X-DX Y` and the symmetry of Gamma; its stated nonvanishing possibility is correct. The bounded-readout estimate for pure arctangent is an exact pointwise integral bound, and no invalid L-infinity operator bound for the initialized transpose is inferred from it.

One wording clarification is advisable when presenting Section 5: a particular nonlinear reference with a finite total residual clock may have constants independent of physical horizon, but the original compact-time theorem also permits a direct construction with constants depending on each finite T. What must be horizon independent in either route is the single chosen activation. This distinction does not affect any of the audited bounds, and the manuscript's other discussion correctly identifies the finite-horizon alternative.

## Final-copy verification

Independently verified the final repository copy `studies/mean_field_peeling/three_sample_odd_activation_threshold/routes/NONLINEAR_REFERENCE.md`, SHA-256 `2e0381a184f9802377f96163fd8f68ae336dfb3cbd18a2ea07da6f364b253d2a`. Its only difference from the audited original is the Section 5 wording clarification described above: the uniform-clock method is a sufficient route, and a direct compact-time construction may have T-dependent constants while retaining a single T-independent activation. This correction is accurate. **Final-copy limited-claims verdict: PASS.**

Also verified that final `routes/GEOMETRY.md` has SHA-256 `08768e8c190e0e428efe978fa751b35b7444d327364c7bd393a2e9af9eee2fa9`, byte-identical to the separately audited geometry original. Its limited-claims PASS is unchanged.
