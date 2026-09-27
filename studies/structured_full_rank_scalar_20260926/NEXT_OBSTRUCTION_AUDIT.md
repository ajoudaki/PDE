# Internal audit of the persistent selective-feedback obstruction

2026-09-27. Same-study cross-check of `NEXT_OBSTRUCTION_ROUTE.md`, its exact
block-model equations, the relevant compiler functions in
`true_aggregate_ode.py` and `true_aggregate_selective.py`, and the two
existing result reports quoted for alias gaps. No numerical experiment,
training, source-code edit, or symbolic-code execution was performed. This is
an author-team audit, not an independent promotion review.

**Verdict.** No material mathematical defect found in the stated scope.
The permanent pure-first-layer omissions, the exact retained-row residual,
its positive Gaussian small-time coefficient, and the uniform-in-J lower
bound for the twelve specified coordinates check. The note correctly does
not turn that joint moment lower bound into an output-only lower bound.

## 1. Permanent omission and the retained row

The inspected `graft` function retains every old formal vertex and edge,
removes one decoration, and adds the local replacement decorations and
fresh child vertices. `canonical` only changes the root and branch order.
Consequently, starting at an output with a second-layer vertex, no number
of these local derivative steps produces a tree containing only a single
first-layer vertex. Coefficient-field derivatives are not included by the
selection's descendant enumeration. This distinction matters.

For m=H=1, the fixed feedback seed s=<beta x> and its derivative contain
pure first-layer monomials x^2, beta x, and beta^2 x^r for r=0,2,4. The
protected derivative of <x^2> adds beta x^r for r=1,3,5. The remaining
protected fields and second-layer Gram moments have a second-layer vertex,
which their derivatives preserve. Thus beta^3 x^3, beta^3 x^5 and
beta^3 x^7 are absent for every output depth J with dependency_depth=0,
whereas q=<beta^2 x^4> and b=<beta x^5> are retained.

The claim that all six U_(r,e) occur by J=2 also checks. The first output
derivative contains one-edge trees with root decoration zeta h^e,
e=0,2, and first-layer decoration beta x^4. Their coefficients come from
the G x' term and the memory part of x', and are not identically zero.
Differentiating one of the four x factors by that same memory term gives
beta^2 x^3(1-x^2)^2 at the existing first-layer vertex. Its expansion has
precisely r=3,5,7, with nonzero coefficients. Hence all six desired trees
are included after two output-descendant steps. No new pure-first-layer
beta^3 tree is thereby created because the existing second vertex remains.

The direct product rule is

    q'=2<beta beta' x^4>+4<beta^2 x^3 x'>.

The beta term is 2 sigma(b-q). The transpose term in x' contributes

    -16 L^2 R E[k^(-1) sum_(i,gamma)
           beta_i^2 x_i^3(1-x_i^2)^2 G_(gamma i)
                              zeta_gamma(1-h_gamma^2)].

Since U uses k^(-2) and G/Gscale, this is exactly
-16(k Gscale)L^2 R U_combination. The factor is k Gscale, not Gscale
and not k^2 Gscale. The memory contribution is exactly

    eta=32 L^4 R tau <beta^3 x^3(1-x^2)^2>.

The combination coefficients of U are 1,-1,-2,2,1,-1, with absolute sum
eight. Thus the retained-row absolute envelope is
(4+128 k Gscale L^2) sigma, matching the implemented row-envelope penalty.
There is no overlooked pure-first-layer child in this q row.

## 2. Small-time coefficient on the actual Gaussian orbit

The source correctly uses bounded ratios instead of asserting analyticity
of an unbounded-mark flow. At time zero R=-y, h=h_0, zeta=alpha=0,
beta=x_0 and L=1. Integrating the two normalized equations yields

    zeta(t)/t -> y h_0,
    alpha(t)/t^2 -> -y^2 h_0(1-h_0^2).

The factor two in alpha'=2R zeta(1-h^2)-2sigma alpha disappears upon
integrating the leading term proportional to t. The clock and memory
bounds provide deterministic bounds on these ratios near zero, so their
products pass through expectation by dominated convergence. Therefore

    tau(t)/t^3 -> -y^3 kappa,
    kappa=<h_0^2(1-h_0^2)^2>,
    <beta^3 x^3(1-x^2)^2> -> mu
          =E[tanh^6 Z(1-tanh^2 Z)^2].

For a unit training input, w_i dot u is N(0,1). Conditional on x_0,
each component of Gx_0 is a centered Gaussian with variance
k^(-1)sum_i x_(0,i)^2, which is positive almost surely. Hence both kappa
and mu are strictly positive. Their product in eta is valid without an
independence assumption: tau and the first-layer moment are already two
separate scalar population averages. Finally R tends to -y, giving

    eta(t)/t^3 -> 32 y^4 kappa mu >0.

The sign, the fourth power of y, and the order t^3 all check.

## 3. The uniform-in-J twelve-coordinate lower bound

The set contains eleven moments: q, b, six U coordinates, F, v_0 and v_2;
including L gives twelve coordinates. All occur by J=2 and the selected q
row depends only on them, regardless of any other retained descendants.

At initialization q=b=E tanh^6 Z lie strictly inside (-1,1), and the other
nine moments vanish. Their exact continuations are continuous. For U this
uses one integrable Gaussian mark times bounded dynamic factors. Thus a
single small T_0, independent of J, makes clipping inactive on the exact
fixed coordinates. It need not make all exact Gaussian tree moments lie
in the clipping cube, which would be false at sufficiently high degree.

For the approximate fixed coordinates, their own row-envelope penalties
make [-2,2] invariant because they start inside that interval. Other
high-degree Gaussian initial moments can be larger without invalidating
this invariant region: all RHS child values and field inputs are clipped.
For each finite J those other coordinates are finite initially and have
bounded-forcing, inward-linear-penalty equations on compact time intervals.
Thus their presence does not prevent the fixed-row comparison.

Set B=2+|y|, M=exp(BT), a=k Gscale, and use the maximum norm on the twelve
coordinates. On |q|,...,|v_2|<=2 and 1<=L<=M,

    |R|<=B,   Lip(R)<=B,
    |U_combination|<=8,   Lip(U_combination)<=8.

The first term 2 sigma(pi(b)-pi(q)) has Lipschitz bound 8B. For the edge
term, differentiating the L^2 R coefficient and the U combination gives
256 a B(M^2+M). For the penalty, |q-pi(q)|<=1 and its Lipschitz constant
is one; the resulting bound is 8B+256 a B(M^2+M). Adding them gives exactly

    C_T=B[16+512a(M^2+M)].

The clock bound applies to both the exact and approximate trajectories
since L'=|R|L and |F|<=1 physically or after clipping. All bounds used in
C_T are independent of J.

Since eta(t)>=16y^4 kappa mu t^3 on a sufficiently small fixed interval,
its time integral is at least 4y^4 kappa mu T^4. Integrating the exact and
selected q rows from the same q(0), then using the Lipschitz bound, gives

    4y^4 kappa mu T^4
       <=|q(T)-qhat(T)|+C_T integral_0^T ||K-Khat||_infinity
       <=(1+TC_T)E_J(T).

This proves the advertised floor. With initial q error delta, subtracting
delta before taking the positive part is the correct modification.

This is a lower bound for the exact-Gaussian-initialized mathematical
extension of the selected ODE. The source code's ordinary pool initializer
checks a bounded mark support; it is not itself a Gaussian quadrature
initializer. The note explicitly changes only the theoretical initial
expectations for this obstruction and does not claim a new experiment.
That distinction should remain visible in any synthesis.

## 4. Output scope and the saved alias gaps

The internal moment lower bound does not establish that f alone stays
inaccurate. Its proof allows errors in q, b, U, v_0, v_2 or L to account for
the discrepancy while selected outputs remain accurate. The note states
this limit and does not assert the missing propagation theorem.

The separate alias bound

    max(|p-f|,|z-f|)>=|p-z|/2

is the triangle inequality for two scalar predictions at the same time and
input. The reported alias gaps 0.52853, 0.23706 and 0.05088 occur in the
two inspected existing reports. Their halved values are 0.264265, 0.11853
and 0.02544, subject to the reports' rounding. This does not choose the
more accurate decoder and does not bound the passive-only error.

One minor wording refinement was sent to the author: qualify “the training
inputs lie on the circle” as applying to the saved tasks, since the general
model also permits interior disk inputs. The exact same-input alias
inequality itself does not require a circle and is unaffected.

## 5. Conclusion of this internal check

The fixed feedback boundary is a valid witness-specific obstruction to
joint convergence of the stated twelve aggregates as output depth alone
increases. It leaves open both output-only convergence of that family and
the effectiveness of a hierarchy which expands every feedback dependency.
It is fully compatible with the separate Gaussian/full-circle existence
construction. No new training run is needed for these logical conclusions.
