# Campaign 5: three-input equicorrelated equal-label channel

## Frozen decision question

Does the first genuinely cyclic input geometry preserve the finite-order
output-kernel Stieltjes signs?

Campaign 5 studies three unit-RMS inputs with equicorrelated Gram matrix

$$
G(\rho)=
\begin{pmatrix}
1&\rho&\rho\\
\rho&1&\rho\\
\rho&\rho&1
\end{pmatrix},
\qquad -\frac12\le \rho\le1.
$$

The interval is exactly the PSD domain: the eigenvalues are
$1+2\rho,1-\rho,1-\rho$.  The labels are fixed to $(1,1,1)$, and no mixed
label or four-input branch belongs to this campaign.

For outputs $f_1,f_2,f_3$, define

$$
g=\frac{f_1+f_2+f_3}{3},
\qquad
D= n\nabla g\mathbin\cdot\nabla.
$$

The average squared loss is

$$
L=\frac13\sum_{\alpha=1}^3(f_\alpha-1)^2.
$$

On the permutation-symmetric channel
$(f_1,f_2,f_3)=(g,g,g)$,

$$
L=(g-1)^2,
\qquad
\dot g=2(1-g)K_3(g;\rho).
$$

Thus the tested scalar feature direction is the exact natural-loss reduction,
not an unrelated objective.

Internally the compiler removes thirds by using

$$
A=f_1+f_2+f_3=3g,
\qquad
\widetilde D=3D=n\nabla A\mathbin\cdot\nabla.
$$

If

$$
J_k(\rho)=\mathbb E[\widetilde D^kA],
$$

then the desired formal mean-field jet is recovered exactly as

$$
F_3^{(k)}(0;\rho)=\frac{J_k(\rho)}{3^{k+1}}.
$$

All fixed-order limits are leading-width MFP limits.  A finite formal jet is
not assumed to define a positive-time or global mean-field curve.

## Competing hypotheses and claim level

- **Campaign prediction:** the exact moment candidates
  $\mu_0(\rho),\mu_1(\rho),\mu_2(\rho)$ and
  $\Delta_1(\rho)=\mu_0\mu_2-\mu_1^2$ are nonnegative throughout the full
  PSD interval.
- **Discriminating alternative:** the signed triangle-cycle contractions,
  absent for two inputs, make at least one of these four rational functions
  negative at an admissible correlation.
- **Failure:** an exact negative witness for any of the four quantities,
  after every compiler and denominator gate passes, falsifies the
  three-input equal-label finite-order Stieltjes extension.  It does not by
  itself falsify the canonical one-input conjecture unless the witness is the
  canonical endpoint $\rho=1$.
- **Pass:** exact nonnegativity of all four quantities on the entire interval
  is stronger finite-order continuum evidence only.  It does not prove
  all-order Hankel positivity, existence of a representing measure, or global
  trajectory identification.
- **Inconclusive:** any timeout, memory failure, arithmetic overflow,
  provenance mismatch, failed regression gate, or uncertified interval sign.

Orders three and five are feasibility and novelty gates only.  They are not
Stieltjes success criteria because $\mu_2$ and $\Delta_1$ require order
seven.

## Mechanism preserved

The quadratic first-hidden activation makes individual input-sign flips
invisible, but the three-input Wick calculus retains the switching-invariant
triangle product.  For a Gaussian triple with common correlation $\rho$,

$$
\mathbb E[(u^1)^2(u^2)^2(u^3)^2]
=1+6\rho^2+8\rho^3.
$$

The nonzero $\rho^3$ term is the smallest cyclic input invariant unavailable
to every two-input campaign.  The same Gram matrix $G(\rho)$ must enter both:

1. the initialization moments of $(u^1,u^2,u^3)$; and
2. the first-layer $u$-gradient metric in every $u$-hit rewrite.

Omitting the second occurrence changes the training problem and invalidates
the experiment.

## Exact MFP grammar

A connected raw derivative state is a bipartite tree:

- a row vertex carries a power of the readout Gaussian;
- a column vertex carries the three exponents of
  $(u^1,u^2,u^3)$;
- an edge is a middle-weight factor.

The three local rewrites are the exact equal-label analogues of the accepted
one- and two-input compilers.  Every feature color has coefficient $+1$.
An off-diagonal first-layer metric factor contributes one power of $\rho$.
Terminal column moments are exact trivariate Gaussian moment polynomials in
$\rho$.  Production arithmetic must be checked signed integer arithmetic;
overflow must throw rather than wrap.

The implementation may expose an internal two-color equal-label mode solely
as a regression control.  No mixed-sign production channel is authorized.

## Mandatory validity gates

No coefficient or sign is interpreted unless all applicable gates pass.

1. Every even feature jet through the computed order is exactly zero.
2. Every normalized three-input jet is an exact rational polynomial in
   $\rho$ with denominator dividing $3^{k+1}$.
3. The exact first derivative is

   $$
   F_3'(0;\rho)
   =\frac{141+80\rho^2+112\rho^4}{3}.
   $$

4. At $\rho=1$, every computed normalized derivative reproduces the accepted
   canonical one-input derivative.
5. In internal two-color mode, normalization by $2^{k+1}$ reproduces the
   accepted Campaign-2 equal-label jet through the common computed order.
6. A transparent labelled-edge Wick oracle and the checked connected
   compiler agree coefficient-for-coefficient through order three.
7. The transparent calculation records an explicit nonzero surviving
   three-color contribution at order three.  In particular, at least one
   nonzero odd power of $\rho$ must be traced to a terminal contraction whose
   color support is exactly $\{1,2,3\}$; an unexplained aggregate odd
   coefficient is not sufficient.
8. The trivariate moment evaluator agrees with direct labelled Gaussian Wick
   pairing over every exponent triple reached by the order-three oracle and
   with
   $\mathbb E[(u^1)^2(u^2)^2(u^3)^2]=1+6\rho^2+8\rho^3$.
9. Source, command, binary, raw-output, and certificate hashes must be frozen
   for every accepted production stage.

## Stage A: order-three feasibility

- Target: complete exact $F_3^{(k)}(0;\rho)$ for $0\le k\le3$.
- Independent route: transparent labelled-edge Wick enumeration through
  order three.
- Hard cap: 2 GiB address space and 10 minutes wall time.
- Required gates: all gates above that are meaningful through order three,
  including the exact first derivative, two-input control, canonical
  endpoint, and explicit nonzero three-color sector.
- Branch rule: Stage B is authorized only if Stage A completes within its cap
  and all gates pass.  Otherwise the campaign stops as inconclusive.

## Stage B: order-five novelty and resource projection

- Target: complete exact jets through order five.
- Hard cap: 4 GiB address space and 30 minutes wall time.
- The scale-invariant novelty statistic is

  $$
  \mathcal I(\rho)
  =\frac{F_3'(0;\rho)F_3^{(5)}(0;\rho)}
  {F_3^{(3)}(0;\rho)^2}.
  $$

  It must be proved nonconstant on $[-1/2,1]$; otherwise the apparent family
  may collapse to separate output and time rescalings and Stage C is not
  scientifically justified.
- Record value-state, terminal-contraction, polynomial-degree, time, and peak
  memory growth at orders three and five.
- Project the cost of order seven before starting it.  Stage C is authorized
  only if the scale-invariant novelty gate passes and a sectorized exact run
  is projected to fit the frozen cumulative CPU and per-sector memory caps.
- Failure to meet either condition stops the campaign without a Stieltjes
  conclusion.

## Stage C: order-seven decisive finite test

- Target: complete exact $F_3^{(7)}(0;\rho)$ using a sectorized compiler.
- Per-sector address-space cap: 4 GiB.
- Cumulative CPU-time cap across all order-seven sectors: 6 CPU-hours.
- Every sector result is written atomically: write a temporary file, validate
  its schema and exact sector identity, then rename it into the checkpoint
  directory.  A completed sector must survive interruption and be reusable
  only when its source, binary, and configuration hashes still match.
- The runner must stop before launching a sector that would exceed the
  remaining cumulative budget.  Enlarging the budget, switching to an
  uncapped monolithic run, or adding a new contraction route after observing
  the order-seven result is not authorized.

If and only if all order-seven sectors complete and every validity gate
passes, exact reversion constructs

$$
K_3(y;\rho)
=F_3'\!\left(F_3^{-1}(y;\rho);\rho\right)
=a(\rho)+\mu_0(\rho)y^2-\mu_1(\rho)y^4
+\mu_2(\rho)y^6+O(y^8).
$$

The primary exact tests are

$$
\mu_0(\rho),\qquad
\mu_1(\rho),\qquad
\mu_2(\rho),\qquad
\Delta_1(\rho)=\mu_0(\rho)\mu_2(\rho)-\mu_1(\rho)^2.
$$

After rational cancellation, both numerator and denominator of every
quantity must be certified on each half-interval

$$
\left[-\frac12,0\right]
\qquad\text{and}\qquad
[0,1]
$$

by exact rational Sturm root counts plus exact endpoint signs.  Positive
coefficient lists or numerical sampling may be reported as secondary
diagnostics but are not the primary certificate.  A zero requires exact
factorization and a proof that its multiplicity is compatible with
nonnegativity.

## Terminal stop

The campaign ends after the order-seven sign report, or earlier at the first
failed gate or exhausted cap.  It does not branch to order nine, mixed labels,
non-equicorrelated triangles, or four inputs.

