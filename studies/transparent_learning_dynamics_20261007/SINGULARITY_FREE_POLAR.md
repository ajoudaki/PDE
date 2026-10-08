# Exact response-Gram dynamics through an invertible memory lift

Status: derived research construction, 2026-10-07. This continues the explicitly authorized second-round moment route. The supervisor supplied the unipotent-shear lift after reading the restricted polar result. The derivation below checks and completes that proposal using only the already supplied compressed-runtime source, `RELATIONAL_QUOTIENT.md`. No additional scientific source or experiment was used.

The construction removes the square-transfer and nonsingularity restrictions from `MOMENT_ROUTE.md`. It gives an exact autonomous realization of the supplied compressed runtime using actual response Gram matrices, coactivation tensors, block masks, a readout response, and residuals. It has polynomial overhead in the compressed dimension. The equations separate changes in response similarities from rotation of nonlinear interaction geometry.

This is an explanatory change of state variables, not an additional information-compression theorem. In particular, the Gram matrix of a shear can encode the original layer map. The exactness claim and that transparency limitation must both remain visible.

This is an internal derivation from the supplied runtime equations. The original dense-to-compressed proof was not supplied or independently audited in this scoped route.

## 1. Supplied runtime in metric-orthonormal algebra coordinates

Use the finite activation-algebra coordinates already constructed in the supplied source. Let \(r_0\le\min(d,N)\) be the span dimension of the \(N\) declared training and passive validation inputs. Their fixed coefficients are \(\xi_a\in\mathbb R^{r_0}\), preserving the input inner products. Layer \(\ell\) has algebra dimension \(r_\ell\le q\), multiplication operation \(\mathcal P_\ell^{\mathrm{block}}\), unit \(u_\ell^{\mathrm{block}}\), and ordinary Euclidean inner product. Each multiplication operation represents the original coordinatewise product in a metric-orthonormal basis. It is commutative, associative, and unital; it need not be self-adjoint in the metric.

There are two source-scope choices. The finite-panel version uses the input span just defined and the supplied panel-generated activation algebras. The all-input version instead sets \(r_0=d\), takes the entire input space \(\mathbb R^d\), and generates the hidden algebras at initialization with \(A(0)\mathbb R^d\subseteq U_1\), the initial readout, closure under multiplication, and closure under the initial forward and adjoint maps. Here \(A(0)\) is the compressed runtime's initial input map before the algebra-coordinate change, and \(U_\ell\) is the generated hidden activation subalgebra in layer \(\ell\). This is the same finite algebra construction with a larger permitted input seed. It still has \(r_\ell\le q\).

In the all-input version the first-layer invariance holds for every \(v\in\mathbb R^d\): the initial image lies in \(U_1\), and each later first-layer update applied to \(v\) is a linear combination of the training backward directions with coefficients \(v_a^\top v\). Subsequent forward and backward invariances follow by the same algebra argument. Consequently the exact realization below agrees with the compressed predictor at every input in \(\mathbb R^d\), and in particular simultaneously at every input on the sphere, throughout the source-runtime existence interval. This extends the domain of exact equality; any claim of dense-model accuracy on that larger domain still requires a source certificate for that domain. The finite-panel construction and its smaller input-span cost are unchanged.

For either source-scope choice, write the source transfers as

\[
R_1:\mathbb R^{r_0}\to\mathbb R^{r_1},\qquad
R_\ell:\mathbb R^{r_{\ell-1}}\to\mathbb R^{r_\ell}\quad(\ell\ge2),
\]

with source readout \(w\in\mathbb R^{r_L}\) and residual state \(c\in\mathbb R^m\). There is no assumption on the ranks or shapes of the \(R_\ell\).

Writing \(h_a^{(0)}=\xi_a\), the source forward and stipulated backward operations are

\[
z_a^{(\ell)}=R_\ell h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\phi(z_a^{(\ell)}),
\]

\[
\delta_a^{(L)}=\phi'(z_a^{(L)})\odot\widehat w,
\qquad
\delta_a^{(\ell)}=
\phi'(z_a^{(\ell)})\odot R_{\ell+1}^\top\delta_a^{(\ell+1)}.
\]

Here scalar functions and the displayed product are evaluated in the relevant finite algebra, exactly as in the source. The corrected readout is

\[
V=\frac1{\sqrt m}[h_1^{(L)},\ldots,h_m^{(L)}],\qquad
\widehat w=w+V(V^\top V)^{-1}
\left[\frac{y-c}{\sqrt m}-V^\top w\right].
\]

The source dynamics are

\[
\dot R_\ell=\frac2m\sum_{a=1}^m c_a
\delta_a^{(\ell)}h_a^{(\ell-1)\top},\qquad
\dot w=\frac2m\sum_{a=1}^m c_a h_a^{(L)},\qquad
\dot c=-\frac2mKc,
\]

\[
K_{ab}=h_a^{(L)\top}h_b^{(L)}
+\sum_{\ell=1}^L
(\delta_a^{(\ell)\top}\delta_b^{(\ell)})
(h_a^{(\ell-1)\top}h_b^{(\ell-1)}).
\]

Only training indices drive these sums. Outputs are \(f_a=\widehat w^\top h_a^{(L)}\), and the training identity is \(f_a=y_a-c_a\). As in the source, work on the domain \(V^\top V>0\). These backward directions and \(K\) are stipulated by that runtime; no claim that they are gradients or the tangent kernel of the corrected predictor is needed.

## 2. An invertible lift that preserves every layer computation

Form the common Hilbert space

\[
\mathcal H=\mathbb R^{r_0}\oplus\mathbb R^{r_1}\oplus\cdots\oplus\mathbb R^{r_L},
\qquad D=\sum_{j=0}^Lr_j.
\]

Let \(I_j\) embed block \(j\) into \(\mathcal H\). Give the input block the ordinary coordinatewise algebra on \(\mathbb R^{r_0}\); no nonlinear input-block operation will affect the predictor. Give each hidden block its supplied activation algebra. The direct-sum multiplication \(\mathcal P^0\) acts independently in the blocks. Its unit is \(u^0\), and the block idempotents are

\[
e_0^0=I_0\mathbf1,\qquad
e_j^0=I_j u_j^{\mathrm{block}}\quad(j\ge1).
\]

They satisfy \(\mathcal P^0(e_j^0,x)=I_jI_j^\top x\), so multiplication by a block idempotent is the orthogonal block projection even though general multiplication need not be self-adjoint.

Replace each source transfer by the full-space shear

\[
F_\ell=I+I_\ell R_\ell I_{\ell-1}^\top.
\]

The nonidentity part \(N_\ell=I_\ell R_\ell I_{\ell-1}^\top\) has \(N_\ell^2=0\), because its source and target blocks are distinct. Hence

\[
F_\ell^{-1}=I-N_\ell
\]

for every source transfer, including rectangular and rank-deficient ones.

Start a full forward memory at \(X_a^{(0)}=I_0\xi_a\). Apply \(F_\ell\), then apply the activation only in block \(\ell\), leaving all other blocks unchanged. Before that step, block \(\ell\) is zero and block \(\ell-1\) contains the source activation. Consequently the step writes \(\phi(R_\ell h_a^{(\ell-1)})\) into block \(\ell\), while keeping the earlier features. Induction gives

\[
X_a^{(\ell)}=I_0\xi_a+\sum_{j=1}^\ell I_jh_a^{(j)}.
\]

The lifted readout is \(I_Lw\). Thus this enlarged representation gives exactly the source predictions; the extra coordinates are the already computed earlier-layer features.

The update has the restricted support

\[
\dot F_\ell=\frac2m\sum_a c_a
(I_\ell\delta_a^{(\ell)})
(I_{\ell-1}h_a^{(\ell-1)})^\top.
\]

This support preserves the shear form. The full backward recursion must preserve the ungated blocks, while the learning pulse selects only the current target block. Keeping that distinction is essential.

## 3. Response Grams and coactivation moments in polar frames

Set \(O_0=I_D\). Recursively take the polar factorization

\[
F_\ell O_{\ell-1}=O_\ell S_\ell,
\qquad O_\ell^\top O_\ell=I,
\qquad S_\ell>0.
\]

This factorization exists uniquely because the shears are invertible. Store the response Gram

\[
G_\ell=S_\ell^2
=O_{\ell-1}^\top F_\ell^\top F_\ell O_{\ell-1}.
\]

Its \(ij\) entry is the inner product of the actual responses of the full forward memory to pulses along the \(i\)-th and \(j\)-th current source-frame directions. The positive square root \(S_\ell=G_\ell^{1/2}\) is computed algebraically from the Gram state.

In frame \(\ell\), store the multiplication table, the full algebra unit, and the one block mask needed at that stage:

\[
\mathcal P_\ell(x,y)=O_\ell^\top\mathcal P^0(O_\ell x,O_\ell y),\qquad
u_\ell=O_\ell^\top u^0,\qquad
e_\ell=O_\ell^\top e_\ell^0.
\]

Write \(\mathcal P_\ell(x,y)_i=\sum_{j,k}T_{\ell,ijk}x_jy_k\). The entries are third-order coactivation moments of the frame vectors. The same block mask selects the current layer's features for the following layer's learning pulse, so one mask per frame suffices. Storing every block mask in every frame would also be valid but is unnecessary.

The readout state is

\[
\rho=O_L^\top I_Lw.
\]

The complete moving state is

\[
\bigl(G_\ell,T_\ell,u_\ell,e_\ell\bigr)_{\ell=1}^L,
\qquad \rho,\qquad c.
\]

The matrices \(F_\ell,R_\ell,O_\ell\) are used for initialization and proof, not retained for evaluating the proposed vector field.

For any scalar activation function \(\psi\), define in frame \(\ell\)

\[
\mathsf L_\ell(x)_{ij}=\sum_kT_{\ell,ikj}x_k,
\qquad
\Psi_\ell(x)=\psi(\mathsf L_\ell(x))u_\ell.
\]

Multiplication in the finite direct-sum algebra is diagonalizable over the reals: in the original hidden coordinates it is coordinatewise multiplication, and the input block is also coordinatewise. Scalar functional calculus therefore gives the exact scalar activation in any frame. Write \(\Phi_\ell\) for \(\psi=\phi\) and \(\Phi'_\ell\) for \(\psi=\phi'\). No activation series is truncated. Repeated eigenvalues do not create a mathematical singularity; a stable finite-precision implementation is a separate issue.

## 4. Forward evaluation and full backward transport

All displayed forward vectors in this section are evaluated from the retained state, not separately evolved. Start with \(x_a^{(0)}=I_0\xi_a\), and set \(h_a^{(0)}=x_a^{(0)}\). The full frame-\(\ell\) preactivation and postactivation memories are

\[
z_a^{(\ell)}=S_\ell x_a^{(\ell-1)},
\]

\[
x_a^{(\ell)}=
\mathcal P_\ell(u_\ell-e_\ell,z_a^{(\ell)})
+\mathcal P_\ell(e_\ell,\Phi_\ell(z_a^{(\ell)})).
\]

The current layer's feature pulse is its masked part,

\[
h_a^{(\ell)}=\mathcal P_\ell(e_\ell,x_a^{(\ell)}).
\]

Here \(h_a^{(\ell)}\in\mathbb R^D\) represents \(I_\ell h_a^{(\ell)}\) from the source model in frame \(O_\ell\). The use of the same layer notation means the original feature with its zero extension and frame transformation, not a new feature approximation.

Form the corrected readout from the masked final features:

\[
C=\frac1{\sqrt m}[h_1^{(L)},\ldots,h_m^{(L)}],\qquad
\widehat\rho=\rho+C(C^\top C)^{-1}
\left[\frac{y-c}{\sqrt m}-C^\top\rho\right],
\qquad
f_a=\widehat\rho^\top h_a^{(L)}.
\]

The readout and the correction are supported in the final block as represented by its current mask.

For each training sample set the full backward vector \(b_a^{(L)}=\widehat\rho\), and recurse downward:

\[
g_a^{(\ell)}=
\mathcal P_\ell(u_\ell-e_\ell,b_a^{(\ell)})
+\mathcal P_\ell\left(e_\ell,
\mathcal P_\ell(\Phi'_\ell(z_a^{(\ell)}),b_a^{(\ell)})\right),
\]

\[
d_a^{(\ell)}=\mathcal P_\ell(e_\ell,g_a^{(\ell)}),
\qquad
b_a^{(\ell-1)}=S_\ell g_a^{(\ell)}.
\]

The full \(g_a^{(\ell)}\) is transported to the previous frame. The masked \(d_a^{(\ell)}\) is the learning direction for the original layer. Transporting only the masked vector instead would in general change the lifted backward computation.

To check that its masked component is the original backward signal, start at the final layer. The lifted adjoint shear transports the current target-block signal to the preceding block by \(R_\ell^\top\), while retaining signals already present in later blocks. The next masked gate changes only the preceding block. Induction gives \(d_a^{(\ell)}=O_\ell^\top I_\ell\delta_a^{(\ell)}\) at every layer. No frame-overlap matrix is needed: \(S_\ell=O_\ell^\top F_\ell O_{\ell-1}\) transports forward memories, and its transpose, equal to itself, transports backward vectors.

## 5. Closed residual-driven moment dynamics

Compute the current physical pulse interaction in the two adjacent frames:

\[
D_\ell=\frac2m\sum_{a=1}^m c_a
d_a^{(\ell)}h_a^{(\ell-1)\top}.
\]

It includes the actual residual factors and equals \(O_\ell^\top\dot F_\ell O_{\ell-1}\). It is computed when evaluating the vector field, rather than retained as a moving transfer parameter.

Set \(\Omega_0=0\). In ascending layer order, solve for the skew matrix \(\Omega_\ell\):

\[
\Omega_\ell S_\ell+S_\ell\Omega_\ell
=D_\ell-D_\ell^\top
+S_\ell\Omega_{\ell-1}+\Omega_{\ell-1}S_\ell.
\]

For \(S_\ell>0\), this has a unique skew solution; in its eigenbasis each \(ij\) entry is divided by \(\sigma_i+\sigma_j>0\). Then evolve

\[
\dot G_\ell=S_\ell D_\ell+D_\ell^\top S_\ell
+G_\ell\Omega_{\ell-1}-\Omega_{\ell-1}G_\ell,
\]

\[
\dot{\mathcal P}_\ell(x,y)
=-\Omega_\ell\mathcal P_\ell(x,y)
+\mathcal P_\ell(\Omega_\ell x,y)
+\mathcal P_\ell(x,\Omega_\ell y),
\qquad
\dot u_\ell=-\Omega_\ell u_\ell,
\qquad
\dot e_\ell=-\Omega_\ell e_\ell.
\]

The equation for \(\mathcal P_\ell\) is an explicit action on the three indices of \(T_\ell\). It generates no higher tensor order. Complete the system by

\[
\dot\rho=\frac2m\sum_a c_a h_a^{(L)}-\Omega_L\rho,
\qquad
\dot c=-\frac2mKc,
\]

\[
K_{ab}=h_a^{(L)\top}h_b^{(L)}
+\sum_{\ell=1}^L
(d_a^{(\ell)\top}d_b^{(\ell)})
(h_a^{(\ell-1)\top}h_b^{(\ell-1)}).
\]

This is a finite autonomous system. Its sequence of algebraic evaluation is: take positive Gram square roots; run masked forward evaluation; correct the readout; run the full masked backward recursion; form the pulse interactions; solve the angular-velocity recursion; evaluate the displayed derivatives. No current source map or orthogonal frame is consulted.

Every term is label-driven. If \(c=0\), then all \(D_\ell=0\). Starting with \(\Omega_0=0\), the unique skew solve gives all \(\Omega_\ell=0\), and every retained derivative vanishes. Validation inputs are evaluated in the forward pass but do not appear in any driving sum, correction column, or backward update.

## 6. Exactness and absence of transfer-rank singularities

Differentiating the defining polar relation gives

\[
\dot S_\ell=-\Omega_\ell S_\ell+D_\ell+S_\ell\Omega_{\ell-1}.
\]

Its symmetry is exactly the angular-velocity equation. Differentiating \(G_\ell=O_{\ell-1}^\top F_\ell^\top F_\ell O_{\ell-1}\) gives the proposed Gram equation. Differentiating the multiplication, unit, mask, and readout definitions gives the remaining equations. Thus a source-runtime solution produces a moment-system solution with identical predictions.

For the converse, start from the stated moment initialization. On the open domain \(G_\ell>0\) and \(C^\top C>0\), the vector field is locally Lipschitz. Solve \(\dot O_\ell=O_\ell\Omega_\ell\) with the initialized frames for the proof only. Orthogonality is preserved because each \(\Omega_\ell\) is skew. The tensor, unit, and mask equations imply that their values are the original fixed algebra objects expressed in these frames: both expressions solve the same linear transformation equations with the same initial conditions.

Set \(F_\ell=O_\ell G_\ell^{1/2}O_{\ell-1}^\top\). The derivative of the positive square root is uniquely determined by the Sylvester equation

\[
S_\ell\dot S_\ell+\dot S_\ell S_\ell=\dot G_\ell.
\]

Substitution of the proposed Gram law gives the polar derivative displayed above, hence

\[
\dot F_\ell=O_\ell D_\ell O_{\ell-1}^\top.
\]

Each lifted \(d_a^{(\ell)}\) is supported in physical block \(\ell\), and each lifted \(h_a^{(\ell-1)}\) is supported in physical block \(\ell-1\), by the mask identities. Thus \(\dot F_\ell\) has exactly the original restricted support. Since the initial value is \(I+I_\ell R_\ell(0)I_{\ell-1}^\top\), the entire reconstructed path remains a shear of that form. The forward and backward inductions then recover the source runtime and all of its predictions. The lifted readout also stays supported in block \(L\) because its physical derivative is a sum of final-block features.

The shear identity prevents rank singularities independently of the rank of \(R_\ell\). Quantitatively,

\[
\|F_\ell\|\le1+\|R_\ell\|,\qquad
\|F_\ell^{-1}\|\le1+\|R_\ell\|,
\]

so

\[
(1+\|R_\ell\|)^{-2}I
\preceq G_\ell
\preceq(1+\|R_\ell\|)^2I.
\]

Therefore the polar domain cannot fail at a finite time at which the source maps remain finite. A uniform bound on those maps gives a uniform positive lower bound for the Gram matrices and for the eigenvalue sums in the skew solves. Even without such a uniform bound, the exact construction remains defined at every finite time for which the source runtime exists. The original readout-correction rank condition is unchanged and is the only inherited rank-domain restriction.

Local uniqueness consequently identifies both systems on the entire source-runtime existence interval. This proof uses observable equality, not an assumption that the compressed source tracks dense weights or dense hidden features.

## 7. Cost, provenance, and what becomes transparent

The state has

\[
L\left[\frac{D(D+1)}2+D^3+2D\right]+D+m
\]

stored scalar entries before exploiting algebraic constraints. Fixed inputs cost \(Nr_0\), labels cost \(m\), and the frame-zero algebra is fixed initialization data. All other multiplication tensors are initialized from the source initialization and their polar frames, then evolved. It is not necessary to retain the original layer maps or frames after producing the initial state.

At fixed depth, the panel version has \(D\le r_0+Lq\le N+Lq\), while the all-input version has \(D\le d+Lq\). Storage and arithmetic evaluation therefore have polynomial overhead in the corresponding explicit dimensions. The all-input activation algebra is initialized from the full initial input map; no future validation inputs or labels are required to define its state. Matrix square roots, skew Sylvester solves, and finite-dimensional activation evaluation are standard finite matrix operations; dense multiplication-tensor contractions also have polynomial cost. These are exact-real arithmetic statements. They do not supply a precision-uniform implementation or a conditioning theorem for a particular matrix-function algorithm.

The response-Gram law has an exact stretching/rotation decomposition in the midpoint frame. Define the symmetric pulse interaction and the relative angular velocity by

\[
E_\ell=\frac{D_\ell+D_\ell^\top}{2},\qquad
\Lambda_\ell=\Omega_\ell-\Omega_{\ell-1}.
\]

The skew solve is

\[
\Lambda_\ell S_\ell+S_\ell\Lambda_\ell=D_\ell-D_\ell^\top.
\]

Use the matrix commutator convention \([G,\Omega]=G\Omega-\Omega G\). Writing \(D_\ell=E_\ell+(D_\ell-D_\ell^\top)/2\) and substituting the preceding identity gives

\[
S_\ell D_\ell+D_\ell^\top S_\ell
=S_\ell E_\ell+E_\ell S_\ell
+\frac12[G_\ell,\Lambda_\ell],
\]

and hence

\[
\dot G_\ell-
\left[G_\ell,\frac{\Omega_\ell+\Omega_{\ell-1}}2\right]
=S_\ell E_\ell+E_\ell S_\ell.
\]

Thus the symmetric pulse interaction gives the similarity change after subtracting rotation at the midpoint angular velocity. The skew interaction fixes the relative frame rotation and can also change Gram entries in the preceding frame when \(G_\ell\) is anisotropic; it is not correct to say that only the symmetric part affects the raw \(\dot G_\ell\). The coactivation tensor transports under \(\Omega_\ell\), recording the nonlinear gating geometry relative to the transmitted pulse directions. These frame terms derive from the same residual-driven pulse update, with no external forcing or prerecorded dynamics.

There is an unavoidable limitation to the claim being made. In the original physical source/target blocks,

\[
F=\begin{pmatrix}I&0\\R&I\end{pmatrix}
\quad\Longrightarrow\quad
F^\top F=
\begin{pmatrix}I+R^\top R&R^\top\\R&I\end{pmatrix}.
\]

Thus a shear Gram can contain the original map as a cross-block entry. The moving algebra and masks retain the orientation needed to read such relationships in changing frames. This representation does not discard generic relevant parameter information, and its exact equivalence should not be advertised as an additional aggregate compression theorem. If the intended scientific criterion excludes all invertible geometric encodings of the compressed state, this candidate does not meet that stricter criterion. Its added mathematical content is a closed law in response similarities and coactivation geometry with an explicit stretching/rotation interaction mechanism and no evolving transfer table as primary state.

## 8. Transfer of an already proved observable certificate

Suppose an independently established certificate for the supplied compressed runtime states, on a specified event and for the declared finite input panel,

\[
\sup_{t\in\mathcal T}\max_a
|f_a^{\mathrm{dense}}(t)-f_a^{\mathrm{compressed}}(t)|\le E(n,q),
\]

and supplies existence and invertibility of the readout correction on the same time set \(\mathcal T\). The exact equality proved above gives

\[
f_a^{\mathrm{moment}}(t)=f_a^{\mathrm{compressed}}(t)
\]

on that set, and hence precisely the same dense-prediction error, event, norm, panel, and horizon for the moment system. In particular an all-time source certificate transfers as an all-time certificate. No accuracy guarantee for internal hidden states, no new input generalization, and no improvement of the original error follows.

For the all-input source-scope choice, the exact equality holds for every input. Accordingly, if the source certificate instead controls \(\sup_{t\in\mathcal T}\sup_{\|v\|=1}|f^{\mathrm{dense}}(v,t)-f^{\mathrm{compressed}}(v,t)|\), the identical sphere-uniform certificate transfers. Pointwise or finite-panel source accuracy cannot be upgraded to that stronger norm by exact conjugacy alone.

The first-round restricted-polar rank-domain gap is repaired by the invertible memory lift. The source compression certificate remains imported: its original proof has not been independently audited here. Whether this explicit geometric mechanism satisfies the desired degree of scientific transparency remains distinct from the exactness and transfer theorem.
