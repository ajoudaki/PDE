# Fixed positive-time population gradient flow beyond arctan

The proved extension permits **every fixed finite number of hidden layers**,
different activations at different layers, any fixed finite dataset, and a
nonvanishing subGaussian stored readout at initialization. Its positive
physical-time interval is independent of width and the vanishing GD step.
The full statement and proof are in
[GENERAL_POPULATION_GF_PROOF.md](/tmp/pde-gf-supervisor-worktree/GENERAL_POPULATION_GF_PROOF.md),
with the necessary detailed estimate in
[GENERAL_DEPTH_RESPONSE_PROOF.md](/tmp/pde-gf-supervisor-worktree/GENERAL_DEPTH_RESPONSE_PROOF.md).

The activation assumption is

\[
\phi^{(\ell)}\in C^1(\mathbb R),\qquad
\sup_s|\phi^{(\ell)\prime}(s)|<\infty,\qquad
|\phi^{(\ell)\prime}(s)-\phi^{(\ell)\prime}(t)|\le D_2|s-t|.
\]

Activation values may be unbounded. This includes arctan, tanh, sigmoid,
softplus, GELU, SiLU, and continuously differentiable quadratic smoothings
of ReLU. ReLU itself is outside this proof because its derivative jumps.
No oddness, monotonicity, analyticity, or derivative lower bound is required.

Inputs satisfy a fixed bound on \(\|x_a\|_2/\sqrt d\), and labels are bounded.
For the weighted loss \(\sum_a\omega_a(f_a-y_a)^2\), with positive weights
summing to one, the time can be chosen independently of the number of
examples and their angles. The inputs and their number are still fixed in
the width limit. For summed loss, physical time is rescaled by the number
of examples.

First-weight entries can be iid centered subGaussian variables. Middle
matrices remain independent Gaussian matrices with variance
\(\sigma_\ell^2/n\). The stored readout may have any fixed iid subGaussian
law, including zero or an order-one Gaussian law. Perturbations vanishing
in the stated RMS/operator distance are also covered; in particular every
polynomially vanishing Gaussian readout scale is allowed.

The stored learning-rate multipliers are

\[
(n\kappa_1,\kappa_2,\ldots,\kappa_L,n\kappa_{L+1}).
\]

There is \(T_*>0\) such that **for every sequence \(\eta_n>0\) tending to
zero**, GD at physical time \(t=k\eta_n\) converges to the unique population
flow on \([0,T_*]\). Predictions, loss, and kernel entries converge uniformly
in probability; joint hidden path laws converge with second moments in the
uniform path norm; integrated squared hidden speeds converge. There is no
condition linking \(\eta_n\) to a power of width. The time can depend on
depth, activation bounds, initialization scales, label/input bounds, and
learning multipliers. A bound uniform in depth is not claimed.

For two hidden layers the population equations retain the concrete network
operations:

\[
H_a^{(1)}=\phi^{(1)}(Z_a^{(1)}),\quad
Z_a^{(2)}=W^{(2)}H_a^{(1)},\quad
H_a^{(2)}=\phi^{(2)}(Z_a^{(2)}),\quad
f_a=\mathbb E[W^{(3)}H_a^{(2)}],
\]
\[
\delta_a^{(2)}=W^{(3)}\phi^{(2)\prime}(Z_a^{(2)}),\qquad
\delta_a^{(1)}=\phi^{(1)\prime}(Z_a^{(1)})(W^{(2)})^*\delta_a^{(2)},
\]
\[
\begin{aligned}
\dot Z_a^{(1)}&=-2\kappa_1\sum_b\omega_bG_{ab}r_b\delta_b^{(1)},\\
\dot W^{(2)}&=-2\kappa_2\sum_b\omega_b r_b\delta_b^{(2)}\otimes H_b^{(1)},\\
\dot W^{(3)}&=-2\kappa_3\sum_b\omega_b r_bH_b^{(2)}.
\end{aligned}
\]

Here \(G_{ab}=x_a^\top x_b/d\), \(r_a=f_a-y_a\), and
\((u\otimes v)V=u\mathbb E[vV]\). The two neuron populations are separate;
each expectation pairs fields in one population. \(W^{(2)}\) acts from the
first to the second, and its adjoint acts back. This state is autonomous but
has infinitely many scalar degrees of freedom.

The loss can also be \(\sum_a\omega_a\ell_a(f_a)\), provided the derivatives
\(\ell_a'\) are locally bounded and locally Lipschitz with common bounds on
bounded prediction intervals. Replace \(2r_b\) in the updates by
\(\ell_b'(f_b)\). Convexity is unnecessary for this local theorem.

The proof first bounds RMS fields and operator norms. The response lemma
then bounds each backward-slot sensitivity by \(C\Delta\omega_b\) and
controls marginal subGaussian tails uniformly in the number of Euler
steps. It uses weighted time sums, not maxima over a refining Gaussian
history. Localization consequently gives an error estimate of the form

\[
C e^{C(1+R)T_*}
\left[(1+R)(\eta_n+\Delta)+e^{-cR^2}+o_{\mathbb P}(1)\right].
\]

The width limit is taken at fixed cutoff \(R\) and oracle mesh \(\Delta\),
then \(\Delta\to0\), then \(R\to\infty\). This makes the fixed-time
interval survive the joint width/step limit. The only fixed-program
external input is the Gaussian matrix/transpose response theorem of
[Tensor Programs III](https://arxiv.org/pdf/2009.10685); the uniform estimate
and continuous-time comparison are supplied in the proof files.

Genuine nonlinear feature movement is separately proved for **two hidden
layers**, zero limiting readout, Gaussian first initialization, positive
initialization and training scales, normalized pairwise nonparallel inputs,
nonzero labels, and both activations nonaffine. On a possibly smaller fixed
interval, every input's hidden preactivation and activation RMS displacement
is of order \(t^2\), with a strictly positive coefficient, and its RMS speed
is of order \(t\). The middle matrix acts differently on every initial
feature, the kernel changes, loss strictly decreases, and affine-fit errors
stay positive. These assertions are detailed in
[ACTIVITY_SOURCE_AUDIT.md](/tmp/pde-gf-supervisor-worktree/ACTIVITY_SOURCE_AUDIT.md).
Existence at greater depth does not by itself establish these stronger
per-layer activity assertions there.

No all-finite-horizons theorem, non-Gaussian middle-matrix universality, or
claim of publication priority is made.
