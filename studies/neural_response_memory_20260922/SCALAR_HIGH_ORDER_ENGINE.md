# Exact linear algebra for the scalar hierarchy

2026-09-25. This note documents `scalar_high_order_engine.py` under the frozen
`SCALAR_HIGH_ORDER_PROTOCOL.md`. It concerns the finite truncated equations,
not their approximation accuracy. No tensor symmetry is assumed.

## State and Jacobian

For an order P between two and six, retain real or complex ordered tensors
Tj of shape M^j, with TP fixed outside the moving state. Let alpha=2/M and
v=-alpha(T1-y). The moving training equations are

    Tj' = T(j+1) : v,       1 <= j < P,

where a vector contracts the last axis. Optional local signatures have
sigma0=1, sigmak'=v outer sigma(k-1), and zero initial values for k>=1.
Neither the signatures nor passive outputs affect training.

For a perturbation delta, the exact Jacobian action is

    (J delta)_j = deltaT(j+1) : v - alpha T(j+1) : deltaT1,
    (J delta)_sigmak = v outer deltaSigma(k-1)
                      - alpha deltaT1 outer sigma(k-1),

with deltaTP=0 and deltaSigma0=0. These formulas define the implemented sparse
Jacobian without finite differences. The moving training size is
sum_(j=1)^(P-1) M^j. Signatures double it. With signatures, the stored Jacobian
pattern has M^P + 4 sum_(j=2)^(P-1) M^j + M entries. For M=8,P=6, the augmented
state has 74896 entries and this pattern has 411912 entries. The terminal
tensor has 262144 entries.

The API is `ScalarHierarchy(coefficients, labels, order=None,
with_signatures=True)`, with coefficients named `T1` through `TP`.
`initial_state()` returns a fresh state. `tensors(state)`, `signatures(state)`
and `training_state(state)` expose the corresponding state views.
`reset_signatures(state)` returns a copy and preserves every training entry
bit for bit. The model owns a read-only copy of its fixed terminal tensor.

## Exact small Newton solve

Consider (I-gamma J)delta=b for any finite scalar gamma. The training block
equations rearrange to

    deltaTj = bj - alpha gamma T(j+1):deltaT1
                 + gamma deltaT(j+1):v.

Starting at j=P-1 and substituting backwards into the j=1 equation gives

    S deltaT1 = b1 + sum_(j=2)^(P-1) gamma^(j-1) bj:v^(j-1),
    S = I + alpha sum_(k=1)^(P-1) gamma^k A_k,

where A_k is T(k+1) with its k-1 intermediate axes contracted with v;
the first and last axes remain free. Thus S is only M by M. The signs follow
from delta v=-alpha deltaT1. TP is a fixed coefficient, so there is no bP.
After solving for deltaT1, the displayed backward recurrence recovers all
other moving training tensors. Forward substitution then gives

    deltaSigma1 = bSigma1-alpha gamma deltaT1,
    deltaSigmak = bSigmak-alpha gamma deltaT1 outer sigma(k-1)
                  + gamma v outer deltaSigma(k-1),  k>=2.

This is exact block elimination of the full Newton system. It is valid
whenever S is nonsingular, equivalently whenever the full Newton matrix is
nonsingular: eliminating the other blocks uses only identity diagonal blocks.
Every contraction is bilinear, including for complex inputs; no conjugation
or permutation of ordered derivative indices is used.

The implementation contracts with w=gamma v to avoid separately forming
powers of gamma. Factoring costs tensor contractions plus an M by M LU;
storage and tensor arithmetic remain O(M^P). It does not form or factor the
full Newton matrix on each step. `linearize(state)` owns immutable copies of
all coefficients used in this solve. `snapshot.factor(gamma).solve(b)` holds
both that snapshot and its original gamma even after the model state changes.
The immutable snapshot is required for a modified Newton iteration or cached
factor reuse; live state views would give the wrong linear system.

## BDF adapter and compatibility boundary

`StructuredBDF(model,t0,y0,t_bound,**options)` subclasses SciPy BDF. It inherits
`BDF._step_impl` without any replacement of the timestep, order selection,
Newton stopping rule, error estimate, or interpolation. The initial ordinary
sparse Jacobian selects the sparse base-constructor allocation path. Before
the first step, its Jacobian/factorization/solve callbacks are replaced by
immutable descriptors and the exact elimination above. A factor reused by
SciPy after a rejected error estimate retains its original gamma, as SciPy's
ordinary cached factor does.

The installed SciPy version used for source inspection and verification is
1.11.4. This adapter depends on BDF's internal `I-c*J`, `lu` and `solve_lu`
interface, so another SciPy version requires rerunning its compatibility
tests. The ordinary `model.jac` remains available for a stock sparse BDF
reference. Algebraic equivalence does not promise bitwise-identical floating
point trajectories. In particular, multiplying a residual by -alpha before
instead of after its contraction can differ in the last rounding bit.

## Passive transport and resetting

For passive tensors with first-axis length N and remaining axes of length M,
the exact local transfer is

    Tj_new = sum_(k=0)^(P-j) T(j+k)_old : sigmak,

contracting the last k axes and taking sigma0=1. Iterating the chain's integral
equations proves this identity: the newest velocity contributes the first
axis of the signature, while each additional nested integral contributes
one later axis. For an earlier segment sigma and later segment tau, the
combined signature is sum_r tau_r outer sigma_(k-r). Substituting this
concatenation into the transfer agrees with two successive transports.

`recenter_coefficients(coefficients,signatures)` uses the original old anchors
for every summand, returns new lower-order anchors and the identical terminal
array object, and mutates no input. Boundary arithmetic uses NumPy longdouble
or clongdouble as appropriate. This reduces cancellation but is not a proof
that any particular research endpoint is well conditioned; saved training
readout gaps and resolution gates are still required. Directly integrated
training tensors are preserved on resets rather than reconstructed from
signature polynomials.

## Deterministic checks

`test_scalar_high_order_engine.py` checks every Jacobian column by complex
step for P2 through P6; complex directional differences; structured solves
against independent dense and sparse solves for real/complex states, complex
right-hand sides and several real/complex gamma values; immutable cached
factors; P4 agreement with the previous engine; multisegment concatenation;
rectangular complex passive transport against a separately integrated forced
chain; and stock versus structured BDF on small fixtures. These checks test
implementation identities and solver equivalence, not research fitting or
the convergence of the hierarchy.
