# Canonical order-one features separate every finite antipodal-free input set

This is an independently derived, frozen candidate for the exact Gaussian
population closure at order `p=N=1`. Its scientific inputs were only the complete
lines 13161–13786 of `docs/global_nonlinear.md` (parts B/C.1, including H3.1,
H3.N1 and H3.CS7) and the complete `docs/NOTATION.md`. No other study, route,
previous initialization result, experiment or external scientific source was used.
The required proof and research skills and shared workflow were read.

The source-slice SHA-256 is
`0a00ff65642c57068bc3cbf8dcda5a3024edd8e12213a521168fb4db9b303bb1`;
the notation SHA-256 is
`199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b`.
HEAD at startup was `bcee9782651c34ae1204d37186e5c57e9282b273`.
This author owns only this file and made no Git-index changes.

Claim type: exact theorem with a complete argument below. Check status: author
algebraic and analytic audit; this is a research candidate, not promoted material
or an independent review. The theorem concerns initialization and represented
readouts, and does not assert a nonlinear training endpoint or all-time behavior.

## Statement and scope

Use normalized input directions \(u=x/\sqrt2\in S^1\), the canonical correlated
Gaussian marks, the actual contraction \(D=L_2^{-1}CL_1^{-T}\), and the prescribed
ridge \(\eta=\eta_1=1/4096\). Keep \(w=g\), \(M=D\), and write \(H_0(u)\) for the
upper activation field. Initially the readout is \(c=0\).

**Theorem.** For every finite list \(u_1,\ldots,u_m\in S^1\) satisfying

\[
u_a\ne u_b,\qquad u_a\ne-u_b\quad(a\ne b),
\]

the fields \(H_0(u_a)\) are linearly independent in the exact upper-population
\(L^2\) space. Consequently

\[
K_{ab}=E_2[H_0(u_a)H_0(u_b)]
\]

is positive definite. For any strictly positive training weights \(\omega_a\),
the weighted matrix
\(\operatorname{diag}(\sqrt\omega)K\operatorname{diag}(\sqrt\omega)\)
is also positive definite. The same independence holds after adjoining any query
\(u_*\notin\{\pm u_1,\ldots,\pm u_m\}\).

For every real label vector \(y\) and every real prescribed query value \(t\),
there is a bounded readout \(c_t\) at these same fixed hidden parameters satisfying

\[
E_2[c_tH_0(u_a)]=y_a,\qquad E_2[c_tH_0(u_*)]=t.
\]

Thus finite labels do not uniquely determine the represented predictor, even
with both hidden layers frozen at canonical order-one initialization. This does
not say that canonical gradient flow has multiple solutions or can reach every
such readout. The argument uses no time evolution or limiting interchange.

The proof first derives the exact raw contraction, then proves strict monotonicity
of its effective scalar input map, then proves independence of the resulting
tanh fields, and finally constructs the readouts by a positive Gram matrix.

## 1. Exact correlated contraction before reduction

Let \(g_1,g_2\) be independent standard Gaussians. In the lower population set

\[
h_i=\tanh g_i,\quad P_i=\zeta_i+\alpha h_i,\quad T_i=\tanh P_i,
\]

where \(\zeta_1,\zeta_2\) are independent \(N(0,\tau)\) and independent of \(g\).
The upper population is separate: \(\xi_1,\xi_2\) are independent \(N(0,v)\),
and \(Z_i=\tanh\xi_i\). Here

\[
v=E\tanh^2G,\quad \tau=E\tanh^2(\sqrt vG),\quad\alpha=1-\tau,
\]

with \(G\sim N(0,1)\). Define scalar moments in one lower coordinate by

\[
\gamma=ET_i^2,\quad\delta=E(1-T_i^2)=1-\gamma,
\quad\beta=E[h_iT_i].
\]

All of \(v,\tau,\alpha,\gamma,\delta\) are strictly positive; later we also
prove \(0<\beta\le\alpha v\). The raw lists, in their prescribed order, are

\[
\psi_1=(1,h_1,h_2,T_1,T_2)^T,\qquad\psi_2=(1,Z_1,Z_2)^T.
\]

Independence of the two lower coordinate pairs and their centered oddness give

\[
G_1=\begin{pmatrix}
1&0&0&0&0\\
0&v&0&\beta&0\\
0&0&v&0&\beta\\
0&\beta&0&\gamma&0\\
0&0&\beta&0&\gamma
\end{pmatrix},\qquad G_2=\operatorname{diag}(1,\tau,\tau).
\]

Use the exact identity H3.1/H3.CS7:

\[
E_2[B A_0F]=\sum_iE_1[Fh_i]E_2[\partial_{\xi_i}B]
 +\sum_iE_1[\partial_{\zeta_i}F]E_2[BZ_i].                 \tag{1}
\]

For \(B=Z_j\), the upper expectations in (1) are
\(E_2\partial_{\xi_i}Z_j=\alpha\mathbf1_{i=j}\) and
\(E_2[Z_jZ_i]=\tau\mathbf1_{i=j}\). Lower derivatives are zero for \(h_i\),
and \(E_1\partial_{\zeta_j}T_i=\delta\mathbf1_{i=j}\). Thus

\[
C=\begin{pmatrix}
0&0&0&0&0\\
0&\alpha v&0&\alpha\beta+\tau\delta&0\\
0&0&\alpha v&0&\alpha\beta+\tau\delta
\end{pmatrix}.                                                \tag{2}
\]

The first row and column vanish by the centered oddness in (1). In particular,
the response contribution \(\tau\delta\), the correlation \(\beta\), and the
joint marks \((g,\zeta)\) are retained.

Let \(R_\ell=G_\ell+\eta I=L_\ell L_\ell^T\). With
\(a(u)=L_1^{-1}E_1[\psi_1\tanh(g\cdot u)]\), the initialized preactivation is
exactly

\[
\begin{split}
b_2^TD a(u)
 &=\psi_2^TL_2^{-T}L_2^{-1}C
                 L_1^{-T}L_1^{-1}E_1[\psi_1\tanh(g\cdot u)]\\
 &=\psi_2^TR_2^{-1}CR_1^{-1}E_1[\psi_1\tanh(g\cdot u)].       \tag{3}
\end{split}
\]

This checks the right transpose in \(D\) directly. Define

\[
\begin{split}
\Delta&=(v+\eta)(\gamma+\eta)-\beta^2>0,\\
A&=\frac{\alpha v(\gamma+\eta)-\beta(\alpha\beta+\tau\delta)}{\Delta},\\
B&=\frac{\alpha\eta\beta+\tau\delta(v+\eta)}{\Delta}.       \tag{4}
\end{split}
\]

These are the two entries of
\([\alpha v,\alpha\beta+\tau\delta]
\left(\begin{smallmatrix}v+\eta&\beta\\\beta&\gamma+\eta\end{smallmatrix}\right)^{-1}\).
Positivity of \(\Delta\) follows since that matrix is a covariance matrix plus
strictly positive ridge. No sign of \(A\) is assumed.

Set

\[
m(s)=E_\zeta\tanh(\zeta+s),\quad
\chi(g)=A\tanh g+B m(\alpha\tanh g).
\]

The function \(m\) is odd and smooth; its derivative
\(J(s)=E_\zeta\operatorname{sech}^2(\zeta+s)\) lies in \((0,1]\).
All differentiations here are allowed by bounded tanh derivatives. For
\(-1\le t\le1\), let \(G,V\) be independent standard Gaussians and define

\[
F(t)=\frac{1}{\tau+\eta}
 E\big[\chi(G)\tanh(tG+\sqrt{1-t^2}V)\big].                \tag{5}
\]

Conditioning first on \(g\) in (3), and using
\(g\cdot u=u_i g_i+u_{3-i}g_{3-i}\) with \(u_{3-i}^2=1-u_i^2\), now gives

\[
H_0(u)=\tanh\big(F(u_1)Z_1+F(u_2)Z_2\big).              \tag{6}
\]

Changing the sign of \(u_{3-i}\) does not change that conditional Gaussian law.
Equation (6) is therefore derived from the correlated contraction, rather than
assumed as a simplified independent initialization.

## 2. The effective scalar map is strictly increasing

We prove \(\chi'(g)>0\) first. Gaussian integration by parts gives

\[
1-v=E[G\tanh G]>E\tanh^2G=v,
\]

because \(G\tanh G>\tanh^2G\) for \(G\ne0\). Thus \(0<v<1/2\).
Since \(v<1\), pointwise comparison gives \(0<\tau<v\), so
\(1/2<\alpha<1\). A second integration by parts and Cauchy–Schwarz give

\[
E[\xi\tanh\xi]=v\alpha,\qquad v^2\alpha^2\le v\tau,
\qquad \alpha^2v\le\tau.                                \tag{7}
\]

Gaussian boundary terms vanish because tanh is bounded and Gaussian densities
decay; the derivatives used above are bounded.

Since \(m(0)=0\) and \(0<m'\le1\), for nonzero \(h\)
\(0<h m(\alpha h)\le\alpha h^2\). Hence

\[
0<\beta=E[h m(\alpha h)]\le\alpha v.                    \tag{8}
\]

We need a uniform derivative bound that does not assume \(A\ge0\). Let
\(s_0=1+2\tau=3-2\alpha\) and put

\[
\lambda=s_0^{-1/2}e^{-\alpha^2/s_0}.
\]

The inequality \(\log\cosh z\le z^2/2\) follows by integrating
\(\tanh z\le z\) on the positive half-line and then using evenness. Therefore
\(\operatorname{sech}^2z\ge e^{-z^2}\). Completing the Gaussian square yields

\[
J(s)\ge s_0^{-1/2}e^{-s^2/s_0}\ge\lambda\quad(|s|\le\alpha).
\]

Conditioning on \(h\) and applying Jensen to the convex exponential similarly
gives

\[
\delta\ge s_0^{-1/2}E e^{-\alpha^2h^2/s_0}
          \ge s_0^{-1/2}e^{-\alpha^2v/s_0}.                \tag{9}
\]

These elementary bounds imply

\[
\delta+\lambda>1.                                      \tag{10}
\]

Here are explicit estimates proving (10), so no numerical Gaussian integration
is hidden in this step. If \(1/2<\alpha\le3/4\), then
\(3/2\le s_0<2\), \(v<1/2\), and (9) gives

\[
\delta+\lambda\ge\frac{e^{-3/16}+e^{-3/8}}{\sqrt2}
 \ge\frac{23}{16\sqrt2}>1.
\]

We used \(e^{-r}\ge1-r\) and \(23^2>2\cdot16^2\). If \(3/4\le\alpha<1\),
then \(\tau\le1/4\), \(s_0\le3/2\), and (7)–(9) give

\[
\delta\ge\sqrt{2/3}\,e^{-1/6}\ge\frac56\sqrt{2/3}.
\]

Also \(\lambda\ge e^{-1}>1/3\): indeed \(\alpha^2\le1\), and
\(-\tfrac12\log s-1/s\) is increasing on \(1\le s\le2\), with value \(-1\)
at \(s=1\). The elementary series estimate \(e<3\) supplies the last inequality.
Since \(\sqrt{2/3}>4/5\), their sum exceeds one. This proves (10).

The centered variables \(h\) and \(\zeta\) are orthogonal, of squared norms
\(v\) and \(\tau\), and integration by parts gives \(E[T\zeta]=\tau\delta\).
Expanding the nonnegative squared norm of
\(T-(\beta/v)h-\delta\zeta\) therefore proves

\[
\gamma\ge\beta^2/v+\tau\delta^2.                         \tag{11}
\]

From (4), (8) and (11), \(B>0\), and

\[
\begin{split}
\Delta-\delta\,[\alpha\eta\beta+\tau\delta(v+\eta)]
 &\ge\eta[\beta^2/v+v+\eta-\alpha\beta\delta]>0.
\end{split}
\]

The strict last sign uses \(\alpha\beta\delta\le\alpha^2v\delta\le v\) and
\(\eta>0\). Thus \(0<B<1/\delta\). The first coordinate of the defining row
identity in (4) is \(A(v+\eta)+B\beta=\alpha v\). For \(|s|\le\alpha\), it gives

\[
\begin{split}
A+\alpha B J(s)
 &=\frac{\alpha v+B[\alpha(v+\eta)J(s)-\beta]}{v+\eta}\\
 &\ge\frac{\alpha}{v+\eta}
      \{v[1-B(1-J(s))]+\eta BJ(s)\}\\
 &\ge\frac{\alpha v}{(v+\eta)\delta}(\delta+\lambda-1)>0. \tag{12}
\end{split}
\]

Here \(0<J\le1\), \(B\le1/\delta\), and \(J\ge\lambda\) justify the final
inequality. Consequently

\[
\chi'(g)=\operatorname{sech}^2g\,[A+\alpha B J(\alpha\tanh g)]>0.
\]

For \(-1<t<1\), differentiating (5) and integrating by parts once in each of
\(G,V\) cancels the terms involving the second derivative of tanh and gives

\[
F'(t)=\frac1{\tau+\eta}
 E\big[\chi'(G)\operatorname{sech}^2(tG+\sqrt{1-t^2}V)\big]>0.       \tag{13}
\]

For clarity, before integration by parts the derivative is the expectation of
\(\chi(G)\operatorname{sech}^2(Y)[G-tV/\sqrt{1-t^2}]\), where
\(Y=tG+\sqrt{1-t^2}V\). The \(G\) integration produces
\(E[\chi'(G)\operatorname{sech}^2Y]+tE[\chi(G)(\tanh)''(Y)]\), and the \(V\)
integration cancels the second term. Bounded derivatives and Gaussian first
moments justify differentiation on compact subintervals of \((-1,1)\).

Dominated convergence makes \(F\) continuous at both endpoints. The strict
interior inequality then makes \(F\) strictly increasing on all of \([-1,1]\):
between any two distinct endpoints or interior points one can choose two
interior points with a strict difference. Oddness of \(\chi\), symmetry of \(V\),
and (5) give \(F(-t)=-F(t)\). In particular, \(F(t)=0\) exactly when \(t=0\).

## 3. Independence of all finite non-antipodal families

Write \(r(u)=(F(u_1),F(u_2))\). Strict monotonicity implies that \(r\) is injective,
\(r(-u)=-r(u)\), and \(r(u)\ne0\) for \(u\in S^1\). Thus distinct directions modulo
antipodes give nonzero vectors \(r_a=r(u_a)\) with \(r_a\ne\pm r_b\).

The law of \(Z=(\tanh\xi_1,\tanh\xi_2)\) has a positive density everywhere on
\((-1,1)^2\): the Gaussian density is positive and coordinatewise tanh has a
smooth inverse there. If

\[
\sum_{a=1}^m d_a\tanh(r_a\cdot Z)=0\quad\text{in }L^2,
\]

continuity and positivity of this density force the same identity at every point
of the open square. Otherwise a neighborhood of a point with nonzero value
would have positive probability.

Choose \(q\in\mathbb R^2\) such that all \(r_a\cdot q\) are nonzero and have
distinct absolute values. This excludes only finitely many lines, namely the
orthogonal complements of \(r_a\), \(r_a-r_b\), and \(r_a+r_b\), all of which
are nonzero vectors. Explicitly, \(q=(1,z)\) works after excluding finitely many
real values of \(z\); a vector with zero second coordinate imposes no excluded
value because its first coordinate is nonzero.

Restrict the identity to \(Z=tq\) for small real \(t\). Each term is real analytic
for every real \(t\), so the identity extends to all \(t\in\mathbb R\). The
one-variable continuation used here is elementary: at a finite endpoint of an
interval where an analytic function is zero, continuity of every derivative
forces all Taylor coefficients to vanish and extends the zero interval.

Put \(s_a=|r_a\cdot q|>0\) and \(e_a=d_a\operatorname{sign}(r_a\cdot q)\).
Reorder the distinct numbers so that \(s_1<\cdots<s_m\). We have

\[
\sum_a e_a\tanh(s_at)=0\quad(t\in\mathbb R),\qquad\sum_a e_a=0,
\]

where the second equality is the limit as \(t\to+\infty\). Subtract it from the
first equality, multiply by \(e^{2s_1t}\), and use the exact formula

\[
\tanh(st)-1=-\frac{2}{e^{2st}+1}.
\]

The limit is \(-2e_1=0\). Remove that term and repeat with the smallest remaining
\(s_a\). All \(e_a\), hence all \(d_a\), are zero. This proves the independence.

For any nonzero vector \(z\in\mathbb R^m\),

\[
z^TKz=E_2\left(\sum_a z_aH_0(u_a)\right)^2>0.
\]

The weighted assertion follows by substituting
\(z=\operatorname{diag}(\sqrt\omega)v\), which is nonzero whenever \(v\ne0\).
Adjoining the stated query still satisfies the same pairwise conditions, so its
augmented Gram matrix is positive definite as well.

## 4. Explicit readout-nullspace interpolants

Let \(H_a=H_0(u_a)\), \(H_*=H_0(u_*)\), and \(k_a=E_2[H_aH_*]\). Define

\[
c_{\mathrm{base}}=\sum_a(K^{-1}y)_aH_a,\qquad
R_*=H_*-\sum_a(K^{-1}k)_aH_a.
\]

Direct substitution gives \(E_2[c_{\mathrm{base}}H_a]=y_a\) and
\(E_2[R_*H_a]=0\). Independence of the augmented family makes \(R_*\ne0\), and

\[
\kappa_*=\|R_*\|_{L^2(E_2)}^2
 =K_0(u_*,u_*)-k^TK^{-1}k>0,\qquad E_2[R_*H_*]=\kappa_*.
\]

For arbitrary \(t\in\mathbb R\), set

\[
c_t=c_{\mathrm{base}}+
       \frac{t-k^TK^{-1}y}{\kappa_*}\,R_* .               \tag{14}
\]

Equation (14) fits the same \(y_a\) at every training direction and gives exactly
\(t\) at \(u_*\). Each \(c_t\) is a finite linear combination of bounded fields,
so it is bounded and belongs to the admissible population readout space. It is
also odd under upper-mark sign reversal, as are all the \(H_0(u)\). All these
states share the same canonical initialized \(w,M\); their readouts differ from
the prescribed initial \(c=0\).

For completeness, any readout fitting the labels is \(c_{\mathrm{base}}+r\), with
\(r\perp\operatorname{span}\{H_1,\ldots,H_m\}\). Orthogonality proves that
\(c_{\mathrm{base}}\) is the unique interpolant of minimum \(L^2(E_2)\) norm.
Thus an additional selection criterion can choose one interpolant; label fitting
alone cannot choose the values in (14).

## Scope checks and limitations

- This is the exact Gaussian population closure with the scheduled positive
  ridge. In fact the proof uses only \(\eta>0\), but no ridge change is needed
  for the stated canonical theorem.
- No finite quadrature rule can inherit the universal finite-set statement
  without a sample-count restriction: with \(P_2\) upper nodes its Gram rank is
  at most \(P_2\). The theorem concerns the exact population integration.
- Antipodal exclusions are necessary: \(H_0(-u)=-H_0(u)\). At a training direction
  or its antipode the query value is fixed by the corresponding label and oddness.
- Positive definiteness for each finite set gives no uniform lower eigenvalue
  bound over sets with arbitrarily close points and no conditioning guarantee.
- The field \(c_t\) in (14) is a represented readout at fixed hidden parameters.
  It is not asserted to be a reachable endpoint of the prescribed nonlinear
  gradient flow or of its zero-initialized frozen-feature comparator.
- The argument proves order one only. Higher-order independence and any
  nonlinear endpoint characterization remain outside this candidate.
- No experiments, code changes, time discretization, neural-width limit,
  promotion action or cross-study scientific retrieval were performed.
