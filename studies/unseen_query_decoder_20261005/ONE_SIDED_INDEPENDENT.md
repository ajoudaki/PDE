# Independent real one-sided stability derivation

2026-10-06. Bounded independent author attempt on the assigned sharper
Taylor-source lemma. This is not an independent review, a promoted result,
or a proof of a complete passive decoder. No other route's findings were
read. No experiment or Git operation was performed.

The answer is positive, conditional on the five supplied source interfaces.
The real endpoint stability exponent can be bounded by
\(C\beta^{70L}(1+S\sqrt{\ell})\), with no algebraic factor
\(r=m/\gamma\). Keeping the original complex patch schedule, this gives
Taylor degree and local precision at most \(C\beta^{100L}Z\).
The argument must use Euclidean parameter blocks and compare perturbed
real flows through the true gradient field. It does not assert that the
noisy auxiliary field is a gradient field or that complex-time evolution
is monotone.

## 1. Scope, inherited bounds, and coordinates

The complete scientific inputs were FAST_TAYLOR_NOISE.md,
SANE_TAYLOR_SOURCE.md, PHYSICAL_PARAMETER_ACCOUNTING.md,
FAST_SCALAR_FORCING.md, and FAST_FINITE_SOURCE_BRIDGE.md. Their hashes at
the end of the read are recorded below. Links in those notes were not
followed. The research, rigorous-proof, canonical-notation, and linked
neural-network presentation instructions were read and applied.

Keep the source's network, all trained layers and physical mobilities,
zero initial readout, scientific event, full original label intersection,
and deterministic width gates. For \(m\) unit inputs
\(v_a\in\mathbb R^d\), width \(n\), and \(L\ge2\) hidden layers,
the actual forward pass and mean squared loss are
\[
 z_a^{(1)}=Av_a,\qquad
 z_a^{(j)}=W^{(j)}h_a^{(j-1)},\qquad
 h_a^{(j)}=\phi_j(z_a^{(j)}),\qquad
 f_a=\frac{w^Th_a^{(L)}}n,
 \qquad \mathcal L=\frac1m\sum_{a=1}^m(f_a-y_a)^2.
 \tag{1}
\]
Here \(A\in\mathbb R^{n\times d}\),
\(W^{(j)}\in\mathbb R^{n\times n}\) for \(2\le j\le L\),
and \(w\in\mathbb R^n\). Define the residual-free backward variables
\[
 k_a^{(L)}=w,\qquad
 \delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot k_a^{(j)},\qquad
 k_a^{(j)}=W^{(j+1)T}\delta_a^{(j+1)}.
 \tag{2}
\]
Write \(r_a=f_a-y_a\) for sample residuals, reserving the scalar
\(r\) below for the inverse normalized training gap. Set
\[
 r=m/\gamma,\quad Y=\|y\|_2/\sqrt m>0,\quad
 S=16Yr\le1,\quad \ell=\log(en),\quad B=\beta^{100L},
\]
\[
 Z=(a_0+1)\ell+\log(e+B(1+r)(m+d+2)),\qquad 1\le a_0\le12.
 \tag{3}
\]
The supplied activation envelope has \(\beta\ge10\), bounds the first
two derivatives on the half-strip, and bounds the other constants stated
in the source. Keep \(Y\ge n^{-1}\), \(Y\le\beta^{3L}\), and
\(r^{-1}\le\beta^{6L}\). Zero labels use the exact zero branch.

Introduce the real Euclidean parameter vector
\[
 x=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n).
 \tag{4}
\]
For a variation \(v=(E_A,E_2,\ldots,E_L,e_w)\), its Euclidean
norm \(|v|\) is the square root of the sum of squared Frobenius/vector
norms of these blocks. The source's norm is their sum, denoted here by
\(\|v\|_\Sigma\). With \(c_L=\sqrt{L+1}\),
\[
 |v|\le\|v\|_\Sigma\le c_L|v|.
 \tag{5}
\]
Let \(x_0\) be initialization, \(\tau=t/r\), and
\(U=(x-x_0)/Y\). Thus \(U\) is exactly the source's normalized
displacement, written in Euclidean blocks. Denote the reference trajectory
by \(X(\tau)\) and the true normalized field by \(\overline F\).

We retain the original \(T,h_j,H\) from FAST_TAYLOR_NOISE.md, with
equal patch lengths and the certified ceiling allowance. In particular
\[
 T<32\ell,\quad
 H\le CB(1+r)Z\sqrt\ell,\quad
 h_j^{-1}\le CB(1+r)\sqrt\ell.
 \tag{6}
\]
Put \(q(\tau)=2^{-\lfloor\tau/4\rfloor}\),
\(q_j=q(\tau_j)\), \(q_T=q(T)\), and
\[
 d_n=\frac{\beta^{-200L}q_T}{(1+r)^2\sqrt n},\qquad
 \Lambda_j=B(1+r)(1+q_j\sqrt\ell),\qquad M=B(1+r).
 \tag{7}
\]
The source supplies holomorphy in the \(\|\cdot\|_\Sigma\)-tube
of radius \(d_n\) about the reference on each complex patch disk,
\(\|D\overline F\|_\Sigma\le\Lambda_j\),
\(\|X'\|_\Sigma\le M\), and \(4h_j\Lambda_j\le1/8\).
It also supplies, throughout that tube,
\[
 \max_{a,j}\|k_a^{(j)}\|_\infty
       \le 2\beta^{40L}S\sqrt\ell,\qquad
 \frac{\|(r_a)_a\|_2}{\sqrt m}\le3Yq_j.
 \tag{8}
\]
The tube forward subtraction constant is \(\beta^{4L}\), output
subtraction constant is at most \(\beta^{8L}\), and nearby hidden
operators are bounded by eleven. These statements, and the local
arithmetic/forcing statements used below, are inherited interfaces; this
note does not reconstruct their Gaussian scientific event.

## 2. The loss gradient in the correct metric

Differentiating (1) in the coordinates (4) gives
\[
 \nabla_{A/\sqrt n}f_a=\frac{\delta_a^{(1)}v_a^T}{\sqrt n},
 \qquad
 \nabla_{W^{(j)}}f_a=\frac{\delta_a^{(j)}h_a^{(j-1)T}}n,
 \qquad
 \nabla_{w/\sqrt n}f_a=\frac{h_a^{(L)}}{\sqrt n}.
 \tag{9}
\]
The stated physical velocities are therefore exactly
\(\dot x=-\nabla_x\mathcal L(x)\). Time and amplitude normalization
give
\[
 \overline F(U)=-\frac rY\nabla_x\mathcal L(x_0+YU),
\]
\[
 D\overline F(U)
 =-\frac{2r}{m}\sum_a
   \left\{\nabla_xf_a\nabla_xf_a^T+r_a\nabla_x^2f_a\right\}.
 \tag{10}
\]
There is no remaining \(Y^{-1}\) in the derivative. On real parameters
the first matrix in braces is positive semidefinite in the Euclidean
inner product (4). This sign is generally unavailable in the sum norm
and unavailable on a complex time contour.

## 3. A dimension-free output Hessian bound throughout the tube

Fix any real state in a patch tube, any training sample, and a real
direction \(v=(E_A,E_2,\ldots,E_L,e_w)\). A prime in this section is
the derivative along the parameter line \(x+sv\), evaluated at zero;
it is not a time derivative. Thus
\[
 z^{(1)\prime}=\sqrt n E_Av_a,\qquad
 z^{(j)\prime}=E_jh^{(j-1)}+W^{(j)}h^{(j-1)\prime},\qquad
 h^{(j)\prime}=\phi_j'(z^{(j)})\odot z^{(j)\prime}.
 \tag{11}
\]
Taking the directional limit of the supplied tube forward subtraction
bound, or iterating (11), gives
\[
 \max_j\left\{\|z^{(j)\prime}\|_{2,n},
                      \|h^{(j)\prime}\|_{2,n}\right\}
       \le\beta^{4L}\|v\|_\Sigma,
 \qquad \|a\|_{2,n}=\|a\|_2/\sqrt n.
 \tag{12}
\]
The recurrence verifies this for every direction; it is not a bound only
on directions tangent to the reference trajectory.

The second forward derivative obeys
\[
 z^{(1)\prime\prime}=0,\qquad
 z^{(j)\prime\prime}
     =2E_jh^{(j-1)\prime}+W^{(j)}h^{(j-1)\prime\prime},
\]
\[
 h^{(j)\prime\prime}
   =\phi_j''(z^{(j)})\odot(z^{(j)\prime})^{\odot2}
       +\phi_j'(z^{(j)})\odot z^{(j)\prime\prime}.
\]
Insert these identities into
\(f_a''=2(\sqrt n e_w)^Th^{(L)\prime}/n+w^Th^{(L)\prime\prime}/n\).
Eliminating the second derivatives down the layers with (2) gives the
exact identity
\[
 \begin{split}
 f_a''={}&\frac2{\sqrt n}e_w^Th^{(L)\prime}
 +\frac2n\sum_{j=2}^L
       \delta_a^{(j)T}E_jh_a^{(j-1)\prime}\\
 &+\frac1n\sum_{j=1}^L
       k_a^{(j)T}\left[
       \phi_j''(z_a^{(j)})\odot(z_a^{(j)\prime})^{\odot2}\right].
 \end{split}
 \tag{13}
\]
All backward quantities in (13) belong to the state being differentiated,
which lies in the tube and hence satisfies (8).

The first term has magnitude at most
\(2\beta^{4L}\|v\|_\Sigma^2\). For each mixed-layer term use
\[
 \frac1n|\delta^TE_jh'|
 \le\|\delta\|_{2,n}\|E_j\|_F\|h'\|_{2,n},
 \qquad
 \|\delta_a^{(j)}\|_{2,n}
 \le2\beta^{40L+1}S\sqrt\ell.
 \tag{14}
\]
For each activation-curvature term use
\[
 \frac1n\left|k^T[\phi''(z)\odot(z')^{\odot2}]\right|
 \le\beta\|k\|_\infty\|z'\|_{2,n}^2.
 \tag{15}
\]
In particular, no maximum-coordinate bound on the variation \(z'\) is
needed. Converting \(z'\) itself to a coordinate maximum and then
multiplying two RMS bounds would introduce an unnecessary \(\sqrt n\).
The square in (15) is summed directly; only the backward carrier needs a
coordinate maximum, and that maximum occurs once.

Equations (12)--(15), followed once by
\(\|v\|_\Sigma^2\le(L+1)|v|^2\), prove the deliberately loose bound
\[
 |v^T\nabla_x^2 f_a\,v|
       \le\beta^{70L}(1+S\sqrt\ell)|v|^2.
 \tag{16}
\]
For example the curvature sum before norm conversion is at most
\(2L\beta^{48L+1}S\sqrt\ell\|v\|_\Sigma^2\);
the mixed sum and readout term are smaller powers. The factors
\(L(L+1)\) and all numerical factors fit inside (16) for
\(\beta\ge10,L\ge2\). Since the real Hessian is symmetric, (16)
also bounds its Euclidean operator norm. The bound is uniform over every
training sample, every state in the real tube, and every real variation.

## 4. Real one-sided Lipschitz integral

Discard only the negative Gram part of (10). Cauchy--Schwarz over samples,
(8), (16), and \(Yr\le1/16\) give
\[
 \begin{split}
 \langle v,D\overline F(U)v\rangle
 &\le 2r\left(\frac1m\sum_a|r_a|\right)
               \beta^{70L}(1+S\sqrt\ell)|v|^2\\
 &\le 6Yr\,q_j\beta^{70L}(1+S\sqrt\ell)|v|^2
 \le \mu_j|v|^2,
 \end{split}
 \tag{17}
\]
where
\[
 \mu_j=\beta^{70L}q_j(1+S\sqrt\ell),\qquad
 G=\sum_jh_j\mu_j
       \le9\beta^{70L}(1+S\sqrt\ell).
 \tag{18}
\]
The last step uses the supplied left-sum bound \(\sum_jh_jq_j\le9\).
Consequently \(G\le C\beta^{70L}\sqrt\ell\), with no algebraic
factor \(r\), and \(\mu_j\le\Lambda_j\).

At a fixed real time, the sum-norm tube is convex. Integrating
\(D\overline F\) along the segment between two states \(U,V\) in
that tube proves
\[
 \langle U-V,\overline F(U)-\overline F(V)\rangle
                         \le\mu_j|U-V|^2.
 \tag{19}
\]
This is a real one-sided Lipschitz estimate throughout the numerical
tube, not just along the reference trajectory.

The endpoint residual issue is substantive. The reference residual tends
to zero, whereas numerical error need not. Here the output change
anywhere in the tube is at most \(\beta^{8L}Yd_n\), and
\[
 \beta^{8L}d_n
 =\frac{\beta^{-192L}q_T}{(1+r)^2\sqrt n}\le q_T\le q_j.
 \tag{20}
\]
Thus (8) remains true even at the last patch. Replacing this tube by a
fixed radius without its \(q_T\) factor would require a separate
residual-floor term in (17). The supplied tube already pays for the
needed shrinking radius: \(\log(d_n^{-1})\le CZ\). No extra label
restriction is being imposed.

## 5. Forced Taylor maps: complex production, real propagation

The local coefficient-error construction of FAST_TAYLOR_NOISE.md and
FAST_SCALAR_FORCING.md yields a holomorphic auxiliary field
\(\overline F_j^{\rm num}(s/h_j,U)\), with real coefficients and
fixed realized forcing polynomials. On the tube its defect satisfies
\[
 \|\overline F_j^{\rm num}-\overline F\|_\Sigma\le\eta,
 \qquad \eta=C_N\delta,\qquad
 C_N=B^2(1+r)^2\sqrt\ell,
 \tag{21}
\]
provided
\[
 0<\delta\le\delta_0
 :=\frac{\beta^{-150L}Sq_T}{(1+r)^2\sqrt n}.
 \tag{22}
\]
It has complex derivative bound \(2\Lambda_j\). Fixed additional
physical pair and arithmetic budgets change absolute constants only.
The auxiliary field need not be a gradient, and its Hessian sign is not
used.

Let \(b\) be a real numerical anchor and
\(e_j=|b-X(\tau_j)|\). Suppose \(c_Le_j\le d_n/8\) and
\(4h_j\eta\le d_n/16\). The original complex contraction proof,
unchanged, constructs its local solution \(X^{\rm num}\) and gives
on \(|s|<4h_j\)
\[
 \|X^{\rm num}(s)-X(\tau_j+s)\|_\Sigma
                          \le2c_Le_j+8h_j\eta.
 \tag{23}
\]
This proof uses \(\Lambda_j\), not \(\mu_j\), and is valid only
because the original patch length is retained.

For real \(0\le s\le h_j\), write the difference equation as the
true-field difference plus the defect (21). Equation (19) gives
\[
 D^+|X^{\rm num}(s)-X(\tau_j+s)|
 \le\mu_j|X^{\rm num}(s)-X(\tau_j+s)|+\eta.
\]
At a zero difference this upper right derivative bound follows directly
from the difference equation; elsewhere divide the squared-norm
inequality by twice the norm. Multiplication by \(e^{-\mu_js}\) and
integration yield
\[
 |X^{\rm num}(s)-X(\tau_j+s)|
                         \le e^{\mu_js}(e_j+s\eta).
 \tag{24}
\]

The realized coefficient recurrence still computes the first \(K+1\)
Taylor coefficients of this auxiliary solution: no change to its causal
coefficient identification is needed. Apply Cauchy's formula to the
difference in (23) on the circle \(|s|=2h_j\). At any real
\(0\le s\le h_j\), the difference-series tail has Euclidean norm at
most \((2c_Le_j+8h_j\eta)2^{-K}\). The reference tail is at most
\(2Mh_j2^{-K}\). Hence, for \(K\ge4\), the committed Taylor
endpoint satisfies
\[
 e_{j+1}\le
   (1+2h_j\mu_j+2c_L2^{-K})e_j
       +C h_j\eta+2Mh_j2^{-K}.
 \tag{25}
\]
Here \(e^{\mu_jh_j}\le1+2\mu_jh_j\) because
\(\mu_jh_j\le\Lambda_jh_j\le1/32\). Independent endpoint
rounding of Euclidean norm at most \(h_j\eta\) adds to the displayed
forcing term. It is not represented as a constant forcing that allegedly
preserves the same Taylor polynomial. The same estimates control every
interior polynomial value.

The entire endpoint recurrence is in the single norm \(|\cdot|\).
The factor \(c_L\) occurs in the exponentially small Taylor-tail term,
the tube admission test, and final observation conversion. It is never
multiplied once per patch as a change of stability norm.

## 6. Explicit degree and precision choices

Let
\[
 \varepsilon=\frac1{c_L}
       \min\{d_n/128,n^{-a_0}/(128B)\},
\]
\[
 P_*=1+G+
 \log\frac{2^{40}(1+c_L)(M+1)(C_N+1)(H+1)(T+1)}
                  {\varepsilon\min\{1,\delta_0\}}.
 \tag{26}
\]
All logarithms are natural unless their base is displayed. Choose
\[
 K=8+\left\lceil\frac{8P_*}{\log2}\right\rceil,
 \qquad
 \delta=\min\left\{\delta_0,
        \frac{\varepsilon e^{-8P_*}}{2^{20}C_N(T+1)}\right\},
 \qquad
 e_0\le\frac{\varepsilon e^{-8P_*}}{2^{20}}.
 \tag{27}
\]
The exact-root version has \(e_0=0\). These are conservative choices
that also make the activation interpolation degree \(J=O(K)\).

The product of (25)'s multipliers is at most
\[
 \exp\{2G+2c_LH2^{-K}\}\le e^{2G+1}.
\]
Summing its forcing and source tails bounds every endpoint by
\[
 e^{2G+1}\{e_0+CTC_N\delta+2MT2^{-K}\}.
 \tag{28}
\]
The choices (26)--(27), including their absolute slack, put this and
the interior bound below \(\varepsilon/8\). Thus
\(c_Le_j<d_n/8\) and \(4h_j\eta<d_n/16\) hold inductively,
closing every real-anchor and complex-tube admission condition. Further
fixed error-budget allocations only enlarge the numerical constants.
The physical sum-norm error is at most \(Yc_L\varepsilon/8\).
Uniform prediction sensitivity \(B\), followed by the unchanged fitting
tail after \(T\), gives the inherited normalized all-time whole-sphere
accuracy \(n^{-a_0}\).

To account for all scales, the inherited gates give
\[
 S=16Yr\ge16\beta^{-6L}/n,
 \qquad
 \log\delta_0^{-1}+\log\varepsilon^{-1}\le CZ.
\]
The formulas for \(M,C_N,H,T,c_L\) give logarithms at most \(CZ\).
Together with (18), this proves
\[
 P_*\le C\{Z+\beta^{70L}\sqrt\ell\}\le CBZ,
 \qquad
 K+\log\delta^{-1}+\log(e_0^{-1})\le CBZ
 \tag{29}
\]
when a positive initial tolerance at the upper bound in (27) is used.
The \(e_0^{-1}\) term is omitted for exact initialization. The statement
concerns sufficient tolerances, not arbitrarily smaller chosen ones.

All the following local interfaces inherit this bound by their explicit
formulas, without changing their causal or physical meaning.

* Matrix-answer noise: choose
  \(b_\sigma=\lceil2K+\log_2(4/\delta)\rceil\), so
  \(\sigma4^K\le\delta/4\) and \(b_\sigma\le CBZ\).
* Real activation values and interpolation: the source's choices
  \(J\ge K+2\), \(J\ge\log_2(C\beta^2/\delta)\), and
  \(\nu\le\delta/(C\beta^25^J)\) have
  \(J+\log\nu^{-1}\le CBZ\). Its continuous value extension and
  centered-polynomial arithmetic are unchanged.
* Local dyadic arithmetic: the source tolerance contains \(4^{-K}\)
  and fixed polynomial factors in \(n,B,1+r,R,K\). Its working-word
  estimate is a sum of their logarithms and \(J\); hence it is at most
  \(CBZ\), apart from charged input/primitive descriptions.
* Current-operand physical pairs and guard tests: in
  FAST_SCALAR_FORCING.md, the actual rank factors and weights have
  \(\log A\le C(K+J+Z)\) by the same local disk, Cauchy, and centered
  interpolation bounds. Also \(\log N_{\rm sum}\le CZ+C\log(K+1)\).
  Its choice
  \(\epsilon_{\rm pair}\le\delta/(C4^KN_{\rm sum}^2A^{10})\)
  therefore needs \(CBZ\) bits. The first-guard prefix-completion
  proof continues to use the original complex local contraction and
  strict slack, now with (25)--(28) for anchors.
* Finite iid-packet implementation: the finite bridge's one-call
  quantities are fixed powers of \(n,R,b,\sigma^{-1}\), whose logarithms
  are now \(O(BZ)\). Its Gaussian truncation contributes
  \(O(Z+\log(1/\rho))\). Equations (20)--(23) there consequently give
  \(p_{\rm loc}\le C\{BZ+\log(1/\rho)\}\). Replace its initial-root
  allowance involving \(e^{-2E}\) by the explicit \(e_0\) allowance
  (27), requiring \(\sqrt d\epsilon_G/Y\le e_0\). This adds only
  \(CBZ\) bits using \(Y^{-1}\le n\). Its common finite
  postprocessing, posterior completion, and total-variation argument
  are unchanged inherited interfaces.

Since \(H\) is unchanged while \(K\le CBZ\), the associated
initialized action count can be stated as
\[
 R\le C\{d+mL B^2(1+r)Z^2\sqrt\ell\}.
 \tag{30}
\]
This is a count for the physical source and its specified finite
implementation. It is not total bit work or a passive decoder theorem.
All analytic-activation evaluation work and input encodings remain
charged. Nor does (29) replace a global Lipschitz requirement for an
unrelated expanded row-history map.

## 7. Bounded outcome and proof limitations

The sharper real one-sided integral is established from the supplied
tube bounds by the explicit Hessian expansion (13). It controls real
perturbed local flows, the Taylor difference tail, local physical pair
errors, and the inherited dyadic finite-source construction. The
full original labels are retained. The removal of an algebraic
\(m/\gamma\) factor is a precision improvement at the original patch
schedule; the original complex Jacobian bound and its dependence on
\(m/\gamma\) are still used locally to justify holomorphic solutions.

The main failure modes have explicit resolutions here: use the scaled
Euclidean metric for the Gram sign; sum squared vector variations in
the Hessian instead of applying a \(\sqrt n\) coordinate conversion;
use the tube's \(q_T\) factor to preserve residual decay at late times;
use one norm across real endpoints; retain absolute-norm estimates on
complex contours; and treat the auxiliary non-gradient field solely as
a bounded forcing perturbation of the true field.

The result remains conditional on the original scientific event and the
five given physical/source interfaces. This independent derivation does
not certify unassigned source proofs, change their stochastic width
threshold, or complete any unresolved passive-query stability theorem.

Input SHA-256 values:

| Input | SHA-256 |
|---|---|
| FAST_TAYLOR_NOISE.md | `71c67ce4de343077f3795aa9a9892052560da7b7ab51a59f6609027744c8881c` |
| SANE_TAYLOR_SOURCE.md | `24b8d368da31e9d8bf00bb1c7fc85f75cb0efcc30a9cbc8409ac9c520bb916af` |
| PHYSICAL_PARAMETER_ACCOUNTING.md | `395301fcca55af8937281f22b56c3ffe366d8e46fe7b4b12aeec35e5ca462279` |
| FAST_SCALAR_FORCING.md | `6b74c2a49046bdce4d30b0bf46535ddbc6498332b91fb3d516fefb0bd09f23bb` |
| FAST_FINITE_SOURCE_BRIDGE.md | `7ef69972a213fb26b77cd1c0ed4dcbd8b7d12f9e3b06906f351f7443f79894e6` |
