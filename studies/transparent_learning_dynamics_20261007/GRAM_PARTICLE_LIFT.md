# An exact anchored Gram lift, and why it is not a new particle reduction

This bounded continuation was derived on 2026-10-07 from the supplied compressed
runtime and the author's frozen `RELATIONAL_QUOTIENT.md`. Those are its complete
scientific inputs. No external literature, other study, experiment, or Git
mutation was used. The specified coordinatewise backward gates are preserved;
arbitrary fixed SPD metrics are allowed. This note is a theoretical candidate,
not an independent review or promoted result.

An exact autonomous Gram evolution exists, with rank-one sample-mediated forces
and no additional invertibility assumption. It is useful as an interaction
representation. However, because a complete fixed landmark frame is retained,
the Gram state is globally equivalent to the preceding transfer-response chart.
The dynamic–dynamic similarities are redundant. Calling the transported probe
vectors particles does not make this a further reduction, nor does it satisfy a
strong requirement that no evolving state encode the layer maps.

## 1. Fixed semantic landmarks and multiplication

There are \(m\) training examples with labels \(y\), and finitely many passive
validation inputs fixed at time zero. Their fixed input features are
\(v_a\in\mathbb R^d\). The compressed model has layer widths \(q_\ell\),
metrics \(M_\ell\succ0\), moving first map \(A\), deeper maps \(B_\ell\),
readout \(w\), and residual state \(c\). Its update directions, factors, and
corrected readout are the ones in `RELATIONAL_QUOTIENT.md`.
Throughout, \(\langle x,y\rangle_{M_\ell}=x^\top M_\ell y\).

Here is the necessary fixed construction, recalled explicitly. Let \(U_0\)
be the span of the declared input vectors. Starting with the unit vector in each
layer, \(A(0)U_0\) in layer 1, and \(w(0)\) in the top layer, repeatedly
adjoin coordinatewise products, initial forward images, and initial metric-adjoint
images. Terminate when no span grows. This produces the smallest unital
coordinate-product subspaces \(U_\ell\) containing those seeds and satisfying

\[
B_\ell(0)U_{\ell-1}\subseteq U_\ell,\qquad
B_\ell(0)^*U_\ell\subseteq U_{\ell-1},\qquad
B_\ell(0)^*=M_{\ell-1}^{-1}B_\ell(0)^\top M_\ell.
\]

The construction terminates after at most \(\sum_\ell q_\ell\) strict
dimension increases. Its generated vectors are initial feature patterns,
readout patterns, forward/backward transports, and products of those patterns.
They are not selected hidden-unit directions. Fix orthonormal bases of these
spans, retaining the generated-word provenance:

\[
E_0^\top E_0=I_{r_0},\qquad
E_\ell^\top M_\ell E_\ell=I_{r_\ell},\qquad
\operatorname{range}E_\ell=U_\ell.
\]

The spaces are invariant under the supplied rank-one map updates and their
adjoints. The fixed landmark basis therefore remains valid even if the current
training features, map images, or response patterns change rank. The first note
gives the complete lifting proof of this invariance.

For each layer retain the unit coordinates \(u_i=\langle e_i,\mathbf1\rangle_M\)
and multiplication coefficients

\[
T_{ijk}=\langle e_i,e_j\odot e_k\rangle_M,\qquad
\mathcal P(x,y)_i=\sum_{j,k}T_{ijk}x_jy_k.
\]

Layer superscripts are omitted in this display only. These coefficients obey
\(T_{ijk}=T_{ikj}\); they are not generally symmetric in all indices. Multiplication
is commutative, while the inner-product adjoint is a separate structure.

Define \(\mathsf L_\ell(x)_{ij}=\sum_kT_{ikj}^{(\ell)}x_k\). For
\(\psi=\phi\) or \(\phi'\), define

\[
\Psi_\ell(x)=\psi(\mathsf L_\ell(x))u^{(\ell)}.
\]

This is a finite matrix-function rule. Each \(\mathsf L_\ell(x)\) is
diagonalizable with real spectrum: a polynomial with the distinct coordinates
of \(E_\ell x\) as its simple roots annihilates it. On its distinct spectral
values, use polynomial interpolation of \(\psi\). This yields
\(E_\ell\Psi_\ell(x)=\psi(E_\ell x)\) exactly, including coincident
coordinate values. Write \(\Phi_\ell\) and \(\Phi_\ell'\) for the two
choices; the latter denotes evaluation of scalar \(\phi'\), not a Jacobian.
The first note gives the explicit spectral formula and its numerical-conditioning
qualification. No moving layer matrix is reconstructed by this nonlinear rule.

## 2. Actual vectors represented by the Gram state

For each layer define transported landmark responses

\[
p_j^{(1)}=Ae_j^{(0)},\qquad
p_j^{(\ell)}=B_\ell e_j^{(\ell-1)}\quad(\ell\ge2),
\qquad 1\le j\le r_{\ell-1}.
\]

The interpretation is the preactivation response to a fixed, semantically
generated input pattern at that layer. This is a declared intervention probe,
not a training example or an independently evolving neuron. At the top layer
include the actual readout vector \(w\) as an additional vector.

Let \(X_\ell\) be the matrix whose columns are, in order, the fixed landmarks
\(e_i^{(\ell)}\), the transported responses \(p_j^{(\ell)}\), and, only
when \(\ell=L\), the readout \(w\). Define the moving Gram state

\[
G_\ell=X_\ell^\top M_\ell X_\ell.
\]

Use symbolic index names \(e_i,p_j,w\) for entries of this matrix. Thus
\(G_{\ell;e_i,p_j}=\langle e_i^{(\ell)},p_j^{(\ell)}\rangle_{M_\ell}\),
and its landmark block is the fixed identity. The complete stored moving state
is \((G_1,\ldots,G_L,c)\). No vector coordinates or other map variables are
required for its evaluation. Initial Gram matrices are computed from the original
time-zero compressed maps and readout.

The cloud vectors are well-defined observables of the original state. Nevertheless,
the collection \((p_j)_j\) is also the image of a basis under the layer map;
it encodes the map on the relevant source space. This information content is not
removed by changing the name of the vectors.

## 3. Evaluation using only current Gram entries

Store \(\xi_a=E_0^\top v_a\). Starting with \(\eta_a^{(0)}=\xi_a\),
evaluate

\[
\zeta_{a,i}^{(\ell)}
 =\sum_{j=1}^{r_{\ell-1}}G_{\ell;e_i,p_j}\eta_{a,j}^{(\ell-1)},
\qquad
\eta_a^{(\ell)}=\Phi_\ell(\zeta_a^{(\ell)}).
\]

These are respectively the landmark coefficients of preactivation and activation.
For the readout, set

\[
\rho_i=G_{L;e_i,w},\qquad
C=\frac1{\sqrt m}[\eta_1^{(L)},\ldots,\eta_m^{(L)}],\qquad
\widehat\rho=\rho+C(C^\top C)^{-1}
 \left[\frac{y-c}{\sqrt m}-C^\top\rho\right].
\]

This is precisely the original correction. Its required inverse is the only
inverse of a time-dependent matrix introduced here. The rule is defined on the
same domain as the supplied model; no additional Gram-rank assumption is made.

For training examples compute the backward directions by

\[
\begin{aligned}
d_a^{(L)}&=\mathcal P_L\bigl(\Phi_L'(\zeta_a^{(L)}),\widehat\rho\bigr),\\
k_{a,j}^{(\ell)}&=
 \sum_iG_{\ell+1;p_j,e_i}d_{a,i}^{(\ell+1)},\\
d_a^{(\ell)}&=\mathcal P_\ell\bigl(
 \Phi_\ell'(\zeta_a^{(\ell)}),k_a^{(\ell)}\bigr).
\end{aligned}
\]

The middle equation is the actual pairing
\(\langle p_j^{(\ell+1)},\delta_a^{(\ell+1)}\rangle_{M_{\ell+1}}\).
It represents the metric adjoint; the following multiplication represents the
stipulated coordinate gate. No substitution of a metric-gradient activation
adjoint has been made.

For any cloud-vector index \(s\), define the evaluated similarities

\[
\langle s,h_a^{(\ell)}\rangle
 =\sum_iG_{\ell;s,e_i}\eta_{a,i}^{(\ell)},\qquad
\langle s,\delta_a^{(\ell)}\rangle
 =\sum_iG_{\ell;s,e_i}d_{a,i}^{(\ell)}.
\]

Here brackets abbreviate the actual \(M_\ell\) inner product, not new stored
variables. Feature–feature and response–response pairings are dot products of
their landmark coefficients. Consequently the supplied residual matrix is

\[
\begin{aligned}
K_{ab}={}&\eta_a^{(L)\top}\eta_b^{(L)}
 +(d_a^{(1)\top}d_b^{(1)})(\xi_a^\top\xi_b)\\
&+\sum_{\ell=2}^L(d_a^{(\ell)\top}d_b^{(\ell)})
 (\eta_a^{(\ell-1)\top}\eta_b^{(\ell-1)}).
\end{aligned}
\]

The prediction is \(f_a=\widehat\rho^\top\eta_a^{(L)}\), with
\(f_a=y_a-c_a\) for training examples.

## 4. Rank-one forces and the universal Gram equation

Write \(\gamma=2/m\). The actual vector equations induced by the supplied
map updates are

\[
\dot e_i^{(\ell)}=0,\qquad
\dot p_j^{(\ell)}
 =\gamma\sum_{a=1}^m c_a\,
   \eta_{a,j}^{(\ell-1)}\delta_a^{(\ell)},\qquad
\dot w=\gamma\sum_{a=1}^m c_a h_a^{(L)}.
\]

For the first layer, \(\eta_a^{(0)}=\xi_a\) gives the same formula. A
sample pushes a transported probe along its backward response, weighted by the
sample's overlap with that source probe and its residual. This is a precise
similarity-mediated force statement.

Define a square coefficient matrix \(F_\ell\), indexed by the same cloud
labels as \(G_\ell\), by setting all entries to zero except

\[
(F_\ell)_{p_j,e_i}
 =\gamma\sum_{a=1}^m c_a d_{a,i}^{(\ell)}
   \eta_{a,j}^{(\ell-1)},\qquad
(F_L)_{w,e_i}=\gamma\sum_{a=1}^m c_a\eta_{a,i}^{(L)}.
\]

Every coefficient is determined by current Gram entries, fixed tensors, fixed
inputs, and training labels. In column convention
\(\dot X_\ell=X_\ell F_\ell^\top\). Differentiation gives the closed
system

\[
\dot G_\ell=F_\ell G_\ell+G_\ell F_\ell^\top,\qquad
\dot c=-\gamma Kc.
\]

No \(X_\ell\), \(A\), or \(B_\ell\) is needed during evaluation of
this right-hand side. In particular, no Gram factorization or inverse is used.

The component interactions are equally explicit. Suppressing layer labels and
writing \(\eta_{a,j}^{-}=\eta_{a,j}^{(\ell-1)}\),

\[
\begin{aligned}
\dot G_{e_i,p_j}
 &=\gamma\sum_a c_a d_{a,i}\eta_{a,j}^{-},\\
\dot G_{p_i,p_j}
 &=\gamma\sum_a c_a\left[
 \eta_{a,i}^{-}\langle\delta_a,p_j\rangle
 +\eta_{a,j}^{-}\langle p_i,\delta_a\rangle\right].
\end{aligned}
\]

At the top layer,

\[
\begin{aligned}
\dot G_{e_i,w}&=\gamma\sum_a c_a\eta_{a,i}^{(L)},\\
\dot G_{w,p_j}&=\gamma\sum_a c_a\left[
 \langle h_a^{(L)},p_j\rangle
 +\eta_{a,j}^{(L-1)}\langle w,\delta_a^{(L)}\rangle\right],\\
\dot G_{w,w}&=2\gamma\sum_a c_a\langle w,h_a^{(L)}\rangle.
\end{aligned}
\]

These are metric similarities of declared feature, response, and intervention
objects. They are not isotropic pairwise forces between free particles: the
fixed landmark frame and coactivation tensor participate essentially.

## 5. Exactness, positivity, degeneracies, and costs

Projecting the original vector equations gives the preceding Gram equations.
Conversely, the landmark–transport blocks satisfy exactly the transfer-response
ODE in `RELATIONAL_QUOTIENT.md`, and the landmark–readout block satisfies its
readout ODE. The lift proved there identifies the forward features, supplied
backward directions, correction, residual matrix, and predictions. Thus this
Gram system inherits the same conditional dense-prediction certificate, with
exactly the original norm, horizon, event, and fixed validation set.

Positivity and constant rank can also be checked directly. Write the Gram matrix
in landmark/dynamic block form,

\[
G_\ell=
\begin{pmatrix}I&Z_\ell\\Z_\ell^\top&H_\ell\end{pmatrix},\qquad
F_\ell=
\begin{pmatrix}0&0\\D_\ell&0\end{pmatrix}.
\]

Here \(Z_\ell\) has one column per transported response and, at the top,
one additional column for the readout. The block equations are

\[
\dot Z_\ell=D_\ell^\top,\qquad
\dot H_\ell=D_\ell Z_\ell+Z_\ell^\top D_\ell^\top.
\]

Therefore

\[
\frac{d}{dt}\bigl(H_\ell-Z_\ell^\top Z_\ell\bigr)=0.
\]

Valid initialization has \(H_\ell=Z_\ell^\top Z_\ell\), because every
cloud vector lies in the landmark span. This identity remains exact, so

\[
G_\ell=
\begin{pmatrix}I\\Z_\ell^\top\end{pmatrix}
\begin{pmatrix}I&Z_\ell\end{pmatrix}\succeq0,
\qquad \operatorname{rank}G_\ell=r_\ell.
\]

The moving response cloud may gain or lose rank; the full anchored cloud cannot,
because it contains its fixed basis. No pseudoinverse, generic-rank assumption,
moving-frame division, or restriction on the rank of any \(B_\ell\) is
required. Eigenvalue coincidences in the activation functional calculus are
mathematically regular. The original corrected-readout inverse can still fail;
this lift neither introduces nor repairs that failure.

If all effective widths are bounded by \(q\), and
\(r_0\le\min(d,N)\) for \(N\) declared inputs, storing the symmetric
Gram matrices uses

\[
\sum_{\ell=1}^L
 \frac{s_\ell(s_\ell+1)}2+m,
\qquad
s_\ell=r_\ell+r_{\ell-1}+\mathbf1_{\ell=L}
\]

scalars, including the fixed landmark blocks. The moving Gram storage is
\(O(Lq^2+qr_0+r_0^2+m)\); the fixed multiplication tensors cost
\(O(Lq^3)\), and fixed input coefficients cost \(O(Nr_0)\). The apparent
\(r_0^2\) storage is merely redundant dynamic–dynamic similarity storage in
the first layer and can be omitted if a minimal chart is desired. Evaluation
has polynomial arithmetic cost; using block sparsity avoids a generic dense
matrix multiplication for the Gram equation. Precision-uniform stability of
spectral activation evaluation is not claimed.

Only training indices occur in forces, correction, and residual dynamics.
Validation labels are absent. Enlarging the initial landmark construction to
include additional fixed validation inputs changes the representation, not the
underlying training trajectory: both Gram systems lift to the same original
initial-value problem. Validation is therefore passive in the exact sense.

## 6. Candid assessment of the particle interpretation

The gain is an explicit observable interaction law. One can inspect which
training residual changes a similarity and factor its contribution into forward
overlap, backward overlap, and the coactivation operation. Nonlinear orientation
is carried by a declared fixed algebra. Adjoint geometry is carried by inner
products. Those are substantive explanatory separations.

The stronger reduction claim fails for this lift. From \(G_\ell\), read off
\(Z_\ell\) directly. Its transport columns are exactly

\[
(Z_1)_{ij}=\langle e_i^{(1)},Ae_j^{(0)}\rangle_{M_1},\qquad
(Z_\ell)_{ij}=\langle e_i^{(\ell)},B_\ell e_j^{(\ell-1)}\rangle_{M_\ell}.
\]

Its final readout column is \(\rho\). Conversely these blocks reconstruct
every valid Gram entry by \(H_\ell=Z_\ell^\top Z_\ell\). The maps
between this Gram manifold and the preceding transfer-response chart are global
polynomial inverses. The Gram description is therefore a redundant embedding
of exactly that chart, not a further quotient.

Moreover, neither forward evaluation, backward evaluation, readout correction,
nor the force coefficients require the dynamic–dynamic block \(H_\ell\).
Those similarities have no independent feedback into the dynamics. Even an
inconsistent initialization with \(H_\ell-Z_\ell^\top Z_\ell\ne0\)
would carry that discrepancy as a constant unused block, rather than repair it
through a new physical mechanism. This is a particularly direct test of how
much the particle language adds.

The full-rank case is not rare in an algebraic sense. If any seed in a layer has
\(q_\ell\) distinct coordinate values, its powers from degree zero through
\(q_\ell-1\) span the full coordinate space: their evaluation matrix is a
Vandermonde matrix with determinant
\(\prod_{i<j}(z_j-z_i)\ne0\). Thus one sufficiently separating initial
pattern already makes \(U_\ell=\mathbb R^{q_\ell}\). In that case the
landmark–transport pairings contain the full corresponding layer map in another
basis. The Gram format does not conceal this fact mathematically, and should not
conceal it in scientific presentation.

Dropping the spanning landmarks would remove this direct recoding, but then the
fixed coactivation algebra can no longer be applied to a generic vector from its
pairwise similarities alone. The three-coordinate tanh counterexample in the
first note demonstrates the lost orientation information. That is an obstruction
to this simplest unanchored proposal, not a no-go theorem for all possible richer
relational models.

Accordingly, the bounded route succeeds at an exact, restartable, algebra-enriched
Gram realization and a transparent rank-one force identity. It does not establish
a genuinely new particle reduction under a criterion that excludes transformed
map state. Obtaining such a reduction would require a further structural theorem:
either fewer relational observables must determine the relevant future without
recovering the transfer chart, or an approximation must control the effect of
discarding that chart information. Neither implication is proved here.
