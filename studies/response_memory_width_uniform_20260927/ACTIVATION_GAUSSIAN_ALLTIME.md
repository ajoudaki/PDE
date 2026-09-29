# Small activity globalizes the Gaussian response for unbounded activations

28 September 2026. Scoped author derivation in the existing response-memory
study. The `solve-math-rigorously` skill and the adversarial-audit guidance
of `investigate-conjectures` were applied. Inputs were the complete assigned
`SMALL_LABEL_GAUSSIAN.md`, `ACTIVATION_EXTENSION.md`,
`ACTIVATION_SMALL_LABEL_ROUTE.md`, `SLOW_ORDER_UNIFORM_BOUND.md`, and
`ACTIVATION_INITIAL_GRAM.md`; `docs/index.qmd`, `docs/notation.qmd`; and
the complete C.1--C.2 proof units of `docs/03-local-population.qmd`.
No other study, archived book, experiment, external source, additional
dependency unit, or further agent was used. Only this report was written.
This is an internal proof candidate, not promotion or independent review.

**Result.** The dense population theorem in `SMALL_LABEL_GAUSSIAN.md`
extends to different globally Lipschitz, globally `C^{1,1}` activations
in the different layers, including unbounded activations. Small activity
replaces bounded activation values by fixed feature RMS bounds. The full
forward and backward carrier tails come from C.2's simultaneous response
bootstrap, not from the global Lipschitz property alone. The resulting
all-time population tails transfer to a qualitative, order-independent,
dense-only finite-width remainder. No quantitative width rate follows.

The argument does not establish the same Gaussian conclusion under only
`C^{1,1}_{loc}` regularity and bounded slope without a controlled derivative
modulus. The finite-width deterministic fitting theorem for that larger
class remains separate.

## 1. Statement and precise objects

Fix finite hidden depth `L>=2`, sample count `m`, input dimension `d`,
and inputs `x_a`. No orthogonality or invertibility of their input Gram
is required. Write

\[
 X=\max_a\|x_a\|_2/\sqrt d,\qquad
 \|v\|_m^2=m^{-1}\sum_a v_a^2,\qquad Y=\|y\|_m.
 \tag{1}
\]

For each layer assume

\[
 \phi_\ell\in C^1(\mathbb R),\quad
 a_\ell=|\phi_\ell(0)|<\infty,\quad
 s_\ell=\|\phi_\ell'\|_\infty<\infty,\quad
 j_\ell=\operatorname{Lip}(\phi_\ell';\mathbb R)<\infty.
 \tag{2}
\]

Use canonical independent Gaussian first and hidden initialization and
exactly zero stored readout, the averaged squared loss, and unit canonical
mobilities `(n,1,...,1,n)`. The population spaces and the initial hidden
operators with their actual adjoints are the generated spaces of C.1.
Choose a deterministic `K>=1` bounding those initial hidden operators.
As proved in C.1, the finite Gaussian operator event and fixed-program
second-moment convergence give this bound on every generated finite span,
and hence its closure. Let `A_0` bound each initial first-preactivation
`L2` norm; under the canonical Gaussian convention `A_0=X` suffices.

Use the population fields

\[
 Z_{1,a}=W_1x_a/\sqrt d,\quad
 Z_{\ell,a}=W_\ell H_{\ell-1,a},\quad H_{\ell,a}=\phi_\ell(Z_{\ell,a}),
\]
\[
 P_{L,a}=w,\quad P_{\ell,a}=W_{\ell+1}^*\delta_{\ell+1,a},\quad
 \delta_{\ell,a}=\phi_\ell'(Z_{\ell,a})P_{\ell,a},\quad
 f_a=\mathbb E[wH_{L,a}].
 \tag{3}
\]

Every pairing is within its own layer. In particular `P` is the full
trained carrier. Let

\[
 \Gamma_w(0)=m^{-1}(\mathbb E[H_{L,a}(0)H_{L,b}(0)])_{a,b}
       \succeq\lambda_0 I_m,\qquad\lambda_0>0.
 \tag{4}
\]

The theorem assumes this actual initial gap. The Gaussian initialization
conditions in `ACTIVATION_INITIAL_GRAM.md` supply it, for example, for
nonzero pairwise nonproportional inputs, a nonpolynomial first activation,
and nonconstant later activations satisfying (2). Linear or affine
activations require their own rank check. Sine, cosine, softplus, GELU,
SiLU, unit ELU, softsign, and layer-dependent choices are allowed by (2);
the activation names alone do not certify (4) for arbitrary data.

For differences of population parameters use

\[
 d(\theta,\vartheta)=\|W_1-V_1\|_{L^2(\mathbb R^d)}
 +\sum_{\ell=2}^L\|W_\ell-V_\ell\|_{\rm HS}
 +\|w-v\|_2.
 \tag{5}
\]

Only learned hidden increments and their differences are required to be
Hilbert--Schmidt. Initialized actions need not be Hilbert--Schmidt. Finite
counterparts of (5) are first-matrix Frobenius norm divided by `sqrt(n)`,
ordinary hidden Frobenius norms, and readout RMS, summed over the blocks.
The first matrix can be recovered by integrating its fixed input vectors,
so using it instead of the first-preactivation tuple causes no loss.

**Theorem.** A number `Y_*>0`, depending only on these fixed data and
activation/initialization bounds and `lambda_0`, has the following
properties for every label vector with `0<Y<=Y_*`:

1. There is a unique global strong dense population flow, with the
   equations holding in (5), and
   \[
    \rho_D(t)\le Ye^{-\lambda_0t},\qquad
    \int_0^\infty\rho_D(t)dt\le Y/\lambda_0,\qquad
    \int_t^\infty\|\dot\theta_D(v)\|_{\rm sum}dv
          \le CY e^{-\lambda_0t}.
    \tag{6}
   \]
   It converges in (5) to an interpolating parameter state.
2. There are `c,C>0`, independent of time and uniform over the displayed
   label range and directions, such that
   \[
    \sup_{t\in[0,\infty]}\max_{\ell,a}
    \mathbb E\exp(c|U_{\ell,a}(t)|^2)\le C,
    \quad U\in\{Z,H,P,\delta\}.
    \tag{7}
   \]
   The readout is included as `P_L`. Time infinity means the limiting
   parameter's fields. This bounds each time marginal, not a supremum
   inside the exponential.
3. Dense finite GF converges on each prescribed finite physical horizon
   in C.1's observable topologies. The same local-in-horizon transfer
   applies to every actual GD step sequence tending to zero, with no
   width/step rate assumed. For GF, the fixed-cutoff, all-time integrated
   tail statement (35) and the common dense-only floor (36) below hold.

The last conclusion does not assert empirical subGaussian tails of every
trained finite array, a concentration rate in width, or a tail theorem
uniform in a width-dependent cutoff. At `Y=0`, the exactly zero readout
makes all updates vanish and the assertions reduce to initialization.

The proof constructs deterministic population Euler programs stopped by
activity, establishes their Gaussian reference tails, excludes their stop
using a one-reference Jacobian modulus, and only then constructs the
continuous global flow. Thus activity is not assumed for a flow whose
existence is still being proved.

## 2. Deterministic tube and exact activity recurrences

Put `D=K+1` and define fixed feature bounds

\[
 M_1=a_1+s_1(A_0+1),\qquad
 M_\ell=a_\ell+s_\ell D M_{\ell-1}\quad(\ell\ge2).
 \tag{8}
\]

The inequality `|phi_l(z)|<=a_l+s_l|z|` implies these RMS bounds on
the tube

\[
 \max_a\|Z_{1,a}\|_2<A_0+1,\qquad
 \|W_\ell\|_{\rm op}<D\quad(\ell\ge2).
 \tag{9}
\]

Consider a population Euler program with physical steps `h_k`, residual
`r_k`, and define

\[
 \rho_k=\|r_k\|_m,\quad \alpha_k=h_k\rho_k,\quad
 s_j=\sum_{k<j}\alpha_k,\quad u_{a,k}=r_{a,k}/\rho_k.
 \tag{10}
\]

At zero residual freeze the state and delete its zero activity steps.
Otherwise `||u_k||_m=1`, so `|u_{a,k}|<=sqrt(m)` and
`m^{-1}sum_a|u_{a,k}|<=1`. Stop the program at total activity `S<=1`
or at first tube exit, truncating a last step if necessary. The exact
updates are

\[
 \Delta w_k=-\frac{2\alpha_k}{m}\sum_a u_{a,k}H_{L,a,k},
\]
\[
 \Delta W_{1,k}=-\frac{2\alpha_k}{m}\sum_a
      u_{a,k}\delta_{1,a,k}(x_a/\sqrt d)^T,
\]
\[
 \Delta W_{\ell,k}=-\frac{2\alpha_k}{m}\sum_a
      u_{a,k}\delta_{\ell,a,k}\otimes H_{\ell-1,a,k}.
 \tag{11}
\]

Define

\[
 b_L=2M_Ls_L,\qquad b_\ell=s_\ell D b_{\ell+1}\quad(\ell<L).
 \tag{12}
\]

The readout update and descending backpropagation give, at every stopped
node and affine interpolation state,

\[
 \|w\|_2\le2M_LS,\qquad
 \max_a\|\delta_{\ell,a}\|_2\le b_\ell S.
 \tag{13}
\]

At interpolation states use the readout bound there and recompute the
full backward network; (9) gives the same induction. The rank-one identity
`||U tensor V||HS=||U||2||V||2`, followed by summation of (11), yields

\[
 \|W_1-W_{1,0}\|_2\le2Xb_1S^2,\qquad
 \|W_\ell-W_{\ell,0}\|_{\rm HS}
                    \le2b_\ell M_{\ell-1}S^2.
 \tag{14}
\]

The first-preactivation displacement is at most `2X^2b_1S^2`.
Choose `S_b>0` sufficiently small that this and every hidden bound in
(14) are below `1/2`. Then a first tube exit contradicts the corresponding
strict margin. This reasoning also covers an exit inside an affine step,
because its increment is a fraction of the last Euler increment.

For an explicit feature-drift recurrence set

\[
 A_1=2s_1X^2b_1,\qquad
 A_\ell=s_\ell\{DA_{\ell-1}+2b_\ell M_{\ell-1}^2\}.
 \tag{15}
\]

Subtract the forward networks as
`W_l(Hprev-Hprev,0)+(W_l-Wl,0)Hprev,0`, use (14) and the
Lipschitz activation, and induct to get

\[
 \max_a\|H_{\ell,a}-H_{\ell,a}(0)\|_2\le A_\ell S^2,
 \qquad
 \|\Gamma_w-\Gamma_w(0)\|_{\rm op}
                         \le2M_LA_LS^2.
 \tag{16}
\]

The second inequality follows by expanding each product in the Gram;
every entry difference before division by `m` is bounded by its right
side, and an `m` by `m` matrix with entries at most `B/m` in magnitude
has operator norm at most `B`.

Reduce `S_b` so `2M_LA_LS_b^2<=lambda_0/2`. The tangent Gram, including
all blocks, then obeys

\[
 \Gamma\succeq\Gamma_w\succeq\lambda_0 I/2,\qquad
 \|\Gamma\|_{\rm op}\le G,
 \qquad\|F(\theta)\|_{\rm sum}\le V\rho.
 \tag{17}
\]

For example `G>=1` may dominate
`M_L^2+X^2b_1^2+sum_(l>=2)b_l^2M_(l-1)^2`, since `S<=1`.
One may take `V=2M_L+2Xb_1+sum_(l>=2)2b_lM_(l-1)`.
The preliminary residual bound `rho<=1+2M_L^2` holds when `Y,S<=1`.
All these estimates require only bounded slopes and linear growth.
They make no assertion about Gaussian tails after training.

## 3. Exact reused-matrix response in activity

This section spells out why C.2 is applicable after the time change.
At each fixed population program, the values `alpha_k,u_k` are
deterministic numbers, even though they were obtained causally from earlier
population expectations. Freeze these numbers, scalar contractions, and
Gaussian covariance laws in all named-source derivatives, exactly as in
C.1--C.2. This is legitimate for a population oracle program. It does
not freeze the random feedback of an actual finite trained network.

For the canonical hidden variance one, use C.2's forward and backward
Gaussian slots `xi^(l),eta^(l)` and response coefficients

\[
 \mathsf A^{(\ell)}_{ak,bs}
 =\mathbb E\frac{\partial\delta_{\ell,a,k}}
                    {\partial\xi^{(\ell)}_{b,s}},\qquad
 \mathsf C^{(\ell)}_{ak,bs}
 =\mathbb E\frac{\partial H_{\ell-1,a,k}}
                    {\partial\eta^{(\ell)}_{b,s}}.
 \tag{18}
\]

The exact scalar response representation is

\[
 Z_{\ell,a,k}=\xi^{(\ell)}_{a,k}
       +\sum_{b,s<k}\mathsf F^{(\ell)}_{ak,bs}\delta_{\ell,b,s},
\]
\[
 P_{\ell-1,a,k}=\eta^{(\ell)}_{a,k}
       +\sum_{b,s\le k}\mathsf D^{(\ell)}_{ak,bs}H_{\ell-1,b,s},
 \tag{19}
\]
\[
 \mathsf F^{(\ell)}_{ak,bs}
 =\mathsf C^{(\ell)}_{ak,bs}
  -\frac{2\alpha_su_{b,s}}m
        \mathbb E[H_{\ell-1,b,s}H_{\ell-1,a,k}],
\]
\[
 \mathsf D^{(\ell)}_{ak,bs}
 =\mathsf A^{(\ell)}_{ak,bs}
  -\mathbf1_{s<k}\frac{2\alpha_su_{b,s}}m
        \mathbb E[\delta_{\ell,b,s}\delta_{\ell,a,k}].
 \tag{20}
\]

The slot covariances are the corresponding source covariances `E[HH]`
and `E[delta delta]`. The frozen coefficients in (11) are bounded by
`sqrt(m)`; (8) and (13) bound all their source RMS norms by a common
fixed constant. Thus C.2's innovation, memory, and root bounds are
independent of the physical horizon, number of nodes, and label size
in `Y<=1`. They depend on the fixed finite dataset, which is allowed here.

For clarity, the response bounds needed from C.2 have the form

\[
 \sum_{b,s\le k}|\mathsf A^{(\ell)}_{ak,bs}|
          \le\mathfrak a_\ell,\qquad
 |\mathsf C^{(\ell)}_{ak,bs}|
          \le\mathfrak c_\ell\alpha_s/m.
 \tag{21}
\]

Let `J` be the common training-memory coefficient bound, put
`f_l=mathfrak c_l+J` for `l>=2` and `f_1=1`, and use
`N(U)=sup_(p>=2)||U||p/sqrt(p)`. Under (21), C.2's actual field
recurrences, with constants `K_0,C` fixed before the response caps, are

\[
 \mathcal N(H_{1,a,k})\le K_0+K_0S\sup_{b,s<k}\mathcal N(P_{1,b,s}),
\]
\[
 \mathcal N(H_{\ell,a,k})\le K_0+K_0f_\ell S
                              \sup_{b,s<k}\mathcal N(P_{\ell,b,s}),
\]
\[
 \mathcal N(P_{\ell,a,k})\le K_0+(\mathfrak a_{\ell+1}+JS)
                              \sup_{b,s\le k}\mathcal N(H_{\ell,b,s}),
\]
\[
 \mathcal N(w_k)\le K_0+K_0S\sup_{b,s<k}\mathcal N(H_{L,b,s}).
 \tag{22}
\]

These equations are where unbounded features matter: their subGaussian
norms are bootstrapped together with those of the backward carriers.
They cannot be replaced by the tanh bound `|H|<=1`.

Here are the derivative recurrences ensuring (21). For the sum `V_k`
of absolute derivatives of a forward field over its own forward slots,
maximized over the constructed prefix, and
`d_l=1+mathfrak a_(l+1)` (`d_L=1`),

\[
 V_k\le1+Cf_\ell\sum_{u<k}\alpha_u
       \left(d_\ell+\frac1m\sum_b|P_{\ell,b,u}|\right)V_u.
 \tag{23}
\]

For the derivative `D_k` produced by one fixed backward slot at `(b,s)`,

\[
 D_k\le Cf_{\ell-1}\alpha_s/m+
 Cf_{\ell-1}\sum_{u<k}\alpha_u
  \left(d_{\ell-1}+\frac1m\sum_a|P_{\ell-1,a,u}|\right)D_u,
 \quad k>s;\qquad D_k=0\ (k\le s).
 \tag{24}
\]

The pulse retains exactly `alpha_s/m`, including for the bottom first-layer
update. Discrete Gronwall uses only `sum alpha<=S`. For any family with
`N(P)<=B`, Jensen with weights `alpha_u/(m sum alpha)` gives

\[
 \mathbb E\exp\left(\lambda\sum_{u<k}\frac{\alpha_u}{m}
                     \sum_b|P_{\ell,b,u}|\right)
 \le\frac43\exp(2e\lambda^2S^2B^2).
 \tag{25}
\]

No temporal independence or maximum over Gaussian histories is involved.
Cauchy--Schwarz and (23)--(25) give exactly the cap-improvement estimates

\[
 \sum_{b,s\le k}|\mathsf A^{(\ell)}_{ak,bs}|
 \le C(B_{P,\ell}+d_\ell)
      e^{Cf_\ell S d_\ell+Cf_\ell^2S^2B_{P,\ell}^2},
\]
\[
 \frac{|\mathsf C^{(\ell)}_{ak,bs}|}{\alpha_s/m}
 \le Cf_{\ell-1}
      e^{Cf_{\ell-1}S d_{\ell-1}
          +Cf_{\ell-1}^2S^2B_{P,\ell-1}^2}.
 \tag{26}
\]

C.2 chooses the `mathfrak c` caps bottom to top, the `mathfrak a` caps
top to bottom, then `B_H=2K_0`, `B_(P,L)=2K_0` and
`B_(P,l)=4K_0(1+mathfrak a_(l+1))`, and finally a sufficiently small
`S_r>0`. All exponents in (26) are then below `log(2)`, and (22)
preserves the field caps. Current forwards are constructed bottom to top
using only earlier backward fields; current backwards are constructed
top to bottom using already constructed current upper coefficients.
This is the causal induction in C.2, unchanged when each step is
`alpha_s` instead of a constant mesh. Consequently, for
`S<=min(S_b,S_r)`, every stopped node has common bounds (7).
The forward preactivation conclusion follows from (19) and the first
update, and `delta` follows by the bounded slope multiplying `P`.
An affine interpolation state is one appended fractional Euler step,
so it enjoys the same marginal bounds.

For nonsmooth second derivatives in (2), use C.1's mollification argument.
Compactly supported convolution gives
`||phi_epsilon-phi||infinity<=C s_l epsilon`,
`||phi'_epsilon-phi'||infinity<=C j_l epsilon`, with uniform first and
second derivative bounds `s_l,j_l`. Values at zero increase by at most a
fixed multiple of epsilon. The constants and activity interval above are
therefore common to all sufficiently small smoothings. C.1's one-reference
comparison, including the displayed smoothing errors, passes the finite
programs and subsequently the flow to the original activation; Fatou
preserves the exponential-square bounds. Unit ELU and softsign require
this step; a classical second derivative everywhere is not assumed.

## 4. Excluding activity exit before constructing the flow

Let `J(theta)` denote the prediction differential from the canonical
mobility Hilbert space to sample RMS, so the gradient field is
`F(theta)=-2J(theta)^*r` and `Gamma=JJ^*`. On the tube, forward
differences are bounded by `C d`. The only unbounded product in backward
subtraction is handled against a stopped reference node by

\[
 \|[\phi_\ell'(Z)-\phi_\ell'(Z_k)]P_k\|_2
 \le j_\ell R\|Z-Z_k\|_2
       +2s_\ell\|P_k\mathbf1_{|P_k|>R}\|_2.
 \tag{27}
\]

The carrier difference is a readout difference at the top, or a bounded
operator applied to the next backward difference plus an operator
difference times a bounded-RMS reference field. Descending this recurrence
adds the cutoff term at each layer; it does not multiply successive
cutoff factors. The Jacobian blocks are the fixed-input/backward products,
`delta tensor H`, and `H_L`. Using (8), (13), the rank-one norm identity,
and (7) gives

\[
 \|J(\vartheta)-J(\theta_k)\|
 \le C\{(1+R)d(\vartheta,\theta_k)+e^{-cR^2}\}.
 \tag{28}
\]

Only the reference node supplies tails. In particular no tail estimate
for arbitrary points of the tube is being inferred from their RMS bounds.
Gate-product continuity also justifies integrating the prediction
differential along a parameter segment: the gate is bounded, continuous,
and tested against an `L2` carrier, as in C.1.

An Euler segment has length at most `Vh_k rho_k` in (5), so its exact
prediction increment is

\[
 r_{k+1}=(I-2h_k\Gamma_k)r_k+q_k,\qquad
 \|q_k\|_m\le h_k\rho_k\,\omega(h_k),
 \quad\omega(h)\longrightarrow0,
 \tag{29}
\]

where, with the fixed residual bound `Q=1+2M_L^2`, one may use
`omega(h)=C inf_(R>=1){(1+R)hQ+exp(-cR^2)}`. This is uniform
over all stopped programs and elapsed physical times. For
`h_k<=1/(2G)`, (17) bounds the first term's norm by
`(1-lambda_0 h_k)rho_k`. Choose a maximal physical mesh small enough
that `omega(h_k)<=lambda_0/2`; then

\[
 \rho_{k+1}\le(1-\lambda_0h_k/2)\rho_k,\qquad
 \sum_{k<j}h_k\rho_k
       \le\frac{2(\rho_0-\rho_j)}{\lambda_0}
       \le\frac{2Y}{\lambda_0}.
 \tag{30}
\]

Set `S=4Y/lambda_0` and choose `Y_*>0` such that this is at most
`min(1,S_b,S_r)`. First attainment of the activity cap contradicts (30),
including when a final physical step was truncated to reach it. Tube
exit was already excluded in Section 2. The finite Euler program therefore
extends to every prescribed physical horizon with constants independent
of that horizon. The only division by a residual has been at a nonzero
Euler node; zero nodes remain stationary.

## 5. Strong global construction and its all-time tails

Use C.1's joint generated action-space construction for countably many
sequences of these deterministic Euler programs on every positive integer
physical horizon, their finite unions, and the needed smoothings.
The deterministic adaptive coefficients do not affect consistency of the
finite programs or the inherited initialized operator/adjoint bounds.
For two meshes with maximal physical steps `h,h'` on a fixed `[0,T]`,
C.1's reference comparison, now using (28) and the global common ball,
gives

\[
 \sup_{t\le T}d(\theta^h(t),\theta^{h'}(t))
 \le C_Te^{C(1+R)T}
             \{(1+R)(h+h')+e^{-cR^2}\}.
 \tag{31}
\]

The same estimate holds in the stronger hidden-increment HS norm because
every increment is rank one and
`||U tensor V-U' tensor V'||HS<=||U-U'||2||V||2+
||U'||2||V-V'||2`. First send meshes to zero at fixed `R`, then send
`R` to infinity. The factor `exp(CRT-cR^2)` tends to zero for fixed
`T`. Completeness gives a limit. The bounded-gate continuity argument of
C.1 passes its integral equations to that limit; it is a strong solution.

The identical one-reference estimate proves uniqueness against any other
strong solution while it stays in a slightly larger tube. Only the
constructed solution supplies tails. First-exit continuation excludes
departure of an alternative solution, and solutions constructed for two
different horizons agree on their overlap. Thus there is one global flow.

The Gram gap survives the limit. Its exact residual equation is
`dot r=-2Gamma r`, hence

\[
 \dot\rho=-2\langle r,\Gamma r\rangle_m/\rho
        \le-\lambda_0\rho.
 \tag{32}
\]

For `Y>0`, the upper Gram bound also gives `rho(t)>=Ye^{-2Gt}>0`
on finite intervals, which justifies the division. Equations (17) and
(32) prove (6). Finite total variation in the complete spaces in (5)
gives the limiting parameter; forward continuity and `rho(t)->0`
give interpolation.

At each fixed time, preactivations, activations, full carriers, and backward
fields converge in `L2` along the Euler approximation. Almost-sure
subsequences and Fatou transfer their common exponential-square estimates
to the limit. The constants are independent of the chosen time.
The same argument at the parameter endpoint proves (7) for `t=infinity`.

If initialized-only carriers are desired, they too have subGaussian
population marginals. For example

\[
 (W_{\ell+1}(t)-W_{\ell+1,0})^*\delta_{\ell+1,a}(t)
 =-\frac2m\sum_b\int_0^t r_b(s)H_{\ell,b}(s)
       \mathbb E[\delta_{\ell+1,b}(s)\delta_{\ell+1,a}(t)]\,ds.
 \tag{33}
\]

Minkowski in every `Lp`, (7), bounded backward RMS, and finite activity
bound the `N` norm of this field. Subtracting it from full `P_l` gives
the initialized branch. In contrast to tanh, (33) is not in general
coordinatewise bounded, because its forward fields can be unbounded.
Downstream cutoff estimates should use full `P_l` directly. The learned
forward branch is handled in the same way using `delta` and `E[HH]`.

## 6. Qualitative finite-width transfer and one dense-only floor

Let `G_n` be the canonical finite initialization event with operator
norms at most a common `K`, first-preactivation RMS at most a common
`A_0`, and initial readout-feature Gram at least `lambda_0 I`.
Choose these constants with slack relative to the population bounds,
reducing the common `lambda_0` if needed. Gaussian operator concentration,
first-layer averaging, and `ACTIVATION_INITIAL_GRAM.md` imply
`Pr(G_n)->1`. A full gap need not hold for `n<m`; no all-width
initialization claim is made.

On `G_n`, the continuous finite dense flow obeys the same tube/activity
proof and exponential residual decay, with constants independent of width.
Its finite-dimensional vector field is locally Lipschitz under (2), and
bounded total variation on the tube gives continuation. These deterministic
facts require no trained Gaussian assertion.

Fix a finite `T`. Evaluate the fixed Gaussian oracle programs from Section
5 on the actual initialized arrays, and reconstruct their finite-rank proxy
parameters as in C.1. Fixed-program convergence controls every finite-list
node, scalar contraction, second moment, and continuous quadratic tail
majorant. The one-reference cutoff estimate (27) then transfers recomputed
backward fields as well as forwards, residuals, and vector fields.
Comparing the stopped actual finite flow to the proxy and choosing the
error below a larger tube's exit margin excludes that stop. For actual GD
the comparison includes its maximal step, exactly as in C.1.

The limit order is: choose a carrier cutoff, choose a sufficiently fine
fixed reference program, let width tend to infinity at that fixed program,
then refine the program and send the comparison cutoff to infinity.
Equivalently, in the displayed bounds take width first at fixed cutoff
and mesh, then mesh to zero, then cutoff to infinity. The Gaussian tail
beats `exp(C_T R)` on each fixed finite `T`. Thus the C.1 convergence
conclusions apply on every prescribed finite horizon. No numerical width
threshold is supplied by this argument.

Here is a direct reusable all-time consequence for full dense carriers.
For a finite dense GF path define, on `G_n`,

\[
 H_n(M,t)=\sum_{\ell=1}^L\max_a
 \frac{\|P_{\ell,a,n}^D(t)
          \mathbf1_{|P_{\ell,a,n}^D(t)|>M}\|_2}{\sqrt n},
 \qquad
 Z_n(M)=\int_0^\infty\rho_n^D(t)H_n(M,t)dt,
 \tag{34}
\]

and set `Z_n(M)=0` off `G_n`. The same conclusion holds if the finite
sum also includes any or all of `Z,H,delta`. Their RMS norms are uniformly
bounded on the tube, so `Z_n(M)<=C` independently of `n,M`.
There are constants `C_0,c>0` such that for every fixed `M>=1` and
`epsilon>0`,

\[
 \Pr\{Z_n(M)>C_0e^{-cM^2}+\epsilon\}\longrightarrow0.
 \tag{35}
 \]

This remains true if the finite sum includes mixed tails
`||U 1_(|V|>M)||RMS`, for any of these fields `U,V` belonging to
the same neuron population. It therefore includes forward/backward mixed
tails and readout/last-layer mixed tails, not only separate marginal
cutoffs. On the population side Cauchy--Schwarz gives
`||U 1_(|V|>M)||2 <= ||U||4 Pr(|V|>M)^(1/4)`, which is bounded
by `C exp(-cM^2)` using (7). No independence of `U,V` is needed.

To verify this without presuming empirical trained tails, first fix `T`.
For a scalar field use `g_M(v)=(|v|-M)_+`, which is 1-Lipschitz,
has at most linear growth, and obeys
`|v|1_(|v|>2M)<=2g_M(v)`. Its `L2` norm changes by at most the
RMS change in the field. Fixed-program convergence transfers its squared
empirical norm from each oracle node. One-reference carrier comparison
then transfers it to the actual finite dense path. A finite time grid,
the uniform parameter speed bound, and (27) against its reference nodes
make the time interpolation error arbitrarily small. The population
bound (7) controls the limiting cutoff norms by `C exp(-cM^2)`;
halving `M` only changes `c`. Prediction convergence similarly transfers
the residual weight on `[0,T]`. This proves the bound for the compact
time integral in the same ordered limits just specified.

For the mixed-tail version, a continuous cutoff majorizing
`U^2 1_(|V|>M)` and vanishing at `|V|<=M/2` has at most quadratic
growth in the joint same-population tuple. Fixed-program convergence
therefore applies. To transfer from reference fields `U_*,V_*` to actual
fields `U,V`, split the event `|V|>M` into `|V_*|>M/2` and
`|V-V_*|>M/2`, write `U=(U-U_*)+U_*`, and on the second event split
`U_*` at a separate cutoff `R`. The resulting bound is
`||U-U_*||RMS + ||U_* 1_(|V_*|>M/2)||RMS
+ (2R/M)||V-V_*||RMS + ||U_* 1_(|U_*|>R)||RMS`.
First take the reference comparison error to zero at fixed `M,R`, then
send `R` to infinity. This proves mixed-tail transfer without tails for
the actual finite fields. The deterministic late-time argument below is
unchanged because a mixed tail is bounded by the RMS norm of `U`.

For the late interval, the deterministic finite RMS and residual bounds give
`integral_T^infinity rho_n^D H_n<=C exp(-lambda_0 T)` on `G_n`,
uniformly in `n,M`. Choose `T` after the desired error tolerance and before
the fixed-program width limit. This proves (35), with Gaussian constants
independent of the physical horizon. It uses neither a growing transcript
nor a growing cutoff in the fixed-program theorem.

For integer `M>=1` define

\[
 a_n=\sup_{M\in\mathbb N,\ M\ge1}
       \bigl(Z_n(M)-C_0e^{-cM^2}\bigr)_+.
 \tag{36}
\]

This is bounded, measurable, and depends solely on the dense flow and
initialized arrays. It obeys `a_n->0` in probability and, simultaneously
in integer cutoff,

\[
 Z_n(M)\le C_0e^{-cM^2}+a_n.
 \tag{37}
\]

Indeed, for a target tolerance choose a fixed integer `J` making the
Gaussian term at `J` smaller than half that tolerance. Since `Z_n` is
nonincreasing, every excess with `M>=J` is at most `Z_n(J)`, which
is small with probability tending to one by (35). For the finitely many
`M<J`, use (35) and a finite union bound. No quantitative uniform-cutoff
theorem is needed. This is the full-carrier replacement for the tanh-only
initialized-branch floor in `SLOW_ORDER_UNIFORM_BOUND.md`.

## 7. Scope of the activation extension

All constants in Sections 2 and the continuous finite fitting bootstrap
use only activation values at zero and bounded slopes. The all-time
Gaussian population construction also needs the globally bounded
derivative-Lipschitz constants in two specific places: the response
derivative rows (23)--(26) and the linear cutoff modulus (27).

If `phi_l'` is only locally Lipschitz, a radius-dependent
`ell(R)=max_l Lip(phi_l';[-R,R])` cannot silently replace `j_l` by a
fixed constant. Smoothing/truncating outside a growing radius can make
the C.2 activity interval shrink to zero. The product-rule coefficient
in (23) becomes `|phi_l''(Z)| |P|`; bounded slope by itself gives no
integrability bound for this product or its time-integrated exponential.
Likewise simultaneous preactivation and carrier clipping introduces the
growth of `ell(R)` into the reference comparison. Nothing in the present
assumptions controls that growth.

For example the smooth function
`phi(x)=integral_0^x sin(exp(u^4))du` has bounded slope but extremely
large curvature `4x^3 exp(x^4)cos(exp(x^4))`. Its curvature is not
absolutely integrable against a nondegenerate centered Gaussian density:
on the positive half-line the substitution `v=exp(x^4)` turns that
absolute-curvature integral into a constant times
`integral_1^infinity |cos(v)| exp(-c sqrt(log(v)))dv`, which diverges.
This diagnoses failure of a required derivative-moment estimate, not
failure of a trained-flow theorem for this particular activation.

Thus the verified result here is the global derivative-Lipschitz class
(2). Extending the Gaussian conclusion to a larger local-regularity
class needs an additional response/moment argument with an explicit
modulus; the existing deterministic finite-width theorem alone does
not supply it. Exact ReLU and leaky ReLU are outside (2) for the separate
reason that their derivatives jump.

The result supplies the dense Gaussian input for the autonomous old-clock
closure comparison while preserving correlated finite data, canonical
Gaussian actions and their adjoints, unbounded activations, and learned
hidden matrices. It does not prove the closure's source approximation or
feedback estimate; those are separate deterministic obligations. In
particular no population Gaussian statement was assigned to the closure
or to actual finite trained arrays without the fixed-program transfer in
Section 6.

## 8. Scoped check of the combined candidate

At the supervisor's subsequent request, I read the complete
`ACTIVATION_NEAR_QUADRATIC_ALLTIME.md` at SHA-256
`30d0eb49d29e09fe372a9ac1c9dcf5b267c401f6d54d2c23846c14f967ae8207`.
The assigned check covered its Section 4 Gaussian bridge, Sections 2 and 5
whole-input prediction transfer, and compatibility of hypotheses and
quantifiers. Its deterministic near-quadratic calculation was treated as
a separately checked premise; I did not read an additional route or open
a new research direction. This is a scoped author cross-check, not a
fresh independent promotion review.

The full-carrier bridge agrees with Sections 1--6 above: it includes the
readout, uses the canonical Gaussian law only through deterministic
population reference programs, excludes the activity stop before taking
the flow limit, and transfers fixed cutoffs to actual dense GF before
using the deterministic remaining-activity bound. Its integer-cutoff
supremum yields a vanishing dense-only remainder. I reported that it
should explicitly set `Z_n(M)=0` off `G_n`, making that random quantity
defined and bounded on the whole probability space.

The prediction extension is valid with the following explicit details.
Include the high-probability bound
`||W_1(0)||F/sqrt(n)<=C` in the common event `G_n`; the training-only
preactivation bound does not imply it when the inputs do not span the
input space. Canonical Gaussian initialization with fixed `d` supplies
this extra bound. Uniform first-layer displacement then bounds the full
first-layer norm throughout dense and every closure path. For
`v=||x||/sqrt(d)`, linear growth and bounded slopes give, through fixed
depth, both

\[
 \|h_\ell(t,x)\|_{\rm RMS}\le C(1+v),\qquad
 \|\widehat h_\ell(t,x)-h_{\ell,D}(t,x)\|_{\rm RMS}
       \le C(1+v)d_n(t).
 \tag{38}
\]

The finite readout pairing and its bounded RMS imply the candidate's
prediction discrepancy bound `C(1+v)D_n(q)`. The same bounds hold in
population spaces. Bounded slopes, bounded operators and the full
first-layer norm also give a uniform Lipschitz constant in `x` on all
these predictor paths.

For population test predictions, include the first Gaussian row's `d`
coordinates and countably many rational passive test inputs in the
generated action spaces. Each finite test set is an admissible collection
of correctly typed forward probes in C.1; no test residual is inserted
into training. Its finite-dimensional root tuple is still subGaussian.
The joint finite-program construction is consistent under deleting these
probes. The uniform input Lipschitz constant then identifies their common
extension to every real input and upgrades finite-test convergence to
uniform convergence on each bounded input domain, on a fixed physical
time interval, by a finite input net.

Both dense finite and dense population paths have remaining parameter
variation at most `C exp(-kappa T)`. By (38), their prediction variation
after `T` is at most `C(1+v)exp(-kappa T)`. Splitting at `T` therefore
extends compact-domain convergence to the whole physical half-line.
For a test law with finite second input moment, split the input integral
at `||x||<=R`: the bounded-domain part converges in probability and the
outside part of the squared all-time error is bounded by

\[
 C\int_{\|x\|>R}(1+\|x\|/\sqrt d)^2\,\mu(dx)
          \longrightarrow0.
 \tag{39}
\]

This proves the required dense-only remainder for the norm with time
supremum *inside* the test-input integral; no interchange of time
supremum and integral is assumed. Add this remainder to the deterministic
closure/dense bound to obtain the candidate's (7), and use a bounded
domain supremum to obtain its (8). The remainder is independent of
closure order. The RMSE comparison follows by the reverse triangle
inequality at each time.

The global parameter and residual bounds give the same compact-domain
equicontinuity and uniform remaining-time modulus for each fixed closure
order. They yield subsequential predictor limits (or weak subsequential
limits of their laws), and the vanishing width remainder transfers the
order bound to every such limit. I recommended explicitly describing
these limits as possibly random unless deterministic identification is
proved separately. No uniqueness of a fixed-order population moment ODE
or full-sequence predictor limit follows from compactness alone.

Subject to these precision edits, the checked Gaussian and prediction
bridges contain no further missing input. The theorem's fixed finite
depth/data, fixed small positive labels, exactly zero readout, Gaussian
initialization, global derivative-Lipschitz class, and qualitative width
quantifiers are consistent throughout the frozen candidate.
