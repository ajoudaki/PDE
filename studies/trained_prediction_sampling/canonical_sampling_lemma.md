# Sampling a Hilbert-valued functional of a probability law

**Draft awaiting checks.** The theorem below is a sufficient sampling theorem. Verifying its hypotheses for any particular trained dynamical system is a separate mathematical task.

## Statement

Let \(\mathcal Z\) be a compact metric space, let \(H\) be a separable real Hilbert space, and let \(\mu\in\mathcal P(\mathcal Z)\). Equip the probability laws with \(W_1\). Let \(U\) be a \(W_1\)-open neighborhood of \(\mu\), and let \(F:U\to H\) be bounded and \(W_1\)-continuous. Use the total-variation norm convention \(\|\delta_z-\delta_{z'}\|_{\rm TV}\le2\).

Assume the following three properties.

1. **Actual first mixture response.** There is a jointly Borel kernel \(I:U\times\mathcal Z\to H\), with \(\int I_Q\,dQ=0\), such that on every affine probability segment \(Q_t=Q+t\eta\) contained in \(U\), \(t\mapsto F(Q_t)\) is continuously differentiable, including one-sided endpoint derivatives, and

   \[
   \frac d{dt}F(Q_t)=\int I_{Q_t}(z)\,\eta(dz).
   \tag{R1}
   \]

   Here \(\eta\) is a zero-mass finite signed measure, and the stated Bochner integrals exist. In particular,

   \[
   I_Q(z)=\left.\frac d{d\epsilon}
   F((1-\epsilon)Q+\epsilon\delta_z)\right|_{\epsilon=0+}.
   \tag{R2}
   \]

2. **Uniform mixed second differences.** There is \(M<\infty\) such that, whenever the affine rectangle \(Q+s\eta+t\xi\), \(0\le s,t\le1\), consists of probability laws in \(U\),

   \[
   \|F(Q+\eta+\xi)-F(Q+\eta)-F(Q+\xi)+F(Q)\|_H
   \le M\|\eta\|_{\rm TV}\|\xi\|_{\rm TV}.
   \tag{R3}
   \]

3. **Continuity at the sampling law.** As \(Q\to\mu\) in \(W_1\), with \(Q\in U\),

   \[
   \|I_Q-I_\mu\|_{L^2(\mu;H)}\longrightarrow0.
   \tag{R4}
   \]

The norm in (R4) uses the fixed law \(\mu\). Joint continuity of \((Q,z)\mapsto I_Q(z)\) near \(\{\mu\}\times\mathcal Z\) is a sufficient condition. The uniform local bounds needed for its integrability follow in the proof. A bounded second derivative in total variation implies (R3), but no second derivative of \(F\) is assumed here.

Let \(Z_1,Z_2,\ldots\) be iid with law \(\mu\), and put \(\mu_m=m^{-1}\sum_{i=1}^m\delta_{Z_i}\). There exist a \(W_1\)-open neighborhood \(V\) of \(\mu\), with \(V\subset U\), and a bounded Borel function \(\widetilde F:\mathcal P(\mathcal Z)\to H\), equal to \(F\) on \(V\), such that

\[
 \widetilde F(\mu_m)-F(\mu)
       =\frac1m\sum_{i=1}^m I_\mu(Z_i)+r_m,
 \qquad m\mathbb E\|r_m\|_H^2\longrightarrow0.
 \tag{R5}
\]

Moreover, \(\mathbb P(\mu_m\notin V)\le c_1e^{-c_2m}\) for constants \(c_1,c_2>0\). Consequently any globally defined finite-valued Borel extension \(\widehat F\) of \(F\) has the same expansion with \(\sqrt m\,r_m\to0\) in probability. The \(L^2\) assertion also holds for \(\widehat F\) if it is bounded, or more generally if

\[
 m\mathbb E\|\widehat F(\mu_m)-\widetilde F(\mu_m)\|_H^2
       \longrightarrow0.
 \tag{R6}
\]

In particular, the assertion for an actual endpoint statistic presupposes that this statistic is defined on all sample outcomes, or that an extension has explicitly been chosen.

The covariance operator of the limiting Gaussian is

\[
 C_\mu h=\int\langle I_\mu(z),h\rangle_H I_\mu(z)\,\mu(dz),
 \qquad \operatorname{tr}C_\mu=\int\|I_\mu(z)\|_H^2\,\mu(dz),
 \tag{R7}
\]

and

\[
 \sqrt m\,[\widetilde F(\mu_m)-F(\mu)]
      \Rightarrow\mathcal N_H(0,C_\mu),\qquad
 m\mathbb E\|\widetilde F(\mu_m)-F(\mu)\|_H^2
      \longrightarrow\operatorname{tr}C_\mu.
 \tag{R8}
\]

The distributional conclusion transfers to every extension above; the second-moment conclusion transfers under (R6).

## Proof: line estimates and localization

If \(\mathcal Z\) has one point, every empirical law equals \(\mu\), and centering gives \(I_\mu=0\). All conclusions then hold directly. Assume its diameter \(D\) is positive.

First, (R3) gives the required Taylor estimate using only the first derivative. On a segment \(Q_t=Q+t\eta\), write \(f(t)=F(Q_t)\). For \(0\le a<b<1\), apply (R3) to the rectangle with base \(Q_a\) and increments \((b-a)\eta\) and \(h\eta\). Divide by \(h>0\) and let \(h\downarrow0\). Equation (R1) gives

\[
 \|f'(b)-f'(a)\|_H\le M(b-a)\|\eta\|_{\rm TV}^2.
\]

One-sided continuity covers the endpoints. Integrating the inequality proves

\[
 \left\|F(Q+\eta)-F(Q)-\int I_Q\,d\eta\right\|_H
       \le\frac M2\|\eta\|_{\rm TV}^2.
 \tag{R9}
\]

Choose \(\rho>0\) such that \(B_{W_1}(\mu,\rho)\subset U\). Write \(B=\sup_U\|F\|_H\) and let \(\tau=\min\{1/2,\rho/(8D)\}\). If \(W_1(Q,\mu)<3\rho/4\), the contaminations \((1-s)Q+s\delta_z\), \(0\le s\le\tau\), stay in \(U\), since their distance from \(Q\) is at most \(sD\). By (R2) and (R9),

\[
 \|I_Q(z)\|_H\le 2B/\tau+2M\tau=:L
 \quad\text{for all such }Q\text{ and all }z.
 \tag{R10}
\]

This also proves the local square integrability used in (R4).

To construct a cutoff, choose a finite \(\epsilon\)-net \(z_1,\ldots,z_N\) in \(\mathcal Z\), with \(\epsilon=\rho/16\), and define

\[
 a_j(z)=(2\epsilon-d(z,z_j))_+,\qquad
 \psi_j(z)=\frac{a_j(z)}{\sum_k a_k(z)}.
\]

The denominator is at least \(\epsilon\). Thus the \(\psi_j\) are continuous, take values in \([0,1]\), and sum to one. Sending \(z\) to \(z_j\) with probabilities \(\psi_j(z)\) couples any law \(Q\) with \(Q^d=\sum_j(Q\psi_j)\delta_{z_j}\) at cost at most \(2\epsilon\). Coupling common discrete mass identically and the remainder at cost at most \(D\) gives

\[
 W_1(Q,\mu)\le4\epsilon+
              \frac D2\sum_j|Q\psi_j-\mu\psi_j|.
 \tag{R11}
\]

Put \(b=\rho/(2DN)\). Choose a smooth \(\chi_0:\mathbb R\to[0,1]\) equal to one on \([-1/2,1/2]\), positive on \((-1,1)\), and zero off that interval. Define

\[
 \chi(Q)=\prod_j\chi_0\bigl((Q\psi_j-\mu\psi_j)/b\bigr),
 \qquad V=\{Q:\max_j|Q\psi_j-\mu\psi_j|<b/2\}.
 \tag{R12}
\]

The support of \(\chi\) is contained in \(\{Q:W_1(Q,\mu)\le\rho/2\}\) by (R11); \(\chi=1\) on \(V\). Its first and second law derivatives have bounded scalar kernels, since they are finite sums of products of the \(\psi_j\) and derivatives of \(\chi_0\). Let \(a_Q(z)\) denote its first kernel. Define

\[
 \widetilde F(Q)=\chi(Q)F(Q)\quad(Q\in U),\qquad
 \widetilde F(Q)=0\quad(Q\notin U).
\]

Its centered first kernel is obtained by subtracting its \(Q\)-mean from

\[
 A_Q(z)=\chi(Q)I_Q(z)+F(Q)a_Q(z)
 \tag{R13}
\]

on \(U\), and setting it to zero elsewhere. This kernel is uniformly bounded by (R10), boundedness of \(F\), and the cutoff derivative bounds. The product and its first derivatives extend across the cutoff boundary because \(\chi\) and its derivatives vanish there and the other factors are uniformly bounded on a larger open neighborhood. Thus the first mixture calculus remains valid globally. On \(V\), the centered first kernel of \(\widetilde F\) is exactly \(I_Q\), so (R4) is preserved.

For completeness, the mixed finite-difference bound also survives this extension without any second derivative of \(F\). On a rectangle whose corners are indexed by \(00,10,01,11\), the exact product identity is

\[
\begin{aligned}
 \Delta_{12}(\chi F)
  ={}&\chi_{11}\Delta_{12}F
    +(\chi_{11}-\chi_{10})(F_{10}-F_{00})\\
   &+(\chi_{11}-\chi_{01})(F_{01}-F_{00})
    +(\Delta_{12}\chi)F_{00}.
\end{aligned}
 \tag{R14}
\]

On any rectangle in \(B_{W_1}(\mu,3\rho/4)\), (R3), the first derivative bound (R10), the bounded first and second derivatives of \(\chi\), and boundedness of \(F\) bound (R14) by

\[
 M_*\|\eta\|_{\rm TV}\|\xi\|_{\rm TV}
 \tag{R15}
\]

for a constant \(M_*\) independent of the rectangle.

For a general probability rectangle, its parameter domain is compact. The inverse images of \(B_{W_1}(\mu,3\rho/4)\) and of the complement of the support of \(\chi\) are an open cover of that domain. A sufficiently fine rectangular grid has every cell inside one member of this cover: choose parameter balls whose doubled balls lie in a member of the cover, take a finite subcover of the original balls, and use cells of diameter smaller than their minimum radius. In the first kind of cell (R15) applies; in the second the extended function is zero. Summing mixed cell differences telescopes to the difference on the whole rectangle. The products of cell side lengths sum to one, giving the global bound (R15). Hence \(\widetilde F\) has globally bounded first kernel and second mixed differences.

Finally, a variable in \([0,1]\) has centered log moment-generating function at most \(\lambda^2/8\): its second derivative is a tilted variance, at most \(1/4\), and its value and first derivative vanish at zero. Exponential Markov and independence therefore give

\[
 \mathbb P\bigl(|\mu_m\psi_j-\mu\psi_j|\ge b/2\bigr)
       \le2e^{-mb^2/2}.
\]

The union bound yields

\[
 \mathbb P(\mu_m\notin V)\le2N e^{-mb^2/2}.
 \tag{R16}
\]

## Proof: the global sampling calculation

It remains to prove (R5) for a bounded functional defined on all probability laws, with a uniformly bounded centered first kernel and mixed difference bound \(M_*\). In this part write \(G\) for that functional and \(J_Q\) for its first kernel. We will apply the result to \(G=\widetilde F\), whose kernel satisfies \(J_\mu=I_\mu\).

The finite-test construction (R11), repeated with an arbitrarily small \(\epsilon\), shows that empirical laws converge to \(\mu\) in \(W_1\) in probability. Indeed, each finite set of bounded continuous empirical averages converges by its variance bound; (R11) then makes the remaining deterministic error arbitrarily small. The same conclusion holds for \(m^{-1}\mu+m^{-1}\sum_{i=2}^m\delta_{Z_i}\).

### Bias

Define

\[
 \nu_i=(1-i/m)\mu+m^{-1}\sum_{j=1}^i\delta_{Z_j},
 \qquad 0\le i\le m.
\]

Every segment from \(\nu_{i-1}\) to \(\nu_i\) consists of probability laws. Equation (R9), now with constant \(M_*\), gives

\[
 G(\nu_i)-G(\nu_{i-1})
 =m^{-1}\int J_{\nu_{i-1}}(z)(\delta_{Z_i}-\mu)(dz)+R_i,
 \qquad\|R_i\|_H\le2M_*/m^2.
\]

Conditional on the previous samples, the first term has mean zero. Consequently

\[
 b_m:=\mathbb EG(\mu_m)-G(\mu),\qquad
 \|b_m\|_H\le2M_*/m.
 \tag{R17}
\]

### Higher-order Hoeffding components

For any square-integrable \(H\)-valued statistic \(T=T(Z_1,\ldots,Z_m)\), define

\[
 T_S=\sum_{A\subset S}(-1)^{|S|-|A|}
                 \mathbb E[T\mid Z_i:i\in A],
 \qquad S\subset\{1,\ldots,m\}.
 \tag{R18}
\]

Finite inclusion--exclusion gives \(T=\sum_ST_S\). Each nonempty component has zero conditional mean when any coordinate in its index set is integrated out: terms in (R18) that include that coordinate cancel the terms that omit it. Choosing a coordinate in the symmetric difference of two distinct index sets proves their orthogonality in \(L^2\). Thus

\[
 R^{\rm H}:=T-\mathbb ET-
       \sum_i(\mathbb E[T\mid Z_i]-\mathbb ET)=\sum_{|S|\ge2}T_S
\]

is orthogonal to constants and to all sums of one-coordinate functions.

Let \(T^{(i)}\) replace \(Z_i\) by an independent copy, and let
\(D_{ij}T=T-T^{(i)}-T^{(j)}+T^{(ij)}\). A double replacement kills components not containing both indices. For a component containing both, the four replacement terms have equal second moments and are pairwise orthogonal, by conditioning on a coordinate where they differ. Components with distinct index sets also remain orthogonal after replacement. Hence

\[
 \mathbb E\|D_{ij}T\|_H^2
       =4\sum_{S\supset\{i,j\}}\mathbb E\|T_S\|_H^2,
\]

and summing over pairs gives

\[
 \mathbb E\|R^{\rm H}\|_H^2
       \le\frac14\sum_{i<j}\mathbb E\|D_{ij}T\|_H^2.
 \tag{R19}
\]

Apply this with \(T_m=G(\mu_m)\). Replacing observations \(i\) and \(j\) gives a probability rectangle with edge measures \(m^{-1}(\delta_{Z_i'}-\delta_{Z_i})\) and \(m^{-1}(\delta_{Z_j'}-\delta_{Z_j})\). Therefore

\[
 \|D_{ij}T_m\|_H\le4M_*/m^2,
 \qquad
 \mathbb E\|R_m^{\rm H}\|_H^2\le2M_*^2/m^2.
 \tag{R20}
\]

### The first projection

By symmetry, using the version of conditional expectation obtained by integrating over the other samples, write

\[
 h_m(z)=m\{\mathbb E[T_m\mid Z_1=z]-\mathbb ET_m\},
 \qquad \int h_m\,d\mu=0.
\]

Let \(Q_m=m^{-1}\mu+m^{-1}\sum_{j=2}^m\delta_{Z_j}\). The law \(Q_m+m^{-1}(\delta_z-\mu)\) is a probability measure for every \(z\). Its Taylor expansion around \(Q_m\) has remainder at most \(2M_*/m^2\). Averaging over the other samples, subtracting the \(\mu\)-average over \(z\), and multiplying by \(m\) gives

\[
 h_m(z)=\mathbb E\left[J_{Q_m}(z)-\int J_{Q_m}\,d\mu\right]+e_m(z),
 \qquad \sup_z\|e_m(z)\|_H\le4M_*/m.
 \tag{R21}
\]

The laws \(Q_m\to\mu\) in \(W_1\) in probability. Assumption (R4), preserved near \(\mu\) by localization, and the globally bounded first kernel imply

\[
 \mathbb E\|J_{Q_m}-J_\mu\|_{L^2(\mu;H)}^2\longrightarrow0.
\]

To justify the expectation, the norm tends to zero in probability by continuity and is uniformly bounded; splitting at any fixed threshold proves convergence of its expectation. Jensen's inequality in (R21), together with \(\mu J_\mu=0\), now proves

\[
 \|h_m-J_\mu\|_{L^2(\mu;H)}\longrightarrow0.
 \tag{R22}
\]

### The exact remainder identity

The Hoeffding decomposition gives

\[
 T_m-G(\mu)=b_m+m^{-1}\sum_i h_m(Z_i)+R_m^{\rm H}.
\]

Define \(r_m\) by subtracting \(m^{-1}\sum_iJ_\mu(Z_i)\). The bias, higher-order component, and centered one-coordinate sum are mutually orthogonal in \(L^2\). Independence of the summands gives the exact identity

\[
 m\mathbb E\|r_m\|_H^2
   =m\|b_m\|_H^2+m\mathbb E\|R_m^{\rm H}\|_H^2
                         +\|h_m-J_\mu\|_{L^2(\mu;H)}^2.
 \tag{R23}
\]

The first two terms are at most \(6M_*^2/m\) in total by (R17) and (R20), and the last tends to zero by (R22). This proves (R5). No quantitative modulus in (R4) is needed.

On \(\{\mu_m\in V\}\), any extension \(\widehat F\) in the statement equals \(\widetilde F\). Equation (R16) therefore proves the transfer in probability. If \(\widehat F\) is bounded, multiplying its squared uniform difference from \(\widetilde F\) by \(m\mathbb P(\mu_m\notin V)\) proves (R6). This completes the sampling expansion and its localization claims.

## Covariance, spatial tests, and the Hilbert CLT

Set \(X=I_\mu(Z)\). It is centered and square integrable by (R10). The operator \(C_\mu h=\mathbb E[\langle X,h\rangle X]\) is positive and self-adjoint. For any orthonormal basis \((e_j)\), Tonelli and Parseval give

\[
 \sum_j\langle C_\mu e_j,e_j\rangle
       =\mathbb E\sum_j|\langle X,e_j\rangle|^2
       =\mathbb E\|X\|_H^2<\infty.
\]

Thus \(C_\mu\) is trace class and has the trace in (R7). Its nonnegative eigenvalues \(\lambda_j\), with an orthonormal eigenbasis supplemented in its kernel if needed, define a centered Gaussian \(\mathcal G=\sum_j\sqrt{\lambda_j}\,N_je_j\), where the \(N_j\) are independent standard normals. Summability of \(\lambda_j\) gives convergence in \(L^2(H)\), and its covariance is \(C_\mu\). Degenerate covariance is allowed.

Here is a direct projection proof of the Hilbert CLT. Put \(S_m=m^{-1/2}\sum_iI_\mu(Z_i)\). For any scalar projection \(Y=\langle X,h\rangle\), centering and finite variance give

\[
 \mathbb E e^{itY/\sqrt m}
       =1-\frac{t^2\mathbb EY^2}{2m}+o(m^{-1}).
\]

For the remainder, set \(q(u)=e^{iu}-1-iu+u^2/2\). Then \(q(u)=o(u^2)\) at zero and \(|q(u)|\le C u^2\) for all real \(u\). For fixed \(t\), \(mq(tY/\sqrt m)\to0\) pointwise and its absolute value is at most \(Ct^2Y^2\); dominated convergence proves the displayed expansion. Taking the \(m\)-th power proves the scalar Gaussian characteristic-function limit. Applied to every linear combination of a fixed finite number of coordinates, this proves the finite-dimensional CLT.

For a finite-dimensional orthogonal projection \(\Pi_N\) increasing to the identity, independence and centering give

\[
 \mathbb E\|(1-\Pi_N)S_m\|_H^2
       =\mathbb E\|(1-\Pi_N)X\|_H^2\longrightarrow0
\]

uniformly in \(m\). The Gaussian has the same tail second moment. For any bounded 1-Lipschitz function on \(H\), replacing its argument by \(\Pi_N\) changes either expectation by at most the square root of that tail second moment. Let \(m\to\infty\) at fixed \(N\), using the finite-dimensional conclusion, and then let \(N\to\infty\). This proves weak convergence \(S_m\Rightarrow\mathcal G\) on the separable Hilbert space. Equation (R5) supplies an error tending to zero in \(L^2\) after multiplication by \(\sqrt m\), so proves the first part of (R8). Cauchy--Schwarz, \(\mathbb E\|S_m\|^2=\operatorname{tr}C_\mu\), and (R5) prove its second part.

If \(H=L^2(\mathbb S^1,\lambda)\) for a finite circle measure \(\lambda\), these statements apply to spatial tests. For \(\psi_1,\ldots,\psi_k\in H\), the limiting covariance matrix of the integrals against these tests is

\[
 \Sigma_{ab}=\int_{\mathcal Z}
   \left(\int_{\mathbb S^1}I_\mu(z)(x)\psi_a(x)\,\lambda(dx)\right)
   \left(\int_{\mathbb S^1}I_\mu(z)(x)\psi_b(x)\,\lambda(dx)\right)
      \mu(dz)=\langle C_\mu\psi_a,\psi_b\rangle_H.
 \tag{R24}
\]

A jointly measurable representative of \(I_\mu\in L^2(\mu;H)\) defines the spatial covariance kernel

\[
 c_\mu(x,x')=\int I_\mu(z)(x)I_\mu(z)(x')\,\mu(dz)
 \tag{R25}
\]

as an element of \(L^2(\lambda\otimes\lambda)\): the integrand's norm in that space is \(\|I_\mu(z)\|_H^2\), which is integrable. Its integral operator is \(C_\mu\), by Fubini and Cauchy--Schwarz. Formula (R24) concerns continuous linear spatial tests; point evaluation requires additional regularity beyond \(L^2\).

All statements treat \(F\) and its kernel as deterministic. If they retain a random initialization environment independent of the samples, the theorem applies conditional on that environment when its hypotheses hold there. An unconditional Gaussian limit additionally requires the conditional covariance to be deterministic; otherwise the conditional limits generally form a Gaussian mixture.
