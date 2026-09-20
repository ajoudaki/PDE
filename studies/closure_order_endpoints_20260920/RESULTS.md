# Closure order and the final fitted function

2026-09-20. Internally checked research, not promoted material. Full arguments
are in the linked route reports. All comparisons concern exact population
closures in the canonical enriched hierarchy of C.4.7.10.B/D.3, with its
actual ridge schedule, joint initialization, transpose and physical metric.
No previous study is an input.

## 1. What is established

There are three different positive conclusions, whose scopes should not be
combined into a stronger unproved claim.

1. **Every finite compatible circle dataset:** after a specified positive
   interval of full nonlinear training, freeze the hidden layers and fit the
   readout. The final predictors stabilize uniformly on the whole circle as
   order increases. There is an explicit consecutive-order error bound. A
   second, bounded-noise readout selector has the same order-stability property,
   zero limiting loss and a noise-independent selected function. These are
   modified optimizers: hidden evolution stops after the initial interval.
2. **Uninterrupted canonical GF:** for the orthogonal two-point family with
   opposite labels of amplitude at most `10^-3`, all sufficiently large orders
   fit, have strong endpoints, and converge uniformly in both physical time
   and circle input to one reference trajectory and its fitted endpoint.
   Both hidden layers and every trainable block actually move.
3. **Any reached finite-order state:** a small-loss/positive-Gram inequality
   certifies all subsequent unmodified GF, exponential loss decay, finite
   remaining state travel and a whole-circle output tail. Two such certificates
   give an explicit bound between endpoints at orders `p` and `p+1`, involving
   only their current states.

These results prove stabilization in their stated settings. They do **not**
prove a rapid rate expressed solely in the integer order `p`, or general
unit-label endpoint convergence for uninterrupted canonical GF.

## 2. Common setting and why order changes the dynamics

Let `phi=tanh`, and write the normalized physical inputs as
`x in sqrt(2) S^1`. The first preactivation is `w dot x/sqrt(2)`.
The training law is

\[
 \mu=\sum_{i=1}^m\mu_i\delta_{(x_i,y_i)},\qquad
 \mu_i>0,\quad \sum_i\mu_i=1,\quad |y_i|\le1,
\]

with unhalved loss `L=sum_i mu_i(f(x_i)-y_i)^2`.
Compatibility means equal labels on identical inputs and opposite labels on
antipodal inputs; these constraints follow from the odd architecture. Merge
such compatible duplicates into representatives. The remaining inputs are
distinct modulo sign; no linear independence, equal-weight, minimum-angle or
bound on sample count is assumed.

At order `p` the state is the canonical `(Gamma_1,Gamma_2,M_p)`, represented
on its frozen initialization carrier by `(w_p,c_p,M_p)`. It has upper feature
and prediction

\[
 H_p(t,x)=\phi\!\left(A_p(t)
            \phi(w_p(t)\cdot x/\sqrt2)\right),\qquad
 f_p(t,x)=\langle c_p(t),H_p(t,x)\rangle_{L^2(\Omega_2)}.
                                                        \tag{1}
\]

Use the joint canonical initialized carrier to compare different orders.
The correctly lifted action and its learned increment are

\[
 A_p=B_p+K_p,\quad B_p=Q_{2,p}A_0Q_{1,p},\quad
 K_p=U_{2,p}(M_p-D_p)U_{1,p}^*.
\]

Here `Q_(l,p)=U_(l,p)U_(l,p)^*` are positive contractions. The lifted
middle velocity is the full rank-force filtered on both sides:
`K_p'=Q_(2,p) F_K Q_(1,p)`. Thus increasing order changes both initialized
action and the middle-block mobility. It is not just appending zero
coefficients to one unchanged differential equation. The physical metric
still uses `||M_p'||_F`, not a substituted lifted HS norm.

## 3. Broad theorem for a specified modified optimizer

Complete proof: [SELECTION_ROUTE.md](SELECTION_ROUTE.md), including Section 9's
extension of the exact-population short-time comparison to every bounded
circle law. This extension is derived here from the complete established
C.4.7.10.A construction; it is not attributed to the narrower written
data domain of Part B's exact population hierarchy statement.

### Initialization determines a positive burn-in time

At full canonical initialization set

\[
 V_{ij}=\mathbb E_g\!\left[
   \phi(g\cdot x_i/\sqrt2)\phi(g\cdot x_j/\sqrt2)\right],
 \quad g\sim N(0,I_2),\quad Z\sim N(0,V),
\]
\[
 G^0_{ij}=\sqrt{\mu_i\mu_j}\,
                  \mathbb E[\phi(Z_i)\phi(Z_j)],\qquad
 \gamma_0=\lambda_{\min}(G^0).
                                                        \tag{2}
\]

For every reduced compatible finite dataset, `gamma_0>0`. To see the first
nontrivial step, a vanishing linear combination of the lower tanh ridge
functions vanishes everywhere by Gaussian full support. Restrict to a line
whose nonzero input projections have distinct squares. The first `m` odd
tanh Taylor coefficients are all nonzero, and give an invertible Vandermonde
system. Hence `V>0`. The upper Gaussian then has full support, and varying
one coordinate at a time proves independence of `phi(Z_i)`. Positive weights
preserve the Gram's definiteness.

Choose identically at every order

\[
 T=\min\{1/200,\sqrt{\gamma_0/56}\}>0,
 \qquad \gamma=\gamma_0/4.                              \tag{3}
\]

Run the unchanged full closure GF until `T`. The energy and velocity bounds
give full-reference upper-feature drift at most `10T^2+4T^4`. Consequently
its learned Gram at `T` is at least `gamma_0 I/2`. Exact hierarchy comparison
on this short interval proves

\[
 \delta_p=\sup_x\|H_p(T,x)-H(T,x)\|_2\longrightarrow0,
 \quad \zeta_p=\|c_p(T)-c(T)\|_2\longrightarrow0.          \tag{4}
\]

Since the weighted Gram changes by at most twice the feature difference,
there exists `p_0` such that the actual learned Gram `G_p>=gamma I` for
all `p>=p_0`. This is proved, not imposed as a trajectory assumption.
The threshold `p_0` is not made effective here. Small orders are covered
whenever their own Gram passes the same check.

For nonzero labels, the full middle action has nonzero second derivative
at initialization, and genuine middle learning occurs during every positive
burn-in interval. For each fixed dataset sufficiently large closures inherit
nonzero hidden-action motion. The general theorem does not assert a uniform
amount of hidden learning, or motion of both hidden layers for every law.

### Continue with readout GF

Freeze `w_p,M_p` at `T` and abbreviate `H_p(x)=H_p(T,x)`. Define

\[
 (E_pc)_i=\sqrt{\mu_i}\langle c,H_p(x_i)\rangle,
 \quad \bar y_i=\sqrt{\mu_i}y_i,\quad G_p=E_pE_p^*.
\]

For phase time `s=t-T`, train only the readout:

\[
 c_p'=-2E_p^*(E_pc_p-\bar y),\qquad c_p(0)=c_p(T).
                                                        \tag{5}
\]

Its exact endpoint and uniform output tail are

\[
 c_p^*=(I-E_p^*G_p^{-1}E_p)c_p(T)+E_p^*G_p^{-1}\bar y,
\]
\[
 L_p(T+s)\le L_p(T)e^{-4\gamma s},\qquad
 \|f_p(T+s)-f_p^*\|_\infty\le\gamma^{-1/2}e^{-2\gamma s}.
                                                        \tag{6}
\]

The component invisible to the training inputs is retained from the
nonlinear burn-in; silently deleting it would select a different function.
For any two orders with `G_p,G_q>=gamma I`, define current-feature defects

\[
 \delta_{p,q}=\sup_x\|H_p(x)-H_q(x)\|_2,
 \quad \zeta_{p,q}=\|c_p(T)-c_q(T)\|_2.
\]

Then the final functions obey

\[
 \boxed{\displaystyle
 \|f_p^*-f_q^*\|_\infty
 \le(1+\gamma^{-1})(\zeta_{p,q}+2T\delta_{p,q})
       +2(\gamma^{-1}+\gamma^{-2})\delta_{p,q}.}
                                                        \tag{7}
\]

In particular `q=p+1` gives the requested adjacent-closure bound. Its right
side uses the actual states at the common finite time, coupled by their
canonical joint initialization, not an unknown final target.

Proof mechanism: `||G_p-G_q||<=2delta_(p,q)`; cross-kernel vectors differ
by at most `2delta_(p,q)`; and the inverse identity bounds
`||G_p^-1-G_q^-1||<=2delta_(p,q)/gamma^2`. Subtracting the explicit
readout endpoints proves (7). By (4) these endpoints converge uniformly
on the whole circle to the same modified optimizer applied to the full
canonical short-time population solution. The uniform tail (6) also proves
convergence along every joint sequence `p -> infinity, s -> infinity`.
Deterministic iterated limits commute; fixed-time order convergence follows
from continuity of the finite Gram matrix exponential.

### A noise-independent minimum-norm selector

There is a separate readout-phase rule with a simpler endpoint comparison.
Put `P_p=E_p^*G_p^-1 E_p`, `N_p=I-P_p` and choose any strongly measurable
bounded random field `U_s` with `||U_s||_2<=1`. For `0<=eta<=gamma`, use

\[
 c_p'=-2E_p^*(E_pc_p-\bar y)-\gamma N_pc_p
          +\eta\sqrt{L_p}\,N_pU_s.                    \tag{8}
\]

The hidden fields remain frozen. This is a pathwise bounded random force,
not Brownian white noise or minibatch full-network GF. Noise is actually
injected only when its projected force and the loss are nonzero. Existing
bounded dictionary marks can supply `U_s`; no future function is supplied.

Because `E_pN_p=0`, the residual solves `r'=-2G_pr` independently of the
noise, while the invisible readout component is damped. The potential

\[
 \mathcal V_p=L_p+\|N_pc_p\|_2^2
 \quad\text{satisfies}\quad
 \mathcal V_p'\le-\gamma\mathcal V_p.                   \tag{9}
\]

The final readout is the unique minimum-norm interpolant
`c_p^dagger=E_p^*G_p^-1 bar y`, independent of the forcing path.
Consequently

\[
 \boxed{\displaystyle
 \|f_p^\dagger-f_q^\dagger\|_\infty
 \le2(\gamma^{-1}+\gamma^{-2})\delta_{p,q}.}             \tag{10}
\]

Relative to the full short-time reference and its same selector, one gets
the explicit joint bound

\[
 \|f_p(T+s)-f^\dagger\|_\infty
 \le \sqrt{\max(\gamma^{-1},1)(1+4T^2)}\,e^{-\gamma s/2}
       +2(\gamma^{-1}+\gamma^{-2})\delta_p.              \tag{11}
\]

Thus order error and physical training-time error are separated. Every
joint sequence with both parameters tending to infinity converges to the
same whole-circle function, even with different allowed noise paths at
different orders. Unrelated forcing paths need not have a fixed-positive-time
inner order limit; no such statement is needed or claimed.

## 4. Uninterrupted canonical gradient flow

### An unconditional nonlinear family

Complete proof and internal check:
[ENDPOINT_ROUTE.md](ENDPOINT_ROUTE.md),
[ENDPOINT_REVIEW.md](ENDPOINT_REVIEW.md).
For

\[
 \mu_\alpha=\tfrac12\delta_{(\sqrt2e_1,\alpha)}
           +\tfrac12\delta_{(\sqrt2e_2,-\alpha)},
 \qquad 0<\alpha\le10^{-3},                            \tag{12}
\]

there is an order threshold `p_0` independent of `alpha` such that every
`p>=p_0` follows the unchanged canonical GF for all physical time, fits
exactly at its strong endpoint, and satisfies

\[
 \sqrt{L_p(t)}\le\alpha e^{-t/40},\quad
 \int_t^\infty\|\dot\theta_p\|_{\mathrm{physical}}\,ds
      \le\sqrt{80}\,\alpha e^{-t/40},
\]
\[
 \|f_p(t)-f_p^\infty\|_\infty\le18\alpha e^{-t/40}.
                                                        \tag{13}
\]

The full reference tail is at most `7alpha exp(-t/5)`, and the exact
closure trajectories converge to it on every finite horizon. Therefore

\[
 \boxed{\displaystyle
 \sup_{t\ge0}\sup_{x\in\sqrt2 S^1}
       |f_p(t,x)-f(t,x)|\longrightarrow0,
 \qquad \|f_p^\infty-f^\infty\|_\infty\longrightarrow0.}
                                                        \tag{14}
\]

The proof is not a fixed-feature replacement. An initial upper training Gram
gap and the small target amplitude trap the original physical flow in a
fixed ball. Energy then gives a uniform finite-travel tail. The canonical
reference feature orbit gives Gaussian reverse-query tails on all physical
times, closing the actual hierarchy comparison. Both hidden activations,
the lower rows, middle action and readout move for every fixed nonzero
amplitude and sufficiently large order. The activity threshold may depend
on `alpha`; activity is not bounded away from zero as `alpha -> 0`.

This is a real but restricted small-amplitude result. It does not cover
unit binary labels or a general input geometry under uninterrupted GF.

### A current-state certificate for arbitrary finite data

Complete proof: [LEAD_COMPARISON.md](LEAD_COMPARISON.md), Sections 2–3.
At any reached fixed-order state at time `T`, let

\[
 \kappa=\lambda_{\min}\!\left[
   \sqrt{\mu_i\mu_j}\langle H(T,x_i),H(T,x_j)\rangle
                                    \right]>0,
 \quad A_*=\|A(T)\|,\quad C_*=\|c(T)\|_2,
\]
\[
 r=\min\{1,\kappa/[4(A_*+2)]\},\qquad
 B=\sqrt{1+(C_*+1)^2[1+(A_*+1)^2]}.
\]

If the entirely current-state inequality

\[
                  \sqrt{2L(T)/\kappa}<r                 \tag{15}
\]

holds, the unchanged GF fits, has a strong endpoint, and

\[
 L(T+s)\le L(T)e^{-2\kappa s},\qquad
 \|f(T+s)-f^\infty\|_\infty
      \le B\sqrt{2L(T+s)/\kappa}.                       \tag{16}
\]

The proof controls evolution of the feature Gram: it bounds its drift
inside the physical state ball, proves its gap cannot
close before exit, and uses energy/path length to exclude that exit. It
does not assume a future spectral gap.

If orders `p,q` pass (15) at the same time, then

\[
 \boxed{\displaystyle
 \|f_p^\infty-f_q^\infty\|_\infty
 \le\|f_p(T)-f_q(T)\|_\infty
      +B_p\sqrt{2L_p(T)/\kappa_p}
      +B_q\sqrt{2L_q(T)/\kappa_q}.}                    \tag{17}
\]

This applies to `q=p+1`, including low orders if their actual states pass.
It is an a posteriori theorem; eventual passage is not proved for every
canonical trajectory. Uniform certificates and all-finite-horizon order
convergence suffice to pass to endpoints, as (12)–(14) demonstrate in an
unconditional family.

## 5. What the hierarchy itself controls, and the missing order rate

Complete arguments: [LEAD_COMPARISON.md](LEAD_COMPARISON.md), Sections 1,4,
and [OPERATOR_ROUTE.md](OPERATOR_ROUTE.md).
Let `S_p` synthesize a raw initialized dictionary and
`eta_p=1/[1024(p+1)^2]`. For a fixed field `v` in the initialized
observable space `H_l^obs`, where the raw spans have dense union, define

\[
 \mathcal E_p(v)=\inf_a\{
        \|v-S_pa\|_2^2+\eta_p|a|^2\}
       =\langle v,(I-Q_p)v\rangle.                     \tag{18}
\]

Actual raw-list nesting and the decreasing ridge imply

\[
 \mathcal E_{p+1}(v)\le\mathcal E_p(v)\downarrow0,
 \quad 0\le Q_p\le Q_{p+1}\le I,
 \quad\sum_p\|(Q_{p+1}-Q_p)v\|_2^2\le\|v\|_2^2.       \tag{19}
\]

This concerns a fixed field; it does not say the learned predictors improve
monotonically with order. The sharpened quantitative bound is

\[
 \|(I-Q_p)v\|_2\le\inf_a\left\{
      \|v-S_pa\|_2+\frac{|a|}{64(p+1)}\right\}.          \tag{20}
\]

For example, with `||A_0||<=2`,

\[
 \|(B_p-A_0)v\|_2
 \le2\sqrt{\mathcal E_{1,p}(v)}
                  +\sqrt{\mathcal E_{2,p}(A_0v)}.       \tag{21}
\]

Together with the adjoint analogue these control the omitted forward and
backward sources. Approximation is needed for the actual trained lower
forward fields, upper backward fields, their initialized actions and the
learned rank force. Compactness and dictionary density prove these sources
vanish on a fixed horizon, but do not bound their speed in `p`.

This identifies the missing quantitative estimate. A bound on approximation
error together with raw coefficient cost in (20), uniform on those reachable
field families, would give a rate for (4). Formula (11) would then pass it
directly to the selected fitted function. For unchanged GF, a uniform-tail
certificate would also be needed: if finite-time error is bounded by
`A delta_p exp(b(t-T))` and endpoint tails by `C exp(-kappa(t-T))`, balancing
time gives endpoint order error `O(delta_p^(kappa/(b+kappa)))`.

There is a rigorous reason not to invent a rate from density: in any nested
finite-dimensional dense hierarchy, for any proposed decreasing rate there
is a Hilbert-space field whose approximation error is not bounded by a
constant times that rate. The construction in LEAD_COMPARISON Section 4
proves this. It is **not** a slowly approximated canonical-trajectory example;
the reachable fields may possess extra structure. Rapid convergence for
those fields remains open, not disproved.

## 6. Why merely fitting does not answer the question

[FITTING_ALONE.md](FITTING_ALONE.md) constructs, in the actual canonical
closure spaces and for every fixed finite compatible training set, a
uniformly bounded family of exactly fitted stationary states with both hidden
blocks at initialization. At one extra input their predictions alternate
between `+1` and `-1` with order. Hence consecutive whole-circle errors
are at least two despite zero training loss at every order.

These are not proved reachable from canonical zero-readout initialization.
They refute the implication from fitting and bounded displacement alone;
they do not refute the desired canonical-GF conclusion. The positive results
above add the missing dynamical selection and output-tail control.

## 7. Claim status and next decisive estimate

All stated proved results have complete within-study arguments. Separate
informed internal checks covered the original-GF endpoint theorem, the
selection theorem and all-law short-time extension, the fitting obstruction,
and the lead's filter/certificate proofs. The reports record their scopes,
hashes and the two minor corrections. They are not isolated promotion reviews.
No numerical experiment or new maintained-code claim supports these results.

The most useful next research problem is a quantitative approximation theorem
for the particular forward/backward fields produced by canonical training in
the enriched polynomial-and-word dictionary. This is more specific than
proving density again. For general uninterrupted GF, one additionally needs
an all-time output-tail mechanism or a proof that the current-state certificate
is eventually reached uniformly in sufficiently large order. Neither missing
step is concealed by the modified-optimizer theorem.
