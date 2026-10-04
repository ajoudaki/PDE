# Check of explicit all-order Legendre closure fitting

2026-10-04. Scoped reconstruction. **PASS for the stated deterministic
fitting theorem, physical bounds, and beta-envelope cap.** No additional
geometry, bounded activation values, or Gaussian forward normalization is
needed. The new approximate-energy estimate closes the readout bound with
\(R=S\sqrt\lambda\); it does not lose an additional power of the covariance
gap. This check establishes no probabilistic trained-carrier estimate.

The complete principal input was `GENERAL_EXPLICIT_CLOSURE_FITTING.md`,
SHA-256 `2247f0d4b189b8d38f1c996db3438a55d562ca6b0e6c82c8ae71b3110e708cbd`.
The other scientific inputs were the previously checked complete
`GENERAL_EXPLICIT_FITTING.md`, only §§1--2 of
`GENERAL_LEGENDRE_TRANSFER.md`, and the complete projection lemma and
fitting subsection of `paper/proof_alltime.tex` (lines 98--339 when read).
No other report or source was used for this check. The canonical-notation
and rigorous-math skills were applied. This is an internal component check,
not an independent promotion review.

## 1. Equations, history normalization, and defect sign

The first block is \(A\in\mathbb R^{n\times d}\); the other hidden blocks
are reconstructed \(n\times n\) matrices. The output is
\(f=w^\top h^{(L)}/n\), the loss is
\(\rho^2=m^{-1}\sum_a(f_a-y_a)^2\), and the dense comparison field has
mobilities \(n,1,\ldots,1,n\). The closure's clock obeys
\(\dot\tau=\rho\), \(\tau(0)=1\). At zero residual its raw moment
equations are regular and every velocity is zero.

Before a possible zero residual, use the clock coordinate \(\xi\), put
\(c_a=r_a/\rho\) and \(b_a^{(\ell)}=c_a\delta_a^{(\ell)}\), and prepend
constant forward and zero backward histories on \([0,1]\). For a clock
endpoint \(A_c=\tau(t)\), the stored modes are exactly the unnormalized
shifted-Legendre moments of these histories on \([0,A_c]\). Therefore the
reconstruction equals

\[
\widehat W^{(\ell)}-W_0^{(\ell)}
=-\frac2{mn}\sum_a\int_0^{A_c}
(\Pi_q^{A_c}b_a^{(\ell)})(\xi)
(\Pi_q^{A_c}h_a^{(\ell-1)})(\xi)^\top\,d\xi.
\tag{A}
\]

The factors \((2j+1)/A_c\) in the modal expression are precisely the
reciprocal squared norms of the unnormalized modes. Differentiating the
projected bilinear integral gives its unprojected endpoint product minus
the product of the two endpoint projection errors. Consequently

\[
\dot{\widehat\theta}=F(\widehat\theta)+\mathcal E,
\qquad \mathcal E_A=\mathcal E_w=0,
\]
\[
\mathcal E_\ell
=\frac{2\rho}{mn}\sum_a
(b_a^{(\ell)}-b_a^{(\ell),*})
(h_a^{(\ell-1)}-h_a^{(\ell-1),*})^\top.
\tag{B}
\]

Here \(F\) is the genuine dense gradient field at the current reconstructed
state. The positive sign and the factors \(2,\rho,m,n\) agree with the
source. The symbol \(\mathcal E_\ell\) in this report distinguishes the
matrix defect from the scalar source constant \(E\).

## 2. Independent numerical verification of the projection bounds

The weighted derivative eigenvalues of the shifted Legendre modes are
\(k(k+1)\). Orthogonality and integration by parts therefore bound the
omitted modes \(k\ge q\) by

\[
\|(I-\Pi_q^{A_c})u\|_2^2
\le\frac1{q(q+1)}\int_0^{A_c}
\xi(A_c-\xi)\|u'(\xi)\|^2\,d\xi.
\]

The endpoint error multiplier is
\((p_q(\xi/A_c)+p_{q-1}(\xi/A_c))/2\). Its squared norm is

\[
\frac{A_c}{4}\left(\frac1{2q+1}+\frac1{2q-1}\right)
=\frac{A_c q}{4q^2-1}\le\frac{A_c}{3q},
\]

including equality at \(q=1\). This verifies the first numerical endpoint
constant in (8).

To check the bounded-history endpoint constant without accepting an
unspecified manuscript constant, write
\(v(\theta)=\sqrt{\sin\theta}P_k(\cos\theta)\) and
\(Q(\theta)=(k+1/2)^2+(4\sin^2\theta)^{-1}\). The Legendre equation gives
\(v''+Qv=0\), so

\[
\frac d{d\theta}\left(v^2+\frac{(v')^2}{Q}\right)
=-\frac{Q'(v')^2}{Q^2}\ge0\quad(0<\theta<\pi/2).
\]

At \(\pi/2\), the values of the even and odd polynomials, together with
\(\binom{2r}{r}/4^r\le(r+1)^{-1/2}\), bound this energy by \(4/k\).
The binomial inequality itself follows inductively from the ratio
\((2r-1)/(2r)\):
\((2r-1)^2(r+1)\le4r^3\) for \(r\ge1\).
It follows that \(|v|\le2/\sqrt k\) and
\(|v'|\le2\sqrt Q/\sqrt k\). Since
\(\sqrt Q\le k+1/2+(2\sin\theta)^{-1}\), differentiation of
\(P_k(\cos\theta)=v(\theta)/\sqrt{\sin\theta}\) gives

\[
|\partial_\theta P_k(\cos\theta)|
\le3\sqrt k(\sin\theta)^{-1/2}
 +2k^{-1/2}(\sin\theta)^{-3/2}.
\]

On \([1/k,\pi/2]\), \(\sin\theta\ge2\theta/\pi\) bounds the respective
integrals by \(3\pi\sqrt k\) and
\(4(\pi/2)^{3/2}<8\). On \([0,1/k]\),
\(|P_k'|\le k(k+1)/2\) bounds the integral by
\((k+1)/(4k)\le1/2\). This derivative inequality follows by summing
the differentiated Legendre recurrence and using \(|P_j|\le1\) on
\([-1,1]\). For example, the latter follows from the elementary integral
representation whose integrand is
\((\cos\theta+i\sin\theta\cos\alpha)^j\), of modulus at most one.
Parity then gives

\[
\operatorname{Var}(P_k)
\le6\pi\sqrt k+17\le(6\pi+17)\sqrt k<36\sqrt k.
\]

The endpoint projection kernel is
\((p_q'+p_{q-1}')/2\), so its integral absolute value is at most
\(36\sqrt q\). At \(q=1\) the kernel is identically one. Thus the source's
constant \(64\sqrt q\) is valid with a substantial margin. Integrating
this scalar kernel against a Hilbert-valued history proves the same
operator norm without a coordinate factor.

Finally, differentiating the minimum least-squares error as \(A_c\) grows
leaves exactly the squared endpoint error: the interior derivative pairs
the projection residual with a polynomial of degree below \(q\), which
vanishes. This justifies the growing projection-error identity used in
the bootstrap.

## 3. All constants in the stopped bootstrap

Set \(S=8Y/\lambda\), \(R=S\sqrt\lambda\), and work before the stated
stops. Write \(D_\ell=s(9s)^{L-\ell}\) and \(D=D_1\). Backward propagation
gives \(\|\delta_a^{(\ell)}\|_2/\sqrt n\le D_\ell R\). Since
\(m^{-1}\sum_a c_a^2=1\), the backward history in the Hilbert norm
\((m^{-1}n^{-1}\sum_a\|\cdot\|_2^2)^{1/2}\) is bounded by
\(D_\ell R\) at each clock time. No estimate on individual \(c_a\) is
needed.

Projection contraction in (A) gives

\[
\|\widehat W^{(\ell)}-W_0^{(\ell)}\|_F
\le4HD_\ell R\sqrt{(1+S)S}.
\]

The first-block equation gives
\(\|A-A_0\|_F/\sqrt n\le2DRS\). Because
\(S\le1\), \(S\le(64H^2D)^{-1}\), and \(\sqrt\lambda\le H\), these
displacements are at most \(\sqrt2/16\) and \(1/(32H)\), respectively.
They are strictly below one, proving the claimed mixer margins.

For clarity, the sphere energy used in the source can be written as

\[
Z_\ell(t)=\sup_{\|v\|_2=1}\frac1n\int_0^{\tau(t)}
\|\partial_\xi h^{(\ell)}(\xi,v)\|_2^2\,d\xi.
\]

The prefix has zero derivative. Its supremum bounds the training average
energy whenever that average is used in a defect estimate.
Polynomial endpoint evaluation has norm \(q/\sqrt{A_c}\), giving a
backward endpoint error at most \((q+1)D_\ell R\) in sample RMS. By
sample Cauchy--Schwarz, the squared defect divided by \(\rho^2\) is at
most four times this squared bound times the mean squared forward endpoint
error. Integrating in the clock and applying the growing projection-error
identity gives

\[
\int_0^t\rho\|\mathcal E_\ell/\rho\|_F^2\,du
\le\frac{q+1}{q}(1+S)^2D_\ell^2R^2Z_{\ell-1}
\le2(1+S)^2D_\ell^2R^2Z_{\ell-1}.
\tag{C}
\]

The first-layer chain rule gives
\(Z_1\le4Ss^2D_1^2R^2\). For later layers, the three contributions to
the clock derivative are the dense matrix velocity, its defect, and the
preceding feature derivative. Their squared integrated bounds are,
respectively,

\[
64SH^4D_\ell^2R^2,\qquad
32H^2D_\ell^2R^2Z_{\ell-1},\qquad81Z_{\ell-1}.
\]

The factor three and activation factor \(s^2\) give exactly (13).
Moreover \(32H^2D_\ell^2R^2\le1/128<1\), so the recurrence in (1)
indeed gives \(Z_\ell\le C_\ell SR^2\). The \(C_\ell\) increase; hence
\(C=\sqrt{C_L}\) controls all layers. Every sphere feature displacement
is bounded by

\[
\sqrt{SZ_\ell}\le CSR=CS^2\sqrt\lambda\le\sqrt\lambda/8\le H/8.
\]

This strictly improves the sphere feature cap. For the top training
feature matrix divided by \(\sqrt{mn}\), the operator perturbation is at
most the same displacement. The initial gap therefore gives least
singular value at least
\((1/\sqrt2-1/8)\sqrt\lambda>\sqrt\lambda/2\), establishing the
readout Gram gap \(\lambda/4\).

For the pointwise defect, the backward endpoint error is at most
\(65\sqrt qD_\ell R\); the forward error is at most
\(\sqrt{2/(3q)}\sqrt{C_{\ell-1}S}\,R\). Consequently

\[
\|\mathcal E_\ell\|_F
\le130\sqrt{2/3}\,D_\ell\sqrt{C_{\ell-1}}\sqrt S R^2\rho.
\]

Summing verifies (14) with the defined scalar
\(E=130\sum_{\ell=2}^LD_\ell\sqrt{C_{\ell-1}}\).
For the ordinary prediction Jacobian \(J\), the defect acts as
\((J\mathcal E)_a=n^{-1}\sum_{\ell\ge2}
\delta_a^{(\ell)\top}\mathcal E_\ell h_a^{(\ell-1)}\). Thus

\[
\|J\mathcal E\|_m
\le2HDR\sum_{\ell\ge2}\|\mathcal E_\ell\|_F
\le2HDE S^{7/2}\lambda^{3/2}\rho\le\lambda\rho/4.
\]

The final step is precisely the fourth condition in \(S_*\), combined
with \(\sqrt\lambda\le H\). It introduces no further gap dependence.

## 4. Residual decay and the approximate energy argument

The mean tangent Gram is the sum of the readout, first-block, and hidden
parameter-gradient Grams, with entries

\[
\Gamma_{ab}=\frac1m\left[
\frac{h_a^{(L)\top}h_b^{(L)}}n
+\frac{\delta_a^{(1)\top}\delta_b^{(1)}}n v_a^\top v_b
+\sum_{\ell=2}^L
\frac{\delta_a^{(\ell)\top}\delta_b^{(\ell)}}n
\frac{h_a^{(\ell-1)\top}h_b^{(\ell-1)}}n\right].
\]

It is positive semidefinite and dominates its readout block. With
\(\Gamma_w\succeq\lambda I/4\), the exact residual equation
\(\dot r=-2\Gamma r+J\mathcal E\) implies
\(\dot\rho\le-\lambda\rho/4=-\kappa\rho\). This gives both the tail
activity bound and realized total activity at most \(4Y/\lambda=S/2\).

The closure is not a gradient flow in its raw moments. The argument
correctly applies the parameter metric to the dense field \(F\), not
to the full closure velocity. The exact identities are

\[
\|F\|_{\rm par}^2=4\langle r,\Gamma r\rangle_m\ge\lambda\rho^2,
\qquad
-\frac d{dt}\rho^2
=\|F\|_{\rm par}^2-2\langle r,J\mathcal E\rangle_m.
\]

Since the cross term has absolute value at most
\(\lambda\rho^2/2\), these imply
\(-d(\rho^2)/dt\ge\|F\|_{\rm par}^2/2\).
For any stopped interval \([0,T]\), integration by parts yields

\[
\begin{aligned}
\int_0^T e^{\kappa t}\|F\|_{\rm par}^2\,dt
&\le2Y^2-2e^{\kappa T}\rho(T)^2
  +2\kappa\int_0^T e^{\kappa t}\rho(t)^2\,dt\\
&\le4Y^2.
\end{aligned}
\]

Weighted Cauchy--Schwarz then gives
\(\int_0^T\|F\|_{\rm par}\,dt\le2Y/\sqrt\kappa
=4Y/\sqrt\lambda=R/2\). The readout has no defect, so its normalized
norm stays at most \(R/2\). This closes its stopping boundary with the
stated margin, rather than requiring the larger direct bound from the
integral of \(\rho\).

All stopping margins are strict. The raw moment vector field is locally
Lipschitz on \(\tau>0\), including zero residual; all its velocities vanish
at a zero-residual state. Local uniqueness backwards from such an
equilibrium excludes a finite first zero for a nonstationary solution.
The integral moment formulas, bounded physical features and backward
responses, and \(1\le\tau\le1+S\) bound the entire raw state for every
fixed \(n,q\). These bounds exclude a finite maximal existence endpoint.
The finite integrals of \(\|F\|_{\rm par}\) and
\(\sum_\ell\|\mathcal E_\ell\|_F\) imply finite physical parameter path
length. Thus the physical parameters converge, and residual decay proves
interpolation. For \(Y=0\) the initialized state is stationary. Because
the event and every estimate are independent of \(q\), the conclusion
holds for every positive integer order on the same event.

## 5. Comparison-interface constants and the activation envelope

The block-speed constants in (18) follow from the dense speeds
\(2DR\rho\), \(4HD_\ell R\rho\) and the individual defect bound above.
Their forward recursion is the ordinary chain rule. The tangent Gram
trace is at most

\[
G=4H^2+D_1^2R^2+4H^2R^2\sum_{\ell=2}^LD_\ell^2,
\]

so \(\|\dot r\|_m\le(2G+\lambda/4)\rho\). For \(Y>0\), the normalized
residual \(c=r/\rho\) therefore has
\(\|\dot c\|_m\le2\|\dot r\|_m/\rho\le4G+\lambda/2\).
This verifies (18)--(19). The zero-label stationary case requires no
definition of \(c\).

Here is an explicit check of the deliberately loose powers in §5.
Write \(\beta=\beta_\partial\ge10\). The dense note gives
\(H\le(2\beta)^L\le\beta^{3L/2}\), and

\[
D_\ell\le\beta^{2L-2\ell+1},\quad
C_1\le\beta^{4L+1},\quad
246s^2\le\beta^5,\quad
192s^2H^4D_\ell^2\le\beta^{10L-4\ell+7}.
\]

Unrolling the recurrence bounds the initial contribution to \(C_L\)
by \(\beta^{9L-4}\), and each later contribution, indexed by
\(\ell\ge2\), by \(\beta^{15L-9\ell+7}\). For \(L\ge2\), all are
at most \(\beta^{15L-11}\). Since \(L\le\beta^L\),
\(C_L\le\beta^{16L}\), hence \(C\le\beta^{8L}\).
Also \(D\le\beta^{2L}\), and

\[
E\le130L\beta^{10L}\le\beta^{12L}.
\]

For the last inequality use \(130\le\beta^3\) and
\(L\le\beta^{L-1}\), followed by \(L+2\le2L\).
The four candidates defining \(S_*\) are each at least
\(\beta^{-8L}\): their reciprocal powers are bounded using
\(64H^2D\le\beta^{5L+2}\),
\(\sqrt{8C}\le\beta^{4L+1}\), and
\((8H^2DE)^{2/7}\le\beta^{(34L+2)/7}\).
All three exponents are at most \(8L\).
Finally \(8\le\beta^{2L}\) implies
\(\lambda\beta^{-10L}\le(\lambda/8)\beta^{-8L}
\le(\lambda/8)S_*\), proving the stated sufficient label cap.

As a direct additional consequence of the checked speed bounds, the
closure also has the sphere endpoint estimate

\[
\sup_{\|v\|=1}|\widehat f(\infty,v)-\widehat f(t,v)|
\le (8H^2+RV_L)\frac{\rho(t)}\kappa
\le (8H^2+RV_L)\frac Y\kappa e^{-\kappa t}.
\]

This follows from \(\|\dot w\|_2/\sqrt n\le4H\rho\),
\(\|h^{(L)}\|_2/\sqrt n\le2H\), and the feature-speed bound
\(V_L\rho\); using \(R\) rather than the sharper \(R/2\) is conservative.
The deterministic results above still do not supply the probabilistic
trained-carrier estimate or its numerical constants.
