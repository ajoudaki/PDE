# A rigorous joint mean-field/gradient-flow limit for the two-hidden-layer arctangent network

## Theorem

For every width \(n\), consider the one-sample network
\[
A_i=W_i^{(1)},\qquad H_i=\phi(A_i),\qquad
S_j=\sum_{i=1}^nB_{ji}H_i,
\]
\[
G_j=\phi(S_j),\qquad f_n=\sum_{j=1}^nc_jG_j,
\qquad L_n=(f_n-1)^2,                              \tag{T1}
\]
where \(\phi(x)=\arctan x\).  Initialize all variables independently by
\[
A_i(0)\sim N(0,1),\qquad B_{ji}(0)\sim N(0,n^{-1}),
\qquad c_j(0)\sim N(0,n^{-4}).                     \tag{T2}
\]
Use exact full-batch GD with base step and raw layer multipliers
\[
\eta_n=n^{-2},\qquad
(\lambda_A,\lambda_B,\lambda_c)=(n,1,n^{-1}),       \tag{T3}
\]
Linearly interpolate the three parameter arrays on the clock
\(t=k\eta_n\), and at intermediate times recompute \(H,S,G,f,L\) from
those interpolated parameters.

Then, along the full sequence \(n\to\infty\), the exact GD processes converge in probability, uniformly on every compact time interval, to a unique autonomous and restartable action-law gradient flow.  The empirical path laws of \(A\) and \(S\) converge in \(W_2(C([0,T]))\).  Outputs, losses, all three scaled kernel blocks, and both hidden velocity energies converge in the modes stated below.

There exists \(T_*>0\) such that, for every \(0<T\le T_*\):

1. both hidden marginal laws have finite strictly positive variance;
2. both hidden layers have finite positive integrated mean-square velocity and nonzero mean-square displacement;
3. all three parameter blocks have finite positive integrated scaled kernel;
4. the affine-regression residual of \(\arctan\) is positive in both hidden layers;
5. \(K(t)\) is nonconstant and \(L(T)<L(0)=1\).

In particular, this is a genuinely nonlinear feature-learning limit, not a frozen-feature or affine limit.  Moreover
\[
\eta_n\lambda_A=n^{-1},\qquad
\eta_n\lambda_B=n^{-2},\qquad
\eta_n\lambda_c=n^{-3},                            \tag{T4}
\]
so every raw parameter step tends to zero.

The proof has five bridges: exact normalization; a dimension-free regularized flow; fixed-mesh width identification by a finite population-oracle tensor program; a same-width Euler sandwich yielding the continuous action law; and a direct comparison of exact GD with that flow.  The final section proves strict activity and nonlinearity.

## 1. Exact finite-width equations

Put
\[
C=nc,\qquad \langle u,v\rangle_n=n^{-1}u^\top v,
\qquad (u\otimes_n v)z=u\langle v,z\rangle_n,
\]
and write
\[
q(x)=\phi'(x)=\frac1{1+x^2},\qquad
D=C\odot q(S),\qquad P=B^\top D,qquad e=f_n-1.     \tag{1.1}
\]
Then \(f_n=\langle C,G\rangle_n\).  Direct differentiation gives
\[
\frac{\partial f_n}{\partial A_i}=\frac1nq(A_i)P_i,
\qquad
\frac{\partial f_n}{\partial B_{ji}}=\frac1nD_jH_i,
\qquad
\frac{\partial f_n}{\partial c_j}=G_j.             \tag{1.2}
\]
Multiplying the loss gradients by (T3) proves that the associated finite-width gradient flow is exactly
\[
\dot A=-2e\,q(A)\odot P,qquad
\dot B=-2e\,D\otimes_nH,qquad
\dot C=-2e\,G.                                     \tag{1.3}
\]
The three scaled tangent-kernel blocks are
\[
K^A_n=\|q(A)P\|_n^2,qquad
K^B_n=\|H\|_n^2\|D\|_n^2,qquad
K^C_n=\|G\|_n^2,                                  \tag{1.4}
\]
where \(\|v\|_n^2=\langle v,v\rangle_n\).  Thus, for \(K_n=K_n^A+K_n^B+K_n^C\),
\[
\dot f_n=-2eK_n,qquad \dot L_n=-4e^2K_n.          \tag{1.5}
\]
In particular, \(|e(t)|\le |e(0)|\) along the flow.

Differentiating \(S=BH\) will also be useful:
\[
\dot S=-2e\left\{\|H\|_n^2D+B[q(A)^2\odot P]\right\}. \tag{1.6}
\]

## 2. The regularizing coordinate and dimension-free flow estimates

Define
\[
F(a)=a+\frac{a^3}{3},\qquad X=F(A),\qquad J=F^{-1},
\qquad h(x)=\arctan J(x).                           \tag{2.1}
\]
Since \(F'(a)=q(a)^{-1}\), equation (1.3) becomes
\[
\boxed{
\begin{aligned}
A&=J(X),& H&=h(X),& S&=BH,\\
G&=\arctan S,&D&=Cq(S),&e&=\langle C,G\rangle_n-1,\\
\dot X&=-2eB^\top D,&
\dot B&=-2eD\otimes_nH,&
\dot C&=-2eG.
\end{aligned}}                                    \tag{2.2}
\]
This is exact, not a linearization.  Also
\[
J'(x)=q(J(x)),\qquad h'(x)=q(J(x))^2,               \tag{2.3}
\]
so \(J,h,q\circ J\) are globally Lipschitz; \(|H|,|G|\le a_0:=\pi/2\).

For two states define
\[
d_n(\theta,\widetilde\theta)
=\|X-\widetilde X\|_n+
 \|B-\widetilde B\|_{\mathrm{op}}+
 \|C-\widetilde C\|_n.                            \tag{2.4}
\]
On a set on which \(\|B\|_{\mathrm{op}},\|\widetilde B\|_{\mathrm{op}}\le M_B\) and \(\|C\|_\infty,\|\widetilde C\|_\infty\le M_C\), the vector field in (2.2) is Lipschitz in (2.4), with a constant independent of \(n\).  Indeed,
\[
\|H-\widetilde H\|_n\le\|X-\widetilde X\|_n,     \tag{2.5}
\]
\[
\|S-\widetilde S\|_n
\le a_0\|B-\widetilde B\|_{\mathrm{op}}
  +M_B\|X-\widetilde X\|_n,                       \tag{2.6}
\]
and
\[
\|D-\widetilde D\|_n
\le \|C-\widetilde C\|_n
 +M_C\operatorname{Lip}(q)\|S-\widetilde S\|_n.  \tag{2.7}
\]
Furthermore
\[
|e-\widetilde e|
\le a_0\|C-\widetilde C\|_n
 +\|\widetilde C\|_n\|S-\widetilde S\|_n,        \tag{2.8}
\]
\[
\|B^\top D-\widetilde B^\top\widetilde D\|_n
\le \|B-\widetilde B\|_{\mathrm{op}}\|D\|_n
 +M_B\|D-\widetilde D\|_n.                        \tag{2.9}
\]
Finally \(\|u\otimes_nv\|_{\mathrm{op}}=\|u\|_n\|v\|_n\).  Substitution of (2.5)--(2.9) into (2.2) gives
\[
\|V_n(\theta)-V_n(\widetilde\theta)\|_{d_n}
\le L(M_B,M_C,\|C\|_n,\|\widetilde C\|_n)d_n(\theta,\widetilde\theta). \tag{2.10}
\]

The required bounded set is invariant on each compact interval, uniformly in width on a high-probability initialization event.  From (1.5), \(|e(t)|\le |e(0)|\), and hence
\[
\|C(t)\|_\infty\le\|C(0)\|_\infty+2a_0|e(0)|t.  \tag{2.11}
\]
Equation (2.2) then bounds \(\|B(t)\|_{\mathrm{op}}\), followed by \(\|X(t)\|_n\).  Explicitly,
\[
\|\dot B\|_{\mathrm{op}}
\le2a_0|e(0)|\|C\|_n,
\quad
\|\dot X\|_n
\le2|e(0)|\|B\|_{\mathrm{op}}\|C\|_n.             \tag{2.12}
\]
Now \(\|C_n(0)\|_n=O_{\mathbb P}(n^{-1})\), \(\|C_n(0)\|_\infty=o_{\mathbb P}(1)\), and \(\|X_n(0)\|_n=O_{\mathbb P}(1)\).  A self-contained \(1/4\)-net argument gives a constant \(M_0\) with
\[
\mathbb P(\|B_n(0)\|_{\mathrm{op}}>M_0)\le2e^{-cn}. \tag{2.13}
\]
Indeed, two unit-sphere \(1/4\)-nets have at most \(9^n\) points each,
\(\|B\|_{\mathrm{op}}\le2\max_{u,v}|v^\top Bu|\), and every fixed bilinear form is \(N(0,n^{-1})\); a union bound proves (2.13) for any sufficiently large fixed \(M_0\).

Consequently (2.2) has a unique global finite-width solution.  On every \([0,T]\), explicit Euler with mesh \(\delta\), polygonally interpolated, satisfies
\[
\sup_{t\le T}d_n(\theta_n^\delta(t),\theta_n(t))
\le C_T\delta                                             \tag{2.14}
\]
on an event of probability tending to one.  To verify (2.14), the local defect is at most \(\frac12L_TM_T\delta^2\), where \(M_T\) bounds the vector field; the recurrence
\(r_{k+1}\le(1+L_T\delta)r_k+\frac12L_TM_T\delta^2\) and discrete Gronwall give the assertion.  A stopped bootstrap keeps the Euler iterates in the slightly enlarged bounded set.

## 3. The only nonclassical external theorem

We use the following exact specialization of Greg Yang, *Tensor Programs III: Neural Matrix Laws*, arXiv:2009.10685v3, Setup 2.2 and Theorem 2.10.

**Fixed-program reused-Gaussian theorem.**  Fix a finite program whose
initial matrix has iid \(N(0,1/n)\) entries, independent of all initial
vectors, whose initial vector coordinates are iid copies of a fixed jointly
Gaussian vector (the covariance may be singular), and whose instructions
are coordinatewise polynomially bounded maps and finitely many applications
of \(B_0\) and \(B_0^\top\).  For every fixed finite list of program vectors
and every polynomially bounded test \(\psi\),
\[
\frac1n\sum_{i=1}^n\psi(Z_{n,i}^1,\ldots,Z_{n,i}^r)
\longrightarrow
\mathbb E\psi(Z^1,\ldots,Z^r)\quad\text{almost surely}. \tag{3.1}
\]
The limiting variables retain every reused-transpose response term; a transpose call is not replaced by an independent multiplication.

The full primary proof was checked.  Its Gaussian-conditioning step conditions the matrix simultaneously on all preceding \(BY\) and \(B^\top V\) calls.  A simultaneous induction proves empirical-moment convergence and constructs a full-support core set.  At singular covariance, rank stability and zero stability show that a zero limiting innovation is eventually an exact finite-width linear dependence; a positive innovation is a high-rank projected Gaussian for which the proof establishes the required strong law.  This closes the singular-covariance case without assuming rank stability.  The theorem is only for one fixed finite parameterless program.

We do **not** use the paper's Appendix A.1 conditional almost-sure strengthening or Appendix A.2 mean-convergence proof.  Independent inspection found that the former is false for arbitrary varying conditioning sigma-fields and that the printed proof of the latter omits a uniform-integrability step.  Neither is needed here.  Nor do we import the paper's operator-norm citation; (2.13) was proved directly.

## 4. One canonical action space and its autonomous flow

The continuum state must live on fixed spaces before a time integral or a
restart map can be discussed.  We construct those spaces once, from the
initial Gaussian action, rather than constructing unrelated GNS spaces at
individual times.

### 4.1  Simultaneous cyclic realization of the initial action

Use two sorts, right and left.  Let \(\mathscr P_R,\mathscr P_L\) be the
countable formal probe grammar generated by the right Gaussian coordinate
\(A_0\), the left zero coordinate, rational linear combinations, formal
applications of \({\bf B}_0,{\bf B}_0^*\), and coordinate maps from the
following countable library:

* the exact maps \(F,J,h,\arctan,q\),
  \((c,s)\mapsto c q(s)\), and
  \((a,p)\mapsto q(a)^rp\), \(r=1,2\);
* clipping at every positive integer level; and
* a countable algebra of bounded Lipschitz cylinder functions with rational
  data which generates every finite-dimensional Borel sigma-field.

The grammar is closed again after every new coordinate map or matrix call.
It is countable, and every finite part is one fixed finite \(\mathrm{NETSOR}^T\)
program.  Apply (3.1) to every finite part and intersect the resulting
countably many probability-one events.  The limiting same-side finite joint
laws are consistent.  Kolmogorov extension therefore gives probability
spaces \((\Omega_R,\mu_R)\), \((\Omega_L,\mu_L)\) carrying all formal
right and left coordinates.  Because the bounded Lipschitz cylinder algebra
is present, their spans are dense in
\[
\mathcal H_R=L^2(\Omega_R,\mu_R),\qquad
\mathcal H_L=L^2(\Omega_L,\mu_L).                  \tag{4.1}
\]
Rational coefficients make the grammar countable; multiplication by an
arbitrary fixed real is obtained in the \(L^2\) closure by rational
approximation.  A particular finite tensor program may equivalently use
that real directly as part of its fixed coordinate map.

For a formal right probe \(v\), define \(B_0v\) to be the coordinate named
by \({\bf B}_0v\), and similarly on the left.  On the product coupling of
all widths, (2.13) and Borel--Cantelli imply
\(\|B_{0,n}\|_{\rm op}\le M_0\) eventually almost surely.  Passing to the
limiting squared norms gives
\[
\|B_0v\|_{\mathcal H_L}\le M_0\|v\|_{\mathcal H_R}. \tag{4.2}
\]
Thus zero-norm relations are respected and \(B_0\) extends uniquely to all
of \(\mathcal H_R\).  Passing to the limit in
\(\langle u,B_{0,n}v\rangle_n=\langle B_{0,n}^\top u,v\rangle_n\)
proves that the named transpose action is its Hilbert adjoint.  The
ZHat/ZDot rule in (3.1) is what determines these actions; in particular the
adjoint is not an independent Gaussian operator.

Put \(X_0=F(A_0)\in\mathcal H_R\), \(C_0=0\in\mathcal H_L\).  On the fixed
spaces (4.1), for a triple \(\Theta=(X,B,C)\), define
\[
\begin{aligned}
A&=J(X),&H&=h(X),&S&=BH,\\
G&=\arctan S,&D&=Cq(S),&e&=\langle C,G\rangle_L-1,
\end{aligned}                                      \tag{4.3}
\]
and
\[
\dot X=-2eB^*D,\qquad
\dot B=-2eD\otimes H,\qquad
\dot C=-2eG.                                      \tag{4.4}
\]
Here \((D\otimes H)v=D\langle H,v\rangle_R\).  Lipschitz Nemytskii
maps act on \(L^2\); the product \(Cq(S)\) is in \(L^2\) whenever
\(C\in L^\infty\); and \(D\otimes H\) is a bounded operator of norm
\(\|D\|_2\|H\|_2\).  Thus every term in (4.4) is defined.

### 4.2  Existence, uniqueness, and restartability

We give the functional-analytic existence argument explicitly.  On a path
interval \([0,\tau]\), use the complete metric
\[
\sup_{t\le\tau}\{\|X-\widetilde X\|_2+
\|B-\widetilde B\|_{\rm op}+\|C-\widetilde C\|_2\} \tag{4.5}
\]
on the closed class having prescribed bounds on \(\|B\|_{\rm op}\) and
\(\|C\|_\infty\).  This class is complete: an \(L^2\) limit of functions
bounded by the same \(L^\infty\) constant has a representative with that
bound.  The integral map associated with (4.4) preserves the class for
small \(\tau\), because \(|G|\le a_0\), and (2.5)--(2.10), with ordinary
Hilbert norms, show that it has Lipschitz constant \(L\tau\).  Taking
\(L\tau<1\) proves existence and uniqueness by the contraction argument.

The Hilbert-space chain rule and the adjoint identity give
\[
\dot e=-2eK,\qquad
K=\|q(A)B^*D\|_2^2+
  \|H\|_2^2\|D\|_2^2+\|G\|_2^2\ge0.              \tag{4.6}
\]
Hence \(|e(t)|\le|e(0)|\).  Exactly as in (2.11)--(2.12),
\[
\|C(t)\|_\infty\le\|C_0\|_\infty+2a_0|e(0)|t,\quad
\|\dot B\|_{\rm op}\le2a_0|e(0)|\|C\|_2,
\]
\[
\|\dot X\|_2\le2|e(0)|\|B\|_{\rm op}\|C\|_2. \tag{4.7}
\]
These bounds prevent finite-time blow-up and continue the solution for all
finite times.  They also put every coordinate product used above in the
closure of the formal cylinder grammar (approximate first by uniformly
bounded cylinder functions and then use dominated \(L^2\) convergence).

Equation (4.4) is autonomous.  At any current state
\(\Theta=(X,B,C)\), root the saturated typed grammar of Section 4.1 at
\(X,C,B,B^*\), and let
\(\mathcal K_R(\Theta),\mathcal K_L(\Theta)\) be the closures of its
rational probe spans.  These are the **current cyclic spaces**.  By closure
of the grammar, \(B\mathcal K_R\subseteq\mathcal K_L\),
\(B^*\mathcal K_L\subseteq\mathcal K_R\), and every coordinate map in
(4.3) preserves the appropriate cyclic closure.  Picard iteration of
(4.4), started at \(\Theta\), uses only those operations; hence its future
trajectory remains on these cyclic spaces.  The action of \(B\) outside
them is therefore neither observed nor retained by the law-level state.

If two complete current-rooted action laws agree, mapping each named probe
to its counterpart is an isometry with dense range in the two cyclic
spaces.  It extends to surjective unitaries
\(U_R:\mathcal K_R\to\widetilde{\mathcal K}_R\) and
\(U_L:\mathcal K_L\to\widetilde{\mathcal K}_L\).  Saturation gives
\(U_LB=\widetilde B U_R\), \(U_RB^*=\widetilde B^*U_L\), and commutation
with all coordinate maps.  It also sends \(D\otimes H\) to
\((U_LD)\otimes(U_RH)\).  Thus (4.4) is equivariant on precisely the
future-relevant spaces, and uniqueness descends to action-law equivalence
classes without any unproved density claim in the larger initial
realization.  Restarting the same integral equation at time \(s\) proves
\[
\Phi_t(\Phi_s[\Theta_0])=\Phi_{t+s}[\Theta_0].     \tag{4.8}
\]
No absolute-time tags, initialization array, or history belong to the
current state.

## 5. Fixed meshes, the population oracle, and the joint limit

Let \(\Theta_k^\delta=(x_k,b_k,c_k)\) be explicit Euler applied to (4.4)
on the canonical spaces, and use lower-case letters for all its derived
nodes.  For \(N=\lceil T/\delta\rceil<\infty\),
\[
b_k=B_0-2\delta\sum_{r<k}e_r d_r\otimes h_r.       \tag{5.1}
\]
Consequently
\[
s_k=B_0h_k-2\delta\sum_{r<k}e_rd_r
                 \langle h_r,h_k\rangle_R,
\quad
p_k=B_0^*d_k-2\delta\sum_{r<k}e_rh_r
                 \langle d_r,d_k\rangle_L.        \tag{5.2}
\]

### 5.1  A genuinely fixed finite tensor program

Define finite-width oracle vectors using the deterministic scalars in
(5.2): \(\bar X_{n,0}=F(A_{n,0})\), \(\bar C_{n,0}=0\), and
\[
\begin{aligned}
\bar H_{n,k}&=h(\bar X_{n,k}),\\
\bar S_{n,k}&=B_{0,n}\bar H_{n,k}
-2\delta\sum_{r<k}e_r\bar D_{n,r}
                    \langle h_r,h_k\rangle_R,\\
\bar G_{n,k}&=\arctan\bar S_{n,k},\qquad
\bar D_{n,k}=\bar C_{n,k}q(\bar S_{n,k}),\\
\bar P_{n,k}&=B_{0,n}^\top\bar D_{n,k}
-2\delta\sum_{r<k}e_r\bar H_{n,r}
                    \langle d_r,d_k\rangle_L,\\
\bar X_{n,k+1}&=\bar X_{n,k}-2\delta e_k\bar P_{n,k},\\
\bar C_{n,k+1}&=\bar C_{n,k}-2\delta e_k\bar G_{n,k}.
\end{aligned}                                      \tag{5.3}
\]
All coefficients in (5.3) are deterministic and independent of \(n\), and
there are only finitely many \(B_{0,n},B_{0,n}^\top\) calls.  It is therefore
one fixed parameterless program: the language permits arbitrary fixed real
coordinate maps, so the possibly irrational numbers \(e_r\) and the
canonical Grams cause no parameter line or empirical feedback.  Induction
on \(k\), using the canonical
construction of Section 4 and (5.2), identifies its symbolic limiting
variables with the canonical Euler nodes.  Theorem (3.1) then gives, almost
surely, every finite joint law and empirical moment needed below.

Define the finite oracle rank memory
\[
\bar B_{n,k}=B_{0,n}-2\delta\sum_{r<k}e_r
                   \bar D_{n,r}\otimes_n\bar H_{n,r}. \tag{5.4}
\]
The program nodes in (5.3) are not asserted to be exact actions of (5.4).
Their two exact residuals are
\[
\begin{aligned}
\bar B_{n,k}\bar H_{n,k}-\bar S_{n,k}
&=-2\delta\sum_{r<k}e_r\bar D_{n,r}
 \bigl(\langle\bar H_{n,r},\bar H_{n,k}\rangle_n
       -\langle h_r,h_k\rangle_R\bigr),\\
\bar B_{n,k}^*\bar D_{n,k}-\bar P_{n,k}
&=-2\delta\sum_{r<k}e_r\bar H_{n,r}
 \bigl(\langle\bar D_{n,r},\bar D_{n,k}\rangle_n
       -\langle d_r,d_k\rangle_L\bigr).
\end{aligned}                                      \tag{5.5}
\]
This is the point at which empirical Gram errors enter; they are not
silently replaced by expectations.

Let \(\mathscr M_N\) be the finite list consisting of the output moment,
all \(H\)- and \(D\)-Grams in (5.5), and the squared norms of every oracle
vector in (5.3).  Set
\[
\zeta_n=\max_{M\in\mathscr M_N}|M_n-M|.            \tag{5.6}
\]
Theorem (3.1) gives \(\zeta_n\to0\) almost surely.  In particular all
oracle vector norms are bounded on that event for large \(n\), and (5.5)
is bounded by \(C_{N,\delta}\zeta_n\) in normalized \(L^2\).

### 5.2  Coupling to the actual scalar-feedback Euler scheme

Use the same \(A_{n,0},B_{0,n}\) for the actual and oracle schemes.  Let
\(B_{n,k}\) be the actual learned matrix, and define
\[
E_{n,k}=\|X_{n,k}-\bar X_{n,k}\|_n+
        \|C_{n,k}-\bar C_{n,k}\|_n+
        \|B_{n,k}-\bar B_{n,k}\|_{\rm op}.        \tag{5.7}
\]
On the common bounded event, (2.5)--(2.9) and the residuals (5.5) give,
node by node,
\[
\begin{aligned}
&\|H_{n,k}-\bar H_{n,k}\|_n+
 \|S_{n,k}-\bar S_{n,k}\|_n+
 \|G_{n,k}-\bar G_{n,k}\|_n\\
&\quad+\|D_{n,k}-\bar D_{n,k}\|_n+
 \|P_{n,k}-\bar P_{n,k}\|_n+|e_{n,k}-e_k|
 \le C_{N,\delta}(E_{n,k}+\zeta_n).               \tag{5.8}
\end{aligned}
\]
For clarity, the scalar step in (5.8) is
\[
|e_{n,k}-e_k|\le
|\langle C_{n,k},G_{n,k}\rangle_n-
  \langle\bar C_{n,k},\bar G_{n,k}\rangle_n|
+|\langle\bar C_{n,k},\bar G_{n,k}\rangle_n-
  \langle c_k,g_k\rangle_L|,
\]
and the second term is one of (5.6).  The first is bounded by the preceding
vector differences.  Subtracting the three Euler updates and using
\(\|u\otimes v-u'\otimes v'\|_{\rm op}\le
\|u-u'\|_2\|v\|_2+\|u'\|_2\|v-v'\|_2\) yields
\[
E_{n,k+1}\le(1+C_{N,\delta}\delta)E_{n,k}
             +C_{N,\delta}\delta\zeta_n.          \tag{5.9}
\]
Here \(E_{n,0}=\|C_{n,0}\|_n=O_{\mathbb P}(n^{-1})\).  Since \(N\) is
fixed, discrete Gronwall proves
\[
\max_{k\le N}E_{n,k}\longrightarrow0
\quad\text{in probability}.                       \tag{5.10}
\]
This proves fixed-mesh identification of the actual Euler network.  It
does not assert, or require, a tensor theorem with \(N=N_n\to\infty\).

### 5.3  Removing the mesh

The estimates of Section 2 hold verbatim on the canonical spaces.  Thus
canonical Euler and the unique solution of (4.4) satisfy
\[
\sup_{t\le T}\{\|x^\delta-X\|_2+
\|b^\delta-B\|_{\rm op}+\|c^\delta-C\|_2\}
\le C_T\delta.                                     \tag{5.11}
\]
The finite-width Euler estimate is (2.14).  We now define the topology and
prove the assertion for arbitrary nested operator probes.

Let \(\mathscr L_R,\mathscr L_L\) be the countable current-rooted typed
language with roots \(x,c\), rational linear combinations, current
\({\bf b},{\bf b}^*\) calls, the exact globally Lipschitz or bounded maps
\(J,h,\arctan,q\), the controlled map \((c,s)\mapsto cq(s)\), every
rational bounded-Lipschitz cylinder map, and
\[
(a,p)\mapsto q(a)^r\rho_M(p),\qquad r=1,2,\quad M\in\mathbb N. \tag{5.12}
\]
It is closed after every operation.  An \(R\)-**record** is a finite list
of same-side probe tuples from this language together with their
inner-products.  Its distance is the sum of the \(W_2\) distances of the
tuple laws and the absolute differences of the listed inner-products.
Choose an enumeration \((R_j)\) and define
\[
d_{\rm act}(\Theta,\widetilde\Theta)
=\sum_{j\ge1}2^{-j}\{1\wedge d_{R_j}(\Theta,\widetilde\Theta)\}. \tag{5.13}
\]
We work in the category carrying the common operator and \(C\)-supremum
bounds proved in Sections 2 and 4; finite records alone would not encode
such a bound.

Here is the required structural estimate.  If two states live on the same
finite normalized spaces, or on the same canonical spaces, and
\[
d_0=\|x-\widetilde x\|_2+
    \|b-\widetilde b\|_{\rm op}+\|c-\widetilde c\|_2,
\]
then for every fixed probe \(v\) in (5.12)
\[
\|v(\Theta)-v(\widetilde\Theta)\|_2\le C_vd_0.     \tag{5.14}
\]
This follows by induction on the syntax tree.  The coordinate-map steps
use their Lipschitz bounds; \(cq(s)\) uses the common \(C\)-supremum bound;
and the operator step is exactly
\[
\|bv-\widetilde b\,\widetilde v\|_2
\le\|b-\widetilde b\|_{\rm op}\|v\|_2+
   \|\widetilde b\|_{\rm op}\|v-\widetilde v\|_2, \tag{5.15}
\]
with the identical adjoint estimate.  Rational combinations and
inner-products follow from the triangle and Cauchy--Schwarz inequalities.
This proves (5.14) for arbitrarily nested \(b,b^*\) calls, and coupling
coordinates gives the corresponding \(d_R\) estimate.

At a fixed mesh, a finite oracle record is again one fixed tensor program.
To see this without hiding empirical feedback, recursively expand every
new \(b_kv\) call as
\[
B_0v-2\delta\sum_{r<k}e_rd_r\langle h_r,v\rangle_R, \tag{5.16}
\]
and every adjoint call analogously, using the deterministic canonical
inner-product.  Only finitely many calls occur.  Let
\(\zeta_{n,R}\) be the maximum absolute empirical-minus-canonical
difference of the finite list of Grams introduced by this recursion,
together with (5.6).  Theorem (3.1) gives
\(\zeta_{n,R}\to0\) almost surely.  Induction on probe depth, using the
exact finite-rank action and (5.15), gives
\[
\max_{v\in R}\|v(\bar\Theta_{n,k})-\bar v_{n,k}\|_n
\le C_{R,N,\delta}\zeta_{n,R},                    \tag{5.17}
\]
where \(\bar v_{n,k}\) is the deterministic-coefficient tensor-program
probe from (5.16).  Equations (5.7)--(5.10) and (5.14) then identify the
actual Euler record with the canonical Euler record.

Finally compare finite-width flow to its Euler scheme using (2.14) and
(5.14), take \(n\to\infty\) at fixed \(\delta\) using (5.17), and compare
canonical Euler to canonical flow using (5.11) and (5.14).  Uniform time
moduli replace the finite grid by all of \([0,T]\).  Hence, for every fixed
record and every \(\varepsilon>0\),
\[
\sup_{t\le T}d_R(\theta_n(t),\Theta(t))
\longrightarrow0\quad\text{in probability}.       \tag{5.18}
\]
For the metric (5.13), first choose a finite prefix whose remaining weight
is below \(\varepsilon/2\), and apply a union bound to that prefix.  This
proves uniform compact-time convergence in \(d_{\rm act}\).
The state carries the common operator bound furnished by (2.13) and the
finite rank integral in (4.4); mere finite-record convergence without this
bound would not suffice.  Equations (4.4), (4.8), and (5.18) prove the
claimed well-posed, autonomous, restartable law-level limit.

## 6. Path laws, kernels, and velocities

The raw preactivations are \(A=J(X)\) and \(S=Bh(X)\).  From (1.3), (1.6), and the bounds of Section 2,
\[
\sup_n\sup_{t\le T}\bigl(\|\dot A(t)\|_n+
\|\dot S(t)\|_n\bigr)<\infty                       \tag{6.1}
\]
on the high-probability initialization event.  For either \(Z=A\) or \(Z=S\), and an interval \(I\) of length \(\delta\),
\[
\frac1n\sum_i\sup_{s,t\in I}|Z_i(t)-Z_i(s)|^2
\le\delta\int_I\|\dot Z(r)\|_n^2\,dr.            \tag{6.2}
\]
Hence each empirical path law is within \(C_T\sqrt\delta\) in
\(W_2(C([0,T]))\) of its grid projection.  At a fixed grid, (5.18)
reduces the assertion to a fixed Euler program; (3.1) then gives weak
convergence and convergence of the squared grid maximum, since that maximum
is a polynomially bounded test of finitely many program vectors.  First let
\(n\to\infty\), then let the grid mesh tend to zero in (6.2).  This proves
\[
\frac1n\sum_i\delta_{A_i(\cdot)}\to\mu_A,qquad
\frac1n\sum_j\delta_{S_j(\cdot)}\to\mu_S
\quad\text{in }W_2(C([0,T]))                       \tag{6.3}
\]
in probability, as well as uniform integrability of the squared path suprema.

One further argument is necessary for the gated backpropagated fields; they are not naively Lipschitz as maps \(L^2\times L^2\to L^2\).  Put again \(P=B^*D\).  Equations (2.5)--(2.9) show that
\[
(X,B,C)\longmapsto(A,S,D,P)                         \tag{6.4}
\]
is Lipschitz from the bounded regularized state into normalized \(L^2\).  Also
\[
\dot P=\dot B^*D+B^*\dot D,qquad
\dot D=\dot Cq(S)+Cq'(S)\dot S,                    \tag{6.5}
\]
and (1.6) implies a uniform \(L^2\) bound on the right sides.  Consequently the joint empirical laws of \((A,P)\) converge uniformly in time in \(W_2(\mathbb R^2)\), and the resulting family is compact in that topology.

We use the following elementary lemma.

**Dominated pushforward lemma.**  If \(\mu_r\to\mu\) in \(W_2(\mathbb R^2)\), with coordinates \((a,p)\), and \(\Psi\) is continuous with \(|\Psi(a,p)|\le |p|\), then \(\Psi_\#\mu_r\to\Psi_\#\mu\) in \(W_2(\mathbb R)\).  The assertion is uniform over a compact \(W_2\)-family.

**Proof.**  \(W_2\) convergence is weak convergence plus uniform integrability of \(a^2+p^2\).  On \(|p|\le M\), truncate further to a compact set and approximate \(\Psi\) by bounded continuous functions.  Outside it,
\[
\int|\Psi|^2\mathbf1_{|p|>M}\,d\mu_r
\le\int p^2\mathbf1_{|p|>M}\,d\mu_r,              \tag{6.6}
\]
which tends to zero uniformly in \(r\) as \(M\to\infty\).  This proves weak convergence and convergence of second moments of the pushforwards, hence \(W_2\) convergence.  Compactness gives the uniform form. \(\square\)

Apply the lemma to
\[
\Psi_1(a,p)=q(a)p,qquad \Psi_2(a,p)=q(a)^2p.       \tag{6.7}
\]
Both are bounded in magnitude by \(|p|\).  The required uniform truncation is as follows.
Let
\[
\mu_{n,t}=\frac1n\sum_i\delta_{(A_{n,i}(t),P_{n,i}(t))},
\qquad \mu_t=\mathcal L(A(t),P(t)).                 \tag{6.8}
\]
The fixed-record convergence (5.18), the Lipschitz map (6.4), and the time
modulus from (6.5) imply
\[
\sup_{t\le T}W_2(\mu_{n,t},\mu_t)\longrightarrow0
\quad\text{in probability}.                       \tag{6.9}
\]
The image \(\{\mu_t:0\le t\le T\}\) is compact in \(W_2\).  For any
\(\gamma,\mu\in\mathcal P_2(\mathbb R^2)\), an optimal coupling of their
second coordinates gives
\[
\int p^2\mathbf1_{|p|>M}\,d\gamma
\le4W_2(\gamma,\mu)^2
 +2\int p^2\mathbf1_{|p|>M/2}\,d\mu.              \tag{6.10}
\]
Indeed, if \(|p_\mu|\le M/2<|p_\gamma|\), then
\(|p_\gamma|\le2|p_\gamma-p_\mu|\); otherwise use
\(|p_\gamma|^2\le2|p_\gamma-p_\mu|^2+2|p_\mu|^2\).
A finite \(W_2\)-cover of the compact limiting family, followed by (6.10),
gives
\[
\lim_{M\to\infty}\limsup_{n\to\infty}
\mathbb P\!\left(\sup_{t\le T}
 \int p^2\mathbf1_{|p|>M}\,d\mu_{n,t}>\varepsilon\right)=0. \tag{6.11}
\]

Let \(\rho_M(p)=(-M)\vee(p\wedge M)\) and
\[
Q=q(A)^2P,\qquad Q_M=q(A)^2\rho_M(P),              \tag{6.12}
\]
with identical finite-width notation.  Then
\[
\|Q-Q_M\|_2^2\le\int p^2\mathbf1_{|p|>M}\,d\mu_t, \tag{6.13}
\]
and the same empirical inequality holds.  At fixed \(M\), the map in
(6.12) is bounded and globally Lipschitz, so \(Q_M,BQ_M\), and all their
joint Grams are fixed action probes and converge uniformly by (5.18).
Put
\[
\alpha_n=\|H_n\|_n^2,\quad
Y_n=\alpha_nD_n+B_nQ_n,\quad
Y_{n,M}=\alpha_nD_n+B_nQ_{n,M},                   \tag{6.14}
\]
and define \(Y,Y_M\) canonically.  Uniform operator bounds give
\[
\|Y_n-Y_{n,M}\|_n\le M_B\|Q_n-Q_{n,M}\|_n,
\quad
\|Y-Y_M\|_2\le M_B\|Q-Q_M\|_2.                 \tag{6.15}
\]
Using
\(|\|u\|^2-\|v\|^2|\le(\|u\|+\|v\|)\|u-v\|\), first take
\(n\to\infty\) at fixed \(M\), and only then \(M\to\infty\).  Equations
(6.11)--(6.15) prove
\[
\sup_{t\le T}|\|Y_n(t)\|_n^2-\|Y(t)\|_2^2|
\longrightarrow0\quad\text{in probability}.      \tag{6.16}
\]
Since \(\dot S_n=-2e_nY_n\), (6.16) gives uniform convergence of its
squared velocity.  The same argument applied to \(q(A)P\), whose magnitude
is at most \(|P|\), handles \(\dot A\).  Hence
\[
\int_0^T\|\dot Z_n(t)\|_n^2dt
\longrightarrow\int_0^T\|\dot Z(t)\|_2^2dt,
\qquad Z=A,S.                                     \tag{6.17}
\]
The blocks \(K^B,K^C\) use bounded activations and \(D\), while \(K^A\)
uses the same dominated truncation.  Consequently
\[
K_n^r\to K^r\quad(r=A,B,C),\qquad K_n\to K         \tag{6.18}
\]
uniformly on \([0,T]\), and \(f_n,L_n\) converge uniformly as well.

## 7. Exact GD versus the finite-width flow

It remains to replace the auxiliary Euler schemes by the exact GD specified in the theorem.  Let
\[
R=-2eB^*D.                                          \tag{7.1}
\]
One raw GD step is \(A^+=A+\eta q(A)R\); the \(B,C\) updates are exactly the Euler updates of (2.2).  Since \(F\) is cubic,
\[
F(A+\eta q(A)R)=F(A)+\eta R
 +\eta^2Aq(A)^2R^2+\frac{\eta^3}{3}q(A)^3R^3       \tag{7.2}
\]
coordinatewise, with no remainder.  Now
\[
\sup_a|a|q(a)^2<\infty,qquad
\|R\|_n\le C_T,qquad
\|R\|_\infty\le\sqrt n\|R\|_n.                  \tag{7.3}
\]
Therefore the one-step defect relative to Euler in the \(X\)-coordinate is at most
\[
C_T(\eta^2\sqrt n+\eta^3n).                         \tag{7.4}
\]
The ordinary ODE local defect is \(O_T(\eta^2)\).  Applying the dimension-free stability estimate (2.10) step by step gives
\[
\sup_{t\le T}d_n(\theta_n^{\mathrm{GD}}(t),\theta_n(t))
\le C_T\bigl(\eta+\eta\sqrt n+\eta^2n\bigr).       \tag{7.5}
\]
The proof is first stopped on the enlarged bounded set from Section 2; the right side tends to zero, so the first-exit event is impossible for large \(n\).  With \(\eta=\eta_n=n^{-2}\), (7.5) tends to zero.

We linearly interpolate the parameter iterates and recompute all network
nodes from those interpolated parameters.  Let \(V_{A,k},V_{B,k}\) be the
constant parameter slopes on step \(k\).  Then
\[
V_{A,k}=-2e_kq(A_k)P_k,\qquad
V_{B,k}=-2e_kD_k\otimes_nH_k,                     \tag{7.6}
\]
and, at \(t=k\eta+s\), \(0\le s\le\eta\),
\[
\partial_tS(t)=V_{B,k}\arctan(A_k+sV_{A,k})
+(B_k+sV_{B,k})q(A_k+sV_{A,k})V_{A,k}.            \tag{7.7}
\]
The bounded-state estimates give
\[
\sup_{k\eta\le T}\{\|V_{A,k}\|_n+
\|V_{B,k}\|_{\rm op}+\|\partial_tS\|_n\}\le C_T  \tag{7.8}
\]
on the stopped event; (7.5) closes the stop.

It remains to pass the squared slopes, where a fourth-moment shortcut would
be invalid.  Let \(\widehat\mu_{n,k}\) be the empirical law of
\((A_k^{\rm GD},P_k^{\rm GD})\).  Equations (7.5), (6.4), and (6.9) give
\[
\max_{k\eta_n\le T}
W_2(\widehat\mu_{n,k},\mu_{k\eta_n})\longrightarrow0. \tag{7.9}
\]
Thus the uniform square-tail estimate (6.11) also holds at all GD nodes.
Since \(q'\) is bounded, on \(|P_k|\le M\),
\[
\|[q(A_k+sV_{A,k})-q(A_k)]V_{A,k}\|_n
\le C_T\eta M^2,                                  \tag{7.10}
\]
while on the complement both terms are bounded pointwise by
\(C_T|P_k|\).  Take \(n\to\infty\) at fixed \(M\), then \(M\to\infty\).
Define
\(\mathcal V^S_{n,k}=-2e_k\{\|H_k\|_n^2D_k+
B_k[q(A_k)^2P_k]\}\).  Equations (7.7)--(7.10), including the easy
\(\|V_{B,k}[H(A_k+sV_{A,k})-H_k]\|_n\le C_T\eta\)
term, show
\[
\int_0^T\left\|\partial_tS_n^{\rm GD}(t)-
\mathcal V^S_{n,\lfloor t/\eta\rfloor}\right\|_n^2dt
\longrightarrow0\quad\text{in probability}.       \tag{7.11}
\]
The same fixed-\(M\) action-probe argument as (6.12)--(6.16), followed by
Riemann-sum convergence of the strongly continuous limiting velocities,
therefore yields
\[
\int_0^T\|\partial_tA_n^{\rm GD}\|_n^2dt
\to\int_0^T\|\dot A\|_2^2dt,\qquad
\int_0^T\|\partial_tS_n^{\rm GD}\|_n^2dt
\to\int_0^T\|\dot S\|_2^2dt.                     \tag{7.12}
\]

We finally prove, rather than infer from same-time \(L^2\) convergence, the
path-space assertion for exact GD.  For \(Z=A,S\), let
\(\widehat\Lambda_n^Z=n^{-1}\sum_i\delta_{Z_{n,i}^{\rm GD}(\cdot)}\).
For a deterministic partition \(\pi=\{t_j\}\) of mesh at most \(\Delta\),
let \(I_\pi z\) interpolate its grid values.  Every absolutely continuous
scalar path satisfies
\[
\|z-I_\pi z\|_\infty^2
\le4\sum_j\sup_{s,t\in[t_j,t_{j+1}]}|z(t)-z(s)|^2.
\]
Cauchy--Schwarz, coordinate averaging, and (7.12) give
\[
W_2(\widehat\Lambda_n^Z,(I_\pi)_\#\widehat\Lambda_n^Z)^2
\le4\Delta\int_0^T\|\partial_tZ_n^{\rm GD}(t)\|_n^2dt
=O_{\mathbb P}(\Delta).                            \tag{7.13}
\]
At the finitely many coarse-grid times, (7.5), the Lipschitz property of
\(J\), and (2.6) imply convergence of the GD grid-vector empirical law to
the canonical grid law.  Hence, for fixed \(\pi\),
\[
(I_\pi)_\#\widehat\Lambda_n^Z
\longrightarrow (I_\pi)_\#\mu_Z
\quad\hbox{in }W_2(C([0,T])).                     \tag{7.14}
\]
The limiting version of (6.2) gives
\(W_2(\mu_Z,(I_\pi)_\#\mu_Z)\le C_T\sqrt\Delta\).
The triangle inequality in (7.13)--(7.14), first \(n\to\infty\) at fixed
\(\pi\), then \(\Delta\downarrow0\), proves
\[
\widehat\Lambda_n^A\to\mu_A,\qquad
\widehat\Lambda_n^S\to\mu_S
\quad\hbox{in }W_2(C([0,T]))\text{ in probability}. \tag{7.15}
\]

The uniform kernel/output/loss assertion for exact GD requires one final
tail transfer.  Define at every interpolated time
\[
\widehat\mu_{n,t}
=\frac1n\sum_i\delta_{(A_{n,i}^{\rm GD}(t),
                       P_{n,i}^{\rm GD}(t))}.
\]
The state estimate (7.5), the Lipschitz estimate (6.4), and (6.9) imply
\[
\sup_{t\le T}W_2(\widehat\mu_{n,t},\mu_t)
\longrightarrow0\quad\text{in probability}.       \tag{7.16}
\]
Applying (6.10) gives (6.11) with \(\widehat\mu_{n,t}\), uniformly over
the whole interpolation rather than only its nodes.  At fixed \(M\), the
map \(q(a)\rho_M(p)\) is bounded Lipschitz, so (7.5), (5.14), and the
flow convergence identify its squared empirical norm uniformly in time.
The difference from \(q(A)P\) has squared norm bounded by the tail in
(6.11).  Taking \(n\to\infty\) at fixed \(M\), then \(M\to\infty\), proves
\[
\sup_{t\le T}|K_{n,\rm GD}^A(t)-K^A(t)|
\longrightarrow0.                                 \tag{7.17}
\]
\(K^B,K^C\), the output, and the loss contain only bounded activations and
the Lipschitz field \(D=Cq(S)\), so (7.5) passes them directly.  Therefore
\[
\sup_{t\le T}\left(
 |K_{n,\rm GD}(t)-K(t)|+|f_{n,\rm GD}(t)-f(t)|
 +|L_{n,\rm GD}(t)-L(t)|\right)\longrightarrow0   \tag{7.18}
\]
in probability, and each of the three kernel blocks converges separately.

The actual \(C_n(0)\) was already included in the coupling: its normalized
\(L^2\) norm is \(O_{\mathbb P}(n^{-1})\), its sup norm is
\(o_{\mathbb P}(1)\), and (5.7)--(5.10) transfer it to the zero canonical
mark.  Sections 4--7 now prove the full joint diagonal convergence.

## 8. Exact initial action law and reused-adjoint response

Let
\[
A_0\sim N(0,1),\qquad H_0=\arctan A_0,qquad
m=\mathbb E H_0^2>0.                               \tag{8.1}
\]
The initial second preactivation has law
\[
Z\sim N(0,m).                                       \tag{8.2}
\]
Put
\[
G_0=\arctan Z,qquad
u(Z)=G_0q(Z)=\frac{\arctan Z}{1+Z^2},qquad
\nu=\mathbb Eu(Z)^2>0,qquad
\kappa=\mathbb Eu'(Z).                              \tag{8.3}
\]
The reused adjoint \(\Xi=B_0^*u(Z)\) contains both an innovation and a response.  We prove its law directly.

Condition on \(H=(H_i)\).  For row \(b_j\) of \(B_0\), let \(s_j=b_j^\top H\) and \(m_n=\|H\|_n^2\).  Gaussian regression gives
\[
b_j=\frac{s_j}{nm_n}H+\widetilde b_j,qquad
\widetilde b_j\mid(H,s_j)\sim
N\left(0,\frac1nP_H^\perp\right),                 \tag{8.4}
\]
independently over \(j\).  Consequently, conditionally on \((H,s)\),
\[
B_0^\top u(s)=a_nH+\sqrt{\nu_n}\,P_H^\perp\Gamma, \tag{8.5}
\]
where
\[
a_n=\frac1{nm_n}\sum_js_ju(s_j),qquad
\nu_n=\frac1n\sum_ju(s_j)^2,qquad
\Gamma\sim N(0,I_n).                               \tag{8.6}
\]
The laws of large numbers give \(\nu_n\to\nu\), and Gaussian integration by parts for \(Z\sim N(0,m)\) gives
\[
a_n\to\frac{\mathbb E[Zu(Z)]}{m}=\mathbb Eu'(Z)=\kappa. \tag{8.7}
\]
Moreover \(\|P_H^\perp\Gamma-\Gamma\|_n\to0\) in probability.  Hence the joint empirical limit is
\[
\Xi=\sqrt\nu\,\Gamma+\kappa H_0,qquad
\Gamma\sim N(0,1),\quad \Gamma\perp A_0.          \tag{8.8}
\]
This is precisely the innovation plus the Onsager/response term; omitting the second summand would be wrong.

Define
\[
d=\mathbb E[q(A_0)^2\Xi^2]
=\nu\mathbb E q(A_0)^2
+\kappa^2\mathbb E[q(A_0)^2H_0^2]>0.               \tag{8.9}
\]
On the left Hilbert space define the positive operator
\[
\mathcal R=mI+B_0M_{q(A_0)^2}B_0^*,                \tag{8.10}
\]
where \(M_{q(A_0)^2}\) is coordinate multiplication.  Then
\[
\langle u,\mathcal Ru\rangle
=m\nu+\langle B_0^*u,q(A_0)^2B_0^*u\rangle
=m\nu+d>0.                                         \tag{8.11}
\]
Thus \(\mathcal Ru\ne0\).

## 9. Small-time motion and completion of the theorem

At \(t=0\), \(C=0\), \(e=-1\), and hence \(D=P=0\).  The integral equations, in the strong \(L^2\) and operator topologies constructed above, give node by node
\[
C(t)=2tG_0+O_{L^2}(t^2),qquad
D(t)=2t\,u+O_{L^2}(t^2),                            \tag{9.1}
\]
\[
A(t)-A_0=2t^2q(A_0)\Xi+o_{L^2}(t^2),               \tag{9.2}
\]
\[
B(t)-B_0=2t^2u\otimes H_0+o_{\mathrm{op}}(t^2),   \tag{9.3}
\]
and
\[
S(t)-Z=2t^2\mathcal Ru+o_{L^2}(t^2).               \tag{9.4}
\]
For example, \(\dot D(0)=2u\), so
\(A''(0)=4q(A_0)B_0^*u\), \(B''(0)=4u\otimes H_0\); differentiating \(S=BH\) then gives
\[
S''(0)=4\{m u+B_0[q(A_0)^2B_0^*u]\}=4\mathcal Ru. \tag{9.5}
\]
These derivatives exist because the action flow is strongly continuous, all scalar derivatives of \(\arctan\) are bounded, and the relevant operator actions are bounded.  Alternatively, (9.1)--(9.4) follow directly by dividing the integral equations by the indicated powers of \(t\) and using dominated convergence.

The two hidden velocity energies therefore satisfy
\[
V_A(t)^2=16dt^2+o(t^2),qquad
V_S(t)^2=16\|\mathcal Ru\|_2^2t^2+o(t^2),          \tag{9.6}
\]
and the displacements satisfy
\[
\mathbb E|A(t)-A_0|^2=4dt^4+o(t^4),qquad
\mathbb E|S(t)-Z|^2=4\|\mathcal Ru\|_2^2t^4+o(t^4). \tag{9.7}
\]
Both leading coefficients are strictly positive by (8.9)--(8.11).  Hence both hidden layers have finite positive integrated velocity and nonzero displacement on every sufficiently short nonzero interval.

Let
\[
k_3=\mathbb E(\arctan Z)^2>0.                       \tag{9.8}
\]
Equations (9.1)--(9.4) yield
\[
K^A(t)=4dt^2+o(t^2),qquad
K^B(t)=4m\nu t^2+o(t^2),                            \tag{9.9}
\]
and, since
\(G(t)=G_0+2t^2q(Z)\mathcal Ru+o_{L^2}(t^2)\),
\[
K^C(t)=k_3+4(m\nu+d)t^2+o(t^2).                    \tag{9.10}
\]
Indeed \(\langle G_0,q(Z)\mathcal Ru\rangle=\langle u,\mathcal Ru\rangle=m\nu+d\).  Therefore
\[
K(t)=k_3+8(m\nu+d)t^2+o(t^2),                      \tag{9.11}
\]
so every block has a finite positive time integral and the total kernel is nonconstant.

Also
\[
f(t)=2k_3t+o(t),qquad
L(t)=1-4k_3t+o(t),                                  \tag{9.12}
\]
so \(f(0)=0\ne1\) and \(L(T)<L(0)\) for all sufficiently small \(T>0\).

It remains only to verify hidden variance and surviving nonlinearity.  At zero the laws are \(N(0,1)\) and \(N(0,m)\).  Their variances are positive and, by (6.3), continuous in time; hence they stay positive on a short interval.  For a law \(\mu\) with positive variance, the squared distance of \(\arctan z\) from affine functions is
\[
\mathcal N(\mu)=
\operatorname{Var}_\mu(\arctan Z)
-\frac{\operatorname{Cov}_\mu(Z,\arctan Z)^2}
       {\operatorname{Var}_\mu(Z)}.                \tag{9.13}
\]
It is strictly positive for either initial Gaussian: equality would make \(\arctan z\) affine on a full-support measure and, by continuity, on \(\mathbb R\).  The moments in (9.13) are continuous under \(W_2\); for the only unbounded mixed moment, an optimal coupling gives
\[
|\mathbb E[X\arctan X-Y\arctan Y]|
\le a_0\|X-Y\|_2+\|Y\|_2\|X-Y\|_2.              \tag{9.14}
\]
Thus both nonlinear residuals remain positive and have positive time integrals after reducing \(T_*\) if necessary.

All assertions in the theorem have now been proved. \(\square\)

## Audit note on external dependencies

The only research-level theorem used is the fixed finite, parameterless
reused-Gaussian Master Theorem (3.1).  Its hypotheses are met only by the
deterministic finite program (5.3); empirical feedback, the width-dependent
small readout initialization, continuous time, and exact GD are handled
separately in Sections 2 and 4--7.  No growing-program,
conditional-expectation, mean-convergence, DMFT, or operator-norm theorem
is assumed.

The audited primary source is Greg Yang, *Tensor Programs III: Neural
Matrix Laws*, arXiv:2009.10685v3 (8 May 2021),
<https://arxiv.org/pdf/2009.10685v3>.  The source check covered Setup 2.2,
Box 1 and Remarks 2.11--2.12, Theorem 2.10, and the complete
Moments/CoreSet proof in Appendix L: simultaneous conditioning on every
earlier \(BY\) and \(B^\top V\) constraint, rank and zero stability, the
zero-innovation and positive-innovation branches, and the projected
Gaussian strong law.  Those arguments establish exactly (3.1), including
singular initial Gaussian covariance and every reused-transpose response.
They give no estimate uniform in program length, and none is used here.

The audit found and repaired six literal slips inside that proof rather
than silently inheriting them.  In the transpose-adjunction Case 2
(source file proofs.tex, lines 1578--1617), the conditioning vector must be
\[
U=(\widehat Z^{u^1},\ldots,\widehat Z^{u^k}),
\]
not \((Z^{u^1},\ldots,Z^{u^k})\); only the former is the Gaussian vector
whose covariance is the displayed matrix \(C\), and conditioning on it
gives the asserted independence.  After Case 1 is substituted, the next
column must be \((Z^{v^1},\ldots,Z^{v^k})\), not its hatted version.  With
those two replacements, ordinary possibly-singular Gaussian regression
\(b^\top C^+U\) proves the printed adjunction identity.

In the high-moment collision count (source lines 1044--1125), the
one-collision contribution is
\[
n^{-(p-1)/4}n^{2p-1}B''_{2p}
=n^{(7p-3)/4}B''_{2p},
\]
not \(n^{7(p-1)/4}B''_{2p}\).  After the surrounding \(n^{-2p}\)
normalization it is \(n^{-(p+3)/4}B''_{2p}\), which is summable for the
proof's choice \(p\ge6\); the Borel--Cantelli conclusion is unchanged.
Finally, the Gaussian-conditioning variance near source line 3019 is
\[
\operatorname{Var}(\widehat Z^g\mid\widehat Z)
=\sigma_A^2\!\left(\mathbb E(Z^h)^2
 -\mathring\gamma^\top\mathring\Upsilon^+
  \mathring\gamma\right)=\mathring\sigma^2,
\]
not the dimensionally inconsistent printed
\(\mathbb E(Z^g)^2-\cdots=\mathring\sigma\).
These are local symbol/count repairs; the corrected quantities are exactly
those defined earlier in the source, and every subsequent bound uses the
correct squared variance.  The complete induction was reread with these
repairs in place.

Three earlier/later displays require the following additional corrections.
In the simultaneous Gaussian-conditioning lemma (source lines 243--278),
the conditional mean is
\[
E=ZQ^+ +P^{+\top}X^\top-P^{+\top}P^\top ZQ^+;     \tag{A.1}
\]
the source's \(Y\) is undefined and must be \(Z\), and the Lagrange
multiplier calculation requires \(Q^+\), not \(Q^\top\).  Direct
multiplication, using the compatibility \(X^\top Q=P^\top Z\), verifies
\(EQ=Z\) and \(P^\top E=X^\top\); the displayed Lagrange stationarity
then proves that (A.1) is the minimum-Frobenius-norm solution.  The
orthogonal Gaussian remainder in the lemma is therefore unchanged.

In the projected-variance rewrite (source lines 1866--1869), with
\(\gamma=Y^\top h/n\) and \(\Upsilon=Y^\top Y/n\), the exact identity is
\[
\sigma^2=\sigma_A^2\left(\frac{h^\top h}{n}
                         -\gamma^\top\Upsilon^+\gamma\right), \tag{A.2}
\]
because \(Y^\top h=n\gamma\) and
\((Y^\top Y)^+=n^{-1}\Upsilon^+\).  This is precisely the expression whose
limit the next source line states.  Finally, at source lines 3663--3668,
\[
\frac1n\sum_\alpha
\max(\sigma^2d_\alpha,\mathring\sigma^2)^p
\le\max(\sigma^2,\mathring\sigma^2)^p,             \tag{A.3}
\]
not the same maximum to the power \(p/2\).  Since
\(\sigma\to\mathring\sigma\), (A.3) has the uniform boundedness required
there.  None of (A.1)--(A.3) alters a definition or a subsequent estimate;
they repair the literal algebra used to reach the intended quantities.

Two printed auxiliary claims were deliberately excluded after source-level
inspection: Appendix A.1's arbitrary varying-conditioning almost-sure
claim is stronger than dominated convergence warrants, and the printed
Appendix A.2 mean-convergence proof omits a uniform-integrability step.
The Gaussian operator-norm citation there is also not used; (2.13) is the
complete net proof required here.  Thus no conclusion of the external
paper beyond the verified assertion (3.1) enters this proof.
