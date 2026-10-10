# Simultaneous input nonlinearity and feature-learning certificates

Date: 2026-10-10. Continuation of this study's mechanism certificate. This
addition resolves the distinction between nonlinear dependence on labels and
nonlinear dependence on inputs. It changes neither the dense dynamics nor
the compression algorithms. No live paper edit or book promotion is made.

## Statement

Use the paper's Gaussian-initialized fixed-depth network, zero readout,
mean-square loss, mobilities `(n,1,...,1,n)`, and compression assumptions.
Assume \(m\ge2\), every activation is nonaffine and paper-admissible (analytic with
bounded strip derivative, values possibly unbounded), the fixed labels are
nonzero, and distinct training inputs satisfy \(|x_a^\top x_b|<d\).
These additional activity assumptions are local to this corollary, not
restrictions on the general compression theorem. They imply \(d\ge2\).

There are four deterministic passive inputs on the input sphere and constants
\(c,t_*>0\), all depending on the fixed problem but not on width, with the
following property. For every fixed \(0<t\le t_*\), simultaneously for
Legendre, Harmonic and Taylor, with probability tending to one as width grows,

\[
 \inf_{a\in\mathbb R^d,\,b\in\mathbb R}
 \sup_{x\in\mathcal X}|f_{\rm model}(t,x)-a^\top x-b|
 \ge ct,                                                   \tag{1}
\]

\[
 \sup_{x\in\mathcal X}
 |f_{\rm model}(t,x)-f_{{\rm NTK},n}(t,x)|\ge ct^3.          \tag{2}
\]

Here \(f_{{\rm NTK},n}\) is the frozen initial tangent-kernel flow of the
coupled dense reference, not the compressed model's own tangent kernel.
Legendre and Harmonic use their whole-sphere domain. Taylor uses its declared
panel augmented, if necessary, by these four passive inputs; no labels for
them are used. Every hidden layer of the dense reference also has normalized
joint training-feature squared displacement at least a positive constant
times \(t^4\), with the same fixed-time probability convention.

All compression errors still tend to zero, and the original stronger
comparison to actual dense-run variability is unchanged. The first separation
excludes every deep linear network, even allowing biases, arbitrary training,
and a moving kernel: its predictor at a given time remains affine in the raw
input. The second separation, together with actual layerwise motion, excludes
the same-initialization frozen-feature explanation. The original
label-superposition corollary separately excludes a common label-linear
prediction rule across labels \(y\) and \(y/2\).

These conclusions distinguish two observable properties. They do not claim
that the nonlinear component of each hidden representation moves, or that
every imaginable label-dependent fixed feature representation is excluded.

## 1. The initial prediction velocity is not affine

Write \(v=x/\sqrt d\). At initialization the population top-feature covariance
has the rotationally invariant form

\[
 K_0(v,u)=F_L(v^\top u),\qquad \|u\|=\|v\|=1.
\]

The exact zero-readout velocity converges at every fixed finite list of queries
to the deterministic function

\[
 g(v)=\frac2m\sum_{a=1}^m y_a F_L(v^\top v_a).              \tag{3}
\]

We prove that (3) is non-affine for every nonzero label vector under the
stated geometric assumptions, including labels that are linearly realizable
on the training set. No nonlinear target assumption is added.

Here is a self-contained kernel argument. A continuous nonaffine activation
with bounded derivative has at most linear growth and is not a polynomial.
Its Gaussian Hermite expansion is therefore square summable with infinitely
many nonzero coefficients. For normalized Hermite polynomials and correlated
standard Gaussians, the identity
\(\mathbb E[H_j(G)H_k(G')]=\mathbf1_{j=k}r^k\) shows that the corresponding
covariance function has nonnegative power-series coefficients. The identity
follows by comparing coefficients in
\(\mathbb E[e^{sG-s^2/2}e^{tG'-t^2/2}]=e^{rst}\).
Completeness of the Gaussian polynomial system can be seen by taking the
Gaussian-weighted exponential transform of a function orthogonal to every
polynomial: its entire transform has every derivative zero, hence vanishes,
and Fourier uniqueness gives the zero function. Finite Hermite support would
make the continuous activation a polynomial everywhere, and its bounded
derivative would then make it affine.

At each layer compose that covariance series with the preceding covariance
divided by its positive marginal variance. Starting from \(F_0(s)=s\), all
coefficients remain nonnegative. If the preceding series has a positive
coefficient at degree \(j\ge1\), a positive outer coefficient at degree
\(k\) contributes positively at degree \(jk\). Nonzero constant terms
cause no problem: nonnegative series permit regrouping, and evaluating at
one gives the finite Gaussian second moment. Consequently

\[
 F_L(s)=\sum_{k=0}^\infty c_k s^k,\qquad
 c_k\ge0,\quad\sum_k c_k<\infty,
\]

with unbounded positive support and uniform absolute convergence for
\(-1\le s\le1\).

For this paragraph only let \(P\) be the orthogonal projection onto affine
functions on the unit sphere with normalized surface measure \(\sigma\):

\[
 (Ph)(v)=\int h(u)\,d\sigma(u)
       +d\,v^\top\int u h(u)\,d\sigma(u).
\]

Applying \(I-P\) to both variables of the positive kernel \((v^\top u)^k\)
gives another positive kernel

\[
 R_k(v,u)=(v^\top u)^k-a_k-b_kv^\top u,
\quad
 a_k=\int(z^\top u)^k\,d\sigma(z),\quad
 b_k=d\int(z^\top u)^{k+1}\,d\sigma(z).
\]

Rotational invariance makes \(a_k,b_k\) independent of unit \(u\).
Projection in either variable subtracts exactly the displayed affine part;
projection twice gives the same result. Positivity follows directly by
projecting each coordinate of the tensor feature \(v^{\otimes k}\): the
resulting feature Gram is \(R_k\).

Since \(d\ge2\), \(|z^\top u|<1\) almost everywhere in surface measure,
and dominated convergence gives \(a_k,b_k\to0\). The nonparallel input
condition gives

\[
 [R_k(v_a,v_b)]_{a,b=1}^m\longrightarrow I_m.
\]

Thus these positive semidefinite matrices are positive definite for all
sufficiently large \(k\). If \(g\) were affine, applying \(I-P\), evaluating
at the training inputs and pairing with \(y\) would give

\[
 0=\frac2m\sum_{k=0}^\infty c_k
       \sum_{a,b}y_a y_b R_k(v_a,v_b)>0.
\]

The strict inequality uses unbounded positive coefficient support and
\(y\ne0\); every summand is nonnegative. This contradiction proves the
claim. Boundedness of \(P\) on continuous functions and absolute uniform
convergence justify the projection and summation interchange.

## 2. Four predetermined inputs witness nonlinearity

Every non-affine function on the sphere is non-affine on some great circle.
Indeed, if it were affine on every great circle, its antipodal average would
be constant on each such circle and hence globally constant, since any two
points lie on a common great circle. Subtract that constant and extend the
remaining odd function homogeneously from the sphere to \(\mathbb R^d\).
Its restriction to every two-dimensional linear subspace would be linear.
Every pair of vectors lies in such a subspace, so the extension would be
additive and homogeneous, hence globally linear, a contradiction.

Choose a great circle on which \(g\) is not affine, three distinct points on
that circle, and a fourth where the affine interpolant through their
\(g\)-values fails. Every three distinct circle points are noncollinear.
Writing the fourth as an affine combination of the first three, subtracting
and normalizing gives coefficients \(c_i\) and points \(u_i\), \(1\le i\le4\),
such that

\[
 \sum_i|c_i|=1,\qquad \sum_i c_i=0,\qquad
 \sum_i c_i u_i=0,\qquad \delta:=\sum_i c_i g(u_i)>0.        \tag{4}
\]

Reverse the common coefficient sign if needed. These are deterministic
functions of the initial population covariance, training inputs and labels;
they use no realized initialization, trained weights or future trajectory.
The physical inputs are \(\sqrt d\,u_i\). Four is the minimum possible
number for an affine-annihilating witness with distinct sphere points,
because any three distinct sphere points are affinely independent.

For any function \(h\), the normalized witness yields

\[
 \inf_{a,b}\max_i|h(u_i)-a^\top u_i-b|
 \ge\left|\sum_i c_i h(u_i)\right|.                       \tag{5}
\]

We use a fixed deterministic choice of these points. The argument does not
claim that every arbitrary four-point panel works, or give a cheap procedure
for finding a numerically well-conditioned witness uniformly over problems.

## 3. A width-uniform first-order time remainder

This new input-nonlinearity result does not need a trained passive-query population
limit or a uniform complex-time disk. A direct real-variable bootstrap gives
the needed finite-width estimate. All constants in this paragraph are local
proof notation, independent of width; their explicit form is deliberately
conservative rather than an algorithmic prescription.

Choose a fixed \(B\ge8\) bounding all \(|\phi_\ell(0)|\) and real derivative
bounds. The initialization event

\[
 \|W^{(1)}(0)\|_{\rm op}/\sqrt n\le B,
 \qquad \max_{2\le\ell\le L}\|W^{(\ell)}(0)\|_{\rm op}\le B
\]

has probability tending to one for fixed \(d,L\). Put, only in this proof,

\[
 A=B+1,\quad H=(2A^2)^L,\quad D=A^{2L},\quad
 E=2Y^2DH^2,\quad T=\min\{1,(2YH\sqrt D)^{-1}\}.
\]

Bootstrap the scaled first operator and all other hidden operator norms
below \(A\). Forward induction bounds every feature RMS, uniformly over the
input sphere, by \(H\); backward induction bounds each backward-response
RMS by \(D\|w\|_2/\sqrt n\). Energy dissipation bounds residual RMS by \(Y\).
The exact flow therefore gives

\[
 \|w(t)\|_2/\sqrt n\le2YHt,
\]

\[
 \|W^{(1)}(t)-W^{(1)}(0)\|_{\rm op}/\sqrt n\le Et^2,
 \qquad
 \|W^{(\ell)}(t)-W^{(\ell)}(0)\|_{\rm op}\le Et^2.
\]

For example the hidden-matrix speed is at most
\(2YDH\|w\|_2/\sqrt n\), by Cauchy--Schwarz over the training examples;
the first-layer version replaces \(H\) by one. Integration gives the bounds.
Since \(ET^2\le1/2\), the bootstrap closes with a strict margin.
Lipschitz forward recursion then gives

\[
 \sup_x\frac{\|h^{(\ell)}(t,x)-h^{(\ell)}(0,x)\|_2}{\sqrt n}
 \le Jt^2,\qquad J=BEH\sum_{k=0}^{L-1}(BA)^k.
\]

Use the decomposition of each preactivation difference into the current
matrix times the previous feature difference plus the matrix increment times
the initial feature. The first-layer starting bound is \(BEt^2\).

Write \(g_n(x)=\dot f_n(0,x)\). The output and readout equations give
\(|f_n(t,x)|\le2YH^2t\) and

\[
 \|\dot w(t)-\dot w(0)\|_2/\sqrt n
 \le4YH^3t+2YJt^2.
\]

Integrating this inequality and multiplying by the initial features, while
bounding the moving-feature contribution separately, yields

\[
 \sup_{\|x\|=\sqrt d}|f_n(t,x)-t g_n(x)|\le Ct^2,
 \qquad C=2YH^4+\frac83YHJ T,\quad0\le t\le T.             \tag{6}
\]

All factors are explicit and independent of width. Gaussian matrix operator
bounds used here can be obtained directly from a fixed-radius sphere net:
each bilinear form for an \(n\times n\) matrix with entries \(N(0,1/n)\)
has Gaussian tails, and a sufficiently loose fixed bound (increase \(B\)
if using this elementary net proof) beats the two exponential net cardinalities.
For the first matrix with fixed \(d\), \(W^{(1)\top}W^{(1)}/n\to I_d\)
entrywise by the ordinary law of large numbers.

At the finitely many training and witness inputs, initial kernel convergence
follows by induction on layers. Conditional on the preceding layer, rows of
the next preactivation tuple are independent Gaussian vectors with the
empirical preceding Gram as covariance. Linear growth bounds their feature
products' conditional second moments on bounded covariance sets, so the
conditional variance of each empirical Gram entry is \(O(1/n)\). Its mean
is a continuous function of that finite covariance matrix, including singular
ones: couple Gaussians through their continuous positive square roots and use
the Lipschitz activation and Cauchy--Schwarz. Induction proves convergence of
all finitely many entries. Thus \(g_n(\sqrt d\,u_i)\to g(u_i)\) in probability.

Fix \(0<t\le\min\{T,\delta/(4C)\}\). Intersect the initialization
operator-norm event with the event that the witness applied to \(g_n\)
differs from \(\delta\) by at most \(\delta/4\). Equation (6) then gives

\[
 \sum_i c_i f_n(t,\sqrt d\,u_i)\ge\delta t/2.
\]

This event has probability tending to one. Applying (5) proves the dense
version of (1), at a fixed positive time, without interchanging width and
an uncontrolled time remainder.

## 4. Transfer and exact Taylor qualification

For any predictions \(f,g\) on a common query domain, distance to affine
functions is 1-Lipschitz in the supremum norm:

\[
 \left|\inf_{a,b}\|f-a^\top x-b\|_\infty
       -\inf_{a,b}\|g-a^\top x-b\|_\infty\right|
 \le\|f-g\|_\infty.
\]

Each compression error tends to zero in probability at its prescribed order.
At a fixed time its error on the four witnesses is eventually at most
\(\delta t/4\) with probability tending to one. This proves (1).
Equation (2) and actual hidden-feature movement follow from the repaired
compatible-data theorem and its compression-transfer argument in
`COMPRESSION_CONSEQUENCE.md`. Take the minimum of the finitely many positive
time thresholds and constants and a finite union bound over the methods.
The fixed-time feature-learning proof retains its explicitly documented
maintained-book local-population dependency; the new input-nonlinearity
proof above does not add another such dependency.

For Legendre and Harmonic no query-domain or storage change is needed. If
Taylor originally has \(p\) passive inputs, declare the witness inputs too:
\(p'\le p+4\). Replace \(p\) by \(p'\) in its existing storage formula,
and change nothing else. In particular,

\[
\begin{split}
 C(m+p+4)^2\bigg[&
 (Ym/\gamma)^4[\log(en)]^3\\
 &+(m/\gamma)^2[\log(en)]^2[\log(e+\log(en))]^2\bigg]
 +C(m+p+4)d
\end{split}
\]

is sufficient. Since \(m\ge2\), the quadratic panel factor increases by
at most nine and the data factor by at most three. The exponent of \(\log n\)
is still three. No passive label, dense rollout, or future information is added.
If the original panel already witnesses non-affinity, no augmentation is
required. An arbitrary unaugmented panel cannot be asserted to do so: on
affinely independent points every prediction vector has an affine interpolant.

## Check status

The input-kernel lemma was independently derived from the prompt-only
assignment in `INPUT_KERNEL_LEMMA.md`. A separate prompt-only derivation
supplied the four-point witness and verified the explicit real-time bootstrap.
Fresh scoped reports `AUDIT_INPUT_KERNEL.md` and `AUDIT_INPUT_TIME.md` check
the kernel/witness and real-time/transfer portions separately. These are not
promotion reviews of the inherited feature-learning dependency. Their
explicit sample-count qualification, event intersection and wording
clarifications are incorporated here; none changes the intended theorem or
its constants. The coordinator read both full reports and checked their
calculations against this proof.

## Paper-facing conclusion and boundaries

The clean paper statement is that the same compact trajectories are
simultaneously separated from (i) all input-affine predictors, including
deep linear feature-learning networks, and (ii) their dense reference's
frozen initial tangent-kernel trajectory, while approximating the nonlinear
dense dynamics with vanishing error. Every dense hidden layer moves at
a nonvanishing normalized scale. The two failures are different, so show
the two inequalities together rather than calling a moving kernel proof
of input nonlinearity.

The witness occurs at sufficiently early, fixed positive times. Neither
separation is asserted at the fitted endpoint; there is no test-risk ordering.
Constants may shrink with nearly parallel inputs, nearly affine activations,
or small nonzero labels. Width tends to infinity after time and all problem
parameters are fixed. The broader compression theorem remains unchanged.

The supplement `NONLINEAR_FEATURE_INCREMENT.md` further proves that the
nonlinear part of the dense first-layer feature increment is nonzero at
the same fixed-time, width-asymptotic scale. This does not identify the
compressed internal coordinates with dense features, prove that every later
layer's nonlinear component moves, or prove that the cubic output departure
from NTK itself has a non-affine input component. Those stronger statements
are not asserted.
