# Finite physical source, selected metric, and exact empirical queries

2026-10-07. Author construction for insertion into the integrated decoder
proof. This file supplies the deterministic physical-source construction and
its finite Gaussian and selected-metric implementation. The high-probability
source event and dense-center estimate are internal lemmas of the integrated
result; their probabilities are not additional hypotheses of its final
theorem. The finite arithmetic and short-seed algorithms are the separate
internal word-backend lemmas. No earlier check verdict is a mathematical
dependency.

**Assembly status.** Complete author construction, subject to fresh checking
of this frozen version and its stated internal source/backend dependencies.
It is not a promotion claim or a substitute for those independent checks.

## 1. Physical variables and the precise source-event interface

Write \(v_a=x_a/\sqrt d\), so \(\|v_a\|_2=1\), and retain the
dense forward and backward recursions
\[
z_a^{(1)}=Av_a,\quad z_a^{(j)}=W^{(j)}h_a^{(j-1)},\quad
h_a^{(j)}=\phi_j(z_a^{(j)}),\quad f_a=w^\top h_a^{(L)}/n,
\]
\[
k_a^{(L)}=w,\qquad
\delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot k_a^{(j)},\qquad
k_a^{(j)}=W^{(j+1)\top}\delta_a^{(j+1)}.
\tag{FC.1}
\]
The residual is \(r_a=f_a-y_a\), and the loss is
\(m^{-1}\sum_a r_a^2\). In physical time the exact equations are
\[
\dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\quad
\dot W^{(j)}=-\frac2{mn}\sum_a r_a\delta_a^{(j)}h_a^{(j-1)\top},
\quad \dot w=-\frac2m\sum_a r_a h_a^{(L)}.
\tag{FC.2}
\]
Thus these are the original mobilities \((n,1,\ldots,1,n)\).
Initially \(A_{ik}\sim N(0,1)\), \(W^{(j)}_{ik}\sim N(0,1/n)\)
independently and \(w=0\). Every label restriction below is a consequence
of the original common label allowance; none replaces it by a smaller cap.

Let
\[
\lambda=\gamma/m,\quad r=\lambda^{-1},\quad
Y=\|y\|_2/\sqrt m>0,\quad S=16Yr\le1,\quad
\ell=\log(en),\quad B=\beta^{100L}.
\tag{FC.3}
\]
The scalar \(r\) is distinct from the indexed residual \(r_a\).
The zero-label branch is the exact constant zero predictor. The nonzero
finite-word branch retains \(nY\ge1\). The source/fitting bounds give
\(Y\le\beta^{3L}\) and \(r^{-1}\le\beta^{6L}\).
All estimates use the existing
\[
Z=\ell+\log\left(e+
\frac{(m+d+2)\beta^{100L}(1+r)}\delta\right).
\]
The implemented moment order is \(p\); it has fixed source confidence and
is prescribed in the integrated theorem, with \(\log(p+2)\le CZ\).

Here is the exact event used from the internal finite-source lemma. The
training trajectory, its forward/backward fields and the training response
fields are holomorphic on a neighborhood of
\[
[-r_t,32\ell/\lambda+r_t]+i[-r_t,r_t],\qquad
r_t=\frac1{pB(1+\lambda)\sqrt\ell}.
\tag{FC.4}
\]
The initialized operator bounds, the fitted real trajectory, and all-time
real feature bounds hold there with their stated real/complex distinction.
On the complex domain, hidden operators are at most ten, training feature
RMS is at most \(\beta^{3L}\), training backward RMS is at most
\(S\beta^{6L}\), carrier maximum is at most
\(S\beta^{40L}\sqrt\ell\), and the preactivation imaginary part is
at most \(a/4\). The parameter-gradient response satisfies
\[
\max_{a,b,j}\|R_{ba}^{(j)}\|_\infty
\le S\beta^{72L}\sqrt\ell.
\tag{FC.5}
\]
Here \(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\) and
\(R_{ba}^{(j)}=D_\Theta z_b^{(j)}\nabla_\Theta(nf_a)\), with the
Euclidean/Frobenius gradient in these blocks. This definition includes all
mobility and width factors and contains no residual.
For normalized time \(\tau=\lambda t\), a disk of radius
\(\lambda r_t/2\) about a real anchor \(\tau_j\) has training residual
RMS at most \(2Y e^{-\tau_j/4}\). These are direct conclusions of that
source lemma at the full label allowance. In particular, no lower bound of
the form \(\sqrt\ell\ge c(m,\gamma,\beta,L)\) is imported here.

For a displacement \(u=(A-A_0,W^{(2)}-W_0^{(2)},\ldots,w)\), use
\[
\|u\|_\Sigma=\|A-A_0\|_F/\sqrt n+
\sum_{j=2}^L\|W^{(j)}-W_0^{(j)}\|_F+\|w\|_2/\sqrt n,
\]
\[
\|u\|_{\mathcal H}^2=\|A-A_0\|_F^2/n+
\sum_{j=2}^L\|W^{(j)}-W_0^{(j)}\|_F^2+\|w\|_2^2/n.
\tag{FC.6}
\]
Then \(\|u\|_{\mathcal H}\le\|u\|_\Sigma\le
c_L\|u\|_{\mathcal H}\), where \(c_L=\sqrt{L+1}\).
Set \(\bar u(\tau)=u(r\tau)/Y\). This normalization changes proof
coordinates only. The normalized vector field is denoted by
\(\overline F\).

## 2. Analytic tube and real stability, with explicit panel orders

Choose the normalized source horizon and the equal-panel mesh by
\[
T_0=2\{10\log n+\log(1+66Br)\},\qquad
T_0\le T\le T_0+1/4,\qquad
h_0\le\frac1{128pB(1+r)\sqrt\ell},\qquad H=\lceil T/h_0\rceil,
\quad h=T/H.
\tag{FC.7}
\]
Choose a certified dyadic upper approximation \(T\) in the indicated
interval and the largest dyadic \(h_0\) below its bound. The numerical
horizon gate gives \(T_0<24\ell\), hence \(T<32\ell\).
Now \(T/h_0\) is rational, its ceiling is an exact integer operation,
and the equal-panel length \(h=T/H\) is rational. Scalar integration
weights using this rational are rounded only at their declared local
arithmetic step. Thus \(h_0/3\le h\le h_0\), and
\[
H\le CpB(1+r)Z\sqrt\ell.
\tag{FC.8}
\]
Every radius-\(4h\) panel disk lies in (FC.4). Put
\[
q(\tau)=2^{-\lfloor\tau/4\rfloor},\quad q_j=q(jh),\quad
q_T=q(T),\qquad
d_n=\frac{\beta^{-200L}q_T}{(1+r)^2\sqrt n},
\]
\[
M=B(1+r),\qquad \Lambda_j=B(1+r)(1+q_j\sqrt\ell).
\tag{FC.9}
\]
We first verify the tube needed for numerical restarts. A physical parameter
perturbation of sum norm at most \(Yd_n\) changes a training preactivation
by RMS at most \(\beta^{4L}Yd_n\), by forward subtraction of (FC.1).
Indeed, each changed-matrix term is bounded by the old feature RMS times
its matrix operator norm, and each unchanged hidden propagation multiplies
the previous RMS error by at most \(11\beta\le\beta^3\).
Its coordinate error is therefore at most \(\sqrt n\beta^{4L}Yd_n<a/16\).
Stopping the segment at a first half-strip exit proves that no exit occurs.
The operator cap increases by at most one.

Backward subtraction at a reference source state uses
\[
\Delta\delta^{(j)}=\phi_j'(\widetilde z^{(j)})\odot\Delta k^{(j)}
+[\phi_j'(\widetilde z^{(j)})-\phi_j'(z^{(j)})]\odot k^{(j)},
\quad
\Delta k^{(j)}=\widetilde W^{(j+1)\top}\Delta\delta^{(j+1)}
+\Delta W^{(j+1)\top}\delta^{(j+1)}.
\tag{FC.10}
\]
Only the changed-gate term uses a reference carrier maximum. Summing the
downward linear recursion gives RMS at most
\(\beta^{50L}(1+S\sqrt\ell)Yd_n\). There is one carrier-maximum
factor, not a product of such factors across layers. Conversion to a
coordinate bound, using \(Y/S=1/(16r)\), \(r^{-1}\le\beta^{6L}\),
and (FC.9), keeps the carrier maximum within twice its source bound.
Prediction subtraction on the training complex tube has coefficient at most
\(\beta^{8L}\) in the physical sum norm. At real parameter states the
same bound holds for every real unit input, by the real all-sphere feature
bound and forward subtraction; no passive complex-time analyticity is used.
The residual
on this tube is consequently at most \(3Yq_j\) in sample RMS.

Subtracting the three factors in each gradient product of (FC.2), and
using the forward and backward subtractions just proved, bounds the
complex normalized Jacobian by \(\Lambda_j\). For clarity, before
normalization the residual-difference terms contribute at most
\(\beta^{70L}\), and the backward/feature-difference terms contribute
at most \(\beta^{70L}Yq_j(1+S\sqrt\ell)\). Normalization multiplies
this by \(r\); \(Yr\le1/16\) and the unused powers from 70 to 100
give (FC.9). The normalized true derivative is at most \(M\).
Thus the unclipped field is holomorphic and \(\Lambda_j\)-Lipschitz
on the complex normalized sum-norm tube of radius \(d_n\).

The sharper real estimate is essential. In the Euclidean coordinates
\(P=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)\), (FC.2) is
\(\dot P=-\nabla_P\mathcal L\). The blocks of \(g_a=\nabla_Pf_a\)
are \(\delta_a^{(1)}v_a^\top/\sqrt n\),
\(\delta_a^{(j)}h_a^{(j-1)\top}/n\), and
\(h_a^{(L)}/\sqrt n\). Differentiating the forward recursion in a
physical direction gives RMS derivatives of \(z,h\) at most
\(\beta^{9L}\|e\|_\Sigma\). Differentiating (FC.10), with the
unchanged point as reference, gives backward derivative RMS at most
\(\beta^{55L}(1+S\sqrt\ell)\|e\|_\Sigma\). Each hidden block of
\(Dg_a[e]\) is the sum of the two outer products
\(D\delta_a[e]h_a^\top/n+\delta_a Dh_a[e]^\top/n\);
their Frobenius norms are products of the respective RMS norms. Summing
the at most \(L+1\) blocks, and using \(\|e\|_\Sigma\le c_L\|e\|_{
\mathcal H}\), proves
\[
\|D_P^2f_a\|_{\mathcal H\to\mathcal H}
\le\beta^{70L}(1+S\sqrt\ell).
\tag{FC.11}
\]
The real normalized Jacobian is exactly
\[
D\overline F=-\frac{2r}{m}\sum_a
\{g_ag_a^\top+r_aD_P^2f_a\}.
\]
Its first quadratic form is nonpositive. Using the tube residual bound
and (FC.11) on its second term gives
\[
\langle e,D\overline F e\rangle_{\mathcal H}
\le\mu_j\|e\|_{\mathcal H}^2,
\quad \mu_j=\beta^{80L}q_j(1+S\sqrt\ell),
\quad E_+=9\beta^{80L}(1+S\sqrt\ell).
\tag{FC.12}
\]
Indeed \(m^{-1}\sum_a|r_a|\le3Yq_j\) and \(rY\le1/16\).
Since \(\int_0^\infty q=8\), its decreasing left sums obey
\(\sum_jhq_j\le8+h\le9\), so \(\sum_jh\mu_j\le E_+\).
This estimate holds throughout each real tube and hence on segments
between the compared states. It is not applied on complex segments.

Choose
\[
\varepsilon=\min\{d_n/(2^{12}c_L),n^{-10}/(2^{12}Bc_L)\},
\]
\[
K=8+\left\lceil\frac{4E_+
+\log[2^{20}(c_L+1)(M+1)(T+1)/\varepsilon]
+\log(1+16c_LH)}{\log2}\right\rceil,
\]
\[
\delta_0=\frac{\beta^{-150L}S q_T}{(1+r)^2\sqrt n},\quad
C_N=B^2(1+r)^2\sqrt\ell,\quad
\delta_\dagger=\min\left\{\delta_0,
\frac{\varepsilon e^{-4E_+-10}}{2^{20}C_N(T+1)}\right\}.
\tag{FC.13}
\]
These are constructive choices, with fixed fractions of \(\delta_\dagger\)
allocated below. In particular
\[
K+\log(1/\delta_\dagger)+\log(1/\varepsilon)
+\log(H+1)+\log(h^{-1})\le CBZ.
\tag{FC.14}
\]
To check the small scales, \(S\ge16\beta^{-6L}/n\),
\(q_T^{-1}\le2e^{T\log2/4}\), and \(T\le CZ\); every remaining
factor in (FC.13) has logarithm at most \(CZ\), apart from
\(E_+\le CB\sqrt\ell\). No algebraic factor \(r\) enters the
degree or numerical word length.

## 3. Causal coefficients, real activation values, and physical forcing

Use \(\xi=(\tau-jh)/h\); brackets \([k]\) denote its power-series
coefficients. The current physical parameters have coefficients through
degree \(K\), and the normalized recurrence is
\[
\bar u[0]=\bar u_j,\qquad
\bar u[k+1]=\frac h{k+1}[\xi^k]\overline F
\left(\sum_{b=0}^k\bar u[b]\xi^b\right),\quad 0\le k<K.
\tag{FC.15}
\]
At a fixed order evaluate forward layers upward, backward layers downward,
residuals, and then gradient coefficients. Write
\(D^{(j)}=W^{(j)}-W_0^{(j)}\). The initialized actions are exactly
\[
z_a^{(j)}[k]=W_0^{(j)}h_a^{(j-1)}[k]
+\sum_{b+c=k}D^{(j)}[b]h_a^{(j-1)}[c],
\]
\[
k_a^{(j)}[k]=W_0^{(j+1)\top}\delta_a^{(j+1)}[k]
+\sum_{b+c=k}D^{(j+1)}[b]^\top\delta_a^{(j+1)}[c].
\tag{FC.16}
\]
The first layer uses its \(d\) root columns and fixed input coordinates;
the top backward carrier is \(w[k]\). For
\(g_a^{(j)}[b]=\sum_{c+e=b}r_a[c]\delta_a^{(j)}[e]\), the physical
hidden coefficients satisfy
\[
D^{(j)}[k+1]=-
\frac{2hr}{mn(k+1)}\sum_a\sum_{b+c=k}
g_a^{(j)}[b]h_a^{(j-1)}[c]^\top.
\tag{FC.17}
\]
The analogous first and readout formulas are obtained directly from
(FC.2). A learned matrix is represented by these actual stored factors
and scalar weights; no orthogonalization or inverse Gram enters them.
Committing a panel appends their integrated weights. All old fields keep
their original scalar arguments.

Here is a finite value-based realization of the activation coefficients.
Let \(\alpha=\min(1,a/16)\), so \(\alpha^{-1}\le\beta\).
At a real order-zero preactivation \(x\), interpolate \(J_a\) values
of \(\phi(x+\alpha t_i)\), where
\(t_i=-1+2i/(J_a-1)\). Each supplied value has absolute error at most
\(\nu\). Use its polynomial \(p_x\) in the centered variable
\((z-x)/\alpha\), and use the actual derivative of this same polynomial
for the backward gate.

For completeness, subtract \(\phi(x)\), which interpolation reproduces.
On \(|s|=4\), the resulting function has modulus at most \(4\beta\alpha\).
The residue formula with \(\omega(s)=\prod_i(s-t_i)\) gives interpolation
error at most \(C\beta\alpha2^{-J_a}\) on \(|s|\le1/2\): numerator
factors are at most \(3/2\) and denominator factors at least three.
The sum of the absolute cardinal polynomials on that disk is at most
\[
\frac{[3(J_a-1)/2]^{J_a-1}}{(J_a-1)!}\le5^{J_a}.
\]
Cauchy's formula on circles of radius \(1/4\), followed by rescaling,
therefore proves simultaneous value/first/second derivative errors at most
\(C\beta^2(2^{-J_a}+5^{J_a}\nu)\) on \(|z-x|\le\alpha/4\).
Choose
\[
J_a\ge\max\{K+2,\lceil\log_2(C\beta^2/\delta_\dagger)\rceil\},
\qquad \nu\le\delta_\dagger/(C\beta^2 5^{J_a}),
\tag{FC.18}
\]
with the least admissible orders and fixed additional error fractions.
Then \(J_a\le CK\) and \(\log\nu^{-1}\le CBZ\).
Only real values are requested; their evaluator costs remain charged.

The scalar disk is available at each computed center. From (FC.2), (FC.5)
and residual RMS at most \(2Y\),
\(\|\partial_\tau z_a^{(j)}\|_\infty\le
S^2\beta^{72L}\sqrt\ell/4\). A radius-\(4h\) panel changes the
reference preactivation by at most \(hS^2\beta^{72L}\sqrt\ell<
\alpha/4096\). The tube changes it by at most
\(\sqrt n\beta^{4L}Yd_n<\alpha/4096\). The small node defects
below leave the same strict margin. A first-exit argument therefore puts
all polynomial evaluations in their interpolation disks.

In the following bounds \(R\) is the deterministic enclosing field/call
count explicitly constructed in (FC.25); that recipe depends only on the
orders already chosen. Every initialized action is replaced by
\(W_0v+\sigma\zeta\) or
\(W_0^\top u+\sigma\zeta\), with fresh hidden independent
\(\zeta\sim N(0,I_n)\). On the event that each such vector has RMS at
most two, its errors through one panel through coefficient \(K-1\)
form a polynomial of RMS at most \(\sigma4^K\) on \(|\xi|\le4\).
Only those orders are needed by (FC.15). Choose
\[
\sigma\le\tfrac1{64}\delta_\dagger4^{-K}.
\tag{FC.19}
\]
Every positive tolerance specified by an upper bound here is chosen as the
largest dyadic below the stated minimum, after the fixed budget fractions.
The precision upper bounds refer to those choices, not arbitrary smaller
numbers. The common noise level is refined in Section 5 before setup.
The probability of a raw-noise RMS violation is at most \(Re^{-n/2}\).
Indeed exponential Markov with parameter \(3/8\) gives
\(\Pr(\|\zeta\|_2^2>4n)\le
\exp[-(3-\log4)n/2]\le e^{-n/2}\).

Physical scalar pair calls use the actual created operands and return
\(\widehat p(u,v)=n^{-1}u^\top v+e\), with
\(|e|\le\epsilon_{\rm pair}\). If an actual stored matrix is
\(D=n^{-1}\sum_\mu c_\mu a_\mu b_\mu^\top\), its approximate
forward action differs from its exact action by precisely
\[
\sum_\mu c_\mu a_\mu e(b_\mu,v).
\tag{FC.20}
\]
This compares the same realized matrix on both sides. Let
\(N_{\rm sum}=C(R+K+1)^3\) bound all rank/convolution summand counts,
and let \(A_\ast\ge2\) bound their scalar weights, factor RMS,
\(n+1,m,L,K,Y^{-1},h^{-1}\), and inverse strict guard margins.
Use finite bounds from the explicit formulas with a factor-four slack;
interpolation scratch has size \(e^{CJ_a}\) times a polynomial in these
scales. Thus \(\log A_\ast\le CBZ\).
Equation (FC.20) has RMS at most
\(N_{\rm sum}A_\ast^2\epsilon_{\rm pair}\). Readout coefficients
are sums of pairs and have scalar error at most
\(N_{\rm sum}\epsilon_{\rm pair}\). The exact rank-matrix norm is
\[
\|D\|_F^2=\sum_{\mu,\nu}c_\mu c_\nu
\langle a_\mu,a_\nu\rangle_n\langle b_\mu,b_\nu\rangle_n;
\]
its pair-error change is at most
\(3N_{\rm sum}^2A_\ast^4\epsilon_{\rm pair}\).
Converting integrated-coefficient errors to velocity errors multiplies by
\((k+1)/(hY)\), already in the polynomial allowance. Consequently all
these physical errors, including normalized residual errors, extend to
forcing polynomials bounded by
\(C4^KN_{\rm sum}^2A_\ast^8\epsilon_{\rm pair}\). Choose
\[
\epsilon_{\rm pair}\le
\delta_\dagger/(C4^KN_{\rm sum}^2A_\ast^{10}).
\tag{FC.21}
\]
Principal local arithmetic outputs obey the same allowance. Their finite
precision uses only the logarithms in (FC.14), (FC.18), (FC.21): centered
polynomial interpolation has coefficient sums at most \(e^{CJ_a}\), and
truncated convolution is submultiplicative in coefficient \(\ell^1\).
It never raises the large real center to power \(J_a\).

Freeze the realized coefficient errors into these forcing polynomials.
This is a proof construction, not advance observation of future noises.
The resulting holomorphic field \(\overline F_j^{\rm num}(\xi,U)\),
with fixed polynomial activation coefficients and fixed forcings, obeys
\[
\|\overline F_j^{\rm num}-\overline F\|_\Sigma
\le C_N\delta_\dagger=:\eta_\dagger,\qquad
\|D_U\overline F_j^{\rm num}\|\le2\Lambda_j.
\tag{FC.22}
\]
To verify the label scaling, forward error is at most
\(\beta^{4L}\delta_\dagger\); backward error is at most
\(\beta^{60L}(1+S\sqrt\ell)\delta_\dagger\); readout RMS is at most
\(C\beta^{3L}S\); hence residual error is at most
\(\beta^{10L}S\delta_\dagger\). Subtraction of the residual/backward/
feature factors gives physical field error at most
\(C\beta^{80L}[Y(1+S\sqrt\ell)+S+S^2]\delta_\dagger\).
Multiplication by \(r/Y\), using \(S/Y=16r\), gives (FC.22).
An independently added residual error of RMS \(Y\delta_\dagger\) has the
same bound. Differentiating the same recursions uses only the first two
polynomial derivatives from (FC.18) and the same tube bounds, proving the
second inequality. No derivative of an activation center is taken.

If the starting Hilbert error is \(e_j\) with \(c_Le_j\le d_n/8\),
the difference equation on \(|z|<4h\) is a contraction in the sum-norm
ball of radius \(d_n/2\): its contraction factor is
\(8h\Lambda_j\le1/4\), and its forcing is bounded by
\(c_Le_j+4h\eta_\dagger\). Thus both local flows exist on that disk,
and their difference is at most \(2c_Le_j+8h\eta_\dagger\).
On its real diameter, (FC.12) instead gives Hilbert error
\((e_j+s\eta_\dagger)e^{s\mu_j}\). Cauchy's coefficient estimate at
radius \(2h\) then gives the endpoint recurrence
\[
e_{j+1}\le(1+2h\mu_j+2c_L2^{-K})e_j
+4h\eta_\dagger+2Mh2^{-K}.
\tag{FC.23}
\]
The extra unit in the forcing coefficient pays separately rounded endpoints;
they are additive errors, not forcings asserted to leave the polynomial
unchanged. The same calculation controls interior times. Products of the
multipliers are at most \(\exp(2E_++2c_LH2^{-K})\). Substitution of
(FC.13) bounds the total error by \(\varepsilon/8\), provided
\[
e_0\le\varepsilon e^{-4E_+-10}/2^{20}.
\tag{FC.24}
\]
The proof closes the tube assumptions inductively. Strict-slack guards
are justified causally: at a first potentially active guard, freeze the
preceding defects and complete the remaining panel with zero defects.
The contraction just proved supplies its local solution. Formal coefficient
induction identifies the already computed prefix with that solution, whose
Cauchy bounds lie strictly inside the guard. The proposed first activation
is impossible. The argument applies to coefficient caps and approximate norm
tests using (FC.20)–(FC.21), and inserts no residual projection into the
holomorphic recurrence.

Uniform real prediction subtraction and the original fitting tail at \(T\)
now give a parameter-defined predictor of error at most \(CYn^{-10}\),
for the entire sphere and all physical times, when parameters are frozen
after \(T\). This includes the dense fitted endpoint.

## 4. Actual named fields and the finite Gaussian law

Fix the source instructions before drawing randomness. In each panel and
for each sample/layer/order name the preactivation, activation, gate,
backward carrier, backward response, residual-weighted backward response,
and each initialized answer in (FC.16). Also name the interpolation sample
values and its needed centered coefficients, the readout coefficients,
the constant field, and the \(d\) first-layer root columns. Each initialized
call names one innovation field. Coefficient products internal to one
coordinatewise interpolation or convolution are temporary scalar work;
they never become operands of empirical reductions. Residuals and rank
weights are shared scalars. This is a literal finite field recipe, of size
\[
R_0=1+d+C_0mLH(K+J_a+1),\qquad R=R_0+C_0(L+1),
\tag{FC.25}
\]
where a fixed integer \(C_0\), for example 128, covers the listed field
types and reserved query fields. Naming a reused field twice is unnecessary.
The bounds (FC.8), (FC.14), (FC.18), and \(L\le\beta^L\) give
\[
R\le Cp\beta^{201L}(m+d+2)(1+r)Z^{5/2}.
\tag{FC.26}
\]
There are \(O(mLHK^2)\) rank weights, at most \(CR^2\); there are
not that many distinct row factors. Acquisition of every missing unordered
pair is performed when both fields exist, at the end of a complete matrix
call when necessary. Mandatory innovation contractions remain inside their
own call. Thus at most \(P\le C_1R^2\) scalar acquisitions occur.
Here \(P\) includes each scalar component of every mandatory innovation
contraction, ordinary complete-table pair, and appended query reduction.
Reserve distinct scalar marks for all of them, including an innovation pair
that may also have an ordinary pair entry. This counts every finite scalar
sampler used in the Gaussian cutoff below.
All scalar means use the constant field. Norms of rank matrices use products
of acquired pairs as displayed after (FC.20), not additional fourth moments.

One fully explicit oversized local cap in Section 3 is
\[
A_\ast=2^{128(J_a+K+1)}
\big[(n+1)(m+L+d+R+K+2)(B+1)(1+r)
(1+Y^{-1})(1+h^{-1})(1+d_n^{-1})(1+S^{-1})\big]^{128}.
\tag{FC.27}
\]
It exceeds the physical Cauchy coefficient bounds, rank weights, all
interpolation intermediate coefficient sums, and the inverse fixed guard
margins. For example, endpoint rank weights are bounded by a polynomial in
\(rT,K,m\); interpolation weights by \(e^{CJ_a}\); and principal
coordinate bounds by \(\sqrt n\) times their RMS bounds. Each displayed
operation has bounded product degree or its explicit centered interpolation
coefficient bound. Enlarging the fixed factor 128, if required by a chosen
arithmetic implementation, changes no parameter exponent. Its logarithm is
at most \(CBZ\). Take \(b=A_\ast\) as a common loose RMS cap for all
physical query/raw-answer fields; interpolation-only fields do not enter
physical posterior Gram solves. Their finite coordinate caps are retained
separately for metric selection.

We now derive the initialized-matrix calls, including their two orientations.
For a single hidden matrix \(W\) with iid \(N(0,1/n)\) entries, suppose
the previous raw observations are
\[
Y_f=WV+\sigma\Xi,\qquad X_b=W^\top U+\sigma Z_b.
\tag{FC.28}
\]
Here \(V\in\mathbb R^{n\times a}\), \(U\in\mathbb R^{n\times b_h}\)
are predictable old forward and reverse queries. The noise vectors are fresh
independent standard Gaussians and are hidden. The letters \(Y_f,X_b\)
denote answer matrices and are unrelated to the label scale \(Y\).
At a complete observable history, put
\[
Q=V^\top V/n,\quad K_h=U^\top U/n,\quad
H_c=U^\top Y_f/n,\quad J_c=X_b^\top V/n,\quad \Delta=\sigma^2.
\]
The likelihood times prior density is proportional to
\[
\exp\{-\tfrac n2\|W\|_F^2
-\tfrac1{2\Delta}(\|Y_f-WV\|_F^2+\|X_b-W^\top U\|_F^2)\}.
\]
Predictability permits this expression even for adaptive calls: each query
is fixed after the preceding answer history is fixed. Completing its square
shows that the posterior mean solves
\[
\Delta\overline W+(UU^\top/n)\overline W
+\overline W(VV^\top/n)=(Y_fV^\top+UX_b^\top)/n.
\tag{FC.29}
\]
The covariance operator is \((\Delta/n)
(\Delta I+\mathcal L_{UU^\top/n}+\mathcal R_{VV^\top/n})^{-1}\),
where left and right multiplication have their literal meanings. Its inverse
is well defined since the quadratic form of its denominator is at least
\(\Delta\|M\|_F^2\). Likelihoods factor by matrix label, preserving
conditional independence of different hidden matrices.

Define \(C=(\Delta I+Q)^{-1}\), \(D=(\Delta I+K_h)^{-1}\), and solve
\[
(\Delta I+K_h)E+EQ=-H_cC-DJ_c.
\tag{FC.30}
\]
Diagonalizing the two real symmetric coefficients shows that all Sylvester
divisors are \(\Delta+\lambda_i(K_h)+\lambda_j(Q)\ge\Delta\).
Direct substitution in (FC.29) verifies
\(\overline W=Y_fCV^\top/n+UDX_b^\top/n+UEV^\top/n\).
For the next forward query \(q\), let
\(v=V^\top q/n\), \(x=X_b^\top q/n\), \(d_q=q^\top q/n\).
Its conditional mean is
\[
m_q=Y_fCv+U(Dx+Ev).
\tag{FC.31}
\]
For the next reverse query \(u\), it is
\(V(CY_f^\top u/n+E^\top U^\top u/n)+XD(U^\top u/n)\),
with \(X=X_b\).

Set
\[
f(a)=\frac\Delta{\Delta+a}
\{d_q-v^\top[(\Delta+a)I+Q]^{-1}v\},\quad a\ge0.
\tag{FC.32}
\]
Diagonalize \(UU^\top/n\) and \(VV^\top/n\) in the posterior covariance
operator. The variance of \(Wq\) along an eigenvector of the former with
eigenvalue \(a\) is \((\Delta/n)q^\top[(\Delta+a)I+VV^\top/n]^{-1}q\).
The identity
\[
(cI+VV^\top/n)^{-1}
=c^{-1}[I-V(cI+Q)^{-1}V^\top/n]
\]
is checked by multiplication and turns this variance into (FC.32). Therefore
the next noisy answer has covariance
\(\Gamma=\Delta I+f(UU^\top/n)\). In particular
\(0\le f(a)\le d_q\) and \(\Gamma\succeq\sigma^2I\).

Let \(f_0=f(0)\), \(c=\sqrt{\Delta+f_0}\), and define the rational
divided difference
\[
h_f(a)=\frac{-f_0+\Delta v^\top C[(\Delta+a)I+Q]^{-1}v}{\Delta+a},
\qquad
T_q(a)=\frac{h_f(a)}{\sqrt{\Delta+f(a)}+c}.
\tag{FC.33}
\]
Resolvent subtraction gives \(a h_f(a)=f(a)-f_0\), including zero by
continuity; no division by a possibly zero Gram eigenvalue occurs. Along
each singular direction of \(U/\sqrt n\),
\(c+aT_q(a)=\sqrt{\Delta+f(a)}\). Hence
\[
\Gamma^{1/2}=cI+UT_q(K_h)U^\top/n.
\tag{FC.34}
\]
This is the positive square root. Every inverse above has floor
\(\sigma^2\), and the denominator in (FC.33) has floor \(2\sigma\).
The reverse formula exchanges the forward and reverse histories. Empty
histories simply omit their blocks.

All these coefficients are computable with matrices of order at most
\(CR\). In eigenbases of \(Q,K_h\), the Sylvester solve divides entry
\((i,j)\) by \(\Delta+k_i+q_j\), and the two contractions needed in
(FC.33) are
\[
\sum_j\frac{\widetilde v_j^2}{\Delta+k_i+q_j},\qquad
\sum_j\frac{\widetilde v_j^2}{(\Delta+q_j)(\Delta+k_i+q_j)}.
\tag{FC.35}
\]
There is no materialized Kronecker matrix. Away from genuine moment arrays,
symmetrize the whole physical-field Gram, project it onto the PSD cone and
cap its Frobenius norm at \(8R b^2\). This protection fixes a genuine Gram
under the cap. Euclidean projection on a closed convex set is nonexpansive:
the two minimizing variational inequalities imply
\(\|Px-Py\|^2\le\langle Px-Py,x-y\rangle\).
The protected augmented block \(\left(\begin{smallmatrix}Q&v\\v^\top&d_q
\end{smallmatrix}\right)\) is a Gram, so its \(f(a)\) is nonnegative
by the same variance formula. Positive-part protections on any finitely
computed \(f\) preserve the explicit floors.

These coefficient maps have fixed polynomial local sensitivity. For a
checkable envelope let \(z=C(2+R+b+\sigma^{-1})\). Genuine/protected Gram
norms are at most \(z^4\); inverse norms are at most \(z^2\).
For perturbation size \(e\) in the moment entries, Frobenius conversions
cost at most \(z^2\). The inverse identity gives error at most \(z^6e\).
Subtracting (FC.30) gives \(E\)-error at most \(z^{18}e\), including
its bounded right side. Resolvent contractions (FC.35), or their equivalent
gapped tensor formulas, have errors at most \(z^{36}e\). The square-root
bound
\(\|A^{1/2}-B^{1/2}\|_F\le(2\sigma)^{-1}\|A-B\|_F\)
follows by solving
\(A^{1/2}X+XB^{1/2}=A-B\). Multiplying the remaining factors and
applying the final gapped inverse bounds the correction and mean coefficient
errors by \(z^{60}e\). Thus \(z^{100}\) is a common coefficient and
Lipschitz cap, with ample dimension and constant slack. This calculation is
for one call, not a product across earlier calls.

## 5. One finite pre-setup precision schedule and chronological coupling

The finite row packet contains its \(d\) first roots and one innovation
coordinate for every prescribed training call and every reserved query call.
All coordinates are independent. Scalar-noise marks are a separate independent
finite bit string. A finite Gaussian sampler can be coupled to a standard
Gaussian \(g\) with coordinate error at most \(\epsilon_G\) when
\(|g|\le T_G\): use the midpoint of the \(b_G\)-bit interval containing
\(\Phi(g)\), then a certified inverse CDF clipped to \([-T_G,T_G]\).
The interval index is uniform. The clipped inverse has Lipschitz constant
at most \(\sqrt{2\pi}e^{T_G^2/2}\); consequently
\[
b_G\log2\ge T_G^2/2+\log(C/\epsilon_G)
\tag{FC.36}
\]
suffices, with inverse-evaluation error at most \(\epsilon_G/2\).
The finite arithmetic backend supplies the certified evaluation. For
\(N_G=n(d+R)+P+1\), choose
\(T_G=\lceil2+\sqrt{2\log(1024N_G/\rho_0)}\rceil\), with
\(\rho_0=2^{-20}\). The union of coupled sampler failures is below
\(\rho_0/512\). The implemented algorithm draws bits directly.

All named row fields are dyadic. An ordinary pair acquisition uses exact
dyadic products and exact integer summation, retains division by \(n\)
as a rational until rounding, and records
\[
C_a=Q_{h_s}\left(n^{-1}\sum_i u_a(i)v_a(i)+\eta\widehat e_a\right).
\tag{FC.37}
\]
Here \(Q_{h_s}\) is fixed nearest-grid rounding with a fixed tie convention,
and \(h_s\le\eta\) is the scalar grid, distinct from the panel length.
For a forward matrix call compute the protected mean coefficients,
symmetric correction \(\widetilde T\), and scalar \(\widetilde c\)
before reading its fresh innovation. Put
\(A_c=U^\top/n\), \(B_c=U\widetilde T\). Then execute
\[
\widehat t=Q_{h_t}(A_c\widehat g+\eta\widehat e),\qquad
\widehat y=Q_{h_y}(\widetilde m+B_c\widehat t+
\widetilde c\widehat g).
\tag{FC.38}
\]
Small coefficient arrays are rounded once to dyadics, symmetrically where
required; final row combinations have exact dyadic arithmetic before the
indicated rounding. The guard \(\widetilde c\ge\sigma/2\) is inactive
on the successful range. No other matrix call or new coefficient solve
occurs between these two operations. Reverse calls exchange orientations.
The subsequent complete-table pairs are acquired after the answer is formed.

At a fixed past consider, only for the proof, the affine Gaussian shadow
\[
t=A_cg+\eta e,\qquad y=\widetilde m+B_ct+\widetilde c g.
\tag{FC.39}
\]
Its answer covariance is
\(\widetilde\Gamma=\widetilde S^2+\eta^2B_cB_c^\top\), where
\(\widetilde S=\widetilde cI+B_cA_c\) is symmetric. The map is
invertible since \(\eta,\widetilde c>0\):
\[
g=(y-\widetilde m-B_ct)/\widetilde c,\qquad
e=(t-A_cg)/\eta.
\tag{FC.40}
\]
Therefore the entire finite call (FC.38), including every finite innovation
mark used later, is a deterministic function \(J_H(y,t)\): reconstruct
(FC.40), apply the fixed sampler functions and run the finite arithmetic.
This possibly discontinuous map is used only in the proof. The algorithm
executes (FC.38) directly and pays no numerical cost for (FC.40).

Let \(Q_H(dy,dt)\) be the shadow kernel. Couple it to the physical call
\(y=W_0q+\sigma\zeta\), with hidden fresh noise, by attaching
\(t\mid(H,y,W_0)\sim Q_H(dt\mid y)\), then applying the same \(J_H\).
This attachment is conditionally independent of every initialized matrix
given \((H,y)\); its likelihood cancels in Bayes' formula. Consequently
the Gaussian posterior derived in Section 4 remains valid at the next
complete call, even if the finite marks are reused. Moreover
\[
\|Q_H(dy,dt)-P_H(dy)Q_H(dt\mid y)\|_{\rm TV}
=\|Q_H(dy)-P_H(dy)\|_{\rm TV}.
\tag{FC.41}
\]
Integration against the common conditional kernel gives one inequality;
projection onto \(y\) gives the reverse. Deterministic finite postprocessing
cannot increase this distance. The proof filtration includes raw answers,
but excludes hidden physical noise, future innovation coordinates, and the
private selected metric. No Gaussian-posterior claim is made at the
intermediate prefix that reveals only \(\widehat t\).

Here are quantitative finite choices. Let
\(\mathcal M=(n+1)z^{120}\). This bounds every row-affine norm in
(FC.38). Direct subtraction from (FC.39) gives
\[
\|\widehat t-t\|_\infty
\le(\mathcal M+1)\epsilon_G+h_t/2=:d_t,
\quad
\|\widehat y-y\|_\infty
\le h_y/2+\mathcal M d_t+\mathcal M\epsilon_G.
\tag{FC.42}
\]
Choose \(h_t\le\min(\eta,h_y/(64\mathcal M))\) and
\(\epsilon_G\le\min(h_t/(64\mathcal M),h_y/(64\mathcal M^2))\).
Then the answer error is below \(h_y\). At a shared raw history the
old finite and raw answers differ by at most \(h_y\). Their moments
differ by at most \(2bh_y+h_y^2\); acquired-pair noise adds at most
\(\eta(T_G+1)+h_s\). Thus the coefficient input error is at most
\[
e_{\rm mom}=C\{(b+1)h_y+h_y^2+\eta(T_G+1)+h_s\}.
\tag{FC.43}
\]
Both queries are the same actual finite vectors at this history; there is
no comparison with recomputed queries at a different history. If finite
coefficient error is \(\epsilon_c\), put
\(e_c=e_{\rm mom}+z^{10}\epsilon_c\). Section 4's local estimates give
\(\|\widetilde m-m\|_2\le\sqrt n z^{110}e_c\) and
\(\|\widetilde S-S\|_{\rm op}\le z^{110}e_c\), including the old
answer-to-finite-answer change in the row combinations. Also
\(\|B_cB_c^\top\|_F\le nRb^2z^{200}\).

Since \(S\succeq\sigma I\), a sufficient smallness condition is
\[
\kappa=z^{230}(\sqrt n\,e_c+n\eta^2)\le1/32.
\tag{FC.44}
\]
It implies \(\widetilde S\succeq\sigma I/2\). Expanding
\(\widetilde S^2-S^2=(\widetilde S-S)\widetilde S+S(\widetilde S-S)\)
bounds the Frobenius covariance error. To verify the TV conclusion, write
\(E=\Gamma^{-1/2}(\widetilde\Gamma-\Gamma)\Gamma^{-1/2}\).
The Gaussian density integral gives relative entropy
\[
\tfrac12\{\|\Gamma^{-1/2}(\widetilde m-m)\|^2+
\operatorname{tr}E-\log\det(I+E)\}.
\]
For \(\|E\|\le1/2\), diagonalization and
\(x-\log(1+x)\le x^2\) bound this by half the sum of squared
\(\sigma^{-1}\)-scaled mean and \(\sigma^{-2}\)-scaled covariance
errors. Split the density integral over an event attaining total variation
and its complement. Convexity of \(u\log u\) bounds relative entropy
below the resulting Bernoulli relative entropy. Its second derivative in
its first argument is \(1/[a(1-a)]\ge4\), and it and its first derivative
vanish at equality; integrating twice gives \({\rm KL}\ge2{\rm TV}^2\).
Thus \({\rm TV}\le\sqrt{{\rm KL}/2}\).
The exponents in (FC.44) dominate these expressions, so the one-call TV is
at most \(\kappa\), with all positivity hypotheses included.

Make the choices once, before generating any source or metric. A passive
answer tolerance sufficient for Section 7 is
\[
a_{\rm qry}=n^{-10}/[C\beta^{6L}(1+r)].
\]
First choose a dyadic \(\sigma\) below (FC.19) and
\(a_{\rm qry}/16\), common to training and query calls. Then compute
\(z,\mathcal M,T_G\), and
\[
\xi_0=\frac{\rho_0}{2^{20}(R+1)(n+1)z^{240}},
\]
\[
\eta\le\frac{\min(\epsilon_{\rm pair},\xi_0)}{64(T_G+1)},\quad
h_s\le\eta/4,\quad
h_y\le\min\{a_{\rm qry}/64,\epsilon_{\rm pair}/64,
\xi_0/[64(b+1)]\},\quad
\epsilon_c\le\xi_0/(64z^{10}).
\tag{FC.45}
\]
Take each dyadic within a factor two below its bound. Further lower \(h_y\)
to the initialized-answer fraction of (FC.21), so its polynomial forcing
is also allocated there. Choose \(h_t,\epsilon_G\) from (FC.42), and
add
\[
\eta\epsilon_G\le
\frac{\rho_{\rm acq}\min(h_s,h_t)}{64(P+1)},\qquad
\epsilon_G\le\frac{Y\varepsilon e^{-4E_+-10}}
{2^{20}(\sqrt d+1)}.
\tag{FC.46}
\]
The first pays for literal metric replay below; the second implies (FC.24)
since the finite first-layer displacement has normalized Hilbert norm at
most \(\sqrt d\epsilon_G/Y\). All other local rank/query arithmetic
is made finer than its allocated fraction of \(a_{\rm qry}\), divided
by the explicit local polynomial caps.

Every tolerance logarithm above is at most \(CBZ\). Indeed this is a fixed
number of products/minima of (FC.14), \(A_\ast\), counts, and local
noise floors; it never multiplies precision by the number of earlier calls.
Exact empirical summation adds \(\log n\) bits. The prescribed finite
backend can therefore use
\[
w\le C\beta^{110L}Z
\tag{FC.47}
\]
bits per word, including integer ranges, coefficient scratch and counters.
This claim retains the charged activation/input interfaces of the theorem.

At complete-call boundaries maximally couple the shadow and physical raw
answers. On equality attach the same conditional augmentation and use the
same finite postprocessing. The finite tapes then agree literally until
failure. Summing (FC.44) over at most \(R\) calls costs at most
\(\rho_0/64\). Sampler failure is charged on the iid-packet marginal,
and raw-noise/source failure on the physical marginal. Before a mismatch,
both histories are identical, so these probabilities add. On the surviving
event, finite answers have form \(W_0q+\sigma\zeta+d\) with
\(\|d\|_{2,n}\le h_y\), current-operand pairs meet (FC.21), and
the strict-slack physical proof in Section 3 applies. This proves the
finite physical-source coupling without a global row-history Lipschitz
assumption and without changing the scientific Gaussian initialization.

## 6. Selected packets and literal replay at local precision

Use only the completed finite training table in the permitted offline setup.
Let \(V_\ast\in\mathbb R^{n\times s}\), \(s\le CR\), have its named
dyadic fields as columns, including the constant one. If its exact dyadic
rank is \(q\), then \(1\le q\le\min(n,s)\). Choose independent
columns \(J\) and rows \(I\) for which
\(H_I=V_\ast[I,J]\) is invertible; define
\[
C_I=V_\ast[:,J]H_I^{-1},\qquad M_I=C_I^\top C_I/n.
\tag{FC.48}
\]
Every column lies in the span of those selected columns. Restriction to
\(I\) identifies its coordinates, proving
\[
V_\ast=C_I V_\ast[I,:],\qquad C_I[I,:]=I_q,
\qquad
V_\ast^\top V_\ast/n=V_\ast[I,:]^\top M_I V_\ast[I,:].
\tag{FC.49}
\]
In particular \(M_I\succeq I_q/n\), and the constant column gives
\(\boldsymbol1^\top M_I\boldsymbol1=1\).

The selected matrix can be bounded without any subspace-gap hypothesis.
If \(|(C_I)_{ij}|>2\), replace selected row \(j\) by original row \(i\).
Multilinearity gives
\(|\det H_{I,\rm new}|=|(C_I)_{ij}|\,|\det H_I|>2|\det H_I|\).
The new row cannot duplicate a different selected row, since its coefficient
there would be zero. Repeat until every entry of \(C_I\) is at most two
in modulus. For a table with fractional precision \(b_f\) and coordinate
cap \(B_f\), a nonzero starting determinant is at least \(2^{-qb_f}\),
and Hadamard bounds every selected determinant by \(q^{q/2}B_f^q\).
There are therefore fewer than
\(q[b_f+\log_2 B_f+\tfrac12\log_2q]+1\) swaps. This is a finite exact
integer algorithm on the scaled dyadic table; its work and temporary
expanded-integer storage are charged in the word-backend lemma. At termination
\[
|(M_I)_{ij}|\le4,\qquad \|M_I\|_{\rm op}\le4q.
\tag{FC.50}
\]

To make every unsuccessful branch finite as well, cap each named field
coordinate at a fixed dyadic \(B_f\) larger than
\(8(n+1)z^{300}\), choosing a dyadic within a factor two of that bound.
The physical local bounds and the sampler event keep these guards inactive.
Off the successful range this specifies a total algorithm. Its cap logarithm
is at most \(CBZ\); finite endpoint failure flags are deterministic scalar
instructions. Rows with identical finite packet/prefix arguments always
produce identical field bits, including on failed branches.

Every operational guard is computable from the finite row fields or scalar
state: coordinate caps are rowwise; learned-matrix norm tests use (FC.20)'s
pair formula; residual norm tests use the \(m\) scalar outputs; coefficient
floors and caps use their small finite arrays. The initialized operator and
scientific source events are used only in the proof. The algorithm does not
test an unmaterialized initialized operator norm or recognize a source-good
event for free. If a finite operational guard fails, its deterministic failure
flag and dummy output follow the finite prescribed instruction schedule.

Round symmetric metric entries with error at most \(\epsilon_M\), producing
\(M_0\), and retain
\[
\widehat M=M_0+q\epsilon_MI_q.
\]
Then \(\widehat M\succeq M_I\) and
\(\|\widehat M-M_I\|_{\rm op}\le2q\epsilon_M\). For selected
operand vectors bounded by \(B_f\),
\[
|u^\top(\widehat M-M_I)v|\le2q^2B_f^2\epsilon_M.
\tag{FC.51}
\]
No inverse metric is used in training or querying.

We prove the replay claim despite the private metric depending on the entire
completed source and its noises. For a fixed real \(a\), Gaussian \(e\),
grid \(g>0\), and \(0<v\le g/2\),
\[
\Pr\{\operatorname{dist}(a+\eta e,g(\mathbb Z+1/2))\le v\}
\le2v(g^{-1}+\eta^{-1}).
\tag{FC.52}
\]
If \(f\) is the density of \(a+\eta e\), then
\(\int|f'|=2/(\eta\sqrt{2\pi})\le\eta^{-1}\). Integration of
\(f(s+kg)\le f(x)+\int_{s+kg}^{s+(k+1)g}|f'|\) over each interval,
then summation, gives \(\sum_k f(s+kg)\le g^{-1}+\eta^{-1}\).
Integrating over an interval of length \(2v\) proves (FC.52), uniformly
in \(a\). The same proof works conditionally when \(a\) is known and
the fresh \(e\) remains independent.

Fix \(\rho_{\rm acq}=2^{-12}\), let
\(g_\ast=\min(h_s,h_t)\), and set
\[
\zeta=\rho_{\rm acq}g_\ast/[64(P+1)],\qquad
\epsilon_M\le\zeta/(2q^2B_f^2).
\tag{FC.53}
\]
In setup copy the selected packets and scalar marks exactly. Compact training
replaces the empirical pair in (FC.37) by
\(u(I;C_{<a})^\top\widehat Mv(I;C_{<a})\), and uses the same finite
mark, grid and finite coefficient instructions. This bilinear form is formed
with exact dyadic products and summation, then the specified outer rounding;
an additional local arithmetic error up to \(\zeta\) would also suffice.

Condition on the entire packet array and all preceding scalar marks. The
next exact empirical mean is then fixed and the fresh raw scalar Gaussian
is independent. Since both scalar grids are at most \(\eta\), (FC.52)
with \(v=4\zeta\) bounds the chance of being within \(4\zeta\) of
this update's boundary by \(16\zeta/g_\ast\). A union over the \(P\)
updates costs less than \(\rho_{\rm acq}/4\). Condition (FC.46) and the
sampler event give simultaneous scalar-mark change at most \(\zeta\).
If compact and source prefixes agree, their selected operand bits agree.
Equations (FC.49), (FC.51), (FC.53) put the metric error below \(\zeta\).
The source and compact pre-rounding values are then within \(3\zeta\)
of the same raw Gaussian value, and lie in its same rounding cell.
Induction gives literal equality of all scalar prefixes with failure at
most \(\rho_{\rm acq}\).

This proof conditions on the packet array, not on the privately chosen metric.
It applies to any random packet array independent of the fresh scalar marks;
independence among different packets is unnecessary. Thus it also applies
after the inner short-seed replacement. It asserts equality on the realized
tape, and does not assert uniform quadrature over changed prefixes.
The selected packet coordinates, rounded metric, finite scalar-noise marks,
current scalar history and coefficient arrays occupy \(CR^2\) words.
The full field table, exact rational metric intermediates, and all future
scalar answers are discarded after offline setup. Future answers are
recomputed causally during compact training, not retained as advice.

## 7. An unseen query streams the original empirical contractions

At physical time \(t=r\tau\le rT\), take the already acquired panel
containing \(\tau\) and evaluate its finite parameter polynomial. A panel
is acquired as a whole by the causal coefficient recurrence at its left
endpoint; requests within it do not acquire the next panel. At \(\tau\ge T\)
use its frozen final state. The current first-layer increment and readout
are scalar combinations of old named fields. A hidden increment has exactly
the finite rank-list form
\[
D=T_r A_r S_r^\top/n,
\tag{FC.54}
\]
where columns of \(T_r,S_r\) are old row fields and \(A_r\) is the current
finite matrix of scalar rank weights. The subscripts here identify the
rank representation and are not the inverse-gap scalar \(r\).

For a new unit input \(v\), regenerate one row packet at a time from the
retained inner seed and evaluate the old finite field DAG at its immutable
creation-time scalar arguments. No scalar training reduction is recomputed.
The first-layer value is the dot product of its \(d\) finite initial roots
with \(v\), plus the exact finite learned increment. At a hidden layer the
learned action is computed from the actual empirical contraction
\[
c_h=S_r^\top h/n,\qquad Dh=T_rA_rc_h.
\tag{FC.55}
\]
Stream all \(n\) rows to form every entry of \(c_h\). These are exact
dyadic sums followed by allocated finite scalar rounding; no population
expectation is substituted. Similarly stream the new field's pairings with
each old forward and reverse query/answer field. Use these and the already
acquired old moments in (FC.30)–(FC.35), then perform (FC.38) using the
reserved finite innovation coordinates and scalar marks. In particular the
entire \(U\widetilde T\widehat t\) covariance correction remains.
The final readout is likewise its empirical pair with the top feature.

A constant number of passes per layer suffices: a pass obtains the new
query moments and rank contractions; a pass obtains the innovation
contractions; a pass evaluates the answer/activation and its next needed
pairs. Multiple quantities in a pass have separate exact accumulators.
Previous query fields are reevaluated rowwise at their already computed
scalar arguments. The coefficient arrays are prepared once per fixed query
context, never per regenerated row. A query uses \(CR^2\) words of scalar
history, coefficients, accumulators and row scratch, besides its seed scratch.

Each query starts its own local transcript at the current training prefix.
The reserved coordinates are reused as a deterministic function of the fixed
member seed; no query augments the retained training history, and no previous
query answer is inserted as a new matrix constraint. This gives one well-defined
finite prediction for every external code. The analysis below couples each
fixed code separately; its final simultaneous event covers adaptive choices.

For a fixed input/time code, run the iid source only through that acquired
prefix and append the passive calls just described. Do not reveal the
discarded future training answers first. Section 5's coupling applies to
this chronological source-plus-query computation with the same pre-setup
precision, because the old training moments and new query moments satisfy
the same tolerances. Refining only the new query would not justify that step.
The private selected metric is not added to the Gaussian posterior filtration.
Metric replay is used afterward to identify the actual retained prefix.

In the physical coupled process, the finite parameter state is within the
all-sphere bound from Section 3. On its operator/feature event, forward
subtraction for an additional answer/arithmetic defect of RMS at most
\(a_{\rm qry}\) gives
\[
e_j\le\beta(11e_{j-1}+Ca_{\rm qry}),
\qquad e_j=\|\widehat h^{(j)}-h^{(j)}\|_2/\sqrt n.
\tag{FC.56}
\]
The first-layer input/initial-root arithmetic has its own allocated fraction
of the same tolerance. Since \(11\beta\le\beta^{5/2}\), the geometric
sum in (FC.56) is at most \(C\beta^{3L}a_{\rm qry}\). The readout
RMS is at most \(CY\beta^{3L}(1+r)\), so the choice in Section 5 makes the
query-only prediction change at most \(CYn^{-10}\), with an absolute
total allocation after increasing the fixed constant in \(a_{\rm qry}\).
Fresh physical noise RMS failures have total probability at most
\(CL e^{-n/2}\), already included when \(R\) counts the appended calls.
For one member impose \(Re^{-n/2}\le2^{-20}\); the clean branch's stated
implementation gate is a stronger sufficient bound. The source failure at
\(2^{-20}\), this noise failure, the coupling at \(\rho_0/64\), the
sampler at \(\rho_0/512\), and metric replay at \(2^{-12}\) total less
than \(1/1024\). Thus allocating at most \(1/64\) each to the internal
dense-center and inner-generator errors still leaves the combined failure
strictly below \(1/16\). These allocations give the fixed-code one-member
physical conclusion required by the internal dense-center and short-seed
lemmas. There is no passive bias of size \(R/n\) or
\(\sqrt{R/n}\): (FC.55) has computed its exact finite empirical target.

## 8. Physical sphere/time codes, tails, and adaptive queries

The finite decoder is permitted to be discontinuous. Its input mesh uses
regularity of the physical reference alone. On the real operator/readout
event, successive forward subtraction gives
\[
|f_n(t,v)-f_n(t,v')|/Y
\le C\beta^{20L}(1+r)\|v-v'\|_2.
\tag{FC.57}
\]
The first normalized operator has bounded norm; each hidden propagation
costs at most \(11\beta\); Cauchy–Schwarz pairs the last feature difference
with readout RMS at most \(CY\beta^{3L}(1+r)\). Differentiating the
physical prediction and using (FC.2) gives
\[
|\partial_\tau f_n(r\tau,v)|/Y
\le C\beta^{20L}(1+r)
\tag{FC.58}
\]
through the finite horizon. For example the physical vector-field norm is
at most \(Y\beta^{12L}\), and prediction sensitivity at most
\(\beta^{8L}\); multiplication by \(r\) gives the stated bound.
These estimates use real states and real inputs only.

Choose an integer
\[
k_{\rm ext}=\left\lceil
\log_2[C n^{10}\beta^{20L}(1+r)(d+2)(T+2)]
\right\rceil.
\tag{FC.59}
\]
For a unit \(v\), approximate its coordinates by a lattice vector \(z\)
of step \(2^{-k_{\rm ext}-6-\lceil\log_2(d+1)\rceil}\), then use the
mathematical sphere point \(z/\|z\|_2\). The lattice approximation can
ensure \(\|z-v\|_2\le2^{-k_{\rm ext}-3}\); consequently
\(\|z\|_2\ge1/2\) and
\(\|z/\|z\|_2-v\|_2\le2^{-k_{\rm ext}-2}\).
Its code is the finite integer vector \(z\); normalization is evaluated
to the finer internal precision, with that error allocated in Section 5.
Approximate input access may choose any qualifying code; no exact rounding
tie on an arbitrary real input must be decided.

Within its current acquired panel, approximate the fractional time from
below, round down at mesh \(2^{-k_{\rm ext}}\), and clamp to \([0,1]\).
Using a certified lower approximation with error at most one mesh width
changes it by at most two mesh widths. The code and original time remain
in the same acquired panel. At a boundary either already acquired adjacent
certified panel can be used; both compare to the same physical value.
Include all panel labels and their two endpoints and one frozen-tail code.
The mesh is never enumerated or stored. Since \(\log H\le CZ\),
\[
\log N_{\rm ext}\le
C\{d[k_{\rm ext}+\log(d+2)]+k_{\rm ext}+\log(H+1)\}
\le C(d+1)Z.
\tag{FC.60}
\]
Equations (FC.57)–(FC.59) make the physical input/time rounding error a
fixed fraction of \(Yn^{-10}\). Beyond \(T\), compare to the physical
prediction at \(T\), adding the fitting tail
\(CYH_D^2r e^{-T/2}\le Yn^{-10}/4\). This proves the same scope at
\(t=\infty\).

The internal dense-center lemma and Section 7 therefore give, for each
fixed code, a one-member bad-output probability at most \(1/16\), after
the fixed source/coupling/replay/generator allocations. The internal
whole-member amplification lemma makes all coded median outputs accurate
simultaneously with the specified confidence. To transfer to an arbitrary
query, compare its returned coded value with the physical value at that
code, then use (FC.57)–(FC.59) and the tail. No continuity estimate for
the finite decoder is used. Because this is one event for every code,
queries may be chosen after inspecting the retained model and previous
answers. Their dependence creates no new union bound or posterior premise.

The resulting comparison with the independent dense reference is
\(2B_n+A_{\rm num}Yn^{-10}\), with \(A_{\rm num}\) an absolute
allocated constant. Its explicit mesh coefficient gives \(B_n\ge32Y/n\),
so the stated numerical gate absorbs the remainder into \(3B_n\).
The centers and source events used in this argument are proof objects;
the retained model never receives them or any unknown test label.

## 9. Small positive labels and scope of the finite interfaces

For completeness the separate branch \(0<nY<1\) has the following explicit
recipe. Put \(Z_Y=Z+\log(1/(nY))\). Keep the same physical horizon
and source domain, replace the panel count by
\(H=\lceil T/h_0\rceil+\lceil BZ_Y\rceil\), and then compute (FC.13)
with this \(H\), adding \(\lceil\log_2(1/(nY))\rceil\) to its Taylor
degree. Choose \(J_a,\delta_\dagger\) and every subsequent tolerance
from the actual \(Y,S\) by the same formulas. There is no circular choice:
\(Z_Y,H,K,J_a,R\) are fixed in that order before the pair and sampler
precisions. The extra degree makes \(J_a=O(K)\) valid even when
\(\delta_0\) is tiny, and the extra panels ensure \(K\le CH\).
All short-complex-panel estimates improve as the step shrinks.

Here \(\log(1/Y)=\log n+\log(1/(nY))\le CZ_Y\). Therefore every
precision estimate above holds with \(Z_Y\), and
\[
R_Y\le Cp\beta^{201L}(m+d+2)(1+r)Z_Y^{5/2},\qquad
w_Y\le C\beta^{110L}Z_Y.
\tag{FC.61}
\]
The source-event width has no new lower label condition. The finite
implementation must additionally keep the explicitly enlarged Gaussian-RMS
gate
\[
R_Ye^{-n/2}\le2^{-20},
\quad\text{equivalently}\quad n\ge2\log(2^{20}R_Y),
\tag{FC.62}
\]
where \(R_Y\) is the constructed integer field/call count. This is a
finite numerical gate, not an unquantified stochastic threshold. Using the
right side of (FC.61) as a deterministic certificate gives a directly
checkable sufficient version. The finite row-root cutoff and code count are
recomputed with these orders. Replacing only the word precision would have
missed the activation interpolation orders and the raw-noise union. All
claimed numerical storage/work envelopes use \(Z_Y\) in this branch;
the displayed clean headline remains its \(nY\ge1\) branch.

### Interfaces and provenance

Equations (FC.25)–(FC.26) define the actual field/call recipe and establish
the claimed parameter dependence. Equations (FC.13), (FC.18), (FC.21),
(FC.36), (FC.42), (FC.45)–(FC.46), and (FC.53) define one shared finite
precision schedule before setup; their logarithms give (FC.47). The selected
metric has at most \(R\) selected packets, all empirical communication is
through \(CR^2\) scalar words, and its exact replay is on the finite tape
it actually acquired. New queries regenerate the original finite rows and
use all two-orientation covariance terms. These are the interfaces required
by the separate internal word-backend and short-seed lemmas; no additional
scientific hypothesis or undeclared history sensitivity is needed here.

For the short-seed interface the entire scalar transcript has
\(O(R^2w)\) bits. This count includes acquired pairs, shared scalar branch
outputs consumed by later field definitions, and the final row coefficient
vector at each field's creation. Row-local branches and internal spectral
pivots or CDF bisection decisions are deterministic computations from the
packet and candidate scalar inputs, and are recomputed rather than retained
as transcript entries.
A matrix call does not retain its whole correction matrix forever: after
\(\widehat t\) is acquired it multiplies \(\widetilde T\widehat t\),
combines that vector with the mean coefficients, retains at most \(CR\)
coefficients for its new affine row field, and discards the \(R\)-square
temporary matrices. There are \(CR\) field creations, so these vectors
occupy \(CR^2\) words. The temporary spectral/Sylvester matrices are
recomputed or discarded during fixed-context coefficient preparation.

For a candidate-transcript verifier, all creation-time scalar arguments and
these coefficient vectors are hardwired proof data. One pass through the
packets accumulates at most \(CR^2\) exact dyadic sums. Each accumulator
needs only a constant multiple of \(w\) bits, since its products have
bounded arity and \(\log n\) is included in \(w\). After the stream,
the verifier checks every scalar rounding instruction and coefficient-vector
consistency in chronological order from those sums, reusing \(CR^2\) words
of small-matrix scratch. It need not retain each earlier spectral matrix.
Induction then identifies a passing candidate with the actual transcript.
Thus both transcript length and between-packet verifier state are
\(O(R^2w)\), not \(O(R^3w)\). At an intermediate training time only
the already acquired coefficient vectors are retained; the future vectors
used in offline selection have been discarded with the future-answer table.

Initialization remains offline: its selected metric may depend on the entire
virtual finite training trajectory. Its full source table is temporary.
The retained state contains seeds, selected finite packets, the rounded
metric, scalar-noise marks, current acquired history and finite instructions.
It contains no dense hidden matrix, full row table or future-answer table.
Training is causal scalar acquisition. Querying does not advance training.
The numerical finite source approximates dense gradient flow; it is not
asserted itself to fit exactly. The comparison remains to an independent
dense reference over the whole sphere, all physical times and the fitted
endpoint. The analytic upper certificate remains an absolute guarantee.
The same finite construction also supports the intrinsic-quantile
comparison proved below, with the original numerical remainder.

Scientific inputs actually read: the integrated decoder statements and
proof interfaces and quantitative fitting section; the authorized decoder
notes SOURCE_SEED_EXACT_QUERY, FAST_FINITE_SOURCE_BRIDGE,
FAST_LOCAL_PRECISION_TEST, FAST_PHYSICAL_QUERY_GRID,
NOISY_TWO_ORIENTATION_TRANSCRIPT, SANE_DECODER_CORE, SANE_METRIC_PACKETS,
FAST_LOCAL_COMPOSITION, GAP_REFINED_PHASE_COSTS; and their directly needed
physical method dependencies GAP_DEGREE_REFINEMENT,
PHYSICAL_PARAMETER_ACCOUNTING, FAST_TAYLOR_NOISE, FAST_SCALAR_FORCING,
FAST_LOCAL_KERNEL_AUDIT, SANE_TAYLOR_SOURCE and SANE_ADAPTIVE_TIME.
Their older conditional status statements and audit verdicts are not used
as premises. The source author supplied the source-event interface recorded
in Section 1; source probability is proved in the integrated IC lemma.
The canonical-notation skill, its neural reference and the rigorous-math
skill were read and applied. No experiments, outside-study inputs, Git
mutations, maintained-book edits, or edits to other authors' files were made.
