# Complete reconstruction of the quantitative dataset synthesis

2026-10-04. **PASS for the complete current synthesis as an implication
from its named internally checked source and real-fitting inputs.**
No mathematical correction is required in the checked version. This is a
collaborative internal reconstruction, not an isolated promotion review
and not a claim that the source theorems have been promoted.

The complete synthesis was checked at SHA-256
`304363d4587c94ee997bc2fb573446d30a6cd878fce547f1a78e6390ca4f4170`.
Its final version uses the stronger sufficient label condition
\(Y\le c\lambda/\sqrt m\). The previous version, checked first at
`f20eaa36ce61e4c0890896e5e9b54e9f93ccbd6435347cb3ed95d5d9d473835e`,
used the valid but more conservative condition
\(Y\le c\lambda^{3/2}\).

Other complete inputs read for this reconstruction were:

- `GENERAL_WEIGHTED_COMPARISON.md`, SHA-256
  `1dcb779135b616aa66be4cd830d2bd2f3217a56eeae8f3cdf7394a52262a4306`;
- the author's frozen `DATASET_SOURCE_CONSTANTS.md`, initially SHA-256
  `a51ee9bd550abcbcc4561d9236c1ef83d5bf389c12e66181ebb529c707d63d8e`,
  with the subsequently authorized energy refinement appended at
  `340fae2324747c34225cc3ee4993452549f9296fd3ac7271e35061ae2fcf7ac6`;
- the separately authorized `DATASET_LABEL_DEPENDENCE.md`, SHA-256
  `b5d44373013c67b25a44d7907eef69b4458049eaca11f846b6c64df56b7400d3`.

The complete deep source/activation and authorized cavity proofs were
already read during the frozen source audit. Their scope and provenance
are recorded there. No new prior-study source was accessed. The separate
geometry note was not read: the elementary two-input calculation needed
to check Section 7 is reconstructed below. The supervisor independently
coordinated a further check of the real energy input; the present verdict
identifies that result as a dependency rather than claiming independent
promotion validation of the whole research chain.

## 1. Normalization and the sharper sufficient label condition

The network, independent Gaussian initialization, zero readout, averaged
squared loss, and mobilities agree with the original compression theorem.
The synthesis defines

\[
 \lambda=\min\{1,\lambda_{\min}(Q^{(L)}/m)\},\qquad
 Y^2=m^{-1}\sum_a y_a^2,
\]

where \(Q^{(L)}\) is the initialized limiting feature second-moment
matrix. This is the correct normalization for residual evolution
\(\dot c=-2(K/m)c\). It is distinct from both the unnormalized
gap and \(\ell_n=\log(en)\). Bounded final activations give
\(m\lambda\le B_\phi^2\), including when the cap is active.

The real energy identity is

\[
 -\frac d{dt}\|c(t)\|_m^2
 =\frac{\|\dot A\|_F^2}{n}
  +\sum_{\ell=2}^L\|\dot W^{(\ell)}\|_F^2
  +\frac{\|\dot w\|_2^2}{n}.
 \tag{1}
\]

On a stopped real Gram tube, the residual gap of order \(\lambda\)
and (1) bound total mobility path length by \(CY/\sqrt\lambda\).
Zero readout then gives the same bound for its RMS norm. Combining the
hidden speed bound \(C\rho\|w\|_n\) with residual activity gives
hidden displacement at most \(CY^2/\lambda^{3/2}\). The normalized
feature matrix consequently moves by at most that amount. Since its
initial smallest singular value is of order \(\sqrt\lambda\),
\(Y\le c\lambda\) closes the Gram tube; the explicit constants
and simultaneous hidden-operator margin in the real energy note check.
Weighted blocks satisfy the same identity. Rectangular cavities retain
the normalization \(n\), and total neuron mass at most one suffices
for every upper bound. Fixed initial-gap losses are absorbed by the
single structural label constant.

The source proof only needs the resulting real physical tube and
residual decay \(\rho\le Ye^{-c\lambda t}\), with activity
allowance \(S=C_0Y/\lambda\). Its coarser coordinate readout and
response bounds \(CS\) remain valid by integration. The source
proof's additional scalar requirements are fixed small \(S\),
\(S^2B\le c\), and \(S^2\log(e+B)\le c\).
The per-sample Gaussian reference has a structural exponential moment;
the maximum over samples costs at most \(m\). Thus \(B=Cm\)
works, and \(S^2m\le c\) suffices for the budget requirements.

The condition \(S^2\le c\lambda\) in the frozen initial audit
was only the older real Gram bootstrap. Reinspection of the real and
complex insertion propagator, endpoint trace series, Gaussian modulus,
short non-real propagation, angular/forward induction, and pole exclusion
finds no other use of that condition. Replacing just the real bootstrap
therefore gives the complete sufficient list

\[
                  Y\le c\lambda,\qquad S\le c,
                  \qquad S^2m\le c.
 \tag{2}
\]

Every inequality in (2) follows from
\(Y\le c\lambda/\sqrt m\), after decreasing a structural
constant. This checks synthesis (4), (8), and (9), and verifies that the
new threshold applies to the full source theorem rather than to fitting
alone. The older \(c\lambda^{3/2}\) threshold remains a valid
subclass by \(m\lambda\le B_\phi^2\). No necessity or optimality
claim is warranted or made.

## 2. Pairing defects and all comparison constants

Under (2), the original and weighted models have structural operator
bounds. Their feature RMS norms are bounded and their response RMS norms
are at most \(CS\). For a source approximated coordinatewise to
\(\epsilon\), positive cubature transfers its empirical RMS to
selected RMS with an error at most \(2\epsilon\). The requirement
\(\epsilon\le Y\), together with \(Y\le CS\), therefore
retains the response bound \(CS\) after selection.

Pairing defects cost \(C\epsilon\); their time integrals are
against total residual activity at most \(S\). Initial projected
operators are contractive in the weighted norms. The learned retained
reference operators differ from them by at most \(CS^2\). These
facts verify that the constants in the forward/backward subtraction
are structural, independently of selected masses and the sample count.

Let \(d(t)\) be the sum of parameter-block distances from the
compressed state to the retained reference, in the weighted norms of
the comparison note. Let
\(M=\max\{1,\max_{a,\ell,i,t\le T}|k_{a,i}^{(\ell)}(t)|\}\).
Forward subtraction gives feature error \(C(d+\epsilon)\).
Multiplying each changed gate by the true reference carrier, then
descending through the bounded layer operators, gives response error
\(C(1+M)(d+\epsilon)\). The factor \(M\) is additive through
this recursion, rather than raised to a power of depth.

Every tangent-Gram entry is a sum of a feature pairing, response/feature
pairing products, and a first-layer response pairing times
\(v_a^\top v_b\). Therefore

\[
 \max_{a,b}|(K_C-K_n)_{ab}|
 \le C(1+M)(d+\epsilon).
 \tag{3}
\]

The normalization in the synthesis is essential:
\(\|E/m\|_{\rm op}\le\|E/m\|_F\le\max_{a,b}|E_{ab}|\).
Thus (3) controls the **normalized** tangent-Gram difference with no
additional factor \(m\).

## 3. Reconstruction of synthesis equations (10)--(15)

Set \(u=c_C-c_n\), \(\Gamma=K/m\), and
\(\rho_n=\|c_n\|_m\). The exact difference equation is

\[
 \dot u=-2\Gamma_Cu-2(\Gamma_C-\Gamma_n)c_n.
 \tag{4}
\]

The compressed normalized feature Gram retains a gap of order
\(\lambda\), and its tangent Gram dominates it. Taking the sample
RMS norm in (4), using (3), and regularizing at a zero norm proves
synthesis (10). Integration, with \(u(0)=0\), gives

\[
 \int_0^t\|u(s)\|_m\,ds
 \le\frac{C(1+M)}\lambda
         \int_0^t\rho_n(s)(d(s)+\epsilon)\,ds.
 \tag{5}
\]

This verifies (11), including its single inverse-gap factor.

Subtracting the actual rank-one velocities accounts separately for the
residual difference, response difference, and feature difference. The
coefficient of \(\|u\|_m\) is structural: the readout block has
bounded feature norm and hidden blocks have bounded response/feature
products. The other terms are bounded by
\(C(1+M)\rho_n(d+\epsilon)\). This proves (12).
After inserting (5), \(\lambda\le1\) gives

\[
 d(t)\le\frac{C(1+M)}\lambda
          \int_0^t\rho_n(s)(d(s)+\epsilon)\,ds.
\]

Apply the integral Gronwall inequality to \(d+\epsilon\), whose
initial value is exactly \(\epsilon\). The result is

\[
 d(t)+\epsilon
 \le\epsilon\exp\left\{
      \frac{C(1+M)}\lambda\int_0^t\rho_n(s)\,ds\right\}.
 \tag{6}
\]

There is no missing multiplicative \(1+M\) outside this exponential.
The looser prefactor in the original comparison note was unnecessary
for this direct argument with \(d+\epsilon\). Equation (6)
proves synthesis (13).

The real all-time carrier estimate retains its amplitude:
\(\max|k|\le CS\sqrt{\ell_n}\). Its proof uses a Gaussian
tail for the reference divided by \(S\); the union over samples
and neurons is absorbed by the width threshold. The singleton shift
is \(CS(1+S^2B)\le CS\), and its all-time tail is also
\(o(S)\). Consequently

\[
 \frac{C(1+M)S}\lambda
 \le\frac{CY}{\lambda^2}
        +\frac{CY^2}{\lambda^3}\sqrt{\ell_n}.
 \tag{7}
\]

This checks every power in synthesis (14). The observation error is
bounded by \(C(d+\epsilon)\): subtract the readouts, subtract
the features using the bounded reference readout RMS, and add the
selected/original pairing defect. No additional carrier factor is needed.
Taking \(\epsilon=n^{-1}\) in (6)--(7) proves (15).

Write \(A=CY^2/\lambda^3\) for this paragraph only. If
\(\ell_n\ge\max\{2,16A^2\}\), then
\(A\sqrt{\ell_n}\le\ell_n/4\le(\ell_n-1)/2\), so
\(e^{A\sqrt{\ell_n}}\le\sqrt n\). This proves the asserted
sufficient restriction
\(\ell_n\ge C(1+Y^4/\lambda^6)\). Under the larger label
threshold \(c\lambda/\sqrt m\), this restriction is
dataset-dependent; under the smaller \(c\lambda^{3/2}\)
threshold its coefficient is structural. The synthesis states that
distinction correctly.

Both independently fitting models have sphere query tails bounded by
\(CS e^{-c\lambda T}\). For
\(T=C_T\lambda^{-1}\ell_n\), sufficiently large structural
\(C_T\) makes these tails at most \(Cn^{-1}\). Combining with
(15) proves the first inequality of synthesis (6), for all times and
the fitted endpoints. The second inequality follows from
\(Y/\lambda^2\le c/(\lambda\sqrt m)\). The old
\(\exp(C/\sqrt\lambda)\) simplification is correctly retained
only for the smaller-label subclass.

## 4. Source approximation, total storage, and the width threshold

With (2), the source proof has structural complex radius
\(c\ell_n^{-(L+4)}\) and coordinate magnitude
\(C\ell_n^{L+2}\). Its horizon contributes the explicit
\(\lambda^{-1}\) factor to the algebraic time degree. The
Bernstein/Fourier tail bounds at tolerance \(n^{-1}\), with fixed
logarithmic prefactors absorbed into \(n_0\), give

\[
 p\le C\lambda^{-1}\ell_n^{L+6},\qquad
 J\le C\ell_n^{L+5}.
\]

A query family therefore contributes at most
\(C\lambda^{-1}\ell_n^{d(L+5)+1}\) real coefficient vectors.
There are a structural number of such families per layer and \(O(m)\)
training-only backward families, each contributing \(O(p)\).
The initialized training vectors add \(O(m)\) and the first-weight
columns add \(d\). This reconstructs synthesis (17).

Positive cubature on constants and pairwise products selects
\(O(R^2)\) neurons per layer. All adjacent learned dense matrices
therefore cost \(O(R^4)\); first weights cost \(O(dR^2)\).
Masses and readouts are lower-order contributions. With
\(a=d(L+5)+1\ge L+6\), \(\lambda\le1\), and \(d\)
part of the structural parameters, this is bounded by
\(C(1+m)^4\lambda^{-4}\ell_n^{4a}\), plus \(Cm(d+1)\)
for the retained data and labels. Thus (7) counts the full state and
fixed storage, and still gives a smaller representation for sufficiently
large width at fixed parameters. The exact-real preprocessing cost is
excluded explicitly, consistent with the original representation contract.

The covariance-map Lipschitz constant
\(A_\phi=B_\phi D_2+D_1^2\) is correct, including for diagonal
entries. Gaussian covariance interpolation can be regularized at
singular covariances; no intermediate eigenvalue denominator enters.
Conditional concentration and the depth recurrence give
\(A_LB_\phi^2\sqrt{2\log(2Lm^2/\eta)/n}\) for the entrywise
error. Dividing the operator norm by \(m\) removes the entry-count
factor. Thus synthesis (18), with coefficient 32, indeed suffices for
normalized initialized Gram error at most \(\lambda/4\).

The synthesis correctly distinguishes this quantitative initialization
ingredient from the full width threshold. The latter must also absorb
fixed moment degree, cavity transfer and insertion constants, sample and
query nets, \(\log(\lambda^{-1})\), the comparison amplification
restriction, and \(n^{-1}\le Y\). The term
\(e^{o(1)/S}\) prevents silently asserting a common inherited
threshold for all arbitrarily small positive labels. Its stated
\(n_0(d,L,b,B_\phi,m,\lambda,Y,\eta)\) accommodates these
dependencies. Uniform prefactors over datasets do not imply one event
simultaneous over datasets, one event over widths, or a theorem for
growing \(m\) or vanishing \(\lambda\); all these distinctions
are preserved.

## 6. Independent calculation of the stated two-input example

For tanh and two unit inputs with angle \(\theta\), set
\(q_0=1\), \(c_0=\cos\theta\), and define recursively

\[
 q_\ell=\mathbb E\tanh^2(\sqrt{q_{\ell-1}}G),\qquad
 c_\ell=\mathbb E[\tanh(U)\tanh(V)],
\]

where \(G\sim N(0,1)\), and \((U,V)\) have variances
\(q_{\ell-1}\) and covariance \(c_{\ell-1}\). Every
\(q_\ell>0\). Covariance differentiation gives derivative
\(\mathbb E[\operatorname{sech}^2(U)
\operatorname{sech}^2(V)]\), whose limit as the covariance
increases to the common variance is

\[
 a_\ell=\mathbb E\operatorname{sech}^4(
                          \sqrt{q_{\ell-1}}G)>0.
\]

Bounded derivatives justify this limit even at the singular endpoint.
Hence
\(q_\ell-c_\ell=a_\ell(q_{\ell-1}-c_{\ell-1})
+o(q_{\ell-1}-c_{\ell-1})\). Since
\(1-\cos\theta=\theta^2/2+o(\theta^2)\),

\[
 \lambda_-=(q_L-c_L)/2
 =\frac{\theta^2}{4}\prod_{\ell=1}^L a_\ell
      +o(\theta^2),\qquad
 \lambda_+=(q_L+c_L)/2\longrightarrow q_L>0.
\]

This checks synthesis (19), including positivity of the asymptotic
constant. In the fixed initialized-feature geometry with Gram
\(Q^{(L)}\), the minimum squared readout norm is
\(y^\top Q^{(L)-1}y\). The vectors
\((\alpha,-\alpha)\) and \((\alpha,\alpha)\) have squared
Euclidean norm \(2\alpha^2\) and are eigenvectors of
\(Q^{(L)}\) with eigenvalues \(2\lambda_-\) and
\(2\lambda_+\), respectively. Their minimum squared readout
norms are therefore exactly \(\alpha^2/\lambda_-\) and
\(\alpha^2/\lambda_+\), as stated. This calculation concerns
the limiting fixed feature geometry, and does not identify trained
features with their initialization.

For \(m=2\), the sufficient threshold
\(Y\le c\lambda/\sqrt m\) is of order \(\lambda\), hence
of order \(\theta^2\). The synthesis correctly avoids turning
that sufficient threshold into a necessary obstruction or a theorem
adapted to the label direction.

## 7. Final verdict and provenance of the refinement

All seven sections of the final synthesis were read and reconstructed.
The main error bound, label threshold, retained-coordinate count,
initialization estimate, asymptotic qualifications, and geometry example
are mutually consistent. No correction remains for the checked hash.

During this check the supervisor suggested combining the new real energy
theorem with the already frozen source audit. The present reconstruction
verified that no non-real source step needs \(S^2\le c\lambda\),
and reported the exact larger-label amplification threshold. The
supervisor incorporated the resulting stronger theorem into the synthesis;
the complete revised text was then reread. This exchange is why the
report is collaborative internal validation. The complete source
theorems and the separate deterministic real energy theorem remain
identified research dependencies. No experiments, manuscript changes,
Git mutations, or promotion were performed.
