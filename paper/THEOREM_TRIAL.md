# Trial integration of the uniform response-memory results

The comparison manuscript is `main_theorem_trial.tex`, compiled as
`main_theorem_trial.pdf`. The existing `main.tex`, `main.pdf`, figures and
original appendix inputs are preserved.

The main text now has one central theorem for the original residual-speed
closure: exponential fitting at every order, all-time normalized-parameter
tracking, and whole-input prediction against the dense population flow.
It states the Gaussian initialization, exactly zero readout, positive initial
feature-Gram gap, fixed small-label threshold and activation assumptions
together. The order envelope is nearly quadratic; the width remainder
vanishes in probability but has no claimed numerical rate.

Two consequences follow directly: sublinear divergent order gives a vanishing
fraction of dense evolving state, and a consistent hidden-learning-rate
rescaling replaces the label condition by alpha times label RMS being small.
The broader-label finite-time result is an appendix branch. Its constant is
width-independent on an explicitly stated joint width/order region; its
sufficient order threshold is not width-independent.

The generic fixed-width theorems for both clocks remain in the appendices.
The older frozen-span population construction is omitted from this trial to
keep the argument focused. Experiments and figures are unchanged. The
comparison appendix distinguishes proved compression from conditional
root-width costs and from uncertified solver accuracy assumptions.

Trial inputs:

- `trial_core.tex`: central statements, interpretation and costs.
- `trial_alltime_proof.tex`: the small-label proof and population passage.
- `trial_tracking_proof.tex`: the sharp tracking estimate and test predictions.
- `trial_finite_time.tex`: broader-label finite-time proof.
- `trial_comparison_appendix.tex`: matched accuracy/resource comparisons.

Compile from the paper directory, keeping auxiliary files outside it:

```bash
mkdir -p /tmp/pde-theorem-trial-build
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=/tmp/pde-theorem-trial-build main_theorem_trial.tex
cp /tmp/pde-theorem-trial-build/main_theorem_trial.pdf main_theorem_trial.pdf
```

This is an authoring trial based on the current study derivations, not a
replacement of the main manuscript or a promotion to the maintained book.

## Width-rate obligation

The requested all-time moving-state bound
`epsilon^(-5/2+o(1))` is **not proved by the current argument under the main
theorem's hypotheses**. This is an unresolved estimate, not a counterexample
to that possible stronger theorem.

The tracking proof gives, on common events `G_n` whose probabilities tend
to one,

\[
 \mathcal E_\mu(\widehat f_{n,q},f_\infty)
 \le C_\mu\omega(q)+b_{n,\mu},\qquad
 b_{n,\mu}=C_\mu\Phi(a_n)+d_{n,\mu},
\]
\[
 \Phi(u)=u e^{K\sqrt{\log(e+1/u)}},\qquad
 d_{n,\mu}=\mathcal E_\mu(f_{n,D},f_\infty),\qquad
 a_n,d_{n,\mu}\xrightarrow{\Pr}0.
\]

Section 6 of `ACTIVATION_GAUSSIAN_ALLTIME.md` takes width to infinity at
each **fixed** cutoff and **fixed** reference program. The finite union
and monotonicity argument then proves convergence of the supremum defining
`a_n`, without a width modulus. In particular, it does not permit replacing
the fixed cutoff by `M_n` of order `sqrt(log n)`, or refining the reference
program with width while retaining a numerical rate. The population
sub-Gaussian bounds control field magnitudes, not finite-width empirical
errors or bias. The dense whole-input prediction passage also uses
qualitative finite-probe limits and input truncation. Small total activity
controls time amplification but does not quantify these empirical errors.

There is an unconditional fixed-confidence cost. For `u>0`, `0<delta<1`,
define the finite integer

\[
 N_\mu(u,\delta)=\min\left\{N\ge1:
 \sup_{n\ge N}\Pr\bigl(G_n^c\cup\{b_{n,\mu}>u\}\bigr)
 \le\delta\right\}.
\]

Finiteness follows directly from the two convergence-in-probability
statements. Choose an integer `q_v` with `C_mu omega(q_v)<=v` and
`q_v=v^(-1/2+o(1))`. Taking
`n=N_mu(epsilon/2,delta)` and `q=q_(epsilon/2)` proves error at most
`epsilon` with probability at least `1-delta`, using

\[
 M\le 2(L-1)mN_\mu(\varepsilon/2,\delta)q_{\varepsilon/2}
       +(d+1)N_\mu(\varepsilon/2,\delta)+O(1)
 =O\!\left(N_\mu(\varepsilon/2,\delta)
       [Lm\varepsilon^{-1/2+o(1)}+d+1]\right).
\]

Other allocations replace the half split by `u` and `epsilon-u`, and may
minimize this expression over `0<u<epsilon`; they do not bound the unknown
width threshold. To see the logical obstruction, the qualitative statement
`b_n->0` alone allows the deterministic sequence `b_n=1/log(e+n)`.
Satisfying the displayed sufficient certificate would then require
`n>=exp(1/epsilon)-e`, irrespective of order. No polynomial total-state
budget follows. This example diagnoses insufficiency of the certificate;
it is not claimed to arise from the actual network and is not a lower
bound on its true error. Passing first to a fixed-order population limit
also does not avoid the width cost of implementing its length-`n` moments.

For the desired exponent it would suffice to prove, at each fixed
confidence, `N_mu(u,delta)=u^(-2+o(1))` as an upper bound. A more primitive
sufficient estimate is

\[
 a_n=O_{\Pr}(n^{-1/2+o(1)}),\qquad
 d_{n,\mu}=O_{\Pr}(n^{-1/2+o(1)}),
\]

with deterministic subpower envelopes: the map `Phi` preserves this
exponent, giving `b_(n,mu)=O_Pr(n^(-1/2+o(1)))`, hence a sufficient
`n=epsilon^(-2+o(1))` and the requested moving-state cost. These two
quantitative estimates are the missing proof obligation under the existing
model assumptions. Neither is supplied by the fixed-program theorem, and
an initialization concentration estimate alone does not bound either
trained quantity. The manuscript must retain the width-dependent cost
above, or label the numerical exponent conditional, until that obligation
is proved.
