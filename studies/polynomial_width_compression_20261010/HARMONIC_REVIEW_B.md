# Independent audit B: harmonic rank obstruction and finite anti-concentration

2026-10-10. Independent isolated mathematical review. **PASS within the
stated scope.** Both elementary lemmas are correct, with their displayed
constants and probability bounds. The harmonic lemma rules out a qualifying
width polynomial in dimension for the current uniform-source,
canonical-tolerance, exact-metric construction with its stated literal
storage inventory. It does not rule out a different output approximation.
The scalar lemma is a valid conditional anti-concentration tool, not a
completed dense-variability or trajectory theorem.

No substantive flaw was found. One application clarification is useful:
the final-layer row products must be centered conditionally before applying
the mean-zero scalar lemma; their conditional mean is absorbed into the
allowed shift. This operation is justified below and does not change the
lemma or its constants.

## Inputs and independence

I read both candidate notes completely; the complete `paper/compact.tex`
and `paper/compact_selected.tex`; the assigned source interface, lines
1–75 of `paper/compact_foundations.tex`; and `docs/notation.qmd`.
I applied the rigorous-math and canonical-notation skills, including the
neural-network conventions. I did not read a study README, another review,
study history, or any route file linked from the candidates. In particular,
the historical cross-reference to `WIDTH_GATE_REFINEMENT.md` was not opened
and is not needed for this verdict. No experiment or external theorem was
needed for the two elementary arguments.

The following SHA-256 digests were identical before and after the proof
audit. For the foundations file the digest identifies the complete file,
but only its assigned interface was read.

| Input | SHA-256 |
|---|---|
| `HARMONIC_ROUTE.md` | `d19953be9d8182b493bd5677df5f375fb9f005d3a303ecdf769ca6151a56df8d` |
| `FINITE_ANTI_CONCENTRATION.md` | `1334458610524b644c6ee20186add3ee1dfe275b6c04f0850321e17841486cb7` |
| `paper/compact.tex` | `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` |
| `paper/compact_selected.tex` | `3add2b694f38a4d7dbce90e51dafd375a7e8dee2e06d26b2d5af451bddb44885` |
| `paper/compact_foundations.tex` | `6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |

## 1. Admissible network and current construction

The paper explicitly uses zero initial readout, independent standard
Gaussian first-layer entries, hidden entries of variance \(1/n\), normalized
query \(v=x/\sqrt d\), prediction \(f_n=w^\top h^{(L)}/n\), and loss
\(m^{-1}\sum_a(f_{n,a}-y_a)^2\). Its \(w\) is the readout called
\(W^{(L+1)}\) in the notation contract; the zero-readout initialization is
the paper's expressly stated convention.

For \(\phi(z)=z+\cos z\), the activation is entire, real on the real
axis, and unbounded there. Since

\[
 |\sin(x+iy)|\le\cosh y,\qquad
 |\cos(x+iy)|\le\cosh y,
\]

its first derivative is bounded on the strip of width one and its first
two derivatives obey the half-strip envelope. The paper's maximum defining
\(\beta\) is exactly \(16\). Thus unbounded activation values do not
violate any stated hypothesis.

For two centered jointly Gaussian coordinates of common variance \(q\)
and covariance \(c\), simultaneous sign reversal makes the mixed
linear–cosine expectations zero. The identities

\[
 \cos Z_1\cos Z_2
 =\tfrac12\{\cos(Z_1+Z_2)+\cos(Z_1-Z_2)\},\qquad
 \mathbb E\cos(Z_1\pm Z_2)=e^{-(q\pm c)}
\]

give exactly the candidate's recursion. Starting from \((1,1/2)\),
the off-diagonal covariance remains nonnegative, and the gap stays
positive because each gap increment is

\[
 e^{-q}(\cosh q-\cosh c)\in(0,1/2).
\]

After two layers, \(1/2<\gamma=q_2-c_2<3/2\), independent of \(d\).
The proposed two inputs have unit norm and inner product \(1/2\).
The two positive labels have RMS \(Y=(\gamma/4)16^{-60}\), half the
allowed small-label upper bound for \(m=L=2\). Hence all parameters
except \(d,n\) are fixed and every training assumption is met.

The relevant transfer interface really does require a single linear
neuron space \(E_1\subset\mathbb R^n\) approximating the first forward
source uniformly over the promised sphere and time interval. Time zero
therefore requires approximation of

\[
 F_A(v)=Av+\cos(Av),\qquad A=W^{(1)}(0),\quad v\in S^{d-1}.
\]

The canonical tolerance in `cp:selected-tolerance` is at most \(1/n\):
its last denominator contains \(2Cmn\), all its remaining factors are
at least one, \(C\ge1\), and \(\gamma/m\le1\). The requirement that
\(E_1\) additionally contain constants, initial training features and
first-weight columns only restricts the class of spaces further.

## 2. Independent reconstruction of the finite source-rank bound

Fix even \(k\ge2\), \(d\ge k\), and let

\[
 c_k=\frac{e^{-4}4^{-k}}{2k!},\qquad u_{ij}=A_{ij}/\sqrt d.
\]

Restrict queries to \(v=s/\sqrt d\), with independent uniform signs
\(s_j\in\{-1,1\}\). The degree-\(k\) Walsh coefficient of row \(i\)
of \(F_A\) is

\[
 b_{i,S}=(-1)^{k/2}\prod_{j\in S}\sin u_{ij}
                         \prod_{j\notin S}\cos u_{ij},
 \qquad |S|=k.
\]

This follows by multiplying the elementary exponential factors. The
linear part has degree one, so contributes nothing for the chosen \(k\).
Let \(B=(b_{i,S})\) and \(G=BB^\top\).

On the candidate's row-norm and maximum-entry event, the dimension
condition gives \(|u_{ij}|\le1/2\). Integration of
\(\tan t\le2t\) gives \(\cos^2 u\ge e^{-2u^2}\), while integrating
\(\cos t\ge\cos(1/2)>1/\sqrt2\) gives
\(\sin^2u\ge u^2/2\). Hence, with \(x_j=\sin^2u_{ij}\),

\[
 \prod_j\cos^2u_{ij}\ge e^{-4},\qquad
 s_x:=\sum_jx_j\ge1/4,\qquad
 \max_jx_j\le8\log(nd)/d.
\]

The total weight of ordered \(k\)-tuples with at least one repeated
index is at most
\(\binom{k}{2}\sum_jx_j^2s_x^{k-2}\). Subtracting this union bound
from \(s_x^k\) proves

\[
 k!\sum_{|S|=k}\prod_{j\in S}x_j
 \ge s_x^k\left(1-\binom{k}{2}\frac{\max_jx_j}{s_x}\right)
 \ge\tfrac12 4^{-k}.
\]

In each squared Walsh coefficient, the product of cosine squares over
the complement of \(S\) is at least the product over all coordinates.
Thus \(G_{ii}\ge c_k\). The two chi-square exponential estimates at
\(t=1/4\) and \(t=-1/2\) respectively have decay exponents exceeding
\(1/16\); the scalar Gaussian bound gives entrywise failure
\(2nd\exp[-4\log(nd)]=2(nd)^{-3}\). The asserted total failure for
these diagonal conditions, \(2ne^{-d/16}+2(nd)^{-3}\), is valid.

For one row, a coordinate in \(S\mathbin\triangle T\) gives an odd
sine–cosine factor, so distinct Walsh coefficients are uncorrelated.
Writing

\[
 \theta_d=\mathbb E\sin^2(Z/\sqrt d)
          =\tfrac12(1-e^{-2/d})\le1/d,
\]

the second moment of each coefficient is
\(\theta_d^k(1-\theta_d)^{d-k}\). Independence of two Gaussian rows
then gives, for \(i\ne j\),

\[
 \mathbb E G_{ij}^2
 =\binom dk\theta_d^{2k}(1-\theta_d)^{2(d-k)}
 \le\frac1{k!d^k}.
\]

There are \(n(n-1)\) ordered off-diagonal entries. Applying Markov to
their squared Frobenius norm gives the candidate's failure term
\(4n(n-1)/(c_k^2k!d^k)\). On the intersection of the two events,

\[
 G\succeq(c_k/2)I_n.
\]

No conditional independence after training, selected-space independence,
or independence between these two events was used.

For any linear \(E\), let \(P\) be its ordinary Euclidean orthogonal
projection. Coordinate approximation with error \(\eta\) implies
\(\|(I-P)F_A(v)\|_2^2\le n\eta^2\), since Euclidean distance is
at most \(\sqrt n\) times coordinate distance. Finite Walsh Parseval,
with only degree \(k\) retained, yields

\[
 n\eta^2\ge\|(I-P)B\|_F^2
 =\operatorname{tr}((I-P)G)
 \ge\frac{c_k}{2}(n-\dim E).
\]

This is precisely the asserted dimension bound and is deterministic
once \(G\succeq(c_k/2)I_n\); it therefore holds simultaneously for
every space chosen using \(A\).

As a separate check of the full-rank implication, if \(E\ne\mathbb R^n\)
choose a unit vector \(w\in E^\perp\). The approximation gives
\(|w^\top F_A(v)|\le\|w\|_1\eta\le\sqrt n\eta\), whereas the
degree-\(k\) part has squared average \(w^\top Gw\ge c_k/2\).
Consequently \(n\eta^2\ge c_k/2\). This contradicts
\(\eta\le1/n\) and \(n>2/c_k\), independently confirming the
integer-rank conclusion.

## 3. Polynomial quantifiers and literal storage

Let \(a>1\) be any fixed real number and take
\(n=\lceil d^a\rceil\). Choosing an even integer \(k>2a\) is
legitimate: \(k\) is an auxiliary proof parameter and does not alter the
activation or training family. For this fixed \(k\), the dimension
condition and \(n>2/c_k\) hold eventually, and every failure term tends
to zero. In particular the off-diagonal failure is
\(O_{a,k}(d^{2a-k})\). Small \(c_k\) changes the finite onset, not the
asymptotic assertion. This argument covers arbitrary finite \(a\).

When \(E_1=\mathbb R^n\), the required exact metric identity

\[
 u_I^\top Mv_I=u^\top v/n\qquad(u,v\in E_1)
\]

forces \(I=\{1,\ldots,n\}\): an omitted coordinate \(j\) is ruled
out by \(u=v=e_j\). The paper explicitly represents and retains both
initial and moving copies of \(W_C^{(1)}\in\mathbb R^{|I|\times d}\).
One copy alone therefore costs \(nd\) real coordinates. This is a
lower bound for that explicit inventory; no bit-complexity, oracle,
procedural representation, or information-theoretic claim is needed.

For fixed \(z=Ym/\gamma>0\) and any fixed finite activation/depth
constant \(C>0\), the logarithm of the second headline-storage term is

\[
 (d+1)(\log C-\log d)+4\log z
 +(3d+2)\log\log(e\lceil d^a\rceil)
 =-d\log d+3d\log\log d+O_{a,C,z}(d).
\]

It tends to \(-\infty\). Thus the headline is \(O_C(d^2)\), while
\(nd/d^2\ge d^{a-1}\to\infty\). With probability tending to one,
the current contract and the headline storage cannot both hold.

For any proposed threshold bounded by \(K(1+d)^b\) after the other
parameters and a fixed confidence are fixed, choose
\(a>\max\{b,1\}\). The above widths exceed that threshold for all
large \(d\), yet success probability tends to zero. This refutes every
fixed polynomial degree and every fixed coefficient \(K\), rather than
only low-degree thresholds. There is no contradiction with the paper's
pointwise eventual theorem, which explicitly fixes \(d\) and permits a
nonpolynomial onset.

The optional \(m=d\) construction is also valid. Starting the same
covariance recursion at \((1,0)\) gives \(1<\gamma<2\), and the
equicorrelation matrix has least eigenvalue \(q_2-c_2\). The proposed
labels satisfy the cap, keep \(Ym/\gamma\) fixed, and have
\(Y^{-1}=O(m)\). Therefore any fixed-degree joint polynomial in the
displayed parameters reduces to a polynomial in \(m\), to which the
same choice of \(a\) applies.

The conclusion remains tied to the current uniform source contract and
canonical tolerance. That tolerance is a sufficient design choice in the
transfer proof, not a proved necessary condition for every predictor
achieving output error \(Y/n\). The candidate explicitly makes this
distinction. It does not derive a lower bound for trained predictions,
all autonomous reductions, or a replacement comparison theorem.

## 4. Finite shift-uniform anti-concentration

Let \(X_i\) be iid, mean zero, with variance \(\sigma^2>0\) and
third absolute moment \(M_3<\infty\). An independent copy \(X'\)
has

\[
 \mathbb E(X-X')^2=2\sigma^2,
 \qquad \mathbb E|X-X'|^3\le8M_3.
\]

Taylor's remainder for cosine therefore gives

\[
 |\mathbb Ee^{itX}|^2
 \le1-\sigma^2t^2+\tfrac43M_3|t|^3
 \le1-\tfrac12\sigma^2t^2
 \le e^{-\sigma^2t^2/2}
\]

for \(|t|\le3\sigma^2/(8M_3)\). The square-root bound is valid;
for example \(M_3\ge\sigma^3\) implies \(|t|\sigma\le3/8\)
in this range. Independence gives, for

\[
 Z=\frac{\sum_iX_i}{\sigma\sqrt n},\qquad
 R=\frac{3\sigma^3\sqrt n}{8M_3},
\]

the bound \(|\mathbb Ee^{iuZ}|\le e^{-u^2/4}\) for \(|u|\le R\).

The Gaussian majorant of the interval indicator, followed by its Fourier
identity and the triangle inequality, is uniform in the shift \(b\):

\[
 \Pr(|Z-b|\le a)
 \le\frac{\sqrt e\,a}{\sqrt{2\pi}}
   \int_{\mathbb R}e^{-a^2u^2/2}|\mathbb Ee^{iuZ}|\,du.
\]

On \([-R,R]\), enlarging the integral of \(e^{-u^2/4}\) to the
line gives \(\sqrt{2e}\,a\). On the complement, the characteristic
function has modulus at most one, so the contribution is at most
\(\sqrt e\Pr(|G|>aR)\le2\sqrt e\,e^{-a^2R^2/2}\), with \(G\)
standard Gaussian. All integrals are absolutely dominated by Gaussian
kernels, which justifies interchange with expectation. No density or
nonlattice property of \(X_i\) is assumed.

Putting \(a=\delta/10\), the proposed width condition gives

\[
 \frac{a^2R^2}{2}
 =\frac{9\delta^2\sigma^6n}{12800M_3^2}
 \ge\frac{18000}{12800}\log(16/\delta)
 \ge\log(16/\delta).
\]

The resulting bound is

\[
 \Pr(|Z-b|\le\delta/10)
 \le\left(\frac{\sqrt{2e}}{10}+\frac{\sqrt e}{8}\right)\delta
 <\delta.
\]

Thus \(2000\) is a valid, nonoptimal numerical constant. Applying the
same inequalities conditionally proves the conditional statement whenever
conditional centering, independence, variance, third moment, and the
displayed width inequality hold almost surely. If these moment and width
conditions hold only on a conditioning-measurable good event, the conditional
conclusion holds on that event and its failure probability must be added
in any unconditional application. The shift must be measurable with
respect to the conditioning information, not chosen using the remaining
unconditioned summands.

## 5. Exact connection to initial prediction velocity

At \(w(0)=0\), the hidden weight velocities vanish and
\(\dot w(0)=2\sum_b y_bh_b^{(L)}(0)/m\). Differentiating
\(f_{n,a}=w^\top h_a^{(L)}/n\) therefore gives exactly

\[
 \dot f_n(0,x_a)=\frac2{mn}\sum_i P_{i,a},\qquad
 P_{i,a}:=h_i^{(L)}(0,x_a)\sum_b y_bh_i^{(L)}(0,x_b).
\]

Given the lower initialized layers, these row products are conditionally
iid because the final hidden matrix rows are independent Gaussian rows.
Conditioning also on an independent reference network preserves this
fact. A sample index measurable from the conditioning information is
permitted.

To make the intended application explicit, let \(\mathcal F\) contain
that information, and define

\[
 \mu_a=\mathbb E[P_{i,a}\mid\mathcal F],\qquad
 X_i=P_{i,a}-\mu_a,\qquad
 \sigma_a^2=\mathbb E[X_i^2\mid\mathcal F],\qquad
 M_{3,a}=\mathbb E[|X_i|^3\mid\mathcal F].
\]

When \(\sigma_a>0\), put
\(Z_a=\sum_iX_i/(\sigma_a\sqrt n)\). For any
\(\mathcal F\)-measurable reference velocity \(D_a\),

\[
 \dot f_n(0,x_a)-D_a
 =\frac{2\sigma_a}{m\sqrt n}(Z_a-b_a),\qquad
 b_a=\frac{m\sqrt n}{2\sigma_a}
             \left(D_a-\frac{2\mu_a}{m}\right).
\]

The mean mismatch is consequently an allowed shift; it need not vanish.
The original row products are generally not mean zero, so stating this
centering step would improve the application paragraph. It is a clarification,
not an obstruction.

As the candidate correctly states, a polynomial-width good event for
positive conditional variance and a controlled third moment remains to
be proved. A derivative difference alone also does not give a quantitative
difference of actual trajectories without remainder or time-regularity
control. Neither missing component is supplied by this scalar lemma, and
neither is claimed in the candidate.

Both results are internally valid in their delimited roles. This review
does not certify the unprovided source-event proof, the remaining dense
variability argument, or a universal impossibility theorem for prediction
compression. Only this assigned report was written; the frozen scientific
inputs were not edited.
