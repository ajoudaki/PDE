# Initial frozen NTK comparison at matched loss

User-authorized extension of the first-quadrant study, 2026-09-14. Only this
study, its generated products and the maintained code/docs are scientific
inputs. No other study source, results or implementations are used. The side-task
owns NTK_COMPARE.py, NTK_PLOTS.py, this plan, a scoped README update and the new
`data/generated/quadrant_network_closure/ntk_001/` output namespace. No subagents,
GPU access, new network training, edits to previous outputs or shared Git writes.

Compare the maintained two-hidden-layer tanh model with its full initial
mobility-weighted tangent kernel, retaining the original width8192 seeds11/29/47,
their float32-stored initial parameters and physical block mobilities(n,1,n).
Regenerate initial arrays from the recorded PCG64 stream, verify their float64
hashes, cast to float32, and evaluate these rounded values in float64 on CPU.
Use the recorded 16 training inputs and 1448 dense circle directions, with
training inputs rounded as in the original network calculation. Coefficients
may use initialization, training inputs and labels only; stopping times may use
the corresponding network's final scalar training loss.

For residual-free initial backward fields delta1,delta2, unit inputs u,v and
hidden activations h1,h2, the maintained finite_network.kernel_blocks gives

    K1(u,v) = (u·v)(delta1(u)·delta1(v))/n
    K2(u,v) = (h1(u)·h1(v))(delta2(u)·delta2(v))/n²
    K3(u,v) = h2(u)·h2(v)/n.

Let K=sum K_l(X,X)=V diag(lambda) V^T. On the original unhalved-MSE clock,

    r(t) = V diag(exp(-2t lambda/16)) V^T (f0(X)-y),
    f(t,u) = f0(u) - K(u,X)V diag(q_t(lambda))V^T(f0(X)-y),
    q_t(lambda) = -expm1(-2t lambda/16)/lambda; q_t(0)=2t/16.

For each of the three fixed seeds, bracket the first time at which training MSE
equals that seed's network MSE at T=100 using at most60 time doublings from100,
then90 bisections. Plot the mean matched-loss NTK alongside unchanged network
and N1/N3/N5 endpoint outputs. Record an NTK loss trajectory at the original201
times and a logarithmic continuation to the matched endpoint. Do not place
matched-time predictions on a common-time axis. No fitting to passive outputs,
kernel regularization, eigenvalue clipping, or parameter/seed search.

Numerical gates: nonzero-readout cross-kernel check against maintained oracle
within2e-12; spectral solution versus augmented matrix exponential within2e-11,
including a singular test; regenerated initial training predictions within3e-9
and initial training G2 within3e-6 of saved observations; positive training
kernel eigenvalues, symmetry error at most1e-12; matched MSE error below1e-9;
training prediction identity below1e-7. Verify matched propagation on64 uniformly
spaced angles plus all training inputs using70-decimal arithmetic, prediction
error below1e-6 and loss error below1e-9. High-precision checks establish arithmetic
accuracy for the reconstructed finite kernel, not a width limit or population bound.

Report training MSE and whole-circle output RMSE/max discrepancy from the network,
using the original1440 uniform indices for circle metrics. No method is required
to win. Preserve original curves and inputs exactly; old numerical limitations
remain in force. If radius2+f becomes nonpositive, increase the common reference
radius to ceil(max absolute output)+1 and label it; never clip predictions.

Update five meaningful figures (radial overlay, individual radial views, output
versus angle, training predictions, loss/Gram overview), add one NTK stopping-time
figure, and retain the seven other original figures in a combined13-page PDF.
The output-only NTK has no separately defined nonlinear hidden activations;
keep existing frozen-initial-Gram baselines labelled as frozen hidden features,
not an NTK Gram evolution. Budgets: three initial-kernel evaluations, two CPU
BLAS threads, at most300 seconds execution, 3GiB resident memory and100MiB new
outputs. Retain failures and stop at numerical failure; no unplanned runs.
