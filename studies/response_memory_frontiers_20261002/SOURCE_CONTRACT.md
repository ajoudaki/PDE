# Source and model contract

Root completed the full current manuscript and all included mathematical files:
`main.tex` (1620 lines), `results.tex` (233), `proof_alltime.tex` (928),
`proof_tracking.tex` (319), `proof_finite_time.tex` (502),
`comparison_appendix.tex` (327), `sphere_appendix.tex` (29), including all
figure captions. No nested mathematical includes were omitted. Initial hashes
are in the startup manifest. Required `docs/index.qmd`, `docs/notation.qmd`,
AGENTS and workflow Part 1 were read. The maintained implementation README was
inspected only in part; no maintained API is currently used or changed. New
experimental code must either be self-contained or finish the relevant API
reading before use. No prior study is a scientific dependency.

## Canonical starting model

For m fixed examples, n neurons and L hidden layers, first preactivations are
W^(1)x/sqrt(d), hidden preactivations W^(ell)h^(ell-1), and scalar output
f=w^T h^(L)/n. Residual r=f-y, unhalved mean squared loss and rho=sqrt(mean r²).
Backward response delta=n partial f/partial z excludes the residual. Block
mobilities are (n,1,...,1,n). The initial readout in the main theorem is exactly
zero; first weights have iid N(0,1) entries, hidden weights iid N(0,1/n).

The closure stores RAW moments bar h and bar delta, not normalized histories:

    tau(0)=1, tau_dot=rho;
    bar h_k = integral_0^tau h(xi) p_k(xi/tau) dxi;
    bar delta_k = integral_0^tau (r delta/rho)(xi) p_k(xi/tau) dxi.

The unit prefix has constant initial forward features and zero backward signal.
Only bar h_0 is initially nonzero. With p_k(1)=1 and integral p_k²=1/(2k+1),
both moment equations use the triangular dilation
`k M_k + sum_{j<k}(2j+1)M_j`; their physical sources are rho h and r delta.
Every learned hidden matrix is reconstructed as

    W_hat = W0 - 2/(mn tau) sum_{a,k<q} (2k+1) bar delta_ak bar h_ak^T.

All forward/backward signals are evaluated in this reconstructed network.
The raw system never divides by rho. Any forward normalized key at q=1 would
be bar h_0/tau. More precisely, a reconstruction
W0+(mn)^(-1) sum v_a k_a^T requires
`k_a=bar h_a0/tau`, `v_a=-2 bar delta_a0`. These derived coordinates are not used
as a replacement notation in this study.

## Exact foothold

Let h*,b* be current-endpoint values of the projected forward history and
b=r delta/rho history. The induced hidden physical velocity differs from the
canonical gradient flow at the same current network by

    E_ell = 2 rho/(mn) sum_a (b_a-b*_a)(h_a-h*_a)^T.

Its time-integrated norm is bounded by the product of the two L² history
projection tails, because growing-interval projection error obeys
`D_u_dot=rho ||u-u*||²`. Both the pairing and the endogenous feedback are
essential. Small observable error alone says nothing about hypergradients,
long-time stability, changed data schedules, optimizer geometry or new
architectures without another argument.

## What the manuscript actually proves

The all-time q^(-2+o(1)) approximation is for fixed depth/data, smooth globally
Lipschitz gates, a positive initial feature-Gram gap and sufficiently small
fixed labels. It gives fitting at every order and an order-independent width
remainder, not a quantitative width rate or unique fixed-order moment law.
The broader finite-width compact-horizon theorem has O(1/q) error and does not
require fitting. Its constants may depend on width and the entire horizon.
The joint-clock O(1/q²) theorem changes the coordinate, tracks a nontrivial
Gram matrix and assumes additional regularity; it is not an automatic upgrade
for discontinuous schedules or stochastic updates.

## Extension ledger

Attention, recurrence/equilibrium and controlled curricula are NEW models.
Their matrix-gradient factorization is to be derived independently and each
new clock/prefix/normalization specified. No all-time, Gaussian population or
compression conclusion transfers merely by applying the algebra to a block.
Total state includes W0, external data, solver workspace and optimizer state.
Temporal truncation and spatial rank truncation are distinct approximation axes.

GPU environment verified outside sandbox: two RTX3090 24GiB, idle at startup,
`/home/amir/miniconda3/bin/python`, PyTorch2.9.0+cu130. GPU commands need sandbox
escalation because /dev/nvidia* is hidden inside the sandbox; authorization
comes from the user's ongoing experimental request. No packages installed.
