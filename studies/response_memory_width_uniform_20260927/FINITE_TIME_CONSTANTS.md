# What is stronger, and how the finite-time constants grow

28 September 2026. This answers the follow-up to
`ACTIVATION_UNIT_LABEL_FINITE_TIME.md`. It continues the same canonical
old-clock investigation. The statement below sharpens the time bookkeeping
using a small relative-defect bootstrap and the weighted Legendre bound.
It concerns actual autonomous closure trajectories. No paper/book edit,
experiment, or external literature input is involved.

## 1. Comparison with the current paper

The current `paper/main.tex` learning-speed theorem (near line 402) allows
any `C^{1,1}_loc` activation, arbitrary finite initialization/data/labels,
and fixes width. Its constants may depend on width. It proves the order
`P^-1` estimate for all sufficiently large orders; if activation values and
slopes are globally bounded it proves it for every order. Its joint-clock
theorem additionally proves `P^-2` at fixed width under extra smoothness.

The new result adds explicit uniform control over families of widths under
uniform initial bounds, bounded activation slopes, and a specified joint
order/width condition. It also sharpens the old-clock source tail to
`B_0 P^-3/2+s_(n,T) P^-2`. It does not subsume every paper result:

- Local smoothness alone in the paper permits unbounded slopes. The new
  width estimates require globally bounded slopes.
- The paper allows each arbitrary finite initialization; the new constants
  are uniform over a family with fixed normalized initial bounds.
- The new width-uniform parameter metric normalizes the first layer and
  readout by `sqrt(n)` while retaining ordinary Frobenius distance in the
  middle layers. It is not the paper's full unnormalized Euclidean metric.
- The new statement concerns the old clock and does not replace the paper's
  joint-clock theorem.
- Its joint order can grow exponentially with `sqrt(n)`. It does not prove
  the paper's fixed-order population-closure conjecture or efficient
  large-width rank reduction.

On the overlapping hypotheses it is a quantitative improvement in width
control and source approximation. Calling it universally stronger would
hide the preceding distinctions. The bound on label RMS can be any fixed
finite constant, not only one; it is not a perturbative small-label condition.

## 2. A constant and an order threshold must be reported together

A statement `error<=C_T/P` only for `P>=P_0(T,n)` has two quantitative
outputs. Since the actual source estimate has powers strictly better than
`P^-1`, increasing `P_0` can absorb any given prefactor. One could make the
displayed `C_T` equal to one by paying in the order threshold. That is not
an all-time theorem and is not an intrinsic improvement of complexity.

The meaningful report therefore keeps the source factor, amplification,
and sufficient order separate. A useful explicit choice is given next.
The powers below are proved upper bounds, not optimality claims.

## 3. Explicit bounds

Retain exactly the deterministic setting of
`ACTIVATION_UNIT_LABEL_FINITE_TIME.md`: fixed `L>=2,m,d`, fixed finite
inputs, globally bounded slopes and locally Lipschitz derivatives,
uniform initial middle-operator and first-training-preactivation RMS bounds,
`Y<=1`, and `B_0=||w_0||_2/sqrt(n)<=1`. The discrepancy is

\[
 d_n^2=\|\widehat W_1-W_{1,D}\|_F^2/n+
       \sum_{\ell=2}^L\|\widehat W_\ell-W_{\ell,D}\|_F^2+
       \|\widehat w-w_D\|_2^2/n.
\]

Let `U=1+sqrt(T)`. The physical tube in that proof has preactivation RMS
at most `C U^L`. Take its actual radius `R_T` and define

\[
 \gamma_{n,T}=\sqrt n\max_\ell\operatorname{Lip}
  (\phi_\ell';[-R_T\sqrt n,R_T\sqrt n]),
 \qquad s_{n,T}=1+\gamma_{n,T}.
 \tag{1}
\]

Constants denoted `C` below depend on the fixed problem and initialization
bounds and global slopes, but not on `T,n,P` or the local gate modulus.
There is such a constant for which define

\[
 A_T=C U^{3L+4},\qquad
 B_{n,T}=C T\{U^{L-1}+\gamma_{n,T}U^{2L-1}\},
 \tag{2}
\]
\[
 H_{n,T}=\exp\!\left(C\left[
 1+\log U+\log(1+\gamma_{n,T})+
 T U^{2L}+T\gamma_{n,T}U^{2L-1}\right]\right).
 \tag{3}
\]

Increasing the fixed `C` in (3) if necessary, every integer

\[
 P\ge\max\{B_0^2H_{n,T}^2,\ s_{n,T}H_{n,T}\}
 \tag{4}
\]

gives closure continuation through `T` and

\[
 \sup_{t\le T}d_n(t)
 \le A_T e^{B_{n,T}}
     \left(\frac{B_0}{P^{3/2}}+\frac{s_{n,T}}{P^2}\right)
 \le\frac{2A_T}{P}.
 \tag{5}
\]

Thus one concrete width-independent prefactor is

\[
 C_T\le C(1+T)^{3L/2+2}.
 \tag{6}
\]

The polynomial bound is accompanied by (3)--(4), not supplied without it.
The two terms in the raw source estimate can more precisely be bounded by
`C B_0 U^(L+1) P^-3/2` and `C s U^(3L+4) P^-2`.
The former is zero at zero readout.

For globally Lipschitz activation derivatives, their bound can be included
in the fixed constants. A simple sufficient form of (4), valid for all
`T>=0`, is

\[
 \log P\ge C\left[
 (1+T)^{L+1}+\sqrt n\,(1+T)^{L+1/2}\right].
 \tag{7}
\]

Indeed `P>=H^2` suffices because (3) can ensure `H>=s`; powers of
`U=1+sqrt(T)` are bounded by fixed-depth constants times the corresponding
powers of `sqrt(1+T)`, and the logarithmic terms are absorbed by the two
positive terms in (7). At zero readout the sharper threshold is `P>=sH`.
For merely local gate regularity use (1)--(4), since the modulus may grow
arbitrarily with the radius and cannot be replaced by a universal power
of time and width.

## 4. Proof of the sharper time bookkeeping

### 4.1 A narrow tube and a relative-defect stopping rule

Dense loss dissipation gives normalized displacement at most
`rho(0)sqrt(T)<=C sqrt(T)`. On the physical radius-one neighborhood of the
dense path, fixed-depth forward and backward induction gives

\[
 \|W_\ell\|_{\rm op},\ \|w\|_2/\sqrt n\le CU,
 \quad \|h_{\ell,a}\|_2/\sqrt n\le CU^\ell,
 \quad \|\delta_{\ell,a}\|_2/\sqrt n\le CU^{L-\ell+1}.
 \tag{8}
\]

The prediction differential in the mobility norm is at most `C_J U^L`.
Stop the closure at distance
`r_T=c U^-L<=1` from dense, with `c` small enough that prediction RMS
changes by at most one. Its residual then satisfies `rho<=rho_D+1<=Q`
with fixed `Q`, and `tau<=1+QT<=CU^2`. The same residual bound holds
on every joining parameter segment at a common physical time.

Also stop when `e_E/rho` reaches

\[
 \varepsilon_T=(1+C_J T U^L)^{-1},
 \qquad e_E=\sum_{\ell=2}^L\|E_\ell\|_F.
 \tag{9}
\]

For positive initial residual, this ratio starts at zero and is continuous
before stopping. Zero initial residual gives the stationary solution.
The closure's velocity is `F+E`, so on the doubly stopped interval

\[
 |\dot{\widehat\theta}|_n\le CU^L\rho,
 \qquad \|\dot h_{\ell,a}\|_2/(\sqrt n\rho)
                        \le CU^{L+\ell-1}.
 \tag{10}
\]

The canonical residual equation is
`dot r=-2 Gamma r+JE`, where `Gamma` is a positive semidefinite tangent
Gram and `J` is the prediction differential. In particular

\[
 \dot\rho\le C_J U^L\varepsilon_T\rho.
\]

Integrating forward from any physical time `s` gives

\[
 \rho(u)\le e\rho(s)\quad(s\le u\le T),\qquad
 \frac{\tau(t)-\tau(s)}{\rho(s)}\le eT.
 \tag{11}
\]

This is an upper comparison derived from positive semidefiniteness. No
Gram gap, loss decay rate, or lower bound on residual is assumed.

### 4.2 Weighted backward energy removes the exponential source factor

Write `b_l=(r_a delta_(l,a)/rho)_a` and `c=r/rho`. The sample/neuron RMS
norm is the ordinary Euclidean norm divided by `sqrt(mn)`. From (8)--(10),
`||dot c||_m<=CU^(2L)`. Differentiate backpropagation using the local gate
modulus in (1), the full carrier supremum bounded by its Euclidean norm,
and downward induction. This gives

\[
 \|\dot\delta_{\ell,a}\|_2/\sqrt n
                  \le Cs_{n,T}U^{3L-\ell}\rho,
 \qquad \|\dot b_\ell\|_{\rm RMS}
                  \le Cs_{n,T}U^{3L-\ell+1}.
 \tag{12}
\]

For clarity the first estimate comes from the parameter differential
bound `||D delta_l[v]||_RMS<=Cs U^(2L-l)|v|_n`, combined with (10).
In that bound, the top readout term is bounded directly; each lower layer
adds a gate term of size `gamma U^L |v|_n`, a matrix-increment term,
and at most `CU` times the next backward difference. This costs only one
factor `sqrt(n)` from the full carrier. The second estimate in (12) uses
`dot b=dot c delta+c dot delta`, `rho<=Q`, and (8).

Subtract the initial backward prefix step. Its amplitude has RMS at most
`CB_0`, since the initial operators have fixed bounds. For the remaining
continuous history, the weighted Legendre derivative energy is exactly

\[
 \int_0^{\tau(t)}\xi(\tau(t)-\xi)
              \|\widetilde b_\ell'(\xi)\|_{\rm RMS}^2d\xi
 =\int_0^t\tau(s)(\tau(t)-\tau(s))
                 \frac{\|\dot b_\ell(s)\|_{\rm RMS}^2}{\rho(s)}ds.
 \tag{13}
\]

By (11), this is at most `CU^2 T` times the squared-speed integral in
physical time. Equation (12) therefore bounds its square root by
`C s U^(3L-l+4)`. The weighted Legendre tail inequality and the step tail
give

\[
 Q_{b,\ell}\le C\left[
 B_0 U/\sqrt P+s_{n,T}U^{3L-\ell+4}/P\right].
 \tag{14}
\]

Here `Q` denotes a normalized `L^2` history tail. For the forward tail one can also use the weighted estimate, together
with the closure's physical motion energy. Since the physical equation
is `dot theta=F+E`, its squared loss obeys

\[
 \dot{\mathcal L}=-|F|_n^2-\langle F,E\rangle_n
            \le-\tfrac12|F|_n^2+\tfrac12|E|_n^2.
\]

On the stopped interval, `rho<=Q` and `|E|_n<=epsilon_T Q`.
The expression `T epsilon_T^2` is uniformly bounded for all horizons
(use `U>=1` and `x/(1+x)^2<=1/4` with `x=C_J T`). Since initial loss
is bounded and terminal loss is nonnegative, integration yields
`integral_0^t |F|_n^2<=C`, hence
`integral_0^t |dot theta|_n^2<=C`. This does not assume that closure loss
is monotone.

The forward differential at layer `j` has RMS operator norm at most
`CU^(j-1)`. Thus its physical squared-speed integral is at most
`CU^(2j-2)`. Using (11) in its weighted derivative energy as in (13)
bounds that energy by `CU^2 T U^(2j-2)<=CU^(2j+2)`.
The weighted Legendre inequality at `j=ell-1` therefore gives

\[
 Q_{h,\ell-1}\le C U^{\ell}/P.
 \tag{15}
\]

The exact accumulated-defect identity bounds each link's integral by
`2 Q_(b,l) Q_(h,l-1)`. Multiply (14)--(15), sum the fixed number of links,
and use `ell<=L`:

\[
 \int_0^t e_E(s)ds
 \le C\left[B_0U^{L+1}P^{-3/2}
             +s_{n,T}U^{3L+4}P^{-2}\right].
 \tag{16}
\]

This is polynomial in the horizon at fixed depth. In particular it does
not retain an exponential inverse-residual factor from the unweighted
backward derivative estimate.

### 4.3 Why the relative-defect assumption closes

The bound (16) alone does not establish a pointwise bound on `E/rho`.
For that stopping boundary use the unweighted endpoint argument of
`ACTIVATION_UNIT_LABEL_FINITE_TIME.md`, now with (8)--(10).
The relative residual derivative and normalized direction derivative are
bounded by `CU^(2L)`. Hence on the stopped interval the ratio of any two
positive residual values is at most `exp(C T U^(2L))`.
The readout equation bounds readout RMS by
`B_0+C U^L integral rho`. Applying these comparisons in the unweighted
forward/backward derivative energies, their inverse initial-residual
factors cancel when the endpoint errors are multiplied. The result is

\[
 e_E/\rho\le A_T^{\rm end}
                  [B_0/\sqrt P+s_{n,T}/P],
 \quad A_T^{\rm end}\le
 C U^{5L+6}\exp(C T U^{2L}).
 \tag{17}
\]

The initial step uses the exact endpoint error

\[
 \mathbf1_{[1,\tau]}(\tau)
 -(\Pi_P\mathbf1_{[1,\tau]})(\tau)
 =\tfrac12[p_P(1/\tau)+p_{P-1}(1/\tau)],
\]

whose absolute value is at most one. This identity follows by integrating
`K_P=(p_P'+p_(P-1)')/2`. It removes the earlier generic `sqrt(P)` bound
for the discontinuous part. The continuous parts use the usual endpoint
`H^1` bound with its `P^-1/2` factor. The full bookkeeping of (17) is given
in the companion constants check.

Choose the fixed constant in (3) so
`H>=4 A_T^end/epsilon_T`. Then (4) makes (17) at most
`2 A_T^end/H<=epsilon_T/2`. Thus the relative-defect stopping boundary
cannot be reached. Its potentially exponential cost has been put in the
order condition, not discarded from the argument.

### 4.4 One-sided gradient stability gives the propagation factor

In mobility coordinates gradient flow is ordinary gradient flow of the
squared loss. First and second directional differentiation of the forward
network on (8) gives

\[
 |Df_a[v]|\le CU^L|v|_n,
\]
\[
 |D^2f_a[v,v]|\le
 C[U^{L-1}+\gamma_{n,T}U^{2L-1}]|v|_n^2.
 \tag{18}
\]

For the second estimate, the first-layer feature has second directional
RMS at most `C gamma |v|_n^2`. At each later layer the terms are
`phi''(z)(Dz)^2`, two matrix-increment/feature-increment terms, and the
preceding second derivative times the matrix. The first derivative RMS
is `O(U^(ell-1)|v|_n)`; converting one coordinate factor to a supremum
costs `sqrt(n)`. Induction bounds the second feature derivative by
`C[U^(ell-2)+gamma U^(2ell-2)]|v|_n^2`, with the noncurvature first-layer
term absent. Pairing with the readout gives (18). For local `C^{1,1}`
activations these statements hold almost everywhere along a parameter
segment by the absolute-continuity chain rule; a classical Hessian at every
point is not required.

Along the segment between dense and closure parameters, residual RMS is
at most `Q`. For the scalar restriction `g(a)=L(theta_D+a v)`,

\[
 g''(a)=\frac2m\sum_b (D f_b[v])^2
       +\frac2m\sum_b r_b D^2f_b[v,v]
 \ge-C[U^{L-1}+\gamma_{n,T}U^{2L-1}]|v|_n^2.
\]

The first term is nonnegative. Integrating this inequality along the
segment proves the one-sided comparison for the negative gradient field.
Thus distance satisfies

\[
 \dot d_n\le C[U^{L-1}+\gamma_{n,T}U^{2L-1}]d_n+e_E
\]

in the integral or upper-derivative sense, also at zero distance. Gronwall
and (16) give the first bound in (5).

Finally choose (3)'s constant so also `H>=exp(B_(n,T))` and
`H>=4A_T/r_T`. Condition (4) makes the bound at most `2A_T/P<=r_T/2`.
This rules out the physical stopping boundary. Bounded moment integrals
and physical parameters rule out a finite raw-ODE endpoint, exactly as in
the previous proof. Both bootstrap conditions have now been discharged.
This proves (4)--(6).

## 5. Interpretation

The useful statement is polynomial prefactor together with exponential
order requirement, and with the unabsorbed error formula (5) available.
There is no proof that these powers of time are optimal. In particular,
(6) is not a polynomial-in-time stability estimate at fixed `P`: (4)
changes with the horizon, and the explicit amplification (2) remains.

By multiplying the order factor `H` by `A_T` one can even replace
`2A_T/P` by `2/P`. This changes the required order and supplies no new
all-time guarantee. The same observation explains why asking for the
smallest isolated `C_T` is not a well-defined complexity question.

For predictions, a uniform initial full first-layer normalized norm gives
`|Delta f(t,x)|<=C U^L(1+||x||/sqrt(d))d_n(t)`. Thus one may take
`C_(T,mu)<=C_mu U^(4L+4)` in the test-RMS conclusion on the same joint
region, for a test probability measure with finite second input moment.
The parameter and prediction prefactors differ by this explicit forward
Lipschitz factor; their time powers should not be conflated.
