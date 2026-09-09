# Offset-arctan nontriviality certificate — conditional candidate

For the fixed activation
\[
\phi(z)=1+\varepsilon\arctan z,\qquad \varepsilon=1/10,
\qquad \phi'(z)=\frac{\varepsilon}{1+z^2},
\]
all three hidden populations have nonzero second-order feature movement,
and the output kernel strictly increases initially, in any canonical
strong population flow satisfying premise C below. Uniform deterministic response
row bounds also prevent affine collapse at every time in any limiting
hidden law. These are conditional nontriviality conclusions, not a proof
of existence, the response bootstrap, or the joint MF/GF/exact-GD theorem.

## 1. Model, conventions, and exact conditional premises

Write \(b=5/6\), \(a=7/6\), and \(S=3/2\). Then
\(b<\phi<a\), \(0<\phi'\le\varepsilon\), and
\(F(z)=10(z+z^3/3)\) satisfies \(F'=1/\phi'\).
The first trained block is \(z^{(1)}=W^{(1)}\) for the single input 1.
At finite width,
\[
h^{(\ell)}=\phi(z^{(\ell)}),\quad
z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},\quad
f_n=\frac{(W^{(4)})^T h^{(3)}}n,\quad L_n=(f_n-1)^2.
\]
All initialization blocks are independent:
\(z^{(1)}_{0,i}\sim N(0,1)\),
\(W^{(2)}_{0,ij},W^{(3)}_{0,ij}\sim N(0,1/n)\), and
the rescaled \(W^{(4)}_{0,i}\sim N(0,n^{-2})\).
Use finite transpose \(T\) and population Hilbert adjoint \(*\).
Finite vector sizes are ordinary \(\|u\|_2/\sqrt n\); matrix sizes
are ordinary operator or Frobenius norms. Population sizes are ordinary
\(L^2\) norms. No normalized-norm aliases are used.

On three separate population spaces let \(E_\ell\) denote expectation;
\((u\otimes v)x=uE_{\ell-1}[vx]\) for adjacent layers. The required
uncut feature-time equations, with the same forward definitions, are
\[
\begin{aligned}
\delta^{(3)}&=W^{(4)}\phi'(z^{(3)}),&
q^{(2)}&=(W^{(3)})^*\delta^{(3)},&
\delta^{(2)}&=\phi'(z^{(2)})q^{(2)},\\
q^{(1)}&=(W^{(2)})^*\delta^{(2)},&
\delta^{(1)}&=\phi'(z^{(1)})q^{(1)},\\
\frac{dz^{(1)}}{ds}&=\delta^{(1)},&
\frac{dW^{(\ell)}}{ds}&=\delta^{(\ell)}\otimes h^{(\ell-1)}
\quad(\ell=2,3),&
\frac{dW^{(4)}}{ds}&=h^{(3)}.
\end{aligned}                                                    \tag{1}
\]
Their finite counterparts replace \(*\) by \(T\) and each rank-one
action by \(\delta^{(\ell)}(h^{(\ell-1)})^T/n\).
Exact raw GD adds \(2\eta_n(1-f_{n,k})\), \(\eta_n=n^{-2}\), times
these finite directions evaluated at the old raw state, then recomputes
hidden objects. Raw parameters are interpolated in physical time.
The residual is outside every \(\delta^{(\ell)}\). The \(F\)-mesh
used below is a proof discretization, not an exact rewrite of raw GD.

The following premises are explicitly conditional:

- **R1 (fixed-mesh identification).** For this specific \(\phi,F\),
  the scalar representation (9)–(10) below holds on every fixed mesh,
  including its source independence, covariances, formal derivative
  convention, and learned terms. Auxiliary clipping is allowed there.
- **R2 (uniform rows).** Use the supplied candidate bounds, still
  conditional on the main bootstrap, with \(A=3/2\):
  \[
  |a^{(\ell)}_{kj}|\le A\Delta\quad(j<k),\qquad
  \sum_{j\le k}|b^{(\ell)}_{kj}|\le1,
  \quad \ell=2,3,\quad k\Delta\le S.                 \tag{2}
  \]
  These constants are independent of mesh and auxiliary clipping.
  Forward coefficients as well as backward rows are included.
- **C (flow and identification, when referring to trained dynamics).**
  There is an uncut integral solution of (1), with zero population
  readout initially, canonical Gaussian initial matrix actions and
  their adjoints, continuous \(L^2\) fields and operator-norm-continuous
  bounded matrix actions. Its one-time hidden laws are weak limits
  of the R1 programs as the mesh and clipping are removed. For claims
  about every finite physical time, this solution is constructed on
  \([0,S]\). Section 2 needs only such a solution near zero and its
  initial Gaussian laws; the tail argument in Section 3 needs only
  R1–R2 and applies to any weak limiting laws, without assuming C.
- **C_b (backward-field identification, only for the positive-time
  backward corollary).** The weak identification in C also includes
  \(\delta^{(2)},\delta^{(3)},q^{(1)},q^{(2)}\), with their
  same-layer joint laws along the same approximating programs.

Identification of this solution with the full-sequence finite GF and
prescribed exact raw GD remains a separate, unproved transfer requirement
here. No conclusion for those finite dynamics is inferred just from R1.

## 2. Initial movement with all trained blocks retained

Set \(m_\ell=E_\ell[(h^{(\ell)}_0)^2]\). With \(G\sim N(0,1)\),
the initial forward Gaussian laws give
\[
z^{(1)}_0\sim N(0,1),\quad z^{(2)}_0\sim N(0,m_1),\quad
z^{(3)}_0\sim N(0,m_2),
\]
where recursively \(m_\ell=E\phi(\sqrt{v_\ell}G)^2>1\),
\(v_1=1,v_2=m_1,v_3=m_2\). Indeed symmetry gives
\(E\phi(\sqrt vG)^2=1+\varepsilon^2 E\arctan(\sqrt vG)^2>1\).
Define, on their respective populations,
\[
\begin{aligned}
\beta_3&=h^{(3)}_0\phi'(z^{(3)}_0),\\
\beta_2&=\phi'(z^{(2)}_0)(W^{(3)}_0)^*\beta_3,\\
\beta_1&=\phi'(z^{(1)}_0)(W^{(2)}_0)^*\beta_2,\\
V_1&=\beta_1,\\
V_2&=m_1\beta_2+W^{(2)}_0[\phi'(z^{(1)}_0)\beta_1],\\
V_3&=m_2\beta_3+W^{(3)}_0[\phi'(z^{(2)}_0)V_2].
\end{aligned}                                                    \tag{3}
\]

Here is the needed initial transpose calculation, re-derived for the
offset activation. If \(W_{ij}\sim N(0,1/n)\), \(y=Wh\), and
\(h\ne0\) is independent of \(W\), conditioning on \(h,y\) gives
\[
W=\frac{yh^T}{\|h\|_2^2}+\widetilde W P_{h^\perp},\qquad
W^Tu=h\frac{y^Tu/n}{\|h\|_2^2/n}
       +\frac{\|u\|_2}{\sqrt n}P_{h^\perp}g                 \tag{4}
\]
in conditional law, for any \(u\) determined without observing the
residual \(\widetilde W\); \(g\) is fresh standard Gaussian.
This follows by projecting each independent Gaussian row onto \(h\)
and its orthogonal complement. The removed projection satisfies
\(E[\|P_{\operatorname{span}(h)}g\|_2^2/n\mid h]=1/n\).
Thus conditional averaging gives the scalar law
\(ch+\sigma G\), where \(c=E[yu]/E[h^2]\) and
\(\sigma^2=E[u^2]\), with independent innovation. The variance is
not reduced by subtracting the response term.

Apply (4) first to \(W^{(3)}_0,h^{(2)}_0,\beta_3\). On population 2,
\[
(W^{(3)}_0)^*\beta_3=c_3\phi(z^{(2)}_0)+\sigma_3G_2,
\quad \sigma_3^2=E_3[\beta_3^2]>0,
\quad
c_3=\frac{\varepsilon^2}{m_2}
 E_3\frac{z^{(3)}_0\arctan z^{(3)}_0}{1+(z^{(3)}_0)^2}>0.       \tag{5}
\]
The term \(\varepsilon E_3[z^{(3)}_0/(1+(z^{(3)}_0)^2)]\)
vanishes by symmetry; the remaining integrand is positive off zero.
In particular, the old pointwise assertion
\(z\phi(z)\phi'(z)>0\) would be false for this candidate.
Here \(G_2\) is independent of \(z^{(2)}_0\), so
\[
\sigma_2^2:=E_2[\beta_2^2]
=E_2\!\left[\phi'(z^{(2)}_0)^2
  \{c_3^2\phi(z^{(2)}_0)^2+\sigma_3^2\}\right]>0.
\]
For the second transpose, condition on \(z^{(1)}_0,z^{(2)}_0\) and
the entire independent \(W^{(3)}_0\). Then \(\beta_2\) is fixed
without exposing the conditional residual of \(W^{(2)}_0\).
Equation (4) gives, on population 1,
\[
(W^{(2)}_0)^*\beta_2=c_2\phi(z^{(1)}_0)+\sigma_2G_1,\qquad
c_2=\frac{c_3\varepsilon^2}{m_1}
 E_2\frac{z^{(2)}_0\arctan z^{(2)}_0}{1+(z^{(2)}_0)^2}>0,
\]
where \(G_1\) is independent of \(z^{(1)}_0\). These contractions
follow from conditional Gaussian averaging: bounded forward features
and gates preserve the vanishing projection error in (4); the remaining
second-moment contractions pass by Cauchy–Schwarz. Consequently
\[
\gamma_1:=E_1[\beta_1^2]>0,\quad
\gamma_2:=m_1E_2[\beta_2^2]>0,\quad
\gamma_3:=m_2E_3[\beta_3^2]>0,\quad
\Gamma=\gamma_1+\gamma_2+\gamma_3>0.                     \tag{6}
\]
For example \(\gamma_1=E_1[\phi'(z^{(1)}_0)^2
\{c_2^2\phi(z^{(1)}_0)^2+\sigma_2^2\}]>0\).
Adjunction in (3) gives
\[
E_2[\beta_2V_2]=\gamma_2+\gamma_1>0,\qquad
E_3[\beta_3V_3]=\Gamma>0.
\]
Thus every \(V_\ell\ne0\) in \(L^2\); since \(\phi'(z)>0\)
for every finite \(z\), every \(\phi'(z^{(\ell)}_0)V_\ell\ne0\).

At zero population readout, every \(\delta^{(\ell)}_0=0\), so all
initial hidden velocities vanish. Under C, integration of (1) and strong continuity yield
\(W^{(4)}(s)/s\to h^{(3)}_0\) and
\(\delta^{(\ell)}(s)/s\to\beta_\ell\) in \(L^2\).
For rigor, if \(x_s\to x_0\) in probability, \(u_s\to u_0\) in
\(L^2\), and \(g\) is bounded continuous, then
\(g(x_s)u_s\to g(x_0)u_0\) in \(L^2\): separate \(u_s-u_0\),
truncate the fixed \(u_0\), and use bounded convergence in probability.
Applied to the integral difference quotient of \(\phi\), this also
proves the chain rule along these curves, without assuming Fréchet
differentiability of \(\phi:L^2\to L^2\).
In particular the exact identities
\[
\frac{dz^{(2)}}{ds}
 =E_1[(h^{(1)})^2]\delta^{(2)}
  +W^{(2)}[\phi'(z^{(1)})\delta^{(1)}],\qquad
\frac{dz^{(3)}}{ds}
 =E_2[(h^{(2)})^2]\delta^{(3)}
  +W^{(3)}\left[\phi'(z^{(2)})\frac{dz^{(2)}}{ds}\right]
\]
give, in \(L^2\),
\[
\begin{aligned}
\frac{dz^{(\ell)}}{ds}&=sV_\ell+o(s),&
z^{(\ell)}(s)-z^{(\ell)}_0&=\tfrac12s^2V_\ell+o(s^2),\\
\frac{dh^{(\ell)}}{ds}&=s\phi'(z^{(\ell)}_0)V_\ell+o(s),&
h^{(\ell)}(s)-h^{(\ell)}_0
 &=\tfrac12s^2\phi'(z^{(\ell)}_0)V_\ell+o(s^2).
\end{aligned}                                                    \tag{7}
\]
Also \(W^{(\ell)}(s)-W^{(\ell)}_0
=\tfrac12s^2\beta_\ell\otimes h^{(\ell-1)}_0+o(s^2)\)
in Hilbert–Schmidt norm for \(\ell=2,3\); explicitly,
\(\|W^{(\ell)}(s)-W^{(\ell)}_0\|_{\rm HS}^2
=s^4\gamma_\ell/4+o(s^4)\). Only the increments need be
Hilbert–Schmidt. The readout has the nonzero first-order term
\(sh^{(3)}_0\). Hence no trained block has been frozen.

The four population kernel blocks are
\[
\kappa_1=E_1[(\delta^{(1)})^2],\quad
\kappa_2=E_1[(h^{(1)})^2]E_2[(\delta^{(2)})^2],\quad
\kappa_3=E_2[(h^{(2)})^2]E_3[(\delta^{(3)})^2],\quad
\kappa_4=E_3[(h^{(3)})^2].
\]
They are the limits sought for, respectively,
\((\|\delta^{(1)}\|_2/\sqrt n)^2\),
\((\|\delta^{(2)}\|_2/\sqrt n)^2(\|h^{(1)}\|_2/\sqrt n)^2\),
\((\|\delta^{(3)}\|_2/\sqrt n)^2(\|h^{(2)}\|_2/\sqrt n)^2\),
and \((\|h^{(3)}\|_2/\sqrt n)^2\).
Equations (6)–(7) imply
\[
\kappa_\ell(s)=\gamma_\ell s^2+o(s^2)\ (\ell=1,2,3),\qquad
\kappa_4(s)=m_3+\Gamma s^2+o(s^2),\qquad
\frac{d\kappa_4}{ds}=2\Gamma s+o(s).                    \tag{8}
\]
The output coefficient is exactly
\(E_3[h^{(3)}_0\phi'(z^{(3)}_0)V_3]=\Gamma\), so the output
kernel itself is strictly increasing for sufficiently small positive
feature time, not merely the sum of the hidden kernels.

Define \(\kappa=\sum_{\ell=1}^4\kappa_\ell\).
With \(f=E_3[W^{(4)}h^{(3)}]\), (1) gives \(df/ds=\kappa\)
by the displayed chain rules and adjunction. Thus
\(f(s)=m_3s+o(s)\); the physical clock
\(ds/dt=2(1-f)\) satisfies \(s(t)=2t+o(t)\). Consequently
\[
h^{(\ell)}(t)-h^{(\ell)}_0
=2t^2\phi'(z^{(\ell)}_0)V_\ell+o(t^2),\quad
\kappa_4(t)=m_3+4\Gamma t^2+o(t^2),\quad
\sum_\ell\kappa_\ell(t)=m_3+8\Gamma t^2+o(t^2).
\]
Each hidden kernel is \(4\gamma_\ell t^2+o(t^2)>0\) initially.
For completeness each hidden feature has integrated squared speed
\[
\int_0^T E_\ell\!\left[\left(\frac{dh^{(\ell)}}{dt}\right)^2\right]dt
=\frac{16}{3}E_\ell[(\phi'(z^{(\ell)}_0)V_\ell)^2]T^3+o(T^3)>0
\]
for small \(T>0\). All coefficients are fixed population quantities.

## 3. No affine collapse at any finite reached time

Here is the precise R1 representation used, with \(k\Delta\le S\):
\[
\begin{aligned}
F(z^{(1)}_k)&=F(z^{(1)}_0)+\Delta\sum_{r<k}q^{(1)}_r,\\
z^{(\ell)}_k&=\xi^{(\ell)}_k+
      \sum_{j<k}a^{(\ell)}_{kj}\delta^{(\ell)}_j
                       &&(\ell=2,3),\\
q^{(\ell-1)}_k&=\zeta^{(\ell-1)}_k+
      \sum_{j\le k}b^{(\ell)}_{kj}h^{(\ell-1)}_j
                       &&(\ell=2,3),\\
h^{(\ell)}_k&=\phi(z^{(\ell)}_k),\qquad
W^{(4)}_k=\Delta\sum_{r<k}h^{(3)}_r,\\
\delta^{(3)}_k&=W^{(4)}_k\phi'(z^{(3)}_k),\qquad
\delta^{(2)}_k=\phi'(z^{(2)}_k)\tau_R(q^{(2)}_k).
\end{aligned}                                                    \tag{9}
\]
Here \(\tau_R(q)=q\) for \(|q|\le R\),
\(|\tau_R(q)|\le|q|\), and \(|\tau_R'|\le1\); clipping is only
an auxiliary proof device. The centered Gaussian groups
\(\xi^{(2)},\xi^{(3)},\zeta^{(1)},\zeta^{(2)}\) are mutually
independent and independent of \(z^{(1)}_0\), with arbitrary temporal
correlations within a group and covariances
\[
E[\xi^{(\ell)}_k\xi^{(\ell)}_j]
 =E_{\ell-1}[h^{(\ell-1)}_kh^{(\ell-1)}_j],\quad
E[\zeta^{(\ell-1)}_k\zeta^{(\ell-1)}_j]
 =E_\ell[\delta^{(\ell)}_k\delta^{(\ell)}_j].
\]
The deterministic coefficients retain both trained and response terms:
\[
\begin{aligned}
a^{(\ell)}_{kj}
 &=E\frac{\partial h^{(\ell-1)}_k}{\partial\zeta^{(\ell-1)}_j}
   +\Delta E[h^{(\ell-1)}_kh^{(\ell-1)}_j],&& j<k,\\
b^{(\ell)}_{kj}
 &=E\frac{\partial\delta^{(\ell)}_k}{\partial\xi^{(\ell)}_j}
   +\Delta\mathbf1_{j<k}E[\delta^{(\ell)}_k\delta^{(\ell)}_j],&& j\le k.
\end{aligned}                                                    \tag{10}
\]
Derivatives are of the explicit scalar program holding deterministic
coefficients and covariances fixed; formal source coordinates remain
distinct even for singular covariance. In particular the current terms
\(j=k\) in backward rows are retained.

We prove uniform positive probabilities of both tails; an interval
support or a density theorem is unnecessary. Let
\(\overline\Phi(x)=P(G\ge x)\) for standard Gaussian \(G\).
Since \(b<h^{(\ell)}_k<a\),
\[
b^2\le\operatorname{Var}(\xi^{(\ell)}_k)\le a^2,
\quad |\delta^{(3)}_k|\le\varepsilon aS,
\quad \operatorname{Var}(\zeta^{(2)}_k)\le\varepsilon^2a^2S^2.
\]
For layer 3, (2) and (9) give
\(|z^{(3)}_k-\xi^{(3)}_k|\le C_3:=A\varepsilon aS^2
=63/160<0.4\).
The correction need not be independent of the Gaussian. For either
sign and every \(u>0\), the pointwise bound gives
\[
P(\pm z^{(3)}_k\ge u)
 \ge\overline\Phi((u+C_3)/b)>0.                         \tag{11}
\]

For layer 2, \(|q^{(2)}_j|\le|\zeta^{(2)}_j|+a\). Put
\(Q=\varepsilon aS+a=161/120\); then
\(\|q^{(2)}_j\|_{L^2}\le Q\) and
\(\|\delta^{(2)}_j\|_{L^2}\le\varepsilon Q\). Hence
\[
|z^{(2)}_k-\xi^{(2)}_k|
 \le R_{2,k}:=A\varepsilon\Delta\sum_{j<k}
                  (|\zeta^{(2)}_j|+a),\qquad
ER_{2,k}\le A\varepsilon SQ=483/1600<0.302.
\]
Markov's inequality gives
\(P(R_{2,k}\le1)\ge1117/1600>0.698\). This dominating variable
depends only on the \(\zeta^{(2)}\) source group and deterministic
coefficients, hence is independent of \(\xi^{(2)}_k\).
The actual correction may depend on \(\xi^{(2)}\); we never assume
otherwise. Intersecting independent events gives
\[
P(\pm z^{(2)}_k\ge u)
 \ge\frac{1117}{1600}\overline\Phi((u+1)/b)>0.         \tag{12}
\]

For layer 1 the covariance formula gives
\(\|\zeta^{(1)}_j\|_{L^2}=\|\delta^{(2)}_j\|_{L^2}
\le\varepsilon Q\). Thus
\[
|F(z^{(1)}_k)-F(z^{(1)}_0)|
\le R_{1,k}:=\Delta\sum_{j<k}|\zeta^{(1)}_j|+aS,
\qquad ER_{1,k}\le S(\varepsilon Q+a)=1561/800<2.
\]
This bound is independent of \(z^{(1)}_0\), and
\(P(R_{1,k}\le4)\ge1/2\). Intersect that event with
\(F(z^{(1)}_0)\ge F(u)+4\), or its negative counterpart.
Since \(F\) is increasing and odd,
\[
P(\pm z^{(1)}_k\ge u)
 \ge\tfrac12\overline\Phi\!\left(F^{-1}(F(u)+4)\right)>0. \tag{13}
\]
No temporal independence, continuous-time Gaussian process construction,
or supremum over a Gaussian path has been used.

The bounds (11)–(13) are independent of mesh, clipping, and time
index. They survive every weak limit: for the closed sets
\([u,\infty)\) and \(( -\infty,-u]\), weak convergence gives
limiting probability at least the limsup of the approximating
probabilities. This applies also to indices approaching any fixed
feature time. Every such limiting hidden law therefore has unbounded
support in both directions; in particular it cannot collapse to one
or two points or a bounded affine patch.

There is also a positive-time backward corollary under C and C_b.
Fix \(s>0\). Since \(W^{(4)}(s)=\int_0^s h^{(3)}(v)\,dv\ge bs\)
and \(\phi'(z^{(3)}(s))>0\) almost surely,
\(E_3[\delta^{(3)}(s)^2]>0\). Along approximating mesh indices
\(k\Delta\to s\), weak convergence and truncation of \(x^2\)
give
\[
\liminf E[(\delta^{(3)}_k)^2]\ge E_3[\delta^{(3)}(s)^2]>0.
\]
Choose an eventual positive lower bound \(v_3\) for the source
variances \(\operatorname{Var}(\zeta^{(2)}_k)=E[(\delta^{(3)}_k)^2]\).
Since \(|q^{(2)}_k-\zeta^{(2)}_k|\le a\),
\(P(\pm q^{(2)}_k\ge u)\ge
\overline\Phi((u+a)/\sqrt{v_3})>0\) for \(u>0\).
Passing closed tails shows \(q^{(2)}(s)\) has unbounded support.
Thus \(\delta^{(2)}(s)=\phi'(z^{(2)}(s))q^{(2)}(s)\ne0\)
in \(L^2\). Applying the same lower-semicontinuity argument to
\(E[(\delta^{(2)}_k)^2]=\operatorname{Var}(\zeta^{(1)}_k)\)
and using \(|q^{(1)}_k-\zeta^{(1)}_k|\le a\) proves unbounded
support of \(q^{(1)}(s)\) and \(\delta^{(1)}(s)\ne0\).
This uses the sequential implication from layer 3 to layer 2 to layer 1,
without presupposing nonzero lower backward fields.

Consequently all four kernel blocks are positive for every \(s>0\).
The exact identities following (7)'s derivation also give
\[
E_2\!\left[\delta^{(2)}\frac{dz^{(2)}}{ds}\right]
=\kappa_2+\kappa_1>0,\qquad
E_3\!\left[\delta^{(3)}\frac{dz^{(3)}}{ds}\right]
=\kappa_3+\kappa_2+\kappa_1>0.
\]
Together with \(dz^{(1)}/ds=\delta^{(1)}\) and \(\phi'>0\),
these imply nonzero preactivation and feature velocities in every hidden
layer at every positive reached time. Strict output-kernel increase is
asserted only on the initial interval established in (8).

For any one of these square-integrable preactivations \(z\),
\(\operatorname{Var}(z)>0\), and minimizing first over the intercept
and then over the slope gives
\[
\mathcal E(z):=\inf_{\alpha,\beta\in\mathbb R}
 E[(\phi(z)-\alpha z-\beta)^2]
 =\operatorname{Var}(\phi(z))
  -\frac{\operatorname{Cov}(z,\phi(z))^2}{\operatorname{Var}(z)}>0. \tag{14}
\]
To prove strictness, the quadratic minimization attains its minimum.
If it were zero, boundedness of \(\phi(z)\) and the unbounded support
of \(z\) would force the minimizing slope to be zero. Strict
monotonicity of \(\phi\) would then force \(z\) to be constant,
contradicting (11)–(13). Thus (14) excludes effective affinity under
the actual law, not just affinity of the formula on an abstract interval.

Under C the moments in (14) are continuous in time: \(L^2\)
continuity of \(z\), bounded Lipschitz \(\phi\), and
Cauchy–Schwarz give continuity of every displayed covariance and
variance. Hence, on each compact physical interval on which the flow
is reached, \(\min_{\ell=1,2,3}\min_{0\le t\le T}
\mathcal E(z^{(\ell)}(t))>0\).

If C holds on \([0,S]\), all finite physical horizons are reached
inside it. Indeed \(df/ds=\kappa\ge\kappa_4\ge b^2\),
\(f(0)=0\), and \(b^2S=25/24>1\). There is a unique
\(s_*\le b^{-2}=36/25<S\) with \(f(s_*)=1\).
The continuous kernel is bounded on \([0,s_*]\), and along the
physical clock
\[
1-f(s(t))=\exp\!\left(-2\int_0^t\kappa(s(v))\,dv\right)>0.
\]
Thus the clock cannot reach \(s_*\) at finite \(t\); its bounded
locally Lipschitz right-hand side continues it for all finite times.
The non-affinity conclusion consequently holds on every finite physical
horizon, conditional on C, without a lower bound uniform as \(t\to\infty\).

## 4. Width-limit meaning and remaining obligations

Once the main joint path/second-moment and kernel convergence is proved
for finite GF and exact raw GD, (7)–(8) imply, for either sequence,
\[
\left(\frac{\|h^{(\ell)}_n(t)-h^{(\ell)}_n(0)\|_2}{\sqrt n}\right)^2
 \xrightarrow[n\to\infty]{P}
 4t^4E_\ell[(\phi'(z^{(\ell)}_0)V_\ell)^2]+o(t^4)>0,
\]
and \(\kappa_{4,n}(t)-\kappa_{4,n}(0)\to
4\Gamma t^2+o(t^2)>0\), for every sufficiently small fixed
\(t>0\). The order is width first, then the small-time expansion;
neither coefficient contains a width-vanishing factor. The finite
readout has \(E[\|W^{(4)}_0\|_2^2/n]=n^{-2}\), explaining the
zero population initial value, but dynamical transfer of that small
initialization is still part of the main convergence proof.

Remaining obligations are precisely the arctan-offset versions of R1,
the uniform rows R2, construction/identification and uniqueness of C,
the additional backward identification C_b for its stated corollary,
and the full joint width/flow/raw-GD bridge with all required observables.
This sidecar supplies no response bootstrap and does not certify that
those obligations have been discharged. Conditional on them, nontrivial
population feature learning, strict initial output-kernel change, and
absence of finite-time affine collapse have the derivations above.

Source scope: the contract `ACTIVATION_DESIGN_CONTRACT.md` in this directory
and `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md`,
especially lines 211–451 (representation), 456–617 (actions),
1748–1917 (gradient identities), and 1919–2322 (old nonlinearity proof),
were read. The latter file has SHA256
`f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4`.
Its original-activation nontriviality conclusions are not invoked for
this candidate; the offset-dependent signs and finite-time argument
are derived here. No simulation, repository modification, other agent,
or source-task communication was used.
