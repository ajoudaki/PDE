# A persistent feedback boundary in the output-only selective hierarchy

2026-09-27. Scoped theoretical assessment within this study. No training or
new experiment. Inputs: the exact block model in sections 1–2 of
`AGGREGATE_SCALAR_CONSTRUCTION.md`; `TRUE_AGGREGATE_OBSTRUCTION.md`,
`TRUE_AGGREGATE_GAUSSIAN.md`, the bounded-tree construction and its audit;
the selective compiler sources and completed selective-result reports.
The investigate-conjectures and solve-math-rigorously skills were applied.
These are internally derived study results, not promoted book material.

**Conclusion.** Selective failures do not imply that every effective scalar
aggregate ODE fails. There is, however, a precise defect in the current
output-only refinement: increasing its output depth never removes certain
first-layer feedback boundaries. Below, on the actual canonical Gaussian
population, a fixed set of eleven retained moments and the clock has a
strictly positive, depth-independent approximation lower bound. This is a
limitation of that selective family; it is not an output-only lower bound
and does not apply to a selection which expands every feedback dependency.
For the saved experiments, the disagreement between core and passive
predictions at the same input gives a separate direct output-error lower
bound with no reference-network assumption.

## 1. The quantifiers which the failures do not settle

Fix block size k, number of data m, memory order H, bounded labels and the
specified Gaussian initialization. A horizon-independent approximation
hierarchy consists of finite autonomous scalar ODEs A_D whose equations,
state counts and initialization rules do not depend on elapsed time or on
a chosen terminal horizon. The compact-time claim is

\[
\text{for every finite }T,\qquad
\lim_{D\to\infty}\sup_{0\le t\le T,\ u\in S^1}
 |\widehat f_D(t,u)-f(t,u)|=0.
\tag{1}
\]

The required D for a numerical tolerance may depend on the horizon in this
statement. Requiring one D(epsilon) to give error epsilon simultaneously
for every finite T would instead mean uniform approximation on [0,infinity).
Those two quantifier orders must not be interchanged.

An effective polynomial theorem additionally bounds state count,
coefficient construction, initialization, RHS/decoder work and precision as
functions of the structural parameters and accuracy. A negative theorem
about all such methods must define that admissible computational class.
The single deterministic Gaussian orbit and its separating clock do not
give an information-theoretic state-dimension lower bound; the clock
playback construction in `TRUE_AGGREGATE_OBSTRUCTION.md` is expressly
inadmissible. Conversely, failure of the current zero-boundary selection
is not a failure of every ordinary expected-statistics representation.

The bounded-G aggregate construction already proves a substantive positive
result for its stated finite-query target. The separate
`NEXT_GAUSSIAN_ROUTE.md`, subsequently read completely and internally
crosschecked during this assignment, extends this to the actual Gaussian
block population and a common full-circle decoder. It combines propagated
Gaussian cutoff control, uniform passive-query families and a sufficiently
slow horizon-independent cutoff schedule. Its cost certificate is very
poor. Thus bare computable aggregate existence is now supported by a
constructive theorem; the requested useful polynomial cost remains open.
Neither conclusion can be accepted or rejected from the numerical behavior
of a nonexhaustive selective family.

## 2. What output depth does not expand

The tested selective family has `dependency_depth=0`, `output_depth=J`,
`preserve_essential=True`, and zero omitted children. Its retained set is
the union of a fixed feedback/Gram seed set and J generations of local
tree derivatives beginning at the outputs. Here a tree derivative means
the compiler's local-coordinate Lie derivative; coefficient-field
derivatives are not included in this descendant operation.

In `true_aggregate_ode.py`, `graft` retains every existing vertex and edge,
changes decorations at one existing vertex, and attaches fresh vertices.
`canonical` reroots a tree without deleting vertices. Every output root
contains a second-layer vertex. Consequently every output descendant has
at least one second-layer vertex, however large J becomes. A tree supported
on a single first-layer vertex can enter only through the fixed seed set.

This is an exact property of the selection, including its canonicalization,
not a count-based heuristic. The exact-signature compiler optimization
preserves the same selected equations.

The following specialization supplies an explicit missing feedback family.
Set H=m=1, choose a unit training input and a nonzero scalar label y, and
allow any fixed k>=1. This is a valid member of the canonical target class.
Use the clock-normalized local coordinates

\[
x=\tanh(wu),\quad h=\tanh(z_2(u)),\quad
\beta=B_0/L,\quad \alpha=A_0/L^2,\quad \zeta=c/(2L).
\]

For a vector expression v write
\(\langle v\rangle=\mathbb E[k^{-1}\sum_i v_i]\), with the
appropriate layer understood. Define

\[
F=\langle\zeta h\rangle,\quad
R=2F-y/L,\quad \sigma=|R|,\quad
\tau=\langle\alpha\zeta(1-h^2)\rangle.
\]

The exact lifted equations include

\[
\begin{aligned}
\beta'&=\sigma(x-\beta),\\
\zeta'&=-Rh-\sigma\zeta,\\
\alpha'&=2R\zeta(1-h^2)-2\sigma\alpha,\\
x'&=-4L^2R(1-x^2)^2\odot
             G^T[\zeta(1-h^2)]
       +8L^4R\tau\,\beta\odot(1-x^2)^2,\\
L'&=\sigma L.
\end{aligned}
\tag{2}
\]

All products except matrix multiplication are coordinatewise. These formulas
use the actual reused G and its transpose.

For this one-input specialization, the fixed pure-first-layer seed
moments have beta exponent at most two. Indeed the seed \(s=\langle\beta
x\rangle\) and its direct derivative contribute
\(\langle x^2\rangle,\langle\beta x\rangle\), and
\(\langle\beta^2x^r\rangle\) for r=0,2,4, besides one-edge trees.
The protected first-layer Gram derivative adds
\(\langle\beta x^r\rangle\) for r=1,3,5. All other feedback/Gram
seeds have a second-layer vertex. Thus

\[
q=\langle\beta^2x^4\rangle
\quad\hbox{is retained, while}\quad
\langle\beta^3x^3\rangle,\ 
\langle\beta^3x^5\rangle,\ 
\langle\beta^3x^7\rangle
\quad\hbox{are absent for every }J.
\tag{3}
\]

Increasing `dependency_depth` would remove this particular statement.

## 3. An exact residual on the canonical Gaussian orbit

Let a=k Gscale, where Gscale is the fixed positive normalization used by
the compiler. For r=3,5,7 and e=0,2 define its normalized one-edge moments

\[
U_{r,e}=
\mathbb E\left[\frac1{k^2}\sum_{i,\gamma}
 \frac{G_{\gamma i}}{\mathrm{Gscale}}
 \beta_i^2x_i^r\zeta_\gamma h_\gamma^e\right],
\qquad
\mathcal U=U_{3,0}-U_{3,2}-2U_{5,0}+2U_{5,2}
                         +U_{7,0}-U_{7,2}.
\]

Direct differentiation of q using (2) gives

\[
q'=2\sigma(b-q)-16aL^2R\mathcal U+\eta(t),
\quad b=\langle\beta x^5\rangle,
\quad
\eta(t)=32L^4R\tau
             \langle\beta^3x^3(1-x^2)^2\rangle.
\tag{4}
\]

For every J>=2, b and all six U moments are retained. For b, use the
protected derivative of the first Gram moment. For U, the first output
derivative includes the forward-memory trees

\[
\zeta(1-h^2)\;\text{---}\;
              \beta(1-x^2)^2.
\]

Here the edge is the normalized G contraction. Differentiating an x
decoration at that first-layer vertex by the memory part of (2) creates
the trees with \(\beta^2x^r\), r=3,5,7, and second decorations
\(\zeta h^e\), e=0,2. Their coefficients are nonzero. Thus every term
of (4) except eta belongs to the selected q row already at J=2. Equation
(3) deletes exactly the three monomials whose signed combination is eta.
No new output depth can restore them.

A separate scoped symbolic check of the current `FastSelectiveClosure`
at m=H=1, k=2, unit input, y=1 and J=2 found exactly eleven combined
terms in this row: the eight non-source terms are retained, and the only
three missing children are precisely the three in (3), with coefficients
32,-64,32 multiplying L^4 R tau. This check compiled equations only; it
did not evolve a training trajectory. The structural argument above
supplies the statement for every k and every J>=2.

The source is nonzero on the prescribed Gaussian orbit. At time zero,
\(\beta_0=x_0\), \(\alpha_0=\zeta_0=0\), L_0=1 and R_0=-y.
Write \(h_0=\tanh(Gx_0)\). Integral forms of (2) give

\[
\frac{\zeta(t)}t\longrightarrow yh_0,
\qquad
\frac{\alpha(t)}{t^2}\longrightarrow
       -y^2h_0(1-h_0^2).
\]

The clock bounds imply uniform local bounds on both ratios; the gates
are bounded. Pointwise continuity and dominated convergence consequently
give

\[
\frac{\tau(t)}{t^3}\longrightarrow-y^3\kappa,
\qquad
\kappa=\left\langle h_0^2(1-h_0^2)^2\right\rangle>0,
\]

and

\[
\langle\beta^3x^3(1-x^2)^2\rangle\longrightarrow
\mu:=\mathbb E[\tanh^6 Z\,(1-\tanh^2 Z)^2]>0,
\qquad Z\sim N(0,1).
\]

For k>=1, \(Gx_0\) is conditionally a nondegenerate centered Gaussian
almost surely, proving strict positivity of kappa; positivity of mu is
immediate from the nonzero nonnegative integrand. Hence

\[
\eta(t)/t^3\longrightarrow32y^4\kappa\mu>0.
\tag{5}
\]

This argument uses bounded ratios and integrals rather than an unproved
high-order analytic expansion of the Gaussian flow. Existence and
continuity of the stipulated canonical characteristic solution are the
same local hypotheses as in the earlier obstruction note.

## 4. A depth-independent quantitative error floor for twelve coordinates

Let K consist of the eleven moments

\[
q,\ b,\ (U_{r,e})_{r=3,5,7;\ e=0,2},\ F,
v_0=\langle\alpha\zeta\rangle,
v_2=\langle\alpha\zeta h^2\rangle,
\]

and L. Thus tau=v_0-v_2. These coordinates are present for every J>=2.
Initialize the finite scalar closure by the exact canonical Gaussian
expectations; no future trajectory is supplied. This strengthens the
initializer relative to an empirical finite-pool initializer and isolates
the approximation defect.

For these twelve coordinates, define

\[
E_J(T)=\sup_{0\le t\le T}
      \max_{v\in K}|v(t)-\widehat v_J(t)|.
\]

There exists T_0>0 such that, for every 0<T<=T_0 and every J>=2,

\[
E_J(T)\ge
\frac{4y^4\kappa\mu\,T^4}{1+T C_T}>0,
\tag{6}
\]

where C_T is explicit and independent of J. For the implemented retained-row
penalty, one possible value is

\[
B=2+|y|,\quad M=e^{BT},\qquad
C_T=B\,[16+512a(M^2+M)].
\tag{7}
\]

**Proof.** By (5), reduce T_0 so that
\(\eta(t)\ge16y^4\kappa\mu t^3\) on [0,T_0]. The exact eleven
moments initially lie strictly inside [-1,1]: the pure first-layer ones
are expectations of strict powers of tanh, and every U,F,v is zero.
Continuity permits a further reduction of T_0 so that clipping is inactive
on the exact K coordinates. This does not impose bounded G; only these
fixed low moments are involved.

Write pi for clipping to [-1,1]. The selected q row, for all J>=2, is the
same fixed function

\[
\begin{aligned}
\mathcal F(K)={}&2\widehat\sigma[\pi(b)-\pi(q)]
 -16aL^2\widehat R\,\mathcal U(\pi(U))\\
&-(4+128aL^2)\widehat\sigma[\,q-\pi(q)\,],\\
\widehat R={}&2\pi(F)-y/L,\qquad
\widehat\sigma=|\widehat R|.
\end{aligned}
\tag{8}
\]

The coefficient in the last line is the exact retained-row absolute
envelope: four sigma from the b,q terms and 128aL^2 sigma from the six
edge terms. The moments q and all other fixed coordinates remain in
[-2,2] under their own envelope penalties, starting from their bounded
initial values. The approximate and exact clocks satisfy 1<=L<=M,
because their clipped or physical normalized output obeys |F|<=1 and
L'=|R|L<=BL. A possibly large initial value of some other high-degree
Gaussian moment does not enter the fixed function (8).

Clipping and q-pi(q) are both 1-Lipschitz. On this compact region,
|R|<=B, R is B-Lipschitz in the sup norm, |U_combination|<=8,
and its Lipschitz constant is eight. Bounding the first term in (8)
gives 8B; the edge term gives 256aB(M^2+M); the penalty gives
B[8+256a(M^2+M)]. Their sum is (7). The same estimate holds between
the exact K and the approximate K.

The exact row is q'=F(K)+eta, while the approximate row is
qhat'=F(Khat). Subtract and integrate from the identical initial q:

\[
\int_0^T\eta(t)\,dt
\le |q(T)-\widehat q(T)|
       +C_T\int_0^T\|K(t)-\widehat K(t)\|_\infty\,dt
\le(1+TC_T)E_J(T).
\]

The source integral is at least 4y^4 kappa mu T^4. This proves (6).
For an initializer with q error at most delta, subtract delta from the
numerator before taking its positive part. QED.

**Scope of (6).** It is a true canonical-reachability lower bound for a
fixed finite set of ordinary aggregate observables and the current
output-only selection. It is stronger than observing a formally missing
moment. It does not imply a lower bound on f alone: an inaccurate internal
moment can, in principle, coexist with accurate selected outputs. A
noncancelling propagation argument to f and loss is a separate obligation.
No such output-only propagation theorem is claimed here. In particular,
(6) cannot be used against a new selection which differentiates all
essential feedback moments recursively.

## 5. A direct output limitation certified by the alias discrepancy

Suppose at a scalar state and one training input u_a the implementation
reports a core prediction p_a and a passive-query prediction z_a. For any
single-valued target f(t,u), including the actual canonical Gaussian
population at that same physical time,

\[
\max\{|p_a-f(t,u_a)|,\ |z_a-f(t,u_a)|\}
       \ge\tfrac12|p_a-z_a|.
\tag{9}
\]

This is the triangle inequality. It requires no trained reference, no
same-stopping-time comparison, no finite-width identification and no
circle quadrature estimate. The two scalar predictions refer to the
same time and input. Since the training inputs in these saved tasks lie on the circle, a
claim that both internal training predictions and the passive whole-circle
decoder uniformly approximate the same exact output must obey this bound.

For example, `SELECTIVE_ALL_TASKS_RESULTS.md` reports maximum alias gaps
of approximately 0.52853 for the close opposite-label pair and 0.23706
for the mixed quartet at J2. At least one of the two corresponding
output errors is therefore approximately at least 0.26426 and 0.11853,
respectively, against *any* single-valued exact target at that time.
The fitted orthogonal J2 continuation in `SELECTIVE_TIGHTER_RESULTS.md`
has a reported gap 0.05088 and hence the analogous bound 0.02544.
These numerical values inherit the reports' rounding; (9) is exact.

This does not identify which decoder is closer to the target. It does not
lower-bound the passive-only error if the core prediction is excluded from
the claimed observable family. It does prove that describing both as
accurate values of one learned function is untenable below half their
disagreement. Merely forcing the two decoders to report the same number
would remove this diagnostic, but would not prove target accuracy.

## 6. What changes in the research conclusion

| Claim | Status and exact scope |
|---|---|
| Output depth J exhausts the needed feedback hierarchy | False for the current `dependency_depth=0` selection; (3) gives permanent omissions. |
| Its retained aggregate trajectory converges to the canonical one as J grows | False jointly on the twelve fixed coordinates K, by (6), even with exact Gaussian initialization. |
| Its saved core and passive predictions can both be uniformly accurate below half their alias gap | False by (9). |
| The current J family cannot approximate f alone arbitrarily accurately | Open here; noncancelling output propagation is missing. |
| No computable aggregate-only width-independent hierarchy can approximate Gaussian block population outputs on compact time intervals | Contradicted by the internally checked construction in `NEXT_GAUSSIAN_ROUTE.md`; its inefficient rate does not settle the useful polynomial question. |
| A useful polynomial accuracy/size/work guarantee follows from bounded-tree existence alone | Not established; the Gaussian tail, coefficient-growth, initialization and complexity obligations remain distinct. |

The single highest-leverage structural repair is to expand dependencies of
all retained essential coefficient fields, including dot-s constituents,
instead of expanding only output tree children. That creates a genuinely
exhaustive dependency hierarchy to which a finite-propagation argument
could apply. The number and conditioning of those additional scalar states,
and their actual output errors, still need control. No additional training
is authorized or performed by this assessment.
