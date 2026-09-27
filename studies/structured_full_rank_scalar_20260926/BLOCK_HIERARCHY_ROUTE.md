# Gaussian block hierarchy: exact reduction and remaining identification gap

This is a prompt-only scoped theoretical analysis. No repository scientific sources or other route drafts were read. The supervisor supplied the canonical equations, and clarified the initial conditions as `L(0)=1`, `A_j(0)=0`, `B_0(0)=h_1(0)`, and `B_j(0)=0` for `j>0`. No experiments were performed. This note applies the rigorous-math and investigate-conjectures skills.

## Conclusion

Independent Gaussian blocks give an exact nonlinear particle representation of the finite-`P` closure. A finite sample of blocks gives an autonomous, restartable scalar ODE whose state and stored coefficients are independent of target width `n`. It retains the full nonlinear first-layer motion, second-layer features, readout motion, and dense cross-block learned correction.

Two required quantitative bridges remain open: polynomial dependence on block size in the particle approximation, and identification of the large-block limit with the dense Gaussian population dynamics. Neither follows from full rank, bounded spectral norms, or a central limit theorem at initialization. This is a substantive possible hierarchy, but its presently proved portion does not establish the user's full target.

## 1. Exact block equations

Write `n=bk`, let `G_β` be independent `k×k` matrices with entries `N(0,1/k)`, and set

\[
W_0=\operatorname{diag}(G_1,\ldots,G_b).
\]

Every block, hence `W_0`, is invertible almost surely: its determinant is a nonzero polynomial in continuously distributed entries. Initial storage is `O(nk)`, rather than `O(n²)`. At fixed `k`, this is still linear in `n`; the population particle approximation below is what removes `n` from the scalar simulator.

Block `β` has dynamic state

\[
X_\beta=(w_\beta,c_\beta,(A_{\beta j},B_{\beta j})_{j<P}),
\qquad
D_k=k(d+1+2mP).
\]

The frozen block `G_β` needs `k²` scalar coefficients. For any training or passive test input `u`, define

\[
s_j(u)=\frac1b\sum_{\beta=1}^b\frac1kB_{\beta j}^{\mathsf T}h_{1\beta}(u),
\quad
v_j(u)=\frac1b\sum_{\beta=1}^b\frac1kA_{\beta j}^{\mathsf T}\delta_{2\beta}(u).
\]

These are vectors in `R^m`. With `a_j=2j+1`, the exact forward and backward equations are

\[
\begin{aligned}
h_{1\beta}(u)&=\tanh(w_\beta u),\\
z_{2\beta}(u)&=G_\beta h_{1\beta}(u)
-\frac2{mL}\sum_{j<P}a_jA_{\beta j}s_j(u),\\
h_{2\beta}(u)&=\tanh z_{2\beta}(u),\\
f(u)&=\frac1b\sum_\beta\frac1k c_\beta^{\mathsf T}h_{2\beta}(u),\\
\delta_{2\beta}(u)&=c_\beta\odot(1-h_{2\beta}(u)^2),\\
\delta_{1\beta}(u)&=(1-h_{1\beta}(u)^2)\odot
\left[G_\beta^{\mathsf T}\delta_{2\beta}(u)
-\frac2{mL}\sum_{j<P}a_jB_{\beta j}v_j(u)\right].
\end{aligned}
\]

Insert these into the supplied `w,c,A,B,L` equations without further approximation. For example,

\[
\dot w_\beta=-\frac2m\sum_{a=1}^m
r_a\delta_{1\beta}(u_a)u_a^{\mathsf T},
\qquad
\dot c_\beta=-\frac2m\sum_a r_a h_{2\beta}(u_a).
\]

The training coupling uses at most `m+2Pm²` scalar fields: outputs, the `s` overlaps, and the `v` overlaps. They are computed in a causal algebraic order: `s` from `(w,B)`, then second-layer features and outputs, then `v`. There is no implicit algebraic fixed point at a single time.

The learned term contains blocks `A_{βj} B_{γj}^T` for every pair `(β,γ)`. Thus the learned matrix is generally dense across blocks. The finite-`P` rank restriction already present in the specified closure is retained; no additional fixed learned subspace or lazy-feature approximation is imposed.

Input correlations are retained exactly through the same vector `(tanh(wu_a))_{a≤m}` in each block. No orthogonality or independent-input assumption is used.

## 2. Population law and scalar simulator

For fixed `k`, replace the empirical block average by an expectation under a law `μ_t^{(k)}` of nonlinear blocks. Its particles evolve by the same finite-dimensional equations, driven by fields evaluated under this law. This is a McKean–Vlasov description with quenched matrix `G`.

The canonical initialization has `c_i(0)~N(0,1/n²)`. Therefore its fixed-`k`, `b→∞` population law has exactly `c(0)=0`. A `q`-block approximation to this law should also initialize `c=0`. Initializing it at variance `1/(qk)²` instead introduces a separate small-readout-initialization approximation.

Replace each law expectation by the average of `q` sampled blocks. The simulator is autonomous and restartable with

\[
N_{\rm dynamic}=1+qk(d+1+2mP),
\qquad N_{\rm static}=qk^2.
\]

The shared `L` accounts for the extra dynamic coordinate. A direct right-hand-side evaluation costs `O(qk²m)` plus lower-order memory operations when `m,d,P` are fixed. Test inputs require evaluation of their own `s_j(u)` and forward features from the current finite state; they do not require adding training dynamics.

This construction is a genuine finite ODE after sampling. The exact population law itself is infinite dimensional and must not be called a finite scalar closure.

## 3. A defensible fixed-block theorem with a spectral cutoff

Consider any initialization law supported on `||G||op≤R`, retain Gaussian first-layer weights, set `c(0)=0`, and use the supplied bounded memory initialization and `L(0)=1`. Fix bounded training inputs and labels and a finite horizon `T`.

**Theorem candidate, with an elementary proof route.** The block population equation is well posed, and its interacting `q`-block approximation satisfies, for training outputs and any fixed finite collection of bounded passive inputs,

\[
\mathbb E\sup_{t\le T}|f_{k,q}(t,u)-f_k(t,u)|
\le \frac{C(k,T,R,m,d,P,U,Y)}{\sqrt q}.
\]

The constant is independent of ambient width `n`; it is not presently proved polynomial in `k`. The same statement applies to the coupling fields. A uniform-circle version can be obtained by a covering argument, using the bounded-input output Lipschitz estimate and finite first-layer Gaussian moments; this adds accuracy-dependent covering factors and does not remove the `k`-stability issue.

Here is the proof structure and the particular obstruction in its constants.

1. With zero initial readout, `C(t)=max_i|c_i(t)|` obeys the comparison inequality `D⁺C≤2(C+Y)`, since `|f_a|≤C` and `|tanh|≤1`. Thus `c`, residuals, and `L` have bounds depending on `T,Y` but not on `k,q`. The triangular linear memory equations then bound every coordinate of `A_j,B_j` independently of `k,q`. Also `L≥1`.
2. Use the normalized block norm `k^{-1/2}` times the Euclidean/Frobenius norms of `w,c,A,B`. Gaussian initial `w` need not be bounded: tanh and its derivatives are globally bounded, and normalized Gaussian moments are uniform in `k` at fixed `d`.
3. On the bounded reachable `c,A,B,L` region, the vector field is globally Lipschitz in these normalized block variables, with a valid conservative bound

   \[
   K_{k,R,T}\le C_T(1+R^2+R\sqrt k).
   \]

   The `R√k` term is real in this norm estimate. In the first-layer equation the difference of `φ'(wu)` multiplies `G^Tδ_2`. Controlling this multiplication operator requires `||G^Tδ_2||∞`; spectral control alone gives only `R√k||δ_2||∞`. Thus one cannot infer dimension-free stability merely by normalizing Euclidean norms.
4. Couple each interacting block to an iid population block with the same initialization. The finite list of bounded moment fields of the independent population blocks has sampling error `O(q^{-1/2})`. Uniformity in time follows, for example, by bounding the expectation of the initial empirical error plus the time integral of the derivative empirical error. The necessary scalar moment derivatives have finite bounds for fixed `k,R,T`.
5. The Lipschitz comparison and Gronwall inequality yield the displayed result. This proof supplies a constant of the rough form `poly(k,R) exp[C_T(1+R²+R√k)]`, not a polynomial bound in `k`.

Consequently, fixed-`k` Monte Carlo is polynomial in `ε^{-1}`, but a joint bound polynomial in `k,ε^{-1}` remains unproved. The failure of this estimate to be polynomial is a proof obstruction, not a lower bound against the hierarchy.

One sufficient additional hypothesis would bound all reachable first-layer backpropagation coordinates by `O(log k)` while keeping the other bounds polynomial. This makes the deterministic Gronwall factor polynomial in `k`. Stronger probabilistic estimates, such as uniform sub-Gaussian tails for the learned backpropagation fields, could also suffice. Such estimates must be proved along the nonlinear training trajectory; they do not follow from Gaussian initialization, because `G` and `δ_2` become dependent.

## 4. Gaussian blocks, truncation, and what a cutoff does not prove

Conditioning Gaussian blocks on `||G||op≤R`, or scaling blocks down when their norm exceeds `R`, gives full-rank bounded-spectrum blocks almost surely. Conditioning and scaling are different initialization laws and should be recorded as such. Neither may silently replace the Gaussian-block target.

A useful elementary tail bound follows from a finite net. A `1/4` net of the unit sphere has at most `9^k` points. If `||G||op>R`, some net pair satisfies `|v^TGu|>R/2`; for fixed unit `u,v`, this scalar is `N(0,1/k)`. A union bound gives

\[
p_{k,R}:=\Pr(\|G\|_{\rm op}>R)
\le 2\exp\left[2k\log 9-\frac{kR^2}{8}\right].
\]

This loose bound is sufficient: for a fixed sufficiently large `R`, the discarded probability is exponentially small in `k`.

The bad blocks' outputs and overlap fields remain bounded because `c,A,B,h_1,h_2` have coordinate bounds independent of `G`. Compare the original Gaussian population law with the conditioned law by coupling their good blocks. Bad blocks contribute only their probability mass to the global fields; the good blocks propagate this perturbation with the finite-`k` stability constant. This gives a bound of the schematic, justifiable form

\[
\sup_{t\le T}|f_k^{\rm Gaussian}-f_k^{\rm conditioned}|
\le C_T\exp\{C_T(1+R^2+R\sqrt k)\}\,p_{k,R}.
\]

At fixed sufficiently large `R`, this bound tends to zero as `k→∞`, since `-ck` dominates `C√k`. This is a useful asymptotic cutoff removal. It does **not** make the sampling cost polynomial in `k`: the good-block stability constant can still be `exp(C√k)`.

For fixed small `k`, taking `R→∞` in this particular one-shot bound need not prove convergence on a long horizon; the `R²` term in its stability exponent can dominate the Gaussian tail exponent. Local-in-time arguments or sharper stability estimates are needed. The cutoff result is therefore not a proof of an arbitrary-accuracy, jointly polynomial Gaussian-block solver for every `k`.

## 5. Dense Gaussian identification is a separate limit interchange

Let `F_{b,k}` denote the output process with `b` Gaussian blocks of size `k`, and let `F_k=lim_{b→∞}F_{b,k}` when this population limit exists. With one block, `F_{1,k}` is the canonical width-`k` dense Gaussian system, apart from any explicitly separated readout-initialization convention.

The desired identification is

\[
\lim_{k\to\infty}\lim_{b\to\infty}F_{b,k}
=\lim_{k\to\infty}F_{1,k}.
\]

The equality does not follow from the identity on the line `b=1`. It exchanges a block-population limit with an increasing local interaction range. Finite-time nonlinear feedback and repeated reuse of both `G` and `G^T` are precisely the mechanisms for which an initialization central limit theorem is insufficient.

A concrete sufficient route is to define the causal block response map under imposed global fields, prove that its averaged response converges to the same Gaussian dynamical law that governs the canonical dense model, and establish a uniform stability/uniqueness estimate for the self-consistency equation. The latter converts the response-map consistency error into output error. Both statements must include the entire time interval and the finite-`P` memories, not just initial covariances or static feature distributions.

The finite blocks preserve all repeated-matrix response paths internally. This is a reason the construction is plausible, and a distinction from replacing each multiplication by fresh independent Gaussian noise. It is not a proof of the limit identification.

If dense-limit existence and a quantitatively stable response-map theorem are assumed, one can state the final conditional hierarchy theorem: for every `T,ε`, choose a block size `k` whose dense-identification error is at most `ε/3`, control Gaussian truncation by `ε/3`, and choose `q` from the particle error bound to achieve the remaining `ε/3`. The state is then independent of `n`. A polynomial total complexity theorem additionally requires quantitative polynomial sampling stability and a quantitative relation between `k` and the identification error.

## 6. Non-vacuity and error bookkeeping

The distinct errors are:

- finite original width/block count (`b`) versus its fixed-`k` population law;
- the vanishing initial readout (`1/n`) convention;
- sampling the population law with `q` blocks;
- any spectral cutoff or modification of Gaussian initialization;
- large-block (`k`) identification with the dense Gaussian population target;
- time discretization, if the scalar ODE is numerically integrated;
- finite-`P` closure error only if the target is later changed to the untruncated training dynamics.

The present task fixes `P`, so improving `q` or `k` does not establish convergence as `P→∞`.

An independent sampled surrogate targets population outputs. It cannot reproduce arbitrary finite-`n` realization fluctuations without additional information or coupling. A finite-`n` guarantee must specify a width threshold and probability mode.

Repeating the same finite matrix block is another full-rank initialization, but its fixed-`k` population law is conditional on that matrix and generally retains quenched randomness. Repeating all initial block states as well makes the dynamics exactly a width-`k` dense network; that is a tautological small-network encoding and changes the stipulated iid first-layer initialization. Independent blocks with iid first-layer rows avoid that exact collapse, but still require the identification theorem above.

The honest current claim is therefore: an exact block-particle skeleton and a finite autonomous Monte Carlo approximation are available; the full polynomial-complexity Gaussian hierarchy is a promising conditional program, with a reachable-backpropagation stability estimate and the dense-limit identification as its two major open obligations.
