# Nonodd endpoint comparison: scalar and mean-adapted routes

2026-10-11. Scoped continuation of the endpoint investigation. The initial
inputs were `paper/compact.tex`, `paper/compact_fitting.tex`,
`ODD_DEPTH_ENDPOINT.md`, and `PRODUCT_QUERY_ROUTE.md`. The supervisor then
explicitly added the complete `paper/compact_foundations.tex`; its source
budget is used below. The rigorous-math and canonical-notation skills and
the neural-network notation reference were applied. No other study or
archived book source was used.

The strongest result is the mean-adapted comparison in Section 5: the actual
nonodd endpoint is within \(De(Y/\lambda)^2/\sqrt n\) in centered Gaussian
query \(L^2\) of the explicitly defined comparator (19), with
\(D\le\beta^{16L}\) and no stronger label cap. Anti-concentration for that
comparator remains open because its biases depend on training. Sections
2--4 record the direct comparison to ordinary frozen features: an exact
arbitrary-depth mixed-moment reduction and a two-layer estimate at the
weaker scale \(C(Y/\lambda)^3/\sqrt n\). The source budget's normalization
cannot silently be replaced by the smaller interpolation norm.

## 1. Actual network, conditioning, and the readout estimate

Use the canonical network and its actual gradient flow:

\[
 h^{(1)}(x)=\phi_1(W^{(1)}v),\quad
 z^{(j)}(x)=W^{(j)}h^{(j-1)}(x),\quad
 h^{(j)}(x)=\phi_j(z^{(j)}(x)),\quad
 f_n(x)=n^{-1}w^\top h^{(L)}(x),\qquad v=x/\sqrt d,
\]
\[
 r_a=f_n(x_a)-y_a,\quad \mathcal L=m^{-1}\sum_a r_a^2,
\]
\[
 \dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,
 \quad
 \dot W^{(j)}=-\frac2{nm}\sum_a r_a\delta_a^{(j)}h_a^{(j-1)\top},
 \quad
 \dot w=-\frac2m\sum_a r_a h_a^{(L)}.
\tag{1}
\]

Here \(j\ge2\) in the middle equation,
\(\delta_a^{(L)}=w\odot\phi_L'(z_a^{(L)})\), and
\(\delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot
W^{(j+1)\top}\delta_a^{(j+1)}\). The initialization is the paper's
independent Gaussian initialization with \(w_0=0\). Retain its activation
assumptions and label cap. Write

\[
 \lambda=\gamma/m\le1,\quad \varepsilon=Y/\lambda,
 \quad \rho(t)=\|r(t)\|/\sqrt m,
 \quad s=\max(1,\max_j\|\phi_j'\|_\infty),
 \quad b_2=\max_j\|\phi_j''\|_\infty.
\]

The derivative suprema here are on the real axis; \(s,b_2\le\beta\).
Let \(S\subset\mathbb R^d\) be the proper training span and fix a unit
query \(v\in S^\perp\). Condition only on the active initialization: the
first-layer Gaussian coordinates on \(S\), and all hidden matrices.
The entire training trajectory is measurable under this conditioning, and

\[
 Z=W_0^{(1)}v\sim N(0,I_n),\qquad
 W_t^{(1)}v=Z.
\tag{2}
\]

The query forward recursion therefore starts with \(h^{(1)}(Z)=\phi_1(Z)\).
The fitting event can be chosen using the active problem alone. On it,
hidden operator norms are at most nine, training feature RMS is at most
\(2H\), and \(\int_0^\infty\rho\le2\varepsilon\), where
\(H=\max_{0\le j\le L}\sqrt{Q^{(j)}_{11}}\).

Use the fitting constants

\[
 D_j=s(9s)^{L-j},\quad U_1=D_1,\quad U_j=2HD_j\ (j\ge2),
 \quad F_1=sU_1,\quad F_j=s(2HU_j+9F_{j-1}),\quad F=F_L.
\]

Set \(B_t=[h^{(L)}(t,x_a)]_{a=1}^m/\sqrt n\), \(u_t=w_t/\sqrt n\),
and

\[
 u_*=B_0(B_0^\top B_0)^{-1}y,\qquad e=\|u_*\|.
\tag{3}
\]

The readout comparison in `ODD_DEPTH_ENDPOINT.md`, Section 2, uses no
oddness. Its ingredients are \(\dot u_t=-(2/m)B_t r_t\),
\(\|B_t-B_0\|_{\rm op}/\sqrt m\le
2F(\sup_{s\le t}\|u_s\|)\int_0^t\rho\), and the identity

\[
 \tfrac12\partial_t\|u_t-u_*\|^2
 =-2\rho^2+\frac2m\langle(B_t-B_0)^\top u_*,r_t\rangle.
\]

Integration first gives \(\sup_t\|u_t\|\le3e\). Projecting the
integrated readout equation onto the orthogonal complement of
\(\operatorname{range}B_0\), and using endpoint interpolation on its range,
then gives the same estimates

\[
 e\le\sqrt2Y/\sqrt\lambda,\qquad
 \sup_t\|u_t\|\le3e,\qquad
 \|u_\infty-u_*\|\le120Fe\varepsilon^2,
 \qquad
 \|\dot W_t^{(j)}\|_F\le2U_j\rho(t)\|u_t\|
 \quad(2\le j\le L).
\tag{4}
\]

Thus the changed readout is already controlled with the correct \(e\)
factor. No centered activation has been substituted into the network.
For the first layer the corresponding velocity bound is
\(\|\dot W_t^{(1)}\|_F/\sqrt n\le2U_1\rho(t)\|u_t\|\);
the unnormalized bound in (4) is used only for hidden mixers.

## 2. An arbitrary-depth centered scalar inequality

In this section every norm and expectation over \(Z\) is conditional on
the active initialization. For a scalar random variable \(X(Z)\), write
\(\|X\|_{2,c}=(\mathbb E_Z|X-\mathbb E_ZX|^2)^{1/2}\).
Let \(a\in\mathbb R^n\) be any fixed vector under this conditioning, and
put \(a_{\rm rms}=\|a\|/\sqrt n\). Use the actual hidden path and define
the backward factor before the activation derivative by

\[
 p_t^{(L)}(Z)=a,\qquad
 p_t^{(j)}(Z)=W_t^{(j+1)\top}
       [\phi_{j+1}'(z_t^{(j+1)}(Z))\odot p_t^{(j+1)}(Z)].
\tag{5}
\]

This is an explicitly defined linear response to \(a\); when \(a=w_t\)
it is the ordinary current backward factor, and when \(a=w_\infty\)
it is generally a different, mixed-time response.

Define \(J_t^{(j)}=D_Zh_t^{(j)}\). Then

\[
 \|J_t^{(j)}\|_{\rm op}\le K_j^+,
 \quad K_j^+=s(9s)^{j-1},\qquad
 \|\phi_j'(z_t^{(j)})\odot p_t^{(j)}\|
       \le D_j\|a\|.
\tag{6}
\]

The derivative of the query preactivation along training obeys the exact
recursion

\[
 \dot z_t^{(1)}=0,\qquad
 \dot z_t^{(j)}=\dot W_t^{(j)}h_t^{(j-1)}
       +W_t^{(j)}[\phi_{j-1}'(z_t^{(j-1)})\odot\dot z_t^{(j-1)}].
\tag{7}
\]

For \(j\ge2\), let

\[
 M_j(t;a)=
 \left(\frac1n\mathbb E_Z\sum_i
       |p_{t,i}^{(j)}(Z)|^2|\dot z_{t,i}^{(j)}(Z)|^2\right)^{1/2},
 \qquad
 A_L=2\sum_{j=2}^L K_{j-1}^+D_jU_j.
\tag{8}
\]

The following inequality is proved without any moment assumption beyond
the Gaussian input and the fitting estimates:

\[
 \left\|\frac1n a^\top(h_\infty^{(L)}-h_0^{(L)})\right\|_{2,c}
 \le\frac1{\sqrt n}\left[
 A_La_{\rm rms}\int_0^\infty\rho(t)\|u_t\|\,dt
 +b_2\sum_{j=2}^L(9s)^{j-1}\int_0^\infty M_j(t;a)\,dt\right].
\tag{9}
\]

To prove it, differentiate the product formula for
\(\nabla_Z(a^\top h_t^{(L)})=J_t^{(L)\top}a\).
A differentiated matrix \(W_t^{(j)}\) contributes

\[
 J_t^{(j-1)\top}\dot W_t^{(j)\top}
 [\phi_j'(z_t^{(j)})\odot p_t^{(j)}].
\]

Its Euclidean norm is at most
\(2K_{j-1}^+D_jU_j\rho(t)\|u_t\|\|a\|\), by (4) and (6).
A differentiated activation derivative at layer \(j\ge2\) contributes

\[
 (D_Zz_t^{(j)})^\top
 [\phi_j''(z_t^{(j)})\odot\dot z_t^{(j)}\odot p_t^{(j)}].
\]

Its Gaussian \(L^2\) norm is at most
\(b_2(9s)^{j-1}\sqrt n M_j(t;a)\), since
\(\|D_Zz_t^{(j)}\|\le9K_{j-1}^+=(9s)^{j-1}\).
There is no layer-one term because \(Z\) is constant in training time.
Integrate these identities, apply Minkowski, divide by \(n\), and apply
Gaussian Poincare \(\|X\|_{2,c}\le\|\nabla_ZX\|_{L^2}\). This gives (9).
Poincare follows, for these smooth functions, by Gaussian Hermite expansion:
variance weights each positive-degree coefficient by one and gradient
energy by its degree. Bounded activation derivatives and linear growth
provide the required Gaussian integrability. They also bound the query
feature norm by \(C(\sqrt n+\|Z\|)\), so the time integrals in (9) are
finite at each fixed \(n\) using (4) and (7). Limits from finite time
therefore justify the endpoint version.

Nonzero intermediate means are present in (7). In fact, with
\(\mu_t^{(j)}=\mathbb E_Zh_t^{(j)}\), it is exactly

\[
 \dot z_t^{(j)}
 =\dot W_t^{(j)}\mu_t^{(j-1)}+W_t^{(j)}\dot\mu_t^{(j-1)}
 +\dot W_t^{(j)}(h_t^{(j-1)}-\mu_t^{(j-1)})
 +W_t^{(j)}\partial_t(h_t^{(j-1)}-\mu_t^{(j-1)}).
\tag{10}
\]

Centering the scalar output does not remove the first two terms from the
changed activation derivatives in the proof of (9).

Apply (9) with \(a=w_\infty\). The frozen-feature endpoint is
\(f_{\rm RF}=u_*^\top h_0^{(L)}/\sqrt n\), and
\(K_L^0=s(8s)^{L-1}\) is the initialized query Lipschitz constant.
The decomposition into changed readout against \(h_0^{(L)}\) and changed
features against \(w_\infty\), together with (4), gives

\[
 \|f_n(\infty,\sqrt d\,v)-f_{\rm RF}\|_{2,c}
 \le\frac1{\sqrt n}\left[
 (120K_L^0F+18\sqrt2 A_L)e\varepsilon^2
 +b_2\sum_{j=2}^L(9s)^{j-1}
                \int_0^\infty M_j(t;w_\infty)\,dt\right].
\tag{11}
\]

Here \(\|u_\infty\|\int\rho\|u_t\|\le18e^2\varepsilon\), and
\(e^2\varepsilon\le\sqrt2e\varepsilon^2\sqrt\lambda
\le\sqrt2e\varepsilon^2\). Thus all terms except the displayed mixed
moments already have the requested normalization.

A sufficient bridge, **not proved here**, would be

\[
 M_j(t;w_\infty)
 \le C_j\rho(t)\|u_t\|\|u_\infty\|.
\tag{12}
\]

It would yield a coefficient
\(120K_L^0F+18\sqrt2[A_L+b_2\sum_{j=2}^L(9s)^{j-1}C_j]\)
in front of \(e\varepsilon^2/\sqrt n\). This coefficient would still
need a quantitative activation/depth bound compatible with the existing
label cap. A weaker sufficient condition is the corresponding integrated
bound on the last term of (11). Fourth moments of the two factors in (8)
would suffice by Cauchy--Schwarz, but (12) cannot be declared a theorem
merely because those moments have been named.

## 3. What the existing source budget does prove

The source proof in `paper/compact_foundations.tex` removes its training
exponential budgets with probability tending to one. Apply that result to
the active training problem alone. Its scale is \(S_0=16\varepsilon\),
its budget is \(\mathcal B=1024\mathrm e^2L\), and its positive constant
\(\eta_*\) is defined there entirely from activation bounds and depth.
At the top layer \(k^{(L)}=w\). On \(0\le t\le T\), budget removal gives

\[
 \frac1n\sum_i\exp\left\{
       \eta_*\sup_{0\le t\le T}|w_i(t)|/S_0\right\}\le\mathcal B.
\]

For \(x\ge0\), \(x^4\le(4/(\mathrm e\eta_*))^4e^{\eta_*x}\).
The fitting tail and the source proof's real backward subtraction bound
make every additional coordinate change after \(T=32\log(en)/\lambda\)
at most \(S_0\), eventually. Therefore, for
\(M_i=\sup_{t\ge0}|w_i(t)|\),

\[
 \frac1n\sum_iM_i^4\le C_w^4\varepsilon^4,
 \qquad
 C_w=16\left[8\left\{
 \mathcal B\left(\frac4{\mathrm e\eta_*}\right)^4+1\right\}\right]^{1/4}.
\tag{13}
\]

This is an actual all-time training-readout bound for unbounded activations.
It is measurable under the active conditioning and introduces no additional
label cap. The same argument bounds each training backward carrier at its
source normalization. The source proof does not remove exponential budgets
for general passive-query carriers, does not treat the mixed-time response
(5) with \(a=w_\infty\), and does not normalize its moments by \(e\).

For two hidden layers these distinctions can be quantified directly.
Put \(H_i=\phi_1(Z_i)\), \(\mu=\mathbb EH_i\),
\(\sigma^2=\operatorname{Var}H_i\),
\(s_1=\|\phi_1'\|_\infty\), \(s_2=\|\phi_2'\|_\infty\),
and \(t_2=\|\phi_2''\|_\infty\). Let
\(E=W_\infty^{(2)}-W_0^{(2)}\). The canonical row update and training
feature bound imply

\[
 \|E_i\|\le\frac{8Hs_2\varepsilon}{\sqrt n}M_i,
 \qquad |E_i\mathbf1|\le8Hs_2\varepsilon M_i.
\tag{14}
\]

For \(G(Z)=n^{-1}w_\infty^\top[
\phi_2((W_0^{(2)}+E)H)-\phi_2(W_0^{(2)}H)]\), differentiating in \(Z\)
and using Poincare gives the exact estimate from `PRODUCT_QUERY_ROUTE.md`:

\[
 \operatorname{Var}_ZG\le\frac{2s_1^2}{n^2}\left[
 s_2^2\|E\|_F^2\|w_\infty\|^2
 +64t_2^2\left\{\sigma^2\sum_iw_{\infty,i}^2\|E_i\|^2
       +\mu^2\sum_iw_{\infty,i}^2(E_i\mathbf1)^2\right\}\right].
\tag{15}
\]

The factor 64 uses \(\|W_0^{(2)}\|\le8\). Independence of the first
layer's \(H_i\), including their nonzero mean, gives exactly the two weighted
sums. Since \(\|E\|_F\le12U_2e\varepsilon\) and
\(\|w_\infty\|\le3e\sqrt n\), (13)--(15) yield

\[
 \|G\|_{2,c}\le\frac1{\sqrt n}\left[
 72s_1s_2U_2e\varepsilon^2
 +64\sqrt2\,s_1t_2Hs_2C_w^2
        \sqrt{\mu^2+\sigma^2/n}\,\varepsilon^3\right].
\tag{16}
\]

Adding the readout term contributes at most
\(120K_2^0Fe\varepsilon^2/\sqrt n\). This proves a centered scalar
endpoint comparison for the actual two-layer network with arbitrary
permitted unbounded, nonodd activations. It improves the old product-query
note, where (13) was missing.

It still does not give the desired uniform coefficient multiplying
\(e\varepsilon^2\). The ratio \(\varepsilon/e\) is not controlled
by the stated fitting inequalities with an activation/depth-only constant.
For example, at the level of those inequalities it can have order
\(\lambda^{-1/2}\). Replacing the second term in (16) by
\(Ce\varepsilon^2\) therefore introduces an unproved strengthening.
Nor has a sufficiently small envelope for the source coefficient \(C_w\)
been established for an endpoint anti-concentration transfer.

## 4. Alternate exact representation and remaining bridge

There is an exact representation that uses current-time readouts in one
term. Since \(w_0=0\), integration by parts gives

\[
 \frac1n w_\infty^\top(h_\infty^{(L)}-h_0^{(L)})
 =\frac1n\int_0^\infty\left[
 w_t^\top\dot h_t^{(L)}
 +\dot w_t^\top(h_t^{(L)}-h_0^{(L)})\right]dt.
\tag{17}
\]

The first term uses actual current backward responses. The second uses
\(\dot w_t=-(2/m)\sum_a r_a h_a^{(L)}(t)\); expressing its feature
difference as a time integral introduces responses to training-feature
probes at a different time. Thus (17) is a useful alternative, but does
not itself eliminate the mixed-moment obligation.

For direct comparison with ordinary frozen features, the proved
arbitrary-depth result is (11), and the proved two-layer unbounded result
is (16) plus its stated readout term. Its missing bridge is a bound on
the actual passive-query mixed moments in (11), or an
equivalent bound obtained from (17), at the interpolation normalization
\(e\varepsilon^2\), with quantitatively sufficient activation/depth
constants. Training source moments at scale \(\varepsilon\), global
readout energy, and Frobenius displacements separately do not establish
that bridge. No full endpoint lower theorem is claimed here.

## 5. Verified mean-adapted comparator

The supervisor proposed a different comparator after the preceding scalar
reduction. It does recover the desired comparison constant without oddness.
It changes the remaining problem: anti-concentration is now needed for a
comparator whose biases depend on the trained state.

Keep the active conditioning from Section 1. For the actual endpoint query
features, set

\[
 \mu_\infty^{(j)}=\mathbb E_Zh_\infty^{(j)}(Z),\qquad
 b_j=W_\infty^{(j)}\mu_\infty^{(j-1)}\quad(2\le j\le L).
\tag{18}
\]

These are fixed vectors under the conditioning, rather than functions of
the realized query \(Z\). Their expectations are finite because the query
maps are Lipschitz with at most linear growth. Define a proof comparator
recursively by

\[
 \widehat h^{(1)}(Z)=\phi_1(Z),\qquad
 \widehat\mu^{(j)}=\mathbb E_Z\widehat h^{(j)}(Z),
\]
\[
 \widehat h^{(j)}(Z)=\phi_j\left(
 W_0^{(j)}[\widehat h^{(j-1)}(Z)-\widehat\mu^{(j-1)}]+b_j\right)
 \quad(2\le j\le L).
\tag{19}
\]

The expectation in (19) is evaluated after the preceding layer has been
constructed; there is no fixed-point equation. This comparator is not the
actual network with its activation function replaced by a centered one.
Its offsets explicitly retain the actual endpoint preactivation means.
It uses trained quantities and is only an analysis object.

The map \(Z\mapsto\widehat h^{(j)}(Z)\) is
\(K_j^0=s(8s)^{j-1}\)-Lipschitz: each subtracted mean and each bias is
constant in \(Z\). Gaussian Poincare therefore gives, for every
deterministic matrix \(E\),

\[
 \mathbb E_Z\|E(\widehat h^{(j)}-\widehat\mu^{(j)})\|^2
 \le(K_j^0)^2\|E\|_F^2.
\tag{20}
\]

This covariance estimate uses no oddness and no independence between
\(E\), the initialized mixers, and the biases.

Put \(E_j=W_\infty^{(j)}-W_0^{(j)}\) and
\(R_j=\|h_\infty^{(j)}-\widehat h^{(j)}\|_{L^2(Z;\mathbb R^n)}\).
The two preactivations have the same offset \(b_j\), so their exact
difference is

\[
 \begin{aligned}
 z_\infty^{(j)}-\widehat z^{(j)}
 ={}&W_\infty^{(j)}\left[
 (h_\infty^{(j-1)}-\mu_\infty^{(j-1)})
 -(\widehat h^{(j-1)}-\widehat\mu^{(j-1)})\right]\\
 &+E_j(\widehat h^{(j-1)}-\widehat\mu^{(j-1)}).
 \end{aligned}
\tag{21}
\]

Centering is an orthogonal projection in vector-valued Gaussian \(L^2\),
so the norm of the bracket in (21) is at most \(R_{j-1}\). Applying the
operator bound nine, (20), and the activation Lipschitz bound gives

\[
 R_1=0,\qquad
 R_j\le s\left[9R_{j-1}+K_{j-1}^0\|E_j\|_F\right].
\tag{22}
\]

Let \(M=\sup_t\|u_t\|\). Equation (4) yields
\(\|E_j\|_F\le4U_jM\varepsilon\). Thus, for the constant already
used in the odd-activation argument,

\[
 T_L=\sum_{j=2}^L s(9s)^{L-j}U_jK_{j-1}^0,
 \qquad R_L\le4M\varepsilon T_L\le12e\varepsilon T_L.
\tag{23}
\]

Define the scalar comparator
\(\widehat f=u_*^\top\widehat h^{(L)}(Z)/\sqrt n\).
The exact decomposition

\[
 f_n(\infty,\sqrt d\,v)-\widehat f
 =\frac{(u_\infty-u_*)^\top\widehat h^{(L)}}{\sqrt n}
 +\frac{u_\infty^\top(h_\infty^{(L)}-\widehat h^{(L)})}{\sqrt n}
\]

and (4), (20), and (23) prove

\[
 \|f_n(\infty,\sqrt d\,v)-\widehat f\|_{2,c}
 \le\frac{De\varepsilon^2}{\sqrt n},\qquad
 D=120K_L^0F+36\sqrt2\,T_L\le\beta^{16L}.
\tag{24}
\]

For the second term, \(\|u_\infty\|R_L\le36e^2\varepsilon T_L\)
and \(e^2\varepsilon\le\sqrt2e\varepsilon^2\). The envelope on \(D\)
uses only the activation/depth estimates for \(F,K_L^0,T_L\) proved in
the odd note; those numerical bounds themselves never used oddness.
Equation (24) therefore retains the original cap and the desired
interpolation normalization. It is a complete centered comparison lemma.

There is still no established random-feature CLT for \(\widehat f\).
At initialization, choosing \(b_j=W_0^{(j)}\mathbb E_Zh_0^{(j-1)}\)
would recover the usual initialized network exactly. The offsets (18)
instead depend on the whole trained state. Conditional on preceding
initialized layers, the last-layer rows in (19) are not supplied by the
known independent Gaussian-row construction: their biases, and potentially
the preceding comparator layers, depend on those same rows through
training. Conditioning on all biases does not restore that construction,
because the conditioned mixer rows need no longer have their original
independent Gaussian law.

Conditional on the active initialization, only \(Z\) is random. Equation
(20) gives an upper covariance bound for its comparator features, but no
lower bound or Gaussian limit for \(u_*^\top\widehat h^{(L)}\). Neither
the original top Gram diagonal nor (24) by itself supplies such a lower
bound. Thus adaptive bias dependence invalidates a direct invocation of
the existing frozen-feature row CLT; it has not been proved to destroy
anti-concentration of the actual comparator. A new anti-concentration or
conditional variance argument for (19) is the remaining obligation for
this route. No counterexample to that obligation is asserted.
