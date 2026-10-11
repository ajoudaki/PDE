# Independent audit of Gaussian-oracle endpoint assembly

2026-10-11. Internal proof audit, not promotion.

**Verdict: PASS for the assembly and its stated interfaces.** The adaptive
two-sided Gaussian conditioning, measurable transcript event, depth recursion,
readout moment extraction, and transfer to two actual fitted endpoints have no
unresolved gap in the frozen inputs. This verdict takes the precise numerical
approximation and projected-Gaussian lemma conclusions as separate modules;
it does not replace their independent audits or certify the entire source
cavity proof afresh. No counterexample to the stated endpoint conclusion was
found. The qualifications in the assembly statement are necessary to retain.

## Scope and frozen inputs

This audit used only the neutral assignment, the required rigorous-math and
canonical-notation skills (including the neural-network reference), and the
eight inputs listed below. The four endpoint modules, the moment note, and
the three paper sources were read completely. The moment note was used only
to check the exact training-readout fourth-moment extraction. No study
history, README, other research note, or previous or parallel review report
was consulted. Author notices identifying pending statement clarifications
and final assembly edits were received; their contents did not substitute
for reconstruction of the revised statements. No input was edited.

SHA-256 hashes of the audited bytes:

| Input | SHA-256 |
|---|---|
| `GAUSSIAN_ORACLE_ENDPOINT.md` | `1a7e0c84881b1c0a043215b40b588b21a01532260885bedc9ac4ea182a29405b` |
| `GELU_SILU_FLOW_ROUTE.md` | `f3b33474289c38cc38bfbb9eeb90d5aed7652b7a025f4c3171f11e5140908c1c` |
| `GELU_SILU_PROJECTED_SCALAR.md` | `eb6c0b39570216a6dda3d9ba7ad96fd12493da20bfd393f87af2d12fc1b44a29` |
| `GELU_SILU_PROJECTED_INNOVATION.md` | `fac32d132b76e002ef9a956a426d1a182a2aa1bece4eb04c51a7095c135fdb2b` |
| `NONODD_MOMENT_ROUTE.md` | `882de8bf0e33e7d7c6a62cb1afd29d633531ccc7a6b4cdb1942cccef98c4fa93` |
| `paper/compact.tex` | `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `paper/compact_foundations.tex` | `6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0` |

The first five paths are relative to this study. The last three are relative
to the repository root.

The notified clarification pass was reread: it makes the initialized-base
representation and restricted first-layer operator explicit, states
\(B\ge0\) and deterministic rank envelopes in the scalar module, and
fixes the constants in the unused positive-probability alternative uniformly
in width. These changes preserve every assembly interface checked below.

## 1. Exact joint adaptive conditioning

Let the initial sigma field contain the fixed data and the first-layer
initialized values on the training span, but none of the initialized hidden
matrix entries. The hidden matrices are independent with entry variance
\(1/n\). At each finite algorithm step, the matrix index, orientation, and
query vector are measurable with respect to this field and earlier answers.
This access condition is essential and is satisfied by the algorithm in
Section 6 of `GELU_SILU_FLOW_ROUTE.md`.

For one matrix \(G\), let \(V\) and \(U\) be the forward and transpose
query spans after any step. In Frobenius Euclidean matrix space the
observation nullspace is
\[
 \mathcal N=\{A:AP_V=0,\ P_UA=0\}
           =\{(I-P_U)A(I-P_V):A\in\mathbb R^{n\times n}\}.
\]
The orthogonal projection onto this nullspace is
\(A\mapsto(I-P_U)A(I-P_V)\). Its complementary projection applied to
\(G\) is exactly
\[
 M=GP_V+P_UG(I-P_V).
\]
It is known from the transcript, including for dependent query lists. For
example, if \(V_*\) and \(U_*\) are the matrices of query columns,
with answers \(F_*=GV_*\) and \(B_*=G^\top U_*\), then
\[
 GP_V=F_*V_*^\dagger,\qquad
 P_UG=(U_*^\dagger)^\top B_*^\top.
\]
Thus the displayed conditional mean is not shorthand for an unobserved
entrywise computation.

For adaptivity, condition on the previous transcript. The next vector is
then fixed. The new answer is a linear observation of a conditionally
Gaussian residual supported on the previous nullspace. Gaussian orthogonal
projection gives the updated nullspace obtained by adding precisely this
new forward or transpose vector. The updated mean is the unique matrix
matching all recorded answers and orthogonal to that nullspace. This proves
the formula by induction, even when the new observation is degenerate.

The same induction applies to the product of all hidden-matrix spaces.
Conditional on the past, only the selected matrix is observed. The other
residual blocks are independent of that observation and retain their laws.
Selecting the matrix using past answers introduces no additional information
after the past is fixed. Therefore the final residual blocks are jointly
independent conditional on the complete transcript. The formula involving
fresh matrices is a conditional-law representation, realizable on an
extension of the probability space; it need not identify new Gaussian
matrices as literal functions of the original matrices.

The algorithm has a deterministic query bound. Its Taylor arithmetic and
activation evaluations require no entry inspection, and its learned
increments are known outer-product sums. Initialization of a parameter state
can be read symbolically as initialized matrix plus stored increment; no
hidden full-matrix read is necessary. The first matrix is accessed only on
training directions. Consequently \(Z=W_0^{(1)}v\sim N(0,I_n)\) at the
fixed orthogonal query is independent of the transcript and all residual
blocks, and its value is unchanged by every auxiliary or actual update.

**Result:** the representation in assembly equations (2) and (5) is valid
jointly across layers. Conditioning additionally on full hidden norms,
actual trajectories, or integrator success would invalidate this reasoning;
the assembly does not do so.

## 2. Transcript bounds and the exact source moment used

The fitting lemma supplies an event of probability tending to one on which
the actual flow converges and interpolates, training features have RMS at
most \(2H\), hidden initialization operators are at most eight, and fitted
hidden operators are at most nine. At interpolation,
\[
 Y^2=\frac1m\sum_a
 \left|\frac{w_\infty^\top h_a^{(L)}(\infty)}n\right|^2
 \le4H^2\frac{\|w_\infty\|^2}n.
\]
The approximation error in the physical parameter norm therefore gives
\(\|\widehat w\|/\sqrt n\ge Y/(4H)>0\) eventually. The fitting upper
bound \(\|w_\infty\|/\sqrt n\le2Y/\sqrt\lambda\), where
\(\lambda=\gamma/m\), likewise transfers to a fixed upper bound.

The fourth moment requires the source proof's empirical exponential budget,
not just its public maximum. With \(S=16Y/\lambda>0\), its stopped budget
and budget-removal argument give, on an event of probability tending to one,
\[
 \frac1n\sum_i\exp\left(
 \frac{\eta_*}{S}\sup_{0\le t\le T}|w_i(t)|\right)
 \le\mathcal B,
 \qquad T=32\log(en)/\lambda.
\]
This follows by retaining only the top-layer carrier terms
\(k_a^{(L)}=w\) in `cp:src-budget`. The source's
`cp:src-budget-removal` sends the width to infinity at each fixed moment
order before taking the infimum over orders; its constants do not acquire a
new confidence-dependent label restriction.

The fitting tail gives
\[
 \sup_{t\ge T}\frac{|w_i(t)-w_i(T)|}{S}
 \le\frac{\sqrt{n\lambda}}8e^{-16\log(en)}\le\frac18.
\]
Thus the all-time exponential mean is at most \(2\mathcal B\). Applying
\(x^4\le(4/e)^4e^x\) for \(x\ge0\) gives exactly the sufficient bound
\[
 \frac1n\sum_i\sup_{t\in[0,\infty]}|w_i(t)|^4
 \le 2\mathcal B\left(\frac{64}{e\eta_*}\right)^4
       (Y/\lambda)^4.
\]
Every constant is fixed for the problem. An energy-normalized fourth moment
uniform over all datasets is neither supplied nor needed.

For the approximant,
\[
 \|\widehat w-w_\infty\|_{4,n}
 \le n^{1/4}\|\widehat w-w_\infty\|_{2,n}=O(n^{-63/4}),
 \qquad \|a\|_{p,n}=(n^{-1}\sum_i|a_i|^p)^{1/p}.
\]
The fourth moment therefore transfers with a vanishing error. For each
known matrix part,
\[
 \|M_j\|\le2\|W_0^{(j)}\|\le16,
 \qquad
 \|\widehat W^{(j)}-W_0^{(j)}\|\le17+o(1),
\]
so \(\|A_j\|<40\) eventually. All displayed bounds on
\(\widehat w,A_j\) themselves define a transcript-measurable event
\(E_n\). The original fitting, source, and approximation events imply
\(E_n\) and thereby prove \(\Pr(E_n^c)=o(1)\); they are not appended
to the conditional sigma field. This distinction is implemented correctly.

## 3. Recursive law and final scalar interfaces

For a transcript in \(E_n\), expose only \(Z\) and the residual matrices
below layer \(j\). The preceding query feature is then fixed, and the
remaining matrix at layer \(j\) is fresh. Its action has conditional law
\[
 \widehat z^{(j)}=A_j\widehat h^{(j-1)}+
 \sigma_j(I-P_{U_j})g_j,
 \qquad
 \sigma_j=\frac{\|(I-P_{V_j})\widehat h^{(j-1)}\|}{\sqrt n}.
\]
The query-law normalization is correct: matrix entries have variance
\(1/n\), so no additional factor of \(\sqrt n\) is missing.

The innovation lemma uses its \(P=P_{U_j}\) and next removed subspace
\(Q=P_{V_{j+1}}\). Both ranks are bounded by a deterministic
\(O(\log(en)^{9/2})=o(n)\). Initially use \(P=0\), zero mean,
unit scale, and \(Q=P_{V_2}\). The lemma gives positive lower innovation
RMS and bounded feature RMS, uniformly over admissible transcripts.
With \(\|A_j\|\le40\), a valid upper recursion is
\(H_1=2\), \(H_j=42H_{j-1}\). Every resulting mean RMS and noise
interval is fixed and finite at fixed depth, with a positive lower endpoint.
Successive conditional failure probabilities sum to \(O(1/n)\).

At the final step one must restrict only to success through layer
\(L-1\). This is measurable in the lower exposed blocks. In particular,
one must not condition the final Gaussian on the layer-\(L\) norm event
which is optionally also proved by the innovation lemma. The assembly's
phrase “successful lower query layers” has exactly the valid meaning.

The final scalar lemma then applies with
\[
 P=I-P_{U_L},\quad b=A_L\widehat h^{(L-1)},\quad
 w=\widehat w,\quad E^2=a_0,\quad M_4=a_4,
 \quad F=\sqrt n\,\widehat f_n(\sqrt d\,v).
\]
Its projection convention is complementary to the innovation lemma's,
and the substitution above accounts for that. Its rank defect is
\(\operatorname{rank}P_{U_L}=o(n)\). No independence between
\(b,w,P\) is required after conditioning; only the final Gaussian must
remain fresh. The traceable fourth-moment bound supplies both scalar energy
delocalization and the \(O(n^{-1/4})\) Hessian estimate. These interfaces
are satisfied for all-GELU, all-SiLU, and any fixed layerwise mixture.

The innovation note's fourth-moment/Paley--Zygmund consequence alone would
give only positive probability. The assembly correctly uses the separate
scalar note's uniform normal approximation to obtain arbitrary fixed
confidence. No promotion of the weaker consequence is being made.

## 4. Uniform center and transfer to the actual second run

After averaging over good transcripts and successful lower layers, the
scalar lemma implies constants \(v_0>0\) and a deterministic sequence
\(\epsilon_n\to0\) such that, for every \(r>0\),
\[
 \sup_{a\in\mathbb R}
 \Pr\{|\widehat f_n(\sqrt d\,v)-a|\le r/\sqrt n\}
 \le\frac{2r}{\sqrt{2\pi v_0}}+\epsilon_n.
\]
Here \(\epsilon_n\) includes bad transcripts, lower-layer failures, and
the scalar approximation error. The conditional means need not converge or
agree between networks.

For precision on failure events, define an actual endpoint prediction to be
zero when its fitted limit does not exist. This measurable extension is used
only in the proof. Let \(X_n\) and \(X'_n\) be these extensions for two
independent ordinary runs, and let \(\widehat X_n\) be the first
approximant. The second extended prediction is independent of the entire
first run, so integration of the preceding uniform bound against its law
gives the same estimate for \(\widehat X_n-X'_n\).

By the numerical module and deterministic forward subtraction, there is an
event \(A_n\) of probability \(1-o(1)\) on which the first fitted limit
exists and \(|\widehat X_n-X_n|\le Cn^{-16}\). The Gaussian event
\(\|Z\|\le2\sqrt n\) may be included in \(A_n\) at an additional
\(o(1)\) cost; it is used for this probability bound, not for the earlier
fresh-Gaussian conditioning. Let \(F'_n\) be the second fitting event.
For each fixed \(c>0\), eventually
\[
 \begin{aligned}
 &\Pr\{\text{both fit and }|X_n-X'_n|\ge c/\sqrt n\}\\
 &\qquad\ge
 1-\Pr\{|\widehat X_n-X'_n|\le2c/\sqrt n\}
       -\Pr(A_n^c)-\Pr((F'_n)^c)\\
 &\qquad\ge1-\frac{4c}{\sqrt{2\pi v_0}}-o(1).
 \end{aligned}
\]
For example \(c=\delta\sqrt{2\pi v_0}/16\) makes the fixed term
\(\delta/4\); all remaining failures are eventually below
\(3\delta/4\). This proves exactly the requested individual-width,
fixed-confidence conclusion. Only the first run needs an approximant.

## 5. Boundary tests and issues

There is no blocking assembly issue. The following restrictions must stay
visible in any final theorem or compressed proof.

- Positive fixed \(Y\) gives a positive energy constant; zero labels with
  zero initialized readout yield the identically zero predictor.
- Proper training span and a query fixed in its orthogonal complement supply
  the untouched first-layer Gaussian. Full-span data and queries chosen
  using the initialization are not covered by this proof.
- All problem parameters and depth are fixed. Innovation and scalar
  constants can be extremely small; the proof supplies no polynomial width
  threshold, uniform growing-depth result, or uniform limit as \(Y\to0\).
- Final nonaffinity is substantive. For the scalar lemma with an affine
  activation, take \(w=\mathbf1\), \(b=0\), and
  \(P=I-\mathbf1\mathbf1^\top/n\). Then energy and empirical fourth
  moment both equal one and the rank defect is one, but the random scalar
  is identically zero. The Hermite-tail argument excludes this obstruction
  for raw GELU and SiLU.
- A bound \(\max_i|w_i|=O(\sqrt{\log n})\) alone does not certify the
  fixed \(M_4\) required by the scalar lemma. The source exponential
  budget is an actual dependency and should remain cited explicitly.
- The first-layer initialization symbol in the auxiliary parameter tuple
  represents a matrix accessible only on the training span. It must not be
  implemented by an unrestricted entry-inspecting algorithm.

## 6. Final assembly recheck

The finalized assembly was reread completely. Its hash is
`1a7e0c84881b1c0a043215b40b588b21a01532260885bedc9ac4ea182a29405b`;
all other source hashes agree with the table above. The former draft-status
paragraph has been replaced by an internally checked study-theorem status,
with explicit fitting/source dependencies and a distinction from promotion.
The scoped assembly verdict remains **PASS**.

The final choices
\[
 a_1=(2Y/\sqrt\lambda+1)^2,
 \qquad a_4=16\beta^{114L}(Y/\lambda)^4+1
\]
have fixed positive slack over the fitting and source bounds and are valid
eventually after the vanishing numerical error. The final-layer conditioning
now explicitly stops at layer \(L-1\). The variance constant \(v_0\),
extended endpoint on fitting failure, radius \(2c/\sqrt n\), and choice
\(c=\delta\sqrt{2\pi v_0}/16\) agree with the derivation in Section 4.
Neither the theorem scope nor the label cap has changed.

The final dependency section cites another note for the activation-strip
membership. That note was not accessed under this audit's source boundary;
the asserted elementary fact can also be checked directly. For GELU,
\(\Phi(x+iy)=\Phi(x)+i\int_0^y\varphi(x+it)\,dt\), where
\(\varphi(z)=e^{-z^2/2}/\sqrt{2\pi}\). On every fixed horizontal strip,
both this function and \((x+iy)\varphi(x+iy)\) are bounded, proving the
required bound for \(\phi'(z)=\Phi(z)+z\varphi(z)\). For SiLU on
\(|y|<1\), putting \(r=e^{-x}\) gives
\[
 |1+re^{-iy}|\ge\cos(1/2)(1+r).
\]
Thus its logistic factor is bounded and its derivative is at most
\(\sec^2(1/2)e^{-|x|}\) in modulus. Multiplication by \(|x+iy|\) still
leaves a bounded function, so SiLU's first derivative is bounded on this
pole-free strip. Their second derivatives on a smaller strip are bounded
by Cauchy's formula, as required by the common paper envelope.

The revised status is appropriate within the expressly stated modular
boundary. This audit neither reads nor substitutes other reports' verdicts,
and does not authorize or perform manuscript promotion.
