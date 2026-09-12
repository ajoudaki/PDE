# Actual finite-GF capture: fixed-horizon bridge

Status: coordinator proof module; conditional only on the population construction
and tail bounds specified below. It is not a standalone proof of milestone A.
Inputs are the complete maintained finite-program theorem III.F.1–III.F.11,
C.1–C.2, C.4.1–C.4.3 and C.4.7; see SOURCE_COVERAGE.md for hashes.
No training experiment, finite-width endpoint or arbitrary simultaneous limit
is used. This file is author work, not an independent review.

## Statement needed from the population construction

Fix one positive epsilon and one admitted added law, and a finite physical
horizon T (which may equal tau0/epsilon). Suppose controlled population Euler
programs for its actual mixture GF converge strongly on [0,T] to a unique
population path theta, with the following bounds uniform in sufficiently fine
Euler partitions: ordinary raw state ball; readout essential supremum;
passive-query second-moment tails

    tau_R(Q(u)) + tau_R(c) <= C exp(-a R^2),  R>=1,

for every training and finitely named observation input. Constants may depend
on the fixed epsilon and T. Here tau_R(v)=||v 1_{|v|>R}||_2; any equivalent
soft cutoff can be used in intermediate convergence arguments. Assume all these
Euler programs live on the same initialized Gaussian carrier and use its actual
forward action and actual adjoint. Their strong limit determines predictions
by f_theta(u)=<c,tanh((A0+K)tanh(w.u))>.

Then the actual width-n mixture GF, starting at the prescribed independent
Gaussian arrays with their actual nonzero readout, converges in probability to
this prediction in C([0,T]xS1). For every finite list of times and inputs, its
first-row, forward hidden, upper gate, readout, and actual forward/adjoint-query
fields have the joint same-layer observation limits supported by the maintained
finite-program theorem and its second-moment extension. This includes paired
second-hidden activation distances between mixture and reference flows using
the same initialized arrays. No unknown finite-width endpoint is introduced.

## Proof

At width n give each layer's vector space its normalized Euclidean inner
product n^{-1}sum. Middle increments have ordinary Frobenius norm. The raw
state-increment metric is

    d_n^2=||w-wbar||_(n,2)^2+||W2-W2bar||_F^2
                                      +||c-cbar||_(n,2)^2.

The initialized middle action itself is bounded in operator norm, rather than
Frobenius norm; only its increments enter d_n. Work on initial events on which
its operator norm, the first-row second moment and initial loss are bounded.
Their probabilities tend to one by the established Gaussian initialization
bounds and laws of large numbers. The actual initial readout has entries of
standard deviation 1/n. Its maximum tends to zero in probability, because
Pr(max_j |c0,j|>eta)<=2n exp(-n^2 eta^2/2). Its normalized second moment also
tends to zero. It is retained in every finite array and proxy, never set to zero.

The finite GF is global at every n. Its smooth vector field is locally
Lipschitz in finite dimensions; unhalved loss dissipation gives
integral_0^T ||theta_n'||_raw^2 <= L_n(0). Hence its raw displacement is at most
sqrt(T L_n(0)). This bounds the action norm by its initialized norm plus the
Frobenius increment. Also |c_n'(j)|<=2 integral |f_n-y| dmu <=2 sqrt(L_n(0)),
so ||c_n(t)||_infty<=||c_n(0)||_infty+2T sqrt(L_n(0)). These bounds imply a
finite raw velocity bound on [0,T], uniform on the preceding initial events.
They justify continuation and every subsequent comparison; they do not provide
the decisive population query tails.

Fix a finite Euler partition h and freeze the *population Euler program's*
scalar training coefficients. Run that exact finite program on the actual
Gaussian arrays, including their initial readout. Call it the finite proxy.
It uses every actual middle multiplication and its actual transpose; no
independent replacement is made. The fixed-program neural law and its
at-most-quadratic observation extension show convergence of all its finitely
named fields, scalar contractions and second moments to their population
program values. The small initial readout passes by a fixed-oracle cutoff induction, rather
than a dimension-dependent finite-dimensional Lipschitz bound. First construct
the finite oracle with zero limiting readout instructions and the same actual
first/middle arrays. Its fixed nodes have the proved joint second-moment laws.
Compare the actual-readout proxy to that oracle, keeping its Gaussian readout
additively in the former. The initial raw error tends to zero. At a coordinate
update, every changed bounded gate multiplying an oracle L2 field is split at
a fixed cutoff R: its bounded part is controlled by the preceding raw error,
and its remaining normalized error by that oracle field's empirical L2 tail.
At fixed program and R the latter converges by the node's second-moment law;
then R tends to infinity. Direct action and rank subtractions handle the other
terms. Induction through the finite number of nodes therefore gives raw error
tending to zero at every node. Readout suprema stay bounded on the initial
events because the update is a sum of bounded tanh values and the actual
initial maximum vanishes. No uniform Lipschitz constant on arbitrary
width-dependent parameter balls is assumed. This is the fixed-program
extension used by C.4.7; the zero-readout object is only a comparison oracle,
never a replacement for an actual finite run or its actual-readout proxy.
In particular, the discrepancy between a proxy prediction at an update input
and its population coefficient's prediction tends to zero. Denote the maximum
of these finitely many discrepancies by zeta_(n,h); then zeta_(n,h)->0 in
probability for fixed h.

For clarity, the comparison can be made at every left Euler endpoint and its
affine interpolation. The interpolation stays on a common raw ball. Its
recomputed c and Q tails converge at a fixed cutoff to the corresponding
population tails. One may first name a finite additional interpolation grid;
the forward/action maps are L2 Lipschitz on this ball with bounded readout,
and the proxy raw interpolation speed is bounded. Soft tails
||(|Q|-R)_+||_2 are one-Lipschitz in Q and pass to the fixed-program limit.
A finer interpolation grid and the elementary inequalities relating hard tails
at R to soft tails at R/2 give the asserted bound uniformly over interpolation
time, with enlarged constants. No growing transcript is taken before width.

Subtract actual GF from the affine proxy. The one-reference product inequality
is elementary: for a bounded Lipschitz gate b and an arbitrary comparison
vector qbar,

    ||(b(z)-b(zbar))qbar||_2
                <= C R ||z-zbar||_2 + C tau_R(qbar).

Apply it to the lower gate multiplier with the proxy Q as qbar and to the
upper multiplier with proxy c. Direct bounded-operator subtraction handles Q
itself. The middle rank subtraction uses
||a tensor b||_HS=||a||_2||b||_2. Prediction residual subtraction is bounded by
the raw distance on the common ball. The frozen coefficient error contributes
zeta_(n,h), and the interpolation defect contributes O(h_max). Thus, for each
fixed cutoff R and the fixed T,

    sup_[0,T] d_n <= C_T exp(C_T R) [
       (1+R)(h_max+zeta_(n,h))
       + sup_proxy_time (tau_R(c_proxy)+sum_j p_j tau_R(Q_proxy(u_j))) ].

The two finite states have identical initial arrays, so there is no initial
state error in this inequality. The actual initial Gaussian readout remains
inside both states and the harmless uniform initial bounds above.

Take n->infinity with the partition and cutoff fixed. The proxy tails tend to
bounded Gaussian population tails, and zeta_(n,h) vanishes. For any desired
comparison error, first choose R large enough that
C_T exp(C_T R-a'R^2) is smaller than that error, then choose h_max small enough
that its amplified interpolation defect is smaller still. Both choices are
finite at every fixed positive epsilon. This proves proximity of finite GF to
the finite proxy in probability, with arbitrarily small prescribed error.
Strong population Euler completion then identifies the unique population path.
One does not send R to infinity at a fixed positive mesh, or claim uniform
width rates as epsilon tends to zero.

On each common raw ball,

    sup_u |f_theta(u)-f_thetabar(u)| <= C_T d(theta,thetabar),
    ||H2_theta(u)-H2_thetabar(u)||_2 <= C_T d(theta,thetabar).

The input Lipschitz constants are bounded by products of the readout, action
and first-row norms; H1 and H2 satisfy the corresponding L2 input estimates.
Consequently finite input nets upgrade proxy prediction convergence to the
whole circle, uniformly in physical time using the same velocity bounds.
This proves the claimed C([0,T]xS1) convergence.

For joint reference/mixture observations, use the union of their finite proxy
programs on the SAME Gaussian arrays and the finite-program joint law. Paired
bounded activation products are permitted second-moment observations. Both
finite flows are close to their proxies in the normalized hidden norms, so
Cauchy–Schwarz passes each mixed inner product and squared distance. Reference
capture is required only on this fixed finite T, where the established result
applies. The endpoint appears only afterwards, through the proved population
reference convergence as epsilon tends to zero and T=tau/epsilon tends to
infinity. Thus the paired finite statistic at time T converges to

    (1/m) sum_i ||H2_theta_mu(T)(u_i)-H2_theta_*(T)(u_i)||_2^2.

Combining the new population selection theorem (when proved) with the already
proved reference endpoint convergence gives its constrained-path versus latent
endpoint limit. This order keeps the actual common initialization intact.

## Quantifiers and scope

For every fixed positive epsilon small enough for the population continuation,
T=tau0/epsilon is finite. The proof above supplies width convergence for that
T, without any bound uniform in epsilon. Only then does epsilon tend to zero.
If population selection is uniform over a compact law box, its risk/hidden
margins can be uniform on that box, while the width convergence may still be
stated pointwise in the law. Uniform finite-width rates and raw-GD are not
claimed. All circle inputs are physical sqrt(2)u in the final prediction.
