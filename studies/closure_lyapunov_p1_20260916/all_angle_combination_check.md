# Post-freeze combination check: every reflection-family separation

2026-09-16. This author-side cross-check was requested after
`all_angles_cone_attempt.md` was frozen. I then read the root candidates
`scalar_margin_extension.md` and `scalar_strict_gain.md`. This is a
post-freeze combination check, not an isolated review or promotion
approval. Original frozen files are unchanged; no experiments were run.

**Conclusion:** both scalar arguments are valid and combine with the
proved initialization lemma to give exact p=1 population-closure
convergence and strictly increased endpoint upper-hidden contrast for
every separation in the specified reflection family. The unproved
cross-sign condition is no longer needed for these conclusions.

## Combined statement

Use the prescribed p=1 Gaussian mark populations, eta=1/4096, canonical
middle contraction, zero initial population readout, actual transpose,
fixed physical metric, and unhalved probability-weighted squared loss.
For

\[
 u_+=(a,b),\quad u_-=(a,-b),\quad
 a\ge0,\quad b>0,\quad a^2+b^2=1,
\]

give the two samples equal mass and labels +1,-1. Their angular separation
is 2 arccos a, ranging over (0,pi]. Define from the current state

\[
 U=\frac{H^2(u_+)-H^2(u_-)}2,\quad
 F=E_2[cU],\quad C=E_2U^2,\quad q=E_2c^2,
\]

and let C_0 be the exact initialized value of C. Then C_0>0 and the
canonical physical trajectory satisfies

\[
 f(u_+)=F=-f(u_-),\qquad 0\le F(t)<1\quad(t<\infty),
\]
\[
 \mathcal L(t)\le e^{-4C_0t},\qquad C(t)\ge C_0,
 \qquad q(t)\le F(t)^2/C_0\le1/C_0.                     \tag{1}
\]

There is a finite fitting limit X_infty, with convergence in the physical
population L2/Frobenius metric and in the stronger bounded-coordinate
characteristic norms. The remaining physical path length obeys

\[
 \int_t^\infty\|\dot X(v)\|_{\rm physical}\,dv
                         \le\sqrt{\mathcal L(t)/C_0}.   \tag{2}
\]

Moreover,

\[
 C(X_\infty)>C_0,
\]

so the squared L2 separation of the actual upper hidden representations
strictly increases between initialization and the fitting endpoint:

\[
 \|H^2_\infty(u_+)-H^2_\infty(u_-)\|_2^2
                  >\|H^2_0(u_+)-H^2_0(u_-)\|_2^2.     \tag{3}
\]

The rate C_0 and the strict increase depend on the pair. Neither a positive
angle-independent rate nor a uniform lower bound on the increase is
asserted near input coincidence.

## Initialization closes the scalar theorem's premise

The frozen initialization result proves B_2(0)>0 for every b>0, where
the initialized upper preactivations are

\[
 Z_\pm=\beta_1B_1(0)\mathbin{\pm}\beta_2B_2(0).
\]

Therefore

\[
 U_0=\tfrac12[\tanh(\beta_1B_1(0)+\beta_2B_2(0))
              -\tanh(\beta_1B_1(0)-\beta_2B_2(0))]
\]

has the strict sign of beta_2 whenever beta_2!=0. The canonical upper
Gaussian mark has probability one of being nonzero. Thus E U_0^2>0.
The sign or subsequent monotonicity of B_1 is not needed. The proof also
includes a=0, so the antipodal endpoint is covered.

## Check of the normalized-readout argument

Reflection symmetry of the exact fixed dictionary and initialization
gives the invariant prediction relation f(u_-)=-f(u_+). Consequently
the physical loss flow is 2(1-F) times the fixed-metric gradient of F.
The autonomous auxiliary flow X_s=grad F has finite-s existence from
the previously established bounded-characteristic estimates. This
continues to be the exact trained closure; it introduces no frozen
features or target-dependent forcing.

Writing h=(w,M), the readout is linear in c and its feature-gradient
velocity is c_s=U(h). Thus exactly

\[
 F_s=K=C+\|h_s\|^2,\qquad q_s=2F,\qquad
                         F^2\le qC\le qK.             \tag{4}
\]

At zero feature time the hidden gradient vanishes because c=0. Therefore
c=sU_0+o(s) and F=sC_0+o(s). In particular F>0 and q>0 at small
positive s; monotonicity of F then keeps them positive thereafter.
For positive s,

\[
 P=\frac q{F^2},\qquad
 P_s=-\frac{2(qK-F^2)}{F^3}\le0,
 \qquad\lim_{s\downarrow0}P=1/C_0.                    \tag{5}
\]

Every denominator and the one-sided initialization limit is justified.
Equations (4)–(5) give q<=F^2/C_0 and C>=F^2/q>=C_0 for every
positive finite feature time. Thus F_s>=C_0, so there is a unique finite
s_*<=1/C_0 at which F=1.

The physical clock s_t=2(1-F(s)) stays below s_* at each finite t and
approaches it as t tends to infinity. Indeed e=1-F solves
e_t=-2K e, and K is continuous, bounded, and at least C_0 on [0,s_*].
This yields (1). The composed solution is the unique canonical physical
solution. Since ||X_dot||=2e sqrt K<=-e_dot/sqrt(C_0), integration proves
(2). The bounded feature-time derivatives also give the claimed stronger
state convergence. Prediction continuity at the endpoint proves fitting.

The argument does not require C_s>=0. It establishes C>=C_0 through
the monotone current-state ratio P. Its singularity at ambient F=0 does
not invalidate the pathwise statement, whose initialized limit is known.

## Check of strict endpoint contrast gain

At initialization, vary only the second active middle row by
m_2 -> (1+lambda)m_2. This is an allowed variation in the same fixed
physical coefficient metric. It changes B_2 to (1+lambda)B_2 and leaves
B_1 and the lower state fixed. Differentiation gives

\[
 \left.\frac{dC}{d\lambda}\right|_{\lambda=0}
 =E_2[U_0\beta_2B_2(0)
       \{\operatorname{sech}^2Z_++\operatorname{sech}^2Z_-\}]>0.
                                                               \tag{6}
\]

The integrand is strictly positive away from beta_2=0 because U_0 has
the sign of beta_2 B_2(0), and both finite gates are positive. Thus the
physical hidden gradient grad_h C(h_0) is nonzero.

The hidden-gradient expansion in the root addendum is justified:

\[
 h_s=DU(h)^*c
      =s\,DU(h_0)^*U_0+o(s)
      =\tfrac{s}{2}\operatorname{grad}_h C(h_0)+o(s).    \tag{7}
\]

In this closure the lower derivative is a finite vector of contractions
E[b phi'(w dot u)(delta w dot u)], and the remaining maps use finite
matrices, bounded marks, and bounded gates. Their operator continuity
along the bounded characteristic trajectory follows directly from these
formulas. Thus (7) does not rely on an unverified global smoothness claim
for an unrestricted L2 nonlinear superposition operator.

By (6)–(7), ||h_s||>0 on some initial positive interval. Since q>0 there,

\[
 qK-F^2=(qC-F^2)+q\|h_s\|^2>0.
\]

Thus P decreases strictly on that interval and remains nonincreasing
afterward. For any s_*>0, integrate over a nonempty subinterval contained
in both (0,s_*) and the interval of strict decrease. It follows that
P(s_*)<1/C_0, even if fitting occurs very early. Finally
C(s_*)>=1/P(s_*)>C_0, proving (3).

## Supersession and remaining scope

For convergence, state convergence, and strict endpoint contrast gain in
this reflection family, the former all-time cross-sign bottleneck is
superseded. Its truth remains an optional structural question; it is
not a premise of the combined theorem. The all-angle initialization proof
remains useful and supplies the sole nondegeneracy premise C_0>0.

Every angular separation is represented by this family, but the theorem
does not yet cover every orientation of a pair at a given separation.
Arbitrary rotations are not symmetries of the prescribed finite
dictionary. Without a valid symmetry reducing the two residuals to one
scalar residual, the actual physical trajectory need not follow grad F,
and (4) does not supply this argument for that trajectory. The generic
oriented-pair target therefore remains open in this combination check.

No full-network identification or closure-order approximation guarantee
is inferred from these exact fixed-order optimization statements.
