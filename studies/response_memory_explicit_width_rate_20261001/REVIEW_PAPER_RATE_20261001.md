# Paper compatibility, quantifiers, and rate audit

2026-10-01. Independent scoped internal audit of `RESULT.md`; this is not a promotion review.

**Verdict: conditional PASS for paper compatibility, quantifiers, and rate arithmetic.** I found no defect in the claimed exponent `1/512`, the all-order event, the finite-second-moment test-law passage, or the all-time/end-point extension, provided the quantitative finite-program and physical-proxy estimates stated in the study hold with their advertised uniform constants. Those estimates were hypotheses of this assignment, not independently certified by this report. Thus this report alone does not establish the unconditional explicit-width theorem.

## Scope, provenance, and actual coverage

The supervisor assigned the paper-compatibility and quantifier audit, explicitly directing that the Gaussian-program and damped-comparison rates be treated as hypotheses for the arithmetic audit. The assigned scientific inputs were `RESULT.md`, `DAMPED_TRANSFER.md`, the current `paper/main.tex` and its included theorem/proof/appendix files, and `paper/NOTES_alltime_theorem.md`. A later scope extension supplied `PROGRAM_RATE_ADDENDUM.md`, Sections 9.1–9.3, to resolve the precise interpolation-defect factor.

I read the following complete files, including every displayed equation and proof: `RESULT.md` (268 lines), `DAMPED_TRANSFER.md` (213), `paper/main.tex` (1620), `paper/results.tex` (233), `paper/proof_alltime.tex` (928), `paper/proof_tracking.tex` (319), `paper/proof_finite_time.tex` (502), `paper/comparison_appendix.tex` (327), `paper/sphere_appendix.tex` (29), and `paper/NOTES_alltime_theorem.md` (128). Truncated tool displays were reread in smaller ranges. For the addendum I actually read lines 530–775: Sections 9.1–9.3 and adjacent boundary context. The added source is used below only for the Section 9 interpolation/damping argument and its probe-budget clarification; earlier proxy and Gaussian-program proofs were not read.

No study README, `PROGRAM_RATE_CHECK.md`, other review report, other study, archived book, Git history, or historical conversation was read. No experiment, numerical simulation, manuscript edit, or Git mutation was performed. File enumeration was metadata only. The proof method follows the `solve-math-rigorously` skill and the `investigate-conjectures` adversarial-audit guidance. No external literature result is used to replace a missing in-scope argument.

SHA-256 at review time:

| Input | SHA-256 |
|---|---|
| `RESULT.md` | `8050f8ff34f00e1263e422d8b8a51bba85be4ae216cec5bd66299b7b2454c267` |
| `DAMPED_TRANSFER.md` | `27ee61e6aa1367329e0baf3e1ae41993ead53f323ba98af2942a1f034bd3a96c` |
| `PROGRAM_RATE_ADDENDUM.md` (partial content coverage above) | `a11c6e70204a0202da18075afc6565f6e46205de08865cdbcc5c5c38fccd43b7` |
| `paper/main.tex` | `60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95` |
| `paper/results.tex` | `6e76e83aae3a3e36f588bdf37dddf72ac811bf2644de664fb0b4b83f117704a1` |
| `paper/proof_alltime.tex` | `f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d` |
| `paper/proof_tracking.tex` | `e75f8122ab0ed0bc5f8c0b5f979b7e1a1b779c94440367d62d9a98892d3e53be` |
| `paper/proof_finite_time.tex` | `07ebf620943f5e8078e4f7647dfa9df893157f16d29c684e758dcd63d33eacd4` |
| `paper/comparison_appendix.tex` | `14cfb87d7f4932131c984781fc0bc03b955f883d4fc909c4794c2be4bcc1bedf` |
| `paper/sphere_appendix.tex` | `f1a5c87937b1c805faa89edee9fb2ad2809de1f873b4e83888ccf5e5cdf673e2` |
| `paper/NOTES_alltime_theorem.md` | `866e741ca5ea0a4f5883e437fd5d921d02bfec180121fe1134225acfefa7528b` |

## 1. The scientific contract matches the current paper

`RESULT.md:9–35` matches the network, initialization, mobilities, activation class, and small-label/Gram hypotheses of `paper/main.tex:177–201` and `paper/results.tex:17–33`. In particular, the hidden matrices are initialized at variance `1/n` and then reused with their actual transposes; the first layer has variance one, and the readout is exactly zero. Bounded activation values are not required.

The distance at `RESULT.md:37–44` is exactly `paper/main.tex:203–209`: first/readout blocks divided by `sqrt(n)`, hidden increments in unnormalized Frobenius norm. The population counterpart uses first/readout `L2` and hidden-increment Hilbert–Schmidt norms (`paper/proof_alltime.tex:503–506,552–554`). The proof does not assert convergence of initialized finite matrices to population operators in this parameter distance. Finite/proxy and population/Euler comparisons take place separately in their respective spaces; empirical prediction tests connect their scalar outputs.

`RESULT.md:29` correctly selects the original clock and closure, `paper/main.tex:332–379`: `dot(tau)=rho`, `tau(0)=1`, constant forward prefix, zero backward prefix, closure-generated responses, and unchanged first-layer/readout updates. The joint clock and the broader-label finite-time theorem are not substituted for this model. The raw closure has no division by `rho`; zero labels give the stationary case (`paper/proof_alltime.tex:311–338`).

The target at `RESULT.md:46` is the paper's deterministic **dense population predictor**. It is not a frozen kernel, an independently resampled reverse operator, or a uniquely identified population moment-state ODE at fixed order. The latter remains explicitly unclaimed in `paper/results.tex:214–233` and `paper/proof_tracking.tex:306–319`.

## 2. The paper actually supplies the named qualitative foundations

The following dependency map was checked against the actual current proofs, rather than inferred from the theorem statement or the notes file.

| Input used by the study | Current-paper source and scope |
|---|---|
| Common physical tube, Gram gap, global fitting for every order | `proof_alltime.tex:174–338`; deterministic on the single initialization event, with thresholds independent of width/order |
| Total activity and parameter/prediction speed | `proof_alltime.tex:324–337`; `proof_tracking.tex:256–288` |
| Exact two-orientation finite Gaussian conditioning | `proof_alltime.tex:383–437`; the displayed conditional mean obeys both transcript constraints and the residual Gaussian is projected on both complements |
| Singular query covariances and continuous/linear-growth instructions | `proof_alltime.tex:439–485`; a qualitative fixed-program argument, without a width rate |
| Common bounded initialized population operators and true adjoints | `proof_alltime.tex:488–506`; generated-span construction, same-array operator bound, and passage of the finite adjoint identity |
| Uniform population carrier tail envelope | `proof_alltime.tex:508–703`; small-activity response/field induction and uniform sub-Gaussian marginal bounds for the original Euler references |
| Strong population flow, gap, uniqueness, all-time endpoint, stated activation class | `proof_alltime.tex:705–815`; Euler comparison, strong limit, finite variation, and mollification |
| Dense carrier transfer and definition of `a_n` | `proof_alltime.tex:817–928`; qualitative fixed-program/fixed-cutoff transfer followed by monotonicity |
| Deterministic all-order tracking from `a_n` | `proof_tracking.tex:31–252` |
| Whole-input prediction and deterministic target | `proof_tracking.tex:254–304` |

I found no missing named qualitative foundation in this dependency chain. In particular, the common initialized operators and the uniform marginal tail estimate are supplied by arguments inside the current manuscript; this audit does not import those assertions from another study or from a general citation to Tensor Programs. The tail assertion is sub-Gaussian control of each time marginal, not Gaussianity of a trained carrier and not an exponential moment of its time supremum (`proof_alltime.tex:793–797`). The study only needs the former.

For the broad `C1` activation class with Lipschitz derivative, the paper's tail derivation first uses smooth activations, then removes smoothing with uniform activation/gate errors and common caps (`proof_alltime.tex:799–815`). For any fixed unsmoothed Euler program the same passage is available: finite instruction continuity, frozen deterministic coefficient convergence, and Fatou pass the uniform tail bounds. It creates no new label threshold or query covariance-gap assumption. It does not itself give a quantitative program-size/width modulus.

The initialization event can have polynomially small failure under the existing assumptions. Operator failures are exponentially small (`proof_alltime.tex:46–52`). First-layer quadratic averages have finite variance. For the Gram, the conditional covariance-entry Chebyshev estimate at lines 56–68 is `C/(n epsilon^2)` at every fixed tolerance. At each of the finitely many layers, continuity of the covariance map at its deterministic limit supplies a fixed positive input tolerance for a specified output tolerance, even at singular intermediate covariance. Backward selection of these finitely many tolerances and a union bound give `C/n` failure for a fixed final Gram margin. A quantitative Lipschitz inverse-covariance estimate is not needed for this initialization-only claim.

## 3. The correct remainder and every-order event are retained

The paper defines

\[
a_n=\sup_{M\in\mathbb N,\,M\ge1}
\bigl(Z_n(M)-Ce^{-cM^2}\bigr)_+,
\qquad b_n=C\Phi(a_n),
\quad \Phi(u)=u e^{K\sqrt{\log(e+1/u)}}.
\]

This is `proof_alltime.tex:915–925` and `proof_tracking.tex:233–252`. `RESULT.md:87–108` uses the correct dense **carrier** tail: the top carrier is `w`; lower carriers are `W^T delta`. It does not silently replace them by gated backward responses or initialization-only fields. Choosing the envelope constants once, as allowed at `RESULT.md:103`, merely fixes which admissible dense-only excess is being bounded.

For prediction, the additional term is essential:

\[
b_{n,\mu}=C_\mu\Phi(a_n)+d_{n,\mu},\qquad
d_{n,\mu}=\mathcal E_\mu(f_{n,D},f_\infty).
\]

It is correctly retained at `RESULT.md:105–112`, consistent with `proof_tracking.tex:297–303` and `NOTES_alltime_theorem.md:53–76`.

Once the good initialization event and the dense-only quantitative tail event occur, the deterministic paper proof applies to every positive integer order with the same constants. Its small-order fallback is also deterministic (`proof_tracking.tex:233–250`). No countable union of order-dependent probability bounds is required. Intersecting with one dense prediction event for a fixed `mu` preserves the all-order conclusion. This is exactly the common event claimed at `RESULT.md:63–79`.

“For all sufficiently large widths” has the usual per-width high-probability meaning. It does not claim one event on which the bounds hold almost surely for every width. Likewise the prediction event is common to all orders for each fixed test law, not one event simultaneously uniform over every probability measure.

## 4. Damping factor and proof-budget arithmetic

The exact residual subtraction is correct (`RESULT.md:186–190`, `DAMPED_TRANSFER.md:26–37`):

\[
\dot u=-2\Gamma_Du-2(\Gamma_D-\Gamma_p)r_p-J_pE_p.
\]

The actual dense Gram supplies damping. A proxy Gram gap is unnecessary. Leaving `r_p` in every response-change term yields amplification `exp(CR)` when `int rho_p` is bounded. This is the same one-reference mechanism as the paper, with dense and perturbed-reference roles chosen appropriately.

**Resolved source-factor check.** `DAMPED_TRANSFER.md:108–122` states the sufficient error factor `(1+T)(1+R)eta`, whereas `RESULT.md:172–206` uses the sharper `(T+1+R)xi`. This is not a defect: the addendum's `alpha(t)=(t-t_k)rho_k` at lines 560–564, pointwise defect (A28) at lines 605–608, and activity estimates at lines 614–622 integrate directly to (A29), `(T+1+R)xi`, at lines 624–629. Equations (A32) and (A35), lines 676–678 and 748–754, then give the factor used in RESULT. The weaker factor would also leave the final logarithmic exponent unchanged.

Write `ell_n=log(e^e+n)` and `k=floor(ell_n^(1/128))`. For sufficiently large widths, `k>=2` and `k` is within a fixed factor of `ell_n^(1/128)`. The choices at `RESULT.md:214–224` give

\[
N=O(k^3),\qquad N^5=O(\ell_n^{15/128})=o(\log n),
\qquad T=O(\log k),\quad h=O((\log k)/k),\quad R=O(\sqrt{\log k}).
\]

Consequently `exp(CN^5)n^(-1/8)=n^(-1/8+o(1))`, while the quoted finite-program failure is `n^(-1/2+o(1))+Ce^(-cn)`. Polynomial factors in `N`, including finite unions of scalar empirical tests, are absorbed by decreasing a fixed positive width exponent. The program bias `exp(-cN^2)` is smaller than every fixed negative power of `k`, and `T xi<=1` eventually. Choose the fixed cutoff constant so `exp(-cR^2)<=k^(-4)`. Then

\[
e^{CR}(1+R)h
=k^{-1}\exp(O(\sqrt{\log k}))O((\log k)^{3/2})
=k^{-1+o(1)}.
\]

The remaining activity after `T=(2/kappa)log k` is `O(k^(-2))`. Additional factors `1+R`, or a final `Phi` transform, are `k^(o(1))`. Thus, conditional on the finite-program/proxy transfer,

\[
a_n\le k^{-1+o(1)},\qquad
b_n\le Ck^{-1/3}\le C\ell_n^{-1/512}.
\]

The last inequality has slack: `k^(-1/3)` is of order `ell_n^(-1/384)`. The stronger chain in `DAMPED_TRANSFER.md:141–175`, `k^(-3/4)` to `k^(-2/3)` to `k^(-1/2)`, is also arithmetically consistent. No polynomial width-accuracy conclusion follows from these choices.

For the budget, a single normalized passive probe and the unrolled training operations fit `N=C_0 k^3` as asserted. The addendum explicitly states elementary count `C k^2(1+P)` for `P<=k` (`PROGRAM_RATE_ADDENDUM.md:549–556`). Scalar tail observations can be polynomially numerous without introducing that many extra initialized-matrix query instructions. This audit checks the budget consequence of that stated count; the full elementary-program construction remains outside the independently verified scope.

## 5. Unbounded queries, finite-second-moment laws, and nets

Set `s_x=1+||x||/sqrt(d)`. The normalized first-layer query vector is bounded, and the passive activation map

\[
\psi_{\ell,x}(u)=\phi_\ell(s_xu)/s_x
\]

has uniformly bounded intercept and slope: `|psi(0)|<=a` and `|psi'|<=s`. Its derivative need not have a uniform Lipschitz constant in `x`; indeed that constant can grow like `s_x`. This causes no loss here because passive prediction instructions use only forward activations and linear actions. They do not add passive backward responses or differentiated gates. Thus `RESULT.md:245` uses the appropriate normalization for a first-derivative/Lipschitz finite-program estimate. The uniform quantitative **program** conclusion for this class is still one of the assigned hypotheses.

On the original physical good event, the paper gives the deterministic envelope and input Lipschitz bound (`proof_tracking.tex:256–288`), also inherited by the population predictor. If `X_n(x)=sup_t|f_{n,D}(t,x)-f_infty(t,x)|`, a per-probe good event with error `Cs_x k^(-1/2)` and probability complement `Cn^(-c)` therefore implies

\[
\mathbb E[\mathbf1_{\mathcal G_n}X_n(x)^2]
\le Cs_x^2(k^{-1}+n^{-c}).
\]

No moment of the dynamics off `G_n` is needed: the random quantity is defined to be zero there. For `S_mu=int s_x^2 dmu<infinity`, Tonelli gives

\[
\mathbb E[\mathbf1_{\mathcal G_n}d_{n,\mu}^2]
\le CS_\mu(k^{-1}+n^{-c}).
\]

At threshold `C_mu k^(-1/4)`, Markov gives failure

\[
O_\mu(k^{-1/2}+k^{1/2}n^{-c})+\Pr(\mathcal G_n^c)
\le C_\mu\ell_n^{-1/512}.
\]

The omitted factor `k^(1/2)` on the polynomial-width term in `RESULT.md:256` is harmless after decreasing the generic positive exponent `c`; it is not an additional assumption. The error threshold itself is `k^(-1/4)=O(ell_n^(-1/512))`. Constants need only `S_mu`, which is bounded by a function of the second input moment. There is no assumption of bounded support or a rate for the tail of `mu`.

The stronger input from `DAMPED_TRANSFER.md:179–205`, squared per-probe error `k^(-3/2)`, gives threshold and failure both `k^(-1/2)` and hence exponent `1/256`. The stated `1/512` is a valid weakening.

For a fixed bounded domain, a mesh `k^(-1/2)` has at most `C_X k^(d/2)` points. Run the single-probe argument separately at each point and union-bound, yielding `C_X k^(d/2)n^(-c)<=C_X n^(-c')` for some fixed `c'>0`. The common input Lipschitz bound fills the gaps in the net. No independence is needed, and the entire net is never inserted into one `N=O(k^3)` program. Thus there is no dimension-dependent violation of the instruction budget in `RESULT.md:258`. The stronger mesh in `DAMPED_TRANSFER.md:207` works by the same calculation.

## 6. Infinite time, endpoints, and claim boundaries

The all-time extension uses the dense and population prediction variations after `T`, each bounded by `Cs_x e^(-kappa T)` (`proof_alltime.tex:784–797`, `proof_tracking.tex:279–300`). The proxy need not be trained or proved to fit beyond `T`. An estimate on `[0,T]`, its value at `T`, and these two tail variations control every later time. The same finite-variation argument gives the actual limiting fitted functions. Parameter convergence and the deterministic pointwise prediction inequality transfer the conclusion to every closure order at `t=infinity`. Time continuity permits the supremum to be taken over a countable dense set when measurability is needed.

There is no exchange of a time supremum and an expectation in the test-law argument: the per-probe random variable already contains `sup_{t>=0}`, and Tonelli applies to that nonnegative measurable quantity. The theorem concerns a common physical-time trajectory and its true limiting endpoint, not separately chosen finite-loss stopping times from the experimental figures.

The final claim boundaries in `RESULT.md:260–268` agree with the paper: an explicit logarithmic width remainder would not establish root-width sampling accuracy, unconditional initialization-averaged error moments, an `epsilon^(-5/2)` moving-state guarantee, a fixed-order deterministic moment law, or a universal algorithmic lower bound. The special linear lower-bound example named at line 266 was not an input to this audit and is not certified here.

## Outstanding dependency boundary

No arithmetic or paper-compatibility correction is required by this audit. A complete theorem verdict still requires independent verification of the quantitative growing-program construction and its physical reconstruction consistency, including uniform normalized-probe constants, joint empirical/tail tests, the exact filtration and two-orientation coupling, and the advertised `exp(CN^5)` loss. Their main proofs are in `PROGRAM_RATE_ROUTE.md` and the earlier sections of `PROGRAM_RATE_ADDENDUM.md`, outside this audit's initial scope and not certified here. The current paper supplies only fixed-program qualitative convergence; it cannot substitute for those quantitative checks. The addendum's Section 9 resolves the interpolation-factor issue but does not, on its own, discharge the earlier program and node-consistency obligations.
