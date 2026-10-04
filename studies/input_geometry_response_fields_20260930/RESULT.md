# Compressing the input dependence of response memory

## Result and scope

There is a route beyond storing a separate history for every training example: represent the input dependence of the responses, and retain only the action of the data distribution on that function class. The controlling structure is input regularity on a fixed-dimensional domain. Low matrix rank is not a hypothesis.

The concrete construction below combines positive data moment matching with the learning-speed response-memory closure. For a fixed finite tanh network, a fixed finite horizon, and inputs on a fixed analytic parametrized domain of dimension s, it gives

\[
 \sup_{0\le t\le T}\sup_{u\in[-1,1]^s}
 |\widehat f_{q,p}(t,\chi(u))-f_\pi(t,\chi(u))|
 \le C_{T,n}\left(q^{-1}+e^{-c_{T,n}p}\right).                 \tag{1}
\]

Here q≥1 and p≥0 are integers. The law pi can be any empirical probability distribution or a continuum distribution, with label second moment at most Y². The algorithm uses at most

\[
 K\le 2(p+1)^s+1                                             \tag{2}
\]

positive weighted input-label pairs and 2(L−1)nqK evolving internal-memory coordinates. All constants are independent of the number of original data points, their separation, their minimum probabilities, and the regularity of their labels. They can depend on n, L, T, Y, the input parametrization, and the realized initialization. Equation (1) controls the entire interval and all inputs in the domain, not just training points or an endpoint.

This is a compact-time, fixed-width theorem. It is not a width-uniform population theorem, an all-time fitting theorem, or a claim of small practical constants. The initialized dense matrices are retained exactly. No small-label or successful-training hypothesis is used. The construction does not need a future trajectory or a dense reference run.

The proof is included below. The input-moment construction is classical cubature; the present deduction is its explicit combination with autonomous response memory and its sample-count-independent trajectory bound. Priority for this combination has not been established.

## 1. Model and the data's exact role

There are L hidden layers of width n. The architecture and scaling are

\[
 h^{(1)}=\tanh(W^{(1)}x/\sqrt d),\qquad
 h^{(\ell)}=\tanh(W^{(\ell)}h^{(\ell-1)}),\qquad
 f_\theta(x)=w^Th^{(L)}(x)/n.
\]

Every weight is trained. With pi a probability law of (u,y), x=chi(u), and
\(\mathcal L_\pi(\theta)=\mathbb E_\pi(f_\theta(x)-y)^2\), canonical GF is

\[
 \dot\theta=F_\pi(\theta)
 =-2D\mathbb E_\pi[(f_\theta(x)-y)\nabla_\theta f_\theta(x)],   \tag{3}
\]

where D has block mobilities n,1,...,1,n for first weights, internal matrices, and readout. All parameter norms below are ordinary Euclidean/Frobenius block norms. In particular ||D||=n.

Write mu for the input marginal, nu for the finite signed label measure
\(\nu(A)=\mathbb E[y\,1_{u\in A}]\), and \(v=\mathbb E y^2\). Then exactly

\[
 F_\pi(\theta)=-2D\left[\int f_\theta\nabla f_\theta\,d\mu
                      -\int\nabla f_\theta\,d\nu\right],      \tag{4}
\]
\[
 \mathcal L_\pi(\theta)=\int f_\theta^2\,d\mu-2\int f_\theta\,d\nu+v.
                                                                  \tag{5}
\]

All functions in these integrals are evaluated at chi(u). The total variation of nu is at most E|y|≤Y. These formulas do not assume a density, noiseless targets, or a smooth regression function. The gradient does not use higher conditional moments of y; the residual-RMS clock additionally uses v.

This is a useful distinction: the network need not reconstruct an irregular label function pointwise to approximate its training dynamics. It must approximate the label measure's action on the smooth functions the network can currently generate.

## 2. Exact response fields, including irregular labels

Let delta denote backpropagation without the residual:

\[
 \delta^{(L)}=w\odot\phi'(z^{(L)}),\qquad
 \delta^{(\ell)}=\phi'(z^{(\ell)})\odot(W^{(\ell+1)})^T\delta^{(\ell+1)}.
\]

For any order q and the old clock tau'=rho=\(\sqrt{\mathcal L}\), tau(0)=1, a forward memory H_k is driven by rho h, and a backward memory B_k by (f−y)delta. Both have the same triangular damping

\[
 (\mathcal T U)_k=kU_k+\sum_{j<k}(2j+1)U_j.
\]

Because the damping coefficients are shared scalars, there is the exact identity

\[
 B_k(t,u,y)=A_k(t,u)-yC_k(t,u),                              \tag{6}
\]

with zero initial A,C and

\[
 \dot H_k=\rho h-(\rho/\tau)(\mathcal T H)_k,\quad
 \dot A_k=f\delta-(\rho/\tau)(\mathcal T A)_k,\quad
 \dot C_k=\delta-(\rho/\tau)(\mathcal T C)_k.                 \tag{7}
\]

Indeed substituting (6) into (7) gives the original B equation and initial condition; uniqueness proves the identity. H_0(0,u)=h(0,u) and higher H initially vanish. A learned internal matrix is consequently

\[
 \widehat W^{(\ell)}=W_0^{(\ell)}-
 \frac2{n\tau}\sum_{k<q}(2k+1)
 \left[\int A^{(\ell)}_k(H^{(\ell-1)}_k)^T d\mu
       -\int C^{(\ell)}_k(H^{(\ell-1)}_k)^T d\nu\right].      \tag{8}
\]

The appropriate objects are therefore input-dependent fields H,A,C, not unrelated vectors for every example. Replacing them by finite input coordinates is a second approximation axis, independent of the temporal order q. Fixed input coordinates do not freeze the neural features: every coefficient and every network response continues to evolve.

## 3. A finite data representation with positive weights

Let V_p be the tensor-polynomial space of degree at most p in each of s input coordinates; J=(p+1)^s. Choose a real basis psi_1,...,psi_J including 1. There is a probability distribution

\[
 \pi_p=\sum_{j=1}^{K}a_j\delta_{(u_j,y_j)},\quad a_j>0,
 \quad\sum_j a_j=1,\quad K\le2J+1,                         \tag{9}
\]

matching all 2J+1 data statistics

\[
 \int\psi_i\,d\pi_p=\int\psi_i\,d\pi,\qquad
 \int y\psi_i\,d\pi_p=\int y\psi_i\,d\pi,\qquad
 \int y^2d\pi_p=\int y^2d\pi.                              \tag{10}
\]

The points can be taken from the original dataset when pi is empirical. For a continuum law they may be taken from a full-measure subset of its support. Only E y²<∞ is needed: the input polynomials are bounded, so all coordinates of the feature map (psi,y psi,y²) are integrable.

Here is a proof including the noncompact-label case. Let Z be this integrable finite-dimensional feature map. Its expectation lies in the closed convex hull of any full-measure range: a separating linear functional would contradict its expected value. If the expectation is on the relative boundary, take a supporting hyperplane. Its nonnegative slack has zero expectation and therefore vanishes almost surely. Restrict the range to that hyperplane. Repeating reduces dimension until the expectation is in the relative interior of the closed convex hull. That relative interior is contained in the convex hull itself: an interior point is enclosed by a finite simplex of sufficiently nearby points from the convex hull, obtained by perturbing a small surrounding simplex within the closure. Thus EZ is a finite convex combination of actual range points. Since the constant coordinate of Z is 1, its affine dimension is at most 2J. Any combination with more than 2J+1 points has an affine dependence. Moving its positive coefficients along that dependence until one vanishes reduces the number without changing the expectation. Repetition proves (9)–(10).

For a finite dataset this is also an elementary exact-arithmetic algorithm. Start with the empirical weights, find a null vector c for the retained feature columns (including the constant row), and replace a by a−t c with t=min_{c_j>0}a_j/c_j. All weights remain nonnegative, at least one disappears, and all moments remain exact. This can be done in a stream retaining at most 2J+2 columns before elimination. It reads the whole dataset once; it does not obtain its information for free.

The continuum existence statement is the finite-integrable-function form of the cubature theorem. Bayer and Teichmann give a complete proof as Corollary 2 of [The proof of Tchakaloff's theorem](https://people.math.ethz.ch/~jteichma/tchakaloff120405.pdf). An effective continuum implementation additionally needs certified moments and a supplied or computable positive cubature; integrability alone does not give an algorithm for finding its nodes. An unknown distribution cannot be exactly summarized without a sampling error term.

## 4. Why this summary preserves the whole nonlinear flow

Assume chi extends holomorphically to a neighborhood of the closed cube, is real on the cube, and has bounded real image. Fix theta_0,n,L,T,Y. Let

\[
 F_0=\sup_u|f_{\theta_0}(\chi(u))|,\qquad
 R=\|\theta_0\|+\sqrt{nT}(F_0+Y)+1.
\]

Both original and cubature dense flows stay in the ball ||theta||≤R−1. In fact (3) implies

\[
 \dot{\mathcal L}=-\|D^{-1/2}\dot\theta\|^2,\qquad
 \int_0^T\|\dot\theta\|^2dt\le n\mathcal L(0),\qquad
 \|\theta(t)-\theta_0\|\le\sqrt{nT}\sqrt{\mathcal L(0)}.
\]

For either law, \(\sqrt{\mathcal L(0)}\le F_0+Y\), because (10) preserves label second moment. A finite maximal time would have a limiting finite state by this same energy estimate and Cauchy–Schwarz on the remaining interval; local existence would extend it. The dense flows therefore exist globally. No convexity or interpolation condition was used.

On the fixed ball and real cube, f, its parameter gradient, and its Hessian are bounded. The analytic input parametrization and tanh composition extend uniformly to a common complex neighborhood. To verify uniformity, every real preactivation is in a compact real interval. Tanh has no pole there. Uniform continuity and a finite number of layer compositions give a sufficiently small complex neighborhood, uniformly for all theta in the compact ball, on which every preactivation avoids the poles. The differentiated expressions are holomorphic there too. Shrinking once more supplies a closed product Bernstein ellipse E_b^s with b>1 and finite uniform bounds.

For completeness, a bounded holomorphic vector-valued G on E_b^s has tensor Chebyshev coefficients bounded by 2^s M b^{-|alpha|_1}. This follows by substituting u_j=(z_j+z_j^{-1})/2 and moving each Laurent-coefficient contour to |z_j|=b; the contour length cancels the z_j^{-1} factor. The Euclidean vector norm satisfies the same integral estimate. Summing coefficients with at least one alpha_j>p gives

\[
 \|G-Q_pG\|_\infty
 \le2^s M s\,\frac{b^{-(p+1)}}{(1-b^{-1})^s}.               \tag{11}
\]

This is the tensor version of the classical Chebyshev analytic bound; [Trefethen's Chapter 8](https://raw.githubusercontent.com/chebfun/ATAP/master/chap8.m) gives its one-dimensional contour proof. Apply (11) separately to G=grad f and G=f grad f. There are polynomials in V_p with uniform errors at most A b^{-p}, simultaneously for every theta in the ball. This is input approximation, not a Taylor expansion in training time or in the parameter displacement.

Matched moments now cancel the polynomial parts of (4) exactly. Positivity and the preserved label second moment imply

\[
 \sup_{\|\theta\|\le R}\|F_\pi(\theta)-F_{\pi_p}(\theta)\|
 \le4n(1+Y)A b^{-p}.                                      \tag{12}
\]

For example, the unlabeled remainder is integrated against two probability laws and is at most 2A b^{-p}; the labeled remainder is at most 2Y A b^{-p}. Multiplication by 2D gives (12).

Let M_0,M_1,M_2 bound |f|, ||grad f|| and ||Hess f|| on the real ball and cube. Both vector fields have Lipschitz constant at most

\[
 \Lambda=2n[M_1^2+(M_0+Y)M_2].                             \tag{13}
\]

This follows by differentiating (3), bounding the grad f outer product, and using E|f−y|≤M_0+Y. Importantly, neither (12) nor (13) contains K, m, or a minimum atom weight.

Subtract the two flow integral equations. Starting at the same initialization, their distance e(t) satisfies

\[
 e(t)\le\int_0^t\Lambda e(s)ds+4n(1+Y)A\,t b^{-p}.
\]

Multiplying the associated scalar differential majorant by e^{-Lambda t}, or iterating this integral inequality, gives

\[
 \sup_{t\le T}e(t)
 \le4n(1+Y)A\,T e^{\Lambda T}b^{-p}.                       \tag{14}
\]

The predictor is Lipschitz in theta, uniformly over the entire input cube, so its error is at most M_1 times (14). The same argument works on any other fixed compact test-input set, changing only that final Lipschitz constant. This is the precise feedback argument: the data summary controls the vector field everywhere in an a priori region, so it remains valid when its own training trajectory departs slightly from the reference trajectory.

## 5. Autonomous temporal compression of the weighted problem

Run the usual learning-speed response-memory closure on (9), replacing all sample averages by sums weighted by a_j. For each internal layer and node store q forward and q backward vectors. Set

\[
 \rho^2=\sum_ja_jr_j^2,\quad\dot\tau=\rho,\quad\tau(0)=1,
\]
\[
 \dot H_{k,j}=\rho h_j-(\rho/\tau)(\mathcal T H)_{k,j},\quad
 \dot B_{k,j}=r_j\delta_j-(\rho/\tau)(\mathcal T B)_{k,j},    \tag{15}
\]
\[
 \widehat W^{(\ell)}=W_0^{(\ell)}-
 \frac2{n\tau}\sum_j a_j\sum_{k<q}(2k+1)
 B^{(\ell)}_{k,j}(H^{(\ell-1)}_{k,j})^T.                    \tag{16}
\]

The first matrix and readout obey their canonical weighted GF equations evaluated at the reconstructed current network. Initial H_0 is the initial activation; all other moments are zero. These are a finite autonomous ODE, including at zero residual: the displayed right sides require no division by rho. Both W0 and its transpose are evaluated exactly.

We prove, rather than assume, a bound uniform over all positive finite probability weights with label RMS≤Y:

\[
 \sup_{t\le T}\|\widehat\theta_q(t)-\theta_{\pi_p}(t)\|
 \le C_{T,n}/\sqrt{q(q+1)}.                                \tag{17}
\]

### 5.1 Uniform physical bounds for tanh, for every q

The readout equation gives the exact identity

\[
 \frac{d}{dt}\|w\|^2
 =n\mathbb E y^2-4n\mathbb E(f-y/2)^2\le nY^2.
\]

Thus set B_w=\(\sqrt{\|w_0\|^2+nY^2T}\), varrho=B_w/sqrt(n)+Y, S=T varrho and A_0=1+S. Then ||w||≤B_w, rho≤varrho, tau≤A_0. These apply to both flows. Activations have norm at most alpha=sqrt(n).

For clock-coordinate histories on [0,tau], extend h constantly over [0,1] and b=r delta/rho by zero there. The moment reconstruction is precisely the integral pairing of their first q orthogonal projections. At rho=0 take b=0 for these proof formulas. Projection contraction and
\(\mathbb E_j\|b_j\|^2\le\beta_\ell^2\) whenever ||delta_j||≤beta_l imply, inductively from the top layer,

\[
 \beta_L=B_w,\quad
 D_\ell=\|W_0^{(\ell)}\|_F+2A_0\beta_\ell\alpha/n,\quad
 \beta_{\ell-1}=D_\ell\beta_\ell.                            \tag{18}
\]

Indeed ||W_lhat||F≤D_l by Cauchy–Schwarz for the paired histories, and ||delta_(l−1)||≤||W_lhat||op||delta_l||, because |tanh'|≤1. Dense weights satisfy the same bounds using the exact history integral. Finally
\(\|W^{(1)}(t)\|_F\le\|W^{(1)}_0\|_F+2SX\beta_1\), where X=sup||x||/sqrt(d). These are finite bounds independent of q,K,m and the atom weights. The moment formulas then bound each component for every fixed finite weighted dataset, ensuring continuation through T. The formulas below do not depend on the largest individual label.

### 5.2 Projection identity and depth control

Write Pi_q for the first q Legendre projections on [0,tau]. For a vector history u, let D_u=||u−Pi_qu||² in clock-coordinate L², and u*=(Pi_qu)(tau). The growing-interval projection energy identity is

\[
 \dot D_u=\rho\|u-u^*\|^2.                                 \tag{19}
\]

Here is an explicit justification. The residual u−Pi_qu is orthogonal to every polynomial of degree below q. Differentiate its squared norm on a growing interval. The derivative of the projected polynomial, viewed at fixed history coordinate, remains a polynomial of degree below q, so its interior inner product with the residual vanishes. The moving endpoint contributes exactly rho||u−u*||². The actual historical values u(xi) are fixed once recorded. The initial residual energy is zero for both prescribed prefixes.

The same differentiation for the cross residual pairing gives the exact physical equation

\[
 \dot{\widehat\theta}=F_{\pi_p}(\widehat\theta)+E,\qquad
 E_1=E_w=0,\qquad
 E_\ell=\frac{2\rho}{n}\mathbb E_j[(b_j-b_j^*)(h_j-h_j^*)^T]. \tag{20}
\]

Equivalently, the reconstruction minus its own exact gradient accumulator is 2/n times the cross residual integral. This proves the sign and product structure in (20). By time and data Cauchy–Schwarz and (19),

\[
 \int_0^T\|E_\ell\|_Fdt
 \le\frac2n\sqrt{\mathbb E D_{b,\ell}\,\mathbb E D_{h,\ell-1}}. \tag{21}
\]

For an absolutely continuous u with square-integrable clock derivative, the Legendre equation and integration by parts give

\[
 D_u\le\frac{\tau^2}{4q(q+1)}\int_0^\tau\|u'(\xi)\|^2d\xi. \tag{22}
\]

To see the coefficient, shifted Legendre polynomials p_k satisfy −[x(1−x)p_k']'=k(k+1)p_k. Their derivatives are orthogonal for weight x(1−x). Bessel's inequality bounds the coefficient sum with factor k(k+1) by the weighted derivative energy; every omitted k≥q supplies at least q(q+1). Rescaling [0,1] to [0,tau], and bounding xi(tau−xi)≤tau²/4, proves (22).

It remains to control forward derivatives without assuming that the reconstructed matrix velocity is bounded uniformly in q. Let
\(Z_\ell=\mathbb E_j\int_0^\tau\|(h_j^{(\ell)})'\|^2d\xi\).
Let v_1=2beta_1 X and v_l=2beta_l alpha/n for internal layers. These bound ||F_l||/rho. First-layer chain differentiation gives Z_1≤S(v_1X)².

Endpoint evaluation on degree q−1 polynomials has norm q/sqrt(tau), since sum_{k<q}(2k+1)=q². Projection contraction and the b bound therefore imply
\(\mathbb E\|b-b^*\|^2\le(q+1)^2\beta_\ell^2\).
Using (20), (19), (22), and (q+1)/q≤2 gives

\[
 \int_0^T\rho\|E_\ell/\rho\|_F^2dt
 \le\frac{2\beta_\ell^2A_0^2}{n^2}Z_{\ell-1}.              \tag{23}
\]

For later layers the clock derivative obeys
\(h_\ell'=\phi'(z_\ell)\odot[(F_\ell/\rho+E_\ell/\rho)h_{\ell-1}+W_\ell h_{\ell-1}']\).
Thus, using ||u+v+w||²≤3(||u||²+||v||²+||w||²),

\[
 Z_\ell\le3\left[S v_\ell^2\alpha^2+
 \left(D_\ell^2+\frac{2\beta_\ell^2A_0^2\alpha^2}{n^2}\right)
 Z_{\ell-1}\right].                                       \tag{24}
\]

This finite depth recursion is independent of q and K. The zero backward prefix gives E D_b≤S beta_l². Substitution of (22) and (24) into (21) bounds the total integrated defect by C/sqrt(q(q+1)). The original physical vector field is Lipschitz on the common bounded parameter region with a constant controlled by X,Y,n,L and initialization, not K. Subtracting the dense and perturbed integral equations and applying the same integral inequality as in (14) proves (17).

If the initial residual vanishes, the closure and dense flow are both stationary and (17) is immediate. Otherwise a locally unique autonomous solution cannot reach an equilibrium at a finite regular time and have been nonstationary before it, by uniqueness backward from that state. Thus rho>0 on each nonstationary finite segment, justifying the clock-coordinate differentiation. Alternatively the identities follow by restriction to positive-rho intervals and continuity.

### 5.3 Combination

Add (14) and (17). A Lipschitz predictor estimate on the common bounded parameter region gives (1), with c=log b. Both constants and both inequalities are uniform over the entire data class specified in Section 1. The use of a coreset did not introduce an unverified K-dependence into the temporal theorem.

Any probability measure on the test-input domain satisfies the same RMS prediction discrepancy bound, since an L² norm is at most the uniform norm. For any square-integrable test label distribution, the absolute difference of the two test RMSEs is at most that prediction discrepancy by the reverse triangle inequality. Neither assertion bounds the dense model's statistical generalization error to an unknown ground truth.

## 6. State, computation and accuracy

The moving memory state is

\[
 2(L-1)nqK+nd+n+1.
\]

The nd+n terms are the first weights and readout. Static data storage is O(K(d+1)); static initialized internal matrices cost (L−1)n², exactly as before. Ordinary dense arithmetic for one RHS evaluation costs

\[
 O(Ln^2K+LnqK^2+ndK+LnqK).
\]

The first term is application of the fixed matrices and their transposes, the second applies all learned outer products to the K current response vectors, and the last uses prefix sums for the triangular moment updates. No dense learned matrix need be formed. Restart requires only this state and the static coefficients. Evaluating a new test point uses the same reconstructed matrix actions, with no test history required.

At accuracy epsilon, take q≥2C/epsilon and
p≥c^{-1}log(2C/epsilon). For fixed n,L,T,s,geometry,Y, this gives

\[
 M_{\rm learned}=O\!\left(Ln\,\varepsilon^{-1}
                [\log(1/\varepsilon)]^s+nd+n\right).        \tag{25}
\]

It is independent of m and of the number of elapsed integration steps. It is smaller than storing the internal dense learned matrices when 2qK<n; it need not be smaller at every n or tolerance. The analytic constants and the curse of intrinsic dimension can make the sufficient K very large. No runtime advantage or width-uniform epsilon exponent follows from (25).

The finite-data elimination algorithm has, for example, O(mJ³) arithmetic work with naive nullspace recomputation, and O(J²+Jd) working storage. This is a conservative constructive bound, not an optimized algorithm. Reading all data is unavoidable if the summary is to reflect them. These are arithmetic and real-coordinate counts, not bit-complexity or conditioning bounds for cubature construction. Floating-point moment matching, ODE discretization, and estimating a continuum law add separate numerical/statistical errors.

A useful implementation avoids dividing by tiny weights or storing huge selected labels. Store gamma_j=sqrt(a_j), beta_j=gamma_j y_j, and weighted moments U_{k,j}=gamma_j H_{k,j}, V_{k,j}=gamma_j B_{k,j}. Then 0<gamma_j≤1, sum gamma_j²=1, and sum beta_j²≤Y². With e_j=gamma_j f_j−beta_j, the exact same algorithm becomes

\[
 \rho=\left(\sum_j e_j^2\right)^{1/2},\qquad
 \dot U_{k,j}=\gamma_j\rho h_j-(\rho/\tau)(\mathcal T U)_{k,j},\qquad
 \dot V_{k,j}=e_j\delta_j-(\rho/\tau)(\mathcal T V)_{k,j},
\]
\[
 \widehat W^{(\ell)}=W_0^{(\ell)}-
 \frac2{n\tau}\sum_{j,k}(2k+1)V^{(\ell)}_{k,j}(U^{(\ell-1)}_{k,j})^T,
 \qquad \dot w=-2\sum_j\gamma_j e_jh_j,
\]

with the analogous first-layer source −2 sum_j gamma_j e_j delta_{1,j}x_j^T/sqrt(d), initial U_{0,j}=gamma_j h_j(0), and V=0. Every stored label coefficient is bounded by Y; no y_j or reciprocal a_j is needed at runtime. This removes one obvious numerical hazard, but does not by itself certify the conditioning of the preprocessing linear algebra.

## 7. Why smoothness, rather than an unweighted coefficient norm

A bound on an unweighted l² coefficient norm is not enough for uniform truncation: every single orthonormal basis vector has norm one, however high its index. An l¹ bound also permits a single arbitrary high-frequency mode. Sparsity can help adaptive approximation, but selecting useful modes and controlling their nonlinear feedback is an additional problem.

A regularity-weighted norm supplies the missing compactness. For a circle expansion U(theta)=sum_k U_k exp(ik theta),

\[
 \sum_k(1+k^2)^r\|U_k\|^2\le B^2
 \quad\Longrightarrow\quad
 \sum_{|k|>p}\|U_k\|^2\le B^2(1+p^2)^{-r}.
\]

An exponential coefficient weight gives an exponential tail. The regularity or analytic radius must stay controlled along training. In the theorem above that control is derived on a finite horizon from a common parameter region, not assumed from a good initial snapshot. No norm-minimizing objective is added to the neural training law.

More abstractly, the relevant data distance is the largest difference of their averages of (f_theta−y)grad f_theta over the reachable parameter region. This is exactly the source term in the flow comparison. Input geometry and regularity give a constructive way to make that distance small with finitely many statistics. A basis is a numerical realization of that property; matrix rank alone does not describe it.

There is also a direct coefficient implementation: interpolate the fields H,A,C in a finite input basis, precompute its mu and nu pairings, and evolve nodal sources through the original nonlinear network. The complete finite equations and an O(mesh-size) fixed-q compact-time theorem are in FIELD_ROUTE.md; analytic interpolation gives a spectral refinement there. Its constants can depend on q. The positive-cubature implementation above is used for (1) because its separate temporal proof keeps the constants uniform in both q and the number of retained nodes.

The representation of a smooth field may produce low-rank approximating matrices as a consequence. It does not assume that the exact learned matrix has low rank. Infinitely many inputs can generate an infinite-rank kernel that is uniformly approximable at any fixed tolerance. Conversely, m≫R alone neither proves nor disproves low-rank accuracy. The relevant question is whether the response function class develops fine input-scale structure requiring increasing resolution.

## 8. Exact polynomial example and limits of the conclusion

For affine chi and polynomial activations of degree at most b≥1, a depth-L predictor is a polynomial of input degree at most D_*=b^L. Parameter differentiation does not raise its input degree. Therefore all canonical dense gradients are determined exactly by input moments through degree 2D_* and label-weighted moments through degree D_*. Its loss additionally uses E y². Two data laws matching these moments generate identical vector fields for every parameter value, hence identical training trajectories from the same initialization. One positive cubature with

\[
 K\le\binom{s+2b^L}{s}+\binom{s+b^L}{s}+1
\]

matches these moments simultaneously for every width and initialization. The canonical dense polynomial flows exist globally by the same squared-loss energy argument, so this equality of dense trajectories holds for all t≥0. This is an exact result about compressing the data dependence of that polynomial architecture; the dense learned matrices have not thereby been compressed.

The same statement holds exactly for every finite order-q memory closure, on its common existence interval. The hidden h_l has degree at most b^l, delta_l has degree at most D_*−b^{l−1}, and its A_l, C_l history fields have degrees at most 2D_*−b^{l−1} and D_*−b^{l−1}. Their pairings with H_(l−1) require at most degrees 2D_* and D_*. The same cubature works for every n and q. It removes sample count from the response-memory state exactly, though global existence of every polynomial-activation finite-q closure is not claimed. Thus sample count is not an intrinsic state dimension even for nonlinear feature learning. This example has poor depth dependence and is not a replacement for tanh, but it verifies the organizing principle exactly.

For tanh, the quantitative conclusion is finite-time. Training can sharpen input structure or amplify perturbations at later times. An all-time theorem would require a uniform regularity region and suitable accumulated stability, which are not consequences of data moment matching. Increasing width can also worsen the sufficient analytic radius; no exchange of width and input-resolution limits is proved here.

For unknown data distributions, sample count still affects how accurately their static moments can be estimated. This work removes m from the evolving state conditional on the available distribution information; it does not remove the statistical information requirement.

## 9. Prior ingredients and status

Positive finite moment representations and analytic polynomial approximation are established ingredients, cited above with the complete needed arguments included. Gradient-preserving weighted subsets also predate this work: [CRAIG](https://proceedings.mlr.press/v119/mirzasoleiman20a/mirzasoleiman20a.pdf), equation (2), explicitly targets uniform gradient approximation; its stated convergence theorems use strong convexity, while its neural application updates the subset during training (Section 3.4). The present argument uses a uniform analytic input approximation over a finite-horizon reachable parameter region and a separate response-memory closure. It does not claim novelty for coreset training, polynomial moments or Gronwall stability.

This is a theoretical construction and bound, not empirical validation of an efficient implementation. The scope of any internal check is recorded in README.md and CHECK.md. The paper and maintained book are unchanged.
