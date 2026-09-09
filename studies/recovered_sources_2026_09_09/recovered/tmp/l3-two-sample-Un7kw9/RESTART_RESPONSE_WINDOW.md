# A fixed-amplitude response restart with the full Gaussian history

This note proves a short-future-window estimate for the actual canonical
source programs at a reached nonaffine state. The amplitude can be fixed
at $e=0.1$. The hypothesis is a bound on the *past* history, not a
response bound on the proposed future window. The latter is proved by
the four-stage causal construction below.

It also identifies the remaining continuation problem. Uniformly bounded
primal norms and a uniformly bounded history norm defined below prevent
finite accumulation of the available windows. Finiteness of those norms
at each successive reached time does not suffice. Propagation of the
history norm leaves a specific weighted response-energy term unbounded;
the primal estimate does not close it. Consequently this note does not
prove the universal-activation two-sample theorem.

Read in full: `CONTRACT.md`,
`DATA_DEPENDENT_CONSTANTS_CLARIFICATION.md`,
`NONLINEAR_RESPONSE_PERTURBATION.md`, `TWO_SAMPLE_SOURCE_BASELINE.md`,
`PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md`, and
`/etc/codex/skills/solve-math-rigorously/SKILL.md`.
The certified angle-specific result is used without re-audit. There are
no agents, experiments, or external theorem dependencies in this note.

## 1. Program, history, and the statement

Use precisely equations (6)--(10) of
`NONLINEAR_RESPONSE_PERTURBATION.md`, with

\[
 \phi_e(z)=1+z+e\arctan z,\qquad
 \mathcal D_{e,R}(z,q)=q+e g(z)\tau_R(q),\qquad
 g(z)=(1+z^2)^{-1},\qquad 0<e\le1.
 \tag{1}
\]

Here $R$ is the auxiliary backward cap. Below, the letter $H_*$,
not $R$, denotes the deterministic history bound. All estimates are
independent of the cap. The theorem concerns the label-directed feature
program with $c_a=y_a/2$, $P=\Gamma\operatorname{diag}(c)$.
It does not replace a physical residual vector by a label vector.

For a sample block use the maximum absolute row-sum norm $|\cdot|$.
For a row of time blocks use the sum of their block norms. All derivatives
are formal source derivatives with deterministic coefficients and
covariances frozen, including in singular source directions.

Let $s_m=u\le S<\infty$ be a reached mesh time. Every old source,
coefficient, and coordinate expression is retained. Define

\[
 J^i_{v,j}=\partial_{\zeta^i_j}Z^i_v\quad(i=1,2),
 \qquad
 U^i_v=\sum_{j\le v}|\partial_{\xi^i_j}Z^i_v|
 \quad(i=2,3),\qquad
 T_v=\sum_{j\le v}|\partial_{\xi^3_j}C_v|.
 \tag{2}
\]

The derivative in $J^i_{v,j}$ is a $2\times2$ block. Write

\[
 D^{i,\xi}_{r,j}=\partial_{\xi^i_j}\delta^i_r
 \quad(i=2,3),\qquad
 D^{2,\zeta}_{r,j}=\partial_{\zeta^2_j}\delta^2_r.
\]

The following are nonnegative random variables on their *separate*
coordinate populations. Empty maxima and sums are zero:

\[
 \mathcal H_1(u)=1+
   \max_{j<v\le m}\frac{|J^1_{v,j}|}{h_j},
 \tag{3}
\]

\[
\begin{split}
 \mathcal H_2(u)=1
 &+\max_{j<v\le m}\frac{|J^2_{v,j}|}{h_j}
   +\max_{v\le m}U^2_v\\
 &+\max_{j<m}\frac1{h_j}
          \sum_{r<m}h_r|D^{2,\zeta}_{r,j}|
   +\sum_{r<m}h_r\sum_{j\le r}|D^{2,\xi}_{r,j}|,
 \tag{4}
\end{split}
\]

\[
 \mathcal H_3(u)=1+\max_{v\le m}U^3_v
                 +\max_{v\le m}T_v
                 +\sum_{r<m}h_r\sum_{j\le r}|D^{3,\xi}_{r,j}|.
 \tag{5}
\]

There is no division by a terminal zero step: every index divided by
$h_j$ has $j<m$ and hence $h_j>0$. The old diagonal
$D^{2,\zeta}_{j,j}$ in (4) is included with its weight $h_j$.
In particular it is not erroneously assumed to be $O(h_j)$.

These are history norms of random derivatives, not just absolute values
of their expectations. They include past preactivation responses and
accumulated backward responses. This extra content is necessary for the
estimates below. A bound solely on the deterministic $a,b$ rows is not
being renamed as an $L^2$ bound on their underlying random derivatives.

**Local restart lemma.** Fix $B,H_*\ge1$ and $S<\infty$. Suppose
the actual canonical prefixes at $u$, in the mesh/cap family under
consideration, satisfy

\[
 \max_{i=1,2,3}\|\mathcal H_i(u)\|_2\le H_*.
 \tag{6}
\]

Suppose also that the primal sizes on the prefix and candidate future
window are at most $B$: each sample's first preactivation $L^2$ norm,
both matrix operator norms, and the readout $L^2$ norm. It suffices to
assume these bounds up to a first exit. There are explicit finite
constants

\[
 A_2,A_3,M_3,M_2,K=K(B,H_*,S),\qquad
 d_* =\min\{1,(2K)^{-1}\}>0
 \tag{7}
\]

such that every continuation with $s_k-u\le d_*$, $s_k\le S$,
satisfies

\[
 |a^i_{kj}|\le A_i h_j\quad(j<k),\qquad
 \sum_{j\le k}|b^i_{kj}|\le M_i\quad(i=2,3),
 \tag{8}
\]

including all columns $j<m$. All coordinate fields have a common
subGaussian moment bound on the extended prefix, and (3)--(5) at its end
have a finite $L^2$ bound $\Psi(B,H_*,S)$. No smallness of $e$
depending on $B,H_*,S$, the input pair, or the horizon is used.

The assertion is an estimate for the actual cap programs: (8) is its
conclusion, not its future hypothesis. It gives estimates usable in a
subsequent mesh/cap limit. It does not assert that an uncut population
limit exists merely because a fixed mesh has been identified.

## 2. What a restart retains

For $k\ge m$ the exact equations are, in particular,

\[
\begin{split}
 Z^1_k&=Z^1_m+\sum_{m\le r<k}h_rP\delta^1_r,\\
 Z^2_k&=\xi^2_k+\sum_{r<m}a^2_{kr}\delta^2_r
                     +\sum_{m\le r<k}a^2_{kr}\delta^2_r,\\
 Z^3_k&=\xi^3_k+\sum_{r<m}a^3_{kr}\delta^3_r
                     +\sum_{m\le r<k}a^3_{kr}\delta^3_r,\\
 C_k&=C_m+\sum_{m\le r<k}h_rc^TH^3_r,\\
 q^{i-1}_k&=\zeta^{i-1}_k+
        \sum_{v<m}b^i_{kv}H^{i-1}_v+
        \sum_{m\le v\le k}b^i_{kv}H^{i-1}_v.
 \tag{9}
\end{split}
\]

The old-column coefficients $a^i_{kr},b^i_{kv}$ still depend on the
new row $k$; replacing them by row $m$ is not allowed.
Nor is $Z^2_k$ a new independent Gaussian applied to a reached field.
For example its source retains

\[
 \mathbb E[\xi^2_{k,a}\xi^2_{r,b}]
     =\mathbb E_1[H^1_{k,a}H^1_{r,b}],\qquad r<m,
 \tag{10}
\]

and each other Gaussian group retains its analogous complete covariance.
Equations (9)--(10), rather than a newly initialized source system, are
the restart used here. No new independent Gaussian noise is inserted.

At a nonaffine reached state the exact current returns remain

\[
 b^3_{ka,kb}=\mathbf1_{a=b}\mathbb E L^3_{k,aa},
 \qquad
 b^2_{ka,kb}=\mathbf1_{a=b}\mathbb E L^2_{k,aa}
        +b^3_{ka,kb}\mathbb E[V^2_{k,aa}G^2_{k,bb}],
 \tag{11}
\]

where $G=\operatorname{diag}(\phi_e'(Z))$,
$V=\operatorname{diag}(\partial_q\mathcal D)$, and
$L=\operatorname{diag}(\partial_z\mathcal D)$.
They have no factor $s_k-u$. We use

\[
 |G|,|V|\le2,\qquad |L^i_k|\le e Q^i_k,
 \quad Q^1_k=|q^1_k|_\infty,\quad
 Q^2_k=|q^2_k|_\infty,\quad Q^3_k=|C_k|.
 \tag{12}
\]

The current terms will be bounded using the primal $L^2$ estimate
and the old random response envelope. They are never absorbed by
pretending that the future interval makes them small.

## 3. Bounds already implied by the past hypothesis

Set $Q_*=32B^3$. The forward bounds $4B,7B^2,10B^3$ and backward
bounds $2B,4B^2,8B^3$, obtained from (1) and the bounded matrix actions,
show that $Q_*$ dominates every relevant sample-pair $L^2$ norm and
every scalar Gaussian source standard deviation. In particular

\[
 \|Q^i_k\|_2\le Q_*.
 \tag{13}
\]

The learned part of a forward coefficient block is at most $Q_*^2h_j$.
The sum of the learned backward block norms is at most $SQ_*^2$.
Both statements follow by Cauchy--Schwarz and
$\sum_b|c_b|=1$, with the column label retained.

For all old rows the response formulas and (3)--(6) give

\[
 A_0=2H_*+Q_*^2,
 \qquad M^0_3=eQ_*H_*+2H_*+SQ_*^2,
 \qquad M^0_2=eQ_*H_*+4M^0_3H_*+SQ_*^2.
 \tag{14}
\]

Indeed the forward response is $\mathbb E GJ$. At the top the
backward derivative row is $L^3\partial Z^3+V^3\mathbf1\partial C$,
whose expected absolute row norm is at most $eQ_*H_*+2H_*$.
At the middle it is

\[
 L^2_k\partial_{\xi^2} Z^2_k
       +V^2_k\sum_{v\le k}b^3_{kv}G^2_v
                                      \partial_{\xi^2}Z^2_v.
 \tag{15}
\]

The first term has expected row norm at most $eQ_*H_*$, and the
second at most $4M^0_3H_*$. This proves (14) without Gaussian
independence between a multiplier and its response.

The earlier perturbation note's moment argument, Section 3, requires
only coefficient bounds, source variance bounds, and $e\le1$; it
does not require a small perturbation from affine. Thus (14) supplies
all past coordinate moments needed here. The response-envelope argument
in its Section 4 also shows that (3)--(5) are a natural finite history
norm: they are bounded by a constant times

\[
 \left(1+S+\sum_{r<m}h_rQ^i_r\right)
 \exp\left\{C S+C e\sum_{r<m}h_rQ^i_r\right\}
 \tag{16}
\]

in the appropriate population, with $C$ depending on the prefix
coefficient bounds. For (4), the diagonal transpose derivative is
bounded by 2 and its time weight cancels its single $h_j$ denominator;
every strictly later derivative carries $h_j$. The same Section 4
bounds all the preactivation maxima in (3)--(5) by one increasing
exponential. In particular (16) uses no random maximum of the Gaussian
coordinates over mesh times. It has finite moments uniformly in a
bounded-coefficient prefix, by the elementary Gaussian exponential
calculation reproduced below.

## 4. Trial constants and an integrable short-window remainder

Choose the following constants in the indicated order:

\[
\begin{split}
 A_2&=2H_*+4+Q_*^2+1,\\
 A_3&=2A_2H_*+4A_2+Q_*^2+1,\\
 M_3&=eQ_*(1+A_3H_*)+2H_*+SQ_*^2+1,\\
 M_2&=eQ_*(1+A_2H_*)
          +4M_3(1+A_2)H_*+SQ_*^2+1.
 \tag{17}
\end{split}
\]

They can be made independent of $e\in(0,1]$ by replacing its
appearances on the right by 1. Put

\[
 A=\max(1,A_0,A_2,A_3),\qquad
 M=\max(1,M^0_2,M^0_3,M_2,M_3).
\]

On any causal prefix covered by these trial bounds, finite iteration of
the coordinate equations gives

\[
 \|Q^i_k\|_p\le L_*\sqrt p\quad(p\ge2),
 \tag{18}
\]

where a deliberately loose choice valid for all fields as well is

\[
 L_*=1000(1+Q_*)(1+A)(1+M)(1+S)^2
       \exp\{20(1+A)(1+M)(1+S)^2\}.
 \tag{19}
\]

For clarity, the middle-layer iteration has feedback $2AM\sum h_r$,
the bottom one $2M\sum h_r$, and the top one $2AS\sum h_r$.
Their forcing is bounded by a numerical multiple of
$(1+Q_*)(1+A)(1+S)\sqrt p$; recovering $q$ adds a factor at most
$1+M$. Their finite-product bounds are respectively
$\exp(2AMS),\exp(2MS),\exp(2AS^2)$, all dominated by (19).
This verifies (18), including unequal meshes, with no future response
assumption beyond the temporary coefficient bounds at available stages.

Let

\[
 \kappa=100(1+A)(1+M)(1+S),\qquad
 E^i_k=\exp\left\{\kappa(s_k-u)
               +\kappa e\sum_{m\le r<k}h_rQ^i_r\right\}.
 \tag{20}
\]

For $s_k-u\le1$, the elementary exponential estimates give

\[
 \|E^i_k\|_6\le2\exp\{\kappa+20\kappa^2L_*^2\}.
 \tag{21}
\]

Here is the integrability justification. Expanding a square exponential
using (18) and $n!\ge(n/\mathrm e)^n$ gives
$\mathbb E\exp(Q^2/(4\mathrm e L_*^2))\le2$.
The inequality $vQ\le Q^2/(4\mathrm e L_*^2)+\mathrm e v^2L_*^2$
then gives
$\mathbb E e^{vQ}\le2e^{\mathrm e v^2L_*^2}$.
For $d=s_k-u>0$, convexity gives

\[
 \exp\left(v\sum_{m\le r<k}h_rQ_r\right)
       \le\sum_{m\le r<k}\frac{h_r}{d}e^{vdQ_r}.
\]

Apply this with $v=6\kappa e$, take the sixth root, and use
$6\mathrm e<20$. The case $d=0$ is immediate. This argument uses
all actual time correlations and needs no independence from the past.

In particular, for any old envelope $F$ from (3)--(5) in the same
population, Hölder with exponents $2,6,6,6$ proves

\[
 \mathbb E\left[F E^i_k(1+Q^i_k)
                   \sum_{m\le r<k}h_r(1+Q^i_r)\right]
 \le 2H_*d(1+\sqrt6L_*)^2
                    e^{\kappa+20\kappa^2L_*^2}.
 \tag{22}
\]

Only the old envelope's $L^2$ norm is used. No independence or higher
moment of $F$ is silently imposed. Omitting either current multiplier
from (22) yields the corresponding simpler estimate.

## 5. Future derivatives with old forcing retained

This section supplies the small factor $d=s_k-u$. All statements are
pathwise before taking expectations. Use the exact derivative equations
(24), (26), and (28) of the perturbation note.

For bottom transpose source $j<m$, the forcing is the actual
$J^1_{m,j}$. For $m\le j<k$, it is $h_jPV^1_j$.
In either case, the remaining terms are precisely the future integral
of

\[
 P\left[L^1_rJ^1_{r,j}
           +V^1_r\sum_{v\le r}b^2_{rv}G^1_vJ^1_{v,j}\right].
 \tag{23}
\]

The summation in (23) includes $v<m$; these old derivatives have bound
$h_j\mathcal H_1(u)$. Consequently, after division by $h_j$, finite
iteration bounds the future derivatives by
$4\kappa\mathcal H_1(u)E^1_k$. Their remainder after subtracting the
specified forcing is bounded by

\[
 4\kappa^2\mathcal H_1(u)E^1_k
                   \sum_{m\le r<k}h_r(1+Q^1_r).
 \tag{24}
\]

For a middle transpose source, the two appropriate forcing terms are

\[
 \sum_{r<m}a^2_{kr}D^{2,\zeta}_{r,j}\quad(j<m),
 \qquad a^2_{kj}V^2_j\quad(m\le j<k).
 \tag{25}
\]

Their norms divided by $h_j$ are at most
$A_2\mathcal H_2(u)$ and $2A_2$. The remainder is

\[
 \sum_{m\le r<k}a^2_{kr}
       \left[L^2_rJ^2_{r,j}
          +V^2_r\sum_{v\le r}b^3_{rv}G^2_vJ^2_{v,j}\right].
 \tag{26}
\]

Here (4) bounds the first term of (25), including its $r=j$ term.
Old $J^2_{v,j}$ in (26) are also bounded by (4).
The same finite iteration gives (24) with population 2 in place of 1.
Its leading derivative bound is again $4\kappa\mathcal H_2(u)E^2_k$.

For middle forward-source rows define the actual old-forcing row

\[
 J^{2,\mathrm{old}}_{k,j}
      =I\mathbf1_{k=j}+\sum_{r<m}a^2_{kr}D^{2,\xi}_{r,j}.
 \tag{27}
\]

Its absolute row sum is at most $1+A_2\mathcal H_2(u)$.
The difference from the true row is the sum over $m\le r<k$ of
$a^2_{kr}D^{2,\xi}_{r,\bullet}$.
By (15) its norm is bounded by

\[
 A_2\sum_{m\le r<k}h_r(eQ^2_r+4M_3)
       \max_{v\le r}U^2_v.
 \tag{28}
\]

The maximum over old $v$ is controlled by (4); future maxima are
controlled by finite iteration. Thus both the full row bound and the
remainder bound (24) hold for (27) as well.

At the top use

\[
 J^{3,\mathrm{old}}_{k,j}
      =I\mathbf1_{k=j}+\sum_{r<m}a^3_{kr}D^{3,\xi}_{r,j},
 \qquad T^{\mathrm{old}}_{k,j}=\partial_{\xi^3_j}C_m.
 \tag{29}
\]

Their row sums are at most $1+A_3\mathcal H_3(u)$ and
$\mathcal H_3(u)$. The exact remainders satisfy

\[
 \partial Z^3_k-J^{3,\mathrm{old}}_k
    =\sum_{m\le r<k}a^3_{kr}
                      (L^3_r\partial Z^3_r+V^3_r\mathbf1\partial C_r),
\]
\[
 \partial C_k-\partial C_m
    =\sum_{m\le r<k}h_rc^TG^3_r\partial Z^3_r.
 \tag{30}
\]

For the sum of the two row norms the feedback is at most
$\sum_{m\le r<k}h_r(2A_3+2+eA_3Q^3_r)$ times the preceding
maximum. The bounds (24) therefore hold for their remainders too.

For completeness, the finite iteration used here has the following
elementary form. If $x_k\le f+\sum_{m\le r<k}h_r\lambda_r \max(f,x_m,\ldots,x_r)$, where $f,\lambda_r\ge0$, induction gives
$x_k\le f\prod_{m\le r<k}(1+h_r\lambda_r)$.
Bound this product by the exponential of its nonnegative sum.
In (23)--(30), $f\le4\kappa\mathcal H_i(u)$ after the stated source
normalization, and all feedback coefficients are bounded by
$\kappa(1+Q^i_r)$; (20) uses the sharper coefficient
$\kappa+\kappa eQ^i_r$. Substitution back into the remainder sums
gives (24). This also explains why none of these estimates acquires a
factor equal to the number of source times.

## 6. Closing the actual four coefficient rows

Equations (22)--(30) imply that every expected remainder below is at most
$Kd$, where, for example, one may take

\[
 K=10^6\kappa^4(1+H_*)(1+L_*)^2
                   \exp\{2\kappa+100\kappa^2L_*^2\}.
 \tag{31}
\]

To verify that this single bound covers the outputs, a forward output
multiplies (24) by at most 2. A top backward output multiplies its
preactivation remainder by at most $eQ_k$, and its readout remainder
by at most 2. A middle backward output adds at most $4M_3$ times the
largest expected preactivation-row remainder, as well as the
$eQ_k$ term. Thus a common pathwise majorant is
$100\kappa^3\mathcal H_i(u)E^i_k(1+Q^i_k) \sum_{m\le r<k}h_r(1+Q^i_r)$; (22) is dominated by (31).

1. **Construct $a^2_k$.** Multiply the bottom forcing and remainder
   by $G^1_k$, then add the learned term. Uniformly over *all*
   $j<k$, old and new,

   \[
    |a^2_{kj}|/h_j\le2H_*+4+Q_*^2+Kd=A_2-1+Kd.
    \tag{32}
   \]

   Only strictly earlier $b^2_r$ has been used.

2. **Construct $a^3_k$.** The newly bounded $a^2_k$ makes (25)
   available. Its two forcing bounds, the gate bound, and the learned
   term give

   \[
    |a^3_{kj}|/h_j\le2A_2H_*+4A_2+Q_*^2+Kd=A_3-1+Kd.
    \tag{33}
   \]

   Only past $b^3_r$ occurs in its future integral.

3. **Construct $b^3_k$.** Split its derivative into the old-forcing
   terms $L^3_kJ^{3,\mathrm{old}}_k+V^3_k\mathbf1\partial C_m$
   and the remainders (30). By Cauchy--Schwarz and (13),

   \[
    \mathbb E\big[Q^3_k(1+A_3\mathcal H_3(u))\big]
       \le Q_*(1+A_3H_*).
   \]

   Therefore

   \[
    |b^3_{k\bullet}|_{\rm r}
      \le eQ_*(1+A_3H_*)+2H_*+SQ_*^2+Kd=M_3-1+Kd.
    \tag{34}
   \]

   This includes the direct current source in (29), hence the first
   current return in (11). No current $b^3_k$ was assumed to obtain it.
   Its construction now makes the actual $q^2_k$ available.

4. **Construct $b^2_k$.** In (15), split every future preactivation
   derivative using (27). Every old $U^2_v$ is at most
   $\mathcal H_2(u)$; every future old-forcing row is at most
   $1+A_2\mathcal H_2(u)\le(1+A_2)\mathcal H_2(u)$.
   The first term of (15) contributes at most
   $eQ_*(1+A_2H_*)$ before its remainder. The second contributes
   at most $4M_3(1+A_2)H_*$. Hence

   \[
    |b^2_{k\bullet}|_{\rm r}
      \le eQ_*(1+A_2H_*)+4M_3(1+A_2)H_*+SQ_*^2+Kd
      =M_2-1+Kd.
    \tag{35}
   \]

   The current $b^3_{kk}G^2_k$ contribution is present in (15).
   Thus (35) also includes the second current return in (11).

Choose $d\le d_*$, so $Kd\le1/2$. Equations (32)--(35) have a
strict half-unit margin. Induct through their four stages, and then
through the time nodes. At each stage the temporary bounds used in
(18)--(30) concern only rows already bounded in that induction. At
$k=m$ the future sums are empty, and the old-forcing estimates alone
give the same margin. This proves (8). It does not rely on continuity
of a coefficient system whose dimension grows with the mesh.

The entire extended prefix now has deterministic bounds $A,M$.
Consequently (18) holds throughout it. Applying the global derivative
envelope (16) with these bounds gives a finite, mesh/cap-independent
bound for (3)--(5) at the new endpoint. One possible loose bound is

\[
 \Psi(B,H_*,S)=100\kappa^3(1+S)(1+L_*)
       \exp\{2\kappa(1+S)+100\kappa^2(1+S)^2L_*^2\}.
 \tag{36}
\]

Indeed the preactivation responses are bounded by a numerical multiple
of $\kappa\exp(\kappa S+\kappa e\sum h_rQ_r)$; accumulated backward
responses add at most a multiple of
$\kappa^2(1+S+\sum h_rQ_r)$. Apply Hölder and the same exponential
calculation as (21), now with total duration at most $S$. This proves
(36). In particular a higher moment of the original history envelope
is not required to conclude its new $L^2$ bound: the full-origin
derivative equations supply it once the extended coefficient bounds
have been established.

If a future primal bound was not supplied, it has a local version
independent of responses. Starting from reached primal sizes at most
$B_0\ge1$, take a ball of radius $2B_0$. Direct forward/backward
norm estimates bound the sum of the raw update norms by
$50(2B_0)^3$. Thus on a future interval of length at most
$B_0/[100(2B_0)^3]$, the displacement is at most $B_0/2$.
The first-exit induction gives a uniform primal margin, including for
Euler steps. If $B_{\rm past}$ bounds the retained prefix, apply the
lemma with $B=\max\{B_{\rm past},2B_0\}$ and the smaller of its
response-window length and the local primal length. One may instead
choose $B_0\ge B_{\rm past}$. A reached-state bound alone is not a
bound on its retained past. This uses no affine comparator and no small amplitude.

## 7. What prevents accumulation, and what is not proved

The constants (14), (17), (19), (20), and (31) are increasing finite
functions of upper bounds for $B,H_*,S$. Therefore the following is a
precise nonaccumulation criterion for this estimate:

> If, before a putative finite terminal time $u_*\le S$, the actual
> canonical prefixes have common primal bound $\bar B<\infty$ and
> common bounds $\|\mathcal H_i(u)\|_2\le\bar H<\infty$, uniformly
> in the mesh/cap family, then the source estimate restarts on a common
> sufficient length
> $\delta_* = \min\{d_*(2\bar B,\bar H,S),
> \bar B/[100(2\bar B)^3]\}>0$ by the local primal argument.
> If the candidate continuations already have primal bound $\bar B$,
> their response-window length is $d_*(\bar B,\bar H,S)$.
> Such a terminal time cannot be
> caused by failure of this response estimate. The certified window
> lengths need not accumulate there.

Equivalently, covering a bounded horizon with these *uniform* bounds
requires at most $1+\lceil 2S/\delta_*\rceil$ windows (with a shorter final
one). For meshes of maximum step below $\delta_*/2$, choose consecutive
windows with length between $\delta_*/2$ and $\delta_*$, apart from the
final remainder. Any refinement must remain in the family for which the
uniform hypotheses hold; it is not the same controlled trajectory.
None of these choices changes $e$.

The word “uniform” is essential. The proof gives only

\[
 H_{i+1}\le\Psi(B_i,H_i,S),\qquad
 d_i=d_*(B_i,H_i,S)
 \tag{37}
\]

as a sufficient recursive certificate, up to a neighboring mesh node
and final-window shortening, when no global history estimate is known.
Here $i$ indexes windows, and $H_i$ bounds all three population history
norms. The right side of (36) grows much faster than linearly in
$H_i$, and the available $d_*$ tends to zero as $H_i$ increases.
These estimates supply no divergent lower bound for the sum of the
available window lengths. Finiteness at each restart therefore does
not establish continuation to every prescribed finite $S$, even
under a separately known primal bound on that horizon.

This is a statement about the estimate. It neither asserts that the
actual response norm blows up nor asserts that accumulation must occur.
A strong primal endpoint alone does not give (6) at that endpoint.

## 8. The exact dynamical inequality still unclosed

The obstruction is visible already in a single bottom source column;
the middle and top equations have the corresponding multiplier. Fix a
past source slot $(j,b)$, and, after its direct forcing time, put

\[
 v_k=h_j^{-1}\partial_{\zeta^1_{j,b}}Z^1_k\in\mathbb R^2,
 \qquad
 F_k=P\left[L^1_kv_k+
           V^1_k\sum_{r\le k}b^2_{kr}G^1_rv_r\right].
 \tag{38}
\]

The exact Euler derivative update and its Euclidean energy identity are

\[
 v_{k+1}=v_k+h_kF_k,
\]
\[
 \mathbb E\|v_{k+1}\|_2^2-\mathbb E\|v_k\|_2^2
   =2h_k\mathbb E\langle v_k,F_k\rangle
                          +h_k^2\mathbb E\|F_k\|_2^2.
 \tag{39}
\]

All old responses in the sum in (38) remain present. The contribution
of $L^1_k$ to $\mathbb E\langle v_k,F_k\rangle$ is exactly

\[
 e\,\mathbb E\left[
   v_k^TP\operatorname{diag}
       \big(g'(Z^1_{k,a})\tau_R(q^1_{k,a})\big)v_k\right].
 \tag{40}
\]

Using $\|P\|_{\mathrm{op}}\le1$ and $|g'|\le1$ bounds the absolute
value of (40) by $e$ times

\[
 \mathbb E[Q^1_k\|v_k\|_2^2].
 \tag{41}
\]

The memory term in (38) has the deterministic row factor
$|b^2_{k\bullet}|_{\rm r}$ and past $L^2$ response norms. It can
be bounded by these norms using Cauchy--Schwarz at each old slot.
In contrast, the primal bound gives only

\[
 \mathbb E[Q^1_k\|v_k\|_2^2]
       \le Q_*\big(\mathbb E\|v_k\|_2^4\big)^{1/2},
 \tag{42}
\]

which is not an inequality in the $L^2$ history norm.
The last term of (39) likewise includes
$h_k^2\mathbb E[(Q^1_k)^2\|v_k\|_2^2]$.
It is finite on every bounded-coefficient prefix by the established
envelopes, but a primal bound alone does not give its needed uniform
control. If a differentiable continuous response limit is available,
the corresponding leading energy equation is obtained from (39);
no such limit is needed to locate the gap in this exact finite-mesh
identity.

Even a subGaussian bound for the multiplier does not repair (42) using
only an $L^2$ response norm. This can be checked within a single
Gaussian probability space. Let $G\sim N(0,1)$ and

\[
 V_n=\exp(nG-n^2).
\]

Completing the square in the Gaussian density gives

\[
 \mathbb EV_n^2=1,
 \qquad
 \mathbb E[GV_n^2]=2n,
 \qquad
 \mathbb E[|G|V_n^2]\ge2n.
 \tag{43}
\]

The multiplier $G$ has one fixed Gaussian law, and each $V_n$ is
smooth with every finite moment. Thus bounded multiplier variance,
uniform subGaussian multiplier tails, and a bounded response $L^2$
norm admit no general bound on the weighted energy (41). This is a
functional obstruction to the proposed norm inequality, **not** a
claim that $V_n$ is an actual network response or a counterexample to
the fixed-data theorem.

For the canonical dynamics one must therefore bound the actual signed
term (40), or its absolute majorant (41), by a quantity that propagates
the history norm without finite-time blow-up. The sign of $g'(Z)\tau_R(q)$
(or $g'(Z)q$ in the uncut version)
cannot simply be discarded and then credited with a favorable
cancellation; no such canonical cancellation has been proved here.
Using higher response moments merely moves this same weighted term
to the next moment. The global envelopes (16), with coefficients
estimated from the unknown history norm itself, yield (36), not a
closed non-blow-up differential or integral inequality.

Thus the new result is a full-history local response restart for one
fixed nonlinear activation, with a quantitative nonaccumulation
criterion. The precise missing global estimate is propagation of the
history norm through (39)--(42), including the actual signed nonlinear
term (40). Neither the certified angle-specific theorem nor the
universal-activation theorem is strengthened by treating that missing
estimate as an assumption. All arguments retain the two sample blocks,
both matrix orientations, and all old Gaussian correlations; none
uses an inverse input Gram matrix, so the local result includes
$\rho=-1$ and either label choice.
