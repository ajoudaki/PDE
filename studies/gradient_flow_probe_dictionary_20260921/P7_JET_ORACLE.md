# Finite canonical Taylor oracle through middle-weight power eight

## Frozen check design

This independently scoped CPU algebra oracle tests the complete finite
gradient vector field at the two physical probes `sqrt(2)e_a`, with equal
weights `1/2`, unhalved MSE, and exactly zero initial readout. It uses ordinary
Taylor coefficients, not divided derivatives. The initial matrix `A_0` has
entries of variance `1/n`; its adjoint is its actual transpose.

Write `g=W^(1)`, `h=tanh(g)`, `z=A h`, `H=tanh(z)`, `f=mean(c H)`,
`b=y-f`, `ell=1-h^2`, `d=1-H^2`, and `u=c d`. The equations tested are

```
c' = sum_a b_a H_a
A' = (u * b) h.T / n
g' = b * ell * (A.T @ u).
```

The `1/n` appears in the output mean and middle outer product; it does not
appear in the actual adjoint action. The factors of two from the loss and
one half from the probe weights cancel. The normalized input Gram is the
identity. Differentiating `h=tanh(g)` gives the separate activation equation
`h'=b*ell^2*(A.T@u)`, fixing the second lower gate independently.

The question is whether an ordinary coefficient recurrence preserves all
moving residuals, all three moving weight blocks, and both moving gates
through `A[t^8]`, `h[t^6]`, and `u[t^7]`. The alternative is an indexing,
normalization, composition, omitted-feedback, or label-extraction error.
This is an exact finite algebra check evaluated in floating point. It is
not a population dictionary, finite-width limit, training experiment, or
test of positive-time closure convergence.

Before implementation, the following bounded checks were fixed:

- Two Gaussian fixtures: `(seed,n,y)=(8101,5,(0.7,-1.1))` and
  `(8107,7,(-0.6,0.9))`.
- Numerical full jets through order eight, constructed by time-series
  multiplication and `tanh`'s differential recurrence; no finite differences.
- A separate sparse bivariate polynomial recurrence in symbolic labels;
  coefficient extraction by exact monomial bookkeeping, never interpolation.
- Comparison with the existing general-input vector field through order
  eight and the existing closed coefficient formulas through their supplied
  orders. Checks of the lower activation, upper preactivation/activation,
  gate and output differential identities through order seven.
- Label parity, zero-label stationarity, nonzero moving-block coefficients,
  and agreement between polynomial evaluation and numerical jets at the two
  declared nonsymmetric label values and their negatives.
- Maximum normalized absolute discrepancy threshold `3e-12`, using
  `max(1,max(abs(reference)))` as denominator. Any nonfinite quantity fails.
  No extrapolation to larger widths, no training, no GPU use, and no search
  over fixtures. Stop after these checks pass or expose an unresolved error.

Scientific inputs are restricted to `jet_check.py`, `p45_jet_check.py`,
`DERIVATION.md`, `P45_DERIVATION_ROUTE.md`, `new_dictionary.py`, and
`new_dictionary_p45.py` in this study. No other p7 agent's formulas or
findings were used before freezing this oracle. Required mathematical and
research skill instructions were read. The source and check results below
will be frozen before comparing any p7 candidate.

## Recurrence and why it gives the full finite coefficients

For a finite array-valued series `X(t)=sum_k X_k t^k`, multiplication means
the ordinary coefficient convolution

```
[XY]_k = sum_{j=0}^k X_j Y_(k-j).
```

The same rule uses matrix multiplication for an operator action and
pointwise multiplication for gates. For `Y=tanh(X)`, the initial value is
`Y_0=tanh(X_0)`, and the identity `Y'=X'(1-Y^2)` gives

```
Y_k = (1/k) sum_{j=1}^k j X_j
       (delta_(k-j,0) - sum_{q=0}^{k-j} Y_q Y_(k-j-q)),  k>=1.
```

All `Y` entries on the right have index at most `k-1`. Given state
coefficients through degree `k`, substitute these compositions and products
in the three vector fields and set each next state coefficient to its
velocity coefficient divided by `k+1`. Induction therefore determines the
unique formal solution through degree eight. Because this is a finite
smooth vector field, ordinary successive time differentiation at the
initial state gives the same coefficients of any local solution. The
recurrence does not infer them from trajectory samples.

The polynomial version repeats this recurrence with coefficients in the
ring of polynomials in `y1,y2` with finite array coefficients. Monomials are
stored as integer exponent pairs; addition and multiplication are exact
bookkeeping operations. Floating-point rounding affects the array values,
not which label powers are multiplied. No labels from a task enter this
coefficient construction.

The vector field is invariant under `y -> -y`, `c -> -c`, with `g,A`
unchanged. Its recurrence thus makes `g,A,h,z,H` and both gates even in
labels, and `c,f,b,cgate,reverse` odd. A second induction bounds every
position coefficient's label degree by its time degree: a factor `y` can
enter only through the constant residual coefficient, and advancing the
state recurrence then also advances time degree. Later residual coefficients
are output coefficients already controlled by that induction. In particular,
all possible degrees of `A_8` are `2,4,6,8`, of `h_6` are `2,4,6`, and
of `cgate_7` are `1,3,5,7`. The oracle retains every one of these degrees.

## Frozen result

The implementation `p7_jet_oracle.py` has SHA256
`8bb5cf889ecad721a52af9a1aaa275d6fb51b9884d6fbd992526e28aaa26543d`.
It was frozen and its API sent to the supervisor before exposure to any
p7 candidate formulas or other p7 agent's findings. Both declared fixtures
passed every check. The maximum normalized absolute discrepancy was
`3.6894710014097244e-16`, below the prespecified `3e-12` threshold.

| Check | Scope |
|---|---|
| Existing general-input oracle | All three state blocks through `t^8` |
| Existing independent closed formulas | All supplied coefficients through middle `t^6` |
| Direct normalization formulas | `c_1=Hy`, `A_2=(c_1 d*y)h.T/(2n)`, `h_2=y ell^2 A_0.T(c_1d)/2` |
| Differential composition identities | State, lower activation, upper preactivation/activation, both gates, output, residual, and `cgate`, through derivative degree seven |
| Symbolic polynomial evaluation | Every returned field at both label signs |
| Parity | Exact monomial parity and numerical sign symmetry |
| Degenerate labels | All positive-degree state and derived-field coefficients vanish at `y=0` |
| Moving-block checks | Lower, middle, readout, output feedback, `h_6`, `cgate_7`, `A_8` all nonzero |

The following are Frobenius norms of monomial-coefficient tables, not norms
of those polynomials at a selected task label:

| Fixture | Field/time | Degree 1 or 2 | Degree 3 or 4 | Degree 5 or 6 | Degree 7 or 8 |
|---|---|---:|---:|---:|---:|
| seed 8101, n=5 | `A_8` (even degrees) | 1.8300e-6 | 1.7386e-3 | 2.6959e-2 | 4.5046e-2 |
| seed 8101, n=5 | `h_6` (even degrees) | 6.6401e-4 | 8.4949e-2 | 2.3736e-1 | — |
| seed 8101, n=5 | `cgate_7` (odd degrees) | 5.8147e-7 | 3.3652e-3 | 3.4020e-1 | 1.2135 |
| seed 8107, n=7 | `A_8` (even degrees) | 4.1444e-7 | 2.4135e-4 | 2.5036e-3 | 3.6635e-3 |
| seed 8107, n=7 | `h_6` (even degrees) | 1.1719e-4 | 9.6089e-3 | 1.9357e-2 | — |
| seed 8107, n=7 | `cgate_7` (odd degrees) | 1.1173e-7 | 5.6381e-4 | 3.1294e-2 | 9.7475e-2 |

These finite sample values establish neither a population identity nor
independence of proposed dictionary columns. They show that a finite check
which discards lower label degrees would fail to test nonzero coefficients.

## API and artifacts

`full_jet(w0,a0,labels,order=8)` returns a dictionary of time-major arrays.
For example, `J['a'][8]` is the actual matrix coefficient `[t^8]A(t)`,
`J['h'][6]` is an `(n,2)` activation coefficient, and `J['cgate'][7]` is
the `(n,2)` coefficient `[t^7](c(t)*(1-H(t)^2))`. The first weight is
`J['w']`; for normalized axis probes it equals the lower preactivation.
`J['b']=y-f` uses the positive residual convention.

`full_polynomial_jet(w0,a0,order=8)` returns dictionaries with
`P[name][k][(i,j)] = [t^k y1^i y2^j]name`. Missing monomials are zero.
`evaluate_polynomial_jet(P,labels)` reconstructs numerical coefficient arrays.
`label_degree(P,name,k,d)` returns a dense table with its final axis indexed
by `j=0,...,d`, multiplying `y1^(d-j)y2^j`. Thus
`label_degree(P,'cgate',7,7)[:,a,:]` is the eight-column upper coefficient
table for probe `a`, while `label_degree(P,'h',6,6)[:,a,:]` contains the
seven candidate lower coefficients, including any structurally zero endpoint.

All finite pairings are literal arithmetic means and all matrix actions use
the supplied `a0` and its transpose. A population candidate can therefore
be compared with this oracle after explicitly replacing its pairings by
empirical pairings **for the algebra check only**. That replacement does
not define an admissible population dictionary or validate any population
moment reduction.

The reproducible command is

```
python studies/gradient_flow_probe_dictionary_20260921/p7_jet_oracle.py \
  --output-dir data/generated/gradient_flow_probe_dictionary_20260921/p7_jet_oracle01
```

The output directory contains `results.json`, two `case_<seed>_numeric.npz`
archives, and two `case_<seed>_polynomial.npz` archives. Numeric archives
include all returned coefficient arrays and the fixed labels. Polynomial
archive keys have form `<field>__t<k>__degree<d>` and the same trailing
monomial axis as `label_degree`. Results record source/input hashes,
environment versions, degree supports, every error group, and moving-block
norms. The command refuses to overwrite existing coefficient archives or
results. The authorized deterministic check program is complete.
