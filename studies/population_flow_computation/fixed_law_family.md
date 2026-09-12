# Frozen target law family, version 1

This definition is independent of every requested solver accuracy. It fixes
Y=1 and T=40. It is an internally checked computable admission construction,
not a practically evaluated radius. See admission_route.md and its independent
bounded check admission_check.md for the complete inequalities and proofs.

Fix once and for all the constants (4)--(5) of admission_route.md at Y=1,T=40.
Use its scalar searches (6)--(11). To make every selection deterministic and
avoid hanging on an exact equality, implement strict-inequality searches by
dovetailing finite candidate lists with increasing interval precision: at
stage n, check the first n integer candidates with the first n precision
levels; return the first strictly certified candidate at the first successful
stage, resolving ties by candidate index. Computable interval approximations
of the displayed elementary functions suffice. A strict solution eventually
exists because the negative quadratic tail exponent dominates the positive
linear exponent. Use the same rule for dyadic candidates 2^{-k}, k=1,2,...,
in (8) and (11), with strict versions of every upper bound.

Call the resulting positive dyadic radius rho. Fix d as the dyadic selected
by this same deterministic rule subject to

    0 < d < min(rho/96, 1/100).

This is a finite algorithmic definition of ONE positive rational constant.
It does not mean recomputing or shrinking d when accuracy, quadrature, time
step or sample size changes. Its literal bit representation has not been
materialized; the bounds are astronomically conservative.

The target family consists of all rational parameters

    a,b in [d,2d],  p in [1/2-d,1/2+d],

with V uniform on [-1,1] and independent branch J of probabilities p,1-p:

    J=1: u=(cos(aV),sin(aV)), y=1-b(1+V)/2;
    J=2: u=(-sin(aV),cos(aV)), y=-1+b(1+V)/2;
    x=sqrt(2)u.

Both branches are genuinely nonatomic arcs and labels depend on the arc
position. Distinct training directions need not be orthogonal. The coupled
input coordinates lie on the circle, and their joint law is not a product.
W1(mu,nu*)<=a/2+b/2+4|p-1/2|<=6d<rho/8. Midpoint quadrature with N cells
per branch has error <=(a+b/2)/(2N) in the normalized input/label W1 metric.
These claims and the mesh/radius bootstrap were checked independently.

The substantially broader numerical configuration family includes arbitrary
finite probability laws on the same circle with finite bounded labels,
positive numerical noise, positive physical steps and finite horizons, and
midpoint quadratures of these arc laws with any 0<a<=1/4, 0<b<=1/4,
1/4<=p<=3/4. The same source equations and refinement parameters define every
one of these finite computations. No broader population-existence theorem is
inferred. The executed arc law a=.03,b=.02,p=.53 belongs only to this broader
exploratory scope; it is not substituted for the admitted tiny-arc family.

The exact reference nu* is a separate admitted benchmark. Its nonlinear
learned trajectory is an appropriate practical target even when changed-law
effects for the tiny admitted arcs are much smaller than ordinary numerical
accuracy. Approximating that trajectory still requires its own error proof;
nearby-law existence does not provide one for the implemented method.
