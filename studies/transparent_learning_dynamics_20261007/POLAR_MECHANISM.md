# What the polar response geometry reveals—and what it retains

This bounded extension uses only the supervisor's supplied shear/polar equations and the author's already frozen `OBSERVABLE_GEOMETRY.md`. It does not import another study or a dense-model certificate. The supplied polar equations are correct. They yield an exact account of how signed learning pulses change response similarities and rotate the activation algebra. Their information content, however, generally remains that of the compressed layer maps: the off-diagonal block of a shear Gram already contains the original map.

The useful scientific statement is therefore an exact geometric representation with explicit mechanisms, not an additional compression theorem or a general new theory of learning.

## 1. The objects and their measured similarities

Use fixed orthonormal coordinates for the direct-sum Hilbert space

\[
\mathcal H=\mathcal H_0\oplus\mathcal H_1\oplus\cdots\oplus\mathcal H_L,
\]

where \(\mathcal H_0\) is the declared input span and \(\mathcal H_\ell\) is compressed layer \(\ell\), with its stipulated positive-definite metric. Let \(D=\dim\mathcal H\). The symbols \(\iota_\ell\) and \(\pi_\ell=\iota_\ell^\top\) denote the isometric block injection and projection in these orthonormal coordinates.

For \(\ell\ge2\), lift \(B_\ell:\mathcal H_{\ell-1}\to\mathcal H_\ell\) to

\[
F_\ell=I+\iota_\ell B_\ell\pi_{\ell-1}.
\]

For layer 1, use \(B_1=A\) on the input span. Because the source and target blocks are distinct, \(N_\ell=\iota_\ell B_\ell\pi_{\ell-1}\) obeys \(N_\ell^2=0\), and

\[
F_\ell^{-1}=I-N_\ell.
\]

Each shear is invertible even when its layer map is zero or rank deficient. Starting with \(O_0=I\), define the sequential polar factorization by

\[
F_\ell O_{\ell-1}=O_\ell S_\ell,
\qquad
S_\ell=(O_{\ell-1}^\top F_\ell^\top F_\ell O_{\ell-1})^{1/2},
\qquad
O_\ell=F_\ell O_{\ell-1}S_\ell^{-1}.
\tag{1}
\]

The square root is the positive-definite one: diagonalize its positive-definite argument and take the positive square root of each eigenvalue. This construction proves directly that \(O_\ell\) is orthogonal and \(S_\ell\) is positive definite. Put

\[
G_\ell=S_\ell^2.
\]

This \(G_\ell\) is an **operator-response Gram**, not the sample feature Gram \(\langle h_a^{(\ell)},h_b^{(\ell)}\rangle\). For coefficient vectors \(u,v\) in the preceding stage's frame,

\[
u^\top G_\ell v
=\langle F_\ell O_{\ell-1}u,F_\ell O_{\ell-1}v\rangle_{\mathcal H}.
\tag{2}
\]

It measures similarities of the responses to specified state perturbations. In the fixed physical source/target blocks, it determines, for example,

\[
\begin{aligned}
\langle F_\ell\iota_{\ell-1}h,F_\ell\iota_{\ell-1}k\rangle
&=\langle h,k\rangle+\langle B_\ell h,B_\ell k\rangle,\\
\langle F_\ell\iota_{\ell-1}h,F_\ell\iota_\ell r\rangle
&=\langle B_\ell h,r\rangle.
\end{aligned}
\tag{3}
\]

The second pairing is the signed transmitted response of \(h\) in target direction \(r\). Thus the matrix contains both response lengths and cross-block transfer information.

The positivity is created by the invertible embedding, not by a lower bound on any training feature Gram. One has \(\det G_\ell=1\), since every shear has determinant one, and

\[
\operatorname{tr}G_\ell=D+\|B_\ell\|_F^2.
\]

These are properties of the chosen representation. They do not assert conservation of sample similarities or training-flow volume.

## 2. Exact pulse equations and their derivation

Let \(c_s=y_s-f_s\) denote the training deficit. Under the stipulated compressed update, define the receiving and sending pulse coordinates

\[
p_{\ell s}=O_\ell^\top\iota_\ell\delta_s^{(\ell)},
\qquad
q_{\ell s}=O_{\ell-1}^\top\iota_{\ell-1}h_s^{(\ell-1)}.
\]

For layer 1, replace \(h_s^{(0)}\) by the fixed input vector. The source runtime's metrics are already incorporated in the Hilbert-space orthonormal coordinates. Its update gives

\[
U_\ell=O_\ell^\top\dot F_\ell O_{\ell-1}
=\frac2m\sum_{s=1}^m c_sp_{\ell s}q_{\ell s}^\top.
\tag{4}
\]

The pulse directions are those prescribed by the runtime; no assertion that they are gradients of a corrected predictor is needed. Define the angular velocities

\[
\Omega_\ell=O_\ell^\top\dot O_\ell,
\qquad \Omega_\ell^\top=-\Omega_\ell,
\qquad \Omega_0=0.
\]

Suppress a fixed layer index temporarily, and write \(\Omega_-\) for \(\Omega_{\ell-1}\). Differentiating (1) gives

\[
\dot S=U+S\Omega_- -\Omega S.
\tag{5}
\]

The equality of (5) with its transpose yields

\[
\Omega S+S\Omega
=U-U^\top+S\Omega_-+\Omega_-S.
\tag{6}
\]

Differentiating \(G=O_-^\top F^\top FO_-\) separately gives

\[
\dot G=SU+U^\top S+[G,\Omega_-],
\qquad [X,Y]=XY-YX.
\tag{7}
\]

This confirms the supplied formulas, including the side on which each \(S\) multiplies \(U\) and the sign of the frame commutator. In an eigenbasis of \(S\), the linear map \(X\mapsto XS+SX\) multiplies entry \((i,j)\) by \(s_i+s_j>0\). Therefore (6) has a unique solution, which is skew-symmetric because its right-hand side is skew-symmetric. There is no denominator involving a singular value of \(B_\ell\), a residual, or a difference of eigenvalues.

For test directions \(u,v\), remove the preceding frame's rotation by defining \(\mathring G=\dot G-[G,\Omega_-]\). Equations (4) and (7) give

\[
u^\top\mathring Gv
=\frac2m\sum_s c_s
\left[(p_s^\top Su)(q_s^\top v)+(q_s^\top u)(p_s^\top Sv)\right].
\tag{8}
\]

A deficit changes a response similarity through a source overlap and a receiving overlap. On a single test direction,

\[
u^\top\mathring Gu
=\frac4m\sum_s c_s(p_s^\top Su)(q_s^\top u).
\]

This is signed: response lengths can grow or shrink. Positive definiteness of \(G\) does not require a positive-semidefinite derivative.

## 3. What is symmetric deformation and what is rotation?

Decompose the pulse matrix into its symmetric and skew parts,

\[
E=(U+U^\top)/2,
\qquad Z=(U-U^\top)/2,
\qquad \Lambda=\Omega-\Omega_-.
\]

Equation (6) simplifies exactly to

\[
\Lambda S+S\Lambda=2Z.
\tag{9}
\]

Thus the skew pulse interaction determines rotation of the receiving frame relative to the sending frame. Equation (7), however, does **not** say that only \(E\) changes \(G\):

\[
\mathring G=SE+ES+[S,Z].
\tag{10}
\]

In an \(S\)-eigenbasis,

\[
\Lambda_{ij}=\frac{2Z_{ij}}{s_i+s_j},\qquad
\mathring G_{ij}=(s_i+s_j)E_{ij}+(s_i-s_j)Z_{ij}.
\tag{11}
\]

Anisotropic stretch therefore couples skew pulses into the response Gram. The clean split holds in a precisely stated rotating frame. By (9),

\[
[S,Z]=\tfrac12[G,\Lambda],
\]

so (10) is equivalently

\[
\dot G-[G,(\Omega+\Omega_-)/2]=SE+ES.
\tag{12}
\]

The commutator is an isospectral rotation: when it acts alone, the eigenvalues of \(G\) stay fixed. For a simple eigenvalue, its instantaneous change is \(2s_iE_{ii}\) in the corresponding principal direction of \(S\). At a repeated eigenvalue, the first-order changes are the eigenvalues of \(2s_iE\) restricted to that eigenspace; the commutator restricts to zero there. The skew part supplies relative frame rotation and its induced rotation of an anisotropic metric. Symmetric off-diagonal terms can also change the metric's principal directions, so “symmetric changes only lengths, skew changes only directions” would be too strong.

At isotropic stretch \(S=\lambda I\), the distinction reduces to

\[
\mathring G=2\lambda E,\qquad \Lambda=Z/\lambda.
\]

This special case supports the intuitive split without an anisotropy correction. Equation (12) is its exact general form, using the average angular velocity rather than silently fixing a frame.

## 4. Why the coactivation tensor rotates

Let \(\mathcal P\) be the fixed coordinatewise multiplication operation expressed in the initial orthonormal coordinates. If the input space is represented only by its declared span, any fixed coordinate algebra can be chosen on that input block: input coordinates are never activated, so its multiplication does not affect the masked network. In frame \(O_\ell\), the operation's coefficient tensor \(T_\ell\) is defined by

\[
\mathcal P_\ell(u,v)=O_\ell^\top\mathcal P(O_\ell u,O_\ell v),
\qquad
\mathcal P_\ell(u,v)_i=\sum_{j,k}T_{\ell,ijk}u_jv_k.
\]

Since \(\dot O_\ell=O_\ell\Omega_\ell\), differentiation gives

\[
\dot T_{ijk}
=-\sum_p\Omega_{ip}T_{pjk}
+\sum_pT_{ipk}\Omega_{pj}
+\sum_pT_{ijp}\Omega_{pk}.
\tag{13}
\]

The output index rotates contragrediently; each input index rotates with its argument. Write \(\mathbf1\) for the algebra unit in the initial coordinates; after metric orthonormalization it need not be the literal all-ones column. The algebra unit and a physical block projector have coordinates

\[
u_\ell=O_\ell^\top\mathbf1,\qquad
P_{j|\ell}=O_\ell^\top\iota_j\pi_jO_\ell,
\]

and obey

\[
\dot u_\ell=-\Omega_\ell u_\ell,
\qquad \dot P_{j|\ell}=[P_{j|\ell},\Omega_\ell].
\tag{14}
\]

These equations change the representation of the same activation algebra and physical blocks. They do not assert that the network learns a new activation function. Their scientific content is the changing alignment of the response metric with the fixed nonlinear operation: a direction that is long in the response metric can point into a different pattern of coordinatewise coactivation or saturation.

For example, let \(a_{\ell-1}\) contain the input and already-computed activations in the preceding frame, with later physical blocks zero. The next shear gives \(b_\ell=S_\ell a_{\ell-1}\). If \(\Phi_{T_\ell}\) denotes exact coordinatewise activation represented by the finite algebra, the masked forward step is

\[
a_\ell=(I-P_{\ell|\ell})b_\ell
+P_{\ell|\ell}\Phi_{T_\ell}(b_\ell).
\tag{15}
\]

Earlier blocks are retained, and only the new target block is activated. The unit is needed when \(\phi(0)\ne0\); masked evaluation must not insert that offset into uncomputed blocks. This formula makes clear why \(G_\ell\), its square root, the tensor, and the masks have distinct roles. The backward and corrected-readout calculations must similarly use the supplied metric runtime, without silently replacing its gates by gradient adjoints.

## 5. Same ordinary stretch, different nonlinear behavior

An elementary example demonstrates what a stretch-only description of an unrestricted map loses. Let

\[
B_1=I_2,\qquad
B_2=\frac1{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix},
\qquad x=e_1,
\]

and choose \(w_1=e_1\), \(w_2=B_2e_1\). Both maps have right stretch \((B_j^\top B_j)^{1/2}=I_2\), and the preactivation/readout pairs have identical pairwise Grams. With coordinatewise \(\phi=\sin\), their readouts are nevertheless

\[
w_1^\top\sin(B_1x)=\sin1,
\qquad
w_2^\top\sin(B_2x)=\sqrt2\sin(1/\sqrt2)>\sin1.
\tag{16}
\]

The inequality follows because \(\sin t/t\) decreases on \((0,1]\): its derivative has numerator \(t\cos t-\sin t\), whose derivative is \(-t\sin t<0\) and whose limit at zero is zero. The readout was rotated together with the map, so the difference comes from the non-equivariance of the nonlinear activation, rather than an unmatched readout direction.

In a polar frame, the missing distinction appears in the rotated multiplication tensor and unit. Ordinary metric-preserving rotations generally do not preserve coordinatewise multiplication. This explains why a stretch-only nonlinear model needs additional orientation information.

There is an essential qualification: (16) is **not** an example of two distinct shears with identical full \(G_\ell\) in the same known preceding frame. Their shear Grams have the same spectra, but different cross-block entries. That distinction matters for the next point.

## 6. Why the full shear Gram is also a re-encoding of the map

In the known source/target physical blocks,

\[
F(B)=\begin{pmatrix}I&0\\B&I\end{pmatrix},
\qquad
F(B)^\top F(B)
=\begin{pmatrix}I+B^\top B&B^\top\\B&I\end{pmatrix}.
\tag{17}
\]

The lower-left block is exactly \(B\). Thus the full shear Gram contains the orientation information that \(B^\top B\) omits. For known \(O_{\ell-1}\),

\[
F_\ell^\top F_\ell=O_{\ell-1}G_\ell O_{\ell-1}^\top
\]

recovers \(B_\ell\) by block projection. Then (1) recovers \(O_\ell\). Starting with \(O_0=I\), all layer maps are therefore recoverable recursively from all the full Grams and the fixed physical decomposition.

Rotated tensors, units, and masks permit the right-hand side to be evaluated without carrying those maps as moving variables. They also avoid repeatedly reconstructing the original chart. That computational representation is different from removing the information in the maps. In this constrained shear family, the extra tensors are compatible geometric coordinates determined by the same underlying maps and initial activation algebra; they are not an independent proof that pairwise data alone were insufficient once the full cross-block Gram was retained.

Only special low-dimensional invariances or an additional approximation could make this an actual information reduction. No such reduction follows from positivity, polar factorization, or polynomial overhead alone. The construction should not be described as meeting a criterion that excludes every invertible re-encoding of a compressed network.

## 7. Candid criteria for scientific transparency

The construction has explanatory value if its presentation does the following:

- Defines the measured response pairing (2), and distinguishes it from sample feature similarities.
- Shows the signed source/receiver pulse identity (8) and the exact symmetric/skew split (9)–(12).
- Connects tensor rotation to the gate/coactivation alignment needed by the nonlinear step (15), without suggesting that the activation itself changes.
- States the recovery formula (17), so the retained transfer information and redundant coordinates are visible.
- Derives actual requested sample/output observables from the state and uses the existing corrected runtime exactly.

At fixed \(D\) and depth, the state is finite. Storing a dense \(T_\ell\) for every stage uses \(O(LD^3)\) moving coefficients; the Grams use \(O(LD^2)\), and naively retaining every block mask in every stage uses \(O(L^2D^2)\). Units and readout/residual coordinates are smaller. Many entries satisfy compatibility constraints. If the declared input span and compressed widths make \(D\) polylogarithmic in dense width, this polynomial enlargement stays polylogarithmic; this is a storage statement, not a new accuracy theorem.

The proved contribution of this audit is the exact response-geometry interpretation, the audited evolution equations, the frame-qualified symmetric/skew mechanism, and the distinction between ordinary stretch and a full shear Gram. The proposed coordinates offer a useful geometric view. They do not, by themselves, eliminate the compressed maps' information, establish a further state reduction, or strengthen an inherited dense-model error bound.
