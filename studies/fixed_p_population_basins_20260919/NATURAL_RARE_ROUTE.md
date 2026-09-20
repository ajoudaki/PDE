# Full population flow with rare accepted refreshes

2026-09-19. Scoped independent theoretical route, frozen before comparison.
No experiments; no promotion. The modification below becomes rare as its
parameter tends to zero. It does not become small in jump amplitude.

The strongest conclusion proved here is this: for every event frequency
\(\varepsilon>0\), a process running the exact original full population
gradient flow between accepted proposals has nonincreasing loss, an explicit
exponential loss bound in physical flow time, and an almost-sure zero-loss
parameter endpoint. On every fixed time interval it agrees exactly with the
original deterministic flow with probability at least
\(e^{-\varepsilon T}\). Its quantitative guarantee comes from a separate,
finite-dimensional readout search whose candidates can replace all incumbent
blocks. Thus this is a rigorous rare-rescue approximation to original GF,
not a theorem for small local kicks, Brownian perturbations, or original GF.

## 1. Scope, exact system, and information contract

Scientific inputs read completely within the assigned scope:

* `RATE_RESTART_ROUTE.md`, SHA-256
  `6a2c8b8d4e962962685e98175a7332d292c7e7676ffc19b622093a0f3c15b923`;
* `NOISE_GLOBAL_PROGRESS.md`, SHA-256
  `70fc60f0554f54041c233d0f50f697e1cfab9a0dd834c8293470540818e11288`;
* `ESCAPE_AND_LIMITS.md`, SHA-256
  `544a5fde3b224cfa30539754c5d27123b900c12ed3fe5df98df00d5a8dd20ac2`;
* `RATE_EXISTING_RULE.md`, SHA-256
  `1632f66b461f492468aa91d07b564694e1f146ca35187e37bd6862ef3e0c1c50`;
* established `docs/global_nonlinear.md`, assigned complete B/C.1 span
  13161--13786 and D.3 span 15146--15528. The dictionary, full joint marks,
  normalization, physical metric, equations, and all-finite-time existence
  at each fixed order were checked in these spans.

Required process inputs: root `AGENTS.md`, Part 1 of
`RESEARCH_WORKFLOW.md`, the rigorous-math skill, and the
conjecture-investigation skill with its research-contract and
adversarial-audit references. No other study, concurrent route, or review
was read. An attempted prompt-only delegation for an elementary endpoint
check was refused by the agent-capacity limit; it supplied no input.

Fix \(p\in\{1,2,3\}\). On the unchanged canonical mark carriers use

\[
\mathcal H=L^2(\lambda_1;\mathbb R^2)\oplus L^2(\lambda_2)
 \oplus\mathbb R^{d_2\times d_1},\qquad S=(w,c,M),
\]

with the physical population/Frobenius norm. For finite compatible binary
data \((u_i,y_i,\mu_i)\), \(u_i\in S^1\), \(\mu_i>0\), and
\(\sum_i\mu_i=1\), write

\[
\begin{split}
a_i&=E_1[b_1\tanh(w\cdot u_i)],& z_i&=b_2^TMa_i,& H_i&=\tanh z_i,\\
f_i&=E_2[cH_i],&r_i&=f_i-y_i,&
d_i&=E_2[b_2c(1-H_i^2)],\\
q_i&=b_1^TM^Td_i,&L(S)&=\sum_i\mu_i r_i^2.
\end{split}                                                     \tag{1}
\]

The original physical-time vector field is

\[
F(S)=-2\left(
 \sum_i\mu_i r_i(1-\tanh^2(w\cdot u_i))q_i u_i,
 \sum_i\mu_i r_iH_i,
 \sum_i\mu_i r_i d_i a_i^T\right)=-\nabla_{\mathcal H}L(S).
                                                               \tag{2}
\]

The actual transpose, bounded normalized dictionaries, full initialized
joint laws, and initialization \(S_0=(g,0,D)\) are unchanged. In particular
\(L(S_0)=1\). The field is locally Lipschitz on \(\mathcal H\), and its
flow \(\Phi_t\) exists for every finite \(t\ge0\), from every state in
\(\mathcal H\). The complete proof in `ESCAPE_AND_LIMITS.md`, Section 1,
uses bounded dictionaries and bounded derivatives of tanh; successive
bounds on the readout, matrix, and row speeds exclude finite-time escape.
Along each segment,

\[
\frac{d}{dt}L(\Phi_tS)=-\|F(\Phi_tS)\|_{\mathcal H}^2.           \tag{3}
\]

The approximation parameter \(\varepsilon\) is an event frequency per
unit of this physical time. Accuracy is denoted \(a\), to distinguish it
from the modification parameter. All population expectations and loss
tests are exact. Events are instantaneous mathematical interventions;
physical flow time is not a claim about numerical integration or processor
time. Geometry preprocessing is performed once and is not charged to this
clock. There is no width, particle, dictionary-order, or time-step limit.

## 2. A label-independent proposal family

Merge repeated and antipodal inputs, reversing label signs where necessary
and adding masses. Oddness of (1) preserves the exact loss. Let \(n\ge1\)
be the resulting number of representatives, pairwise distinct modulo sign.
The assigned dictionaries contain vectors \(l,e\) satisfying

\[
b_1^Tl=1,\qquad b_2^Te=X=\tanh\xi_1,                           \tag{4}
\]

and \(X\) has positive density on \((-1,1)\). Lower marks are nonatomic
through \(g_1\). These facts were verified in the assigned book spans.

For every pair of distinct input lines choose one unit direction with equal
input signs and one with opposite signs, avoiding all input orthogonality
directions. Their allowed sets are nonempty open arcs. This gives directions
\(v_1,\ldots,v_J\) with sign rows distinct modulo sign; if \(n=1\), use
one nonorthogonal direction. Set

\[
\alpha_j=\frac{3^{j-1}}{(3^J-1)/2},\quad
s_i=\sum_j\alpha_j\operatorname{sign}(v_j\cdot u_i),\quad
m=\min_{i,j}|v_j\cdot u_i|>0,
\]
\[
\eta=\min\bigl(\{|s_i|\}_i\cup
 \{|s_i-s_k|,|s_i+s_k|\}_{i<k}\bigr)>0.                         \tag{5}
\]

The largest nonzero power of three exceeds the sum of all preceding
powers, proving the last strict inequality, also for differences or sums
of two sign rows after division by two. Partition lower marks into cells
\(A_j\) of masses \(\alpha_j\), using Gaussian quantiles of \(g_1\).
Put \(v=v_j\) on \(A_j\), and define

\[
T_* =\frac{\log(8/\eta)}{2m},\quad
w_*=T_*v,\quad M_*=el^T,\quad
t_i=\sum_j\alpha_j\tanh(T_*v_j\cdot u_i),\quad
H_i^*=\tanh(t_iX),\quad K_{ij}=E_2[H_i^*H_j^*].                \tag{6}
\]

The tanh tail bound gives \(|t_i-s_i|\le\eta/4\). Therefore the
\(t_i\) are nonzero and distinct modulo sign. Their feature functions are
linearly independent: a dependence is an analytic identity on the real
line, by positive density on \((-1,1)\). After absorbing slope signs,
order the distinct positive slopes. The limit at positive infinity sets
the coefficient sum to zero. Subtract that constant relation and multiply
by \(e^{2t x}\) for the smallest slope \(t\); the corresponding term
tends to minus twice its coefficient and all other terms vanish.
Induction proves independence. Hence \(K\) is positive definite.

Let \(W=\operatorname{diag}(\mu_i)\) and define

\[
\begin{gathered}
S(b)=(w_*,\sum_j b_jH_j^*,M_*),\qquad
V(b)=L(S(b))=(Kb-y)^TW(Kb-y),\\
Q=KWK,\quad \kappa=\lambda_{\min}(Q)>0,\quad
\Lambda=\lambda_{\max}(Q),\quad
\chi=\lambda_{\min}(K^{1/2}WK^{1/2})>0.                         \tag{7}
\end{gathered}
\]

All anchors, features, and spectral constants use inputs, masses, and mark
laws, without labels. The finite exact state

\[
b_*=K^{-1}y,\quad c_*=\sum_j(b_*)_jH_j^*,\quad S_*=S(b_*),
\qquad L(S_*)=0                                                \tag{8}
\]

is a proof witness, never given to or computed by either algorithm below.
The algorithms see labels through actual loss values only. If
\(\lambda=\lambda_{\min}(K)\) and \(C=\sqrt{n/\lambda}\), then
\(\|c_*\|_2\le C\). For every \(b\),

\[
\|S(b)-S_*\|_{\mathcal H}^2
=(b-b_*)^TK(b-b_*)\le V(b)/\chi.                               \tag{9}
\]

Indeed, apply the smallest-eigenvalue inequality for
\(K^{1/2}WK^{1/2}\) to \(K^{1/2}(b-b_*)\). Thus bounded loss
controls distance to the single zero-loss state within this candidate
family, although it does not do so on the full population space.

## 3. Independent rare refreshes: polynomial physical-time rate

This first construction has no auxiliary optimizer. It is a Markov process
on the original population state. Independently of the flow, run a rate
\(\varepsilon\) Poisson clock. At each event draw an independent absolute
candidate \(Z\), and replace the incumbent by \(Z\) exactly when
\(L(Z)<L(S^-)\). Between every pair of events, including rejected events,
continue (2) at its original physical speed. Zero loss is absorbing.

One permitted candidate law fixes \(w_*,M_*\), uses an orthonormal basis
of \(\operatorname{span}\{H_i^*\}_{i=1}^n\), and draws its readout
coefficients from \(N(0,s^2I_n)\), with \(s=(C+1)/\sqrt n\).
For \(0<a\le1\),

\[
P\{L(Z)\le a\}\ge q_n a^{n/2},\qquad
q_n=\frac{(n/(2e))^{n/2}}{\Gamma(n/2+1)}(C+1)^{-n}>0.           \tag{10}
\]

To verify the bound, the physical coefficient vector of \(c_*\) has
norm at most \(C\), and the ball of radius \(\sqrt a\) about it has
loss at most \(a\), by \(|H_i^*|\le1\) and \(\sum_i\mu_i=1\).
On that ball Gaussian density is at least
\((2\pi s^2)^{-n/2}e^{-(C+1)^2/(2s^2)}\). Multiply by the
ball volume \(\pi^{n/2}a^{n/2}/\Gamma(n/2+1)\) to obtain (10).

Let \(\tau_a=\inf\{t:L(S(t))\le a\}\). A candidate with loss at most
\(a\) is accepted whenever the incumbent is above \(a\). Thus, conditional
on \(N_t=k\) Poisson events, failing to hit \(a\) requires all \(k\)
independent candidates to fail that test. The Poisson generating function
\(E z^{N_t}=e^{\varepsilon t(z-1)}\), obtained by summing its probability
mass function, gives

\[
\begin{split}
P\{\tau_a>t\}&=P\{L(S(t))>a\}
 \le e^{-\varepsilon q_n t a^{n/2}},\\
E\tau_a&\le\frac{1}{\varepsilon q_n a^{n/2}},\\
E L(S(t))&\le\min\left\{1,
 \Gamma(1+2/n)(\varepsilon q_n t)^{-2/n}\right\},\quad t>0.
\end{split}                                                     \tag{11}
\]

The mean hitting bound integrates the survival probability. The expected
loss bound integrates \(P\{L>a\}\) over \(0<a<1\), then extends the
integral to infinity and substitutes
\(z=\varepsilon q_n t a^{n/2}\). In particular,

\[
t\ge\frac{\log(1/\delta)}{\varepsilon q_n a^{n/2}}
\quad\Longrightarrow\quad P\{L(S(t))\le a\}\ge1-\delta.         \tag{12}
\]

The loss tends to zero almost surely: it is nonincreasing, and (11)
forces its limiting value below each positive rational threshold.
Every rejected event counts in (11)--(12), and all time spent following
the full flow counts. No recurrence or bound on incumbent norms is used.

If desired, all candidate blocks can be independently randomized. Use
the isometric coefficient space with piecewise constant lower rows on
the cells \(A_j\), readouts in the same feature span, and arbitrary
middle matrices. Its dimension is \(d=2J+n+d_1d_2\). Set

\[
R_*=(T_*^2+\|M_*\|_F^2+C^2)^{1/2},\quad
A_*^2=1+C^2B_1^2B_2^2(1+\|M_*\|_F^2),\quad
B_l=\mathop{\rm ess\,sup}|b_l|.
\]

For any state \(S\), boundedness and the Lipschitz constant one of tanh
give \(L(S)\le A_*^2\|S-S_*\|^2\): subtract the lower features, then
the upper preactivations as
\((M-M_*)a_i+M_*(a_i-a_i^*)\), and finally the readout using \(c_*\).
Drawing all coefficients from
\(N(0,(R_*+1)^2I_d/d)\) gives (10)--(12) with \(n\) replaced by
\(d\), and

\[
q_d=\frac{(d/(2e))^{d/2}}{\Gamma(d/2+1)}
       [A_*(R_*+1)]^{-d}.                                     \tag{13}
\]

This is still a specially constructed global proposal family. The present
polynomial bound does not by itself give convergence of population
parameters; the stronger construction below does.

## 4. Rare offers from a small auxiliary search: exponential rate

Retain the same independent rate-\(\varepsilon\) event clock, but add
one auxiliary vector \(b\in\mathbb R^n\), initially zero. Its coefficients
do not freeze or constrain the incumbent's hidden-layer evolution.
At each event, if \(\ell=V(b)>0\), draw \(G\sim N(0,I_n)\) and offer
the auxiliary update

\[
b'=b+\frac{\sqrt{\kappa\ell}}{4n\Lambda}G.                      \tag{14}
\]

Accept this update within the auxiliary chain exactly when
\(V(b')<V(b)\). If \(V(b)=0\), leave \(b\) unchanged. Offer its resulting
state \(S(b)\) to the incumbent, again replacing the incumbent exactly
when it improves its own current loss. Continue full GF at all other
times. In particular, rejected offers never stop the flow. The complete
restartable Markov state is \((S,b)\), not \(S\) alone.

Write \(b_k,V_k\) for the auxiliary state and loss after event \(k\),
and set

\[
q_0=\frac{e^{-2}}{2\sqrt{2\pi}},\qquad
\gamma=\frac{q_0\kappa}{4n\Lambda}\in(0,1),\qquad q=1-\gamma.
                                                               \tag{15}
\]

Here is the complete single-event contraction. For \(u=b-b_*\), let
\(g=Qu\), \(\ell=u^TQu\), and
\(\sigma=\sqrt{\kappa\ell}/(4n\Lambda)\). Then

\[
\|g\|^2\ge\kappa\ell,\qquad
V(b+\sigma G)-\ell=2\sigma g\cdot G+\sigma^2G^TQG.             \tag{16}
\]

Resolve \(G\) along \(g/\|g\|\) and its independent orthogonal
component. The event that the parallel coordinate belongs to \([-2,-1]\)
has probability at least \(e^{-2}/\sqrt{2\pi}\). If \(n\ge2\), the
orthogonal squared norm is at most \(2(n-1)\) with probability at least
one half, by its mean \(n-1\) and Markov's inequality. For \(n=1\) it
is identically zero. Their joint event therefore has probability at least
\(q_0\), and on it \(g\cdot G\le-\|g\|\), \(\|G\|^2\le4n\).
Equation (16) is then at most

\[
-2\sigma\sqrt{\kappa\ell}+4n\Lambda\sigma^2
=-\frac{\kappa\ell}{4n\Lambda}.
\]

This update is accepted; elsewhere the acceptance test still prevents
increase. At zero loss the following inequality is also exact:

\[
E[V_{k+1}\mid b_k]\le qV_k,\qquad E V_k\le q^k.                \tag{17}
\]

At time zero both losses are one. Flow and accepted replacements decrease
the incumbent loss. At each event the incumbent either takes the auxiliary
offer or already has no larger loss. Induction, including the full intervening
flow segments, gives

\[
L(S(t))\le V_{N_t}\quad\text{for every }t\ge0.                  \tag{18}
\]

The auxiliary sequence is independent of event times: it uses only its
own Gaussian draws and loss values. Therefore (17), (18), and the Poisson
generating function prove the physical-time bounds

\[
\begin{split}
E L(S(t))&\le e^{-\varepsilon\gamma t},\\
P\{\tau_a>t\}&\le\min\{1,a^{-1}e^{-\varepsilon\gamma t}\},\\
E\tau_a&\le\frac{\log(1/a)+1}{\varepsilon\gamma},
                    \qquad 0<a<1,\\
t\ge\frac{\log(1/(a\delta))}{\varepsilon\gamma}
&\quad\Longrightarrow\quad P\{L(S(t))\le a\}\ge1-\delta.
\end{split}                                                     \tag{19}
\]

The expectation formula splits the survival integral at
\(t=\log(1/a)/(\varepsilon\gamma)\). Monotonicity and the first line
prove almost-sure zero loss, by the same countable-threshold argument as
in Section 3. The geometry cost is explicit: \(\kappa,\Lambda\) are
eigenvalues of the matrix in (7). For certified estimates one can use
\(\kappa\ge\mu_{\min}\lambda^2\), \(\Lambda\le n^2\), and
\(\lambda\ge\det K/n^{n-1}\). These bounds can be extremely poor.

The parameter \(\varepsilon\) in this theorem changes only event timing.
The auxiliary Gaussian steps shrink as its loss decreases; its initial
steps and the incumbent's global replacement jumps do not shrink as
\(\varepsilon\downarrow0\).

## 5. Well-posedness, monotonicity, and a parameter endpoint

For either construction, the Poisson clock has finitely many events on
every bounded interval, almost surely. Its independent interarrival times
are exponential with mean \(1/\varepsilon\). A direct nonexplosion
argument observes that the probability of an interarrival exceeding
\(1/\varepsilon\) is \(e^{-1}\); independence implies infinitely many
such intervals almost surely, because the probability of avoiding them
forever after any specified index is zero. Their sums tend to infinity.
Every drawn finite-dimensional Gaussian vector has finite coordinates;
all candidates are states of \(\mathcal H\). Concatenate the globally
defined unique flow segments and the stated measurable accept/reject map.
This constructs a unique right-continuous process with left limits at
every finite time, path by path. The losses are nonincreasing. The upper
marks and lower marks themselves are never resampled.

Write \(v(t)=\|F(S(t))\|\) outside event times, and let
\(D_j=L(S(T_j^-))-L(S(T_j))\ge0\) be each accepted loss drop, zero
for a rejection. On every finite interval, the exact energy identity is

\[
L(S(t))+\int_0^t v(s)^2ds+\sum_{T_j\le t}D_j=1.                \tag{20}
\]

For the exponential-rate construction only, put
\(a_0=\varepsilon\gamma>0\). Its entire continuous path length has a
finite expectation:

\[
E\int_0^\infty v(s)ds\le\frac{2}{\sqrt{a_0}}.                 \tag{21}
\]

Proof. For \(0<\beta<a_0\), multiply the Stieltjes energy identity by
\(e^{\beta t}\) and integrate by parts on \([0,T]\). Dropping the
nonnegative weighted jump drops and terminal loss gives

\[
\int_0^T e^{\beta s}v(s)^2ds
\le1+\beta\int_0^T e^{\beta s}L(S(s))ds.
\]

Take expectations, use (19), and let \(T\uparrow\infty\) by monotone
convergence on the nonnegative left side. The result is at most
\(a_0/(a_0-\beta)\). Cauchy--Schwarz for the time integral, followed
by Cauchy--Schwarz for expectation, bounds the expected unweighted length
by \(\sqrt{a_0/[\beta(a_0-\beta)]}\). Taking \(\beta=a_0/2\)
proves (21). In particular this length is finite almost surely.

For the auxiliary offers \(Z_k=S(b_k)\), (9), (17), and
Cauchy--Schwarz give

\[
E\sum_{k=1}^\infty\|Z_k-S_*\|
\le\frac{\sqrt q}{\sqrt\chi(1-\sqrt q)}<\infty.                \tag{22}
\]

Enumerate only accepted incumbent jumps. The distance of its pre-jump
state from the previous accepted offer is at most the continuous path
length between them. The triangle inequality through \(S_*\) consequently
gives, for every finite collection of accepted jumps,

\[
\sum\|S(T_j)-S(T_j^-)\|
\le\|S_0-S_*\|+2\sum_{k=1}^\infty\|Z_k-S_*\|
                 +\int_0^\infty v(s)ds.                       \tag{23}
\]

For the first jump use \(S_0\) in place of a previous offer; each later
offer distance appears at most twice. Letting the number of jumps grow
proves the inequality for all jumps. Combining (21)--(23) bounds the
expected total variation in the physical Hilbert space by

\[
E\operatorname{Var}_{[0,\infty)}S
\le\|S_0-S_*\|
 +\frac{2\sqrt q}{\sqrt\chi(1-\sqrt q)}
 +\frac4{\sqrt{\varepsilon\gamma}}<\infty.                     \tag{24}
\]

Completeness of \(\mathcal H\) and finite total variation give a limit
\(S_\infty\in\mathcal H\), almost surely. Continuity of the loss and
(19) give \(L(S_\infty)=0\). If infinitely many incumbent offers are
accepted, their auxiliary indices tend to infinity and (22) forces those
post-jump states to tend to \(S_*\), so \(S_\infty=S_*\). If only
finitely many are accepted, the final full-flow segment converges to some
zero-loss state, which need not be \(S_*\). No deterministic convergence
rate in parameter norm is asserted.

## 6. Exact compact-time convergence to original full GF

Let \(S^0(t)=\Phi_tS_0\) be the original deterministic trajectory.
Couple it to either rare-event process \(S^\varepsilon\) by the same
initial state. Before the first event, their equations and initial state
are identical, so uniqueness gives equality. Hence for every \(T<\infty\),

\[
P\{S^\varepsilon(t)=S^0(t)\ \text{for all }0\le t\le T\}
\ge e^{-\varepsilon T}.                                      \tag{25}
\]

For every \(r>0\),

\[
P\left\{\sup_{0\le t\le T}
 \|S^\varepsilon(t)-S^0(t)\|_{\mathcal H}>r\right\}
\le1-e^{-\varepsilon T}\le\varepsilon T.                      \tag{26}
\]

This gives convergence in probability in the raw uniform path metric,
even though perturbed paths can jump. The total variation distance
between their path laws (defined as the supremum over measurable events)
is at most \(1-e^{-\varepsilon T}\), by this coupling. It controls every
measurable bounded path observable, not only training loss.

For the auxiliary construction the approximation also holds in every
finite raw moment on a fixed horizon. Since \(V_k\le1\), (9) gives
\(\|Z_k\|\le R_*+1/\sqrt\chi\). By (20) the total continuous path
length on \([0,T]\) is at most \(\sqrt T\), pathwise. Let

\[
R=\max\{\|S_0\|,R_*+1/\sqrt\chi\},\qquad
C_T=R+\|S_0\|+2\sqrt T.
\]

After the most recent accepted jump the incumbent starts within radius
\(R\); if there was none it starts at \(S_0\). Thus its norm is at most
\(R+\sqrt T\), while the original norm is at most
\(\|S_0\|+\sqrt T\). Combining with (25), for every \(r\ge1\),

\[
E\left[\sup_{t\le T}\|S^\varepsilon(t)-S^0(t)\|^r\right]
\le C_T^r(1-e^{-\varepsilon T})\longrightarrow0.                \tag{27}
\]

An almost-sure coupling of the whole approximation family is possible:
take one sequence of unit-rate exponential interarrivals \(E_j\), and
put \(T_j^\varepsilon=(E_1+\cdots+E_j)/\varepsilon\), using one
sequence of candidate randomness. Since \(E_1>0\) almost surely, for
each fixed \(T\), all sufficiently small \(\varepsilon\) have no event
on \([0,T]\). The coupled paths are eventually exactly equal there.
Countably many integer horizons give almost-sure local uniform convergence
on \([0,\infty)\). This is a compact-time statement, not uniform agreement
for all time at each fixed positive \(\varepsilon\).

For independent refreshes and a bounded differentiable cylinder observable
\(f\), the generator is
\(Df(S)F(S)+\varepsilon E[f(J(S,Z))-f(S)]\), where \(J\) is the
accept/reject map. Its jump term is bounded by
\(2\varepsilon\|f\|_\infty\). The auxiliary process has the analogous
formula on \((S,b)\). This is another precise meaning of a small
modification; it does not bound jump size or give a small additive drift.

## 7. Limit order, physical cost, and the small-kick obstruction

For every \(\varepsilon>0\), (19) gives all-time fitting and a parameter
endpoint. For every fixed \(t\), (25) and \(0\le L\le1\) give
\(E L(S^\varepsilon(t))\to L(S^0(t))\). Therefore

\[
\lim_{\varepsilon\downarrow0}\lim_{t\to\infty}
 E L(S^\varepsilon(t))=0,
\qquad
\lim_{t\to\infty}\lim_{\varepsilon\downarrow0}
 E L(S^\varepsilon(t))=L_\infty^0,                              \tag{28}
\]

where original GF's monotonicity gives \(L_\infty^0\ge0\), but its
value is not proved here. Exchanging these limits would assume exactly
the missing conclusion about original GF. Likewise, (26) ensures
closeness on growing horizons if \(\varepsilon T_\varepsilon\to0\),
whereas (19) forces small loss from its own bound when
\(\varepsilon T_\varepsilon\to\infty\). Those are distinct regimes.

There is a matching elementary obstruction to uniform-in-frequency
acceleration. If original GF has \(L(S^0(t))>a\) at a specified time
\(t\), then

\[
P\{\tau_a^\varepsilon>t\}\ge e^{-\varepsilon t}.               \tag{29}
\]

This is the event of no intervention; original loss monotonicity ensures
that the original path has not crossed \(a\) earlier either. If original
GF were to stay above \(a\) forever, then
\(E\tau_a^\varepsilon\ge1/\varepsilon\), and confidence
\(1-\delta\) would require time at least
\(\varepsilon^{-1}\log(1/\delta)\). This conditional observation
does not assert that such a nonfitting canonical dataset exists.

The rare event mechanism grants each fixed positive target a chance of
success independent of how far the incumbent has traveled. It achieves
this by absolute global candidates. In the exponential variant its
strong contraction is entirely the auxiliary positive-definite quadratic
readout problem. The full flow contributes descent but is not credited
with the global guarantee. The auxiliary search never computes a fitted
readout, but its data-dependent family is engineered to contain one.

Replacing an accepted global candidate by an infinitesimal displacement
toward it does not preserve the proof: a straight path can cross an
uphill region even when its endpoint has lower loss. Restricting proposal
norms also destroys the incumbent-independent success event in (10).
For centered small Gaussian kicks, the allowed source gives state-ball
probabilities depending on the incumbent norm, with positive-loss norm
escape still unresolved for the original strict-decrease algorithm.
Thus no implication from (19), (25), or (27) to unconditional fitting
under bounded small kicks is established here. No impossibility theorem
for such more local processes is claimed either.

If proposals have positive processor cost, (19) is a physical-flow-time
statement for the exact hybrid process, not an elapsed-computation bound.
For example, charging a fixed deterministic cost \(c\) at each event and
pausing GF during that charge produces a different clock. Since the
event count is Poisson in accumulated GF time, it can be translated with
a separate Poisson-count bound; one must specify this convention rather
than rename proposal count as physical time.

## 8. Claim and check record

| Claim | Status and scope |
|---|---|
| Full-GF rare independent refresh process exists globally | Proved, every fixed \(\varepsilon>0\) |
| Nonincreasing loss and explicit polynomial physical-time bounds | Proved in (10)--(13), global candidate replacement |
| Auxiliary rare-offer exponential bounds, counting all time/events | Proved in (14)--(19), exact-oracle population process |
| Finite total physical parameter variation and zero-loss endpoint | Proved in (20)--(24), auxiliary construction |
| Exact agreement with original GF on compact intervals with high probability | Proved in (25)--(27), limit \(\varepsilon\downarrow0\) at fixed horizon |
| Almost-sure local uniform GF approximation under one coupling | Proved after (27) |
| Uniform-in-time closeness or transfer of fitting to original GF | Not established; (28)--(29) expose the limit obstruction |
| Unconditional fitting for bounded small incumbent kicks or ordinary SDE noise | Open here; no such identification is made |

Author check: agent `natural_noise_rare` directly checked all displayed
algebra, the Poisson conditioning, event-time independence, loss dominance,
weighted energy integration, and summation of accepted jump distances.
Checks include \(n=1\), zero auxiliary loss, no accepted incumbent jumps,
finitely versus infinitely many accepted jumps, arbitrary ill-conditioning,
all rejected events, canonical zero readout, and the noncommuting limit
order. Source hashes above identify the study inputs. Metadata-only Git
checks preceded the sole owned-file edit; no shared/index mutation was
made. The result is an internally derived and author-checked candidate;
no independent review is claimed. Frozen before any route comparison.
