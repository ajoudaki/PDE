# Independent adversarial audit of the actual top positive-curvature bound

Verdict: **PASS for the scoped lemma.**

Candidate: `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/ACTUAL_TOP_POSITIVE_CURVATURE_BOUND.md`

Certified revised candidate SHA256: `af07fcbd7f937206858e942aa2b9e728734db908205112227191d54c1fd09c4c`

Original candidate SHA256: `698cb7888a2891ecb70e91996591ec33fc1650edd3360f136d06edc68d824c7e`. That version received a clean scoped PASS before the clarifications; this historical verdict is preserved.

Original 654-line report SHA256: `7a51fcce0d7d7e408d1cdf2db026abd560a1a01fa0a59e8e8738e39c6cafe1e7`.

The original candidate and the solve-math-rigorously skill at `/etc/codex/skills/solve-math-rigorously/SKILL.md` were read in full during the isolated audit. No ledger, prior review, other proof note, external mathematical source, or experimental result was consulted for that audit. For this final certification, the complete revised candidate (359 lines, 13,418 bytes) was read once and its supplied SHA256 was verified; only this audit's own report was also read. No experiments were performed, and the candidate was not edited during either audit pass.

The revised candidate implements both previously nonblocking clarifications, updates the historical-status wording, and explicitly identifies the prefix variable as feature time. The numbered equations (1)--(16), including (14a)--(14c), and their underlying estimates are unchanged. The clarified conditional second-moment statements are verified in Section 10.

All displayed estimates and the scoped trajectory-existence, probability, expectation, and uniformity assertions are established below for the certified revised candidate. No mathematical correction is required. The last section records the clarifications as resolved and certifies this exact version.

This verdict concerns the dynamics defined by (2), the positive part of the top coefficient, and the stated frozen-upper-weights input Hessian. It does not certify that (2) arises from any unspecified loss or time change. It does not certify a global network theorem, a transported-response estimate, or any assertion about the middle curvature coefficient. Those are outside the candidate's stated scope.

In the network application, the prefix \(t\), horizon \(S\), and trajectory evaluations in (2) use feature time. In particular, the \(t^5\) estimate below is a feature-time estimate; no conversion to physical time is asserted.

## 1. Setup, elementary bounds, and exact masking

Take an integer width \(n\ge1\). The vectors \(z^{(1)},h^{(1)},z^{(2)},h^{(2)},z^{(3)},h^{(3)},W^{(4)},\delta^{(2)},\delta^{(3)}\) belong to \(\mathbb R^n\); the two hidden matrices and \(Q\) are \(n\times n\). Every vector norm below is an ordinary Euclidean or maximum norm, and every matrix norm is an ordinary operator or Frobenius norm. Transposes are finite-dimensional \({}^T\).

For \(\phi(z)=\arctan z\) and \(c=\pi/2\),

\[
\phi'(z)=\frac1{1+z^2},\qquad
\phi''(z)=-\frac{2z}{(1+z^2)^2}.
\]

Thus \(|\phi|\le c\), \(0<\phi'\le1\), \(\phi\) has the sign of its argument, and \(\phi\) is 1-Lipschitz by integrating its derivative. Also \(|\phi''|\le2\): for \(|z|\le1\) this is immediate from the displayed formula, while for \(|z|\ge1\), \(|z|/(1+z^2)^2\le |z|/|z|^4\le1\).

The assumptions on \(\tau\) imply \(\tau(0)=0\), continuity, and

\[
\|\tau(v)\|_2\le\|v\|_2
\quad (v\in\mathbb R^n).
\]

No monotonicity, sign preservation, differentiability, or oddness of \(\tau\) is required. This includes allowed maps that reverse signs. A diagonal zero-one \(Q\) has operator norm at most one and commutes with every diagonal \(D_\ell\).

If \(Q_{ii}=0\), then \(h_i^{(2)}=\delta_i^{(2)}=0\) at all times. Equation (2) consequently gives

\[
((W^{(2)})')_{ij}=0\quad\text{for every }j,
\qquad
((W^{(3)})')_{ji}=0\quad\text{for every }j.
\]

The corresponding row of \(W^{(2)}\) and column of \(W^{(3)}\) are exactly frozen at their stored initial values. Inactive preactivations \(z_i^{(2)}\) need not be frozen, since \(h^{(1)}\) moves; their activation and backward signal are masked. They cannot affect the remaining computation through those frozen rows and columns: the forward contribution is multiplied by \(h_i^{(2)}=0\), and the backward contribution by \(\delta_i^{(2)}=0\). This verifies the claimed fully pruned dynamics without deleting stored parameters or omitting the lower update.

## 2. Existence and deterministic bounds on every trained factor

Write

\[
\varepsilon=\frac{\|W^{(4)}(0)\|_2}{\sqrt n}.
\]

Since \((W^{(4)})'=h^{(3)}\) and \(\|h^{(3)}\|_2\le c\sqrt n\), integration gives

\[
\frac{\|W^{(4)}(s)\|_2}{\sqrt n}
\le\varepsilon+cs,
\qquad
\frac{\|\delta^{(3)}(s)\|_2}{\sqrt n}
\le\varepsilon+cs.
\tag{R1}
\]

For any two vectors \(u,v\), direct summation of squared entries gives

\[
\|uv^T/n\|_{\rm F}^2
=\frac{\|u\|_2^2\|v\|_2^2}{n^2}.
\]

As \(\|h^{(2)}\|_2\le c\sqrt n\),

\[
\|W^{(3)}(s)-W^{(3)}(0)\|_{\rm F}
\le c\int_0^s(\varepsilon+cu)\,du
=c(\varepsilon s+cs^2/2).
\tag{R2}
\]

The operator norm of an increment is at most its Frobenius norm. If \(\varepsilon\le1\), \(s\le S\), and the initial hidden operator norms are at most \(M\), (R2) yields precisely the candidate's

\[
\|W^{(3)}(s)\|_{\rm op}\le K_3
=M+c(S+cS^2/2).
\]

Using the actual clipped and masked definition of \(\delta^{(2)}\),

\[
\begin{aligned}
\|\delta^{(2)}\|_2
&=\|QD_2\tau((W^{(3)})^T\delta^{(3)})\|_2\\
&\le\|(W^{(3)})^T\delta^{(3)}\|_2
\le K_3\|\delta^{(3)}\|_2.
\end{aligned}
\tag{R3}
\]

Therefore

\[
\begin{aligned}
\|W^{(2)}(s)-W^{(2)}(0)\|_{\rm F}
&\le cK_3(\varepsilon s+cs^2/2),\\
\|W^{(2)}(s)\|_{\rm op}
&\le K_2=M+cK_3(S+cS^2/2).
\end{aligned}
\tag{R4}
\]

These are Frobenius bounds on the increments, not width-independent Frobenius bounds on the initial matrices. The candidate makes this distinction correctly.

The first equation of (2) now gives

\[
\frac{\|(z^{(1)})'(s)\|_2}{\sqrt n}
\le K_2K_3(\varepsilon+cs).
\tag{R5}
\]

For arbitrary finite initial data with no restriction \(\varepsilon\le1\), repeat exactly these inequalities with

\[
\begin{aligned}
M_0&=\max(\|W^{(2)}(0)\|_{\rm op},\|W^{(3)}(0)\|_{\rm op}),\\
K_3^{\rm ran}&=M_0+c(\varepsilon S+cS^2/2),\\
K_2^{\rm ran}&=M_0+cK_3^{\rm ran}(\varepsilon S+cS^2/2).
\end{aligned}
\]

In particular, the unrestricted version does not substitute \(1\) for a readout norm exceeding one.

For completeness, existence and uniqueness require no additional regularity of the clipping. In the finite-dimensional state \((z^{(1)},W^{(2)},W^{(3)},W^{(4)})\), the right side of (2) is locally Lipschitz: its constituents are smooth functions, linear maps, products, and the Lipschitz map \(\tau\). An elementary local construction is as follows. In a sufficiently small closed ball about an initial state, bound the vector field by \(B\) and its Lipschitz constant by \(L\). Choose a time interval on which integration of a vector of norm at most \(B\) stays in that ball. Starting with the constant initial path, iterate the integral equation. Successive differences are bounded by

\[
B\frac{L^k s^{k+1}}{(k+1)!},\qquad k\ge0.
\]

Their sum converges uniformly, giving a solution by passage through the integral equation. Iterating the integral inequality for the difference of two solutions gives a bound proportional to \((Ls)^k/k!\), which tends to zero, proving uniqueness.

On every prescribed finite horizon, (R1)--(R5), or their unrestricted versions, bound all state components. At fixed finite width, an operator norm bound bounds each matrix entry. Integration of (R5) bounds \(z^{(1)}\) relative to its finite initial value. A finite terminal time would therefore leave the solution in a compact set on which the vector field is bounded; the solution has a limit at that time and the preceding local construction extends it. Hence there is no finite-time escape, and the trajectory exists uniquely on \([0,S]\). Its coordinates are continuously differentiable because the vector field is continuous.

## 3. Exact actual top velocity, including every trained contribution

Differentiating \(h^{(1)}=\phi(z^{(1)})\) and using the lower update gives

\[
(h^{(1)})'=D_1(z^{(1)})'
=D_1^2(W^{(2)})^T\delta^{(2)}.
\]

The product rule for \(z^{(2)}=W^{(2)}h^{(1)}\) gives

\[
\begin{aligned}
(z^{(2)})'
&=(W^{(2)})'h^{(1)}+W^{(2)}(h^{(1)})'\\
&=\left(\frac{\|h^{(1)}\|_2^2}{n}I
+W^{(2)}D_1^2(W^{(2)})^T\right)\delta^{(2)}.
\end{aligned}
\tag{R6}
\]

Since \(Q\) is fixed, \((h^{(2)})'=QD_2(z^{(2)})'\). The product rule for \(z^{(3)}=W^{(3)}h^{(2)}\) therefore yields

\[
\begin{aligned}
(z^{(3)})'
&=(W^{(3)})'h^{(2)}+W^{(3)}(h^{(2)})'\\
&=\frac{\|h^{(2)}\|_2^2}{n}\delta^{(3)}
+W^{(3)}QD_2(z^{(2)})'.
\end{aligned}
\tag{R7}
\]

Thus (5) is exact. The first term in (R7) is the trained \(W^{(3)}\) contribution. The two terms in (R6) include the trained \(W^{(2)}\) and moving lower feature. The readout is its actual evolving value in \(\delta^{(3)}\). There is no missing derivative of \(\tau\): these calculations differentiate the forward factors once and insert the prescribed velocity, rather than differentiate the backward signal.

The coefficient matrix in (R6) has operator norm at most \(c^2+K_2^2\), so

\[
\frac{\|(z^{(2)})'\|_2}{\sqrt n}
\le(c^2+K_2^2)K_3(\varepsilon+cs).
\]

Using \(\|QD_2\|_{\rm op}\le1\) in (R7) gives

\[
\frac{\|(z^{(3)})'(s)\|_2}{\sqrt n}
\le\bigl[c^2+K_3^2(c^2+K_2^2)\bigr](\varepsilon+cs)
=K(\varepsilon+cs).
\tag{R8}
\]

This proves (6) with exactly (3), including its initial-time factor. Substitution of \(K_2^{\rm ran},K_3^{\rm ran}\) proves the same statement with exactly \(K^{\rm ran}\) in (14a).

## 4. Scalar sign lag without coordinatewise sign agreement

Let \(z\) be absolutely continuous on \([0,t]\), and define \(\bar a,V,U\) as in the candidate. Fix \(v\in[0,t]\). If \(\bar a(v)\phi''(z(v))\le0\), the claimed inequality is immediate. If it is positive, then \(z(v)\ne0\) and \(\bar a(v)z(v)<0\).

Suppose first \(z(v)>0\), \(\bar a(v)<0\). Continuity of \(z\), the sign of \(\phi\), and the negative integral imply that \(z(u)<0\) for some \(u\in[0,v]\). Therefore

\[
|z(v)|=z(v)\le |z(v)-z(u)|
\le\int_u^v|z'(r)|\,dr\le V(v).
\]

Moreover \(v\phi(z(v))\ge0\) has the opposite sign from \(\bar a(v)\), and hence

\[
|\bar a(v)|
\le |v\phi(z(v))-\bar a(v)|
\le\int_0^v|z(v)-z(u)|\,du.
\]

The same conclusions hold when \(z(v)<0\), \(\bar a(v)>0\): a point of positive \(z\) exists earlier, and \(v\phi(z(v))\le0\) again has the opposite sign from \(\bar a(v)\).

In both cases, absolute continuity supplies

\[
\begin{aligned}
\int_0^v|z(v)-z(u)|\,du
&\le\int_0^v\int_u^v|z'(r)|\,dr\,du\\
&=\int_0^v r|z'(r)|\,dr=U(v).
\end{aligned}
\]

The last identity can also be checked directly by integration by parts with \(A(u)=\int_0^u|z'(r)|\,dr\): the double integral is \(vA(v)-\int_0^v A(u)\,du\). Thus no signed interchange or unjustified cancellation is involved.

Consequently, in the positive case,

\[
[\bar a(v)\phi''(z(v))]_+
=\frac{2|\bar a(v)||z(v)|}{(1+z(v)^2)^2}
\le2U(v)V(v)\le2U(t)V(t).
\]

This proves (7), including both sign configurations, zeros, and \(v=0\).

For \(a(v)=a(0)+\bar a(v)\), apply \([x+y]_+\le[x]_++|y|\) and \(|\phi''|\le2\) to obtain

\[
\sup_{0\le v\le t}[a(v)\phi''(z(v))]_+
\le2|a(0)|+2V(t)U(t).
\tag{R9}
\]

The initial term is necessary in this general statement: at \(v=0\), an initial readout with sign opposite to a nonzero \(z(0)\) gives a positive left side, whereas \(V(0)U(0)=0\). This verifies (8), including its caveat.

## 5. Coordinatewise prefix supremum and the exact fifth power

For each top neuron, the actual readout equation is

\[
W_i^{(4)}(v)=W_i^{(4)}(0)+\int_0^v\phi(z_i^{(3)}(u))\,du,
\]

so (R9) applies exactly, without replacing the trained path by an expansion.

The Euclidean integral inequality

\[
\left\|\int f(u)\,du\right\|_2\le\int\|f(u)\|_2\,du
\]

follows by taking the supremum of \(x^T\int f\) over \(\|x\|_2=1\) and using \(|x^Tf|\le\|f\|_2\). Apply it to the vector of absolute top velocities and then to that vector multiplied by time. Equation (R8) gives

\[
\begin{aligned}
\frac{\|V^{(3)}(t)\|_2}{\sqrt n}
&\le K(\varepsilon t+ct^2/2),\\
\frac{\|U^{(3)}(t)\|_2}{\sqrt n}
&\le K(\varepsilon t^2/2+ct^3/3).
\end{aligned}
\tag{R10}
\]

Sum (R9) only after taking each coordinate's supremum. Cauchy--Schwarz gives

\[
\frac1n\sum_iV_i^{(3)}(t)U_i^{(3)}(t)
\le\frac{\|V^{(3)}(t)\|_2\|U^{(3)}(t)\|_2}{n},
\]

and

\[
\frac1n\sum_i|W_i^{(4)}(0)|
\le\frac{\|W^{(4)}(0)\|_2}{\sqrt n}=\varepsilon.
\]

These prove (10). In particular, the proof never replaces a sum of coordinatewise suprema by the generally smaller supremum of a sum.

Expanding its right side gives exactly

\[
2\varepsilon
+K^2\varepsilon^2t^3
+\frac{7c}{6}K^2\varepsilon t^4
+\frac{c^2}{3}K^2t^5.
\tag{R11}
\]

The mixed coefficient is \(2(c/3+c/4)=7c/6\). For exactly zero initial readout, only the last term survives. This proves (11), with coefficient \(K^2c^2/3\), for every \(t\in[0,S]\). The fifth power comes from an integrated \(O(s)\) velocity, giving \(V=O(t^2)\), and its time-weighted integral, giving \(U=O(t^3)\). No small-time remainder, limit interchange, or initial derivative expansion is used. The estimate does not assert that the power is sharp.

## 6. Canonical event and its explicit constants

Under the specified initialization,

\[
\varepsilon=\frac{\|G^{(4)}\|_2}{n\sqrt n}.
\]

On (12), \(\varepsilon\le2/n\), which is at most one for \(n\ge2\). Use \(M=10\) in the deterministic constants. From (R11),

\[
\begin{aligned}
2\varepsilon&\le4/n,\\
K^2\varepsilon^2t^3&\le4K^2S^3/n^2\le2K^2S^3/n,\\
\frac{7c}{6}K^2\varepsilon t^4&\le\frac{7c}{3}K^2S^4/n.
\end{aligned}
\]

For example, (13) holds with

\[
C_S=\max\left\{4+2K^2S^3+\frac{7c}{3}K^2S^4,
\frac{c^2}{3}K^2\right\},
\]

where \(K\) is evaluated at \(M=10\). This verifies that \(C_S\) is independent of width, mask, clipping, and the time prefix.

Here is an independent derivation of (14). A maximal \(1/4\)-separated subset \(\mathcal N\) of the Euclidean unit sphere is a \(1/4\)-net. The open balls of radius \(1/8\) around its points are disjoint and lie in the ball of radius \(9/8\). Volume scaling gives \(|\mathcal N|\le9^n\). This packing bound also ensures a finite maximal set can be constructed.

For a matrix \(A\), choose unit vectors \(x,y\) attaining its bilinear operator norm, and approximate them by \(x_0,y_0\in\mathcal N\). The decomposition

\[
x^TAy-x_0^TAy_0=(x-x_0)^TAy+x_0^TA(y-y_0)
\]

has absolute value at most \(\|A\|_{\rm op}/2\). Consequently

\[
\|A\|_{\rm op}\le2\max_{x_0,y_0\in\mathcal N}|x_0^TAy_0|.
\]

For a canonical hidden matrix and fixed unit vectors \(x_0,y_0\), the bilinear form is a centered Gaussian of variance

\[
\frac1n\sum_{i,j}(x_0)_i^2(y_0)_j^2=\frac1n.
\]

Completing the square in its one-dimensional Gaussian integral gives moment generating function \(e^{\lambda^2/(2n)}\). Applying Markov's inequality and minimizing over \(\lambda>0\) gives

\[
\mathbb P(|x_0^TAy_0|>r/2)\le2e^{-nr^2/8}.
\]

Union over the two nets and two matrices therefore gives

\[
\mathbb P(M_0>r)\le4e^{2n\log9-nr^2/8}.
\tag{R12}
\]

At \(r=10\), this is the first error in (14):

\[
4e^{-(25/2-2\log9)n}.
\]

For a standard Gaussian scalar \(g\), rescaling the Gaussian integral gives \(\mathbb E e^{\lambda g^2}=(1-2\lambda)^{-1/2}\) for \(\lambda<1/2\). Independence of the coordinates gives

\[
\mathbb E e^{\|G^{(4)}\|_2^2/4}=2^{n/2}.
\]

Markov's inequality at \(\|G^{(4)}\|_2^2=4n\) bounds failure of the readout event by

\[
e^{-n}2^{n/2}=e^{-(1-\frac12\log2)n}.
\]

The union bound gives exactly (14). Both exponents are strictly positive. No initial bound on \(z^{(1)}\) is needed, since the deterministic proof already covers arbitrary finite lower initial state; the canonical Gaussian state is finite almost surely. No claim about a Gaussian trained law was used.

## 7. Unconditional polynomial moments and expectation

The unrestricted constants in (14a) are polynomials in the two nonnegative variables \(M_0,\varepsilon\), with coefficients depending only on \(S\) and \(c\). The unrestricted deterministic proof above proves (10) with \(K^{\rm ran}\) on every finite initial state, including the complement of (12).

For \(r\ge10\), \(r^2/16\ge2\log9\). Thus (R12) implies, for all \(n\ge1\),

\[
\mathbb P(M_0>r)
\le4e^{-nr^2/16}\le4e^{-r^2/16}.
\]

For every \(p>0\), expressing \(x^p\) as \(\int_0^x p r^{p-1}\,dr\) gives

\[
\mathbb E M_0^p
\le10^p+4p\int_{10}^{\infty}r^{p-1}e^{-r^2/16}\,dr<\infty,
\]

uniformly in width.

The Gaussian integral also gives

\[
\mathbb E e^{\lambda\|G^{(4)}\|_2^2}=(1-2\lambda)^{-n/2},
\qquad \lambda<1/2.
\]

Repeated differentiation at zero yields

\[
\mathbb E\|G^{(4)}\|_2^{2k}=\prod_{j=0}^{k-1}(n+2j).
\]

The differentiation is justified by domination: on a sufficiently small interval about zero, a polynomial in \(\|G^{(4)}\|_2^2\) times its exponential is bounded by a constant times \(e^{\lambda_0\|G^{(4)}\|_2^2}\) for some fixed \(0<\lambda_0<1/2\), whose expectation is finite.

Consequently

\[
\mathbb E\varepsilon^{2k}
=n^{-3k}\prod_{j=0}^{k-1}(n+2j)
\le\left(\prod_{j=0}^{k-1}(1+2j)\right)n^{-2k}.
\tag{R13}
\]

This checks both powers of \(n\) in (14b). In particular,

\[
\mathbb E\varepsilon\le n^{-1},\qquad
\mathbb E\varepsilon^2=n^{-2},\qquad
\mathbb E\varepsilon^4=n^{-4}(1+2/n)\le3n^{-4}.
\tag{R14}
\]

Every fixed moment of the polynomials in (14a) is uniformly finite. To see this without assuming independence of a polynomial and the readout norm, expand an integer power into finitely many monomials. Each mixed moment is bounded by

\[
\mathbb E[M_0^a\varepsilon^b]
\le(\mathbb E M_0^{2a})^{1/2}
   (\mathbb E\varepsilon^{2b})^{1/2}.
\]

Higher integer moments bound any remaining positive real moment. This argument in fact does not need independence between \(M_0\) and \(\varepsilon\), although the canonical initialization supplies it.

Uniform boundedness of \(\mathbb E[(K^{\rm ran})^4]\), together with (R14), gives

\[
\begin{aligned}
\mathbb E[(K^{\rm ran})^2\varepsilon^2]
&\le\bigl(\mathbb E[(K^{\rm ran})^4]\bigr)^{1/2}(\mathbb E\varepsilon^4)^{1/2}
\le C_Sn^{-2},\\
\mathbb E[(K^{\rm ran})^2\varepsilon]
&\le\bigl(\mathbb E[(K^{\rm ran})^4]\bigr)^{1/2}(\mathbb E\varepsilon^2)^{1/2}
\le C_Sn^{-1},\\
\mathbb E[(K^{\rm ran})^2]&\le C_S.
\end{aligned}
\]

Taking expectations in the exact expansion (R11), with \(K\) replaced by \(K^{\rm ran}\), gives

\[
\mathbb E\left[\frac1n\sum_i\sup_{0\le v\le t}
[W_i^{(4)}(v)\phi''(z_i^{(3)}(v))]_+\right]
\le\frac2n+C_S\left(\frac{t^3}{n^2}+\frac{t^4}{n}+t^5\right)
\le C_S(n^{-1}+t^5)
\]

for \(0\le t\le S\). This proves (14c) unconditionally; it does not discard a bad event. The unrestricted proof supports this expectation estimate even for \(n=1\).

The asserted integrability is also sufficient in the literal uniform-integrability sense. At \(t\le S\), the nonnegative right side of (R11) with random constants is bounded by a fixed polynomial in \(M_0,\varepsilon\) having a uniformly bounded second moment. For such dominating variables \(D\),

\[
\mathbb E[D\,\mathbf1_{D>R}]\le\mathbb E[D^2]/R.
\]

This tends to zero uniformly as \(R\) tends to infinity. No limiting random-field theorem is necessary for the stated expectation estimate.

## 8. Quantifiers over time prefixes, masks, and clippings

The constants in Sections 2--5 use only \(S\), the initial hidden operator norms, and \(\varepsilon\). They do not use the number or location of retained middle coordinates, differentiability of \(\tau\), a tail bound on \(q^{(2)}\), or any event along a trajectory.

For a fixed width and one realization of the initial blocks, every fixed diagonal zero-one mask and every prescribed allowed clipping map defines its own unique trajectory. The deterministic proof applies to all of them on that same realization. On event (12), the same deterministic \(C_S\) therefore controls all these trajectories and all \(t\in[0,S]\) simultaneously. No union bound over masks, clippings, or time is necessary.

The mask and map must be fixed for each trajectory, as stated. The argument does not assert the same exact differentiation for masks that switch with time. Random selection from the allowed fixed choices is covered pathwise, even if selected using the initial data, provided the resulting trajectory is measurable, as the candidate explicitly requires.

For a prescribed \(Q,\tau\), measurability is not an extra hidden restriction. Local Lipschitz dependence gives continuous dependence of the solution on its initial state over finite intervals: iteration of the integral difference inequality bounds a perturbation by its initial norm times \(e^{Ls}\) on a common bounded neighborhood. The coefficient paths are continuous in time. Their supremum on a compact interval is the supremum over a countable dense subset (with the degenerate interval \(t=0\) treated directly), hence measurable. For general choices, the candidate correctly retains the measurability qualification instead of claiming measurability of an arbitrary uncountable supremum.

The polynomial domination in Section 7 is the same for every such choice, so the expectation constant is uniform too. The result does not need or assert an exchange of expectation with a supremum over all clippings.

Uniformity in width means constants independent of \(n\), and the stated probability for each width. It does not mean that (14), unchanged, is a probability bound for one intersection over all widths.

## 9. Euclidean input Hessian and positive trace

At fixed time \(s\), keep the current \(W^{(3)},W^{(4)}\) fixed and regard the full network's middle activation as a free input \(u\). The scalar function is

\[
f_s(u)=\frac1n\sum_i W_i^{(4)}(s)
\phi\bigl((W^{(3)}(s)u)_i\bigr).
\]

Two ordinary coordinate derivatives give

\[
\frac{\partial^2 f_s}{\partial u_j\partial u_k}(u)
=\frac1n\sum_iW_i^{(4)}(s)
\phi''\bigl((W^{(3)}(s)u)_i\bigr)
W_{ij}^{(3)}(s)W_{ik}^{(3)}(s).
\]

At \(u=h^{(2)}(s)\), this is exactly (15). The \(1/n\) factor is present once, from the output definition. This is an input Hessian with frozen upper weights, not a parameter Hessian or a derivative of the training trajectory.

At this fixed time, put \(b_i=W_i^{(4)}\phi''(z_i^{(3)})\) and

\[
P=\frac1n(W^{(3)})^T\operatorname{diag}([b_i]_+)W^{(3)}.
\]

Both \(P\) and

\[
P-\mathcal H^{(2)}
=\frac1n(W^{(3)})^T\operatorname{diag}([-b_i]_+)W^{(3)}
\]

are positive semidefinite. Let \(\Pi\) be the orthogonal projection onto the positive eigenspace of \(\mathcal H^{(2)}\). In an orthonormal eigenbasis,

\[
\operatorname{Tr}[(\mathcal H^{(2)})_+]
=\operatorname{Tr}(\Pi\mathcal H^{(2)})
\le\operatorname{Tr}(\Pi P)
\le\operatorname{Tr}P.
\]

The first inequality sums nonnegative quadratic forms of \(P-\mathcal H^{(2)}\); the second sums nonnegative quadratic forms of \(P\) on the orthogonal complement. This proves the needed trace comparison without using the generally invalid inference \((\mathcal H^{(2)})_+\le P\).

Directly computing the trace gives

\[
\operatorname{Tr}P
=\frac1n\sum_i[b_i]_+\|\operatorname{row}_i(W^{(3)})\|_2^2
\le\frac{K_3^2}{n}\sum_i[b_i]_+,
\]

because \(\|\operatorname{row}_i(W^{(3)})\|_2
=\|(W^{(3)})^Te_i\|_2\le\|W^{(3)}\|_{\rm op}\).

Finally,

\[
\sup_{0\le s\le t}\operatorname{Tr}[(\mathcal H^{(2)}(s))_+]
\le\frac{K_3^2}{n}\sum_i\sup_{0\le s\le t}[b_i(s)]_+.
\tag{R15}
\]

This verifies the stated consequences of (10)--(13), including the time supremum. The main coefficient estimate covers all masks; the Hessian paragraph expressly describes the full network and its free middle input, so no claim about a different pruned-input parameterization is needed.

For the unconditional Hessian estimate, multiply the unrestricted version of (R11), with \(K\) replaced by \(K^{\rm ran}\), by \((K_3^{\rm ran})^2\). This yields

\[
2(K_3^{\rm ran})^2\varepsilon
+(K_3^{\rm ran})^2(K^{\rm ran})^2\varepsilon^2t^3
+\frac{7c}{6}(K_3^{\rm ran})^2(K^{\rm ran})^2\varepsilon t^4
+\frac{c^2}{3}(K_3^{\rm ran})^2(K^{\rm ran})^2t^5.
\]

All required moments are finite uniformly. More explicitly,

\[
\mathbb E[(K_3^{\rm ran})^4(K^{\rm ran})^4]
\le\bigl(\mathbb E[(K_3^{\rm ran})^8]\bigr)^{1/2}
   \bigl(\mathbb E[(K^{\rm ran})^8]\bigr)^{1/2}\le C_S.
\]

Applying Cauchy--Schwarz to each readout factor gives

\[
\begin{aligned}
\mathbb E[(K_3^{\rm ran})^2\varepsilon]&\le C_S/n,\\
\mathbb E[(K_3^{\rm ran})^2(K^{\rm ran})^2\varepsilon^2]&\le C_S/n^2,\\
\mathbb E[(K_3^{\rm ran})^2(K^{\rm ran})^2\varepsilon]&\le C_S/n,\\
\mathbb E[(K_3^{\rm ran})^2(K^{\rm ran})^2]&\le C_S.
\end{aligned}
\]

Together with (R15), these prove exactly the asserted unconditional bound \(C_S(n^{-1}+t^5)\) for the supremum of the Euclidean positive trace. The candidate correctly allows higher moments for these products; fourth moments of each factor alone are not silently used to control an eighth-order mixed moment.

## 10. Fresh Gaussian probe and RMS scaling

Condition on the actual network and fix a time \(s\). Then \(H=\mathcal H^{(2)}(s)\) is a fixed symmetric matrix. For every vector \(x\),

\[
x^THx\le x^TH_+x,\qquad x^TH_+x\ge0,
\]

and hence \((x^THx)_+\le x^TH_+x\). A fresh standard Gaussian \(\xi\) independent of the network has conditional second moment \(\mathbb E_\xi\xi\xi^T=I\). Expanding the quadratic form therefore proves

\[
\mathbb E_\xi[(\xi^TH\xi)_+]
\le\sum_{j,k}(H_+)_{jk}\mathbb E_\xi[\xi_j\xi_k]
=\operatorname{Tr}H_+.
\]

This is (16). It uses independence after conditioning, not a claim that the trained network is Gaussian. In fact, conditional second moment \(I\) would suffice.

The statement is instantaneous. The uniform positive-trace bound permits a uniform bound on these conditional expectations at individual times. It does not by itself bound the conditional expectation of a supremum over time using a single shared probe. It also does not identify a transported training response with a fresh independent probe. The candidate makes neither inference.

For the metric specified by the norm \(\|u\|_2/\sqrt n\), the second variation of \(f_s\) is still \(v^THw\). If \(A\) is its representing curvature operator in that metric, the defining equality is

\[
\frac1n v^TAw=v^THw\quad\text{for all }v,w,
\]

so \(A=nH\). Multiplication by a positive scalar preserves eigenvectors and scales eigenvalues, giving

\[
A_+=nH_+,
\qquad
\frac1n\operatorname{Tr}A_+=\operatorname{Tr}H_+.
\]

This verifies the candidate's Euclidean versus RMS distinction without changing any ordinary norm convention. The trace estimate supplies

\[
\|A_+\|_{\rm op}\le\operatorname{Tr}A_+
\le C_S(1+nt^5)
\]

on the canonical event, after absorbing \(K_3^2\) into \(C_S\). Thus the normalized trace conclusion cannot simply be relabeled as the same width-independent positive operator-norm estimate for \(A\).

For a centered transported probe \(\eta\) whose conditional covariance given the network is \(\Gamma\), the corresponding elementary inequality is

\[
\mathbb E[(\eta^TH\eta)_+\mid\text{network}]
\le\operatorname{Tr}(H_+\Gamma).
\]

One can bound the latter by \(\|\Gamma\|_{\rm op}\operatorname{Tr}H_+\) when the conditional covariance norm is controlled. Without any such control, scaling a probe in a positive eigendirection scales its positive quadratic work arbitrarily. This substantiates the candidate's warning about covariance and alignment; it supplies no transported-response theorem.

For a probe with conditional mean \(m\) and conditional covariance \(\Gamma\), expanding the centered covariance and using \(\mathbb E[\eta-m\mid\text{network}]=0\) gives

\[
\mathbb E[\eta\eta^T\mid\text{network}]=\Gamma+mm^T.
\]

Applying the same pointwise quadratic-form inequality therefore proves

\[
\mathbb E[(\eta^TH\eta)_+\mid\text{network}]
\le\operatorname{Tr}\bigl(H_+(\Gamma+mm^T)\bigr).
\]

This verifies the noncentered formula now stated explicitly in the revised candidate. Both formulas use conditional second moments given the actual network.

## 11. Resolved clarifications and final certification

Both previously nonblocking clarifications are resolved in the certified revised candidate:

1. The transported-probe paragraph now explicitly states conditional mean zero and conditional covariance given the actual network. It also explicitly replaces \(\Gamma\) by \(\Gamma+mm^T\) for conditional mean \(m\). Section 10 proves both statements, including the conditional positive-work inequality.

2. The RMS paragraph now explicitly states that the normalized positive-trace estimate does not transfer the same \(n^{-1}+t^5\) scale to a width-independent RMS positive operator norm, and that a different, rougher operator bound may follow from the coordinatewise readout estimate. Indeed, using \(|W_i^{(4)}(s)|\le|W_i^{(4)}(0)|+cS\), the event \(\|G^{(4)}\|_2\le2\sqrt n\), and \(|\phi''|\le2\) gives \(\|(n\mathcal H^{(2)})_+\|_{\rm op}\le2K_3^2(2/\sqrt n+cS)\). This confirms the revised distinction.

The opening status now directs the reader to the independent review's audited version. The explicit feature-time statement fixes the interpretation of the prefix \(t\): the fifth-power estimate concerns feature time throughout the proof. These wording changes preserve the original scoped mathematical conclusion and its original clean PASS.

The report's expectation calculations now use \(K^{\rm ran}\) and \(K_3^{\rm ran}\) directly, with no temporary aliases for those constants. Generic local Lipschitz constants and the generic probe matrix \(H\) retain their original notation.

The candidate establishes the actual trained top-coefficient prefix positive-part estimate, the canonical event with the stated constants, its unconditional expectation version, and the Euclidean Hessian and fresh-probe consequences. The initial readout contribution, clipping and pruning factors, fifth feature-time power, polynomial moment control, and Hessian factor \(1/n\) remain established. No clarification or correction remains open.

This final certification applies exactly to candidate SHA256 `af07fcbd7f937206858e942aa2b9e728734db908205112227191d54c1fd09c4c`.

**Required corrections: none for the scoped lemma. Verdict: PASS.**
