# Activation scope of fixed-depth finite-horizon tracking

Date: 2026-09-25. Status: independently developed scoped author analysis,
frozen before receiving another route's findings. No experiment or Git
operation was performed. This note audits activation assumptions; it does
not replace the separate fixed-depth projection and continuation proofs.

## 1. Conclusion and contract

For the original activity closure, a natural sufficient smooth activation
class is C^{1,1}_loc(R). For the explicitly evaluated response-speed closure,
C^{2,1}_loc(R) is a natural sufficient class. These are sufficient conditions,
not asserted optimal regularity thresholds. Tanh, exact GELU and logistic
sigmoid satisfy both. Global boundedness of the activation is unnecessary
for finite-time existence of the dense flow, or for estimates confined to a
compact physical-state neighborhood. In particular unbounded GELU is not an
obstruction of the kind encountered at a kink.

Literal ReLU and standard SELU with the prescribed selected derivatives do
not admit the same universal theorem over arbitrary finite initial arrays:

* ReLU's selected dense equation can have multiple absolutely continuous
  solutions with the same initial state.
* SELU's selected dense equation can have no absolutely continuous solution
  from a finite initial state, and regular initial states can reach such a
  state in finite time.
* Both have a discontinuous normalized backward-response map at admissible
  states with strictly positive residual RMS. The continuous clock based on
  the ordinary a.e. response derivative does not absorb its jumps.

The strongest immediate transfer is conditional on a positive training
preactivation margin throughout the chosen finite dense horizon. A theorem
across switches requires additional selected-flow existence and stability
work. For the new clock it also needs a new history-regularity argument or a
changed clock; transversality by itself does not restore the claimed
Lipschitz response history.

The target remains the finite-dimensional stored-weight model with any fixed
finite hidden depth H, fixed finite width n and data, output c^T h_H/n,
unhalved squared loss, mobilities (n,1,...,1,n), and P tending to infinity
after these choices and a finite T. Neither a smooth approximation to an
activation nor a differential inclusion is silently substituted for the
selected-field model. The solver still uses its own current responses and
has no dense-trajectory input.

## 2. Exact activation conventions and sufficient smoothness

Use z_{1,a}=W_1 U_a, z_{ell,a}=W_ell h_{ell-1,a},
h_{ell,a}=phi(z_{ell,a}), and

    delta_H=c odot phi'(z_H),
    delta_ell=phi'(z_ell) odot W_{ell+1}^T delta_{ell+1}.

For internal links ell=2,...,H let b_{ell,a}=r_a delta_{ell,a}/rho when
rho>0. The new observable stacks the incoming forward responses
h_{ell-1,a} and b_{ell,a}; adding other forward responses does not change
the regularity conclusions. All norms below are finite-dimensional.

The input activation note specifies ReLU'(0)=0 and
SELU'(0)=lambda alpha, where

    lambda=1.0507009873554804934193349852946,
    alpha=1.6732632423543772848170429916717.

For SELU write a=lambda alpha and b=lambda in the counterexamples below;
there a and b are scalar one-sided slopes, not sample indices or backward
vectors. Thus a>b>0. ReLU and SELU are continuous locally Lipschitz maps,
but their selected first derivatives jump at zero. Exact GELU is z Phi(z),
with derivative Phi(z)+z varphi(z). Sigmoid is the uncentered logistic map.

If every layer activation is C^{1,1}_loc, finite products and compositions
make the prediction C^{1,1}_loc, the loss gradient locally Lipschitz, and
the dense selected field an ordinary locally Lipschitz field. The original
raw moment field uses only phi, phi', rho and nonzero history-length
denominators, so it is locally Lipschitz too, including at rho=0. This is
the regularity required by the local existence/uniqueness and physical
Lipschitz comparison steps of the old proof. The deep projection estimate
is a separate obligation; no assertion that its two-layer H1 estimate
automatically carries to every upper incoming history is made here.

If every activation is C^{2,1}_loc, then on rho>0 the map Psi is C^{1,1}_loc.
Indeed normalization r/rho is smooth there, while differentiating delta
uses phi''. The explicit physical velocity V obtained from the weighted
moment reconstruction is locally Lipschitz in its state where G is positive
definite. Hence g=rho+||D Psi(theta)V|| is locally Lipschitz. Products,
matrix inversion on the positive-definite domain, and the norm preserve
this property, proving the stated new finite ODE has a locally Lipschitz
field. No derivative of g and no third ordinary activation derivative is
needed. A C2 activation alone gives continuity of the displayed field but
does not justify this particular local-Lipschitz uniqueness argument.

## 3. Dense finite-time compactness needs no bounded activation

Let Gamma be the positive block-diagonal mobility matrix and L(theta) the
nonnegative loss. For C^{1,1}_loc activations the unique local dense solution
satisfies theta_dot=-Gamma grad L and

    dL/dt=-||theta_dot||_{Gamma^{-1}}^2.

Integrating and applying Cauchy--Schwarz yields, on every existing interval,

    integral_0^t ||theta_dot||_{Gamma^{-1}}^2 ds <= L(theta_0),
    ||theta(t)-theta_0||_{Gamma^{-1}} <= sqrt(t L(theta_0)).

Therefore a putative finite maximal interval lies in a compact parameter
ball. The field is bounded on a larger compact ball, so the state is
Lipschitz in time there and has a limit at the maximal endpoint. Local
existence from that limit extends the solution, a contradiction. Thus the
dense solution exists uniquely for all finite time. This proof permits
arbitrary growth of phi at infinity; only its local regularity is used.

On any finite dense horizon the prediction Jacobian is bounded. Since
F=-Gamma grad L is linear in the current residual with bounded coefficient
on that compact ball, ||r_dot||_RMS <= C_T rho. Wherever rho>0 this gives
rho_dot>=-C_T rho. Hence rho(t)>=rho(0) exp(-C_T T)>0 if rho(0)>0.
If rho(0)=0, the locally unique dense flow is stationary. These facts
support the same compact-tube and residual stopping arguments used by the
smooth tracking proofs, without assuming globally bounded activations.

For ReLU/SELU the energy identity still holds along any existing absolutely
continuous selected-field solution. To check the kink carefully: if z(t)
is absolutely continuous, z_dot=0 almost everywhere on the level set
{z=0}. At those times phi(z(t))_dot=0 as well, so
phi(z)_dot=phi'_selected(z) z_dot almost everywhere. Away from zero the
ordinary chain rule applies. Applying this successively through the finite
network gives the loss identity. Its resulting bound is conditional on
existence and cannot repair the counterexamples below.

## 4. ReLU: a finite network with nonunique selected dense flow

Take n=d=M=1, input U=1, target y=1, any H>=2, and all hidden activations
ReLU. Set W_1(0)=0 and W_2(0)=...=W_H(0)=c(0)=1. All mobilities equal one.
Every hidden output is zero at this state. The selected derivative at
every hidden preactivation is zero, so every selected parameter velocity is
zero. The constant path is a solution and rho=1.

There is also a departing solution. In the open region where all weights
are positive, the network is the scalar product

    f=c W_H ... W_2 W_1.

Extend this polynomial expression through W_1=0 just to solve its smooth
gradient equation locally. At the displayed initial state its W_1 velocity
is 2 and every other velocity is zero. Continuity of this polynomial field
therefore gives a positive-time solution with W_1(t)>0 and all remaining
weights positive. For every t>0 sufficiently small it is exactly the
selected ReLU field. Failure of the differential equation at the single
initial time is immaterial to the specified absolutely continuous,
almost-everywhere solution convention. It is consequently a second valid
solution from the same initial arrays. Remaining stationary until any
chosen time and then using this departing branch gives further solutions.

This falsifies universal uniqueness of the literal dense target, before any
compression issue arises. It is not a counterexample to a smooth theorem
or to an expressly specified alternative nonsmooth solution convention.

It also exposes the response-clock problem directly: b_{H}(0)=0, while
on the departing branch r<0 and delta_H=c, so b_H(t)=-c(t)->-1 as t down
to zero. The forward responses and physical parameters are continuous but
the prescribed Psi is not.

An interior-time version does not require starting at a kink. With the
same positive weights, take target y=-1 and W_1(0)>0 sufficiently small.
Its positive-region W_1 velocity is bounded above by a negative constant
until W_1 reaches zero; other weights remain positive over this short
time. Thereafter the constant state satisfies the selected equation. Just
before this hitting time b_H=c>0, and at and after it b_H=0, while rho=1
at the hit. Thus an actual selected trajectory has a backward-response
jump even with a regular initial network.

## 5. SELU: a finite network with no selected dense continuation

Take n=d=1, two samples U_+=1 and U_-=-1, targets y_+=1 and y_-=q, with

    1<q<alpha^H,

and any H>=2. Set w=W_1=0 and W_2=...=W_H=c=1 initially. Every hidden
response is zero, so all internal-weight and readout velocities vanish at
that state. The selected W_1 velocity, however, is

    w_dot=a^H(1-q)<0,       a=lambda alpha.

The factor 2 from the unhalved loss cancels the sample count M=2. For w>0
near zero, all preactivations of sample + are positive and all those of
sample - are negative. The one-sided limiting velocity is

    F_w(0+)=b^H-q a^H<0,    b=lambda.

For w<0 the signs exchange, giving

    F_w(0-)=a^H-q b^H>0.

These are strict inequalities. Continuity within each sign region provides
a neighborhood of the full initial state and kappa>0 where F_w<=-kappa
when w>0 and F_w>=kappa when w<0. A purported absolutely continuous
solution remains in that neighborhood for a short time. There

    (w^2)_dot=2w F_w <=0

almost everywhere, including the set w=0 because of its leading factor.
Since w(0)^2=0, integration forces w(t)=0 throughout that interval. Every
other selected velocity then vanishes, so all remaining parameters stay
at their initial values. But the selected equation demands
w_dot=a^H(1-q)<0 almost everywhere, contradicting w=0. No such solution
exists.

This is not merely an initial-time defect. Start instead at a sufficiently
small positive w with other weights close to one. The smooth positive-side
flow reaches w=0 in finite time because w_dot<=-kappa, while the other
weights remain in the same neighborhood. At the hit the same argument
precludes any selected absolutely continuous continuation. The strict
inequalities persist in an open neighborhood of those regular initial
parameters. Energy boundedness does not prevent this obstruction.

## 6. Why the literal response-speed clock misses switches

Already with one scalar sample, y=1, W_2=...=W_H=c=1, and W_1=w close to
zero, rho>0. For SELU,

    lim_{w down to 0} b_H(w)=-lambda,
    b_H(0)=lim_{w up to 0} b_H(w)=-lambda alpha.

Thus Psi is discontinuous and D Psi does not exist at this admissible
positive-residual state. For an actual crossing, take w initially negative
and sufficiently close to zero with y=1 and all other weights positive.
Both one-sided W_1 velocities are strictly positive, so the piecewise
smooth dense solution crosses to w>0; b_H jumps there. The ReLU example
in section 4 supplies an actual hitting trajectory with the same problem.

If one interprets the new formula a.e. on the smooth pieces, its integral

    L(t)=1+integral_0^t rho ds+integral_0^t ||Psi_dot_ac|| ds

is continuous. Suppose t_* is a jump time with finite one-sided Psi limits
and finite clock. For s<t_*<t tending to t_*, L(t)-L(s)->0, whereas
||Psi(t)-Psi(s)|| tends to a nonzero jump magnitude. Therefore the encoded
history cannot be 1-Lipschitz, or even continuous, in xi=L. An a.e. bound
on its derivative alone does not imply absolute continuity or membership
in H1. The smooth proof's estimate D_b=O(P^-2) therefore has an invalid
hypothesis if applied unchanged across such a switch.

The polynomial moment, weighted Gram, covariance-defect and projection
energy identities survive for bounded measurable backward histories along
existing trajectories. In particular D_f_dot=rho||f-fstar||^2 holds a.e.
New history mass, not a derivative of f, drives that identity. The lost
step is the H1 approximation estimate and, independently, selected-field
well-posedness and stability. This is a failure of the literal universal
theorem and its proof premises, not a no-go result for all nonsmooth
compression methods or a proof that every nonsmooth closure diverges.

Adding jump magnitudes to the clock's total variation and filling each
jump by an interpolating response path would change the construction.
It requires explicit jump updates, an insertion-measure convention, and
a new autonomous realization. Such a repair cannot be described as the
unchanged clock g=rho+||D Psi(theta) theta_dot||.

## 7. What can be recovered without changing activation

### Positive-margin transfer

Assume a specified dense selected solution on [0,T] satisfies

    min_{ell,a,i,t} |z_{ell,a,i}(t)| >= eta>0.

It stays in one smooth activation-sign region. Choose a smooth scalar
activation agreeing exactly with ReLU or SELU outside (-eta/2,eta/2).
Such a function can be constructed by smooth interpolation between the
two branches inside that gap. It matches the activation and all relevant
derivatives on the dense path and on a sufficiently small compact
parameter tube. The smooth dense solution agrees there, and the smooth
tracking theorem makes sufficiently high-order closures remain in the
same tube. Their original/new moment fields therefore coincide with the
literal activation fields throughout [0,T]. This proves conditional
transfer of the corresponding smooth rate and regular existence, with
constants/order thresholds allowed to depend on eta. No activation was
changed on either realized trajectory. The argument applies independently
to every fixed finite depth.

### Finite crossings: exact identities and a conditional slower source bound

Assume an existing piecewise regular new-clock trajectory with rho>0,
bounded clock L, finitely many backward-response jumps, and finite total
jump magnitude J_f for each backward history f. Interpret its clock by
the a.e. derivative on the smooth pieces. Incoming forward histories are
continuous and 1-Lipschitz in xi. For any backward history write

    f(xi)=f_cont(xi)+sum_j Delta f_j 1_{xi>=xi_j},

where f_cont is 1-Lipschitz and constant on the prefix. This follows by
subtracting the finitely many jumps and integrating its bounded derivative.
Let N=P(P+1). Since dmu<=dxi, the ordinary Legendre projection is an
admissible comparator for weighted best approximation. Its continuous-part
error is at most L sqrt(L-1)/(2 sqrt(N)).

For completeness a scalar step admits a degree-<P comparator with L2(dxi)
error at most (3/2)sqrt(L/P), for P>=2. Replace its jump by a one-sided
linear ramp of width delta=L/P inside [0,L]; at least one side has enough
room. Step-to-ramp error is at most sqrt(delta), while the ramp derivative
has L2 norm delta^{-1/2}. The H1 Legendre bound then gives projection error
at most L/(2 sqrt(N delta))<=sqrt(L/P)/2. Add these two errors. Linearity
of projection and the triangle inequality consequently give

    sqrt(D_f) <= L sqrt(L-1)/(2 sqrt(N))
                   +(3/2) J_f sqrt(L/P).

The forward factor satisfies sqrt(D_h)<=L sqrt(L-1)/(2 sqrt(N)). Thus the
unchanged projection-energy identity and endpoint defect formula give a
conditional integrated-defect bound O(P^-3/2)+O(P^-2), with constants
depending on L, jump magnitudes, fixed depth, width and samples. This is
a sufficient upper bound, not an optimality claim. Its assumptions are
about the closure-generated paths; they have not been proved uniformly
in P here. It is not yet a dense tracking theorem.

Finite isolated transversal dense switches are a plausible setting for a
separate hybrid stability theorem, provided both one-sided fields cross in
the same direction with a quantitative normal-speed lower bound, other
surfaces are separated, and closure existence and jump control are proved.
Those assumptions exclude the SELU inward-pointing obstruction. They do
not remove backward-response jumps, and so do not recover the unchanged
new-clock H1 proof or its O(P^-2) rate. For the old clock, backward jumps
alone do not invalidate covariance reconstruction, but smooth Gronwall
stability still must be replaced by a proved crossing-stability estimate.

## 8. Claim status and provenance

| Claim | Status and scope |
|---|---|
| Smooth dense global finite-time existence without bounded activation | Proved above for C^{1,1}_loc |
| Local regularity needed by both finite closure ODEs | Proved sufficient conditions above |
| All smooth fixed-depth projection/continuation estimates | Separate route obligation, not proved by this activation audit |
| Universal literal ReLU uniqueness | Falsified by section 4 |
| Universal literal SELU selected-flow existence | Falsified by section 5 |
| New clock makes kinked backward histories Lipschitz | Falsified by section 6 |
| Positive-margin transfer of a valid smooth tracking theorem | Proved conditional transfer |
| Finite-jump O(P^-3/2) integrated-defect estimate | Proved under explicit trajectory/jump/clock assumptions |
| General nonsmooth dense tracking across switches | Open here; existence, stability and uniform jump bounds remain |

Complete scientific inputs read, with read-version SHA256:

* ACTIVATION_CIRCLE_DERIVATION.md:
  de95c624a6cd19abd824d118c985b99a87cf65d4b25ed6110b57da5716a95976
* DEEP_CIRCLE_DERIVATION.md:
  17ffa7efe44d588a47b8f566c5cbdc72199e012ae058bab232427e6685203bd9
* RESPONSE_CLOCK_FULL_CLOSURE.md:
  06560b5a53bbff5d0de7640ca2162f56d36ae25e7e57eb5b565505a951e8fa67
* RESPONSE_CLOCK_UNCONDITIONAL_BOUND.md:
  dda4d7b386b13129f30a64e6012b553b6ba783c41ed932874d98a93788ca7027
* ORACLE_FINITE_HORIZON_BOUND.md:
  bfe32ba200b980f088846f5c9e902f08e6e740219368b6cbbfc19616029f16c1

Required skills read: solve-math-rigorously; investigate-conjectures and
its research-contract, evidence-ledger and adversarial-audit references.
No external scientific source, other study, experiment result, other route
report, code or Git history was read. Only this assigned report was written.
These are original derivations and an author audit, not promotion review.

## 9. Complete collaborative check of the combined fixed-depth theorem

Check date: 2026-09-25. After the initial report above was frozen at SHA256
a90bcd2a9e8682ba1b83540b296fe84d13152d4cafefc51309ec76cc20b23af4,
the supervisor authorized reading one additional complete scientific input:
DEEP_ACTIVATION_ERROR_THEOREM.md. Its checked version has SHA256
f580a58d90e2e107226d311f934af00b9556e8ef7634f0f23be254c35e568e2d.
Coverage is all 514 lines, sections 1--9 and every displayed equation
(1)--(26), including hypotheses, proof, implementation counts, activation
boundary and provenance. The entire file was read, not selected excerpts.
No other route report, new scientific input, experiment or Git history was
read. This is a collaborative internal full check, not independent promotion
review. Root's synthesis had already incorporated this route's nonsmooth
findings before this check.

Outcome: PASS. No required mathematical or computational correction was
found in the checked version. The details below record the actual checks
and their scope; they do not enlarge the theorem's claims.

### A. Quantifiers, normalization and finite constructions

The theorem keeps n,d,M,H,T fixed and then takes sufficiently large P.
It correctly avoids extending the earlier two-layer tanh all-P existence
statement to the full activation/depth class. The Euclidean physical norm
is consistent throughout; replacing it by a block sum only in the upper
estimate for the defect is legitimate. Canonical output normalization and
mobilities give exactly F_1,F_l,F_w in (4). The encoded incoming history at
link l is h_(l-1), while its backward history is r delta_l/rho, so no forward
and backward coordinates of an intermediate layer are inadvertently merged.

The old initialization has zero backward history and constant forward
history on the prefix. New initialization has matching constants and
the fixed prefix subtraction. Both reconstruct the exact initialized
matrices. The shared Gram is appropriate because all links and samples
use the same coordinate and measure. The moving polynomial coordinates do
not change the underlying degree-<P space in the historical variable xi.
This verifies the projection interpretation used later.

### B. Projection energy and physical defect

For the new construction, differentiating tr(B G^{-1} B^T) cancels the
two dilation terms from B against the inverse-Gram dilation terms. The
remaining rank-one insertion contributes
rho(2<f,fstar>-||fstar||^2), with the displayed sign and coefficients.
Subtracting from the raw-energy derivative gives (9). Initially D_f=0
for every prefix, including the old zero backward prefix. Its single
initial jump changes no growing-integral differentiation identity.

For the old clock, G=tau diag(1/(2k+1)) satisfies the same matrix equation:
the off-diagonal entries of TG+GT^T equal tau, and diagonal entries are
2k tau/(2k+1). This confirms the same cancellation without an extra
evolving Gram. Product differentiation of reconstruction gives (10) with
the positive defect sign. Rank-one Frobenius norms and Cauchy--Schwarz in
time give (11). Its integral controls the norm of the velocity defect,
which is stronger than a bound only on its signed primitive.

### C. Dense continuation and the explicit compact ball

The mobility operator has maximal eigenvalue n, hence loss dissipation
gives integral ||theta_dot||^2<=n rho0^2 and displacement at most
sqrt(nt)rho0. Applied between any two times, Cauchy--Schwarz makes the
trajectory Cauchy at a finite putative endpoint. Its finite limit belongs
to the full locally Lipschitz field domain, allowing continuation. This
is valid for C^{1,1}_loc activations and uses no global activation bound.

The ball in (13) therefore leaves dense dynamics a full unit of radial
margin. Recursion (14) bounds each forward response and backward signal
on that ball: the matrix operator norm is at most R, each coordinate of
a preactivation is at most R times the preceding Euclidean response norm,
and diagonal gate operator norms are s_l. Each term in V in (15) bounds
the matching physical block divided by rho. Each term in a is the norm
bound for the corresponding prediction-gradient block, including its 1/n
factor. Convexity of the ball turns the gradient estimate into the claimed
prediction-RMS and residual-RMS Lipschitz bounds. A finite K exists by
the field's local Lipschitz property on that compact ball. These constants
do not refer to a future dense trajectory. The differential residual bound
rho_dot>=-aVrho and its first-zero argument verify (16).

### D. Old-clock depth induction and continuation

Endpoint evaluation on degree-<P polynomials has squared norm
sum_(k<P)(2k+1)/tau=P^2/tau. The old backward history has total sample-mean
energy at most (tau-1)B_l^2, so the projected endpoint RMS is at most
P B_l. Adding the present endpoint bounds the backward residual RMS by
(P+1)B_l. From (10),

    ||E_l/rho||_F^2 <= 4(P+1)^2 B_l^2 mean_a||a_la-astar_la||^2/n^2.

Integration against rho dt, identity (9), and the H1 Legendre bound give
the factor (P+1)^2/[P(P+1)]=(P+1)/P<=2, exactly as in (18).
There is no remaining P-dependent factor in that estimate.

The forward derivative at layer l involves F_l/rho, E_l/rho and the
preceding derivative. The three-term square bound gives precisely (19),
including A_(l-1)^2 multiplying the defect-energy estimate and R^2
multiplying the preceding derivative energy. The induction is genuinely
triangular: no Z_l term is used to bound itself, even though backward
responses couple all physical layers. Layer one uses only its unchanged
outer equation and has the stated base bound. The proof needs Z only
through H-1 for the compressed links; allowing the same recursion through
H is harmless.

Backward residual energy is at most S B_l^2 because its prefix is zero.
Combining this with (17), sample Cauchy--Schwarz and (11) gives exactly
B_old=(A/n)sum_l B_l sqrt(S Zbar_(l-1)). Gronwall then gives (21).
Before the first ball exit all constants hold. Choosing the resulting
error <=1/2 excludes that exit with a strict margin. For each fixed P,
bounded histories and tau in [1,A] bound the full raw state, allowing
continuation on the locally Lipschitz domain tau>0. The continuation
does not require a uniform positive residual lower bound: rho=0 is an
ordinary locally Lipschitz equilibrium of the raw field. Its backward
uniqueness justifies using positive rho on existing regular segments
when rho0>0. This verifies the old theorem without a missing closure
loss-decay or small-order existence assumption.

### E. New-clock regularity, sharp constant and continuation

The relaxed first-layer assumption is correct. Every monitored backward
response uses gates phi_l', l>=2. Its directional derivative differentiates
these gates and forward responses, but the first-layer gate enters only
through D h_1=diag(phi_1') D z_1. Thus phi_1'' is absent. Locally Lipschitz
phi_1' makes D h_1 locally Lipschitz, while locally Lipschitz phi_l'' for
l>=2 supplies the corresponding property in backward derivatives.
Consequently Psi is C^{1,1}_loc on rho>0 under the stated hypotheses.
These are sufficient regularity assumptions, not a proved necessary
minimum for every possible network or formulation.

The reconstructed physical velocity is explicit and locally Lipschitz
where G is positive definite and rho>0. Composing it with D Psi and the
norm verifies the required locally Lipschitz finite ODE, without assuming
g differentiable. Compactness gives finite J on the stopped physical and
residual region. The raw-history energy sum is bounded by A B_resp,
including the matching prefixes. Inequality 2sqrt(xy)<=x+y then gives
C0=A B_resp/(nM) and the physical variation bound VS+C0. Integrating the
actual definition of the clock proves (23), without presupposing a cap.

The entire stacked history, not just each component, has derivative norm
at most one in xi. Summing the vector Legendre comparison over all entries
therefore gives the single quantity L^2(L-1)/(4P(P+1)) in (24).
Combining (11) with 2sqrt(xy)<=x+y leaves the factor 1/(nM), yielding
exactly B_new=Lambda^2(Lambda-1)/(4nM). No depth or sample factor is
missing: their influence remains in the unscaled stacked clock and J.

The two order conditions exclude both the ball exit and residual exit
strictly. For every fixed P, the constant prefix gives a positive-definite
Gram uniformly over 1<=L<=Lambda. Compactness is used only for that fixed
P, so no unjustified conditioning bound uniform in P occurs. Bounded raw
moments, positive residual margin, bounded L and this Gram lower bound put
the complete state inside its regular domain and justify continuation.
This verifies the new theorem and its stated eventual-in-P quantifiers.

### F. Activation boundary, examples and computational claims

The tanh, exact GELU and sigmoid conclusions follow directly from their
smoothness on R. The additional listed smooth examples also satisfy the
hypotheses; unbounded polynomial or GELU activations cause no gap because
all closure estimates are stopped on the explicit finite ball. The new
second-derivative condition is limited to internal/output hidden layers.

The checked ReLU counterexample uses W1=1,W2=0,w=1, rather than the first-
layer-zero example in section 4 of this report. Its selected field vanishes
at that state; its polynomial positive-region field has W2_dot=2 and a
positive departing solution. The possible mismatch at one departure time
is immaterial to the specified a.e. convention. It is a valid independent
finite example of nonuniqueness. The SELU two-sample one-sided velocities,
inward-pointing neighborhood, W1-squared argument and incompatible selected
velocity are all correct. The claim about nearby regular initial states
reaching the obstruction uses strict signs and bounded upper velocities
over a sufficiently short interval, and is valid.

The response jump invalidates the H1 step in the new proof across literal
kinks; the note correctly preserves the exact history identities instead
of claiming those fail. Positive-margin transfer is conditional and does
not silently smooth either realized trajectory. The final open nonsmooth
statement is properly limited by the selected-flow counterexamples.

The implementability formulas cancel g from internal physical velocities,
then use a forward directional pass and reverse differentiated backprop.
Every phi_l'' occurrence has l>=2. No implicit g solve or supplied dense
trajectory remains. Moving history storage, outer blocks, fixed matrices,
one shared symmetric Gram, prefix storage, rank bounds, O(P^3) shared
factorization, O((H-1)MnP^2) factor solves, per-vector operator actions and
prefix-sum dilation counts are consistent. These are component operation
counts, not a measured runtime or full finite-precision guarantee; the
text expressly preserves that distinction and the unimplemented status.

No correction is requested. This check establishes internal consistency
of the complete frozen candidate under its stated hypotheses, not
promotion, practical solver accuracy, width/depth-uniformity, or a new
general nonsmooth theorem.

## 10. Complete check of the final revised candidate

The supervisor subsequently authorized a fresh complete read of the revised
DEEP_ACTIVATION_ERROR_THEOREM.md, now 565 lines, SHA256
57e6e16b9af6ea32dd3cbc266f1c5b9054ae63219ce8e191bffdb3b87f44d8dd.
All 565 lines and sections 1--9 were reread in full, including the new
all-P corollary and equation (21a). The file hash was verified after this
read. The original audit in section 9 remains attached to its original
frozen version; this section records separate coverage of the final version.
No other route report or additional scientific source was read.

Final revised-candidate outcome: PASS. No required correction found.
The complete old/new proofs, constants, regularity and computational claims
retain the checks in section 9. Explicit lambda>0, alpha>1,
ReLU'(0)=0 and SELU'(0)=lambda alpha now remove any ambiguity in the
nonsmooth examples; their formulas and contradiction arguments remain
correct under precisely these conventions.

The new old-clock corollary correctly assumes both globally bounded
activations and globally bounded first derivatives, while retaining
C^{1,1}_loc for local uniqueness. Its independent a priori bounds avoid
using the previously stopped high-order comparison to prove all-order
existence. Specifically:

1. The unchanged linear-readout equation gives
   d||w||^2/dt=-4n mean_a(f_a-y_a)f_a
   =nY^2-4n mean_a(f_a-y_a/2)^2. Thus B_w, q, S and A bound the readout,
   residual, accumulated activity and old interval at every existing order.
2. Global incoming-response bounds allow the middle-matrix estimates to
   run downward in depth. At link l, the already obtained B_l bounds the
   current and historical backward responses. Projection contraction and
   the zero backward prefix give
   ||W_lhat-W_l0||_F<=2B_l a_(l-1)sqrt(tau(tau-1))/n,
   which is at most the increment in D_l. The dense increment is bounded
   by 2S B_l a_(l-1)/n. The recurrence
   B_(l-1)=s_(l-1)D_l B_l then bounds the next backward signal. This has
   no circular dependency: bounding W_l only uses higher matrices and a
   globally bounded incoming activation, not a bound on W_l itself.
3. The unchanged first-layer equation gives exactly
   ||W_1||_F<=||W_10||_F+2SX B_1. The combined block bounds define a common
   compact region independent of P, containing the dense and every old
   closure trajectory on its existing interval. Raw moment representations
   and 1<=tau<=A bound each fixed-P realization, establishing its
   continuation through every finite T with no order threshold.
4. On this common region F has a finite P-independent Lipschitz constant.
   The forward energy induction from (18)--(19) remains valid with
   global activation/slopes and D_l in the layer-l operator term. Its
   endpoint-factor cancellation is unchanged. The resulting integrated
   defect and Gronwall comparison therefore establish (2) for every
   P>=1, with common finite-horizon constants.

The listed corollary examples tanh, sigmoid, arctan and smooth periodic
activations satisfy these additional bounds. The text correctly makes no
corresponding assertion about all small orders for the new clock and does
not include unbounded GELU in this stronger old-clock corollary. No proof
of practical constants, numerical stability or uniformity in T/H/n/M is
introduced by the addition. This remains a collaborative internal full
check rather than a promotion review; no experiments, root-file edits or
Git operations were performed.
