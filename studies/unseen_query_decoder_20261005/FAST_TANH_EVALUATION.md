# Tanh evaluation is covered by the local decoder's bit-work envelope

2026-10-06. Elementary lead-author implementation lemma; initially pending
the bounded assembly reconstruction. This is a specialization of evaluator
costs, not a restriction of the general activation theorem.

For real input x represented to the requested precision, tanh(x) can be
evaluated to absolute error 2^(-p) with O(p^3) bit work and O(p) live
scratch, including argument-length allowance in p. The constants are
absolute. Only real values are needed by the decoder's activation
interpolation and passive evaluation; no derivative oracle is used.

## Direct finite algorithm

Oddness reduces to x>=0. If x>=p+4, output one. Indeed
1-tanh(x)=2/(exp(2x)+1)<=2 exp(-2x)<2^(-p-3).
The comparison uses an integer cutoff, not an exact comparison with a
transcendental number. Acquisition error in x is charged separately below.

Otherwise choose k>=0 by binary comparisons so z=2x/2^k is in [0,1]
and 2^k<=4(p+4). Thus k=O(log(p+2)). Evaluate exp(-z) using the first
J+1 terms of its alternating Taylor series, J=16(p+1). Generate each
term from the previous one by multiplication by -z and division by its
integer index. Accumulate the sum, then square k times. All arithmetic
uses b=p+C log_2(p+2)+C fractional guard bits, with one sufficiently
large absolute C. Clip the exponential approximation to [0,1] after
its Taylor evaluation and after every squaring.

On [0,1], the exact alternating remainder has magnitude at most
1/(J+1)!. To check that it fits the guard allowance, at least floor(J/2)
factors in J! are at least J/2, so
log_2(J!)>=floor(J/2)log_2(J/2); this dominates p plus any of the fixed
logarithmic guards needed here, increasing the fixed 16 if necessary.
The exact term magnitudes are at most one. Rounding its recurrence and
summing J terms costs at most C J^2 2^(-b), by induction and addition.
Projection to [0,1] cannot increase distance from the exact exponential.
Each subsequent squaring is 2-Lipschitz on [0,1], and its rounding adds
O(2^(-b)). Thus the total squaring amplification is at most 2^k<=4(p+4).
The stated logarithmic guard allowance makes the resulting approximation
to exp(-2x) accurate to 2^(-p-5).

Finally use tanh(x)=(1-exp(-2x))/(1+exp(-2x)). Its denominator is at
least one, and this rational function is 2-Lipschitz in its exponential
argument on [0,1]. Ordinary rounded division at b bits therefore yields
the requested error with spare margin. Restore the sign for negative x.

There are O(p) multiplications/divisions of O(p)-bit numbers and only
O(log(p+2)) squarings. Schoolbook multiplication and long division each
cost O(p^2) bit operations. A constant number of terms, accumulators,
and O(p)-bit work arrays suffice, proving the claimed work and scratch.
Since |tanh'(x)|<=1, input error at most 2^(-p-3) is enough after a
constant increase in requested precision. Handling long supplied input
descriptions and producing those input bits remains an input-access charge.

## Substitution into the complete local ledger

Use the local assembly's field certificate R>=1 and common word length p.
It calls activations/data at most CnR^3 times during initialization,
CR^4 times during all updates, and C(L+1)(n/R+R^2) times per query.
Applying the tanh algorithm adds respectively

\[
 CnR^3p^3,\qquad CR^4p^3,\qquad
 C(L+1)(n/R+R^2)p^3
\]

bit operations for the activation part. The first is below the existing
metric-construction term nR^5p^3; the second is already an update term;
the third is below the existing query stream (L+1)np^3 plus preparation
(L+1)R^4p^3. One live O(p)-bit evaluator fits the existing peak memory.
Therefore the explicit local bounds need no larger powers for tanh
evaluation. Training/query data access, scale/output encodings, and
certificate costs are still charged separately as before.

This observation does not give O(p^3) evaluation for arbitrary analytic
activations. Their supplied evaluator description, work, and scratch
remain explicit interfaces. It also does not reduce the query's factor n.
