## 13. Integrated initial-matrix queries with exact trained memory

This section gives a finite representation and a supplied-path approximation
bound for the three-hidden-layer arctangent network. It keeps both orientations
of both hidden matrices and all trained increments. It does not construct a
population space or a causal finite-query approximation to training.

### 13.1. Exact finite equations

Fix a width \(n\ge1\), one input \(x=1\), one label \(y=1\), and
\(\phi(z)=\arctan z\). All hidden vectors and the stored readout
\(a=W^{(4)}\) have length \(n\); the two middle matrices have size
\(n\times n\). Vector norms are ordinary Euclidean norms, and matrix
norms are ordinary operator norms; every width normalization is explicit. Define
\[
 h^\ell=\phi(z^\ell),\quad z^2=W^{(2)}h^1,\quad
 z^3=W^{(3)}h^2,\quad f=a^Th^3/n,
\]
\[
 \delta^3=a\odot\phi'(z^3),\quad q^2=(W^{(3)})^T\delta^3,
 \quad\delta^2=\phi'(z^2)\odot q^2,\quad
 \delta^1=\phi'(z^1)\odot(W^{(2)})^T\delta^2.
 \tag{13.1}
\]
Superscripts on vectors are layer indices. The feature-ascent equations are
\[
 (z^1)'=\delta^1,\qquad (W^{(2)})'=\delta^2(h^1)^T/n,
 \qquad (W^{(3)})'=\delta^3(h^2)^T/n,\qquad a'=h^3.
 \tag{13.2}
\]
The prime means feature time \(s\), with block mobilities \((n,1,1,n)\).
The physical full-square-loss velocity is \(-2(f-1)\) times (13.2).
When a physical orbit is represented by a feature orbit, its clock satisfies
\(ds/dt=-2(f-1)\). No clock or width convergence is used here.

The canonical initialization has independent \(z^1_{0,i}\sim N(0,1)\),
middle entries \(N(0,1/n)\), and \(a_{0,i}\sim N(0,n^{-2})\), all blocks
independent. Every following identity holds for arbitrary deterministic
initial values along a finite \(C^1\) solution on \([0,S]\). The estimates
are implications of their explicitly stated bounds, not new probability
estimates for those events.

Let \(F(z)=z+z^3/3\), applied coordinatewise, and \(X^1=F(z^1)\).
Its derivative \(F'=1/\phi'\) is positive, and its limits at the two ends
of the real line are infinite with the corresponding signs. It therefore
has a globally defined inverse. Put
\[
 b(s)=\int_0^s\delta^2(u)\,du,\quad
 M_2(s)=\int_0^s b'(u)(h^1(u))^T/n\,du,\quad
 M_3(s)=\int_0^s\delta^3(u)(h^2(u))^T/n\,du.
 \tag{13.3}
\]
The symbol \(b\) here denotes a primitive, not a backward sensitivity.
Then \(W^{(\ell)}=W^{(\ell)}_0+M_\ell\) for \(\ell=2,3\), and
\[
 \begin{split}
 X^1(s)&=X^1_0+(W^{(2)}_0)^Tb(s)+R_1(s),\\
 R_1(s)&=\int_0^s h^1(u)\frac{b'(u)^T[b(s)-b(u)]}{n}\,du,
 \qquad z^1=F^{-1}(X^1).
 \end{split} \tag{13.4}
\]
Indeed \((X^1)'=(W^{(2)})^T b'\). Substituting the integral for
\(M_2\) into \(\int_0^s M_2(v)^Tb'(v)\,dv\), and integrating first
over \(u\le v\le s\), gives (13.4). All integrands are continuous in
finite dimension, so this interchange is legitimate. The other equations are
\[
 \begin{aligned}
 z^2(s)&=W^{(2)}_0h^1(s)+\int_0^s b'(u)
                         \frac{h^1(u)^Th^1(s)}n\,du,\\
 z^3(s)&=W^{(3)}_0h^2(s)+\int_0^s\delta^3(u)
                         \frac{h^2(u)^Th^2(s)}n\,du,\\
 a(s)&=a_0+\int_0^s h^3(u)\,du,\\
 q^2(s)&=(W^{(3)}_0)^T\delta^3(s)+\int_0^s h^2(u)
                         \frac{\delta^3(u)^T\delta^3(s)}n\,du,\\
 b'(s)&=\phi'(z^2(s))\odot q^2(s).
 \end{aligned} \tag{13.5}
\]
Here \(h^\ell=\phi(z^\ell)\) and \(\delta^3=a\odot\phi'(z^3)\).
These equations follow by substituting the trained matrices into (13.1).
Conversely, a \(C^1\) solution of (13.3)–(13.5) with \(b(0)=0\)
and the stated initial data reconstructs (13.2): differentiation gives
\(R_1'=M_2^Tb'\), hence \((X^1)'=(W^{(2)})^Tb'\), while the
matrix and readout derivatives follow directly from their integrals.

There are precisely four initial-matrix actions in this representation:

| Initial action | Argument |
|---|---|
| \(W^{(2)}_0\) | \(h^1\) |
| \((W^{(2)}_0)^T\) | \(b\) |
| \(W^{(3)}_0\) | \(h^2\) |
| \((W^{(3)}_0)^T\) | \(\delta^3\) |

The lower backward vector \(\delta^2\) remains in the equation for
\(b'\). It is its primitive that enters the initial lower transpose.

### 13.2. A width-independent time net on a supplied path

Assume, on \([0,S]\),
\[
 \|W^{(2)}\|_{\rm op},\ \|W^{(3)}\|_{\rm op},\ \|a\|_\infty
 \le B,\qquad B\ge1. \tag{13.6}
\]
Write \(c=\pi/2\); then \(|\phi|\le c\), \(|\phi'|\le1\),
and \(|\phi''|\le2\). Thus
\(\frac{\|\delta^3\|_2}{\sqrt n}\le B\), \(\frac{\|q^2\|_2}{\sqrt n}\le B^2\), and
\(\frac{\|b'\|_2}{\sqrt n}=\frac{\|\delta^2\|_2}{\sqrt n}\le B^2\). Direct differentiation gives
\[
 \begin{aligned}
 (h^1)'&=\phi'(z^1)^2\odot(W^{(2)})^T\delta^2,\\
 (z^2)'&=\frac{\|h^1\|_2^2}{n}\delta^2+W^{(2)}(h^1)',\\
 (h^2)'&=\phi'(z^2)\odot(z^2)',\\
 (z^3)'&=\frac{\|h^2\|_2^2}{n}\delta^3+W^{(3)}(h^2)',\\
 (\delta^3)'&=h^3\odot\phi'(z^3)
                  +a\odot\phi''(z^3)\odot(z^3)'.
 \end{aligned} \tag{13.7}
\]
Consequently their Euclidean norms divided by \(\sqrt n\), in the same
order, are bounded by
\[
 B^3,\quad Z_2=(c^2+B^2)B^2,\quad Z_2,\quad
 Z_3=c^2B+BZ_2,\quad c+2BZ_3.
 \tag{13.8}
\]
In particular every argument in the table has \(\frac{\|v'\|_2}{\sqrt n}\le C\),
where \(C=\max\{1,B^2,B^3,Z_2,c+2BZ_3\}\) depends only on \(B\).
Integration proves \(\frac{\|v(s)-v(t)\|_2}{\sqrt n}\le C|s-t|\).

For \(\varepsilon>0\), choose a mesh of \([0,S]\) with gaps at most
\(\varepsilon/C\). It uses at most \(1+\lceil CS/\varepsilon\rceil\)
points when \(S>0\), and one when \(S=0\). If \(\pi(s)\) is the
last mesh point before \(s\), then for each table entry \((A,v)\),
\[
 \sup_{s\le S}\frac{\|A[v(s)-v(\pi(s))]\|_2}{\sqrt n}
 \le\|A\|_{\rm op}\varepsilon\le B\varepsilon.
 \tag{13.9}
\]
The last bound follows from (13.6) at time zero and equality of a matrix
and transpose operator norm. Thus each supplied trajectory admits a number
of sampled arguments per orientation independent of width. All trained
memory terms in (13.3)–(13.5) are still retained.

### 13.3. Continuity of the retained rank memories

For two \(C^1\) path pairs \((b,h)\), \((\widetilde b,\widetilde h)\)
with \(b(0)=\widetilde b(0)=0\), assume
\(\frac{\|h\|_2}{\sqrt n},\frac{\|\widetilde h\|_2}{\sqrt n}\le B_h\),
\(\frac{\|h'\|_2}{\sqrt n},\frac{\|\widetilde h'\|_2}{\sqrt n}\le L_h\), and
\(\frac{\|b'\|_2}{\sqrt n},\frac{\|\widetilde b'\|_2}{\sqrt n}\le L_b\).
Let \(e_b=\sup_s\frac{\|b-\widetilde b\|_2}{\sqrt n}\) and
\(e_h=\sup_s\frac{\|h-\widetilde h\|_2}{\sqrt n}\).
For \(M(s)=\int_0^s b'h^T/n\,du\), integration by parts gives
\[
 M-\widetilde M=(b-\widetilde b)h^T/n
 -\int_0^s(b-\widetilde b)(h')^T/n\,du
 +\int_0^s\widetilde b'(h-\widetilde h)^T/n\,du.
\]
The rank-one identity \(\|vw^T/n\|_{\rm op}=\|v\|_2\|w\|_2/n\)
follows by Cauchy–Schwarz, with equality in the direction of \(w\) when
both vectors are nonzero. Therefore
\[
 e_M:=\sup_s\|M-\widetilde M\|_{\rm op}
 \le(B_h+SL_h)e_b+SL_b e_h. \tag{13.10}
\]
For \(R(s)=\int_0^s M^Tb'\,du\), split its difference into
\(\int(M-\widetilde M)^Tb'\) and
\(\int\widetilde M^T(b'-\widetilde b')\).
Integrating the second term by parts, and using
\(\|\widetilde M\|_{\rm op}\le SL_bB_h\),
\(\|\widetilde M'\|_{\rm op}\le L_bB_h\), proves
\[
 \sup_s\frac{\|R-\widetilde R\|_2}{\sqrt n}
 \le SL_b e_M+2SL_bB_h e_b. \tag{13.11}
\]
These are the lower-memory bounds for \(h=h^1\). For top memory,
if both \(h^2\) paths satisfy \(\|h^2\|_2/\sqrt n\le B_2\) and both
\(\delta^3\) paths satisfy \(\|\delta^3\|_2/\sqrt n\le D_3\), the direct difference
of its two rank-one integrands gives
\[
 \sup_s\|M_3-\widetilde M_3\|_{\rm op}
 \le SB_2\sup_s\frac{\|\delta^3-\widetilde\delta^3\|_2}{\sqrt n}
       +SD_3\sup_s\frac{\|h^2-\widetilde h^2\|_2}{\sqrt n}. \tag{13.12}
\]
No convergence of \(b'\) was needed for (13.10)–(13.11); its uniform
bound and the regularity of \(h\) supplied the integration by parts.
The mesh estimate controls the residuals obtained by changing only the four
initial responses in the integral equations along the given path. It does
not estimate the difference of solutions of those changed equations.

### 13.4. What the representation still requires

A sampled actual query has been generated using all earlier matrix actions,
including actions at arguments absent from the retained mesh. Its value is
therefore not shown measurable from a transcript containing only the retained
calls. A proposed algorithm can use its own frozen responses and queries;
(13.9) proves consistency along the actual path, not stability of that
algorithm or legitimacy of conditioning its queries as independent Gaussian
innovations. No such conditioning is used in this section.

The nonlinear stability term is explicit. With the same zero primitive,
\[
 b(s)-\widetilde b(s)=\int_0^s\!
 \{\phi'(z^2)\odot(q^2-\widetilde q^2)
  +[\phi'(z^2)-\phi'(\widetilde z^2)]\odot\widetilde q^2\}\,du.
 \tag{13.13}
\]
The first summand has Euclidean norm divided by \(\sqrt n\) at most \(\frac{\|q^2-\widetilde q^2\|_2}{\sqrt n}\).
Splitting the second at any \(Q>0\) gives
\[
 \frac{\|[\phi'(z^2)-\phi'(\widetilde z^2)]\odot\widetilde q^2\|_2}{\sqrt n}
 \le 2Q\frac{\|z^2-\widetilde z^2\|_2}{\sqrt n}
    +2\frac{\|\widetilde q^2\mathbf1_{|\widetilde q^2|>Q}\|_2}{\sqrt n}.
 \tag{13.14}
\]
The mean value theorem bounds the first part and \(|\phi'|\le1\)
bounds the second. An RMS bound alone gives no uniform tail decay: the
vectors \(\sqrt n e_1\) have RMS one and tail RMS one for every
\(n>Q^2\). Taking \(z=e_1\), \(\widetilde z=0\), and
\(\widetilde q=\sqrt n e_1\) also makes the left side of (13.14) equal
to \(1/2\), although \(\frac{\|z-\widetilde z\|_2}{\sqrt n}=1/\sqrt n\).
These deterministic arrays refute a bound based only on those norms; they
are not asserted to be states reached by the initialized network.

Temporal Lipschitz bounds alone also give no strong Hilbert-space compactness.
In \(\ell^2\), the paths \(s\mapsto s e_j\) are uniformly bounded and
Lipschitz on \([0,S]\), but at fixed \(s>0\) distinct values are separated
by \(\sqrt2s\). No norm-convergent subsequence exists there.
Finally the lower backward response is
\[
 (W^{(2)})^T\delta^2
   =\frac{d}{ds}[(W^{(2)}_0)^Tb]+M_2^Tb'. \tag{13.15}
\]
Uniform approximation of the integrated response need not control its
derivative. For nonzero fixed \(v\), \(j^{-1}\sin(js)v\) tends uniformly
to zero and has bounded derivative, while the squared time-\(L^2\) norm of
its derivative is
\(\|v\|^2(S/2+\sin(2jS)/(4j))\), tending to \(S\|v\|^2/2\)
when \(S>0\). Hidden velocities and raw first-kernel convergence therefore
need additional control. None of these examples asserts a canonical network
counterexample. They identify the exact missing inferences between the finite
representation, causal approximation, state convergence and derivative
observables. Cap removal and autonomous population restart remain separate.
