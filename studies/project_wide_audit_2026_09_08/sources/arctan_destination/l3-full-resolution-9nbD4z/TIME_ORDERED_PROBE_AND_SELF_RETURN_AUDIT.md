# Adaptive rare-block audit and the Gaussian time-ordered tangent expansion

## Independent audit

ADAPTIVE_RARE_SELF_BLOCK_MODULUS.md passes. The submatrix-net union bound and its constants, adaptive signed-diagonal domination, layer-cake/Jensen step, frozen-row replacement, the estimate h(min(1,4d))<=4 omega(d), and the stated C_M are valid. The lemma applies simultaneously to adaptive gates and sets. Its scope correctly excludes rare-to-bulk transport and control of the full/pruned state discrepancy.

## 1. The exact retarded tangent kernel

Use the actual full-network tangent equation (2) of ACTUAL_BULK_GAUSSIAN_TANGENT_ENERGY.md:

    y'=L_s y+R_s M_(b_s) T_s y+f_s,
    b_s=phi''(z2(s)) q2(s),      y(0)=0.

Let U(s,t) be the propagator of the bounded coefficient L_s, and put v(s)=T_s y(s). At every finite width,

    v(s)=v0(s)+integral_0^s K(s,t) M_(b_t) v(t) dt,
    v0(s)=T_s integral_0^s U(s,t) f_t dt,
    K(s,t)=T_s U(s,t) R_t.                              (1)

All coefficients are evaluated on the actual trained path. On primal-bounded paths, ||K(s,t)||op<=C_S, and the independent-probe forcing gives E_xi||v0(s)||2^2<=C_S/n. These statements use no q tail.

Crucially, the current-time return is exactly

    K(s,s)=T_s R_s
          =m1(s)I+W2(s)D1(s)^2 W2(s)*=A2(s).          (2)

Thus the new rare self-block lemma controls a genuine part of this kernel. The time-ordered expansion, however, uses K(s,t) at different times and between different supports; (2) alone does not control those transports.

Iterating (1) gives the exact kth term

    v_k(s)= integral_(0<t_k<...<t_1<s)
       K(s,t_1) M_(b_t1) K(t_1,t_2) M_(b_t2) ...
       K(t_(k-1),t_k) M_(b_tk) v0(t_k) dt.              (3)

For fixed n the bounded finite-dimensional coefficients justify this expansion. No width-uniform estimate of its terms is asserted.

## 2. What the proposed Wick-sized bound would and would not imply

A bound sqrt(n)||v_k||L2 <= C_S (C_S sqrt(k))^k/k! would indeed sum on every finite horizon. It would establish a mean-square tangent bound with no finite-time radius restriction.

Its usual Lr Gaussian extension, however, is

    sqrt(n)||v_k||Lr <= C_S (C_S sqrt(r k))^k/k!,

whose sum has an exp(C_S r) bound. That does NOT give the sqrt(r)log r response moments required by the earlier Osgood reduction. This distinction is real: for a scalar Gaussian Z, the Dyson terms of exp(sigma Z) have precisely this moment scaling, while

    ||exp(sigma Z)||Lr = exp(sigma^2 r/2).

This scalar example is only a logical check on the proposed summation, not a model for the network. Successful L2 Wick counting could still support a different coupling argument, but it needs a separate bridge to global population continuation.

## 3. Adaptation enters at the first nontrivial Wick contraction

For independent standard Gaussian disorder coordinates G_a,G_b and a smooth functional F for which the displayed Gaussian integration-by-parts operations are justified (or with compactly supported cutoffs and their boundary terms retained),

    E[G_a G_b F]=1_(a=b) E[F]+E[partial_a partial_b F].  (4)

In (3), after expressing q2=W3_0*delta3 plus its bounded learned history, F contains the actual delta3, K, and v0. The second term of (4) therefore differentiates the full causal flow. It is not zero. For example differentiating a middle gate gives phi'''(z2) partial_a z2, and differentiating a probe covariance gives the mixed second responses displayed in equations (10)--(11) of the tangent-energy note.

Causality represents those mixed derivatives by further integrals. It does not bound their amplitudes: the mixed variation equation contains

    phi'''(z2) q2 zeta2^a zeta2^b
       +phi''(z2)[q_dot2^a zeta2^b+q_dot2^b zeta2^a].

Consequently the ordinary Wick pair count is not an estimate of (3) unless these derivative contractions are also controlled. Bounded activations bound their explicit scalar derivative factors, but not the causal variations multiplying those factors.

## 4. Canonical initial self-return: localized covariance but favorable mean sign

There is a concrete feature of the actual Gaussian initialization that a resummation should retain. All objects in this section are at s=0. Set

    d0=D3 H3,        E3=D3^2+H3 phi''(z3),
    A0=m1 I+W2 D1^2 W2*,
    B0=m1 I+W2 W2*,
    h=H2.

For the independent probe K=xi e_i^T/sqrt(n), the exact derivative jets are

    c'(0)=D3 K h,
    delta_dot'(0)=D2 r,
    r=e_i (xi dot d0/sqrt(n))
         +h_i W3* E3 xi/sqrt(n),

    zeta2''(0)=A0 D2 r,
    gamma2''(0)=B0 D2 r.                               (5)

At coordinate i, the second term in each resulting Gaussian linear form has Euclidean coefficient norm O(n^(-1/2)) on the initial operator-bound event. Therefore

    E_xi[gamma2_i''(0) zeta2_i''(0)]
      =(B0)_ii(A0)_ii D2_i^2 ||d0||2^2+O(n^(-1/2)).    (6)

Here ||d0||2 is normalized. Thus Gamma_(i,i)(s) has an order-n coefficient in its s^4 term. Independent probe averaging does not automatically spatially spread this covariance.

This jet does not refute a finite-time bound ||Gamma_i||2<=C Lambda_i: c'(0) is nonzero, so Lambda_i starts at order s^2. In fact

    Lambda_i(s)=s^2 h_i^2 ||D3||2^2+o_n(s^2).

No width-uniform remainder estimate allowing a contradictory time choice has been proved.

The principal self-site curvature nevertheless has a favorable EXACT Gaussian conditional sign. Given the entire lower initialization and z3=W3_0 h, Gaussian row conditioning gives

    E[q_i'(0) | lower initialization,z3]
       =(h_i/m2) <z3,D3 H3>,       m2=||h||2^2.        (7)

Both <z3,D3 H3> and ||d0||2^2 are nonnegative. Since

    phi''(z2_i) h_i <=0,

the principal i-site coefficient in the expectation of
<phi''(z2)q2,Gamma_i> is nonpositive after this conditioning. Multiplying by the leading coefficient of Lambda_i^(r-1) preserves the sign, since that coefficient is a nonnegative function of the same conditioned fields. This verifies a leading self-return dissipation in the exact canonical flow. It makes no claim about the off-site contributions, finite positive times, or the entire moment inequality.

## 5. The specific resummation still needed

For a scalar site equation

    z_i'=a_i q_i phi'(z_i)+c_i,

the homogeneous diagonal tangent factor has the exact expression

    exp(integral_t^s a_i phi''(z_i)q_i du)
      = [phi'(z_i(s))/phi'(z_i(t))]
        exp(-integral_t^s [phi''/phi'](z_i)c_i du).      (8)

For arctangent, |phi''/phi'|<=1. With no bulk forcing and zero initial tangent, variation only of q gives the stronger cancellation

    zeta_i(s)=phi'(z_i(s)) integral_0^s a_i(u) q_dot_i(u) du.

In the network, c_i is the rare-to-bulk contribution of the actual mobility, and its variation is part of the actual causal tangent. The new self-block modulus controls the diagonal/rare principal part in (8), but supplies neither c_i nor the two-time transports in (1). Treating the pruned Gaussian bulk force as the actual one would reintroduce the unproved comparison.

The narrower next resolver is therefore a signed bound for the actual two-time rare-to-bulk return, after diagonal arctangent resummation, or directly for the mixed-response term in (4). The favorable initial sign (7) is evidence about the principal contact term only. No all-time Wick bound or Osgood moment estimate has been proved.
