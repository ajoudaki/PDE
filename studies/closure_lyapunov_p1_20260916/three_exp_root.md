# Root route: a nonlinear exponential potential on a declared bounded-readout region

2026-09-16. This is a new conditional construction for the exact initialized
canonical p=1 closure. It uses the full physical-time energy identity and
the exact upper-feature compactness theorem in generic3_stationary_geometry.md.
It does not establish that a generic trajectory remains in the region used
below. It is not the requested unconditional theorem from initialization.

The user now permits any increasing comparison between potential and loss,
not just a power. This makes a nonlinear dissipation modulus sufficient.
The construction here obtains such a modulus without assuming a uniformly
positive complete feature Gram, or monotonic individual hidden distances.

## 1. Fixed information and a compact current-feature problem

Fix numbers C>0 and 0<ell<1/3 BEFORE using the construction. These are
declared bounds, not values defined by the unknown future trajectory.
Consider the part of a canonical trajectory on which

    ||c||_(L2) <= C,             L <= ell.

The same target and metric as the study apply: three equally weighted
circle inputs, labels (+1,+1,-1), and unhalved square loss. Write
V_i=y_i H_i and m_i=y_i f_i. The exact readout equation and loss are

\[
 \dot c=\frac23\sum_i(1-m_i)V_i,
 \qquad \mathcal L=\frac13\sum_i(m_i-1)^2.
 \tag{1}
\]

Let K be the L2 closure of {tanh(Z dot v):v in R2}, where Z is the
canonical fixed upper mark. By the complete proof in
generic3_stationary_geometry.md, K is compact and adds only the functions
sign(Z dot d), |d|=1, to the finite tanh fields. Distinct nonzero members
of any triple are independent after grouping equal/opposite fields.

For V in K^3 put G_ij=E[V_i V_j]. Define the compact feasible set Omega
of pairs (V,m) by the two conditions

\[
 0\le \frac13\|m-\mathbf1\|^2\le\ell,
 \qquad
 \begin{pmatrix}G&m\\m^T&C^2\end{pmatrix}\succeq0.
 \tag{2}
\]

The block positivity is exactly the existence of a readout of norm at
most C realizing those three margins. To check this without assuming an
invertible Gram, block positivity gives

    |a dot m| <= C sqrt(a^T G a)   for every a in R3.

Thus the assignment sum a_i V_i -> a dot m is well defined on their
finite-dimensional span and bounded by C times its L2 norm. Its Riesz
representative within that span has norm at most C and the prescribed
pairings. Conversely any such readout gives (2) by expanding the squared
norm of sum a_i V_i plus a scalar multiple of c, and adding the unused
nonnegative amount C^2-||c||^2 to the last diagonal entry. This verifies
both directions including singular G.

Compactness follows from compact K^3, the bounded closed margin ellipsoid,
continuity of all Gram entries in L2, and closedness of positive
semidefiniteness. No compactness of the full neural state is asserted.
For an explicit finite-dimensional parameterization, write v=z/(1-|z|)
for |z|<1 and use sign(Z dot z) at |z|=1. This maps the closed unit disk
continuously into L2 and onto K, by the same dominated-convergence proof.
The minimizations below therefore use three closed two-dimensional disks
and three bounded scalar margins. No future trajectory appears in them.

Define on Omega

\[
 A(V,m)=\frac49(\mathbf1-m)^TG(\mathbf1-m),
 \qquad E(m)=\frac13\|m-\mathbf1\|^2.
 \tag{3}
\]

At an actual current state these are ||dot c||^2 and L respectively.
Crucially,

\[
                  A(V,m)=0\quad\Longrightarrow\quad E(m)=0.
 \tag{4}
\]

Here is the full argument. Every feasible m_i is at least
1-sqrt(3ell)>0. By the representative readout from (2), a zero V_i
would force m_i=0, and an opposite pair would force m_i=-m_j; both
are excluded. Equal fields have equal margins. The equality A=0 means
sum_i (1-m_i)V_i=0 in L2. Group equal fields; the remaining nonzero
fields have no opposite pair and are independent. Each group's
coefficient is its size times 1-m_i, so all margins equal one. This
proves (4). Compatible same-class feature coincidences are allowed.

## 2. The explicit scalar modulus and potential

For 0<=s<=ell define, with an empty inner minimum interpreted as infinity,

\[
 d(s)=\min\left\{s,\ \min_{(V,m)\in\Omega}
                   \big[A(V,m)+(s-E(m))_+\big]\right\}.
 \tag{5}
\]

This is a fixed variational definition from the known mark law and the
declared C,ell. It does not minimize over learned endpoints or trajectories.
Each function inside the minimum is nondecreasing and 1-Lipschitz in s;
the same is true of their infimum, and d(0)=0, 0<=d(s)<=s.
For s>0 the value is strictly positive. If Omega is empty, d(s)=s.
Otherwise its inner minimum is attained by compactness. A zero value
would require A=0 and E>=s; (4) instead requires E=0, a contradiction.

At a current state satisfying the bounds, use that very pair (V,m) in
(5), with s=L=E(m), to obtain d(L)<=||dot c||^2. Exact energy gives

\[
                   \dot{\mathcal L}\le-d(\mathcal L).
 \tag{6}
\]

Define the current-state potential

\[
 \Phi(S)=
 \begin{cases}
 \displaystyle\exp\!\left[-\int_{\mathcal L(S)}^{\ell}
                                    \frac{ds}{d(s)}\right],
                      &0<\mathcal L(S)\le\ell,\\
 0,                   &\mathcal L(S)=0.
 \end{cases}
 \tag{7}
\]

Since d is continuous and positive away from zero, the integral is finite
at every positive lower endpoint. Since d(s)<=s, it tends to infinity
as that endpoint tends to zero. Consequently Phi is continuous and
strictly increasing as a function of loss on [0,ell], from zero to one.
Let h:[0,1]->[0,ell] be its scalar inverse. It is continuous and increasing,
with h(0)=0, and is determined by exactly the same fixed information.

For any interval on which the declared bounds hold and L>0, the chain
rule, INCLUDING all dependence of (7) on the evolving state, gives

\[
 \dot\Phi=\frac{\Phi}{d(\mathcal L)}\dot{\mathcal L}
             \le-\Phi,
 \qquad \mathcal L=h(\Phi).
 \tag{8}
\]

At zero loss all physical velocities vanish, so continuation is constant.
Thus if the bounds hold for every t>=t0,

\[
 \Phi(S_t)\le e^{-(t-t_0)}\Phi(S_{t_0}),
 \qquad
 \mathcal L(t)\le h\big(e^{-(t-t_0)}\Phi(S_{t_0})\big).
 \tag{9}
\]

For each 0<epsilon<L(t0), the equally explicit finite horizon is

\[
             t-t_0\ge\int_\epsilon^{\mathcal L(t_0)}\frac{ds}{d(s)}.
 \tag{10}
\]

There is no claim that h is a power or that the loss itself decays
exponentially. The unit exponential rate in (8) fixes a normalization of
the transformed potential; the actual difficulty and geometry of fitting
remain in the inverse comparison h and in the declared readout bound.

## 3. What this resolves, and what it does not

This is an explicit future-free exponential potential with a monotone loss
comparison for a rigorously specified conditional regime. It refines the
previous compactness-only bounded-readout theorem into a nonlinear
dissipation law and a defined training horizon. The geometry enters through
the exact compact family of signed upper features, allowing arbitrary
fluctuations and compatible coincidences. The training metric is unchanged.

It does NOT prove a canonical generic trajectory reaches L<1/3 or remains
under any declared C. Taking C to be an unevaluated future supremum would
not discharge that assumption. The unrestricted-state obstruction in
three_exp_invariant.md shows precisely why simply removing C cannot work
for a loss-only modulus: readout norms may diverge while a fixed positive
loss has arbitrarily small full gradient. Those constructed states are not
known to be reached, so they do not refute an initialized mixed potential.

The construction was supplied to the invariant-route author only after
that author's independent route was frozen. Its separate bounded check
is recorded in three_exp_reparam_check.md. Root checked the PSD equivalence,
singular groups, sign-function boundary, positivity and continuity of d,
the zero endpoint, chain rule and finite tolerance horizon. No computation
or external convergence theorem is used in this proof.
