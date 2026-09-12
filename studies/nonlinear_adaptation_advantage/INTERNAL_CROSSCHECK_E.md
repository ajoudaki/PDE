# Internal cross-check E of the full-frozen comparison transfer

Reviewer: /root/energy_route, 2026-09-12.
Assignment: persist the completed internal cross-check of COMPARISON_TRANSFER.md.
Verdict: **no required correction found for its stated claims and conditions**.
This is an internal mathematical cross-check, not a promotion review.

## Inputs, coverage, and isolation

Reviewed input: COMPARISON_TRANSFER.md, authored by root, complete file,
lines 1–259, including every proof, constant, conditional statement,
implementation boundary and dependency/limitation paragraph.

Exact reviewed SHA-256:

    d341800ae1b42a38b583514d18ced89c6118290fc2dc2456a9f93258776495c2

The reviewer first froze the independently developed ROUTE_ENERGY.md before
reading any scientific content from COMPARISON_TRANSFER.md. Its frozen hash is:

    01779adf6e60fde92fb6979c3e421b3bc5061850bc3051399714b7d4aa58993b

After that freeze, the supervisor expressly authorized this internal cross-check.
The complete transfer file was read without truncation and its hash verified.
Both hashes were rechecked immediately before recording this report and remained
identical. ROUTE_ENERGY.md has not been edited.

The review used the contract, required mathematical/research skills, and
established source coverage already read for Route E:

* RESEARCH_CONTRACT.md and docs/NOTATION.md, in full.
* docs/global_nonlinear.md, lines 12994–17016: complete C.4.9–C.4.10.
* The contained dependencies in that file at 1840–1902, 5475–5782,
  5999–6103 and 6104–6521.
* docs/special_data_limits.md, lines 3785–4326: complete III.F.

The exact hashes and reading limitations of those inputs are retained in
ROUTE_ENERGY.md §9. The unread complements were not audited. No other route or
other study was read. No new research, experiment, numerical execution, or
formal verification was performed during this cross-check.

## Mathematical checks and outcomes

### 1. Complete frozen evolution and common metric

Checked the typed maps D_p:H_p→E, D_p*:E→H_p, and K_p=D_p*D_p.
Since d(u) is odd, the adjoint representative is odd. Inner products and
force integrals on odd functions are unchanged by replacing p with p_s.
This does not substitute a different prediction metric.

The operator exponential is justified by norm convergence for bounded K_p;
its contraction follows from positivity and the displayed energy derivative.
The raw tangent equation (3) reconstructs the same predictor by differentiation
and uniqueness. Its continuous representative, and anchor preservation from
d(e_a)=0, avoid treating point evaluation as a functional on arbitrary L²
equivalence classes. All raw gradient blocks remain present.

The matching initial risk derivatives in (4) have the correct factor four
for the unhalved loss. They do not prove a difference between the learners.

Outcome: no correction required.

### 2. Absence of a permanent frozen approximation floor

Checked the dense-range proof from self-adjoint injectivity:
ran(K_p) has orthogonal complement ker(K_p)={0}. With
h(t)=<S(t)v,K_pS(t)v>, the derivative is
h'=-4||K_pS(t)v||². The latter norm is nonincreasing because K_p commutes
with S(t), and S(t) is a contraction. Therefore

    t ||S(t)K_p v||² <= h(0)/4 <= ||K_p|| ||v||²/4.

The factor 1/4 is correct. Approximation by ran(K_p), followed by contraction,
proves convergence for every fixed residual without a spectral gap.

For uniformity on a finite-cap compact task family, multiplication by
sqrt(p_s) correctly conjugates the problem to the common odd L²(rho) space.
Uniform density convergence supplies operator-norm convergence of the bounded
conjugated kernels and norm convergence of initial residuals. Continuity at
each finite time, compactness, a finite subcover and monotone risk give one
finite time for the prescribed tolerance. The argument supplies no practical
rate and does not imply a finite-episode comparison.

Outcome: no correction required.

### 3. Identical observations and the empirical frozen learner

Checked that the empirical covariance A_hat is nonnegative even with repeated
or singular samples; no inverse or empirical rank condition appears. The
raw error equation is exactly

    (z_hat-z)'=-2 A_hat(z_hat-z)-2 I_m+2 N_m.

The residual used in I_m is evaluated on the deterministic population path.
Conditional centering and iid pairs eliminate the cross terms in the noise
second moment. No independence of trained quantities and their own labels
is assumed.

The contraction/Duhamel estimate, Cauchy–Schwarz in time, Tonelli, Markov and
union bound yield C_F as written. Multiplying the raw error by L_0 gives
beta_m=L_0 C_F/sqrt(m); the two L_0 factors are necessary and correct.
This agrees with the independently derived frozen sampling bound (E18)
in ROUTE_ENERGY.md.

The squared-risk error 2B_0 beta_m+beta_m² follows directly from the norm
difference with ||F_fr-q||_p<=B_0. The same observations may be used for
the nonlinear learner because combining its event with the frozen event
requires only a union bound, not event independence.

Outcome: no correction required.

### 4. Conditional threshold and finite-GF transfer

Checked the inversion of the Osgood modulus:
eta_N is exactly the input giving output d_N at time T. Because d_N<=1/2,
the strict branch condition holds. The chosen d_N gives alpha_m<=a/8.
The chosen beta_*<=1 gives

    2B_0 beta_m+beta_m² <= (2B_0+1)beta_* <= a/8.

Thus the empirical comparison retains 3a/4, conditional on the explicitly
unproved population margin a. The four noise/input failure allowances
sum to delta; the noiseless specialization correctly omits noise terms.

For each fixed task, sample and positive epsilon, the established finite-GF
capture applies. Conditioning on the realized sample is valid for every
empirical law; bounded conditional failure probabilities permit integration.
Width is first, contamination second, and samples last. Whole-circle
prediction convergence controls risk, with the spare a/4 allowing the a/2
conclusion in (13). No class-uniform width threshold or finite endpoint
restart is asserted.

Outcome: no correction required. The population comparison hypothesis is
substantive and remains unproved.

### 5. Finite Gram representation and approximate-kernel boundary

Checked the 1/m normalization in K_m and the reconstruction (14).
Differentiation at sample points recovers the exact empirical equation.
The construction requires exact endpoint queries; it is not a proof that
those queries are available from a finite neural approximation.

For (15), the exact empirical residual supremum is initially at most B_0
because |Y_i|<=1, and its integral inequality gives
B_0 exp(2K_0t). Subtracting the approximate and exact equations puts the
prediction error under tilde k and the kernel discrepancy against the exact
residual. The resulting scalar Gronwall bound is precisely the stated
exp(2K_1 T)[zeta+2T chi B_0 exp(2K_0 T)].

This stability argument does not require tilde k to be positive or symmetric;
its uniform absolute bound suffices. It correctly leaves the task of proving
input approximation errors zeta and chi to any proposed implementation.

Outcome: no correction required.

## Scope of the verdict

All stated mathematical claims in the frozen input were checked under their
explicit established hypotheses. No unresolved objection requiring a correction
was found. In particular the shared-sample transfer agrees with the independent
Route E calculation.

The report does not establish the missing nonlinear-versus-frozen population
margin, a beneficial change in relative component learning, a middle-layer
attribution, or a finite-neural realization of the frozen endpoint kernel.
It is not one of the fresh isolated promotion reviews in Part 2 of the
repository workflow: the reviewer is a research-route author, the assignment
was an internal cross-check, and no promotion packet or authorization is involved.

## Recording checks

Before this report was written, read-only metadata showed HEAD
1bed52ef4a190589659fccce96acf50bb7a2e8c5 and an empty Git index.
The workflow hash remained
8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12.
Concurrent files were left untouched. The only new artifact from this request
is INTERNAL_CROSSCHECK_E.md; no Git/index write was performed.

