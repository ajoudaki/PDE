# C-H3 portfolio comparison

Coordinator synthesis, 2026-09-12. Status: bounded attempt closed; the full
milestone is incomplete. The three first-route files were frozen before this comparison.
Their observations are candidates, not accepted canonical additions.

## Common target and decisive obstacle

The target is the exact C.4.7.9 population GF at physical T=1/200, with the
same two Gaussian action orientations and joint population interpretation.
H2 is already promoted. No finite-network initialization is changed here.

H2's source (H2.10) is evaluated on an unavailable exact trajectory. Its
compactness proof gives convergence but cannot itself certify the result of
a finite computation. A useful H3 implementation must replace that premise
by a computable order rule or by a rigorously computable defect and a proved
comparison estimate. Comparing numerical resolutions does neither.

## Three materially different routes

| Route | Mechanism actually investigated | What it supplies | What remains |
|---|---|---|---|
| A priori dictionary | Saturated Euler circuits, a full coefficient-box cover, bounded initialized words and H2 ridge filters | A constructive way to replace target-dependent compact covers; full-covariance square-root and Gaussian quantization bounds | Complete constants, recursive certified compiler and useful storage/cost; the literal cover is very large |
| A posteriori residual | Lift a finite represented H2 state to the same base A0; evaluate new initialized action programs on that state; compare with cutoff-menu stability | A target-free stopping criterion and a proposed Bernstein representation with a qualitative eventual-acceptance argument | Implement and validate the recursive action/defect producer, including singular joint Gaussian laws, population and input integration; quantify cost |
| Short-time Duhamel | Frozen initialized feature kernel with a finite integral remainder for w,K,c; exact finite source contractions for motion | A finite closed formula with a potentially useful rigorous error bound at this horizon | A fixed-order error floor; further accuracy does not follow by tightening its quadrature |

These are different mechanisms, not three resolutions of one simulation.
No route supplies a complete tested arbitrary-accuracy solver by itself.
The residual route may use the improved common-carrier stability lemma below;
that does not create the missing defect producer.

## A component obstacle that was removed

The coordinator's `H3_stability_proof.md` closes the existing causal source cap
at T=.005 using exact rational constants. The script proves a beta-row cap
1/32, a backward-response shift at most .031251031, and a marginal Gaussian
tail at cutoff .2 below 1.16e-16. The same-base raw comparison constant is
L=8.2608 in the specified ball. Thus a SUPPLIED full RHS defect 1e-5 and zero
initial error would imply terminal raw error below 5.105e-8.

The exact script was executed and independently checked by a nonauthor after
its own route was frozen. That audit is an internal component check, not an
isolated promotion review. The calculation is conditional on a defect and
approximate-state bounds; no actual path is certified by this scalar result.
The source cap uses the established named-source recursions, not temporal
analyticity, an independent reverse action, or a Stieltjes representation.

## Two-dimensional reference symmetry

For the preregistered orthogonal two-atom reference, the short-time source
contractions reduce further than generic tensor quadrature. Let

    h_i=tanh(g_i), l_i=1-h_i^2, q=E h_i^2,
    z_i=A0 h_i, H_i=tanh(z_i), s_i=1-H_i^2, H=H_1-H_2.

The z_i are independent N(0,q). Put m_j=E s_i^j, v=1-m_1,
a=3m_2-2m_1, k=m_1^2. The true reused reverse action satisfies

    P_1=A0*(s_1 H)=zeta_1+a h_1-k h_2,
    Var(zeta_1)=m_2(1+v)-m_3.

This follows by taking the frozen named derivatives of s_1(H_1-H_2):
E partial_(z_1)=m_2-2E[H_1^2 s_1]=a and
E partial_(z_2)=-E s_1s_2=-k. Its centered source is independent of g.
It does not make the output P_1 independent of g.

Define L_2=E l_1^2, L_4=E l_1^4, J=E l_1^4 h_1^2,
J_2=E l_1^2 h_1^2 and

    V=[m_2(1+v)-m_3]L_4+a^2 J+k^2 q L_4.

Then V=E[l_1^4 P_1^2]. For b'=1-vb,b(0)=0, the leading paired first
activation motion is b^2 sqrt(V)/2. This is a statement about the leading
initialized field; a bound on its difference from the actual GF motion is
separately necessary.

The corresponding forward query U_1=A0(l_1^2 P_1) has decomposition

    U_1=xi+L_2 s_1 H,
    Var(xi)=V,
    Cov(xi,z_1)=c_1=a J_2,
    Cov(xi,z_2)=c_2=-k L_2 q.

The unbounded operand is interpreted in L2, by bounded smooth saturation of
P_1 followed by its limit. Gaussian moments and bounded gate derivatives
justify the frozen derivative limits; operator norm <=2 justifies the action
limit. Only its own reverse slot has a nonzero formal derivative. Singular
covariances are retained rather than discarded.

With lambda=q+L_2, conditioning xi jointly on z_1,z_2 shows that the squared
factor for the leading paired second activation motion is

    F=V m_2+(c_1^2/q^2)(E[z^2 s^2]-q m_2)
      +2 lambda[(c_1/q)E[z s^3 tanh(z)]
                -(c_2/q)m_3 E[z tanh(z)]]
      +lambda^2[m_4(1+v)-m_5].

Thus the leading motion is b^2 sqrt(F)/2. All displayed integrals are one
dimensional. Conditional residual variance is nonnegative by the exact
joint Gram; it cancels algebraically from the displayed contraction. The
agent independently derived and implemented the same formula before the
coordinator sent this check; the agreement is disclosed, not presented as a
fresh isolated review. Numerical quadrature and nonlinear remainders still
require their own certificates.

## Scope of an unsuccessful completion

If only the scalar stability and fixed-order reference computation survive,
the failure concerns the presently implemented numerical closure and its
general refinement/certification interface. It does not refute H2 convergence
or prove a lower bound against all autonomous closures. In particular, the
residual route remains a possible constructive route rather than an
impossibility argument.

An effective positive-radius family inside H2 is a distinct obligation. H2's
existential law radius cannot be replaced by a convenient decimal. Nor does
the new all-finite-law short-time source cap automatically prove that a
specified perturbed law lies within the original H2 neighborhood.

Final execution, reproduction, review outcomes and promotion disposition are
recorded in [H3_assessment.md](H3_assessment.md). The bounded reference succeeds
at its preregistered accuracy; full C-H3 remains incomplete. The existing book
and maintained code have not been changed by this attempt.
