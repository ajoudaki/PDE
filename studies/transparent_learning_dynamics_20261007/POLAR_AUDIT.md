# Adversarial audit of the shear-embedded polar realization

Audit date: 2026-10-07. Scientific inputs were the supervisor's proposed formulas,
the supplied compressed runtime, and this author's `RELATIONAL_QUOTIENT.md`.
No other route's notes, external literature, or experiments were used. This is
a scoped independent derivation of the proposed construction within the study,
not a promotion review. The earlier mistake of interpreting the stipulated
coordinate gate as a metric-gradient gate is explicitly excluded here.

The supervisor subsequently reported that a deterministic identity-check script
now exists for the main construction. This auditor has neither inspected nor
independently run that script; the audit evidence here is the algebraic derivation.

**Verdict:** the proposed exact realization is algebraically valid when initialized
compatibly and evaluated with the masks and projections specified below. The
shear embedding removes the need for invertible original layer maps. The polar
rotation equation and metric equation have the stated signs. No missing
cross-frame overlap is needed. No new rank condition remains, beyond the original
corrected-readout inverse. The construction stores a full transported activation
algebra, so it is an exact geometric representation with polynomial overhead,
not a proof of additional state compression or elimination of map information.

## 1. The metric embedding and the actual masks

Let \(q_0=d\), let \(q_1,\ldots,q_L\) be the compressed widths, and put

\[
\mathcal H=\mathbb R^d\oplus\bigoplus_{\ell=1}^L\mathbb R^{q_\ell},
\qquad D=d+\sum_{\ell=1}^Lq_\ell,
\qquad
\mathcal M=\operatorname{diag}(I_d,M_1,\ldots,M_L).
\]

Write \(\iota_j\) for injection into block \(j\), \(\pi_j\) for block
extraction, and \(P_j=\iota_j\pi_j\) for the block projector. Adjoint stars
refer to \(\mathcal M\), or to the corresponding source and target metrics.

The original first map is \(B_1=A\), with source metric \(M_0=I_d\).
Define the lifted maps

\[
F_\ell=I+N_\ell,\qquad
N_\ell=\iota_\ell B_\ell\pi_{\ell-1}.
\]

Because distinct blocks have disjoint support,
\(\pi_{\ell-1}\iota_\ell=0\). Therefore

\[
N_\ell^2=0,\qquad F_\ell^{-1}=I-N_\ell.
\]

This holds for every rectangular \(B_\ell\), including zero maps and every
rank-deficient map. The inverse is not an additional assumption.

Flatten the metric once, with
\(Q=\mathcal M^{1/2}\), and denote flattened operators by
\(\widetilde F_\ell=QF_\ell Q^{-1}\). All subsequent orthogonality and
transpose operations are Euclidean. The coordinatewise activation algebra in
the flattened space has product and unit

\[
\mu(x,y)=Q\bigl[(Q^{-1}x)\odot(Q^{-1}y)\bigr],\qquad u=Q\mathbf1.
\]

Its block indicators are \(b_j=Q\iota_j\mathbf1\). Multiplication by
\(b_j\) equals \(P_j\), because the block-diagonal matrix \(Q\) commutes
with \(P_j\). Thus the indicators define mutually orthogonal block projectors
despite arbitrary nondiagonal metrics inside the blocks.

This detail is essential: after flattening and rotation, an indicator must act
through the transported multiplication product. Componentwise multiplication
by its numerical coordinates would generally implement the wrong mask.

## 2. The unrotated lift preserves the exact optimizer

For a declared input, initialize \(a_0=\iota_0v\). At each layer form
\(z_\ell=F_\ell a_{\ell-1}\), then apply \(\phi\) only in block
\(\ell\), leaving all other blocks unchanged. Induction gives

\[
a_\ell=(v,h^{(1)},\ldots,h^{(\ell)},0,\ldots,0),\qquad
\pi_\ell z_\ell=B_\ell h^{(\ell-1)}.
\]

Here \(h^{(0)}=v\). Before step \(\ell\), the target block is zero;
the shear adds exactly the desired preactivation. No assumption \(\phi(0)=0\)
is needed because unvisited blocks are not activated.

Start the backward pass from \(k_L=\iota_L\widehat w\). At step
\(\ell\), apply the original coordinate gate in block \(\ell\) and
the identity in all other blocks, obtaining \(g_\ell\); then set
\(k_{\ell-1}=F_\ell^*g_\ell\). The lower unvisited blocks of the backward
vector remain zero until reached. Induction consequently gives

\[
P_\ell g_\ell=\iota_\ell\delta^{(\ell)},\qquad
\pi_{\ell-1}k_{\ell-1}=B_\ell^*\delta^{(\ell)}.
\]

Previously visited upper blocks retain their backward signals, but cannot affect
the next lower block except through its prescribed adjacent map. In particular,
\(\delta^{(\ell)}=\phi'(z^{(\ell)})\odot B_{\ell+1}^*
\delta^{(\ell+1)}\) remains the stipulated coordinate-gated direction.
The mask is not replaced by its metric adjoint.

The permitted lifted update is precisely

\[
\dot F_\ell=\frac2m\sum_{a=1}^m c_a
 (P_\ell g_{a,\ell})(P_{\ell-1}a_{a,\ell-1})^*.
\]

It has only the \((\ell,\ell-1)\) block, equal to the supplied update of
\(B_\ell\). Its diagonal is zero, and all other blocks are zero. Therefore
the identity-plus-shear form is preserved. The readout remains in block \(L\)
and obeys \(\dot w=\frac2m\sum_a c_a h_a^{(L)}\).

Using unprojected retained forward or backward vectors in this update would
write many extra blocks, destroy the stipulated shear structure, and change
the optimizer. The two projections are necessary, not cosmetic.

## 3. Sequential polar frames and sufficient stored state

Fix a time-independent orthogonal \(O_0\). For each layer take the unique
positive polar factorization

\[
\widetilde F_\ell O_{\ell-1}=O_\ell S_\ell,\qquad
S_\ell\succ0,\qquad G_\ell=S_\ell^2.
\]

Explicitly,

\[
G_\ell=O_{\ell-1}^\top\widetilde F_\ell^\top
 \widetilde F_\ell O_{\ell-1},\qquad
O_\ell=\widetilde F_\ell O_{\ell-1}G_\ell^{-1/2}.
\]

The inverse exists because the lifted shear is invertible. This statement
requires no singular-value lower bound on the original rectangular map.

In frame \(\ell\), transport the multiplication product, unit, and all block
indicators:

\[
\mu_\ell(x,y)=O_\ell^\top\mu(O_\ell x,O_\ell y),\qquad
u_\ell=O_\ell^\top u,\qquad
b_j^{(\ell)}=O_\ell^\top b_j.
\]

Store all coefficients \(T_{\ell,ijk}\) of \(\mu_\ell\). Define
\(P_j^{(\ell)}x=\mu_\ell(b_j^{(\ell)},x)\). This equals
\(O_\ell^\top P_jO_\ell x\), so it is a Euclidean orthogonal projector.
The fixed frame-zero product and masks are also needed; they are initialization
data, not additional evolving variables.

The moving state is

\[
(G_\ell,T_\ell,u_\ell,(b_j^{(\ell)})_{j=0}^L)_{\ell=1}^L,
\qquad \rho=O_L^\top Q\iota_Lw,\qquad c.
\]

The initial values must be obtained from a common original initialization by
the sequential polar construction. Arbitrary independent tensors or masks need
not represent a valid lifted network. All compatibility constraints are preserved
by the rotation equations below.

## 4. A closed forward/backward evaluation with no frame overlaps

For a scalar function \(\psi\), let \(\Psi_\ell(x)\) be its evaluation
in the finite algebra \((T_\ell,u_\ell)\). Concretely, form multiplication
by \(x\), take \(\psi\) of that finite matrix, and apply it to \(u_\ell\).
The spectral-interpolation identity proved in `RELATIONAL_QUOTIENT.md` shows
that this is exactly \(O_\ell^\top Q\psi(Q^{-1}O_\ell x)\).
Write \(\Phi_\ell\) and \(\Phi_\ell'\) for \(\psi=\phi,\phi'\).

Starting with the fixed input coordinates
\(x_{a,0}=O_0^\top Q\iota_0v_a\), evaluate

\[
\begin{aligned}
\zeta_{a,\ell}&=S_\ell x_{a,\ell-1},\\
x_{a,\ell}&=(I-P_\ell^{(\ell)})\zeta_{a,\ell}
 +P_\ell^{(\ell)}\Phi_\ell(\zeta_{a,\ell}).
\end{aligned}
\]

This is exact because
\(O_\ell^\top\widetilde F_\ell O_{\ell-1}=S_\ell\).
No \(O_\ell^\top O_{\ell-1}\) is missing: its role is already contained
in the polar transition factor \(S_\ell\).

The terminal feature used by the readout is only
\(H_a=P_L^{(L)}x_{a,L}\). With training columns
\(C=m^{-1/2}[H_1,\ldots,H_m]\), define

\[
\widehat\rho=\rho+C(C^\top C)^{-1}
 \left[\frac{y-c}{\sqrt m}-C^\top\rho\right].
\]

The correction is identical to the supplied correction because
\(H_a=O_L^\top Q\iota_Lh_a^{(L)}\). Using the entire retained forward
vector \(x_{a,L}\) instead would change the correction Gram matrix and the
predictor. The prediction is \(f_a=\widehat\rho^\top H_a\).

For training inputs set \(k_{a,L}=\widehat\rho\), and evaluate backward:

\[
\begin{aligned}
g_{a,\ell}&=(I-P_\ell^{(\ell)})k_{a,\ell}
 +P_\ell^{(\ell)}\mu_\ell
     (\Phi_\ell'(\zeta_{a,\ell}),k_{a,\ell}),\\
k_{a,\ell-1}&=S_\ell g_{a,\ell}.
\end{aligned}
\]

The second identity uses the transpose of the same polar transition factor;
\(S_\ell^\top=S_\ell\). It is the exact lifted adjoint, not a new
gradient convention. Define the projected factors

\[
d_{a,\ell}=P_\ell^{(\ell)}g_{a,\ell},\qquad
s_{a,\ell}=P_{\ell-1}^{(\ell-1)}x_{a,\ell-1}.
\]

The source mask is in frame \(\ell-1\); the target mask is in frame
\(\ell\). Their coordinates need not be transported into a common frame:
they are the two factors of an operator from the former frame to the latter.
The required update representation is therefore

\[
U_\ell=\frac2m\sum_{a=1}^m c_a d_{a,\ell}s_{a,\ell}^\top
 =O_\ell^\top\dot{\widetilde F}_\ell O_{\ell-1}.
\]

The residual matrix also uses only current state:

\[
K_{ab}=H_a^\top H_b+
 \sum_{\ell=1}^L
 (d_{a,\ell}^\top d_{b,\ell})
 (s_{a,\ell}^\top s_{b,\ell}).
\]

Each pairing is between vectors in the same frame. At layer 1 the source
pairing is exactly \(v_a^\top v_b\). This is the original supplied \(K\),
without asserting that it is a tangent kernel of the corrected predictor.

## 5. Derivation of the proposed polar differential equations

Define \(\Omega_\ell=O_\ell^\top\dot O_\ell\), which is skew-symmetric,
and \(\Omega_0=0\). Differentiating
\(\widetilde F_\ell O_{\ell-1}=O_\ell S_\ell\) and multiplying by
\(O_\ell^\top\) gives

\[
U_\ell+S_\ell\Omega_{\ell-1}
 =\Omega_\ell S_\ell+\dot S_\ell.
\]

Since \(\dot S_\ell\) must be symmetric, subtracting the transpose yields

\[
\Omega_\ell S_\ell+S_\ell\Omega_\ell
 =U_\ell-U_\ell^\top
  +S_\ell\Omega_{\ell-1}+\Omega_{\ell-1}S_\ell.
\]

The right-hand side is skew-symmetric. In an orthogonal eigenbasis of
\(S_\ell\), the solution entries are the right-hand-side entries divided
by \(\sigma_i+\sigma_j>0\). This proves existence, uniqueness, and
skew-symmetry of \(\Omega_\ell\). Repeated singular values cause no
singularity; there is no eigenvalue-difference denominator.

Differentiating the formula for \(G_\ell\) directly gives

\[
\dot G_\ell
 =S_\ell U_\ell+U_\ell^\top S_\ell
  +G_\ell\Omega_{\ell-1}-\Omega_{\ell-1}G_\ell.
\]

Thus the proposed commutator \([G_\ell,\Omega_{\ell-1}]\) has the correct
sign. Both terms on the right are symmetric. The angular velocities are computed
in increasing layer order because \(\Omega_\ell\) depends on the previous
one. The forward/backward evaluation and all \(U_\ell\) can be completed
before this angular recursion.

For clarity about tensor index signs, the exact transported-product equation is

\[
\dot T_{\ell,ijk}
 =-\sum_a(\Omega_\ell)_{ia}T_{\ell,ajk}
  +\sum_aT_{\ell,iak}(\Omega_\ell)_{aj}
  +\sum_aT_{\ell,ija}(\Omega_\ell)_{ak}.
\]

The input-index terms are right actions. Writing them with left-action index
placement would reverse their apparent sign because \(\Omega\) is skew.
The remaining equations are

\[
\begin{aligned}
\dot u_\ell&=-\Omega_\ell u_\ell,\qquad
\dot b_j^{(\ell)}=-\Omega_\ell b_j^{(\ell)},\\
\dot\rho&=\frac2m\sum_{a=1}^m c_a H_a-\Omega_L\rho,\qquad
\dot c=-\frac2m Kc.
\end{aligned}
\]

These expressions finish the autonomous evaluation rule. They contain no
unknown frame matrices or original layer maps.

## 6. Reverse lift: checking sufficiency rather than only necessity

To exclude a merely formal coordinate identity, start from a compatible initial
state and a solution of the proposed state equations while \(G_\ell\succ0\)
and the original correction is defined. Integrate the auxiliary equations
\(\dot O_\ell=O_\ell\Omega_\ell\) from the known initial frames. They
preserve orthogonality. These auxiliary matrices are used for proof only; the
runtime right-hand side does not require them.

The tensor, unit, and mask equations imply that their values are precisely the
rotations of the same fixed flattened algebra and indicators. This follows by
differentiating those rotations, which gives the displayed equations and their
initial values. In particular, all algebra identities and projector identities
are preserved.

Set \(S_\ell=G_\ell^{1/2}\). Differentiating its square gives the unique
symmetric solution of
\(S_\ell\dot S_\ell+\dot S_\ell S_\ell=\dot G_\ell\). The matrix

\[
X_\ell=U_\ell+S_\ell\Omega_{\ell-1}-\Omega_\ell S_\ell
\]

is symmetric by the angular Sylvester equation. Substitution using that same
equation gives
\(S_\ell X_\ell+X_\ell S_\ell=\dot G_\ell\). Positivity of
\(S_\ell\) makes this symmetric Sylvester solution unique, so
\(\dot S_\ell=X_\ell\).

Now reconstruct for the proof

\[
\widetilde F_\ell=O_\ell S_\ell O_{\ell-1}^\top.
\]

Differentiating and substituting \(\dot S_\ell=X_\ell\) cancels all
angular terms, giving

\[
\dot{\widetilde F}_\ell=O_\ell U_\ell O_{\ell-1}^\top.
\]

The forward/backward identities then show that this is exactly the flattened
restricted block update from Section 2. The initial reconstructed map is the
initial shear; its derivative has only that shear's off-diagonal block.
Therefore it stays a shear, and its block map follows the supplied optimizer.
The reconstructed readout \(Q^{-1}O_L\rho\) obeys the original top-block
readout equation, and its correction agrees with the original correction.
The residual matrix and equation likewise agree.

This proves an exact reverse lift. Smoothness on the correction domain gives
local uniqueness, so the original compressed trajectory and the proposed state
trajectory correspond throughout their common domain. No change of optimizer,
new arbitrary layer invertibility condition, or lost direction is hidden in
the derivation.

## 7. Degeneracies and remaining limitations

The shear inverse gives

\[
\sigma_{\min}(\widetilde F_\ell)
 \ge\frac1{1+\|\widetilde N_\ell\|}.
\]

Thus on any interval where the original compressed maps remain bounded, the
polar factors stay uniformly positive. Original layer ranks may change freely,
including passage through the zero map. Coincident polar eigenvalues are regular
for both square-root differentiation and the angular Sylvester equation. No
rank assumption on \(A\), \(B_\ell\), or their feature images is introduced.

A direct boundary check is the scalar zero map. Its lifted matrix is
\(F=\left(\begin{smallmatrix}1&0\\b&1\end{smallmatrix}\right)\).
At \(b=0\), with fixed incoming frame \(I\), one has \(S=I\). For an
arbitrary instantaneous rate \(\dot b\), the formulas give

\[
U=\begin{pmatrix}0&0\\\dot b&0\end{pmatrix},\qquad
\Omega=\frac12\begin{pmatrix}0&-\dot b\\\dot b&0\end{pmatrix},\qquad
\dot G=\begin{pmatrix}0&\dot b\\\dot b&0\end{pmatrix}.
\]

All rates are finite at the rank-changing point \(b=0\), and
\(\Omega S+\dot S=U\) with \(\dot S=\dot G/2\), as required.

There are nevertheless genuine limits. If the original corrected-readout matrix
loses rank, this construction encounters exactly that original failure. If an
original map diverges, the lower bound can vanish in the limit; the construction
does not prove global existence. Numerical errors can violate SPD, algebra, mask,
or shear-compatibility constraints even when the exact equations preserve them.
A stable numerical realization requires a separate implementation and error
analysis. Near-coincident spectra in a naive interpolation implementation of the
activation algebra remain a numerical issue, not a mathematical rank obstruction.

Validation inputs are fixed at time zero and occur only in forward prediction.
The correction, forces, readout update, and residual equation use training
indices only. Validation labels are absent, so their outputs are passive.

The fixed ambient dimension is \(D=d+\sum_\ell q_\ell\). Full transported
products cost \(O(LD^3)\) moving scalars; metrics cost \(O(LD^2)\), masks
cost \(O(L(L+1)D)\), and readout/residual state costs \(O(D+m)\). All are
finite polynomial costs, but input dimension is included. Polylogarithmic
dependence on dense width follows only when \(d\), \(L\), and the imported
compressed-width dependencies support it. No unrestricted assertion independent
of \(d\) follows from the shear embedding.

The full transported multiplication tensors carry orientation information.
Together with the polar metrics they can encode the original relevant maps up
to compatible algebra symmetries. The construction avoids reconstructing those
maps during evaluation; it does not prove their information has disappeared.
Unlike the earlier anchored Gram lift, its evolving tensors and metrics both
participate in the current nonlinear feedback. That gives a substantive geometric
decomposition, but calling it a new particle theory or a further compression
would require an additional scientific criterion or theorem.

Exact prediction equality transfers only the supplied compressed-model error
certificate, with its original norm, validation class, probability, and horizon.
The external certificate itself has not been audited here.

The audit therefore supports the exact polar realization with four nonnegotiable
implementation conditions: use algebraic masks, project both update factors,
use only the terminal block for the correction, and initialize all transported
objects from common polar frames. It does not support stronger claims about
state reduction, numerical stability, global fitting, or dense accuracy beyond
the imported certificate.
