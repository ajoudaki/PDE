# All-time prediction stability and the quantitative width question

28 September 2026. Continuation of the same research question. This note
records the second focused attempt to prove the numerical compression
corollary under the existing small-label hypotheses. It does not change
the optimizer, the initialization, the activation class, or the paper.

**Status: the requested numerical corollary is not proved.** A new exact
all-time prediction comparison, several quantitative matrix-return
results, and an inverse-free representation of the response term are
proved below and in the linked complete derivations. The remaining
obligation is a quantitative joint law for the actual trained matrix
and its transpose. None of the reduced Gaussian models is substituted
for that neural-network law.

## 1. The requested statement and the existing certificate

Keep fixed training data of size m, input dimension d, and hidden depth
L. Keep the canonical Gaussian first/hidden initialization, exactly zero
readout, a positive limiting initial readout-feature Gram gap, and fixed
labels of RMS Y below the existing width-independent threshold. Each
activation is C1 with bounded derivative and globally Lipschitz derivative;
activation values may have linear growth. Use the actual autonomous
learning-speed-clock closure of order q.

For a fixed test law mu with finite second moment let

\[
 \mathcal E_{n,q}=\left(\int\sup_{t\ge0}
  |\widehat f_{n,q}(t,x)-f_\infty(t,x)|^2\,d\mu(x)\right)^{1/2}.
\]

The proved study certificate remains

\[
 \mathcal E_{n,q}\le C_\mu q^{-2}e^{K\sqrt{\log(e+q)}}+\eta_{n,\mu},
 \qquad \eta_{n,\mu}\longrightarrow0\quad\hbox{in probability}.
 \tag{1}
\]

It holds simultaneously in q on the stated common initialization events.
Its constants and the order term have no width or time dependence. The
remainder is dense-only and independent of q, but it has no established
numerical width rate. More explicitly it can be taken to include both
the trained-carrier transfer remainder and dense prediction error:

\[
 \eta_{n,\mu}=C_\mu\Phi(a_n)+d_{n,\mu},\qquad
 \Phi(u)=u e^{K\sqrt{\log(e+1/u)}}.
\]

The desired sufficient moving-state cost would follow from a bound such
as

\[
 \mathcal E_{n,q}\le C_{\mu,\delta}
 \{q^{-2}e^{K\sqrt{\log(e+q)}}+
       n^{-1/2}e^{K_\delta\sqrt{\log(e+n)}}\}
 \tag{2}
\]

with probability at least 1-delta, for sufficiently large n, without
further assumptions. Equation (2) is the target, not a theorem of this
note. The study's qualitative width passage does not imply it.

## 2. A new exact comparison at the prediction level

This part is a theorem. It applies to the actual dense network or actual
moment closure, and uses the dense population flow only as the reference.
The complete derivation is also in
[WIDTH_RATE_DIRECT_PREDICTOR_R2.md](WIDTH_RATE_DIRECT_PREDICTOR_R2.md).

Normalize training-vector norms by
\(|v|_m^2=m^{-1}\sum_a v_a^2\). Write h(t,x) for the last hidden feature
vector and define the two-time forward correlations

\[
 Q_{ab}(t,s)=\frac{h(t,x_a)^T h(s,x_b)}{mn},\qquad
 Q_b^x(t,s)=\frac{h(t,x)^T h(s,x_b)}{mn}.
 \tag{3}
\]

For the population reference, replace n-normalized inner products by
population expectations, and use a star. All matrices in (3) act on
training vectors with the ordinary summation convention.

Zero initial readout and its canonical equation give the exact identity

\[
 w(t)=-\frac2m\sum_b\int_0^t r_b(s)h(s,x_b)\,ds.
\]

Consequently, for both dense training and the autonomous closure,

\[
 r(t)=-y-2\int_0^t Q(t,s)r(s)\,ds,\qquad
 f(t,x)=-2\int_0^t Q^x(t,s)r(s)\,ds.
 \tag{4}
\]

The established small-label estimates imply for the reference

\[
 Q_*(t,t)\succeq\lambda I,
 \quad\sup_t\|Q_*(t,t)\|\le G,
 \quad b(s):=\sup_{t\ge s}\|\partial_sQ_*(t,s)\|
                    \le C Y\rho_*(s),
\]
\[
 B:=\int_0^\infty b(s)\,ds\le CY^2<\infty.
 \tag{5}
\]

Indeed, every hidden-weight velocity has canonical norm at most
CY rho_*(s), because its backward field has RMS at most CY. The forward
differential on the physical tube is bounded using operator norms and
activation slopes only. Thus the training-feature velocity has population
RMS at most CY rho_*(s). Differentiating the second factor in (3) proves
(5). No derivative of a backward gate is taken. The argument below needs
only B finite, not B<lambda; it does not reduce the existing label range.

Define the actual residual-weighted sources

\[
 D(t)=-2\int_0^t[Q(t,s)-Q_*(t,s)]r(s)\,ds,
\]
\[
 D_x(t)=-2\int_0^t[Q^x(t,s)-Q_*^x(t,s)]r(s)\,ds.
 \tag{6}
\]

Set e=r-r_* and E(t)=integral_0^t e(s)ds. Subtract (4) and integrate by
parts in s. Since E(0)=0, the result is exactly

\[
 E'(t)=-2Q_*(t,t)E(t)
       +2\int_0^t\partial_sQ_*(t,s)E(s)\,ds+D(t).
 \tag{7}
\]

The homogeneous propagator of the first term has norm at most
exp[-2lambda(t-u)], by differentiating its squared norm. Variation of
constants in (7), and then interchange of two nonnegative integrals, give

\[
 |E(t)|_m\le\frac{\|D\|_\infty}{2\lambda}
             +\frac1\lambda\int_0^t b(s)|E(s)|_m\,ds.
\]

The integral integrating factor therefore proves

\[
 \boxed{\sup_{t\ge0}|E(t)|_m
       \le\frac{e^{B/\lambda}}{2\lambda}\|D\|_\infty.}
 \tag{8}
\]

For a passive input x, forward RMS bounds and (5) likewise give

\[
 G_x:=\sup_t\|Q_*^x(t,t)\|\le C a(x),\qquad
 B_x:=\int_0^\infty\sup_{t\ge s}\|\partial_sQ_*^x(t,s)\|ds
                         \le C a(x)Y^2,
 \quad a(x)=1+\|x\|/\sqrt d.
\]

Integration by parts in the passive version of (4) and (8) now yield

\[
 \boxed{\sup_{t\ge0}|f(t,x)-f_*(t,x)|
 \le \frac{G_x+B_x}{\lambda}e^{B/\lambda}\|D\|_\infty
              +\sup_{t\ge0}|D_x(t)|.}
 \tag{9}
\]

Minkowski gives the whole-input consequence

\[
 \mathcal E_\mu(f,f_*)
 \le C\|a\|_{L^2(\mu)}\|D\|_\infty+
      \left(\int\sup_{t\ge0}|D_x(t)|^2d\mu(x)\right)^{1/2}.
 \tag{10}
\]

Thus output error can be bounded without a parameter-distance estimate,
without a derivative of the compression source, without a backward-tail
comparison, and without a factor growing with physical time. The source
in (6) retains the actual finite residual and trained correlations; it is
not an oracle source.

## 3. Progress on producing the width source

The following complete lemmas concern precisely specified Gaussian
models. They remove several unnecessary obstacles, but have not yet
been assembled into a law for the actual network.

**Nonlinear Gaussian return.** For g standard Gaussian in R^n and
U in Gaussian W1,2 with values in R^n,

\[
 \mathbb E\left|\frac{g^TU-\operatorname{tr}DU}{\sqrt n}\right|^2
 =\frac1n\mathbb E\left[\|U\|^2+\operatorname{tr}((DU)^2)\right]
 \le\frac1n\mathbb E[\|U\|^2+\|DU\|_F^2].
 \tag{11}
\]

In (11), the trace term means tr((DU)(DU)), not (tr DU)^2. Gaussian
adjointness and the commutator partial_j delta_i=delta_i partial_j+1_i=j
prove the identity for smooth sources; W1,2 approximation proves the
displayed extension. This retains the full nonlinear response and uses
only one weak derivative. A Hilbert--Schmidt chain-rule estimate also
permits adaptive boundary histories; the precise conditions and proof
are in Sections 7--8 of the direct-predictor report.

**Stable returned vectors, even for singular history covariances.** Let
G(h) be an isonormal Gaussian process on a Hilbert source space H. For
F in L2, the vector m_F defined by

\[
 \langle m_F,h\rangle=\mathbb E[F G(h)]
\]

exists and satisfies

\[
 \|m_F-m_{\widetilde F}\|_H\le\|F-\widetilde F\|_{L^2}.
 \tag{12}
\]

For a finite named representation F=F_0(G(h_1),...,G(h_k)), Gaussian
integration by parts identifies m_F with
sum_j E[partial_j F_0]h_j. No inverse covariance appears. This controls
the contracted response vector, rather than possibly unstable individual
response coefficients. It does not make infinite-dimensional Gaussian
white noise an H-valued iid observation.

**Continuous adaptive history feedback.**
[WIDTH_RATE_ACTIVITY_CAVITY_R2.md](WIDTH_RATE_ACTIVITY_CAVITY_R2.md)
proves a complete root-width theorem for a Hilbert-valued Gaussian
roundtrip with a Lipschitz gate, an independent scalar Gaussian base,
and a fixed trace-class source covariance. The adaptive message solves
the actual nonlinear return equation. A uniform empirical-process
estimate over the entire Hilbert ball gives O_Pr(n^-1/2), with a
polynomial-confidence n^-1/2 log^2(n) version. There is no time-node
count and no extra gate derivative. Its independent-row hypothesis is
proved in the reduced model, not assumed for trained neurons.

**Correct forward/transpose coupling in reduced programs.**
[WIDTH_RATE_CAUSAL_COUPLING_R2.md](WIDTH_RATE_CAUSAL_COUPLING_R2.md)
proves joint Sobolev-history estimates for one Gaussian matrix and its
actual transpose with matrix-independent sources, and an exact
transpose-then-forward return with its response term. The same report
develops further return comparisons and records their scopes. Ordinary
Gaussian history transport must not be silently used as a chronological
conditioning identity or as proof of the initialized matrix's marginal.

All these bounds are compatible with the original activation regularity.
They do not assert that the trained finite network has independent
Gaussian source rows. The counterexamples in the detailed notes rule out
specific proposed proof shortcuts, not the neural-network claim.

## 4. The remaining theorem-level obligation

For actual closure histories, an estimate

\[
 \|D_{n,q}\|_\infty+
 \left(\int\sup_t|D_{n,q,x}(t)|^2d\mu(x)\right)^{1/2}
 \le C_{\mu,\delta}\{q^{-2+o(1)}+n^{-1/2+o(1)}\}
 \tag{13}
\]

would finish the prediction and complexity result through (10). This is
a potentially weaker target than quantitative strong coupling of every
trained carrier. It is not supplied by the already proved resolvent.

The same matrix generates the finite forward histories and is then
reused on their nonlinear backward histories. Conditioning exposes an
order-one response term and a centered innovation. The new lemmas
control some response terms and some exact Gaussian roundtrips. What is
still missing is their **joint adaptive comparison for the actual deep
flow**, with the canonical Gaussian matrix marginal and constants
controlled as its time description is refined. Centered return noise
from different row cavities is not independent merely because each row
was Gaussian before training.

The capped deletion proposal also remains incomplete: ordinary RMS
field error does not automatically control the Euclidean discrepancy of
a single inserted response pulse. Using that discrepancy in a width
recursion would conceal a sqrt(n) loss. Whole-row first-chaos projections
avoid that loss for the mean response, but the joint centered innovation
still needs its own law. The complete direct-predictor report distinguishes
these two constructions explicitly.

## 5. What can actually be said about moving state now

Solving the proved order term gives

\[
 q_\varepsilon=\varepsilon^{-1/2}
                 \exp[O(\sqrt{\log(1/\varepsilon)})].
 \tag{14}
\]

Let N_mu(epsilon,delta) be a sufficient width beyond which the remainder
in (1), including the exceptional initialization event, is at most
epsilon/2 with probability at least 1-delta. Such an N exists by the
proved convergence in probability. No power bound for it is established.
At this width the rigorous sufficient moving-state count is

\[
 2(L-1)m\,N_\mu(\varepsilon,\delta)q_\varepsilon
       +N_\mu(\varepsilon,\delta)(d+1)+O(1).
 \tag{15}
\]

For every deterministic q_n tending to infinity with q_n=o(n), the
actual closure still converges to the same all-time population predictor
while its moving state is o(n^2). This qualitative compression statement
does not require a numerical width rate and remains valid.

If (2) or (13) were proved, their sufficient choices would be
n_epsilon=epsilon^-2 exp[O(sqrt(log(1/epsilon)))] and (14), giving
epsilon^-5/2 exp[O(sqrt(log(1/epsilon)))] moving state. That calculation
is correct, but its width premise remains unproved. It is a sufficient
budget calculation, not a lower bound or an optimality theorem. The fixed
initialized matrices and their dense actions remain outside the moving
count; no total-storage or per-step-runtime reduction follows from that
exponent alone.

## 6. Scope of this attempt

The coordinator reconstructed the new predictor resolvent, Gaussian
divergence/response identities, static forward/transpose coupling, and
Hilbert-ball empirical-return argument. The scoped authors checked their
own detailed derivations. These are internal proof checks, not independent
promotion reviews. There were no new training experiments, external
literature searches, manuscript edits, commits, or Git mutations in this
continuation. The earlier downloaded primary-source packet was available
to the specified coupling route. Concurrent repository changes were kept.
