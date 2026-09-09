# R3 — Harmonic activation, exact curvature cancellation, and its obstruction

Status: analytic sidecar result, 2026-09-06. **The target remains OPEN.**
One candidate is analyzed; no second candidate is proposed. The candidate
has an exact curvature/readout-energy identity, but that identity does not
establish the required global stability. The positive results below are
initialization facts and structural lemmas, not a population theorem.

## 1. Scope and candidate

The contract and route registry in this directory were read fully. The
mandatory `solve-math-rigorously` and `investigate-conjectures` skills were
read, together with the latter's research-contract, evidence-ledger,
adversarial-audit, and proof-search-orchestration references. Relevant
sections of the specified one-sample proof were read: the model/setup,
operator-state and comparison construction, response estimate, and
physical-time energy/clock argument. No theorem for another activation is
imported. No experiments, agents, clipping, or changes to old artifacts
were used. Sample-exchange symmetry and the first-layer coordinate change
are left to R1.

The subsequently supplied `EXACT_TWO_SAMPLE_REDUCTION.md` was also read
fully. Its finite symmetry is in law; its population symmetry statements
retain their deterministic-limit or intrinsic existence/uniqueness
premises. This note does not remove those premises. Section 6 below
records the consequence of its short-feature-time obstruction for (1).

Use, in all three hidden layers, the single fixed activation

\[
                 \phi(z)=\sin z+\cos z.
\tag{1}
\]

Its amplitude and frequency are fixed independently of width, horizon,
angle, and labels. It is smooth, bounded, nonlinear, neither even nor odd,
and satisfies the exact identities

\[
 |\phi|,|\phi'|\le\sqrt2,\qquad
 \phi''=-\phi,\qquad \phi^2+(\phi')^2=2.
\tag{2}
\]

The proposed mechanism is to replace a small feature-clock interval by
an energy cancellation in curvature-driven response equations. Sections
3–5 identify exactly what this mechanism does and does not control.
There is no change of initialization, learning-rate scaling, physical
clock, or layer updates.

## 2. Proved initialization facts, including antiparallel inputs

For centered jointly Gaussian real variables \(U,V\),

\[
 \phi(U)\phi(V)=\cos(U-V)+\sin(U+V),
\]

so

\[
 \mathbb E[\phi(U)\phi(V)]
       =\exp\{-\operatorname{Var}(U-V)/2\}.
\tag{3}
\]

Here the sine expectation vanishes by joint sign symmetry; the cosine
expectation follows by integrating the Gaussian characteristic function.
In particular \(\mathbb E\phi(U)^2=1\) for every centered Gaussian
\(U\), including degenerate ones.

At initialization define the uncentered feature Gram matrices
\(Q^{(\ell)}_{ab}=\mathbb E[H^{(\ell)}_aH^{(\ell)}_b]\).
The prescribed Gaussian forward initialization and (3) give

\[
 Q^{(\ell)}=\begin{pmatrix}1&c_\ell\\c_\ell&1\end{pmatrix},
 \quad c_1=e^{-(1-\rho)},\quad
 c_2=e^{-(1-c_1)},\quad c_3=e^{-(1-c_2)}.
\tag{4}
\]

To justify the forward step directly, conditional on previous features
each next-layer row is exactly centered Gaussian with covariance their
empirical Gram matrix, independently across rows. Conditional variances
of bounded empirical feature products tend to zero. Formula (3),
continuity in the covariance, and induction then give (4). Thus this
calculation requires only a forward Gaussian law at initialization.

For every \(\rho<1\), including \(\rho=-1\), all three \(c_\ell\)
belong to \((0,1)\). The feature Gram matrices are therefore positive
definite. At antiparallel inputs specifically,

\[
 \phi(G)+\phi(-G)=2\cos G,\qquad
 \phi(G)-\phi(-G)=2\sin G,
\]

and neither is zero as a Gaussian random variable. Both label modes
survive through all three forward layers. At zero population readout,

\[
 \dot W^{(4)}(0)=2\big(y_1H^{(3)}_1+y_2H^{(3)}_2\big),
\quad
 \|\dot W^{(4)}(0)\|_2^2
       =8(1+y_1y_2c_3)>0.
\tag{5}
\]

This rules out the stipulated parity-induced stationary initialization
for either label choice. For comparison, an exactly odd activation at
antiparallel inputs preserves opposite hidden features through the
forward network; same labels then cancel the readout update. An exactly
even activation makes the first features equal; opposite labels then
cancel the readout update. At zero readout the hidden updates also vanish
in either case. Candidate (1) has neither cancellation.

Strict distributional nonlinearity at initialization is also explicit.
For \(G\sim N(0,v)\), \(v>0\), Gaussian integration gives

\[
 \mathbb E\phi(G)=e^{-v/2},\quad
 \mathbb E[G\phi(G)]=ve^{-v/2},\quad
 \mathbb E\phi(G)^2=1.
\]

Minimizing the quadratic error over real \(a,b\) yields

\[
 \inf_{a,b}\mathbb E\big(\phi(G)-aG-b\big)^2
             =1-(1+v)e^{-v}>0.
\tag{6}
\]

The strict inequality is \(e^v>1+v\). Each initialized hidden marginal
has \(v=1\), so its error is \(1-2/e\), a fixed positive number.
Neither (5) nor (6) proves nonlinearity at every later time or feature
learning in every hidden layer. Those target obligations remain open.

## 3. Exact curvature/readout-energy identity

Work first at finite width, using the contract's actual physical time.
For one top-layer neuron \(i\), set

\[
 a=W^{(4)}_i,\quad u=\sqrt n\,W^{(3)}_{i,:}\in\mathbb R^n,
 \quad v_b=h^{(2)}_b/\sqrt n,\quad p_b=-2r_b.
\]

Then \(z_b=u\cdot v_b\), and the exact row/readout updates are

\[
 \dot a=S(u):=\sum_{b=1}^2p_b\phi(z_b),\qquad
 \dot u=a\,g(u),\quad
 g(u):=\sum_{b=1}^2p_b\phi'(z_b)v_b.
\tag{7}
\]

The coefficients \(p_b,v_b\) in (7) are their current values in the
fully trained model. For the following partial derivative they are held
fixed as independent arguments; this is a Jacobian block calculation,
not a dynamics with frozen layers. Differentiating (7) with respect to
\((a,u)\) gives the symmetric direct block

\[
 J=\begin{pmatrix}
 0&g^T\\
 g&-a\sum_b p_b\phi(z_b)v_bv_b^T
 \end{pmatrix}.
\tag{8}
\]

Changes in residuals and lower features supply additional terms in the
full network variation equation. They are not included in \(J\).

Put \(\kappa_b=\|v_b\|^2\),
\(\kappa=(\kappa_1+\kappa_2)/2\), and
\(\epsilon=(\kappa_1-\kappa_2)/2\). Taking the trace of (8) proves

\[
 \operatorname{tr}J
   =-\kappa a\dot a
     -\epsilon a\,[p_1\phi(z_1)-p_2\phi(z_2)].
\tag{9}
\]

In particular, **under the explicitly stated condition**
\(\kappa_1(t)=\kappa_2(t)=\kappa(t)\),

\[
 \operatorname{tr}J=-\frac{\kappa}{2}(a^2)'.
\tag{10}
\]

No sample-exchange assertion is needed for (9), and none is proved here.
If R1 supplies equal norms along a population solution, it may use (10).

More precisely, let \(\Psi'=J\Psi\), \(\Psi(0)=I\), on an interval
where the coefficients are continuous and \(\kappa\) is absolutely
continuous. The inverse fundamental matrix solves
\((\Psi^{-1})'=-\Psi^{-1}J\), so \(\Psi\) stays invertible.
Differentiation of the determinant then gives
\((\log\det\Psi)'=\operatorname{tr}J\). Integrating (10) by parts
proves the exact formula

\[
 \log\det\Psi(t)
 =-\tfrac12\kappa(t)a(t)^2
  +\tfrac12\kappa(0)a(0)^2
  +\tfrac12\int_0^t\kappa'(s)a(s)^2\,ds.
\tag{11}
\]

Thus harmonic curvature does produce an energy identity. It controls
the volume change of this direct response block. It is not a bound on
\(\|\Psi\|\), and is not the determinant formula for the full network
response after the omitted couplings are restored.

This cancellation family is essentially forced if one demands only an
endpoint function of the readout. Suppose a nonconstant bounded smooth
activation \(\psi\), a nonzero \(a\), and a scalar energy \(E(a)\)
satisfy, for arbitrary \(p_1,p_2,z_1,z_2\),

\[
 a\sum_b p_b\psi''(z_b)
       =E'(a)\sum_b p_b\psi(z_b).
\tag{12}
\]

Taking one coefficient nonzero shows \(\psi''=c\psi\), with
\(c=E'(a)/a\). Requiring the same identity for other nonzero readout
values makes \(c\) constant and \(E(a)=ca^2/2+\mathrm{constant}\).
For \(c>0\), the solutions are linear combinations of
\(e^{\sqrt c z}\) and \(e^{-\sqrt c z}\); boundedness at both ends
forces zero. For \(c=0\), boundedness makes an affine solution constant.
For \(c<0\), the bounded solutions are harmonic functions. Candidate
(1) takes \(c=-1\) and includes both parities. This proves a restricted
classification for identity (12), not a no-go theorem for more elaborate
energies involving lower layers or other state variables.

## 4. Exact obstruction: zero trace with an expanding curvature direction

Here is a state of the **full, unchanged** finite model, with no frozen
layers. It is an algebraic obstruction to a global curvature-sign or
trace-to-norm argument, not a state claimed to arise from Gaussian
initialization.

Take \(n=2,d=1,x_1=1,x_2=-1\), labels \((1,-1)\), and any
\(a>0\). Set

\[
 W^{(1)}=\begin{pmatrix}0\\\pi/4\end{pmatrix},\qquad
 W^{(2)}=\begin{pmatrix}
 -\pi/4&\pi/(2\sqrt2)\\
 \pi/4&-\pi/(2\sqrt2)
 \end{pmatrix},
\]
\[
 W^{(3)}=\frac{\pi}{4\sqrt2}
       \begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
 W^{(4)}=\begin{pmatrix}a\\-a\end{pmatrix}.
\tag{13}
\]

Direct substitution gives

\[
 h^{(1)}_1=(1,\sqrt2)^T,\quad h^{(1)}_2=(1,0)^T,
\]
\[
 z^{(2)}_1=(\pi/4,-\pi/4)^T,\quad
 z^{(2)}_2=(-\pi/4,\pi/4)^T,
\]
\[
 h^{(2)}_1=(\sqrt2,0)^T,\quad
 h^{(2)}_2=(0,\sqrt2)^T,
\quad z^{(3)}_1=z^{(3)}_2=(\pi/4,\pi/4)^T.
\]

Both top features equal \((\sqrt2,\sqrt2)^T\); hence \(f_1=f_2=0\),
\(r=(-1,1)\), and \(p=(2,-2)\). The top gate vanishes because
\(\phi'(\pi/4)=0\). Consequently every hidden velocity vanishes, and
the readout velocity vanishes because the two top features agree.
State (13) is an exact stationary point of the full equations.

For its first top neuron, \(v_1=e_1,v_2=e_2\), \(g=0\), and the
incoming-row part of (8) is

\[
 J_{uu}=\begin{pmatrix}-2\sqrt2a&0\\0&2\sqrt2a\end{pmatrix}.
\tag{14}
\]

Its trace is zero, while one direction expands. The auxiliary direct
response has factors \(e^{-2\sqrt2at}\) and \(e^{2\sqrt2at}\), with
product one. Thus even exact identity (11) cannot turn determinant
control into norm control.

The expanding direction is also a true negative-curvature direction of
the full loss, not an artifact of dropping the residual derivative.
Perturb only the second coordinate of \(u_1\) by \(\tau\). Then
\(f_1(\tau)=0\) and

\[
 f_2(\tau)=\frac a2
       [\phi(\pi/4+\tau)-\sqrt2],\qquad
 f_2'(0)=0,\quad f_2''(0)=-a/\sqrt2.
\]

Since \(L=1+(f_2+1)^2\) on this perturbation,

\[
                         L''(0)=-\sqrt2a<0.
\tag{15}
\]

At a stationary point, the gradient-flow linearization is minus the
loss Hessian in the fixed positive parameter metric. A negative Hessian
direction implies a positive eigenvalue after conjugating by the square
root of that metric. Therefore the full stationary point is linearly
unstable. This disproves global dissipativity of the proposed curvature
mechanism over all states. It does **not** disprove bounded evolution,
uniqueness, or feature learning from the prescribed initialization.
In particular, it is not legitimate to replace that initialization by
(13) and call it a counterexample to the contract.

## 5. A Gaussian-initialization obstruction at the actual middle gate

The missing estimate is more specific than the saddle in Section 4.
The middle backward field is
\(\delta^{(2)}_a=\phi'(Z^{(2)}_a)q^{(2)}_a\). Its variation contains

\[
 d\delta^{(2)}_a
    =\phi'(Z^{(2)}_a)dq^{(2)}_a
       -\phi(Z^{(2)}_a)q^{(2)}_a\,dZ^{(2)}_a.
\tag{16}
\]

The harmonic identity has replaced the curvature by a bounded feature;
it has not removed the unbounded backward multiplier. The sign of this
multiplier is already uncontrolled at the first nonzero initialization
coefficient, as the following static Gaussian calculation proves.

Let \((U_1,U_2)\) be the initialized top preactivation pair with
covariance \(Q^{(2)}\), and define bounded smooth functions

\[
 S(U)=y_1\phi(U_1)+y_2\phi(U_2),\qquad
 V_a(U)=S(U)\phi'(U_a).
\]

Let \(Q_a\) denote the initialized transpose query
\((W^{(3)}_0)^*V_a\). Its same-neuron law on the middle layer has the
form

\[
 Q_a=\sum_{b=1}^2 m_{ab}H^{(2)}_{b,0}+G_a,
 \quad m_{ab}=\mathbb E[\partial_bV_a(U)],
 \quad\mathbb E[G_aG_c]=\mathbb E[V_a(U)V_c(U)],
\tag{17}
\]

where the centered Gaussian vector \((G_1,G_2)\) is independent of the
initialized middle preactivation pair. In particular
\(\sigma_a^2:=\mathbb E G_a^2=\mathbb E V_a(U)^2>0\).

Here is a direct justification of (17), including why its Gaussian term
does not disappear into the forward-feature span. Condition on the full
lower-layer initialization, and let
\(H\in\mathbb R^{n\times2}\) be its middle-feature matrix. Write
\(C_n=H^TH/n\), \(P=H(H^TH)^{-1}H^T\), and \(U=WH\).
On invertibility of \(C_n\), Gaussian orthogonal projection gives

\[
 W=U(H^TH)^{-1}H^T+R(I-P),
\]

where \(R\) has independent \(N(0,1/n)\) entries and is independent
of \(U\) conditional on \(H\). This decomposition follows row by row:
orthogonal Gaussian projections have zero covariance and hence are
independent. For the vector \(V_a\) evaluated on the rows of \(U\),

\[
 W^TV_a=HC_n^{-1}(U^TV_a/n)+(I-P)R^TV_a.
\tag{18}
\]

Conditional on \(H,U\), the last terms for \(a,c\) are Gaussian with
cross-covariance \((V_a^TV_c/n)(I-P)\). From (4), \(C_n\to Q^{(2)}\)
in probability and the limit is positive definite. The rows of \(H\)
are bounded, so \(P_{jj}=O(1/n)\) on any fixed lower bound for the
smallest eigenvalue of \(C_n\). Conditional laws of large numbers give
\(U^TV_a/n\to\mathbb E[UV_a(U)]\) and
\(V_a^TV_c/n\to\mathbb E[V_aV_c]\). For the first limit the conditional
variances are bounded by a constant times \(1/n\), since \(V_a\) is
bounded and the Gaussian covariance is bounded. The second has bounded
summands. At any tagged coordinate the conditional residual covariance
therefore tends to the deterministic covariance in (17). Its conditional
Gaussian characteristic function converges to a constant independent of
the middle features; this proves the asserted independence in the
same-neuron limit. Finally, integration by parts in the nonsingular
Gaussian density gives

\[
 \mathbb E[UV_a(U)]=Q^{(2)}\mathbb E[\nabla V_a(U)],
\]

which identifies the mean in (17). The boundary terms vanish because
\(V_a\) and its derivatives are bounded and the density is Gaussian.

To see \(\sigma_a>0\), the law of \(U\) has a positive density on
\(\mathbb R^2\). For \(a=1\), choose \(U_1=0,U_2=-\pi/4\): then
\(V_1=y_1\ne0\), for either label pair. Continuity gives a positive
Gaussian-measure neighborhood. Interchange the coordinates for \(a=2\).

In fact the entire covariance
\(\Sigma=(\mathbb E[V_aV_c])_{a,c=1}^2\) is positive definite.
If \(\alpha^T\Sigma\alpha=0\), continuity and the positive Gaussian
density imply

\[
 S(u_1,u_2)[\alpha_1\phi'(u_1)+\alpha_2\phi'(u_2)]=0
                  \quad\hbox{for all }(u_1,u_2).
\]

There is an open rectangle on which \(S\ne0\), by the preceding
explicit nonzero value. On that rectangle, differentiate the second
factor in \(u_1\) and in \(u_2\). This gives
\(\alpha_1\phi''(u_1)=\alpha_2\phi''(u_2)=0\). Since the harmonic
\(\phi''\) is not identically zero on any interval, \(\alpha=0\).

Since each middle \(Z^{(2)}_{a,0}\) has a continuous Gaussian marginal,
\(\phi(Z^{(2)}_{a,0})\ne0\) almost surely: its zeros form a countable
discrete set. Conditional on the middle pair, the curvature coefficient

\[
                  -\phi(Z^{(2)}_{a,0})Q_a
\tag{19}
\]

is Gaussian with strictly positive variance
\(\phi(Z^{(2)}_{a,0})^2\sigma_a^2\). It has both signs and arbitrarily
large values in both directions with positive probability. This applies
to every \(\rho<1\) and both label patterns, including antiparallel.

**The scalar label-mode reduction does not cancel this innovation.**
Indeed set \(B_a=y_a\phi''(Z^{(2)}_{a,0})\). Conditional on the
middle pair,

\[
 \sum_{a=1}^2y_a\phi''(Z^{(2)}_{a,0})Q_a
     \quad\hbox{has Gaussian variance}\quad B^T\Sigma B>0.
\tag{19a}
\]

The vector \(B\) is nonzero almost surely and \(\Sigma\) is positive
definite, as just proved. Thus even this label-weighted combination has
both unbounded tails. This is an exact obstruction to cancellation of
the initial middle curvature by summing the two residual contributions;
it does not exclude cancellation with additional state variations in a
more elaborate energy.

Calculation (17) is an initialization statistic independent of any
population existence assertion. If a sufficiently differentiable
population trajectory is established, then zero readout gives

\[
 (q^{(2)}_a)'(0)=2Q_a,
\tag{20}
\]

because \((W^{(4)})'(0)=2S\) and the hidden velocities initially vanish.
Thus (19) is half the first nonzero coefficient of the troublesome
curvature multiplier in (16). It rules out a sign-definite first-order
damping argument and a deterministic essential bound on that coefficient.
It does not rule out moment estimates, a later state-dependent bound,
or an energy that cancels this term against other variations.

## 6. What physical energy supplies, and the exact remaining gap

At finite width, smooth gradient flow in the contract's metric satisfies

\[
 L'(t)=-\|\dot\theta(t)\|_{\rm metric}^2,\qquad
 \int_0^T\|\dot\theta\|_{\rm metric}^2\,dt\le L(0),
 \quad\|\theta(t)-\theta(0)\|_{\rm metric}
                \le\sqrt{tL(0)}.
\tag{21}
\]

The first identity follows by differentiating \(L\) and substituting
\(\dot\theta=-\nabla L\); the other two follow by integration and
Cauchy–Schwarz. On a finite maximal interval, (21) also makes the
trajectory Cauchy at its endpoint; the finite-dimensional smooth field
can be restarted there. Hence finite gradient flow exists on every
finite horizon. This elementary fact is not the population conclusion.

For bounded candidate (1), loss decrease additionally gives the
coordinatewise estimate

\[
 |\dot W^{(4)}_i|
 \le2\sqrt2(|r_1|+|r_2|)\le4\sqrt{L(0)},\qquad
 |W^{(4)}_i(t)|\le |W^{(4)}_i(0)|+4t\sqrt{L(0)}.
\tag{22}
\]

This bound uses the actual residuals and actual physical time. Together
with bounded activations and bounded operator increments from (21), it
provides compact-horizon primal control. It does not provide the required
strong stability of (16). Bounded \(L^2\) norms of \(q^{(2)}\) and
\(dZ^{(2)}\) do not bound their product in \(L^2\). For instance, on
an event of probability \(\varepsilon\), take
\(q=dZ=\varepsilon^{-1/2}\); both norms are one, whereas
\(\|q\,dZ\|_2=\varepsilon^{-1/2}\). This illustration only diagnoses
the norm inequality, not the law of the actual trajectory.

The old one-sample proof overcomes this difficulty by a quantitative
response/tail estimate on a bounded feature-clock interval. For (1),
no argument has been established that closes the coupled response system
on every finite physical horizon. Equations (10)–(11) govern only a trace
of the direct top block, while (16)–(20) expose the still-uncontrolled
middle product. Initialization kernel positivity (4) is not a later
contrast-kernel lower bound and cannot be used to confine the clock.

The root's new reduction sharpens the last point. Candidate (1) is
bounded and Lipschitz with both constants \(\sqrt2\), so Section 6 of
`EXACT_TWO_SAMPLE_REDUCTION.md` applies directly: for opposite labels,
the normalized feature-flow predictor \(g_{\rm mode}=(f_1-f_2)/2\)
satisfies \(|g_{\rm mode}(s)|\le C_S\sqrt{1-\rho}\) on every fixed
bounded-primal feature interval, with angle-independent initial norm
bounds. There can be no angle-uniform short-feature-time fitting proof
for this activation. Consistently, (4) gives its initial normalized
contrast readout kernel

\[
 \tfrac14\mathbb E(H^{(3)}_{1,0}-H^{(3)}_{2,0})^2
       =\tfrac12(1-c_3)\sim\tfrac12(1-\rho)
                      \quad(\rho\uparrow1),
\tag{23}
\]

where the ratio follows by applying
\((1-e^{-x})/x\to1\) successively in (4). No activation parameter is
being sent to a linear limit here. The root obstruction does not rule
out a proof with constants depending on \(\rho\), which the contract
allows. Equations (19a) and (23) explain why neither a scalar residual
mode nor a fixed harmonic amplitude repairs the missing global response
estimate by itself.

## 7. Claim ledger and route recommendation

| Claim | Status and exact scope |
|---|---|
| One fixed smooth, bounded, nonlinear, non-even/non-odd candidate | Proved by (1)–(2); no limiting scale |
| Both label modes present at Gaussian initialization for all \(\rho<1\) | Proved by (3)–(5), including \(\rho=-1\) |
| Strict hidden distributional nonlinearity at initialization | Proved by (6) |
| Curvature converts to a readout-energy derivative | Exact identity (9); (10)–(11) require equal current input-feature norms |
| Classification of readout-only identity (12) | Proved within its stated universal scalar ansatz |
| Trace cancellation bounds every sensitivity direction | Falsified by (13)–(15) |
| Harmonic curvature has a sign-definite initial middle feedback coefficient | Falsified by (17)–(20) |
| Scalar label-mode summation cancels the initial middle Gaussian curvature innovation | Falsified by positive-definite covariance and (19a) |
| Harmonic activation allows one angle-uniform short fitting interval | Excluded by the root's Section 6; consistent with (23) |
| Compact-horizon finite GF existence and energy | Proved by (21)–(22) |
| Population well-posedness, reached-state restart, and full GF/GD/width convergence | Open |
| Strict nonlinearity at every finite time and all-hidden-layer feature learning | Open beyond the initialization facts above |

**Recommendation:** retain (1) as an unresolved witness, but close the
specific “harmonic scalar energy/trace implies global response stability”
argument. No alternative activation theorem has been proved. The saddle
and initial Gaussian coefficient are obstructions to that argument, not
counterexamples to the target or to this witness from prescribed roots.

**Next analytic falsifier:** any proposed replacement energy should first
be differentiated against the middle term (16), retaining the joint
Gaussian innovation (17). It must either cancel the product (19) against
specified coupled variations or control it by a proved trajectory law;
a readout-only endpoint energy, a pointwise curvature sign, and the
label-mode summation (19a) do not supply that control. A candidate energy
claimed to be globally dissipative on all states
must also survive (13)–(15); a claim restricted to reached states must
prove that restriction rather than assume it. Constructing and bounding
such a coupled energy remains the decisive open step for this route.
