# Slow orders: an all-time Gaussian envelope with a dense-only width floor

28 September 2026. Scoped internal proof continuation. The unchanged autonomous
old clock is retained, the initial readout is exactly zero, and the label RMS
is fixed and positive. No experiment, external search, further delegation,
population-closure existence assumption, or trained finite-network Gaussian
tail assumption is used.

**Result.** Under the small-label Gram-gap hypotheses already used in
`SMALL_LABEL_ALLTIME_SYNTHESIS.md` and `SMALL_LABEL_GAUSSIAN.md`, there are
deterministic constants `C,kappa,c,A>0`, good initialization events `G_n` with
probability tending to one, and a nonnegative random floor `b_n -> 0` in
probability such that, simultaneously for every integer order `q>=1`,

\[
 \sup_{t\ge0}d_n(\widehat\theta_{n,q}(t),\theta_n^D(t))
 \le \frac Cq\exp\!\bigl(\kappa\sqrt{\log(e+q)}\bigr)+b_n
 \qquad\hbox{on }G_n.                                      \tag{1}
\]

The floor is constructed from **dense finite-network carrier tails alone**,
not from the closure discrepancy. In particular every fixed `0<gamma<1`
gives a bound `C_gamma q^-gamma+b_n`, after changing the floor by an
equivalent vanishing one if desired. Thus every deterministic `q_n -> infinity`
works, including `log n`, `log log n`, or orders below `sqrt(n)`. No rate in
`n` is supplied for the floor; (1) does not imply that it is smaller than
the displayed order term along any specified sequence.

The proof combines the all-time energy comparison with **integrated dense
carrier tails**. It uses the unconditional `q^-1` accumulated velocity
defect and therefore does not need the potentially singular dense history
quotient in the closure's terminal clock.

## 1. Contract, hypotheses, and imported statements

Fix depth, input dimension, finite data, canonical Gaussian hidden
initialization, tanh, canonical mobilities, and zero readout. Each dense
finite network and all its closure orders use the same initialized arrays.
Use exactly the old-clock raw moment equations and reconstruction of
`GENERAL_AUTONOMOUS_SYNTHESIS.md`, equations (1)--(3). In particular every
clock, residual, feature, and response used by the algorithm is its own.

The discrepancy is the maintained sum norm

\[
 d_n(\theta,\vartheta)=\frac{\|W_1-V_1\|_F}{\sqrt n}
   +\sum_{\ell=2}^L\|W_\ell-V_\ell\|_F
   +\frac{\|w-v\|_2}{\sqrt n}.                              \tag{2}
\]

The full readout sample Gram at the dense population initialization must
have a positive gap. A fixed compatible invariant residual subspace can
be substituted only when its invariance and gap have separately been
verified, as allowed in `SMALL_LABEL_GAUSSIAN.md`. Correlated data are
allowed; arbitrary inconsistent duplicate inputs are not silently supplied
with a nonexistent full Gram gap. Fix an admissible gap lower bound and
take the fixed label RMS `0<Y<=Y_*` small enough for both small-label input
reports. Constants below may depend on these fixed data, depth, Gaussian
convention, gap, and label bound, but never on width, order, or time.

The good events `G_n` impose the initialized operator and Gram bounds in
the small-label reports; their probabilities tend to one. All deterministic
comparisons below are on `G_n`. No assertion of a full Gram gap at widths
`n<m` is needed. Write `rho_n` for the dense finite residual RMS. The input
reports provide, simultaneously for all orders,

\[
 \int_0^\infty\rho_n\le S,\qquad
 \int_T^\infty\rho_n\le C Y e^{-\lambda T},\qquad
 \rho_n(t)\le C Y e^{-\lambda t},\qquad
 \varepsilon_q:=\int_0^\infty\|E_{n,q}(t)\|_{\rm sum}dt\le C/q.
                                                               \tag{3}
\]

Here `S<=CY`; the more precise defect bound is `CY^3/sqrt(q(q+1))`.
The common hidden operator bounds and dense backward RMS bounds hold
for every time. The learned part of each dense backward carrier is
pointwise bounded, by its exact dense history integral.

The all-time energy comparison, equation (3) of
`SMALL_LABEL_ALLTIME_SYNTHESIS.md`, is

\[
 d_{n,q}(t)\le C\varepsilon_q+
 C\int_0^t\rho_n(u)[d_{n,q}(u)+G_{n,q}(u)]\,du.                \tag{4}
\]

In `G_(n,q)`, the remaining unbounded multipliers are the initialized
dense carriers

\[
 k^n_{\ell,a}(t)=W_{0,\ell+1}^{\top}\delta^D_{\ell+1,a}(t)
 \quad(\ell<L),\qquad k^n_{L,a}=w_0=0.                       \tag{5}
\]

`SMALL_LABEL_GAUSSIAN.md` constructs the global dense population with
uniform Gaussian tails for the full backward carriers. Its initialized
carriers have the same type of tail bound: subtract the pointwise bounded
learned term, use a cutoff at half the threshold above twice that bound,
and enlarge the constants for the bounded range of smaller thresholds.
Thus there are fixed `A_0,c_0>0` such that

\[
 \sup_{t\ge0}\sum_\ell\max_a
 \|k^\infty_{\ell,a}(t)
             \mathbf1_{|k^\infty_{\ell,a}(t)|>M}\|_2
       \le A_0e^{-c_0M^2}\quad(M\ge1).                       \tag{6}
\]

This is a bound on each time marginal, uniform in time. It is not a
Gaussian moment of a path supremum.

## 2. A deterministic cutoff estimate in finite total activity

Define the actual dense empirical tail

\[
 H_n(M,t)=\sum_{\ell=1}^L\max_a
     \|k^n_{\ell,a}(t)\mathbf1_{|k^n_{\ell,a}(t)|>M}\|_{\rm RMS}.
                                                               \tag{7}
\]

The forward difference bound has constants independent of time on the
common physical ball. Since
`|tanh'(u)-tanh'(v)|<=min(2|u-v|,1)`, splitting at `M` gives

\[
 G_{n,q}(t)\le CM d_{n,q}(t)+H_n(M,t).                         \tag{8}
\]

Put

\[
 Z_n(M)=\mathbf1_{G_n}\int_0^\infty\rho_n(t)H_n(M,t)\,dt.       \tag{9}
\]

On `G_n`, insert (8) into (4) and apply the scalar integral comparison
with measure `rho_n(t)dt`. More explicitly, if
`b(t)=C epsilon_q+C integral_0^t rho_n H_n`, then `b` is increasing,
and successive substitution in (4) bounds `d(t)` by
`b(t) exp(C(1+M) integral_0^t rho_n)`. Taking the time supremum gives

\[
 E_{n,q}:=\sup_{t\ge0}d_{n,q}(t)
    \le C e^{\kappa_0 M}[q^{-1}+Z_n(M)],\qquad M\ge1.          \tag{10}
\]

The factor `exp(C(1+M)S)` has been absorbed into `C exp(kappa_0 M)`.
Its exponent has no physical horizon. This is the crucial improvement
over an `exp(C_T M)` estimate with uncontrolled horizon dependence.

The dense backward RMS and initialized operator bounds also give

\[
 0\le H_n(M,t)\le C Y\quad\hbox{on }G_n.                      \tag{11}
\]

Consequently `Z_n(M)` is uniformly bounded and is nonincreasing in `M`.
Equation (10) is valid simultaneously in order and cutoff for each finite
network on the event. It assumes no Gaussian estimate for that network.

## 3. Deriving fixed-cutoff transfer for actual dense carriers

The statement needed is deliberately weaker than a trained finite-network
Gaussian tail theorem: for every **fixed** `T,M` and `eta>0`,

\[
 \lim_{n\to\infty}\Pr\left\{G_n\cap
  \left[\sup_{t\le T}H_n(M,t)>A_1e^{-c_1M^2}+\eta\right]
                    \right\}=0,                             \tag{12}
\]

with `A_1,c_1` independent of `T`. This follows from the already constructed
finite same-array Gaussian-program proxies; it is not an additional
premise. Here are the necessary steps.

Fix `T`. Use the sampled dense-history proxy of
`GENERAL_REFERENCE_PROJECTION.md`, Section 12, with its finite program
approximation. It has the same initialized arrays and prescribed clipped
forward histories; its learned matrices are their exact finite-rank
integrals. Let `nu -> 0` denote the deterministic population proxy mismatch
as its meshes and finite-program approximation are refined. At a fixed
proxy, all empirical finite-program errors tend to zero in probability.

For an auxiliary carrier cutoff `R`, separate from the target cutoff `M`,
the dense version of equation (63) of that report (the `P` term removed)
gives

\[
 \sup_{t\le T}d_n(\theta_n^D(t),\theta_n^R(t))
 \le C_T e^{C_T R}
       [\nu+e^{-c_2R^2}+o_{\Pr}(1)].                         \tag{13}
\]

The finite-network comparison in (13) is between actual dense GF and the
proof-only proxy. It does not refer to a population closure. Constants
are uniform as the proxy is refined at fixed `T`; the Gaussian exponent
can be fixed using the uniform population bound (6).

The one-reference backward subtraction, equations (27)--(29) of the same
report, additionally gives

\[
 \max_{\ell,a}\sup_{t\le T}
 \|\delta^D_{\ell,a}(t)-\delta^R_{\ell,a}(t)\|_{\rm RMS}
 \le C_T(1+R)e^{C_T R}
       [\nu+e^{-c_2R^2}+o_{\Pr}(1)].                         \tag{14}
\]

To check this inference, apply the subtraction with the recomputed proxy
fields as reference, use (13), and use the proxy carrier tail bound (61).
The proxy's learned-adjoint output is pointwise bounded by its clipped
history formula (59a), so no unbounded learned multiplier was omitted.
Since both paths use the same initialized matrix,

\[
 \|k^n_{\ell,a}-k^R_{\ell,a}\|_{\rm RMS}
 \le K\|\delta^D_{\ell+1,a}-\delta^R_{\ell+1,a}\|_{\rm RMS}
 \quad(\ell<L).                                             \tag{15}
\]

For each fixed `R` and proxy take width to infinity first. Next refine
the proxy. Finally let `R -> infinity`. The remaining upper bound in
(14) vanishes because
`(1+R)exp(C_T R-c_2 R^2) -> 0` for this fixed `T`. Equivalently, for a
specified error tolerance one first chooses a sufficiently large finite
`R`, then a sufficiently accurate fixed proxy, then a sufficiently large
width. This proves that the actual dense initialized carriers can be
made arbitrarily close in empirical RMS, uniformly on `[0,T]`, to the
recomputed proxy carriers. It does not assert a rate for this closeness.

For any two fields `u,v` on one finite RMS space,

\[
 \|u\mathbf1_{|u|>2M}\|_{\rm RMS}
 \le2\|u-v\|_{\rm RMS}
       +2\|v\mathbf1_{|v|>M}\|_{\rm RMS}.                   \tag{16}
\]

Indeed on `|u|>2M, |v|<=M`, one has `|u|<=2|u-v|`; on the other
part use `|u|<=|u-v|+|v|`, and then the norm triangle inequality.
Apply (16) to the actual dense and proxy carriers. The proxy empirical
tail transfers by the fixed-program convergence proved in Section 12.3,
including its uniform-time finite-net argument. One may use a continuous
quadratic-growth cutoff majorant, so no zero-atom assumption at the
threshold is needed.

At the population, the proxy carrier is uniformly `L2`-close to the true
dense carrier. Applying (16) once more bounds its tail by the right side
of (6), with a rescaled threshold, plus a vanishing proxy error. The
limiting tail constants here are fixed multiples of `A_0,c_0`; although
the approximation effort depends on `T`, these tail constants do not.
Absorb the finite threshold rescalings into `A_1,c_1`. Equations
(14)--(16) prove (12).

This derivation is a fixed-cutoff statement with a vanishing additive
error. It has not replaced that error by a Gaussian tail uniformly in
width or in a cutoff growing with width.

## 4. Transferring the activity-weighted tail through infinite time

For every fixed `M>=1` and every `eta>0`,

\[
 \Pr\{Z_n(M)>A e^{-cM^2}+\eta\}\longrightarrow0              \tag{17}
\]

for constants `A,c` independent of `M` and time. To prove it, split (9)
at a deterministic `T`. Equations (3), (11), and (12) imply

\[
 Z_n(M)\le S\sup_{t\le T}H_n(M,t)+C Y^2e^{-\lambda T}
       \quad\hbox{on }G_n.                                  \tag{18}
\]

Choose `T` so that the second term is below `eta/2`. At this fixed `T`,
apply (12) with tolerance `eta/(2S)`; `S>0` since `Y>0`. Its Gaussian
term contributes `S A_1 exp(-c_1M^2)`, independent of `T`. Off `G_n`,
`Z_n(M)=0`. This proves (17) after adjusting constants.

Thus physical time is removed before an order-dependent cutoff is
selected. The tail after `T` was bounded by RMS and loss decay alone;
no empirical Gaussian estimate at late times was used.

## 5. A simultaneous floor defined entirely by the dense path

Restrict cutoff values to positive integers and define

\[
 a_n=\sup_{j\in\mathbb N,\ j\ge1}
          \bigl(Z_n(j)-A e^{-cj^2}\bigr)_+.                   \tag{19}
\]

This is a finite nonnegative measurable random variable: the supremum is
countable, and `Z_n(j)` is uniformly bounded by (3), (11). It is zero
off `G_n`. It uses only the dense trajectory and initialization event.

**Claim:** `a_n -> 0` in probability. Fix `epsilon>0`. Choose an integer
`J` such that `A exp(-cJ^2)<epsilon/2`. For the finitely many `j<J`,
(17) and a finite union show that their excesses in (19) are at most
`epsilon` with probability tending to one. For every `j>=J`,

\[
 \bigl(Z_n(j)-A e^{-cj^2}\bigr)_+\le Z_n(j)\le Z_n(J).
\]

Equation (17) at the one fixed cutoff `J` makes this tail at most
`epsilon` with probability tending to one. This proves the claim.
In particular the floor construction requires no growing-program
concentration result.

By its definition, simultaneously for every integer `M>=1`,

\[
 Z_n(M)\le A e^{-cM^2}+a_n.
\]

Together with (10), this gives the fully pathwise intermediate bound

\[
 E_{n,q}\le C e^{\kappa_0 M}
          [q^{-1}+e^{-cM^2}+a_n]
 \quad(q,M\in\mathbb N,\ q,M\ge1),\quad\hbox{on }G_n.         \tag{20}
\]

The same random `a_n` works for all closure orders.

## 6. Optimization, explicit order envelope, and slow joint sequences

Put `delta=q^-1+a_n>0`. If `delta<1`, choose the integer

\[
 M=\max\left(1,\left\lceil
             \sqrt{c^{-1}\log(1/\delta)}\right\rceil\right).
\]

Then `exp(-cM^2)<=delta`, and the integer rounding only changes the
constant in `exp(kappa_0 M)`. If `delta>=1`, use `M=1`. Both cases
yield, for a fixed `kappa>0`,

\[
 E_{n,q}\le C\Phi(q^{-1}+a_n),\qquad
 \Phi(x)=x\exp\!\left(\kappa\sqrt{\log(e+1/x)}\right)
   \ (x>0),\qquad\Phi(0)=0.                                \tag{21}
\]

The function is continuous at zero: writing `x=exp(-u)` makes the
logarithm of `Phi(x)` equal to `-u+O(sqrt(u))`. Its factor
`Phi(x)/x` is nonincreasing in `x`. Consequently it is subadditive,
directly, without a monotonicity assumption on `Phi` itself:

\[
 \Phi(x+y)=x\frac{\Phi(x+y)}{x+y}
           +y\frac{\Phi(x+y)}{x+y}
         \le\Phi(x)+\Phi(y).                                \tag{22}
\]

Use (22) in (21) and set `b_n=C Phi(a_n)`. Continuity at zero and
(19) give `b_n -> 0` in probability, proving (1).

For each fixed `0<gamma<1`, on any fixed bounded interval of `x`,

\[
 \Phi(x)\le C_\gamma x^\gamma.                              \tag{23}
\]

Near zero this follows because
`-(1-gamma)u+kappa sqrt(log(e+exp(u)))` is bounded above; away from
zero it follows by continuity. The random `a_n` is uniformly bounded,
so (21) and `(x+y)^gamma<=x^gamma+y^gamma` give the alternative bound

\[
 E_{n,q}\le C_\gamma(q^{-\gamma}+a_n^\gamma)
       \quad\hbox{on }G_n,\quad\hbox{simultaneously in }q.    \tag{24}
\]

For each fixed integer `q_0>=1`, using the same cutoff in (20) for all
`q>=q_0` also proves the all-time width-first statement

\[
 \forall\zeta>0:\quad
 \Pr\left\{\sup_{q\ge q_0}E_{n,q}
     >\frac C{q_0}e^{\kappa\sqrt{\log(e+q_0)}}+\zeta\right\}
       \longrightarrow0.                                   \tag{25}
\]

The probability of `G_n^c` is absorbed here. For the integer-rounded
sequences `q_n=log n` and `q_n=log log n`, (24) respectively gives
`C_gamma(log n)^-gamma+C_gamma a_n^gamma` and
`C_gamma(log log n)^-gamma+C_gamma a_n^gamma` on `G_n`. Any other
diverging sequence obeys the same formula with its own `q_n`; there is
no requirement that `q_n` exceed `sqrt(n)` or any other width scale.

The forward difference recurrence on the common all-time physical ball
also gives, for every fixed bounded test-input set `K`,

\[
 \sup_{t\ge0,x\in K}|\widehat f_{n,q}(t,x)-f_n^D(t,x)|
       \le C_K E_{n,q}.                                     \tag{26}
\]

Thus the same order envelope and floor control predictions. This is
comparison with the same finite dense network, not a quantitative
finite-width law of large numbers for the population predictor.

There is also a pure rate along a sufficiently slow deterministic order
schedule. Since `a_n -> 0` in probability, choose strictly increasing
deterministic integers `N_j`, also satisfying `N_j>=j^4`, so that

\[
 \sup_{n\ge N_j}\Pr\{a_n>1/j\}\le1/j.                       \tag{27}
\]

For `n>=N_1`, put `Q_n=max{j:N_j<=n}`. Then `Q_n -> infinity`,
`Q_n<=n^(1/4)`, and `Pr{a_n>1/Q_n}<=1/Q_n`. On the intersection
of `G_n` with `a_n<=1/Q_n`, (24) gives, simultaneously for all integer
orders `1<=q<=Q_n`,

\[
 E_{n,q}\le 2C_\gamma q^{-\gamma}\quad(0<\gamma<1).           \tag{28}
\]

The probability of this event tends to one. In particular the selected
order `Q_n` has a pure `C_gamma Q_n^-gamma` tracking rate. One can make
`Q_n` no larger than any prescribed deterministic diverging cap `h_n`:
choose `N_j` additionally so that `h_n>=j` for every `n>=N_j`. This
uses only the definition of divergence of `h_n`, not its monotonicity.
The construction of `N_j` is qualitative. It certifies the existence of
a sufficiently slow schedule, and does not certify that `n^(1/4)`,
`log n`, or `log log n` themselves satisfy the pure rate without a floor.
Equations (1) and (24) apply to those explicit schedules with their floor.
The argument for (28) uses the power estimate directly, so no unproved
monotonicity of `Phi` for large `kappa` is required.

## 7. Claim boundary and internal audit

- **Proved relative to the specified study inputs:** (12), the fixed-cutoff
  dense-tail transfer; (17), its all-time activity-weighted version; the
  dense-only simultaneous floor (19); and the all-time near-one order
  envelope (1), (21), (24), (25).
- **Still open here:** an explicit power or other numerical rate in width
  for `a_n` or `b_n`; removing the floor; an exact all-time `C/q` endpoint
  for arbitrary depth and correlated data; and every exponent at least
  one for this direct accumulated-defect route.
- The all-time result uses finite total residual activity in the feedback
  exponent. It does not merely insert `T=log q` into an unquantified
  compact-time constant.
- The finite-program proof is always invoked at fixed cutoff, finite
  horizon, and fixed program before taking width large. The monotone
  tail argument creates a vanishing floor without claiming a rate for
  a growing transcript.
- No terminal closure residual ratio, uniform population closure, or
  finite-width Gaussian carrier bound has been assumed. A proof-only
  proxy supplies reference estimates; it supplies nothing to the
  implemented autonomous closure.
- This result is weaker than the still-open uniform finite-width `C/q`
  target. It strengthens the earlier qualitative all-time conclusion by
  supplying an explicit order envelope plus a separately vanishing,
  dense-only width floor.

## 8. Exact input scope

The complete scientific inputs used before freezing this derivation were
only these six files in this study. No maintained book passage, other study,
or `old_docs/` was read. Hashes recorded at the completion of reading:

| File | SHA-256 |
|---|---|
| `SMALL_LABEL_ALLTIME_SYNTHESIS.md` | `f5a01b31860174734439590cf52fed11795fab62adc5ca367418ecbe44e34f28` |
| `SMALL_LABEL_GAUSSIAN.md` | `1d7cecbf36bea7c5ced2caf1d336d9d70d12db14ffb7a61bde44b580f998becb` |
| `GENERAL_AUTONOMOUS_SYNTHESIS.md` | `8ea4888e9874250e8386f32c492781dbc111fceda17ad5afc4e77a1b6980e735` |
| `GENERAL_GAUSSIAN_TRANSPORT.md` | `004a7b6ed9ec193fd906e336a82baa7d456098925fe209e17d947ba21d7d93d5` |
| `GENERAL_REFERENCE_PROJECTION.md` | `db29db73c99b309d77f8233c4e0e1b3060ba8905588a7a893ddc9ccbf177801c` |
| `GENERAL_GEOMETRIC_STABILITY.md` | `559d375c64c6f79c5dac3a1ad9de6616ae3e7caf7cf5ecc386abce9e7057c799` |

Required process inputs read: `investigate-conjectures/SKILL.md`, its
`research-contract.md`, `evidence-ledger.md`, and `adversarial-audit.md`
references, and `solve-math-rigorously/SKILL.md`. This is an internal
analytic derivation; it has not received an independent promotion review.

After this derivation was frozen, the coordinator explicitly authorized
reading the complete `SLOW_ORDER_UNIFORM_BOUND.md` for an internal cross-check.
Its initial Sections 1--8, before addition of the confidence corollary,
agree with the argument here. In particular its fixed-cutoff transfer and
slow diagonal do not introduce a trained finite-tail or population-closure
assumption. This later reading was a synthesis check, not a scientific
input to the frozen derivation. The synthesis's additional spectral-slack
source was not read or checked in this scope.
