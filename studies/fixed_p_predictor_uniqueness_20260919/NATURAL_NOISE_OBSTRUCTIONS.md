# What vanishing noise can and cannot select

2026-09-19. Frozen author derivation for the scoped natural-noise route.
Scientific inputs: only `MODEL_AND_GEOMETRY.md` and `CANONICAL_FEATURES.md`
in this study, plus the self-contained arguments below. No experiments,
external scientific sources, maintained-code changes, or Git-index changes.
Status: mathematical candidate, not independently reviewed or promoted.

Isolation metadata: after deriving and reporting the principal axis-noise
construction and scalar regularization obstruction to the supervisor, a
metadata-only concurrency query unexpectedly returned completed-agent
summaries outside the assigned scope. Those summaries were not used, followed,
or incorporated. This route is therefore **not fully isolated**. This note
records exposure only; the derivations below use the two assigned inputs.
The original report was frozen before any comparison with the parallel routes,
with SHA-256
`81a92c1dd43c3e5b48ddf71e7dbcbe745bc1617d49531f967f925e7ff1751bfe`.
The separately headed bounded-random-ODE corollary in Section 1.3 was added
after the informed penalty-route check, at the supervisor's explicit request.
It uses only the invariant decomposition already proved in the original
frozen report; the original Brownian argument is retained.

## Contract and conclusion

The object is the exact order-one Gaussian population model, its physical
Hilbert metric, and its canonical initialization. A noise-independent limit
means that, for a fixed dataset and fixed positive noise amplitude, the
limiting predictor is almost surely a deterministic function, independent of
the realized Brownian path. This is stronger than a deterministic limit after
subsequently sending the noise amplitude to zero. Exponential fitting means
the original, unpenalized training loss tends to zero at an exponential rate
in physical time. Constants may depend on the fixed dataset.

There is an exact obstruction even from canonical initialization: a bounded,
arbitrarily small, finite-rank readout noise can vanish after time one, leave
the full original physical gradient-flow training trajectory unchanged, and
leave a nondegenerate Gaussian value at an unseen input. The training loss
nevertheless decays exponentially, and the entire state converges. This
refutes selection guarantees based solely on smallness and eventual
vanishing of genuine noise. It does not rule out a carefully specified noise
and drift that actively select one predictor, or prove any failure of the
unperturbed canonical flow.

The remaining exact conclusions are narrower: a positive random clock
inherits the original flow's endpoint; interpolation has neutral directions;
ordinary SGD supplies no noise at exact interpolation; hidden anchoring alone
does not remove readout ambiguity; and isotropic vanishing weight decay has
a precise selection-versus-exponential-fitting obstruction already in a
two-coordinate linear problem. Projected decay avoids that last obstruction
for fixed hidden features, but this is an explicitly changed optimizer.

## 1. Exact canonical-start additive-noise counterexample

Use one training example

\[
x_1=\sqrt2 e_1,\qquad y_1=1,\qquad \mu_1=1,
\]

and inspect the unseen direction \(x_*=\sqrt2 e_2\). This is a finite
compatible dataset in the assigned model. Write the independent upper marks
as \(Z_i=\tanh\xi_i\). They are centered, have positive density on
\((-1,1)\), and \(E Z_i^2=\tau>0\).

### 1.1 A noise direction invisible to the full training gradient

The assigned canonical-feature calculation gives

\[
H_0(e_1)=\tanh(\kappa_0 Z_1),\qquad
H_0(e_2)=\tanh(\kappa_0 Z_2),\qquad
\kappa_0=F(1)>0.
\]

Here and below the argument of \(H\) denotes a normalized direction;
the physical input is \(\sqrt2\) times that direction. Define

\[
b=\frac{E[Z_2\tanh(\kappa_0 Z_2)]}{\tau},\qquad
q(Z_2)=\tanh(\kappa_0 Z_2)-bZ_2.                 \tag{1}
\]

Then \(q\) is bounded and odd, and

\[
E q=0,\qquad E[qZ_2]=0,\qquad
E[q\tanh(\kappa_0Z_2)]=\|q\|_2^2>0.            \tag{2}
\]

For strict positivity, if \(q=0\) in \(L^2\), the positive density and
continuity imply \(\tanh(\kappa_0 z)=bz\) on \((-1,1)\). The third
derivative at zero of the left side is \(-2\kappa_0^3\ne0\), while that
of the right side is zero. This contradiction proves \(q\ne0\).

It remains to show that this direction is invisible to the *moving* hidden
gradient, not merely to the initialized training feature. The block
structure derived in `CANONICAL_FEATURES.md` makes this exact.

After only a permutation of the lower dictionary coordinates, write

\[
b_1=(b_{10},\,\beta_1(g_1,\zeta_1),\,
                    \beta_2(g_2,\zeta_2)),\qquad
b_2=(b_{20},\,dZ_1,\,dZ_2),\quad
d=(\tau+\eta)^{-1/2}.                            \tag{3}
\]

Each \(\beta_i\in\mathbb R^2\) is bounded, centered and odd under
\((g_i,\zeta_i)\mapsto(-g_i,-\zeta_i)\). The two lower coordinate
pairs are independent. The lower covariance plus ridge has no entries
between the constant, pair-one and pair-two groups. Its Cholesky factor
therefore has the same separation even in the original interleaved order.
The raw contraction matrix likewise has only a \(Z_1\)-to-pair-one block
and a \(Z_2\)-to-pair-two block. Hence the canonical \(D\) has precisely
that block structure. The permutation preserves the physical Euclidean and
Frobenius metrics.

Consider the following family of states:

- \(w=(W(g_1,\zeta_1),g_2)\), with \(W\) odd in its two arguments;
- the middle matrix has only the two coordinate blocks just described;
  its second block is fixed at its canonical value;
- the readout is \(c=C(Z_1)+Xq(Z_2)\), with \(C\) odd and \(X\in\mathbb R\).

All canonical initial parameters belong to this family, with \(W=g_1\),
\(C=0\), and \(X=0\). For the training direction, the lower feature is
supported only on pair one; consequently

\[
H_h(e_1)=\tanh(\kappa(h)Z_1)                     \tag{4}
\]

for a real scalar \(\kappa(h)\), initially \(\kappa_0\). The exact upper
hidden adjoint is

\[
U=E_2[c\operatorname{sech}^2(\kappa Z_1)b_2].    \tag{5}
\]

Its constant component is zero: the \(C\)-term is odd in \(Z_1\), and
the \(q\)-term has zero mean. Its \(Z_2\)-component is zero, using
\(E Z_2=0\) for the \(C\)-term and \(E[qZ_2]=0\) for the noise term.
Its \(Z_1\)-component receives no noise contribution, using \(E q=0\).
Thus \(U\) has only its first-coordinate component and is completely
independent of \(X\).

To check invariance in the original physical metric, put
\(r=1-f(e_1)\), and let
\(a=E_1[b_1\tanh(w\cdot e_1)]\). The unhalved square loss gives

\[
\dot M=2rUa^T,\qquad
\dot w=2r\operatorname{sech}^2(w\cdot e_1)
              (b_1^TM^TU)e_1,\qquad
\dot c=2rH_h(e_1).                               \tag{6}
\]

These are the actual coupled forward and transpose interactions. Formula
(5) shows that \(\dot M\) changes only its first coordinate block, while
\(\dot w\) changes only \(W\). Its increment is an odd function of
\((g_1,\zeta_1)\), since \(\beta_1\) is odd and
\(\operatorname{sech}^2 W\) is even. The readout increment is odd in
\(Z_1\). The asserted family is therefore invariant, including under any
added readout increment in the direction \(q\). In particular the hidden
and \(C\) dynamics are exactly independent of \(X\).

### 1.2 Exponential fitting and global convergence of the unchanged base flow

For completeness, exponential fitting in this example does not rely on a
missing universal canonical-flow theorem. Within the invariant family set

\[
K(\kappa)=E\tanh^2(\kappa Z_1),\qquad
\rho=E[C(Z_1)Z_1\operatorname{sech}^2(\kappa Z_1)].
\]

The scalar \(\kappa\) is the coefficient of \(Z_1\) in (4); its gradient
below uses precisely the original physical hidden norm. The full hidden
gradient of the training prediction is \(\rho\nabla_h\kappa\), since
all other upper components in (5) vanish. Consequently (6) gives

\[
\begin{split}
\dot C(z)&=2r\tanh(\kappa z),\\
\dot\kappa&=2r\rho\|\nabla_h\kappa\|^2,\\
\dot r&=-2r\bigl(K(\kappa)+
                       \rho^2\|\nabla_h\kappa\|^2\bigr).
\end{split}                                      \tag{7}
\]

On every local solution the last equation and \(r(0)=1\) imply
\(r(t)>0\). Starting with \(\kappa_0>0\), the first equation implies
\(C_t(z)z\ge0\) as long as \(\kappa>0\). Thus \(\rho\ge0\), so the
second equation makes \(\kappa\) nondecreasing and prevents it from
leaving this positive region. With

\[
k_0=E\tanh^2(\kappa_0Z_1)>0,
\]

we obtain for all times of existence

\[
0<r(t)\le e^{-2k_0t},\qquad
L(t)=r(t)^2\le e^{-4k_0t},\qquad
\|C_t\|_\infty\le2\int_0^t r(s)\,ds\le k_0^{-1}.       \tag{8}
\]

These bounds also give global existence and convergence. Indeed (5), after
the exact cancellation of \(Xq\), gives
\(\|U\|\le B_2/k_0\). Since \(\|a\|\le B_1\),

\[
\|\dot M\|_F\le\frac{2B_1B_2}{k_0}e^{-2k_0t}.
\]

Thus \(M\) is uniformly bounded and has an exponentially small tail.
The second equation in (6) now gives an analogous integrable exponential
bound on \(\|\dot w\|_2\); the first equation in (7) gives one on
\(\|\dot C\|_\infty\). The locally Lipschitz physical vector field
therefore extends for every finite time, and \((h,C)\) converges in its
physical norm at rate \(e^{-2k_0t}\). Local Lipschitzness follows directly
from bounded dictionary fields and the bounded first two tanh derivatives,
as in the assigned model estimates, on any set with bounded \(M,C\).
The global bounds just obtained preclude any finite-time escape from such
sets. No uniform-in-dataset rate is asserted.

### 1.3 Genuine noise and a random limiting predictor

Let \(B_t\) be one real Brownian motion, independent of the fixed population
marks. For any \(\varepsilon>0\) keep the hidden physical gradient flow
unchanged and set

\[
dc=-\nabla_cL(h,c)\,dt
       +\varepsilon(1-t)_+q\,dB_t,\qquad
dh=-\nabla_hL(h,c)\,dt.                         \tag{9}
\]

This is a finite-rank, Hilbert-space-valued stochastic perturbation; there
is no cylindrical-noise or infinite-trace assumption. The initial state is
exactly canonical. Equations (5)--(7) give the explicit decomposition

\[
c_t=C_t(Z_1)+X_tq(Z_2),\qquad
X_t=\varepsilon\int_0^{t\wedge1}(1-s)\,dB_s.      \tag{10}
\]

For \(t\ge1\), \(X_t=X_1\) exactly. Its law is centered Gaussian with
variance \(\varepsilon^2/3\). The elementary deterministic-integrand
Itô-integral fact used here follows by approximating \(1-s\) with step
functions: each integral is a linear combination of independent Gaussian
increments, with variance the corresponding sum of squared integrands
times interval lengths; the \(L^2\) limit has variance
\(\int_0^1(1-s)^2ds=1/3\) and the limiting Gaussian characteristic
function. Nothing is being inferred from an infinite-time martingale limit.

The training loss is exactly the deterministic loss in (8). Both hidden
blocks and the nonlinear training gates evolve according to the original
physical gradient flow; they have not been frozen or replaced. The noise
vanishes continuously and completely at time one. Its amplitude can be
arbitrarily small, and the full state converges thereafter.

For the query \(e_2\), \(w\cdot e_2=g_2\) is unchanged, its lower
feature lies only in pair two, and the second middle block is unchanged.
Therefore

\[
H_{h_t}(e_2)=\tanh(\kappa_0Z_2),\qquad
f_t(e_2)=X_t\|q\|_2^2.                         \tag{11}
\]

The \(C_t\) term contributes zero by independence and centered oddness.
Combining (10)--(11) proves

\[
\operatorname{Var}[f_\infty(e_2)]
       =\frac{\varepsilon^2}{3}\|q\|_2^4>0.     \tag{12}
\]

Thus the limiting predictor is not noise-independent, despite exponential
zero training loss and physical-state convergence. In fact the full
predictor converges uniformly over the normalized circle: the state tails
are exponential, tanh is Lipschitz, and \(M,c\) are bounded along each
realization, which bounds the feature-to-predictor map uniformly in the
unit input direction.

Even requiring noise to vanish whenever the residual is zero is insufficient
by itself: replace the coefficient in (9) by
\(\varepsilon r(t)(1-t)_+\). The same cancellation leaves \(r\) deterministic
and strictly positive on \([0,1]\); the terminal Gaussian variance becomes
\(\varepsilon^2\int_0^1r(s)^2(1-s)^2ds>0\). This modification is still not
ordinary SGD noise, whose range has additional restrictions discussed below.

#### Bounded random-ODE corollary

The same obstruction holds with a uniformly bounded random velocity
perturbation, without any Brownian differential. Let \(\xi\) take values
\(+1\) and \(-1\) with equal probability, independently of the fixed
population marks, and replace (9) by

\[
\dot c=-\nabla_cL(h,c)+\varepsilon\xi(1-t)_+q,
\qquad \dot h=-\nabla_hL(h,c).
\]

The perturbation is continuous in time, vanishes at time one, and has
physical norm at most \(\varepsilon\|q\|_2\). The same exact adjoint
cancellation gives the unchanged deterministic \((h_t,C_t,r(t))\) from
Section 1.2 and

\[
X_t=\varepsilon\xi\int_0^{t\wedge1}(1-s)ds,
\qquad X_\infty=\frac{\varepsilon\xi}{2},\qquad
\operatorname{Var}[f_\infty(e_2)]
       =\frac{\varepsilon^2}{4}\|q\|_2^4>0.       \tag{12a}
\]

Thus a uniformly bounded random-ODE forcing also retains a random predictor
while the full state converges and the training loss satisfies (8).
For a residual-vanishing version use
\(\varepsilon\xi r(t)(1-t)_+q\) instead. Its norm has the same bound,
since \(0<r(t)\le1\), while

\[
X_\infty=\varepsilon\xi
              \int_0^1r(s)(1-s)ds,\qquad
\operatorname{Var}[f_\infty(e_2)]
 =\varepsilon^2\|q\|_2^4
       \left(\int_0^1r(s)(1-s)ds\right)^2>0.      \tag{12b}
\]

Strict positivity follows from the continuous, deterministic, strictly
positive residual on \([0,1]\). This corollary concerns perturbations of
the original loss flow; it does not assert tangency to any additional
selection objective or invalidate a theorem imposing that different
condition.

**Exact scope.** This is a counterexample to an inference from vanishing or
residual-vanishing noise to deterministic selection, and to any proposed
guarantee covering perturbations of the form (9). It is not a no-go theorem
for every designed stochastic optimizer. The noise is a permitted common
Brownian forcing in one bounded readout-field direction, not a claim about
independent Brownian forcing of every particle. No positive-loss trap,
alternative noiseless trajectory, or failure of uniqueness of the
deterministic initial-value problem is asserted.

## 2. What the interpolation geometry actually says

Let \(S=(h,c)\), \(G(S)=A_hc-Y\), and \(L=|G|^2\). At an interpolant
\(S_*\), differentiability of \(G\) and local Lipschitzness of its derivative
give the exact linearization

\[
D(\nabla L)(S_*)=2DG(S_*)^*DG(S_*).             \tag{13}
\]

Indeed \(\nabla L=2DG^*G\), \(G(S_*+v)=DG(S_*)v+o(\|v\|)\), and
\(DG(S_*+v)=DG(S_*)+O(\|v\|)\). Substitution proves (13) without
assuming a globally twice differentiable \(L^2\) Nemytskii map.

Every \((0,q)\) with \(q\in\ker A_{h_*}\) lies in the kernel of (13).
The assigned feature theorem supplies such directions visible at any new
query for the initialized hidden representation. Thus a loss estimate alone
cannot provide a contracting estimate for all predictor directions. This
statement describes the loss Hessian; it does not say that every tangent
direction remains exactly decoupled along an arbitrary nonlinear flow.
Section 1 supplies a specific exact decoupling where this stronger fact holds.

The elementary normal/tangent model is

\[
dr=-2(r-1)dt,\qquad dz=\sigma(t)dB_t,
\quad L=(r-1)^2,\quad (r_0,z_0)=(0,0).          \tag{14}
\]

For any nonzero \(\sigma\) supported in \([0,1]\),
\(L=e^{-4t}\) while \(z_\infty=\int_0^1\sigma,dB\) is nondegenerate.
This is an exact fixed-feature example, not by itself a proof about the
full physical model. Its geometric mechanism is precisely realized by
(9)--(12).

If a normal coordinate is also forced, even its rate requires a noise-tail
condition. For example
\(du=-2u,dt+\sigma(t)dB_t\) has

\[
E u(t)^2=e^{-4t}u(0)^2+
                \int_0^t e^{-4(t-s)}\sigma(s)^2ds.       \tag{15}
\]

This follows by the integrating factor and the same step-function
variance calculation. Taking \(\sigma(s)=(1+s)^{-1}\), the integral over
\([t-1,t]\) alone is at least
\((1-e^{-4})/[4(1+t)^2]\) for \(t\ge1\). Hence vanishing noise alone
does not even imply exponential loss in expectation in the stable normal
direction. Section 1 avoids this separate issue and therefore isolates the
selection obstruction.

## 3. Random clocks retain the original endpoint question

Let \(V=-\nabla L\), and let \(S^0(s)\) be the original deterministic
solution for its actual interval of existence. For a positive, locally
integrable random speed \(a(t,\omega)\), define

\[
\tau(t,\omega)=\int_0^t a(s,\omega)ds,
\qquad \dot S=a(t,\omega)V(S).
\]

The chain rule and initial-value uniqueness give
\(S(t,\omega)=S^0(\tau(t,\omega))\), wherever defined. If
\(\tau\to\infty\) and the original predictor has a limit, every clock
has that same limit. If the original solution satisfies
\(L(S^0(s))\le C e^{-\lambda s}\) and
\(\tau(t)\ge at-b\) for constants \(a>0,b\), then
\(L(S(t))\le C e^{\lambda b}e^{-\lambda at}\).

These are conditional inheritance statements. They provide neither a new
endpoint selector nor a proof that the original canonical solution fits
every dataset. If the accumulated clock time is finite, even an existing
infinite-time limit is generally not reached.

A Brownian Itô term parallel to \(V\) is not automatically this random
clock: Itô's formula for \(S^0(\tau)\) adds a drift involving
\(DV\,V\). A Stratonovich flow interpretation also needs an admissible
clock and existence at all clock values visited. One must specify which
construction is intended before importing deterministic trajectories.

## 4. Ordinary SGD cannot be credited with unspecified tangential selection

For per-example square losses
\(\ell_i(S)=(f_S(x_i)-y_i)^2\),

\[
\nabla\ell_i(S)=2(f_S(x_i)-y_i)\nabla f_S(x_i).
\]

At exact interpolation, every individual gradient is zero. Therefore every
ordinary minibatch gradient is zero and its sampling covariance is zero.
The full manifold of interpolants remains absorbing for this noise
mechanism. This alone is not a counterexample from canonical initialization,
but it prevents an argument that SGD noise continues mixing among exact
interpolants until only one remains.

At a differentiable interpolant the first-order sample-gradient expansion is

\[
\nabla\ell_i(S_*+v)
 =2\bigl(Df_i(S_*)v\bigr)\nabla f_i(S_*)+o(\|v\|).       \tag{16}
\]

It lies, to first order, in the span of the sample gradients
\(\nabla f_i(S_*)\). A tangent vector satisfying \(Df_i(S_*)v=0\)
for all \(i\) receives no first-order restoring contribution from these
sample gradients. Higher-order geometry and the training path may still
produce an implicit bias; (16) does not rule that out.

For fixed hidden features every minibatch readout update lies in
\(\operatorname{ran}A^*\). Hence \(Pc\), with \(P\) the projection
onto \(\ker A\), is exactly invariant, regardless of sample order or
step sizes. From canonical \(c=0\), this invariance is compatible with a
unique minimum-norm fitted readout if SGD converges. From differing tangent
initializations it preserves their differences. Neither statement transfers
without proof to moving features, where the kernel itself changes.

In the one-example construction of Section 1, ordinary minibatch sampling
has no randomness at all. The rank-one forcing there is a genuine additional
noise, and must not be renamed SGD noise.

## 5. Isotropic decay: exact fitting versus erasure of tangent memory

### 5.1 Constant weight decay has a nonzero residual

For fixed hidden features with \(K=AA^*>0\), consider

\[
\dot c=-2A^*(Ac-Y)-\lambda c,\qquad\lambda>0.
\]

The unique stationary point is

\[
c_\lambda=A^*(K+\lambda I/2)^{-1}Y,
\qquad
Ac_\lambda-Y=-\frac\lambda2(K+\lambda I/2)^{-1}Y.       \tag{17}
\]

Multiplication by \(2A^*A+\lambda I\) verifies the first identity, and
\(K(K+\lambda I/2)^{-1}-I\) gives the second. For \(Y\ne0\) the
residual is nonzero. Strict positive decay removes the readout nullspace,
but generally biases the original labels.

### 5.2 Vanishing isotropic decay cannot combine universal erasure with an exponential loss tail

The smallest exact model already proves a schedule-independent obstruction.
Let the training prediction be \(r\), an unseen prediction be \(z\), and

\[
L=(r-1)^2,\qquad
\dot r=2(1-r)-\lambda(t)r,\qquad
\dot z=-\lambda(t)z,\qquad r(0)=0,             \tag{18}
\]

where \(\lambda\ge0\) is any locally integrable function. The same
equations describe the time after a compactly supported noise has deposited
a nonzero random \(z\). The interval \([0,1]\) is invariant for \(r\),
as can also be checked by the explicit integrating-factor solution.
For any time \(T\),

\[
z(t)=z(T)\exp\left(-\int_T^t\lambda(s)ds\right).       \tag{19}
\]

Erasing every such tangent perturbation requires
\(\int_T^\infty\lambda=\infty\). Conversely, assume the original loss
has any exponential tail \(L(t)\le Ce^{-\eta t}\), \(\eta>0\). Put
\(u=1-r\). Then \(u\ge0\), \(u\to0\), and
\(\int_T^\infty u<\infty\). Integrating (18) gives

\[
\int_T^t\lambda(s)r(s)ds
   =2\int_T^t u(s)ds-r(t)+r(T).                 \tag{20}
\]

The right side is bounded as \(t\to\infty\). Since \(r(t)\to1\),
we have \(r(t)\ge1/2\) for all sufficiently large \(t\); nonnegativity
then forces \(\int_T^\infty\lambda<\infty\). Equation (19) therefore
retains a strictly positive fraction of every nonzero tangent perturbation.

This contradiction uses no asymptotic regularity or monotonicity assumption
on \(\lambda\), and even does not need to assume \(\lambda(t)\to0\).
It is an exact obstruction to this isotropic-decay construction, not to all
regularizers or all coupled nonlinear systems.

For an explicit selection schedule, take \(\lambda(t)=1/(1+t)\). Direct
solution of \(u'+(2+1/(1+t))u=1/(1+t)\), \(u(0)=1\), gives

\[
u(t)=\frac{1+e^{-2t}}{2(1+t)},\qquad
z(t)=\frac{z(0)}{1+t}.
\]

It erases tangent memory and reaches zero loss, but the loss is asymptotic
to \(1/[4(1+t)^2]\), not exponential.

### 5.3 A hidden anchor alone does not select the readout

Add only \(\gamma\|h-h_0\|^2/2\) to the original objective, with
\(\gamma>0\). Every state

\[
h=h_0,\qquad c=B_{h_0}Y+q,\qquad q\in\ker A_{h_0}
\]

is stationary: both the loss gradient and the hidden-anchor gradient are
zero. The assigned feature theorem shows that these stationary points can
give arbitrary values at a new query. Thus a unique anchor in hidden space
is not a selection criterion for the full predictor. Anchoring the readout
at its canonical zero as well introduces the ordinary weight-decay bias
illustrated by (17). Additional constraints or projections would need their
own proof.

## 6. A modest constructive alternative, with its exact boundary

The scalar tradeoff disappears if contraction acts only on the readout
nullspace. Freeze hidden features at a known \(h\) with \(K_h>0\), and
write \(A,K,B,P\) for its fixed operators. For \(\gamma>0\), consider

\[
dc=\{-2A^*(Ac-Y)-\gamma Pc\}dt+q\sigma(t)dB_t,
\quad q\in\ker A,\quad \sigma(t)=0\ (t\ge1).             \tag{21}
\]

Then exactly

\[
\dot e=-2Ke,\qquad
d(Pc)=-\gamma Pc,dt+q\sigma(t)dB_t.
\]

The row component converges to \(BY\); after time one the null component
decays as \(e^{-\gamma(t-1)}Pc_1\). Thus every realization converges to
the same minimum-norm interpolant, with exponential zero training loss.
This is causal, uses only the present fixed Gram matrix and data, and does
not encode a future endpoint. It is also a changed optimizer with frozen
hidden features, so it is not a solution of the intended full-feature
learning problem. For moving \(h\), differentiating \(P_hc\) introduces
\(DP_h[\dot h]c\); omitting that transport term is not justified by (21).

The useful design lesson is precise: a deterministic selection contraction
that is invisible to the fitted constraints can coexist with exponential
fitting. Noise disappearance alone supplies no such contraction. A proposed
full physical construction must identify what selects the hidden state and
the readout-nullspace component, prove those mechanisms in the moving
geometry, and preserve an explicit exponential residual estimate.

## Claim ledger and remaining gap

| Claim | Status and scope |
|---|---|
| Arbitrarily small eventually vanishing additive noise can leave a random predictor despite exponential fitting | Proved in Section 1 for the exact canonical-start order-one physical flow and one compatible example |
| All possible genuine noisy extensions fail deterministic selection | Not claimed; the construction falsifies only an unrestricted inference from noise decay |
| Positive random clocks select a new endpoint | False as a mechanism: they reparameterize the original orbit, conditional on existence |
| Loss curvature contracts all prediction directions near interpolation | False in general by (13), with an exact persistent direction in Section 1 |
| SGD continues mixing at an exact interpolant | False for ordinary square-loss sampling; every sample gradient is zero |
| Canonical SGD has path-dependent endpoints in the full model | Open here; neither a proof nor a counterexample was obtained |
| Isotropic decay universally erases tangent memory while preserving exponential zero loss | False already in (18)--(20) |
| Hidden anchoring alone determines the represented predictor | False as a stationary-selection claim |
| Projected nullspace decay works at fixed hidden features | Proved by (21); extension to moving hidden features is not supplied |

No blanket conclusion about universal fitting or uniqueness of the original
noiseless canonical gradient-flow endpoint follows from this report. The
decisive missing ingredient for a successful modified full-feature theorem
is an explicit, verified selection drift or equivalent constrained dynamics,
not merely an escape or annealing argument.
