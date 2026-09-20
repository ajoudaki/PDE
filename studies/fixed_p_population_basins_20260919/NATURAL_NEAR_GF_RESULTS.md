# Continuous perturbations and the precise meaning of approaching GF

2026-09-19. Lead synthesis and combined theoretical candidate. This note
uses only the completed same-study routes identified below. It contains
a new combination argument and therefore requires its own internal check.
No experiments, numerical-runtime claim, or promotion.

## 1. The useful positive results, without conflating them

There are now three distinct ways to retain a fitting theorem while
moving beyond paused hidden evolution:

1. A continuous current-state conditioning correction gives pathwise
   exponential loss decay, continuous motion of every block, and a
   finite fitted endpoint. It can include an explicitly small bounded
   colored readout noise. Its vector field approaches ordinary GF on
   bounded regions with nonsingular feature Gram, but the correction
   can become strong near degeneracy.
2. Rare accepted global offers allow completely original GF between
   events and give quantitative rates plus unconditional compact-time
   approximation to GF as event frequency tends to zero. The offers
   remain global replacements.
3. Rare activation of a deadline-controlled readout process keeps the
   original hidden equations running at every time. It gives rates
   and compact-time approximation, but uses a singular proposal clock
   and later confines hidden travel through successful readout jumps.

The first route is the main continuous optimizer result. It does not
derive its convergence from noise alone. The second and third routes
establish a weaker rare-intervention meaning of proximity to GF.

Sections 2--4 below combine the first route with the analytic
random-time lemma from the third. The combined process has continuous
state paths, exponential expected physical-time loss decay and an
unconditional compact-time GF limit. Its approximation parameter also
delays activation of the conditioning correction. That delay must
remain explicit; it is not a uniform small-drift theorem.

## 2. Exact continuously evolving construction

Use the canonical p=1 or p=2 finite compatible binary circle closure,
with complete fixed marks, original population Hilbert metric,
initialization S0=(g,0,D), and L0=1. Combine compatible duplicate and
antipodal data into m representatives. Let

\[
H_i=\phi(b_2^TMa_i),\quad
a_i=E_1[b_1\phi(w\cdot x_i/\sqrt2)],\quad
L=\sum_i\mu_i(E_2[cH_i]-y_i)^2,\quad \phi=\tanh,
\]
\[
K_{ij}=\sqrt{\mu_i\mu_j}E_2[H_iH_j].
\tag{1}
\]

The exact original vector field is F=-nabla L. Canonical K0>0 is
proved in INITIAL_EXCLUSION.md and its supplied p=1 extension.
The physical time t below is always the time parameter of this ODE
and its continuous modifications; there is no proposal-evaluation
clock or held-state phase.

Fix epsilon>0 and 0<=nu<=epsilon. Draw a single independent activation
time T_epsilon~Exp(epsilon). Run original GF exactly until that time.
At activation, retain the full current state; no parameter is reset.
Almost surely its Gram is positive, as justified in Section 3.

From activation onward run the continuous additive-noise construction
NATURAL_TANGENT_NOISE.md:

\[
\begin{split}
R&=\operatorname{tr}K^{-1},\qquad
\Phi_\varepsilon=L(1+\varepsilon R),\\
z&=\nabla_cL,\qquad
\beta_\varepsilon=
\frac{\varepsilon L[-\langle\nabla L,\nabla R\rangle]_+}{\|z\|^2},\\
B(S)u&=\frac{\|z\|^2u-z\langle z,u\rangle}{1+\|z\|^2},\\
\dot S&=-\nabla\Phi_\varepsilon
       -\beta_\varepsilon(0,z,0)
       +(0,\nu\sqrt L B(S)U_t,0).
\end{split}
\tag{2}
\]

Here U_t is independent bounded symmetric colored readout noise,
piecewise constant with finitely many refreshes on bounded intervals,
and ||U_t||<=1. A fixed known unit readout field times independent
random signs at fixed physical intervals is enough. Thus no Gram
at activation is needed to choose the noise directions.

All gradients are in the same physical metric. Define beta=0 at zero
loss and absorb there. A finite positive-Gram-domain exit is also
absorbing only if its limiting loss is zero, as the dependency proves.
On the probability-zero event of a singular activation Gram, define
the process to continue original GF; this measurable exceptional
convention does not change any almost-sure or expectation result.

There are no state jumps at activation or at noise-refresh times.
The enlarged restart state consists of the population state,
activation flag, noise refresh phase and current noise value.
Before activation the exponential law is memoryless; after activation
the fixed regularization/noise parameters determine the continuation.
All coefficients are current-state quantities and declared data;
no future-trained state or original trajectory is supplied.

## 3. Activation is almost surely well defined

NATURAL_CONTINUOUS_ROUTE.md, Section 3, proves that det K(S^0(t)) along
original canonical GF is real analytic in time. Its complete proof
uses the Banach coordinates (w-g,c,M) in L-infinity x L-infinity x
finite matrices. They stay bounded on every finite interval under
canonical GF. Complex tanh is uniformly holomorphic on a fixed strip
around the real axis, so the vector field is locally holomorphic
in those coordinates even though the frozen real Gaussian g is
unbounded. Complex Picard contraction proves local time analyticity.
The Gram entries and determinant are analytic compositions.

Since det K(0)>0, the determinant is not identically zero. The
one-variable analytic zero argument makes its exceptional times
locally finite, hence countable. An independent exponential time
hits none with probability one. This supplies exactly the needed
activation premise without asserting positivity at every fixed time.

The bounded-carrier argument concerns original GF before activation;
no time analyticity of the subsequently random corrected flow is
assumed or needed.

## 4. Combined physical-time theorem and proof

For every epsilon>0, the process above is globally defined almost
surely, has continuous state paths and nonincreasing actual loss,
and has a finite strong zero-loss population endpoint almost surely.
Moreover

\[
E L_\varepsilon(t)
\le L_0\left(\frac43e^{-\varepsilon t}
             -\frac13e^{-4\varepsilon t}\right)
\le\frac43L_0e^{-\varepsilon t}.
\tag{3}
\]

For every fixed T<infinity and d>0,

\[
P\left\{\sup_{0\le t\le T}
\|S_\varepsilon(t)-S^0(t)\|_{\mathcal H}>d\right\}
\le1-e^{-\varepsilon T}\le\varepsilon T.
\tag{4}
\]

For 0<a<L0, its actual physical hitting time obeys

\[
E\tau_a\le\frac1\varepsilon+
\frac1{4\varepsilon}\log\frac{L_0}{a},\qquad
P(\tau_a>t)\le
\min\left\{1,\frac{4L_0}{3a}e^{-\varepsilon t}\right\}.
\tag{5}
\]

**Proof.** Before activation, original GF is globally defined and
decreases loss. Section 3 ensures a finite positive-Gram state at
activation almost surely. NATURAL_CONDITIONING_FLOW.md proves local
regularity, positive-loss boundary avoidance, all-time continuation
with explicit fitted-endpoint absorption, and finite total parameter
travel for the conditioning drift. NATURAL_TANGENT_NOISE.md proves
that the bounded tangent noise preserves its pathwise loss and
potential inequalities and adds finite total path length. Applying
those complete results to the actual activation state gives

\[
L_\varepsilon(t)\le
L(S^0(T_\varepsilon))
e^{-4\varepsilon(t-T_\varepsilon)}
\le L_0e^{-4\varepsilon(t-T_\varepsilon)},\quad
t\ge T_\varepsilon.
\tag{6}
\]

Their hypotheses require only finite state and positive current Gram,
not canonical fields at the time the correction begins. The random
potential at activation can be very large but is finite almost
surely. No moment bound on it is needed for (3), which uses the
actual-loss estimate (6) with prefactor at most L0.

Integrating the event T_epsilon>t and the density on [0,t] gives

\[
\begin{split}
E L_\varepsilon(t)
&\le L_0e^{-\varepsilon t}
 +L_0\int_0^t \varepsilon e^{-\varepsilon s}
                       e^{-4\varepsilon(t-s)}\,ds\\
&=L_0\left(\frac43e^{-\varepsilon t}
             -\frac13e^{-4\varepsilon t}\right).
\end{split}
\]

This proves (3). The postactivation time to loss a is at most
(4epsilon)^(-1) log(L0/a), so E T_epsilon=1/epsilon gives the
first part of (5). Monotonicity and Markov's inequality applied
to (3) give its second part. The total finite original-GF path
before activation followed by the almost-sure finite corrected
path gives the claimed strong endpoint.

Before activation the process equals original GF by uniqueness.
The event T_epsilon>T therefore implies identical state paths
on [0,T], proving (4). Under the coupling T_epsilon=E/epsilon
with one E~Exp(1), the paths are eventually exactly equal on
each fixed compact interval as epsilon decreases to zero.
Countably many integer horizons give almost-sure local uniform
convergence under that coupling. This is stronger than (4) in
coupling form, but not uniform approximation on [0,infinity).

## 5. Closeness claims that must remain separate

Immediate activation at time zero is also a valid algorithm and
has the stronger pathwise estimate L(t)<=L0 exp(-4epsilon t).
NATURAL_TANGENT_NOISE.md proves a quantitative O(epsilon+nu)
state comparison to original GF on every finite reference interval
on which its Gram remains positive throughout.

Delayed random activation supplies unconditional compact-time
closeness in (4), even if original GF has an isolated Gram
singularity. It does so because activation becomes rare, not
because all later conditioning forces are uniformly small.
It would be misleading to conceal this switching mechanism or
present (4) as proof of uniformly small drift along all paths.

Along every initialized trajectory, the actual random noise velocity
in (2) is bounded by nu sqrt L<=epsilon sqrt L0. However the deterministic
conditioning correction contains K^{-1} and its derivatives and
can become large near degeneracy. Thus the full modification is
not merely an arbitrarily small additive-noise version of GF.

The long-time and small-parameter limits cannot be exchanged by
this theorem. The rate epsilon in (3) tends to zero precisely
in the approximation limit; on the guaranteed fitting scale
t of order epsilon^{-1}, activation is no longer unlikely.

More generally, a nondegenerating uniform exponential bound would
already imply the unresolved original-GF fitting result. Indeed,
suppose S_epsilon(t)->S^0(t) in probability for each fixed t and
E L(S_epsilon(t))<=C exp(-lambda t) with C,lambda>0 independent
of epsilon. Continuity of L gives convergence of losses in
probability. Select an almost-sure convergent subsequence at that
t; nonnegativity and the elementary Fatou inequality yield
L(S^0(t))<=C exp(-lambda t). This holds for every fixed t,
so original GF would itself fit exponentially. The argument does
not forbid such a theorem; it identifies its true strength.

## 6. Mechanism comparison and unresolved target

| Process | Hidden evolution and state paths | Rate and GF limit | Main limitation |
|---|---|---|---|
| Immediate conditioning correction, with optional tangent noise | All blocks continuously evolve; no neighborhood around initialization imposed | Pathwise exponential actual loss; locally O(epsilon+nu) close to GF where the reference Gram stays positive | Conditioning force can become large near degeneracy |
| Rare activation of the same continuous correction | Original GF until activation, continuous corrected fields afterward | Expected exponential loss (3), unconditional compact-time GF limit (4), strong endpoint | Approximation partly comes from delaying activation |
| Rare global auxiliary offers | Original GF between events, possibly large state jumps | Expected exponential loss and unconditional compact-time GF limit | Global replacement and separate fixed-feature search |
| Rare activation of deadline readout kicks | Original hidden GF continuously; readout jumps | Expected exponential loss, strong endpoint, compact-time GF limit | Singular proposal clock and hidden travel controlled after activation |
| Ordinary GF plus homogeneous small accepted readout kicks | Original hidden GF continuously | Exact finite-time existence and small-amplitude compact-time GF limit | Unconditional fitting/rate still lacks a global Gram or escape estimate |

The stronger requested interpretation remains unresolved: original
full GF plus only a uniformly small local random perturbation, no
strong conditioning correction, rare global intervention, or hidden
travel restriction, with an unconditional all-time rate from canonical
initialization on every compatible dataset. No counterexample to
that canonical statement was proved in this continuation.

The continuous potential is a substantive positive optimizer result,
but its guarantee comes from explicitly maintaining the cost of
correcting outputs through the current representation. It is not a
proof that ordinary noise alone repairs every bad equilibrium.

## 7. Evidence and dependencies

Complete original independent routes:
NATURAL_RARE_ROUTE.md and NATURAL_CONTINUOUS_ROUTE.md.
Lead continuous proofs:
NATURAL_CONDITIONING_FLOW.md and NATURAL_TANGENT_NOISE.md.
The present combination uses only the latter two proofs and the
analytic random-time lemma of the continuous route. All new
probability, clock, limit and hitting-time calculations are given
above. This combination is a candidate until independently checked.
No numerical evidence or external stochastic convergence theorem
is used.
