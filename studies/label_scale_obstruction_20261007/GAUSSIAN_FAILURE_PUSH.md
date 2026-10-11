# Nonlinear obstruction to an ordered saturation escape

2026-10-11. Scoped theoretical continuation. Scientific inputs were the
supervisor's prompt, `docs/notation.qmd`, and the complete
`GLOBAL_FAILURE_ALTERNATIVES.md`, `TANH_BAD_BASIN.md`, and, after explicit
scope expansion, `GAUSSIAN_TRAPPING_RENEWAL.md`. Required research, proof,
and canonical-notation instructions were applied. No experiment or Git
operation was performed. This is an internally derived contribution, not
promoted material.

**Outcome.** The requested Gaussian failure theorem remains open. There is
a new obstruction to the most direct saturation mechanism: an ordered pair
of positive top neurons cannot both undergo monotone escape with bounded
readouts when the sample residuals have one sign change in their common
first-layer feature. The obstruction is nonlinear and permits the first
layer and the residuals to evolve arbitrarily subject to its stated sign
condition. A preceding elementary inequality also supplies, without any
joint asymptotic expansion, the coefficient bound left conditional in the
earlier transverse linear test. Neither result excludes a nonsymmetric
escape with sign changes, unbounded readouts, or a different feature geometry.

## 1. Model, target, and the invariant family being tested

Let the fixed inputs be unit vectors
\(x_a\in\mathbb R^d\), \(1\le a\le m\), with no parallel or antiparallel
pair, and let \(X=[x_1,\ldots,x_m]\). For fixed width \(n\), the actual
network and loss are

\[
\begin{aligned}
A&\in\mathbb R^{n\times d},&W&\in\mathbb R^{n\times n},&w&\in\mathbb R^n,\\
U&=\tanh(AX),&H&=\tanh(WU),&f&=H^\top w/n,\\
r&=f-y,&\mathcal L&=\|r\|_2^2/m.
\end{aligned}
\]

The nonlinearities act entrywise. Physical gradient flow has mobilities
\((n,1,n)\). Initialization is independent
\(A_{jk}(0)\sim N(0,1)\), \(W_{ij}(0)\sim N(0,1/n)\), and exactly
\(w(0)=0\). The target remains fixed admissible \(X,y\), and constants
\(c,p>0\), independent of width and draw, such that

\[
\liminf_{n\to\infty}
\Pr\!\left\{\lim_{t\to\infty}\mathcal L_n(t)\ge c\right\}\ge p.
\tag{1}
\]

The time limit in (1) precedes the width limit. The theorems below are
deterministic statements at each fixed width. They do not prove (1), and
their hypotheses are not claimed to hold on a Gaussian event of positive
probability.

We test the exact invariant family

\[
A_{j:}=p^\top\quad(1\le j\le n),\qquad
W_{ij}=q_i/n,\qquad w_i=v_i,
\tag{2}
\]

where \(p\in\mathbb R^d\) and \(q_i,v_i\in\mathbb R\) evolve. Define

\[
u_a=\tanh(p^\top x_a),\qquad
f_a=\frac1n\sum_i v_i\tanh(q_i u_a),\qquad r_a=f_a-y_a.
\]

For a real auxiliary argument \(q\), define the time-dependent scalar
function

\[
F_t(q)=-\frac2m\sum_a r_a(t)\tanh(q u_a(t)),\qquad
E_t(q)=\partial_qF_t(q)
      =-\frac2m\sum_a r_a(t)u_a(t)\operatorname{sech}^2(q u_a(t)).
\tag{3}
\]

In derivatives with respect to this auxiliary \(q\), current \(r_a(t)\)
and \(u_a(t)\) are held fixed. Thus \(E_t\) is a derivative of the
current function in (3), not its physical time derivative. The exact
restricted dynamics are

\[
\begin{aligned}
\dot v_i&=F_t(q_i),\qquad \dot q_i=v_i E_t(q_i),\\
\dot p&=-\frac{2}{mn}\sum_{i,a}
 v_iq_i r_a\operatorname{sech}^2(q_i u_a)
 \operatorname{sech}^2(p^\top x_a)x_a.
\end{aligned}
\tag{4}
\]

To check both invariance and the factors, the full middle-weight equation
is

\[
\dot W_{ij}=-\frac{2w_i}{mn}\sum_a
 r_a\operatorname{sech}^2((WU)_{ia})U_{ja}.
\]

Substitution of (2) makes it independent of \(j\), and multiplication
by \(n\) gives \(\dot q_i\) in (4). Substitution into the first-weight
equation makes every first-weight row velocity equal, yielding the stated
\(\dot p\). The readout equation is \(\dot w=-2Hr/m\).
Consequently (4) includes actual training of both hidden layers. This
family itself has first-layer rank one and is Gaussian-null when there
is more than one first-layer row. It is used to test an escape mechanism,
not as a Gaussian initialization construction.

## 2. A residual sign condition controls the derivative ratio

Here is the pointwise hypothesis needed below. At a given time all
\(u_a\) lie in \((0,1]\), and there is a number \(u_*\in[0,1]\) with

\[
u_a<u_*\ \Longrightarrow\ r_a\le0,\qquad
u_a>u_*\ \Longrightarrow\ r_a\ge0.
\tag{5}
\]

Residuals of either sign are allowed at equality \(u_a=u_*\). Thus all
negative residuals occur at feature values no larger than those carrying
positive residuals. The cases in which all residuals have one sign are
included by choosing \(u_*=0\) or \(u_*=1\).

**Lemma 1.** Fix any values satisfying (5), and use (3) to define
\(E(q)\). If \(q_0>0\) and \(E(q_0)>0\), then for every \(q\ge q_0\),

\[
E(q)>0,\qquad
\frac{E'(q)}{E(q)}\ge-2,
\qquad
E(q)\ge e^{-2(q-q_0)}E(q_0).
\tag{6}
\]

In particular,

\[
F(q)-F(q_0)=\int_{q_0}^qE(s)\,ds
\ge\frac{E(q_0)}2\bigl(1-e^{-2(q-q_0)}\bigr).
\tag{7}
\]

**Proof.** For \(u>0\), put
\(k_q(u)=u\operatorname{sech}^2(qu)>0\). Its logarithmic derivative
with respect to \(q\) is

\[
\ell_q(u)=\frac{\partial_q k_q(u)}{k_q(u)}
        =-2u\tanh(qu).
\]

For fixed \(q>0\), the function \(u\mapsto\ell_q(u)\) is decreasing:
its derivative is
\(-2\tanh(qu)-2qu\operatorname{sech}^2(qu)<0\). Also
\(-2\le\ell_q(u)\le0\) for \(0\le u\le1\).
Write

\[
P(q)=\frac2m\sum_{r_a<0}(-r_a)k_q(u_a),\qquad
N(q)=\frac2m\sum_{r_a>0}r_a k_q(u_a),\qquad E=P-N.
\]

Every term in \(P\) has \(u_a\le u_*\), and every term in \(N\)
has \(u_a\ge u_*\). Therefore

\[
E'(q)
=\frac2m\sum_{r_a<0}(-r_a)k_q(u_a)\ell_q(u_a)
 -\frac2m\sum_{r_a>0}r_a k_q(u_a)\ell_q(u_a)
\ge\ell_q(u_*)\,[P(q)-N(q)].
\tag{8}
\]

Where \(E(q)>0\), (8) implies \(E'(q)\ge-2E(q)\). On the connected
interval of positivity starting at \(q_0\), integration gives the last
bound in (6). That interval cannot have a finite right endpoint: continuity
and this positive lower bound would give a positive value at such an
endpoint. Hence it extends to infinity. Integrating the lower bound for
\(E\) proves (7). This argument concerns a fixed time and does not
differentiate the residuals or the first-layer features. \(\square\)

The sign hypothesis is preserved in a useful geometric setting. Suppose
the samples can be ordered so that \(u_1\le\cdots\le u_m\), while
the labels satisfy \(y_1\ge\cdots\ge y_m\). If all \(q_i,v_i>0\),
then \(u\mapsto n^{-1}\sum_i v_i\tanh(q_i u)\) is increasing.
Consequently \(r_1\le\cdots\le r_m\), which gives (5), including
ties. In the existing paired-sphere construction, \(p\) is along the
first coordinate, \(u_a=\tanh(p_1s_a)\) with \(p_1>0\), and the
labels are decreasing with the positive coordinates \(s_a\). That
construction is a special case.

## 3. The earlier linear coefficient condition is automatic here

Along a symmetric trajectory of (4), write \(q_i=q\), \(v_i=v>0\).
A top-neuron perturbation with zero mean across neurons has scalar
coordinates \((\xi,\zeta)\), for the perturbations of \(q_i,v_i\),
and satisfies

\[
\dot\xi=v E_t'(q)\xi+E_t(q)\zeta,
\qquad \dot\zeta=E_t(q)\xi.
\tag{9}
\]

The shared predictions and the first-weight velocity have zero first
variation in this direction, so the current residual and \(p\) do not
add terms to (9). More explicitly, take fixed coefficients \(\eta_i\)
with \(\sum_i\eta_i=0\), and set
\(\delta q_i=\eta_i\xi\), \(\delta v_i=\eta_i\zeta\), \(\delta p=0\).
Every first variation of an average over neurons is a constant times
\(\sum_i\eta_i\), hence vanishes. Differentiation of the two top
equations in (4) then gives (9).

Suppose on a tail that (5) holds,

\[
\dot q>0,\qquad q(t)\longrightarrow\infty,
\qquad 0<v(t)\le V<\infty.
\tag{10}
\]

Because \(\dot q=vE_t(q)\), (10) gives \(E_t(q)>0\). Reparametrizing
(9) by the increasing coordinate \(q\), and applying Lemma 1, gives

\[
\frac{d\xi}{dq}=\frac{E_t'(q)}{E_t(q)}\xi+\frac\zeta v,
\qquad
\frac{d\zeta}{dq}=\frac\xi v,
\qquad \frac{E_t'(q)}{E_t(q)}\ge-2.
\tag{11}
\]

For initial \(\xi,\zeta>0\), both remain positive. Define
\(M_0=\left(\begin{smallmatrix}-2&1/V\\1/V&0\end{smallmatrix}\right)\).
Componentwise (11) is bounded below by multiplication by \(M_0\).
Its positive eigenvalue is

\[
\lambda_+=\sqrt{1+V^{-2}}-1>0,
\]

and \(l=(1,(V\lambda_+)^{-1})^\top\) is a positive left eigenvector.
Thus

\[
\frac d{dq}(l_1\xi+l_2\zeta)
\ge\lambda_+(l_1\xi+l_2\zeta),
\]

which proves exponential growth of this weighted perturbation as a
function of \(q\). In the notation of the earlier renewal note,
\(E_t=-2b_r/m\) and \(E_t'=-2a_r/m\), so this proves its missing
ratio bound \(a_r/b_r\ge-2\) in the present residual-ordering class.
It needs no approximation \(v\approx v_*\), no comparison of the
escape rates of the two hidden layers, and no exchange of limits.
The other assumptions in (10) remain actual assumptions about the
trajectory; this section does not establish them for every scalar escape.

## 4. A nonlinear obstruction for two unequal top neurons

The following theorem uses the exact equations, not their linearization.
It also permits unequal neuron coordinates throughout the argument.

**Theorem 2.** Consider a trajectory of (4) on \([t_0,\infty)\). Suppose
the sign condition (5) holds at every time in that interval. Let \(i,j\)
be two top neurons with

\[
q_i(t_0)\ge q_j(t_0)>0,
\qquad v_i(t_0)\ge v_j(t_0)>0,
\tag{12}
\]

and at least one strict inequality. The following three conditions cannot
all hold:

\[
0<v_i(t),v_j(t)\le V<\infty,\qquad
E_t(q_j(t))>0,\qquad q_j(t)\longrightarrow\infty.
\tag{13}
\]

Thus two top neurons ordered in both their positive weight and their
positive readout cannot both continue this monotone saturation mechanism
with bounded readouts. No bound on \(\dot p\), no convergence assumption
on \(p\) or \(r\), and no width-dependent constant is required.

**Proof.** Suppose all conditions in (13) hold, and define

\[
\eta=q_i-q_j,\qquad \zeta=v_i-v_j.
\]

At any current time, Lemma 1 gives \(E_t(q)>0\) for every
\(q\ge q_j\). The region \(\eta,\zeta\ge0\) is forward invariant.
Indeed, on its face \(\eta=0\), (4) gives
\(\dot\eta=\zeta E_t(q_j)\ge0\). On its face \(\zeta=0\),
(7) gives
\(\dot\zeta=F_t(q_i)-F_t(q_j)\ge0\). The vector field is smooth,
so these inward-pointing inequalities imply invariance: on each compact
time interval, a Lipschitz bound and Gronwall applied to the negative
parts of the two coordinates exclude a first crossing.

Since \(v_jE_t(q_j)>0\), the coordinate \(q_j\) is strictly increasing
and can serve as the independent variable. The equations and Lemma 1 give

\[
\begin{aligned}
\frac{d\zeta}{dq_j}
&=\frac{F_t(q_i)-F_t(q_j)}{v_jE_t(q_j)}
 \ge\frac{1-e^{-2\eta}}{2v_j}
 \ge\frac{1-e^{-2\eta}}{2V},\\
\frac{d\eta}{dq_j}
&=\frac{v_iE_t(q_i)-v_jE_t(q_j)}{v_jE_t(q_j)}
 \ge\left(1+\frac\zeta{v_j}\right)e^{-2\eta}-1
 \ge\left(1+\frac\zeta V\right)e^{-2\eta}-1.
\end{aligned}
\tag{14}
\]

In particular \(\zeta\) is nondecreasing. If its initial value is
strictly positive, choose a smaller number \(\zeta_*>0\). Otherwise
\(\eta(t_0)>0\), and the first inequality in (14) makes \(\zeta\)
strictly positive after a short interval. In either case there is a
time \(t_1\ge t_0\) and a number \(\zeta_*>0\) with
\(\zeta(t)\ge\zeta_*\) for all \(t\ge t_1\).

Set

\[
\eta_* =\frac14\log(1+\zeta_*/V)>0,
\qquad \kappa=\sqrt{1+\zeta_*/V}-1>0.
\]

Whenever \(0\le\eta\le\eta_*\), the second inequality in (14)
implies \(d\eta/dq_j\ge\kappa\). Since \(q_j\to\infty\),
\(\eta\) must reach \(\eta_*\) in finite \(q_j\)-distance if it is
initially below it. At that boundary its derivative remains at least
\(\kappa\), so it cannot cross back downward. Thus for all sufficiently
large \(q_j\), the first inequality in (14) gives

\[
\frac{d\zeta}{dq_j}\ge
\frac{1-e^{-2\eta_*}}{2V}>0.
\]

Integration to \(q_j=\infty\) forces \(\zeta\to\infty\), contradicting
\(0<v_i,v_j\le V\). \(\square\)

This proof supplies a finite quantitative escape from any proposed
bounded-readout region. Once \(\zeta\ge\zeta_*\), reaching
\(\eta\ge\eta_*\) requires at most \(\eta_*/\kappa\) additional
\(q_j\)-distance if starting below the threshold. Thereafter the readout
difference exceeds \(V\) in at most
\(2V^2/(1-e^{-2\eta_*})\) further \(q_j\)-distance. The constants
depend on the specified perturbation and readout bound, not on width.

## 5. Consequences for the existing escape and for Gaussian capture

For the two effective sample types in the existing paired-sphere example,
write \(0<u_1<u_2<1\), \(y_1=\alpha>\beta=y_2>0\). If all top
\(q_i,v_i>0\), the predictions satisfy \(f_1<f_2\), and hence
\(r_1<r_2\). Condition (5) follows. Multiplicities of the two sample
types only multiply their terms by positive integers and do not change
Lemma 1 or Theorem 2.

The exactly replicated scalar escape has all \((q_i,v_i)\) identical,
so it does not satisfy the strict part of (12) and is not contradicted.
But an arbitrarily small perturbation that increases both coordinates of
one top neuron relative to another creates the forbidden ordered pair.
If that perturbed trajectory continues to satisfy (5), keeps both
readouts positive and bounded, and sends the smaller top weight
monotonically to infinity, Theorem 2 gives a contradiction. Thus this
class of escape has no open trapping neighborhood within the invariant
family (2) when all of those properties are required of every trajectory
in the neighborhood. Any full-network open trapping neighborhood with
those same properties would restrict to such a neighborhood in (2), so
that stronger assertion is also excluded.

More generally, at any starting time for an escape satisfying (5),
positive bounded readouts, and increasing unbounded top coordinates for
every neuron, no pair may be strictly ordered in both coordinates.
Sorting distinct \(q_i\)'s must therefore place the \(v_i\)'s in strict
reverse order. This is a necessary condition, not an exclusion theorem:
the reverse-order region is open and can have positive probability.
Nor does eventual departure from the positive-readout region imply
fitting. A readout can change sign, a top weight can cease to be monotone,
or a different escape can emerge.

For an actual all-positive saturation escape, boundedness of the individual
readouts follows from the loss and need not be separately assumed.
Here is the precise specialization.

**Corollary 3.** Suppose on a tail that all \(q_k,v_k>0\), all
\(u_a>0\), and (5) holds. Suppose two neurons satisfy the strict ordering
(12) at the beginning of this tail, \(E_t(q_j)>0\) throughout it, and,
for some fixed sample \(a_0\),

\[
q_j(t)\longrightarrow\infty,\qquad
q_j(t)u_{a_0}(t)\longrightarrow\infty.
\tag{15}
\]

Then these hypotheses are inconsistent with the actual gradient flow.

**Proof.** Loss decreases, so at every time

\[
0\le f_{a_0}(t)\le
|y_{a_0}|+\sqrt{m\mathcal L(0)}=:B<\infty.
\]

All terms in its defining readout sum are nonnegative. The pair ordering
is preserved as proved in Theorem 2, so \(q_i\ge q_j\). By (15),
both \(\tanh(q_i u_{a_0})\) and \(\tanh(q_j u_{a_0})\) are at least
\(1/2\) for all sufficiently large times. Thus

\[
v_i(t),v_j(t)\le2nB
\]

on that tail. They are also bounded on its preceding compact interval
by smooth finite-time existence. A finite bound \(V\) in Theorem 2
therefore exists, giving the contradiction. The bound may depend on the
fixed width, which is sufficient for this deterministic argument.
\(\square\)

In particular, the unbounded-readout alternative cannot rescue an escape
that retains nonnegative contributions from every neuron and actually
saturates these two neurons on a common sample. Cancellation or departure
from the other hypotheses is necessary. The corollary does not give a
uniform-in-width rate.

The result is independent of Gaussian initialization and does not justify
a probability estimate for (1). In particular:

- A Gaussian feature cloud is not represented by the rank-one family
  (2). No post-training independence or Gaussian law has been assumed.
- A statement about linear instability or escape from the bounded positive
  region cannot be converted into zero probability of all bad limiting
  behavior without a separate basin argument.
- The sign-adapted finite bad endpoints in the preceding renewal note are
  unaffected. Their actual Gaussian capture remains unresolved.
- There is no new unconditional fitting or parameter-boundedness theorem
  here. In particular, bounded predictions do not bound individual
  readouts when cancellation is possible.

The main remaining negative obligation is a bad basin that survives these
corrective top-neuron directions and is reached from the full Gaussian
hidden initialization with probability bounded below as width grows.
The present calculation rules out a concrete monotone, bounded,
positive-readout saturation mechanism after an ordered split. It does
not supply or rule out the required nonsymmetric replacement.

| Claim | Status |
|---|---|
| Residual ordering implies the lower derivative-ratio bound | Proved by Lemma 1, at every finite state satisfying (5). |
| Conditional linear amplification about the replicated escape | Proved with explicit exponent under (10); the former ratio hypothesis is now discharged in this class. |
| Ordered, unequal positive top neurons can jointly escape monotonically with bounded readouts | Ruled out by Theorem 2 under (5). |
| Such an escape can evade the bound through unbounded positive readouts while all neuron contributions stay nonnegative | Ruled out by loss monotonicity and Corollary 3 under (15). |
| Every trajectory near the replicated escape fits | Not established. |
| A nonsymmetric saturation escape with nonvanishing Gaussian basin mass | Open. |
| Gaussian capture of the sign-adapted finite minima | Open. |
| Fixed-label, time-first Gaussian failure target (1) | Open. |
