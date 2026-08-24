# Preregistration: genuine paired-cavity product

**Frozen before the run:** 23 August 2026.

## Question

The exact value-level proof has reduced the lower learned-history comparison to
the joint estimate
\[
 \mathbb E\,{1\over n}\sum_i
 |R_{2,i}^{\rm cav}(s)\{Z_{2,i}(s)-Z_{2,i}^{\rm cav}(s)\}|^q
 \lesssim n^{-q/2}.                                      \tag{1}
\]
This experiment tests the scaling in (1).  It cannot prove (1), and no numerical
outcome changes a theorem rung.

## Genuine cavity convention

For every canonical initialization and a uniformly sampled middle index \(j\),
the cavity initialization sets both
\[
 \Gamma_{1,j:}=0,\qquad \Gamma_{2,:j}=0,                 \tag{2}
\]
and then reruns the complete unclipped feature-time flow from
\(P_1(0)=P_2(0)=0\).  No learned correction from the full orbit is reused.  Hence
the cavity orbit has
\[
 Z_{2,j}^{\rm cav}=R_{2,j}^{\rm cav}=B_{2,j}^{\rm cav}=0
\]
at every time, up to arithmetic error.  A cavity which deletes only the raw
blocks while retaining the full learned matrices is not the object in (1).

## Frozen statistics

At \(s=1,2,4\) and \(q=2,4,6,8\), record
\[
 J_q(n,s)=\sqrt n\left\{
 {1\over n}\sum_i
 |R_{2,i}^{\rm cav}(s)\Delta Z_{2,i}(s)|^q
 \right\}^{1/q},                                        \tag{3}
\]
as well as
\[
 Z_q(n,s)=\sqrt n\,\|\Delta Z_2(s)\|_{q,n},\qquad
 R_q^{\rm cav}(n,s)=\|R_2^{\rm cav}(s)\|_{q,n}.          \tag{4}
\]
The primary statistic is \(J_q\).  The other two distinguish failure of the
base cavity scale from failure caused by weighted alignment.

Main widths are \(n=128,256,512,1024,2048\).  The feature integrator is explicit
midpoint with step \(h=0.01\), float32 evolution, and float64 aggregation.
Independent replicas are used at every width.  A common-draw step-halving audit
uses \(h=0.005\) at \(n=256,512\); a common-draw float64 audit uses \(n=128,256\).

## Frozen interpretation

For each \((q,s)\), fit the ordinary least-squares slope of
\(\log\operatorname{median}J_q\) against \(\log n\), with a replica bootstrap
95-percent interval.  The result is **formal empirical support** only if:

1. every central slope is at most \(0.08\);
2. every upper 95-percent endpoint is at most \(0.15\);
3. every available median \(J_q(2048,s)/J_q(256,s)\) is at most \(1.60\);
4. the median symmetric relative discrepancy in \(J_q\) is at most \(0.08\)
   for every step-halving and arithmetic audit cell; and
5. the cavity-zero identity in Section 2 is at most \(10^{-5}\) in float32
   and \(10^{-10}\) in float64.

There is **formal empirical evidence against** (1) if, for some \(q\ge4\) and
both \(s=2,4\), the lower 95-percent slope endpoint exceeds \(0.15\) and the
largest/smallest-width median ratio exceeds \(1.60\), after all numerical audits
pass.

Any other valid run is inconclusive.  A rare-event tail beyond the simulated
replica count remains an obvious alternative explanation even after a formal
support verdict.
