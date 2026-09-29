# Explicit finite-time constants: scoped proof check

28 September 2026. Scientific input: the complete
`ACTIVATION_UNIT_LABEL_FINITE_TIME.md` only. This is a sufficient-bound
derivation for that theorem, not an optimality claim or a promoted result.
The original closure, its clock, and its initialization are unchanged.

## 1. What is meaningful to bound

Write

\[
 U=1+\sqrt T,\qquad \gamma=\sqrt n\,\ell_{n,T},\qquad s=1+\gamma.
\]

Constants denoted by `C` below depend only on the fixed inputs, depth,
initial bounds, and activation values/slopes in the input theorem. They
do not depend on `T,n,P`, labels, initialization within the stated bounds,
or the local gate modulus. Different occurrences can have different
values; one sufficiently large fixed constant makes the final displayed
choices valid. The preactivation radius may be chosen as `R_T=C U^L`.

A useful separated bound is

\[
 \int_0^t e_E(v)\,dv
 \le A(T)\left[B_0P^{-3/2}+sP^{-2}\right],
 \qquad
 A(T)=C U^{3L+4},                                                     \tag{1}
\]

and

\[
 d_n(t)\le A(T)e^{D(T,\gamma)}
       \left[B_0P^{-3/2}+sP^{-2}\right],
\qquad
 D(T,\gamma)=C T\left[U^{L-1}+\gamma U^{2L-1}\right].                   \tag{2}
\]

These estimates initially hold on an additional relative-defect and
narrow-tube stopping interval. Section 5 gives explicit sufficient orders
which close both stopping conditions. The stronger separated version of
(1) has prefactors `C U^(L+1)` for its `B_0 P^(-3/2)` term and
`C U^(3L+4)` for its `s P^(-2)` term. These powers are sufficient bounds;
their minimality is not claimed.

The coefficient of `1/P` by itself has no invariant best time growth:
the theorem also permits changing the sufficient order threshold. In
fact, the threshold below yields `d_n<=2/P`, with the entire time cost
paid in the threshold. Equations (1) and (2) expose the costs before this
reparameterization.

## 2. A narrow tube and a relative-defect bootstrap

The radius-one region of the input proof gives

\[
 D,B,A\le C U,\qquad M_j\le C U^j,\qquad
 \beta_j\le C U^{L-j+1},\qquad R_T\le C U^L.                            \tag{3}
\]

Forward differentiation in the mobility norm gives, uniformly on this
convex region,

\[
 \max_a\frac{\|Dz_{j,a}[v]\|_2+\|Dh_{j,a}[v]\|_2}{\sqrt n}
       \le C U^{j-1}|v|_n,
 \qquad \|Df[v]\|_m\le C_J U^L|v|_n.                                  \tag{4}
\]

For the first inequality, the first layer is bounded by the fixed input
norm; at layer `j` the matrix increment acts on a feature of size
`C U^(j-1)`, and the preceding increment is propagated by an operator of
size `C U`. The readout adds its increment times `h_L` and `w` times the
feature increment, both bounded by the second expression in (4).

Set

\[
 r_T=c U^{-L},\qquad 0<c\le\min\{1,(2C_J)^{-1}\},
\]

and set `epsilon_T=(1+C_J T U^L)^(-1)`, enlarging `C_J` to bound the
prediction differential on the region if necessary. Stop when either
`d_n=r_T`, `e_E/rho=epsilon_T`, or the raw closure reaches
its maximal existence time. If the initial residual is zero the original
proof gives an equilibrium, so suppose `eta=rho(0)>0`. Initially the
forward histories are constant and their endpoint projection errors
vanish, hence `e_E/rho=0`. On this stopped interval, the loss decrease of
the dense flow and (4) give

\[
 \rho\le Q_0+C_J U^Lr_T\le Q_0+1=:Q_1,
 \qquad \tau\le1+Q_1T\le C U^2.                                      \tag{5}
\]

The same residual bound holds along the parameter segment joining the
dense and closure points at every fixed time.

Each canonical velocity block has mobility norm at most `C U^L rho`:
for hidden links the relevant product is
`beta_j M_(j-1)<=C U^L`, and the first layer and readout satisfy the same
bound. The relative-defect stopping condition, which in particular gives
`e_E/rho<=1`, therefore implies

\[
 |\dot\theta|_n\le C U^L\rho,
 \qquad
 \max_a\frac{\|\dot h_{j,a}\|_2+\|\dot z_{j,a}\|_2}{\sqrt n}
       \le C U^{L+j-1}\rho,
 \qquad \|\dot r\|_m\le C U^{2L}\rho.                                \tag{6}
\]

The raw solution cannot reach a zero-residual equilibrium at a finite
interior time, by the local uniqueness argument in the input proof.
Thus, with a fixed sufficiently large `C` and
`V=exp(C T U^(2L))`,

\[
 V^{-1}\eta\le\rho(t)\le V\eta,\quad
 \int_0^t\rho\,dv\le T V\eta,\quad
 \int_0^t\rho^{-1}\,dv\le T V/\eta,\quad
 \|\dot c\|_m\le C U^{2L},\qquad c=r/\rho.                           \tag{7}
\]

The last bound follows from
`dot c=dot r/rho-r dot rho/rho^2` and
`|dot rho|<=||dot r||_m`.

## 3. Tail and endpoint estimates with explicit powers

For a link `j=2,...,L`, the forward history in the link is `h_(j-1)`.
Its normalized clock derivative energy, using `d xi=rho dt`, satisfies

\[
 \left(\frac1{mn}\sum_a\int_0^\tau
              \|\partial_\xi h_{j-1,a}\|_2^2d\xi\right)^{1/2}
 \le C\sqrt T\,U^{L+j-2}V^{1/2}\sqrt\eta.                            \tag{8}
\]

The readout equation and (7) imply

\[
 \frac{\|w(t)\|_2}{\sqrt n}\le B_0+C T U^L V\eta,
 \qquad
 \max_a\frac{\|\delta_{j,a}\|_2}{\sqrt n}
     \le C U^{L-j}(B_0+T U^L V\eta).                                  \tag{9}
\]

Differentiating backpropagation along an absolutely continuous parameter
curve gives

\[
 \max_a\frac{\|D\delta_{j,a}[v]\|_2}{\sqrt n}
 \le C\left[U^{L-j}+\gamma U^{2L-j}\right]|v|_n.                      \tag{10}
\]

Here a gate variation at layer `k>=j` contributes at most the product of:
the propagated operator factor `C U^(k-j)`, the full carrier supremum
bound `C sqrt(n) U^(L-k+1)`, the local gate modulus, and the preactivation
increment RMS `C U^(k-1)|v|_n`. Its total power is
`U^(L+k-j)<=U^(2L-j)`. The non-gate terms have power `U^(L-j)`.
This argument uses the almost-everywhere chain rule for a Lipschitz gate
on its compact preactivation range, so a classical second derivative at
every scalar point is unnecessary. Combining (6) and (10) gives

\[
 \max_a\frac{\|\dot\delta_{j,a}\|_2}{\sqrt n}
       \le C s U^{3L-j}\rho.                                        \tag{11}
\]

For `b_a=c_a delta_(j,a)`, (7), (9), (11), and
`eta<=V rho` consequently imply

\[
 \left(\frac1{mn}\sum_a\|\dot b_a\|_2^2\right)^{1/2}
 \le C U^{3L-j}(1+T U^L)V^2(B_0+s\rho).                              \tag{12}
\]

For example, the only term requiring the conversion `eta<=V rho` is
`C T U^(4L-j) V eta`, coming from `dot c` times the accumulated readout.
The fixed sample count absorbs `max_a|c_a|<=sqrt(m)`.

The initial backward jump has RMS amplitude at most `C B_0`: its
backpropagation uses the initial operator bound `K`. Subtract that jump
times `1_[1,tau]` and call the continuous remainder `tilde b`. From (7)
and (12),

\[
 \left(\frac1{mn}\sum_a\int_0^\tau
                  \|\partial_\xi\widetilde b_a\|_2^2d\xi\right)^{1/2}
 \le C\sqrt T\,U^{3L-j}(1+T U^L)V^{5/2}
                  (B_0/\sqrt\eta+s\sqrt\eta).                       \tag{13}
\]

There is a useful improvement over the bounded-history endpoint estimate
in the input proof. For the step `g=1_[1,tau]`, put `a=1/tau`. Integration
of its endpoint kernel gives exactly, for `tau>1`,

\[
 g(\tau)-(\Pi_Pg)(\tau)
       =\tfrac12[p_P(a)+p_{P-1}(a)],\qquad
 |g(\tau)-(\Pi_Pg)(\tau)|\le1.                                      \tag{14}
\]

Indeed the kernel is `(p_P'+p_(P-1)')/2`, its integral over `[a,1]` is
`1-[p_P(a)+p_(P-1)(a)]/2`, and `|p_k|<=1`. At the initial endpoint the
same bounded right-limit convention applies, and the forward endpoint
error is zero. The normalized `L^2` tail of this step remains at most
`C sqrt(tau/P)`, as in the input proof.

For brevity define the two coefficients appearing in (8), (13), without
their residual factors,

\[
 a_j=C\sqrt T\,U^{L+j-2}V^{1/2},\qquad
 b_j=C\sqrt T\,U^{3L-j}(1+T U^L)V^{5/2}.
\]

The supplied polynomial estimates, (8), (13), and (14) yield forward and
backward endpoint errors `E_h,E_b` and normalized tails `Q_h,Q_b` with

\[
 E_h\le\sqrt\tau\,a_j\sqrt\eta/\sqrt P,
 \qquad E_b\le C B_0+\sqrt\tau\,b_j(B_0/\sqrt\eta+s\sqrt\eta)/\sqrt P,
\]
\[
 Q_h\le\tau a_j\sqrt\eta/P,
 \qquad Q_b\le C\sqrt\tau B_0/\sqrt P
           +\tau b_j(B_0/\sqrt\eta+s\sqrt\eta)/P.                    \tag{15}
\]

The exact defect identity bounds `e_E/rho` by twice the sum of `E_h E_b`;
the exact integrated identity bounds `integral e_E` by twice the sum of
`Q_h Q_b`. Since

\[
 a_jb_j=C T U^{4L-2}(1+T U^L)V^3,
\]

the residual denominators cancel in both products. Using
`eta<=Q_0`, `B_0<=1`, `s>=1`, `tau<=C U^2`, and `T<=U^2` gives

\[
 \frac{e_E}{\rho}
 \le C U^{5L+4}V^3
                  [B_0P^{-1/2}+sP^{-1}],
\qquad
 \int_0^t e_E\,dv
 \le C U^{5L+6}V^3
                  [B_0P^{-3/2}+sP^{-2}].                            \tag{16}
\]

For instance, the continuous-tail product contains
`tau^2 T U^(4L-2)(1+T U^L)`, bounded by `C U^(5L+6)`;
the continuous endpoint product has one fewer factor of `tau` and gives
`C U^(5L+4)`. The jump products have smaller powers. Absorbing the fixed
factor three in `V^3` into its exponent gives the preliminary endpoint
coefficient `A_end(T)=C U^(5L+6) exp(C T U^(2L))` and the convenient bound

\[
 e_E/\rho\le A_{\rm end}(T)[B_0P^{-1/2}+sP^{-1}].                    \tag{17}
\]

All these bounds are uniform as `eta` tends to zero through positive
values. The zero case was handled before division. The exponential
coefficient in (17) will close the relative-defect bootstrap. It is not
necessary in the accumulated source bound, as the next argument shows.

The squared-loss structure gives an upper bound on residual growth
without its canonical negative term. In mobility coordinates, with `J`
the prediction Jacobian, the perturbed residual equation is
`dot r=-2 J J^* r+J E`, where adjoints use sample RMS and mobility inner
products. Thus

\[
 \dot\rho\le\|J\|\,|E|_n
       \le C_J U^L\epsilon_T\rho,
 \qquad \rho(u)\le e\,\rho(v)\quad(0\le v\le u\le T).               \tag{17a}
\]

The last inequality follows because
`C_J U^L epsilon_T T<=1`. In particular,

\[
 \frac{\tau(t)-\tau(v)}{\rho(v)}
       =\frac{\int_v^t\rho(u)du}{\rho(v)}\le eT.                    \tag{17b}
\]

Retain the weight in the Legendre derivative inequality from the input
proof instead of replacing it by its maximum. On `[0,tau(t)]` it gives

\[
 \|(I-\Pi_P)g\|_{L^2}^2
 \le\frac1{P(P+1)}\int_0^{\tau(t)}
               \xi(\tau(t)-\xi)\|g'(\xi)\|^2d\xi.                 \tag{17c}
\]

For the continuous backward remainder, substitution `xi=tau(v)` and
(17b) bound its right-hand integral by

\[
 \int_0^t
  \frac{\tau(v)[\tau(t)-\tau(v)]}{\rho(v)}
             \|\dot b(v)\|^2dv
 \le C U^2 T\int_0^t\|\dot b(v)\|^2dv,                             \tag{17d}
\]

where every norm in this formula is the sample/neuron RMS norm. Using
the simpler region bounds (3), (5), (7), and (11), rather than (12),
gives `||dot b||<=C s U^(3L-j+1)`: the `dot c` term is bounded by
`C U^(2L) U^(L-j+1)`, and the backward derivative term by
`C s U^(3L-j) rho<=C s U^(3L-j)`. Therefore

\[
 Q_b\le C\left[
       B_0 U P^{-1/2}+s U^{3L-j+4}P^{-1}\right].                    \tag{17e}
\]

Indeed, taking the square root in (17d) supplies `C U T`, which is at
most `C U^3`, times the stated bound on `dot b`; the jump contribution
still uses `sqrt(tau/P)<=C U/sqrt(P)`.

For the forward tail, one can improve on the pointwise-speed estimate by
using physical loss dissipation. On the closure, in mobility coordinates,

\[
 \dot{\mathcal L}=-|F|_n^2-\langle F,E\rangle_n
       \le-\tfrac12|F|_n^2+\tfrac12|E|_n^2,
 \qquad
 \int_0^t|E|_n^2dv\le Q_1^2 T\epsilon_T^2\le C.
\]

The last bound is uniform in `T`, since `U>=1` and
`T/(1+C_J T U^L)^2<=T/(1+C_J T)^2<=1/(4C_J)`; take `C_J>=1`.
Integrating the loss inequality and using nonnegativity of the loss
gives `integral |F|_n^2<=2Q_0^2+integral |E|_n^2`. Therefore

\[
 \int_0^t|\dot\theta|_n^2dv
       \le2\int_0^t(|F|_n^2+|E|_n^2)dv\le C.
\]

Apply the weighted inequality (17c) to the forward history as well.
Equation (17b) and the differential bound (4) give

\[
 \int_0^{\tau(t)}\xi(\tau(t)-\xi)
           \|h_{j-1}'(\xi)\|_{\rm RMS}^2d\xi
 \le C U^2T\int_0^t\|\dot h_{j-1}(v)\|_{\rm RMS}^2dv
 \le C U^2T U^{2j-4}\int_0^t|\dot\theta|_n^2dv
 \le C U^{2j}.
\]

Thus `Q_h<=C U^j/P`. Multiplication in the exact integrated defect
bound yields the improved polynomial source

\[
 \int_0^t e_E(v)dv
 \le C\left[
     B_0 U^{L+1}P^{-3/2}+s U^{3L+4}P^{-2}\right].                  \tag{17f}
\]

This proves the polynomial source bound (1). The weight in (17c) is
essential to this improvement: it matches the remaining clock interval
against the instantaneous residual in (17b), avoiding an inverse
residual comparison in the final accumulated source.

## 4. One-sided propagation improves the stability exponent

The mobility norm is Euclidean after a fixed linear rescaling of the
parameter blocks. In those coordinates the canonical vector field is
the negative gradient of the loss. This allows its positive semidefinite
prediction-Jacobian contribution to be discarded in an upper bound for
the growth of a difference.

Let `theta(u)=theta_D+u v`, `0<=u<=1`, be a joining segment at a fixed
physical time, with `|v|_n=d_n`. The first derivatives satisfy (4).
The second derivatives along this scalar segment exist almost everywhere
and obey

\[
 \max_a\frac{\|h_{j,a}''(u)\|_2}{\sqrt n}
 \le C[U^{j-2}+\gamma U^{2j-2}]|v|_n^2\quad(j\ge2),
 \qquad
 \max_a\frac{\|h_{1,a}''(u)\|_2}{\sqrt n}
       \le C\gamma |v|_n^2.                                        \tag{18}
\]

To verify this, differentiating `z_j=W_j h_(j-1)` twice gives
`z_j''=2v_(W_j)h_(j-1)'+W_j h_(j-1)''`. The non-gate terms have RMS
bound `C U^(j-2)|v|_n^2`. The gate term is bounded by

\[
 \ell_{n,T}\frac{\|(z_j')^2\|_2}{\sqrt n}
 \le\ell_{n,T}\sqrt n
             \left(\frac{\|z_j'\|_2}{\sqrt n}\right)^2
 \le C\gamma U^{2j-2}|v|_n^2.
\]

Propagation of the preceding gate term contributes
`C gamma U^(2j-3)|v|_n^2`, no larger than the displayed term. The readout
second derivative is `2v_w^T h_L'/n+w^T h_L''/n`, hence

\[
 \max_a|f_a''(u)|
 \le C[U^{L-1}+\gamma U^{2L-1}]|v|_n^2.                             \tag{19}
\]

These statements follow by differentiating the locally Lipschitz first
derivative along the segment, not by assuming a globally classical
Hessian. At points where a scalar gate is nondifferentiable the
almost-everywhere Lipschitz chain-rule bound is sufficient.

Put `g(u)=||f(theta(u))-y||_m^2`. The residual on the joining segment
is bounded by `Q_1` from (5). Consequently, almost everywhere,

\[
 g''(u)=2\|f'(u)\|_m^2+2\langle r(u),f''(u)\rangle_m
 \ge-C[U^{L-1}+\gamma U^{2L-1}]|v|_n^2.
\]

Integration in `u`, using `F=-grad L` in mobility coordinates, gives

\[
 \langle v,F(\widehat\theta)-F(\theta_D)\rangle_n
 \le C[U^{L-1}+\gamma U^{2L-1}]d_n^2.                                \tag{20}
\]

The perturbed-flow identity therefore implies
`d_n'<=C[U^(L-1)+gamma U^(2L-1)]d_n+e_E` wherever `d_n>0`;
the integrated inequality at zero follows by regularizing the norm.
Multiplication by the corresponding exponential integrating factor and
use of (1) prove (2). A two-sided vector-field Lipschitz estimate would
instead give the valid but weaker factor `exp(C T s U^(2L))`.

## 5. An explicit joint threshold and continuation

Choose

\[
 H=\max\{4A_{\rm end}(T)/\epsilon_T,\ 4/r_T,\ A(T)e^{D(T,\gamma)},\ 1\},
 \qquad
 P\ge\max\{B_0^2H^2,\ sH\}.                                        \tag{21}
\]

Then (17) yields `e_E/rho<=2A_end/H<=epsilon_T/2`. Multiplying (2) by `P` and using
the two order inequalities gives `d_n<=2/P`; since `P>=sH>=4/r_T`, this
is at most `r_T/2`. Both stopping conditions are thus excluded by
continuity. Physical parameters and the clock are bounded; each of the
finitely many moment vectors is an integral of a bounded finite-width
history against a polynomial of absolute value at most one. The entire
raw state remains bounded with `tau>=1`, so local existence extends the
solution through `T`. This is exactly the continuation mechanism in the
input proof, now closing both bootstrap conditions.

The explicit factor in (21) satisfies

\[
 \log H\le C\left[1+\log U+T U^{2L}
                          +T\gamma U^{2L-1}\right].                 \tag{22}
\]

No property `H>=s` is needed for (21). If one wants the original theorem's
form `H=exp(Lambda_T s)`, the choice

\[
 \Lambda_T=C[1+\log U+T U^{2L}]                                     \tag{23}
\]

dominates all terms in (21), and can also ensure `H>=s`. The original
joint threshold then gives `d_n<=2/P`, so its normalized error coefficient
can be chosen as `C_T=1` with this enlarged threshold. Alternatively,
to retain the polynomial source coefficient explicitly, use
`H_0=max{4A_end/epsilon_T,4A(T)/r_T,exp(D),1}` in the same order threshold.
Then `d_n<=2A(T)/P`, both bootstraps still close, and the explicit
choice in the original notation is `C_T=C U^(3L+4)`. These are different
parameterizations of a sufficient theorem, not competing optimality
statements. Both thresholds obey the logarithmic upper bound (22).

For globally Lipschitz gates with `ell_(n,T)<=J`, a sufficient
logarithmic-order scale obtained from (21), for `T>=1`, is

\[
 \log P\ \ge\ C\left[T^{L+1}
                    +J\sqrt n\,T^{L+1/2}+1\right]
                  +\log(1+J\sqrt n),                               \tag{24}
\]

where `C` also absorbs the factor two needed for the `B_0^2H^2` term.
For merely local gates, use their actual modulus on `[-C U^L sqrt(n),
C U^L sqrt(n)]`; the activation assumptions impose no universal growth
rate on that modulus as the interval expands.

## 6. A check on the original broader stopping argument

Even without the extra bootstrap, the original proof need not produce a
double exponential. In its radius-one region it has
`tau<=C U^(L+3)`. Direct induction in its forward-energy recurrence gives

\[
 Z_j^*\le C U^{(4L+6)j-L-3}.
\]

The endpoint estimates then give
`e_E/rho<=C U^(2L^2+L-2)`. Combining this with the prediction differential
bound `C U^L` shows
`|dot rho|/rho<=C U^(2L^2+2L-2)`. Its residual comparison therefore costs
only `exp(C T U^(2L^2+2L-2))`, and subsequent operations in the source
bound are products, powers, and fixed-length integrals. The much smaller
exponential needed in the preliminary endpoint estimate (17) comes from
the stronger stopping argument. The final polynomial source coefficient
(1) additionally uses the weighted-tail argument; neither step treats an
already exponential constant as a Gronwall rate.

None of these upper bounds proves that exponential time growth, the
powers of time displayed here, or the order threshold are necessary.
