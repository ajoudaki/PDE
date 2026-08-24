# Depth-two identity forty-moment Hankel audit

Status: frozen after exact long-jet production but before determinant
evaluation, 20 August 2026.

## Input and decision objects

Use the exact `mu_0,...,mu_39` in `RESULTS.json`, already obtained by two
exact feature-jet assemblers and two exact output-coordinate transforms.
Do not extrapolate or refit any moment.

Audit the nested ordinary and shifted Hankel matrices

\[
H_d=(\mu_{i+j})_{i,j=0}^d,\qquad
H_d^+=(\mu_{i+j+1})_{i,j=0}^d,
\qquad 0\le d\le19.
\]

An exact rational LDL decomposition must produce every leading determinant.
Every determinant through size six and both terminal size-twenty
determinants are independently recomputed by fraction-free symbolic
determinants.  Any disagreement is inconclusive.

If all twenty leading determinants in each family are positive, Sylvester's
criterion proves every displayed matrix positive definite.  This is a
finite forty-moment statement only; it cannot be called an all-order
Stieltjes theorem or a representing-measure construction.

