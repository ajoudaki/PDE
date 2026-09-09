# Resolution evidence ledger

Status vocabulary follows the conjecture-investigation workflow.  The source
of truth for prior results remains `../CURRENT_RESEARCH_STATE.md`.

## C-1: canonical fixed-order formal jet

- Statement: for every fixed derivative order, the canonical Gaussian
  expectation has the all-order decorated-forest reduction and a finite
  leading-width value defining $F^{(k)}(0)$.
- Claim-ladder rung: exact formal construction.
- Status: proved for the canonical special-case grammar.
- Limitation: no concentration, positive-time curve, or uniformity in the
  derivative order.
- Authoritative sources: `../../mean_field_peeling/CURRENT_RESEARCH_STATE.md`
  Sections 11.1--11.3 and `../CURRENT_RESEARCH_STATE.md` Sections 1 and 3.

## C-2: V1 all-order Stieltjes moment existence

- Statement: every ordinary and shifted Hankel matrix of $(\mu_r)$ is PSD.
- Claim-ladder rung: hierarchy convergence / existence.
- Status: open.
- Supporting evidence: exact $(\mu_0,\ldots,\mu_7)$, all accessible canonical
  tests, finite prefixes of several parameter-continuum families, and an
  exactly solvable positive variance boundary.
- Contrary evidence: none for the canonical sequence; several generic proof
  mechanisms and the stronger metric-uniform extension have exact
  counterexamples.
- Cheapest decisive resolver: an all-order architecture-specific Gram,
  Jacobi, cone-preservation, or operator construction; negatively, any exact
  later Hankel quadratic form.  The canonical order-fifteen and
  order-seventeen gates have now passed exactly.  The next new leading
  ordinary determinant is $H_4$; it requires $\mu_8$, hence the canonical jet
  through order nineteen.  No order-nineteen computation was attempted in
  the frozen successor.
- Concrete falsifier: any later exact negative canonical Hankel form.

## C-3: V2 determinacy

- Statement: the V1 representing measure is unique.
- Claim-ladder rung: uniqueness.
- Status: open.
- Supporting evidence: none decisive; the solvable variance boundary is
  determinate but is a different model.
- Contrary evidence: the canonical zero-radius theorem forces any measure to
  have unbounded support, so compact-support determinacy is unavailable.
- Cheapest decisive resolver: moment-growth asymptotics sufficient for a
  determinate or indeterminate Stieltjes criterion, or essential
  self-adjointness/nonuniqueness of the canonical Jacobi operator.

## C-4: V3 global neural identification

- Statement: an independently constructed deterministic width-first kernel
  exists and equals the moment-selected Stieltjes resolvent on the declared
  physical output interval.
- Claim-ladder rung: identification with the intended system.
- Status: open.
- Supporting evidence: two finite widths and several proxy experiments only.
- Contrary evidence: no valid counterexample; finite-width comparisons are
  statistically unresolved and do not identify the limit.
- Dependencies: V1, V2, deterministic positive-time mean-field existence,
  derivative/width-limit compatibility, and a nonperturbative equality
  principle.
- Concrete falsifier: a rigorous limiting kernel violating complete
  monotonicity, a Stieltjes Loewner condition, or a mandatory moment bracket.

## C-5: solvable variance boundary

- Statement: the normalized $\alpha=0$ boundary has an explicit positive,
  compactly supported Stieltjes measure.
- Claim-ladder rung: complete special-case theorem.
- Status: proved.
- Limitation: it is not the canonical $\alpha=1$ architecture; its signed
  first variation rules out additive-measure and coordinatewise-monotone
  Jacobi homotopies.

## C-6: formal zero radius

- Statement: the canonical feature and physical-loss formal jets have radius
  zero.
- Claim-ladder rung: exact all-order growth theorem.
- Status: proved.
- Consequence: if V1 holds, every representing measure has unbounded support.
- Nonconsequence: zero radius neither proves nor refutes moment existence or
  determinacy.

## C-7: exact finite-order compatibility

- Statement: all conditions decidable from the first eight canonical moments
  and the accepted parameter-family prefixes pass.
- Claim-ladder rung: finite construction / tested compatibility.
- Status: proved at the recorded finite orders.
- Supersedes: the earlier first-six-moment formulation after exact acceptance
  of the order-fifteen/order-seventeen successor.
- Nonconsequence: no upgrade to C-2.

## C-8: generic and local positivity mechanisms

- Statement: raw coefficient positivity, generic Gaussian gradient flow,
  local profile total positivity, additive variance measures,
  coordinatewise Jacobi monotonicity, and aggregate-sector total
  nonnegativity suffice for V1.
- Claim-ladder rung: proposed proof mechanisms.
- Status: falsified as generic sufficiency claims.
- Limitation: these failures do not falsify C-2; any successful proof must use
  a genuinely nonlocal architecture-specific relation.

## C-9: uniform block-metric Stieltjes extension

- Statement: the output-kernel moments are Stieltjes for every
  $D_{\alpha,\beta}=D_a+\alpha D_u+\beta D_W$ with
  $(\alpha,\beta)\in[0,\infty)^2\setminus\{(0,0)\}$.
- Claim-ladder rung: U1, the stronger family-level moment/existence claim.
- Status: **disproved**.
- Exact counterexample: for \(\beta=1\), the determinant obeys
  \[
  \det(\mu_{i+j+1}(\alpha))_{i,j=0}^2
  =\frac{55296P(\alpha)}{2358125(63+48\alpha)^{33}}<0
  \]
  for every \(0\leq\alpha\leq1/100\).
- Interior scope: every \(0<\alpha\leq1/100\) gives a strictly positive block
  metric, so the counterexample is not an artifact of freezing \(u\).
- Sharp finite-prefix audit: on the full \(\beta=1\) ray, every other leading
  condition available from \(\mu_0,\ldots,\mu_5\) has a
  coefficientwise-positive numerator.  The displayed determinant has one
  unique positive root
  \(\alpha_*=0.017519225541486\ldots\), exactly isolated between
  \(17519225541486/10^{15}\) and
  \(17519225541487/10^{15}\).  The six-moment truncation fails below
  \(\alpha_*\), is singular at it, and passes strictly above it.  This is not
  an all-order phase boundary.
- Consequence: uniform U2 and U3 are false because each includes U1.
- Nonconsequence: canonical V1--V3 at $(1,1)$ remain open.
- Authority: `BLOCK_METRIC_RESOLUTION.md`,
  `BLOCK_METRIC_COUNTEREXAMPLE.json`, and
  `block_metric_counterexample.py`.
- Interior authority: `BLOCK_METRIC_POSITIVE_ALPHA_JET.json`,
  `ALPHA_INTERVAL_CERTIFICATE.json`, and the direct-\(\mathbb Q[\alpha]\) and
  37-node scalar reconstruction audits.
- Sharp finite-prefix authority: `alpha_transition_certificate.py` and
  `ALPHA_TRANSITION_CERTIFICATE.json`.

## C-10: canonical order-fifteen/order-seventeen successor

- Statement: the canonical fixed-order recurrence gives
  \[
  F^{(15)}(0)=49079184579077107476764629402991788032,
  \qquad
  F^{(17)}(0)=30555969894096099495444855650521777374167040.
  \]
  Exact inversion gives
  \[
  \mu_6=
  \frac{233701098505506644778710348585571696126248608}
  {523079786422749003601451969851378666466523525},
  \quad
  \mu_7=
  \frac{70048496819304110407804100699554764688052780719822}
  {218993917770958359962588987442799241938248378067125}.
  \]
- Claim-ladder rung: exact fixed-order construction.
- Status: accepted exact computational certificate.
- Hankel consequence: every principal minor of the newly completed
  $H_3=(\mu_{i+j})_{i,j=0}^3$ and
  $H_3^+=(\mu_{i+j+1})_{i,j=0}^3$ is strictly positive.  In particular,
  \[
  \det H_3=
  \frac{4581116513595315356583611738530988438162599733688069549013816754981347215833268704400090246049792}
  {65354315638055287686313547406928749888486398559119734829544762489701014494772697096643566490984375}>0
  \]
  and
  \[
  \det H_3^+=
  \frac{137984062500683379206705700665534552146154930313101025462488622111967390693657363652277493269175099282762503439873283096576}
  {4841427533479109861977652240500543777398925508758255281888009610895813561244370117263221332603626422004447587045586035469140625}>0.
  \]
- Independent evidence: two isolated exact recurrences reproduce the entire
  accepted prefix, all parity zeros, and both new integers.  The retained
  production order-seventeen run used 230.318 seconds and 189.4375 MiB peak
  RSS; the independent route used 43.59 seconds at standalone order fifteen
  and 163.08 seconds with 94,060 KiB peak RSS at order seventeen.
- Limitation: this proves only eight-moment finite-prefix compatibility.  It
  supplies no all-order PSD theorem, trajectory-limit theorem, determinacy,
  or neural-curve identification.
- Stop: the protocol ended at order seventeen; no order-nineteen branch was
  authorized or attempted.
- Supersedes: the earlier ledger statement that the next unresolved finite
  gate required $F^{(15)}(0)$.
- Authority: `canonical_high_order/RESULTS.md`,
  `canonical_high_order/PRODUCTION_RESULT.json`,
  `canonical_high_order/INDEPENDENT_RESULT.json`, and
  `canonical_high_order/F17_MOMENT_HANKEL_AUDIT.json`.

## C-11: canonical hidden-norm high-order successor

- Statement: for $N_j(y)=Q_j(F^{-1}(y))$, the canonical first-hidden response
  $(N_1(\sqrt x)-1)/x$ has nine exact moment candidates, while the independent
  second-hidden response $(N_2(\sqrt x)-3)/x$ has eight.
- Claim-ladder rung: exact fixed-order construction for companion
  observables.
- Status: accepted exact computational certificate.
- Hankel consequence: the first-hidden ordinary $H_4$ and shifted $H_3^+$
  are positive definite; the second-hidden ordinary and shifted $H_3,H_3^+$
  are positive definite.  Every accessible principal minor is strictly
  positive.  The same statement holds for both normalized literal-RMS
  response sequences.
- Structural scope: $Q_1'=8F$, so the first response is inherited from the
  inverse-output Stieltjes structure and its ninth moment uses
  $Q_1^{(18)}=8F^{(17)}$ without $F^{(19)}$.  The second response is a separate
  companion conjecture and is not implied by output positivity.
- Independent evidence: two isolated exact recurrences agree on the complete
  $F,Q_1,Q_2$ jets through their frozen orders; direct $y$-coordinate
  inversion and an algebraically separate $x=rA(r)^2$ inversion agree on all
  moments, matrices, and principal minors.
- Limitation: finite-prefix compatibility only; no all-order companion
  measure, determinacy, positive-time mean-field limit, or neural-trajectory
  identification follows.
- Stop: no $F^{(19)}$ or $Q_2^{(18)}$ branch was attempted.
- Authority: `canonical_hidden_high_order/RESULTS.md`,
  `canonical_hidden_high_order/HIDDEN_MOMENT_HANKEL_AUDIT.json`, and
  `canonical_hidden_high_order/INDEPENDENT_HIDDEN_SCALAR_AUDIT.json`.

## C-12: shallow raw-square formal counterexample and characteristics

- Statement: the one-input \((\alpha,\beta)=(0,1)\) boundary is exactly a
  random-multiplier one-hidden-layer raw-square feature flow, and its
  separately fixed width-limit jet is a positive rescaling of the
  conventional multiplier-one shallow jet.
- Claim-ladder rung: exact finite-width reduction, fixed-order limit, and
  formal-moment falsification.
- Status: **proved**.  The conventional shallow moments through \(\mu_5\)
  have
  \[
  \det(\mu_{i+j+1})_{i,j=0}^2
  =-\frac{86245462994269879146938487857152}
  {516623655319449980325461333747775}<0.
  \]
  Hence this shallow formal output-kernel sequence is not Stieltjes.
- Dynamical structure: every neuron obeys
  \(a'=v^2,\ v'=2av\), conserves
  \(c=a^2-v^2/2\), and has the exact representation
  \(a=-D'/(2D),\ v=v_0/D\) with \(D''=4cD\).
- Compression consequence: Stieltjes positivity is not necessary for an
  exact low-dimensional characteristic/transport representation.  The
  result is not a closed scalar population-loss ODE or a finite-state lower
  bound against other compression classes.
- Limitation: iid Gaussian characteristics have poles on positive-measure
  initial-data sets before every fixed positive feature time, so no ordinary
  global Gaussian population curve or identification theorem is asserted.
- Authority: `SHALLOW_QUADRATIC_REDUCTION.md`,
  `shallow_quadratic_certificate.py`, and
  `SHALLOW_QUADRATIC_CERTIFICATE.json`.

## C-13: smooth-activation-universal extension

- Statement: the formal output-kernel moments are Stieltjes for every smooth
  bounded activation in the two-hidden-layer, one-input, equal-Euclidean-
  metric model.
- Claim-ladder rung: family-level activation-universal extension.
- Status: **disproved**.
- Counterexample: for the normalized sine activation, independently audited
  order-five Gaussian-normal-form maps give
  \(A=4.03709694646564\ldots>0\),
  \(\mu_0=-3.16776198608130\ldots<0\), and
  \(\mu_1=-3.03999737837846\ldots<0\).
- Limitation: this is one explicit fixed-order annealed counterexample, not a
  theorem about typical activations and not a positive-time trajectory
  result.  It does not refute the canonical quadratic \((1,1)\) sequence.
- Authority: `../../mean_field_peeling/generic_first_stieltjes/README.md` and
  its order-five primary/independent/hostile-audit artifacts.
