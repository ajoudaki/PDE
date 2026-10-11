# Harmonic route: a rank obstruction to polynomial qualifying width

2026-10-10. Scoped author proof, not an independent review or promotion.
The current Harmonic construction cannot retain its stated total-storage
bound at a qualifying width polynomial in input dimension. This obstruction
already occurs at initialization, with fixed depth, fixed positive labels,
two correlated training inputs, and an admissible unbounded activation.
It does not use a defect in the complex-source probability argument.

The scope is precise: the result concerns the current construction's
uniform coordinate approximation of its forward source by a linear neuron
space, followed by exact-metric coordinate selection and the explicitly
stored selected first matrix. It is not a lower bound for every possible
predictor that approximates the trained output. A replacement that avoids
this source requirement would need a different comparison argument; the
present obstruction does not decide whether such a replacement exists.

## 1. Current interface and the claim under test

The relevant current interfaces are in `paper/compact_selected.tex`:

- The source-to-runtime proposition requires a linear space
  \(E_1\subset\mathbb R^n\) approximating the initial forward source,
  in particular
  \[
  h^{(1)}(0,v)=\phi(W^{(1)}(0)v),\qquad v\in S^{d-1},
  \]
  to coordinate error \(\eta\), uniformly on the sphere.
- Its canonical tolerance satisfies
  \[
  \eta\le
  \frac{\gamma}{2Cmn(1+\sqrt{m/\gamma})
         (1+\sqrt{\log(en)})e^{\sqrt{\log(en)}}}
  \le\frac1n,
  \tag{1}
  \]
  because \(C\ge1\) and \(\gamma/m\le1\).
- Exact-metric selection satisfies
  \[
  u_I^\top Mv_I=u^\top v/n\qquad(u,v\in E_1).
  \tag{2}
  \]
- The selected model retains the first matrix
  \(W_C^{(1)}\in\mathbb R^{|I|\times d}\), with
  \(W_C^{(1)}(0)=W^{(1)}(0)_{I,:}\). The retained inventory explicitly
  includes both its current and initial copies.

The Harmonic proof constructs such source spaces and claims, in its
fixed-problem eventual range, total storage at most
\[
 B_C(n,m,d,Y,\gamma)
 =C(m+d)^2+
 \left(\frac Cd\right)^{d+1}
 \left(\frac{Ym}{\gamma}\right)^4[\log(en)]^{3d+2},
 \tag{3}
\]
where \(C\) depends only on activations and depth. We test whether the
same bound and the same construction can hold once width exceeds a
polynomial in the displayed problem parameters. A polynomial here has
fixed finite degree; its degree cannot increase with input dimension.

The answer is negative even at fixed confidence, fixed \(m,\gamma,Y,L\)
and fixed activation. For every proposed polynomial threshold in \(d\),
there is a sequence of widths above that threshold at which every source
space meeting (1) is \(\mathbb R^n\), with probability tending to one.
Equation (2) then selects all first-layer coordinates, whose first matrix
alone costs \(nd\), exceeding (3).

## 2. One fixed admissible family of training problems

Take two hidden layers, \(L=2\), and the same activation in both:
\[
 \phi(z)=z+\cos z.
 \tag{4}
\]
It is real on the real axis and entire. On \(|\operatorname{Im}z|<1\),
\(|\phi'(z)|=|1-\sin z|\le1+\cosh1\); its second derivative is
bounded on the half-strip by \(\cosh(1/2)\). Its values on the real
axis are unbounded. Thus the current activation class applies with strip
\(a=1\) and the paper's envelope \(\beta=16\).

For every \(d\ge2\), let \(m=2\) and take normalized training inputs
\[
 v_1=e_1,\qquad v_2=(e_1+\sqrt3e_2)/2,
 \qquad x_a=\sqrt d\,v_a.
 \tag{5}
\]
Their correlation is \(1/2\). The initial population covariance at each
layer has diagonal \(q_\ell\) and off-diagonal \(c_\ell\), with
\((q_0,c_0)=(1,1/2)\). For centered jointly Gaussian variables with
variance \(q\) and covariance \(c\), simultaneous sign symmetry kills
the terms \(\mathbb E[Z_1\cos Z_2]\). The elementary Gaussian
characteristic function gives
\[
 \mathbb E[\cos Z_1\cos Z_2]=e^{-q}\cosh c.
\]
Therefore the exact layer recursion is
\[
 q_{\ell+1}=q_\ell+e^{-q_\ell}\cosh q_\ell,
 \qquad
 c_{\ell+1}=c_\ell+e^{-q_\ell}\cosh c_\ell.
 \tag{6}
\]
In particular \(q_\ell>c_\ell\ge0\), and the smaller eigenvalue
at the top layer is
\(\gamma=q_2-c_2\), independent of \(d\). Each gap increment is
positive and less than \(1/2\), since
\[
 0<e^{-q}(\cosh q-\cosh c)
 \le e^{-q}(\cosh q-1)
 =\tfrac12(1-e^{-q})^2<\tfrac12.
\]
Hence \(1/2<\gamma<3/2< m\), verifying both the positive feature
gap and \(m/\gamma\ge1\). Fix labels \(y_1=y_2=Y\), where
\[
 Y=\frac{\gamma}{4}\,\beta^{-60}>0.
 \tag{7}
\]
Then the paper's small-label condition
\(Y\le(\gamma/m)\beta^{-30L}\) holds, with strict slack. Every
parameter other than \(d,n\), including \(Ym/\gamma\), is now fixed.
All initialized first-layer rows remain independent \(N(0,I_d)\),
and all other blocks and the optimizer have the paper's unchanged law.

## 3. A finite Gaussian source-rank lemma

Let \(A\in\mathbb R^{n\times d}\) have independent standard Gaussian
entries, and let
\[
 F_A(v)=Av+\cos(Av)\in\mathbb R^n,
 \qquad v\in S^{d-1},
 \tag{8}
\]
where cosine is coordinatewise. Fix an even integer \(k\ge2\), with
\(d\ge k\), and define the positive constant
\[
 c_k=\frac{e^{-4}4^{-k}}{2k!}.
 \tag{9}
\]
Assume
\[
 \frac{8\log(nd)}d
 \le\min\left\{\frac14,\frac1{8\binom{k}{2}}\right\}.
 \tag{10}
\]
With probability at least
\[
 1-2ne^{-d/16}-2(nd)^{-3}
   -\frac{4n(n-1)}{c_k^2 k!d^k},
 \tag{11}
\]
every linear subspace \(E\subset\mathbb R^n\) satisfying
\[
 \sup_{v\in S^{d-1}}\inf_{u\in E}\|F_A(v)-u\|_\infty
 \le\eta
 \tag{12}
\]
obeys
\[
 n-\dim E\le\frac{2n\eta^2}{c_k}.
 \tag{13}
\]
The event in (11) holds simultaneously for all spaces \(E\), including
spaces chosen after seeing \(A\). In particular, if
\(\eta\le1/n\) and \(n>2/c_k\), then \(E=\mathbb R^n\).

Here is a complete proof using a finite subset of the sphere. For
\(s\in\{-1,1\}^d\), put \(v=s/\sqrt d\). Give this finite set its
uniform probability measure. For each coordinate subset
\(S\subset\{1,\ldots,d\}\), define its Walsh character
\(\chi_S(s)=\prod_{j\in S}s_j\). Independence of the signs gives
\(\mathbb E_s\chi_S\chi_T=1\) when \(S=T\) and zero otherwise;
these \(2^d\) characters form an orthonormal basis for all real
functions on the sign cube.

Write \(u_{ij}=A_{ij}/\sqrt d\). The product identity
\[
 e^{i\sum_j u_{ij}s_j}
 =\prod_{j=1}^d(\cos u_{ij}+i s_j\sin u_{ij})
\]
shows that the degree-\(k\) Walsh coefficient in row \(i\) of (8) is
\[
 b_{i,S}=(-1)^{k/2}
       \prod_{j\in S}\sin u_{ij}
       \prod_{j\notin S}\cos u_{ij},\qquad |S|=k.
 \tag{14}
\]
The linear part of (8) has Walsh degree one and contributes nothing.
Let \(B\in\mathbb R^{n\times\binom dk}\) be the matrix with
entries (14), and set \(G=BB^\top\).

We first lower-bound its diagonal. On the event
\[
 \tfrac12\le\sum_j u_{ij}^2\le2\quad\text{for every }i,
 \qquad
 \max_{i,j}A_{ij}^2\le8\log(nd),
 \tag{15}
\]
condition (10) gives \(|u_{ij}|\le1/2\). On this interval
\(\cos^2u\ge e^{-2u^2}\) and \(\sin^2u\ge u^2/2\).
For the first inequality, integrate
\(\tan t\le2t\) on \([0,1/2]\); the latter bound follows from
\(\cos t\ge\cos(1/2)>1/\sqrt2\), or by integrating that lower
derivative bound for sine. Thus
\[
 \prod_j\cos^2u_{ij}\ge e^{-4},\qquad
 \sum_j\sin^2u_{ij}\ge\frac14,
 \qquad \max_j\sin^2u_{ij}\le\frac{8\log(nd)}d.
 \tag{16}
\]
For nonnegative numbers \(x_j\), write \(s_x=\sum_jx_j\) and
let \(e_k(x)=\sum_{|S|=k}\prod_{j\in S}x_j\). Among the ordered
terms in \(s_x^k\), the total contribution of tuples with a repeated
index is at most
\[
 \binom{k}{2}\left(\sum_jx_j^2\right)s_x^{k-2}
 \le\binom{k}{2}(\max_jx_j)s_x^{k-1}.
\]
Consequently (10) and (16), with \(x_j=\sin^2u_{ij}\), give
\[
 k!e_k(x)\ge s_x^k
 \left(1-\binom{k}{2}\frac{\max_jx_j}{s_x}\right)
 \ge\tfrac12 4^{-k}.
\]
In (14), the product of the cosine squares over \(j\notin S\)
is at least their product over all \(j\), since each factor is in
\([0,1]\). It follows that
\[
 G_{ii}=\sum_{|S|=k}b_{i,S}^2\ge e^{-4}e_k(x)\ge c_k.
 \tag{17}
\]

For completeness, the failure probability of (15) has the first two
terms in (11). The Gaussian identity
\(\mathbb Ee^{t\|A_{i,:}\|_2^2}=(1-2t)^{-d/2}\) gives
\[
 \Pr(\|A_{i,:}\|_2^2\ge2d)
 \le e^{-d/2}2^{d/2}\le e^{-d/16},
\]
by \(t=1/4\), and
\[
 \Pr(\|A_{i,:}\|_2^2\le d/2)
 \le e^{d/4}2^{-d/2}\le e^{-d/16},
\]
by \(t=-1/2\). Union over rows gives \(2ne^{-d/16}\).
The scalar Gaussian bound
\(\Pr(|Z|>u)\le2e^{-u^2/2}\), obtained from its exponential
moment and optimized in the exponent, gives the entrywise failure
\(2nd\,e^{-4\log(nd)}=2(nd)^{-3}\).

It remains to control off-diagonal entries of \(G\). For a standard
Gaussian \(Z\), let
\[
 \theta_d=\mathbb E\sin^2(Z/\sqrt d)
       =\frac{1-e^{-2/d}}2\le\frac1d.
\]
Within a single Gaussian row, (14) implies
\[
 \mathbb E[b_{i,S}b_{i,T}]=0\quad(S\ne T),
 \qquad
 \mathbb E b_{i,S}^2=\theta_d^k(1-\theta_d)^{d-k}.
 \tag{18}
\]
For the first equality, a coordinate in the symmetric difference
\(S\mathbin\triangle T\) contributes the odd factor
\(\sin(Z/\sqrt d)\cos(Z/\sqrt d)\), whose expectation is zero.
Independence of distinct rows and (18) give, for \(i\ne j\),
\[
 \mathbb E G_{ij}^2
 =\binom dk\theta_d^{2k}(1-\theta_d)^{2d-2k}
 \le\frac1{k!d^k}.
\]
Writing \(G_{\rm off}=G-\operatorname{diag}(G)\), Markov's
inequality therefore gives
\[
 \Pr(\|G_{\rm off}\|_F>c_k/2)
 \le\frac{4n(n-1)}{c_k^2k!d^k}.
 \tag{19}
\]
On the intersection with (15), (17) and
\(\|G_{\rm off}\|_{\rm op}\le\|G_{\rm off}\|_F\) imply
\[
 G\succeq(c_k/2)I_n.
 \tag{20}
\]
This proves the claimed event probability without conditioning on any
training trajectory or any other Gaussian matrix block.

Finally let \(P\) be Euclidean orthogonal projection onto \(E\).
Equation (12) implies
\(\|(I-P)F_A(v)\|_2^2\le n\eta^2\) for every query. Apply
the finite Walsh Parseval identity to the vector-valued function
\((I-P)F_A(s/\sqrt d)\), retaining just its degree-\(k\) terms:
\[
 n\eta^2
 \ge\mathbb E_s\|(I-P)F_A(s/\sqrt d)\|_2^2
 \ge\|(I-P)B\|_F^2
 =\operatorname{tr}((I-P)G)
 \ge\frac{c_k}{2}(n-\dim E).
\]
This is (13). The last rank conclusion follows because \(n-\dim E\)
is a nonnegative integer and \(2n\eta^2/c_k\le2/(c_kn)<1\).

## 4. Every polynomial width threshold fails for the current construction

Fix any exponent \(a>1\) and set \(n=\lceil d^a\rceil\).
Choose once and for all an even integer \(k>2a\). This choice is an
analysis parameter; it changes neither the activation (4) nor the
network, source, dataset or algorithm. Condition (10) holds for all
sufficiently large \(d\), and every failure term in (11) tends to
zero: the last one is \(O_{a,k}(d^{2a-k})\). Also \(n>2/c_k\)
eventually. Thus, with probability tending to one, the initial source
requirement and canonical tolerance force
\[
 E_1=\mathbb R^n.
 \tag{21}
\]
Any set \(I\) satisfying (2) must then contain all \(n\) coordinates.
Indeed, if \(j\notin I\), choosing \(u=v=e_j\in E_1\) makes the
left side zero and the right side \(1/n\), a contradiction. The
current selected first matrix therefore retains at least \(nd\) real
coordinates, even if every other array is ignored.

For the fixed family in Section 2, put \(z=Ym/\gamma>0\), which is
independent of \(d\). At \(n=\lceil d^a\rceil\), the second term
of (3) tends to zero. Its logarithm is
\[
 (d+1)(\log C-\log d)+4\log z
 +(3d+2)\log\log(e\lceil d^a\rceil)
 =-d\log d+3d\log\log d+O_{a,C,z}(d)\longrightarrow-\infty.
 \tag{22}
\]
Consequently (3) is \(O_C(d^2)\), while the necessary first-matrix
storage satisfies
\[
 \frac{nd}{d^2}\ge d^{a-1}\longrightarrow\infty.
 \tag{23}
\]
This contradicts the claimed storage bound on an event whose probability
tends to one.

More explicitly, suppose a qualifying threshold is bounded by
\(K(1+d)^b\) after fixing all the other parameters of Section 2 and
fixing confidence, say at \(1-\delta=3/4\). Choose
\(a>\max\{b,1\}\). Then \(\lceil d^a\rceil\) exceeds the
threshold eventually, but (21)--(23) forbid success of the current
construction with probability tending to one. This refutes every finite
polynomial degree \(b\), not merely exponents below two. It also
permits arbitrary fixed constants depending on activation and depth.

The current fixed-\(d\), fixed-problem eventual theorem is not
contradicted: its onset can occur after these polynomial-width ranges.
The obstruction is exactly to upgrading that onset to a polynomial in
dimension while retaining both the present source construction and (3).

## 5. Optional sample-size version with \(m=d\)

The same argument can be expressed with growing sample count. Take
\(m=d\), \(v_a=e_a\), and keep (4), \(L=2\), and \(\beta=16\).
The population covariance at every layer is
\[
 Q^{(\ell)}=(q_\ell-c_\ell)I_m+c_\ell\mathbf1\mathbf1^\top,
\]
where (6) now starts at \((q_0,c_0)=(1,0)\). Because
\(c_\ell\ge0\), its least eigenvalue is
\(\gamma=q_2-c_2\), again independent of \(m,d\), and
\(1<\gamma<2\). Set every label equal to
\[
 Y_m=\frac{\gamma}{2m}\,\beta^{-60}.
\]
The small-label condition holds, \(Ym/\gamma=\beta^{-60}/2\) is
constant, and \(Y_m^{-1}\), \(m/\gamma\), and \(d\) are all
polynomial in \(m\). Any threshold polynomial jointly in those
parameters reduces to a polynomial in \(m\). Choosing a larger fixed
exponent \(a>1\), \(n=\lceil m^a\rceil\), and an even
\(k>2a\), the same event forces first-matrix storage \(nd\),
whereas (3) is \(O_C(m^2)\). This variant directly tests sample-size
dependence but uses a varying label amplitude. The primary construction
in Sections 2--4 avoids that issue by fixing \(Y\) and \(m=2\).

## 6. What this resolves, and what remains open

The factorial tail factor in the current Harmonic approximation lemma is
loose, and its exact weighted lattice count is valid before asymptotic
simplification. Neither fact resolves the present obstruction. No sharper
harmonic tail, exact volume estimate, or rank-revealing calculation can
produce a low-dimensional uniform source space when (20) holds. A
full-width fallback has valid approximation error but needs at least
\(nd\), which (22)--(23) show is not paid for by the unchanged headline.

Likewise, shortening the complex-time radius can remove deterministic
contour gates but cannot change (8), which is at time zero. Quantifying
the whole-query analytic source probability does not change this rank
argument. The earlier finite-training-source repair in
`WIDTH_GATE_REFINEMENT.md` explicitly does not claim a new whole-sphere
complex-source theorem; extending it would leave this separate storage
obstruction intact.

The following distinctions are essential:

| Claim | Status established here |
|---|---|
| All source spaces approximating the current initial first-layer source to \(\eta\le1/n\) have full rank at the specified polynomial widths | Proved, with explicit failure probability (11) |
| Current exact-metric selected construction then needs more storage than (3) | Proved from its stated first-matrix representation |
| A qualifying width polynomial in \(d\) can preserve this construction and (3) | Ruled out, even with all other problem parameters fixed |
| The existing fixed-problem eventual Harmonic theorem is false | Not asserted; the proof does not imply this |
| Every autonomous output approximation needs this much storage | Open; the proof does not imply this |
| An output-only comparison using a different source contract can meet the requested bound | Open and outside this obstruction |

The rank argument uses a subset of the promised whole-sphere domain and
allows arbitrary data-dependent source subspaces. It assumes no training
path approximation, width-independent lower singular value for a growing
spherical-harmonic basis, or independence after training. The degree
\(k\) is fixed before taking the dimension limit; its small constant
\(c_k\) only increases the finite starting dimension, and cannot repair
a polynomial threshold. No source or retained-state factor is hidden in
a confidence gate.

Scientific inputs inspected for this scoped route were the current setup,
source constants, domain verification, selected model, source tolerance,
inventory and Harmonic approximation passages in `paper/compact.tex`,
`paper/compact_foundations.tex` and `paper/compact_selected.tex`; the
assigned polynomial-width study README; the established notation and
book entry point; and the directly relevant prior Harmonic/source-radius
and width-factorization passages. The new proof itself uses only the
current interfaces cited in Section 1 and the explicit elementary
calculations above. No older-study theorem is assumed in the obstruction.
No paper or book edits, experiments, or Git mutations were performed.
