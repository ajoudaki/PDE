# Pause / resume state

Status: **NONTERMINAL CHECKPOINT — user-paused on 21 August 2026**.

All isolated agents finished cleanly before the pause.  There are no live
construction, audit, or numerical jobs.  The research goal remains open; no
positive closure theorem and no universal impossibility theorem has been
claimed.

When the user says **resume**, continue from the two boxed obligations in
Sections 5 and 6 below.  Do not rederive the finite-width model or rerun the
capped numerical panel.

## 1. Frozen canonical model and convention

The finite matrix action is ordinary multiplication with
`G=W/sqrt(n)`, while vector inner products are normalized:

\[
\langle x,y\rangle_n=n^{-1}x^Ty,
\qquad
(p\otimes q)x=p\langle q,x\rangle_n.
\]

Thus `(p tensor q)_{ij}=p_iq_j/n`.  One late referee instead defined the
matrix action itself with an additional `1/n`; that convention is not the
frozen model and its scaling warning must not be imported here.  The same
referee's objection to the lower bound on `h=<H^2>` is also resolved in the
iid model by the exact identity in Section 4.

## 2. Proved finite-width theorem

Let

\[
X=u^2,\quad \alpha^2=\langle X^2\rangle+\epsilon,
\quad H=X/\alpha,
\]

\[
Z=GH,\quad \beta^2=\langle Z^4\rangle+\epsilon,
\quad Y=Z^2/\beta,
\]

\[
f=\langle A,Y\rangle,quad C=A-fY,quad
R={2\over\beta}ZC,quad g=G^TR,quad
T=g-H\langle H,g\rangle.
\]

Feature ascent is exactly

\[
A'=Y,qquad G'=R\otimes H,qquad
u'={2\over\alpha}uT.                              \tag{2.1}
\]

The exact tangent kernel is

\[
K=\langle Y^2\rangle
+\langle H^2\rangle\langle R^2\rangle
+{4\over\alpha}\langle HT^2\rangle,             \tag{2.2}
\]

and `f'=K`.  Physical full-MSE flow is

\[
\dot\theta=2\eta(y_*-f)\theta',
\qquad
\dot e=-2\eta eK,
\qquad e=y_*-f.                                    \tag{2.3}
\]

The denominators are at least `sqrt(epsilon)`, the residual keeps its sign,
and the finite-dimensional flow is global.  The complete derivation and
balance laws are in `FINITE_WIDTH_THEOREM.md`.

## 3. Proved nontriviality

Every trained layer has nonzero gradient almost surely at finite width.  Put

\[
a=3+\epsilon,quad s=3/a,quad
b^2=3s^2+\epsilon,quad D=a^2b^2.
\]

At iid initialization,

\[
K_A\to{27\over D},\qquad
K_G\to{36\over D},\qquad
K_u\to{48\over D},\qquad
K\to{111\over D}.                                \tag{3.1}
\]

Both hidden normalized features have nonzero order-one initial velocity; in
particular

\[
\|H'(0)\|_n^2\to {64s^2\over ab^2}>0,
\qquad
\|Y_G'(0)\|_n^2\to {48s^4\over b^4}>0.           \tag{3.2}
\]

Therefore RMS normalization does not make the model linear, lazy,
readout-only, or frozen-feature.

## 4. Proved compact-horizon action and tangent identities

For every fixed feature horizon `S`, with probability tending to one,

\[
\inf_{s\le S}h(s)\ge {1\over1+16\epsilon},
\qquad h=\langle H^2\rangle.                     \tag{4.1}
\]

The short proof is important.  If `m=<u^2>`, then

\[
m'={8\epsilon^2f\over\alpha^2\beta^2}.          \tag{4.2}
\]

On the iid event `m(0)>=1/2` and `f(0)>=-n^-1/4`, monotonicity `f'>=0`
gives `m(s)>=1/2-8Sn^-1/4>=1/4`.  Jensen gives
`<u^4>>=1/16`, proving (4.1).  This is not circular.

Consequently, on every fixed interval,

\[
\int\langle R^2\rangle,qquad
\int\langle (u')^2\rangle,qquad
\sup_s\|G(s)\|_{op},qquad
\int\langle T^2\rangle                         \tag{4.3}
\]

are bounded in probability uniformly in width.

There is also an exact endpoint tangent-action identity.  With

\[
\mathcal K_Z=hI+GS_HG^T,qquad
S_H={4\over\alpha}(I-H\otimes H)M_H(I-H\otimes H),
\]

and `P=<R,GS_HG^TR>>=0`,

\[
\begin{aligned}
4\int_0^T h\beta^{-1}\langle YC^2\rangle ds+
\int_0^TP\,ds
={}&\langle A_0,Y(T)-Y(0)\rangle\\
&+\int_0^T
\{\langle Y(s),Y(T)\rangle-\|Y(s)\|^2\}\,ds.   \tag{4.4}
\end{aligned}
\]

Hence the left side is at most
`sqrt(2)||A_0||+T/4`.  This proves total action control and rules out
arbitrary prescribed support rotations as true trajectories.  It still does
not give uniform integrability of the spatial or temporal kinetic densities.

## 5. Exact unresolved convergence gate

The two dangerous weighted densities are exactly kinetic energies:

\[
\boxed{
\beta^{-2}Z_i^2C_i^2={1\over4}R_i^2,
\qquad
\alpha^{-1}H_iT_i^2={1\over4}(u_i')^2.}          \tag{5.1}
\]

A proved conditional theorem says that the full weighted-tail condition
needed for output equicontinuity follows if there is an increasing convex
`Phi`, `Phi(r)/r->infinity`, such that

\[
\boxed{
\sup_n\mathbb E\int_0^S
\langle\Phi(R^2)+\Phi((u')^2)\rangle_n ds<\infty
\quad\text{for every fixed }S.}                 \tag{DV}
\]

The proof uses (5.1), state-set measure tightness from Section 4, and the
de-la-Vallée-Poussin criterion.  It was independently audited after restoring
the canonical matrix convention.

`(DV)` itself remains open.  Exchangeability, fixed-coordinate propagation
of chaos, and total action do not imply it: a uniformly random coordinate
can carry order-one empirical kinetic energy while disappearing from every
fixed marginal.  Exact admissible phase-space states realize this defect.

The sharp probabilistic subproblem is a stopped adaptive leave-one-pack
estimate for

\[
1_J(I-H_t\otimes H_t)G_0^TR_t                 \tag{5.2}
\]

at entropy cost `|J| log(en/|J|`, plus a signed temporal-coercivity estimate
for

\[
\int_0^t
\{H_j(s)-H_j(t)\langle H_s,H_t\rangle\}
\langle R_s,R_t\rangle\,ds.                    \tag{5.3}
\]

Initialization pack bounds are proved.  Fixed-mass simultaneous row/column
packs are excluded on `o(n^-1/2)` iid feature-time horizons, and nonzero
output action is excluded on the smaller `o(n^-3/4)` scale by a crude
deterministic bootstrap.  These partial exponents are not the compact-time
theorem; the interval up to `o(1)` remains open.  For target one and fixed
positive `epsilon`, the physical clock has `ds/dt=2eta(1-f)` and does not
invalidate these one-sided exclusions.

## 6. Exact unresolved operator-source gate

The best finite-width Markov rewrite uses the fixed source `Gamma=G(0)` and
three current fields `(A,H,Q)`, `Q=G-Gamma`:

\[
Z=(\Gamma+Q)H,quad Y=N_\epsilon(Z^2),quad
R={2\over\beta}Z(A-fY),                         \tag{6.1}
\]

\[
A'=Y,qquad Q'=R\otimes H,qquad
H'=S_H(\Gamma+Q)^TR.                            \tag{6.2}
\]

It is exact, autonomous, and restartable at every finite width.  Six natural
limit realizations have been independently ruled out in their stated scope:

1. source-independent strong-Hilbert embeddings are not norm-tight;
2. an `L2` graphon is Hilbert--Schmidt and cannot retain the Ginibre singular
   law; white noise is distribution-valued and cannot be raw-squared;
3. a single Banach pointwise algebra with continuous `L1` inclusion embeds
   in `L-infinity`, excluding Gaussian marks;
4. the current coordinate law loses matrix-reuse orientation;
5. fixed `L^p`, `p!=2`, has width-growing worst-case Ginibre operator norm,
   while `L2` multiplication is unbounded;
6. finite Fock/Malliavin/traffic grade truncations fail because the
   Marchenko--Pastur Krylov family has new directions at every depth.

These do **not** prove universal impossibility.  The closest surviving class
is an infinite-depth rooted-traffic or noncommutative Gaussian source coupled
to a graded Fréchet/Wiener/Hida field algebra with closable actions.  Its
fixed-depth algebra is formal and correct, but positive-time well-posedness,
continuous kernel readout, finite-width identification, and the prohibition
against disguised hierarchy storage remain unresolved.

The second boxed obligation is therefore:

\[
\boxed{
\text{construct and audit that graded source without storing the full
hierarchy, or prove a recoding-invariant exhaustion theorem.}}              \tag{SRC}
\]

## 7. Numerical route-selection panel

The preregistered panel hit its ten-minute cap after ten of sixteen matched
cases and was stopped.  The completed maximum-kernel medians showed no
width-growing peak, but hitting-time ratios were mixed.  The frozen verdict
is **inconclusive**.  Do not rerun or reinterpret it as proof.  The emitted
summaries are in `EARLY_SPIKE_PARTIAL_RESULTS.md`.

## 8. Resume order

On resume:

1. Start with `(DV)`, using a genuinely dynamic leave-one-pack/cavity or
   temporal-coercivity argument; do not retry low-energy or state-only
   entropy bounds.
2. In parallel, formulate the surviving graded source without an ultraproduct
   and prove a fixed-cutoff continuous-time theorem.  Fixed-order Wick or
   Euler identities alone are insufficient.
3. Only attempt cutoff removal after `(DV)` or an equivalent kinetic
   no-condensation estimate is available.
4. If pursuing a negative theorem, first freeze a recoding-invariant regular
   Markov class (for example via a past-to-future Hankel-rank condition).
   Field count and “not disguised” prose do not define an exhaustive class.
5. Independently referee every candidate terminal proof before changing the
   goal status.

## 9. Files to read on resume

- `PROTOCOL.md` — frozen model and terminal contract.
- `FINITE_WIDTH_THEOREM.md` — exact dynamics, kernel, balances, initialization.
- `HOSTILE_AUDIT.md` — spikes, alignment, and nontriviality audit.
- `KINETIC_COMPACTNESS_GATE.md` — action and conditional `(DV)` theorem.
- `REACHABLE_TAIL_AUDIT.md` — stopped pack estimates and open probability gap.
- `OPERATOR_SOURCE_AUDIT.md` — source candidates and scoped no-go results.
- `CONTRACT_AUDIT.md` — why a universal finite-field no-go is not presently
  well-posed.
- `EVIDENCE_LEDGER.md` and `APPROACH_REGISTRY.md` — claim and route status.
- `EARLY_SPIKE_PARTIAL_RESULTS.md` — capped numerical record.

