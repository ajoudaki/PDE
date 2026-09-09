# Audit: general-activation constant-species residual IDE

Audit date: 22 August 2026.

Primary theorem:

- `CONSTANT_SPECIES_GENERAL_ACTIVATION_IDE.md`
- SHA-256: `dbfcdfc03208aa40695f56ff9065a6cea9a262447a55a2b4ea61694f6765929e`

Mechanical regression:

- `audit_general_activation_identities.py`
- SHA-256: `2b420e57778649252994c5348a3b2a297b6a3062b29a60208e94c18835022647`

## 1. Constant-species semantics audit

The comparison sources were the completed arctangent protocol, theorem, and
final audit.  They define “constant sized” as a fixed number of
field/operator/measure species, each of which may be infinite-dimensional.
They do not require a finite-dimensional scalar state or constant numerical
work.

Verdict: pass.

- The arctangent model has one immutable pointed action source and current
  state \((A,r,q,e)\): two \(L^2\) fields, one trace-class field, and one
  scalar.
- The residual particle model has one minimal dynamic species,
  \(s\mapsto\rho_t(s)\in\mathcal P_1(\mathbb R^p)\).
- The continuum of depth points is the domain of one field, not a growing
  family of state species.
- \(x,r,p,v,f,K\), and the loss are uniquely recomputed current-state
  readouts.  Restart uses \(\rho_{t_*}\) alone and retains no training
  history.
- This semantic match does not identify the two architectures.  The
  arctangent theorem is for a dense two-hidden-layer Ginibre model and needs
  transpose-action memory; the residual theorem is for a particle model and
  has no such source.

## 2. Functional-analytic reconstruction audit

An independent route reconstructed the theorem from A1--A2 and checked:

- the deterministic reachable state strip;
- global finite and characteristic well-posedness;
- completeness and measurability of the profile space;
- strict restartability in the characteristic class;
- uniform-in-depth Dobrushin stability;
- empirical \(W_1\) convergence under only a first moment;
- noncircular depth regularity;
- \(O(L^{-1})\) coupled depth consistency;
- kernel convergence; and
- arbitrary deterministic joint limits \(n,L\to\infty\).

Repairs forced by this audit:

1. A1--A2 are now described as conditions on the chosen raw
   parameterization, not as reparameterization-invariant conditions.
2. The map from a measure profile to its velocity is explicitly shown to be
   Lipschitz into a sup-norm space of continuous velocity fields before
   joint measurability of characteristics is used.
3. Uniqueness is explicitly limited to the stated characteristic class.
4. Grid evaluations use the canonical \(W_1\)-continuous depth
   representative.
5. The \(\mathcal P_1\) empirical argument now displays the radial-truncation
   inequality.
6. Nonaffinity plus an unmatched label is no longer asserted to guarantee
   motion; positive initial gradient energy is the exact condition.
7. The boundaries for ReLU, superlinear growth, and unbounded effective
   weights are explicit.

Final verdict: pass.  No \(C^2\) activation hypothesis or second moment is
needed for the stated qualitative theorem.

## 3. Hostile finite-closure audit

The audit independently proved the finite-point duality argument in
Proposition 12.1 and the generalized-Vandermonde infinite-rank corollary.
It then attacked the quantifiers and forced the following qualifications:

- the obstruction is universal over finitely supported laws;
- moments are fixed, linear, and state-independent;
- the recovery is exact, not approximate;
- a continuum of relevant state values and a nondegenerate variable-slope
  parameterization are required;
- finite atomic or otherwise special reachable orbits are not excluded;
- finite forward span is not sufficient for dynamic closure without
  invariance under the transport generators; and
- activation names alone do not imply infinite parameter-state rank.

The theorem now also gives a nonlinear one-moment special closure as a
counter-control and explicitly disclaims absolute minimality of the measure
field.

Final verdict: pass for the stated universal fixed-linear-moment
obstruction.  It is not a classification of all nonlinear closures.

## 4. Activation-diverse finite regression

Command:

```bash
python3 studies/mean_field_peeling/residual_continuous_depth_gradient_flow/audit_general_activation_identities.py
```

Frozen output:

```text
tanh: jac=4.457e-11 sym=0.000e+00 dyn=0.000e+00 lambda_min=8.571e-02
arctan: jac=3.721e-11 sym=0.000e+00 dyn=1.388e-17 lambda_min=9.407e-02
sine: jac=3.530e-11 sym=0.000e+00 dyn=2.776e-17 lambda_min=1.056e-01
identity: jac=4.684e-11 sym=0.000e+00 dyn=4.163e-17 lambda_min=1.903e-01
softplus: jac=3.334e-11 sym=0.000e+00 dyn=0.000e+00 lambda_min=8.342e-02
```

For every activation the script checks each finite output/parameter Jacobian
entry, kernel symmetry and positivity, and equality of the chain-rule and
kernel output velocities.  This is a regression audit, not a premise of the
analytic proof.

## 5. Final claim boundary

| Claim | Verdict |
|---|---|
| Exact finite algebra | proved |
| Constant-species autonomous IDE | proved |
| Global characteristic well-posedness and restartability | proved |
| Compact-time width and continuous-depth convergence | proved |
| Arbitrary joint \(n,L\to\infty\) without a rate relation | proved |
| General uniformly admissible \(C^{1,1}\) feature map | proved |
| Exact ReLU or superlinear/unbounded-weight extension | open/not claimed |
| Dense Gaussian-matrix ResNet | different problem/not claimed |
| Absolute finite-dimensional minimality | not claimed |

No formal proof assistant was used.  The result is a conventional analytic
proof with independent semantic, functional-analytic, hostile-closure, and
finite-regression audits.
