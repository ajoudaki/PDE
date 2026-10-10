# Residual directions, adaptive features, and the large-label obstruction

2026-10-10. Continuation of the same multi-input investigation. This note
establishes exact identities, a favorable local feature-learning effect,
and conditional nonperturbative fitting criteria. It does **not** establish
arbitrary-label Gaussian fitting or remove a hypothesis from a compression
theorem. No simulation or change of training dynamics is used.

## 1. Scope and normalization

Use the model of [LABEL_SCALE.md](LABEL_SCALE.md), Section 1: `m>=2` sphere
inputs, width `n`, fixed hidden depth `L>=2`, strip-analytic activations with
bounded derivatives (values need not be bounded), independent first Gaussian
weights of variance one and hidden Gaussian weights of variance `1/n`,
zero initial readout, mean loss, and mobilities `(n,1,...,1,n)`.
The target is every fixed finite label vector, not labels growing with width.

Let `H` be the `n by m` top-feature matrix, `w` the stored readout, and
\[
f=H^\top w/n,\quad r=f-y,\quad
\mathcal L=\|r\|_2^2/m,\quad Y=\|y\|_2/\sqrt m,\quad G=H^\top H/n.
\]
For all parameters `theta`, the mobility is the fixed positive matrix `M`.
In whitened coordinates `vartheta=M^(-1/2)theta`, let
\[
J=D_\vartheta f,\qquad K=JJ^\top,\qquad
\rho=\|r\|_2/\sqrt m,\qquad
\kappa=\frac{r^\top Kr}{m\|r\|_2^2}\quad(r\ne0).
\]
Here `K` is the **full** tangent Gram, with `K>=G` as positive-semidefinite
matrices. All time derivatives refer to physical training time. Exactly,
\[
\dot r=-2Kr/m,\qquad \dot\rho=-2\kappa\rho,\qquad
-\dot{\mathcal L}=\|\dot\theta\|_{M^{-1}}^2=4\kappa\rho^2.
\tag{D1}
\]
Global existence at every finite time, without a label restriction, was
proved in the companion note. The case `y=0` is the stationary zero predictor;
the remaining discussion assumes `y!=0` and nonzero initial gradient.

The actual fitting requirement is
\[
\rho(t)=Y\exp\left(-2\int_0^t\kappa(s)\,ds\right)\longrightarrow0.
\tag{D2}
\]
Thus divergence of this integral is necessary and sufficient. A positive
constant lower bound on `kappa` is sufficient but stronger. Nonvanishing
alone is insufficient: a strictly positive function may have finite integral.

Indeed the full gradient cannot become exactly zero at a finite time unless
it was zero initially. Otherwise smooth autonomous ODE uniqueness, backward
from that equilibrium and then along the earlier interval, would make the
earlier trajectory stationary too. The same observation excludes reaching
zero residual in finite time from nonzero residual. Hence `kappa(t)>0` at
every finite time along each nonstationary trajectory. The unresolved issue
is its tail, not exact finite-time avoidance of the full tangent nullspace.

## 2. Residual turning favors weak directions, not strong ones

Define the unit residual `u=r/||r||`. Differentiating its normalization in
(D1) gives
\[
\dot u=-\frac2m(K-m\kappa I)u.
\]
Differentiating `kappa=u^T K u/m` then gives the exact identity
\[
\dot\kappa=\frac1m u^\top\dot K u-\|\dot u\|_2^2.
\tag{D3}
\]
The squared norm arises because
\(\|\dot u\|^2=4[\|Ku\|^2-(u^\top Ku)^2]/m^2\).
It is a spectral variance and is always nonnegative. Thus residual turning
lowers the current training rate; improvement has to come from changing `K`.

For a fixed positive-semidefinite matrix `K_0`, let `lambda_j` be its
eigenvalues and `c_j` the coordinates of `y` in an orthonormal eigenbasis.
Then
\[
m\kappa(t)=
\frac{\sum_j\lambda_j c_j^2e^{-4\lambda_jt/m}}
     {\sum_j c_j^2e^{-4\lambda_jt/m}}.
\]
Strong modes disappear first; the remaining residual favors the weakest
mode present in the labels. This is an exact fixed-feature benchmark, not
a replacement of the nonlinear network.

The same sign holds initially in the actual deep model. Zero readout gives
zero hidden velocity; the hidden Jacobian of the output is also zero.
Therefore `K(0)=G(0)` and `dot(K)(0)=0`, and (D3) yields
\[
\dot\kappa(0)=-\frac4{m^2}
\left[
\frac{y^\top G(0)^2y}{\|y\|^2}
-\left(\frac{y^\top G(0)y}{\|y\|^2}\right)^2
\right].
\tag{D4}
\]
It is strictly negative unless `y` lies in one eigenspace of `G(0)`.
For the two-input shifted-tanh example of the companion note, with
`y=(sqrt(2)Y,0)` and population Gram
`gamma I+(b+mu)^2 11^T`, (D4) tends in probability to `-(b+mu)^4<0`.
Thus monotonic improvement of the directional rate is false even under
the stipulated Gaussian and large-width quantifiers.

This does **not** refute a floor at `lambda_min(G(0))/m`: the directional
rate in that example starts above the floor. Neither its initial decrease
nor a decreasing minimum feature eigenvalue proves that this floor is crossed.

### The nonlinear term that must compensate

Put `g=J^T r` and `S=sum_a r_a Hess_vartheta(f_a)`, just in this calculation.
Then `dot(vartheta)=-2g/m`, and differentiating `K=JJ^T` gives
\[
r^\top\dot K r
=2g^\top\dot J^\top r
=2g^\top S\dot\vartheta
=-\frac4m g^\top Sg.
\]
Consequently
\[
\kappa(t)+\int_0^t\|\dot u(s)\|^2\,ds
=\kappa(0)-\frac4{m^2}\int_0^t
\frac{g(s)^\top S(s)g(s)}{\|r(s)\|^2}\,ds.
\tag{D5}
\]
The residual-weighted output Hessian has no universal sign. Readout
linearity does not remove it. To see the remaining terms, write the hidden
whitened parameters as `v`, the readout as `b=w/sqrt(n)`, and
`F(v)=H(v)/sqrt(n)`. With `C=D_v(F r)` and
`T=sum_i b_i D_v^2(F r)_i`, holding `r` fixed in these derivatives,
\[
g=\begin{pmatrix}C^\top b\\Fr\end{pmatrix},\qquad
S=\begin{pmatrix}T&C^\top\\C&0\end{pmatrix},\qquad
g^\top Sg=(C^\top b)^\top T(C^\top b)+2(Fr)^\top CC^\top b.
\]
Neither surviving term has a sign forced by the stated activation class.
No favorable all-time bound for their integral is proved here.

## 3. Feature learning nevertheless helps at its first nonzero order

Keep the whitened coordinates `(v,b)` and `F=H/sqrt(n)` from above, so
`f=F(v)^T b`. Define the fixed-label feature energy, locally in this proof,
\(s(v)=\|F(v)y\|^2=y^\top G(v)y\).
Zero readout gives
\[
\dot b(0)=2F(0)y/m,\quad \dot v(0)=0,\quad
\ddot v(0)=2\nabla_v s(v_0)/m^2.
\]
The last identity follows by differentiating
`dot(v)=-(2/m)D_v(F r)^T b`; only differentiating `b` survives at zero.
Therefore
\[
y^\top\ddot G(0)y=\frac2{m^2}\|\nabla_v s(v_0)\|^2.
\]
Let `J_h=D_v f`. It vanishes initially, whereas
\(\dot J_h(0)^\top y=\nabla_v s(v_0)/m\). Since `K=G+J_h J_h^T`,
\[
y^\top\ddot K(0)y=\frac4{m^2}\|\nabla_v s(v_0)\|^2\ge0.
\tag{D6}
\]
Half is improvement in top features; half is newly available hidden-gradient
directions. All hidden layers and their physical mobilities are included.

Let `r_fr` solve the matched frozen-feature equation
`dot(r_fr)=-2G(0)r_fr/m`, with `r_fr(0)=-y` and
`L_fr=||r_fr||^2/m`. The actual and frozen residual derivatives agree through
second order, because `dot(K)(0)=0`. Their third derivatives differ by
`2 ddot(K)(0)y/m`. Taylor expansion and (D6) give
\[
\mathcal L(t)-\mathcal L_{\rm fr}(t)
=-\frac8{3m^4}\|\nabla_v s(v_0)\|^2t^3+o(t^3).
\tag{D7}
\]
The directional-rate comparison is
\[
\kappa(t)-\kappa_{\rm fr}(t)
=\frac{2\|\nabla_v s(v_0)\|^2}{m^3\|y\|^2}t^2+o(t^2).
\]
When the displayed gradient is nonzero, the loss is strictly smaller than
with frozen features for all sufficiently small positive times. Under label
rescaling `y -> c y`, the favorable cubic coefficient scales as `c^4`.
The allowed time interval is not claimed uniform in `c`, width or other
problem parameters. When the coefficient is zero, the higher-order sign is
not specified. These are local statements, not an all-time dominance theorem.

## 4. Representing the labels is weaker than preserving every feature direction

Here `F=H/sqrt(n)` and `b=w/sqrt(n)` again, with `dot(b)=-2Fr/m`.
Define the target representation cost
\[
C_y(t)=\inf\{\|a\|^2:F(t)^\top a=y\},
\]
with value infinity if there is no such readout. Linear algebra gives
`C_y=y^T G^dagger y` when `y` is in the range of `G`; the minimum-norm
choice is `a=F G^dagger y`. This is an analysis certificate, not an extra
oracle supplied to the compression algorithm. It only concerns the fixed
labels, not all sample-space directions.

Let `a(t)` be that minimum-norm choice wherever it exists. No derivative
of `a` is used. Directly from the readout equation,
\[
\frac d{dt}\|b\|^2=-4\mathcal L+2\langle a,\dot b\rangle,
\qquad
\int_s^T\|\dot b\|^2\,dt\le\mathcal L(s)-\mathcal L(T).
\]
Integration, Cauchy--Schwarz and monotonicity of the loss give
\[
4(T-s)\mathcal L(T)
\le\|b(s)\|^2+
2\sqrt{\left(\int_s^T C_y(t)\,dt\right)
        (\mathcal L(s)-\mathcal L(T))}.
\tag{D8}
\]

**Conditional fitting theorem.** Suppose `C_y` is finite almost everywhere
and locally integrable after some finite `s_0`, and
\[
\liminf_{T\to\infty}\frac1{T^2}\int_{s_0}^T C_y(t)\,dt<\infty.
\tag{D9}
\]
Then `L(t)->0` for every finite label size. Indeed, write `ell=lim L(t)`
and take a sequence `T_k` along which the expression in (D9) is at most
a finite `D`. Divide (D8) by `T_k`, let `k` tend to infinity with fixed `s`,
and obtain `4 ell <= 2 sqrt(D(L(s)-ell))`. Let `s` tend to infinity to
conclude `ell=0`. In particular `C_y(t)=O(1+t)` suffices. Conversely,
positive limiting loss forces this time-integrated representation cost
divided by `T^2` to diverge to infinity, if it remains locally integrable.

If `C_y(t)<=B^2` from initialization, the explicit consequence is
\[
\mathcal L(T)\le\frac{BY}{2\sqrt T}.
\tag{D10}
\]
This is not an exponential tail and is not enough by itself to preserve the
compression headlines. The current argument supplies only residual decay
of order `T^(-1/4)` in this bounded-cost case.

### Approximate targets and the order of limits

For any measurable candidate readout `a(t)`, set `e=F^T a-y`. The same
identity has the extra term `4 r^T e/m`. Applying
`2 r^T e <= ||r||^2+||e||^2` gives, from zero initial readout,
\[
\mathcal L(T)\le
\frac YT\sqrt{\int_0^T\|a(t)\|^2dt}
+\frac1{mT}\int_0^T\|e(t)\|^2dt.
\tag{D11}
\]
For a positive regularization parameter `epsilon`, the explicit choice
`a=F(G+epsilon I)^(-1)y` has squared norm at most
`||y||^2/(4 epsilon)` and error `-epsilon(G+epsilon I)^(-1)y`.
The norm bound follows by diagonalization and
`s/(s+epsilon)^2 <= 1/(4 epsilon)` for nonnegative eigenvalues `s`.
Consequently the condition
\[
\lim_{\epsilon\downarrow0}\limsup_{T\to\infty}
\frac1{mT}\int_0^T
\|\epsilon(G(t)+\epsilon I)^{-1}y\|^2dt=0
\tag{D12}
\]
also implies fitting. The first term of (D11) is at most
`sqrt(m)Y^2/(2 sqrt(epsilon T))`, which vanishes first at fixed `epsilon`.
Positive definiteness at every finite time does not justify interchanging
these two limits. Proving (D9) or (D12) for arbitrary-label Gaussian training
remains open.

### Even the target representation cost need not improve monotonically

The shifted-tanh example from Section 7 of the companion note gives a
counterexample to monotone decrease of `C_y` under typical Gaussian
initialization. Use its local notation
`g=tanh(Z+s)`, `p=sech^2(Z+s)`, `mu=E g`, `gamma=Var(g)>0`, with `s>0`
sufficiently small and activation offset `b>1` fixed independently of width.
Then `G(0)` tends to `G_*=gamma I+(b+mu)^2 11^T`. For labels
`y=(sqrt(2)Y,0)`, the entrywise limit `T` of `ddot(G)(0)` is
\[
\begin{aligned}
T_{11}&=4Y^2\{2\mathbb E[(b+g)^2p^2]
                 +(\mathbb E[Z(b+g)p])^2\},\\
T_{12}&=2Y^2(b+\mu)\{2\mathbb E[(b+g)p^2]
                 +\mathbb E[Zp]\mathbb E[Z(b+g)p]\},\\
T_{22}&=0.
\end{aligned}
\tag{D13}
\]
For completeness, these entries use the same conditional Gaussian
decomposition `W=Xi(U^T U)^(-1)U^T+V Pi` proved in the companion note.
Contracting `ddot(h_1)` with `h_1` makes the direct and independent
remainder terms each `E[(b+g)^2p^2]`; the projected direction contributes
`(E[Z(b+g)p])^2`. Contracting with the second feature vector instead yields
its independent mean `b+mu`, and the first projected factor is `E[Zp]`.
The second projected direction contributes zero. The second sample's
acceleration contains `Q_21 -> 0`, yielding `T_22=0`. Conditional variances
vanish and the sample-average limits are justified exactly as there.

Let `e_-=(1,-1)/sqrt(2)` and `e_+=(1,1)/sqrt(2)` just in this paragraph.
The eigenvalues of `G_*` are `gamma` and `lambda_+=gamma+2(b+mu)^2`, so
`G_*^(-1)y=(Y/gamma)e_-+(Y/lambda_+)e_+`. The companion note proves that
\[
e_-^\top T e_-=2Y^2(c_1b+c_0),\qquad
c_1=2\operatorname{Cov}(g,p^2)
+\mathbb E[Z(g-\mu)p]\mathbb E[Zp]<0,
\]
where `c_0` is independent of `b`. From (D13), the other two contractions
`e_-^T T e_+` and `e_+^T T e_+` are `O(Y^2 b^2)`. Hence
\[
(G_*^{-1}y)^\top T(G_*^{-1}y)
=\frac{2Y^4c_1}{\gamma^2}b+O(Y^4)<0
\]
for sufficiently large fixed `b`; the last asymptotic is as `b` grows,
with `s` fixed, before the width limit is taken. Since `dot(G)(0)=0`,
\[
\ddot C_y(0)=-(G(0)^{-1}y)^\top\ddot G(0)(G(0)^{-1}y).
\]
The initial Gram is invertible with probability tending to one, and the
convergence above proves `P{ddot(C_y)(0)>0}->1` for the chosen fixed
activation, at every fixed `Y>0`. Thus a proof of (D9) cannot simply assert
that the label representation cost decreases.

## 5. Hidden sensitivities can rescue weak top features

This route uses the actual last hidden matrix, without changing architecture.
Let `U=[h_1^(L-1),...,h_m^(L-1)]` and `z_ia=z_i^(L)(x_a)` at the current
time. For this section write
\[
Q=U^\top U/n,\qquad
S_{ab}=\frac1n\sum_iw_i^2\phi_L'(z_{ia})\phi_L'(z_{ib}).
\]
The contribution of `W^(L)` to the full tangent Gram is exactly
\[
K^{(L)}=Q\odot S.
\tag{D14}
\]
Indeed `partial f_a/partial W_ij^(L)=w_i phi_L'(z_ia)U_ja/n`, and
this matrix block has mobility one. Taking the Frobenius inner product
of two such derivatives proves (D14), including both factors `1/n`.

If `Q>=g I` for some `g>0`, then
\[
K\succeq G+g\,\operatorname{diag}_{a}
\left[\frac1n\sum_iw_i^2\phi_L'(z_{ia})^2\right].
\tag{D15}
\]
To justify the matrix inequality without importing a positivity theorem,
`S` is a Gram matrix. If `Q-gI` is also a Gram matrix, their entrywise
product is the Gram matrix of tensor products of the respective vectors,
hence positive semidefinite. Also `I odot S=diag(S_aa)`.

More weakly, the actual residual only needs the corresponding weighted sum:
\[
\kappa\ge\frac{\|Hr\|^2}{mn\|r\|^2}
+\frac g m\frac{\sum_a r_a^2S_{aa}}{\|r\|^2}.
\]
A minimum over all `S_aa` is sufficient, but unnecessarily strong if weak
derivative moments occur only on samples with negligible residual.

Thus a uniform positive lower bound on every `S_aa`, together with a
preceding-layer feature gap, supplies a full tangent gap. A lower bound
only on the residual-weighted sum supplies directional coercivity, which
is enough for the corresponding residual estimate. The full-gap bound works
even if the top-feature Gram collapses. Such a bound is not proved merely
by writing (D15).

This compensation is possible in the actual architecture, not just in an
abstract matrix example. Take the companion note's two-layer cosine
activation, `U^T U/n=I_2`, `w=a 1` with `a>0`, and
\[
W^{(2)}=\frac{\pi}{2n}\mathbf1(u_1+u_2)^\top.
\]
Both top preactivation columns are `pi/2`, so both feature columns are
`(3/2) 1` and `G` has rank one. Both derivatives are `-1/2`, however, giving
`K^(2)=(a^2/4)I_2`. This is an admissible parameter-state example of rescue,
not a claim about its probability of occurring during Gaussian training.

### A deterministic anti-concentration reduction

Set, only here,
\[
u_w=\frac1n\sum_iw_i^2,\qquad
M_4=\frac1n\sum_iw_i^4,\qquad
p_a(\epsilon)=\frac1n\#\{i:|\phi_L'(z_{ia})|<\epsilon\}.
\]
On the complement of this small-derivative set, the derivative square is
at least `epsilon^2`. Cauchy--Schwarz on the removed coordinates gives
\[
S_{aa}\ge\epsilon^2
\left[u_w-\sqrt{M_4p_a(\epsilon)}\right].
\tag{D16}
\]
In particular, if `u_w>=u_*>0`, `M_4<=C_4`, and
`p_a(epsilon)<=u_*^2/(4C_4)` for every sample, then
`S_aa>=epsilon^2 u_*/2`. Independence between weights and preactivations
is **not** assumed.

Alternatively, a varying cohort of at least `p_0 n` neurons per sample with
`|w_i|>=b_0` and `|phi_L'(z_ia)|>=epsilon` gives directly
`S_aa>=p_0 b_0^2 epsilon^2`. The cohort need not be the same for different
samples or times. A very small fraction depending on the fixed label size
could worsen constants and width thresholds without changing the width
exponent. The fraction and the two thresholds must remain positive and
independent of width and time on the asserted event; their persistence has
not been proved.

At a population level, a uniformly bounded preactivation density and
second moment would imply the needed small-derivative fraction for some
positive `epsilon`. Choose a compact interval whose tail probability is
small by the second moment. On that interval a nonconstant real-analytic
activation has only finitely many derivative zeros. Their shrinking
sublevel neighborhoods have Lebesgue measure tending to zero; the bounded
density controls their probability. A finite-width, uniform-time empirical
version still needs proof. Gaussianity holds at initialization only; it
cannot be silently assumed after training or after repeated matrix use.

### Why simpler state bounds do not close this route

In the cosine example of the companion note, choose two orthogonal vectors
`u_1,u_2` in `R^n` with norms `sqrt(n)`, so `U^T U/n=I_2`, and let
\[
W^{(2)}=\frac\pi n\mathbf1u_2^\top+B,\qquad BU=0,\qquad w=a\mathbf1.
\]
The first activation is linear and `A=U`, with the same orthogonal sphere
inputs. Then the top preactivations are identically `0` and `pi`, the top
features are `2` and `1`, and labels `(3a,-a)` give the same non-fitting
local minimum as before. Every top-layer activation derivative is zero, so all
`S_aa=0`, despite an exactly conditioned preceding layer and positive
readout norm. The free matrix `B` may be dense with bounded operator norm.
This is a parameter-state obstruction, not a Gaussian-reachability theorem.
It shows why bounded norms alone cannot replace the missing anti-concentration.

An initially unused readout is not a permanently inactive reserve. Its top
row velocity contains `w_i`, but its input changes when preceding layers
move. Moreover in this cosine model every initialized readout coordinate
has `dot(w_i)(0)=a(3h_1i-h_2i)>=a`, independent of Gaussian tails. A reserve
argument needs a genuine persistence estimate, not a small initial readout.

## 6. Time-averaged correction can replace an instantaneous gap

The following criterion is deterministic and applies to the actual full
tangent matrix. In this section put `A(t)=2K(t)/m`, so `dot(r)=-A r`.
Suppose there exist positive constants `tau,alpha,B`, independent of the
starting time, such that on every interval `[t,t+tau]`,
\[
\int_t^{t+\tau}A(s)\,ds\succeq\alpha I,
\qquad \int_t^{t+\tau}\|A(s)\|_{\rm op}\,ds\le B.
\tag{D17}
\]
Then
\[
\|r(t+\tau)\|^2\le
\left(1-\frac{2\alpha}{(1+B)^2}\right)\|r(t)\|^2.
\tag{D18}
\]

**Proof.** Write `E=int_t^(t+tau) r^T A r`. Positivity gives
`||A r||^2 <= ||A|| r^T A r`; hence for any `s` in the interval,
`||r(s)-r(t)|| <= sqrt(B E)`. The triangle inequality in the weighted
space-time norm then yields
\[
\sqrt\alpha\,\|r(t)\|
\le\left(\int r(t)^\top A(s)r(t)\,ds\right)^{1/2}
\le\sqrt E+B\sqrt E.
\]
Indeed the difference term is at most
`sqrt(int ||A|| ||r(s)-r(t)||^2) <= B sqrt(E)`.
The energy identity `||r(t)||^2-||r(t+tau)||^2=2E` proves (D18).
Since `alpha<=B`, its contraction factor lies between `1/2` and `1`.
Iteration gives an exponential residual tail. On each interval the metric
parameter path is at most `sqrt(tau L(t))`; the resulting geometric sum
is finite. No pointwise positive minimum eigenvalue is required: different
directions may be corrected at different times.

In fact the matrix lower bound in (D17) is stronger than this proof needs.
It is enough to require, only in the actual direction at the start of each
window,
\[
\int_t^{t+\tau}u(t)^\top A(s)u(t)\,ds\ge\alpha,
\qquad u(t)=r(t)/\|r(t)\|.
\tag{D17-directional}
\]
Retain the same integrated operator bound `B`. The proof above is unchanged:
it uses the lower bound only on `r(t)`, not on any other vector. The vector
inside this integral is held fixed at the beginning of the window; it is
not `u(s)`. This makes explicit a residual-specific route that permits all
unneeded sample directions to degenerate.

The meaningful missing assertion is (D17), or its directional version,
with constants uniform in width
on a sufficiently likely Gaussian event, allowed to depend on the fixed
problem and label size. It is not established by initial Gaussian support.
Even if it were established, compression still needs controlled responses
and analytic approximation constants along the large-motion trajectory.

## 7. A vanishing rate may still fit, but changes the available time scale

Suppose, as an explicit conditional hypothesis after some finite time `T`,
\[
\kappa(t)\ge c\rho(t)^p,\qquad c>0,\qquad 0\le p<2.
\tag{D19}
\]
Here `p` is a local exponent, not the compression order. Equation (D1) gives
\[
\rho(t)\le
\begin{cases}
\rho(T)e^{-2c(t-T)},&p=0,\\
[\rho(T)^{-p}+2cp(t-T)]^{-1/p},&p>0.
\end{cases}
\]
Since the parameter speed equals `-dot(rho)/sqrt(kappa)`, integration gives
\[
\int_T^\infty\|\dot\theta\|_{M^{-1}}dt
\le\frac{\rho(T)^{1-p/2}}{\sqrt c(1-p/2)}.
\tag{D20}
\]
Thus parameters converge and labels are fitted even with a vanishing rate.
For `p<1` one also has
`int_T^infty rho <= rho(T)^(1-p)/(2c(1-p))`.
For the following width scalings, require a fixed `p`, a width-independent
positive lower bound on `c`, and a width-independent upper bound on the
onset time `T`; the label RMS `Y` is already fixed. For `p>0`, this certificate
alone supplies a sufficient residual horizon
`O(n^(p/2))` at error `n^(-1/2)`, rather than `O(log n)`; the metric-tail
bound supplies `O(n^(p/(2-p)))` for that metric accuracy. These are worst-case
sufficient orders from this criterion, not lower bounds for actual training.
They do not preserve the current compression conclusions automatically.

## 8. Research assessment and exact remaining obligations

| Route | Established here | What remains unproved |
|---|---|---|
| Residual avoids weak directions | The residual-turning term has the opposite sign; initial directional improvement is false generically | A weaker positive all-time or integrated directional bound |
| Features improve under training | Favorable quadratic tangent and cubic loss correction relative to frozen features | Its continuation past the initial local interval |
| Labels remain cheaply representable | Deterministic criterion (D9), including linear growth of squared target cost | Gaussian reachable-state control of that cost; monotone cost is false |
| Hidden sensitivities rescue weak features | Exact last-layer contribution (D14), lower bound (D15), moment reduction (D16) | Persistent preceding-layer geometry and derivative anti-concentration |
| Different directions are corrected over time | Window criterion (D17) implies exponential fitting and finite path | A width-uniform Gaussian proof of the window condition |

The most useful positive mechanism is not automatic residual rotation away
from weak directions. It is adaptive correction: newly available hidden
sensitivities, or changing informative directions over a time window, can
compensate for that rotation. The displayed identities make this mechanism
precise, but do not prove that it persists for the entire allowed activation
and data class. In particular, a theorem valid at every bounded parameter
state is impossible because of the explicit saturated bad states.

For preserving the compression scope, the highest-leverage next obligation
is a **Gaussian reachable-state, width-uniform excitation bound**, such as
(D17), with controlled nonlinear responses. A proof only of eventual fitting
via (D9) or an algebraic rate via (D19) is useful but insufficient. No
incompressibility statement, promotion, or change to an integrated theorem
is made by this note.

Sources: the canonical model, this study's complete `LABEL_SCALE.md`, and
the exact calculations above. Three scoped mathematical routes supplied
independent first-round derivations; their concrete findings were then
cross-checked and combined by the lead. No external optimization theorem
or unpromoted result from another study is used.
