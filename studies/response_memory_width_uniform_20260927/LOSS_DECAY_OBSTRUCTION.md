# A stationary closure and arbitrarily long Gaussian plateaus

Scoped theoretical check, 28 September 2026. This note checks a witness
proposed by the supervising task; it is not an independent discovery or an
isolated review. Permitted inputs were the current `paper/main.tex` canonical
model and response-memory equations, this study's `OLD_CLOCK_ROUTE.md` and
`ENERGY_STABILITY_ROUTE.md`, and `docs/notation.qmd` as needed. The
`solve-math-rigorously` skill was applied. No training experiment, external
literature, other study, or maintained-file change was used.

**Conclusion.** Orthogonal normalized inputs, realizability by the same
architecture, and nonsingular hidden matrices do not imply loss decay for
every deterministic initialization of any finite-order response-memory
closure. A stationary example below has loss `5/2` at every time and every
order. Continuous dependence then gives arbitrarily long loss plateaus on
open sets of finite-width Gaussian initializations, including small nonzero
readouts. The exact stationary witness has Gaussian probability zero. Neither
the witness nor the open-set plateau argument refutes almost-sure eventual
decay, a quantitative high-probability theorem, or a population theorem.

## 1. Canonical setup and a nonsingular initialization

Use the manuscript's canonical tanh model and mobilities with

\[
 n=d=m=2,\qquad L=2,\qquad
 x_1=\sqrt2\,e_1,\quad x_2=\sqrt2\,e_2,\qquad
 y_1=2,\quad y_2=-1.
\]

The inputs are orthogonal and each has norm `sqrt(d)`. Let

\[
 a=\frac18,\qquad Q(s)=\operatorname{atanh}(\operatorname{atanh}s),
\]
\[
 W^{(1)}_0=
 \begin{pmatrix}Q(a)&Q(2a)\\Q(2a)&Q(4a)\end{pmatrix},
 \qquad W^{(2)}_0=I_2,\qquad w_0=0.
 \tag{1}
\]

All evaluations of `Q` are real: `4a=1/2<tanh(1)`, so
`atanh(s)<1` on the required interval. Since

\[
 \tanh(\tanh(Q(s)))=s,
\]

the initial top-feature matrix, with samples as columns, is

\[
 H_0=
 \begin{pmatrix}a&2a\\2a&4a\end{pmatrix}.
 \tag{2}
\]

Both hidden parameter matrices in (1) are nonsingular. To check the first,
write the convergent Taylor expansion on this interval as
`Q(s)=sum_j c_j s^{p_j}`, with positive coefficients, distinct positive odd
exponents, and at least two terms. This follows by composing the convergent
positive-coefficient odd series for `atanh`; for example the coefficients of
`s` and `s^3` are `1` and `2/3`. Apply Cauchy--Schwarz to the sequences

\[
 u_j=\sqrt{c_j a^{p_j}},\qquad v_j=2^{p_j}u_j.
\]

They belong to `ell^2` because their squared norms are `Q(a)` and `Q(4a)`.
They are not proportional because at least two distinct exponents occur.
Consequently

\[
 Q(2a)^2=\left(\sum_j u_jv_j\right)^2
 <\left(\sum_j u_j^2\right)\left(\sum_jv_j^2\right)
 =Q(a)Q(4a),
\]

which is exactly `det W^(1)_0>0`. In particular this construction uses
nonzero first-layer weights and an invertible initialized hidden link, with
`||W^(2)_0||_op=1`. It does use a rank-deficient feature matrix (2).

## 2. The physical trajectory is stationary for every order

At (1), the residual vector is `r=-y=(-2,1)^T`. Equation (2) gives

\[
 H_0y=0.
\]

The canonical readout velocity therefore vanishes:

\[
 \dot w=-\frac2mH_0r=\frac2mH_0y=0.
\]

Since `w=0`, every backward response `delta_a^(ell)` vanishes. Thus the
first-layer velocity is zero and every residual-weighted backward memory
remains zero. The reconstruction consequently keeps
`W_hat^(2)=W^(2)_0=I_2`, irrespective of the order `P>=1`.

For completeness, the forward moment coordinates do move. Set

\[
 \rho_*=\sqrt{\frac52},\qquad \tau(t)=1+\rho_*t.
\]

For each constant forward history `h_a=h_a^(1)(0)`, the old-clock moments are

\[
 \bar h_{a,0}(t)=\tau(t)h_a,\qquad
 \bar h_{a,k}(t)=0\quad(1\le k<P),\qquad
 \bar\delta_{a,k}(t)=0\quad(0\le k<P).
 \tag{3}
\]

These formulas satisfy the prescribed prefix initialization. For `k=0`,
the forward moment ODE is `dot bar h_(a,0)=rho_* h_a`. For `k>=1`, its
right side is

\[
 \rho_*h_a-\frac{\rho_*}{\tau}
 \left[k\,0+(2\cdot0+1)\bar h_{a,0}\right]=0,
\]

because all other lower moments vanish. The backward ODE has zero forcing
and zero initial state. Substitution into the reconstruction proves that
(1) and (3) solve the complete autonomous old-clock system. Its local
uniqueness identifies this as the actual initialized trajectory; (3) exists
for all physical times.

For the joint clock, both the forward responses and
`b_a=r_a delta_a/rho_*` are constant, with `b_a=0`. Hence the response-speed
term is zero and its clock also satisfies `dot tau=rho_*`. Its backward
moments are zero, so its reconstruction also remains `I_2` for every order.

It follows for either clock that

\[
 \mathcal L(t)=\frac52\quad(t\ge0),\qquad
 \int_0^\infty\sqrt{\mathcal L(t)}\,dt=\infty.
 \tag{4}
\]

Thus it is the physical network parameters that are stationary; the full
state includes an advancing clock and growing zeroth forward moments.

## 3. The same architecture interpolates the data

Keep `n=d=m=L=2` and `W^(2)=I_2`, but choose

\[
 W^{(1)}=
 \begin{pmatrix}Q(a)&0\\0&Q(a)\end{pmatrix},
 \qquad w=\begin{pmatrix}4/a\\-2/a\end{pmatrix}.
\]

The two top features are `(a,0)^T` and `(0,a)^T`. With the canonical
readout normalization `f_a=w^T h_a^(2)/n`, their predictions are exactly

\[
 f_1=\frac12(4/a)a=2,\qquad
 f_2=\frac12(-2/a)a=-1.
\]

This is a finite exact interpolator of the same data in the same
architecture. The obstruction in (4) is therefore not inconsistent labels,
near-parallel inputs, or insufficient expressive capacity.

## 4. What Gaussian full support does and does not imply

Fix a finite order `P` and finite horizon `T`. The old-clock raw ODE is
locally Lipschitz in its state on `tau>0`: it uses `rho=||r||/sqrt(m)` and
`r_a delta_a`, without division by `rho`. Its prefix state depends
continuously on the initialization. The explicit reference trajectory (3)
stays in a compact subset of `tau>=1` on `[0,T]`. Finite-horizon continuous
dependence therefore gives an open neighborhood `U_(P,T)` of the
initialization (1) such that all initializations in that neighborhood obey

\[
 \sup_{0\le t\le T}|\rho(t)-\rho_*|<\frac{\rho_*}{2},
 \qquad
 \int_0^T\rho(t)\,dt\ge\frac{\rho_*T}{2}.
 \tag{5}
\]

Here the neighborhood includes perturbations of both hidden parameter
blocks **and the readout**. It can be intersected with any prescribed open
ball `||w_0||<epsilon`, `epsilon>0`, and still be an open neighborhood of
(1). It can also be chosen inside one fixed bounded neighborhood, common
to all `T`, in which the first-layer matrix remains invertible and, for
example, `1/2<||W^(2)_0||_op<3/2`. This follows by first fixing that bounded
open neighborhood and then intersecting each continuous-dependence
neighborhood with it.

At finite width, independent nondegenerate Gaussian first-layer, hidden,
and readout entries have a strictly positive joint density everywhere.
Thus `U_(P,T)` has positive probability for canonical Gaussian hidden
initialization and a nondegenerate small Gaussian readout, including the
stored convention `w_(0,i)~N(0,1/n^2)`. Under a continuous readout law,
`w_0=0` itself has probability zero; (5) applies to an open set of small
nonzero readouts instead. If the convention fixes `w_0=0` deterministically,
the section of this neighborhood at zero readout is open in the hidden
parameters and has positive hidden-Gaussian probability as well.

Consequently no finite deterministic bound on `int_0^infinity rho(t) dt`
that depends only on this fixed data geometry, order, architecture, and
these upper parameter-norm bounds can hold uniformly over the permitted
Gaussian realizations. Given a proposed bound `C`, choose
`T>2C/rho_*`; (5) violates it on a positive-probability set within the same
bounded parameter neighborhood. Likewise, a uniform deterministic decay
envelope tending to zero is impossible under only those restrictions.

This is a finite-horizon support argument. The neighborhoods and their
probabilities may shrink with `T` and may depend on `P`. It does **not**
establish a positive-probability set with an infinite plateau. In particular:

- The exact stationary initialization in (1) has Gaussian probability zero.
- No failure of almost-sure eventual fitting or almost-sure finiteness of
  `int_0^infinity rho` has been proved.
- A high-probability estimate with explicit failure-probability and width
  dependence is not contradicted.
- No population-limit obstruction follows from this finite-width example.

Additional dynamical or probabilistic arguments remain necessary for those
stronger Gaussian and population questions.
