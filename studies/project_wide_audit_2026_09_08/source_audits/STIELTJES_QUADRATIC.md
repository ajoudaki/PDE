# Stieltjes / quadratic source-group audit

Date: 2026-09-08. Independent, read-only mathematical audit, except for this new report. No experiments, coefficient-generation runs, simulations, agents, task messages/resumption, commits, branch changes, or research-file edits were made. No other new source-auditor report was read.

## 1. Consolidation verdict

The defensible consolidation is **exact finite-order canonical compatibility together with several sharply scoped negative theorems**, not either “Stieltjes closure proved” or “all quadratic mean-field closures impossible.”

1. The canonical two-hidden-layer, one-sample, raw-square, unit-block-metric output sequence has retained exact derivatives through **17**, giving eight output moments and positive definite ordinary/shifted Hankel matrices through size four. It has no inspected order-19 output certificate. The ninth first-hidden moment comes instead from a Ward identity.
2. The uniform block-metric Stieltjes claim is false, including an interval with **every block trained**. The conventional shallow raw-square and two-hidden-layer raw-cubic extensions are also false. The partially quadratic QI model supplies a separate order-17 negative witness. None is a counterexample to the canonical QQ, unit-metric sequence.
3. The formal annealed feature jet has zero Taylor radius. This rules out its exact analytic realization with analytic readout and defeats the prescribed positive Taylor/positive-compiler approximation families. It does **not** rule out smooth nonanalytic ODEs, all signed resummations, all operator/IDE descriptions, or an actual positive-time neural limit.
4. The tagged-site DMFT argument is a valid **conditional cooperative comparison**. Its tagged law was not derived for this network. Its step trace additionally requires a relaxed-selection assumption. It does not establish instantaneous fitting of the network.
5. I read the entire 3,342-line covariant-Schur manuscript. Its stated theorem would rule out the frozen continuous-readout, compact-time-uniform canonical closure contract, even with infinite-dimensional fields. I do **not independently certify its adaptive probability/derivative bridge**: the response-multiplier and finite-word synthesis estimates require more justification at the stated norms. This is a specific unresolved proof obligation, not a counterexample to the claimed network theorem. Historical “PASS” labels are not substituted for that missing audit.
6. Generic-batch noncommutative Stieltjes closure was amended into an **incomplete formulation**, not an established theorem: the map from raw source-word jets to transformed noncommutative moments was not defined.

The named skills were read in full: solve-math-rigorously, investigate-conjectures, and the latter's evidence-ledger/adversarial-audit references. Their effect here was to separate formal identities, retained computation, conditional deductions, source assertions, and unaudited dependencies, and to test the strongest no-go claims against their actual assumptions.

## 2. Model and claim types

### Canonical object

Use H for the number of hidden layers and B for the number of training samples. Here H=2, B=1, equal hidden width n, no biases, both activations raw square, and independent standard Gaussian initial A,u,W. Write

\[
G=W/\sqrt n,\quad X=u^{\odot2},\quad Z=GX,\quad B_{\rm back}=A\odot Z,\quad
R_{\rm back}=G^\top B_{\rm back},\quad
f_n=\langle A,Z^{\odot2}\rangle_n,\quad
\langle v,w\rangle_n=n^{-1}v^\top w.
\]

Thus the output average is scaled by 1/n, not the lazy 1/sqrt(n) readout convention. Feature ascent is D_n=n grad(f_n)·grad in raw (A,u,W) coordinates. In (A,u,G) coordinates the vector metric is normalized L2 and the matrix metric is Frobenius:

\[
A'=Z^2,\quad u'=4uR_{\rm back},\quad
G'=2B_{\rm back}X^\top/n,
\]
\[
K_n=f_n'=\langle Z^4\rangle_n+
4\langle X^2\rangle_n\langle B_{\rm back}^2\rangle_n+
16\langle X R_{\rm back}^2\rangle_n\ge0.
\]

At initialization its limiting baseline is 27+36+48=111. This K is the **output learning-metric tangent kernel**, not a hidden covariance, backward kernel, or the retarded DMFT response. The formulas are exact finite-width identities. See the [canonical contract](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/PROOF_CONTRACT.md:9) and [finite equations](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:25).

For full squared loss L=(y_star-f_n)^2, physical gradient flow is

\[
\dot\theta=2\eta(y_\star-f_n)\theta',\qquad
\dot f_n=2\eta(y_\star-f_n)K_n,\qquad
\dot L=-4\eta K_nL.
\]

This is gradient flow with the stated metric, not SGD, momentum, Adam, or a fixed-step discrete-time theorem. The scalar feature clock is valid for B=1, or a separately proved invariant residual direction; it is not automatically valid for a rotating generic-batch residual.

The earlier quadratic-nonclosure convention uses phi(z)=z^2/2 and middle weights of variance gamma/n, with readout average 1/n, vector block rates n, and middle-weight block rate 1. If W_hist=sqrt(lambda/n) W_canonical, lambda=gamma, then

\[
f_{\rm hist}=(\lambda/8)f^\circ,\qquad
D_{\rm hist}=(\lambda D_a^\circ+\lambda D_u^\circ+D_W^\circ)/8.
\]

Consequently gamma=4/3 in that normalization is not the canonical raw-square unit metric; its initial feature speed is 17/6, not 111. Positive rate changes preserve the relevant zero-radius obstruction, but numerical coefficients must not be copied between these conventions. The [master normalization discussion](/home/amir/Codes/PDE/studies/quadratic_nonclosure/QUADRATIC_MUP_NONCLOSURE_MASTER_REPORT.md:249) was checked in scope.

### Formal moments versus a training curve

The primary definition holds k fixed before n tends to infinity:

\[
F^{(k)}(0)=\lim_{n\to\infty}\mathbb E[D_n^k f_n].
\]

These are annealed coefficients. They are not, by this definition, concentration in probability, derivatives of an identified limit, or an exchange of differentiation and a positive-time width limit. Readout sign reversal gives formal oddness. With S=F^{-1} the formal inverse, define

\[
K(y)=F'(S(y)),\qquad
\mathcal R(x)=\frac{K(\sqrt x)-111}{x}
=\sum_{r\ge0}(-1)^r\mu_r x^r.
\]

The relevant positive measure, if it exists, is a measure on nonnegative spectral values with
\(\mu_r=\int\lambda^r\,d\rho(\lambda)\), and its candidate resolvent is
\(\mathcal R_\rho(x)=\int(1+x\lambda)^{-1}d\rho(\lambda)\).

| Level | What must be proved | Audited canonical status |
|---|---|---|
| Finite jet | Fixed-order Gaussian/Wick computation | Retained exact jet through order 17 |
| Finite Hankel gates | PSD of the available matrices | All accessible output gates strictly PD |
| V1, all-order measure | Both H_d=(mu_(i+j)) and H_d^+=(mu_(i+j+1)) PSD for every d | Open in inspected sources |
| V2, determinacy | Uniqueness of the representing measure | Open; existence alone is insufficient |
| V3, identification | Independently constructed neural response equals the selected resolvent | Not established |
| Global fitting/nonlazy evolution | Positive-time/global existence, limit identification, endpoint convergence, and the claimed observable behavior | Not a consequence of these certificates |

The classical Stieltjes moment criterion applies to a real infinite sequence with all moments finite. It does not upgrade a finite positive prefix into positivity of the particular unknown continuation. The reciprocal-coordinate formulation using coefficients of 1/K is an equivalent Stieltjes formulation, not independent evidence. Equality of all derivatives is insufficient for positive-time identity in this zero-radius setting. These distinctions are explicitly locked in the [full proof contract](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/PROOF_CONTRACT.md:47).

## 3. Evidence ledger and certificate inventory

“Verified” below distinguishes direct proof checking from checking arithmetic on retained coefficient tables. No upstream coefficient generator was rerun.

| Claim / exact setup | Evidence and my disposition | Boundary |
|---|---|---|
| Canonical QQ, H=2, B=1, all blocks unit rate | Full finite-order derivation read; retained F through 17; downstream rational Hankel arithmetic checked | Eight output moments, not all orders |
| First hidden Q1=E[u^2], in output coordinate | Full companion derivation/results read; Ward Q1'=8F; nine moments | Not a backward kernel; ninth moment needs no F19 |
| Second hidden Q2=E[Z^2], in output coordinate | Full companion derivation/results read; eight moments | Separate observable, not implied solely by Q1 Ward identity |
| Block metric D_a+alpha D_u+beta D_W | Full negative proof and positive-alpha derivation read; explicit negative witness and interval signs checked | Refutes uniform metric claim, not alpha=beta=1 |
| Shallow raw square, H=1, B=1 | Full reduction, exact jet and characteristic proof read | Characteristic solvability does not imply population Stieltjes or global fitting |
| Raw cubic, H=2, B=1, all unit blocks | Full Gaussian-program derivation and results read; shifted 2x2 determinant recomputed exactly from displayed moments | Refutes activation-universal assertion |
| QI: inner square, outer identity, H=2 | Full closure manuscript and order-17 report read; negative shifted 4x4 determinant recomputed | Different architecture from QQ |
| IQ: inner identity, outer square | Same full manuscripts; retained eight-moment pass | Finite compatibility only; no all-order theorem |
| H=3 raw square | Full derivation and order-13 report read | Six moments; H2 and H2+ PD as retained computation |
| Raw/normalized sine, H=2 | Full two results manuscripts read | High-precision computed negative signs, not independently certified interval/sign proof here |
| Formal Taylor/positive-compiler no-go | Full decisive proofs read and checked | Formal annealed / specified compiler class |
| Tagged-site DMFT step argument | Full primary conditional proof read and checked | Tagged representation and network identification unproved |
| Canonical covariant-Schur initial layer | Full manuscript read; preliminary algebra and final conditional implication checked | Adaptive bridge not independently certified; Section 7 |

### Canonical 17 versus hidden 18 versus output 19

The [order-17 result](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/canonical_high_order/RESULTS.md:5) retains

\[
F^{(15)}(0)=49079184579077107476764629402991788032,
\]
\[
F^{(17)}(0)=30555969894096099495444855650521777374167040.
\]

F17 determines mu_0 through mu_7. Largest available output matrices are H3 and H3+, both 4x4. An ordinary H4 would require mu_8, hence F19; a shifted H4+ would require mu_9, hence F21. The retained branch explicitly stopped at 17.

For hidden observables put N_j(y)=Q_j(S(y)), with baselines Q1(0)=1 and Q2(0)=3. The audited companion transforms are

\[
\frac{N_j(\sqrt x)-Q_j(0)}x,\qquad
\frac{\sqrt{N_j(\sqrt x)/Q_j(0)}-1}x.
\]

They concern output coordinate x=y^2, not physical time. These are one-point preactivation norms; in particular Q1=E[u^2] is not E[X^2]=E[u^4], the first activated-feature squared norm. Neither companion is a sample-pair covariance or a two-time backward kernel. The finite-width identity Q1'=8f follows from homogeneity in u and yields

\[
Q_1^{(18)}(0)=8F^{(17)}(0)
=244447759152768795963558845204174218993336320.
\]

Thus both first-hidden companion sequences have nine moments, with H4 and H3+ available; both second-hidden sequences have eight, with H3 and H3+ available. All retained gates are strictly PD. Also
\(dN_1/dy=8y/K(y)\), so the first squared-norm companion is structurally tied to the reciprocal output kernel, rather than being an independent test of every layer. See [Ward identity and cutoff](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/canonical_hidden_high_order/RESULTS.md:43) and [actual definitions](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/canonical_hidden_high_order/RESULTS.md:5).

I independently checked the stored rational principal-minor entries using BigInt fraction arithmetic: output 52; first-hidden relative RMS 83; first-hidden squared RMS 83; second-hidden relative RMS 52; second-hidden squared RMS 52. Total **322 stored entries**, including repetition across nested matrices, not 322 independent tests. All agree and are positive. This checks the finite moment-to-Hankel step, not a fresh derivation of F17. Six hidden-audit source/result/protocol hash references also match the local files.

### Older compiler inventory, not additional new certifications

The [compiler README](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/README.md:35), read fully, inventories:

- Root canonical exact D1,D3,D5,D7,D9,D11, with separate connected/exhaustive/contraction routes; downstream canonical Gaussian programs later extend to 13/17.
- Campaign 1: D_a+lambda(D_u+D_W), output and hidden squared-RMS, finite 2x2 ordinary/shifted gates on lambda>=0.
- Campaign 2: B=2 equal-norm inputs in same/opposite-label invariant channels, order-seven ordinary 2x2 gates; Gram matrix retained in covariance and first-layer metric.
- Campaign 3: first activation u^2-c, 0<=c<=2, finite moment and ordinary 2x2 interval certificates.
- Campaign 4: independent alpha,beta, through order nine, mu_0..mu_3 and both 2x2 gates. Its low-order quadrant pass is compatible with the later order-13 negative shifted 3x3 gate.
- Campaign 5: B=3 equicorrelated equal-label invariant channel, exact order five and two moment signs only; no completed F7 or Hankel determinant.
- Campaign 6: bounded D13 threshold probe, protocol-inconclusive; no accepted new bound.

I did not fully audit the primary continuum proofs of Campaigns 1–5, the root D11 binary, or their arithmetic implementations. These entries are inventory/provenance, not new blanket endorsements. No B=4 or arbitrary-label/batch theorem follows.

## 4. Decisive exact Stieltjes counterexamples

### 4.1 Uniform block metric: verified negative theorem

At (alpha,beta)=(0,1), u is frozen, but A and W train. Let m_n=<u^4>_n. Conditional on u the rows reduce exactly to

\[
a'=z^2,\quad z'=2m_naz,\quad a(0)\sim N(0,1),\quad z(0)\sim N(0,m_n).
\]

For each fixed derivative order the conditional expectation is a polynomial multiple of m_n^(k+1). Gaussian moments give the needed uniform integrability and m_n tends to 3. Thus the limit is generated by
\(\mathcal X=z^2\partial_a+6az\partial_z\), applied to az^2. Its monomial recursion is

\[
\mathcal X(a^p z^q)=p a^{p-1}z^{q+2}+6q a^{p+1}z^q.
\]

This supplies a finite, exact, reproducible proof of the jet, rather than a fit to numerical trajectories. Formal inversion produces

\[
(\mu_0,\ldots,\mu_5)=
\left(
\frac{480}{49},\frac{43756}{151263},\frac{7214528}{200120949},
\frac{12545175968}{2402451992745},
\frac{171752915595136}{200241971143303005},
\frac{2199776554157960896}{14570607030242443158825}
\right).
\]

Its shifted determinant is

\[
\det H_2^+=
-\frac{86245462994269879146938487857152}
{200150589172828762588730609071155193161975}<0.
\]

For the monic polynomial

\[
p(t)=t^2-\frac{14165989123115588}{49896409440894219}t
+\frac{40042013405871059816}{2310453239160606810795},
\]

the moment functional gives

\[
\mathcal L[tp(t)^2]=
-\frac{673792679642733430835456936384}
{329714727520793070279653295504327135}<0.
\]

I recomputed both identities from the retained rational moments. A nonnegative measure cannot give a negative integral of t p(t)^2 on [0,infinity). Higher moments cannot repair this violation. See [full reduction](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/BLOCK_METRIC_RESOLUTION.md:89) and [negative form](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/BLOCK_METRIC_RESOLUTION.md:237).

Crucially, the negative result extends to **0<alpha<=1/100, beta=1**, so it is not only a frozen-block artifact. The [positive-alpha proof](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/POSITIVE_ALPHA_JET_DERIVATION.md:61) eliminates the trained middle matrix as a time integral, then proves the finite chronological Gaussian detransposition recurrence using Gaussian regression, Stein identities, quotienting null limiting covariance directions, and fixed-degree moment bounds. Forward and transpose uses retain their response terms; they are not treated as fresh independent matrices.

Exact inversion yields
\[
\Delta(\alpha)=\frac{55296P(\alpha)}{2358125(63+48\alpha)^{33}}.
\]
P has degree 36, negative constant/linear coefficients and strictly positive coefficients thereafter. Both P(0) and P(1/100) are negative. Strict convexity therefore puts P below its negative endpoint chord. I checked the stored coefficient signs and exact endpoint arithmetic. The denominator is positive.

The same polynomial has exactly one positive root by its single coefficient-sign variation and a sign-changing rational bracket. I verified
\[
17519225541486/10^{15}<\alpha_*<17519225541487/10^{15}.
\]
The full manuscript classifies the six-moment prefix as negative shifted determinant below alpha_*, singular at alpha_*, and both leading families PD above it. That is a **finite-prefix** transition, not the boundary of an all-order Stieltjes phase. The unit canonical metric alpha=beta=1 is not refuted.

### 4.2 Shallow raw square: verified reduction and limitation

For H=1, f_n=n^-1 sum a_i v_i^2 with independent unit Gaussian a_i,v_i and both vector blocks trained, the characteristic equations are
\[
a'=v^2,\qquad v'=2av.
\]
The multiplier-m population jet obeys F_m(s)=m F_1(ms); hence
\[
K_m(y)=m^2K_1(y/m),\quad \mathcal R_m(x)=\mathcal R_1(x/m^2),\quad
\mu_r^{(m)}=m^{-2r}\mu_r^{(1)}.
\]
The preceding m=3 boundary therefore transfers its negative shifted 3x3 determinant to the conventional shallow model, whose K0=7. This is a genuine shallow counterexample, not canonical H=2 QQ.

The full characteristic solution is also elementary: c=a0^2-v0^2/2 is invariant; D''=4cD, D(0)=1, D'(0)=-2a0; a=-D'/(2D), v=v0/D. It gives exact finite-neuron dynamics before the first pole and a transport description. For every fixed s>0, the unbounded Gaussian initialization has positive mass of characteristics that pole before s. Near relevant pole surfaces the cubic readout is not ordinarily integrable. One cannot average these formulas and declare a classical global Gaussian population solution without specifying a justified continuation. Compactly supported initialization before a common first pole is a different, valid local statement. See [full shallow proof](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/SHALLOW_QUADRATIC_REDUCTION.md:17), [characteristics](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/SHALLOW_QUADRATIC_REDUCTION.md:239), and [population obstruction](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/SHALLOW_QUADRATIC_REDUCTION.md:339).

### 4.3 Architecture survey: which counterexample says what

The raw-cubic H=2, B=1, iid Gaussian, all-unit-block recurrence has K0=305775. Its four order-nine moments are positive, but
\[
\det H_1^+=
-\frac{3136318387543181669964663532850762952758515589}
{36859700346470723980544924489290665938162841796875000}<0.
\]
The explicit witness is p(t)=t-mu_2/mu_1. I read the full [primary recurrence derivation](/home/amir/Codes/PDE/studies/mean_field_peeling/cubic_compiler/depth2_gaussian_program/DERIVATION.md:1) and [exact moment report](/home/amir/Codes/PDE/studies/mean_field_peeling/cubic_compiler/depth2_gaussian_program/STIELTJES_RESULTS.md:28), and independently recomputed that determinant from the four displayed rational moments. The coefficient-generation code itself was not audited end to end or rerun. This exact finite-order computation refutes “every smooth activation has this Stieltjes output transform”; cubic is smooth.

For QI, K0=10, the retained order-17 moment table gives
\[
\det H_3^+=
-\frac{12717014161759221378928329747546434159184880978088665219012521749}
{1006179463097402343750000000000000000000000000000000000000000000000}<0.
\]
I recomputed it from the eight displayed rational moments. IQ, K0=11, passes its retained eight-moment gates; canonical QQ, K0=111, is again a third model. The [full partially quadratic proof](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/autonomous_single_source_closure/THEOREM_AND_AUDIT.md:27) and [order-17 table](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/autonomous_single_source_closure/PARTIAL_ORDER17_RESULTS.md:8) do not identify positive-time width limits. The QI/IQ order-17 implementation was not independently rederived in this audit.

The H=3 raw-square program has a retained six-moment pass through F13, K0=14175, not a negative result and not an all-order theorem. The sine reports exhibit negative first moments and negative higher gates at high precision; I read both reports, but not a rigorous enclosure proof for their transcendental arithmetic. Their signs should be described here as retained high-precision computational evidence, not promoted into a newly independently certified exact theorem. No identity-activation all-order spectral manuscript was read fully; the historical “forty moments/order 81” identity claim is not a quadratic order-19 certificate.

## 5. Zero radius and the actual negative closure statements

### 5.1 All-order formal divergence: checked proof

The complete [approximate-source negative proof](/home/amir/Codes/PDE/studies/quadratic_nonclosure/approximate_single_source_conjecture_resolution.md:280) and [adversarial source](/home/amir/Codes/PDE/studies/quadratic_nonclosure/adversarial_audit_report.md:127) were read in full. The core argument is coefficientwise positivity, a retained scalar branch, and Gaussian factorial moments.

In canonical normalization, retain the frozen-u branch of Section 4.1. For odd k=2r+1, the polynomial P_k=(X^k(az^2))/k! contains only monomials a^(2p)z^(2q), p+q=r+2, with nonnegative coefficients. On z=sqrt(6)a, a0=1,
\[
az^2=6(1-6s)^{-3},\qquad
P_k(1,\sqrt6)=6^{k+1}\binom{k+2}{2}.
\]
For independent A~N(0,1), Z~N(0,3), m=p+q,
\[
\mathbb E[A^{2p}Z^{2q}]/6^q
=(2p-1)!!(2q-1)!!2^{-q}\ge m!/4^m.
\]
The full canonical primitive vector field has nonnegative polynomial coefficients. Removing its u-update histories removes only nonnegative Wick contributions, so cancellation cannot invalidate the retained lower bound. Thus if F(s)=sum a_r s^(2r+1),
\[
a_r\ge \frac{9^{r+1}}4(r+2)!\binom{2r+3}{2}.
\]
Its (2r+1)-st root diverges. The historical half-square proof gives the corresponding positive-rate bound with q0=3/4 and b_gamma=(1/2)min(1,gamma/2); the change of normalization does not turn that formal theorem into a trajectory theorem.

This proves zero radius of the formal feature series. The feature-loss odd coefficients are -2a_r. For physical time with eta absorbed and label 1, put p(t)=-s(-t); then
\[
p'=2(1+F(p)),\quad p(0)=0,\quad p\succeq_{\rm coef}2t.
\]
Since L_phys(-t)=(1+F(p(t)))^2, its coefficient at t^(2r+1) is at least 2^(2r+2)a_r. The physical-loss **formal jet** also has zero radius. The full short composition proof was checked in the [current-state amendment](/home/amir/Codes/PDE/studies/stieltjes_conjecture/CURRENT_RESEARCH_STATE.md:2397).

Correct implication: an analytic vector field with analytic readout, in a setting where the analytic ODE theorem applies, cannot exactly realize this jet at initialization. Incorrect implication: no smooth finite-dimensional ODE can realize it. Smooth functions may have divergent Taylor series and nonzero flat differences; smoothness is not analyticity.

There is no conflict between zero radius and a possible all-order Stieltjes measure. Such a measure would have to have unbounded support: compact support makes R and K analytic near zero and hence the local scalar equation F'=K(F) analytic, a contradiction. With all moments finite, an unbounded-support resolvent can still be smooth at x=0 from the right. Neither its existence nor neural identification follows from this observation.

### 5.2 Prescribed Taylor closures: a genuine internal no-go

Let F_M be the initialization Taylor truncations with their nonnegative limiting coefficients, and couple them to the residual clock. For every s>0, F_M(s) tends to infinity. For each 0<y<1 the positive root r_M(y) of F_M(r)=y tends to zero, and its physical hitting time obeys
\[
t_M(y)\le r_M(y)/(2(1-y)).
\]
Their continuous loss curves consequently converge pointwise to the step equal to 1 at zero and 0 at every positive time. They are not uniformly Cauchy on any interval containing zero. This is a statement about the **surrogate sequence**, not the network loss.

The prescribed iterated approximation claim
\[
\lim_{M\to\infty}\limsup_{n\to\infty}
\mathbb E\,d_T(L_M,L_n)=0
\]
is impossible for the bounded uniform path metric: the triangle inequality would make the deterministic L_M uniformly Cauchy. No identified network limit is needed for this contradiction. The proof does not address a coupled diagonal M=M(n), arbitrary signed/rational approximants, or convergence on intervals bounded away from initialization. See [the exact quantifiers](/home/amir/Codes/PDE/studies/quadratic_nonclosure/approximate_single_source_conjecture_resolution.md:511).

The stronger positive-compiler statement similarly needs its positivity assumptions. If each fixed coefficient converges to the positive divergent formal coefficient, every positive-time polynomial evaluation diverges. For the symbolic explicit-Euler pullback, selecting k first-order insertions gives the nonnegative contribution tau^k (N)_k/N^k c_k. First fix k, then refine N. This does not say that ordinary finite-n integration fails. The positive-semigroup obstruction requires a cone-preserving semigroup, all D^k f in generator domains, and a continuous positive Wick readout. Its Taylor remainder is then nonnegative and forces an infinite readout. Signed dynamics, altered domains, or discontinuous/renormalized observables escape that particular argument. See [positive semigroup and compiler proofs](/home/amir/Codes/PDE/studies/quadratic_nonclosure/adversarial_audit_report.md:508).

### 5.3 Topology and finite encoding

The L2 spike example a_R=z_R=R 1_E, P(E)=R^-3 has both L2 norms tending to zero while E[a_R z_R^2]=1. It disproves continuity of that cubic readout on the unrestricted ambient L2 space. It is not a reached-state example for the canonical dynamics.

A Banach function algebra continuously embedded in L1 with bounded ordinary multiplication forces
\(\|x^m\|_1\le C_1C_2^{m-1}\|x\|_X^m\), hence \(\|x\|_\infty\le C_2\|x\|_X\). Such a single algebra cannot contain an unbounded Gaussian coordinate. Scale spaces, restricted reachable sets, or other products are not excluded. These short proofs are fully present in the [adversarial manuscript](/home/amir/Codes/PDE/studies/quadratic_nonclosure/adversarial_audit_report.md:419).

The project's noncommutative continuation/encoding no-go additionally assumes freeness/faithfulness and branch separation. I checked that qualification in the master and historical amendment, but did not fully read its separate primary encoding proof; it is **not independently certified here** and must not become canonical-path nonexistence. Likewise, this audit does not promote frozen normalized-monomial-cutoff non-invariance into full normalized-system proliferation.

The partially quadratic manuscript gives useful finite-width matrix/invariant reductions but also an eigenvalues-only obstruction: with X=(1,2,3), two compatible orientations have the same retained spectrum/output but different weighted contractions <X r^2> (1/3 versus 7/9). A conserved spectral object alone therefore does not close that readout speed. This is not a proof against every Lax or operator formulation. See [the explicit orientation counterexample](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/autonomous_single_source_closure/THEOREM_AND_AUDIT.md:95).

## 6. Tagged-site DMFT: conditional theorem, not canonical fitting

The [entire amended primary manuscript](/home/amir/Codes/PDE/studies/quadratic_nonclosure/mean_field_single_source_conjecture_audited_resolution.md:1) was read. Its assumed effective law is
\[
z(t)=\xi(t)+\int_0^t r(s)M(t,s)a(s)z(s)\,ds,\qquad
a'=rz^2,
\]
with a0~N(0,1) independent of the **entire** continuous nondegenerate Gaussian process xi; deterministic causal continuous M with positive initial value; self-consistent f(0)=0; and
\[
f'=2(1-f)\kappa,\qquad \kappa\ge\mathbb E[z^4]/4.
\]
The finite-width initial diagonal calculation M(0,0)=3/2+2gamma is a consistency check, not a derivation of that positive-time process.

If output remains below a fixed subtarget level, r>=c>0. Continuity of M gives M>=m>0 on a small triangle. Independence gives positive probability of the joint event a0>=A and xi(t)>=z_star>0 on a short interval. On it the cooperative comparison
\[
b'=cv^2,\quad v'=cm\,bv,\quad b(0)=A,\quad v(0)=z_\star
\]
is a lower solution. Its invariant is v^2-z_star^2=m(b^2-A^2), and for large A its blow-up time is
\[
T_A=\frac1{2cm\alpha}\log\frac{A+\alpha}{A-\alpha},
\quad \alpha^2=A^2-z_\star^2/m,\quad T_A=O(\log A/A).
\]
The integral of v^4 diverges at that pole. Any fixed positive event probability therefore contradicts the assumed finite subtarget drift budget. No continuous-at-zero classical output can satisfy all these stipulated equations.

The discontinuous fitting trace requires a further monotone/no-overshoot relaxed-selection rule. No such solution or network limit is constructed. A continuous surrogate has uniform error at least 1/2 against the stipulated 1-to-0 step, or at least 1 if initialized at 1. That elementary approximation lower bound does not identify the network's target trace.

The manuscript cites Bordelon–Pehlevan 2205.09653 as general DMFT precedent. **I did not read that external primary theorem/proof in this audit and do not certify its application.** More importantly, the project itself supplies no specialization establishing this law's covariance, independence, complete response channels, self-consistency, well-posedness, or neural identification. None of the conditional comparison above needs that external citation. Root's broad literature survey cannot replace these model-specific missing deductions. See [explicit assumptions and disclaimer](/home/amir/Codes/PDE/studies/quadratic_nonclosure/mean_field_single_source_conjecture_audited_resolution.md:158).

## 7. Canonical covariant-Schur no-go: full read, unresolved certification

### Stated theorem and what it would imply

The [3,342-line manuscript](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:51) claims, for the exact canonical iid sequence, a fixed predictor gain delta0>0 by feature time at most (0.09+o(1))/sqrt(log n), with probability tending to one. For fixed y_star>0 and eta>=eta0>0, choose delta0<y_star/4; the corresponding physical time tends to zero.

If established, this implies failure of convergence in probability uniformly on [0,T] to **any continuous output readout**: at the random hitting time t_n,
\[
\delta_0\le2\|f_n-F\|_{\infty,[0,T]}+|F(t_n)-F(0)|\to0
\]
would be a contradiction. The [frozen contract](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/FROZEN_CONJECTURE.md:64) explicitly allows a fixed finite number of infinite-dimensional fields. Therefore this implication is stronger than a finite-number-of-moments no-go, but weaker than “no canonical limit in any topology” or “the full network loss is the instantaneous-fitting step.”

### Decisive proof skeleton

The exact column decomposition x=X_j, g=G_(.j), z=Z-xg gives h=g^T D_A g, rho=g^T D_A z, R_j=hx+rho, x'=8x(hx+rho). The manuscript derives the positive principal source in rho', the row equations, and an exact endpoint identity removing a dangerous derivative. These are useful exact algebraic statements.

With L=sqrt(log n), tau=Ls, x=L^2 U, H=Lh, P=rho/L, the outer system is
\[
U_\tau=8U(HU+P),\quad H_\tau=3,\quad P_\tau=26U.
\]
Candidate columns have rate a/2+b^2/6. The competing row system has alpha_tau=zeta^2, zeta_tau=14alpha zeta. A retained outward-rounded fixed-point C certificate brackets the relevant column minimum between 0.08389 and 0.0839 and places row poles after 0.11. I read all 239 lines of that C source, including interval monotonicity, outward arithmetic, overflow checks, parameter enclosure and tail bound; I did **not** compile or execute it. Its actual SHA matches the frozen source hash.

The proof then needs a quenched adaptive bridge: row-resummed bath estimates, exact one-column local resolvents, reciprocal-level rather than fixed-time derivatives, multi-layer mixed-source synthesis, and a common-source Schur contraction. It uses exact clocks, a coarea/spacing argument and reinsertion bounds to isolate a leading column up to x=n^(1/3). The terminal comparison promotes it to x of order sqrt(nL); the kernel inequality converts that growth into fixed output gain. The terminal argument is conditional on the pre-cap good event and is not a replacement for proving that event.

### Specific unresolved estimate

The issue is not whether normalized L2 is an algebra—the final text correctly acknowledges it is not. It supplies a special sharp **difference-score multiplier** lemma and then a derivative-closed finite-word synthesis lemma. The decisive coupled estimates are asserted from conditional Gaussian concentration and “the exact local equations” at [equation (4.12w7g')](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:1298). The later synthesis catalogue includes every slot derivative of order r=0,1,2, score order k=0,1 with r+k<=2, allowing common responses, one-star response differences and fresh-fiber responses. See [catalogue and proof](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:2336).

I cannot verify from the supplied proof that all these differentiated, adaptively selected coefficients have the required dimension-uniform Lipschitz/mean bounds before the event they are used to establish. In particular, the assertion that every conditional mean is a regression/self-return term with the smaller layer density is not accompanied by a complete estimate for the nonlinear local-solution-map catalogue. One-/two-fiber deletion and a Gaussian concentration theorem do not by themselves establish this mean bound.

A concrete norm stress explains why this is a substantive obligation. On a positive-density bounded core layer J, take a bounded row i and a matrix tangent
\[
M=e_iX_J^\top/\|X_J\|_2,\qquad a=v=0.
\]
Its Frobenius norm and the seven-component normalized graph tangent norm at a bounded core are O(1), up to the stated layer factors. But MX has a single coordinate of order sqrt(n), and
\[
D^2F_A[(0,0,M),(0,0,M)]=2(MX)^{\odot2}
\]
has normalized L2 norm of order sqrt(n), not a polylogarithmic bound. The [source norms](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:1001) alone therefore do not justify two arbitrary tangent multiplications.

This example does **not** refute the special reached difference-score lemma, nor does it show the canonical path violates the claimed theorem. The manuscript explicitly tries to restrict the dangerous products to one special sharp direction, for example in [the arbitrary-source linear response argument](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:2080). However, the broader r=2 catalogue must either be restricted to exactly those directions or be given an additional reachable-source/delocalization proof. The displayed L2 mapping table is not that proof.

Accordingly my disposition is **full primary read; preliminary identities and conditional consequence checked; adaptive bridge unclosed in this audit**. Do not consolidate its header as an independently verified canonical nonexistence theorem on my authority. Conversely, do not conflate this uncertainty with the already proved formal Taylor no-go or the explicitly conditional DMFT comparison.

## 8. Generalized Stieltjes and experiments: corrected reading

For arbitrary observables U(theta), metric M, batch residual r and full mean squared loss,
\[
\dot U=(2\eta/B)J_U M J_f^\top r,\quad
\Theta=J_f M J_f^\top\succeq0,\quad
\dot L=-(4\eta/B^2)r^\top\Theta r.
\]
These are exact projected-gradient identities. The observable mobility Gamma=J_U M J_U^T is PSD but generally is not determined by U alone. Neither identity supplies a closed observable ODE, a Stieltjes measure, or an optimal-transport structure.

For generic noncommuting sample fields, raw words D_w U are not yet transformed Stieltjes moments. The August-18 amendment explicitly withdraws the completeness of the earlier word-moment proposal: no unique output/source coordinate, mixed-word alternating-sign convention, directional restriction theorem, finite-order transform, multivariate resolvent, or feedback reconstruction had been defined. Even hypothetical positive word matrices would still require self-adjoint-domain, determinacy, approximation and neural-identification work.

The numerical summary in CURRENT_RESEARCH_STATE was inspected in scope, not its entire experiment archive. It distinguishes solvable-proxy calibration, protocol-inconclusive canonical pilots, failed FP32 update/rounding gates, qualified FP64 local successors, and a later 4096/8192 comparison without established strict successive-order improvement or resolved width trend. Those are not proof of canonical global proxy accuracy. I ran no experiment and do not re-certify their empirical protocols.

## 9. Supersession and task provenance

Local repository snapshot: HEAD 6300e9211ddb797029acae15fbff57bcd2344618. This is only repository provenance; actual audited file bytes are bound by Section 10 hashes. Uncommitted or copied research documents must not be identified with a remote-host version merely because their paths match.

The five PDE histories were located using the local session index and inspected by targeted older-turn extraction, not read in full. Important amendments were checked against current primary sources:

| Task | Located history / decisive historical amendment |
|---|---|
| PDE #13, 01a01b9c-013f-7e81-9f34-0579642ff124 | [Raw-cubic negative gate, August 20](/home/amir/.codex/sessions/2026/08/19/rollout-2026-08-19T22-00-03-01a01b9c-013f-7e81-9f34-0579642ff124.jsonl:1792); [later identity versus quadratic distinction](/home/amir/.codex/sessions/2026/08/19/rollout-2026-08-19T22-00-03-01a01b9c-013f-7e81-9f34-0579642ff124.jsonl:5714) |
| PDE #14, 019fd269-7862-7d03-a0d6-2cde7686de5d | [August 9 acknowledgement that tagged DMFT was not derived](/home/amir/.codex/sessions/2026/08/05/rollout-2026-08-05T16-52-35-019fd269-7862-7d03-a0d6-2cde7686de5d.jsonl:1499); [August 19 source-wide scope corrections](/home/amir/.codex/sessions/2026/08/05/rollout-2026-08-05T16-52-35-019fd269-7862-7d03-a0d6-2cde7686de5d.jsonl:3349) |
| PDE #15, 019ffb5f-fce5-7543-9f03-989ab3d18cd0 | [Earlier generalized proposal](/home/amir/.codex/sessions/2026/08/13/rollout-2026-08-13T15-46-39-019ffb5f-fce5-7543-9f03-989ab3d18cd0.jsonl:20727) superseded in scope by [August 18 noncommutative formulation gap](/home/amir/.codex/sessions/2026/08/13/rollout-2026-08-13T15-46-39-019ffb5f-fce5-7543-9f03-989ab3d18cd0.jsonl:21199) |
| PDE #16, 019fe763-6d7f-75d2-946c-d0faab6ff38c | [Older five-moment snapshot](/home/amir/.codex/sessions/2026/08/09/rollout-2026-08-09T18-38-00-019fe763-6d7f-75d2-946c-d0faab6ff38c.jsonl:30342), superseded for coefficient scope by the August-18 exact F13–F17 files; scoped numerical-method amendments were also located |
| PDE #9, 01a02086-3a46-77f2-9409-e596ced2f051 | [August 22 retraction of full inserted-tag Hessian estimate](/home/amir/.codex/sessions/2026/08/20/rollout-2026-08-20T20-54-22-01a02086-3a46-77f2-9409-e596ced2f051.jsonl:23742); [later difference-jet repair](/home/amir/.codex/sessions/2026/08/20/rollout-2026-08-20T20-54-22-01a02086-3a46-77f2-9409-e596ced2f051.jsonl:28743). Older coefficient-29, fixed-time pole-spacing and full-state susceptibility arguments were also located as superseded, not accepted proofs |
| PDE-2 #19, 01a01598-b22b-7663-a7c2-2fdcb57971c9 | Confirmed read-only SQLite record; remote history unavailable in this audit |

For #19 the user-specified host is remote-ssh-discovered:black-chatgpt-2. A mode=ro query of /home/codex-b/.codex/state_5.sqlite returned name/title “Stieltjes Program — High-Order Moments and Counterexamples,” cwd /home/amir/Codes/PDE, git_sha c3b28358fa113c5180eb9bfbcf74116bc629b900, and private rollout path /home/codex-b/.codex/sessions/2026/08/18/rollout-2026-08-18T17-58-43-01a01598-b22b-7663-a7c2-2fdcb57971c9.jsonl. Its thread_artifacts query returned no records.

No callable app task-reading tool was exposed in this audit's tool catalog. I did not access the private rollout or change permissions. No recovered source export positively tied to that remote task/version was located. Therefore #19 is **identified but not history-audited**. Local high-order manuscripts support the qualified repository conclusions above, not an assertion about every amendment in that private task.

The #9 manuscript's header records a historical “mathematical body” hash be9d0d95d12bd20f55429c1d57bcf431b7cfcd27885a447ed361a6a4f1587f37. The complete current file has the separately computed hash below; these hash domains must not be silently equated. Forked rollout timestamps can also reflect inherited content rather than the original event; the cited amendment texts and current source content, not final-message recency alone, determine supersession.

## 10. What I read and byte-level evidence

F = full file read, including proof; S = scoped inspection; C = structured certificate inspection/arithmetic checking. Line counts are newline counts. All links resolve to the local snapshot, not to remote-host bytes.

| File | Read | Lines | SHA-256 |
|---|---:|---:|---|
| [PROOF_CONTRACT](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/PROOF_CONTRACT.md:1) | F | 196 | cd9d2b33eb284199011914cbb729e6dc2c45b9d84f45865fe740e79a7b28baf6 |
| [BLOCK_METRIC_RESOLUTION](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/BLOCK_METRIC_RESOLUTION.md:1) | F | 472 | f806171d43764351dbb4e11d7e68289777ea5c54c6541895402e926e80f7e459 |
| [POSITIVE_ALPHA_JET_DERIVATION](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/POSITIVE_ALPHA_JET_DERIVATION.md:1) | F | 387 | a6107b798bea3e1cf4331bafbbc1163a56996abdf5ef5cca4dff1adf833db9a2 |
| [SHALLOW_QUADRATIC_REDUCTION](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/SHALLOW_QUADRATIC_REDUCTION.md:1) | F | 391 | 062345d6d101b782e768f317be319a3f332ee3b6fae3eb979db607232f26ed56 |
| [Approximate single-source resolution](/home/amir/Codes/PDE/studies/quadratic_nonclosure/approximate_single_source_conjecture_resolution.md:1) | F | 838 | fa58d9683eca82395df58aa0ecc1dc5187e9adb197138535a599f1abf259fe6b |
| [Adversarial audit, with proofs](/home/amir/Codes/PDE/studies/quadratic_nonclosure/adversarial_audit_report.md:1) | F | 806 | 51d2c7ed76f7625ca00d93d55715356e111e597e4c82fbb28a2743ccbd1afa72 |
| [Conditional tagged-site resolution](/home/amir/Codes/PDE/studies/quadratic_nonclosure/mean_field_single_source_conjecture_audited_resolution.md:1) | F | 734 | 42e43d24915cb824521df614f0035646c9b8ad0c85a1f91247dd6ccedefeab9a |
| [COVARIANT_SCHUR](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/CANONICAL_CONCENTRATION_NO_GO_COVARIANT_SCHUR.md:1) | F | 3342 | a1eb606ab73a34476ac5ab8f848c25db681c662d655ac6a90f8099eb5ef24c1c |
| [FROZEN_CONJECTURE](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/FROZEN_CONJECTURE.md:1) | F | 114 | 7216f09f09ee71f3d4e080b07ddd8cfc8005c19737a23bfb4bb009c93c0b2452 |
| [Outer pole C certificate](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/operator_ide_resolution/outer_pole_certificate.c:1) | F, not run | 239 | f191d9720196e9300b7771a4b9aca4e65340cf3f2399e44d60493ccf062026d1 |
| [Quadratic compiler README](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/README.md:1) | F | 199 | 7cfb6689d09339c39d70ae1aec17a9ac550e5a026bbb50f20526dc63d2733aab |
| [Autonomous closure THEOREM_AND_AUDIT](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/autonomous_single_source_closure/THEOREM_AND_AUDIT.md:1) | F | 325 | 0a7c7313a447b3f7f5345b5901f189ff6133d22401a4bb6c3f7bad87242e42e0 |
| [PARTIAL_ORDER17_RESULTS](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/autonomous_single_source_closure/PARTIAL_ORDER17_RESULTS.md:1) | F | 117 | 6c01d091fac00f679758d9ae34a857b7a4da3e83d9b6a5d11327a1a3765ee225 |
| [Canonical high-order NOTES](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/canonical_high_order/NOTES.md:1) | F | 259 | 48d3eaedace0a951ca10b15478425a2e3c997b787c81dac5c227c47d1b255150 |
| [Canonical high-order RESULTS](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/canonical_high_order/RESULTS.md:1) | F | 123 | 710acc329da6dd543c56c8fb17e3519ac25fd9e81b6b163f3371a650469800f9 |
| [Canonical hidden RESULTS](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/canonical_hidden_high_order/RESULTS.md:1) | F | 145 | d3f33f4d0297a2fd32338a8ae21b0538f28f3b7d2d73df63198cb7a4d5b68618 |
| [Hidden PRODUCTION_CONTRACTION](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/canonical_hidden_high_order/PRODUCTION_CONTRACTION.md:1) | F | 69 | 73c01b0867b0dff006144c5bb7f8589ba7250d60076a2db82ea02656f19eec10 |
| [Cubic DERIVATION](/home/amir/Codes/PDE/studies/mean_field_peeling/cubic_compiler/depth2_gaussian_program/DERIVATION.md:1) | F | 199 | dae32d2548af863ed46e935c5b3e0a5399153f8c0dd64a12e458de60db7a8bac |
| [Cubic STIELTJES_RESULTS](/home/amir/Codes/PDE/studies/mean_field_peeling/cubic_compiler/depth2_gaussian_program/STIELTJES_RESULTS.md:1) | F | 180 | 8fbd439577796074893deffecb1fd68406e911b8f7394848a6edacfe6e9fb610 |
| [H3 quadratic DERIVATION](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/depth3_gaussian_program/DERIVATION.md:1) | F | 211 | 69dd9fddaec51b6ec228b17952cfef8a0deb1e995f17f8df192035cc562b552a |
| [H3 ORDER13_STIELTJES_RESULTS](/home/amir/Codes/PDE/studies/mean_field_peeling/quadratic_compiler/depth3_gaussian_program/ORDER13_STIELTJES_RESULTS.md:1) | F | 149 | ee71b593560361f15b1794cdd97f84a186056c301ae5f03fe3dc21057465fdcc |
| [Sine RESULTS](/home/amir/Codes/PDE/studies/mean_field_peeling/sine_compiler/depth2_gaussian_program/RESULTS.md:1) | F | 86 | 255414aba0ed4d7ccd932cb897433d0d39a8b3fa05f96d699207ad1f2f60f83a |
| [Sine ORDER9_RESULTS](/home/amir/Codes/PDE/studies/mean_field_peeling/sine_compiler/depth2_gaussian_program/ORDER9_RESULTS.md:1) | F | 152 | d95a659656857c412d9677a71a86525ff7b8a53ae8427b4a41bf0a3d6f3f453c |
| [Stieltjes CURRENT_RESEARCH_STATE](/home/amir/Codes/PDE/studies/stieltjes_conjecture/CURRENT_RESEARCH_STATE.md:1) | S | 2821 | 909732206d7cc0ffbda455a1aec4219efea64925400293fbccbabfe64d2a7882 |
| [Quadratic NONCLOSURE_MASTER_REPORT](/home/amir/Codes/PDE/studies/quadratic_nonclosure/QUADRATIC_MUP_NONCLOSURE_MASTER_REPORT.md:1) | S | 2982 | 445eb14f26e0011cab632f9e595b243e0af2f61a2c2f4119d61a0237f338a328 |
| [BLOCK_METRIC_COUNTEREXAMPLE.json](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/BLOCK_METRIC_COUNTEREXAMPLE.json:1) | C | 65 | 30f01203422f989924ffe32e5c84f3e7f40129dc9aac2f9e23c980958f27a447 |
| [ALPHA_INTERVAL_CERTIFICATE.json](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/ALPHA_INTERVAL_CERTIFICATE.json:1) | C | 140 | ec8f441d79e5493718baa45fa773a011b18b6a1ff20bd87f866b94694e1237fd |
| [F17_MOMENT_HANKEL_AUDIT.json](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/canonical_high_order/F17_MOMENT_HANKEL_AUDIT.json:1) | C | 245 | 1cf1684bf7d2bac2732348add4cd6f229aa7081c6ad0707e5fc3b0c438815fab |
| [HIDDEN_MOMENT_HANKEL_AUDIT.json](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/canonical_hidden_high_order/HIDDEN_MOMENT_HANKEL_AUDIT.json:1) | C | 1545 | 53b17ed96c8b5aa791a4e94b2e224c8fafbfa19525a58d0b0a9f2b53bf21dd85 |

Scoped current-state reads covered the opening claim ledger/model, principal resolution sections, canonical/hidden high-order amendments, and zero-radius section; specifically lines 1–205, 398–540, 1198–1320, 1406–1508, 2397–2473 plus heading searches. The master report was scoped to opening status/model, normalization and amendment searches, not read fully. The old operator round registry was used only as provenance. Old “FINAL”/repair manuscripts and every historical referee report were not read in full; no theorem is accepted here merely because one was marked PASS.

Canonical retained result files inspected structurally:

- [PRODUCTION_RESULT.json](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/canonical_high_order/PRODUCTION_RESULT.json:1): eadea98387abb473a4eef7c7ea1300b9b65b4d28217db8201b92722840052f4c.
- [INDEPENDENT_RESULT.json](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/canonical_high_order/INDEPENDENT_RESULT.json:1): 3eeae3509a141f9d36d2f0b3fdae6134073eb8d08c52b2446d3bdd66b7e4ea6e.
- Generator import/function inventories were scoped, not full code audits: [production](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/canonical_high_order/production_canonical_recurrence.py:345), bccec0577ffd205d5625d8e6e1d9c4dba7dab8a7a218edd5a58866ea8606d688; [independent](/home/amir/Codes/PDE/studies/stieltjes_conjecture/resolution_program/canonical_high_order/independent_canonical_recurrence.py:267), 8c0aa4f49b7920c739b385664743a678db7a12f5160baee38a1b40acab2274ea. Separate implementations are evidence against coding mistakes, not independent proofs of the shared Gaussian reduction.

History file hashes for the line-linked rollouts in Section 9:

| Source | SHA-256 |
|---|---|
| PDE #13 local rollout | 662bf4f08c5d20f0c20a3fe893fe4c69cca135b135f7e812528b7c35a22a9904 |
| PDE #14 local rollout | 52e9f2dd836e1d45323a0c7ecd70b8dd2f9ad1bad1eb1ce2fb206c878c5a0081 |
| PDE #15 local rollout | dc4218e54b001e225e1c006772af18b8d122b9f4989f3cc0c1d39caafef9e860 |
| PDE #16 local rollout | a70bb9a3021baab2bc86263622f5317e92d3771805dc87f197a0d4b3ae664b9a |
| PDE #9 local rollout | 5200e1e6f6156a093db90f503f62afd0cb57571abae885f3c9c6ac7e9ae3c857 |
| Local session_index.jsonl | 4e5724c934effd809bdb42db56795c556c3035643999f7160728b8f9afb918d4 |

The live read-only SQLite query is record-level provenance, not a claimed immutable full-database snapshot.

Skill hashes, all fully read: solve-math-rigorously SKILL.md 9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7; investigate-conjectures SKILL.md a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de; evidence-ledger.md 9e7573b37cbd954432236bdcb13f6b83b6325e0ff2653a198939842bc81c3a2e; adversarial-audit.md 8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501, all under /etc/codex/skills.

## 11. Concrete corrected statements for the consolidation

| Recollection to avoid | Replacement |
|---|---|
| “The quadratic Stieltjes conjecture was resolved.” | The block-metric-uniform strengthening was disproved. Canonical QQ unit-metric all-order positivity was not resolved. |
| “Canonical order 19 passed.” | Canonical output order 17 passed. First-hidden order 18 follows from Q1'=8F and gives a ninth hidden moment without F19. |
| “All the hidden/backward kernels were Stieltjes.” | Finite output-coordinate transforms of two hidden norms and their normalized square roots passed. This is not a theorem about backward or two-time kernels. |
| “Positive moments/Hankel tests gave a global loss ODE.” | Finite Hankel compatibility is below all-order measure existence, determinacy, positive-time identification and fitting. |
| “Zero radius rules out smooth finite ODEs.” | It rules out exact analytic realizations with analytic readout and the specified positive Taylor/compiler classes. Smooth nonanalytic realizations are not excluded by that argument. |
| “The Taylor loss boundary layer is the network loss boundary layer.” | The established Taylor result concerns a non-Cauchy surrogate family. A canonical network layer requires an additional quenched theorem. |
| “DMFT proved instantaneous interpolation.” | The project postulated a tagged law; under its strong assumptions the comparison forbids positive subtarget delay. A selected step additionally needs a relaxed-selection rule; network identification is missing. |
| “The canonical no-go was independently settled because all reviewers passed.” | The covariant-Schur manuscript states a strong canonical initial-layer theorem; this audit read it fully but leaves its adaptive derivative/probability bridge uncertified for the reasons in Section 7. |
| “Noncommutativity proves no finite-source canonical path exists.” | The encoding argument has freeness/faithfulness/branch-separation assumptions and does not establish canonical path nonexistence. |
| “The multi-input Stieltjes closure is already defined.” | Symmetry-reduced scalar channels are defined; the generic noncommutative transformed-moment map and causal reconstruction were still missing in the recovered amendment. |

Outstanding consolidation limitations are source access to PDE-2 #19, an independent complete audit of the covariant-Schur adaptive bridge, and—if stronger computational certification is desired—end-to-end review of the retained high-order generators and transcendental sine enclosures. None was silently replaced by numerical experiments, literature abstracts, or prior PASS labels.
