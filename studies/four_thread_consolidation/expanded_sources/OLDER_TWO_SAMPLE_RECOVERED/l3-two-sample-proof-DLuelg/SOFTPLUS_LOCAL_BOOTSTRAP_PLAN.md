# Root working plan: restore a local theorem for shifted softplus

UNVERIFIED proof architecture, not a theorem or a transferred old result.
2026-09-06. Fixed phi=1+0.1 softplus, no changes to the canonical model.
This file preserves the next critical-path calculation across context.

The loss of a uniform feature ceiling need not invalidate a local
Gaussian-response construction. Proposed replacement: linear growth plus
Gaussian source chaining, with THREE analytical reference cuts (both
reverse queries and readout only where it enters delta3). Readout update
remains the exact feature average/difference. These cuts are proof
references, not a proposed optimizer. All details below need a proof.

1. Reference finite dynamics: delta3=tau_Rw(w) phi'(z3), usual two
   back-query cuts, otherwise the raw feature Euler equations. At fixed
   caps the field is locally L2-Lipschitz on bounded primal sets. Features
   have linear growth and bounded gates; every troublesome old factor in
   a gate difference is capped. Bound the initial operator norms and
   all RMS primal quantities in a fixed box on a sufficiently small
   deterministic interval, independently of all caps/width. This follows
   from a finite polynomial differential/discrete comparison, since
   |tau(x)|<=|x|. Readout RMS and both back deltas/queries are O(s).
   Do not presume a global clipped theorem or a gradient energy identity.

2. Derive the exact finite Gaussian scalar law including tau_Rw. The
   usual A/B definitions and four independent source groups still apply
   to this changed finite program; formal derivatives include tau_Rw'.
   Prove the fixed-program identification using the already audited
   elementary Gaussian conditioning method, not an unstated theorem for
   nonlinear unbounded tests. Linear growth + Gaussian finite moments
   should permit the existing truncation/projection argument.

3. Bootstrap total backward coefficient rows B2,B3<=1 and separate
   forward coefficient constants |A2|<=C2 Delta, |A3|<=C3 Delta.
   The primal RMS bounds give cap-independent pointwise source variances.
   Forward physical identities give L2 time-Lipschitz H1,H2 even before
   a response bound: bottom velocity uses bounded gates, bounded ops and
   RMS back deltas. Hence the forward Gaussian sources xi2,xi3 have
   uniformly Lipschitz covariance metric.

4. Supply an ELEMENTARY finite Gaussian chaining lemma: centered finite
   linearly interpolated Gaussian arrays with bounded initial variance
   and L2-increment metric <=D|t-u| have a mesh-uniform sub-Gaussian
   supremum. Use dyadic nets, Gaussian union bounds at each level with
   thresholds proportional to (u+sqrt(j+1))2^(-j), and sum the levels.
   Both samples cost a fixed factor; within-source independence is not
   needed. This is stronger than the L2-only chaining in R23 and must be
   fully proved. No specialized concentration theorem need be invoked.

5. Pointwise linear-growth recursions under the coefficient bootstrap:
   - Bottom |Z1| is bounded by initial |G| plus integrals of |zeta1|,
     a constant, and a linear Volterra term in max_past|Z1|.
   - Middle |Z2_k|<=|xi2_k|+C2 Delta sum_past e|q2|, and
     |q2_k|<=|zeta2_k|+B3(a0+e max_past|Z2|), a0=1+e log2.
     Discrete Gronwall bounds sup|Z2| by sup|xi2|, a constant, and
     integral|zeta2|. A supremum estimate for zeta2 is NOT needed.
   - Top |Z3|<=|xi3|+C3 Delta sum e|w|, and
     |w_k|<=s(a0+e max_past|Z3|). A Volterra bound makes sup|Z3|
     Gaussian-controlled by sup|xi3|, and w/s has a Gaussian envelope.
   Gaussian marginal variance plus time Jensen controls the exponential
   moments of integral|zeta_j|, without source path continuity or a
   mesh-dependent maximum. This gives all feature sup moments and all
   individual-time q1,q2 Gaussian envelopes under the coefficient bootstrap.

6. Re-run the response induction with these envelopes, not bounded
   features. Single bottom source injection has size C e^2 Delta, times
   exp(C integral(|q1|+B2)). Its expectation is bounded for sufficiently
   small S, so A2 <= Delta(G1_bound+C e^2). The analogous middle injection
   gives A3 <= Delta(G2_bound+C e^2 C2). Choose C2,C3 first from fixed
   primal bounds; then choose S small. No self-defining constant loop.
   Forward middle total derivatives have L2 (indeed all fixed-p) bound
   via exp(C C2 integral(|q2|+B3)).

7. Top full delta derivative includes BOTH readout and gate terms:
   T3 <= e Dw_row+c|w| DZ3_row (tau derivatives at most one).
   Top Volterra closure gives schematically
   T3_sup<=S(e^2+c K3) exp(C C3 S^2(e^2+c K3)),
   with K3 Gaussian-controlled from step 5. Thus E T3=O(S).
   Learned transpose rows are O(S^3). Prove CURRENT B3=O(S) first.
   Then CURRENT B2 is bounded by
   E[(c|q2|+e^2 B3) P2]+learned term =O(S),
   using primal ||q2||2=O(S) and bounded ||P2||2. Choose S to make both
   current rows strictly below the bootstrap threshold. Time-zero reverse
   slots with zero variance must be retained, as in the audited P3 proof.

8. Fixed-cap population construction, same separate bounded Gaussian
   operators, three-cut comparison, and cut removal still require full
   proof. On a common bounded primal ball the asymmetric comparison
   constant appears LINEAR in the largest of Rw,R1,R2, not their product:
   split a difference into new gate times cut-query difference and old
   cut query times gate difference. Products with features use their
   bounded RMS norms. Gaussian tails for w,q1,q2 would beat exp(CR).
   Verify every constant and state/probe/velocity bridge; this is not a
   claim that the old bounded-activation theorem transfers automatically.

9. This proposed local theorem would discharge the existence premises
   of R26/R27 on a genuine short interval for the new activation. It would
   NOT give global opposite-label continuation. The purpose of pursuing
   the activation is its new same-mode curvature/action identities, which
   still need a bound for the correlated historical sensitivity.

Avoid circularity: do not derive source variance from the wished-for
tails, do not use an uncut population path to construct the references,
do not assume clipping preserves gradient energy, and do not treat the
finite Gaussian source rows as independent evolved neurons.

## Concrete constants worked out by root, not yet proof-audited

On the finite zero-readout feature references, start with first RMS <=2
and both initial hidden operator norms <=10. Use phi<=2+.1|z|. Bootstrap
first RMS<=3, both operator norms<=11, readout RMS<=1. This gives
H1 RMS<=2.3, H2 RMS<=4.53, H3 RMS<=6.983<7;
delta3 RMS<=.1||w||2, q2<=1.1||w||2, delta2<=.11||w||2,
q1<=1.21||w||2, delta1<=.121||w||2.
Thus ||w||2<=7s, first speed<=.121||w||2, W2 operator speed<=.253||w||2,
W3 speed<=.453||w||2. For S<=.1 all box inequalities improve strictly
by summing left-node Euler increments (or integrating). Exact forward
differences using the NEXT operator in the product split give Z2 RMS
speed<=.715||w||2 and Z3 speed<=2.83859||w||2. Hence H1/H2 give
cap-independent Lipschitz covariance metrics for xi2/xi3. Check rounding
up at each use; these values are not certified numerical constants yet.

Proposed response thresholds use the P3 convention
|A2_ka,rb|<=20 Delta/2, |A3_ka,rb|<=60 Delta/2, total B2/B3 rows<=1.
Moment bounds can be chosen uniformly for S<=.1 first, then S decreased
so E(P1)<=2 and ||P2||2<=2 for the injection/total sensitivity factors.
This gives A2's bracket <=(2.3)^2+.02<20, and A3's bracket
<= (4.53)^2+.01*20*2 <60, with ample margin.
The top total derivative is O(S) in expectation because w/S has a
sub-Gaussian envelope. Current B3=O(S) is proved before current B2.
Use ACTUAL primal ||q2||2<=7.7s (not its coarse pointwise envelope)
in Cauchy--Schwarz for B2. Learned transpose rows are O(S^3).
The final S0 can be defined as any sufficiently small positive number
depending only on finite Gaussian-envelope constants, with the strict
bootstrap improvements spelled out; a sharp numerical S0 is unnecessary.
