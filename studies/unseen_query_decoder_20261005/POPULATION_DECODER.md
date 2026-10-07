# Population transcript route for a query supplied after training

2026-10-05. Scoped independent theoretical attempt. Internal partial result;
not a promotion or a completed compression theorem. No experiments were run.

The available finite-panel theorem does not imply the requested late-query
theorem. There is, however, a concrete candidate whose *conditional memory
count* has the desired absolute exponent five: compile training into a causal
Gaussian program of temporal Taylor jets, and extend its scalar Gaussian law
when a query arrives. The missing steps are quantitative growing-program
identification, stability of the population numerical construction, and an
autonomous all-time continuation with counted memory. None is established by
the two authorized research inputs. The exact identities and the conditional
count below identify the candidate without treating its missing estimates as
assumptions of a claimed theorem.

## 1. Scope, notation, and inherited input

Let $v_a=x_a/\sqrt d\in S^{d-1}$, $1\le a\le m$, with
$\operatorname{span}\{v_a\}=\mathbb R^d$, $m\ge d$, and fixed depth
$L\ge2$. The width-$n$ network is

\[
z^{(1)}(t,v)=A(t)v,\qquad
z^{(\ell)}(t,v)=W^{(\ell)}(t)h^{(\ell-1)}(t,v),\qquad
h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad
f_n(t,v)=w(t)^Th^{(L)}(t,v)/n.
\]

Initialization has independent $N(0,1)$ entries in $A$, independent
$N(0,1/n)$ entries in the hidden mixers, and $w(0)=0$. All blocks train
under mean squared loss, with mobilities $n,1,\ldots,1,n$. The residual is
always $r_a=f_n(t,v_a)-y_a$. Write

\[
\delta_a^{(L)}=w\odot\phi_L'(z_a^{(L)}),\qquad
\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot
                  (W^{(\ell+1)})^T\delta_a^{(\ell+1)}.
\]

Activations are real on the real axis, analytic on a common strip, and have
bounded first derivative there; values can be unbounded. We retain the original
small-label allowance of the authorized finite-panel source, not an additional
width-dependent label restriction. The positive initial training-feature Gram
gap is $\gamma$, and $\lambda=\gamma/m$. All problem parameters are fixed
as width tends to infinity. Constants below may depend on them.

The inherited near-root independent-dense comparison has the whole-sphere,
all-physical-time topology

\[
\mathbb P\left\{\|f_n-f_n'\|_*>b_n(\delta)\right\}\le\delta,
\qquad
\|F\|_*:=\sup_{t\in[0,\infty]}\sup_{v\in S^{d-1}}|F(t,v)|,
\tag{1}
\]

at sufficiently large individual width, with

\[
b_n(\delta)=C_\delta n^{-1/2}
 e^{C\sqrt{\log(en)}}\sqrt{\log(en)}+C/n=n^{-1/2+o(1)}.
\tag{2}
\]

The endpoint in this norm is the fitted limit. Equation (1) is an inherited
internally checked source statement, not reproved here. The explicit finite-panel
source separately gives an autonomous $O(\log(en)^5)$-storage model accurate
to $n^{-1+o(1)}$ on a panel declared before compilation. Its theorem expressly
makes no assertion about the same model on later queries.

## 2. What dense concentration supplies, and what it does not

A deterministic predictor center exists separately at every $n,\delta$.
Indeed, integrate (1) over the second root. Some fixed root $g_{n,\delta}$
has

\[
\mathbb P_G\{\|f_n(G)-f_n(g_{n,\delta})\|_*>b_n(\delta)\}\le\delta.
\tag{3}
\]

This is an existential center in the complete function space. It does not
show that the selected dense root is compactly describable or that its output
can be evaluated with compact workspace. It also does not identify a common
population predictor: a deterministic sequence of different centers has zero
independent-copy fluctuation regardless of whether it converges or of its bias
relative to any proposed population equation.

Consequently, replacing the dense network by “the population prediction”
requires both an identification/error theorem and an actual counted evaluator.
Neither follows from (1). Storing that entire predictor as one function-valued
coordinate would violate the representation contract.

There is an exact first-layer simplification. Put
$V=[v_1\ \cdots\ v_m]\in\mathbb R^{d\times m}$ and
$\alpha(v)=V^T(VV^T)^{-1}v$. The spanning assumption implies

\[
v=V\alpha(v),\qquad
z^{(1)}(t,v)=\sum_{a=1}^m\alpha_a(v)z_a^{(1)}(t).
\tag{4}
\]

This identity holds at every width and time. It does not imply the analogous
linear relation for $h^{(1)}$, or at subsequent layers. Analytic nonlinear
composition is precisely where an unseen input adds new matrix arguments.

## 3. Exact learned-memory and late-query identities

The actual finite gradient flow obeys

\[
\begin{aligned}
\dot A&=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^T,\\
\dot W^{(\ell)}&=-\frac2{mn}\sum_a
              r_a\delta_a^{(\ell)}h_a^{(\ell-1)T},\\
\dot w&=-\frac2m\sum_a r_a h_a^{(L)}.
\end{aligned}\tag{5}
\]

Integrating (5), without approximation, gives for any late query $v$

\[
\begin{aligned}
z^{(\ell)}(t,v)
 &=W_0^{(\ell)}h^{(\ell-1)}(t,v)\\
 &\quad-\frac2m\sum_a\int_0^t r_a(s)\delta_a^{(\ell)}(s)
 \frac{h_a^{(\ell-1)}(s)^Th^{(\ell-1)}(t,v)}n\,ds,\\
f_n(t,v)
 &=-\frac2m\sum_a\int_0^t r_a(s)
 \frac{h_a^{(L)}(s)^Th^{(L)}(t,v)}n\,ds.
\end{aligned}\tag{6}
\]

There are two unknowns in (6): the initialized action on a new nonlinear
argument, and its joint pairings with training-history fields. Training-only
Gram matrices do not determine these objects at finite width. Treating the
new action as independent Gaussian would erase transpose responses.

To make that last point exact, let one initialized mixer $W_0$ have previously
revealed $W_0H=Z$ and $W_0^TD=B$, with independent columns in $H,D$.
Define $P_H=H(H^TH)^{-1}H^T$, and similarly $P_D$. For a new input $h$
chosen measurably from the complete preceding transcript, Gaussian conditioning
gives

\[
\begin{aligned}
W_0h&\overset d=Z\alpha+D\beta
  +\frac{\|(I-P_H)h\|_2}{\sqrt n}(I-P_D)g,\\
\alpha&=(H^TH)^{-1}H^Th,\qquad
\beta=(D^TD)^{-1}B^T(I-P_H)h,
\end{aligned}\tag{7}
\]

where $g\sim N(0,I_n)$ is fresh conditionally on that transcript. The $D\beta$
term preserves reverse observations. Formula (7) is valid for genuinely causal
finite queries, not for selected samples of a trajectory whose unrecorded
matrix calls have been discarded. Exact dependent columns can be deleted;
nearly dependent columns need quantitative stability. The training gap
$\gamma>0$ supplies no lower bound on all such history Grams.

## 4. Exact finite Taylor-program count

This section counts algebraic instructions. It does not assert a global
convergence estimate for the resulting numerical scheme.

At a real patch origin τ, write $U[k]=\partial_t^kU(\tau)/k!$.
Order-$K$ jets satisfy the exact truncated-power-series recurrences

\[
\begin{aligned}
z^{(1)}_a[k]&=A[k]v_a,\\
z^{(\ell)}_a[k]&=\sum_{i+j=k}W^{(\ell)}[i]h_a^{(\ell-1)}[j],\\
h_a^{(\ell)}[k]&=[s^k]\phi_\ell\left(\sum_{i=0}^Kz_a^{(\ell)}[i]s^i\right),\\
(k+1)A[k+1]&=-\frac2m\sum_a\sum_{i+j=k}r_a[i]\delta_a^{(1)}[j]v_a^T,\\
(k+1)W^{(\ell)}[k+1]&=-\frac2{mn}\sum_a\sum_{i+j+q=k}
 r_a[i]\delta_a^{(\ell)}[j]h_a^{(\ell-1)}[q]^T,\\
(k+1)w[k+1]&=-\frac2m\sum_a\sum_{i+j=k}r_a[i]h_a^{(L)}[j].
\end{aligned}\tag{8}
\]

The prediction and backward jets follow from the same power-series product
rule and the displayed definitions. At order $k$, the parameter jets are
known from lower orders; a forward pass followed by a backward pass then
produces the order-$k$ gradient. Thus (8) specifies a causal finite calculation.

Every trained mixer can be represented as its original $W_0^{(\ell)}$ plus
linear combinations of rank-one pairs of past training feature and response
jets. Distinct triple indices in (8) change scalar coefficients; they do not
create distinct new vector directions beyond those feature/response jets.
For $H$ patches and degree $K$, let

\[
R=C_{L,m}(H+1)(K+1)+d.
\tag{9}
\]

Then all initialized-matrix actions, in both orientations, and all named vector
directions can be bounded by $R$, after enlarging the fixed coefficient.
Dense learned memories have the form

\[
W_0^{(\ell)}+\sum_{i,j\le R}c_{ij}^{(\ell)}u_i^{(\ell)}
                         v_j^{(\ell-1)T}/n.
\tag{10}
\]

The coefficient count is $O_L(R^2)$. Formula (10) alone still stores $nR$
vector entries if interpreted at finite width; it is not a compact realization.

High derivatives do not themselves require an exponentially large stored
Faà di Bruno list. At one neuron, put $p(s)=\sum_{i=1}^Kz[i]s^i$, and compute
the triangular array $[s^k]p(s)^j$, $j,k\le K$, by convolution. Then

\[
h[k]=\sum_{j=0}^k\frac{\phi^{(j)}(z[0])}{j!}[s^k]p(s)^j.
\tag{11}
\]

This uses $O(K^2)$ scratch and polynomial arithmetic work. The corresponding
backward calculation uses derivatives through order $K+1$. These derivatives
may have large bounds, affecting quadrature accuracy and stability; the
polynomial *storage* count is not a bound on these constants. The common
activation evaluator must actually evaluate the needed derivatives or finite
approximations to them; no new derivative oracle is free.

## 5. Conditional Gaussian-law representation and late-query workspace

Suppose a valid deterministic population version of the complete causal
program (8) has been constructed. A field at a single neuron is then represented
by a scalar expression in its layer's initial roots and finitely many Gaussian
innovations, together with deterministic coefficients fixed by earlier
expectations. The law includes both directions of each initialized mixer.
This is a conditional statement about a Gaussian program, not an assertion
that trained finite neurons are independent.

Maintain the program's $O(R^2)$ covariance, response, and rank-memory scalar
coefficients and its algorithmic instruction schema. A scalar neuron evaluator
can run the jet recurrence sequentially with $O(R+K^2)$ live scalar values.
It need not retain the full arithmetic expression tree. Loop indices and
recursion stacks are ordinary counted data; they do not encode dense weights.

If each required expectation has a finite constructive quadrature rule with
certified truncation/error control, tensor quadrature over at most $C(R+d)$
Gaussian variables can be streamed: retain one vector of nodes, its index
vector, one accumulator, and one evaluator workspace. This has $O(R^2+d^2)$
space even when the number of nodes is enormous. The quadrature cannot be
treated as a primitive exact integration oracle. Selection of finite nodes
and error tolerances, including errors through nearly singular conditioning,
is a proof obligation.

When $v$ arrives, (4) supplies its first preactivation as a function of the
training first-layer law. The first activation remains nonlinear. At each
subsequent layer, compute its cross-pairings with the retained training
directions, evaluate the learned-memory part of (10), and append the new
initialized action using the *joint* Gaussian law (7). The query is passive
and supplies no training residual. This process is causal layer by layer:
the new argument is determined before its own matrix answer is introduced.
At a fixed requested time, it requires $O_L(R)$ extra pairings/coefficients
and a bounded number of additional Gaussian actions, within $O_L(R^2+d^2)$
total workspace. Joint dependence on all earlier matrix uses is retained.

This establishes a genuine conditional distinction from spatial interpolation:
query dimension increases the Gaussian evaluator's input and fixed task
coefficients, but need not increase a power of $\log n$. It does not establish
the error of that evaluator against the actual trained dense network.

## 6. Where exponent five would come from

The authorized finite-panel analytic source supplies, on its source event,

\[
T_n=C\log(en)/\lambda,\qquad
r_n=c/[\lambda\sqrt{\log(en)}],
\tag{12}
\]

for finitely declared source curves, with constants independent of width.
For an analytic function bounded by $M_n$ on a disk of radius $r_n$,
the degree-$K$ Taylor tail on the concentric half disk is at most
$2M_n2^{-K-1}$, by summing the Cauchy coefficient bounds. If $M_n$ is
polynomial in $n$, degree $K=C_A\log(en)$ makes this tail at most
$n^{-A}$. Covering time with patches of radius proportional to $r_n$
would require

\[
H=O(\log(en)^{3/2}),\qquad
R=O_{L,m,d}(\log(en)^{5/2}),\qquad
R^2=O_{L,m,d}(\log(en)^5).
\tag{13}
\]

This derivation is conditional in three places. First, a radius of an exact
finite-width trajectory is not automatically a radius of the deterministic
population program or of a nearby numerical trajectory. Second, a supplied
Taylor tail does not bound accumulated perturbations of a multistep solver.
Third, the source theorem for each fixed panel does not automatically yield
one event for all late queries or a growing panel. Source constants, stopping
probabilities, and their dependence on program size must be controlled.

Thus (13) is a rigorously identified candidate storage scale, not a completed
upper bound for an accurate model.

## 7. Precise missing bridges and their logical roles

The following are sufficient obligations for this particular route. They are
not extra assumptions claimed to follow from the problem hypotheses.

**Growing-program width bridge.** For $H,K,R$ as in (13), construct the causal
population program associated with (8), using the actual original model and
label allowance, and prove that its passive-query prediction $F_{n,H,K}$
obeys

\[
\mathbb P\left\{
\sup_{t\le T_n,\ v\in S^{d-1}}
|f_n(t,v)-F_{n,H,K}(t,v)|
>C_\delta n^{-1/2}e^{C\sqrt{\log(en)}}\log(en)^C
\right\}\le\delta+o(1).
\tag{14}
\]

Here the exponent $C$ on the logarithm is fixed independently of width;
its value is not required for the absolute *storage* exponent. The proof must
include high-order derivative instruction growth, concentration accumulated
over $R(n)$ dependent Gaussian calls, and history-rank loss without imposing
new positive eigenvalue gaps. A theorem for every separately fixed number of
matrix calls cannot be applied by substituting $R=R(n)$. The authorized
dense-comparison source expressly identifies this quantifier problem.

**Numerical population bridge.** Produce the scalar coefficient program and
finite expectation evaluators with controlled errors in (14), total stored
coefficients plus evaluator workspace $C R^2$, and no inaccessible population
function as a primitive. Establish the complex neighborhood and propagation
estimate needed to justify $H,K$, or provide another construction with the
same count. Large work and ordinary high arithmetic precision may be allowed;
an encoded dense state in a large integer or real is not.

**Autonomous continuation bridge.** The training representation must update
from its own counted state, rather than a precomputed future trajectory. A
finite causal Gaussian program can be implemented as an autonomous scheduled
algorithm using a clock and its coefficient/history state, but finitely many
patches stop at $T_n$. To satisfy an all-time evolving-model requirement,
provide a continuation using no additional unbounded history, with

\[
\int_{T_n}^\infty\sup_v|\partial_tF_n(t,v)|\,dt
 \le C e^{-\kappa T_n}.
\tag{15}
\]

An analogous tail is already available for the actual dense flow. If the
representation is also required to fit its training labels exactly at its
endpoint, that property must be proved for its own dynamics. The gap of the
original dense trajectory is not a fitting theorem for an approximate
population algorithm.

Under these three bridges, the elementary triangle inequality gives the
requested all-time near-root accuracy: for $t\ge T_n$, compare both outputs
to their values at $T_n$, then use (14) and their two tails. The same argument
includes $t=\infty$. No infinite-time/width interchange is needed. This
conditional transfer is proved; the three bridges remain open in this pass.

If a static time-indexed approximation were explicitly accepted instead,
evaluating the finite-horizon construction at $\min\{t,T_n\}$ would use only
the dense tail to extend its numerical output guarantee. That is not a proof
of an autonomously continuing nonlinear model or its own fitted endpoint and
is not offered here as satisfying the current contract.

## 8. Recomputing from scratch: exact workspace audit

An arbitrarily slow decoder can recompute intermediate scalar expressions and
save space. It cannot thereby regenerate discarded arbitrary Gaussian dense
weights. Keeping a seed that reproduces all original iid initialization entries
needs a valid finite-information model and a proof for that initialization law;
a short pseudorandom seed is not automatically the original Gaussian law.

Direct depth-first evaluation of a dense numerical solution saves its vector
state only if both the initialization coordinates and the solution expression
are accessible from counted data, and the entire recursion depth is counted.
A naive explicit method with $n^c$ sequential time steps has $n^c$ dependency
depth. Unlimited work alone does not reduce that stack to logarithmic memory.
An analytic jet construction could reduce the depth, but still needs (14) and
the numerical bridge to replace initialization by a computable population law.

Likewise, direct expectation over all $O(n^2)$ Gaussian initialization entries
has an $O(n^2)$-coordinate integration argument or equally long nested
enumeration stack. Putting its entire quadrature index in one enormous integer
would be precisely a packing shortcut. This is a limitation of these proposed
algorithms, not a computational lower bound against every possible decoder.

A clock-only “state” with an unspecified solution-map evaluator leaves the
whole task in an uncounted function oracle. The Gaussian-program proposal is
useful only insofar as Sections 4–7 replace that evaluator by finite scalar
instructions and prove their accuracy.

## 9. The stronger $n^{-1+o(1)}$ target

A deterministic population-only prediction cannot attain the stronger target
under the source's nondegenerate variability hypotheses $m\ge2,Y>0$.
The finite-panel source gives an independent-dense lower bound, witnessed at
a training query, of order

\[
a_n=c_{\delta}Y\sqrt\gamma\,
      n^{-1/2}\log(en)^{-5/2}.
\]

If one deterministic predictor $F_n$ approximated both independent copies
with error $\varepsilon_n=o(a_n)$ with arbitrarily high probability, then
$\|f_n-f_n'\|_*\le2\varepsilon_n$ on the intersection of those two success
events. Choose the individual failure probabilities and the lower-bound
failure probability to have sum less than one. This contradicts the displayed
lower bound for large $n$. In particular $n^{-1+o(1)}=o(a_n)$.

This argument does not rule out a decoder retaining an initialization-dependent
compact summary. The finite-panel compressor demonstrably preserves more
realization-specific information. Extending such information to the whole
sphere below the variability scale is a separate problem, and is not solved
by the deterministic Gaussian-law candidate above. The case $Y=0$ is exactly
zero, and no lower-bound claim is made for the source's exceptional cases.

## 10. A separate label-series reopening mechanism

One may introduce a scalar label multiplier $\zeta$, replacing $y$ by
$\zeta y$, and seek a series for the entire prediction in $\zeta$. At zero
multiplier, the zero-readout flow is stationary. Its successive label
derivatives are determined by differentiated finite-network equations and can
therefore be represented by recursive Gaussian and time integrals at each
fixed order. A decoder could evaluate such coefficients at the supplied query,
without storing all spatial polynomial coefficients.

This is a distinct possible representation, not a consequence of the real
small-label assumption. To use order $K=O(\log n)$ at the original labels
requires a complex label disk containing $\zeta=1$ with a uniform geometric
tail, including all physical times. It further requires quantitative width
errors for order growing with $n$, a full recursion/derivative workspace count,
and stable computable Gaussian/time integration. Recursive formulas can have
small descriptions while their depth or simultaneous working arrays grow
much faster; unlimited arithmetic work does not prove a memory bound.

The authorized dense-comparison report explicitly records only fixed-order
label identities and a shrinking complex label disk in the inspected source
route. It supplies neither the required fixed disk nor summable root-width
errors across orders. No new convergence estimate is derived here. The route
remains a possible reopening mechanism if those estimates are proved, with
the same deterministic-center restriction from Section 9 at the stronger
accuracy target.

## 11. Provenance and frozen status

Read completely: `finite_panel_absolute_compression_20261005/RESULT.md`;
`integrated_general_compression_20261004/GENERAL_DENSE_COMPARISON.md`;
`docs/index.qmd`; `docs/notation.qmd`. Additional maintained material read:
`docs/02-gaussian-reuse.qmd`, complete Sections 1–2 and 13.1–13.4. Section 2
supplies (7); Section 13 makes the distinction between a supplied-path memory
approximation and a causal Gaussian program explicit. No linked research
artifact outside the supervisor's authorized inputs was opened. No archive,
other route file, source history, or experiment was used. After this route
reported its initial mechanism and call-count analysis, supervisor followups
prompted the workspace and continuation audit and the label-series alternative.
A further supervisor message supplied the independent-center lower argument;
Section 9 had independently derived that argument before the message arrived.
Thus the initial route was isolated, while the final note includes these
explicit supervisory followups.

Process reads: the complete `investigate-conjectures` skill and its
research-contract and adversarial-audit references. The required canonical
notation skill at `/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`
returned `Permission denied`; its contents and neural-network reference were
not available to this route. The supplied presentation requirements and the
complete maintained notation contract were applied directly.

Frozen conclusion: exact finite identities, exact causal Taylor action counts,
and a conditional $O(\log(en)^5)$ Gaussian-program workspace architecture are
established here. An accurate autonomous late-query model at the requested
near-root scale is not established or refuted. The main error-source bottleneck
is (14); analytic/numerical stability and all-time finite-memory continuation
are additional independent obligations. The stronger deterministic
population-only $n^{-1+o(1)}$ claim is excluded by inherited nondegenerate
variability, without excluding initialization-dependent compact decoders.
