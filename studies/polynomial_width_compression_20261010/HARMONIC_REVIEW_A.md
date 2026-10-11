# Independent audit A: Harmonic source-rank obstruction

2026-10-10. Independent isolated mathematical review, not a promotion review.

## Conclusion and input boundary

The proposed finite Gaussian source-rank lemma is correct, including its
constants and probability estimate. Its application rules out every fixed
polynomial qualifying-width threshold for the current Harmonic construction
while preserving both its canonical uniform source tolerance and its displayed
total-storage bound. I found no mathematical defect in that scoped conclusion.

This is an obstruction to the current source witness and literal selected-array
representation. It does not prove that every autonomous output approximator has
large storage, that the selected predictor cannot sometimes be accurate without
the source certificate, or that the paper's fixed-problem eventual theorem is
false. The candidate makes these distinctions correctly.

The following are the inspected scientific inputs and their SHA-256 hashes:

| Input | SHA-256 |
|---|---|
| `HARMONIC_ROUTE.md`, complete | `d19953be9d8182b493bd5677df5f375fb9f005d3a303ecdf769ca6151a56df8d` |
| `paper/compact.tex`, complete | `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` |
| `paper/compact_selected.tex`, complete | `3add2b694f38a4d7dbce90e51dafd375a7e8dee2e06d26b2d5af451bddb44885` |
| `docs/notation.qmd`, complete | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `paper/compact_foundations.tex`, only lines 1–75, the complete analytic-source proposition | `6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0` |
| `FINITE_ANTI_CONCENTRATION.md`, complete, separate optional audit below | `47c1a271a3e92d65b6b64682c1940602c5cd2131d46db3fe2b5c26418273a132` |

The foundations hash identifies the complete file; only the authorized
proposition was read. I did not read the study README, study history, other
reviews, the linked width-refinement note, other studies, or the source
proposition's proof. The rigorous-math and canonical-notation skills, including
the neural-network reference, were applied. No experiments were needed. Only
this report was written.

## The construction really has the necessary source and storage requirements

The paper uses normalized queries \(v=x/\sqrt d\in S^{d-1}\), independent
standard Gaussian first-layer entries, and

\[
h^{(1)}(0,v)=\phi(W^{(1)}(0)v).
\]

The formal source-family definition in `compact_foundations.tex` includes

\[
h^{(j)},\quad W^{(j)}(0)h^{(j-1)},\quad
\delta^{(j)},\quad W^{(j+1)}(0)^\top\delta^{(j+1)},
\]

with the forward image omitted for \(j=1\) and the reverse image omitted for
\(j=L\). The first-layer feature itself is included. The source-to-runtime proposition in
`compact_selected.tex` requires coordinatewise approximation of these families
on \([0,T]\), including time zero, and the Harmonic proof explicitly chooses
the canonical tolerance and whole-sphere feature coefficient spaces. Thus the
candidate has identified an actual requirement of this construction.

Writing \(C\ge1\) for the transfer constant, its chosen tolerance obeys

\[
\eta\le
\frac{\gamma}{2Cmn(1+\sqrt{m/\gamma})
(1+\sqrt{\log(en)})e^{\sqrt{\log(en)}}}\le\frac1n,
\]

since \(\gamma/m\le1\). This is a sufficient tolerance explicitly chosen by
the current Harmonic proof; it is not claimed to be necessary for all ways of
proving output accuracy.

The selection interface requires

\[
u_I^\top Mv_I=\frac{u^\top v}{n}\qquad(u,v\in E_1).
\]

Its autonomous model stores \(W_C^{(1)}\in\mathbb R^{|I|\times d}\),
initialized by restricting \(W^{(1)}(0)\) to \(I\). The inventory expressly
retains both its current and initial copies. Therefore \(E_1=\mathbb R^n\)
forces \(I=\{1,\ldots,n\}\): if \(j\notin I\), taking \(u=v=e_j\)
would equate zero to \(1/n\). Charging only one first matrix already gives

\[
\text{retained real coordinates}\ge nd.
\]

This is a literal-array conclusion in the paper's stated representation,
not an information-theoretic lower bound under unrestricted encodings.

## Independent derivation of the finite rank lemma

Let \(A\in\mathbb R^{n\times d}\) have independent standard Gaussian
entries and set \(F_A(v)=Av+\cos(Av)\). Fix even \(k\ge2\), \(d\ge k\),
and put

\[
c_k=\frac{e^{-4}4^{-k}}{2k!},\qquad
\frac{8\log(nd)}d\le
\min\left\{\frac14,\frac1{8\binom{k}{2}}\right\}.
\]

The sign cube \(v=s/\sqrt d\), \(s\in\{-1,1\}^d\), lies on the promised
sphere. Its orthonormal Walsh characters are

\[
\chi_S(s)=\prod_{j\in S}s_j.
\]

Put \(u_{ij}=A_{ij}/\sqrt d\). Expanding
\(\prod_j(\cos u_{ij}+is_j\sin u_{ij})\) and taking real parts shows that
the degree-\(k\) coefficient of row \(i\) is

\[
b_{i,S}=(-1)^{k/2}\prod_{j\in S}\sin u_{ij}
                       \prod_{j\notin S}\cos u_{ij},\qquad |S|=k.
\]

The linear term has only degree one. Let \(B=(b_{i,S})\) and \(G=BB^\top\).
I verify its lower spectral bound using a diagonal event and an unconditional
second-moment estimate; no conditioning on a trained network is involved.

On

\[
\frac12\le\sum_j u_{ij}^2\le2\quad\text{for all }i,
\qquad \max_{i,j}A_{ij}^2\le8\log(nd),
\]

we have \(|u_{ij}|\le1/2\). Integrating \(\tan t\le2t\) and
\(\cos t\ge\cos(1/2)>1/\sqrt2\) on \([0,1/2]\) gives

\[
\cos^2u\ge e^{-2u^2},\qquad \sin^2u\ge u^2/2.
\]

Thus \(\prod_j\cos^2u_{ij}\ge e^{-4}\). For \(x_j=\sin^2u_{ij}\),
write \(s_x=\sum_jx_j\ge1/4\) and

\[
e_k(x)=\sum_{|S|=k}\prod_{j\in S}x_j.
\]

The ordered terms with any repeated index in \(s_x^k\) have total weight
at most

\[
\binom{k}{2}\Big(\sum_jx_j^2\Big)s_x^{k-2}
\le\binom{k}{2}(\max_jx_j)s_x^{k-1}.
\]

Since \(\max_jx_j\le8\log(nd)/d\), the assumed bound makes the
last expression at most \(s_x^k/2\). Consequently

\[
k!e_k(x)\ge\tfrac12s_x^k\ge\tfrac12 4^{-k},\qquad
G_{ii}\ge e^{-4}e_k(x)\ge c_k.
\]

The Gaussian moment generating function gives, with \(t=1/4\) for the
upper tail and \(t=-1/2\) for the lower tail,

\[
\Pr(\|A_{i,:}\|_2^2\ge2d)\le
e^{-(1-\log2)d/2}\le e^{-d/16},
\]
\[
\Pr(\|A_{i,:}\|_2^2\le d/2)\le
e^{-(\log2/2-1/4)d}\le e^{-d/16}.
\]

The two numerical exponents are greater than \(1/16\). Union over rows,
and the scalar bound \(\Pr(|Z|>u)\le2e^{-u^2/2}\), give diagonal-event
failure at most

\[
2ne^{-d/16}+2nd\,e^{-4\log(nd)}
=2ne^{-d/16}+2(nd)^{-3}.
\]

For distinct subsets \(S,T\) of size \(k\), the expectation of
\(b_{i,S}b_{i,T}\) vanishes: a coordinate in their symmetric difference
contributes the odd factor \(\sin(Z/\sqrt d)\cos(Z/\sqrt d)\). With

\[
\theta_d=\mathbb E\sin^2(Z/\sqrt d)
=\frac{1-e^{-2/d}}2\le\frac1d,
\]

the diagonal coefficient second moment is
\(\mathbb E b_{i,S}^2=\theta_d^k(1-\theta_d)^{d-k}\).
Independence between rows now gives, for \(i\ne j\),

\[
\mathbb E G_{ij}^2
=\binom dk\theta_d^{2k}(1-\theta_d)^{2d-2k}
\le\frac1{k!d^k}.
\]

Therefore Markov's inequality yields

\[
\Pr\!\left(\|G-\operatorname{diag}G\|_F>c_k/2\right)
\le\frac{4n(n-1)}{c_k^2k!d^k}.
\]

Combining events by a union bound and using the Frobenius bound on operator
norm proves

\[
G\succeq\frac{c_k}{2}I_n
\]

with precisely the probability asserted in the candidate. A possibly negative
finite lower bound for that probability is simply vacuous; the application
below makes all failure terms tend to zero.

Let \(E\subset\mathbb R^n\) be any linear space satisfying the asserted
uniform coordinate approximation and let \(P\) be its Euclidean orthogonal
projection. Euclidean projection minimizes Euclidean distance, and an
\(\ell^\infty\) error at most \(\eta\) has Euclidean norm at most
\(\sqrt n\eta\). Hence, by Walsh Parseval and positivity of discarded
degrees,

\[
\begin{aligned}
n\eta^2
&\ge\mathbb E_s\|(I-P)F_A(s/\sqrt d)\|_2^2\\
&\ge\|(I-P)B\|_F^2
=\operatorname{tr}((I-P)G)
\ge\frac{c_k}{2}(n-\dim E).
\end{aligned}
\]

This proves the claimed dimension estimate. The event depends only on \(A\),
so it holds simultaneously for every possible \(E\), including a space chosen
after seeing every initialized block. If \(\eta\le1/n\) and \(n>2/c_k\),
the nonnegative integer \(n-\dim E\) is less than one and is therefore zero.

## Admissibility of the fixed training family

Take two hidden layers and \(\phi(z)=z+\cos z\). This activation is entire
and real on the real line. On \(|\operatorname{Im}z|<1\),
\(|\phi'(z)|\le1+\cosh1\); on the half-strip,
\(|\phi''(z)|\le\cosh(1/2)\). Its value at zero is one. Thus the
paper's exact envelope formula gives \(\beta=16\) with strip \(a=1\), and
unbounded real values are explicitly permitted by the paper.

For \(m=2\), use \(v_1=e_1\), \(v_2=(e_1+\sqrt3e_2)/2\). The corresponding
inputs \(x_a=\sqrt d\,v_a\) have the required norm. For centered jointly
Gaussian variables of common variance \(q\) and covariance \(c\), symmetry
under simultaneous sign reversal removes both linear-cosine cross terms.
The identity \(2\cos u\cos v=\cos(u-v)+\cos(u+v)\), together with the
Gaussian characteristic function, gives

\[
\mathbb E[\phi(Z_1)\phi(Z_2)]=c+e^{-q}\cosh c.
\]

Consequently the candidate's recursion for the diagonal \(q_\ell\) and
off-diagonal \(c_\ell\) of the uncentered population feature Gram is exact.
Starting from \((1,1/2)\), it preserves \(q_\ell>c_\ell\ge0\), and each
gap increment is positive and strictly less than \(1/2\). Thus

\[
\frac12<\gamma=q_2-c_2<\frac32<2=m.
\]

This is exactly the least eigenvalue of the two-by-two Gram. It is independent
of \(d\). The constant positive labels \(y_1=y_2=Y=\gamma\beta^{-60}/4\)
have label RMS \(Y\) and satisfy

\[
0<Y<\frac\gamma2\beta^{-60}
=\frac\gamma m\beta^{-30L}.
\]

All advertised admissibility conditions therefore hold with every parameter
except \(d,n\) fixed. The initialization argument requires neither an event
for later layers nor a fitting or complex-source probability estimate.

## Polynomial quantifiers and the storage comparison

Fix any real \(a>1\) and choose an even integer \(k>2a\), once before the
dimension limit. Set \(n=\lceil d^a\rceil\). Then

\[
\frac{8\log(nd)}d\longrightarrow0,\qquad
2ne^{-d/16}\longrightarrow0,\qquad
2(nd)^{-3}\longrightarrow0,\qquad
\frac{4n(n-1)}{c_k^2k!d^k}=O_{a,k}(d^{2a-k})\longrightarrow0.
\]

Also \(n>2/c_k\) eventually. Although \(c_k\) can be extremely small, it is
strictly positive and independent of \(d\). It changes the finite onset only.
The event forcing \(E_1=\mathbb R^n\) therefore has probability tending to one.

For every fixed positive headline constant \(C\), and fixed
\(z=Ym/\gamma>0\), the logarithm of the second storage term is

\[
\log\!\left[(C/d)^{d+1}z^4
          \{\log(e\lceil d^a\rceil)\}^{3d+2}\right]
=-d\log d+3d\log\log d+O_{a,C,z}(d)\longrightarrow-\infty.
\]

The advertised count is consequently \(O_C(d^2)\), whereas the required
first matrix alone has \(nd\ge d^{a+1}\) coordinates. Their ratio diverges.

If a proposed threshold, at any fixed positive confidence, is bounded by
\(K(1+d)^b\) after the other parameters are fixed, choosing
\(a>\max\{b,1\}\) places this entire sequence above that threshold
eventually. Yet the joint source-contract/storage success probability tends
to zero. This contradicts the proposed positive fixed confidence. It covers
every finite degree \(b\), including degrees depending on the fixed activation
or depth. It does not use a degree \(k\) growing with \(d\).

The optional \(m=d\) example is valid too. Starting the same covariance
recursion from \((q_0,c_0)=(1,0)\) yields
\(Q^{(2)}=(q_2-c_2)I+c_2\mathbf1\mathbf1^\top\) and
\(1<\gamma=q_2-c_2<2\). With
\(Y_m=\gamma\beta^{-60}/(2m)\), the ratio \(Y_m m/\gamma\) stays constant,
while \(Y_m^{-1}\) and \(m/\gamma\) grow linearly in \(m\). A polynomial
in these parameters is a polynomial in \(m\), and the same contradiction
applies. This variant does vary the positive labels; the main example does not.

The original eventual theorem holds \(d\) and the other problem data fixed
while taking \(n\to\infty\), and explicitly disclaims a polynomial onset.
The growing-\(d\) sequence here does not refute that theorem.

## Separate optional audit: finite anti-concentration

The standalone anti-concentration lemma is correct for independent identically
distributed centered variables, and its stated constant 2000 is sufficient.
This conclusion supplies no further evidence for the Harmonic obstruction.

For \(\mathbb EX=0\), \(\mathbb EX^2=\sigma^2>0\),
\(\mathbb E|X|^3=M_3<\infty\), and an independent copy \(X'\),
the third-order cosine remainder gives

\[
|\mathbb Ee^{itX}|^2
\le1-\sigma^2t^2+\frac{|t|^3}{6}\mathbb E|X-X'|^3
\le1-\sigma^2t^2+\frac43M_3|t|^3.
\]

For \(|t|\le3\sigma^2/(8M_3)\), this is at most
\(1-\sigma^2t^2/2\le e^{-\sigma^2t^2/2}\). Independence therefore
gives, for \(Z=\sum_iX_i/(\sigma\sqrt n)\),

\[
|\mathbb Ee^{iuZ}|\le e^{-u^2/4}
\quad\text{if }|u|\le R=\frac{3\sigma^3\sqrt n}{8M_3}.
\]

The Gaussian majorant of an interval and its integrable Fourier transform
give, uniformly in \(b\in\mathbb R\),

\[
\Pr(|Z-b|\le a)
\le\frac{\sqrt e\,a}{\sqrt{2\pi}}
\int_{\mathbb R}e^{-a^2u^2/2}|\mathbb Ee^{iuZ}|\,du
\le\sqrt{2e}\,a+2\sqrt e\,e^{-a^2R^2/2}.
\]

The first term integrates \(e^{-u^2/4}\) over the whole line. The second
uses modulus at most one outside \([-R,R]\) and the Gaussian two-tail bound.
For \(a=\delta/10\), the proposed width assumption implies

\[
\frac{a^2R^2}{2}
=\frac{9\delta^2\sigma^6n}{12800M_3^2}
\ge\frac{18000}{12800}\log(16/\delta)
\ge\log(16/\delta).
\]

The resulting bound is
\((\sqrt{2e}/10+\sqrt e/8)\delta<\delta\). This verifies both the
normalization and the numerical slack.

One small wording improvement is advisable: the conditional version must
explicitly retain **conditional independence and identical distribution**,
as well as the conditional moment assumptions, and its shift must be
measurable with respect to the conditioning sigma-field. Conditional moments
alone would not suffice: independent symmetric signs conditioned to have sum
zero retain conditional mean zero, variance one and third absolute moment one,
but their sum is deterministically zero. The natural reading of “the same
assertion holds conditionally” retains all assumptions, so this is a
clarification rather than a defect in the proved result. The advertised
final-layer application does state the needed conditional iid property.

At the paper's zero initial readout, differentiating
\(f_n=w^\top h^{(L)}/n\) eliminates the feature-velocity term and gives
exactly

\[
\dot f_n(0,x_a)=\frac2{mn}\sum_i h_i^{(L)}(0,x_a)
                         \sum_b y_bh_i^{(L)}(0,x_b).
\]

Conditional on lower initialized layers, these row products are iid; for
application of the centered lemma their conditional means must be subtracted
and included in the shift. Conditioning further on an independent reference
network preserves their conditional iid law. As the candidate states, a
quantitative conditional variance lower bound, moment control on a suitable
event, and a derivative-to-trajectory estimate are still required. The lemma
alone is not a polynomial-width dense-variability theorem.

## Audit disposition

Accept the Harmonic source-witness obstruction at its stated scope. No
correction to its finite lemma or polynomial contradiction is required.
The separate finite anti-concentration lemma also passes, with the conditional
independence wording clarification above. No general output-compression
impossibility or complete polynomial-width theorem is established by either
result.
