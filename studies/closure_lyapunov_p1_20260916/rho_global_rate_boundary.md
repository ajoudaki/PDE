# A global boundary on geometry-independent rates

2026-09-16. Author-side exact corollary of the complete finite-horizon
continuity and initialization calculation in `sphere_second_variation.md`.
No experiment, global failure-to-fit example, or promotion is claimed.

Use the canonical d=3, p=1 initialized closure with equal masses, labels
(+1,+1,-1), and signed unit inputs v_i=y_i u_i. Write m_i=f(v_i),
L=(1/3) sum_i(m_i-1)^2 and

    C0(v)=E2[(H1^0+H2^0+H3^0)^2]/9,
    Phi=L[1+C0(1+E2 c^2)/(C0+F^2)], F=(m1+m2+m3)/3.

The finite-horizon response proof establishes continuity in the full
six-dimensional data space, C0>0 for every triple, and Phi(0)=2. In
particular, compactness gives min C0=c_min>0 on (S^2)^3.

**Claim.** The symmetric-family decay rate 4C0 cannot hold for this Phi
on every distinct, non-antipodal signed triple. More generally no positive
geometry-independent exponential rate with a geometry-independent initial
bound and loss comparison can cover all such triples.

**Proof.** Fix a unit vector v and first take the limiting signed triple
(v,v,-v). At every state the predictor is odd, so its signed outputs are
(z,z,-z), where z=f(v). Thus, exactly,

    L=[2(z-1)^2+(-z-1)^2]/3=(z-1/3)^2+8/9 >= 8/9.

For the original fixed labels this limiting triple has u1=u2=u3=v, so
the positive loss is caused by contradictory labels on identical inputs.
It is not asserted to be an admissible fitting problem.

For any prescribed finite T, finite-horizon dependence gives an open
neighborhood of this limiting triple on which L(T)>7/9. That neighborhood
contains triples whose three physical directions are distinct and have no
antipodal pair, and even triples whose three signed vectors are linearly
independent. For example use small independent tangential perturbations
of the first two occurrences of v while keeping the third near -v.
There are then no contradictions forced by equality or oddness of inputs.

If the proposed inequality Phi(t)<=2 exp(-4C0 t) held on all these
nondegenerate triples, choose a finite T with

    2 exp(-4 c_min T)<7/9.

The loss comparison L<=Phi would contradict the preceding continuity
bound for sufficiently close nondegenerate triples. A fixed positive rate
lambda and common initial bound P yield the same contradiction by taking
P exp(-lambda T)<7/9. More generally the argument applies to a common
increasing comparison L<=psi(Phi), psi(z)->0 as z->0, with a common
initial upper bound. End of proof.

The conclusion is loss of a uniform rate near incompatible data, not
infinite convergence time for a fixed compatible geometry, and not
nonexistence of a geometry-dependent potential. The user permits
geometry-dependent rates. This corollary therefore explains a necessary
feature of a possible global theorem; it does not refute the requested
theorem. It also shows why positive C0, even uniformly positive C0, cannot
by itself control the two independent disagreement directions globally.
