# Current result: exponential decay survives unequal input angles

2026-09-16. Internal research, not promoted. This supersedes the prior
statement that no unconditional perturbed-family extension had been proved.
It does not supersede the open status of arbitrary three-input circle data.

## Main theorem

The complete proof is `resolution_open_family.md`; its unchanged frozen
version passed the fresh isolated complete review in
`resolution_open_family_review.md`. Retain the exact canonical
initialized p=1 population closure in dimension three and equal data weights.
Labels are exactly (+1,+1,-1), with no small-label assumption. Let

    v_i(e)=(1+e e_i)/sqrt(3+2e+e^2),  0<e<e_0.

There is e_0>0, and for each such e a positive input radius delta(e), such
that EVERY triple of unit directions with

    |u_1-v_1(e)|<delta(e),
    |u_2-v_2(e)|<delta(e),
    |u_3+v_3(e)|<delta(e)

has the following all-time properties from prescribed initialization.
Physical inputs are sqrt(3)u_i. This is an open set in (S^2)^3, so it
contains triples with all pairwise angles unequal and no symmetry.

Define from the actual current second-layer fields and readout

    U=(H_1+H_2-H_3)/3, F=E2[c U], q=E2[c^2],
    C_0=E2[U_0^2]>0,
    Phi=L [1+C_0(1+q)/(C_0+F^2)].

Here C_0 is a fixed Gaussian initialization expectation for the actual data.
Then some lambda(e)>0, uniform on the specified neighborhood, satisfies

    L<=Phi, Phi(0)=2, Phi_dot<=-lambda(e)Phi,
    L(t)<=Phi(t)<=2 exp(-lambda(e)t).

The probability-normalized full tangent Gram also satisfies K>=k(e)I>0
throughout the initialized trajectory. In fact L<=exp(-4k(e)t), and the
remaining physical path length is at most sqrt(L(t)/k(e)). Thus both
population laws and the full middle matrix converge to a fitting state.

The quantitative addendum `resolution_rate.md` proves the sharp seed
conditioning order c_- e^2<=mu_e<=c_+ e^2, with fixed positive constants.
Its separate complete follow-up review `resolution_rate_review.md` passes
without repairs.
The open family can therefore use k(e)>=c_- e^2/2, and a mixed-potential
rate at least a positive constant times e^2. This quantifies deterioration
of independent correction directions at coalescence. It does not quantify
delta(e), or assert that the symmetric scalar residual decays that slowly.

This is a complete unconditional LOCAL extension to nonsymmetric geometries
with the original unit labels. It is not a proof for every arrangement, a
numerical example, an assumed entry condition, or a change of optimizer.

## What made the proof work

1. The auxiliary compatible coincident configuration has all signed inputs
   v_*=(1,1,1)/sqrt(3). Its upper preactivation is p(s)(Z1+Z2+Z3), with
   p(0)>0. The exact all-layer equations prove p is nondecreasing. The
   accumulated readout has the sign of Z1+Z2+Z3; hence its common backward
   response divided by s has a strictly positive continuous extension to
   s=0, and a positive minimum on any fixed finite auxiliary interval.
2. Nearby distinct permutation seeds inherit that nonzero backward response
   and a nonzero common middle-matrix component. Their three input vectors
   are linearly independent. The first-layer Gram therefore remains positive
   in every output direction for s>0. The exact initialized upper Gram
   supplies positivity at s=0. Compactness produces a positive minimum over
   the complete finite auxiliary interval containing the fitting point.
3. Finite-time input dependence moves nonsymmetric nearby problems into a
   small-loss neighborhood of the seed curve. Full tangent coercivity there
   makes the remaining physical length smaller than the neighborhood radius.
   A first-exit contradiction proves all-time trapping. No finite-horizon
   comparison is extrapolated to infinity without this extra argument.
4. The mixed potential has strict derivative margin on a finite reference
   interval, which persists under input perturbations. In the remaining
   small-loss region its multiplier's exact derivative is O(sqrt(L)), while
   loss has a fixed exponential dissipation bound. This proves decay of
   Phi from time zero, retaining every derivative term.

The coincident configuration is only a proof reference. Every admitted
actual data triple is distinct and nondegenerate. Neither that reference
trajectory nor an unknown endpoint occurs in the potential's formula.

## Geometric meaning

The first layer contributes

    E1 |sum_i z_i sech^2(w.v_i) Q_i v_i|^2
      >=lambda_min([v_i.v_j]) sum_i z_i^2
                              E1[sech^4(w.v_i)Q_i^2].

This explains how reverse response and input geometry jointly protect
independent directions of output correction. Forward upper activations
need not maintain their initial pairwise separation. The loss and the mixed
potential give fitting, while finite physical path length supplies an
additional statement about the complete hidden state.

The potential measures mismatch weighted by current readout size relative
to its signed average prediction. Its multiplier is allowed to increase
on nonsymmetric trajectories; the proof bounds that increase against loss
dissipation. It does not require same-class contraction or different-class
expansion to be separately monotone, or select a unique hidden endpoint.

The previously proposed inverse-tangent correction remains a legitimate
current-state geometry with its exact moving-metric derivative. Its stronger
matrix differential inequality is not proved and is not required here.
It should not be reported as an unconditional potential theorem.

## Independent routes and remaining boundaries

The two orthogonal routes independently derived the same further fact:
every possible rank-loss time of the orthogonal auxiliary curve is isolated,
and its transverse eigenvalue vanishes quadratically. A third route obtained
local finiteness by proving time analyticity in the bounded-increment Banach
space. These routes were compared only after their reports were frozen.
Their generic-amplitude consequences are secondary results: they do not
establish that the unit-amplitude orthogonal endpoint is regular.

| Claim | Status and scope |
|---|---|
| Mixed exponential potential for an open nonsymmetric family with unit labels | Proved in the d=3 canonical closure; resolution_open_family.md |
| All-time full tangent coercivity and full-state convergence for that family | Proved in the same theorem |
| Finitely many orthogonal rank-loss times on each compact auxiliary interval | Independently derived in resolution_endpoint.md and resolution_positive.md; root checked |
| Nonsymmetric open families for all but locally finitely many common label amplitudes near the orthogonal reference | Secondary theorem in resolution_metric.md; root checked, no fresh independent audit of this whole secondary report |
| Unit-label orthogonal endpoint is nondegenerate | Still open |
| Arbitrary nonsymmetric three-input geometry, especially the canonical d=2 circle | Still open |
| Necessity of equal-angle symmetry for learning | Not established; the new open-family theorem removes this restriction locally |
| Initialized failure-to-fit example for compatible generic data | None constructed |

For arbitrary geometry, the missing ingredient is an all-time response or
capture estimate that prevents the loss-carrying directions from becoming
ineffective. Neither initial rank nor the loss identity supplies that
estimate. The present theorem proves it on a genuine open family but does
not justify extending its positive neighborhood across every input geometry.
No numerical experiment was run in this continuation; nothing was promoted.
