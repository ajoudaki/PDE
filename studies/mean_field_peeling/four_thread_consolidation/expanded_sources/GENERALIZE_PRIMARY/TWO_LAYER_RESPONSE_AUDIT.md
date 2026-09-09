# Two-hidden-layer response bound for unbounded smooth activations

This is a complete response/tail lemma for the fixed-mesh population Euler construction. It is not, by itself, the width-to-flow convergence theorem. It supplies the estimate that theorem needs. The argument supports two different, possibly unbounded, activations in \(C^2(\mathbb R)\) with bounded first and second derivatives, and an independent iid subGaussian stored readout at initialization. Constants are independent of the fixed number of training inputs when the loss is averaged with weights whose sum is one. The first-layer roots may be Gaussian with any positive semidefinite covariance whose diagonal is bounded.

The proof uses response derivatives in one direction at a time, with all population residuals, contractions, and response coefficients held fixed. It never takes the maximum of Gaussian variables over a refining time grid.

## Setup and exact response identities

There are \(m<\infty\) fixed inputs, weights \(\omega_b>0\) with \(\sum_b\omega_b=1\), \(|G_{ab}|\le g\), and \(|y_b|\le Y\). Let \(\phi^{(1)},\phi^{(2)}\in C^2(\mathbb R)\), and assume
\[
 |\phi^{(\ell)}(0)|\le L,\qquad
 \|\phi^{(\ell)\prime}\|_\infty\le L,\qquad
 \|\phi^{(\ell)\prime\prime}\|_\infty\le L,
 \quad \ell=1,2.
\]
In particular \(|\phi^{(\ell)}(z)|\le L(1+|z|)\). Positive initialization and learning-rate constants are fixed. Write \(P_{a,k}^{(1)}=(W_k^{(2)})^*\delta_{a,k}^{(2)}\), where
\[
 \delta_{a,k}^{(2)}=W_k^{(3)}\phi^{(2)\prime}(Z_{a,k}^{(2)}),\qquad
 \delta_{a,k}^{(1)}=\phi^{(1)\prime}(Z_{a,k}^{(1)})P_{a,k}^{(1)}.
\]
The stored readout is always \(W^{(3)}\). Population Euler with step \(\Delta\) obeys
\[
 Z_{a,k+1}^{(1)}=Z_{a,k}^{(1)}
 -2\kappa_1\Delta\sum_b\omega_bG_{ab}r_{b,k}
       \phi^{(1)\prime}(Z_{b,k}^{(1)})P_{b,k}^{(1)},
\]
\[
 W_{k+1}^{(3)}=W_k^{(3)}
 -2\kappa_3\Delta\sum_b\omega_b r_{b,k}H_{b,k}^{(2)},
\qquad
 r_{b,k}=\mathbb E[W_k^{(3)}H_{b,k}^{(2)}]-y_b.
\]
The middle matrix has the usual rank expansion with coefficient
\(-2\kappa_2\Delta\omega_b r_{b,s}\).

For the moment suppose the elementary RMS/operator estimate has supplied a time \(T_R>0\) and an \(R\ge1\), independent of \(m\), \(\Delta\), such that, for \(k\Delta\le T_R\), all of
\[
 |r_{a,k}|,\quad \|Z_{a,k}^{(1)}\|_2,\quad
 \|H_{a,k}^{(1)}\|_2,\quad \|Z_{a,k}^{(2)}\|_2,\quad
 \|H_{a,k}^{(2)}\|_2,\quad \|W_k^{(3)}\|_2,\quad
 \|\delta_{a,k}^{(2)}\|_2,\quad \|P_{a,k}^{(1)}\|_2,\quad
 \|W_k^{(2)}\|_{\rm op}
\]
are at most \(R\), after harmlessly enlarging \(R\). Here \(\|U\|_2=(\mathbb E|U|^2)^{1/2}\), only for population random variables. A direct derivation of this preliminary estimate appears below.

The fixed-program Gaussian response theorem gives centered Gaussian families \(\xi_{a,k}\), \(\eta_{a,k}\) with
\[
 \mathbb E[\xi_{a,k}\xi_{b,s}]
   =\sigma_2^2\mathbb E[H_{a,k}^{(1)}H_{b,s}^{(1)}],\qquad
 \mathbb E[\eta_{a,k}\eta_{b,s}]
   =\sigma_2^2\mathbb E[\delta_{a,k}^{(2)}\delta_{b,s}^{(2)}].
\]
Thus every marginal variance is bounded solely using \(R\). The two innovation families live in the two different neuron populations. At a fixed population, its primitive initialization roots are independent of that population's innovation family. No independence across times is asserted or used.

Define
\[
 C_{ak,bs}=\mathbb E\frac{\partial H_{a,k}^{(1)}}{\partial\eta_{b,s}}
 \quad(s<k),\qquad
 A_{ak,bs}=\mathbb E\frac{\partial\delta_{a,k}^{(2)}}{\partial\xi_{b,s}}
 \quad(s\le k).
\]
Then
\[
 Z_{a,k}^{(2)}=\xi_{a,k}
          +\sum_{b,s<k}B_{ak,bs}\delta_{b,s}^{(2)},
\qquad
 P_{a,k}^{(1)}=\eta_{a,k}
          +\sum_{b,s\le k}D_{ak,bs}H_{b,s}^{(1)},                    \tag{1}
\]
where the exact coefficients are
\[
 B_{ak,bs}=\sigma_2^2 C_{ak,bs}
  -2\kappa_2\Delta\omega_b r_{b,s}
          \mathbb E[H_{b,s}^{(1)}H_{a,k}^{(1)}],
\]
\[
 D_{ak,bs}=\sigma_2^2 A_{ak,bs}
  -\mathbf 1_{s<k}2\kappa_2\Delta\omega_b r_{b,s}
          \mathbb E[\delta_{b,s}^{(2)}\delta_{a,k}^{(2)}].          \tag{2}
\]
The initial-Gaussian response terms have \(\sigma_2^2\); the learned rank terms have \(\kappa_2\).

The external result used here is Theorem 2.10 and Box 1, with Remarks 2.11–2.12, of [Tensor Programs III](https://arxiv.org/pdf/2009.10685). Its fixed-program assumptions are independent Gaussian matrix entries of variance \(\sigma_2^2/n\), finitely many Gaussian primitive coordinate vectors, and polynomially bounded coordinate maps and measurements. The root covariance may be singular. Every fixed Euler construction, after its population scalar coefficients have been fixed, satisfies those hypotheses. The maps defining its values and the derivatives with respect to innovation slots have polynomial growth for a fixed number of steps. Only \(\phi,\phi',\phi''\) are required for these derivatives. The ordinary derivative form of the response theorem applies because these maps are differentiable in the innovation slots. A nonsmooth initialization transform is harmless: no response derivative differentiates its independent primitive root.

## A scalar moment estimate that avoids temporal maxima

For a scalar random variable put
\[
 N(U)=\sup_{p\ge2}\frac{\|U\|_p}{\sqrt p}.
\]
This is a norm on the random variables for which it is finite. In particular it satisfies the triangle inequality, and \(N(F(U))\le C(1+N(U))\) when \(|F(u)|\le C(1+|u|)\). Gaussian variables with bounded variance have bounded \(N\).

If \(N(U)\le S\), then for an absolute constant \(c_0\),
\[
 \mathbb E e^{U^2/(c_0 S^2)}\le2,
 \qquad
 \mathbb E e^{\lambda |U|}\le2e^{c_0\lambda^2S^2/2}
 \quad(\lambda\ge0).                                           \tag{3}
\]
For the first inequality, expand the exponential and use
\(\mathbb E|U|^{2j}\le S^{2j}(2j)^j\) and
\(j!\ge(j/e)^j\); \(c_0=8e\) suffices. The second inequality follows from
\(\lambda|u|\le u^2/(c_0S^2)+c_0S^2\lambda^2/4\), with a larger constant if desired.

Consequently, for arbitrarily dependent \(U_{b,s}\) satisfying the same marginal bound, \(t=k\Delta>0\), Jensen's inequality gives
\[
 \mathbb E\exp\!\left(\lambda\Delta\sum_{s<k,b}\omega_b|U_{b,s}|\right)
 \le \sum_{s<k,b}\frac{\Delta\omega_b}{t}
        \mathbb E e^{\lambda t|U_{b,s}|}
 \le2e^{C\lambda^2t^2S^2}.                                      \tag{4}
\]
The identical estimate without the index \(b\) holds for a single readout field at each time. This controls an integral of absolute values from marginal tails; it makes no assertion about a supremum over a refining grid.

## SubGaussian bounds under provisional response caps

All constants below can be made to hold with one fixed \(K\ge1\), depending only on \(R,L,g,\sigma_2,\kappa_1,\kappa_2,\kappa_3\), and the initial marginal \(N\)-bounds. In particular \(K\) does not depend on \(m,\Delta,k\). Choose \(K\) also to bound \(L\), \(2\kappa_1gR\), and \(2\kappa_3R\). It is fixed before the response caps and time are selected. The powers of \(K\) below are deliberately conservative so no later enlargement is implicit.

Suppose provisionally that
\[
 |C_{ak,bs}|\le c\Delta\omega_b,
 \qquad \sum_{b,s\le k}|A_{ak,bs}|\le a.                        \tag{5}
\]
For all times to which the caps apply, (2) and the RMS bounds imply
\[
 |B_{ak,bs}|\le K(c+1)\Delta\omega_b,
 \qquad \sum_{b,s\le k}|D_{ak,bs}|\le K(a+T).                  \tag{6}
\]
Take maxima of the scalar \(N\)-norms over the indicated finite input/time ranges, not maxima of the random variables. Denote the resulting bounds for \(H^{(1)},P^{(1)},H^{(2)},W^{(3)}\) temporarily by \(h,p,u,w\). Equation (1), the two Euler updates, and bounded activation derivatives give
\[
 h\le K+KTp,\qquad p\le K+K(a+T)h,
\]
\[
 u\le K+K(c+1)Tw,\qquad w\le K+KTu.                           \tag{7}
\]
For example, the forward-memory estimate uses
\(N(\delta_{b,s}^{(2)})\le L N(W_s^{(3)})\), and sums
\(\Delta\omega_b\) to at most \(T\). The backward-memory estimate uses the absolute row sum in (6). There are no products of two unbounded variables in these estimates.

If
\[
 T\le1/(4K),\quad K^2T(a+1)\le\tfrac12,\quad
 K(c+1)T\le1,\quad K^2(c+1)T^2\le\tfrac12,                  \tag{8}
\]
solving the two pairs in (7) gives
\[
 h\le4K,\qquad p\le5K^2(a+1),\qquad
 u\le4K,\qquad w\le2K.                                      \tag{9}
\]
All the \(N\)-norms are finite before the absorption in (7): at a fixed number of Euler steps, (1) and the bounded derivatives imply that each coordinate value has at most linear growth in the finite list of primitive roots and innovation coordinates. The deterministic growth constants may depend on the mesh before (9), but finiteness suffices to justify the algebraic absorption.

## The entrywise forward-response estimate

Fix one backward Gaussian slot \((b,s)\) and differentiate only with respect to that slot. Its derivative is zero in \(Z_{a,k}^{(1)}\) for \(k\le s\). At the next time it enters through the direct \(\eta_{b,s}\) term of \(P_{b,s}^{(1)}\), so the exact first pulse is
\[
 \frac{\partial Z_{a,s+1}^{(1)}}{\partial\eta_{b,s}}
 =-2\kappa_1\Delta\omega_bG_{ab}r_{b,s}
                  \phi^{(1)\prime}(Z_{b,s}^{(1)}).             \tag{10}
\]
Its absolute value is at most \(K^3\Delta\omega_b\). This exact weight is the reason the eventual existence time need not depend on the number of inputs.

Let \(j_k\) be the maximum absolute value of this fixed-slot derivative over all inputs and times from \(s+1\) through \(k\). For \(k>s\), differentiate the first-layer update. The direct derivative of the current innovation \(\eta_{a,k}\) is zero. In its response part, differentiation of (1) gives
\[
 \left|\frac{\partial P_{a,k}^{(1)}}{\partial\eta_{b,s}}\right|
 \le L\sum_{d,v\le k}|D_{ak,dv}|j_k\le K^2(a+T)j_k.
\]
The derivative of \(\phi^{(1)\prime}(Z_{d,k}^{(1)})P_{d,k}^{(1)}\)
has one term bounded by \(L|P_{d,k}^{(1)}|j_k\) and one bounded by
\(K^3(a+T)j_k\). Therefore
\[
 j_{k+1}\le\left[1+K^4\Delta\left(a+1+
               \sum_d\omega_d|P_{d,k}^{(1)}|\right)\right]j_k.
\]
Using (10) and \(1+x\le e^x\),
\[
 j_k\le K^3\Delta\omega_b
 \exp\!\left(K^4T(a+1)+K^4\Delta\sum_{v<k,d}\omega_d|P_{d,v}^{(1)}|\right).
\]
The extra terms with \(v\le s\) on the right are nonnegative and only enlarge it. Apply (4), then (9), and use
\(|C_{ak,bs}|\le L\mathbb E j_k\). Using (3) with \(c_0=8e\),
\[
 \frac{|C_{ak,bs}|}{\Delta\omega_b}
 \le2K^4\exp\!\left(K^4T(a+1)+25c_0K^{12}T^2(a+1)^2\right).            \tag{11}
\]
The random maximum \(j_k\) is only a maximum of sensitivities. Its controlling exponential contains a weighted time sum of \(|P|\), not the random maximum of \(|P|\).

## The backward-response row estimate

For a second-layer field, sum the absolute values of derivatives over all forward innovation slots. Write
\[
 e_{a,k}=\sum_{b,s\le k}
       \left|\frac{\partial Z_{a,k}^{(2)}}{\partial\xi_{b,s}}\right|,
 \qquad v_k=\max_a e_{a,k}.
\]
The readout root is independent of these slots and is held fixed when differentiating. Thus
\[
 \sum_{b,s}\left|\frac{\partial W_k^{(3)}}{\partial\xi_{b,s}}\right|
 \le K^2\Delta\sum_{u<k}v_u,
\]
and
\[
 \sum_{b,s}\left|\frac{\partial\delta_{a,k}^{(2)}}{\partial\xi_{b,s}}\right|
 \le K^3\Delta\sum_{u<k}v_u+K^3|W_k^{(3)}|v_k.                   \tag{12}
\]
Differentiate the first identity in (1) and use (6). The direct innovation contributes exactly one to the derivative row sum. Summing the historical readout-derivative terms first in their later time index yields
\[
 v_k\le1+K^4(c+1)\Delta\sum_{s<k}(T+|W_s^{(3)}|)v_s.
\]
The scalar discrete Gronwall inequality therefore gives
\[
 v_k\le\exp\!\left(K^4(c+1)T^2+
                   K^4(c+1)\Delta\sum_{s<k}|W_s^{(3)}|\right). \tag{13}
\]
Apply (4) with exponent twice as large and \(N(W_s^{(3)})\le2K\). In particular,
\[
 \|v_k\|_2\le\sqrt2\exp\!\left(K^4(c+1)T^2+
                              4c_0K^{10}(c+1)^2T^2\right),         \tag{14}
\]
with the same fixed \(K\). By (12), Cauchy–Schwarz and the RMS readout bound,
\[
 \sum_{b,s\le k}|A_{ak,bs}|
 \le K^3\left(T+\|W_k^{(3)}\|_2\right)\max_{u\le k}\|v_u\|_2
 \le2K^3(R+1)\exp\!\left(K^4(c+1)T^2+4c_0K^{10}(c+1)^2T^2\right).   \tag{15}
\]
The maximum on the middle line is outside the expectation; no norm of a time maximum of the readout or of \(v\) was introduced.

## A noncircular choice of caps and time

Fix
\[
 c=4K^4,\qquad a=4K^3(R+1).
\]
Now choose \(T>0\) no larger than \(T_R\) and one, satisfying (8) and
\[
 K^4T(a+1)+25c_0K^{12}T^2(a+1)^2\le\log2,
\]
\[
 K^4(c+1)T^2+4c_0K^{10}(c+1)^2T^2\le\log2.                           \tag{16}
\]
Every left side tends to zero with \(T\), so such a positive time exists. All constants were fixed before choosing \(T\). Equations (11) and (15) reproduce the caps (5).

To make the bootstrap logically causal, induct over the Euler time index. Initially there are no \(C\)-coefficients. The time-zero \(A\)-row is bounded directly by
\(\|\phi^{(2)\prime\prime}\|_\infty\mathbb E|W_0^{(3)}|\), which is below the cap by the choice of \(K\). Suppose the caps hold through step \(k-1\). The first-layer fields at step \(k\) only use \(P^{(1)}\) through step \(k-1\). Thus the first pair of (7), with \(h\) through \(k\) and \(p\) through \(k-1\), proves the needed first-layer marginal bounds. Their fixed-slot derivatives prove (11) at step \(k\), and hence the \(C\)-cap and the \(B\)-bound at that step. The second pair of (7) uses \(H^{(2)}\) through \(k\), and readout updates only through \(k-1\); it proves the second-layer/readout bounds. Equations (12)–(15) then prove the \(A\)-cap at step \(k\). Finally (1) gives the marginal \(P^{(1)}\)-bound at that step. This closes the induction without presupposing the current \(A\)-cap to prove itself.

Consequently, uniformly over \(\Delta\le T\), \(k\Delta\le T\), and inputs,
\[
 |C_{ak,bs}|\le4K^4\Delta\omega_b,\qquad
 \sum_{b,s\le k}|A_{ak,bs}|\le4K^3(R+1),
\]
and all \(Z^{(1)},H^{(1)},Z^{(2)},H^{(2)},W^{(3)},P^{(1)}\) have bounded marginal \(N\)-norm. Since both backward fields are bounded-derivative multiples of \(W^{(3)}\) or \(P^{(1)}\), they do also. In particular, there are \(c_1,C_1>0\) such that
\[
 \mathbb E e^{c_1|P_{a,k}^{(1)}|^2}
 +\mathbb E e^{c_1|W_k^{(3)}|^2}\le C_1.                     \tag{17}
\]
The squared tail norms are exponentially small in the cutoff squared. All assertions concern marginal tails, uniformly indexed by the mesh, and not exponential tails of a time supremum.

## The preliminary RMS/operator ball does not need bounded activations

At either finite width or in the bounded-operator population realization, define
\[
 q_k=1+\max_a\|Z_{a,k}^{(1)}\|_2+\|W_k^{(2)}\|_{\rm op}
           +\|W_k^{(3)}\|_2,
\]
where each finite-vector norm in this paragraph means explicitly
\(\|z_{a,k}^{(1)}\|_2/\sqrt n\) or \(\|W_k^{(3)}\|_2/\sqrt n\).
For clarity, this paragraph's use of \(q_k\) is only a scalar size bound, unrelated to an activation derivative. Linear growth of the activations and bounded \(\phi'\) give
\[
 \|H_{a,k}^{(1)}\|_2\le Cq_k,\quad
 \|Z_{a,k}^{(2)}\|_2+\|H_{a,k}^{(2)}\|_2\le Cq_k^2,
\]
\[
 |r_{a,k}|\le Cq_k^3,\quad
 \|\delta_{a,k}^{(2)}\|_2\le Cq_k,\quad
 \|P_{a,k}^{(1)}\|_2+\|\delta_{a,k}^{(1)}\|_2\le Cq_k^2.
\]
The first-layer update, the readout update, and
\(\|u\otimes v\|_{\rm op}=\|u\|_2\|v\|_2\)
then give
\[
 q_{k+1}\le q_k+C\Delta q_k^5.                               \tag{18}
\]
If \(q_0\le Q\), choose \(T_R\) so that
\(C(2Q)^5T_R\le Q\). A first-crossing induction in (18) proves
\(q_k\le2Q\) at all grid points with \(k\Delta\le T_R\).
Enlarging \(R\) gives every preceding RMS bound. Independent normalized Gaussian matrix initialization has bounded operator norm with probability tending to one; fixed-input empirical initial second moments converge. The population realization inherits the same operator bound. A common \(Q\), and thus a common \(T_R\), is independent of \(m\) for each fixed dataset under the assumed root/label bounds: the population initial bounds are uniform in \(a\), and the finite-width assertion is a finite union at fixed \(m\). This is not a uniform probability estimate for datasets growing with width.

## Initialization and exact limits of this result

Gaussian initial readout is directly within the finite-program theorem. The same is true for any independent iid scalar subGaussian initial readout law: if \(F\) is its distribution function and \(g\sim N(0,1)\), write
\(W_0^{(3)}=F^{-1}(\Phi(g))\), where \(\Phi\) is the standard Gaussian distribution function. The subGaussian upper and lower tail bounds imply
\[
 |F^{-1}(u)|\le C\left(1+\sqrt{\log\frac1u}
                            +\sqrt{\log\frac1{1-u}}\right).
\]
For Gaussian \(\Phi\), the two logarithms are at most \(C(1+g^2)\), using the elementary lower Gaussian tail bound obtained by integrating the density on \([|g|,|g|+1]\). Thus the quantile transform is polynomially bounded, in fact at most linear in \(|g|\), and is an admissible coordinate operation in TP III. Its innovation-slot derivatives are zero because it depends on an independent primitive root. This reduction also covers bounded and deterministic readout laws, and zero readout.

An analogous finite-program reduction can cover iid centered subGaussian first-weight entries when input dimension is fixed: represent each scalar entry by its Gaussian quantile transform and form the specified fixed input linear combinations. Uniform root \(N\)-bounds then follow from independence and a bounded subGaussian entry parameter. This is an optional extension; the proved estimates above require only uniform marginal root \(N\)-bounds plus a valid fixed-program initialization representation, not Gaussianity of the root itself. Arbitrary joint subGaussian root laws should not be silently included without such a representation.

The calculations are compatible with replacing square-loss residuals by any deterministic oracle coefficients whose magnitudes stay bounded in the preliminary ball. Joint convergence and feedback stability for a different loss additionally require the corresponding local regularity of those coefficients as functions of predictions; that issue is outside this lemma.

Nothing here covers ReLU, unbounded activation derivatives, nonGaussian middle matrices, arbitrary depth, all finite time horizons, or datasets growing with width. The proposed \(C^{1,1}\) extension can use mollification with uniform first/second derivative bounds and the supervisor's localized stability argument; this note proves the response bound for \(C^2\), and does not replace that separate passage to the limit.
