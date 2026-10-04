# Internal audit of the quantitative Gaussian-program argument

Date: 2026-10-01. Scope: fresh mathematical review of the finite-program coupling, its population bias, and the empirical oracle event. This is an internal scoped review, not a promotion review or a verdict on every component of the all-time theorem.

**Verdict: qualified PASS within the assigned scope.** I found no blocking mathematical flaw in the estimate

\[
\xi_N=e^{CN^5}n^{-1/8}+Ce^{-cN^2},
\qquad
\Pr(\text{oracle failure})\le e^{CN^5}n^{-1/2}+Ce^{-cn},
\]

under the stated fixed-depth, finite-data, small-label hypotheses and the paper's original population Euler estimates. The qualification identifies substantive dependencies rather than adding an assumption on the finite network: uniform original population carrier tails and uniformly bounded common initialized operators are necessary inputs. The quantitative argument does not itself establish those inputs from a general adaptive-program hypothesis. Their explicit supplied sources are `paper/proof_alltime.tex:488–506`, `:534–554`, `:556–703`, and `:739–815`.

I independently checked the relevant conditioning, noise regularization, moment, concentration, stopping, bias, and instruction-count steps below. I did not use `PROGRAM_RATE_CHECK.md`, another review, a study README, another study, an external source, Git history, training, or numerical experiments.

## Inputs and complete reading scope

The three study files were read in full, including all of Addendum Section 9. The following paper passages were read directly with their line numbers; the five authorized paper files were also searched for the dependency terms Gaussian, conditioning, population, Euler, operator, tail, carrier, and mollification. Unread paper portions are not implicitly certified.

| Input | Direct reading scope | SHA-256 of complete file |
|---|---|---|
| `RESULT.md` | 1–268, complete | `8050f8ff34f00e1263e422d8b8a51bba85be4ae216cec5bd66299b7b2454c267` |
| `PROGRAM_RATE_ROUTE.md` | 1–462, complete | `d6c7683057b03f710f73be4922a4411ad514bb3e508d3f17678c411a58a0547a` |
| `PROGRAM_RATE_ADDENDUM.md` | 1–863, complete | `a11c6e70204a0202da18075afc6565f6e46205de08865cdbcc5c5c38fccd43b7` |
| `paper/main.tex` | 165–240 | `60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95` |
| `paper/results.tex` | 1–100 | `6e76e83aae3a3e36f588bdf37dddf72ac811bf2644de664fb0b4b83f117704a1` |
| `paper/proof_alltime.tex` | 1–105 and 140–928 | `f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d` |
| `paper/proof_tracking.tex` | 1–110 and 254–319 | `e75f8122ab0ed0bc5f8c0b5f979b7e1a1b779c94440367d62d9a98892d3e53be` |
| `paper/proof_finite_time.tex` | 1–125 | `07ebf620943f5e8078e4f7647dfa9df893157f16d29c684e758dcd63d33eacd4` |

Study paths in this table are relative to `studies/response_memory_explicit_width_rate_20261001/`; paper paths are relative to the repository root. The latter location was clarified by the supervisor after the initially attempted study-local paper paths did not exist. No mathematical input remained missing for this scoped audit. No maintained-book dependency was needed or fetched.

Required process material read: `/etc/codex/skills/solve-math-rigorously/SKILL.md`, `/etc/codex/skills/investigate-conjectures/SKILL.md`, and its `references/adversarial-audit.md`. The explicit scoped assignment replaced ordinary author startup.

## 1. Exact adaptive conditioning, including both orientations

**Checked:** Route 194–216 and 239–246, 326–340; paper `proof_alltime.tex:383–420`.

Let the transcript contain the already revealed constraints `WV=Y` and `W^T U=Q`, with their query columns fixed after conditioning on that transcript. Adaptive queries cause no extra matrix constraint: their dependence on earlier answers is already recorded in the transcript. Revealing a new independent query-noise root also conveys no information about any matrix. Inductively the unrevealed Gaussian matrix factors remain conditionally independent between distinct matrices.

When both previous query Grams are invertible, set

\[
M=Y(V^TV)^{-1}V^T+U(U^TU)^{-1}Q^TP_{V^\perp}.
\]

Compatibility `U^T Y=Q^T V` gives `MV=Y` and `M^T U=Q`. Its two summands are orthogonal to every homogeneous perturbation `P_{U^\perp}AP_{V^\perp}`. Thus Gaussian orthogonal projection gives the conditional matrix as this mean plus `P_{U^\perp}\widetilde W P_{V^\perp}`. For `h_\perp=h-V\alpha_n`, this yields precisely

\[
Wh=Y\alpha_n+U\beta_n+
 \sigma_nP_{U^\perp}g,
\quad
\sigma_n=\|h_\perp\|_2/\sqrt n,
\quad
\beta_n=(U^TU/n)^{-1}(Q^Th_\perp/n).
\]

The transpose call has the exchanged formula. In particular, the reverse-query correction `U\beta_n` and the removed output projection are both retained. No fresh independent matrix is substituted for the actual transpose.

The vectors `g` may be constructed independently of the full previous transcript at each reveal, using auxiliary randomness in degenerate directions when needed. The reference recursion uses deterministic population coefficients and the same Gaussian coordinate arrays. Within each layer it then applies coordinatewise deterministic functions to iid root/innovation tuples, so the reference rows are iid. The actual rows need not be iid. This is the exact distinction needed for Route 258–264.

## 2. Fresh input noise supplies both required lower bounds

**Checked:** Route 144–190 and 317–324; Result 125–149.

For a new scalar query `v_j=h_{0,j}+\epsilon\chi_j`, the new centered unit Gaussian `\chi_j` is independent of all prior scalar nodes and `h_{0,j}`. Consequently, for every deterministic coefficient vector `a`,

\[
\left\|v_j-\sum_{i<j}a_iv_i\right\|_2^2
=\left\|h_{0,j}-\sum_{i<j}a_iv_i\right\|_2^2+\epsilon^2.
\]

Taking the infimum proves the Schur-complement bound `\epsilon^2`, including when all unmodified queries vanish or coincide. It applies separately to the input-query lists in both orientations. With `p\le N`, `\epsilon=e^{-N^2}` and `\|v_i\|_2\le B=(CN^2)^{N+1}`,

\[
\det G_p\ge\epsilon^{2p},\qquad
\lambda_{\min}(G_p)\ge
\frac{\epsilon^{2p}}{(pB^2)^{p-1}}\ge e^{-CN^3}.
\]

Here `\log B=O(N\log N)`; its contribution to the last exponent is at most `O(N^2\log N)`. The dominant noise contribution is `2pN^2=O(N^3)`.

The same orthogonal-distance calculation gives the population innovation standard deviation `\sigma\ge\epsilon`. Therefore

\[
|\sigma_n-\sigma|
\le\epsilon^{-1}|\sigma_n^2-\sigma^2|.
\]

No empirical innovation lower bound is required. This avoids a repeated square-root loss. Reverse constraints only project the output innovation onto an at-most-`N`-dimensional complement; their finite-rank effect is handled separately below.

## 3. Constants and empirical conditioning remain controlled as N grows

**Checked:** Route 157–168, 218–235 and 248–353.

The RMS bound `B` precedes the regression argument. It follows from the common operator bound, coordinate Lipschitz/intercept bounds `CN^2`, and bounded frozen deterministic memory coefficients. It is therefore not circular in the inverse Gram estimates.

Writing `\gamma=e^{-CN^3}`, each regression coefficient is bounded by a fixed polynomial in `N,B,\gamma^{-1}`. For example `\|\alpha\|_2\le\gamma^{-1}\sqrt p B^2`; the bound for `\beta` follows by expanding `h_\perp=h-V\alpha`. This gives coefficient sums `e^{CN^3}`. At most `N` successive linear, coordinate, and regression instructions then give

\[
\max_v\|v\|_4\le e^{CN^4}.
\]

Set `t=n^{-1/4}`. Every required reference pairing has empirical variance at most `M_4^4/n`, where `M_4=\max_v\|v\|_4`. The same estimate holds for the squared soft-tail test, uniformly over deterministic nonnegative thresholds, because

\[
0\le (|v|-M)_+^2\le |v|^2.
\]

Thus `O(N^2)` reference tests fail with probability at most `e^{CN^4}n^{-1/2}`. For every removed projection, conditioning on the past gives

\[
\mathbb E[\|P_Ug\|_2^2/n\mid\text{past}]\le N/n.
\]

Markov at squared threshold `t^2` and a union bound over at most `N` calls cost `O(N^2n^{-1/2})`. No independence between projection events is needed. Gaussian root-norm and fixed-number initialized-operator events supply the additional exponentially small probability. Factors polynomial in `N` can be absorbed in `Ce^{-cn}` in the stated width regime.

Let `e_j` be the maximum actual/reference RMS discrepancy through instruction `j`. Reference norm tests and Cauchy–Schwarz give the empirical pairing perturbation

\[
t+C(B+1)e_j+e_j^2.
\]

Below `CN(B+1)(e_j+t)\le\gamma/2`, Weyl's inequality and the inverse identity give

\[
\|G_n^{-1}\|\le2/\gamma,
\qquad
\|G_n^{-1}-G^{-1}\|
\le2\gamma^{-2}\|G_n-G\|.
\]

Every regression step involves a fixed number of matrix products and inverse perturbations; the sizes contribute only powers of `N`. Its coefficient and variance discrepancies are therefore a fixed polynomial in `N,B,\gamma^{-1}` times `e_j+t`. Including the innovation-floor factor and removed-projection term gives

\[
e_{j+1}\le e^{CN^3}(e_j+t),\qquad
e_N\le e^{CN^4}n^{-1/4}.
\]

With a sufficiently large fixed constant in `\log n\ge CN^5`, the last quantity and `t` are strictly below the stopping threshold. Hence the stopped induction never stops. The advertised larger exponent `CN^5` is sufficient for the coupling, event probability, and all auxiliary factors. It is not a hidden fixed-`N` assertion.

## 4. Population bias and coefficient provenance

**Checked:** Route 70–95, 98–140; Addendum 96–116 and 184–194; paper `proof_alltime.tex:488–703`, `:739–815`.

The bias comparison uses the original and clipped/noisy programs on common population spaces with the same bounded initialized operator and its adjoint. For each fixed `N`, the qualitative joint-program construction supplies this coupling. Taking a countable family if desired supplies the same operator bound for the sequence of `N` used here; no convergence rate is extracted from qualitative convergence.

At a matrix instruction, the additional error is at most `K_0\epsilon`. At a carrier product,

\[
\|g(Z')\operatorname{clip}_N(P')-g(Z)P\|_2
\le jN\|Z'-Z\|_2+s\|P'-P\|_2
 +s\|P\mathbf1_{|P|>N}\|_2.
\]

Only the original carrier appears in the last term. The supplied original Euler bound makes it `Ce^{-cN^2}` uniformly in duration and step count. The original learned-memory coefficients remain fixed in the modified program, so no difference of population feedback coefficients enters this induction. Thus

\[
E_N\le(CN^2)^{N+1}(e^{-N^2}+Ce^{-cN^2})\le Ce^{-c'N^2}
\]

for sufficiently large `N`.

The uniform original coefficient assertion is also valid. A forward memory coefficient has magnitude bounded by

\[
\frac2m h_r|r^o_{b,r}|\,
 |\mathbb E[H^o_{b,r}H^o_{a,k}]|
\le C h_r\rho^o_r,
\]

using fixed sample count and uniform feature RMS. The reverse version uses uniform backward RMS. Summing in `r` uses the paper's `\sum_rh_r\rho^o_r\le2Y/\lambda`, not the physical duration. These are learned-memory coefficients; they must not be confused with the larger, but explicitly bounded, Gaussian-regression coefficients.

The supplied population tail proof uses bounded `g,g'` first for smooth activations. Its response-cap construction has constants independent of step count (paper 632–703). For the stated `C^1` activations with Lipschitz derivative, mollifications share the slope, derivative-Lipschitz, intercept, activity, and Gram margins. At a fixed finite Euler program, continuity of bounded-gate products in `L^2`, frozen deterministic pairings, and bounded common operators passes its node values to the original program. Fatou then passes the same tail constants. No estimate uniform in `N` for the mollification error is needed: each original program inherits the same already uniform tail constant before the quantitative argument is applied.

Comparing an empirical pairing with its original population expectation is legitimate after this bias estimate: both physical scalar-node norms are `O(1)`, since modified norms differ from original norms by `Ce^{-cN^2}`. A factor `B` need not appear in the oracle physical-field bounds.

## 5. Scalar tests, probe normalization, and the oracle event

**Checked:** Route 43–60, 355–361; Addendum 22–45 and 145–204; Result 243–258.

For `T_M(v)=(|v|-M)_+`,

\[
|\|T_M(v_n)\|_n-\|T_M(v_n^*)\|_n|\le e_N,
\quad
|\sqrt a-\sqrt b|\le\sqrt{|a-b|}.
\]

Thus the reference empirical squared-tail tolerance `t` costs only `\sqrt t=n^{-1/8}` at the final norm observation. The population bias costs `Ce^{-cN^2}` because `T_M` is 1-Lipschitz. Finally

\[
\|v\mathbf1_{|v|>M}\|_n
\le2\|(|v|-M/2)_+\|_n
\]

gives exactly Addendum (A7)–(A8). No concentration of the discontinuous indicator is asserted. Thresholds `M/2` and `R/2` are selected in advance; the moment bound is uniform over their values.

With `K` Euler intervals and `P\le K` probes, expanded vector instructions and noise roots total `O(K^2(1+P))`, covered by `N=\lceil C_0K^3\rceil`. There are `O(N^2)` possible node pairings. Carrier tests at `O(K)` training nodes and `N` thresholds total `O(KN)\le O(N^2)`. They are observations and create no additional matrix calls. The exact padded choice of `N` ensures the clipping bias decays; a mere upper bound on `N` would not suffice for that purpose.

For a passive input, the normalized map `u\mapsto\phi(s_xu)/s_x` has slope at most `s` and intercept at most `a`, uniformly in `x`, where `s_x=1+\|x\|/\sqrt d`. Its derivative-Lipschitz constant need not be uniform, but the passive program uses no backward derivative of that map. Its initial normalized Gaussian root has uniformly bounded moments. The regression, coefficient, and bias estimates therefore have constants uniform in a single normalized probe. Separate probe programs avoid exceeding the instruction budget on a larger bounded-domain net.

The auxiliary query noises can be marginalized out. The claimed dense prediction errors and dense carrier remainder are functions of the original initialization alone. If such a conclusion holds on an augmented-space event of probability at least `1-p`, its failure under the original initialization has probability at most `p`. This explains why proof-only randomness does not change the theorem's model or require a user-visible random algorithm.

For the proposed `K=(\log(e^e+n))^{1/128}` and `N=\lceil C_0K^3\rceil`,

\[
N^5=O((\log n)^{15/128})=o(\log n).
\]

The growth condition holds eventually; the finite-width terms and failure probability are polynomially small in `n`, while `e^{-cN^2}` is smaller than every fixed inverse power of `K`. This establishes the Gaussian-program input needed by the separate damped transfer argument, not by itself the complete all-time theorem.

## Findings and disposition

1. **No blocking finding in the assigned Gaussian-program scope.** Inverse conditioning, both matrix orientations, innovation independence, population bias, iid-reference empirical concentration, and growing instruction budgets have the required quantitative bounds. The decisive upstream tail and bounded-operator dependencies are explicitly supplied by the paper; they are not newly assumed finite-width concentration.
2. **Minor wording clarification:** Result 116 says noise is added at “every initialized-matrix query,” whereas Addendum 270 correctly treats the first-layer action as exact. The quantitative matrix-call model is for the square hidden initialized matrices. The first-layer matrix is represented by its iid Gaussian row roots and deterministic input linear combinations (`paper/main.tex:177–201`). State this convention explicitly to avoid suggesting noisy first-layer actions while asserting a zero first-layer discrepancy. The construction and estimates already support this reading.
3. **Scope limit:** This review does not independently certify every Legendre estimate, the entire all-order fitting proof, the final damped-transfer artifact, or the final all-time theorem. Addendum Section 9 was read, but the verdict here concerns its Gaussian oracle inputs and their stated budgets. No polynomial-in-width rate is established by this audit.

No source, model, or proof correction is required to repair a blocking error in this scope. The minor first-layer wording clarification would make the presentation more precise.
