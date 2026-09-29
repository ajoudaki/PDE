# Unit-label compact-horizon theorem under a joint width/order scaling

This is a scoped research result for the actual autonomous old-clock closure
in `paper/main.tex`. It uses only that manuscript's canonical setting and
old-clock construction/proof, `docs/notation.qmd`, `OLD_CLOCK_ROUTE.md`, and
the endpoint-polynomial argument in `SMALL_LABEL_SPECTRAL_SLACK.md`.
The `solve-math-rigorously` skill was applied. This note is internally checked
research, not established book material or an independently reviewed promotion.

The result below allows arbitrary labels of RMS at most one, every fixed
finite depth and arbitrary finite inputs. There is no Gram-gap, small-label,
successful-fitting, Gaussian-initialization, or residual-floor assumption.
Its price is a large joint memory order: the sufficient order grows
exponentially in the square root of width. It therefore establishes joint
width/order convergence, not a width-uniform theorem for unrestricted pairs
`(n,P)`, and not nontrivial low-rank compression at large width.

## 1. Statement and quantifiers

Fix finite integers `L>=2`, `m,d>=1`, inputs `x_1,...,x_m`, `K<infinity`, and
`T<infinity`. Every activation is tanh, the loss is
`m^-1 sum_a (f_a-y_a)^2`, and the block mobilities are `(n,1,...,1,n)`.
Write

\[
 X=\max_a\|x_a\|_2/\sqrt d,\qquad
 Y=\left(m^{-1}\sum_a y_a^2\right)^{1/2},\qquad
 B_0=\|w_0\|_2/\sqrt n.
\]

For every width `n>=1`, allow any finite first-layer initialization, any
hidden initialization satisfying `max_(ell>=2)||W_0^(ell)||_op<=K`, any
readout satisfying `B_0<=1`, and any labels satisfying `Y<=1`.
Let `theta_D` be dense gradient flow, and let `hat theta_(n,P)` be the
physical parameters reconstructed by the original raw old-clock moment ODE,
with the prescribed unit forward prefix, zero backward prefix and the same
initialization. The closure has order `P>=1`, not a modified clock or a
prescribed forcing. Set

\[
 d_n(\theta,\vartheta)^2
 =\frac{\|W^{(1)}-V^{(1)}\|_F^2}{n}
  +\sum_{\ell=2}^L\|W^{(\ell)}-V^{(\ell)}\|_F^2
  +\frac{\|w-v\|_2^2}{n},\qquad s_n=1+\sqrt n.
 \tag{1}
\]

There are finite constants `C_T` and `Lambda_T>=1`, depending only on
`T,L,m,d,X,K`, such that both paths exist uniquely through `T` for every
`n,P`, and

\[
 \sup_{0\le t\le T}d_n(\widehat\theta_{n,P}(t),\theta_D(t))
 \le C_T e^{\Lambda_T s_n}
       \left(\frac{B_0}{P^{3/2}}+\frac{s_n}{P^2}\right).
 \tag{2}
\]

In particular the following are genuine bounds with constants independent
of width, labels, and order:

* If `w_0=0`, every integer `P>=s_n exp(Lambda_T s_n)` satisfies
  `sup_(t<=T) d_n <= C_T/P`.
* If `B_0<=1`, including every vanishing-readout sequence with this bound,
  every integer `P>=exp(2 Lambda_T s_n)` satisfies the same conclusion
  after enlarging `C_T` by an absolute factor.
* More precisely, it suffices to require
  `P>=max{B_0^2 exp(2 Lambda_T s_n), s_n exp(Lambda_T s_n)}`.

There is also a single horizon-independent order choice. For every fixed
`T`, uniformly in all `n>=1` and all integers `P>=ceil(exp(n))`,

\[
 \sup_{t\le T}d_n(\widehat\theta_{n,P}(t),\theta_D(t))
 \le \frac{\widetilde C_T}{P}.
 \tag{3}
\]

More generally any prescribed sequence `P(n)` with
`log P(n)/sqrt(n) -> infinity` gives (3), with a constant that may also
depend on that sequence. These statements concern each fixed physical
horizon; they do not assert an all-time estimate.

The proof has three parts. First, the previously derived forward energy
and a sharper endpoint kernel bound give `||E||/rho<=C_T` pointwise for
the actual closure. This controls its own residual and backward history
without a residual-floor hypothesis. Second, forward and backward spectral
tails give an absolute velocity defect of order `P^-2`, with an additional
`B_0 P^-3/2` prefix term. Third, the explicit finite-width Lipschitz loss is
only `s_n`; the extra spectral power absorbs its exponential amplification
under the displayed joint order conditions.

## 2. Uniform a priori bounds and forward derivative energy

All constants denoted `C` below may depend on the fixed quantities in the
theorem and on `T`, but not on `n,P,Y`, the particular labels, the first-layer
initialization, or a positive lower bound on the residual. An ordinary
Euclidean or Frobenius norm is used throughout; every finite RMS factor is
displayed.

The unchanged readout equation gives, for either path,

\[
 \frac{d}{dt}\frac{\|w\|_2^2}{n}
 =Y^2-\frac4m\sum_a(f_a-y_a/2)^2\le1.
 \tag{4}
\]

Put `B=sqrt(1+T)`, `q=B+1`, `S=Tq`, and `A=1+S`. Define downward

\[
 \beta_L=B,\qquad
 D_\ell=K+2A\beta_\ell,\qquad
 \beta_{\ell-1}=D_\ell\beta_\ell
 \quad(\ell=L,\ldots,2).
 \tag{5}
\]

Then both paths satisfy

\[
 \|w\|_2/\sqrt n\le B,\quad \rho\le q,\quad
 \|W^{(\ell)}\|_{\rm op}\le D_\ell,\quad
 \max_a\|\delta_a^{(\ell)}\|_2/\sqrt n\le\beta_\ell;
 \qquad 1\le\widehat\tau\le A.
 \tag{6}
\]

Here and subsequently hats on closure fields are sometimes suppressed
inside estimates about the closure alone. To verify (6) for the closure,
write `b_a=r_a delta_a/rho` on the physical part of its clock history.
At each clock time

\[
 \frac1{mn}\sum_a\|b_a^{(\ell)}\|_2^2\le\beta_\ell^2,
 \qquad
 \frac1{mn}\sum_a\int_0^\tau\|b_a^{(\ell)}\|_2^2d\xi
 \le S\beta_\ell^2.
\]

Every forward history has normalized squared integral at most `A`.
Projection contraction and the identity
`||uv^T/n||_F=||u||_2||v||_2/n` therefore give

\[
 \|\widehat W^{(\ell)}-W_0^{(\ell)}\|_F
 \le2\sqrt{AS}\,\beta_\ell\le2A\beta_\ell.
\]

The backward recurrence proves (5)--(6) successively downward from the
readout. For dense flow, integration of
`||dot W^(ell)||_F<=2 rho beta_ell` gives the same bound, since `S<=A`.
The first-layer displacement divided by `sqrt(n)` is at most
`2SX beta_1`. These bounds and the raw moment integral formulas bound every
state coordinate at fixed finite `n,P`. The raw field is locally Lipschitz,
including at `rho=0`, because it uses `rho` and `r_a delta_a`, not their
quotient, and its only denominator is `tau>=1`. A bounded finite state at a
finite maximal endpoint has a limit and extends by local existence. This
proves continuation and uniqueness. For dense flow the same conclusion also
follows directly from its loss dissipation identity.

If the initial residual vanishes, every raw velocity and every dense
velocity vanishes, so both paths are identically equal to their initial
parameters. Otherwise local backward uniqueness prevents the closure from
hitting such an equilibrium at finite time. Its clock is then strictly
increasing on every compact physical interval. All following clock
calculations first concern this nonstationary case.

For the closure's own histories put

\[
 Z_\ell(t)=\frac1{mn}\sum_a\int_0^{\tau(t)}
                  \|\partial_\xi h_a^{(\ell)}\|_2^2d\xi.
\]

The exact moment-energy and reconstruction identities are

\[
 \dot D_{h,a}=\rho\|h_a-h_a^*\|_2^2,\qquad
 \dot D_{b,a}=\rho\|b_a-b_a^*\|_2^2,
\]
\[
 \dot{\widehat\theta}=F(\widehat\theta)+E,\qquad E_1=E_w=0,
 \qquad
 E_\ell=\frac{2\rho}{nm}\sum_a
              (b_a^{(\ell)}-b_a^{(\ell)*})
              (h_a^{(\ell-1)}-h_a^{(\ell-1)*})^T.
 \tag{7}
\]

Here `D` is the corresponding unnormalized squared `L2(0,tau)` projection
error, and a star is the projected history at its current endpoint. One
way to derive the first identity is to differentiate the minimum squared
error over polynomials of degree below `P`: the minimizing coefficients'
derivative has zero inner product with the error, and the growing endpoint
contributes exactly the displayed square. Differentiating the projected
pairing in the reconstruction gives the last identity. At `t=0` all these
projection errors are zero.

For completeness, the forward-energy induction used here has explicit
width/order-independent bounds

\[
 Z_1^*=4SX^4\beta_1^2,\qquad
 Z_\ell^*=3\{4S\beta_\ell^2+
             (D_\ell^2+2A^2\beta_\ell^2)Z_{\ell-1}^*\},
 \qquad Z_\ell(t)\le Z_\ell^*.
 \tag{8}
\]

Indeed endpoint evaluation on degree-below-`P` polynomials has norm
`P/sqrt(tau)`, so the RMS backward endpoint error is at most
`(P+1) beta_ell`. The Legendre tail inequality is

\[
 \|g-\Pi_Pg\|_{L^2(0,\tau)}^2
 \le\frac1{P(P+1)}\int_0^\tau\xi(\tau-\xi)\|g'(\xi)\|_2^2d\xi
 \le\frac{\tau^2}{4P(P+1)}\|g'\|_{L^2}^2.
 \tag{9}
\]

This follows by integration by parts in
`-(u(1-u)p_k')'=k(k+1)p_k`, Bessel's inequality for the weighted derivative
coefficients, and Parseval for the tail; rescaling gives the displayed
interval. Thus (7), sample Cauchy--Schwarz and (9) imply

\[
 \int_0^t\rho\|E_\ell/\rho\|_F^2ds
 \le\beta_\ell^2 A^2\frac{P+1}{P}Z_{\ell-1}(t)
 \le2\beta_\ell^2A^2Z_{\ell-1}(t).
 \tag{10}
\]

The first-layer clock derivative has RMS at most `2X^2 beta_1`.
For later layers differentiate
`h_ell=tanh(W_ell h_(ell-1))`, insert
`W_ell'=F_ell/rho+E_ell/rho`, and use (6), (10), and the squared triangle
bound with factor three. This proves (8). This induction precedes and does
not assume any pointwise relative-defect bound.

## 3. Endpoint cancellation gives a relative velocity bound

Two endpoint estimates are needed. For `g in H1(0,tau;R^N)`,

\[
 \|g(\tau)-(\Pi_Pg)(\tau)\|_2
 \le C\sqrt{\tau/P}\,\|g'\|_{L^2(0,\tau)}.
 \tag{11}
\]

For any bounded vector-valued history,

\[
 \|(\Pi_Pg)(\tau)\|_2
 \le C\sqrt P\,\mathop{\rm ess\,sup}_{0<\xi<\tau}\|g(\xi)\|_2.
 \tag{12}
\]

The constants are independent of the vector dimension, so both estimates
also apply to the array of all sample/neuron coordinates, with the explicit
normalizing factor `1/sqrt(mn)`. Here are details of the polynomial bounds.
With `p_j(u)=L_j(2u-1)`, the endpoint kernel is

\[
 K_P(u)=\sum_{j<P}(2j+1)p_j(u)
       =\tfrac12[p'_P(u)+p'_{P-1}(u)].
\]

Its primitive is `(p_P+p_(P-1))/2`, which vanishes at zero. Integration by
parts gives the exact endpoint error

\[
 g(\tau)-(\Pi_Pg)(\tau)
 =\frac12\int_0^\tau[p_P(\xi/\tau)+p_{P-1}(\xi/\tau)]g'(\xi)d\xi.
\]

Orthogonality proves (11). To see `||K_P||_L1<=C sqrt(P)`, it suffices
by the derivative formula to prove `Var L_j<=C sqrt(j)`. Set
`v(theta)=sqrt(sin theta)L_j(cos theta)` and
`Q(theta)=(j+1/2)^2+1/(4 sin^2 theta)`. The Legendre equation gives
`v''+Qv=0`, and

\[
 \frac d{d\theta}\left(v^2+\frac{(v')^2}{Q}\right)
       =-\frac{Q'}{Q^2}(v')^2\ge0\quad(0<\theta\le\pi/2).
\]

At the midpoint, the formulas
`L_(2k)(0)=(-1)^k binom(2k,k)/4^k`, `L_(2k+1)(0)=0`, and
`L'_j(0)=jL_(j-1)(0)` imply the quantity in parentheses is at most `2/j`;
use `binom(2k,k)/4^k<=1/sqrt(k+1)`, whose successive ratios prove it by
induction. Consequently, on `1/j<=theta<=pi/2`,

\[
 \left|\frac d{d\theta}L_j(\cos\theta)\right|
 \le Cj^{-1/2}\{(j+1/2)(\sin\theta)^{-1/2}
                          +(\sin\theta)^{-3/2}\}.
\]

Its integral is `O(sqrt(j))`, using `sin(theta)>=2 theta/pi`.
On `0<=theta<=1/j`, the bound `|L'_j|<=j(j+1)/2` gives variation at most
`1/2`. This derivative bound follows by summing
`L'_(k+1)-L'_(k-1)=(2k+1)L_k` and using `|L_k|<=1`; the latter follows
directly from the integral formula
`L_k(cos theta)=pi^-1 integral_0^pi(cos theta+i sin theta cos phi)^k dphi`,
obtained by coefficient comparison with the Legendre generating function.
Parity treats the other half interval. The case `j=0`, and hence `P=1`,
is immediate. This proves the kernel bound and (12).

Apply (12) to the complete backward array and (11) to the forward array.
Equations (6), (8) give

\[
 \left(\frac1{mn}\sum_a\|b_a^{(\ell)}-b_a^{(\ell)*}\|_2^2\right)^{1/2}
      \le C\sqrt P,\qquad
 \left(\frac1{mn}\sum_a\|h_a^{(\ell-1)}-h_a^{(\ell-1)*}\|_2^2\right)^{1/2}
      \le\frac C{\sqrt P}.
\]

The two endpoint factors cancel in (7). Therefore, with
`e_E(t)=sum_(ell>=2)||E_ell(t)||_F`,

\[
 e_E(t)\le C\widehat\rho(t).
 \tag{13}
\]

This is a statement about the actual autonomous closure for every order;
it uses no backward derivative regularity. Combining (13) with the dense
velocity formulas yields

\[
 \frac{\|\dot{\widehat W}^{(1)}\|_F}{\sqrt n}
 +\sum_{\ell=2}^L\|\dot{\widehat W}^{(\ell)}\|_F
 +\frac{\|\dot{\widehat w}\|_2}{\sqrt n}\le C\widehat\rho,
 \qquad
 \max_{\ell,a}\frac{\|\dot{\widehat z}_a^{(\ell)}\|_2
                           +\|\dot{\widehat h}_a^{(\ell)}\|_2}{\sqrt n}
       \le C\widehat\rho.
 \tag{14}
\]

For example, the second inequality follows successively from the first
layer and from `dot z_ell=dot W_ell h_(ell-1)+W_ell dot h_(ell-1)`.

The prediction differential is uniformly bounded from the parameter norm
in (1) to sample RMS: for a parameter increment `v`, forward differentiation
gives `max_(ell,a)||Dh_a^(ell)[v]||_2/sqrt(n)<=C|v|_n`, and hence
`(m^-1 sum_a |Df_a[v]|^2)^1/2<=C|v|_n`. Here `|v|_n=d_n(v,0)` for a
parameter increment. Thus (14) gives

\[
 \left(\frac1m\sum_a|\dot r_a|^2\right)^{1/2}\le C\rho,
 \qquad |\dot\rho|\le C\rho.
\]

Writing `eta=rho(0)>0` and integrating the last differential inequality,

\[
 c_T\eta\le\widehat\rho(t)\le C_T\eta\quad(0\le t\le T),
 \qquad \int_0^T\widehat\rho\,dt\le C_T\eta,
 \quad \eta\le B_0+Y\le2.
 \tag{15}
\]

The positive constant `c_T` is independent of `eta`. This is a derived
relative lower estimate, not an assumed positive residual floor. No sign
or coercivity of a Gram matrix was used. For `c_a=r_a/rho`,

\[
 \frac1m\sum_a c_a^2=1,\qquad
 \left(\frac1m\sum_a|\dot c_a|^2\right)^{1/2}
 \le2\frac{(m^{-1}\sum_a|\dot r_a|^2)^{1/2}}\rho\le C.
 \tag{16}
\]

## 4. Backward clock regularity and cancellation of the small residual

The readout equation and (15) give

\[
 \|w(t)\|_2/\sqrt n\le B_0+2\int_0^t\rho\,ds
                              \le B_0+C\eta,
 \qquad
 \max_{\ell,a}\|\delta_a^{(\ell)}(t)\|_2/\sqrt n
                              \le C(B_0+\eta).
 \tag{17}
\]

Differentiate the actual backward recurrence. At the top,

\[
 \dot\delta_a^{(L)}
 =\dot w\odot\tanh'(z_a^{(L)})
  +w\odot\tanh''(z_a^{(L)})\odot\dot z_a^{(L)}.
\]

For a lower layer put `q_a^(ell)=(W^(ell+1))^T delta_a^(ell+1)`.
The differentiated terms are

\[
 \tanh''(z_a^{(\ell)})\odot q_a^{(\ell)}\odot\dot z_a^{(\ell)},
 \quad\tanh'(z_a^{(\ell)})\odot
                  (\dot W^{(\ell+1)})^T\delta_a^{(\ell+1)},
 \quad\tanh'(z_a^{(\ell)})\odot
                  (W^{(\ell+1)})^T\dot\delta_a^{(\ell+1)}.
\]

The carrier supremum is bounded by its ordinary Euclidean norm,
`||q_a^(ell)||_infinity<=C sqrt(n)(B_0+eta)`; the same holds for `w`.
Use `|tanh''|<=2`, (14), (17), and `||dot W||_op<=||dot W||_F`.
Downward induction through the fixed depth gives

\[
 \max_{\ell,a}\|\dot\delta_a^{(\ell)}\|_2/\sqrt n
                          \le C s_n\rho.
 \tag{18}
\]

This explicit `sqrt(n)` is the only spatial loss in the source-regularity
estimate. It has no order dependence. From `b_a=c_a delta_a`, (16)--(18),

\[
 \left(\frac1{mn}\sum_a\|\dot b_a^{(\ell)}\|_2^2\right)^{1/2}
 \le C\{B_0+\eta+s_n\rho\}
 \le C\{B_0+s_n\rho\}.
 \tag{19}
\]

In the last step use (15) and `s_n>=1`. In particular if `w_0=0`, the
backward clock derivative has RMS at most `Cs_n`, and the backward history
joins its zero prefix continuously.

For general `B_0`, let `b_(0,a)^(ell)=c_a(0)delta_a^(ell)(0)` and subtract
its only prefix jump:

\[
 \widetilde b_a^{(\ell)}(\xi)
  =b_a^{(\ell)}(\xi)-b_{0,a}^{(\ell)}\mathbf1_{[1,\tau(T)]}(\xi).
\]

This history is continuous at `xi=1` and is `H1` on every finite terminal
interval. Its derivative on the physical part is `dot b/rho`.
Changing variables with `d xi=rho dt`, (15), (19) yield

\[
 \frac1{mn}\sum_a\int_0^{\tau(t)}
                 \|\partial_\xi\widetilde b_a^{(\ell)}\|_2^2d\xi
 \le C\left(\frac{B_0^2}{\eta}+s_n^2\eta\right).
 \tag{20}
\]

The occurrence of `1/eta` in this intermediate estimate is harmless and
will cancel. For the forward history, (14)--(15) give the sharper energy

\[
 \frac1{mn}\sum_a\int_0^{\tau(t)}
                   \|\partial_\xi h_a^{(\ell)}\|_2^2d\xi
 \le C\eta.
 \tag{21}
\]

Apply (9) to (20)--(21). If `Q_h,Q_b` denote the scalar RMS `L2` projection
errors with the factor `1/(mn)` in their squares, then

\[
 Q_{h,\ell}(t)\le\frac{C\sqrt\eta}{P},\qquad
 Q_{b,\ell}(t)
 \le C\left\{\frac{B_0}{\sqrt P}
           +\frac{B_0/\sqrt\eta+s_n\sqrt\eta}{P}\right\}.
 \tag{22}
\]

For the jump term we used
`||(I-Pi_P)1_[1,tau]||_L2<=C sqrt(tau/P)` and
`(mn)^-1 sum_a ||b_(0,a)^(ell)||_2^2<=C B_0^2`. To verify the scalar step
bound, for `P>=2` replace the step by a linear ramp of width `tau/P` on
whichever side of the jump has room. Its `L2` error is at most
`sqrt(tau/P)` and its derivative norm is `sqrt(P/tau)`. Projection
contraction and (9) prove the bound. For `P=1` contraction suffices. The
endpoint `tau=1` has zero step almost everywhere and presents no exception.

By (7), the exact accumulated absolute defect satisfies

\[
 \int_0^t\|E_\ell(s)\|_Fds
 \le\frac2{mn}\sum_a\sqrt{D_{b,\ell,a}(t)D_{h,\ell-1,a}(t)}
 \le2Q_{b,\ell}(t)Q_{h,\ell-1}(t).
\]

Multiplying (22) before discarding its residual factors proves

\[
 \int_0^T e_E(t)dt
 \le C\left\{\frac{B_0\sqrt\eta}{P^{3/2}}
                   +\frac{B_0+s_n\eta}{P^2}\right\}
 \le C\left\{\frac{B_0}{P^{3/2}}+\frac{s_n}{P^2}\right\}.
 \tag{23}
\]

There is no inverse residual or inverse label size in (23). At `eta=0`
the trajectories are stationary and the defect is exactly zero; that case
was separated before division. The proof therefore applies uniformly as
`eta` tends to zero, including labels with arbitrary signs or cancellations
against a nonzero initial prediction. At exactly zero readout, `eta=Y` and
the first term vanishes.

## 5. Explicit width-dependent stability and absorption by order

Let the parameter region be given by the hidden operator bounds and the
readout RMS bound in (6); impose no bound on the first-layer entries.
This region is convex and contains both trajectories and every segment
joining them. The forward differential bounds used after (14) hold throughout
it. The same differentiated backward recurrence used in (18), now with an
arbitrary parameter increment `v`, gives

\[
 \max_{\ell,a}\frac{\|D\delta_a^{(\ell)}[v]\|_2}{\sqrt n}
 \le Cs_n|v|_n.
 \tag{24}
\]

In detail, `||Dz[v]||_2/sqrt(n)<=C|v|_n`, every carrier supremum is at most
`C sqrt(n)`, the matrix-variation term is at most
`||v_(ell+1)||_F ||delta_(ell+1)||_2/sqrt(n)`, and the remaining term is
the next backward differential multiplied by a bounded operator.
These three bounds prove (24) by induction, including the top readout term.

Differentiate the dense update formulas. For example the first-layer block
has the terms `Dr[v] delta x^T` and `r Ddelta[v] x^T`; a hidden block has
in addition `r delta Dh[v]^T/n`; the readout has `Dr[v]h` and `r Dh[v]`.
The rank-one norm identity, (6), (24), `rho<=q`, and the bounded forward and
prediction differentials show

\[
 |DF(\theta)[v]|_n\le Cs_n|v|_n.
\]

Integrating this derivative along a joining segment gives
`|F(theta)-F(vartheta)|_n<=Cs_n d_n(theta,vartheta)`.
Subtract the two physical evolution equations, integrate, and use (23):

\[
 e(t):=d_n(\widehat\theta(t),\theta_D(t))
 \le Cs_n\int_0^t e(s)ds+\int_0^t e_E(s)ds.
\]

The elementary integral Gronwall inequality gives
`e(t)<=exp(Cs_n t) integral_0^t e_E`; for example this follows by applying
an integrating factor to the absolutely continuous upper envelope formed
by the two terms on the right. This proves (2) after choosing
`Lambda_T>=max{1,CT}`. No width-independent Lipschitz stability is asserted
or used.

To verify each joint-order claim, multiply (2) by `P` and put
`H_n=exp(Lambda_T s_n)`. The resulting right side is

\[
 C_T\left\{\frac{B_0H_n}{\sqrt P}+\frac{s_nH_n}{P}\right\}.
 \tag{25}
\]

The more precise order condition in Section 1 makes both terms at most
one. When `B_0=0`, only the second is present. For `B_0<=1`,
`H_n>=s_n` and `P>=H_n^2` control both. Finally for `P>=exp(n)`,
the two terms are bounded respectively by
`exp(Lambda_T(1+sqrt(n))-n/2)` and
`(1+sqrt(n))exp(Lambda_T(1+sqrt(n))-n)`. Each has finite supremum over
positive integers `n`, proving (3). The same argument proves the assertion
for every prescribed super-square-root logarithmic order sequence.

For any fixed bounded input set, the same bounded-operator forward
differentiation bounds predictions and forward hidden RMS discrepancies by
a constant times (1). Thus every asserted `C_T/P` joint-order estimate also
holds for predictions uniformly on that input set. Raw first-layer and
readout Euclidean errors carry their explicit `sqrt(n)` conversion; no
width-uniform statement about those unnormalized norms is implied.

The large sufficient order matters: `mP` then exceeds `n` at large width,
so the corresponding rank-`mP` corollary is vacuous as a rank reduction.
The theorem settles the stated joint compact-horizon approximation question
while leaving unrestricted width/order bounds and useful large-width memory
compression unresolved.
