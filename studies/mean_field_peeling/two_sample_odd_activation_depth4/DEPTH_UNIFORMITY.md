# Depth audit for the convex odd activation

Independent bounded audit, 2026-09-07. No experiments, repository edits, or commits.

## Scope and conclusion

Let `L` mean the number of hidden layers, with the obvious extension of the raw model in `studies/mean_field_peeling/two_sample_odd_activation_theorem/PROOF.md`: independent Gaussian matrices between consecutive layers, the same raw metric factors, initialized readout entries `N(0,n^-2)`, and simultaneous raw GD of step `n^-2`.

There is a rigorous obstruction to retaining a positive **depth-uniform numerical coercivity, initial loss rate, or activation-regression margin** for a fixed nontrivial convex mixture. There is no such obstruction to the different assertion that **one fixed positive mixing coefficient works qualitatively for each fixed finite depth, with all estimates allowed to depend on depth**. This audit does not prove or disprove that latter assertion, and in particular does not establish the proposed single prefactor and exponent `theta = c delta^10` for all finite `L`.

The generic conditioning and deterministic bridges extend to any fixed finite depth once their bounded-path and uniform-source-tail hypotheses have been supplied. Initial-motion nondegeneracy also extends, including the extra middle covariance at `L=4`. The unresolved depth-uniform choice lies in constructing the complete nonlinear source flow and maintaining nonaffinity with one common amplitude bound. The L3 positive supersolution has four coefficient families and one interior local response pair; this is not itself an arbitrary-depth theorem.

## 1. Exact initialization recursion and its consequences

Fix `0 < theta < 1`, put `a=1-theta`, and let

    phi(z) = z - theta (z-arctan z).

Set `q_0=1`, `c_0=rho`, and recursively let `(U,V)` be centered Gaussian with variances `q_l` and covariance `c_l`, and set

    q_{l+1} = E phi(U)^2,
    c_{l+1} = E phi(U) phi(V).

Thus `q_l` is the common initialized feature variance after hidden layer `l`; the preactivation variance at layer `l` is `q_{l-1}`. This is the Gaussian forward recursion obtained at each fixed finite depth and then the width limit. Its scalar recursion can subsequently be studied as `l` increases; this does not assert a simultaneous width-depth limit.

### Proposition 1: positivity at every finite layer

Since `a <= phi'(z) <= 1` and phi is odd, for either sign,

    a |u +/- v| <= |phi(u) +/- phi(v)| <= |u +/- v|.

Consequently,

    a^2 (q_l +/- c_l) <= q_{l+1} +/- c_{l+1}
                            <= q_l +/- c_l,

and

    q_l +/- c_l >= a^(2l) (1 +/- rho) > 0.

This already proves strict positive definiteness for each finite layer under `|rho|<1`. Strict monotonicity and the positive density of the Gaussian pair give a second proof: an identity `u_1 phi(s)+u_2 phi(t)=0` everywhere forces both coefficients to vanish by separate differentiation.

### Proposition 2: forward energy decays polynomially, not exponentially

For every `q>0`, `0<F(q):=E phi(sqrt(q)G)^2<q`, by strict contraction away from zero. Continuity of `F` implies that the decreasing positive recursion `q_{l+1}=F(q_l)` has limit zero; a positive limit would satisfy `F(q)=q`.

Write `D(z)=z-arctan z`. The integral identity

    D(z) = integral_0^z t^2/(1+t^2) dt

implies `|D(z)|<=|z|^3/3` and `|D(z)-z^3/3|<=|z|^5/5`. For `Z=sqrt(q)G`,

    E[Z D(Z)] = q^2 + O(q^3),
    E[D(Z)^2] = O(q^3).

Indeed the two error bounds can be taken as `3q^3` and `5q^3/3`, respectively. Therefore, for each fixed positive theta,

    F(q) = q - 2 theta q^2 + O_theta(q^3).

It follows that `q_{l+1}/q_l -> 1` and

    1/q_{l+1} - 1/q_l
       = (q_l-q_{l+1})/(q_l q_{l+1}) -> 2 theta.

Cesaro averaging yields the exact asymptotic

    lim_{l->infinity} l q_l = 1/(2 theta).

### Proposition 3: the normalized angle does not approach a singular endpoint

Put `r_l=c_l/q_l`. Expand the square-integrable odd function `G -> phi(sqrt(q)G)` in the orthonormal Gaussian Hermite basis. Only odd degrees occur. If its coefficients are `b_m(q)`, the Gaussian generating-function identity gives

    E[H_m(G_1)H_n(G_2)] = 1_{m=n} r^m

for the orthonormal basis and correlation `r`; this identity follows by comparing coefficients in `E exp(tG_1-t^2/2) exp(sG_2-s^2/2)=exp(rst)`. L2 approximation by partial sums passes the identity to phi. Hence

    r_{l+1} = sum_{m odd} w_m(q_l) r_l^m,
    w_m(q) = b_m(q)^2/F(q) >= 0,
    sum_m w_m(q)=1.

Thus the sign is preserved and `|r_{l+1}|<=|r_l|<=|rho|`. In particular

    q_l +/- c_l >= (1-|rho|) q_l >= delta q_l.

For `p_i=y_i/2`, `tau=y_1y_2`, and `H_0=sum_i p_i h_i^L`, the initial projected total kernel is only the readout kernel because the population readout is zero. Therefore

    kappa_L(0) = ||H_0||^2 = (q_L+tau c_L)/2,
    delta q_L/2 <= kappa_L(0) <= q_L.

For each fixed theta and delta this is of order `1/L`. The crude affine lower bound `a^(2L) delta/2` remains valid but seriously understates the actual large-depth signal.

### What this refutes and what it does not

The population loss is `(1-g)^2` under the two-sample symmetry. At initialization `g=0`, `g_dot=2 kappa_L(0)`, and therefore

    loss_dot(0) = -4 kappa_L(0) -> 0.

If an asserted depth-uniform bound were `loss_L(t)<=exp(-gamma_delta t)` for all `t>=0` with `gamma_delta>0`, right differentiation at zero would require `gamma_delta<=4 kappa_L(0)` for every L, a contradiction. In particular the literal L3 numerical bound `exp(-delta t/32)` cannot hold unchanged at all depths for a fixed nonzero theta. Also `||C_dot(0)||=2 sqrt(kappa_L(0))->0`.

The initialized activation-regression error at layer L also vanishes with L. For `Z~N(0,q)`, the admissible affine competitor `z` gives

    inf_{alpha,beta} E[phi(Z)-alpha-beta Z]^2
       <= theta^2 E D(Z)^2 <= (5/3) theta^2 q^3.

A sharper expansion is `(2/3)theta^2 q^3+O_theta(q^4)`: after removing the linear projection, the leading residual is `-(theta/3)(Z^3-3qZ)`, whose variance is `(2/3)theta^2q^3`. The remainder has L2 norm `O_theta(q^(5/2))`, and orthogonal projection is contractive. Substituting `q=q_{L-1}` gives asymptotic `1/(12 theta L^3)`. It remains strictly positive at every finite layer, since a nondegenerate Gaussian has full support and phi is nonaffine.

All these facts are compatible with qualitative convergence, strict finite-layer nonaffinity, and nonzero initial motions at every fixed finite L. They do **not** furnish a counterexample to the fixed-activation / fixed-finite-depth interpretation.

## 2. Arbitrary finite depth: the initial middle covariance and motion

The finite Gaussian-conditioning proof already states its hypothesis for finitely many independent Gaussian matrices, each reusable in both orientations (`two_sample_odd_activation_theorem/sources/L3_LOCAL_COMPLETE_PROOF.md`, section “Finite Gaussian conditioning, with two matrices”). Its response derivation explicitly retains derivative paths through other matrices. Singular-query regularization is finite-transcript and does not require a depth-independent probability bound.

Let `D_i^l=phi'(Z_i^l)` and define

    beta_i^L = H_0 D_i^L,
    beta_i^l = D_i^l A_{l+1,0}^* beta_i^{l+1}.

Write `S_l=E[beta^l(beta^l)^T]`. At the top, `S_L` is positive definite. A zero quadratic form would give the everywhere identity

    (p_1 phi(z_1)+p_2 phi(z_2))
    (u_1 phi'(z_1)+u_2 phi'(z_2)) = 0.

For fixed `z_2`, the first factor has at most one zero as a function of `z_1`. Continuity forces the second factor to vanish everywhere. Differentiation in `z_1` and nonconstant `phi'` force `u_1=0`, and then positivity of `phi'` forces `u_2=0`.

For each downward reused matrix call, the complete initialization transpose formula is

    A_{l+1,0}^* beta_i^{l+1}
       = G_i^l + sum_j h_j^l T^l_{ij},
    T^l_{ij} = E partial_{xi_j^{l+1}} beta_i^{l+1},
    Cov(G^l) = S_{l+1}.

The Gaussian pair `G^l` is independent of the local initialized forward pair. In the derivative, deterministic response coefficients and source covariances are frozen, and the complete explicit dependence on the forward source is differentiated. In particular the derivative of the actual middle response through `h^{l+1}` is present. The covariance is the **full second moment** `S_{l+1}`, not a covariance left after regression on forward features. These are consequences of the stated finite-program source rule; one can first truncate unbounded coordinate products and remove the truncation at this fixed transcript using Gaussian moments and bounded derivatives.

Conditioning on the local forward pair gives

    Cov(beta^l | Z^l)
       = diag(D^l) S_{l+1} diag(D^l)
       >= a^2 lambda_min(S_{l+1}) I.

Hence `S_l` is positive definite, and induction covers every extra interior population, including both middle populations at L4. There is no novel rank obstruction at L4 initialization.

Define the hidden feature-time acceleration blocks by

    V^1 = (1/d) sum_i p_i beta_i^1 x_i,
    V^l = sum_i p_i beta_i^l tensor h_i^{l-1},  l>=2.

Every block is nonzero: if `F_{l-1}` is the preceding feature Gram, then

    ||V^l||_HS^2 = tr(S_l diag(p) F_{l-1} diag(p)) > 0.

For `l=1` the same formula uses the input Gram `Gamma` and equals `d E||V^1||^2`; `Gamma` is positive definite. This argument also covers L1 without requiring a lower reverse source.

Let `U_i^l` be the corresponding preactivation acceleration. At the first layer it is the nontrivial combination `sum_j Gamma_ij p_j beta_j^1`, whose L2 norm is positive because `S_1` is positive definite. The forward product rule and actual adjoints give, for each l,

    sum_i p_i <beta_i^l,U_i^l>
       = sum_{j=1}^l ||V^j||_raw^2 > 0.

At least one sample moves at every layer; input-exchange symmetry gives the two samples equal squared norms, so both move. Since `D_i^l>=a>0`, the feature acceleration is nonzero as well. On any constructed regular feature flow, the same expansion as at L3 gives `kappa(s)=kappa(0)+2s^2||V||^2+o(s^2)`, and the physical clock gives acceleration factor 4 and kernel coefficient `8||V||^2 t^2`.

These motion statements require a constructed regular trajectory to interpret the formal initial derivatives as trajectory derivatives. Their nondegeneracy certificate itself is a fixed finite initialization transcript and does not impose an additional theta-versus-depth smallness restriction.

## 3. Which source and limit mechanisms extend

### Generic conditioning, cap removal, and physical/GD/velocity bridges

At any fixed L, fixed cap, and fixed auxiliary mesh, there are only finitely many queries. The existing generic conditioning proof applies to all `L-1` independent square matrices. The operator-norm event uses a finite union bound. No claim concerning `L=L(n)` follows.

On a bounded primal ball, forward differences have a finite-depth estimate

    sum_{l,i} ||Z_A^l-Z_B^l||_2 <= C_{L,b} ||Theta_A-Theta_B||_raw.

The asymmetric cap gate estimate is unchanged:

    ||D_{R'}(Z_A,q_A)-D_R(Z_B,q_B)||_2
       <= 2||q_A-q_B||_2 + 2eR||Z_A-Z_B||_2
          + 2e || |q_B| 1_{|q_B|>R} ||_2.

Backward substitution gives one factor `R`, not `R^L`: `R` multiplies a forward discrepancy at each gate, and backward discrepancies propagate through bounded actions and bounded `D_q`. Induction gives

    ||V_{R'}(Theta_A)-V_R(Theta_B)||_raw
       <= C_{L,b}(1+eR)||Theta_A-Theta_B||_raw
          + C_{L,b}e sum_Q || |Q_B|1_{|Q_B|>R} ||_2.

Thus, **if** all incoming fields along a bounded reference interval have cap/mesh-uniform Gaussian tails, Gronwall produces an error of the form `C exp(C_{L,b,S}(1+eR)-c_{L,b,S}R^2) -> 0`. The same deterministic estimate, retaining both residuals, gives uniqueness against bounded-primal nonsymmetric competitors and restart from reached states. Constants may depend on L. The scalar physical clock works for every L once the two-sample symmetry and an endpoint above 1 are known.

At fixed cap and finite physical T the raw Euler defect is `C_{L,R,T} eta_n`; hence `eta_n=n^-2` tends to zero for every fixed L. Retaining the original initialized finite readout uses exactly the same fixed-program stability argument. For velocities, recursively apply the forward product rule and truncate only the reference velocity factor in a gate difference. There remains a single truncation factor M multiplying the raw-state discrepancy, with constants depending on L. Compactness of the continuous uncut L2 velocity image gives uniform tails. The ordered limits (width at fixed cap/truncation; cap removal at fixed velocity truncation; final truncation removal) are unchanged, with a finite sum over layers. Consequently these are conditional bridges, not the source of a new all-depth amplitude obstruction.

### The generic finite-L source closure has the same chronology

For arbitrary fixed L the exact local source equations have the pattern

    Z^1 = Z_0^1 + K_1 delta^1,
    Z^l = xi^l + A_l delta^l,                 2<=l<=L,
    q^l = zeta^l + B_{l+1} h^l,              1<=l<L,
    q^L = C,  C_k=sum_{r<k} h_r c_r^T h_r^L.

Each `A_l` is strict causal; each `B_l` is causal including the diagonal. The coefficient formulas are the same expected formal source derivatives plus learned second moments as in L3. On a bounded coefficient prefix, every interior population is the same local system `Z=xi+A delta`, `q=zeta+B h`. Its Volterra moment and derivative-envelope proof uses bounds for A,B and the source variance, not the absence of another interior population.

At row k the construction order becomes

    A_2,k, A_3,k, ..., A_L,k, B_L,k, ..., B_3,k, B_2,k.

A forward coefficient uses the preceding newly bounded forward row and previously constructed reverse rows. The reverse sweep uses the next reverse row, already bounded in the sweep. Current returns satisfy the exact recursion

    (B_L,kk)_ij = 1_{i=j} E L_i^L,
    (B_l,kk)_ij = 1_{i=j} E L_i^l
                  + (B_{l+1,kk})_ij E[V_i^l G_j^l],  l<L,

where `L_i^l=e g'(Z_i^l) tau_R(q_i^l)`, `V_i^l=a+e g(Z_i^l)tau_R'(q_i^l)`, and `G_i^l=a+e g(Z_i^l)`. No current diagonal may be omitted. They are `O_L(e)` on a bounded moment prefix.

The general controlled-response construction therefore admits the same finite-L perturbative proof with a constant `K_L(P,S)`, provided the actual controlled affine Euler programs have a bounded primal ball with strict slack. The formal induction closes an error of the form

    E_k <= K_L e + K_L sum_{r<k} h_r E_r,

and a sufficient amplitude bound has the form

    e <= [2 K_L exp(K_L S)]^-1,

along with the finite-L primal comparison bound. This statement is an extension of the displayed proof mechanism, not a quantitative claim that `K_L` is bounded uniformly in L. Establishing the affine premise and the nonaffinity transfer then supplies a possible depth-dependent admissible threshold. No lower bound on its infimum over L has been established here.

## 4. Why the power-ten certificate cannot simply be reused

The current L3 power-ten proof takes `lambda=a^3 sqrt(v)` and `M=(3/(sqrt(2)lambda))^(1/4)`. Its explicit source certificate, positive supersolution, row-density bounds, and exponent arithmetic are tied to exactly four coefficient families `(A_2,A_3,B_3,B_2)`. The two key strict-factor sandwich identities account for one middle local resolvent. At L4 there are six coefficient families and two interior resolvents; at general L there are `2(L-1)` coefficient families. The Gaussian source covariances stay well-defined, but the quantitative coefficient majorant and nonlinear defect bound need a new induction.

The actual initialization already warns against treating the old affine comparator as uniformly close in depth. For the affine gain `a=1-theta`, the feature variance is `a^(2L)`, whereas the convex activation has `q_L~1/(2theta L)`. Hence

    q_L/a^(2L) -> infinity.

An identity-gain affine comparator instead has variance 1 at every depth, and its top feature differs in L2 norm from the nonlinear top feature by at least `1-sqrt(q_L) -> 1` under every coupling. Thus neither elementary comparator gives a uniformly small initialization tube through all depths. These are limitations of these perturbative comparisons. They are not proofs that the trained nonlinear theorem fails at some finite depth.

To settle the common-coefficient claim positively, a new argument must bound the arbitrary-depth source program and provide a nonaffinity certificate for every finite L under one common positive theta. It could use constants depending on L; what must remain common is the admissible theta itself. To settle it negatively, one needs a finite-depth failure for that theta (or another obstruction to one of the actual qualitative conclusions). Vanishing quantities as L tends to infinity are insufficient.
