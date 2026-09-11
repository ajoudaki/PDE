# Gaussian expectation calculus route (coordinator candidate)

Status: exact finite-dimensional identity below; mesh-uniform neural sensitivity
bound remains a candidate, not an established conclusion. This file records a
structurally different route from ambient raw-state differentiability.

## Why scalar output derivatives may suffice

The desired influence lives in H=L2(circle). A well-posed raw L2 tangent is a
sufficient construction, but is not the only possible usable characterization.
One can instead differentiate the exact finite Gaussian Euler-program output,
including all residual feedback, source covariances and named coefficients,
and prove convergence of these output derivatives as the mesh is removed.
No finite-network tangent theorem is needed for the requested width-first bridge.

The candidate analytic estimate is: for every sufficiently fine population raw
Euler mesh through T=40 and every finite law in one fixed smaller C.4.7 ball,
the first and mixed second derivatives of its whole-circle scalar output in
finite signed zero-mass law directions obey

    ||D F_h(lambda)[sigma]||_H <= C ||sigma||TV,
    ||D² F_h(lambda)[sigma,tau]||_H <= C ||sigma||TV ||tau||TV.

The constant must be independent of mesh, support cardinality, nonzero masses
and covariance rank. Derivatives are only required along probability-law
segments/rectangles where they are defined. This estimate is NOT yet proved.
The separate replacement route investigates its statistical sufficiency.

## Exact covariance differentiation without inverse Grams

Let C(a) be a twice continuously differentiable finite positive-semidefinite
covariance matrix along an interval and let q(a,x) be twice differentiable in a
and four times in x. Assume every derivative used below is bounded by a fixed
polynomial in |x|, uniformly on the parameter interval. With G_a centered
Gaussian of covariance C(a), put M(a)=E q(a,G_a). Then, including one-sided
endpoints,

    M' = E q_a + (1/2) sum_ij C'_ij E q_ij,
    M'' = E q_aa + sum_ij C'_ij E q_aij
           + (1/2) sum_ij C''_ij E q_ij
           + (1/4) sum_ij,kl C'_ij C'_kl E q_ijkl.

Here q_a means explicit parameter differentiation holding the source coordinates
fixed; covariance differentiation is the separate displayed contraction.

Proof: first replace C by C+eta I, eta>0. The Gaussian density has Fourier
transform exp(-t^T C t/2), so its parameter derivative is
(1/2) sum C'_ij partial_ij of that density. This identity can alternatively be
checked directly from the density and the inverse-matrix derivative formula.
Two integrations by parts give the first formula; polynomial growth makes
the boundary terms vanish. Differentiate once more and apply the same formula
to q_a and q_ij to obtain the second formula with the indicated coefficients.
For each eta these formulas are valid on compact parameter subintervals.
As eta decreases to zero, couple G_{a,eta}=G_a+sqrt(eta)N at each fixed a.
Uniformly bounded covariance matrices give uniform moments of every fixed order;
the derivative expressions thus converge in expectation, uniformly in a by
compactness and continuity. Integrate the first and second derivative formulas
on a parameter interval and pass to the limit. The fundamental theorem of
calculus then gives both asserted derivatives for singular C as well. No
derivative of a covariance square root or inverse limiting Gram is used.

The same proof handles several independent source groups by treating their
joint covariance as block diagonal, and handles independent roots by conditioning
and an integrable polynomial envelope. Exponential-linear Gaussian envelopes
also suffice when a common Gaussian exponential moment dominates them.

The dimension-free bound is obtained by using the entry supremum norm of C'
against the sum of absolute expected source derivative entries. For example

    |sum C'_ij E q_ij| <= max_ij |C'_ij| sum_ij E|q_ij|.

Consequently a fixed-program formula alone is insufficient: the absolute
source-tensor sums must be controlled uniformly as the number of slots grows.

## Candidate causal estimate and exact unresolved step

C.4.7.N2–N8 supply the exact finite source recursion. For law masses p_a and
signed changes s_a, the update weight gamma_ka=-2 h_k p_a r_ka has derivatives

    gamma'_ka = -2 h_k (s_a r_ka + p_a r'_ka),
    gamma''_ka = -2 h_k (2 s_a r'_ka + p_a r''_ka).

The initialized action and actual transpose are represented by both source
groups and their response corrections; none may be dropped. The covariance
derivatives must also be retained, for instance

    d E[xi_i xi_j] = d E[H1_i H1_j],
    d E[zeta_i zeta_j] = d E[Delta2_i Delta2_j].

A possible induction uses source derivatives through order five, because two
law derivatives of an expected first source derivative invoke fourth source
derivatives of that first derivative. Under N-cap, lower frozen-source pulses
have all finite moments by N11–N13, while upper first-source rows have pointwise
bounds by N15. Higher derivatives require a new induction, not a citation to
those first-order estimates.

The essential estimate must retain time weights. Lower derivatives with respect
to named reverse sources are injected through h_s p_b. Upper derivatives have
a direct current source of unit weight, while old sources enter via memory.
Repeated differentiation at the SAME old upper source can retain only one
h_s p_b factor: an old readout term h_s p_b phi(xi_sb) has kth source derivative
h_s p_b phi^(k)(xi_sb), not (h_s p_b)^k. Any proposed tensor norm must allow
this diagonal case.

After treating current sources in chronological forward-then-reverse order,
one needs an actual bound of the form

    E1_k <= C (1 + sum_{j<k} h_j E1_j),
    E2_k <= C (1 + sum_{j<k} h_j E2_j),

where E1 includes first residual, covariance and coefficient sensitivities,
and E2 includes their second sensitivities after the first bound is fixed.
The norms must sum absolute coefficient rows with their source masses rather
than divide by a minimum atom weight. The constant must not depend on k.

It is NOT enough to obtain E_k<=C(1+max_{j<k}E_j); iterating that bound can
grow exponentially in the number of steps at fixed physical horizon. Nor is
it enough to bound a covariance derivative by a source tensor sum with an
unweighted maximum over all old times. These are the exact estimates still
requiring proof or refutation before this route can resolve A–C.

## Conditional mesh passage

If the displayed second law derivative bound holds, C.4.7's uniform value
completion gives output derivative convergence. On a smaller ball every atom
contamination segment of a common positive length is admissible. For meshes
h,h' and such a unit direction, a forward difference quotient at epsilon has
derivative errors at most C epsilon and difference at most
2 sup||F_h-F_h'||/epsilon. Choose epsilon proportional to the square root of
the value error. This proves uniform Cauchy convergence of the first output
derivatives, and agreement with the actual contamination derivative of F.
Centering then follows from linearity and the zero direction, provided the
atom integral representation is passed from the finite programs. Weak-law
continuity follows from uniform derivative approximation by their continuous
finite-program counterparts. These passages require the unproved analytic
bound above and are not a completed neural theorem.
