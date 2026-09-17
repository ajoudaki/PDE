# Follow-up analytical review of the quadratic conditioning-rate addendum

2026-09-16. **Verdict: PASS.** No required mathematical repairs.

This is a separate, bounded follow-up review of `resolution_rate.md`. It is
not part of, and does not retrospectively enlarge, the original frozen review
of `resolution_open_family.md`. No experiment, candidate edit, or promotion
was performed.

## Inputs and claim under review

The complete rate addendum was read at SHA-256
`e1053c8e0129c08afab58ac0354ffc7c1ad909aecfdb0ab15230e50961c1ba86`.
The previously permitted main candidate and complete symmetric dependency
retain their reviewed hashes:

- `resolution_open_family.md`:
  `6c949bdec4e78fb895ae71281edd328623a662cba433fba618d65e82055fe337`.
- `three_coordinate_candidate.md`:
  `531b1cb1fe5e5844fcc6da25486e6ee52450860030dd770246e3ee78592521ce`.

The review uses only the new addendum and those previously permitted canonical
inputs. No other route, root check, study README, synthesis, or other review
was read. Shared instructions were rechecked. No missing input blocks the
review.

For the exact initialized d=3 p=1 population closure, the seed directions
are v_i(e)=(1+e e_i)/q_e and q_e^2=3+2e+e^2. The statement concerns

    mu_e = min_{0<=s<=S_*} lambda_min(K_e(s)),
    K_e[i,j] = <grad f(v_i(e)),grad f(v_j(e))>/3,
    S_* = 2/C_*.

Here s is the declared auxiliary gradient clock, S_* is fixed independently
of e, and the inner product includes all physical gradient blocks. The
passing conclusion is the two-sided estimate c_- e^2<=mu_e<=c_+ e^2
for all sufficiently small e>0, with fixed finite positive constants. It
does not assert the same scaling for the scalar symmetric fitting rate,
nor quantify the nonsymmetric data-neighborhood radius.

## 1. Uniform bounds and the early coefficient contrast

The constants in (R2) follow from the auxiliary bounds in the frozen inputs.
In particular, ||M_s||_F<=s gives ||M-D||op<=s^2/2, and

    ||w_s||infinity <= B1 ||M||op ||c||2 <= Vbar s.

The vector L2 bound Wbar follows by adding the bounded increment to
||G||2=sqrt(3). All these bounds hold uniformly for e in [0,1] and
s in [0,S_*]. They require no input-dependent Gaussian supremum.

For fixed i!=j, the exact differentiated difference (R3) is justified by
bounded b1, bounded gates, and the bounded row speed. The contraction of
the feature adjoint and the displayed decomposition give

    |(Delta a)_s|
      <= ||w_s||infinity (2||w||2+1)|v_i-v_j|
      <= Abar delta s.

Thus (R4) follows with the stated factor 1/2. Its initial estimate is exact
at the required scale: the tanh Lipschitz bound and E[GG^T]=I yield
|Delta a(0)|<=delta. The identity

    M(s)Delta a(s)-D Delta a(0)
      = (M(s)-D)Delta a(0)+M(s)(Delta a(s)-Delta a(0))

and contraction of the upper feature map prove (R5), with
Zbar=(1+Mbar*Abar)/2. This is an O(e s^2) estimate for the difference
between two input coefficients along the same actual trajectory. An
O(s^2) estimate without the input-separation factor would not suffice;
the addendum retains that factor correctly.

## 2. Readout conditioning on the initial interval

For 0<=e<=1, b_e=1/q_e decreases from 1/sqrt(3) to 1/sqrt(6),
and a_e=(1+e)/q_e increases from 1/sqrt(3) to 2/sqrt(6). Both lie
in the stated compact interior interval I. The already supplied exact
Gaussian expression for kappa' is continuous and strictly positive there,
so k_->0 and k_+<infinity are valid analytic constants.

The initialized coefficient difference is exactly
theta_e(Z_i-Z_j). Independence, centering and E[Z_i^2]=tau give

    ||Delta z(0)||2 = sqrt(2 tau) theta_e
                    >= k_- sqrt(tau) delta.

The chosen s_0>0 guarantees Zbar*s_0^2<=k_-*sqrt(tau)/2. Subtracting
(R5) proves (R7) on all of [0,s_0], including s=0. The lower derivative
bound g_*=sech^2(B2*Mbar)>0 is legitimate because both preactivations
are pointwise in the fixed bounded interval. The integral mean-value
formula for tanh then gives the claimed lower bound on |H_i-H_j|.

Permutation invariance makes the readout Gram have one parallel and two
equal transverse eigenvalues. With the factor 1/3 in K, the transverse
eigenvalue is exactly ||H_i-H_j||2^2/6. Consequently

    lambda_perp(K_e^c)
      >= g_*^2 k_-^2 tau delta^2/24
      = g_*^2 k_-^2 tau e^2/(12 q_e^2)
      >= g_*^2 k_-^2 tau e^2/72.

The parallel eigenvalue is exactly C_e(s), not three times C_e(s).
The symmetric dependency gives C_e(s)>=C_e(0) for every auxiliary
s>=0, including after its physical fitting endpoint; it does not require
monotonicity of C_e. Initialization continuity gives C_e(0)>=C_*/2
for sufficiently small e. Since e^2<=1, the stated c_early is valid.
All other tangent blocks are positive semidefinite, so the full K has
the same lower bound on the initial interval.

## 3. Uniform positive lower response away from zero

The coincident-reference positivity mechanism is consistent with the frozen
main candidate. The constant coordinates are inactive by mark-sign symmetry.
Permutation symmetry gives the active upper field p(s)(Z_1+Z_2+Z_3),
with p(0)>0. The first-zero argument based on the exact positive-semidefinite
equation for (Ma)_s proves p(s)>0 on every finite auxiliary interval.
For s>0 this makes h(s)>0, while Ma!=0 implies M^T*1!=0. Linear
independence of the active lower features then makes Q_0 nonzero in L2.
The strictly positive finite-argument lower gate gives R_0(s)>0.

Thus continuity on the fixed interval [s_0,S_*], with s_0>0, gives
r_0>0. No positive lower bound as s tends to zero is assumed here.

The transfer to nearby seeds is also uniform in the required topology.
Finite-interval Hilbert dependence gives uniform convergence of w_e in
L2 and of the finite coefficients M_e^T d_{e,i}. Bounded b1 turns the
latter into uniform L-infinity convergence of Q_{e,i}. The input mismatch
is bounded by ||w_0||2 |v_i(e)-v_*|. With a common Qbar and the
Lipschitz bound four for sech^4, the explicit estimate in the addendum
then gives uniform R_{e,i}->R_0. Its two terms are valid by
|Q_e^2-Q_0^2|<=2 Qbar |Q_e-Q_0| and the L1 gate-difference bound.
There are only three input indices, so one e_0 works for all of them.

For the first-layer Gram the displayed pointwise quadratic-form bound is
correct, and the input Gram has smallest eigenvalue e^2/q_e^2. Including
the normalized factor 1/3 and R_{e,i}>=r_0/2 gives

    K_e^w >= r_0 e^2/(6 q_e^2) I >= (r_0/36)e^2 I.

Combining this with the early interval proves the stated positive c_-.

## 4. Matching upper bound and nonsymmetric consequence

At initialization c=0, so d=Q=0 and both hidden-gradient blocks vanish.
The full Gram is exactly the readout Gram. Its transverse eigenvalue and
the upper Lipschitz bound for tanh give

    mu_e <= lambda_perp(K_e(0))
          <= tau theta_e^2/3
          <= (tau k_+^2/9)e^2,

because q_e^2>=3. This checks c_+=tau*k_+^2/9 and proves sharpness
of the power two for this minimum, which includes initialization. It does
not claim that every trained time has this upper bound or that an optimal
loss-decay rate must scale as e^2.

The main open-family theorem may take k(e)=mu_e/2. Its finite-time
comparison and tail-capture proof permits shrinking the data neighborhood
for each fixed e, so the improved lower bound transfers exactly as stated.
Its mixed-potential rate is

    lambda(e)=min{2 C_e(0),mu_e}
              >= min{C_*,c_-}e^2,

using C_e(0)>=C_*/2 and e^2<=1. No uniform neighborhood in e is
needed or inferred. These are uniform rates across the neighborhood chosen
for each seed, after any additional shrinking required for the potential.

## Repairs and limits

**Required repairs: none.** The normalizations, numerical factors and norm
topologies in (R1)--(R13) are consistent. The constants are finite and
strictly positive analytic specifications; g_* and r_0 may be very small,
and the addendum appropriately makes no numerical calibration claim.

The proof closes the rate question for the declared auxiliary seed minimum
and the consequent certified nonsymmetric rate. It supplies neither a
quantified neighborhood radius, a uniform rate at coincident inputs, arbitrary
input geometry, a d=2 result, nor a trained-network limit.
