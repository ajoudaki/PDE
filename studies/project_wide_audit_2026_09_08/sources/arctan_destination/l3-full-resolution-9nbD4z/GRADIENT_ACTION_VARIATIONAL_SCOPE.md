# A precise limitation of prediction and action bounds

This is a counterexample to a proposed general inference about gradient
flows, not to the canonical Gaussian network. It shows that bounded
gradient, a finite feature horizon ending at interpolation, and the exact
loss/action identity do not themselves bound positive transverse
variational amplification.

For each positive integer N, on R x R^N define the smooth predictor

    f_N(x,y)=x+sum_{j=1}^N 2^(-3j)[1-cos(2^(2j)y_j)],

and loss L_N=(f_N-1)^2. Its gradient is

    grad f_N=(1, (2^(-j) sin(2^(2j)y_j))_{j=1}^N),

so ||grad f_N||^2 <= 1+sum_{j>=1}4^(-j)=4/3 everywhere,
uniformly in N. Begin at x=0,y=0. Its feature-time gradient-ascent
trajectory is exactly

    x(s)=s,       y(s)=0,       f_N(s)=s,       0<=s<=1.

Thus the feature horizon to interpolation is one, and along this path

    ||grad f_N||^2=1,       integral_0^1 ||grad f_N||^2 ds=1.

The exact squared-loss physical flow is

    x(t)=1-exp(-2t),       y(t)=0,
    L_N(t)=exp(-4t),
    integral_0^infinity ||theta'(t)||^2 dt=1.

In particular all predictions lie between zero and one, the readout-like
direction has a uniformly positive kernel, and the total action is fixed.

Nevertheless the feature-time variation from initial direction e_j in
the y coordinates is

    v_j(s)=exp(2^j s)e_j,

because the corresponding Hessian entry on the baseline path is 2^j.
In physical time it is

    v_j(t)=exp(2^j[1-exp(-2t)])e_j.

The residual variation vanishes to first order in this transverse
direction, so the displayed physical variational formula includes the
loss multiplier correctly. For every fixed positive time before the
feature horizon, its amplification is unbounded as N increases. Yet
the actual prediction and its rate are independent of N. All these
claims involve smooth finite-dimensional objectives; no infinite-
dimensional differentiability assumption is needed.

Therefore positive transverse Hessian growth need not force a larger
actual prediction rate or consume a larger actual action budget. A
signed inequality that closes the network problem must use additional
canonical network structure linking the particular perturbations to
the actual Gaussian trajectory. The example has neither that network
architecture nor its initialization and does not refute its theorem.

For the Gaussian action decomposition, moving the problematic pairing
across the adjoint only gives

    <q, phi''(Z2) v^2>
       = <delta3, W3[phi''(Z2) v^2]>.

The established operator bound estimates the right side using
||v^2||_2=||v||_4^2. It does not reduce it to the L2 size of v. The
creation/adjoint decomposition preserves this missing integrability
requirement; no signed commutator estimate eliminating it has been
proved here.
