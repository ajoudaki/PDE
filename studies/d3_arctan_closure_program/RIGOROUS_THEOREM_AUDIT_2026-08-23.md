# Rigorous theorem audit: DMFT, Tensor Programs, and GFOM

**Audit date:** 23 August 2026.  Only authoritative full texts were used for
the hypothesis checks below.

## Bottom line

The statement “DMFT has no rigorous mathematics at all” is too broad.  There
are rigorous theorems called DMFT.  The project-relevant conclusion is
nevertheless the same: **no located rigorous DMFT theorem can be invoked for
the frozen three-hidden-layer feature-learning flow.**  Tensor Programs III
does rigorously identify every fixed finite Euler program, but supplies no
uniform-in-mesh convergence or tail theorem.  All remaining continuous-time
work is new mathematics.

## 1. Rigorous DMFT results and their mismatch

Celentano--Cheng--Montanari,
[*The high-dimensional asymptotics of first order methods with random
data*](https://arxiv.org/abs/2112.07572), proves a genuine continuous-time
DMFT theorem.  Its finite flow has the form

\[
 \dot\theta^t=-\theta^t\Lambda_t^{\mathsf T}
 -\delta^{-1}X^{\mathsf T}\ell_t(X\theta^t;z),
\]

with one iid sub-Gaussian design matrix \(X\), a fixed finite channel
dimension \(k\), and a row-separable \(\ell_t\).  Assumption 1 requires
\(\ell_t\) and its Jacobian to be globally Lipschitz uniformly on the compact
time interval.  Its Theorems 1--2 prove well-posedness of the associated
response/covariance system and empirical path convergence.

The frozen network is not a specialization: it has two independent Gaussian
operators, alternates both orientations of each operator, updates both
operators by adaptive low-rank terms, and contains empirical Gram channels.
The middle map \(R_2d(Z_2)\) also has no width-independent global Jacobian
bound on the energy class.  Encoding all of that as a fixed-dimensional
row-separable \(\ell_t\) would itself require the missing theorem.

Gerbelot--Troiani--Mignacco--Krzakala--Zdeborova,
[*Rigorous dynamical mean field theory for stochastic gradient descent
methods*](https://arxiv.org/abs/2210.06591), is also rigorous, but treats
first-order algorithms driven by a Gaussian data/design matrix and obtains
the corresponding memory process.  It is not a theorem for multilayer
weight-matrix training with two reused Gaussian bulks.  Physics derivations
of multilayer training DMFT therefore remain heuristic for this contract.

Dandi--Gamarnik--Pernice--Zdeborova,
[*Rigorous Asymptotics for First-Order Algorithms Through the Dynamical
Cavity Method*](https://arxiv.org/abs/2603.14573), is a recent rigorous
formalization of the cavity argument, so the blanket statement that every
DMFT result is only physicists' formalism would be false.  Its exact API is
nevertheless too narrow here.  Definition 1.1 alternates one iid rectangular
matrix \(X\) and \(X^{\mathsf T}\), with coordinatewise functions
\(F_t,G_t\) of the finite field history.  Assumptions (A1)--(A4) require iid
sub-Gaussian entries, iid sub-Gaussian initialization, and a
width-independent Lipschitz constant.  Theorem 1.3 proves convergence of
Lipschitz empirical tests for each fixed integer horizon \(T\).

The proof's strongest relevant internal estimate, Theorem 2.7, says that for
each fixed \(t,m,p\) there is a width-independent derivative constant
\(\Gamma_{t,m,p}\).  The paper explicitly constructs it inductively from
constants at time \(t-1\) with potentially *larger* derivative and moment
orders; it gives no bound uniform when \(t=T/h\to\infty\).  Eliminating the
learned weights in the frozen model also produces adaptive empirical Gram
coefficients, which are global averaging gates rather than prescribed
coordinatewise \(F_t,G_t\), and there are two independent reused matrices.
Thus neither the headline theorem nor Theorem 2.7 is an invocation.  The
all-reaching graph expansion is useful proof inspiration for the new
multi-cavity estimate, but any mesh-uniform constants and empirical-gate
extension must be proved internally.

## 2. The Tensor Program theorem that really applies

The BP-like transpose theorem in Yang,
[*Tensor Programs II*](https://arxiv.org/abs/2006.14548), is not sufficient.
Its Definition A.3 requires transpose inputs to remain odd in an independent
readout and forward inputs not to depend on that readout.  Feature-learning
updates immediately violate those conditions; the paper itself says its
Master Theorem is false without the BP-like restriction.

The correct fixed-program invocation is Yang,
[*Tensor Programs III: Neural Matrix Laws*](https://arxiv.org/abs/2009.10685),
Theorem 2.10 and its self-parametrized pseudo-Lipschitz extension.  This is an
unrestricted NETSOR-transpose Master Theorem.  It represents every reused
matrix action as

\[
 Z^{Wx}=\widehat Z^{Wx}+\dot Z^{Wx},
\]

where the first term belongs to a joint Gaussian family and the ZDot term is
the exact forward/transpose correlation correction, expressed through
expected symbolic derivatives.  It covers the two Gaussian matrices, their
reused transposes, coordinatewise arctangent gates, and the finitely many
empirical scalar channels at every **fixed** Euler mesh.

It does not cover a number of program lines tending to infinity and gives no
tail constant uniform in the mesh.  Applying it separately for each fixed
mesh and then silently sending the mesh to zero would be an invalid exchange
of limits.

The full-text tail audit is sharper.  Theorem 2.10 gives almost-sure
convergence of empirical averages for each fixed finite program and
polynomially bounded test, but no rate or constant uniform in program length.
Theorem A.5 obtains a fixed-coordinate law only through bounded continuous
tests.  Theorem A.2 upgrades convergence in mean only for quadratically
bounded tests when every nonlinearity is linearly bounded.  Conjecture A.4
explicitly leaves the corresponding general polynomial-tail upgrade open.
Theorem E.15 avoids a rank-stability assumption for pseudo-Lipschitz programs,
but remains a fixed-program theorem; its proof discussion emphasizes that
covariance convergence alone need not give pseudoinverse convergence.

This limitation is substantive, not merely absent bookkeeping.  For two
bounded histories \(X_1=\arctan(hG)\) and
\(X_2=\arctan(2hG)\),

\[
 \frac{X_1-X_2/2}{h^3}\longrightarrow G^3
\]

in every fixed \(L^p\).  Feeding the corresponding normalized Gaussian
forward combination back through the same transpose makes the exact ZDot
term converge to \(G^3/\sqrt{15}\), with moments of order \(p^{3/2}\), even
though both histories are bounded and the forward combination is Gaussian.
Thus no generic mesh-uniform \(Cp\) transpose-response bound follows from the
Master Theorem or bounded arctan features.  The canonical training orbit must
be proved not to align with such collapsing covariance directions.

## 3. Other rigorous first-order-method machinery

Han,
[*Entrywise dynamics and universality of general first order
methods*](https://arxiv.org/abs/2406.19061), gives rigorous nonasymptotic
leave-\(k\)-out and entrywise state-evolution estimates, including some
polylogarithmically growing iteration counts.  Two matrices and transpose
reuse can be embedded into a block Gaussian matrix.  The direct theorem still
does not apply because its update functions are deterministic and
row-separable, whereas eliminating the learned weights creates adaptive
empirical Gram gates.  Its generic moment constants also grow with the
iteration count.  The proof is valuable inspiration for a new weighted
empirical-channel leave-out lemma, not an API-level invocation.

Bao--Han--Xu,
[*A leave-one-out approach to approximate message
passing*](https://arxiv.org/abs/2312.05911), supplies another rigorous
leave-out template, but its cancellations and recursion are specific to AMP.
The frozen gradient flow has no verified reduction to that AMP class.

Berthier--Montanari--Nguyen,
[*State Evolution for Approximate Message Passing with Non-Separable
Functions*](https://arxiv.org/abs/1708.03950), permits uniformly Lipschitz
nonseparable denoisers for Gaussian AMP.  This is potentially relevant to the
finite-rank empirical Gram channels, but it is a fixed-iteration AMP theorem.
No verified reduction simultaneously preserves this network's exact
gradient updates, two reused matrices, and a mesh length tending to infinity.

Nguyen--Pham,
[*A Rigorous Framework for the Mean Field Limit of Multilayer Neural
Networks*](https://arxiv.org/abs/2001.11443), proves a quantitative
multilayer neuronal-embedding limit, but its fully connected forward pass
uses the law-of-large-numbers scaling
\(n^{-1}\sum_j w_{ij}\phi(h_j)\) with order-one sampled weights.  The frozen
model uses the central-limit/maximal-update scaling
\(n^{-1/2}\sum_j W_{ij}\phi(h_j)\), whose quenched Gaussian bulk survives and
is reused through its transpose.  Rewriting one as the other makes the
paper's uniformly Lipschitz layer maps depend on width.  Its theorem is
therefore not an invocation for this contract.

Chen--Yang--Zhao--Gu,
[*Global Convergence and Rich Feature Learning in L-Layer Infinite-Width
Neural Networks under muP Parametrization*](https://arxiv.org/abs/2503.09565),
also does not supply a growing-time limit.  Its infinite-width variables are
the fixed-SGD-iteration Tensor Program variables inherited from Yang--Hu: the
paper assumes the limit at an integer iteration and proves feature linear
independence and the conditional statement that any convergent infinite-width
training sequence is globally optimal.  It does not prove uniform finite-width
convergence as the number of steps diverges, continuous gradient-flow
well-posedness, or raw tangent-kernel convergence.  The activation hypotheses
and the depth generality therefore do not bridge the present mesh limit.

## 4. Path-space large-deviation machinery

Rigorous path-space large-deviation results for Gaussian random networks do
exist, but the closest APIs use nondegenerate dynamical noise in an essential
way.  Cabana--Touboul,
[*Large deviations for randomly connected neural networks: II.
State-dependent interactions*](https://arxiv.org/abs/1601.00985), studies

\[
 dX_i=\left(f(X_i)+\sum_jJ_{ij}b(X_i,X_j)\right)dt
       +\lambda\,dW_i,
\]

with bounded interaction \(b\), \(\lambda>0\), and a short-time condition
\(2\sigma^2\|b\|_\infty^2T/\lambda^2<1\).  The proof obtains the rate function
by a Girsanov density relative to the independent Brownian system.  Setting
\(\lambda=0\) is therefore not a specialization: it destroys both the
Radon--Nikodym argument and the allowed time interval.  The theorem also has
one static coupling family and no reused transpose or trained matrix.

Ben Arous--Guionnet,
[*Symmetric Langevin spin glass dynamics*](https://cims.nyu.edu/~benarous/Publications/benarous_31.pdf),
likewise proves a path empirical-measure large-deviation upper bound and law
of large numbers for noisy symmetric Langevin dynamics in a short-time or
high-temperature regime.  Its Brownian reference dynamics and symmetric
spin-glass Hamiltonian are not the two-bulk deterministic gradient flow here.
Related random-neural-network LDPs have the same stochastic-reference and
bounded-interaction structure.

Gaussian log-Sobolev does apply to the finite raw disorder, but it is a
reduction rather than a solution.  The Aida--Stroock moment form gives

\[
 \|F-\mathbb EF\|_p\lesssim\sqrt p\,
 \|\|\nabla F\|_2\|_p.
\]

For the adaptive middle query its gradient is the same column/full-flow
response isolated in the Malliavin reduction.  A pathwise bound on this
Jacobian sees \(\|B_3\|_\infty\) and \(\|B_2\|_\infty\); already the Gaussian
output maximum grows as \(\sqrt{\log n}\).  Otto--Reznikoff type weak-
interaction log-Sobolev criteria do not help: they require a smooth positive
Gibbs density, uniform conditional LSIs, and absolute mixed-Hessian bounds,
whereas the trajectory law is a singular deterministic pushforward and the
absolute influence sum loses the random cancellations.  Consequently a
transport/LSI proof must first establish the same reachable weighted-response
delocalization that is currently missing.

These papers remain useful proof inspiration: they show how an auxiliary
path law can retain Gaussian memory while a final state description is
Markovian in a richer immutable source.  They cannot be invoked, and their
conclusions for weak empirical-path tests would still need a separate
exponential-tail/raw-square upgrade.  A deterministic zero-noise contraction
principle for the present adaptive transpose flow would be new mathematics,
not a corollary of the cited LDPs.

Exact adaptive Gaussian conditioning gives a sharper positive reduction.
If \(X\) and \(B\) are the previously revealed right and left query spaces
for one raw bulk, then, using orthogonal projections rather than an unstable
Gram inverse,

\[
 \Gamma\mid\mathcal F
 \stackrel d=M+P_B^\perp\widetilde\Gamma P_X^\perp .
\]

The innovation in the next coordinate of \(\Gamma^*b\) is conditionally
Gaussian with variance at most \(\|b\|_n^2\), hence has a \(C\sqrt p\) bound.
Only the predictable regression \((M^*b)_j\) remains.  Bayati--Montanari and
nonseparable AMP control its analogue at each fixed iteration through
Gaussian conditioning and Onsager terms; no audited result makes that
regression uniform when the query history has length \(T/h\) and successive
directions become nearly collinear.  The required new statement is a
mesh-uniform causal-regression/weighted-response lemma, not a fresh-noise
estimate.

## 5. Consequence for the proof strategy

The only external theorem currently invoked in the convergence backbone is
the unrestricted Tensor Programs III Master Theorem, and only at fixed mesh.
The continuous bridge must prove one of the following internally:

1. a uniform-in-mesh exponential tail for the limiting TP ZDot middle query;
2. an equivalent finite-width signed two-sided cavity/weighted-interaction
   estimate; or
3. a different fully proved stability mechanism that passes the raw square
   energies.

DMFT formulas may be ignored without losing a theorem.  The newly rigorous
dynamical-cavity derivative expansion may be mined as a combinatorial proof
template, but no DMFT result is cited to discharge an obligation.  The only
external invocation in the convergence backbone remains Tensor Programs III
at a fixed finite mesh.

## 6. Sequential deep mean field is a different limit, and its depth-three display is not proved

Sirignano--Spiliopoulos,
[*Mean Field Analysis of Deep Neural Networks*](https://arxiv.org/html/1903.04440v5),
is a genuine rigorous result for its principal two-hidden-layer model, but it
is not an API for the frozen contract.  The full text makes four decisive
distinctions explicit.

First, its network uses deterministic mean-field averages (N_\ell^{-1})
with order-one weights, whereas the frozen model has centered Gaussian
operator blocks with entries of variance (1/n) and simultaneous
fluctuation-scale forward/adjoint actions.  The paper itself contrasts its
(1/N) regime with (1/\sqrt N) regimes and says that the latter have a
different limit.

Second, Assumption 2.1 requires \(\sigma\in C_b^2\), compactly supported data,
compactly supported iid initial parameters, and continuous initialization
densities.  The bounded arctangent activation qualifies, but the frozen
Gaussian initialization does not satisfy the compact-support premise.

Third, the width limit is explicitly iterated:

\[
 \lim_{N_2\to\infty}\lim_{N_1\to\infty}g_t^{N_1,N_2}(x),
\]

with (N_1\to\infty) while (N_2) is fixed, followed by
(N_2\to\infty).  The first layer also supplies the SGD clock.  This peeling
removes precisely the simultaneous equal-width Gaussian feedback loop that
creates C-13.  It cannot be exchanged for the diagonal limit
(N_1=N_2=N_3=n\to\infty) without a uniformity theorem, and none is stated.

Fourth, Theorem 2.3 is a pointwise predictor convergence theorem for the
two-hidden-layer model.  Section 4.2 writes a candidate three-hidden-layer
system only after saying one *expects* that iterated limit, and then states
that the rigorous proof for the three-layer form is left to the reader.
Thus even in the paper's own sequential, compactly supported (1/N) regime,
the depth-three display is not a proved theorem in that source.  It also
asserts neither convergence of the raw tangent kernel nor convergence in the
frozen current-action/nuclear operator topology.

The paper's proof architecture remains informative: parameterize limiting
weights by their initial labels, obtain uniform bounds from compact support,
couple the next-layer particles, and close a Gronwall estimate before peeling
the next width.  Applying that architecture here would require proving
uniform-in-outer-width bounds strong enough to diagonalize the iterated
limits.  For the frozen Gaussian feature flow, that uniformity is again the
no-condensation/cavity estimate C-13.  The result is therefore a useful
comparison and an architectural alternative, not a shortcut or an invoked
theorem for this contract.
