##### C.4.10.3. Continuum separation and finite target conditioning

Write \(u_\alpha=(\cos\alpha,\sin\alpha)\), with angles modulo \(2\pi\),
and let \(\rho(d\alpha)=d\alpha/(2\pi)\) be normalized arc measure on the
entire normalized circle. Physical inputs are \(x=\sqrt2u_\alpha\).
Fix \(D\ge0\) and the density class
\[
 {\cal P}_D=\{p\in C(S^1):\ \tfrac12\le p\le2,\quad
          \int p\,d\rho=1,\quad \operatorname{Lip}_{S^1}(p)\le D\},
 \tag{NSS1}
\]
where the Lipschitz constant uses shortest circular angle distance.
The uniform density belongs to this class, including when \(D=0\).

Use the fitted reference state \(\theta_\dagger=(w_\dagger,K_\dagger,
c_\dagger)\) and its actual action \(A_\dagger=A_0+K_\dagger\) from
C.4.5 and C.4.9. At that state abbreviate
\[
 \begin{aligned}
 H^1(u)&=\tanh(w_\dagger\cdot u),&
 Z^2(u)&=A_\dagger H^1(u),& H^2(u)&=\tanh Z^2(u),\\
 \delta(u)&=c_\dagger\operatorname{sech}^2Z^2(u),&
 Q(u)&=A_\dagger^*\delta(u).
 \end{aligned}
\]
\[
 g(u)=\bigl(u\operatorname{sech}^2(w_\dagger\cdot u)Q(u),
                \delta(u)\otimes H^1(u),\,H^2(u)\bigr),\qquad
 F_*(\alpha)=\langle c_\dagger,H^2(u_\alpha)\rangle.
 \tag{NSS2}
\]
Here \(g(u)\) is the scalar prediction gradient in the raw Hilbert
increment space \({\cal E}\). Its hidden subspace \({\cal E}_H\) contains
the first-row and middle Hilbert--Schmidt blocks; it excludes the readout.
Only the middle increment is Hilbert--Schmidt. The initialized action and
the adjoint in (NSS2) are the same retained Gaussian action and its true
Hilbert adjoint.

The reference bounds used below are
\[
 \|c_\dagger\|_2\le C:=\sqrt{10},\quad \|c_\dagger\|_\infty\le10,
 \quad\|A_\dagger\|_{\rm op}\le M:=2+\sqrt{10},\quad
 \|w_\dagger\|_2\le W:=\sqrt2+\sqrt{10}.
 \tag{NSS3}
\]
Consequently \(\sup_u\|g(u)\|\le L_0:=\sqrt{1+C^2(1+M^2)}<17\).
The fields \(H^1,H^2,g,F_*\) are odd in \(u\), whereas \(\delta,Q\)
are even. The reference fits \(F_*(0)=1,F_*(\pi/2)=-1\), and its input
Lipschitz constant is at most \(CMW<76\).

We first prove separation for signed input measures. This gives
injectivity of the constrained gradient even in its middle block.
Compactness then explains why a positive lower bound must be restricted
to the finite target spaces defined below.

###### Protected rows separate odd signed measures

Let \(\mathfrak F(z)=z/2+\sinh(2z)/4\), so
\(\mathfrak F'(z)=\cosh^2z\). The reference feature clock on
\(0\le s\le s_\dagger\le10\) satisfies
\[
 \mathfrak F(w_a(s))-\mathfrak F(g_a)=X_a(s),\qquad
 X_a(s)=\tfrac12y_a\int_0^s Q(e_a;v)\,dv,\qquad
 (y_1,y_2)=(1,-1),
 \tag{NSS4}
\]
with independent standard normal roots \(g_1,g_2\).
The reference source bound in C.4.9.A gives a finite constant \(C_Q\)
such that \(\sup_{s,a}\|Q(e_a;s)\|_{L^r}\le C_Q\sqrt r\) for every
\(r\ge2\). Equivalently this follows from C.4.6.S40--S44.
Define the nonnegative random variable
\[
 \begin{gathered}
 N_{\rm ref}=\tfrac12\sum_{a=1}^2\int_0^{s_\dagger}|Q(e_a;s)|\,ds,
 \qquad C_{\rm env}:=10C_Q,\\
 \|N_{\rm ref}\|_{L^r}\le C_{\rm env}\sqrt r,\qquad
 \sup_s|X_a(s)|\le N_{\rm ref}\quad\hbox{almost surely}.
 \end{gathered}
 \tag{NSS5}
\]
Minkowski proves the moment bound. The strong integral equations and
Fubini give the simultaneous clock bound. This uses integrals of the
active queries, without a random supremum over passive inputs.
Taking \(r=(z/(eC_{\rm env}))^2\ge2\) in Markov's inequality gives
\[
             \Pr\{N_{\rm ref}>z\}\le \exp[-z^2/(e^2C_{\rm env}^2)].
 \tag{NSS6}
\]
No independence of \(N_{\rm ref}\) and the first-row roots is asserted.

Fix a unit vector \(v\) with nonzero coordinates. For every sufficiently
large positive integer \(R_{\rm box}\), the Gaussian density gives
\[
 \Pr\{|g-R_{\rm box}v|_\infty\le1\}
       \ge(2/\pi)\exp[-(R_{\rm box}+\sqrt2)^2/2]
                     >\Pr\{N_{\rm ref}>R_{\rm box}^2\}.
 \tag{NSS7}
\]
Thus the box intersects \(\{N_{\rm ref}\le R_{\rm box}^2\}\) in positive probability.
On that intersection put \(c_v=\min_a|v_a|/2>0\); for large \(R_{\rm box}\),
\(|g_a|\ge c_vR_{\rm box}\). The minimum of \(\mathfrak F'\) on
\([g_a-1,g_a+1]\) is at least \(e^{2(|g_a|-1)}/4>R_{\rm box}^2\).
Monotonicity and (NSS4)--(NSS5) first place \(w_a(s)\) inside that
interval and then imply
\[
 \sup_{s\le s_\dagger}|w_a(s)-g_a|
                  \le4R_{\rm box}^2e^{-2(|g_a|-1)}\longrightarrow0.
 \tag{NSS8}
\]
For example, leaving the interval would change \(\mathfrak F\) by more
than \(R_{\rm box}^2\), contrary to (NSS5); the displayed bound then follows by
integrating its derivative between \(g_a\) and \(w_a(s)\).

**Signed-measure separation.** If a finite real signed Borel measure
\(\mu\) on the circle is odd under \(u\mapsto-u\), then
\[
             \int H^1(u)\,d\mu(u)=0\ \hbox{in }H_1
                    \quad\Longrightarrow\quad \mu=0 .
 \tag{NSS9}
\]
The integral is Bochner integrable, since \(H^1\) is continuous into
\(H_1=L^2(\Omega_1)\) and bounded by one in norm.

To prove (NSS9), intersect each positive-probability event in (NSS7)
with the full-measure sets where the clock identities and the asserted
zero integral hold. Choose one first-layer coordinate from each
intersection. Along these choices \(w_\dagger/R_{\rm box}\to v\).
If the two inputs perpendicular to \(v\) are not atoms of \(|\mu|\),
bounded convergence against the total variation gives
\[
 \int\operatorname{sign}(v\cdot u)\,d\mu(u)=0.
 \tag{NSS10}
\]
A finite measure has at most countably many atoms: for every positive
integer \(k\), only finitely many can have mass at least \(1/k\).
The excluded perpendicular directions and coordinate-axis directions
therefore form a null set of angles. Consequently
\(S(\beta)=\int\operatorname{sign}(\cos(\alpha-\beta))\,d\mu(\alpha)\)
vanishes for almost every \(\beta\).

For \(k(t)=\operatorname{sign}(\cos t)\), direct integration on the two
half circles gives
\[
 \widehat k(j):=\int k(t)e^{-ijt}\,d\rho(t)
       =\frac{2\sin(j\pi/2)}{\pi j}\ (j\ne0),\qquad \widehat k(0)=0.
 \tag{NSS11}
\]
Indeed its sine integrals vanish, and subtracting the complementary
half-circle cosine integral doubles the integral on
\((-\pi/2,\pi/2)\). Fubini applies to the bounded kernel and finite
variation measure, and gives
\(\widehat S(j)=\widehat k(j)\int e^{-ij\alpha}\,d\mu(\alpha)\).
Every odd Fourier coefficient of \(\mu\) is zero. Oddness already
annihilates each even coefficient, including its total mass.

Here is the required uniqueness step for finite measures. The Fejer kernels
\[
 {\cal K}_m(t)=\frac1{m+1}\left|\sum_{j=0}^m e^{ijt}\right|^2
 \tag{NSS12}
\]
are nonnegative and have \(\rho\)-integral one. Outside circular distance
\(\eta>0\) from zero they are at most
\(((m+1)\sin^2(\eta/2))^{-1}\), by the finite geometric sum.
Uniform continuity therefore makes \({\cal K}_m*f\to f\) uniformly
for every continuous circle function \(f\): split its convolution error
inside and outside that neighborhood, then decrease \(\eta\).
These convolutions are trigonometric polynomials, so all their integrals
against \(\mu\) vanish. Hence \(\int f\,d\mu=0\) for every continuous
\(f\). Continuous ramps converging to an arc indicator give zero mass
on every arc whose endpoints are not atoms of \(|\mu|\), by dominated
convergence. Choose a dense set of such endpoints. Finite unions of
these arcs form a generating algebra, and continuity under monotone
limits extends the zero measure to all Borel sets. This proves (NSS9).

###### The middle block and the anchor projection

The stronger weighted assertion is
\[
 \int\delta(u)\otimes H^1(u)\,d\mu(u)=0
      \ \hbox{in }{\cal S}_2(H_1,H_2),\quad \mu\ \hbox{finite and odd}
                         \quad\Longrightarrow\quad\mu=0.
 \tag{NSS13}
\]
The integrand is continuous in Hilbert--Schmidt norm: the first feature
is \(L^2\)-continuous, the bounded action preserves continuity, and
\[
 \|\delta(u)-\delta(v)\|_2
       \le2\|c_\dagger\|_\infty\|Z^2(u)-Z^2(v)\|_2 .
\]
Rank-one subtraction then gives the asserted continuity and
integrability against \(|\mu|\).

We make the representatives needed for (NSS13) explicit. Work with this
fixed finite measure \(|\mu|\), which is even when \(\mu\) is odd.
Approximate the continuous map \(u\mapsto Z^2(u)\in H_2\) uniformly
in \(L^2\) by simple input fields. A subsequence converges in the product
measure \(|\mu|\otimes\mathbb P_2\), giving a jointly measurable
representative finite almost everywhere and representing \(Z^2(u)\)
for \(|\mu|\)-almost every input. Construct on one semicircle and extend
by oddness; this also retains the separately chosen values at any named
atoms and their antipodes. Applying the gate with the fixed representative
of \(c_\dagger\) makes \(\delta(u,z)\) even, jointly measurable, and
bounded by 10. No exceptional set uniform over all measures is required.

The Hilbert--Schmidt norm of a finite sum of tensors equals the \(L^2\)
norm of its kernel on \(\Omega_2\times\Omega_1\): expansion gives
\(\sum_{i,j}\langle a_i,a_j\rangle_2\langle b_i,b_j\rangle_1\)
on both sides for \(\sum_i a_i\otimes b_i\).
Bochner simple approximations and completion therefore identify the
kernel of the integral in (NSS13) with
\(\int\delta(u,z)H^1(u,\omega_1)\,d\mu(u)\).
Boundedness by \(10|\mu|(S^1)\) justifies Fubini. The zero operator
thus gives a zero first-layer integral for almost every \(z\in\Omega_2\).

The readout is nonzero since
\(\langle c_\dagger,H^2(e_1)\rangle=1\). Choose \(z\) outside all the
preceding null sets with \(c_\dagger(z)\ne0\).
The measure \(d\mu_z(u)=\delta(u,z)d\mu(u)\) is finite and odd.
By (NSS9) it is zero. For \(|\mu|\)-almost every \(u\), its multiplier
\(c_\dagger(z)\operatorname{sech}^2Z^2(u,z)\) is nonzero, because its
preactivation is finite. The identity
\(|\mu_z|=|\delta(\cdot,z)|\,|\mu|\) then forces \(|\mu|=0\).
This proves (NSS13), without assuming injectivity of \(A_\dagger\).

Let \(G:\mathbb R^2\to{\cal E}\) have columns \(g(e_1),g(e_2)\).
If their middle blocks had a nontrivial linear relation, (NSS13) applied
to \(\frac12\sum_a\beta_a(\delta_{e_a}-\delta_{-e_a})\) would make
all its coefficients zero. Thus
\[
 M_\dagger=G^*G>0,\qquad
 \Pi_\dagger=I-GM_\dagger^{-1}G^*,\qquad d(u)=\Pi_\dagger g(u).
 \tag{NSS14}
\]
These are the same anchor Gram and orthogonal projection as in C.4.9.
Write \(d_H(u)\) for the first-row/middle block of \(d(u)\).

For \(p\in{\cal P}_D\), let \({\cal H}_p\) be the real closed odd subspace
of \(L^2(p\rho)\), with norm \(\|\cdot\|_p\). Closure follows from
equivalence with the \(L^2(\rho)\) norm. Its norm and all force integrals
below are unchanged on replacing \(p\) by
\(p_s(u)=(p(u)+p(-u))/2\): products of two odd functions are even.
Define
\[
 T_pa=\int a(u)d(u)p(u)d\rho(u),\qquad
 T_{H,p}a=\int a(u)d_H(u)p(u)d\rho(u).
 \tag{NSS15}
\]
Both operators have norm at most \(L_0\), by Cauchy--Schwarz.
They are injective, even after retaining only their middle block.
Indeed set \(U=\int a(u)g(u)p(u)d\rho(u)\) and
\(\beta=M_\dagger^{-1}G^*U\). A zero middle block gives (NSS13) for
\[
 d\mu=a(u)p_s(u)d\rho(u)
            -\tfrac12\sum_{b=1}^2\beta_b
                              (\delta_{e_b}-\delta_{-e_b}).
 \tag{NSS16}
\]
This is a finite odd measure since \(a\in{\cal H}_p\subset L^1(p\rho)\).
Its absolutely continuous and atomic parts are mutually singular.
The conclusion \(\mu=0\), together with \(p_s\ge1/2\), gives \(a=0\).

###### Compact operators and uniform finite target conditioning

The endpoint map \(u\mapsto g(u)\) is raw-norm continuous.
To check its only unbounded gate product, subtract \(Q(u)-Q(v)\) first.
The remaining bounded multiplier difference converges against the fixed
\(Q(v)\in L^2\): truncate \(|Q(v)|\) at a fixed level, use bounded
convergence on the truncated part, then remove its \(L^2\) tail.
Forward fields, upper gates, the actual adjoint, and the rank-one block
are continuous by their factorwise bounds. Hence \(d,d_H\) are continuous.
Finite input partitions approximate them uniformly by finitely valued
kernels. Their induced finite-rank operators approximate \(T_p,T_{H,p}\)
in operator norm, with error at most the kernel's uniform error.
Thus these operators are compact.

There is no positive coercivity constant on all of \({\cal H}_p\).
This space is infinite-dimensional since positive density preserves
linear independence of all odd trigonometric modes. For an orthonormal
sequence \(a_j\), every finite-rank operator sends \(a_j\) to zero in
norm, by Bessel's inequality applied to its finitely many linear
functionals. Finite-rank approximation then gives
\(\|T_pa_j\|\to0\) and \(\|T_{H,p}a_j\|\to0\).
The finite-dimensional restriction below supplies the needed lower bounds.

Put \(q_0(\alpha)=\cos^3\alpha-\sin^3\alpha\) and
\(h(\alpha)=\sin^2(2\alpha)\). For each integer \(N\ge0\), define
\[
 E_N=\operatorname{span}\{F_*-q_0,\,
 h\cos((2k+1)\alpha),\,h\sin((2k+1)\alpha):0\le k\le N\}.
 \tag{NSS17}
\]
All generators are odd Lipschitz functions vanishing at the anchors.
The space is nonzero because \(h\cos\alpha\) is nonzero. It contains
\(F_*-q_N\) for every target whose prescribed series \(v\) has coefficient
indices at most \(N\). The actual harmonic degree of that target is at
most \(2N+5\); \(E_N\) itself also retains the possibly nonpolynomial
reference generator \(F_*-q_0\) exactly.

Let \(d_N=\dim E_N\). Delete any exact dependencies using the
\(L^2(\rho)\) Gram of the listed generators, and orthonormalize the
remaining functions to obtain \(b_1,\ldots,b_{d_N}\).
This chooses a fixed basis independent of \(p\) and of target coefficients.
For \(p\in{\cal P}_D\), define real \(d_N\times d_N\) matrices
\[
 \begin{aligned}
 C_N(p)_{ij}&=\int b_i b_jp\,d\rho,\\
 A_N(p)_{ij}&=\langle T_pb_i,T_pb_j\rangle_{\cal E},\\
 A_{H,N}(p)_{ij}&=\langle T_{H,p}b_i,T_{H,p}b_j\rangle_{{\cal E}_H}.
 \end{aligned}
 \tag{NSS18}
\]
One has \(\frac12I\le C_N(p)\le2I\), and both other matrices are
positive definite by (NSS15)--(NSS16).
Their uniform generalized eigenvalue bounds are
\[
 \lambda_N=\min_{\substack{p\in{\cal P}_D\\z^TC_N(p)z=1}}
                          z^TA_N(p)z,\qquad
 \lambda_{H,N}=\min_{\substack{p\in{\cal P}_D\\z^TC_N(p)z=1}}
                          z^TA_{H,N}(p)z .
 \tag{NSS19}
\]
Both minima exist and satisfy \(0<\lambda_{H,N}\le\lambda_N\le L_0^2\).
Here are the compactness details establishing strict positivity uniformly.
Bounded densities have a subsequence converging on a fixed countable
dense set, by diagonal extraction. The common Lipschitz bound makes that
subsequence uniformly Cauchy, using a finite sufficiently fine input net.
Its uniform limit preserves the bounds, integral and Lipschitz constant.
Thus \({\cal P}_D\) is compact. All entries in (NSS18) are continuous
in the uniform density norm, by bounded kernels and their Bochner integrals.
The constraint in (NSS19) gives \(|z|\le\sqrt2\); it is closed and
prevents a limiting vector from being zero. Its feasible set is therefore
compact. A zero attained minimum would contradict injectivity of \(T_p\)
or \(T_{H,p}\) on the nonzero function \(\sum_i z_i b_i\).
The upper and ordering bounds follow from (NSS15) and the hidden
coordinate projection being a contraction.

In particular, for every \(p\in{\cal P}_D\) and \(a\in E_N\),
\[
 \|T_pa\|^2\ge\lambda_N\|a\|_p^2,\qquad
 \|T_{H,p}a\|^2\ge\lambda_{H,N}\|a\|_p^2 .
 \tag{NSS20}
\]
These constants depend only on \(N,D\) and the specified reference.
They are defined by finite matrices and a compact density minimization;
no numerical value or positive bound uniform as \(N\to\infty\) is asserted.
The reference residual is included exactly in \(E_N\); subsequent
approximation errors concern the prescribed target tail and the movement
of the actual nonlinear state.
