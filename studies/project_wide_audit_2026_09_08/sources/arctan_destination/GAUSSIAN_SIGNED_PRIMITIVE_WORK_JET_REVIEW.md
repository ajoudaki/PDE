# Independent complete proof audit

**Verdict: PASS for the complete stated zero-readout finite-jet theorem. No mathematical correction is required at the hashes below.** In particular, the finite-width coefficient, its exact conditional mean (including the empirical-product bias), its strictly positive expectation for every \(n\ge2\), and its convergence in probability and in \(L^1\) to the displayed positive constant all check out. This verdict does not extend to tiny readout or a width-uniform positive-time sign.

I read `/etc/codex/skills/solve-math-rigorously/SKILL.md` and all four permitted mathematical inputs in full. I used no experiments, external sources, ledgers, other reviews, history, other agent work, or files merely referenced by these inputs. No input was edited. The derivations below independently check the needed dependency premises rather than relying on their status labels.

All mathematical inputs are in `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/`:

| Input | SHA256 |
| --- | --- |
| `GAUSSIAN_SIGNED_PRIMITIVE_WORK_JET.md` | `4f982b4f23204186c484f014a9c064480f93709e1d7001942886b0ad9511c6f3` |
| `ACTUAL_BACKPROP_PRIMITIVE_RESPONSE.md` | `067e1bc7d38c7409dab9639f29f84543abd2d0b7a9b9d543f9a47a6747e54d1e` |
| `ACTUAL_PRIMITIVE_OFFDIAGONAL_PAIR.md` | `f7f1b24a4f53cacdf0f86258eafb9b4ae86473b894d70fc9346af0726697df04` |
| `ACTUAL_LOG_GATE_COVARIANCE_COMMUTATOR.md` | `5770d934df3840184d0b19bc3a15eae82290cc879201fe862786ba56d24c6c76` |

All four input hashes were unchanged when checked again after the audit and report creation.

## 1. Setup and independently checked dependency premises

Here \(\phi=\arctan\), \(D_l=\operatorname{diag}\phi'(z_l)\), \(h_l=\phi(z_l)\), and \(w=W^{(4)}\). The initialization under audit is \(w(0)=0\), independent standard Gaussian coordinates of \(z_1(0)\), and independent entries \(N(0,1/n)\) in \(W_2(0),W_3(0)\), independent of that first layer. All traces, transposes, and Frobenius norms are ordinary; \(u\otimes v=uv^T/n\). Put \(d_3=D_3w\), \(q=W_3^Td_3\), \(\delta=D_2q\). The feature equations underlying the dependencies give
\[
w'=h_3,\qquad W_3'=d_3\otimes h_2,\qquad
W_2'=\delta\otimes h_1,\qquad z_1'=D_1W_2^T\delta.
\]
Consequently, directly differentiating \(z_2=W_2h_1\),
\[
z_2'=(m_1I+K)\delta,\qquad
m_1=\|h_1\|^2/n,\quad K=W_2D_1^2W_2^T.                 \tag{R1}
\]
This checks the actual mobility, including first-layer training.

For any one permitted probe let \(p=\operatorname{variation}\delta\), \(a=\int_0^s p\), \(\zeta=\operatorname{variation}z_2\), and \(u=\operatorname{variation}q\), and put \(\beta=\phi''/\phi'\). Differentiating \(\delta=D_2q\), then \(c=D_2^{-1}a\), gives exactly
\[
p=D_2u+\phi''(z_2)\odot q\odot\zeta,\qquad
c'=u+\beta(z_2)\odot(q\odot\zeta-z_2'\odot c).       \tag{R2}
\]
Every inverse is finite because \(\phi'(x)=(1+x^2)^{-1}>0\). Thus the candidate's work (1) is precisely the signed contribution to the derivative of \((2n)^{-1}\sum_i\mathbb E_\xi\|c_i\|^2\), with the separate source contribution \(n^{-1}\sum_i\mathbb E_\xi c_i^Tu_i\). No extra normalization factor is missing.

The primitive representation in the first dependency can also be checked without a referenced file. With its tangent variables \(x=D_1^{-1}\operatorname{variation}z_1\), \(A=\operatorname{variation}W_2\), learned top variation \(B\), and readout variation, the lower equations are
\[
x'=A^T\delta+W_2^Tp,\qquad
A'=p\otimes h_1+\delta\otimes D_1^2x.
\]
The curvature term in the derivative of \(D_1^{-1}\) cancels the corresponding term in \(\operatorname{variation}z_1'\). The upper equations are the full chain rules for \(W_3'\) and \(w'\), giving exactly that dependency's \(L_0,R,f_{\rm top}\). In particular, the lower components of \(L_0\) are autonomous, \(f_{\rm top}\) is purely upper, and \(T R=m_1I+K\). Variation of constants and
\(\partial_s(U_0(t,s)R_s)=U_0(t,s)(R_s'-L_{0,s}R_s)\)
therefore give
\[
\zeta(t)=(m_1I+K)_t a(t)+\int_0^tN_0(t,s)a(s)\,ds.  \tag{R3}
\]
There is no omitted direct lower forcing. Its equal-time kernel is also consistent: applying \(T\) to the lower part of \(L_0R-R'\) gives \(\delta\otimes k-\langle\delta,k\rangle_n I\), \(k=W_2D_1^2h_1\).

For the source estimates, a probe matrix \(\Delta=\xi e_i^T/\sqrt n\) satisfies
\[
\|\xi\mapsto\Delta h_2\|_{2\to n}=|h_{2,i}|/n,
\qquad n\mathbb E\|\Delta^Td_3\|_n^2=\|d_3\|_n^2.
\]
On the explicitly stipulated bounded primal/operator/readout events, these identities give the asserted \(C_S/n\) operator scale for \(f_{\rm top}\), and the asserted second-moment scale for the full \(q_K\). Bounded propagation, (R3)'s state representation, and time Cauchy–Schwarz then give the first dependency's source estimate (14). The contact term \(\Delta^Td_3\) needs only this second-moment bound; it is not incorrectly assigned operator scale \(1/n\). For the candidate's local jet, finite-dimensional local boundedness suffices: no probability estimate for those events, positive-time coercivity, clipping theorem, or uniform source estimate is needed.

Substitution of (R1), (R3) into (R2) cancels the two \(m_1\) terms exactly. Using \(\beta_j=-2z_{2,j}D_{2,j}\), symmetry of \(K\), and symmetry of \(\Sigma=n\mathbb E cc^T\) gives the off-diagonal dependency's polarized sum (4)–(5); each diagonal term is zero. Memory remains in (R3). This verifies the signed-work premise without assigning a sign from positive semidefiniteness.

The log-gate dependency supplies no further probabilistic premise. Its relevant probe jet is rederived below. Its algebra is consistent: writing its mobility as \(C_0=(m_1I+K)/m_1\), \(L=\operatorname{diag}\log\phi'(z_2)\), \(B=LC_0\), \(B_0=L'C_0\), \(\Gamma=n\mathbb E_\xi aa^T\), and \(\eta=(I-B)a\), one has \(J_g=LC_0L'-L'C_0L\) skew, \(Q=[B,B_0]=J_gC_0\), and
\[
\operatorname{Tr}(J_gC_0\Gamma)=\tfrac12\operatorname{Tr}(J_g[C_0,\Gamma]),
\qquad Q^TC_0=-C_0Q.
\]
Also \(G=C_0(I-LC_0)^{-1}\) is symmetric positive by its displayed congruence representation; it gives \(\eta^TG\eta=a^TC_0(I-LC_0)a\) and \(\eta^TGQa=0\). Differentiating this energy gives the dependency's (6), with all \(C_0'\) and source terms retained. None of these identities makes the actual probe covariance isotropic or proves a sign for the present work. The candidate does not import the merely referenced second-integration-by-parts or coercivity results.

## 2. Full finite-width jet and column averaging

All fields in this section are initial fields. At zero readout, \(d_3=\delta=0\); all hidden velocities vanish, whereas \(w'=h_3\). With \(\psi=\phi\phi'\), set
\[
v=W_3^T\psi(z_3),\qquad D=D_2,\qquad A_2=m_1I+K.
\]
The chain rules give \(q'=v\), \(\delta'=Dv\), and \(z_2''=A_2Dv\). Under the initial column probe, the lower initial state does not vary and \(\operatorname{variation}z_3=h_{2,i}\xi/\sqrt n\). Hence
\[
\operatorname{variation}q'(0)
=\frac1{\sqrt n}\left(e_i\psi(z_3)^T+
h_{2,i}W_3^T\operatorname{diag}\psi'(z_3)\right)\xi
=R_i\xi/\sqrt n.                                    \tag{R4}
\]
Both factors in \(D_3h_3\) are differentiated: \(\psi'=\phi'^2+\phi\phi''\). In particular the readout response is included. Top training has zero initial velocity and zero probe variation of that velocity; its effects cannot add another term at this order.

Since \(a'=p\), \(a(0)=p(0)=0\), differentiating once more gives
\[
c_i(s)=\frac{s^2}{2\sqrt n}R_i\xi+O_n(s^3)\|\xi\|,
\qquad
\zeta_i(s)=\frac{s^2}{2\sqrt n}A_2DR_i\xi+O_n(s^3)\|\xi\|. \tag{R5}
\]
The \(m_1D R_i\) part comes from \(W_2\) training and the \(KDR_i\) part from first-layer training. Alternatively (R3), with \(a=O_n(s^2)\), places its retained memory at order at least \(s^3\). The log-gate dependency's \(\Gamma=(s^4/4)DR_iR_i^TD+o_n(s^4)\) follows as well.

Finite-dimensional smooth ODE dependence gives these operator-valued Taylor expansions at every fixed finite initial state. Linearity in \(\xi\) bounds the resulting work remainder by a finite-state constant times \(s^6\|\xi\|^2\). Thus probe averaging of the remainders, not just of the formal coefficients, is legitimate at fixed width.

Using \(q(s)=sv+O_n(s^2)\), \(z_2'(s)=sA_2Dv+O_n(s^2)\), and (R5) in the work gives
\[
\mathscr W_n(s)=s^5J_n+O_n(s^6),\qquad
J_n=\frac1{4n^2}\operatorname{Tr}[\mathcal M(v)C],
\]
\[
\mathcal M(v)=\operatorname{diag}(\beta\odot v)KD
-\operatorname{diag}(\beta\odot KDv),\qquad
C=\sum_iR_iR_i^T.                                    \tag{R6}
\]
The factors are \(1/n\) for column averaging and \(1/(4n)\) from the two probe responses. The two instantaneous \(m_1\) terms cancel. For \(n=1\), \(\mathcal M(v)=0\), proving exactly the asserted \(J_1=0\), not vanishing of all later work.

Writing \(h=h_2\), \(m=\|h\|^2/n\), \(d=\psi(z_3)\), \(E=\operatorname{diag}\psi'(z_3)\), and \(\ell=W_3^TEd\), multiplication gives
\[
C=\|d\|^2I+h\ell^T+\ell h^T+nmW_3^TE^2W_3.          \tag{R7}
\]
Thus the contact, both cross, and distributed terms are all present.

## 3. Exact first-stage conditioning and product bias

Conditional on the entire lower initialization and \(z=z_3\), Gaussian projection of each row gives
\[
W_3=zh^T/(nm)+XP/\sqrt n,\qquad
P=I-hh^T/(nm),                                        \tag{R8}
\]
where \(X\) is standard Gaussian. Conditional on the lower initialization alone, the \(z_j\) are independent \(N(0,m)\). The event \(m=0\) has probability zero. This construction uses independent residual rows with a projected covariance, not independent entries of the conditioned \(W_3\).

With the candidate's barred averages, write
\[
v=\bar\gamma h+\varepsilon,\quad
\varepsilon=PX^Td/\sqrt n,\quad
\ell=\frac{z^TEd}{nm}h+PX^TEd/\sqrt n.
\]
The quadratic term in (R7) has conditional mean
\(nm\bar\tau I+(z^TE^2z/(nm)-\bar\tau)hh^T\)
and linear residual part \(hu^T+uh^T\), \(u=PX^TE^2z/\sqrt n\). Consequently
\[
\mathbb E_X C=n\bar A I+\bar\kappa hh^T,
\qquad
\bar\kappa=\frac{2z^TEd+z^TE^2z}{nm}-\bar\tau.
\]
The covariances of \(\varepsilon\) with \(PX^TEd/\sqrt n\) and \(u\) are respectively \(P(d^TEd/n)\) and \(P(d^TE^2z/n)\). The remaining centered linear times quadratic product is odd Gaussian. Therefore
\[
\mathbb E_X[\varepsilon_jC_{kl}]
=\bar\lambda(h_kP_{jl}+P_{jk}h_l),                    \tag{R9}
\]
with exactly the candidate's \(\bar\lambda\).

Expanding (R6) leaves the coefficient
\(\beta_jK_{jk}D_k(v_jC_{kj}-v_kC_{jj})\).
Its rank-one mean terms cancel; (R9) leaves
\[
\mathbb E_X[v_jC_{kj}-v_kC_{jj}]
=(\bar\lambda-n\bar A\bar\gamma)(h_k-h_j\mathbf1_{j=k}),
\]
because \(h_kP_{jj}-h_jP_{jk}=h_k-h_j\mathbf1_{j=k}\). Thus
\[
\mathbb E_XJ_n=\frac{\bar\lambda-n\bar A\bar\gamma}{4n^2}S_n,
\quad S_n=\sum_{j\ne k}\beta_jK_{jk}\psi(z_{2,k}).     \tag{R10}
\]

For \(Z\sim N(0,m)\), direct expansion of the empirical product gives
\[
n\mathbb E[\bar A\bar\gamma\mid\mathrm{lower}]
=(n-1)A(m)\gamma(m)+\frac1m\mathbb E[Z\psi(Z)^3]
+\mathbb E[Z\psi'(Z)^2\psi(Z)].
\]
Meanwhile \(\mathbb E\bar\lambda=\chi(m)+\mathbb E[Z\psi'(Z)^2\psi(Z)]\). Gaussian integration by parts for the bounded smooth function \(\psi^3\), whose derivative is bounded and whose Gaussian boundary terms vanish, gives
\[
\frac1m\mathbb E[Z\psi(Z)^3]=3\mathbb E[\psi'(Z)\psi(Z)^2]=3\chi(m).
\]
Subtracting yields exactly
\[
\mathbb E[\bar\lambda-n\bar A\bar\gamma\mid\mathrm{lower}]
=-(n-1)A(m)\gamma(m)-2\chi(m).                       \tag{R11}
\]
In particular the correction is \(-2\chi\); replacing the empirical product by the product of its means would be incorrect.

## 4. Second-stage conditioning and strict finite-width sign

Conditional on \(z_1,z_2\), row projection gives
\(W_2=z_2h_1^T/(nm_1)+YP_1/\sqrt n\), with \(P_1=I-h_1h_1^T/(nm_1)\). Distinct residual rows are independent and centered. Thus, for \(j\ne k\),
\[
\mathbb E[K_{jk}\mid z_1,z_2]
=\frac{z_{2,j}z_{2,k}}{n^2m_1^2}\sum_r h_{1,r}^2D_{1,r}^2
=\frac{b_{1,n}}{nm_1^2}z_{2,j}z_{2,k}.               \tag{R12}
\]
There is no diagonal residual contribution to \(S_n\), since its diagonal is identically zero. Since \(m\) is measurable in \(z_2\), (R10)–(R12) prove precisely
\[
\mathbb E[J_n\mid z_1,z_2]
=-\frac{[(n-1)A(m)\gamma(m)+2\chi(m)]b_{1,n}}{4n^3m_1^2}
\sum_{j\ne k}[z_{2,j}\beta(z_{2,j})][z_{2,k}\psi(z_{2,k})]. \tag{R13}
\]

Here \(m_1,m,b_{1,n}>0\) almost surely. For every positive variance, \(A>0\), \(\gamma>0\) because \(x\psi(x)>0\) for \(x\ne0\), and \(\chi>0\) by the integration-by-parts identity just proved. Although \(\psi'\) is not pointwise positive, that causes no defect in this argument. Every nonzero \(z_{2,j}\) satisfies \(z_{2,j}\beta(z_{2,j})<0\) and \(z_{2,j}\psi(z_{2,j})>0\). All these coordinates are nonzero almost surely. For \(n\ge2\), every summand in (R13) is negative and the conditional mean is strictly positive. The integrability proved below then implies \(\mathbb EJ_n>0\). No pointwise sign for every pair of initialized matrices has been proved or used.

## 5. Conditional Poincare and the actual random coefficient

The Gaussian Poincare inequality needed is \(\operatorname{Var}F(X)\le\mathbb E\|\nabla F(X)\|_F^2\) for independent standard Gaussian entries and a Gaussian-Sobolev function with square-integrable gradient. The candidate's semigroup argument is valid: invariance and integration by parts yield \(-\partial_t\mathbb E(P_tF)^2=2\mathbb E\|\nabla P_tF\|^2\); \(\nabla P_tF=e^{-t}P_t\nabla F\), Jensen, and integration on \([0,\infty)\) give the constant one. Cutoff approximation applies here because, conditional on the fixed fields, \(J_n\) is polynomial of degree at most three in \(X\); the lower contraction is quadratic in \(Y\). Their conditional coefficients are finite whenever \(m,m_1>0\).

For \(\bar C=C/n\), a Frobenius-unit change in the standard residual \(X\) has \(\delta W_3=\delta XP/\sqrt n\). Holding the conditioned fields fixed gives
\[
\|\delta v\|\le C,\quad
\|\bar C\|_{\rm op}\le C(1+\|W_3\|_{\rm op}^2),\quad
\|\delta\bar C\|_F\le C(1+\|W_3\|_{\rm op})/\sqrt n.  \tag{R14}
\]
For example, differentiating either cross term in (R7)/\(n\) costs \(\|h\|\|\delta\ell\|/n=O(n^{-1/2})\), and differentiating its quadratic term costs \(O(\|W_3\|_{\rm op}/\sqrt n)\). The bounds use only bounded \(\psi,\psi',h_j\).

The two diagonal traces, separately, obey
\[
|\operatorname{Tr}[\mathcal M(q)\bar C]|
\le2\sqrt n\|K\|_{\rm op}\|\bar C\|_{\rm op}\|q\|,
\qquad \|\mathcal M(q)\|_F\le C\|K\|_{\rm op}\|q\|.  \tag{R15}
\]
Indeed \(\|\operatorname{diag}(KD\bar C)\|\le\sqrt n\|K\|_{\rm op}\|\bar C\|_{\rm op}\), and the other trace uses \(\|\operatorname{diag}\bar C\|\le\sqrt n\|\bar C\|_{\rm op}\). The Frobenius bound follows by bounding each row of \(K\) and then \(KDq\). Since \(\|v\|\le C\sqrt n\|W_3\|_{\rm op}\), differentiation of \(J_n=(4n)^{-1}\operatorname{Tr}[\mathcal M(v)\bar C]\) proves
\[
\|\nabla_XJ_n\|_F
\le\frac{C\|K\|_{\rm op}(1+\|W_3\|_{\rm op}^2)}{\sqrt n}. \tag{R16}
\]
This is a bound on the supremum of all unit directional derivatives, so it is the full gradient norm, without a missing factor from the number of matrix entries.

For an original matrix \(W\) with independent \(N(0,1/n)\) entries, two \(1/4\)-nets of the unit sphere each have at most \(9^n\) points. Approximation gives \(\|W\|_{\rm op}\le2\max|u^TWv|\) on the nets. Each bilinear form has variance \(1/n\), hence
\[
\mathbb P(\|W\|_{\rm op}>x)\le2\,9^{2n}e^{-nx^2/8}.
\]
Integrating above a fixed sufficiently large threshold proves uniform moments of every fixed order. Also \(\|K\|_{\rm op}\le\|W_2\|_{\rm op}^2\). Averaging conditional Poincare in (R16), and only then using the original independent \(W_2,W_3\) laws, gives
\[
\mathbb E|J_n-\mathbb E_X[J_n\mid\mathrm{lower},z_3]|^2\le C/n. \tag{R17}
\]
No uniform bound on the conditional mean matrix in (R8) is needed; the integrated conditional distribution is the original Gaussian distribution. This also avoids integrating inverse powers of \(m\).

Conditional on the lower layer, \(z_{3,j}=\sqrt mG_j\) are independent. On any fixed compact positive variance interval, conditional variance bounds give \(\bar A-A(m)\to0\), \(\bar\gamma-\gamma(m)\to0\) in probability, while \(\bar\lambda/n\to0\). The scalar functions have the claimed continuity and compact-interval derivative bounds by differentiation against a standard Gaussian with dominated Gaussian moments. Boundedness of \(\phi\) and conditional averaging first give \(m_1\to\mu_1\), then \(m\to\mu_2>0\); thus restriction to such an interval loses probability tending to zero. Finally
\[
S_n=\beta(z_2)^TK\psi(z_2)-\sum_j\beta(z_{2,j})\psi(z_{2,j})K_{jj},
\qquad |S_n|/n\le C\|K\|_{\rm op}.
\]
Combining these facts with (R10), (R17) proves the candidate's full random-coefficient approximation
\[
J_n=-\tfrac14A(m)\gamma(m)S_n/n+o_{\mathbb P}(1).     \tag{R18}
\]

## 6. Lower concentration, width limit, and uniform integrability

For clarity, the lower conditional gradient can be written explicitly. Put \(W=W_2\), \(T=D_1^2\), \(b=\beta(z_2)\), \(f=\psi(z_2)\), and \(F=\operatorname{diag}(b\odot f)\). In the conditional parametrization \(W=z_2h_1^T/(nm_1)+YP_1/\sqrt n\),
\[
\nabla_Y(S_n/n)
=\frac{b(TW^Tf)^T+f(TW^Tb)^T-2FWT}{n\sqrt n}\,P_1. \tag{R19}
\]
Since \(\|b\|,\|f\|\le C\sqrt n\), \(\|T\|_{\rm op}\le1\), and \(\|F\|_{\rm op}\le C\), the two bilinear pieces each have norm at most \(C\|W\|_{\rm op}/\sqrt n\), and the diagonal piece has norm at most \(C\|W\|_F/(n\sqrt n)\). Conditional Poincare, averaged under the original \(W_2\) law with \(\mathbb E\|W_2\|_F^2=n\), therefore gives
\[
\mathbb E\left|S_n/n-
\frac{b_{1,n}}{n^2m_1^2}\sum_{j\ne k}
[z_{2,j}\beta(z_{2,j})][z_{2,k}\psi(z_{2,k})]\right|^2\le C/n. \tag{R20}
\]
The conditional mean here is (R12), so potential small \(m_1\) denominators have not been estimated by unjustified inverse moments.

The first-layer bounded-variable law of large numbers gives \(m_1\to\mu_1>0\) and \(b_{1,n}\to b_1>0\). Conditional on that layer the \(z_{2,j}\) are independent \(N(0,m_1)\). In fact both functions \(x\beta(x)\) and \(x\psi(x)\) are bounded, so their empirical means concentrate uniformly over the possible \(m_1\). Their Gaussian means are continuous in the variance. Factoring the off-diagonal sum as the product of sums minus the diagonal, whose contribution divided by \(n^2\) is \(O(1/n)\), gives, for \(Z\sim N(0,\mu_1)\),
\[
S_n/n\ \longrightarrow\ \frac{b_1}{\mu_1^2}
\mathbb E[Z\beta(Z)]\mathbb E[Z\psi(Z)]
\quad\text{in probability}.                         \tag{R21}
\]
Equations (R18), (R21) prove the candidate's exact constant
\[
J_*=-\frac{A(\mu_2)\gamma(\mu_2)b_1}{4\mu_1^2}
\mathbb E[Z\beta(Z)]\mathbb E[Z\psi(Z)]>0.
\]
Every denominator is positive. The first final expectation is strictly negative and the second strictly positive under a nondegenerate Gaussian; the other factors were checked positive above.

Lastly (R14)–(R15), applied directly to (R6), yield the pointwise bound
\[
|J_n|\le C\|W_2\|_{\rm op}^2\|W_3\|_{\rm op}
(1+\|W_3\|_{\rm op}^2).                              \tag{R22}
\]
The proved Gaussian operator moments imply a uniform bound on \(\mathbb E|J_n|^p\) for every fixed finite \(p\), in particular uniform integrability in \(L^1\). Convergence in probability to the deterministic \(J_*\) therefore upgrades to \(\mathbb E|J_n-J_*|\to0\). This also justifies all conditional expectations and the strict unconditional expectation sign in section 4. No Taylor-remainder integrability or expectation–time-differentiation exchange is being substituted for this coefficient bound.

## 7. Exact scope of the PASS

The audited conclusions are the complete candidate statements (2)–(5): the actual, fully trained, probe- and column-averaged work has the stated finite-state expansion; \(J_1=0\); \(\mathbb EJ_n>0\) for every \(n\ge2\); and \(J_n\to J_*>0\) in probability and in \(L^1\). In particular \(\mathbb P(J_n>0)\to1\). The proof uses both exact conditional Gaussian laws, including response–coefficient correlations, and never assumes an isotropic probe covariance after matrix reuse.

The expansion is taken first at fixed width and fixed initialization. It supplies no common positive time interval, no interchange of the width limit with a Taylor expansion, and no sign for the positive-time width-limit work. The report makes no such assertion. It also supplies no pointwise sign for all finite-width initializations, no sign of the full energy derivative including the ordinary source, no bound on the response amplitude, and no contradiction to an upper Gronwall estimate or a different integrated-energy cancellation. The zero-readout assumption is essential to the proved jet: transfer to prescribed tiny readout, clipped-flow conclusions, population continuation, and the canonical global theorem remain outside this result. These limitations agree with the current candidate; none is silently filled by a dependency's status or a forbidden reference.
