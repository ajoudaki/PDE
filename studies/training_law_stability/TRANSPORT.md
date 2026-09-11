# Coupled-law comparison in the full first-row state

This proof unit supplies a deterministic comparison estimate, its quantitative
consequences for reference flows with Gaussian tails, and continuity of the
averaged displacement observables. It does not independently construct the
Gaussian action spaces or prove a finite-width identification theorem. Those
obligations are in the other proof units of this study. All statements below
use the actual two-hidden-layer tanh network and its matrix adjoint.

## 1. State, finite interpretation, and exact field

Write `u=x/sqrt(2)`, so `|u|=1`, and put `phi=tanh`. Let
`H_1=L2(Omega_1)` and `H_2=L2(Omega_2)` be real probability Hilbert spaces
with their coordinate operations. A population state is

\[
 \theta=(w,A,c)\in L^2(\Omega_1;\mathbb R^2)
       \times\mathcal B(H_1,H_2)\times H_2.
\]

The vector field preserves the affine class `A=A_0+K` where `K` is a
norm-limit of finite-rank operators: the rank-one integrand in (T2) is
continuous on the compact data support, so finite simple approximations
converge in operator norm, as do their time integrals. Define

\[
\begin{aligned}
 Z^1_\theta(u)&=w\cdot u,& H^1_\theta(u)&=\phi(Z^1_\theta(u)),\\
 Z^2_\theta(u)&=A H^1_\theta(u),& H^2_\theta(u)&=\phi(Z^2_\theta(u)),\\
 f_\theta(u)&=\langle c,H^2_\theta(u)\rangle_{H_2},&
 r_\theta(u,y)&=f_\theta(u)-y,\\
 P^2_\theta(u)&=c,&\delta^2_\theta(u)&=\phi'(Z^2_\theta(u))c,\\
 P^1_\theta(u)&=A^*\delta^2_\theta(u),&
 \delta^1_\theta(u)&=\phi'(Z^1_\theta(u))P^1_\theta(u).
\end{aligned}                                                   \tag{T1}
\]

All pairings use a single neuron population. The population rank-one
operator is `(a tensor b)v=a E_1[bv]`. For a probability law `mu` of `(u,y)`
on `S^1 x [-Y,Y]`, the exact mean-square-loss physical vector field is

\[
 F_\mu(\theta)=\left(
 -2\int r_\theta\delta^1_\theta u\,d\mu,
 -2\int r_\theta\delta^2_\theta\otimes H^1_\theta\,d\mu,
 -2\int r_\theta H^2_\theta\,d\mu\right).                         \tag{T2}
\]

In the first integral the scalar field multiplies the explicit input
vector `u`, producing a two-component row. For a finite network, take
`w=W^(1)`, `A=W^(2)`, `c=W^(3)`, replace field norms by the Euclidean or
Frobenius norm divided by `sqrt(n)`, inner products by `a^T b/n`, and
rank-one actions by `a b^T/n`. Formula (T2) then gives exactly the raw
stored-weight mobilities `(n,1,n)`, as follows from
`docs/finite_dynamics.md` §§1–2. Raw GD is
`theta_(j+1)=theta_j+eta F_mu(theta_j)` with all three blocks evaluated at
the preceding state. Parameter interpolation does not interpolate hidden
features: (T1) is recomputed at the interpolated parameters.

On a common carrier define

\[
 D(\theta,\bar\theta)=\|w-\bar w\|_{L^2(\mathbb R^2)}
                  +\|A-\bar A\|_{\rm op}+\|c-\bar c\|_2.       \tag{T3}
\]

Its finite version is exactly the full-first-matrix distance requested in
the research contract. No cross-width or finite-to-population operator
distance is used anywhere in this proof.

The bound `|phi|<=1`, `|phi'|<=1`, and `Lip(phi')<=2` will be used throughout.
If every individual state norm is at most `B>=1`, then, for every input,

\[
 \|H^1\|_2,\|H^2\|_2\le1,\quad
 \|\delta^2\|_2\le B,\quad \|P^1\|_2,\|\delta^1\|_2\le B^2,
 \quad |f|\le B,\quad |r|\le B+Y.                                \tag{T4}
\]

Consequently the sum of the three velocity norms is at most
`V=2(B+Y)(B^2+B+1)`. If initial individual norms are at most `S_0`, choose
`B=2S_0+2` and

\[
 T_{\rm ball}=\min\{1,(B-S_0)/(4V)\}>0.                          \tag{T5}
\]

The integral-flow first-exit argument and the sum of Euler increments show
that both stay inside this ball up to `2T_ball` for Euler mesh at most
`T_ball`: before a putative first exit the increment of each norm is at most
`2T_ball V<(B-S_0)`. Piecewise affine interpolants have speed bounded by
`V`. These bounds hold for every probability law and every finite empirical
law, regardless of its cardinality.

For the specified initialization, `||W^(1)_0||_F^2/n` tends in probability
to `2`, and `||W^(3)_0||_2^2/n` has expectation `n^(-2)`. The initialized
middle operator is bounded with probability tending to one by the elementary
sphere-net argument in finite dynamics §4. Thus a fixed `S_0` gives a common
high-probability finite ball, independent of the training data. The population
root is the full row `w_0=(g_1,g_2)` with independent standard normals and
`c_0=0`. Retaining the second root coordinate remains necessary even if a
reference training law sees only the first coordinate.

## 2. The one-reference transport estimate

For a field `P`, write `tau_R(P)=||P 1_{|P|>R}||_2`. If the reference
state is `bar theta`, set

\[
 \mathfrak T_{\nu,R}(\bar\theta)
 =\tau_R(\bar c)+\int\tau_R(P^1_{\bar\theta}(u'))\,
                                  \nu(du',dy').                    \tag{T6}
\]

At finite width these are individual empirical neuron RMS tails. In
particular, for a finite reference law with weights `omega_b`, the second
term is the weighted sum of the individual reference tails, not a tail of a
maximum over the reference inputs or over the actual dataset.

**Transport lemma.** On the ball above, for every `R>=1`, every two laws
`mu,nu`, and every two states on the same carrier,

\[
 \|F_\mu(\theta)-F_\nu(\bar\theta)\|_{T3}
 \le C(1+R)\bigl(D(\theta,\bar\theta)+\mathcal W_1(\mu,\nu)\bigr)
       +C\mathfrak T_{\nu,R}(\bar\theta).                           \tag{T7}
\]

Here `W1` uses `|u-u'|+|y-y'|`, and `C` depends only on `B,Y`. The same
constant works for the normalized finite-network norms and actions. Only
the reference state requires tails.

**Proof.** Fix any coupling `pi` of the two laws, and abbreviate
`h=|u-u'|`, `D=D(theta,bar theta)`. Keeping the full first row gives

\[
 \|Z^1_\theta(u)-Z^1_{\bar\theta}(u')\|_2
 \le\|w-\bar w\|_2+\|\bar w\|_2 h\le D+Bh.
\]

The activation is 1-Lipschitz. Expanding
`A H^1-bar A bar H^1=(A-bar A)H^1+bar A(H^1-bar H^1)` therefore gives

\[
 \max_{\ell=1,2}\bigl(\|Z^\ell_\theta(u)-Z^\ell_{\bar\theta}(u')\|_2
          +\|H^\ell_\theta(u)-H^\ell_{\bar\theta}(u')\|_2\bigr)
       \le C(D+h),                                                   \tag{T8}
\]
\[
 |f_\theta(u)-f_{\bar\theta}(u')|\le C(D+h),\qquad
 |r_\theta(u,y)-r_{\bar\theta}(u',y')|
                         \le C(D+h)+|y-y'|.                         \tag{T9}
\]

For any two preactivations and any reference field `bar P`, pointwise
splitting at `|bar P|=R` gives

\[
 \|[\phi'(Z)-\phi'(\bar Z)]\bar P\|_2
       \le2R\|Z-\bar Z\|_2+2\tau_R(\bar P).                        \tag{T10}
\]

For the top backward field, split its difference as
`phi'(Z^2)(c-bar c)+[phi'(Z^2)-phi'(bar Z^2)]bar c`. Thus

\[
 \|\delta^2_\theta(u)-\delta^2_{\bar\theta}(u')\|_2
       \le C(1+R)(D+h)+2\tau_R(\bar c).                             \tag{T11}
\]

Expanding the adjoint difference, and using (T4), bounds the corresponding
`P^1` difference by `B` times (T11) plus `BD`. Split the first backward
field in the same way, now applying (T10) to `P^1_bar theta(u')`. The result is

\[
 \|\delta^1_\theta(u)-\delta^1_{\bar\theta}(u')\|_2
 \le C(1+R)(D+h)
       +C\tau_R(\bar c)+2\tau_R(P^1_{\bar\theta}(u')).                \tag{T12}
\]

There is one power of `R`: the earlier backward error is multiplied only
by a bounded operator and bounded activation derivative. The new gate
cutoff adds an `R` term and does not multiply that earlier error by `R`.

For the first-weight integral the exact decomposition is

\[
\begin{aligned}
 r\delta^1u-\bar r\bar\delta^1u'
  &=(r-\bar r)\delta^1u
    +\bar r(\delta^1-\bar\delta^1)u
    +\bar r\bar\delta^1(u-u').
\end{aligned}
\]

The row-field norm of a product `P u` equals `||P||_2 |u|`. Therefore
(T4), (T9), and (T12) bound this difference by
`C(1+R)(D+h+|y-y'|)` plus the two reference tails. This verifies the
explicit changing-input factor in the first-weight gradient.

For the middle integral use the identity

\[
 r\delta^2\otimes H^1-\bar r\bar\delta^2\otimes\bar H^1
 =(r-\bar r)\delta^2\otimes H^1
 +\bar r(\delta^2-\bar\delta^2)\otimes H^1
 +\bar r\bar\delta^2\otimes(H^1-\bar H^1)
\]

and `||a tensor b||_op=||a||_2||b||_2`. Equations (T4), (T8), (T9),
and (T11) give the same bound. The readout integral uses
`rH^2-bar r bar H^2=(r-bar r)H^2+bar r(H^2-bar H^2)` and needs no tail.
Integrate these three estimates against `pi`. Every tail depends only
on the second marginal, so its integral is exactly (T6). Taking the
infimum of the coupling costs proves (T7); existence of an optimal
coupling is unnecessary. All the norm inequalities also hold under the
finite normalized pairings, proving the finite assertion. ∎

The full Gaussian first-row root is not multiplied by a backward field
in this argument. It enters (T8) only through its RMS norm. In particular,
no unproved Gaussian estimate for products of root and backward fields,
no Gaussian maximum over observations, and no Gram inverse is hidden in
(T7).

## 3. Reference tails and the quantitative modulus

For fixed finite reference laws the established C.2 response lemma proves,
on a common time interval `T_response>0`,

\[
 \sup_{t\le T_{\rm response}}\max_b
 E\exp(c_0|P^1_{\bar\theta(t)}(u_b)|^2)\le C_0,
 \qquad \sup_t E\exp(c_0|\bar c(t)|^2)\le C_0.                       \tag{T13}
\]

Its full weighted response proof is in `docs/global_nonlinear.md` C.2:
the current application has depth two, `|G_ab|<=1`, weights summing to
one, tanh with the three displayed derivative bounds, full independent
Gaussian first roots, zero readout, Gaussian middle matrix, and the
RMS/residual bounds (T4). These verify every bound parameter of that lemma;
its constants are independent of the number and sizes of atom weights.
The named-source rule is supplied by A.2 and its contained III.F.1–III.F.7
dependencies in `docs/special_data_limits.md`. Both orientations are retained.
Arbitrary step sizes of bounded total time and affine Euler-state evaluations
are explicitly included in C.2. The full-row fields are obtained by their
exact row update (T2); passive first directions do not change any trained
preactivation or source recurrence.

The tail implication is elementary: for a constant depending on `c_0`,
`s^2 1_{|s|>R} <= C exp(c_0 s^2) exp(-c_0 R^2/2)`. Taking expectation
and square roots in (T13) yields

\[
 \sup_{t\le T_*}\mathfrak T_{\nu,R}(\bar\theta(t))
                  \le C e^{-cR^2},\qquad
 T_*\le\min(T_{\rm ball},T_{\rm response}).                         \tag{T14}
\]

For an input-population reference the sufficient hypothesis is exactly
the integrated bound (T14). No assertion about exponential tails uniformly
over a continuum of inputs, or about a supremum over time inside a random
tail, is needed. Its passage from finite-law references is proved with the
strong state construction in `POPULATION.md`.

Let `theta(t),bar theta(t)` be strong flows with laws `mu,nu`, common
initial state, and a reference satisfying (T14). Integrating (T7) and
applying the elementary integral Gronwall inequality gives

\[
 \sup_{t\le T_*}D(\theta(t),\bar\theta(t))
 \le C e^{aR}\left((1+R)q+e^{-cR^2}\right),
 \qquad q=\mathcal W_1(\mu,\nu),\ R\ge1.                            \tag{T15}
\]

For completeness, if `d(t)<=b+L int_0^t d(s)ds`, define
`v(t)=b+L int_0^t d(s)ds`; then `v'(t)<=Lv(t)` and
`e^(-Lt)v(t)<=b`. Here `b=CT_*[(1+R)q+e^(-cR^2)]` and
`L=C(1+R)`, which proves (T15) after enlarging constants. Unequal
initial states add their distance inside the parentheses.

For `0<q<=1` put `s=log(e/q)>=1` and choose
`R=max(1,c^(-1/2)) sqrt(s)`. Then `e^(-cR^2)<=e^(-s)=q/e`, and
`1+R<=C exp(C sqrt(s))`. Consequently

\[
 \sup_{t\le T_*}D(\theta(t),\bar\theta(t))
           \le Cq\exp\!\left(C\sqrt{\log(e/q)}\right).              \tag{T16}
\]

The uniform prediction conclusion follows from (T8)–(T9) with `u=u'`.
For `q=0`, let `R` tend to infinity in (T15); the right side tends to
zero, giving equality of states and predictions. For `q>1`, the a priori
bound gives `D<=6B` and `sup_u|f-bar f|<=2B`; the asserted local modulus
is not evaluated at a negative logarithm. All admissible distances are
at most `2+2Y`.

The same argument applies to differently meshed Euler interpolants or a
finite proxy with velocity defect. If the grid states differ from their
interpolated states by at most `V eta` and `V Delta`, and the reference
velocity defect is at most `epsilon` in the sum norm, (T15) becomes

\[
 \sup_{t\le T_*}D(\theta(t),\bar\theta(t))
 \le C e^{aR}\left[D(\theta(0),\bar\theta(0))
 +(1+R)(q+\eta+\Delta)+\epsilon
 +\int_0^{T_*}\mathfrak T_{\nu,R}(\bar\theta_{\rm grid}(s))ds\right].
                                                                    \tag{T17}
\]

This formulation needs only integrated reference tails. A fixed number of
reference proxy grid states can have a common defect tending to zero in
probability. Such a finite-program identification is an input to (T17),
not a conclusion from deterministic stability. Taking width limits with
the reference law, cutoff, and coarse mesh fixed is therefore legitimate;
using a growing Gaussian program without a separate estimate would not be.

## 4. Strong continuity and averaged representation displacement

The maps in (T1) are jointly continuous in `(theta,u)` into their field
spaces on every ball. For the unbounded backward multiplier the needed
fact is: if `Z_j->Z` and `P_j->P` in `L2`, then
`phi'(Z_j)P_j->phi'(Z)P` in `L2`. Subtract the changing `P_j` first.
For the remaining term restrict to `|P|<=M`, use the Lipschitz bound
on `phi'`, then bound the complement by `2 tau_M(P)` and send `M`
to infinity. The argument is uniform on compact sets of states and
inputs by continuity and a finite subcover. Hence the integrands in (T2)
are continuous functions of data and states into their respective Banach
spaces. They are Bochner integrable: their ranges on the compact data
support are compact and therefore separable, and (T4) bounds their norms.

Fix the common initial state `theta_0`. For either hidden preactivations
or activations, write `V_theta^ell(u)` for that field and define

\[
 J_\ell(\theta,\mu)
   =\int\|V_\theta^\ell(u)-V_{\theta_0}^\ell(u)\|_2^2\,\mu(du,dy).
                                                                    \tag{T18}
\]

This is a mean-square displacement averaged over the training-input law;
its RMS is `sqrt(J_ell)`. Initial and current individual norms are bounded
by fixed constants on the ball. Equations (T8) for both current and initial
states imply, with any coupling of `(u,y)` and `(u',y')`,

\[
 \left|\|V_\theta^\ell(u)-V_{\theta_0}^\ell(u)\|_2^2
       -\|V_{\bar\theta}^\ell(u')-V_{\theta_0}^\ell(u')\|_2^2\right|
                       \le C(D(\theta,\bar\theta)+|u-u'|).
\]

Indeed use `|a^2-b^2|<= (a+b)|a-b|` for the two field norms and the
triangle inequality for their difference. Integrate and minimize the
coupling cost to obtain

\[
 |J_\ell(\theta,\mu)-J_\ell(\bar\theta,\nu)|
                 \le C\bigl(D(\theta,\bar\theta)+\mathcal W_1(\mu,\nu)\bigr).
                                                                    \tag{T19}
\]

Combined with (T16), this is quantitative continuity of the squared
displacement at any fixed time. A reference law with `J_ell>0` for both
layers therefore has an open `W1` neighborhood retaining positive margins.
Its reference activity still needs the actual-flow C.3 argument, provided
in `NONLAZY.md`; this continuity lemma by itself makes no activity claim.

## 5. Checks and precise dependencies

The proof covers coincident inputs, singular canonical Grams, atomic laws,
vanishing atom weights after deleting zero-mass atoms, arbitrary joint
input-label correlations, and zero labels. For a zero-signal stationary
reference, no positive displacement is inferred. The input metric is exactly
the requested cost after `u=x/sqrt(2)`. Every field estimate is in normalized
RMS or an actual operator norm on one carrier.

The transport lemma (T7), the conditional reference-flow comparison
(T15)–(T17), continuity, and the displacement estimate (T19) have complete
arguments here. The quantitative law theorem additionally requires the
constructed common carrier, strong distribution-driven flows, and inherited
integrated reference tails. The simultaneous algorithm theorem additionally
requires the fixed-oracle identification and its ordered approximation
limits. These dependencies are kept explicit and are not renamed assumptions
of the requested final result. No finite-width quantitative replacement rate
or claim about expected absolute generalization gaps is made.
