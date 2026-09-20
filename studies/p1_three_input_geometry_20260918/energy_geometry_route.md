# Energy and sign geometry route for three canonical p=1 inputs

Frozen independent proof attempt, 2026-09-18. Author: scoped agent
`p1_energy_geometry`. Internal derivations only; no independent review,
promotion, experiment, numerical coefficient evaluation, or external source.

**Outcome.** This route does not prove an exponential potential for three
general nonparallel inputs. It proves three precise limitations of proposed
energy arguments: the one-input lower balance entropy has no three-direction
pointwise extension; readout–matrix quadratic imbalance has both derivative
signs even with the canonical initialized hidden state; and nodewise lower
activation growth is false along the actual prescribed trajectory for an open
family of admissible three-input geometries. A one-input exponential theorem
is included to identify exactly what succeeds before the geometric obstruction
appears. It is a diagnostic theorem outside the requested nonparallel class,
not a substitute for the target.

## 1. Scope, sources, and target

The target is the exact population p=1 system in input dimension two, with
unit inputs, labels `(1,1,-1)`, masses
`(q/2,(1-q)/2,1/2)`, `0<q<1`, and prescribed initialization
`w=g, c=0, M=D`. The active matrix remains the full 2-by-4 matrix. Both
canonical joint mark laws, the reused reverse term, the ridge `1/4096`, and
the physical population-L2/L2/Frobenius metric are retained. No trained matrix
is replaced by a diagonal matrix in the three-input analysis.

The desired result would supply a positive current-state potential controlling
the loss and decaying at a fixed exponential rate along the prescribed
trajectory, with constants determined before its future geometry is known.
A future lower Gram bound, finite action length, or saddle avoidance cannot
be assumed to complete this target.

Scientific inputs read were exactly:

* `docs/observable_p1.md`, completely, SHA256
  `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba`;
* `docs/global_nonlinear.md`, C.4.7.9 and C.4.7.10.D.3 completely;
  full-file SHA256
  `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c`;
* this study's `initial_geometry.md`, completely, SHA256
  `6856fb3d2cca5d59d1b00c4bd3cf87dd74f87315999e244b42dd1662647f091d`;
* this study's `stationary_geometry.md`, completely, SHA256
  `2fce30a3824d8bff4ecc9b04771f3986bc539735722f3434168103c464e7cfbc`.

The required research and rigorous-mathematics skills and their applicable
research-contract/adversarial-audit instructions were read. No other route,
study, history, source, or experimental result was read before this freeze.
Only this report is written by this agent.

Use the supplied notation

\[
 a_i=E_1[b_1\tanh(w\cdot u_i)],\quad z_i=Ma_i,
 \quad T_i(b)=\tanh(b\cdot z_i),
\]
\[
 f_i=E_2[cT_i],\quad
 d_i=E_2[b_2c\operatorname{sech}^2(b_2\cdot z_i)],
 \quad R_i=\mu_i(f_i-y_i).
\]

Then the exact equations are

\[
 \dot c=-2\sum_iR_iT_i,\quad
 \dot M=-2\sum_iR_id_ia_i^T,\quad
 \dot w=-2\sum_iR_i(b_1\cdot M^Td_i)
             \operatorname{sech}^2(w\cdot u_i)u_i.       \tag{1}
\]

At every finite time the bounded-displacement characteristic class supplied
by the sources justifies the differentiations below. All fields used in the
counterexamples are bounded odd fields, and all matrix entries remain finite.

## 2. Exact norm balances and the residual-length bottleneck

Let `N_c=E_2 c^2`, `N_M=||M||_F^2`. Direct differentiation of (1) gives

\[
 \dot N_c=-4\sum_iR_if_i,
 \qquad
 \dot N_M=-4\sum_iR_i\,d_i\cdot z_i.                    \tag{2}
\]

Consequently

\[
 \frac{d}{dt}(N_c-N_M)
 =-4\sum_iR_iE_2\!\left[c\,
    \{\tanh s_i-s_i\operatorname{sech}^2s_i\}\right],
 \qquad s_i=b_2\cdot z_i.                              \tag{3}
\]

The scalar bracket has the sign of `s_i`, but the entire integrand contains
both the readout and the sample residual. That scalar tanh fact is therefore
not a sign theorem for (3). With binary labels and total mass one, another
exact identity is

\[
 \dot N_c=2\left(1-\mathcal L-\sum_i\mu_i f_i^2\right). \tag{4}
\]

This is not a uniform upper bound on `N_c` integrated over infinite time.

For clarity, introduce only as an analysis quantity

\[
 A(t)=\int_0^t\sqrt{\mathcal L(s)}\,ds.
\]

The contraction normalization gives `|a_i|<=1` and `|d_i|<=||c||_2`.
Cauchy–Schwarz over the data gives `sum_i mu_i |f_i-y_i|<=sqrt(L)`.
Writing `B_1=ess sup |b_1|<infinity`, successive integration of (1) gives

\[
 \|c(t)\|_\infty\le2A(t),\qquad
 \|M(t)-D\|_F\le2A(t)^2,
\]
\[
 \|w(t)-g\|_\infty
 \le 2B_1\|D\|_{\rm op}A(t)^2+2B_1A(t)^4.             \tag{5}
\]

For the last line, the speed is at most
`4 B_1 A A' (||D||op+2 A^2)`. Thus finite residual length would provide
the desired all-time bounds on every physical block. The ordinary loss
identity bounds the squared velocity integral, however, and does not bound
`A(infinity)`. Using (5) with an assumed finite `A(infinity)` would leave
the main long-time assertion unproved. Also, `A` is history-dependent and is
not being proposed as an admissible current-state potential.

## 3. Quadratic readout–matrix imbalance is not monotone on the canonical class

The following is an exact ambient-class counterexample using the canonical
initialized hidden state itself. It does not assert that its alternate
readouts occur on the trajectory starting from zero.

Fix any three admissible nonparallel directions and set `w=g, M=D`.
The initial-geometry source proves that the resulting `z_i` are nonzero
and pairwise unequal up to sign. Put

\[
 H=\operatorname{span}\{T_1,T_2,T_3\}\subset L^2(\Omega_2),
 \quad s_i^*=\mu_i y_i,
\]
\[
 S(b)=\sum_i s_i^*(b\cdot z_i)
                        \operatorname{sech}^2(b\cdot z_i).
                                                               \tag{6}
\]

**Claim.** `S` does not belong to `H`.

To prove this, choose a vector `e` for which
`ell_i=e dot z_i` are nonzero with distinct absolute values, and set
`X_i=ell_i^2`. Such a vector exists by avoiding finitely many lines.
An alleged relation `S=sum_i A_i T_i`, restricted to `b=t e` near zero,
has Taylor coefficients

\[
 (2n+1)\sum_i s_i^*\ell_iX_i^n
       =\sum_i A_i\ell_iX_i^n\quad(n\ge0).              \tag{7}
\]

Every odd tanh coefficient is nonzero, as proved in the supplied stationary
geometry source, so cancellation of those coefficients is legitimate. Apply
the shift polynomial `P(E)=product_i(E-X_i)` to both sides. The right side
vanishes. The left becomes

\[
 2\sum_i s_i^*\ell_iX_i^{n+1}P'(X_i)=0\quad(n\ge0).
\]

The Vandermonde system for `n=0,1,2` forces each
`s_i^* ell_i X_i P'(X_i)=0`, whereas all these factors are nonzero.
The initial passage from an L2 relation to a relation near zero uses the
strictly positive density of the upper law and continuity. This proves the
claim.

Define `v=S-Proj_H S`, a nonzero bounded odd function, and take the two
alternate states `c=v` and `c=-v`, keeping `w=g, M=D`. Since `c` is
orthogonal to every `T_i`, both states have `f_i=0` and loss one. Formula
(3) gives exactly

\[
 \left.\frac{d}{dt}(N_c-N_M)\right|_{c=v}
       =-4\|v\|_2^2<0,\qquad
 \left.\frac{d}{dt}(N_c-N_M)\right|_{c=-v}
       =+4\|v\|_2^2>0.                                \tag{8}
\]

Hence no monotonicity of this imbalance follows from parity, initialized
hidden geometry, fixed norm bounds, or scalar tanh concavity alone. A
successful proof for `c(0)=0` would need an additional preserved property
of the readout generated by its history. This result neither proves nor
disproves such a property.

At the actual initial state the first derivative in (3) is zero. If
`Y=sum_i mu_i y_i T_i` and
`Q=sum_i mu_i y_i (T_i-s_i sech^2 s_i)`, its exact second derivative is

\[
                 (N_c-N_M)''(0)=8E_2[YQ].              \tag{9}
\]

No sign for (9), over the entire prescribed three-input family, is asserted
in this report.

## 4. The one-direction mechanism really does give an exponential theorem

For this section only, let every signed input `y_i u_i` equal `e_1`.
Oddness reduces the data to one unit input `e_1` with target `+1`.
This is outside the nonparallel target class.

Write

\[
 \xi=(b_{1,h_1},b_{1,k_1})\in\mathbb R^2,
 \quad s=w_1,
 \quad a=E_1[\xi\tanh s],\quad z=m\cdot a,
 \quad B=b_{2,1}.
\]

The exact initialized independence and signed-coordinate symmetries imply
the following invariant subspace. The readout is a function of `B` only;
`s` depends only on the first lower coordinate pair; `w_2=g_2`; the only
moving matrix entries are `m=(M_{1,h_1},M_{1,k_1})`; all the other entries
stay at their canonical values. Indeed, all feature pairings in the unused
coordinate have zero expectation by independence and centeredness, the
second component of the upper backward vector is zero, and (1) preserves
these assertions. Thus this reduction is derived for this special data;
it is not imposed on the three-input dynamics.

Let

\[
 f=E_2[c\tanh(Bz)],\quad e=1-f,\quad
 d=E_2[Bc\operatorname{sech}^2(Bz)],\quad
 C=E_1[\xi\xi^T\operatorname{sech}^4s]\succeq0.
\]

In the increasing time variable `d tau/dt=2e`, the exact equations are

\[
 c_\tau=\tanh(Bz),\quad
 m_\tau=d a,\quad
 s_\tau=d(\xi\cdot m)\operatorname{sech}^2s,
\]
\[
 a_\tau=dCm,\qquad
 z_\tau=d\bigl(|a|^2+m^TCm\bigr).                       \tag{10}
\]

There is no circular assumption that `e` remains positive. For one sample
the prediction equation in physical time is
`f'=2(1-f)||grad f||^2`, so
`e(t)=exp(-2 integral_0^t ||grad f||^2 ds)>0` at each finite time.
The source's finite-time existence bounds make that integral finite.

The initialized-geometry source gives `z(0)=F(1)>0`. While `z>0`,
`B c_tau=B tanh(Bz)>=0`. Starting from `c=0`, this implies `Bc>=0`
and therefore `d>=0`. Equation (10) makes `z` nondecreasing, closing this
invariance argument and keeping `z>=z(0)` for all time. Finally,

\[
 f_\tau=E_2\tanh^2(Bz)
              +d^2\bigl(|a|^2+m^TCm\bigr)
       \ge\kappa_0,
 \quad \kappa_0=E_2\tanh^2(BF(1))>0.                   \tag{11}
\]

Thus the current-state potential `L=e^2` obeys

\[
              \dot{\mathcal L}\le-4\kappa_0\mathcal L,
 \qquad \mathcal L(t)\le e^{-4\kappa_0t}.               \tag{12}
\]

The constant uses only the prescribed initialization. The total residual
length is at most `1/(2 kappa_0)`, so (5) gives uniform bounds on all moving
blocks. No future feature condition is assumed.

This scalar reduction also has an exact lower balance invariant:

\[
                    |m|^2-E_1\sinh^2s=\text{constant}. \tag{13}
\]

Indeed, the two tau derivatives are both `2 d z`, since
`(sinh^2 s)'=sinh(2s)` and
`sinh(2s) sech^2 s=2 tanh s`. At each finite time bounded displacement
from Gaussian `g_1` makes every integral here finite and justifies
differentiation. The exponential conclusion is from the monotonicity in
(10)–(11), not from an unsupported coercivity inference from (13).

## 5. The one-input entropy cannot cancel three lower gates

Consider extending (13) by a local scalar entropy `E_1 Phi(w)` balanced
against `||M||_F^2`. Direct cancellation of the contribution of each input
in the two derivatives would require

\[
 \operatorname{sech}^2(w\cdot u_i)\,
                 \nabla\Phi(w)\cdot u_i
       =2\tanh(w\cdot u_i),
\]

or equivalently

\[
              \nabla\Phi(w)\cdot u_i
                    =\sinh(2w\cdot u_i),\quad i=1,2,3.\tag{14}
\]

**Proposition.** For three pairwise nonparallel directions in the plane,
no C1 function on `R^2` satisfies (14).

Their unique linear dependence is `sum_i lambda_i u_i=0`, with all
`lambda_i` nonzero: a zero coefficient would make the other two directions
parallel. Multiplying (14) by these coefficients would force

\[
                \sum_i\lambda_i\sinh(2w\cdot u_i)=0
                         \quad\text{for every }w.     \tag{15}
\]

Choose `v` with all `v dot u_i` nonzero and with distinct absolute values,
again by avoiding finitely many lines. Put `w=t v`. As `t` tends to
positive infinity, the term with largest `|v dot u_i|` has a unique
exponential growth rate and a nonzero leading coefficient. Dividing by
that exponential contradicts (15). This proves the proposition.

This falsifies the direct inputwise entropy-cancellation route. It does not
exclude a nonlocal entropy, a state-dependent matrix weighting, residual-
dependent cancellation, or an invariant that uses special trajectory
relations. It also explains why the successful identity (13) cannot simply
be summed over three directions: the same two-dimensional row field must
serve all three gates.

## 6. Nodewise lower monotonicity fails on an open canonical three-input family

This counterexample concerns the actual prescribed initialization and
trajectory, unlike Section 3.

Because the full system is odd in the input, change variables
`v_i=y_i u_i` and replace all labels by `+1`. The predictions and loss are
unchanged after multiplication by the original labels, and substitution
in (1) shows that the physical vector field is exactly unchanged. This is
an exact relabeling, with no alteration of either mark law.

Let

\[
 a_i^0=E_1[b_1\tanh(g\cdot v_i)],\quad z_i^0=Da_i^0,
 \quad T_i^0(b)=\tanh(b\cdot z_i^0),
\]
\[
 Y(b)=\sum_j\mu_jT_j^0(b),\qquad
 e_i=E_2[b_2Y(b_2)\operatorname{sech}^2(b_2\cdot z_i^0)].
\]

Since `c(0)=0`, `w'(0)=M'(0)=0` and `c'(0)=2Y`. Differentiating the
row equation therefore gives

\[
 w''(0)=4\sum_i\mu_i(b_1\cdot D^Te_i)
                  \operatorname{sech}^2(g\cdot v_i)v_i.\tag{16}
\]

At the coincident signed-input reference `v_i=e_1`, write `z_0=F(1)>0`.
Independence and symmetry of the upper coordinates give

\[
 e_i=e_0e_1,\qquad
 e_0=E_2[B\tanh(Bz_0)\operatorname{sech}^2(Bz_0)]>0.
\]

Consequently

\[
 w''(0)\cdot e_1
       =4e_0(b_1\cdot D^Te_1)\operatorname{sech}^2g_1.\tag{17}
\]

Use the exact initialized bands from the supplied sources, with positive
normalizers `a_*,b_*`:

\[
 b_1\cdot D^Te_1
 =\left(\frac{d_h}{a_*}
           -\frac{d_k\beta}{b_*(v+\eta)}\right)h_1
                    +\frac{d_k}{b_*}k_1
 =A_*h_1+B_*k_1,\qquad B_*>0.                         \tag{18}
\]

The joint law of `(h_1,k_1)` has positive density on `(-1,1)^2`.
Choose `h_1` in a sufficiently small compact positive interval and `k_1`
in a compact interval below `-1/2`, so that
`|A_* h_1|<B_*/4`. On this positive-probability set,
`g_1>0` but `b_1 dot D^T e_1<-B_*/4`. Restrict the second lower
coordinate pair to any compact set of positive probability. Shrinking
the first intervals slightly if necessary gives a compact lower-mark set
of positive probability on which (17) is uniformly strictly negative.

All quantities in (16), and `g dot v_i`, depend continuously on the three
input directions, uniformly on this compact mark set. The population
integrals are continuous by bounded convergence. Therefore, for every
triple of signed directions sufficiently close to `e_1`, the same set has

\[
             g\cdot v_i>0,\qquad w''(0)\cdot v_i<0
                         \quad(i=1,2,3).              \tag{19}
\]

The neighborhood contains pairwise nonparallel triples; restricting to
them gives an open nonempty family in the admissible configuration space.
For any fixed such triple, local C2 dependence in the bounded-displacement
Banach space gives the uniform expansion

\[
 \tanh(w(t)\cdot v_i)
 =\tanh(g\cdot v_i)
   +\frac{t^2}{2}\operatorname{sech}^2(g\cdot v_i)
                           w''(0)\cdot v_i+o(t^2).
\]

Thus every one of the three initially positive lower activations decreases
on a common positive-probability set for all sufficiently small positive
times. Their magnitudes decrease as well. In original variables this is
the family with `u_1,u_2` close to `e_1` and `u_3` close to `-e_1`,
with labels `(1,1,-1)` and the prescribed positive masses.

The mechanism is the nonzero reversed-feature band `d_k`: lower reverse
noise allows the initialized backward linear form to have the opposite
sign to `g_1`. Removing that term would change the canonical system.
Aggregate feature growth is not disproved by this calculation; indeed it
coexists with the scalar aggregate monotonicity in Section 4. The precise
falsified assertion is nodewise monotonic growth of the lower activation
magnitudes from the prescribed initialization.

## 7. Frozen claim ledger and outstanding obligation

| Claim | Status | Scope and limitation |
|---|---|---|
| Norm identities (2)–(4), residual-length bounds (5) | Exact | They do not bound the infinite residual length. |
| Quadratic imbalance is monotone on the canonical bounded-displacement class | Falsified by (8) | Alternate bounded odd readouts; their reachability from zero is not asserted. |
| Scalar signed-input canonical flow has exponential loss decay | Proved in (10)–(12) | Degenerate one-direction data only; not the requested three-input theorem. |
| A local inputwise lower entropy extends the scalar balance to three directions | Falsified by (14)–(15) | Does not exclude more general nonlocal or residual-dependent energies. |
| Every lower activation magnitude grows from canonical initialization in an aligned three-input geometry | Falsified by (16)–(19) | Actual prescribed trajectory; open family of admissible nonparallel triples. |
| General three-input canonical flow admits the requested exponential current-state potential | Open | No all-time conditioning, finite residual length, or residual-specific lower dissipation bound has been established. |

The remaining energy-route obligation is concrete: find and prove a
preserved, aggregate relation linking the readout generated from zero to the
three evolving upper vectors, strong enough to bound residual dissipation
without presuming a future Gram gap. Neither scalar tanh concavity nor the
two natural layer-norm balances supplies that relation. The calculations
above are route falsifiers, not a counterexample to exponential decay of the
prescribed three-input trajectory.

## 8. Post-freeze follow-up: bounded interpolation through compatible collisions

After the independent Sections 1–7 were frozen, the supervisor requested a
specific additional lemma concerning compatible upper-feature collisions.
No other route artifact was read. This section proves that lemma; it does
not claim the required geometric protection along the canonical trajectory.

Write `H=L2(Omega_2)` and

\[
                       F(x)(b)=\tanh(b\cdot x).
\]

Because the upper marks are bounded, this is a C-infinity map from `R^2`
to both `H` and `L-infinity(Omega_2)`, with derivatives of each fixed order
uniformly bounded on bounded sets. Its first two derivatives are

\[
 DF(x)[v]=(b\cdot v)\operatorname{sech}^2(b\cdot x),
\]
\[
 D^2F(x)[v,v]=(b\cdot v)^2\tanh''(b\cdot x).           \tag{20}
\]

**Theorem (uniform bounded interpolation for at most three compatible
codes).** Fix positive `r,R,delta`, with `r<=R`. There is a finite constant
`C=C(r,R,delta)` depending also on the fixed canonical upper law such that
the following holds. Let `m<=3`, labels `y_i` in `{+1,-1}`, and upper codes
`z_i` satisfy, on putting `x_i=y_i z_i`,

\[
 r\le|x_i|\le R,\qquad |x_i+x_j|\ge\delta\quad(i\ne j).\tag{21}
\]

Then there is a bounded odd readout `c_*` with

\[
 E_2[c_*F(z_i)]=y_i\quad\text{for every }i,
 \qquad \|c_*\|_2+\|c_*\|_\infty\le C.                \tag{22}
\]

Exact repetitions among the `x_i` are allowed and impose duplicate
constraints. No lower bound on `|x_i-x_j|` appears. Thus the minimum-norm
L2 interpolating readout is uniformly bounded as compatible codes merge.
The L-infinity statement asserts existence of a bounded interpolant; it
does not require the minimum-L2 solution to minimize the L-infinity norm.

Sign folding reduces (22) exactly to
`<c_*,F(x_i)>=1`. We prove the latter assertion.

### 8.1. Two confluent independence facts

For nonzero `x,v`, the four functions

\[
 F(x),\quad DF(x)[e_1],\quad DF(x)[e_2],
                  \quad D^2F(x)[v,v]                  \tag{23}
\]

are linearly independent. Indeed, an alleged relation can be written

\[
 A\tanh(b\cdot x)+(b\cdot p)\operatorname{sech}^2(b\cdot x)
                 +B(b\cdot v)^2\tanh''(b\cdot x)=0.
\]

The upper law has positive density on an open neighborhood of zero, so
the continuous identity holds there. Divide by `sech^2(b dot x)` and
write `s=b dot x`. Since `tanh''s=-2 tanh(s) sech^2(s)`, this gives

\[
       \frac A2\sinh(2s)+b\cdot p-2B(b\cdot v)^2\tanh s=0.\tag{24}
\]

On the line `s=0`, the identity forces `p` to be parallel to `x`, so
`b dot p=lambda s`. If `v` is not parallel to `x`, fix small nonzero
`s` and vary `b` transversely in the open neighborhood. The coefficient
of the transverse quadratic term in (24) forces `B=0`. Its cubic and
linear coefficients then give `A=lambda=0`.

If `v=nu x`, `nu!=0`, compare the coefficients of `s,s^3,s^5` in (24):

\[
 A+\lambda=0,\quad \frac23 A-2B\nu^2=0,
 \quad \frac2{15}A+\frac23B\nu^2=0.
\]

The last two imply `(16/45)A=0`, hence `A=B=lambda=0`.
This proves (23).

The second fact is that

\[
                  F(x),\quad DF(x)[v],\quad F(z)       \tag{25}
\]

are independent whenever `x,z` are nonzero, `z!=+/-x`, and `v!=0`.
Choose `e` so `ell=e dot x`, `k=e dot z`, and `h=e dot v` are nonzero,
with `ell^2!=k^2`. Restricting an alleged relation to `b=t e`, its odd
Taylor coefficients, after canceling the nonzero tanh coefficient, are

\[
 A\ell X^n+B h(2n+1)X^n+CkY^n=0,
 \qquad X=\ell^2,\quad Y=k^2.
\]

Applying `(E-X)(E-Y)` gives `2BhX^{n+1}(X-Y)=0`, so `B=0`.
The remaining two-term Vandermonde system gives `A=C=0`. This proves
(25). The corresponding two-function assertions follow by dropping a
function from either independent list.

Each independence statement yields uniform positive Gram lower bounds
on any compact set of its displayed parameters that satisfies its strict
conditions. To verify this without a uniformity assumption, minimize the
continuous squared norm of a linear combination over that compact parameter
set times the unit coefficient sphere. A zero minimum would contradict
the pointwise independence just proved.

### 8.2. Three codes in one small cluster

For three distinct points choose a farthest pair and relabel it
`x_1=x`, `x_2=x+h v`, where `h>0` and `|v|=1`. With `u` a unit
perpendicular to `v`, write

\[
                     x_3=x+h(a v+b u).
\]

The farthest-pair property gives `0<=a<=1` and `|b|<=1`: both distances
from `x_3` to the pair's endpoints are at most `h`. Define three
transformed feature functions

\[
 Q_1=F(x),\qquad Q_2=\frac{F(x+hv)-F(x)}h,
\]
\[
 Q_3=\frac{F(x_3)-(1-a)F(x)-aF(x+hv)}{d},
 \qquad
 d=\sqrt{(hb)^2+\{h^2a(1-a)/2\}^2}.                   \tag{26}
\]

Here `d>0`: its only zero cases are `b=0,a=0 or 1`, which would repeat
an endpoint, contrary to the current distinctness assumption.

There is a uniform L-infinity expansion as `h` tends to zero,

\[
 Q_2=DF(x)[v]+O(h),
\]
\[
 Q_3=\alpha DF(x)[u]+\beta D^2F(x)[v,v]+O(h),
 \quad \alpha=\frac{hb}{d},\quad
 \beta=-\frac{h^2a(1-a)}{2d},\quad\alpha^2+\beta^2=1.\tag{27}
\]

The uniformity when the third point is extremely close to an endpoint
is essential. To prove it, split the numerator of `Q_3` into a transverse
increment and an error of linear interpolation along the segment. The
transverse increment is

\[
 F(x+h(av+bu))-F(x+hav)=hb\,DF(x)[u]+O(h^2|b|).
\]

For the segment let `g(s)=F(x+shv)`, `0<=s<=1`. Twice integrating its
second derivative gives

\[
 g(a)-(1-a)g(0)-ag(1)=-\int_0^1G_a(s)g''(s)\,ds,
\]

where `G_a(s)=(1-a)s` for `s<=a` and `G_a(s)=a(1-s)` for `s>=a`.
Its integral is `a(1-a)/2`. The uniform third-derivative bound gives

\[
 g(a)-(1-a)g(0)-ag(1)
 =-\frac{h^2a(1-a)}2D^2F(x)[v,v]+O(h^3a(1-a)).
\]

Dividing the combined remainder by `d` bounds it by a constant times
`h`, because `d` dominates each of `h|b|` and `h^2a(1-a)/2`.
This establishes (27), including all highly unequal separation scales.

For `x` in the compact annulus of (21), `v` on the unit circle, and
`alpha^2+beta^2=1`, the three limiting functions in (27), together with
`Q_1=F(x)`, are independent by (23). They therefore have a common positive
Gram lower bound. For all sufficiently small `h`, the actual three
functions in (26) have a common positive Gram lower bound too, by (27).
Their L-infinity norms are also uniformly bounded.

The desired target values in these coordinates are exactly

\[
                  (\langle c_*,Q_1\rangle,
                    \langle c_*,Q_2\rangle,
                    \langle c_*,Q_3\rangle)=(1,0,0).   \tag{28}
\]

Solving the three-by-three Gram system for a readout in their span yields
uniform L2 and L-infinity bounds. For example, a Gram lower bound `kappa`
gives `||c_*||_2^2<=1/kappa`, and its coefficients and the uniform
L-infinity feature bounds control `||c_*||_infinity`. Crucially, the
vanishing denominators in (26) do not enter (28).

### 8.3. Completion over all configurations

For completeness, a compactness contradiction organizes every remaining
case without assuming a collision pattern. If no uniform bound existed,
take a sequence of at most three sign-folded code configurations satisfying
(21) for which every interpolant requires an unbounded norm. Pass to a
subsequence with fixed code count and convergent codes. Their limits are
nonzero and never antipodal by (21).

If all limiting codes are distinct, their feature Gram is positive definite
by the ridge-independence result in the supplied sources, and stays so in
a neighborhood. Its inverse supplies bounded interpolants. If exactly two
merge, use the basis

\[
 F(x_1),\quad\frac{F(x_2)-F(x_1)}{|x_2-x_1|},\quad F(x_3).
\]

After a subsequence the normalized difference direction converges. The
basis tends to (25), its target is `(1,0,1)`, and its Gram remains uniformly
positive. Exact repetitions in the sequence simply delete a duplicate
constraint and reduce to two distinct limiting features. If all three
merge, Section 8.2 gives the contradiction, with exact duplicates handled
by the two-function limit `F(x),DF(x)[v]` or the single feature `F(x)`.
The identical two-function argument covers an original code count two.
Thus every case supplies a common finite bound, proving (22). Every basis
function used is odd, so all constructed readouts have the required parity.

### 8.4. Exact residual-specific consequence and its remaining hypothesis

The theorem avoids demanding a uniform lower eigenvalue of the upper
feature Gram at compatible collisions. If its geometric constants were
known to hold along a trajectory, choose the bounded comparator `c_*` at
each current state. No derivative of that comparator is needed:

\[
 \langle\dot c,c-c_*\rangle
 =-2\sum_i\mu_i(f_i-y_i)
               \langle F(z_i),c-c_*\rangle
 =-2\mathcal L.
\]

Therefore

\[
 \|\dot c\|_2^2\ge
        \frac{4\mathcal L^2}{(\|c\|_2+C)^2}.           \tag{29}
\]

The readout norm has the unconditional sharper bound

\[
 \frac{d}{dt}\|c\|_2^2
 =4\sum_i\mu_i(y_if_i-f_i^2)
 =1-4\sum_i\mu_i(f_i-y_i/2)^2\le1,
 \qquad\|c(t)\|_2^2\le t.                             \tag{30}
\]

Under the still-unproved geometric protection (21) for all time,
the loss identity and (29)–(30) would imply

\[
 \dot{\mathcal L}\le-\frac{4\mathcal L^2}{(\sqrt t+C)^2}
             \le-\frac{2\mathcal L^2}{t+C^2},
\]

and, from initial loss one,

\[
 \mathcal L(t)\le
     \frac1{1+2\log(1+t/C^2)}\longrightarrow0.          \tag{31}
\]

Equation (31) is stated only to expose the exact missing bridge. It is not
an unconditional fitting theorem and not the requested exponential theorem.
The positive result of this follow-up is (22): compatible collisions alone
do not force an unbounded interpolating readout when there are at most three
upper codes. Bounding those codes and excluding zero or incompatible
antipodal approach along the canonical trajectory remain unresolved.
