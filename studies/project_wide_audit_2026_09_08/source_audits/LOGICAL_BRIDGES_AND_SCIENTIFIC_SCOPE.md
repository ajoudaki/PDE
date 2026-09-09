# Logical bridges and scientific-scope checks

These elementary arguments are written out for the unified document. They are not new global neural-network theorems. They prevent interpretation errors when combining the project's results.

## 1. Zero Taylor radius does not prohibit smooth autonomous ODEs

Let G be a standard real Gaussian and define

\[
g(t)=\mathbb E\frac{1}{1+t^2G^2},\qquad t\in\mathbb R.
\]

For every fixed derivative order k, differentiating `r(tG)` where `r(x)=1/(1+x^2)` gives `G^k r^(k)(tG)`. Each rational derivative r^(k) is bounded on the real line, and every Gaussian absolute moment is finite. Dominated differentiation therefore gives g in C-infinity, including at zero. Its derivatives satisfy

\[
\frac{g^{(2k)}(0)}{(2k)!}=(-1)^k\mathbb E G^{2k}=(-1)^k(2k-1)!!,
\qquad g^{(2k+1)}(0)=0.
\]

The coefficient root `((2k-1)!!)^(1/(2k))` tends to infinity. For example, at least the last floor(k/2) factors in `(2k-1)!!` are at least k, which already makes that root diverge. Thus the Taylor series has radius zero.

Nevertheless the autonomous system

\[
\dot s=1,\qquad \dot q=g'(s),\qquad (s(0),q(0))=(0,1)
\]

has the unique global solution `(s(t),q(t))=(t,g(t))`. Its vector field is smooth, locally Lipschitz, finite-valued everywhere and never zero. It has no singularity at the initial state. This counterexample is a logical test of an ODE impossibility inference, not a proposed neural-network closure or a source-compression theorem.

A finite-dimensional analytic vector field with an analytic observable produces analytic local time dependence, so a correctly identified actual zero-radius jet does obstruct that analytic class. A formal width-limit jet needs an additional identification argument before it describes derivatives of an actual limiting path. Zero radius by itself says nothing comparable about smooth ODEs, nonanalytic initial-data PDEs, or operator evolutions with unbounded generators.

## 2. Compact-time approximation reaches any fixed requested training accuracy

Suppose for each fixed finite T,

\[
\sup_{0\le t\le T}|\mathcal L_n(t)-\mathcal L(t)|\to0
\quad\text{in probability},
\]

and the deterministic population loss tends to zero as t tends to infinity. Given epsilon>0 choose a finite `T_epsilon` with `L(T_epsilon)<=epsilon/2`. Then

\[
\Pr(\mathcal L_n(T_\varepsilon)>\varepsilon)
\le
\Pr\left(\sup_{t\le T_\varepsilon}|\mathcal L_n(t)-\mathcal L(t)|>\varepsilon/2\right)
\longrightarrow0.
\]

If `L(t)<=B exp(-ct)`, one can take `T_epsilon=max(0,c^-1 log(2B/epsilon))`. The same compact-time theorem controls every earlier time. This is approximation through a prescribed accuracy-dependent training horizon. It is not exact zero loss at a finite time, one width bound valid for every epsilon, or uniform approximation on `[0,infinity)`.

For mean-square loss `L=m^-1 sum_a r_a^2` and exact population prediction dynamics `dot f=-(2/m)K r`,

\[
\dot{\mathcal L}=-\frac{4}{m^2}r^TKr.
\]

A bound `r^TKr>=kappa ||r||_2^2` along the actual trajectory implies `dot L<=-(4 kappa/m)L`. A lower eigenvalue bound for the whole kernel is sufficient but stronger than needed. Neither property follows just from strict positive definiteness of the initialization kernel.

## 3. Data incompatibility obstructs fitting, not limit existence

For duplicate inputs with labels +1 and -1, any deterministic predictor takes the same value f on both. The average squared loss is

\[
\frac12[(f-1)^2+(f+1)^2]=1+f^2\ge1.
\]

This rules out fitting below that floor. A well-defined stationary limit at f=0 is completely compatible with it. Thus duplicate contradictory samples are not a counterexample to population-limit existence.

There are broader architecture-induced versions. If all hidden activations are odd, biases are absent and the readout is linear, induction gives `f(-x)=-f(x)` at every width and training time. Distinct antipodal samples with equal labels then have the same loss floor. If the first activation is even, the first hidden representations of x and -x coincide, so opposite labels cannot be fit. Neither implication means the data labels are necessarily wrong: the architecture may impose an inappropriate symmetry. Ordinary biases or a nonodd/non-even activation can change that expressivity restriction, but doing so defines a different model and must be stated.

Likewise, a deep linear network is still linear in its input. Arbitrary finite labels need not lie in its realizable prediction subspace. A global population dynamics theorem for arbitrary data, if available, would not automatically be a zero-loss theorem for arbitrary labels.

## 4. Why a tiny bounded nonlinear offset helps one label but strains contrasts

Suppose the top hidden activation obeys `|phi(z)-c|<=a` at every z, and two limiting predictions use the same trained readout A. If their labels are +1 and -1 and both prediction errors are at most epsilon<1, then

\[
2(1-\varepsilon)
\le |f_+-f_-|
=|\mathbb E[A(H_+-H_-)]|
\le \|A\|_2\|H_+-H_-\|_2
\le 2a\|A\|_2.
\]

Therefore `||A||_2 >= (1-epsilon)/a`. A positive constant offset can fit the common-label mode without this inverse-nonlinearity cost, but it cancels exactly from the contrast. This elementary representation bound explains one mechanism behind the different proof conditioning of equal-label and opposite-label constructions. It is not an impossibility theorem: the needed readout norm is finite at each fixed a>0, and it neither forces concentration nor prohibits a population limit.

An angular-separation restriction alone does not eliminate this particular inverse-amplitude bound. Conversely, a nonzero raw-input Gram eigenvalue cannot by itself control a trained nonlinear contrast. The appropriate quantities must be justified for the actual feature evolution.

## 5. Four asymptotic axes and two different meanings of universality

A theorem for every separately fixed depth L does not imply a joint limit with L=L_n tending to infinity. A theorem for every separately fixed finite dataset does not imply an input-population limit with sample count m=m_n growing. Constants, topology, initialization laws and residual-network scaling may all change along those limits. Compact training-time convergence is yet another quantifier, and the accuracy-dependent final training horizon is another operation.

“Universal” can mean deterministic and independent of the particular Gaussian initialization realization within a fixed model; it need not mean independent of architecture, activation, data distribution, optimizer or initialization ensemble. Such broader universality requires a separate theorem.

## 6. What an eventual generalization explanation still needs

The deterministic limiting training flow may select a unique representation for the specified random initialization law while having no proved population-risk guarantee. Matching a finite list of training predictions does not control predictions away from that list. An informative extension needs passive test-input/representation observables, a legitimate data-generating distribution or task structure, and a link from the selected representation to test risk. A sample-population limit is one possible organization, not a prerequisite for every finite-sample generalization theorem.

The energy-dissipation identity of gradient flow is not, by itself, a reason its features generalize: a steepest-descent or minimum energy-dissipation variational characterization can be shared by objectives that generalize poorly. The needed new content is a task-relevant bias among fitting solutions, expressed in the derived geometry and connected to statistical risk.

No blanket assertion that these programs are absent from all literature is justified here. The primary-literature audit must delimit established results and the remaining architecture/scaling-specific novelty.
