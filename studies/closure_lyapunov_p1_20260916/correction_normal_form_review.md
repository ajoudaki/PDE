# Isolated review of the current-state normal-form correction

2026-09-16. Independent mathematical review of the complete frozen candidate
`correction_normal_form.md`, SHA256
`0344d4526096580cb994b99dddb5b7ab4af8db3049ec7c34fc6abe1fccd4383e`.
No experiments, candidate edits, promotion, or inspection of other research
directions were performed.

**Verdict: PASS within the stated local-residual/current-state scope.**
The finite homological construction, exact quintic remainder, uniform local
bounds, positivity and decay constants, and current-state trapping theorem
are valid. I found no blocking mathematical defect. Two small formal
clarifications are recorded below. This result does not establish initialized
capture for the broad input family or control at singular tangent Grams.

## 1. Inputs and exact scope

I read the complete candidate, `docs/NOTATION.md`, `docs/observable_p1.md`,
the canonical C.4.7.9 state/dynamics/well-posedness material and relevant
C.4.7.10 B/C.1/D.3 definitions and existence material, and the complete
same-study `perturbation_modes.md`, `perturbation_metric_template.md`, and
`sphere_second_variation.md`. Required mathematical and conjecture-audit
skills were applied. References to additional study artifacts were not
followed. No README, prior review, other route, or other study was read.

The object is the exact fixed-order population closure on its frozen mark
spaces, with three signed unit inputs, full evolving middle matrix and its
actual transpose, physical population-L2/Frobenius metric, and the unhalved
mean-square loss. The correction uses current-state integrals and finite
linear systems. It supplies no extra evolving variable, future trajectory,
or fitting endpoint. Its finite coefficient count does not turn the
underlying continuum populations into finitely many scalar coordinates;
the candidate does not make that stronger claim.

The reference to previously proved regular-endpoint families at candidate
lines 210–212 has no specified endpoint theorem among the assigned inputs.
I therefore do not independently certify which families have that property.
The implication from convergence to a regular fitting endpoint to eventual
entry into this certificate is valid, as explained in Section 5 below; this
dependency limitation does not affect the new local construction.

## 2. Algebra, factors and exact remainder

The displayed gradients have the correct three blocks and probability
normalization. If J maps a physical increment h to
`(<j_i,h>)_i`, then K=JJ*, grad L=2J*xi and

    X'=-2J*xi,    xi'=-2Kxi,    L'=-4 xi^T K xi=-||X'||^2.

All matrices in these formulas are those of the canonical closure.
Writing R=K^(-1), directional inverse differentiation gives

    D_j R=-R(D_j K)R.

Consequently the sign and factor two of the cubic term in candidate (3)
are correct.

It is essential, and correctly stated, that z be held independent of X in
B. With that convention, the ordinary chain rule along the characteristic
curve gives exactly

    d p(X,xi(X))/dt=(B p-A_K p)(X,xi).

On homogeneous degree m>=1 symmetric tensors, A_K is the self-adjoint
operator `2 sum_(r=1)^m K_(r)`. Its eigenvalues are precisely the displayed
`2 sum_i alpha_i k_i`. Thus K>=mu I gives
`||A_K^(-1)||<=1/(2m mu)` in the invariant Frobenius tensor norm, with no
condition on eigenvalue multiplicity. The dimensions for degrees three and
four in three variables are 10 and 15. Finite matrix inverse
differentiation is valid at repeated eigenvalues.

Also A_K p2=4|z|^2. Substituting the two definitions gives the exact
telescoping calculation

    (B-A_K)(p2+p3+p4)
      =-4|z|^2+(Bp2-A_K p3)+(Bp3-A_K p4)+Bp4
      =-4|z|^2+Bp4.

This is an identity of polynomials in the independent formal variable,
evaluated at xi only afterward. The final coefficient remains a
current-state function; “quintic” means degree five in z with X fixed,
not a global degree-five polynomial in all physical coordinates.
Differentiating Bp2 inside the next correction differentiates its direction
fields as well as K. The recursive definition includes those terms.

The scalar check is also correct. Before evaluation, take
`B=-2zk(x)partial_x` and `A=2k(x)z partial_z`. The resulting coefficients
are exactly

    p3=z^3 k_x/(3k^2),
    p4=z^4 [k_x^2/(6k^3)-k_xx/(12k^2)].

Evaluation at z=x leaves the exact remainder
`-2k(x)x^5 partial_x[k_x^2/(6k^3)-k_xx/(12k^2)]` in addition to -4x^2.

## 3. Population regularity and physical-ball bounds

The compressed induction in candidate Section 4 is valid. The following
details explain why an unrestricted L2 Nemytskii smoothness theorem is not
being used.

For fixed inputs let

    s_i=w.v_i,  t_i=tanh'(s_i),  Z_i=b2^T M a_i,
    Q_i=b1^T M^T d_i.

The exact Gram can be written

    K_ij=(1/3)[E2(H_i H_j)+(d_i.d_j)(a_i.a_j)
               +(v_i.v_j)E1(t_i t_j Q_i Q_j)].

Each j_l has bounded row and readout components, uniformly when ||c||2
and ||M|| are bounded. Differentiation along j_l gives

    D_(j_l) s_i=(v_i.v_l)t_l Q_l/sqrt(3),
    D_(j_l) c=H_l/sqrt(3),
    D_(j_l) M=d_l a_l^T/sqrt(3),
    D_(j_l) Z_i=b2^T[(D_(j_l)M)a_i+M D_(j_l)a_i].

The right sides are bounded functions or finite vectors/matrices, with
bounds depending only on the fixed feature envelopes and current bounds
for ||c||2 and ||M||. The formulas for a_i and d_i then propagate the same
property. More explicitly, every relevant expression is a finite sum of
products of finite coefficients, bounded gate derivatives, lower moments
of bounded gate products, and upper moments of either bounded gate
products or c times such products. In the last class, differentiation has
the form

    D_(j_l) E2[c F(Z)]
      =E2[(H_l/sqrt(3))F(Z)+c D_(j_l)F(Z)].

It never creates two undifferentiated copies of c in the same pointwise
integrand. Products of separate c-dependent moments are harmless.
Cauchy--Schwarz bounds each c-linear moment by ||c||2 times the bounded
factor. All fixed-order tanh derivatives are bounded. This class of
expressions is preserved by further directional differentiation, including
differentiation of the direction fields themselves.

There are only three nested state differentiations of p2 in Bp4, together
with the finite inverse operations. The inverse bound above and the
finite inverse derivative identity control those operations whenever
K>=mu I. This proves finite uniform bounds a3,a4,a5 with exactly the
dependencies claimed in the candidate. The base row w does not appear
outside gates in this fixed-input calculus, so no supremum bound on w or
Gaussian truncation is required.

Continuity in the physical metric can be checked on the same expression
class. A difference of lower gate products is bounded in L1 by a constant
times ||w-w_tilde||2. Hence lower moments, a_i, and the finite coefficients
are continuous. Because b2 is bounded, convergence of M and a_i gives
uniform convergence of the upper Z_i and their gates. For an upper moment,

    |E2[c F]-E2[c_tilde F_tilde]|
      <=||c-c_tilde||2 ||F||2
        +||c_tilde||2 ||F-F_tilde||2.

The second factor difference is uniformly controlled. Products and the
uniformly invertible finite matrix operations preserve continuity.
Thus K and all correction coefficients are continuous in the physical
metric on the stated bounded regions.

This also resolves the possible ball-topology objection: a physical ball
does not give a common L-infinity bound for c or w-g, but the coefficient
estimates require neither. The bounded-characteristic class is sufficient
for the time chain rule, and the displayed formulas and bounds extend to
the physical ball. Continuity of K at a positive-definite state supplies
a positive lower eigenvalue bound on a smaller ball; bounds on c and M
and the preceding induction supply all the other constants there.

## 4. Positivity and decay constants

On (10),

    L/Lambda<=p2(X,xi)<=L/mu,
    |p3+p4|<=a3 L^(3/2)+a4 L^2,
    |Bp4|<=a5 L^(5/2).

The two conditions in (11) therefore give exactly
`p2/2<=E_corr<=3p2/2` and `E_corr'<=-2L`. These inequalities include
L=0 by direct evaluation. Adding the stated geometric correction,
`Phi_corr=L+kappa E_corr`, gives

    L<=Phi_corr<=[1+3kappa/(2mu)]L,
    Phi_corr'<=-(4mu+2kappa)L
       <=-[(4mu+2kappa)/(1+3kappa/(2mu))]Phi_corr.

There is no reversed comparison or missing factor in these bounds.
Positive thresholds exist for any finite a3,a4,a5 and Lambda>0, including
the cases of zero coefficient bounds.

## 5. Trapping and the all-time conclusion

For L>0, put q=xi^T K xi. Until a first exit from the ball,

    -d sqrt(L)/dt=2q/sqrt(L),    ||X'||=2sqrt(q).

Since q>=mu L, the ratio of the first quantity to the second is at least
sqrt(mu). Thus total physical length up to any such time is at most
`sqrt(L(X0)/mu)`, strictly less than R. A first exit would have physical
distance R and contradict this length bound. Canonical finite-time
continuation then gives the trajectory for every future time. Decreasing
L preserves L<=ell, so the corrected-potential inequality persists.

The finite total physical length yields a Cauchy trajectory in the complete
population-L2/Frobenius space. Its limit remains strictly inside the ball,
and continuity of the prediction map and L(t)->0 imply exact fitting.
No future metric estimate or supplied endpoint was used. If L(X0)=0,
X'=0 and uniqueness gives the stationary solution directly.

If a separate theorem supplies convergence to a fitted X_* with K(X_*)>0,
the continuity and boundedness just proved give a common small ball about
X_* with all constants. For sufficiently large t, a fixed smaller ball
about X(t) lies in it and sqrt(L(X(t))/mu) is smaller than that ball's
radius. Hence eventual entry follows. This verifies the implication, not
any unprovided theorem identifying which initialized families have a
regular endpoint.

## 6. Defects, clarifications and limitations

No major or construction-fatal defect was found. Two nonblocking formal
clarifications would improve precision:

1. At candidate lines 65–70, specify **m>=1**. A_K annihilates degree-zero
   constants. All actual uses here have m=2,3,4, so the omission changes no
   construction or conclusion.
2. In Section 5, explicitly state L(X0)<=ell and handle L(X0)=0 by
   stationarity before dividing by sqrt(L). The intended positive-loss
   argument is correct, and the zero-loss case is immediate.

The following are substantive limitations, not defects in the stated claim:

- Uniform positivity of K already gives L'<=-4mu L and the trapping
  argument without the correction. The new contribution is the explicit
  cancellation of the geometric-cost defects. No better global capture
  region or decay rate follows just from adding these terms.
- The coefficients become uncontrolled as the least eigenvalue of K
  approaches zero. The construction gives no protection against a singular
  endpoint and no regular continuation of the potential through one.
- Near a regular fitted state, joint small input/state perturbations have
  xi=O(|epsilon|); local uniform coefficient bounds then make the remainder
  O(|epsilon|^5), including mixed directions. This is a residual expansion.
  At a nonfitted reference, xi need not be small in the input perturbation
  parameter, so it is not an all-path fifth-order input expansion.
- The result does not prove entry from the prescribed broad initialized
  family, an all-time input-response bound, closure-order convergence, or
  identification with a general-dimensional trained-network limit.

These boundaries are already preserved in the candidate's main claims.

## Versioned addendum: clarified candidate

2026-09-16. I reread the complete revised candidate, SHA256
`381cf0cc0339e0d87408e3328b6c14c295de1a58841f439d0d170c0d5b0a0d72`.
Reversing exactly the four textual edits implementing the two review
clarifications reproduces the original frozen SHA256 recorded above.
There are no other content changes.

The revised invertibility statement explicitly requires m>=1. The trapping
hypotheses explicitly require L(X0)<=ell with ell satisfying (11), and the
proof handles zero loss by stationarity both initially and upon any later
arrival at zero, before using the positive-loss division. Both clarification
items in Section 6 are resolved. **PASS remains unchanged** for the stated
local-residual/current-state theorem. The limitations and endpoint-dependency
qualification in the original review remain unchanged. Original provenance
and findings above are retained as the review of the earlier frozen version.
