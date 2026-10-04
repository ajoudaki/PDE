# Finite deletion and near-quarter-order all-time tracking

2026-10-03. Scoped proof search for the actual two-tanh dense network and
the actual residual-RMS Legendre closure with the same initialization.
**Internally proved:** sufficiently small fixed labels and
\(q_n=n^{1/4}\exp\{A\sqrt{\log(e+n)}\}\) give strict root-width,
all-physical-time, input-integrated same-width tracking for two tanh hidden
layers and every fixed compatible finite sphere dataset. The complete local
insertion and probability arguments have separate collaborator
reconstructions. This is a study result awaiting the repository's promotion
process. The first route candidate (a weak carrier maximum followed by finite
deletion/reinsertion) was frozen before sibling results were received.
No experiment, manuscript edit, or Git operation is involved.

Inputs read: the complete own-study `FINITE_TAIL_ROUTE.md`,
`FINITE_TAIL_CHECK.md`, `NONORTHOGONAL_DIRECT_ROUTE.md`,
`NONORTHOGONAL_TAIL_ROUTE.md`, `NONORTHOGONAL_CHECK.md`,
`FINITE_MIXED_MOMENT_ROUTE.md`, `FINITE_MIXED_MOMENT_CHECK.md`, and
`GENERAL_DATA_ASSESSMENT.md`; subsequently the complete
`DATA_QUOTIENT_CLOCK.md`, `DATA_QUOTIENT_CHECK.md`, and the probability
reconstruction `Q_ORDER_POSITIVE_PROBABILITY_CHECK.md`; the manuscript's complete setting and
Legendre construction, `results.tex`, `proof_alltime.tex`, and
`proof_tracking.tex`; `docs/index.qmd` and `docs/notation.qmd`.
The required canonical-notation/neural reference, rigorous-proof, and
conjecture-investigation instructions were applied.

## 1. Frozen local lemma and its role

The new object is a retained network driven through its second-layer
preactivations. Deleting a first-layer neuron removes its incoming row and
its initialized outgoing column. The neuron's bounded first-layer activation
history is treated as an external scalar function; all retained parameters
still follow their **own actual residual-driven gradient flow**.

Fix the finite data \(v_a=x_a/\sqrt d\), \(a=1,\ldots,m\), with no
orthogonality requirement. Let \(N=n-r\), where the number \(r\ge1\) of
deleted neurons is fixed. Retained parameters are
\[
 \Theta=(A,H,w),\qquad A\in\mathbb R^{N\times d},\quad
 H\in\mathbb R^{n\times N},\quad w\in\mathbb R^n,
 \qquad W=H/\sqrt n.
\]
The squared Euclidean norm on this product is the sum of the squared block norms.
All normalizations remain \(n\). For an external vector \(e_a\in\mathbb
R^n\), set
\[
 h_a=\tanh(Av_a),\quad z_a=Wh_a+e_a,\quad
 \mathcal F_a(\Theta,e)=w^\top\tanh z_a,\quad
 f_a=\mathcal F_a/n,\quad r_a=f_a-y_a.
\]
Thus \(r_a\) denotes a residual, while \(r\) without a sample index above
denotes the fixed deletion count. The retained vector field is
\[
 F(\Theta,e)=-\frac2m\sum_a r_a\nabla_\Theta\mathcal F_a(\Theta,e).
 \tag{1}
\]
It differentiates at fixed external \(e\). This is exactly the retained
part of the full network's equation when its omitted contributions are
inserted into \(e\).

Let \(\Theta^0(t)\), \(0\le t\le T_n=c_T\log n\), be the autonomous
zero-input cavity, with zero initial readout. Its top response and retained
lower carrier are
\[
 \delta_a^0=w^0\odot\operatorname{sech}^2z_a^0,
 \qquad k_a^0=(W^0)^\top\delta_a^0.
\]
Up to a reference stopping time \(\sigma\le T_n\), assume the already
proved physical tube and fitting estimates, with fixed constants:
\[
 \|W^0\|_{\rm op}\le K,\quad \|w^0\|_\infty\le S,
 \rho^0(t)\le C S e^{-\kappa t},\quad
 \int_0^{\sigma}\rho^0(t)dt\le CS,
 \max_{a,i}|k^0_{a,i}(t)|\le 2M_n,
 \quad M_n=A_0 S\log n.                         \tag{2}
\]
Here \(A_0>0\) is fixed; it is unrelated to the matrix \(A\).
For the trace conclusion also assume the cavity budget
\[
 \mathcal M_\eta^0(\sigma)
 =\kappa\int_0^\sigma e^{-\kappa t}
     \frac1n\sum_{i=1}^{N}
       \exp\{\eta\max_a|k^0_{a,i}(t)|/S\}\,dt\le 2B.       \tag{3}
\]
Deleted coordinates may equivalently be filled with zero and their
exponentials with one; this changes the budget by at most \(r/n\).

Condition on the entire retained initialization. The omitted columns
\(x_j\), \(1\le j\le r\), are independent \(N(0,I_n/n)\) vectors.
For deterministic controls \(a_{a,j}:[0,T_n]\to[-1,1]\), let
\[
 e_a(t)=\sum_{j=1}^r x_j a_{a,j}(t)+\zeta_a(t),\qquad
 \operatorname{Lip}(a_{a,j})\le C\log n,\qquad
 \sup_{t,a}\|\zeta_a(t)\|_2\le C_r n^{-1/2}.          \tag{4}
\]
The small remainder \(\zeta\) may be adaptive; no independence is needed
for a deterministic stability bound for that term. For arbitrary measurable
\(\zeta\), (5) is a pathwise estimate along an existing absolutely
continuous solution. It does not assert well-posedness for every possible
feedback rule defining \(\zeta\). In the application the full dense
solution already exists by the fitting theorem; its learned omitted columns
give continuous \(\zeta\), and this pathwise estimate is all that is used.
For a prescribed continuous source, the finite-dimensional smooth vector
field has its usual local solution, and the estimates below continue it
through the reference interval.

**External perturbation lemma.** For sufficiently small fixed
\(S>0\), depending only on the deterministic tube constants and \(A_0\),
there is a conditional event of probability at least
\(1-C_r\exp(-n^{2/5})\) on which the following hold simultaneously for
all controls in (4), all \(t\le\sigma\), and every deleted column.
Let \(V\) solve the linearization of (1) about \((\Theta^0,0)\) with
external source \(\sum_jx_ja_{a,j}\) and zero initial variation. Then
\[
 \sup_{t\le\sigma}\|V(t)\|\le n^{1/100},\qquad
 \sup_{t\le\sigma}\|\Theta(t)-\Theta^0(t)-V(t)\|
       \le n^{-1/10}.                                  \tag{5}
\]
The entries of every linear first-layer variation, readout variation,
second-layer preactivation variation, and retained lower-carrier variation
are at most \(n^{-1/5}\) in absolute value. Consequently the actual
retained carrier discrepancy obeys
\[
 \max_{t\le\sigma,a,i}|k_{a,i}(t)-k^0_{a,i}(t)|=o(1).
                                                               \tag{6}
\]
For a single omitted column and its scalar control, let \(R_{a,a(\cdot)}(t)
\in\mathbb R^{n\times n}\) be the linear map from that column to the
top-response variation. The same event gives
\[
 \left|x^\top R_{a,a(\cdot)}(t)x-
       \frac1n\operatorname{tr}R_{a,a(\cdot)}(t)\right|
 \le n^{-1/5}.                                        \tag{7}
\]
Under (3) and \(CS^2\le\eta/2\), its trace satisfies
\[
 \frac1n|\operatorname{tr}R_{a,a(\cdot)}(t)|
 \le CS+CS^3\sqrt B+o(1).                            \tag{8}
\]
The constants and sufficiently-large-width threshold may depend on fixed
\(r,B,\eta,S\), but no exponent does. A random control selected after
seeing the omitted columns is covered because the good event is
simultaneous over the deterministic control class.

The complete reconstruction in `Q_ORDER_INSERTION_CHECK.md` verifies this
lemma, including (10), the nonlinear bound (14), the uniform control event,
and the subinterval trace estimate.

## 2. Exact linearization, including the adaptive residual

Write \(J(t,s)\) for the fundamental solution of the cavity variational
equation, and \(U_0(t,s)\) for the contraction generated by its negative
Gram part. If
\[
 L=\sqrt{\frac2{mn}}[\nabla\mathcal F_a]_{a=1}^m,
\]
then
\[
 D_\Theta F=-LL^\top-\frac2m\sum_a r_a^0D_\Theta^2\mathcal F_a.
                                                               \tag{9}
\]
The only unbounded Hessian block is diagonal over retained first-layer
neurons, with \(i\)-block
\(k^0_{a,i}\tanh''((A^0v_a)_i)v_av_a^\top\).
All other Hessian blocks have fixed operator bounds. Thus (2), contraction
of \(U_0\), and Gronwall give
\[
 \sup_{s\le t\le\sigma}\|J(t,s)\|_{\rm op}
 \le \exp\{CS(1+M_n)\}\le n^{1/400}                 \tag{10}
\]
after choosing \(S\) small and then \(n\) large. Fixed prefactors can be
absorbed by a strict margin in the label smallness inequality.

For one sample, the gradient of \(\mathcal F_a\) with respect to its
external input is \(\delta_a\). Therefore its mixed derivative is
\(D_e\nabla_\Theta\mathcal F_a=B_a^\top\), where
\(B_a=D_\Theta\delta_a\) is an \(n\)-by-parameter-dimension matrix.
At the cavity,
\[
 B_a[U]=\operatorname{sech}^2z_a^0\odot U_w
 +(w^0\odot\tanh''z_a^0)\odot
 \left[W^0(\operatorname{sech}^2(A^0v_a)\odot U_Av_a)
                +U_Hh_a^0/\sqrt n\right],
 \qquad \|B_a\|_{\rm op}\le C.                      \tag{11}
\]
For scalar source \(e_a=x a_a(t)\), its linear forcing is
\[
 (P_a+Q_a)x a_a(t),\quad
 P_a=-\frac2{mn}\nabla\mathcal F_a(\delta_a^0)^\top,
 \quad Q_a=-\frac2m r_a^0B_a^\top.                   \tag{12}
\]
In particular \(P_a\) has rank one and operator norm at most \(CS\),
while \(Q_a\) has rank at most \(n\) and norm at most \(C|r_a^0|\).
Neither contribution has been discarded. Consequently
\[
 V(t)=\sum_a\int_0^t J(t,s)(P_a(s)+Q_a(s))x a_a(s)ds.
                                                               \tag{13}
\]
Multiple deleted columns add linearly. The direct external term in the
top-response variation is
\(\operatorname{diag}(w^0\odot\tanh''z_a^0)x a_a(t)\).

## 3. Nonlinear remainder estimate and its reconstruction

Set \(\alpha_a=V_Av_a\), \(\nu=V_w\), and
\[
 z_{a,V}=W^0(\operatorname{sech}^2(A^0v_a)\odot\alpha_a)
            +V_Hh_a^0/\sqrt n+\sum_jx_ja_{a,j}.
\]
Let \(k_{a,V}\) denote the full linear retained-carrier variation,
including its direct external term. Suppose the linear variation satisfies
\[
 \|V\|+\max_a\|e_a\|_2\le Cn^{a_*},\qquad
 \max_a(\|\alpha_a\|_\infty+\|\nu\|_\infty+
           \|z_{a,V}\|_\infty+\|k_{a,V}\|_\infty)
       \le Cn^{-b_*},
 \quad a_*=1/100,\quad b_*=1/5.
\]
For an additional Euclidean parameter perturbation \(U\), with
\(u=\|U\|\le n^{-1/10}\), the pointwise Taylor bound is
\[
\begin{split}
 &\|F(\Theta^0+V+U,e)-F(\Theta^0,0)
       -D_\Theta F(\Theta^0,0)(V+U)-D_eF(\Theta^0,0)e\|\\
 &\quad\le C(1+M_n)\left[
 \rho^0\{n^{a_*-b_*}+n^{-b_*}u+u^2\}
 +n^{-1/2}\{n^{2a_*}+n^{a_*}u+u^2\}\right].        \tag{14}
\end{split}
\]
Here \(e\) in (14) is the linear external source, before the small
\(\zeta\) remainder. The constants also cover the fixed number of samples
and sources.

Here is the blockwise derivation; every norm in the next paragraphs is an
ordinary Euclidean or Frobenius norm. Let \(\Delta A=V_A+U_A\),
\(\Delta H=V_H+U_H\), and \(\Delta w=V_w+U_w\). To keep the displayed
bounds short within this calculation only, set
\[
 R=n^{a_*-b_*}+n^{-b_*}u+u^2,\qquad
 P=n^{-1/2}(n^{2a_*}+n^{a_*}u+u^2).
\]
For a smooth scalar function with bounded second derivative, the
coordinatewise Taylor remainder has absolute value at most the constant
times the square of its increment. Splitting an increment into its linear
part and its \(U\) part gives the three product estimates below.

The gradient blocks of \(\mathcal F_a\) are
\[
 (\operatorname{sech}^2(Av_a)\odot k_a)v_a^\top,
 \qquad \delta_a h_a^\top/\sqrt n,
 \qquad \tanh z_a.
\]
For the first block, the sole large reference coefficient multiplies the
coordinatewise quadratic first-layer Taylor remainder. Its norm is bounded
by \(CM_n\|\alpha_a^2\|_2\). Split the first-layer perturbation as
linear plus \(U_Av_a\); then
\[
 \|\alpha_a^2\|_2\le Cn^{a_*-b_*},\quad
 \|\alpha_a\odot U_Av_a\|_2\le Cn^{-b_*}u,\quad
 \|(U_Av_a)^2\|_2\le Cu^2.
\]
More explicitly, write the first-feature difference as
\(\Delta h_a=\operatorname{sech}^2(A^0v_a)\odot\Delta A v_a+R_{h,a}\).
Then \(\|R_{h,a}\|_2\le CR\). The preactivation difference is its
full linear variation plus
\[
 R_{z,a}=W^0R_{h,a}+
     \frac{\Delta H}{\sqrt n}\Delta h_a,
 \qquad \|R_{z,a}\|_2\le C(R+P).
\]
Indeed \(\|\Delta H/\sqrt n\|_{\rm op}\le
n^{-1/2}(n^{a_*}+u)\); its product with the first-order feature
difference costs \(CP\), and its product with \(R_{h,a}\) is smaller.
Expanding \(\delta_a=w\odot\operatorname{sech}^2z_a\), the readout/gate
cross term and the gate Taylor remainder have norms at most \(C(R+P)\):
the linear readout and preactivation have the stated infinity bounds,
their \(U\) parts have Euclidean norm at most \(Cu\), and \(R_{z,a}\)
has the bound just proved. Thus, writing \(\delta_{a,\mathrm{lin}}\) for
its full first variation,
\[
 \Delta\delta_a=\delta_{a,\mathrm{lin}}+R_{\delta,a},
 \qquad \|R_{\delta,a}\|_2\le C(R+P).
\]
Next
\[
 \Delta k_a=k_{a,\mathrm{lin}}+R_{k,a},\qquad
 R_{k,a}=(W^0)^\top R_{\delta,a}
          +\frac{\Delta H^\top}{\sqrt n}\Delta\delta_a,
 \qquad\|R_{k,a}\|_2\le C(R+P).
\]
The last product is \(CP\); the linear response map for \(\delta_a\)
has bounded operator norm and its input has norm \(C(n^{a_*}+u)\).

Changed-gate times changed-carrier uses both linear infinity bounds
\(\alpha_a,k_{a,V}\); it must not be bounded by a generic product of
Euclidean norms. The top gate terms use the corresponding bounds for
\(\nu,z_{a,V}\). Every \(H\)-matrix perturbation acts as
\(V_H/\sqrt n\), so its bilinear products cost at most
\(C n^{-1/2}(n^{2a_*}+n^{a_*}u+u^2)\).
The same \(n^{-1/2}\) appears in the middle gradient's outer product.
Combining these formulas gives the full gradient remainder bound
\[
 \|\nabla_\Theta\mathcal F_a(\Theta^0+V+U,e)
       -\nabla_\Theta\mathcal F_a(\Theta^0,0)
       -D\nabla_\Theta\mathcal F_a[V+U,e]\|
 \le C(1+M_n)(R+P).
\]

Finally the variation of the adaptive residual contributes two additional
products. The linear residual is bounded by
\(C n^{-1/2}(n^{a_*}+u)\). The scalar prediction remainder is bounded
by \(C(1+M_n)n^{-1}(n^{2a_*}+n^{a_*}u+u^2)\), while the reference
gradient has norm \(C\sqrt n\). These produce precisely the second
brace of (14), even though they are not multiplied by \(\rho^0\).
To justify the scalar prediction remainder, apply the extended Hessian
bound in \((\Theta,e)\) on the joining segment. The formulas above,
with increments multiplied by a scalar in \([0,1]\), show that every
segment carrier is its reference value plus its linear variation and a
remainder \(C(R+P)\). Its maximum is therefore \(2M_n+o(1)\).
The readout coordinates remain at most \(S+o(1)\) and the hidden
operator at most \(K+o(1)\). The extended Hessian has norm at most
\(C(1+M_n)\); its external-input blocks are bounded by the top gate
and readout. Dividing the scalar Taylor remainder by \(n\) gives
the claimed bound. Expanding the product of residual and gradient in (1)
now yields
\(C(1+M_n)[\rho^0(R+P)+P]\). Since \(\rho^0\le C\), this is
exactly (14) after enlarging the constant.

With \(U=\Theta-\Theta^0-V\), variation of constants, (10), and (14)
give on the bootstrap \(\sup\|U\|\le n^{-1/10}\)
\[
 \sup\|U\|\le C(1+M_n)(1+T_n)n^{1/400}
 [n^{-19/100}+n^{-3/10}+n^{-1/5}
                         +n^{-48/100}].             \tag{15}
\]
The right side is \(o(n^{-1/10})\). The source \(\zeta\) contributes
at most \(C(1+T_n)n^{-1/2+1/400}\) by the same local Lipschitz bounds.
Continuity therefore excludes a first attainment of the remainder cap.
The proof must verify (14) with the **linear** carrier and preactivation
variations, not accidentally assume infinity bounds on the unknown full
variation.

## 4. Gaussian linearization event and uniform controls

The output maps in (13), composed with first-layer/readout projections or
the derivative of a top preactivation or retained carrier, have operator
norm at most \(C(1+T_n)n^{1/400}\). Their direct external terms have
bounded norms. For sufficiently large width these are bounded by
\(n^{1/200}\). Every coordinate of such a map applied to independent
\(N(0,I_n/n)\) columns is centered Gaussian with variance at most
\(C_rn^{-1+1/100}\). Its tail at \(n^{-1/5}/2\) is bounded by
\(2\exp(-c_r n^{59/100})\). There are only \(C_rn\) relevant vector
coordinates; the \(H\) block needs a Euclidean bound, not an entrywise
one. Its linear image has rank at most \(rn\), expected norm at most
\(C_rn^{1/200}\), and Gaussian concentration at \(n^{1/100}\) is
stronger than needed.

For a deterministic \(n\)-by-\(n\) matrix \(R\), a Gaussian column
satisfies the quadratic-form tail obtained by diagonalizing its symmetric
part and multiplying the one-dimensional Gaussian-square moment-generating
functions:
\[
 \Pr\left\{|x^\top Rx-\operatorname{tr}(R)/n|>u\right\}
 \le2\exp\left[-c\min\left\{
 \frac{n^2u^2}{\|R\|_{\rm HS}^2},
 \frac{nu}{\|R\|_{\rm op}}\right\}\right].          \tag{16}
\]
When \(\|R\|_{\rm op}\le n^{1/200}\), use
\(\|R\|_{\rm HS}\le\sqrt n\|R\|_{\rm op}\) and
\(u=n^{-1/5}/2\); the failure probability is again at most
\(2\exp(-c n^{59/100})\).

The bounded control class on \([0,T_n]\), with Lipschitz constant
\(C\log n\), has an internal uniform \(n^{-3/10}\)-net with
\[
 \log N\le C_r n^{3/10}(\log n)^3.                 \tag{17}
\]
Sample at mesh \(n^{-3/10}/(C\log n)\), round values at accuracy
\(n^{-3/10}\), and select one actual path per occupied bin. This proves
(17). Linear response changes by at most
\(C(1+T_n)n^{1/400}\|x\|_2\|a-\widetilde a\|_\infty\),
and a quadratic pairing changes by the same factor with \(\|x\|_2^2\).
Thus the approximation error is \(o(n^{-1/5})\) on \(\|x\|_2\le C_r\).
The Gaussian failure exponent dominates (17).

Terminal times can be covered by a polynomial-size net. On the stopped
finite-dimensional tube all time derivatives of the displayed response
operators have polynomial-in-\(n\) bounds: the first three derivatives
of tanh are globally bounded, and every remaining coordinate is bounded by a
polynomial from its Euclidean bound. The linear fundamental solution and
its time derivatives satisfy the same bound by (10). Taking a sufficiently
fine polynomial mesh extends the inequalities to all terminal times,
including the reference stop endpoint. This adds only \(O(\log n)\) to
the logarithmic net cardinality. Conditional on retained initialization,
the stopped reference and these nets are deterministic. No conditioning
on a full-network event is used when applying the Gaussian formulas.

## 5. Trace estimate on an empirical-budget stop

The already checked finite Schatten argument applies to every interval
\([s,t]\subset[0,\sigma]\). Its proof uses only the activity measure and
the budget bound, so (3) gives
\[
 \sup_{s\le t\le\sigma}
 \frac{\|J(t,s)-U_0(t,s)\|_{\rm HS}}{\sqrt n}
       \le CS+CS^2\sqrt B.                          \tag{18}
\]
The constant absorbs a fixed \(\eta^{-1}\); the smallness condition is
\(CS^2\le\eta/2\). For the residual forcing \(Q_a\) in (12), use
the rank bound \(n\), contraction of \(U_0\), and (11):
\[
 \frac{\|B_b(t)J(t,s)Q_a(s)\|_{\rm HS}}{\sqrt n}
 \le C|r_a^0(s)|[1+CS+CS^2\sqrt B].                 \tag{19}
\]
Integration, \(|a_a|\le1\), and
\(|\operatorname{tr}R|/n\le\|R\|_{\rm HS}/\sqrt n\)
bound this part of the trace by \(CS+CS^3\sqrt B\).
The direct external derivative contributes at most \(CS\).

For the adaptive forcing \(P_a\), use its rank **one**, instead of
discarding this finite-rank structure:
\[
 \frac1n|\operatorname{tr}(B_b(t)J(t,s)P_a(s))|
 \le\frac{C}{n}\|J(t,s)\|_{\rm op}\|P_a(s)\|_{\rm op}
 \le CS n^{-1+1/400}.                              \tag{20}
\]
The time integral is at most \(CS T_n n^{-1+1/400}=o(1)\).
Equations (19)--(20) prove (8), subject to reconstructing (18) on the
precise stopped cavity interval. The external control enters only through
its amplitude in this trace calculation.

## 6. Autonomous cavities and transfer of stopping times

The remainder of this note completes the finite probability argument using
the local lemma just proved. Its complete collaborator reconstruction is
`Q_ORDER_POSITIVE_PROBABILITY_CHECK.md`.

Let the full dense network have two tanh hidden layers, canonical Gaussian
initialization and zero initial readout. Assume its fixed initialized
population feature Gram has a positive gap. Fix a full initialization
event with a strict positive Gram margin, operator bounds, and the
manuscript's first-layer bounds. Its probability tends to one. Deleting
any fixed number of first-layer neurons preserves a smaller fixed Gram
margin, simultaneously for every deletion set of that size: the omitted
initialized contribution to a top preactivation has Euclidean norm at
most \(K\sqrt r\), so the normalized feature and Gram changes are
\(O(\sqrt{r/n})\). The operator and first-layer bounds do not increase.
The deterministic fitting proof applies to the rectangular cavity with
the same normalization \(n\). Fix one \(\kappa>0\) below the fitting
rates for both the full network and all these cavities, using the smaller
Gram margin. Set
\[
 Y=\left(m^{-1}\sum_a y_a^2\right)^{1/2},\qquad S=2Y/\kappa.
\]
The constants and label threshold are independent of each fixed deletion
count; only its sufficiently-large-width threshold depends on that count.
The case \(Y=0\) is stationary and needs no division by \(S\).

For \(Y>0\), put \(K_i(t)=\max_a|k_{a,i}(t)|\). Use the
full maximum cap \(M_n=A_0S\log n\), full cumulative budget cap \(B\),
and physical terminal time \(T_n=c_T\log n\). Let \(\sigma_n\) be
the first full cap time, limited by \(T_n\). Each autonomous cavity
with deleted set \(I\) has its own analogous stop \(\sigma_{-I}\)
with caps \(2M_n,2B\). The budget is (3) with the full or corresponding
cavity carriers. The stopping time \(\sigma_n\) is distinct from the
algorithm's residual-RMS clock \(\tau\).

The actual omitted first-layer histories are admissible external controls
on every common prefix. With \(G_{ab}=v_a^\top v_b\),
\[
 \frac{d}{dt}h_{a,i}^{(1)}
 =-\frac2m\sum_b r_bG_{ab}
   \operatorname{sech}^2z_{a,i}^{(1)}
   \operatorname{sech}^2z_{b,i}^{(1)}k_{b,i}.
 \tag{21}
\]
Their absolute values are at most one and derivatives at most
\(C\rho M_n\le C\log n\) before the full stop. Constant extension
of any such prefix lies in (4). The actual learned omitted column obeys
\[
 \|W_{:,i}(t)-W_{0,:,i}\|_2
 \le \frac1{\sqrt n}\int_0^t\|w(s)\|_\infty\,d\mu(s)
 \le\frac{S^2}{2\sqrt n},\qquad
 d\mu=\frac2m\sum_a|r_a|dt.                         \tag{22}
\]
Here \(\|w(t)\|_\infty\le\mu([0,t])\) and \(\mu([0,\infty))\le S\).
Multiplying by bounded omitted activations and summing a fixed number of
columns gives the allowed adaptive source \(\zeta\).

For each fixed deletion count, union the conditional insertion events over
all its deletion sets. On the common initialization event their failure
probability is at most \(C_rn^r e^{-n^{2/5}}=o(1)\). Apply the local
lemma only until \(\min(\sigma_n,\sigma_{-I})\). It gives retained
carrier discrepancy \(\varepsilon_{n,r}\le C_rn^{-1/10}=o(1)\).
A cavity cannot reach its maximum cap first, since at such an endpoint
its maximum is at most \(M_n+\varepsilon_{n,r}<2M_n\).
For the budget, the sharper relative estimate is
\[
 e^{\eta K_i^{(-I)}(t)/S}
 \le e^{\eta\varepsilon_{n,r}/S}e^{\eta K_i(t)/S},
 \qquad i\notin I.
\]
Thus on the common prefix
\[
 \mathcal M_\eta^{(-I)}
 \le e^{\eta\varepsilon_{n,r}/S}\mathcal M_\eta+O(r/n)
 \le B+o(1)<2B.                                    \tag{23}
\]
The added term allows zero-filling deleted coordinates and is absent if
they are omitted from the sum. Consequently \(\sigma_{-I}\ge\sigma_n\).
Continuity and the strict margins justify reaching the cap endpoint.
This is a comparison on a common prefix followed by continuation; it does
not assume the desired cavity survival when applying the lemma.

## 7. Gaussian reinsertion and fixed-block empirical moments

Freeze each cavity top response at its own stop, and set it to zero if
its cavity-measurable initialization conditions fail:
\[
 d_a^{-I}(t)=\delta_a^{(-I)}(t\wedge\sigma_{-I}),
 \qquad 0\le t\le T_n.
\]
This proof reference excludes every initialized column \(x_i\),
\(i\in I\). Its deterministic normalized bounds are
\[
 d_a^{-I}(0)=0,\quad
 \sup_t\|d_a^{-I}(t)\|_2/\sqrt n\le CS,\quad
 \operatorname{Var}(d_a^{-I})/\sqrt n\le CS.          \tag{24}
\]
Indeed \(\dot\delta_a=\operatorname{sech}^2z_a\odot\dot w+
w\odot\tanh''z_a\odot\dot z_a\) has normalized norm at most
\(C\rho\), whose integral is \(CS\). Freezing creates no jump.
Given the retained initialization, define
\[
 Z_i^{-I}=\frac1S\max_a\sup_{t\le T_n}|x_i^\top d_a^{-I}(t)|,
 \qquad i\in I.
\]
These are conditionally independent, and for every fixed \(\lambda\ge0\)
there is a deterministic finite constant \(L(\lambda)\) such that
\[
 \mathbb E[e^{\lambda Z_i^{-I}}\mid\text{retained initialization}]
 \le L(\lambda).                                   \tag{25}
\]
The constant is independent of every fixed deletion count. To verify it,
parameterize the normalized curve in (24) by its bounded arc length.
An arc-length net at scale \(2^{-j}\) has \(C2^j\) points. The
Gaussian increments at that level have standard deviations at most
\(C2^{-j}\). A Gaussian tail and union bound, followed by summing over
levels, give
\(\Pr\{Z_i^{-I}>C(1+u)\mid\text{cavity}\}\le Ce^{-cu^2}\).
The finite sample maximum only changes constants. Integration gives (25).

Singleton insertion supplies an actual carrier comparison, not a Gaussian
law for the trained coordinate. Combine (5), (7), (8), and (22): through
the full stop,
\[
 |k_{a,i}(t)-x_i^\top d_a^{-i}(t)|
 \le R(B,S)+o(1),\qquad R(B,S)=CS(1+S^2\sqrt B).
 \tag{26}
\]
In detail, the top response is its cavity response plus its linear
response \(R_{a,a(\cdot)}x_i\) and an \(O(n^{-1/10})\) Euclidean
remainder. Pair the remainder with \(\|x_i\|_2\le C\), use the
quadratic-form estimate on the linear term, and add
\(|(W_{:,i}-x_i)^\top\delta_a|\le S^3/2\).
The constant in (26) belongs to singleton insertion and does not depend
on the moment order used below.

Different singleton Gaussian references are not independent. For a fixed
set \(I\ni i\), full-to-singleton and full-to-\(I\) comparisons give
\[
 \sup_{a,t\le\sigma_n}\|d_a^{-i}(t)-d_a^{-I}(t)\|_2
 \le C_{|I|}n^{1/100}.                              \tag{27}
\]
Both processes exclude \(x_i\), but the validity event and full prefix
in (27) need not be independent of it. Resolve this by projecting their
difference onto the deterministic Euclidean ball of radius
\(C_{|I|}n^{1/100}\), enlarging that constant to dominate (27).
The projected process remains independent of \(x_i\), is bounded by
that radius on every retained outcome, and has normalized total variation
at most \(CS\), because Euclidean projection is 1-Lipschitz.
It agrees with the unprojected difference on the successful full prefix.

The Gaussian pairing with this projected process has standard deviation
at most \(D_n=C_{|I|}n^{-1/2+1/100}\), and metric covering number at
scale \(u\) at most \(1+CS/u\). Dyadic chaining from scale \(D_n\)
bounds its mean supremum by
\(CD_n\sqrt{\log(e+S/D_n)}\), and its tail at \(n^{-1/5}\) by
\(C_{|I|}e^{-n^c}\) for a fixed \(c>0\). Therefore, outside a
superpolynomially small event, simultaneously over every fixed-size block,
\[
 \max_{a,t\le\sigma_n}
 |x_i^\top(d_a^{-i}(t)-d_a^{-I}(t))|\le n^{-1/5}.
 \tag{28}
\]
The full stopping event has not been conditioned upon at any stage.
The radial projection is an auxiliary proof reference, not an alteration
of the training algorithm.

Let \(\mathcal G_n\) denote the common full initialization event, and put
\[
 H_n=\mathbf1_{\mathcal G_n}\frac1n\sum_i
       \exp\left\{\frac\eta S\sup_{t\le\sigma_n}K_i(t)\right\}.
\]
The stopped maximum gives \(H_n\le n^{\eta A_0}\). Fix any integer
\(p\ge1\), independently of width. Union the insertion and projection
events for all deletion sets of size at most \(p\). Their failure on
\(\mathcal G_n\) is at most \(C_pn^{C_p}e^{-n^c}\), so its
contribution to \(\mathbb EH_n^p\) vanishes even after multiplication
by \(n^{p\eta A_0}\).

For a tuple of \(p\) distinct indices, use their set as the common
deleted block. Equations (26)--(28) bound its exponential product by
\[
 e^{p\eta[R(B,S)+o(1)]/S}\prod_{i\in I}e^{\eta Z_i^{-I}}.
\]
Drop the nonnegative full-prefix and good-event indicators before taking
the conditional expectation. Conditional independence and (25) give
the bound \([e^{\eta R(B,S)/S}L(\eta)]^p+o(1)\).
For a tuple with fewer distinct indices, of multiplicities \(d_j\)
summing to \(p\), the same argument gives the finite constant
\(e^{p\eta R(B,S)/S}\prod_jL(d_j\eta)+o(1)\).
There are only \(O_p(n^{p-1})\) such collision tuples, so their
normalized contribution vanishes. Hence, for every fixed \(p\),
\[
 \limsup_{n\to\infty}\mathbb EH_n^p
 \le D(B,S)^p,\qquad
 D(B,S)=L(\eta)e^{C\eta(1+S^2\sqrt B)}.              \tag{29}
\]
The base \(D(B,S)\) is independent of \(p\). Constants in collision
moments and width thresholds may depend on \(p\), which is harmless.
All columns in a fixed block are deleted simultaneously; iterating
deletions with successively doubled stops would not justify this argument.

## 8. Closing the caps and obtaining the actual all-time maximum

Choose \(\eta,A_0>0\) first, and then a fixed
\(B>4L(\eta)e^{C\eta}\). Choose the small fixed label threshold so
that the local insertion lemma, \(CS^2\le\eta/2\), and
\(e^{C\eta S^2\sqrt B}\le2\) all hold, with strict margins.
These choices are independent of confidence, width, order, and every
fixed empirical moment degree. They give \(D(B,S)<B\).

If the budget cap is reached by \(\sigma_n\), its cumulative value
\(B\) is at most \(H_n\), since the deterministic time weight has
mass at most one. Equation (29) and Markov's inequality imply for every
fixed \(p\)
\[
 \limsup_n\Pr\{\mathcal G_n,\text{budget cap reached by }T_n\}
 \le[D(B,S)/B]^p.
\]
Take the infimum over fixed integers \(p\). The right side tends to
zero; thus budget stopping has probability tending to zero. The order of
limits is width first at a fixed moment degree, then moment degree to
infinity. No growing-degree cavity theorem is assumed.

Likewise, (26) and the Gaussian supremum tail proving (25) give
\[
 \Pr\{\mathcal G_n,\text{maximum cap reached by }T_n\}
 \le o(1)+Cn\exp\{-c(A_0\log n-C_B)^2\}\longrightarrow0.
\]
Thus both stops are excluded through \(T_n\) with probability tending
to one. This proves a high-probability finite budget bound, not an
expectation bound on every unstopped fitting trajectory.

On the same successful-stop event, (26) and a second Gaussian union bound,
now at a fixed sufficiently large multiple of \(\sqrt{\log(e+n)}\),
give
\[
 \max_{a,i,t\le T_n}|k_{a,i}(t)|
 \le C S\sqrt{\log(e+n)}                            \tag{30}
\]
with probability tending to one. The constant can be fixed once so that
the Gaussian union failure is, for example, \(O(n^{-2})\); the other
failure terms need only tend to zero. The bounded shift in (26) is
absorbed into the same constant, uniformly over the chosen small-label
range.

For the actual dense carrier, differentiation of \(k_a=W^\top\delta_a\)
and the all-time physical bounds give
\[
 \frac{\|k_a(t)-k_a(T_n)\|_2}{\sqrt n}
 \le CS e^{-\kappa T_n},\qquad t\ge T_n.             \tag{31}
\]
Choose \(c_T\kappa>1/2\). Then the remaining coordinate drift is
\(o(S)\), so (30) extends to every physical time. The top carrier is
the readout and has \(\|w\|_\infty\le S\). Consequently there are
events \(\Omega_n\), of probability tending to one, on which
\[
 \sup_{t\ge0}\max_{a,i}|k_{a,i}^{(1)}(t)|
       +\sup_{t\ge0}\|w(t)\|_\infty
 \le C S\sqrt{\log(e+n)}.                           \tag{32}
\]
If an all-time version of the stopped exponential budget is desired,
choose additionally \(c_T\kappa>\eta A_0\); (31) and the already
proved maximum make its remaining deterministic-weight integral vanish.
Only the maximum (32) is used in the following tracking conclusion.

## 9. Consequence for the actual autonomous Legendre closure

**Unconditional same-width theorem.** Fix two tanh hidden
layers, fixed finite data with a positive initialized feature-Gram gap,
and the canonical independent Gaussian initialization with zero readout.
For sufficiently small fixed label RMS \(Y\), independent of width,
closure order, and confidence, compare the dense network and the actual
autonomous Legendre closure from the same initialization. Retain the
original clock \(\dot\tau=\rho\), \(\tau(0)=1\), and every original
unclipped update. For every fixed test-input probability law \(\mu\)
with finite second moment, there are constants \(C_\mu,K>0\) and
events of probability tending to one such that, simultaneously for every
order \(q\ge1\),
\[
 \mathcal E_\mu(\widehat f_{n,q},f_{n,D})
 \le C_\mu\exp\{K\sqrt{\log(e+n)}\}
          \frac{\sqrt{\log(e+q)}}{q^2},              \tag{33}
\]
where
\[
 \mathcal E_\mu(g,f)
 =\left(\int\sup_{t\ge0}|g(t,x)-f(t,x)|^2d\mu(x)\right)^{1/2}.
\]
In particular, choose any fixed \(A_1>K/2\), and define
\[
 q_n=\left\lceil n^{1/4}
             \exp\{A_1\sqrt{\log(e+n)}\}\right\rceil.
 \tag{34}
\]
Then \(q_n=n^{1/4+o(1)}=o(n)\), and on those events
\[
 \mathcal E_\mu(\widehat f_{n,q_n},f_{n,D})
 \le C_\mu n^{-1/2}.                               \tag{35}
\]
Equivalently, for each \(\delta>0\) the assertion holds with
probability at least \(1-\delta\) at every sufficiently large width;
the required width may depend on confidence, the fixed input data, and
the fixed label vector. Nonzero labels are fixed before taking the width
limit; a width threshold uniform as \(Y\downarrow0\) is not asserted.
It includes the fitted
endpoint and the time supremum inside the test-input integral.

To obtain (33), use the previously checked two-layer defect estimate
\[
 \int_0^\infty\|E_2(t)\|_Fdt
 \le CY^{5/2}q^{-2}\sqrt{\log(e+q)}
\]
for the actual unclipped closure, proved in
`NONORTHOGONAL_DIRECT_ROUTE.md`. The dense-only damping estimate is
\(D_{n,q}\le C e^{C_0YM}(\epsilon_q+Z_n(M))\).
On \(\Omega_n\), choose \(M=CS\sqrt{\log(e+n)}+1\).
Then the dense carrier tail \(Z_n(M)\) is exactly zero, by (32).
No clipping has been put in either differential equation. These bounds
give the corresponding normalized parameter inequality (33); the
manuscript's whole-input estimate multiplies it by the finite constant
\(C_\mu\). Substituting (34) gives
\[
 C_\mu n^{-1/2}\sqrt{\log(e+n)}
       e^{-(2A_1-K)\sqrt{\log(e+n)}}\le C_\mu' n^{-1/2},
\]
which proves (35). Constants can retain the smaller exponent proportional
to \(Y^2\), but that refinement is unnecessary for the conclusion.

For fixed \(m,d\), the moving state in (34) has size
\(O(n^{5/4}e^{A_1\sqrt{\log(e+n)}})\), a vanishing fraction of
the dense learned matrix. The initialized \(n\)-by-\(n\) matrix is
still stored and applied exactly. No finite-to-population convergence
rate, new carrier-moment assumption, diagonalization of the input Gram,
or changed clock is used.

The theorem is deliberately scoped to two tanh hidden layers. The next
section removes the separate Gram condition for each fixed normalized
dataset with compatible duplicate/antipodal labels. Inconsistent labels
with a persistently positive original residual clock are outside this
proof, as is arbitrary depth. The local and probability reconstructions
give an internal PASS for this final scope; they are collaborator checks,
not isolated promotion reviews.

## 10. Fixed positive weights and arbitrary compatible sphere data

The proof also holds for fixed positive sample weights \(p_a\),
\(\sum_a p_a=1\). Replace the average over samples by its weighted
version, set \(\rho^2=\sum_a p_ar_a^2\), and use
\[
 F(\Theta,e)=-2\sum_a p_ar_a\nabla_\Theta\mathcal F_a,
 \qquad
 L=\sqrt{2/n}[\sqrt{p_a}\nabla\mathcal F_a]_a,
 \qquad d\mu=2\sum_a p_a|r_a|dt\le2\rho\,dt.
 \tag{36}
\]
The exact adaptive term is still \(-LL^\top\). The external terms
are now
\[
 P_a=-\frac{2p_a}{n}\nabla\mathcal F_a\delta_a^\top,
 \qquad Q_a=-2p_ar_aB_a^\top.
\]
Their rank, normalization, and all trace arguments are unchanged.
The bounds on individual residuals and normalized residual directions use
\(|r_a|\le\rho/\sqrt{p_a}\); their constants may depend on the fixed
smallest weight. The fitting and projection arguments use weighted sample
RMS and the positive weighted readout-feature Gram
\[
 \operatorname{diag}(\sqrt p)\,
       H^{(2)\top}H^{(2)}\,
       \operatorname{diag}(\sqrt p)/n.
\]
Here \(H^{(2)}\) is the matrix with columns \(h_a^{(2)}\).
Cauchy--Schwarz in the sample weights gives every activity estimate used
above. The two-layer absolute defect proof replaces each sample average
by \(\sum_a p_a\), while its two history factors, \(q^{-2}\) order,
and \(\sqrt{\log(e+q)}\) loss remain the same. These substitutions
establish (33)--(35) for fixed positive weights.

Now let the original training vectors satisfy \(\|v_a\|_2=1\).
Partition them into classes under equality up to sign, choose one unit
representative \(u_j\) per class, and write
\(v_a=s_au_j\), \(s_a\in\{-1,1\}\). Assume label compatibility:
there is a class label \(\bar y_j\) with \(y_a=s_a\bar y_j\) for
every member of that class. This includes arbitrary distinct nonantipodal
inputs with arbitrary labels. Put \(p_j=|I_j|/m>0\).

Oddness of tanh and evenness of its derivative give, at every parameter
state, \(h_a^{(\ell)}=s_ah_j^{(\ell)}\),
\(f_a=s_af_j\), and \(\delta_a^{(\ell)}=\delta_j^{(\ell)}\).
Hence the full dense updates are exactly the weighted updates on the
representatives. The autonomous closure has the same exact quotient:
its forward moments have sign \(s_a\), and its representative backward
moments are the signed class averages
\(\bar\delta_{j,k}=|I_j|^{-1}\sum_{a\in I_j}s_a\bar\delta_{a,k}\).
Substituting these into reconstruction gives the weighted representative
formula with weights \(p_j\). In particular,
\[
 \rho^2=\sum_jp_j(f_j-\bar y_j)^2,
 \qquad Y^2=\sum_jp_j\bar y_j^2,
 \qquad\dot\tau=\rho,
\]
so the physical dynamics and original clock are preserved exactly.

The representatives are pairwise nonproportional. Their first tanh
Gaussian feature covariance is positive definite: a null quadratic form
would give a continuous identity \(\sum_jc_j\tanh(u_j^\top x)=0\)
for all \(x\). Applying one finite difference perpendicular to every
representative except a fixed one removes all the other summands and
forces a sufficiently high scalar finite difference of tanh to vanish.
Mollification and differentiation in the step sizes would make tanh a
polynomial, contrary to bounded nonconstancy. For a single representative
its nonzero Gaussian feature variance gives positivity directly. A
positive Gaussian covariance in the next layer has full support; varying
one coordinate in any proposed tanh feature identity gives positivity
there as well. Multiplication by positive square-root weights preserves
the gap. The complete quotient/positivity proof and its checked edge
cases are `DATA_QUOTIENT_CLOCK.md` and `DATA_QUOTIENT_CHECK.md`, both
read in full for this extension.

Thus (33)--(35) apply to **every fixed finite sphere dataset with
compatible duplicate/antipodal labels**, without an independent Gram
assumption and without orthogonality. The constants and positive fixed
label threshold depend on the actual dataset; no uniformity over
colliding geometries is claimed. The test law \(\mu\) is arbitrary
with finite second moment and imposes no assumption on unseen labels.
If the compatibility condition fails, the original residual RMS contains
an irreducible constant term and the exact quotient clock changes to
\(\sqrt{\sum_jp_j(f_j-\bar y_j)^2+\sigma^2}\), with
\(\sigma>0\). That case is not covered by this all-order proof.
