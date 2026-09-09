# Independent audit of the polynomial source-response candidate

Audited candidate: `/tmp/sharpen_response.md`, SHA-256
`094a9a79a3086230881ee91c5119e81bcde357dc7271c0fc4883d8721be275c7`,
followed by revised SHA-256
`51b0f717b33ed618219e086d32b16a95ef4253892171597d1805dd9d37a64f7f`
with the explicit `10^(-70) B^(-400)` threshold. The new neighborhood,
derivative, moment, and bootstrap
calculations were rechecked below.
Affine geometry inspected: `/tmp/sharpen_affine.md`, SHA-256
`8387e2f253063c139dacb282ca9f2372478521f54b33a9ef6c8dbd83f2b521ca`.
Exact source equations checked against `SOURCE_AND_LIMIT_BRIDGE.md` and
`sources/THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA.md`, especially (8), (9),
(11), (13), and (17). The baseline Gaussian-probe convention was also read.
The solve-math-rigorously skill was applied. No experiments, proof edits,
delegation, or commits were performed.

## Verdict

I found no mathematical obstruction in the proposed nonlinear closure.
In particular, solving the affine source recursions before applying a
random majorant genuinely removes the old nonperturbative `exp(P S)`.
Every unbounded gate derivative is `e Q` and enters a preactivation
equation through a strictly causal transfer with a polynomial density.
Current backward returns are output multipliers; no current inverse or
lower bound on a mesh step is needed.

The candidate is a **conditional interface lemma**. Its polynomial
conclusion requires the actual affine response/probe bounds, including
the enlarged initialization scale, in its Section 1. The affine geometry
note alone expressly does not supply those source bounds. This audit
does not certify the root's final numerical delta exponent or those
separate affine-input constructions.

The calculations below make the candidate's terse nonlinear argument
checkable. The specific constants are very oversized but consistent
with the displayed polynomial operations. I did not identify a need to
replace the claimed polynomial by a nonpolynomial bound.

## 1. Exact affine source map and its Jacobian

Write `A=A2`, `B=B3` for the middle population. Its affine source equation
is

    H2 = a xi2 + a² A (zeta2 + B H2).

Therefore, with `R=(I-a²AB)^(-1)`, the reverse-source derivative is
`V=a²RA`, and the forward-source derivative of delta2 is `W=a²BR`.
The corresponding bottom and top formulas are exactly the candidate's
`F` and `T`. No covariance parameter occurs in these formal affine
derivatives.

Using `L=I+BV=(I-a²BA)^(-1)` and `R=I+VB`, differentiation gives

    dF = F (dB2) F,
    dV = a² R (dA2) L + V (dB3) V,
    dT = T (dA3) T,
    dW = a² L (dB3) R + W (dA2) W.

Thus the candidate's coupled Jacobian is exact. The backward-forcing
shift is also exact: subtracting `J3` from `Y3` and
`a²L J3 R+J2` from `Y2` leaves only forward forcing

    E2 + F J2 F + a² F L J3 R F,
    E3 + V J3 V.

This works for arbitrary causal backward row forcing, including diagonal
forcing and entries without an `h_j` density.

For any causal row-bounded `Q` and strict-density `U`,
`|QU|_d <= |Q|_r |U|_d`. Consequently the strict sandwich estimate in the
candidate follows immediately by bounding the row norm of its first
strict factor. With the candidate's baseline bounds,

    |R|_r, |L|_r, |R1|_r, |R3|_r <= 2 B³,
    |FL|_d, |RF|_d <= 2 B⁴.

Hence shifted forward forcing has density at most a universal multiple
of `B^9` times the original forcing norm. No minimum time step enters.

## 2. Sample sectors and positivity scaling

At the folded affine baseline, the first/middle forward arrays are
diagonal in the active/inactive sample basis. The affine deltas are
sample-identical, so both backward coefficient arrays and `T,W` have
only an active-active block. For a coefficient variation in any other
sample sector, `T X3 T` and `W X2 W` vanish. There is therefore no ladder
feedback in those sectors. The candidate's triangular reconstruction is
valid there.

In the active sector, all raw finite Euler update polynomials have
nonnegative numerical coefficients in the independent initialized
Gaussian coordinates after the stated normalization and label folding.
Each Wick expectation of a monomial is nonnegative: an odd multiplicity
gives zero; an even multiplicity gives a product of positive variances.
This establishes the required nonnegative coefficients for active
learned moments. The source recursion then establishes them for the
active response coefficients by causal addition and multiplication.
This reasoning concerns expectations and deterministic coefficients,
and does not claim pathwise positivity of Gaussian weights.

Scaling the initial matrix variances by `beta²` does multiply each
initialized-matrix return by `beta²`; it does not multiply the learned
raw update by an extra `beta²`. Therefore the differentiated equation

    (I-J0) C' = 2(F,V,T,W) + M'

has the stated positive forcing. In the active sector, its two forward
components dominate `h_j/(8B)`, using `a>=1/2` and `v_u>=1/B`.
For a polynomial with nonnegative coefficients,
`f'(1) <= f(beta_*)/(beta_*-1)` follows term by term from
`beta_*^m-1 >= m(beta_*-1)`. Thus the assumed polynomial coefficient
bound at `beta_*` bounds `C'` in the mixed norm, including backward row
sums. This avoids differentiating a covariance square root.

The finite chronological inverse is positive in this scalar sector.
Comparison with `C'` therefore bounds its action on arbitrary forward
density forcing. Together with the exact shift, the advertised
`10^6 B^20` bound has ample slack: the shift costs order `B^9`, the
positive comparison costs order `B^3`, and the other sectors cost at
most order `B^15` by direct substitution.

## 3. Neighborhood resolvents do not need mesh-dependent smallness

Let `D` be the coefficient mixed-norm discrepancy. Row perturbations of
`a²A2B3`, `a²B3A2`, and `A3K3` are at most a universal multiple of
`B²D`; the bottom perturbation is at most `BD`. The baseline inverse row
bounds above then make the Neumann ratio at most a universal multiple
of `B^5D`. For example `D <= (12 B^5)^(-1)` suffices after harmless
enlargement of constants. The much smaller neighborhood in the
candidate meets this restriction.

Nearby inverse row bounds can consequently be taken as `4B³`.
Multiplying such an inverse by a forward coefficient or an integration
kernel gives strict transfers of density at most a universal multiple
of `B⁴`. The useful forms are

    R1 H_P,   R A2,   R3 A3,

and the corresponding affine direct source transfers. A strict factor
on the right, or the displayed strict sandwich, preserves the density.
This also justifies second-order inverse expansions in the mixed norm.
They involve a fixed number of row norms, strict densities and two
coefficient increments, so a bound `10^20 B^100 D²` is conservative.

## 4. Moment closure uses only deterministic row norms

At fixed actual coefficients, write the nonlinear source equations as
their affine equations plus the value remainders

    e atan(Z),    e g(Z) tau_R(q).

The first is bounded by `e pi/2`; the second by `e |q|`, independently
of the cap. Apply the same-array affine inverse separately in each
population, then reconstruct features, incoming fields and deltas.
The source Gaussian coordinates have `Lp` norm bounded by `C B sqrt(p)`
from the independent primal variance bound. Only a fixed number of
additional factors `B`, `S<=B`, and inverse row norms occur.

For orientation, the bottom solved forward field costs at most order
`B^5 sqrt(p)`, the middle at most `B^6 sqrt(p)`, and reconstruction of
the middle incoming field costs one more factor `B`. The nonlinear
remainder is bounded by a fixed polynomial times `e X_p`. Thus

    X_p <= C B^7 sqrt(p) + C B^7 e X_p

with enlarged universal constants is available. The candidate's
`Rstar=10^4 B^20` dominates this. This argument takes a maximum of
deterministic `Lp` norms over time, not the norm of a random time
supremum. It applies to every `p>=2` and gives the stated subGaussian
control.

## 5. Exact nonlinear derivative expansion

This is the main audit point. In the middle population put
`G=a+Gtilde`, `Vgate=a+Vtilde`, and retain `Lgate`. At frozen actual
arrays the exact derivative equation is

    J = Ixi + A2 [Lgate J + Vgate (Izeta + B3 G J)].

Subtract its same-array affine part and apply
`R=(I-a²A2B3)^(-1)`. The exact result is

    J = R(Ixi + a A2 Izeta)
        + R A2 [Lgate J + Vtilde Izeta
                + a Vtilde B3 J + a B3 Gtilde J
                + Vtilde B3 Gtilde J].

Here `|Gtilde|,|Vtilde|<=e` and `|Lgate_r|<=e Q_r`.
Since `RA2` has a polynomial strict density, the unbounded term gives

    P e sum_{r<k} h_r Q_r |J_r|.

Each other unknown term gives at most

    P e sum_{r<k} h_r max_{v<=r}|J_v|,

using the deterministic backward row bound. The factor `e²` is bounded
by `e`. The bottom calculation is identical with `H_P` in place of
`A2`. At the top, substitute `T=H_c G J` before applying the affine
inverse; all additional feedback again goes through the strict
transfer `R3 A3`, and only `Lgate_r J_r` contains `Q_r`.

Consequently a literal positive finite recursion yields

    |J_k| <= P f exp(P e s_k + P e sum_{r<k} h_r Q_r).

For a single transpose source `f=h_j`: its only explicit injection
passes through an integration kernel or `A2_{kj}`, so it has that
factor, and the derivative is zero before the source time. For full
forward rows, `f=1` and the direct identity row has row norm one.
There is no need to assign an `h_j` factor to each past forward-source
entry.

Backward output differentiation has the terminal factor
`P(1+eQ_k)`. In particular `Lgate_k J_k` is retained. This is a direct
output term: the preactivation equations only use earlier deltas, so it
does not require inverting a matrix involving `h_k Q_k` or any current
nonlinear gate.

## 6. Envelope moments and derivative defect

Let `||Q_r||_p <= K sqrt(p)` with polynomial `K`. For any fixed moment
order `m`, Jensen with weights `h_r/S` gives

    E exp(m P e sum h_r Q_r)
      <= 1-s_k/S + sum (h_r/S) E exp(m P e S Q_r).

A subGaussian variable has bounded linear-exponential moment whenever
the coefficient times its subGaussian norm is bounded. Hence the
right side is universally bounded once `e P S K` is sufficiently
small, as the candidate's restriction ensures. Hölder handles one or
several terminal/source `Q` factors; their fixed moments are
polynomial in `K`. No temporal independence is needed.

Subtracting the same-array affine derivative equation leaves exactly
the bracketed terms in Section 5, with an additional bounded `Gtilde`
at a feature output. Applying the same strict transfer gives expected
defect at most `P e h_j` for a transpose source and `P e` for a full
forward row. Backward output reconstruction adds its terminal
`Lgate_k J_k` and deterministic coefficient row, giving the same
polynomial row defect. All factors are fixed-depth products of inverse
bounds, time length, coefficient norms, and bounded envelope moments.
With the explicit loose bounds used in the candidate, degree 200 and
coefficient `10^30` leave ample slack.

This calculation verifies the required absence of a hidden `exp(P S)`.
Replacing the original affine Volterra feedback by a fresh Gronwall
bound would lose this property, but the candidate does not do that.

## 7. Covariance, continuity, and the final bootstrap

The affine formal derivative map depends on the deterministic source
coefficient arrays only. Its value is independent of the Gaussian
covariance used to realize the same-array affine source fields.
Therefore the nonlinear defect calculation above uses the actual
nonlinear source covariance only to bound moments; it never varies or
differentiates that covariance. The learned-moment difference is a
separate forcing supplied by the common raw primal comparison.

At each fixed mesh and finite cap, the causal source construction is
continuous in the amplitude. Gaussian square-root continuity gives
couplings even at rank loss. Formal derivatives are finite causal
compositions with bounded first derivatives at fixed cap, so their
expectations pass continuously using their finite-program bounds.
Off-support named slots stay distinct. These are precisely the
conditions needed for amplitude homotopy; no covariance inverse is
required.

Combining the coefficient-map Taylor expansion with the derivative
defect and learned-moment forcing gives, in the revised candidate,

    D <= 2·10^36 B^220 e + 10^26 B^120 D².

Take `d0=(4·10^26 B^120)^(-1)` and `e<=10^(-70)B^(-400)`.
On `D=d0`, the quadratic term is `d0/4`. The linear term divided by
`d0/4` is at most `3.2·10^(-7) B^(-60)<1`. Also
`e Lstar S Rstar <= 10^(-58) B^(-329)`, so the exponential-moment
restriction is met. Thus the first-exit homotopy is valid. It bounds all
coefficient arrays and validates the moments previously derived on
that neighborhood. Cap and mesh do not occur in the restriction.

The revised draft supplies sharper intermediate bounds
`|F|_d<=2B`, `|V|_d<=4B`, `|T|_r<=2B`, inverse rows at most `9B³`,
and source moments at most `10^4B^8 sqrt(p)`. I checked their displayed
identities and constant estimates. Its largest second-variation
terms have orders `B^11D²` for V and `B^14D²` for W, consistent with
the stated `5000` and `20000` bounds for B>=2 and well below the final
Taylor bound. The revised explicit remainder expansion agrees with
Section 5 of this audit.

## Remaining checks outside this audit

1. Prove the actual affine source/probe bounds using the integrated
   raw Hessian, including the finite-mesh/finite-width passage. A
   population primal bound alone does not identify this propagator.
2. Supply a common enlarged initialization scale `beta_*` with
   polynomial inverse gap, existence through the original horizon,
   and polynomial probe constants there.
3. Substitute a verified polynomial `B_delta` into the interface
   threshold. The candidate correctly labels its suggested exponent
   20 for `B_delta` as conditional.

These are input obligations, not defects in the nonlinear resolvent
closure examined here.
