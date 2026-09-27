# Aggregate Galerkin dynamics on Gaussian initial labels

Scoped internal theoretical audit, 2026-09-27. Inputs were only
`block_scalar_closure.py`, `BLOCK_HIERARCHY_ROUTE.md`,
`RESTRICTED_THEOREM.md`, `GAUSSIAN_HIERARCHY_ASSESSMENT.md`, and the
supervisor's assignment. The investigate-conjectures and
solve-math-rigorously skills were applied. No training, experiment, external
scientific input, other study, or another agent's findings were used.

## Conclusion and scope

There is a genuine aggregate construction: evolve polynomial coefficients
of the entire block state as a function of its immutable Gaussian initial
labels. It does not evolve independently sampled representative blocks.
Its basis is fixed in initial-label space, while both layers' features and
all memory factors move.

Unmodified Hermite Galerkin convergence is not established by this audit.
Unbounded Gaussian multiplication and loss of pointwise bounds after
projection obstruct the immediate Hilbert-space argument. Both can be
repaired by a specified, vanishing regularization: truncate the static block
matrix and clip auxiliary dynamic coordinates outside a rigorously known
finite-horizon reachable region. The resulting finite coefficient ODEs
converge on every finite horizon to the untruncated Gaussian-block
population closure at fixed block size and fixed memory order. A short-time
Gaussian integrability argument removes the matrix cutoff globally in time;
one must not integrate a single `exp(C_T T ||G||^2)` estimate.

This result concerns the canonical population convention `c(0)=0`.
Fixed-variance Gaussian initial readouts need another tail argument. The
finite-width readout variance `1/n^2` in the supplied sources vanishes in
the population target.

There is an additional approximation degree `J`. It cannot be omitted from
the state count. One can fold all chosen truncations into one hierarchy
index, but that changes what the index denotes. A claim of arbitrary
accuracy at fixed `k,m,P` and fixed coefficient count does not follow.

## Exact label representation and finite coefficient equations

Fix `k,m,P,d`, bounded data `|u_a|<=1`, and let

\[
s=k^2+kd,\qquad D=k(d+1+2mP),\qquad \xi\sim\gamma_s=N(0,I_s).
\]

Use the first `k^2` coordinates to form `G(ξ)` with independent entries
`ξ_ij/sqrt(k)`, and the remaining `kd` coordinates for `w_0(ξ)`.
The exact block state is

\[
X(t,\xi)=(w,c,A_0,\ldots,A_{P-1},B_0,\ldots,B_{P-1})\in\mathbb R^D,
\]

where `w` is `k×d`, `c` is `k`, and every `A_j,B_j` is `k×m`.
There is one common scalar `L`. Set

\[
X_0=(w_0,0,0,B_{00},0,\ldots),\quad
(B_{00})_{ia}=\tanh((w_0)_i\cdot u_a),\qquad L_0=1.
\]

For any bounded test input, all expectations below mean Gaussian-label
integration and are computed from the current coefficient state:

\[
\begin{aligned}
h(u,\xi)&=\tanh(w(\xi)u),\\
S_j(u)&=\mathbb E[k^{-1}B_j^{\mathsf T}h(u)],\\
z(u,\xi)&=G(\xi)h(u,\xi)
 -\frac2{mL}\sum_{j<P}(2j+1)A_j(\xi)S_j(u),\\
H(u,\xi)&=\tanh z(u,\xi),\qquad
f(u)=\mathbb E[k^{-1}c^{\mathsf T}H(u)],\\
\delta_a(\xi)&=c(\xi)\odot\operatorname{sech}^2z(u_a,\xi),\\
V_j(u_a)&=\mathbb E[k^{-1}A_j^{\mathsf T}\delta_a],\\
b_a(\xi)&=\operatorname{sech}^2(w(\xi)u_a)\odot
\left[G(\xi)^{\mathsf T}\delta_a(\xi)
 -\frac2{mL}\sum_{j<P}(2j+1)B_j(\xi)V_j(u_a)\right].
\end{aligned}
\]

Writing `r_a=f(u_a)-y_a`, `ρ=(m^{-1}Σ_a r_a^2)^{1/2}`, the vector field is

\[
\begin{aligned}
F_w&=-\frac2m\sum_a r_a b_a u_a^{\mathsf T},&
F_c&=-\frac2m\sum_a r_a H(u_a),\\
F_{A_{ja}}&=r_a\delta_a-\frac\rho L
\left[jA_{ja}+\sum_{\ell<j}(2\ell+1)A_{\ell a}\right],\\
F_{B_{ja}}&=\rho h(u_a)-\frac\rho L
\left[jB_{ja}+\sum_{\ell<j}(2\ell+1)B_{\ell a}\right],&
\dot L&=\rho.
\end{aligned}
\tag{1}
\]

These are exactly the population version of the supplied implementation.
The expectations are evaluated in the causal order `S`, then `f,δ`, then
`V`; there is no same-time implicit fixed point.

Let `Ψ_α` be the normalized product Hermite polynomial for the standard
Gaussian measure, and `I_J={α∈N^s:|α|<=J}`. Write

\[
X_J(\xi)=\sum_{\alpha\in I_J}x_\alpha\Psi_\alpha(\xi).
\]

With `F_R^*` the explicitly regularized field defined below, the aggregate
ODE is

\[
\dot x_\alpha=\mathbb E[\Psi_\alpha F_R^*(X_J,L;\xi)],\qquad
\dot L=\rho_R^*(X_J,L),\qquad
x_\alpha(0)=\mathbb E[\Psi_\alpha X_0].
\tag{2}
\]

Every coordinate is an ordinary scalar coefficient. The exact dynamic
state count is

\[
N_{\rm dyn}=1+k(d+1+2mP)\binom{k^2+kd+J}{J}.
\tag{3}
\]

For `d=2`, this becomes
`1+k(3+2mP) binom(k^2+2k+J,J)`. No random initial block matrices are stored.
Static data consist of the dataset, the formula for the Gaussian law and
basis, truncation parameters, and any chosen quadrature representation.
Basis multiindices can be enumerated; storing them explicitly costs at most
`s binom(s+J,J)` integers. If an additional independent Gaussian readout
label were included, `s` would become `k^2+kd+k`, but the theorem below has
not proved that enlarged initialization case.

## A priori bounds and the regularized field

Fix a finite horizon `T`, put `Y=max_a |y_a|`, and define

\[
C=Y(e^{2T}-1),\quad H=C+Y,\quad
A=HCT,\quad B=\Lambda=1+HT.
\tag{4}
\]

The same scalar comparisons as in the supplied restricted theorem give,
for the exact block closure with any static matrix law,

\[
|c_i|\le C,\quad |A_{jia}|\le A,\quad |B_{jia}|\le B,
\qquad1\le L\le\Lambda.
\tag{5}
\]

Indeed `|f_a|<=||c||∞` and `|dot c_i|<=2(||c||∞+Y)`. For the sharper
memory bounds, let `p_j` denote the shifted Legendre polynomial on `[0,1]`.
Its identities `p_j(1)=1` and
`x p_j'(x)=j p_j(x)+Σ_(ell<j)(2ell+1)p_ell(x)` show, by differentiation,
that the exact memory solution is

\[
\begin{aligned}
A_{ja}(t)&=\int_0^t r_a(s)\delta_a(s)
 p_j\!\left(\frac{L(s)}{L(t)}\right)ds,\\
B_{ja}(t)&=h_a(0)\int_0^1p_j\!\left(\frac{v}{L(t)}\right)dv
+\int_0^t\rho(s)h_a(s)
 p_j\!\left(\frac{L(s)}{L(t)}\right)ds.
\end{aligned}
\tag{4a}
\]

The first term of `B` gives precisely its prescribed initial moments,
since `∫_0^1 p_j=1` for `j=0` and zero otherwise. The elementary bound
`|p_j(x)|<=1` on `[0,1]` follows, for example, from
`P_j(cos θ)=π^{-1}∫_0^π(cos θ+i sin θ cos φ)^j dφ`: the integrand has
modulus at most one. The identity is verified by expansion, and the
imaginary terms integrate to zero. Since `1<=L(s)<=L(t)`, (4a) gives
`|A_j|<=HCT` and `|B_j|<=1+∫_0^tρ=L(t)`, independently of `P`.
The proof does not bound `w_0` or `G`. If `g=||G||F`, the backward field
has the coordinate bound

\[
|(G^{\mathsf T}\delta_a)_i|
 +\left|\frac2{mL}\sum_j(2j+1)(B_jV_j)_i\right|
\le C\sqrt{k}\,g+2P^2ABC.
\]

Consequently

\[
\sup_{t\le T}\|w(t,\xi)-w_0(\xi)\|_F
\le 2THC\bigl(kg+2\sqrt{k}P^2AB\bigr)
\le M_T(1+g).
\tag{6}
\]

Use the radial matrix cutoff

\[
G_R=\min(1,R/\|G\|_F)G
\]

with its continuous value at zero. This is the Euclidean projection onto
the Frobenius ball, is 1-Lipschitz, and remains full rank almost surely.
It is a changed initialization law, whose error will be removed below.

To define `F_R^*`, replace `G` by `G_R` and replace every occurrence of
`c,A,B,L` in the right side and moment fields by their coordinatewise
clipping to the intervals in (5). Leave `w` unclipped. This includes clipping
the memory coordinates in the damping terms. These substitutions give a
globally bounded, globally Lipschitz map on

\[
\mathcal H=L^2(\gamma_s;\mathbb R^D)\times\mathbb R,
\]

with a bound `K_R<=K_0(1+R^2)`, where `K_0` is a finite computable function
of `k,m,P,T` and the bounded data. To check this, tanh and its first two
derivatives are bounded, clipping is 1-Lipschitz, moment integrands have
bounded factors, expectation has `L^2→R` norm one, and the only quadratic
matrix factor comes from the forward/transpose pair in `F_w`. The
unclipped `w` occurs only through tanh or its derivative. All constants
can therefore be bounded by the finite compositions in (1).

For a bounded matrix law, the exact solution stays in (5), so this
extension agrees with the original equations along the entire exact
trajectory. Global Picard iteration for the Lipschitz extension gives the
solution; (4)-(5) verify that it solves the original equations. The
extension is needed because polynomial projection need not preserve the
pointwise bounds in (5).

## Galerkin convergence for each matrix cutoff

Let `Z_R=(X_R,L_R)` denote the exact solution with `G_R`, and let `Π_J`
project the first component of `H` onto Hermites of degree at most `J`,
leaving `L` unchanged. Equation (2) is a finite globally Lipschitz ODE.
Subtracting its equation from the exact one and applying the Lipschitz
bound yields

\[
\sup_{t\le T}\|Z_{R,J}(t)-Z_R(t)\|_{\mathcal H}
\le e^{K_RT}\left[
\|(I-\Pi_J)Z_0\|_{\mathcal H}
+\int_0^T\|(I-\Pi_J)F_R^*(Z_R(t))\|_{\mathcal H}\,dt\right].
\tag{7}
\]

Hermite completeness and dominated convergence already make the right side
tend to zero. A quantitative bound is also available. For a Gaussian
Sobolev function `v`, orthogonality and
`∂_i Ψ_α=sqrt(α_i) Ψ_(α-e_i)` give

\[
\|(I-\Pi_J)v\|_2^2
\le\frac1{J+1}\mathbb E\|\nabla_\xi v\|^2.
\tag{8}
\]

This follows first for polynomials by summing their coefficients, and
extends to Gaussian `W^{1,2}` by approximation. The initial map `X_0`
has bounded label derivatives. At fixed moment history, the local vector
field is Lipschitz in `X` with constant at most `K_0(1+R^2)` and in its
matrix label with a bound at most `K_1(1+R)`. The 1-Lipschitz matrix cutoff
therefore gives, by a difference quotient and Gronwall,

\[
\sup_{t\le T}\|\nabla_\xi X_R(t)\|_2
\le [M_0+K_1(1+R)T]e^{K_0(1+R^2)T}.
\]

When differentiating in the label argument, the common moment history is
constant with respect to that argument. Its dependence on time does not
add a label derivative. Applying the chain rule also bounds the label
gradient of `F_R^*(Z_R(t))`. Equations (7)-(8), with polynomial factors in
`R` absorbed into an exponential, imply

\[
\sup_{t\le T}\|Z_{R,J}(t)-Z_R(t)\|_{\mathcal H}
\le C_T e^{b_T R^2}(J+1)^{-1/2},\qquad R\ge1.
\tag{9}
\]

Here and below constants can depend on `k,m,P,T` and data but never on
ambient network width. Clipped output evaluation from the coefficient
state satisfies the same form of bound, uniformly over `|u|<=1`, because
its Lipschitz constant is at most a constant times `1+R`.

## Removing the Gaussian cutoff on every finite horizon

This is the part not supplied by the one-shot cutoff estimate in the
earlier route note. Couple every cutoff using the same Gaussian labels.
For `S>=R`, write `e(t,ξ)=|X_R-X_S|` in a fixed Euclidean block norm, and

\[
D(t)=\mathbb E[(1+g)e(t,\xi)]+|L_R-L_S|.
\]

The bounds above give the uniform envelope

\[
e(t,\xi)\le M_T(1+g),\qquad D(t)\le M'_T.
\tag{10}
\]

The initial `w_0` cancels in this difference. Directly subtract the causal
fields in the order `S,f,V`. Bounded factors and tanh's Lipschitz
derivative give a field difference bounded by
`C_T[D(t)+E(g 1_{g>R})]`. Subtracting the local equations then gives

\[
D^+e(t,\xi)\le C_0(1+g^2)e(t,\xi)
 +C_0(1+g)D(t)
 +C_0(1+g^2)\mathbf1_{\{g>R\}},
\tag{11}
\]

and
`|dot L_R-dot L_S|<=C_0[D+E(g 1_{g>R})]`.
The two powers of `g` in (11) are the forward and transpose uses of the
same matrix. All these constants are independent of `R,S,w_0`.
At fixed `k,m,T` and data, `C_0` can be chosen polynomial in `P`: (4a)
keeps the reachable coordinate bounds independent of `P`, and the only
remaining dependence comes from finite-dimensional norm factors and sums
of the polynomial weights `2j+1` and the triangular memory coefficients.
This does not make the final rate uniform or polynomial in `P`.

For this Gaussian block law the elementary Gaussian integral gives

\[
\mathbb E e^{a g^2}=(1-2a/k)^{-k^2/2},\qquad 0\le a<k/2.
\tag{12}
\]

Choose a fixed short interval length `δ>0` with
`2 C_0 δ<k/8`; reduce it to at most one if needed. For an interval
starting at `t_0`, the pointwise variation-of-constants inequality from
(11) contains the initial term `exp(C_0δ(1+g^2))e(t_0,ξ)`. Cauchy-Schwarz
and (10) show that its weighted expectation is at most

\[
\begin{aligned}
&\mathbb E[(1+g)e^{C_0\delta(1+g^2)}e(t_0,\xi)]\\
&\quad\le D(t_0)^{1/2}
\left(M_T\mathbb E[(1+g)^2e^{2C_0\delta(1+g^2)}]\right)^{1/2}
\le C\sqrt{D(t_0)}.
\end{aligned}
\tag{13}
\]

The forcing kernel's weighted expectation is finite by (12). The tail
forcing is at most `C exp(-cR^2)` for some `c>0`: multiply its integrand
by `exp(cg^2-cR^2)` on `g>R` and choose, for example, `c=k/8` with the
above strict choice of `δ`. Polynomial factors in `g` are integrable
under the remaining Gaussian exponential margin. Gronwall on this
short interval consequently gives

\[
\sup_{t_0\le t\le t_0+\delta}D(t)
\le C[\sqrt{D(t_0)}+e^{-cR^2}].
\tag{14}
\]

The same estimate holds with the expectation of the within-interval
supremum of the state difference. Starting from identical initial data
and iterating for `N=ceil(T/δ)` intervals yields

\[
\sup_{t\le T}D(t)\le C_T e^{-a_T R^2},\qquad
a_T=c\,2^{-(N-1)}>0.
\tag{15}
\]

The constants may be extremely poor. To verify the iteration, a recurrence
`d_{j+1}<=C(sqrt(d_j)+η)`, `d_0=0`, is bounded by
`A η^(2^{-(j-1)})` for `j>=1`, `η<=1`, and sufficiently large fixed `A`.

Equation (15) makes the cutoff solutions Cauchy on every compact time
interval. The within-interval supremum version gives a subsequence
converging uniformly in time for almost every label. Equations (5)-(6)
supply integrable envelopes for all fields and local integral equations,
so dominated convergence identifies the limit with the untruncated
Gaussian population equations. This proves existence without assuming a
Gaussian population solution in advance.

For uniqueness, compare two solutions of the untruncated equation with
the same initial labels. On an interval whose initial difference is zero,
the tail forcing in (11) is absent. Integrating the variation-of-constants
bound using (12) gives `D(t)<=C∫_(t0)^t D(s) ds`, hence `D=0` on the
interval. Repeating the same short intervals proves uniqueness for all
`t<=T`. It is not necessary for `E exp(C_0 T g^2)` to exist.

The causal output comparison uses only `|u|<=1`, not an input net.
Therefore (15) also gives

\[
\sup_{t\le T,\ |u|\le1}|f_R(t,u)-f(t,u)|
\le C_T e^{-a_T R^2}.
\tag{16}
\]

Combining (9) and (16) proves the unconditional fixed-block estimate

\[
\sup_{t\le T,\ |u|\le1}|f_{R,J}(t,u)-f(t,u)|
\le C_T\left[e^{-a_T R^2}
 +e^{b_T R^2}(J+1)^{-1/2}\right].
\tag{17}
\]

For sufficiently large `J`, choose
`R^2=log(J+1)/(2(a_T+b_T))`. Both terms are then bounded by
`C_T(J+1)^(-θ_T)`, where

\[
\theta_T=\frac{a_T}{2(a_T+b_T)}>0.
\tag{18}
\]

This establishes finite-horizon convergence of a regularized coefficient
hierarchy for genuinely Gaussian blocks, not merely a theorem conditional
on bounded block matrices. It does not prove convergence of raw,
unregularized Hermite Galerkin truncations.

## Computability, mechanism, and limits of the result

The right side of (2) consists of finite-dimensional Gaussian integrals of
explicit elementary functions and known polynomials. These are not
unspecified law-function coordinates or future-trajectory oracles.
They can be evaluated to any prescribed tolerance using deterministic
quadrature: bound the Gaussian polynomial tails explicitly; on a compact
label box the integrand has a computable Lipschitz bound from the current
finite coefficients; a sufficiently fine tensor grid then has a certified
integration error. Numerical integration error in the ODE vector field is
an additional, separately controllable perturbation. Exact Gaussian
integration is not a constant-cost primitive in a computational claim.

Quadrature nodes are evaluation locations, not independent evolving
particles. At every node the state is reconstructed from the same finite
coefficient vector. The integrals can be refined without adding dynamic
coordinates. Replacing them by a single underresolved, square collocation
rule can collapse into a reparametrized particle method and must not be
confused with the convergent Gaussian-integral construction.

The frozen objects are the initial-label coordinates and their basis.
The functions `w_J(ξ),c_J(ξ),A_J(ξ),B_J(ξ)` evolve, and so do
`tanh(w_J(ξ)u)` and the complete second-layer features. No fixed-feature,
small-motion, Taylor-in-time, or future-trajectory approximation has been
introduced. The learned forward and transpose moment couplings retain
the unrestricted cross-block interactions already present at memory
order `P`. Equation (2) is autonomous and restartable from its current
coefficients and `L`; a previously chosen horizon-dependent clipping
level remains part of that ODE's fixed specification.

The cost is severe. At fixed label dimension,
`binom(s+J,J)~J^s/s!`; with `d=2`, `s=k^2+2k`. Thus the exponent in the
coefficient-count error rate is only `θ_T/s`, and deterministic
quadrature adds its own dimensional cost. The constants in (15) can
deteriorate exponentially under time-interval iteration, and no joint
polynomial bound in `k,m,P,T,1/ε` is asserted. A finite-horizon theorem
allows its chosen degree and cutoff to depend on the requested horizon;
the state dimension does not grow while the ODE runs. A uniform-in-all-time
guarantee with one fixed degree is not proved.

Finally, all of this approximates the fixed-`k`, fixed-`P` block population
law. It leaves untouched the separate large-block identification with
dense Gaussian training, the finite-width realization error, and the
memory-order limit. It is an aggregate solver above the existing closure,
not a resolution of those remaining identification questions. The proof
is internally derived and has not received an independent frozen-input
review or promotion approval.
