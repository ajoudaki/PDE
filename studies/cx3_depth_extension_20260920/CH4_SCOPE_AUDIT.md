# C-H4 scope and depth-extension audit

Author-side source audit for `cx3_depth_extension_20260920`, 2026-09-20.
Maintained source HEAD: `bcee9782651c34ae1204d37186e5c57e9282b273`.
This is a scoped contract extraction and structural gap analysis, not an
independent complete review or a new depth theorem. No training, tests, numerical
experiments, Git mutation, or other-study reading was performed.

## 1. Exact retained contract

The C-H4 theorem is `docs/global_nonlinear.md`, C.4.7.10.D.1–D.5
(lines 14246–16000). It extends the **same two-hidden-layer** closure used by
C-H3 to physical time 40 on a **different fixed supported family**. It does not
extend the C-H3 law family to time 40.

The finite network is bias-free, has dimension two and common hidden width
`n`, activation `tanh` at both hidden layers, stored independent Gaussian
variances `(1,1/n,1/n²)`, output division by `n`, mobilities `(n,1,n)`, residual
`f-y`, and unhalved probability-weighted squared loss. The first input to the
network is `u=x/sqrt(2)` on the unit circle. The finite random readout is
retained; zero readout occurs only in its population limit. The initialized
middle action is the canonical joint Gaussian action `A0`, with its actual
adjoint and `||A0||op<=2`; only its learned increment `K` is Hilbert–Schmidt.
These are fixed model choices, not interchangeable normalizations.
Sources: D.1, H40.C2; `docs/NOTATION.md` in full.

### Fixed represented laws

Set

\[
E_0=8192,\qquad E_{j+1}=2^{E_j}\quad(0\leq j<10),\qquad
\rho=2^{-E_{10}},\qquad
U(s)=\left(\frac{1-s^2}{1+s^2},\frac{2s}{1+s^2}\right),\qquad
\mathsf R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

For rational endpoints `-1<=a<=b<=1`, `-1<=c<=d<=1`, the family is

\[
\mu=\tfrac12\operatorname{Law}(\sqrt2 U(\rho S),+1)
     +\tfrac12\operatorname{Law}(\sqrt2\mathsf R U(\rho V),-1),
\quad S\sim\operatorname{Unif}[a,b],\quad V\sim\operatorname{Unif}[c,d].
\]

A degenerate interval denotes its atom. Two nondegenerate intervals give a
nonatomic law because the maps are injective. For example `a=b=0,c=d=1`
gives two inputs with normalized inner product `-2rho/(1+rho²)`, so even the
atomic subfamily is not confined to orthogonal inputs. Mixed atomic/nonatomic
choices are included. The parameters, radius and support are fixed before
closure or numerical refinement; shrinking them with the requested tolerance
would change the contract. No atom-count, minimum-weight or positive
Gram-eigenvalue hypothesis is added. Sources: H40.F1–F3.

The exact-population theorem is broader than that numerical representation:
it covers every separately fixed Borel law in `V_rho`, with equal label masses,
the prescribed binary labels, and normalized inputs within `2rho` of the
corresponding reference axes almost surely. D.2 proves an explicit cap radius
`r_cap` and then `rho<r_cap`; it does not rely on an unquantified assertion that
this radius lies in an earlier open neighborhood. D.4's executable numerical
statement uses the represented rational-endpoint family above. Neither family
is a theorem for arbitrary circle laws or a uniform-circle teacher law.

### Horizon, observables and learning

For each separately fixed supported law, the canonical solution is strong
`C1` on `[0,40]` in the row `L2`, increment HS and readout `L2` spaces. It is
unique on the prescribed initialized carrier and uniquely restartable from
each reached state. Arbitrary ambient operator states are not covered.

The approximation error includes all of:

1. prediction supremum on `[0,40]` times the **whole circle**;
2. uniform-time Euclidean `W2` error of each layer's training-averaged pair law
   `Law_(Omega_l x mu)(H^l(0,u),H^l(t,u))`;
3. uniform-time errors in the corresponding RMS paired displacements;
4. uniform-time training-risk error.

The pair uses the same initialized/current population coordinate and the same
input. Comparing separate marginals or coupling current neurons independently
of their own initial values would lose the claimed motion observable. There
is no cross-layer neuron pairing. Bounded hidden pairs also pass to the actual
finite-network interpretation. Sources: H40.C15–C16, H40.N2, H40.N7.

The target-flow learning guarantees are

\[
R_\mu(f_\mu(40))\leq\tfrac14,\qquad
J_{l,\mu}(1/200)\geq10^{-13}\quad(l=1,2),
\]

where `J` is the **squared** paired RMS displacement. Initial population risk
is one. These guarantees concern different times. They assert neither motion
at time 40 nor that feature motion causes the risk reduction. The theorem
does not establish superiority to a frozen-feature model. Sources: H40.F4;
D.2, section 6; C.4.7.7.

### Reference endpoint versus perturbed-law horizon

The reference is
`nu*=1/2 delta_(sqrt(2)e1,+1)+1/2 delta_(sqrt(2)e2,-1)`.
C.4.5.1 constructs its autonomous feature-time state and the unique first
feature time `s_dagger` at which
`b=<c,(H2_1-H2_2)/2>=1`. It proves `0<s_dagger<=10`. The physical clock
`ds/dt=2(1-b)` approaches this state only as physical time tends to infinity.
The reference has the all-time conclusions

\[
\sup_x|f_*(t,x)-f_*^\infty(x)|\leq17\sqrt{10}e^{-t/5},\qquad
R_{\nu_*}(f_*(t))\leq e^{-2t/5}.
\]

The selected endpoint is characterized by the actual trained feature equation,
not by uniqueness among interpolating predictors. Sources: C.4.5 exact
statement; C.4.5.1 sections 1–3, R4–R23.

C.4.5's perturbed-law conclusion compares the predictor at physical time 40
to **this reference endpoint**. Its advertised whole-circle error is at most
`1/4` with probability tending to one, and its proof has the stricter
limiting margin `1/16`. D.2 puts the supported family in that transfer domain
and applies the GF version, while D.3 identifies the perturbed population
flow. Thus the same reference-endpoint comparison is inherited on the
supported family (and is compatible with the stronger margins). It is not a
claim that the perturbed law has its own selected endpoint, converges to the
reference endpoint, fits its labels exactly, or is controlled for all time.
Only the reference receives the all-time/endpoint conclusion.

### GF, GD and numerical integration are separate

* C-H4's target and finite-network capture are **physical gradient flow**.
  Finite GF capture is in probability over initialization. For iid empirical
  data it is joint probability over samples and initialization. Width and
  sample count can grow arbitrarily relative to one another for each fixed
  target law. Actual approximating empirical laws need not remain within the
  support caps. No uniform failure probability over laws is asserted.
* The inherited C.4.5 endpoint/risk/activity statement for **raw GD** requires
  `eta_k sqrt(n_k)->0`, uses raw-weight interpolation and recomputed hidden
  fields, and observes the preceding GD node at time 40. C.4.7.7 explicitly
  states that its new nonlinear GF theorem does not extend that earlier GD
  theorem to a whole time-40 changed-law path theorem.
* The maintained closure solver uses **simultaneous explicit Heun** on its
  finite closure coordinates. This is numerical integration of the closure
  ODE, not literal finite-network GD or an exact physical flow at a fixed
  step. No rounded-Heun energy identity or unconditional loss descent is
  asserted.

Sources: D.2 section 6, D.3 reference/finite-GF paragraphs, D.4; C.4.5 (3)–(5),
C.4.7.1 and C.4.7.7; `observable_solver.py:204–247`.

## 2. Closure, representation and numerical contract

The exact order-`N` closure retains the matrix `M`, fixed `D`, and the two
joint laws `Law(b1,g,w)` and `Law(b2,c)`. The characteristic coordinates `w,c`
are not polynomial expansions in the features. The data-law interface is also
retained. Initialization is `w=g,c=0,M=D`.

The full dictionary is essential: its core consists of total-degree-at-most-N
Chebyshev products in the four lower variables
`(tanh g1,tanh g2,tanh p1,tanh p2)` and the two upper variables
`(tanh xi1,tanh xi2)`, where `xi_i=A0 tanh(g_i)` and
`p_i=A0* tanh(xi_i)`. An exhaustive prefix of bounded initialized words in
both actual action orientations is appended. The core alone is not substituted
for the exhaustive hierarchy. The ridge is fixed by order,
`eta_N=1/[1024(N+1)^2]`, and every retained coordinate, including redundant
ones, survives. `D=L2^{-1} C_N L1^{-T}` uses the same initialized action in
both directions. Sources: H40.C5–C8; `observable_initialization.py`.

At each input, evolution forms

\[
a=E_1[b_1\tanh(w\cdot u)],\quad H^2=\tanh(b_2^TMa),\quad
d=E_2[b_2c(1-(H^2)^2)],\quad Q=b_1^TM^Td,
\]

and evolves `w,c,M` by H40.C6. Both directions use `M` and `M.T`; they are
not independent Gaussian maps. The initializer/compiler is finished before
training, and no source tape, future trajectory, hidden action service or
observation history is consulted by the RHS. Sources: H40.C6; D.5;
`observable_solver.py:157–223`.

At a fixed exact order, the state includes probability laws and therefore is
not yet a finite scalar array. The numerical implementation replaces **each
complete joint mark law** by a finite integration rule. Separate initializer
size `Q` and population replay size `P` have separate roles. Independent
sampling of each mark coordinate would alter the joint law. The top and
bottom population indices are not paired with each other. Sources: D.4,
fixed-order mark limits; `code/README.md:794–822`.

For retained population sizes `P1,P2`, feature dimensions `d1,d2` and input
node count `A`, the complete retained numerical state has

\[
P_1(d_1+5)+P_2(d_2+2)+2d_1d_2
\]

scalars, and the input rule has `4A`. The two matrices index features, not
network width. Runtime state and stage storage do not grow with elapsed steps;
the planned step count needs its integer bits. D.5 separately counts
initialization tables, generic source graphs, arithmetic bit costs, input
blocks, output arrays and metadata. These are finite-resolution storage/work
statements, not affordable complexity guarantees in the requested accuracy.

For each fixed law and fixed order, the proven refinement order is:

\[
\text{arithmetic}\ \to\ \text{time mesh}\ \to\ \text{input quadrature}
\ \to\ \text{population replay}\ \to\ \text{initializer quadrature}
\ \to\ \text{generic source regularization};
\quad\text{then closure order }N\to\infty.
\]

The source regularization step is vacuous on the optimized core branch. All
resource allowances must admit each requested finite operation. This is the
iterated limit H40.N2; it supplies no arbitrary simultaneous diagonal, fixed
precision order limit, order/width rate, monotonicity, tolerance selector or
finite-run trajectory certificate.

Componentwise midpoint quadrature is explicit even for nonatomic laws and has
`W1` error at most `rho/m`; it is distinct from population integration. The
symbolic exponent has eleven small expression nodes, but resolving its radius
requires a denominator with `E10+1` bits. At precision `p` the implementation
may replace the radius by zero when `E10>4(p+8)+2`, with `p=17` for float64.
The coordinate displacement is at most `2rho<10^(-p-8)`, and that replacement,
the exact positive law, direct coordinate rounding, weight rounding and any
further collapse are recorded. Operational weights remain literal. Increasing
precision eventually disables collapse for the fixed exact law only with
sufficiently raised finite resource allowances. This proves asymptotic
representability, not practical resolution of the supported perturbations.
Sources: H40.N1–N8 and D.5; `observable_laws.py` in full.

The maintained time-40 validation records 14 configurations and exact
own-state restart. At its declared precisions, all supported perturbations
collapse to reference directions. Wider radius-1/20 arc runs are explicitly
exploratory. Orders 1,3,5 have dimensions `(5,3),(35,10),(128,21)`, with the
order-5 redundant tails retained. Finite output panels and saved times are
operational diagnostics, not the theorem's supremum norms. No runs or tests
were repeated in this audit. Sources: D.5; `code/README.md:1032–1114`.

## 3. What genuinely needs new work at three hidden layers

These are proof obligations exposed by the maintained proof, not assertions
that a depth extension is impossible.

**Internal gate products.** With typed actions `A2:H1->H2`, `A3:H2->H3`, the
three-layer algebra would have

\[
\Delta^3=c\phi'(Z^3),\quad Q^3=A_3^*\Delta^3,\quad
\Delta^2=\phi'(Z^2)Q^3,\quad Q^2=A_2^*\Delta^2.
\]

At two layers H40.C11 subtracts `c phi'(Z2)` using the reference `c` in
`L-infinity`. The only remaining problematic gate product is the bottom
`phi'(w.u)Q`, handled by one cutoff on the reference `Q` in H40.C12. At three
layers subtraction of `Delta2` also contains
`[phi'(Z2_N)-phi'(Z2)]Q3`. A bounded `L2->L2` action does not make `Q3`
bounded. That term needs a further tail/truncation argument; its error then
enters both `K2'=-2 int r Delta2 tensor H1` and the lower adjoint chain.
Plain repetition of the `L2`-Lipschitz calculation is invalid.

**More source families and coupled response rows.** C.4.7.3 N3–N8 uses one
forward family on population 2 and one reverse family on population 1.
Under its backward-row cap, each passive `Q` is a Gaussian plus a bounded
linear combination of first activations (N10). Its upper derivative recursion
closes pointwise because the readout and upper gates are bounded. At depth
three population 2 participates in two distinct adjacent matrix actions and
their adjoints; it must retain their full joint dependence. The corresponding
internal backward operand is no longer bounded by the readout supremum.
New causally ordered, mass-weighted source recursions and a uniform cap are
needed across both matrices. Gaussian initialization of separate matrices
does not license replacing trained forward/backward calls by independent maps.
Even the existing two-layer absolute cap estimate N19 cannot close at time 40;
the reference comparison is essential. Failure of that estimate is explicitly
not coefficient divergence.

**Reference continuation and selected endpoint.** The all-time two-layer
reference construction uses a coordinate clock that removes the first gate,
then a Lipschitz system involving a bounded upper readout (C.4.5.1 R5). The
scalar symmetry/feature-time energy identities suggest an architecture for a
deeper reference, but a third layer leaves an internal moving gate/adjoint
product after the bottom clock change. The maintained reference existence,
passive response-tail and endpoint proofs do not supply that new continuation
argument. Nor do the explicit two-layer constants `m>=1/10`, `T=40` and the
dyadic radius transfer automatically. Any changed depth-dependent horizon,
law radius or activity threshold must be stated as a changed contract.

**Dictionary, omitted actions and convergence.** A deeper closure needs a
generated observable space on every population and all adjacent initialized
actions and actual adjoints. Each initialized contraction and its joint marks
must come from a complete finite source program. The two-layer polynomial
core, its `(4,2)` Gaussian integration dimensions, response contraction and
dimensions `(5,3),(35,10),(128,21)` are architecture-specific. D.3's strong
filter argument is structurally reusable only after proving density and
reducing-space invariance for the new typed word language. Uniform control of
every forward/backward omitted action on compact target field sets and each
projected HS derivative must then enter the deeper one-reference comparison.
No operator-norm convergence of the initialized projections is available.

**Identification, motion and literal implementation.** A formal deep finite
closure and even its own energy identity would not establish that it equals
the finite-width limit. The finite-program/proxy capture must be checked for
the deeper source graph while retaining the actual finite readout. Pair laws
must preserve original/current fields on all three layers; current marginal
laws are insufficient. The literal maintained solver and initializer have two
populations and one feature matrix, so they do not implement a depth-three
closure. Extra matrix blocks, the intermediate joint law, frozen initial
fields, numerical limits, serialization and full storage/bit accounting need
explicit treatment. General finite-network support for arbitrary depth in
the package README does not extend the population closure API.

For every separately fixed depth, constants and finite dictionary sizes may
depend on that depth if the intended theorem permits it. That does not supply
a uniform-in-depth statement or justify taking depth to infinity. The main
upstream obligation is a canonical deeper reference and/or supported-law
trajectory with enough uniform passive tails to close the repeated internal
gate products; only after that can the projection and numerical arguments
be assessed as extensions of C-H4 rather than conditional formal machinery.

## 4. Actual read coverage and limits of this audit

All following paths are inside the permitted maintained inputs unless a skill
path is shown. The report uses the supplied scoped-subagent exception to
ordinary author startup and did not read study history or any other study.

* `docs/NOTATION.md`: complete, lines 1–98.
* `docs/global_nonlinear.md`: complete C.4.7.10.D.1–D.5, lines 14246–16000.
  The final read continued through line 16015, exposing only the next section's
  opening; that section is not evidence used here.
* Same chapter: C.4.5 statement, margins and limitations, lines 5270–5474;
  complete C.4.5.1 sections 1–3, lines 5475–5781. The final read continued
  through line 5795, exposing the next subsection's opening, not its proof.
* Same chapter: complete C.4.7.1 statement/observation contract, lines
  8989–9170; C.4.7.3 introduction and complete source/temporary-cap sections
  1–2, lines 9296–9611. The read continued through 9660 (opening of weighted
  transport and N20–N21). C.4.7.7 was read completely, lines 11398–11440.
* `code/README.md`: model/normalization lines 1–41 and complete relevant
  closure/solver/time-40 sections, lines 626–1114. An initial broad read also
  exposed later optional Torch prose, but no Torch-specific claim is needed.
* `code/pde/observable_solver.py`: complete, lines 1–350.
* `code/pde/observable_laws.py`: complete, lines 1–472.
* `code/pde/observable_initialization.py`: complete, lines 1–397.
* Required process sources read completely:
  `/etc/codex/skills/solve-math-rigorously/SKILL.md`,
  `/etc/codex/skills/investigate-conjectures/SKILL.md`, and its
  `references/research-contract.md`.

Heading-only searches in the maintained chapter and API modules were used to
locate these passages. No unlisted full section is represented as independently
checked: in particular III.F, the remaining C.4.7.3 cap proof, C.4.7.4–5,
C-H3's complete initialization/arithmetic proofs, and compiler/arithmetic
implementation dependencies were not independently reverified by this scoped
audit. D.1–D.5 expressly invokes them, and the present document extracts that
maintained dependency contract rather than certifying their proofs afresh.
No required scoped source was missing.

## 5. Bounded check of the assembled CONTRACT.md

Follow-up author-side check, 2026-09-20. I read the complete current
`CONTRACT.md` and reread the shared `AGENTS.md`; I did not read another
agent's assessment. This disposition compares the proposed obligations to
the maintained C-H4 inputs already read above. It does not validate a future
proof or implementation.

**Disposition: the contract preserves the substantive C-H4 D.1–D.5 target.**
Its positive depth-dependent radius, onset/activity times, fitting horizon
and motion margins are intentional extensions under the user's requested
`[0,T]` with substantial training. Their being fixed before all approximation
limits is explicit. Literal reuse of the two-layer numbers is unnecessary.
The following baseline obligations are present:

* The long branch contains every supported half-mass binary Borel law, not
  only two atoms. It explicitly requires nonorthogonal atomic members,
  genuinely nonatomic members and an exact represented arc family with
  convergent in-domain integration. Using distance `rho_L` instead of the
  old `2rho` is only a naming convention for the new radius; the represented
  maps must of course be chosen to stay inside that stated bound.
* Loss starts at one and ends strictly below `1/4`, with slack for transfer
  to finite networks. The fitting estimate must justify the horizon.
  The conditional `b_s>=m_L` argument is correctly distinguished from
  continuation, identification and perturbation control. The value
  `log(8)/(4m_L)` yields the stated conditional reference risk bound `1/8`.
* Motion remains the training average of squared **initial/current paired**
  activation differences. The contract strengthens the layer count to every
  layer and adds a stated early nonaffinity obligation. It does not infer
  final-time activity from early activity or motion in one layer from total
  gradient energy.
* Uniform-time whole-circle prediction, fixed admitted same-layer joint
  observations with second moments, pair `W2`, RMS and risk convergence are
  preserved. Whole-sphere observation for separately fixed higher-dimensional
  finite data is a named broader onset target. No finite output grid replaces
  the input supremum, and no cross-layer neuron-index pairing is introduced.
* Actual GF capture, deterministic and independent empirical data-law limits,
  and retained finite random readout are explicit. The long-horizon raw-GD
  bridge is correctly a new obligation with its own sufficient condition;
  neither C-H4 D nor a Heun limit is presented as having proved it already.
* The same closure runs through the full interval, with its complete current
  state and fixed marks at restart. There is no exact-state reset, new
  initialization or growing elapsed-time transcript. Actual initialized
  action adjoints, full joint marks, a determining word family, the retained
  ridge directions, iterated limits and initialization/storage/precision
  costs are all retained.

One minor wording clarification would help: section 5's phrase
“exact finite-population equations” should mean the **finite-feature,
law-valued closure**, before population quadrature. Its retained probability
laws are not a finite scalar array. The width-independent finite scalar
state is obtained only at a fixed numerical population resolution. The rest
of section 5 already distinguishes these limits correctly; this is a
clarification, not an identified mathematical scope defect.

**Reference endpoint clause.** C-H4 D's mandatory target is the actual
perturbed-law trajectory and its numerical approximation through a fixed
substantial-training time, with risk and early paired motion. The all-time
reference flow and selected reference endpoint belong to C.4.5.1 and underpin
the maintained two-layer proof; C.4.5 also supplies the related fixed-horizon
comparison to that reference endpoint. They are not all-time perturbed-law
conclusions of D. Consequently the contract may keep the reference-global
and endpoint extension as a named additional objective for this user's
finite-horizon target. Its present instruction to report any loss of that
inherited scope prevents silent substitution. If only the finite branch is
completed, the final claim should say that the **C-H4-D-type finite-horizon
extension** is complete while the **reference-global/endpoint extension** is
open, rather than claiming the entire inherited endpoint package. Making
the latter mandatory is necessary only if the intended headline additionally
promises a depth extension of C.4.5's endpoint theorem.

No forgotten C-H4-D baseline or missing scoped input was found in this bounded
contract comparison. No contract edit, computation, tests or Git writes were
performed; this disposition was appended only to the present audit.
