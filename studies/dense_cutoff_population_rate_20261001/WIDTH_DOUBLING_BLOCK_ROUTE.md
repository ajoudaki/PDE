# Autonomous block endpoint and its independent-block comparison

2026-10-03. Scoped continuation of the width-\(n\) versus width-\(2n\)
question. This note proves a positive endpoint bridge for the matched
block variance/mobility interpolation. It does not prove that the
interpolation changes the trained prediction by a small amount.
No experiment, manuscript edit, Git operation, or other-study input.

Complete relevant inputs read: DECISIVE_CONDITIONAL_ROUTE.md,
ROOT_WIDTH_CONDITIONAL_THEOREM.md, the previously checked
GENERAL_SELF_AVERAGING.md and SELF_AVERAGING_FEEDBACK_ROUTE.md,
and the current paper's model/physical setting. The first two older
sources concern deterministic controls; their independence assertion
at the block endpoint must be modified for autonomous shared residuals.
The exact autonomous replacement is derived below.

**Proved result.** At the block endpoint, the output of the two
shared-residual width-\(n\) blocks is close, over all physical time and
in every fixed finite-second-moment query law, to the average of two
independently trained width-\(n\) networks using the same block
initializations:
\[
 \mathcal E_\mu\!\left(F_{2n,0},
                  \frac{f_n^1+f_n^2}{2}\right)
 \le C_{\delta,\mu}n^{-1/2}e^{K\sqrt{\log(e+n)}}
 \tag{A}
\]
with probability at least \(1-\delta\), for all sufficiently large
widths depending on confidence. The same rate holds between \(F_{2n,0}\)
and either independent block prediction. The proof needs carrier
maxima only for the independently trained reference blocks, not for
the shared-residual blocks.

## 1. Matched profile and exact autonomous endpoint

Fix depth \(L\ge2\), finite data \(v_a=x_a/\sqrt d\), and positive
weights \(p_a\) summing to one. Use the canonical mobilities and smooth
activation class in GENERAL_SELF_AVERAGING.md: bounded first three
derivatives, values allowed to grow linearly, a positive initial
feature-Gram gap on the compatible data quotient, and small fixed labels.

Let \(N=2n\). Split each hidden layer into two blocks of size \(n\).
For each hidden matrix, let the variance/mobility profile be
\[
 c_{ij}^{\ell}(s)=
 \begin{cases}
  2(1-s),&i,j\text{ are in corresponding blocks},\\
  2s,&i,j\text{ are in different blocks},
 \end{cases}
 \qquad 0\le s\le\tfrac12 .
 \tag{1}
\]
Hidden initialized entries are independent
\(N(0,c_{ij}^\ell(s)/N)\). First-layer entries remain independent
standard Gaussians, and the readout starts at zero. For the autonomous
profiled network, put \(R_a=F_{N,s}(x_a)-y_a\), and train by
\[
 \begin{split}
 \dot W^1&=-2\sum_a p_aR_a\delta_a^1v_a^\top,\\
 \dot W_{ij}^\ell
   &=-\frac{2c_{ij}^\ell(s)}{N}
          \sum_a p_aR_a\delta_{a,i}^\ell h_{a,j}^{\ell-1},
       \quad \ell\ge2,\\
 \dot w&=-2\sum_a p_aR_a h_a^L .
 \end{split}
 \tag{2}
\]
Here the prediction normalization is \(F_{N,s}=w^\top h^L/N\).
Both the edge variance and its mobility carry the same profile factor.

At \(s=1/2\), (1)–(2) give the canonical width-\(2n\) network
exactly. At \(s=0\), every off-block hidden entry is zero and stays
zero. Each diagonal block has hidden variance \(2/N=1/n\) and hidden
update coefficient \(2/N=1/n\). Its read-in and readout equations are
also the canonical width-\(n\) equations, except that both blocks use
the same residual.

Let \(\widetilde f_j\) denote the prediction of block \(j\), with its
own normalization \(1/n\), \(j=1,2\). Then the exact endpoint is
\[
 F_{2n,0}=\frac{\widetilde f_1+\widetilde f_2}{2},\qquad
 R_a=\frac{\widetilde f_{1,a}+\widetilde f_{2,a}}2-y_a.
 \tag{3}
\]
If \(\widetilde\Theta_j=(\widetilde W_j^1,
 \sqrt n\,\widetilde W_j^2,\ldots,\sqrt n\,\widetilde W_j^L,
 \widetilde w_j)\), and
\(\widetilde g_{j,a}=\nabla_{\widetilde\Theta_j}
                      [n\widetilde f_{j,a}]\), then
\[
 \dot{\widetilde\Theta}_j
       =-2\sum_a p_aR_a\widetilde g_{j,a}.
 \tag{4}
\]
The two initialized blocks are independent. The trained blocks are
generally dependent because \(R\) uses both. In particular, (3) is
not the average of two independently autonomous predictions.

For comparison, run independent autonomous width-\(n\) networks from
these same two initializations:
\[
 f_j=f_n^j,\qquad r_{j,a}=f_{j,a}-y_a,\qquad
 \dot\Theta_j=-2\sum_a p_a r_{j,a}g_{j,a},\qquad
 g_{j,a}=\nabla_{\Theta_j}[nf_{j,a}].
 \tag{5}
\]
Their trajectories are independent under the product initialization law.
The tilded and untilded states in each block agree initially.

## 2. Physical tube and fitting of the shared-residual pair

This step requires no stochastic carrier theorem for the tilded blocks.
On a deterministic initialization event, assume bounded first-weight
Frobenius RMS and hidden operators in each block, and a fixed positive
gap for the average initialized readout-feature Gram.
For the comparison in this note we may take the stronger event that
each block has its own strict initial Gram margin; its probability
tends to one.

For any prescribed common control of total variation at most a small
fixed \(S_*\), the physical bootstrap applies separately to both blocks:
\[
 \|\widetilde w_j\|_{\rm rms}\le CS_*,\qquad
 \operatorname{Var}(\widetilde W_j^1/\sqrt n)
       +\sum_{\ell\ge2}\operatorname{Var}(\widetilde W_j^\ell)
       \le CS_*^2.
 \tag{6}
\]
Here the variation uses Frobenius norms, and bounded slopes plus initial
physical bounds keep all feature RMS and matrix operators bounded.
Indeed the readout field has bounded RMS; backward recursion then
bounds response RMS by \(CS_*\); every hidden update field has
normalized norm \(CS_*\); integration gives (6). A strict smallness
choice closes the tube uniformly in width and time.

Define the raw tangent matrix of block \(j\) by
\[
 \widetilde\Lambda_{j,ab}
       =n^{-1}\langle\widetilde g_{j,a},\widetilde g_{j,b}\rangle,
 \qquad D_p=\operatorname{diag}(\sqrt{p_a}),\qquad
 \widetilde K_j=D_p\widetilde\Lambda_jD_p .
 \tag{7}
\]
Each is positive semidefinite and dominates its weighted
readout-feature Gram. Equation (6) changes that feature Gram by at most
\(CS_*^2\). Choose \(S_*\) so the average Gram retains a gap
\(\lambda>0\). Let
\(\widetilde{\overline K}=(\widetilde K_1+\widetilde K_2)/2\).
The exact shared-residual equation is
\[
 \frac{d}{dt}(D_pR)
       =-2\widetilde{\overline K}(D_pR),\qquad
 \widetilde{\overline K}\succeq\lambda I .
 \tag{8}
\]
Thus \(\rho_R=\|D_pR\|_2\le Ye^{-2\lambda t}\), and its common
control has total variation
\[
 2\int_0^\infty\sum_a p_a|R_a(t)|\,dt
 \le2\int_0^\infty\rho_R(t)\,dt\le Y/\lambda.
 \tag{9}
\]
Take \(Y/\lambda<S_*/2\). A first-exit argument prevents exit from
the controlled tube, proving global existence, exponential fitting,
and convergence of both parameter blocks. Only the averaged output
must fit; the individual tilded block predictions need not interpolate
the labels separately.

Fix a common decay rate \(\kappa>0\) for the two independent networks
and the shared-residual pair, and put \(S=CY/\kappa\) for their
common activity scale, after increasing the fixed constant if needed.
All tilded and untilded blocks then have the same type of physical tube.
This deterministic argument uses an empirical initial average Gram,
whose positive margin follows with high probability from the initialized
feature limit. It does not replace that empirical margin by an
expectation inside an individual trajectory.

## 3. Exact forced comparison

Assume the two independent reference blocks also obey the trained
carrier maximum
\[
 \max_{j,a,\ell,i,t}|k_{j,a,i}^\ell(t)|\le M .
 \tag{10}
\]
No corresponding tilded maximum is assumed.
Define their normalized block parameter discrepancies
\[
 D_j=
 \frac{\|\widetilde W_j^1-W_j^1\|_F}{\sqrt n}
 +\sum_{\ell=2}^L\|\widetilde W_j^\ell-W_j^\ell\|_F
 +\frac{\|\widetilde w_j-w_j\|_2}{\sqrt n},
 \qquad D=D_1+D_2 .
 \tag{11}
\]
The ordinary reference-side backward subtraction proved in
SELF_AVERAGING_FEEDBACK_ROUTE.md gives
\[
 \|\Delta g_{j,a,h}\|_{\rm rms}
       \le C[D_{j,w}+(M+S)D_{j,h}],\qquad
 \|\Delta g_{j,a,w}\|_{\rm rms}\le CD_{j,h}.
 \tag{12}
\]
The first RMS in (12) means the Euclidean hidden-gradient norm divided
by \(\sqrt n\). Only reference carriers multiply gate differences.
Both trajectories' physical operator/RMS bounds handle all other terms.
Consequently
\[
 \|\widetilde K_j-K_j\|_{\rm op}
       \le C(1+SM)D_j,\qquad \|K_j\|_{\rm op}\le C,
 \tag{13}
\]
where \(K_j=D_p\Lambda_jD_p\) is the independent block tangent.

Use weighted residual coordinates
\[
 \xi_j=D_pr_j,\qquad
 s=\frac{\xi_1+\xi_2}{2},\qquad
 d=\frac{\xi_1-\xi_2}{2},\qquad
 e=D_pR-s .
 \tag{14}
\]
Thus
\(D_p(R-r_1)=e-d\) and \(D_p(R-r_2)=e+d\).
The shared-versus-independent parameter equations (4)–(5), with
identical initial states in each block, give
\[
 D(t)\le
 C\int_0^t[\|e(u)\|_2+\|d(u)\|_2]\,du
 +C(1+M)\int_0^t[\rho_1(u)+\rho_2(u)]D(u)\,du .
 \tag{15}
\]
Here \(\rho_j=\|\xi_j\|_2\). This is an exact forcing comparison,
not an application of a controlled-path Lipschitz theorem.

Let \(\overline K=(K_1+K_2)/2\). From
\(\dot\xi_j=-2K_j\xi_j\), one gets
\[
 \dot s=-2\overline K s-(K_1-K_2)d .
 \tag{16}
\]
Combining (8) and (16) yields the exact error equation
\[
 \boxed{\displaystyle
 \dot e=-2\widetilde{\overline K}e
       -2(\widetilde{\overline K}-\overline K)s
       +(K_1-K_2)d,\qquad e(0)=0.}
 \tag{17}
\]
The last term records the independent residual disagreement and must
not be dropped. It does not require a small difference of the
independently initialized tangent matrices: their separate bounds
\(\|K_j\|\le C\) suffice.

The propagator of \(-2\widetilde{\overline K}\) is bounded by
\(e^{-2\lambda(t-u)}\). Also
\(\|s\|\le(\rho_1+\rho_2)/2\).
Using (13), variation of constants in (17), and then Tonelli, gives
\[
 \int_0^t\|e(u)\|_2\,du
 \le C(1+SM)\int_0^t(\rho_1+\rho_2)D\,du
                  +C\int_0^t\|d(u)\|_2\,du .
 \tag{18}
\]
Insert this in (15) and use
\(\int_0^\infty(\rho_1+\rho_2)\le CS\).
Gronwall with the increasing inhomogeneity
\(J(t)=\int_0^t\|d(u)\|_2\,du\) gives
\[
 \boxed{\displaystyle
 \sup_{t\ge0}D(t)\le
        C e^{CS(1+M)}J(\infty).}
 \tag{19}
\]
Every coefficient is width independent except the explicit maximum
\(M\). No tilded carrier moment, operator sensitivity, or control
homotopy is an additional assumption.

## 4. Whole-input and endpoint comparison

For a query \(v=x/\sqrt d\), physical forward subtraction gives
\[
 \sup_t|\widetilde f_j(t,x)-f_j(t,x)|
       \le C(1+\|v\|)\sup_tD_j(t).
 \tag{20}
\]
Let
\[
 C_\mu=C\left(\int(1+\|x\|/\sqrt d)^2\,d\mu(x)\right)^{1/2},
\]
finite for every fixed query law with finite second moment.
Equations (3), (19), and (20) prove
\[
 \boxed{\displaystyle
 \mathcal E_\mu\!\left(F_{2n,0},\frac{f_1+f_2}{2}\right)
       \le C_\mu e^{CS(1+M)}
             \int_0^\infty
                \left\|D_p\frac{f_1(X)-f_2(X)}2\right\|_2\,dt .}
 \tag{21}
\]
The physical-time supremum is inside the query integral. Both reference
and shared-residual parameter paths converge, so (21) includes their
fitted limits. It is an estimate at the same physical time.

Let
\[
 \epsilon=\sup_{t\ge0}\|d(t)\|_2 .
\]
Independent fitting gives
\(\|d(t)\|\le(\rho_1+\rho_2)/2\le Ye^{-\kappa t}\).
Therefore
\[
 J(\infty)\le\int_0^\infty
                    \min\{\epsilon,Ye^{-\kappa t}\}\,dt
 \le\frac{\epsilon}{\kappa}
                 [1+\log_+(Y/\epsilon)].
 \tag{22}
\]
The right side is interpreted as zero at \(\epsilon=0\).
For \(0<\epsilon<Y\), split the integral at
\(\kappa^{-1}\log(Y/\epsilon)\); for \(\epsilon\ge Y\), the
integral is at most \(Y/\kappa\le\epsilon/\kappa\).
Thus the time integration introduces only a logarithm at a polynomial
width rate, not a fixed nonvanishing residual error.

## 5. Probabilistic near-root consequence

Draw the two block initializations independently. The established
finite carrier/physical result gives, for both independent reference
paths on events of probability tending to one,
\[
 M=C_{\rm car}S\sqrt{\log(e+n)} .
 \tag{23}
\]
The shared-residual pair needs only their initial physical and Gram
margins, so Section 2 constructs its entire fitting path on the same
initialization event.

Apply GENERAL_SELF_AVERAGING.md to the two reference networks at the
fixed training query law \(\sum_a p_a\delta_{x_a}\).
For every fixed confidence, it gives
\[
 \epsilon\le\epsilon_n
      =C_\delta n^{-1/2}e^{K_0\sqrt{\log(e+n)}}
 \tag{24}
\]
for sufficiently large widths. The function
\(\epsilon[1+\log_+(Y/\epsilon)]\) is nondecreasing, so (22)
may use this deterministic upper bound. For fixed nonzero \(Y\),
\[
 J(\infty)\le
       C_\delta n^{-1/2}e^{K_0\sqrt{\log(e+n)}}\log(e+n)
\]
for all sufficiently large \(n\).
The amplification in (19) is at most
\(C e^{K_1\sqrt{\log(e+n)}}\). Absorb the remaining logarithm
into a further fixed enlargement of the exponential constant.
Union the finitely many good events, taking each failure probability
to be a fixed fraction of the requested \(\delta\).
This proves (A) without a numerical rate for the physical/carrier
event's complement.

To compare \(F_{2n,0}\) with either reference block, apply the same
same-width theorem also to the query law \(\mu\), and use
\[
 \mathcal E_\mu(F_{2n,0},f_1)
 \le\mathcal E_\mu\!\left(F_{2n,0},\frac{f_1+f_2}{2}\right)
            +\tfrac12\mathcal E_\mu(f_1,f_2).
 \tag{25}
\]
One application to the mixture of \(\mu\) and the training query law
can supply both discrepancy estimates. This preserves the original
finite-second-moment assumption.
For \(Y=0\), every readout remains zero and all displayed prediction
comparisons are exactly zero.

This is a fixed-confidence high-probability result. It does not assert
an unconditional expected error on the complement of the good event.

## 6. What remains for width \(n\) versus width \(2n\)

The canonical width-\(2n\) endpoint is \(F_{2n,1/2}\), while the
proved bridge concerns \(F_{2n,0}\). Under the natural common-Gaussian
profile coupling, the exact triangle inequality is
\[
 \mathcal E_\mu(F_{2n,1/2},f_1)
 \le \mathcal E_\mu(F_{2n,1/2},F_{2n,0})
                   +\mathcal E_\mu(F_{2n,0},f_1).
 \tag{26}
\]
The second term has now been bounded at the near-root rate.
No estimate for the first term is proved here. The older controlled
profile identity differentiates both edge covariance and mobility;
its signed response contrast remains substantive. For autonomous
profiled training, the residual response must also be retained.

The deterministic center \(c_n\) from GENERAL_SELF_AVERAGING.md
is also a near-root center for \(F_{2n,0}\), by (25).
Canonical width \(2n\) concentrates near its own center \(c_{2n}\).
Neither assertion bounds
\(\mathcal E_\mu(c_{2n},c_n)\). That remaining deterministic shift is
the width-bias issue; same-width concentration does not control it.

In particular, the block endpoint must not be declared equal to an
average of independent autonomous blocks. The present proof supplies
the missing approximate equality, but does not make either profile
endpoint equal to the other. The result is a genuine positive
intermediate bridge, not a completed width-doubling theorem.
