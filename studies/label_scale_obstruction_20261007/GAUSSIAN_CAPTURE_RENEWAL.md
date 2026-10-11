# Renewed Gaussian-capture route: a quantitative constant-feature witness

Status: new internally derived partial positive result, not independently
reviewed. No canonical-Gaussian macroscopic nonfitting theorem is proved.
The new result below supplies a width-uniform finite-time Gaussian
probability bridge that was absent from the earlier cosine-activation
discussion. It excludes the proposed all-nonnegative-readout mechanism
under its stated residual condition; it does not exclude eventual bad
capture after readouts change sign.

This is a reused-context continuation. Scientific inputs were the prompt,
the complete GAUSSIAN_NEGATIVE_MASS.md, UNCONDITIONAL_NEGATIVE_ROUTE.md,
and TWO_LAYER_PERSISTENCE.md, and the already-read maintained Gaussian
program construction in docs/12-three-sample-learning.qmd, III.F.1–11.
No other study, new peer draft, experiment, or Git operation was used.
The later unaudited saddle-avoidance claim is not a dependency.

## 1. Exact scope and the result

The primary requested model has tanh in both hidden layers. The theorem
in this note instead uses a **linear first activation** and a bounded
second activation $\phi$ satisfying

$$
\phi\in C^2(\mathbb R),\qquad
\|\phi\|_\infty+\|\phi'\|_\infty+\|\phi''\|_\infty<\infty,\qquad
\phi'(0)=0.
\tag{1}
$$

Set $c=\phi(0)$. The relevant analytic example is
$\phi(z)=(3+\cos z)/2$, with $c=2$.
No assertion below silently transfers to tanh/tanh.

For fixed unit inputs $X=[x_1,\ldots,x_m]\in\mathbb R^{d\times m}$,
fixed labels $y\in\mathbb R^m$, and width $n$, write

$$
U=AX,\qquad Z=WU,\qquad H=\phi(Z),\qquad
f=H^\top w/n,\qquad r=f-y,\qquad
\mathcal L=\|r\|_2^2/m.
\tag{2}
$$

The mobilities are $(n,1,n)$, and the initialization is exactly
$A_{ij}(0)\sim N(0,1)$,
$W_{ij}(0)\sim N(0,1/n)$ independently, with $w(0)=0$.
Let

$$
\Omega_n(t)=-\frac{2c}{m}\int_0^t\mathbf1^\top r_n(s)\,ds.
\tag{3}
$$

This is the readout a hypothetical neuron with constant feature vector
$c\mathbf1$ would acquire under the actual residual history.

**Finite-time witness theorem.** For every fixed $T<\infty$ and
$\delta>0$, there is $p=p(T,\delta,X,y,\phi)>0$, independent of width,
such that for each fixed top-neuron index $j$,

$$
\liminf_{n\to\infty}
\Pr\!\left\{
 \sup_{t\le T}\max_a|Z_{ja}(t)|<\delta,\quad
 \sup_{t\le T}|w_j(t)-\Omega_n(t)|<\delta
\right\}\ge p.
\tag{4}
$$

Here the index can be chosen, for example, as $j=1$ at every width.
Exchangeability makes the bound identical for all top indices.

The finite-time Gaussian-program limit exists for (2). Denote its
deterministic prediction path by $f_\infty(t)$ and define

$$
\Omega_\infty(t)=\frac{2c}{m}
 \int_0^t\mathbf1^\top(y-f_\infty(s))\,ds.
\tag{5}
$$

For every fixed $T,\delta$, there is $p_*>0$ such that

$$
\Pr\!\left\{
\frac1n\#\left\{j:
 \max_a|Z_{ja}(T)|<\delta,\quad
 |w_j(T)-\Omega_\infty(T)|<\delta
\right\}\ge p_*
\right\}\longrightarrow1.
\tag{6}
$$

Only the endpoint cohort is asserted with high probability in (6).
Equation (4) is the single-neuron pathwise statement. No uniformity as
$T\to\infty$ is claimed for either $p$ or $p_*$.

**Consequence.** If $\Omega_\infty(T)<0$ at some finite deterministic
time, a positive fraction of actual finite-width readouts is strictly
negative at that time with probability tending to one. A claimed
nonnegative-readout invariant is therefore false in this situation.

This is stronger than qualitative full support: the cohort fraction is
bounded below by a fixed positive number independent of width.

## 2. Width-independent finite-horizon bounds

Put $\Gamma=X^\top X$ and
$b_a=w\odot\phi'(Z_{:a})$. The exact closed equations for $U,W,w$ are

$$
\dot U=-\frac2m W^\top[b_1,\ldots,b_m]
                 \operatorname{diag}(r)\Gamma,\qquad
\dot W=-\frac2{mn}\sum_a r_ab_au_a^\top,\qquad
\dot w=-\frac2m Hr.
\tag{7}
$$

Because the first activation is linear, there is no bottom gate.
The original parameter gradient flow gives
$\|r(t)\|_2\le\|y\|_2$. Bounded $\phi$ therefore yields
$\|w(t)\|_\infty\le C t$.
On each fixed horizon,

$$
\frac{\|\dot U\|_F}{\sqrt n}\le C_T\|W\|_{\mathrm{op}},
\qquad
\|\dot W\|_F\le C_T\frac{\|U\|_F}{\sqrt n}.
\tag{8}
$$

Thus bounds on the initial normalized root norm and initialized action
give deterministic bounds on

$$
\sup_{t\le T}
\left(
\frac{\|U(t)\|_F}{\sqrt n}
+\frac{\|\dot U(t)\|_F}{\sqrt n}
+\|W(t)\|_{\mathrm{op}}+\|w(t)\|_\infty
\right).
\tag{9}
$$

The constants are independent of width. A scalar Gronwall estimate
applied to $\|U\|_F/\sqrt n+\|W\|_{\mathrm{op}}$ suffices.
These bounds also imply global finite-time existence. They remain
valid when one specified top neuron is removed from the output and
its own updates are disabled; that system is the gradient flow of its
restricted loss.

For two states in such bounds, use the distance

$$
D=\frac{\|U-\widetilde U\|_F}{\sqrt n}
+\|W-\widetilde W\|_F
+\frac{\|w-\widetilde w\|_2}{\sqrt n}.
\tag{10}
$$

The right side of (7) is Lipschitz in this distance, with constant
$C_T$ independent of width. In particular, for each sample,

$$
\|b_a-\widetilde b_a\|_{2,n}
\le \|\phi'\|_\infty\|w-\widetilde w\|_{2,n}
 +\|\widetilde w\|_\infty\|\phi''\|_\infty
   \|Z_{:a}-\widetilde Z_{:a}\|_{2,n}.
\tag{11}
$$

Forward action differences and rank-one update differences give all
remaining bounds. Only the reference readout multiplies the gate
difference. One can equivalently clip the readout in $b_a$ above the
known horizon bound to obtain a locally Lipschitz field on an open
normalized Hilbert-space neighborhood.

## 3. Uniform Gaussian-process small balls

The following elementary fact is the probabilistic input.

**Lemma.** Let $G_n(t)\in\mathbb R^m$, $0\le t\le T$, be centered
continuous Gaussian processes, with

$$
\mathbb E|G_{n,a}(0)|^2\le M^2,\qquad
\mathbb E|G_{n,a}(t)-G_{n,a}(s)|^2\le L^2|t-s|^2.
\tag{12}
$$

For every $\varepsilon>0$, there is $p_0>0$, depending only on
$m,T,M,L,\varepsilon$, such that

$$
\Pr\{\sup_{t\le T}\max_a|G_{n,a}(t)|<\varepsilon\}\ge p_0
\tag{13}
$$

for every member of the family. Degenerate Gaussian covariances are
allowed.

**Proof.** Gaussian tails and a union bound over dyadic increments give

$$
\Pr\!\left\{
\max_{a,k}|G_{n,a}((k+1)T2^{-\ell})
             -G_{n,a}(kT2^{-\ell})|
 >K2^{-\ell/2}
\right\}
\le 2m\,2^\ell
 \exp\!\left(-\frac{K^2\,2^\ell}{2L^2T^2}\right).
\tag{14}
$$

If $L=0$, the process is constant and that part of the argument is
unnecessary. Choose $K$ large enough that the sum of the right sides
and the probability of $|G_n(0)|_\infty>K$ are at most $1/2$.
Dyadic chaining then gives a common bound and a common $1/2$-Hölder
modulus on an event of probability at least $1/2$.
Continuous functions with those bounds have a finite uniform
$\varepsilon/4$-net: choose a sufficiently fine time grid, quantize
values on the grid, and use the common modulus between grid points.
Let the size of such a net be $N$.

For each Gaussian law, one ball in this net has probability at least
$1/(2N)$. Two independent copies $G_n,G_n'$ lie in that same ball with
probability at least $1/(4N^2)$, and their difference then has supremum
less than $\varepsilon/2$. Since
$(G_n-G_n')/\sqrt2$ has the same law as $G_n$, (13) follows, with a
strictly smaller ball than required. This proof uses neither a
nonsingular covariance matrix nor a dimension-dependent Gaussian
density lower bound. $\square$

## 4. One-row cavity and the self-interaction estimate

Fix a top index $j$ and write $q=W_{j,:}(0)$.
Remove this row's contribution from the output, keep its readout
identically zero, and keep its middle row zero. Let
$(V,\widetilde W,\widetilde w)$ be the resulting cavity state;
the $j$th rows/coordinates of $\widetilde W,\widetilde w$ are zero.
Its residual is $r^{\mathrm{cav}}$.

Condition on $A(0)$ and every initialized middle row other than $q$.
The whole cavity trajectory is now fixed, and
$q\sim N(0,I_n/n)$ remains independent of it.
On the event that its initial normalized root norm and remaining
initialized action are bounded, (9) holds for this trajectory.
Consequently

$$
G_a(t)=qV_{:a}(t)
$$

is a centered Gaussian process satisfying (12), with constants
independent of width and of the conditioned cavity trajectory.
The lemma gives a common lower bound for
$\sup_{a,t}|qV_{:a}(t)|<\varepsilon$.

We also require $\|q\|_2\le2$. Its Gaussian failure probability tends
to zero independently of the cavity state, so this requirement only
reduces the small-ball lower bound by $o(1)$.
The good initial cavity norm event has probability tending to one
by the root law of large numbers and the Gaussian action-norm bound.

To estimate the actual effect of the row, define an augmented reference

$$
\overline U=V,\qquad
\overline W=\widetilde W+e_jq,\qquad
\overline w=\widetilde w+\omega e_j,\qquad
\omega(t)=-\frac{2c}{m}\int_0^t
                    \mathbf1^\top r^{\mathrm{cav}}(s)\,ds.
\tag{15}
$$

Its initial state agrees exactly with the full initialized state.
Its prediction differs from the cavity prediction by
$\omega\,\phi(qV)/n$, which is $O_T(1/n)$.
On the Gaussian small-ball event,

$$
|\phi'(qV_{:a})|\le\|\phi''\|_\infty\varepsilon,\qquad
|\phi(qV_{:a})-c|\le\|\phi'\|_\infty\varepsilon.
\tag{16}
$$

Evaluate the full vector field (7) at the augmented reference and
subtract its prescribed velocity. There are only two kinds of defects:

1. Its additional prediction changes the coefficients by $O_T(1/n)$.
   In the distance (10), this contributes $O_T(1/n)$.
2. The test row has backward coefficients
   $\omega\phi'(qV_{:a})=O_T(\varepsilon)$.
   Its missing contribution to $\dot U$ has normalized norm
   $O_T(\varepsilon/\sqrt n)$ because $\|q\|_2\le2$.
   Its middle-row update has Frobenius norm
   $O_T(\varepsilon/\sqrt n)$ because
   $\|V_{:a}\|_2=O_T(\sqrt n)$ and the update has denominator $n$.
   Its readout defect is $O_T(\varepsilon)$ in one coordinate,
   hence $O_T(\varepsilon/\sqrt n)$ in normalized norm.

Thus the total defect is at most
$C_T(\varepsilon/\sqrt n+1/n)$.
All actual and augmented-reference states have the bounds needed for
(11), so Gronwall yields

$$
\sup_{t\le T}D(t)
\le C_T\left(\frac{\varepsilon}{\sqrt n}+\frac1n\right).
\tag{17}
$$

This does **not** make the row's own preactivation error automatically
$O(n^{-1/2})$. Its pointwise estimate is instead

$$
\begin{aligned}
|Z_{ja}-qV_{:a}|
&\le\|(W-\overline W)_{j,:}\|_2\|U_{:a}\|_2
    +\|q\|_2\|U_{:a}-V_{:a}\|_2\\
&\le C_T\sqrt n\,D,
\\
|w_j-\omega|&\le\sqrt n\,D.
\end{aligned}
\tag{18}
$$

Combining (17)–(18) gives $O_T(\varepsilon+n^{-1/2})$ self-errors.
The factor $\sqrt n$ is retained. The suppression by $\phi'(0)=0$,
not a false vanishing-self-interaction claim, allows $\varepsilon$
to be selected afterward.

Prediction differences between the actual and cavity trajectories are
bounded by $C_TD+C_T/n$. Hence

$$
\sup_{t\le T}|\omega(t)-\Omega_n(t)|
\le C_T\left(\frac{\varepsilon}{\sqrt n}+\frac1n\right).
\tag{19}
$$

For prescribed $\delta$, choose a fixed sufficiently small
$\varepsilon>0$, then take width large. Equations (13), (17)–(19)
prove (4).

## 5. Why the witness becomes a positive fraction

Here the finite-horizon limit is needed, not an independence assumption
for trained neurons.

For this linear-first-activation model the strong population state is

$$
L^2(\Omega_1)^m
\times\bigl(W_0+\mathcal S_2(L^2(\Omega_1),L^2(\Omega_2))\bigr)
\times L^2(\Omega_2).
$$

The root tuple $U(0)$ is Gaussian with covariance $\Gamma$, iid across
first-layer neurons and independent of the initialized middle action.
Singular $\Gamma$ is allowed. The maintained Gaussian-program
construction supplies common generated layer spaces, a bounded
initialized action, and its actual adjoint.

On a fixed horizon, clip the readout only in
$b_a=w\phi'(Wu_a)$ above its deterministic pointwise bound. This
product is a globally Lipschitz coordinate map with bounded first
derivatives. The forward map, scalar residual contractions, and
rank-one updates make (7) locally Lipschitz on bounded state balls.
The bounds (8)–(9) supply continuation, and the readout bound keeps
the clip inactive. Thus a unique strong population flow exists on
each fixed interval.

At a fixed Euler mesh, current middle actions unroll into the original
Gaussian matrix, its transpose, and rank-one updates whose coefficients
are permitted scalar contractions. All coordinate instructions satisfy
the finite-program hypotheses. Width-independent Euler error follows
from the preceding norm and Lipschitz bounds. Take width to infinity
at fixed mesh, then refine the mesh.

This proves uniform prediction convergence on $[0,T]$, and deterministic
weak limits of the empirical joint laws of
$(Z_{j1}(T),\ldots,Z_{jm}(T),w_j(T))$. No transcript length grows with
width. In particular, $\Omega_n\to\Omega_\infty$ uniformly on $[0,T]$.

Apply (4) with a margin smaller than $\delta/4$. Except on an event
of vanishing probability, it places the selected row within a fixed
inner neighborhood of
$(0,\ldots,0,\Omega_\infty(T))$ with probability bounded below by $p$.
Choose a bounded Lipschitz function equal to one on this inner
neighborhood and zero outside the neighborhood in (6).
By top-neuron exchangeability, the expected empirical average of this
function is bounded below by $p-o(1)$. Its empirical average converges
in probability to a deterministic number, by the fixed-time law just
proved. Boundedness also gives convergence of expectations, so the
limit is at least $p$. With probability tending to one the average,
and hence the fraction of rows in the outer neighborhood, is at
least $p/2$. This proves (6).

## 6. Application to the proposed cosine trap

Take $m=d=2$, $x_1=e_1$, $x_2=e_2$,

$$
\phi_1(z)=z,\qquad \phi_2(z)=(3+\cos z)/2,\qquad
y=(P,-1),\quad P>2.
\tag{20}
$$

This keeps canonical Gaussian initialization, zero readout, fixed
nonparallel inputs, and activations independent of width.
The initial population top-feature Gram is

$$
\frac{(1-e^{-1})^2}{8}I_2
+\left(\frac{3+e^{-1/2}}2\right)^2\mathbf1\mathbf1^\top,
\tag{21}
$$

and is positive definite.
Interpolation elsewhere is possible: realize top feature rows
$(2,1)$ and $(1,2)$ using preactivations $(0,\pi)$ and $(\pi,0)$.
The prediction coefficients
$(2P+1)/3$ and $-(P+2)/3$ then produce $(P,-1)$ exactly.
For width $n\ge2$, multiply these two coefficients by $n$ in the
readout and set other readout coordinates to zero. Thus this is not
a compatibility or capacity obstruction.

Every initialized readout starts with positive velocity because
$\phi_2\in[1,2]$ and $P>2$. The proposed all-positive collapsed pattern
is $v=(2,1)$ with least-squares coefficient
$S_*=(2P-1)/5$. Its predictions and loss are

$$
f_*=S_*(2,1),\qquad
\mathcal L_*=(P+2)^2/10.
\tag{22}
$$

But

$$
\mathbf1^\top(y-f_*)=-(P+2)/5<0.
\tag{23}
$$

If the deterministic population prediction path converged to this
pattern, then

$$
\Omega_\infty(T)=2\int_0^T\mathbf1^\top(y-f_\infty(t))\,dt
\longrightarrow-\infty.
\tag{24}
$$

The witness theorem therefore has two exact implications:

- Such convergence cannot occur together with a population readout
  that remains nonnegative almost surely at every time.
- Such convergence cannot occur together with a single finite
  bound on the essential supremum of the readout, uniform over all
  times. For any proposed bound, (6) produces a later fixed time
  with a positive fraction of readouts below its negative.

More directly, whenever a fixed time has
$\int_0^T\mathbf1^\top(y-f_\infty)<0$, a strictly positive fraction
of finite-width readouts is negative with probability tending to
one. The initially positive velocities do not give an invariant
positive cone.

These conclusions quantify the earlier constant-row objection.
They do not prove fitting: a negative cohort can later change sign
again, and its guaranteed fraction can shrink rapidly as the chosen
horizon grows. They also do not exclude positive-loss limits with
readout magnitudes lacking a uniform essential bound.

## 7. What remains open for the requested failure

No fixed tanh/tanh example with macroscopic limiting loss and
nonvanishing canonical-Gaussian probability has been found here.
The new theorem uses both a linear first activation and a top critical
point at zero. Tanh/tanh has neither of these features, so it is not
covered.

The old cosine bad basin remains a genuine finite-width deterministic
basin; this note does not erase it or contradict its positive
fixed-width Gaussian probability. Its probability may vanish as
width grows, and the theorem above concerns deterministic finite
times and population support, not arbitrary late capture times.

For the alternate-activation negative route, the remaining narrow
obligation is now stronger than an initial Gaussian small ball:
one must show actual permanent capture despite the finite-time
constant-feature witnesses, including possible negative readouts.
Conversely, a fitting argument would need stable corrective dynamics
or a whole-future path estimate that turns these witnesses into
lasting residual reduction. Neither follows from the present
finite-horizon theorem.

The exact new output is (4)–(6), including the explicit self-impact
estimate (17)–(18). It is a width-uniform Gaussian probability
statement, not a claim of unconditional nonfitting, not a conditional
future kernel-gap theorem, and not merely qualitative finite-time
full support.
