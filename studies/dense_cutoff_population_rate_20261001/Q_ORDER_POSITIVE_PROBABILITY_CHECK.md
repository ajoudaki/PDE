# Internal probability audit of finite cavity reinsertion

2026-10-03. Internal collaborative reconstruction, not a promotion review.
This note checks the complete local insertion, stopping, empirical-moment,
and prediction-comparison chain in Q_ORDER_POSITIVE_ROUTE.md.

**Final verdict: internal PASS.** For two tanh hidden layers, fixed finite
sphere data with compatible duplicate/antipodal labels, and sufficiently
small fixed labels, the actual unclipped same-width closure tracks dense
training with all-time prediction error $C_\mu/\sqrt n$ using
$q_n=\lceil n^{1/4}\exp\{A_*\sqrt{\log(e+n)}\}\rceil=n^{1/4+o(1)}$.
The original residual-RMS clock and shared Gaussian initialization are
retained. The conclusion holds on events of probability tending to one;
the width threshold may depend on the fixed data, fixed label vector, and
confidence. This is not an arbitrary-depth or dense-to-population rate.

The full-network stop is never conditioned on as an independence event.
Autonomous cavities, whole-path Gaussian suprema, and a proof-only radial
projection preserve the needed Gaussian independence. Section 9 reconstructs
the strengthened local nonlinear estimate, and Section 10 checks the weighted
compatible quotient. These checks supersede the interim conditional status
under which the outer argument was first developed.

The final source has SHA-256
`9026935501ce94886d9eee81c6d318d3f45ac2f526597be5de71b0989a959f27`.
The complete mathematical reconstruction used source SHA-256
`cb38dfcbd752e50f0cde1ae60a8d16f7db5bcd2fafbd69dc65546a2efeb3e590`.
The final version adds only the missing display-math closing delimiter
after the source's equation (14); that formatting correction was inspected
and changes no mathematical content or verdict.

Inputs read were the complete `FINITE_MIXED_MOMENT_ROUTE.md` and its complete
internal check, the complete `Q_ORDER_POSITIVE_ROUTE.md`, and the
previously authorized current-paper definitions and fitting/speed arguments.
The later end-to-end check also reads the complete
`NONORTHOGONAL_DIRECT_ROUTE.md` and `NONORTHOGONAL_CHECK.md`, with the
current paper's complete tracking proof. The intermediate strengthened
insertion source read for Sections 1--7 had SHA-256
`145b1b7d94f636f81c2c28bed2a9bf1a9f7bdda68be4f8c06c0a90aa047b7de6`.
Only the assigned report is written. There were no experiments, other-study
reads, manuscript edits, or Git operations. Canonical notation, the neural
response conventions, rigorous-math, and adversarial research instructions
were applied.

## 1. Precise objects and required analytic inputs

Use the two-tanh dense network from the source. Write

\[
\delta_a=w\odot\operatorname{sech}^2z_a^{(2)},\qquad
k_a=W^\top\delta_a,\qquad K_i(t)=\max_a|k_{a,i}(t)|,
\qquad S=2Y/\kappa>0.
\]

The ordinary initialized outgoing column of first-layer neuron $i$ is
$x_i=W_{0,:,i}\sim N(0,I_n/n)$. All normalizations remain $n$ after
deleting a fixed set $I$ of first-layer neurons. An autonomous cavity
deletes their incoming rows and outgoing columns and generates its own
residuals. Superscript $(-I)$ denotes this cavity.

Fix positive constants $\eta,A,B$, put

\[
M_n=AS\log n,\qquad T_n=c_T\log n,
\qquad
\mathcal M_\eta(t)=\kappa\int_0^t e^{-\kappa s}
   \frac1n\sum_i e^{\eta K_i(s)/S}ds.
\]

Let $\sigma$ be the first physical time up to $T_n$ at which the full
maximum reaches $M_n$ or its cumulative budget reaches $B$, capped at
$T_n$. Let $\sigma_{-I}$ be the analogous cavity stop with caps
$2M_n,2B$. These are physical stopping times; the network's learning clock
is still denoted by $\tau$.

The argument uses the following analytic inputs, reconstructed below with
their stated quantifiers.

1. A common initialization event $\mathcal G_n$, of probability tending
   to one, on which the full dense network has the manuscript's fitting and
   physical bounds. For every fixed deletion count $r$, the same event
   must imply the corresponding initialization bounds for all $r$-cavities,
   with a fixed smaller Gram margin, at all sufficiently large widths.
2. Conditional on a cavity's retained initialization, the external insertion
   lemma holds with failure at most $C_r e^{-n^c}$, uniformly over its
   admitted deterministic source controls. It compares the actual retained
   dynamics with that cavity until the common prefix of their stops.
3. The lemma yields a retained carrier discrepancy at most
   $\varepsilon_{n,r}=o(1)$, and an ordinary Euclidean top-response
   discrepancy at most $C_r n^{1/100}$, uniformly on that prefix.
4. Singleton insertion yields, for every sample and deleted neuron,
   \[
   |k_{a,i}(t)-x_i^\top\delta_a^{(-i)}(t)|
   \le R(B,S)+\varepsilon_{n,1},
   \quad R(B,S)=CS(1+S^2\sqrt B).
   \tag{1}
   \]
   The constant $C$ in this singleton statement is independent of later
   empirical moment order.
5. The smallness threshold for $S$ is independent of every fixed deletion
   count $r$. Constants and sufficiently-large-width thresholds may depend
   on $r$. Otherwise one cannot choose fixed labels first and subsequently
   send the empirical moment order to infinity.

The source proves items 2--4 through its equations (5)--(8). Section 9 of
this report reconstructs its nonlinear estimate (14), uniform source-control
event, and trace bound separately from the outer probability calculation.

The first item is compatible with the initialized geometry. Removing $r$
bounded first-layer features changes each initialized top preactivation by
$\sum_{i\in I}x_i h_{a,i}^{(1)}$, whose Euclidean norm is at most
$r\|W_0\|_{\rm op}$. Tanh is 1-Lipschitz, so the normalized top-feature
change is $O(r/\sqrt n)$, and its normalized feature Gram change is also
$O(r/\sqrt n)$. A full Gram margin therefore implies a smaller fixed
cavity margin. Retained operator and first-layer RMS bounds do not increase.
The fitting proof must be applied with a rectangular $n\times(n-r)$
hidden matrix and unchanged $n$ normalization; its norm and Gram estimates
have the same constants once that smaller initialization margin is fixed.
Choose one common $\kappa>0$ below the resulting full and cavity fitting
rates, and use this same value in $S$, the budget weight, and the horizon.
The smaller cavity Gram margin must not silently retain a larger decay rate
available only to the full system.

## 2. Transfer of the cavity stops

Fix a deletion set $I$ of size $r$. Until
$\min(\sigma,\sigma_{-I})$, the actual omitted first-layer histories are
bounded by one and have Lipschitz constant $C\log n$. Indeed their
derivatives are bounded by $C\rho M_n$, using the exact first-layer
update. Extend any such prefix constantly to $[0,T_n]$. The extended
control lies in the deterministic control class in the insertion lemma.
The event being uniform over that class is what permits a control selected
by the omitted Gaussian columns.

The omitted learned-column contribution has Euclidean size at most
$C_rS^2/\sqrt n$, by the actual column update and total residual
activity. It is the adaptive small source allowed in the insertion lemma.
These facts validate application of the lemma up to the common prefix;
they do not assume that the cavity has already survived until $\sigma$.

Suppose first that a cavity reaches its maximum cap before $\sigma$.
The retained-carrier comparison gives at that endpoint

\[
\max_{a,i\notin I}|k_{a,i}^{(-I)}|
\le M_n+\varepsilon_{n,r}<2M_n
\]

for sufficiently large width, a contradiction.

For the budget cap, use a relative exponential comparison:

\[
e^{\eta K_i^{(-I)}(t)/S}
\le e^{\eta\varepsilon_{n,r}/S}e^{\eta K_i(t)/S},
\qquad i\notin I.
\]

Integrating the positive time weight gives, at every common-prefix endpoint,

\[
\mathcal M_\eta^{(-I)}
\le e^{\eta\varepsilon_{n,r}/S}\mathcal M_\eta+O(r/n)
\le B+o(1)<2B.
\tag{2}
\]

The $O(r/n)$ term allows filling deleted coordinates with zero carriers;
it is absent if the sum simply omits them. Here $S>0$ is fixed before
width tends to infinity. Equation (2) contradicts a first earlier cavity
budget stop. Thus $\sigma_{-I}\ge\sigma$ on the insertion event.
Continuity includes a cap endpoint, and simultaneous attainment at a time
strictly below $\sigma$ gives the same contradiction.

This proof uses the lemma on a common prefix and then extends that prefix by
a strict cap margin. It does not use independence of the full stop. It also
removes the earlier provisional restriction
$2\eta A<1/10$: that restriction came from an unnecessary absolute
maximum bound on the difference of exponential budgets.

## 3. Independent whole-path Gaussian reference processes

Freeze every cavity's response at its own stop:

\[
d_a^{-I}(t)=\delta_a^{(-I)}(t\wedge\sigma_{-I}),
\qquad 0\le t\le T_n.
\]

If its cavity-measurable initialization conditions fail, define this proof
reference to be identically zero. On $\mathcal G_n$ at sufficiently large
width it agrees with the actual stopped cavity. In either case it is
independent of all columns $x_i$, $i\in I$.

The cavity's physical bounds give

\[
\max_{t,a}\frac{\|d_a^{-I}(t)\|_2}{\sqrt n}\le CS,
\qquad
\frac1{\sqrt n}\operatorname{Var}_{[0,T_n]}(d_a^{-I})\le CS,
\qquad d_a^{-I}(0)=0.
\tag{3}
\]

The total variation estimate follows from
\[
\dot\delta_a=\operatorname{sech}^2z_a\odot\dot w+
w\odot\tanh''z_a\odot\dot z_a.
\]
The normalized top-response speed is at most $C\rho$, with integrable
residual activity $CS$.
Freezing adds no jump. The constants in (3) are independent of each fixed
deletion count, after increasing its width threshold.

Conditional on the retained initialization, define

\[
Z_i^{-I}=\max_a\sup_{t\le T_n}|x_i^\top d_a^{-I}(t)|/S,
\qquad i\in I.
\]

These random variables are independent conditional on the common cavity.
They are not claimed independent without conditioning. For every fixed
$\lambda\ge0$, (3) gives a deterministic bound

\[
\mathbb E[e^{\lambda Z_i^{-I}}\mid\text{retained initialization}]
\le L(\lambda)<\infty,
\tag{4}
\]

uniform in width, the retained initialization, and each fixed deletion count.

One direct justification avoids any growing-time factor. Parameterize the
curve $d_a^{-I}/(S\sqrt n)$ by its bounded arc length. Its Gaussian
canonical distance is at most arc-length distance. Dyadic arc-length nets
have $O(2^j)$ points at level $j$; Gaussian increments between adjacent
levels have standard deviation $O(2^{-j})$. The scalar Gaussian tail and
a union bound show that all increments are bounded by
$C2^{-j}(\sqrt{j+1}+u)$ outside a set of probability $Ce^{-cu^2}$.
Sum these bounds in $j$, and take the union over the fixed samples. This
gives $\Pr\{Z_i^{-I}>C(1+u)\mid\text{cavity}\}\le Ce^{-cu^2}$.
Integrating this tail against a linear exponential proves (4).

Thus the finite Gaussian reference has the required linear-exponential
moments even though the actual carrier is adaptive.

## 4. Replacing singleton cavities by one common cavity

For a fixed set $I$ containing $i$, both $d^{-i}$ and $d^{-I}$
omit column $i$. Their difference is therefore independent of $x_i$.
The comparisons full-to-singleton and full-to-$I$ give on their good event

\[
\max_{a,t\le\sigma}\|d_a^{-i}(t)-d_a^{-I}(t)\|_2
\le C_r n^{1/100}.
\tag{5}
\]

The restriction $t\le\sigma$ is random and depends on $x_i$, so one
must not apply conditional Gaussian estimates to (5) directly.

There is a simple valid extension. Let $P_R$ be Euclidean projection onto
the ball of deterministic radius $R=C_r n^{1/100}$, increasing its
constant to dominate (5), and set

\[
\widetilde d_{a,iI}(t)=P_R(d_a^{-i}(t)-d_a^{-I}(t)).
\]

This is a proof-only reference process, not a modification of either
network. It is still independent of $x_i$, has deterministic norm at most
$R$, and equals the original difference throughout the good full prefix.
Projection onto a Euclidean ball is 1-Lipschitz, so (3) bounds its normalized
total variation by $CS$.

The conditional Gaussian process
$x_i^\top\widetilde d_{a,iI}(t)$ has maximal standard deviation at most

\[
D_{n,r}=C_r n^{-1/2+1/100},
\]

and canonical metric covering number at resolution $u$ at most
$1+CS/u$. Dyadic nets starting at scale $D_{n,r}$, with the same
increment argument as above, give a supremum bounded in expectation by

\[
C D_{n,r}\sqrt{\log(e+S/D_{n,r})}=o(1)
\]

and a tail at level $n^{-1/5}$ bounded by $C_r e^{-n^c}$, with a
fixed positive $c$ after decreasing it if necessary. A union over all
fixed-size sets and their members preserves a superpolynomial failure
bound. On the insertion event it follows that

\[
\max_{a,t\le\sigma}
|x_i^\top(d_a^{-i}(t)-d_a^{-I}(t))|\le n^{-1/5}.
\tag{6}
\]

No full-network event was conditioned upon. The radial projection makes the
small-variance bound hold on every retained outcome before the Gaussian
estimate is applied.

An alternative is to reapply the insertion lemma between cavities $(-i)$
and $(-I)$, inserting $I\setminus\{i}$, until their shared minimum
stop. That comparison and its event omit $i$. Freeze both at the shared
minimum, obtain (5) there, and use the same Gaussian estimate. The
full-to-cavity strict margins then put that shared stop after $\sigma$.
Generic Euclidean Lipschitz subtraction is not a substitute: it could cost
$e^{CT_n}$ and lose the required small projection scale.

## 5. Empirical moments, including collisions and failure events

Define the nonnegative stopped empirical supremum

\[
H_n=\mathbf1_{\mathcal G_n}\frac1n\sum_i
 \exp\left\{\frac\eta S\sup_{t\le\sigma}K_i(t)\right\}.
\]

By continuity and the maximum stop, $H_n\le n^{\eta A}$. Fix an
integer $k\ge1$. Union the insertion and projection events needed for
all deletion sets of size at most $k$. Their total failure probability on
$\mathcal G_n$ is $C_k n^{C_k}e^{-n^c}$. Its contribution to
$\mathbb EH_n^k$ is at most
$n^{k\eta A}C_k n^{C_k}e^{-n^c}=o(1)$.

Expand $H_n^k$ as a sum over $k$-tuples. For a tuple of distinct indices,
let $I$ be that tuple's set. Equations (1) and (6) bound its product on
the good event by

\[
\exp\{k\eta(R(B,S)+o(1))/S\}
 \prod_{i\in I} e^{\eta Z_i^{-I}}.
\]

Drop the nonnegative full-stop and good-event indicators **before** taking
the conditional expectation. Conditional independence for the common cavity
and (4) then bound this expectation by

\[
[e^{\eta R(B,S)/S}L(\eta)]^k+o(1).
\tag{7}
\]

The base of the $k$-th power is independent of $k$. This fact is
essential; a bound of the form $C_k^k$ with unbounded $C_k$ would not
close the fixed-budget argument.

For a tuple with $r<k$ distinct indices, give each index its multiplicity
$d_j$, with $\sum_{j=1}^r d_j=k$. The same argument gives the finite
constant

\[
e^{k\eta R(B,S)/S}\prod_{j=1}^r L(d_j\eta)+o(1).
\]

There are $O_k(n^{k-1})$ colliding tuples, so their normalized contribution
is $o(1)$. Using only the crude maximum $n^{k\eta A}$ for collision
terms would not suffice for every $k$; higher fixed Gaussian exponential
moments are what remove them.

Combining the terms, for every fixed integer $k\ge1$,

\[
\limsup_{n\to\infty}\mathbb EH_n^k
\le D(B,S)^k,
\qquad
D(B,S)=L(\eta)\exp\{C\eta(1+S^2\sqrt B)\}.
\tag{8}
\]

This proof only needs superpolynomial insertion failure for each fixed block
count; an exponential rate is more than enough. Initialization failure is
handled separately by $\mathbf1_{\mathcal G_n}$, not multiplied by the
large stopped maximum.

## 6. Closing the two caps and the order of choices

Choose $\eta,A>0$ first. Choose a fixed $B$ larger than, for example,
$4L(\eta)e^{C\eta}$. Then choose $S>0$ small enough that the insertion
lemma applies and $e^{C\eta S^2\sqrt B}\le2$. These choices are
independent of confidence and of empirical moment order. They give
$D(B,S)<B$, with a strict margin.

If the budget reaches $B$ by $\sigma\le T_n$, then

\[
B=\mathcal M_\eta(\sigma)
\le\frac1n\sum_i e^{\eta\sup_{t\le\sigma}K_i(t)/S},
\]

because the deterministic time weight has total mass at most one. Hence for
each fixed $k$, (8) and Markov's inequality give

\[
\limsup_n\Pr\{\mathcal G_n,\text{budget cap reached by }T_n\}
\le[D(B,S)/B]^k.
\]

Taking the infimum over fixed integers $k$ gives zero. The order is
explicit: first fix $k$ and let width grow, then take $k\to\infty$.
No growing-$k$ insertion theorem is needed. The label threshold must stay
fixed in this order of limits.

Singleton insertion and (4)'s Gaussian supremum tail also give

\[
\Pr\{\mathcal G_n,\text{maximum cap reached by }T_n\}
\le o(1)+Cn\exp[-c(A\log n-C)^2]\longrightarrow0.
\]

The fixed shift $R(B,S)/S$ is absorbed into $C$. Thus the $AS\log n$
cap is strictly above the resulting $O_{\Pr}(S\sqrt{\log n})$ maximum.

For all-time transfer, the physical bounds imply

\[
\frac{\|k_a(t)-k_a(T_n)\|_2}{\sqrt n}
\le CS e^{-\kappa T_n},\qquad t\ge T_n.
\]

Indeed differentiate $k_a=W^\top\delta_a$, use the operator and response
speed bounds, and integrate the residual. Choosing $c_T\kappa>1/2$
makes every coordinate's remaining change $o(1)$. The remaining weighted
budget is at most

\[
e^{-\kappa T_n}\exp\{\eta(M_n+o(1))/S\}
=n^{-c_T\kappa+\eta A+o(1)},
\]

which tends to zero when $c_T\kappa>\eta A$. Thus this argument supplies
an all-time empirical budget at most $B+o(1)$, and hence at most $2B$,
with probability tending to one.

This is a **high-probability budget bound**. It does not itself prove
$\mathbb E[\mathbf1_{\mathcal G_n}\mathcal M_\eta(\infty)]\le C$
for the unstopped process: rare trajectories after a stop may require an
additional uniform-integrability estimate. The high-probability bound is
sufficient for the finite carrier-tail implication in the mixed-moment note.

## 7. Probability verdict and safeguards

No fatal probability loophole was found in the repaired outer argument. Its
validity depends on the insertion conclusions in Section 1 with precisely
their uniformities. In particular:

- A cavity evaluated using the full residual driver is not an independent
  reference. The source uses autonomous cavities, which is the required
  construction.
- A Gaussian projection bound at a full-network stopping event is not
  justified by conditioning on that event. Sections 3--4 construct independent
  whole-path references first and use the event only for a pathwise identity.
- The common-cavity comparison must have a small Euclidean response
  discrepancy and controlled total variation. Projection by an independent
  column then is small; an arbitrary $O(n^{1/100})$ vector selected by that
  same column would not be small after projection.
- The moment base and label threshold must be independent of $k$.
  Dependence of fixed-$k$ remainders, Gaussian collision moments, and width
  thresholds on $k$ is harmless in the specified order of limits.
- A proof of the local nonlinear remainder is indispensable. The checked
  earlier mixed-moment sensitivity bound is only a conditional aggregate
  bound; it does not establish insertion by itself.

The probability mechanism checks with these safeguards. The required
external perturbation lemma is reconstructed in Section 9, closing the
analytic input to this argument.

## 8. Minimal end-to-end comparison after the insertion lemma

The near-quarter order schedule follows directly from the dense carrier
maximum. No additional Gaussian empirical square-exponential bound is needed.
This section reconstructs that implication using the insertion lemma
checked in Section 9.

Once the caps close, singleton insertion and the whole-path Gaussian bound
show, with probability tending to one,

\[
\max_{i,a,t\le T_n}|k_{a,i}(t)|
\le C S\sqrt{\log(e+n)}.
\tag{9}
\]

Take a fixed sufficiently large constant in the Gaussian union bound, so its
failure is $Cn^{1-cC^2}\to0$. The fixed reinsertion shift is absorbed
by the right-hand side for large width. This constant can be chosen before
confidence; no confidence-dependent order schedule is needed. The physical
tail after $T_n$, bounded in Section 6, extends (9) to all time after
enlarging $C$. The dense readout obeys $\|w_D\|_\infty\le S$.

Therefore the deterministic cutoff

\[
M_n^*=C S\sqrt{\log(e+n)}
\]

lies above every dense carrier and readout coordinate on these events.
The residual-weighted dense carrier tail $Z_n(M_n^*)$, as defined in
the paper's tracking argument, is exactly zero. This cutoff changes only
the proof; dense and closure training remain unclipped.

The completely checked two-tanh source estimate is

\[
\epsilon_q=\int_0^\infty\|E_2(t)\|_Fdt
\le CY^{5/2}q^{-2}\sqrt{\log(e+q)}.
\]

The paper's deterministic one-reference damping bound, retaining its
small-label scale, is

\[
D_{n,q}:=\sup_{t\ge0}d_n(\widehat\theta_{n,q}(t),\theta_{n,D}(t))
\le C e^{C_0YM}[\epsilon_q+Z_n(M)].
\]

It holds at every real cutoff $M>0$; integer cutoffs in the paper merely
index its probabilistic tail event. Substituting $M_n^*$ gives, with a
fixed finite $K$,

\[
D_{n,q}\le C\exp\{K\sqrt{\log(e+n)}\}
 q^{-2}\sqrt{\log(e+q)}
\tag{10}
\]

simultaneously for every order on the same dense-reference event. Constants
can be uniform on the reduced sufficiently-small-label interval; alternatively
they may depend on one fixed nonzero label vector.

Choose any fixed $A_*>K/2$ and set

\[
q_n=\left\lceil n^{1/4}
           \exp\{A_*\sqrt{\log(e+n)}\}\right\rceil.
\tag{11}
\]

Then $\log(e+q_n)=O(\log(e+n))$, and (10) yields

\[
\sqrt n D_{n,q_n}
\le C e^{-(2A_*-K)\sqrt{\log(e+n)}}
             \sqrt{\log(e+q_n)}\le C.
\tag{12}
\]

The last quantity is bounded because a positive exponential in
$\sqrt{\log n}$ dominates its polynomial factor. Also

\[
\frac{\log q_n}{\log n}=\frac14+o(1),\qquad q_n=o(n).
\]

Thus the schedule is $n^{1/4+o(1)}$. Its moving memory has size
$2mnq_n+n(d+1)+O(1)=n^{5/4+o(1)}$ for fixed data and dimension.
The initialized dense mixer is still stored exactly, so this statement is
about evolving state rather than total storage or matrix-vector runtime.

Finally the paper's whole-input comparison gives

\[
|\widehat f_{n,q_n}(t,x)-f_{n,D}(t,x)|
\le C(1+\|x\|_2/\sqrt d)D_{n,q_n}.
\]

For every fixed query law $\mu$ with finite second moment, square this
bound, take the physical-time supremum, and integrate. On the same event,

\[
\left(\int\sup_{t\ge0}
 |\widehat f_{n,q_n}(t,x)-f_{n,D}(t,x)|^2d\mu(x)\right)^{1/2}
\le\frac{C_\mu}{\sqrt n}.
\tag{13}
\]

Taking a supremum over a fixed bounded query set gives the corresponding
uniform absolute-error bound. The event probability tends to one, so for
every fixed confidence $1-\delta$, (13) holds at every sufficiently
large width with constants and an order schedule independent of width and
physical time. Width thresholds may depend on confidence. The compared
models have the same width and initialization.

This consequence is restricted to **two tanh hidden layers**, fixed finite
compatible data with positive quotient feature Gram, sufficiently small
fixed labels, zero readout, and the original residual-RMS closure. It does
not give a numerical dense-to-population rate, arbitrary-depth tracking,
large-label tracking, or incompatible-label tracking.

## 9. Reconstruction of the strengthened local insertion argument

The strengthened insertion source, unchanged scientifically in the complete
final version, supplies the following checks beyond the outer argument.

In coordinates $\Theta=(A,\sqrt nW,w)$, differentiating the actual
residual-driven vector field gives exactly

\[
D_\Theta F=-LL^\top-\frac2m\sum_a r_aD^2\mathcal F_a.
\]

The first term is a contraction generator, so only the residual-weighted
Hessian enters the norm growth estimate. The sole large Hessian block is
the diagonal first-layer block containing $k_{a,i}\tanh''(A_iv_a)$.
On the reference maximum stop its integrated norm is
$O(S+S^2\log n)$. A fixed sufficiently small $S$ therefore gives the
source's $\|J(t,s)\|\le n^{1/400}$, uniformly in all subintervals.
There is no factor $e^{CT_n}$ from treating the negative Gram as arbitrary
growth.

The derivative with respect to external second-layer preactivation has both
terms

\[
-\frac2{mn}\nabla\mathcal F_a\delta_a^\top
\quad\hbox{and}\quad
-\frac2m r_a(D_\Theta\delta_a)^\top.
\]

The first is the adaptive-residual derivative, of rank one; the second
includes all mixed forward and adjoint effects. These are exactly the source's
$P_a,Q_a$, with the stated normalizations. No source from differentiating
the residual is missing.

For the nonlinear estimate, let $V$ be the linear response and $U$ the
unknown remainder. The linear coordinate bounds yield

\[
\|\alpha_V^2\|_2\le n^{1/100-1/5},\quad
\|\alpha_V\odot\alpha_U\|_2\le Cn^{-1/5}\|U\|,
\quad \|\alpha_U^2\|_2\le C\|U\|^2.
\]

The same estimates apply to the linear top preactivation and readout.
Expanding successively the first features, top preactivation, top response,
and lower carrier gives the source's $C(R+P)$ remainders, where

\[
R=n^{1/100-1/5}+n^{-1/5}\|U\|+\|U\|^2,
\qquad P=n^{-1/2}(n^{2/100}+n^{1/100}\|U\|+\|U\|^2).
\]

Matrix-variation cross products carry $n^{-1/2}$ because the physical
matrix variation is $\Delta H/\sqrt n$. The changed first gate times
changed carrier is controlled using the supplied infinity bounds for both
linear quantities; the unknown remainder is used only in Euclidean norm.
This avoids assuming the very delocalization being proved.

The scalar prediction remainder uses the extended Hessian in
$(\Theta,e)$. Its operator bound $C(1+M_n)$ on the joining segment is
justified by the preceding carrier expansion, which places that segment's
carriers within $o(1)$ of the reference and its small linear variation.
Thus this segment bound is not an assumed second nonlinear stability result.
Multiplying by the adaptive residual and expanding its own variation gives
precisely a residual-weighted $R$ term and an unweighted $P$ term.

After propagation by $n^{1/400}$, integration over $T_n=O(\log n)$,
and multiplication by $1+M_n=O(\log n)$, the largest powers are
$n^{-19/100+1/400}$ and $n^{-1/5+1/400}$. They are both
$o(n^{-1/10})$. The bootstrap for the Euclidean remainder closes with a
strict margin. The adaptive small source of norm $O(n^{-1/2})$ gives an
even smaller integrated contribution. The bounded remainder and linear
response also provide the finite-state bounds needed for continuation through
the reference interval.

Conditional on retained initialization and a fixed scalar control, every
linear coordinate is Gaussian with variance $O(n^{-1+1/100})$. At
threshold $n^{-1/5}$, its failure exponent is $n^{59/100}$.
The corresponding centered quadratic form has the same exponent from the
source's finite Gaussian-square moment-generating-function calculation.
The uniform scalar-control net has log cardinality
$O_r(n^{3/10}(\log n)^3)$, which is strictly smaller. Its uniform
approximation error is $O(n^{-3/10+1/400}\log n)=o(n^{-1/5})$.
Polynomial terminal-time nets add only $O(\log n)$ to the log
cardinality. This verifies the claimed exponential failure scale after
weakening its exponent to $2/5$.

Finally, the trace estimate does not require a missing columnwise weighted
Stein bound. The previously checked normalized Schatten estimate controls
$J-U_0$ by $CS+CS^2\sqrt B$ on each reference subinterval. Composing
with the bounded top-response derivative and $Q_a$, then integrating
its residual factor, gives $CS+CS^3\sqrt B$. The direct external gate
derivative costs $CS$. The adaptive $P_a$ contribution is rank one,
so its normalized trace costs only $CS n^{-1+1/400}T_n=o(1)$.
These facts reconstruct the singleton shift required in (1).

No local algebraic error was found in this strengthened insertion proof.
Together with Sections 2--8, this gives an end-to-end internal reconstruction
for positive-Gram data.


## 10. Weighted compatible quotient and final scope

The final source's Section 10 replaces uniform sample weights by fixed
positive weights $p_a$ summing to one. Its weighted formulas
\[
F=-2\sum_a p_ar_a\nabla\mathcal F_a,\qquad
L=\sqrt{2/n}[\sqrt{p_a}\nabla\mathcal F_a]_a,\qquad
P_a=-\frac{2p_a}{n}\nabla\mathcal F_a\delta_a^\top,\qquad
Q_a=-2p_ar_aB_a^\top
\]
retain the exact negative Gram, rank-one adaptive source, and residual
source used throughout the proof. Weighted Cauchy--Schwarz gives
$2\sum_a p_a|r_a|\le2\rho$; individual residual bounds cost only the fixed
smallest weight. Hence the fitting, activity, trace, Gaussian, and defect
arguments extend with constants depending on these weights.

For normalized inputs, equality up to sign partitions the data into classes.
Odd forward features and even gates give $h_a=s_a h_j$ and
$\delta_a=\delta_j$ within a class. Compatible labels satisfy
$y_a=s_a\bar y_j$, so summing updates and signed backward moments gives the
exact weighted quotient with $p_j=|I_j|/m$. Its residual RMS is exactly the
original RMS. Thus the original learning clock and both compared physical
trajectories are preserved, including their initialization.

The quotient representatives are pairwise nonproportional. The complete
positivity proof in the authorized DATA_QUOTIENT_CLOCK.md and its check
rules out a null Gaussian tanh feature combination by finite differences
and nonpolynomiality; the next tanh layer preserves positivity by Gaussian
full support. Positive weights preserve the gap. The initialized Gram
condition is therefore automatic for each fixed compatible sphere dataset.
Its size and the allowed label threshold remain geometry dependent.

The final source also explicitly fixes nonzero labels before the width
limit. It does not claim a width threshold uniform as $Y\downarrow0$.
The pathwise clarification for an adaptive small source does not assert
well-posedness for arbitrary feedback rules: the application uses the
already existing full dense solution, so its source is continuous and the
comparison applies. Both qualifications are appropriate.

The complete claim is internally checked in this precise scope. No
unconditional expectation bound over all unstopped fitting trajectories,
arbitrary-depth extension, inconsistent-label extension, or numerical
dense-to-population rate is inferred. No maintained manuscript or book
material was promoted by this check.
