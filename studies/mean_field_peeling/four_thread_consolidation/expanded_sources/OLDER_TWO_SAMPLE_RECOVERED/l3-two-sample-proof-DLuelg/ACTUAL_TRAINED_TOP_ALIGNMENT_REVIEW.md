# Independent adversarial audit: actual trained top misalignment

Date: 2026-09-06.

## Verdict and scope

**The finite-trajectory construction passes.** For every fixed integer \(n\geq4\) and every prescribed positive time bound, the proposed family contains a zero-readout initialization whose actual, fully trained loss gradient flow has \(W^{(4)}_1>0\) and \(z^{(3)}_{1,1}-z^{(3)}_{2,1}<0\) before that bound. For a sufficiently small fixed perturbation, the trajectory initially has positive contrast and positive readout, then loses that alignment. At the resulting fixed physical observation time, strict misalignment persists on an open set of all initial parameters, which has positive probability under the specified finite Gaussian law.

I found no incorrect normalization, derivative, Taylor coefficient, circular symmetry premise, or failure of the strict-sign or Gaussian-neighborhood argument. Two statement precisions are required: the initialization depends on the requested small observation time, and the claimed uniform primal bounds must specify normalized vector norms and matrix operator norms. Uniform boundedness in the full raw parameter metric would be false. These issues and optional presentation changes are separated below.

This verdict concerns a structural finite-width, finite-trajectory lemma. It establishes neither a mean-field impossibility result nor a probability bound uniform in width. No population theorem, continuation estimate, or research-ledger claim was used or audited.

## Inputs, isolation, and hashes

The only mathematical inputs were:

- `/tmp/l3-two-sample-proof-DLuelg/ACTUAL_TRAINED_TOP_ALIGNMENT_TEST.md`, all 217 lines.
- `/tmp/l3-two-sample-proof-DLuelg/CONTRACT_AND_LEDGER.md`, lines 10–81, the section headed `Target and fixed model`, including the exact network, raw updates, metric, physical-time definition, and kernels. No authority/provenance discussion, claim ledger, research-cycle results, or other project mathematics or reviews were read.

The requested procedural skill was read in full by the reviewing assistant:
`/home/amir/.codex/skills/solve-math-rigorously/SKILL.md`.
No agents, experiments, numerical calculations, symbolic-computation programs, or outside mathematical sources were used. File reads, boundary identification, hashing, and writing this report were the only tool-assisted operations.

SHA-256 hashes of the reviewed input snapshot:

```text
466f93f48fda1b5ff3d1905e7b0d45b26b171ce1494cb5e0b811c7e58326a8f1
  ACTUAL_TRAINED_TOP_ALIGNMENT_TEST.md (whole file)

1461e507927317e77c481bc1a51931f1e676c6473af410a48c858715da481218
  CONTRACT_AND_LEDGER.md (whole-file integrity hash only)

e633994927965510b9c0605d27ed221b33de485caa7cda2bb9029a6343707d0e
  CONTRACT_AND_LEDGER.md, exact bytes emitted by sed -n '10,81p'

9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7
  solve-math-rigorously/SKILL.md
```

References to candidate line numbers below refer to this hashed version. The candidate and contract were not edited. Their whole-file hashes and the permitted contract-section hash were rechecked after report creation and matched the values above.

## 1. Activation, metric, and every normalization

Write \(w=W^{(4)}\), \(g=(f_1-f_2)/2\), and let primes denote ascent in the feature parameter \(s\): \(\theta'=\operatorname{grad}_{\rm raw}g\). Physical loss-flow time is denoted by \(t\). Products of vectors in backward definitions are componentwise.

For \(\sigma(z)=e^z/(1+e^z)\), direct differentiation gives

\[
\phi'(z)=1+\sigma(z),\qquad
\phi''(z)=\sigma(z)(1-\sigma(z))>0,\qquad
\phi'''(z)=\sigma(z)(1-\sigma(z))(1-2\sigma(z)).
\]

Thus \(\phi\) is smooth, strictly convex, and strongly monotone, with \(1<\phi'<2\). In particular,

\[
\phi(0)=\log2,\quad \phi'(0)=\tfrac32,\quad
\phi''(0)=\tfrac14,\quad \phi'''(0)=0.
\]

The identity \(1+e^z=e^z(1+e^{-z})\) gives

\[
\phi(z)-\phi(-z)=3z,\qquad
\phi'(z)+\phi'(-z)=3.
\]

The contract's squared raw norm of a parameter increment is exactly

\[
\|d\theta\|_{\rm raw}^2
=\frac dn\|dW^{(1)}\|_F^2
+\|dW^{(2)}\|_F^2+\|dW^{(3)}\|_F^2
+\frac1n\|dw\|_2^2.
\]

Since the Euclidean first-weight gradient of \(g\) is

\[
\frac1{2n}
\bigl(\delta^{(1)}_1x_1^T-\delta^{(1)}_2x_2^T\bigr),
\]

inverting its metric multiplies this by \(n/d\). The complete feature field is therefore

\[
\begin{aligned}
(W^{(1)})'&=\frac1{2d}
 (\delta^{(1)}_1x_1^T-\delta^{(1)}_2x_2^T),\\
(W^{(\ell)})'&=\frac1{2n}
 (\delta^{(\ell)}_1(h^{(\ell-1)}_1)^T
 -\delta^{(\ell)}_2(h^{(\ell-1)}_2)^T),\quad \ell=2,3,\\
w'&=\frac12(h^{(3)}_1-h^{(3)}_2),\\
(z^{(1)}_b)'&=\frac12
 (C_{b1}\delta^{(1)}_1-C_{b2}\delta^{(1)}_2).
\end{aligned}
\]

In particular, \(C=I_2\) gives coefficients \(+1/2\) and \(-1/2\) for the two first-layer preactivation updates. There is no additional factor \(1/n\) in these updates. The factors \(1/n\) in the two hidden-matrix updates are present, and the readout factor \(1/n\) in the prediction cancels against its inverse metric.

As an independent algebraic check, the raw gradients of \(f_a\) in these blocks are respectively

\[
\delta^{(1)}_ax_a^T/d,\quad
\delta^{(\ell)}_a(h^{(\ell-1)}_a)^T/n,\quad
h^{(3)}_a.
\]

Their raw inner products are precisely the contract's \(K^{(1)}_{ab}\), \(K^{(2)}_{ab}\), \(K^{(3)}_{ab}\), and \(K^{(4)}_{ab}\). Hence physical loss descent gives

\[
\dot f_a=-2\sum_b r_b\sum_{\ell=1}^4K^{(\ell)}_{ab},
\]

with the stated loss-sum normalization. No learning-rate or physical-time factor has been absorbed into \(s\) silently.

## 2. The \(n\geq4\) initialization and what is bounded

For \(d=2\), \(x_1=\sqrt2e_1\), \(x_2=\sqrt2e_2\), assigning the two columns of \(W^{(1)}\) to the two specified first-preactivation vectors divided by \(\sqrt2\) realizes them exactly. The normalized input Gram matrix is \(I_2\). With \(W^{(2)}=I_n\), the first two feature layers are exactly \(S,T=PS\) and \(H,PH\) as stated. Strict monotonicity of \(\phi\circ\phi\) gives \(\Delta>0\) and \(E>0\), so neither \(c=\Delta/E\) nor the perturbation \(\varepsilon/\Delta\) has a zero denominator.

Let \(u=- (e_1-e_2)+c(e_3-e_4)\). Then

\[
u^TH=-\Delta+cE=0,\qquad u^TPH=-u^TH=0.
\]

The third and fourth top preactivations are \(b\Delta,-b\Delta\) on sample 1 and their reverse on sample 2. All later top preactivations are zero. This verifies every initial top coordinate and

\[
V=w'(0)=(0,0,v,-v,0,\ldots,0),\qquad
v=\frac32b\Delta>0.
\]

The embedding does not silently discard the later neurons. Their initial first-layer activations are \(\log2\), and their second-layer activations are

\[
\phi(\log2)=\log6.
\]

They therefore contribute to normalized inner products, even though they have zero initial preactivations at the first and third layers. Write \(S=(s_A,s_B,s_C,s_D,s_0,\ldots,s_0)\), with \(s_0=\log2\). Then

\[
\begin{aligned}
g_1&=\frac{s_A^2+s_B^2+s_C^2+s_D^2+(n-4)s_0^2}{n},\\
h_1&=\frac{2s_As_B+2s_Cs_D+(n-4)s_0^2}{n},\\
g_1-h_1&=\frac{(s_A-s_B)^2+(s_C-s_D)^2}{n}>0.
\end{aligned}
\]

These are the inner products actually used in the proof. No invariant four-neuron subsystem is needed: later columns of matrix updates can become nonzero during training.

The displayed initial matrices satisfy a width-independent bound on \(\|W^{(1)}\|_F\), \(\|W^{(2)}\|_{\rm op}=1\), and \(\|W^{(3)}\|_{\rm op}\), with \(w=0\). The initial hidden vectors have bounded coordinates and bounded empirical norms \(\|h^{(\ell)}_a\|_2/\sqrt n\) and \(\|z^{(\ell)}_a\|_2/\sqrt n\). These facts persist for the family of initial states with \(\varepsilon\) in a fixed sufficiently small interval. However, \(\|W^{(2)}\|_F=\sqrt n\), and unnormalized hidden activation norms generally also grow like \(\sqrt n\). This distinction is a statement issue, not an error in the dynamics.

## 3. Exact sample/label symmetry and actual physical time

Use \(\mathcal S\) for the parameter transformation in candidate lines 68–71, reserving \(S\) for the first-layer feature vector. Both \(P\) and the input-coordinate exchange \(R\) are orthogonal involutions. The transformation is an isometry of every block of the raw metric.

The initial first matrix satisfies \(PW^{(1)}R=W^{(1)}\). The second matrix commutes with \(P\). Every displayed nonzero third-matrix row is odd under right multiplication by \(P\), while left multiplication exchanges it with its negative partner. Hence \(PW^{(3)}P^T=W^{(3)}\). The zero readout satisfies \(w=-Pw\). Replacing \(a\) by \(-1+\varepsilon/\Delta\) preserves these identities.

For arbitrary parameters, not just fixed points of \(\mathcal S\), forward propagation gives

\[
f_a(\mathcal S\theta)=-f_{3-a}(\theta).
\]

Consequently \(g(\mathcal S\theta)=g(\theta)\), and, using the actual fixed labels \(y=(1,-1)\),

\[
L(\mathcal S\theta)
=(-f_2-1)^2+(-f_1+1)^2
=(f_2+1)^2+(f_1-1)^2=L(\theta).
\]

If a differentiable scalar function is invariant under a linear metric isometry, differentiating its invariance in an arbitrary parameter direction \(\xi\) gives

\[
\langle\operatorname{grad}g(\mathcal S\theta),\mathcal S\xi\rangle
=\langle\operatorname{grad}g(\theta),\xi\rangle,
\]

and therefore \(\operatorname{grad}g(\mathcal S\theta)=\mathcal S\operatorname{grad}g(\theta)\). The same holds for \(L\). Smooth finite-dimensional fields are locally Lipschitz. Thus \(\mathcal S\theta(s)\) and \(\theta(s)\) solve the same initial-value problem when the initial state is fixed, and uniqueness preserves the fixed-point subspace. This is pathwise symmetry; it uses no distributional symmetry claim.

On that subspace,

\[
z^{(\ell)}_2=Pz^{(\ell)}_1,\quad
h^{(\ell)}_2=Ph^{(\ell)}_1,\quad
w=-Pw,\quad f_2=-f_1,
\]

so \(f_1=g\), \(r_1=g-1\), and \(r_2=1-g\). Taking the full ambient gradient, rather than differentiating only a restricted scalar identity, yields

\[
-\operatorname{grad}_{\rm raw}L
=-2[(g-1)\operatorname{grad}f_1+(1-g)\operatorname{grad}f_2]
=4(1-g)\operatorname{grad}_{\rm raw}g.
\]

This proves the exact field identity needed for the clock. Along the symmetric feature solution, \(g(0)=0\); continuity gives a short interval on which \(1-g>0\). Define

\[
t(s)=\int_0^s\frac{du}{4(1-g(u))}.
\]

Its derivative is positive. Composing the feature trajectory with its inverse gives

\[
\frac{d\theta}{dt}
=\theta'(s)\frac{ds}{dt}
=4(1-g(s))\operatorname{grad}_{\rm raw}g(\theta(s))
=-\operatorname{grad}_{\rm raw}L(\theta(s)).
\]

This is the contract's actual finite GF, with the vector field normalized as the raw increment divided by \(\eta_n\). No discrete-to-continuous limit or externally prescribed forcing is needed for this trajectory argument.

One wording qualification: forward sample fields are permuted by \(P\), but residual-free backward fields satisfy

\[
\delta^{(\ell)}_2=-P\delta^{(\ell)}_1,\qquad
q^{(\ell)}_2=-Pq^{(\ell)}_1.
\]

The readout supplies the additional minus sign. The candidate's displayed backward calculations are consistent with this.

## 4. Base-state derivatives through third order

All derivatives in this section are evaluated at \(s=0\), with \(\varepsilon=0\). Every hidden parameter velocity vanishes because each hidden gradient contains \(w=0\). Thus all first hidden-field velocities also vanish, and differentiating a composite activation twice gives only \((h^{(\ell)}_a)''=\phi'(z^{(\ell)}_a)(z^{(\ell)}_a)''\); all terms involving \(((z^{(\ell)}_a)')^2\) vanish.

### Backward derivatives and the first two trainable layers

Put \(r=\phi'(b\Delta)\), \(l=\phi'(-b\Delta)\), so \(r+l=3\). Since \(w=0\),

\[
(\delta^{(3)}_1)'=(0,0,vr,-vl,0,\ldots),\qquad
(\delta^{(3)}_2)'=(0,0,vl,-vr,0,\ldots).
\]

In differentiating \(q^{(2)}_a=(W^{(3)})^T\delta^{(3)}_a\), the derivative of \(W^{(3)}\) contributes nothing. Multiplying the two nonzero rows gives, for both samples,

\[
(q^{(2)}_a)'=bv(r+l)(e_1-e_2)=Q(e_1-e_2),\qquad
Q=3bv=\frac92b^2\Delta>0.
\]

For \(i=1,2\), let \(P_i=\phi'(S_i)\), \(U_i=\phi'(z^{(1)}_{1,i})\). These symbols are scalar derivatives; \(P_i\) is not a matrix entry of the permutation. It follows that

\[
\begin{aligned}
(\delta^{(2)}_1)'&=Q(P_1,-P_2,0,\ldots),\\
(\delta^{(2)}_2)'&=Q(P_2,-P_1,0,\ldots),\\
(\delta^{(1)}_1)'&=Q(U_1P_1,-U_2P_2,0,\ldots),\\
(\delta^{(1)}_2)'&=Q(U_2P_2,-U_1P_1,0,\ldots).
\end{aligned}
\]

Here \(q^{(1)}_a{}'=(\delta^{(2)}_a)'\) because \(W^{(2)}=I\). The correctly metrized first-layer accelerations are therefore

\[
\begin{aligned}
(z^{(1)}_1)''&=\frac Q2(U_1P_1,-U_2P_2,0,\ldots),\\
(z^{(1)}_2)''&=\frac Q2(-U_2P_2,U_1P_1,0,\ldots),\\
(h^{(1)}_1)''&=\frac Q2(U_1^2P_1,-U_2^2P_2,0,\ldots).
\end{aligned}
\]

The matrix acceleration is

\[
(W^{(2)})''=\frac1{2n}
[(\delta^{(2)}_1)'S^T-(\delta^{(2)}_2)'T^T].
\]

The product rule for \(z^{(2)}_1=W^{(2)}h^{(1)}_1\) has no cross term because both first derivatives vanish. Hence

\[
(z^{(2)}_1)''
=\frac12[g_1(\delta^{(2)}_1)'-h_1(\delta^{(2)}_2)']
+\frac12\phi'(z^{(1)}_1)^2(\delta^{(2)}_1)'.
\]

Its first two coordinates, after applying the final activation derivative, are

\[
\begin{aligned}
(h^{(2)}_{1,1})''&=\frac Q2
 [g_1P_1^2-h_1P_1P_2+U_1^2P_1^2],\\
(h^{(2)}_{1,2})''&=\frac Q2
 [-g_1P_2^2+h_1P_1P_2-U_2^2P_2^2].
\end{aligned}
\]

Subtracting gives exactly the candidate's

\[
J=\frac Q2
 [g_1(P_1^2+P_2^2)-2h_1P_1P_2
   +P_1^2U_1^2+P_2^2U_2^2].
\]

The first two terms inside the brackets equal

\[
g_1(P_1-P_2)^2+2(g_1-h_1)P_1P_2>0.
\]

The other two terms are also strictly positive. Thus \(J>0\), with no assumption about the sign of \(h_1\), \(S_i\), or \(H_i\). All entries of \((h^{(2)}_1)''\) numbered at least 3 vanish: the corresponding entries of both backward derivatives and rows of \((W^{(2)})''\) are zero. Symmetry gives \((h^{(2)}_2)''=P(h^{(2)}_1)''\).

### The third matrix and top-field accelerations

Differentiating its full update gives

\[
(W^{(3)})''=\frac1{2n}
[(\delta^{(3)}_1)'H^T-(\delta^{(3)}_2)'(PH)^T].
\]

Rows 1 and 2 are zero at this base state, because \(V_1=V_2=0\). Rows 3 and 4 are

\[
\frac v{2n}(rH^T-l(PH)^T),\qquad
\frac v{2n}(-lH^T+r(PH)^T),
\]

respectively; all later rows are zero. For row 1, the complete product rule therefore reduces to its original row applied to \((h^{(2)}_a)''\). The \(c(e_3-e_4)\) part contributes zero, giving

\[
(z^{(3)}_{1,1})''=-J,\qquad
(z^{(3)}_{2,1})''=J.
\]

With \(D_1=(z^{(3)}_{1,1}-z^{(3)}_{2,1})/2\), this proves

\[
D_1(0)=D_1'(0)=0,\qquad D_1''(0)=-J.
\]

For a check on all the other top coordinates, define

\[
G_2=\|H\|_2^2/n,\qquad B_2=H^TPH/n.
\]

The sample-1 top-preactivation acceleration vector is

\[
(-J,J,\alpha_3,\alpha_4,0,\ldots),
\]

where

\[
\alpha_3=bJ+\frac v2(rG_2-lB_2),\qquad
\alpha_4=-bJ+\frac v2(-lG_2+rB_2).
\]

The sample-2 vector is its permutation by \(P\). These formulas retain the \(1/n\) from the third-matrix metric through \(G_2,B_2\).

### Second and third derivatives of the readout; hidden third derivatives

Because all first hidden velocities vanish, \(w''(0)=0\). Differentiating \(w'=(h^{(3)}_1-h^{(3)}_2)/2\) twice gives

\[
w_i'''(0)=\frac12
\left[\phi'(z^{(3)}_{1,i})(z^{(3)}_{1,i})''
-\phi'(z^{(3)}_{2,i})(z^{(3)}_{2,i})''\right].
\]

The \(\phi''(z)(z')^2\) terms are zero, rather than omitted approximations. Thus

\[
w'''(0)=(-\tfrac32J,\tfrac32J,\zeta,-\zeta,0,\ldots),
\]

where

\[
\zeta=\frac32bJ
+\frac v4[(r^2+l^2)G_2-2rlB_2].
\]

In particular, the claimed \(w_1'''(0)=-(3/2)J\) is exact.

There is also a useful complete check on the other parameter third derivatives. Collect the three hidden parameter blocks as \(X\). The feature system has the form

\[
X'=\mathcal B(X)w,\qquad w'=V(X),
\]

where \(\mathcal B(X)\) is linear as an operator on \(w\). At \(w(0)=0\), one has \(X'(0)=0\), \(w''(0)=0\), \(X''(0)=\mathcal B(X(0))V(X(0))\), and, on differentiating once more, \(X'''(0)=0\). Accordingly every third derivative of a forward hidden field also vanishes at \(s=0\). Equivalently, uniqueness under time reversal gives \(X(-s)=X(s)\), \(w(-s)=-w(s)\). This applies for every zero-readout perturbation in the candidate family. The candidate uses weaker, but valid, Taylor remainder orders.

All four parameter blocks actually train. The first-layer acceleration is nonzero. The second-matrix acceleration is nonzero: \(P_1S=P_2T\) would contradict equal norms of \(S,T\) and \(P_1>P_2\). The third-matrix acceleration is nonzero because \(rH=lPH\) would contradict \(r>l\) and \(\|H\|=\|PH\|>0\). Finally \(w_3'=v>0\). These nonzero quantities persist for sufficiently small perturbations by continuity. A zero first hidden velocity at initialization is not a frozen block.

## 5. Perturbation, including the new top-row acceleration

Write the candidate's small parameter as \(\varepsilon>0\), to distinguish it from coordinate vectors. Set

\[
a_\varepsilon=-1+\varepsilon/\Delta,
\qquad u_\varepsilon=a_\varepsilon(e_1-e_2)+c(e_3-e_4).
\]

The initial top pair for neuron 1 is \((\varepsilon,-\varepsilon)\). Thus

\[
D_1(0;\varepsilon)=\varepsilon,\quad
D_1'(0;\varepsilon)=0,\quad
w_1'(0;\varepsilon)=\tfrac32\varepsilon,\quad
w_1''(0;\varepsilon)=0.
\]

It would be an error to continue setting the first third-matrix row acceleration to zero after this perturbation. The candidate does not do that: it uses the zero only at the base point and then smooth dependence. The following exact perturbed computation checks that justification directly.

Extend \(P_i,U_i\) to \(i=3,4\) by the same definitions as above, and set

\[
\Lambda_{ij}=\frac12
 [g_1(P_i^2+P_j^2)-2h_1P_iP_j+P_i^2U_i^2+P_j^2U_j^2]
\quad ((i,j)=(1,2),(3,4)).
\]

These are fixed positive constants for fixed lower initialization and \(n\), and \(J=Q\Lambda_{12}\). The exact perturbed backward derivative is

\[
(q^{(2)}_1)'=(q^{(2)}_2)'
=Q(e_1-e_2)+\frac92\varepsilon u_\varepsilon.
\]

This follows because each antisymmetric top pair contributes its row times its readout derivative times \(\phi'(z)+\phi'(-z)=3\). The first and second coordinate-pair differences in \((h^{(2)}_1)''\) are therefore

\[
\bigl(Q+\tfrac92\varepsilon a_\varepsilon\bigr)\Lambda_{12},
\qquad \tfrac92\varepsilon c\Lambda_{34}.
\]

Put \(p_+=\phi'(\varepsilon)\), \(p_-=\phi'(-\varepsilon)\). The new first-row acceleration is exactly

\[
(\operatorname{row}_1W^{(3)})''
=\frac{3\varepsilon}{4n}[p_+H^T-p_-(PH)^T].
\]

Combining this row acceleration with the lower-feature acceleration gives

\[
D_1''(0;\varepsilon)
=a_\varepsilon\bigl(Q+\tfrac92\varepsilon a_\varepsilon\bigr)\Lambda_{12}
+\tfrac92\varepsilon c^2\Lambda_{34}
+\tfrac98\varepsilon(G_2-B_2)
=-J+O_n(\varepsilon).
\]

The last term is the top row's own learning contribution, with its exact width factor. This identity verifies that no order-one contribution is missing when the top row starts moving.

Let \(M_1=(z^{(3)}_{1,1}+z^{(3)}_{2,1})/2\). At this perturbed initial state the lower-feature contribution to \(M_1''\) cancels, since \(u_\varepsilon P=-u_\varepsilon\), while the row-update contribution is

\[
M_1''(0;\varepsilon)
=\frac{3\varepsilon}{8}(p_+-p_-)(G_2+B_2).
\]

Consequently

\[
w_1'''(0;\varepsilon)
=\frac32D_1''(0;\varepsilon)
+\frac{p_+-p_-}{2}M_1''(0;\varepsilon)
=-\frac32J+O_n(\varepsilon).
\]

For the explicit positive-coordinate example, \(M_1''>0\) when \(\varepsilon>0\). Thus the paired preactivations generally cease to be exact negatives. The proof is nevertheless sound: it uses \(\phi(z)-\phi(-z)=3z\) at initialization, and differentiates the actual feature difference thereafter. It never needs that identity at unequal, nonopposite later preactivations.

## 6. Uniform Taylor bounds and the strict sign flip

Here uniformity is in sufficiently small \(\varepsilon\), for each fixed \(n\). The initial parameter family is a compact smooth curve on any fixed closed small \(\varepsilon\)-interval. The finite vector field is smooth on the full parameter space. Choose a closed neighborhood of this curve inside a larger compact neighborhood. On the larger neighborhood the field and its required derivatives are bounded. A time shorter than the distance to its boundary divided by the field bound keeps solutions inside it. Taking a still shorter time if necessary makes the integral equation a contraction using the derivative bound. This supplies common local existence and uniqueness. For two such solutions, the integral inequality for their difference gives the bound \(e^{Ls}\|\theta_0-\widetilde\theta_0\|\), where \(L\) is that derivative bound. Differentiating the field along the solutions gives bounded time derivatives of the needed orders on this common interval.

These facts justify the candidate's Taylor remainders uniformly in \(\varepsilon\), without any width-uniform ODE assertion. Combining the initial values and derivatives already checked gives

\[
\begin{aligned}
D_1(s;\varepsilon)
&=\varepsilon-\frac J2s^2+O_n(\varepsilon s^2+s^3),\\
w_1(s;\varepsilon)
&=\frac32\varepsilon s-\frac J4s^3
  +O_n(\varepsilon s^3+s^4).
\end{aligned}
\]

The quadratic coefficient is \(D_1''/2!=-J/2\), and the cubic coefficient is \(w_1'''/3!=-(3J/2)/6=-J/4\). The parity established above would improve the pure-time remainders to \(s^4\) and \(s^5\), respectively, but that improvement is not needed.

At

\[
s_\varepsilon=2\sqrt{\varepsilon/J},\qquad
s_\varepsilon^2=4\varepsilon/J,
\]

the leading terms become

\[
\varepsilon-\frac J2s_\varepsilon^2=-\varepsilon,
\]

and

\[
\frac32\varepsilon s_\varepsilon-\frac J4s_\varepsilon^3
=\left(\frac32-1\right)\varepsilon s_\varepsilon
=\frac12\varepsilon s_\varepsilon
=\frac{\varepsilon^{3/2}}{\sqrt J}.
\]

The contrast remainder is \(O_n(\varepsilon^{3/2})\); the readout remainder is \(O_n(\varepsilon^2)\). Their ratios to their respective strict leading margins tend to zero. Thus, for sufficiently small positive \(\varepsilon\),

\[
D_1(s_\varepsilon;\varepsilon)<0,\qquad
w_1(s_\varepsilon;\varepsilon)>0.
\]

For each such fixed \(\varepsilon\), continuity and \(D_1(0)=\varepsilon>0\), together with \(w_1'(0)=3\varepsilon/2>0\), give an earlier interval on which both are positive. Hence there is an actual loss of the initial positive alignment. At the unperturbed base state, by contrast, \(D_1(s)=-Js^2/2+o(s^2)\) and \(w_1(s)=-Js^3/4+o(s^3)\); both are negative. The perturbation is essential and is used noncircularly.

For an explicit clock check, initially only the readout component of \(\operatorname{grad}g\) is nonzero, so

\[
g'(0;\varepsilon)=\|\operatorname{grad}_{\rm raw}g\|_{\rm raw}^2
=\frac{2v^2+(9/2)\varepsilon^2}{n}=:\kappa_\varepsilon.
\]

The common short interval can be chosen so \(1-g>0\) for all sufficiently small \(\varepsilon\). Integration of the exact inverse clock gives

\[
t_\varepsilon:=t(s_\varepsilon)
=\frac14s_\varepsilon+O_n(s_\varepsilon^2)
\sim\frac12\sqrt{\varepsilon/J}>0.
\]

It tends to zero and gives the same state, hence the same strict inequalities, in actual physical GF. As a derivative-level check, at the base initialization

\[
\frac{d^2D_1}{dt^2}(0)=-16J,\qquad
\frac{d^3w_1}{dt^3}(0)=-96J.
\]

For the perturbed family the physical second derivative of \(w_1\) is generally not zero:

\[
\frac{d^2w_1}{dt^2}(0)=-24\varepsilon\kappa_\varepsilon.
\]

This comes from differentiating the clock factor. The candidate's zero second derivative is correctly a feature-time statement, not an accidental physical-time claim.

## 7. Full-support finite-Gaussian neighborhood

Fix \(n\), then fix a sufficiently small \(\varepsilon>0\), and then fix the central trajectory's physical observation time \(t_\varepsilon\). This order matters. The physical loss field is smooth everywhere in the finite parameter space. On a compact tube around the central solution up to \(t_\varepsilon\), its derivative is bounded; the same local-existence and difference estimate used above ensure that sufficiently close initial conditions have solutions through that fixed time and nearby terminal parameters.

The maps from terminal parameters to \(w_1\) and to \(D_1\) are continuous. Since their terminal inequalities are strict, there is an open neighborhood \(U\subset\mathbb R^{2n^2+3n}\) of the central initial weights on which both inequalities hold under actual physical GF at the same \(t_\varepsilon\). No feature clock or symmetry is asserted for perturbed points of \(U\).

Under the contract with \(d=2\), the entries of \(W^{(1)}\), \(W^{(2)}\), \(W^{(3)}\), and \(w\) have variances \(1/2\), \(1/n\), \(1/n\), and \(n^{-2}\), respectively. Each variance is strictly positive for fixed finite \(n\), and all entries are independent. Their joint density is therefore continuous and strictly positive everywhere in this finite-dimensional space. A closed ball of positive radius contained in \(U\) has positive volume and a positive minimum density, so \(\mathbb P(U)>0\).

The event \(w=0\) has probability zero. Removing it from \(U\) leaves its positive probability unchanged. This proves the stated conclusion with the prescribed genuinely random readout. It does not put positive mass on the zero-readout or exact-symmetry submanifold.

If one additionally wants random initial positive alignment for this neuron, continuity allows \(U\) to be shrunk so \(D_1(0)>0\); intersecting it with \(w_1(0)>0\) still leaves a nonempty open set of positive Gaussian probability. This optional strengthening is not needed for the candidate's stated terminal inequalities.

There is no lower bound here uniform in \(n\), in \(\varepsilon\downarrow0\), or in the observation time. The neighborhood may be very small and its Gaussian probability may decay arbitrarily rapidly with width. Local existence through the observation time suffices; no global finite-network or population existence theorem is a premise.

## 8. Adversarial and circularity checks

The following potential failures were specifically tested against the derivation:

1. **Using the Euclidean first-weight metric.** That would introduce the wrong first-layer scaling. Inverting \(d/n\) gives the candidate's \(1/2\) preactivation factor exactly.
2. **Ignoring nonzero activations outside the first four coordinates.** Such a truncation would be wrong for this activation. The exact \(g_1,h_1,G_2,B_2\) retain those coordinates, and the proof works for all \(n\geq4\).
3. **Inferring a gradient identity only from the loss restricted to a symmetry subspace.** That inference alone would be insufficient. The full residual-gradient calculation in Section 3 establishes the ambient vector identity at every symmetric state.
4. **Assuming symmetry rather than preserving it dynamically.** The initial fixed-point identities, metric isometry, full loss invariance with the opposite labels, and ODE uniqueness establish preservation independently of the sign-flip calculation.
5. **Assuming paired preactivations stay opposite.** They need not; the perturbed \(M_1''\) explicitly detects this. Only the initial opposition and the true derivative of the feature difference are used.
6. **Keeping the first top row frozen after perturbation.** Its exact nonzero acceleration contributes \(9\varepsilon(G_2-B_2)/8\) to \(D_1''\). This is correctly covered by \(O_n(\varepsilon)\).
7. **Assuming the sign of an inner product.** Positivity of \(J\) uses \(g_1-h_1=\|S-T\|^2/(2n)>0\) and positive activation derivatives; it does not assume \(h_1\geq0\).
8. **Using Taylor expansions whose constants diverge as \(\varepsilon\to0\).** The initial data and smooth field stay in a common finite-dimensional compact neighborhood for fixed \(n\). The required uniformity follows there; no width-uniform estimate is used.
9. **Converting a feature-time sign statement into physical time without checking the sign of the clock.** The factor \(4(1-g)\) is positive on a common short interval because \(g(0)=0\). The inverse clock yields the actual loss flow and \(t_\varepsilon\to0\).
10. **Assigning probability to an exact zero-readout or symmetry event.** The positive-probability claim is instead made for an open set in the full parameter space at a fixed physical time. Full support applies to that set.
11. **Assuming the very alignment invariant being disproved.** No step does so: the nonzero lower-feature acceleration is derived from the other active top pair and the two lower trainable blocks. It does not use an aligned-sector estimate or any continuation conclusion.

None of these produces a counterexample to the intended finite-trajectory lemma. Two stronger literal readings of the prose do fail, as detailed next.

## 9. Required statement repairs

These are statement precisions. No change to the construction, derivative calculation, sign argument, or probability argument is required.

**R1 — Make the small-time quantifiers explicit (candidate lines 14–18).** The proved assertion is

\[
\forall n\geq4\ \forall\tau>0\ \exists\theta_0
\ \exists t\in(0,\tau):
\quad w(0)=0,\quad w_1(t)>0,\quad D_1(t)<0,
\]

with \(\theta_0=\theta_{\varepsilon,n}\) selected after choosing the time bound. It is not a demonstration of one fixed initialization with misalignment at positive times arbitrarily close to zero. For each fixed \(\varepsilon>0\), the constructed trajectory is initially positively aligned on a nonempty interval; at \(\varepsilon=0\), both relevant quantities are initially negative. The section-4 proof already has the correct dependence. The opening statement should say explicitly that the initial state varies with the requested small time.

**R2 — Specify the uniformly bounded norms (candidate lines 14 and 59–61).** The available statements define a raw metric but do not define “bounded-primal.” If this means the full raw parameter norm, the claim is false: \(W^{(2)}=I_n\) has raw squared norm contribution \(n\). Likewise unnormalized activation-vector norms are not bounded. The valid assertion is a width-independent bound on the displayed weight operator norms (and on \(\|W^{(1)}\|_F\)), together with empirical hidden-vector norms \(\|h^{(\ell)}_a\|_2/\sqrt n\) and \(\|z^{(\ell)}_a\|_2/\sqrt n\), or coordinatewise bounds. Naming these norms removes the ambiguity without weakening the structural misalignment conclusion.

## 10. Presentation suggestions, separate from required repairs

- At candidate line 80, say “forward sample fields” when claiming permutation by \(P\), or also state the minus-permutation law for the residual-free backward fields. The equations later in the candidate already have the correct signs.
- After perturbing the first row, one sentence noting that its previously vanishing acceleration becomes \(O_n(\varepsilon)\) would make the smooth-dependence argument harder to misread. The exact expression in Section 5 of this review is available if a direct check is desired.
- Keep the distinction between feature time and physical time visible near the Taylor display. The formula \(t_\varepsilon\sim s_\varepsilon/4\) is a compact explicit check; feature-time derivatives should not be relabeled as physical derivatives.
- The existing weaker remainders are sufficient. Time-reversal parity can sharpen them, but doing so is optional and does not strengthen the scoped conclusion needed here.

**Scoped disposition:** accept the actual fully trained finite-trajectory misalignment argument, with R1–R2 made explicit in its statement. The finite full-support Gaussian conclusion is valid at a fixed positive physical observation time. No audited step supports a typical-width failure or a mean-field impossibility claim, and none is needed for this structural lemma.
