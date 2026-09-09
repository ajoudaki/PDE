# Three-hidden-layer arctangent extension: exact results and unresolved step

This is a proof-status audit, not a proof of the requested infinite-width theorem. It records what can be justified without a new assumption. In particular, the counterexample below refutes a width-independent continuity modulus for the vector field on bounded state sets, not convergence from the specified Gaussian initialization. Failure of that vector-field estimate is not itself failure of a stability estimate for the time-t solution map.

## Model and exact finite-width gradient flow

There is one input, equal to one, and one target, equal to one. The three hidden layers have width n. The trainable first preactivation z^(1) and rescaled output weights W^(4) are vectors in R^n; W^(2), W^(3) are n by n matrices. Put

\[
\phi(s)=\arctan s,\quad h^{(\ell)}=\phi(z^{(\ell)}),\quad
z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},
\]
\[
f_n=\frac{(W^{(4)})^\top h^{(3)}}n,\quad r_n=f_n-1,\quad L_n=r_n^2.
\]

Independently initialize z^(1)_i with N(0,1), both hidden matrices with independent N(0,1/n) entries, and W^(4)_j with N(0,1/n^2). The corresponding limiting output initialization is zero; this is not the order-one Gaussian readout in some older three-layer notes.

The rescaled preactivation derivatives are

\[
\delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\quad
\delta^{(2)}=\phi'(z^{(2)})\odot (W^{(3)})^\top\delta^{(3)},\quad
\delta^{(1)}=\phi'(z^{(1)})\odot (W^{(2)})^\top\delta^{(2)}.
\]

They satisfy delta^(ell)=n partial f_n/partial z^(ell); the loss residual is not included in delta. With the same layerwise learning-rate scaling as the two-hidden-layer model, exact continuous gradient flow is

\[
\dot z^{(1)}=-2r_n\delta^{(1)},\qquad
\dot W^{(2)}=-\frac{2r_n}{n}\delta^{(2)}(h^{(1)})^\top,
\]
\[
\dot W^{(3)}=-\frac{2r_n}{n}\delta^{(3)}(h^{(2)})^\top,\qquad
\dot W^{(4)}=-2r_n h^{(3)}.
\]

The vector blocks use squared Euclidean lengths divided by n in the parameter metric, while the matrix blocks use ordinary squared Frobenius lengths. Direct differentiation gives

\[
\dot f_n=-2r_n K_n,\qquad \dot L_n=-4r_n^2 K_n,
\]
\[
K_n=\frac{\|\delta^{(1)}\|_2^2}{n}
+\frac{\|\delta^{(2)}\|_2^2\|h^{(1)}\|_2^2}{n^2}
+\frac{\|\delta^{(3)}\|_2^2\|h^{(2)}\|_2^2}{n^2}
+\frac{\|h^{(3)}\|_2^2}{n}.
\]

Every term is nonnegative. Thus |r_n(t)| <= |r_n(0)|.

These finite equations have a unique global solution. To see this, fix T and bounds on the initial matrix operator norms, on ||z^(1)(0)||_2/sqrt(n), and on ||W^(4)(0)||_infinity. Constants below depend only on those bounds and T. Since |phi| <= pi/2 and 0 < phi' <= 1, the output equation bounds ||W^(4)||_infinity on [0,T], hence also ||delta^(3)||_2/sqrt(n). The W^(3) equation then bounds ||W^(3)||_op. Consequently ||(W^(3))^top delta^(3)||_2/sqrt(n), and therefore ||delta^(2)||_2/sqrt(n), are bounded. The W^(2) equation next bounds ||W^(2)||_op, which bounds ||delta^(1)||_2/sqrt(n) and the motion of z^(1). All bounds are finite and independent of n on the specified initial events. The finite-dimensional vector field is smooth, so boundedness on each compact interval permits continuation for all time. For Gaussian initialization the specified initial bounds hold with probability tending to one when their constants are chosen sufficiently large (and an output-coordinate bound of one suffices).

The bottom coordinate change F(s)=s+s^3/3, x^(1)=F(z^(1)), is exact for this flow:

\[
\dot x^{(1)}=-2r_n(W^{(2)})^\top\delta^{(2)}.
\]

This change is not an exact change of a discrete GD step.

## The new stability term

Only here introduce p^(2) as shorthand for the repeatedly used backward signal:

\[
p^{(2)}=(W^{(3)})^\top\delta^{(3)}.
\]

The energy and operator estimates above bound its root mean square, ||p^(2)||_2/sqrt(n), not its largest coordinate. For two states, an exact identity is

\[
\delta^{(2)}-\widetilde\delta^{(2)}
=\phi'(z^{(2)})\odot(p^{(2)}-\widetilde p^{(2)})
+[\phi'(z^{(2)})-\phi'(\widetilde z^{(2)})]\odot\widetilde p^{(2)}.
\]

The first product is bounded in root mean square by the difference of the backward signals. The second product need not be small merely because the preactivation difference is small in root mean square and the backward signal has bounded root mean square. A bounded signal's root mean square is not a bound on the operator norm of coordinatewise multiplication by that signal.

Here is a network-consistent example, not just a pair of arbitrary vectors. Let 1 denote the all-ones vector, e_1 the first coordinate vector, and b=phi(1)=pi/4. Compare two states with

\[
z^{(1)}=\mathbf1,\quad W^{(4)}=\mathbf1,\quad
W^{(3)}=\frac{\mathbf1 e_1^\top}{\sqrt n},\quad
W^{(2)}=0,\quad
\widetilde W^{(2)}=\frac{e_1\mathbf1^\top}{bn}.
\]

All unspecified blocks agree. Every matrix operator norm and vector root mean square is bounded uniformly in n, and the output coordinates are bounded. The state distance, using root mean square for vectors and operator norm for matrices, is exactly

\[
\|\widetilde W^{(2)}-W^{(2)}\|_{\rm op}=\frac1{b\sqrt n}\longrightarrow0.
\]

In the first state, z^(2)=z^(3)=0, r_n=-1, and delta^(2)=sqrt(n)e_1. In the second,

\[
\widetilde z^{(2)}=e_1,\quad
\widetilde z^{(3)}=\frac b{\sqrt n}\mathbf1,\quad
\widetilde r_n=\arctan(b/\sqrt n)-1,\quad
\widetilde\delta^{(2)}=\frac{\sqrt n}{2(1+b^2/n)}e_1.
\]

It follows that the W^(2) velocities are

\[
\dot W^{(2)}=\frac{2b}{\sqrt n}e_1\mathbf1^\top,\qquad
\dot{\widetilde W}^{(2)}=
\frac{-\widetilde r_n b}{\sqrt n(1+b^2/n)}e_1\mathbf1^\top.
\]

Their operator-norm difference tends to b, not zero. Thus there is no width-independent modulus of continuity for this vector field on arbitrary bounded sets of these state norms. The same example works with Frobenius distance for the varying matrix, since it has rank one.

These states are not asserted to arise from canonical Gaussian initialization. Consequently this example does not disprove the requested limit. It rules out deriving a width-independent vector-field continuity estimate solely from the displayed bounded-state estimates.

One useful estimate beyond those bounds would control large coordinates of the actual adaptive backward signal, uniformly over width and all approximation meshes needed in the proof. For example, exponential moment control of that signal yields an error modulus of order d log(e/d), where d is the root-mean-square preactivation error. Indeed, split the second product above at |tilde p^(2)|=R. Its root mean square is at most

\[
\|\phi''\|_\infty R d+
\frac{\|\widetilde p^{(2)}\mathbf1_{\{|\widetilde p^{(2)}|>R\}}\|_2}{\sqrt n}.
\]

A uniformly exponential squared-tail estimate lets one choose R proportional to log(e/d). Such a bound has not been proved here for the canonical trajectory or its mesh approximations. It is a sufficient strategy, not a necessary assumption of every possible proof.

## Why fixed-step Gaussian calculations do not finish this argument

At any fixed number of Euler steps, unrolling each trained matrix gives its initialization plus finitely many rank-one updates. This is the finite-computation setting of repeated-Gaussian-matrix limit arguments; a self-contained proof of that separate probabilistic theorem is not included in this audit. Even granting the fixed-step limits, what remains unjustified is a bound uniform as the number of steps tends to infinity while physical time remains fixed. The distinction between the width limit and the additional continuous-time existence/uniqueness problem is also explicit in the discussion headed “Discrete- vs Continuous-Time Gradient Descent” in [Tensor Programs IV, supplement](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf).

Even Gaussian multipliers do not repair an L2 derivative induction without a further estimate. If G is standard Gaussian and

\[
Y_m=\frac{G^m}{\sqrt{\mathbb EG^{2m}}},
\]

then E Y_m^2=1, but E[(G Y_m)^2]=2m+1. This is why a response proof cannot bound the L2 norm of every product of a Gaussian-size field and an earlier derivative by a constant times the earlier derivative's L2 norm. A proof must control their joint higher moments or exploit a different cancellation.

## Status and scope

Established in this note: exact finite equations, four-block loss dissipation, global finite-width flow, uniform compact-time root-mean-square/operator bounds on bounded initial events, and an explicit obstruction to obtaining width-independent vector-field continuity solely from those bounds.

Not established: a unique autonomous population flow for this three-hidden-layer Gaussian model; uniform passage from finite meshes to continuous time; the joint width/learning-rate limit of raw GD; or convergence of all four raw kernel blocks. In particular no learning-rate extension is certified here merely by copying the two-layer estimate.

The older local draft /tmp/L3_SELF_CONTAINED_PROOF.md uses a different activation (sin+cos), a short-time restriction, and a response-norm argument requiring repair. The prior project audit studies/d3_arctan_closure_program/FINAL_CONVERGENCE_AUDIT.md identifies the same middle-product problem, but its older order-one Gaussian output initialization must not be conflated with the vanishing output initialization here. Independent route checks in this investigation explicitly used the latter initialization. None supplied the missing unconditional estimate or an alternative complete proof.

Therefore the requested theorem has not been resolved by this work. Neither a formal limiting equation nor a conditional tail-based theorem should be reported as its proof.
