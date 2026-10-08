# Causal response memory and ordered sample forces

Status: independent first-round theory result, 2026-10-07. This is an internally derived research note, not established book material. Scientific inputs were the supervisor's assignment and subsequent clarification that the activation class has bounded derivatives on a prescribed complex strip. No literature, other study, or book material was retrieved. No experiments were run.

The route yields an exact causal memory representation and an explicit autonomous cubic response model whose coefficients have a direct feature-learning interpretation. It does **not** yet yield the requested arbitrary-accuracy, all-time closure with polynomial overhead in a polylogarithmic retained dimension. The gap is a response-algebra compression estimate, in addition to uniform control of the approximation remainder and its propagation.

## 1. Setup and what a closure must supply

There are (m) training examples (v_a\in\mathbb R^d), labels (y_a), width (n), and (L) hidden layers. A finite passive validation panel is included among evaluated sample indices, but only training indices drive the flow. The network is

\[
z_a^{(1)}=Av_a,\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\phi(z_a^{(\ell)}),\qquad
f_a=\frac1n w^\top h_a^{(L)}.
\]

Here (A\in\mathbb R^{n\times d}), (W^{(\ell)}\in\mathbb R^{n\times n}) for (\ell\ge2), and (w\in\mathbb R^n). The activation acts coordinatewise. Set (r_a=f_a-y_a) and (\mathcal L=m^{-1}\sum_a r_a^2). The scaled backward signals are

\[
\delta_a^{(L)}=w\odot\phi'(z_a^{(L)}),\qquad
\delta_a^{(\ell)}=
\phi'(z_a^{(\ell)})\odot
W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]

The initialization has Gaussian (A_0,W_0^{(\ell)}) with the stipulated variances and (w_0=0). The mobilities are (n,1,\ldots,1,n), so

\[
\dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,
\qquad
\dot W^{(\ell)}=-\frac{2}{mn}\sum_a
r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},
\qquad
\dot w=-\frac2m\sum_a r_a h_a^{(L)}.
\]

Define the accumulated sample forces, initialized at zero, by

\[
u_a(t)=-\frac2m\int_0^t r_a(s)\,ds,
\qquad \dot u_a=-\frac2m r_a.
\]

These are actual integrated residual forces, not independent sample clocks. All integrals below are ordinary Riemann–Stieltjes integrals against these continuously differentiable paths.

A qualifying closure must determine predictions and its future motion from its retained state and fixed data computed at initialization. Storing a whole history, retaining current weights under another name, or asking a dense trajectory for later coefficients does not establish this. Moving-coordinate count and fixed-coefficient storage are separate costs.

## 2. Exact forward and backward memory

Integrating the rank-one parameter velocities gives

\[
\begin{aligned}
A(t)&=A_0+\sum_b\int_0^t\delta_b^{(1)}(s)v_b^\top\,du_b(s),\\
W^{(\ell)}(t)&=W_0^{(\ell)}+
\frac1n\sum_b\int_0^t
\delta_b^{(\ell)}(s)h_b^{(\ell-1)}(s)^\top\,du_b(s),\\
w(t)&=\sum_b\int_0^t h_b^{(L)}(s)\,du_b(s).
\end{aligned}
\]

For historical time (s) and current time (t), define the scalar pairings

\[
H_{ba}^{(\ell)}(s,t)=\frac1n h_b^{(\ell)}(s)^\top h_a^{(\ell)}(t),
\qquad
B_{ba}^{(\ell)}(s,t)=\frac1n\delta_b^{(\ell)}(s)^\top\delta_a^{(\ell)}(t).
\]

Substitution into the forward pass is exact:

\[
\begin{aligned}
z_a^{(1)}(t)
&=A_0v_a+\sum_b(v_b^\top v_a)
\int_0^t\delta_b^{(1)}(s)\,du_b(s),\\
z_a^{(\ell)}(t)
&=W_0^{(\ell)}h_a^{(\ell-1)}(t)
+\sum_b\int_0^t
\delta_b^{(\ell)}(s)
H_{ba}^{(\ell-1)}(s,t)\,du_b(s),\\
f_a(t)&=\sum_b\int_0^t H_{ba}^{(L)}(s,t)\,du_b(s).
\end{aligned}
\]

The backward pass becomes

\[
\begin{aligned}
\delta_a^{(L)}(t)
&=\phi'(z_a^{(L)}(t))\odot
\sum_b\int_0^t h_b^{(L)}(s)\,du_b(s),\\
\delta_a^{(\ell)}(t)
&=\phi'(z_a^{(\ell)}(t))\odot
\left[
W_0^{(\ell+1)\top}\delta_a^{(\ell+1)}(t)
+\sum_b\int_0^t h_b^{(\ell)}(s)
B_{ba}^{(\ell+1)}(s,t)\,du_b(s)
\right].
\end{aligned}
\]

These formulas expose the mechanism. A hidden-layer update writes an association between the activation and the backward signal at the write time. Later forward propagation reads that association through a historical/current activation pairing; later backward propagation reads it through a historical/current backward pairing. Replacing either pairing by a current/current Gram matrix changes the dynamics.

This is an exact causal identity, but not a finite scalar closure. It still uses vector histories and the initialized linear maps. In particular, two-time scalar correlations alone do not evaluate the coordinatewise nonlinearities in the displayed equations. This prevents promoting the identity itself into a solution of the requested reduction problem.

For comparison, the exact instantaneous response coefficient is

\[
K_{ab}(t)=H_{ab}^{(L)}(t,t)
+(v_a^\top v_b)B_{ab}^{(1)}(t,t)
+\sum_{\ell=2}^L
H_{ab}^{(\ell-1)}(t,t)B_{ab}^{(\ell)}(t,t),
\qquad
\dot f_a=\sum_bK_{ab}\dot u_b.
\]

The equality follows by taking the mobility-weighted inner product of the parameter gradients of (f_a,f_b). Each term has the stated normalization: the (A) term is ((v_a^\top v_b)(\delta_a^\top\delta_b)/n), and a hidden (W) term is the product of the two normalized pairings. At initialization (\delta=0), hence (K(0)=H^{(L)}(0,0)).

## 3. The first feature-learning correction has a transparent finite state

Collect the hidden parameters into (\eta=(A,W^{(2)},\ldots,W^{(L)})), regarded as a Euclidean vector using Frobenius inner products on matrix blocks. Its mobility operator (M_\eta) multiplies the (A) block by (n) and leaves the other blocks unchanged. In this section write (h_a(\eta)=h_a^{(L)}(\eta)), and let

\[
h_a^0=h_a(\eta_0),\qquad
J_a=D_\eta h_a(\eta_0).
\]

Thus (J_a) maps a hidden-parameter perturbation to a perturbation of the final activation vector. The controlled system can be written

\[
d\eta=\frac1n\sum_a M_\eta D_\eta h_a(\eta)^\top w\,du_a,
\qquad
dw=\sum_a h_a(\eta)\,du_a.
\]

The needed fixed coefficients are the initialized feature Gram matrix and a four-sample response Gram matrix:

\[
H^0_{ce}=\frac1n h_c^{0\top}h_e^0,
\qquad
R_{ce,ab}=
\frac1{n^2}
\left\langle
M_\eta^{1/2}J_c^\top h_e^0,
M_\eta^{1/2}J_a^\top h_b^0
\right\rangle.
\]

The ordered pair ((c,e)) has a concrete meaning: freeze the readout to (h_e^0), backpropagate the output at sample (c), and take its hidden-parameter response. The matrix (R), indexed by ordered pairs, is the Gram matrix of these virtual-readout responses. It is positive semidefinite. Computing it uses only the initialized network and the supplied input panel, not a trained trajectory.

For training indices define ordered force integrals

\[
S_{ba}(t)=\int_0^t u_b(s)\,du_a(s),
\qquad
S_{bad}(t)=\int_0^t S_{ba}(s)\,du_d(s).
\]

The index order is chronological: (b) acts before (a), then (d). Their autonomous updates are

\[
\dot S_{ba}=u_b\dot u_a,
\qquad
\dot S_{bad}=S_{ba}\dot u_d,
\qquad
S_{ba}(0)=S_{bad}(0)=0.
\]

The explicit cubic response is

\[
f_c^{[3]}=
\sum_e H^0_{ce}u_e
+\sum_{a,b,d}R_{dc,ab}S_{bad}
+\sum_{e,a,b}R_{ce,ab}u_eS_{ba}.
\]

All summed indices are training indices; the evaluated index (c) can also be a passive validation point. Coupling this output formula to (\dot u_a=-2(f_a^{[3]}-y_a)/m) and the displayed memory updates gives a finite autonomous system. It stores (m+m^2+m^3) moving scalar coordinates, independently of width. Its fixed coefficients have four sample indices, and require additional coefficients for the validation panel. No evolving weights occur in this system.

Here is the derivation. Scale a fixed finite-variation force path by a scalar (\varepsilon). Because the controlled equations are invariant under ((u,w,\eta)\mapsto(-u,-w,\eta)), hidden parameters have even degree in (\varepsilon), whereas the readout and outputs have odd degree. The first nonzero terms satisfy

\[
\begin{aligned}
w^{[1]}&=\sum_b h_b^0u_b,\\
\eta^{[2]}&=\frac1n\sum_{a,b}
M_\eta J_a^\top h_b^0 S_{ba},\\
h_c^{[2]}&=J_c\eta^{[2]},\\
w^{[3]}&=\frac1n\sum_{a,b,d}
J_dM_\eta J_a^\top h_b^0 S_{bad}.
\end{aligned}
\]

The output through degree three is

\[
\frac1n\bigl(w^{[1]\top}h_c^0+
w^{[3]\top}h_c^0+w^{[1]\top}h_c^{[2]}\bigr),
\]

which gives the formula above after substituting the definition of (R). The two cubic contributions distinguish feature motion that changes later readout writes from feature motion that changes the final evaluation of the current readout. This makes the extra mechanism beyond frozen-kernel training explicit.

On any fixed instance and controlled-path neighborhood where the analytic expansion is valid, the omitted term is (O(\varepsilon^5)). This is a local response statement. It is **not** an all-time bound uniform in width, and with fixed nonzero label scale it is **not** an error that tends to zero as (n\to\infty). No such promotion is made here.

The identities (S_{ab}+S_{ba}=u_au_b) split the second-order memory into its endpoint-determined symmetric part and its antisymmetric ordered-area part. Thus some memory coordinates can be removed, but the antisymmetric part carries information absent from the force totals.

## 4. Force totals lose actual nonlinear information

The following example uses an activation within the bounded-strip-derivative class. Take (L=1), (n=2), (m=d=2), (v_1=e_1,v_2=e_2), and (\phi(z)=\sin z). Consider the initialized preactivation columns

\[
z_1^0=(\pi/6,\pi/6)^\top,
\qquad
z_2^0=(\pi/6,\pi/3)^\top.
\]

Their feature Gram matrix has entries

\[
H^0_{11}=\frac14,\quad
H^0_{12}=\frac{1+\sqrt3}{8},\quad
H^0_{22}=\frac12,\quad
\det H^0=\frac{2-\sqrt3}{32}>0.
\]

The two force paths below have identical endpoint (u_1=u_2=s): first apply sample 1 by amount (s), then sample 2 by amount (s); or reverse that order. In this one-layer orthogonal-input example,

\[
R_{ce,ab}=\mathbf1_{c=a}\frac1n
\sum_i h_{e,i}^0h_{b,i}^0\cos^2(z_{c,i}^0).
\]

The three relevant coefficients are

\[
R_{11,12}=\frac{3(1+\sqrt3)}{32},\qquad
R_{21,21}=\frac18,\qquad
R_{12,12}=\frac38.
\]

For unequal force amounts (\alpha,\beta), substituting the ordered integrals into the cubic formula gives

\[
f_1(1\text{ then }2)-f_1(2\text{ then }1)
=-\frac32R_{11,12}\alpha^2\beta
+\left(\frac12R_{21,21}-R_{12,12}\right)\alpha\beta^2
+O((|\alpha|+|\beta|)^5).
\]

In particular, at equal amounts this is

\[
-\frac{29+9\sqrt3}{64}s^3+O(s^5),
\]

which is nonzero for sufficiently small positive (s). The leading coefficient and Gram determinant remain nonzero on an open neighborhood of this initialization. Gaussian initialization assigns positive probability to that neighborhood.

This refutes an exact input-output reduction that retains only the accumulated force totals and must handle arbitrary externally supplied sample-force paths. It does **not** prove that no finite closure exists for the smaller class of paths generated by fixed-label gradient flow; those controls have additional feedback constraints. It also does not refute an approximation that retains ordered memories.

## 5. Analyticity does not make the response algebra terminate

There is a second precise obstruction to a tempting shortcut: the sample vector fields need not generate a finite-dimensional Lie algebra, even for sine activation and a shallow network. It is enough to inspect one neuron with two orthogonal inputs. Write its two preactivations as (x,y) and its readout as (w). The two controlled vector fields are

\[
V_1=w\cos x\,\partial_x+\sin x\,\partial_w,
\qquad
V_2=w\cos y\,\partial_y+\sin y\,\partial_w.
\]

Use the commutator convention ([V_1,V_2]=V_1\cdot\nabla V_2-V_2\cdot\nabla V_1). Since the (y)-component of (V_1) is zero, the (y)-component of the (k)-fold commutator (\operatorname{ad}_{V_1}^kV_2) is

\[
\cos y\,V_1^k w.
\]

For (k\ge1), (V_1^k w) is a polynomial in (w) of degree (k-1). Its leading coefficient is

\[
(\cos x\,\partial_x)^{k-1}\sin x.
\]

To check that this coefficient never vanishes identically, put (s=\sin x). The operator becomes ((1-s^2)\partial_s); its (j)-fold application to (s) is a polynomial of degree (j+1) with leading coefficient ((-1)^j j!\ne0). Consequently these commutators have different nonzero maximal degrees in (w), so they are linearly independent. The same obstruction persists in a multi-neuron network by restricting attention to a neuron's coordinate block.

Thus there is no exact universal finite commutator truncation supplied merely by shallow depth, analyticity, or bounded strip derivatives. This result concerns the Lie algebra of vector fields, not minimal nonlinear state dimension: the original three-coordinate neuron already has a finite nonlinear state. It therefore does not prove a general finite-closure impossibility theorem.

## 6. What arbitrary-order control signatures would require

For a word (a_1\cdots a_k) of training indices define

\[
S_{a_1\cdots a_k}(t)
=\int_{0<t_1<\cdots<t_k<t}
du_{a_1}(t_1)\cdots du_{a_k}(t_k).
\]

The empty-word value is 1 and

\[
\dot S_{a_1\cdots a_k}
=S_{a_1\cdots a_{k-1}}\dot u_{a_k}.
\]

These variables are causal, initialized without future information, and restartable from their current stored values. The cubic construction shows concretely how initialized response contractions evaluate their first nonlinear output terms. At higher orders, differentiating the forward pass and the backward pass generates further initialized response tensors; their admissible compression remains to be proved. Listing unnamed iterated derivatives would not answer the transparency requirement.

There are two separate quantitative obstacles.

First, one needs a width-controlled convergent expansion over the whole force path. Set

\[
U(t)=\sum_{a=1}^m\int_0^t|du_a(s)|.
\]

For any length (k), the sum of the absolute iterated-integral values obeys

\[
\sum_{a_1,\ldots,a_k}|S_{a_1\cdots a_k}(t)|
\le \frac{U(t)^k}{k!}.
\]

Indeed, replace each signed differential by its total-variation measure, sum the index choices inside the ordered integral, and integrate over one of the (k!) time-ordering simplices. If the output coefficients at order (k) obey a bound (C k! R^{-k}), and (U(\infty)\le\rho R) for some (\rho<1), the response tail for a fixed supplied control path is at most

\[
C\sum_{k>q}\rho^k=\frac{C\rho^{q+1}}{1-\rho}.
\]

This is a conditional source estimate, not a theorem establishing those coefficient and action bounds for the stated network class. Bounded strip derivatives and existing small-label assumptions are promising inputs, but their actual constants and their width dependence have to be verified. A fixed-control error also needs a feedback stability argument before it becomes an error for the autonomous training surrogate. Finally, stability must include the passive outputs, not merely training residual decay.

Second, the literal word construction has

\[
N_q=\sum_{k=1}^q m^k
\]

moving coordinates, plus the output coefficients for those words. Even if the favorable constants above were independent of width, an accuracy (\varepsilon=n^{-c}) obtained from geometric decay generally requires (q=O(\log n)). For (m>1), the resulting explicit state bound is polynomial in (n), not polynomial in (\log n). This is a complexity limitation of the full-word construction. It is not a lower bound for every possible response representation. Symmetry relations remove some redundant words, but a polynomial-size replacement needs a separate structural theorem.

When (m=1), every word is the repeated single index and (S_{1\cdots1}=u_1^k/k!); the order-memory obstruction disappears. That special case does not resolve several-sample training. Nor does an existing compact representation of the parameter trajectory automatically bound the rank of its initialized response tensors or the complexity of their contractions.

## 7. Present conclusion and precise next bridge

The exact causal skeleton and cubic response law are derived. They identify a meaningful extra object beyond the frozen feature kernel: the Gram matrix of virtual-readout hidden responses, coupled to ordered sample-force memories. The sine example establishes that chronological information can affect predictions at the first nonlinear order while the initialized feature Gram is positive. The nonterminating commutator calculation rules out an exact finite-order shortcut based solely on analyticity.

What remains open is the requested all-time closure at arbitrary accuracy with acceptable width dependence. The decisive missing statement is a bound on the effective rank or compressibility of the higher ordered response contractions, with coefficients obtained at initialization, coupled to an all-time tail and feedback-transfer estimate. An abstract full-word expansion, an (O(\|y\|^5)) local remainder, or finite vector-valued history storage does not supply that statement.

The excluded quadratic-activation toy was considered during derivation and discarded as evidence about the stipulated regime: its derivatives are not bounded on the required strip. None of the conclusions above relies on it.
