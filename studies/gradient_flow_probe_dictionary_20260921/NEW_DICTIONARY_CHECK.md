# Finite-carrier derivative dictionary implementation and checks

`new_dictionary.py` is study-owned code. It imports the maintained
`pde.observable_torch_p1.ClosureEngine` and `TensorState`; no other study
implementation is used. It performs no training or file writes.

## Declared construction

The comparison uses historical normalized directions `u=e1,e2`, hence
physical probes `x=sqrt(2)e1,sqrt(2)e2`, for both dictionary families. This
differs from the literal physical axes in the original derivation. Accordingly
`h=tanh(w0)`, `H=tanh(W0 h)`, `U_ab=H_b(1-H_a^2)`,
`L_ab=(1-h_a^2)^2 W0.T U_ab`, and

```text
F_ab = v U_ab + W0 L_ab,
v = E[tanh(G)^2], G standard normal.
```

The coefficient would be `2v` at the original literal physical axes; it is
`v` at this comparison's shared scale. The working Gaussian variance uses
deterministic 256-node Gauss-Hermite quadrature:

```text
v128 = 0.39429449039796227
v256 = 0.3942944903978411
absolute discrepancy = 1.2118084313783584e-13
```

The discrepancy is recorded, not asserted to be a rigorous integration-error
bound. New levels p=1,2,3 denote maximum middle-weight powers t^2,t^3,t^4.
The conceptual p=0 is not accepted by the implementation.

Both p=1 and p=2 use lower `(h1,h2)` and upper `(U11,U12,U21,U22)`.
For p=3, append lower `(L11,L12,L21,L22)`. With
`A_abc=D_a D_b F_bc`, `B_abc=H_c phi''(Z_a) F_ab`, append these eight
upper functions, in this order:

```text
C1 = A111 + 3 B111
C2 = A112 + 3(B112+B121)
C3 = A121 + 3 B122
C4 = A122
C5 = A211
C6 = A212 + 3 B211
C7 = A221 + 3(B212+B221)
C8 = A222 + 3 B222
```

For the h1 factor, these first four functions multiply
`(y1^4,y1^3 y2,y1^2 y2^2,y1 y2^3)/6`; for h2 the final four multiply
`(y1^3 y2,y1^2 y2^2,y1 y2^3,y2^4)/6`. Thus they collect repeated symbolic
label monomials before defining the dictionary. They do not introduce labels
into frozen marks. No derivative factorial or RMS scaling is applied to the
prescribed columns. The dictionary sizes are `(2,4),(2,4),(6,12)` and the
unrestricted middle matrices have `8,8,72` entries. This implementation check
does not extend the population minimality argument to finite-width jets.

For each side, `G=psi.T psi/n`, `L L.T=G+eta I`, and `b=psi L^{-T}`, with
`eta=1/[1024(p+1)^2]`. Initialize `M0=b2.T W0 b1/n`. The entire represented
middle block is `b2 M0 b1.T/n`; there is no retained dense background. Both
the first weights and the finite random readout are copied from the same
canonical carrier. Ordinary maintained coordinate dynamics therefore use
the same ridge-filtered metric as the inherited comparison rule. Ridge is
not exact orthogonal projection, and the small increment dictionary does
not preserve the original full initialized network.

## API and diagnostics

```text
raw_features(initial, p) -> (psi1, psi2, metadata)
build(initial, p, *, block_size=512, forward_mode="auto")
    -> (ClosureEngine, TensorState, metadata)
```

`initial` is the maintained finite engine's `TensorState`. Device and dtype
are preserved. The resulting engine retains its own frozen arrays and no
dense initialized matrix. Diagnostics include raw and effective Gram
eigenvalues, numerical ranks and their explicit thresholds, directions with
filter eigenvalue above one half, effective degrees of freedom, ridge
condition, Cholesky residual, and the ridge-whitening identity residual.
Numerical ranks use `max(n,K)*dtype_epsilon*largest_Gram_eigenvalue`.
All metadata is JSON-serializable. The first two raw dictionaries are
identical; their only order-dependent change in `build` is eta.
The builder rejects nonfinite diagnostics, ridge condition above `1e10`,
or direct triangular relative residual
`norm(b L.T-psi)/norm(psi)` above `1e-8` (zero input uses the absolute
residual). These are operational gates, not accuracy guarantees.

## Independent small CPU validation

Executed on CPU float64, width 37, seeds 9 and 41, with five numerical label
pairs per seed (including zero, single-axis, mixed-sign and unequal labels):

```text
PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 /home/amir/miniconda3/bin/python -B studies/gradient_flow_probe_dictionary_20260921/validate_new_dictionary.py
```

Result: **PASS**. The validator independently reconstructs initialized
fields; checks the normalized-probe R coefficient; contracts arbitrary labels
before comparison with the eight collected functions; checks the complete
cubic feedback tensor; compares initial middle matrices with direct
`psi (G+eta I)^{-1} psi.T/n` filters; checks initial predictions; and compares
the maintained velocity against independent autograd of the current nonlinear
loss with mobilities `(n,n,1)` for `(w,c,M)`. It also verifies input-state
ownership and exact p=1/p=2 raw-table identity.

Maximum absolute discrepancies across these checks:

| Check | Maximum discrepancy |
|---|---:|
| Normalized-probe F/R coefficient | 4.441e-16 |
| Collected quartic upper coefficients | 1.777e-15 |
| Complete cubic feedback tensor | 1.777e-15 |
| Direct filtered initial middle matrix | 7.009e-16 |
| Direct initial prediction | 7.807e-18 |
| Independent loss-gradient velocities | 2.776e-16 |
| Raw level identity and preserved read-in/readout | 0 |

The relative-to-max(1,reference) comparison tolerance is 3e-12; exact-copy
checks use zero tolerance. Cholesky relative residuals were below 2e-14 and
ridge identity residuals below 2e-11. Observed numerical ranks were `(2,4)`,
`(2,4)`, `(6,12)` for both seeds. These are finite implementation and algebra
checks, not training, a population convergence test, or exact finite-width
Taylor matching. The maintained backend emitted a Torch TF32 API deprecation
warning during CPU construction; it did not affect the checks.

The final gated implementation was checked again on 2026-09-21. Retained
evidence is in
`data/generated/gradient_flow_probe_dictionary_20260921/implementation_check01/checks.json`;
`stdout.json` preserves the validator's exact JSON output and `stderr.txt`
preserves the warning. The checks record the exact command above, working
directory `/home/amir/Codes/PDE`, environment settings, UTC check time, and
these SHA-256 source hashes:

```text
new_dictionary.py
69e961da6614823f9d8afa8258a097aefef13ce37faf9b2b9184182b7ef9fb87
validate_new_dictionary.py
0ba4ce3b257205a81443afc188e997a7a3f5d55dc532f107f092d3f1cb907af1
```
