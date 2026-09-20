# Continuous hidden flow with rare activation of deadline-accelerated readout noise

2026-09-19. Independent scoped theoretical route. Frozen candidate before
cross-route comparison; not independently reviewed or promoted. No experiment.

## 1. Outcome and exact scope

There is an unconditional construction, at canonical orders p=1,2 and for
every finite compatible binary circle dataset, that has all of the following:

* both hidden blocks have continuous paths and follow their original
  gradient-flow equations almost everywhere, with their original unit
  mobilities; the equations also hold in integral form across readout jumps;
* only the readout has jumps; original readout GF also runs between jumps;
* the full state converges strongly almost surely to a finite exact fit;
* expected loss decreases exponentially in physical time;
* as epsilon tends to zero, the entire state path converges to original GF
  uniformly on each fixed compact time interval, in probability.

The construction is explicitly **rare intervention, followed by large or
small accepted perturbations with a singular proposal clock**. Epsilon controls
the rate at which the intervention is activated, not the amplitudes of its
subsequent perturbations. It is not ordinary small Brownian noise, SGD, or a
homogeneous Poisson process of small kicks. The singular clock is the price of
retaining a deterministic bound on hidden travel while GF runs continuously.
Sections 7–8 derive the exact remaining obstruction for simpler noise laws.

The scientific inputs were only complete RATE_ADAPTED_READOUT.md,
RATE_SMALL_READOUT_NOISE.md, ESCAPE_AND_LIMITS.md, INITIAL_EXCLUSION.md,
INITIAL_REVIEW.md and established global_nonlinear.md spans 13161–13786 and
15146–15528. No other study, route, review, history, or numerical output was
consulted. The required rigorous-mathematics and conjecture-investigation
skills and their research-contract, hostile-audit, and bounded-search process
references were read. All new ingredients used below are derived here.

## 2. Model and contract

Fix the canonical bounded dictionaries b1,b2 at p=1 or p=2. After exact
aggregation of duplicates and antipodes, let u_i be distinct modulo antipodes,
y_i in {-1,1}, and mu_i>0 with sum mu_i=1. On the fixed canonical carriers,

\[
 a_i=E_1[b_1\tanh(w\cdot u_i)],\quad
 H_i=\tanh(b_2^TMa_i),\quad f_i=E_2[cH_i],
\]
\[
 (Ah)_i=\sqrt{\mu_i}E_2[hH_i],\quad
 K=AA^*,\quad e_i=\sqrt{\mu_i}(f_i-y_i),\quad L=|e|^2.
 \tag{1}
\]

The state is S=(w,c,M) in the physical Hilbert space
L2(lambda1;R2) plus L2(lambda2) plus the finite matrix space, with its usual
product metric. Write F=-grad L for the full physical vector field in
ESCAPE_AND_LIMITS.md (1). The initialized state is S0=(g,0,D), L0=1.
Initial feature independence proved in INITIAL_EXCLUSION.md (18), together
with INITIAL_REVIEW.md Section 6, gives K(S0)>0 for every dataset here.
The fixed-order vector field is locally Lipschitz on Hilbert balls and has
global finite-time GF continuation, as proved in ESCAPE_AND_LIMITS.md Section 1.

Our closeness statement is

\[
 \sup_{0\le t\le T}\|S_\epsilon(t)-S^0(t)\|_{\mathcal H}
       \longrightarrow0\quad\hbox{in probability},\qquad T<\infty,
 \tag{2}
\]

where S^0 is original GF with exactly the same initialization. Jump paths
are compared in the uniform norm; (2) is stronger than merely comparing
predictions. It is a fixed-order, exact-population theorem. No neural-width,
quadrature, order-to-infinity, or numerical-time limit is being exchanged.
All coefficients use only current state, initial marks, finite data, and
fresh independent scalar or finite-dimensional randomness. No target path or
fitted state is supplied. The process is restartable from its current state
plus its activation flag, elapsed stage age, and fixed intervention constants.

## 3. Positive Gram at an independent random GF time

**Lemma.** Along the original canonical fixed-order GF, det K(t) is a real
analytic function of physical time on every finite interval. Consequently
the times at which K(t) fails to be positive definite form a locally finite,
and hence countable, subset of [0,infinity).

**Proof.** Use the characteristic Banach space

\[
 X=L^\infty(\lambda_1;\mathbb R^2)
   \oplus L^\infty(\lambda_2)
   \oplus\mathbb R^{d_2\times d_1}
\]

for the coordinates (w-g,c,M). Canonical GF stays in X on every compact
time interval: the supplied energy and velocity bounds give finite bounds
on c, M, and w-g in the stated norms. At any real state in X, complexify
these coordinates. Tanh is holomorphic, bounded, and has bounded first
derivative on the strip |Im z|<pi/4, uniformly over Re z. A sufficiently
small complex X ball about this real state keeps every w dot u_i in this
strip. Bounded b1,b2 and the local bounds on a_i and M ensure, after possibly
shrinking the ball, that every b2^T M a_i also stays in the strip. The
unbounded frozen g is real and does not affect these imaginary-part bounds.

Every operation in F is then a bounded multilinear product, an expectation,
or a holomorphic Nemytskii map with a common strip bound. Uniform Cauchy
estimates on a narrower strip give norm-convergent Taylor series for the
Nemytskii maps. Thus F extends holomorphically to this complex X ball, and
is bounded and Lipschitz on a smaller ball.

For completeness, solve there on a small complex time disk by Picard
iteration z_{n+1}(t)=z0+integral_0^t F(z_n(s)) ds. Choose the time radius
so that its product with the bound on F remains inside the smaller ball
and its product with the Lipschitz constant is less than one. The iterates
are holomorphic and converge uniformly in X, by the contraction estimate;
the limit is holomorphic and solves z'=F(z). Restriction to real time equals
the existing GF by local uniqueness. Repeating at each reached real state
proves local real analyticity everywhere on the GF trajectory.

Each entry K_ij(t)=sqrt(mu_i mu_j) E[H_i(t)H_j(t)] is therefore real
analytic. Its complex extension uses the bilinear product H_i H_j, without
complex conjugation; this equals the required real Gram entry on real time.
Hence det K is real analytic. It is nonzero at t=0. A real analytic scalar
function on a connected interval that has an accumulating sequence of zeros
is identically zero: at an interior accumulation point its first nonzero
Taylor coefficient, if one existed, would isolate the zero; if none exists,
the Taylor series vanishes nearby, and overlapping Taylor neighborhoods
continue that identity throughout the interval. Applied also across each
finite endpoint using the local extension, this rules out accumulation on
compact intervals. Since K is positive semidefinite, det K>0 is equivalent
to K>0. This proves the lemma.

Draw a scalar activation time T_epsilon with exponential rate epsilon>0,
independently of everything else, and run exact original GF until then.
The preceding countable exceptional set has probability zero under this
absolutely continuous law, so K(S^0(T_epsilon))>0 almost surely. This does
not claim that the original Gram stays positive at every deterministic time.
Exceptional realizations may be assigned original GF forever without
changing any almost-sure or expectation conclusion.

## 4. Always-running GF and a finite deadline for each successful kick

At activation, write S_* for the reached state, ell_*=L(S_*),
C_*=||c_*||2 and M_*=||M(S_*)||F. If ell_*=0, remain at this exact fit.
Otherwise fix theta in (0,1), sigma>0, and nu>0, all independent of epsilon.
Put B_l=ess sup|b_l| and B=B1 B2. Define once at activation

\[
 \kappa_*=\lambda_{\min}(K(S_*)),\quad\kappa=\kappa_*/2,
 \quad\rho=\frac{\kappa_*}{4B\max(1,M_*)},\quad
 \bar M=M_*+\rho,
\]
\[
 R=\frac{\sqrt{\ell_*}}{1-\sqrt\theta},\qquad
 \bar C=C_*+\left[\frac{1+\sqrt\theta}{\sqrt\kappa}+2\right]R,
\]
\[
 h=\min\left\{1,
 \frac{\rho}{4B\bar C(1+\bar M)R}\right\}>0.
 \tag{3}
\]

The following stage starts immediately at activation and again after each
accepted jump. Let s be the physical time elapsed since this stage began.
Throughout the stage run all blocks with their exact original F velocities.
Generate proposal times by an independent inhomogeneous Poisson clock with

\[
 \lambda(s)=\frac{\nu}{h-s},\qquad 0\le s<h.
 \tag{4}
\]

At a proposal time, at its current state and current loss ell>0, draw an
independent Z~N(0,sigma^2 I_m), and propose

\[
 \delta c=\sqrt{\ell}\,A^*K^{-1}Z.                     \tag{5}
\]

Accept this jump precisely if its new loss is at most theta ell. Rejecting
does nothing and takes no extra physical time. In particular GF is never
paused during failures. After acceptance reset s to zero and use the same
fixed constants (3). Proposal evaluations are ideal exact population
operations; this is a physical-time theorem, not a finite computation-cost
bound. This declared clock is not the earlier fixed-duration trial clock.

We now prove all inverses used in (5) exist and all stages succeed before h.
Neither is assumed.

### 4.1 Deterministic tube bounds for every finite admissible history

On the hidden tube

\[
 ||w-w_*||_2+||M-M(S_*)||_F<\rho,
 \tag{6}
\]

the elementary feature subtraction in RATE_ADAPTED_READOUT.md (5) gives

\[
 ||K-K(S_*)||_{op}
 \le2B\max(1,M_*)
       (||w-w_*||_2+||M-M(S_*)||_F),
\]

so K>=kappa I. A readout jump leaves K unchanged. At fixed hidden state,
(5) yields exactly e^trial=e+sqrt(ell)Z. Therefore its conditional success
probability is the state-independent number

\[
 q=\Pr\{|e_1+\sigma G|^2\le\theta\}>0,
       \qquad G\sim N(0,I_m).                         \tag{7}
\]

Every accepted jump has

\[
 ||\delta c||_2\le
       \frac{1+\sqrt\theta}{\sqrt\kappa}\sqrt{\ell}.
 \tag{8}
\]

Let ell_j be the loss at the start of stage j, with ell_0=ell_*.
GF decreases loss and acceptance multiplies its current value by at most
theta, giving ell_j<=theta^j ell_*. Thus sum sqrt(ell_j)<=R. Until a
possible first exit from (6), any finite sequence of completed stages of
duration less than h, followed by a partial stage of duration at most h,
obeys the original velocity estimates

\[
 ||c'||_2\le2\sqrt L,\quad
 ||M'||_F\le2B||c||_2\sqrt L,\quad
 ||w'||_2\le2B||M||_F||c||_2\sqrt L.                  \tag{9}
\]

Equations (8), h<=1, and the geometric sum imply ||c||2<=bar C.
Integrating hidden speeds then gives total hidden travel at most

\[
 2Bh\bar C(1+\bar M)R\le\rho/2.                    \tag{10}
\]

This strictly prevents a first exit, including one during a partial stage.
It also proves the inverse stays bounded on the entire stage up to its
deadline, even if no acceptance had yet occurred. Thus the geometric and
clock arguments do not assume one another circularly.

### 4.2 Stage success, lack of explosion, and strong endpoint

For s<h the cumulative intensity in (4) is nu log[h/(h-s)]<infinity.
There are finitely many proposals before s almost surely. Each conditional
success probability is exactly q, regardless of the trajectory and earlier
rejections. Repeated conditioning, or first conditioning on the Poisson
times and multiplying the conditional rejection probabilities, gives

\[
 \Pr\{W_j>s\mid\hbox{history at stage start}\}
       =(1-s/h)^{\nu q},\qquad 0\le s<h,              \tag{11}
\]

where W_j is the duration until acceptance. The right side tends to zero as
s increases to h. Hence each stage succeeds strictly before its deadline
almost surely, and uses only finitely many proposals. Countably many such
probability-one statements hold simultaneously.

Conditioned on activation and its constants, the durations W_j are iid
with the law (11): their conditional law given every earlier stage is
always that same law. In particular P(W_j>=h/2)=2^(-nu q)>0. For every N,
the probability of no such long stage after N is the limit of
(1-2^(-nu q))^k, namely zero. A countable union over N proves infinitely
many long stages occur, so sum W_j=infinity. There is no finite physical
time accumulation of stages or proposals. The original vector field has
finite-time continuation between these finitely many actual jumps, so the
process is globally defined. If exact zero occurs, stopping is harmless.

The sum of accepted jump norms is bounded by (8) and R. The integrated
readout speed is at most 2hR; the matrix speed has total integral at most
2Bh bar C R; and the row speed has total integral at most
2Bh bar M bar C R. Thus the full path has finite total variation after
activation in the physical Hilbert norm. The Hilbert space is complete,
so S_epsilon(t) has a finite strong limit as t tends to infinity. There
are infinitely many accepted stages unless zero has already been attained,
and ell_j<=theta^j ell_*. Continuity of the finite-data prediction map
in this norm makes the limiting loss zero. These are unconditional
almost-sure statements from the canonical initialization.

## 5. Physical-time rates and the epsilon limit

Put a=log(1/theta)>0. Since every stage lasts less than h<=1, by time
t>=T_epsilon at least floor((t-T_epsilon)/h) stages have finished. Consequently

\[
 L_\epsilon(t)\le
 \ell_*\theta^{\lfloor(t-T_\epsilon)/h\rfloor}
 \le \theta^{-1}e^{-a(t-T_\epsilon)},\quad t\ge T_\epsilon.
 \tag{12}
\]

Before activation L<=1. If 0<epsilon<a, integration against the exponential
activation density gives

\[
 E L_\epsilon(t)
 \le e^{-\epsilon t}
   +\theta^{-1}\epsilon
       \frac{e^{-\epsilon t}-e^{-a t}}{a-\epsilon}
 \le\left(1+\frac{\epsilon}{\theta(a-\epsilon)}\right)e^{-\epsilon t}.
 \tag{13}
\]

For example choose theta=1/4 and 0<epsilon<=log(4)/2. This is an explicit
unconditional exponential bound in the unchanged GF physical-time units.
It deteriorates as epsilon decreases, because interventions become rare.
Its prefactor is at most 1+1/theta over the stated epsilon range. The
almost-sure postactivation loss exponent in (12) is at least a, with a
finite random prefactor theta^(-1) exp(a T_epsilon).

For a tolerance 0<delta<1, at most
J_delta=ceil(log(1/delta)/a) successful stages suffice. Thus the loss hitting
time satisfies

\[
 \tau_\delta\le T_\epsilon+hJ_\delta
       \le T_\epsilon+J_\delta\quad\hbox{almost surely},
 \qquad E\tau_\delta\le\epsilon^{-1}+J_\delta.
 \tag{14}
\]

The absence of a data-conditioning factor in (13)–(14) is purchased by the
unbounded near-deadline evaluation rate and the Gram inverse, whose physical
kick sizes and number of evaluations may be very costly. A stage's accepted
proposal index is geometric(q), so its mean count is 1/q; inverting a poorly
conditioned Gram is still a separate cost.

For each fixed T and eta>0 the construction agrees **exactly** with original
GF on [0,T] whenever T_epsilon>T. Hence

\[
 \Pr\left\{\sup_{t\le T}||S_\epsilon(t)-S^0(t)||_{\mathcal H}>\eta\right\}
 \le1-e^{-\epsilon T}\le\epsilon T.                  \tag{15}
\]

This proves (2) without any moments of the possibly large postactivation
states. Coupling T_epsilon=E/epsilon with one E~Exp(1), each sample path
agrees with GF on every prescribed compact interval for all sufficiently
small epsilon. Thus this coupling even gives locally uniform almost-sure
convergence. It does not give unbounded-norm moment convergence or uniform
closeness on [0,infinity). Since 0<=L<=1, fixed-time expected losses also
converge to original GF's loss by the elementary bound
|E L_epsilon(t)-L^0(t)|<=P(T_epsilon<=t).

The limit order matters:

\[
 \lim_{\epsilon\downarrow0}\lim_{t\to\infty}E L_\epsilon(t)=0,
 \qquad
 \lim_{t\to\infty}\lim_{\epsilon\downarrow0}E L_\epsilon(t)
       =\lim_{t\to\infty}L^0(t),                     \tag{16}
\]

and the value of the latter original-GF limit remains unresolved. This
construction neither identifies the limiting fitted state as epsilon tends
to zero nor proves that the original GF fits.

## 6. Why this changes the dynamics, and what is not claimed

The hidden paths are continuous and evolve with the exact original hidden
velocities almost everywhere. Readout jumps can change those velocities
abruptly, so a classical hidden derivative at a jump time is not asserted.
Their equations are never projected, slowed,
reinitialized, or frozen. Those velocities nevertheless respond to accepted
readout jumps, and the intervention is designed to keep the hidden state
within a small, data-dependent tube around the randomly reached state S_*.

The readout proposals use current population features, the Gram inverse,
and loss magnitude. They do not use a desired fitted readout or the direction
-e in their Gaussian mean. Acceptance introduces a deliberate descent bias.
The output noise remains isotropic before acceptance, but the accepted law
is not centered. The stage deadline, singular attempt intensity, and zero
physical evaluation duration are all extra algorithmic structure. Thus the
theorem answers the stated continuity and compact-time-limit requirements
with a precisely disclosed optimizer; it does not justify calling that
optimizer ordinary infinitesimal stochastic GF.

The analytic random-time lemma is essential for arbitrary late activation.
At p=3, initial Gram positivity was not established by the permitted inputs,
so no unconditional canonical p=3 conclusion is claimed. The conditional
construction does apply at any fixed bounded dictionary with an analytic
canonical characteristic trajectory and initially positive readout Gram.

## 7. Exact diagnostic for genuinely small continuous readout diffusion

Consider instead the direct Itô candidate

\[
 dw=F_wdt,\quad dM=F_Mdt,\quad
 dc=F_cdt+\epsilon\sqrt L\,A^*dB_t,
 \tag{17}
\]

where B is m-dimensional Brownian motion. This paragraph gives identities
up to any bounded-state stopping time on which a solution exists; it does
not import an all-time SDE theorem or assume future boundedness. The hidden
blocks have finite variation, and readout enters predictions linearly, so
the finite-dimensional Itô calculation is exact. Let K_full be the weighted
full tangent Gram (readout plus both hidden-block Grams), with K_full>=K.
Then

\[
 de=-2K_{full}e\,dt+\epsilon\sqrt L\,K\,dB_t,
\]
\[
 dL=\left[-4e^TK_{full}e
       +\epsilon^2 L\operatorname{tr}(K^2)\right]dt
       +2\epsilon\sqrt L\,e^TK\,dB_t.               \tag{18}
\]

Since ||A||<=1 and tr K<=1, tr(K^2)<=1. If one separately proved the
deterministic lower bound K>=kappa I for all reached states, then the drift
would be at most -(4kappa-epsilon^2)L. For epsilon^2<4kappa, localization
and sufficient integrability would yield the corresponding expectation
rate. The supplied initialization theorem gives K(0)>0 only. It supplies
neither that global lower bound nor integrability of the SDE. Therefore
(18) does not prove an unconditional rate for (17).

There is also a genuine ambient-state obstruction: at every state
(w,c,M)=(w,0,0), H_i=0, A=0, and every GF block vanishes. The coefficient
in (17) is zero there as well, so this positive-loss state is exactly
absorbing for every epsilon. More generally at w=0,M=0, arbitrary noise
acting only on c cannot activate either hidden block: a_i=H_i=0 makes
M'=0, while M=0 makes w'=0. These examples refute a theorem from every
ambient initial state, even for some stronger readout noises. They do not
refute fitting from the particular canonical initialized state, which is
different and starts with positive Gram.

For nonvanishing additive readout diffusion dc=F_cdt+epsilon Q^(1/2)dB,
the exact additional drift is epsilon^2 tr(A Q A*). At any fitted state
where this trace is positive, the process immediately generates prediction
variance. Thus persistent prediction-active additive diffusion is not a
process absorbed at exact fits; vanishing noise or loss-weighting is needed
for the strong fitted-endpoint property. This local observation is not a
global invariant-measure theorem.

## 8. Ordinary Poisson small kicks: precise surviving gap

Run full GF continuously, and at homogeneous Poisson rate lambda>0 propose

\[
 \delta c=\epsilon\sqrt L\,A^*G,
       \qquad G\sim N(0,I_m),                        \tag{19}
\]

accepting any loss decrease. This process is globally well defined at every
finite time: there are finitely many proposals, each has finite Hilbert
norm, and intervening full GF has global finite-time existence. Its loss
is nonincreasing. Every proposed norm is at most epsilon sqrt(L0)|G|,
so on a fixed interval the cumulative jump norm tends to zero almost surely
under a common Poisson/mark coupling as epsilon tends to zero. The finite
number of jump times and continuous dependence of locally Lipschitz GF on
bounded finite-time trajectories prove uniform compact-time convergence
to original GF. One can prove this directly by induction over the finitely
many proposal times, applying the local Gronwall bound between them.

At a state with K>=kappa I and epsilon<=kappa/(4m), the Gaussian event
in RATE_SMALL_READOUT_NOISE.md Section 3 has probability at least
q_*=exp(-2)/(2 sqrt(2pi)) and gives

\[
 L^{trial}/L\le1-2\epsilon\kappa+4m\epsilon^2
                 \le1-\epsilon\kappa.              \tag{20}
\]

If such a deterministic kappa bound were valid at all reached states,
the full GF only helps and conditioning over each small clock interval
would yield E L(t)<=L0 exp(-lambda q_* epsilon kappa t). The same bound
would imply integrability of sqrt L over time in expectation. Because
the expected jump variation is bounded by
lambda epsilon E|G| integral E sqrt L dt, the readout total variation
would be finite almost surely. Equations (9) would then give finite total
variation of M and w and a strong fitted endpoint. Thus one specific
uniform Gram lemma would close this entire route.

It is exactly the unproved lemma. A homogeneous Poisson process permits
arbitrarily long first waiting times with positive probability. Therefore
the old deterministic argument that allocates at most h units of GF per
fractional loss decrease cannot be reused. One cannot insert a bound on
hidden displacement across that wait, or a uniform kappa, just because
canonical K(0)>0. The analytic lemma in Section 3 only excludes Gram zeros
at almost every finite time; it supplies no positive all-time lower bound
and no lower bound as t tends to infinity.

Consequently ordinary small accepted Poisson readout noise has exact
finite-time well-posedness and a genuine small-amplitude GF limit, but an
unconditional canonical all-time fitting/rate theorem remains open here.
The construction in Sections 3–5 closes that gap by imposing finite stage
deadlines after rare activation. These two limits must not be conflated.

## 9. Claim ledger and hostile checks

| Claim | Status | Decisive dependency or limitation |
|---|---|---|
| Canonical K(0)>0 at p=1,2 | supplied internally checked theorem | exact finite compatible circle data |
| det K along original GF is analytic | proved here | bounded-characteristic finite-order dynamics |
| Independent exponential activation meets K>0 | proved here | analyticity plus K(0)>0, no global Gram bound |
| Deadline proposal process globally well defined | candidate proof complete | tube before every deadline and nonexploding renewal times |
| Full hidden original GF remains continuously active | exact by construction | readout kicks alter its current-state forcing |
| Strong finite fitted endpoint | candidate proof complete | summable accepted jumps and all-block travel |
| Expected exponential physical-time rate | candidate proof complete | (13), ideal zero-duration proposal evaluations |
| epsilon->0 compact-time state closeness | exact coupling proof | rare activation, not shrinking postactivation amplitudes |
| Ordinary small Brownian-noise unconditional fitting | open | (18) lacks global coercivity and SDE continuation/integrability |
| Ordinary small accepted Poisson-noise fitting | open | uniform Gram lemma absent |
| Original GF convergence to zero | unchanged/open | long-time and epsilon limits cannot be exchanged |

Hostile checks: no hidden feature freezing; no deterministic bound on a
homogeneous Poisson waiting time; no initial-Gram-to-global-Gram inference;
no boundedness-to-precompactness inference; no infinite-dimensional Itô
smoothness assertion; no future-path coefficient; no conflation of physical
time with finite evaluation cost; no conclusion for every ambient initial
state; no unproved canonical p=3 extension; no exchange of the limits (16).

Registry recommendation: **complete candidate for the expressly disclosed
rare-intervention/deadline construction; open for genuinely small continuous
or homogeneous Poisson readout noise.** The latter requires a new invariant,
coercivity argument, or quantified escape mechanism, rather than a repetition
of the initialization and finite-time energy bounds.
