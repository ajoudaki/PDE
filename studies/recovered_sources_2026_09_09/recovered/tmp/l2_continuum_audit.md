# Independent continuum audit: the two-hidden-layer arctangent construction

## 1. Exact scaling and equations

For
\[
 A_i(0)\sim N(0,1),\qquad B_{ji}(0)\sim N(0,n^{-1}),\qquad
 c_j(0)\sim N(0,n^{-4}),
\]
put
\[
 C=nc,\quad \langle u,v\rangle_n=n^{-1}u^Tv,\quad
 H=\arctan A,\quad S=BH,\quad G=\arctan S,
\]
\[
 q(x)=(1+x^2)^{-1},\quad D=Cq(S),\quad e=\langle C,G\rangle_n-1.
\]
The forward output is exactly \(f_n=\langle C,G\rangle_n\).  With raw
mobilities \((\lambda_A,\lambda_B,\lambda_c)=(n,1,n^{-1})\), the
finite-width gradient-flow equations are
\[
 \dot A=-2e\,q(A)B^TD,\qquad
 \dot B=-2e\,D\otimes_nH,\qquad
 \dot C=-2eG,                                      \tag{1}
\]
where \(u\otimes_nv=uv^T/n\).  Direct differentiation gives the kernel
blocks
\[
 K^A=\|q(A)B^TD\|_n^2,\qquad
 K^B=\|H\|_n^2\|D\|_n^2,\qquad K^C=\|G\|_n^2.      \tag{2}
\]
Consequently \(\dot f=-2eK\) and \(\dot L=-4e^2K\).

## 2. The regularizing coordinate really gives dimension-free stability

Let
\[
 \mathcal F(a)=a+a^3/3,\qquad X=\mathcal F(A),\qquad J=\mathcal F^{-1}.
\]
Since \(\mathcal F'(a)=q(a)^{-1}\), (1) is exactly equivalent to
\[
 \dot X=-2eB^TD,\qquad \dot B=-2eD\otimes_nH,\qquad
 \dot C=-2eG,                                      \tag{3}
\]
with \(A=J(X)\).  Here \(J' =q\circ J\), so \(J\) is 1-Lipschitz, and
\(h=\arctan\circ J\) satisfies \(|h'|=q(J)^2\le1\).  Also
\(q\circ J\) is globally Lipschitz.

Use
\[
 d_n((X,B,C),(\widetilde X,\widetilde B,\widetilde C))
 =\|X-\widetilde X\|_n+\|B-\widetilde B\|_{op}
  +\|C-\widetilde C\|_n.                            \tag{4}
\]
On a set where \(\|B\|_{op},\|\widetilde B\|_{op}\le M_B\) and
\(\|C\|_\infty,\|\widetilde C\|_\infty\le M_C\), every map in (3) is
Lipschitz in (4), with a constant depending only on \(M_B,M_C\).  For
example,
\[
 \|BH-\widetilde B\widetilde H\|_n
 \le(\pi/2)\|B-\widetilde B\|_{op}
     +M_B\|X-\widetilde X\|_n,
\]
and
\[
 \|Cq(S)-\widetilde Cq(\widetilde S)\|_n
 \le\|C-\widetilde C\|_n
   +M_C\operatorname{Lip}(q)\|S-\widetilde S\|_n.
\]
The identities
\(\|u\otimes_nv\|_{op}=\|u\|_n\|v\|_n\) and
\(\|B^*u\|_n\le\|B\|_{op}\|u\|_n\) finish the estimate.

There are width-independent a priori bounds on every compact interval.
Indeed, loss dissipation gives \(|e(t)|\le |e(0)|\), while
\[
 \|C(t)\|_\infty\le\|C(0)\|_\infty+\pi |e(0)|t.
\]
Then (3) successively bounds \(\|B(t)\|_{op}\) and \(\|X(t)\|_n\).
For the stated Gaussian initialization, with probability tending to one,
\(\|B(0)\|_{op}\le M_0\), \(\|X(0)\|_n\le M_0\), and
\(\|C(0)\|_\infty\le1\), for an absolute constant \(M_0\).  The first
claim follows directly from a Gaussian epsilon-net bound; no asymptotic
spectral theorem is needed.  Thus (3) has a unique global finite-width
solution and its Euler method has, uniformly in \(n\), error \(C_T\delta\).

## 3. Correct fixed-mesh identification

It is not legitimate simply to call the trained mesh a parameterless tensor
program: the Euler iterates contain empirical scalar moments.  The correct
argument uses a deterministic population oracle.

Fix \(\delta>0\) and \(N=T/\delta<\infty\).  Expand the learned matrix:
\[
 B_k=B_0-2\delta\sum_{r<k}e_rD_r\otimes_nH_r.        \tag{5}
\]
Therefore
\[
 B_kv=B_0v-2\delta\sum_{r<k}e_rD_r\langle H_r,v\rangle_n,
\]
\[
 B_k^*u=B_0^*u-2\delta\sum_{r<k}e_rH_r\langle D_r,u\rangle_n. \tag{6}
\]
Construct the oracle recursively by replacing every scalar in (6), and
\(e_k\), by the deterministic expectation prescribed by the preceding
oracle variables.  Since \(N\) is fixed, the oracle is a finite,
parameterless program using only \(B_0,B_0^*\), coordinate maps, and fixed
real coefficients.  Its coordinate maps are polynomially bounded (in fact
all maps relevant after \(J\) are bounded or Lipschitz).

The parameterless reused-matrix Master Theorem, applied only to this fixed
program, gives almost-sure convergence of all oracle empirical moments.
Induction on \(k\), using (6), the high-probability bound on
\(\|B_0\|_{op}\), and Cauchy--Schwarz, then proves that every actual Euler
probe is \(o(1)\) from its oracle counterpart in normalized \(L^2\).
For example, if all earlier probes are coupled, then the discrepancy in
the first display of (6) is bounded by \(\|B_0\|_{op}\|v-v^o\|_n\) plus a
finite sum of vector discrepancies and empirical-moment discrepancies.
The latter vanish by the oracle theorem and the induction hypothesis.
This proves fixed-mesh identification without invoking a theorem for a
growing number of steps and without invoking the rank-unstable
parameterized version of Tensor Programs.

## 4. From fixed meshes to a compact-time autonomous action law

For each finite \(n\), compare its two Euler schemes of meshes \(\delta\)
and \(\delta'\) through the same exact ODE (3).  The estimate of Section 2
gives
\[
 \sup_{t\le T}d_n(\theta_n^\delta(t),\theta_n^{\delta'}(t))
 \le C_T(\delta+\delta').                            \tag{7}
\]
Every fixed finite probe built from \(X,C,B,B^*\), bounded Lipschitz
coordinate maps, and normalized inner products is Lipschitz on the same
bounded set.  Thus its two empirical laws are within
\(C_{T,P}(\delta+\delta')\) in \(W_2\).  Taking \(n\to\infty\) first in
(7), using Section 3, shows that the deterministic fixed-mesh action laws
are Cauchy as \(\delta\downarrow0\).  This is the required bridge; it does
not compare matrices of different dimensions.

For completeness, at each time enumerate a countable dense set of finite
right and left probes generated by the **current** \((X,C,B,B^*)\), and
record every finite joint coordinate law and every normalized inner
product.  The resulting metric is a weighted sum of truncated
\(W_2\) distances.  Positivity of finite empirical Gram matrices passes to
the limit.  Quotienting the two rational probe spans by their null
seminorms and completing produces Hilbert spaces \(\mathcal H_R,\mathcal
H_L\).  A Gaussian epsilon-net bound gives \(\|B_0\|_{op}\le M_0\)
eventually almost surely; hence
\[
 \|B_0v\|_{\mathcal H_L}\le M_0\|v\|_{\mathcal H_R}
\]
first for formal probes and then by completion.  The finite identity
\(\langle u,B_0v\rangle=\langle B_0^*u,v\rangle\) proves that the two
formal actions extend to adjoint bounded operators.  The same statement
holds for the current operator because it is \(B_0\) plus the Bochner
integral of bounded rank-one operators.  Thus restarting uses only current
\((X,C,B)\), not \(B_0\) or the update history.

Finite joint laws supply the commutative coordinate algebras on each side.
Lipschitz Nemytskii maps extend continuously in \(L^2\); multiplication by
\(Cq(S)\) is legitimate because \(C\in L^\infty\), with its deterministic
bound above.  Rank-one maps are bounded.  Therefore (3) is a genuine ODE
on this two-sorted realization.  The estimate in Section 2 proves
uniqueness.  Two realizations of the same complete action law are
intertwined by the unitary induced on formal probes, so uniqueness descends
to the law state.  The flow is consequently autonomous, restartable, and
satisfies the semigroup property.

## 5. Path laws and velocity observables

In addition to \(\|\dot A\|_n\le\|\dot X\|_n\), direct differentiation gives
\[
 \dot S=-2e\{\|H\|_n^2D+B[q(A)^2B^*D]\}.             \tag{8}
\]
The bounds above imply \(\sup_{n,t\le T}(\|\dot A\|_n+
\|\dot S\|_n)<\infty\).  On a time interval of length \(\delta\),
\[
 {1\over n}\sum_i\sup_{s,t\in I}|z_i(t)-z_i(s)|^2
 \le \delta\int_I {1\over n}\sum_i|\dot z_i(r)|^2\,dr. \tag{9}
\]
Consequently each empirical path law is at \(W_2(C[0,T])\)-distance
\(O(\sqrt\delta)\) from its grid projection.  Fixed-grid joint laws and
their second moments converge by Section 3.  Sending first \(n\to\infty\)
and then \(\delta\downarrow0\) proves the full path-law convergence and,
at the same time, path-square uniform integrability.  Applying the same
mesh argument to the velocity observables requires one extra truncation;
they are not naively \(L^2\)-Lipschitz because an unbounded backpropagated
field is multiplied by a moving gate.  Here is the complete repair.

Put \(P=B^*D\).  On the bounded state sets of Section 2, the maps
\[
 (X,B,C)\mapsto (A,S,D,P)
\]
are Lipschitz from the metric (4) into the corresponding normalized
\(L^2\) spaces: the only final estimate needed is
\[
 \|B^*D-\widetilde B^*\widetilde D\|_n
 \le \|B-\widetilde B\|_{op}\|D\|_n
      +\|\widetilde B\|_{op}\|D-\widetilde D\|_n.   \tag{9a}
\]
Thus the coordinate coupling proves uniform \(W_2\) convergence of the
joint empirical laws of \((A,P)\) whenever the state converges.  Moreover,
\[
 \dot P=\dot B^*D+B^*\dot D,\qquad
 \dot D=\dot Cq(S)+Cq'(S)\dot S,                    \tag{9b}
\]
and the preceding bounds show \(\sup_{n,t\le T}\|\dot P(t)\|_n<\infty\).
Consequently these joint laws are equicontinuous in time in \(W_2\), and
the mesh argument gives convergence uniformly in \(t\).

We use the following elementary mapping lemma.  If
\(\mu_r\to\mu\) in \(W_2(\mathbb R^2)\) for coordinates \((a,p)\), and
\(\Psi\) is continuous with \(|\Psi(a,p)|\le |p|\), then
\(\Psi_\#\mu_r\to\Psi_\#\mu\) in \(W_2\).  To prove it, truncate at
\(|p|\le M\).  The truncated map can be uniformly approximated on compact
sets by a bounded Lipschitz map, while
\[
 \int |\Psi|^2\mathbf1_{|p|>M}\,d\mu_r
 \le\int p^2\mathbf1_{|p|>M}\,d\mu_r.
\]
The right side tends to zero uniformly in \(r\) because \(W_2\)
convergence is equivalent to weak convergence plus uniform integrability
of squared norms.  First let \(r\to\infty\), then \(M\to\infty\).
The same proof is uniform for a compact \(W_2\)-family of measures.

Apply this lemma to
\[
 \Psi_1(a,p)=q(a)p,\qquad \Psi_2(a,p)=q(a)^2p.       \tag{9c}
\]
Both have magnitude at most \(|p|\).  It follows that the first hidden
velocity \(-2e\Psi_1(A,P)\), its squared norm \(K^A\), and
\(Q=\Psi_2(A,P)\) converge uniformly in time in the required \(L^2\)/scalar
sense.  For the remaining unbounded term in (8), truncate \(Q\) in the
same way and use
\[
 \|B(Q-Q_M)\|_n\le M_B\|Q-Q_M\|_n.                 \tag{9d}
\]
This proves convergence of the second hidden velocity, its squared norm,
and both velocity time integrals.  The other kernel blocks contain only
bounded activations and \(D\), and are already Lipschitz.  Hence all three
kernel blocks converge uniformly on compact time intervals.  No fourth
moment of \(P\), and no tensor-program estimate uniform in program length,
is used.

## 6. Exact GD on the diagonal mesh

Let \(R=-2eB^*D\).  Exact GD gives \(A^+=A+\eta q(A)R\), while its \(B,C\)
updates are exactly Euler updates of (3).  The cubic identity
\[
 \mathcal F(A+\eta q(A)R)=\mathcal F(A)+\eta R
 +\eta^2Aq(A)^2R^2+{\eta^3\over3}q(A)^3R^3           \tag{10}
\]
is exact.  Since \(\sup_a|a|q(a)^2<\infty\),
\(\|R\|_n\le C_T\), and \(\|R\|_\infty\le\sqrt n\|R\|_n\), the one-step
defect in \(X\) is at most
\[
 C_T(\eta^2\sqrt n+\eta^3n).                         \tag{11}
\]
Discrete Gronwall, together with the ordinary Euler error, yields
\[
 \sup_{t\le T}d_n(\theta_n^{GD}(t),\theta_n(t))
 \le C_T(\eta+\eta\sqrt n+\eta^2n).                  \tag{12}
\]
The estimate is first proved under the a-priori bounds of Section 2 and
then closes them by a bootstrap.  With \(\eta=n^{-2}\), (12) tends to zero.
Moreover \(\eta\lambda_A=n^{-1}\), \(\eta\lambda_B=n^{-2}\), and
\(\eta\lambda_c=n^{-3}\), so all required raw step sizes vanish.

The velocity assertion for the piecewise-linear interpolation also follows,
but again requires the truncation in Section 5.  Its first-layer slope is
exactly \(-2e_kq(A_k)P_k\).  For the second layer, writing
\(V_{B,k}=-2e_kD_k\otimes_nH_k\) and
\(V_{A,k}=-2e_kq(A_k)P_k\),
\[
 {S_{k+1}-S_k\over\eta}
 =V_{B,k}H_k+B_k{\arctan(A_k+\eta V_{A,k})-\arctan A_k\over\eta}
  +V_{B,k}\{\arctan(A_k+\eta V_{A,k})-\arctan A_k\}. \tag{12a}
\]
On \(|P_k|\le M\), the middle difference quotient differs from
\(q(A_k)V_{A,k}\) by at most \(C_T\eta M^2\).  On the complement, both
are bounded in magnitude by \(C_T|P_k|\); the uniform square-tail estimate
from Section 5 applies.  First take the joint width limit, then
\(M\to\infty\).  The final term of (12a) is \(o_{L^2}(1)\) because
\(\|V_{B,k}\|_{op}\le C_T\) and
\(\|\arctan(A_k+\eta V_{A,k})-\arctan A_k\|_n
\le\eta\|V_{A,k}\|_n\).  Hence both discrete hidden-velocity energies and
their integrals converge to those of (1) and (8).

The actual \(C_n(0)\) can be replaced by zero: \(\|C_n(0)\|_n=O_P(n^{-1})\)
and \(\|C_n(0)\|_\infty=o_P(1)\), and Section 2 transfers this discrepancy
uniformly on compact times.

## 7. Nondegeneracy, activity, and nonlazy behavior

Let \(A_0\sim N(0,1)\), \(H_0=\arctan A_0\),
\(m=E H_0^2>0\), and \(Z\sim N(0,m)\).  Put
\[
 G_0=\arctan Z,\quad U=G_0q(Z),\quad
 \nu=EU^2>0,\quad \Xi=B_0^*U.
\]
The parameterless reused-adjoint rule gives
\[
 \Xi\ \stackrel d=\ \sqrt\nu\,\Gamma+\kappa H_0,qquad
 \kappa=Eu'(Z),                                    \tag{13}
\]
where \(u(z)=\arctan(z)q(z)\) and \(\Gamma\sim N(0,1)\) is independent of
\(A_0\).  Hence
\[
 d:=E[q(A_0)^2\Xi^2]
 =\nu E q(A_0)^2+\kappa^2E[q(A_0)^2H_0^2]>0.         \tag{14}
\]
On the left Hilbert space define
\[
 \mathcal R=mI+B_0M_{q(A_0)^2}B_0^*.
\]
It is positive and
\(\langle U,\mathcal RU\rangle=m\nu+d>0\), so
\(\mathcal RU\ne0\).

The integral equations, using only \(L^2\) convergence and boundedness of
the scalar derivatives, now give
\[
 C(t)=2tG_0+O_{L^2}(t^2),\quad D(t)=2tU+O_{L^2}(t^2),
\]
\[
 A(t)-A_0=2t^2q(A_0)\Xi+o_{L^2}(t^2),\qquad
 S(t)-Z=2t^2\mathcal RU+o_{L^2}(t^2).                \tag{15}
\]
Thus
\[
 V_A(t)^2=16dt^2+o(t^2),\qquad
 V_S(t)^2=16\|\mathcal RU\|_2^2t^2+o(t^2),          \tag{16}
\]
and both hidden layers have positive integrated velocity and nonzero
displacement on every sufficiently short nonzero interval.

The kernel blocks satisfy
\[
 K^A(t)=4dt^2+o(t^2),\quad K^B(t)=4m\nu t^2+o(t^2),
\]
\[
 K^C(t)=k_3+4(m\nu+d)t^2+o(t^2),\quad
 k_3=E(\arctan Z)^2>0.                              \tag{17}
\]
Therefore all three blocks have positive time integrals and
\[
 K(t)=k_3+8(m\nu+d)t^2+o(t^2)
\]
is nonconstant.  Since \(e(0)=-1\) and \(K(0)=k_3>0\), loss decreases for
all sufficiently small positive times.

Finally, the two initial preactivation laws are nondegenerate Gaussians.
If the regression residual of \(\arctan\) on \(1,z\) vanished under either
law, continuity and the everywhere-positive Gaussian density would force
\(\arctan\) to be affine on \(\mathbb R\), a contradiction.  The residual
equals
\[
 \operatorname{Var}(\arctan Z)
 -{\operatorname{Cov}(Z,\arctan Z)^2\over\operatorname{Var}(Z)}.
\]
It is continuous under \(W_2\) while the variance stays bounded away from
zero.  Hence hidden variances and both nonlinear residuals remain strictly
positive on a short interval.

## Audit conclusion

The continuum and diagonal-limit parts are valid after the two corrections
made above: use a deterministic population oracle at fixed mesh, and use a
same-width Euler sandwich rather than a cross-dimensional operator-norm
comparison.  No theorem uniform in the number of tensor-program steps is
needed.  The only nonclassical external input left is the **parameterless,
fixed finite program** reused-matrix Master Theorem.  Its exact source and
proof must be audited separately; the argument above does not rely on the
more weakly proved parameterized/no-rank-stability extension.
