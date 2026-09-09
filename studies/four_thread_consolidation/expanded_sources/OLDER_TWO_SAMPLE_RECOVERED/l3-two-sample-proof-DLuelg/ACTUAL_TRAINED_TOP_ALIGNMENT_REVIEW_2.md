# Isolated adversarial review: actual trained top alignment

Date: 2026-09-06.

## Verdict and audit boundary

**The stated structural finite-gradient-flow lemma is correct. I found no required mathematical correction.** For every fixed integer \(n\geq4\) and every \(\tau>0\), the construction gives bounded initial operator norms, exactly zero initial readout, and a physical observation time \(0<t<\tau\) at which the first readout coordinate is positive and its current sample preactivation contrast is negative. The strict event extends to a full-dimensional open set of initial parameters and consequently has positive probability under the prescribed finite Gaussian initialization.

This verdict is limited to that assertion. It establishes neither a mean-field counterexample nor a width-uniform probability or time estimate. It does not certify an activation's population theorem, or the precise hypotheses of an external frozen-top estimate: neither was supplied as an authorized mathematical input. The proof's statements distinguishing the finite lemma from the two-sample population target are appropriate.

Only the following mathematical text was read:

1. The complete [ACTUAL_TRAINED_TOP_ALIGNMENT_TEST.md](/tmp/l3-two-sample-proof-DLuelg/ACTUAL_TRAINED_TOP_ALIGNMENT_TEST.md), 233 lines.
2. The “Target and fixed model” section of [CONTRACT_AND_LEDGER.md](/tmp/l3-two-sample-proof-DLuelg/CONTRACT_AND_LEDGER.md:10), lines 10–81 inclusive, including its heading and final blank line.

I personally read the complete procedural [solve-math-rigorously/SKILL.md](/home/amir/.codex/skills/solve-math-rigorously/SKILL.md). No provenance, research ledger, other mathematical source, previous review, or task history was read. No agents, experiments, or candidate edits were used. The checks below are analytic calculations.

SHA-256 identifiers:

| Source | SHA-256 |
| --- | --- |
| Complete candidate proof | e83eaee5b01c77b1e0a4663af61714aea4d62a4095f2331898ea2d68271d13b9 |
| Authorized contract section only | e633994927965510b9c0605d27ed221b33de485caa7cda2bb9029a6343707d0e |
| Complete procedural skill | 9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7 |

The contract hash is over the extracted section, including its heading and newline after each line. It is deliberately not presented as a hash of the full ledger.

## 1. Activation, inputs, raw metric, and all normalization factors

Write \(w=W^{(4)}\), and use componentwise products for products of two neuron vectors. The activation satisfies

\[
\phi'(z)=1+\frac{e^z}{1+e^z}\in(1,2),\qquad
\phi''(z)=\frac{e^z}{(1+e^z)^2}>0.
\]

It is smooth, strictly convex, and strongly monotone with lower derivative bound 1. Its relevant exact identities are

\[
\phi(z)-\phi(-z)=3z,\qquad
\phi'(z)+\phi'(-z)=3,\qquad \phi'(0)=\frac32.
\]

For the first identity, the difference of the two logarithms is \(z\), while the difference of the two explicit linear terms is \(2z\). There is no approximation of the activation here. Strict monotonicity applied twice gives \(\Delta>0\) and \(E>0\) when \(A>B\) and \(C>D\).

The proposed \(d=2\), \(x_1=\sqrt2 e_1\), \(x_2=\sqrt2 e_2\) satisfy \(\|x_a\|^2/d=1\) and \(C_{ab}=\delta_{ab}\), so \(\rho=0\) is allowed. Dividing the two desired preactivation columns by \(\sqrt2\) gives exactly \(W^{(1)}x_a=z^{(1)}_a\).

The contract metric is

\[
\|\dot\theta\|_{\rm raw}^2
=\frac dn\|\dot W^{(1)}\|_F^2+
 \|\dot W^{(2)}\|_F^2+\|\dot W^{(3)}\|_F^2+
 \frac1n\|\dot w\|_2^2.
\]

The Euclidean derivatives of \(f_a=w^Th^{(3)}_a/n\) have a factor \(1/n\). Inverting the first and last metric blocks gives

\[
\begin{aligned}
(\nabla_{\rm raw}f_a)_{W^{(1)}}&=\frac1d\delta^{(1)}_a x_a^T,\\
(\nabla_{\rm raw}f_a)_{W^{(\ell)}}&=\frac1n\delta^{(\ell)}_a
 (h^{(\ell-1)}_a)^T,\quad \ell=2,3,\\
(\nabla_{\rm raw}f_a)_w&=h^{(3)}_a.
\end{aligned}
\]

Consequently the exact feature-ascent field for \(g=(f_1-f_2)/2\) is

\[
\begin{aligned}
(W^{(1)})'&=\frac1{2d}
  (\delta^{(1)}_1x_1^T-\delta^{(1)}_2x_2^T),\\
(W^{(\ell)})'&=\frac1{2n}
  [\delta^{(\ell)}_1(h^{(\ell-1)}_1)^T-
   \delta^{(\ell)}_2(h^{(\ell-1)}_2)^T],\quad \ell=2,3,\\
w'&=\frac12(h^{(3)}_1-h^{(3)}_2),\\
(z^{(1)}_b)'&=\frac12
  (C_{b1}\delta^{(1)}_1-C_{b2}\delta^{(1)}_2).
\end{aligned}
\]

This verifies the potentially consequential factors: \(1/(2d)\) for first weights, \(1/(2n)\) for hidden matrices, \(1/2\) for readout ascent, and \(1/2\) rather than \(1/(2n)\) in the first preactivation ascent when \(C=I_2\).

As a separate normalization check, taking raw inner products of the displayed gradients yields exactly

\[
K^{(1)}_{ab}=C_{ab}\frac{(\delta^{(1)}_a)^T\delta^{(1)}_b}{n},
\quad
K^{(\ell)}_{ab}=
\frac{(\delta^{(\ell)}_a)^T\delta^{(\ell)}_b}{n}
\frac{(h^{(\ell-1)}_a)^Th^{(\ell-1)}_b}{n},
\quad
K^{(4)}_{ab}=\frac{(h^{(3)}_a)^Th^{(3)}_b}{n}.
\]

Thus \(\dot f_a=-2\sum_b(\sum_\ell K^{(\ell)}_{ab})r_b\), as in the contract. Dividing the raw updates by \(\eta_n\) gives the physical gradient field used here. There is no further factor \(n^{-2}\) to insert into that continuous-time field.

## 2. Exact finite symmetry and the physical clock

Let \(\mathcal S\) denote the parameter transformation in candidate lines 79–82, to distinguish it from the vector \(S=h^{(1)}_1\). Both \(P\) and \(R\) are orthogonal involutions. Left/right multiplication by them preserves each metric block above; the extra sign on \(w\) also preserves its norm.

For arbitrary parameters, forward propagation gives

\[
z^{(\ell)}_a(\mathcal S\theta)
=Pz^{(\ell)}_{3-a}(\theta),\qquad
h^{(\ell)}_a(\mathcal S\theta)
=Ph^{(\ell)}_{3-a}(\theta),
\]

and hence

\[
f_1(\mathcal S\theta)=-f_2(\theta),\qquad
f_2(\mathcal S\theta)=-f_1(\theta).
\]

With labels \((1,-1)\), this exchanges and negates the two residuals. It preserves their squared sum and preserves \(g\).

The proposed initial state is fixed by \(\mathcal S\). The first matrix identity follows by exchanging its two columns and then applying \(P\); the identity matrix commutes with \(P\). Each initially specified third-layer row is antisymmetric under column permutation by \(P\), and the paired row is its negative, so simultaneous row and column permutations restore \(W^{(3)}\). The same check applies after the \(a\)-perturbation.

For a smooth invariant scalar function \(F\) and every perturbation \(v\),

\[
\langle\nabla F(\mathcal S\theta),\mathcal S v\rangle_{\rm raw}
=DF(\mathcal S\theta)[\mathcal S v]
=DF(\theta)[v]
=\langle\mathcal S\nabla F(\theta),\mathcal S v\rangle_{\rm raw}.
\]

Thus both gradient fields are equivariant. They are smooth finite-dimensional fields, so local uniqueness applies. Applying \(\mathcal S\) to a solution with fixed initial data produces the same solution. This establishes exact pathwise symmetry for both flows, not just a symmetry of a random initialization law.

On the fixed subspace,

\[
h^{(\ell)}_2=Ph^{(\ell)}_1,\quad
z^{(\ell)}_2=Pz^{(\ell)}_1,\quad
w=-Pw,\quad f_2=-f_1,\quad g=f_1.
\]

For the backward fields the sign is opposite:

\[
\delta^{(3)}_2=-P\delta^{(3)}_1,\quad
q^{(2)}_2=-Pq^{(2)}_1,\quad
\delta^{(2)}_2=-P\delta^{(2)}_1,
\]

and likewise for \(q^{(1)}\) and \(\delta^{(1)}\). For example,
\(w\phi'(Pz)=-P[w\phi'(z)]\), and the commutation of \(W^{(3)}\) with \(P\) propagates this identity downward. This sign convention agrees with the apparently equal \(q^{(2)}\) derivatives below, since \(P(e_1-e_2)=-(e_1-e_2)\).

The clock factor is an identity of the full ambient gradient, not merely a derivative of the loss restricted to a subspace. At a symmetric state,

\[
\begin{aligned}
-\nabla_{\rm raw}L
&=-2[(g-1)\nabla_{\rm raw}f_1+(1-g)\nabla_{\rm raw}f_2]\\
&=4(1-g)\nabla_{\rm raw}g.
\end{aligned}
\]

Therefore \(dt/ds=[4(1-g)]^{-1}\) is the correct inverse clock. Inverting it gives \(d\theta/dt=-\nabla_{\rm raw}L\). Its positivity on a common short interval is justified quantitatively in Section 7 below. The assertion concerns continuous finite GF, not exact discrete GD at its prescribed mesh.

One distinction matters: the fixed-subspace condition gives sample permutation, but does not generally preserve “row 2 equals minus row 1” or opposite preactivations at a single neuron for all positive times. The proof uses those stronger relations only at initialization. I found no step that illicitly assumes their persistence.

## 3. Initial norm bounds and the neurons beyond the first four

Fix \(A,B,C,D,b\) once, independently of \(n,\tau\), and take \(c=\Delta/E\). For the perturbed family write
\(a_\varepsilon=-1+\varepsilon/\Delta\), with \(0\leq\varepsilon\leq\Delta/2\). Then

\[
\|W^{(1)}\|_F^2=A^2+B^2+C^2+D^2,\qquad
\|W^{(2)}\|_{\rm op}=1,\qquad
\|W^{(2)}\|_F=\sqrt n,
\]

\[
\|W^{(3)}\|_{\rm op}\leq\|W^{(3)}\|_F
=2\sqrt{a_\varepsilon^2+c^2+b^2},\qquad \|w\|=0.
\]

Since \(|a_\varepsilon|\leq1\) on this positive-parameter interval, these give the asserted uniform initial bounds, including the first-matrix operator norm.

For every index \(i>4\), the initial coordinates are

| Layer | \(z^{(\ell)}_{a,i}\) | \(h^{(\ell)}_{a,i}\) |
| --- | --- | --- |
| 1 | \(0\) | \(\log2\) |
| 2 | \(\log2\) | \(\log6\) |
| 3 | \(0\) | \(\log2\) |

The first four coordinates also lie in fixed bounded sets: the top ones are \((\varepsilon,-\varepsilon,b\Delta,-b\Delta)\) for sample 1 and their permutation for sample 2. A uniform coordinate bound gives each asserted vector norm divided by \(\sqrt n\). No bound on the full raw parameter norm independent of \(n\) is needed or valid for \(W^{(2)}=I_n\).

The extra coordinates must still be retained in inner products. Put \(s_i=S_i\) and \(\gamma=\log2\). Exactly,

\[
g_1=\frac{s_1^2+s_2^2+s_3^2+s_4^2+(n-4)\gamma^2}{n},
\qquad
h_1=\frac{2s_1s_2+2s_3s_4+(n-4)\gamma^2}{n}.
\]

Thus

\[
g_1-h_1
=\frac{(s_1-s_2)^2+(s_3-s_4)^2}{n}
=\frac{\|S-T\|^2}{2n}>0.
\]

The tails add to the \(J\)-bracket the term

\[
\frac{n-4}{n}\gamma^2(P_1-P_2)^2.
\]

It is nonnegative and is already included in the candidate's \(g_1,h_1\). In particular, the candidate has not replaced an \(n\)-neuron calculation by a four-neuron one.

There are nonzero tail-column entries of the second-matrix acceleration even at the base state:

\[
(W^{(2)})''_{1j}=(W^{(2)})''_{2j}
=\frac{Q\gamma}{2n}(P_1-P_2),\qquad j>4.
\]

These are compatible with all rows numbered at least 3 of \((W^{(2)})''\) vanishing at the base state. The proof asserts a row statement, not a column statement. The subsequent feature calculation correctly accounts for these columns.

All these identities include \(n=4\), when the tail terms are absent. No argument needs a fifth neuron.

## 4. Independent base-state derivative calculation

All derivatives in this and the next section are feature-time derivatives at \(s=0\).

Since \(w=0\), all residual-free backward fields vanish, so every hidden parameter and hidden feature has zero first derivative. Only the readout moves initially:

\[
w'=V=(0,0,v,-v,0,\ldots,0),\qquad
v=\frac32b\Delta>0.
\]

Let \(r=\phi'(b\Delta)\), \(l=\phi'(-b\Delta)\). Differentiating \(\delta^{(3)}=w\phi'(z^{(3)})\) gives

\[
(\delta^{(3)}_1)'=(0,0,vr,-vl,0,\ldots),\qquad
(\delta^{(3)}_2)'=(0,0,vl,-vr,0,\ldots).
\]

The terms involving \(w\) or \(W^{(3)\prime}\) vanish. Multiplication by the initial \(W^{(3)T}\) therefore yields

\[
(q^{(2)}_1)'=(q^{(2)}_2)'=bv(r+l)(e_1-e_2)=Q(e_1-e_2).
\]

Here \(r+l=3\), so \(Q=3bv=(9/2)b^2\Delta>0\), with no hidden width factor.

Writing \(p_i=\phi'(S_i)\) and \(u_i=\phi'(z^{(1)}_{1,i})\), the candidate's \(P_i,U_i\), gives

\[
d_1:=(\delta^{(2)}_1)'=Q(p_1,-p_2,0,\ldots),\qquad
d_2:=(\delta^{(2)}_2)'=Q(p_2,-p_1,0,\ldots).
\]

Since \(q^{(1)\prime}=\delta^{(2)\prime}\) at \(W^{(2)}=I\), the first-layer derivatives are

\[
(z^{(1)}_1)''=\tfrac12u\,d_1,\qquad
(z^{(1)}_2)''=-\tfrac12(Pu)\,d_2,\qquad
(h^{(1)}_1)''=\tfrac12u^2d_1.
\]

Differentiating the exact second-matrix ascent gives

\[
(W^{(2)})''=\frac1{2n}(d_1S^T-d_2T^T).
\]

In \(z^{(2)}_1=W^{(2)}h^{(1)}_1\), the mixed first-derivative product vanishes. Therefore

\[
(z^{(2)}_1)''
=\tfrac12(g_1d_1-h_1d_2)+\tfrac12u^2d_1,
\qquad
(h^{(2)}_1)''=p\,(z^{(2)}_1)''.
\]

Explicitly, its first two entries are

\[
\begin{aligned}
(h^{(2)}_{1,1})''&=\frac Q2
[g_1p_1^2-h_1p_1p_2+p_1^2u_1^2],\\
(h^{(2)}_{1,2})''&=\frac Q2
[-g_1p_2^2+h_1p_1p_2-p_2^2u_2^2].
\end{aligned}
\]

Their difference is exactly the displayed \(J\) in candidate (3). The matrix-dependent part of its bracket is

\[
g_1(p_1-p_2)^2+2(g_1-h_1)p_1p_2>0.
\]

The first-layer contribution \(p_1^2u_1^2+p_2^2u_2^2\) is also strictly positive. Thus \(J>0\), without assuming a sign for \(h_1\). In particular, the positive first-layer term is not suppressed by \(1/n\).

All entries of \((h^{(2)}_1)''\) with index at least 3 vanish at this base point: \(d_1,d_2\) have support only in the first pair, so both terms in the last feature-acceleration formula have that support. The second sample's acceleration is its permutation.

For the first third-matrix row \(m\), the exact ascent formula is

\[
m'=\frac{w_1}{2n}
\left[\phi'(z^{(3)}_{1,1})(h^{(2)}_1)^T
-\phi'(z^{(3)}_{2,1})(h^{(2)}_2)^T\right].
\]

At the base point both \(w_1\) and \(w_1'\) vanish, so \(m'=m''=0\). Consequently, for
\(D_1=(z^{(3)}_{1,1}-z^{(3)}_{2,1})/2\),

\[
D_1''=\tfrac12m[(h^{(2)}_1)''-P(h^{(2)}_1)'']
=a[(h^{(2)}_{1,1})''-(h^{(2)}_{1,2})'']
=-J.
\]

The factor \(1/2\) in the contrast cancels the factor 2 from subtracting the permuted acceleration. This confirms candidate (4).

Finally, \(w_1''=0\) because the hidden first velocities vanish, and

\[
w_1'''=\frac{\phi'(0)}2
[(z^{(3)}_{1,1})''-(z^{(3)}_{2,1})'']
=-\frac32J.
\]

Dividing this third derivative by \(3!=6\) gives the coefficient \(-J/4\) in the readout Taylor expansion.

The other third-matrix rows are not being frozen. For example,

\[
(W^{(3)})''_{3,:}=\frac v{2n}(rH-lPH)^T\ne0.
\]

Its nonzero contrast follows from \((r+l)\Delta>0\). Both lower blocks also have nonzero accelerations, and \(w'\ne0\). The source of the negative \(D_1''\) is therefore an actual trajectory of the fully trained system.

## 5. Perturbed second and third derivatives, including row training

The proof invokes smooth dependence for these terms. An explicit calculation confirms what that argument must include.

Set

\[
a_\varepsilon=-1+\varepsilon/\Delta,\quad
m_\varepsilon=a_\varepsilon(e_1-e_2)^T+c(e_3-e_4)^T,\quad
\nu=\frac32\varepsilon,\quad \kappa=3\nu=\frac92\varepsilon,
\]

\[
\alpha=\phi'(\varepsilon),\qquad
\beta=\phi'(-\varepsilon),\qquad \alpha+\beta=3.
\]

The initial first top preactivations are exactly \((\varepsilon,-\varepsilon)\), so \(D_1(0)=\varepsilon\), \(w_1'(0)=\nu\). All hidden first velocities and \(w_1''(0)\) remain zero.

The two additional readout derivatives at neurons 1 and 2 give the exact perturbed identity

\[
(q^{(2)}_1)'=(q^{(2)}_2)'
=Q(e_1-e_2)+\kappa m_\varepsilon^T
=(Q+\kappa a_\varepsilon)(e_1-e_2)
 +\kappa c(e_3-e_4).
\]

Thus the previously zero third and fourth lower-feature accelerations generally become \(O(\varepsilon)\). They must not be set to zero in a perturbed calculation.

Extend \(p_i,u_i\) above to \(i=1,\ldots,4\), and define the fixed-in-\(\varepsilon\) brackets

\[
\mathcal B_{ij}
=g_1(p_i^2+p_j^2)-2h_1p_ip_j+p_i^2u_i^2+p_j^2u_j^2,
\qquad (i,j)=(1,2),(3,4).
\]

Applying the same second-layer formula to each pair gives exactly

\[
\begin{aligned}
\mathcal J_{12}
&:=(h^{(2)}_{1,1})''-(h^{(2)}_{1,2})''
=\frac{Q+\kappa a_\varepsilon}{2}\mathcal B_{12},\\
\mathcal J_{34}
&:=(h^{(2)}_{1,3})''-(h^{(2)}_{1,4})''
=\frac{\kappa c}{2}\mathcal B_{34}.
\end{aligned}
\]

Here \(J=(Q/2)\mathcal B_{12}\). All entries beyond the first four of this feature acceleration are still zero at the initial instant, though there is no assertion that the lower tail stays fixed later.

Let

\[
G=\|H\|^2/n,\qquad K=H^TPH/n.
\]

The first third-matrix row now has the nonzero acceleration

\[
m_\varepsilon''=\frac{\nu}{2n}(\alpha H-\beta PH)^T.
\]

Its contribution to the contrast acceleration is

\[
\frac12m_\varepsilon''(H-PH)
=\frac{3\nu}{4}(G-K).
\]

Therefore the complete perturbed second derivative is

\[
D_{1,\varepsilon}''(0)
=a_\varepsilon\mathcal J_{12}+c\mathcal J_{34}
 +\frac{3\nu}{4}(G-K)
=-J+O_n(\varepsilon).
\]

The three terms respectively account for the first lower pair, the newly accelerated second lower pair, and training of the first third-matrix row. In particular, the candidate's \(O(\varepsilon)\) includes more than the change of \(a\).

For the extra-neuron check,

\[
G-K=\frac{\Delta^2+E^2}{n}.
\]

The tail therefore cancels from this row-induced contrast term. It does not cancel from all row effects: for \(j>4\),

\[
(m_\varepsilon'')_j=
\frac{\nu(\alpha-\beta)\log6}{2n}.
\]

These entries are \(O(\varepsilon^2/n)\), since \(\alpha-\beta=O(\varepsilon)\).

To check the readout third derivative without incorrectly imposing opposite top preactivations for positive time, introduce the top mean

\[
M_1=(z^{(3)}_{1,1}+z^{(3)}_{2,1})/2.
\]

The lower-feature contribution to \(M_1''(0)\) vanishes because \(m_\varepsilon P=-m_\varepsilon\). The row contribution is

\[
M_{1,\varepsilon}''(0)
=\frac{\nu}{4}(\alpha-\beta)(G+K)=O_n(\varepsilon^2).
\]

It follows exactly that

\[
\begin{aligned}
w_{1,\varepsilon}'''(0)
&=\frac{\alpha+\beta}{2}D_{1,\varepsilon}''(0)
 +\frac{\alpha-\beta}{2}M_{1,\varepsilon}''(0)\\
&=\frac32D_{1,\varepsilon}''(0)
 +\frac{\nu}{8}(\alpha-\beta)^2(G+K)\\
&=-\frac32J+O_n(\varepsilon).
\end{aligned}
\]

The mean correction is actually \(O_n(\varepsilon^3)\); the weaker stated error is sufficient. This verifies the perturbed cubic coefficient while retaining all common-mode and tail effects.

There is also an exact consistency check on the hidden third derivatives. Write all hidden parameters as \(X\). Feature ascent has the form \(X'=A(X)w,\ w'=B(X)\), with smooth functions \(A,B\). Starting from \(w=0\) gives \(X'=0,\ w''=DB(X)X'=0\), and differentiating \(X'\) twice gives \(X'''(0)=0\). Since hidden features depend only on \(X\), their third derivatives at zero vanish too, at both the base and perturbed states. The candidate's less sharp remainders remain valid; no missing cubic hidden term is needed.

## 6. Taylor bounds and their quantifiers

The necessary local existence and remainder argument is finite-dimensional and does not require any width-uniform smooth-flow theorem.

For fixed \(n\), the parameter space is \(\mathbb R^{2n^2+3n}\). The raw metric is a fixed positive-definite metric there. Both the feature and physical vector fields are \(C^\infty\) on that whole space. The initial state depends affinely on \(\varepsilon\).

Here is the precise local ODE fact needed: a \(C^1\) vector field is bounded and Lipschitz on a sufficiently small closed ball; initial states in a smaller concentric ball have unique solutions on a common time interval that remain in the larger ball. Their differences are bounded by their initial difference times \(e^{Ls}\), where \(L\) bounds the derivative of the field on that ball. If the field is \(C^\infty\), the time derivatives needed for any fixed Taylor order are bounded on a still smaller common interval.

These hypotheses hold here because closed bounded balls are compact in the fixed finite parameter dimension, and every relevant derivative is continuous. More concretely, choose radius \(R>0\) about the base state, place all sufficiently small-\(\varepsilon\) initial states in its \(R/4\) ball, and let \(M_n,L_n\) bound the field and its first derivative on the closed \(R\) ball. An interval of length at most \(R/[4(1+M_n)]\) keeps those trajectories inside the \(R/2\) ball by the integral equation and a first-exit argument. The difference estimate follows from

\[
\|\theta_\varepsilon(s)-\theta_0(s)\|
\leq\|\theta_\varepsilon(0)-\theta_0(0)\|
+L_n\int_0^s\|\theta_\varepsilon(u)-\theta_0(u)\|\,du.
\]

Higher time derivatives are finite compositions of derivatives of the smooth field and smooth observations on this compact set. This gives the required uniform-in-\(\varepsilon\) Taylor constants. No bound on the full parameter norm independent of \(n\) is being assumed.

Precisely, for each fixed \(n\) there exist \(\varepsilon_{0,n}>0\), \(s_{0,n}>0\), and finite \(C_{D,n},C_{w,n}\) such that, for all \(0\leq\varepsilon\leq\varepsilon_{0,n}\) and \(0\leq s\leq s_{0,n}\),

\[
\left|D_{1,\varepsilon}(s)-\varepsilon+\frac J2s^2\right|
\leq C_{D,n}(\varepsilon s^2+s^3),
\]

\[
\left|w_{1,\varepsilon}(s)-\frac32\varepsilon s+\frac J4s^3\right|
\leq C_{w,n}(\varepsilon s^3+s^4).
\]

The first estimate uses \(D'(0)=0\), \(D''(0)=-J+O_n(\varepsilon)\), and a uniformly bounded third time derivative. The second uses \(w(0)=0\), \(w'(0)=3\varepsilon/2\), \(w''(0)=0\), the checked third derivative, and a uniformly bounded fourth time derivative. Smoothness supplies each of these bounds.

“Uniformly for small \(s,e\)” in candidate line 195 is therefore justified with \(n\) held fixed, as stated in lines 176–177. Reading it as width-uniform would go beyond the proof; that stronger reading is unnecessary for the lemma.

## 7. Strict sign reversal and arbitrarily short physical times

Fix \(n\), hence \(J=J_n>0\), and set \(s_\varepsilon=2\sqrt{\varepsilon/J}\). Choose \(\varepsilon\) small enough that this lies in the preceding common interval. Direct substitution gives

\[
D_{1,\varepsilon}(s_\varepsilon)
=-\varepsilon+R_D,\qquad
|R_D|\leq C_{D,n}
\left(\frac{4\varepsilon^2}{J}
 +\frac{8\varepsilon^{3/2}}{J^{3/2}}\right),
\]

\[
w_{1,\varepsilon}(s_\varepsilon)
=\frac{\varepsilon^{3/2}}{\sqrt J}+R_w,\qquad
|R_w|\leq C_{w,n}
\left(\frac{8\varepsilon^{5/2}}{J^{3/2}}
 +\frac{16\varepsilon^2}{J^2}\right).
\]

After division by \(\varepsilon\) in the first estimate and by \(\varepsilon^{3/2}/\sqrt J\) in the second, both relative errors tend to zero. In particular, for every sufficiently small positive \(\varepsilon\),

\[
D_{1,\varepsilon}(s_\varepsilon)\leq-\varepsilon/2<0,\qquad
w_{1,\varepsilon}(s_\varepsilon)
\geq\frac{\varepsilon^{3/2}}{2\sqrt J}>0.
\]

Since the original contrast is \(2D_1\), these are exactly the desired inequalities, with the same signs.

The positive initial derivative \(w_1'(0)=3\varepsilon/2\), together with \(D_1(0)=\varepsilon\), already ensures an earlier interval of strict alignment. As an explicit check, at \(s=s_\varepsilon/2\),

\[
D_{1,\varepsilon}(s)=\frac{\varepsilon}{2}
 +O_n(\varepsilon^{3/2})>0,\qquad
w_{1,\varepsilon}(s)=\frac54\frac{\varepsilon^{3/2}}{\sqrt J}
 +O_n(\varepsilon^2)>0.
\]

Thus the readout begins by moving in the agreeing direction and later has a strictly opposite current contrast. The construction does not merely produce a negative contrast with a zero readout.

For the clock, along feature ascent

\[
g'(s)=\|\nabla_{\rm raw}g(\theta_\varepsilon(s))\|_{\rm raw}^2\geq0,
\qquad g(0)=0.
\]

On the common compact neighborhood the right-hand side has a finite bound for fixed \(n\). Shrinking the common interval therefore ensures \(0\leq g\leq1/2\) for all the small-\(\varepsilon\) trajectories. Consequently

\[
\frac14\leq\frac{dt}{ds}\leq\frac12,\qquad
\frac{s_\varepsilon}{4}\leq t_\varepsilon\leq
\frac{s_\varepsilon}{2}=\sqrt{\varepsilon/J}.
\]

Thus \(t_\varepsilon>0\) and \(t_\varepsilon\to0\). Taking \(\varepsilon<J\tau^2\), as well as all the previous smallness conditions, gives \(t_\varepsilon<\tau\).

This has the required quantifier order:

\[
\forall n\geq4\ \forall\tau>0\
\exists\varepsilon=\varepsilon(n,\tau)>0\
\exists t_\varepsilon\in(0,\tau).
\]

The initial states vary with \(\varepsilon\). There is no assertion that the bad times accumulate at zero along one fixed trajectory. The fixed upper bound \(\varepsilon\leq\Delta/2\) used for initial norm control is compatible with every subsequent smallness choice.

## 8. Full physical-flow neighborhood and Gaussian probability

Fix \(n\) and one admissible positive \(\varepsilon\), and then fix the physical time \(t_\varepsilon\) just obtained. At that time the two strict margins above hold.

For the physical vector field \(F_{\rm phys}=-\nabla_{\rm raw}L\), the reference trajectory on \([0,t_\varepsilon]\) is compact and lies inside a region where the field is smooth. A bounded derivative on a slightly larger compact neighborhood, the integral equation, and the same difference estimate give a neighborhood of its initial state whose solutions all exist to \(t_\varepsilon\) and depend continuously on all initial coordinates there. The maps

\[
\theta_{\rm init}\longmapsto
w_1(t_\varepsilon;\theta_{\rm init}),\qquad
\theta_{\rm init}\longmapsto
z^{(3)}_{1,1}(t_\varepsilon;\theta_{\rm init})
-z^{(3)}_{2,1}(t_\varepsilon;\theta_{\rm init})
\]

are consequently continuous. Their strict inequalities define an open set containing the deterministic initial state. It contains an ordinary ball in the full \(\mathbb R^{2n^2+3n}\) parameter space.

This step uses the physical loss flow after perturbing arbitrary initial weights. It does not assume that nonsymmetric neighbors have \(f_2=-f_1\) or share the reference feature clock.

For this fixed \(n\), the contract initialization has independent entries of positive variances \(1/2\), \(1/n\), \(1/n\), and \(1/n^2\) in its four blocks. Its joint density is continuous and strictly positive at every finite parameter vector. A closed ball of positive radius contained in the open event has a positive minimum density and positive Lebesgue volume. Hence the event has strictly positive probability.

The exactly symmetric zero-readout center itself has probability zero, which does not affect this argument. The intersection of the open event with the union of the readout-coordinate hyperplanes has probability zero; thus the Gaussian conclusion includes an almost surely nonzero random readout. It does not assert exact zero readout or exact symmetry for the random realization.

The radius of the open set and its probability may depend on both \(n\) and \(\varepsilon\), and may become arbitrarily small. No lower bound uniform in width or proximity to zero time follows. The proof makes no such claim.

## 9. Required corrections and optional presentation

### Required mathematical corrections

None for the stated structural finite-GF lemma. I found no missing normalization, invalid finite-symmetry argument, unaccounted \(n>4\) contribution, erroneous derivative, insufficient fixed-width Taylor estimate, sign failure, or gap in the physical-flow Gaussian-open-set conclusion.

In particular, the following would have been substantive errors, but are not present: freezing the first third-matrix row after perturbation; setting the perturbed third/fourth lower-feature accelerations to zero; using \(w'_1=(3/2)D_1\) as an exact identity for the whole future path; importing the feature clock to nonsymmetric neighbors; or claiming a width-uniform probability from full support.

### Optional presentation improvements

1. After introducing feature ascent, display its four raw block updates. This makes the \(1/(2d)\), \(1/(2n)\), and readout \(1/2\) factors directly inspectable.
2. Make the fixed-\(n\) convention explicit beside the two Taylor \(O\)-terms, and impose one fixed upper bound such as \(0<e\leq\Delta/2\) when describing the bounded family.
3. Add one sentence distinguishing preserved sample permutation from the initial opposite-row/opposite-preactivation relations. The latter generally cease to hold.
4. If a more explicit perturbation check is desired, display the first-row acceleration \(m_e''=\nu(\alpha H-\beta PH)^T/(2n)\) and mention the \(O(e)\) acceleration in the second lower pair. The current smooth-dependence argument already covers both.
5. A sentence such as \(s_e/4\leq t_e\leq s_e/2\) on \(0\leq g\leq1/2\) would make the arbitrary-\(\tau\) conclusion immediate.
6. Keep any statements about an external frozen-top estimate conditional on that estimate actually requiring the universal alignment premise disproved here. The permitted inputs are sufficient for the structural lemma, not for auditing an unseen theorem's full hypothesis set.

These are presentation and scope-precision suggestions, not conditions for validity of the finite trajectory construction.
