# Isolated adversarial review: relative gates and first-velocity compactness

Date: 2026-09-06.

Sole mathematical source: `/tmp/l2-two-sample-proof-0ywjpp/ALL_ANGLE_FIRST_VELOCITY_COMPACTNESS.md`.

Verified SHA-256: `a78c7439023d51e19e17b57e0105521a81fb09ccfc1920b32e97f376fdf6d742`.

The source was read completely, lines 1–211. References below use those
line numbers and its equation numbers. Neither candidate note named in
the source was opened. No other mathematical file, external source,
experiment, or agent was used. The rigorous-math skill was used only as
a procedural audit guide. The source was not edited.

## 1. Precise verdict and accepted scope

**PASS for the stated bounded conditional implication.** For fixed
`0<T<infinity` and fixed `rho in (-1,1)`, the array relations (3) or (4),
the explicit uniform bounds (5), and the control-increment bound (6)
give the claimed first-velocity translation estimates. They give
quadratic-Wasserstein relative compactness of the joint position and
velocity empirical laws for GF, and for the GD sequence with vanishing
step size explicitly specified at lines 144–147 (`eta_n=n^-2`). The
proof equally permits any sequence `eta_n -> 0` with those same uniform
bounds. The limit retains the position–velocity integral relation and
the expected integrated squared first velocity, so there is no defect
in that kinetic energy along a convergent subsequence. The recomputed
activation and its actual time derivative may be included jointly.

No additional bound on the magnitude of `u`, no gate lower bound, no
matrix-action moment, and no independence assertion is needed for this
conditional conclusion. Constants in the translation estimates depend
on the stated uniform bounds as well as on `T,rho`.

The vanishing-step regime is explicitly supplied in Section 4; it is
not a consequence of (3)–(6). It is the regime used by the displayed
GD projection argument. At fixed positive `eta`, the bound
`C(h+eta)^(2/3)` does not tend to zero as the projection mesh `h` tends
to zero. This observation limits that argument; it is not a
counterexample to compactness under some other argument or regime.

**Two application assertions remain unverified:** the claimed derivation
of (5)–(6) for the actual finite GF/raw-GD schemes (lines 73–82), and the
claimed exact anti-odd network invariance at `rho=-1` (lines 84–90).
Neither follows from the accepted array hypotheses. The algebraic
endpoint extension is valid if the exact invariant condition is
separately supplied. These reservations do not invalidate the
nondegenerate conditional implication.

This is not an all-angle population theorem, a verification of the
finite-network action estimates, or an identification of a population
velocity equation.

## 2. Relative gate: both endpoint velocities are essential to this proof

Source: lines 12–31, equations (1)–(2).

Put `a=p(x)>0`, `b=p(y)>0`. Directly,

    |a-b|/(a+b) = tanh(|log a-log b|/2).

Since `|(log p)'|=|2x/(1+x^2)|<=1` and `tanh r<=min(1,r)` for
`r>=0`, equation (1) holds, including `x=y`. There is no singular
denominator because `p` is strictly positive at every finite argument.
No uniform lower bound on `p` is asserted or needed.

For `d=au`, `e=bv`, and `theta=|a-b|/(a+b)`,

    |d-e| <= a|u-v| + theta(a+b)|v|
           <= (1+theta)a|u-v| + theta(|d|+|e|)
           <= 2|u-v| + theta(|d|+|e|).

The middle step uses `a|v|<=a|u|+a|u-v|=|d|+a|u-v|`.
Thus zeros or signs of `u,v`, or of any residual represented inside
them, present no exception. In particular, the estimate has not
silently replaced either endpoint weighted field by an unweighted
control that lacks a moment bound.

For two coordinates, apply this scalar inequality to each coordinate.
With `theta=max(theta_1,theta_2)`, the Euclidean triangle inequality
gives

    |d-e|_2 <= 2|u-v|_2 + theta(|d|_2+|e|_2).

Also `theta<=min(1,|x-y|_2/2)`. The two sample coordinates therefore
remain together in the same neuron vector. Equation (2) and its vector
extension are correct.

## 3. Time translations, exponent, and the GF/GD distinction

Source: lines 35–71 and 94–125, equations (3)–(9).

All shifted norms must be taken on

    Omega_tau = {1,...,n} x [0,T-tau],
    measure = (1/n) sum_i dt,       0<tau<T.

This is the natural interpretation of the source. No zero extension,
periodic extension, or evaluation beyond `T` is needed.

Write `v=dot z` and use `||.||_RMS` for the empirical Euclidean norm at
a fixed time. For GF, integrating the derivative bounds gives

    ||z(t+tau)-z(t)||_RMS <= K tau,
    ||u(t+tau)-u(t)||_RMS <= K_u tau.

There is no hidden absolute-continuity assumption here under the
source's GF wording: at each finite `n`, differentiability and the
pointwise RMS derivative bounds bound each individual derivative by a
finite constant, hence give Lipschitz paths. A statement allowing only
a.e. differentiability of otherwise arbitrary paths would instead
need absolute continuity; that weakening is not used in this review.

For raw GD, let `u_k, z_k` be the left-node values. The number of
increments between the nodes containing `t` and `t+tau` is at most
`tau/eta+1`. Consequently,

    ||u(t+tau)-u(t)||_RMS <= K_u(tau+eta),
    ||bar z(t+tau)-bar z(t)||_RMS <= K(tau+eta).

For the second inequality, each full node increment is `eta v_k`,
whose RMS is at most `K eta`. The actual affine interpolation also
satisfies the sharper bound

    ||z(t+tau)-z(t)||_RMS <= K tau.

The last truncated GD cell is harmless: its actual interpolation is
integrated only up to `T`. No full increment beyond `T` is needed in
the shifted-time integrals. Values at the finitely many nodes may be
assigned by the left-node convention; changing those values does not
change an `L2` or `L3` quantity.

Integrating the squared control estimate over `[0,T-tau]` proves (6)
with the stated `sqrt(T)` factor. These steps use RMS triangle
inequalities, not independence of coordinates or neurons.

For fixed `rho in (-1,1)`, the eigenvalues of `C` are `1+rho` and
`1-rho`. Thus

    ||C||_op = 1+|rho|,
    D := ||C^(-1)||_op = 1/(1-|rho|),
    ||d||_L3 <= D J.

Each of the two shifted restrictions of `d` to `Omega_tau` has `L3`
norm at most `D J`. With `r=tau+e`, the gate ratio obeys

    theta^6 <= theta^2 <= |Delta(z or bar z)|^2/4,
    ||theta||_L6 <= (T K^2/4)^(1/6) r^(1/3).

In particular, the exponent is exactly `1/3`: the squared increment
is `O(r^2)`, followed by a sixth root. It is neither a claimed
pointwise temporal exponent nor a bound on an individual neuron's
increment uniform in `n`.

Because `1/2=1/6+1/3`, applying the two-endpoint gate bound gives the
explicit estimate

    ||d(.+tau)-d(.)||_L2
      <= 2 sqrt(T) K_u r
         + 2 D J (T K^2/4)^(1/6) r^(1/3).

Multiplying by `||C||_op` gives the corresponding velocity estimate.
This verifies (9). Absorbing the linear term requires only a bounded
range of `r`, as the source states. In the specified GD sequence one
can restrict to `eta<=1` and omit finitely many preceding terms.

For clarity, write `a=arctan(z)` for the recomputed activation called
`h` in the source, and `w=dot a`. For both schemes,

    w(t)=diag(p(z(t)))v(t)                 a.e. in time.

Here `z` is the actual continuous interpolation, including in GD.
Since `p<=1` and `|p'|=p |(log p)'|<=1`,

    |w(t+tau)-w(t)|
      <= |v(t+tau)-v(t)| + beta(t)|v(t)|,
    beta(t) <= min(2,|z(t+tau)-z(t)|).

Then `beta^6<=16|Delta z|^2`, so

    ||beta||_L6 <= (16 T K^2)^(1/6) tau^(1/3).

Another `L6 x L3 -> L2` application proves the asserted translation
bound for `w`. The gate inside the GD update is frozen at `bar z`,
whereas the gate in this chain rule is evaluated at `z(t)`. These
are correctly distinguished in the source. The derivative of a
polygon through the node activations is a different object and is
not used.

## 4. Singular endpoint and the unsupported invariance assertion

Source: lines 73–90 and 113–115.

The nondegenerate proof does not supply a uniform estimate as `rho`
approaches either endpoint. Its constant `D` diverges. It cannot be
applied to an arbitrary sequence `rho_n -> +/-1` on the strength of
the stated uniform bounds alone.

At `rho=-1`, if the additional exact invariant condition

    d_i(t)=(b_i(t),-b_i(t))

holds at every relevant time or GD node, then `C d_i=2d_i` and

    |d_i|=|v_i|/2.

Replacing `D` by `1/2` in the preceding estimates validates the
conditional endpoint argument. The equality is stronger than the
inequality stated in the source. It requires no singular inverse.

One sufficient array-level symmetry is `z_2=-z_1` and `u_2=-u_1`
(using node positions for the GD gate). The evenness of `p` then gives
`d_2=-d_1`. The resulting position update preserves opposite
positions in GF and at every GD node and throughout affine cells.
What remains to be proved for an actual network is that its control
`u` has and preserves the required opposite-coordinate symmetry.

That condition is not implied by the array bounds. For example, if
one merely substitutes `rho=-1` into (3), the constant arrays

    z=(0,0),  u=(1,1),  d=(1,1),  v=C d=0

satisfy the displayed array relations and all the relevant bounds,
but do not satisfy `|d|<=|v|/2`. This is not a counterexample to the
conditional endpoint lemma; it shows why its invariant-subspace
premise cannot be dropped.

The sole source provides no full finite-network equations, control
definition, or symmetry-preservation calculation from which to verify
its stronger statements about forward fields, reverse fields,
residual controls, and a nonzero finite readout. Odd activations and
the label pair are not a substitute within this note for that missing
model-specific verification. Accordingly, the actual antiparallel
application is **unverified**, not disproved. The aligned endpoint
`rho=1` is explicitly outside the source's assertion.

## 5. Finite projections and quadratic-Wasserstein compactness

Source: lines 129–170, equations (10)–(11).

Let `H=L2([0,T];R^2)` and let `h=T/m`. The uniform time partition used
here is independent of the GD step partition. For an interval `I` of
length `h`, put `v_I=h^(-1) integral_I v`. Expanding both sides gives

    integral_I |v-v_I|^2
      = integral_I |v|^2 - h|v_I|^2
      = (1/(2h)) integral_I integral_I |v(t)-v(s)|^2 ds dt.

Thus the factor `1/(2h)` is correct. Also,

    ||P_h v||_H^2 = h sum_I |v_I|^2 <= ||v||_H^2.

The finite-dimensional Euclidean coordinates can be chosen as
`sqrt(h) v_I`; using unweighted cell averages as coordinates must
retain this factor in the norm.

By symmetry in the double integral and the substitution `s=t+tau`,

    sum_I integral_I integral_I |v(t)-v(s)|^2 ds dt
      = 2 integral_0^h sum_I integral_{t,t+tau in I}
                    |v(t+tau)-v(t)|^2 dt dtau.

Enlarging the inner domains to `[0,T-tau]` and averaging over neurons
gives exactly

    (1/n) sum_i ||v_i-P_h v_i||_H^2
      <= (1/h) integral_0^h ||v(.+tau)-v(.)||_L2(Omega_tau)^2 dtau
      <= C(h+e)^(2/3).

This verifies (10), with no missing endpoint term or missing factor
of two. There is no boundary-extension hypothesis. The same proof
applies to `w=dot a`.

The third bound in (5) states precisely

    (1/n) sum_i ||v_i||_H^4 <= A^2.

It is a fourth moment of the `L2` path norm, not a spacetime `L4`
bound on the velocity. Projection is a contraction, so (11) follows
with exactly the same bound. For any projected law `nu`,

    integral_{||x||>R} ||x||^2 dnu(x) <= A^2/R^2.

This is the quadratic-tail estimate needed for `W2`. A bounded
second moment alone would not give it.

Here is an explicit justification of the finite-dimensional
compactness step. Fix `h`. Cover the radius-`R` ball in its
finite-dimensional image by finitely many balls of radius `delta`.
Map each point of the ball to a covering center, using a fixed
tie-breaking rule, and map the complement to zero. This is a Borel
finite-valued map `q`, with

    W2(nu,q_#nu)^2 <= delta^2 + A^2/R^2.

On that one finite support the vector of probability masses has a
convergent subsequence. If two such vectors are close, match the
common mass at each point and transport the unmatched mass a
distance at most the support diameter. The squared transport cost is
at most the squared diameter times half the sum of the absolute mass
differences. Thus convergence of these masses gives `W2` convergence.
Taking large `R` and small `delta` proves total boundedness of the
projected laws. The moment bound and finite dimension are both used.

Let `mu_n=(1/n)sum_i delta_{v_i}`. The same-neuron coupling gives

    W2(mu_n,(P_h)_#mu_n)^2 <= C(h+eta_n)^(2/3)

for GD, and the same estimate with `eta_n=0` for GF. For GD, choose
a small fixed `h` and then a sufficiently late tail of the sequence
so that `eta_n` is small. The projected tail has a finite `W2` net;
the coupling transfers this to a net for the original tail. The
omitted finite prefix can be covered by finitely many additional
points. This proves total boundedness in the full `H`, rather than
merely tightness of each projection. It also explains why the order
of limits at lines 145–147 is legitimate.

No heavy compactness or representation theorem is needed to produce
a limit. Extract a `W2`-Cauchy subsequence with successive distances
at most `2^-k`. Its members are finite empirical laws, so choose
finite transport tables whose square-root costs are summable. Glue
the tables by using, at each positive-mass atom, the next table's row
divided by that atom's mass as transition probabilities. Zero-mass
rows are irrelevant. This construction can be realized by successive
subdivisions of `[0,1]` into intervals of the prescribed masses.

The resulting `H`-valued variables `X_k` have the required marginal
laws and satisfy

    sum_k (E||X_{k+1}-X_k||_H^2)^(1/2) < infinity.

Their distances are summable almost surely because the expectation
of their sum is finite. Completeness of `H` gives a measurable
almost-sure limit `X`; the same summability and the triangle
inequality in mean square give `E||X_k-X||_H^2 -> 0`. In particular
`X` has a finite second moment, and its law is the `W2` limit. This
fills in the constructive completeness sketch at lines 166–170.
Only elementary finite transport and completeness are required.

## 6. Joint topology, measurability, and kinetic energy

Source: lines 172–194, equation (12).

Use the explicit product metric

    D((z,v),(z',v'))^2
      = ||z-z'||_infinity^2 + ||v-v'||_H^2

on `E=C([0,T];R^2) x H`. Both factors, and hence `E`, are complete
and separable. An equivalent fixed product norm gives the same
convergence assertion. The Wasserstein claim is for probability laws
on this space, with strong `L2` in the velocity coordinate.

Let `Pi_h z` be the polygon through the actual values `z(jh)`,
including `z(T)`. On one cell `I=[b,b+h]`, absolute continuity gives

    |z(t)-Pi_h z(t)|
      <= |integral_b^t v| + ((t-b)/h)|integral_b^(b+h) v|
      <= 2 sqrt(h) (integral_I |v|^2)^(1/2).

Taking the supremum and then averaging proves the source's bound

    (1/n) sum_i ||z_i-Pi_h z_i||_infinity^2
      <= 4h (1/n) sum_i ||v_i||_H^2 <= 4h T K^2.

Moreover `(Pi_h z)'=P_h v` a.e.; the finite approximation even
preserves the integral relation exactly. Its two coordinates are
coupled through the same neuron. Separate marginal subsequence
arguments, which would not by themselves identify the joint law,
are not being used.

Polygonal interpolation is a supremum-norm contraction, and `P_h`
is an `H`-norm contraction. Thus the projected joint laws have the
uniform fourth-norm bound

    (1/n) sum_i (||Pi_h z_i||_infinity^2+||P_h v_i||_H^2)^2
      <= 2(B+A^2).

There is no missing initial-position moment: the bound `B` in (5)
already bounds `(1/n)sum_i |z_i(0)|^4`. The displayed bound above
directly supplies quadratic tails in the joint metric. The joint
same-neuron approximation has squared cost at most

    4h T K^2 + C(h+e)^(2/3).

Its range is finite-dimensional. The finite-cell argument and the
constructive limit argument from Section 5 therefore apply in `E`
and establish (12).

There is also no hidden measurability problem for the deterministic
arrays under review. Continuous paths are elements of `C`, and the
velocities define Borel `L2` equivalence classes; the GF derivative
is a limit of measurable difference quotients, and GD velocities
are step functions. The empirical laws are finite sums of point
masses. Node evaluation for `Pi_h` is applied to continuous positions,
not to `L2` equivalence classes. Cell integration for `P_h` is a
continuous operator on `H`. All the approximation maps used above
are consequently Borel. The finite quantizers can be made Borel by
the stated tie-breaking convention.

To verify the limit's integral relation without an implicit
representation theorem, define the continuous defect function

    R(z,v)=||z(.)-z(0)-integral_0^. v(s)ds||_infinity.

It satisfies

    |R(z,v)-R(z',v')|
      <= 2||z-z'||_infinity + sqrt(T)||v-v'||_H.

Every original pair has `R=0`. If its joint law converges in `W2`
to `mu`, coupling to `mu` and using this inequality gives
`integral R^2 dmu=0`. Hence the integral relation holds for
`mu`-almost every pair, simultaneously for all `t in [0,T]`.
The endpoint values of the position are included; pointwise endpoint
values of the velocity are neither needed nor claimed to converge.

For the energy conclusion, any coupling of `(z,v)` and `(z',v')`
gives

    |E||v||_H^2-E||v'||_H^2|
      <= (E||v-v'||_H^2)^(1/2)
           [(E||v||_H^2)^(1/2)+(E||v'||_H^2)^(1/2)].

The second moments are bounded and the coupling cost tends to zero
under `W2` convergence. Therefore

    lim_n (1/n) sum_i integral_0^T |dot z_i(t)|^2 dt
      = integral_E ||v||_H^2 dmu(z,v).

This is exactly the absence of a defect in the tracked first-velocity
kinetic energy. The same reasoning works on any fixed time subinterval.
It asserts convergence of energies of laws under suitable couplings,
not convergence of a prescribed original neuron across widths.

For the optional larger tuple, `a=arctan z` satisfies
`||a||_infinity<=||z||_infinity` and `||w||_H<=||v||_H`.
The position and fourth-moment bounds therefore carry over, and the
translation bound for `w` was verified in Section 3. Project both
positions and both velocities in the same neuron tuple. The same
argument gives joint `W2` compactness and energy convergence for
`w` as well. The identities `a=arctan z` and `w=diag(p(z))v` survive
the limit: uniform convergence of `z` gives uniform convergence of
the gates, and strong `L2` convergence of `v` then gives convergence
of their product in `L2`.

These conclusions are deterministic statements about empirical laws.
They apply pathwise to random arrays on an event where all the
required bounds hold uniformly over the sequence. No probabilistic
mode of convergence, common almost-sure event, deterministic limit,
or annealed moment bound follows unless the corresponding random
hypotheses are separately provided. The source's deterministic
formulation does not require such additional hypotheses.

## 7. Required obligations versus optional improvements

### Required to apply or extend the conditional lemma

1. **Actual finite schemes:** independently establish all the uniform
   bounds in (5) and the control-increment bound (6), together with
   the stated array identities, for the intended family of finite
   schemes. The assertions at lines 73–82 were not verified here.
   In particular, a per-neuron work estimate gives the `A` bound
   only together with the claimed uniform RMS envelope bound; this
   review imports neither one. The wording at lines 198–199 about
   “actual first-layer work bounds” must be read conditionally.
   Lines 205–206 correctly retain the obligation to verify them.
2. **Antiparallel application:** prove exact anti-odd control and gate
   compatibility for the specified network, initial data, and GF/GD
   update, including any finite readout. Alternatively, state exact
   `d=(b,-b)` as an additional hypothesis for an endpoint lemma.
   Neither oddness of the activation alone nor a singular inverse
   proves that assertion from the present array hypotheses.
3. **Scope when quoting the result:** retain fixed `T,rho`, uniform
   constants, and the source's vanishing-step regime for the GD
   projection proof. Retain the joint strong topology and the
   deterministic or explicitly pathwise interpretation. Dropping
   these qualifications requires another argument.

No new uniform moment hypothesis or repair to an inequality is
required for the nondegenerate bounded conditional conclusion.

### Optional exposition improvements

- Define the shifted integration domain `[0,T-tau]` and the product
  metric in (12) explicitly.
- Write that `C_{T,rho}` also depends on the uniform `K,J,K_u` bounds;
  its notation currently suppresses those dependencies.
- Avoid reusing `h` for both the activation and the projection mesh.
- Include the projected norm formula, the fourth-moment tail estimate,
  and one explicit finite-mass transport argument from Section 5
  above. These make the compactness proof easier to audit; the
  source's sketches have valid elementary completions.
- State the closed integral relation and energy convergence at the
  level of laws, to prevent a stronger claim about matching original
  neurons across widths or about pointwise velocity traces.

## 8. Coverage record

| Requested audit | Result |
| --- | --- |
| Relative gate with two endpoint velocities | Correct; no division by a control or residual, and no gate lower bound. |
| `L3 x L6` and the translation exponent | Correct `1/3`; the full two-endpoint estimate is derived above. |
| GF versus frozen-node raw GD | Correct distinction; recomputed activation uses the actual affine position. |
| Invertibility and angular endpoints | Correct for fixed `abs(rho)<1`; no uniform endpoint passage. |
| Exact anti-odd invariance | Conditional endpoint algebra correct; actual-network invariance unverified from this source. |
| Finite-cell projection norm identity | Correct factor, time-domain enlargement, and weighted Euclidean norm. |
| Velocity-law `W2` with a fourth norm moment | Correct; finite projections and uniform quadratic tails are both essential to this argument. |
| Joint `C x L2` compactness | Correct same-neuron approximation, moment control, and strong product topology. |
| No first kinetic-energy defect | Correct for the tracked velocities along `W2`-convergent subsequences; no limiting force equation identified. |
| Probability, topology, endpoints, measurability | No fatal gap under the stated deterministic interpretation; qualifications are explicit above. |
| Actual finite-scheme bounds / population claims | Not established or imported; outside this isolated conditional verdict. |

Final disposition: **accept the bounded conditional lemma; retain the
finite-scheme and exact-invariance verification obligations. Do not
promote this review to an all-angle population theorem.**
