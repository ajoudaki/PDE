# Independent review of the full-rho endpoint extension

2026-09-16. Fresh isolated theoretical review. No experiments. Internal
review only; this report does not promote any result to the established library.

**Verdict: PASS for the candidate's stated claims and quantifiers.** I found
no mathematical defect requiring correction. The result covers every
orientation in the original rho family, including rho=-1/2, with at most
finitely many exceptional positive label amplitudes on every bounded range.
The all-time nonsymmetric perturbation theorem is valid whenever the seed's
fitting endpoint is nonsingular, even if its earlier path loses transverse
rank. Neither this review nor the candidate establishes an almost-every-rho
or every-rho theorem at the prescribed amplitude A=1.

## Frozen inputs and isolation

The reviewed candidate is `rho_endpoint_extension.md`, SHA256
`d8b6401195dbfe1b1f2e7e3f4177b318364c3cd8ec3f221b314c594a341933ef`.
Its hash was checked before and after the mathematical reading.

I read the complete candidate and the three assigned same-study dependencies:

| Input | SHA256 |
|---|---|
| `three_coordinate_candidate.md` | `531b1cb1fe5e5844fcc6da25486e6ee52450860030dd770246e3ee78592521ce` |
| `resolution_open_family.md` | `6c949bdec4e78fb895ae71281edd328623a662cba433fba618d65e82055fe337` |
| `resolution_rate.md` | `e1053c8e0129c08afab58ac0354ffc7c1ad909aecfdb0ab15230e50961c1ba86` |

The canonical inputs were the complete `docs/NOTATION.md` and
`docs/observable_p1.md`, plus the relevant state, initialization, gradient,
and well-posedness material in `docs/global_nonlinear.md` C.4.7.9 and
C.4.7.10 B/C.1/D.3. The investigate-conjectures and solve-math-rigorously
skills, including the adversarial-audit reference, were applied.

I did not read the study README, history, other route reports, other studies,
or any earlier verdict. In particular, the candidate's named
`perturbation_orthogonal.md` and `resolution_endpoint.md` were outside this
assignment and were not consulted. The exchange identity below was checked
directly from the displayed model, so their absence leaves no necessary
scientific premise unverified for this review. Only this report was written.

## Contract and inherited premises

The candidate retains the exact d=3, p=1 correlated Gaussian populations,
ridge eta=1/4096, initial state (G,0,D), evolving full 4-by-7 matrix and its
actual transpose, and population-L2/L2/Frobenius metric. Removing constant
coordinates uses the exact preserved oddness of the initialized flow.
The auxiliary parameter s reparametrizes the physical optimizer and is not
an additional operational state coordinate.

The three-coordinate dependency supplies its own finite-time characteristic
existence argument in d=3. Its initialized rank-three proof applies to every
a!=b, including the case where the three input vectors are dependent. I
checked the positive derivative of its initialized scalar map kappa and the
third-derivative argument when the initialized coefficient matrix has zero
parallel eigenvalue. Thus C_0>0 does not rely on invertibility of the input
Gram.

The inherited inequalities also have the required all-feature-time scope.
Along X_s=grad F, F_s=K=||grad F||^2 and q_s=2F. Cauchy--Schwarz gives
qK>=F^2, so q/F^2 is nonincreasing from its limit 1/C_0 at s=0. Consequently
q<=F^2/C_0, C>=C_0, and K>=C_0. They continue past any specified fitting
amplitude; they are not merely pre-fitting bounds.

Global input negation is valid with the state map (w,c,M)->(w,-c,M).
It fixes initialization, preserves F and the physical metric after changing
the data, and sends the auxiliary vector field to the transformed vector
field. The parameter omega=m/d after choosing d=a-b>0 therefore covers the
whole family. Its two signs for -1/2<rho<1 are correctly retained as separate
orientations. No unsupported rotation invariance is used.

## Transverse criterion and the dependent-input endpoint

Permutation equivariance gives the stated parallel/perpendicular matrix
blocks and hence formula (5). One can verify the section 2 exchange step
without the unprovided orthogonal report. Put h(z)=sech^2(z). The definition
of the transverse eigenvalue of [d_1 d_2 d_3] gives

    2 d_perp = E_2[(Z_1-Z_2)c(h(z_1)-h(z_2))]/R_Z.

Since z_1-z_2=theta_perp(Z_1-Z_2)/R_Z, this becomes

    d_perp = theta_perp r,
    r = E_2[(Z_1-Z_2)^2 c
            integral_0^1 h'(z_2+t(z_1-z_2)) dt]/(2 R_Z^2).

The bounds |Z_1-Z_2|<=2, |h'|<=2 and ||c||infinity<=s prove
|r|<=4s/R_Z^2; the same expression proves continuity across theta_perp=0.
The matrix evolution then gives equation (6), and its integrating-factor
argument correctly proves m_perp never vanishes at finite s. The candidate
does not mistake this for nonvanishing of theta_perp.

The full tangent Gram has eigenvalues lambda_parallel and the double
lambda_perp. Its three gradient blocks give equations (7)--(8), with the
correct factors for the unweighted Gram. In particular
lambda_parallel=3||grad F||^2>=3C_0.

At lambda_perp=0, the readout contribution forces H_1=H_2 almost surely.
Injectivity of tanh and the positive-density upper law force theta_perp=0.
Then all z_i=kS, and C>=C_0>0 forces k!=0. Therefore M^T 1 is nonzero.
The six active lower features are linearly independent: conditioning on G
eliminates the k coefficients through their independent positive conditional
variances, after which the independent h coordinates eliminate the rest.
Thus V=b_1^T M^T 1 is nonzero in L2.

Now d_i=d_parallel 1/3 and Q_i=d_parallel V/3. The pairwise bound

    |x v_1-y v_2|^2 >= (1-|rho|)(x^2+y^2)

and strict positivity of the lower gates force d_parallel=0 when the row
contribution in (7) vanishes. Conversely theta_perp=d_parallel=0 makes
every contribution in (7) zero. This proves the claimed equivalence (10).
At rho=-1/2 the bound still has coefficient 1/2, so the dependent triple
introduces no missing case. A three-input Gram inverse is never needed.

## Forced crossing, quadratic coefficient, and compact uniformity

At a rank-loss event, d_i=Q_i=0. Thus M_s,w_s,a_{i,s},z_{i,s} vanish,
while c_s=tanh(kS). Differentiating d_i leaves precisely equation (13):

    (d_parallel)_s = delta
      = E_2[S tanh(kS) sech^2(kS)]/R_Z.

The integrand has the strict sign of k away from S=0, and S is nondegenerate.
Hence delta!=0. Bounded features and fixed-data characteristic speeds justify
the differentiation and continuity needed for local strict monotonicity.
The rank-loss set is closed, so isolation yields finitely many events on a
compact s interval; possible accumulation at s=0 is also excluded by the
initialized rank-three result.

The expansion coefficients in (14)--(15) are correct. The middle term has
leading coefficient delta^2||a_1-a_2||^2/6, since ||1||^2=3. The row term
has leading coefficient

    delta^2 E_1[V^2 |g_1 v_1-g_2 v_2|^2]/18.

The readout difference is o(s-s_0), so its squared contribution is
o((s-s_0)^2). The row expectation is strictly positive by the pairwise bound,
V nonzero in L2, and positive gates. Thus J_rho>0, including at rho=-1/2.
The two-sided quadratic zero is established, not merely an upper bound on
the rate of vanishing.

The compact-family argument uses the necessary uniform hypotheses.
On I compact in omega, C_0 is continuous and has a positive minimum c_I.
All endpoints with 0<A<=A_max occur before A_max/c_I. State and input
subtraction is valid in the Hilbert metric because Gaussian G has finite
second moment, while backward coefficients and feature evaluations are
bounded. It gives locally uniform Lipschitz dependence in omega. Direct
differentiation of d_parallel also gives joint continuity of its s derivative.
No L-infinity continuity in input direction is needed.

The closed rank-loss set in the resulting compact (s,omega) rectangle has
a finite cover by rectangles where that derivative has one strict sign and
is bounded away from zero. Each rectangle contributes at most one event on
each fixed-omega fiber. Their finite number is therefore a uniform bound;
pointwise finiteness alone would not have sufficed.

The opposite signs at two nearby time endpoints persist in omega. Monotonicity
then gives a unique zero s=sigma(omega), and subtraction with the derivative
lower bound proves its Lipschitz estimate. Composing with F gives the claimed
Lipschitz amplitude charts. Actual exceptional points additionally require
theta_perp=0; the candidate does not assert that each entire chart is bad.
The finite compact covers yield a joint null set on the full parameter domain.

For completeness, endpoint continuity follows from F_s>=c_I: on a common
bounded interval, the inverse-time difference is bounded by

    |s_A(omega)-s_B(omega_tilde)|
      <= (|A-B|+sup_s |F(s,omega)-F(s,omega_tilde)|)/c_I.

This verifies the openness assertion. Density follows by varying amplitude
on each fiber, since that fiber has only finitely many exceptional values
in a bounded range.

## Endpoint positivity and the all-time perturbation conclusion

Equation (17) uses K=G/3, consistent with z_i=(f_i-A)/sqrt(3):

    ||X'||^2 = 4 z^T K z,    L'=-||X'||^2.

Continuity of the full Gram in the Hilbert metric gives a coercive ball about
the nonsingular fitting endpoint. The seed reaches any sufficiently small
neighborhood of that endpoint at a finite physical time, with arbitrarily
small positive residual. Finite-time continuous dependence transfers those
entry conditions to nearby input triples. Inside the ball,

    -d sqrt(L)/dt >= sqrt(k)||X'||

gives remaining path length at most sqrt(L(T)/k). The chosen margins make
a first exit impossible. Global characteristic existence handles all finite
times, including the earlier noncoercive portion. If loss becomes zero,
uniqueness makes the path stationary. The proof therefore does not require
full tangent coercivity at earlier seed times.

The rate from time zero also checks: the seed satisfies -L'/L>=4C_0, and its
loss stays bounded away from zero on a fixed finite interval. Continuous
dependence preserves a strictly positive ratio there, while the coercive
tail gives the remaining rate. This proves (18) without an entry-time
prefactor.

The full derivative of the mixed potential is included. Its displayed
gradient is correct, and bounded Hilbert balls with C_0 bounded away from
zero give finite B and Lambda. Therefore

    Phi' <= -4k Phi + 2B sqrt(Lambda) L^(3/2).

The stated small-loss threshold absorbs the positive term using W>=1.
The finite-time seed inequality persists by continuity, and enlarging the
chosen entry time creates no circularity: the coercive ball and its bounds
were fixed first. This proves (21), with Phi(0)=2A^2. No sign of W' is
assumed on the perturbed flow.

Exponential residual decay in the trapping ball also gives integrable
L-infinity velocities for c and w-G: their speeds are bounded by a finite
constant times sqrt(L), since d is controlled by ||c||2 and Q by bounded
features and finite matrix coefficients. Thus the stronger state convergence
and the common-mark W2 coupling claimed at the end of section 6 are justified.

## Both orientation branches and the fixed-amplitude limitation

The near-coincident proof in `resolution_open_family.md` extends to
sufficiently small negative e by the same two-sided continuity at e=0.
Its input matrix eigenvalues e,e,e+3 remain nonzero. For positive e,
omega=(3+e)/e tends to positive infinity. For negative e, globally negating
the inputs makes a-b positive and gives the same formula for omega, now
tending to negative infinity. Hence both tails in section 7 are covered.
This does not provide a new range separated from coincidence.

The fixed-amplitude caveat is essential and correctly stated. A Lipschitz
graph can coincide with A=1 throughout a nonempty interval, so neither joint
two-dimensional nullity nor finite vertical fibers gives a null prescribed
horizontal slice. The nonzero s derivative of d_parallel cannot substitute
for control along the constraint F=1. The candidate leaves that implication
open and identifies the missing weighted cross-time correlation estimate.
It also avoids assuming analytic geometry dependence from a finite-dimensional
ODE theorem when the actual row state has Gaussian marks.

No revisions are required for the audited theorem. A self-contained future
presentation could include the short explicit formula for r above in place
of the reference to the orthogonal report. The proved results remain internal
exact-closure statements, with no network-identification, closure-accuracy,
universal-fitting, or rotation-invariance conclusion.
