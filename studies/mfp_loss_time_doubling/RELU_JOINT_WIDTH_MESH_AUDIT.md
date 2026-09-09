# Joint width--mesh limits for normalized ReLU loss descent

## 0. Verdict

Consider the same one-input, two-hidden-layer network

\[
 H_j=\phi(u_j),\qquad
 z_i={1\over\sqrt n}\sum_{j=1}^nW_{ij}H_j,\qquad
 f_n={1\over n}\sum_{i=1}^na_i\phi(z_i),
 \tag{0.1}
\]

with iid standard-Gaussian initialization, normalized ReLU

\[
 \phi(x)=\sqrt2\,x_+,
\]

and one-sample half-square loss

\[
 \ell_n={1\over2}(1-f_n)^2.
\]

Writing \(r=1-f_n\), one Euler loss step is exactly

\[
 \begin{aligned}
 a^+&=a+h r\,\phi(z),\\
 W^+&=W+{h r\over\sqrt n}
       \{a\odot\phi'(z)\}\phi(u)^T,\\
 u^+&=u+h r\,\phi'(u)\odot
       {W^T\{a\odot\phi'(z)\}\over\sqrt n}.
 \end{aligned}                                                \tag{0.2}
\]

There is currently **no proved deterministic scaling**

\[
 h=h_n\downarrow0,\qquad n\to\infty,                         \tag{0.3}
\]

under which the actual hard-ReLU finite-width Euler paths in (0.2) are
known to converge to a canonical generalized mean-field gradient flow.
This is not just the absence of a rate.  Two logically prior statements
are open:

1. for each fixed nonzero \(h\) and fixed finite number of steps, the
   discontinuous, adaptively reused \(W/W^T\) program has not been
   identified with a hard-indicator OMFP DAG; and
2. the candidate hard-indicator population Euler states have not been
   shown to converge, as \(h\downarrow0\), to a unique restartable
   occupation-measure dynamics whose loss readout is unique.

Consequently conditions such as \(nh_n\to\infty\), although naturally
forced by one particular spatial boundary-layer estimate proved below,
are not sufficient theorems for (0.3).  They are not universal necessary
conditions either: an attracting gate can self-average in time even when
there are no fresh gates in a width-\(h_n\) spatial slab.

The rest of the note proves exactly what can be said about gate counts,
explains why a diagonal limit is strictly stronger than the available
fixed-program results, and separates two inequivalent regularizations.

## 1. Exact initialization boundary-layer law

Let \(\gamma(x)=(2\pi)^{-1/2}e^{-x^2/2}\), let \(b>0\), and let
\(h_n>0\) tend to zero.  Define the bottom- and top-gate slab counts

\[
 N_n^u(b)=\sum_{j=1}^n{\bf1}_{\{|u_j|\le b h_n\}},\qquad
 N_n^z(b)=\sum_{i=1}^n{\bf1}_{\{|z_i|\le b h_n\}}.       \tag{1.1}
\]

Put

\[
 c_b=2b\gamma(0)=b\sqrt{2\over\pi}.                     \tag{1.2}
\]

### Proposition 1.1

At initialization:

1. If \(nh_n\to\infty\), then
   \[
   {N_n^u(b)\over nh_n}\xrightarrow{\mathbb P}c_b,
   \qquad
   {N_n^z(b)\over nh_n}\xrightarrow{\mathbb P}c_b.     \tag{1.3}
   \]
2. If \(nh_n\to\lambda\in(0,\infty)\), each of
   \(N_n^u(b)\) and \(N_n^z(b)\), marginally, converges in law to a
   Poisson random variable of mean \(c_b\lambda\).  No joint-independence
   assertion is made.
3. If \(nh_n\to0\), then
   \[
   \mathbb P\{N_n^u(b)+N_n^z(b)>0\}\longrightarrow0.   \tag{1.4}
   \]

#### Proof

The bottom count is binomial with parameters \(n\) and

\[
 p_n^u=\mathbb P\{|G|\le bh_n\}
      =c_bh_n+o(h_n).                                   \tag{1.5}
\]

Thus

\[
 \operatorname{Var}\!\left({N_n^u(b)\over nh_n}\right)
 \le {p_n^u\over nh_n^2}=O((nh_n)^{-1}),                \tag{1.6}
\]

which proves the first bottom assertion.  The usual binomial generating
function

\[
 \mathbb E s^{N_n^u}=(1-p_n^u+p_n^us)^n                 \tag{1.7}
\]

proves the Poisson assertion when \(np_n^u\to c_b\lambda\), and the
union bound \(\mathbb P(N_n^u>0)\le np_n^u\) proves the zero-count
assertion.

For the top count condition on \(u=(u_1,\ldots,u_n)\).  Set

\[
 Q_n={1\over n}\sum_{j=1}^n\phi(u_j)^2.                 \tag{1.8}
\]

Normalization gives \(\mathbb E\phi(G)^2=1\), so the strong law gives
\(Q_n\to1\) almost surely.  Conditional on \(u\), the independent rows
of \(W\) give iid

\[
 z_i\mid u\sim N(0,Q_n).                                \tag{1.9}
\]

Therefore \(N_n^z(b)\mid u\) is binomial with success probability

\[
 p_n^z(u)=2\Phi\!\left({bh_n\over\sqrt{Q_n}}\right)-1,
 \qquad
 {p_n^z(u)\over h_n}\longrightarrow c_b                \tag{1.10}
\]

almost surely.  On \(Q_n\in[1/2,2]\), the ratio in (1.10) is uniformly
bounded.  Conditional Chebyshev, followed by dominated convergence, proves
(1.3).  Conditional use of (1.7), again followed by dominated convergence,
proves the Poisson limit.  Finally, on \(Q_n\in[1/2,2]\),
\(p_n^z\le C_bh_n\); hence

\[
 \mathbb P(N_n^z>0)
 \le \mathbb P\{Q_n\notin[1/2,2]\}+C_bnh_n\to0.        \tag{1.11}
\]

Combining the two layers proves (1.4). \(\square\)

### What Proposition 1.1 does and does not imply

If a collection of gates has a deterministic one-step displacement bound
\(|z_i^+-z_i|\le bh_n\), every gate in that collection which changes sign
belongs to the slab counted by \(N_n^z(b)\).  Thus (1.3) is the exact
spatial self-averaging threshold for a bounded-speed initialization slice.
The actual speeds in (0.2) are unbounded and depend on the reused matrix;
one needs a truncation estimate uniform over the adaptive history before
this observation becomes a crossing theorem.

In particular, Proposition 1.1 does **not** prove that \(nh_n\to\infty\)
is necessary for path convergence.  It proves only that it is necessary
for relative consistency of this particular width-\(h_n\) empirical
density estimator.

## 2. A benchmark uniform-in-time count and the missing dependence theorem

Suppose, only for this paragraph, that at each of
\(m_n=\lceil T/h_n\rceil\) times one had a conditional binomial slab count
of mean comparable to \(nh_n\), with a Bernstein bound

\[
 \mathbb P\{|N_{n,k}-\mathbb E_kN_{n,k}|>epsilon nh_n
             \mid\mathcal F_k\}
 \le2e^{-c\epsilon^2nh_n}.                              \tag{2.1}
\]

No independence between different times is needed for a union bound, which
would give

\[
 \mathbb P\left\{
 \max_{k<m_n}|N_{n,k}-\mathbb E_kN_{n,k}|>epsilon nh_n
 \right\}
 \le {2(T+h_n)\over h_n}e^{-c\epsilon^2nh_n}.           \tag{2.2}
\]

Hence the benchmark condition

\[
 {nh_n\over\log(1/h_n)}\longrightarrow\infty           \tag{2.3}
\]

would make all spatial slab counts self-average simultaneously.

Equation (2.2) is a rigorous implication of (2.1), but (2.1) is **not**
proved for (0.2).  At later times each queried row and column depends on all
earlier actions of the same \(W\) and \(W^T\).  Gaussian conditioning leaves
regression responses on the adaptive query span, and that span grows like
\(T/h_n\).  Hard gates can also create singular history Grams and exactly
inactive coordinates.  Thus there is no conditional iid row law to which
(2.1) may simply be applied.

## 3. Regular crossings and attracting crossings have different counts

For a regular transverse gate with speed of order one, a single step can
cross only from an \(O(h_n)\) slab.  The spatial count is therefore
\(O_{\mathbb P}(nh_n)\) per time slice and, over \(T/h_n\) slices, the raw
regular-crossing count is heuristically \(O(nT)\).  Turning this heuristic
into a theorem requires a dynamic coarea/small-ball bound for all adaptive
queries, which is one of the open hard-indicator bridges.

An attracting gate is different.  Freeze its negative- and positive-side
normal velocities at

\[
 p>0>q.                                                   \tag{3.1}
\]

Hard-ReLU Euler is then

\[
 z_{k+1}=z_k+h_n\{p+(q-p)I_k\},
 \qquad I_k={\bf1}_{\{z_k>0\}}.                         \tag{3.2}
\]

Inside the invariant strip \(h_nq<z<h_np\), put

\[
 \lambda={p\over p-q},\qquad
 x_k={z_k/h_n-q\over p-q}.                              \tag{3.3}
\]

Then, apart from the immaterial endpoint convention,

\[
 x_{k+1}=\{x_k+\lambda\},\qquad
 I_k=x_k+\lambda-x_{k+1}.                               \tag{3.4}
\]

Consequently, for every \(N\ge1\),

\[
 \left|\sum_{k=0}^{N-1}I_k-N\lambda\right|<1.          \tag{3.5}
\]

Thus one already-hit gate contributes on the order of \(T/h_n\) binary
gate-side samples, but its time occupation converges with error at most
\(h_n/T\), independently of \(n\).  If a positive fraction of the \(n\)
gates enters such sliding strips, the raw number of gate-side samples can
be \(O(nT/h_n)\), not \(O(nT)\).
This proves why a single rule based on \(nh_n\) cannot resolve both regular
and attracting gates.

For fixed \(\lambda\in(0,1)\), the number of actual sign switches is also
\(\Theta(T/h_n)\).  If \(\lambda\le1/2\), every symbol \(I_k=1\) is
isolated and contributes two transitions, up to endpoint errors; if
\(\lambda\ge1/2\), apply the same argument to the isolated symbols
\(I_k=0\).

The hard-Euler Young measure at the frozen attracting gate is

\[
 \nu_{p,q}=(1-\lambda)\delta_0+\lambda\delta_1.          \tag{3.6}
\]

For every integer \(r\ge1\),

\[
 \int s^r\,d\nu_{p,q}(s)=\lambda.                       \tag{3.7}
\]

This full moment statement matters: the tangent kernel contains squares of
gate-dependent cotangents.  Replacing the oscillatory gate by its mean
\(\lambda\) changes the second moment from \(\lambda\) to \(\lambda^2\).

## 4. Why no diagonal \(h_n\) follows from fixed-program convergence

Let \(N_n=\lceil T/h_n\rceil\).  A joint limit requires a growing-program
estimate, schematically

\[
 \max_{k\le N_n}d\bigl(X_{n,h_n}^k,X_{h_n}^k\bigr)
 \xrightarrow{\mathbb P}0,                             \tag{4.1}
\]

where \(X_{h}^k\) is the population hard-indicator Euler state, followed by
a population mesh theorem

\[
 X_h\longrightarrow X\quad\hbox{on }[0,T].             \tag{4.2}
\]

Pointwise convergence for each fixed program length does not imply (4.1)
for any prescribed \(N_n\to\infty\): its constants can grow arbitrarily
fast with the adaptive query-span dimension.  For hard ReLU the situation
is stricter still, because even the fixed-program statement needed to
define \(X_h^k\) is open.

The smooth growing-mesh audit elsewhere in this study obtains the
*conditional* candidate

\[
 N_n\asymp\left({\log n\over\log\log n}\right)^{1/3}    \tag{4.3}
\]

only after assuming quantitative robust rank and no amplification of weak
adaptive innovations.  Those hypotheses are not proved there, and hard
ReLU adds discontinuous gates and inactive atoms, so (4.3) cannot be quoted
as a result for (0.2).

There is also no classical finite-width flow to use as an intermediate
object.  The explicit width-two construction in `RELU_COMPACT_TIME_AUDIT.md`
shows that, for every fixed convention for \(\phi'(0)\), an open,
positive-Gaussian-probability set of initial parameters reaches an
attracting gate at which the classical ODE cannot be continued.  This does
not disprove an Euler/Filippov limit; (3.5) shows precisely how Euler can
pass to an occupation limit when the classical ODE cannot.

## 5. Softplus is a different, well-defined regularization

Define the RMS-normalized softplus

\[
 s_\tau(x)=\tau\log(1+e^{x/\tau}),\qquad
 \phi_\tau(x)={s_\tau(x)\over\|s_\tau(G)\|_2},
 \qquad \tau>0.                                         \tag{5.1}
\]

Then \(\phi_\tau\in C^\infty\), has at most linear growth, and for every
fixed \(r\ge1\),

\[
 \|s_\tau'\|_\infty\le1,\qquad
 \|s_\tau''\|_\infty\le{1\over4\tau},\qquad
 \|s_\tau^{(r)}\|_\infty\le C_r\tau^{1-r}.            \tag{5.2}
\]

Moreover \(\|s_\tau(G)\|_2\to\|G_+\|_2=2^{-1/2}\), so
the normalization factors remain bounded above and below for all small
\(\tau\).  Therefore, for each fixed \(\tau>0\), fixed nonzero mesh, and
fixed finite number of steps, the smooth fixed-program width theorem in
this study applies.  At each fixed finite width, the smooth loss vector
field also has a unique classical solution up to the exit time from every
bounded parameter set, and ordinary Euler convergence holds on compact
intervals on which that solution remains in such a set.

These two true statements still do not give a simultaneous
\((n,h,\tau)\)-limit.  The constants in (5.2) diverge as \(\tau\downarrow0\),
the number of reused queries diverges as \(h\downarrow0\), and the nonlinear
population compact-time tail theorem has not been proved for this dense
two-layer connector.  The natural resolution conditions

\[
 h_n/\tau_n\to0,\qquad n\tau_n\to\infty                \tag{5.3}
\]

say only that Euler resolves the transition layer locally and that the
layer contains many particles spatially.  Without uniform stability,
response, and tail estimates, (5.3) is not a sufficient theorem.  A naive
global Euler estimate can contain \(\exp(C T/\tau_n)\), so even
\(h_n=o(\tau_n)\) need not control that estimate.

### Soft smoothing and hard Euler make different local selections

This can be seen exactly in the abstract frozen normal form.  Smooth (3.2)
by replacing the binary gate fraction \(I\) with
\(J_\tau=\sigma(z/\tau)\), where
\(\sigma(x)=(1+e^{-x})^{-1}\):

\[
 \dot z=p+(q-p)\sigma(z/\tau).                          \tag{5.4}
\]

Its unique attracting equilibrium satisfies

\[
 \sigma(z_\tau^*/\tau)=\lambda={p\over p-q},\qquad
 z_\tau^*=\tau\log{\lambda\over1-\lambda}.             \tag{5.5}
\]

Hence soft smoothing selects the deterministic *gate fraction* \(\lambda\)
and its square is \(\lambda^2\).  Hard Euler selects the binary Young
measure (3.6), whose first moment is also \(\lambda\) but whose second
moment is \(\lambda\).  Since \(0<\lambda<1\),

\[
 \lambda-\lambda^2=\lambda(1-\lambda)>0.                \tag{5.6}
\]

For the RMS-normalized softplus the actual derivative is
\(\phi_\tau'=a_\tau J_\tau\), with
\(a_\tau=\|s_\tau(G)\|_2^{-1}\to\sqrt2\).  Thus the corresponding
discrepancy of squared slopes is
\(a_\tau^2\lambda(1-\lambda)\to2\lambda(1-\lambda)\), not merely
\(\lambda(1-\lambda)\).

In the full softplus network the background velocities corresponding to
\(p,q\) also depend on \(\tau\), so this frozen calculation is
asymptotically exact only when those backgrounds converge to their hard
values.  It nevertheless proves the local selection mismatch.  Softplus
is a viable regularized model, but it cannot be used as a proof of the
hard-Euler limit unless one proves that the actual network readout depends
only on first gate moments.  It does not: squared cotangents in the tangent
kernel see the squared-slope discrepancy above.

## 6. Exact open bridge and viable next formulations

A theorem for a canonical hard-ReLU joint limit would have to establish,
uniformly for \(k\le T/h_n\):

1. adaptive hard-indicator Gaussian conditioning with the true reused
   \(W/W^T\) responses;
2. dynamic small-ball/coarea estimates and concentration for all regular
   gate crossings;
3. tightness of the learned rank-one connector and every raw squared
   cotangent needed by the loss kernel;
4. convergence of multigate occupations to a joint Young measure, not just
   convergence of scalar gate means;
5. uniqueness and restartability of the resulting occupation-augmented
   OMFP dynamics; and
6. a quantitative growing-program error that permits an explicit choice of
   \(h_n\).

None of these may be replaced by Proposition 1.1 or positive homogeneity.
Homogeneity supplies the conditional compact-time norm estimates in
`RELU_COMPACT_TIME_AUDIT.md`; it does not determine the occupation state or
control the discontinuous reused adjoint.

There are therefore two honest viable programs:

- **Hard Euler program.**  Take (3.6)--(3.7), together with the joint
  correlations of simultaneous gates, as new state variables and prove
  items 1--6.  This is the regularization that can identify the actual
  explicit-Euler limit.
- **Smooth program.**  Fix \(\tau>0\), first prove the missing uniform
  population tail/stability theorem for \(\phi_\tau\), remove the mesh,
  and only afterwards study \(\tau\downarrow0\).  Its local selection is
  (5.5), generally different from hard Euler at second order.

Until one of these programs is closed, the endpoint loss mesh convergence
and every proposed explicit joint scaling \(h_n\) remain open for the actual
normalized-ReLU dense network (0.1)--(0.2).
