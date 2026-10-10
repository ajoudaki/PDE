# Retained responses, trainability, and compression of nonlinear learning

This study assembles one line of work: retain enough of the forward and
backward responses of a nonlinear network to describe its training, understand
whether the retained system learns, and control the error of its prediction.
The compact paper is the main quantitative result. The older dictionaries,
landscape results, and protected-geometry arguments supply distinct earlier
answers to these same representation and learning questions.

This is an assembled research source, not an addition to the established book.
The complete current compact proof is frozen in the five local `compact*.tex`
files. Selected older statements and their full proof sources are retained in
[older_theory.md](older_theory.md) and its source archive. Mathematical claims
below have the scope of those sources; the assembly does not confer promotion
status or replace their proofs with a summary.

## 1. The common problem and the different retained states

Use the book's notation: width $n$, number of training samples $m$, input
dimension $d$, and hidden depth $L$. For inputs $x_a$ of norm $\sqrt d$, put
$v_a=x_a/\sqrt d$. The dense network is

$$
z_a^{(1)}=W^{(1)}v_a,\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),\qquad
f_n(x_a)=\frac{(W^{(L+1)})^\top h_a^{(L)}}n.
$$

Write $r_a=f_n(x_a)-y_a$ and $\mathcal L_n=m^{-1}\sum_a r_a^2$.
The parameter mobilities are $(n,1,\ldots,1,n)$. The compact paper calls the
readout $w$; its exact correspondence is $w=W^{(L+1)}$. It initializes that
readout at zero, with independent Gaussian first-layer entries of variance
one and hidden entries of variance $1/n$. The book's small *random* readout
and the older population zero readout are distinct conventions and are not
silently substituted for this finite-network initialization.

The residual-free backward fields are

$$
\delta_a^{(L)}=W^{(L+1)}\odot\phi_L'(z_a^{(L)}),\qquad
\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot
W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
$$

In particular, the hidden weight velocity contains the forward/backward
pairing

$$
\dot W^{(\ell)}=-\frac{2}{nm}\sum_{a=1}^m
r_a\,\delta_a^{(\ell)}h_a^{(\ell-1)\top},\qquad 2\le\ell\le L.
$$

This identifies the shared object being represented: responses and their
pairings under actual matrix reuse. It does not identify every reduced model.

| Construction | Retained representation | Question addressed |
|---|---|---|
| Older observable dictionaries | Fixed initialized population feature families and a finite evolving coefficient state | Which current observables support prediction and learning? |
| Gaussian/orthogonal dictionary controls | Alternative frozen subspaces with matched dictionary dimensions on the same finite initialized carrier | How much does the chosen representation matter? |
| Legendre compression | A fixed number of moving history moments, together with fixed initialized dense mixers | Can the trained matrix correction be represented without storing a growing history? |
| Harmonic/Taylor compression | Selected neuron coordinates, exact source metrics, selected mixers, and a corrected nonlinear evolution | Can both retained responses and their geometry be compressed while preserving the dense prediction? |

The older dictionaries are predecessors in the representation program. The
paper adds a different quantitative construction and a comparison with a
coupled dense network. No claim that an old fixed-order dictionary is
literally a special case of the new selected-coordinate dynamics is needed
or established by this assembly.

## 2. Current main result: complete-trajectory compression

The authoritative statement is `cp:headline` in [compact.tex](compact.tex).
All four included proof files are present beside it; it imports neither the
long manuscript nor an originating study. Its hypotheses are material:

- Fixed $m\ge2$, $d$, and $L\ge2$, as width $n$ grows.
- Each layer activation is real on the real axis, holomorphic on a common
  strip $|\operatorname{Im}z|<a$, and has bounded first derivative there.
- With $Q^{(0)}_{ab}=v_a^\top v_b$ and
  $Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)]$ for
  $Z\sim N(0,Q^{(\ell-1)})$, the initialized last-layer population Gram has
  gap $\gamma=\lambda_{\min}(Q^{(L)})>0$ and $m/\gamma\ge1$.
- Define $Y=\|y\|_2/\sqrt m$ and

$$
\beta=\max\left\{10,1+\max_\ell|\phi_\ell(0)|,16/a,
\max_{\ell,j\in\{1,2\}}\sup_{|\operatorname{Im}z|\le a/2}
|\phi_\ell^{(j)}(z)|\right\}.
$$

  The label condition is $0<Y\le(\gamma/m)\beta^{-30L}$.
  Zero labels give a stationary predictor and are separate from the relative
  error statement.

For a promised query set $\mathcal X$, write

$$
\|f-g\|_{\mathcal X}
=\sup_{t\in[0,\infty]}\sup_{x\in\mathcal X}|f(t,x)-g(t,x)|,
$$

where infinity denotes the fitted limit. If $\widetilde f_n$ is an independent
dense run on the same training problem, each of the three constructions has

$$
\frac{\|f_{\rm model}-f_n\|_{\mathcal X}}
{\|f_n-\widetilde f_n\|_{\mathcal X}}
\xrightarrow{\mathbb P}0.
$$

The reference $f_n$ is the construction's coupled dense run. A missing fitted
limit or zero denominator counts as failure. The dense comparison supplies a
transient fluctuation witness, not an endpoint fluctuation theorem.

| Method | Promised queries | Sufficient retained real coordinates |
|---|---|---|
| Legendre | Whole sphere | Moving: $Cm(m/\gamma)^3 n^{5/4}[\log(en)]^2 e^{\sqrt{\log(en)}/2}$; additionally $(L-1)n^2$ fixed mixer coordinates |
| Harmonic | Whole sphere | $C(m+d)^2+(C/d)^{d+1}(Ym/\gamma)^4[\log(en)]^{3d+2}$ total |
| Taylor | Training inputs plus $p$ passive inputs declared before initialization | $C(m+p)^2[(Ym/\gamma)^4[\log(en)]^3+(m/\gamma)^2[\log(en)]^2[\log(e+\log(en))]^2]+C(m+p)d$ total |

Here $C$ depends only on activations and depth. The symbol $p$ in this table
counts passive inputs; it is **not** the older closure order. Harmonic and
Taylor also give absolute error at most $Y/n$ at each fixed confidence for
sufficiently large individual widths. Passive labels are never supplied.

The width thresholds are qualitative and problem-dependent. Counts concern
real coordinates, not finite-bit memory or setup work. Nonprimitive activation
evaluators are charged separately. The theoretical initializers use the
initialization and its finitely many derivatives; the proof gives no practical
global compiler cost bound. These are prediction-compression statements, not
generalization-risk conclusions or bounds on the old hierarchy's closure error.

### Complete proof organization

| Frozen file | Role and principal labels |
|---|---|
| [compact_fitting.tex](compact_fitting.tex) | Dense fitting, finite parameter length, fitted tails (`cp:fit`); signed perturbation stability (`cp:signed`) |
| [compact_foundations.tex](compact_foundations.tex) | Full analytic source argument and coefficient estimates (`cp:source`) |
| [compact_legendre.tex](compact_legendre.tex) | Projection identities, autonomous history construction and comparison (`cp:projection`, `cp:legendre`); actual dense variability (`cp:dense-lower`) |
| [compact_selected.tex](compact_selected.tex) | Sparse exact metrics, shared corrected evolution, initialized coefficient existence, and the two source constructions (`cp:selection`, `cp:selected`, `cp:jets`, `cp:harmonic`, `cp:panel`) |
| [compact.tex](compact.tex) | Complete setup, headline theorem and final probabilistic assembly |

The mechanism connecting fitting to compression is concrete. The fitting lemma
gives $\|r(t)\|_2/\sqrt m\le Y e^{-\gamma t/(2m)}$ and finite remaining
parameter length. The signed comparison weights perturbation growth by
integrable residual activity. Controlled finite-time approximation can then
be joined to fitted tails. The selected-coordinate method additionally
preserves a source-space metric and uses a readout correction; its optimizer
is specified explicitly and is not ordinary gradient flow of the corrected
prediction. The Legendre moments describe a growing history interval with a
fixed number of stored modes, rather than retaining every earlier state.

## 3. Related earlier results: why representation and geometry matter

[older_theory.md](older_theory.md) presents the selected complete statements,
model conventions, proof dependencies and historical check status. Its source
archive retains the full arguments. The selected content has three roles:

1. **Representation and landscape.** Circle landscape results at orders one
   through three, the complementary sphere result in its stated sector, and
   initialized-feature geometry explain fitting expressivity and architectural
   loss floors. They do not supply convergence of every trajectory.
2. **Protected ordinary-flow learning.** Pair and cyclic-triple results identify
   geometry that survives training and forces loss decay and state convergence
   for their stated families. They complement the compact paper's dense and
   selected-flow fitting arguments at different, explicitly specified scopes.
3. **Limits of incomplete trainability criteria.** Lower-layer trainability
   despite upper-feature collision, and a reached architectural plateau,
   distinguish the full training geometry from a single feature Gram and
   distinguish trajectory behavior from the existence of favorable states.

Do not replace these by weaker historical intermediate results or import
noisy-optimizer/selector results that were deferred. The weighted slow-onset
classification, C-X extensions, and attention program remain outside this
selected assembly.

## 4. Dictionaries as the earlier computational comparison

[DICTIONARIES.md](DICTIONARIES.md) records the finite-carrier dictionary contract,
the matched Gaussian and orthogonal controls, and the selected historical
findings, including negative results. The question is prediction fidelity to
the trained dense function under an explicit representation budget. It is
related to the newer compression question but has a different approximation
parameter, query sampling rule, and numerical horizon.

The reusable core preserves frozen dictionaries, nested random subspaces,
seed conventions, dictionary dimensions, conditioning and endpoint-fit checks.
Observable raw spaces are nested; their ridge-normalized columns need not be
column prefixes. Historical results
are retained with their original evidence and limitations; this assembly does
not rerun a training campaign or turn those results into new empirical claims.

## 5. One implementation family, explicit construction contracts

[CODE.md](CODE.md) describes dense, Legendre, Harmonic and Taylor execution.
[DICTIONARIES.md](DICTIONARIES.md) describes the earlier closure and dictionary
execution. Their code is local to this study or depends on the maintained
`code/` library, not the paper's experiment driver or a historical study ZIP.
The shared conventions are normalized input rows, residual $f-y$, unhalved
mean squared loss where applicable, and actual forward/backward reuse.
The older weighted population model retains its stated probability weights.

Code coverage is about the declared numerical methods and tested configurations,
not every quantifier of an asymptotic theorem. In particular, an initializer
using a dense rollout must be identified as such. An origin-jet approximation
must state its order and cannot inherit the global analytic compiler's theorem
merely because it uses no later trajectory samples. Finite-step evolution and
empirical quadrature are likewise not exact GF or exact Gaussian integration.

The implementation checks target equations, source metrics, initialization,
projection, energy identities and numerical steps. Large sweeps, manuscript
figures, campaign scheduling and broad performance benchmarking are outside
this assembly. Actual check commands and results are recorded in the README.

[DATA.md](DATA.md) and [VISUALS.md](VISUALS.md) describe the supporting
reproducibility layer: toy tasks, official-split binary MNIST preparation,
radial/spherical prediction and signed-error views, and offline interactive
comparisons. [support_example.py](support_example.py) connects them to all
three compression methods and the dense reference. These are reusable
utilities and operational examples; they introduce no empirical learning claim.

## 6. Status and intended integration

The current study preserves the compact theorem and its proofs, assembles the
older distinct results, and supplies a small common implementation surface.
Source identity, dependency completeness and small numerical checks are separate
from mathematical acceptance. Older review verdicts remain attached to their
original inputs; the unified document is not an independent review of itself.

If promoted after the required review gates, the quantitative compression
argument belongs in Part II after autonomous computation. The earlier learning
geometry belongs in Part III near trainability, with cross-references explaining
its role in the same response-representation program. Shared code belongs in
the maintained implementation. One assembled promotion can have these several
natural destinations without repeating proofs or forcing unrelated model
assumptions into a single theorem.
