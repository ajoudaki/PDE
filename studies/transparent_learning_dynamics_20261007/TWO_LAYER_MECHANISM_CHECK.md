# Two nonlinear hidden layers: checked initial feature acceleration

Status: internally checked finite-initial-program identities, 2026-10-07. The proposed first-layer acceleration and isolated learned-middle-matrix contribution are correct. The total second-layer acceleration includes the additional first-layer-motion term derived below.

Scientific inputs: the supervisor's canonical two-hidden-layer example and this author's complete CAUSAL_GAUSSIAN_ROUTE.md and RESPONSE_GAUSSIAN_CLOSURE.md. No other route, integrated study, other study, book, literature, experiment, or Git history was consulted. Required research, proof and canonical-notation skills are reused. No positive-time width limit, interchange of differentiation with such a limit, or continuous-time error rate is asserted.

## 1. Exact model, clock, and meaning of a limiting derivative

There are two training inputs and one passive input:
\[
v_1=e_1,\qquad v_2=e_2,\qquad
v_3=\frac{2e_1+e_2}{\sqrt5},\qquad
S=(v_a^\top v_b)_{a,b\le3}
=\begin{pmatrix}
1&0&2/\sqrt5\\
0&1&1/\sqrt5\\
2/\sqrt5&1/\sqrt5&1
\end{pmatrix}.
\]
Only \(y_1,y_2\) are supplied. There is no label or training residual for sample 3. Put
\[
T(x)=\tanh x,\qquad g(x)=T'(x)=\operatorname{sech}^2x,
\qquad T''(x)=-2T(x)g(x).
\]
At width \(n\),
\[
z_{1,a}=Av_a,\quad h_{1,a}=T(z_{1,a}),\quad
z_{2,a}=Wh_{1,a},\quad h_{2,a}=T(z_{2,a}),\quad
f_a=\frac1n w^\top h_{2,a}.
\]
Initially \(A\) has independent \(N(0,1)\) entries, \(G=W(0)\) has independent \(N(0,1/n)\) entries independently of \(A\), and \(w(0)=0\). Define
\[
c_b=y_b-f_b\quad(b=1,2),\qquad
\delta_{2,a}=w\odot g(z_{2,a}),\qquad
b_{1,a}=W^\top\delta_{2,a},\qquad
\delta_{1,a}=g(z_{1,a})\odot b_{1,a}.
\]
Since \(m=2\), the physical factor \(2/m\) is exactly one. The prescribed flow is
\[
\dot A=\sum_{b=1}^2c_b\delta_{1,b}v_b^\top,\qquad
\dot W=\frac1n\sum_{b=1}^2c_b\delta_{2,b}h_{1,b}^\top,\qquad
\dot w=\sum_{b=1}^2c_bh_{2,b}. \tag{1}
\]

Let
\[
C_{\ell,ab}^{(n)}(t)=\frac1n h_{\ell,a}(t)^\top h_{\ell,b}(t)
\]
be the same-time feature Gram. Every finite-width derivative at \(t=0\) below follows by differentiating (1), a smooth finite-dimensional ODE. We use the shorthand
\[
\mathcal A_{\ell,ab}
=\lim_{n\to\infty}^{\mathbb P}
\left.\frac{d^2}{dt^2}C_{\ell,ab}^{(n)}(t)\right|_{t=0}. \tag{2}
\]
The calculations prove that these limits exist for the entries claimed. An expression informally written as \(C_{\ell,ab}''(0)\) refers here to (2), not to differentiating an unproved limiting positive-time flow. Field derivatives below likewise mean their limiting initial row laws.

No smallness of \(y_1,y_2\) is needed for these local identities; in particular they hold throughout any supplied fixed small-label class, including zero or opposite-sign labels.

## 2. Initial scalar laws and the first nonzero return

In the first population, take
\[
X_1,X_2\ \hbox{independent }N(0,1),\qquad
X_3=\frac{2X_1+X_2}{\sqrt5},\qquad H_a=T(X_a),
\]
and define
\[
\sigma^2=\mathbb E[T(X)^2]>0,\qquad
q_X=\mathbb E[g(X)^2]>0,\qquad X\sim N(0,1). \tag{3}
\]
The initial training feature Gram is \(\sigma^2 I_2\). Therefore, in the second population,
\[
Z_1,Z_2\ \hbox{are independent }N(0,\sigma^2).
\]
The readout derivative and the reverse-query inputs are
\[
Q=y_1T(Z_1)+y_2T(Z_2),\qquad
\dot w(0)\ \leadsto\ Q,\qquad
d_a(Z)=g(Z_a)Q\quad(a=1,2). \tag{4}
\]
Here \(\leadsto\) denotes convergence of the relevant empirical row law and the moments used below. It does not identify neuron indices between the two populations.

At \(t=0\), all hidden parameter and feature velocities vanish. Consequently
\[
\dot\delta_{2,a}(0)=g(z_{2,a}(0))\odot\dot w(0),\qquad
\dot b_{1,a}(0)=G^\top\dot\delta_{2,a}(0). \tag{5}
\]
The term \(\dot W^\top\delta_{2,a}\) vanishes at zero; no term has been dropped at a nonzero time.

The joint first-return law is
\[
\boxed{
\dot b_{1,a}(0)\ \leadsto\
B_a:=\zeta_a+\sum_{b=1}^2 H_b R_{ab},\qquad
R_{ab}=\mathbb E[\partial_b d_a(Z)],
} \tag{6}
\]
where \((\zeta_1,\zeta_2)\) is centered Gaussian independent of \((X_1,X_2)\), with
\[
\boxed{\mathbb E[\zeta_a\zeta_b]=\mathbb E[d_a(Z)d_b(Z)].} \tag{7}
\]
It is therefore independent of \(X_3\) as well. The Gaussian covariance in (7) is the raw second-moment matrix of the reverse inputs. One must not subtract the covariance of the reaction term \(HR^\top\) from it.

For an explicit coefficient calculation, let a scalar \(Z\sim N(0,\sigma^2)\), and put
\[
\alpha=\mathbb E[g(Z)],\qquad
\beta=\mathbb E[g(Z)^2],\qquad
\nu=\mathbb E[T(Z)^2]=1-\alpha,\qquad
r_0=\mathbb E[g(Z)^2+T(Z)T''(Z)]=3\beta-2\alpha. \tag{8}
\]
Differentiating \(d_a=g(Z_a)\sum_c y_cT(Z_c)\) gives
\[
R_{ab}=y_b\mathbb E[g(Z_a)g(Z_b)]
 +\mathbf1_{\{a=b\}}\mathbb E[Q T''(Z_a)].
\]
Independence and oddness of \(T\) imply
\[
\boxed{
R=\begin{pmatrix}
y_1r_0&y_2\alpha^2\\
y_1\alpha^2&y_2r_0
\end{pmatrix}.} \tag{9}
\]
Thus the proposed diagonal term
\(y_a\mathbb E[\operatorname{sech}^4Z+\tanh Z\,\tanh''Z]\)
and off-diagonal term \(y_b(\mathbb E\operatorname{sech}^2Z)^2\) are both correct. The reaction has a plus sign in (6). Although the \(T T''\) part is nonpositive, its complete diagonal coefficient satisfies
\[
r_0
=\mathbb E[(Tg)'(Z)]
=\frac1{\sigma^2}\mathbb E[Z T(Z)g(Z)]>0, \tag{10}
\]
by Gaussian integration by parts. Its sign therefore follows the corresponding label.

For completeness, (7) becomes
\[
\begin{aligned}
\mathbb E\zeta_1^2
&=y_1^2\mathbb E[g(Z)^2T(Z)^2]+y_2^2\beta\nu,\\
\mathbb E\zeta_2^2
&=y_2^2\mathbb E[g(Z)^2T(Z)^2]+y_1^2\beta\nu,\\
\mathbb E[\zeta_1\zeta_2]
&=(y_1^2+y_2^2)\alpha\,\mathbb E[g(Z)T(Z)^2].
\end{aligned} \tag{11}
\]
In particular, independence of \(Z_1,Z_2\) does not make the two Gaussian returns independent. The last covariance is positive whenever at least one label is nonzero. The total covariance of \(B=(B_1,B_2)\) is
\[
\operatorname{Cov}(B)
=\operatorname{Cov}(\zeta)+\sigma^2RR^\top,
\]
because the Gaussian innovation and the first-population features are independent and centered.

### Direct justification of the joint return law

Let \(H\in\mathbb R^{n\times2}\) collect the initial training features, \(Z=GH\), and \(\Gamma_n=H^\top H/n\). Then \(\Gamma_n\to\sigma^2 I_2\) in probability. Conditioned on \(H\), the rows of \(Z\) are independent \(N(0,\Gamma_n)\).

For any fixed collection of bounded smooth upper-row functions, let \(D\) collect their evaluations on \(Z\). On the event that \(\Gamma_n\) is invertible, the exact Gaussian conditional law gives
\[
G^\top D
\stackrel{\mathrm{law}}=H\Gamma_n^{-1}\frac{Z^\top D}{n}
 +(I-P_H)N,\qquad
P_H=H(H^\top H)^{-1}H^\top, \tag{12}
\]
where, conditionally on \(H,Z\), the rows of \(N\) are independent centered Gaussian vectors with covariance \(D^\top D/n\). The normalized squared Frobenius norm of \(P_HN\) has conditional mean
\[
\frac{\operatorname{rank}H}{n}\operatorname{tr}(D^\top D/n)\longrightarrow0.
\]
Conditional laws of large numbers and continuity in \(\Gamma_n\) identify the deterministic coefficients. Gaussian integration by parts gives
\[
\frac1{\sigma^2}\mathbb E[Z_bD_j(Z)]
=\mathbb E[\partial_bD_j(Z)]\qquad(b=1,2).
\]
This proves (6)–(7), jointly for any such finite collection of functions. All functions used here, including the additional test functions in Section 4, are bounded with bounded derivatives. For any fixed integer \(p\ge2\), the conditional Gaussian moment bound for the removed term is at most
\[
\mathbb E\!\left[\frac1n\sum_i|(P_HN)_i|^p\,\middle|\,H,Z\right]
\le \frac{C_p}{n}\sum_i(P_H)_{ii}^{p/2}
\le \frac{C_p\operatorname{rank}H}{n},
\]
since \(D\) is bounded and \(0\le(P_H)_{ii}\le1\). Conditional laws of large numbers for the remaining independent Gaussian rows, followed by this estimate and Hölder's inequality, yield convergence of every fixed polynomial moment of the returned fields. Products with bounded functions of \(X_1,X_2,X_3\) are therefore justified. This proof uses no positive-time limit theorem.

## 3. First-layer feature acceleration and passive response

Differentiating (1) at zero gives, for every panel input,
\[
\ddot z_{1,a}(0)\leadsto\sum_{b=1}^2y_b S_{ab}g(X_b)B_b,\qquad
\ddot h_{1,a}(0)\leadsto
J_a:=g(X_a)\sum_{b=1}^2y_b S_{ab}g(X_b)B_b. \tag{13}
\]
The quadratic chain-rule term is zero because \(\dot z_{1,a}(0)=0\). For the two training inputs,
\[
J_1=y_1g(X_1)^2B_1,\qquad
J_2=y_2g(X_2)^2B_2. \tag{14}
\]
Since both first feature velocities vanish,
\[
\mathcal A_{1,12}=\mathbb E[J_1H_2+H_1J_2].
\]
The centered Gaussian terms contribute zero. In the first summand, the \(H_1R_{11}\) contribution vanishes by oddness, while
\[
\mathbb E[J_1H_2]
=y_1R_{12}\mathbb E[g(X_1)^2]\mathbb E[H_2^2]
=y_1y_2 q_X\sigma^2\alpha^2.
\]
The second summand is identical. Thus
\[
\boxed{\mathcal A_{1,12}
=2y_1y_2\sigma^2q_X\alpha^2
=2y_1y_2\sigma^2\,
\mathbb E[\operatorname{sech}^4X]\,
(\mathbb E[\operatorname{sech}^2Z])^2.} \tag{15}
\]
The formula is nonzero when \(y_1y_2\ne0\), with the sign of that product. It describes sample interaction despite \(S_{12}=0\): the two samples share the trained readout and the middle matrix, and the transpose return aligns each lower response with the other sample's feature. Removing the reaction term in (6) would incorrectly give zero in (15).

The passive feature acceleration is exactly
\[
\boxed{
J_3
=g(X_3)\left[
\frac{2y_1}{\sqrt5}g(X_1)
\left(\zeta_1+H_1y_1r_0+H_2y_2\alpha^2\right)
+\frac{y_2}{\sqrt5}g(X_2)
\left(\zeta_2+H_1y_1\alpha^2+H_2y_2r_0\right)
\right].} \tag{16}
\]
This is the proposed passive formula with every coefficient and covariance supplied. Only the training labels occur; sample 3 is evaluated, not trained.

The passive upper initialization also must retain the nonlinear feature covariance. Define
\[
q_{13}=\mathbb E[H_1H_3],\qquad q_{23}=\mathbb E[H_2H_3].
\]
Then the second-population initial triple is centered Gaussian with covariance
\[
\mathbb E[Z_aZ_b]
=\begin{pmatrix}
\sigma^2&0&q_{13}\\
0&\sigma^2&q_{23}\\
q_{13}&q_{23}&\sigma^2
\end{pmatrix}_{ab}. \tag{17}
\]
In particular, one cannot set \(Z_3=(2Z_1+Z_2)/\sqrt5\). Indeed,
\[
\operatorname{Var}\!\left(Z_3-\frac{2Z_1+Z_2}{\sqrt5}\right)
=\mathbb E\!\left[
\left(T\!\left(\frac{2X_1+X_2}{\sqrt5}\right)
-\frac{2T(X_1)+T(X_2)}{\sqrt5}\right)^2\right]>0.
\]
The strict inequality holds because the continuous functions inside the square are not identical, as is already seen from their cubic terms near zero. The linear identity holds for \(X_3\), before the first nonlinear activation, not for its next-layer preactivation. The initial passive output slope is the finite-program limit
\[
\dot f_3(0)\ \longrightarrow\
y_1\mathbb E[T(Z_1)T(Z_3)]
+y_2\mathbb E[T(Z_2)T(Z_3)], \tag{18}
\]
with the Gaussian law (17). This gives an explicit observable passive response without inventing a passive residual.

## 4. Middle-matrix contribution versus total second-layer acceleration

In finite-width matrix expressions below, \(d_a\) and \(\psi_a\) denote the coordinatewise evaluations of their scalar functions on the initial upper preactivations. At zero, \(\dot W=\dot h_1=0\). Therefore the exact finite-width product rule is
\[
\ddot z_{2,a}(0)=\ddot W(0)h_{1,a}(0)+G\ddot h_{1,a}(0),\qquad
\ddot W(0)=\frac1n\sum_{b=1}^2y_b d_b\,h_{1,b}(0)^\top. \tag{19}
\]
The first term is the contribution of learning the middle matrix; the second is the contribution of moving its input features. These are an additive decomposition of the initial acceleration of the same flow, not a claim that changing the training rule leaves the later trajectory unchanged.

Since the initial training feature Gram tends to \(\sigma^2I_2\), the middle-matrix piece, for \(a=1,2\), is
\[
\ddot z_{2,a}(0)\big|_{\mathrm{middle}}\leadsto
\sigma^2y_a d_a,\qquad
\ddot h_{2,a}(0)\big|_{\mathrm{middle}}\leadsto
\sigma^2y_a g(Z_a)^2Q.
\]
It follows that
\[
\boxed{\mathcal A_{2,12}\big|_{\mathrm{middle}}
=2y_1y_2\sigma^2\nu\beta
=2y_1y_2\sigma^2\,
\mathbb E[\tanh^2Z]\,\mathbb E[\operatorname{sech}^4Z].} \tag{20}
\]
This verifies the proposed formula precisely as an isolated contribution. It is not the total \(\mathcal A_{2,12}\).

One can also calculate the remaining contribution using only a joint first return, without assuming that an adapted forward action of \(G\) is independent Gaussian. Define the bounded upper-row tests
\[
\psi_1(Z)=g(Z_1)T(Z_2),\qquad
\psi_2(Z)=g(Z_2)T(Z_1).
\]
Exact finite-width adjointness gives
\[
\frac1n\psi_a^\top G\ddot h_{1,a}(0)
=\frac1n(G^\top\psi_a)^\top\ddot h_{1,a}(0). \tag{21}
\]
Append \(\psi_1,\psi_2\) to the same block of reverse queries as \(d_1,d_2\) in (12). Their limiting fields are
\[
B_{\psi_1}=\zeta_{\psi_1}+H_2\alpha^2,\qquad
B_{\psi_2}=\zeta_{\psi_2}+H_1\alpha^2,
\]
because \(\mathbb E\partial_1\psi_1=0\) and
\(\mathbb E\partial_2\psi_1=\alpha^2\), and conversely for \(\psi_2\). The Gaussian covariance rule gives
\[
\mathbb E[\zeta_{\psi_1}\zeta_1]
=\mathbb E[\psi_1d_1]=y_2\beta\nu,\qquad
\mathbb E[\zeta_{\psi_2}\zeta_2]
=y_1\beta\nu. \tag{22}
\]
Using (14), the limiting first term of (21) is consequently
\[
\begin{aligned}
\mathbb E[B_{\psi_1}J_1]
&=y_1q_X\,\mathbb E[\zeta_{\psi_1}\zeta_1]
 +y_1\mathbb E[g(X_1)^2H_2\alpha^2
                   (H_1y_1r_0+H_2y_2\alpha^2)]\\
&=y_1y_2q_X\bigl(\beta\nu+\sigma^2\alpha^4\bigr).
\end{aligned}
\]
The analogous second term is equal. Therefore
\[
\mathcal A_{2,12}\big|_{\mathrm{first\ layer}}
=2y_1y_2q_X\bigl(\beta\nu+\sigma^2\alpha^4\bigr), \tag{23}
\]
and the total is
\[
\boxed{
\mathcal A_{2,12}
=2y_1y_2\left[
(\sigma^2+q_X)\nu\beta+\sigma^2q_X\alpha^4
\right].} \tag{24}
\]
The first-layer part contains both a correlated Gaussian-return contraction and a reaction-alignment contraction. Both have been retained. When \(y_1y_2>0\), every coefficient in (20), (23), and (24) is positive; opposite signs reverse the cross-Gram acceleration.

## 5. Verdict and scope

The proposed formulas for \(R_{aa}\), \(R_{ab}\) with \(a\ne b\), \(\mathcal A_{1,12}\), the passive first-layer acceleration, and the isolated learned-middle-matrix contribution all pass with the prescribed \(2/m=1\) clock. The necessary qualifications are:

1. The return Gaussian fields are jointly correlated by (7) and (11), not independently sampled across training inputs.
2. The upper passive preactivation uses the nonlinear feature covariance (17), not the linear relation satisfied by the raw input projections.
3. The middle-matrix contribution (20) is only one part of the total second-layer acceleration, whose complete value is (24).
4. Every limiting derivative here is a rigorously identified finite initial-program statistic as in (2). This note proves no positive-time limiting flow or continuous-time approximation rate.

The example displays genuinely nonlinear feature motion in both hidden layers, cross-sample interaction for orthogonal training inputs, and a passive response driven only by the training set. It does so with explicit scalar Gaussian laws and their return correlations, not with an independence ansatz for reusing the initial matrix.
