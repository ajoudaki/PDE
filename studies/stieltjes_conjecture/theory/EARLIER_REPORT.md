# Formal Stieltjes exact-computation audit

> **Superseded status notice (2026-08-12).** The order-11 computation described
> below as provisional has since been completed and audited.  The accepted
> value is
> 
> \[
> F_1^{(11)}(0)=291982832387585872335470592.
> \]
> 
> Its sector-by-sector provenance is recorded in
> `studies/stieltjes_conjecture/peeling/D11_LOWER_SECTOR_AUDIT.md`,
> `studies/stieltjes_conjecture/peeling/d11_high_sectors_exact.txt`, and
> `studies/stieltjes_conjecture/theory/certificates_order11.json`.  The historical text
> below is retained as an audit trail, not as the current research state.

## Current conclusion

No exact negative Hankel determinant was established.  The exact coefficient
pipeline is certified through derivative order 7.  A provisional derivative-11
calculation which stopped at ten Wick pairs is incomplete: the eleven- and
twelve-pair sectors are both strictly positive.  Therefore every moment or
Hankel determinant using that provisional coefficient is superseded.

## Exact low-order certificate

For the normalized Taylor coefficients of `F`,

```
D^1 f = 111
D^3 f = 1685184
D^5 f = 77400633120
D^7 f = 7315868433079296
```

and hence

```
a0 = 111
a1 = 280864
a2 = 645005276
a3 = 50804641896384/35
```

Through the available order, exact series inversion gives

```
mu0 = 280864/4107
mu1 = 38443196932/5616860517
```

so the size-one ordinary and shifted Hankel minors are positive.

`exact_graph_wick.py` obtains the large-n coefficient by differentiated
colored forests followed by exact Wick edge-pair contractions.  Two separate
audits are in `independent_checks.py`:

1. direct union-find enumeration of every Wick pairing agrees through order 3;
2. an unrelated scalar `n=1` exponent-triple recurrence agrees with graph
   differentiation through order 5.

The separately developed connected-component peeling recurrence gives the
same derivative through order 7.

## Exact high-sector facts

At derivative order 11, write `p` for the number of Wick pairs and `q` for the
explicit power of `1/n`.  The two omitted maximal sectors are

```
p=12, q=1: no B-derivative hit;
p=11, q=2: exactly one B-derivative hit.
```

Both are nonzero.  Explicit certified subfamilies are:

### p=12 witness family

Hit the same initial `x` factor all eleven times.  The coefficient is `8^11`.
Pair the resulting twelve odd `c` rows in any of `11!!` ways; within each row
pair, pair the two central edges and the two leaf edges.  The quotient has six
row classes and seven column classes, exactly `q+p=13` free classes.  Its
Gaussian moment is `3^6`.  Consequently this sector contributes at least

```
8^11 * 11!! * 3^6 = 65094137791119360.
```

### p=11 witness family

First differentiate an initial leaf B edge, then hit the same other initial
`x` factor ten times.  Pair the two edges in the even initial row and pair the
ten new odd rows in `9!!` ways as above.  The quotient again has thirteen free
classes and Gaussian moment `3^7`.  Consequently this sector contributes at
least

```
2 * 8^10 * 9!! * 3^7 = 4438236667576320.
```

These are lower bounds from explicit contraction families, not full sector
values.

At derivative order 13, the analogous all-`x` central-star family gives the
exact single-state contribution

```
8^13 * 13!! * 3^7 = 162474967926633922560.
```

It is independently evaluated from `order13_single_star.term` by the exact
component pairing code.

## Maximal-sector and lower-bound computations

The no-B-hit peeling recurrence gives exact maximal-pair sectors

```
D1: 75
D3: 666240
D5: 17576484864
D7: 947374026522624
```

The order-7 value agrees with direct enumeration of all 317 maximal-sector
forest states.  At order 11, generation is fast (29462 canonical states), but
complete Wick evaluation exceeded the available memory/time budget.

An exact positive-subset recurrence was made by declaring the Wick value zero
for every terminal connected component above a chosen raw-B-edge cap.  Since
all derivative and Wick summands are nonnegative, this is a rigorous lower
bound.  With cap 14 it gives

```
D^11 f >= 171581079093364877390972928
```

in 201.052 seconds.  Caps 2, 4, 6, 8, 10, 12 give the independently monotone
sequence

```
47549726635753458892800
3307693726260619821416448
19137221983807142685401088
52323627265312021203603456
92313546074432999279050752
135235415744792683804366848
```

as required by positivity.  The cap-14 bound is not by itself enough to
determine the relevant Hankel sign.

## Reproduction

Low-order graph recurrence:

```bash
python studies/stieltjes_conjecture/theory/exact_graph_wick.py \
  --max-order 5 \
  --output studies/stieltjes_conjecture/theory/derivatives_order5.json
```

Independent checks:

```bash
python studies/stieltjes_conjecture/theory/independent_checks.py \
  --max-order 5 --direct-wick-through 3
```

Rational series and Hankel certificate:

```bash
python studies/stieltjes_conjecture/theory/stieltjes_certificates.py \
  studies/stieltjes_conjecture/theory/derivatives_order5.json \
  --output studies/stieltjes_conjecture/theory/certificates_order5.json
```

Compile and run the positive-subset order-11 certificate:

```bash
g++ -O3 -std=c++20 -march=native \
  studies/stieltjes_conjecture/theory/peeling_lower_bound.cpp \
  -o /tmp/peeling_lower_bound
/tmp/peeling_lower_bound 11 14
```

Compile maximal-sector generator/evaluator:

```bash
g++ -O3 -std=c++20 -march=native -fopenmp \
  studies/stieltjes_conjecture/theory/leading_wick_jet_forest.cpp \
  -o /tmp/leading_wick_maxsector
OMP_NUM_THREADS=8 /tmp/leading_wick_maxsector 7 8 8
```

## Inverse-derivative reduction

There is an exact simplification of the Stieltjes question that removes the
derivative-square factor from the earlier reversion formula.  Write

```
F(t) = t phi(t^2),       G = F^{-1}.
```

Then Lagrange--Buermann inversion gives

```
G'(sqrt(x)) = 1/K(sqrt(x)) = sum_n (-1)^n h_n x^n,
h_n = (-1)^n [z^n] phi(z)^(-2n-1).
```

Moreover, the original sequence `mu` is Stieltjes if and only if `h` is
Stieltjes.  Indeed, if

```
sum_n (-1)^n h_n x^n
  = h0 / (1 + beta1*x/(1 + beta2*x/(1 + ...))),
```

then taking the reciprocal and subtracting its constant term gives

```
R(x) = (beta1/h0) / (1 + beta2*x/(1 + beta3*x/(1 + ...))).
```

Thus the S-fraction for `mu` is obtained by deleting the first level of the
S-fraction for `h`.  Equivalently, a representing measure `rho` for `h` would
give the passive-string representation

```
F^{-1}(y) = integral arctan(y*sqrt(t))/sqrt(t) rho(dt).
```

The first exact values are

```
h0 = 1/111,
h1 = 280864/50602347,
h2 = 275096956420/69205338429957,
h3 = 477889187282572736/157745610337167536445,
h4 = 3606194676606167103991472/1510164507677215425250682565.
```

Their ordinary Hankel determinants through size three and their shifted
determinants through size two are positive.  With B-variance `lambda/n`, the
available `h0,...,h4`, the two size-two determinants, and the ordinary
size-three determinant all have coefficientwise-positive numerators after
clearing their manifestly positive denominators.

This reduction does not by itself prove positivity.  Even an acyclic positive
cooperative system with the same coefficient-2 binary bridge-product rule can
fail: `C'=0, U'=C, Q'=2 U C, F'=C+2 Q C+4 Q^2`, with initial values
`C=1,U=Q=F=0`, gives `F=t+(2/3)t^3+(4/5)t^5` and hence
`mu1=-4/3`.  A proof therefore has to use the precise graft incidence and Wick
boundary values of the model, not positivity or bridge factorization alone.

## Remaining bottleneck

Compute the complete derivative-11 coefficient including `p=11,12`, then
recompute `mu4` exactly.  Only after that correction is the derivative-13
threshold for the shifted size-three Hankel determinant meaningful.  A direct
complete proof of the Stieltjes property remains open; positivity of all raw
derivative/Wick terms does not itself imply positivity of the reversion-derived
Hankel minors.
