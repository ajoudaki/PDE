# Precommitted symbolic-\(Q^0\) audit

## Decision question

After the independent \(Q^0=1\) maps and the primary symbolic maps were
separately frozen, do their layer-tagged coefficients agree as polynomials in
the *explicit* first-layer metric factor \(Q^0\)?

The layer moments remain formal atoms in this test.  In particular, their
implicit dependence on the forward variances is not expanded.

## Competing outcomes

- **Pass:** for both \(H=3\) and \(H=4\), every atom coefficient agrees
  exactly at the six reconstruction points below and at the holdout.
- **Fail:** any exact rational coefficient or atom-support discrepancy.
- **Inconclusive:** the comparison does not finish within the declared
  resource envelope or an input hash/format gate fails.

No floating-point comparison is permitted.

## Independent degree bound

The only explicit occurrence of \(Q^0\) in the exact feature flow is

\[
\dot z^1=Q^0 b^1.
\]

Every application of the feature vector field can introduce this metric
factor at most once.  Hence the coefficient of \(D^k f\), after treating all
layer moments as formal atoms, has explicit \(Q^0\)-degree at most \(k\).
Thus the bounds for \((A,B,C)\) are respectively \((1,3,5)\), independently
of depth.  Six distinct evaluations therefore determine the largest of the
three coefficient polynomials.

## Points and exact decision rule

The reconstruction points are

\[
\left\{\frac12,\frac23,1,\frac32,2,3\right\},
\]

and the holdout is \(Q^0=5/2\).  At each point the independent factored
compiler is specialized first and then distributively canonicalized.  The
primary symbolic map is independently specialized by counting its explicit
`Q0` atoms.  The two sparse maps are compared after stripping only those
`Q0` atoms; no activation-moment identity is imposed.

If all six reconstruction comparisons vanish, then for every fixed
activation-atom monomial the difference is a degree-at-most-five polynomial
with six distinct roots, hence is identically zero.  The seventh point is a
redundant implementation holdout rather than part of that proof.

## Validity and resource gates

- Inputs must match their pre-existing freeze manifests.
- Canonical monomials are ordered tuples of layer-tagged one-dimensional
  moments; no numerical activation evaluation is used.
- Arithmetic uses `fractions.Fraction` throughout.
- At most one independent expanded root and one primary-specialized root are
  retained at a time.
- Hard envelope: 20 minutes wall time and 8 GiB peak resident memory for the
  complete \(H=3,4\) check.  Crossing either gate is inconclusive.

