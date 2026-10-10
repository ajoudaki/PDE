# Fresh isolated notation and mathematical-interface audit

Date: 2026-10-09. Scope: the five frozen compact-manuscript sources listed below, read completely. This is an independent adversarial audit of persistent semantic notation, statement interfaces, and selected mathematical normalizations. It is not an empirical or novelty review.

## Verdict

**PASS for the strict limit of at most 30 globally remembered semantic symbols. My independent count is 29.** I found no additional quantity whose meaning has to survive outside the public statement/proof module that binds it. This conclusion comes from tracing later uses, not from accepting the manuscript's inventory table.

Statement-only reading works for the dependency chain: the fitting, analytic-source, projection, Legendre, dense-variability, selection, transfer, compiler, approximation, and final-construction statements supply the objects and hypotheses needed by their consumers. The subsequent proofs rebind their auxiliary parameters or explicitly instantiate a public statement. I found no imported private source coefficient, undefined nonstandard norm needed by a consumer, suppressed sample/gap factor, or added hypothesis in the checked interfaces.

No fatal, major, or minor concern requiring a repair was established. The checked interface algebra is sound. This conclusion is narrower than a full independent rederivation of every stochastic remainder bound in the long source proof.

## Isolation, complete coverage, and immutable-input check

Scientific inputs were restricted to these files. I read all 3,958 lines, including every proof, inner claim, coefficient table, and final assembly:

| File | Complete coverage |
|---|---:|
| `paper/compact.tex` | 1–290 |
| `paper/compact_fitting.tex` | 1–244 |
| `paper/compact_foundations.tex` | 1–1554 |
| `paper/compact_legendre.tex` | 1–752 |
| `paper/compact_selected.tex` | 1–1118 |

The first combined read of `compact.tex` had an output truncation; I separately reread lines 118–181, including the full notation table and scope declaration. The other manuscript reads were bounded, untruncated chunks. Targeted follow-up searches were restricted to the same five files.

Required process inputs read completely:

- `/etc/codex/skills/solve-math-rigorously/SKILL.md`;
- `/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` and its `references/neural-response-memory.md`;
- `/home/codex-b/.codex/skills/review-ai-paper/SKILL.md` and its `references/severity-rubric.md`.

The explicit isolated assignment and single-report format controlled source access and output. I did not read a study README, inventory file, another study, another review, prior verdicts, Git history, the original paper, or external scientific sources. I made no manuscript edits, ran no experiments, and created no scratch products.

Before/after SHA-256 checks were identical:

| File | SHA-256 before and after |
|---|---|
| `compact.tex` | `a56acbdc765fa6e42f8aba186dec0b3ea3a59e9fa4c7d66ac1a7839bc0688445` |
| `compact_fitting.tex` | `f35f1dfd9c47bd5abbf97c849b0176347e9e5da8adba5e7ab8b75c79868b2c51` |
| `compact_foundations.tex` | `4e7d25a8501e7928f60e538f1c80e7e73a3e2f04d34a1ae4d40407ffc1f545f9` |
| `compact_legendre.tex` | `bca774baab3a5ba9879340fc61a92b9cbdff522600620d1972ab12b876f48239` |
| `compact_selected.tex` | `cd203e7de6f8e3d23331d58ac64366350dd076405d63e8fc238f8f9a794beeee` |

## Independent semantic inventory

I count a mathematical object family once when layer/sample indices select instances of the same definition. I count different meanings separately even when they use the same letter. Ordinary operators, derivatives, transposes, evaluations at time zero, bound indices, and variables quantified inside a single statement/proof do not create persistent semantic objects. A proof's temporary symbols are excluded only after checking that later modules can discard them.

| Number | Persistent object | Binding in `compact.tex` |
|---:|---|---|
| 1 | Width, \(n\) | 59–63 |
| 2 | Number of training examples, \(m\) | 59 |
| 3 | Input dimension, \(d\) | 60 |
| 4 | Hidden depth, \(L\) | 61 |
| 5 | Passive-panel size, \(p\) | 136–138 |
| 6 | Input family/query, \(x\) | 59–60 |
| 7 | Normalized input, \(v=x/\sqrt d\) | 61, 65–66 |
| 8 | Labels, \(y\) | 59, 73–74 |
| 9 | Physical time, \(t\) | 84, 128–135 |
| 10 | First/hidden weight family, \(W\) | 62–63, 69–71 |
| 11 | Readout, \(w\) | 63, 72 |
| 12 | Preactivations, \(z\) | 69–71 |
| 13 | Features, \(h\) | 70–71 |
| 14 | Residuals, \(r\) | 73 |
| 15 | Residual-free backward responses, \(\delta_a^{(\ell)}\) | 77–82 |
| 16 | Layer activation family, \(\phi\) | 64–65, 71, 99–105 |
| 17 | Activation-strip width, \(a\) | 99–100 |
| 18 | Activation envelope, \(\beta\) | 101–106 |
| 19 | Population feature-Gram family, \(Q\) | 108–112 |
| 20 | Population gap, \(\gamma\) | 113 |
| 21 | Label RMS, \(Y\) | 114 |
| 22 | Training loss, \(\mathcal L\) | 74 |
| 23 | Promised query domain, \(\mathcal X\) | 128–138 |
| 24 | All-time/query discrepancy norm, \(\|\cdot\|_{\mathcal X}\) | 129–135 |
| 25 | Failure probability, \(\delta\) | 142–149 |
| 26 | Activation/depth-only constant convention, \(C\) | 124–126 |
| 27 | Coupled dense predictor, \(f_n\) | 72, 191–193 |
| 28 | Independent dense predictor, \(\widetilde f_n\) | 139–140 |
| 29 | Compressed predictor, \(f_{\rm model}\) | 174–175, 182–193 |

In particular, the backward-response \(\delta\) and confidence \(\delta\) count separately. The input and its normalization also count separately. Method names on \(f_{\rm model}\) select its three constructions; they are not additional persistent predictors. Initialized values such as \(W_0^{(j)}\) are evaluations of the same trajectory. Derivatives \(\phi',\phi''\) and ordinary Euclidean/operator/Frobenius norms are standard operations rather than new remembered definitions.

## Where the remaining notation is bound

The following is the exhaustive scope partition for nonpersistent notation. Each row covers the entire indicated statement/proof block, including its inner claims; all remaining symbol introductions fall inside these blocks. Examples identify the significant families rather than counting their many indexed instances as global objects.

| Scope | Locally bound objects and boundary check |
|---|---|
| Fitting statement/proof, `compact_fitting.tex` 4–207 | The statement defines \(H,\mathsf H,\theta,\|\cdot\|_{\rm par}\). Its proof binds \(\lambda,\rho,s,b,D_j,U_j,F_j,F\), Gaussian/net/covariance variables, and stopped-horizon variables. Later uses take the stated Gram, tail, or norm formulas. Legendre independently defines its own \(H,s,b,D_j\) at 107–116. |
| Signed perturbation statement/proof, fitting 209–244 | \(F,\theta,\theta',J,J',\rho,\rho',K,e,\mathcal E\) and proof variables \(d,R,\epsilon\) are explicitly bound to this generic estimate. These uses do not redefine the global input dimension or residual family. |
| Analytic-source statement, foundations 8–103 | \(T,r_t,r_q\), the finite lists, and panel variables \(J,t_b,r_b\) are local quantified data/results. Passive backward responses are explicitly defined by the ordinary recursion. The exported bounds are in canonical quantities, including all factors of \(m,\gamma,Y,d,n\). |
| Analytic-source proof, foundations 105–1554 | The entire coefficient ledger, \(\lambda,S,\ell,k\), working radii, mobility coordinates, cavity/root/port variables, budgets, insertion maps, Gaussian processes, moment orders, and expanding-domain functions are proof-private. Working radii are explicitly redefined at 309–314 and compared with the statement at 1484–1553. No `cp:src-*` private claim or equation is referenced from another manuscript module. |
| Projection statement/proof, Legendre 4–76 | \(A,q,P_j,p_j^A,\Pi_q^A,u,g\), endpoint kernel and one-dimensional polynomial estimates are local. The construction recalls the projection definitions at 176–179. |
| Legendre statement/proof, Legendre 78–534 | The statement binds the order \(q\). The proof defines its own parameter scales, hatted closure state, moments, clock \(\tau\), histories, defects, parameter discrepancy, comparison coefficients, norms and thresholds. Local fitting/comparison subarguments share these within one construction. No later theorem requires those internal objects. |
| Derivative-transfer statement/proof, Legendre 539–570 | \(r,M,g,N\), Chebyshev coefficients, polynomial and Joukowski variables are local. Here \(r\) is a radius, explicitly distinct from the global residual meaning. |
| Dense-variability statement/proof, Legendre 572–752 | The statement quantifies \(c_{\phi,L,\delta}\). Moment variables, innovation witness, conditional law, shifts and transfer radius are private. The assembly uses the stated lower bound and explicitly fixes its confidence budget. |
| Sparse-coordinate statement/proof, selected 11–86 | \(E,r,I,D,M\), the metric norm, activation bounds, barrier variables and basis matrices are local. The transfer proof obtains new layer-indexed metrics by explicitly applying this statement. |
| Source-to-runtime statement/proof, selected 90–657 | The statement defines \(W_0,T,\eta,q,E_j\) and the source contract. The proof binds all selected/reference states, deficits, metrics/adjoints, corrected readout, sample Grams, Hilbert norms, coefficients and errors. In particular \(Q_C\) is explicitly a local sample Gram, not the population \(Q\). The finite-horizon claim and fitting claim are internal to this one construction. Later source methods use only its error, tolerance and retained-count formulas. |
| Initialized-jet compiler, selected 661–765 | Rectangle data, conformal-map variables, Taylor coefficients, parameter tuple/vector field, truncation order and quadrature variables are introduced locally. No conformal-map coefficient is imported into a subsequent construction. |
| Joint approximation statement/proof, selected 769–903 | \(T,r_t,r_q,M_n,\eta,\alpha_T,b_d,D_d,P_T,H_*,N,N_1,H_1\) are defined in the statement. Harmonic spaces, their basis/dimension/projectors, generating-function and lattice variables are proof-local. The Harmonic proof explicitly instantiates the statement at 920–945. |
| Harmonic construction, selected 905–993 | Its proof rebinds \(\lambda,z,\ell,T,\eta,r_t,r_q,M_n,\alpha_T,N,N_1,R\), with radii written out in canonical quantities. It does not reuse a source-proof working radius or coefficient. |
| Logarithmic construction, selected 997–1118 | Its proof rebinds \(\lambda,z,\ell,T,J,t_b,r_b,M_n,\eta,K\), coefficient-curve variables and the exact input reduction \(U_0,k,R\). No panel clock or forcing schedule remains as unexplained runtime state. |
| Headline assembly, `compact.tex` 254–288 | \(\delta_0\) is fixed locally; the dense lower-bound coefficient is supplied by the public variability statement. No private implementation coefficient appears. |

The long source proof is a substantial module, not a device that wraps the whole paper in one proof. It has a concrete public contract consisting of three analytic-domain/response assertions. Its local claims cooperate to establish that contract; the remainder of the paper can discard their notation. The Legendre and selected-runtime proofs likewise have independently usable error/count statements. Thus allowing their internal shared locals does not evade the global memory constraint.

Norm and meaning checks also passed. Dense neuron norms in the selected comparison are declared to be divided by \(\sqrt n\) at selected 167–169; the metric norm is constructed in the selection statement, and selected parameter norms are displayed at 247–254. The dense and selected sample Grams are explicitly distinguished at 494–503. Different uses of \(\lambda,z,S,H,\mathcal K,q\) are newly bound inside their respective modules. The scope-limited exception allowing a fixed-problem constant in qualitative source-proof estimates is stated at foundations 478–481; that broader dependence is not exported as a headline constant.

## Independent mathematical-interface checks

1. **Dense-flow normalization and fitting rate.** Differentiating \(f_n=w^\top h^{(L)}/n\) gives parameter derivatives \(\delta^{(1)}v^\top/n\), \(\delta^{(j)}h^{(j-1)\top}/n\), and \(h^{(L)}/n\). Applying the stated mobilities gives exactly `compact.tex` 87–92. In the displayed mobility norm, the energy identity in fitting 150–166 and the Gram margin \(\mathsf H^\top\mathsf H/(mn)\succeq\gamma I/(4m)\) yield residual RMS decay \(e^{-\gamma t/(2m)}\), with the stated factors. The parameter-tail and output-tail interfaces do not exchange this norm with an unnormalized parameter norm.

2. **Legendre moments, clock and defect.** The moments are unnormalized integrals, not projection coefficients. Orthogonality gives coefficients \((2j+1)/\tau\), matching the reconstruction at Legendre 134–136. Differentiation of \(P_j(2\xi/\tau-1)\) produces the displayed \(j\) and \(2i+1\) mixing terms. The forward write is \(\widehat\rho\widehat h\), while the backward write is \(\widehat r_a\widehat\delta_a\); their distinction is preserved. Polarization of the growing-interval projection-error identity gives the positive defect \(2\widehat\rho\sum_a e_{b,a}e_{h,a}^{\top}/(mn)\). Residual division occurs only in a proof history and is treated by stationary continuation; the stored-state ODE has no such division. The exact moving count is \(n(d+1)+1+2(L-1)mnq\). Substituting the prescribed \(q\) into the final \(q^{-2}\) estimate gives \(CY/(\sqrt n[\log(en)]^3)\), including the cancellation of \(e^{\sqrt{\log(en)}}\).

3. **Exact selected metric.** Substitution into the displayed formula for \(M\) gives \(P^\top MP=I\); the middle matrix has eigenvalues of \(G^{-1}\) on the selected source range and one on its complement. Hence the stated comparison with \(D\) and the factor-two coordinate multiplication bound follow. This preserves the \(1/n\) neuron inner product rather than an unnormalized Gram.

4. **Corrected readout and cancellation.** With columns of \(V_C\) divided by \(\sqrt m\), the readout formula gives \(V_C^*\widehat w_C=(y-c_C)/\sqrt m\), hence exact training predictions \(y-c_C\). Defining the local deficit error \(e=(c_C-c_n)/\sqrt m\), the local correction \(p=T_Ce\), and \(\zeta=w_C-w_R+p\), one has \(T_CQ_C=V_C\). Therefore the \(-2T_CQ_Ce\) term cancels the raw-readout term \(2V_Ce\) exactly, as claimed at selected 510–521. Moreover \(\langle p,T_CQ_Ce\rangle=\|e\|^2\), confirming the dissipative term used next. This argument does not assume coordinate activation gates are self-adjoint in the selected metric; that qualification is explicit.

5. **Source-radius and panel interfaces.** The private sphere time radius reduces to \(a(\gamma/m)/(1024Y^2U\sqrt{\log(en)})\); the displayed bound on \(U\) gives the exported radius in canonical quantities. The query-radius comparison and four-family envelopes are likewise explicitly reduced at foundations 1492–1536. For the panel, the working bound \(40960(U_{\rm fin}/a)(Ym/\gamma)^2\sqrt{\log(en)}\) is converted to the public \(\beta^{30L}\) coefficient, and \(80\mathcal K\) to \(\beta^{16L}\), without deleting the label factor. The finite-panel construction uses the public disks and half-radius intervals, not a silently reused working domain.

6. **Initialized jets and paired images.** Direct substitution in the compiler map gives \(\mathfrak t(0)=0\) and \(\mathfrak t(\xi_*)=T\), while the disk maps inside the stated time rectangle. The continuation therefore uses origin derivatives. Applying initialized matrices to base coefficient vectors preserves pairing exactly; the norm-eight allowance controls the introduced image error. In the panel construction the normalized Taylor variable is \((t-t_b)/r_b\), and the coefficients \(r_b^ku^{(k)}(t_b)/k!\) have the stated bound. Geometric summation gives the claimed tail and coefficient-error constants. No trained parameter is needed as an input in this interface.

7. **Storage powers and dimension reduction.** The sphere calculation gives \(\alpha_T^{-1}=128\beta^{30L}(Ym/\gamma)^2\sqrt{d+3}[\log(en)]^{3/2}\). Combining this with the spatial radius and simplex count yields coefficient order \((Ym/\gamma)^2[\log(en)]^{3d/2+1}\), and squaring yields the headline \((Ym/\gamma)^4[\log(en)]^{3d+2}\). The factorial inequality supplies the stated dimension dependence. For the panel, squaring its panel count and multiplying by the squared Taylor order yields exactly the two displayed terms, including the factor \((Ym/\gamma)^4\). The map \(v\mapsto U_0^\top v\) preserves unit norms on the declared input span, and \(W^{(1)}U_0\) retains standard Gaussian row covariance. Thus the finite-panel reduction does not add a normalization or input-rank hypothesis.

8. **Actual dense variability and final probability statement.** At zero readout the exact derivative is \(2\sum_iU_{i,a}(U_i^\top y)/(mn)\). The two independent last-layer innovations give conditional variance factor \(8/m^2\), consistent with the stated lower bound. In derivative transfer the physical factor is \(2/r\); choosing radius \(m/(\gamma\sqrt{\log(en)})\) and order proportional to \(\log(en)\) gives the required \([\log(en)]^{-5/2}\) denominator. The final coefficient contains \(Y\sqrt\gamma\), with cancellation of the sample factor. The witness is explicitly a positive training time, not the fitted training endpoint. The assembly intersects events without requiring independence and lets the fixed confidence budget decrease only after taking the width limit. The declared failure convention is retained.

## Severity and confidence

| Category | Finding | Consequence |
|---|---|---|
| Fatal | None established | No foundational notation/interface failure found. |
| Major | None established | No repair requiring a changed theorem scope or substantial restructuring found. |
| Minor | None established | No concrete local repair is necessary for the assessed contract. |

Confidence is **high for the exact 29-symbol count and the absence of proof-private imports**, because every source line and every module boundary was read and the suspicious coefficient families were searched within the allowed corpus. Confidence is **high for the algebraic normalizations, cancellation, and count transformations listed above**. Confidence is **moderate for the complete technical stochastic proof as a whole**: it was read in full and checked for coherent scopes, premises and interfaces, but this audit did not separately rederive every cavity Taylor remainder, numerical ledger entry, or Gaussian-entropy estimate from scratch. No absent scientific input was needed for the narrower conclusions reported here.
