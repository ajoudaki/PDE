## 10. Correlated opposite labels: mixed-activation finite fitting

This section proves a finite-GF result, not a population limit or a raw-GD
theorem. Some first rows are frozen by the activation's own saturation under
the actual gradient, not by changing the optimizer. Other rows are not frozen
by prescription. Section 11 gives a separate positive unsaturated-mass result;
neither assertion alone proves nonzero hidden feature velocity.

### 10.1 Model, invariant rows and finite existence

Fix two deterministic inputs with \(\|x_a\|^2=d\),
\(G_{ab}=x_a^Tx_b/d\), \(G_{12}=\rho\in(-1,1)\), and labels
\((y_1,y_2)=(1,-1)\). In particular \(d\ge2\).
Fix \(R>0\) and an odd smooth activation \(\phi^{(1)}\), with
\(\phi^{(1)}(0)=0\), whose derivative is even, nonnegative, supported on
\([-R,R]\), and strictly positive on \((-R,R)\). Put
\[
 A=\int_0^R(\phi^{(1)})'(u)\,du>0,\qquad
 P=\|(\phi^{(1)})'\|_\infty,
 \qquad \phi^{(2)}(z)=z+\varepsilon\arctan z,\quad
 M=1+\varepsilon,\quad \varepsilon>0.
 \tag{10.1}
\]
Thus \(|\phi^{(1)}|\le A\), \(1\le(\phi^{(2)})'\le M\), and
\(|\phi^{(2)}(z)|\le M|z|\). The activations are fixed independently of
the input configuration; constants below may depend on that configuration.

Use the shared raw parameters and normalizations:
\[
 z_a^{(1)}=W^{(1)}x_a/\sqrt d,\quad
 h_a^{(1)}=\phi^{(1)}(z_a^{(1)}),\quad
 z_a^{(2)}=W^{(2)}h_a^{(1)},\quad h_a^{(2)}=\phi^{(2)}(z_a^{(2)}),
 \quad f_a=(W^{(3)})^Th_a^{(2)}/n,\quad r_a=f_a-y_a.
\]
Here both hidden widths are \(n\), and \(W^{(3)}\) is the stored readout.
With the unhalved sum loss \(\mathcal L_\Sigma=\|r\|^2=2\mathcal L_n\),
the exact flow is
\[
 \dot W^{(1)}=-\frac2{\sqrt d}\sum_a r_a\delta_a^{(1)}x_a^T,
 \quad \dot W^{(2)}=-\frac2n\sum_a r_a\delta_a^{(2)}(h_a^{(1)})^T,
 \quad \dot W^{(3)}=-2\sum_a r_a h_a^{(2)},
 \tag{10.2}
\]
where
\[
 \delta_a^{(2)}=W^{(3)}\odot(\phi^{(2)})'(z_a^{(2)}),\qquad
 \delta_a^{(1)}=(\phi^{(1)})'(z_a^{(1)})\odot
                         (W^{(2)})^T\delta_a^{(2)}.
\]
Mean-loss GF has half these velocities and takes twice the physical time
to traverse the same path. All statements here use (10.2).

Let \(\mathbf h^{(\ell)}=[h_1^{(\ell)},h_2^{(\ell)}]\), a finite
\(n\)-by-two array, and \(K^{(\ell)}\) the raw kernel block for parameter
\(W^{(\ell)}\). Direct differentiation gives
\[
 \dot r=-2Kr,\quad K=K^{(1)}+K^{(2)}+K^{(3)},
\]
\[
 K^{(1)}_{ab}=G_{ab}\frac{(\delta_a^{(1)})^T\delta_b^{(1)}}n,
 \quad K^{(2)}_{ab}=
 \frac{(h_a^{(1)})^Th_b^{(1)}}n
 \frac{(\delta_a^{(2)})^T\delta_b^{(2)}}n,
 \quad K^{(3)}=\frac{(\mathbf h^{(2)})^T\mathbf h^{(2)}}n.
 \tag{10.3}
\]
Each is a Gram matrix: the first uses the vectors
\(\delta_a^{(1)}x_a^T/\sqrt{nd}\), the second the matrices
\(\delta_a^{(2)}(h_a^{(1)})^T/n\), and the last the vectors
\(h_a^{(2)}/\sqrt n\). Consequently
\[
 -\frac{d}{dt}\mathcal L_\Sigma
 =4r^TKr
 =\frac{\|\dot W^{(1)}\|_F^2}n+
   \|\dot W^{(2)}\|_F^2+\frac{\|\dot W^{(3)}\|^2}n.
 \tag{10.4}
\]
The smooth finite vector field has a unique local solution. Integrating each
squared speed and applying Cauchy--Schwarz gives, for \(0\le s<t\),
\[
 \frac{\|W^{(1)}(t)-W^{(1)}(s)\|_F}{\sqrt n},\quad
 \|W^{(2)}(t)-W^{(2)}(s)\|_F,\quad
 \frac{\|W^{(3)}(t)-W^{(3)}(s)\|}{\sqrt n}
 \ \le\sqrt{(t-s)\mathcal L_\Sigma(0)}.
 \tag{10.5}
\]
At fixed width these bounds produce finite parameter limits at any finite
maximal endpoint. Local existence at that endpoint extends the solution.
Thus GF exists globally for every finite initial state, without any of the
success-event assumptions below.

A first row whose two initial preactivations lie outside \((-R,R)\)
remains fixed: its two gates vanish, fixing the row solves its equation, and
local uniqueness identifies this with its actual evolution. Let \(N_s,N_o\)
count these saturated rows with respectively equal and opposite signs.
Their constant contribution to the first-feature Gram is
\[
 \frac{(\mathbf h^{(1)}(t))^T\mathbf h^{(1)}(t)}n
 \succeq\frac{A^2}n
 \begin{pmatrix}N_s+N_o&N_s-N_o\\N_s-N_o&N_s+N_o\end{pmatrix}
 \succeq\gamma_n I_2,
 \quad \gamma_n=\frac{2A^2}n\min(N_s,N_o).
 \tag{10.6}
\]
The other rows add a positive semidefinite Gram. The eigenvectors
\((1,1)\) and \((1,-1)\) give the two displayed eigenvalues.

### 10.2 Fitting after an actual loss margin

Assume for now \(\gamma_n\ge\gamma>0\) and
\(\|W^{(2)}(0)\|_{\rm op}\le B_0\). Define the scalar quantities
\[
 e=\|r\|,\quad M_2=\|W^{(2)}-W^{(2)}(0)\|_F,\quad
 M_3=\|W^{(3)}\|/\sqrt n,\quad b_0=M_3(0),\quad
 S_w(t)=\int_0^t e(u)M_3(u)\,du.
 \tag{10.7}
\]
This weighted residual integral is not a replacement optimizer.
For each second neuron put
\(D_i=\operatorname{diag}((\phi^{(2)})'(z^{(2)}_{1,i}),
(\phi^{(2)})'(z^{(2)}_{2,i}))\). By (10.6), congruence of positive
matrices gives
\[
 K^{(2)}=\frac1n\sum_i(W_i^{(3)})^2D_i
 \frac{(\mathbf h^{(1)})^T\mathbf h^{(1)}}n D_i
 \succeq\gamma M_3^2 I_2.
\]
Therefore
\[
 \frac{d}{dt}\mathcal L_\Sigma\le-4\gamma M_3^2\mathcal L_\Sigma,
 \qquad e'\le-2\gamma M_3^2e\quad\hbox{where }e>0.
 \tag{10.8}
\]
At zero residual all velocities vanish and the solution stays constant.

The homogeneity defect of the top activation is bounded:
\[
 D(z)=z(\phi^{(2)})'(z)-\phi^{(2)}(z)
 =\varepsilon\left(\frac z{1+z^2}-\arctan z\right),\qquad
 \|D\|_\infty=\varepsilon\pi/2.
\]
Indeed \(D'(z)=-2\varepsilon z^2/(1+z^2)^2\), \(D(0)=0\), and its
two infinite limits are \(\mp\varepsilon\pi/2\). Set
\[
 C=2\sqrt2MA,\qquad D_0=4\sqrt2(\varepsilon\pi/2+MB_0A).
\]
The rank-one equation and \(\sum_a|r_a|\le\sqrt2e\) give
\(\|\dot W^{(2)}\|_F\le CeM_3\), hence \(M_2\le CS_w\).
Differentiating the two squared parameter norms, not the moving hidden
features, yields the exact centered balance
\[
 \frac{d}{dt}(M_2^2-M_3^2)
 =-\frac4n\sum_a r_a(W^{(3)})^T
 \left[D(z_a^{(2)})-
 (\phi^{(2)})'(z_a^{(2)})\odot W^{(2)}(0)h_a^{(1)}\right].
 \tag{10.9}
\]
For example, the first norm differentiates to
\(-4n^{-1}\sum_a r_a(W^{(3)})^T[
(\phi^{(2)})'(z_a^{(2)})\odot
(W^{(2)}-W^{(2)}(0))h_a^{(1)}]\); subtracting the readout norm
derivative supplies (10.9). Cauchy--Schwarz now proves
\[
 |M_2^2-M_3^2+b_0^2|\le D_0S_w,\quad
 M_2\le M_3+\sqrt{D_0S_w},\quad
 M_3^2\le C^2S_w^2+b_0^2+D_0S_w.
 \tag{10.10}
\]
Only the initial operator norm enters, not an initial Frobenius norm growing
with width. Also, using \(\|\mathbf h^{(1)}\|_F\le A\sqrt{2n}\),
\[
 \|f\|\le \sqrt2MA M_3(B_0+M_2)
 \le C M_3(B_0+M_3+\sqrt{D_0S_w}).
 \tag{10.11}
\]

Suppose the actual flow reaches \(\mathcal L_\Sigma(t_0)<2\) at finite
\(t_0\). Put \(e_0=e(t_0)\), \(\nu=\sqrt2-e_0>0\), and
\[
 c=\min\{1,\nu/[C(B_0+1+\sqrt{D_0})]\}>0.
\]
For \(t\ge t_0\), monotonicity and the reverse triangle inequality give
\(\|f(t)\|\ge\nu\). If \(M_3\le1\), (10.11) bounds it below by
\(c/(1+\sqrt{S_w})\); if \(M_3\ge1\), the same bound holds since
\(c\le1\). Let
\[
 F(x)=\int_0^x\frac{du}{1+\sqrt u}
 =2[\sqrt x-\log(1+\sqrt x)]\quad(x\ge0).
\]
Combining this lower bound with (10.8) and \(S_w'=eM_3\) gives
\[
 e(t)+2\gamma c[F(S_w(t))-F(S_w(t_0))]\le e_0.
 \tag{10.12}
\]
This integrates a time-domain differential inequality; it does not invert
the clock and remains valid through zero residual by constant continuation.
The inequality \(\log(1+u)\le u/2+\log2\), obtained by maximizing its
left side minus \(u/2\), implies \(F(x)\ge\sqrt x-2\log2\).
Thus, with
\[
 S_b=[F(S_w(t_0))+e_0/(2\gamma c)+2\log2]^2,\quad
 U=B_0+CS_b,\quad \beta=c/(1+\sqrt{S_b})>0,
\]
we have \(S_w(t)\le S_b\), \(\|W^{(2)}(t)\|_{\rm op}\le U\),
and an upper bound for \(M_3\) from (10.10), for every \(t\ge0\).
Moreover \(M_3(t)\ge\beta\) for \(t\ge t_0\). It follows that
\[
 \mathcal L_\Sigma(t)\le e_0^2e^{-4\gamma\beta^2(t-t_0)},\qquad
 \int_0^\infty e(t)\,dt
 \le t_0\sqrt{\mathcal L_\Sigma(0)}+e_0/(2\gamma\beta^2).
 \tag{10.13}
\]
The constants are noncircular: (10.5) already gives
\[
 S_w(t_0)\le \sqrt{\mathcal L_\Sigma(0)}b_0t_0
                   +\tfrac23\mathcal L_\Sigma(0)t_0^{3/2}.
\]
Finally, the exact equations imply
\[
 \|\dot W^{(2)}\|_F\le CeM_3,\quad
 \|\dot W^{(3)}\|/\sqrt n\le CUe,\quad
 \|\dot W^{(1)}\|_F/\sqrt n\le2\sqrt2PMUeM_3.
 \tag{10.14}
\]
All three speeds are integrable. Completeness in each finite-dimensional
parameter space gives finite endpoints, and continuity of the predictor plus
(10.13) makes their predictions exactly the two labels.

### 10.3 The actual Gaussian initialization supplies the margin

Initialize all entries independently with
\[
 W^{(1)}_{0,ij}\sim N(0,1),\quad W^{(2)}_{0,ij}\sim N(0,1/n),\quad
 W^{(3)}_{0,i}\sim N(0,n^{-2}).
 \tag{10.15}
\]
Let \((U_1,U_2)\sim N(0,G)\). Write \(p_s\) and \(p_o\) for its
probabilities of both coordinates having absolute value at least \(R\),
with respectively equal and opposite signs. Nondegenerate Gaussian density
is positive on all open corners, so
\(\gamma=A^2\min(p_s,p_o)>0\). Set \(\kappa=\gamma/2\), \(B_0=8\).
The event \(E_F=\{N_s/n\ge p_s/2,\ N_o/n\ge p_o/2\}\) gives
\(\gamma_n\ge\gamma\) and satisfies
\[
 \mathbb P(E_F^c)\le\frac4n
       \left(\frac{1-p_s}{p_s}+\frac{1-p_o}{p_o}\right).
 \tag{10.16}
\]
Each count has variance \(np(1-p)\); integrating the squared centered
count on its deviation event proves this bound, without independence between
the two counts.

Conditional on the first weights, second-preactivation row pairs are
independent centered Gaussians with covariance
\(Q=(\mathbf h^{(1)}(0))^T\mathbf h^{(1)}(0)/n\). On \(E_F\),
\(Q\succeq\gamma I_2\), \(Q_{aa}\le A^2\). Represent one pair as
\(Z=U+\sqrt\gamma\xi\), with independent Gaussian vectors of covariances
\(Q-\gamma I_2\) and \(I_2\). Conditional on \(U\), the transformed
coordinates \(\phi^{(2)}(Z_a)\) are independent. For a scalar random
variable \(T\) and independent copy \(T'\),
\[
 \operatorname{Var}(\phi^{(2)}(T))
 =\tfrac12\mathbb E(\phi^{(2)}(T)-\phi^{(2)}(T'))^2
 \ge\tfrac12\mathbb E(T-T')^2=\operatorname{Var}(T),
\]
since \((\phi^{(2)})'\ge1\). Conditional variance therefore shows that
the second-feature second-moment matrix is at least \(\gamma I_2\).
For its empirical version \(K^{(3)}(0)\), the fourth moment estimate
\[
 \mathbb E[\phi^{(2)}(Z_a)^2\phi^{(2)}(Z_b)^2\mid W^{(1)}_0]
 \le M^4\sqrt{3Q_{aa}^2\,3Q_{bb}^2}\le3M^4A^4
\]
and conditional row independence bound the expected squared Frobenius error
by \(12M^4A^4/n\). At error threshold \(\gamma/2\), this gives
\[
 \mathbb P\{K^{(3)}(0)\not\succeq\kappa I_2\mid W^{(1)}_0\}
 \le48M^4A^4/(n\gamma^2)\quad\hbox{on }E_F.
 \tag{10.17}
\]
The scalar Gaussian fourth moment is three times variance squared; it follows
by twice integrating the Gaussian density derivative by parts.

Two elementary norm bounds complete the event:
\[
 \mathbb P\{\|W^{(2)}_0\|_{\rm op}>8\}
 \le2e^{-(8-2\log9)n},\quad
 \mathbb P\{b_0>2/n\}\le e^{-(1-(\log2)/2)n}.
 \tag{10.18}
\]
For the first, a maximal 1/4-separated unit-sphere set has at most \(9^n\)
points by disjoint radius-1/8 ball volumes, and is a 1/4-net. Approximating
both unit test vectors shows that the norm is at most twice the largest
bilinear form on the two nets. Each form is \(N(0,1/n)\), whose tail beyond
four is at most \(2e^{-8n}\) by its exponential moment. The union bound gives
the first estimate. For the second, \(b_0^2=n^{-3}\sum_i\xi_i^2\), where
the \(\xi_i\) are independent standard Gaussians. Since
\(\mathbb E e^{\xi_i^2/4}=\sqrt2\), exponential Markov at \(4n\) gives
the second estimate. These exponential moments follow by integrating the
Gaussian density and completing its square.

Let \(E\) be the intersection of \(E_F\), the two norm events, and
\(K^{(3)}(0)\succeq\kappa I_2\). Then
\[
 \mathbb P(E)\ge\max(0,1-p_n),\quad
 p_n=\frac4n\left(\frac{1-p_s}{p_s}+\frac{1-p_o}{p_o}\right)
 +\frac{48M^4A^4}{n\gamma^2}
 +2e^{-(8-2\log9)n}+e^{-(1-(\log2)/2)n}\longrightarrow0.
 \tag{10.19}
\]
The conditional failure in (10.17) is integrated only over \(E_F\); no
independence between overlapping second-layer events is asserted.

It remains to prove an actual loss margin, not merely a negative initial
derivative. If initially \(\mathcal L_\Sigma(0)\le4\), energy and the
activation Lipschitz bounds give
\[
 \frac{\|\mathbf h^{(1)}(t)-\mathbf h^{(1)}(0)\|_F}{\sqrt n}
 \le P\sqrt{2t\mathcal L_\Sigma(0)},
\]
\[
 \frac{\|\mathbf h^{(2)}(t)-\mathbf h^{(2)}(0)\|_F}{\sqrt n}
 \le M\sqrt{2t\mathcal L_\Sigma(0)}
       [A+P(B_0+\sqrt{t\mathcal L_\Sigma(0)})].
 \tag{10.20}
\]
For the second inequality expand the preactivation difference as
\((W^{(2)}(t)-W^{(2)}(0))\mathbf h^{(1)}(0)+
W^{(2)}(t)(\mathbf h^{(1)}(t)-\mathbf h^{(1)}(0))\) and use (10.5).
Choose
\[
 \tau=\min\{1/4,\ \kappa/[32M^2(A+P(B_0+1))^2]\}>0.
\]
For \(t\le\tau\), (10.20) is at most \(\sqrt\kappa/2\).
Each unit sample-direction vector therefore has image under
\(\mathbf h^{(2)}(t)/\sqrt n\) of norm at least \(\sqrt\kappa/2\).
Thus \(K^{(3)}(t)\succeq\kappa I_2/4\) and (10.4) implies
\(\mathcal L_\Sigma(t)\le\mathcal L_\Sigma(0)e^{-\kappa t}\).

On the two norm events, (10.11) at zero gives \(\|f(0)\|\le2CB_0/n\).
Set
\[
 n_* =\left\lceil\max\left\{2,
 \frac{2CB_0}{\min(2-\sqrt2,\sqrt2(e^{\kappa\tau/4}-1))}
 \right\}\right\rceil.
\]
All constants are fixed and the denominator is positive. For \(n\ge n_*\),
\(\mathcal L_\Sigma(0)\le4\) and
\(\mathcal L_\Sigma(0)\le2e^{\kappa\tau/2}\). Hence the actual solution
satisfies
\[
 \mathcal L_\Sigma(\tau)\le2e^{-\kappa\tau/2}<2.
 \tag{10.21}
\]
Section 10.2 now applies. This proves global finite-GF fitting and finite
parameter endpoints on the explicit event \(E\) with probability tending to
one, for every fixed interior correlation. The nonzero Gaussian readout was
never replaced by zero.

All bounds can be chosen uniformly in width on \(E\), as follows. Set
\[
 e_* =\sqrt2e^{-\kappa\tau/4},\quad
 c_* =\min\{1,(\sqrt2-e_*)/[C(B_0+1+\sqrt{D_0})]\},\quad
 S_{\rm pre}=2\tau+\tfrac83\tau^{3/2},
\]
\[
 \overline S=[F(S_{\rm pre})+e_* /(2\gamma c_*)+2\log2]^2,
 \quad \overline U=B_0+C\overline S,
 \quad \beta_* =c_* /(1+\sqrt{\overline S}).
 \tag{10.22}
\]
Since \(b_0\le1\), the pre-margin bound gives \(S_w(\tau)\le S_{\rm pre}\).
Use the fixed lower bound \(c_*\) in (10.12) to obtain
\[
 S_w(\infty)\le\overline S,\quad
 \sup_t\|W^{(2)}(t)\|_{\rm op}\le\overline U,\quad
 \sup_t M_3(t)^2\le C^2\overline S^2+1+D_0\overline S,
\]
\[
 \mathcal L_\Sigma(t)\le e_*^2e^{-4\gamma\beta_*^2(t-\tau)}
 \quad(t\ge\tau),\qquad
 \int_0^\infty e(t)\,dt\le2\tau+e_* /(2\gamma\beta_*^2).
 \tag{10.23}
\]
These estimates do not bound individual readout coordinates uniformly in
width, or their products with top curvature. Outside \(E\) the proof asserts
global finite existence, not fitting. No constants are claimed uniform near
\(\rho=\pm1\).

## 11. Permanent first-gate mass on an augmented event

Retain exactly the model and event of Section 10. Put
\(\lambda_1=\|(\phi^{(1)})''\|_\infty>0\),
\(c_a=-2r_a\), and
\(q_a^{(1)}=(W^{(2)})^T\delta_a^{(2)}\), without a residual inside
the latter. The first-coordinate equations are
\[
 \dot z^{(1)}_{a,i}=\sum_{b=1}^2G_{ab}
       (\phi^{(1)})'(z^{(1)}_{b,i})c_b q^{(1)}_{b,i}.
 \tag{11.1}
\]
On \(E\), define
\[
 V_i=\int_0^\infty\sum_a|c_aq^{(1)}_{a,i}|\,dt,
 \qquad V_* =2\sqrt2M\overline U\overline S.
\]
Since \(\|q_a^{(1)}\|/\sqrt n\le M\overline U M_3\) and
\(\sum_a|c_a|\le2\sqrt2 e\), the Euclidean integral triangle inequality
on each finite interval, followed by the monotone limit, gives
\[
 \frac1n\sum_i V_i^2\le V_*^2.
 \tag{11.2}
\]
Every \(V_i\) is finite at each fixed width; independence from initialization
is neither assumed nor needed.

Let \(\Phi\) be the standard Gaussian distribution function and define
\[
 p_{\rm strip}=[2\Phi(R/2)-1]\,2[1-\Phi(3R/\sqrt{1-\rho^2})]>0,
\]
\[
 B_* =2V_* /\sqrt{p_{\rm strip}},\quad
 \delta_* =(R/2)e^{-\lambda_1B_*},\quad
 p_* =\min_{|z|\le R-\delta_*}(\phi^{(1)})'(z)>0.
 \tag{11.3}
\]
For each ordered pair \(a,b\) of distinct samples take the initial strip
\[
 I_a^0=\{i:|z^{(1)}_{a,i}(0)|\le R/2,
 \ |z^{(1)}_{b,i}(0)-\rho z^{(1)}_{a,i}(0)|\ge3R\}.
\]
Augment \(E\) by \(E_S=\{|I_1^0|/n,|I_2^0|/n\ge p_{\rm strip}/2\}\).
On \(E\cap E_S\), each sample has a fixed subset \(I_a\), of size at
least \(np_{\rm strip}/4\), for which
\[
 |z^{(1)}_{a,i}(t)|\le R-\delta_*\quad(t\ge0,i\in I_a),\qquad
 \inf_{t\ge0}\frac1n\sum_i[(\phi^{(1)})'(z^{(1)}_{a,i}(t))]^2
 \ge(p_{\rm strip}/4)p_*^2.
 \tag{11.4}
\]

To prove this, a row in \(I_a^0\) starts with its \(a\)-coordinate interior
and \(b\)-coordinate exterior. Before an exit from those strict conditions,
the \(b\) gate is zero and (11.1) gives
\[
 z_b^{(1)}-\rho z_a^{(1)}
   =z_b^{(1)}(0)-\rho z_a^{(1)}(0),\qquad
 \dot z_a^{(1)}=(\phi^{(1)})'(z_a^{(1)})c_aq_a^{(1)}
\]
for this row. The derivative vanishes at both endpoints and is
\(\lambda_1\)-Lipschitz, so
\(0\le(\phi^{(1)})'(z)\le\lambda_1(R-|z|)\) inside.
The absolutely continuous distance to the boundary satisfies
\((R-|z_a^{(1)}|)'\ge-\lambda_1|c_aq_a^{(1)}|(R-|z_a^{(1)}|)\)
almost everywhere. Multiplication by its integrating factor yields
\[
 R-|z_a^{(1)}(t)|\ge(R/2)e^{-\lambda_1V_i}>0,
 \qquad |z_b^{(1)}(t)|\ge3R-|\rho|R>2R.
\]
Continuity contradicts any finite first exit, and these time-independent
margins hold for every finite time. By (11.2), at most fraction
\(p_{\rm strip}/4\) of all rows have \(V_i>B_*\). Set
\(I_a=I_a^0\cap\{V_i\le B_*\}\). Subtraction of this worst-case count
from each strip count separately proves (11.4). The subsets may depend on
the entire trajectory, but are fixed in time; no selection from future data
is used in defining the actual dynamics.

For Gaussian first rows, \(z_a^{(1)}(0)\) and
\(z_b^{(1)}(0)-\rho z_a^{(1)}(0)\) are independent centered Gaussians,
of variances one and \(1-\rho^2\): their joint Gaussian characteristic
function factors because their covariance is zero. Thus each strip indicator
has mean \(p_{\rm strip}\), independently across neurons. The same count
variance argument as (10.16) gives
\[
 \mathbb P(E_S^c)\le8(1-p_{\rm strip})/(np_{\rm strip}).
\]
Consequently (11.4) holds simultaneously for both samples and all time with
probability at least
\(\max\{0,1-p_n-8(1-p_{\rm strip})/(np_{\rm strip})\}\), for
\(n\ge n_*\). No independence between the two events is assumed.

The extra event cannot simply be omitted. For even \(n\ge n_*\), choose
first rows realizing \(n/2\) preactivation pairs \((2R,2R)\) and
\(n/2\) pairs \((2R,-2R)\); the independent inputs permit this under the
displayed normalization. Choose \(W^{(2)}_0=I_n\) and
\(W^{(3)}_{0,i}=1/n\). All first gates vanish forever. Nevertheless
\(N_s=N_o=n/2\), \(\|W^{(2)}_0\|_{\rm op}=1<8\), \(b_0=1/n<2/n\),
and \(K^{(3)}(0)=\phi^{(2)}(A)^2I_2\succ\kappa I_2\).
All defining inequalities of \(E\) have strict margins. An open neighborhood
retains them and keeps every first row saturated; independent Gaussian
initialization has positive density on that neighborhood. Thus \(E\) alone
does not imply unsaturated mass, even almost surely at such fixed width.

The conclusion is gate mass, not force or motion. It supplies no lower bound
on residuals, reverse queries, hidden velocities or reverse-weighted kernels,
and no top-layer distributional nonaffinity. These two sections assert neither
a joint population limit nor a GD result, and do not cover antipodal inputs.
