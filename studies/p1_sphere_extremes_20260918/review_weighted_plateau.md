# Independent audit of the initialized plateau and weighted architectural floor

Verdict: **PASS for the precisely stated claims in `plateau_construction.md`
and `architectural_loss_floor.md`.** No mathematical blocker was found.
This is an independent internal review, not promotion or a claim about a
finite neural network. The positive plateau is architectural
nonrealizability; it is not optimization failure on realizable data.

## Scope, isolation, and input identity

The neutral assignment required an analytic audit of the canonical
dimension-three, order-one population system, including its exact
initialization, all trainable blocks, physical factors, bounded ascent
clock, physical endpoint, hidden-block motion, terminal asymptotic, and
the complete weighted three-input architectural minimum. No experiment,
numerical integration, source search outside the assigned boundary, or
consultation with another reviewer was performed.

The complete assigned study inputs were read:

| Input | SHA-256 |
|---|---|
| `plateau_construction.md` | `bebcf883e62faad99051820596563dc5358a46dd920637460ad21793c1c1cc89` |
| `architectural_loss_floor.md` | `63cd366e6f1a89f4958fea9eb4901ac4fe295132783dc5759d69d07851415da4` |
| `initialization_positivity.md` | `73dae11c96755efd5e5362f879db9ca4197ddf0e3860434e939ecd529e0f55f5` |
| `protected_family.md` | `a7fb86719adaf96c3f3fc60a8e5f02618c4eb60aa32461cd7b1df77cd417178d` |
| `terminal_geometry.md` | `d9f0057e7a9709f8ec78f78a50b744ca870a479f59ce92625e9041456f46fcad` |

Established inputs were all of `docs/observable_p1.md` (SHA-256
`0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba`)
and exactly the equations/existence material in
`docs/global_nonlinear.md` C.4.7.9.3--4 and C.4.7.10.D.3.
The rigorous-mathematics and conjecture-investigation skills and their
research-contract/adversarial-audit references were read. No study README,
history, previous verdict, other study, or other route's findings were
read. The supporting candidates were read completely; the verdict concerns
the two assigned target statements and the lemmas they use, rather than
independently certifying every unrelated extension in those supporting files.
All six displayed file hashes were rechecked after the report was written
and remained unchanged.

## 1. Canonical system, full gradient, and exact symmetry

The prescribed lower joint law retains
`h=tanh G` and `k=tanh(sqrt(tau) Z+alpha h)` together. The reverse-response
term `tau gamma`, the ridge `eta=1/4096`, and the right Cholesky transpose
are all present in the two initialized bands of `D`. No Gaussian
independence substitution has been made for `G` and `k`.

The constant feature coordinates can be omitted on the initialized odd
mark sector for the exact reason given by the established source:
`w` and `c` are odd in their respective marks, the lower constant pairing
and upper constant reverse pairing vanish, and the constant matrix row
and column have zero velocity. This is invariant under the full vector
field. Every remaining entry of the `3 x 6` matrix is trained, and the
reverse contraction uses the actual `M^T`.

For a unit input `u`, direct differentiation in the population `L2` and
matrix Frobenius metrics yields

\[
 \nabla f(u)=
 \bigl(\operatorname{sech}^2(w\cdot u)
       (b_1^TM^Td(u))u,\ h(u),\ d(u)a(u)^T\bigr).
\]

These are exactly the source equations, with no extra population weight,
missing factor of two, or factor of `sqrt(3)`: the raw sphere inputs are
normalized before entering this formula.

Input oddness holds for every architecture state, including states outside
the initialized odd mark sector. For the proposed law, with
`b=1-2a>0`, `v=-e_2`, and `F=f(v)`, it gives the global identity

\[
 \mathcal L=2a+2a f(e_1)^2+b(1-F)^2.
\]

The reflection argument is exact. Under
`R=diag(-1,1,1)`, `R_1=diag(R,R)`, and the corresponding
measure-preserving mark involutions,

\[
 a_{\theta^R}(u)=R_1a_\theta(Ru),\qquad
 f_{\theta^R}(u)=f_\theta(Ru).
\]

The state transformation is an isometry, fixes `(g,0,D)`, and preserves
`F` because `Rv=v`. Local uniqueness therefore fixes the ascent trajectory
under that transformation. Consequently `f(e_1)=f(-e_1)=0` along it.
The derivative of `2a f(e_1)^2` vanishes in every full-state direction at
these states. The actual physical vector field there is exactly

\[
 \theta_t=2b(1-F)\nabla F.
\]

This reduction follows from the unrestricted gradient and uniqueness; it
does not replace the full system by a projected or frozen-feature model.

## 2. Initial activity, ascent-clock existence, and level-one crossing

At the axis input, the only two active lower coefficients are the signed
versions of `nu/a_0` and `beta eta/((nu+eta)b_0)`. Thus

\[
 Da(v)=\ell v,\qquad
 \ell=d_h\nu/a_0+d_k\beta\eta/((\nu+\eta)b_0)>0.
\]

Positivity of `beta` is justified by conditioning on `h`: the conditional
mean of `k` is odd and strictly increasing and therefore has the strict
sign of `h`. The remaining factors are positive in the exact canonical
initialization. The upper coordinate `b_2 dot v` is nondegenerate, so

\[
 k=E_2\tanh^2(\ell b_2\cdot v)>0.
\]

The nonreadout gradient blocks vanish at zero because `c(0)=0`, giving
`||grad F(theta_0)||^2=k` without any approximation.

For the ascent equation `theta_s=grad F`, the bounded feature envelopes
`L_j=ess sup |b_j|`, `A=L_1L_2`, and `D_0=||D||_F` give

\[
 \|c(s)\|_\infty\le s,\quad
 \|M(s)\|_F\le D_0+As^2/2,\quad
 \|w(s)-g\|_\infty\le AD_0s^2/2+A^2s^4/8.
\]

The last bound follows by integrating
`||w_s||_infinity <= As(D_0+As^2/2)`; its factors and powers are correct.
On each bounded set the vector field is locally Lipschitz in the affine
Banach space of bounded `w-g`, bounded `c`, and finite `M`, because all
features and all required derivatives of tanh are bounded. The fixed
unbounded Gaussian `g` appears only inside those gates. The contraction
argument in the assigned existence source thus applies unchanged to
this ascent vector field. These polynomial bounds and bounded velocities
produce a Cauchy endpoint at every prospective finite maximal clock, where
local existence restarts the solution. This proves existence for every
finite `s`, not only a conditional estimate before an unproved endpoint.

Writing `C_0=||c||_2^2` and `kappa=||grad F||^2`, differentiation gives

\[
 F_s=\kappa\ge\|h\|_2^2,\quad (C_0)_s=2F,
 \quad F^2\le C_0\|h\|_2^2.
\]

The initial expansions imply `F=ks+o(s)` and
`C_0=ks^2+o(s^2)`. Positivity then persists by the displayed derivative
identities. For every positive clock,

\[
 (F^2/C_0)_s=2F(C_0\kappa-F^2)/C_0^2\ge0.
\]

Its initial limit is `k`, so `kappa>=k` and `F(s)>=ks`. There is therefore
a unique finite `s_*>0` with `F(s_*)=1`, and `s_*<=1/k`. This step supplies
both existence of the fitted scalar endpoint and its nondegeneracy
`kappa_*>=k`; neither is inferred from a stationary-state ansatz.

## 3. Physical-time convergence, strict descent, and tail

The scalar equation `s'=2b(1-F(s))` is locally Lipschitz. It increases from
zero, cannot reach its equilibrium `s_*` at finite time by uniqueness,
and cannot converge to a smaller clock because its speed would then have
a positive lower bound. Thus `s(t)` exists for all nonnegative physical
time and increases to `s_*`. The composed state solves the full physical
equations and is their canonical solution by uniqueness.

For `E=L-2a=b(1-F)^2`, the factors are

\[
 E'=-4b\kappa(s(t))E,
 \quad E(0)=b,
 \quad 0<E(t)\le b e^{-4bkt}.
\]

Consequently the physical loss decreases strictly at every finite time,
`L'(0)=-4b^2 k`, and the attained limiting value is exactly `2a`.
At `a=1/4`, the three inputs are distinct, all weights are positive,
the two label masses are both `1/2`, and

\[
 \mathcal L(0)=1,\qquad \mathcal L'(0)=-k,\qquad
 \mathcal L_\infty=1/2,\qquad
 0<\mathcal L(t)-1/2\le\tfrac12e^{-2kt}.
\]

The endpoint is bounded in the asserted norms for `w-g`, `c`, and `M`;
it also has finite Hilbert state norm. This does not assert that the
Gaussian-based field `w` itself has finite essential supremum.

Smoothness on the bounded finite-clock interval gives

\[
 1-F(s)=\kappa_*(s_*-s)+O((s_*-s)^2),\qquad
 |\kappa(s)-\kappa_*|=O(s_*-s).
\]

The change of variables `dt=ds/[2b(1-F)]` then proves absolute integrability
of `kappa(s(t))-kappa_*` on the infinite physical interval. Solving the
residual equation exactly therefore gives a finite positive constant

\[
 C=\exp\left[-2b\int_0^\infty(\kappa(s(t))-\kappa_*)\,dt\right]
\]

and the claimed asymptotic

\[
 \mathcal L(t)=2a+bC^2e^{-4b\kappa_*t}(1+o(1)).
\]

Bounded ascent speed and the endpoint expansion also justify convergence
of the complete moving state at rate `O(exp(-2b kappa_* t))` in the
stated norms. No uncontrolled limit exchange or implicit compactness
claim is needed.

## 4. Both hidden blocks move before the endpoint

The sign reflections of coordinates one and three both fix the active
input `v=-e_2`, the initialization, and `F`. The same uniqueness argument
used above forces `Ma(v)=rho v`. Starting at `rho(0)=ell>0`, the readout is

\[
 c(s,B)=\int_0^s\tanh(\rho(\sigma)B)\,d\sigma,
 \qquad B=b_2\cdot v.
\]

It depends only on `B`; independence and centering of the other upper
coordinates give `d=delta v`. While `rho>0`, the readout has the strict
sign of `B` at positive clock, hence

\[
 \delta=E_2[Bc\operatorname{sech}^2(\rho B)]>0.
\]

Direct use of the full gradients gives

\[
 a_s=SM^Td,\quad M_s=da^T,\quad
 S=E_1[b_1b_1^T\operatorname{sech}^4(w\cdot v)]\succeq0,
\]
\[
 \rho_s=\delta(\|a\|^2+v^TMSM^Tv)\ge0.
\]

This prevents a first zero of `rho` and closes the sign argument. In
particular `rho>=ell`, `a!=0`, and `M_s!=0` at every positive clock.

The lower Gram is positive definite: each pair `(h,k)` has no nontrivial
almost-sure linear relation because `k` has positive conditional variance
given `G`; different pairs are independent and centered; the normalization
is invertible. Since `rho>0` forces `M^Tv!=0`, the reverse field
`q=delta b_1^TM^Tv` is nonzero in `L2`. The lower gate is strictly positive
almost surely at finite states, so `w_s!=0` as well. Positive physical
clock speed transfers both assertions to every finite `t>0`. Their zero
velocities exactly at initialization are correctly acknowledged.

## 5. Initialization certificate and strict monotonicity of T

The weighted expressivity proof uses the full conditional coefficient
`Psi`, not merely its positive first term. The independent checks of its
sign certificate are:

1. Conditioning gives `0<beta<=alpha nu`.
2. Gaussian integration by parts and Cauchy--Schwarz on
   `k-(beta/nu)h` give `b_0^2>=tau gamma^2+eta`.
3. Hence `0<B_*=c_*d_k/b_0<=1/gamma`.
4. Integrating `sech^2 z>=1-z^2` yields
   `K(h)/h>=alpha^2(1-alpha/3)=m<alpha` on `0<h<=1`.
   Multiplying the negative quantity `m-alpha` by the upper bound for
   `B_*` has exactly the inequality direction used in the candidate.
5. The analytic bounds `nu<3/7`, `alpha>11/15`,
   `eta/(nu+eta)<1/65`, and `gamma>=alpha-alpha^2 nu` give

\[
 \frac{c_*\Psi(h)}h\ge
 \frac\alpha\gamma\left(\frac7{15}-\frac{1936}{4725}-\frac1{65}\right)
 =\frac\alpha\gamma\frac{2552}{61425}>0.
\]

The Gaussian boundary terms vanish, the variables used for integration
by parts are the independent canonical reverse variables, and the
positive ridge is retained throughout. This establishes the required
strict sign without quadrature.

For `g>0` and `0<=r<1`, putting
`Y=rg+sqrt(1-r^2)V` gives

\[
 \partial_r m_r(g)
 =gE\phi'(Y)-rE\phi''(Y)
 =gE\phi'(Y)+2rE[\phi(Y)\phi'(Y)]>0.
\]

The Gaussian integration-by-parts factor is correct. When `r>0`, pairing
positive and negative values of `Y` shows that the last expectation is
positive: `phi(z)phi'(z)` is odd and positive for positive `z`, and a
Gaussian with positive mean has strictly greater density at `z` than at
`-z`. At `r=0`, the first term alone is positive. Differentiation is valid
on compact subintervals of `(-1,1)`; after integration by parts its bound
is at most `|g|+2`, up to the bounded `Psi` factor in the outer integral.

Oddness in `g` and the strict sign of `Psi(phi(g))` therefore give
`T'(r)>0` for `0<=r<1`. Oddness of `T` supplies strict increase on the
negative half, and continuity by dominated convergence extends strict
increase to both endpoints. Thus `T` is injective on the entire closed
interval, not merely nonzero away from zero. Coordinatewise application
proves

\[
 Da_0(x)=\pm Da_0(x')\quad\Longleftrightarrow\quad x=\pm x'
\]

with the same selected sign, and the initialized vector never vanishes
on the sphere.

## 6. Complete weighted three-input minimum and initial stationarity

After removing zero weights, choose one representative per input class
modulo sign. There are at most three classes. Their initialized vectors
are nonzero and distinct modulo sign by the preceding injectivity result.
The upper mark law has positive density on an open cube about zero.
Consequently an almost-sure linear relation among the corresponding
features `H_G=tanh(b_2 dot z_G)` is a continuous identity there.

Choose a direction whose inner products `t_G` are nonzero with distinct
squares; the excluded set is a finite union of proper hyperplanes.
Restriction to a short line in that direction and the nonzero first,
third, and fifth tanh coefficients give the Vandermonde system
`sum_G A_G t_G^(2n+1)=0`, `0<=n<m<=3`. Its determinant is a nonzero
multiple of `prod_G t_G prod_{G<H}(t_H^2-t_G^2)`. Thus the features are
linearly independent and their Gram matrix `K` is positive definite.

For any prescribed real vector of class predictions `m`, the bounded
readout `c=sum_G (K^{-1}m)_G H_G`, with exactly `w=g` and `M=D`, attains
those predictions. It belongs to the same odd mark sector. This is a
valid expressivity construction and makes no assertion that the physical
trajectory freezes its hidden blocks or reaches that particular state.

Writing `x_i=sigma_i v_G`, the definitions

\[
 W_G=\sum_{i\in G}p_i>0,\qquad
 m_G=W_G^{-1}\sum_{i\in G}p_i\sigma_i y_i
\]

give, by direct completion of the square,

\[
 \mathcal L(\theta)=\sum_G W_G(1-m_G^2)
       +\sum_G W_G(f_\theta(v_G)-m_G)^2.
\]

The constructed readout attains all class means simultaneously, proving
that the first sum is the exact attained global minimum. Since the
averaged variables `sigma_i y_i` take only the values `+/-1`, a class
contributes zero precisely when those variables agree on every active
atom. This proves the complete stated compatibility condition, including
repeated points, antipodal points, arbitrary positive unequal weights,
and removal of zero-weight atoms. In particular input linear dependence
alone is no expressivity obstruction for at most three active classes.

The independent-input realizability construction in Section 6 of the
plateau candidate also checks: positive definiteness of the gated lower
Gram gives local surjectivity, independent targets can be chosen in the
open images, a finite `M` maps them to the coordinate vectors, and the
independent centered upper features admit the stated bounded readout.
The weighted theorem proves the stronger conclusion using the original
hidden coordinates directly.

Finally the full initial loss derivative is

\[
 \mathcal L'(0)=-4\left\|\sum_G W_Gm_GH_G\right\|_2^2.
\]

Feature independence proves that it vanishes exactly when every
`m_G=0`, equivalently when the architectural minimum is one. All three
velocities then vanish and local uniqueness makes initialization
stationary forever. Every law with architectural minimum below one has
strict initial descent. The proof controls the complete nonlinear
initialized feature family; cancellation of only the first input moment
does not establish stationarity.

## 7. Adversarial interpretation and remaining open claim

| Possible obstruction or alternative | Audit conclusion |
|---|---|
| Initialization, ridge, reverse-response, transpose, or physical scaling changed | Ruled out by direct comparison with the established formulas. |
| Scalar reduction silently freezes hidden parameters | Ruled out: the full gradient induces the reduction and both hidden velocities are nonzero for finite positive time. |
| A lower bound is mistaken for the actual limiting loss | Ruled out: finite ascent-clock crossing and the unique physical clock prove attainment in the limit. |
| Feature clock escapes or the limiting state is only formal | Ruled out by explicit bounds and continuation in the declared norms. |
| Only an exponential upper bound, not an asymptotic equivalent, is proved | Ruled out by absolute integrability of the terminal rate correction. |
| Finite dictionary creates additional three-input collisions or dependencies | Ruled out at initialization by strict `T` injectivity and the three-feature Vandermonde argument. |
| Positive limiting loss proves failure to optimize a realizable dataset | False interpretation: the pair of equally labelled antipodes imposes exactly the attained positive architectural floor. |
| Architectural realizability proves all compatible laws are learned from initialization | Unsupported; neither reviewed statement makes this inference. |

The plateau example has three distinct inputs and balanced label mass
at `a=1/4`, but its directions span only a plane and its antipodal labels
are incompatible with every odd predictor. The weighted formula identifies
this as a global architectural minimum. The remaining question of a
positive initialized limiting loss above that minimum on compatible,
realizable data is open in these inputs. This limitation is explicit and
does not block either reviewed claim.

No required repair or blocking omission was found. The review does not
authorize promotion and does not extend these exact population results
to finite quadrature, finite neural width, higher closure order, or a
trained-network limit.
