# Audit report: nonlinear residual mean-field IDE theorem

Audit date: 22 August 2026.

Audited theorem:

- `RESNET_MEAN_FIELD_IDE_THEOREM.md`
- SHA-256: `d380c3396a87186a52fc4351df12c7090374fbe4ed5333c23a9b80deccd9692e`

Finite-identity regression:

- `audit_finite_identities.py`
- SHA-256: `910e7d32e9642c583d7f11f51864ef3030494b174ce1aeb6677352a094bb9caf`

## 1. Independent algebra and normalization audit

Scope:

- residual normalization `1/(nL)`;
- gradient-flow multiplier `nL`;
- batch factor `1/B`;
- downstream sensitivity indexing;
- scaled finite and continuum kernels;
- finite and continuum loss dissipation.

Result: pass after two presentational repairs.  The population kernel was made explicit as equation (5.6), and the continuum loss was named explicitly.  The auditor independently recovered

\[
 \nabla_{\theta_{\ell i}}F_b^{n,L}
 =\frac1{nL}R_{b,\ell+1}^{n,L}
   \nabla_\theta\Phi(\theta_{\ell i},X_{b,\ell}^{n,L}),
\]

\[
 \dot F_b^{n,L}
 =-\frac\eta B\sum_cK_{bc}^{n,L}(F_c^{n,L}-y_c),
\]

and

\[
 \dot{\mathcal E}^{n,L}
 =-\frac\eta L\sum_\ell\frac1n\sum_i|q_{\ell i}^{n,L}|^2.
\]

Final discrepancy count in the assigned algebraic scope: zero.

## 2. Independent functional-analytic audit

Scope:

- completeness and measurability of the depth-profile state space;
- characteristic well-posedness and restartability;
- uniform-in-depth Dobrushin stability;
- empirical `W_1` source convergence;
- noncircular depth regularity;
- the coupled `O(L^{-1})` depth estimate;
- arbitrary joint width-depth quantifiers;
- justification of training-time differentiation.

Repairs made during the audit:

1. The metric-valued `L^1` state space was defined explicitly using Borel profiles with integrable first moment.
2. Uniqueness was stated in the named characteristic class.
3. The characteristic fixed-point map's joint measurability and continuity were derived from the Lipschitz map from the current profile to a continuous velocity field.
4. Grid values were tied to the canonical `W_1`-continuous depth representative.
5. Training-time differentiation of the forward depth equation was justified using the characteristic integral form, dominated convergence, and Volterra Gronwall.
6. The pathwise character and all layer-index ranges in the main estimate were made explicit.

Result: pass.  The auditor reconstructed the decisive estimates

\[
 \max_\ell e_\ell^X+\max_\ell e_\ell^R
 \le C d_L(\boldsymbol\mu,\boldsymbol\nu),
\]

\[
 d_L(\boldsymbol\mu_t,\boldsymbol\nu_t)
 \le e^{Ct}d_L(\boldsymbol\mu_0,\boldsymbol\nu_0),
\]

and

\[
 \sup_{t\le T}E_L(t)\le C_T/L.
\]

No circularity, missing moment hypothesis, or hidden relation between `n` and `L` remained.

## 3. Hostile scope and non-vacuity audit

Scope:

- whether the IDE is genuinely single-training-time and restartable;
- whether the theorem secretly asserts a stronger layer topology;
- whether arbitrary joint `n,L` convergence really follows;
- whether the nonlinear witness is degenerate or lazy;
- whether the result is improperly promoted to a dense Gaussian-matrix architecture.

Repairs made during the audit:

1. The introduction now distinguishes exact continuous-time training from the two actual limits.
2. The initialization statement and finite-second-moment theorem were reconciled.
3. `Nonlazy` was defined as a nonzero limiting transport velocity and strict order-one loss dissipation; no unproved claim about `dK/dt` is made.
4. The averaged initial residual field was proved nonaffine, not merely the individual neuron.
5. Unsupported language suggesting an automatic Gaussian-to-non-Gaussian transition was removed.
6. The boundary separating this particle ResNet from a dense CLT-scaled matrix ResNet was made explicit.

Result: pass for the stated scalar residual particle architecture and averaged-depth topology.  The audit explicitly rejects interpreting the theorem as any of the following:

- empirical `sup_layer W_1` convergence without a width-depth relation;
- a theorem for a dense Gaussian-matrix or standard matrix-muP ResNet;
- proof that the limiting kernel necessarily changes at first order;
- long-time optimization or convergence to a minimizer.

## 4. Computational finite-identity regression

Command:

```bash
python3 studies/mean_field_peeling/residual_continuous_depth_gradient_flow/audit_finite_identities.py
```

Frozen output:

```text
max_output_jacobian_error=4.4565847540090076e-11
kernel_symmetry_error=0.0000000000000000e+00
output_dynamics_error=0.0000000000000000e+00
kernel_min_eigenvalue=8.5710146311935020e-02
```

The script checks every output/parameter Jacobian entry at a random finite instance, scaled-kernel symmetry and positivity, and equality of the chain-rule and kernel output velocities.  This is a regression audit only and is not used as a premise of the analytic proof.

## 5. Final claim ledger

| Claim | Status |
|---|---|
| Exact finite forward, adjoint, gradient, kernel, and loss identities | proved analytically; independently audited |
| Global finite-`n,L` gradient flow | proved |
| Global depth-`L` population characteristic flow | proved |
| Global compact-horizon single-time IDE well-posedness and restartability | proved in the characteristic class |
| Exact-flow width convergence, uniform in depth under averaged `W_1` | proved |
| Population continuous-depth error `O(L^{-1})` | proved |
| Arbitrary joint `n,L -> infinity` convergence in probability | proved |
| Uniform compact-time output, MSE, and scaled-kernel convergence | proved |
| Explicit strictly nonlinear, non-frozen witness | proved |
| Empirical `sup_layer W_1` convergence for arbitrary `L(n)` | not claimed |
| Dense Gaussian-matrix/muP ResNet theorem | not claimed |
| Long-time optimization theorem | not claimed |

No formal proof assistant was used.  The theorem is a conventional analytic proof checked by three independent reconstruction audits plus one numerical finite-identity regression.
