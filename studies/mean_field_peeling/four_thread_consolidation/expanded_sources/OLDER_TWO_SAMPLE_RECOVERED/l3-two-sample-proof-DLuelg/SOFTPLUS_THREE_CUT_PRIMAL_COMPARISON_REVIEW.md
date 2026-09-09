# Isolated adversarial mathematical audit

Candidate: `/tmp/l3-two-sample-proof-DLuelg/SOFTPLUS_THREE_CUT_PRIMAL_COMPARISON.md`

Candidate SHA-256:

```text
51323710f5c02314f232b3fa8e42a7dc9c0c385530398c009fa28a595bf3f02f
```

Audited version: 32,606 bytes, 1,050 lines. Review date: 2026-09-06.

The full candidate was read. It was the sole mathematical and contextual input. The named plan was not opened; no project files, history, other reviews, external sources, experiments, or agents were used. Verification below is analytical, including exact arithmetic on the displayed terminating decimals. The rigorous-math skill supplied procedural guidance only. The candidate was not edited.

## Verdict and required findings

**No required mathematical correction found within the candidate's stated scope.** The finite Euler bounds, raw-coordinate normalization, exact product identities, feature increment estimates, Gaussian covariance-metric consequence, asymmetric vector-field comparison, and conditional extensions are valid. All displayed numerical coefficients checked below are correct upper bounds; the coefficients described as exact sums are indeed those exact sums.

The conclusions are understood with their inherited hypotheses: the initial conditions (17) for the short primal estimates; the common input data, primal box, and finite old caps for (35); ordered old/new cuts when replacing mismatch defects by old truncation defects; and supplied bounded base operators for the population formulation. Section 6 is a consequence of Section 5 under those comparison hypotheses. It does not create an ordering-free old-tail theorem. Two useful restatements of inherited hypotheses are listed as optional findings near the end.

There is no missing global theorem to prove here. In particular, a construction or identification of an infinite-width Gaussian program, a population limit, uniform tail decay, or global flow continuation is not needed to establish the claims actually made.

## 1. Norms and canonical input-span normalization

### 1.1 Operator and rank-one norms

On \(E_n\), an orthonormal basis is \(e_j^{(n)}=\sqrt n\,e_j\), where \(e_j\) is the ordinary coordinate basis. Therefore the operator Hilbert--Schmidt norm is

\[
\sum_j\|We_j^{(n)}\|_n^2
=\sum_j\sum_i W_{ij}^2.
\]

Thus the unnormalized Frobenius norm in the candidate is exactly the operator HS norm. Scaling both the domain and range Euclidean inner products by the same factor leaves the operator norm and transpose unchanged. In particular, \(W^*=W^{\mathsf T}\), and \(\|W\|_{\rm op}\leq\|W\|_{\rm HS}\).

For the specified tensor,

\[
(u\otimes_n v)_{ij}=\frac{u_iv_j}{n},
\qquad
\|u\otimes_n v\|_{\rm HS}^2
=\frac{\sum_i u_i^2\sum_j v_j^2}{n^2}
=\|u\|_n^2\|v\|_n^2.
\]

Equation (1) is correct. An extra factor \(n^{-1/2}\) in the matrix HS norm would have been an error; none is present. Likewise,

\[
\|\delta x^{\mathsf T}\|_{n,2}=\|\delta\|_n\|x\|_{\mathbb R^2},
\]

which is the raw first-coordinate identity used later.

### 1.2 Input coordinates and the first raw metric

The displayed coordinates satisfy

\[
a^2+b^2=1,\qquad a^2-b^2=\rho.
\]

Consequently \(x_\pm\) have Euclidean norm one and the Gram matrix is exactly (2). These are coordinates of the *normalized* original vectors \(X_c/\sqrt d\), not an assertion that the original \(X_c\) themselves have Euclidean norm one.

Let \(Q\) have orthonormal columns spanning the original input span, with the appropriate one-coordinate embedding at a rank-one endpoint. Then

\[
X_c=\sqrt d\,Qx_c,
\qquad
\Theta=\sqrt d\,W^{(1)}Q,
\qquad
W^{(1)}X_c=\Theta x_c.
\]

For an increment \(V\) of \(W^{(1)}\) supported on this span, meaning \(V=VQQ^{\mathsf T}\),

\[
\|\sqrt d\,VQ\|_{n,2}^2
=\frac dn\|VQ\|_F^2
=\frac dn\|V\|_F^2.
\]

This proves the claimed isometry with the stated canonical raw first-weight metric. For an arbitrary increment the corresponding equality is with its span component \(VQQ^{\mathsf T}\). The candidate expressly restricts the equality to span increments and freezes the orthogonal directions, so it does not mistakenly claim the isometry for unrestricted increments.

One can also check the update directly in original coordinates. The span update corresponding to (9) is

\[
F_{W^{(1)}}
=\frac1{2d}\sum_c y_c\delta_1^c X_c^{\mathsf T}.
\]

Multiplying on the right by \(\sqrt d\,Q\) produces \(F_\Theta\) in (9). Multiplying by \(X_c\) gives

\[
F_{z_1^c}
=\frac12\sum_s y_s\frac{X_s\cdot X_c}{d}\delta_1^s
=\frac12\sum_s y_s C_{cs}\delta_1^s.
\]

There is no missing factor of \(d\), \(n\), or \(\sqrt d\) in (9), (12), or (13).

For an independent first-weight row with entry variance \(1/d\),

\[
\operatorname{Cov}(W^{(1)}_iX_c,W^{(1)}_iX_d)
=\frac{X_c\cdot X_d}{d}=C_{cd}.
\]

Orthogonal projection gives independent standard normal active coordinates in that row. At \(\rho=1\), only the \(a\)-coordinate is used; at \(\rho=-1\), only the \(b\)-coordinate is used. The unused coordinate can be set to zero in the reduced representation, while original orthogonal weights remain frozen. This introduces no additional Gaussian variable into the represented preactivations. No inverse Gram matrix is needed.

### 1.3 Hidden matrices and readout

The hidden matrices act by ordinary multiplication and their coordinate velocities are

\[
(F_2)_{ij}=\frac1{2n}\sum_c y_c\delta_{2,i}^c h_{1,j}^c,
\qquad
(F_3)_{ij}=\frac1{2n}\sum_c y_c\delta_{3,i}^c h_{2,j}^c.
\]

The \(1/n\) is in the rank-one update, not in a redefinition of the matrices. For identity cuts these are also the derivatives of \(\frac12\sum_c y_cf_c\) in the stated HS metric; the first-coordinate and readout derivatives in their RMS metrics are the other components of (9). This checks the scaling without assuming that the cut field is itself a gradient.

The term “canonical” is verified here relative to the original-input normalization and raw metrics explicitly stated in the candidate. No external plan or alternative convention was imported to support that word.

## 2. Activation and cut assumptions

The activation bounds are valid:

\[
0<g(x)<0.1,\qquad
g'(x)=0.1\sigma(x)(1-\sigma(x))\in[0,0.025],
\]

and

\[
\phi(x)\leq 1+0.1\log2+0.1|x|\leq2+0.1|x|.
\]

Thus the pointwise Lipschitz constants \(0.1\) and \(0.025\) pass unchanged to finite RMS and probability-space \(L^2\) norms. The feature norm estimate uses the triangle inequality and the fact that the constant function \(1\) has norm one. It does not assert that a product of two general \(L^2\) fields is in \(L^2\).

Assumption (4) implies \(\tau(0)=0\), contraction of the norm, and a Lipschitz constant at most one. The derivative observations are correct: an everywhere differentiable scalar map with derivative bounded by one is Lipschitz by the mean-value theorem, and an absolutely continuous map with the derivative bound almost everywhere is Lipschitz by integration. Hard clipping is allowed under (4).

The smooth family (6a) also checks out. On the transition interval,

\[
\psi'(t)=\tfrac32-t.
\]

Its value and derivative match the neighboring pieces at \(t=1/2\) and \(t=3/2\). Odd extension is continuously differentiable at zero and at the negative junctions. On the positive half-line it is increasing, no larger than \(t\), and no larger than one. Therefore \(r\psi(x/r)\) contracts absolute values, is 1-Lipschitz, and has actual output cap \(r\).

For \(t\geq0\), monotonicity of \(\psi'\) gives

\[
\psi(t)-t\psi'(t)
=\int_0^t[\psi'(s)-\psi'(t)]\,ds\geq0.
\]

The derivative with respect to \(r\) displayed in the candidate is consequently nonnegative for \(x\geq0\). Hence

\[
0\leq\tau_r(x)\leq\tau_s(x)\leq x
\quad (x\geq0,\ r\leq s).
\]

Oddness proves (36) for negative \(x\), and the definitions at zero and infinity preserve it. The identity radius is \(r/2\), whereas the output cap is \(r\); the proof does not confuse those two quantities. The separate warning that a cut with ceiling \(2r\) contributes cap \(2r\) is appropriate.

## 3. Exact Euler identities

All products and updates in (7)--(16) have compatible types and normalizations. In particular, the cut of \(w\) is used only in \(\delta_3\); the readout update contains the uncut feature \(h_3\).

Writing \(\Theta=(u,v)\), the two columns of (9) are

\[
F_u=\frac a2(\delta_1^+-\delta_1^-),
\qquad
F_v=\frac b2(\delta_1^++\delta_1^-),
\]

which verifies (12), including the second-column plus sign. Applying the raw first-coordinate update to \(x_c\) gives (13).

For either hidden layer, the identity

\[
W'h'-Wh=W'(h'-h)+(W'-W)h
\]

is exact. Substituting the Euler matrix increment gives precisely (14), because

\[
(\delta^d\otimes_n h^d)h^c
=\delta^d\langle h^d,h^c\rangle_n.
\]

The use of the *next* matrix \(W'\) includes the cross term. Written in an alternative expansion, that term is

\[
W'(h'-h)=W(h'-h)+(W'-W)(h'-h).
\]

Nothing of order \(\Delta_k^2\) was dropped or estimated as zero.

For each scalar coordinate, the fundamental theorem of calculus gives (15), including when the increment is zero. The integral defining the diagonal gate lies between zero and \(0.1\), so its operator norm is at most \(0.1\).

Finally,

\[
\langle w',h'\rangle_n-\langle w,h\rangle_n
=\langle w',h'-h\rangle_n+\langle w'-w,h\rangle_n
\]

proves (16) with the same exact cross-term convention. No prediction estimate subsequently assumes a cut readout increment.

## 4. Finite short primal bounds

### 4.1 Bounds inside the provisional box

Within (19), the forward bound table is obtained by successive operator and activation estimates:

| Quantity | Verified upper bound |
|---|---:|
| \(\|h_1^c\|_n\) | \(2+0.1(3)=2.3\) |
| \(\|z_2^c\|_n\) | \(11(2.3)=25.3\) |
| \(\|h_2^c\|_n\) | \(2+0.1(25.3)=4.53\) |
| \(\|z_3^c\|_n\) | \(11(4.53)=49.83\) |
| \(\|h_3^c\|_n\) | \(2+0.1(49.83)=6.983<7\) |

Writing \(\omega=\|w\|_n\), contractions, bounded gates, and operator bounds give

\[
\|\delta_3^c\|_n\leq0.1\omega,
\quad
\|q_2^c\|_n\leq1.1\omega,
\quad
\|\delta_2^c\|_n\leq0.11\omega,
\quad
\|q_1^c\|_n\leq1.21\omega,
\quad
\|\delta_1^c\|_n\leq0.121\omega.
\]

Every cap disappears from these primal estimates. None of these steps requires a coordinatewise bound on an uncut query.

The averaged raw velocities then satisfy

\[
\|F_w\|_n\leq7,\qquad
\|F_\Theta\|_{n,2}\leq0.121\omega,
\qquad
\|F_2\|_{\rm HS}\leq0.253\omega,
\qquad
\|F_3\|_{\rm HS}\leq0.453\omega,
\]

since \(0.11(2.3)=0.253\) and \(0.1(4.53)=0.453\). The projected first velocity has the same \(0.121\omega\) bound because \(|C_{cd}|\leq1\). For the raw first velocity, each outer product has norm \(\|\delta_1^c\|_n\); no recovery from projected coordinates or inverse of \(C\) is being used.

### 4.2 The induction closes without a mesh restriction

Starting from \(w_0=0\), summation gives \(\omega_j\leq7t_j\) at preceding nodes. The exact telescoping formula is

\[
\sum_{j<k}\Delta_jt_j
=\tfrac12\left(t_k^2-\sum_{j<k}\Delta_j^2\right)
\leq\tfrac12t_k^2.
\]

Therefore all the displacement coefficients in (18) are correct:

| Displacement | Exact coefficient of \(t_k^2\) |
|---|---:|
| Raw first coordinates; also first preactivations | \(0.121(7)/2=0.4235\) |
| \(W_2\), in HS norm | \(0.253(7)/2=0.8855\) |
| \(W_3\), in HS norm | \(0.453(7)/2=1.5855\) |

At \(t_k=0.1\), these imply respectively

\[
\max_c\|z_{1,k}^c\|_n\leq2.004235<3,
\]

\[
\|W_{2,k}\|_{\rm op}\leq10.008855<11,
\qquad
\|W_{3,k}\|_{\rm op}\leq10.015855<11,
\]

and \(\|w_k\|_n\leq0.7<1\). Initial states satisfy the provisional box, and the estimates at node \(k\) only use earlier-node velocities. This proves the induction without presupposing control of a next-step matrix. Arbitrary positive mesh increments are permitted as long as \(t_N\leq0.1\), including a single step of length \(0.1\).

Initial matrix HS norms need not be bounded. Only initial operator norms and the HS norms of *increments* are used. Likewise, a large input-invisible component of \(\Theta_0\) does not undermine the displacement estimate: the velocity itself is controlled directly and lies in the input span.

The five coefficients in (24) are exactly (7) times those in (21): \(0.7,7.7,0.77,8.47,0.847\). There is no coefficient error in this section.

## 5. Forward increments and time metrics

Once the induction has controlled both endpoint matrices, (14) yields

\[
\|\Delta z_{2,k}^c\|_n
\leq\left[11(0.0121)+0.253(2.3)\right]\Delta_k\omega_k
=0.715\Delta_k\omega_k,
\]

and

\[
\|\Delta z_{3,k}^c\|_n
\leq\left[11(0.0715)+0.453(4.53)\right]\Delta_k\omega_k
=2.83859\Delta_k\omega_k.
\]

The arithmetic in (25)--(26) is exact:

| Calculation | Result |
|---|---:|
| \(0.1(0.121)\) | \(0.0121\) |
| \(11(0.0121)\) | \(0.1331\) |
| \(0.253(2.3)\) | \(0.5819\) |
| \(0.1331+0.5819\) | \(0.715\) |
| \(0.1(0.715)\) | \(0.0715\) |
| \(11(0.0715)\) | \(0.7865\) |
| \(0.453(4.53)\) | \(2.05209\) |
| \(0.7865+2.05209\) | \(2.83859\) |
| \(0.1(2.83859)\) | \(0.283859\) |

For a nodal feature interpolant, the slope on interval \(k\) has norm at most its coefficient in (25) times \(\omega_k\). At a time \(v\) in that interval,

\[
\omega_k\leq7t_k\leq7v.
\]

Integrating this bound, split at mesh points if necessary. The resulting coefficients are

| Feature | Coefficient of \(t^2-u^2\) | Coefficient of \(S|t-u|\) |
|---|---:|---:|
| \(H_1\) | \(7(0.0121)/2=0.04235\) | \(0.0847\) |
| \(H_2\) | \(7(0.0715)/2=0.25025\) | \(0.5005\) |
| \(H_3\) | \(7(0.283859)/2=0.9935065\) | \(1.987013\) |

The second column is converted to the third using \(t+u\leq2S\). Endpoint feature bounds persist under convex interpolation.

For physical features recomputed from the raw linear interpolant, the box persists because the first preactivations are affine in the raw first coordinates, the operator norm is convex, and the readout norm is convex. The frozen raw derivatives on interval \(k\) satisfy (22). Differentiating the two products gives exactly (28), which uses current features and current matrices but frozen velocities. Their bounds again give \(0.715\omega_k\) and \(2.83859\omega_k\) for the preactivation derivatives. The same time estimates follow. The candidate correctly distinguishes this interpolation from nodal feature interpolation.

The time statements are understood on the domain of the interpolants, namely \([0,t_N]\). Making that domain explicit in the displayed quantifier would be helpful but does not affect any estimate; see optional finding O2.

## 6. Gaussian covariance-metric consequence

For deterministic feature paths, (29) is a finite linear combination of a standard Gaussian vector. For each source group it therefore defines a centered jointly Gaussian family, and

\[
\mathbb E\xi_{\ell,c}(t)\xi_{\ell,d}(u)
=\frac1n\sum_i H_{\ell-1,i}^c(t)H_{\ell-1,i}^d(u).
\]

Using the same Gaussian vector for both sample indices is necessary for the cross-sample Gram covariance in (30), and the construction does so. The two source groups use independent Gaussian arrays.

In particular, there is the exact metric identity

\[
\mathbb E|\xi_{\ell,c}(t)-\xi_{\ell,c}(u)|^2
=\|H_{\ell-1}^c(t)-H_{\ell-1}^c(u)\|_n^2.
\]

Thus (31) has exactly the first two time constants from (27), \(0.0847S\) and \(0.5005S\). The variance bounds are respectively \(2.3^2=5.29\) and \(4.53^2=20.5209\). Initially, (17) yields

\[
\|h_{1,0}^c\|_n\leq2.2,
\quad
\|z_{2,0}^c\|_n\leq10(2.2)=22,
\quad
\|h_{2,0}^c\|_n\leq4.2,
\]

so the sharper variances \(2.2^2=4.84\) and \(4.2^2=17.64\) are valid.

For random feature paths satisfying the hypotheses almost surely, fresh Gaussians independent of the entire path give these identities *conditionally* on that path. The unconditional process produced that way need not be Gaussian; it can be a mixture of Gaussian laws. The candidate does not claim otherwise: it explicitly makes the conditional interpretation and distinguishes it from a separately specified Gaussian source with the expected Gram covariance.

For such a separately specified centered Gaussian source, let

\[
K((c,t),(d,u))
=\mathbb E\langle H^c(t),H^d(u)\rangle.
\]

Its increment variance is

\[
K((c,t),(c,t))+K((c,u),(c,u))-2K((c,t),(c,u))
=\mathbb E\|H^c(t)-H^c(u)\|^2.
\]

The uniform squared feature bound can therefore be averaged to obtain the same metric inequality. The kernel is positive semidefinite since every finite quadratic form is the expectation of a squared Hilbert norm. This explains precisely why the covariance-metric consequence is valid and what information it uses.

It does not identify original evolved network sources as conditionally Gaussian, prove independence of evolved neurons, or establish a width limit. No such identification is needed here.

## 7. The asymmetric comparison and every numerical coefficient

### 7.1 Forward differences

The raw first-coordinate bound gives \(A_1\leq d_\theta\). The two exact product splits give

\[
A_2\leq11(0.1A_1)+2.3d_2
\leq1.1d_\theta+2.3d_2\leq2.3D,
\]

\[
A_3\leq11(0.1A_2)+4.53d_3
\leq1.21d_\theta+2.53d_2+4.53d_3\leq4.53D.
\]

The coefficient \(2.53\) is \(1.1(2.3)\), and \(1.21=1.1^2\). Feature differences are bounded by \(0.1A_\ell\). Equation (40) is correct even at singular \(C\), because it starts from raw first coordinates.

### 7.2 The essential multiplication estimate

For a single layer, inserting \(\tau^n(v)\) into (41) gives

\[
\begin{aligned}
\|\tau^n(\widetilde v)g(\widetilde z)-\tau^o(v)g(z)\|_2
\leq{}&0.1\|\widetilde v-v\|_2
+0.1\|\tau^n(v)-\tau^o(v)\|_2\\
&+0.025r\|\widetilde z-z\|_2.
\end{aligned}
\]

Here the last estimate uses the pointwise bound \(|\tau^o(v)|\leq r\), and only that old cut is put in \(L^\infty\). The new cut is used through its Lipschitz property. This is valid for finite RMS or population \(L^2\) fields. It neither multiplies two uncontrolled \(L^2\) fields nor imports a new-cap ceiling.

The old deltas in the adjoint splits (43) satisfy \(\|\delta_3\|_2\leq0.1\) and \(\|\delta_2\|_2\leq0.11\). Operator differences are bounded by their HS norms. These facts prove the first inequalities in each row of (44).

### 7.3 Backward coefficient audit

Successive substitution yields the following exact bookkeeping. Each row lists the coefficient of \(D\), followed by the coefficients of the three defects.

| Quantity | Constant part | Coefficient of \(R\) | \(E_w\) | \(E_2\) | \(E_1\) |
|---|---:|---:|---:|---:|---:|
| \(B_3\) | \(0.1\) | \(0.025(4.53)=0.11325\) | \(0.1\) | \(0\) | \(0\) |
| \(Q_2\) | \(11(0.1)+0.1=1.2\) | \(11(0.11325)=1.24575\) | \(1.1\) | \(0\) | \(0\) |
| \(B_2\) | \(0.1(1.2)=0.12\) | \(0.124575+0.0575=0.182075\) | \(0.11\) | \(0.1\) | \(0\) |
| \(Q_1\) | \(11(0.12)+0.11=1.43\) | \(11(0.182075)=2.002825\) | \(1.21\) | \(1.1\) | \(0\) |
| \(B_1\) | \(0.1(1.43)=0.143\) | \(0.2002825+0.025=0.2252825\) | \(0.121\) | \(0.11\) | \(0.1\) |

For \(B_2\), the two cap terms are \(0.1(1.24575)R\) and \(0.025(2.3)R\). For \(B_1\), they are \(0.1(2.002825)R\) and \(0.025R\). A cap is never multiplied by a preceding \(B\) or \(Q\) bound. This proves, rather than merely suggests, the absence of cap products.

### 7.4 Raw velocity coefficients

Equation (45) follows from the unit norm of the inputs and the averaged sum. The exact tensor split (46) permits the new feature to be controlled in RMS and the old delta to be controlled in RMS; the HS norm of their tensor is the product of those two norms. It requires no coordinatewise ceiling for the feature.

Thus

\[
\|\Delta F_2\|_{\rm HS}\leq2.3B_2+0.011A_1,
\quad
\|\Delta F_3\|_{\rm HS}\leq4.53B_3+0.01A_2,
\quad
\|\Delta F_w\|_n\leq0.1A_3.
\]

The coefficient table is consequently

| Velocity component | Constant part of \(D\) coefficient | Coefficient of \(RD\) | \(E_w\) | \(E_2\) | \(E_1\) |
|---|---:|---:|---:|---:|---:|
| \(F_\Theta\) | \(0.143\) | \(0.2252825\) | \(0.121\) | \(0.11\) | \(0.1\) |
| \(F_2\) | \(2.3(0.12)+0.011=0.287\) | \(2.3(0.182075)=0.4187725\) | \(0.253\) | \(0.23\) | \(0\) |
| \(F_3\) | \(4.53(0.1)+0.01(2.3)=0.476\) | \(4.53(0.11325)=0.5130225\) | \(0.453\) | \(0\) | \(0\) |
| \(F_w\) | \(0.1(4.53)=0.453\) | \(0\) | \(0\) | \(0\) | \(0\) |

Adding the rows gives exactly

\[
0.143+0.287+0.476+0.453=1.359,
\]

\[
0.2252825+0.4187725+0.5130225=1.1570775,
\]

and defect coefficients

\[
0.121+0.253+0.453=0.827,
\qquad
0.11+0.23=0.34,
\qquad
0.1.
\]

These verify the first inequality of (35) in full. For the second,

\[
2(1+R)-(1.359+1.1570775R)
=0.641+0.8429225R\geq0
\]

for every \(R\geq0\), and all three defect coefficients are at most one. There is no downward rounding.

For identical cuts the defects vanish exactly, giving local Lipschitz continuity in the full raw state norm. This is stronger than merely controlling the two first-layer projections, and it does not become singular as \(\rho\to\pm1\).

## 8. Different-cut mismatches versus nested old tails

The definitions in (34) are precisely what (42) needs: each mismatch is evaluated at the *old* input to the relevant cut. In particular, the old \(q_2\) uses the old \(w\)-cut and the old \(W_3\); the old \(q_1\) uses the old \(q_2\)-cut and old \(W_2\). They are not uncut or new-reference queries.

For arbitrary cuts satisfying (4), (35) is valid with these exact mismatches. No ordering is needed for that statement, and the new cuts can be uncapped.

For a common family satisfying (36), replacement by (37) additionally uses componentwise ordering of new and old parameters. The sufficient condition stated in Section 5, \(r_j\leq R\leq s_j\), supplies that ordering. The weaker condition \(r_j\leq s_j\) would also suffice. Pointwise (36) then gives \(E_j\leq T_j\).

For hard clipping,

\[
|x-\tau_r(x)|=(|x|-r)_+,
\]

so (38) is exact. For a general cut that is identity on \([-\alpha r,\alpha r]\), the defect vanishes inside that interval and outside it obeys

\[
|x-\tau_r(x)|\leq|x|+|\tau_r(x)|\leq2|x|.
\]

For a sign-preserving contraction, \(\tau_r(x)\) lies between zero and \(x\) in the signed order, so the factor becomes one. Equation (39) is valid without an unstated positivity hypothesis; the positivity improvement is separately qualified.

The candidate's example also correctly establishes the necessity of a relationship between the cuts: at \(x=1/2\), old hard clipping at one gives zero truncation defect, whereas a new zero map gives mismatch \(1/2\), despite satisfying the advertised ceiling of two. A ceiling is only an upper bound; it does not order the cut maps.

Even for the hard-clip family itself, reversing cap order can invalidate an old-tail replacement. At \(x=1/2\), old cap one and new cap zero have zero old tail and nonzero mismatch. Thus the inherited ordering condition must be retained in the Euler and continuous-time consequences. This is the optional restatement in O1, not a defect in the comparison proof under its stated ordered-cut hypotheses.

## 9. Other primal balls

The feature bounds \(H_1,H_2,H_3\) and forward difference constants \(L_2,L_3\) following (47) are valid. Using sums instead of maximum coefficients in \(L_2=0.1\beta_2+H_1\) and \(L_3=0.1\beta_3L_2+H_2\) only makes them conservative.

The old backward bounds are

\[
\|\delta_3^c\|_2\leq0.1m_w,
\qquad
\|\delta_2^c\|_2\leq0.01\beta_3m_w.
\]

Consequently the extra operator-difference terms entering \(B_2\) and \(B_1\) are \(0.01m_wD\) and \(0.001\beta_3m_wD\), respectively. This verifies (47a). In (47b), the additional terms come from the old deltas in the two tensor splits and the readout:

\[
0.001\beta_3m_w A_1+0.01m_w A_2+0.1A_3
\leq(0.001\beta_3m_w+0.01m_wL_2+0.1L_3)D.
\]

There is no hidden cap dependence in these coefficients.

For an explicit certificate of (47c), substitution in the displayed recurrences even gives

\[
\begin{aligned}
\|F^n(\widetilde U)-F^o(U)\|_{L^2/\mathrm{HS}}
\leq{}&[c_0+c_1R]D
+0.1L_3E_w+0.1L_2E_2+0.1E_1,\\
c_0={}&0.2L_3+0.02m_wL_2+0.002\beta_3m_w,\\
c_1={}&0.025(1+L_2^2+L_3^2).
\end{aligned}
\]

To see this, combine \(B_1+H_1B_2\) using the last row of (47a), which makes the coefficient of \(B_2\) equal to \(L_2\); substitution of the \(B_2\) row then makes the coefficient of \(B_3\) equal to \(L_3\). Substituting \(B_3\) and adding the remainder in (47b) gives the formula above. Hence one may choose

\[
C_{\rm ball}
=\max\{c_0,c_1,0.1L_3,0.1L_2,0.1\}.
\]

This is not a needed replacement for the candidate's proof; it verifies explicitly that its asserted constant depends only on the ball and that the cap dependence remains linear.

## 10. Prediction, Euler, and conditional continuous-time consequences

The prediction split (48) is valid by Cauchy--Schwarz:

\[
|\widetilde f_c-f_c|
\leq7d_w+\|w\|_n(0.1A_3)
\leq7d_w+0.453D\leq7.453D.
\]

For two Euler references satisfying the comparison hypotheses, take the triangle inequality in each of the four raw component norms. This gives (49) with \(E\) first; ordered cuts then allow \(T\). The coefficient \(2(1+R)\) is exactly the coarse coefficient already proved in (35).

Let \(a=2(1+R)\) and \(T_j=T_{w,j}+T_{2,j}+T_{1,j}\). Direct iteration gives

\[
D_k\leq D_0\prod_{\ell<k}(1+a\Delta_\ell)
+\sum_{j<k}\Delta_jT_j\prod_{j<\ell<k}(1+a\Delta_\ell).
\]

The products are nonnegative, and \(1+x\leq e^x\) for \(x\geq0\) yields (50). The forcing exponent is correctly \(t_k-t_{j+1}\): the term inserted at step \(j\) is propagated only through subsequent steps. For \(j=k-1\), the product is empty and its exponent is zero. There is no off-by-one error.

For differentiable finite reference solutions, the same initial conditions and short time interval permit the continuous box argument: before a possible first exit, \(\|w(t)\|\leq7t\), and integrating the other velocity bounds gives the same quadratic constants. The strict box improvement excludes such an exit during the stated interval, conditional on the solution being defined there. The physical feature chain rule gives the same time metrics.

For two solutions remaining in the box, let \(T(t)\) denote the sum of ordered old defects. The integral form of (35) gives

\[
D(t)\leq D(0)+\int_0^t[aD(s)+T(s)]\,ds.
\]

If \(Y(t)\) is the right side, then \(D\leq Y\) and \(Y'\leq aY+T\). Multiplication by \(e^{-at}\) and integration prove (51). This argument does not differentiate a norm at its zero set or assume differentiability of \(D\) itself.

Neither estimate states that the forcing defects tend to zero. The exponential factor also does not by itself justify passage to arbitrarily large caps. No such passage is asserted.

## 11. Conditional population-space formulation

### 11.1 Operators, adjoints, and kernels

On the specified probability spaces, a square-integrable kernel defines a bounded operator because

\[
\begin{aligned}
\|Kf\|_2^2
&\leq\int\left(\int|K(y,x)|^2\,d\mu_1(x)\right)
\left(\int|f(x)|^2\,d\mu_1(x)\right)d\mu_2(y)\\
&=\|K\|_{L^2(\mu_2\otimes\mu_1)}^2\|f\|_2^2.
\end{aligned}
\]

The HS norm agrees with the kernel norm. One way to verify the identification is first to take a finite sum of rectangular tensor kernels. Such kernels give finite-rank operators, and expansion in orthonormal bases of the finite spans shows equality of the two squared norms. Finite sums of product functions are dense in product \(L^2\); passing to the completion gives the stated identity for an arbitrary square-integrable kernel.

For \(f\in E_1\), \(g\in E_2\), the absolute integral of \(K(y,x)f(x)g(y)\) is bounded by

\[
\|K\|_{L^2(\mu_2\otimes\mu_1)}\|f(x)g(y)\|_{L^2(\mu_2\otimes\mu_1)}
=\|K\|_{\rm HS}\|f\|_2\|g\|_2.
\]

Fubini therefore applies to the bilinear pairing and proves the kernel-adjoint formula. For the bounded base operators, \(A_\ell^*\) is the Hilbert-space adjoint; it need not be given by a kernel. Thus \(W_\ell^*=A_\ell^*+K_\ell^*\) is well-defined exactly as stated.

The rank-one update kernel is \(\delta(y)h(x)\), with squared norm

\[
\int|\delta(y)|^2\,d\mu_\ell(y)
\int|h(x)|^2\,d\mu_{\ell-1}(x).
\]

This proves its HS norm formula and matches the finite normalization. More explicitly, for uniform \(n\)-point probability spaces a matrix \(W\) corresponds to the integral kernel \(K(i,j)=nW_{ij}\). Its kernel norm is the ordinary Frobenius norm of \(W\), and a kernel increment \(\delta_i h_j\) corresponds to the matrix increment \(\delta_i h_j/n\). Thus the population notation does not silently change the raw finite matrix metric.

### 11.2 Well-defined fields and transfer of the inequalities

Probability mass one makes the activation's constant part integrable with the same norm used in the finite estimates. The gates are bounded, cuts are contractions, and all \(W_\ell\) and adjoints are bounded. Therefore all forward and backward fields lie in the appropriate \(L^2\) spaces. Tensor velocities are HS.

For two states, the fixed \(A_\ell\) are common. Thus \(\widetilde W_\ell-W_\ell=\widetilde K_\ell-K_\ell\) is HS even if \(A_\ell\) is not. All uses of an HS bound on a matrix difference remain valid. For a single Euler reference, its updates preserve this affine operator class.

The finite proofs use Hilbert norms, operator bounds, bounded multiplication by gates or old cuts, scalar Lipschitz inequalities, and rank-one HS identities. These all hold in the supplied spaces. In particular, no step in (35) asks for an \(L^2\times L^2\to L^2\) multiplication estimate. The same numerical local inequality is valid.

The physical-interpolation derivative argument also remains sound along the relevant \(L^2\) paths. For a fixed \(z,v\in L^2\), boundedness of \(g\) and scalar differentiation imply

\[
\frac{\phi(z+hv)-\phi(z)}h\longrightarrow g(z)v
\quad\text{in }L^2,
\]

by dominated convergence, since the quotient is bounded in absolute value by \(0.1|v|\). If a path increment is \(hv+o(h)\) in \(L^2\), the Lipschitz property of \(\phi\) controls the additional \(o(h)\) error. This justifies the chain rule along a differentiable path; it does not require an unproved assertion of Fréchet differentiability of the Nemytskii map on all of \(L^2\).

If the Gaussian-metric observation is also transported to a supplied population feature path, the finite Gaussian sum is replaced by a Gaussian linear functional on the closed span of that path. That span is separable: a finite union of norm-continuous paths on a compact interval is generated densely by its values at a countable dense set of times. Choose an orthonormal basis \(e_m\) of the span and independent standard normals \(G_m\), and define

\[
Z(h)=\sum_mG_m\langle h,e_m\rangle
\]

as a series converging in the auxiliary probability-space \(L^2\). Its covariance is \(\langle h,k\rangle\), so the same metric identity follows. This is an auxiliary Gaussian construction and supplies no Gaussian representation of \(A_2\) or \(A_3\).

The population result is consequently a valid conditional operator-space statement. It does not require, and does not provide, an identification of these bounded base operators with a finite-width random initialization or its limit.

## 12. State-dependent sample coefficients

The extension changes the outer sample weights to \(b_c(U)\); it leaves the definitions of the cut backward fields in (8) unchanged. With this meaning, it is valid.

If \(|b_c(U)|\leq1\) throughout the box, every velocity bound used in the short-time induction survives because it used

\[
\left\|\tfrac12\sum_c y_cV_c\right\|
\leq\tfrac12\sum_c\|V_c\|.
\]

No cancellation between the two labels was used to obtain the numerical primal constants. The Euler product identities still follow by substitution of the actual frozen velocities. The uncut readout velocity becomes \(\frac12\sum_c b_c(U)h_3^c\); it is generally no longer the difference of the two features. Likewise the two first-coordinate columns become

\[
F_u=\frac a2\bigl(b_+\delta_1^++b_-\delta_1^-\bigr),
\qquad
F_v=\frac b2\bigl(b_+\delta_1^+-b_-\delta_1^-\bigr).
\]

These are the intended substitutions of the weights in (9)--(10), not an assertion that the specialized label-difference shorthand remains literal for general coefficients.

For any one component with sample field \(V_c\), split

\[
b_c(\widetilde U)V_c^n(\widetilde U)-b_c(U)V_c^o(U)
=b_c(\widetilde U)[V_c^n(\widetilde U)-V_c^o(U)]
+[b_c(\widetilde U)-b_c(U)]V_c^o(U).
\]

The first term is bounded by the existing componentwise comparison because the new coefficient has absolute value at most one. The second term is controlled by (53) and the norms of the *old unweighted sample fields*:

| Component | Bound on the old sample-field norm |
|---|---:|
| Raw first coordinates | \(0.121\) |
| \(W_2\) | \(0.11(2.3)=0.253\) |
| \(W_3\) | \(0.1(4.53)=0.453\) |
| Readout | \(7\) |

Their sum is exactly

\[
0.121+0.253+0.453+7=7.827.
\]

The two terms in the sample sum are averaged by \(1/2\); this introduces no extra factor of two. Thus the sharp first bound in (35) can be augmented by \(7.827L_bD\), and its coarse form is precisely (54).

Both old and new states must use the same coefficient functions as specified in (53). If two unrelated coefficient functions were compared, an additional mismatch would be needed, but the candidate makes no such claim. Similarly, it does not cover moving coefficients inside nonlinear cuts, or an unbounded loss derivative. These are scope restrictions already reflected in the setup, not omitted terms in (54).

## Optional findings

### O1. Repeat the ordered-cap hypothesis in Section 6

Location: the Euler consequence beginning at candidate line 910, and the continuous-time consequence beginning at line 940.

Section 5 correctly states the ordering needed for \(E_j\leq T_j\). In Section 6, “for a family satisfying (36)” is best read together with that preceding ordered-comparison setup. For independent quotation of (49)--(51), add a short phrase such as “with old caps at most \(R\) and each new cap at least its corresponding old cap.” A family satisfying (36) does not by itself require a selected pair of parameters to be in increasing order.

Classification: optional clarification of an inherited hypothesis. The comparison and its consequences are correct under that hypothesis. An ordering-free interpretation would be false and is not endorsed by this review.

### O2. State the interpolation time domain explicitly

Location: the quantifier preceding (27), in Section 4.

The interpolants are defined on \([0,t_N]\). One could write \(0\leq u\leq t\leq S\leq t_N\leq0.1\), or explicitly require the queried times to lie in the interpolation domain. If \(S\) is only an upper horizon and exceeds \(t_N\), the estimate still applies to \(u,t\leq t_N\); no value outside the path's domain is defined by the construction.

Classification: optional domain clarification. It changes no constant or proof step.

No further mathematical lemma is required for the stated local results. The expanded certificates in this review, including an explicit \(C_{\rm ball}\), are verification details rather than requested repairs.

## Scope findings and nonclaims

1. **Deterministic initial box.** The finite theorem is conditional on (17). The Gaussian input calculation verifies a covariance and normalization; it does not claim that the finite random initialization satisfies (17) surely or with a specified probability. No initialization probability bound is needed for the conditional theorem.

2. **Short finite-time control.** The Euler result is uniform in width, caps, and mesh for the stated horizon \(t_N\leq0.1\). It does not give global continuation or global-in-time bounds.

3. **Covariance metric only.** The auxiliary Gaussian fields have the stated Gram covariance and increment metric. Their construction does not identify the original network's sources, an evolved Gaussian program, or a width limit. With random frozen features, Gaussianity is conditional unless a separate Gaussian process with expected covariance is specified.

4. **Local comparison only.** The state comparison requires a common finite width and inputs, both states in the designated ball, and finite old output caps. New caps do not enter its coefficient. The same-cut consequence gives local Lipschitz continuity, not a cap-uniform global Lipschitz estimate for an uncut population field.

5. **Actual old defects.** Different-cut comparison is always stated with exact old-state mismatches. Old-tail substitution requires the explicitly verified ordering property. The bounds do not replace old fields by an envelope, a new reference, or an uncut trajectory.

6. **No asserted tail removal.** The old fields depend on their cuts. Their cap-uniform \(L^2\) bounds alone do not establish the uniform tail estimates that a cap-removal argument might need. Equations (50)--(51) explicitly remain forced comparison estimates. The candidate does not claim defect vanishing.

7. **Supplied population operators.** The population extension assumes common bounded base operators and HS kernel increments. It constructs neither a Gaussian base operator nor a limit model. Its algebra is valid under those supplied data.

8. **Specified outer sample weights.** The numerical extension requires \(|b_c|\leq1\) and the common Lipschitz bound (53). Unbounded or differently placed loss factors are not included implicitly.

9. **No gradient-energy assumption.** The cut reference field is explicitly defined. The proof requires no assertion that clipping preserves a gradient structure, and uses no clipped energy identity.

These boundaries are appropriately separated from the claims proved. Within them, the candidate passes this isolated audit with no required mathematical repair.
