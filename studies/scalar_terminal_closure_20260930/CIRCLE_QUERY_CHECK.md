# Circle query observer: algebra and implementation obligations

Date: 2026-09-30.

Verdict: **PASS for the planned query-response formulas, shared-integral
observer, odd Fourier representation, and 729-scalar model count.** This
is an algebra/design check. The experiment implementation has not yet been
read or executed, and no numerical validity gate is certified here.

Scientific input scope: complete `CIRCLE_EXPERIMENT_PLAN.md`, the exact
q=1 definition in the complete study `README.md`, the previously checked
complete `TERMINAL_SCALAR_THEOREM.md`, and complete maintained
`code/pde/finite_network.py`. Shared instructions and the previously read
`solve-math-rigorously` skill also apply. Links to other artifacts in the
README were not followed. No training, other study, or external source was
used.

Input SHA256 values at this check:

- Plan: `822b7af56f056af2901d1f15b40ac464cf7a5babc80c7750be64f50b0259d4de`.
- README: `f48a1f829d684478f5c988709dfc7514b2849317cd76446107a73978e9582777`.
- Terminal theorem: `fbb93521867a03c8a01ebe8c29f88d04b643cf3d6fa4af53151e13ddf4c6bde5`.
- Maintained finite network API: `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551`.

## Normalized inputs and the true transpose

Write \(u=x/\sqrt d\). For the circle, \(d=2\),
\(x(\theta)=\sqrt2(\cos\theta,\sin\theta)^T\), and therefore

\[
u(\theta)=(\cos\theta,\sin\theta)^T.
\]

When the implementation stores \(u\), the first layer is
\(h(u)=\tanh(Au)\), and its velocity is

\[
\dot A=-\frac2m\sum_a r_a\ell_a u_a^T.
\]

There is no additional division by \(\sqrt d\) in either expression.
Conversely, the maintained API always divides its supplied physical inputs
by \(\sqrt d\); parity tests against it must supply \(x=\sqrt d\,u\).

Let \(V=(v_1,\ldots,v_m)\), \(K=(k_1,\ldots,k_m)\), both \(n\times m\).
For any query feature or response block, the same fixed mixer satisfies

\[
BH_q=W_0H_q+\frac1{mn}V(K^TH_q),
\]
\[
B^TD_q=W_0^TD_q+\frac1{mn}K(V^TD_q).
\]

The second expression uses the literal transpose of the same \(W_0\).
The roles of \(V\) and \(K\) reverse under transposition. Using
\(V(K^TD_q)\), or another random mixer, would give the wrong backward
response. Query points introduce no extra value or key states.

## Exact train-to-query coefficients

At any current finite q=1 state, define for a fixed query \(u\)

\[
h_u=\tanh(Au),\quad g_u=\tanh(Bh_u),\quad
f_u=\frac1n w^Tg_u,
\]
\[
d_u=w\odot(1-g_u^2),\qquad
\ell_u=(1-h_u^2)\odot B^Td_u.
\]

Every training-indexed object below, including \(v_a,k_a\), refers to a
training point. The exact cross coefficients are

\[
C(u,a)=\frac2m\left[
\frac{g_u^Tg_a}{n}
+(u^Tu_a)\frac{\ell_u^T\ell_a}{n}
+\frac{d_u^Td_a}{n}\frac{h_u^Tk_a}{n}
\right],
\tag{Q1}
\]
\[
b(u)=\frac1{m\sqrt m\,\tau}\sum_{a=1}^m
\frac{d_u^Tv_a}{n}\frac{h_u^T(h_a-k_a)}{n}.
\tag{Q2}
\]

Then

\[
\dot f_u=-\sum_a C(u,a)r_a+\|r\|_2b(u).
\tag{Q3}
\]

To verify the formula, differentiate

\[
\dot f_u=\frac1n\dot w^Tg_u+
\frac1n d_u^T\dot B h_u+
\frac1n\ell_u^T\dot A u.
\]

The readout and first-layer velocities give the first and second terms
of (Q1). The residual-driven value part of

\[
\dot B=-\frac2{mn}\sum_a r_ad_ak_a^T
+\frac{\|r\|_2}{m\sqrt m\,n\tau}
\sum_a v_a(h_a-k_a)^T
\]

gives the last term of (Q1), while its key-motion part gives (Q2).
The two contractions in each of those terms each carry a factor \(1/n\)
after differentiating the output. This checks the extra output factor
and the conversion \(\rho=\|r\|_2/\sqrt m\).

In column-sample matrix notation, use training blocks
\(U,H,G,D,\mathcal E\) and query blocks
\(U_q,H_q,G_q,D_q,\mathcal E_q\), where \(\mathcal E\) denotes the
first-layer backward responses \(\ell\). With \(N_q\) queries,
\(C_q\) has shape \(N_q\times m\), and

\[
C_q=\frac2m\left[
\frac{G_q^TG}{n}
+(U_q^TU)\odot\frac{\mathcal E_q^T\mathcal E}{n}
+\frac{D_q^TD}{n}\odot\frac{H_q^TK}{n}
\right],
\tag{Q4}
\]
\[
b_q=\frac1{m\sqrt m\,\tau}
\left[
\frac{D_q^TV}{n}\odot\frac{H_q^T(H-K)}{n}
\right]\mathbf1_m.
\tag{Q5}
\]

In particular, setting query inputs equal to training inputs must recover
the training \(C\) and \(b\), with the query as the **row** index and
training source as the **column** index. The key pairing is \(H_q^TK\),
not an exchange of current and stored features or a symmetrization of
the resulting matrix.

## One shared integral state for every query

Reset time to the q=1 handoff. Freeze the training coefficients \(C_0,b_0\),
the handoff function \(f_0(u)\), and the query functions \(C_0(u,:),b_0(u)\).
Let the scalar state be

\[
(\widehat r,z,s)\in\mathbb R^m\times\mathbb R^m\times\mathbb R,
\]
\[
\dot{\widehat r}=-C_0\widehat r+\|\widehat r\|_2b_0,
\qquad \dot z=\widehat r,\qquad \dot s=\|\widehat r\|_2,
\]
\[
\widehat r(0)=r_0,\qquad z(0)=0,\quad s(0)=0.
\tag{Q6}
\]

The untruncated frozen-query prediction is exactly

\[
\widehat f(u,t)=f_0(u)-C_0(u,:)z(t)+b_0(u)s(t).
\tag{Q7}
\]

Differentiation proves that (Q7) is the passive-observable ODE with the
shared scalar residual feedback. It does not require a moving coordinate
for each query. The clock, if desired, is reconstructed as
\(\widehat\tau(t)=\tau_0+s(t)/\sqrt m\); no additional moving clock
coordinate is necessary.

A useful exact training identity is

\[
\widehat r(t)=r_0-C_0z(t)+b_0s(t).
\tag{Q8}
\]

Thus the **untruncated** query output at training points equals
\(y+\widehat r\). The residual ODE does not use the query Fourier
approximation, so a truncated Fourier output need not satisfy this identity
exactly. Reported training loss \(\|\widehat r\|_2^2/m\) and any training
loss reconstructed through the Fourier predictor must therefore be named
separately or have their discrepancy measured.

Equation (Q7) is an exact identity for the frozen observer. Accuracy against
the evolving full q=1 query requires the passive-observable hypotheses
of the terminal theorem. A positive handoff contraction diagnostic alone
does not certify those full-tube hypotheses. Finite-time numerical
comparisons remain meaningful even when such a theorem certificate has
not been established.

## Why every retained query function uses only odd frequencies

At a fixed finite state, the bias-free tanh network satisfies

\[
h_{-u}=-h_u,\quad g_{-u}=-g_u,\quad f_{-u}=-f_u,
\qquad d_{-u}=d_u,\quad\ell_{-u}=\ell_u.
\]

Each term of (Q1) changes sign under \(u\mapsto-u\): its respective
odd factor is \(g_u\), \(u^Tu_a\), or \(h_u^Tk_a\). Each summand of
(Q2) also changes sign, through \(h_u^T(h_a-k_a)\). Hence

\[
F(\theta+\pi)=-F(\theta)
\]

for every one of the \(m+2\) functions
\(f_0,C_0(\cdot,1),\ldots,C_0(\cdot,m),b_0\), independently of the
training geometry or labels. Constant and even Fourier modes vanish in
exact arithmetic. This is antipodal oddness, not oddness under
\(\theta\mapsto-\theta\): both sine and cosine coefficients are needed.

For \(N=2048\) equally spaced samples
\(\theta_j=2\pi j/N\), the planned truncated representation is

\[
F_{32}(\theta)=\sum_{k\in\{1,3,\ldots,63\}}
\left[a_k\cos(k\theta)+c_k\sin(k\theta)\right],
\tag{Q9}
\]
\[
a_k=\frac2N\sum_jF(\theta_j)\cos(k\theta_j),\qquad
c_k=\frac2N\sum_jF(\theta_j)\sin(k\theta_j).
\tag{Q10}
\]

With the usual negative-exponential FFT convention, these are
\(a_k=2\operatorname{Re}(\mathrm{FFT}(F)_k)/N\) and
\(c_k=-2\operatorname{Im}(\mathrm{FFT}(F)_k)/N\). The indices are the
actual frequencies \(1,3,\ldots,63\), not consecutive frequencies
\(1,\ldots,32\). The largest retained frequency is below Nyquist.

There are 64 real coefficients per function. Forming them by a finite
sample sum can introduce aliasing from unresolved higher frequencies,
in addition to discarding higher odd modes. Oddness alone supplies no
quantitative bound on either error. The independent midpoint grid
\(2\pi(j+1/2)/8192\) is appropriate empirical validation and does not
overlap the source grid; it is not a uniform-circle certificate.

For a diagnostic panel, write the Fourier representation errors at handoff
as \(\Delta f_0(u),\Delta C_0(u,:),\Delta b_0(u)\). At every later
scalar state,

\[
|\widehat f_{32}(u,t)-\widehat f(u,t)|
\le |\Delta f_0(u)|
+\|\Delta C_0(u,:)\|_2\|z(t)\|_2
+|\Delta b_0(u)|s(t).
\tag{Q11}
\]

Here \(s\ge0\) and \(\|z\|_2\le s\). Under the original Euclidean
terminal margin, the frozen residual obeys
\(s(\infty)\le\|r_0\|_2/\lambda_0\); without a certificate, (Q11)
still applies using the measured finite-time integral. Saving the raw
panel coefficients therefore separates spatial representation error
from error caused by freezing the coefficients.

The decomposition of endpoint error is pointwise exact:

\[
\widehat f_{32}-f_{q=1}
=(\widehat f_{32}-\widehat f)+(\widehat f-f_{q=1}),
\]

with an additional \(f_{q=1}-f_{\rm dense}\) term for dense comparison.
Norms of these components need not add exactly because of cancellation.
For the static control, reporting both raw \(f_0\) and Fourier \(f_{0,32}\)
distinguishes actual q=1 tail movement from the matched Fourier
no-continuation baseline.

## Scalar count

For \(m=8\), the planned model retains:

| Item | Scalars |
|---|---:|
| Frozen training response \(C_0\) | 64 |
| Frozen training drift \(b_0\) | 8 |
| Ten query functions, 64 Fourier coefficients each | 640 |
| Moving residual \(\widehat r\) | 8 |
| Moving integrated residual \(z\) | 8 |
| Moving integrated norm \(s\) | 1 |
| **Fixed total** | **712** |
| **Moving total** | **17** |
| **Total** | **729** |

The initial residual is already the initial value of a moving coordinate;
it need not be retained a second time for restart. Optional \(\tau_0\),
training labels, task metadata, integrator workspace, and output grids
should be accounted for separately. Labels are unnecessary for evaluating
the residual loss or unseen Fourier output after handoff. Fixed Fourier
frequencies can be generated from their prescribed index rule.

For comparison, the two-layer dense network at \(n=1024,d=2\) has
\(nd+n^2+n=1{,}051{,}648\) moving parameter scalars. The exact q=1 state
has \(nd+n+2nm+1=19{,}457\) moving scalars plus the fixed
\(n^2=1{,}048{,}576\) mixer entries, excluding data and diagnostic copies.
Generating the 712 frozen coefficients still requires that full handoff
state and query-feature work. The 729-scalar evaluator count does not
erase this cost or establish an asymptotic compression theorem.

## Required implementation checks

1. On a tiny deterministic **non-initial** state with nonzero \(w,V\)
   and \(H-K\), compare the direct chain-rule query derivative with
   (Q3), and with central directional differences of
   \(f(X\pm\varepsilon\dot X,u)\). Perturb all evolving state blocks,
   including keys and clock, while keeping the same \(W_0\) fixed.
   Use more than one \(\varepsilon\) to distinguish truncation from
   cancellation. Initialization alone makes several terms vanish and
   cannot validate their factors.
2. Verify both matrix actions against explicitly formed
   \(B=W_0+VK^T/(mn)\), using a nonsymmetric mixer. Check query rows
   at the training points against the training residual derivative;
   this detects index and transpose mistakes.
3. Compare the dense RHS to maintained `finite_network.flow_velocity`
   using physical inputs \(\sqrt d\,U\), the same supplied weights,
   zero or deliberately chosen matching readout, and default unit
   `kappas`. The maintained initializer's random small readout is not
   the experiment's prescribed zero-readout initializer.
4. Check (Q8) throughout scalar integration, and compare (Q7) for a few
   queries with independently appended passive-observer ODEs. Both
   should agree up to numerical integration/roundoff error.
5. Validate Fourier conventions on single known sine and cosine
   functions at retained odd frequencies, and check antipodal parity
   of the actual sampled \(f_0,C_q,b_q\). Evaluate reconstruction on
   the independent midpoint grid. Record raw and Fourier query errors
   separately, including their training-point discrepancy.
6. Ensure scalar continuation reads only the retained training/Fourier
   coefficients and its own current scalar state. Full q=1 future
   states and diagnostic arrays belong only to the reference/evaluation
   path. The 8192-query panel must not become hidden moving model state.
7. For any exactly antipodal, odd-labeled training task, a full-space
   positive margin may be obstructed by redundant even residual
   directions. If \(E\) has orthonormal columns spanning the paired
   odd residual space, the correctly normalized restricted generator
   is \(-E^TC_0E\,q+\|q\|_2E^Tb_0\). Its Euclidean diagnostic margin
   is \(\lambda_{\min}(\operatorname{sym}(E^TC_0E))-
   \|E^Tb_0\|_2\). Check the pairing, labels, subspace invariance and
   numerical symmetry error before interpreting that diagnostic.
   It remains distinct from a certified terminal tube.

All full-flow and scalar comparisons must use the common physical times
and the prespecified handoffs. The derived observer supports the planned
test of unseen-circle fidelity; successful fitting alone supplies no
unseen-output accuracy conclusion.

## Addendum: complete producer audit before training

The supervisor subsequently authorized reading the complete implementation
`circle_terminal_experiment.py` and the tiny-check evidence
`data/generated/scalar_terminal_closure_20260930/circle_checks_01/checks.json`.
No training was run by this checker.

The complete implementation audited here has SHA256

`93c90fe81cd4b3e2e598526d2a1e73315d9f9407d474ac0677af491fe2d95ab6`.

Verdict for this frozen implementation: **PASS on the mathematical
dynamics and observer; protocol/recovery fixes identified below.** Any
later producer changes require their own targeted check. The supervisor
has already stated an intention to add the Fourier training-loss and exact
observer-consistency diagnostics, which are absent from this frozen version.

### Model, integrator, and observer implementation

`fields` uses the stored normalized inputs directly, with no second
normalization. Its q=1 forward action is
`w0 @ first + values @ (keys.T @ first)/(m*n)`, and its backward action is
`w0.T @ delta + keys @ (values.T @ delta)/(m*n)`. Both agree with the
derived matrix and its true transpose. Its derivative formula
`4*exp(-2*abs(z))/(1+exp(-2*abs(z)))**2` is mathematically \(\tanh'(z)\)
and avoids subtracting nearly equal numbers in saturated regions.

`velocity` implements the unhalved-MSE mobilities and exact q=1 state
equations correctly. The dense matrix velocity uses the current forward
features; q=1 evolves values, keys and the shared clock instead. The
initializer draws \(A\) and \(W_0\) from the prescribed RNG in that
order, repeats that same initializer for every task and resolution, and
uses zero readout in both reference models.

`rk4` is simultaneous classical RK4. Its second and third stages use the
half-step state, its fourth stage uses the full third-stage increment,
and its final sum has weights \((1,2,2,1)/6\). All blocks at a given stage
are evaluated from the same state, and capture/diagnostic functions do
not mutate the state used by the precomputed first-stage velocity.

`response` implements (Q4) and (Q5) exactly, including their row/column
orientation, all factors of \(m,n,\sqrt m\), and the correct current-
feature/key gap. Query blocking changes only allocation, not the
mathematical response. No coefficient is symmetrized or projected for
use in the scalar dynamics; symmetric parts are used only for diagnostics.

`fourier_coefficients` and `fourier_basis` have matching cosine/sine
ordering and FFT signs. Their 32 frequencies are exactly the odd
frequencies through 63. Source sampling and independent midpoint
validation use the precommitted resolutions. The spatial error recorded
in `capture` includes both discarded-mode and sampling-alias effects on
the validation grid; it should not be described as a rigorous continuous
Fourier tail bound.

`scalar_solution` evolves precisely \((\widehat r,z,s)\) from (Q6), with
its own residual feedback and the declared DOP853 tolerances. Giving its
time interval the absolute handoff time is valid because the system is
autonomous. The final Fourier readout multiplies coefficient columns by
\((1,-z_1,\ldots,-z_m,s)^T\), agreeing with (Q7). The saved direct readout
is the exact untruncated frozen observer on the diagnostic panel. No
future q=1 outputs enter the scalar integration or coefficient fitting.

### Supplied tiny-check evidence

The supplied check file reports:

| Check | Reported maximum error |
|---|---:|
| Dense first-layer RHS versus maintained API | \(5.55\times10^{-16}\) |
| Dense middle-layer RHS versus maintained API | \(5.55\times10^{-17}\) |
| Dense readout RHS versus maintained API | \(1.11\times10^{-16}\) |
| q=1 query directional difference, step \(10^{-4}\) | \(1.35\times10^{-10}\) |
| q=1 query directional difference, step \(10^{-5}\) | \(8.37\times10^{-12}\) |
| q=1 query directional difference, step \(10^{-6}\) | \(2.09\times10^{-11}\) |
| Retained sine/cosine Fourier reconstruction | \(1.33\times10^{-15}\) |
| Scalar residual/integral analytic check | \(3.18\times10^{-11}\) |

The checks in the read source are meaningful: the q=1 directional test
uses nonzero random readout and values, independent non-current keys,
nonzero residuals, train and unseen query inputs, and perturbations of all
state blocks including the clock. The maintained dense API is supplied
physical inputs \(\sqrt2\,U\), so the tiny parity test also checks the
normalization. The scalar test uses a negative initial residual and a
nonzero norm drift, verifying its sign as well as both integrated controls.
These are supplied execution results, not executions by this checker.

### Protocol fidelity and fixes for the audited revision

The width, seed, three threshold handoffs, step sizes, maximum physical
time, common-time coarse stop, and finite-query evaluation grid match the
plan. Fine and optional refined runs use the coarse-selected handoff times
and final time. Their steps are dyadic, so the recorded common times are
exactly compatible. The script uses one sequential worker and limits
loaded BLAS thread pools to two. It records the requested two full-flow
endpoint sensitivity measures, the primary scalar endpoint sensitivity,
and common-time dense/q=1 loss sensitivities. Missing primary handoff data
make the refinement gate fail instead of silently passing.

The following issues were sent to the supervisor before training:

1. **Budget checks omit endpoint and scalar analysis.** The deadline is
   checked in the full-flow RK loop, but not while constructing the
   endpoint query outputs, integrating all scalar continuations, or
   writing/analyzing those outputs after the loop. A run can therefore
   exceed the nominal cumulative wall budget during those phases. Add
   checks at bounded phase boundaries and preserve the last completed
   results when a budget stop occurs.
2. **An interrupted case loses most of its trajectory.** Loss/residual
   arrays and final states are written only after successful completion
   of the full-flow loop and all scalar analyses. A timeout or exception
   can leave handoff files and a failure record but lose that case's
   collected loss history and current state. The plan requires retained
   partial failures; save a partial checkpoint on interruption, preferably
   with the phase, current physical time, and per-model status.
3. **Initial arrays are not saved.** The source records hashes of the
   common initial \(A\) and \(W_0\), but saves no initial array file.
   Although the seed and code allow deterministic reconstruction in the
   recorded environment, the plan expressly requests initial states.
   Saving the common initializer once per run suffices and avoids
   unnecessary copies across tasks/resolutions.
4. **An empty away-from-boundary mask produces a JSON failure.**
   `mean(sign_error[off_boundary])` is NaN if no dense query has absolute
   output at least 0.05. `allow_nan=False` then aborts serialization. Use
   a null metric together with the recorded zero eligible fraction/count
   in this case; it is not evidence of zero sign error.
5. **Finite loss is weaker than finite state.** The loop checks finite
   losses, but not every state block. Saturating nonlinearities can mask
   a nonfinite hidden parameter in an output. To implement the declared
   finite-state gate, check every dense and q=1 block at the recorded
   step states and before saving a handoff/endpoint.
6. **The RSS statistic is sampled, not the true peak.** Sampling current
   RSS after complete RK steps/captures can miss allocation peaks within
   stages or endpoint analysis. Either name it sampled maximum RSS or
   obtain the process high-water RSS, and check the declared 4-GiB cap.
   The inspected allocation structure is modest at the fixed dimensions,
   but that observation is not the same as measuring the promised peak.

Two reporting distinctions also remain useful. First, the current static
control is the raw handoff function, whereas the primary moving scalar
prediction includes Fourier representation error. Retain it for measuring
true q=1 tail movement, and add the static Fourier function when claiming
a control matched to the output representation. Second, the current
refinement gate checks training-loss sensitivity for dense and q=1 only.
Recording the primary scalar loss sensitivity as well would remove any
ambiguity in the plan's phrase “maximum observed common-time training-loss
change.” These do not alter the tested scientific parameters.

The producer records failed sensitivity gates and permits only one finer
run per task, as planned. The eventual report must still list unreached
handoffs and unfinished tasks explicitly, and must not interpret a selected
resolution as validated when its gate is false. No model-level transpose,
normalization, response-source, Fourier-sign, or shared-observer error was
found in the audited version.

## Addendum: frozen source of the running experiment

The supervisor next authorized a complete audit of the source snapshot
in `data/generated/scalar_terminal_closure_20260930/circle_width1024_02/`
and the tiny-check file in `circle_checks_02/`. The entire frozen producer
was read. Its SHA256 is

`f5ea7959bbd440aa161b6cb0ee484e68d9e81d5e7cce5e4b9b1df590a170c6ba`.

**Mathematical implementation verdict remains PASS.** The following
changes from the first audited source are correct:

- An input array with shape \(8\times2\) is transposed once into the
  required column-sample shape \(2\times8\). This changes storage
  orientation only, with no additional normalization or point reordering.
- The common initial \(A,W_0\), and zero readout are now saved to
  `initialization.npz`. Together with the task inputs and the specified
  zero values, initial keys \(\tanh(AU)\), and clock one, these define
  both initial states.
- The endpoint Fourier training MSE is now evaluated from the Fourier
  function at the original training angles, independently of the residual
  ODE loss. Its consistency diagnostic subtracts
  \(y+\widehat r(t)\), as required.
- The exact training observer is evaluated as
  \(y+r_0-C_0z+b_0s\), and its discrepancy from
  \(y+\widehat r(t)\) is recorded. This checks the correct integrated
  residual identity at the endpoint.

The supplied `circle_checks_02/checks.json` repeats the successful tiny
check values recorded above. No training result was inspected during this
source audit, and no source, running process, scientific parameter, or
training artifact was changed by this checker.

The supervisor reports that the earlier `circle_width1024_01` attempt
failed before training because of the input-array orientation and was
retained. That account is not a separately audited execution claim here;
the final source's orientation handling is directly verified.

The earlier notes on deadline coverage, interrupted-case persistence,
finite-state checking, sampled RSS, and the empty boundary mask still
describe the frozen producer. The supervisor has acknowledged the budget
and recovery limitations, is monitoring the run externally, and will not
report an empirical result without complete saved data and valid gates.
This report does not certify those external monitoring actions or an
unobserved execution outcome. In particular, finite-grid empirical success
must not be upgraded to a terminal-tube theorem or a whole-circle uniform
certificate.
