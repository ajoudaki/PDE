# Approach registry

| ID | Route | Exact target | Status | Falsifier / gate |
|---|---|---|---|---|
| A | Multi-matrix adaptive conditioning | Fixed-`h` width limit for every finite `(L,N)` | **completed / hostile PASS** | `WIDTH_DEPTH_TIME.md` closes predictability, rank, concentration, stopping removal, and terminal uniform integrability; see `AUDIT_WIDTH.md` |
| B | Inverse-free singular Price compiler | `C^5` width-first output and an explicit fifth-order envelope | **completed / hostile PASS** | `COMPILER_DEPTH_TIME.md` closes the `C^{12}` derivative budget and explicit envelope recursion; see `AUDIT_COMPILER.md` |
| C | Nodewise compact cubic recursion | exact quadratic law of `kappa_{phi,L,t}` in `t` and nine activation moments | **completed after Route D2** | the contraction algebra is proved on the common fixed-operator germ and reduces correctly at depth two, identity, affine, and constant activations |
| D1 | Finite-list cylindrical oracle | one-invariant factor `-t(2t-1)J_{phi,L}/2` | **failed / superseded** | `AUDIT_CUBIC.md` found circular source-jet lists, no enlargement cocycle, moving-query misuse, and unproved singular mixed regularity |
| D2 | Fixed bounded-operator bridge `W_{a,0}=I_a+J_a^*` | common singular gradient germ and exact temporal/Euler intertwining | **completed / hostile PASS** | fixed isometries give raw Gaussian laws, adjoints give intrinsic responses, and chronological induction matches every temporal node; see `OPERATOR_BRIDGE_CHECK.md` and `AUDIT_CUBIC_REAUDIT.md` |
| E | Uniform Koopman/Banach operator | shared `C_phi,L t^4` fifth-order bound on `|eta| <= c_phi,L/t` | exploratory | must construct a fixed state space and uniform `C^5` one-step bounds for the actual reused-matrix DAG |
| F | Finite-width Taylor then `n -> infinity` | shortcut to cubic coefficients | rejected | violates the prescribed order of limits unless an independent intertwining theorem is supplied |

Routes A, B, C, and D2 now combine into the unconditional fixed-`(L,t)`
theorem. Route D1 remains in the registry as a superseded negative result,
so its loopholes are not reintroduced. Route E is still required for a
polynomial-in-`t` remainder constant uniform over unbounded time.
