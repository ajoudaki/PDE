# Geometry and fitting in the selected fixed-order population results

This is a source-backed assembly of the older results explicitly selected for
`book_promotion_20261010`. It preserves complete proof sources in
`older_theory_sources.tar.gz`; `older_sources.json` records the original paths,
exact line ranges where excerpted, source-file hashes, and archived-byte hashes.
The exposition below states the selected conclusions and their assumptions,
then identifies the proof chain. It is not a new independent mathematical
review, a promotion decision, or a proof that these closures describe dense
networks for all training times.

The common question is which aspects of feature geometry permit fitting, and
which conclusions about training actually follow. The answer has several
distinct parts. The selected landscape results exclude suboptimal local minima
in stated population spaces. The initialized-feature result shows that fitting
finite labels does not determine a predictor away from the training inputs.
The three-input construction shows that a rank-one upper-feature Gram can
coexist with full trainability through the lower layer. The dynamical results
prove fitting on exact symmetry families and exhibit an initialized positive
plateau that attains an architectural loss floor. These claims concern related
objects, but none supplies a missing implication for a different model.

## 1. Common model, exact initialization, and conventions

Let the data be a finite probability law
\(\mu=\sum_{a=1}^m\mu_a\delta_{(x_a,y_a)}\), with
\(\mu_a>0\), \(\sum_a\mu_a=1\), and
\(u_a=x_a/\sqrt d\in S^{d-1}\). Labels are real unless a result below
specifies binary or opposite labels. The activation is \(\phi=\tanh\).
The closure has two fixed probability spaces, with expectations
\(\mathbb E_1,\mathbb E_2\), and bounded feature columns
\(b_1\in\mathbb R^{K_1}\), \(b_2\in\mathbb R^{K_2}\).
Its moving variables are a lower field
\(w\in L^2(\Omega_1;\mathbb R^d)\), an upper readout
\(c\in L^2(\Omega_2)\), and a full matrix
\(M\in\mathbb R^{K_2\times K_1}\). Define

\[
\begin{aligned}
a_a&=\mathbb E_1[b_1\phi(w\cdot u_a)],&
v_a&=Ma_a,& Z_a^{(2)}&=b_2^\top v_a,\\
H_a^{(2)}&=\phi(Z_a^{(2)}),&
f_a&=\mathbb E_2[cH_a^{(2)}],&r_a&=f_a-y_a,\\
d_a&=\mathbb E_2[b_2c\phi'(Z_a^{(2)})],&&
\mathcal L&=\sum_a\mu_a r_a^2.
\end{aligned}
\]

Here \(d_a\) is an upper coefficient vector, not input dimension. The
physical metric is
\(\|\delta w\|_2^2+\|\delta c\|_2^2+\|\delta M\|_F^2\).
The exact gradient flow is

\[
\begin{aligned}
\dot w&=-2\sum_a\mu_ar_a\phi'(w\cdot u_a)
                   (b_1^\top M^\top d_a)u_a,\\
\dot c&=-2\sum_a\mu_ar_aH_a^{(2)},&
\dot M&=-2\sum_a\mu_ar_a d_a a_a^\top,\\
\dot{\mathcal L}&=-\|\dot w\|_2^2-\|\dot c\|_2^2-\|\dot M\|_F^2.
\end{aligned}
\]

The reverse action is the actual transpose of this same matrix. The loss is
unhalved; every time rate below uses these factors. The saved state may
equivalently be the complete joint laws
\(\operatorname{Law}(b_1,g,w)\), \(\operatorname{Law}(b_2,c)\), together
with \(M\). Separate marginal laws would discard necessary correlations.
At fixed order, bounded marks and bounded activation derivatives give local
existence and uniqueness in bounded \(w-g,c\) and finite \(M\); the energy
and polynomial finite-time bounds in the archived current-book excerpts
continue the initialized flow through every finite time. Those bounds alone
give no all-time compactness or fitting theorem.

For canonical order \(p=1\) and any dimension used below, take independent
standard Gaussian lower coordinates \(g_i,\zeta_i^0\), and separate
independent standard Gaussian upper coordinates \(\widetilde g_i\). Put

\[
\begin{gathered}
\nu=\mathbb E\phi(G)^2,\quad
\tau=\mathbb E\phi(\sqrt\nu G)^2,\quad \alpha=1-\tau,\\
h_i=\phi(g_i),\quad R_i=\sqrt\tau\zeta_i^0+\alpha h_i,
\quad k_i=\phi(R_i),\quad B_i=\phi(\sqrt\nu\widetilde g_i),\\
\beta=\mathbb E[h_i k_i],\quad s=\mathbb E k_i^2,\quad
\gamma=1-s,\quad \eta=1/4096,\\
\ell_h=\sqrt{\nu+\eta},\quad
\ell_k=\sqrt{s+\eta-\beta^2/(\nu+\eta)},\quad
\ell_2=\sqrt{\tau+\eta}.
\end{gathered}
\]

All normalization denominators are positive. In the odd invariant sector,

\[
b_1=\left(h/\ell_h,
       \{k-\beta h/(\nu+\eta)\}/\ell_k\right),\quad
b_2=B/\ell_2,
\]
\[
D=\left(d_h I_d\ \ d_k I_d\right),\qquad
d_h=\frac{\alpha\nu}{\ell_h\ell_2},\quad
d_k=\frac{\alpha\beta\eta/(\nu+\eta)+\tau\gamma}
          {\ell_k\ell_2},\qquad (w,c,M)_0=(g,0,D).
\]

In particular \(R_i\) is correlated with \(g_i\); the response term
\(\tau\gamma\) is retained. The full feature lists also have a constant
coordinate. Canonical simultaneous mark-negation makes \(w,c\) odd and
keeps the constant row and column of \(M\) inactive. Removing those
coordinates gives \((K_1,K_2)=(2d,d)\) without restricting any remaining
matrix entry. This removal applies only in that sector. The higher-order
ambient theorem below retains all constant and polynomial coordinates.

For \(d=2\) and \(p=2,3\), the full canonical lists are all Chebyshev
products of total degree at most \(p\) in
\(X_1=(h_1,h_2,k_1,k_2)\) and \(X_2=(B_1,B_2)\).
The initialized-word prefixes add no new bounded feature at these orders.
Their dimensions are \((15,6)\) and \((35,10)\), respectively. If
\(\psi_\ell\) denotes its raw list, the definition is

\[
L_\ell L_\ell^\top=\mathbb E_\ell[\psi_\ell\psi_\ell^\top]
                         +\eta_p I,
\quad b_\ell=L_\ell^{-1}\psi_\ell,
\quad\eta_p=[1024(p+1)^2]^{-1},\quad D=L_2^{-1}CL_1^{-\top}.
\]

The raw contraction \(C\) is specified without an evolving Gaussian action:
for a lower polynomial feature \(F(X_1)\) and an upper feature \(Q(X_2)\),

\[
\mathbb E_2[Q A_0F]
=\sum_{i=1}^2\mathbb E_1[Fh_i]\mathbb E_2[\partial_{\xi_i}Q]
 +\sum_{i=1}^2\mathbb E_1[\partial_{\zeta_i}F]\mathbb E_2[QB_i],
\]

where \(\xi_i=\sqrt\nu\widetilde g_i\),
\(\zeta_i=\sqrt\tau\zeta_i^0\); apply this entrywise to the raw
lists. The archive includes this complete canonical definition and its
finite Gaussian contraction derivation. No theorem about a neural-width or
closure-order limit is needed to define the fixed-order objects here.

The historical sources use \(L\) for loss, \(z_a\) or \(v_a\) for the
finite upper code, and \(H_a\) or \(h_a^2\) for the upper activation.
Here these are \(\mathcal L\), \(v_a\), and \(H_a^{(2)}\), respectively;
a source superscript 2 denoting layer is never a square. Closure order
\(p\) is distinct from width, sample count, and a numerical integration
count.

## 2. Architectural loss floor and the selected landscape theorems

Every represented predictor is odd in input: \(f(-x)=-f(x)\). Group
observations modulo sign, choose one representative \(x_g\) per group,
and write \(x_a=\epsilon_a x_g\), \(\epsilon_a\in\{-1,1\}\). Define

\[
\pi_g=\sum_{a\in g}\mu_a,\qquad
\bar y_g=\pi_g^{-1}\sum_{a\in g}\mu_a\epsilon_a y_a,\qquad
\mathcal L_{\rm arch}=\sum_g\sum_{a\in g}
                   \mu_a(\epsilon_a y_a-\bar y_g)^2.
\]

Expanding the squares gives the exact statewise identity

\[
\mathcal L=\mathcal L_{\rm arch}
              +\sum_g\pi_g\{f(x_g)-\bar y_g\}^2.
\]

The two selected landscape conclusions are:

* **Order one, arbitrary finite sphere data.** For \(d\ge2\), the exact
  canonical odd population space of arbitrary odd \(L^2\) fields \(w,c\)
  and arbitrary finite \(M\in\mathbb R^{d\times2d}\) has no suboptimal
  local minimum in the physical product norm. Every local minimum attains
  \(\mathcal L_{\rm arch}\), and that floor is attained. There is no
  sample-count, input-linear-independence, bounded-displacement, or matrix-rank
  restriction. For inputs distinct modulo sign, the floor is zero.
* **Orders two and three, arbitrary finite circle data.** For \(d=2\), the
  same conclusion holds on the full canonical population space with all
  polynomial coordinates, arbitrary \(L^2\) fields, and arbitrary full
  \(M\). It covers every finite sample count and finite real labels.
  The same polynomial proof also covers the full order-one dictionary in
  \(d=2\). No higher-order all-dictionary theorem is asserted.

The first proof is complete in `no_bad_local_minima.md`, §§1–8; the second
in `p2_p3_unrestricted_theorem.md`, §§1–7. Both use changes of \(w\) on
arbitrarily small population sets. At a local minimum, oddness of the
input ridge functions and matrix stationarity force the samplewise condition
\(r_aM^\top d_a=0\). An exactly prediction-preserving change of \(c\)
orthogonal to the current upper-feature span then forces a derivative
feature into that span if a residual is nonzero. At order one, a linear
factor times \(\operatorname{sech}^2\) cannot lie in a finite tanh-ridge
span. At orders two and three, the relevant space is the polynomial image
\(\{b_2^\top Mv:v\in\mathbb R^{K_1}\}\) of the **current** matrix;
double complex poles exclude the required inclusion for a nonconstant
image. Constant and zero images are treated separately by flat-state
perturbations. The proofs include exact interpolation and the signed-group
reduction above; they require neither independently trainable sample
moments nor a nonsingular current feature Gram.

The population topology matters: the small-set variations are unavailable
in this form for a fixed finite particle population. A landscape theorem
does not prove initialized GF convergence, stochastic escape, a rate, or
avoidance of saddles. The order-one source also proves the limited exact-GF
corollary that no neighborhood of a suboptimal equilibrium is entirely in
that equilibrium's point basin: every neighborhood contains a state of
strictly lower loss, whose decreasing loss prevents convergence to the
higher-loss point. This is neither a basin-measure theorem nor a stochastic
statement. A universal negative leading Taylor coefficient along one fixed
straight direction is a stronger, separate assertion and is not part of
either selected landscape theorem.

## 3. Canonical initialized features and predictor nonuniqueness

For \(d=2,p=1\), keep \(w=g,M=D\). The complete correlated coefficient
calculation in `CANONICAL_FEATURES.md`, §§1–2, gives

\[
H_0^{(2)}(u)=\tanh\{B_1F(u_1)+B_2F(u_2)\},\qquad u\in S^1,
\]

where \(F:[-1,1]\to\mathbb R\) is odd and strictly increasing. Its
explicit definition uses the preceding constants. Let

\[
(A,B_*)=(\alpha\nu,\alpha\beta+\tau\gamma)
       \begin{pmatrix}\nu+\eta&\beta\\\beta&s+\eta\end{pmatrix}^{-1},
\quad j(g)=A\tanh g+B_*\mathbb E_\zeta\tanh(\zeta+\alpha\tanh g),
\]
\[
F(t)=\frac{1}{\tau+\eta}\mathbb E\!\left[
 j(G)\tanh(tG+\sqrt{1-t^2}V)\right],
\]

with independent standard \(G,V\) and \(\zeta\sim N(0,\tau)\).
The proof establishes positivity of the **combined** derivative \(j'\);
it does not assume \(A\ge0\). Gaussian integration by parts gives
\(F'(t)=(\tau+\eta)^{-1}\mathbb E[j'(G)\phi'(tG+
\sqrt{1-t^2}V)]>0\) in the interior, and continuity treats the endpoints.
Sources using the normalized upper mark \(b_2=B/\ell_2\) instead write
\(Da_0(u)=(T(u_1),T(u_2))\); the exact conversion is
\(T=\ell_2F\). These are the same preactivation, not two initializations.

For every finite set \(u_1,\ldots,u_m\) distinct modulo sign,
the fields \(H_a=H_0^{(2)}(u_a)\) are linearly independent in upper
population \(L^2\). Thus \(K_{ab}=\mathbb E_2[H_aH_b]\) is positive
definite, as is its congruence by any positive weight diagonal matrix.
The statement still holds after adjoining any
\(u_*\notin\{\pm u_1,\ldots,\pm u_m\}\), regardless of finite \(m\).

Here is the explicit resulting freedom in the represented predictor. Put
\(H_*=H_0^{(2)}(u_*)\), \(k_a=\mathbb E_2[H_aH_*]\), and

\[
c_{\rm base}=\sum_a(K^{-1}y)_aH_a,\quad
R_*=H_*-\sum_a(K^{-1}k)_aH_a,\quad
\kappa_*=\|R_*\|_2^2>0.
\]
For every prescribed real query value \(z\), the bounded odd readout

\[
c_z=c_{\rm base}+\frac{z-k^\top K^{-1}y}{\kappa_*}R_*
\]

fits all training labels and predicts exactly \(z\) at \(u_*\), with
the same initialized hidden parameters. Every fitting readout is
\(c_{\rm base}+r\) with \(r\perp\operatorname{span}\{H_a\}\), and
\(c_{\rm base}\) is uniquely of minimum \(L^2\) norm. The full proof of
finite-family independence and the construction is in §§3–4 of the source:
positive upper density turns an almost-sure relation into an identity on
an open square, a generic line produces distinct tanh scales, and their
exponential tails are independent.

This is representational nonuniqueness. These readouts are constructed
states, not multiple solutions or identified endpoints of the prescribed
gradient flow. No modified selector or optimizer is assembled. Positive
definiteness for each finite set gives no uniform conditioning near input
collisions, and a finite upper quadrature has a separate finite-rank bound.

## 4. Lower-layer trainability despite complete classwise upper collapse

Fix three pairwise nonparallel directions in \(S^1\). In the canonical
odd class with \(w-g\in L^\infty\), bounded \(c\), and finite full
\(M\), the differential of
\(w\mapsto(a_1,a_2,a_3)\in\mathbb R^{4\times3}\) is onto, using
bounded odd perturbations. Its derivative is

\[
J_w\delta w=
\left(\mathbb E_1[b_1\phi'(w\cdot u_a)(u_a\cdot\delta w)]\right)_{a=1}^3.
\]

`stationary_geometry.md`, Lemma 2, proves that \(J_w^*\) has trivial
kernel. Positive lower-mark density near zero forces any candidate kernel
linear forms to be proportional. The resulting constant gate ratios would
bound \(\big||g\cdot u_i|-|g\cdot u_j|\big|\), contradicting the
Gaussian tails for distinct directions modulo sign. The right inverse
\(J_w^*(J_wJ_w^*)^{-1}\) is bounded and odd. This is a qualitative
current-state assertion, without an all-time lower singular-value bound.

The selected construction in `result.md`, §3, follows. A bounded odd
perturbation of \(w=g\) makes \(a_1,a_2,a_3\) independent; the proof
following Theorem 5 of `stationary_geometry.md` supplies the determinant
argument. Complete them to a basis \((a_1,a_2,a_3,a_4)\) of
\(\mathbb R^4\). Choose independent \(z,z_\perp\in\mathbb R^2\),
and define

\[
Ma_1=Ma_2=z,\quad Ma_3=-z,\quad Ma_4=z_\perp,
\qquad c=\frac{\tanh(b_2^\top z)}{\mathbb E_2\tanh^2(b_2^\top z)}.
\]

Then \(M\) has rank two, the predictions are \((1,1,-1)\), and the
upper activation family has rank one. Nevertheless, its common backward
vector satisfies

\[
z^\top d=
\frac{\mathbb E_2[(b_2^\top z)\tanh(b_2^\top z)
                         \operatorname{sech}^2(b_2^\top z)]}
     {\mathbb E_2\tanh^2(b_2^\top z)}>0.
\]

At any state in this class, a vector \(\xi\in\mathbb R^3\) annihilates
the full prediction differential precisely when

\[
\sum_{a\in C}\epsilon_a\xi_a=0\ \text{for every nonzero code class},
\quad \xi_aM^\top d_a=0\ \text{for every }a,
\quad \sum_a\xi_a d_a a_a^\top=0,
\]

where \(v_a=\epsilon_av_C\) within each nonzero class; zero codes are
separate. This is §5 of `stationary_geometry.md`. In the constructed state,
\(M^\top\) is injective and \(d_a=d\ne0\), so the middle condition
forces \(\xi=0\). Thus the complete prediction differential has rank
three although the readout Gram has rank one. Positive data weights do
not change that rank. The construction works for every such input triple;
it is not a claim that canonical training reaches this particular geometry.
The broader stationary classification in the archived source is context,
not an additional global-convergence assertion in this selection.

## 5. Exact reflected-pair and antipodal fitting

Take \(d=2,p=1\), canonical initialization, equal probabilities, and
opposite targets \((+A,-A)\), with any \(A>0\). Full-state fitting and
convergence hold for either of these data classes:

* \((u,Pu)\), with distinct directions, where \(P\) is one of
  \(\operatorname{diag}(1,-1)\), \(\operatorname{diag}(-1,1)\), the
  coordinate swap, or the negative coordinate swap;
* \((u,-u)\) for every \(u\in S^1\). For compatible antipodal labels
  the probabilities may in fact be arbitrary positive values summing to one.

For example \((a,b),(a,-b)\), \(a\ge0,b>0,a^2+b^2=1\), realizes
every separation angle in \((0,\pi]\). This is not every orientation
of each separation. The exact normalized dictionary symmetries are
proved in `antipodal_upgrade_check.md`, §3; arbitrary rotations cannot be
substituted for them. Input oddness supplies the antipodal case directly.

Define the current contrast, signed prediction, and readout norm by

\[
U=\tfrac12(H_+^{(2)}-H_-^{(2)}),\quad
F=\mathbb E_2[cU],\quad C=\mathbb E_2U^2,\quad
q=\mathbb E_2c^2,\quad C_0=\mathbb E_2U_0^2>0.
\]

Symmetry and uniqueness preserve opposite predictions, so
\(\mathcal L=(A-F)^2\) and the **full** physical flow is
\(\dot X=2(A-F)\nabla F\), \(X=(w,c,M)\). For the auxiliary ascent
clock \(X_s=\nabla F\), let
\(K=\|\nabla F\|^2=C+\|\nabla_{(w,M)}F\|^2\). Exactly,

\[
F_s=K,\quad q_s=2F,\quad F^2\le qC\le qK,\quad
\left(\frac q{F^2}\right)_s=-\frac{2(qK-F^2)}{F^3}\le0,
\quad \lim_{s\downarrow0}\frac q{F^2}=\frac1{C_0}.
\]

The archived scalar proof supplies finite-clock continuation before using
the fitting argument. Consequently \(C\ge C_0\), \(K\ge C_0\),
and there is a unique finite \(s_*\le A/C_0\) with \(F(s_*)=A\).
The physical clock \(\dot s=2(A-F)\) tends to \(s_*\) without
reaching it in finite physical time. For every \(t\ge0\),

\[
\mathcal L(t)\le A^2e^{-4C_0t},\qquad
C(t)\ge C_0,\qquad \|c(t)\|_2^2\le A^2/C_0,
\qquad
\int_t^\infty\|\dot X(v)\|\,dv
 \le\sqrt{\mathcal L(t)/C_0}.
\]

The complete state converges in the physical metric, in supremum norm for
the increments \(w-g,c\), and in Frobenius norm for \(M\). The joint
laws converge in \(\mathcal W_2\) under the identical-mark coupling.
The regular current-state potential
\(\Phi=(1+q)/(C_0+F^2)\) satisfies

\[
\dot\Phi=-\frac{4(A-F)F\{(qK-F^2)+(K-C_0)\}}{(C_0+F^2)^2}\le0.
\]

The singular ratio \(q/F^2\) is used only for positive time with its
proved one-sided initial limit; no ambient continuous extension is claimed.
The exact allowed matrix variation in `regular_potential_check.md` and
the antipodal scaling in `all_angles_result.md` give
\(\nabla_{(w,M)}C(X_0)\ne0\). Therefore the ratio decreases strictly
initially and
\(C(X_\infty)>C_0\). Neither monotonicity of \(C(t)\) at every time
nor an angle-uniform gain as opposite labels coalesce is asserted.

There is also a separate **small-label theorem for any orientation**.
For \(v\ne\pm u\), let

\[
\lambda(u,v)=\lambda_{\min}\!\left(
\tfrac12\begin{pmatrix}
\mathbb E H_0(u)^2&\mathbb E H_0(u)H_0(v)\\
\mathbb E H_0(u)H_0(v)&\mathbb E H_0(v)^2
\end{pmatrix}\right)>0.
\]

If \(0<A\le\lambda/(8\sqrt5)\), canonical training on opposite
targets obeys
\[
\mathcal L(t)\le A^2e^{-\lambda t},\qquad
\int_t^\infty\|\dot X(v)\|\,dv
 \le\frac{2A}{\sqrt\lambda}e^{-\lambda t/2}.
\]
The trajectory remains within \(\rho/2\) of initialization, where
\(\rho=\sqrt\lambda/(2\sqrt5)\); a first-exit argument proves the
evolving readout Gram stays above \(\lambda I/4\). It is not an
assumed future Gram bound. The same proof allows arbitrary two labels
whose root-mean-square is at most the stated threshold. Near the fitted
endpoint the fitting set is a \(C^1\) Hilbert submanifold of codimension
two; the loss Hessian has two positive normal eigenvalues and an
infinite-dimensional tangent kernel. Its explicit graph and the stronger
characteristic convergence proof are retained in `route_local.md`, §§3–4,
and the all-orientation initialization and basin proof in
`arbitrary_pair_local.md`, §§1–5.

For a generic pair at unit labels, a second residual direction need not
vanish: writing \(G=(f_++f_-)/2\) gives
\(\mathcal L=(A-F)^2+G^2\) and
\(\dot X=2(A-F)\nabla F-2G\nabla G\). The selected scalar proof does
not control this term. Its arbitrary-orientation unit-label conclusion
therefore remains unproved by this packet.

## 6. Uniform fitting over every canonical cyclic three-input orbit

For \(d=3,p=1\), let \(P\) cyclically permute the three coordinates.
For every \(u\in S^2\), use equal probabilities on
\(\sqrt3u,\sqrt3Pu,\sqrt3P^2u\), all with label \(+1\).
One may simultaneously negate any chosen input and its label, since this
leaves the loss and full vector field identical at every state.

There is a single positive constant, depending only on canonical
initialization,

\[
k_*:=\min_{u\in S^2}\mathbb E_2\left[
\frac13\sum_{j=0}^2\tanh(b_2^\top P^jDa_0(u))\right]^2>0,
\]

such that every one of these initialized flows satisfies
\(\dot{\mathcal L}\le-4k_*\mathcal L\),
\(\mathcal L(t)\le e^{-4k_*t}\), and converges to an actual fitted
endpoint. Uniform bounds hold for \(w-g,c\) in supremum norm and \(M\)
in Frobenius norm; \(w\) itself retains its fixed unbounded Gaussian
part. Compatible repeated inputs at cyclic fixed points are included.

`initialization_positivity.md` proves
\(Da_0(u)=(T(u_1),T(u_2),T(u_3))\), with continuous odd \(T\) strictly
of the sign of its argument; therefore this code never vanishes on the
sphere. For any nonzero code \(z\), the averaged tanh feature has a
nonzero linear Taylor term if \(z_1+z_2+z_3\ne0\). Otherwise, with
\(\ell_j(b)=b^\top P^jz\), its cubic term is nonzero because
\(\ell_0+\ell_1+\ell_2=0\) and
\(\sum_j\ell_j^3=3\ell_0\ell_1\ell_2\) is a nonzero polynomial.
Positive upper density gives pointwise \(k(u)>0\); continuity and sphere
compactness give the stated minimum. Exact cyclic equivariance makes the
predictions equal, so the complete scalar-clock lemma in
`protected_family.md`, §1, applies with \(s_*\le1/k_*\).
This is the full proof chain of `cyclic_uniformity.md`.

For
\(u_\theta=\cos\theta(1,1,1)/\sqrt3+
\sin\theta(2,-1,-1)/\sqrt6\), the input Gram eigenvalues are
\(3\cos^2\theta\) and \(\tfrac32\sin^2\theta\) twice.
The uniform theorem includes all \(0\le\theta\le\pi/2\): the
interior triples are independent, the first endpoint collapses, and the
second is a planar 120-degree triple. After changing the last input and
label sign at the latter endpoint, \(x_3=x_1+x_2\), labels are
\((1,1,-1)\), and \(\sum_a\mu_ay_ax_a=0\). No homogeneous linear
predictor fits these values, whereas this initialized nonlinear closure
does. This statement concerns homogeneous linear predictors, not affine
ones. Mixed-label masses are \(2/3,1/3\), not balanced. The uniform rate
does not assert uniform stability under independent perturbations, other
weights, or arbitrary rotations of the dictionary.

## 7. A balanced initialized positive plateau at the architectural floor

For \(d=3,p=1\), choose \(0<a<1/2\), \(b=1-2a\), and

\[
(x_1,y_1,\mu_1)=(\sqrt3e_1,1,a),\quad
(x_2,y_2,\mu_2)=(-\sqrt3e_1,1,a),\quad
(x_3,y_3,\mu_3)=(\sqrt3e_2,-1,b).
\]

All three inputs are distinct and span a plane. With \(v=-e_2\) and
\(F=f(v)\), the exact ambient loss is
\[
\mathcal L=2a+2a f(e_1)^2+b(1-F)^2\ge2a.
\]
Canonical reflection symmetry keeps \(f(e_1)=f(-e_1)=0\), so the
full trajectory is the ascent curve \(X_s=\nabla F\) with physical
clock \(\dot s=2b(1-F)\). Define, entirely at initialization,

\[
\ell=d_h\nu/\ell_h+
       d_k\beta\eta/\{(\nu+\eta)\ell_k\}>0,\qquad
k=\mathbb E_2\tanh^2(\ell b_2\cdot v)>0.
\]

Then
\[
\mathcal L(0)=1,\quad \dot{\mathcal L}(0)=-4b^2k<0,
\quad \lim_{t\to\infty}\mathcal L(t)=2a,
\quad 0<\mathcal L(t)-2a\le b e^{-4bkt}
\]
for every finite \(t\). The complete state converges to a bounded
endpoint, and loss decreases strictly at every finite time. Both hidden
blocks satisfy \(\dot w(t)\ne0\), \(\dot M(t)\ne0\) for every
\(t>0\), although their initial velocities vanish with the zero readout.

More precisely, the ascent curve has a unique finite \(s_*\le1/k\)
with \(F(s_*)=1\). If
\(\kappa_* =\|\nabla F(X(s_*))\|^2\ge k\), there exists
\(C_*>0\) such that
\[
\mathcal L(t)=2a+b C_*^2e^{-4b\kappa_*t}(1+o(1)).
\]
The increments \(w-g,c\) and \(M\) converge at rate
\(O(e^{-2b\kappa_*t})\) in their characteristic supremum/Frobenius
norms. Choosing \(a=1/4\), \(b=1/2\) gives exactly balanced label
masses, limiting loss \(1/2\), initial derivative \(-k\), and
\(\mathcal L(t)-1/2\le\tfrac12e^{-2kt}\).

`plateau_construction.md`, §§1–5, contains the complete proof, including
the finite-clock bounds, physical-clock continuation, integrability of the
terminal correction determining \(C_*\), and both hidden-motion checks.
This plateau attains \(\mathcal L_{\rm arch}=2a\). It establishes
initialized learning followed by positive limiting loss because same-label
antipodes cannot be fitted by an odd predictor; it does not demonstrate
optimization failure on realizable data. The source's separate §6 finite-fit
construction for independent triples is archived as context, without
promoting it into a claim about initialized reachability.

## 8. Proof coverage, historical checking, and remaining limits

The archive retains the seven complete selected primary files and the
complete proof files needed for the foregoing statements. One supporting
file is excerpted at complete relevant sections: the scalar-clock lemma
and exact cyclic-symmetry calculation from `protected_family.md`. Its
stronger open-family continuation is not a premise. Current Quarto excerpts
replace historical source-name pointers: `docs/observable_p1.md` maps to
the general-dimensional coefficient/parity material in
`docs/07-observable-closure.qmd`; the old `global_nonlinear.md` B dictionary
and fixed-order continuation point to the archived sections of
`docs/08-autonomous-computation.qmd` and
`docs/07-observable-closure.qmd`. `docs/notation.qmd` is included in full.
No archived `old_docs/` passage was read or substituted.

| Selected claim | Complete proof source and essential support | Historical check status |
|---|---|---|
| Full order-two/order-three landscape and floor | `p2_p3_unrestricted_theorem.md`; canonical polynomial dictionary | Informed internal audit and a separate fresh isolated internal PASS, with no requested mathematical corrections. |
| Odd-sector order-one landscape and floor; limited GF basin consequence | `no_bad_local_minima.md`; exact p=1 coefficient model | Informed internal PASS, followed by real-label/floor and GF-corollary supplements. The reviewer was a prior route author; this was not isolated promotion review. |
| Initialized finite-family independence and free query values | `CANONICAL_FEATURES.md` | Informed internal PASS; 167 inserted opening-delimiter escapes were verified as a formatting-only repair. The repaired source and complete version-closure report are retained. |
| Upper collapse with full lower-layer trainability | `result.md` §3; `stationary_geometry.md` Lemma 2, §5, and representability argument | Supporting stationary geometry received a fresh isolated internal PASS after explicit binary-label and parity-scope corrections; the synthesis construction is author-checked. The selected construction does not broaden the saddle theorem's label assumptions. |
| Reflected/antipodal fitting, strict contrast gain, arbitrary-pair small labels | `all_angles_result.md`, `scalar_margin_extension.md`, `arbitrary_pair_local.md`, `route_local.md`, `antipodal_upgrade_check.md`, `scalar_strict_gain.md`, `regular_potential_check.md` | Component analytical internal audits plus post-freeze author/informed combination checks. The combined assembly was not a fresh whole-packet promotion review. |
| Uniform cyclic fitting | `cyclic_uniformity.md`; `initialization_positivity.md`; archived scalar/symmetry sections of `protected_family.md` | Separate internal review PASS of the cyclic corollary and its named dependencies. |
| Initialized positive plateau | `plateau_construction.md` §§1–5; exact p=1 coefficient model | Fresh isolated internal PASS of the initialized plateau, endpoint, terminal tail, physical factors, and both hidden-block motions. |

Historical verdicts describe their recorded versions and scope. The manifest
identifies the bytes assembled now; it does not turn those verdicts into new
checks of the current Quarto edition. Relevant original review reports or
status excerpts are retained as provenance, not mathematical premises.

This assembly read the complete selected primary proofs, the complete
mathematical dependencies used above, and the relevant current-book model,
dictionary, parity, and continuation passages. It reconciled normalization,
dimension, labels, state topology, time factors, and source-version status;
verified the archive against its manifest and the manifest against the source
bytes; and checked document delimiters and source coverage. It ran no numerical
experiment, training campaign, external-source search, or fresh adversarial
proof review. The surrounding source files can contain historical pointers or
broader conclusions that are not premises of the selected chain.

No missing other-study or external theorem is needed for these selected
statements, formulated directly for the specified exact Gaussian-mark
closure. Remaining **logical bridges**, rather than missing proof files,
include general initialized convergence from an absence-of-bad-minima result,
selection of a particular off-training predictor, reachability of the
constructed collapsed fitting states, general unit-label two-residual
control, and transfer of fixed-order all-time results to a dense network.
Weighted slow-onset results and modified optimizer/selector results are not
part of this assembly. No conclusion about all later work in the originating
studies is inferred from the open questions in these selected historical
sources.
