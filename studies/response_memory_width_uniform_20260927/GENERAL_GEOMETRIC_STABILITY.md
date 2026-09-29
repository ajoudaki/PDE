# Correlated controls, learned adjoints, and the top-link defect

Scoped analytic attempt, 28 September 2026. The assigned inputs were
`AUTONOMOUS_ONE_SAMPLE.md`, `OLD_CLOCK_ROUTE.md`,
`ENERGY_STABILITY_ROUTE.md`, the canonical setting and complete old-clock
proof in the current `paper/main.tex`, and `docs/notation.qmd`. The
`solve-math-rigorously` skill was applied. No experiments, literature search,
other study, or other current route output was used. This is an author
calculation, not an independent promotion review.

**Result and scope.** The full autonomous, arbitrary-depth,
correlated-sample width-uniform comparison remains open in this route.
Three precise results are obtained:

1. The learned adjoints of the actual closure map population `L2` into
   `L-infinity` with a width- and order-independent bound. The accumulated
   moment defect has the same property and an explicit interpolated small
   `L2 -> Lp` norm for every finite `p`.
2. The actual top hidden-link defect is
   `O(P^-2 + B_initial P^-3/2)` for arbitrary fixed sample count and depth,
   under a positive initial residual and bounded initial readout. In
   particular, for two hidden layers and zero initial readout, the entire
   autonomous closure has an `O(P^-2)` accumulated velocity defect for
   arbitrary correlated samples. This is consistency, not trajectory
   tracking. No stability hypothesis is used.
3. Two nonparallel, nonorthogonal inputs admit no common smooth positive
   Riemannian metric that cancels every signed first-layer carrier control.
   An explicit closed control loop has a hyperbolic derivative. Hence a
   control-space proof cannot obtain a width-uniform Lipschitz estimate
   from the carriers' `L2` bounds alone. The constructed controls are not
   claimed to be network-generated, so this does not disprove the desired
   closure theorem.

## 1. Conventions and imported unconditional bounds

Use the original tanh network, canonical mobilities, loss
`m^-1 sum_a r_a^2`, and autonomous old-clock closure. In population
notation let `H_l=L2(Omega_l)` on probability spaces; the first weight is
an `R^d`-valued row field, hidden increments are Hilbert--Schmidt, and
the readout belongs to `H_L`. Every hidden operator is used with its true
adjoint. For finite widths, every population vector norm below means
the explicit finite RMS `||u||_2/sqrt(n)`, every pairing means `u^T v/n`,
and `u tensor v` means `uv^T/n`. Hidden Hilbert--Schmidt norms are ordinary
finite Frobenius norms. The parameter norm is

\[
 \|v\|_{\rm mob}^2
 =\frac{\|v_1\|_F^2}{n}
   +\sum_{\ell=2}^L\|v_\ell\|_F^2
   +\frac{\|v_w\|_2^2}{n}.
 \tag{1}
\]

The unconditional existence and consistency statements here concern
every finite width. The population formulas are also valid whenever
the indicated population paths exist with these bounds and chain
rules; this note does not construct a general-depth population flow.

Use `B,q,S,A,D_l,beta_l,Z_l^*` from Section 1 of
`OLD_CLOCK_ROUTE.md`, and put `X=max_a ||x_a||/sqrt(d)`. Those are derived
constants, independent of order and uniformly bounded on families with
bounded initialized hidden operator norms and initial readout RMS. In
particular, through the prescribed physical horizon `T`, the actual
finite-width closure exists for every order and satisfies

\[
 \|w\|_{H_L}\le B,\quad \rho\le q,\quad
 1\le\tau\le A=1+S,\quad
 \|W^{(\ell)}\|_{\rm op}\le D_\ell,\quad
 \max_a\|\delta_a^{(\ell)}\|_{H_\ell}\le\beta_\ell.
 \tag{2}
\]

For a forward or backward history, `Pi_P` is its orthogonal projection
in clock time onto polynomials of degree below `P`, with the original
constant forward and zero backward prefixes. Write

\[
 b_a^{(\ell)}=\frac{r_a}{\rho}\delta_a^{(\ell)},\qquad
 D_{h,\ell,a}=\|(I-\Pi_P)h_a^{(\ell)}\|_{L^2_\xi(H_\ell)}^2,
 \quad D_{b,\ell,a}=\|(I-\Pi_P)b_a^{(\ell)}\|_{L^2_\xi(H_\ell)}^2.
\]

These divisions are proof coordinates on nonstationary paths. The raw
closure never divides by `rho`; a zero-residual initial state is
stationary. All objects in Sections 1--3 are closure objects, so hats
are suppressed. The exact defect equation and derived bounds are

\[
 \dot\theta=F(\theta)+E,\qquad E_1=E_w=0,
 \qquad
 \int_0^T\sum_{\ell=2}^L\|E_\ell\|_{HS}\,dt
 \le\varepsilon_P:=\frac{C_{\rm comp}}{\sqrt{P(P+1)}},
 \tag{3}
\]

\[
 \begin{split}
 \frac1m\sum_a\int_0^\tau\|b_a^{(\ell)}\|_{H_\ell}^2d\xi
   &\le S\beta_\ell^2,\\
 \frac1m\sum_a\int_0^\tau
       \|(h_a^{(\ell)})'\|_{H_\ell}^2d\xi&\le Z_\ell^*,\\
 \frac1m\sum_aD_{h,\ell,a}
   &\le\frac{A^2Z_\ell^*}{4P(P+1)},\\
 \int_1^{\tau(T)}\|E_\ell/\rho\|_{HS}^2d\xi
   &\le I_\ell:=2\beta_\ell^2A^2Z_{\ell-1}^*.
 \end{split}\tag{4}
\]

The same-history identity further gives

\[
 \int_0^T\|E_\ell\|_{HS}dt
 \le2\sqrt{\left(\frac1m\sum_aD_{b,\ell,a}\right)
             \left(\frac1m\sum_aD_{h,\ell-1,a}\right)}.
 \tag{5}
\]

All these statements already have complete proofs in the assigned
old-clock route. They do not include any trajectory stability estimate.

## 2. The actual learned adjoint has bounded output coordinates

Let `A_l=W^(l)-W_0^(l)` denote the closure's learned hidden increment.
At every time and every order,

\[
 \|A_\ell^*\|_{H_\ell\to L^\infty(\Omega_{\ell-1})}
 \le 2\sqrt{AS}\,\beta_\ell.
 \tag{6}
\]

To prove this, use the exact reconstruction

\[
 A_\ell=-\frac2m\sum_a\int_0^\tau
      (\Pi_Pb_a^{(\ell)})(\xi)\otimes
      (\Pi_Ph_a^{(\ell-1)})(\xi)\,d\xi.
\]

For almost every lower-layer neuron `omega`, the scalar history
`h_a(.,omega)` is bounded in absolute value by one. Scalar projection
contraction in time gives

\[
 \|\Pi_Ph_a(\cdot,\omega)\|_{L^2(0,\tau)}\le\sqrt\tau.
\]

For `g in H_l`, Cauchy--Schwarz in time therefore yields

\[
 |(A_\ell^*g)(\omega)|
 \le\frac{2\sqrt\tau}{m}\sum_a
       \|\Pi_Pb_a\|_{L^2_\xi(H_\ell)}\|g\|_{H_\ell}
 \le2\sqrt{AS}\,\beta_\ell\|g\|_{H_\ell}.
\]

The last inequality is projection contraction followed by
Cauchy--Schwarz over samples and (4). The pointwise-in-neuron argument
is justified by Fubini; there are only finitely many projected modes.
It does not use the generally false claim that the time projection is
uniformly bounded on scalar `L-infinity`.

There is a corresponding bound for the accumulated defect. Define

\[
 A_{\ell,\rm acc}
 =-\frac2m\sum_a\int_0^\tau b_a^{(\ell)}\otimes
                             h_a^{(\ell-1)}d\xi,
 \qquad R_\ell=A_\ell-A_{\ell,\rm acc}.
\]

Orthogonality of the time projection gives the exact identity

\[
 R_\ell=\frac2m\sum_a\int_0^\tau
   [(I-\Pi_P)b_a^{(\ell)}]\otimes
   [(I-\Pi_P)h_a^{(\ell-1)}]d\xi,
 \qquad \dot R_\ell=E_\ell.
 \tag{7}
\]

Since `I-Pi_P` is also an orthogonal projection,
`||(I-Pi_P)h_a(.,omega)||_(L2_time)<=sqrt(tau)`. Repeating the proof of
(6) gives

\[
 \|R_\ell^*\|_{H_\ell\to L^\infty}
 \le2\sqrt A\left(\frac1m\sum_aD_{b,\ell,a}\right)^{1/2}
 \le2\sqrt{AS}\,\beta_\ell.
 \tag{8}
\]

On the other hand, `R_l(0)=0` and (3) imply
`||R_l||_(HS)<=epsilon_P`. For `2<=p<infinity`, the elementary
inequality `||u||_p<=||u||_infinity^(1-2/p)||u||_2^(2/p)` consequently gives

\[
 \|R_\ell^*\|_{H_\ell\to L^p}
 \le(2\sqrt{AS}\,\beta_\ell)^{1-2/p}
                  \varepsilon_P^{2/p}.
 \tag{9}
\]

This places the actual accumulated error in a more restricted class than
an arbitrary Hilbert--Schmidt perturbation. It supplies no small
`L2 -> L-infinity` norm: the exponent in (9) tends to zero as `p`
increases. Also, the initialized term `W_0^* delta` is still only
controlled in `L2`. Thus (6)--(9) do not remove the carrier multiplier
from a general feedback comparison.

## 3. Improved autonomous consistency at the top hidden link

Assume additionally `w_0 in L-infinity` and `rho_0>0`. Set

\[
 B_\infty=\|w_0\|_\infty+2S,\qquad
 J^2=X^2\beta_1^2+\sum_{\ell=2}^L\beta_\ell^2+1,
 \qquad I=\sum_{\ell=2}^LI_\ell.
 \tag{10}
\]

Choose `P_0` so that every `P>=P_0` satisfies

\[
 J\varepsilon_P\le\frac12\rho_0e^{-2J^2T},
 \qquad \mu:=\frac12\rho_0e^{-2J^2T}>0.
 \tag{11}
\]

Every constant below is independent of width and order if the initial
bounds, the initial residual lower bound, depth, samples, data and
horizon are uniform. In particular, (11) is not a uniform statement for
families whose initial residual approaches zero.

### 3.1 A residual lower bound derived from consistency alone

The predictor differential has norm at most `J` from the mobility
parameter space into the sample RMS space. Indeed, its gradient for
sample `a` has blocks

\[
 \delta_a^{(1)}\,x_a^T/\sqrt d,\qquad
 \delta_a^{(\ell)}\otimes h_a^{(\ell-1)}\ (\ell\ge2),
 \qquad h_a^{(L)}.
\]

Their squared mobility norms sum to at most (10), by (2) and
`||h_a||<=1`. Cauchy--Schwarz in parameter space, and then averaging over
samples, proves the differential assertion. Since
`F=-(2/m)sum_a r_a grad_mob f_a`, it also proves
`||F||_mob<=2J rho`. Thus the exact closure equation gives

\[
 \left(\frac1m\sum_a|\dot r_a|^2\right)^{1/2}
 \le 2J^2\rho+J\|E\|_{\rm mob},
 \qquad
 \dot\rho\ge-2J^2\rho-J\|E\|_{\rm mob}.
\]

The scalar norm is differentiable along a nonstationary path since
`rho>0`. Multiply the last inequality by `exp(2J^2 t)` and integrate.
Using `||E||_mob<=sum_l ||E_l||_(HS)` and (3),

\[
 \rho(t)\ge \rho_0e^{-2J^2t}
       -J\int_0^t e^{-2J^2(t-s)}\|E(s)\|_{\rm mob}ds
 \ge\rho_0e^{-2J^2T}-J\varepsilon_P\ge\mu.
 \tag{12}
\]

There is no comparison with the dense path in this proof. In particular,
using (12) does not assume the missing trajectory theorem.

### 3.2 Clock derivative energies

Write `c_a=r_a/rho`; then `(1/m)sum_a c_a^2=1`. Let `e=E/rho` in clock
coordinates and put

\[
 R_1=8J^4S+2J^2I.
\]

By (4), `integral ||e||_mob^2 dxi<=I`. The preceding predictor bound,
divided by `rho`, gives

\[
 \int_1^{\tau(T)}\frac1m\sum_a|r_a'|^2d\xi\le R_1.
\]

Differentiation of the unit sample vector yields

\[
 c'=\rho^{-1}\left(I_m-\frac{cc^T}{m}\right)r',
 \qquad
 \int_1^{\tau(T)}\frac1m\sum_a|c_a'|^2d\xi
 \le\mu^{-2}R_1.
 \tag{13}
\]

The matrix in parentheses is an orthogonal projection in Euclidean
space, hence also in its constant rescaling to sample RMS.

The unchanged readout equation gives, pointwise,
`|dot w|<=2rho`, so `||w||_infinity<=B_infinity` and `||w'||_(H_L)<=2`.
At the top hidden layer,

\[
 z_a^{(L)\prime}
   =(F_L/\rho)h_a^{(L-1)}
       +(E_L/\rho)h_a^{(L-1)}
       +W^{(L)}h_a^{(L-1)\prime}.
\]

The dense velocity term obeys `||F_L/rho||_(HS)<=2beta_L`. The square of
a sum of three vectors is at most three times the sum of their squared
norms. Therefore

\[
 \frac1m\sum_a\int_1^{\tau(T)}
      \|z_a^{(L)\prime}\|_{H_L}^2d\xi
 \le V_L:=3\left(4S\beta_L^2+I_L+D_L^2Z_{L-1}^*\right).
 \tag{14}
\]

Since `delta_a^(L)=w tanh'(z_a^(L))`, and `|tanh''|<=2`,

\[
 \frac1m\sum_a\int_1^{\tau(T)}
       \|\delta_a^{(L)\prime}\|_{H_L}^2d\xi
 \le J_\delta:=8S+8B_\infty^2V_L.
 \tag{15}
\]

Explicitly, differentiate the product, bound the two terms by
`||w'||` and `2B_infinity ||z_a'||`, and use `(u+v)^2<=2u^2+2v^2`.
In population spaces the scalar chain rule holds on almost-everywhere
absolutely continuous representatives; its displayed integrable bound
then gives the Bochner `H1` statement. No unbounded backward carrier
appears at this top layer.

Finally `b_a^(L)=c_a delta_a^(L)`, `|c_a|<=sqrt(m)`, and
`||delta_a^(L)||<=B`. Combining (13)--(15) gives

\[
 \frac1m\sum_a\int_1^{\tau(T)}
       \|b_a^{(L)\prime}\|_{H_L}^2d\xi
 \le J_b:=2B^2\mu^{-2}R_1+2mJ_\delta.
 \tag{16}
\]

All these estimates hold for the actual autonomous closure for every
`P>=P_0`.

### 3.3 Two tails and the prefix

Let

\[
 B_{\rm initial}^2
   =\frac1m\sum_a\|c_a(0)\delta_a^{(L)}(0)\|_{H_L}^2
   \le\|w_0\|_{H_L}^2.
\]

Subtract the initial jump from each backward history:
`b_a = b_(a,continuous) + c_a(0)delta_a(0) 1_{xi>1}`. The first term
meets the zero prefix continuously and has derivative energy (16).
The Hilbert-valued Legendre bound and Minkowski's inequality in the
combined sample/history space give

\[
 \left(\frac1m\sum_a D_{b,L,a}\right)^{1/2}
 \le \frac{A\sqrt{J_b}}{2\sqrt{P(P+1)}}
       +\frac32 B_{\rm initial}\sqrt{A/P}.
 \tag{17}
\]

For completeness, the scalar step estimate used here is
`||(I-Pi_P)1_{xi>1}||_(L2(0,tau)) <= (3/2)sqrt(tau/P)`. Set
`a=tau/P`. If `tau-1<a`, approximate the step by zero. Otherwise,
replace its jump by a ramp of length `a`; the step-ramp error is at
most `sqrt(a)`, while the ramp derivative norm is `a^-1/2`. The
Legendre derivative bound gives a ramp-projection error at most
`sqrt(a)/2`. Best approximation and the triangle inequality prove the
estimate. This argument also covers `tau=1` by a zero error.

Insert (17) and the forward tail in (4) into (5). The result is

\[
 \int_0^T\|E_L(t)\|_{HS}dt
 \le\frac{A^2\sqrt{Z_{L-1}^*J_b}}{2P(P+1)}
  +\frac{3A^{3/2}B_{\rm initial}\sqrt{Z_{L-1}^*}}
          {2P\sqrt{P+1}}.
 \tag{18}
\]

This is an absolute accumulated velocity estimate, not merely a signed
reconstruction estimate. For `w_0=0` its second term vanishes. If all
labels also vanish, both exact and closure systems are stationary and
the defect is zero; otherwise `rho_0` is the positive label RMS.

When `L=2`, `E_L` is the only defect block. Thus arbitrary correlated
finite training samples have the stronger total consistency order
`O(P^-2)` at zero initial readout. The bound, initially stated for
`P>=P_0`, can be extended to all integer orders by increasing the
constant: for the finitely many smaller orders use (3), with the
factor `sqrt(P(P+1))<=sqrt(P_0(P_0+1))`.

For `L>2`, (18) improves only the top link. Differentiating an internal
backward response produces
`tanh''(z_l) (W_(l+1)^* delta_(l+1)) z_l'`. Equations (2), (4) and
(6) leave the initialized-carrier part as a product of two `L2`
fields. It cannot be inserted into (16) as though it were `L2`.
Consequently (18) does not imply a `P^-2` bound for the sum of all
hidden defects at greater depth.

## 4. Why a common fixed control metric fails for correlated inputs

This section is a geometric diagnostic of the first-layer dynamics.
It is a statement about controlled row equations, not an assertion
that arbitrary controls are realizable by the trained network.

Let `v_a=x_a/sqrt(d)` and let `u in R^d` be a first weight row. Its
actual equation has the form

\[
 \dot u=\sum_a q_a(t,\omega)V_a(u),\qquad
 V_a(u)=s(u\cdot v_a)v_a,\qquad s(z)=\operatorname{sech}^2z,
 \tag{19}
\]

where the actual scalar control is
`q_a=-(2/m)r_a (W^(2)*delta_a^(2))(omega)`. A route using only the
known carrier RMS estimates treats these controls as `L2` fields.
For one sample, `G'=1/s` straightens the single field. The following
result shows the obstruction to cancelling all correlated controls
using one fixed metric, even allowing that metric to be curved.

**Lemma.** If `v_1,v_2` are nonparallel and `v_1 dot v_2 != 0`, no
`C2` positive Riemannian metric on a neighborhood of zero makes both
`V_1` and `V_2` Killing vector fields.

Here a Killing field means its local flow preserves the metric;
equivalently its metric Lie derivative is zero. This is exactly the
cancellation needed if every signed common control is to contribute
zero to the infinitesimal squared comparison distance.

**Proof.** Put `c=v_1 dot v_2` and use the bracket convention
`[V_1,V_2]=DV_2 V_1-DV_1 V_2`. Direct differentiation yields

\[
 [V_1,V_2](u)
  =c\{s(u\cdot v_1)s'(u\cdot v_2)v_2
       -s(u\cdot v_2)s'(u\cdot v_1)v_1\}.
\]

Because `s(0)=1`, `s'(0)=0`, and `s''(0)=-2`, this field vanishes at
zero and has derivative

\[
 A=D[V_1,V_2](0)=2c(v_1v_1^T-v_2v_2^T).
 \tag{20}
\]

The bracket of two Killing fields is Killing: in local coordinates,
expanding the derivative rule for a tensor gives
`L_[V_1,V_2] g = L_V_1 L_V_2 g - L_V_2 L_V_1 g`, up to the
irrelevant simultaneous sign convention for the bracket. Both terms
vanish. At a zero of a Killing field, the directional derivative of
the metric along that field vanishes, and its Killing equation reduces
to

\[
 A^T M+MA=0,\qquad M=g(0)>0.
\]

But (20) is a nonzero real symmetric matrix: nonparallel inputs imply
`v_1v_1^T != v_2v_2^T`. It therefore has a real eigenvector `e` with
a nonzero real eigenvalue `lambda`. Multiplying the last equation on
both sides by `e` gives `2lambda e^T M e=0`, a contradiction. This
proves the lemma.

Requiring nonexpansion for every signed control gives the same
obstruction: applying nonexpansion to a flow and its inverse forces
both to be isometries. A metric allowed to depend on the whole
reference control path is not excluded by this lemma. Its distortion
must, however, be controlled to recover the original parameter norm.
The next explicit calculation shows why `L2` control bounds alone do
not provide that distortion estimate.

## 5. An explicit expanding closed loop

Take two unit inputs in a plane, oriented so
`c=v_1 dot v_2 in (0,1)`. Let `Phi_a^t` be the flow of `V_a` and use
the scalar primitive from the one-sample route,

\[
 G(z)=z/2+\sinh(2z)/4,\qquad G'=1/s.
\]

Each flow exists for all real times since `V_a` is smooth and bounded.
For a small `h>0`, set

\[
 t_1=G(h),\qquad
 t_2=G((1+c)h)-G(ch),
 \qquad
 \Psi=\Phi_2^{-t_1}\circ\Phi_1^{-t_2}
                \circ\Phi_2^{t_2}\circ\Phi_1^{t_1}.
 \tag{21}
\]

The orbit of zero under these four segments is exactly

\[
 0\longmapsto hv_1\longmapsto h(v_1+v_2)
       \longmapsto hv_2\longmapsto0.
\]

For example, on the second segment the `v_2` preactivation moves from
`ch` to `(1+c)h` in time `t_2`, because `G` of that preactivation
increases at unit speed. The third segment reverses exactly that
preactivation interval for `v_1`. This verifies `Psi(0)=0` without an
approximation or limiting control construction.

Write `P_a=v_av_a^T`. A segment of the `a` flow taking its scalar
preactivation from `z` to `z_new` has derivative

\[
 D\Phi_a=I+(r-1)P_a,\qquad r=s(z_{\rm new})/s(z).
 \tag{22}
\]

To verify (22), the flow changes only the component along `v_a`;
differentiating `G(z_new)=G(z)+t` gives
`dz_new/dz=s(z_new)/s(z)`, while every perpendicular component is
unchanged. At the four successive points in (21), put

\[
 r_1=s(h),\qquad r_2=s((1+c)h)/s(ch).
\]

The four ratios in (22) are `r_1,r_2,r_2^-1,r_1^-1`. Therefore

\[
 D\Psi(0)
 =[I+(r_1^{-1}-1)P_2][I+(r_2^{-1}-1)P_1]
  [I+(r_2-1)P_2][I+(r_1-1)P_1].
 \tag{23}
\]

Its determinant on the input plane is exactly one, since each factor
has eigenvalues `r` and one. Using `s(z)=1-z^2+O(z^4)` gives

\[
 r_1=1-h^2+O(h^4),\qquad
 r_2=1-(1+2c)h^2+O(h^4),
\]

\[
 D\Psi(0)=I+2ch^2(P_1-P_2)+O(h^4).
 \tag{24}
\]

On the plane, `P_1-P_2` has eigenvalues
`+sqrt(1-c^2)` and `-sqrt(1-c^2)`: its trace is zero and its
determinant in the orthonormal basis starting with `v_1` is
`-(1-c^2)`. Equivalently, the discriminant of the two-by-two matrix
in (24) is
`16c^2(1-c^2)h^4+O(h^6)>0` for small `h`. Its two real eigenvalues are

\[
 \lambda_\pm
  =1\pm2c\sqrt{1-c^2}\,h^2+O(h^4),
 \qquad \lambda_+>1,\quad \lambda_-<1,
 \quad\lambda_+\lambda_-=1.
 \tag{25}
\]

This also rules out any fixed pointwise norm, even a nonquadratic
one, that is preserved by both controlled flows: a norm preserved by
the closed loop at its fixed point cannot have an eigenvector whose
length is multiplied by `lambda_+>1`.

### Concentration prevents an `L2`-control-only bound

Fix a small `h` for which (25) holds and a horizon `T>0`. The loop has
control duration `D=2(t_1+t_2)` when one control at a time equals `+1`
or `-1`. Let `p` denote this periodic two-component pulse control,
with period `D`; its Euclidean norm is one except at switching times.
On the probability space `(0,1)`, choose `A_N=(0,N^-2)` and use

\[
 q_N(t,\omega)
  =\frac{ND}{T}\,p\!\left(\frac{ND}{T}t\right)
                     \mathbf1_{A_N}(\omega),\qquad 0\le t\le T.
 \tag{26}
\]

These controls satisfy exactly

\[
 \|q_N(t)\|_{L^2(\Omega;\mathbb R^2)}=D/T,
 \qquad \int_0^T\|q_N(t)\|_{L^2}\,dt=D,
 \qquad \int_0^T\|q_N(t)\|_{L^2}^2dt=D^2/T,
 \tag{27}
\]

independently of `N`. A row starting at zero completes `N` copies of
the same closed loop on `A_N`; outside that set it is stationary.
The whole unperturbed row path remains in the fixed parallelogram
with vertices listed after (21).

Let `e_+` be a unit expanding eigenvector in (25), and perturb the
initial row by `epsilon e_+ 1_(A_N)`. For each fixed `N`, smooth
finite-dimensional dependence on initial values gives

\[
 \lim_{\epsilon\to0}
 \frac{\|u_{N,\epsilon}(T)-u_{N,0}(T)\|_{L^2}}
      {\|u_{N,\epsilon}(0)-u_{N,0}(0)\|_{L^2}}
 =\lambda_+^N.
 \tag{28}
\]

Indeed numerator and denominator both contain the concentration
factor `1/N`, while the derivative of `Psi^N` at its fixed point is
`D Psi(0)^N`. For each `N`, sufficiently small perturbations also
remain in one fixed bounded enlargement of the parallelogram.
Thus no local Lipschitz bound can depend only on the fixed horizon,
the bounds (27), and boundedness of the reference row path.

The same example is finite-dimensional at widths `n=N^2`: use one
active neuron, control amplitude `ND/T` there, and zero elsewhere.
Its control RMS is again `D/T`; the first-row discrepancy in the
mobility metric is exactly its Euclidean discrepancy divided by `N`.
Hence this is a width obstruction, not an artifact of infinite
population spaces.

Crucially, (26) freely prescribes the two neuronwise controls. It
does not enforce their relation to the shared trained operator,
readout, residuals, and hidden-only moment defect. Nor does (28)
have the common initial condition of the actual dense/closure pair.
It rules out a general RMS-controlled transport shortcut, not the
canonical Gaussian autonomous approximation statement.

## 6. Exact remaining obligation

The original target needs a stability estimate for the two actual
network paths, or a direct comparison that uses the dependence between
their moment errors and their carrier controls. Sections 4--5 show
that a common fixed metric cannot erase all correlated first-layer
controls. A path-dependent transported metric must control its
distortion using more than carrier RMS bounds. Sections 2--3 identify
additional properties of the actual forcing that a successful proof
may use: bounded learned-adjoint coordinates, finite-`p` smoothing
of the accumulated defect, and a faster top-link consistency rate.

For two hidden layers, (18) supplies the approximation slack that a
separately proved sub-Gaussian reference-tail modulus could absorb.
This note proves no such trained Gaussian tail estimate. For larger
depth, even that combination leaves the internal links at the
unconditional `P^-1` consistency order. Neither the geometric
diagnostic nor the top-link theorem resolves those missing facts.

The candidate was frozen with the arguments above before reading
other current route outputs. No maintained manuscript or book file
was changed.
