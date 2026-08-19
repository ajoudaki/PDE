# Independent canonical hidden-observable recurrence audit

Status: exact order-seventeen/order-sixteen run complete; frozen Campaign-1
regressions passed,
19 August 2026.

## Frozen contract

The run uses the canonical metric (D_a+D_u+D_W).  It constructs the exact
fixed-order width-limit Taylor state through degree seventeen and contracts

\[
F(t)=\mathbb E[A(t)Z(t)^2],\qquad
Q_1(t)=\mathbb E[X(t)],\qquad
Q_2(t)=\mathbb E[Z(t)^2].
\]

Here (X=u^2), so (Q_1) and (Q_2) are the first- and second-hidden
**squared** preactivation RMS observables.  The terminal targets were fixed at
(F^{(17)}(0)), (Q_1^{(16)}(0)), and (Q_2^{(16)}(0)); no higher-order
branch was run.

`independent_hidden_recurrence.py` reuses only the already-audited independent
packed-monomial and Isserlis substrate.  It writes the recurrence and the
three observable contractions separately and imports neither the production
hidden implementation nor its retained result.  All arithmetic is exact
`Fraction` arithmetic.

## Regression and identity gates

Before accepting new hidden rows, the run reproduced:

- every accepted canonical output derivative through order seventeen;
- every frozen canonical Campaign-1 (Q_1,Q_2) derivative through order
  eight;
- zero even derivatives for (F) and zero odd derivatives for (Q_1,Q_2);
- the exact Ward identity
  (Q_1^{(k)}(0)=8F^{(k-1)}(0)), (1\le k\le16).

All gates passed exactly.

## New hidden derivatives

The new nonzero first-hidden rows are

\[
\begin{aligned}
Q_1^{(10)}(0)&=9\,449\,289\,134\,603\,204\,493\,312,\\
Q_1^{(12)}(0)&=2\,335\,862\,659\,100\,686\,978\,683\,764\,736,\\
Q_1^{(14)}(0)&=822\,828\,098\,233\,973\,314\,828\,964\,208\,181\,248,\\
Q_1^{(16)}(0)&=392\,633\,476\,632\,616\,859\,814\,117\,035\,223\,934\,304\,256.
\end{aligned}
\]

The new independent second-hidden rows are

\[
\begin{aligned}
Q_2^{(10)}(0)&=487\,967\,758\,483\,103\,808\,178\,176,\\
Q_2^{(12)}(0)&=145\,387\,231\,337\,138\,218\,955\,012\,063\,232,\\
Q_2^{(14)}(0)&=60\,684\,843\,616\,663\,232\,253\,966\,043\,066\,638\,336,\\
Q_2^{(16)}(0)&=33\,941\,339\,036\,399\,103\,897\,550\,977\,212\,861\,900\,095\,488.
\end{aligned}
\]

All odd hidden derivatives through order fifteen vanish exactly.

## Resources and retained evidence

The exact 17/16 run completed in 158.110 seconds and peaked at 95.852 MiB
RSS, below the frozen 30-minute/8-GiB caps.  At terminal degree seventeen the
(A,X,Y,Z) polynomials contained respectively 1,733, 1,109, 1,758, and 1,758
monomials.

The complete derivatives, per-degree diagnostics, gate values, and source
hashes are retained in `INDEPENDENT_HIDDEN_RESULT.json`.  Its producing source
SHA-256 is

```text
fd923a6bff5e7f6d3f09a56f8a2ec208068615e7545c7e2d31178dd7c4817893
```

The frozen Campaign-1 input SHA-256 is

```text
02215aa7c18f3550a19f34b89734b6bf5b66a2825e8aa5bc103517767982ee1a
```

Three independent-route regression tests pass when invoked directly.  The
current system interpreter does not provide the `pytest` package, so the test
functions were imported and executed explicitly rather than through the
pytest runner.

## Claim level

These are exact fixed-order width-limit jets under the proved finite
Gaussian-program recurrence.  They do not by themselves prove a Stieltjes
representation for either hidden trajectory.  Exact output-coordinate series
reversion and ordinary/shifted Hankel tests are logically separate downstream
steps.
