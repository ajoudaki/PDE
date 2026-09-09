# Legal bounded queries: a positive theorem and the remaining derivative gap

2026-09-08. Independent adversarial audit. The only program documents read were
`CONTRACT.md` and `development/BOUNDED_SINE_PICARD.md`. No experiments were run.
The mathematical-proof skill was used for proof discipline.

## Finding

I found **no valid concentration counterexample** satisfying all the requested
restrictions. In particular, a normalized shrinking-support probe is not legal,
and using a bounded probe followed by a discontinuous sign operation merely
moves the missing amplification into the update.

There is a positive finite-time theorem below. Bounded, Lipschitz queries and
semilinear causal updates have uniformly sub-Gaussian Gaussian-action source
paths, without any gradient or energy hypothesis. The proof keeps the same
matrix and its transpose and permits arbitrarily many continuous interactions.
It is not a fixed-query independence argument.

The actual bounded-sine flow is outside the theorem's update class. Its update
contains a *state-dependent* coefficient multiplying an incoming field. Bounded
derivatives of that coefficient do not make the entire update globally
Lipschitz. A completely legal one-query example demonstrates that the resulting
variational response can have a diverging maximum at fixed physical time, even
for a true gradient flow with a nonnegative energy and exact dissipation. That
example does **not** concentrate sources. It rules out an unjustified shortcut,
not the physical target.

Thus neither generic Gaussian-action concentration examples nor a claim of
uniform Lipschitzness settles the bounded-sine branch. A reached-path estimate
that tolerates random, unbounded local responses is still needed.

## 1. What concentration means here

Write `A=G/sqrt(n)`, where the entries of `G` are independent standard Gaussians,
and use `||x||_n^2=n^{-1} sum_j |x_j|^2`. For a scalar source path `q_j(t)`, put

\[
Q_j=\sup_{0\le t\le T}|q_j(t)|.
\]

A sufficient condition excluding concentration is

\[
\lim_{K\to\infty}\sup_n
\mathbb E\left[\frac1n\sum_j Q_j^2\mathbf1_{Q_j>K}\right]=0.
\tag{1.1}
\]

Indeed, for any possibly matrix-dependent sets `S_n`,

\[
\sup_{t\le T}\frac1n\sum_{j\in S_n}|q_j(t)|^2
\le K^2\frac{|S_n|}{n}
+\frac1n\sum_jQ_j^2\mathbf1_{Q_j>K}.
\tag{1.2}
\]

If `|S_n|/n` tends to zero in probability, first use (1.1) and Markov's
inequality on the second term, and then send `n` to infinity in the first.
The left side tends to zero in probability. This allows completely adaptive
choices of the concentrating sets.

This audit addresses (1.1), not just boundedness of `||q(t)||_n`.

## 2. A positive finite-time theorem for smooth legal queries

Here is a precisely specified causal class. Fix finite row dimensions `d_1,d_2`,
independent of width. Let

\[
F_\ell:\mathbb R^{d_\ell}\to\mathbb R^{d_\ell},\qquad
p_\ell:\mathbb R^{d_\ell}\to\mathbb R,\qquad
s_\ell\in\mathbb R^{d_\ell}
\]

be fixed maps and vectors. Suppose `F_ell` are globally Lipschitz and
`p_ell` are bounded and globally Lipschitz. For convenience they may be `C^1`
with bounded derivatives; Lipschitz maps alone suffice. There are no
width-dependent gains, normalizations other than `A=G/sqrt(n)`, or time scales.

The row states solve

\[
\begin{aligned}
\dot X_j&=F_1(X_j)+s_1 q_j,&
q&=A^Tp_2(Y),\\
\dot Y_a&=F_2(Y_a)+s_2 v_a,&
v&=Ap_1(X).
\end{aligned}
\tag{2.1}
\]

Initialize every first-layer row at one fixed `x_*` and every second-layer row
at one fixed `y_*`. These initial states are deterministic and independent of
the matrix. Every actual matrix probe is bounded, namely `p_1(X)` or `p_2(Y)`.
The incoming fields themselves need not be bounded. Equation (2.1) is affine
in each incoming field. For each finite matrix, its full vector field is
globally Lipschitz, so the solution exists uniquely for all finite times.

**Theorem 2.1.** For every fixed `T<infinity`, there are `alpha_T>0` and
`C_T<infinity`, independent of `n` and of the selected coordinate, such that

\[
\sup_n\mathbb E\exp\left(
\alpha_T\sup_{t\le T}|q_j(t)|^2\right)\le C_T,
\qquad
\sup_n\mathbb E\exp\left(
\alpha_T\sup_{t\le T}|v_a(t)|^2\right)\le C_T.
\tag{2.2}
\]

In particular, (1.1) holds in both layers. No independence between a trained
query and `A` is asserted or used. No energy identity is assumed.

### Proof: stop only the initial matrix norm

Choose constants `B,L,c` bounding the two query maps, their Lipschitz constants,
the drift Lipschitz constants, `|F_ell(0)|`, and `|s_ell|`. All constants below
may depend on these fixed quantities, the initial states, and `T`.

Fix a numerical `M`, chosen sufficiently large below, and set

\[
\mathcal D_M=\{G:\|G/\sqrt n\|_{\rm op}\le M\}.
\]

On this set, a deterministic Gronwall bound in the ordinary Euclidean norm
gives

\[
\sup_{t\le T}\big(\|X(t)\|+\|Y(t)\|
+\|\dot X(t)\|+\|\dot Y(t)\|\big)
\le C_{T,M}\sqrt n.
\tag{2.3}
\]

To check the normalization, a query has Euclidean norm at most `B sqrt(n)`, so
each action in (2.1) has norm at most `MB sqrt(n)`. Also
`||F_ell(X)|| <= L ||X|| + |F_ell(0)| sqrt(n)`.
Integrating this scalar differential inequality first bounds the state, and
substitution into (2.1) then bounds its velocity. This proves (2.3).

Differentiating the queries almost everywhere gives

\[
\|\dot q(t)\|\le ML\|\dot Y(t)\|,
\qquad
\|\dot v(t)\|\le ML\|\dot X(t)\|.
\]

Consequently, with a constant `D_{T,M}` independent of width,

\[
\frac1n\sum_jQ_j^2
\le 2\|q(0)\|_n^2+
2T\int_0^T\|\dot q(t)\|_n^2dt
\le D_{T,M}^2
\quad\hbox{on }\mathcal D_M.
\tag{2.4}
\]

The identical estimate holds for the forward path supremum. Thus the theorem
will control the whole source path, not just its values at prescribed times.

### Proof: sensitivity to the underlying Gaussian entries

Consider any two matrices `G, G_tilde` in `D_M`, and their solutions with the
same deterministic initial state. Put
`Delta=||X-X_tilde||+||Y-Y_tilde||` and
`epsilon=||G-G_tilde||_F`. Splitting the matrix difference in each action yields

\[
\begin{aligned}
\|A^Tp_2(Y)-\widetilde A^Tp_2(\widetilde Y)\|
&\le ML\|Y-\widetilde Y\|+B\varepsilon,\\
\|Ap_1(X)-\widetilde Ap_1(\widetilde X)\|
&\le ML\|X-\widetilde X\|+B\varepsilon.
\end{aligned}
\tag{2.5}
\]

The factor `sqrt(n)` in a bounded query cancels the `1/sqrt(n)` in the Gaussian
matrix scaling. Thus (2.1), its integral form, and Gronwall give

\[
\sup_{t\le T}\Delta(t)\le C_{T,M}\varepsilon.
\]

Substitution into (2.5) proves

\[
\sup_{t\le T}\big(\|q(t)-\widetilde q(t)\|
+\|v(t)-\widetilde v(t)\|\big)
\le K_{T,M}\|G-\widetilde G\|_F.
\tag{2.6}
\]

In particular, the scalar function `G -> Q_j(G)` is `K_{T,M}`-Lipschitz on
`D_M` in the ordinary Euclidean metric on the `n^2` independent Gaussian
entries. This is a dimension-free bound. It is the step that will fail for the
actual state-dependent multiplier unless a new estimate is supplied.

### Proof: concentration and its center

Extend `Q_j` from `D_M` to all matrices with the same Lipschitz constant, for
example by

\[
\widehat Q_j(G)=\inf_{H\in\mathcal D_M}
\{Q_j(H)+K_{T,M}\|G-H\|_F\}.
\]

The extension is nonnegative and equals `Q_j` on `D_M`. A `K`-Lipschitz function
`f` of a standard Gaussian vector in any finite dimension satisfies

\[
\mathbb P(f-\mathbb Ef\ge u)\le e^{-u^2/(2K^2)},
\qquad
\mathbb P(f-\mathbb Ef\le-u)\le e^{-u^2/(2K^2)}.
\tag{2.7}
\]

One proof is included after the theorem so that no unverified adaptive-query
concentration theorem is being invoked.

The joint dynamics, initialization, and stopping event are invariant under
permutations of the first-layer coordinates. Equation (2.4) therefore gives

\[
\mathbb E[Q_j^2\mathbf1_{\mathcal D_M}]\le D_{T,M}^2.
\tag{2.8}
\]

Take `M` large enough that `P(D_M)>=3/4` for every width. Markov's inequality
and (2.8) imply

\[
\mathbb P(\widehat Q_j\le2(D_{T,M}+1))\ge\tfrac12.
\]

The lower-tail inequality in (2.7) now bounds its mean by

\[
\mathbb E\widehat Q_j
\le2(D_{T,M}+1)+K_{T,M}\sqrt{2\log2}.
\tag{2.9}
\]

Combining (2.7) and (2.9), and integrating the resulting Gaussian upper tail,
shows that `E exp(alpha Q_j^2) 1_{D_M}` is bounded uniformly in width for some
fixed positive `alpha`. The same argument uses second-layer permutations for
the forward source.

### Proof: remove the matrix-norm stop

A `1/4`-net of the unit sphere in `R^n` has at most `9^n` points, by the
disjoint-ball volume argument. Approximating each of the two unit vectors in
the bilinear expression for the operator norm shows

\[
\|A\|_{\rm op}
\le2\max_{u,v\text{ in the nets}}|u^TAv|.
\]

Each scalar on the right is Gaussian with variance `1/n`. A union bound gives

\[
\mathbb P(\|A\|_{\rm op}>s)
\le2\exp(2n\log9-ns^2/8)
\le2e^{-ns^2/16}\quad(s\ge M),
\tag{2.10}
\]

where, for example, `M=16` suffices and ensures the earlier probability bound.
Independently of the dynamics or of the initial state,

\[
Q_j\le B\sqrt n\|A\|_{\rm op},
\tag{2.11}
\]

because every reverse query is bounded. Put `beta=alpha B^2<1/16`. Integrating
(2.10) against the derivative of `exp(beta n s^2)` gives

\[
\begin{split}
\mathbb E[e^{\alpha Q_j^2}\mathbf1_{\mathcal D_M^c}]
&\le2e^{-(1/16-\beta)nM^2}\\
&\quad+4\beta n\int_M^\infty
s e^{-(1/16-\beta)ns^2}\,ds.
\end{split}
\]

The right side is uniformly bounded. Decrease the `alpha` obtained above to
satisfy this restriction. This proves (2.2) and hence (1.1). The proof for `v`
is identical. ∎

**Verification of (2.7).** For a smooth `K`-Lipschitz function of an
`N`-dimensional standard Gaussian, let `B_t` be standard Brownian motion and
let `P_t` be its heat semigroup. The martingale
`M_t=P_{1-t}f(B_t)` satisfies
`dM_t=grad P_{1-t}f(B_t) dB_t`. Averaging the gradient preserves its bound `K`,
so its quadratic variation at time one is at most `K^2`. The exponential
martingale inequality gives
`E exp(lambda(f(B_1)-Ef(B_1))) <= exp(lambda^2 K^2/2)`.
Markov's inequality and minimization over positive or negative `lambda` give
(2.7). Mollification preserves the Lipschitz bound and converges pointwise;
the at-most-linear growth of Lipschitz functions permits passage to Gaussian
exponential moments. This covers the extension used above.

## 3. Why a legal bounded needle does not reproduce the usual example

For a deterministic set `S` of density `delta`, the normalized needle

\[
e_\delta=\delta^{-1/2}\mathbf1_S
\]

has unit normalized `L^2` norm but unbounded coordinate size as `delta` tends
to zero. It cannot be a bounded forward query.

The legal replacement `a=1_S` gives `(Aa)_r` of variance `delta`. A fixed
`L`-Lipschitz scalar operation obeys

\[
\mathbb E|\psi((Aa)_r)-\psi(0)|^2\le L^2\delta.
\tag{3.1}
\]

On a bounded-operator event, one more matrix or transpose action changes its
normalized norm by at most the fixed operator norm. For any fixed finite
composition whose whole row operations are globally Lipschitz, the same
comparison propagates the smallness with a fixed constant. The continuous
version of that statement is (2.5)–(2.6).

To change the vanishing signal into a nonvanishing reverse query immediately,
one must insert a discontinuity, an amplification diverging with `delta`, or
some operation outside this globally Lipschitz class. For example,
`sign(Aa)` discards the small scale and `tanh((Aa)/sqrt(delta))` inserts it
explicitly into a diverging gain. Neither is a fixed bounded-gain update.

This observation is not a theorem about every permitted affine-in-field
continuous update. It explains exactly why that common counterexample does
not supply the requested negative result.

## 4. A legal gradient example defeats the stronger Lipschitz shortcut

Primitive smoothness and query boundedness do not imply the uniform
variational estimate used in (2.6).

Query the matrix once with the deterministic bounded vector `1` and store

\[
V=A\mathbf1.
\]

The `V_a` are independent standard Gaussians. In each second-layer row, run the
fixed scalar equation

\[
\dot x_a=V_a\sin x_a,\qquad x_a(0)=0.
\tag{4.1}
\]

If a reverse probe is desired, use `sin(x)`, which is bounded and is zero on
this trajectory. There is no direct access to any matrix entry. One initial
state and one stored incoming field per row suffice. The update is affine in
the incoming field, its coefficient and every derivative of that coefficient
are bounded by one, the physical horizon is fixed, and there is no hidden
normalization or width-dependent gain.

The trajectory is exactly `x(t)=0`. Its derivative with respect to its initial
condition is, however,

\[
\frac{\partial x_a(t)}{\partial x_a(0)}=e^{tV_a}.
\tag{4.2}
\]

For every `t>0` and every fixed `K`,

\[
\mathbb P\left(\max_a e^{tV_a}\le K\right)
=\Phi((\log K)/t)^n\longrightarrow0.
\tag{4.3}
\]

Thus the state-space variational propagator has no width-uniform deterministic
operator bound with high probability. This happens on a perfectly legal,
stationary trajectory. On the other hand, each row response has every fixed
moment: `E exp(pt V)=exp(p^2 t^2/2)`. The Gaussian source `V` does not
concentrate, and the reverse source is zero. This is expressly **not** a source
concentration counterexample.

The example can also be an exact true gradient flow. Equip the `x` state with
the normalized raw metric and define the nonnegative energy

\[
\mathcal E_n(x)=\frac1n\sum_a
\left[\sqrt{1+V_a^2}+V_a\cos x_a\right].
\tag{4.4}
\]

Its negative raw gradient is (4.1), and direct differentiation gives

\[
\frac{d}{dt}\mathcal E_n(x(t))
=-\frac1n\sum_a|\dot x_a(t)|^2.
\tag{4.5}
\]

The energy has a finite width-independent initial expectation. On the chosen
trajectory, displacement and dissipated energy are both zero, while (4.3)
still holds.

Equation (4.4) is not the contract's network square loss, and the initialized
Gaussian matrix is frozen. Therefore it establishes only the stated logical
point: being an energy-dissipating true gradient flow does not, by itself,
bound the variational response. A use of physical training must exploit more
than the bare gradient identity or its displacement consequence.

## 5. Exact relation to the bounded-sine physical equations

For the separate activation `phi(z)=1+(1/2) sin(z)`, the earlier report gives,
on each fixed energy-stopped horizon, uniform coordinate bounds for

\[
h_i,\quad C,\quad b_i=C\phi'(v_i),\quad
\mathcal U(a,b),
\]

where `A=A_0+U` and `U` has normalized kernel `mathcal U`. In particular, the
learned corrections `U h_i` and `U^*b_i` are coordinatewise bounded. Possible
source concentration is therefore carried by the original Gaussian actions
`A_0h_i` and `A_0^*b_i`.

The first-layer equation has the form

\[
\dot z_i=-\sum_j\Gamma_{ij}r_j\phi'(z_j)q_j.
\tag{5.1}
\]

Comparing two solutions produces the exact component

\[
-\sum_j\Gamma_{ij}r_j
\big(\phi'(z_j)-\phi'(\widetilde z_j)\big)q_j.
\tag{5.2}
\]

Consequently the pointwise derivative of this row update contains
`r_j phi''(z_j) q_j`. Its coefficient `phi'` is bounded, and its derivative
`phi''` is bounded, but the derivative of the **whole** update with respect to
the local state is not bounded independently of the incoming field.
This is the exact reason that (2.5) does not lead to the state comparison used
in (2.6). The same distinction is already visible in (4.1).

The physical energy supplies a bound on residuals, the matrix operator norm,
the readout, and integrated raw speed. It supplies no immediate bound on
`max_j |q_j|`, on multiplication by `q_j` in `L^2`, or on the state-space
variational propagator. Example (4.4) shows why one cannot infer the last
bound from the abstract gradient identity. The contract's additional special
structure is its square-loss residual feedback with all three blocks trained;
none of the positive estimates here uses that structure, and the example does
not reproduce it.

A sufficient extension of the proof of Theorem 2.1 would be a dimension-free
Lipschitz estimate for each physical source as a function of the Gaussian
initialization on suitable high-probability events, together with a uniform
center bound. A uniform bound on the full state variational propagator would
be stronger than necessary and is an implausible intermediate requirement in
view of (4.2). Alternatively, a cavity estimate or an averaged response
estimate could tolerate the individual factors `exp(tV)` and still establish
(1.1). No such extension is proved in this audit.

## 6. Claim boundary

| Statement | Status |
|---|---|
| Bounded queries with semilinear globally Lipschitz continuous updates have finite-time source-path sub-Gaussian tails | Proved in Theorem 2.1 |
| A bounded shrinking-support probe plus a fixed globally Lipschitz finite computation reproduces the normalized-needle concentration example | Ruled out by the small-signal estimate in Section 3 |
| Bounded derivatives of the primitive scalar coefficients imply a uniform state variational bound | Refuted by the legal example (4.1) |
| A true gradient identity and finite raw displacement repair that variational implication | Refuted as an abstract implication by (4.4)–(4.5) |
| The legal example concentrates a Gaussian-action source | False; its nonzero source is exactly Gaussian |
| A concentration counterexample exists under all of the requested broader causal restrictions | Not established |
| The actual bounded-sine physical sources satisfy (1.1) | Not established |
| The bounded-sine or principal affine–tanh contract is resolved | Not established |

The useful positive conclusion is that bounded legal queries can decisively
change the tail problem: they suffice for a large continuous-interaction class
without energy. The remaining issue is the actual flow's state-dependent
affine multiplier and its averaged response, not an already available generic
bounded-query counterexample.
