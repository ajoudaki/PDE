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
   \tag{C.4.7.NF}
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
   \tag{C.4.7.NG}
   \]
   Query tails and weighted moments used below are proved for these
   trajectories; they are not conditions imposed on competing solutions.

2. **Law continuity.** There are \(C_Y,a_Y,q_Y>0\) such that, for
   \(q=\mathcal W_1(\mu,\rho)\le q_Y\) and \(\mu,\rho\in U_Y\),
   \[
   \sup_{t\le40}\|\theta_\mu(t)-\theta_\rho(t)\|_{\rm raw}
             \le C_Yq^{a_Y}.
   \tag{C.4.7.NL}
   \]
   In particular \(\sup_{t\le40,x}|f_\mu(t,x)-f_\rho(t,x)|
   \le\Omega_Y(q)\), where \(\Omega_Y(q)=C_Yq^{a_Y}\) at small q and
   a sufficiently large constant at larger q. Thus \(\Omega_Y(q)\to0\).

3. **Actual finite GF and arbitrary sampling/width limits.** For each
   fixed Borel \(\mu\in U_Y\), actual finite GF exists globally and
   \[
   \sup_{t\le40,x}|f_{n,\mu}(t,x)-f_\mu(t,x)|\longrightarrow0
                                    \quad\hbox{in probability}.
   \tag{C.4.7.NW1}
   \]
   More generally, for every deterministic sequence of empirical laws
   \(\lambda_k\to\mu\) in \(\mathcal W_1\) and every \(n_k\to\infty\),
   \[
   \sup_{t\le40,x}|f_{n_k,\lambda_k}(t,x)-f_\mu(t,x)|
       \longrightarrow0\quad\hbox{in probability}.
   \tag{C.4.7.NW2}
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
   \tag{C.4.7.NR}
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
   \tag{C.4.7.NB}
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
 \tag{C.4.7.NE}
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
 \tag{C.4.7.NEF}
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

The same energy calculation gives (C.4.7.NG) for any already existing strong
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
\(2\int r\nabla f\,d\mu\). Pair it with (C.4.7.NF) and integrate to obtain
(C.4.7.NG). The readout bound follows pointwise from
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
 \tag{C.4.7.NC}
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
 \tag{C.4.7.NT}
\]
Split \(|P|\le R\) and its complement and use respectively
\(\operatorname{Lip}(\phi')\le2\) and bounded gates. The upper backward
subtraction applies (C.4.7.NT) to \(P=\bar c\); its error subsequently passes
through a bounded adjoint and bounded first gate. The additional lower
gate difference applies (C.4.7.NT) to \(P=\bar Q\). These errors add, so there
is one cutoff factor, not its square. Changing u costs
\(\|\bar w\|_2|u-v|\), as well as the explicit change of the first
gradient's final vector u. Coupling the laws and integrating gives (C.4.7.NC),
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

##### C.4.7.3. Uniform passive-query tails for raw Euler programs

Fix \(Y\ge1\), \(T=40\), the raw state \(\theta=(w,K,c)\),
\(A=A_0+K\), and the initialization \((g,0,0)\) stated above.
The aliases \(w=W^{(1)}\), \(A=W^{(2)}\), and \(c=W^{(3)}\)
retain their stated population types. Let
\(\lambda=\sum_a p_a\delta_{(\sqrt2u_a,y_a)}\), where
\(p_a>0\), \(\sum_a p_a=1\), \(|u_a|=1\), and \(|y_a|\le Y\).
Consider any finite raw Euler program with deterministic positive steps
\(h_k\), nodes \(t_k=\sum_{j<k}h_j\), and total length at most \(T\).
All residuals are its actual population residuals. Every named-source
derivative below freezes residuals, contractions, covariance laws, and
deterministic response coefficients; it differentiates only the named
coordinate expression. Throughout, \(\phi=\tanh\); unqualified \(L^p\)
norms use the population of their argument. Generic constants \(C\),
\(C_B\), and \(C_{B,p}\) may increase from one estimate to the next and
depend only on \(Y,T\), the fixed model, and the displayed cap and moment
order. The constants \(C_0,R_0\) defined in (C.4.7.N9) remain fixed.

For a passive query \(u\in S^1\), distinguish its one current forward
slot from the earlier training slots, and define
\[
 \mathcal B_k=\sup_{u\in S^1}
 \left\{|\beta_{ku,ku}|+\sum_{s<k,b}|\beta_{ku,sb}|\right\}.
 \tag{C.4.7.N1}
\]
The coefficients are defined below. Each row is obtained by appending a
fresh unused query to a finite program; earlier unused queries contribute
zero response coefficients. The deterministic row functions extend
continuously to the whole circle. The supremum in (C.4.7.N1) is outside every
expectation.

We prove that there are \(\rho>0\), \(h_0>0\), and \(B<\infty\),
depending only on \(Y,T\) and the fixed model, such that
\[
 \mathcal W_1(\lambda,\nu_*)<\rho,\qquad
 h_{\max}:=\max_k h_k\le h_0
 \quad\Longrightarrow\quad
 \sup_{k:t_k\le T}\mathcal B_k\le B.
 \tag{C.4.7.N-cap}
\]
The same constants work for every finite support cardinality, every
positive set of atom weights, every covariance rank, and every admitted
mesh. They will give constants \(a,M>0\) such that every recomputed
passive reverse query, including at affine Euler interpolation times,
satisfies \(\tau_R(Q(u))\le M e^{-aR^2}\) for \(R\ge1\).

The proof first obtains all moment and transport estimates under a
temporary cap. It reduces (C.4.7.N-cap) to a uniform coefficient bound for
reference raw Euler programs. A fresh-query estimate proves a cap for
the reference physical-clock Euler programs; differentiated consistency
transfers it to reference raw Euler. A second causal induction then
transfers that raw reference cap to all nearby finite laws. All constants
are finite; no useful numerical lower bound on \(\rho\) is asserted.

###### 1. Exact source equations and construction order

Set

\[
 m_{ka}=h_kp_a,\qquad \gamma_{ka}=-2m_{ka}r_{ka}.
\]

Use \(H^{(1)}_{ka}=\phi(w_k\cdot u_a)\), \(Z^{(2)}_{ka}=A_kH^{(1)}_{ka}\),
\(H^{(2)}_{ka}=\phi(Z^{(2)}_{ka})\), \(\Delta^{(2)}_{ka}=c_k\phi'(Z^{(2)}_{ka})\), and
\(Q_{ka}=A_k^*\Delta^{(2)}_{ka}\). A subscript ku denotes an arbitrary passive
query at the current node. The exact Euler updates are

\[
 \begin{split}
 w_{k+1}&=w_k+\sum_a\gamma_{ka}\phi'(w_k\cdot u_a)Q_{ka}u_a,\\
 c_{k+1}&=c_k+\sum_a\gamma_{ka}\phi(Z^{(2)}_{ka}),\\
 K_{k+1}&=K_k+\sum_a\gamma_{ka}\Delta^{(2)}_{ka}\otimes H^{(1)}_{ka}.
 \end{split}                                                   \tag{C.4.7.N2}
\]

The two centered Gaussian orientation families are \(\xi\) on population 2
and \(\zeta\) on population 1. Their exact
source covariances are

\[
 \mathbb E_2[\xi_{ka}\xi_{sb}]=\mathbb E_1[H^{(1)}_{ka}H^{(1)}_{sb}],\qquad
 \mathbb E_1[\zeta_{ka}\zeta_{sb}]=\mathbb E_2[\Delta^{(2)}_{ka}\Delta^{(2)}_{sb}].                  \tag{C.4.7.N3}
\]

The orientation families are independent; the lower population uses \(g\)
and \(\zeta\), and the upper population uses \(\xi\). Within each family, times and inputs
need not be independent. Singular covariance is allowed. The two populations
are not paired finite-neuron coordinates.

With all deterministic objects frozen as above, define

\[
 \alpha_{ka,sb}=\mathbb E_1[\partial_{\zeta_{sb}}H^{(1)}_{ka}]\quad(s<k),\qquad
 \beta_{ka,sb}=\mathbb E_2[\partial_{\xi_{sb}}\Delta^{(2)}_{ka}]\quad(s\le k).
 \tag{C.4.7.N4}
\]

Specializing C.2 (6)–(11), with unit initialized variance and unit mobilities, gives

\[
 \begin{split}
 F_{ka,sb}&=\alpha_{ka,sb}+\gamma_{sb}\mathbb E_1[H^{(1)}_{ka}H^{(1)}_{sb}],\quad s<k,\\
 D_{ka,sb}&=\beta_{ka,sb}
              +\mathbf1_{s<k}\gamma_{sb}\mathbb E_2[\Delta^{(2)}_{ka}\Delta^{(2)}_{sb}],\\
 Z^{(2)}_{ka}&=\xi_{ka}+\sum_{s<k,b}F_{ka,sb}\Delta^{(2)}_{sb},\\
 Q_{ka}&=\zeta_{ka}+\sum_{s\le k,b}D_{ka,sb}H^{(1)}_{sb}.
 \end{split}                                                   \tag{C.4.7.N5}
\]

Here \(F,D\) are scalar coefficient arrays representing the displayed
answers of the retained action \(A\) and its actual adjoint \(A^*\).
All current forward calls precede the current reverse calls. In particular

\[
 \beta_{ka,kb}=\mathbf1_{a=b}\mathbb E_2[c_k \phi''(Z^{(2)}_{ka})].                  \tag{C.4.7.N6}
\]

For a freshly appended passive query replace the right side by its one
distinguished current slot. The current \(c,w\) use only earlier steps;
current \(Z^{(2)}\) has only its own direct current \(\xi\). This proves (C.4.7.N6), including at a
singular or duplicated query. There is no sum of unweighted current
coefficients over all the other inputs.

For a fixed past backward pulse \(p=(s,b)\), put
\(v_{k;p}=\partial_{\zeta_p}w_k\). It is zero for \(k\le s\). Differentiating (C.4.7.N2)
and (C.4.7.N5) gives exactly

\[
 \begin{split}
 v_{k+1;p}=v_{k;p}+\sum_a\gamma_{ka}u_a\bigg[
 &\phi''(w_k\cdot u_a)Q_{ka}(u_a\cdot v_{k;p})\\
 &+\phi'(w_k\cdot u_a)\bigg\{\mathbf1_{(k,a)=p}
       +\sum_{q\le k}D_{ka,q}\phi'(w_{t(q)}\cdot u_q)
                         (u_q\cdot v_{t(q);p})\bigg\}\bigg],\\
 \alpha_{ku,p}&=\mathbb E_1[\phi'(w_k\cdot u)\,u\cdot v_{k;p}].
 \end{split}                                                   \tag{C.4.7.N7}
\]

The notation \(q\le k\) sums named training slots through time \(k\);
\(t(q)\) is the time index of the slot, and \(u_q\) is its input.
The direct pulse at step \(s\) has magnitude at most \(2R_0m_p\);
this is where both its atom mass and its step enter.

For an upper forward pulse \(p\), define

\[
 U_{ku;p}=\partial_{\xi_p}Z^{(2)}_{ku},\quad
 C_{k;p}=\partial_{\xi_p}c_k,\quad
 V_{ku;p}=\partial_{\xi_p}\Delta^{(2)}_{ku}.
\]

The exact upper equations are

\[
 \begin{split}
 C_{k;p}&=\sum_{q<k}\gamma_q \phi'(Z^{(2)}_q)U_{q;p},\\
 U_{ku;p}&=\mathbf1_{(k,u)=p}+\sum_{q<k}F_{ku,q}V_{q;p},\\
 V_{ku;p}&=\phi'(Z^{(2)}_{ku})C_{k;p}+c_k \phi''(Z^{(2)}_{ku})U_{ku;p},\\
 \beta_{ku,p}&=\mathbb E_2V_{ku;p}.
 \end{split}                                                   \tag{C.4.7.N8}
\]

These are finite causal derivative equations, not a derivative of an
ambient \(L^2\) vector field. No covariance, contraction, residual, \(\alpha\), or
\(\beta\) is differentiated.

Every fixed finite graph is defined before a uniform cap is sought.
Chronological construction gives a finite Gaussian innovation list;
Q is a Gaussian plus finitely many bounded first features with already
finite coefficients. Lower source derivatives at the next instruction
have a finite polynomial envelope in that finite Gaussian list, and the
bounded upper gates/readout preserve their finite moments. This inductive
argument supplies the finite coefficients in (C.4.7.N4), even on a long graph;
it asserts no bound uniform in its number of instructions.

###### 2. Consequences of a temporary backward coefficient cap

The following bounds are useful without assuming an infinite-horizon
bootstrap. They hold for every prefix on which the already constructed
backward rows have a specified cap B. At a new node the lower estimates
use only past rows; the upper estimates then construct the current row.

For all raw Euler programs through T, independently of a coefficient cap,

\[
 \|c_k\|_\infty\le C_0:=Y(e^{2T}-1),\qquad |r_{ka}|\le R_0:=Y+C_0.
 \tag{C.4.7.N9}
\]

Indeed \(\|c_{k+1}\|_\infty\le(1+2h_k)\|c_k\|_\infty+2h_kY\), since
\(|\phi|\le1\) and \(|f|\le\|c\|_2\le\|c\|_\infty\); the product bound
\(\prod_k(1+2h_k)\le e^{2T}\) proves (C.4.7.N9). Together with (C.4.7.NE), this bounds the raw row, Hilbert–Schmidt increment,
action norm, and raw speed on every prefix, without a coefficient cap.

Suppose the \(\beta\) row cap is B. Define

\[
 D_0=B+2R_0C_0^2T.
\]

Then (C.4.7.N5) gives \(\sum_q|D_{ku,q}|\le D_0\), and hence

\[
 Q_{ku}=\zeta_{ku}+J_{ku},\qquad |J_{ku}|\le D_0,
 \qquad \mathbb E_1\zeta_{ku}^2\le C_0^2.                                \tag{C.4.7.N10}
\]

The J in this display includes both response and learned contributions.
For every \(\lambda\ge0\) and every prefix,

\[
 \mathbb E_1\exp\left(\lambda\sum_{j<k,a}h_jp_a|Q_{ja}|\right)
 \le 2\exp\{\lambda TD_0+\lambda^2T^2C_0^2/2\}.                 \tag{C.4.7.N11}
\]

To verify this, use (C.4.7.N10), the scalar bound
\(\mathbb E e^{\lambda|G|}\le2e^{\lambda^2\operatorname{Var}(G)/2}\), and Jensen with weights
\(h_jp_a/\sum_{i<k}h_i\). No temporal or input independence and no maximum of
a Gaussian history is used.

Put \(M_{k;p}=\max_{s<j\le k}|v_{j;p}|\). Since \(|\phi'|\le1\), \(|\phi''|\le2\), (C.4.7.N7)
and discrete Gronwall give

\[
 {M_{k;p}\over m_p}
 \le2R_0\exp\left\{2R_0D_0T+
                      4R_0\sum_{j<k,a}h_jp_a|Q_{ja}|\right\}.
 \tag{C.4.7.N12}
\]

The direct source appears only once, at time s; every later term is
bounded by \(2R_0h_j(D_0+2\sum_a p_a|Q_{ja}|)M_{j;p}\). Iterating this
scalar inequality proves (C.4.7.N12). Thus, for each \(p\ge1\),

\[
 \|M_{k;p_0}/m_{p_0}\|_{L^p}
 \le L_p(B):=4R_0\exp\{6R_0D_0T+8R_0^2pT^2C_0^2\}.                 \tag{C.4.7.N13}
\]

Here \(p_0\) denotes the slot and p the moment order. In particular

\[
 |\alpha_{ku,sb}|\le A_B h_sp_b,\qquad
 |F_{ku,sb}|\le f_Bh_sp_b,\quad
 A_B=L_1(B),\quad f_B=A_B+2R_0.                                \tag{C.4.7.N14}
\]

There is also a **past-source density bound for \(\beta\)**, stronger than its
row bound for handling law transport. Put \(d_0=2R_0T+2C_0\). From (C.4.7.N8), the
full derivative row sum of c is at most
\(2R_0\sum_{j<k}h_j\mathcal U_j\), where
\(\mathcal U_j=\max_{i\le j,a}\sum_p|U_{ia;p}|\). Hence the row sum of V is at most
\(d_0\mathcal U_k\), and

\[
 \mathcal U_k\le1+f_Bd_0\sum_{j<k}h_j\mathcal U_j
       \le e^{f_Bd_0T}.                                    \tag{C.4.7.N15}
\]

These inequalities hold pointwise. Consequently

\[
 \sum_{p\le k}|\beta_{ku,p}|\le d_0e^{f_Bd_0T}.              \tag{C.4.7.N16}
\]

For completeness fix a single past forward slot \(p_0=(s,b)\). At time s
only \(U_{sb;p_0}=1\) is nonzero, so only \(V_{sb;p_0}=c_s\phi''(Z^{(2)}_{sb})\) is
nonzero and its magnitude is at most \(2C_0\). For k>s, (C.4.7.N8) then yields

\[
 |C_{k;p_0}|\le2R_0m_{p_0}
       +2R_0\sum_{s<j<k}h_j\max_a|U_{ja;p_0}|,
\]
\[
 \max_a|U_{ka;p_0}|
 \le f_Bd_0m_{p_0}
       +f_Bd_0\sum_{s<j<k}h_j\max_a|U_{ja;p_0}|.
\]

In the second inequality the c-memory double sum is bounded by T times
the single sum. Thus

\[
 |\beta_{ku,sb}|\le b_Bh_sp_b\quad(s<k),\qquad
 b_B=2R_0+d_0^2f_Be^{f_Bd_0T},\qquad
 |\beta_{ku,ku}|\le2C_0.                                     \tag{C.4.7.N17}
\]

All constants in (C.4.7.N10)--(C.4.7.N17) are independent of the number of atoms,
minimum atom weight, number of steps, and covariance rank. The equations
also give, for each fixed finite p,

\[
 \|\sup_{j\le k}|w_j|\|_{L^p}+\sup_{j,a}\|Q_{ja}\|_{L^p}
       +\sup_{j,a}\|Z^{(2)}_{ja}\|_{L^p}\le C_{B,p}.               \tag{C.4.7.N18}
\]

For \(w\) use its accumulated update, (C.4.7.N10), and Minkowski with weights
\(h_jp_a\). For \(Z^{(2)}\) use \(|\Delta^{(2)}|\le C_0\), (C.4.7.N14), and the forward innovation of
variance at most one. This does not claim a moment bound for a supremum
of \(Q\) or \(Z^{(2)}\) over all times and inputs. All higher moments here
come from named-field decompositions and source recursions; actions and
adjoints are used only with their stated \(L^2\) bounds.

The absolute estimates alone do not continue the C.2 cap to T. For example
they offer only the sufficient inequality

\[
 B\ \ge\ \Psi_T(B):=d_0\exp\{d_0T(L_1(B)+2R_0)\}.             \tag{C.4.7.N19}
\]

With the overestimates (C.4.7.N9) at T=40 the right side already grows faster
than B with a larger positive value at zero; (C.4.7.N19) cannot select a cap.
This is a failure of this absolute estimate, not a demonstration that
the actual coefficients diverge.

###### 3. Weighted law transport of the coefficients

Assume temporarily that some \(h_*>0\) and \(B_*<\infty\) bound
\(\mathcal B_k\le B_*\) for every two-atom reference raw Euler program
through \(T\) with \(h_{\max}\le h_*\). The reference clock argument
below will prove this bound. We first prove its implication for nearby laws,
retaining all source weights and comparing the same passive input.

Take a finite optimal coupling of a finite \(\lambda\) and the two-atom
reference. Split atoms according to its nonzero pairs and write it as
\(p_a,(u_a,y_a),(v_a,z_a)\). Then

\[
 q=\mathcal W_1(\lambda,\nu_*)=\sum_ap_ae_a,\qquad
 e_a=|u_a-v_a|+|y_a-z_a|.                                   \tag{C.4.7.N20}
\]

Both programs now have the same source names and masses. Splitting a
reference atom does not enlarge its \(\beta\) row cap: for every old slot,
its \(\alpha\), F, and \(\beta\) coefficients split in proportion to the new atom
mass, while the current coefficient remains its one distinguished direct
coefficient (C.4.7.N6). To check this claim, the lower pulse in (C.4.7.N7) is linear in
its initial \(\gamma_{sb}\) and identical repeated reference queries have
identical scalar values. Its normalized derivative is therefore unchanged
by splitting. Equation (C.4.7.N5) then splits F in the same proportion. The
single upper pulse equations (C.4.7.N8), starting with its one current impulse,
split every later coefficient in that proportion as well. Induction in
time proves the claim. Zero coupling weights are discarded.

Run both programs on the same mesh and on their joint Gaussian-source
realization. Theorem III.F.1, the source rule (III.F.9)–(III.F.10), and the
fixed neural-product extension A.2, applied to their finite union
gives, for matched slots,

\[
 \|\xi_i-\bar\xi_i\|_{L^p}
      =\|N(0,1)\|_{L^p}\|H^{(1)}_i-\bar H^{(1)}_i\|_2,
\quad
 \|\zeta_i-\bar\zeta_i\|_{L^p}
      =\|N(0,1)\|_{L^p}\|\Delta^{(2)}_i-\bar\Delta^{(2)}_i\|_2.          \tag{C.4.7.N21}
\]

Indeed the cross covariances are the corresponding cross contractions;
subtracting them gives the squared source difference in (C.4.7.N21). This is a
coupling by the source covariance rule, not a Lipschitz claim for an
arbitrary matrix square root or an inverse Gram matrix.

Write \(\mathrm d V=V-\bar V\) for a comparison difference, and let
\(\eta\) bound the maximum raw distance between the two programs through
the prefix. The elementary forward/action subtractions on their common
ball give

\[
 |r_{ka}-\bar r_{ka}|
 +\|H^{(1)}_{ka}-\bar H^{(1)}_{ka}\|_2+\|Z^{(2)}_{ka}-\bar Z^{(2)}_{ka}\|_2
 +\|\Delta^{(2)}_{ka}-\bar\Delta^{(2)}_{ka}\|_2+\|Q_{ka}-\bar Q_{ka}\|_2
 \le C(\eta+e_a),
\]
\[
 |\gamma_{ka}-\bar\gamma_{ka}|
                  \le C h_kp_a(\eta+e_a).                  \tag{C.4.7.N22}
\]

For Q subtract \(A^*\Delta^{(2)}\) directly; c is uniformly bounded pointwise,
so the upper gate difference is \(L^2\) Lipschitz. No first-layer multiplier
occurs in Q itself. At the same passive input u replace \(e_a\) by zero.

Define the coefficient discrepancy at a common passive query by

\[
 E_k=\sup_u\left\{|\beta_{ku,ku}-\bar\beta_{ku,ku}|
          +\sum_{s<k,b}|\beta_{ku,sb}-\bar\beta_{ku,sb}|\right\}.
 \tag{C.4.7.N23}
\]

The current slots are paired as distinguished query slots. Earlier
training slots use the coupling (C.4.7.N20). Comparing the current coefficient
of a far contaminant with a reference *axis* current coefficient would
give an O(1) difference even at arbitrarily small contamination mass.
The same-passive-input convention in (C.4.7.N23) avoids that invalid norm.

Here is the quantitative comparison needed for the bootstrap. If both
programs' previously constructed \(\beta\) rows are at most B, then

\[
 E_k\le C_B\left\{(\eta+q)^{1/16}
                              +\sum_{j<k}h_jE_j\right\}.
 \tag{C.4.7.N24}
\]

Constants can be enlarged to cover \(\eta+q\ge1\); only its approach to zero
matters. The current bound in (C.4.7.N24) uses only past nearby-law \(\beta\) caps.
The rest of this section gives the derivative estimates proving (C.4.7.N24).

First, within either capped program the \(\beta\) row is Lipschitz in its
current passive input, with a constant depending only on B. For \(\alpha\),
differentiate only the displayed input in (C.4.7.N7), or use the mean-value
bound
\(|\phi'(w\cdot u)u-\phi'(w\cdot v)v|\le C(1+|w|)|u-v|\) and (C.4.7.N13). This gives
\(|\alpha_{ku,p}-\alpha_{kv,p}|\le C_Bm_p|u-v|\).
The same estimate holds for F by its contraction formula. For the
upper rows, all past V and the row C are identical at the two passive
queries. In (C.4.7.N8), the past part of U differs by at most
\(\sum_p|F_{ku,p}-F_{kv,p}|\sum_l|V_{p;l}|\), which is bounded by
\(C_B|u-v|\) using (C.4.7.N15). The current \(\phi'(Z^{(2)}),\phi''(Z^{(2)})\) factors differ in \(L^2\) by
\(C\|Z^{(2)}(u)-Z^{(2)}(v)\|_2\le C_B|u-v|\); tanh has bounded third derivative.
Multiplying by the pointwise derivative row bound (C.4.7.N15) proves the
asserted \(\beta\) row bound. Thus a matched active-output row costs at most
\(E_k+C_Be_a\), in addition to the learned contraction discrepancy in
(C.4.7.N22).

Second, subtraction of (C.4.7.N7) has a causal linear propagation part using
the nearby-law coefficients and a source part. The propagation coefficient
for the maximum norm of a pulse difference is bounded by

\[
 2R_0h_k\left(D_0+2\sum_ap_a|Q_{ka}|\right).                 \tag{C.4.7.N25}
\]

The source part consists exactly of the differences of \(\gamma\), the two
input vectors, the gates \(\phi',\phi''\), \(Q\), and \(D\), each multiplied by an
unchanged reference pulse. In particular there is no derivative of D in
this subtraction. The D difference is

\[
 \mathrm d  D_{i,p}=\mathrm d \beta_{i,p}
 +\mathbf1_{t(p)<t(i)}\left[
  \mathrm d \gamma_p \mathbb E_2[\bar\Delta^{(2)}_i\bar\Delta^{(2)}_p]
       +\gamma_p\mathrm d  \mathbb E_2[\Delta^{(2)}_i\Delta^{(2)}_p]\right],          \tag{C.4.7.N26}
\]

where unbarred \(\gamma\) is used in the second term. This also verifies that
learned-memory errors retain \(m_p\).

All unchanged normalized pulses have every fixed finite moment by (C.4.7.N13).
Gate and field differences needed in the source part have an \(L^{12}\) bound
\(C_B(\eta+e_a)^{1/16}\). For bounded gates interpolate the \(L^2\) bound (C.4.7.N22)
with their pointwise bound. For w or Q interpolate their \(L^2\) difference
with the uniform \(L^{24}\) bounds (C.4.7.N18); interpolation gives exponent 1/11,
which implies the weaker displayed exponent on a bounded distance range.
For the input factors themselves use \(|u_a-v_a|\le e_a\).
Products of up to three factors are bounded in \(L^4\) by Hölder with \(L^{12}\)
norms. The random integrating factor obtained from (C.4.7.N25) has every fixed
moment by (C.4.7.N11); Cauchy--Schwarz bounds its product with each forcing
term. Minkowski sums the time/atom masses. Discrete Gronwall therefore
gives, for every past pulse p=(s,b),

\[
 {\|\max_{j\le k}|v_{j;p}-\bar v_{j;p}|\|_2\over m_p}
 \le C_B\left\{(\eta+e_b)^{1/16}+q^{1/16}
                              +\sum_{j<k}h_jE_j\right\}.   \tag{C.4.7.N27}
\]

One way to verify the averaging in this estimate is to retain each
\(e_a^{1/16}\) until the last step and use
\(\sum_ap_ae_a^{1/16}\le q^{1/16}\). The direct pulse uses (C.4.7.N22) and has
the same factor \(m_p\); dividing by it does not leave \(1/p_b\).
In the D term, its row variation multiplies the reference maximum pulse
norm from (C.4.7.N13); its active-output discrepancy is bounded just above.
There is also a term in which D is unchanged and a *past source's* gate
or input changes. This is where (C.4.7.N17) is essential: its old-source
coefficient satisfies \(|D_{ka,sb}|\le C_Bh_sp_b\), so

\[
 \sum_{s<k,b}|D_{ka,sb}|e_b^{1/16}
             \le C_BT\sum_bp_be_b^{1/16}\le C_BTq^{1/16}.
 \tag{C.4.7.N27a}
\]

The one current coefficient costs \(C_Be_a^{1/16}\) and is averaged
with the outside update weight \(p_a\). A row bound without the past-source
density bound would not justify this step.
These account for every term from the two sums in (C.4.7.N7). No
maximum of the \(e_a\) and no unweighted sum over source indices is taken.

By the second line of (C.4.7.N7), (C.4.7.N27), and Hölder for the difference of its
outside gate, at a common passive input

\[
 \sum_{p<k}|\mathrm d \alpha_{ku,p}|
 \le C_B\left\{(\eta+q)^{1/16}
                              +\sum_{j<k}h_jE_j\right\}.   \tag{C.4.7.N28}
\]

Here \(\sum_{p<k}m_p\le T\); the contribution depending on the source
\(e_b\) averages as in (C.4.7.N27). The identical estimate holds for the F-row
difference by (C.4.7.N5) and (C.4.7.N22). For a matched active output add
\(C_Be_a\) using the passive-input estimate. Entrywise versions keep the
factor \(m_p\) and its \(e_b\) term.

For a current output slot \(i=(k,u)\), write \(q<i\) for
\(t(q)<k\); the symbols \(k,i\) in the next display have this relation.
The exact upper differences are

\[
 \begin{split}
 \mathrm d  U_{i;p}
    &=\sum_{q<i}\mathrm d  F_{i,q}\bar V_{q;p}
                       +\sum_{q<i}F_{i,q}\mathrm d  V_{q;p},\\
 \mathrm d  C_{k;p}
    &=\sum_{q<k}\{\mathrm d \gamma_q \phi'(\bar Z^{(2)}_q)\bar U_{q;p}
             +\gamma_q\mathrm d  \phi'(Z^{(2)}_q)\bar U_{q;p}
             +\gamma_q \phi'(Z^{(2)}_q)\mathrm d  U_{q;p}\},\\
 \mathrm d  V_{i;p}
    &=\phi'(Z^{(2)}_i)\mathrm d  C_{k;p}+\mathrm d  \phi'(Z^{(2)}_i)\bar C_{k;p}
          +c_k\phi''(Z^{(2)}_i)\mathrm d  U_{i;p}
          +\{\mathrm d  c_k \phi''(\bar Z^{(2)}_i)+c_k\mathrm d  \phi''(Z^{(2)}_i)\}
                                                        \bar U_{i;p}.
 \end{split}                                               \tag{C.4.7.N29}
\]

The direct U impulses cancel after pairing the distinguished current
slots. To keep output errors weighted, set

\[
 G_k=(\eta+q)^{1/16}+\sum_{j<k}h_jE_j,\qquad
 L_k=\sum_ap_a\left\|\sum_p|\mathrm d  V_{ka;p}|\right\|_2.
\]

Every barred upper derivative row is bounded pointwise by (C.4.7.N15).
The F propagation coefficients have density \(f_Bh_jp_a\), and \(\gamma\)
retains its original mass. Summing (C.4.7.N29) over source indices, taking \(L^2\),
then averaging its active output index gives

\[
 L_k\le C_BG_k+C_B\sum_{j<k}h_jL_j.                         \tag{C.4.7.N29a}
\]

In this estimate the F-row forcing at a matched active output is at most
\(C_B(G_k+e_a)\) by (C.4.7.N28); the field factors at that output cost
\(C_B(\eta+e_a)\) by (C.4.7.N22). Both are averaged with \(p_a\). In the C-row,
which does not depend on the output query, the same factors are already
multiplied by \(h_jp_a\). These are all appearances of an output transport
cost in (C.4.7.N29). Since \(G_k\) is nondecreasing, discrete Gronwall yields
\(L_k\le C_BG_k\) after increasing \(C_B\). For a common passive output there
is no \(e_a\) term, and the same equations give

\[
 \left\|\sum_p|\mathrm d  V_{ku;p}|\right\|_2
                 \le C_BG_k+C_B\sum_{j<k}h_jL_j\le C_BG_k.
 \tag{C.4.7.N29b}
\]

Taking expected absolute values proves (C.4.7.N24). The current diagonal
contributes at most \(C\eta\) directly from (C.4.7.N6). There is no current
unknown \(E_k\) on the right: (C.4.7.N28) uses only earlier lower updates, and all
upper memory terms in (C.4.7.N29) are strictly earlier. No supremum over the
matched active-output costs \(e_a\) was used.

The raw discrepancy \(\eta\) used above is available before the
reference raw coefficient bound has been proved. The raw bound (C.4.7.NE), the Hilbert–Schmidt transport estimate (C.4.7.NC), and
the actual reference tails of C.4.5.2 (R17)–(R18) give, for every finite
raw Euler program with training law \(\lambda\),

\[
 \sup_{k:t_k\le T}d(\theta_{\lambda,k},\theta_*(t_k))
       \le \omega_T(q+h_{\max}),\qquad \omega_T(s)\to0.     \tag{C.4.7.N30}
\]

To see the mesh term, interpolate the Euler path affinely; its speed is
uniformly bounded by the crude raw ball. Apply the transport estimate
with the actual reference as its tail-bearing endpoint. The distance
from the interpolated Euler state to its left endpoint is at most
\(V_Th_{\max}\), so the cutoff inequality acquires
\(C(1+R_{\rm cut})h_{\max}\). Integrating gives
\(C e^{CR_{\rm cut}}\{(1+R_{\rm cut})(q+h_{\max})+e^{-cR_{\rm cut}^2}\}\). Taking the cutoff to be a sufficiently large constant times
\(\sqrt{\log(e/(q+h_{\max}))}\) proves (C.4.7.N30) for small
\(q+h_{\max}>0\); define the modulus to be zero at zero and enlarge
it using the common raw bound outside that range. This is a comparison to one
existing flow, not a construction of a changed-law flow.
Applying (C.4.7.N30) to \(\lambda\) and to the reference raw Euler program gives a
valid \(\eta\) tending to zero with \(q+h_{\max}\) in (C.4.7.N24).

Assume the reference raw coefficient bound stated at the start of this part. Its reference Euler Q tails are Gaussian by (C.4.7.N10).
For the two raw programs on the **same** mesh, the transport estimate
therefore gives, at a fixed cutoff \(R_{\rm cut}\), the recurrence

\[
 d_{k+1}\le[1+Ch_k(1+R_{\rm cut})]d_k
          +Ch_k\{(1+R_{\rm cut})q+e^{-cR_{\rm cut}^2}\}.
\]

Both start at the same state. Iteration and cutoff choice give

\[
 \sup_k d_k\le\Phi_{B_*}(q),\qquad
 \Phi_{B_*}(q)\longrightarrow0\quad(q\downarrow0),          \tag{C.4.7.N30a}
\]

uniformly over admitted meshes; there is no mesh defect in this
comparison. One can take \(\Phi(q)=Cq e^{C\sqrt{\log(e/q)}}\) for small q
after enlarging constants. The crude ball for the nearby program
suffices; only the reference endpoint of the transport estimate
requires tails.

Set \(B=B_*+1\) and use its invariant duplication property.
At the first potential failed row, all prior nearby-law rows are at
most B. Estimates (C.4.7.N10)--(C.4.7.N29) apply in their causal order. Discrete
Gronwall in (C.4.7.N24) gives

\[
 E_k\le C_B e^{C_BT}
                 \{\Phi_{B_*}(q)+q\}^{1/16}.                \tag{C.4.7.N31}
\]

Choose positive \(\rho\) small enough that the right side is at most 1/2
whenever \(q<\rho\), and put \(h_0=h_*\).
The current row is then at most \(B_*+1/2<B\), contradicting first failure.
The zero-readout initialization has \(\beta=0\), so induction starts.
This proves (C.4.7.N-cap), conditional on that reference bound.
Formula (C.4.7.N10) gives a uniform Gaussian marginal tail for every passive
\(Q\), and (C.4.7.N9) controls the readout. This argument has not inferred
convergence of changed-law paths from their fixed positive proximity to
the reference.

More explicitly, once the cap is fixed, \(Q=G+J\), \(\operatorname{Var}(G)\le C_0^2\),
\(|J|\le D_0\). For \(R_{\rm cut}\ge2D_0\), the event \(|Q|>R_{\rm cut}\) implies
\(|G|>R_{\rm cut}/2\). Integrating the scalar Gaussian tail and absorbing its
polynomial prefactor gives \(\tau_{R_{\rm cut}}(Q)\le M e^{-aR_{\rm cut}^2}\) with finite
positive a,M depending only on the fixed caps. Enlarge M to cover the
remaining \(R_{\rm cut}\ge1\) and the bounded readout. Averaging these individual tail bounds over any admitted training law
preserves the same constants, as does restriction to a smaller radius. A state
on an affine Euler segment is obtained by appending one shorter final
step; the same bound applies to its recomputed fields. This is a
marginal-in-time statement, not an exponential bound for a path maximum.

###### 4. Raw-to-clock mesh errors and their named derivatives

The clock change is exact for continuous reference flow. Its raw Euler
defect and the named derivatives of that defect must still be summed;
the following bounds do so under the temporary cap.

Let

\[
 \mathcal F(w)=w/2+\sinh(2w)/4,\quad \mathcal F'(w)=1/\phi'(w),
\quad R_h(w,b_0)=\mathcal F(w+hb_0\phi'(w))-\mathcal F(w)-hb_0.
\]

Here \(b_0\) is a scalar velocity coefficient.
Put \(\vartheta=hb_0\phi'(w)\). Taylor's integral identity gives

\[
 R_h=h^2b_0^2\phi'(w)^2
                \int_0^1(1-s)\mathcal F''(w+s\vartheta)\,ds.
 \tag{C.4.7.N32}
\]

The elementary hyperbolic identities imply

\[
 \phi'(w)^2|\mathcal F''(w+z)|\le2e^{2|z|},\qquad
 \phi'(w)^2|\mathcal F'''(w+z)|\le4e^{2|z|},\qquad |\phi''|\le2\phi'.
\]

For example \(|\sinh(2(w+z))|\le e^{2|z|}\cosh(2w)\) and
\(\phi'(w)^2\cosh(2w)\le2\); the bound for the third derivative follows in
the same way. Differentiating the explicit integral (C.4.7.N32), rather than
separately estimating the large terms before cancellation, yields

\[
 |R_h|\le Ch^2 b_0^2e^{2h|b_0|},
\]
\[
 |\partial_wR_h|\le Ch^2b_0^2(1+h|b_0|)e^{2h|b_0|},\qquad
 |\partial_{b_0}R_h|\le Ch^2|b_0|(1+h|b_0|)e^{2h|b_0|}.
 \tag{C.4.7.N33}
\]

Every named derivative consequently obeys

\[
 |\partial_p R_h|
 \le Ch^2e^{2h|b_0|}(1+h|b_0|)
                \{b_0^2|\partial_p w|+|b_0||\partial_p b_0|\}.
 \tag{C.4.7.N34}
\]

On the reference, including any split representation, the row-coordinate
update has precisely this form with

\[
 b_{0,a,k}=-2\sum_{j:v_j=e_a}p_jr_{kj}Q_{kj}.
 \tag{C.4.7.N35}
\]

Under the temporary cap its scalar marginals have uniformly bounded
Gaussian norms, by (C.4.7.N10) and the total atom mass. Formula (C.4.7.N11) or the
scalar Gaussian exponential moment controls the factor in (C.4.7.N33)--(C.4.7.N34).
Therefore \(\sum_k\|R_{h_k}\|_{L^p}\le C_{B,p}h_{\max}\) for every fixed finite p.

For a backward source \(p_0\)=(s,j), at the direct injection step
\(|\partial_{p_0}b_0|\le2R_0p_j\) and \(\partial_{p_0}w_s=0\).
Dividing that step's estimate (C.4.7.N34) by \(m_{p_0}=h_sp_j\) costs at most
\(C_{B,p}h_s\). At every later step, (C.4.7.N7), (C.4.7.N13), and the D-row cap give

\[
 \|\partial_{p_0}w_k/m_{p_0}\|_{L^p}
 +\|\partial_{p_0}b_{0,a,k}/m_{p_0}\|_{L^p}\le C_{B,p}.
\]

Using Hölder in (C.4.7.N34) and \(\sum_kh_k^2\le Th_{\max}\) now proves

\[
 {1\over m_{p_0}}\sum_{k\ge s}
               \|\partial_{p_0}R_{h_k}\|_{L^p}
                                  \le C_{B,p}h_{\max}.     \tag{C.4.7.N36}
\]

This proves summability of the named backward-pulse clock defect with
its correct mass normalization. A local lower-population function is
independent of the upper \(\xi\) slots when deterministic coefficients are
frozen; there is no additional \(\xi\) derivative of its clock defect.
The c/K updates are the same in raw and clock formulations.

###### 5. The physical reference source anchor and its transfer

**The reference clock coefficient bound.**

Use the two reference clocks \(X_a=\mathcal F(w_a)-\mathcal F(g_a)\) and the scalar solution
\(w_a=J(X_a,g_a)\) of \(J_X=\operatorname{sech}^2J\), \(J(0,g)=g\). Thus
\(|J_X|\le1\). Its active first features have \(|\partial_X\phi(J)|=\operatorname{sech}^4J\le1\).
The physical reference clock equations are

\[
 \dot X_a=-r_aQ_a,\qquad
 \dot K=-\sum_{a=1}^2r_a\Delta^{(2)}_a\otimes H^{(1)}_a,\qquad
 \dot c=-\sum_{a=1}^2r_aH^{(2)}_a.                                \tag{C.4.7.N37}
\]

Their raw fields are the reference flow of C.4.5.1 (R4)–(R8).
The factor \(-r_a\) in (C.4.7.N37) is \(-2p_ar_a\) with \(p_a=1/2\).
On the common
carrier these equations are Lipschitz on the bounded sets used below,
by the explicit subtractions that follow; Euler convergence here needs
no raw first-gate estimate.

For the auxiliary source extraction use finite initialized matrices
with \(\|A_0\|_{\rm op}\le10\) and **zero readout**. This auxiliary fixed program identifies the zero-readout population
coefficients. The actual finite-network initialization in the theorem
retains its specified random readout. In the finite calculation every
field norm is \(\|v_n\|_2/\sqrt n\), and the increment norm is the
ordinary Frobenius norm \(\|K_n\|_F\). These are the finite versions of
population \(L^2\) and Hilbert–Schmidt norms by III.F.8
(III.F.28)–(III.F.31). By (C.4.7.N9) and bounded activations, at all nodes,

\[
 \|c_k\|_\infty\le C_0,\quad |r_{ka}|\le R_0,\quad
 \|K_k\|_{HS}\le2TR_0C_0,\quad \|A_k\|_{op}\le M:=10+2TR_0C_0.
 \tag{C.4.7.N38}
\]

These bounds also hold if a fresh root is added to one forward or
reverse query and all descendants, including residuals, are recomputed.
Forward tanh and its gate remain bounded, so every subsequent c and K
increment obeys the same estimate. Reverse forcing changes only the
clock increment directly. Thus there is no assumption that a forced
program retains a gradient-flow energy identity.

For two unforced subsequent clock states on this ball set
\(x=\sum_a\|\mathrm d  X_a\|_2\), \(\varkappa=\|\mathrm d  K\|_{\rm HS}\), \(z=\|\mathrm d  c\|_2\),
and \(d=x+\varkappa+z\). The same-root scalar bound for J gives

\[
 \begin{split}
 \sum_a\|\mathrm d  H^{(1)}_a\|_2&\le x,\qquad
 V:=\sum_a\|\mathrm d  Z^{(2)}_a\|_2\le Mx+2\varkappa,\\
 D:=\sum_a\|\mathrm d \Delta^{(2)}_a\|_2&\le2z+2C_0V,\qquad
 P:=\sum_a\|\mathrm d  Q_a\|_2\le MD+2C_0\varkappa,\\
 S:=\sum_a|\mathrm d  r_a|&\le2z+C_0V.
 \end{split}                                               \tag{C.4.7.N39}
\]

The three velocity differences in (C.4.7.N37) are at most

\[
 MC_0 S+R_0P,\qquad C_0S+R_0(D+C_0x),\qquad S+R_0V.                    \tag{C.4.7.N40}
\]

For example subtract \(r\Delta^{(2)}\otimes H^{(1)}\) into its residual, upper
field, and lower feature differences; the rank norm is the product of
its \(L^2\) factors. Equations (C.4.7.N39)--(C.4.7.N40) give a bound \(Ld\) with the fixed
overestimate

\[
 L=100(1+M+C_0+R_0)^4,
 \qquad E=\exp(LT).                                        \tag{C.4.7.N41}
\]

Hence any post-pulse Euler difference is amplified by at most E,
independently of width, step count, and step sizes. Splitting an atom
retains these equations after summing its identical descendants.

Insert \(\varepsilon e\), with \(e\) a fresh standard Gaussian root of
the answer's population, into the complete reverse answer at slot \((s,b)\).
Its only immediate state change is in the clock corresponding to
\(v_b=e_a\), with norm at most

\[
 2R_0 h_sp_b|\varepsilon|\|e\|_2.                               \tag{C.4.7.N42}
\]

For a passive first feature
\(H^{(1)}(u)=\phi(u_1J(X_1,g_1)+u_2J(X_2,g_2))\), the difference is at most x.
The subsequent passive feature difference is therefore bounded by
\(2R_0Eh_sp_b|\varepsilon|\|e\|_2\).

Instead insert the root into one complete forward answer \(Z^{(2)}_{sb}\).
At that node its activation, \(\Delta^{(2)}\), residual, and reverse answer change
by at most, respectively,

\[
 |\varepsilon|\|e\|_2,\quad 2C_0|\varepsilon|\|e\|_2,\quad
 C_0|\varepsilon|\|e\|_2,\quad 2MC_0|\varepsilon|\|e\|_2.
\]

Use the old Q and the bounded new residual when subtracting the clock
update. The three immediate state increments have total norm at most
\(P_0h_sp_b|\varepsilon|\|e\|_2\), where

\[
 P_0=2\{MC_0^2+2R_0MC_0+C_0^2+2R_0C_0+C_0+R_0\}.                          \tag{C.4.7.N43}
\]

The terms arise from \(\mathrm d (rQ)\), \(\mathrm d (r\Delta^{(2)}\otimes H^{(1)})\), and
\(\mathrm d (rH^{(2)})\), respectively. A passive later \(\Delta^{(2)}\) satisfies

\[
 \|\mathrm d \Delta^{(2)}(u)\|_2\le z+2C_0(Mx+\varkappa)\le K_0d,
 \qquad K_0=1+2C_0(M+1).                                    \tag{C.4.7.N44}
\]

Thus its post-pulse change is at most
\(P_0K_0Eh_sp_b|\varepsilon|\|e\|_2\).

Extract the named coefficients by the full mechanism of C.4.5.2
(R5)--(R15). Here are the hypotheses and the order of limits needed
for this application. At each fixed graph clip the Gaussian first
roots smoothly. The passive feature's derivatives with respect to X
are bounded uniformly in the root clipping level; its root
derivatives are bounded at each fixed level. A readout clip equal to
the identity on a neighborhood of \([-C_0,C_0]\) is inactive. Thus the
fixed-program theorem and its complete source extension apply to
forced and unforced graphs, including singular covariance and
variance-zero slots. At a fixed graph all source derivatives have a
finite deterministic bound independent of root clipping: the clock
derivatives are bounded, the readout is bounded, and every matrix
answer is a source plus a finite sum with fixed coefficients.
Chronological convergence and this derivative bound remove root
clipping and make all coefficients continuous as \(\varepsilon\) tends to
zero, exactly as proved in C.4.5.2, proof part 2, (R5)–(R7). No mesh-uniform source cap was
used in this fixed-graph step.

Fix the mesh and nonzero \(\varepsilon\) and first let width tend to infinity.
The initialization operator event and \(\|e_n\|_2/\sqrt n\to1\) have
probability tending to one, by III.F.2 (III.F.4) and the Gaussian
second-moment calculation. Theorem III.F.1 and its extension just checked transfer
(C.4.7.N42)--(C.4.7.N44) and their pairing with the fresh Gaussian root. In the
source coordinate expression that root enters only in the specified
slot as \(\mathrm{slot}+\varepsilon e\). The selected residuals and covariance laws
may depend on \(\varepsilon\) but are deterministic, and all Gaussian source
groups are independent of this local new root. Conditional
one-dimensional Gaussian integration by parts therefore gives

\[
 \mathbb E[eV^\varepsilon]=\varepsilon\mathbb E[\partial_{\rm slot}V^\varepsilon].
 \tag{C.4.7.N45}
\]

The expectation in (C.4.7.N45) is in the population of the observed field.
The unforced expression is independent of \(e\). Cauchy--Schwarz in the
joint limit, division by \(|\varepsilon|\), then the fixed-graph
zero-forcing continuity just proved yield

\[
 |\alpha^{\rm cl}_{ku,sb}|\le2R_0Eh_sp_b,
 \qquad |\beta^{\rm cl}_{ku,sb}|\le P_0K_0Eh_sp_b\quad(s<k),
 \qquad |\beta^{\rm cl}_{ku,ku}|\le2C_0.                     \tag{C.4.7.N46}
\]

The argument works for each passive u with the same constants.
Consequently every reference physical clock Euler program through T
has the cap

\[
 B_{\rm cl}=2C_0+TP_0K_0E.                                   \tag{C.4.7.N47}
\]

This proves a bound for the specified named coefficients. It does
not infer a derivative transverse to a singular source support from
the unforced value law. The fresh root and the width-first,
forcing-second order in (C.4.7.N45) are essential.

**Transfer from clock Euler to raw reference Euler.**

Compare the reference raw and clock Euler programs on the same mesh
and common Gaussian source carrier. Write
\(X^r_a=\mathcal F(w^r_a)-\mathcal F(g_a)\) for the transformed raw program and \(X^c\)
for clock Euler. The raw program satisfies the exact clock update
with the extra vector of defects (C.4.7.N32). Its lower first-feature
expression is the same function of X and g as in the clock program.

Define \(E_k\) by (C.4.7.N23) for this raw/clock pair, with no change of data
law, and assume a temporary cap B on all preceding raw \(\beta\) rows.
Let \(\eta_h\) bound the raw discrepancy of their fields. There is an
\(\eta_h\) tending to zero with \(h_{\max}\) independently of that cap: (C.4.7.N30)
compares raw Euler with the actual reference, while (C.4.7.N39)--(C.4.7.N41), the
bounded clock speed, and the integrated Euler error compare clock
Euler with the same reference in clock/HS/\(L^2\) norm. The scalar bound
\(|J_X|\le1\) converts the latter distance to raw distance. In particular
all the field differences in (C.4.7.N22) are \(O(\eta_h)\).

For a backward pulse \(p_0\)=(s,b), put
\(\chi^r_{k;p_0}=\partial_{\zeta_{p_0}}X^r_k\), and define \(\chi^c\) similarly.
For a lower first feature let \(J_q^r\) and \(J_q^c\) denote its two
clock derivatives. Each has norm at most two, and their difference
in \(L^2\) is at most \(C\eta_h\), since each is a product of bounded tanh
gates with bounded derivatives. At reference active slots one can
use the sharper bound one. Differentiating the two clock recursions
gives the exact pair

\[
 \chi^r_{k+1;p_0}=\chi^r_{k;p_0}
   +\sum_a\gamma^r_{ka}v_a\left\{\mathbf1_{(k,a)=p_0}
             +\sum_{q\le k}D^r_{ka,q}J_q^r\chi^r_{t(q);p_0}\right\}
   +\partial_{p_0}R_k,
\]
\[
 \chi^c_{k+1;p_0}=\chi^c_{k;p_0}
   +\sum_a\gamma^c_{ka}v_a\left\{\mathbf1_{(k,a)=p_0}
             +\sum_{q\le k}D^c_{ka,q}J_q^c\chi^c_{t(q);p_0}\right\}.
 \tag{C.4.7.N48}
\]

Here \(v_a\) is the reference axis of that atom, and the lower feature
derivative is a row vector applied to \(\chi\). The clock reference cap
(C.4.7.N47) bounds its D rows by \(D_{\rm cl}=B_{\rm cl}+2R_0C_0^2T\). Since the clock gates
are bounded, its pulses satisfy the **pointwise** bound

\[
 \max_{j\le k}|\chi^c_{j;p_0}|/m_{p_0}
                        \le2R_0\exp(4R_0D_{\rm cl}T).         \tag{C.4.7.N49}
\]

Subtract (C.4.7.N48). Its raw propagation coefficients have a deterministic
bound depending only on B and (C.4.7.N9); there is no random Q multiplier.
Differences of \(\gamma\) and the clock gates cost \(C\eta_h\), multiplied
by the bounded normalized reference pulse (C.4.7.N49). The D-row difference
is at most \(E_j+C\eta_h\) by (C.4.7.N26). Finally (C.4.7.N36) bounds the sum of
the normalized defect derivatives in \(L^2\) by \(C_Bh_{\max}\). Discrete
Gronwall gives

\[
 {\|\max_{j\le k}|\chi^r_{j;p_0}-\chi^c_{j;p_0}|\|_2\over m_{p_0}}
    \le C_B\left\{\eta_h+h_{\max}
                                  +\sum_{j<k}h_jE_j\right\}.
 \tag{C.4.7.N50}
\]

The maximum on the left is controlled by the sum of the forcing
norms and a deterministic integrating factor. It does not require
an \(L^2\) bound on a supremum of the raw field discrepancy.

Take expected first-feature derivatives to obtain the same bound for
the \(\alpha\) row difference, after summing its source masses. For a
passive output its derivative outside chi differs in \(L^2\) by
\(C\eta_h\) and is bounded, so the statement remains uniform in u.
The upper source equations (C.4.7.N8) are identical in the two schemes;
subtracting them as in (C.4.7.N29), using the source density bounds and
discrete Gronwall, proves

\[
 E_k\le C_B\left\{\eta_h+h_{\max}
                                  +\sum_{j<k}h_jE_j\right\}.
 \tag{C.4.7.N51}
\]

Set \(B=B_{\rm cl}+1\). At any first potentially failed raw row, all previous
rows obey this cap. The defect estimate (C.4.7.N36) uses only those previous
raw Q fields. The current \(\alpha\) then obeys (C.4.7.N50), and the current
\(\beta\) obeys (C.4.7.N51), whose right side has no current \(\beta\). Gronwall
yields \(E_k\le C_Be^{C_BT}(\eta_h+h_{\max})\). Choose \(h_*\) positive and
small enough that this is at most 1/2 whenever \(h_{\max}\le h_*\).
Then the current raw row is at most \(B_{\rm cl}+1/2<B\), so induction cannot
fail. Both zero-readout initial programs have \(\beta=0\). This proves the reference raw coefficient bound with \(B_*=B_{\rm cl}+1\).
The weighted law-transport induction above now proves (C.4.7.N-cap) and its
uniform passive Gaussian-tail consequence through physical time \(T=40\).

The two bootstraps are separate: the first uses one fixed, independently
proved clock anchor to control reference raw Euler; the second uses
that raw anchor and weighted law transport to control all nearby finite
laws. Neither bootstrap takes a supremum of far-atom transport costs
or assumes the tails of the not-yet-controlled current query.

##### C.4.7.4. Strong completion, law continuity and reached uniqueness

The preceding source argument supplies a radius \(\rho>0\), a mesh
threshold and constants \(a,M>0\) such that all sufficiently fine
finite-law raw Euler programs in \(U_\rho\) satisfy
\[
 \tau_R(c_k)+\int\tau_R(Q_k(u))\,d\mu(u,y)
                      \le M e^{-aR}\quad(R\ge1).
 \tag{C.4.7.NH}
\]
It actually supplies Gaussian tails for every passive query. The weaker
exponential estimate (C.4.7.NH) is enough for the remaining construction.
All constants are uniform on a fixed smaller neighborhood. Choose
\(0<\delta_Y<\rho/4\); further decreases do not affect the argument.

For two Euler interpolants on meshes of maximal steps \(h,h'\), with
laws \(\mu,\nu\) in that smaller neighborhood, put
\[
 s(t)=d(\theta^h_\mu(t),\theta^{h'}_\nu(t))
                     +q+V_T(h+h'),\qquad q=\mathcal W_1(\mu,\nu).
\]
The preceding-node distance is at most the current distance plus
\(V_T(h+h')\). Apply (C.4.7.NC) at these nodes and (C.4.7.NH), and choose
\(R=1+a^{-1}\log(1/s)\). For \(0<s\le1\) this gives almost everywhere
\[
 s'(t)\le Ls(t)\log(e/s(t)),\qquad
 s(t)\le e^{1-\alpha(t)}s(0)^{\alpha(t)},\quad
                         \alpha(t)=e^{-Lt}>0.
 \tag{C.4.7.NO}
\]
To verify the integration, set \(z=\log(e/s)\); then \(z'\ge-Lz\).
Multiplication by \(e^{Lt}\) and integration prove the displayed bound.
At a zero value use \(s+\eta\), the monotonicity of
\(v\log(e/v)\) on \((0,1)\), and then \(\eta\downarrow0\).
For sufficiently small initial s the bound remains below one through T,
so a first-exit argument validates its use on the whole interval. For
larger errors the common raw bound (C.4.7.NE) suffices. No lower bound on the
tail exponent relative to T is needed.

Finite probability laws are dense in \(\mathcal W_1\) on the compact
data domain: partition it into finitely many Borel cells of diameter at
most b, move each cell's mass to a representative, and pay at most b.
For any \(\mu\in U_Y\), take such finite laws \(\nu_j\to\mu\) and
meshes \(h_j\to0\). They eventually lie in a fixed smaller neighborhood
where (C.4.7.NH) is uniform. Formula (C.4.7.NO) makes the Euler paths Cauchy in
\(C([0,T];\mathcal E)\), including the HS component. The same estimate
between any two families makes the limit independent of both choices.
Their preceding-node states have the same limit. Joint field continuity
proved after (C.4.7.NC) now passes their integral equations to
\[
 \theta_\mu(t)=(g,0,0)+\int_0^t\mathcal F_\mu(\theta_\mu(s))\,ds.
 \tag{C.4.7.NI}
\]
The convergence of the integrands is uniform in time. Otherwise a sequence
of discrepant times has a convergent subsequence, and joint continuity at
the corresponding limiting state and law gives a contradiction. Thus
(C.4.7.NI) is a strong \(C^1\) equation in all three raw components, and every
coefficient is computed from the current state and the fixed law. Its
energy and readout bounds are (C.4.7.NG).

The needed tails pass to the constructed paths without a coordinate
supremum assumption. For fixed R the map
\(v\mapsto(|v|-R)_+\) is 1-Lipschitz on \(L^2\), and
\[
 \|v\mathbf1_{|v|>2R}\|_2
                \le2\|(|v|-R)_+\|_2\le2\tau_R(v).
 \tag{C.4.7.NP}
\]
Uniform state convergence and bounded multiplier continuity imply
uniform-in-input Q convergence at a fixed time. The resulting continuous
positive-part norms pass also through the converging law integral.
Consequently (C.4.7.NH), with an enlarged M and exponent \(a/2\), holds for
the constructed path, at every time with the same constants.

Comparing two such paths by (C.4.7.NC), their tails and (C.4.7.NO) proves (C.4.7.NL), with
\(a_Y=e^{-LT}\) after changing constants. The forward formulas give
\[
 \sup_u\|H^{(1)}_\theta(u)-H^{(1)}_{\bar\theta}(u)\|_2
          \le\|w-\bar w\|_2,
\]
\[
 \sup_u\|Z^{(2)}_\theta(u)-Z^{(2)}_{\bar\theta}(u)\|_2
          \le\|A\|_{\rm op}\|w-\bar w\|_2+\|K-\bar K\|_{\rm HS}.
\]
Together with bounded c these give the same type of uniform prediction
modulus. Common raw bounds give its constant large-q branch.

An arbitrary competing strong raw solution on the prescribed carrier
has a bounded path on a compact interval. Apply (C.4.7.NC) with that competitor
as its first endpoint and the constructed solution as its tail-bearing
second endpoint. Only the latter's tails enter. Formula (C.4.7.NO) at zero
initial discrepancy proves equality. Applying this argument on
\([s,40]\) proves the reached-state uniqueness and restart assertion.
Existence for this restart is furnished by the restriction of (C.4.7.NI);
neither new Gaussian roots nor a local theorem from every ambient state
is needed. No extra tail or weighted regularity is imposed on a
competitor.

We will also need the law comparison on one common Euler mesh with no
mesh-error floor. Subtract the two recursions at the same node and use
(C.4.7.NC) and (C.4.7.NH). If \(s_k=d(\theta^h_\mu(t_k),\theta^h_\nu(t_k))+q\),
then
\(s_{k+1}\le s_k+L\Delta_k s_k\log(e/s_k)\) below one. Compare each
step with the scalar increasing solution of
\(v'=Lv\log(e/v)\): its derivative increases while \(v<1\), so its
exact increment dominates the Euler increment. Induction and the same
first-exit bound give
\[
 \sup_k d(\theta^h_\mu(t_k),\theta^h_\nu(t_k))
                      \le Cq^{a_Y}.
 \tag{C.4.7.NLM}
\]
All constants remain uniform on the smaller neighborhood. Bounded c and
the displayed forward inequalities also give
\(\sup_u\|Q_\theta(u)-Q_{\bar\theta}(u)\|_2\le C d(\theta,\bar\theta)\)
for these Euler states: subtract \(A^*\Delta^{(2)}\) and use the
uniform pointwise bound on the comparison readout in its gate product.

##### C.4.7.5. Actual finite GF and the observation limits

The population tail estimate does not by itself assert a finite-width
moment theorem. We therefore give the approximation order explicitly.
Fix one finite comparison law \(\nu\) in the neighborhood and one fine
raw Euler mesh h. The resulting population program has finitely many
instructions. Expand K as its finite sum of ranks, and realize this
program on the actual initialized finite arrays using its deterministic
population residuals and contractions. Include the actual finite initial
readout additively in the proxy parameters, as in C.4.3 (A3). Its assigned
increments are the oracle increments. Actual GF and proxy therefore start
at the same finite arrays.

The complete fixed-program theorem III.F.1–7 and A.1 applies to this
fixed graph. Its roots are the two first-row Gaussians, the two queried
orientations are \(A_0\) and its actual adjoint, and the coordinate
instructions are continuous of at most linear growth. A backward product
is a bounded gate times a named \(L^2\) field. To recover the recomputed
proxy feedback from the oracle instructions, subtract each gate product,
truncate its fixed oracle field as in (C.4.7.NT), take width to infinity and
remove that cutoff using its joint second-moment limit. Scalar
contractions converge by the two-factor RMS inequality. The finite rank
expansion handles learned actions in both orientations. The finite
initial readout RMS and supremum tend to zero; the same finite induction
propagates this additive discrepancy while preserving the actual finite
initialization.

At this fixed \((\nu,h)\), recomputed proxy fields and assigned
velocities consequently differ from their oracle versions by
\(o_{\mathbb P}(1)\). The proxy lies on a deterministic enlargement
of the ball (C.4.7.NE) with probability tending to one. Its increment norm and
pairings have exactly their HS interpretation: if
\(K=\sum_i a_i\otimes b_i\) and
\(\widetilde K=\sum_j\tilde a_j\otimes\tilde b_j\), then
\[
 \langle K,\widetilde K\rangle_{\rm HS}
       =\sum_{i,j}\langle a_i,\tilde a_j\rangle
                    \langle b_i,\tilde b_j\rangle.
 \tag{C.4.7.NK}
\]
The finite Frobenius contraction of ranks \(a_ib_i^T/n\) is the same
sum of normalized pairings. Each is an identified same-layer second
moment, so (C.4.7.NK) involves no cross-carrier subtraction.

For any fixed cutoff R, positive-part second-moment convergence, (C.4.7.NP)
and (C.4.7.NH) imply at the finitely many proxy nodes
\[
 \tau_R(\bar c_n(t_k))+
       \int\tau_R(\bar Q_n(t_k,u))\,d\nu
                         \le M'e^{-a'R}+o_{\mathbb P}(1).
 \tag{C.4.7.NPT}
\]
These are normalized finite RMS tails. The constants \(M',a'>0\) are
independent of the chosen law and mesh in the smaller neighborhood;
fixed cutoff rescaling changes only these constants. No growing
transcript has been submitted to a fixed-program theorem.

Let \(\lambda_j\to\mu\) in \(\mathcal W_1\), with
\(n_j\to\infty\). The actual laws may here be arbitrary Borel laws;
only the proxy law is finite. Compare actual GF with the proxy on their
common finite carrier, using the law-independent finite energy bounds
and (C.4.7.NC). A proxy interpolant differs from its preceding node by at most
\(V'h+o_{\mathbb P}(1)\). On any interval \([b_0,b_1]\) of length
at most \(\ell\), the sum distance E obeys
\[
 \sup_{b_0\le t\le b_1}E(t)
 \le e^{C(1+R)\ell}E(b_0)
   +C\ell e^{C(1+R)\ell}
    \{(1+R)(\mathcal W_1(\lambda_j,\nu)+h)
                     +M'e^{-a'R}+o_{\mathbb P}(1)\}.
 \tag{C.4.7.NAP}
\]
The proxy velocity defect is included in the fixed-program probability
error. Every random error here is for fixed \(\nu,h,R\).

Choose a finite time partition with \(C\ell<a'/2\). On each interval
the amplified tail in (C.4.7.NAP) tends to zero as R increases. For a required
final accuracy, choose the last interval's cutoff and its required
incoming accuracy, then the preceding interval's cutoff and incoming
accuracy, and continue backwards over the finite partition. This produces
finitely many fixed cutoffs and positive tolerances. Next choose the
finite law \(\nu\) close enough to \(\mu\), and h small enough, so
all their deterministic errors meet these tolerances. Finally take
\(j\to\infty\). The finitely many fixed-program probability errors
and \(\mathcal W_1(\lambda_j,\mu)\) vanish together. Forward induction
in (C.4.7.NAP) gives arbitrarily small finite GF/proxy raw error through40.
This choice order is why an arbitrarily small positive tail exponent
suffices. It neither asserts a finite moment bound uniform over all laws
nor requires a relation between sample count and width.

The population proxy converges in raw norm to (C.4.7.NI), while each fixed
proxy's joint node laws, action tests, and pairings converge by the
fixed-program theorem. These two comparisons prove the stated state
identification. Forward/prediction formulas are Lipschitz on the bounded
raw balls, uniformly in u. Full row bounds give input continuity, and
the velocity bound gives the needed time continuity. Finite time/input
nets, with the fixed-program limit at their nodes, yield (C.4.7.NW2).
Holding \(\lambda_j=\mu\) for all j in precisely the same comparison
proves (C.4.7.NW1), including for a nonatomic Borel law with exact loss
integration. No empirical total-variation approximation has been used.

Here are the further observation passages. In any same-carrier
comparison, applying a named bounded action costs its norm times the
input error, plus the input norm times the HS increment error if the
learned action changes. A globally Lipschitz coordinate operation
preserves \(L^2\) approximation. For a fixed bounded continuous gate
times a named \(L^2\) field, first truncate that field and restrict the
gate arguments to a compact box. On the box uniform continuity applies;
off it the joint second-moment limits give tightness and uniform
integrability. Remove the restrictions after the fixed approximation
limit. Induction over a finite observation program proves the joint
same-layer \(\mathcal W_2\) limit and all quadratic contractions in
the theorem. Keeping the initialized and current hidden fields in the
same tuple gives the paired observations. This argument admits no
arbitrary unbounded product and makes no operator-norm comparison
between carriers.

For iid data of size m, the compact partition proof is elementary.
Move both \(\mu\) and its empirical law to the representatives of a
partition with cell diameter b. The two moves cost at most \(2b\).
The remaining distance is at most half the data diameter times the sum
of cell-mass discrepancies. Each empirical cell frequency has variance
at most \(1/(4m)\), so this remaining term tends to zero in probability
for the fixed finite partition. First let m increase, then b decrease.
Thus empirical \(\mathcal W_1\) converges in probability. All proxy
events in (C.4.7.NAP) concern its fixed law and initialization, independent of
the observations. Combining these events and the data-distance event
by a finite union bound proves the iid conclusion for arbitrary
\(m_j,n_j\to\infty\).

##### C.4.7.6. Nonlinear variation and the finite nonlinear limit

Continue with the strong raw flows, common Gaussian carrier, neighborhood,
and finite-GF capture constructed above, on \(T=40\). All field, action,
raw-norm and data-space notation is unchanged. Law integrals written in
\((u,y)\) use the pushforward under \(u=x/\sqrt2\). Put \(D_Y=2+2Y\),
an upper bound for the diameter of \(\mathcal Z\) in its stated metric.

Write \(\theta_*=\theta_{\nu_*}\). Its identification with the reference
of C.4.6 follows from the strong equation, common initialization and
reached-state uniqueness already proved. For every \(\nu\in\mathcal P(\mathcal Z)\),
put \(\sigma=\nu-\nu_*\) and

\[
 \mu_{\epsilon,\nu}=(1-\epsilon)\nu_*+\epsilon\nu,
 \qquad
 \epsilon_Y=\min\{1/2,\delta_Y/(2D_Y)\}>0.
 \tag{C.4.7.NV-radius}
\]

The radius \(\delta_Y\) is chosen below inside the neighborhood on which
the preceding construction has uniform constants. Coupling unchanged
mass to itself gives
\(\mathcal W_1(\mu_{\epsilon,\nu},\nu_*)\le\epsilon D_Y\le\delta_Y/2\).
Thus every \(\nu\), including every nonatomic law, and the whole closed
interval \(0\le\epsilon\le\epsilon_Y\) are admitted.

The conclusions proved here are

\[
 \sup_{\nu\in\mathcal P(\mathcal Z)}\sup_{0\le t\le T}
 \|\theta_{\mu_{\epsilon,\nu}}(t)-\theta_*(t)
                  -\epsilon\dot\theta_\sigma(t)\|_{\rm raw}
       =o(\epsilon),
 \tag{C.4.7.NV-raw-remainder}
\]

\[
 \sup_{\nu\in\mathcal P(\mathcal Z)}
 \sup_{\substack{0\le t\le T\\x\in\sqrt2S^1}}
 |f_{\mu_{\epsilon,\nu}}(t,x)-f_{\nu_*}(t,x)
                   -\epsilon\mathscr D_\sigma f(t,x)|
       \le\epsilon\omega_Y(\epsilon),
 \qquad \omega_Y(\epsilon)\longrightarrow0,
 \tag{C.4.7.NV-prediction-remainder}
\]

where \(\dot\theta_\sigma\) and \(\mathscr D_\sigma f\) are exactly the
raw variation and prediction response of C.4.6. The modulus is deterministic
and independent of \(\nu\). The proof first turns active query tails into
passive tails using a small probe atom. Radial saturation then controls
the unbounded clock weights on the actual paths. The resulting forcing
continuity and compact response family justify Taylor expansion along
those response directions and a comparison with the nonlinear flow.

###### 1. Probe atoms and passive exponential tails

Write \(U_r=\{\mu:\mathcal W_1(\mu,\nu_*)<r\}\). Choose fixed
\(0<r_0<r_1<\rho\), where \(\rho>0\) is the radius of the preceding
source construction, and ultimately take \(\delta_Y\le r_0\).
The already proved active-tail estimate (C.4.7.NH) supplies \(a,M,h_1>0\) such
that every finite law \(\lambda\in U_{r_1}\), every finite raw Euler
mesh of maximal step at most \(h_1\) through \(T\), and every node \(k\)
obey

\[
 \int \tau_R(Q_{\lambda,k}(u))\,d\lambda(u,y)
       \le M e^{-aR},\qquad
 \tau_R(P):=\|P\mathbf1_{|P|>R}\|_{H_1},\qquad R\ge1.
 \tag{C.4.7.NV-active-tail}
\]

The readout and raw state bounds (C.4.7.NE), and the same-mesh law estimate
(C.4.7.NLM), are uniform on this ball. In particular there are \(C_0,q_0>0\)
and \(\alpha>0\), independent of the mesh, such that

\[
 \max_k\|\theta_{\lambda,k}-\theta_{\kappa,k}\|_{\rm raw}
       \le C_0\mathcal W_1(\lambda,\kappa)^\alpha,
 \qquad \mathcal W_1(\lambda,\kappa)\le q_0.
 \tag{C.4.7.NV-same-mesh}
\]

There is no additive mesh error in this estimate: both recursions use
the identical mesh. This permits probe masses tending to zero at a
fixed mesh.

For completeness, \(Q(u)\) is Lipschitz in raw state on these bounded
sets with their common readout supremum bound. At the same input, factor
subtraction gives

\[
 \begin{aligned}
 \|Z^{(2)}-\bar Z^{(2)}\|_2
 &\le\|K-\bar K\|_{\rm HS}
             +\|\bar A\|\|w-\bar w\|_2,\\
 \|\Delta^{(2)}-\bar\Delta^{(2)}\|_2
 &\le\|c-\bar c\|_2
             +2\|\bar c\|_\infty\|Z^{(2)}-\bar Z^{(2)}\|_2,\\
 \|Q-\bar Q\|_2
 &\le\|K-\bar K\|_{\rm HS}\|\Delta^{(2)}\|_2
             +\|\bar A\|\|\Delta^{(2)}-\bar\Delta^{(2)}\|_2.
 \end{aligned}
 \tag{C.4.7.NV-query-comparison}
\]

Fix \(\lambda\in U_{r_0}\) with finite support and any passive
\(u\in S^1\). The label zero is allowed. Define

\[
 \lambda_\eta=(1-\eta)\lambda+\eta\delta_{(\sqrt2u,0)},
 \qquad
 0<\bar\eta<\min\{1,(r_1-r_0)/D_Y,q_0/D_Y\}.
 \tag{C.4.7.NV-probe-law}
\]

For \(0<\eta\le\bar\eta\), the direct mixture coupling gives
\(\mathcal W_1(\lambda,\lambda_\eta)\le D_Y\eta\), so both laws
are in \(U_{r_1}\). On their common mesh, (C.4.7.NV-same-mesh) and
(C.4.7.NV-query-comparison) give
\(\|Q_{\lambda,k}(u)-Q_{\lambda_\eta,k}(u)\|_2\le C_1\eta^\alpha\).
The selected atom has mass at least \(\eta\), even if it coincides with
an old atom. Hence (C.4.7.NV-active-tail), for \(R\ge2\), gives

\[
 \tau_{R/2}(Q_{\lambda_\eta,k}(u))
       \le\eta^{-1}M e^{-aR/2}.
\]

The pointwise alternatives \( |P'|\le R/2\) and \( |P'|>R/2\)
on \( |P|>R\) imply
\(\tau_R(P)\le2\|P-P'\|_2+2\tau_{R/2}(P')\). Therefore

\[
 \tau_R(Q_{\lambda,k}(u))
       \le2C_1\eta^\alpha+2\eta^{-1}M e^{-aR/2}.
 \tag{C.4.7.NV-probe-tail}
\]

Choose \(\eta=\bar\eta\exp\{-aR/[2(1+\alpha)]\}\) and set
\(b=a\alpha/[2(1+\alpha)]>0\). Both terms have the same exponential
decay, so a fixed \(C_2<\infty\) satisfies

\[
 \sup_{\substack{\lambda\in U_{r_0}\text{ finite}\\
                  \text{admitted meshes},\ k,\ u\in S^1}}
 \tau_R(Q_{\lambda,k}(u))\le C_2e^{-bR},\qquad R\ge2.
 \tag{C.4.7.NV-passive-tail}
\]

There was no division by any preexisting atom weight. The only inverse
mass in (C.4.7.NV-probe-tail) is paid for by the quantitative change of law.

The bound \(\Pr(|Q|>R)\le R^{-2}\tau_R(Q)^2\) and the identity

\[
 \mathbb E e^{\beta|Q|}
       =1+\int_0^\infty\beta e^{\beta R}\Pr(|Q|>R)\,dR
\]

show that \(\beta=b\) gives a common finite exponential moment:
the portion \(0\le R\le2\) is bounded directly, and the remaining
integrand is bounded by a constant times \(e^{-bR}\).
For each \(\mu\in U_{r_0}\), take its finite-law, fine-mesh strong
approximations within \(U_{r_0}\). The readout supremum bound passes
to their strong \(L^2\) limit by an almost surely convergent subsequence.
Equation (C.4.7.NV-query-comparison) then passes each passive query to that
limit in \(L^2\). At any deterministic time use preceding mesh nodes;
the vanishing state interpolation error has the same conclusion.
For each fixed time and input, apply convergence in probability to
\(\min(N,e^{\beta|Q|})\), take expectations using boundedness, then
let \(N\to\infty\). The constants are unchanged for all parameters:

\[
 \sup_{\mu\in U_{r_0},\,0\le t\le T,\,u\in S^1}
           \mathbb E_1 e^{\beta|Q_\mu(t,u)|}\le M_Q<\infty.
 \tag{C.4.7.NV-passive-moment}
\]

This is uniformity of individual query marginals. A coordinate
supremum over time and inputs has not been placed inside this moment.

###### 2. Radial saturation and the actual inverse-gate forcing

The strong raw path has square-integrable velocity in time, so Fubini
gives almost surely absolutely continuous row representatives. Since
\(\cosh^2 z=1+\sinh^2z\ge1+z^2\ge2|z|\),
\(|z|\phi'(z)\le1/2\). The exact row equation consequently gives,
for almost every coordinate and time,

\[
 \frac d{dt}|w_\mu(t)|^2
 =-4\int r_\mu(t,u,y)Q_\mu(t,u)
       (w_\mu(t)\cdot u)\phi'(w_\mu(t)\cdot u)\,d\mu
 \le2\int |r_\mu(t,u,y)|\,|Q_\mu(t,u)|\,d\mu.
 \tag{C.4.7.NV-radial}
\]

The preceding energy identity and \(c(0)=0\) give
\(\|c_\mu(t)\|_2\le Y\sqrt T\), so
\(|r_\mu(t,u,y)|\le R_{\rm rad}:=Y(1+\sqrt T)\). Define

\[
 J_\mu=\int_0^T\int|Q_\mu(s,u)|\,d\mu(u,y)\,ds,
 \qquad W_\mu=\sup_{0\le t\le T}|w_\mu(t)|.
\]

The jointly measurable representatives needed here follow from the
strongly continuous query map and its separable \(L^2\) range; finite
simple approximations give representatives on the product of parameter
space and \(\Omega_1\). Equation (C.4.7.NV-passive-moment) and Fubini give
\(J_\mu<\infty\) almost surely. Integrating (C.4.7.NV-radial) yields

\[
 W_\mu^2\le|g|^2+2R_{\rm rad}J_\mu.
 \tag{C.4.7.NV-row-envelope}
\]

For \(0\le\lambda T\le\beta\), Jensen's inequality for the probability
measure \(T^{-1}\,ds\,d\mu\), followed by (C.4.7.NV-passive-moment), gives

\[
 \mathbb E_1e^{\lambda J_\mu}
 \le\frac1T\int_0^T\int
        \mathbb E_1e^{\lambda T|Q_\mu(s,u)|}\,d\mu\,ds
 \le M_Q.
 \tag{C.4.7.NV-integrated-query}
\]

Choose \(0<\gamma\le\min\{1/8,\beta/(8R_{\rm rad}T)\}\). Cauchy–Schwarz,
(C.4.7.NV-row-envelope), and (C.4.7.NV-integrated-query) imply

\[
 \sup_{\mu\in U_{r_0}}\mathbb E_1e^{\gamma W_\mu^2}
 \le(\mathbb E_1e^{2\gamma|g|^2})^{1/2}
      (\mathbb E_1e^{4\gamma R_{\rm rad}J_\mu})^{1/2}
 \le(1-4\gamma)^{-1/2}M_Q^{1/2}=:M_W<\infty.
 \tag{C.4.7.NV-row-square-moment}
\]

Indeed the two independent standard Gaussian root coordinates give
\(\mathbb E e^{2\gamma|g|^2}=(1-4\gamma)^{-1}\), by combining their
normal densities with the exponential. No independence between \(g\)
and the evolved queries was used.

For every separately fixed positive integer \(p\), the exponential
series in (C.4.7.NV-passive-moment) gives
\(\mathbb E_1|Q_\mu(t,u)|^{2p}\le M_Q(2p)!/\beta^{2p}\).
Since \(\cosh^2(w_j)\le e^{2W_\mu}\) and
\(4pW_\mu\le\gamma W_\mu^2+4p^2/\gamma\), Cauchy–Schwarz gives

\[
 \sup_{\mu\in U_{r_0},\,t\le T,\,u\in S^1,\,j=1,2}
 \mathbb E_1\{\cosh^2(w_{\mu,j}(t))|Q_\mu(t,u)|\}^{p}
 \le e^{2p^2/\gamma}M_W^{1/2}
             \{M_Q(2p)!/\beta^{2p}\}^{1/2}<\infty.
 \tag{C.4.7.NV-weighted-moments}
\]

Define the actual inverse-gate forcing field on \(\Omega_1\) by

\[
 \mathcal I_{\mu,j}(t,u)=
 u_j\cosh^2(w_{\mu,j}(t))\phi'(w_\mu(t)\cdot u)Q_\mu(t,u).
 \tag{C.4.7.NV-clock-force}
\]

The factor \(u_j\) retains the zero contribution at the other reference
axis. Taking \(p=3\) in (C.4.7.NV-weighted-moments) proves a common bound
\(\mathbb E_1|\mathcal I_{\mu,j}(t,u)|^3\le C_3\), hence

\[
 \sup_{\mu\in U_{r_0},\,t\le T,\,u\in S^1,\,j=1,2}
 \mathbb E_1\bigl[|\mathcal I_{\mu,j}(t,u)|^2
                   \mathbf1_{|\mathcal I_{\mu,j}(t,u)|>R}\bigr]
       \le C_3/R\longrightarrow0.
 \tag{C.4.7.NV-forcing-UI}
\]

These estimates concern the actual reached family. They assert no
\(L^p\)-bounded action of \(A_0\) or \(A_0^*\) beyond their given
\(L^2\) actions.

###### 3. The exact clock equation

Set

\[
 F(z)=z/2+\sinh(2z)/4,\qquad \psi=F^{-1},\qquad
 F'(z)=\cosh^2z=1/\phi'(z),\qquad
 \psi'(X)=\phi'(\psi(X)).
 \tag{C.4.7.NV-clock}
\]

The positive derivative and limits at infinity make \(F\) a bijection;
\(\psi\) is 1-Lipschitz, with bounded Lipschitz derivative because
\(\psi''=(\phi''\circ\psi)(\phi'\circ\psi)\) is bounded. Write

\[
 \Theta_\mu=(X_\mu,K_\mu,c_\mu),\qquad
 X_{\mu,j}=F(w_{\mu,j}),\qquad
 \mathcal V=L^2(\Omega_1;\mathbb R^2)
             \oplus\mathcal S_2(H_1,H_2)\oplus H_2,
\]

with its square-sum Hilbert norm. The initial clock is \(F(g_j)\in L^2\):
\(|F(g_j)|\le |g_j|/2+e^{2|g_j|}/4\), and
\(\mathbb E e^{a|g_j|}\le2e^{a^2/2}\) for every finite \(a\ge0\).

The clock is justified without assuming an unbounded coordinate map
preserves all of \(L^2\). Apply the scalar chain rule to the almost
surely absolutely continuous raw row. Its transformed derivative is
\(-2\int r_\mu\mathcal I_{\mu,j}\,d\mu\). The residual bound and
(C.4.7.NV-forcing-UI) make this an integrable \(H_1\)-valued velocity on
\([0,T]\). Fubini and the scalar integral identity therefore identify
\(X_{\mu,j}\) with an absolutely continuous \(H_1\) curve starting at
\(F(g_j)\).

At a clock state \(\Theta=(X,K,c)\), recover \(w_j=\psi(X_j)\) and
the forward and backward fields defined above. For the reference axes put \(r_j=f(e_j)-y_j\),
\(y_1=1,y_2=-1\), and define

\[
 \begin{aligned}
 (\mathcal F_0(\Theta))_{X,j}&=-r_jQ(e_j),\\
 (\mathcal F_0(\Theta))_K
    &=-\sum_{j=1}^2r_j\Delta^{(2)}(e_j)\otimes H^{(1)}(e_j),\\
 (\mathcal F_0(\Theta))_c&=-\sum_{j=1}^2r_jH^{(2)}(e_j).
 \end{aligned}
 \tag{C.4.7.NV-reference-field}
\]

Here \(F'(w_j)\phi'(w_j)=1\) cancels the first gate exactly, and the
two atom masses cancel the loss factor two. For an arbitrary probability
law \(\nu\), define on every reached state

\[
 \mathcal Q_\nu(\Theta)=-2\int r(u,y)
 \left((\mathcal I_j(\Theta,u))_{j=1,2},
       \Delta^{(2)}(u)\otimes H^{(1)}(u),H^{(2)}(u)\right)d\nu(u,y),
 \qquad \mathcal B_\nu=\mathcal Q_\nu-\mathcal F_0.
 \tag{C.4.7.NV-law-field}
\]

For reached states all these Bochner integrals exist: the integrands
have separable measurable ranges. For the first component, truncate its
continuous coordinate formula at a fixed level. The resulting bounded
coordinate map is strongly measurable; (C.4.7.NV-forcing-UI) makes these
truncations converge in \(L^2\), uniformly in the input. Their limit is
therefore strongly measurable and has a uniform \(L^2\) bound. The other
components are strongly continuous in the input and obey the raw bounds.
Integration against a probability law is consequently legitimate.
The exact contamination equation is

\[
 \Theta_{\epsilon,\nu}'=
 \mathcal F_0(\Theta_{\epsilon,\nu})
       +\epsilon\mathcal B_\nu(\Theta_{\epsilon,\nu}),
 \qquad \Theta_{\epsilon,\nu}(0)=\Theta_*(0).
 \tag{C.4.7.NV-exact-equation}
\]

The field \(\mathcal F_0\) is defined on all of \(\mathcal V\).
The contaminated field in (C.4.7.NV-law-field) is used only where its
weighted integrals have just been proved to exist.

###### 4. Reference comparison with one bounded readout endpoint

On sets with bounded \(\|K\|_{\rm HS}\) and \(\|c\|_2\), if at
least one of two compared readouts has a fixed \(L^\infty\) bound, then

\[
 \|\mathcal F_0(\Theta)-\mathcal F_0(\widetilde\Theta)\|_{\mathcal V}
       \le L\|\Theta-\widetilde\Theta\|_{\mathcal V}.
 \tag{C.4.7.NV-reference-Lipschitz}
\]

To verify this, let \(M_A\) bound the two action norms and \(M_c\)
bound the \(L^2\) readout norms, and suppose \(\|c\|_\infty\le H_c\).
Uniformly over \(u\in S^1\),

\[
 \|H^{(1)}-\widetilde H^{(1)}\|_2\le\|X-\widetilde X\|_2,
 \quad
 \|Z^{(2)}-\widetilde Z^{(2)}\|_2
       \le M_A\|X-\widetilde X\|_2+\|K-\widetilde K\|_{\rm HS}.
\]

Use the bounded endpoint in the precise factorization

\[
 c\phi'(Z^{(2)})-\widetilde c\phi'(\widetilde Z^{(2)})
 =(c-\widetilde c)\phi'(\widetilde Z^{(2)})
       +c\{\phi'(Z^{(2)})-\phi'(\widetilde Z^{(2)})\}.
\]

Its norm is at most
\(\|c-\widetilde c\|_2+2H_c\|Z^{(2)}-\widetilde Z^{(2)}\|_2\).
The prediction difference is at most
\(\|c-\widetilde c\|_2+M_c\|Z^{(2)}-\widetilde Z^{(2)}\|_2\).
Actual adjunction then bounds

\[
 \|Q-\widetilde Q\|_2
 \le M_A\|\Delta^{(2)}-\widetilde\Delta^{(2)}\|_2
             +M_c\|K-\widetilde K\|_{\rm HS}.
\]

Substitution into (C.4.7.NV-reference-field), and
\(\|a\otimes b-\tilde a\otimes\tilde b\|_{\rm HS}
\le\|a-\tilde a\|_2\|b\|_2+\|\tilde a\|_2\|b-\tilde b\|_2\),
prove (C.4.7.NV-reference-Lipschitz). Its row component contains no product
of an arbitrary clock difference with an unbounded backward query.

The actual readouts obey \(\|c_\mu(t)\|_\infty\le2YT\), and
(C.4.7.NV-forcing-UI) bounds \(\mathcal B_\nu(\Theta_{\epsilon,\nu})\)
uniformly in \(\nu,\epsilon,t\). Subtract (C.4.7.NV-exact-equation) from
the reference equation. Iterating the scalar integral inequality
\(v(t)\le a+L\int_0^tv(s)ds\) gives \(v(t)\le ae^{Lt}\), so

\[
 \sup_{\nu\in\mathcal P(\mathcal Z),\,t\le T}
       \|\Theta_{\epsilon,\nu}(t)-\Theta_*(t)\|_{\mathcal V}
       \le C_{\rm var}\epsilon.
 \tag{C.4.7.NV-clock-first-order}
\]

This first-order displacement bound is a consequence of the reached
forcing estimates.

###### 5. Continuity of the forcing along the actual paths

We claim

\[
 \sup_{\nu,\,t\le T,\,u\in S^1,\,j=1,2}
 \|\mathcal I_j(\Theta_{\epsilon,\nu}(t),u)
             -\mathcal I_j(\Theta_*(t),u)\|_2\longrightarrow0.
 \tag{C.4.7.NV-force-continuity}
\]

If it failed, choose \(\epsilon_m\downarrow0\), laws \(\nu_m\),
times \(t_m\), and inputs \(u_m\) along which the difference is bounded
away from zero. Pass to a subsequence with \(t_m\to t\), \(u_m\to u\)
and a fixed index \(j\). By (C.4.7.NV-clock-first-order) and reference
continuity, \(\Theta_{\epsilon_m,\nu_m}(t_m)\to\Theta_*(t)\)
strongly in \(\mathcal V\). The lower features converge in \(L^2\),
using \(\psi\)'s Lipschitz bound and
\(\|(u_m-u)\cdot w_*(t)\|_2\le|u_m-u|\|w_*(t)\|_2\).
The action and upper features then converge. The bounded readout
factorization in the preceding subsection gives convergence of
\(\Delta^{(2)}\) and \(Q\) in \(L^2\).

The continuous finite-dimensional function
\(u_j\cosh^2(w_j)\phi'(w\cdot u)\) converges in measure under this
convergence of its arguments. Its product with the convergent query
therefore converges in measure to the limiting \(\mathcal I_j\).
Equation (C.4.7.NV-forcing-UI) upgrades this to \(L^2\) convergence.
Explicitly, uniformly integrable squares make the integral of the
squared difference on any set of sufficiently small probability
uniformly small; on the complement of the event that its magnitude
exceeds \(\eta\), its squared integral is at most \(\eta^2\).
Convergence in measure and then \(\eta\downarrow0\) prove the claim.
The same argument applies to the reference sequence \((t_m,u_m)\);
the triangle inequality contradicts the assumed failure.

Residual differences tend to zero uniformly by
(C.4.7.NV-clock-first-order), while their absolute values and all weighted
force norms are uniformly bounded. The remaining components of
(C.4.7.NV-law-field) have the ordinary Lipschitz differences already proved.
Integration against any probability law is bounded by the supremum
of the integrand norm. Thus

\[
 \sup_{\nu,\,t\le T}
 \|\mathcal B_\nu(\Theta_{\epsilon,\nu}(t))
             -\mathcal B_\nu(\Theta_*(t))\|_{\mathcal V}
       \longrightarrow0.
 \tag{C.4.7.NV-source-defect}
\]

With \(\epsilon=0\), the same argument proves joint strong continuity
of the atom forcing in time, input and label. In particular all
reference law integrals below are continuous in time.

###### 6. The linear equation and its compact family of directions

At a reference clock state and for \(v=(\xi,B,d)\in\mathcal V\), define
the following directional fields; the prefix \(\eta\) denotes a
directional variation, not a time derivative:

\[
 \begin{aligned}
 \eta w_j&=\phi'(w_j)\xi_j,&
 \eta H^{(1)}(u)&=\phi'(w\cdot u)\sum_j u_j\eta w_j,\\
 \eta Z^{(2)}(u)&=A\eta H^{(1)}(u)+BH^{(1)}(u),&
 \eta H^{(2)}(u)&=\phi'(Z^{(2)}(u))\eta Z^{(2)}(u),\\
 \eta f(u)&=\langle d,H^{(2)}(u)\rangle
                      +\langle c,\eta H^{(2)}(u)\rangle,\\
 \eta\Delta^{(2)}(u)&=d\phi'(Z^{(2)}(u))
                  +c\phi''(Z^{(2)}(u))\eta Z^{(2)}(u),\\
 \eta Q(u)&=A^*\eta\Delta^{(2)}(u)+B^*\Delta^{(2)}(u).
 \end{aligned}
 \tag{C.4.7.NV-directional-fields}
\]

The bounded linear generator on \(\mathcal V\) is

\[
 \begin{aligned}
 (\mathcal L(t)v)_{X,j}
   &=-(\eta f(e_j))Q(e_j)-r_j\eta Q(e_j),\\
 (\mathcal L(t)v)_K
   &=-\sum_j\bigl[(\eta f(e_j))\Delta^{(2)}(e_j)\otimes H^{(1)}(e_j)
          +r_j\eta\Delta^{(2)}(e_j)\otimes H^{(1)}(e_j)
          +r_j\Delta^{(2)}(e_j)\otimes\eta H^{(1)}(e_j)\bigr],\\
 (\mathcal L(t)v)_c
   &=-\sum_j\bigl[(\eta f(e_j))H^{(2)}(e_j)+r_j\eta H^{(2)}(e_j)\bigr].
 \end{aligned}
 \tag{C.4.7.NV-generator}
\]

Every map is bounded uniformly in \(t\le T\): the only coefficient
multiplying an unrestricted upper preactivation variation is
\(c\phi''(Z^{(2)})\in L^\infty\). The remaining products are bounded
multipliers, Hilbert scalar pairings, or Hilbert–Schmidt ranks.
In particular no \(Q(e_j)\xi_j\) pointwise product occurs.

The family \(\mathcal L(t)\) is strongly continuous. To justify its
multiplier steps, if uniformly bounded functions converge in measure,
their product with a fixed \(L^2\) field converges in \(L^2\): truncate
the fixed field, use bounded convergence in measure on its bounded
part, and then remove its square-integrable tail. The reference fields
are strongly continuous, their action increments are HS-continuous,
and their readout factors are uniformly bounded. Applying this
observation successively in (C.4.7.NV-directional-fields) and
(C.4.7.NV-generator) proves the assertion for each fixed \(v\).

For clarity, a uniformly bounded strongly continuous generator has a
unique strong propagator \(U(t,s)\) on this finite interval. Starting
from \(v\), iterated integrals of the generator have norms at most
\(\|v\|L_*^k(t-s)^k/k!\), where \(L_*=\sup_t\|\mathcal L(t)\|\).
Their uniformly convergent series solves the integral equation and
has norm at most \(e^{L_*(t-s)}\|v\|\). Iterating the difference
equation proves uniqueness with the same factorial bound.
Consequently the solution of

\[
 v_\sigma'=\mathcal L(t)v_\sigma+b_\sigma(t),\qquad
 b_\sigma(t)=\mathcal B_\nu(\Theta_*(t)),\qquad v_\sigma(0)=0
 \tag{C.4.7.NV-response-equation}
\]

is \(v_\sigma(t)=\int_0^tU(t,s)b_\sigma(s)ds\), and the map from
continuous forcing to \(C([0,T];\mathcal V)\) is bounded and linear,
with norm at most \(Te^{L_*T}\). Substitution into the integral equation
is justified by this integrable bound. The forcing is continuous, so
the response is strongly \(C^1\).

The atom map

\[
 z=(x,y)\longmapsto
 \bigl[t\longmapsto
   \mathcal Q_{\delta_z}(\Theta_*(t))-\mathcal F_0(\Theta_*(t))\bigr]
       \quad\hbox{in }C([0,T];\mathcal V)
 \tag{C.4.7.NV-atom-curves}
\]

is continuous on compact \(\mathcal Z\), by the joint continuity proved above.
Its image is compact. Each \(b_{\nu-\nu_*}\) is a Bochner average of
this image and belongs to its closed convex hull. That hull is compact:
cover the image by finitely many balls of radius \(h\); every convex
combination is within \(h\) of the convex hull of their centers. The
latter hull is the continuous image of a finite-dimensional compact
simplex. This gives total boundedness for each \(h>0\), and closure
in the complete curve space gives compactness.

The bounded linear solution map in (C.4.7.NV-response-equation) therefore gives

\[
 \{v_{\nu-\nu_*}:\nu\in\mathcal P(\mathcal Z)\}
       \text{ has compact closure in }C([0,T];\mathcal V),
 \quad
 \mathcal C:=\overline{\{v_{\nu-\nu_*}(t):\nu\in\mathcal P(\mathcal Z),\ t\le T\}}
       \text{ is compact in }\mathcal V.
 \tag{C.4.7.NV-compact-directions}
\]

The second statement uses continuity of evaluation on the product of
the compact closure of the curve family and compact time.

The equation is exactly the C.4.6 equation, rather than a separately
defined response with an unspecified identification. That section
uses \(X_j^{\rm old}=F(w_j)-F(g_j)\); our clock differs by the same
fixed \(L^2\) initial field for every law. Clock differences and tangent
coordinates thus coincide. At the reference axes
(C.4.7.NV-reference-field) is \(X_j'=-r_jQ(e_j)\), and
(C.4.7.NV-directional-fields) agrees term by term with C.4.6.T14. Formula
(C.4.7.NV-generator) is the product differentiation of this field, hence
the operator in C.4.6.T6. Moreover \(\cosh^2(w_j)=1/\phi'(w_j)\), so

\[
 b_\sigma(t)=-2\int r_*(t,u,y)
 \left(
   \left(u_j\frac{\phi'(w_*(t)\cdot u)}{\phi'(w_{*,j}(t))}
                 Q_*(t,u)\right)_{j=1,2},
   \Delta_*^{(2)}(t,u)\otimes H_*^{(1)}(t,u),H_*^{(2)}(t,u)
 \right)d\sigma(u,y),
 \tag{C.4.7.NV-exact-source}
\]

which is C.4.6.T5 including the residual, sign, factor two and reference
subtraction. Uniqueness of the linear equation identifies \(v_\sigma\)
with that section's response. In particular

\[
 \dot\theta_\sigma(t)=
 ((\phi'(w_{*,j}(t))\xi_{\sigma,j}(t))_{j=1,2},B_\sigma(t),d_\sigma(t)),
 \qquad
 \mathscr D_\sigma f(t,\sqrt2u)=\eta f_*(t,u)[v_\sigma(t)].
 \tag{C.4.7.NV-response-identification}
\]

###### 7. Taylor consistency on compact directions

We first prove the needed \(L^2\) fact. Let \(N\) be a scalar or
finite-dimensional function with bounded Lipschitz first derivative,
and let \(v\) range over a relatively compact subset of \(L^2\). Then

\[
 \sup_{a,v}
 \left\|\frac{N(a+\epsilon v)-N(a)}{\epsilon}-DN(a)v\right\|_2
       \longrightarrow0,
 \tag{C.4.7.NV-compact-Taylor}
\]

where bases \(a\) are arbitrary whenever the expressions are defined.
On \( |v|\le R\), the scalar integral remainder is bounded by
\(C\epsilon R|v|\); on \( |v|>R\), it is bounded by \(C|v|\).
Compact \(L^2\) families have uniformly vanishing square tails.
Indeed a finite \(L^2\) net, and
\(\|v\mathbf1_{|v|>2R}\|_2
\le2\|v-v_0\|_2+2\|v_0\mathbf1_{|v_0|>R}\|_2\),
reduce the claim to finitely many square-integrable fields. Choose
\(R\) first and then \(\epsilon\) to prove (C.4.7.NV-compact-Taylor),
uniformly in the bases. The argument works for a family of functions
with a common derivative bound and Lipschitz constant.

Apply it to \(\psi\), to the finite-dimensional map
\(X\mapsto\phi(\sum_j u_j\psi(X_j))\), and to \(\phi\) and
\(\phi'\) at the upper preactivation. Their first derivatives are
bounded and Lipschitz uniformly over \(u\in S^1\); for the second
map use \( |u|=1\), bounded \(\psi',\psi''\), and bounded
\(\phi',\phi''\). The needed further derivatives of tanh are bounded.

At compact reference times and for \(v\in\mathcal C\), the linear
directions in (C.4.7.NV-directional-fields) form compact \(L^2\) families,
also when \(u\) varies over the circle. To check this, the bounded
multiplier argument from the preceding subsection gives joint strong
continuity in \((t,u)\) on each fixed direction. Uniform operator bounds
and a finite net extend that continuity to compact direction sets.
The action \(A(t)\) is norm-continuous because \(K(t)\) is HS-continuous.
For \(BH^{(1)}(t,u)\), continuity follows from the HS action bound.
Thus every successive linear image is the continuous image of the
relevant compact parameter product.

These facts expand the lower and upper features with precisely the
linear terms in (C.4.7.NV-directional-fields), with \(o(\epsilon)\) errors
uniform in \(t,u,v\in\mathcal C\). Bilinear action terms such as
\(\epsilon B[H^{(1)}_{\rm new}-H^{(1)}_*]\) are \(O(\epsilon^2)\)
in \(L^2\). If the upper preactivation already has an \(o(\epsilon)\)
error after its linear term, the Lipschitz bounds for \(\phi,\phi'\)
pass that error before applying (C.4.7.NV-compact-Taylor).

There is one pointwise product requiring a further check. In the
expansion of \((c_*+\epsilon d)\phi'(Z^{(2)}_{\rm new})\), the cross
term divided by \(\epsilon\) is

\[
 d\{\phi'(Z^{(2)}_{\rm new})-\phi'(Z^{(2)}_*)\}.
 \tag{C.4.7.NV-backward-cross-term}
\]

The bracket is uniformly bounded and has \(L^2\) norm \(O(\epsilon)\).
For any fixed \(R\), its product with \(d\mathbf1_{|d|\le R}\)
therefore tends uniformly to zero in \(L^2\). The complementary norm
is at most \(2\|\phi'\|_\infty\|d\mathbf1_{|d|>R}\|_2\),
uniformly small by compactness of the \(d\) directions. This proves
that (C.4.7.NV-backward-cross-term) is \(o(1)\) in \(L^2\). The other upper
backward Taylor remainder is multiplied by the bounded reference
readout. After actual adjunction, the remaining action cross term is
bounded by \(\epsilon\|B\|_{\rm HS}\) times an \(O(\epsilon)\)
backward difference. Prediction products are scalar pairings and
middle-field products are Hilbert–Schmidt ranks; their cross terms
are \(O(\epsilon^2)\) by Cauchy–Schwarz and the rank norm identity.
Residual differences have the same scalar expansion.

Substitution of these expansions into every component of
(C.4.7.NV-reference-field) proves

\[
 \sup_{t\le T,\,v\in\mathcal C}
 \|\mathcal F_0(\Theta_*(t)+\epsilon v)
       -\mathcal F_0(\Theta_*(t))-\epsilon\mathcal L(t)v\|_{\mathcal V}
       =o(\epsilon).
 \tag{C.4.7.NV-field-Taylor}
\]

The same expansions of \(\psi\) and the scalar predictor prove their
corresponding \(o(\epsilon)\) formulas, including the supremum over
all \(u\in S^1\). These are Taylor estimates on compact directions;
no estimate on an arbitrary bounded \(L^2\) direction ball is claimed.

###### 8. Comparison with the nonlinear path and return to raw state

Let \(\widetilde\Theta_{\epsilon,\nu}=
\Theta_*+\epsilon v_{\nu-\nu_*}\), and define

\[
 \rho_{\epsilon,\nu}(t)=
 \mathcal F_0(\widetilde\Theta_{\epsilon,\nu}(t))
       -\mathcal F_0(\Theta_*(t))-\epsilon\mathcal L(t)v_{\nu-\nu_*}(t).
\]

Equations (C.4.7.NV-compact-directions) and (C.4.7.NV-field-Taylor) give
\(\sup_{\nu,t}\|\rho_{\epsilon,\nu}(t)\|=o(\epsilon)\).
Subtracting the response equation from (C.4.7.NV-exact-equation), with
\(e=\Theta_{\epsilon,\nu}-\widetilde\Theta_{\epsilon,\nu}\), yields

\[
 \begin{aligned}
 e'={}&\mathcal F_0(\Theta_{\epsilon,\nu})
           -\mathcal F_0(\widetilde\Theta_{\epsilon,\nu})\\
 &+\epsilon\{\mathcal B_\nu(\Theta_{\epsilon,\nu})
                  -\mathcal B_\nu(\Theta_*)\}
       +\rho_{\epsilon,\nu},\qquad e(0)=0.
 \end{aligned}
 \tag{C.4.7.NV-error-equation}
\]

Both compared curves have uniformly bounded action and \(L^2\)
readout norms, by the raw estimates and compactness of the response
family. The actual curve has the uniform pointwise readout bound
\(2YT\). Thus (C.4.7.NV-reference-Lipschitz) applies although the response
readout need not be bounded pointwise. Equations (C.4.7.NV-source-defect)
and (C.4.7.NV-error-equation), followed by the scalar integral inequality,
give

\[
 \sup_{\nu,t\le T}
 \|\Theta_{\epsilon,\nu}(t)-\Theta_*(t)
                         -\epsilon v_{\nu-\nu_*}(t)\|_{\mathcal V}
       =o(\epsilon).
 \tag{C.4.7.NV-clock-remainder}
\]

For the raw row, first replace \(X_{\epsilon,\nu}\) by
\(X_*+\epsilon\xi_\sigma\), at an \(o(\epsilon)\) cost because
\(\psi\) is 1-Lipschitz. Then (C.4.7.NV-compact-Taylor) gives

\[
 \psi(X_*+\epsilon\xi_\sigma)-\psi(X_*)
       =\epsilon\phi'(w_*)\xi_\sigma+o(\epsilon)
       \quad\text{in }L^2,
\]

uniformly in \(\nu,t\). The other raw blocks equal their clock-state
blocks, proving (C.4.7.NV-raw-remainder) with (C.4.7.NV-response-identification).
The predictor is uniformly Lipschitz in clock state on these bounded
sets, by the forward and pairing bounds used above. Replace the actual
state by \(\widetilde\Theta_{\epsilon,\nu}\) and apply its uniform
compact-direction Taylor formula. This proves
(C.4.7.NV-prediction-remainder). A deterministic modulus can be obtained by
taking the supremum of the normalized error over \(\nu,t,u\) and
\(0<\epsilon'\le\epsilon\), and defining its value at zero to be zero.
The just-proved uniform small-o makes this supremum finite for small
\(\epsilon\) and tending to zero; uniform state and response bounds
extend it to the rest of \(0<\epsilon\le\epsilon_Y\).

###### 9. Exact bridge to finite GF

For each width retain the actual three initialized Gaussian arrays,
including the small stored readout, and use those same arrays for
every \(\epsilon\). At fixed width the exactly integrated finite loss
has a smooth parameter field, affine in \(\epsilon\). The finite
energy bound keeps all paths \(0\le\epsilon\le1\) in one compact
parameter ball on \([0,T]\), whose radius may depend on that initialized
network. On this ball the mean value formula and the scalar integral
inequality first give \(\|\theta_{n,\epsilon}-\theta_{n,0}\|_{C_t}
\le C_n\epsilon\). Dividing the integral-equation difference by
\(\epsilon\), its mean-value coefficients converge uniformly to the
reference derivative coefficients. A second integral comparison gives
the right derivative \(D_\sigma f_n\), with zero initial variation.
This is the finite derivative constructed in C.4.6.4; no width-uniform
constant is used in its construction.

Fix \(\nu\in\mathcal P(\mathcal Z)\) and \(\epsilon\in(0,\epsilon_Y]\).
Write \(\|\cdot\|_\infty\) for the supremum over
\([0,T]\times\sqrt2S^1\). The exact triangle inequality is

\[
 \begin{aligned}
 \frac{\|f_{n,\mu_{\epsilon,\nu}}-f_{n,\nu_*}
                           -\epsilon D_\sigma f_n\|_\infty}{\epsilon}
 \le{}&\omega_Y(\epsilon)\\
 &+\frac{\|f_{n,\mu_{\epsilon,\nu}}-f_{\mu_{\epsilon,\nu}}\|_\infty
            +\|f_{n,\nu_*}-f_{\nu_*}\|_\infty}{\epsilon}\\
 &+\|D_\sigma f_n-\mathscr D_\sigma f\|_\infty.
 \end{aligned}
 \tag{C.4.7.NV-finite-triangle}
\]

At this fixed positive \(\epsilon\), the two prediction errors vanish
in probability by the finite capture established above, since both
laws lie in its neighborhood. The last error vanishes in probability
by C.4.6.T10 with exactly this fixed \(\nu\), this physical horizon,
and the same Gaussian initialization. A finite union bound suffices;
independence of the three errors is unnecessary. For any \(a>0\),
choose \(\epsilon\) small enough that \(\omega_Y(\epsilon)<a/2\),
then take width to infinity at that fixed \(\epsilon\). This proves

\[
 \lim_{\epsilon\downarrow0}\limsup_{n\to\infty}
 \Pr\left[
 \frac{\displaystyle
  \sup_{\substack{0\le t\le40\\x\in\sqrt2S^1}}
  |f_{n,\mu_{\epsilon,\nu}}(t,x)-f_{n,\nu_*}(t,x)
                            -\epsilon D_\sigma f_n(t,x)|}{\epsilon}
       >a\right]=0
 \quad\text{for every fixed }\nu\in\mathcal P(\mathcal Z),\ a>0.
 \tag{C.4.7.NV-finite-nonlinear-limit}
\]

The population remainder is uniform over contaminating laws. The finite
statement fixes the law before its probability limit and takes width
before the contamination limit. It gives no uniform finite-width
remainder, no joint rate for \(\epsilon\) and width, and no supremum
over laws of finite failure probabilities. All conclusions concern
physical GF through \(40\), with the stated initialization and exact
Borel-law loss; they assert neither a raw-GD variation theorem nor an
ambient \(L^2\) Fréchet derivative or a quadratic nonlinear remainder.

##### C.4.7.7. Inherited risk and paired hidden activity

On the binary-label subclass and the intersection with the C.4.5 ball
\(\mathcal W_1(\mu,\nu_*)<\exp\{-\exp(3000)\}\), the new population
flow has risk at time40 at most \(1/4\), and both training-averaged
paired squared hidden displacements at time \(1/200\) at least
\(10^{-13}\). These are the existing subclass and times, now attached
to the constructed changed-law population trajectories.

Indeed the complete comparison in C.4.5.3 applies to actual finite GF
with zero discretization defect and gives its strict margins. If f,g
are uniformly bounded in absolute value by B, then
\[
 |\mathcal L_\mu(f)-\mathcal L_\mu(g)|
                  \le2(B+Y)\|f-g\|_\infty.
\]
The fixed-state loss integrand is Lipschitz in the joint normalized
input/label metric, with constant
\(2(B+Y)\max\{\operatorname{Lip}f,1\}\). Thus (C.4.7.NW1)–(C.4.7.NW2) pass
the finite risks to the population risk, including the empirical-law
limit. For a hidden field bounded by one, keeping the same initialized
field in each comparison gives
\[
 \left|\|H-H_0\|_2^2-\|\bar H-H_0\|_2^2\right|
                           \le4\|H-\bar H\|_2.
\]
The paired observation contract retains \(H,H_0\) jointly on their
own carrier; its fixed-program limit identifies the displayed norms.
Uniform input continuity passes their training-law integrals. This
therefore passes the strict finite hidden-activity margins as well.

The new nonlinear theorem concerns the one physical GF interval
\([0,40]\). It gives no all-time changed-law dynamics, endpoint selection
or continuity, universal fitting, activity for every bounded-label law,
activity at time40, or comparison with frozen-feature learning. It does
not extend the earlier raw-GD theorem to this interval. The neighborhood
radius is positive but has no claimed useful numerical size. The
population remainder is uniform over contamination laws; the finite
nonlinear statement takes width first for each fixed contamination law
and fixed positive epsilon, and asserts no simultaneous epsilon/width
rate or uniform finite failure probability over all laws.
