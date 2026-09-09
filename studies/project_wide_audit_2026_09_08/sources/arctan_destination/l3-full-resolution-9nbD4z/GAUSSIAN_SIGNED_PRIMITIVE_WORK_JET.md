# The first Gaussian signed primitive-work coefficient is positive

Candidate pending independent audit. This note computes a genuinely
Gaussian-initialized signed response quantity, averaged over every
top-matrix column probe. It does not use a localized deterministic
configuration or replace the response covariance by an isotropic one.
The theorem in this version uses exactly zero initial readout, with
the prescribed independent Gaussian hidden initialization. Transfer
of this finite jet to the prescribed tiny readout is a separate
obligation, not assumed here.

The result is an initial Taylor coefficient at finite width, followed
by its width limit. No uniform Taylor remainder, positive-time sign
after taking width to infinity, response-amplitude bound, or population
continuation is claimed.

## Quantity and conclusion

Use the canonical uncut feature equations and all three hidden layers.
For each middle-layer column index \(i\), perturb the initial
\(W^{(3)}\) in direction \(\xi e_i^T/\sqrt n\), where \(\xi\) is
standard Gaussian and independent of the trained trajectory. Let
\(\zeta_i(s)\) be the resulting variation of \(z^{(2)}(s)\), and set
\[
a_i(s)=\int_0^s \operatorname{variation}_i\delta^{(2)}(u)\,du,\qquad
c_i(s)=\operatorname{diag}(\phi'(z^{(2)}(s)))^{-1}a_i(s).
\]
These are actual linear responses with all trained parameters varied.
The inverse is finite at every finite state. The following scalar
functions will recur:
\[
\psi(x)=\phi(x)\phi'(x),\qquad
\psi'(x)=\phi'(x)^2+\phi(x)\phi''(x),\qquad
\beta(x)=\frac{\phi''(x)}{\phi'(x)}
       =-\frac{2x}{1+x^2}.
\]
The split-free primitive identity in
ACTUAL_PRIMITIVE_OFFDIAGONAL_PAIR.md identifies the full signed work
(ordinary bounded forcing excluded) as
\[
\mathscr W_n(s)=\frac1n\sum_{i=1}^n\mathbb E_\xi
\left[c_i(s)^T\operatorname{diag}(\beta(z^{(2)}(s)))
\left(q^{(2)}(s)\odot\zeta_i(s)
 -(z^{(2)})'(s)\odot c_i(s)\right)\right].
\tag{1}
\]
The expectation conditions on the whole actual trajectory and averages
only the auxiliary probe. The summation over \(i\) is part of the
quantity, not a choice of a favorable column.

With zero initial readout,
\[
\mathscr W_n(s)=J_n s^5+O_n(s^6).
\tag{2}
\]
Every expectation below other than \(\mathbb E_\xi\) concerns the
independent Gaussian initialization. For \(n\ge2\),
\[
\mathbb E J_n>0,\qquad
J_n\longrightarrow J_*>0\ \hbox{in probability and in }L^1.
\tag{3}
\]
At \(n=1\), \(J_n=0\). Here is an explicit formula for the limit.
For a standard scalar Gaussian \(G\), define
\[
\mu_1=\mathbb E\phi(G)^2,\quad
\mu_2=\mathbb E\phi(\sqrt{\mu_1}G)^2,\quad
b_1=\mathbb E[\phi(G)^2\phi'(G)^2].
\]
For \(v>0\), with \(Z_v=\sqrt v G\), put
\[
A(v)=\mathbb E\psi(Z_v)^2+
                     v\mathbb E\psi'(Z_v)^2,\qquad
\gamma(v)=\frac{\mathbb E[Z_v\psi(Z_v)]}{v},\qquad
\chi(v)=\mathbb E[\psi'(Z_v)\psi(Z_v)^2].
\]
All are finite, and \(A(v),\gamma(v),\chi(v)>0\). The last sign follows
from Gaussian integration by parts:
\[
3\chi(v)=\frac1v\mathbb E[Z_v\psi(Z_v)^3]>0.
\tag{4}
\]
The functions have bounded continuous derivatives where needed on any
compact positive variance interval. Finally, for \(Z=\sqrt{\mu_1}G\),
\[
J_*=-\frac{A(\mu_2)\gamma(\mu_2)b_1}{4\mu_1^2}
           \mathbb E[Z\beta(Z)]\,\mathbb E[Z\psi(Z)].
\tag{5}
\]
The first last-factor expectation is strictly negative and the second
strictly positive. Also \(\mu_1,\mu_2,b_1>0\); thus (5) is strictly
positive without numerical evaluation of an integral.

## Finite-width jet with every trained factor

In this section all undecorated fields are evaluated at initialization.
Write
\[
D_2=\operatorname{diag}(\phi'(z^{(2)})),\quad
K=W^{(2)}\operatorname{diag}(\phi'(z^{(1)})^2)(W^{(2)})^T,\quad
m_1=\|h^{(1)}\|_2^2/n,\quad m=\|h^{(2)}\|_2^2/n.
\]
With readout zero, every hidden parameter velocity is zero at \(s=0\),
while \((W^{(4)})'(0)=h^{(3)}\). Therefore
\[
(q^{(2)})'(0)=v^{(2)}:=(W^{(3)})^T\psi(z^{(3)}),\quad
(\delta^{(2)})'(0)=D_2v^{(2)},\quad
((z^{(2)})')'(0)=(m_1I+K)D_2v^{(2)}.
\tag{6}
\]
Thus \(v^{(2)}\) denotes only the initial feature-time slope of
the middle backward query.

At initialization the lower state and \(z^{(2)}\) have zero variation
under a top-column probe. Differentiating the first formula in (6)
with respect to that initial column gives
\[
R_i=e_i\psi(z^{(3)})^T+
h^{(2)}_i(W^{(3)})^T\operatorname{diag}(\psi'(z^{(3)})),\qquad
\operatorname{variation}_i(q^{(2)})'(0)=R_i\xi/\sqrt n.
\]
Thus
\[
c_i(s)=\frac{s^2}{2\sqrt n}R_i\xi+O_n(s^3),\qquad
\zeta_i(s)=\frac{s^2}{2\sqrt n}(m_1I+K)D_2R_i\xi+O_n(s^3).
\tag{7}
\]
For the second expansion, differentiate the actual first-layer and
second-matrix velocities: the first-layer variation contributes
\(K D_2R_i\xi\), and the trained second-matrix variation contributes
\(m_1D_2R_i\xi\), both with \(s^2/(2\sqrt n)\).
The same result follows from the complete primitive representation,
whose retained memory has no term of order \(s^2\).
Top-matrix training and readout variation are already present in
the time derivative and in both terms of \(R_i\); they are not frozen.

For a vector \(q\) define the linear matrix expression
\[
\mathcal M(q)=\operatorname{diag}(\beta(z^{(2)})\odot q)K D_2
       -\operatorname{diag}(\beta(z^{(2)})\odot K D_2q).
\]
Substitute (6)--(7) into (1). The two \(m_1I\) terms cancel exactly,
giving
\[
J_n=\frac1{4n^2}\operatorname{Tr}\!\left[
                  \mathcal M(v^{(2)})\sum_iR_iR_i^T\right].
\tag{8}
\]
The remainders in (2) and (7) are at fixed \(n\) and fixed finite
initial state. Smooth finite-dimensional ODE dependence supplies
these derivatives; all probe responses are linear in a finite Gaussian
vector, so probe averaging of their coefficients is legitimate.

Set
\[
d=\psi(z^{(3)}),\quad E=\operatorname{diag}(\psi'(z^{(3)})),\quad
\ell=(W^{(3)})^TEd,\qquad C=\sum_iR_iR_i^T.
\]
Ordinary matrix multiplication gives the complete column-averaged
covariance numerator
\[
C=\|d\|_2^2I+h^{(2)}\ell^T+\ell(h^{(2)})^T
                      +nm(W^{(3)})^TE^2W^{(3)}.
\tag{9}
\]
Both cross terms are essential in the following exact conditioning.

## Exact top-matrix conditioning, without independent-coordinate claims

Condition on the whole lower initialization and on \(z^{(3)}\). Since
\(m>0\) almost surely, the conditional matrix law is
\[
W^{(3)}=\frac{z^{(3)}(h^{(2)})^T}{nm}
                  +\frac1{\sqrt n}X P,\qquad
P=I-\frac{h^{(2)}(h^{(2)})^T}{nm},
\tag{10}
\]
where \(X\) has independent standard Gaussian entries. Before this
conditioning the \(z^{(3)}_j\), given the lower initialization, are
independent \(N(0,m)\). The reused outputs in (9) are not asserted
independent.

Use bars for the following empirical scalar averages over the top layer:
\[
\bar v=\|d\|^2/n,\quad \bar\tau=\operatorname{Tr}(E^2)/n,\quad
\bar\gamma=(z^{(3)})^Td/(nm),\quad
\bar A=\bar v+m\bar\tau,
\]
\[
\bar\lambda=\frac1n\sum_j
 [\,\psi'(z^{(3)}_j)\psi(z^{(3)}_j)^2+
 z^{(3)}_j\psi'(z^{(3)}_j)^2\psi(z^{(3)}_j)\,].
\]
For one scalar \(\bar\kappa\), whose value cancels below, (9)--(10)
give
\[
\mathbb E_X C=n\bar A I+
                  \bar\kappa h^{(2)}(h^{(2)})^T,\qquad
\mathbb E_X v^{(2)}=\bar\gamma h^{(2)},
\tag{11}
\]
\[
\mathbb E_X[(v^{(2)}_j-\bar\gamma h^{(2)}_j)C_{kl}]
=\bar\lambda\,[h^{(2)}_kP_{jl}+P_{jk}h^{(2)}_l].
\tag{12}
\]
To verify (12), the centered part of \(v^{(2)}\) is
\(P X^Td/\sqrt n\). Its covariance with the centered part of \(\ell\)
is \(P\,n^{-1}\sum_j\psi'(z^{(3)}_j)\psi(z^{(3)}_j)^2\).
The linear part of \(nm(W^{(3)})^TE^2W^{(3)}\) has the form
\(h^{(2)}u^T+u(h^{(2)})^T\), where
\(u=PX^TE^2z^{(3)}/\sqrt n\); its covariance with the centered
query supplies the second summand of \(\bar\lambda\).
The remaining product is odd of degree three in \(X\) and has mean
zero. For (11), one may compute
\[
\bar\kappa=
\frac{2(z^{(3)})^TEd}{nm}
+\frac{(z^{(3)})^TE^2z^{(3)}}{nm}-\bar\tau.
\]

Define the off-diagonal lower contraction
\[
S_n=\sum_{j,k}\beta(z^{(2)}_j)K_{jk}\phi'(z^{(2)}_k)
            [h^{(2)}_k-h^{(2)}_j\mathbf1_{j=k}].
\tag{13}
\]
Expanding the trace in (8), its \(j,k\) summand contains
\(\mathbb E_X[v^{(2)}_jC_{kj}-v^{(2)}_kC_{jj}]\).
The \(\bar\kappa\) terms cancel. The covariance terms simplify because
\[
h^{(2)}_kP_{jj}-h^{(2)}_jP_{jk}
=h^{(2)}_k-h^{(2)}_j\mathbf1_{j=k}.
\]
Consequently
\[
\mathbb E_X J_n
   =\frac{\bar\lambda-n\bar A\bar\gamma}{4n^2}S_n.
\tag{14}
\]
Now average over the independent top preactivations, still conditional
on the whole lower initialization. The empirical-product bias matters:
\[
\mathbb E[\bar\lambda-n\bar A\bar\gamma\mid\text{lower}]
=-(n-1)A(m)\gamma(m)-2\chi(m).
\tag{15}
\]
Indeed \(n\mathbb E[\bar A\bar\gamma]
=(n-1)A\gamma+v^{-1}\mathbb E[(\psi(Z_v)^2+
v\psi'(Z_v)^2)Z_v\psi(Z_v)]\), at \(v=m\).
Subtracting this from \(\mathbb E\bar\lambda\) cancels the
\(\psi'^2 Z_v\psi\) terms, and (4) gives the remaining \(-2\chi\).

## Lower-matrix conditioning determines the Gaussian sign

Condition now on \(z^{(1)}\) and \(z^{(2)}\). Put
\[
b_{1,n}=\frac1n\sum_r(h^{(1)}_r)^2\phi'(z^{(1)}_r)^2.
\]
The analogue of (10) for \(W^{(2)}\), with
\(P_1=I-h^{(1)}(h^{(1)})^T/(nm_1)\), shows for \(j\ne k\) that
\[
\mathbb E[K_{jk}\mid z^{(1)},z^{(2)}]
=\frac{b_{1,n}}{nm_1^2}z^{(2)}_jz^{(2)}_k.
\]
The diagonal of (13) is zero exactly. Since \(m\) depends only on
\(z^{(2)}\), (14)--(15) therefore give the exact finite-width identity
\[
\mathbb E[J_n\mid z^{(1)},z^{(2)}]
=-\frac{[(n-1)A(m)\gamma(m)+2\chi(m)]b_{1,n}}
             {4n^3m_1^2}
\sum_{j\ne k}
 [z^{(2)}_j\beta(z^{(2)}_j)]
 [z^{(2)}_k\psi(z^{(2)}_k)].
\tag{16}
\]
All factors preceding the sum, except its explicit minus sign, are
strictly positive almost surely. Each summand is strictly negative
almost surely. This proves the strict expectation sign for \(n\ge2\).
It is not a pointwise sign assertion for each initialized matrix.

## Concentration of the coefficient and its explicit limit

For completeness, the conditional averages just used also identify
the actual random coefficient, not merely its expectation.
The Gaussian Poincare inequality used below is
\(\operatorname{Var}F(X)\le\mathbb E\|\nabla_XF(X)\|^2\)
for independent standard Gaussian entries and a differentiable
function with square-integrable gradient. One proof uses the Gaussian
semigroup \(P_tF(x)=\mathbb E F(e^{-t}x+\sqrt{1-e^{-2t}}G)\):
Gaussian integration by parts gives
\(-\frac d{dt}\mathbb E(P_tF)^2=2\mathbb E\|\nabla P_tF\|^2\);
also \(\nabla P_tF=e^{-t}P_t\nabla F\).
Integrating, using Jensen, and letting \(t\to\infty\) proves the
inequality for smooth bounded functions. Cutoff approximation in the
Gaussian Sobolev norm gives the stated polynomial-growth case used
here. Conditional residuals in (10) are polynomial in \(X\).

Let \(\bar C=C/n\). Conditional on the lower fields and \(z^{(3)}\),
the functions \(\psi,\psi'\) have deterministic bounds and
\(\|h^{(2)}\|/\sqrt n\le\pi/2\). For a Frobenius-unit variation of
the standard residual matrix \(X\), direct differentiation of (9)--(10)
gives
\[
\|\delta v^{(2)}\|_2\le C,\quad
\|\bar C\|_{\rm op}\le C(1+\|W^{(3)}\|_{\rm op}^2),\quad
\|\delta\bar C\|_{\rm F}
\le \frac{C(1+\|W^{(3)}\|_{\rm op})}{\sqrt n},
\]
\[
\|\mathcal M(v^{(2)})\|_{\rm F}
\le C\|K\|_{\rm op}\|v^{(2)}\|_2,\qquad
\|v^{(2)}\|_2\le C\sqrt n\|W^{(3)}\|_{\rm op}.
\]
Moreover, expanding the two diagonal traces as in (13) gives
\[
|\operatorname{Tr}[\mathcal M(\delta v^{(2)})\bar C]|
\le 2\sqrt n\,\|K\|_{\rm op}\|\bar C\|_{\rm op}
                       \|\delta v^{(2)}\|_2.
\]
Hence (8) implies the gradient estimate
\[
\|\nabla_X J_n\|_{\rm F}
\le \frac{C\|K\|_{\rm op}(1+\|W^{(3)}\|_{\rm op}^2)}{\sqrt n}.
\tag{17}
\]
Gaussian matrices of variance \(1/n\) have uniformly bounded fixed
operator-norm moments: a pair of \(1/4\)-nets has size at most \(9^{2n}\),
and their bilinear forms are \(N(0,1/n)\), giving
\(\Pr(\|W\|_{\rm op}>x)\le2\,9^{2n}e^{-nx^2/8}\);
integration above a fixed sufficiently large \(x\) proves the moment
bound. Also \(\|K\|_{\rm op}\le\|W^{(2)}\|_{\rm op}^2\).
Average conditional Poincare using (17), then the original independent
Gaussian matrix laws. It follows that
\[
J_n-\mathbb E_X[J_n\mid\text{lower},z^{(3)}]\to0
\quad\hbox{in }L^2.
\tag{18}
\]

The conditional scalar law \(z^{(3)}_j=\sqrt m\,G_j\) and finite
Gaussian moments give
\(\bar A\to A(m)\), \(\bar\gamma\to\gamma(m)\), and
\(\bar\lambda/n\to0\) in probability whenever \(m\) stays in a
compact positive interval. Conditional variance estimates are uniform
on such an interval. The initialization laws give \(m\to\mu_2>0\),
so restricting to that interval loses probability tending to zero.
Also \(|S_n|/n\le C\|K\|_{\rm op}\). Thus (14), (18) yield
\[
J_n=-\frac{A(m)\gamma(m)}4\,\frac{S_n}{n}+o_{\mathbb P}(1).
\tag{19}
\]

Condition on \(z^{(1)},z^{(2)}\) and differentiate \(S_n/n\) with
respect to the standard residual matrix in \(W^{(2)}\). Writing
\(S_n=\beta(z^{(2)})^TK\psi(z^{(2)})
-\sum_j\beta(z^{(2)}_j)\psi(z^{(2)}_j)K_{jj}\),
the two bilinear derivatives have gradient norm at most
\(C\|W^{(2)}\|_{\rm op}/\sqrt n\); the diagonal trace derivative
is at most \(C\|W^{(2)}\|_{\rm F}/(n\sqrt n)\).
Here \(\phi'(z^{(1)})^2\le1\), and both \(\beta,\psi\) are bounded.
The same Poincare argument gives
\[
\frac{S_n}{n}-
\frac{b_{1,n}}{n^2m_1^2}\sum_{j\ne k}
[z^{(2)}_j\beta(z^{(2)}_j)]
[z^{(2)}_k\psi(z^{(2)}_k)]
\longrightarrow0\quad\hbox{in }L^2.
\tag{20}
\]
The first-layer law of large numbers gives \(m_1\to\mu_1\) and
\(b_{1,n}\to b_1\). Conditional on that layer, the \(z^{(2)}_j\)
are independent \(N(0,m_1)\). Conditional averaging, with uniformly
bounded Gaussian moments on \(m_1\le(\pi/2)^2\), gives the two limits
of the means in (20). The removed diagonal divided by \(n^2\) tends
to zero in probability. Consequently
\[
\frac{S_n}{n}\to
\frac{b_1}{\mu_1^2}\mathbb E[Z\beta(Z)]\mathbb E[Z\psi(Z)].
\]
Combining with (19) proves (5) in probability.
Finally, (8)--(9) give the deterministic bound
\[
|J_n|\le C\|W^{(2)}\|_{\rm op}^2
\|W^{(3)}\|_{\rm op}(1+\|W^{(3)}\|_{\rm op}^2).
\]
The Gaussian operator moments already proved make this uniformly
square integrable. Therefore the convergence is also in \(L^1\).
No independent-coordinate claim after matrix reuse is used: two exact
conditional matrix laws and concentration of empirical contractions
supply the joint calculation.

## Consequence and exact limitation

The zero-readout Gaussian coefficient is not merely nonzero: it is
strictly positive in its deterministic width limit and with probability
tending to one at large width. Thus an exact Gaussian-average
nonpositivity or cancellation of this signed primitive work cannot be
justified by the indicated initial-jet algebra.

This does not refute an upper Gronwall bound with a positive constant,
nor cancellation with the separately retained ordinary source, nor a
different time-integrated signed energy. It also does not give a
positive-time limiting sign without a uniform remainder. The full
canonical global theorem remains open. Until a separate proof transfers
this jet to the prescribed tiny readout, (3) is explicitly a
zero-readout proxy result, not a change to the initialization contract.

Explicit mathematical dependencies:
ACTUAL_BACKPROP_PRIMITIVE_RESPONSE.md for the exact primitive and
retained response; ACTUAL_PRIMITIVE_OFFDIAGONAL_PAIR.md for its
split-free signed work; ACTUAL_LOG_GATE_COVARIANCE_COMMUTATOR.md
for the independently rederived initial probe formula.
