# Population spectral approximation and hidden activity: independent candidate

Status: candidate theoretical derivation, not independently reviewed, not a
milestone or promotion claim. Author: the independently scoped `population_route`
agent. Date: 2026-09-12. No experiments, numerical eigenvalue calculations, Git
writes, or reads of other attempts were performed.

The useful result is a local population oracle inequality for the actual
nonlinear constrained evolution. Its approximation floor is an endpoint
spectral tail of the prescribed target, with an explicit Fourier truncation
bound. The new structural step is injectivity of a continuum endpoint
middle-gradient operator. It does **not** give a positive spectral gap on the
infinite-dimensional function space. A robust subfamily inside the frozen
class has strictly positive unseen-risk improvement and paired upper-hidden
activation displacement during a common finite episode.

The population inequalities below are conditional on the continuum constrained
flow being constructed on a common interval with the original-model equation
specified below. This attempt does not claim that C.4.9's stated one-atom
continuation/capture theorem already supplies that continuum construction.
Original-mixture continuation, empirical sampling, a sample-based stopping
rule, and the ordered finite-GF bridge remain outside this route.

## 1. Inputs, contract, and exact dependency boundary

Scientific inputs actually read:

- The frozen class/model contract in this study's README.
- `docs/NOTATION.md` completely.
- `docs/global_nonlinear.md` C.4.9 completely, including A-supplement.4.
- The same book, C.4.5.1 sections 1–3 (full reference construction,
  symmetry, endpoint); C.4.5.2 section 1; C.4.6.3 sections 1–6 (complete
  cavity, Gaussian maximum, and population-envelope proofs through S45);
  and A.1–A.4 completely.
- `docs/special_data_limits.md` III.F completely, after the supervisor
  expressly supplied that dependency scope. A truncated read of III.F.5–7
  was repaired by a separate read.

Process inputs: AGENTS.md, RESEARCH_WORKFLOW.md, the rigorous-math and
conjecture-investigation skills, and the latter's research-contract,
proof-search, evidence-ledger, and adversarial-audit references. Scoped reading
replaced ordinary author startup. No web scientific inputs were used.

At the pre-write metadata check, HEAD was
`b14dc38bdca0c7835685e768e6ca0657d60cf10d`, the index was empty, and unrelated
working changes were present and left untouched. Read-input SHA-256 values:

| Input | SHA-256 |
| --- | --- |
| global_nonlinear.md | `7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465` |
| NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| README.md | `e74b04e95b4363a32dc887c244dbdf0370418f2c98770a98decff48d89358956` |
| special_data_limits.md | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |

Keep the frozen two-hidden-layer tanh model, Gaussian initialization,
mobilities, raw Hilbert metric, physical GF, whole circle, exact anchor
weights, and actual reused action/adjoint. Write normalized inputs
`u(alpha)=(cos(alpha),sin(alpha))`, normalized arc measure `rho`, and
`F(alpha)=F_*(sqrt(2)u(alpha))`. The endpoint state is `theta_dagger`.

The input density is `p`, `1/2<=p<=2`, with Lipschitz constant at most `D`.
The target remains

\[
 q=q_0+\sin^2(2\alpha)v,\quad q_0=\cos^3\alpha-\sin^3\alpha,
 \qquad \sum_{k\ge0}(2k+1)^s(|a_k|+|b_k|)\le R\le1/8,
 \quad s\ge1.
\]

Finite series and absolutely convergent infinite series are both included.
Target coefficients never depend on a trained predictor. Endpoint spectral
coordinates used for analysis below do not alter these coefficients or the
training dynamics.

For a reached state define `g_theta`, `G_theta`, `M_theta`, and `Pi_theta`
exactly as in C.4.9.NS2. Set

\[
 D_\theta(u)=\Pi_\theta g_\theta(u),\qquad
 T_{\theta,p}a=\int a(u)D_\theta(u)p(u)\,d\rho(u).
 \tag{P1}
\]

The required continuum equation is

\[
 \theta'=-2T_{\theta,p}(f_\theta-q),\qquad
 \theta(0)=\theta_\dagger.
 \tag{P2}
\]

Its coefficients use the current nonlinear state. Conditionally centered
noise disappears from this population equation because `g_theta(X)` depends
only on `X` and the state, so `E[xi g_theta(X)]=0`. The target risk is

\[
 E(\tau)=\int(f_{\theta(\tau)}-q)^2p\,d\rho.
 \tag{P3}
\]

Both `f_theta` and `q` are odd under `alpha -> alpha+pi`.
`H1,H2,g_theta,D_theta` are odd; `delta=c phi'(Z2)` is even. Thus all
population forces and risks are unchanged when `p` is replaced by

\[
 p_e(\alpha)=\tfrac12[p(\alpha)+p(\alpha+\pi)].
 \tag{P4}
\]

This is an exact symmetry reduction of integrals, not a change to the data
law. Below use `p_e` in the function-space inner product, and abbreviate it
by `p` when no confusion arises. It is still a probability density between
1/2 and 2 with the same Lipschitz bound.

On a sufficiently small raw ball of radius `rho_a>0`, C.4.9.B.2–B.3 gives
anchor invertibility and fixed endpoint constants

\[
 \sup_u\|g_\theta(u)\|\le L_1,\quad
 \sup_u|f_\theta(u)-F(u)|\le C_f d,\quad
 \sup_u\|D_\theta(u)-D_\dagger(u)\|\le C_d\sqrt d,
 \qquad d=\|\theta-\theta_\dagger\|_{\rm raw}\le\rho_a\le1.
 \tag{P5}
\]

The B.3 proof is uniform over all circle queries, although B's learning
application selects a small one-atom rectangle. Its projector depends only
on the two anchors. Therefore its estimates apply here unchanged. One may
use B.3's displayed constants and
`rho_a=min(1,(kappa/(2a_M))^2)`. With `C=sqrt(10)` from the endpoint bounds,
the actual velocity satisfies

\[
 \|\theta'\|\le V:=2(C+2)L_1,
 \qquad d(\tau)\le V\tau
 \tag{P6}
\]

until first exit. The residual bound is `|f_theta-q|<=C+2`, because the
unit raw ball has `||c||_2<=C+1` and `|q|<=1`. A common existence interval
and `VT<=rho_a/2` ensure by first exit that all arguments stay in the ball.

## 2. Continuum first-feature separation

**Lemma 1.** Let `zeta` be a finite odd signed Borel measure on the circle.
If

\[
 \int\tanh(w_\dagger\cdot u(\alpha))\,d\zeta(\alpha)=0
 \quad\hbox{in }L^2(\Omega_1),
 \tag{P7}
\]

then `zeta=0`.

This is stronger than finite-list independence and needs an additional
argument; no continuum coercivity is inferred from finite Gram matrices.

**Proof.** The endpoint protected-row estimate from C.4.9.B.2 is sufficient.
Here is also a way to obtain precisely its needed envelope without using a
random supremum over passive queries. Let `F_cl'=cosh^2` denote the scalar
first-row clock primitive. Along the reference feature interval,

\[
 F_{cl}(w_a(s))-F_{cl}(g_a)=X_a(s),\qquad
 X_a(s)=\tfrac12y_a\int_0^s Q_a(v)\,dv.
\]

C.4.9.A's reference-flow source bound gives
`sup_(s,a)||Q_a(s)||_r<=C_Q sqrt(r)` for every `r>=2`.
Consequently, by Minkowski and `s_dagger<=10`,

\[
 N=\tfrac12\sum_{a=1}^2\int_0^{s_\dagger}|Q_a(s)|\,ds,
 \quad \|N\|_r\le10C_Q\sqrt r,\quad
 \sup_s|X_a(s)|\le N\quad\hbox{almost surely}.
 \tag{P8}
\]

Fubini supplies the last statement for the absolutely continuous active
clocks. The constant `C_Q` may instead be obtained from C.4.6.S40–S44.
No independence of `N` and `g` is needed. Markov with
`r=(z/(e C_N))^2` gives
`Pr(N>z)<=exp[-z^2/(e^2 C_N^2)]` once that exponent uses `r>=2`.

Fix a vector `v` with nonzero coordinates. The Gaussian box
`|g-tv|_infinity<=1` has probability at least
`(2/pi)exp[-(t|v|+sqrt(2))^2/2]`. For large `t` this exceeds
`Pr(N>t^2)`. Its intersection with `N<=t^2` therefore has positive
probability. On the intersection `|g_a|>=c_v t`, and the minimum of
`F_cl'` on `[g_a-1,g_a+1]` exceeds `exp(2(|g_a|-1))/4`.
Since this is greater than `t^2`, monotonicity first puts `w_a` in that
unit interval and then gives

\[
 |w_{\dagger,a}-g_a|\le4t^2e^{-2(|g_a|-1)}\longrightarrow0.
 \tag{P9}
\]

Choose one point from each positive-probability intersection outside the
null set in (P7). At those points, `w_dagger/t -> v`. If neither
perpendicular direction to `v` is an atom of `|zeta|`, dominated convergence
against the finite variation measure yields

\[
 S(\beta):=\int\operatorname{sign}(\cos(\alpha-\beta))
                    \,d\zeta(\alpha)=0,
 \qquad v/|v|=u(\beta).
 \tag{P10}
\]

A finite measure has at most countably many atoms. The restrictions on `v`
exclude only a null set of angles. Thus `S=0` almost everywhere. For the
kernel `s(t)=sign(cos t)`, direct integration gives its complex Fourier
coefficients

\[
 \widehat s(m)=\frac{2\sin(m\pi/2)}{\pi m}\quad(m\ne0),
 \qquad \widehat s(0)=0.
 \tag{P11}
\]

In particular they are nonzero for every odd integer. Fubini is valid
because the kernel is bounded and `zeta` has finite variation. It shows
`widehat S(m)=widehat s(m) widehat zeta(m)` (up to the immaterial consistent
sign convention, since `s` is even). Oddness of `zeta` already annihilates
all even Fourier coefficients, including zero. Thus every Fourier
coefficient of `zeta` vanishes.

For completeness this implies zero measure as follows. The Fejer kernels
`K_M(t)=|sum_(k=0)^M exp(ikt)|^2/(M+1)` are nonnegative, have integral one
against `rho`, and their mass outside any fixed neighborhood of zero tends
to zero, by
`K_M(t)<=1/((M+1)sin^2(t/2))`. Uniform continuity then proves
`K_M*h -> h` uniformly for every continuous circle function `h`.
These convolutions are trigonometric polynomials, so their integrals
against `zeta` vanish. Passing to the uniform limit gives `int h dzeta=0`
for every continuous `h`. Approximation of interval indicators from inside
and outside at non-atomic endpoints gives zero mass on a generating algebra
of arcs; finite additivity and continuity of finite signed measures give
`zeta=0`. This proves the lemma.

## 3. Injective continuum middle gradient; compact spectrum

Let `H_p` be the real Hilbert space of odd functions in `L2(p_e rho)`.
Write `T_p=T_(theta_dagger,p_e)`.

**Lemma 2.** The map `a -> (T_p a)_K`, where the subscript denotes only
the Hilbert–Schmidt middle increment block, is injective on `H_p`.
Consequently `T_p` and its combined hidden block are injective.

**Proof.** Put

\[
 U=\int a(u)g_\dagger(u)p_e(u)d\rho(u),\qquad
 \beta=M_\dagger^{-1}G_\dagger^*U.
\]

If `(T_p a)_K=0`, then

\[
 \int a(u)p_e(u)\delta_\dagger(u)\otimes H^1_\dagger(u)\,d\rho(u)
 =\sum_{b=1}^2\beta_b\delta_\dagger(e_b)\otimes H^1_\dagger(e_b).
 \tag{P12}
\]

The tensor kernel identifies these Hilbert–Schmidt operators with elements
of `L2(Omega2 x Omega1)`: verify first on finite tensor sums by expanding
their squared norms, then use completion. Joint measurable representatives
exist from the continuous maps into `L2`; one can construct them by limits
of circle step functions. Since `|delta_dagger|<=10`, and `a` is `L1`,
the kernel integral is well defined and Fubini applies. For almost every
second-layer coordinate `z`, (P12) says in `L2(Omega1)` that the first
features annihilate the measure

\[
 d\eta_z=a(u)p_e(u)\delta_\dagger(u,z)d\rho(u)
             -\sum_{b=1}^2\beta_b\delta_\dagger(e_b,z)\delta_{e_b}.
\]

Its odd part has density `a p_e delta_dagger` and atoms
`-(1/2)sum_b beta_b delta_dagger(e_b,z)(delta_(e_b)-delta_(-e_b))`.
Even measures integrate to zero against `H1`, so Lemma 1 makes that odd
part zero. Its absolutely continuous and atomic parts are mutually
singular. In particular

\[
 a(u)p_e(u)c_\dagger(z)\operatorname{sech}^2 Z^2_\dagger(u,z)=0
 \quad\hbox{for almost every }(u,z).
 \tag{P13}
\]

The endpoint readout is nonzero because it fits the first anchor. For
almost every coordinate where `c_dagger!=0`, the preactivation is finite
for almost every circle input, so the gate is strictly positive there.
Fubini and `p_e>=1/2` therefore imply `a=0`. This proves the claim without
assuming injectivity of the trained action.

**Lemma 3.** `A_p=T_p^*T_p` is compact, positive, self-adjoint and injective
on `H_p`. It has an orthonormal basis `(e_j)` of eigenfunctions with
eigenvalues `lambda_1>=lambda_2>=...>0` tending to zero.

The map `u -> D_dagger(u)` is continuous into the raw Hilbert space and
uniformly bounded by `L0<17`, by C.4.9.B.3. Approximate it uniformly by
finitely valued circle step functions. The resulting maps approximating
`T_p` have finite-dimensional ranges, with operator error at most the
uniform approximation error, by Cauchy–Schwarz and `int p_e=1`. Thus `T_p`
is compact; the other operator properties follow from its definition
and Lemma 2.

Here are the needed spectral theorem details. For a nonzero positive
compact self-adjoint operator `A`, let
`lambda=sup_(||x||=1)<Ax,x>`. Positivity and the discriminant inequality
give `|<Ax,y>|^2<=<Ax,x><Ay,y>`, hence `||A||=lambda>0`.
For a maximizing sequence `(x_n)`,
`||(A-lambda I)x_n||^2<=2lambda(lambda-<Ax_n,x_n>)->0`.
Compactness of `(Ax_n)` gives a convergent subsequence of `(x_n)` and a
unit eigenvector of eigenvalue `lambda`. Repeat on its orthogonal
complement, which is invariant by self-adjointness. If the resulting
positive eigenvalues did not tend to zero, the images of their orthonormal
eigenvectors would have no convergent subsequence, contradicting compactness.
On the orthogonal complement of all selected vectors the operator norm is
at most every remaining maximal eigenvalue, and hence zero. Injectivity
makes that complement zero. Infinite dimension and injectivity rule out
finite termination. This proves precisely the decomposition used below.

The explicit failure of continuum uniform coercivity is now visible:
`||T_p e_j||^2=lambda_j->0`, although `||e_j||_p=1`.
This is a proof-route obstruction to a uniform all-mode PL bound, not a
counterexample to learning the compact target class.

## 4. Nonlinear spectral oracle inequality

Define the endpoint spectral projection `P_J` onto `e_1,...,e_J`, and

\[
 r_0=F-q,\qquad b_J(p,q)=\|(I-P_J)r_0\|_p.
 \tag{P14}
\]

These are fully determined by the established endpoint, the input density,
and the prescribed target. They use neither the future trajectory nor an
eigenbasis of an evolving unknown operator. They are analysis quantities,
not coefficients supplied to (P2).

**Proposition 4 (conditional only on continuum flow existence).** Suppose
the strong actual constrained equation (P2) exists on `[0,tau_ex]` in the
source-regular reached class. For `J>=1`, choose `T>0` such that

\[
 T\le\tau_{ex},\qquad VT\le\rho_a/2,\qquad
 4C_d^2VT\le\lambda_J.
 \tag{P15}
\]

Then throughout `[0,T]`, with the actual evolving features and projection,

\[
 E(\tau)\le e^{-\lambda_J\tau}E(0)
      +2\{b_J(p,q)+C_fVT\}^2(1-e^{-\lambda_J\tau}).
 \tag{P16}
\]

**Proof.** Scalar gradient continuity and the strong curve chain rule from
C.4.9.B.3 justify differentiation under the circle integral: on the compact
time/input set the scalar gradients and velocity are bounded and continuous.
The orthogonal projection identity gives the exact energy law

\[
 E'=-4\|T_{\theta,p}r_\theta\|^2,
 \qquad r_\theta=f_\theta-q.
 \tag{P17}
\]

Anchor derivatives are zero since `G_theta^* Pi_theta=0`. Thus all residuals
remain odd and belong to `H_p`. From (P5),

\[
 \|(T_{\theta,p}-T_p)a\|\le C_d\sqrt d\,\|a\|_p,
 \quad
 \|(I-P_J)r_\theta\|_p\le b_J+C_fd.
 \tag{P18}
\]

Orthogonality of the eigenbasis yields

\[
 \|T_pr_\theta\|^2
   =\sum_j\lambda_j|\langle r_\theta,e_j\rangle_p|^2
   \ge\lambda_J\{E-\|(I-P_J)r_\theta\|_p^2\}.
 \tag{P19}
\]

For Hilbert vectors `x,y`,
`||x+y||^2 >= (1/2)||x||^2-||y||^2`, since subtracting the right side
leaves `(1/2)||x+2y||^2`. Apply this with `x=T_p r_theta` and
`y=(T_(theta,p)-T_p)r_theta`. By (P18)–(P19) and (P15),

\[
 \|T_{\theta,p}r_\theta\|^2
 \ge\left(\frac{\lambda_J}{2}-C_d^2d\right)E
           -\frac{\lambda_J}{2}(b_J+C_fd)^2
 \ge\frac{\lambda_J}{4}E
           -\frac{\lambda_J}{2}(b_J+C_fVT)^2.
\]

Substitute into (P17), multiply the resulting differential inequality by
`exp(lambda_J tau)`, and integrate. This gives (P16).

For every `q` with `E(0)>0`, completeness of the eigenbasis gives
`b_J->0`. Choose a finite `J` with `b_J<=sqrt(E(0))/4`, and then decrease
the positive `T` so that additionally `C_fVT<=sqrt(E(0))/4`. The floor
in (P16) is then at most `E(0)/2`, proving strict population improvement
for every positive time up to `T`. This is not an arbitrary-accuracy result
at a fixed positive horizon: the permissible time depends on `lambda_J`.

### Explicit dependence on the frozen Fourier target complexity

Let `v_N` retain indices `0,...,N` and let
`q_N=q_0+sin^2(2alpha)v_N`. Weighted absolute summability gives

\[
 \|q-q_N\|_\infty\le\frac{R}{(2N+3)^s},\qquad
 b_J(p,q)\le\|(I-P_J)(F-q_N)\|_p+\frac{R}{(2N+3)^s}.
 \tag{P20}
\]

The second inequality uses that `I-P_J` is an orthogonal contraction and
`p_e rho` is a probability measure. For a finite target, the tail is
exactly zero once its last coefficient is retained. Every term involving
`q_N` is an explicit finite linear combination of the specified Fourier
coefficients and the fixed endpoint spectral projections. Equations
(P15)–(P16) and (P20) form a target-dependent approximation/oracle bound.
At a fixed admitted `T`, one can minimize its right side over the indices
`J,N` satisfying (P15); this changes only the reported bound.

The spectrum need not align with Fourier modes. Replacing `P_J` by a
Fourier projection and applying finite-dimensional Gram positivity directly
would leave an uncontrolled cancellation with omitted modes. This is why
the spectral projection is used in the inequality while Fourier truncation
controls the independently prescribed target family.

There is also a bound uniform over the entire frozen coefficient ball at a
fixed input density. Put
`psi_(k,c)=sin^2(2alpha)cos((2k+1)alpha)` and define `psi_(k,s)` with sine.
Then

\[
 b_J(p,q)\le B_{J,R,s}(p):=
 \|(I-P_J)(F-q_0)\|_p+R\eta_{J,s}(p),
\]
\[
 \eta_{J,s}(p)=\sup_{k\ge0,\,b\in\{c,s\}}
       \frac{\|(I-P_J)\psi_{k,b}\|_p}{(2k+1)^s}.
 \tag{P20a}
\]

Indeed apply the triangle inequality to the absolutely convergent series
and then the weighted coefficient bound. Every `psi` has norm at most one.
For every finite `K`,

\[
 \eta_{J,s}(p)\le\max\left\{
  \max_{k\le K,\,b\in\{c,s\}}
       \frac{\|(I-P_J)\psi_{k,b}\|_p}{(2k+1)^s},
                     (2K+3)^{-s}\right\}.
 \tag{P20b}
\]

At fixed `K`, all finitely many projected tails tend to zero as `J` grows;
then send `K` to infinity. Thus `B_(J,R,s)(p)->0`. Replacing `b_J` by
`B_(J,R,s)` in (P16) gives a declared floor bounded solely from the frozen
coefficient class, the input law, and the reference quantities. It requires
no optimization over target-dependent future trajectories. No uniform rate
in `J` or a practical cost for calculating the endpoint spectrum is claimed.

## 5. Robust subfamily with strict unseen risk and paired hidden change

Assume `0<R<=1/8` and put `a=R/4`. Inside the frozen family choose

\[
 q=q_0+\sin^2(2\alpha)\{a(\cos\alpha+\sin\alpha)+w(\alpha)\},
 \qquad
 \sum_k(2k+1)^s(|w_{a,k}|+|w_{b,k}|)\le a/4.
 \tag{P21}
\]

The total coefficient budget is at most `2a+a/4=9R/16<R`; there is room
for perturbations in independently varying odd Fourier modes. Allow every
input density in the original `D`-Lipschitz class and every admissible
centered-noise law. For finite series interpret the condition in its finite
coefficient space; its relative interior is nonempty. The infinite-series
closure is also allowed. No support restriction or density concentration
has been introduced.

The endpoint obeys `F(pi/2-alpha)=-F(alpha)`, by the fully read reference
symmetry proof C.4.5.1.R7. The same is true of `q_0`. The function
`psi=sin^2(2alpha)(cos alpha+sin alpha)` is symmetric under that swap.
Direct integration gives

\[
 \|\psi\|_\rho^2
 =\int\sin^4(2\alpha)(1+\sin2\alpha)d\rho=3/8.
\]

The odd power integrates to zero by a shift of `pi/2`; the fourth-power
mean is `3/8` from expanding `(1-cos4alpha)^2/4`. The symmetric part of
the `w` perturbation has `L2(rho)` norm at most `||w||_infinity<=a/4`.
Orthogonal projection onto swap-symmetric functions therefore gives

\[
 \|F-q\|_\rho\ge a(\sqrt{3/8}-1/4),\qquad
 E(0)\ge E_*:=\frac{a^2}{2}(\sqrt{3/8}-1/4)^2>0.
 \tag{P22}
\]

This target choice uses a known symmetry, not an endpoint-fitted target.

The density class is compact in the uniform norm: boundedness and the
common Lipschitz estimate give finite uniform nets by sampling a fine
circle grid, and uniform limits preserve all constraints. The coefficient
class in (P21) is compact in the uniform target norm: for every `N` its
first finitely many coefficients range over a compact set, and its omitted
series has uniform bound `(a/4)/(2N+3)^s`. A diagonal subsequence followed
by this tail bound gives uniform convergence, and finite partial weighted
sums show the limit satisfies the original bound. Thus the combined
`(p,q)` family, denoted `C_rob`, is compact.

Define endpoint quantities

\[
 U_{p,q}=\int(F-q)g_\dagger p\,d\rho,\quad
 \beta_{p,q}=M_\dagger^{-1}G_\dagger^*U_{p,q},\quad
 d_{p,q}=\Pi_\dagger U_{p,q},\qquad
 \gamma_*:=\min_{(p,q)\in C_{rob}}\|(d_{p,q})_K\|_{HS}^2.
 \tag{P23}
\]

Uniformly bounded `g_dagger` makes all displayed maps continuous under
uniform convergence of `(p,q)`. By Lemma 2 and (P22), the minimized
quantity is positive at every point. Compactness therefore proves
`gamma_*>0`. This is a precise deterministic endpoint constant, analogous
to C.4.9.B's unevaluated Gram minimum, and is not a numerically evaluated
rate. Its dependence is only on the fixed model and `D,R,s`.

For each `(p,q)` keep `r_0` and `beta` fixed and define the hidden-only
contrast

\[
 O_{p,q}(\theta)
 =\int r_0(u)\langle c_\dagger,H^2_\theta(u)\rangle p(u)d\rho(u)
   -\sum_{b=1}^2\beta_b\langle c_\dagger,H^2_\theta(e_b)\rangle.
 \tag{P24}
\]

It depends on current hidden features, with the readout in the observation
held at the known endpoint. Its gradient at the endpoint is
`o_dagger=((d_(p,q))_hidden,0)`. The same strong scalar chain rule as
C.4.9.B.4 applies under the integral, so along the actual (P2)

\[
 O'(0)=-2\|(d_{p,q})_{hidden}\|^2\le-2\gamma_*.
 \tag{P25}
\]

Here are sufficient uniform quantitative continuation constants. Let

\[
 R_0^{max}=(C+1)^2,\quad
 S_*:=\sup_{C_{rob}}\{\|r_0\|_{L^1(p)}+|\beta_1|+|\beta_2|\}<\infty,
\]
\[
 B_d=L_1C_f+C_d\sqrt{R_0^{max}},\quad
 B_V=2B_d,\quad
 A_H=S_*C_gV+L_0\sqrt{R_0^{max}}B_V.
 \tag{P26}
\]

All are computable from the already specified endpoint bounds; for example
`|beta|<=||M_dagger^-1|| ||G_dagger|| L0 sqrt(R_0^max)` bounds `S_*`.
The endpoint gradient modulus (P5) and its fixed-readout hidden version
from C.4.9.B.4 imply, for `d<=rho_a`,

\[
 \|T_{\theta,p}r_\theta-d_{p,q}\|\le B_d\sqrt d,
 \quad \|V_{p,q}(\theta)-V_{p,q}(\theta_\dagger)\|\le B_V\sqrt d,
\]
\[
 \|o_{p,q}(\theta)-o_{p,q}(\theta_\dagger)\|
      \le S_*C_g\sqrt d,
 \quad |O'_{p,q}(\theta)-O'_{p,q}(\theta_\dagger)|\le A_H\sqrt d.
 \tag{P27}
\]

For the first line subtract the residual first, costing
`L1 C_f d`, and then subtract `D`, costing `C_d sqrt(d)||r0||_p`.
For the last line use the preceding fixed-readout gradient bound,
`||V||<=V`, and `||o_dagger||<=L0 sqrt(R_0^max)`.

Assume now that continuum construction provides a common positive
existence interval over `C_rob`. Choose a common positive `T_rob` with

\[
 T_{rob}\le\tau_{ex},\qquad
 VT_{rob}\le\min\{\rho_a/2,\gamma_* /(4B_d^2),
                                      (\gamma_*/A_H)^2\}.
 \tag{P28}
\]

Then `||T_(theta,p)r_theta||>=sqrt(gamma_*)/2` and
`O'<=-gamma_*` throughout this whole episode. Integrating (P17) gives

\[
 E(0)-E(\tau)\ge\gamma_*\tau\quad(0\le\tau\le T_{rob}).
 \tag{P29}
\]

To convert the hidden contrast into actual upper-hidden activation motion,
define the paired observable on the same initialized carrier

\[
 J_2(\tau)=\frac13\left\{
   \int\|H^2_{\theta(\tau)}(u)-H^2_\dagger(u)\|_2^2p(u)d\rho(u)
   +\sum_{b=1}^2\|H^2_{\theta(\tau)}(e_b)-H^2_\dagger(e_b)\|_2^2
                         \right\}.
 \tag{P30}
\]

Cauchy–Schwarz first in `Omega2`, then in the direct sum of the
`L2(p rho)` coefficient space and the two anchor coefficients, yields

\[
 |O(\theta(\tau))-O(\theta_\dagger)|^2
 \le3\|c_\dagger\|_2^2(E(0)+|\beta|^2)J_2(\tau).
\]

With `B_*^2=sup_(C_rob)(E(0)+|beta|^2)<infinity`,

\[
 J_2(\tau)\ge\frac{\gamma_*^2\tau^2}{3C^2B_*^2}>0
 \qquad(0<\tau\le T_{rob}).
 \tag{P31}
\]

This is actual second-hidden activation displacement, not merely a nonzero
hidden parameter block. The derivative sign persists along the nonlinear
flow by (P27)–(P28). The continuum term measures genuinely unseen circle
inputs. The two anchors are included in the observable because the
constraint correction in the exact hidden contrast includes them.

A specified population stopping choice on this robust family is half the
minimum of the four positive upper bounds on `T_rob` in (P28), with the
common `tau_ex` supplied by the continuum construction. These constants
depend only on `D,R,s` and the fixed reference. It is therefore a
predetermined stop, independent of the realized observations or unknown
target coefficients; after capture its physical counterpart is
`t_stop=T_rob/epsilon`. This is an available theoretical stopping choice
with unevaluated endpoint constants. A data-adaptive or numerically
certified implementation of the stop has not been established here.

At `R=0`, the chosen robust subfamily is unavailable. The spectral oracle
inequality still applies to `q=q0`, but this route does not prove
`F!=q0`. It makes no unconditional strict-improvement assertion in that
degenerate target-diversity case.

## 6. Adversarial checks and precise remaining obligations

| Proposed implication | Check/outcome |
| --- | --- |
| Finite Gram positivity implies continuum coercivity | Rejected. Lemmas 1–2 independently prove injectivity; Lemma 3 proves the uniform infinite-mode gap is zero. |
| The middle action must be injective | Not used. Strict positivity of the tanh gate and continuum first-feature separation suffice. |
| A protected Gaussian event must be independent of the learned displacement | Not used. The Gaussian box probability dominates the envelope-tail probability; a union bound gives a positive intersection. |
| A signed density might cancel anchor multipliers | Ruled out in Lemma 2 by uniqueness of its odd measure and mutual singularity of its density and four anchor atoms. |
| Nonuniform density could hide the symmetric target component | The original lower bound `p>=1/2` preserves (P22). Symmetrization is an exact integral identity only. |
| Centered noise might bias the population force | Its conditional expectation vanishes exactly. No empirical-noise claim is inferred. |
| The spectral argument freezes training features | It does not. (P17) is the actual nonlinear energy identity; (P18) explicitly bounds the moving operator. |
| A Fourier tail rate alone proves a useful contraction rate | Rejected. The endpoint spectrum also enters, and no lower eigenvalue rate is proved. |
| Nonzero hidden parameter velocity proves activation motion | Not used as the conclusion. (P24)–(P31) prove a finite activation-displacement margin by an actual hidden contrast. |
| The target was chosen from the trained predictor | The robust family is specified by fixed Fourier coefficients and the known swap symmetry, before any learning comparison. |
| Arbitrary accuracy on a fixed episode follows as J grows | Not claimed; the allowed time in (P15) can shrink with the eigenvalue. |
| Existing one-atom capture automatically covers this class | Not claimed. This is the central external-to-route bridge still required. |

Remaining work before a milestone claim:

1. Construct (P2), uniformly over the required continuum laws and finite
   empirical laws, from full retained reference histories, and establish
   original-fixed-mixture continuation and capture at `t=tau/epsilon`.
   Finite-atom positivity alone supplies none of this law extension.
2. Establish sampling and centered-noise estimates for the selected paths,
   together with an available stopping rule. The quantities `q`, `p`, and
   `b_J` in this population theorem are not an empirical stopping rule.
3. Transfer the population conclusions and the paired observable through
   actual finite GF, with width first for every fixed positive epsilon,
   epsilon second, and sample size last.
4. Independently audit this frozen candidate, especially the signed-measure
   first-feature separation, the Hilbert–Schmidt/Fubini passage, and the
   nonlinear spectral constants. No separate checker has yet reconstructed
   this route.

Route recommendation: retain as a concrete population candidate for comparison
with the independent continuation and statistical routes. Its strongest
unconditional new assertion is endpoint continuum injectivity and the
associated compact spectral structure. Its strongest conditional assertion
is (P16), with (P20), plus the robust margins (P29) and (P31).
