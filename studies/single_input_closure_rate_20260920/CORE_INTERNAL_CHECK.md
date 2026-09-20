# Internal check of the fixed-core obstruction

Verdict: PASS as a diagnostic for the specified polynomial-core-only hierarchy.
No material gap found. This is an independent internal check, not a promotion
review, and it does not establish or refute an order-to-error rate for the
maintained H3 hierarchy with its growing bounded-word prefix.

Reviewed input: `CORE_OBSTRUCTION.md`, SHA256
`21e9b0804525d30d64f7b20dc217db147b3db8c5f26653e1d735ae90b96b0bff`.
The reviewer did not author that file. The permitted supporting sources were
the same study's README and maintained `docs/global_nonlinear.md`, especially
the exact source rule (3.5), C.4.7.8 (H6), B.1, C.4.5.1's feature argument,
and C.4.7.10.B's H3 dictionary/filter construction. The reviewer separately
derived the single-input dynamics before receiving this candidate; the frozen
`ROUTE_DYNAMICS.md` has SHA256
`f84da8b5a840079a239ae8b2ffd4c12359f8abab08f27d831e0534f2ac2fa755`.
No other route or study was read. No numerical experiment or Git action was
performed.

## 1. Exact object and scope checked

The target is the canonical population flow for one normalized training input
`e1`, label `+1`, with the full first row `(g1,g2)`, zero limiting readout,
bounded initialized Gaussian action `A0`, and its actual adjoint. The physical
loss is unhalved, with the prescribed mobilities. The comparator increases
only the Chebyshev polynomial degree of the *fixed* H3 core and uses the H3
ridge `eta_N=1/[1024(N+1)^2]`; its bounded-word prefix is not allowed to grow.

This distinction is essential. The maintained H3 scheme appends all bounded
valid word codes through order `N`. It eventually sees new action queries,
whereas the comparator remains confined to fixed generated sigma-fields.
The candidate consistently restricts its negative conclusion to the latter.

## 2. Gaussian source and actual-adjoint check

Use the candidate's notation

\[
 h_i=\tanh g_i,\quad Y_i=A_0h_i,\quad H_i=\tanh Y_i,
 \quad p_i=A_0^*H_i,
\]
\[
 q=\mathbb Eh_1^2>0,\quad v=\mathbb EH_1^2>0,
 \quad \alpha=\mathbb E\operatorname{sech}^2Y_1.
\]

The two forward inputs are independent centered fields, so their uncentered
Gram is `q I`. The exact initial forward answers are therefore independent
`N(0,q)` coordinates. These are initial finite-program queries, not a claim
that trained action answers remain Gaussian.

For the two reverse calls, the source rule (H6) gives

\[
 p_i=\zeta_i+\alpha h_i,
 \qquad (\zeta_1,\zeta_2)\sim N(0,vI),
\]

with this reverse source vector independent of the original first-row roots.
The response term is required by reuse of the same action: it is
`h_j E[partial_(Y_j) H_i]=alpha h_i`. Both `g2` and the second reverse probe
remain in the retained information; neither is dropped in the obstruction.

Because tanh is a Borel bijection onto `(-1,1)`, the polynomial core has
completed generated sigma-fields

\[
 \mathcal G_1=\sigma(g_1,g_2,\zeta_1,\zeta_2),\qquad
 \mathcal G_2=\sigma(Y_1,Y_2).
\]

Now set `d=H1(1-H1^2)`. Its named source derivatives satisfy
`partial_(Y_2)d=0` and
`partial_(Y_1)d=(1-H1^2)(1-3H1^2)`. Appending `A0* d` therefore gives

\[
 A_0^*d=\zeta_d+b h_1,
 \qquad b=\mathbb E[(1-H_1^2)(1-3H_1^2)].
\]

The new source has variance `E d^2`, covariance `E[d H_i]` with `zeta_i`,
and is jointly Gaussian with them independently of `g`. Symmetry and
independence give `E[d H2]=0`. Put

\[
 \lambda=\frac{\mathbb E[dH_1]}{v},\qquad
 \xi=\zeta_d-\lambda\zeta_1,
 \qquad\omega=\mathbb Ed^2-\frac{(\mathbb E[dH_1])^2}{v}.
\]

Gaussian covariance subtraction shows that `xi` is independent of both old
reverse sources and of `g`, hence independent of the entire retained lower
sigma-field. The conditional expectation identity is exactly

\[
 P_1A_0^*d=\lambda\zeta_1+b h_1,\qquad
 A_0^*d-P_1A_0^*d=\xi.                                  \tag{C1}
\]

Strict Cauchy–Schwarz gives `omega>0`. Equality would imply `d=lambda H1`
almost surely; off the probability-zero event `H1=0`, this would make
`1-H1^2` constant. The continuous nondegenerate law of `H1` contradicts that.

Adversarial alternative checked: an incorrectly independent adjoint or a
response-only transpose would change (C1). The candidate uses neither.
It retains the response `b h1` and the correct covariance with the previously
seen reverse source. The omitted part is only the orthogonal Gaussian
innovation after conditioning on the complete fixed core.

## 3. Projection and hidden-gradient check

Let `P_l=E[·|G_l]` on the full canonical carrier, and `B=P2 A0 P1`. Then
`B*=P1 A0* P2`; this is the actual adjoint of the compressed action. Since
`h1` and `Y1` belong to their respective retained spaces,
`B h1=P2 Y1=Y1`. Thus the initialized training first and second hidden
fields agree. The limiting readout is zero in both systems.

The projected flow remains inside its generated spaces: every coordinate
gate preserves measurability, `B` and `B*` map between the retained spaces,
and each constrained middle increment has both factors there. Its middle
gradient is consequently the same rank as the unconstrained gradient whenever
its two factors are retained. This verifies the projected model used by the
candidate, rather than merely assigning it a formal action.

At initialization the scalar directional differential of the upper training
feature is

\[
 J_0(a,C)=\operatorname{sech}^2Y_1
 [C h_1+A_0(\operatorname{sech}^2g_1\,a)].
\]

The row direction has only its first coordinate; the second coordinate is
stationary. In the row-`L2` plus middle-HS metric,

\[
 J_0^*H_1=(\operatorname{sech}^2g_1 A_0^*d, d\otimes h_1).
\]

For the projected model the first component uses `P1 A0* d`, while the
rank component stays `d tensor h1` because `P2 d=d` and `P1 h1=h1`.
By (C1), the cross term with `xi` vanishes conditionally on `G1`. Also
`E[xi^2|G1]=omega`. Hence

\[
 \|J_0^*H_1\|^2-\|J_{B,0}^*H_1\|^2
 =\omega\,\mathbb E\operatorname{sech}^4g_1=:D>0.          \tag{C2}
\]

Plain orthogonality alone would not identify the weighted square as
`omega E sech^4(g1)`; independence does, and was verified above. The candidate
has this stronger property, so there is no hidden weighted-projection gap.

## 4. Finite-order expansion check

The transformed single-input integral equation gives a global feature flow
for either initialized bounded action. On bounded feature intervals,
`||c(s)||_infty<=s`, `||K(s)||HS<=s^2/2`, and `||A(s)||<=2+s^2/2`.
The first-layer coordinate satisfies `w1=j(X,g1)`, where `j_X=sech^2(j)`;
this makes the transformed field Lipschitz in `L2(X)+HS(K)+L2(c)` with
bounded readout supremum. Thus the strong curves used in the candidate exist.

The candidate's difference quotients suffice and do not assume threefold
Frechet differentiability of a Nemytskii map on `L2`:

1. Since `c_s=h` and `h(s)->H1` in `L2`, `c(s)/s->H1` in `L2`, with
   `|c(s)/s|<=1` pointwise.
2. Consequently `delta2(s)/s->d` in `L2`. Bounded action continuity gives
   `A(s)*delta2(s)/s->A0* d` in `L2`.
3. Multiplying by the changing bounded lower gate preserves this limit.
   The multiplier converges in probability, so its product with each fixed
   square-integrable vector converges in `L2`: truncate that vector, use
   boundedness on the truncated part, and then remove its `L2` tail.
4. The rank-one difference estimate also gives
   `K_s(s)/s->d tensor h1` in HS. Integration yields
   `hidden(s)=hidden(0)+(s^2/2)J0*H1+o_L2+HS(s^2)`.
5. For a scalar map with bounded continuous derivative, if
   `(z(s)-z0)/s^2->a` in `L2`, then the mean-value integral and the same
   bounded-multiplier argument give
   `(phi(z(s))-phi(z0))/s^2->phi'(z0)a` in `L2`.
   The operator product cross term is controlled by its HS norm times its
   vector `L2` norm. Applying this through the two hidden activations gives
   `h(s)=H1+(s^2/2)J0 J0*H1+o_L2(s^2)`.

Integrating the last identity yields

\[
 c(s)=sH_1+\frac{s^3}{6}J_0J_0^*H_1+o_{L^2}(s^3).
\]

Pairing this with the expansion of `h(s)` produces

\[
 f(s)=v s+
 \left(\frac12+\frac16\right)
 \langle H_1,J_0J_0^*H_1\rangle s^3+o(s^3)
 =v s+\frac23\|J_0^*H_1\|^2s^3+o(s^3).                 \tag{C3}
\]

The projected model satisfies the same derivation with its own initialized
action. Thus the feature-time difference is `(2/3)D s^3+o(s^3)`. All required
variables are square integrable; the only unbounded new reverse field is a
Gaussian source plus a bounded response and is acted on by bounded gates.
No positive Taylor radius or interchange of width and time derivatives is
used.

## 5. Physical-time coefficient and observable separation

Both physical clocks solve `s_t=2(1-f(s))`, starting at zero. Their right-hand
sides are locally Lipschitz near zero and equal `2` at zero, so
`s(t)=2t+O(t^2)` and the same holds for `s_B(t)`.
By (C3), the two feature predictions differ by `O(s^3)`. Subtracting the
clock equations therefore gives, on a fixed sufficiently short interval,

\[
 |s(t)-s_B(t)|
 \le C\int_0^t|s(a)-s_B(a)|\,da+C\int_0^t a^3\,da.
\]

Integrating the scalar inequality gives `|s-s_B|=O(t^4)`. The clock mismatch
therefore contributes only `O(t^4)` to the prediction. Substituting
`s(t)=2t+O(t^2)` into the cubic feature difference proves the candidate's
coefficient and sign:

\[
 f(t,e_1)-f_B(t,e_1)=\frac{16}{3}D t^3+o(t^3)>0          \tag{C4}
\]

for all sufficiently small positive physical times. Thus this is an error
at identical physical times and at the very same training input, not a
loss-matched or passive-only distinction.

The result provides an explicit positive leading coefficient `D`, but not a
numerically certified duration on which a specified lower error holds. Its
qualitative nonconvergence conclusion only needs one sufficiently small fixed
positive time, so such a duration is not a missing premise for that conclusion.

## 6. Polynomial-core limit check

The core laws have positive densities on their open cubes: `(g,p)` has a
positive density since `p=zeta+alpha tanh(g)` with nondegenerate independent
Gaussian `zeta`; the coordinatewise tanh map is a diffeomorphism. The upper
core follows from the nondegenerate forward Gaussian pair.

Polynomials are dense in the two core `L2` spaces. One fully specified route
is to truncate to a compact interior box, approximate indicator rectangles by
continuous ramps whose boundary strips have vanishing measure, approximate
simple functions, and then apply multivariate Bernstein approximation on the
closed cube. The total-degree Chebyshev products span those polynomials.

For every fixed retained polynomial coefficient vector `a`, zero padding
keeps its Euclidean norm unchanged at larger orders, and

\[
 \|(I-Q_N)S_Na\|_2\le\frac{\sqrt{\eta_N}}2\|a\|
 \longrightarrow0.
\]

Contraction and density give strong convergence to the identity on the core
space. Since every retained basis field is core measurable,
`Q_N=Q_N P_l`, and hence `Q_N->P_l` strongly on the full carrier. This verifies
the stronger full-carrier statement needed to obtain

\[
 B_N=Q_{2,N}A_0Q_{1,N}\longrightarrow P_2A_0P_1=B,
 \qquad B_N^*\longrightarrow B^*                         \tag{C5}
\]

strongly in both orientations. This does not assert operator-norm convergence.

To identify the dynamical limit, the reference must be the *projected* flow.
Its compact exact path produces the three defects

\[
 \sup_{s,u}\|(B_N-B)H_B^1(s,u)\|_2,
 \quad\sup_s\|(B_N^*-B^*)\delta_B(s)\|_2,
\]
\[
 \sup_s\|Q_{2,N}(K_B)_sQ_{1,N}-(K_B)_s\|_{HS}.
\]

The first two tend to zero by (C5), uniformity on compact `L2` sets, and
continuity of the fields. The third tends to zero by finite-rank approximation
and a finite time net, since `(K_B)_s=P2(K_B)_sP1` and the derivative is a
continuous HS curve. These are precisely the sources for subtracting the
transformed single-input equations. The common bounds on action and readout
supremum make their propagation Lipschitz, yielding a vanishing state and
output error on every fixed feature interval. No omitted Gaussian-tail bound
is needed in this transformed comparison.

Physical-clock convergence then follows on every separately fixed short
physical interval from the same scalar Lipschitz comparison used above.
Thus the polynomial-core-only flows converge to `f_B`, as claimed. The
conditional expectation projection does not disappear with degree, and no
source relative to the *unprojected* target was assumed to vanish.

## 7. Exact consequence and boundaries

For every requested physical horizon `T>0`, choose a fixed `t0` with
`0<t0<=T` small enough for (C4). If `f_N^core` denotes the degree-only flow,
the proved projected limit implies

\[
 \lim_{N\to\infty}|f_N^{core}(t_0,e_1)-f(t_0,e_1)|
 =|f_B(t_0,e_1)-f(t_0,e_1)|>0.
\]

Consequently its uniform prediction error over `[0,T]` and the circle cannot
vanish. This remains a statement about the specific fixed H3 core; it is not
a no-go theorem for every finite Gaussian core or every finite closure.

The full H3 grammar can encode `H1(1-H1^2)`, apply the actual adjoint, and
retain bounded functions of the resulting reverse query. Thus its growing
word prefix eventually accesses information excluded by this fixed-core
limit. The candidate's obstruction is compatible with qualitative convergence
and with a possible quantitative rate for the complete maintained hierarchy.
It does not settle that positive-rate target.

No correction to the candidate is required for the stated diagnostic claim.
For later presentation, retain the explicit distinction between a local cubic
separation and a quantitative lower bound valid on a numerically specified
interval; the latter has not been proved here.
