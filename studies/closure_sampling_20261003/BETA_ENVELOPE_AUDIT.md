# What the beta envelope measures, and what Gaussian normalization controls

2026-10-04. Scoped audit within the existing architecture-constant investigation.
This note audits the seven inputs listed at the end, and proves the elementary
Gaussian identities and counterexamples below. It does not import their linked
prerequisites, read other studies, change the model, or establish a new all-time
compression theorem. Its new calculations await separate reconstruction.

The central distinction is that the source's beta is an envelope for analytic
norms and numerical proof constants. It is not the gain of an independent
Gaussian matrix on a given vector. Conditions
\(\mathbb E\phi(Z)^2=\mathbb E\phi'(Z)^2=1\), for \(Z\sim N(0,1)\),
do control certain initialized mean-square recurrences. They do not permit
substituting one for beta in the proved source or runtime inequalities.

## 1. Exact provenance of the lower bounds on beta

The current definition in `ARCHITECTURE_CONSTANT_REFINEMENT.md`, equations
(1)--(1a), is
\[
B=\max(1,B_\phi),\qquad
\beta=\max\{10,B,s,t_\phi,16/a\}.
\tag{1}
\]
Here \(a>0\) is a common complex strip width, \(B_\phi\) bounds activation
values on that strip, and \(s,t_\phi\ge1\) bound the first two derivatives
on its inner half. The optional Cauchy choices are \(s=4B/a\) and
\(t_\phi=32B/a^2\), with the other entries of the maximum already at least
one. The source files use \(t\) for the curvature bound; this note writes
\(t_\phi\) to distinguish it from physical training time.

The original source route, equation (1), had a floor eight and operator
caps three/four. Its Section 7 explicitly supersedes these with the common
initialized, real, and complex caps eight, nine, and ten. Its equations
(24), (30), and (38)--(42), and the rescaled-label route, equations (3),
(7), and (27), then use ten as a deterministic propagation coefficient.
For example, the latter route has
\[
K_\ell=2B(10s)^{L-\ell},\qquad
P_1=2,\qquad P_\ell=B+10sP_{\ell-1}+1.
\tag{2}
\]
The simplifications \(10s\le\beta^2\) and
\(L\le\beta^{L-1}\) absorb these products and sums into powers of beta.
The same floor absorbs factors such as 16, 32, 128, 4000 and
\(64e^2L\) by spending further powers; it does not assert an exact
tenfold gain in the network.

The analytic entry has a separate origin. The reconciled source equation
(32), repeated as equation (31) of the rescaled-label route, is
\[
c=\min\left\{\frac1{8d},
 \frac{a}{32[4U_*+(d-1)V_*]}\right\},\qquad
r_n=\frac{c}{\sqrt{\log(en)}}.
\tag{3}
\]
The coordinate response coefficients \(U_*,V_*\) bound the displacement
of complex preactivations. This choice keeps that displacement below
\(a/32\). Thus
\[
c^{-1}=\max\left\{8d,
 \frac{32}{a}[4U_*+(d-1)V_*]\right\}.
\tag{4}
\]
The condition \(\beta\ge16/a\) provides \(a^{-1}\le\beta/16\)
when converting (4) to a power of beta. The refined anisotropic time and
angular radii in the architecture note retain the same dependence on
the actual strip width. This dependence multiplies the coefficient
count; it cannot be discarded into a larger width threshold.

There is a useful exact redundancy: with the generic Cauchy choice,
\[
\max\{10,32B/a^2\}\ge\frac{\sqrt{320B}}a>\frac{16}a.
\tag{5}
\]
Consequently deleting the explicit entry \(16/a\) from that particular
maximum changes no value of beta. With separately certified derivative
bounds, as used for tanh, the entry can dominate and is no longer
redundant. For the stated tanh certificate
\((a,B,s,t_\phi)=(1,2,2,4)\), it is precisely what gives beta 16.

Simply setting beta to one would falsify the displayed envelopes before
any probability argument: \(P_1=2\), \(K_L=2B\), and
\(K_{\rm src}=32\max(1,\max K_\ell,\max sK_\ell)\) are already
larger than one. The rescaled carrier budget \(64e^2L\) is larger than
one too. In the runtime proof the genuine conditions
\(224FU(Y/\lambda)^2\le1\) and \(6J_0Y/\lambda\le1\) would
not follow from \(Y/\lambda\le1\). These are failures of the proposed
substitution in the proof, not lower bounds on the best possible theorem.
One may retain universal numerical factors explicitly rather than hide
them in beta, but that gives different formulas, not the old formulas
with beta replaced by one.

## 2. Four different kinds of gain

The proof contains four distinct objects.

* Universal constants account for stopped tubes, metric comparisons,
  triangle inequalities, tail probabilities, and finite sums.
* Deterministic layer factors bound arbitrary directions: examples are
  \(10s\) in (2), and \(9g\), with \(g=2B_{\rm rt}\), in
  `DEPTH_CONSTANT_SEPARATION.md`. The factor two in the latter arises
  from \(D/4\preceq H\preceq D\): a diagonal multiplier in the
  selected-neuron metric can cost twice its coordinate supremum.
* Analytic radius depends on values off the real axis and on \(a^{-1}\)
  as in (3)--(4).
* An independent Gaussian mixer has unit mean-square gain on any given
  vector independent of that mixer.

For the last assertion, if \(W_{ij}\) are independent \(N(0,1/n)\)
and \(q\in\mathbb R^n\) is independent of \(W\), then, conditionally
on \(q\ne0\),
\[
\frac{\|Wq\|_{2,n}^2}{\|q\|_{2,n}^2}
 \mathrel{\overset{d}=}\frac{\chi_n^2}{n},\qquad
\mathbb E[\|Wq\|_{2,n}^2\mid q]=\|q\|_{2,n}^2,
\quad \|u\|_{2,n}=\frac{\|u\|_2}{\sqrt n}.
\tag{6}
\]
For \(q=0\) the identity of norms is exact. Equation (6) follows by
computing the variance of each independent Gaussian row pairing.

It is not an operator-norm identity. An elementary way to see the
difference avoids any limiting spectral theorem. Let \(r_j\) be row
\(j\) of \(W\), and choose the matrix-dependent unit vector
\(q=r_1/\|r_1\|_2\). Then
\[
\|Wq\|_2^2=\|r_1\|_2^2+
 \sum_{j=2}^n\frac{(r_j^\top r_1)^2}{\|r_1\|_2^2}
 \longrightarrow2
\tag{7}
\]
in probability: the first term has law \(\chi_n^2/n\), and
conditionally on \(r_1\), the second has law \(\chi_{n-1}^2/n\).
Thus an operator cap arbitrarily close to one cannot replace the
independent-vector statement, even at initialization.

The source's forward derivative operators allow arbitrary parameter
directions. Its backward responses reuse the matrices through subsequent
gates. The runtime compares adaptive states in a non-diagonal metric.
Equation (6) alone changes none of these deterministic bounds. The
completed runtime improvement already separates the initialized mixer
cap eight from the larger source coefficient \(K\); it does not convert
the resulting tube nine to a unit Gaussian gain.

## 3. What the two Gaussian normalization equations do imply

Suppose \(\mathbb E\phi(Z)^2=\mathbb E\phi'(Z)^2=1\), for a
standard real Gaussian \(Z\). In the limiting initialized covariance
recursion, a unit input gives \(Q_{aa}^{(0)}=1\). Applying the first
identity successively gives \(Q_{aa}^{(\ell)}=1\) at every layer.
In particular the top covariance has trace \(m\), so its minimum
eigenvalue \(\gamma\) is at most one. Thus
\(\lambda=\min(1,\gamma/m)=\gamma/m\). This removes the
generic conversion loss using \(\gamma\le B^2\), without bounding
the analytic norm \(B\) itself by one.

For a tangent, the covariance with the preactivation matters. Let
\((Z,J)\) be a centered jointly Gaussian pair with
\(\mathbb EZ^2=1\), \(v=\mathbb EJ^2\), and
\(c=\mathbb EZJ\). A separate standard Gaussian \(U\) gives the
representation \(J=cZ+\sqrt{v-c^2}\,U\). Therefore
\[
\mathbb E[\phi'(Z)^2J^2]
 =v+c^2\{\mathbb E[Z^2\phi'(Z)^2]-1\}.
\tag{8}
\]
The cross term vanishes by independence and \(\mathbb EU=0\).
When \(c=0\), (8) is exactly the unit mean-square gate recurrence.
For sphere tangents at the first layer, the conditions
\(\|v_0\|=\|u\|=1\) and \(v_0^\top u=0\) make
\(A_iv_0\) and \(A_iu\) independent standard Gaussians. Thus the
unit gate recurrence is exact there. The independent mixer step then
has (6). Extending this observation uniformly over layers, queries,
and training requires the corresponding joint-law and concentration
arguments; it is not a consequence of the two scalar moments alone.

Even a Gaussian correlated direction can violate unit gain. For any
\(\omega>0\), define
\[
A_\omega^2=\frac{2}{\omega^2(1-e^{-2\omega^2})},\quad
\mu_\omega^2=1-\frac{\tanh(\omega^2/2)}{\omega^2},\quad
\phi_\omega(x)=\mu_\omega+
 A_\omega[\cos(\omega x)-e^{-\omega^2/2}],
\tag{9}
\]
using the positive square roots. The mean-square centered cosine term
is \(\tanh(\omega^2/2)/\omega^2<1/2\), so the definition is real.
The Gaussian characteristic function gives
\(\mathbb E\cos(bZ)=e^{-b^2/2}\) and, by differentiating its
absolutely integrable defining integral twice,
\(\mathbb E[Z^2\cos(bZ)]=(1-b^2)e^{-b^2/2}\).
Using \(\sin^2 x=(1-\cos2x)/2\) now gives exactly
\[
\mathbb E\phi_\omega(Z)^2=
\mathbb E\phi_\omega'(Z)^2=1,\qquad
\mathbb E[Z^2\phi_\omega'(Z)^2]
 =1+\frac{4\omega^2}{e^{2\omega^2}-1}>1.
\tag{10}
\]
This bounded entire activation therefore expands the normalized
Gaussian direction \(J=Z\). This is a radial direction, so it does
not refute a theorem restricted to tangents of the unit sphere.

## 4. The precise higher mixed moment missing during training

For the actual evolving network write
\(J^{(\ell)}(t,v,u)=D_vz^{(\ell)}(t,v)[u]\). Differentiating
the exact layer recursion, with the gates evaluated at layer \(\ell-1\),
gives
\[
\dot J^{(\ell)}
 =\dot W^{(\ell)}[\phi'J^{(\ell-1)}]
  +W^{(\ell)}[\phi''\dot z^{(\ell-1)}J^{(\ell-1)}]
  +W^{(\ell)}[\phi'\dot J^{(\ell-1)}].
\tag{11}
\]
In the study's mobility coordinates
\(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\), put
\(F_a=nf_a\) and define the residual-free response
\(R_a^{(\ell)}=D_\Theta z^{(\ell)}\nabla_\Theta F_a\).
For residuals \(r_a=f_a-y_a\) and mean squared loss,
\(\dot z^{(\ell)}=-(2/m)\sum_a r_aR_a^{(\ell)}\).
The middle term of (11) consequently requires the actual mixed norm
\[
\sup_{t,v,u,a}
 \|\phi''(z^{(\ell)})\odot
                 R_a^{(\ell)}\odot J^{(\ell)}\|_{2,n}.
\tag{12}
\]
Using the curvature supremum reduces it to
\(t_\phi\|R_a^{(\ell)}\odot J^{(\ell)}\|_{2,n}\).
Separate second moments do not control this product. One sufficient
bound is
\[
\|R\odot J\|_{2,n}\le\|R\|_{4,n}\|J\|_{4,n},
\tag{13}
\]
which is Cauchy--Schwarz applied to \(n^{-1}\sum_iR_i^2J_i^2\).
The corresponding adaptive fourth or joint moments, with an acceptable
depth recurrence, have not been supplied by the two normalization
equations. Curvature terms in the source Hessian,
\(Dz^\top\operatorname{diag}(\phi''k)Dz\), have the same issue.
Moreover training reuses the matrix rows, so lower-layer conditioning
alone no longer proves (6) for the actual responses.

This missing implication already has a bounded analytic counterexample.
For any real \(k\ge2\), define
\[
\psi_k(x)=(1+4k^2)^{1/4}\int_0^x e^{-k^2t^2}\,dt,
\qquad
\phi_k(x)=\sqrt{1-\mathbb E\psi_k(Z)^2}+\psi_k(x).
\tag{14}
\]
The integral denotes its entire primitive. Oddness gives
\(\mathbb E\psi_k(Z)=0\). On the real line,
\[
\|\psi_k\|_\infty^2
 \le\frac{\pi\sqrt{1+4k^2}}{4k^2}
 \le\frac{\pi\sqrt{17}}{16}<1,
\tag{15}
\]
where the middle expression decreases for positive \(k\), and its
value at two gives the last bound. Thus the square root in (14) is
well defined. On any strip \(|\operatorname{Im}z|<a\), integrate
first along the real axis and then vertically to get
\[
|\psi_k(x+iy)|\le(1+4k^2)^{1/4}
 \left(\frac{\sqrt\pi}{2k}+a e^{k^2a^2}\right).
\tag{16}
\]
Each \(\phi_k\) is therefore real on the real axis, holomorphic,
and bounded on every finite horizontal strip, as required by the
activation class. This is not a family with fixed analytic norm and
strip width simultaneously; the point is that the two moments do not
bound those quantities.

Completing the square in the Gaussian density gives
\(\mathbb E e^{-bZ^2}=(1+2b)^{-1/2}\) for \(b\ge0\).
Differentiating this integrable expression gives
\(\mathbb E[Z^2e^{-bZ^2}]=(1+2b)^{-3/2}\).
Since
\(\phi_k'(x)=(1+4k^2)^{1/4}e^{-k^2x^2}\), substitution yields
\[
\begin{aligned}
\mathbb E\phi_k(Z)^2&=1,&
\mathbb E\phi_k'(Z)^2&=1,\\
\mathbb E\phi_k'(Z)^4
 &=\frac{1+4k^2}{\sqrt{1+8k^2}}\longrightarrow\infty,&
\mathbb E\phi_k''(Z)^2
 &=\frac{4k^4}{1+4k^2}\longrightarrow\infty.
\end{aligned}
\tag{17}
\]
For independent standard \(Z,U\), the actual initialized first-layer
angular activation tangent is \(Q=\phi_k'(Z)U\). Therefore
\[
\mathbb EQ^2=1,\qquad
\mathbb EQ^4=3\frac{1+4k^2}{\sqrt{1+8k^2}}\longrightarrow\infty.
\tag{18}
\]
Thus even a genuine initialized tangent with unit second moment has no
fourth-moment bound uniform over this normalized activation class. Taking
the two factors in (13) equal to that tangent makes the product RMS
unbounded across the class. This demonstrates the logical insufficiency
of the proposed scalar assumptions; it does not identify those equal
factors with the actual training response in (12), nor prove that its
all-time depth dependence must be exponential.

## 5. Consequence for the current theorem

The Gaussian normalizations can sharpen the initialized variance and
orthogonal-tangent calculations, and make the capped gap exact. They
leave the existing deterministic source Hessian, complex radius, adaptive
mixed responses, and selected-metric runtime bounds unresolved. A
smaller all-time coefficient would require new estimates for those
objects and a new assembly of the explicit label and radius conditions.
The already derived power envelopes remain valid; this audit supplies
no justification for replacing their beta by one.

## Inputs and check status

Complete sources read, with their SHA-256 values at audit time:

| Source | SHA-256 |
| --- | --- |
| `ARCHITECTURE_CONSTANT_REFINEMENT.md` | `b33f8b2ebb04eba386f59f125fd4d8f22ff3273bc094f64808db865dd27caba7` |
| `EXPLICIT_ARCHITECTURE_CONSTANTS.md` | `19a307c4c8d9325605b0a88099dce8668baf1f61e3bf7088bc5ba36deee3c64d` |
| `EXPLICIT_SOURCE_CONSTANTS_ROUTE.md` | `d4a1bf4bd247d1b93909d4ee001da74c4c6f4573021370800f9c152dae05ab6a` |
| `LABEL_DEPTH_RESCALING_ROUTE.md` | `d06ceea6598bf3f86e0843682c5600365ef01b4b80eaad6544ceec1a9d4ec1f1` |
| `DEPTH_CONSTANT_SEPARATION.md` | `6e23f2eb95b1979e7be722f76bafb43ee239f83cc5175d58d17a0f9e73fcb17f` |
| `EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md` | `775ed6756af7de018c961173b850ad69930a71e4273c669bfe71c93182987bcd` |
| `NONEXPANSIVE_INITIAL_QUERY_ROUTE.md` | `0f705c36cf297f086ee6eedecfcf4e99f467bf73fdc5ccad79ea7e6f476a3da9` |

Applied canonical notation and its neural reference, rigorous proof
instructions, and the shared workflow. The audit derived (5)--(18)
directly, with no external theorem or numerical experiment. No new
scientific route was received from another agent before this file was
frozen. The original sources' inherited insertion dependencies were not
re-audited; this file checks the stated constant uses and the normalization
implications only. No Git or maintained-book mutation was made.
