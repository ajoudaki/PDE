# Short-time reference certificate: numerical component

Status: implemented study component, pending independent scientific review.
This does not complete C-H3. In particular it has a fixed analytical error
floor, and its executed prediction output is a positive whole-circle witness
at e1 rather than an implemented full-circle numerical field.

The original independent assessment is frozen in `H3_route_shorttime.md`.
This continuation was explicitly assigned after that freeze. The coordinator's
`H3_contract.md` was then read; its reference law, times, restart, accuracy
thresholds and resource limits govern this component. No other H3 route was
read. The coordinator later sent a matching one-dimensional contraction
derivation: it coincided with the formula already derived and implemented in
`reference_coefficients`; this agreement is a disclosed cross-check, not a
fresh independent review. Required decisive-experiments guidance was read.

## Configuration, controls and validity gates

Use the exact reference law, labels (+1,-1), equal masses, directions e1,e2,
and Y=1. Times are 0,.0025,.005, with restart from the computed b,beta
intervals at .0025. Both paired RMS null signals are zero. No canonical GF
trajectory, finite network, or training optimizer is run. This is a direct
analytical comparison of a finite initialized-observable construction with
the established canonical flow.

The scientific pass criteria remain those in the contract: a certified
whole-circle prediction-change lower bound above 1e-4; first and upper paired
RMS lower bounds above 1e-7; prediction error at most 1e-5 and each RMS error
at most 1e-7. A candidate-vs-canonical analytical error is combined with
quadrature and arithmetic interval widths. Changed resolutions are allowed
only for numerical validity, without changing these criteria.

The numerical preflight used 60 decimal digits, composite Simpson with 8192
subintervals on [0,8], symmetry for the negative half-line, and rigorous
Gaussian tail bounds. It checked every derivative-envelope entry, the .52
initial variance bound, and the analytical final-time error margins. Its
conservative runtime estimate was under one minute and RSS under 20 MiB.
The six deterministic tests took 2.13 seconds. This passes the preflight
resource and certificate-path gate; the subsequent single reference execution
was announced to the coordinator before starting it.

## Sharpened analytical bounds

All earlier identities and integral comparisons remain as in the original
report. Here only their constants are sharpened. Put

    L=4/(3sqrt(3)), sigma=sqrt(.52), T=.005,
    kappa=sigma+(10+4T^2)T^2,
    a=4 kappa+2 kappa^2 T^2,
    z=2a+2 kappa,
    c=(2/3)(1+2T)z exp(2T).

The bound `Lip(phi')<=L` follows by maximizing `2h(1-h^2)` on [0,1].
Also `q=E tanh^2G <= E min(G^2,1)=1-2varphi(1)<.52`; integration by
parts gives the equality, and the last strict inequality is checked with
outward arithmetic. For every initial input, `||H2(0,u)||2<=sqrt(q)<=sigma`.
Using the original Z bound once in the readout equation yields

    ||c(t)||2 <= 2 kappa t.

Thus integrating middle and row velocities again gives

    ||K||HS <= 2 kappa t^2,
    ||w-g||2 <= a t^2,
    sup_u ||Z2-z_u||2 <= z t^2,
    ||c-cF||2 <= c t^3.

The frozen readout obeys `||cF||2<=2 sigma t`. For its reverse query
normalized by 2t, the Gaussian standard deviation is at most sigma and the
bounded response magnitude is at most `S=1+L sigma`: the forward derivative
coefficient is at most one, and the other is bounded by
`L E|H_b|<=L sigma`. This remains true for correlated support directions.

At cutoff R=8, set d=(R-S)/sigma and

    tau^2 <= 2[(sigma^2 d+2 sigma S)varphi(d)
                    +(sigma^2+S^2)varphi(d)/d].

The upper Gaussian tail has been replaced by Mills' bound `Phi(-d)<=varphi(d)/d`.
Consequently this is an upper bound on the squared normalized query tail.
Mills' bound follows by replacing one by x/d in its positive tail integral.

The row subtraction's changed-residual term now uses `||qF||2<=4 sigma t`;
its learned-action term uses `||K||op||d2||2<=4 kappa^2t^3`. The middle
subtraction uses `||dF||2<=2 sigma t` and `||d2||2<=2 kappa t`. Thus

    Cw=(4+8 sigma T)c+(8L+16 sigma T)z+8 kappa^2+4LRa,
    CK=(2+4 sigma T)c+(4L+8 sigma T)z+4 kappa a,
    Ew(t)<=Cw t^4/4+2tau t^2,
    EK(t)<=CK t^4/4.

The known Duhamel row increment satisfies
`||dwB||4<=d0 t^2`, with `d0=2(3^(1/4)sigma+S)`. Using the exact spatial
remainder constant L/2 gives

    EZ(t)<=2Ew(t)+L d0^2 t^4+EK(t)+2 kappa a t^4,
    sup_u |f(t,u)-fF(t,u)| <= (c+2z)t^3.                    (N1)

The latter prediction estimate concerns the exact frozen-kernel observation
fF, not fB. It is an admitted, cheaper approximation for prediction alone;
the paired hidden outputs still include the nonzero nonlinear Duhamel motion.
No zero hidden motion is substituted into the paired-motion metric.
Every bound is uniform in time on the unchanged [0,T] and in the whole circle.
The interval preflight obtained

    Ew(T)<2.185161e-8,
    EK(T)<6.348280e-9,
    EZ(T)<6.472138e-8,
    sup_(t<=T,u)|f-fF|<2.416665e-6.

The lower and upper RMS measurements below require additional, explicitly
controlled spatial linearization errors, not included in EZ itself.

## One-dimensional initialized contractions

Let `h=tanh G`, `l=1-h^2`, and let `z~N(0,q)`, `H=tanh z`, `s=1-H^2`.
All expectations below are scalar one-dimensional Gaussian integrals. Define

    q=E h^2, k=E H^2,
    m=E l^2, n=E l^2 h^2,
    alpha=1-4k+3E H^4,
    gamma=(1-k)^2,
    v=E H^2s^2+kE s^2,
    V=(E l^4)(v+gamma^2q)+alpha^2 E l^4h^2.                (N2)

At the reference the two initial forward sources are independent N(0,q).
Set `U1=(H1-H2)s1`. The exact reverse source formula is

    P1=A0*U1=zeta1+alpha h1-gamma h2,
    Var(zeta1)=v.

Independence of zeta and g and oddness give `E[l1^4 P1^2]=V`.
For `J1=A0(l1^2P1)`, the forward source formula from the frozen report gives

    J1=xi+m U1,
    Var(xi)=V,
    Cov(xi,z1)=alpha n,
    Cov(xi,z2)=-gamma qm.

The source xi is correlated with z1,z2. Define

    A=alpha n/q, B=-gamma m, C=q+m.

Conditioning the joint Gaussian xi on z1,z2 gives mean `A z1+B z2` and
independent residual variance `V-q(A^2+B^2)`. Expanding
`E s1^2 [xi+C(H1-H2)s1]^2` and integrating the independent second coordinate
gives

    F=V E s^2 + A^2(E z^2s^2-qE s^2)
       +2C[A E zHs^3-B(E s^3)(E zH)]
       +C^2[E H^2s^4+kE s^4].                              (N3)

The B-squared term cancels between the conditional mean and residual variance.
The negative sign before B is essential: it arises from the -H2 part of U1.
An independent exact rational four-point product-law test checks this expansion
against the unexpanded squared conditional expression. It verifies the algebra,
not the Gaussian model by itself; that identification is the source-rule proof.

The readout state at the reference has `b1=b, b2=-b`, and its initialized upper
Gram is k times the identity. Hence

    b'=1-kb, beta'=b'b, b(0)=beta(0)=0.

The stored scalar beta is the diagonal beta of the full six-scalar candidate;
its off-diagonal entries are -beta. The exact current-state update used is

    b_new=exp(-k h)b_old+(1-exp(-k h))/k,
    beta_new=beta_old+(b_new^2-b_old^2)/2.                   (N4)

It retains the previous interval errors. The implementation performs one step
to .0025, saves its b,beta intervals, then uses those intervals for the second
step. A separate direct interval formula checks overlap with the restarted
result; this overlap is a sanity check in addition to the algebraic semigroup
identity. The formulas do not invoke any target trajectory or elapsed list.

The leading RMS outputs are `beta sqrt(V)` and `beta sqrt(F)`. Pairing is with
the same initial neuron coordinate throughout, not an independently coupled
initial marginal. Both support directions have the same squared norms, so
these are the correct training-averaged RMS values for their respective leading
increments.

For the extra spatial errors, use `||U1||2<=sqrt(1.04)`, `|U1|<=2`,
`|alpha|<=1`, and `0<=gamma<=1`. The alpha bound follows by inspecting
`(1-H^2)(1-3H^2)`, whose absolute value is at most one. Thus

    P4=3^(1/4)sqrt(1.04)+2 >= ||P1||4,
    R4=1.04+2*3^(1/4)sqrt(1.04)+2 >= ||qU1+J1||4.

For the second bound, J1's Gaussian source has variance
`E(l1^2P1)^2 <= ||P1||2^2 <=4||U1||2^2`; its response mU1 is bounded by two;
and qU1 is bounded by 1.04. The spatial tanh remainders therefore imply

    |D1_true-beta sqrt(V)| <= Ew + (L/2) beta^2 P4^2,
    |D2_true-beta sqrt(F)| <= EZ + (L/2) beta^2 R4^2.        (N5)

The moment and beta intervals are then included directly. These estimates
remain below the fixed RMS error limits when the preflight moment widths are
inserted. The retained errors are relative to the original initialization,
not reset to zero at restart.

## Outward arithmetic and quadrature proof

`H3_shorttime_solver.py` uses only Python standard-library Decimal and Fraction;
there is no dependency on mpmath, flint, scipy, or empirical quadrature differences.
Every arithmetic endpoint operation is followed by `next_minus` or `next_plus`.
Decimal exp and sqrt are correctly rounded; they are likewise widened by one
decimal ulp. Integer powers are implemented by these widened multiplications,
not by a general transcendental power function. Constants are exact decimal
rationals except pi, which is enclosed by

    pi=16 arctan(1/5)-4 arctan(1/239).

Each arctangent uses 64 exact rational alternating-series terms plus the next
term as a rigorous remainder. The identity follows from the tangent addition
formula and the signs/ranges of the two angles. Input q is an interval; its
square root and every upper Gaussian moment propagate this interval directly.
No covariance eigenvalue inversion occurs. The sole division by q is gated
by its certified positive lower bound; the kernel k is likewise positive before
the current-state update divides by it.

For a moment `E[z^a P(tanh z)]`, `z=sigma x`, the integrated function on the
standard Gaussian line is

    rho(x) sigma^a x^a P(tanh(sigma x)), a in {0,1,2}.

If Q is its polynomial factor in (x,h,sigma), differentiating it together with
rho applies the exact polynomial rule

    Q -> partial_x Q+sigma(1-h^2)partial_h Q-xQ.

Four exact integer-coefficient applications are used. With `0<=sigma<=1` and
`|h|<=1`, each monomial x^j rho(x) is bounded by the table
`(1,1,1,1,1,2,5)` for j=0,...,6. These bounds are verified in outward arithmetic
from its maximum at sqrt(j), or at zero for j=0. The sum of absolute polynomial
coefficients times these bounds is a rigorous supremum for the fourth
derivative. The largest value among used moments is 788640.

For completeness, the Simpson bound used requires no unverified numerical
library theorem. On [-h,h], its fourth-order Peano kernel, normalized to h=1,
is

    K(v)=(1-v)^4/24-[(1-v)^3+4(-v)_+^3]/18,
    -1<=v<=1.

For v>=0 it is `-(1-v)^3(1+3v)/72`; it is even on the negative half.
It is nonpositive and its absolute integral is 1/90. Applying the scalar
fourth-order integral remainder, with Simpson annihilating all cubic terms,
therefore bounds a panel error by `h^5 sup|f''''|/90`. Summing N/2 panels on
[0,R] and doubling for the even full-line integrand yields

    error <= R^5 sup|f''''|/(90 N^4).

The standard Gaussian tails, with `|P(tanh z)|<=1` for all the particular
nonnegative factored integrands used, are bounded by

    2rho(R)/R                        (a=0),
    2rho(R)                          (a=1),
    2rho(R)(R+1/R)                   (a=2).

These follow from Mills' inequality and one integration by parts. Since
sigma<=1, they also bound z^a. The tails add [0,bound]; quadrature remainder
adds a symmetric interval. Every Simpson weight is nonnegative, so interval
summation directly propagates all evaluation and initial-q uncertainties.
Roundoff is already included at each operation, rather than added as an
unverified last-digit tolerance.

At R=8,N=8192, the largest Simpson bound is below 6.376e-8 for an individual
initialized moment. Its effect on RMS is much smaller because the RMS output
is multiplied by beta, approximately T^2/2. The Gaussian tail bounds are below
1e-12. The implementation records the complete individual error budgets.

## Prediction scope and remaining implementation gap

At the reference, for every normalized input u, the exact cheap observation is

    fF(t,u)=b(t)[K(u,e1)-K(u,e2)],
    K(u,v)=E2[tanh(A0 tanh(g dot u)) tanh(A0 tanh(g dot v))].

Its kernel is an initialization-only two-dimensional Gaussian integral whose
covariance is itself a two-dimensional Gaussian expectation. This specifies
an effective numerical observation map with explicit smooth integrands, but
the current executable does not implement that map at arbitrary u. It evaluates
`fF(t,e1)=b(t)k` and records the uniform analytical bound (N1). The latter and
this positive witness give an enclosing whole-circle signal interval with
lower endpoint from e1 and upper endpoint 2t. It proves that the named
whole-circle signal is positive with the prescribed margin, without claiming
an accurate numerical maximum or a delivered full-circle function.

A future full-circle implementation must control its additional kernel
quadrature and coefficient errors uniformly; the present executable's
`prediction_total` includes only the e1 coefficient interval. It must not be
reported as a numerical full-circle approximation certificate. The exact
canonical-vs-fF analytical bound is uniform, but this distinction matters for
the complete C-H3 objective.

The fixed analytical error floor, the absent arbitrary-epsilon refinement,
the representation and numerical membership of a fixed nonorthogonal/nonatomic
family, and general admissible observation graphs remain outside this component.
The coordinator owns their synthesis and the H2 extension.

## Reproduction and execution record

From `/home/amir/Codes/PDE`:

```
python studies/observable_hierarchy/H3_shorttime_test.py
python studies/observable_hierarchy/H3_shorttime_solver.py --preflight --output data/generated/observable_hierarchy/H3_shorttime_preflight_FRESH/result.json
python studies/observable_hierarchy/H3_shorttime_solver.py --run --output data/generated/observable_hierarchy/H3_shorttime_reference_FRESH/result.json
```

Fresh output paths are required; existing results are never overwritten.
The result records Python/platform, 60-digit precision, source SHA256, Gaussian
moment intervals, individual quadrature/tail bounds, initialization/evolution
runtime, peak RSS, current-state restart intervals, analytical errors, actual
observable enclosures, and the limited demonstration verdict.

Initial preflight: `data/generated/observable_hierarchy/H3_shorttime_preflight_20260912/`.
After replacing general integer powers by only rounded interval multiplications:
`data/generated/observable_hierarchy/H3_shorttime_preflight_20260912_v2/`.
Both preflights are preserved; the first is superseded for the current source.
First authorized reference execution:
`data/generated/observable_hierarchy/H3_shorttime_reference_20260912/`.
The completed result values and runtime are appended below after execution.

### Completed first execution

Exit status zero; the limited reference-component thresholds passed. Runtime
was 6.279923 seconds, of which 0.002236 seconds was coefficient evolution and
output enclosure; peak RSS was 17,536 KiB. Python was 3.10.12 on Linux x86_64.
The exact serialized final-time enclosures are in the result JSON. Rounded
outwards for this record:

| Quantity | Certified true enclosure or error |
|---|---:|
| First paired RMS at .0025 | [1.1231885e-6, 1.1260042e-6] |
| Upper paired RMS at .0025 | [1.6654131e-6, 1.6737500e-6] |
| First paired RMS at .005 | [4.4732053e-6, 4.5182496e-6] |
| Upper paired RMS at .005 | [6.6076920e-6, 6.7410684e-6] |
| First RMS total absolute error at .005 | <2.252213e-8 |
| Upper RMS total absolute error at .005 | <6.668817e-8 |
| Prediction at e1 at .005 | [.0011791368, .0011839702] |
| Whole-circle prediction-signal lower bound | >.0011791368 |
| Analytical whole-circle prediction error | <2.416665e-6 |

At zero, every true signal is zero and the intervals include zero. The tiny
signed Decimal endpoints there are outward rounding artifacts, not a claimed
nonzero signal. The restart computation consumed the saved b,beta intervals
and its final enclosures overlapped the direct formula's enclosures.

Retained hashes:

```
H3_route_shorttime.md d0311b28d98ed93d2cab56b6240ab9813b53820675435e6f9590dced924c0fea
H3_shorttime_solver.py b266d3ae2716c8bad1575f6367bc56c0f5828eaa9d786660958b543f487cbdc0
H3_shorttime_test.py 67902e0dca71c04f3e1654081be4cc704b985d5713eb238079110cfbf4a7f903
H3_shorttime_reference_20260912/result.json 7ffb8100cc824d6bd7a91678d34642a170b387c7a464487592a5746283508a23
```

The six tests passed with actual command
`python studies/observable_hierarchy/H3_shorttime_test.py`, exit zero, 2.126
seconds. They cover exact-rational interval arithmetic, a rational-series
oracle for exp, pi enclosure and tanh symmetry, zero-variance Gaussian
quadrature, the independent rational four-point contraction oracle, and
symbolic fourth-derivative bookkeeping. The installed Decimal docstrings
were inspected and explicitly state correct ROUND_HALF_EVEN rounding for exp
and sqrt; the code widens their outputs. No external scientific result or
uncertified scipy integration is imported.

This is internally executed evidence pending a fresh complete independent
proof/code review. It is not a promoted result or a claim that the full
H3_contract has passed.

### Numerical-validity correction and second execution

The coordinator identified two numerical semantics that required correction
before freezing for review. In the first source, the final reported total-error
sums were computed with nearest Decimal arithmetic rather than explicitly
rounded upwards, despite their component intervals being outward. Also the
midpoint restart passed the saved state in memory, without a write/reload cycle.
The source matching that first result was preserved as
`H3_shorttime_solver_v1.py`, hash
`b266d3ae2716c8bad1575f6367bc56c0f5828eaa9d786660958b543f487cbdc0`.
The first result is not overwritten. Its printed total-error endpoints and
its lack of disk-reload evidence are superseded by the corrected source and
second result; the scientific model, bounds, configuration and thresholds did
not change.

Current total-error sums and interval widths are evaluated in the outward I
arithmetic, and their upper endpoints are serialized as the error bounds.
The reusable checkpoint functions encode/decode exact decimal b,beta and all
coefficient endpoints, an exact rational elapsed time, the fixed horizon,
working precision, and the original canonical initialization as the analytical
certificate origin. Nonfinite/reversed intervals, missing coefficients, wrong
precision/certificate origin, and out-of-horizon elapsed times are rejected.
Saving refuses to overwrite an existing checkpoint.

The elapsed rational time is numerical certificate bookkeeping. It only chooses
the cumulative analytical error bound, and enforces its horizon; it does not
enter the b,beta vector field or grow into an elapsed-history list. The prior
interval widths carry all accumulated initialization and arithmetic uncertainty.
No analytical error is reset at the midpoint. On the repaired run the driver
actually writes `midpoint_checkpoint.json`, reads it back, and advances its
reloaded b,beta,coefficients and elapsed certificate time. Final output records
the checkpoint hash and the exact reloaded intervals.

The expanded nine deterministic tests passed with exit zero in 2.067 seconds.
New checks cover exact roundtrip of nonzero interval widths, invalid/reversed
and nonfinite state rejection, preservation of original certificate origin,
overwrite rejection, and a resumed-vs-direct interval sanity check with prior
coefficient uncertainty. The unchanged analytical preflight was rerun at
`data/generated/observable_hierarchy/H3_shorttime_preflight_20260912_v3/`.
The second and final coordinator execution authorized for numerical validity
uses `data/generated/observable_hierarchy/H3_shorttime_reference_v2_20260912/`.

The repaired execution exited zero and passed the unchanged limited component
criteria in 6.169790 seconds, with 17,836 KiB peak RSS. Its coefficient evolution,
checkpoint write/reload, and final enclosures took 0.002975 seconds. Total
outward-rounded errors remain below 2.252213e-8 (first RMS), 6.668817e-8 (upper
RMS), and 2.416667e-6 (the e1 prediction output including its numerical width).
The rounded true-observable enclosures in the preceding table remain valid.
Reloaded elapsed certificate time is exactly 1/400; its b interval is
[.00249926123544752140394, .00249926124063547944091], rounded outwards here,
so preexisting uncertainty was actually preserved.

Frozen repaired-source/result hashes:

```
H3_shorttime_solver.py cf3b479826c8900bc4097d023128330c380df415d83b2a782054c5e565542e6b
H3_shorttime_test.py 11dd36c0d7ead265ddc3bfc20f7d5b688d1f6dacac7cfe8b7b652468c81eedb5
H3_shorttime_reference_v2_20260912/result.json 65fc312d561c19b7c61bf7c06c086a332e82a4a17032c7591c8820b453e13718
H3_shorttime_reference_v2_20260912/midpoint_checkpoint.json b259269d531197a0feb466c68e4a90459f86cf0763079619def1f7deee622e17
```

Both coordinator executions are now consumed; no further reference execution
is undertaken here. Independent reproductions remain governed by the root
contract. The repaired producer and this complete note are ready for fresh
complete isolated review, with all earlier limitations retained.
