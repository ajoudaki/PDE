# Passive population sources and the precise finite-source obligation

Author component: `/root/source_alternative`, 2026-09-11. This is an author
proof candidate, awaiting independent scientific review. No established file
is changed. The result below proves the population off-support source estimate
on the complete fitted reference. It does **not** infer a finite-coordinate
moment estimate from second-moment convergence.

The model is the canonical two-hidden-layer tanh network, input
`x=sqrt(2)u`, `u in S1`, mean unhalved square loss, stored mobilities
`(n,1,n)`, and independent centered Gaussian initialization of variances
`(1,1/n,1/n²)`. The target finite theorem retains the actual finite
readout. The auxiliary feature-source graphs below have zero readout,
as in the maintained population-source construction; this file asserts
no replacement of the actual finite reference by those graphs.
The reference law is
`nu_*=1/2 delta_(sqrt(2)e1,+1)+1/2 delta_(sqrt(2)e2,-1)`.

The argument uses the complete maintained proofs in global-nonlinear B.1,
C.4, and C.4.5, and the Gaussian-program and action construction in
special-data III.F.1–9. The required extensions of the source rule to a
passive direction are derived here. No source/derivative rule is inferred
merely from the value theorem. Both mathematical skills, including the
research contract, evidence, adversarial-audit and proof-search references,
were used. Startup HEAD was `e111b632b5a6da7fe8ccf54eb6e286422f50af96`;
the shared index was empty, and unrelated dirty files were preserved.

## 1. Reference and the passive source statement

Write `phi=tanh`, `H_i=L²(Omega_i)`. The initialized middle action is
`A_0:H_1->H_2`, with its actual Hilbert adjoint and `||A_0||op<=2`.
It need not be Hilbert–Schmidt. Let `j_X=phi'(j)`, `j(0,g)=g`, and put

\[
 w_a(s)=j(X_a(s),g_a),\qquad H_a^1=\phi(w_a),\quad
 Z_a^2=AH_a^1,\quad H_a^2=\phi(Z_a^2),\quad
 \delta_a=c\phi'(Z_a^2),\quad Q_a=A^*\delta_a.
 \tag{S1}
\]

The feature equation, with `y_1=1,y_2=-1`, is

\[
 X_{a,s}=\tfrac12y_aQ_a,\qquad
 A_s=\tfrac12\sum_a y_a\delta_a\otimes H_a^1,\qquad
 c_s=\tfrac12\sum_a y_a H_a^2.                         \tag{S2}
\]

Its actual fitted endpoint is at `s=s_dagger<=S:=10`.
Global-nonlinear C.4.5.1 proves the strong reference, the physical clock
`s_t=2(1-b)`, and the bounds on this whole feature segment

\[
 \|c\|_2\le\sqrt {10},\quad \|c\|_\infty\le10,\quad
 \|A\|_{op}\le2+\sqrt {10},\quad
 \|w\|_2\le\sqrt2+\sqrt {10}.                         \tag{S3}
\]

For any passive direction define, from this same state,

\[
 H^1(s,u)=\phi(w(s)\cdot u),\quad Z^2(s,u)=AH^1(s,u),\quad
 \delta(s,u)=c\phi'(Z^2(s,u)),\quad Q(s,u)=A^*\delta(s,u).
 \tag{S4}
\]

**Passive source lemma.** On a compatible extension of the common Gaussian
source construction, for every `(s,u) in [0,s_dagger] x S1`,

\[
 Q(s,u)=\zeta(s,u)+D(s,u),\qquad |D(s,u)|\le B,
 \qquad B=225400e^{2880}+180.                             \tag{S5}
\]

The `zeta` family is centered jointly Gaussian, independent of the full
first-row root `(g_1,g_2)`, and

\[
 E[\zeta(s,u)\zeta(v,z)]=E_2[\delta(s,u)\delta(v,z)],
 \qquad E\zeta(s,u)^2\le10.                              \tag{S6}
\]

The bound in (S5) is an essential bound for each parameter pair and for
the countable parameter families used in the construction. We do not
need an assertion about a pointwise supremum over uncountably many pairs.
It gives all moments uniformly in the pair. The remainder is allowed to
depend on the root and the Gaussian sources; no independence of `D` is
asserted.

## 2. Derivation of the passive source rule

Use a separately fixed sufficiently fine feature Euler mesh with total
length at most `s_dagger`. The maintained HS version of B.1 and C.4.5.2
give, with strict slack for this unforced mesh,
`||A||op<7`, `||c||2<4`, and `||c(s_k)||infinity<=s_k`.
Let `gamma_jb=h_j y_b/2`. The active source recursion and its named-slot
derivative convention are C.4.5.2 (R5)–(R7): covariance entries,
expectations, learned-rank contractions and deterministic coefficients
are held fixed under a named source derivative.

At a target node `k`, append the two passive calls (S4), without making
an update from them. The initialized forward query is `H^1(s_k,u)` and
the initialized reverse query is `delta(s_k,u)`; learned increments are
expanded as their previous rank sums. The fixed Gaussian source rule gives

\[
 Z^2_{ku}=\xi_{ku}
 +\sum_{j<k,b}\left\{\alpha_{ku,jb}
       +\gamma_{jb}E_1[H^1_{ku}H^1_{jb}]\right\}\delta_{jb},
 \quad \alpha_{ku,jb}=E_1[\partial_{\zeta_{jb}}H^1_{ku}],
 \tag{S7}
\]

\[
 Q_{ku}=\zeta_{ku}
 +\sum_{j<k,b}\left\{\beta_{ku,jb}
       +\gamma_{jb}E_2[\delta_{ku}\delta_{jb}]\right\}H^1_{jb}
 +\beta_{ku,ku}H^1_{ku},
 \tag{S8}
\]

where `beta_ku,jb=E_2[partial_(xi_jb) delta_ku]` and
`beta_ku,ku=E_2[c_k phi''(Z^2_ku)]`. Any active forward slots at the
same node have coefficient zero: `c_k` depends only on earlier nodes,
and the appended passive upper expression (S7) contains only earlier
active deltas and its own new forward slot. Any active reverse slots
at that node likewise have coefficient zero in (S7), since the clocks
have not yet been updated. This explains all current-slot terms,
including when `u` equals an existing active direction. Singular or
duplicate query slots remain separate formal expressions; III.F.5
identifies their contracted source corrections without an inverse limit.

For completeness, the new coordinate instruction meets the same
source-rule extension as the active one. It is

\[
 H_u(X,g)=\phi\left(\sum_a u_a j(X_a,g_a)\right),\qquad
 \partial_{X_a}H_u=u_a\phi'(w\cdot u)\phi'(w_a).             \tag{S9}
\]

Thus `|partial_Xa H_u|<=|u_a|<=1`. Clip both root coordinates smoothly
at a fixed level before applying `j`, and clip the readout outside an
open neighborhood of `[-10,10]`. The identity
`j_g=phi'(j)/phi'(g)` makes all root derivatives bounded at a fixed
root clip. Every first named-source derivative in this finite graph has
a deterministic bound independent of root clip: (S9), the active
`H_X=sech^4 j`, bounded `phi'`, bounded `c phi''`, and finite linear
response sums are the entire derivative recursion. Root derivatives
are never taken in a named-source calculation.

Remove the root clip chronologically. Couple finite source vectors by
the positive square roots of their converging covariance matrices.
Continuity of these roots, also at rank loss, is proved in III.F.5.
The just-proved finite-graph derivative bounds imply convergence of
their expected derivatives by bounded convergence in probability;
bounded or at-most-linear value envelopes imply L² convergence of
values. This closes the induction for coefficients and values. At
finite width the direct change of the bounded first activation at a
fixed clock is at most twice the indicator that either root was
clipped. Its empirical squared mean tends to its Gaussian probability.
Same-root clock Lipschitz continuity from (S9) and the initialized
action bound propagate this error through the separately fixed graph.
Let width grow first and then remove the root clip. Thus (S7)–(S8)
describe the actual uncut fixed-program limits. This proof also applies
with a fresh Gaussian root inserted into one complete answer with a
coefficient epsilon; the same derivative bounds and covariance-root
coupling prove continuity of its coefficients as epsilon tends to zero.

## 3. Uniform coefficient bounds

For two reference-mesh states with the same roots use

\[
 d=x+a+z,\quad x=\sum_b\|X_b-\widetilde X_b\|_2,\quad
 a=\|A-\widetilde A\|_{op},\quad z=\|c-\widetilde c\|_2.
 \tag{S10}
\]

The same-root scalar contraction and `|u|=1` imply

\[
 \|H^1(u)-\widetilde H^1(u)\|_2\le x,\quad
 \|Z^2(u)-\widetilde Z^2(u)\|_2\le a+7x,
\]
\[
 \|\delta(u)-\widetilde\delta(u)\|_2
 \le z+2s(a+7x)\le Kd,\qquad K=140.                       \tag{S11}
\]

The same estimates hold for normalized finite arrays. C.4.5.2 derives
the active same-root stability coefficient `L(s)<=8+56s` and hence
`E=exp(8S+28S²)=exp(2880)` for subsequent mesh amplification. It also
derives the immediate state displacement from adding `epsilon e` to
one complete active forward answer:
`h_j P |epsilon| ||e||2`, with `P=(7+1)S+1/2=161/2`.
A complete active reverse pulse immediately displaces only one clock,
by `h_j |epsilon| ||e||2/2`. These estimates apply in the same strict
ball after first fixing the mesh and then taking epsilon small enough;
the readout supremum remains bounded by feature time because its
updates use only bounded tanh outputs.

Combine those pulse estimates with (S11). At a later passive node,
the forward pulse changes `delta_ku` by at most
`h_j P K E |epsilon| ||e||2`, and the reverse pulse changes `H^1_ku`
by at most `h_j E |epsilon| ||e||2/2`.
Here finite norms are divided by `sqrt(n)` as in C.4.5.2.

To extract the named derivatives, fix the mesh and nonzero epsilon,
then take the joint fixed-program width limit including the independent
standard Gaussian pulse root. In its own layer this root enters the
scalar expression only as `slot+epsilon e`; all selected coefficients
are held fixed under differentiation in this local root. Gaussian
integration by parts, conditional on the other roots and source groups,
gives `E[e V^epsilon]=epsilon E[partial_slot V^epsilon]`.
The unforced expression is independent of the unused root, so
`E[e V^0]=0`. The finite Cauchy–Schwarz pairing inequality and the
pulse bounds pass through joint second-moment convergence. Divide by
`|epsilon|`, and only afterwards use the zero-forcing derivative
continuity proved in Section 2. This gives

\[
 |\alpha_{ku,jb}|\le h_jE/2,\qquad
 |\beta_{ku,jb}|\le h_jPKE\quad(j<k),\qquad
 |\beta_{ku,ku}|\le2S.                                    \tag{S12}
\]

The integration by parts is legitimate because the finite scalar
expressions and derivatives in question are bounded for a fixed graph;
in particular `|H_u|<=1`, `|delta_u|<=S`. No derivative of a limiting
flow or a derivative transverse to an unforced singular support was
assumed.

The Gaussian sources of the passive calls have variances at most `1`
and `16` on the mesh. Since `|H^1|<=1`, `||delta||2<=4`, and
`sum_(j,b)|gamma_jb|<=S`, (S8) and (S12) imply

\[
 |Q_{ku}-\zeta_{ku}|
 \le 2SPKE+SC^2+2S
 =225400e^{2880}+180=B,
 \qquad C=4.                                             \tag{S13}
\]

The corresponding forward remainder has the bound `S²(E+1)` from
(S7). Constants are uniform in the passive direction, mesh length and
all sufficiently fine meshes; no positive Gram eigenvalue occurs.

## 4. Passage to the actual common reference and all-time weighted moments

Adjoin a countable refining mesh family and a dense countable circle
family to the common source construction. The cross-program covariance
identities give isometries
`||xi_H-xi_H'||2=||H-H'||2` and
`||zeta_delta-zeta_delta'||2=||delta-delta'||2`.
B.1's same-root clock/HS/readout convergence implies uniform L²
convergence of the passive `H`, `Z`, `delta`, and `Q` on compact
feature time and the whole circle: (S9), bounded actions and bounded
readout prove the relevant forward and reverse difference estimates.
The source isometry therefore gives convergence of `zeta`; subtraction
gives convergence of the remainder in L². A limit in L² of fields
bounded by `B` is bounded by `B` almost surely: choose a subsequence
with summable squared errors, apply Markov to each error threshold,
and take the resulting almost-sure limit. Gaussianity, the covariance
identity, and independence from the root pass in every finite tuple.
Then use strong continuity in time and input and the source isometry
to extend from the dense family. The variance bound improves to `10`
using (S3). This proves (S5)–(S6) on the actual common reference.

Let `G` denote a standard real normal and, for finite `p>=2`, put

\[
 k_p=\|G\|_p,\quad C_{g,p}=\|\cosh^2G\|_p,\quad
 M_p=B+\sqrt {10}\,k_p,\quad
 N_p=C_{g,p}M_p+S M_{2p}^2.                               \tag{S14}
\]

Every number is finite: `cosh²G<=exp(2|G|)`, and Gaussian exponential
moments follow by completing the square. In particular
`C_(g,2)^2=(3+4 exp(2)+exp(8))/8`.
Equations (S5)–(S6) imply, uniformly over `(s,u)`,

\[
 \|Q(s,u)\|_p\le M_p,\qquad
 \|X_a(s)\|_p\le\tfrac S2 M_p.                           \tag{S15}
\]

The second estimate integrates (S2) and uses the integral triangle
inequality; Fubini applies since the first bound makes the time integral
absolutely integrable in every indicated Lp.
With `F(z)=z/2+sinh(2z)/4`, the exact scalar identity
`F(w_a)=F(g_a)+X_a` gives

\[
 {d\over dX}\cosh^2j(X,g)=2\tanh j(X,g),\qquad
 \cosh^2w_a\le\cosh^2g_a+2|X_a|.                         \tag{S16}
\]

Consequently

\[
 \sup_{s,u}\|\cosh^2w_a(s)Q(s,u)\|_p\le N_p.             \tag{S17}
\]

Indeed the `cosh²g_a` term times `zeta(s,u)` has Lp norm at most
`C_(g,p) sqrt(10) k_p`, by independence in (S6); its product with `D`
has norm at most `C_(g,p) B`. The remaining term is bounded by
`2||X_a||_(2p)||Q||_(2p)<=S M_(2p)^2` using Hölder and (S15).
This accounts for all dependencies, including possible dependence
between `X`, `Q` and `D`. Likewise `|w_a|<=|g_a|+|X_a|` gives

\[
 \sup_{s,u}\||w(s)|Q(s,u)\|_p
 \le 2k_pM_p+S M_{2p}^2.                                 \tag{S18}
\]

These bounds extend to every physical time because its feature clock
stays in `[0,s_dagger)`. Their constants have no dependence on a
physical horizon `T` or on a perturbing law.

## 5. Admissible forcing and its bound

Use the tangent Hilbert space

\[
 \mathcal H=L^2(\Omega_1;\mathbb R^2)
       \oplus\mathcal S_2(H_1,H_2)\oplus H_2.
 \tag{S19}
\]

The first block is the clock variation
`xi_a=delta w_a/phi'(w_a)`; thus its ordinary Hilbert norm is precisely
the reference-weighted tangent norm in the question. Define

\[
 q(s,u)=\left(
  (u_a\cosh^2w_a\,\phi'(w\cdot u)Q(u))_{a=1,2},
  \delta(u)\otimes H^1(u),\ \phi(Z^2(u))\right).            \tag{S20}
\]

This is a strongly continuous `mathcal H`-valued function of `(s,u)`.
Here are the product details. The raw and clock reference curves and
the passive `Q` fields are jointly L² continuous by their bounded
actions and readout supremum. The map `X -> cosh²j(X,g)` is 2-Lipschitz
by (S16), so that factor is L² continuous. Products converge in
probability. Their uniform Lp bounds for any fixed `p>2`, supplied by
(S17), make their squares uniformly integrable: the second moment
outside magnitude `R` is at most `N_p^p/R^(p-2)`. Splitting into that
tail and a bounded set proves L² convergence of each product.
Bounded gate multiplication then uses the same truncation argument.
The middle block is continuous in HS norm by its rank-one difference
identity; the last is L² continuous by Lipschitz tanh.

Using (S3), (S17), and the rank norm identity,

\[
 \sup_{s,u}\|q(s,u)\|_{\mathcal H}
 \le C_q:=\sqrt{N_2^2+11}.                               \tag{S21}
\]

Here the first-block squared norm is at most
`sum_a u_a² N_2²=N_2²`, since the direction is a unit vector.
For any finite signed Borel measure `sigma` on `S1 x [-Y,Y]`, including
nonatomic measures, the map

\[
 b_\sigma(t)=-2\int(f_*(t,u)-y)q(s(t),u)\,d\sigma(u,y)
 \tag{S22}
\]

is a strongly continuous Bochner integral in `mathcal H` and satisfies

\[
 \sup_{t\ge0}\|b_\sigma(t)\|_{\mathcal H}
 \le B_Y\|\sigma\|_{TV},\qquad
 B_Y=2(\sqrt {10}+Y)C_q.                                  \tag{S23}
\]

For the integral, the compact parameter domain has a continuous image,
therefore a separable bounded image, in the Hilbert space; integration
against the total variation measure is consequently legitimate.
Continuity in time follows by uniform continuity on each compact time
interval and the total-variation integral bound. Equation (S23) uses
`|f_*|<=sqrt(10)`. It needs no finite support, atom-weight lower bound,
Gram inverse, or regular conditional distribution of labels.
Zero total mass is not needed to define this linear operator; it is
imposed when interpreting it as a probability-law direction.

If an independently proved homogeneous propagator bound is
`sup_(0<=r<=t)||U(t,r)||<=C_U`, variation of constants immediately
gives `sup_(t<=T)||v_sigma(t)||<=C_U B_Y T ||sigma||TV`.
This last implication is conditional on that propagator theorem;
the source result (S23) itself is unconditional on the constructed
reference. The output derivative functional has norm below 17 by
(S3) and the raw prediction-gradient estimate; the clock-to-raw first
variation map is a contraction. Hence its corresponding whole-circle
prediction bound is `17 C_U B_Y T ||sigma||TV` under the same condition.

## 6. What can and cannot replace the actual finite-source estimate

The population proof above does not supply finite-coordinate higher
moments by itself. B.1 transfers joint W2 laws and quadratic moments;
the unbounded product `cosh²w_a Q(u)` has higher growth and is not one
of those measurements. A deterministic illustration shows the missing
implication. On a probability space choose events `E_n` of probability
`n^-4`, and put `X_n=Q_n=n 1_(E_n)`. Then both converge to zero in L²,
while `||X_n Q_n||2=1` for every n. This is a counterexample to a
proposed inference from two L² limits, not a network counterexample.

For finite capture, a sufficient statement weaker than coordinate-supremum
moments is uniform integrability in probability of the **actual finite**
weighted source tails. For the clipped source used in FINITE_CAPTURE,
it is enough that, for each fixed perturbing law and each fixed T,

\[
 \lim_{R\to\infty}\limsup_{n\to\infty}
 \Pr\left\{\int_0^T\!\int
  \|q_n(t,u)-q_{n,R}(t,u)\|_{\mathcal H_n}
  \,d|\sigma|(u,y)dt>a\right\}=0\quad(a>0).                \tag{S24}
\]

Indeed the difference between the exact and clipped finite tangent
equations has zero initial value, the same bounded compact-time
generator, and a forcing difference bounded by
`2(C_T+Y) integral ||q_n-q_n,R|| d|sigma|`. Iterating its integral
inequality gives uniform state error at most
`2(C_T+Y)exp(C_T T)` times the double integral in (S24).
Thus an integrated estimate suffices for the primary finite state
capture, although extra observation equicontinuity still needs its
own justified bounds. The stronger finite F13 in FINITE_CAPTURE is
one possible way to obtain both requirements.

Neither an L² source limit, a population higher moment, nor a bounded
homogeneous propagator establishes (S24). The separate actual finite
source proof must supply it, for example by a valid column-deletion
argument. This file leaves that finite obligation explicitly open and
does not assert that the primary milestone is resolved by (S23).

## 7. Check record and status

The coefficient arithmetic is exact:
`2*10*(161/2)*140=225400`, `10*16+2*10=180`, and
`8*10+28*10²=2880`. The inverse-gate derivative in (S16) and the
Gaussian `cosh^4` expectation were independently checked algebraically.
No training experiment, sweep, Monte Carlo check, raw-GD derivative
claim, or promotion is part of this component.

| Claim | Status and exact scope |
|---|---|
| Passive source extension (S5)–(S6) | Author proof candidate on the actual population feature segment; constants uniform in input |
| Inverse-gate weighted moments (S17)–(S18) | Derived from that source extension; uniform in all physical time |
| Bochner forcing and TV bound (S22)–(S23) | Derived; arbitrary finite signed Borel laws and bounded labels |
| L² limits alone imply weighted-product convergence | Refuted by the displayed abstract counterexample |
| Actual finite weighted source convergence | Not proved in this component; (S24) records a weaker sufficient estimate |
| Full primary derivative-capture theorem | Depends on actual finite source control and the other study components |

Independent reviews must inspect the full maintained probability and
reference dependencies together with this proof. The all-time forcing
constant uses the certified `s_dagger<=10`, hence indirectly the fixed
reference lower bound `m>=1/10`; it has no conditioning dependence on
the perturbing law, its support, atom weights, or input Gram.
