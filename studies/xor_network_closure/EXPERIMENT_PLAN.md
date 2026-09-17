# Shifted four-pole XOR comparison through T=100

The user chose to retain the bias-free model and move the pole angles so that
same-label inputs are not antipodal. Root's declared centers are 0° (+1), 90°
(−1), 150° (+1), 240° (−1). Each pole has the same four offsets
−5°, −5/3°, +5/3°, +5°, giving 16 equally weighted deterministic inputs.
The data seed is therefore inapplicable. The two class convex hulls must intersect;
check this by intersecting the two segments joining their respective pole means.
Also verify no same-label pair is antipodal, including the full ±5° arcs. No
angle selection or adjustment based on training results is permitted.

This is a nonlinear classification stress, not a claim that fitting nonlinear
labels necessarily requires hidden feature learning. The matched frozen-feature,
trainable-readout baseline below tests that additional mechanism.

## Model and retained information

Use the established two-hidden-layer tanh network and observable solver without
changing code/. Unit directions u=(cos θ,sin θ) correspond to physical x=√2 u.
Finite forward equations: h1=tanh(W1 u), h2=tanh(W2 h1), f=cᵀh2/n. Initialization
is independent Gaussian W1 entries variance 1, W2 variance 1/n, stored c variance
1/n². Physical block mobilities are (n,1,n), loss is the unhalved mean squared
training residual, and all blocks evolve by simultaneous explicit Heun steps.
No bias, whitening, output rescaling, clipping, minibatches or optimizer change.

The closure uses the maintained initialized joint populations and moving w,c,M,
including Mᵀ in backpropagation. Order N, coefficient integration Q, population
quadrature P and time step are distinct approximation axes. Its initial c=0.
It receives only inputs and labels, never network trajectories or fitted coefficients.
The new law and T=100 are exploratory, outside the maintained proved data/horizon
contract. No convergence theorem is claimed.

Eight network runs: widths 2048 and 8192, each at seeds 11,29,47, float32 h=0.01;
plus width8192 seed11 h=0.005, and width2048 seed11 float64 h=0.01. Draw Gaussian
arrays with NumPy default_rng in the established block order in float64 before
casting; preserve initialization hashes. Disable TF32 and reduced-precision
matmul accumulation. GPU workers use two GPUs, one concurrent network per GPU.

Eight closure runs: N=1,3,5 each with Q=2048/P=1024 and Q=4096/P=2048, h=0.01;
plus N3 Q2048/P1024 h=0.005 and N5 Q4096/P2048 h=0.005. Use float64 and the
maintained order-dependent ridge, without modifying initialization tolerances.
Two CPU closure workers maximum; one BLAS thread per worker.

## Observations and baselines

Save every 0.5 physical time from 0 to100 inclusive (201 observations). At each
time save predictions on all 16 training inputs and a passive 128-point full circle,
the training loss, both full hidden Grams on the combined 144-point panel, and both
layers' RMS movement from their own initial activations. Gram accumulation is
float64. Panel order is training first, circle second. Retain actual endpoint
states or solver restarts for every successful run, plus initial-state hashes.

Network Gℓ(a,b)=hℓ(ua)·hℓ(ub)/n; closure uses its population weights. Reference
Grams are the three-seed means separately at each width; mean loss averages
individual losses. Compare both G(t) and ΔG(t)=G(t)−G(0). For m-point panels use
matrix RMS ||A||F/m. Report training and passive-circle panels separately.

Frozen-Gram baseline is the reference mean G(0). The stronger loss control freezes
both hidden layers but trains the readout with its original physical mobility.
For each network initialization its exact training evolution is
f(t)=y+exp(−2tK/m)(f(0)−y), K=G2(0) on training inputs, m=16. This deterministic
linear solve needs no additional training campaign. Retain per-seed and mean
loss curves. It is a readout-only control, not the full frozen tangent kernel.

## Gates, interpretation and stop

Before GPU training, independently check the fresh finite RHS against maintained
finite_network and torch autograd on nonzero small random states, including every
block, the MSE factor and physical mobilities. Check Gram diagonals/RMS identities
and the frozen-readout formula at zero time and against its differential equation.
Check closure Gram observations against maintained fields and a save/load restart.
These are deterministic implementation checks, not exploratory training pilots.

All 16 runs must record exact observation counts/times, finite arrays, symmetric
bounded Grams and endpoint PSD (tolerance 2e−10), and scalar identities. Relative
rounding tolerance is 3e−6 for float32 observables and 2e−10 for float64. Flag any
sampled loss increase exceeding max(1e−6,1e−4 times preceding loss). No silently
dropped observations, resumed failed trajectories or outcome-dependent retries.

Numerical time/precision controls must have maximum absolute loss and matrix RMS
G/ΔG discrepancies ≤0.002 over both panels; record each separately. Each N's two
quadrature resolutions use the same diagnostic cutoff. Failure marks that axis
unresolved, not a failed hierarchy theorem. Comparisons against networks are
descriptive if their relevant numerical controls fail.

Operational agreement: maximum loss discrepancy ≤0.02 and Gram RMS discrepancy
≤0.05, separately by layer and panel. Report exact values and all order rankings;
these thresholds are declared conventions. Nontrivial movement requires maximum
frozen-Gram error >0.02. A closure improves on freezing if its maximum Gram error
is at most half the frozen baseline's, separately by layer/panel. A hidden-training
advantage is supported only if the width8192 mean terminal loss is at most half
the matched readout-only loss with an absolute loss improvement ≥0.05. Mere
nonlinear-label fitting or nonzero Gram movement does not establish this advantage.
Terminal loss ≤0.01 is the declared fitting diagnostic. Preserve adverse outcomes.

Hard stop: common T=100, no horizon extension; maximum 20 minutes of scientific
wall time from first trajectory, 600 seconds per worker, 8 GiB generated products,
3 GiB minimum free disk. No search grid or additional widths/seeds beyond this list.
An exceeded bound or numerical failure stops that run and is recorded; unaffected
predeclared runs may finish within the global cap. Stop all active work at the
global cap. No further experimental branch is authorized by this plan.

All new source/configuration files stay flat in studies/xor_network_closure/;
all generated artifacts use one fresh data/generated/xor_network_closure/run_001/.
Freeze input, plan and producer hashes before the first trajectory. Save exact
commands, environment, hardware, timestamps, exit statuses and output hashes.
Root owns plan, shared input preparation, coordination, analysis and plots;
fresh scoped agents own independent finite and closure runners. A separate raw
arithmetic check will inspect frozen outputs without reading the main analysis.
