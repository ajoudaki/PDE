# Three hidden tanh layers with two coupled response-memory operators

Date: 2026-09-24. Status: exact finite-dimensional construction and algebraic
derivation for an internal study extension; empirical accuracy, global
convergence, and width-uniform estimates remain separate claims. This is
collaborative theory work, not an independent promotion review.

The authorized experiment compares the dense network with the chronological
shifted-Legendre closure at P=1,2,3 and width n=4096 on circle data. The
identities below hold for any finite width, input dimension, uniformly
weighted finite training set, and integer P>=1. They do not select the data,
labels, time horizon, numerical solver, or empirical acceptance thresholds;
those belong to the experiment protocol.

The initial derivation's scientific inputs were restricted to this study's `MOMENT_CONSTRUCTION.md`,
`RATIONAL_CANDIDATE_ROUTE.md`, `orthogonal_moment_engine.py`, `moment_engine.py`,
and `docs/NOTATION.md`, plus the supervisor's assignment and initialization
clarification. The older rational-gate route supplies model conventions and
the response-lift idea; the present construction uses the chronological
orthogonal moments, with fixed prefix length one, from the construction note
and orthogonal engine. No other study, external scientific source, or
experimental output was read.

A subsequent scoped audit read the complete ten assigned mathematical
progression and correction reports. `DEEP_CIRCLE_CONTEXT_DIGEST.md` records
their exact coverage, hashes, inherited numerical caveats, and correspondence
with this derivation. It required no change to the equations below.

## 1. Exact model and scaling

Let U_a=x_a/sqrt(d), a=1,...,M, with x_a in R^d. The matrices W1 in
R^(n by d), W2,W3 in R^(n by n), and the stored readout c in R^n define

\[
 z_{1,a}=W_1U_a,\quad h_{1,a}=\tanh z_{1,a},\qquad
 z_{2,a}=W_2h_{1,a},\quad h_{2,a}=\tanh z_{2,a},
\]
\[
 z_{3,a}=W_3h_{2,a},\quad h_{3,a}=\tanh z_{3,a},\qquad
 f_a=c^Th_{3,a}/n,\quad r_a=f_a-y_a,\quad
 \mathcal L=M^{-1}\sum_a r_a^2.
\]

There are three hidden layers and four parameter blocks. In particular,
W3 is now the second internal matrix; the readout is c=W4.

The original initialization conventions give independent Gaussian entries

\[
 W_1(0)_{ij}\sim N(0,1),\qquad
 W_2(0)_{ij},W_3(0)_{ij}\sim N(0,1/n),\qquad
 c_i(0)\sim N(0,1/n^2).
\]

Thus the first matrix is not divided by sqrt(n), and the stored readout is
drawn as `standard_normal(n)/n`. The prescribed new draw order is
`W1, W20, W30, c` from NumPy `default_rng(20260920)`. A common seed alone does
not give matched initial networks if implementations use different draw order.

Write activation derivatives explicitly; for tanh they equal 1-h^2
componentwise. The backward recurrence is

\[
 \delta_{3,a}=c\odot(1-h_{3,a}^2),\qquad
 \delta_{2,a}=(1-h_{2,a}^2)\odot W_3^T\delta_{3,a},\qquad
 \delta_{1,a}=(1-h_{1,a}^2)\odot W_2^T\delta_{2,a}.
\]

These are n times the derivatives of f with respect to the corresponding
preactivations; the residual is not included in delta. Differentiating the
loss therefore gives

\[
 \nabla_{W_1}\mathcal L=\frac2{Mn}\sum_a r_a\delta_{1,a}U_a^T,
 \qquad
 \nabla_{W_\ell}\mathcal L=\frac2{Mn}\sum_a
 r_a\delta_{\ell,a}h_{\ell-1,a}^T\quad(\ell=2,3),
\]
\[
 \nabla_c\mathcal L=\frac2{Mn}\sum_a r_ah_{3,a}.
\]

For the block mobilities (n,1,1,n), the exact dense gradient flow is

\[
 \dot W_1=-\frac2M\sum_a r_a\delta_{1,a}U_a^T,\qquad
 \dot W_\ell=-\frac2{Mn}\sum_a
 r_a\delta_{\ell,a}h_{\ell-1,a}^T\quad(\ell=2,3),\qquad
 \dot c=-\frac2M\sum_a r_ah_{3,a}.
 \tag{1}
\]

The factors of n follow from the output normalization and mobilities,
independently of the initialization variances.

## 2. Two chronological moment pairs on one activity interval

Every object from this point through section 6 belongs to the surrogate's
current trajectory unless explicitly described as dense. Let

\[
 \rho^2=M^{-1}\sum_a r_a^2,\qquad
 \dot s=\rho,\quad s(0)=0,\qquad L=1+s.
\]

Here L is the history-interval length, not the number of hidden layers.
On an interval with rho>0 define

\[
 u_{\ell,a}=r_a\delta_{\ell,a}/\rho,\qquad \ell=2,3.
\]

On the virtual prefix 0<=tau<=1, set u_{ell,a}(tau)=0 and
h_{ell-1,a}(tau)=h_{ell-1,a}(0). For tau=1+s(t), use the current network
responses. The prefix contributes exactly zero to each learned-matrix
history integral. The backward history may jump at tau=1; no continuity
across this artificial boundary is assumed.

Let ell_k(v) be the shifted Legendre polynomial of degree k on [0,1],
normalized by ell_k(1)=1 and

\[
 \int_0^1\ell_j(v)\ell_k(v)\,dv=\frac{\mathbf1_{j=k}}{2k+1}.
\]

One definition is the Rodrigues formula
ell_k(v)=(1/k!) d^k/dv^k [v^k(v-1)^k]. Repeated integration by parts proves
orthogonality because lower-degree polynomials have zero kth derivative and
all boundary terms vanish. For the diagonal norm it gives
((2k)!/(k!^2)) integral_0^1 v^k(1-v)^k dv=1/(2k+1).

For each link ell=2,3, sample a, and k=0,...,P-1 retain

\[
 A_{\ell,k,a}=\int_0^L u_{\ell,a}(\tau)\ell_k(\tau/L)\,d\tau,
 \qquad
 B_{\ell,k,a}=\int_0^L h_{\ell-1,a}(\tau)\ell_k(\tau/L)\,d\tau.
 \tag{2}
\]

The moving interval uses the same clock L for both links. The four collections
A2,B2,A3,B3 are distinct. In particular, B3 contains second-layer responses,
whereas A2 contains second-layer backward signals; neither can replace the
other merely because both are neuron vectors in layer 2.

To differentiate (2), use

\[
 v\ell_k'(v)=k\ell_k(v)+\sum_{j<k}(2j+1)\ell_j(v).
 \tag{3}
\]

The coefficient of ell_k is k by the leading term. For j<k, integration by
parts gives integral_0^1 v ell_k' ell_j=1, since the boundary at 1 is one
and integral ell_k(ell_j+v ell_j')=0 by orthogonality. Division by the norm
of ell_j proves the remaining coefficients in (3). The endpoint source in
the moving integral is rho u=r delta, so the operational equations require
no division by rho:

\[
 \dot A_{\ell,k,a}=r_a\delta_{\ell,a}
 -\frac\rho L\left(kA_{\ell,k,a}
       +\sum_{j<k}(2j+1)A_{\ell,j,a}\right),
\]
\[
 \dot B_{\ell,k,a}=\rho h_{\ell-1,a}
 -\frac\rho L\left(kB_{\ell,k,a}
       +\sum_{j<k}(2j+1)B_{\ell,j,a}\right).
 \tag{4}
\]

Initialize A=0, B_{ell,0,a}=h_{ell-1,a}(0), and B_{ell,k,a}=0 for k>0.
For any one moment array T and its endpoint source b, the orders needed in
the experiment are exactly

\[
 \dot T_0=b,\qquad
 \dot T_1=b-(\rho/L)(T_1+T_0),\qquad
 \dot T_2=b-(\rho/L)(2T_2+T_0+3T_1).
\]

Truncate this list after its first P equations. These transport equations
are exact moment identities along the surrogate, not a fitted temporal
Taylor expansion.

## 3. Reconstruction and coupled forward/backward actions

For ell=2,3 define

\[
 K_\ell=-\frac2{ML}\sum_{a,k<P}(2k+1)
                A_{\ell,k,a}B_{\ell,k,a}^T,
 \qquad
 \widehat W_\ell=W_{\ell0}+K_\ell/n.
 \tag{5}
\]

For one link and sample, its degree-(P-1) history projection is
u_P(tau)=L^(-1) sum_k (2k+1) A_k ell_k(tau/L), and similarly for h_P.
Orthogonality gives

\[
 \int_0^L u_P(\tau)h_P(\tau)^T\,d\tau
   =\frac1L\sum_{k<P}(2k+1)A_kB_k^T,
\]
\[
 \int_0^L uh^T\,d\tau
 -\int_0^L u_Ph_P^T\,d\tau
   =\int_0^L(u-u_P)(h-h_P)^T\,d\tau.
\]

The mixed projection/residual terms vanish entrywise. Thus (5) replaces each
exact learned-weight history integral by its projected cross moment; its
discarded part is the response covariance in the omitted history modes.
This identity concerns the surrogate's own histories, so it does not assume
that the moments track a precomputed dense trajectory.

Use these same reconstructed matrices in both directions:

\[
 h_1=\tanh(W_1U),\quad
 h_2=\tanh(\widehat W_2h_1),\quad
 h_3=\tanh(\widehat W_3h_2),
\]
\[
 \delta_3=c\odot(1-h_3^2),\quad
 \delta_2=(1-h_2^2)\odot\widehat W_3^T\delta_3,\quad
 \delta_1=(1-h_1^2)\odot\widehat W_2^T\delta_2.
 \tag{6}
\]

The outer equations for W1 and c remain (1), evaluated at (6). All sources
in (4) use these current responses. No exact dense trajectory supplies
moments, coefficients, or forcing.

For a current vector v in the preceding layer, the learned forward action is

\[
 (K_\ell/n)v=-\frac2{ML}\sum_{a,k<P}(2k+1)
 A_{\ell,k,a}\frac{B_{\ell,k,a}^Tv}{n}.
\]

The reverse action exchanges A and B in precisely this expression. Hence,
for every pair v,w, w^T(K_ell/n)v=((K_ell/n)^T w)^Tv exactly. The initialized
actions likewise use W_{ell0} and its actual transpose. Independent reverse
maps or separately recomputed reverse memories violate the intended model.

In the population-state notation, m1 can hold W1,h1,B2; m2 can hold h2,A2,B3;
and m3 can hold c,h3,A3. The shared scalars and current normalized pairings
are Q. This is one coupled autonomous state; the two memory operators are
not separately trained networks.

## 4. Rational response lift and explicit evaluation order

Retain h1,h2,h3 and rho as dynamic training-state variables, initialized by
the exact tanh forward pass and residual RMS. For each internal link,
differentiate (5) using the already computed moment velocities:

\[
 \dot{\widehat W}_\ell=-\frac2{MnL}
 \sum_{a,k<P}(2k+1)
 \left[\dot A_{\ell,k,a}B_{\ell,k,a}^T
       +A_{\ell,k,a}\dot B_{\ell,k,a}^T
       -\frac\rho L A_{\ell,k,a}B_{\ell,k,a}^T\right].
 \tag{7}
\]

Propagate the response derivatives in forward layer order:

\[
 \dot h_{1,a}=(1-h_{1,a}^2)\odot(\dot W_1U_a),
\]
\[
 \dot h_{2,a}=(1-h_{2,a}^2)\odot
  (\dot{\widehat W}_2h_{1,a}+\widehat W_2\dot h_{1,a}),
\]
\[
 \dot h_{3,a}=(1-h_{3,a}^2)\odot
  (\dot{\widehat W}_3h_{2,a}+\widehat W_3\dot h_{2,a}),
\]
\[
 \dot f_a=(\dot c^Th_{3,a}+c^T\dot h_{3,a})/n,
 \qquad
 \dot\rho=\frac1{M\rho}\sum_a r_a\dot f_a.
 \tag{8}
\]

There is no simultaneous implicit solve. At any ODE stage:

1. Form both current factor operators from A,B,L; use the stored responses
   to compute f,r, then delta3,delta2,delta1 in reverse layer order.
2. Compute W1dot,cdot,Ldot and all four moment-array velocities by (1),(4).
3. Form both operator velocities by (7), applied through factors.
4. Compute h1dot,h2dot,h3dot,fdot,rhodot by (8).

In particular, B3dot depends on current h2, not h2dot; A2dot depends on
current delta2, not delta2dot. Although delta2 uses the current upper operator,
it does not use that operator's velocity. This removes the apparent cycle.
The current and derivative factor actions must use the same ODE-stage state;
updating one moment pair in place before evaluating the other changes the
numerical method and can change the equations.

Every RHS expression is rational on rho>0,L>0. Tanh and square root are
needed at initialization and for independent consistency diagnostics or new
query inputs. Ordinary tanh recomputation at every training RHS instead
defines the equivalent nonlifted mathematical closure, but its evaluated
RHS is not rational.

The lift preserves h1=tanh(W1 U), h2=tanh(What2 h1), and
h3=tanh(What3 h2) in continuous time. Indeed, for each layer the right-hand
side is exactly (1-h^2) zdot for its actual differentiated preactivation.
If q=tanh(z), the discrepancy obeys
(h-q)dot=-(h+q) zdot (h-q), componentwise. A zero initial discrepancy stays
zero on every interval of existence. Also

\[
 \frac d{dt}\left(\rho^2-M^{-1}\sum_a r_a^2\right)=0.
\]

If redundant compatibility coordinates C_k are retained, initialize C_k=1
and evolve C_kdot=rho; then C_k-L=0 is another exact invariant. They are not
needed by (5). At an exactly consistent zero residual state, all physical
and raw-moment velocities vanish. Define the lifted boundary vector field
to be zero there rather than evaluating the expression for rhodot.

These are continuous-time invariants. A numerical integrator must measure
their drift at every hidden layer and in rho, especially near zero residual.
Rationality does not prevent denominator conditioning or imply stability.

For derivative-memory interpretation, let Psi_k(v)=integral_0^v ell_k(w)dw.
Assuming absolutely continuous activity histories after the prefix,
integration by parts gives, with v=(1+sigma)/L,

\[
 B_{\ell,k,a}=L\mathbf1_{k=0}h_{\ell-1,a}(s)
 -L\int_0^s\Psi_k((1+\sigma)/L)
                  \frac{d h_{\ell-1,a}}{d\sigma}\,d\sigma,
\]
\[
 A_{\ell,k,a}=L\mathbf1_{k=0}u_{\ell,a}(s)
 -L\Psi_k(1/L)u_{\ell,a}(0)
 -L\int_0^s\Psi_k((1+\sigma)/L)
                  \frac{d u_{\ell,a}}{d\sigma}\,d\sigma.
\]

The middle term in the second identity is the initial jump from zero on the
prefix. These are equivalent coordinates, requiring no higher derivatives.
The raw equations (4) avoid subtractive cancellation and division by rho
in the backward-source evolution.

## 5. Exact two-link closure defect

Define current endpoint projections

\[
 u_{\ell,P,a}=\frac1L\sum_{k<P}(2k+1)A_{\ell,k,a},\qquad
 h_{\ell-1,P,a}=\frac1L\sum_{k<P}(2k+1)B_{\ell,k,a}.
\]

For one link and sample suppress their indices and set
J_P=L^(-1) sum_{k<P}(2k+1) A_k B_k^T. Applying (4), the contributions from
the moment endpoints are rho(u h_P^T+u_P h^T). The denominator derivative,
the k A_k and k B_k terms, and both triangular sums together equal

\[
 -\frac\rho{L^2}\sum_{j,k<P}(2j+1)(2k+1)A_jB_k^T
 =-\rho u_Ph_P^T.
\]

For the diagonal terms this uses 1+2k=2k+1; the two triangular sums provide
the two off-diagonal halves. Therefore

\[
 \dot J_P=\rho\{u h_P^T+u_Ph^T-u_Ph_P^T\}
 =\rho\{u h^T-(u-u_P)(h-h_P)^T\}.
\]

Substitution into (5) proves, separately for ell=2,3,

\[
 E_\ell:=\dot{\widehat W}_\ell
       +\frac2{Mn}\sum_a r_a\delta_{\ell,a}h_{\ell-1,a}^T
 =\frac2{Mn}\sum_a
    (r_a\delta_{\ell,a}-\rho u_{\ell,P,a})
    (h_{\ell-1,a}-h_{\ell-1,P,a})^T.
 \tag{9}
\]

The sign is positive. Its rank is at most M for each link, even though each
learned increment has rank at most MP. Initially h_{ell-1,P}=h_{ell-1}(0),
so E2(0)=E3(0)=0 identically for every realization and every P>=1. This
certifies matching initial physical weight velocities, not positive-time
trajectory accuracy.

On its invariant manifold, the reconstructed physical network satisfies
the original dense vector field evaluated at its own weights, plus
(0,E2,E3,0). There is no additional outer-weight or response approximation.
The defect is not the derivative difference between separately evolved dense
and surrogate trajectories: that difference also contains propagation through
the nonlinear vector field. The two defects need not evolve independently,
since every current source uses both reconstructed hidden matrices.

For example, at a fixed physical state the additional output velocity is

\[
 \dot f_a\big|_{\rm defect}=\frac1n\left(
  \delta_{2,a}^T E_2h_{1,a}+\delta_{3,a}^T E_3h_{2,a}\right),
\]

and hence the exact loss identity is

\[
 \dot{\mathcal L}=-n\|\nabla_{W_1}\mathcal L\|_F^2
 -\|\nabla_{W_2}\mathcal L\|_F^2
 -\|\nabla_{W_3}\mathcal L\|_F^2
 -n\|\nabla_c\mathcal L\|_2^2
 +\langle\nabla_{W_2}\mathcal L,E_2\rangle_F
 +\langle\nabla_{W_3}\mathcal L,E_3\rangle_F.
\]

Loss monotonicity of a truncated surrogate is therefore not automatic.
Writing e_u=u-u_P and e_h=h-h_P, (9) also gives the explicit bound

\[
 \|E_\ell\|_F\le\frac{2\rho}{M}\sum_a
 \frac{\|e_{u,\ell,a}\|_2}{\sqrt n}
 \frac{\|e_{h,\ell-1,a}\|_2}{\sqrt n}.
\]

This is an error-production identity and estimate. Tracking the exact dense
flow further needs stability estimates for the coupled network. No rate in
P, global tracking statement, or width-uniform bound is derived here.

## 6. State size, checks, and claim limits

The minimal lifted moving state contains

\[
 nd+n+4PnM+3nM+2
\]

scalars: W1,c; A2,B2,A3,B3; h1,h2,h3; s,rho. Optional shared C_k add P
redundant scalars. The two fixed initialized matrices require 2n^2 scalars
and retain dense forward and transpose actions. The learned operators each
have rank <=MP and operator velocities in (7) admit rank <=2MP factorizations.
Their application costs O(nMP) per vector, or O(nPM^2) for an M-column
response batch. This is compression of moving learned state; it does not
remove the stored initialized matrices or their multiplication cost.

Implementation checks appropriate to this derivation are: dense gradients
against independent automatic differentiation with the stated mobilities;
initial matching for all four physical blocks; both transpose identities;
both derivative-factor identities; both defects (9); every lifted response
invariant; rho and optional C-L invariants; shared initialization across P;
and a numerical step-refinement comparison before attributing discrepancies
to the closure. The supervisor and implementation agent own their execution
and evidence; this derivation itself contains no executed experiment.

The exact algebra supports a finite autonomous construction and identifies
its omitted covariance at both hidden links. Tests at P=1,2,3 can support or
reject those tested compression levels over the recorded finite horizon.
They cannot prove hierarchy convergence, all-time validity, a population
limit, or width-independent complexity. In particular, adding the third
hidden layer introduces coupled error propagation, even though the
linkwise moment and defect identities keep the same form.

## Provenance and check scope

Author: scoped theory agent `/root/deep_derivation`. Required process inputs
read: `RESEARCH_WORKFLOW.md`; `solve-math-rigorously/SKILL.md`;
`investigate-conjectures/SKILL.md` and its research-contract, evidence-ledger,
and adversarial-audit references. No experiment was run by this author.
The argument was checked algebraically against the allowed original
implementation, including dimensions, all factors of n, transpose use,
P=1,2,3 transport coefficients, initialization, the zero-residual boundary,
and the product-rule defect. This records an author check, not an independent
review or repository-level internally-checked designation.

Read-version SHA256 hashes:

| Input | SHA256 |
|---|---|
| MOMENT_CONSTRUCTION.md | 5d8bf7fb354fbdef138676ca0ee5d59799a9032e6f6f531ca4650c8e0e5a9025 |
| RATIONAL_CANDIDATE_ROUTE.md | 6f66e47ff2ac4017f538f4a46dcb7c75cea41dba79ffecbb64404fef57a19c51 |
| orthogonal_moment_engine.py | 32f80cf35c44b5015821fa8c8726bb8ff3bc6f7eb3e1b7abe9ee62ea8f529909 |
| moment_engine.py | ebf39cf377f1eb0f5dea64fa1ab946fddcb11a662b2368472017abef9237acd9 |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |

HEAD before writing: `06faa62043f573b8313370c4eb020ed27240ada1`.
The shared index was empty. Existing concurrent changes were left untouched;
this agent writes only this derivation file and performs no Git mutation.
