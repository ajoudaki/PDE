# Independent finite source derivation by deleting a neuron

Author: `/root/weighted_source_recovery`. This is parallel author research,
not an isolated review, an accepted theorem, or a replacement for the frozen
candidate. The main source file arrived while this derivation was in progress.
Its column-zeroing construction is different from the neuron-deletion
construction below. Both retain the actual finite reference readout.

The result below supplies (F13) of `FINITE_CAPTURE.md`, including the maximum
over a compact time interval and the entire input circle. It also supplies a
finite auxiliary-feature-flow bound whose population limit is uniform over
the fitted reference's whole physical trajectory. No experiment is used.

## 1. Exact finite objects and statement

Use the canonical two-hidden-layer tanh model with normalized input
`u=x/sqrt(2)`, stored middle matrix `A`, stored readout `c`, full first row
`w=(w_1,w_2)`, forward equations

\[
 h^1(u)=\tanh(wu),\qquad z^2(u)=Ah^1(u),\qquad
 h^2(u)=\tanh z^2(u),\qquad f(u)=c^Th^2(u)/n.
 \tag{D1}
\]

The independent initialized entries have variances `(1,1/n,1/n²)`. Every
finite Euclidean and Frobenius norm below is ordinary; all RMS factors are
displayed. Define

\[
 \delta(u)=c\phi'(z^2(u)),\quad Q(u)=A^T\delta(u),\quad
 F(z)=z/2+\sinh(2z)/4,\quad X_a=F(w_a)-F(g_a),\quad \phi=\tanh.
 \tag{D2}
\]

Then `w_a=J(X_a,g_a)` with `J_X=phi'(J)` and `|J_X|<=1`. Training the
reference atoms `(e1,+1),(e2,-1)` with weights one half, unhalved mean
squared loss and mobilities `(n,1,n)` gives exactly

\[
 X'_a=k_a Q_a,\qquad A'=\sum_a k_a\delta_a(h_a^1)^T/n,\qquad
 c'=\sum_a k_a h_a^2,\qquad k_a=-r_a,\quad r_a=f(e_a)-y_a.
 \tag{D3}
\]

The same notation is used for a separate auxiliary system in which the two
controls are prescribed deterministic continuous functions with
`|k_1|+|k_2|<=4`. This is a second theorem, not a claim that the finite
reference shares the population feature clock.

For either system on a fixed interval `[0,H]`, let

\[
 E_n=\{\|A_0\|_{op}\le10,\ \|c_0\|_\infty\le1,
                          \|g\|_F/\sqrt n\le2\},\qquad
 N_i=\sup_{t\le H,u\in S^1}|Q_i(t,u)|.
 \tag{D4}
\]

For every finite `p>=2`, the proof constructs a finite deterministic `K_H`
independent of `n,i` such that

\[
 \left(E[1_{E_n}N_i^p]\right)^{1/p}\le K_H\sqrt p.
 \tag{D5}
\]

It consequently proves every fixed moment of the envelopes

\[
 N_i,\qquad
 \bigl(\cosh^2g_{ia}+8H N_i\bigr)N_i,\qquad
 \bigl(|g_i|+8H N_i\bigr)N_i,
 \tag{D6}
\]

uniformly in `n,i` after multiplication by `1_E`. Averaging these inequalities
over `i` supplies (F13), with its exact weight
`W^#_ia=cosh²g_ia+2 sup_t|X_ia(t)|` bounded by the second envelope in (D6).
Constants depend on the horizon and fixed initialized norm thresholds;
there is no dependence on a perturbing law, atom weights or an input Gram.

## 2. Deterministic bounds and global finite existence

For physical GF, initial loss is at most four on `E_n`. Differentiating the
finite loss using (D3) gives its negative raw squared speed, with metric
`||dw||F²/n+||dA||F²+||dc||²/n`. Thus the loss cannot increase,
`sum_a|r_a|<=4`, and the raw displacement through `H` is at most `2sqrt(H)`.
The finite smooth ODE cannot escape in finite time: its raw displacement
bound makes the parameter path Cauchy at any proposed finite endpoint;
the local integral-equation contraction restarts it there.

For prescribed controls the following direct bounds instead prove
continuation. They hold for physical GF as well. Put

\[
 C=1+4H,\quad M=10+4CH,\quad W=2+4MCH,\quad \lambda=4CH.
 \tag{D7}
\]

Integration of (D3), bounded activations, and the rank-one norm identity give

\[
 \|c\|_\infty\le C,\quad \|A\|_{op}\le M,\quad
 \|w\|_F/\sqrt n\le W,\quad
 \sum_a\|X_a\|_2/\sqrt n\le4MCH.
 \tag{D8}
\]

Indeed `||c'||infty<=4`, `||A'||F<=4C` and
`sum_a||X'_a||2/sqrt(n)<=4MC`. The last estimate and
`|J(X,g)-g|<=|X|` yield the row bound. These finite bounds exclude escape in
the clock system; conversely the scalar chain rule gives (D3)'s exact raw
first-layer equation. The primitive is globally invertible because
`F'=cosh²>=1` and `F(z)` tends to opposite infinities at opposite ends.

All the bounds remain true for the neuron-deleted system below. Its
physical version has precisely the negative gradient of the same two-atom
loss on the reduced parameter arrays, with the normalization `n` unchanged.
Its initial prediction magnitude is at most one. There is no loss bound
imported from the full network into the cavity.

## 3. Remove one first-layer coordinate completely

Fix `i`. Delete the first-row root `g_i`, the first-neuron clock in both
input coordinates, and initialized column `a_i=A_0 e_i`. Run (D3) on the
remaining `n-1` first neurons and all `n` second neurons, retaining output
normalization `1/n` and middle rank factor `1/n`. Denote the middle matrix
of this rectangular network by `Ahat`, its remaining clocks by `Xhat`, and
its readout by `chat`. Its passive first hidden vector has `n-1` entries.
The case `n=1` means an empty first space and causes no exceptional term.

For physical GF its residuals are recomputed from its own predictions. For
prescribed controls it uses those same controls. Define

\[
 E_n^{(i)}=\{\|A_{0,-i}\|_{op}\le10,
       \|c_0\|_\infty\le1,\ \|g_{-i}\|_F/\sqrt n\le2\}.
 \tag{D9}
\]

This event and the entire cavity flow are independent of both `a_i` and
`g_i`. The event `E_n` is contained in (D9); we will never condition on
`E_n` when calling a Gaussian column independent.

The actual middle column obeys

\[
 \sup_{t\le H}\|A_i(t)-a_i\|_2\le\lambda/\sqrt n.
 \tag{D10}
\]

This is a coordinate bound from
`A'_i=sum_a k_a delta_a h^1_ai/n`, `|h^1_ai|<=1` and
`||delta_a||2<=C sqrt(n)`. Put `d_i=||a_i||2` and
`beta_i=(d_i+lambda)/sqrt(n)`. Uniformly over passive `u`, the omitted
forward contribution `A_i(t)h_i^1(t,u)` therefore has RMS at most `beta_i`.

Compare only the actual remaining clocks and columns with the cavity:

\[
 x=\sum_a\|X_{-i,a}-Xhat_a\|_2/\sqrt n,\quad
 a=\|A_{-i}-Ahat\|_F,\quad z=\|c-chat\|_2/\sqrt n,\quad e=x+a+z.
 \tag{D11}
\]

All three differences start at zero. No small operator-norm assertion is
made about removing the initialized column itself. Set
`R=a+Mx+beta_i`. The same-root bound for `J` gives, at every input,

\[
 \|z^2-zhat^2\|_2/\sqrt n\le R,\quad
 \|\delta-\deltahat\|_2/\sqrt n\le z+2CR,\quad
 |f-fhat|\le z+CR.
 \tag{D12}
\]

For the first inequality write the full forward action as
`A_-i h_-i+A_i h_i`; subtract the cavity by adding and subtracting
`A_-i hhat`. The feature difference has RMS at most `x`, the retained
matrix difference has operator norm at most `a`, and the missing column
is bounded by (D10). The other two inequalities follow by subtracting
the bounded-gate/readout products. The retained reverse query difference is

\[
 \|Q_{-i}-Qhat\|_2/\sqrt n
     \le Ca+M(z+2CR).
 \tag{D13}
\]

Let `D=sum_a|k_a-khat_a|`. For physical GF, (D12) implies
`D<=2(z+CR)`; for prescribed controls it is zero. Subtracting the three
equations in (D3), including their controls, proves for almost every time

\[
 \begin{split}
 x'&\le MC D+4\{Ca+M(z+2CR)\},\\
 a'&\le C D+4(z+2CR)+4Cx,\\
 z'&\le D+4R.
 \end{split}
 \tag{D14}
\]

For example the middle rank subtraction contributes the delta difference
times a hidden RMS at most one, and a hidden difference times readout RMS
at most `C`. The first equation compares only retained backward fields;
there is consequently no reverse injection in coordinate `i`. Norms of
absolutely continuous finite curves satisfy these derivative inequalities
at almost every time, including the usual integrated interpretation at
zeros of the norms.

The following explicit constants verify the scalar closure. Put

\[
 P=MC+C+1,\quad V=2C(M+1)+1,
\]
\[
 L=2P(1+CM)+4\{2C+M+1+VM\},\qquad J=2PC+4V,
 \quad D_H=JH e^{LH}.
 \tag{D15}
\]

Since `R<=Me+beta_i`, summing (D14) gives
`e'<=Le+J beta_i`, with a little positive slack in the coefficient of `e`.
Integrating the scalar inequality by successive substitution yields

\[
 \sup_{t\le H}e(t)\le D_H\,\beta_i.
 \tag{D16}
\]

Every constant in this deletion estimate is independent of the deleted
root and column, apart from the displayed `beta_i`. The actual finite
reference retains its random initial readout throughout the comparison.

## 4. Conditional Gaussian query and deterministic remainder

Define the scalar process

\[
 Z_i(t,u)=a_i^T\deltahat(t,u).
 \tag{D17}
\]

Conditional on the cavity arrays it is centered Gaussian, with covariance
`deltahat(t,u)^T deltahat(s,v)/n`. The actual query has the exact expansion

\[
 Q_i=Z_i+a_i^T(\delta-\deltahat)+(A_i-a_i)^T\delta.
 \tag{D18}
\]

(D10), (D12), and (D16) bound its last two terms by

\[
 d_i\{(1+2CM)D_H+2C\}(d_i+\lambda)+C\lambda.
 \tag{D19}
\]

Indeed multiplying the delta RMS difference by `d_i sqrt(n)` cancels the
`sqrt(n)` denominator in `beta_i`. Since `d_i<=10` on `E_n`, set

\[
 B_H=10\{(1+2CM)D_H+2C\}(10+\lambda)+C\lambda.
 \tag{D20}
\]

Then, simultaneously in time and input, `|Q_i-Z_i|<=B_H` on `E_n`.
The initialized column is not declared independent of the actual delta;
its dependent contribution is exactly (D18)'s second term.

For the cavity, direct differentiation using its deterministic bounds gives

\[
 \|\partial_t\deltahat(u)\|_2/\sqrt n
       \le L_t:=4+8C^2(1+M^2),\qquad
 \|\partial_\alpha\deltahat(u(\alpha))\|_2/\sqrt n
       \le L_\alpha:=2CMW.
 \tag{D21}
\]

In the first inequality `||zhat_t||RMS<=4C(1+M²)`, obtained by
differentiating the action and its bounded-gate first feature. In the
second, `||zhat_alpha||RMS<=M||what||RMS<=MW`. The readout derivative
supremum is at most four. Thus on `E_n^(i)`, the conditional Gaussian
process on `q in [0,1]²` corresponding to `t=Hq1, alpha=2pi q2` has
variance at most `C²` and increment standard deviation at most

\[
 L_0\|q-q'\|_1,\qquad L_0=HL_t+2\pi L_\alpha.
 \tag{D22}
\]

Here is the elementary Gaussian maximum estimate needed to finish. For
`N` centered jointly Gaussian variables of variance at most `v²`, their
maximum absolute value has tail at most `2N exp(-r²/(2v²))` by the scalar
Gaussian exponential moment and a union bound. Consequently its Lp norm,
`p>=2`, is at most
`v{sqrt(2log(2N))+2sqrt(p)}`. To verify the latter bound, subtract
`v sqrt(2log(2N))` and take its positive part. Its tail is at most
`exp(-r²/(2v²))`. Integrating to the even moment `2ceil(p/2)` gives an
upper bound `(2v²)^m m!`; `m!<=m^m` and monotonicity of Lp norms suffice.
No independence between these `N` variables is required.

Apply this estimate to square dyadic grids. A level-k parent increment has
standard deviation at most `2L0 2^-k`; there are at most `4^(k+1)` such
increments. Minkowski and the convergent sum of `2^-k sqrt(k+2)` bound
their total Lp cost by `60 L0 sqrt(p)`. The four initial corner values
cost at most `4C sqrt(p)`. Telescoping to arbitrary points is legitimate
because at fixed width (D17) has continuous coefficient functions. Thus

\[
 \left(E_{a_i}\sup_{t,u}|Z_i(t,u)|^p\right)^{1/p}
             \le64(C+L_0)\sqrt p\quad\hbox{on }E_n^{(i)}.
 \tag{D23}
\]

The conditioning is valid on the event in (D9), independently of `a_i`.
Using `E_n subset E_n^(i)` in (D18)-(D23) proves (D5) with the fully
specified constant `K_H=B_H+64(C+L0)`. This proof even gives a dominating
random variable independent of the deleted root `g_i`; independence is
not needed for the following simpler Hölder argument.

## 5. Own-gate weights and weighted tails

The exact identities

\[
 \partial_X\cosh^2J(X,g)=2\tanh J(X,g),\qquad
 \cosh^2J(X,g)\le\cosh^2g+2|X|
 \tag{D24}
\]

follow from `J_X=sech²J` and hold for either sign of `X`. Each individual
control has magnitude at most four, so
`sup_t|X_ia|<=4H N_i` and `sup_t|w_i|<=|g_i|+8H N_i`.
These prove the pathwise envelopes in (D6).

Gaussian roots have every fixed linear-exponential moment:
`E exp(q|G|)<=2 exp(q²/2)`. Hence Hölder and (D5) bound all fixed moments
of (D6), including any fixed finite product of these envelopes. There is
no assumption that the actual query and its root are independent. If `P_i`
is any one of the nonnegative source envelopes and `p>2`, then

\[
 E[1_{E_n}n^{-1}\sum_i P_i^2 1_{P_i>R}]
           \le R^{-(p-2)} E[1_{E_n}n^{-1}\sum_i P_i^p]
           \le C_{p,H}R^{-(p-2)}.
 \tag{D25}
\]

Markov's inequality proves the required uniform empirical square-tail
control in probability. Since the Gaussian matrix norm estimate and root
second-moment law give `P(E_n)->1`, the complement disappears in the
ordered limit `lim_R limsup_n`. Bounds in this section are proved directly
for actual continuous finite flows; no empirical higher moments have been
inferred from a W2 population limit.

## 6. Population passage and uniformity over physical time

For any finite list of times and passive inputs, B.1's transformed Euler
construction gives joint empirical W2 convergence of the full root,
clock, raw first row and passive Q. This includes actual small Gaussian
readout: the finite same-root clock/action/readout comparison handles its
vanishing supremum. To justify the passive reverse extension, append
`A*{c phi'(A phi(w.u))}` at each requested time to a fixed mesh program.
Bound the readout by (D8), clip it outside that bound, use A.1's continuous
at-most-linear instruction theorem for `J`, and apply the fixed-program
theorem jointly to both matrix orientations. The same-root clock stability
bounds the finite-flow/mesh and population-flow/mesh errors. In the middle
block use Frobenius/HS differences: the operator difference is at most
that norm and rank-one differences have the same bound in HS norm. Passive
Q differences obey (D12)-(D13)'s ordinary bounded-readout subtraction.
Thus width is taken first at every fixed mesh; the mesh is removed next.

Exactly that construction applies to the auxiliary constant controls
`k_a=y_a/2` on `[0,10]`, with zero limiting readout. Its finite readout may
be the actual Gaussian readout or zero; both converge to the same limit by
the preceding comparison. This gives the feature equation in C.4.5.1, not
a new population flow. That reference proof establishes
`0<=s(t)<s_dagger<=10` for every physical time.

Here is the moment passage, which does not ask the W2 theorem to supply
higher moments. At a fixed finite list of parameter pairs apply its weak
convergence to `min(R,max_j|Q(t_j,u_j)|^p)`. This is bounded continuous,
so convergence in probability of its empirical average implies convergence
of expectations. Inserting `1_E` changes the latter by at most `R P(E^c)`.
Use (D5), then let `R` increase. Next increase the finite lists to a fixed
countable dense set including both active directions. Monotone convergence
gives a measurable population envelope `N#` with

\[
 \|N^\#\|_p\le K_{10}\sqrt p,\qquad p\ge2.
 \tag{D26}
\]

Joint L2 continuity of passive Q extends domination to every fixed
deterministic time/input: approximate it by a dense sequence and choose
an almost surely convergent L2 subsequence. Thus `|Q(s,u)|<=N#` in each
L2 equivalence class. This does not assert continuous coordinate sample
paths in two parameters. Fubini is sufficient when integrating against
any fixed observation measure. Active clocks are coordinatewise absolutely
continuous by their integral equation, and hence
`sup_s|X_a(s)|<=5N#` for these particular controls. The exact bound (D24)+therefore gives

\[
 |\cosh^2w_a(s)Q(s,u)|\le(\cosh^2g_a+10N^\#)N^\#.
 \tag{D27}
\]

Hölder and (D26) make the right side L2, and in fact every fixed Lp.
One fully explicit bound for the square sum over `a` is

\[
 \sup_{s\le10,u}
 \left(\sum_a\|\cosh^2w_a(s)Q(s,u)\|_2^2\right)^{1/2}
 \le\sqrt2\{2^{5/4}e^8 K_{10}+40K_{10}^2\}.
 \tag{D28}
\]

Here `||N#||4<=2K10` and
`||cosh²G||4<=(2e^32)^(1/4)`. Restricting to `s=s(t)` makes this a
uniform-in-physical-time population bound. It is distinct from (D5)'s
compact-time finite statement and claims no all-time finite-width limit.

The same finite-list bounded-test passage with a root and clock tuple,
followed by (D25), identifies every fixed weighted source tuple with its
moments. No finite support assumption enters the source. Borel integration
against a fixed law and the rest of the derivative-capture proof are
separate downstream steps in `WEIGHTED_SOURCE.md` and `FINITE_CAPTURE.md`.

## 7. Relationship to the frozen source and check scope

The main source file zeros one initialized column, retains every neuron,
and compares both complete clock arrays. Its missing reverse answer
contributes a conditional Gaussian forcing divided by `sqrt(n)` in its
state comparison. This proof removes the first neuron from the comparison
and compares only the remaining clocks; its missing forward contribution
has a deterministic bound on the good event. The resulting actual-query
remainder (D20) is deterministic, at the price of changing the comparison
architecture to a rectangular cavity. The actual network and theorem
architecture are unchanged in both arguments.

I read the completed source file after deriving (D12)-(D23), and
reconstructed its S21-S28, conditioning event, feature-flow reduction and
bounded-test passage. No substantive objection was found in that source
argument. This is corroborating author work and does not satisfy the
workflow's fresh isolated scientific-review gate.

Read inputs: complete B.1 and C.4 including C.4.5 in
`docs/global_nonlinear.md`; A.1-A.4 there; complete III.F.1-10 in
`docs/special_data_limits.md`; finite dynamics §§1-4; the canonical notation
and research reading guide. The required mathematical skills and applicable
research-contract, evidence, adversarial-audit and proof-search references
were read. The input hashes at reconstruction were:

| Input | SHA-256 |
|---|---|
| global_nonlinear.md | `d473d95ee27bc39d484185cea2689b5d3ceed448567a1527488f1003e24f1fa1` |
| special_data_limits.md | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| finite_dynamics.md | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| WEIGHTED_SOURCE.md | `580c7556976c52727733263b2cfc199c16ff699d8ea64130111b7bba8fe45831` |

No Git operation or training run was performed by this author. This file is
the only write assignment used after coordination resolved the concurrent
arrival of the primary source file. The broader milestone still depends on
the propagator and derivative-capture arguments and the authorized reviews.
