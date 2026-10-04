# Actual finite carrier tails by a controlled cavity argument

This is an internally derived result for this study. It proves actual finite-network all-time tails in a restricted but nonlinear setting. It does not prove the requested dense finite-to-population root-width estimate.

Scientific inputs read: the setting in `paper/main.tex`; complete `paper/results.tex`, `paper/proof_alltime.tex`, and `paper/proof_tracking.tex`; `docs/notation.qmd`; and this study's README. The canonical-notation skill and its neural reference, and the rigorous-proof skill, were applied. No other study or archived book passage was read.

## 1. Result and additional assumptions

Retain the manuscript's dense gradient flow, Gaussian initialization, exactly zero initial readout, fixed data, initial feature-Gram gap, and small fixed labels. Impose these additional assumptions:

- There are exactly two hidden layers, so the only hidden matrix is \(W=W^{(2)}\in\mathbb R^{n\times n}\).
- With \(v_a=x_a/\sqrt d\), the training inputs satisfy \(v_a^\top v_b=\mathbf 1_{a=b}\).
- The first activation is \(\phi_1(z)=\tanh z\).
- The second activation \(\phi_2\) is bounded, with \(|\phi_2|\le B\), \(|\phi_2'|\le s\), and \(\operatorname{Lip}(\phi_2')\le j\). In particular both activations may be tanh.

Here \(m,d,B,s,j\) are fixed independently of width. The usual backward fields are

\[
\delta_a^{(2)}=w\odot\phi_2'(z_a^{(2)}),\qquad
k_a^{(1)}=W^\top\delta_a^{(2)},\qquad
\delta_a^{(1)}=\phi_1'(z_a^{(1)})\odot k_a^{(1)},
\]

and the top carrier is \(k_a^{(2)}=w\).

Let \(\mathcal G_n\) be the manuscript's fitting event, with initialized operator bound \(\|W_0\|_{\rm op}\le K\). Its deterministic fitting estimate gives

\[
\int_0^\infty\rho(t)\,dt\le Y/\kappa,
\qquad Y=\Bigl(m^{-1}\sum_a y_a^2\Bigr)^{1/2}.
\]

Write \(S=2Y/\kappa\), and decrease the fixed label threshold so \(S\le1\). The result is trivial when \(Y=0\), so below \(S>0\).

**Finite carrier theorem.** There are constants \(c,C>0\), depending on \(K,m,B,s,j\) but independent of \(n,S,t\), such that every neuron \(i\) and sample \(a\) satisfy

\[
\mathbb E\!\left[\mathbf 1_{\mathcal G_n}
 \exp\left\{\frac{c}{S^2}\sup_{t\ge0}|k_{a,i}^{(1)}(t)|^2\right\}\right]
\le C.
\tag{1}
\]

On \(\mathcal G_n\), \(\sup_t\|w(t)\|_\infty\le BS\). Consequently,

\[
\Pr\left(\mathcal G_n\cap
 \left\{\max_{a,i}\sup_{t\ge0}|k_{a,i}^{(1)}(t)|>M\right\}\right)
\le Cmn\exp\{-cM^2/S^2\}.
\tag{2}
\]

Thus a smooth carrier cutoff equal to the identity on \([-M_n,M_n]\), with

\[
M_n\ge BS+C S\sqrt{\log(Cmn/\delta)},
\tag{3}
\]

is inactive along the entire dense finite trajectory, except on an event of probability at most \(\delta+\Pr(\mathcal G_n^c)\). The original and cutoff finite algorithms therefore agree exactly on that event's complement. This conclusion concerns trained finite coordinates; no finite-to-population rate is used anywhere in its proof.

The proof below first establishes a stronger control-path statement, uniformly over all residual histories with total variation at most \(S\). A cavity then separates a Gaussian matrix column from a deterministic family of possible backward fields. An elementary Gaussian chaining argument bounds the supremum over that family. This handles adaptive residuals without declaring them independent of initialization.

## 2. Exact transformed equations

Define the increasing smooth bijection

\[
F(z)=\frac z2+\frac{\sinh(2z)}4,
\qquad F'(z)=\cosh^2z=\frac1{\phi_1'(z)},
\]

and define \(\psi(p)=\tanh(F^{-1}(p))\). Its derivative satisfies

\[
\psi'(p)=\operatorname{sech}^4(F^{-1}(p)),
\qquad |\psi|\le1,\quad 0<\psi'\le1.
\tag{4}
\]

All functions act coordinatewise on vectors. Let \(p_a=F(z_a^{(1)})\), so \(h_a^{(1)}=\psi(p_a)\). The exact first-layer dynamics are

\[
\dot z_a^{(1)}=-\frac2m\sum_b r_b\delta_b^{(1)}v_b^\top v_a
=-\frac2m r_a\phi_1'(z_a^{(1)})\odot k_a^{(1)}.
\]

Define the integrated residual path

\[
b_a(t)=-\frac2m\int_0^t r_a(u)\,du.
\]

The chain rule cancels the first-layer gate, giving the exact controlled system

\[
\begin{aligned}
 dp_a&=k_a^{(1)}\,db_a,\\
 dw&=\sum_a h_a^{(2)}\,db_a,\\
 dW&=\frac1n\sum_a\delta_a^{(2)}h_a^{(1)\top}\,db_a,\\
 h_a^{(1)}&=\psi(p_a),\quad z_a^{(2)}=Wh_a^{(1)},\quad
 h_a^{(2)}=\phi_2(z_a^{(2)}),\\
 \delta_a^{(2)}&=w\odot\phi_2'(z_a^{(2)}),\quad
 k_a^{(1)}=W^\top\delta_a^{(2)}.
\end{aligned}
\tag{5}
\]

The initial coordinates \(p_a(0)=F(W_0^{(1)}v_a)\) need not have a useful bounded derivative with respect to Gaussian roots. The argument does not differentiate them or bound their maximum.

The \(\ell^1\) total variation of the actual driver is bounded by

\[
\sum_a\int_0^\infty|db_a|
=\frac2m\int_0^\infty\sum_a|r_a(t)|\,dt
\le2\int_0^\infty\rho(t)\,dt\le S.
\tag{6}
\]

Every prefix of this driver can be reparametrized by its accumulated \(\ell^1\) variation and then extended constantly to \([0,S]\). It belongs to the deterministic class

\[
\mathcal B_S=\{b:[0,S]\to\mathbb R^m:
 b(0)=0,\ b\text{ absolutely continuous},\
 \sum_a|b_a'(u)|\le1\text{ almost everywhere}\}.
\tag{7}
\]

This class is compact in the uniform norm. In particular it contains all reparametrized actual prefixes, although the particular chosen prefix depends on initialization. Solutions of (5) are invariant under these increasing time changes; this follows directly by the integral change of variables. Constant portions make no parameter change. It therefore suffices to bound the terminal carriers of (5), uniformly over deterministic \(b\in\mathcal B_S\).

## 3. Width-independent control estimates

Fix a deterministic initialization with \(\|W_0\|_{\rm op}\le K\). Throughout this section, \(b\in\mathcal B_S\) is arbitrary, not necessarily generated by a residual.

Use the ordinary normalized parameter difference

\[
D(X,\widetilde X)=
 \sum_{a=1}^m\frac{\|p_a-\widetilde p_a\|_2}{\sqrt n}
 +\frac{\|w-\widetilde w\|_2}{\sqrt n}
 +\|W-\widetilde W\|_F,
\qquad X=(p_1,\ldots,p_m,w,W).
\tag{8}
\]

As \(|h^{(1)}|\le1\), \(|h^{(2)}|\le B\), the controlled integral equations give, at variation time \(u\le S\),

\[
\|w(u)\|_\infty\le Bu,\qquad
\frac{\|\delta_a^{(2)}(u)\|_2}{\sqrt n}\le sBu,
\qquad
\|W(u)-W_0\|_F\le sB S^2.
\tag{9}
\]

For the last inequality, the Frobenius norm of each rank-one integrand is at most
\((\|\delta_a^{(2)}\|_2/\sqrt n)(\|h_a^{(1)}\|_2/\sqrt n)\le sBS\), and the total driver variation is at most \(S\). Thus \(\|W\|_{\rm op}\le K+sBS^2\). Also \(\|k_a^{(1)}\|_2/\sqrt n\le (K+sB)sBS\). These bounds prevent finite-time blowup on \([0,S]\); the finite-dimensional locally Lipschitz ODE has a unique solution on that interval.

Write (5) as \(dX=\sum_a V_a(X)\,db_a\). On the tube

\[
\|w\|_\infty\le BS,\qquad \|W\|_{\rm op}\le K+sB,
\tag{10}
\]

each \(V_a\) has norm at most a constant \(V\), and is Lipschitz in (8), with constant \(L\); \(V,L\) are independent of \(n\) and \(S\le1\). To verify this, (4) first gives

\[
\frac{\|h_a^{(1)}-\widetilde h_a^{(1)}\|_2}{\sqrt n}\le D,
\qquad
\frac{\|z_a^{(2)}-\widetilde z_a^{(2)}\|_2}{\sqrt n}\le CD.
\]

Then

\[
\frac{\|\delta_a^{(2)}-\widetilde\delta_a^{(2)}\|_2}{\sqrt n}
\le s\frac{\|w-\widetilde w\|_2}{\sqrt n}
 +jBS\frac{\|z_a^{(2)}-\widetilde z_a^{(2)}\|_2}{\sqrt n}
\le CD.
\tag{11}
\]

Subtracting \(W^\top\delta_a^{(2)}\) uses only (11), bounded operators, and \(\|\delta_a^{(2)}\|_2/\sqrt n\le sBS\). The matrix-update difference uses

\[
\left\|\frac{uv^\top-\widetilde u\widetilde v^\top}{n}\right\|_F
\le\frac{\|u-\widetilde u\|_2}{\sqrt n}\frac{\|v\|_2}{\sqrt n}
 +\frac{\|\widetilde u\|_2}{\sqrt n}\frac{\|v-\widetilde v\|_2}{\sqrt n}.
\]

This verifies every component of the asserted Lipschitz bound. There is no unbounded first-carrier multiplier in \(V_a\).

It is essential to control the solution in the uniform norm of the *integrated* driver, rather than in the \(L^1\) distance of its derivative. Here that estimate follows by integration by parts. Let \(X^b,X^c\) start at the same initial state, and put \(\varepsilon=\max_a\sup_u|b_a(u)-c_a(u)|\). Their difference is

\[
X^b(u)-X^c(u)=
\sum_a\int_0^u[V_a(X^b)-V_a(X^c)]\,db_a
+\sum_a\int_0^u V_a(X^c)\,d(b_a-c_a).
\]

The path \(V_a(X^c)\) is absolutely continuous, and its total variation is at most \(LV S\): composition with an \(L\)-Lipschitz map multiplies variation by at most \(L\), and \(X^c\) has variation at most \(VS\). Componentwise integration by parts bounds the second term by \(m\varepsilon V(1+LS)\). Gronwall against the variation measure of \(b\) therefore gives

\[
\sup_{u\le S}D(X^b(u),X^c(u))
\le mV(1+LS)e^{LS}\varepsilon\le C\varepsilon.
\tag{12}
\]

Combining this with (11),

\[
\frac{\|\delta_a^{(2),b}(S)-\delta_a^{(2),c}(S)\|_2}{\sqrt n}
\le C\|b-c\|_\infty.
\tag{13}
\]

No differentiability of \(V_a\) beyond its Lipschitz property is needed for this integration-by-parts argument.

## 4. Delete one first-layer neuron

Fix a first-layer neuron \(i\). Write \(W_{0,i}\in\mathbb R^n\) for the initialized column and \(W_{0,-i}\in\mathbb R^{n\times(n-1)}\) for the other columns.

The cavity system has first-layer vectors \(p_a^{-i}\in\mathbb R^{n-1}\), readout \(w^{-i}\in\mathbb R^n\), and matrix \(W^{-i}\in\mathbb R^{n\times(n-1)}\). It uses exactly (5), with neuron \(i\) omitted from the first layer and with every normalization still equal to \(n\), not \(n-1\). It starts from \(W_{0,-i}\), the retained initial first-layer coordinates, and zero readout. For each deterministic driver it is independent of \(W_{0,i}\). All estimates (9)--(13) still apply when \(\|W_{0,-i}\|_{\rm op}\le K\), since a cavity feature has norm at most \(\sqrt n\).

Compare the true and cavity systems using the *same* driver \(b\). In (8), compare only the retained first-layer coordinates, the readout, and the retained columns. In particular, do not include the deleted \(p_{a,i}\) in the distance. Call the resulting distance \(D_i(u)\).

The full column satisfies the uniform estimate

\[
\|W_i(u)-W_{0,i}\|_2
\le\frac1n\sum_a\int_0^u\|\delta_a^{(2)}\|_2|h_{a,i}^{(1)}|\,|db_a|
\le\frac{sBS^2}{\sqrt n}.
\tag{14}
\]

Set \(q_i=\|W_{0,i}\|_2+sBS^2/\sqrt n\). The direct missing contribution to a second-layer preactivation is \(W_i h_{a,i}^{(1)}\), of Euclidean norm at most \(q_i\). After splitting off that contribution, the actual restricted dynamics differ from the cavity vector fields by a forcing of norm at most \(Cq_i/\sqrt n\) per unit driver variation. Indeed, the readout forcing is at most \(s q_i/\sqrt n\); the top-backward forcing is at most \(jBSq_i/\sqrt n\); multiplication by the retained matrix and the rank-one update preserve this bound. Thus

\[
\sup_{u\le S}D_i(u)\le\frac{CSq_i}{\sqrt n}.
\tag{15}
\]

For the top backward field the sharper factor \(S\) is retained: the readout difference from (15) is \(O(Sq_i/\sqrt n)\), and the gate difference is multiplied by \(\|w\|_\infty\le BS\). Therefore

\[
\sup_{u\le S}
\|\delta_a^{(2),b}(u)-\delta_a^{(2),-i,b}(u)\|_2
\le CSq_i.
\tag{16}
\]

At terminal time,

\[
\begin{aligned}
k_{a,i}^{(1),b}(S)
&=W_{0,i}^\top\delta_a^{(2),-i,b}(S)+R_{a,i}^b,\\
|R_{a,i}^b|
&\le\|W_{0,i}\|_2\,CSq_i
 +\frac{sBS^2}{\sqrt n}\,sBS\sqrt n.
\end{aligned}
\tag{17}
\]

On \(E_n=\{\|W_0\|_{\rm op}\le K\}\), both \(\|W_{0,i}\|_2\le K\) and \(q_i\le K+sB\). Hence, uniformly over all samples, neurons, and drivers,

\[
|R_{a,i}^b|\le CS.
\tag{18}
\]

The error is bounded, not asserted to vanish in width. A bounded shift is sufficient for a Gaussian tail estimate.

## 5. Gaussian chaining over all driver histories

Condition on all first-layer initialization and \(W_{0,-i}\). The remaining column has law \(W_{0,i}\sim N(0,I_n/n)\). Define the cavity family to be zero when \(\|W_{0,-i}\|_{\rm op}>K\), so the family always obeys the deterministic bounds used next. This conditioning event is independent of the omitted column.

For a fixed sample \(a\), let

\[
G_b=W_{0,i}^\top\delta_a^{(2),-i,b}(S),\qquad b\in\mathcal B_S.
\]

Conditionally, this is a centered Gaussian process. From (9) and (13),

\[
\mathbb E_i G_b^2\le (sBS)^2,
\qquad
\mathbb E_i|G_b-G_c|^2\le C^2\|b-c\|_\infty^2,
\qquad G_0=0,
\tag{19}
\]

where \(\mathbb E_i\) integrates only the omitted column. The family is continuous in the driver norm for every finite column realization, so a countable dense family gives the same supremum.

Here is an explicit entropy and moment argument. For \(0<\varepsilon\le S\), sample a driver at a grid of mesh at most \(\varepsilon/4\) and round its values to a coordinate lattice of mesh \(\varepsilon/4\). Drivers with the same rounded values differ by at most \(\varepsilon\) uniformly, after adjusting a fixed constant for \(m\). Select one actual driver from each nonempty bin. This gives an internal \(\varepsilon\)-net \(\mathcal N_\varepsilon\subset\mathcal B_S\) with

\[
\log|\mathcal N_\varepsilon|
\le C_m(1+S/\varepsilon)\log(2+S/\varepsilon).
\tag{20}
\]

Take nets \(\mathcal N_\ell\) at \(\varepsilon_\ell=S2^{-\ell}\), with \(\mathcal N_0=\{0\}\), and select nearest points \(\pi_\ell b\). Each Gaussian increment
\(G_{\pi_\ell b}-G_{\pi_{\ell-1}b}\) has standard deviation at most \(CS2^{-\ell}\), and there are at most \(|\mathcal N_\ell||\mathcal N_{\ell-1}|\) possible pairs.

For any finite family of centered Gaussian variables with standard deviations at most \(\sigma\), the union bound

\[
\Pr\{\max_{r\le N}|Z_r|>\sigma\sqrt{2(\log(2N)+u)}\}\le e^{-u}
\]

and tail integration imply
\(\|\max_r|Z_r|\|_{L^p}\le C\sigma(\sqrt{\log(2N)}+\sqrt p)\) for \(p\ge2\). Independence within the Gaussian family is unnecessary. Applying this to each net increment, using (20), and summing by the \(L^p\) triangle inequality yields

\[
\begin{aligned}
\left\|\sup_{b\in\mathcal B_S}|G_b|\right\|_{L^p(\mathbb E_i)}
&\le CS\sum_{\ell\ge1}2^{-\ell}
 \left(\sqrt p+\sqrt{(\ell+1)2^\ell}\right)\\
&\le CS\sqrt p.
\end{aligned}
\tag{21}
\]

Continuity identifies the telescoping limit with \(G_b\). The summable displayed majorant justifies the infinite sum. The constants are deterministic and uniform in the conditioned cavity data on the indicated operator event.

Let \(U_{a,i}=\sup_{b\in\mathcal B_S}|k_{a,i}^{(1),b}(S)|\), the supremum of the absolute true terminal carrier. Equations (17)--(18), and the implication \(E_n\subset\{\|W_{0,-i}\|_{\rm op}\le K\}\), give

\[
\|\mathbf 1_{E_n}U_{a,i}\|_{L^p}\le CS\sqrt p,
\qquad p\ge2.
\tag{22}
\]

We never condition on \(E_n\) when declaring the Gaussian law. Instead, we bound \(\mathbf 1_{E_n}U_{a,i}\) pointwise by the unrestricted Gaussian supremum from (21), plus \(CS\). This preserves the valid conditional Gaussian calculation.

Expanding the exponential in a series and using (22) at \(p=2r\), together with \(r!\ge(r/e)^r\), proves

\[
\mathbb E\left[\mathbf 1_{E_n}\exp\{cU_{a,i}^2/S^2\}\right]\le C
\tag{23}
\]

for sufficiently small fixed \(c>0\). The actual all-time path lies in this control class on \(\mathcal G_n\), and \(\mathcal G_n\subset E_n\). Equations (1)--(2) follow.

## 6. Weighted finite tails and cutoff removal

For completeness, define the manuscript's finite tail quantities in this two-layer case:

\[
H_n(M,t)=\max_a\frac{\|k_a^{(1)}(t)\mathbf 1_{|k_a^{(1)}(t)|>M}\|_2}{\sqrt n}
 +\frac{\|w(t)\mathbf 1_{|w(t)|>M}\|_2}{\sqrt n},
\quad Z_n(M)=\mathbf 1_{\mathcal G_n}\int_0^\infty\rho(t)H_n(M,t)\,dt.
\]

For \(M\ge BS\) the readout term vanishes. Equation (23) and tail integration give

\[
\mathbb E[\mathbf 1_{E_n}U_{a,i}^2\mathbf 1_{U_{a,i}>M}]
\le CS^2e^{-cM^2/S^2},
\tag{24}
\]

after reducing \(c\). Bounding a maximum by the sum over the fixed \(m\) samples, using (6), and applying Cauchy--Schwarz to the empirical square root gives

\[
\mathbb E Z_n(M)\le CS^2e^{-cM^2/S^2}.
\tag{25}
\]

No independence between neurons is needed here. For any prescribed \(r>0\) and \(\delta>0\), choosing \(M=A_{r,\delta}S\sqrt{\log(e+n)}\) therefore gives \(Z_n(M)\le C_\delta S^2n^{-r}\) with probability at least \(1-\delta\), by Markov's inequality and a sufficiently large fixed \(A_{r,\delta}\). This weighted-tail conclusion could be used even when complete inactivity is unnecessary.

The stronger maximum estimate (2) gives actual inactivity at (3). At a dense state satisfying \(|w_i|\le M_n\) and \(|k_{a,i}^{(1)}|\le M_n\), the recursive cutoff backward fields equal the original backward fields. Thus the full dense trajectory solves the cutoff ODE with the same initial conditions. The finite-dimensional cutoff ODE is locally Lipschitz; uniqueness forces equality of the two trajectories on every finite horizon, and the globally bounded dense path provides their common continuation. This proves finite cutoff removal with zero error on the event in (2), not merely a small error bound.

## 7. Limits and exact remaining gap

The theorem is stronger than the manuscript's qualitative finite-tail transfer within its additional assumptions: it controls the actual time supremum before exponentiation, gives quantitative growing cutoffs, and does not use a finite-program approximation or a population convergence rate.

It does not establish the requested theorem for arbitrary fixed training data or arbitrary fixed depth. Orthogonality was used exactly in the second equality preceding (5). For a general input Gram \(G_{ab}=v_a^\top v_b\), the transformed equation becomes

\[
dp_a=\sum_bG_{ab}
 \frac{\phi_1'(z_b^{(1)})}{\phi_1'(z_a^{(1)})}
 k_b^{(1)}\,db_b.
\]

The cross-sample derivative ratio is unbounded for tanh, so the width-independent Lipschitz estimate in Section 3 no longer follows. At depth three, the gate of the intermediate backward field is multiplied by an unbounded carrier even after this first-layer change of coordinates. These are precise failures of this proof, not counterexamples to the desired tail theorem.

A second tempting inference is also invalid: Gaussian marginal laws or tails for the population do not imply (1) for adaptive finite coordinates, nor do qualitative empirical-law limits supply a rate at \(M_n\asymp\sqrt{\log n}\). The cavity/chaining proof above supplies the missing finite statement only in the specified special case.

Finally, strict \(C_\delta/\sqrt n\) prediction convergence still does not follow even in this special case. The finite cutoff removal error is now zero with high probability, but one still needs a quantitative all-time comparison between the cutoff finite system and its cutoff population, including its width bias. A bound of the form \(C(M)n^{-1/2}\), with \(C(M)\) growing as \(e^{CM}\), gives \(n^{-1/2+o(1)}\) at (3), not strict root width. This note proves no concentration about the finite-width mean and no bias estimate. Those remaining bridges must be established independently; they cannot be inferred from (1), (25), or the existence of the dense population.
