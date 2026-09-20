# Explicit proposal budgets for the fractional-progress Gaussian rule

2026-09-19. Frozen scoped theoretical candidate; no experiments and no
promotion. The proof below concerns exactly the held-state fractional
acceptance rule of `NOISE_GLOBAL_PROGRESS.md`, Section 5. It does not
concern the older rule accepting every strict decrease.

The result is a finite, explicit, instance-dependent high-probability
proposal budget for every positive target accuracy. The constants can
be exceptionally poor. The construction uses finitely many covariance
coordinates with certified tail bounds; it contains neither an unknown
infimum of success probabilities nor an inverse hitting-time CDF.
For an arbitrary mathematically specified covariance the formulas are
well-defined. Numerical computability additionally requires effective
access to that covariance and the stated population integrals, as made
precise in Section 8. No effective presentation of arbitrary real input
data or arbitrary operators is silently assumed.

## 1. Input scope and exact contract

Allowed and actually read scientific inputs, in full:

* `NOISE_GLOBAL_PROGRESS.md`, SHA-256
  `70fc60f0554f54041c233d0f50f697e1cfab9a0dd834c8293470540818e11288`;
* `NOISE_RECURRENCE.md`, SHA-256
  `644b6f9d306f7e8bde06c5fda5732e69bd960de88b9ee5e5ddcea5eaad1845e9`;
* `ESCAPE_AND_LIMITS.md`, SHA-256
  `544a5fde3b224cfa30539754c5d27123b900c12ed3fe5df98df00d5a8dd20ac2`.

Required process inputs: root `AGENTS.md`, Part 1 of
`RESEARCH_WORKFLOW.md`, `solve-math-rigorously`, and
`investigate-conjectures` with its research-contract, evidence-ledger,
and adversarial-audit references. No established-book file was needed.
The supervisor remains responsible for checking the dictionary premises
against its complete established sources.

Scope disclosure: after deriving the rate mechanism, the agent used
`list_agents` to check available capacity for a proof check. The tool
unexpectedly returned completed agents' full summaries, including other
studies. Those summaries were not inputs to this argument and were not
used. This attempt therefore cannot be called blind or isolated. A fresh
isolated checker should receive only this frozen candidate and its three
listed scientific dependencies.

The exact state, loss, and physical norm are

\[
\begin{split}
\mathcal H&=L^2(\lambda_1;\mathbb R^2)\oplus L^2(\lambda_2)
             \oplus\mathbb R^{d_2\times d_1},\qquad S=(w,c,M),\\
a_i&=E_1[b_1\tanh(w\cdot u_i)],\qquad
H_i=\tanh(b_2^TMa_i),\qquad f_i=E_2[cH_i],\\
L(S)&=\sum_i\mu_i(f_i-y_i)^2,\qquad u_i=x_i/\sqrt2\in S^1.
\end{split}                                                    \tag{1}
\]

The finite data have positive masses summing to one and compatible binary
labels. Merge duplicates and antipodes with the prescribed label signs;
this preserves the full loss. Let \(n\ge1\) be the number of resulting
directions, distinct modulo sign. Retain the complete canonical mark
laws, dictionary normalization, actual transpose, all trainable blocks,
and initialization \((g,0,D)\) for \(p=1,2,3\). The argument also applies
from any deterministic \(S_0\in\mathcal H\) with a known finite norm bound.

Write \(B_l=\mathop{\rm ess\,sup}|b_l|\). The exact structural inputs
used are the boundedness of the dictionaries, a nonatomic lower mark,
and fixed vectors \(l,e\) for which

\[
b_1^Tl=1,\qquad b_2^Te=X,\qquad |X|<1,
\tag{2}
\]

where the law of \(X\) has positive density on \((-1,1)\).
These hold for the three orders in the assigned source.

Let \(Z\sim\nu=N(0,\Sigma)\), where \(\Sigma\) is positive, injective,
trace class on the physical Hilbert space. Its fixed noise scale is
included in \(\Sigma\). Proposals are iid copies of this same \(Z\).
The spectral representation used throughout is

\[
\Sigma\psi_j=\lambda_j\psi_j,\quad
\lambda_j>0,\quad V=\sum_{j\ge1}\lambda_j<\infty,\quad
\Lambda=\sup_j\lambda_j>0.                                      \tag{3}
\]

The \(\psi_j\) form an orthonormal basis and the coordinates of \(Z\)
are independent \(N(0,\lambda_j)\) variables. One may order eigenvalues
decreasingly, making \(\Lambda=\lambda_1\).

Fix \(\theta\in(0,1)\). At stage \(s\), starting from loss \(\ell_s>0\),
optionally run exact physical gradient flow for a fixed duration
\(h\ge0\). Complete the stage if the resulting loss is at most
\(\theta\ell_s\). Otherwise hold the resulting state fixed and accept
the first Gaussian proposal with loss at most \(\theta\ell_s\).
Rejected proposals cause no state change and no intervening flow.

The main observable is loss at the first attainment of \(L\le\varepsilon\).
There is no width limit, time discretization, or change of optimizer in
this claim. The default \(h=0\) gives a pure proposal-count statement;
Section 6 includes every fixed finite \(h\).

## 2. A fixed finite-dimensional family of rescue centers

Choose finitely many unit directions \(v_j\) avoiding orthogonality to
all \(u_i\), with sign rows
\(\sigma_i=(\operatorname{sign}(v_j\cdot u_i))_j\) distinct modulo sign.
For example, take a direction in every open sector cut out by the
finitely many lines \(v\cdot u_i=0\). For a nonparallel pair of inputs
there are sectors with equal signs and sectors with opposite signs,
so their full sign rows cannot be equal or opposite. Choose positive
rational \(\alpha_j\) summing to one such that

\[
s_i=\sum_j\alpha_j\sigma_{ij}\ne0,\qquad s_i\ne\pm s_k\ (i\ne k).
\tag{4}
\]

Such masses can be found by enumerating rational points in the open
simplex: the forbidden equalities form finitely many proper affine
hyperplanes. Partition the nonatomic lower mark space into sets of
masses \(\alpha_j\), and let \(v(\omega)=v_j\) on the corresponding set.
Thus \(\|v\|_2=1\). Put

\[
m=\min_{i,j}|v_j\cdot u_i|>0,\qquad
H_i^*(X)=\tanh(s_iX),\qquad K_{ik}=E_2[H_i^*H_k^*].              \tag{5}
\]

The Gram matrix is positive definite. Indeed a zero linear combination
is zero throughout \((-1,1)\), by positive density and continuity, and
then on all of \(\mathbb R\) by real analyticity. Absorbing signs gives
distinct positive slopes. Its limit at positive infinity sets the sum
of coefficients to zero; subtract that constant relation and multiply
by \(e^{2aX}\), where \(a\) is the smallest remaining slope. Since
\(e^{2aX}(\tanh(aX)-1)\to-2\), while larger-slope terms tend to zero,
the coefficient of that slope vanishes. Repetition removes all terms.

Choose a certified constant
\(0<\kappa\le\lambda_{\min}(K)\), and set \(M_*=el^T\).
For an arbitrary \(\|S\|\le R\), define

\[
f_i^*(c)=E_2[cH_i^*],\qquad
k(c)=\sum_i[K^{-1}(y-f^*(c))]_i H_i^*.
\tag{6}
\]

Then \(E_2[(c+k(c))H_i^*]=y_i\). Because \(|H_i^*|\le1\) and
\(|y_i|=1\),

\[
\|k(c)\|_2^2=(y-f^*)^TK^{-1}(y-f^*)
  \le\frac{n(1+R)^2}{\kappa}.
\tag{7}
\]

Define the explicit positive constants

\[
A_R=\frac{\sqrt n(1+R)}{\sqrt\kappa},\qquad C_R=R+A_R.
\tag{8}
\]

Thus \(\|k(c)\|\le A_R\) and \(\|c+k(c)\|\le C_R\).

For a target \(a>0\), write \(\log_+ t=\max(0,\log t)\) and choose

\[
\begin{split}
T(R,a)&=\max\left\{1,\ \frac{\log_+(16C_R/\sqrt a)}{m},
            \frac{8(R+1)}m\sqrt{\frac{C_R}{\sqrt a}}\right\},\\
r(R,a)&=\min\left\{1,\ \frac{\sqrt a}{4(C_RB_1B_2+1)}\right\},\\
H(R,a)&=\left[T(R,a)^2+A_R^2+(\|M_*\|_F+R)^2\right]^{1/2}.
\end{split}                                                    \tag{9}
\]

The rescue center

\[
g_S=(T(R,a)v,\ k(c),\ M_*-M)
\tag{10}
\]

satisfies \(\|g_S\|\le H(R,a)\) and belongs to the single fixed space

\[
E=\operatorname{span}\{(v,0,0),(0,H_i^*,0):1\le i\le n\}
       \oplus\{(0,0,A): A\in\mathbb R^{d_2\times d_1}\}.
\tag{11}
\]

Its dimension is \(d=1+n+d_1d_2\). It does not depend on the incumbent,
target, or iteration. In particular, no term \(-w\) is being added.

For every \(u\in\mathcal H\) with \(\|u\|<r(R,a)\),

\[
L(S+g_S+u)<a.                                                   \tag{12}
\]

To verify (12), absorb \(u_w\) into \(\widetilde w=w+u_w\), whose norm
is at most \(R+1\). On \(\{|\widetilde w|\le Tm/2\}\), every lower
preactivation has the sign \(\sigma_{ij}\) and magnitude at least
\(Tm/2\). Since \(|\tanh t-\operatorname{sign}t|\le2e^{-2|t|}\),
while the complement has probability at most
\(4(R+1)^2/(T^2m^2)\),

\[
\left|E_1\tanh((\widetilde w+Tv)\cdot u_i)-s_i\right|
 \le 2e^{-Tm}+\frac{8(R+1)^2}{T^2m^2}
 \le\frac{\sqrt a}{4C_R}.                                      \tag{13}
\]

The identities (2) turn the \(M_*\) upper preactivation into \(X\)
times that expectation. The added matrix error changes it by at most
\(B_1B_2r\), since \(|a_i|\le B_1\). The upper tanh is 1-Lipschitz.
Pairing its error with \(c+k(c)\), and using \(|H_i|\le1\) for the
readout error, gives

\[
|f_i(S+g_S+u)-y_i|
 \le C_R\left[\frac{\sqrt a}{4C_R}+B_1B_2r\right]+r
 \le\frac{\sqrt a}{2}.
\tag{14}
\]

Weights summing to one imply loss at most \(a/4<a\).
Thus (9) provides concrete uniform centers and a concrete robust radius.

## 3. A finite covariance recipe for the uniform success probability

Take an orthonormal basis \(e_1,\ldots,e_d\) of (11). It is directly
constructible from \(v\), the matrix units, and the functions
\(\sum_i(K^{-1/2})_{ij}H_i^*\). Let \(P_N\) project onto
\(\psi_1,\ldots,\psi_N\), and define

\[
D_N^2=\sum_{l=1}^d\|(I-P_N)e_l\|^2
     =d-\sum_{j\le N}\sum_{l\le d}|\langle\psi_j,e_l\rangle|^2.
\tag{15}
\]

For the \(H=H(R,a)\) and \(r=r(R,a)\) from (9), choose any finite
\(N=N(R,a)\ge1\) such that

\[
H^2D_N^2\le r^2/16,\qquad
\sum_{j>N}\lambda_j\le r^2/128.
\tag{16}
\]

Such an \(N\) exists because \(E\) is finite dimensional,
\(P_N\to I\) strongly, and \(\Sigma\) is trace class. Under the
effective-input convention in Section 8, searching for strict versions
of (16) terminates with finitely many certified calculations.

Put \(\rho=r/(4\sqrt N)\) and define

\[
q(R,a)=\frac78\prod_{j=1}^N
 \left[\frac{2\rho}{\sqrt{2\pi\lambda_j}}
       \exp\left(-\frac{(H+\rho)^2}{2\lambda_j}\right)\right]>0.
\tag{17}
\]

Every factor is a lower bound on an actual one-dimensional interval
probability and is less than one. Therefore \(0<q(R,a)<1\).
This number depends only on the displayed data, dictionary, covariance,
radius, and target, not on the particular incumbent in that ball.

**Uniform success bound.** For every \(\|S\|\le R\),

\[
\nu\{Z:L(S+Z)<a\}\ge q(R,a).                                  \tag{18}
\]

Proof: for any \(g\in E\) with \(\|g\|\le H\), the Hilbert--Schmidt
bound on the restriction of \(I-P_N\) to \(E\) gives
\(\|(I-P_N)g\|\le HD_N\le r/4\). The Gaussian tail has second moment
\(\sum_{j>N}\lambda_j\), so Markov's inequality yields

\[
P(\|(I-P_N)Z\|<r/4)\ge7/8.                                    \tag{19}
\]

In the first \(N\) coordinates, require
\(|\langle Z-g,\psi_j\rangle|<\rho\) for every \(j\le N\).
Since \(|\langle g,\psi_j\rangle|\le H\), the minimum Gaussian
density on each required interval is at least
\((2\pi\lambda_j)^{-1/2}\exp(-(H+\rho)^2/(2\lambda_j))\).
Integration gives the corresponding factor in (17). These coordinate
events and the tail event are independent. On their intersection,

\[
\|Z-g\|\le\|P_N(Z-g)\|+\|(I-P_N)Z\|+\|(I-P_N)g\|
 <3r/4<r.
\tag{20}
\]

Consequently \(\nu(B(g,r))\ge q(R,a)\). Apply this with \(g=g_S\)
and use (12).

This derivation does not assume \(E\subset\operatorname{Ran}\Sigma^{1/2}\).
Its centers can have infinite Cameron--Martin norm. No infinite-field
translation formula is used. The finite-dimensionality of the successful
control family, rather than compactness of the state ball, is decisive.

## 4. A tail bound for the accepted proposal

For \(t\ge0\),

\[
P\{\|Z\|>\sqrt{2V+4\Lambda t}\}\le e^{-t}.
\tag{21}
\]

For a finite Gaussian projection,

\[
E\exp\left(\frac{\|P_NZ\|^2}{4\Lambda}\right)
 =\prod_{j\le N}\left(1-\frac{\lambda_j}{2\Lambda}\right)^{-1/2}
 \le \exp\left(\frac{\sum_{j\le N}\lambda_j}{2\Lambda}\right).
\tag{22}
\]

The last inequality uses \(-\log(1-x)\le2x\) for
\(0\le x\le1/2\); its derivative proof is
\((2x+\log(1-x))'=2-1/(1-x)\ge0\) on that interval. Monotone
convergence as \(N\to\infty\), followed by the exponential Markov
inequality, proves (21). Known upper bounds for \(V\) and \(\Lambda\)
can replace their exact values in (21).

Now hold a state \(T\) fixed and accept the first of iid Gaussian
proposals belonging to a measurable success set \(A\), with probability
\(p=\nu(A)>0\). Let \(W\) be the number of proposals and \(Z_*\) the
accepted proposal. Independence and a geometric sum give

\[
P(W>k)=(1-p)^k,\qquad
P(Z_*\in B)=\sum_{j\ge1}(1-p)^{j-1}\nu(A\cap B)
           =\frac{\nu(A\cap B)}p.                              \tag{23}
\]

Therefore if \(p\ge q>0\), then, for \(\alpha,\beta\in(0,1)\),

\[
\begin{split}
k&=\left\lceil\frac{\log(1/\alpha)}q\right\rceil
  \quad\Longrightarrow\quad P(W>k)\le\alpha,\\
b&=\sqrt{2V+4\Lambda\log\frac1{\beta q}}
  \quad\Longrightarrow\quad P(\|Z_*\|>b)\le\beta.
\end{split}                                                    \tag{24}
\]

The second estimate follows from (21) with Gaussian tail probability
\(\beta q\) and (23). It controls the first successful proposal, not
an arbitrary unconditional Gaussian sample. It also avoids multiplying
a Gaussian tail bound by the potentially enormous trial budget.
No independence between the two events in (24) is required.

## 5. Explicit accuracy-versus-proposal theorem, with no intervening flow

Let \(\|S_0\|\le R_0\), \(L_0=L(S_0)\), and fix
\(\delta\in(0,1)\), \(0<\varepsilon<L_0\). Define

\[
J=\left\lceil\frac{\log(L_0/\varepsilon)}{\log(1/\theta)}\right\rceil,
\qquad a=\theta\varepsilon,\qquad
\alpha=\beta=\frac{\delta}{2J}.
\tag{25}
\]

Starting from the known \(R_0\), perform the following finite deterministic
recursion for \(s=0,\ldots,J-1\):

\[
\begin{split}
q_s&=q(R_s,a) &&\text{by (9), (15)--(17)},\\
k_s&=\left\lceil\frac{\log(2J/\delta)}{q_s}\right\rceil,\\
b_s&=\sqrt{2V+4\Lambda\log\frac{2J}{\delta q_s}},\\
R_{s+1}&=R_s+b_s,\qquad
B(\varepsilon,\delta)=\sum_{s=0}^{J-1}k_s.
\end{split}                                                    \tag{26}
\]

**Theorem.** For the unchanged held-state fractional-progress rule with
\(h=0\), the proposal count \(\tau_\varepsilon\) until the incumbent
first satisfies \(L\le\varepsilon\) obeys

\[
P\{\tau_\varepsilon\le B(\varepsilon,\delta)\}\ge1-\delta.
\tag{27}
\]

All numbers in (26) are finite. If \(L_0\le\varepsilon\), take
\(B=0\); exact zero initial loss is included in that case. At canonical
binary initialization, \(L_0=1\) and one may use
\(R_0=(\|g\|_2^2+\|D\|_F^2)^{1/2}\).

Proof: restrict attention to stages whose initial loss exceeds
\(\varepsilon\); after the target is met there is nothing more to
prove. Conditional on the complete history at a reached stage \(s\)
with \(\|S_s\|\le R_s\), its acceptance threshold is
\(\theta\ell_s>\theta\varepsilon=a\). Every candidate counted by
(18) is accepted, so its success probability is at least \(q_s\).
The held state does not move while proposals are rejected. By (24),
conditionally the stage uses at most \(k_s\) proposals except with
probability \(\alpha\), and its accepted displacement is at most
\(b_s\) except with probability \(\beta\). On both good events,
\(\|S_{s+1}\|\le R_{s+1}\).

Iterated conditioning and the union bound over the at most \(J\)
reached stages bound the probability of any first bad stage by
\(J(\alpha+\beta)=\delta\). On the complement, at most \(J\)
stages and \(\sum k_s\) proposals are needed, because
\(\ell_J\le\theta^J L_0\le\varepsilon\). This proves (27).

The use of \(a=\theta\varepsilon\), rather than a stage's random
possibly tiny achieved loss, is essential. While accuracy has not yet
been reached, it gives a deterministic lower threshold for success.
One must not replace it with \(\theta^{s+1}L_0\): that quantity is an
upper bound on the next-stage threshold and could count unacceptable
proposals when an earlier stage greatly overshot its target.

## 6. Exact gradient flow for a fixed duration between stages

The source proves global well-posedness and the physical energy identity

\[
\frac{d}{dt}L(S(t))=-\|\dot S(t)\|^2.
\tag{28}
\]

Thus a duration \(h\) starting from stage loss \(\ell_s\) changes the
state by at most

\[
\|S(h)-S(0)\|
 \le\int_0^h\|\dot S(t)\|dt
 \le\sqrt{h\int_0^h\|\dot S(t)\|^2dt}
 \le\sqrt{h\ell_s}
 \le\sqrt{h\theta^sL_0}.
\tag{29}
\]

No bound on the pointwise gradient or on the whole infinite trajectory
is required. For this algorithm, replace (26) by

\[
\begin{split}
F_s&=R_s+\sqrt{h\theta^sL_0},\\
q_s&=q(F_s,\theta\varepsilon),\\
k_s&=\left\lceil\frac{\log(2J/\delta)}{q_s}\right\rceil,\qquad
b_s=\sqrt{2V+4\Lambda\log\frac{2J}{\delta q_s}},\\
R_{s+1}&=F_s+b_s,\qquad B_h(\varepsilon,\delta)=\sum_{s<J}k_s.
\end{split}                                                    \tag{30}
\]

If the flow completes a stage, it uses zero proposals and its new norm
is at most \(F_s\le R_{s+1}\). Otherwise the held postflow state has
norm at most \(F_s\), so the proof of Section 5 applies unchanged.
Consequently (27) holds with \(B_h\) for this exact algorithm too.
Flow may attain the requested accuracy before a stage is complete;
that only shortens the first hitting time.

Under the explicit clock convention that each proposal costs one unit
and each flow segment costs \(h\), the corresponding hitting time is
at most \(B_h+Jh\) with probability at least \(1-\delta\).
This is not a bound on the computational cost of evaluating exact
population integrals or numerically solving the flow.

## 7. Quantiles, expectations, and uniformity

Equation (27) is already an explicit high-probability accuracy-versus-
proposal statement. If a simultaneous sequence is desired, choose
\(\varepsilon_j\downarrow0\), \(\delta_j>0\) with
\(\sum_j\delta_j\le\delta\), and calculate each
\(B_h(\varepsilon_j,\delta_j)\) from the original deterministic state.
On an event of probability at least \(1-\delta\), every accuracy
\(\varepsilon_j\) is attained by its respective budget. Taking running
maxima of these budgets yields an increasing deterministic schedule.
This is a union bound for one unchanged trajectory, with no restarts.

The following expectation statement is justified: conditional on every
particular held state and positive stage threshold, the stage waiting
time has finite mean \(1/p\). For the deterministic first held state,
the bound (18) also gives a finite deterministic upper bound on that
mean. However, (27) by itself does not imply a finite unconditional
expected proposal count for an arbitrary later accuracy. Integrating
the resulting quantile bound need not converge, and the argument does
not control \(E[1/p]\) at later random states. That expectation question
remains open here; infinite expectation is not asserted either.

No uniform rate over all full-support covariances, all compatible input
geometries, or all initial norms is claimed. Small covariance eigenvalues,
small sign margins \(m\), an ill-conditioned Gram \(K\), and the recursion
of norm envelopes can make the finite bound enormous. The mechanism is
repeated global proposals during held stages, with all three physical
blocks still trainable; it does not establish efficient optimization,
an infinitesimal-noise limit, or convergence of ordinary GF/SGD.

## 8. Effective inputs and the precise computability qualification

Each evaluation of \(q(R,a)\) requires a finite \(N\), finitely many
positive eigenvalues, finitely many scalar products
\(\langle\psi_j,e_l\rangle\), and certified upper bounds for the two
tails in (16). A sufficient presentation is:

1. Certified approximations to the finite data, dictionary constants,
   Gram matrix, and sign margins, with the strict separations already
   specified. Positive \(\kappa\) is certified by finite matrix bounds.
2. A supplied spectral representation of \(\Sigma\), with certified
   approximations to its positive \(\lambda_j\), the above scalar
   products, and a trace-tail modulus tending to zero.
3. Finite known bounds for \(V\), \(\Lambda\), and the initial norm.

For (15), a tail certificate follows from lower bounds on the finite
sum of squared scalar products, since \(d\) is known exactly. Those
certificates tend to zero as the projection expands and approximations
are refined. Strictly stronger inequalities than (16) hold for all
sufficiently large \(N\), so interval certification terminates. Lower
bounds for (17), and upper bounds for (24)--(30), can then be computed
using ordinary finite real calculations with outward error control.
An exact known trace \(V\), together with certified partial eigenvalue
sums, is one way to obtain the trace-tail certificates.

The theorem's mathematical scope is every positive injective trace-class
covariance, whether or not effectively given. Calling its numerical
budget Turing-computable for an arbitrary unspecified or noncomputable
operator would be false. The explicit finite-covariance recipe is the
strongest effective claim supported by these inputs. This qualification
does not hide an optimization over all population states or a stochastic
hitting-time oracle.

## 9. Claim and audit record

| Claim | Status and exact scope |
|---|---|
| Finite-dimensional robust rescue family | Proved in (4)--(14), using the assigned low-order dictionary premises |
| Explicit Gaussian success bound on a physical norm ball | Proved in (15)--(20), for every full-support trace-class covariance |
| Accepted-proposal size control | Proved in (21)--(24); accounts for conditioning on success |
| Finite high-probability proposal budget | Proved in (25)--(30), for the held-state fractional-progress rule |
| A numerical algorithm producing that budget | Exact under the effective-input conditions in Section 8 |
| Finite unconditional expected count at every accuracy | Open; not implied by conditional geometric means |
| Fitting under acceptance of every strict decrease | Unchanged and unresolved by this note |

Author check: direct symbolic verification of every displayed inequality
and conditional probability calculation, by scoped agent
`noise_rate_existing`; source hashes recorded in Section 1. Checks include
large target accuracy, one merged input, arbitrarily ill-conditioned
positive Gram matrices, centers outside the Cameron--Martin space,
zero-loss stopping, a stage that overshoots its threshold, flow-only
stages, and the zero-duration flow specialization. No numerical experiment
or computational proof check was used. No independent review is claimed.

The principal hostile alternatives are addressed as follows. An arbitrary
bounded Hilbert ball need not have a uniform Gaussian translate mass;
the proof instead controls the finite-dimensional family (11). A selected
successful Gaussian need not retain the original tail probability; (23)
retains its exact conditioning factor. Stage losses can overshoot their
nominal geometric envelope; (25) uses the accuracy floor only before the
target is met. Norms need not be bounded forever; (26) is a finite-horizon
probabilistic envelope. Arbitrary covariance inputs need not be effectively
computable; Section 8 states the required presentation explicitly.

The source's previous limitation was that it supplied no proposal-count
rate. This note adds an instance-dependent high-probability rate for that
same fractional rule. It does not contradict the source's lack of a
uniform rate or unconditional expectation estimate, and changes none of
its claims about the original strict-decrease rule.
