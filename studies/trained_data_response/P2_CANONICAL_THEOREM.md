#### C.4.7. Nonlinear training near the fitted tanh reference

The infinitesimal response in C.4.6 describes actual finite-network
derivatives at the fitted reference. We now construct the nearby nonlinear
population trajectories through the substantial-training time 40, identify
their actual finite GF, and prove that the same response approximates finite
contaminations to first order. The new estimate controls named source
coefficients along raw Euler programs on a positive neighborhood of laws.
Its constants do not depend on how many atoms approximate a law or on their
smallest mass.

##### C.4.7.1. Model, theorem and observation contract

Fix \(Y\ge1\), \(T=40\), and
\[
 \mathcal Z=\sqrt2S^1\times[-Y,Y],\qquad
 d_{\mathcal Z}((x,y),(x',y'))=|x-x'|/\sqrt2+|y-y'|.
\]
Write \(\mathcal W_1\) for this Wasserstein distance and \(u=x/\sqrt2\).
Use exactly the two-hidden-layer tanh model of C.4: no biases, equal hidden
widths, stored independent centered Gaussian variances \((1,1/n,1/n^2)\),
and mobilities \((n,1,n)\) for the unhalved loss
\(\mathcal L_\mu=\int(f_n(x)-y)^2\,d\mu(x,y)\). Thus
\[
 h_n^{(1)}=\tanh(W_n^{(1)}u),\quad
 h_n^{(2)}=\tanh(W_n^{(2)}h_n^{(1)}),\quad
 f_n(x)=(W_n^{(3)})^Th_n^{(2)}/n.
\]
Every finite Borel-law loss integral is exact. The actual finite initial
readout is retained. The opposite-label reference is
\[
 \nu_*=\tfrac12\delta_{(\sqrt2e_1,+1)}
             +\tfrac12\delta_{(\sqrt2e_2,-1)}.
\]

On the common canonical Gaussian carrier of III.F and C.4, use the typed
aliases \(w=W^{(1)}\), \(A=W^{(2)}=A_0+K\), \(c=W^{(3)}\), and put
\(H_\ell=L^2(\Omega_\ell)\) for the two layer Hilbert spaces. Define
\[
 \mathcal E=L^2(\Omega_1;\mathbb R^2)
       \oplus\mathcal S_2(L^2(\Omega_1),L^2(\Omega_2))
       \oplus L^2(\Omega_2),\qquad \theta=(w,K,c),
\]
\[
 \|\theta-\bar\theta\|_{\rm raw}^2
   =\|w-\bar w\|_2^2+\|K-\bar K\|_{\rm HS}^2+\|c-\bar c\|_2^2.
\]
Only the learned increment K is Hilbert–Schmidt. Retain the initialized
Gaussian action \(A_0\) and its actual Hilbert adjoint, both with their
joint coordinate realization. The prescribed initialization is
\(\theta(0)=(g,0,0)\), \(g\sim N(0,I_2)\).
For \(\phi=\tanh\), define at each state
\[
 H^{(1)}(u)=\phi(w\cdot u),\quad Z^{(2)}(u)=AH^{(1)}(u),\quad
 H^{(2)}(u)=\phi(Z^{(2)}(u)),\quad f(u)=\langle c,H^{(2)}(u)\rangle,
\]
\[
 \Delta^{(2)}(u)=c\phi'(Z^{(2)}(u)),\quad Q(u)=A^*\Delta^{(2)}(u),
 \quad r(u,y)=f(u)-y.
\]
All population pairings contract within the indicated layer. A rank
\(a\otimes b\) sends \(v\) to \(a\langle b,v\rangle\).

**Theorem.** There is \(\delta_Y>0\), independent of width and sample
count, such that the following hold on
\[
 U_Y=\{\mu\in\mathcal P(\mathcal Z):
                         \mathcal W_1(\mu,\nu_*)<\delta_Y\}.
\]
This neighborhood is relative to all probability laws on \(\mathcal Z\).
It imposes no atom-count, minimum-weight, angle, Gram-rank or prescribed
label-function condition.

1. **Strong autonomous training and reached restart.** Each \(\mu\in U_Y\)
   has a solution \(\theta_\mu\in C^1([0,40];\mathcal E)\), with one-sided
   endpoint derivatives, of
   \[
   \theta'_\mu=\mathcal F_\mu(\theta_\mu)
   =-2\left(\int r\phi'(w\cdot u)Q(u)u\,d\mu,
       \int r\Delta^{(2)}(u)\otimes H^{(1)}(u)\,d\mu,
       \int rH^{(2)}(u)\,d\mu\right).
   \tag{NF}
   \]
   These are Bochner integrals in the three raw spaces. The solution is
   unique among strong raw solutions on the same prescribed carrier with
   the same initialization and retained Gaussian primitives. For every
   \(s\in[0,40]\), its restriction to \([s,40]\) is the unique strong
   continuation from its reached state under the same law and primitives.
   No well-posedness from an arbitrary ambient operator state is asserted.
   The constructed path satisfies
   \[
   \mathcal L_\mu(t)+\int_0^t\|\theta'_\mu(v)\|_{\rm raw}^2\,dv
         =\mathcal L_\mu(0)\le Y^2,\qquad
   \|c_\mu(t)\|_\infty\le2Yt.
   \tag{NG}
   \]
   Query tails and weighted moments used below are proved for these
   trajectories; they are not conditions imposed on competing solutions.

2. **Law continuity.** There are \(C_Y,a_Y,q_Y>0\) such that, for
   \(q=\mathcal W_1(\mu,\rho)\le q_Y\) and \(\mu,\rho\in U_Y\),
   \[
   \sup_{t\le40}\|\theta_\mu(t)-\theta_\rho(t)\|_{\rm raw}
             \le C_Yq^{a_Y}.
   \tag{NL}
   \]
   In particular \(\sup_{t\le40,x}|f_\mu(t,x)-f_\rho(t,x)|
   \le\Omega_Y(q)\), where \(\Omega_Y(q)=C_Yq^{a_Y}\) at small q and
   a sufficiently large constant at larger q. Thus \(\Omega_Y(q)\to0\).

3. **Actual finite GF and arbitrary sampling/width limits.** For each
   fixed Borel \(\mu\in U_Y\), actual finite GF exists globally and
   \[
   \sup_{t\le40,x}|f_{n,\mu}(t,x)-f_\mu(t,x)|\longrightarrow0
                                    \quad\hbox{in probability}.
   \tag{NW1}
   \]
   More generally, for every deterministic sequence of empirical laws
   \(\lambda_k\to\mu\) in \(\mathcal W_1\) and every \(n_k\to\infty\),
   \[
   \sup_{t\le40,x}|f_{n_k,\lambda_k}(t,x)-f_\mu(t,x)|
       \longrightarrow0\quad\hbox{in probability}.
   \tag{NW2}
   \]
   The same holds in joint probability for iid samples of any sizes
   \(m_k\to\infty\), independent of initialization. No relative
   sample-count/width rate is required. State and action identification
   has the precise approximation and observation meaning below.

4. **Nonlinear approximation by the C.4.6 response.** For any probability
   law \(\nu\) on \(\mathcal Z\), put \(\sigma=\nu-\nu_*\) and
   \(\mu_\epsilon=(1-\epsilon)\nu_*+\epsilon\nu\). Take
   \[
   \epsilon_Y=\min\{1/2,\delta_Y/[2(2+2Y)]\}.
   \]
   Then \(\mu_\epsilon\in U_Y\) for \(0\le\epsilon\le\epsilon_Y\).
   With exactly the finite-first response
   \(D_\sigma f=\mathscr D_\sigma f\) of C.4.6,
   there is a deterministic modulus \(\omega_Y(\epsilon)\to0\),
   uniform over all \(\nu\), such that
   \[
   \sup_{t\le40,x}|f_{\mu_\epsilon}(t,x)-f_{\nu_*}(t,x)
                       -\epsilon D_\sigma f(t,x)|
                \le\epsilon\omega_Y(\epsilon).
   \tag{NR}
   \]
   The analogous raw-state remainder holds with the raw variation
   obtained from C.4.6's clock tangent. With common initialization across
   epsilon, let \(D_\sigma f_n=\partial_{\epsilon+}
   f_{n,\mu_\epsilon}|_{\epsilon=0}\) be the actual finite GF derivative.
   For every separately fixed \(\nu\) and every \(a>0\),
   \[
   \lim_{\epsilon\downarrow0}\limsup_{n\to\infty}
   \Pr\!\left[
    \frac{\sup_{t\le40,x}|f_{n,\mu_\epsilon}-f_{n,\nu_*}
                         -\epsilon D_\sigma f_n|}{\epsilon}>a
   \right]=0.
   \tag{NB}
   \]
   Width is taken first at fixed positive epsilon. Neither a
   width-uniform finite-n remainder nor an arbitrary simultaneous
   epsilon/width rate is asserted.

For the state assertion, fix a target law and required accuracy. Choose a
finite comparison law and a finite raw Euler mesh, and hence one finite
oracle program, before taking width to infinity. The population program
approximates the path in the raw norm. Its realization on the actual
initialized arrays, including the actual initial readout additively,
approximates actual finite GF in the same-carrier distance
\[
 \|w_n-\bar w_n\|_F/\sqrt n+\|K_n-\bar K_n\|_F
                         +\|c_n-\bar c_n\|_2/\sqrt n.
\]
The approximation error can be made arbitrarily small, uniformly through
40, in probability in the stated order of choices. Learned increments
are finite sums of ranks at each oracle. Their HS norms and pairings are
identified by the finite double sums of the two same-layer Gram
contractions. A finite matrix is never subtracted from a population
operator on a different carrier.

An admitted observation starts with a finite list of raw w,c and named
\(H^{(1)},Z^{(2)},H^{(2)},\Delta^{(2)},Q\) fields at specified times
and inputs, together with identified initialized generated fields. It
uses finitely many correctly typed \(A_0,A_0^*,A(t),A(t)^*,K(t),K(t)^*\)
actions, continuous globally Lipschitz coordinate operations, and fixed
bounded continuous gates multiplying named \(L^2\) fields. Its joint
same-layer empirical law converges with second moments, equivalently in
\(\mathcal W_2\) for each finite tuple. Quadratic contractions and paired
initialized/current hidden observations are included. Arbitrary unbounded
coordinate products, nonlinear clocks and inverse-gate fields require
their own moment and approximation proofs. No cross-carrier operator-norm
convergence is claimed.

##### C.4.7.2. Raw bounds and the comparison estimate

Use the equivalent sum distance
\(d(\theta,\bar\theta)=\|w-\bar w\|_2+\|K-\bar K\|_{\rm HS}
+\|c-\bar c\|_2\). It lies between the raw norm and \(\sqrt3\) times
that norm. At finite width use the explicit normalized distance just
displayed. All comparisons share the same initialized primitives.

Every separately finite-law raw Euler program exists by recursion on the
canonical action spaces. Bounded gates preserve \(L^2\), and each middle
update is a Hilbert–Schmidt rank. For any mesh with nonnegative steps
\(\Delta_k\) summing to at most T, let \(C_k=\|c_k\|_\infty\). The
readout update gives
\(C_{k+1}+Y\le(1+2\Delta_k)(C_k+Y)\). Consequently, for
\(C_T=Y(e^{2T}-1)\), \(R_T=Y+C_T\), and a fixed
\(M_0\ge\|A_0\|_{\rm op}\),
\[
 \|c_k\|_\infty\le C_T,\quad
 \|K_k\|_{\rm HS}\le2TR_TC_T=:K_T,\quad
 \|A_k\|_{\rm op}\le M_0+K_T=:A_T,
\]
\[
 \|w_k\|_2\le\sqrt2+2TR_TA_TC_T,
 \qquad \|\mathcal F_\mu(\theta_k)\|_{(1)}
       \le2R_T(A_TC_T+C_T+1)=:V_T.
 \tag{NE}
\]
Here \(\|\cdot\|_{(1)}\) is the sum of the three raw component norms.
The affine interpolants obey the same bounds. Their crude constants are
finite at T=40 and independent of atom counts, weights and meshes; no
discrete energy inequality is used. The same calculation on finite arrays
works when the initial readout supremum is at most one and the initial
row RMS is at most two, with the corresponding enlarged constants.

At fixed width the exact Borel-law vector field is smooth: on each
finite-dimensional compact parameter set every derivative of its
integrand is bounded uniformly in the compact data domain, so
differentiation under the integral follows from the mean-value formula.
The field is the negative gradient in the metric with squared norm
\(\|v\|_F^2/n+\|B\|_F^2+\|d\|_2^2/n\). Thus
\[
 \mathcal L_\mu(t)+\int_0^t
 \bigl(\|\dot w_n\|_F^2/n+\|\dot K_n\|_F^2
                              +\|\dot c_n\|_2^2/n\bigr)\,ds
       =\mathcal L_\mu(0).
 \tag{NEF}
\]
On a finite maximal interval this bounds each parameter displacement by
\(\sqrt{t\mathcal L_\mu(0)}\), and bounds a terminal Cauchy increment
by \(\sqrt{|t-s|\mathcal L_\mu(0)}\). The finite endpoint and local
smoothness extend the solution, proving global finite existence and
uniqueness. On the initialization event
\(\|A_{0,n}\|_{\rm op}\le10\),
\(\|w_{0,n}\|_F/\sqrt n\le2\), \(\|c_{0,n}\|_\infty\le1\),
which has probability tending to one by the Gaussian estimates in C.4.6,
\(\mathcal L_\mu(0)\le(Y+1)^2\) for all laws. The finite raw states
through40 then lie on a common deterministic ball, and
\(\|c_n(t)\|_\infty\le1+2t(Y+1)\).

The same energy calculation gives (NG) for any already existing strong
population solution. For precision, the scalar prediction differential
has the three raw gradient blocks
\(\phi'(w\cdot u)Q(u)u\),
\(\Delta^{(2)}(u)\otimes H^{(1)}(u)\), and \(H^{(2)}(u)\).
The weighted Taylor argument in III.F.10 gives this scalar differential
without asserting Fréchet differentiability of an ambient activation map.
Bounded multiplier continuity, bounded actions and the rank norm identity
make this gradient jointly continuous in state and input. Compactness of
the input domain makes the continuity uniform near any fixed state: a
contrary sequence has a convergent input subsequence. The law integral is
therefore continuously differentiable, with gradient
\(2\int r\nabla f\,d\mu\). Pair it with (NF) and integrate to obtain
(NG). The readout bound follows pointwise from
\(\int|r|\,d\mu\le\sqrt{\mathcal L_\mu(t)}\le Y\).
These are a priori estimates for an existing path, not an existence
theorem from every raw endpoint.

For \(\tau_R(v)=\|v\mathbf1_{|v|>R}\|_2\), C.4.1's full-row
comparison strengthens to
\[
 \|\mathcal F_\mu(\theta)-\mathcal F_\rho(\bar\theta)\|_{(1)}
 \le C(1+R)\{d(\theta,\bar\theta)+\mathcal W_1(\mu,\rho)\}
       +C\left[\tau_R(\bar c)+\int\tau_R(\bar Q(u))\,d\rho\right]
 \quad(R\ge1).
 \tag{NC}
\]
The constant depends only on the common raw/action bounds and Y. Here is
the complete norm upgrade needed from that proof. Every action difference
uses \(\|K-\bar K\|_{\rm op}\le\|K-\bar K\|_{\rm HS}\). Every
middle-velocity difference is a sum of ranks, and
\[
 \|a\otimes b-\bar a\otimes\bar b\|_{\rm HS}
 \le\|a-\bar a\|_2\|b\|_2+\|\bar a\|_2\|b-\bar b\|_2.
\]
This is the same bound used for its operator norm in C.4.1. The only
unbounded gate products there use
\[
 \|[\phi'(z)-\phi'(\bar z)]P\|_2
                 \le2R\|z-\bar z\|_2+2\tau_R(P).
 \tag{NT}
\]
Split \(|P|\le R\) and its complement and use respectively
\(\operatorname{Lip}(\phi')\le2\) and bounded gates. The upper backward
subtraction applies (NT) to \(P=\bar c\); its error subsequently passes
through a bounded adjoint and bounded first gate. The additional lower
gate difference applies (NT) to \(P=\bar Q\). These errors add, so there
is one cutoff factor, not its square. Changing u costs
\(\|\bar w\|_2|u-v|\), as well as the explicit change of the first
gradient's final vector u. Coupling the laws and integrating gives (NC),
with tails only under the comparison marginal. This accounts for every
norm change in the complete C.4.1 proof. The identical normalized
finite-array calculation gives its same-width form.

Finally \(\mathcal F_\mu(\theta)\) is jointly continuous in raw state
and \(\mathcal W_1\) law. A bounded continuous multiplier converging in
measure converges strongly when applied to one fixed \(L^2\) field, by
truncating that field. This proves each backward-field continuity; the
forward actions and rank identity handle the other factors. Compactness
of the data domain again gives uniformity in data. A continuous
Banach-valued integrand G on that domain has compact separable range and
is Bochner integrable. Coupling at mean distance q gives the bound
\(\omega_G(b)+2\|G\|_\infty q/b\) for a law change: split transport
distances at b and use Markov's inequality. Send q to zero and then b to
zero. These facts justify the joint continuity claim and its use below.
