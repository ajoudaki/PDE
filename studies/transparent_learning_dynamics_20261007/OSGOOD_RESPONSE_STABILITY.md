# Osgood response stability from carrier tails

2026-10-07. Independent kinetic-route derivation, written for the supervisor's bounded continuation. Scientific inputs: the supplied abstract tail assumptions and canonical gradient-flow equations already in this study's allowed finite-response notes. No additional source, literature, experiment, or other study was used. In particular, no integrated-source carrier estimate is imported or certified here.

This note proves dimension-independent gate estimates under either exponential or Gaussian-square carrier tails, explicit global scalar comparison bounds, and a conditional finite-depth gradient-flow application. The carrier assumptions, bounded trajectory geometry, residual integrability, and approximation-defect bounds remain separate premises. No sampling or continuum-limit theorem is inferred from them.

## 1. A global family of Osgood moduli

For an error scale \(K>0\) and \(\alpha\in\{1/2,1\}\), define

\[
\omega_{K,\alpha}(x)=
\begin{cases}
0,&x=0,\\
x[\log(\mathrm e K/x)]^\alpha,&0<x\le K,\\
x,&x\ge K.
\end{cases} \tag{1}
\]

The two positive branches agree at \(K\). This function is continuous and increasing, dominates \(x\), and has \(\omega_{K,\alpha}(x)/x\) nonincreasing. Consequently it is subadditive: for \(x,y>0\), its value at \(x+y\) is at most
\(x\omega(x)/x+y\omega(y)/y\). Also,

\[
\omega_{K,\alpha}(c x)\le c\,\omega_{K,\alpha}(x)
\quad(c\ge1),\qquad
\omega_{K,\alpha}(x)\le\omega_{K',\alpha}(x)
\quad(K\le K'). \tag{2}
\]

For monotonicity on \((0,K)\), differentiate \(xL^\alpha\) with \(L=\log(\mathrm e K/x)\ge1\): the derivative is \(L^{\alpha-1}(L-\alpha)\ge0\). The ratio property proves (2). The integral

\[
\int_{0+}\frac{dx}{\omega_{K,\alpha}(x)}=\infty \tag{3}
\]

follows by the substitution \(L=\log(\mathrm e K/x)\). Thus both are Osgood moduli. The linear continuation above \(K\) makes every comparison below defined at every nonnegative error; logarithms of numbers below one never occur.

## 2. Gate comparison on an arbitrary probability space

Let \(z,z',k,k'\) be real random variables on one probability space, with the stated differences square-integrable. The reference carrier is \(k\). Let \(a:\mathbb R\to\mathbb R\) satisfy

\[
\|a\|_\infty\le B,\qquad \operatorname{Lip}(a)\le D,
\qquad B,D\ge0.
\]

Write \(\delta_z=\|z-z'\|_2\) and \(\delta_k=\|k-k'\|_2\). The decomposition

\[
a(z)k-a(z')k'
=a(z')(k-k')+k[a(z)-a(z')]
\]

and a cutoff \(R\ge0\) give

\[
\|a(z)k-a(z')k'\|_2
\le B\delta_k+D R\delta_z
+2B\left(\mathbb E[k^2\mathbf1_{\{|k|>R\}}]\right)^{1/2}. \tag{4}
\]

This inequality is deterministic in the underlying joint law. It requires no independence between the fields, and no tail assumption on \(k'\). In particular it applies on the finite probability space of \(n\) neurons with uniform mass, with \(\|\cdot\|_2\) equal to normalized RMS.

### Gaussian-square tail

Suppose, for some \(A>0\),

\[
\mathbb E[k^2\mathbf1_{\{|k|>R\}}]
\le A^2\exp(-R^2/A^2),\qquad R\ge0. \tag{5}
\]

If \(B,D>0\), set \(K=2B/D\). Then

\[
\|a(z)k-a(z')k'\|_2
\le B\delta_k+\sqrt3\,A D\,
\omega_{K,1/2}(\delta_z).
\tag{6}
\]

For \(0<\delta_z\le K\), choose
\(R=A\sqrt{2\log(K/\delta_z)}\) in (4). The last two terms become at most

\[
AD\delta_z\bigl[1+\sqrt{2\log(K/\delta_z)}\bigr]
\le\sqrt3\,AD\delta_z\sqrt{1+\log(K/\delta_z)}.
\]

The final inequality follows from
\(1+\sqrt{2u}\le\sqrt{3(1+u)}\) for \(u\ge0\), whose squared difference is \((\sqrt u-\sqrt2)^2\). For \(\delta_z\ge K\), (5) at \(R=0\) gives \(\|k\|_2\le A\), so the gate-change term is at most \(2BA=ADK\le AD\delta_z\). At \(\delta_z=0\) it is zero. These cases prove (6) globally.

A square-exponential moment assumption supplies (5) after a fixed rescaling. If

\[
\mathbb E\exp(k^2/A_0^2)\le M,\qquad M\ge1,
\]

write \(X=k^2/A_0^2\). Since \(x e^{-x/2}\le2/\mathrm e<1\),

\[
\mathbb E[k^2\mathbf1_{\{|k|>R\}}]
\le M A_0^2\exp[-R^2/(2A_0^2)].
\]

Thus (5) holds with \(A=A_0\sqrt{\max(M,2)}\). In particular, a budget at most two permits \(A=\sqrt2 A_0\). The moment bound is used directly; this avoids any assumption about a density or independence of neurons.

### Exponential tail

Suppose instead that

\[
\mathbb E\exp(|k|/A)\le M,
\qquad A>0,\quad M\ge1. \tag{7}
\]

For \(X=|k|/A\), the inequality \(x^2e^{-x/2}\le16/\mathrm e^2\) gives

\[
\begin{aligned}
\mathbb E[k^2\mathbf1_{\{|k|>R\}}]
&\le\frac{16}{\mathrm e^2}M A^2e^{-R/(2A)},\\
\left(\mathbb E[k^2\mathbf1_{\{|k|>R\}}]\right)^{1/2}
&\le2A\sqrt M e^{-R/(4A)}.
\end{aligned} \tag{8}
\]

Also \(\|k\|_2\le A\sqrt M\), since \(x^2\le e^x\) for \(x\ge0\). If \(B,D>0\), set \(K=4B\sqrt M/D\). Then

\[
\|a(z)k-a(z')k'\|_2
\le B\delta_k+4AD\,
\omega_{K,1}(\delta_z).
\tag{9}
\]

For \(0<\delta_z\le K\), choose \(R=4A\log(K/\delta_z)\). Equations (4) and (8) bound the gate-change term by

\[
AD\delta_z[1+4\log(K/\delta_z)]
\le4AD\delta_z[1+\log(K/\delta_z)].
\]

For \(\delta_z\ge K\), use \(2B\|k\|_2\le2BA\sqrt M\le AD\delta_z\). The zero-error case follows directly.

If \(B=0\), the gate output is zero. If \(D=0\), the gate is constant and the right side reduces to \(B\delta_k\); no logarithmic scale needs to be defined. If a carrier scale is zero in the limiting interpretation, the carrier is zero almost surely and the same reduction applies. These conventions avoid divisions by vanishing constants.

The weaker exponential budget therefore changes the response modulus from \(x\sqrt{\log(C/x)}\) to \(x\log(C/x)\). Both remain Osgood. Neither estimate uses a sample maximum growing like \(\sqrt{\log n}\).

## 3. Explicit global scalar comparison with additive defects

Let \(e:[0,\infty)\to[0,\infty)\) be locally absolutely continuous, let \(b,d\ge0\) be locally integrable, and suppose almost everywhere

\[
e'(t)\le b(t)\omega_{K,\alpha}(e(t))+d(t). \tag{10}
\]

For a specified horizon \(T\le\infty\), assume

\[
\mathcal B_T=\int_0^T b(s)ds<\infty,\qquad
\eta\ge e(0)+\int_0^T d(s)ds,
\qquad \eta\ge0. \tag{11}
\]

There is an explicit increasing comparison function \(\Phi_{K,\alpha}(\eta,\beta)\) such that

\[
e(t)\le\Phi_{K,\alpha}\left(\eta,\int_0^t b(s)ds\right),
\qquad 0\le t\le T. \tag{12}
\]

Here \(\Phi(0,\beta)=0\). If \(\eta\ge K\), both moduli have the linear continuation and

\[
\Phi_{K,\alpha}(\eta,\beta)=\eta e^\beta. \tag{13}
\]

For \(0<\eta<K\), put \(q=\log(\mathrm e K/\eta)>1\). The two formulas are

\[
\Phi_{K,1/2}(\eta,\beta)=
\begin{cases}
\mathrm e K\exp[-(\sqrt q-\beta/2)^2],
&0\le\beta\le2(\sqrt q-1),\\
K\exp[\beta-2(\sqrt q-1)],
&\beta\ge2(\sqrt q-1),
\end{cases} \tag{14}
\]

and

\[
\Phi_{K,1}(\eta,\beta)=
\begin{cases}
\mathrm e K\exp[-q e^{-\beta}],
&0\le\beta\le\log q,\\
K\exp[\beta-\log q],
&\beta\ge\log q.
\end{cases} \tag{15}
\]

These branches match when the comparison reaches \(K\). They give a bound at every error size and every finite accumulated coefficient.

To prove (12), integrate (10) and use the additive defect floor \(\eta\):

\[
e(t)\le\eta+\int_0^t b(s)\omega(e(s))ds=:E(t).
\]

For \(\eta>0\), \(E\ge e\) and monotonicity gives \(E'\le b\omega(E)\). Hence

\[
\int_\eta^{E(t)}\frac{dx}{\omega(x)}\le\int_0^t b(s)ds.
\]

The integral is strictly increasing in its upper endpoint and unbounded at infinity, so it can be inverted globally. Below \(K\), setting \(q(t)=\log(\mathrm e K/E(t))\) gives the comparison equations
\(\frac{d}{d\beta}\sqrt q=-1/2\) for \(\alpha=1/2\), and \(\frac{d}{d\beta}q=-q\) for \(\alpha=1\). Above \(K\), \(dE/d\beta=E\). These equations give (13)–(15). If \(\eta=0\), apply the result with every positive floor and let it decrease to zero; the formulas tend to zero at each finite \(\beta\), proving uniqueness at zero defect as well.

### Small-defect forms

In the Gaussian-square case, if

\[
\eta\le\mathrm e K\exp[-(1+\mathcal B_T/2)^2],
\]

the comparison stays below \(K\) throughout the horizon, and

\[
\sup_{t\le T}e(t)
\le\eta\exp\left[
\mathcal B_T\sqrt{\log(\mathrm e K/\eta)}
-\frac{\mathcal B_T^2}{4}\right]
\le\eta\exp\left[
\mathcal B_T\sqrt{\log(\mathrm e K/\eta)}\right]. \tag{16}
\]

For fixed \(\mathcal B_T,K\), this is \(\eta^{1-o(1)}\) as \(\eta\downarrow0\). For example, for every \(0<\varepsilon<1\), the final expression is bounded by
\((\mathrm e K)^\varepsilon\exp[\mathcal B_T^2/(4\varepsilon)]\eta^{1-\varepsilon}\), by completing the square.

In the exponential case, if

\[
\eta\le\mathrm e K\exp[-e^{\mathcal B_T}],
\]

the comparison stays below \(K\), and

\[
\sup_{t\le T}e(t)
\le\mathrm e K\left(\frac{\eta}{\mathrm e K}\right)^{e^{-\mathcal B_T}}.
\tag{17}
\]

Thus a coefficient bound \(b(t)\le C\) on a fixed horizon produces the exponent \(e^{-CT}\). The constant \(C\) here includes gate, geometry, and clock factors; it is not claimed universal. If \(\mathcal B_\infty<\infty\) and the defect is integrable, the same formulas hold uniformly over all physical time.

### A version for sampled-time errors

Suppose instead that a nonnegative continuous error satisfies an integral estimate

\[
e(t)\le e(0)+\int_0^t b(s)
\omega_{K,\alpha}(e(\pi_h(s))+\varepsilon_h)ds
+\int_0^t d(s)ds, \tag{18}
\]

where \(0\le\pi_h(s)\le s\), for example the left endpoint of a mesh interval, and \(\varepsilon_h\ge0\). Let \(e^*(t)=\sup_{u\le t}e(u)\). The right side with \(e(\pi_h(s))\) replaced by \(e^*(s)\) is nondecreasing in \(t\). Taking the supremum and adding \(\varepsilon_h\) therefore gives the same comparison with initial floor \(\eta+\varepsilon_h\). In particular,

\[
e^*(t)\le\Phi_{K,\alpha}
\left(\eta+\varepsilon_h,\int_0^t b(s)ds\right). \tag{19}
\]

For exponential tails, fixed \(\mathcal B_T\), and \(\eta+\varepsilon_h\le C h\), this is \(O(h^{e^{-\mathcal B_T}})\). Equation (19) is an abstract comparison lemma. Establishing (18), the within-step error \(\varepsilon_h\), and a common realization for a particular Euler scheme remains a separate task.

## 4. Conditional application to the canonical finite-depth flow

Here the norm and gradient scaling are important. At width \(n\), let

\[
z_{1,a}=Av_a,\quad h_{\ell,a}=\phi_\ell(z_{\ell,a}),\quad
z_{\ell,a}=W_\ell h_{\ell-1,a}\ (\ell\ge2),\quad
f_a=\frac1n w^\top h_{L,a},\quad c_a=y_a-f_a,
\]

with \(|v_a|=1\) and training indices \(a\le m\). Set

\[
b_{L,a}=w,\qquad
\delta_{\ell,a}=\phi'_\ell(z_{\ell,a})\odot b_{\ell,a},\qquad
b_{\ell-1,a}=W_\ell^\top\delta_{\ell,a}.
\]

Use the mobility Hilbert norm on parameter increments

\[
\|\Delta\theta\|_n^2
=\frac1n\|\Delta A\|_F^2
+\sum_{\ell=2}^L\|\Delta W_\ell\|_F^2
+\frac1n|\Delta w|^2,
\qquad \theta=(A,W_2,\ldots,W_L,w). \tag{20}
\]

The hidden-matrix increment norm in (20) is unnormalized Frobenius norm. This is deliberate: a rank-one update \(\delta h^\top/n\) has Frobenius norm equal to the product of the two normalized vector norms. Replacing it by a further factor \(n^{-1/2}\) would not control its action on a normalized feature vector uniformly in width. The absolute initialized-matrix norm need not be bounded in (20); only increments are compared.

With the inner product associated with (20), the output gradient is explicitly

\[
\nabla_n f_a=
\left(
\delta_{1,a}v_a^\top,\;
\left\{\frac1n\delta_{\ell,a}h_{\ell-1,a}^\top\right\}_{\ell=2}^L,\;
h_{L,a}
\right). \tag{21}
\]

For \(\kappa=2/m\), the canonical physical flow is

\[
\dot\theta=\kappa\sum_{a=1}^m c_a\nabla_n f_a. \tag{22}
\]

This reproduces the first-layer, hidden-layer, and readout mobilities exactly.

Fix a reference trajectory \(\theta(t)\), a comparison trajectory \(\theta'(t)\), and their connecting segment \(\theta_s(t)=(1-s)\theta(t)+s\theta'(t)\). Assume on the interval under consideration:

1. All hidden operators on these segments have operator norm at most a fixed \(R_W\), and all evaluated feature vectors and readouts on the segments have normalized RMS norm at most a fixed \(H\).
2. Each activation is globally Lipschitz, each derivative gate is bounded and globally Lipschitz, with fixed bounds. A common \(B\ge1\) bounds the activation Lipschitz constants and the derivative-gate supremum norms; the derivative-gate Lipschitz bounds are denoted by \(D_\ell\).
3. The *reference* training carriers \(b_{\ell,a}(t)\), viewed on the uniform neuron probability space, satisfy either (5) uniformly or an exponential budget (7) uniformly. The comparison carriers are not assumed to have those tails.

The activation assumption bounds its Lipschitz constant, not its values; unbounded activation values are permitted. These are explicit conditional hypotheses, with constants independent of width.

On a stopped error ball \(\|\theta'-\theta\|_n\le\rho\), the segment geometry bounds can be obtained from reference geometry alone. If the reference operators are bounded by \(R_0\), its features and readout by \(H_0\), then segment operators are bounded by \(R_0+\rho\) and readouts by \(H_0+\rho\). First-layer activation differences are at most \(B\rho\) in normalized RMS. Inductively the next activation difference is at most \(B[(R_0+\rho)\times\text{previous activation difference}+\rho H_0]\). A fixed finite depth therefore supplies a segment feature bound depending only on \(R_0,H_0,\rho,B,L\). This derivation needs no comparison-carrier tail or comparison-field higher moment.

Under these hypotheses there are constants \(C<\infty\) and \(K>0\), independent of width, such that for every training output and every \(s\in[0,1]\),

\[
\|\nabla_n f_a(\theta_s)-\nabla_n f_a(\theta)\|_n
\le C\omega_{K,\alpha}(\|\theta'-\theta\|_n), \tag{23}
\]

where \(\alpha=1/2\) for (5) and \(\alpha=1\) for (7). Only fixed depth, sample count, geometry bounds, gate bounds, and carrier-budget constants enter \(C,K\).

To verify (23), write \(e=\|\theta'-\theta\|_n\). Forward differences are Lipschitz in \(e\). Indeed,

\[
\|z_{1,a}(\theta_s)-z_{1,a}(\theta)\|_{2,n}\le e,
\]

and, layer by layer,

\[
\|z_{\ell,a}(\theta_s)-z_{\ell,a}(\theta)\|_{2,n}
\le R_W B\|z_{\ell-1,a}(\theta_s)-z_{\ell-1,a}(\theta)\|_{2,n}+He.
\]

Thus every preactivation difference is at most a fixed constant times \(e\). Apply (6) or (9) at each backward gate, with the reference carrier. The carrier difference itself enters linearly, multiplied by the bounded gate. Between gates,

\[
\|b_{\ell-1,a}(\theta_s)-b_{\ell-1,a}(\theta)\|_{2,n}
\le R_W\|\delta_{\ell,a}(\theta_s)-\delta_{\ell,a}(\theta)\|_{2,n}
+e\|\delta_{\ell,a}(\theta)\|_{2,n}.
\]

All carrier RMS norms are bounded by the readout bound and the finite product of operator and gate bounds. Starting from the readout difference at most \(e\), induction gives \(C\omega_{K,\alpha}(e)\) for every backward difference. Choose a common \(K\) at least as large as the finitely many gate scales, and absorb the forward Lipschitz constants using (2). The modulus is not iterated through depth: only the preactivation error enters its nonlinear argument, and that error is already \(O(e)\).

Finally, each hidden-gradient block obeys

\[
\left\|\frac{\delta_s h_s^\top-\delta h^\top}{n}\right\|_F
\le\|\delta_s-\delta\|_{2,n}\|h_s\|_{2,n}
+\|\delta\|_{2,n}\|h_s-h\|_{2,n}.
\]

The first and last blocks in (21) have the corresponding normalized vector estimates. Summing finitely many squared block bounds proves (23).

## 5. Residual-weighted one-sided stability of the flow

Suppose the reference solves (22), while the comparison satisfies

\[
\dot\theta'=\kappa\sum_{a=1}^m c'_a\nabla_n f_a(\theta')+r(t),
\qquad c'_a=y_a-f_a(\theta'), \tag{24}
\]

where the defect \(r\) is measured in (20). The same fixed labels are used. Let \(\Delta\theta=\theta'-\theta\), \(e=\|\Delta\theta\|_n\), and define the segment-average output gradient

\[
\overline g_a=\int_0^1\nabla_n f_a(\theta_s)ds,
\qquad
f_a(\theta')-f_a(\theta)=\langle\Delta\theta,\overline g_a\rangle_n.
\]

The last identity is the fundamental theorem of calculus along the segment. Equation (23) bounds

\[
\|\nabla_n f_a(\theta)-\overline g_a\|_n\le C\omega(e),
\qquad
\|\nabla_n f_a(\theta')-\overline g_a\|_n\le2C\omega(e).
\]

Write \(\Delta f_a=f_a(\theta')-f_a(\theta)\). Since \(c'_a-c_a=-\Delta f_a\), the exact difference identity is

\[
\begin{aligned}
\langle\Delta\theta,
\kappa\sum_a[c'_a\nabla_n f_a(\theta')-c_a\nabla_n f_a(\theta)]\rangle_n
={}&-\kappa\sum_a(\Delta f_a)^2\\
&+\kappa\sum_a c'_a\langle\Delta\theta,\nabla_n f_a(\theta')-\overline g_a\rangle_n\\
&-\kappa\sum_a c_a\langle\Delta\theta,\nabla_n f_a(\theta)-\overline g_a\rangle_n.
\end{aligned} \tag{25}
\]

Discarding the nonpositive first term gives

\[
\frac12\frac d{dt}e^2
\le\kappa C\bigl(\|c\|_1+2\|c'\|_1\bigr)e\omega_{K,\alpha}(e)
+e\|r(t)\|_n.
\]

Hence, almost everywhere where \(e>0\), and also in the upper-derivative sense at zero,

\[
e'(t)\le b(t)\omega_{K,\alpha}(e(t))+d(t),
\quad
b(t)=\kappa C(\|c(t)\|_1+2\|c'(t)\|_1),\quad
d(t)=\|r(t)\|_n. \tag{26}
\]

The cancellation in (25) matters. Bounding the residual difference in absolute value before using the gradient structure would generally add a nonintegrable constant to \(b(t)\), even when both residuals decay. No convexity of the nonlinear network loss is asserted or needed for (25).

Equations (12)–(17) now apply with

\[
\mathcal B_T=\kappa C\int_0^T
\bigl(\|c(t)\|_1+2\|c'(t)\|_1\bigr)dt,
\qquad
\eta=e(0)+\int_0^T\|r(t)\|_n dt. \tag{27}
\]

On a fixed compact horizon, a uniform residual bound makes \(\mathcal B_T\) finite uniformly in width. For an all-time conclusion, uniform integrability of both residual trajectories in (27) is an additional premise. Carrier tails and bounded operators/features alone do not prove it. Likewise, the proof does not establish the reference carrier budget, segment geometry bounds, or an integrable defect for a proposed approximation.

If the bounds were obtained only up to an error stopping radius \(0<\rho\le K\), the comparison closes that stopping argument whenever its right side remains strictly below \(\rho\). Sufficient smallness conditions are \(\eta<\mathrm e K\exp[-(\sqrt{\log(\mathrm e K/\rho)}+\mathcal B_T/2)^2]\) in the Gaussian-square case, and \(\eta<\mathrm e K\exp[-\log(\mathrm e K/\rho)e^{\mathcal B_T}]\) in the exponential case. Continuity then rules out the first hit of the stopping radius.

The output gradients themselves have bounded Hilbert norm under the geometry bounds, by (21) and the bounded RMS backward recursion. Thus the segment identity also gives \(|f_a(\theta')-f_a(\theta)|\le C_f e\), with a width-independent constant. Parameter stability therefore controls the declared panel outputs whenever the geometry assumptions cover that panel.

The same argument applies in a Hilbert realization in which the displayed forward/backward operations, gradient identities, and rank-one norm estimates remain valid with the specified normalizations. A particular realization or limiting equation must first be shown to have those properties; this note does not assume their identification from finite-program laws.

## 6. Result status

The gate estimates, global Osgood comparisons, sampled-time comparison lemma, and conditional gradient-flow stability above have complete derivations in this note. They require no neuron independence and have constants independent of width when the stated tail and geometry budgets are uniform.

An exponential reference-carrier budget is sufficient for the weaker but still Osgood modulus and fixed-horizon power-law continuity. A Gaussian-square budget gives the sharper near-linear small-defect estimate. Neither budget is proved here for neural training. A finite-program width approximation, a continuous-time common realization, an Euler-defect estimate, and an all-time residual/geometry bound remain distinct inputs. No compression, sample approximation, or interchange of width and time limits follows solely from this module.
