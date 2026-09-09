# Connected cubic compiler: pre-run color-quotient amendment

## Prior attempt

The first `two_input_cubic_connected.cpp` order-seven plus-channel
run reached the frozen 20-minute timeout (exit status 124) before emitting
order seven.  Orders through five had already passed, but the order-seven
attempt is **inconclusive**.  No cap is enlarged and no partial order-seven
value is retained.

## Exact amended representation

For the equal-label plus channel, the global color exchange

\[
1\longleftrightarrow2
\]

leaves all of the following invariant:

- the channel signs \((1,1)\);
- the Gram matrix \(Q(\rho)\);
- every cubic \(a\)-, \(u\)-, and middle-weight rewrite;
- the bivariate Gaussian terminal moment;
- the desired sum of the two sample roots.

Therefore a tree and the tree obtained by exchanging the two exponent
coordinates at every column have exactly the same value polynomial.  The
amended cache key is the lexicographically smaller of their two canonical
uncolored-tree codes.  The final root sum is evaluated as twice the
color-zero root.  No tree term, covariance factor, or cross-example response
is deleted.

This quotient is not valid without modification for the minus channel; the
amended production remains plus-only.

## Frozen gates before renewed order seven

1. Quotiented and unquotiented sources agree through order five.
2. The quotient reproduces the two Gaussian-program polynomial assemblies
   through order five.
3. The vertex-partition and quotient-Wick terminal evaluators still agree on
   every reached terminal key through order five.
4. All parity, normalization, \(\rho=1\), source-hash, and model gates in
   `ORDER9_CONNECTED_PROTOCOL.md` remain in force.

## Amended resource and branch rule

- Audited order five: 5 minutes and 8 GiB.
- Renewed quotiented order seven: 12 minutes and 20 GiB.
- Order nine is authorized only if the quotiented order-seven run completes
  within that bound and all exact gates pass.
- Authorized order nine: 30 minutes and 32 GiB.
- No further representation amendment or cap increase is authorized in this
  campaign if the quotient route times out.

Passing the quotient gates upgrades only computational efficiency.  It does
not strengthen the positive-time or finite-width claim boundary.
