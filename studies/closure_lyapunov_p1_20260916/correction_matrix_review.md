# Isolated mathematical review of the initialized matrix correction

2026-09-16. Analytic review; no experiments and no promotion decision.

Frozen principal input: `correction_matrix.md`, SHA256
`cec95a18660aa562ed2914d8c2de2d3d0cba7c78822ba6366252d5439b4454aa`.

Separately authorized addendum: `correction_initial_rank.md`, SHA256
`17c835025d60ba332860f87d5331edd0136959a12c7b06354eced88eb1efd9d5`.
Its additional conclusion concerns the formula's domain only.

The complete frozen principal input and addendum were read. The scientific
dependencies read were `docs/NOTATION.md`, `docs/observable_p1.md`,
`docs/global_nonlinear.md` C.4.7.9 and C.4.7.10 B/C.1/D.3, and the complete
same-study `three_coordinate_candidate.md`, `perturbation_modes.md`,
`sphere_second_variation.md`, and `rho_endpoint_extension.md`. The scoped
independent-review instructions and solve-math-rigorously skill were applied.
No README, study history, prior review, other current route findings, other
study, or references outside this assignment were consulted.
`perturbation_metric_template.md`, mentioned in the principal input's account
of its author inputs, was not in the reviewer input scope and was not read.
No assertion from it is needed for the proofs audited below.

## Verdict

**PASS within the stated mathematical scope.** No mathematical defect was
found in the explicit matrix potential, the exact defect, its first/second
trained recurrence, the quadratic correction, or the conditional all-time
neighborhood theorem. The additional initialized-rank proof also passes.

The theorem requires a symmetric unit-label seed with a positive-definite
full tangent Gram at its fitting endpoint. It does not establish that
hypothesis on a new unit-label rho range. The larger domain established by
the addendum does not enlarge this decay theorem. The report makes these
limitations explicit and does not turn a finite-horizon Taylor calculation
into an all-time estimate.

There is one useful comparison clarification and several minor notation
issues below. None changes the stated conclusions.

## 1. Physical normalization and initialized interpolation

Let J be the derivative of the normalized prediction vector p in the
population-L2/Frobenius metric. Then K=JJ* equals (2), including all three
blocks and the actual transpose of M. Since L=|p-n|², the physical flow is
X'=-2J*r and consequently

    p'=-2Kr,    L'=-4 r^T K r=-||X'||².

The readout equation gives q'=-4 r^T p. Thus the factors of three and two
in (1)–(3) agree with the unhalved mean-square loss and with the supplied
canonical dynamics.

The initialized feature map H0:R³→L2(Omega2) has H0*c equal to the
normalized initialized-feature predictions. The constraint H0*c=n is
therefore precisely interpolation of the three absorbed unit labels.
The proposed c*=H0 Gamma0^{-1}n is feasible. Its orthogonality to
ker(H0*) proves that its squared norm is the minimum, equal to
n^T Gamma0^{-1}n. Hence the reciprocal normalization mu0 is correct.
This calculation involves initialized fields only.

On Gamma0>0, S=Gamma0+pp^T is positive definite at every finite current
state. In particular the potential has no singularity when an evolving
tangent or readout Gram loses rank. It controls L, and its initial value is
exactly two. At symmetry, permutation invariance gives
Gamma0=C0 nn^T+nu0(I-nn^T), mu0=C0, and p=Fn. Substitution recovers the
previous scalar potential exactly, so the supplied symmetric theorem
applies with its original physical time and all full-state dynamics.

## 2. Complete derivative and the initialization sign

With R=S^{-1}, direct differentiation gives

    S'=-2(Kr p^T+p r^T K),
    R'=2R(Kr p^T+p r^T K)R,
    (r^T R r)'=-4a+4av,

where a=r^T R K r and v=p^T R r. The equality of the two scalar
cross-contractions uses transpose symmetry of R and K, not commutation.
Combining this identity with q'=-4b proves exactly (6) and (7).
No K' is required because the time-dependent inverse is S^{-1}, not K^{-1}.
The report correctly avoids inferring a sign for a from positivity of R
and K.

At initialization, u=1/mu0, a=1, k=C0 and b=v=0. Thus

    Phi_mat'(0)=-4(C0+mu0),
    D_(4mu0)(0)=-4(C0-mu0).

The block inverse gives mu0=C0-beta0^T D0^{-1}beta0. This establishes
both the exact nonpositive sign and the quadratic coefficient
-4|beta1|²/nu0 in (10), with the stated coefficient rather than
second-derivative convention. The naive-potential defect in Section 2 is also
correct.

**Comparison clarification.** The successful comparison changes both the
potential prefactor and the proposed dataset-dependent rate: the naive
calculation uses 4C0, while the corrected one uses 4mu0. At the unchanged
rate 4C0, the corrected potential instead has

    D_(4C0)(0)=4(C0-mu0),

which is positive when beta0 is nonzero. This is consistent with the
explicit formulas in the candidate, so it is not a mathematical error.
Making the rate change explicit in the prose would prevent the stronger,
incorrect reading that changing the prefactor alone repairs the same-rate
defect. Section 5 proves some fixed positive rate on a neighborhood; it
does not claim that 4mu0 works there for all time.

## 3. Actual quadratic correction and trained recurrence

In the mean/transverse coordinates, the Schur complement B of d in S is
positive. Completing the block square gives

    r^T S^{-1}r=e²/d+(zeta+eh/d)^T B^{-1}(zeta+eh/d),

with the plus sign forced by the mean residual -e. Subtracting the old
potential yields (12). Since

    zeta+eh/d=((C0+F)/d)zeta+(e/d)beta0,

its first perturbation coefficient is exactly Z in (13). The expansions
B^{-1}=nu0^{-1}I+O(epsilon) and
mu0-C0=-epsilon²|beta1|²/nu0+O(epsilon³) give every term of (13).
The invariant mean observables may have first variations: their variations
only multiply the already quadratic terms in this difference. No false
vanishing of those first variations is used. At time zero the two beta1
terms cancel, as required by the common initial potential value.

The transverse response equation (14) has the correct normalization.
Differentiating P=(C0+F)/d and H=e/d gives (15), and differentiating the
coefficient in (13) gives (16). In particular the coefficient of the
trained coupling response b1 is

    4e(1+q)C0[((P²/nu0-1/d)zeta1)+(PH/nu0)beta1]·b1,

as in (17). It has no algebraically supplied sign. The calculation concerns
the added defect at a common rate (or the base value of a smooth varying
rate); it is not a proof that the full defect is nonpositive.

For the complete recurrence, multiplying S R=I through degree two gives
exactly (18), with the displayed matrix order. The scalar reciprocal rule
gives (19). Every contraction in (20) is its ordinary polynomial coefficient;
in particular a_j retains the ordered R_b K_c product and k_j includes K_2.
Their convolutions reproduce (7), giving (21). Replacing every rate product
by convolution with 4mu0,j correctly includes rate variations. Polarization
or two-variable convolution recovers all mixed coefficients, with A_2 equal
to one half of the one-parameter second derivative.

The supplied complete sphere response equations contain the normal sphere
acceleration, both state/input mixed terms, both first-response products,
and the second trained state. Their weighted Gaussian bounds justify the
expectation products and Taylor remainders used here on each fixed horizon.
No unrestricted L2 multiplication theorem or all-time response bound is
being assumed.

## 4. The regular-endpoint all-time neighborhood theorem

The theorem in Section 5 is valid, including the anticommutator argument.
The necessary continuity and trapping steps can be checked in the declared
physical Hilbert norm, without treating the Gaussian row as bounded.
For example, between nearby states and inputs,

    |a_i-a_tilde_i| <= ||w-w_tilde||_2
                      +||w_tilde||_2 |v_i-v_tilde_i|.

Finite coefficient dimension and bounded b2 then control the upper
preactivation difference in essential supremum. Subtracting d_i uses
readout L2 differences and the essential-supremum upper-gate difference.
Also |Q_i| is bounded by B1 ||M||op ||c||2. These facts control the full
gradient differences and hence K on a physical state ball. Only a bound
on the readout L2 norm is needed here, which the ball supplies.

Choose one sufficiently small ball and data neighborhood satisfying both
K>=kappa I and the later matrix inequality. The initialized symmetric
trajectory approaches its fitting endpoint and its loss tends to zero.
Finite-time continuous dependence therefore puts nearby trajectories in
the interior of that ball at a sufficiently large finite T. While a path
stays there,

    -d(sqrt L)/dt=||X'||²/(2sqrt L)>=sqrt(kappa)||X'||.

Choosing sqrt(L(T)/kappa) below the remaining distance to the ball boundary
precludes a first exit. At L=0 the physical vector field vanishes.
This proves one neighborhood of data valid for every subsequent time,
rather than a sequence of shrinking finite-horizon neighborhoods.

For potential decay, write P=I+mu0(1+q)S^{-1}. At the symmetric endpoint,
both P and K are scalar on the mean and transverse subspaces. They commute,
and congruence by P^{-1/2} turns 2(KP+PK) into 4K there. Thus if
k_*=lambda_min(K_*)>0, continuity yields

    2(KP+PK)>=3k_* P

throughout a sufficiently small common state/data neighborhood. This is a
valid positive margin; positivity of K by itself would not suffice.

The exact derivative

    P'=mu0 q' R+mu0(1+q)R'

has norm at most B|r| there because R,K,p,q and mu0 are bounded and
Gamma0 is uniformly positive. Consequently

    Phi_mat'<=-3k_*Phi_mat+B|r|³.

Taking T large enough that B|r(T)|<=k_* and using monotonicity of L and
P>=I gives the claimed tail inequality with rate 2k_*. On the compact
initial interval, the seed potential remains positive and its logarithmic
derivative is at most -4C0. The explicit derivative and finite-time
continuity preserve the weaker margin -2C0 for nearby data. Combining
the two intervals gives (22) with a fixed positive rate and initial value
two. Earlier transverse rank losses are irrelevant to this compact-time
argument.

The final state-limit claims also follow. The length bound gives a physical
Hilbert limit. On the trapped tail, the row essential-supremum speed is
bounded by a constant times sqrt(L), and the readout speed has the same
bound directly from |H_i|<=1. Exponential decay makes them integrable.
The finite-time characteristic solution supplies finite initial increments
at T, so w-g and c converge in essential supremum. Coupling the frozen
marks identically proves the stated W2 convergence of the saved joint laws.

## 5. Singular-endpoint scope

At a symmetric fitting center the transverse weight is
1+C0(1+q_*)/nu0. Linearizing residual evolution while freezing that center
gives the coefficient (lambda-4nu_*) times this weight, exactly as in (25).
Thus nu_*=0 obstructs a positive-rate inequality on unrestricted ambient
residual directions for this linearized system.

The distinction drawn in the candidate is essential and correct. At a
singular physical endpoint, the first prediction variations arising from
state variations lie in the range of J, which equals the range of K.
An arbitrary transverse residual need not be attainable to first order.
Equation (25) alone therefore supplies neither a counterexample among
initialized perturbed trajectories nor a theorem about their convergence.

The supplied rho endpoint criterion identifies a zero transverse
eigenvalue with the simultaneous conditions theta_perp=0 and d_parallel=0.
The present calculations do not exclude those conditions at F=1. The
exceptional-amplitude result cannot be restricted to amplitude one to infer
an almost-every-rho result. The candidate's claim boundary is accurate.

## 6. Separate review of the initialized-rank addendum

**PASS.** The complete initialization proof supplies an odd, strictly
increasing scalar kappa and a positive upper-mark density on the open cube.
Coordinatewise injectivity gives k(v)=±k(u) exactly when v=±u, and k(v)
is nonzero for unit v.

For three distinct non-antipodal directions, choose z avoiding the planes
orthogonal to k(v_i) and k(v_i)±k(v_j). All their normal vectors are
nonzero. A fully explicit justification of this choice is to try
z=(1,t,t²): each plane excludes the roots of a nonzero polynomial of degree
at most two, so finitely many planes exclude only finitely many t.
The resulting t_i=z·k(v_i) are nonzero and have pairwise distinct squares.

An almost-sure linear dependence of the initialized fields holds everywhere
in the open cube by continuity and positive density. Restricting to Z=sz
near zero and taking the nonzero degree-one, degree-three, and degree-five
tanh coefficients gives the matrix with columns (t_i,t_i³,t_i⁵)^T.
Its determinant is the product of t_1 t_2 t_3 and the Vandermonde in
t_1²,t_2²,t_3², so it is nonzero. This proves the claimed independence
and hence Gamma0>0 regardless of the input Gram rank.

In fact, repeated or antipodal inputs immediately give equal or opposite
fields, so the exclusion is also necessary for rank three in this unit-input
setting. This observation does not provide a sign for the trained defect.
The addendum correctly extends the formula's domain, initial value and loss
control, while leaving the all-time decay theorem unchanged.

## 7. Minor notation and presentation points

- In (14), b_1 denotes a two-dimensional coupling response, while earlier
  b_1 denotes the seven-dimensional frozen lower feature column. Both meanings
  are recoverable, but using a different coupling symbol would avoid a type
  collision in a document that still uses the canonical b_1.
- In Section 5, k_* is lambda_min(K_*); in Section 6 it is reassigned to
  n^T K_* n. The reassignment is explicit and does not affect (25), but a
  distinct symbol for the mean eigenvalue would make rate comparisons safer.
- The addendum's expressions n=1/sqrt(3) and xi=p-1/sqrt(3) mean the
  three-vector of ones divided by sqrt(3), as defined in the principal input.
  Writing the vector explicitly would remove the scalar/vector ambiguity.
- The C0 used in the final fixed rate is the seed's initialized value. A
  seed subscript there would distinguish it from nearby datasets' varying C0.

These are presentation issues, not missing hypotheses or false identities.
The substantive open issue remains the initialized dynamics at a possibly
singular unit-label endpoint, not initialization rank or inverse regularity.
