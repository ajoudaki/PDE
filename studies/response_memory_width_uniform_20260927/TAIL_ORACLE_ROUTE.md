# Clipped initialized carriers: a tail oracle and the precise closure gap

This scoped analytic route uses only `LEARNED_GATE_RESTORATION.md`,
`OLD_CLOCK_ROUTE.md`, `SHARED_RESIDUAL_GATE_ORACLE.md`, and
`docs/notation.qmd`, together with the required mathematical/research skills.
No experiments, searches, manuscript changes, or Git operations were used.
The candidate was derived without reading another active route.

**Result.** There is a well-posed population and finite-width oracle that
uses its own backward gate on every learned branch and on the clipped part
of every initialized carrier. Dense gates act only on initialized-carrier
overflow. Its error is

\[
 \sup_{t\le T}d(\bar\theta_{P,M}(t),\theta_D(t))
 \le \frac{C_{\rm comp}\exp((a+bM)T)}{\sqrt{P(P+1)}}.                 \tag{1}
\]

The constants are explicit below and independent of width, order, and
threshold; their dependence on fixed depth is through stated recursions.
With \(M(P)\to\infty\) and \(M(P)=o(\log P)\), the oracle tracks the dense
path and its remaining dense-gate velocity correction tends to zero for
each regular population reference. This is asymptotically vanishing oracle
intervention, not a theorem for the fully autonomous closure.

For the latter, the same calculation gives the different bound

\[
 \sup_{t\le T}d(\widehat\theta_P(t),\theta_D(t))
 \le e^{(a+bM)T}
       \left(\frac{C_{\rm comp}}{\sqrt{P(P+1)}}+B_T(M)\right),       \tag{2}
\]

where \(B_T(M)\) is an explicit weighted dense-carrier tail. Ordinary dense
\(L^2\) path regularity implies \(B_T(M)\to0\) but gives no decay that
offsets the exponential in (2). Even finiteness of every carrier moment
does not provide that implication. A separate, conditional Osgood theorem
below states exactly which stronger tail information does close autonomous
tracking. This route does not disprove the unrestricted closure conjecture.

## 1. Setting and the oracle

Use the canonical tanh flow, fixed finite training set
\(q_a=x_a/\sqrt d\), \(a=1,\ldots,m\), and fixed hidden depth \(L\ge2\).
Each population neuron space has probability measure. Formulas below use
population \(L^2\) norms. At finite width, replace vector \(L^2\) norms by
\(\|v\|_2/\sqrt n\), first-row norms by \(\|W_1\|_F/\sqrt n\), and
hidden Hilbert--Schmidt norms by ordinary Frobenius norms. The tensor
\(u\otimes v\) is \(g\mapsto u\mathbb E[vg]\), represented by
\(uv^T/n\). Initialized hidden operators need only be bounded.

Write \(A_\ell=W_\ell-W_{0,\ell}\) and \(v=w-w_0\). The dense reference
is a regular canonical solution on \([0,T]\), with gates
\(D_{\ell,a}^D=\tanh'(z_{\ell,a}^D)\). In particular, its forward and
backward fields are continuous in their population \(L^2\) spaces.
The oracle starts from the same physical initialization as the dense flow
and computes its actual forward activations and gates from its own
physical weights. Denote its own gate by \(\bar D_{\ell,a}\).

For \(M\ge0\), let

\[
 c_M(u)=\max(-M,\min(u,M)),\qquad r_M(u)=u-c_M(u).
\]

Clipping and the overflow map are both 1-Lipschitz. For gates
\(g,d\in[0,1]\), define

\[
 \mathcal B_M(g,d,u)=g\,c_M(u)+d\,r_M(u).                       \tag{3}
\]

Thus a coordinate with \(|u|\le M\) uses only the own gate \(g\).
For \(|u|>M\), the bounded part uses \(g\), and only the overflow uses
the supplied gate \(d\). Equivalently,
\(\mathcal B_M=gu+(d-g)r_M(u)\). This last term is the explicit dense
consistency correction; it is not suppressed in the oracle description.

Define the backward responses by

\[
 \bar\delta_{L,a}
   =\mathcal B_M(\bar D_{L,a},D_{L,a}^D,w_0)+\bar D_{L,a}\bar v,
                                                                    \tag{4}
\]
\[
 \bar\delta_{\ell,a}
   =\mathcal B_M\!\left(\bar D_{\ell,a},D_{\ell,a}^D,
                        W_{0,\ell+1}^*\bar\delta_{\ell+1,a}\right)
       +\bar D_{\ell,a}\bar A_{\ell+1}^*\bar\delta_{\ell+1,a},
 \qquad \ell<L.                                                  \tag{5}
\]

All residuals, the old clock, forward histories, backward histories, and
learned weights are the oracle's own. Precisely,
\(\bar r_a=\bar f_a-y_a\),
\(\bar\rho=(m^{-1}\sum_a\bar r_a^2)^{1/2}\),
\(\bar\tau=1+\int_0^t\bar\rho\). The first layer and readout obey

\[
 \dot{\bar W}_1=-\frac2m\sum_a\bar r_a\bar\delta_{1,a}q_a^T,
 \qquad
 \dot{\bar w}=-\frac2m\sum_a\bar r_a\bar h_{L,a}.                  \tag{6}
\]

For each hidden link, store the first \(P\) raw old-clock Legendre moments
of \(\bar h_{\ell-1,a}\) and
\(\bar b_{\ell,a}=\bar r_a\bar\delta_{\ell,a}/\bar\rho\), with constant
initial forward prefix and zero backward prefix, and reconstruct

\[
 \bar A_\ell=-\frac2m\sum_a\int_0^{\bar\tau}
       (\Pi_P\bar b_{\ell,a})(\xi)
           \otimes(\Pi_P\bar h_{\ell-1,a})(\xi)\,d\xi.             \tag{7}
\]

The actual raw insertion sources are \(\bar\rho\bar h\) and
\(\bar r_a\bar\delta_a\), so no division by zero enters the raw ODE.
At a zero residual all raw and outer velocities vanish.

At the dense state the two gates in (3) coincide, so
\(\mathcal B_M(D^D,D^D,u)=D^D u\). Hence (4)--(5) recombine to canonical
dense backpropagation for every \(M\). If \(w_0=0\), the entire top layer
is already self-gated; no top dense gate is needed.

The alternative literal mask
\(1_{\{|q^D|\le M\}}\bar D\bar q+
1_{\{|q^D|>M\}}D^D\bar q\) has the same useful one-reference estimate
at finite width. In population \(L^2\), however, that support mask does not
bound the current carrier \(\bar q\), so it does not establish local
Lipschitz regularity of the raw population ODE. Construction (3) resolves
this issue rather than silently assuming it away. It clips the current
carrier; dense carriers will enter only the comparison and tail bounds.

## 2. A priori bounds and existence, without comparison

Let

\[
 X=\max_a\|q_a\|,\quad Y=(m^{-1}\sum_a y_a^2)^{1/2},\quad
 R_0=\|w_0\|_{L^2},\quad K_{0,\ell}=\|W_{0,\ell}\|_{\rm op},
\]
\[
 R=(R_0^2+TY^2)^{1/2},\quad Q=R+Y,\quad S=TQ,\quad A=1+S.
                                                                    \tag{8}
\]

The unchanged readout equation implies

\[
 \frac d{dt}\|\bar w\|_{L^2}^2
 =-\frac4m\sum_a(\bar f_a-y_a)\bar f_a
 =Y^2-\frac4m\sum_a(\bar f_a-y_a/2)^2\le Y^2.
\]

Consequently \(\|\bar w\|_{L^2}\le R\), \(\bar\rho\le Q\),
\(\bar\tau\le A\), and pointwise integration of (6) gives
\(\|\bar v\|_{L^\infty}\le2S\).

The two summands in (3) have the same sign as \(u\). Since both gates lie
in \([0,1]\), \(|\mathcal B_M(g,d,u)|\le |u|\). Therefore the following
recursion bounds both the oracle and the dense state, uniformly in \(M,P\):

\[
 \beta_L=R_0+2S,\qquad
 J_\ell=2\sqrt{AS}\,\beta_\ell,\qquad K_\ell=K_{0,\ell}+J_\ell,
 \qquad \beta_{\ell-1}=K_\ell\beta_\ell.                         \tag{9}
\]

Indeed, given \(\max_a\|\bar\delta_{\ell,a}\|_{L^2}\le\beta_\ell\),
the sample-averaged squared backward history norm is at most
\(S\beta_\ell^2\), whereas each forward history has squared norm at most
\(A\). Cauchy--Schwarz in history and samples, and projection contraction
in (7), give \(\|\bar A_\ell\|_{\rm HS}\le J_\ell\), hence the same
operator bound. Equations (3)--(5) give the next backward bound in (9).
The dense increment has norm at most \(2S\beta_\ell\le J_\ell\), by its
unprojected history integral. Also
\(\|\bar W_1-W_1(0)\|_{\rm row,L^2}\le2SX\beta_1\).

For fixed \(g,d\), the scalar map \(u\mapsto\mathcal B_M(g,d,u)\) is
continuous and piecewise affine with slopes \(g\) and \(d\). Thus it is
1-Lipschitz. Together with \(|\tanh''|\le2\), this proves the global bound

\[
 \|\mathcal B_M(D(z),D^D,u)
       -\mathcal B_M(D(\widetilde z),D^D,\widetilde u)\|_{L^2}
 \le\|u-\widetilde u\|_{L^2}+2M\|z-\widetilde z\|_{L^2}.         \tag{10}
\]

The remaining learned-adjoint term requires the same inactive truncation
used in `LEARNED_GATE_RESTORATION.md`. For completeness, if \(p_k\) is
the shifted Legendre polynomial, its raw forward moment satisfies pointwise

\[
 |H_{a,k}|\le\int_0^{\bar\tau}|p_k(\xi/\bar\tau)|\,d\xi
       \le\frac A{\sqrt{2k+1}}.                                \tag{11}
\]

In the learned backward branch only, temporarily clip \(H_{a,k}\) at
\(A/\sqrt{2k+1}+1\), and clip \(v\) in (4) at \(2S+1\).
The reconstructed adjoint has the finite-sum expression

\[
 \bar A_\ell^*u=-\frac2{m\bar\tau}
       \sum_{a,k<P}(2k+1)H_{\ell-1,a,k}
                           \langle B_{\ell,a,k},u\rangle.
\]

Bounded clipped forward factors make multiplication by the varying own
gate locally Lipschitz in \(L^2\); (10) treats the initialized branch.
Scalar inner products, bounded initialized operators, the finite forward
recursion, and the locally Lipschitz residual norm preserve this property.
The supplied gates are strongly continuous multiplication operators on
every fixed \(L^2\) operand: convergence of the dense preactivations in
\(L^2\) gives convergence in measure of the bounded gates, and truncating
the operand reduces strong convergence to bounded dominated convergence.
This provides continuous time dependence and local Lipschitz state
dependence of the auxiliary raw ODE.

Its readout and clock bounds are unchanged, and its raw forward moments
still integrate actual bounded activations. Thus both auxiliary clippings
remain inactive by (11) and the bound on \(v\). The bounds (9) and the
raw moment integral representations bound the complete Hilbert state.
For fixed \(P,M\), the finite-sum formulas have uniformly bounded local
Lipschitz and velocity constants on this visited state ball; denominators
are at least one. If a maximal interval ended before \(T\), the velocity
bound would give a norm limit of the state at its endpoint, and local
existence there would extend it. This proves existence through \(T\).
Any solution of the original system has the same inactive bounds and hence
belongs to the same locally unique auxiliary system. This proves uniqueness.

## 3. Compression defect, uniformly in the clipping threshold

Let \(G_M(t,\theta)\) be the uncompressed physical update using (4)--(5)
and the state's own residual. Differentiating (7) gives exactly

\[
 \dot{\bar\theta}=G_M(t,\bar\theta)+E,\qquad E_1=E_w=0,
\]
\[
 E_\ell=\frac{2\bar\rho}{m}\sum_a
       (\bar b_{\ell,a}-\bar b_{\ell,a}^*)
          \otimes(\bar h_{\ell-1,a}-\bar h_{\ell-1,a}^*),         \tag{12}
\]

where a star is endpoint evaluation of the history projection. One way to
verify (12) is to differentiate the projected pairing: its clock derivative
is \(b^*\otimes h+b\otimes h^*-b^*\otimes h^*\). Subtracting the
uncompressed pairing derivative \(b\otimes h\) gives (12) with its sign.
For the squared projection error \(D_u=\|u-\Pi_Pu\|^2\), stationarity
of the least-squares coefficients cancels their derivatives and gives
\(\dot D_u=\bar\rho\|u-u^*\|^2\). The prefixes have zero initial error.
Therefore

\[
 \int_0^T\|E_\ell\|_{\rm HS}\,dt
 \le 2\sqrt{\left(\frac1m\sum_aD_{b,\ell,a}\right)
             \left(\frac1m\sum_aD_{h,\ell-1,a}\right)}.           \tag{13}
\]

For clarity, the forward projection estimate needed here follows from the
shifted Legendre differential identity
\(-[\xi(\tau-\xi)p_k']'=k(k+1)p_k\).
Integration by parts and orthogonality give, for every finite partial
Legendre sum of a Hilbert-valued \(H^1\) function \(h\), its weighted
derivative energy at most
\(\int_0^\tau\xi(\tau-\xi)\|h'\|^2\).
Indeed the derivative of the partial sum is the orthogonal projection in
the weighted derivative inner product, as follows by applying that
differential identity to each mode. Passing to finite tail sums and using
\(k(k+1)\ge P(P+1)\) for \(k\ge P\) gives

\[
 \|h-\Pi_Ph\|_{L^2(0,\tau)}^2
 \le\frac{\tau^2}{4P(P+1)}\int_0^\tau\|h'(\xi)\|^2\,d\xi.      \tag{14}
\]

Endpoint evaluation on degree-below-\(P\) polynomials has squared norm
\(\sum_{k<P}(2k+1)/\tau=P^2/\tau\). The sample RMS backward endpoint
error is consequently at most \((P+1)\beta_\ell\). Equations (12), (14),
and the identity for \(\dot D_h\) imply

\[
 \int_0^T\bar\rho\|E_\ell/\bar\rho\|_{\rm HS}^2dt
 \le \frac{P+1}{P}A^2\beta_\ell^2 Z_{\ell-1}
 \le2A^2\beta_\ell^2Z_{\ell-1},                                \tag{15}
\]

where \(Z_j\) bounds the sample-averaged integrated squared derivative
of the actual forward activations in their own clock. The chain rule,
\(\|G_{M,\ell}/\bar\rho\|_{\rm HS}\le2\beta_\ell\), and (15) give
the valid recursion

\[
 Z_1=4SX^4\beta_1^2,\qquad
 Z_\ell=3\left[4S\beta_\ell^2+
           (K_\ell^2+2A^2\beta_\ell^2)Z_{\ell-1}\right].         \tag{16}
\]

One can apply these clock computations on intervals with positive residual
and extend by the stationary zero-residual convention. No derivative of a
backward gate or of the clipping map was taken. Inserting the backward
mass bound \(m^{-1}\sum D_b\le S\beta_\ell^2\) and (14)--(16) in (13)
proves

\[
 \int_0^T\sum_{\ell=2}^L\|E_\ell\|_{\rm HS}\,dt
 \le\varepsilon_P:=\frac{C_{\rm comp}}{\sqrt{P(P+1)}},\qquad
 C_{\rm comp}=A\sum_{\ell=2}^L\beta_\ell\sqrt{SZ_{\ell-1}}.       \tag{17}
\]

These constants do not contain \(M\). The same constants, though not
necessarily optimal, bound the autonomous old-clock closure's defect and
states at finite width, as follows either from this argument with own
gates throughout or from `OLD_CLOCK_ROUTE.md`.

## 4. The oracle estimate and exact threshold dependence

Use the parameter distance

\[
 d(\theta,\theta_D)=\|W_1-W_1^D\|_{\rm row,L^2}
       +\sum_{\ell=2}^L\|A_\ell-A_\ell^D\|_{\rm HS}
       +\|w-w_D\|_{L^2}.                                      \tag{18}
\]

The forward preactivation and activation differences are at most
\(U_\ell d\), where

\[
 U_1=X,\qquad U_\ell=K_\ell U_{\ell-1}+1.                     \tag{19}
\]

The dense learned carrier has the additional bound

\[
 \|(A_{\ell+1}^D)^*\delta_{\ell+1,a}^D\|_{L^\infty}
       \le2S\beta_{\ell+1}^2.                                \tag{20}
\]

To verify it, the exact dense history is
\(A_j^D=-2m^{-1}\sum_b\int_0^t r_b^D\delta_{j,b}^D\otimes
h_{j-1,b}^D\,ds\). Its adjoint applied to \(u\) is a weighted sum of
the pointwise bounded fields \(h_{j-1,b}^D\), with scalar coefficients
bounded by \(|r_b^D|\beta_j\|u\|_{L^2}\). Integration and
\(m^{-1}\sum|r_b^D|\le\rho_D\) give
\(\|(A_j^D)^*u\|_\infty\le2S\beta_j\|u\|_2\), proving (20).

For the initialized branch, insert the dense carrier \(q^D\) between
the two states and use (10):

\[
 \|\mathcal B_M(\bar D,D^D,\bar q)-D^Dq^D\|_2
 \le\|\bar q-q^D\|_2+2M\|\bar z-z^D\|_2.                    \tag{21}
\]

At the top, \(q^D=w_0\); the learned readout \(v_D\) is bounded by
\(2S\) pointwise. At lower layers subtract the learned branch as

\[
 \bar D\bar A^*\bar\delta-D^D(A^D)^*\delta^D
 =\bar D\bar A^*(\bar\delta-\delta^D)
   +\bar D(\bar A-A^D)^*\delta^D
   +(\bar D-D^D)(A^D)^*\delta^D.
\]

Use (20) for the last term. The resulting backward bound is

\[
 \max_a\|\bar\delta_{\ell,a}-\delta_{\ell,a}^D\|_2
       \le V_\ell(M)d,
\]
\[
 V_L(M)=1+(4S+2M)U_L,
\]
\[
 V_\ell(M)=K_{\ell+1}V_{\ell+1}(M)+\beta_{\ell+1}
                    +(4S\beta_{\ell+1}^2+2M)U_\ell.            \tag{22}
\]

If \(w_0=0\), the \(2MU_L\) term can be omitted at the top.
Define

\[
 \Lambda(M)=2\left[XV_1(M)
       +\sum_{\ell=2}^L\big(V_\ell(M)+\beta_\ell U_{\ell-1}\big)
       +U_L\right],
\]
\[
 C_f=1+RU_L,\qquad
 C_r=2\left[X\beta_1+\sum_{\ell=2}^L\beta_\ell+1\right].       \tag{23}
\]

At common residual, subtraction of each gradient product and sample
Cauchy--Schwarz give velocity difference at most
\(\rho\Lambda(M)d\). The residual RMS difference is at most \(C_fd\),
and changing only residuals costs at most \(C_r\) times that difference.
Therefore

\[
 \|G_M(t,\bar\theta)-G_M(t,\theta_D)\|_{\rm sum}
       \le(a+bM)d,\qquad
 a=Q\Lambda(0)+C_rC_f,\quad b=Q\Lambda_1,                      \tag{24}
\]

where \(\Lambda_1\) is the coefficient of \(M\) in \(\Lambda(M)\).
It is explicit: set

\[
 W_L=2U_L,\quad W_\ell=K_{\ell+1}W_{\ell+1}+2U_\ell,
 \qquad \Lambda_1=2\left[XW_1+\sum_{\ell=2}^LW_\ell\right].     \tag{25}
\]

At zero initial readout one may instead set \(W_L=0\).
Without that improvement,
\(W_\ell=2\sum_{j=\ell}^L U_j\prod_{k=\ell+1}^jK_k\).
Thus the pre-Gronwall constant is affine in \(M\), not a power
\(M^L\). The dependence on depth is in these products and the downward
quadratic recursion (9); it is not claimed to be uniformly controlled as
\(L\to\infty\).

The dense trajectory solves \(\dot\theta_D=G_M(t,\theta_D)\).
Subtract its integral equation from (12), use (17) and (24), and iterate
the scalar integral inequality. The exponential series gives
\(d(t)\le\varepsilon_P e^{(a+bM)t}\), proving (1).

For test inputs, repeat (19) with \(U_1=\|x\|/\sqrt d\). Then
\(|f(\theta,x)-f_D(x)|\le[1+RU_L(x)]d\). This transfers every proved
parameter estimate to uniform prediction error on bounded inputs and to
\(L^2\) prediction error under any test distribution with finite second
input moment.

## 5. Dense tails and asymptotically vanishing oracle intervention

Define the dense initialized carriers

\[
 q_{L,a}^D=w_0,\qquad
 q_{\ell,a}^D=W_{0,\ell+1}^*\delta_{\ell+1,a}^D\quad(\ell<L),
\]
\[
 t_\ell(t,M)=\left(\frac1m\sum_a
                   \|r_M(q_{\ell,a}^D(t))\|_2^2\right)^{1/2}.
                                                                    \tag{26}
\]

Overflow tails are no larger than the ordinary tails
\(\|q^D1_{\{|q^D|>M\}}\|_2\). Define the nonnegative propagation
weights

\[
 c_j=2\left[X\prod_{k=2}^jK_k
             +\sum_{\ell=2}^j\prod_{k=\ell+1}^jK_k\right],
 \qquad H_M(t)=\sum_{j=1}^Lc_jt_j(t,M),                         \tag{27}
\]

where an empty product is one and an empty sum is zero.

For a fixed regular population reference,

\[
 \gamma(M):=\sup_{t\le T}H_M(t)\longrightarrow0.               \tag{28}
\]

Here is the uniform-in-time justification. Each carrier path is continuous
in \(L^2\), so its image on \([0,T]\) has a finite \(\epsilon\)-net in
\(L^2\). The overflow map is 1-Lipschitz. The tail norm at an arbitrary
time is consequently at most \(\epsilon\) plus the largest tail norm of
the finitely many net elements. Each of those tends to zero by dominated
convergence. Taking \(M\to\infty\), then \(\epsilon\to0\), proves
(28), including the finitely many samples and layers.

Let \(F\) denote the fully self-gated physical vector field. At one fixed
oracle physical state, compare its clipped backward recursion with full
backpropagation. The local difference in the initialized branch is
\((D^D-\bar D)r_M(\bar q^M)\), with
\(\bar q_{\ell,a}^M=W_{0,\ell+1}^*\bar\delta_{\ell+1,a}\).
The difference of the higher backward response propagates with operator
norm at most \(K_{\ell+1}\). Since the gate difference is at most one,
the same downward recursion that produced (27) gives

\[
 \|F(\bar\theta_{P,M})-G_M(t,\bar\theta_{P,M})\|_{\rm sum}
 \le \bar\rho\sum_{j=1}^Lc_j
      \left(\frac1m\sum_a\|r_M(\bar q_{j,a}^M)\|_2^2\right)^{1/2}.
                                                                    \tag{29}
\]

For \(j<L\), Lipschitzness of overflow and (22) bound the last RMS by
\(t_j(t,M)+K_{0,j+1}V_{j+1}(M)d\). At the top it is exactly
\(t_L(t,M)\). Define
\(D_M=\sum_{j<L}c_jK_{0,j+1}V_{j+1}(M)\), an affine function of \(M\).
Then (1), (28)--(29) yield

\[
 \int_0^T\|F(\bar\theta_{P,M})-G_M(t,\bar\theta_{P,M})\|_{\rm sum}dt
 \le QT\left[\gamma(M)+D_M\varepsilon_Pe^{(a+bM)T}\right].     \tag{30}
\]

Choose any \(M(P)\to\infty\) with \(M(P)=o(\log P)\), for example
\(M(P)=\sqrt{\log(P+1)}\). Both terms in (30) tend to zero, and (1)
also tends to zero. In particular these oracle paths satisfy
\(\dot{\bar\theta}_{P,M(P)}=F(\bar\theta_{P,M(P)})+o_{L^1_t}(1)\)
after including the compression defect (17).

Every finite member nevertheless receives dense gates, and (30) is only
an approximate-solution statement. It does not make that algorithm
autonomous, prove stability of another approximate solution, or establish
that the actual autonomous closure follows the same path.

At finite width, (1) and (30) are deterministic with the displayed
normalizations. To make (28) or (30) uniform over widths, one additionally
needs \(\sup_{n,t}H_{n,M}(t)\to0\), or an appropriate probabilistic
uniform-integrability statement. Uniform RMS bounds alone do not imply
it. For instance a vector with one entry \(\sqrt n\) and all other entries
zero has RMS one but its RMS overflow approaches one as \(n\to\infty\)
at every fixed \(M\). This example concerns the inference from norm bounds;
it is not asserted to be a carrier reached by canonical Gaussian training.

## 6. The fully autonomous comparison and its unresolved factor

At finite width, let \(\widehat\theta_P\) be the actual old-clock closure,
whose existence and defect bound are supplied by `OLD_CLOCK_ROUTE.md` and
Section 3. At population width the following is a comparison statement for
any such regular closure solution on \([0,T]\); it does not independently
establish existence of the unclipped population moment ODE.

Subtract its fully self-gated backward recursion from the dense recursion.
At a lower layer the exact initialized-branch identity is

\[
 \widehat D W_0^*\widehat\delta-D^D W_0^*\delta^D
  =\widehat D W_0^*(\widehat\delta-\delta^D)
       +(\widehat D-D^D)c_M(q^D)
       +(\widehat D-D^D)r_M(q^D).                              \tag{31}
\]

The first two terms are bounded by the same coefficients as (21), and
the last term's sample RMS is at most \(t_\ell(t,M)\). Subtract the
learned branch exactly as in Section 4. Thus, with backward-error RMS
\(e_\ell\),

\[
 e_\ell(t)\le V_\ell(M)d(t)+\Gamma_\ell(t,M),\qquad
 \Gamma_L=t_L,\quad
 \Gamma_\ell=K_{\ell+1}\Gamma_{\ell+1}+t_\ell.                \tag{32}
\]

Split vector fields first at the common dense residual and then at fixed
closure responses. Equations (23), (27), and (32) imply

\[
 \|F(\widehat\theta_P)-F(\theta_D)\|_{\rm sum}
  \le(a+bM)d(t)+\rho_D(t)H_M(t).                              \tag{33}
\]

Define

\[
 B_T(M)=\int_0^T\rho_D(t)H_M(t)dt\le S\gamma(M).               \tag{34}
\]

The integral equation, compression bound, and scalar integrating factor
now prove (2). A sufficient condition for convergence by this particular
bound is a choice \(M(P)\to\infty\) satisfying both

\[
 \frac{e^{bTM(P)}}P\to0,\qquad
 e^{bTM(P)}B_T(M(P))\to0.                                    \tag{35}
\]

If all dense initialized carriers are essentially bounded by one common
\(M_0\) throughout the horizon, then \(B_T(M_0)=0\), and (2) does give
the endpoint \(O(P^{-1})\) autonomous estimate with that fixed threshold.
This is an additional dense-carrier hypothesis, not a consequence of the
initialized operator bounds.

The slow diagonal used in (30) guarantees the first limit in (35), but
not the second. Choosing \(M\) first to make the raw tail small and then
\(P\) to make compression small does not avoid this condition: the
threshold chosen in the first step also changes the multiplier of that
same tail. This is the forbidden limit interchange in a naive tail proof.

For \(bT>0\), dense \(L^2\) regularity alone does not imply even
\(\liminf_{M\to\infty}e^{bTM}B_T(M)=0\). A time-constant carrier
\(q(s)=s^{-\alpha}\), \(s\in(0,1)\), \(0<\alpha<1/2\), is a regular
\(L^2\) path. For \(M\ge1\), substitution
\(s=M^{-1/\alpha}u\) gives its exact overflow norm

\[
 \|(q-M)_+\|_2
  =\left[\int_0^1(u^{-\alpha}-1)^2du\right]^{1/2}
          M^{1-1/(2\alpha)}.                                 \tag{36}
\]

It tends to zero only polynomially, so multiplication by \(e^{bTM}\)
diverges. Even all finite moments do not resolve the issue. On a countable
probability space, put \(q(k)=e^k\) and
\(\Pr\{k\}=Z^{-1}e^{-k^2}\), \(k\ge1\), with
\(Z=\sum_{k\ge1}e^{-k^2}<\infty\). Every \(p\)-th moment is finite,
since \(pk-k^2=-(k-p/2)^2+p^2/4\). Taking
\(k=\lceil\log(2M)\rceil\) shows

\[
 \|r_M(q)\|_2\ge\frac{e^k}{2\sqrt Z}e^{-k^2/2}.
\]

The logarithm of this lower bound is of order \(- (\log M)^2\), which
cannot offset any positive multiple of \(M\). These two examples disprove
the claimed tail implication from regularity/moments. They do not assert
that either carrier is realized by the specified Gaussian network, nor do
they disprove autonomous tracking. A theorem exploiting special Gaussian
trajectory structure would be additional evidence beyond these premises.

## 7. Conditional autonomous tracking by a tail modulus

The exponential-tail product is a sufficient condition for the fixed-
threshold proof, not a necessary condition for tracking. One can do better
than freezing \(M\) throughout the interval. With \(\gamma\) from (28),
define, for \(u\ge0\),

\[
 \omega(u)=(a+1)u+
      \inf_{M\ge0}\bigl[bMu+Q\gamma(M)\bigr].                 \tag{37}
\]

This is a finite nondecreasing concave function with \(\omega(0)=0\),
\(\omega(u)>0\) for \(u>0\), and \(\omega(u)\to0\) as \(u\downarrow0\).
The last property follows by choosing a large fixed \(M\) with small
\(\gamma(M)\), then taking \(u\) small. Equation (33) holds for every
threshold at every time; minimizing it pointwise is therefore valid.
The extra \(u\) in (37) only increases the bound. We obtain

\[
 d(t)\le\varepsilon_P+\int_0^t\omega(d(s))ds.                  \tag{38}
\]

**Conditional theorem.** If

\[
 \int_{0+}\frac{du}{\omega(u)}=\infty,                         \tag{39}
\]

then \(\sup_{t\le T}d(\widehat\theta_P(t),\theta_D(t))\to0\).
For finite-width uniform convergence, use common constants and a common
tail envelope \(\gamma\) satisfying (39). Population existence remains
as specified in Section 6.

Here is the complete scalar argument. For \(\varepsilon_P>0\), set
\(z(t)=\varepsilon_P+\int_0^t\omega(d(s))ds\). Then \(d\le z\), and
monotonicity of \(\omega\) gives \(z'\le\omega(z)\) almost everywhere.
Integration yields
\(\int_{\varepsilon_P}^{z(t)}du/\omega(u)\le t\). If some fixed
\(\eta>0\) were reached by \(z\) before \(T\), this would imply
\(\int_{\varepsilon_P}^{\eta}du/\omega(u)\le T\), contradicting (39)
for sufficiently large \(P\). Hence \(d\) tends uniformly to zero.
If \(\varepsilon_P=0\), repeat with any positive \(\varepsilon\) and
let it decrease to zero.

For example, the additional envelope
\(\gamma(M)\le C e^{-cM^\alpha}\), for large \(M\), gives, by choosing
\(M=(2\log(1/u)/c)^{1/\alpha}\),

\[
 \omega(u)\le C_1u\,[1+(\log(1/u))^{1/\alpha}]
 \quad\text{for small }u.                                   \tag{40}
\]

Substitution \(v=\log(1/u)\) shows that the reciprocal of this upper
bound has divergent integral precisely when \(\alpha\ge1\). Thus a
uniform exponential or faster dense-carrier tail is sufficient for this
conditional convergence theorem on every fixed horizon. No Gaussian or
exponential carrier tail is inferred here from Gaussian matrix
initialization.

When \(\alpha>1\), (2) itself also proves convergence: take
\(M(P)=(\log P/c)^{1/\alpha}\). Both terms are
\(P^{-1}\exp(O((\log P)^{1/\alpha}))\), up to constants. This is
\(P^{-1+o(1)}\), not a proved constant-times-\(P^{-1}\) endpoint rate.
For merely exponential tails, the optimized modulus (or iteration on
sufficiently short time intervals) avoids requiring a tail exponent larger
than \(bT\). For slower envelopes, failure of the sufficient Osgood test
does not disprove convergence; it leaves this scalar comparison route
unclosed. Mere \(L^2\) continuity, or unspecified high finite moments,
provides no verified condition (39).

## 8. Claim status and exact remaining obligation

| Claim | Status and scope |
|---|---|
| Clipped initialized-carrier oracle is well posed through \(T\) | Proved in population and finite width, every fixed \(P,M\) |
| Oracle tracking is \(C_T(M)/P\), with \(C_T(M)=C_{\rm comp}e^{(a+bM)T}\) | Proved with width-independent constants on the stated initialized bounds |
| Oracle intervention tends to zero along a slow threshold diagonal | Proved for a fixed regular population reference; uniform widths additionally need uniform dense-carrier tails |
| The actual autonomous closure obeys the tail comparison (2) | Proved at finite width; conditional on population closure existence on the horizon |
| Dense regularity alone makes the amplified tail small | False as an inference from \(L^2\) regularity, even from unspecified finiteness of all moments |
| An Osgood dense-carrier tail modulus implies autonomous convergence | Proved conditionally by (37)--(39); no endpoint \(P^{-1}\) rate asserted |
| Fully autonomous width-uniform tracking under only the present dense-flow premise | Open |

This extends the earlier learned-gate oracle without superseding its valid
fixed-oracle theorem. The new construction localizes all external gate
dependence to initialized-carrier overflow and quantifies its disappearance.
The remaining bridge is a justified stability or carrier-tail estimate for
the actual dense/closure pair, sufficiently strong for (35), (39), or a
different structured-defect argument. Vanishing intervention by itself is
not that bridge. These are internal analytic results, not promotion review.
