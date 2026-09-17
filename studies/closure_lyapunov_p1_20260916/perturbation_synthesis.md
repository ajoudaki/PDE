# What perturbing the solved geometry reveals

2026-09-16. Current answer to the user's proposed method. This continues
the same Lyapunov investigation. It supplies exact new identities and a
concrete conditional template; it does not announce generic convergence.

## Answer and role of the restriction

The proposal helps in a mathematically concrete way. The old restriction
was used to make the three signed predictions equal throughout training,
through a permutation isometry of the exact initialized dictionary. The
signs of angles are not, by themselves, an identified necessity for
learning. No proof shows that this symmetry is necessary for fitting.

The old argument retained the first layer in the dynamics and in
||grad F||^2, but used its contribution only as a nonnegative term.
It did not exploit the first-layer interactions to control the two
prediction-disagreement directions. That is a real source of information
left unused by the scalar proof.

## 1. Exact missing modes, rather than guessed distance penalties

For m_i=y_i f_i, let F=mean(m_i), delta_i=m_i-F,
e=1-F and V=mean(delta_i^2). Exactly,

    L=e^2+V.

Let g_i=grad m_i, gbar=mean(g_i), z=mean(delta_i g_i),
K=||gbar||^2, B=<gbar,z>, Ddelta=||z||^2, q=E c^2. Then

    F_dot=2eK-2B,
    V_dot=4eB-4Ddelta,
    q_dot=4eF-4V.

The old normalized-readout argument acquires the exact defect

    (q/F^2)_dot=-(4/F^3)[e(qK-F^2)+FV-qB],  F>0.

The uncontrolled coupling is B. It represents how an update aimed at
the average signed prediction affects unequal signed predictions, and
conversely. At the symmetric reference B=V=0. For nearby actual input
vectors on a fixed finite horizon, delta=O(epsilon), V=O(epsilon^2),
B=O(epsilon^2). The latter uses equal row sums of the reference tangent
Gram. Changes of F,q,K themselves can still be first order. No all-time
perturbation bound follows from these estimates.

The exact complete tangent Gram is the sum of readout, middle and
first-layer terms. In canonical unsigned notation its entries are

    E2[H_i^2 H_j^2]
    +(a_i.a_j)(d_i.d_j)
    +(u_i.u_j) E1[sech^2(w.u_i)sech^2(w.u_j)q_i q_j].

Here H_i^2 denotes the second-layer field, not its square. Labels conjugate
this Gram for signed predictions. All three blocks are positive
semidefinite as matrices, although individual cross-input terms have
no fixed sign. This is the relevant interaction geometry.

Complete independent derivation: [perturbation_modes.md](perturbation_modes.md).
Root checked all equations, factors, finite-horizon qualifications, the
old potential's derivative, and the proposed inverse-transverse correction
including its matrix derivative. The provenance sentence about references
to other studies should read "unassigned same-study dependencies were not
followed"; no other study was used by the candidate or this route.

## 2. A definite template: instantaneous physical correction cost

[perturbation_metric_template.md](perturbation_metric_template.md) defines
the probability-normalized full tangent Gram K and normalized signed
residual r=(m-1)/sqrt(3). On K>0,

    E=r^T K^(-1)r

is the minimum squared physical size of a parameter correction that
would remove the current residual in the linearized prediction map.
This definition uses only the current state, not a future fitted endpoint.
In mean/disagreement coordinates (-e,zeta), write the current Gram as
[[k,b^T],[b,H]] and S=H-bb^T/k. Then exactly

    E=e^2/k+(zeta+e b/k)^T S^(-1)(zeta+e b/k).

Its perturbation expansion contains three inseparable quadratic pieces:
disagreement energy, a mean/disagreement cross term, and the positive
term completing their square. Both hidden layers determine their weights.
Thus the proposed perturbation method gives an explicit form for missing
terms without assuming all hidden distances should move monotonically.

The complete metric derivative is

    E_dot=-4L-r^T K^(-1)K_dot K^(-1)r.

The last term is essential. The sufficient condition
K_dot>=lambda K-4K^2 gives E_dot<=-lambda E. It has NOT been established
for the reached generic states. The independent post-freeze check is
[perturbation_metric_check.md](perturbation_metric_check.md).

A stronger conditional conclusion avoids a separate uniform upper bound
on K. Cauchy--Schwarz gives L_dot<=-4L^2/E where L>0. Hence, under
the preceding metric inequality, the explicit potential

    Phi_new=L+lambda E

satisfies

    L<=Phi_new,       Phi_new_dot<=-(lambda/2)Phi_new.

Indeed divide the desired inequality by lambda^2 E and set
x=L/(lambda E); it is 4x^2+1>=(x+1)/2. The difference equals
4(x-1/16)^2+31/64. At E=0 one has zero residual and zero velocities.
This is a PROVED conditional implication, not verification of the metric
inequality. The matrix inequality is a stronger sufficient condition
than necessary; the same proof needs only its quadratic form in
K^(-1)r along the actual residual. No claim of a necessary universal
matrix condition is made.

The independent mode route instead keeps the old potential and adds a
current inverse-transverse-Gram term. Its complete evolution produces a
specific 2-by-2 matrix test. Neither candidate is yet proved to decrease
on every generic initialized trajectory, and the new cost does not
automatically inherit the old scalar theorem even on the reference.

## 3. A new first-layer balance and explicit angular defects

[perturbation_lower_balance.md](perturbation_lower_balance.md) proves
that for orthogonal unit inputs the full closure preserves

    ||M||F^2 - E1 sum_i sinh^2(w.u_i).

This is a relation between both hidden layers, for arbitrary labels.
It is a conserved, generally indefinite quantity, not itself a loss
controlling Lyapunov function. For arbitrary unit inputs its derivative
is exactly

    (2/m) sum_(i!=j) r_j(u_i.u_j)
             E1[sinh(2w.u_i)sech^2(w.u_j)q_j].

Here r_j=f_j-y_j is the canonical unsigned residual. Thus perturbing
orthogonality exposes concrete mixed forward/backward statistics.
A pointwise lower-only primitive cannot cancel these drives universally
for nonorthogonal inputs: the required vector field
G^(-1)sinh(2z) has nonsymmetric mixed derivatives. This narrow obstruction
leaves coupled M/backward/state-metric corrections fully open.

The fresh complete [balance audit](perturbation_lower_balance_audit.md)
passed all numbered formulas, with three explicit scope clarifications:
fixed dictionary, actual input vectors approaching the reference, and
m=d for the full coordinate metric. Root applied exactly those
clarifications; no numbered formula changed. Both audited and current
source hashes are retained by the report/current note and manifest.

## 4. A more precise orthogonal-reference bottleneck

The independently frozen [perturbation_orthogonal.md](perturbation_orthogonal.md)
uses coordinate permutation blocks of the actual w and M to show that
the two equal transverse tangent eigenvalues are

    1/2 ||H_1^2-H_2^2||_2^2
      +1/2 ||d_1 a_1^T-d_2 a_2^T||F^2
      +E1[sech^4(w_1)q_1^2].

Upper-feature coincidence alone therefore need not destroy conditioning:
the first-layer term can retain both missing directions. The actual
middle matrix's transverse component remains nonzero at every finite
auxiliary time. Nevertheless its contraction with the lower features
could be zero; full tangent degeneracy is exactly a simultaneous zero
of that contraction and a specified common upper backward correlation.
The report does not exclude that event at the fitting endpoint.

Root checked the entire derivation: permutation blocks, factors 1/3,
the integral divided difference, finite-time nonvanishing matrix component,
weighted lower Gram positivity, and its explicit ambient fitting example.
Two wording qualifications: "full row rank" refers to the active
3-by-6 middle block (the full 4-by-7 matrix has inactive constants),
and "bounded state" means bounded w-g,c,M, with frozen Gaussian g.
The ambient example is not asserted reachable. This is an author-side
complete check, not a fresh isolated review of this second route.

## Current research conclusion

The user's method has produced a definite template and genuinely new
first-layer information. What remains is a reachable-state estimate
controlling disagreement correction and its changing geometry. A small
perturbation calculation identifies the terms but does not bound them
for infinite training time. The original generic circle theorem and an
unconditional perturbed-family theorem remain open. No adverse example
here proves failure of initialized fitting.

No experiments were run. The previous diagnostic remains closed. All
artifacts are in the existing flat study; the README is updated and no
shared scientific file or Git index was changed. Independent routes were
frozen before comparison; the inverse-full-metric check is explicitly a
later bounded check, not an independent discovery of that candidate.
