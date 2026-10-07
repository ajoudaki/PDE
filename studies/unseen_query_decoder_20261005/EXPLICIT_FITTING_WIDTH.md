# Polynomial success width for original initialization and dense fitting

2026-10-07. Scoped proof-only derivation. This note establishes an explicit
initialization and all-time dense-fitting width, under the original dense
fitting label condition. It does not quantify the inherited trained-carrier
and complex-source event. No experiment, Git operation, maintained-file
change, or promotion was performed.

The two improvements over the assigned general fitting proof are exponential
concentration before taking a sphere net, and separate propagation of
standard deviations and covariance entries. They remove respectively the
exponential dependence on input dimension and the unnecessary
activation-envelope power proportional to depth squared. The original
Gaussian initialization, zero readout, optimizer, covariance gap, and label
allowance are unchanged.

## 1. Model and the explicit theorem

Fix hidden depth \(L\ge2\), \(m\ge d\ge1\), and deterministic unit vectors
\(v_a=x_a/\sqrt d\in S^{d-1}\), \(1\le a\le m\). All hidden layers have
width \(n\). The forward pass and prediction are
\[
z^{(1)}(v)=Av,\qquad z^{(j)}(v)=W^{(j)}h^{(j-1)}(v),\qquad
h^{(j)}(v)=\phi_j(z^{(j)}(v)),\qquad f_n(v)=w^\top h^{(L)}(v)/n.
\tag{1}
\]
Here \(A\in\mathbb R^{n\times d}\), \(W^{(j)}\in\mathbb R^{n\times n}\)
for \(2\le j\le L\), and \(w\in\mathbb R^n\). Their initial entries are
independent \(N(0,1)\), independent \(N(0,1/n)\), and zero, respectively;
the random blocks are mutually independent. Let
\[
b=\max_j|\phi_j(0)|,\qquad s=\max\{1,\max_j\|\phi'_j\|_{L^\infty(\mathbb R)}\}.
\]
For global ODE well-posedness assume also bounded continuous second real
derivatives. The specified analytic strip class satisfies these assumptions.
No bound on activation values, centering, or variance normalization is used.

For a scalar standard Gaussian \(G\), define
\[
q_0=1,\qquad q_j=\mathbb E\phi_j(\sqrt{q_{j-1}}G)^2,
\qquad H=\max\{1,\sqrt{q_1},\ldots,\sqrt{q_L}\}.
\tag{2}
\]
For the training set define
\[
Q^{(0)}_{ab}=v_a^\top v_b,\qquad
Q^{(j)}_{ab}=\mathbb E[\phi_j(Z_a)\phi_j(Z_b)],\quad
Z\sim N(0,Q^{(j-1)}),
\qquad\gamma=\lambda_{\min}(Q^{(L)})>0,\quad\lambda=\gamma/m.
\tag{3}
\]
Every population diagonal is \(q_j\), including when intermediate
covariances are singular. In particular \(\lambda\le H^2/m\le H^2\).

The constants specifying the new width are
\[
R=2H,\quad K=b+sR,\quad D=2sb+4s^2R,\quad
T_1=\sum_{i=0}^{L-1}s^i,\quad T_2=\sum_{i=0}^{L-1}s^{2i},
\]
\[
C=T_2(2K+1+DT_1),\qquad
\varepsilon=\min\left\{\frac1{8T_1},\frac{\gamma}{2mC}\right\},
\qquad h=\min\left\{\frac12,\frac{H}{4(8s)^L}\right\}.
\tag{4}
\]
For \(0<\delta<1\), put
\[
\Xi=\log\frac{16L(m+1)^2}{\delta}+d\log(1+2/h),
\]
\[
N_{\mathrm{fit}}(\delta)=\left\lceil\max\left\{
1,\ \frac{\log(8L/\delta)}{8-2\log9},\
\frac{d\log9+\log(8/\delta)}{8-\log9},\
\frac{32s^2R^2\Xi}{\varepsilon^2}
\right\}\right\rceil.
\tag{5}
\]
All denominators are positive. For every individual integer
\(n\ge N_{\mathrm{fit}}(\delta)\), an event of probability at least
\(1-\delta\), depending only on the initialized network and training inputs,
has the following properties:
\[
\|A_0\|_{\rm op}/\sqrt n\le8,\qquad
\max_{j\ge2}\|W_0^{(j)}\|_{\rm op}\le8,\qquad
\sup_{\|v\|=1,j}\|h_0^{(j)}(v)\|_2/\sqrt n\le3H/2,
\]
\[
\lambda_{\min}\left(\frac{\mathsf H_0^\top\mathsf H_0}{mn}\right)
\ge\lambda/2,\qquad
\mathsf H(t)=[h^{(L)}(t,v_1),\ldots,h^{(L)}(t,v_m)].
\tag{6}
\]

Define the original fitting coefficients, without enlargement:
\[
D_j=s(9s)^{L-j},\quad U_1=D_1,\quad U_j=2HD_j\ (j\ge2),
\quad F_1=sU_1,\quad F_j=s(2HU_j+9F_{j-1}),
\]
\[
F=F_L=s^2\left[(9s)^{2L-2}+4H^2\sum_{i=0}^{L-2}(9s)^{2i}\right].
\tag{7}
\]
On the same event, simultaneously for every deterministic label vector with
\[
Y=\|y\|_2/\sqrt m\le\frac{\gamma}{8mH\sqrt F},
\tag{8}
\]
the original gradient flow exists globally, all parameters converge, and
the limiting prediction interpolates every training label. The full source
and compact-runtime label restrictions may be intersected with (8) without
changing this result; no stronger simple power cap is substituted for them.
For \(Y>0\), uniformly in physical time,
\[
\begin{gathered}
\|A(t)\|_{\rm op}/\sqrt n<9,\quad
\max_{j\ge2}\|W^{(j)}(t)\|_{\rm op}<9,\quad
\sup_{\|v\|=1,j}\|h^{(j)}(t,v)\|_2/\sqrt n<2H,\\
\lambda_{\min}(\mathsf H(t)^\top\mathsf H(t)/(mn))\ge\lambda/4,
\qquad\rho(t):=\|f_n(t,v_a)-y_a\|_2/\sqrt m\le Ye^{-\lambda t/2}.
\end{gathered}
\tag{9}
\]
The norm in the definition of \(\rho\) is over the sample index. The
whole-sphere endpoint bound is
\[
\sup_{\|v\|=1}|f_n(\infty,v)-f_n(t,v)|
\le\frac{65}{4}H^2\frac Y\lambda e^{-\lambda t/2}.
\tag{10}
\]
For \(Y=0\), zero readout gives the stationary zero predictor exactly.
There is no lower bound on \(Y\) in this dense-fitting theorem.

For the activation envelope used in the current study,
\[
\beta=\max\left\{10,1+b,16/a,
\max_{j,1\le k\le2}\sup_{|\operatorname{Im}z|<a/2}
|\phi_j^{(k)}(z)|\right\},
\tag{11}
\]
the explicit gate (5) satisfies the convenient loose envelope
\[
N_{\mathrm{fit}}(\delta)\le
\left\lceil\beta^{32L}(1+m/\gamma)^2
\left[dL\log\beta+\log\frac{16L(m+1)^2}{\delta}\right]\right\rceil.
\tag{12}
\]
Thus depth occurs through a fixed power of \(\beta^L\), rather than
\(\beta^{cL^2}\), and sphere coverage costs linearly in \(d\) inside
the bracket. Neither \(m\ge d\) nor nonsingular intermediate covariances
is needed in the proof, though the requested data class is retained.

## 2. A Gaussian norm estimate, including its proof

If \(G\) is a standard Gaussian vector and \(F(G)\ge0\) is an
\(a_0\)-Lipschitz function, then
\[
\Pr\{|F-\mathbb EF|>t\}\le2e^{-t^2/(2a_0^2)},\quad
\operatorname{Var}(F)\le a_0^2,\quad
0\le\sqrt{\mathbb EF^2}-\mathbb EF\le a_0.
\tag{13}
\]
When \(a_0=0\) the function is constant and the conclusions have their
literal deterministic interpretation. Consequently, if
\(\varepsilon\ge2a_0\),
\[
\Pr\{|F-\sqrt{\mathbb EF^2}|>\varepsilon\}
\le2\exp[-\varepsilon^2/(8a_0^2)].
\tag{14}
\]

Here is a self-contained justification of the Gaussian ingredient. Let
\(P_tg(x)=\mathbb E g(e^{-t}x+\sqrt{1-e^{-2t}}G)\). Gaussian integration
by parts, applied to its generator \(\Delta-x\cdot\nabla\), gives
\[
\operatorname{Ent}_\gamma(g)
=\int_0^\infty\mathbb E_\gamma
\frac{|\nabla P_tg|^2}{P_tg}\,dt
\le\int_0^\infty e^{-2t}\mathbb E_\gamma
P_t\left(\frac{|\nabla g|^2}{g}\right)dt
=\frac12\mathbb E_\gamma\frac{|\nabla g|^2}{g}.
\]
The inequality uses \(\nabla P_tg=e^{-t}P_t\nabla g\) and weighted
Cauchy--Schwarz; Gaussian invariance gives the last equality. The entropy
identity follows by differentiating \(\mathbb E(P_tg\log P_tg)\), then
integrating from zero to infinity, where \(P_tg\) tends to its mean.
It holds first for bounded positive smooth functions, and truncation and
Gaussian domination extend it to exponentials of Lipschitz functions.
For \(g=e^{uF}\), writing \(\psi(u)=\log\mathbb Ee^{uF}\), it gives
\(u\psi'(u)-\psi(u)\le u^2a_0^2/2\). Integration of
\((\psi(u)/u)'\), and the same argument for \(-F\), give
\(\log\mathbb Ee^{u(F-\mathbb EF)}\le u^2a_0^2/2\).
Chernoff minimization proves the tails, and the second derivative at zero
gives the variance bound. Finally
\(\mathbb EF^2=(\mathbb EF)^2+\operatorname{Var}(F)\) proves the bias
bound. Lipschitz functions can be smoothed before these steps and recovered
by dominated convergence.

Suppose \((Z_{ia},Z_{ib})\), \(1\le i\le n\), are independent centered
Gaussian pairs whose covariance diagonals are at most \(R^2\). The
empirical norm
\[
\left(n^{-1}\sum_i\phi(Z_{ia})^2\right)^{1/2}
\]
is \(sR/\sqrt n\)-Lipschitz in standard Gaussian roots. Its mean square
is exactly \(\mathbb E\phi(Z_a)^2\). The corresponding norms of
\(\phi(Z_{ia})+\phi(Z_{ib})\) and
\(\phi(Z_{ia})-\phi(Z_{ib})\) are each
\(2sR/\sqrt n\)-Lipschitz: the pair covariance has operator norm at
most \(2R^2\), the scalar sum or difference has gradient norm at most
\(\sqrt2s\), and taking an empirical Euclidean norm divides the result
by \(\sqrt n\). This also works for singular pair covariance matrices.

If each of these last two empirical norms is within \(\varepsilon\le1\)
of its population root mean square, polarization and
\(\|\phi(Z_a)\pm\phi(Z_b)\|_{L^2}\le2K\) give
\[
\left|n^{-1}\sum_i\phi(Z_{ia})\phi(Z_{ib})
-\mathbb E\phi(Z_a)\phi(Z_b)\right|
\le2K\varepsilon+\varepsilon^2/2
\le(2K+1)\varepsilon.
\tag{15}
\]
Indeed the two squared-norm errors are each at most
\((4K+\varepsilon)\varepsilon\), and polarization divides their sum
by four. By (14), each norm test fails with probability at most
\(2\exp[-n\varepsilon^2/(32s^2R^2)]\), provided
\(n\ge16s^2R^2/\varepsilon^2\). The gate (5) implies this prerequisite.

## 3. Propagating variances separately avoids depth-squared powers

The population RMS map
\[
g_j(\sigma)=\left(\mathbb E\phi_j(\sigma G)^2\right)^{1/2}
\]
obeys
\[
|g_j(\sigma)-g_j(\sigma')|\le s|\sigma-\sigma'|,
\tag{16}
\]
by the reverse triangle inequality in Gaussian \(L^2\), using the same
scalar root \(G\). No lower variance bound is needed.

For centered Gaussian covariances \(C,C'\), both with diagonal entries at
most \(R^2\), write
\(\sigma_a=\sqrt{C_{aa}}\), \(\sigma'_a=\sqrt{C'_{aa}}\), and
\(\Delta=\max_i|\sigma_i-\sigma'_i|\). Define
\(\Psi_j(C)_{ab}=\mathbb E\phi_j(Z_a)\phi_j(Z_b)\). Then
\[
|\Psi_j(C)_{ab}-\Psi_j(C')_{ab}|
\le s^2|C_{ab}-C'_{ab}|+(2sb+4s^2R)\Delta.
\tag{17}
\]
To prove this without dividing by a possibly vanishing variance, first
consider positive variances and put
\(\tau_a=\min(\sigma_a,\sigma'_a)\),
\(\tau_b=\min(\sigma_b,\sigma'_b)\). Shrinking both Gaussian pairs to
these same marginal standard deviations, preserving each correlation,
costs in total at most
\[
sK(|\sigma_a-\sigma'_a|+|\sigma_b-\sigma'_b|)\le2sK\Delta.
\]
This follows by subtracting one product factor at a time and applying
Cauchy--Schwarz with \(\|\phi(\sigma G)\|_{L^2}\le K\).

Let the original correlations be \(\rho,\rho'\). Gaussian integration
by parts at fixed positive marginal variances gives
\[
\frac{d}{d\rho}\mathbb E\phi_j(\tau_aG_1)\phi_j(\tau_bG_2)
=\tau_a\tau_b\mathbb E\phi'_j(\tau_aG_1)\phi'_j(\tau_bG_2),
\]
where the pair has correlation \(\rho\). The formula follows by
differentiating the nonsingular Gaussian density and integrating its mixed
second derivative against the product. Linear growth and bounded
derivatives justify both integrations. Integration over correlations and
dominated convergence extend it to the endpoints \(\rho=\pm1\).
Its modulus is at most \(s^2\tau_a\tau_b\).
Writing \(p=\sigma_a\sigma_b\), \(p'=\sigma'_a\sigma'_b\), direct
subtraction, with the larger of \(p,p'\) in the denominator, gives
\[
\tau_a\tau_b|\rho-\rho'|
\le|C_{ab}-C'_{ab}|+|p-p'|
\le|C_{ab}-C'_{ab}|+2R\Delta.
\]
For example, if \(p\ge p'\), the first bound follows from
\(\rho-\rho'=(C_{ab}-C'_{ab})/p+C'_{ab}(1/p-1/p')\),
\(|C'_{ab}|\le p'\), and \(\tau_a\tau_b\le p\).
Adding the scaling and correlation costs proves (17). Zero variances
follow by continuity, or directly because the corresponding \(\tau\)
vanishes. This proof explains why the coefficient multiplying the entry
error is \(s^2\); the larger feature bound multiplies only the separate
standard-deviation error.

## 4. Conditional layer concentration and the sphere net

Choose an \(h\)-net of the real unit sphere with cardinality
\(P\le(1+2/h)^d\). A maximal separated set has this bound by the
disjoint-ball volume argument. Track the individual empirical RMS norms
at all training points and net points. At each layer also test the two
polarization norms for every training pair. There are at most
\(3m^2+P\) tests per layer.

Conditioned on all preceding initialized layers, the next layer has
independent Gaussian rows whose covariance is the previous empirical
feature Gram. Let \(\Delta_j\) be the maximum individual RMS error from
\(\sqrt{q_j}\) on the training points and net, and let \(E_j\) be the
maximum training covariance-entry error from \(Q^{(j)}\). Initially
\(\Delta_0=E_0=0\). If all tests so far pass, (15)--(17) imply
\[
\Delta_j\le\varepsilon+s\Delta_{j-1},\qquad
E_j\le(2K+1)\varepsilon+s^2E_{j-1}+D\Delta_{j-1}.
\tag{18}
\]
Therefore
\[
\Delta_j\le\varepsilon T_1\le1/8,\qquad
E_j\le\varepsilon T_2(2K+1+DT_1)=\varepsilon C
\le\gamma/(2m).
\tag{19}
\]
The conditional input standard deviations are consequently at most
\(H+1/8<R\), which closes the prerequisite for the next layer's tests.
This is a stopped conditional union bound: no independence between layers,
training pairs, or net points is asserted.

The probability of any failed test before this induction closes is at most
\[
2L(3m^2+P)\exp[-n\varepsilon^2/(32s^2R^2)]\le\delta/2,
\tag{20}
\]
because \(3m^2+P\le4(m+1)^2P\) and the definition of \(\Xi\) has
additional slack. The initial operator estimates obtained from two
one-quarter sphere nets are
\[
\Pr\{\|W_0^{(j)}\|_{\rm op}>8\}
\le2e^{-(8-2\log9)n},\qquad
\Pr\{\|A_0\|_{\rm op}/\sqrt n>8\}
\le2e^{-(8-\log9)n+d\log9}.
\tag{21}
\]
For completeness, the net bound is
\(\|M\|_{\rm op}\le2\max_{u,v\text{ in nets}}|u^\top Mv|\).
At the indicated threshold each scalar Gaussian tail has exponent
\(-8n\), while the nets have sizes \(9^{2n}\) or \(9^{n+d}\).
The second and third gates in (5) make the union of (21) less than
\(\delta/2\).

On the operator event, \(v\mapsto h_0^{(j)}(v)/\sqrt n\) is
\((8s)^j\)-Lipschitz. Its net norms are at most \(H+1/8\), and its
off-net norm increment is at most \((8s)^Lh\le H/4\). Thus every sphere
norm is at most \(11H/8<3H/2\). The final covariance error has operator
norm at most \(mE_L\le\gamma/2\), giving the last line of (6).
This proves (5)--(6).

To check (12), linear growth gives \(H\le(2\beta)^L\le\beta^{2L}\).
For \(L\ge2\), the explicit bounds
\[
R,K\le\beta^{3L},\quad D\le\beta^{4L},\quad
T_1\le\beta^{2L},\quad T_2\le\beta^{3L},\quad C\le\beta^{10L},
\quad\varepsilon^{-1}\le\beta^{11L}(1+m/\gamma)
\]
follow by their finite sums and \(L\le\beta^L\). Also
\(32s^2R^2\le\beta^{8L}\), and
\(\log(1+2/h)\le3L\log\beta\). Hence the concentration term in (5)
is at most \(\beta^{31L}(1+m/\gamma)^2\) times the bracket in (12).
The two operator terms and the ceiling are covered by the displayed
\(\beta^{32L}\) envelope. This is a parameter-uniform numerical bound.

## 5. Deterministic fitting with exactly the existing label allowance

For the residuals \(r_a=f_n(v_a)-y_a\), use
\[
\delta_a^{(L)}=w\odot\phi'_L(z_a^{(L)}),\qquad
\delta_a^{(j)}=\phi'_j(z_a^{(j)})\odot
W^{(j+1)\top}\delta_a^{(j+1)}.
\]
The loss is \(\mathcal L=m^{-1}\sum_ar_a^2=\rho^2\). The original
mobilities give exactly
\[
\dot A=-\frac2m\sum_ar_a\delta_a^{(1)}v_a^\top,\quad
\dot W^{(j)}=-\frac2{mn}\sum_ar_a\delta_a^{(j)}h_a^{(j-1)\top},
\quad\dot w=-\frac2m\sum_ar_ah_a^{(L)}.
\tag{22}
\]
For parameters or parameter differences define
\[
\|\theta\|_{\rm par}^2=\|A\|_F^2/n+
\sum_{j=2}^L\|W^{(j)}\|_F^2+\|w\|_2^2/n.
\]
Stop at a first possible exit from operator caps nine, sphere feature cap
\(2H\), or normalized top Gram gap \(\lambda/4\). Backward recursion
then gives \(\|\delta_a^{(j)}\|_2/\sqrt n\le D_j\|w\|_2/\sqrt n\).
Sample Cauchy--Schwarz in (22) bounds the normalized Frobenius speed of
each hidden block by \(2\rho U_j\|w\|_2/\sqrt n\).

The energy identity and the readout contribution imply
\[
-\frac d{dt}\rho^2=\|\dot\theta\|_{\rm par}^2,
\qquad -\frac d{dt}\rho^2\ge\lambda\rho^2.
\tag{23}
\]
Indeed \(\|\dot w\|_2^2/n=4r^\top\mathsf H^\top\mathsf H r/(m^2n)
\ge\lambda\rho^2\). Thus the claimed residual decay and
\(\int\rho\le2Y/\lambda\) hold up to stopping. Weighted
Cauchy--Schwarz, while \(\rho>0\), gives
\[
\left(\int\|\dot\theta\|_{\rm par}\right)^2
\le\left(\int\frac{\|\dot\theta\|_{\rm par}^2}{\rho}\right)
\left(\int\rho\right)
\le(2Y)(2Y/\lambda).
\tag{24}
\]
If \(\rho\) reaches zero, every velocity is zero and continuation is
constant. Since \(w_0=0\), (24) bounds its RMS norm by
\(2Y/\sqrt\lambda\). Integrating the hidden speeds consequently gives
\[
\|A(t)-A_0\|_F/\sqrt n\le8U_1Y^2/\lambda^{3/2},\qquad
\|W^{(j)}(t)-W_0^{(j)}\|_F\le8U_jY^2/\lambda^{3/2}.
\tag{25}
\]
Subtracting forward passes gives a first-layer feature bound equal to
\(s\|A(t)-A_0\|_F/\sqrt n\), and at every later layer bounds the RMS
feature change by
\[
s\left[2H\|W^{(j)}(t)-W_0^{(j)}\|_F+
9\|h^{(j-1)}(t,v)-h_0^{(j-1)}(v)\|_2/\sqrt n\right].
\]
The recurrence (7) therefore proves, uniformly on the sphere,
\[
\|h^{(j)}(t,v)-h_0^{(j)}(v)\|_2/\sqrt n
\le8F_jY^2/\lambda^{3/2}.
\tag{26}
\]
The explicit formula in (7) implies \(F\ge1,U_j,F_j\). The original
condition (8) gives
\[
8FY^2/\lambda^{3/2}\le\sqrt\lambda/(8H^2)\le1/(8H).
\tag{27}
\]
Thus operator caps improve to \(8+1/8\), and feature caps improve to
\(3H/2+H/8<2H\). The operator change in
\(\mathsf H/\sqrt{mn}\) is at most \(\sqrt\lambda/(8H^2)\le
\sqrt\lambda/8\). Its least singular value remains at least
\(\sqrt\lambda(1/\sqrt2-1/8)>\sqrt\lambda/2\), strictly improving
the stopped Gram boundary. A finite first exit is impossible.

At each fixed finite width the vector field is locally Lipschitz. The
bounded parameter path length in (24) prevents finite-time escape and
gives parameter convergence. Residual decay proves interpolation.
Finally (22) gives \(\|\dot w\|_2/\sqrt n\le4H\rho\); the
instantaneous version of (26) gives
\(\|\dot h^{(L)}(v)\|_2/\sqrt n\le2\rho F\|w\|_2/\sqrt n\).
The product rule then gives
\[
|\dot f_n(t,v)|\le8(H^2+FY^2/\lambda)\rho(t).
\]
Integration and \(FY^2/\lambda\le1/64\le H^2/64\) prove (10).
The event was chosen before the labels, so the deterministic argument
works on that event for every label vector satisfying (8).

## 6. What this does and does not quantify for the analytic source

The fitting and trained-source events are different. The preceding proof
quantifies initialized operator norms, sphere RMS norms, the training Gram
gap, global dense fitting, and the parameter and prediction tails. It does
not use a cavity or trained-coordinate moment theorem.

Even the initial source exponential budgets can be quantified. Use the
source note's \(\eta_{\rm src}\), \(\mathcal B=1024e^2L\), and
\(H_{\max}\). Its displayed recurrences imply \(H\le H_{\max}\),
\(W_{\rm G}\ge128H_{\max}\), and
\(\eta_{\rm src}\le(1024C_{\rm abs}W_{\rm G})^{-1}\), hence
\(\eta_{\rm src}R\le1\). Conditional on earlier layer norm success,
each initialized preactivation is \(N(0,\sigma^2)\), \(\sigma\le R\),
and
\[
\mathbb Ee^{\eta_{\rm src}|Z|}\le2e^{1/2}<4,\qquad
\mathbb Ee^{2\eta_{\rm src}|Z|}\le2e^2<15.
\]
Chebyshev makes the probability that its layer average exceeds eight at
most \(15/(16n)\). A stopped union over \(mL\) layer/sample pairs
therefore bounds every initial sample budget by \(8L<\mathcal B/2\),
with additional failure at most \(15mL/(16n)\). Combining
\(N_{\mathrm{fit}}(\delta/2)\) and \(n\ge2mL/\delta\) gives this
additional initial event with total failure less than \(\delta\).
All initial carriers are exactly zero. Similarly, initial training
preactivation maxima have threshold
\(R\sqrt{2\log(4nLm/\delta)}\) and additional failure at most
\(\delta/2\). These elementary initial estimates do not transfer
themselves to the trained or cavity trajectories.

The inherited source needs the much stronger running carrier estimate
\[
\max_{a,j,i}|k_{a,i}^{(j)}(z)|
\le K_{\rm src}S\sqrt{\log(en)},\qquad S=16Y/\lambda,
\tag{28}
\]
on a complex-time neighborhood, plus the stopped insertion and joint-budget
events supplying it. Fitting alone supplies only an RMS carrier bound; its
conversion to coordinates costs \(\sqrt n\), not \(\sqrt{\log n}\).
It therefore cannot be inserted into the Taylor-source argument in place
of (28) without changing that argument and its costs.

The precise unresolved stochastic step is visible in the assigned source
proof. For each fixed positive integer \(p\) it proves
\[
\limsup_{n\to\infty}\Pr\{\text{a training joint budget is hit}\}
\le mL(16L/\mathcal B)^p.
\tag{29}
\]
Taking the width limit first, and then the infimum over fixed \(p\),
proves probability tending to one for fixed problem data. It supplies no
finite-width remainder. A confidence theorem would need, for example,
\[
\Pr\{\text{budget hit or insertion failure}\}
\le mL(16L/\mathcal B)^p+\mathcal R_p(n;
m,d,L,\gamma,Y,\phi_1,\ldots,\phi_L),
\tag{30}
\]
with an explicit bound on \(\mathcal R_p\) at
\(p\ge\log(2mL/\delta)/\log(\mathcal B/(16L))\). The permitted inputs
do not give that bound. In particular they retain only asymptotic local
coordinate insertion errors \(O_p(n^{-1/30})\), unspecified fixed-deletion
coefficients in projected common-cavity Gaussian radii
\(C_pn^{-49/100}\), unspecified finite collision-moment constants, and
superpolynomial local-exception statements without parameter dependence.
Here the subscript \(p\) on a coefficient denotes dependence on deletion
or moment order; the source's \(O_p\) notation also indicates probabilistic
control and cannot be read as a uniform numerical constant.

The finite-query localization removes the dimension factor from its
Gaussian query mesh, but preserves exactly (29). Its displayed
\(4n^{10}e^{-1024\log(en)}\) term is only the Gaussian mesh component;
it does not bound the missing insertion/common-cavity remainder. The
all-time analytic extension is deterministic conditional on the source
event and introduces no new probability. The Taylor-source proof is also
conditional on that event. None of these statements supplies (30).

There is also an explicit deterministic issue distinct from (30). For
the physical radius \(c/\sqrt{\log(en)}\), the finite-query source retains
\[
n^{-1}\le Y,\qquad
\sqrt{\log(en)}\ge c\max\{8,\lambda,4\mathcal K/\log2,32YSD_W\}.
\tag{31}
\]
At its chosen \(c=\chi(S)/\lambda\), the second inequality can demand
an exponentially large width. This is a sufficient-radius gate, not a
lower bound on the width at which the network or source must work. The
same assigned theorem explicitly allows every smaller
\(0<c\le a/(64YSU_{\rm fin}(S))\). Thus the independent choice
\[
M=\max\{8,\lambda,4\mathcal K/\log2,32YSD_W\},\qquad
c=\min\{a/(64YSU_{\rm fin}(S)),1/M\}
\tag{32}
\]
makes the second gate in (31) automatic for \(n\ge1\). In normalized
time, the inverse radius is
\[
\frac{\sqrt{\log(en)}}{\lambda c}
=\max\left\{\frac{4S^2U_{\rm fin}(S)}a,\frac M\lambda\right\}
\sqrt{\log(en)}.
\tag{33}
\]
The accounting note's full-label power ledger bounds this by
\(\beta^{CL}(1+\lambda^{-1})\sqrt{\log(en)}\) for a numerical exponent
\(C\). This observation does not quantify (30), and the separate
\(n^{-1}\le Y\) construction gate remains as written. Arbitrarily small
positive labels therefore preclude a width bound independent of \(Y\)
for that unchanged gate, although the dense-fitting theorem proved here
has no such restriction. Removing the gate requires a separate justified
change to the source construction, not a stronger label assumption.

The precise completed claim is (5)--(12). An explicit polynomial success
width for the complete inherited analytic source or unseen-query decoder
is still unproved within the assigned inputs. This is a missing quantitative
bridge, not a counterexample to the existence of such a width theorem.

## 7. Scope and provenance

Complete scientific inputs read were the expressly assigned integrated
notes `GENERAL_EXPLICIT_FITTING.md`, `UNBOUNDED_COMPRESSOR_BRIDGE.md`,
`GENERAL_TRAJECTORY_LOWER_BRIDGE.md`, and `ANALYTIC_TAIL_EXTENSION.md`, and
the current study's `PHYSICAL_PARAMETER_ACCOUNTING.md` and
`SANE_TAYLOR_SOURCE.md`. Their links to other research were not followed.
The canonical-notation skill and its neural-network reference, the
rigorous-math skill, and the conjecture skill's adversarial-audit guidance
were read. The present note is a new scoped derivation, not an independent
review of the full decoder. Its only write is this assigned artifact.
