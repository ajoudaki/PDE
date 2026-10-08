# Observable moments, response Grams, and moving coactivation geometry

Later extension: [SINGULARITY_FREE_POLAR.md](SINGULARITY_FREE_POLAR.md) removes this note's square/invertible-transfer restriction using an invertible memory lift. Its exact domain extension supersedes the restricted-domain limitation below; the information-content and transparency caveats remain relevant.

Status: bounded second-round theoretical construction, 2026-10-07. After the independent response-memory result was frozen, the supervisor explicitly supplied the complete `RELATIONAL_QUOTIENT.md` as the compressed-runtime source and as a candidate to critique. That is the only additional scientific source read. No literature, other studies, experiments, or Git operations were used. Required research, rigorous-proof, and canonical-notation instructions remain in force.

There is a useful exact geometric closure on a restricted domain: replace each square invertible hidden transfer by its response Gram matrix, and evolve the coactivation tensor in the associated moving polar frame. Its equations separate similarity deformation from rotation of nonlinear interaction geometry. The state contains actual similarities and coactivation moments, not evolving entries of a transfer map. However, this is a nonlinear change of state variables with polynomial overhead, not a further information reduction, and the present proof does not cover rectangular transfers or passage through singular transfers.

For the unrestricted supplied runtime, finite-atomic moment closure by itself does not fix the transparency issue. A generic fixed activation algebra resolves all individual atoms, so its complete moment state is an invertible encoding of neuron-level information up to permutation. That structural point is proved first.

## 1. What finite activation algebras remember

Let (U\subseteq\mathbb R^q) be a linear subspace containing the coordinatewise unit (\mathbf1) and closed under coordinatewise multiplication. Define an equivalence relation on coordinate indices by

\[
i\sim j\quad\Longleftrightarrow\quad x_i=x_j
\text{ for every }x\in U.
\]

Every vector in (U) is constant on these equivalence classes. Conversely, (U) contains the indicator of each class. To prove this, choose a basis (x^{(1)},\ldots,x^{(r)}) of (U). Distinct classes have different vectors of evaluations ((x_i^{(1)},\ldots,x_i^{(r)})). Choose coefficients outside the finitely many hyperplanes on which two such evaluation vectors have equal linear combination. The resulting (x\in U) takes a distinct value (\lambda_C) on each class (C). The Lagrange polynomial

\[
p_C(s)=\prod_{D\ne C}\frac{s-\lambda_D}{\lambda_C-\lambda_D}
\]

satisfies (p_C(x)=\mathbf1_C\in U), because (U) contains the unit and is closed under multiplication. These class indicators span all block-constant vectors. Therefore (U) is exactly the algebra of functions constant on a partition of the (q) coordinates, and its dimension is the number of blocks.

In particular, if one seed vector has pairwise distinct coordinates, its generated unital algebra is all of (\mathbb R^q). This is a generic situation for a seed with an absolutely continuous distribution that assigns probability zero to equal-coordinate hyperplanes. The precise distribution of a particular compressed initialization must be checked before asserting that probabilistic condition there.

This result has two implications for a moment proposal.

First, a complete finite coactivation algebra is a valid exact representation, but generically its primitive idempotents identify individual hidden coordinates. Its multiplication table contains those atoms up to permutation; it does not erase the nonlinear orientation information that makes a Gram-only model fail.

Second, a simple landmark moment closure is directly invertible. With distinct fixed landmark values (\lambda_1,\ldots,\lambda_q), the (q) moments

\[
\mu_k(x)=\sum_{i=1}^q\lambda_i^k x_i,
\qquad k=0,\ldots,q-1,
\]

determine the entire vector (x\): the Vandermonde matrix has determinant (\prod_{i<j}(\lambda_j-\lambda_i)\ne0). Likewise, the (q^2) moments (\sum_{i,j}\lambda_i^k B_{ij}\nu_j^l), with distinct source and target landmarks, determine the full transfer matrix (B). Calling these quantities moments does not make their dynamics an aggregate explanation.

These are objections to specific complete atomic constructions. They are not a theorem ruling out every finite observable closure.

## 2. Restricted setting for a different, geometrically meaningful state

Use the metric-orthonormal activation-algebra coordinates from the supplied runtime source. In these coordinates all layer inner products are ordinary dot products. To distinguish this derivation from the proposed state, temporarily denote the hidden transfer matrices by (R_\ell(t)), (\ell=2,\ldots,L), their readout by (\rho_{\mathrm{old}}(t)), and the fixed multiplication operations by (\mathcal P_\ell^0). Their fixed units are (u_\ell^0). The runtime equations in these coordinates are exactly those in the supplied source.

Assume here that the hidden algebra dimensions are all equal to (r), and that every (R_\ell(t)\in\mathbb R^{r\times r}), (\ell\ge2), is invertible on the time interval in question. These are additional assumptions; the general runtime does not impose them. The first input map need not be square or invertible.

There are (N) declared training and passive validation inputs, with fixed input Gram values (g_{ab}=v_a^\top v_b). Store the first-layer preactivation coefficients (p_a(t)\in\mathbb R^r) for these inputs. They are moments of actual input responses against the fixed first-layer landmark basis, not a transfer matrix on undeclared inputs. The first-layer frame stays fixed.

For the hidden transfers, define orthogonal matrices (O_1=I), and recursively take the polar decompositions

\[
R_\ell O_{\ell-1}=O_\ell S_\ell,
\qquad
S_\ell=(O_{\ell-1}^\top R_\ell^\top R_\ell O_{\ell-1})^{1/2}>0.
\]

Define the response Gram matrices

\[
G_\ell=S_\ell^2.
\]

Their entries have a direct observable meaning: (G_{\ell,ij}) is the similarity between the two target preactivation responses to unit feature pulses along the (i)-th and (j)-th current source-frame directions. The positive square root (S_\ell=G_\ell^{1/2}) is evaluated from this Gram matrix, rather than evolved as a transfer state.

The moving multiplication operation and its unit are

\[
\mathcal P_\ell(x,y)=
O_\ell^\top\mathcal P_\ell^0(O_\ell x,O_\ell y),
\qquad
u_\ell=O_\ell^\top u_\ell^0.
\]

Writing (\mathcal P_\ell(x,y)_i=\sum_{j,k}T_{\ell,ijk}x_jy_k), each (T_{\ell,ijk}) is a coactivation moment: the receiving frame vector paired with the coordinatewise product of two frame vectors. This is generally not a fully symmetric tensor because the original metric need not make multiplication self-adjoint.

The new readout state is (\rho=O_L^\top\rho_{\mathrm{old}}). The moving state consists of

\[
(p_a)_{a=1}^N,\quad (G_\ell)_{\ell=2}^L,\quad
(T_\ell,u_\ell)_{\ell=2}^L,\quad\rho,\quad c.
\]

The first-layer multiplication tensor and unit remain fixed. The orthogonal frames and transfer matrices are used to derive and initialize these quantities, but are not required to evolve them.

## 3. Evaluation entirely from the moment state

For a scalar function (\psi), multiplication in the finite algebra defines the matrix

\[
\mathsf L_\ell(x)_{ij}=\sum_kT_{\ell,ikj}x_k,
\qquad
\Psi_\ell(x)=\psi(\mathsf L_\ell(x))u_\ell.
\]

The matrix function is evaluated on the finite real spectrum, using polynomial interpolation on distinct eigenvalues or an equivalent matrix-function rule. The source proves why this gives exactly the coordinatewise scalar function in the original algebra. Orthogonal change of frame preserves that identity. Use (\Phi_\ell) for (\psi=\phi) and (\Phi'_\ell) for (\psi=\phi'); the latter means scalar differentiation before functional calculus.

Compute the forward pass from the new state:

\[
z_a^{(1)}=p_a,\qquad
h_a^{(1)}=\Phi_1(p_a),\qquad
z_a^{(\ell)}=S_\ell h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\Phi_\ell(z_a^{(\ell)}).
\]

Only training features enter the corrected readout:

\[
C=\frac1{\sqrt m}[h_1^{(L)},\ldots,h_m^{(L)}],\qquad
\widehat\rho=\rho+C(C^\top C)^{-1}
\left[\frac{y-c}{\sqrt m}-C^\top\rho\right].
\]

As in the supplied runtime, this is defined on the domain (C^\top C>0), and the evaluated outputs are (f_a=\widehat\rho^\top h_a^{(L)}). On training inputs (f_a=y_a-c_a).

The backward directions are

\[
d_a^{(L)}=\mathcal P_L(\Phi'_L(z_a^{(L)}),\widehat\rho),
\qquad
d_a^{(\ell)}=
\mathcal P_\ell(\Phi'_\ell(z_a^{(\ell)}),S_{\ell+1}d_a^{(\ell+1)}).
\]

The same (S_{\ell+1}) appears in the forward and adjoint transport because it is symmetric. The nonlinear gate still uses the possibly nonsymmetric multiplication tensor; no self-adjoint gate assumption is introduced.

Define the actual residual-driven pulse interaction matrix, computed afresh from current features and backward responses, by

\[
D_\ell=\frac2m\sum_{a=1}^m c_a
d_a^{(\ell)}h_a^{(\ell-1)\top},\qquad \ell\ge2.
\]

It is not an additional stored transfer state. It is the moment-frame representation of the current physical transfer velocity, and already includes its residual factors.

## 4. Closed label-driven equations

Set the first-layer frame angular velocity to (\Omega_1=0). For (\ell=2,\ldots,L), determine the skew-symmetric matrix (\Omega_\ell) from

\[
\Omega_\ell S_\ell+S_\ell\Omega_\ell
=D_\ell-D_\ell^\top
+S_\ell\Omega_{\ell-1}+\Omega_{\ell-1}S_\ell.
\]

This is a finite, uniquely solvable linear equation: in an orthonormal eigenbasis of (S_\ell>0), its (ij) entry divides the skew right-hand side by the positive number (\sigma_i+\sigma_j). Equivalently, (\Omega_\ell-\Omega_{\ell-1}) is obtained by applying this inverse to (D_\ell-D_\ell^\top).

The response similarities evolve by

\[
\dot G_\ell
=S_\ell D_\ell+D_\ell^\top S_\ell
+G_\ell\Omega_{\ell-1}-\Omega_{\ell-1}G_\ell.
\]

The coactivation law is the following identity for all coefficient vectors (x,y):

\[
\dot{\mathcal P}_\ell(x,y)
=-\Omega_\ell\mathcal P_\ell(x,y)
+\mathcal P_\ell(\Omega_\ell x,y)
+\mathcal P_\ell(x,\Omega_\ell y),
\qquad
\dot u_\ell=-\Omega_\ell u_\ell.
\]

This is an explicit linear action on the three indices of (T_\ell), and therefore closes on the stored tensor. No higher coactivation moments are generated.

The remaining equations are

\[
\dot p_a=\frac2m\sum_{b=1}^m c_b d_b^{(1)}g_{ba},\qquad
\dot\rho=\frac2m\sum_{a=1}^m c_a h_a^{(L)}-\Omega_L\rho,
\qquad
\dot c=-\frac2mKc,
\]

where the supplied runtime coefficient is evaluated from current similarities:

\[
K_{ab}=h_a^{(L)\top}h_b^{(L)}
+(d_a^{(1)\top}d_b^{(1)})g_{ab}
+\sum_{\ell=2}^L
(d_a^{(\ell)\top}d_b^{(\ell)})
(h_a^{(\ell-1)\top}h_b^{(\ell-1)}).
\]

These formulas determine every derivative from the retained state and fixed input Gram and label data. They are autonomous. In particular, when (c=0), every (D_\ell=0); the angular-velocity recursion gives every (\Omega_\ell=0); and all stored-state derivatives vanish. Frame rotation is itself driven by learning, not by an externally selected clock.

The interaction mechanism is tangible. Symmetrized pulse writes change the similarities of transmitted feature directions. The antisymmetric part rotates the frame in which the nonlinear coactivation table is expressed. The two effects combine because later feature gates depend on that table. Pure response Grams omit the second effect.

## 5. Verification of exactness on the stated domain

Write (\dot O_\ell=O_\ell\Omega_\ell), with skew (\Omega_\ell). Differentiating (S_\ell=O_\ell^\top R_\ell O_{\ell-1}) gives

\[
\dot S_\ell=-\Omega_\ell S_\ell+D_\ell+S_\ell\Omega_{\ell-1}.
\]

The requirement that (\dot S_\ell) remain symmetric is exactly the displayed angular-velocity equation. Differentiating (G_\ell=O_{\ell-1}^\top R_\ell^\top R_\ell O_{\ell-1}) gives

\[
\dot G_\ell=-\Omega_{\ell-1}G_\ell
+D_\ell^\top S_\ell+S_\ell D_\ell
+G_\ell\Omega_{\ell-1},
\]

which is the proposed similarity law. Differentiating the definition of (\mathcal P_\ell) gives its three rotation terms and the unit equation. Differentiating (\rho=O_L^\top\rho_{\mathrm{old}}) gives the readout equation. The first-layer signal equation follows by evaluating the supplied (\dot A) on each fixed input.

Conversely, start the proposed system from the moment state produced by the initial polar decompositions. On any interval where its (G_\ell) remain positive definite and (C^\top C>0), solve (\dot O_\ell=O_\ell\Omega_\ell) for verification only, and set (R_\ell=O_\ell S_\ell O_{\ell-1}^\top). The derivative of the positive square root is uniquely determined by

\[
S_\ell\dot S_\ell+\dot S_\ell S_\ell=\dot G_\ell,
\]

again because all eigenvalue sums are positive. Substitution of the proposed (\dot G_\ell\) shows that this derivative equals (-\Omega_\ell S_\ell+D_\ell+S_\ell\Omega_{\ell-1}). Differentiating the reconstructed (R_\ell) therefore gives (\dot R_\ell=O_\ell D_\ell O_{\ell-1}^\top), precisely the supplied transfer velocity. The tensor and readout reconstruction gives the corresponding original operations and update. Forward and backward passes agree by induction, and all inner products are preserved.

All maps used here are smooth on this positive-definite domain, so the finite vector fields are locally Lipschitz there. Local uniqueness identifies the trajectories on their common interval of existence. This establishes exact predictions, including the passive panel, on that interval. It does not require reconstructing a transfer matrix during evolution.

Validation labels never enter the construction, and validation indices do not drive any sum. Their first-layer responses are propagated by the same training-driven input Gram law. Thus the finite panel remains passive.

## 6. Complexity, interpretation, and the unresolved domain boundary

The moving storage is (Nr+O(Lr^3)+m): first-layer response moments, symmetric response Grams, coactivation tensors and units, the readout, and residuals. The fixed input Gram costs (N^2); its known low-rank structure can also be retained. Initialization uses the original compressed initialization, the finite algebra data, polar decompositions, and declared input responses. No trained trajectory or future coefficient is used. Algebra evaluation, square roots, skew Sylvester solves, and tensor contractions have polynomial arithmetic cost. No uniform finite-precision conditioning bound is claimed.

If the relevant compressed width is polylogarithmic in dense width, this overhead is still polynomial in that retained width. If a dense-to-compressed observable certificate applies and the polar domain persists on its entire horizon, exact conjugacy transfers that certificate with the same observable, norm, probability, and horizon. The persistence of the polar domain is an additional required hypothesis, not something supplied by the predictor approximation certificate.

This construction is more than replacing a transfer table by its entries against new fixed landmarks: the primary objects are response similarities and third-order coactivation moments, and their equations exhibit symmetric versus antisymmetric pulse interactions. Nevertheless, the moving coactivation tensors retain the orientation information removed from the transfer matrices. Generically the state retains the same relevant information as the compressed network, encoded on a constrained manifold of larger ambient dimension. It should be presented as an explanatory geometric realization, not additional state compression or an escape from nonlinear orientation information.

The singularity problem is substantive. At a zero singular value, the positive polar factor may fail to have a differentiable continuation. In one dimension (R=b\ne0), (G=b^2) and (S=|b|); a crossing of (b=0) requires a sign change in the polar frame. The Gram by itself loses the sign, and the frame/coactivation variables may have to jump. Rectangular transfers likewise do not supply square orthogonal polar factors of the form used above. The supplied runtime permits both situations.

Adding fixed identity landmarks can make a larger probe frame nonsingular, but the cross-Gram between those identities and transferred probes directly encodes the original transfer entries. That gives an exact chart of the already criticized kind, not a resolution of the stronger demand. An invertible shear dilation has the same issue: its Gram contains the original transfer as an off-diagonal block. These repairs are not claimed as substantive observable closure.

Therefore the present conclusions are separate. Complete finite-atomic moments generically preserve neuron identity; the restricted polar construction provides an exact and interpretable Gram/coactivation dynamics; and a globally valid version for the actual variable-width runtime remains open. A useful next mathematical question is whether the stipulated small-label regime supplies a uniform nonsingularity certificate for a square version of that runtime, or whether a regular observable chart can cross singular strata without reverting to an encoded transfer table.
