# Isolated review of the singular-state Hessian candidate

2026-09-16. **Verdict: PASS for the conditional current-state geometric
claims.** No substantive repair is required in equations (2)–(12). Two
minor wording/notation repairs are specified below. This is an analytical
review, not a promotion decision or a proof of initialized-flow reachability,
perturbed-flow fitting, or a global Lyapunov inequality.

## Scope and frozen inputs

The assignment and the solve-math-rigorously and investigate-conjectures
skills (including the latter's adversarial-audit reference) were read.
Scientific reading was limited to the assigned candidate and dependencies.
No study README, history, other review, other agent's findings, experiment,
or implementation was consulted. References inside the supplied dependencies
were not followed outside the assignment. The canonical chapter was read at
C.4.7.9 and C.4.7.10 B, C.1, D.3, with the C.4.7.10 opening model statement.
The other listed documents were read completely. The candidate and dependency
hashes were checked again after the review and were unchanged.

SHA-256 values (paths relative to the repository):

| Input | SHA-256 |
|---|---|
| `studies/closure_lyapunov_p1_20260916/rho_singular_hessian.md` | `183ee92d471b1e5752136c5f6d58788e678dc6190edb92848fd320d97fe7ad1e` |
| `docs/README.md` | `60816cf89cf93abc9d752b7d56a66b3302cd9ca0caff4b247991647dfb49b3ad` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/observable_p1.md` | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` |
| `docs/global_nonlinear.md` | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |
| `studies/closure_lyapunov_p1_20260916/three_coordinate_candidate.md` | `531b1cb1fe5e5844fcc6da25486e6ee52450860030dd770246e3ee78592521ce` |
| `studies/closure_lyapunov_p1_20260916/perturbation_modes.md` | `57bea14a8a1290189a2dcf44985b9729671618fd1f152004103c5d1b5c15bf94` |
| `studies/closure_lyapunov_p1_20260916/perturbation_metric_template.md` | `c852c95c0c3f9d26c9512e056ec2a9d1b05837b50d0b46c45b65bb7d85c729b7` |
| `studies/closure_lyapunov_p1_20260916/resolution_endpoint.md` | `9806da5ed7c5f02557a21fef3be193da213c8e83fb5a81aff42206f5f342a79f` |

The canonical chapter hash identifies the whole file; it does not claim a
review of unassigned chapter sections.

## 1. State, metric, and first derivative

Write `g0` for the frozen Gaussian first row and `g*` for the candidate's
common prediction gradient, to avoid its notation collision. The metric is

    <h,k> = E1[h_w.k_w] + E2[h_c k_c] + tr(h_M^T k_M).

The canonical finite-feature equations and the three-coordinate dependency
give, with `phi=tanh`,

    grad f_i = (phi'(w.v_i) Q_i v_i, H_i, d_i a_i^T).

At the assumed state `z_i=z, d_i=0, f_i=1`, this is exactly
`g*=(0,H,0)`. Since `E2[cH]=1` and `c` is square integrable,
`E2[H^2]>0`. Thus `K_ij=||g*||^2/3` has eigenvalue `||g*||^2`
along `n=1/sqrt(3)` and two zero eigenvalues. The rank and normalization
in (2) are correct; neither the feature normalization nor the probability
weights insert an additional metric factor.

The input sign absorption is valid because the bias-free predictor is odd
in its input at every state. Labels remain fixed and have unit magnitude.
All three tangent inputs can be varied independently on the unit sphere.
No common-angle restriction or rotation of the fixed dictionary is used.

## 2. Full second derivative and regularity

For the prescribed sphere curve,

    v_i'(0)=eta_i,
    v_i''(0)=-|eta_i|^2 v_i,
    (w(tau).v_i(tau))''(0)
        =2 h_w.eta_i-|eta_i|^2(w.v_i)

for a linear state path. Thus the mixed lower term and sphere-curvature
term in the candidate are both required and correctly included. Applying
the product and chain rules successively to `a_i`, `M a_i`, and
`E2[c phi(z_i)]` gives

    f_i''(0)
      =2 E2[h_c phi'(z) Z_i]+E2[c phi''(z) Z_i^2]
       +d_i^T(2 h_M A_i+M a_i^[2]).

The last term vanishes because the entire coefficient vector `d_i` is
zero. This does not assume `c=0`, and it does not discard a nonzero
first-layer curvature contribution: that contribution has been contracted
against its zero upper coefficient. The first two terms retain the lower
variation through `A_i` and the mixed middle variation through `h_M a_i`.
The factor two multiplying the readout/preactivation product is correct.
Equation (5) is the full diagonal quadratic form of the mixed state/input
Hessian on the stated tangent directions; polarization recovers its
bilinear form.

The bounded-direction regularity argument is sufficient. On bounded sets
of `w-g0`, `h_w`, `k_w`, and tangent inputs, every lower preactivation
derivative through order three is bounded by a constant times `1+|g0|`.
Bounded tanh derivatives therefore bound the lower scalar Taylor remainder
by `C |tau|^3 (1+|g0|)^3`. Its coefficient expectation uses the finite third
Gaussian moment; its population L2 norm uses the finite sixth moment.
Both exist. Bounded dictionary columns convert these moments into finite
coefficient vectors, whose upper fields are bounded. Bounded `c,h_c,k_c`
then justify the scalar predictor expansion and the L2 gradient expansion
by the same product estimates. Polynomial Gaussian envelopes also work
with the corresponding finite higher moments. No unrestricted L2
Nemytskii C2 assertion is needed.

For the quadratic state path, the extra predictor acceleration is the
ordinary differential applied to `k`, namely `<g*,k>`. Input-only first
derivatives vanish, and the imposed neutrality `<g*,h>=0` removes the
first-order residual. Equation (6) follows with its stated third-order
remainder.

## 3. Quartic loss and the data-dependent potential

Set `s_i=B_i+<g*,k>`. From
`f_i(tau)-1=tau^2 s_i/2+O(tau^3)` and the unhalved mean loss,

    (1/3) sum_i (f_i(tau)-1)^2
      =tau^4 sum_i s_i^2/12+O(tau^5).

Thus the coefficient is `1/12`, not the half-loss coefficient `1/24`.
For any scalar `a`, taking `k_c=a H/E2[H^2]` and zero other blocks is
bounded and realizes `<g*,k>=a`. Minimizing the displayed quadratic
polynomial in `a` gives `a=-bar B` and exactly (8). This is minimization
over local path acceleration only. It supplies no dynamically selected
correction.

At a fitting state, the loss Hessian on a joint direction is
`(2/3) sum_i (df_i)^2`. It vanishes on the stated neutral directions,
although the fourth-order coefficient can be positive. A zero quartic
coefficient is also permitted; the result does not assert that order four
is always the first nonzero order.

The original factor is

    W=1+C0(1+q)/(C0+F^2),
    q=E2[c^2],  F=(f_1+f_2+f_3)/3.

It is finite and positive under the stated assumptions. If its initialized
`C0` is recomputed with the perturbed inputs, the exact initialization
formula is locally Lipschitz in those inputs: subtract lower gates using
`E1|g0|<infinity`, then use bounded features, finite `D`, and the upper
Lipschitz gate. The averaged initialized upper feature and its squared
expectation inherit this property. At the admitted symmetric seed `C0>0`,
so it stays positive nearby. Along the proposed bounded state path `q`
and `F` are also locally Lipschitz. Consequently `W(tau)=W(0)+O(tau)`
with either convention for `C0`, and (9) follows. A derivative of `W`
first contributes at order five and cannot change the order-four
coefficient. Readout and data dependence have therefore been retained.

## 4. Gradient variation, null Hessian, and Schur complement

Differentiating the complete gradient gives the candidate's (10).
In the middle block, the ordinarily present `d_i A_i^T` vanishes.
In the row block, the lower-gate derivative and the direction derivative
multiply `Q_i=0`; the `h_M^T d_i` term also vanishes. The surviving
reverse term is `b1^T M^T D_i`. Its readout dependence
`D_i=E2[b2(h_c phi'(z)+c phi''(z) Z_i)]` is correct. In particular
the formulas do not replace the moving readout by a fixed coefficient or
the full metric by its readout block.

Let `J(tau)^* x=sum_i x_i grad f_i(tau)/sqrt(3)`. For a zero-sum
vector `x`, the constant term of `J(tau)^*x` is zero. Squaring its
first-order L2 expansion proves (11), including the factor `2/3` in
the second derivative. The bounded-direction differentiability above
also justifies this ordinary second derivative, beyond a purely formal
Peano coefficient.

For the orthonormal output basis `(n,E)`,

    J(tau)^* n = g*+O(tau),
    J(tau)^* E = tau A+o(tau).

Hence the three block expansions in the candidate follow immediately.
Since `||g*||>0`, division by `k(tau)` is justified near zero, and

    H_perp-b b^T/k
      =tau^2 [A^*A-A^*g* (g*)^*A/||g*||^2]+o(tau^2)
      =tau^2 A^*(I-P_g*)A+o(tau^2).

This removes precisely the derivative component along the old common
gradient; no factor of three is missing. If the coefficient is positive
definite, its smallest eigenvalue supplies a positive `c tau^2` lower
bound on the Schur complement. Completing the square in the parallel
coordinate gives a congruence to `diag(k,Schur)` with transformation and
inverse uniformly bounded and tending to identity. The full Gram is then
positive definite for small nonzero `tau`, has one eigenvalue bounded
away from zero, and two eigenvalues bounded above and below by positive
multiples of `tau^2`. Conversely, a singular coefficient has a transverse
direction with Schur quadratic form `o(tau^2)`, so both weak eigenvalues
cannot enjoy those quadratic lower bounds. The candidate's qualification
about possible higher-order opening is necessary and correct.

## 5. Claim boundaries and exact minor repairs

The result remains conditional on its explicit current-state assumptions.
The isolated degeneracy result in `resolution_endpoint.md` does not decide
whether the unit-label initialized endpoint is singular. Nothing here
changes that status. Positivity of the local Schur coefficient is not a
global bound, a capture inequality, or a conclusion about the actual
perturbed initialized trajectory. The candidate preserves all of these
distinctions and introduces no hidden trajectory input or additional
evolving state.

The following repairs improve precision without changing the verdict or
any formula's mathematical content:

1. **Notation, lines 22, 31, 90–91.** Keep `g` for the frozen Gaussian
   row and rename the common prediction gradient in (2) to `g_*`.
   Replace subsequent gradient pairings, norms, and projectors by
   `<g_*,h>`, `<g_*,k>`, `||g_*||`, and `P_{g_*}` respectively.
   This removes the type conflict with `w=g+(bounded)`.
2. **Scope wording, lines 197–201.** Replace the sentence asserting that
   the effects “occur together” by: “At the possible singular endpoint,
   the first-order fixed-state input response vanishes. The quadratic
   predictor response and quadratic Schur coefficient describe the next
   possible orders of residual production and metric opening; either
   coefficient may vanish for a chosen direction.” For example, with
   inputs and hidden state fixed, a pure readout variation perpendicular
   to `H` keeps every prediction exactly one, even though hidden-gradient
   derivatives need not vanish. Thus nonzero residual production and
   nonzero metric opening are not asserted to be equivalent.

No experiment or candidate edit was performed. This review writes only
this report.

## Addendum: verification of the two repairs

2026-09-16. **PASS reaffirmed for the revised candidate**, SHA-256
`be854ef80b2ffb26d9624b04b637795790b5474f006c57e5468c59e2281b94f5`.
The complete revised candidate was read. It consistently uses `g_*` for
the common prediction gradient while retaining `g` for the frozen Gaussian
row, and its final paragraph now explicitly permits either quadratic
coefficient to vanish for a chosen direction.

As an exact editorial check, reversing only these gradient-symbol
substitutions and the specified final-paragraph replacement reconstructs
the original frozen SHA-256
`183ee92d471b1e5752136c5f6d58788e678dc6190edb92848fd320d97fe7ad1e`.
Thus no other mathematical formula or claim changed. Both minor repairs
are resolved, and the original analytical verdict and scope limitations
apply to the revised hash. The original review and dependency provenance
above are retained unchanged. This follow-up changed only this addendum;
it performed no scientific experiment and did not modify the candidate.
