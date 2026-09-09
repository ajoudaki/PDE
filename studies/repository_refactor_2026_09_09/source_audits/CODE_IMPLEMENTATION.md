# Completed finite-network implementation

**Final scope:** the four finite-network files below plus `code/pde/gaussian_moments.py` and `code/tests/test_gaussian_moments.py`. The combined suite has **26 passing tests** (15 finite-network, 11 Gaussian moments), including execution from `/tmp` with an explicit import path; final unittest runtime 0.107 s. All six file hashes are in `SHA256SUMS`.

After the read-only audit, the user authorized implementation in a disjoint scope. Added only:

- `/home/amir/Codes/PDE/code/pde/finite_network.py`
- `/home/amir/Codes/PDE/code/pde/__init__.py`
- `/home/amir/Codes/PDE/code/tests/test_finite_network.py`
- `/home/amir/Codes/PDE/code/README.md`

No Git commands or edits, donor edits, theory-document edits, dependency installations, production experiments or generated-data writes were performed. The 556-file source inventory describes the pre-relocation paths; the main agent's move manifest owns their new locations.

The finite implementation follows the actual `docs/NOTATION.md` and `docs/finite_dynamics.md` contracts, which supersede the audit's preliminary optimizer/initialization discussion: equal hidden width n, W1 initialization variance 1, stored hidden-matrix variance 1/n, stored readout variance 1/n², X/sqrt(d), output a^T h/n, mean squared loss without a half factor, and block mobilities n*kappa1, kappa2,...,kappaL,n*kappa_readout. Hidden forward passes use the stored matrices directly. Delta does not contain the residual. GD is simultaneous in all stored raw parameter blocks.

The package exposes `Parameters`, `Activation`, `ForwardPass`, `initialize`, `forward`, `backward`, `loss`, `loss_gradients`, `flow_velocity`, `gd_step`, `kernel_blocks`, and `kernel`, with TANH/ARCTAN/IDENTITY and per-layer custom activations. Runtime requires only NumPy and stdlib; no code or comments depend on studies, private paths or old absolute paths. No runtime output writer is included.

## Validation

All 15 unittest methods passed in 0.100 seconds from the repository and 0.105 seconds from an unrelated cwd. They verify exact Gaussian draw/scaling order, tiny stored readout, depth 1/2/3 and width one, input normalization, all-coordinate finite differences in every parameter block, each kernel block against independently differenced output Jacobians, kernel symmetry/PSD, flow/output/weighted-energy identities, all-depth GD against numeric gradients, one exact hand-calculated simultaneous update, immutability of inputs during updates, correlated/opposite/repeated data and conflicting labels, batch permutation/duplication, zero residual, zero step and input/shape/activation/mobility validation. The initial run caught a string-activation validation error; it was fixed before both passing runs.

An additional read-only comparison to the relocated `studies/mfp_gaussian_calculus/depth/finite_width_jet.py` passed at depths 1,2,3,5. It explicitly converts the new stored middle matrix to the independent reference's unscaled matrix by sqrt(n), matches the same first preactivation, and compares c^T f and c^T K c to the independently generated zeroth/first feature-ascent derivatives. This diagnostic lives only in the private `migration_crosscheck.py` and is not a dependency of the library or its tests.

Exact test command from the repository root:

```sh
env PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 45s python -B -m unittest discover -s code/tests -p 'test_*.py' -v
```

The tested environment is Python 3.10.12 and NumPy 1.26.4. It differs from the repository's historical numerical pins. The earlier 83 passing existing audit tests/checks are separate from this 15-method new implementation suite.

`SHA256SUMS` records full SHA-256 hashes for all six implementation files and the two canonical documents read as contracts. They were read after the final source change.

## Remaining scope

The implementation intentionally matches the equal-width contract; it does not generalize optimizer metrics to unequal widths. It returns an exact flow velocity, not an exact ODE solution. No claim is made that arbitrary GD steps decrease the loss, or that finite tests prove a population limit.

The user's subsequent request for one small exact MFP building block is complete: `gaussian_moment(covariance, powers) -> Fraction` lives in `code/pde/gaussian_moments.py` and is re-exported by `pde`. It adapts the small Isserlis recurrence from the now-relocated `studies/mfp_gaussian_calculus/compiler/normal_form.py`, with a new complete standalone input contract and exact Schur-complement PSD validator. The source contains no donor/path references or runtime dependencies on a compiler. Its implementation uses stdlib only; importing the public package also imports the NumPy finite-network API.

The covariance domain is nonempty finite list/tuple matrices of integer/Fraction entries, square, symmetric and PSD including singular and zero matrices. Powers are matching finite sequences of nonnegative integers; floats and booleans are rejected. Type violations raise TypeError; invalid shape, negative powers or non-PSD covariance raise ValueError. Validation precedes odd/zero-degree shortcuts. Positive pivots use exact Schur complements; zero pivots require a zero corresponding row. Memoization is local and explicitly cleared in a finally block. The README documents state-count/rational-arithmetic growth and that this is no population-limit theorem.

The eleven Gaussian tests use exact uni-/bi-/trivariate known moments, independent coordinates, signed correlations, rank-one/zero covariance, permutation invariance, input preservation and cross-call cache isolation, malformed shapes/types/degrees, nonsymmetry, zero-pivot indefiniteness, and a rational negative eigenvalue boundary as small as 1/10**30. No large-order computations or symbolic framework were introduced. No generalization/residual-network or SciPy code was included.
