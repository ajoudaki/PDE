# Positive cubature for nonlinear neural gradient flow

This is a scoped, internally derived theory result. Its scientific inputs are the supervisor's prompt alone. It has not been promoted to the maintained book or independently reviewed. No training experiment was run.

The result compresses the data in the exact nonlinear gradient field, retaining the original finite network and its canonical mobility. For fixed architecture, initialization, horizon, label RMS bound, and analytic input chart, a positive dataset of size `O(p^s)` produces `O(r^{-p})` error throughout the entire time interval, independently of the original sample count. The same statement includes probability distributions with unbounded labels of finite second moment. The construction does not inspect the training trajectory.

## 1. Precise contract and theorem

Let `K=[-1,1]^s`, with integer `s>=1`, and let `chi:K -> R^d` extend holomorphically to an open complex neighborhood of `K`, with real values on `K`. In particular, a real-analytic chart on a real open neighborhood of the closed cube has this property after restricting its complex extension. Analyticity only in the interior of the cube is a weaker assumption and is not enough for the exponential estimate below.

Let `f_theta(x)` be a fixed finite scalar-output feedforward network made from affine maps and `tanh`, with parameter vector `theta in R^P`; fixed normalization factors and biases are permitted. Write

\[
h_\theta(u)=f_\theta(\chi(u)).
\]

Let `D` be a fixed positive diagonal mobility. This includes the canonical block mobility `diag(n I,I,...,I,n I)`. For integer width `n>=1`, its largest eigenvalue is `n`. The loss and clock used throughout this note are

\[
\mathcal L_\mu(\theta)
 =\int (h_\theta(u)-y)^2\,d\mu(u,y),
\qquad
\dot\theta=-D\nabla_\theta\mathcal L_\mu
 =-2D\int(h_\theta-y)\nabla_\theta h_\theta\,d\mu.
\tag{1}
\]

Thus there is no factor `1/2` in the loss. A different convention changes the clock and the constants.

Fix `theta_0`, `T>0`, and `Y>=0`. Let `pi` be any probability measure on `K x R` satisfying `int y^2 d pi <= Y^2`. It may be an empirical measure with any finite sample count `m`, with arbitrary positive normalized original weights, or a continuum distribution. No regularity of labels or conditional label means is assumed.

For `p>=0`, define

\[
I_p=\{\alpha\in\mathbb N_0^s:|\alpha|_1\le p\},
\qquad N_p=|I_p|=\binom{p+s}{s}.
\]

There is a probability measure

\[
\pi_p=\sum_{j=1}^{k_p}w_j\delta_{(u_j,y_j)},
\qquad w_j>0,\qquad
k_p\le 2N_p+1,
\tag{2}
\]

with nodes in any prescribed full-`pi`-measure subset of `K x R`, for which

\[
\begin{aligned}
\int u^\alpha\,d\pi_p&=\int u^\alpha\,d\pi,
&&\alpha\in I_p,\\
\int y u^\alpha\,d\pi_p&=\int y u^\alpha\,d\pi,
&&\alpha\in I_p,\\
\int y^2\,d\pi_p&=\int y^2\,d\pi.
\end{aligned}
\tag{3}
\]

For finite data the nodes can be selected from the original observations, and `k_p<=min(m,2N_p+1)`. The degree is total degree `p`, not separate degree `p` in each coordinate.

Let `theta(t)` and `theta_p(t)` solve (1) for `pi` and `pi_p`, both initialized at `theta_0`. There are constants `C<infinity`, `r>1`, `L>=0`, and `A<infinity`, depending only on the fixed network and its normalization, `D`, `theta_0`, `T`, `chi`, `s`, and `Y`, such that

\[
\begin{aligned}
\sup_{0\le t\le T}
\|D^{-1/2}(\theta(t)-\theta_p(t))\|
 &\le C r^{-p}\Psi_L(T),\\
\sup_{0\le t\le T}\|\theta(t)-\theta_p(t)\|
 &\le \sqrt{\|D\|}\,C r^{-p}\Psi_L(T),\\
\sup_{\substack{0\le t\le T\\u\in K}}
|h_{\theta(t)}(u)-h_{\theta_p(t)}(u)|
 &\le A C r^{-p}\Psi_L(T),
\end{aligned}
\tag{4}
\]

where

\[
\Psi_L(t)=
\begin{cases}(e^{Lt}-1)/L,&L>0,\\t,&L=0.\end{cases}
\]

All constants are independent of `pi` except through its imposed bound `Y`, and therefore independent of `m`. Neither width-uniform nor horizon-uniform constants are asserted. In particular, the available complex neighborhood can shrink as width, initial parameters, or horizon increase.

The proof has three components: an energy ball containing both trajectories, positive moment cubature, and uniform polynomial approximation of the nonlinear drift on that entire ball.

## 2. Global existence and the common energy ball

Use the fixed coordinate change

\[
v=D^{-1/2}\theta,\qquad v_0=D^{-1/2}\theta_0,
\qquad h_v(u)=h_{D^{1/2}v}(u),
\qquad q_v(u)=\nabla_v h_v(u).
\]

The flow becomes ordinary Euclidean gradient flow:

\[
\dot v=-\nabla_v\mathcal L_\mu(v)
       =-2\int(h_v-y)q_v\,d\mu=:b_\mu(v).
\tag{5}
\]

On every compact parameter set, the network and all its first and second parameter derivatives are uniformly bounded for `u in K`. Since `int |y| d mu <= Y`, differentiation under the integral in (5) is justified by these bounds and dominated convergence. The vector field is locally Lipschitz, giving a unique maximal solution.

Along any interval on which that solution exists,

\[
\frac{d}{dt}\mathcal L_\mu(v(t))
=-\|\nabla_v\mathcal L_\mu(v(t))\|^2
=-\|\dot v(t)\|^2.
\tag{6}
\]

Put `F_0=sup_{u in K}|h_{v_0}(u)|`. The `L^2(mu)` triangle inequality gives

\[
\sqrt{\mathcal L_\mu(v_0)}
\le \|h_{v_0}\|_{L^2(\mu)}+\|y\|_{L^2(\mu)}
\le F_0+Y.
\]

Integrating (6), then applying Cauchy--Schwarz in time, yields

\[
\begin{aligned}
\int_0^t\|\dot v(a)\|^2da
 &\le\mathcal L_\mu(v_0),\\
\|v(t)-v_0\|
 &\le\int_0^t\|\dot v(a)\|da
 \le\sqrt t\,(F_0+Y).
\end{aligned}
\tag{7}
\]

On a hypothetical finite maximal interval, (7) bounds the solution in a compact parameter set. The vector field is bounded there, so the solution is Lipschitz in time and has a limit at the terminal time; local existence at that limit extends it. This rules out finite-time escape and proves global existence.

Because (3) makes `pi_p` a probability measure with exactly the same second label moment, (7) applies to both flows with the same closed convex ball

\[
B_T=\{v:\|v-v_0\|\le R_T\},\qquad
R_T=\sqrt T(F_0+Y).
\tag{8}
\]

In the original parameters, both trajectories lie in the Euclidean ball of radius `sqrt(||D|| T)(F_0+Y)` centered at `theta_0`; for the canonical mobility this is `sqrt(n T)(F_0+Y)`. This ball is obtained before either trajectory is known. There is no small-motion assumption.

For later use, define real-domain constants on `B_T x K`:

\[
F=\sup|h_v(u)|,\qquad
A=\sup\|q_v(u)\|,\qquad
H=\sup\|\nabla_v^2h_v(u)\|_{\mathrm{op}}.
\tag{9}
\]

For any probability measure `mu` with label RMS at most `Y`,

\[
\nabla_v b_\mu(v)
=-2\int\left[q_vq_v^\top+(h_v-y)\nabla_v^2h_v\right]d\mu.
\]

Thus, on the convex ball,

\[
\|b_\mu(v)-b_\mu(\widetilde v)\|
\le L\|v-\widetilde v\|,
\qquad L=2\big[A^2+(F+Y)H\big].
\tag{10}
\]

This uses only the first absolute label moment, bounded by its RMS, and is uniform over the entire admissible distribution class.

## 3. Exact positive cubature, including unbounded continuum labels

Consider the `r_p=2N_p+1` component feature vector

\[
\Phi_p(u,y)
=\big((u^\alpha)_{\alpha\in I_p},
       (yu^\alpha)_{\alpha\in I_p},y^2\big).
\tag{11}
\]

Its constant coordinate is `1`. Every component is integrable: on `K`, `|u^alpha|<=1`, while `int |y|<=Y` and `int y^2<=Y^2`.

### Finite data: constructive elimination

Suppose the current positive weighted list has more than `r_p` observations. Its feature columns are linearly dependent, so there are coefficients `c_i`, not all zero, such that

\[
\sum_i c_i\Phi_p(u_i,y_i)=0.
\]

The constant coordinate gives `sum_i c_i=0`, hence there are both positive and negative coefficients. For current weights `a_i>0`, let

\[
\tau=\min_{c_i>0}\frac{a_i}{c_i},
\qquad a_i'=a_i-\tau c_i.
\]

All new weights are nonnegative, at least one becomes zero, and every feature moment is unchanged. Delete zero weights and repeat until at most `r_p` observations remain. This proves (2)--(3), with strict positivity of every retained weight.

The same procedure can run sequentially: maintain at most `r_p` weighted columns, append the next original weighted observation, and eliminate a column whenever the list reaches `r_p+1`. It requires no network evaluation, gradient calculation, or trajectory. Its input-processing work depends on `m`; the retained data size does not. For rational stored inputs it is a terminating exact-rational linear-algebra construction. Exact-real arithmetic is a mathematical model, not a universal computability guarantee for arbitrary real oracles.

### Continuum: an integrable barycenter lies in the finite convex hull

The following argument supplies the existence step without assuming bounded labels or a compact feature image.

**Finite-dimensional barycenter lemma.** Let `Z` be an integrable random vector in `R^d`, and let `S` be its image on any prescribed probability-one subset of the underlying sample space. Then `E Z` is a finite convex combination of points of `S`.

**Proof.** Write `b=E Z` and `C=closure(conv S)`, considered inside its affine hull. First `b in C`. Otherwise choose a nearest point `c in C` to `b`; it exists because the distance minimization can be restricted to a compact Euclidean ball. Convexity and differentiation of the squared distance along `c+t(z-c)` imply

\[
(b-c)\cdot(z-c)\le0\qquad(z\in C).
\]

Taking expectations with `z=Z` would give `||b-c||^2<=0`, a contradiction.

If `b` is on the relative boundary of `C`, there is a supporting hyperplane through `b`. Here is the needed construction. Take points `b_j` in the affine hull but outside `C`, converging to `b`, and nearest points `c_j in C`. The preceding projection inequality applies to unit vectors

\[
a_j=(b_j-c_j)/\|b_j-c_j\|.
\]

We have `c_j -> b`; a subsequence of these unit vectors converges to a unit vector `a` in the direction space of the affine hull. Passing to the limit gives `a dot(z-b)<=0` for all `z in C`. The integrable nonpositive random variable `a dot(Z-b)` has expectation zero, and therefore vanishes almost surely. Restrict the original full-measure set to this hyperplane. Its affine dimension has fallen by at least one. Repeat this reduction finitely many times.

It remains to treat the case where `b` is in the relative interior of `closure(conv S)`; this includes the final reduced problem. If the affine dimension is zero there is nothing to prove. Otherwise put a small nondegenerate simplex centered at `b` inside that relative interior. Approximate each simplex vertex by a point of `conv S`, which is dense in its closure. When the approximations are sufficiently close, the simplex remains nondegenerate and still has `b` in its interior: its barycentric coordinates depend continuously on the vertices and started strictly positive. Thus `b` is a convex combination of finitely many points of `conv S`, and hence of finitely many points of `S`. This proves the lemma.

Apply the lemma to `Z=Phi_p(u,y)`. The resulting finite convex combination can be reduced by the same linear-dependence elimination as above to at most `r_p` points, because the feature vector contains the constant coordinate `1`. This proves the continuum statement.

The nodes can be required to lie in the topological support of `pi`, since that support has probability one in the Euclidean space `K x R`; one may also intersect with any other prescribed full-measure set. Thus if the labels obey a measurable deterministic relation almost surely, the selected nodes obey it too. No label bound follows: individual selected labels can be large, but their weighted second moment is exactly controlled.

This existence proof is not an algorithm for an unspecified continuum probability measure. Computing a continuum cubature requires an effective representation of the distribution, access to the needed moments, and a means of finding appropriate nodes. An arbitrary probability measure with finite second moment does not supply those computational interfaces.

## 4. Uniform analytic polynomial approximation on the energy ball

The fixed network, the compact real parameter ball `B_T`, and the analytic chart supply a common complex input neighborhood on which both

\[
u\longmapsto q_v(u),\qquad
u\longmapsto h_v(u)q_v(u)
\tag{12}
\]

are holomorphic, uniformly for real `v in B_T`. To check this, every real preactivation in every finite layer ranges over a compact subset of the real line. The poles of `tanh` are off that line. Continuity, compactness of `B_T x K`, and induction through the finitely many layers give a complex neighborhood of `K` in which all these preactivations avoid all poles. Parameter derivatives are finite compositions and products of the same pole-free analytic functions, so they share a possibly smaller neighborhood. This reasoning also gives continuity of the extensions in real `v`.

For `rho>1`, let `E_rho` be the closed solid Bernstein ellipse with boundary `(z+z^{-1})/2` for `|z|=rho`. As `rho` decreases to `1`, its distance from `[-1,1]` tends to zero. Choose `rho>1` such that the product `E_rho^s` is contained in the common neighborhood and define finite bounds

\[
Q_\rho=\sup_{v\in B_T,\ u\in E_\rho^s}\|q_v(u)\|,
\qquad
R_\rho=\sup_{v\in B_T,\ u\in E_\rho^s}
                  \|h_v(u)q_v(u)\|.
\tag{13}
\]

The norms here are complex Euclidean norms. These are structural bounds on an a priori parameter ball; neither is evaluated along an oracle trajectory.

For completeness, suppose `g:E_rho^s -> C^P` is holomorphic on a neighborhood of this set and bounded in norm by `M`. Under the substitution `u_j=(z_j+z_j^{-1})/2`, its Laurent coefficients satisfy

\[
\|a_k\|\le M\rho^{-|k|_1}\qquad(k\in\mathbb Z^s),
\]

by the multivariate Cauchy integral, choosing radius `rho` or `rho^{-1}` according to the sign of each index. Invariance under `z_j -> z_j^{-1}` groups these coefficients into a tensor Chebyshev series

\[
g(u)=\sum_{\alpha\in\mathbb N_0^s}
      c_\alpha\prod_{j=1}^s T_{\alpha_j}(u_j),
\qquad
\|c_\alpha\|\le 2^s M\rho^{-|\alpha|_1}.
\]

The series converges absolutely on `K`. Truncate it at total degree `p`. Since `|T_k(u)|<=1` on `[-1,1]`, for any fixed `1<r<rho` its error satisfies

\[
\begin{aligned}
\|g-P_p g\|_{L^\infty(K)}
&\le 2^sM\sum_{|\alpha|_1>p}\rho^{-|\alpha|_1}\\
&\le 2^sM r^{-p}\sum_{\alpha\in\mathbb N_0^s}
                      (r/\rho)^{|\alpha|_1}\\
&= C_s M r^{-p},
\qquad C_s=2^s(1-r/\rho)^{-s}.
\end{aligned}
\tag{14}
\]

These polynomials have real coefficients when `g` is real on `K`. Apply (14), uniformly over `v in B_T`, directly to the two vector functions (12), producing total-degree-`p` polynomials `Q_{v,p}` and `R_{v,p}` with

\[
\sup_{v,u}\|q_v(u)-Q_{v,p}(u)\|
 \le C_sQ_\rho r^{-p}=:\varepsilon_{Q,p},
\qquad
\sup_{v,u}\|h_v(u)q_v(u)-R_{v,p}(u)\|
 \le C_sR_\rho r^{-p}=: \varepsilon_{R,p}.
\tag{15}
\]

Directly approximating the product `h_v q_v` is relevant to the count: it needs moments only through degree `p`. Multiplying separate degree-`p` approximations of its two factors would instead require degree `2p` moments. The cubature construction never needs to compute the polynomials in (15); they are witnesses in the error proof.

## 5. Drift error and whole-interval trajectory error

Moment matching gives, for every `v in B_T`,

\[
\int R_{v,p}(u)\,d(\pi-\pi_p)=0,
\qquad
\int yQ_{v,p}(u)\,d(\pi-\pi_p)=0.
\]

Both measures have mass one and first absolute label moment at most `Y`. Therefore

\[
\begin{aligned}
\|b_\pi(v)-b_{\pi_p}(v)\|
&\le 2\left\|\int(h_vq_v-R_{v,p})\,d(\pi-\pi_p)\right\|\\
&\quad+2\left\|\int y(q_v-Q_{v,p})\,d(\pi-\pi_p)\right\|\\
&\le4\varepsilon_{R,p}+4Y\varepsilon_{Q,p}\\
&= C r^{-p}=:\delta_p,
\qquad C=4C_s(R_\rho+YQ_\rho).
\end{aligned}
\tag{16}
\]

No maximum label or sample-count factor appears.

Both trajectories remain in `B_T`. Write `e(t)=||v(t)-v_p(t)||`. The integral form of (5), together with (10) and (16), gives

\[
e(t)\le\int_0^t \big[L e(a)+\delta_p\big]da.
\]

Multiplication by the scalar integrating factor, or iteration of this integral inequality, gives

\[
e(t)\le\delta_p\Psi_L(t)\le C r^{-p}\Psi_L(T).
\tag{17}
\]

The parameter transformation gives the second line of (4). For predictions, the line segment between `v(t)` and `v_p(t)` lies in `B_T`, so the fundamental theorem of calculus and (9) give

\[
|h_{v(t)}(u)-h_{v_p(t)}(u)|
\le A\|v(t)-v_p(t)\|
\]

uniformly on all of `K`, proving the last line of (4). One may similarly evaluate on a different prescribed compact input set by replacing `A` in this last step with the corresponding parameter-gradient bound there; compression itself still concerns the original training distribution.

For simultaneous error at most `epsilon>0` in all three quantities in (4), put `W=max(1,sqrt(||D||),A)`. When `C Psi_L(T)>0`, it suffices to take

\[
p\ge\max\left\{0,
\left\lceil\frac{\log\big(W C\Psi_L(T)/\varepsilon\big)}{\log r}
\right\rceil\right\}.
\tag{18}
\]

If the numerator constant vanishes the error bound is already zero. For fixed structural quantities, (2) and (18) give

\[
k_p\le2\binom{p+s}{s}+1
=O\big((1+\log(1/\varepsilon))^s\big)
\quad\text{as }\varepsilon\downarrow0.
\tag{19}
\]

This is a deterministic sample-count-independent support bound. The retained network still has `P` parameters. The proof does not compress width or parameter count.

## 6. Computation, scope, and adversarial checks

- **Coefficient provenance and autonomy.** For finite data the compressed rows and weights are obtained solely from input coordinates, labels, and a degree choice. The moment selection itself is independent of the network and of training time. Its resulting weighted neural flow is autonomous and restartable from its current parameters. It retains all nonlinear feature learning and the original mobility. No teacher trajectory, frozen-feature replacement, or linearized network enters the construction.

- **Exact continuum existence versus effective computation.** The finite-dimensional barycenter proof covers unbounded labels because every feature coordinate is integrable; compactness of the feature image was never used. It does not turn an abstract distribution into computable moments or nodes. A computational theorem for continuum data needs such access as a separate assumption. Similarly, deriving a numerical degree from (18) requires effective certified analytic and derivative bounds; mere abstract analyticity establishes their existence.

- **Output size versus processing time and precision.** The number of retained rows is independent of `m`; reading the original finite dataset is not. No bound independent of `m` is claimed for exact rational bit lengths, conditioning, or a particular numerical solver's cost. Very small weights and very large labels can occur. If desired, the drift can be stored using bounded coefficients `a_j=w_j` and `b_j=w_j y_j`, with `0<a_j<=1`, `|b_j|<=Y`, and `sum_j |b_j|<=Y`; its loss is `sum_j a_j h(u_j)^2-2 sum_j b_j h(u_j)+c`, where `c=int y^2 d pi<=Y^2`. This avoids evaluating a large label before multiplying by its weight, but is not a bit-complexity theorem. The prescribed elimination procedure also prevents treating an unrestricted real coefficient as an unexplained encoding of the original dataset.

- **The second-moment constraint is a certificate, not an additional force.** The `y^2` term is constant in the parameters and does not change the exact gradient. Its matching supplies the common RMS and energy bounds used here. It could be replaced by another proved sufficient second-moment bound, but dropping it without such a bound leaves this particular uniform proof incomplete.

- **Label-weighted moments cannot be dropped.** Take the scalar model `f_theta=tanh(theta)`, initial parameter `theta_0=0`, and two distributions with identical input marginal but constant labels `+1` and `-1`. They have identical unlabeled moments of every degree and identical second label moments. Their initial velocities are `+2D` and `-2D`. Thus unlabeled geometry and label RMS alone do not determine the nonlinear flow.

- **Analyticity at the boundary matters.** A bounded function analytic only on the cube interior can fail even to be continuous at its boundary, as `sin(1/(1-u))` on `u<1` with an arbitrary value assigned at `u=1` shows. Uniform polynomial approximation then fails. Even a continuous smooth extension can lose geometric rates: `chi(u)=exp(-1/(1-u^2))` for `|u|<1`, extended by zero at the endpoints, is flat but nonanalytic there. For the scalar parameterized model `f_a(x)=a tanh(x)`, the derivative in `a` is `tanh(chi(u))`, also flat and nonanalytic at the endpoints. A uniform geometric polynomial approximation rate would imply geometric decay of its Chebyshev coefficients (bound a coefficient by twice the error of any lower-degree approximant); its Chebyshev series would then extend holomorphically to a smaller ellipse, contradicting that nonanalyticity. The theorem consequently states the necessary neighborhood hypothesis explicitly.

- **Positive weights and normalization are part of the surrogate.** A signed moment rule does not automatically preserve the loss's nonnegativity or the bounds by label RMS. The compressed loss is the positive weighted sum with `sum_j w_j=1`, not an unweighted average over the retained rows. Replacing weights with a uniform average changes the vector field.

- **Fixed horizon, fixed architecture.** The Gronwall factor may grow rapidly with `T`; the analytic radius may approach one when the parameter ball becomes large. Nothing here permits an all-time error estimate, exchanging a width limit with the approximation limit, or a complexity bound uniform in depth, width, or input dimension. The exponent `s` reflects the chosen input chart and can itself be costly.

- **No temporal discretization assertion.** Equations (4) and (17) compare exact continuous-time flows. A numerical or temporal moment approximation adds its own residual and stability argument. Its error must be combined explicitly with (16), rather than silently absorbed into the cubature theorem.

- **Degenerate cases.** At `T=0` the compared parameters and predictions agree exactly. If `Y=0`, positivity and the matched second moment force every retained label to be zero. The formula for `Psi_L` covers `L=0`. Data repetitions and lower-dimensional feature images only reduce the support needed by the elimination argument.

The proved claim is the existence, and for finite exact data the algebraic construction, of a positive data cubature giving uniform finite-horizon approximation to the original nonlinear neural gradient flow. Computational guarantees for unspecified continuum measures, numerical conditioning guarantees, width compression, and all-time approximation remain outside this claim.
