# Isolated adversarial review: INITIAL_FEATURE_LEARNING.md

Verdict: **PASS, within the conditional scope specified below.**

No mathematical gap was found in equations (1)--(7), including the
repeated-matrix transpose corrections, the antipodal case, positivity
in the raw metric, acceleration of both samples in every hidden layer,
and the initial kernel expansions. The bounded-derivative extension at
this fixed initial transcript and the claimed sufficiency of a strong
C1 solution are valid. Details of the potentially delicate steps follow.

## Exact scope and isolation

The initial-law conclusions hold for every fixed epsilon>0, each label
pair in {+1,-1}^2, and every fixed rho in [-1,1), with the initialization
and normalization of CONTRACT.md. The actions are the canonical bounded
Gaussian population actions with their actual adjoints and the permitted
fixed-program joint laws. These are population/empirical-limit claims,
not exact coordinate independence assertions at finite width.

The path conclusions assume an already constructed solution of the full
raw feature equations

    theta'(s) = J_s^* C(s),    C'(s) = H(theta(s)),    C(0)=0,

which is C1 in the affine raw Hilbert state space near s=0. Here theta
contains the first weight field and the HS increments of the two hidden
actions. C'=H alone, on an arbitrary curve not solving the hidden
equations, would not suffice. The physical-clock interpretation uses the
constructed symmetric path covered by SYMMETRY_RADIAL_CLOCK.md.

This verdict does not establish construction, uniqueness, nonlinear
comparison, continuation, a two-sample width/GF/GD theorem, nonaffinity
under every later hidden law, or nonzero velocities at every later time.
There is no assertion uniform as rho approaches 1 or epsilon approaches
0. The candidate expressly excludes these stronger conclusions.

The required solve-math-rigorously SKILL.md was read in full. Only the
candidate and its four authorized dependency files were consulted.
Within TWO_SAMPLE_SOURCE_BASELINE.md, the substantive reading was
Section 1 for conventions and Section 3 for fixed-program identification.
Within SYMMETRY_RADIAL_CLOCK.md, it was the normalization, symmetry,
raw strong chain rule, kernel normalization, and clock passages in
Sections 1--4 and 6. Within L3_LOCAL_COMPLETE_PROOF.md, it was the
fixed-program Gaussian conditioning/source rule and bounded-action,
adjunction, and raw HS-space passages; its feature-learning proof was
not read or used. Section headings/search hits were used to locate these
permitted passages. No other notes, history, or reviews were inspected.
No experiments, numerical computations, or agents were used. The
candidate was not modified.

## 1. Forward laws and both transpose returns

Candidate lines 20--47 correctly use uncentered feature second moments.
When -1<rho<1, full support and continuity reduce a zero feature
combination to an identity on R^2; varying either coordinate forces its
coefficient to vanish. At rho=-1, phi(Z)=1+psi(Z) and
phi(-Z)=1-psi(Z), with psi odd and nonconstant. The constant and odd
parts force both coefficients to vanish. Thus the first feature Gram
is positive definite even though the first preactivation covariance is
singular. The independent forward calls then give full-support Gaussian
pairs in layers two and three, whose feature Grams are positive definite.
Linear growth of phi gives every finite initial moment.

For S_3, fix z_2 in the displayed product identity. Because p_1 is
nonzero and phi is strictly increasing onto R, the factor H has at most
one zero as a function of z_1. The second factor vanishes away from that
zero and hence everywhere by continuity. Differentiation gives
u_1 phi''(z_1)=0. Here

    phi'(z)=1+epsilon/(1+z^2),
    phi''(z)=-2 epsilon z/(1+z^2)^2,

so epsilon>0 forces u_1=0, then u_2=0. This proves S_3>0 for both label
choices, including opposite labels at rho=-1.

To check the formal derivatives explicitly, define deterministic

    m_ab = E_3[partial_{z_b}(H_0 phi'(z_a))]
         = E_3[p_b phi'(z_b)phi'(z_a)
                    + 1_{a=b} H_0 phi''(z_a)].

The first transpose has exactly the candidate's form

    q^(2)_a = G^(2)_a + sum_b m_ab H^(2)_{b,0},
    Cov(G^(2)) = S_3 = E_3[beta^(3)(beta^(3))^T].

This is the full joint second-moment covariance. A residual covariance
arising during sequential Gaussian conditioning is only the covariance
of the newly added scalar innovation. Combining it with the prior
same-orientation Gaussian sources gives S_3. Neither centering beta nor
subtracting a forward-feature projection is appropriate in (1).
The opposite-orientation response is the displayed m term; it does not
alter the independence of the Gaussian source group from the initial
population-two forward sources.

At initialization z_b^(2)=xi_b^(2). With m and all covariance parameters
held fixed, the complete derivative needed for (2) is

    partial_{xi_b^(2)} beta^(2)_a
      = 1_{a=b} phi''(z_a^(2))
          [G^(2)_a + sum_c m_ac phi(z_c^(2))]
        + phi'(z_a^(2)) m_ab phi'(z_b^(2)).

In particular, the second term must be retained: it differentiates the
response through the other matrix. G^(2) is a separate formal source,
not a covariance-square-root function to differentiate. This is exactly
the derivative convention in candidate lines 95--100 and in the allowed
fixed-program dependency. Its expectation is the response coefficient
for the second transpose.

Writing D_2=diag(phi'(Z^(2)_{a,0})), conditional covariance gives

    Cov(beta^(2) | Z^(2)_0) = D_2 S_3 D_2
                           >= lambda_min(S_3) I.

Consequently S_2=E_2[beta^(2)(beta^(2))^T]>0. The second transpose is
G^(1) plus the two first-layer features times the expected derivatives
above, with Cov(G^(1))=S_2 and G^(1) independent of the initial root pair.
There is no missing label multiplier or extra return term in (1) or (2).

The bounded-instruction issue at lines 68--76 and 100 is not a gap at
this fixed transcript. The forward activation is globally Lipschitz.
The two uncapped backward coordinate maps are continuous with at most
linear growth in their displayed finite Gaussian/source arguments:
their gates are bounded. Smooth caps make their first derivatives
bounded, allowing the cited theorem. Initial joint W2 convergence
controls the second-moment tails of these linear-growth inputs, so the
cap errors vanish in RMS. Bounded matrix actions propagate each input
error in L2. The resulting source formulas give Gaussian variables plus
linear-growth feature responses; all their finite moments exist.
Expected formal derivatives above converge under cap removal by their
Gaussian moment bounds. Caps can be removed successively through the
finite transcript. This argument requires no mesh-uniform estimate or
uncut-path limit.

## 2. Tensor positivity and the first raw metric

Let P=diag(p_1,p_2), and let M be the relevant preceding-layer feature
Gram. For either matrix block, the candidate's norm formula is

    ||V^(ell)||_HS^2 = tr[(P S_ell P) M],    ell=2,3.

Both factors are positive definite: P is invertible even for opposite
labels. The trace is positive because it equals the trace of the
positive definite matrix M^(1/2) P S_ell P M^(1/2). This calculation uses
separate population inner products, without pairing neurons across
layers. The tensor u tensor v has HS norm ||u||_2 ||v||_2 and finite
representative uv^T/n, as required by the raw matrix Frobenius metric.

For the first field, let X have columns x_1,x_2 and set
D_1=diag(phi'(Z^(1)_{a,0})). Conditional on the first root pair,

    Cov(V^(1) | Z^(1)_0)
      = d^(-2) X P D_1 S_2 D_1 P X^T.

Taking traces, retaining the nonnegative conditional-mean contribution,
and using D_1^2>=I gives

    d E_1||V^(1)||^2
      >= lambda_min(S_2) d^(-1) sum_a p_a^2 ||x_a||^2
       = lambda_min(S_2)/2.

Thus both the 1/d in V^(1) and the d in its raw squared norm are
correct. This proof uses neither an inverse of Gamma nor independence
of the two first-layer preactivations. It includes x_2=-x_1.

Adjunction of the bounded forward linearization in the same metric
gives V=J_0^*H_0. There is no need for Frechet differentiability of the
L2-valued nonlinear feature map.

## 3. C1 suffices for the initial backward and state limits

Here is the precise multiplier argument behind candidate lines 138--144.
If a_s are uniformly bounded multipliers converging in probability to
a_0, and v_s->v_0 in L2, then

    ||a_s v_s-a_0 v_0||_2
      <= sup_s||a_s||_infinity ||v_s-v_0||_2
         + ||(a_s-a_0)v_0||_2 -> 0.

The last limit follows by truncating the fixed L2 vector v_0, using
bounded convergence in probability on its bounded part, and then
removing its L2 tail. No Lp path differentiability for p>2 is needed.

Raw state continuity implies forward L2 continuity, hence convergence
in probability of the bounded gates. Continuity of the HS increments
implies operator-norm continuity of both current actions and adjoints.
Also C'=H and C(0)=0 give C(s)/s->H_0 in L2. Applying the multiplier
argument first to delta^(3)/s and then backwards through the two bounded
adjoints proves

    delta^(ell)_a(s)/s -> beta^(ell)_a in L2,    ell=1,2,3.

The rank-one difference inequality then gives theta'(s)/s->V in the
raw hidden norm. Integration yields

    theta(s)=theta(0)+(s^2/2)V+o(s^2).

Thus (5) follows from the full strong C1 feature equation. This argument
does not infer existence from continuity of an infinite-dimensional
vector field, and it does not assume a second derivative of that field.

## 4. Every sample's hidden feature acceleration

At layer one,

    U^(1)_a = sum_b Gamma_ab p_b beta^(1)_b.

Its conditional variance is at least

    lambda_min(S_2) sum_b Gamma_ab^2 p_b^2 phi'(Z_b^(1))^2
      >= lambda_min(S_2)/4,

because Gamma_aa=1 and p_a^2=1/4. This proves nonzero L2 acceleration
for each sample, including at rho=-1.

The recursive upper preactivation accelerations are

    U^(2)_a = V^(2)H^(1)_{a,0}
               + W^(2)_0[phi'(Z^(1)_{a,0}) U^(1)_a],
    U^(3)_a = V^(3)H^(2)_{a,0}
               + W^(3)_0[phi'(Z^(2)_{a,0}) U^(2)_a].

Pair the first equation with p_a beta^(2)_a and sum over a.
The direct tensor term is ||V^(2)||_HS^2. Moving W^(2)_0 to its actual
adjoint gives sum_a p_a E_1[beta^(1)_a(V^(1) dot x_a)], which equals
d E_1||V^(1)||^2. The same calculation for layer three adds
||V^(3)||_HS^2. This proves both identities in (6), including their
normalization, and excludes simultaneous zero accelerations within
either upper layer.

The symmetry step is valid for opposite labels as well. Put
tau=y_1 y_2 and let pi exchange the samples. The initial root reflection
Q exchanges x_1,x_2 and preserves the Gaussian initialization. On the
canonical symmetric population actions, it sends H_0 to tau H_0 and
beta^(ell)_a to tau beta^(ell)_(pi a). Since p_(pi a)=tau p_a,
the two signs cancel in the hidden V tensors; the first field transforms
by Q. Substitution into the forward acceleration equations therefore
sends U^(ell)_a to U^(ell)_(pi a), with no remaining sign. The invariant
population law gives equal squared L2 norms for the two accelerations.
Together with (6), both norms are positive in each upper layer.

Finally phi'>=1 implies

    ||phi'(Z^(ell)_{a,0}) U^(ell)_a||_2
       >= ||U^(ell)_a||_2 > 0.

The strong path chain rule gives the corresponding feature expansion
with coefficient (s^2/2) phi'(Z^(ell)_{a,0})U^(ell)_a. Equivalently,
the first feature derivative divided by s converges to this acceleration.
Thus all six sample/layer feature accelerations are nonzero in L2.
This does not assert pointwise nonzero acceleration at every neuron.

## 5. Kernel coefficients and the clock

The bounded linearizations J_s are locally uniformly bounded and
J_s V->J_0 V strongly, by the same fixed-factor multiplier argument
and operator continuity. Therefore

    H'(s)/s = J_s[theta'(s)/s] -> J_0 V,
    H(s)=H_0+(s^2/2)J_0 V+o_L2(s^2).

Since E_3[H_0 J_0 V]=||J_0^*H_0||_hidden^2=||V||_hidden^2,

    kappa_4(s)=kappa_0+s^2||V||_hidden^2+o(s^2).

The individual projected hidden blocks have coefficients

    kappa_1(s)=s^2 d E_1||V^(1)||^2+o(s^2),
    kappa_2(s)=s^2 ||V^(2)||_HS^2+o(s^2),
    kappa_3(s)=s^2 ||V^(3)||_HS^2+o(s^2).

Their sum contributes one further s^2||V||_hidden^2, proving the factor
2 in the total-kernel expansion (7). Here kappa_ell=p^T K^(ell)p
and kappa_0=||H_0||_2^2>0; the latter follows from the positive definite
top feature Gram. All projected hidden coefficients are strictly
positive. Both the output projection and the total kernel therefore
differ strictly from their initial values for all sufficiently small
positive feature times.

On the constructed symmetric path, ds/dt=2(1-g) and g(0)=0 give
s(t)=2t+o(t). In particular, the corresponding quadratic coefficients
in physical time are 4||V||_hidden^2 for kappa_4 and
8||V||_hidden^2 for kappa. The clock factor in the candidate is correct.

## SHA-256 provenance

Hashes identify the files read for this review:

```text
bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351  /tmp/l3-two-sample-Un7kw9/INITIAL_FEATURE_LEARNING.md
e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd  /tmp/l3-two-sample-Un7kw9/CONTRACT.md
a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f  /tmp/l3-two-sample-Un7kw9/TWO_SAMPLE_SOURCE_BASELINE.md
40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4  /tmp/l3-two-sample-Un7kw9/SYMMETRY_RADIAL_CLOCK.md
f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4  /tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md
9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7  /etc/codex/skills/solve-math-rigorously/SKILL.md
```
