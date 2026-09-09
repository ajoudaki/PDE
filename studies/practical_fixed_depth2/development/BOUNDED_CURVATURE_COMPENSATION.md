# Bounded activation: exact curvature-compensation attempt

2026-09-08. Independent bounded theoretical subtask. The only project source read was `CONTRACT.md`. No experiments were performed.

**Status.** This report does not close uniqueness or cap removal. It establishes the bounded operator identity in the exact evolution of `q`, then checks three concrete augmentations of the comparison metric. Ordinary `q` and `h` distances leave the original first-layer curvature term and introduce a further multiplier term. Subtracting the bounded upper-layer linearization cancels the corresponding velocity term, but differentiating that linearization introduces an uncontrolled trilinear form. Integrating the force in time moves the difficulty to products of the force and its primitive. These are failures of the specified estimates, not a counterexample to the physical population flow or an impossibility theorem for every augmented metric.

## 1. Scope and regularity

This report uses the distinct, fixed activation

\[
 \phi(s)=1+\tfrac12\tanh s,
 \qquad p(s)=\phi'(s)=\tfrac12\operatorname{sech}^2s.
\]

It is not the principal affine-plus-tanh activation in the contract. Its coefficients are fixed independently of the training horizon. We retain all three inputs, the original raw gradient flow, the original residual feedback, and the actual layer operator and adjoint. No invertibility of the input Gram matrix is used.

Write \(H_a=L^2(\Omega_a)\), with probability measures, \(u_i=x_i/\sqrt d\), and \(\Gamma_{ij}=u_i\cdot u_j\). The first layer is \(w\in L^2(\Omega_1;\mathbb R^d)\), with \(z_i=w\cdot u_i\). Set

\[
 A=A_0+U,\quad h_i=\phi(z_i),\quad v_i=Ah_i,
 \quad k_i=\phi(v_i),\quad b_i=Cp(v_i),\quad q_i=A^*b_i.
\]

The calculations below apply to finite flows, and to two already-existing strong population solutions for which the canonical \(A_0\) is a bounded operator. They do not construct that canonical operator or those solutions. In population, \(U(0)=0\) and \(C(0)=0\). The physical equations are

\[
 \dot w=-\sum_i r_i p(z_i)q_i u_i,
 \quad \dot U=-\sum_i r_i b_i\otimes h_i,
 \quad \dot C=-\sum_i r_i k_i.
 \tag{1}
\]

Here \((b\otimes h)g=b\langle h,g\rangle\). Thus

\[
 \dot z_i=-\sum_j\Gamma_{ij}r_jp(z_j)q_j,
 \qquad
 \dot h_i=-\sum_j\Gamma_{ij}r_jp(z_i)p(z_j)q_j.
 \tag{2}
\]

On a fixed interval \([0,T]\), the energy identity and bounded activation give

\[
 \|r(t)\|_{\ell^2}\le\sqrt{2E(0)},\quad
 \|A(t)\|_{\rm op}\le\|A_0\|_{\rm op}+\sqrt{TE(0)},
 \quad
 \|C(t)\|_\infty\le\|C(0)\|_\infty+
 \tfrac32\sqrt{6E(0)}\,T.
 \tag{3}
\]

Also \(1/2< h_i,k_i<3/2\), \(0<p\le1/2\), and \(\phi''\), \(\phi'''\) are bounded. In population, the initial term in the last bound is zero. At finite width it must be retained; the small Gaussian readout is not replaced by zero. Bounds uniform across width require the corresponding initial operator, energy, and readout events.

All constants below may depend on the bounds in (3), \(T\), and the fixed inputs. They do not depend on a coordinatewise bound for \(q\). Since \(C\) and \(\dot C\) are bounded pointwise, the ordinary chain rules for the displayed compositions give \(h_i,v_i,b_i,q_i\) absolutely continuous as \(L^2\)-valued paths. These chain rules only use bounded scalar derivatives and bounded multipliers; they do not assert ambient \(L^2\) Lipschitzness of the complete vector field.

## 2. The exact bounded self-adjoint operator in the `q` equation

Let \(M_g\) denote multiplication by a bounded scalar field \(g\). Define

\[
 B_i=A^*M_{C\phi''(v_i)}A,
 \qquad
 g_i=\dot U^*b_i+
 A^*\bigl[\dot C p(v_i)+C\phi''(v_i)\dot U h_i\bigr].
 \tag{4}
\]

Then the exact chain rule is

\[
 \boxed{\dot q_i=g_i+B_i\dot h_i.}
 \tag{5}
\]

Indeed, \(\dot v_i=\dot U h_i+A\dot h_i\); substituting this into
\(\dot q_i=\dot U^*b_i+A^*[\dot C p(v_i)+C\phi''(v_i)\dot v_i]\)
gives (5).

Each \(B_i\) is bounded and self-adjoint, with

\[
 \|B_i\|_{\rm op}\le
 \|A\|_{\rm op}^2\|C\|_\infty\|\phi''\|_\infty.
 \tag{6}
\]

It need not be positive. The other terms have stronger elementary bounds:

\[
 \dot U h_i=-\sum_j r_j b_j\langle h_j,h_i\rangle,
 \qquad
 \dot U^*b_i=-\sum_j r_jh_j\langle b_j,b_i\rangle.
\]

Both are bounded pointwise. Consequently \(\|g_i\|_2\le K_T\). Combining (2) and (5) yields a bounded \(L^2(\Omega_1)^3\) generator acting on the vector \(q\):

\[
 \dot q_i=g_i-
 \sum_j B_i M_{r_j\Gamma_{ij}p(z_i)p(z_j)}q_j.
 \tag{7}
\]

In particular, \(q\) is bounded in \(H^1([0,T];L^2)^3\). This alone supplies no stronger spatial tail estimate. For example, the abstract equation \(q'=Q\), \(q(0)=0\), has the same bounded-generator form for every \(Q\in L^2\), with arbitrarily slow allowed \(L^2\) tails. This example tests only the implication from the bounded-generator assertion; it is not asserted to be a physical neural-network trajectory.

## 3. Baseline comparison and the exact missing term

Compare two trajectories with the same \(A_0\), and use bars for the reference and \(\Delta\) for differences. Define

\[
 D=\|\Delta w\|_2^2+\|\Delta U\|_{\rm HS}^2+
 \|\Delta C\|_2^2,
 \qquad a_i=r_iq_i,
 \qquad p_i=p(z_i).
\]

The upper-layer algebra is Lipschitz in this distance along paths satisfying (3). For example,

\[
 \Delta q_i=(\Delta A)^*b_i+
 \bar A^*\{(\Delta C)p(v_i)+
 \bar C[p(v_i)-p(\bar v_i)]\},
 \quad
 \Delta v_i=\Delta A\,h_i+\bar A\Delta h_i.
\]

Since \(\|\Delta A\|_{\rm op}\le\|\Delta U\|_{\rm HS}\),

\[
 \|\Delta q_i\|_2+\|\Delta h_i\|_2+
 |\Delta r_i|+\|\Delta a_i\|_2\le K_T\sqrt D.
 \tag{8}
\]

Expanding (4) in the same way also gives
\(\|\Delta g_i\|_2\le K_T\sqrt D\). To check the potentially delicate product in (4), both \(\dot U h_i\) and \(C\) are bounded pointwise, while their differences are bounded in \(L^2\) by \(K_T\sqrt D\); \(\phi''\) is Lipschitz with bounded values. Thus each difference is a product with only one small \(L^2\) factor.

The raw comparison identity has the form

\[
 \frac12\dot D=R-
 \sum_i\langle\Delta z_i,\Delta p_i\,\bar a_i\rangle,
 \qquad |R|\le K_TD.
 \tag{9}
\]

The last term is exact. Its first-order quadratic version is
\(-\sum_i\bar r_i\langle\bar q_i\phi''(\bar z_i),(\Delta z_i)^2\rangle\).
It has no definite sign under the physical residual feedback.

The same multiplication appears directly in the physical loss Hessian. For a bounded first-layer variation \(\xi\), with \(\xi_i=\xi\cdot u_i\), fixing \(A,C\) gives

\[
 D^2E[\xi,\xi]
 =\sum_i (Df_i[\xi])^2+
 \sum_i r_i\left\{
 \left\langle C\phi''(v_i),[A(p_i\xi_i)]^2\right\rangle
 +\left\langle q_i\phi''(z_i),\xi_i^2\right\rangle
 \right\}.
 \tag{10}
\]

The first term is nonnegative and the first term in braces is bounded by \(K_T\|\xi\|_2^2\). The second term in braces is the remaining first-layer curvature. Equation (10) retains the physical gradient structure; replacing the dynamics by arbitrary controls is unnecessary to exhibit it.

For a fixed reference, put

\[
 \tau_T(R)=\max_i\sup_{0\le t\le T}
 \|\bar q_i(t)\,1_{|\bar q_i(t)|>R}\|_2.
\]

Continuity of the reference path in \(L^2\), compactness of its time image, and a finite-net argument imply \(\tau_T(R)\to0\). Splitting (9) at \(R\), using both \(|\Delta p_i|\le\|\phi''\|_\infty|\Delta z_i|\) and the boundedness of \(p\), gives

\[
 \dot D\le K_T(1+R)D+K_T\sqrt D\,\tau_T(R).
 \tag{11}
\]

For \(e=\sqrt D\), this supplies the modulus

\[
 \dot e\le K_T\omega_T(e),
 \qquad
 \omega_T(e)=\inf_{R\ge1}\{(1+R)e+\tau_T(R)\}.
 \tag{12}
\]

An Osgood conclusion would require
\(\int_{0+}ds/\omega_T(s)=\infty\). Indeed, integrating the differential inequality after dividing by \(\omega_T(e)\), with a positive initial regularization, forces a zero-initial-distance solution to remain zero when this integral diverges. The assertion \(\tau_T(R)\to0\) does not verify that condition. A power tail \(\tau_T(R)\asymp R^{-\alpha}\) produces \(\omega_T(e)\asymp e^{\alpha/(\alpha+1)}\), whose reciprocal is integrable at zero. An exponential tail is one sufficient stronger condition: it gives \(\omega_T(e)\lesssim e[1+\log(1/e)]\). Such a tail has not been proved here.

## 4. Adding `q` and `h` distances

Take the concrete positive augmentation

\[
 \mathcal D_{\lambda,\mu}
 =\tfrac12D+\tfrac\lambda2\sum_i\|\Delta q_i\|_2^2+
 \tfrac\mu2\sum_i\|\Delta h_i\|_2^2,
 \qquad \lambda,\mu\ge0.
\]

By (8), it is equivalent to \(D\) for fixed \(\lambda,\mu\). Define
\(\ell_i=\mu\Delta h_i+\lambda B_i\Delta q_i\). From (5),

\[
 \Delta\dot q_i=\Delta g_i+B_i\Delta\dot h_i+
 \Delta B_i\dot{\bar h}_i,
\]

and from (2),

\[
 \Delta\dot h_i
 =-p_i\sum_j\Gamma_{ij}(p_j\Delta a_j+\Delta p_j\bar a_j)
 +\Delta p_i\dot{\bar z}_i.
 \tag{13}
\]

Using self-adjointness of \(B_i\), all terms in
\(\dot{\mathcal D}_{\lambda,\mu}\) are bounded by \(K_TD\) except the following exact displayed remainder:

\[
 \begin{split}
 \mathcal T_{\lambda,\mu}={}&
 -\sum_j\left\langle
 \Delta z_j+\sum_i\Gamma_{ij}p_i\ell_i,
 \Delta p_j\bar a_j\right\rangle\\
 &+\sum_i\langle\ell_i\Delta p_i,\dot{\bar z}_i\rangle
 +\lambda\sum_i\langle\Delta q_i,
 \Delta B_i\dot{\bar h}_i\rangle.
 \end{split}
 \tag{14}
\]

Thus the original term in (9) is still present. Self-adjointness moves \(B_i\) onto \(\Delta q_i\); it does not create an opposite copy of that term. The two additional first-line/second-line driver terms have no sign supplied by (1).

The final term in (14) introduces a second concrete obstacle. Set
\(m_i=C\phi''(v_i)\). The exact expansion

\[
 \Delta B_i=(\Delta A)^*M_{m_i}A+
 \bar A^*M_{\Delta m_i}A+
 \bar A^*M_{\bar m_i}\Delta A
\]

has harmless first and third terms when paired as in (14). The middle term contributes

\[
 \lambda\int_{\Omega_2}
 (\bar A\Delta q_i)
 \left\{\Delta C\,\phi''(v_i)+
 \bar C[\phi''(v_i)-\phi''(\bar v_i)]\right\}
 (A\dot{\bar h}_i).
 \tag{15}
\]

As written, (15) is well-defined: the braced factor is bounded, and the other two factors are in \(L^2\). To make that factor small at rate \(\sqrt D\), however, the available bounds are only
\(\|\Delta C\|_2+\|\Delta v_i\|_2\lesssim\sqrt D\).
Applying the Lipschitz bound for \(\phi''\) creates three \(L^2\) factors. There is no bound of the form \(K_TD\) from (3) and (8). A truncation argument requires tails of the reference upper-layer velocity \(\bar A\dot{\bar h}_i\), after absorbing the small \(\Delta A\dot{\bar h}_i\) part. These tails are another unproved estimate, rather than a cancellation of the tails in (11).

## 5. Subtracting the upper-layer linearization

A more targeted candidate is

\[
 \eta_i=\Delta q_i-\bar B_i\Delta h_i.
\]

At finite width, differentiating this identity gives the exact cancellation

\[
 \dot\eta_i=\Delta g_i+\Delta B_i\dot h_i-
 \dot{\bar B}_i\Delta h_i.
 \tag{16}
\]

The term \(\bar B_i\Delta\dot h_i\) has disappeared. This is the useful compensation supplied by (5). It does not supply a compensating term for (9).

Moreover,

\[
 \begin{split}
 \dot{\bar B}_i={}&
 \dot{\bar U}^{*}M_{\bar C\phi''(\bar v_i)}\bar A+
 \bar A^*M_{\bar C\phi''(\bar v_i)}\dot{\bar U}\\
 &+\bar A^*M_{\dot{\bar C}\phi''(\bar v_i)
 +\bar C\phi'''(\bar v_i)\dot{\bar v}_i}\bar A.
 \end{split}
 \tag{17}
\]

The last multiplier contains
\(\dot{\bar v}_i=\dot{\bar U}\bar h_i+\bar A\dot{\bar h}_i\).
The first summand is bounded pointwise, but the second is only controlled in \(L^2\). In the derivative of \(\|\eta_i\|_2^2/2\), the exact uncontrolled part of (17) is

\[
 -\int_{\Omega_2}
 (\bar A\eta_i)\,
 \bar C\phi'''(\bar v_i)\,
 (\bar A\dot{\bar h}_i)\,
 (\bar A\Delta h_i).
 \tag{18}
\]

The three displayed image fields are only \(L^2\). The bounded middle coefficient does not give an \(L^1\) estimate for their product. Therefore even the population differentiation in (16) is not justified by the available hypotheses: \(\bar B_i(t)\) is a bounded, strongly continuous operator family, but its operator-norm derivative need not exist or be bounded. The finite identity identifies exactly the estimate a population justification would require.

For orientation, multiplication by an \(L^2\) function need not be a bounded quadratic form on \(L^2\). On a set of measure \(N^{-2}\), the functions \(X=N\) and \(u=N\) have unit \(L^2\) norms, while \(\int Xu^2=N\). This is only a norm inequality check explaining (18); it is not a model counterexample. Adding \(\|\eta\|_2^2\) to the raw distance leaves (9) and requires control of (18).

## 6. Time-integrated force

Let

\[
 F_i(t)=\int_0^t a_i(s)\,ds.
\]

Then \(\dot z=-\Gamma P(z)\dot F\). The difference \(\Delta F\) has a controlled derivative, since \(\|\Delta\dot F\|_2\le K_T\sqrt D\). Adding its squared norm creates no opposite term for (9).

The troublesome part of the integrated first-layer equation is

\[
 I_j(t)=\int_0^t\Delta p_j(s)\dot{\bar F}_j(s)\,ds.
\]

At finite width, integration by parts gives

\[
 \begin{split}
 I_j(t)={}&\Delta p_j(t)\bar F_j(t)\\
 &+\int_0^t\bar F_j\,\phi''(z_j)
 \sum_k\Gamma_{jk}\{p_k\Delta a_k+\Delta p_k\bar a_k\}\,ds\\
 &+\int_0^t\bar F_j
 [\phi''(z_j)-\phi''(\bar z_j)]
 \sum_k\Gamma_{jk}\bar p_k\bar a_k\,ds.
 \end{split}
 \tag{19}
\]

The last integral is an explicit remaining term. Both \(\bar F_j\) and \(\bar a_k=\bar r_k\bar q_k\) are controlled in \(L^2\), so their product is only controlled in \(L^1\). Neither the endpoint product nor the last two integrals have the required uniform \(L^2\) comparison bound. At population level, individual terms produced by this integration by parts need not even be \(L^2\), although the original integral is. Time regularity from (7) does not improve this spatial product estimate.

## 7. Obligations still open

The bounded self-adjoint identity (5) is valid and useful. The calculations above do not show that its physical symmetry cancels the first-layer multiplier in (9). A complete one-reference argument still needs, for example, one of the following precisely stated replacements:

1. A reference modulus for (9) satisfying the divergent-integral condition in (12), derived from the actual physical solution and canonical Gaussian layer actions.
2. A different coercive comparison functional with a proved differential inequality that cancels or bounds (9), and, if it differentiates \(B_i\), a justified treatment of the exact form (18).
3. A direct approximation Cauchy estimate controlling the corresponding defects and the terms (14), (15), or (19), uniformly as caps or widths are removed. Bounded \(H^1_tL^2\) norms alone do not provide this estimate.

Even a successful uniqueness estimate would leave the contract's canonical existence/strong identification, continuation from reached states, actual full-sequence finite-width convergence, the three true kernel blocks, and the named velocity, moment, integrated-speed, and raw-GD observables to establish. The bounded activation and Gaussian initialization have not been used here to prove the missing source-tail estimate. This report therefore records a bounded unsuccessful compensation attempt, not a resolution of the global-limit target.
