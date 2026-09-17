# Post-freeze check of the current-state metric template

2026-09-16. Bounded post-freeze algebra check by the mode-route author.
This is not an independent review: the template incorporates that author's
previous mode identities. No experiment was run and no original artifact
was edited.

Checked the complete `perturbation_metric_template.md`, SHA-256
`c852c95c0c3f9d26c9512e056ec2a9d1b05837b50d0b46c45b65bb7d85c729b7`.
The full tangent Gram was checked against my previously derived formula;
no additional lower-balance material was needed.

**Verdict:** the minimum-correction interpretation, normalization factors,
Schur square, cubic remainder on its stated domain, inverse-metric
derivative, sufficient conditions and linear loss comparison are correct.
There is one useful qualification to the wording about the upper bound,
given below. No generic decay theorem follows until the stated matrix
inequality is proved for the actual closure.

## 1. Normalizations and physical meaning

With J h=(<g_i,h>/sqrt(3))_i, its physical adjoint is
J*z=sum_i z_i g_i/sqrt(3). Consequently JJ*=G/3=K, including the
probability factor. The physical loss gradient is 2J*r, so
Xdot=-2J*r and rdot=-2Kr. Thus the residual dynamics and their factors
are consistent with the unhalved mean square loss and all three physical
gradient blocks.

When K>0, h0=-J*K^{-1}r satisfies Jh0=-r. Its physical squared norm
is r^TK^{-1}JJ*K^{-1}r=r^TK^{-1}r. Every competing solution differs
by an element of ker J, orthogonal to h0. This proves the stated minimum
among solutions of the linearized constraint. No claim of a finite
nonlinear parameter displacement, fitted endpoint distance or exact
linearization over a finite step is being made.

## 2. Schur square and perturbation scope

The orthogonal coordinates are exactly (-e,zeta), since
n^Tr=(sum_i m_i-3)/3=-e and V^Tr=V^Tdelta/sqrt(3)=zeta.
For the block matrix [[k,b^T],[b,H]], elimination gives

    y=(H-bb^T/k)^{-1}(zeta+e b/k).

The plus sign is therefore necessary. Substituting x=(-e-b^Ty)/k
in (-e,zeta).(x,y) gives exactly the template's square. Its three
quadratic terms all have the stated factors; in particular the cross
term is 2e b^Tzeta/(k nu). The compensation term e^2|b|^2/(k^2 nu)
must accompany that cross term.

For the remainder, fix T and a symmetric reference with nu>=nu_min>0.
The scalar k of that reference is >=C0>0 by the frozen theorem.
The O_T(epsilon) kernel comparison then supplies k>=C0/2 for
sufficiently small epsilon, and
S=nu I+O_T(epsilon)>=nu_min I/2 after reducing epsilon again.
The inverse resolvent identity gives
||S^{-1}-nu^{-1}I||=O_T(epsilon). Meanwhile
zeta+e b/k=O_T(epsilon), because e is bounded on the fixed interval.
Sandwiching the inverse error proves O_T(epsilon^3), without requiring
an epsilon derivative. Keeping current e and k, rather than reference
values, is essential to avoid dropping first-order mean changes.

The stated assumptions do not prove nu_min>0 on arbitrary long
intervals or at the reference endpoint. If nu degenerates, the inverse
expansion and its uniform remainder constant fail. Positivity at time
zero supplies a short interval by continuity, exactly as stated.

## 3. Metric derivative and sufficient inequalities

The two residual terms each contribute -2|r|^2, while the inverse
derivative contributes -r^TK^{-1}Kdot K^{-1}r. This gives

    Edot=-4L-r^TK^{-1}Kdot K^{-1}r

with no missing metric term. The full gradient differentiation in the
mode note includes both first-layer gate derivatives and the derivatives
of the actual backward action M^T. It is sufficient to evaluate Kdot
from the current characteristic state.

Congruence of Kdot>=lambda K-4K^2 with K^{-1} gives

    K^{-1}Kdot K^{-1}>=lambda K^{-1}-4I.

Insertion proves Edot<=-lambda E. Similarly,
Kdot>=-theta K^2 gives Edot<=-(4-theta)L; K>=kappa I implies
E<=L/kappa, hence the template's second exponential inequality for
theta<4. These are valid sufficient conditions. Neither is an estimate
already supplied by symmetry or initial rank.

For unit signed labels and inputs, the individual norm estimate is

    ||g_i||^2 <= 1 + ||c||_2^2 + ||M||op^2 ||c||_2^2.

The upper feature is bounded by one; the middle gradient uses
|a_i|<=1, |d_i|<=||c||2; the row gradient uses its gate bound and
||b1^TM^Td_i||2<=||M||op |d_i|. The last inequality uses the
contraction property of the normalized feature map. Since K=G/3,
tr K is the average of those three gradient norm squares, not their
unweighted sum. Thus the template's upper bound contains no missing
factor three. Diagonalization then correctly gives L<=Lambda E.

## 4. Qualification about the upper bound

The upper bound on K is material to the stated instantaneous comparison
L<=Lambda E. Without it, no uniform coefficient Lambda can be inferred
from the inverse metric alone: at a state with K=N I and L=1,
E=1/N. Thus growth of the metric can lower the proposed cost without
the same proportional change of physical residual.

However, the upper bound is not logically necessary to derive exponential
loss decay from the entire differential hypothesis (7) together with
the exact residual dynamics. This is an optional sharpening, not a
counterexample to any displayed sufficient statement in the template.
Indeed Cauchy--Schwarz gives

    L^2 <= (r^TKr)(r^TK^{-1}r) = (r^TKr) E,
    Ldot=-4r^TKr <= -4L^2/E.

If L(t0)>0, E0=E(t0)>0 and (7) holds subsequently, then
E(t)<=E0 exp(-lambda(t-t0)). While L>0, integration yields

    1/L(t) >= 1/L(t0)
                + 4[exp(lambda(t-t0))-1]/(lambda E0).

In particular

    L(t) <= max{L(t0), lambda E0/4} exp(-lambda(t-t0)).

If L reaches zero, the exact gradient vector field vanishes and the
bound persists. This argument yields a loss-decay estimate but does
not establish the same instantaneous comparison L<=Lambda E without
an upper spectral bound. The template's intended potential-plus-linear-
comparison claim therefore remains correctly conditional on that bound.
Recommended precision: say the upper bound is material *for (8)'s
instantaneous linear comparison*, rather than implying it is necessary
for every possible loss-decay argument.

## 5. Provenance correction to the frozen mode note

The provenance sentence in `perturbation_modes.md` saying the frozen
candidate's references were to "other studies" is inaccurate. The
candidate cites additional files in the same study. Those referenced
files were not opened during the independent mode subtask. Its actual
scientific inputs remained the supervisor-assigned documents and the
complete candidate. This correction changes no algebra or source scope;
the frozen mode artifact was left unchanged as requested.

## 6. Root-supplied extension after the frozen-file audit

After the findings above were sent to the root, the root supplied the
following additional candidate for a bounded algebra check. It is not
part of the frozen template audited in Sections 1--4, and is not an
independent proposal by this checker.

Assume along the current flow that K>0 and

    Kdot >= lambda K - 4K^2,    lambda>0.

Define the current-state potential

    Phi_new = L + lambda E.

Then the upper loss comparison is direct: L<=Phi_new. No uniform upper
bound on K is needed. The already checked identities give, when E>0,

    Phi_new_dot <= -4L^2/E - lambda^2 E.

Set x=L/(lambda E)>=0. The elementary inequality

    4x^2+1-(x+1)/2 = 4(x-1/16)^2+31/64 > 0

therefore proves

    Phi_new_dot <= -(lambda/2) Phi_new.

Thus the direction queried by the root is **less than or equal to**.
For every interval on which the matrix hypothesis holds,

    L(t) <= Phi_new(t)
         <= exp[-lambda(t-t0)/2] Phi_new(t0).

The zero-loss case requires no division: because K>0,
E=0 is equivalent to r=0 and L=0. The exact parameter gradient then
vanishes. The state, K and residual remain constant under the autonomous
flow, and Phi_new=0 has derivative zero, satisfying the claimed inequality.

This yields a stronger conditional potential theorem than the frozen
template's E-only construction: the loss term protects the comparison
against upward metric scaling. It does not remove the positive-definite
domain restriction, inverse-metric degeneration, or the unproved matrix
evolution inequality. It does not establish that inequality for the
actual generic initialized p=1 closure. All dependencies are still
current-state data and the fixed declared lambda, with no endpoint or
future trajectory.
