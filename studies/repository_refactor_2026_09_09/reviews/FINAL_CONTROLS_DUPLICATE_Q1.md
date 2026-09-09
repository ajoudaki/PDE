## Destination: finite_optimization_and_controls — Q1. Integrated initial-matrix queries

This fragment records the exact finite arctangent equations needed to define the
filtered comparison. The datum, loss and raw metric are those of fragment S;
all derivatives here use feature time. It also proves the deterministic
compression and states the derivative information it does not provide.

### 1. Finite setup and exact integral equations

Fix a positive integer width \(n\). Each
\(z^{(\ell)},h^{(\ell)},\delta^{(\ell)}\), for \(\ell=1,2,3\),
and the stored readout \(W^{(4)}\) is a real column vector of
length \(n\); \(W^{(2)},W^{(3)}\) are real \(n\)-by-\(n\)
matrices. A superscript \(T\) denotes the ordinary matrix transpose.
The activation is \(\phi(z)=\arctan z\), applied coordinatewise,
and \(\odot\) denotes coordinatewise multiplication. Define
\[
h^{(\ell)}=\phi(z^{(\ell)}),\qquad
z^{(2)}=W^{(2)}h^{(1)},\qquad z^{(3)}=W^{(3)}h^{(2)},
\]
\[
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\qquad
q^{(2)}=(W^{(3)})^T\delta^{(3)},\qquad
\delta^{(2)}=\phi'(z^{(2)})\odot q^{(2)},
\]
\[
\delta^{(1)}=\phi'(z^{(1)})\odot(W^{(2)})^T\delta^{(2)}.
\]
The canonical initialization has independent entries
\(z^{(1)}_{0,i}\sim N(0,1)\),
\(W^{(2)}_{0,ij},W^{(3)}_{0,ij}\sim N(0,1/n)\), and
\(W^{(4)}_{0,i}\sim N(0,n^{-2})\), with all blocks independent.
Every identity below also holds deterministically for any initial
values for which the indicated finite flow exists.

A prime denotes differentiation in feature time \(s\). The uncut
finite feature-time equations are
\[
(z^{(1)})'=\delta^{(1)},\qquad
(W^{(2)})'=\frac{\delta^{(2)}(h^{(1)})^T}{n},\qquad
(W^{(3)})'=\frac{\delta^{(3)}(h^{(2)})^T}{n},\qquad
(W^{(4)})'=h^{(3)}.
\]
This is the feature clock associated with the canonical physical
equations through \(ds/dt=-2(f_n-1)\); no clock convergence is
asserted here. Set
\(F(z)=z+z^3/3\) and \(x^{(1)}=F(z^{(1)})\), coordinatewise.
Since \(F'(z)=1/\phi'(z)\), the transformed first equation is
\((x^{(1)})'=(W^{(2)})^T\delta^{(2)}\).
Introduce the layer-two primitive
\[
a^{(2)}(s)=\int_0^s\delta^{(2)}(u)\,du.
\]
Write the trained increments as
\[
M^{(2)}(s)=\int_0^s
 \frac{(a^{(2)})'(u)(h^{(1)}(u))^T}{n}\,du,\qquad
M^{(3)}(s)=\int_0^s
 \frac{\delta^{(3)}(u)(h^{(2)}(u))^T}{n}\,du.
\tag{Q1.1}
\]
Thus \(W^{(\ell)}(s)=W^{(\ell)}_0+M^{(\ell)}(s)\), for
\(\ell=2,3\). All histories in (Q1.1) are retained exactly. Integrating
the first feature-time equation and interchanging the triangular
integrals gives
\[
\begin{split}
x^{(1)}(s)={}&x^{(1)}_0+(W^{(2)}_0)^T a^{(2)}(s)+R^{(1)}(s),\\
R^{(1)}(s)={}&\int_0^s h^{(1)}(u)
 \frac{((a^{(2)})'(u))^T[a^{(2)}(s)-a^{(2)}(u)]}{n}\,du.
\end{split}                                                    \tag{Q1.2}
\]
Indeed,
\[
\int_0^s (M^{(2)}(v))^T\delta^{(2)}(v)\,dv
=\int_0^s h^{(1)}(u)
  \frac{(\delta^{(2)}(u))^T\int_u^s\delta^{(2)}(v)dv}{n}\,du.
\]
The remaining exact equations are
\[
z^{(1)}=F^{-1}(x^{(1)}),\qquad h^{(1)}=\phi(z^{(1)}),
\]
\[
z^{(2)}(s)=W^{(2)}_0h^{(1)}(s)
 +\int_0^s (a^{(2)})'(u)
       \frac{(h^{(1)}(u))^T h^{(1)}(s)}{n}\,du,
\qquad h^{(2)}=\phi(z^{(2)}),                                \tag{Q1.3}
\]
\[
z^{(3)}(s)=W^{(3)}_0h^{(2)}(s)
 +\int_0^s\delta^{(3)}(u)
       \frac{(h^{(2)}(u))^T h^{(2)}(s)}{n}\,du,
\qquad h^{(3)}=\phi(z^{(3)}),                                \tag{Q1.4}
\]
\[
W^{(4)}(s)=W^{(4)}_0+\int_0^s h^{(3)}(u)du,
\qquad \delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),              \tag{Q1.5}
\]
\[
q^{(2)}(s)=(W^{(3)}_0)^T\delta^{(3)}(s)
 +\int_0^s h^{(2)}(u)
       \frac{(\delta^{(3)}(u))^T\delta^{(3)}(s)}{n}\,du,
\qquad
(a^{(2)})'=\phi'(z^{(2)})\odot q^{(2)}.                    \tag{Q1.6}
\]
The output is exactly
\(f_n(s)=(W^{(4)}(s))^T h^{(3)}(s)/n\).
Only the following four paths are arguments of an initial-matrix
action in (Q1.1)--(Q1.6):
\[
\begin{array}{c|c}
\text{action}&\text{argument}\\ \hline
W^{(2)}_0&h^{(1)}\\
(W^{(2)}_0)^T&a^{(2)}\\
W^{(3)}_0&h^{(2)}\\
(W^{(3)}_0)^T&\delta^{(3)}.
\end{array}                                                    \tag{Q1.7}
\]
In particular, the rough lower backward argument \(\delta^{(2)}\)
has disappeared from the initial-matrix actions in these integral
state equations. It has not disappeared from the nonlinear equation
that generates \(a^{(2)}\).

### 2. What time regularity proves

On \(0\le s\le S\), impose the primal bounds
\(\|W^{(2)}(s)\|_{\rm op},\|W^{(3)}(s)\|_{\rm op},
\|W^{(4)}(s)\|_\infty\le B_S\), with \(B_S\) independent of
\(n\). These are the established actual-trajectory bounds on the
corresponding primal event. All four paths in (Q1.7) then have derivative
Euclidean norm divided by \(\sqrt n\) bounded by a constant \(C_S\)
independent of \(n\). For the new path, boundedness of \(\phi'\)
gives \(\|\delta^{(2)}\|_2/\sqrt n\le B_S^2\), so, for
\(0\le t\le s\le S\),
\[
\frac{\|a^{(2)}(s)-a^{(2)}(t)\|_2}{\sqrt n}
\le\int_t^s\frac{\|\delta^{(2)}(u)\|_2}{\sqrt n}\,du
\le C_S|s-t|.
\tag{Q1.8}
\]
The other three derivative bounds were established in
fragment Q2. Constants are uniform in width on
the stated primal event. These are statements about actual unperturbed
trajectories; they are not assumed for a perturbed comparison process.

Let \(\pi(s)\) be the last mesh point at or before \(s\), for a
deterministic mesh of spacing at most \(\varepsilon/C_S\). Each of
the four query paths changes by Euclidean norm at most
\(\sqrt n\varepsilon\) between \(\pi(s)\) and \(s\). In particular,
\[
\begin{split}
\sup_{s\le S}
 \frac{\|W^{(2)}_0[h^{(1)}(s)-h^{(1)}(\pi(s))]\|_2}{\sqrt n}
 &\le\|W^{(2)}_0\|_{\rm op}\varepsilon,\\
\sup_{s\le S}
 \frac{\|(W^{(2)}_0)^T[a^{(2)}(s)-a^{(2)}(\pi(s))]\|_2}{\sqrt n}
 &\le\|W^{(2)}_0\|_{\rm op}\varepsilon.
\end{split}                                                    \tag{Q1.9}
\]
The two corresponding bounds for \(W^{(3)}_0h^{(2)}\) and
\((W^{(3)}_0)^T\delta^{(3)}\) have right-hand side
\(\|W^{(3)}_0\|_{\rm op}\varepsilon\).
Consequently a specified actual path admits a time net of
\(1+\lceil C_SS/\varepsilon\rceil\) matrix arguments per
orientation, independently of width. This is an approximation of
matrix responses along a supplied trajectory.

The rank memories in (Q1.1)--(Q1.2) do not hide an extra continuity failure
on this uniformly Lipschitz path class. For example, compare two
paths with their corresponding tilded memories. Suppose both paths
obey
\[
\frac{\|h^{(1)}(s)\|_2}{\sqrt n}\le B_h,\qquad
\frac{\|(h^{(1)})'(s)\|_2}{\sqrt n}\le L_h,\qquad
\frac{\|(a^{(2)})'(s)\|_2}{\sqrt n}\le L_a,
\]
and the same bounds hold for the tilded quantities. Define the two
scalar errors
\[
e_a=\sup_{s\le S}
 \frac{\|a^{(2)}(s)-\widetilde a^{(2)}(s)\|_2}{\sqrt n},\qquad
e_h=\sup_{s\le S}
 \frac{\|h^{(1)}(s)-\widetilde h^{(1)}(s)\|_2}{\sqrt n}.
\]
With both primitives zero initially, integration by parts gives
\[
\begin{split}
M^{(2)}(s)-\widetilde M^{(2)}(s)
={}&\frac{[a^{(2)}(s)-\widetilde a^{(2)}(s)](h^{(1)}(s))^T}{n}\\
 &-\int_0^s
  \frac{[a^{(2)}-\widetilde a^{(2)}]((h^{(1)})')^T}{n}\,du\\
 &+\int_0^s
  \frac{(\widetilde a^{(2)})'[h^{(1)}-\widetilde h^{(1)}]^T}{n}\,du,
\end{split}
\]
where all integrand factors are evaluated at \(u\). Hence
\[
\sup_s\|M^{(2)}-\widetilde M^{(2)}\|_{\rm op}
\le(B_h+SL_h)e_a+SL_ae_h.                                   \tag{Q1.10}
\]
Similarly, since
\(R^{(1)}(s)=\int_0^s(M^{(2)}(u))^T(a^{(2)})'(u)du\),
\[
\sup_{s\le S}\frac{\|R^{(1)}(s)-\widetilde R^{(1)}(s)\|_2}{\sqrt n}
\le SL_a\sup_s\|M^{(2)}-\widetilde M^{(2)}\|_{
\rm op}+2SL_aB_h e_a.                                      \tag{Q1.11}
\]
For (Q1.11), integrate
\(\int_0^s(\widetilde M^{(2)})^T
 [(a^{(2)})'-(\widetilde a^{(2)})']du\) by parts, using
\(\|\widetilde M^{(2)}\|_{\rm op}\le SL_aB_h\) and
\(\|(\widetilde M^{(2)})'\|_{\rm op}\le L_aB_h\).
For completeness, if both top-layer paths satisfy
\(\|h^{(2)}\|_2/\sqrt n\le B_2\) and
\(\|\delta^{(3)}\|_2/\sqrt n\le D_3\), then the ordinary
integral for \(M^{(3)}\) gives
\[
\begin{split}
\sup_{s\le S}\|M^{(3)}(s)-\widetilde M^{(3)}(s)\|_{\rm op}
\le{}&SB_2\sup_{s\le S}
 \frac{\|\delta^{(3)}(s)-\widetilde\delta^{(3)}(s)\|_2}{\sqrt n}\\
 &+SD_3\sup_{s\le S}
 \frac{\|h^{(2)}(s)-\widetilde h^{(2)}(s)\|_2}{\sqrt n}.
\end{split}
\]

Thus (Q1.9) yields small equation residuals after replacing only the
initial-matrix responses along the actual trajectory. The exact
rank-update memory has not been dropped to obtain this statement.

### 3. Why this does not yet construct a finite-query approximation

At time \(s_k\), the value of an actual query such as \(a^{(2)}(s_k)\)
has been generated by the dynamics on the entire preceding interval.
Those dynamics used the initial matrices at unrecorded intermediate
arguments. Observing the actual query is causal in physical time,
but it is not thereby measurable from only the retained finite-query
transcript. Gaussian conditioning on the latter transcript cannot
treat that query as a legal next query without proving this
measurability. Sampling a true trajectory does not supply such a proof.

A finite-call algorithm can instead evolve its own state using frozen
or interpolated matrix responses and make new calls on its own
queries. That is an admissible proposed approximation. Equation (Q1.9)
on the true path proves consistency of the substitution, not closeness
between this algorithm and the true dynamics. In particular it does
not establish the rank premise for the actual perturbed histories in
fragment Q4; query perturbations may generate
new directions in subsequent nonlinear queries.

The uniform temporal bounds also do not by themselves give strong
compactness in a fixed infinite-dimensional Hilbert space. For example,
in \(\ell^2(\mathbb N)\), the paths \(s\mapsto s e_j\), where
\(e_j\) is the \(j\)-th standard unit vector, are uniformly bounded
and Lipschitz on \([0,S]\), but their values at any positive time
have no norm-convergent subsequence. This observation is not a claim
that such a family occurs in the canonical network, nor a construction
of a population space for it.

### 4. The retained stability term and derivative observables

For two state paths, the exact primitive difference obeys
\[
\begin{split}
a^{(2)}(s)-\widetilde a^{(2)}(s)=\int_0^s\bigl\{
 &\phi'(z^{(2)})\odot(q^{(2)}-\widetilde q^{(2)})\\
 &+[\phi'(z^{(2)})-\phi'(\widetilde z^{(2)})]
       \odot\widetilde q^{(2)}\bigr\}\,du.
\end{split}                                                    \tag{Q1.12}
\]
All factors inside the integral are evaluated at \(u\).
The first integrand has Euclidean norm divided by \(\sqrt n\)
at most \(\|q^{(2)}-\widetilde q^{(2)}\|_2/\sqrt n\).
In the second integrand, the available bound on
\(\|\widetilde q^{(2)}\|_2/\sqrt n\) does not provide a
width-uniform Lipschitz bound in
\(\|z^{(2)}-\widetilde z^{(2)}\|_2/\sqrt n\).
For \(Q>0\) the exact tail split gives
\[
\begin{split}
&\frac{\|[\phi'(z^{(2)})-\phi'(\widetilde z^{(2)})]
       \odot\widetilde q^{(2)}\|_2}{\sqrt n}\\
&\quad\le\|\phi''\|_\infty Q
  \frac{\|z^{(2)}-\widetilde z^{(2)}\|_2}{\sqrt n}
 +2\frac{\|\widetilde q^{(2)}\odot
   \mathbf1_{\{|\widetilde q^{(2)}|>Q\}}\|_2}{\sqrt n}.
\end{split}                                                    \tag{Q1.13}
\]
The total L2 bound alone neither makes the last term uniformly small
over the approximation family nor supplies the tail-versus-stability
rate needed to pass \(Q\to\infty\). Integrating the initial query
therefore retains the actual middle multiplier; it does not resolve
the continuation problem represented by that multiplier.

There is also a separate observable issue. The lower backward result
is
\[
(W^{(2)}(s))^T\delta^{(2)}(s)
=\frac{d}{ds}\big[(W^{(2)}_0)^T a^{(2)}(s)\big]
 +(M^{(2)}(s))^T(a^{(2)})'(s),                             \tag{Q1.14}
\]
and \(\delta^{(1)}=\phi'(z^{(1)})\odot
(W^{(2)})^T\delta^{(2)}\). Uniform approximation of the integrated
response in (Q1.9) does not imply strong convergence of its derivative.
For example, \(j^{-1}\sin(js)v\) tends uniformly to zero with
uniformly bounded derivative, while its derivatives do not tend to
zero in time L2 for a nonzero fixed \(v\). This is a limitation of
the inference, not a canonical counterexample. Hidden velocities and
the raw first kernel block require additional derivative or energy
control even if uniform state convergence were separately proved.



