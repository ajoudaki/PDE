# Single-sample audit of order-based all-time error claims

This scoped theoretical audit concerns the actual derivative-dictionary model: fixed axis probes independent of the training input and label, complete middle replacement, positive ridge normalization, and trainable read-in and readout. It uses only DERIVATION.md, FACTORIZATION.md, ORDER_COUNTS.md, P7_DICTIONARY_SPEC.md and P7_DERIVATION.md, with the canonical model/initialization checked in the opening of `docs/global_nonlinear.md`. That opening theorem has a different activation and is not imported as a tanh theorem. No training or numerical experiment was run.

The conclusion is a proof-route obstruction, not a proof that this dictionary cannot converge as its order grows. The implemented finite network does not have exact matching initial output jets, even for one axis sample. Its order counts describe factors of the original network's learned middle increment. They do not provide a quantified approximation of the compressed initialization or its later vector field. A valid order-dependent all-time error theorem therefore needs additional estimates.

## 1. The actual initialization is a ridge-filtered action

Write `A0=W^(2)(0)`, let `R_l` be the raw feature tables, and use the normalized empirical inner product `v^T w/n`. Ridge Cholesky normalization with positive scalar ridge `eta_l` gives

\[
 G_l=R_l^TR_l/n,\qquad
 Q_l=B_lB_l^T/n
     =R_l(G_l+\eta_l I)^{-1}R_l^T/n.
\]

This identity is independent of the triangular orientation used to whiten the table. The prescribed coefficient initialization and lift give the exact identity

\[
 M_0=B_2^TA_0B_1/n,\qquad
 \widehat A_0=B_2M_0B_1^T/n=Q_2A_0Q_1.                 \tag{S1}
\]

For a nonzero raw Gram eigenvalue `lambda`, the corresponding eigenvalue of `Q_l` is `lambda/(lambda+eta_l)`, strictly between zero and one. Consequently `Q_l` is not an orthogonal projection, including on the retained span. Writing `P_l` for the orthogonal projection onto that span gives

\[
 \|(P_l-Q_l)|_{\operatorname{ran}P_l}\|_{op}
 =\frac{\eta_l}{\lambda_{l,\min}^{+}+\eta_l}.          \tag{S2}
\]

The formula follows by singular value decomposition of `R_l/sqrt(n)`. It identifies a necessary spectral quantity: a prescribed ridge decreasing with order is not itself a decay estimate for ridge bias if the positive Gram eigenvalues also decrease. Rescaling raw columns preserves their span and changes these filters; the factorial scales in the specification therefore matter to the dynamics.

For a current compressed state, define `h=tanh(W1 x/sqrt(2))` and `delta=c tanh'(Ahat h)`. Under singleton unhalved loss `(f-y)^2`, the coordinate gradient and its lift are

\[
 \dot M=2(y-\widehat f)
 (B_2^T\delta/n)(B_1^Th/n)^T,
\qquad
 \dot{\widehat A}
 =2(y-\widehat f)Q_2(\delta h^T/n)Q_1.                \tag{S3}
\]

Thus positive ridge changes the lifted training metric as well as initialization. Replacing `Q_l` by exact orthogonal `P_l` in a proof changes the implemented model unless the resulting discrepancy is controlled.

## 2. An exact finite-width obstruction, including the random readout

For each fixed nonzero training input `x`, put

\[
 h_0=\tanh(W^1_0x/\sqrt2),\quad
 H_0=\tanh(A_0h_0),\quad
 \widehat H_0=\tanh(Q_2A_0Q_1h_0).
\]

The following applies to the specified fixed-order raw lists, which contain the basic lower axis features and upper `U_ab`, use fixed population constants, and consist of real analytic expressions in the hidden initialized arrays. Positive ridge keeps the inverse in (S1) nonsingular. No task-dependent rank pruning is allowed in the p7 specification.

**Proposition.** At every fixed finite width and positive ridge, `Hhat0 != H0` almost surely under the full-density Gaussian hidden initialization. With the actual independently initialized `c0_i ~ N(0,n^(-2))`, the two initial scalar predictions differ almost surely.

**Proof.** First exhibit hidden arrays for which a component of `Hhat0-H0` is nonzero. Choose every first-layer row equal to one row `v` such that `v.x != 0` and at least one axis coordinate of `v` is nonzero; take `A0=w 11^T/n`, with `w != 0`. Every raw feature column is constant across neurons, since the construction uses coordinate operations, the actual action and transpose, and fixed scalar contractions. Both raw tables contain a nonzero column. If `P=11^T/n`, then `Q_l=q_l P` for numbers `0<q_l<1`. Also `A0 h0=z 1` with `z != 0`, so

\[
 \widehat H_0-H_0
 =\bigl[\tanh(q_1q_2z)-\tanh z\bigr]\mathbf1\ne0.
\]

Each component of this difference is real analytic in all hidden entries. At least one is not identically zero by the witness. A nonzero real analytic function on Euclidean space has a Lebesgue-null zero set: in dimension one its zeros are isolated; inductively, on a product neighborhood expand in one coordinate about a fixed value, choose a coefficient which is not identically zero in the remaining coordinates, apply the induction hypothesis to its zero set and then the one-dimensional result on every other slice. A countable cover by such neighborhoods and Fubini's theorem complete the argument. Gaussian full density therefore makes `Hhat0=H0` a null event.

Conditioned on the hidden arrays, independence of `c0` gives

\[
 \widehat f(0,x)-f(0,x)
   =c_0^T(\widehat H_0-H_0)/n,\qquad
 \operatorname{Var}\bigl(\widehat f(0,x)-f(0,x)\mid W^1_0,A_0\bigr)
   =\|\widehat H_0-H_0\|_2^2/n^4>0.
\]

A nondegenerate Gaussian scalar is zero with probability zero. This proves the proposition. The degenerate hidden arrays used above only certify that an analytic expression is nonzero; they are not being claimed to be typical initializations. QED.

In particular, an error estimate `|fhat(t,x)-f(t,x)| <= C t^(p+1)` near zero, or any exact output-jet matching assertion including order zero, is false for the actual finite model at every fixed positive-ridge order. The initial discrepancy may decrease with width or order; this proposition does not supply a nonvanishing limit or disprove convergence in either limit. Its conditional standard deviation is `n^(-3/2)||Hhat0-H0||_n`.

Setting the finite readout to zero repairs only the zeroth output coefficient. At width one, the same argument is especially explicit: `Hhat0=tanh(q1 q2 z)` and `H0=tanh z`. For `y != 0`, both hidden velocities vanish initially and

\[
 \dot f(0)=2y\tanh^2z,\qquad
 \dot{\widehat f}(0)=2y\tanh^2(q_1q_2z).
\]

These slopes differ strictly almost surely. This is an algebraic finite-width zero-readout example; it is not a Gaussian population counterexample.

## 3. Removing ridge alone does not supply the missing seeds

ORDER_COUNTS.md explicitly counts increment factors without the initialization/action seed fields. At its orders two and three, the upper space is

\[
 \operatorname{span}\{H_1(1-H_1^2),H_2(1-H_1^2),
                     H_1(1-H_2^2),H_2(1-H_2^2)\}.
\]

Every member of this finite population span is bounded. The initial upper preactivation `Y_a=A0 h_a` is a nondegenerate Gaussian, hence essentially unbounded, and cannot belong to that span. With an exact lower projection retaining `h_a` and any exact upper projection onto this span,

\[
 P_2A_0P_1h_a=P_2Y_a\ne Y_a.
\]

Tanh is injective, so the initial upper feature also changes in `L2`. This is a definite population initial-state mismatch for the low-order increment dictionary. It does not alone prove a nonzero scalar output-slope discrepancy, since equality of two norms could occur without equality of their vectors.

FACTORIZATION.md's larger computation-graph construction includes the missing `Y_a` and other arguments/results, and correctly states what exact orthogonal call preservation would require. P7_DERIVATION.md instead specifies factors sufficient for the middle increment through power eight, with separate warnings about population differentiability. Its field containment statement is not a theorem that the whole-replacement dynamics has the corresponding original-network jets. This audit does not claim that no linear combination of later actual Gaussian fields can recover a particular seed; such noncontainment would require an additional proof.

## 4. The one-sample reduction and its precise limits

For any finite version of either network, using its actual positive parameter metric, let `K(t)` be the squared norm of the gradient of the scalar training prediction in that metric. For `(f-y)^2`, the chain rule gives

\[
 \dot f=2(y-f)K(t),\quad K(t)\ge0,\qquad
 f(t)-y=(f(0)-y)\exp\!\left(-2\int_0^tK(s)\,ds\right). \tag{S4}
\]

This remains true for the ridge coefficient model: its middle contribution is the Euclidean squared norm of the `M` prediction gradient, not the dense-middle gradient norm. All finite flows exist for all finite times. Indeed, energy dissipation bounds the integral of squared metric speed by the initial loss; Cauchy--Schwarz bounds displacement on `[0,T]` by `sqrt(T L(0))`. A finite-dimensional smooth vector field on the resulting bounded ball cannot have finite-time escape.

For zero initial readout, both predictions remain in the segment joining `0` to `y`; consequently

\[
 \sup_{t\ge0}|f(t,x)-\widehat f(t,x)|\le |y|.          \tag{S5}
\]

This is a valid all-time scalar bound with no improvement in order. If both flows fit their training label, their training-output endpoint difference is exactly zero, independently of dictionary accuracy. Fitting itself requires `int_0^infty K=+infty` when the initial residual is nonzero and has not been assumed or proved here for the general tanh closure.

An instructive conditional reduction is: if both kernels are bounded below by `kappa>0` and `sup_t |K(t)-Khat(t)| <= epsilon_p`, then for common zero readout,

\[
 \sup_{t\ge0}|f(t,x)-\widehat f(t,x)|
 \le |y|\epsilon_p/(e\kappa).                         \tag{S6}
\]

To verify it, write `A=int K`, `B=int Khat`. The mean-value bound is
`|exp(-2A)-exp(-2B)| <= 2 exp(-2 min(A,B))|A-B|`,
which is at most `2 epsilon_p t exp(-2 kappa t)`; its maximum is `epsilon_p/(e kappa)`. No estimate for `epsilon_p` or uniform positive `kappa` is established for this dictionary. Equation (S6) is a reduction, not an explicit order-rate theorem.

Single-sample fitting controls neither the complete hidden trajectory nor the whole-circle function. For example the bias-free width-one network
`f(u)=c tanh(w tanh(a u1+b u2))`, with `u=x/sqrt(2)`, can fit `f(e1)=y` by setting `c=y/tanh(w tanh a)` while varying `b` freely. At `u=e2`, choices `b=0` and `b=a` give predictions `0` and `y`. Both are finite networks of the correct activation/depth. This is an identifiability example, not a claim about two specified coupled training trajectories.

The fixed two-axis dictionary is not an input-aligned singleton dictionary. A new input already introduces `tanh(W1_0 x/sqrt(2))`; being able to evaluate it from the two Gaussian row coordinates does not put it in a fixed finite linear span. DERIVATION.md proves that arbitrarily many such directions can be linearly independent. Aligning probes with the real sample would change dictionary provenance. Restricting to an axis still requires the initialization and ridge checks above, and a singleton loss has a different factor of two from the equally weighted two-probe loss.

## 5. Finite matching jets alone cannot imply an all-time order rate

The following elementary example isolates this logical gap without pretending to be the experimental dictionary. Train on label one using half squared loss. The baseline scalar prediction is `f(q)=q`, starting at zero, so its output is `F(t)=1-exp(-t)`. For each integer `p>=1`, use instead

\[
 g_p(q)=q+A_pq^{p+1},\qquad
 \dot q=(1-g_p(q))g_p'(q),\qquad q(0)=0.
\]

The prediction `G_p(t)=g_p(q(t))` has the same Taylor coefficients through time order `p` as `F`: its scalar equation is `G_p'=(1-G_p)(g_p'(q))^2`, and `g_p'(q)^2=1+O(q^p)=1+O(t^p)`. Subtracting the equations and integrating gives `G_p-F=O(t^(p+1))`.

Choose `A_p=16^(p+1)/2`. Before `G_p` reaches `1/2`, `q' >= 1/2`, and `g_p(1/16)>1/2`. Thus its first hitting time `t_p` of output `1/2` is at most `1/8`. At that same time `F(t_p)<=t_p<=1/8`, so

\[
 |G_p(t_p)-F(t_p)|\ge3/8\qquad\text{for every }p.
\]

Both flows converge to the training output one: the surrogate parameter increases to the unique positive root of `g_p(q)=1`, and its derivative cannot vanish below that root. Thus agreement of arbitrarily many initial derivatives, and even exact agreement of endpoint training predictions, can coexist with an order-independent discrepancy at intermediate times. What fails is uniform control on the higher derivatives along the traversed interval: `A_p` grows rapidly with `p`. It falsifies the inference from finite jets alone, not the actual closure convergence conjecture.

## Remaining obligations for the actual model

An explicit error bound decreasing with order must estimate the omitted initial forward/adjoint calls, the relevant ridge Gram spectrum and induced metric discrepancy, the error produced on the reached nonlinear trajectory, and its propagation for all times. It must specify whether width is fixed or tends to infinity, and whether its observable is the training output, the whole-circle output, or the state. The finite random readout cannot be replaced silently by its zero population limit. A completed finite-order increment calculation supplies none of these missing all-time estimates automatically.

The strongest established statements here are (S1)--(S4), the almost-sure finite initialization mismatch, the low-order Gaussian seed obstruction, and the scalar reductions (S5)--(S6) with their stated hypotheses. Convergence or a nontrivial all-time order rate for the specified derivative dictionary remains open on these inputs.
