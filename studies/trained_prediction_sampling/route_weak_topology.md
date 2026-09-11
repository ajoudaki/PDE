# Weak Sobolev route for trained prediction sampling

First independent route frozen on 2026-09-11. Author: `/root/weak_topology_route`.
Status: concrete derived lemmas and a sufficient weighted tangent estimate;
the weighted tangent estimate is open. This is not an unconditional proof of
the requested sampling expansion, and it has not received an independent check.

## Scope and sources

The model is exactly C.4.7: two hidden tanh layers, the full Gaussian first
row, retained initialized action `A_0` and its actual adjoint, learned
Hilbert–Schmidt increment `K`, trainable readout `c`, unhalved mean square
loss, physical GF, all Borel laws on `sqrt(2) S^1 x [-Y,Y]`, and `T=40`.
The neighborhood can be decreased inside the one supplied by C.4.7. No
finite-width fluctuation or simultaneous width/sample CLT is claimed.

Permitted scientific sources were the established C.4 material and its explicit
earlier dependencies. Read coverage: complete C.4.7, C.4.1, C.4.5.1–2,
C.2, A.1–A.4 in `docs/global_nonlinear.md`; III.F.1–10 in
`docs/special_data_limits.md`; complete `docs/README.md` and `docs/NOTATION.md`.
The truncated portion of III.F.5 was reread separately. Earlier source proofs
not used in the derivations below, such as the actual finite-GF response
capture in C.4.6 and the raw-GD bridge, were not independently audited here.
No other study or another route's findings were read. No experiment was run.

Input versions at the initial check:

- HEAD: `94f776842874fa9b497cba9d5b0cc313cc019970`.
- `docs/global_nonlinear.md`: SHA-256
  `9e758665ec842167b3fa49ab3b3e6f4539ced45b65a85cda081cc5969258c226`.
- `docs/NOTATION.md`: SHA-256
  `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b`.
- `docs/README.md`: SHA-256
  `5dce185a68fafd4f5f366b491e4b367cdbb9d55443b8ac83eb8f5da3d417a19a`.

The new arguments below use the existing C.4.7 solution and its *Gaussian*
passive-query tails. They do not merely use its weaker displayed exponential
tail corollary. Indeed N-cap and N10 give Gaussian tails at every Euler query;
the positive-part passage NP preserves Gaussian tails at each reached time
and input with uniform constants. Thus, throughout a smaller neighborhood,

\[
 \sup_{\mu,t,u}\|Q_\mu(t,u)1_{|Q_\mu(t,u)|>R}\|_2
       \le C e^{-aR^2},\qquad \|c_\mu(t)\|_\infty\le2YT.       \tag{1}
\]

The positive-part passage is explicit: if `Q_j -> Q` in L2, then
`||( |Q|-R )_+||_2` is the limit of the corresponding norms; consequently
`tau_(2R)(Q) <= 2 liminf tau_R(Q_j)`. Rescale R and the constants.
The raw/action bounds and (1) also imply, for every fixed finite p,

\[
 \sup_{\mu,t}\|w_\mu(t)\|_p+\sup_{\mu,t,u}\|Q_\mu(t,u)\|_p<\infty. \tag{2}
\]

For the row, integrate NF and use Minkowski, `|phi'|<=1`, bounded residuals,
and the marginal Q moment bound. No action on Lp is inferred from its L2 norm.

## 1. A Hilbert law norm with the correct empirical rate

Write `u(a)=(cos a,sin a)`, with `a` on the circle `T=R/(2 pi Z)`.
For a finite signed law difference `sigma`, define signed circle measures

\[
 \sigma_0(B)=\int 1_{a\in B}\,d\sigma(a,y),\qquad
 \sigma_1(B)=\int y1_{a\in B}\,d\sigma(a,y).
\]

Use normalized Haar measure for Fourier coefficients of functions, and
`hat lambda(k)=int exp(-ika) d lambda(a)` for measures. Fix
`1/2<s<1`, for example `s=3/4`, and set

\[
 q_s(\sigma)^2=\sum_{k\in\mathbb Z}(1+k^2)^{-s}
       (|\widehat\sigma_0(k)|^2+|\widehat\sigma_1(k)|^2).       \tag{3}
\]

This is a seminorm on laws, which is appropriate: the GF vector field depends
on the law only through its input marginal and label-weighted input marginal.
Laws with identical pairs of marginals have identical predictions by reached
uniqueness. Their risks can differ by the additive label second moment.

If `hat mu_m` is the empirical law of m iid observations from any Borel mu,
independence and centering give

\[
 \mathbb E q_s(\widehat\mu_m-\mu)^2
 \le {1+Y^2\over m}\sum_{k\in\mathbb Z}(1+k^2)^{-s}<\infty/m. \tag{4}
\]

To check (4), each Fourier coefficient is the centered empirical average of
`exp(-ika)` or `y exp(-ika)`, with squared mean error at most `1/m` or
`Y^2/m`. Sum the nonnegative expectations. Thus `q_s=O_p(m^{-1/2})`
uniformly over laws. Atomic, singular, and continuous distributions are all
included. No total-variation approximation occurs.

For an E-valued function g, Cauchy–Schwarz in Fourier coefficients gives

\[
 \left\|\int g\,d\lambda\right\|_E
       \le\|g\|_{H^s(\mathbb T;E)}\|\lambda\|_{H^{-s}}.       \tag{5}
\]

For completeness, prove (5) first for trigonometric polynomials. Fourier
partial sums converge in Hs; since `s>1/2`, their uniform error is bounded
by their Hs error times `(sum (1+k^2)^(-s))^(1/2)`. Hence their measure
integrals converge to the actual Bochner integral. This proves (5) for the
continuous representatives used here without an unspecified distributional
pairing convention.

## 2. The actual atom force has one Sobolev derivative

At a reached state put `h=phi(w.u)`, `Z=Ah`, `H=phi(Z)`,
`Delta=c phi'(Z)`, `Q=A*Delta`, `f=<c,H>`, and

\[
 G_\theta(a)=\bigl(\phi'(w\cdot u)Q u,\ \Delta\otimes h,\ H\bigr)
       \in E.
\]

Then the force is exactly

\[
 F_\mu(\theta)=-2\int fG_\theta\,d\mu_0
                         +2\int G_\theta\,d\mu_1.            \tag{6}
\]

Let `v=du/da`. Strong angular differentiation gives

\[
 \begin{aligned}
 h_a&=\phi'(w\cdot u)w\cdot v,& Z_a&=Ah_a,& H_a&=\phi'(Z)Z_a,\\
 \Delta_a&=c\phi''(Z)Z_a,&Q_a&=A^*\Delta_a,&f_a&=\langle c,H_a\rangle,\\
 (G_w)_a&=\phi''(w\cdot u)(w\cdot v)Q u+
                 \phi'(w\cdot u)Q_a u+\phi'(w\cdot u)Qv,\\
 (G_K)_a&=\Delta_a\otimes h+\Delta\otimes h_a,&(G_c)_a&=H_a.
 \end{aligned}                                               \tag{7}
\]

Every term is in the stated raw space. The only extra unbounded product is
`(w.v)Q`, whose L2 norm is at most `||w||_4 ||Q||_4` by (2). All A and A*
applications use L2 inputs and their L2 operator norms. In particular this
does not assert that `Z_a` or `Q_a` has a fourth moment.

Here are derivative and continuity details for the potentially delicate first
term. The scalar difference quotient of `phi'(w.u(a))` converges in L4 to
`phi''(w.u)(w.v)`, with dominator `C|w|` in L4. The map Q is C1 in L2 by the
preceding lines of (7), bounded c, and the strong bounded-multiplier lemma.
Q is also continuous in L4: interpolate its L2 continuity with its uniform
L8 bound from (2). Split the product increment by changing its gate first
at fixed Q and then changing Q at the new bounded gate. This proves the
displayed derivative in L2 and its continuity. Ranks use their product norm.

It follows that

\[
 \sup_{\mu,t}\{\|G_{\theta_\mu(t)}\|_{H^1(\mathbb T;E)}+
                  \|f_\mu(t)G_{\theta_\mu(t)}\|_{H^1(\mathbb T;E)}\}
       \le C.                                               \tag{8}
\]

The second term follows from the uniform scalar bounds on f and f_a and
the ordinary product rule. Combining (5), (6), and (8) proves the exact
weak-law forcing estimate

\[
 \|F_\rho(\theta_\mu(t))-F_\mu(\theta_\mu(t))\|_E
                       \le C q_s(\rho-\mu).                  \tag{9}
\]

## 3. Nearly Lipschitz full-state law stability

Let two admitted laws have `q=q_s(rho-mu)`, and let d be the supremum raw
distance of their paths. Compare their same-law vector fields using NC,
with the reached comparison endpoint and (1). The law change at that endpoint
costs (9). In the same-law comparison the first-layer cutoff is the only
unbounded multiplier; the uniform readout bound removes its cutoff if desired.
Integration and elementary Gronwall give, for every `R>=1`,

\[
 d\le C\exp(CR)\{q+\exp(-aR^2)\}.                          \tag{10}
\]

The reference tail is uniform in passive u, so it can be integrated against
either law. All paths start at the same `(g,0,0)`.
For `0<q<e^{-a}`, take `R=sqrt(log(1/q)/a)`. This gives

\[
 d\le C q\exp\{C\sqrt{\log(e/q)}\}=:C\Lambda(q).            \tag{11}
\]

If q=0, send R to infinity in (10); then d=0. Uniform raw bounds cover
larger q. In particular, at every fixed admitted mu, for every eta>0,

\[
 \sup_{t\le40}\|\theta_{\widehat\mu_m}(t)-\theta_\mu(t)\|_E
                         =O_p(m^{-1/2+\eta}).                \tag{12}
\]

The empirical law lies in the admitted W1 neighborhood with probability
tending to one, by C.4.7's compact partition proof. Equation (12) concerns
that event. It is stronger than the existing displayed Hölder modulus but
does not yield differentiability.

## 4. Two remainder terms already have sufficient sampling order

### 4.1. The mixed law/state term

For two reached states at the same time with raw distance d, the same
factor subtractions and (1) give

\[
 \|G_\theta-G_{\bar\theta}\|_{L^2(\mathbb T;E)}+
 \|f_\theta G_\theta-f_{\bar\theta}G_{\bar\theta}\|_{L^2(\mathbb T;E)}
       \le C d\sqrt{\log(e/d)}                              \tag{13}
\]

for small d. Choose the cutoff so that its Gaussian tail is at most d;
the residual and forward factors are ordinarily Lipschitz in raw distance.
Both functions have bounded H1 norms by (8). The Fourier inequality

\[
 \|g\|_{H^s}\le\|g\|_{L^2}^{1-s}\|g\|_{H^1}^{s}             \tag{14}
\]

follows from Hölder applied to the nonnegative Fourier series. Therefore,
with `B_sigma(theta)=F_(mu+sigma)(theta)-F_mu(theta)`,

\[
 \|B_\sigma(\theta_\rho(t))-B_\sigma(\theta_\mu(t))\|_E
 \le C q_s(\sigma)[d\sqrt{\log(e/d)}]^{1-s}
 \le Cq_s(\sigma)^{2-s}\exp\{C\sqrt{\log(e/q_s(\sigma))}\}. \tag{15}
\]

The last inequality uses (11), with `sigma=rho-mu`. For s=3/4 and empirical
sigma, this is `O_p(m^{-5/8+eta})` for every eta>0, and is therefore small
enough after multiplication by sqrt(m). This eliminates the need to prove
a Lipschitz estimate for an angular derivative of the full state variation.

### 4.2. The scalar prediction Taylor remainder

At a reached base state with backward tail (1), let an arbitrary raw
increment `(v,B,d)` have norm h<=1, retaining bounded action and L2 readout
norms on the comparison pair. Then

\[
 \sup_u|f(\theta+(v,B,d),u)-f(\theta,u)-Df(\theta,u)[v,B,d]|
                       \le C h^2\sqrt{\log(e/h)}.             \tag{16}
\]

Here is the weighted expansion. The first-feature increment is
`phi'(w.u)(v.u)+R_1`, where pointwise
`|R_1|<=C min(|v.u|^2,|v.u|)`. The upper preactivation increment is
`A Delta h+B h+B Delta h`, with norm O(h). Expanding the upper tanh in
the scalar pairing with the bounded base readout costs O(h^2), since its
pointwise remainder is at most `C|Delta Z|^2`. The readout cross term costs
`||d||_2 ||Delta H||_2=O(h^2)`. The action cross term also costs O(h^2).
The remaining lower-feature error is exactly `<Q,R_1>`. Splitting Q at R
bounds this by `CR h^2+C tau_R(Q)h`. Choose R proportional to
`sqrt(log(e/h))` so that `tau_R(Q)<=h`. This proves (16) uniformly in u.

With h bounded by (11), the right side is `q^2 exp(C sqrt(log(e/q)))`,
again `o_p(m^{-1/2})` for empirical q. The unresolved part is the actual
parameter path's first variation, not the final scalar observation map.

## 5. Exact influence equation and its unbounded part

Fix one admitted mu. At its actual path, for `xi=(v,B,d)`, define

\[
 \begin{aligned}
 h^{[1]}(u)&=\phi'(w\cdot u)(v\cdot u),\\
 Z^{[1]}(u)&=A h^{[1]}(u)+B h(u),\\
 H^{[1]}(u)&=\phi'(Z(u))Z^{[1]}(u),\\
 f^{[1]}(u)&=\langle d,H(u)\rangle+\langle c,H^{[1]}(u)\rangle,\\
 \Delta^{[1]}(u)&=d\phi'(Z(u))+c\phi''(Z(u))Z^{[1]}(u),\\
 Q^{[1]}(u)&=A^*\Delta^{[1]}(u)+B^*\Delta(u),\\
 G^{[1]}(u)&=\bigl(
 [\phi''(w\cdot u)(v\cdot u)Q(u)+\phi'(w\cdot u)Q^{[1]}(u)]u,
 \Delta^{[1]}(u)\otimes h(u)+\Delta(u)\otimes h^{[1]}(u),
 H^{[1]}(u)\bigr).
 \end{aligned}                                               \tag{17}
\]

Superscript `[1]` means variation, not a network layer. If the displayed
products are integrable, the necessary raw influence equation is

\[
 \xi_\sigma'=L_\mu(t)\xi_\sigma+b_\sigma(t),\quad \xi_\sigma(0)=0,
 \quad b_\sigma(t)=-2\int(f_\mu-y)G_\mu\,d\sigma,
\]
\[
 L_\mu(t)\xi=-2\int
       [f^{[1]}(u)G_\mu(u)+(f_\mu(u)-y)G^{[1]}(u)]\,d\mu.   \tag{18}
\]

This retains all three trainable blocks, both learned-action variations,
the initialized Gaussian action, its actual adjoint, and the changing
residual. For an atom z the centered influence would be
`I_mu(z;t,u)=Df_mu(t,u)[xi_(delta_z-mu)(t)]`; its mean is zero by linearity
and (18), if that equation has the needed solution.

All parts of (18) except one define bounded operators on raw E. The
exception is the row multiplication matrix

\[
 V_\mu(t,\omega)=-2\int(f_\mu(u)-y)\phi''(w\cdot u)
                         Q_\mu(t,u,\omega)uu^T\,d\mu(u,y).
                                                               \tag{19}
\]

Thus `L_mu=M_(V_mu)+R_mu`, where R_mu is bounded on E, uniformly in
time and mu on the smaller neighborhood. For example `Q^[1]` is L2-bounded
by `C||xi||_E` because c is bounded and both action orientations are L2
bounded; the factor `f^[1]` is a scalar bounded by the same norm.
The multiplication part has dense natural domain `{v:V_mu v in L2}`.
It need not be bounded on raw L2. Its matrix norm has uniform Gaussian tails:
it is bounded by a constant times `int |Q(u)| dmu`; Jensen transfers the
subGaussian square-exponential moment of each marginal Q to this average.

## 6. One concrete missing estimate suffices

Let `V_mu,R_mu` be (19) and its bounded remainder. Spectrally clip the
real symmetric 2-by-2 matrix V at eigenvalues +/-N, and call it V_N.
For each integer N, the bounded strongly continuous equation

\[
 (\xi_{\sigma,N})'=(M_{V_N}+R_\mu)\xi_{\sigma,N}+b_\sigma,
                   \qquad \xi_{\sigma,N}(0)=0               \tag{20}
\]

has a unique solution by its iterated-integral series. No Lp existence is
presumed. The following is the precise open estimate:

\[
 \sup_{N\ge1}\sup_{t\le40}
 \left[\|\xi_{\sigma,N}(t)\|_E+\|v_{\sigma,N}(t)\|_8
       +\|d_{\sigma,N}(t)\|_4
       +\sup_u\{\|Z^{[1]}_{\sigma,N}(t,u)\|_4
                            +\|Q^{[1]}_{\sigma,N}(t,u)\|_4\}\right]
             \le C_\mu q_s(\sigma).                         \tag{WT}
\]

The constant may depend on the separately fixed mu; uniformity over mu is
unnecessary for a fixed-law sampling theorem. It must be independent of N,
sigma, support size, and covariance rank. It is enough to prove WT for finite
signed measure directions and their completion under (3). This is a claim
about named tangent queries, not an Lp bound for A_0 on arbitrary inputs.

Here is a complete implication from WT to the desired first-order remainder.

**Cutoff removal.** Gaussian tails of V and Hölder give
`||(V-V_N)v_(sigma,N)||_2 <= C exp(-aN^2) q_s(sigma)`; take the tail in
L^(8/3) and v in L8. Subtract the N and N+1 equations, propagating with the
(N+1)-cutoff bounded generator. Elementary Gronwall gives

\[
 \|\xi_{\sigma,N+1}-\xi_{\sigma,N}\|_{C_tE}
                  \le Cq_s(\sigma)\exp(CN-aN^2).             \tag{21}
\]

These differences are summable. Thus xi_N converges strongly in `C_t E`.
The bounds in WT pass to the limit by L2 convergence and Fatou, for each
time and query with the same constants. Products `V v_N` converge in
`C_t L2`: use uniform L8 control of v_N, L2 convergence, interpolation to
L4, and V's uniform L4 bound. The clipped tails vanish by the first
estimate. The bounded remainder terms pass directly. This proves (18),
with linear dependence on sigma and the WT bounds. The forcing is
continuous; the limiting equation gives a strong derivative once strong
continuity of `V(t)v(t)` is checked by the same interpolation argument.

**Raw field Taylor defect along these directions.** Let q=q_s(sigma).
Under WT,

\[
 \sup_{t\le40}\|F_\mu(\theta_\mu(t)+\xi_\sigma(t))
                  -F_\mu(\theta_\mu(t))-L_\mu(t)\xi_\sigma(t)\|_E
                         \le C_\mu q^{3/2}                 \tag{22}
\]

for q<=1. The lower-feature L2 Taylor error is O(q^2) using v in L4.
After applying the L2-bounded A and including `B Delta h`, the upper
preactivation equals `Z+Z^[1]+e_Z` with `||e_Z||_2=O(q^2)`.
Because `Z^[1]` is L4-small, the upper-feature and base-readout-weighted
gate remainders are O(q^2) in L2. The readout/gate cross term needs care:
bounded gates and `||Z_new-Z||_2=O(q)` give
`||phi'(Z_new)-phi'(Z)||_4=O(q^(1/2))`; multiplication by d in L4 costs
O(q^(3/2)). Hence `Delta_new-Delta-Delta^[1]` and then
`Q_new-Q-Q^[1]` are O(q^(3/2)) in L2, using the actual adjoint.
For the lower gradient the remaining second-order term is bounded by
`||Q||_4 ||v||_8^2=O(q^2)`, and the gate/query-variation cross term by
`||v||_4 ||Q^[1]||_4=O(q^2)`. Ranks and scalar residual cross terms
are controlled by their L2 product bounds. These are all terms of (17)
and prove (22). No L4 bound on `A e_Z` was used.

**Comparison with the actual changed-law path.** Set
`tilde theta=theta_mu+xi_sigma`, where sigma=rho-mu. Its residual in the
nonlinear equation consists of (22) and the mixed source defect (15).
Subtract (18) from the actual equation, using

\[
 \begin{aligned}
 e'={}&F_\mu(\theta_\rho)-F_\mu(\widetilde\theta)
       +[F_\mu(\widetilde\theta)-F_\mu(\theta_\mu)-L_\mu\xi_\sigma]\\
     &+[B_\sigma(\theta_\rho)-B_\sigma(\theta_\mu)].
 \end{aligned}                                               \tag{23}
\]

Apply NC to the first difference with the *actual* reached path as its
tail-bearing endpoint. The approximate path has bounded raw norms by WT;
it need not have a bounded readout or Gaussian query tails. Put
`p=2-s`, so `1<p<3/2`. Equations (15),(22) give a velocity defect at most
`C q^p exp(C sqrt(log(e/q)))`. The same cutoff/Gronwall optimization as
(10) then yields

\[
 \sup_{t\le40}\|\theta_\rho(t)-\theta_\mu(t)-\xi_{\rho-\mu}(t)\|_E
                 \le C_\mu q^{2-s}\exp(C_\mu\sqrt{\log(e/q)}).
                                                               \tag{24}
\]

In particular the right side is `O_p(m^{-(2-s)/2+eta})` for empirical laws.
The predictor is uniformly Lipschitz on the raw bounded sets, and (16)
handles its Taylor error at `theta_mu+xi`. Hence WT implies the uniform
prediction expansion with a remainder `o_p(m^{-1/2})` on the whole time/input
rectangle, and the linear term is the empirical average of the actual
influence equation (18). This argument avoids assuming a bounded propagator
on every raw L2 initial direction.

To extend xi from measure directions to the Hilbert completion, the right
side of WT and linearity make the solutions Cauchy for q_s-Cauchy directions;
(21) is uniform in that norm. The solution map and prediction differential
therefore extend continuously. Centering the atom direction is legitimate
since `int b_(delta_z-mu) dmu(z)=0`; bounded linearity gives zero mean
influence. A functional Gaussian limit still requires the corresponding
Hilbert empirical CLT and its continuous image; this report's main unresolved
analytic input is WT, rather than total variation or a poor empirical rate.

## 7. Adversarial checks: what cannot establish WT

**SubGaussian coefficients alone do not bound a raw propagator.** On Gaussian
`L2`, multiplication by `exp(tG)` is unbounded for every t>0: choose normalized
indicators of `{G>R}` and let R increase. Thus a coefficient with every
Gaussian exponential moment can still generate an unbounded raw-L2
propagator. Integrability is not an essential supremum bound.

**Adding an L2-bounded nonlocal operator can destroy even very regular
forcing.** Take probability space `x in [0,infinity)` with normalized
half-normal density, set `V(x)=x`, and
`h(x)=exp(x^2/4)/(1+x)^2`. Then h is positive and in L2, while
`exp(t x)h(x)` is not in L2 for any t>0. The rank-one operator
`R v=h <1,v>` is bounded. Consider `v'=Vv+Rv+1`, `v(0)=0`.
For the cutoff V_N the solution is nonnegative by the iterated-integral
series and satisfies `v_N(s)>=s`; hence `<1,v_N(s)>=s` and

\[
 v_N(t,x)\ge h(x)\int_0^t e^{(t-s)\min(x,N)}s\,ds.
\]

Restricting the integral to `s in [t/4,t/2]` gives
`v_N(t,x)>= (t^2/16) h(x) exp((t/2)min(x,N))`. Monotone convergence
then makes `||v_N(t)||_2` diverge with N for every t>0. The same argument
works with the bounded symmetric operator `h tensor 1+1 tensor h`.
This is a counterexample to a *generic proof step*, not a counterexample
to the canonical initialized Gaussian action or to the sampling conjecture.

**The existing named-source caps are a different derivative.** N7–N8 freeze
residuals, contractions, covariance laws, alpha and beta. Equation (18)
differentiates the physical law flow and retains all resulting scalar
feedback and actual action variations. Bounds for the former cannot be
renamed as WT. Likewise the two-axis clock cancels the troublesome lower
gate at nu*, but no such cancellation has been established for every fixed
nearby law with arbitrary directions.

**No raw quadratic remainder follows from L2 alone.** Even at scalar base
zero, `v_n=1_(E_n)` with `P(E_n)->0` has L2 norm tending to zero while
`||tanh(v_n)-v_n||_2/||v_n||_2=|tanh(1)-1|`. The actual reached response
family must have more structure than an arbitrary bounded L2 direction ball.
WT states one concrete sufficient structure; (22) records exactly where it
is used.

## Route assessment

The empirical weak topology, the forcing estimate, nearly Lipschitz
nonlinear law stability, the mixed law/state remainder, and the scalar
prediction Taylor remainder are explicit. The route reduces the remaining
analytic work to WT for cutoff solutions of the actual full tangent equation
at each separately fixed nearby law. WT would suffice without an ambient
Lp operator bound or an ambient bounded tangent propagator. It is not
proved by the present source caps. A continuation should attack WT through
the retained Gaussian source/response structure, including differentiated
scalar feedback; repeating the raw cutoff comparison will not supply it.
