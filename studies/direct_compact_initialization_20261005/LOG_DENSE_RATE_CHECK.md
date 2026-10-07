# Independent check of the logarithmic dense comparison

2026-10-06. Scoped reconstruction of
`ROOT_WIDTH_CONCENTRATION_ROUTE.md`, final checked SHA-256
`4b96d88be6ac85f932ba8c30d63ddd7f513074277965d87edb80142768b4760e`.
The complete initially assigned version had SHA-256
`f22e02a57bbef9525148e5bded6c75649aae5a2f20a4db037941057a1cf4570f`.
The sole intervening change reported by the author was the mechanical
repair `I,qquad` to `I,\qquad` in (5); the corrected expression and
final hash were checked.

**Conclusion.** The deterministic comparison (13) and its conditional
finite-confidence consequence (17) follow from the stated hypotheses.
For fixed admissible data and fixed nonzero labels, (17) is
\(O_{\mathrm{data},\delta}(\log(en)/\sqrt n)\), uniformly over
physical time, sphere queries, and fitted endpoints. The strict
\(C_{\mathrm{data},\delta}/\sqrt n\) comparison is not proved.
The sufficient criterion (18)–(19) is valid, and the note correctly
identifies its global extension and joint-moment requirements as open.
No substantive defect was found in this scoped reconstruction.

This is conditional verification of the new argument, not an independent
reproof of the inherited Gaussian source theorem or a promotion review.
No experiments or Git operations were performed. The required
`solve-math-rigorously` skill and `docs/notation.qmd` were read. The
canonical-notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`
returned permission denied; the assigned book-notation fallback was used.

## 1. Checked inputs and exact imported hypotheses

The candidate was read completely. The dependency checks used complete
relevant units of the authorized integrated study:

- `GENERAL_DENSE_COMPARISON.md`, §§1–2;
- `DENSE_SAMPLE_EXPONENT_REFINEMENT.md`, §§1–2 and §7;
- `RESULT.md`, “One common label allowance,” “One width and confidence
  convention,” “Dense model, scope, and numerical certificates,”
  “Quantitative initialization and all-time dense fitting,” and the
  complete “Explicit source recurrences, budget removal and analytic
  domain” unit;
- `UNBOUNDED_COMPRESSOR_BRIDGE.md`, complete §12, authorized separately
  during this check.

Only their fitting, source-event, modulus, and endpoint inputs are imported.
No prior review verdict is used as proof evidence.

Here \(L=2\), both activations are \(\tanh\), the normalized inputs
\(v_a=x_a/\sqrt d\) are orthonormal, and initialization and mobilities
are exactly those of the candidate. In particular \(w(0)=0\).
If
\[
q_1=\mathbb E\tanh^2 Z,\qquad
q_2=\mathbb E\tanh^2(\sqrt{q_1}Z),\qquad Z\sim N(0,1),
\]
the imported covariance recursion gives \(Q^{(1)}=q_1I_m\),
\(Q^{(2)}=q_2I_m\), and \(\gamma=q_2>0\): centered odd features
of independent Gaussian coordinates have zero cross covariance.
Write \(\lambda=\gamma/m\), as in the imported fitting statement.
Tanh is holomorphic with bounded derivative on every fixed strip
\(|\operatorname{Im}z|<a<\pi/2\), so it satisfies the source
activation class.

The imported real-fitting restriction is exactly
\[
0<Y\le\frac{\lambda}{8H_D\sqrt{F_D}},
\]
where \(H_D,F_D\) are the deterministic activation/depth coefficients
defined in the checked fitting unit. The imported source restriction is
\[
S:=16Y/\lambda\le S_*^{\rm src},
\]
where \(S_*^{\rm src}\) is the positive recurrence allowance (S.10)
in the checked source unit. The existing common allowance implies both;
the already stated sufficient specialization is
\(0<Y\le(\gamma/m)\beta^{-30L}\), here \(L=2\), with
\(\beta\) defined in the authorized dense source. No stronger label
restriction is needed for the new deterministic estimate or bridge §12.

At each sufficiently large individual width, the intersection of the
imported fitting and source events has probability tending to one. On
that event the following constants are independent of width and time:
\[
\|W(t)\|_{\rm op}<9,\quad
\|A(t)\|_{\rm op}/\sqrt n<9,\quad
K(t)/m\succeq(\lambda/4)I_m,\quad
\rho(t)\le Ye^{-\lambda t/2}.
\]
Thus the candidate can take \(\kappa=\lambda/4\).
The same fitting input supplies parameter convergence, uniform endpoint
tails, and the sphere/time moduli used below. The source supplies
\(\max_{a,i,t}|k_{a,i}(t)|\le CY\sqrt{\log(en)}\).

The extra fourth-moment input follows directly from bridge (40), including
its stated all-real-time extension. With its constants \(\eta_2>0\)
and \(\mathcal B_2\), let
\(K_{a,i}=\sup_{t\ge0}|k_{a,i}(t)|\). Its running amplitude
dominates \(K_{a,i}/S\), and
\[
x^4\le \left(\frac{2}{e\eta_2}\right)^2e^{\eta_2x^2}
\]
gives
\[
\left(\frac1n\sum_iK_{a,i}^4\right)^{1/4}
\le S\sqrt{\frac{2}{e\eta_2}}\,\mathcal B_2^{1/4}
=C_4Y.
\]
This controls running training carriers. It asserts no corresponding
moment bound for a transported prediction response.

The source probability theorem and its eventual stochastic width are
inherited, not newly certified here. In particular the conclusion is
for each sufficiently large width, not a single event over infinitely
many independent widths.

## 2. Deterministic reconstruction

The loss \(m^{-1}\sum_a r_a^2\), mobilities \((n,1,n)\), and
\(v_a^Tv_b=\delta_{ab}\) give (1) with exactly its factors of
\(m\) and \(n\). Multiplying its first equation by
\(Q'(u)=\cosh^2u=1/\phi'(u)\) gives
\(\dot\eta_a=-(2/m)r_ak_a\). Orthogonality is essential: otherwise
the equation for each \(u_a\) contains other training gates.

For \(T=Q^{-1}(Q(u_0)+\eta)\), differentiation gives
\[
\partial_\eta T=\phi'(T),\qquad
\partial_{u_0}T=\frac{\phi'(T)}{\phi'(u_0)}.
\]
If \(L(q)=1/\phi'(Q^{-1}(q))\), then
\(L'(q)=2\tanh(Q^{-1}(q))\), so \(|L'|\le2\) and \(L\ge1\).
Consequently
\[
\frac{\phi'(T)}{\phi'(u_0)}
=\frac{L(Q(u_0))}{L(Q(u_0)+\eta)}\le1+2|\eta|.
\]
The candidate's feature and squared-gate derivative bounds follow from
\(|\phi'|\le1\), \(|\phi''|\le2\). Comparing two endpoints
first at fixed \(\eta\), then at fixed \(u_0\), is valid even
though interpolated initializations need not be good trajectories:
the scalar bounds hold for every intermediate scalar value of \(u_0\).

Retain the candidate's \(E_A,D,D_w\). The preceding calculation gives
(6). Forward subtraction uses \(\|h_a\|_2/\sqrt n\le1\) and the
operator cap. Backward subtraction uses
\[
\Delta d_a=\Delta w\odot\phi'(z_a)
+w'\odot\bigl(\phi'(z_a)-\phi'(z'_a)\bigr),
\quad
\Delta k_a=(\Delta W)^Td_a+(W')^T\Delta d_a.
\]
Here \(w'\) denotes the second trajectory, not a derivative. These
identities prove (7) using only \(\|w'\|_\infty\le C_wY\), with
no multiplication of a carrier by a state difference.

The three parameter blocks give exactly the Gram formula (8). For its
first-layer diagonal part, the only higher-moment step is
\[
\frac1n\sum_i
 |\Delta(\phi'(u_i)^2)|k_i^2
\le
\frac{\|\Delta(\phi'(u)^2)\|_2}{\sqrt n}
\left(\frac1n\sum_i k_i^4\right)^{1/2}.
\]
The remaining carrier-square difference obeys
\[
\frac1n\sum_i|k_i^2-(k'_i)^2|
\le\frac{\|k-k'\|_2}{\sqrt n}
     \frac{\|k+k'\|_2}{\sqrt n}.
\]
Together with (6)–(7), these prove (9); the other Gram terms use only
RMS feature/carrier bounds. Neither step asserts the invalid vector
estimate that an \(L^4\) carrier times an \(L^2\) state difference
is controlled in \(L^2\).

Subtracting the transformed state equations proves (10), with
\(D(0)=\|\Delta W(0)\|_F\), because both \(\eta(0)\) vanish.
Both initial readouts vanish and both residuals equal \(-y\).
Writing \(B=K/m\), the residual difference satisfies
\[
\frac{d}{dt}\Delta r=-2B\Delta r-2(B-B')r'.
\]
Since \(B\succeq\kappa I\), its homogeneous propagator has norm
at most \(e^{-2\kappa(t-s)}\). Integrating this bound over the
outer time variable yields (11), with the integral of the exponential
bounded by \(1/(2\kappa)\). No derivative of the gap or timewise
commutation of Gram matrices is required.

For \(R=E_A+D+D_w/Y\), substitution into (10) gives
\[
R(t)\le E_A+D(0)+
\frac{C(1+\kappa^{-1})}{Y}
\int_0^t Ye^{-2\kappa s}R(s)\,ds.
\]
The integral of the scalar coefficient is independent of \(n,H,t\).
This proves (12), retaining all dependence on \(H\) in \(E_A\).

Finally write a unit query as
\(v=v_\perp+\sum_a(v_a^Tv)v_a\). On the orthogonal complement,
\(A(t)v_\perp=A(0)v_\perp\); on the training span use (6).
Cauchy–Schwarz in the fixed sample index controls the sum. Forward
subtraction gives
\(|\Delta f|\le C[D_w+Y(E_A+D)]\) uniformly in that query.
Equation (12) therefore proves (13). Existing fitted limits inherit this
uniform bound. The associated fixed-source linearized propagator claim
also follows: an initial residual variation adds at most
\(\|\delta r(0)\|_2/(2\kappa\sqrt m)\) to (11), and its
forward derivative is bounded by \(CY\) times the stated state norm.

## 3. Finite confidence and the full topology

Bounded top features give
\(\|w(t)\|_\infty\le2\int_0^\infty\rho(s)\,ds\le CY\).
Using the imported running carrier maximum in (2), and
\(|r_a|\le\sqrt m\rho\), gives
\(H\le CY^2\sqrt{\log(en)}\). The standard root
\(G=(A(0),\sqrt nW(0))\) thus converts (13) into a pairwise
Lipschitz bound on the entire good set, with
\[
L_n\le\frac{CY}{\sqrt n}
       [1+CY^2\sqrt{\log(en)}].
\]
The factor \(\sqrt n\) on the initialized mixer is essential and
is included correctly.

At each mesh point the scalar infimum extension is finite, agrees with
the good-set prediction, and is globally \(L_n\)-Lipschitz.
Truncating to \([-C_wY,C_wY]\) preserves these properties.
The rotation identity in (16) is valid: at every angle,
\(G_\theta\) and \(V_\theta\) are independent standard Gaussian
vectors, and conditional on \(G_\theta\), the directional derivative
has distribution \(\|\nabla F(G_\theta)\|_2N(0,1)\).
Minkowski and integration over \([0,\pi/2]\), followed by smooth
approximation, yield
\[
\|F(G)-F(G')\|_{L^p}\le C\sqrt p\,L_n.
\]
Taking \(p=\max\{2,\log(2N_n/\delta)\}\), Markov at
\(eC\sqrt pL_n\) gives failure at most \(\delta/(2N_n)\).
The union over \(N_n\) mesh points therefore costs at most
\(\delta/2\). Constants absorb the harmless maximum with two.

The imported modulus in \(u=1-e^{-ct}\), with fixed \(c>0\),
including \(u=1\), is
\[
|f(t(u),v)-f(t(u'),v')|
\le CY(|u-u'|+\|v-v'\|_2).
\]
It holds on the fitting event, not merely pointwise in probability.
An \(n+1\) point time grid and a sphere \(1/n\)-net have total
cardinality at most \(N_n=(n+1)(1+2n)^d\), and add at most
\(CY/n\) to the two-copy comparison. No regularity of the scalar
extensions across mesh points is needed: off-grid control is applied
to the actual good trajectories.

Choose the width so that each copy's combined inherited event fails
with probability at most \(\delta/4\). The two bad-path events cost
at most \(\delta/2\), independently of the Gaussian mesh union.
This proves the displayed structure and \(1-\delta\) confidence of
(17). Constants are independent of width; the eventual stochastic
threshold remains unquantified. Fixed nonzero \(Y\) makes the product
of the two square-root logarithms of order \(\log(en)\).

## 4. Boundary of the strict-root criterion

For the globally defined smooth family in §4, set
\(H(t,v)=\partial_tF_n(t,v;G)-\partial_tF_n(t,v;G')\).
On a fixed cube, the line-segment averaging argument yields the stated
kernel \(|x-z|^{1-d}\). Its conjugate power is locally integrable
exactly when \(p>d\) (with constant kernel in dimension one), so
\(\|H(t,\cdot)\|_\infty\le C_{d,p}\|H(t,\cdot)\|_{W^{1,p}}\).
Applying (16) separately to the time derivative and its first query
derivatives, then Fubini and Minkowski, proves (19) from (18).
The common initial value zero justifies integration from time zero.
Physical fitted endpoints are covered whenever the family agrees with
the fitted physical paths on the asserted event.

The stated quantifiers are sufficient: one fixed \(p>\max(d,2)\),
one width-independent bound in (18), and one global extension family for
each sufficiently large width, with simultaneous path/query agreement
on an event of probability at least \(1-\delta/4\), combine with
Markov failure \(\delta/2\) and two exceptional events to give the
strict root rate. Those requirements are not consequences of (17).

In particular a bound restricted by an event indicator supplies neither
a global extension satisfying (18) nor the mixed products of source
factors and transported response coordinates. The example (22) correctly
shows that bounded separate counting moments and a global response norm
cannot establish that product estimate. It is a counterexample to that
inference, not to neural-network concentration. The candidate preserves
this distinction throughout its final claim boundary.
