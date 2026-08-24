# Finite-width tail audit

Status: discriminating evidence only; not used as a proof.

The script
`../leaky_arctan_depth3_operator_ide/activation_tail_audit.py` integrates the
exact physical gradient flow by RK4 for one label `y=1`.  At `T=2`, with
three independent seeds and step `0.02`, the tanh diagnostics were:

| width | mean predictor | mean raw `K` | `max |Q_2|/sqrt(n)` | largest-coordinate share of `Q_2^2` |
|---:|---:|---:|---:|---:|
| 128 | 0.9188 | 0.6677 | 0.1941 | 0.0602 |
| 256 | 0.9269 | 0.6863 | 0.1439 | 0.0330 |
| 512 | 0.9235 | 0.6824 | 0.1074 | 0.0177 |

For moments `p=(2,4,6,8,12,16)`, the width-512 averages of
`<|Q_2|^p>^(1/p)/p` were

\[
 (0.4042,0.2607,0.2037,0.1707,0.1315,0.1077),
\]

and for `Q_1` they were

\[
 (0.2076,0.1377,0.1099,0.0938,0.0739,0.0612).
\]

The decreasing largest-coordinate energy share and bounded moment ratios
show no ordinary-trajectory focusing at these widths and times.  They do not
exclude rare or vanishing-time concentration, and therefore do not establish
`(AG_T)`.

