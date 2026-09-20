# Uniform fitting over all canonical cyclic three-input orbits

Status: analytic corollary derived after the independently frozen routes
were compared. Its only scientific dependencies are this study's complete
analytic initialization positivity and scalar-clock protection proofs.
No new computation, rotation invariance, or endpoint assumption is used.

Let P cyclically permute three coordinates. For every v in S2, take the
three equally weighted inputs sqrt(3) v, sqrt(3) Pv, sqrt(3) P^2v, all
with label +1. Simultaneously negating any selected input and its label
preserves the exact loss and full dynamics, so mixed binary labels are
allowed in this precise sense. Repeated inputs at fixed points of P are
compatible duplicates; noncollapsed independent triples form a subfamily.

There is a constant k_*>0 depending only on the canonical d=3,p=1
initialization, independent of v, for which every such initialized flow
satisfies

  L'(t)<=-4k_* L(t), L(t)<=exp(-4k_*t),

and converges to an actual bounded fitted state. The bounded-state constants
can also be chosen uniformly over these cyclic orbits. This statement does
not extend the independent-perturbation theorem beyond the small-opening
family already proved in protected_family.md.

## Complete argument

The initialization positivity theorem gives

  z(v)=D a_0(v)=(T(v_1),T(v_2),T(v_3)),

where T is continuous on [-1,1], odd, and T(r)>0 for r>0. Since v is
unit, at least one component is nonzero, so z(v)!=0. The cyclic symmetry
of the exact marks and D gives z(P^jv)=P^jz(v). Define

  m_v(B)=(1/3) sum_(j=0)^2 phi(B^T P^j z(v)),
  k(v)=E2[m_v(b2)^2].

For any nonzero z, this averaged function cannot vanish identically on
the open cube supporting the upper mark law. If the coordinates of z
have nonzero sum, its linear Taylor term at B=0 is nonzero. Otherwise
the nonzero linear forms l_j(B)=B^TP^jz satisfy l_0+l_1+l_2=0, and

  l_0^3+l_1^3+l_2^3=3 l_0 l_1 l_2

is a nonzero polynomial. Since phi(t)=t-t^3/3+O(t^5), the cubic term
of m_v is then nonzero. In either case m_v is nonzero at a point inside
the cube and, by continuity, on a nonempty open subset. The upper mark
law has strictly positive density there, so k(v)>0 for every v in S2.

The map v->z(v) is continuous by dominated convergence, and so is k(v),
since |m_v|<=1. Compactness of S2 therefore gives the explicitly defined
positive constant

  k_* = min_(v in S2) E2[( (1/3) sum_(j=0)^2
                     phi(b2^T P^j D a_0(v)) )^2] >0.

This definition uses only fixed initialization Gaussian expectations and
the compact sphere, not a future trajectory or fitted endpoint. The exact
coordinate-permutation symmetry makes all three predictions equal on each
trajectory. The scalar-clock theorem then gives F_s>=k(v)>=k_* and fitting
at s_*<=1/k_*. Its finite-clock polynomial state bounds are uniform because
the input norms, feature envelopes and D are fixed. Transforming back to
physical time proves every claimed conclusion.

## Which near-edge geometries this excludes

In the opening parametrization of protected_family.md, this result holds
for the whole interval 0<=theta<=pi/2, with a single positive rate.
Every interior 0<theta<pi/2 has three independent inputs. At theta=0 the
three label-oriented directions coincide. At theta=pi/2 they lie in a
plane at pairwise angle 120 degrees and sum to zero; even there, their
averaged nonlinear upper feature is nonzero by the argument above.

After folding labels to (+,+,-) in the latter case, x_3=x_1+x_2 and
sum_i p_i y_i x_i=0. No linear predictor can fit those three labels:
linearity would require f(x_3)=f(x_1)+f(x_2)=2 rather than -1.
The exact initialized nonlinear p=1 closure nevertheless fits at the
uniform rate just proved. Thus vanishing label-weighted first input
moment and singular input Gram do not themselves obstruct this closure.

Equal weights with mixed three labels are unbalanced (class masses 2/3
and 1/3). The zero-moment endpoint is a dependent triple and is identified
as such; the entire nearby interior remains independent. No arbitrary
rotation of this coordinate-specific construction is asserted.
