# Full loss-mesh verdict and joint width--mesh scaling

## 1. Contract

For one input, two hidden layers, and width \(n\), let

\[
 H_j=\phi(u_j),\qquad z_i=n^{-1/2}\sum_{j=1}^nW_{ij}H_j,
 \qquad f_n=n^{-1}\sum_{i=1}^na_i\phi(z_i),
\]

with mutually independent standard-Gaussian \(a_i,u_j,W_{ij}\) at
initialization.  For the one-sample half-square loss

\[
 \ell_n={1\over2}(1-f_n)^2,
\]

put \(g_n=n\nabla f_n\).  The finite-width loss flow and its explicit Euler
scheme are

\[
 \dot\theta=(1-f_n)g_n,\qquad
 \theta_{k+1}=\theta_k+h_n(1-f_n(\theta_k))g_n(\theta_k).
 \tag{1.1}
\]

The gradient-flow clock is \(t=kh_n\).  Thus \(h_n\downarrow0\) resolves
time; it does not slow the vector field in (1.1).

The full mesh guarantee means convergence in probability of the continuous
interpolated predictor and loss in \(C([0,T])\), with their initialized
traces.  A comparison only at the common terminal point of two meshes is
strictly weaker.

## 2. Final verdict

### Normalized quadratic

For

\[
 \phi(x)=x^2/\sqrt3,
\]

the width-first mesh limit fails: every fixed level \(0<\delta<1\) is
reached at a physical time tending to zero.  The finite-width ODE also has a
fixed output and loss change by time \(O((\log n)^{-1/2})\).  Consequently
every joint mesh that is consistent with that finite-width ODE through this
initial layer fails to converge to a continuous initialized mean-field
gradient flow.

One explicit, nonempty ODE-consistent class is obtained by setting

\[
 L_n=\sqrt{\log n},\qquad
 h_n n^{14}\exp\!\left({6\cdot10^{11}n^9\over L_n}\right)\longrightarrow0.
 \tag{2.1}
\]

This rate is sufficient and very nonsharp.  No theorem currently classifies
all deliberately under-resolved diagonals.  Such a diagonal, even if it
converged, would be a discretization-selected dynamics rather than the
joint limit of the canonical finite-width gradient flow.

### Normalized ReLU

For

\[
 \phi(x)=\sqrt2\,x_+,
\]

an ordinary ODE obtained by fixing one value of \(\phi'(0)\) is not globally
well posed.  An open positive-Gaussian-probability set already at width two
hits an attracting gate at which no classical continuation exists.

Hard explicit Euler may nevertheless converge to a Filippov/Young-measure
dynamics.  Whether its actual width-first or joint width--mesh paths converge
to a unique restartable generalized mean-field flow is open.  In particular,
no deterministic \(h_n\downarrow0\) is presently proved sufficient.

There is, however, a positive compactness result: for every deterministic
\(h_n\downarrow0\), the scalar Euler predictor and loss are tight in
\(C([0,T_0])\), where
\[
 T_0={1\over384\cdot6^4}.
\]
Every subsequential limit is continuous and starts at output zero and loss
one half.  Thus ReLU has no quadratic-type scalar initial jump on this
interval.  The classical ReLU answer is negative; existence of continuous
subsequences is positive; uniqueness and identification of the generalized
hard-Euler limit remain unresolved.

## 3. Width-first quadratic initial layer

Let \(F_k^h\) be the deterministic width-first output after \(k\) loss
steps.  For a deterministic nonnegative feature-step schedule
\(s=(s_0,\ldots,s_{m-1})\), write \(\mathcal F_m(s)\) for the width-first
feature-ascent output.

At finite width, every updated coordinate is a polynomial with nonnegative
formal coefficients in the raw Gaussian coordinates and in the schedule.
Gaussian expectation deletes monomials with an odd exponent and is positive
on every even monomial.  Hence, after passing to the fixed-schedule width
limit,

\[
 0\le s_k\le\widetilde s_k\quad\Longrightarrow\quad
 \mathcal F_m(s)\le\mathcal F_m(\widetilde s).          \tag{3.1}
\]

The exact width-first loss recursion is

\[
 F_k^h=\mathcal F_k(s_0,\ldots,s_{k-1}),\qquad
 s_k=h(1-F_k^h).                                        \tag{3.2}
\]

Before \(F_k^h\) reaches \(\delta\in(0,1)\), therefore,

\[
 s_k\ge(1-\delta)h.                                    \tag{3.3}
\]

The audited all-order quadratic feature theorem gives, for every
\(\rho>0\),

\[
 \mathcal F_{2t}(\rho/t,\ldots,\rho/t)\longrightarrow+\infty.
 \tag{3.4}
\]

Take \(h_N=T/N\), fix \(\varepsilon>0\), and put

\[
 t_N=\left\lfloor{\varepsilon\over2h_N}\right\rfloor,
 \qquad \rho_*={(1-\delta)\varepsilon\over4}.
\]

Eventually \(\rho_*/t_N\le(1-\delta)h_N\).  If the loss trajectory did not
hit \(\delta\) by step \(2t_N\), (3.1)--(3.3) would imply

\[
 F_{2t_N}^{h_N}\ge
 \mathcal F_{2t_N}(\rho_*/t_N,\ldots,\rho_*/t_N)
 \longrightarrow+\infty,
\]

contradicting \(F_{2t_N}^{h_N}<\delta\).  Since \(\varepsilon\) is
arbitrary, the first hitting time \(\tau_N(\delta)\) tends to zero.

If continuous interpolants converged uniformly to a continuous \(F\) with
\(F(0)=0\), evaluation at crossing times would give
\(\delta=F_N(\tau_N)\to F(0)=0\), a contradiction.  At the same crossing,

\[
 \left|{1\over2}(1-\delta)^2-{1\over2}\right|
 =\delta-{\delta^2\over2}>0,
\]

so the loss has the same obstruction.

## 4. Joint quadratic no-go for every ODE-consistent diagonal

Let \(f_n^{\rm ode}\) solve (1.1).  The covariant-Schur concentration theorem
provides deterministic \(\delta_0>0\) and random \(\tau_n\le2/L_n\), with
probability tending to one, such that

\[
 f_n^{\rm ode}(\tau_n)-f_n^{\rm ode}(0)\ge\delta_0.
 \tag{4.1}
\]

Therefore any diagonal satisfying

\[
 \sup_{0\le t\le2/L_n}
 |\bar f_n^{h_n}(t)-f_n^{\rm ode}(t)|
 \xrightarrow{\mathbb P}0                             \tag{4.2}
\]

has a fixed predictor and loss change at times tending to zero and cannot
have a continuous initialized compact-time limit.  This implication covers
every honest ODE-resolving joint scaling, independently of how (4.2) is
proved.

For completeness, (2.1) is an explicit sufficient condition for (4.2).
On the Euclidean ball \(\|\theta\|_2\le4n\), direct polynomial estimates
give

\[
 \|V_n\|_2\le4\cdot10^8n^{10},\qquad
 \|DV_n\|_{\rm op}\le3\cdot10^{11}n^9,
 \qquad \|Df_n\|_{\rm op}\le20480n^4,                 \tag{4.3}
\]

where \(V_n=(1-f_n)g_n\).  The exact energy identity

\[
 {d\ell_n\over dt}=-{1\over n}\|\dot\theta\|_2^2
 \tag{4.4}
\]

keeps the ODE in the radius-\(3n\) ball on the relevant interval with
probability tending to one.  Euler's defect estimate and discrete Gronwall
then yield

\[
 \sup_{0\le t\le2/L_n}
 |\bar f_n^{h_n}(t)-f_n^{\rm ode}(t)|
 \le2\cdot10^{13}n^{14}h_n
 \exp\!\left({6\cdot10^{11}n^9\over L_n}\right).       \tag{4.5}
\]

Condition (2.1) makes (4.5) vanish and also closes the radius-\(4n\)
bootstrap.  For example, \(h_n=\exp(-10^{12}n^9)\) belongs to this proved
class for all sufficiently large \(n\).

The much larger candidate scale

\[
 h_n=o\!\left({(\log n)^{1/4}\over\sqrt n}\right)
 \tag{4.6}
\]

is suggested by the fastest terminal column in the concentration proof,
but is not a proved sufficient or necessary condition.  Establishing it
requires a discrete covariant-Schur theorem.

## 5. Exact ReLU obstruction and why a joint rate is not known

At width two take

\[
 u=(1,1),\quad W_1=(1,-1),\quad W_2=(2,0),\quad
 a_1=-1/\sqrt2,\quad a_2=1/(4\sqrt2).
\]

Then the first top preactivation is zero, the second is two, \(f=1/4\), and
the residual is \(3/4\).  The normal velocity at the first gate has the two
one-sided values

\[
 p=3/8>0,\qquad q=-21/8<0.                             \tag{5.1}
\]

Both sides point toward the gate.  Any fixed derivative convention assigns
a nonzero velocity at the gate after an arbitrarily small adjustment of
\(a_1\), while preserving \(p>0>q\).  If an absolutely continuous
classical solution started at contact, \(w=|z_1|\) would satisfy
\(w'\le-\gamma\) almost everywhere on \(\{w>0\}\) and \(w'=0\) almost
everywhere on \(\{w=0\}\).  Hence \(w\equiv0\), contradicting the assigned
nonzero gate velocity.  A transverse backward flow tube is open and has
positive Gaussian probability, so this is a genuine reached obstruction,
not merely a measure-zero initialized contact.

Hard Euler at a frozen attracting gate instead obeys

\[
 z_{k+1}=z_k+h\{p+(q-p)I_k\},\qquad I_k={\bf1}_{\{z_k>0\}}.
\]

Inside its invariant strip it is conjugate to a circle rotation, and with
\(\lambda=p/(p-q)\),

\[
 \left|\sum_{k=0}^{N-1}I_k-N\lambda\right|<1.          \tag{5.2}
\]

It therefore selects the binary Young measure

\[
 (1-\lambda)\delta_0+\lambda\delta_1.                 \tag{5.3}
\]

Every positive gate moment under (5.3) is \(\lambda\), whereas replacing
the gate by its scalar mean would give second moment \(\lambda^2\).  The
loss tangent kernel sees squared cotangents, so a scalar averaged gate does
not close the dynamics.

The scalar local compactness assertion above follows without differentiating
through a gate.  With normalized vector norm \(\|\cdot\|_n\), put
\[
 A=\|a\|_n,\qquad U=\|u\|_n,\qquad
 G=\|W/\sqrt n\|_{\rm op},\qquad R=\max\{1,A,U,G\}.
\]
ReLU Lipschitzness and \(|\phi'|\le\sqrt2\) give for one exact Euler step
\[
 R^+\le R+6hR^5.                                      \tag{5.4}
\]
On the event \(A_0,U_0\le2\), \(G_0\le6\), whose probability tends to one,
(5.4) keeps \(R\le12\) through time
\(T_*=1/(192\cdot6^4)\).  On consecutive states in that ball, a direct
forward calculation gives
\[
 |f^+-f|\le60\cdot12^7h.                              \tag{5.5}
\]
Hence every predictor interpolation is uniformly bounded and
equi-Lipschitz on \([0,T_0]\).  Arzelà--Ascoli gives tightness.  Finally,
independence of \(a_0\) from the initialized upper features and RMS
normalization give exactly
\[
 \mathbb E f_n(0)^2={1\over n},
\]
so all subsequential limits have the initialized trace.  The loss follows
by continuous mapping.

At initialization the number of either lower or upper gates in
\([-bh_n,bh_n]\) has the exact marginal regimes

\[
 {N_n(b)\over nh_n}\xrightarrow{\mathbb P}b\sqrt{2/\pi}
 \quad(nh_n\to\infty),                                 \tag{5.6}
\]

is asymptotically Poisson when \(nh_n\to\lambda\in(0,\infty)\), and is zero
with high probability when \(nh_n\to0\).  This is only an initialization
spatial-slab law.  The temporal occupation law (5.2) is independent of this
count, and reused \(W/W^{\mathsf T}\) creates adaptive dependencies at later
times.  Thus neither \(nh_n\to\infty\) nor the benchmark
\(nh_n/\log(1/h_n)\to\infty\) is presently a path-convergence theorem.

The missing theorem must simultaneously prove fixed-mesh adaptive-indicator
OMFP identification, growing-history concentration, dynamic small-ball
control, joint multigate Young-measure convergence, reused-adjoint square
tails, and uniqueness/restartability.  Until then no \(h_n\) is a proved
solution for actual hard ReLU.

## 6. What can make a continuous limit exist

1. **Change the activation.**  For normalized arctangent, the same depth-two
   feature-learning scaling has a proved, unique, global, restartable
   pointed-action IDE, and finite predictors, tangent kernels, and losses
   converge uniformly on every compact physical-time interval.

2. **Normalize the optimizer by the tangent kernel.**  For the smooth
   quadratic model (and, more generally, along any differentiable trajectory),
   put

   \[
   K_n=Df_n[g_n]={1\over n}\|g_n\|_2^2
   \]

   and, on \(K_n>0\), replace (1.1) by

   \[
   \dot\theta={(1-f_n)g_n\over K_n}.
   \]

   Then exactly

   \[
   \dot f_n=1-f_n,\qquad
   f_n(t)=1-(1-f_n(0))e^{-t},\qquad
   \ell_n(t)=\ell_n(0)e^{-2t}.                         \tag{6.1}
   \]

   This gives a width-independent continuous predictor/loss clock, but it
   is a different optimizer and (6.1) alone does not prove compactness of
   the full parameter state.

3. **Specify a generalized ReLU solution concept.**  An occupation-augmented
   hard-Euler/Filippov OMFP could in principle work, but it must retain the
   full gate moments and correlations in (5.3); its existence and uniqueness
   are open.  Smooth softplus is a different selection at second gate order
   and cannot silently substitute for hard Euler.

4. **Rescale the dynamics rather than merely its numerical mesh.**  Adding a
   separate multiplier \(\alpha_n\) to the vector field changes the physical
   clock.  For the quadratic model, the deterministic envelopes (4.3) show
   explicitly that
   \[
   \alpha_n n^{14}\longrightarrow0
   \]
   gives the trivial frozen predictor/loss limit on every fixed interval:
   on the high-probability initialization event, the scaled flow stays in
   the radius-\(4n\) ball and
   \[
   \sup_{t\le T}|f_n(t)-f_n(0)|
   \le (20480n^4)(4\cdot10^8n^{10})\,T\alpha_n
   \longrightarrow0.
   \]
   This is a changed, vanishing-speed model, not the original gradient-flow
   clock.  The diagnostic critical scale
   \(\alpha_n\sqrt{\log n}\asymp1\) instead zooms into the quadratic
   extreme-coordinate layer and has not been identified as an ordinary
   mean-field flow.

5. **Weaken the endpoint contract.**  One may seek a post-layer limit on
   \([\varepsilon,T]\), or an impulse-renormalized initial state.  Neither
   post-layer quadratic dynamics nor the hard-ReLU generalized path has yet
   been proved, so this is a reformulation rather than an existing theorem.

## 7. Audit boundary

The following are proved: the quadratic width-first initial layer; the
finite-width quadratic ODE initial layer; the explicit Euler-consistent
joint no-go (2.1); the finite-width classical ReLU attracting-gate
obstruction; width- and mesh-uniform local tightness of the ReLU scalar
predictor and loss; the initialization gate-slab law; and the frozen
hard-Euler occupation law.

The following are not proved and are not asserted: failure for every
under-resolved quadratic diagonal; existence or nonexistence of a unique
hard-ReLU generalized joint limit; a sufficient ReLU rate based only on
\(nh_n\); or convergence of the terminal coarse/fine scalar loss after an
initial layer.
