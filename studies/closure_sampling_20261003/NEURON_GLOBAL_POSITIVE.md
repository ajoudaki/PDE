# Response-aware neuron cubature: exact finite jets and the global gap

2026-10-03. Scoped positive-route continuation. This note proves an
initialization-derived finite response construction. It does **not** prove
the requested all-time neuron-compression theorem or an impossibility
theorem. No experiments, trained-path queries, manuscript edits, or Git
operations were used.

Scientific inputs are the current model and closure in `paper/main.tex`,
the initialization/fitting portion of `paper/proof_alltime.tex`, the
complete comparison argument in `paper/proof_tracking.tex`,
`paper/results.tex`, the study's `NEURON_REDUCTION_RESULT.md`,
`JOINT_SOURCE_SAMPLING.md`, `NEURON_CUBATURE_CONSTRUCTION.md`, and
`EMPIRICAL_PATH_QUADRATURE.md`. The explicitly authorized earlier study's
`FINITE_TAIL_ROUTE.md`, `CONTROLLED_FEEDBACK_STABILITY.md`, and
`GENERAL_DATA_STABILITY_ROUTE.md` were inspected for a usable global
continuation estimate; their additional hypotheses were not transferred.
The canonical-notation, rigorous-proof, and conjecture-investigation
instructions were applied.

The target remains the original realized width-$n$, order-$q$ closure,
with canonical Gaussian initialization, zero readout, two tanh hidden
layers, fixed compatible sphere data and sufficiently small fixed labels.
The requested error is

\[
 \left(\int\sup_{t\ge0}
 |\widetilde f_{N,q}(t,x)-\widehat f_{n,q}(t,x)|^2\,d\mu(x)\right)^{1/2}
 \le C_\delta n^{-1/2},
\]

with $N=o(n)$, preferably $Nq=o(n)$. The construction below preserves the
same $q$, the original physical time, both orientations of one compressed
mixer, the moment dynamics, and the model's own residual and clock. Its
guarantee concerns finite initial derivatives, not this displayed target.

## 1. Setup

Write $A=W^{(1)}\in\mathbb R^{n\times d}$,
$W=W^{(2)}\in\mathbb R^{n\times n}$, and $w\in\mathbb R^n$ for
the original closure's reconstructed physical parameters. Set
$v_a=x_a/\sqrt d$. Its forward pass is

\[
 h_a^{(1)}=\tanh(Av_a),\qquad z_a^{(2)}=Wh_a^{(1)},\qquad
 h_a^{(2)}=\tanh z_a^{(2)},\qquad f_a=w^\top h_a^{(2)}/n.
\]

The residual and loss are $r_a=f_a-y_a$ and
$\mathcal L=\rho^2=m^{-1}\sum_a r_a^2$. The backward fields are

\[
 \delta_a^{(2)}=w\odot\operatorname{sech}^2z_a^{(2)},\qquad
 \delta_a^{(1)}=\operatorname{sech}^2(Av_a)
                         \odot W^\top\delta_a^{(2)}.
\]

The first matrix and readout evolve by

\[
 \dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,
 \qquad \dot w=-\frac2m\sum_a r_a h_a^{(2)}.
\tag{1}
\]

The remaining state is $\tau$, with $\dot\tau=\rho$, $\tau(0)=1$,
and the $q$ forward and backward moments for each sample. Their source
terms are $\rho h_a^{(1)}$ and $r_a\delta_a^{(2)}$, respectively;
each moment $M_{a,j}$ has the additional dilation term

\[
 -\frac\rho\tau\left[jM_{a,j}
               +\sum_{k<j}(2k+1)M_{a,k}\right].
\]

Only $\bar h_{a,0}^{(1)}(0)=h_a^{(1)}(0)$ is initially nonzero,
and the mixer is reconstructed as

\[
 W=W_0-\frac2{mn\tau}\sum_{a,j<q}(2j+1)
                  \bar\delta_{a,j}^{(2)}\bar h_{a,j}^{(1)\top}.
\tag{2}
\]

For positive label RMS $Y$, $\rho(0)=Y>0$. At fixed finite $n,q$,
the raw state vector field is real analytic in a neighborhood of its
initial state: tanh has no real poles, $\tau(0)>0$, and the square root
defining $\rho$ has positive argument. Thus every finite time derivative
at zero is defined and computable by repeatedly differentiating these
finite formulas at initialization. This operation does not integrate the
trained trajectory. When $Y=0$, all dynamics are stationary and the
following construction is unnecessary.

For integer $p\ge0$, use $h_{a,k}^{(\ell)}$ and
$\delta_{a,k}^{(2)}$ to denote the actual derivatives
$\partial_t^kh_a^{(\ell)}(0)$ and
$\partial_t^k\delta_a^{(2)}(0)$, for $0\le k\le p$.
These are fixed vectors used during setup, not additional moving states.

## 2. Finite-jet cubature theorem

**Proposition.** For every finite initialized network, label vector with
$Y>0$, order $q\ge1$, and integer $p\ge0$, there is an explicit positive
weighted two-population closure whose first weights are selected original
rows, whose readout is initially zero, and whose fixed mixer $B_0$ obeys

\[
 \|B_0\|_{D_1\to D_2}\le\|W_0\|_{\rm op},\qquad
 B_0^*=D_1^{-1}B_0^\top D_2.
\tag{3}
\]

Here $D_1,D_2$ are diagonal matrices of strictly positive population
weights, each summing to one. The numbers $N_1,N_2$ of retained neurons
satisfy

\[
 \begin{aligned}
 r&\le d+2m(p+1),&N_1&\le1+r(r+1)/2,\\
 s&\le3m(p+1),&N_2&\le1+s(s+1)/2.
 \end{aligned}
\tag{4}
\]

Every training prediction derivative through order $p$ is exactly
preserved. At retained neurons, the first-matrix, readout, all moment,
forward-feature and backward-field derivatives through the same order
also agree with their original counterparts. The clocks have the same
derivatives through this order. These statements apply to the specified
original order $q$; there is no dense-flow substitution.

The initial training feature Gram and first-matrix RMS are preserved
exactly. If the initialized operator and first-layer RMS obey fixed
deterministic bounds, the initial training feature Gram has a fixed
positive gap, and the labels are sufficiently small depending on these
bounds, the weighted fitting argument applies independently of
$p,N_1,N_2,q$. Under these additional hypotheses the reduced model fits;
finite-jet matching alone does not prove fitting or trajectory fidelity.

### Construction

Choose the lower and upper source spaces

\[
 \begin{aligned}
 S_1={}&\operatorname{span}\left\{
 (A_0)_{:,b},\ h_{a,k}^{(1)},\ W_0^\top\delta_{a,k}^{(2)}:
 b\le d,\ a\le m,\ 0\le k\le p\right\},\\
 S_2={}&\operatorname{span}\left\{
 h_{a,k}^{(2)},\ \delta_{a,k}^{(2)},\ W_0h_{a,k}^{(1)}:
 a\le m,\ 0\le k\le p\right\}.
 \end{aligned}
\tag{5}
\]

Let $V\in\mathbb R^{n\times r}$ and
$U\in\mathbb R^{n\times s}$ be empirical orthonormal bases:
$V^\top V/n=I_r$ and $U^\top U/n=I_s$. If a space is zero,
the corresponding empty matrices are interpreted in the usual way.
The dimensions satisfy (4).

Select positive lower and upper cubature rules matching mass and all
symmetric basis products. With retained index sets $I,J$, this means

\[
 V_I^\top D_1V_I=I_r,\qquad U_J^\top D_2U_J=I_s.
\tag{6}
\]

The elementary finite convex-combination elimination argument gives
the support bounds in (4): represent the empirical mean of the
$r(r+1)/2$ symmetric products by at most one more than that many rows,
and do the same upstairs. Starting from uniform weights, eliminate one
positive weight at a time along an affine dependence until this count
is reached. No negative weights or future data enter the construction.

Define

\[
 B=U^\top W_0V/n,\qquad
 B_0=U_JBV_I^\top D_1,\qquad
 B_0^*=V_IB^\top U_J^\top D_2.
\tag{7}
\]

Equation (6) makes $V_I$ and $U_J$ isometries for the weighted norms,
so (3) follows from $\|B\|_{\rm op}\le\|W_0\|_{\rm op}$.
For every derivative appearing in (5), the following two identities
hold exactly:

\[
 \begin{aligned}
 B_0(h_{a,k}^{(1)})_I&=(W_0h_{a,k}^{(1)})_J,\\
 B_0^*(\delta_{a,k}^{(2)})_J
              &=(W_0^\top\delta_{a,k}^{(2)})_I.
 \end{aligned}
\tag{8}
\]

For example, $B_0$ represents $P_{S_2}W_0P_{S_1}$; both the input
$h_{a,k}^{(1)}$ and its image $W_0h_{a,k}^{(1)}$ are in the
chosen spaces. The same argument applies to the transpose. These
relations hold on the stated derivative vectors. Invariance on the
whole source spaces is neither required nor asserted.

Initialize the reduced first matrix as $(A_0)_I$, readout as zero,
and forward-prefix moments from its own first features. Use the
weighted predictor $w_C^\top D_2h_C^{(2)}$, the same raw moment rules,
and reconstruction

\[
 W_C=B_0-\frac2{m\tau_C}\sum_{a,j<q}(2j+1)
      \bar\delta_{C,a,j}^{(2)}\bar h_{C,a,j}^{(1)\top}D_1.
\tag{9}
\]

Every backward pass uses its exact weighted adjoint. This is a finite,
autonomous and restartable system. After setup it stores only these
reduced arrays; $V,U$ and the original derivative arrays can be discarded.

### Proof of derivative matching

We give the induction because moment contraction is the part that
separate forward sampling misses. Every original forward-moment
derivative of order at most $k$ is a linear combination of
$h_{a,j}^{(1)}$, $j\le k$, and every backward-moment derivative is
a linear combination of $\delta_{a,j}^{(2)}$, $j\le k$.
This follows by differentiating the source and dilation equations:
all other factors are scalar derivatives of $r,\rho,\tau^{-1}$.
Likewise, differentiating (1) shows that each readout derivative of
positive order $k$ is a linear combination of
$h_{a,j}^{(2)}$ with $j<k$; its zeroth derivative is zero.

At order zero, the first features are restrictions of the originals.
The first identity in (8) then gives the original selected upper
preactivations, hence the selected upper features. Predictions, backward
fields, and backward moments vanish in both models. Forward prefixes
and clocks agree. Equation (6), since each $h_{a,0}^{(2)}\in S_2$,
also proves exact equality of the initial training Grams.

Suppose the raw-state derivatives through order $k\le p$ agree at
the retained coordinates. Composition with tanh commutes with coordinate
restriction, so the first-feature derivatives agree. Differentiate
(2) applied to a first feature. The $W_0$ term agrees by (8).
Every other term is a scalar derivative of $1/\tau$ multiplying a
backward-moment derivative and an inner product of a forward-moment
derivative with a first-feature derivative. All vectors in that inner
product lie in $S_1$, where (6) preserves it exactly. Thus the upper
preactivation and feature derivatives agree.

All readout derivatives used at this stage lie in $S_2$, as shown
above. Their pairings with upper-feature derivatives are therefore
preserved by (6). Prediction and residual derivatives agree, and so do
$\rho$ derivatives, since $\rho(0)>0$. The upper backward field is
a coordinatewise readout/gate product, so its derivatives agree.

For the lower backward field, expand the transpose of (2).
The $W_0^\top$ term agrees by the second identity in (8).
Each learned term contracts two upper vectors in $S_2$, so (6)
preserves it. The lower gate is already identical at each retained
coordinate. Hence lower backward derivatives agree. The raw update
equations now give matching first-weight, readout, clock and moment
derivatives of the next order. This closes the induction through the
claimed order. None of these contractions introduces a factor of $q$
into the number of required source vectors.

Finally, including the columns of $A_0$ in $S_1$ makes
$A_{0,I}^\top D_1A_{0,I}=A_0^\top A_0/n$ by (6). This and the
exact initial feature Gram give the stated fitting inputs. The weighted
bootstrap uses bounded tanh, the weighted operator norm and rank-one
norm identities, so it introduces no inverse smallest-weight factor.

### Passive probes and cost

For $K$ fixed passive query inputs, augment $S_1$ by their first-feature
derivatives and $S_2$ by their upper-feature derivatives and forward
images, all through order $p$. The same argument gives exact query
prediction derivatives through $p$, with

\[
 r\le d+(2m+K)(p+1),\qquad
 s\le(3m+2K)(p+1).
\tag{10}
\]

The construction does not add these queries to the loss. A continuum
of passive queries still requires a uniform approximation of their
derivative functions. Initial whole-query cubature is available in
`JOINT_SOURCE_SAMPLING.md`; it is not an all-order bound on these new
derivative functions.

For fixed $d,m,K$, the number of retained neurons is $O(p^2)$ and
the moving count is $O(p^2q)$. Fixed coefficients can be stored as
the $N_2\times N_1$ matrix in (7), or its factored form. Original
width-dependent arrays are used during setup only. There is no claim
of an efficient or well-conditioned setup procedure. In particular,
large derivative coefficients and small cubature weights are not
silently declared harmless for a later error estimate.

If a subsequent global argument allowed $p=n^{\gamma+o(1)}$,
then $Nq=n^{2\gamma+1/6+o(1)}$ at the separately certified history
scale, strictly below $n$ when $\gamma<5/12$. This is resource
arithmetic, not a proved choice of $p$ for fidelity.

## 3. Why Gaussian response analyticity is insufficient

The preceding theorem removes an algebraic obstacle: finite response
depth does not itself require exponentially many independent vectors
when the label vector and physical trajectory are fixed. It leaves
the approximation remainder. A tempting argument is that small total
activity and analytic tanh imply a width-independent analytic response
expansion. The following elementary test disproves that implication.

**Lemma.** Let $G,\Xi$ be independent standard Gaussians, let
$\sigma>0$, $c\in\mathbb R$, and put

\[
 H=\operatorname{sech}^2(G)
                  [c\tanh G+\sigma\Xi],\qquad
 F(s)=\tanh(G+sH)\in L^2(G,\Xi),\quad s\in\mathbb R.
\tag{11}
\]

The map $F$ is infinitely differentiable in $L^2$ on the real axis,
but its Taylor series at zero has radius of convergence zero in $L^2$.

**Proof.** For each fixed derivative order, every real derivative of
tanh is bounded. Also $H$ has every finite moment, since its absolute
value is bounded by $|c|+\sigma|\Xi|$. Difference quotients and the
fundamental theorem of calculus are dominated in $L^2$ by a constant
times $|H|^k$ for the $k$th derivative. Thus

\[
 F^{(k)}(0)=H^k\tanh^{(k)}G
\tag{12}
\]

in $L^2$ for every $k$.

Suppose its coefficient sequence $a_k=F^{(k)}(0)/k!$ had a positive
$L^2$ convergence radius $R$. Choose $0<r<R$. The root criterion
then gives $\sum_k\|a_k\|_{L^2}r^k<\infty$, after choosing an
intermediate radius if needed. Tonelli and
$\|a_k\|_{L^1}\le\|a_k\|_{L^2}$ imply

\[
 \sum_k |a_k(G,\Xi)|r^k<\infty
\]

almost surely. Hence the scalar Taylor series converges throughout
$|s|<r$ for almost every pair $(G,\Xi)$.

For a fixed real pair with $H\ne0$, however, the nearest poles of
$s\mapsto\tanh(G+sH)$ occur at
$s=(-G\pm i\pi/2)/H$. Its Taylor radius is exactly

\[
 R(G,\Xi)=\frac{\sqrt{G^2+\pi^2/4}}{|H|}.
\tag{13}
\]

Conditional on any finite $G$, $H$ is a Gaussian with nonzero variance.
Thus $\Pr\{R(G,\Xi)<r\}>0$ for every $r>0$, contradicting
the almost-sure scalar convergence. This proves the lemma.

The random field in (11) is chosen to have the form of the first
gate-weighted reverse response obtained from the exact conditional
Gaussian calculation in `JOINT_SOURCE_SAMPLING.md`. The lemma concerns
an affine displacement along that response, not the complete trained
trajectory. It invalidates the inference from activation analyticity and
Gaussian response tails to a common Hilbert-space Taylor radius. It does
not prove that the actual neural trajectory has no useful asymptotic or
non-Taylor approximation.

The simpler field $\tanh(G+s\Xi)$ already has this property. In a
finite empirical population its Taylor radius is positive, but not
uniform in width. Among $n$ independent pairs, with probability tending
to one there is a pair with $|G_i|\le1$ and
$|\Xi_i|\ge\sqrt{\log n}$: the probability of this event for one
pair is bounded below by $c n^{-1/2}/\sqrt{\log n}$, so the
probability that it occurs nowhere is at most
$\exp\{-c\sqrt n/\sqrt{\log n}\}$. Equation (13), with
$H=\Xi$, then gives empirical radius at most
$C/\sqrt{\log n}$. This last independent-pair estimate is a
diagnostic benchmark, not a claim about independence of trained neurons.

## 4. Exact global estimate still missing

For a retained passive probe, let
$e_p(t,x)=f_C(t,x)-\widehat f_{n,q}(t,x)$. The theorem gives
$\partial_t^ke_p(0,x)=0$ for $0\le k\le p$. At fixed finite
$n,q$, Taylor's integral remainder is the exact implication

\[
 \sup_{0\le t\le T}|e_p(t,x)|
 \le\frac{T^{p+1}}{(p+1)!}
       \sup_{0\le t\le T}|\partial_t^{p+1}e_p(t,x)|.
\tag{14}
\]

The two models' exponential fitting bounds make their prediction
variation after $T$ at most $Ce^{-\kappa T}$ on a bounded query
domain. Therefore $T\asymp\log n$ suffices for the *tail*, but
does not bound the derivative on the right of (14). A sufficient
continuation proof would have to establish, for some
$p=n^{\gamma+o(1)}$ with $\gamma<5/12$, a bound such as

\[
 \left(\int\sup_{0\le t\le T}
  |\partial_t^{p+1}e_p(t,x)|^2\,d\mu(x)\right)^{1/2}
 \le C_\delta n^{-1/2}(p+1)!T^{-(p+1)},
\tag{15}
\]

or a sharper continuation estimate that uses the vanishing initial jets
without requiring (15). For the continuum query norm, the source
construction must also control the initial derivative discrepancies on
that continuum. Neither estimate is proved here.

Even a narrow uniform complex-time strip would not settle this
automatically. For positive strip half-width $r$, the bounded analytic
function

\[
 g_p(t)=\tanh\left(\frac{\pi t}{4r}\right)^{p+1}
\tag{16}
\]

has all derivatives through $p$ equal to zero at zero and modulus at
most one on $|\operatorname{Im}t|<r$. Its value at $T\gg r$ is

\[
 g_p(T)=\exp\left\{-2(p+1)e^{-\pi T/(2r)}
                 [1+O(e^{-\pi T/(2r)})]\right\}.
\tag{17}
\]

Thus analyticity and a strip bound alone permit a discrepancy near one
unless $p$ is exponentially large in $T/r$. This is a counterexample
to an analytic-continuation inference, not a neural prediction-error
lower bound. Small activity might permit a more favorable variable or
a widening analytic domain, but such a domain must be established for
both autonomous systems, including their residual-RMS clocks and the
weighted reduced mixer.

## 5. Current conclusion

The finite-jet construction is an unconditional, exact response-aware
extension of initial cubature. It matches both reused matrix directions,
all retained moment derivatives and finite-probe prediction derivatives,
using $O(p^2)$ neurons and $O(p^2q)$ moving state. It does not rely on
an assumed source-decay theorem.

The decisive missing inequality is a quantitative whole-trajectory
remainder after this initial response matching, of the strength in
(15) or a rigorously stronger substitute. The Gaussian analytic-radius
lemma shows why bounded real tanh derivatives and small fixed activity
do not supply a geometric Taylor tail. The finite-jet result does not
establish $N=o(n)$ at root-width all-time error; the diagnostic lemma
does not rule out that target. No conclusion from this note supersedes
the existing open status of the all-time neuron-reduction question.

## 6. Bounded follow-up: history regularity and Gaussian source amplitudes

This section was added after the finite-jet result was first frozen at
SHA-256 `d88b15074d4b06bc268731e32299e5e46d7d3eeb9d32d51e662d465efa84ab11`.
Subsequently, the proposition's fitting sentence was clarified to state
explicitly its additional positive-Gram, deterministic-bound and
small-label hypotheses, and the dilation sentence was clarified to say
"each moment". The finite-jet construction and proof are unchanged.
The revised preceding version has SHA-256
`8e228c6a9c838af33831e3a6776792a8ff31334435f87bdb930c49e7e644f5c2`.
Additional authorized inputs are `HISTORY_APPROXIMATION_ROUTE.md` and
`HISTORY_APPROXIMATION_CHECK.md`. The question is whether their successful
second-order temporal estimate already supplies summably decaying Gaussian
source coordinates for neuron cubature. It supplies a real pathwise
anisotropy bound, but not that source representation.

Fix one training sample and a finite current clock endpoint $A=\tau(t)$.
Let $h(\xi)\in\mathbb R^n$ be its actual first-layer history, including
the initial prefix. Define

\[
 e_j^A(\xi)=\sqrt{(2j+1)/A}\,p_j(\xi/A),\qquad
 a_j=\int_0^A h(\xi)e_j^A(\xi)\,d\xi,
 \qquad b_j=\frac{\|a_j\|_2}{\sqrt n}.
\tag{18}
\]

Here $a_j$ are vector coefficients, and $b_j$ are their nonnegative
amplitudes; neither is a Gaussian innovation. Put
$\mathcal L_Ah=-[\xi(A-\xi)h']'$ and
$B_A=\|\mathcal L_Ah\|_{L^2(0,A)}/\sqrt n$. The checked history
result proves the domain conditions and the bound
$B_A\le CY^{3/2}(1+YK_q)$, with its actual carrier maximum $K_q$.
Its later comparison/absorption argument controls $K_q$ in the specified
order-width region; this factor is retained here rather than declared
uniform for every order.

The same integration by parts used there gives the stronger coefficient
statement

\[
 \sum_{j\ge1}[j(j+1)]^2b_j^2\le B_A^2,
 \qquad
 \sum_{j\ge J}b_j^2\le\frac{B_A^2}{J^2(J+1)^2}.
\tag{19}
\]

Consequently $b_j\le B_A/[j(j+1)]$. In fact, for every
$2/5<p<2$, Holder's inequality gives

\[
 \sum_{j\ge1}b_j^p
 \le B_A^p
 \left(\sum_{j\ge1}
 [j(j+1)]^{-2p/(2-p)}\right)^{(2-p)/2}<\infty.
\tag{20}
\]

The series converges exactly when $4p/(2-p)>1$, which explains
$p>2/5$. The bound is a width-independent function of $B_A,p$.
For $p\ge2$, summability follows directly from (19). Because $W_0$
is fixed in clock time, the coefficient of the **actual reused action**
$W_0h$ is $W_0a_j$. On $\|W_0\|_{\rm op}\le K$,

\[
 \sum_{j\ge1}[j(j+1)]^2
       \frac{\|W_0a_j\|_2^2}{n}\le K^2B_A^2.
\tag{21}
\]

This estimate holds even though the entire history depends on $W_0$.
It is a legitimate positive consequence of the history theorem and
requires no independence claim.

There is also a geometric interpretation. The map
$Tg=n^{-1/2}\int_0^A h(\xi)g(\xi)d\xi$ from $L^2(0,A)$ to
$\mathbb R^n$ has a rank-at-most-$J$ approximation obtained by keeping
the first $J$ coefficients. Its squared Hilbert--Schmidt error is at
most $B_A^2/[J^2(J+1)^2]$. If $s_k$ are the singular values of
$T$ in decreasing order, the least squared error of a rank-$J$
approximation is $\sum_{k>J}s_k^2$: diagonalize $TT^\top$ and
retain its largest $J$ eigenvalues. Therefore
$J s_{2J}^2\le\sum_{k>J}s_k^2\le CB_A^2J^{-4}$, so
$s_{2J}\le CB_AJ^{-5/2}$. The history has a rapidly approximable
empirical spatial span. Producing that span from the future history
would violate the construction's provenance requirement, so this is
not a neuron-selection algorithm.

The exact Gaussian step is different. Suppose a finite legitimate
matrix-query transcript has already revealed forward actions $W_0H$
and reverse actions $W_0^\top D$, where each new query vector was
measurable with respect to the earlier transcript. Let $P_H,P_D$
be the orthogonal projections onto their respective column spaces,
and condition also on the independent first-layer initialization.
Successive finite Gaussian conditioning gives

\[
 W_0=M+(I-P_D)\frac{G}{\sqrt n}(I-P_H)
\tag{22}
\]

in conditional law. Here $M$ is the conditional mean satisfying the
revealed constraints, and $G$ is a conditionally fresh standard Gaussian
matrix. To see the covariance, the matrices satisfying the homogeneous
constraints are precisely $(I-P_D)X(I-P_H)$; this is the orthogonal
projection in Frobenius geometry of the isotropic Gaussian matrix onto
that linear space. Predictable adaptive choices add no constraint beyond
the revealed linear answers, so this argument applies successively.

For two next query vectors $v,w$ measurable with respect to this
transcript, (22) proves the exact cross-covariance

\[
 \operatorname{Cov}(W_0v,W_0w\mid\text{transcript})
 =\frac{v^\top(I-P_H)w}{n}(I-P_D).
\tag{23}
\]

Thus a predictable query with amplitude $\|v\|_2/\sqrt n\le b_j$
would have new Gaussian variance at most $b_j^2$. The histories in
(18) do not supply such a sequence: $a_j$ uses the entire evolved
trajectory through the endpoint, including actions of both matrix
orientations that have not been revealed when that source is first
needed. Conditioning on $a_j$ as though it were an exogenous query
changes the remaining matrix law. Conditioning on the complete
initialization instead leaves no Gaussian randomness. Equation (19)
does not resolve this distinction.

An actual initial neural response demonstrates the problem already
before a temporal expansion. Take one input, $y>0$, $n\ge2$, and set

\[
 a=A_0v,\quad h=\tanh a,\quad z=W_0h,\quad
 u=2y\tanh z\odot\operatorname{sech}^2z,\quad
 k=W_0^\top u,\quad D_0=\operatorname{diag}(\operatorname{sech}^4a).
\]

The exact first-feature acceleration for every order is
$v_2=\ddot h^{(1)}(0)=2yD_0k$. Conditional on $A_0,z$, the
vector $u$ is known, but $k$ has a nondegenerate Gaussian component
on $h^\perp$. Accordingly,

\[
 u^\top W_0v_2=2y\,k^\top D_0k
\tag{24}
\]

is nonnegative and nonconstant under that conditioning, almost surely.
It cannot be a Gaussian scalar. In particular the endogenous forward
action $W_0v_2$ cannot be replaced by a conditionally Gaussian action
using only its source covariance. After revealing $k$ as an additional
reverse query, $v_2$ becomes predictable and the correct new covariance is

\[
 \operatorname{Cov}(W_0v_2\mid A_0,z,k)
 =\frac{\|(I-P_h)v_2\|_2^2}{n}(I-P_u),
\tag{25}
\]

with a nonzero conditional mean retained. This is precisely the two-sided
conditioning mechanism, now applied to a coefficient of a temporally
smooth actual history. Temporal smoothness does not eliminate it.

The bounded check therefore has a definite outcome. Equations (19)--(21)
give decaying amplitudes for actual empirical temporal coefficient
vectors and their forward images. They do **not** yet give a predictable
Gaussian coordinate system with those amplitudes, bounds on the
conditional-mean response terms in (22), or summable sensitivity of the
autonomous predictor to perturbing its source coordinates. Smoothness in
clock time concerns a different derivative from differentiation with
respect to the reused Gaussian environment. A source-cubature proof
would have to establish that additional correspondence, while retaining
the reverse action. No new conditional global theorem, impossibility
claim, or decay rate for that sensitivity is asserted here.
