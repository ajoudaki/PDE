# Independent canonical high-order recurrence audit

Status: exact order-seventeen run complete; independent agreement obtained,
18 August 2026.

## Isolation and recurrence

[`independent_canonical_recurrence.py`](independent_canonical_recurrence.py)
does not import the production generator or either candidate high-order value.
It reimplements equations (5)--(11) of the proved fixed-order Gaussian-program
recurrence directly at \(\alpha=1\).  Gaussian monomials are represented by
packed base-256 exponent vectors, and all expectations are computed by a new
exact Isserlis recursion over a growing rational covariance matrix.

Two dependency reductions are exact:

1. Since \(\dot A=Z^2\),
   \[
   F(t)=\mathbb E[A(t)Z(t)^2]
       =\mathbb E[A(t)\dot A(t)]
       =\frac12\frac d{dt}\mathbb E[A(t)^2].
   \]
   This avoids constructing the full observable polynomial.  At terminal
   order, its single unavailable \(A_{k+1}\) contribution is contracted
   directly as \(\mathbb E[A_0\sum_{r+s=k}Z_rZ_s]\).
2. After constructing \(Z_k\) at the requested terminal order, the unused
   fields \(B_k,Q_k,R_k\) cannot contribute to any \(F^{(j)}(0)\), \(j\le k\),
   and are not constructed.

These cuts change neither the scalar recurrence nor its exact output.

## Prefix gate

Before accepting a new value, the implementation reproduced every canonical
derivative through order thirteen:

```text
F1  = 111
F3  = 1685184
F5  = 77400633120
F7  = 7315868433079296
F9  = 1181161141825400561664
F11 = 291982832387585872335470592
F13 = 102853512279246664353620526022656
```

All even derivatives through order sixteen were exactly zero.

## New exact values

The independent recurrence gives

\[
\boxed{F^{(15)}(0)
=49\,079\,184\,579\,077\,107\,476\,764\,629\,402\,991\,788\,032}
\]

and

\[
\boxed{F^{(17)}(0)
=30\,555\,969\,894\,096\,099\,495\,444\,855\,650\,521\,777\,374\,167\,040}.
\]

An isolated production implementation returned the same two integers exactly.

## Frozen resource gates

The standalone independent order-fifteen run took 43.59 seconds and peaked at
49,404 KiB RSS, below its 20-minute/4-GiB cap.  The order-seventeen run took
163.08 seconds and peaked at 94,060 KiB RSS, below its 30-minute/8-GiB cap.
At terminal degree seventeen, \(A,X,Y,Z\) contained respectively
1,733, 1,109, 1,758, and 1,758 sparse monomials.  The final row and column Wick
caches contained 241,906 and 240,016 entries.

The complete machine-readable values, commands, checkpoints, cache sizes, and
resource measurements are retained in
[`INDEPENDENT_RESULT.json`](INDEPENDENT_RESULT.json).  The frozen protocol ends
at order seventeen; no order-nineteen branch was attempted.

## Claim level

This is an exact fixed-order width-limit calculation under the already proved
finite Gaussian-program recurrence.  It does not establish a positive-time
trajectory limit or an all-order moment representation.  Stieltjes moments
and Hankel signs are computed separately by exact series inversion.
