###### D.5. Executable representation, storage and bounded validation

The library `pde.observable_laws` implements (H40.F1)–(H40.F3).
`supported_radius()` builds the fixed eleven-node integer expression;
`supported_law(a=...,b=...,c=...,d=...)` retains exact rational endpoints
and the fixed radius. The positive-integer expression operations are literal,
addition, multiplication and power of two. No scientific scope is inferred
from a floating coordinate or from a user-supplied tag. The time-40 validation
worker checks the saved radius against the canonical constructor before using
its supported-family tag. The separate positive rational-radius constructor
uses the same equations with explicitly exploratory scope.

For `m` midpoint nodes per nondegenerate conditional interval, a node has
parameter `a+(b-a)(2k+1)/(2m)` and mass `1/(2m)`. A degenerate interval has
one node of mass `1/2`. The exact conditional law and every midpoint rule
belong to the supported domain. The conditional mean distance from a uniform
parameter to its midpoint is its interval length divided by `4m`.
The Lipschitz constant `2rho` in (H40.F3), followed by the two half masses,
therefore gives

\[
 W_1(\mu_m,\mu)\le {\rho[(b-a)+(d-c)]\over4m}
 \le {\rho\over m}.                                      \tag{H40.I1}
\]

For fixed `m`, the exact midpoint coordinates are rational. This is an actual
finite integration rule for the nonatomic law, independent of population
integration. It does not replace that law by an unspecified sampling oracle.

The law description remains exact even when a finite realization deliberately
uses the reference directions. At decimal precision `p`, the implementation
may use radius zero if `E10>4(p+8)+2`; for float64 it takes `p=17` for this
decision. Comparison with the integer expression stops once an intermediate
value exceeds the finite cutoff and does not expand the tower. In this branch
`rho<2^[-4(p+8)-2]`, so each coordinate-vector replacement is at most `2rho`,
which is below `10^(-p-8)` because `2^4>10`. The exact descriptor, reason for
replacement and transport contribution are saved. This is a stated
approximation; tiny nonzero floating coordinates need not automatically round
to zero. A second flag identifies complete collapse caused by coordinate
rounding after exact coordinate construction.

More precisely, the replacement contributes at most
`rho[max(|a|,|b|)+max(|c|,|d|)]` to the normalized-direction transport cost.
The midpoint and replacement costs add. The implementation also records the
largest actual coordinate rounding error in L1 and the total weight rounding
error, as exact rationals computed from the retained working scalars.
Normalization only for the probability-law interpretation adds at most the
coordinate error plus eight times the weight error; the operational weights
remain literal. The mass and arithmetic arguments in D.4 account for them.

For every fixed law, `E10` is a fixed finite integer. As precision tends to
infinity, the deliberate replacement branch eventually ceases. With adequate
finite resource allowances the denominator can then be formed, the exact
rational rule evaluated, and all its coordinates rounded consistently. If
the caller's allowance is insufficient, the implementation rejects the request
instead of silently changing the radius or deleting nodes. The asymptotic
numerical theorem permits resource ceilings to increase to admit each fixed
finite computation; the default software ceilings are not mathematical
restrictions on the family or on the hierarchy. Resolving this radius at its
own scale is not a practical promise or a requirement of the operational
witnesses below.

Here is the full fixed-resolution storage and work contract. Let `P1,P2`
be the retained joint population sizes, `d1,d2` the dictionary dimensions,
`A` the data-node count, `B<=A` an input block size, and `J` the time-step
count through 40. The saved dynamic state is `w,c,M`; fixed retained data are
`b1,g,p1,b2,p2,D`, the law rule, the exact law description and the arithmetic
and integrator metadata. Its numerical scalar count is

\[
 S=P_1(d_1+5)+P_2(d_2+2)+2d_1d_2,\qquad
 S_{\rm data}=4A.                                         \tag{H40.I2}
\]

The two matrices are feature coefficient matrices of size `d2 by d1`.
There is no raw neuron-by-neuron middle matrix. `D` stores one initialized
action contraction; both training directions use `M` and `M^T`. The generic
initialized-word compiler finishes before evolution and its source transcript
is discarded. Evolution never asks for an arbitrary initialized action.

One RHS evaluation uses

\[
 O\!\left(A[P_1d_1+P_2d_2+P_1+P_2+d_1d_2]+S+A\right)
                                                              \tag{H40.I3}
\]

scalar operations, including validation and array handling. Input blocking
requires `O((P1+P2)B+(d1+d2)B+d1d2)` temporary scalar slots. Heun requires
two evaluations and a constant number of state/dynamic arrays; retaining
adjacent nodes for interpolation does not change this order. The total
evolution work is `J` times (H40.I3), and stage storage is `O(S+A)` plus the
displayed block workspace. A step counter and mesh metadata use `O(log(J+1))`
bits and can be bounded at the start of the run. No list indexed by elapsed
steps is retained.

The initializer has its own finite cost, before this runtime. For the tanh
polynomial core, writing `d=d1+d2`, direct Chebyshev tables and contractions
cost

\[
 O\big((Q+P)(N+1)d+Qd^2+(d_1^3+d_2^3)+Pd^2\big)          \tag{H40.I4}
\]

scalar operations, with table and square-matrix storage
`O((Q+P)((N+1)+d)+d²)`. Here `P=P1=P2` for the supplied initializer;
`Q` is the separate coefficient/Gram integration size. The generic branch
has a finite DAG with `G` nodes and `s` named sources. Its stored joint
tables/factors use `O((Q+P)(G+s+d)+s²+d²)` scalars. A direct bound for its
source differentiation, covariance, replay and normalization work is

\[
 O\big(Q[s(G+s^2)+s^2+d^2]+P(G+s^2)+d^3+Pd^2\big).      \tag{H40.I5}
\]

These costs depend on the finite dictionary and source union, including both
orientations, not on elapsed training time. Syntax/scalar resource checks
precede allocations and reject a request without substituting another
dictionary. The source regularizer is unused on the optimized core branch;
the complete generic path retains every named direction with its positive
regularizer until the stated limit removes it.

Scalar counts are not bit or wall-time bounds. In the rational backend a
retained scalar has `p` decimal places and integer units, requiring
`O(p+log(1+M_*))` bits for a finite magnitude bound `M_*` on the requested
computation. The scale `10^p` and Python integer/object storage are included
in the measured per-entry count. Basic integer/rational operation costs and
the finite rational elementary series multiply the scalar-operation work;
their temporary Fraction numerators/denominators also require storage.
C.4.7.10.C.4 gives the finite elementary construction and its convergence.
On each fixed bounded operand set its series need `O(p)` terms and may use
`O(p² log p)` temporary bits, with constants depending on that set. The
finite-horizon stage bounds of D.4 provide such a set at every fixed outer
resolution. No uniform affordable bound in order or accuracy is inferred.

If the total endpoint-description length is `b` bits, the symbolic law costs
`O(b+1)` bits plus its fixed expression tree. The collapsed branch compares
that tree with a number of bit length `O(log(p+1))`. On the resolved branch
the radius denominator alone costs `E10+1` bits. Exact midpoint coordinate
arithmetic has bit sizes bounded by a fixed multiple of
`E10+b+log(m+1)`; a deliberately loose factor sixteen is checked by the law
implementation before construction. Its finite rational arithmetic and the
storage of the `A` resulting coordinates must be added to (H40.I2)–(H40.I5).
Exact description bytes and actual rounding/collapse information accompany
the saved data. This accounts for an enormous represented law rather than
hiding its expansion cost in a real-number oracle.

At one requested time, the full initial/current pair arrays require
`2(P1+P2)A` scalars; their product weights and inputs require `O(P1+P2+A)`.
Prediction panels, exact observation serialization, and checkpoint strings
have additional finite output/transient costs. They need not be retained for
evolution. The bounded validation uses six fixed output times, independent
of the mesh, and never feeds their outputs into a later state. Its byte and
peak-RSS records distinguish state payloads, structural stage allowances,
serialized metadata, output files, elementary temporaries and process overhead.

The maintained worker `validate_observable_horizon.py` starts every declared
configuration from its prescribed Gaussian initializer and evolves through all
of its own steps to 40. At 20 it serializes its current joint state and law;
loading that state and repeating the remaining identical steps must reproduce
all retained arrays, metadata and final prediction exactly at the same backend
and reduction environment. No intermediate population state is imported, and
no approximation error is reset. Off-mesh observations use only adjacent
computed states and the affine interpolation convention, then evolution
continues from the actual right node.

The fixed bounded plan in `code/validation/observable_horizon_plan.json`
uses genuinely enriched orders `1,3,5`, whose dimensions and nonzero added
initialized-action information were proved in C.4.7.10.B. It includes supported
nonorthogonal atomic and nonatomic law descriptions, separate time,
initialization, population and input-integration refinements, rational
precision comparisons, and resolved exploratory arcs. Resource limits and
failure records are enforced by the shared supervisor; its optional worker
selection preserves the original H3 default. The analysis recomputes loss and
paired RMS from saved observations and reports all comparable declared pairs.
These finite panels and fixed observation times are diagnostics, not numerical
proofs of time-uniform or full-circle accuracy. Supported perturbations that
collapse at the declared precisions are explicitly labelled, so those runs
demonstrate operation at their resolution, not resolved perturbed-law behavior.

The full generation, independent reproduction and analysis commands are in
`code/README.md`. Their operational evidence is separate from D.1–D.4's
qualitative mathematical result and the inherited target learning bounds.
