# Residual-route implementation feasibility

Bounded follow-up, 2026-09-12. No trajectory or Git mutation. The original
`H3_route_residual.md` remains frozen and unchanged.

The existing prototype can execute the necessary **static finite Gaussian
expressions**, including both action directions, at modest low-order cost. It
cannot yet certify a learned-field residual: its learned arrays lack a declared
off-node function and derivatives, and its Gaussian quadrature and covariance
algebra have no outward error bounds. More sharply, the literal float64 H2
dictionary cannot reach its next relevant upper-population source before its
hard ridge ceiling. The uniform-residual scalar certificate in the frozen route
therefore cannot meet the paired-RMS tolerance with that literal implementation.
These are specific implementation/witness conclusions, not an impossibility
claim for C-H3.

The required effective family **inside the H2 neighborhood** is also not yet
specified by a proved numerical radius. The optional all-law short-time
extension in the frozen route does not establish that inclusion and is not used
to claim contract completion here.

## Scope, provenance, and completed preflight

New scientific inputs read completely were `H3_contract.md`,
`H2_prototype_v3.py` (697 lines), `H2_test_prototype_v3.py` (312 lines), and
`H2_prototype_notes_v3.md` (279 lines). Earlier allowed H2 v3 and established
dependency sources remain as recorded in the frozen report. No other route
report was read. The contract's coordination disclosure about another route
was visible; no scientific result was obtained from that route.

The unchanged instruction hashes were checked; current HEAD at startup was
`431deb3ca9b881abaffd57da5562a07e5406f273`. No staged paths were reported.
The required decisive-experiments reference was read before the deterministic
preflight. The plan and stop conditions are in `H3_residual_budget.py`'s module
docstring, written before execution.

Command, from repository root:

```
env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python -B studies/observable_hierarchy/H3_residual_budget.py
```

Fresh output:
`data/generated/observable_hierarchy/H3_residual_preflight_20260912T181758Z_2/results.json`.
The JSON retains source hashes, configuration, Python/NumPy/platform versions,
thread settings, all source diagnostics, conditioning, and sizes. The run
completed with exit status zero. Timed initialization/evaluation work, excluding
imports, used 0.298413362 CPU seconds and 0.303384017 wall seconds; the execution
tool reported 0.339179553 seconds for the complete command. Peak RSS was
144788 KiB (141.39 MiB). The process had an 85-second CPU
limit and 2-GiB address-space limit, below the assigned 90-core-second / 8-GiB
preflight allowance. No further numerical run was performed.

The run only initialized N=1 at Gaussian orders 5,7,9, appended the initialized
queries A0 tanh(g1), A0 tanh(g2), and then queried both reverse fields for the
synthetic **static** readout

    chat=.01[tanh(A0 tanh(g1))-tanh(A0 tanh(g2))], w=g, K=0.

No update or integration time was assigned to this synthetic state. It tests
finite-expression compilation, not approximation to any training state.

## 1. Exactly what can be reused

| Operation needed by residual certificate | Existing support | Missing bridge |
|---|---|---|
| Typed finite initial expression and frozen named derivatives | `Word`, `GaussianProgram` implement these | Add explicit represented current-field expressions and their bounded derivative envelopes |
| Correct A0 and A0* responses on finite expressions | Implemented and static analytic tests inspect nonzero adjoint response | Outward covariance, expectation, and response-coefficient error propagation |
| H2 finite coefficient action and its transpose | `apply_action`, `fields`, `rhs` | Distinguish these B_N+K_N calculations from original A0+Khat certification queries |
| Current population values and scalar contractions | Implemented on tensor GH nodes | A proved continuous off-node reconstruction and population-integration error |
| HS norm of a finite rank residual | Can assemble from existing weighted pairings | Joint Gaussian integrations with intervals; finite sums alone are not certified |
| Soft tail j_R(Q) | Formula can be evaluated on any returned finite expression | Certified Gaussian-tail and integration remainder; zero sampled tail is not zero population tail |
| Full-time/full-circle suprema | None | Validated time interpolant, effective angular modulus/subdivision, outward extrema |
| Finite scalar cutoff-menu barrier | Not implemented | Small separate validated one-dimensional piecewise-affine solver |
| Restart | Current quadrature state is saved | Save represented-field coefficients, fixed source provenance, precision, and accumulated certificate budget |
| Nonatomic law integration | Numerical API accepts only finite `DataLaw` | Effective arc/other-law approximation plus proved input integration errors |

The prototype's `_visit` explicitly rejects `w1,w2,c` in initialized programs.
That is correct: arbitrary learned arrays do not define Gaussian input
expressions. If current fields are declared, for example, as finite rational
polynomials in bounded initialized marks plus g, they can be expanded into
existing rational scale/add/multiply/tanh instructions or a checked extension
of that alphabet. Numerical coefficients are fixed parameters when computing
named-source derivatives. This uses no target action oracle. It changes the
representation layer; merely relabeling the present arrays does not suffice.

Off-node ambiguity is substantive. For any finite set of one-dimensional
quadrature abscissas x_j, the bounded smooth function

    V(x)=P(x)^2/(1+P(x)^2),  P(x)=product_j(x-x_j),

is zero at every abscissa, with zero first derivative there, but has positive
Gaussian L2 norm. Its derivative is bounded because it is continuous and
tends to zero at infinity. Thus even values and first derivatives at all
quadrature points cannot distinguish it from zero. The Gaussian input variance
for an A0 query would differ. A representation and remainder theorem resolve
this ambiguity; quadrature arrays alone do not.

The existing Gaussian algebra is also not a validated version of the frozen
route's procedure. It uses float64 QR/range solves and changes a sufficiently
small *negative* Schur complement to zero, recording the correction. This is
a documented diagnostic convention, not an enclosure of the exact covariance.
The singularity-safe positive-square-root polynomial construction in the frozen
route remains an implementation obligation.

## 2. Static dimensions, conditioning, and measured cost

All values in this subsection are floating diagnostics, except integer counts
and storage arithmetic.

| GH order | N=1 population nodes | Initialization CPU s | State array bytes | Regularized Gram condition numbers |
|---:|---:|---:|---:|---:|
| 5 | 625 / 3125 | .010400174 | 205384 | 5 / 5 |
| 7 | 2401 / 16807 | .023333364 | 1018408 | 5 / 5 |
| 9 | 6561 / 59049 | .066976513 | 3412104 | 5 / 5 |

The retained feature dimensions are 6 and 4. Materialized Gaussian dimensions
are 4 and 5; named source counts are 2 and 5. The reverse-source covariance
condition is approximately 1; the forward-source covariance condition ranges
from 9.585 to 9.763. No negative-Schur correction occurred in these runs.
The raw feature Grams are singular by intentional repeated constant columns;
the condition-five result concerns the ridge-regularized Grams.

For the analytic control E sin(G)^2=(1-exp(-2))/2, the GH5/7/9 errors were
-0.00665334085, -0.000183473293, and -0.00000285202862. These known errors
show why the timings do not establish target accuracy. Resolution differences
are not used as an error bound.

Appending both true initial tanh forward queries raised dimensions to 4 / 7.
The two synthetic reverse queries raised them to 6 / 7, with 15625 / 78125
GH5 nodes. The complete static extension took .193478839 CPU seconds. The
calculated initial canonical readout-velocity norm was .665836790 and its
difference from the compressed N=1 readout velocity was .485082085. These
numbers are **not** rigorous population lower bounds.

The sampled soft tails at R=.1 and R=1 were zero, although the appended
reverse sources had strictly positive reported innovation variances near
2.6e-6 and 2.4e-6. A nondegenerate Gaussian innovation plus bounded response
terms has positive population tail at every finite threshold. In this setup,
zero quadrature tail is therefore precisely a missing-tail diagnostic, not a
valid certificate.

For fixed dimension d and GH order q, tensor node count is q^d. In the full
upper certification union just tested, d=7 with seven source coordinates.
Its carrier alone stores at least 15 float64 numbers per node: seven
independent coordinates, seven named Gaussian coordinates, and one weight.
Thus its carrier storage is at least 120 q^7 bytes. At q=15 this is
20,503,125,000 bytes (19.10 GiB), exceeding the entire 8-GiB contract before
field/gradient caches or time state. At q=11 the carrier already needs
2,338,460,520 bytes; one cached value plus seven derivatives adds
1,247,178,944 bytes. The compiler computes derivative arrays even for a
value-only public call. This is a definite storage limit for this materialized
tensor implementation, not a proof that q=15 is necessary for accuracy.

The frozen route's naive Bernstein mark box at N=1 has first-population
dimension d1+2=8. Degree 10 in each coordinate means 11^8=214358881
coefficients per row component: two float64 row components already use
3,429,742,096 bytes, before integration stages and certification buffers.
Degree 20 would use more than 600 GB for those two components. Thus the
literal full rectangular box is unsuitable for even modest degree under the
8-GiB cap. This is avoidable by exploiting the actual initial source dependence,
as described below; no degree sufficient for the target has been proved.

The most elementary uniform-cell integration bound is also computationally
unusable at these tolerances. For a Lipschitz integrand on [-H,H]^d, partition
cells of side h and use error <=L sqrt(d) h: a sufficient cell count is
(2H L sqrt(d)/delta)^d to achieve integral error delta. Already d=4,H=8,L=1,
delta=1e-7 gives approximately 1.05e34 cells. A near-zero norm enclosure may
need a squared-integral error on the scale 1e-14, worsening this sufficient
bound. These are costs of that elementary certificate, not lower bounds on
all quadrature algorithms. A useful implementation needs substantially sharper
validated quadrature, analytic reductions, or local polynomial remainders.

## 3. Exact source reduction for the smallest dictionary

This reduction is available directly from the pilot and actual adjunction;
it does not modify the initialized law or drop positive covariance modes.

Write

    v=E sin(G)^2, alpha=exp(-v/2), s=(1-exp(-2v))/2,
    xi_i~N(0,v), R_i~N(0,s),
    p_i=R_i+alpha sin(g_i), t_i=tanh(p_i).

The (g_i,R_i) pairs are independent between axes, and xi_1,xi_2 are independent.
N=1's first dictionary is made from 1,sin(g1),sin(g2),t1,t2,1. Its joint law
with g therefore depends on four independent Gaussian coordinates. The upper
dictionary is sin(xi1),sin(xi2),1,1 and depends on only two. Ridge normalization
is a deterministic linear transformation and adds no coordinate dependence.

The extra three upper dimensions materialized by `initialize` are used to form
D, not by the upper population marks. They need not remain in a compressed
upper quadrature population. For a raw upper feature sin(xi_i) and any raw
first feature psi_j, actual adjunction gives

    E2[sin(xi_i) A0 psi_j]=E1[p_i psi_j].

For a constant upper feature, the contraction is zero: the direct forward
source is centered and its response corrections have factors sin(xi_i) with
zero mean. All nonzero Gram/contraction entries therefore reduce to one- or
two-dimensional integrals of (g_i,R_i); off-axis entries factor by independence.
Keep the duplicate features and perform the exact same ridge normalization
after these contractions. This computes the same N=1 dictionary and D.

A source-based represented first field can then use the four frozen source
coordinates, and the upper field the two xi coordinates, while retaining the
H2 marks as fixed functions of those coordinates. This counts all marks and
does not reconstruct a trajectory. At degree 20, the two first-field Bernstein
coefficient arrays on four coordinates need only 3,111,696 float64 bytes.
One must explicitly allow and save these finite initialized source coordinates
and keep their source covariance/response provenance. The current API does not
yet implement this representation.

Certification should also compile minimal required finite unions. The full
seven-dimensional upper union used in the preflight is often unnecessary:
one observation/atom at a time, with triangle bounds where valid, reduces
joint requirements. For a joint or squared contraction, however, all operands
in that contraction must stay jointly coupled; independent source resampling
would change the result. These reductions improve feasibility but do not repair
the literal dictionary limitation in the next section.

## 4. Exact limitation of the literal float64 dictionary

The following claims follow from the explicit code grammar and input checks;
they are not inferred from the floating defect .485.

The first Gaussian seed g1 has code 2. The smallest bounded lower word depending
on a first Gaussian seed is sin(g1), with code 4+8*2=20. An action has code
7+8k, so A0 sin(g1) has code 167. An L expression becomes bounded only after a
sin/cos/tanh instruction; affine nodes and bounded products cannot turn an L
operand into a B result. Hence the first bounded upper word with g dependence
has code

    sin(A0 sin(g1)): 4+8*167=1340.

Rational scaling, affine combinations, and products cannot lower this minimum:
their dependencies have smaller codes and retain the stated sort. The analogous
exact active upper tanh feature is

    tanh(g1):22, A0 tanh(g1):183, tanh(A0 tanh(g1)):1470.

For g2 the corresponding codes are 30,247,1982. These are codes of those
particular expressions, not a general lower bound for every useful alternative
dictionary.

The pilot bypasses the enumeration by retaining sin(xi1),sin(xi2) at N=1.
Before code 1340, all *additional* bounded upper words are g-free. They depend
only on the one forward Gaussian chi=A0 1 and deterministic constants. To
verify the latter point, the earliest reverse query A0*1 has code 15, its first
bounded gate has code 124, the next forward query has code 999, and a bounded
gate of that returned field cannot occur before 7996. Thus a g-free forward/
reverse loop cannot create a new bounded upper feature before 1074 either.
Distinct actions of deterministic constants are scalar multiples of chi.

Consequently, for every literal hierarchy order 1<=N<=1074, the upper retained
feature sigma-field is contained in

    S=sigma(xi1,xi2,chi),
    xi_i=A0 sin(g_i), chi=A0 1.                    (F1)

The initializer may compute many other Gaussian sources when forming D from
lower features. Those computations do not put the sources into the retained
upper features; D consists of deterministic scalar contractions.

`initialize` rejects N>1074 before compilation; `ridge_features` also rejects
an underflowed eta=2^(-N). Float64 cannot represent that positive ridge beyond
1074. Therefore (F1) covers every order that this particular float64 API can
accept. Long before that hard ceiling, duplicate constants give the exact
regularized-Gram condition lower bound

    cond(G+2^(-N)I)>=1+2^(N+1),

because G has a null eigenvector and a largest eigenvalue at least 2 from two
identical constant columns. This does not prove the exact first rejection
order of a floating eigensolver, but identifies the precision burden.

### A rigorous floor for the frozen route's uniform-residual certificate

At the reference initialization, canonical c'=tanh(Z1)-tanh(Z2), where
Z_i=A0 tanh(g_i). The H2 c'_N is S-measurable by (F1), for every supported N.
Let h=tanh(G), v=E sin(G)^2, q=E h^2, a=E[h sin(G)], b=a/v and
sigma^2=q-a^2/v. The initial forward source rule gives independent axis pairs

    Z_i=b xi_i+sigma E_i,

with E_i independent standard normals independent of S. Covariance with chi
vanishes by oddness. These identities use the same action's joint source Gram.

Here is a deliberately crude explicit lower bound, needing no numerical
quadrature. We have q<=1, v>1/4, and |b|<2 by Cauchy–Schwarz. On
G in [3,31/10], tanh(G)>99/100 and |sin(G)|<1/4; the latter follows from
sin(3)<3/20 and the unit Lipschitz bound over an interval of length 1/10.
Therefore |h-b sin(G)|>49/100 there. The Gaussian density on this interval
exceeds 1/450: sqrt(2 pi)<3 and exp(5)<150, while (31/10)^2/2<5. Thus

    sigma^2=E(h-b sin(G))^2 >2401/45000000.         (F2)

The elementary constants can be checked with alternating sine series and
positive exponential series: exp(6)>199 gives tanh(3)>.99, and
sum_(n=0)^10 5^n/n!+(12/7)5^11/11!<150 bounds exp(5). No quadrature estimate
is used in (F2).

Conditional one-dimensional Gaussian integration by parts and Cauchy–Schwarz
give

    Var(tanh(Z_i)|xi_i)>=sigma^2 [E(sech^2(Z_i)|xi_i)]^2.

Indeed E[E_i tanh(b xi_i+sigma E_i)|xi_i]=sigma E[sech^2(Z_i)|xi_i],
and the conditional variance dominates the squared covariance with E_i.
Since E Z_i^2=q<=1, P(|Z_i|<=2)>=3/4. Since cosh(2)<4,
E sech^2(Z_i)>3/64. Jensen and independence of the two conditional innovations
therefore imply, for every S-measurable V,

    ||tanh(Z1)-tanh(Z2)-V||_2^2
      >=2 sigma^2 (3/64)^2 >1/6250000.

In particular the exact canonical source defect at zero obeys

    beta_N(0)>1/2500.                             (F3)

For the frozen route's single uniform bound b_res>=sup_t beta_N(t), its
barrier has z'>=b_res. Consequently

    z(1/200)>1/500000=2e-6.                       (F4)

The first hidden field is initialized exactly, and the frozen report's generic
paired-RMS bound uses z(T) for its final L2 row error. It therefore cannot
produce a <=1e-7 paired-RMS error certificate through that bound for the
literal exact H2 orders supported by this float64 dictionary. Arbitrarily
accurate Gaussian quadrature cannot remove (F3).

This conclusion is deliberately limited. It does not lower-bound the actual
paired-RMS error by 2e-6; (F4) lower-bounds this **upper certificate**. It does
not reject more refined componentwise or time-local residual barriers, a
different finite dictionary, arbitrary-precision access to larger H2 orders,
or other finite autonomous representations. It is a precise obstruction to
combining the present dictionary/API ceiling with the frozen certificate as-is.

## 5. Required effective law family inside H2's actual neighborhood

H2 fixes rho=delta/2 with

    delta=min(delta_Y/4,delta_act,Y,1/4).

The read sources assert positive witnesses for delta_Y and delta_act,Y but
do not specify numerical values or effective lower bounds for those fixed
witnesses. Showing a separate short-time all-law theorem does not prove that
any particular nonzero law perturbation is smaller than this rho. This report
does not make that substitution.

A completely effective family becomes available **if** one supplies a positive
rational r together with a proof r<rho. For computable parameters
|alpha|,|beta|<=r/4 and 0<=h<=r/4, take equal masses with labels +1,-1 and
normalized input angles

    alpha+h s,  pi/2-beta+h s,    s uniform on [-1,1]. (F5)

For h=0 this includes rotated, generally nonorthogonal two-atom laws; for h>0
the law is nonatomic. Couple each arc to its reference center. Since chord
distance is at most angular distance and E|s|=1/2,

    W1(mu_(alpha,beta,h),nu*)
      <=(|alpha|+|beta|)/2+h/2<=3r/8<rho.          (F6)

There is an explicit input-integral interface: n midpoint cells on each arc
give a finite law at W1 distance at most h/n (even h/(2n) follows from the
same coupling). Elementary sin/cos evaluation with certified error preserves
this bound after adding the input-coordinate rounding error. Thus nonatomic
integration is not the missing part of (F5); the unprovided r<rho is.

Exactly which moduli are missing from the selected sources:

1. For delta_Y, C.4.7.3 chooses a long-time neighborhood from a strict bound of
   the form C_B exp(C_B T)(Phi_(B*)(q)+q)^(1/16)<=1/2. Its proof uses several
   generic finite C_B and a reference/mesh modulus. The selected text does
   not instantiate all these constants into a computable positive lower
   bound for the particular delta_Y used in H2.
2. For delta_act,Y, H1 part 8 chooses a common t_a from initialized expansions
   J_l(nu*,t)=b_l^2 t^4+o(t^4), positivity of nonaffinity, and continuity. To
   extract a radius one needs an effective remainder modulus selecting a
   concrete t_a and positive lower margins there, followed by an effective
   law-continuity modulus for both paired displacements and nonaffinity.
   The latter also needs a positive variance lower bound for its denominator.
3. The theorem statements permit further shrinking their neighborhood
   witnesses. A constructive re-extraction must identify a chosen valid witness
   and its relationship to the H2 radius, not claim that an arbitrary unnamed
   positive witness exceeds a proposed rational number.

All the underlying displayed finite-program integrals and elementary estimates
may make such an extraction possible. This bounded task has not completed that
large constant/remainder reconstruction and has no proved positive numerical
radius to report. The simple logical premise rho>0 alone provides existence of
some rational r<rho; it does not supply a reproducible value or a stopping test
that finds one. Contract rung 1 therefore remains open for this implementation.

## 6. Concrete next implementation decision

Do not launch a literal H2-v3 trajectory expecting the frozen scalar certificate
to meet the demo thresholds. First choose and audit a finite dictionary that
resolves the reference initialized tanh sources, or provide arbitrary precision
and a feasible larger-order strategy; (F3) is an analytic check of why this
decision matters. Reuse the correct named-source and transpose logic, but add
explicit represented fields and a genuine outward source-integration backend.
Use the exact pilot source reduction to avoid unnecessary tensor dimensions.

In parallel, contract completion requires a separate effective extraction of
the two radius moduli above, or a user-approved reformulation of the family
contract. The short-time extension alone cannot be presented as inclusion in
the original H2 ball.

The preflight establishes that low-order source expression evaluation is cheap;
it establishes neither required precision nor a certified runtime. A candidate
whose new source enclosures, whole-circle propagation, and chosen dictionary
avoid (F3) can be assessed anew without treating the present witness failure as
a general obstruction to useful C-H3 computation.
