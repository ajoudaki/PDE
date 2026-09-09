# Uniform Borel–Padé transfer and an explicit finite-jet rational alternative

Prepared 6 September 2026. This note proves conditional reconstruction statements. It does not establish the Borel reconstruction premise for the population gradient flow.

## 1. Exact hypotheses for transferring Borel-plane approximation

Fix \(\sigma>0\) and \(T>0\). Suppose the actual function of interest satisfies

\[
f(t)=\int_0^\infty e^{-u}B(tu^\sigma)\,du,
\qquad 0\le t\le T.
\]

Here \(B\) is continuous on the nonnegative ray and is analytic near zero with coefficients

\[
B(\xi)=\sum_{p\ge0}b_p\xi^p,
\qquad b_p=\frac{c_p}{\Gamma(1+\sigma p)}.
\]

The \(c_p\) may be formal Taylor coefficients obtained from initialization derivatives. The displayed integral identity is an assumption about the actual target function, not a consequence merely of the existence of these coefficients.

Let \(R_N\) be rational approximants constructed from finitely many \(b_p\). They can be ordinary Padé approximants when a separate Padé convergence theorem applies. Suppose

\[
\varepsilon_N(L):=\sup_{0\le\xi\le L}|R_N(\xi)-B(\xi)|\longrightarrow0
\quad\text{for each finite }L.
\]

In particular, the approximants eventually have no nonremovable poles on each specified compact segment.

Assume also a common growth bound

\[
|R_N(\xi)|+|B(\xi)|\le C\exp(b\xi^{1/\sigma}),
\quad \xi\ge0,
\quad b\ge0,
\]

and put \(\lambda=1-bT^{1/\sigma}>0\). The reconstructed functions

\[
f_N(t)=\int_0^\infty e^{-u}R_N(tu^\sigma)\,du
\]

then converge uniformly to \(f\) on \([0,T]\).

Indeed, for every \(U>0\), splitting the integral at \(U\) gives the explicit estimate

\[
\sup_{0\le t\le T}|f_N(t)-f(t)|
\le
(1-e^{-U})\varepsilon_N(TU^\sigma)
+\frac C\lambda e^{-\lambda U}.
\]

On the finite part, \(tu^\sigma\in[0,TU^\sigma]\). On the tail,

\[
e^{-u}\bigl(|R_N(tu^\sigma)|+|B(tu^\sigma)|\bigr)
\le Ce^{-(1-bt^{1/\sigma})u}
\le Ce^{-\lambda u}.
\]

Choose \(U\) first to make the tail small, and then \(N\) to make the finite part small. This proves uniform convergence, including \(t=0\).

This proof uses no independent values of the target at positive times. However, a guaranteed computable choice of \(N\) requires a known bound on \(\varepsilon_N(L)\); qualitative convergence alone provides an existence statement.

## 2. A weaker and more practical theorem using a cutoff

The common global growth bound on all \(R_N\) is unnecessary if the approximation uses a finite Laplace cutoff. Assume only

\[
|B(\xi)|\le C e^{b\xi^{1/\sigma}},
\qquad \lambda=1-bT^{1/\sigma}>0,
\]

and the local uniform convergence of \(R_N\) stated above. Define

\[
f_{N,U}(t)=\int_0^U e^{-u}R_N(tu^\sigma)\,du.
\]

Then

\[
\sup_{t\in[0,T]}|f_{N,U}(t)-f(t)|
\le (1-e^{-U})\varepsilon_N(TU^\sigma)
+\frac C\lambda e^{-\lambda U}.
\]

The proof estimates the true \(B\) tail only. Thus even poles of \(R_N\) farther along the positive ray are irrelevant, provided none lie on the compact segment used by the cutoff.

For every \(\epsilon>0\), choose \(U\) so that the last term is at most \(\epsilon/3\), then choose a finite \(N\) so that the first term is at most \(\epsilon/3\). One can choose an increasing-cutoff diagonal sequence with error tending to zero, but no arbitrary rule \(U=U_N\to\infty\) is justified by compact convergence alone: approximation quality must also be controlled on the growing segment \([0,TU_N^\sigma]\).

More generally, the exponential growth hypothesis can be replaced by any uniform true-tail estimate

\[
\sup_{t\le T}\int_U^\infty e^{-u}|B(tu^\sigma)|\,du\longrightarrow0.
\]

## 3. Finite quadrature really gives a finite construction

Fix \(U,N\) as above. Partition \([0,U]\) into subintervals with mesh at most \(h\), choose a sample point \(v_j\) in each, and let

\[
w_j=\int_{u_{j-1}}^{u_j}e^{-u}\,du.
\]

The finite approximation is

\[
\widetilde f_{N,U,Q}(t)=\sum_{j=1}^Qw_j R_N(tv_j^\sigma).
\]

Because \((t,u)\mapsto R_N(tu^\sigma)\) is continuous on the compact rectangle \([0,T]\times[0,U]\), these weighted Riemann sums converge uniformly in \(t\) as the mesh shrinks.

There is also an elementary explicit bound. If

\[
D_N=\sup_{0\le\xi\le TU^\sigma}|R_N'(\xi)|<\infty,
\]

then the quadrature error is at most

\[
D_NT
\begin{cases}
h^\sigma,&0<\sigma\le1,\\
\sigma U^{\sigma-1}h,&\sigma\ge1.
\end{cases}
\]

The bound follows by the mean-value estimate for \(R_N\), the Hölder estimate for \(u^\sigma\) when \(\sigma\le1\), and the derivative bound for \(u^\sigma\) when \(\sigma\ge1\). The weights have total mass \(1-e^{-U}\le1\).

Choose finite \(Q\) to make this error at most \(\epsilon/3\). Then the preceding choices of \(U,N,Q\) give

\[
\sup_{t\in[0,T]}|\widetilde f_{N,U,Q}(t)-f(t)|\le\epsilon.
\]

If \(R_N\) is rational in its argument, the finite sum is rational in \(t\). Its coefficients depend on finitely many initialization coefficients, the declared reconstruction constants, and the quadrature rule. Its degree generally grows with both \(N\) and \(Q\).

This rational function is generally **not** the direct conventional \([m/n]\) Padé approximant of \(f\): its construction approximates the Borel transform and then approximates the Laplace integral. In particular, finite cutoff/quadrature need not preserve the exact initialization Taylor matching conditions. Uniform function approximation is the conclusion.

## 4. An explicit alternative that guarantees rational reconstruction

The preceding theorems intentionally separate Borel summability from rational approximation of \(B\). Merely knowing that \(B\) is analytic along the positive ray does not by itself establish uniform convergence of a chosen ordinary diagonal Padé sequence.

A known analytic domain gives a constructive alternative. Suppose \(B\) is analytic in

\[
D_a=\{\xi\in\mathbb C:\operatorname{Re}\xi>-a\},\qquad a>0.
\]

The explicit maps

\[
w=\frac{\xi}{\xi+2a},
\qquad
\xi=\frac{2aw}{1-w}
\]

map \(D_a\) biholomorphically to the unit disk and back. Therefore

\[
G(w)=B\left(\frac{2aw}{1-w}\right)
=\sum_{j\ge0}g_jw^j
\]

is analytic for \(|w|<1\). Its first \(N+1\) coefficients require only the first \(N+1\) coefficients of \(B\):

\[
g_0=b_0,
\qquad
g_j=\sum_{k=1}^j b_k(2a)^k\binom{j-1}{k-1}
\quad(j\ge1).
\]

Define

\[
R_N(\xi)=\sum_{j=0}^N g_j\left(\frac{\xi}{\xi+2a}\right)^j.
\]

This is a rational function whose only possible pole is \(-2a\), and it is computable from a finite jet at zero. For any \(L<\infty\), put \(q=L/(L+2a)<1\), choose \(q<r<1\), and let

\[
M_r=\max_{|w|=r}\left|B\left(\frac{2aw}{1-w}\right)\right|.
\]

Cauchy's coefficient bound \(|g_j|\le M_r r^{-j}\) gives

\[
\sup_{0\le\xi\le L}|B(\xi)-R_N(\xi)|
\le
\frac{M_r(q/r)^{N+1}}{1-q/r}.
\]

Thus local uniform rational approximation is guaranteed with an explicit geometric error. If a numerical bound on \(M_r\) is given, this is an effective finite-order estimate. For example, the stronger hypothesis

\[
|B(\xi)|\le C e^{b|\xi|}\quad(\xi\in D_a)
\]

implies \(M_r\le C\exp(2ab r/(1-r))\), yielding a completely explicit bound. In the ordinary \(\sigma=1\) Borel case, the same hypothesis supplies the true-ray tail estimate for every \(T<1/b\), with no time restriction from this bound if \(b=0\).

Combining this rational construction with Sections 2–3 proves the requested finite-initialization-data, uniform-on-\([0,T]\) approximation property under explicit analytic-domain, growth, and Borel-identification hypotheses.

The approximation is Taylor truncation in a conformal coordinate, hence a rational or Padé-type construction in \(\xi\). It is **not** generally ordinary \([N/N]\) Padé approximation: it matches the available \(N+1\) Taylor coefficients, rather than imposing the usual \(2N+1\) matching conditions. This distinction must remain explicit.

The general reconstruction framework appears in Costin–Dunne, *Uniformization and Constructive Analytic Continuation of Taylor Series*, Theorem 8, pp. 6–7: https://arxiv.org/pdf/2009.01962. It gives finite-coefficient reconstruction using a known uniformizing map and bounds dictated by the analytic domain. The elementary half-plane specialization above is proved directly, so no further hypotheses from their Riemann-surface theorem are being silently imported.

## 5. Implication for the GF conjecture and limits of the claim

For the population GF program, first establish that the actual scalar observable, output-dependent kernel, or matrix kernel equals the asserted Borel–Laplace sum. Establishing existence of the population GF and computing its initialization derivatives does not establish that identity.

Then either a genuine Padé convergence theorem for the relevant Borel transform or an explicit conformal reconstruction theorem can supply finite initialization-based approximations uniformly on a fixed positive interval. Existing prediction stability estimates and the established joint width/GD theorem can transfer this to network predictions and losses.

No all-time conclusion follows without global continuation and tail control. No general positive-ray Padé convergence theorem has been proved here from Gevrey coefficient bounds alone. No effective complexity guarantee follows from qualitative convergence unless its constants and convergence modulus can be controlled.
