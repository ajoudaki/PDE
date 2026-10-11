# Quantitative paired-query innovation for GELU and SiLU

Scoped theoretical route, 2026-10-11. The proved result in this note is
\[
 V_{\mathrm{pair}}\ge 4^{-L}y^\top(Q^{(L)})^{-1}y.                 \tag{1}
\]
It holds for raw GELU at every hidden layer, raw SiLU at every hidden layer,
and arbitrary layerwise mixtures of these two activations. The bound is
uniform in the training geometry, sample count, labels and positive training
Gram gap. It resolves the quantitative frozen-innovation obstruction for
these activations. It does not itself prove a fluctuation-scale comparison
with the fully trained endpoint. Section 5 states that remaining implication
precisely and derives sufficient constants under the original label cap.

Scientific inputs, read in full, were `paper/compact.tex`,
`paper/compact_fitting.tex`, `NONODD_INNOVATION_ROUTE.md`, and
`ODD_DEPTH_ENDPOINT.md`. No other scientific source or current proof route
was consulted before freezing the result. The rigorous-math,
conjecture-audit, and canonical-notation skills and the neural-network
notation reference were applied. No numerical experiment was performed.

## 1. Setup and activation structure

Use the canonical network
\[
 z^{(1)}(x)=W^{(1)}x/\sqrt d,\qquad
 z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),\qquad
 h^{(\ell)}(x)=\phi_\ell(z^{(\ell)}(x)),\qquad
 f_n(x)=w^\top h^{(L)}(x)/n.
\]
There are fixed training inputs \(x_a\), \(1\le a\le m\), with
\(m\ge2\), \(\|x_a\|=\sqrt d\), fixed labels \(y\ne0\), and fixed
depth \(L\ge2\). The first-layer weights are independent \(N(0,1)\),
the hidden-layer weights are independent \(N(0,1/n)\), all blocks are
independent, and \(w(0)=0\). Put \(v_a=x_a/\sqrt d\). Their span is
proper, and the query direction \(v\) is a fixed unit vector orthogonal
to it. The population training Grams are
\[
 Q^{(0)}_{ab}=v_a^\top v_b,\qquad
 Q^{(\ell)}_{ab}=\mathbb E\phi_\ell(Z_a)\phi_\ell(Z_b),
 \quad Z\sim N(0,Q^{(\ell-1)}).
\]
Assume \(Q=Q^{(L)}\succ0\), and define
\[
 \gamma=\lambda_{\min}(Q),\qquad \lambda=\gamma/m\le1,
 \qquad Y=\|y\|/\sqrt m>0,\qquad
 e_0^2=y^\top Q^{-1}y>0.
\]
Retain the paper's envelope \(\beta\ge10\) and label cap
\(Y\le\lambda\beta^{-30L}\).

Write \(\Phi\) and \(\varphi\) for the standard normal distribution
function and density. The activations under consideration are
\[
 \phi(z)=z\Phi(z)\quad\hbox{or}\quad
 \phi(z)=\frac{z}{1+e^{-z}}.
\]
Each has the decomposition
\[
 \phi(z)=z/2+g(z),\qquad
 g(z)=z(\Phi(z)-1/2)\quad\hbox{or}\quad
 g(z)=\frac z2\tanh(z/2).                                       \tag{2}
\]
Thus \(g\) is even, \(g\ge0\), \(|g(z)|\le|z|/2\), and
\(|\phi(z)|\le|z|\) on the real axis. Its derivatives are respectively
\[
 g'(z)=\Phi(z)-1/2+z\varphi(z),\qquad
 g'(z)=\tfrac12\tanh(z/2)+\tfrac z4\operatorname{sech}^2(z/2).
\]
Both are bounded, odd and nonnegative for \(z\ge0\). Consequently
\(g\) is increasing as a function of \(|z|\). These are the only
activation-specific facts used to prove (1).

Both activations belong to the paper's analytic class. For completeness,
GELU is entire. On a horizontal strip \(|\operatorname{Im}z|\le a\),
\[
 |\Phi(x+iy)|\le 1+|y|e^{y^2/2}\varphi(x),\qquad
 |\varphi(x+iy)|=e^{y^2/2}\varphi(x).
\]
These follow by integrating the entire normal density vertically from
\(x\), and directly from its exponential formula. The identities
\(\phi'=\Phi+z\varphi\) and \(\phi''=(2-z^2)\varphi\) then give
bounded derivatives on each fixed strip, since every fixed polynomial in
\(|x|\) times \(\varphi(x)\) is bounded. SiLU is holomorphic on
\(|\operatorname{Im}z|<\pi\). To check bounds on the closed strip
\(|\operatorname{Im}z|\le1\), write \(s(z)=(1+e^{-z})^{-1}\).
For \(x=\operatorname{Re}z\ge1\), the reverse triangle inequality gives
\(|s|\le2\), \(|1-s|\le2e^{-x}\), and \(|1-2s|\le5\).
Direct differentiation yields
\[
 \phi'=s+zs(1-s),\qquad
 \phi''=2s(1-s)+zs(1-s)(1-2s).
\]
Thus \(|\phi'|\le2+4(x+1)e^{-x}\) and
\(|\phi''|\le8e^{-x}+20(x+1)e^{-x}\) on this half strip.
The identity \(\phi(z)-\phi(-z)=z\) gives
\(\phi'(z)+\phi'(-z)=1\) and \(\phi''(z)=\phi''(-z)\), which
bounds the negative half strip too. On the remaining compact rectangle
\(|x|\le1,|\operatorname{Im}z|\le1\), both derivatives are continuous
and have no pole. This proves the required derivative bounds with common
strip width \(a=1\), without choosing a smaller label cap.

## 2. Query variance propagation

Take two independent first-layer query columns with the same active
initialization, as in `NONODD_INNOVATION_ROUTE.md`. This is an auxiliary
sampling construction and does not require two unused input directions.
Define their population diagonal and cross moments by
\[
 q_0=1,\quad c_0=0,\qquad
 q_\ell=\mathbb E\phi_\ell(U)^2,\qquad
 c_\ell=\mathbb E\phi_\ell(U)\phi_\ell(V),                         \tag{3}
\]
where \((U,V)\) is centered Gaussian with both variances
\(q_{\ell-1}\) and covariance \(c_{\ell-1}\). All training-coordinate
diagonals also equal \(q_\ell\), and the two training-query columns both
equal \(c_\ell\mathbf1\). At the first layer the relevant input
covariances are zero; induction through the Gaussian covariance recursion
preserves these statements.

Global sign reversal \((U,V)\mapsto(-U,-V)\) and evenness of \(g_\ell\)
make every mixed linear-even expectation vanish. Therefore
\[
 \begin{aligned}
 q_\ell&=q_{\ell-1}/4+\mathbb E g_\ell(U)^2,\\
 c_\ell&=c_{\ell-1}/4+\mathbb E g_\ell(U)g_\ell(V),\\
 q_\ell-c_\ell
 &=\frac{q_{\ell-1}-c_{\ell-1}}4
    +\frac12\mathbb E\big(g_\ell(U)-g_\ell(V)\big)^2.
 \end{aligned}                                                   \tag{4}
\]
Nonnegativity of \(g_\ell\), its linear growth, and
\(|\phi_\ell(z)|\le|z|\) yield by induction
\[
 0\le c_\ell<q_\ell\le1,
 \qquad q_\ell\ge4^{-\ell},
 \qquad q_\ell-c_\ell\ge4^{-\ell}.                              \tag{5}
\]
In particular the independent part of the paired query cannot disappear
faster than the explicit exponential factor in (5).

## 3. Which half of the shared Gaussian carries training energy?

Let \((X,U,V)\) denote the centered Gaussian vector entering the final
activation: \(X\in\mathbb R^m\) are its training coordinates and
\(U,V\) the paired query coordinates. Its covariance is the population
augmented Gram at layer \(L-1\). In this section abbreviate
\(q=q_{L-1}\), \(c=c_{L-1}\), and put
\[
 A=(U+V)/2,\qquad B=(U-V)/2,\qquad
 \sigma^2=(q-c)/2.
\]
The Gaussian variables satisfy
\[
 \operatorname{Var}A=(q+c)/2>0,\quad
 \operatorname{Var}B=\sigma^2>0,\quad
 \operatorname{Cov}(X_a,A)=c,
 \quad B\ \hbox{is independent of }(X,A).                         \tag{6}
\]
Indeed both query cross columns agree, so \(\operatorname{Cov}(X_a,B)=0\),
and their equal variances give \(\operatorname{Cov}(A,B)=0\).
For jointly Gaussian variables, the characteristic function
\(\exp(-t^\top\Sigma t/2)\) factors when the cross-covariance block
vanishes. This proves the independence even if the training covariance
is singular.

Put \(b=Q^{-1}y\in\mathbb R^m\), and define
\[
 H=(\phi_L(X_a))_{a=1}^m,
 \qquad T=b^\top H,
 \qquad \mathbb ET^2=b^\top Qb=e_0^2.                            \tag{7}
\]
We prove the energy inequality
\[
 \mathbb E\big[T^2\mathbf1_{\{A\ge0\}}\big]\ge e_0^2/2.          \tag{8}
\]
It is the step that prevents correlation with training features from
destroying the desired lower bound.

For fixed \(a\), the conditional Gaussian distribution of \(X\) given
\(A=a\) has common coordinate mean and covariance
\[
 \mu\mathbf1,\qquad
 \mu=\frac{2c}{q+c}a,\qquad
 C=Q^{(L-1)}-\frac{2c^2}{q+c}\mathbf1\mathbf1^\top\succeq0.
\]
All its marginal variances equal
\[
 \tau^2=q-\frac{2c^2}{q+c}
       =\frac{(q-c)(q+2c)}{q+c}>0.                                \tag{9}
\]
For \(a\ge0\), we have \(\mu\ge0\). If
\(Z\sim N(\mu,\tau^2)\), nonnegativity of \(g_L\) gives
\(\mathbb Eg_L(Z)\ge0\). Also, using oddness of \(g_L'\),
\[
 \mathbb Eg_L'(Z)
 =\int_0^\infty g_L'(z)
 \left[p_\tau(z-\mu)-p_\tau(z+\mu)\right]\,dz\ge0,              \tag{10}
\]
where \(p_\tau(t)=(2\pi\tau^2)^{-1/2}e^{-t^2/(2\tau^2)}\).
The integrand is nonnegative because \(g_L'(z)\ge0\) for \(z\ge0\)
and \((z-\mu)^2\le(z+\mu)^2\). Boundedness of \(g_L'\) justifies
the integral and the splitting at zero.

Gaussian integration by parts gives, for every \(i,j\),
\[
 \mathbb E[X_i g_L(X_j)\mid A=a]
 =\mu\mathbb Eg_L(Z)+C_{ij}\mathbb Eg_L'(Z).                      \tag{11}
\]
To verify this also for singular \(C\), write
\(X=\mu\mathbf1+C^{1/2}G\) with a standard Gaussian vector \(G\),
and apply the one-variable identity
\(\mathbb E[G_k f(G)]=\mathbb E[\partial_k f(G)]\) to
\(f(G)=g_L(\mu+(C^{1/2}G)_j)\). The identity follows by integration
of the Gaussian density derivative; the boundary term vanishes because
\(g_L\) has at most linear growth. Multiplying by the entries of
\(C^{1/2}\) and summing gives (11).

Multiply (11) by \(b_i b_j\) and sum. By (10),
\[
 \begin{aligned}
 &\mathbb E[(b^\top X)(b^\top g_L(X))\mid A=a]\\
 &\quad=\mu(\mathbf1^\top b)^2\mathbb Eg_L(Z)
        +(b^\top Cb)\mathbb Eg_L'(Z)\ge0
        \qquad(a\ge0).                                         \tag{12}
 \end{aligned}
\]
No sign assumption on \(b\) or \(y\) is used. Let
\(M(a)=\mathbb E[T^2\mid A=a]\). The conditional distribution at
\(-a\) is the reflection of that at \(a\). By (2),
\[
 \begin{aligned}
 M(a)-M(-a)
 &=\mathbb E\left[
 \left(\tfrac12 b^\top X+b^\top g_L(X)\right)^2
 -\left(-\tfrac12 b^\top X+b^\top g_L(X)\right)^2
 \,\middle|\, A=a\right]\\
 &=2\mathbb E[(b^\top X)(b^\top g_L(X))\mid A=a]\ge0
 \qquad(a\ge0).
 \end{aligned}                                                   \tag{13}
\]
The distribution of \(A\) is symmetric and has no atom at zero.
Integrating (13) over \(a>0\) proves (8).

## 4. The weighted paired-query lower bound

For real \(a\ge0\) and \(b'\ge0\),
\(|a+b'|\ge|a-b'|\); the monotonicity of \(g_L\) in absolute value
therefore gives
\[
 \phi_L(a+b')-\phi_L(a-b')
 =b'+g_L(a+b')-g_L(a-b')\ge b'.
\]
Changing the sign of \(b'\) changes the sign of the difference.
Consequently
\[
 [\phi_L(a+b')-\phi_L(a-b')]^2\ge(b')^2
 \qquad(a\ge0,\ b'\in\mathbb R).                               \tag{14}
\]
Define the paired influence variance by
\[
 V_{\mathrm{pair}}
 =\mathbb E[(\phi_L(U)-\phi_L(V))^2T^2].                          \tag{15}
\]
The influence has mean zero because the two population training-query
columns agree. All its moments are finite by linear activation growth
and Gaussian moments. Using (14), independence in (6), (8), and (5),
\[
 \begin{aligned}
 V_{\mathrm{pair}}
 &\ge\mathbb E[B^2T^2\mathbf1_{\{A\ge0\}}]\\
 &=\sigma^2\mathbb E[T^2\mathbf1_{\{A\ge0\}}]
 \ge\frac{q_{L-1}-c_{L-1}}4e_0^2
 \ge4^{-L}e_0^2.
 \end{aligned}                                                   \tag{16}
\]
This proves (1). A pointwise lower bound uniformly over negative values of
\(A\) was not needed: the exact conditional Gaussian calculation (12)
ensures that the positive half already carries enough weighted energy.

## 5. Exact remaining endpoint implication and constants

This section is conditional on a centered correction estimate; it does
not assert that estimate. The actual training is gradient flow for
\(\mathcal L=m^{-1}\sum_a r_a^2\), \(r_a=f_n(x_a)-y_a\), with the
paper's block mobilities \((n,1,\ldots,1,n)\). Equivalently, with
\[
 \delta_a^{(L)}=w\odot\phi_L'(z_a^{(L)}),\qquad
 \delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot
       W^{(\ell+1)\top}\delta_a^{(\ell+1)},
\]
its equations are
\[
 \dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\quad
 \dot W^{(\ell)}=-\frac2{nm}\sum_a
 r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},\quad
 \dot w=-\frac2m\sum_a r_a h_a^{(L)}.
\]
Let \(\mathcal A_n\) be the sigma field generated by the first matrix
restricted to the training span and all hidden matrices at initialization.
It determines the training trajectory. The first equation shows that the
orthogonal query column \(Z=W^{(1)}_0v\sim N(0,I_n)\) stays fixed and
is independent of \(\mathcal A_n\). Define
\[
 B_0=[h_0^{(L)}(x_1),\ldots,h_0^{(L)}(x_m)]/\sqrt n,\quad
 u_*=B_0(B_0^\top B_0)^{-1}y,\quad e_n=\|u_*\|,
 \quad F_n(Z)=u_*^\top h_0^{(L)}(Z)/\sqrt n.
\]
On the vanishing-probability event of a singular Gram assign \(F_n\)
and \(e_n\) arbitrary values. Initialization convergence gives
\(e_n\to e_0\) in probability. Put
\[
 R_n(Z)=f_n(\infty,\sqrt d\,v)-F_n(Z).
\]
The needed additional implication is the following estimate on an
\(\mathcal A_n\)-measurable event of probability tending to one:
\[
 \|R_n-\mathbb E_ZR_n\|_{L^2_Z}
 \le\frac{D e_n}{\sqrt n}(Y/\lambda)^2,
 \qquad D\le\beta^{50L}.                                       \tag{17}
\]
Here the conditional expectation averages only the unused query column.
The constant \(D\) must be independent of width, training geometry,
sample count, gap and label amplitude. A smaller explicit bound on \(D\)
is equally sufficient. No bound on the absolute conditional mean of
\(R_n\) is required.

Here is a full constant check showing that (17) closes the endpoint lower
bound without strengthening the label assumption. The paired-query
anti-concentration statement (9) of `NONODD_INNOVATION_ROUTE.md` gives,
at \(\delta=1/4\), an active event of probability at least \(7/8\)
for sufficiently large individual widths, on which
\[
 \sup_{a\in\mathbb R}\Pr_Z\{|F_n(Z)-a|\le c_*/\sqrt n
       \mid\mathcal A_n\}\le1/4,
 \qquad c_*:=\frac{2^{-L}e_0}{1024}.                             \tag{18}
\]
Indeed that statement's admissible radius is
\(\sqrt{2\pi V_{\mathrm{pair}}}/1024\), at least \(c_*\) by (16).
The result (18) derives from conditional Gaussian-row central limits and
the paired conditional small-ball inequality in that source; it does not
assume neuron independence after conditioning on \(\mathcal A_n\).

Intersect with the fitting event, the event (17), and
\(e_n\le\sqrt2e_0\); these exclusions have total probability \(o(1)\)
by the stated hypothesis and the complete fitting lemma. For every center
\(a\), (18), the triangle inequality and conditional Chebyshev give
\[
 \begin{aligned}
 &\Pr_Z\{|f_n(\infty,\sqrt d\,v)-a|\le c_*/(2\sqrt n)
            \mid\mathcal A_n\}\\
 &\qquad\le\frac14+
   \Pr_Z\{|R_n-\mathbb E_ZR_n|>c_*/(2\sqrt n)\mid\mathcal A_n\}\\
 &\qquad\le\frac14+
   2^{23}4^L D^2(Y/\lambda)^4.                                  \tag{19}
 \end{aligned}
\]
The center in (18) is shifted by \(\mathbb E_ZR_n\), which is
permitted because (18) is uniform over all centers. The numerical factor
in (19) is \(4\cdot2\cdot1024^2=2^{23}\), using
\(e_n^2\le2e_0^2\).

The original label cap and (17) imply
\[
 D(Y/\lambda)^2\le\beta^{-10L}
                 \le2^{-L-14}.                                 \tag{20}
\]
For the second inequality it suffices that
\(\beta^{10L}\ge2^{L+14}\); since \(\beta\ge10\), this already
holds at \(L=1\), as \(10^{10}>2^{15}\), and its left side grows
by a larger factor for each further layer. Thus the added term in (19)
is at most \(2^{23}4^L2^{-2L-28}=1/32\).

For an independent actual trained run \(\widetilde f_n\), condition
additionally on its entire value. That value is independent of the first
run's unused query column, so (19) applies with
\(a=\widetilde f_n(\infty,\sqrt d\,v)\). Average the bound and charge
the complement of the active event by one. This yields
\[
 \Pr\left\{
 |f_n(\infty,\sqrt d\,v)-\widetilde f_n(\infty,\sqrt d\,v)|
       \le\frac{2^{-L}e_0}{2048\sqrt n}\right\}
 \le\frac18+\frac14+\frac1{32}+o(1)=\frac{13}{32}+o(1).          \tag{21}
\]
The complete fitting lemma makes failure of either fitted endpoint an
additional \(o(1)\) event. Consequently, if (17) is proved, then for
every sufficiently large individual width,
\[
 \Pr\left\{
 |f_n(\infty,\sqrt d\,v)-\widetilde f_n(\infty,\sqrt d\,v)|
       \ge\frac{2^{-L}e_0}{2048\sqrt n},\quad
       \text{both runs fit}\right\}\ge\frac12.                  \tag{22}
\]
The proof even leaves a limiting success margin of \(19/32\) before
the vanishing exceptional events.

The unconditional frozen result (16) is proved in this note. The precise
unresolved step for the actual endpoint is (17): a centered scalar
comparison that controls the nonlinear effect of nonzero hidden feature
means. Neither oddness nor a centered whole-feature perturbation estimate
has been assumed for GELU or SiLU. The lower bound on innovation needs no
additional gap factor, diagonal assumption, bounded activation values,
label-sign condition, or label restriction beyond the existing cap.
