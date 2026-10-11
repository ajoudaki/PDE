# Rank-free nonlinear feature coercivity: bounded route report

Status: internally derived baseline small-label theorem, not independently reviewed. This is a reconstruction of a local initialization argument, not a new arbitrary-label extension. The arbitrary fixed-label-amplitude target remains open. No experiments or external scientific sources were used. The first round used only the supervisor's model. After that round, the complete same-study notes `GAUSSIAN_NONORTHOGONAL_EXTENSION.md` and `GAUSSIAN_POSITIVE_GEOMETRY.md` were read under explicit supervisor authorization. No other study was consulted.

## 1. Model and exact dynamics

Let the columns of \(X\in\mathbb R^{d\times m}\) be distinct, nonantipodal unit vectors. The number \(m\) is fixed, and \(X\) may have rank strictly below \(m\). The network and loss are
\[
U=\tanh(AX),\quad H=\tanh(WU),\quad
f=H^\top w/n,\quad r=f-y,\quad \mathcal L=\|r\|_2^2/m.
\]
Initialization has independent \(A_{ij}\sim N(0,1)\), \(W_{ij}\sim N(0,1/n)\), and \(w=0\). All parameters train with mobilities \(n,1,n\), respectively.

For sample \(a\), write \(u_a,h_a\) for the corresponding feature columns and set
\[
b_a=w\odot(1-h_a^2),\qquad
c_a=(1-u_a^2)\odot W^\top b_a.
\]
The exact equations are
\[
\dot A=-\frac2m\sum_a r_a c_a x_a^\top,\quad
\dot W=-\frac2{mn}\sum_a r_a b_a u_a^\top,\quad
\dot w=-\frac2m\sum_a r_a h_a.
\]
Their prediction kernel is
\[
K_{ab}=\frac{h_a^\top h_b}{n}
+\frac{b_a^\top b_b}{n}\frac{u_a^\top u_b}{n}
+(x_a^\top x_b)\frac{c_a^\top c_b}{n}.
\]
Each summand is positive semidefinite, and
\[
\dot r=-\frac2mKr,\qquad
\dot{\mathcal L}=-\frac4{m^2}r^\top Kr.
\]

## 2. The nonlinear initialized feature Gram has full rank

Define
\[
(Q_U)_{ab}=\mathbb E_{g\sim N(0,I_d)}
 [\tanh(g^\top x_a)\tanh(g^\top x_b)].
\]
Then \(Q_U\succ0\), irrespective of the rank of \(X\).

To prove this, suppose \(v^\top Q_Uv=0\). The continuous function
\(\sum_a v_a\tanh(g^\top x_a)\) vanishes everywhere, because its square has zero integral against a Gaussian density that is positive everywhere. Choose \(q\in\mathbb R^d\) outside the finitely many hyperplanes perpendicular to \(x_a\), \(x_a-x_b\), and \(x_a+x_b\). All numbers \(\lambda_a=|q^\top x_a|\) are then positive and distinct. Restricting to \(g=tq\) gives
\[
\sum_a d_a\tanh(\lambda_a t)=0,
\qquad d_a=v_a\operatorname{sgn}(q^\top x_a).
\]
First let \(t\to\infty\), obtaining \(\sum_a d_a=0\). Among indices with nonzero coefficient, choose the smallest \(\lambda_a\). Since
\(\tanh(\lambda t)=1-2e^{-2\lambda t}+o(e^{-2\lambda t})\), subtracting the constant relation and multiplying by \(e^{2\lambda_a t}\) gives \(-2d_a=0\), a contradiction. Thus all coefficients vanish.

For every finite \(n\ge m\), \(U(0)\) has column rank \(m\) almost surely. Indeed, the feature vectors \((\tanh(g^\top x_a))_{a=1}^m\) span \(\mathbb R^m\), since any orthogonal vector would contradict the preceding linear-independence proof. Choose \(m\) spanning feature vectors. Therefore the determinant of the first \(m\) sampled rows, as a real-analytic function of their \(md\) input coordinates, is not identically zero. A nonzero real-analytic function on connected Euclidean space has a Lebesgue-null zero set. One direct justification is to cover its zeros by the sets where a first nonvanishing derivative occurs: each point belongs to the zero set of a lower derivative with nonzero gradient, hence locally to a smooth hypersurface; countably many derivative choices and coordinate neighborhoods suffice. Analyticity excludes a point with all derivatives zero unless the function vanishes identically. The Gaussian root tuple has a density, so the determinant is nonzero almost surely.

Conditional on such a full-rank \(U(0)\), the top preactivation rows have a nonsingular Gaussian density on \(\mathbb R^m\). Coordinatewise tanh is a diffeomorphism onto \((-1,1)^m\), so the top-feature rows also have a density there. The determinant of their first \(m\) rows is a nonzero polynomial, with a null zero set. Thus \(H(0)\) has column rank \(m\) almost surely as well.

The iid row law and boundedness imply
\(U(0)^\top U(0)/n\to Q_U\). Conditional on \(U(0)\), the rows of \(W(0)U(0)\) are independent \(N(0,U(0)^\top U(0)/n)\). Consequently
\[
\frac{H(0)^\top H(0)}n\longrightarrow Q_H,
\qquad
Q_H=\mathbb E_{z\sim N(0,Q_U)}[\tanh(z)\tanh(z)^\top],
\]
in probability. Entrywise conditional concentration follows from bounded independent summands; continuity in the covariance follows by coupling through its continuous positive-semidefinite square root and using dominated convergence.

Because \(Q_U\succ0\), the Gaussian \(z\) has positive density on \(\mathbb R^m\). The coordinatewise tanh image contains the open cube \((-1,1)^m\), so no nonzero linear functional of \(\tanh(z)\) vanishes almost surely. Hence \(Q_H\succ0\).

In particular, singularity of the input Gram is not an initialized feature-rank obstruction.

## 3. Complete baseline reconstruction for a fixed small-label range

Put
\[
\kappa=\tfrac12\lambda_{\min}(Q_H)>0,\quad M=10,
\quad C=\sqrt m\left(\frac{1+M^2}{2}+\frac M8\right),
\]
and define
\[
s_0=\min\left\{1,\left(\frac{\sqrt\kappa}{2C}\right)^{1/2}\right\}.
\]
For every fixed label vector satisfying
\[
\|y\|_2\le\frac{\kappa s_0}{8\sqrt m},
\tag{1}
\]
the canonical fully trained network satisfies
\[
\Pr\left\{\mathcal L_n(t)\le\mathcal L_n(0)e^{-\kappa t/m}
              \text{ for every }t\ge0\right\}\longrightarrow1.
\tag{2}
\]
This allows arbitrary rank-deficient data of the stated geometry. Its label threshold depends on the fixed data, but not on width. It does not establish the requested arbitrary-amplitude assertion.

Here is a direct deterministic proof on the initialization event
\[
H(0)^\top H(0)/n\succeq\kappa I_m,
\qquad \|W(0)\|_{\rm op}\le M.
\tag{3}
\]
The first event has probability tending to one by Section 2. For the second, a \(1/4\)-net on each unit sphere has at most \(9^n\) points, and the operator norm is at most twice the largest bilinear form on the two nets. Each such bilinear form is \(N(0,1/n)\), so
\[
\Pr\{\|W(0)\|_{\rm op}>10\}
\le 2\exp(2n\log9-100n/8)\longrightarrow0.
\]

Define the accumulated residual
\[
s(t)=2\int_0^t\sqrt{\mathcal L(v)}\,dv
=\frac2{\sqrt m}\int_0^t\|r(v)\|_2\,dv.
\]
The displayed exact velocities, \(|u_{a,j}|,|h_{a,i}|\le1\), and unit input norms give
\[
\|w(t)\|_\infty\le s(t),\qquad
\|W(t)-W(0)\|_F\le s(t)^2/2,
\]
and
\[
\frac{\|A(t)-A(0)\|_F}{\sqrt n}
\le M s(t)^2/2+s(t)^4/8.
\tag{4}
\]
For the last bound, the instantaneous normalized first-layer speed is at most
\(\|W\|_{\rm op}\|w\|_2s'/\sqrt n\); insert
\(\|W\|_{\rm op}\le M+s^2/2\) and \(\|w\|_2/\sqrt n\le s\), then integrate.

Since tanh is 1-Lipschitz and \(\|X\|_{\rm op}\le\sqrt m\), (4) implies
\[
\begin{aligned}
\frac{\|H(t)-H(0)\|_F}{\sqrt n}
&\le \sqrt m\left[\frac{1+M^2}{2}s(t)^2
                         +\frac M8s(t)^4\right]\\
&\le C s(t)^2\qquad(s(t)\le1).
\end{aligned}
\tag{5}
\]
The two terms before the final bound come from
\((W-W(0))U\) and \(W(0)(U-U(0))\), respectively.

Whenever \(s(t)\le s_0\), (5) is at most \(\sqrt\kappa/2\). For every \(v\in\mathbb R^m\), the triangle inequality applied to \(Hv/\sqrt n\) therefore yields
\[
v^\top H(t)^\top H(t)v/n\ge(\kappa/4)\|v\|_2^2.
\]
The full kernel is larger, so
\[
\|r(t)\|_2\le\|y\|_2e^{-\kappa t/(2m)}
\]
up to any first exit from \(s<s_0\). Integrating gives
\[
s(t)\le\frac{4\sqrt m\|y\|_2}{\kappa}
\le s_0/2.
\]
This contradicts a first exit. Thus the bound holds for all time and proves (2).

The smooth finite-dimensional ODE exists globally: loss dissipation bounds \(\|r\|\), hence \(s(t)\) on each finite time interval, and (4) and the preceding bounds prevent finite-time parameter escape. No width/time interchange or frozen-layer replacement occurs in this argument.

## 4. Finite critical points in the full-feature-rank region

At any finite critical point with \(\operatorname{rank}U=m\), a nonzero residual forces \(w=0\). Indeed, the gradient of middle-weight row \(i\) is proportional to
\[
w_i U\,[r\odot(1-h_i^2)],
\]
where \(h_i\in\mathbb R^m\) is row \(i\) of \(H\). Injectivity of \(U\) and strictly positive finite tanh derivatives show that \(w_i\ne0\) would force \(r=0\).

Every such nonfitting critical point is a strict saddle. At \(w=0\), all pure middle-weight variations leave the loss unchanged. Choose a neuron \(i\) and a middle-row variation \(v\in\mathbb R^n\) such that
\[
U^\top v=\operatorname{diag}(1-h_i^2)^{-1}y;
\]
it exists because \(U\) has full column rank. The mixed second derivative in the readout coordinate \(w_i\) and this middle-row direction is
\(-2\|y\|_2^2/(mn)\ne0\). The two-dimensional Hessian restriction has one zero diagonal entry and a nonzero off-diagonal entry, hence negative determinant and a negative eigenvalue.

This does not prove that the actual flow stays in this rank region, has a finite limit, or avoids every saddle from its singular initialization slice \(w=0\).

## 5. What full support does and does not prove

Full support of a first-neuron distribution guarantees positive feature Gram at each fixed time by the linear-independence argument of Section 2. It gives no uniform-in-time lower bound, even together with uniformly controlled moments and finite transport length.

For an explicit counterexample to that implication, take \(a(t)=e^{-t}a(0)\), with \(a(0)\sim N(0,I_d)\). Every finite-time law has full support; all Gaussian moments are uniformly bounded; and
\[
\int_0^\infty\|a'(t)\|_{L^2}\,dt=\sqrt d<\infty.
\]
Nevertheless, its nonlinear feature Gram tends to zero. This is not an actual-training trajectory or a Gaussian nonfitting counterexample. It only invalidates the proposed sufficient-condition package.

The exact general-geometry first-feature equation is
\[
\dot u_a=-\frac2m(1-u_a^2)\odot
 \sum_b (x_a^\top x_b)r_b(1-u_b^2)\odot W^\top b_b.
\]
Differentiating with respect to the initialized Gaussian matrix creates multiplication of the perturbation by \(W^\top b_b\). Bounded operator and normalized \(L^2\) norms do not control that multiplication on \(L^2\). The orthogonal natural coordinates in the allowed earlier note remove this term; a general Gram does not retain that cancellation.

A naive cavity argument removing one first-layer neuron creates an order-one total top-layer perturbation. Bounding its propagation by the maximum backward coordinate introduces a factor of the form
\(\exp(C\int\|W^\top b\|_\infty)\), which is not width-uniform. Thus this argument does not establish Gaussian backward tails or a bounded causal response shift.

One concrete missing input is a conditional characteristic representation with a continuous Gaussian drive independent of the first-neuron root, plus a uniformly bounded and suitably Lipschitz causal response term on each finite feature interval. Such a representation could give a complete characteristic flow and finite-endpoint full support. It has not been established here.

For a transitive signed input symmetry, deterministic population predictions would stay on the label ray. The scalar readout-homogeneity argument in the allowed geometry note then reaches every fixed amplitude at finite feature time. Rank-deficient examples include odd regular polygons with equal labels. This observation adds a possible geometry class but does not supply the missing population construction, endpoint diversity, or finite-width convergence. It is a conditional route, not a new completed arbitrary-amplitude theorem.

## 6. Route status

The complete positive claim is the explicit rank-free small-label baseline above, pending independent review; it is not a new arbitrary-label extension. Strict positivity of the initialized nonlinear feature Gram is established for all the stated geometries. The arbitrary fixed-amplitude target remains open; no positive-probability Gaussian failure event has been constructed. The transport and cavity route is blocked at quantitative control of the trained backward response, and full-support arguments alone cannot replace that estimate.
