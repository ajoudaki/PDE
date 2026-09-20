# Fixed-depth kernel strictness and loss descent

2026-09-20, supervisor derivation. This supplements the contract's required
activity statement with the other strict finite-data conclusions of maintained
C.3. Inputs are the frozen CH3_ACTIVITY_PROOF.md and CH3_LOCAL_PROOF.md, with
the same finite-data assumptions, model and unhalved weighted loss. It is
local and implies no substantial-training loss threshold.

Use the activity proof's notation: p_a=omega_a y_a, G_ab=u_a.u_b,
H_(ell,a), B_(ell,a), Q_ell=E[H_ell H_ell^T],
D_ell=E[B_ell B_ell^T], activation gate d_(ell,a), preactivation
coefficient R_(ell,a) and activation coefficient E_(ell,a)=d_(ell,a)R_(ell,a).
All Q_ell and D_ell are positive definite by that proof. Put

    J_1=G circ D_1,
    J_ell=Q_(ell-1) circ D_ell, 2<=ell<=L,
    E_star=sum_(ell=1)^L p^T J_ell p.

Here circ means entrywise multiplication, and E_star is a deterministic
positive number, not a population expectation. To check positivity even
if G is singular, decompose any positive semidefinite Q=sum_j v_j v_j^T.
For positive definite D,

    Q circ D=sum_j diag(v_j)D diag(v_j)
         >=lambda_min(D) diag(Q_11,...,Q_mm).

All diagonal entries here are positive: G_aa=1 and every Q_ell,aa>0.
Thus each J_ell is positive definite and E_star>0 because p!=0.

The actual kernel blocks from local proof (29), with unit mobilities, obey

    K^ell(t)=4t^2 J_ell+o(t^2), ell=1,...,L,
    K^(L+1)(0)=Q_L>0.

This follows by substituting Delta_ell(t)=2t B_ell+o_L2(t) and
H_ell(t)=H_ell+o_L2(1), then applying Cauchy--Schwarz to each contraction.
There are finitely many entries, so these are matrix-norm expansions.
Consequently all L+1 blocks are positive definite for sufficiently small
positive t; the L hidden blocks start at zero and are nonconstant.

To verify nonconstancy of the readout block, set S=sum_a p_a H_(L,a).
Adjunction of each actual initialized edge and the recursion for R give

    sum_a p_a E_L[B_(L,a) R_(L,a)]=E_star.                 (1)

Here is the full telescoping step. At edge ell>=2 the learned-matrix
term M_(ell,a)=sum_b p_b Q_(ell-1),ab B_(ell,b) contributes

    sum_a p_a <B_(ell,a),M_(ell,a)>
          =p^T (Q_(ell-1) circ D_ell)p.

The propagated term gives

    sum_a p_a <B_(ell,a),A_ell E_(ell-1,a)>
      =sum_a p_a <A_ell^*B_(ell,a),d_(ell-1,a)R_(ell-1,a)>
      =sum_a p_a <B_(ell-1,a),R_(ell-1,a)>.

Repeat to layer one. There R_(1,a)=sum_b G_ab p_b B_(1,b), yielding
p^T(G circ D_1)p. This proves (1) with no sign cancellation assumption.

The activation expansion gives

    sum_a p_a H_L(t,u_a)=S+2t^2 sum_a p_a E_(L,a)+o_L2(t^2).

Since B_(L,a)=d_(L,a)S, its squared norm and (1) give

    p^T K^(L+1)(t)p=||S||2^2+4E_star t^2+o(t^2),
    p^T K(t)p=||S||2^2+8E_star t^2+o(t^2).

Thus the readout block and total kernel are nonconstant as well. The kernel
direction is p, not the unweighted label vector y.

Each learned hidden matrix moves on every initial preceding feature:

    K_ell(t) H_(ell-1,a)
        =2t^2 sum_b p_b Q_(ell-1),ba B_(ell,b)+o_L2(t^2).

The coefficient vector against the positive-definite B_ell Gram has a-th
entry p_a Q_(ell-1),aa!=0, so this displacement coefficient is nonzero.

Finally, the exact weighted energy/kernel identity gives

    -loss'(0)=4p^T Q_L p=4||S||2^2>0.

Continuity of the actual residual and kernel therefore gives, on a smaller
positive interval, -loss'(t)>=2||S||2^2. Intersect this interval with the
activity and nonaffinity intervals. These statements retain every strict
finite-data conclusion listed by maintained C.3, now at each fixed depth.
They do not assert individual residual magnitudes decrease or uniform margins
as data become parallel, weights/labels vanish, or depth tends to infinity.
