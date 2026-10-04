# Exact polynomial input compression, uniformly in width and time

This supplement checks Sections 1--4 and 8 of this study's `RESULT.md` and proves the polynomial corollary requested by the supervisor. It uses only that assigned material and the cubature argument already derived in `CUBATURE_ROUTE.md`. It is an internal theoretical check, not an independent promotion review. No shared source was edited and no experiment was run.

The corollary is stronger than finite-horizon approximation: one positive cubature, chosen independently of width, initialization, temporal order, and time, preserves every dense polynomial-network gradient field and loss exactly. The dense flows exist globally, so their equality holds for all time. It also preserves the specified finite-order response-memory closure on every common interval of existence. Global existence of that closure is a separate claim and is not needed here.

## 1. Architecture, degree, and one universal data summary

Fix integers `s>=1`, `L>=1`, and `b>=1`, an affine input chart

\[
x=\chi(u)=Mu+c,\qquad u\in K=[-1,1]^s,
\]

and polynomial hidden activations of degree at most `b`. Different layers or neurons may use different such polynomials. For every finite width `n>=1`, retain the architecture and normalizations in `RESULT.md`:

\[
z^{(1)}=W^{(1)}x/\sqrt d,\qquad
h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad
z^{(\ell)}=W^{(\ell)}h^{(\ell-1)}\ (\ell\ge2),\qquad
f_\theta=w^Th^{(L)}/n.
\tag{P1}
\]

The activation is applied coordinatewise. Parameter values are unrestricted real numbers. Adding trained affine biases does not increase any degree bound below, although (P1) is the architecture explicitly under discussion.

Write

\[
d_*=b^L,\qquad
N_a=\binom{s+a}{s}.
\]

Let `pi` be any probability law on `K x R` with `E_pi y^2<infinity`. There is one positive weighted law

\[
\pi_* = \sum_{j=1}^{K_*}a_j\delta_{(u_j,y_j)},
\qquad a_j>0,\qquad \sum_j a_j=1,
\qquad K_*\le N_{2d_*}+N_{d_*}+1,
\tag{P2}
\]

such that

\[
\begin{aligned}
\int u^\alpha\,d\pi_*&=\int u^\alpha\,d\pi
&&(|\alpha|_1\le2d_*),\\
\int yu^\alpha\,d\pi_*&=\int yu^\alpha\,d\pi
&&(|\alpha|_1\le d_*),\\
\int y^2\,d\pi_*&=\int y^2\,d\pi.
\end{aligned}
\tag{P3}
\]

These are total-degree moments. For a finite original dataset, the nodes can be selected from it, with `K_*` additionally bounded by its size. For a continuum law, nodes may be selected from any specified probability-one subset, including a probability-one subset of the topological support. The retained labels need not be bounded, but every retained label is a finite real number and their weighted second moment is preserved.

To see the count, use the `r=N_{2d_*}+N_{d_*}+1` features appearing in (P3). All are integrable, and one is the constant `1`. The integrable-barycenter lemma proved in `CUBATURE_ROUTE.md` puts their expectation in the finite convex hull of their actual full-measure range. The constant coordinate bounds the affine dimension by `r-1`. Any representation with more than `r` positive weights has a linear dependence among its feature columns; its coefficients sum to zero. Moving the weights along this dependence until the first reaches zero removes a node while preserving every feature. Iteration gives (P2). For finite data, this elimination is a direct exact-arithmetic construction from the input moments; it never uses training.

The feature list depends on `s,L,b` and the data law, not on `n`, parameter initialization, a temporal order `q`, or a horizon. Consequently the **same** `pi_*` satisfies all the conclusions below simultaneously for every such choice. In fact the chosen moments also work for every affine chart and every activation of degree at most `b` within the stated architecture class, using the same latent coordinates `u`.

This support bound is an upper bound, not a claim of a universal minimum. An informative necessary lower bound is also available. Let `v_{d_*}(u)` be the vector of all monomials of total degree at most `d_*`, and set

\[
G=\mathbb E_\pi\left[
\begin{pmatrix}v_{d_*}(u)\\y\end{pmatrix}
\begin{pmatrix}v_{d_*}(u)\\y\end{pmatrix}^{\!T}
\right].
\]

Every entry of `G` is matched by (P3). Since a measure with `K_*` nodes represents `G` as a sum of `K_*` rank-one positive semidefinite matrices,

\[
K_*\ge\operatorname{rank}G.
\tag{P4}
\]

For example, if the input polynomial Gram matrix is positive definite, this lower bound is at least `N_{d_*}`; it is `N_{d_*}+1` if `y` is not equal almost surely to a polynomial of degree at most `d_*`. In degenerate cases one node can suffice. There is no uniform positive lower bound on the individual cubature weights.

## 2. Exact dense field, exact loss, and global trajectories

Since the input chart is affine, `deg_u z^(1)<=1`. Composition with a degree-`b` polynomial multiplies the degree by at most `b`, while matrix multiplication does not increase it. Induction gives

\[
\deg_u h^{(\ell)}\le b^\ell,
\qquad
\deg_u f_\theta\le d_*.
\tag{P5}
\]

More explicitly, `f_theta(u)=sum_{|alpha|<=d_*}c_alpha(theta)u^alpha`, where the coefficients are polynomials in the parameters. Differentiating a coefficient in a parameter does not alter its monomial in `u`. Therefore

\[
\deg_u\nabla_\theta f_\theta\le d_*,\qquad
\deg_u(f_\theta\nabla_\theta f_\theta)\le2d_*.
\tag{P6}
\]

The moments (P3) imply, for every parameter value and every width,

\[
\mathcal L_{\pi_*}(\theta)=\mathcal L_\pi(\theta),
\qquad
F_{\pi_*}(\theta)=F_\pi(\theta),
\tag{P7}
\]

where the loss and field have exactly the convention of `RESULT.md`,

\[
\mathcal L_\mu(\theta)=\mathbb E_\mu(f_\theta-y)^2,
\qquad
F_\mu(\theta)=-2D\mathbb E_\mu[(f_\theta-y)\nabla_\theta f_\theta].
\]

Equality of losses uses the unlabeled degree-`2d_*` moments, label-weighted degree-`d_*` moments, and `E y^2`; equality of gradient fields uses the first two families. Both assertions are identities on the entire parameter space. Thus there is no approximation residual or compact-parameter restriction.

For completeness, these dense flows exist globally. Their vector fields are polynomial in the finite parameter vector, hence locally Lipschitz. For `v=D^{-1/2}theta`, gradient flow satisfies

\[
\dot{\mathcal L}_\mu=-\|\dot v\|^2,
\qquad
\|v(t)-v(0)\|\le\sqrt{t\mathcal L_\mu(\theta_0)}.
\tag{P8}
\]

The loss is finite for each finite parameter vector because `K` is compact and `E y^2<infinity`. It is nonnegative because the law is positive. If a maximal solution had finite lifetime `T_max`, (P8) would bound its parameters, and for `0<=a<t<T_max`,

\[
\|v(t)-v(a)\|
\le\sqrt{(t-a)\mathcal L_\mu(\theta_0)}.
\]

This gives a finite terminal limit as `t` tends to `T_max`. Local existence at that limit extends the solution, a contradiction. No coercivity of the polynomial loss is needed.

For every width and every common initialization, uniqueness and (P7) now give

\[
\theta_{\pi_*}(t)=\theta_\pi(t),\qquad
f_{\theta_{\pi_*}(t)}(\chi(u))=f_{\theta_\pi(t)}(\chi(u))
\qquad(t\ge0,\ u\in K).
\tag{P9}
\]

The equality holds on all inputs on which the same network is evaluated, since the parameter vectors coincide. It is exact uniformly in width and time in the following precise sense: one fixed `pi_*` works for each finite width, and each paired trajectory has zero difference at every time. It does not assert a shared bound on the size of those trajectories across widths or time, and it does not reduce their parameter dimension.

## 3. Backpropagation and response-field degree accounting

Use the residual-free backpropagation fields defined in Section 2 of `RESULT.md`:

\[
\delta^{(L)}=w\odot\phi_L'(z^{(L)}),\qquad
\delta^{(\ell)}=\phi_\ell'(z^{(\ell)})\odot
     (W^{(\ell+1)})^T\delta^{(\ell+1)}.
\]

The derivative of a degree-`b` activation has degree at most `b-1`. Because `deg_u z^(ell)<=b^(ell-1)`,

\[
\deg_u\phi_\ell'(z^{(\ell)})
\le(b-1)b^{\ell-1}=b^\ell-b^{\ell-1}.
\]

Multiplying the derivative factors from layer `ell` through layer `L` gives the telescoping sum

\[
\deg_u\delta^{(\ell)}
\le\sum_{j=\ell}^L(b^j-b^{j-1})
=d_*-b^{\ell-1}.
\tag{P10}
\]

For `b=1`, all these derivative degrees are zero; the formula remains valid. Zero polynomials and cancellations can make every stated bound smaller.

For any finite order `q>=1`, the response fields satisfy

\[
\begin{aligned}
\dot H_k^{(\ell)}
 &=\rho h^{(\ell)}-(\rho/\tau)(\mathcal T H^{(\ell)})_k,\\
\dot A_k^{(\ell)}
 &=f\delta^{(\ell)}-(\rho/\tau)(\mathcal T A^{(\ell)})_k,\\
\dot C_k^{(\ell)}
 &=\delta^{(\ell)}-(\rho/\tau)(\mathcal T C^{(\ell)})_k,
\end{aligned}
\tag{P11}
\]

where `rho=sqrt(loss)`, `tau'=rho`, `tau(0)=1`, and

\[
(\mathcal T U)_k=kU_k+\sum_{j<k}(2j+1)U_j.
\]

The damping acts only on the temporal index and has scalar coefficients independent of input. Consequently it cannot increase input polynomial degree. The initial data are `H_0^(ell)=h^(ell)(0)`, `H_k^(ell)=0` for `k>0`, and `A_k^(ell)=C_k^(ell)=0`. Equations (P5), (P10), and (P11) then give the invariant finite polynomial spaces

\[
\begin{array}{c|c}
\text{field}&\text{upper bound on total input degree}\\ \hline
H_k^{(\ell)}&b^\ell\\
\delta^{(\ell)}&d_*-b^{\ell-1}\\
A_k^{(\ell)}&2d_*-b^{\ell-1}\\
C_k^{(\ell)}&d_*-b^{\ell-1}.
\end{array}
\tag{P12}
\]

These statements can also be checked coefficient by coefficient: every monomial above the displayed degree has zero initial coefficient, zero forcing, and a homogeneous finite linear equation in its temporal-index coefficients, so it remains zero.

For internal layers `ell>=2`, the reconstructed weight matrix uses the pairings

\[
\int A_k^{(\ell)}(H_k^{(\ell-1)})^T\,d\mu,
\qquad
\int C_k^{(\ell)}(H_k^{(\ell-1)})^T\,d\nu.
\]

Their input degrees are at most

\[
(2d_*-b^{\ell-1})+b^{\ell-1}=2d_*,
\qquad
(d_*-b^{\ell-1})+b^{\ell-1}=d_*.
\tag{P13}
\]

Thus the internal reconstructions are exactly preserved by (P3), for arbitrary values of their allowed coefficient fields, not only along a particular realized trajectory.

The first-layer gradient needs its input factor; omitting that factor would undercount its degree. In the normalization (P1), the parameter derivatives are

\[
\nabla_{W^{(1)}}f
 =\frac1{n\sqrt d}\delta^{(1)}\chi(u)^T,
\quad
\nabla_{W^{(\ell)}}f
 =\frac1n\delta^{(\ell)}(h^{(\ell-1)})^T\ (\ell\ge2),
\quad
\nabla_w f=\frac1n h^{(L)}.
\tag{P14}
\]

For the first expression, `deg delta^(1)<=d_*-1` and `deg chi<=1`, so its degree is at most `d_*`. Multiplying by `f` requires unlabeled degree at most `2d_*`, and multiplying by `y` requires label-weighted degree at most `d_*`. The readout expression has exactly the same upper requirements. Hence the prescribed dense first-layer and readout updates also use only (P3).

Finally, `B_k=A_k-y C_k` remains an exact separation even with irregular or noisy labels. Degree bounds are imposed on its two input-only fields; no polynomial representation of the label function is being assumed.

## 4. Equality of the finite-order memory closures

Fix any width, initialization, and finite `q`. Expand the polynomial fields in (P12) in complete monomial bases of their stated degrees. Together with the directly evolved first-layer/readout parameters and `tau`, their coefficients form a finite state. The internal matrices are reconstructed from the pairings (P13) and the formula in Section 2 of `RESULT.md`.

For any such coefficient state with `tau>0`, every reconstructed internal matrix agrees under `pi` and `pi_*` by (P3). The resulting predictor therefore agrees as a polynomial in `u`. Its squared loss agrees by (P7), so its residual-RMS clock `rho` agrees. Equations (P11) and (P14) then give the same derivatives of every coefficient and directly evolved parameter. The initial coefficient state is also identical. Thus the two laws define the same finite state equation, not merely the same force at initialization.

The square root in the clock does not obstruct local uniqueness when loss is zero. For two parameter states in a compact set, the reverse triangle inequality in `L^2(mu)` gives

\[
|\rho(\theta)-\rho(\widetilde\theta)|
\le\|f_\theta-f_{\widetilde\theta}\|_{L^2(\mu)}
\le\sup_{u\in K}|f_\theta(u)-f_{\widetilde\theta}(u)|
\le C\|\theta-\widetilde\theta\|.
\tag{P15}
\]

The reconstruction is locally Lipschitz in the finite coefficients and `tau` when `tau>0`; all other operations in the coefficient equation are polynomial or locally Lipschitz compositions. Moreover `tau'=rho>=0` and `tau(0)=1`, so the evolving clock never reaches its singular denominator. The finite coefficient equation is therefore locally Lipschitz and has a unique maximal solution.

Evaluation of this polynomial-field solution at the original data or the cubature nodes satisfies exactly the corresponding atomwise memory equations. Conversely, an atomwise solution extends to the same input-polynomial fields by solving (P11) with its global weights and clock, so comparison via the coefficient equation does not impose extra input regularity on the labels or alter the original closure.

It follows that the order-`q` closures under `pi` and `pi_*` have identical reconstructed weights, directly trained weights, clock, and predictions throughout every common existence interval. If both are defined through this common coefficient system, they have the same maximal existence interval. No dependence of `pi_*` on `q` is needed.

The energy identity (P8) belongs to the dense gradient flow. It has not been established for this memory closure, whose internal weights are reconstructed from truncated histories. Polynomial activations are unbounded. Accordingly, the argument proves exact equality of the closures on their existence interval, but makes no unsupported assertion that every order-`q` polynomial memory closure exists globally.

## 5. Check of the assigned passages and suggested precise corollary

Sections 1--4 of `RESULT.md` are mathematically consistent under their stated tanh, compact-chart, finite-second-moment assumptions. The loss factor, canonical mobility, energy ball, positive support count, noncompact-label convexity argument, tensor Chebyshev tail, uniform vector-field residual, and Gronwall estimate have the correct factors and dependencies. The response split in Section 2 is exact for the stated scalar damping. This check does not independently rederive the separate temporal approximation theorem outside the assigned passages.

The degree formulas in Section 8 are correct as upper bounds. Its wording that pairings require “precisely” those degrees should be replaced by “at most”: special activations, zero parameters, symmetries, or cancellations can reduce them. Its exact-input statement can be strengthened to the following:

> For an affine input chart and polynomial activations of degree at most `b>=1` in `L>=1` hidden layers, set `d_*=b^L`. A single positive weighted dataset with at most `binom(s+2d_*,s)+binom(s+d_*,s)+1` nodes can match all unlabeled moments through total degree `2d_*`, all label-weighted moments through degree `d_*`, and the label second moment. Chosen independently of width, initialization, temporal order, and horizon, this same dataset preserves the entire canonical dense vector field and loss for every finite width and parameter value. The dense gradient flows are global and hence coincide for all time from each common initialization. It also preserves every finite-order response-memory closure exactly throughout each common existence interval. This is an exact data-compression result for polynomial networks; it does not replace the tanh model or establish global existence of its temporal closures.

The retained support size may grow very rapidly with depth through `b^L`; exactness removes dependence on width and time from the required input moment degrees, not dependence on input dimension, activation degree, or network depth. Processing an empirical dataset still requires reading it, and an abstract continuum law still requires effective moment/node access for computational construction.
