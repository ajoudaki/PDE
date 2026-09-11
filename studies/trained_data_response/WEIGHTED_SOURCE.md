# Actual finite reference queries and admissible data forcing

Author: `/root/weighted_source`. This is an author proof candidate, not an
independent review or a promoted result. The new argument is a one-column
deletion comparison for the actual continuous reference flow. It proves the
weighted uniform integrability missing from a value-only Gaussian-program
argument. No training experiment is used.

## 1. Model, notation and conclusions

Use precisely the model in the study assignment: two width-n tanh hidden
layers, no biases, normalized input `u=x/sqrt(2)` on `S^1`, forward equations
`z1=w u`, `h1=tanh(z1)`, `z2=A h1`, `h2=tanh(z2)`,
`f=c^T h2/n`; independent initialized entries of variances `(1,1/n,1/n²)`;
stored-weight mobilities `(n,1,n)`; unhalved mean squared loss; physical time.
Throughout the actual finite reference GF trains on the two atoms
`(e1,+1),(e2,-1)` of weight one half each. Its finite initialized readout is
the prescribed Gaussian vector, never zeroed.

All finite vector norms are ordinary Euclidean norms, with their `sqrt(n)`
normalization displayed. Finite rank-one actions are `v h^T/n`; their ordinary
Frobenius norms equal the corresponding population Hilbert–Schmidt norms.
At population width use the canonical separate spaces
`H1=L²(Omega1)`, `H2=L²(Omega2)`, with the actual initialized Gaussian action
`A0:H1->H2` and its adjoint. Write `A=A0+K`; only `K` is Hilbert–Schmidt.

Let `phi=tanh`, and, for any passive input `u`, define

\[
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad
 H^2(u)=\phi(Z^2(u)),\quad
 \delta(u)=c\phi'(Z^2(u)),\quad Q(u)=A^*\delta(u).
 \tag{S1}
\]

The finite starred action in this display is the actual transpose. Define

\[
 F(z)=z/2+\sinh(2z)/4,\quad
 X_a=F(w_a)-F(g_a),\qquad a=1,2.
 \tag{S2}
\]

Here `g_a` is the unchanged initialized first column. The two active inputs
are exactly the two first-row coordinates, so this is the full first-row
clock. Since `F'=cosh²>0`, the global inverse gives
`w_a=J(X_a,g_a)`, where `J_X=phi'(J)` and `|J_X|<=1`.

For every fixed finite physical `T`, put

\[
 E_n=\{\|A_{0,n}\|_{op}\le10,
          \|c_{0,n}\|_\infty\le1,
          \|g_n\|_F/\sqrt n\le2\}.
 \tag{S3}
\]

Its probability tends to one. The matrix assertion follows from the
contained sphere-net Gaussian estimate in special-data III.F.2; the root
assertion is the iid second-moment law; and
`P(max_j |c0,j|>1)<=2n exp(-n²/2)`. In particular (S3) retains the actual
small Gaussian readout.

**Finite source theorem.** For each finite `p>=1,T<infinity`, there is a
finite deterministic `C_(p,T)` such that

\[
 \mathbb E\left[\mathbf1_{E_n}\frac1n\sum_{i=1}^n
       \sup_{t\le T,u\in S^1}|Q_{n,i}(t,u)|^p\right]
       \le C_{p,T},\qquad n\ge1.                         \tag{S4}
\]

The constants can be chosen with `C_(p,T)^(1/p)<=C_T sqrt(p)` for `p>=2`.
The supremum concerns query **values**; it does not assert Gaussian tails
for input derivatives. Set `N_(n,i)=sup_(t<=T,u)|Q_(n,i)(t,u)|`. Then

\[
 \sup_{t\le T}|X_{n,ia}(t)|\le3T N_{n,i},\qquad
 \sup_{t\le T}|w_{n,i}(t)|\le |g_{n,i}|+6T N_{n,i},
 \tag{S5}
\]

and all finite moments, averaged over coordinates and restricted to `E_n`,
of the following envelopes are bounded independently of width:

\[
 N_{n,i},\quad (1+|g_{n,i}|+N_{n,i})^k,\quad
 \{\cosh^2g_{n,ia}+6T N_{n,i}\}N_{n,i},\quad
 (|g_{n,i}|+6T N_{n,i})N_{n,i}.                    \tag{S6}
\]

Here `k` is any separately fixed finite positive integer. Products of a
fixed number of these envelopes have the same property. These are actual
finite-GF estimates, before any width limit.

**Population source theorem.** For the established reference of C.4.5,
there is a finite `M_*` such that

\[
 \sup_{t\ge0,u\in S^1}
 \left(\sum_{a=1}^2
     \|\cosh^2 w_a(t)Q(t,u)\|_{L^2(\Omega_1)}^2\right)^{1/2}
 \le M_* .                                                 \tag{S7}
\]

The proof below gives an entirely explicit, very large upper bound from
`s_dagger<=10`; alternatively (S7) defines the precise reference quantity
consumed by the forcing theorem. It is not a numerical evaluation of the
actual trained endpoint.

For `Z=sqrt(2)S^1 x [-Y,Y]` and a finite signed Borel measure `sigma`, define
the clock-state forcing, of type

\[
 \mathcal H=L^2(\Omega_1;\mathbb R^2)
          \oplus\mathcal S_2(H_1,H_2)\oplus H_2,
 \tag{S8}
\]

by its Bochner integral

\[
 B_\sigma(t)=\int b(t,u,y)\,d\sigma(\sqrt2u,y),
 \quad b=-2r(t,u,y)\left(
    \left(u_a\frac{\phi'(w\cdot u)}{\phi'(w_a)}Q(u)\right)_{a=1}^2,
    \delta(u)\otimes H^1(u),\ H^2(u)\right).
 \tag{S9}
\]

Then `B_sigma` is continuous in physical time, is linear in `sigma`, and

\[
 \sup_{t\ge0}\|B_\sigma(t)\|_{\mathcal H}
 \le 2(Y+\sqrt{10})\sqrt{M_*^2+11}\,\|\sigma\|_{TV}.
 \tag{S10}
\]

Total variation denotes total mass of the variation measure, with no
factor of one half. The estimate applies in particular to `nu-nu_*`, of
mass at most two. It imposes no support size, atom weight, Gram or
orthogonality restriction on the perturbing law. The same finite forcing
has bounded normalized moments and weighted uniform integrability on
`E_n`, uniformly over `t<=T` and inputs, with constants depending on `T,Y`.

Section 8 states the precise width identification and quadrature conclusion.
These source results alone are not a tangent-capture theorem. They supply
the inhomogeneous term needed by that theorem and by the propagator result.

## 2. Exact physical equations and deterministic reference bounds

The mean loss is `R=(r1²+r2²)/2`. From the stored-weight mobilities the exact
finite reference equations, and their population counterparts, are

\[
 \dot w_a=-r_a\phi'(w_a)Q_a,\quad
 \dot X_a=-r_aQ_a,\quad
 \dot K=-\sum_{a=1}^2r_a\delta_a\otimes H_a^1,\quad
 \dot c=-\sum_{a=1}^2r_aH_a^2 .                    \tag{S11}
\]

Here `Q_a=Q(e_a)`; the two factors of the general `-2 integral` cancel the
two atom weights. Since `F'=1/phi'`, the clock identity in (S11) is exact.
For a general law the corresponding first clock field is
`-2 integral r u_a phi'(w.u)Q(u)/phi'(w_a)`, which gives (S9), with its
displayed sign and normalization. No probability-law derivative is used
to establish these identities.

On (S3), initially `|f_a|<=1`, hence `R(0)<=4`. The true raw energy identity
gives `R(t)<=4` and raw path displacement at most `2sqrt(T)` up to time T.
Therefore, simultaneously for all `t<=T`,

\[
 \|A(t)\|_{op}\le B:=10+2\sqrt T,\quad
 \|c(t)\|_2/\sqrt n\le C:=1+2\sqrt T,
 \quad\|w(t)\|_F/\sqrt n\le W:=2+2\sqrt T,
 \tag{S12}
\]

and `||K||F<=2sqrt(T)`. Moreover `sum_a|r_a|<=4`, `|r_a|<=sqrt(8)<3`.
Integration of `dot c` yields

\[
 \|c(t)\|_\infty\le H:=1+4T.                    \tag{S13}
\]

The raw energy identity follows directly by differentiating the finite
loss and substituting its three negative metric gradients; the three
metric terms are `||dot w||F²/n`, `||dot A||F²`, `||dot c||²/n`.
It prevents finite-time escape for the smooth finite-dimensional field.
These statements also hold for the column-deleted flow below, because it
has the same labels and readout, and its initial matrix norm is no larger.

For passive queries all these bounds are independent of u. Directly from
(S11),

\[
 \|\dot w\|_F/\sqrt n\le4BC,\quad
 \|\dot K\|_F\le4C,\quad \|\dot c\|_\infty\le4.
 \tag{S14}
\]

The chain and product rules in finite dimensions give

\[
 \|\partial_t Z^2(u)\|_2/\sqrt n\le4C(1+B^2),\qquad
 \|\partial_t\delta(u)\|_2/\sqrt n
        \le D_t:=4+8HC(1+B^2),
 \tag{S15}
\]

and factor subtraction gives

\[
 \|\delta(t,u)-\delta(t,v)\|_2/\sqrt n
       \le D_u|u-v|,\quad D_u:=2HBW.
 \tag{S16}
\]

Thus `(t,u)->delta(t,u)` is Lipschitz in normalized L², with deterministic
constants on (S3). Only the first-row **RMS** occurs in (S16). This fact,
applied to the independent cavity, is what permits a whole-circle Gaussian
query-value estimate without bounds on pointwise input derivatives.

## 3. Delete one initialized column, retaining the entire learned flow

Fix neuron i in population 1. Let `a_i=A0 e_i`, an ordinary vector with iid
entries `N(0,1/n)`. Run the full reference GF with the initialized matrix

\[
 \widetilde A_0=A_0-a_i e_i^T
 \tag{S17}
\]

and the same initialized `g,c0`. Denote this flow by tildes. In particular
`tilde K` is trained; no neuron, activation, residual or learned rank is
removed. The flow is independent of the random column `a_i` conditionally
on all remaining initialized variables. Uniqueness of the finite ODE
establishes that measurability and independence.

Define the cavity-good event

\[
 E_n^i=\{\|\widetilde A_0\|_{op}\le10,
            \|c_0\|_\infty\le1,\ \|g\|_F/\sqrt n\le2\}.
 \tag{S18}
\]

It is measurable with respect to the remaining variables, and `E_n` is a
subset of `E_n^i`, because right multiplication by `I-e_i e_i^T` is a
contraction. Conditional Gaussian estimates are always made on (S18),
not by falsely conditioning on an event involving `a_i`.

Set `m_i=||a_i||2`, `epsilon_i=m_i/sqrt(n)` and

\[
 Z_i(t,u)=a_i^T\widetilde\delta(t,u),\qquad
 Z_i^\#=\sup_{t\le T,u\in S^1}|Z_i(t,u)|.
 \tag{S19}
\]

These are scalar probes of the cavity, not replacements for actual query
answers. Their conditional covariance is exactly
`tilde delta(t,u)^T tilde delta(s,v)/n`. Both orientations of the actual
matrix remain in the comparison that follows.

Let

\[
 x=\sum_a\|X_a-\widetilde X_a\|_2/\sqrt n,\quad
 k=\|K-\widetilde K\|_F,\quad
 z=\|c-\widetilde c\|_2/\sqrt n,\quad d=x+k+z.
 \tag{S20}
\]

There is no small operator-norm claim for `A0-tilde A0`. Instead its
forward action on a bounded feature has RMS at most `epsilon_i`. Its
reverse action on a cavity backward field has RMS
`|Z_i(t,e_a)|/sqrt(n)`. With `Delta` denoting full minus cavity, add and
subtract factors in precisely this order:

\[
 \Delta Z_a^2=A\Delta H_a^1
         +(K-\widetilde K)\widetilde H_a^1
         +a_i\widetilde H_{a,i}^1,
\]
\[
 \Delta Q_a=A^T\Delta\delta_a
          +(K-\widetilde K)^T\widetilde\delta_a
          +e_i Z_i(t,e_a).
 \tag{S21}
\]

The second identity deliberately uses the full A in the first term, so
that no uncontrolled column-dependent reverse error appears. On `E_n`,
the deterministic state bounds for both flows yield

\[
 \sum_a\|\Delta H_a^1\|_2/\sqrt n\le x,
 \quad V:=\sum_a\|\Delta Z_a^2\|_2/\sqrt n
                      \le Bx+2k+2\epsilon_i,
\]
\[
 D:=\sum_a\|\Delta\delta_a\|_2/\sqrt n\le2z+2H V,
\]
\[
 P:=\sum_a\|\Delta Q_a\|_2/\sqrt n
       \le BD+2Ck+\frac1{\sqrt n}\sum_a|Z_i(t,e_a)|,
\]
\[
 R_\Delta:=\sum_a|r_a-\widetilde r_a|\le2z+CV.
 \tag{S22}
\]

For the last inequality use `f-tilde f=<Delta c,H2>+
<tilde c,H2-tilde H2>`. The first uses `|J_X|<=1`, with the same roots.
The velocity differences from (S11) satisfy

\[
 \sum_a\|\Delta\dot X_a\|_2/\sqrt n\le BC R_\Delta+3P,
\]
\[
 \|\Delta\dot K\|_F\le C R_\Delta+3(D+Cx),\qquad
 \|\Delta\dot c\|_2/\sqrt n\le R_\Delta+3V.
 \tag{S23}
\]

For example the rank difference is bounded by
`||Delta delta||2/sqrt(n)+C||Delta H1||2/sqrt(n)` before its residual
factor. These estimates include the changed residuals; the cavity has
not been driven by the full flow's residuals.

Write `D0=1+B+C+H+3`, `L=100D0^4`. Substitution of (S22) into (S23)
gives the explicit overestimate

\[
 \dot d\le Ld+\frac L{\sqrt n}
       \left(m_i+\sum_a|Z_i(t,e_a)|\right)
       \quad\hbox{for almost every }t,\qquad d(0)=0.
 \tag{S24}
\]

To check the constant, `V<=3D0 d+2epsilon_i`,
`D<=8D0² d+4D0 epsilon_i`,
`P<=10D0³d+4D0²epsilon_i+sum|Z_i|/sqrt(n)`,
`R_Delta<=5D0²d+2D0epsilon_i`.
The three resulting d coefficients sum to at most `81D0^4`, and the
`epsilon_i` coefficients to at most `36D0³`. Norms of absolutely
continuous finite curves obey the derivative bound by the velocity norm,
which justifies (S24) also at zeros of a component norm. Multiplying its
integral form by the integrating factor gives

\[
 \sqrt n\sup_{t\le T}d(t)
       \le J_T(m_i+2Z_i^\#),\qquad J_T:=LT e^{LT}.
 \tag{S25}
\]

This is the small response to deleting one initialized column that an
operator-norm comparison alone would miss.

For an arbitrary passive input u, the first row still obeys
`||Delta(w.u)||2/sqrt(n)<=x`, so the same forward subtraction gives

\[
 \|\delta(t,u)-\widetilde\delta(t,u)\|_2/\sqrt n
            \le4D0^2(d(t)+\epsilon_i).
 \tag{S26}
\]

The learned transpose contribution has an exact, coordinatewise bound:

\[
 (K(t)^T\delta(t,u))_i
   =-\int_0^t\sum_a r_a(v)H_{a,i}^1(v)
       \frac{\delta_a(v)^T\delta(t,u)}n\,dv,
 \qquad |(K(t)^T\delta(t,u))_i|\le4TC^2.
 \tag{S27}
\]

Using `Q_i=a_i^T delta+(K^T delta)_i`, (S25)–(S27), and `m_i<=10` on
`E_n`, gives

\[
 N_{n,i}\le A_T Z_i^\#+B_T\quad\hbox{on }E_n,
\]
\[
 A_T=1+80D0^2J_T,\qquad
 B_T=400D0^2(J_T+1)+4TC^2.
 \tag{S28}
\]

No independence of the actual `delta` and `a_i` has been assumed. Their
dependence is exactly the error controlled in (S26).

## 4. A contained Gaussian maximum bound

Here are all probability ingredients beyond the initialized operator
bound. If `G_1,...,G_N` are centered jointly Gaussian scalars with
variances at most `v²`, no independence among them is required for

\[
 \Pr\{\max_j|G_j|>r\}\le2N e^{-r^2/(2v^2)}.
 \tag{S29}
\]

This follows by applying the scalar Gaussian exponential moment and
Markov's inequality to each tail and taking a union bound. Consequently,
for `p>=2`,

\[
 \|\max_j|G_j|\|_{L^p}
       \le v\{\sqrt{2\log(2N)}+2\sqrt p\}.
 \tag{S30}
\]

For detail, put `a=v sqrt(2log(2N))` and `V=(max|G_j|-a)_+`.
Equation (S29) implies `P(V>r)<=exp(-r²/(2v²))`.
For `m=ceil(p/2)`, integrating this tail against `2m r^(2m-1)` gives
`E V^(2m)<=(2v²)^m m!`; the integral follows by substituting
`q=r²/(2v²)` and integrating by parts m times. Since `m!<=m^m`,
monotonicity of probability-space Lp norms gives
`||V||p<=||V||_(2m)<=v sqrt(2m)<=v sqrt(2p)`, because
`2m<=p+2<=2p` for `p>=2`. Minkowski gives (S30), with slack in the
constant 2. The case `v=0` is zero.

Suppose a continuous centered Gaussian process `Z(q)`, `q in [0,1]^2`,
has variance at most `C²` and
`||Z(q)-Z(q')||L² <= L0 ||q-q'||_1`. Use square grids of spacing `2^-k`
and round each grid point down to its parent on the preceding grid.
There are at most `4^(k+1)` grid points at level k. Parent increments
have standard deviation at most `2L0 2^-k`. Formula (S30), followed by
Minkowski, bounds the sum over k of their maxima in Lp by

\[
 2L0\sum_{k\ge1}2^{-k}
  \{\sqrt{2\log(2\cdot4^{k+1})}+2\sqrt p\}
       \le60L0\sqrt p.
 \tag{S31}
\]

The inequality follows for instance from `sqrt(k+2)<=k+2` and
`sum_(k>=1) k2^-k=2`, `sum_(k>=1)2^-k=1`. The four level-zero corner
values cost at most `4C sqrt(p)` by (S30). The telescoping sums and
continuity at each q therefore give

\[
 \|\sup_q|Z(q)|\|_{L^p}
                \le64(C+L0)\sqrt p.                    \tag{S32}
\]

This proof works conditionally on arbitrary fixed coefficients. Here,
conditional on all variables except column `a_i`, the process (S19) is
a finite linear combination of independent Gaussians, with continuous
coefficients. On `E_n^i`, (S12), (S15)–(S16) apply to the cavity. Parameterize
`t=T q1`, `u=(cos(2pi q2),sin(2pi q2))`. Thus (S32) gives

\[
 \left(\mathbb E_{a_i}[(Z_i^\#)^p]\right)^{1/p}
       \le C_Z\sqrt p,\qquad
 C_Z:=64\{C+T D_t+2\pi D_u\},\quad\hbox{on }E_n^i.
 \tag{S33}
\]

Since `E_n subset E_n^i`, (S28), conditioning, and then (S33) prove

\[
 \left(\mathbb E[\mathbf1_{E_n}N_{n,i}^p]\right)^{1/p}
     \le (B_T+A_T C_Z)\sqrt p=:C_T\sqrt p.
 \tag{S34}
\]

This bound is the same for every i and n; averaging proves (S4). It has
not inferred empirical moments from RMS convergence or exchangeability.
It used the reached continuous reference flow and its quantitative
column-deletion sensitivity. The selected-column concentrating examples
in special-data J.1 and the three-query obstruction in Gaussian calculus
therefore do not contradict it: those arbitrary adapted queries do not
satisfy (S24) with the present constants.

## 5. Clock weights, products and actual finite uniform integrability

For each fixed g,

\[
 \partial_X\cosh^2 J(X,g)=2\tanh J(X,g),
 \qquad \cosh^2 J(X,g)\le\cosh^2g+2|X|.
 \tag{S35}
\]

The derivative identity follows from `J_X=sech² J`; its absolute value is
at most two, and integration gives the inequality for either sign of X.
This exact estimate avoids an unnecessary exponential in `|X|`. Integrating
`dot X_a=-r_a Q_a` with `|r_a|<=3` proves (S5). The factor 6 in its row
bound is an upper bound for `3sqrt(2)`.

Every Gaussian root has every polynomial and linear-exponential moment.
In particular
`E exp(q|G|)<=E exp(qG)+E exp(-qG)=2exp(q²/2)`.
For any fixed p, the moment of `cosh²g_a N_i` on `E_n` is bounded by
Hölder using the `2p` moments of both factors. No independence between
the evolved query and g is required. The same reasoning applies to all
products in (S6). For example, with

\[
 P_{n,i,a}:=(\cosh^2g_{n,ia}+6T N_{n,i})N_{n,i},
 \tag{S36}
\]

one obtains

\[
 \sup_n\mathbb E\left[\mathbf1_{E_n}\frac1n\sum_i
                          P_{n,i,a}^{p}\right]<\infty.
 \tag{S37}
\]

For the finite source coordinate in (S9), `|r(t,u,y)|<=C+Y` and
`|u_a|,phi'(w.u)<=1`, so its supremum over `t,u,|y|<=Y` is bounded by
`2(C+Y)P_(n,i,a)`. Given any `p>2`,

\[
 \mathbb E\left[\mathbf1_{E_n}\frac1n\sum_i
     P_{n,i,a}^{2}\mathbf1_{P_{n,i,a}>R}\right]
       \le C_{p,T}R^{-(p-2)}.                         \tag{S38}
\]

Markov's inequality shows that these empirical square tails tend to zero
in probability, uniformly in width on `E_n`, as R tends to infinity.
Outside `E_n` the probability tends to zero as n grows. Thus the ordered
statement needed for width passage is

\[
 \lim_{R\to\infty}\limsup_{n\to\infty}
 \Pr\left\{\sup_{t,u,|y|\le Y}
       \frac1n\sum_i |b_{X,a,n,i}(t,u,y)|^2
                     \mathbf1_{|b_{X,a,n,i}|>R}>\varepsilon\right\}=0.
 \tag{S39}
\]

One can put the supremum inside the coordinate envelope as in (S38), so
the stated form follows. The same argument proves weighted tails involving
`|w|Q` or any separately fixed polynomial of the displayed envelopes.
These estimates make no assertion that a bounded initialized Gaussian
action maps every Lp input boundedly into Lp.

## 6. Uniform population bounds from the bounded feature segment

The established physical reference equals the autonomous feature flow

\[
 X_{a,s}=\tfrac12y_a Q_a,\quad
 K_s=\tfrac12\sum_a y_a\delta_a\otimes H_a^1,\quad
 c_s=\tfrac12\sum_a y_aH_a^2,
 \tag{S40}
\]

restricted to `0<=s<s_dagger`, where `s_dagger<=10`, with
`ds/dt=2(1-b)>0`. This is C.4.5.1's actual reference and endpoint, not a
new prescription for physical finite GF. To bound the population sources
uniformly in physical time, apply the preceding cavity argument to the
**auxiliary finite feature equation** (S40) on `0<=s<=S=10`, initialized
with `c0=0`. Only this auxiliary equation has zero finite readout.

Its elementary deterministic bounds, on
`{||A0||op<=10, ||g||F/sqrt(n)<=2}`, are

\[
 \|c(s)\|_\infty\le S,\quad \|K(s)\|_F\le S^2/2,\quad
 B=10+S^2/2,\quad C=H=S+1,
\]
\[
 \|w(s)\|_F/\sqrt n\le
 W:=2+10S^2/2+S^4/8.                               \tag{S41}
\]

Indeed `sum_a |y_a/2|=1`, so `||c_s||infty<=1`,
`||K_s||F<=s`, and
`sum_a ||X_(a,s)||2/sqrt(n)<= (10+s²/2)s`. Integration and
`|J(X,g)-g|<=|X|` give (S41). These bounds prove existence on the entire
finite feature interval as in B.1's transformed integral construction.

The proof of (S21)–(S28) now uses the same fixed controls in both flows;
all residual-difference terms vanish. The retained upper bound `L=100D0^4`
remains valid. The velocity bounds (S14)–(S16) remain upper bounds, since
the absolute sum of feature controls is at most one rather than four.
Consequently the formulas (S28), (S33), (S34), with `T` replaced by S and
the constants (S41), give a number `C_*<infinity` such that

\[
 \mathbb E\left[\mathbf1_{E_n^{feat}}\frac1n\sum_i
      \sup_{s\le S,u}|Q^{feat}_{n,i}(s,u)|^p\right]
         \le(C_*\sqrt p)^p,\qquad p\ge2.             \tag{S42}
\]

Every quantity in this crude bound is explicitly given above. No numerical
flow solution is hidden in `C_*`, and no fitting property of the finite
feature flow is assumed.

We detail how this reaches the *canonical* population flow. On each fixed
transformed Euler mesh, append finitely many passive forward and reverse
queries to the oracle program in B.1. The first-row transform is continuous
with at most linear growth in `(X,g)`, hence global-nonlinear A.1 applies.
Readout products can be clipped outside a fixed open neighborhood of the
bound in (S41), so they meet the fixed-program hypotheses. Both matrix
orientations belong to the same III.F construction. Same-root transformed
stability controls the finite-feature-flow/mesh error uniformly in width.
The corresponding population error tends to zero in clock L², increment
HS and readout L²; the HS assertion is proved in C.4.5.2, §1. Passive Q
errors follow by factor subtraction with bounded readout. Width first at
fixed mesh, then mesh removal, therefore gives the joint empirical W2
limits for every finite list of `(g,X,w,Q(s,u))`.

For a finite list of rational parameter pairs `(s_j,u_j)`, apply this
convergence to the bounded continuous test
`min(R,max_j |Q(s_j,u_j)|^p)`. Its empirical average converges in
probability to the deterministic population expectation; since the test
is bounded, the expectations converge as well. Multiplication by
`1_(E_n^feat)` changes the expectation by at most
`R P((E_n^feat)^c)`, which vanishes. Equation (S42) and monotone convergence,
first in R and then in the finite rational lists, give a population
envelope

\[
 N^\#:=\sup_{(s,u)\in\mathcal D}|Q(s,u)|,
 \qquad\|N^\#\|_{L^p}\le C_*\sqrt p,             \tag{S43}
\]

where `mathcal D` is any fixed countable dense parameter set including
the active directions. This envelope is a statement about simultaneous
representatives on that countable set. For any other fixed deterministic
`(s,u)`, L² continuity of Q supplies an almost surely convergent subsequence
from the dense set; thus `|Q(s,u)|<=N#` in its L² equivalence class.
Fubini gives the bound almost everywhere for any fixed deterministic
observation measure. No assertion of pointwise continuous sample paths
for the population Q, or of Gaussian input-derivative tails, is needed.
The map into L² is jointly continuous and is the canonical action map.

Integration of (S40), followed by Fubini, gives almost surely
`sup_s |X_a(s)|<=S N#/2`, for the absolutely continuous active clocks.
Thus (S35) gives, in every deterministic passive-input equivalence class,

\[
 |\cosh^2w_a(s)Q(s,u)|
          \le(\cosh^2g_a+S N^\#)N^\#.
 \tag{S44}
\]

Hölder, `||N#||4<=2C_*`, and
`||cosh²G||4<=(2e^32)^(1/4)=2^(1/4)e^8` imply the explicit bound

\[
 M_*\le\sqrt2\{2^{5/4}e^8 C_*+4S C_*^2\},\qquad S=10.
 \tag{S45}
\]

The physical path stays in this feature segment, so (S7) holds for all
physical times. This reasoning establishes a uniform population source
bound, separately from the fixed-physical-horizon finite estimate (S4).
It does not claim uniform-in-time finite-width convergence.

## 7. Continuity, admissibility and norms of data forcing

The integrand (S9) has all its components in (S8). For the first component,
`phi'(w_a)^(-1)=cosh²w_a` and (S7) apply. For the others,
`||delta tensor H1||HS<=||c||2`, `||H2||2<=1`.
The established feature endpoint bound gives `||c||2<=sqrt(10)` and
`|f(u)|<=sqrt(10)`, hence `|r(u,y)|<=Y+sqrt(10)`. Squaring the three
component bounds gives (S10).

For completeness the integrand is continuous into (S8) jointly in feature
time, input and label. The bounded reference state and its strong velocity
give deterministic L² Lipschitz bounds for `Q(s,u)` by differentiating
`Q=A*delta` in time and using (S16) in input. Their population derivation
uses III.F.9's strong curve chain rule, not ambient Fréchet differentiability.
The envelope (S43) controls all their higher moments. The elementary
interpolation inequality

\[
 \|V\|_4\le\|V\|_2^{1/3}\|V\|_8^{2/3}
 \tag{S46}
\]

follows by Hölder with `1/4=(1/3)/2+(2/3)/8`. Therefore, for any fixed
weight `W0 in L4`,

\[
 \|W0\{Q(s,u)-Q(s',v)\}\|_2
 \le\|W0\|_4\|Q(s,u)-Q(s',v)\|_2^{1/3}
                         (2\|N^\#\|_8)^{2/3}.
 \tag{S47}
\]

For the changing weight use the exact derivative in (S35):
`|cosh²w_a(s)-cosh²w_a(s')|<=2|X_a(s)-X_a(s')|<=N#|s-s'|`.
Also
`|phi'(w(s).u)-phi'(w(s').v)|`
is bounded by a constant times
`N#|s-s'|+(|g|+S N#)|u-v|`.
Every resulting product with Q and the clock weight is integrable in L²
by (S43), Gaussian root moments, and Hölder. Changing the factors of
`r u_a cosh²w_a phi'(w.u)Q` one at a time, (S47) treats the Q difference
and these bounds treat the remaining factors. This proves continuity,
and in fact a deterministic `1/3` Hölder upper bound in `(s,u,y)` on the
compact feature/data parameter set. Middle and readout factors are simpler
Lipschitz differences in L²/HS.

The range of a continuous map from that compact parameter set into the
Hilbert space (S8) is compact and separable. Finite signed Borel measures
therefore admit its Bochner integral, with norm bounded by the integral
of the norm against the variation measure. This proves existence,
linearity, and (S10). Time continuity of the integral follows from uniform
continuity of its compact-domain integrand. Composing with the physical
clock gives continuity for all finite physical intervals, and the same
estimate holds at the fitted endpoint. This construction does not assume
that every signed zero-mass measure is a two-sided probability-law tangent:
it defines a linear forcing operator after the finite right derivatives
have supplied (S9).

The same reasoning at actual finite width uses (S4)–(S6) and the
deterministic normalized L² Lipschitz bound on `Q(t,u)` from (S14)–(S16).
For example its time constant is at most `4C²+B D_t`, and its input
constant at most `B D_u`. On `E_n` there is a random `Z_n` with bounded
fixed moments, uniformly in n, such that

\[
 \|b_n(t,u,y)-b_n(t',v,y')\|_{\mathcal H_n}
 \le Z_n\{|t-t'|+|u-v|+|y-y'|\}^{1/3}.
 \tag{S48}
\]

Here the finite clock-state norm is
`(||v||F²/n+||B||F²+||d||2²/n)^(1/2)`. To see that `Z_n` has the claimed
moments, use (S47) with normalized empirical norms and the finite envelope
`N_(n,i)`, and bound the remaining factor differences by (S5), (S35).
Every empirical envelope norm involved has bounded moments by (S6),
Jensen, and Hölder. No pointwise-in-input derivative moments are required.
The label term is actually Lipschitz; it is weakened to the displayed
exponent only to use one modulus on the compact set. If its diameter is
larger than one, enlarge `Z_n` by that fixed diameter to cover all pairs.

## 8. Exact identification and arbitrary Borel laws

We specify what convergence this source proof supplies, rather than
inventing an operator-norm distance between different width carriers.

1. For each finite deterministic list of physical times and passive inputs,
   the actual finite reference tuples consisting of the full Gaussian
   roots, clocks, raw first fields, hidden values, c and passive Q have
   their joint within-population W2 limits, identified by B.1 and the
   complete III.F/A.1 fixed-mesh construction. The append-only passive
   reverse call is legitimate for exactly the same reason as C.4.5.3's
   active call: bounded readout makes `c phi'(Z2(u))` a bounded-derivative
   instruction after an inactive fixed readout clip; its response uses
   the same initialized action and transpose. The passive first argument
   `w.u` retains both root coordinates. Actual finite readout is handled
   by the same-root finite-flow/mesh comparison; its supremum vanishes in
   probability as in B.1, rather than by resetting the finite flow.

2. Any finite tuple of the source first components (S9), roots, clocks,
   and query values has joint empirical Wp convergence in probability
   for every separately fixed finite p. First clip the additional
   coordinate functions at a fixed level. The tuple is a bounded
   continuous function of the identified node tuple, so its law converges.
   For any moment exponent p, (S6) with a larger exponent controls the
   unbounded tails by (S38). The same moment bound passes to the limiting
   tuple by bounded tests and monotone convergence. Removing the clipping
   identifies moments as well as weak laws. The elementary finite-cell
   coupling proof in III.F.1 extends verbatim from squared distance to
   p-th distance using `|a-b|^p<=2^(p-1)(|a|^p+|b|^p)`; hence these two
   conclusions give Wp convergence. Roots use their Gaussian moments,
   and clocks use (S5). A claim of all moments for arbitrary unrelated
   Gaussian programs is neither assumed nor concluded.

3. In particular, the W2 source-tuple comparisons extend uniformly over
   compact physical time/input/label parameter sets for each fixed tuple
   arity. Use (S48) and pair equal finite neuron indices to bound empirical
   W2 changes between nearby parameters. Its random modulus is tight by
   the just-proved moment estimates. The limiting modulus follows from
   Section 7 (or the same compact-time physical proof). At a fixed finite
   parameter net every required convergence holds simultaneously by a
   finite union bound. Refine the net after taking width to infinity.
   This proves the asserted uniformity for observable laws, without
   coupling individual finite neurons to invented population neurons.

4. For any fixed Borel probability law nu, choose a deterministic finite
   partition of the compact data space with cells of diameter at most h
   and choose one representative per nonempty cell. Let `pi_h nu` put
   its exact cell mass at that representative. This does not impose a
   lower bound on nonzero masses. Minkowski and (S48) give, uniformly for
   `t<=T`,

   \[
   \|B_{\nu,n}(t)-B_{\pi_h\nu,n}(t)\|_{\mathcal H_n}
          \le Z_n h^{1/3}\quad\hbox{on }E_n.
   \tag{S49}
   \]

   The analogous population bound holds with a deterministic constant.
   For a finite signed measure replace one by its total variation mass
   and partition its positive and negative parts, or retain the fixed
   two reference atoms exactly when forming `nu-nu_*`. At fixed h the
   first forcing field is a finite linear combination of the identified
   source nodes. Middle forcing is a finite sum of ranks; its HS norm
   and its differences are determined by the finite pairwise Gram
   contractions of its factors. All these contractions converge by the
   same-layer tuple statement. Thus fixed-law forcing and any fixed
   finite action/probe extension are obtained in the order: fixed
   quadrature and bounded source clips, width limit, source-clip removal,
   and quadrature refinement. Width-independent tails also allow clips
   and quadrature to be chosen in either prescribed nested order.

For action/probe extensions, a clipped source is first approximated by a
bounded smooth coordinate function on a fixed box of its finite input
tuple. The proof of A.1 permits this fixed approximation. Its normalized
L² error is controlled by (S39) and the corresponding population tail.
The initialized operator norm bound then controls the error after either
matrix orientation; learned ranks use their HS bound. A finite sequence
of such extensions is justified by induction, choosing each fixed smooth
approximation before the width limit. This is the action identification
needed when the linear tangent equation acts on the forcing.

Statements 1–4 provide constants independent of atom count and weights and
convergence for every fixed deterministic nu. They assert no failure
probability supremum over all nu, no convergence rate in width, no
uniform-in-physical-time finite-width approximation, and no convergence
of nonlinear perturbed flows. For nonatomic laws the finite loss and its
forcing are exactly integrated functions; the quadrature above is only a
proof approximation, not an empirical training algorithm.

## 9. Downstream use, remaining products and checks

The supplied admissible state norm is (S8); the admissible measure-forcing
norm is total variation. The exact consumed weighted source moment is
(S7). The proof additionally supplies all fixed moments of the actual
finite reference envelopes in (S6), and population counterparts uniformly
on the fitted feature segment. These are useful for passive output
observations, source truncation and input quadrature. The initialized
middle action is used only as a bounded L² action; no Lp action bound is
claimed.

A future finite-contamination theorem would still have to control
products involving the **perturbed** clocks or differences, such as
`[phi'(w_epsilon.u)/phi'(w_epsilon,a)-
phi'(w_*.u)/phi'(w_*,a)]Q_epsilon(u)`, and nonlinear remainders containing
products of two state variations. The present estimates concern the
reference and its one-column cavity, not those general perturbed paths.
Transport convergence of empirical laws to a nonatomic law is not total
variation convergence; (S49) is a separate quadrature estimate for the
reference's linear forcing.

The author read the complete maintained B.1 and C.4.5 reference/source/
finite bridge bodies, the necessary C.4 full-row/common-space passages,
global-nonlinear A.1–A.2, special-data III.F.1–10 (including the complete
singular-query proof), and the relevant III.V query-extension proof.
III.V was read for context; no III.V theorem is invoked here. The
append-only query proof used in Section 8 is supplied directly by III.F,
A.1, B.1's transformed comparison, and the present source truncation.
The arbitrary-action higher-moment, raw-multiplier/curvature and correlated
clock obstructions were checked explicitly. The invoked tools are the
`solve-math-rigorously` and `investigate-conjectures` skills and the latter's
research-contract, adversarial-audit and proof-search references.

The essential exact checks are reproducible without a training run:

```python
from fractions import Fraction as F
# Laurent polynomials in q=exp(z), represented exactly by exponent:coefficient.
def add(a,b):
    c=dict(a)
    for k,v in b.items(): c[k]=c.get(k,F(0))+v
    return {k:v for k,v in c.items() if v}
def mul(a,b):
    c={}
    for k,v in a.items():
        for l,w in b.items(): c[k+l]=c.get(k+l,F(0))+v*w
    return {k:v for k,v in c.items() if v}
cosh={1:F(1,2),-1:F(1,2)}
sinh={1:F(1,2),-1:F(-1,2)}
cosh2=mul(cosh,cosh)
Fprime={0:F(1,2),2:F(1,4),-2:F(1,4)}
assert Fprime == cosh2
derivative={k:k*v for k,v in cosh2.items() if k*v}
# Cross-multiplied identity (cosh²)'/cosh²=2tanh.
assert mul(derivative,cosh)==mul({k:2*v for k,v in sinh.items()},cosh2)
assert F(1,4) == F(1,3)/2 + F(2,3)/8
# The two atom weights cancel the unhalved-square factor exactly.
assert 2*F(1,2) == 1
print('PASS: primitive, clock envelope derivative, interpolation, loss weights')
```

Source hashes and actual execution evidence are recorded by the study's
coordinator when this candidate is frozen. These checks validate the
displayed identities; they do not replace a complete adversarial review
of the column-deletion and limit arguments.
