# Residual damping and all-time comparison for small labels

Scoped analytic route, 28 September 2026. Inputs: the canonical setting and
old-clock equations/proof in `paper/main.tex`, `docs/notation.qmd`, and this
study's `LOSS_DECAY_ACTIVITY_BOOTSTRAP.md`, `LOSS_DECAY_SYNTHESIS.md`,
`ENERGY_STABILITY_ROUTE.md`, and `OLD_CLOCK_ROUTE.md`. The
`solve-math-rigorously` skill was applied. No other research source, experiment,
subagent, or maintained-file change was used.

**Outcome.** Positive readout Gram and finite activity do remove the infinite
physical horizon from the comparison argument. For the actual original
old-clock closure, they give an all-time `O(P^-1)` parameter theorem at every
fixed width, with an explicit bound

\[
 \sup_{t\ge0}d_n(\widehat\theta_P(t),\theta_D(t))
 \le \frac{C Y^3}{\sqrt{P(P+1)}}
       \exp\{C Y+C\sqrt n\,Y^2\}.
 \tag{1}
\]

Here the small-label threshold and `C` are independent of width; the displayed
exponential is not. This does **not** prove the requested bound for a fixed
positive label size uniformly over arbitrarily large widths. The exact
remaining quantity is an activity-weighted gate/carrier product on the actual
pair of trajectories, displayed in (24) below. No uniform carrier supremum,
Hessian bound, or finite-width stability assumption is used.

The proof first damps the prediction discrepancy, then inserts its integrated
bound into the parameter equations. This avoids integrating a persistent
Jacobian-times-prediction-error term over infinite physical time. A
one-reference backward expansion isolates the only unresolved spatial
multiplication term.

## 1. Deterministic regime and the common all-time bounds

The network, tanh activation, loss, mobilities, and original old-clock
reconstruction are exactly those of the manuscript. Both systems start at
the same parameter. Write

\[
 X=\max_a\|x_a\|_2/\sqrt d,\qquad
 Y=\left(m^{-1}\sum_a y_a^2\right)^{1/2},\qquad
 B_0=\|w_0\|_2/\sqrt n.
\]

Fix depth, data inputs, a hidden operator bound `K`, and a number
`lambda_0>0`. Assume

\[
 \max_{2\le\ell\le L}\|W_{0,\ell}\|_{\rm op}\le K,
 \qquad B_0\le Y,
 \qquad \Gamma_w(0):=\frac{H_L(0)^T H_L(0)}{mn}
                   \succeq\lambda_0 I_m.
 \tag{2}
\]

The same argument works on an invariant compatible residual subspace with
the Gram gap restricted to it. For clarity, all formulas below use the full
sample space.

Choose `Y_*<=1` as in the small-readout theorem of
`LOSS_DECAY_ACTIVITY_BOOTSTRAP.md`, shrinking it when necessary below. For
`0<Y<=Y_*`, set `S=4Y/lambda_0`. Its deterministic activity proof supplies,
simultaneously for every `P>=1`, global closure existence, interpolation,
finite parameter limits, and

\[
 \int_0^\infty\widehat\rho\,dt\le3Y/\lambda_0<S,
 \qquad \widehat\Gamma_w(t)\succeq\lambda_0 I_m/2,
 \qquad \int_0^\infty e_E(t)dt\le
 \varepsilon_P:=\frac{C_EY^3}{\sqrt{P(P+1)}},
 \tag{3}
\]

where `e_E=sum_(l=2)^L ||E_l||_F` and
`dot theta_hat=F(theta_hat)+E`, with `E_1=E_w=0`.
The constants in (3) depend only on `L,X,K,lambda_0`, not on `n,P,Y`
within this regime.

For completeness, the identical activity bootstrap applies to the dense
flow with `E=0`. Until activity reaches `S`, use `A=1+S`, `B=Y+2S` and

\[
 \beta_L=B,\qquad D_\ell=K+2A\beta_\ell,\qquad
 \beta_{\ell-1}=D_\ell\beta_\ell.
 \tag{4}
\]

The dense history integral and the closure's projected history integral
both give these common operator and backward bounds. In the dense case
the bound `2S beta_l<=2A beta_l` suffices for its learned operator. The
forward derivative estimate in the activity note remains valid after
setting the defect to zero. Its bound on top-feature drift therefore keeps
`Gamma_(w,D)>=lambda_0 I/2` on the stopped interval. Consequently

\[
 \dot\rho_D\le-\lambda_0\rho_D,\qquad
 \int_0^t\rho_D\,ds\le\rho_D(0)/\lambda_0
                  \le2Y/\lambda_0=S/2.
 \tag{5}
\]

This excludes first activity exit. Finite-dimensional dense gradient flow
exists globally by the manuscript's energy continuation argument. Thus
(5) holds for all time, and the dense velocity bound by a constant times
`rho_D` also proves a finite parameter limit and interpolation.

In particular, (4) and the compact interval `0<=Y<=Y_*` imply common
constants `D_*,B_*`, independent of width, order, time and label size, such
that along both paths

\[
 \|W_\ell\|_{\rm op}\le D_*,\qquad
 \frac{\|w\|_2}{\sqrt n}\le B_*Y,\qquad
 \max_a\frac{\|\delta_{\ell,a}\|_2}{\sqrt n}\le B_*Y.
 \tag{6}
\]

For example, divide the recursion for every `beta_l` by `Y`; downward
induction bounds the resulting polynomials uniformly on `[0,Y_*]`.
This verifies the uniform dependence used below.

## 2. Forward differences and the exact carrier remainder

Use a sum of the normalized parameter-block norms:

\[
 x(t)=\frac{\|\widehat W_1-W_{1,D}\|_F}{\sqrt n}
          +\sum_{\ell=2}^L\|\widehat W_\ell-W_{\ell,D}\|_F,
 \qquad z(t)=\frac{\|\widehat w-w_D\|_2}{\sqrt n},
 \qquad d(t)=x(t)+z(t).
 \tag{7}
\]

This sum dominates the mobility Hilbert distance `d_n` in (1) and is at
most `sqrt(L+1)` times that distance. The notation `z(t)` in (7) is an
auxiliary scalar readout discrepancy; preactivation vectors retain layer
and sample subscripts.

Set `u_1=X` and `u_l=1+D_*u_(l-1)`. The forward recurrence gives, for
every sample and layer,

\[
 \frac{\|\widehat z_{\ell,a}-z_{\ell,a,D}\|_2}{\sqrt n}
 \le u_\ell x,
 \qquad
 \frac{\|\widehat h_{\ell,a}-h_{\ell,a,D}\|_2}{\sqrt n}
 \le u_\ell x.
 \tag{8}
\]

Indeed, the first-layer difference is the first matrix difference applied
to `x_a/sqrt(d)`. At later layers write the difference as
`(W_hat_l-W_(l,D)) h_(l-1,D)+W_hat_l(h_hat_(l-1)-h_(l-1,D))`, use
`||h_(l-1,D)||_2<=sqrt(n)`, and then use tanh's Lipschitz constant one.

Let `D_(l,a)=diag(tanh'(z_(l,a)))`. Define only on the dense reference

\[
 k_{L,a}=w_0,\qquad
 k_{\ell,a}=W_{0,\ell+1}^T\delta_{\ell+1,a,D}
                  \quad(1\le\ell<L),
\]
\[
 g_\ell(t)=\max_a\left[
 \frac1n\sum_{i=1}^n |k_{\ell,a,i}(t)|^2
  |\tanh'(\widehat z_{\ell,a,i}(t))-
                  \tanh'(z_{\ell,a,i,D}(t))|^2
                     \right]^{1/2},
 \qquad G(t)=\sum_{\ell=1}^L g_\ell(t).
 \tag{9}
\]

At zero initial readout, `g_L=0` identically. Lower-layer terms remain.

The learned part of a dense carrier has a coordinate bound with no width
factor. To check this without a separate regularity assumption, put
`A_(l,D)=W_(l,D)-W_(0,l)`. The exact dense history gives

\[
 (A_{\ell,D}(t)^T\delta_{\ell,a,D}(t))_j
 =-\frac2m\sum_b\int_0^t r_{b,D}(s)h_{\ell-1,b,j,D}(s)
       \frac{\delta_{\ell,b,D}(s)^T\delta_{\ell,a,D}(t)}n\,ds.
\]

Bound the normalized pairing by `beta_l^2`, the feature by one, and the
sample mean of `|r_(b,D)|` by `rho_D`. Hence

\[
 \|A_{\ell,D}(t)^T\delta_{\ell,a,D}(t)\|_\infty
       \le2S\beta_\ell^2,
 \qquad \|w_D(t)-w_0\|_\infty\le2S.
 \tag{10}
\]

Write
`b_l(t)=max_a ||delta_hat_(l,a)-delta_(l,a,D)||_2/sqrt(n)`.
Subtract the top backward relation using the dense readout in the gate
term. Since `|tanh'(v)-tanh'(u)|<=2|v-u|`, (8)--(10) give

\[
 b_L\le z+4S u_Lx+g_L.
 \tag{11}
\]

At lower layers the exact subtraction is

\[
\begin{split}
 \widehat\delta_{\ell,a}-\delta_{\ell,a,D}
 ={}&\widehat D_{\ell,a}\widehat W_{\ell+1}^T
           (\widehat\delta_{\ell+1,a}-\delta_{\ell+1,a,D})\\
 &+\widehat D_{\ell,a}(\widehat W_{\ell+1}-W_{\ell+1,D})^T
             \delta_{\ell+1,a,D}\\
 &+(\widehat D_{\ell,a}-D_{\ell,a,D})
              A_{\ell+1,D}^T\delta_{\ell+1,a,D}\\
 &+(\widehat D_{\ell,a}-D_{\ell,a,D})k_{\ell,a}.
\end{split}
\]

The four terms yield respectively

\[
 b_\ell\le D_* b_{\ell+1}+\beta_{\ell+1}x
          +4S\beta_{\ell+1}^2u_\ell x+g_\ell.
 \tag{12}
\]

Equations (11)--(12), `S=O(Y)`, and `beta_l=O(Y)` prove the uniform,
actual-path inequality

\[
 \max_\ell b_\ell(t)\le C\,[z(t)+Yx(t)+G(t)].
 \tag{13}
\]

Only the initialized-carrier expression (9) is left unestimated here.
There is no closure-carrier tail hypothesis in this calculation.

## 3. The residual equation provides the necessary damping

Let `q=f_hat-f_D=r_hat-r_D` and `v=||q||_m`. The tangent Gram with
canonical mobilities is

\[
 \Gamma_{ab}=\frac1m\left[
 \frac{h_{L,a}^Th_{L,b}}n+
 \frac{\delta_{1,a}^T\delta_{1,b}}n\frac{x_a^Tx_b}d+
 \sum_{\ell=2}^L\frac{\delta_{\ell,a}^T\delta_{\ell,b}}n
                    \frac{h_{\ell-1,a}^Th_{\ell-1,b}}n
                    \right].
 \tag{14}
\]

Each summand is positive semidefinite, so
`Gamma_hat>=Gamma_(w,hat)>=lambda_0 I/2`. Subtracting the exact
residual equations gives

\[
 \dot q=-2\widehat\Gamma q
        -2(\widehat\Gamma-\Gamma_D)r_D+\widehat J E.
 \tag{15}
\]

To bound the Gram difference, a matrix whose entries are bounded in
absolute value by `a/m` has operator norm at most `a`. A backward
normalized pairing changes by at most `2 beta_l b_l`; a forward
normalized pairing changes by at most `2u_l x`. Apply these two facts
to (14), using `|x_a^T x_b/d|<=X^2`, to obtain explicitly

\[
 \|\widehat\Gamma-\Gamma_D\|_{\rm op}
 \le 2u_Lx+2X^2\beta_1b_1+
       \sum_{\ell=2}^L(2\beta_\ell b_\ell+
                                  2\beta_\ell^2u_{\ell-1}x)
 \le C[x+Yz+YG].
 \tag{16}
\]

Also, each sample's hidden-block output differential is
`delta_hat_(l,a)^T E_l h_hat_(l-1,a)/n`; therefore
`||J_hat E||_m<=max_l beta_l e_E<=CY e_E`.
Taking the inner product of (15) with `q/v` when `v>0`, or using the
upper derivative of the norm at `v=0`, proves

\[
 D^+v\le-\lambda_0v+
                  C\rho_D(x+Yz+YG)+CY e_E.
 \tag{17}
\]

One may justify the integrated norm inequality by first replacing `v`
with `sqrt(v^2+eta^2)` and then letting `eta` decrease to zero on a
finite interval. Since `q(0)=0`, integration of (17), followed by
dropping its nonnegative endpoint, gives

\[
 Q(t):=\int_0^t v(s)ds
 \le C\int_0^t\rho_D(s)[x(s)+Yz(s)+YG(s)]ds
          +CY\varepsilon_P(t),
 \quad \varepsilon_P(t):=\int_0^t e_E(s)ds.
 \tag{18}
\]

This is the step unavailable from a bare parameter Lipschitz estimate:
the prediction error is integrated with a coercive residual equation.

## 4. Inserting damping into the parameter differences

Subtract the readout equations by writing
`r_hat h_hat-r_D h_D=q h_hat+r_D(h_hat-h_D)`. Normalized vector norms,
sample Cauchy--Schwarz, and (8) give

\[
 z(t)\le2Q(t)+2u_L\int_0^t\rho_D(s)x(s)ds.
 \tag{19}
\]

In the first-layer equation, the corresponding bound is
`2X[beta_1 v+rho_D b_1]`. For a hidden block, use

`r_hat delta_hat h_hat^T-r_D delta_D h_D^T`

`=q delta_hat h_hat^T+r_D(delta_hat-delta_D)h_hat^T`

`+r_D delta_D(h_hat-h_D)^T`.

After the canonical factor `2/(nm)`, its Frobenius bound is
`2[beta_l v+rho_D(b_l+beta_l u_(l-1)x)]`. Include `E_l`, sum the
hidden blocks and first layer, and use (13). This proves

\[
 x(t)\le CYQ(t)+C\int_0^t\rho_D(s)[z(s)+Yx(s)+G(s)]ds
                     +\varepsilon_P(t).
 \tag{20}
\]

Combining (18)--(20), and using `0<Y<=Y_*<=1`, gives the promised
all-time comparison with only one unresolved term:

\[
 d(t)\le C_0\varepsilon_P(t)+
             C_1\int_0^t\rho_D(s)[d(s)+G(s)]ds.
 \tag{21}
\]

The constants are independent of width, order and physical horizon. This
is a proved inequality for the actual original closure and dense path,
not an assumed stability bound. In particular, growth in physical time
has been completely removed before any estimate of the initialized
carriers. The only time measure remaining is `rho_D(s)ds`, whose total
mass is at most `2Y/lambda_0`.

For a direct bound retaining the exact carrier remainder, define

\[
 A_P(t)=\int_0^t\rho_D(s)G(s)ds.
\]

Both `A_P` and `epsilon_P(t)` are nondecreasing. Applying the elementary
integral Gronwall argument to (21), for each fixed terminal `t`, yields

\[
 \sup_{0\le s\le t}d(s)
 \le [C_0\varepsilon_P(t)+C_1 A_P(t)]
              \exp\!\left(C_1\int_0^t\rho_D(s)ds\right).
 \tag{22}
\]

For example, replace the nondecreasing inhomogeneous term on `[0,t]`
by its value at `t`; differentiating its integral majorant gives the
exponential in (22). This verifies the needed version of Gronwall.

## 5. A complete fixed-width all-time theorem

The deterministic coordinate estimate `||u||_infty<=||u||_2` and (6)
give

\[
 \|k_{L,a}\|_\infty\le\sqrt n\,Y,\qquad
 \|k_{\ell,a}\|_\infty\le
        \|W_{0,\ell+1}\|_{\rm op}\|\delta_{\ell+1,a,D}\|_2
        \le C\sqrt n\,Y\quad(\ell<L).
\]

This is a proved finite-dimensional estimate, expressly containing its
width loss. By (8)--(9), it implies
`G<=C sqrt(n)Y x<=C sqrt(n)Y d`. Substitute into (21), use
`integral rho_D<=2Y/lambda_0`, and apply the same integral argument:

\[
 \sup_{t\ge0}d(t)
 \le C_0\varepsilon_P
       \exp\{C Y+C\sqrt n\,Y^2\}.
 \tag{23}
\]

Equations (3) and (23) prove (1), simultaneously for every `P>=1`.
There is no order threshold in this fixed-width statement. Both
parameter limits exist, so (23) also bounds their difference. Moreover,
(18) gives `integral_0^infinity ||f_hat-f_D||_m dt<infinity` at every
fixed width. This proof does not assume that the closure residual decays
exponentially.

As a separate restricted corollary, the bound is width-uniform for a
family of label sizes with `sqrt(n)Y_n^2` bounded. This permits
`Y_n=O(n^-1/4)` when all other margins are uniform. It is not the
fixed-label theorem posed in the assignment.

## 6. The exact missing estimate for fixed labels

The only additional quantity in (22) is

\[
 \begin{split}
 A_P(\infty)=\sum_{\ell=1}^L\int_0^\infty\rho_D(t)
 \max_a\Bigg[\frac1n\sum_i|k_{\ell,a,i}(t)|^2
 \big|\tanh'(\widehat z_{\ell,a,i}(t))-
              \tanh'(z_{\ell,a,i,D}(t))\big|^2\Bigg]^{1/2}dt.
 \end{split}
 \tag{24}
\]

Thus a width-independent bound `A_P(infinity)<=C/P` would complete the
desired parameter theorem by (22). A stronger, local and potentially
bootstrappable inequality that would also suffice is

\[
 \sum_{\ell=1}^L\int_0^t\rho_D(s)
 \max_a\left[\frac1n\sum_i|k_{\ell,a,i}(s)|^2
       |\widehat D_{\ell,a,ii}(s)-D_{\ell,a,ii,D}(s)|^2\right]^{1/2}ds
 \le a\int_0^t\rho_D(s)d(s)ds+b\varepsilon_P(t),
 \tag{25}
\]

with finite `a,b` independent of width and order for the actual old-clock
pair. This is a specific spatial correlation estimate; it is not the
generic assertion that a network flow has a uniform stability constant.
All other terms in the comparison have been derived above, including
the residual damping and the learned part of every carrier.

Neither (24)'s desired bound nor (25) is proved here. A bound on the RMS
of `k` alone cannot prove (25), since the gate difference can concentrate
on coordinates where `k` is large. Finite activity makes the time
integral finite but supplies no decorrelation in the neuron index. The
positive Gauss--Newton part of the parameter energy acts on prediction
differences, and (17)--(18) already uses that coercivity; it does not
bound the spatial product in (24).

Even a proved sub-Gaussian reference-tail bound, without a correlation
estimate, would not immediately yield the endpoint rate by this route.
Truncating the carrier in (9) gives a modulus of the form
`G<=CY d sqrt(log(A/d))` at small `d` under the corresponding scaled
tail bound. Integration against total dense activity `O(Y)` produces
an amplification of the type `exp(CY^2 sqrt(log P))`. For every fixed
positive `Y`, this is not a constant independent of `P`. This is only a
diagnostic of the truncation argument, not an assertion of such trained
Gaussian tails or a counterexample to the desired closure theorem.

Under the nonparallel-input assumptions of `LOSS_DECAY_SYNTHESIS.md`,
canonical Gaussian initialization satisfies (2), with a fixed positive
`lambda_0`, `K=10`, and `B_0<=Y`, with probability tending to one. Thus
all results up to and including (23) apply on those same events. They
retain the explicit `sqrt(n)` dependence in (23); probability tending to
one does not remove it. At zero readout the top summand of (24) vanishes,
but all lower initialized-carrier summands still require control.

**Scope.** This route completes the passage from compact-time to all-time
tracking at fixed width in the proved small-label fitting regime. It
reduces the requested fixed-label, width-uniform theorem to the concrete
activity-weighted correlation estimate (24), or the sufficient local
form (25), and does not claim that estimate follows from energy
dissipation, Gaussian initialization, or finite residual activity alone.
