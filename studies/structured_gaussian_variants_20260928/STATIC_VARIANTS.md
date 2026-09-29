# Static structured initialization: exact diagnostics and one candidate

This is a scoped, prompt-only theoretical design. Scientific inputs were the
assignment and `docs/notation.qmd`; no other study, external source, or experiment
was used. All statements below concern the initialization of the canonical deep
tanh network. The readout starts at zero, the usual feature-learning mobilities
remain in force, and **every matrix entry remains trainable**. No trained
block-to-dense universality theorem is assumed.

**Conclusion.** The strongest inexpensive static candidate identified here is a
bounded spectrum approximating the square Gaussian spectral law, surrounded by
two fast, randomly signed flat orthogonal mixers. It removes the persistent
block-size term in a fresh forward fourth-moment diagnostic and removes the
block-size term in a simple matrix/transpose reuse diagnostic. Both actions cost
`O(n log n)` and use `O(n)` fixed storage per hidden layer. This does **not** prove
that trained bias vanishes: nonlinear, adaptive reuse of the same mixer remains
the precise unresolved bridge. Strict independence of whole block trajectories
is lost.

## 1. What the baseline diagnostics say

Let `n=Bk`. In the baseline, `W` is block diagonal with independent Gaussian
`k` by `k` blocks, whose entries have variance `1/k`. Write

\[
 M_p(W)=\frac1n\operatorname{tr}((W^TW)^p).
\]

Two different mechanisms must be checked.

**Fresh forward action.** Let the input coordinates be iid, independent of `W`,
with mean zero, second moment `q`, and fourth moment `r_4`. Conditional on the
`k` input coordinates used by a row, its preactivation is Gaussian of variance
`k^{-1}\sum_jh_j^2`. Consequently

\[
 \mathbb E z_i^4=3q^2+\frac{3(r_4-q^2)}k.                 \tag{1}
\]

The dense `n` by `n` Gaussian matrix gives the same formula with `n` in place
of `k`. Thus increasing the number of independent blocks at fixed `k` averages
sampling noise but does not eliminate this forward-law difference. Formula (1)
is an exact diagnostic under its stated iid assumption, not a formula for every
hidden layer of the trained network.

**Matrix/transpose reuse.** For a Gaussian `d` by `d` matrix with variance `1/d`,
write its rows as `g_i`. Then

\[
 \mathbb E\|g_i\|_2^4=1+2/d,\qquad
 \mathbb E(g_i^Tg_j)^2=1/d\quad(i\ne j),
\]

and summing the diagonal and off-diagonal terms proves

\[
 \mathbb E M_2(W)=
 \begin{cases}2+1/n,&\text{dense Gaussian},\\
               2+1/k,&\text{Gaussian blocks}.
 \end{cases}                                             \tag{2}
\]

This is an actual reuse statistic: for independent `v~N(0,I_n)`,
`E_v ||W^T Wv||_2^2/n=M_2(W)`. It is not a proof that the network output has an
error proportional to `1/k`, nor is it a lower bound on trained bias.

Replacing the blocks by orthogonal blocks makes `M_2=1` exactly. It therefore
changes the leading reuse statistic by order one, even though the normalization
`M_1=1` is correct and fresh high-dimensional row projections may look Gaussian.
Uniform operator bounds alone are not the desired repair.

## 2. The most conservative block-only repair is incomplete

Take independent blocks `U_b S V_b^T`, with independent Haar orthogonal factors,
and prescribe the squared singular values so that

\[
 k^{-1}\operatorname{tr}S^2=1,\qquad
 k^{-1}\operatorname{tr}S^4=2.
\]

This makes `M_1=1` and `M_2=2` exactly; for example, half the squared singular
values equal to zero and half equal to two work when `k` is even. That particular
two-point spectrum has `M_3=4`, whereas the dense Gaussian limiting value is
`5`, so matching only `M_2` is deliberately insufficient. Explicitly, expanding
`tr((W^TW)^3)` into six entries and applying Gaussian pairings gives
`E M_3=5+6/d+4/d^2` for a `d` by `d` real Gaussian matrix of variance `1/d`:
among the fifteen pairings, five leave four free indices, six leave three,
and four leave two, before the overall normalization `d^{-4}`.

Even assuming the displayed first two spectral moments, a row `w` of one such
block satisfies

\[
 \mathbb E\|w\|_2^4=\frac{k+4}{k+2},\qquad
 \mathbb E\sum_jw_j^4=\frac{3(k+4)}{(k+2)^2}.
\]

For completeness, if `u` is a uniform unit vector, rotational symmetry gives
`E u_i^4=3 E u_i^2u_j^2`; expanding `(\sum_i u_i^2)^2=1` yields the values
`3/[k(k+2)]` and `1/[k(k+2)]`. Applying these identities first to the left
factor, then to the right factor, gives the displayed row formulas. Expanding
the fourth power of `w^Th` therefore gives

\[
 \mathbb E z_i^4-3q^2
 =\frac{3\{k(r_4-q^2)+4r_4-8q^2\}}{(k+2)^2}.             \tag{3}
\]

It does not generically vanish at fixed `k`. Bounded independent blocks also
have a direct finite-`k` support obstruction: if `||W_b||_{op}\le C` and the
preceding tanh coordinates have absolute value at most one, then
`|z_i|\le C\sqrt{k}`. A nondegenerate dense Gaussian initialization limit has
unbounded preactivation support. This obstructs exact full-law equality at
fixed `k`; it does not quantify prediction error.

Thus spectral adjustment is a defensible small block-only modification, but
neither orthogonalization nor spectral adjustment establishes fixed-`k` dense
universality. Its fixed-action work/storage remain `O(nk)`.

## 3. Recommended static candidate

For the cleanest construction let `n` be a power of two, and let `H` be a
normalized real Hadamard matrix: `H^TH=I` and `|H_ij|=n^{-1/2}`. Take independent
diagonal Rademacher sign matrices `D_\xi,D_\epsilon,D_\eta`, and an independent
permutation matrix `P`. Define

\[
 W=D_\xi H D_\epsilon S P H D_\eta,\qquad
 S=\operatorname{diag}(s_1,\ldots,s_n).                    \tag{4}
\]

Use independent randomness for different hidden layers. The first-layer
initialization and zero readout are unchanged. `P` is not needed in the moment
proofs below, but avoids needlessly fixing the correspondence between the two
Hadamard factors. Other widths require an explicit alternative fast transform;
the present statements are for this width subsequence.

Here is a deterministic spectrum with an exact normalization and a uniform
bound. Let `Q` be the quantile function of the probability density

\[
 \rho(\lambda)=\frac1{2\pi}
       \sqrt{\frac{4-\lambda}{\lambda}}\,
       \mathbf 1_{(0,4)}(\lambda),
 \qquad
 s_j^2=n\int_{(j-1)/n}^{j/n}Q(u)\,du.                    \tag{5}
\]

Its moments are
`C_p=(2p)!/[p!(p+1)!]`, by substituting `\lambda=4u` in the density integral
and evaluating the beta integral. In particular `C_1=1,C_2=2,C_3=5`.
These are the usual target square-Gaussian spectral moments; only the
explicitly derived first and second dense Gaussian moments in (2) are needed
for the proved reuse comparison in this note.

Cell averaging and monotonicity of `Q` give

\[
 \frac1n\sum_js_j^2=1,\quad 0\le s_j\le2,\quad
 \left|\frac1n\sum_js_j^{2p}-C_p\right|
      \le\frac{p4^p}{n}.                                 \tag{6}
\]

To verify the last bound, couple `Q(u)` to its average on the cell containing
`u`. On each cell the absolute deviation is at most that cell's oscillation;
the cell lengths are `1/n` and the sum of oscillations is at most `4`.
Thus the coupled expected absolute difference is at most `4/n`. The function
`x^p` is `p4^{p-1}`-Lipschitz on `[0,4]`. This proves (6), without a random
matrix universality input.

The exact finite invariants of (4) are

\[
 \|W\|_{op}\le2,\qquad
 (WW^T)_{ii}=(W^TW)_{jj}=1,\qquad
 M_p(W)=n^{-1}\sum_js_j^{2p}.                             \tag{7}
\]

The flat absolute entries of each outer orthogonal factor give the diagonal
identities. In particular `|M_2(W)-2|\le32/n`, so the persistent `1/k` term in
(2) is absent. A spectrum with `M_2=2` exactly is also possible, but matching
that one number is less useful than retaining the entire spectral target.

## 4. Forward diagnostic: the effective averaging size becomes n

Fix the spectrum. Averaging only over `D_\epsilon`, any entry of (4) is a sum
of independent signs with coefficient magnitudes `s_j/n`. Hence

\[
 \mathbb E_\epsilon W_{ij}^2=1/n,\qquad
 \mathbb E_\epsilon W_{ij}^4
       =3/n^2-2M_2(W)/n^3.                               \tag{8}
\]

The fourth-moment identity follows by expanding a Rademacher sum:
`E(\sum a_j\epsilon_j)^4=3(\sum a_j^2)^2-2\sum a_j^4`.
For iid fresh input coordinates with moments `q,r_4` as in Section 1,
the exact row norm identity in (7) now gives

\[
 \mathbb E z_i^4
 =3q^2+(r_4-3q^2)
            \left(\frac3n-\frac{2M_2(W)}{n^2}\right).     \tag{9}
\]

This proves removal of the fixed-`k` forward fourth-moment defect, rather than
merely asserting that a mixer should help. It does not say that the finite-`n`
fourth moment is identical to the dense Gaussian fourth moment.

There is also a multiinput, one-row statement for **arbitrary deterministic
bounded input vectors**, independent of the current matrix. Condition on `P`
and set

\[
 A=H^TP^TS^2PH,\quad A_{jj}=1,\qquad
 C_{ab}=\frac1n h_a^TD_\eta A D_\eta h_b.
\]

The conditional covariance of row `i` after averaging its `\epsilon` signs
is `C_{ab}`, independent of `i`; the left row sign has no effect. If
`||h_a||_\infty\le R_a`, then

\[
 \mathbb E_\eta C_{ab}=h_a^Th_b/n,\qquad
 \operatorname{Var}_\eta(C_{ab})
 \le \frac{2R_a^2R_b^2(M_2(W)-1)}n.                      \tag{10}
\]

Indeed, write the centered quadratic form as a sum over `j<l` with
coefficient `A_jl(h_ajh_bl+h_alh_bj)/n`. Distinct sign pairs are orthogonal
in `L^2`, and the sum of squared off-diagonal entries of `A` is
`n(M_2-1)`. This proves the variance bound.

To see the conditional central-limit mechanism without invoking a universality
theorem, write `v_a=PHD_\eta h_a`. Independent bounded signs give

\[
 \Pr\!\left(\max_{a,j}|v_{a,j}|>
   R\sqrt{2\log(2mn/\delta)}\right)\le\delta,
 \qquad R=\max_aR_a.
\]

For a fixed test vector `t\in\mathbb R^m`, one row's scalar projection is a
Rademacher sum with coefficients
`c_j=H_ij s_j\sum_a t_a v_a,j`. Their maximum absolute size tends to zero,
at most `2R||t||_1 sqrt(2 log(2mn/delta)/n)`, while
`\sum_jc_j^2=t^TCt\le4R^2||t||_1^2`. Expanding
`\sum_j\log\cos(c_j)=-\frac12\sum_jc_j^2+O(\sum_jc_j^4)` is valid for all
sufficiently large `n`; the remainder tends to zero since
`\sum c_j^4\le (\max c_j^2)\sum c_j^2`.
Together with (10), this proves convergence of the one-row characteristic
function to the centered Gaussian with covariance `h_a^Th_b/n`, along any
sequence where that Gram converges. Singular limiting input Grams are allowed.
The same conclusion applies conditionally to random bounded inputs independent
of this layer. Tanh's boundedness supplies the input bound at initialization.

This is a fresh forward, one-row result. It does not by itself prove
concentration of the empirical kernel over all rows, a full-depth NNGP limit,
or a trained limit. The shared signs make those additional assertions separate
questions.

## 5. Costs, learning, and the exact remaining gap

The Hadamard transforms in (4) and its transpose each cost `O(n log n)`; signs,
diagonal multiplication, and permutation cost `O(n)`. Fixed storage is `O(n)`
per layer. Thus applying the frozen operators to `O(Lmq)` response vectors has
cost `O(Lmnq log n)` and does not enlarge an existing `O(Lmnq)` moving response
state. This is only the cost of these actions; it is not a bound on every other
contraction in a response algorithm. Nor does it prove that a finite response
truncation is accurate.

The actual trained matrix is not constrained to retain (4). With residual
`r_a=f_a-y_a` and the notation-contract backward coordinate `\delta_a`, its
middle-layer equation remains

\[
 \dot W^{(\ell)}(t)=-\frac{2\kappa_\ell}{mn}
     \sum_{a=1}^m r_a(t)\,
      \delta_a^{(\ell)}(t)(h_a^{(\ell-1)}(t))^T.
\]

Every entry may therefore move. Equations (7) are invariants of the **frozen
initial operator**, not conservation laws for the trained matrix. Independent
initial signs do not imply independent block trajectories after global mixing
or after these globally trained updates.

The single decisive unresolved proposition is a trajectory-level replacement
bound for this initialization and dense Gaussian initialization, with the same
canonical mobilities, finite general multiinput data, zero initial readout,
and small fixed labels. For a fixed horizon `T`, it must control at least

\[
 \sup_{0\le t\le T}\max_a|f_a^{\rm mix}(t)-f_a^{\rm dense}(t)|
\]

in a stated coupling/probability mode, and the learned feature and backward
quantities needed to propagate this error. The replacement must handle
alternating `W_0`, `W_0^T`, and diagonal tanh-derivative factors evaluated on
states that already depend on `W_0`. The sign-independence used in (8)--(10)
then fails. Matching every un-gated singular-value moment still does not
identify contractions with these nonlinear, adapted diagonal factors.

The positive initial feature-Gram gap and small labels can be useful for
stability only after suitable initial-kernel concentration and an error-source
estimate are established. They do not themselves supply a matrix-replacement
estimate. The first necessary new bridge is therefore a **gated/adaptive reuse
comparison**, not another estimate of `||W_0||` or another forward-only
Gaussian approximation. Dense-population existence alone supplies none of it.

This bounded design study stops at that gap. It establishes two repaired
diagnostics and a concrete inexpensive candidate; it does not establish
vanishing trained block-to-dense bias, compact-time trained universality, or an
all-time guarantee.
