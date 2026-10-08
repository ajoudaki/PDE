# Phase-2 instrumentation check

2026-10-07. Bounded independent code and identity audit of
`dense_response_phase2.py` and `causal_response_phase2.py`, with
`causal_population_simulator.py` as a dependency and the frozen phase-1
`dense_learning_experiment.py` as the dense comparison. Only those scientific
inputs were inspected for this audit. All numerical checks used at most
31 neurons/particles and a horizon at most one; no cohort was launched and
no implementation file was edited.

No implementation error was found in the scoped geometry, derivative,
companion-integral, or source-split calculations. Two qualifications must
accompany their interpretation: the Euler ordered sums do not satisfy the
continuous symmetric identity without a known correction, and integrating
instantaneous source rates by Euler does not exactly partition the finite-step
output change. Neither discrepancy is evidence of an omitted physical source.

## Frozen inputs

The inspected SHA-256 values were:

| File | SHA-256 |
|---|---|
| `dense_response_phase2.py` | `9e768a5931dae0f0ece15c75decf0cfefd909c41443bf0d6f6e598790ae64d27` |
| `causal_response_phase2.py` | `5f5bcc2e3ac4a4b5baae161c2fc183bf45338d54f2f3450f33c9329cea7f11de` |
| `causal_population_simulator.py` | `4431bef401087ca0e0f0bd465f1d31d88e7486403ec18d331eab8bbc035e5d76` |
| `dense_learning_experiment.py` | `58d566adc2898a49389c73d659147dd98d39b4eab0c24aaba444dbc91d8a7942` |

## Geometry and the lower-feature defect

The dense network evaluates
\(z_{1,a}=Av_a\), \(h_{1,a}=\tanh z_{1,a}\),
\(z_{2,a}=Wh_{1,a}\), \(h_{2,a}=\tanh z_{2,a}\), and
\(f_a=w^\top h_{2,a}/n\). There are two labeled samples, with
\(c_a=y_a-f_a\), and a passive sample 3. All input directions are normalized.

Let \(\lambda\in\mathbb R^2\) solve
\(v_3=\lambda_1v_1+\lambda_2v_2\). The code solves this relation using the
training columns, rather than reusing the orthogonal-panel coefficients.
Its two cases give

\[
\begin{array}{c|c|c}
\text{case}&v_2&\lambda\\
A&(0,1)&(2,1)/\sqrt5\\
B&(0.6,0.8)&(\sqrt5/4,\sqrt5/4).
\end{array}
\]

In both cases \(v_1=(1,0)\), \(v_3=(2,1)/\sqrt5\), and the unequal labels
are \((0.6,-0.3)\). The `symmetric` case uses the orthogonal panel and
labels \((0.6,-0.6)\). The numerical input relation held within
\(5.56\times10^{-17}\).

Define the layer feature defect
\(q_\ell=h_{\ell,3}-\lambda_1h_{\ell,1}-\lambda_2h_{\ell,2}\), an
\(n\)-vector, and gates \(g_{\ell,a}=1-h_{\ell,a}^2\) in the tanh mode.
Since \(z_{1,3}=\lambda_1z_{1,1}+\lambda_2z_{1,2}\), differentiation gives
the exact continuous identity

\[
\dot q_1=\sum_{b=1}^2\lambda_b
       (g_{1,3}-g_{1,b})\odot\dot z_{1,b},
\qquad
\dot z_{1,b}=\dot A v_b
=\sum_{j=1}^2 c_j S_{bj}\delta_{1,j},
\tag{1}
\]

where \(S_{bj}=v_b^\top v_j\) and
\(\delta_{1,j}=g_{1,j}\odot W^\top(g_{2,j}\odot w)\).
The factor \(2/m\) is one. The code's `direct_lower` uses
`velocity[0] @ v[:, b]`, which includes every \(S_{bj}\). Thus its identity
remains valid in case B. Replacing \(\dot z_{1,b}\) by
\(c_b\delta_{1,b}\) would incorrectly discard the correlated-input terms.

At width 17, seed 811, after five RK4 steps of size 0.1, the direct gate
identity passed to \(1.39\times10^{-17}\) in both cases. A centered directional
difference with increment \(10^{-5}\) agreed with \(\dot q_1\) within
\(9.31\times10^{-12}\). The incorrect orthogonal shortcut differed by only
roundoff in case A but by \(5.80\times10^{-3}\) in case B. This is a
nontrivial correlated-panel check, rather than a zero-readout initial check.

The initialized-affine-gate mode uses the fixed initialized derivatives in
both its affine forward features and its backward gates. Therefore (1)
holds there with those fixed gates as well. It does not require current
tanh gates to be substituted into an affine forward model.

## What the passive source integrals partition

The scalar passive defect is

\[
\Phi=f_3-\lambda_1f_1-\lambda_2f_2=\frac1n w^\top q_2.
\]

Set \(m_a=\dot W h_{1,a}\) and \(\ell_a=W\dot h_{1,a}\). Then the
instantaneous output derivative separates exactly into readout, middle,
and lower contributions:

\[
\dot f_a=rac1n\dot w^\top h_{2,a}
 +\frac1n w^\top(g_{2,a}\odot m_a)
 +\frac1n w^\top(g_{2,a}\odot\ell_a).
\tag{2}
\]

`block_fdot` stores these three terms; `source_rates` takes sample 3 minus
\(\lambda_1\) times sample 1 and \(\lambda_2\) times sample 2 in each row. Therefore
their sum equals \(\dot\Phi\). The independently evaluated parameter-block
kernel agrees with (2), including the correlated factor \(S\) in its lower
block. The saved upper-feature Gram rates also differentiate the Gram
correctly: centered directional differences agreed within
\(2.21\times10^{-12}\) in the above nonzero-readout checks.

The three source integrals partition \(\Phi\), not \(f_3\) alone. In contrast,
`passive_split` stores the different exact algebraic partition

\[
f_3=\frac1n w^\top h_{2,3}(0)
 +\frac1n w^\top[h_{2,3}(t)-h_{2,3}(0)].
\tag{3}
\]

These two stored diagnostics should not be added or compared as if they
partitioned the same scalar. Equation (3) agreed with \(f_3\) within
\(1.39\times10^{-17}\).

`initial_readout_integral` integrates
\(\dot w^\top q_2(0)/n\); because \(w(0)=0\), it equals
\(w(t)^\top q_2(0)/n\). This is a linear companion identity and is preserved
up to roundoff by the shared Euler or RK stages. The mode checks gave error
at most \(6.51\times10^{-19}\). Its readout \(w(t)\) is the actual run's
readout, so this quantity is not a separate frozen-feature training run.

Likewise, `gate_drift_integrals` isolate the explicit upper-gate difference
\(g_{2,a}(t)-g_{2,a}(0)\) inside the middle and lower terms of (2), along
the same trajectory. They are not the total counterfactual effect of changing
all gates: lower gates and the rest of the state also affect the trajectory.
The initialized-affine mode correctly gives exactly zero for this recorded
upper-gate drift. Freezing the middle gives exactly zero middle source;
freezing both hidden blocks gives zero middle and lower sources. All four
mode checks passed their instantaneous identities to at most
\(4.17\times10^{-17}\).

## Continuous identities and numerical integration

The companion variables obey the continuous equations

\[
\dot u=c,\qquad \dot I=cu^\top,
\qquad \dot P=\text{source rates}.
\]

With zero initial readout and companions, the continuous identities are
\(I+I^\top=uu^\top\) and \(\sum_iP_i=\Phi\). The dense implementation
integrates the companions at the same RK stages as the physical state,
which is correct. These nonlinear identities are not automatically exact
in the resulting numerical endpoints.

For Euler with step \(h\), both implementations use the left-point ordered
sum

\[
u_{k+1}=u_k+h c_k,\qquad I_{k+1}=I_k+h c_ku_k^\top.
\]

Expanding \(u_{k+1}u_{k+1}^\top\) and summing gives the exact discrete identity

\[
I_N+I_N^\top
=u_Nu_N^\top-h^2\sum_{k<N}c_kc_k^\top.
\tag{4}
\]

Consequently `ordered_identity_error` is expected to be nonzero for Euler.
For a comparison requiring the continuous symmetric identity on the
piecewise-linear \(u\)-path, use

\[
I_N^{\mathrm{mid}}=I_N+\frac{h^2}{2}\sum_{k<N}c_kc_k^\top.
\tag{5}
\]

The correction is symmetric, so
\(I^{\mathrm{mid}}_{12}-I^{\mathrm{mid}}_{21}=I_{12}-I_{21}\) exactly.
The saved signed area is therefore already the signed area of that
piecewise-linear path. Equation (5) changes the interpretation of the
ordered integrals on the same saved path; it does not change or rerun training.
Using \(I_{aa}=u_a^2/2\) or \(I_{12}+I_{21}=u_1u_2\) on the raw Euler
`ordered` array would be incorrect.

The source discrepancy has a different origin. Euler advances physical
parameters by \(\theta_{k+1}=\theta_k+h\dot\theta_k\) and companions by
\(P_{k+1}=P_k+h\dot\Phi_k\). For the nonlinear observable \(\Phi(\theta)\),
Taylor's formula gives

\[
\Phi(\theta_{k+1})-\Phi(\theta_k)-h\dot\Phi_k
=\frac{h^2}{2}D^2\Phi(\theta_k)
        [\dot\theta_k,\dot\theta_k]+O(h^3).
\tag{6}
\]

Thus `integrated_source_defect` generally has first-order accumulated Euler
error on a fixed smooth bounded interval. Under the corresponding regularity,
joint RK4 integration instead gives fourth-order endpoint error. These are
numerical-integration qualifications, not a new error theorem for the
population approximation or a large-time assertion.

A deterministic case-B check at width 17, seed 811, and horizon one gave:

| Method | Step | Maximum source discrepancy | Maximum raw symmetric ordered discrepancy |
|---|---:|---:|---:|
| RK4 | 0.1 | \(1.453\times10^{-9}\) | \(3.849\times10^{-9}\) |
| RK4 | 0.05 | \(8.977\times10^{-11}\) | \(2.339\times10^{-10}\) |
| RK4 | 0.025 | \(5.577\times10^{-12}\) | \(1.441\times10^{-11}\) |
| Euler | 0.1 | \(1.423\times10^{-4}\) | \(3.119\times10^{-2}\) |
| Euler | 0.05 | \(7.497\times10^{-5}\) | \(1.547\times10^{-2}\) |
| Euler | 0.025 | \(3.844\times10^{-5}\) | \(7.703\times10^{-3}\) |

After including the term in (4), all dense Euler ordered identities held
within \(1.07\times10^{-16}\). The observed source refinement is consistent
with the expected integration orders. This check does not bound the source
discrepancy in the separately run full-horizon cohorts; their saved
`integrated_source_defect` remains the relevant per-run diagnostic.

## Causal geometry and formal responses

A separate scoped audit checked that the supplied input Gram enters the
causal lower initialization, lower updates, lower tangent updates, frozen
replay, and kernel diagnostic consistently. Correlated Gaussian primitives
retain distinct formal coordinate derivatives: differentiating with respect
to one primitive is not differentiating all primitives correlated with it.
The existing response indexing respects that convention.

The causal check used 31 particles, seed 17, step 0.2, four steps, labels
\((0.15,-0.07)\), and normalized inputs
\((1,0),(0.6,0.8),(-0.8,0.6)\). Frozen replay matched exactly. Centered
primitive probes for both Gaussian families, all three source samples, and
probe times indexed 0, 1, and 3 agreed with stored responses across active and
passive evaluated samples within \(1.06\times10^{-12}\). Passive lower
primitive sources had zero responses; a passive upper primitive had only
its direct same-time passive derivative. The corrected identity (4) held
within \(4.8\times10^{-18}\), and midpoint versus left-point areas differed
by \(5.5\times10^{-20}\).

The dense built-in self-test also passed: maximum algebraic identity error
\(5.56\times10^{-17}\), centered output-derivative error
\(6.74\times10^{-13}\), and maximum difference from the phase-1 dense
implementation \(2.78\times10^{-17}\) on its width-17, horizon-0.5 symmetric
comparison.

These checks validate the scoped instrument identities and their indexing.
They do not certify the statistical accuracy of particle quadrature, the
large-width limit, full-cohort outcomes, or the accuracy of the nonlinear
reduced approximation. No source changes are needed for the findings above;
the discrete versus continuous qualifications are needed when reporting data.
