# Direct energy stability for general input geometry

2026-10-03. Scoped proof attempt for the canonical, **unclipped**, two-tanh
dense network and its autonomous learning-speed Legendre closure, at the
same width and throughout physical time. The target is strict
\(C_\delta n^{-1/2}\) tracking with \(q(n)=o(n)\), keeping small fixed
labels and removing input orthogonality. **This note does not prove that
target.** It proves an energy inequality and a sufficient condition on the
spatial distribution of the actual discrepancy. Neither that condition nor
the finite exponential carrier-tail alternative is established here.

Scientific inputs were the current setting and closure in `paper/main.tex`,
complete `paper/results.tex`, `paper/proof_alltime.tex`, and
`paper/proof_tracking.tex`, and this study's `NONORTHOGONAL_DIRECT_ROUTE.md`,
`NONORTHOGONAL_TAIL_ROUTE.md`, and `FINITE_TAIL_ROUTE.md`. The canonical
notation skill and its neural reference, rigorous-math skill, and
conjecture-investigation skill were applied. No other study, historical
chat, experiment, manuscript edit, or Git operation was used.

## 1. Setup and what is already available

There are fixed training inputs \(v_a=x_a/\sqrt d\in\mathbb R^d\),
\(a=1,\ldots,m\), with arbitrary fixed Gram matrix
\(G_{ab}=v_a^\top v_b\). Write \(A=W^{(1)}\), \(W=W^{(2)}\), and
\(g(z)=\operatorname{sech}^2z\). The forward and backward objects are
\[
 z_a^{(1)}=Av_a,\quad h_a^{(1)}=\tanh z_a^{(1)},\quad
 z_a^{(2)}=Wh_a^{(1)},\quad h_a^{(2)}=\tanh z_a^{(2)},\quad
 f_a=n^{-1}w^\top h_a^{(2)},
\]
\[
 r_a=f_a-y_a,\quad \rho=\|r\|_m,
 \qquad \|r\|_m^2=m^{-1}\sum_a r_a^2,
\]
\[
 \delta_a^{(2)}=w\odot g(z_a^{(2)}),\quad
 k_a^{(1)}=W^\top\delta_a^{(2)},\quad
 \delta_a^{(1)}=g(z_a^{(1)})\odot k_a^{(1)}.
\]
The loss is \(\mathcal L=\|r\|_m^2\). Dense gradient flow has the
canonical block mobilities \((n,1,n)\). The actual autonomous closure
uses the same first-layer and readout equations, its own residual clock
\(\dot\tau=\widehat\rho\), \(\tau(0)=1\), and the forward and backward
Legendre moments specified in the manuscript. Hats denote this closure;
the subscript \(D\) denotes dense training.

On the manuscript's common initialization event \(\mathcal G_n\), its
all-order fitting result gives
\[
 \rho_D(t),\widehat\rho(t)\le Ye^{-\kappa t},\qquad
 \int_0^\infty(\rho_D+\widehat\rho)\,dt\le 2Y/\kappa,
 \qquad Y=\|y\|_m\le Y_*.
 \tag{1}
\]
All hidden operator norms are bounded independently of width and order.
Since tanh is bounded and \(w(0)=0\), the exact readout update also gives
\[
 \|w_D(t)\|_\infty,\|\widehat w(t)\|_\infty\le 2Y/\kappa.
 \tag{2}
\]
The closure reconstruction obeys
\[
 \dot{\widehat\theta}=F(\widehat\theta)+E,
 \qquad E=(0,E_2,0),
\]
\[
 E_2=\frac{2\widehat\rho}{mn}\sum_a
  (b_a^{(2)}-b_a^{(2)*})
  (\widehat h_a^{(1)}-\widehat h_a^{(1)*})^\top,
 \qquad b_a^{(2)}=\frac{\widehat r_a}{\widehat\rho}
                    \widehat\delta_a^{(2)}.
 \tag{3}
\]
Here a star means endpoint evaluation of the degree-below-\(q\)
orthogonal Legendre projection in the closure's clock. Formula (3) is an
identity for the original algorithm, not an altered backward recursion.
The direct two-layer source argument in `NONORTHOGONAL_DIRECT_ROUTE.md`
proves, without input orthogonality,
\[
 \epsilon_q:=\int_0^\infty\|E_2(t)\|_F\,dt
 \le C Y^{5/2}q^{-2}\sqrt{\log(e+q)}.
 \tag{4}
\]
Thus this attempt concerns stability after a source estimate already
uniform in width, order, and physical time.

## 2. A prediction-Hessian bound using a fourth moment of the direction

For the discrepancy
\(\Delta\theta=(\Delta A,\Delta W,\Delta w)
=\widehat\theta-\theta_D\), define its mobility norm
\[
 e^2=\frac{\|\Delta A\|_F^2}{n}
      +\|\Delta W\|_F^2
      +\frac{\|\Delta w\|_2^2}{n},
 \qquad
 A_4^2=\left(\frac1n\sum_{i=1}^n
                    \|\Delta A_{i,:}\|_2^4\right)^{1/2}.
 \tag{5}
\]
Both are time-dependent. The notation \(A_4^2\) is the square of the
empirical fourth-moment norm of the first-layer row discrepancy, not a
new matrix. The manuscript's sum distance satisfies
\(e\le d_n\le\sqrt3e\).

Fix a time and let \(\theta_s=\theta_D+s\Delta\theta\),
\(0\le s\le1\), be the straight parameter segment. The operator and
coordinate bounds above hold along this segment by convexity. For one
sample, put
\[
 \eta_a=\Delta A v_a,\qquad
 u_s=\Delta W h_{a,s}^{(1)}
       +W_s\{g(z_{a,s}^{(1)})\odot\eta_a\}.
\]
Thus \(\eta_a=\partial_s z_{a,s}^{(1)}\) and
\(u_s=\partial_s z_{a,s}^{(2)}\). Bounded slopes, features, and
operators give
\[
 \|\eta_a\|_2/\sqrt n\le Ce,\qquad
 \|u_s\|_2/\sqrt n\le Ce,\qquad
 \|\delta_{a,s}^{(2)}\|_2/\sqrt n
       +\|k_{a,s}^{(1)}\|_2/\sqrt n\le CY.
 \tag{6}
\]
Differentiating the prediction twice along the segment gives exactly
\[
\begin{aligned}
 \frac{d^2 f_a(\theta_s)}{ds^2}
 ={}&\frac2n\Delta w^\top\{g(z_{a,s}^{(2)})\odot u_s\}\\
 &+\frac1n w_s^\top\{g'(z_{a,s}^{(2)})\odot u_s^2\}\\
 &+\frac2n\delta_{a,s}^{(2)\top}\Delta W
                 \{g(z_{a,s}^{(1)})\odot\eta_a\}\\
 &+\frac1n k_{a,s}^{(1)\top}
                 \{g'(z_{a,s}^{(1)})\odot\eta_a^2\}.
\end{aligned}
 \tag{7}
\]
Squares on vectors in this formula are coordinatewise. For the first
three terms, Cauchy--Schwarz, (2), (6), and
\(\|\Delta W\|_{\rm op}\le\|\Delta W\|_F\) give bounds
\(Ce^2,CYe^2,CYe^2\), respectively. In particular the first term
does **not** carry a factor of \(Y\).

For the last term use only an RMS carrier bound:
\[
 \frac1n\sum_i|k_{a,s,i}^{(1)}|\,|\eta_{a,i}|^2
 \le
 \left(\frac1n\sum_i|k_{a,s,i}^{(1)}|^2\right)^{1/2}
 \left(\frac1n\sum_i|\eta_{a,i}|^4\right)^{1/2}
 \le CY A_4^2.
 \tag{8}
\]
The fixed input norm is absorbed into \(C\). Taking \(Y_*\le1\)
therefore proves
\[
 \sup_{0\le s\le1}\left|
       \frac{d^2 f_a(\theta_s)}{ds^2}\right|
       \le C(e^2+Y A_4^2).
 \tag{9}
\]
No coordinate carrier cutoff, carrier moment above order two, or Gaussian
claim has been used in this estimate.

## 3. Exact energy identity and a conditional direct tracking theorem

The mobility inner product is
\[
 \langle U,V\rangle_{\rm mob}
 =n^{-1}\langle U_A,V_A\rangle_F
   +\langle U_W,V_W\rangle_F+n^{-1}U_w^\top V_w.
\]
Write \(d_a=\widehat f_a-f_{D,a}=\widehat r_a-r_{D,a}\), and define
the two scalar Taylor remainders
\[
 R_{0,a}=d_a-Df_a(\theta_D)[\Delta\theta],\qquad
 R_{1,a}=Df_a(\widehat\theta)[\Delta\theta]-d_a.
\]
Taylor's integral formula identifies them as the integrals of (7) with
weights \(1-s\) and \(s\), respectively. In particular,
\(\|R_0\|_m+\|R_1\|_m\le C(e^2+YA_4^2)\).

Because \(F=-\nabla_{\rm mob}\mathcal L\), subtraction of the two
flows gives the exact identity
\[
 \frac12\frac{d e^2}{dt}
 =-2\|d\|_m^2
   -\frac2m\sum_a(\widehat r_aR_{1,a}+r_{D,a}R_{0,a})
   +\langle\Delta W,E_2\rangle_F.
 \tag{10}
\]
Indeed substituting
\(Df_a(\widehat\theta)[\Delta\theta]=d_a+R_{1,a}\) and
\(Df_a(\theta_D)[\Delta\theta]=d_a-R_{0,a}\) into the two gradient
pairings produces the first term, since \(\widehat r-r_D=d\).
Consequently
\[
 \frac12\frac{d e^2}{dt}
 \le -2\|d\|_m^2
      +C(\rho_D+\widehat\rho)(e^2+Y A_4^2)
      +e\|E_2\|_F.
 \tag{11}
\]
This preserves both residual factors at their endpoints. Replacing them
by residuals on a parameter segment would introduce an error that need
not decay in physical time, and would not justify all-time Gronwall.

For each width and closure order define
\[
 K_{n,q}=\int_0^\infty
    Y(\rho_D+\widehat\rho)
    \frac{A_4^2}{e^2}\,dt,
 \tag{12}
\]
with the quotient defined as zero when \(e=0\). It is finite at each
fixed width, since
\[
 A_4^2\le\sqrt n\,\|\Delta A\|_F^2/n\le\sqrt n\,e^2,
 \qquad K_{n,q}\le CY^2\sqrt n.
 \tag{13}
\]
For \(e>0\), divide (11) by \(e\) and discard its nonpositive term.
The scalar integrating-factor estimate, with the usual regularization
at zeros of an absolutely continuous norm, gives
\[
 \sup_{t\ge0}d_n(\widehat\theta(t),\theta_D(t))
 \le C\exp\{CY+CK_{n,q}\}\,\epsilon_q.
 \tag{14}
\]
The initial discrepancy is zero, and (1) controls the remaining
integrating factor. This proof uses the actual matrix defect (3).

**Conditional sufficient statement.** Fix the deterministic order sequence
\[
 q_n=\left\lceil n^{1/4}[\log(e+n)]^{1/4}\right\rceil=o(n).
 \tag{15}
\]
Suppose this sequence has the following property: for every \(\delta>0\)
there is a finite \(K_\delta\), independent of width, such that
\[
 \Pr\{\mathcal G_n\cap\{K_{n,q_n}\le K_\delta\}\}
       \ge1-\delta
 \tag{16}
\]
for all sufficiently large \(n\). Then (4) and (14) prove the desired
strict root-width parameter and whole-input prediction tracking at (15).
In fact \(q_n^{-2}\sqrt{\log(e+q_n)}\le Cn^{-1/2}\).
The whole-input comparison in `paper/proof_tracking.tex` transfers the
parameter estimate to every fixed test law with finite second moment
and to every fixed bounded query set. The evolving state count is
\(2mnq_n+n(d+1)+O(1)\), while the initialized \(n\times n\) mixer
continues to be retained exactly. The case \(Y=0\) is stationary.

An easier-to-state sufficient condition for (16) would be
\(A_4^2\le C_\delta e^2\) throughout training, on an event of the
required probability. Condition (12) is weaker: it only asks for
integrability of this ratio with its actual residual weight. Both are
**unproved** for the canonical Gaussian flow. They constrain how the
discrepancy is distributed among first-layer rows; smallness of the
discrepancy alone does not imply either condition. A width-uniform bound
on \(\mathbb E[\mathbf1_{\mathcal G_n}K_{n,q_n}]\) would also suffice:
Markov's inequality controls \(K_{n,q_n}\), and
\(\Pr(\mathcal G_n^c)\to0\) handles the initialization event.

## 4. Why rank and projection orthogonality do not close (12)

The last term of (7) is exactly the troublesome first-layer curvature.
The nonnegative Jacobian Gram of the loss supplies the negative term
in (10), but does not cancel this remainder. In (3), the temporal
orthogonality is in clock history. It does not say that a present row
discrepancy is orthogonal to the coordinate multiplier
\(k_{a,s}^{(1)}g'(z_{a,s}^{(1)})\).

Nor does the fact that \(E_2\) is a sum of \(m\) rank-one matrices
force perturbations to be spatially distributed. For example,
\[
 E_2=uv^\top/n,\qquad u=\mathbf1,\quad v=e_i,
\]
is rank one with bounded entries in its two factors. For a top response
\(\delta^{(2)}=c\mathbf1\),
\[
 E_2^\top\delta^{(2)}=c e_i.
\]
Thus its direct effect on a first carrier can be localized in one
coordinate. If a resulting first-layer discrepancy has only one nonzero
row, the ratio \(A_4^2/e^2\), when its other parameter blocks vanish,
is \(\sqrt n\). Smooth vector histories whose forward projection
residual has just one nonzero coordinate also exist: make all other
coordinates constant and choose a smooth nonpolynomial scalar history
in that coordinate. Projection does not remove this possibility.

These examples are statements about the information supplied by rank,
bounded factors, and temporal projection identities. They are **not**
claimed to be self-consistent Gaussian-initialized training trajectories,
or counterexamples to the requested theorem. They show why those
deterministic properties alone cannot justify the missing distribution
estimate.

The elementary fourth-moment relaxation can also be very wasteful.
It may charge a localized discrepancy even when the dense carrier in
that coordinate is small. A sharper attempt should retain the actual
weighted quadratic form in the last line of (7), or its signed version,
instead of immediately applying (8). That would require control only of
the response directions reached by the closure defect, rather than the
full variational operator. No such estimate has been proved here.

## 5. Status and exact remaining implication

The new proved statements are (7)--(11) and their deterministic
consequence (14). They give an alternative to carrier clipping: a
residual-weighted estimate on the row distribution of the actual
discrepancy would combine directly with the existing general-data
\(q^{-2}\sqrt{\log q}\) source bound. The regular curvature coefficient
integrates to \(O(Y)\); the unresolved coefficient is exactly (12).

This does not establish (16), a finite exponential carrier tail, or the
unconditional general-data root-width theorem. Establishing (16) would
require a new finite Gaussian estimate on the evolving response to the
structured memory defect. Exchangeability and RMS bounds do not prove
it, and replacing that estimate by a full operator-norm response bound
returns to the unbounded local carrier blocks identified in
`NONORTHOGONAL_TAIL_ROUTE.md`. The route is therefore **open at an
explicit probabilistic stability estimate**, not complete and not a
refutation of the central target.
