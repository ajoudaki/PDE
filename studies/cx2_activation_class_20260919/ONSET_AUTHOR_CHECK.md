# Author-side check of the all-law onset extension

Status: the supervisor's complete `ONSET_EXTENSION.md` was read and checked
after the preliminary independent estimates below were recorded. Section 5
records the manuscript findings and repairs. This is author-side verification,
not an isolated review or a promotion verdict.

## 1. Exact norm and preliminary constants

Fix `D0=|phi(0)|`, `D1=||phi'||infinity`, and
`D2=Lip(phi')`. The arguments need only these finite bounds; nonaffinity
is not used for existence. Put `D0bar=D0+D1`, so unit-scale-or-smaller
compactly supported mollifications have this common value-at-zero bound.
Let `S0=11`, `B=24`, and

```
h1 = D0bar + D1 B
h2 = D0bar + D1 B h1
R0 = B h2 + 1
V  = max(1, 2 R0 (D1^2 B^2 + D1 B h1 + h2))
Tball = min(1, (B-S0)/(4V)).
```

The initialization event is `||w0,n||F/sqrt(n)<=11`,
`||A0,n||op<=11`, `||c0,n||2/sqrt(n)<=11`; its probability tends to one
independently of the data. The actual Gaussian readout has squared RMS
expectation `n^-2`, and is retained. In the population `w0=g~N(0,I2)`,
`c0=0`, `||A0||op<=10`, `K0=0`.

While row/readout/action norms are at most `B`, the forward RMS bounds
are `h1,h2`, and the backward bounds are respectively

```
||Delta2||2 <= D1 B
||q||2      <= D1 B^2
||Delta1||2 <= D1^2 B^2.
```

The sum of row-L2, increment-HS, and readout-L2 velocity norms is at most
`V`. The same finite inequality uses row Frobenius divided by `sqrt(n)`,
ordinary middle Frobenius, and readout Euclidean divided by `sqrt(n)`.
Initialized middle matrices themselves are not bounded in Frobenius norm.
The first-exit argument bounds all these trajectories through `2Tball`.

## 2. Full-row and Hilbert--Schmidt transport estimate

For same-carrier states write

```
e = ||w-wbar||2 + ||K-Kbar||HS + ||c-cbar||2,
h = |u-v|,
q(u) = A* [c phi'(A phi(w.u))].
```

On a fixed common raw/action ball,

```
||Z1(u)-Z1bar(v)||2 <= e + B h,
||H1(u)-H1bar(v)||2 + ||Z2(u)-Z2bar(v)||2
 + ||H2(u)-H2bar(v)||2 + |f(u)-fbar(v)| <= C(e+h).
```

Here and below `C` depends only on the ball and `D0,D1,D2`. The
unbounded values of `phi` cause no difficulty: every use is a global
Lipschitz estimate or an L2 feature bound. For a reference multiplier `P`,

```
||[phi'(z)-phi'(zbar)]P||2
 <= D2 R ||z-zbar||2 + 2 D1 ||P 1_{|P|>R}||2.
```

First apply this to `P=cbar`. Then expand the difference of the actual
adjoint actions and apply it to `P=qbar(v)` in the lower gate. The first
cutoff term is multiplied only by bounded action and gate factors. The
second cutoff term is added. Thus the resulting constant grows as `1+R`,
not `(1+R)^2`.

For the row gradient explicitly subtract

```
r Delta1 u - rbar Delta1bar v
 = (r-rbar)Delta1 u + rbar(Delta1-Delta1bar)u
   + rbar Delta1bar(u-v).
```

For the middle gradient use `||a tensor b||HS=||a||2||b||2` and its
two-term difference inequality. After integration over a coupling of laws,

```
||F_mu(theta)-F_nu(thetabar)||sum
 <= C(1+R)(e+W1(mu,nu))
  + C [tau_R(cbar) + integral tau_R(qbar(v)) dnu(v,y)].
```

This is the exact needed extension of maintained C.4.1. It is also valid
for exact Borel-law finite networks. No tail of an input maximum, no
pointwise bound on the full Gaussian row, and no Gram inverse enter it.

## 3. Noncircular regularity and law completion

For every separately fixed finite law and Euler mesh, A.1 constructs the
original `C1,1` finite population program. Its coordinate maps are continuous
with linear envelopes, including the map `(z,c)->c phi'(z)`.

Take smooth mollifications with uniformly bounded first derivative and
second derivative, and uniform convergence of both activation and first
derivative. Their complete finite programs converge strongly on the same
carrier by finite induction: activation differences use the Lipschitz bound;
backward products use bounded-multiplier continuity; learned ranks use the
HS rank difference inequality. This requires no derivative of `phi'`.

Apply maintained C.2 to each smooth program, using depth two, normalized
Gram bound one, variance-one first projections, zero population readout,
unit middle variance and mobilities, and the preliminary bounds above.
Its `Tresponse,gamma,Ctail` depend only on these fixed parameters, never
on atom count, masses, covariance rank or mesh. Fatou then transfers its
active-query and readout subGaussian estimates to the original Euler
program. This transfer occurs before a continuous-time or Borel-law flow
is claimed, so there is no circular existence premise.

On `Tphi<=min(Tball,Tresponse)`, the preceding transport estimate gives

```
sup_t e_ij(t) <= C exp(CR) [
 (1+R)(mesh_i+mesh_j+W1(mu_i,mu_j)) + exp(-cR^2)].
```

Complete finite-law Euler interpolants simultaneously in laws and meshes:
at fixed cutoff take both approximations to their limits, and then remove
the cutoff. Each vector-field integrand is continuous into its L2/HS
space on the compact data domain. It has compact separable range and is
Bochner integrable. For a fixed such integrand `G`, the coupling bound

```
||integral G dmu - integral G dnu||
 <= omega_G(a) + 2 ||G||infinity W1(mu,nu)/a
```

proves the needed law continuity. Joint state/input continuity and a
compact-time subsequence argument make field convergence uniform in time.
The complete strong integral equations therefore pass to the limit.

For arbitrary-law tail transfer use `bM(z)=min(exp(gamma z^2),M)`.
It is bounded and globally Lipschitz for fixed `M`. Backward continuity
gives uniform-input convergence of its expectations. Pass their law
integrals to the limiting law, then increase `M` by monotone convergence.
This proves exactly

```
sup_t E exp(gamma c(t)^2) <= Ctail,
sup_t integral E exp(gamma q(t,u)^2) dmu(u,y) <= Ctail.
```

Cauchy--Schwarz in the data law gives the corresponding integrated RMS
tails `C exp(-cR^2)`, hence the weaker exponential tails required by the
generic closure. This reasoning proves law-integrated backward tails; it
does not by itself prove a pointwise continuum-input subGaussian bound.

## 4. Identification and closure cautions

The finite comparison proxy must include the actual finite initial readout
additively in its parameters. Its assigned increments use a fixed finite
zero-readout population Euler program. At fixed reference law, proof mesh
and cutoff, fixed-program second moments identify the proxy and its
recomputed-velocity defects. The full-row/HS transport estimate then
compares the proxy to actual GF, or to actual raw GD with an extra
`C(1+R) eta_n` term. Consequently `eta_n->0` is sufficient in the joint
width/step limit; no relative step/width/data rate is needed. The actual
laws may be Borel. Only the reference program is finite and frozen before
the width limit.

For the numerical dictionary, all bounded valid Word codes through `16N`
with ridge `2^-N` are a nested cofinal dense smooth dictionary. Literal
duplicates are harmless because the ridge stays positive. They need not
add a strictly new functional direction at every integer order. Tanh,
sine and cosine are initializer probes; training still uses `phi` at both
layers. No tanh parity identity should be claimed for general `phi`.

Continuum closure requires the same Bochner integration check above,
energy differentiation under the compact input integral, and integrated
reference tails in the velocity estimate. Compact `(t,u)` images of `H1`
and `Delta2`, and compact HS image of `K'(t)`, provide the vanishing
omitted-action/projection source. Merely bounded state norms do not.

The full rational two-arc family remains admissible for existence,
neural identification, closure and data quadrature. Its midpoint law has
`W1` error at most `1/(20m)`. Universal activity is neither needed nor
proved. Uniform-time whole-circle predictions and initial/current pair
laws in W2 are covered. Path-space W2 for arbitrary bounded-continuous
observation graphs needs a separate path-equicontinuity argument and
should not be inferred solely from uniform-time marginal W2.

Mathematical cubature/time consistency is valid for every fixed activation
in the stated class. A literal universal finite-precision implementation
requires locally uniform algorithms evaluating `phi` and `phi'`; the
regularity assumptions alone do not imply computability.

## 5. Check of the supervisor manuscript

The complete supervisor manuscript was read after its initial persistence.
Its alternative preliminary ball `||w||2<=3`, `||K||HS<=1`,
`||c||2<=1` is valid. With `||A0||op<=10`, it gives `||A||op<=11`;
the displayed three velocity bounds and
`Tball=min(1,1/[4(1+V)])` give total increment at most `1/4`, strictly
inside every initial margin. Thus it is an admissible sharper alternative
to the constants recorded in Section 1 of this check.

Four concrete issues were reported to the supervisor and their repairs
were read in the updated manuscript:

1. C.2 requires a common RMS bound on *all* backward delta fields. The
   first draft supplied `max(H1,H2,D)`, omitting
   `||delta1||2<=11D^2`. The current manuscript uses
   `max(H1,H2,D,11D^2)` and explicitly checks the lower layer.
2. Hard cutoff second moments need not be continuous at atoms. The
   current proof transfers continuous quadratic ramps using
   `tau_(2R)(vtilde)<=2||vtilde-v||2+2||(|v|-R)_+||2`, which is valid
   pointwise before the L2 triangle inequality. The ramp is bounded
   above by the reference tail and has continuous quadratic growth.
3. Sharing a carrier alone does not establish dictionary-space
   invariance. The current manuscript gives finite-Euler invariance
   under measurable coordinates and both actions, including
   `K=P2 K P1`, and passes through the closed HS block.
4. III.F.10 is stated for C2 activations. The manuscript now cites
   A.4's bounded-Lipschitz-derivative scalar result and III.F.8--9's
   adjunction/curve rules for its C1,1 energy identity instead.

The fixed-mesh mollification argument is noncircular: every original
Euler value program is constructed by A.1, uniform C.2 constants are
obtained for smooth programs, and Fatou transfers the moments before
time or law completion. The law passage uses full raw-state convergence
and continuous compact-input Bochner integrands. Its bounded-exponential
test argument proves exactly the integrated backward estimate required
by the transport and closure comparisons; it does not need pointwise
passive Gaussian tails. The actual-law comparison is uniform in actual
atom counts because only the finite reference law supplies tails and
the actual law enters through a transport coupling.

The fixed-order continuum global continuation is also valid. To make
its implicit bounds explicit, let `B1,B2` bound the marks and let
`W=sqrt(2)+sqrt(T)`, `C=sqrt(T)`, `M*=||D_N||F+sqrt(T)` on a fixed
finite horizon. Energy gives these bounds for `w,c,M`; then

```
|a(u)| <= B1 (|phi(0)|+D W),
|d(u)| <= B2 D C,
|Z2(u)| <= B2 M* B1 (|phi(0)|+D W),
||q(u)||infinity <= B1 M* B2 D C.
```

Since `integral |r| dmu<=1`, these yield uniform finite bounds on
`c'` and `(w-g)'` in Linfty. Their integrals bound the characteristic
unknowns, while the matrix velocity is a finite product of the same
bounds. Hence Cauchy endpoints and locally Lipschitz continuation in
the fixed-order characteristic space are justified for arbitrary
Borel data laws. Neither bounded target activation nor bounded g is
being assumed.

One final completeness addition was requested: state finite-dimensional
local existence for each fixed-width Borel-law field directly from
Lipschitz `phi,phi'` and compact data, then use its exact finite metric
energy identity and finite endpoint continuation to obtain global finite
GF. This is a valid short argument; it is not an unresolved mathematical
obstruction. The all-law onset construction and its stated hierarchy
consequences have no remaining mathematical obstruction found in this
author-side check, subject to including that explicit finite-existence
argument and the independently handled numerical interface.

## Input record

Checked scientific dependencies: maintained `global_nonlinear.md` A.1--A.4,
C.1--C.2, C.4.1--C.4.4 and C.4.7.10 A--C; maintained
`special_data_limits.md` III.F; `docs/NOTATION.md`; and this study's
`CLOSURE_PROOF.md`. No experiment, maintained edit or Git operation was used.
