# One-point Padé: verified analytic guarantees and their limits

Research note, 6 September 2026. This note supplies exact sufficient conditions and prevents overreading general Padé convergence results. It does not assert that a neural population observable has the required analytic continuation or Borel-summability properties.

## Definition and distinct approximation questions

For a formal series \(F(z)=\sum_{j\ge0}a_jz^j\), a Padé pair of type \([p/q]\) satisfies

\[
\deg P\le p,\quad \deg Q\le q,\quad Q\not\equiv0,
\qquad QF-P=O(z^{p+q+1}).
\]

The rational function \(P/Q\) is unique although the polynomial pair need not be unique. When \(Q(0)\ne0\), one normalizes \(Q(0)=1\), and the rational function itself matches the series through degree \(p+q\). Degenerate entries can have common zeros at zero; after cancellation their actual contact order needs care. Under the convergence theorems below the relevant entries are eventually well behaved.

The coefficients used are only \(a_0,\ldots,a_{p+q}\). They can be genuine Taylor coefficients or formal asymptotic coefficients; existence of the algebraic rational approximant does not imply convergence to a given function.

Source for definition/existence/uniqueness and defects: Beckermann and Matos, *Algebraic properties of robust Padé approximants*, arXiv:1310.2438, pp. 1–3, https://arxiv.org/pdf/1310.2438.

Arbitrary rational approximation is different. Every continuous function on [0,T] is uniformly approximable by polynomials (Bernstein's elementary approximation theorem suffices), hence by rational functions. These approximants use function values or global information and need not be Padé approximants of its initialization jet. A flat nonzero function \(e^{-1/t^2}\), extended by zero at zero, has zero jet, whose normal rational Padé approximants are zero. Thus mere continuous/smooth rational approximability supplies no initialization-jet reconstruction theorem.

## Positive ordinary-Padé theorem: de Montessus fixed row

Suppose F is analytic near zero and has a meromorphic continuation to the disk \(|z|<R\), with exactly q poles there, counted with multiplicity. Fix this denominator degree q and let numerator degree p tend to infinity. Then

\[
[p/q]_F\longrightarrow F
\]

uniformly on each compact subset of that disk avoiding the poles. In particular, if T<R and no pole lies on [0,T], then for every epsilon>0 some finite p gives

\[
\sup_{0\le t\le T}|[p/q]_F(t)-F(t)|<\varepsilon.
\]

The denominators converge to the polynomial with exactly those poles as zeros; hence they have no spurious poles near the compact interval for all sufficiently large p. This theorem does not require that the Taylor disk itself contain [0,T]. Nearby complex poles can limit the Taylor radius and be captured by the fixed-degree denominator.

More exact rate statement: let R_q be the largest meromorphy-disk radius with at most q poles and suppose the disk has exactly q poles. For any compact K avoiding them,

\[
\limsup_{p\to\infty}\|F-[p/q]_F\|_K^{1/p}
\le \frac{\max_{z\in K}|z|}{R_q}<1.
\]

The inequality is sufficient here; the cited paper gives a sharp formulation. Its notation \(\pi_{n,q}\) means numerator degree n−q, so substitute n=p+q when comparing statements.

Verified source: Cacoq, de la Calle Ysern and López Lagomasino, *Incomplete Padé approximation and convergence of row sequences of Hermite-Padé approximants*, arXiv:1111.2774, p. 2, named “Montessus de Ballore Theorem,” https://arxiv.org/pdf/1111.2774. The paper defines R_q on p. 1 and explicitly states compact sup-norm convergence and pole attraction. Published J. Approx. Theory 170 (2013), 59–77, DOI https://doi.org/10.1016/j.jat.2012.05.005.

Simple example, independently checked:

\[
F(t)=\frac1{1+t},\qquad
\sum_{j\ge0}(-t)^j\text{ diverges for }t>1,
\qquad [0/1]_F(t)=F(t).
\]

Thus failure of Taylor partial sums on [0,T] can coexist with exact finite Padé reconstruction. This example is analytic at zero and does not address a zero-radius asymptotic series.

## Stahl's theorem is weaker than the requested supremum norm

A safe relevant specialization: for an analytic germ with continuation along paths avoiding a finite set of branch points (more generally the appropriate compact set of zero logarithmic capacity), diagonal/near-diagonal Padé approximants converge in logarithmic capacity in a distinguished domain of single-valued continuation, determined through a minimum-capacity cut. This is not uniform convergence on every compact subset. Tiny exceptional sets may contain poles; even one genuine approximant pole in [0,T] makes the supremum error unbounded.

Primary source: Herbert Stahl, *The Convergence of Padé Approximants to Functions with Branch Points*, J. Approx. Theory 91 (1997), 139–204, DOI https://doi.org/10.1006/jath.1997.3141, publisher https://www.sciencedirect.com/science/article/pii/S0021904597931415. Its abstract explicitly says convergence in capacity, describes the zero-capacity singularity-set condition and near-diagonal degrees, and identifies the extremal domain. One should not quote a generic internet description saying “Padé converges to the maximal analytic continuation” as a compact-uniform theorem.

An additional usable condition: if such capacity convergence is known in a domain D and all sufficiently late rational approximants have no poles in an open subdomain U, then Gonchar's lemma gives locally uniform convergence in U (for the holomorphic limit). In particular take an open neighborhood U of [0,R]. Pole avoidance only on the real interval is not the same as absence of poles in a complex neighborhood.

Verified source: Beckermann–Matos, arXiv:1310.2438, abstract and p. 2, https://arxiv.org/pdf/1310.2438. They state capacity plus absence of poles implies locally uniform convergence and cite Gonchar's 1975 lemma. They also exhibit an SVD-robust Padé approximant with spurious poles, so numerical robustness alone is not this hypothesis. Cacoq et al. pp. 4–5 give the related theorem with one-dimensional Hausdorff content, explicitly distinguishing it from the logarithmic-capacity terminology.

## Why general analyticity does not guarantee diagonal uniform convergence

The Baker–Gammel–Wills conjecture asserted that every function meromorphic in the unit disk and analytic at zero admits one subsequence of diagonal Padé approximants converging uniformly on all compact subsets of that disk away from the function's poles. Lubinsky disproved this with a Rogers–Ramanujan continued fraction.

Primary source: Doron Lubinsky, *Rogers-Ramanujan and the Baker-Gammel-Wills (Padé) conjecture*, Annals of Mathematics 157 (2003), 847–889, https://annals.math.princeton.edu/2003/157-3/p04, also https://arxiv.org/abs/math/0402305.

Buslaev provided a counterexample even to the holomorphic version and to the corresponding algebraic-function conjecture.

Primary source: V. I. Buslaev, *On the Baker–Gammel–Wills conjecture in the theory of Padé approximants*, Sbornik: Mathematics 193:6 (2002), 811–823, https://www.mathnet.ru/eng/sm658, DOI https://doi.org/10.1070/SM2002v193n06ABEH000658. The publisher abstract explicitly states both failures.

Quantifier caution: these counterexamples refute a universal diagonal subsequence working on all compact subsets of a two-dimensional disk. Do not silently turn that into the stronger claim that every function has a particular real [0,T] on which no selectable finite Padé entry can attain arbitrary accuracy. They suffice to refute the frequently invoked blanket compact-uniform diagonal theorem.

A separate striking full-sequence failure: Wallin constructed an entire function for which limsup_n |[n/n](z)|=infinity for every z≠0; its example also has a good locally uniformly convergent subsequence. Verified authoritative author survey: Lubinsky, *Spurious poles in Padé approximation*, Theorem 3.2, p. 10, https://lubinsky.math.gatech.edu/Research%20papers/SpuriousSavannahSurveyFeb262018.pdf. Original: H. Wallin, *The convergence of Padé approximants and the size of the power series coefficients*, Applicable Analysis 4 (1974), 235–251. Since the original was not read, prefer the Lubinsky/Buslaev primary citations above for the final answer and omit Wallin unless helpful.

## A transparent normal-family sufficient condition

There is an elementary condition independent of special Stieltjes structure. Let B be analytic on a connected complex open set U containing zero and [0,R]. Suppose the rational B_N are holomorphic on U, match the Taylor coefficients of B to orders tending to infinity, and are locally uniformly bounded:

\[
\text{for every compact }K\subset U,\qquad
\sup_N\sup_{z\in K}|B_N(z)|<\infty.
\]

Then B_N→B locally uniformly on U.

Proof: Montel's theorem makes every subsequence have a locally uniformly convergent subsubsequence. Cauchy's formula transfers derivatives at zero to its limit. Growing coefficient contact forces every derivative of that limit to equal B's derivatives. The identity theorem gives equality on connected U. Since every convergent subsubsequence has the same limit, the full sequence converges locally uniformly.

This condition can be obtained from verified numerator/denominator bounds, but boundedness is a substantive hypothesis, not a consequence of Padé matching. This argument applies just as well to a Borel transform B and explains exactly what pole and growth control must achieve.

## Application to Borel–Padé reconstruction

For \(F(t)\sim\sum a_jt^j\) and \(B(\xi)=\sum a_j\xi^j/\Gamma(1+\sigma j)\), Borel summation first needs an actual analytic continuation B and identification

\[
F(t)=\int_0^\infty e^{-u}B(tu^\sigma)\,du.
\]

Padé applied to B is an analytic-continuation procedure. Any above compact-uniform theorem can be applied to B, but the Laplace integral samples an unbounded ray. One also needs tail control, or must truncate the integral at a cutoff chosen using a tail bound for the actual B. Borel summability alone does not invoke de Montessus (no finite-pole meromorphy disk has been supplied), does not forbid Padé spurious poles, and does not turn Stahl capacity convergence into a sup estimate.

For a cutoff U, compact-uniform convergence on \([0,TU^\sigma]\) gives

\[
\sup_{0\le t\le T}\left|
\int_0^U e^{-u}[B_N(tu^\sigma)-B(tu^\sigma)]\,du
\right|
\le(1-e^{-U})
\sup_{0\le\xi\le TU^\sigma}|B_N(\xi)-B(\xi)|.
\]

Add a uniformly small tail \(\sup_{t\le T}\int_U^\infty e^{-u}|B(tu^\sigma)|du\). This gives an initialization-jet finite Borel–Padé approximation without needing a global growth bound for B_N. The resulting finite-cutoff integral is generally not a rational function of t; finite quadrature makes it a finite sum of scaled rational functions, which is rational in t and computable from finitely many jets. All orders/cutoffs/quadrature counts are selected for the prescribed epsilon and fixed T.

This is the appropriate logical connection for the PDE project: a verified Padé theorem for the actual Borel transform plus a Borel identity and tail bound closes the remaining approximation implication; none is provided merely by population GF existence.
