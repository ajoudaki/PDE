# A conditional present-state realization of two-layer response memory

Scope: independent, theory-only derivation from the supervisor's supplied
two-layer equations and, in a subsequent message, the exact fixed-program
Gaussian source rule from established docs/special_data_limits.md III.F.
No other study, external source, experiment, or fitted filter is used. This
is an internally derived candidate, not established repository theory.
The decisive unresolved identification is stated below.

## 1. Conclusion and claim level

A finite present-state reduction follows if the **entire two-time covariance
and causal-response system has a finite, positive, causally generated state
realization**, and the realization's coefficients are computable from the
current reduced population. A realization of the learned drift kernels alone
does not suffice. The auxiliary equations below are exact under this
assumption. The supplied equations do not establish the assumption or provide
its coefficient maps for generic two-layer tanh training.

The result is naturally a fixed number of state variables **per neuron**.
At infinite width, the current population law remains an infinite-dimensional
object. Obtaining a finite total-dimensional deterministic system requires a
separate finite moment closure, which is not assumed silently here.

## 2. Exact starting point and an aggregate interaction identity

Let expectations over the two normalized neuron populations be
\(\mathbb E_1,\mathbb E_2\). Write
\[
H_1=\tanh Z_1,\quad Z_1=W_1x/\sqrt d,\qquad
Z_2=W_2H_1,\quad H_2=\tanh Z_2,
\]
\[
f(x)=\mathbb E_2[cH_2(x)],\quad r(x)=f(x)-y(x),\quad
\Delta_2(x)=c\phi'(Z_2(x)),\quad
Q(x)=W_2^*\Delta_2(x),\quad
\Delta_1(x)=\phi'(Z_1(x))Q(x).
\]
Here \(\phi=\tanh\), and the adjoint uses the normalized population inner
products. The supplied gradient flow is
\[
\dot W_2=-2\mathbb E_a[r(a)\Delta_2(a)\otimes H_1(a)],\quad
\dot W_1=-2\mathbb E_a[r(a)\Delta_1(a)x_a/\sqrt d],\quad
\dot c=-2\mathbb E_a[r(a)H_2(a)].
\]
Thus, exactly,
\[
Z_2(t,x)=G_2(t,x)-2\int_0^t\mathbb E_a[
 r_s(a)\Delta_2(s,a)C_1(t,x;s,a)]\,ds,
\tag{1}
\]
\[
Q(t,x)=G_1(t,x)-2\int_0^t\mathbb E_a[
 r_s(a)H_1(s,a)C_2(t,x;s,a)]\,ds,
\tag{2}
\]
where
\[
G_2(t,x)=W_{20}H_1(t,x),\quad
G_1(t,x)=W_{20}^*\Delta_2(t,x),
\]
\[
C_1(t,x;s,a)=\mathbb E_1[H_1(t,x)H_1(s,a)],\quad
C_2(t,x;s,a)=\mathbb E_2[\Delta_2(t,x)\Delta_2(s,a)].
\]
These are uncentered second-moment kernels. In a valid Gaussian cavity
description they may be covariance kernels of centered cavity fields, with
the initialization variance and aspect-ratio factors determined by the
initialization convention. Those factors are not specified in the prompt.

There is also an exact equal-time identity. Put
\(K_0(x,a)=x\cdot x_a/d\), and abbreviate equal-time kernels by
\(C_V(t;x,a)=\mathbb E[V(t,x)V(t,a)]\). Differentiation gives
\[
\dot f_t(x)=-2\mathbb E_a[r_t(a)K_t(x,a)],
\tag{3}
\]
\[
K_t(x,a)=C_{H_2}(t;x,a)
 +C_{H_1}(t;x,a)C_{\Delta_2}(t;x,a)
 +K_0(x,a)C_{\Delta_1}(t;x,a).
\tag{4}
\]
Indeed, the \(\dot c\) term gives the first summand. In
\(\mathbb E_2[\Delta_2(x)\dot Z_2(x)]\), the term
\(\dot W_2H_1(x)\) gives the second summand. For the remaining term, adjointness
gives
\[
\mathbb E_2[\Delta_2(x)W_2\dot H_1(x)]
 =\mathbb E_1[Q(x)\phi'(Z_1(x))\dot Z_1(x)]
 =\mathbb E_1[\Delta_1(x)\dot Z_1(x)],
\]
and
\(\dot Z_1(x)=-2\mathbb E_a[r(a)\Delta_1(a)K_0(x,a)]\).
This proves (3)--(4). In particular, the contribution from training the
interlayer matrix is the product \(C_{H_1}C_{\Delta_2}\). Propagation through
that matrix also enters the first-layer contribution through \(Q\).

Formula (4) is not itself a closure: evolving its factors generally requires
more state and response information.

### Exact finite-program source recursion supplied by the supervisor

This paragraph uses additional supervisor-supplied scientific input from
the established fixed-program rule. Its scope is a fixed, capped causal
program; it is not an assumed continuous-time DMFT theorem.

Index all forward queries by \(p\), with query \(h_p\in L^2(\Omega_1)\),
and all reverse queries by \(q\), with query \(u_q\in L^2(\Omega_2)\).
Let \(q\prec p\) mean that reverse query \(q\) precedes forward query
\(p\); define \(p\prec q\) in the analogous execution order. The source
rule is
\[
W_{20}h_p=\xi_p+\sum_{q\prec p}u_q\,
                  \mathbb E_1[\partial_{\zeta_q}h_p],
\tag{4a}
\]
\[
W_{20}^*u_q=\zeta_q+\sum_{p\prec q}h_p\,
                  \mathbb E_2[\partial_{\xi_p}u_q].
\tag{4b}
\]
The source groups \(\xi\) and \(\zeta\) are independent, with
\[
\mathbb E[\xi_p\xi_{p'}]=\mathbb E_1[h_ph_{p'}],\qquad
\mathbb E[\zeta_q\zeta_{q'}]=\mathbb E_2[u_qu_{q'}].
\tag{4c}
\]
All named derivatives hold covariance entries, population expectations,
prior response coefficients, meshes, and controls fixed; they include
every causal nonlinear path to the query. The answers (4a)--(4b) are
dependent, despite independence of the oriented Gaussian source groups.

For an explicit Euler step \(k\), forward queries are
\(h_{ka}=H_{1,k}(x_a)\), followed by
\(u_{ka}=\Delta_{2,k}(x_a)\). Put
\(\lambda_{jb}=p_b\,\Delta t_j\,r_j(x_b)\). Exact accumulation of
the discrete \(W_2\) updates and (4a)--(4b) gives
\[
Z_{2,k}(x_a)=\xi_{ka}
 +\sum_{(j,b)\prec(ka,\mathrm F)}u_{jb}
       \mathbb E_1[\partial_{\zeta_{jb}}h_{ka}]
 -2\sum_{j<k,b}\lambda_{jb}u_{jb}
       \mathbb E_1[h_{ka}h_{jb}],
\tag{4d}
\]
\[
Q_k(x_a)=\zeta_{ka}
 +\sum_{(j,b,\mathrm F)\prec(ka,\mathrm R)}h_{jb}
       \mathbb E_2[\partial_{\xi_{jb}}u_{ka}]
 -2\sum_{j<k,b}\lambda_{jb}h_{jb}
       \mathbb E_2[u_{ka}u_{jb}].
\tag{4e}
\]
The reverse response sum includes the current forward query. In
particular, at the first step, when the learned-history sums are empty,
the current response can already be nonzero. It must not be removed by
writing every response as a strictly earlier-time integral. Equations
(4d)--(4e) are exact in the fixed-program Gaussian source semantics of
the supplied rule, rather than finite-width identities or a proved
continuous-time limit. They identify all aggregate channels: the two
correlation families and the expected derivatives in both orientations.

## 3. Precise finite-realization hypothesis

For explicit finite coordinate counts, take a fixed dataset
\(\{x_a,y_a,p_a\}_{a=1}^n\), with \(p_a\geq0\), \(\sum_ap_a=1\).
The general data-distribution version has the same integral formulas, but a
finite scalar state additionally requires a spatial representation or a
justified finite data closure. Time-memory compression does not provide it.

Fix a compact interval \([0,T]\). Let \(\mu_{1,t},\mu_{2,t}\) denote the
current laws of the reduced neuron states. They are ordinary current-state
population laws, not laws of complete trajectories. A finite list of current
statistics is
\[
g_j(t)=\mathbb E_{\mu_{1,t}}\psi_{1j}(S_1)
       +\mathbb E_{\mu_{2,t}}\psi_{2j}(S_2),\qquad 1\leq j\leq q.
\tag{5}
\]
The dictionaries \(\psi_{\ell j}\), dimensions, and coefficient rules in the
following assumption must be fixed before the target trajectory is observed.
They may depend on the known dataset, initialization law, model constants,
chosen hierarchy level, and horizon, but not on the realized future.

**Assumption FR.** The actual response-corrected effective population
dynamics admits all of the following properties.

1. For \(\ell=1,2\), there are finite matrices and vectors
   \(A_\ell(g)\in\mathbb R^{k_\ell\times k_\ell}\),
   \(D_\ell(g)\), and \(h_\ell(g,a)\in\mathbb R^{k_\ell}\), and a
   covariance state \(P_\ell(t)\succeq0\), such that, for \(t\geq s\),
   \[
   C_\ell(t,x;s,a)=h_\ell(g_t,x)^\top
       \Phi_\ell(t,s)P_\ell(s)h_\ell(g_s,a),
   \tag{6}
   \]
   where
   \[
   \partial_t\Phi_\ell(t,s)=A_\ell(g_t)\Phi_\ell(t,s),\quad
   \Phi_\ell(s,s)=I,
   \tag{7}
   \]
   \[
   \dot P_\ell=A_\ell P_\ell+P_\ell A_\ell^\top+D_\ell D_\ell^\top.
   \tag{8}
   \]
   Covariances for \(t<s\) are obtained by transposition. If several
   effective Gaussian drives are correlated, (6)--(8) hold for their
   **full joint covariance block**, with one joint latent state. Separate
   marginal realizations do not authorize independent sampling.

2. Every causal-response channel appearing in the effective equations has
   a realization of the form
   \[
   R_{\alpha\beta}(t,x;s,a)=
     L_\alpha(g_t,x)\Psi(t,s)B_\beta(g_s,a),\quad s<t,
   \tag{9}
   \]
   with \(\partial_t\Psi=A_R(g_t)\Psi\), \(\Psi(s,s)=I\).
   A finite direct sum permits distinct blocks. Instantaneous response
   terms, if present, are specified separately as current-state terms.
   Here a causal response means the derivative of the effective observable
   with respect to a specified external probe at an earlier time; the
   probe's injection point and normalization must be part of the DMFT
   specification. All forward/backward and cross-response channels required
   by that specification are included.

3. Every coefficient and statistic in (5)--(9) has a finite, explicitly
   evaluable current-state rule. Evaluating it may use the known dataset,
   the current reduced neuron states and their finite empirical averages,
   and current finite matrix operations. It may not query old activations,
   \(W_{20}\) as a dense matrix, a stored two-time table, functional
   derivatives indexed by the entire past, or a coefficient schedule fitted
   to the target trajectory. The reduced dynamics together with these rules
   is well posed and restartable from its current state.

4. The exact effective-field decomposition is response corrected:
   each adaptive action \(G_\ell\) is a specified Gaussian cavity field
   plus its required response integrals (and any specified current term).
   The Gaussian fields have the joint covariance realized above and the
   correct joint initialization with local neuron variables. Replacing
   \(G_\ell\) directly by a fresh independent Gaussian is explicitly
   excluded.

This is a falsifiable structural assumption on evolving two-time statistics,
not a consequence of tanh smoothness. In particular, part 3 is indispensable:
without it an arbitrary target trajectory could be hidden in
\(A(t),h(t),B(t)\). Parts 1 and 2 by themselves would only be an offline
representation claim.

For a stochastic common environment, the coefficient path can be random.
Then the assertions about Gaussian fields below require a valid conditional
Gaussian construction given that environment. Adapted random coefficients
depending on the same individual driving noise do not in general preserve
Gaussianity. The simplest hypothesis uses deterministic population
statistics at the infinite-width level.

## 4. Auxiliary states derived from the assumption

For each second-layer neuron introduce \(m_2(t)\in\mathbb R^{k_1}\),
initialized to zero, with
\[
\dot m_2=A_1(g_t)m_2+
 \sum_a p_a r_t(a)\Delta_2(t,a)P_1(t)h_1(g_t,a).
\tag{10}
\]
For each first-layer neuron introduce \(m_1(t)\in\mathbb R^{k_2}\),
initialized to zero, with
\[
\dot m_1=A_2(g_t)m_1+
 \sum_a p_a r_t(a)H_1(t,a)P_2(t)h_2(g_t,a).
\tag{11}
\]
Variation of constants in (10) yields
\[
h_1(g_t,x)^\top m_2(t)
 =\int_0^t\sum_a p_a r_s(a)\Delta_2(s,a)
   h_1(g_t,x)^\top\Phi_1(t,s)P_1(s)h_1(g_s,a)\,ds.
\]
Using (6) proves that (1)--(2) become exactly
\[
Z_2(t,x)=G_2(t,x)-2h_1(g_t,x)^\top m_2(t),\qquad
Q(t,x)=G_1(t,x)-2h_2(g_t,x)^\top m_1(t).
\tag{12}
\]
Thus the learned interlayer actions require finite vectors per neuron, with
global coupling through current residuals and statistics.

Likewise a response contribution
\[
\mathcal O_\alpha(t,x)
 =\int_0^t\sum_{\beta,a}p_a
      R_{\alpha\beta}(t,x;s,a)v_\beta(s,a)\,ds
\]
is represented exactly by
\[
\dot o=A_R(g_t)o+\sum_{\beta,a}p_aB_\beta(g_t,a)v_\beta(t,a),
\quad o(0)=0,\quad
\mathcal O_\alpha(t,x)=L_\alpha(g_t,x)o(t).
\tag{13}
\]
The sources \(v_\beta\), signs, and factors here must come from the actual
effective-field derivation; (13) does not guess them.

The original local update equations are already present-state:
\[
\dot Z_1(t,x_a)=-2\sum_b p_b r_t(b)
                 \Delta_1(t,x_b)K_0(x_a,x_b),
\quad
\dot c=-2\sum_b p_b r_t(b)H_2(t,x_b).
\tag{14}
\]
Equations (8), (10)--(14), the pointwise activation definitions, and the
current averages (5) supply the deterministic part of the claimed reduction.
Any instantaneous implicit relation must be solved with the well-posedness
condition included in FR.3.

## 5. Matching the Gaussian driving, not only the drift

For a deterministic coefficient path, introduce a Gaussian latent state
\[
d\eta_\ell=A_\ell(g_t)\eta_\ell\,dt+D_\ell(g_t)\,dB_\ell(t),
\quad \eta_\ell(0)\sim N(0,P_\ell(0)),
\tag{15}
\]
with the prescribed initial correlations and joint Brownian covariance.
Set \(\xi_\ell(t,x)=h_\ell(g_t,x)^\top\eta_\ell(t)\).
The solution is
\[
\eta_\ell(t)=\Phi_\ell(t,0)\eta_\ell(0)
 +\int_0^t\Phi_\ell(t,s)D_\ell(g_s)\,dB_\ell(s).
\]
Its covariance satisfies (8). Since Brownian increments after \(s\) are
independent of \(\eta_\ell(s)\),
\[
\mathbb E[\eta_\ell(t)\eta_\ell(s)^\top]
 =\Phi_\ell(t,s)P_\ell(s),\qquad t\geq s.
\]
Therefore its output covariance is (6). Linear combinations of the initial
Gaussian vector and Brownian integrals are jointly Gaussian, so this matches
every finite-dimensional distribution of the stipulated Gaussian cavity
field, not just its one-time variance. The joint initial law with local
variables and the response corrections are separately required by FR.4.

The covariance state and response states can always be combined by finite
direct sums. There is no claim that their minimal dimensions coincide.

An arbitrary low-rank approximation of a two-time kernel need not be
positive semidefinite and need not possess an online realization. Likewise,
matching only \(C(t,t)\) leaves its temporal correlations undetermined.
Conditions (6)--(8) enforce both temporal consistency and positivity.

If \(D=0\), all Gaussian randomness can be sampled at initialization; this
is a particularly restrictive finite temporal-rank model. Allowing \(D\ne0\)
means that the auxiliary representation reveals new independent latent
information over time. It does not mean that the original gradient flow
receives newly injected physical noise. Smooth original trajectories also
constrain where such innovations can enter: an observed coordinate with
nonzero direct diffusion has nonzero quadratic variation, so cannot exactly
represent a differentiable observable. Hidden-state diffusion may preserve
finitely many derivatives, but covariance regularity must be checked rather
than assumed.

## 6. Coefficient provenance and the remaining constructive gap

None of \(A,D,h,L,B,P,m,o,\eta\) is an independently trained coefficient
in this construction. The actual trainable variables in the supplied model
remain \(W_1,W_2,c\); their gradient flow generated (1)--(4) and (14).
The other quantities are prescribed structural maps, initialized covariance
or random states, and dynamically evolved sufficient statistics.

However, merely calling unknown coefficient maps “structural” does not
derive them. A concrete acceptable instantiation of FR.3 would identify
finite current feature vectors \(U\), derive their instantaneous evolution
\(V\) from the closed local equations, and prove that the relevant evolution
closes in their span. With nonsingular current Gram matrix
\[
G=\mathbb E[UU^\top],\qquad M=\mathbb E[VU^\top],
\]
the coefficient of the orthogonal linear projection is derived by
\[
A=MG^{-1},\qquad
\mathbb E[(V-AU)U^\top]=0.
\tag{16}
\]
To obtain an exact invariant span, one must additionally prove
\(\mathbb E\|V-AU\|^2=0\); orthogonality alone is not closure. For a hierarchy,
one instead needs a controlled residual in a norm that propagates to the
desired observables. Degenerate Gram matrices require a specified supported
subspace and conditioning control.

Formula (16) illustrates allowed coefficient provenance; it is **not** an
implemented response basis or a proof that the required basis exists.
Computing \(V\) by querying the original dense \(W_{20}\) would violate
FR.3. Nor may the missing response dynamics be replaced by fitting
\(A(t)\) from a recorded trajectory.

When a statistic \(g_j\) is the current expectation of a fixed smooth
function \(\psi_j\), its evolution is determined by the local generator:
\[
\dot g_j=\mathbb E[\nabla\psi_j\cdot b
 +\tfrac12\operatorname{tr}(\Sigma\Sigma^\top\nabla^2\psi_j)].
\tag{17}
\]
This is an online population average if current neuron states are retained.
It is a closed finite ODE in \(g\) alone only if its right-hand side can be
expressed through the chosen finite statistics. Nonlinear tanh dynamics
does not make that moment-closure assertion automatic.

## 7. Why zero time-Taylor radius is not the relevant obstruction

The auxiliary equations integrate from the current state. Their derivation
never sums a time-Taylor series. Finite per-neuron state can coexist with an
ensemble observable having zero time-Taylor radius.

For a transparent example, let \(G\sim N(0,1)\), retain the two local state
variables \((G,X)\), and evolve \(\dot G=0\), \(\dot X=G\), \(X(0)=0\).
The bounded observable
\[
F(t)=\mathbb E[(1+X(t)^2)^{-1}]
     =\mathbb E[(1+t^2G^2)^{-1}]
\]
is smooth on the real line. For every fixed derivative order,
differentiation under the expectation is justified by a constant times
the corresponding Gaussian moment: derivatives of \((1+z^2)^{-1}\) are
bounded on the real line. Its formal series at zero has coefficients
\[
[t^{2j}]F(t)=(-1)^j\mathbb E[G^{2j}]
           =(-1)^j(2j-1)!!.
\]
The ratio of successive absolute coefficients is \(2j+1\), so the series
in \(t^2\), and hence the time series, has radius zero. Each individual
trajectory nevertheless has an exact finite present state.

This example establishes logical compatibility, not a closure theorem for
tanh training. Conversely, a finite total-dimensional deterministic ODE
with analytic vector field and analytic observation is locally analytic
where its solution remains finite. Such an object cannot exactly realize a
zero-radius output at that initial point. One must distinguish a population
of finite states, a stochastic state, nonanalytic coefficient rules, and a
finite deterministic analytic ODE.

## 8. A hierarchy needs additional convergence assumptions

Replacing FR by a sequence of ranks \(k\to\infty\) yields a candidate
hierarchy only after specifying a causal rule at every level. Pointwise
low-rank approximation of a recorded covariance is insufficient.

A compact-horizon convergence claim additionally needs:

1. uniformly controlled source residuals for the learned-memory kernels
   and every response kernel in a Volterra-operator norm acting on the
   actual local sources;
2. positive joint Gaussian realizations with a coupling of their paths to
   the target driving paths in the chosen state/observable error norm;
3. stability of the nonlinear self-consistent effective equations in that
   norm, including moment control for the unbounded coefficient \(c\);
4. coefficient construction and conditioning bounds uniform in the
   hierarchy level over the allowed instance class.

These distinguish error production from propagation. Kernel convergence at
isolated times does not alone imply a uniform-in-time Gaussian path
coupling; additional regularity and tightness are needed. A stability
estimate without vanishing source error proves no hierarchy convergence.

## 9. Concrete falsifiers and surviving obligations

For a fixed candidate rank, (6) and (9) imply cross-cut rank bounds. Choose
arbitrary past times \(s_j\leq\tau\) and future times \(t_i\geq\tau\).
Since \(\Phi(t_i,s_j)=\Phi(t_i,\tau)\Phi(\tau,s_j)\), the block matrix
\(C(t_i,x_i;s_j,a_j)\) has rank at most the latent state dimension.
The same argument applies to \(R\). A larger nonzero minor falsifies that
exact candidate dimension. This is a mathematical witness criterion;
no experiment was performed here.

Other candidate falsifiers are an indefinite claimed covariance, a required
diffusion covariance \(\dot P-AP-PA^\top\) that is not positive
semidefinite, a missing cross-response channel, loss of Gaussianity from
noise-dependent coefficients, or two admissible histories reaching the
same claimed reduced state but having different future responses under the
same probe. The last test directly detects hidden memory.

The supplied prompt leaves two major bridges open:

- **DMFT identification:** derive the response-corrected joint law of the
  adaptive fields \(W_{20}H_1\) and \(W_{20}^*\Delta_2\) in continuous
  time, including any limiting current-step response, initialization
  factors, and initial correlations. The supplied fixed-program rule
  establishes (4a)--(4e) at fixed program size; equations (1)--(2) alone
  do not provide the continuous-time identification or justify an
  exchange of program-size, width, and time-mesh limits.
- **Constructive finite response closure:** derive an admissible sequence
  of dictionaries and current-state coefficient rules satisfying FR, or
  controlled approximate versions. A generic state-space ansatz does not
  supply these rules.

What is proved here is the exact aggregate identity (3)--(4) and the
conditional finite-state conversion (10)--(15). Generic finite response
closure, a convergent hierarchy for the supplied tanh model, and finite
total-dimensional closure remain open.
