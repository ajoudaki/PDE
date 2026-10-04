# Complete internal check of canonical one-input neuron compression

2026-10-03. Complete reconstruction of CANONICAL_NEURON_COMPRESSION.md,
first read-version SHA-256
fc1952e8597fc89e91a11b68173a35a931a71059ce5d4e82e9a056c6d1eaa5dc.
The author subsequently replaced exact angular Fourier integrals by finite
trigonometric interpolation. I read and fully checked that replacement.
The final mathematical body checked here has SHA-256
ecc3cc7e8ff8c4c50dc4cf74f47930cbbbf8be30311b2abaa466b616ab371c94.
The reconstruction below incorporates that final finite construction.
The complete complex source dependency was independently checked at
SHA-256
3190cbcef13c3089b2a475c297e9333e98ce3c01f69a686bde217cf87f193fe4,
including its circle-query and parity sections; see
COMPLEX_ACTIVITY_CHECK.md. The explicit conformal lemma and scalar-clock
comparison were already reconstructed in CANONICAL_SCALAR_AUTONOMY_ROUTE.md.
This is an internal collaborative check, not an isolated promotion review.
No experiment, Git write, or source edit was performed.

**Verdict: PASS for the candidate's stated dense-network theorem.**
The actual canonical finite Gaussian reference, initialization-only
construction, two-sided source approximation, coupled reduced dynamics,
whole-circle physical-time supremum, fitted endpoint, and
\(n^{o(1)}\) total moving-coordinate count all reconstruct. The proof does
not require a smaller Gaussian initialization law or a trained-path oracle.
It does not yet assert the same result for the unchanged finite-order
response-memory closure, multiple training inputs, or general depth.

The candidate's reference to a separate weighted stability note is not
needed for this verdict: its required complete real weighted comparison is
derived below from the equations in the candidate itself. A nonvanishing
hidden-mixer motion certificate is also recorded below; a separate
certificate for every hidden representation should be stated explicitly
if that stronger mechanism claim is made.

## 1. Exact model and real activity tube

The reference is the two-hidden-layer width-\(n\) dense model with
\[
 h_\theta=\tanh(a\cos\theta+\beta\sin\theta),\qquad
 g_\theta=\tanh(Wh_\theta),\qquad f_n=w^\top g_\theta/n,
\]
where \(a=Ae_1\), \(\beta=A_0e_2\), and only the input
\(\sqrt2e_1\) with label \(y>0\) trains the network. Its actual
mobilities are \(n,1,n\) and its loss is \((f_n(x_1)-y)^2\).
Dividing the physical equations by \(ds/dt=2(y-f_n(x_1))\) gives the
candidate's activity equations with no missing factor of \(n\) or \(2\).

On the real line,
\[
 \Psi(a)=a/2+\sinh(2a)/4,\quad u=\Psi(a),\quad
 \sigma(u)=\tanh(\Psi^{-1}(u))
\]
have \((\Psi^{-1})'=\operatorname{sech}^2a\le1\) and
\(\sigma'=\operatorname{sech}^4a\le1\). Thus
\[
 u'=W^\top\delta,\qquad
 W'=\delta h^\top/n,\qquad w'=g,\qquad
 \delta=w\odot\operatorname{sech}^2z.
\]

The real bounds in (5) need only an initial operator bound. In particular
\(\|w(s)\|_\infty\le|s|\), and
\[
 \|W'(s)\|_F
   =(\|\delta(s)\|_2/\sqrt n)(\|h(s)\|_2/\sqrt n)
   \le|s|.
\]
Hence the hidden increment is at most \(s^2/2\) in Frobenius norm,
and \(u'\) has normalized Euclidean norm \(C|s|\) on a fixed short
operator tube. The 1-Lipschitz properties then control the feature
differences and preserve a fixed initialized top-feature Gram gap.

The exact derivative of the training prediction is
\[
 f_n'
 =\|g\|_2^2/n
  +(\|\delta\|_2^2/n)(\|h\|_2^2/n)
  +\|\operatorname{sech}^2a\odot W^\top\delta\|_2^2/n.
\]
It has a positive fixed lower bound and finite fixed upper bound on
\([0,S]\). Choosing \(y_*<\gamma S/4\) puts its unique fitting activity
strictly below \(S\). Its own scalar clock increases to that equilibrium,
and the physical residual decays exponentially. All coordinate speeds
have finite total variation along the finite activity interval.

Exactly the same reasoning holds in finite positive weighted Hilbert
spaces. Their total masses are one, so bounded coordinate features have
weighted norm at most one. A weighted rank-one map
\(x y^\top D_1\) has Hilbert--Schmidt norm
\(\|x\|_{D_2}\|y\|_{D_1}\). These facts preserve all constants without
using the smallest weight.

For the initial scalar Gram gap, the empirical first-feature square norm
concentrates above a fixed positive number. Conditional on those
features, the top preactivations are independent centered Gaussians whose
variance equals that norm. The expectation of their squared tanh is
therefore bounded below by a fixed positive constant, and bounded-variable
concentration gives the stated gap. The independent Gaussian operator
bound also has exponentially small failure. Thus the real-tube constants
and label threshold can be fixed independently of confidence.

## 2. Complete source regularity and finite initial representation

The checked complex theorem supplies a joint activity rectangle and angular
strip with radii \(c/\sqrt{\ell}\), where
\(\ell=\log(en/\delta)\), and coordinate bounds \(C\sqrt{\ell}\)
for the needed query sources. Activity parity supplies a symmetric
rectangle. Taking a fixed fraction of the proved radius gives the exact
domain required by the conformal map; no disk of radius \(S\) at zero is
assumed.

One training source used by the candidate is not separately named in the
complex theorem's leading statement: \(W_0^\top\delta(s)\).
Its required bound follows directly. On a radial complex activity path,
\[
 [(W(s)-W_0)^\top\delta(s)]_i
  =\int_0^s h_i(v)\,
                 \frac{\delta(v)^\top\delta(s)}n\,dv.
\]
The path has bounded length, \(h_i\) is uniformly bounded, and both
responses have bounded RMS. This expression is bounded uniformly in \(i\)
by \(CS^3\). Since \(W^\top\delta=k\) has the checked
\(CS\sqrt{\ell}\) coordinate bound, \(W_0^\top\delta\) has the required
\(C\sqrt{\ell}\) bound. It is holomorphic by the same formulas.

For a bounded source \(R(s,\theta)\), the explicit map
\[
 z(\zeta)=\frac{2r}{\pi}
       \log\frac{1+\alpha\zeta}{1-\alpha\zeta},\qquad
 \alpha=\tanh\frac{\pi(S+2r)}{4r}
\]
maps the unit disk into the certified activity rectangle. Taylor
coefficients of \(R(z(\zeta),\theta)\) are scalar linear combinations
of initial activity derivatives \(R^{(j)}(0,\theta)\). Its disk Taylor
tail at the largest real activity obeys
\[
 \frac{M q^{p+1}}{1-q},\qquad
 1-q\ge c e^{-CS/r},\qquad M\le C\sqrt{\ell}.
\]
Thus degree \(p\le C e^{C\sqrt{\ell}}\ell\), chosen with a sufficiently
large fixed constant, gives coordinate error at most \(\epsilon\),
uniformly on real \(s\in[0,S]\) and throughout the complex angular strip,
when \(\epsilon\) is a fixed multiple of \(n^{-1/2}\).

For each real \(s\), the resulting activity approximant remains
holomorphic in angle and bounded there by \(M+\epsilon\). Shifting its
Fourier integral upward or downward gives coefficient bound
\((M+\epsilon)e^{-|j|r_\theta}\). Consequently
\[
 \sum_{|j|>L}|\widehat R_j|
 \le\frac{2(M+\epsilon)e^{-(L+1)r_\theta}}
                 {1-e^{-r_\theta}}.
\]
The finite construction uses the trigonometric interpolant at
\(Q=2L+1\) equally spaced real angles. To check the claimed alias bound,
write \(R(\theta)=\sum_{j\in\mathbb Z}c_j e^{ij\theta}\).
Every frequency \(j\) has a unique representative \(\bar j\in[-L,L]\)
modulo \(Q\), and its values at the interpolation nodes equal those of
\(e^{i\bar j\theta}\). Absolute convergence therefore gives
\[
 R(\theta)-I_LR(\theta)
   =\sum_{|j|>L}c_j(e^{ij\theta}-e^{i\bar j\theta}).
\]
For real \(\theta\), the modulus is at most twice the displayed Fourier
tail. Because \(r_\theta\ge c/\sqrt{\ell}\), a sufficiently large
\(L\le C\ell^{3/2}\) makes this interpolation error at most
\(\epsilon\).

The activity approximation and trigonometric interpolation are linear
operators acting on different variables, so they commute. Their final
coefficient vectors are finite discrete Fourier transforms of initial
activity derivatives at those \(Q\) nodes, combined with fixed scalar
coefficients. Real sine and cosine coefficients preserve the real span
and cost at most \(2L+1\) vectors per derivative order.
This gives dimensions
\[
 r_1,r_2\le C(p+1)(2L+1)+C.
\]
The extra training derivatives and initialized columns contribute only
\(O(p)+O(1)\).

The mixed coefficients depend only on initialization. Computing an initial
derivative differentiates the known finite activity equations at their
initial state, at one of the finitely many fixed query angles. The
coefficient transforms and cubature require only finitely many arithmetic
operations and initial function derivatives. They may be expensive or
poorly conditioned, but neither setup cost nor finite-precision
conditioning is claimed. No trained trajectory or angular integration is
used as an input to the final construction.

## 3. Paired forward and reverse approximation

Let \(\mathcal A\) denote the common finite approximation operator just
constructed. It acts only on the scalar activity and query variables.
Since \(W_0\) is fixed,
\[
 \mathcal A(W_0h)=W_0(\mathcal A h).
\]
Applying the coordinatewise approximation estimate to both source
functions gives, simultaneously,
\[
 \|h-\mathcal A h\|_\infty\le C\epsilon,\qquad
 \|W_0h-W_0(\mathcal A h)\|_\infty\le C\epsilon.
\]
The source-space definitions include the coefficient vectors of
\(\mathcal A h\) in \(S_1\), and their actual \(W_0\) images in
\(S_2\). The corresponding statement for the training response is
\[
 \|\delta-\mathcal A\delta\|_\infty\le C\epsilon,\qquad
 \|W_0^\top\delta-W_0^\top(\mathcal A\delta)\|_\infty
                                                      \le C\epsilon,
\]
with the two approximants in \(S_2,S_1\), respectively. Here only the
activity approximation is needed.

These are bounds on the sampled images themselves. They do not try to
deduce coordinatewise smallness of \(W_0(h-\mathcal A h)\) from an RMS
source error. The common scalar coefficients are what make the exact
two-sided interpolation identities usable.

The readout also has a source-space approximant:
\[
 w(s)=\int_0^s g(v,0)\,dv,\qquad
 w_{\rm app}(s)=\int_0^s g_{\rm app}(v,0)\,dv\in S_2.
\]
Its coordinate error is at most \(CS\epsilon\), and
\(\|w\|_\infty\le S\). This is a proof consequence of the source
approximation; it is not a stored trained-path integral.

## 4. Cubature identities and the actual reduced model

Empirical orthonormal bases satisfy
\(V^\top V/n=I\), \(U^\top U/n=I\). Matching the constant and symmetric
products of their rows with positive masses requires at most
\[
 N_1\le1+r_1(r_1+1)/2,\qquad
 N_2\le1+r_2(r_2+1)/2
\]
original indices. A linear dependence of more evaluation vectors has
coefficients summing to zero because the constant is matched; moving
weights along it to the first zero weight preserves positivity and all
moments. Thus the stated elimination construction proves these counts.

Let \(D_1,D_2\) be the resulting positive diagonal weight matrices. The
restricted bases are isometries for their weighted inner products. With
\[
 B=U^\top W_0V/n,\qquad
 B_0=U_J B V_I^\top D_1,
\]
the normalization is correct:
\(B=(U/\sqrt n)^\top W_0(V/\sqrt n)\).
Hence its ordinary operator norm is at most \(\|W_0\|_{\rm op}\).
The selected basis isometries imply the same bound for \(B_0\) from
\(D_1\) to \(D_2\).

Its exact weighted adjoint is
\[
 B_0^*=D_1^{-1}B_0^\top D_2
       =V_I B^\top U_J^\top D_2.
\]
Thus \(B_0v_I=(W_0v)_J\) whenever \(v\in S_1\) and
\(W_0v\in S_2\), and similarly
\(B_0^*d_J=(W_0^\top d)_I\) for a paired reverse vector.
These follow by expanding the respective vectors in the orthonormal
bases, not by assuming invariance of all of \(S_1,S_2\).

In particular the initialized training \(h_0\), \(W_0h_0\), and \(g_0\)
are reproduced at their selected coordinates, and the training
\(g_0\)-square norm is preserved. Therefore the reduced model has the
same positive initialized scalar Gram and no larger initialized mixer
operator norm.

The physical equations in (13) are an autonomous system using only
\(A_C,B_C,w_C,D_1,D_2,y\). Its residual is its own current weighted
prediction minus \(y\); its reverse pass uses the same \(B_C\) with its
weighted adjoint. The second first-layer column remains the selected
original \(\beta\). The real activity tube and fitting argument of
Section 1 apply to this model.

Tiny masses do not introduce a hidden error factor. For each fixed
finite model the masses are strictly positive, so a bounded weighted norm
also bounds every coordinate sufficiently for finite-dimensional
continuation. Uniform estimates use weighted operator and
Hilbert--Schmidt norms, with constants independent of the least mass.

## 5. Pairing defects and the sampled reference matrix

If \(v,\widetilde v\) have bounded source norms and coordinatewise
\(C\epsilon\) approximants in \(S_1\), insert the two approximants into
both empirical and selected weighted pairings. The approximant pairings
agree exactly. Every remaining term has one coordinatewise remainder and
one bounded weighted or empirical norm. For an approximant its weighted
norm equals its empirical norm by cubature; its empirical norm is bounded
by the source norm plus its error. Hence the pairing defect is
\(C\epsilon\), without any factor involving the number or weights of
retained nodes. The same argument works in \(S_2\), including the readout
approximant just constructed.

Define the sampled reference matrix
\[
 B_R(s)=B_0+\int_0^s\delta_J(v)h_I(v)^\top D_1\,dv.
\]
This is only a proof device. For a query feature \(h_\theta(s)\), its
forward fixed-mixer defect is bounded by inserting
\(v=\mathcal A h_\theta(s)\):
\[
 B_0(h_{\theta,I}-v_I)
          +(W_0v-W_0h_\theta)_J.
\]
The first term is \(C\epsilon\) in the weighted upper norm by the
operator bound, and the second is \(C\epsilon\) by paired coordinate
approximation.

The learned forward defect is exactly
\[
 \int_0^s\delta_J(v)
 \left[
   h_I(v)^\top D_1h_{\theta,I}(s)
      -h(v)^\top h_\theta(s)/n
 \right]dv.
\]
Its pairing bracket is \(C\epsilon\), and
\(\|\delta_J(v)\|_{D_2}\le v\). Thus it is \(C\epsilon\) on the fixed
interval. This proves the first line of (16).

For the reverse action, the paired fixed-mixer defect is controlled in the
same manner using \(\mathcal A\delta\). The learned reverse defect is
\[
 \int_0^s h_I(v)
 \left[
   \delta_J(v)^\top D_2\delta_J(s)
       -\delta(v)^\top\delta(s)/n
 \right]dv.
\]
The upper pairing estimate and \(\|h_I(v)\|_{D_1}\le1\) give the second
line of (16). This explicitly retains the same evolving mixer in both
orientations and all accumulated training feedback.

The readout-query pairing defect gives (17). The reference matrix has
operator norm at most \(K+S^2/2\), since its rank-one integrand has
operator norm at most \(v\).

## 6. Full weighted state comparison

Define reference coordinates
\[
 U_R=u_I,\qquad W_R=w_J,\qquad
 h_R=\sigma(U_R)=h_I,\qquad
 \widehat z_R=B_Rh_R,\qquad
 \widehat g_R=\tanh\widehat z_R,\qquad
 \widehat\delta_R=W_R\odot\operatorname{sech}^2\widehat z_R.
\]
Hats here distinguish evaluation in the reference matrix from the
sampled actual dense quantities \(z_J,g_J,\delta_J\).
The forward source defect yields
\[
 \|\widehat z_R-z_J\|_{D_2}\le C\epsilon,\quad
 \|\widehat g_R-g_J\|_{D_2}\le C\epsilon,\quad
 \|\widehat\delta_R-\delta_J\|_{D_2}\le CS\epsilon.
\]

Their differential residuals in the reduced vector field are therefore
\[
 U_R'-B_R^*\widehat\delta_R
   =k_I-B_R^*\delta_J+
                B_R^*(\delta_J-\widehat\delta_R),
\]
\[
 B_R'-\widehat\delta_Rh_R^\top D_1
       =(\delta_J-\widehat\delta_R)h_R^\top D_1,\qquad
 W_R'-\widehat g_R=g_J-\widehat g_R.
\]
The reverse source defect controls the first displayed term; the uniform
operator and rank-one bounds control all others. Their summed weighted
Euclidean/Hilbert--Schmidt norm is at most \(C\epsilon\).

For clarity, the needed real finite-difference estimate can be derived
without an external stability claim. For reduced and reference states,
write
\[
 E=\|u_C-U_R\|_{D_1}
        +\|B_C-B_R\|_{\rm HS}
        +\|w_C-W_R\|_{D_2}.
\]
Both mixers have uniformly bounded operator norms on \([0,S]\), both
readouts have coordinate maximum at most \(S\), and both first features
have weighted norm at most one. Consequently
\[
 \|h_C-h_R\|_{D_1}\le E,\qquad
 \|B_Ch_C-B_Rh_R\|_{D_2}\le CE,
\]
\[
 \|\delta_C-\widehat\delta_R\|_{D_2}
 \le\|w_C-W_R\|_{D_2}
             +CS\|B_Ch_C-B_Rh_R\|_{D_2}
 \le CE.
\]
The last inequality splits the product with \(W_R\) multiplying the
gate difference. It therefore uses a coordinate bound on the reference
readout, not on the error in that readout.

For the first velocity,
\[
 \|B_C^*\delta_C-B_R^*\widehat\delta_R\|_{D_1}
 \le C\|\delta_C-\widehat\delta_R\|_{D_2}
       +\|B_C-B_R\|_{\rm HS}
                           \|\widehat\delta_R\|_{D_2}
 \le CE.
\]
Subtracting the rank-one middle velocities costs
\[
 \|\delta_C-\widehat\delta_R\|_{D_2}\|h_C\|_{D_1}
       +\|\widehat\delta_R\|_{D_2}\|h_C-h_R\|_{D_1}
 \le CE.
\]
The readout velocity costs the top preactivation difference. Thus the
summed vector-field difference is \(CE\), uniformly in dimension and
masses. Since the reference defect is \(C\epsilon\) and the initial
state error is zero,
\[
 E(s)\le C\int_0^s E(v)\,dv+Cs\epsilon,
\]
and Gronwall proves \(E(s)\le C\epsilon\) throughout \([0,S]\).
The real tube for the reduced model was established independently in
Section 1, so this estimate has no unproved state bootstrap.

## 7. Whole-circle prediction and own physical clocks

The real inverse \(\Psi^{-1}\) is 1-Lipschitz. Therefore the reduced
first trained-column error is controlled in \(D_1\) norm by its
\(u\)-error. The untrained column is identical at selected nodes, so,
for every real angle,
\[
 \|h_{C,\theta}-h_{\theta,I}\|_{D_1}\le C\epsilon.
\]
Insert \(B_Rh_{\theta,I}\) into the top preactivation difference. The
matrix-state error, first-feature error, and forward source defect each
contribute \(C\epsilon\). Applying the real tanh Lipschitz estimate and
then the readout-state and pairing estimates gives
\[
 \sup_{s\in[0,S],\theta\in\mathbb R}
      |f_C(s,x_\theta)-f_n(s,x_\theta)|\le C\epsilon.
\]

Both models use their own scalar physical clocks
\(\dot s=2(y-F(s))\), where \(F\) is that model's training activity
prediction. The original training derivative is at least \(\gamma/2\),
and the uniform activity prediction difference is \(C\epsilon\).
Subtracting the two scalar clock equations, as in the checked clock
lemma, gives
\[
 \sup_{t\ge0}|s_C(t)-s_n(t)|\le C\epsilon/\gamma.
\]
Both clocks remain inside \([0,S]\) and converge to their own unique
fitting activities.

The real reference query derivative has a width-independent bound.
Indeed,
\[
 \partial_s h_\theta
  =\operatorname{sech}^2(a\cos\theta+\beta\sin\theta)
                    \cos\theta\,a',
\]
whose RMS is \(C|s|\). The operator bound and the rank-one update give
the same \(C|s|\) RMS bound for \(\partial_s z_\theta\). Therefore
\[
 |\partial_s f_n(s,x_\theta)|
 \le(\|w'\|_2/\sqrt n)(\|g_\theta\|_2/\sqrt n)
   +(\|w\|_2/\sqrt n)(\|\partial_s g_\theta\|_2/\sqrt n)
 \le C.
\]
No complex-strip coordinate maximum enters this final constant.
Combining this derivative bound with the clock error and the
equal-activity comparison proves the claimed same-physical-time error
\(C\epsilon\), uniformly on the whole real circle. Continuity at the
two fitting activities gives the endpoint comparison. Taking
\(\epsilon\) a fixed multiple of \(n^{-1/2}\) proves (1).

## 8. State count, provenance, and feature-learning scope

Write \(R=C(p+1)(2L+1)+C\). The positive cubature supports have size
\(O(R^2)\) in each layer, so the moving count
\(2N_1+N_1N_2+N_2\) is \(O(R^4)\). Since
\[
 p\le Ce^{C\sqrt{\ell}}\ell,\qquad L\le C\ell^{3/2},
\]
this is at most
\[
 C e^{C\sqrt{\ell}}\ell^{10}.
\]
At every fixed confidence, \(\ell=\log n+O_\delta(1)\), hence this count
is \(n^{o(1)}\) and in particular \(o(n)\).

All basis matrices, original-width source vectors, and the original mixer
may be discarded after constructing the selected rows, positive masses,
and projected initial mixer. The runtime equations and query evaluation
need only those fixed data and their own evolving state. Fixed storage
is no larger than the stated moving-state order. Expensive derivative
formation, finite trigonometric coefficient transforms, and cubature elimination occur
during setup; the theorem does not promise efficient setup or stable
floating-point construction.

The reference remains the actual canonical Gaussian network; the smaller
model's selected and projected initialization is intentionally
noncanonical. Thus canonical-smaller-law lower bounds do not contradict
this construction. Likewise, none of the source spaces is chosen from
future trained snapshots.

There is a direct width-independent hidden-mixer learning certificate.
Let
\[
 h_0=\tanh a_0,\quad z_0=W_0h_0,\quad
 b_0=\tanh z_0\odot\operatorname{sech}^2z_0.
\]
The real tube estimates give
\[
 w(s)=s\,\tanh z_0+O_{\rm RMS}(s^3),\qquad
 \delta(s)=s\,b_0+O_{\rm RMS}(s^3),\qquad
 h(s)=h_0+O_{\rm RMS}(s^2).
\]
For the middle equation, using normalized rank-one products then gives
\[
 W(s)-W_0=\frac{s^2}{2n}b_0h_0^\top+O_F(s^4).
\]
The constants are width independent. Canonical initialization makes both
\(\|b_0\|_2/\sqrt n\) and \(\|h_0\|_2/\sqrt n\) bounded below with
high probability, by the same conditional bounded-variable argument used
for the Gram gap. Thus at one sufficiently small fixed positive activity,
the hidden-mixer displacement has a positive lower bound proportional to
\(s^2\).

For a chosen fixed small label, the upper bound on the training derivative
puts its fitting activity above a positive multiple of \(y\). The preceding
certificate can therefore be placed before fitting by taking
\(s\) a sufficiently small fixed multiple of \(y\).
This verifies actual hidden learning at a width-independent scale.
If a final statement additionally promises a lower bound for displacement
of each hidden feature representation, that stronger certificate should
be supplied explicitly; it is not logically identical to hidden-matrix
motion.

The checked theorem itself is a complete positive autonomous
finite-reference compression result in its declared one-input,
two-hidden-layer, small-fixed-label, whole-circle setting. Extending its
scope requires further arguments, not changes to the present verdict.

## 9. Final source confirmation

I read the complete final source after the author changed its status and
scope paragraphs and inserted the explicit learned-matrix correction for
\(W_0^\top\delta\). Its final SHA-256 is
f83174163ff18c9f71224843abd444da004cf3c4c0a85749a0de4f9a73b44fd3.
The correction is exactly the identity and bound reconstructed in
Section 2 of this check. The status changes accurately distinguish the
completed internal checks from independent promotion review.
The final scope paragraph points to CANONICAL_FEATURE_LEARNING.md as a
separate certificate; that file is not an additional dependency of the
trajectory and state-count proof checked here.

No substantive construction, approximation, stability, complexity, or
physical-clock claim changed from the checked finite-interpolation body.
The PASS therefore applies to this final source hash. The separate
feature-motion certificate retains its own review record.

## 10. Confidence-symbol equivalence

The author subsequently renamed the scalar failure probability from
\(\delta\) to \(\eta\) in exactly its five occurrences: the quantifier,
the probability conclusion, the two occurrences in the complexity bound,
and the definition of \(\ell\). I checked these passages and confirmed
that the backward-response vector \(\delta\) is unchanged throughout.
This is an exact notation change, with no change of quantifiers, constants,
events, equations, or proof. Historical uses of scalar confidence
\(\delta\) in this report correspond to \(\eta\) in the final source.

The PASS applies to final source SHA-256
1a3ec599335af598ac834ce1f3892817d671cce7b42331808b6e84fd531b3a61.
