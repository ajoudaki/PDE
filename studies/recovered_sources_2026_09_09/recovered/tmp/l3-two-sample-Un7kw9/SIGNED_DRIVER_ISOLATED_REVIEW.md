# Isolated adversarial audit of the signed-driver candidates

Date: 2026-09-05. Method: direct proof audit, without agents, numerical
experiments, symbolic-computation experiments, or external sources.

| Candidate | SHA-256 of audited file | Verdict and scope |
|---|---|---|
| `TANGENT_SIGNED_DRIVER_RESPONSE.md` (758 lines) | `36fa3bbad7df00a6916712e23fb132489c498abd73b2e8cb382ad1780c5e701b` | **PASS** — the stated global two-dimensional signed flow, uniform fixed-driver initial-state Jacobian and driver derivative, strict sufficient Gaussian moment condition, and conditional forcing/source algebra. |
| `FINITE_ANGLE_Q_CHANNEL_ROUTE.md` (163 lines) | `6480eec6072f6b043e90e65d7224967cccc4936e37cd34370abfab9b0dcd0ddd` | **PASS, partial scope** — global pure-q flow, common-coordinate radius, the derivative with respect to the initial common coordinate at fixed terminal contrast, its Gaussian moment bound, and the stated population affine/parity algebra. |

No mathematical failure was found in these completed claims. Candidate 2
does **not** establish a fixed-driver Jacobian bound. Neither verdict
certifies a coupled-network response theorem, a dynamical angle limit,
cutoff removal, or the full joint MF/GF/exact-GD theorem.

## Audit boundary

I read `/etc/codex/skills/solve-math-rigorously/SKILL.md` fully and applied
its requirement to check nontrivial steps, exceptional cases, quantifiers,
and theorem scope. Both candidates were read in full. The only research
dependencies inspected were:

- `CONTRACT.md`, for the raw input metric and normalizations;
- `TWO_SAMPLE_SOURCE_BASELINE.md`, especially lines 208–299, for the finite
  Gaussian source representation and its covariance convention;
- `SYMMETRY_RADIAL_CLOCK.md`, especially lines 187–228 and 627–685, for
  population involutions, operator intertwining, and affine updates.

No other research notes, reviews, history, or linked references were
opened. In particular, the references to other response routes inside
Candidate 1 were not followed. The finite-program representation and
population realization are used within their explicitly supplied scope;
their underlying external theorems are not independently re-audited here.
The candidates were not edited.

## Candidate 1 — PASS

### Global signed flow and the exceptional coordinate

The continuation argument at lines 93–132 works in both directions of
driver time. Since \(1\le a\le L=1+e\), the contrast is bounded on finite
driver intervals by \(|V_0|+L|r|\). Integrating \(|M_r|\le2e|V|\) gives
the stated quadratic finite-interval bound. A finite maximal endpoint
would therefore have a limiting state in a compact set, where the smooth
vector field admits continuation. Local smooth dependence on initial
state applies on the same containing sets. This proves the claimed global
\(C^1\) flow, without using the later uniform response estimate.

For a prescribed \(q\in L^1_{\mathrm{loc}}\), its integral \(r(t)\) is
absolutely continuous and has compact image on every compact physical
time interval. Composition with the \(C^1\) flow solves the equation
almost everywhere. The uniqueness inequality uses \(|q|\), so sign changes,
repeated reversals, and intervals on which \(q=0\) cause no problem.
An externally selected driver is held fixed in initial-state derivatives;
this does not assert uniqueness or differentiability of its selection rule.

For \(M_0\ne0\), the equation

\[
M_r=-\frac{2eV}{(1+M^2)^2}M
\]

has a nonvanishing exponential solution on every compact driver interval.
Thus sign preservation and use of the logarithmic invariant are valid.
Direct differentiation gives

\[
\Lambda'(M)=\frac{(1+M^2)(1+M^2+e)}{eM}=-\frac{2a(M)}{b(M)},
\]

and hence \((V^2+\Lambda(M))_r=0\), with no sign assumption on \(VM\)
or \(qV\). The contrast increases onto all of \(\mathbb R\), so every
orbit has exactly one point with \(V=0\).

Writing \(Y=v^2\), \(X=m^2\), the invariant yields

\[
X_Y=-\frac{2eX}{F(X)},\qquad
F(X)=(1+X)(1+X+e)\ge(1+X)^2\ge4X.
\]

Consequently \(-e/2\le X_Y\le0\) and

\[
\sup_r M(r)^2=m_c^2\le M_0^2+(e/2)V_0^2.
\]

The envelope \(|m(v)|\le |m_c|\exp[-ev^2/F(m_c^2)]\) follows by
integrating \((\log|m|)_Y=-e/F(m^2)\le-e/F(m_c^2)\). This also works
on the negative common-coordinate half-line.

At \(M_0=0\), the candidate correctly avoids the logarithm. The full
ambient initial-state Jacobian is

\[
\Psi_r(0,V_0)=(0,V_0+Lr),\qquad
D\Psi_r(0,V_0)=\operatorname{diag}
\left(e^{-2eV_0r-eLr^2},1\right).
\]

Both off-diagonal entries vanish because \(a'(0)=b(0)=0\). Completing
the square gives the exact maximal common-coordinate derivative

\[
\sup_r |M_{M_0}(r)|=e^{\gamma V_0^2},\qquad \gamma=e/L.
\]

This checks the exceptional point, arbitrary initial contrast, and both
signs of \(r\).

### Orbit derivatives, clock inversion, and every explicit constant

At fixed terminal contrast and \(M_0\ne0\), autonomous scalar variation
gives

\[
J=\frac{f(m)}{f(M_0)}
=\frac m{M_0}\frac{F(M_0^2)}{F(m^2)}>0,
\qquad f(m)=-\frac{em}{F(m^2)}.
\]

For \(Y\ge Y_0\), \(|m/M_0|\le1\), yielding \(J\le F(M_0^2)/L\).
For \(0\le Y\le Y_0\), \(f'(m)\ge-e/L\), giving \(J\le e^{\gamma Y_0}\)
by backward integration. Thus the stated \(J_*\) bounds both branches.
Differentiating the invariant also gives the correctly signed formulas

\[
m_{V_0}=-2V_0f(m),\qquad m_v=2vf(m).
\]

They require division by neither \(v\) nor \(V_0\).

The conversion to fixed \(r\) is essential and is supplied at lines
311–377. In the following identities, the derivatives inside the
integrals are still at fixed terminal contrast:

\[
V_{M_0}=a(m(V))\int_{V_0}^{V}\frac{a'(m)m_{M_0}}{a(m)^2}\,dv,
\]

\[
V_{V_0}=\frac{a(m(V))}{a(M_0)}
+a(m(V))\int_{V_0}^{V}\frac{a'(m)m_{V_0}}{a(m)^2}\,dv.
\]

In particular, the moving lower endpoint in the second formula has the
correct positive contribution after clock inversion. Signed integrals
handle \(V<V_0\). Their terminal derivative is \(1/a\ge1/L\), so there
is no vanishing clock denominator. Differentiation concerns finite
integrals; no unjustified differentiation of an improper integral occurs.

All constants in equations (19)–(31) check. With

\[
B=1+|M_0|+\sqrt e\,|V_0|,\quad K=2(e+2),\quad
I=\sqrt{\pi K/e},\quad j=1+K/L,
\]

the inequalities \(|m_c|\le B\) and

\[
F(m_c^2)\le(2B^2)((2+e)B^2)=KB^4
\]

give \(J_*\le jB^4e^{\gamma V_0^2}\). Gaussian integration of the orbit
envelope gives exactly the usable upper bounds

\[
\int |m|\,dv\le IB^3,\quad
\int m^2\,dv\le IB^4,\quad
\sup_v|vm(v)|\le IB^3.
\]

For the last bound the sharp envelope factor is
\(|m_c|\sqrt{F(m_c^2)/(2e\exp(1))}\), which is no larger than \(IB^3\).
Set, as in the candidate,

\[
h=2\gamma I,\quad k=2eLI,\quad d_*=2\sqrt e/L,\quad
\ell_*=L+4e^{3/2}I.
\]

Then \(|m_{V_0}|\le d_*B^2\), \(|m_v|\le hB^3\), and clock inversion
gives the following bounds on all four derivatives at fixed driver time:

| Entry | Verified bound |
|---|---|
| \(V_{M_0}\) | \(kjB^7e^{\gamma V_0^2}\) |
| \(V_{V_0}\) | \(\ell_*B^5\) |
| \(M_{M_0}\) | \((1+hk)jB^{10}e^{\gamma V_0^2}\) |
| \(M_{V_0}\) | \((d_*+h\ell_*)B^8\) |

For example, the integral part of \(V_{V_0}\) is bounded by

\[
4e\gamma L|V_0|\int m^2\,dv
\le4e^{3/2}IB^5,
\]

and \(M_{M_0}=m_{M_0}+m_vV_{M_0}\) accounts for the power \(B^{10}\).
The actual driver derivative satisfies

\[
\|\partial_r\Psi_r\|\le2e\sup|Vm(V)|+L\le(L+2eI)B^3.
\]

Summing the entry bounds and this vector bound proves the claimed
Euclidean operator-norm estimate with precisely

\[
C_e=(1+hk)j+kj+(d_*+h\ell_*)+\ell_*+L+2eI.
\]

Every coefficient is finite for every fixed \(e>0\). For \(M_0=0\),
the exact formulas give a norm sum at most \(e^{\gamma V_0^2}+1+L\),
and this same \(C_e>2+L\) suffices. No hidden dependence on driver,
terminal contrast, elapsed time, or angle enters this local theorem.

### Gaussian condition, source-dependent driver, and late injection

For a centered jointly Gaussian pair with \(v=\operatorname{Var}(V_0)>0\),
write \(M_0=\alpha V_0+Z\), with \(Z\) an independent Gaussian residual,
allowing zero variance. Conditioning bounds the polynomial prefactor by
\(C(1+|V_0|)^{10p}\). Its integral against

\[
\exp\left[\left(p\gamma-\frac1{2v}\right)V_0^2\right]
\]

is finite under the stated strict condition \(p\gamma v<1/2\), for
every \(p>0\). Degenerate covariance and \(v=0\) are handled correctly;
the latter leaves only Gaussian polynomial moments. Continuity in \(r\)
makes the supremum measurable by restriction to rational \(r\).

The strictness counterexample is decisive within the allowed class:
\(M_0=0\), \(V_0\sim N(0,v)\) gives gain exactly \(e^{\gamma V_0^2}\).
At \(p\gamma v=1/2\), its Gaussian density cancels the exponential and
the integral over \(\mathbb R\) diverges. This proves failure at equality
in general, not necessity of the threshold for every nonsingular law.
For \(e=1/10\), \(v=1\), \(p=4\), \(4/11<1/2\) is correct.

Equation (33) is the ordinary chain rule under the expressly assumed
differentiability into \(L^1\). Integration is a bounded linear map from
\(L^1([0,T])\) to continuous primitives, so differentiating that integral
is justified. The equation provides no estimate for the source derivative
of the externally selected \(q\).

For the reversal example, advancing from \((0,0)\) by \(R\) contracts
the common derivative by \(e^{-eLR^2}\). The return map is
\(\Psi_{-R}\) based at \((0,LR)\), whose common derivative is

\[
\exp[-2e(LR)(-R)-eL(-R)^2]=e^{eLR^2}.
\]

Their product is one. An independent common perturbation introduced at
the reached state lacks the preceding contraction. Thus the example
correctly rules out bounding arbitrary late common-channel injections by
the original initial-state constant. It does not contradict the theorem.

### Raw metric, normalized adjoints, sources, and uncontrolled forcing

The network identities are conditional algebra as expressly stated at
lines 501–506 and 638–642. They are exact in finite dimensions and on
population paths with the required differentiability and integrable
products. They assert no general differentiable gradient on an \(L^2\)
ball and no existence of the coupled path.

For the tangent activation map \((h,k)=(\phi(M),a(M)V)\), its adjoint
map is

\[
P=ap+bVq,\qquad Q=aq.
\]

Starting from \(p_3=0,q_3=C\), ordinary transposes yield (36), the block
gradients (37), and the explicit nonzero upper-curvature forcing (39).
Differentiating \(Ah_1,Ak_1,Bh_2,Bk_2\) gives every operator and
transport term in (40). No layer beyond the isolated bottom pure-q
channel is thereby reduced to the local ODE.

For positive separation, the exact coordinate Jacobian is

\[
D(h_\delta,k_\delta)=
\begin{pmatrix}a_\delta&\delta^2b_\delta\\b_\delta&a_\delta\end{pmatrix}.
\]

It follows that the incoming normalized adjoints are

\[
q^\delta=\widehat q_M,\qquad p^\delta=\widehat q_D/\delta,
\]

where sample averages and half-differences define the subscripts \(M,D\).
The outgoing preactivation adjoints are

\[
Q^\delta=\widehat\delta_M,\qquad
P^\delta=\widehat\delta_D/\delta.
\]

Thus \(q\) is the average incoming backward channel and \(p\) is its
normalized difference. These formulas agree with both matrix transpose
recursions. They give (42), including the factor \(\delta^2\).

To check the bottom metric directly, put
\(x_M=(x_1+x_2)/2\), \(x_D=(x_1-x_2)/2\). Their normalized squared
lengths are \(\mu^2\) and \(\delta^2\), and they are orthogonal.
Under the opposite-label feature update, with overall sign absorbed,

\[
M_s=\mu^2\widehat\delta_D,\qquad
V_s=\delta\widehat\delta_M,\qquad V=D/\delta.
\]

Consequently \(u=\delta s\) gives \(M_u=\mu^2P^\delta\), \(V_u=Q^\delta\),
exactly as claimed. The limiting metric coefficients tend to one.
This is a normalization calculation, not convergence of dynamics.

For the finite source representation, identify the candidate's block
\(\mathcal R_{kj}\) with the allowed baseline's backward coefficient
block \(D^{(\ell+1)}_{ka,jb}\). The baseline includes \(j\le k\), so
current-time responses are retained. Multiplication of the complete row
by \(T_\delta\), with forward reconstruction \(J_\delta\), gives
exactly \(T_\delta\mathcal R_{kj}J_\delta\); no causal term is lost.
The source covariance is the uncentered second-moment Gram of the
original transpose query inputs. In channel order \((q,p)\), its
transformation is the Gram of \((Q^\delta,P^\delta)\). This proves all
three identities (45), including the cross covariance, with no missing
metric coefficient or extra power of \(\delta\). Singular covariance
does not obstruct this linear algebra. This is a conditional finite
program identity, not an assertion that every uncut nonlinear program
already satisfies the representation's construction hypotheses.

For opposite-label exchange, original incoming backward fields transform
as \(\widehat q_a\mapsto-\widehat q_{\pi a}\). Their average is odd;
their normalized difference is even. Even parity does not imply zero
on the set where a different even field \(M\) is zero. Transpose mixing
in (39) supplies no factor \(M_1\) in \(p_1\).

Finally, direct differentiation of the forced equation gives, for
\(M\ne0\),

\[
\frac{d}{dt}[V^2+\Lambda(M)]
=\Lambda'(M)a(M)p
=\frac{(1+M^2+e)^2}{eM}p.
\]

The singular coefficient and possible crossings of zero are correctly
acknowledged. Locally integrable prescribed \(p,q\) still give finite
horizon state bounds, but neither (47) nor the local response theorem
controls the actual coupled forcing or its responses. The candidate's
stated limitation is mathematically necessary.

## Candidate 2 — PASS for the completed partial result

### Global flow and angle-uniform radius

Let \(0\le\delta\le1\), \(\mu^2=1-\delta^2\), with \(\delta=0\)
understood through the continuous formulas. Exact subtraction gives

\[
b=-\frac{2eMV}{(1+(M+\delta V)^2)(1+(M-\delta V)^2)}.
\]

The smooth extension also satisfies \(|b|\le2e|V|\). Together with
\(1\le a\le L\), this proves finite-interval continuation in both
directions, surjectivity of \(V(r)\), invariance of \(M=0\), and sign
preservation otherwise. Using \(V\) as the clock introduces no zero
denominator. The equation in \(Y=V^2\) extends through \(V=0\), and its
orbit reconstruction \(M=m(V^2)\) gives the same solution there.

Both displayed denominator identities are exact. In particular,

\[
F=(X-Z-1)^2+4X+e(1+X+Z)\ge4X,
\]

\[
F=(X-Z)^2+(2+e)(X+Z)+L\ge L(1+X).
\]

Thus one explicit choice for the unspecified positive lower-bound
constant \(c_e\) at line 50 is \(L\). The scalar equation gives

\[
-e\mu^2/2\le X_Y\le0,\qquad
\sup_r M(r)^2\le M_0^2+(e\mu^2/2)V_0^2.
\]

These estimates include \(\mu=0\), \(M_0=0\), either sign of initial
contrast, and arbitrary driver reversals.

### The lower bound for \(f_m\) covers every \(X,Z\ge0\)

Direct differentiation at fixed \(Y\), hence fixed \(Z\), gives

\[
f_m=e\mu^2\frac{-F+2XF_X}{F^2}.
\]

If \(F_X\ge0\), this is at least \(-e\mu^2/F\ge-e/L\).
If \(F_X<0\), set \(A=1+e/2\) and \(u=Z-X>A\). Then

\[
D=(u+1)(u+1+e)=u^2+2Au+L,\quad
F=D+4AX,\quad F-2XF_X=D+4uX.
\]

The candidate's expansion is exact:

\[
F^2-L(F-2XF_X)
=D(D-L)+(8AD-4Lu)X+16A^2X^2.
\]

Here \(D\ge L\), \(D\ge2Au\), and \(4A^2\ge L\). Therefore
\(2AD\ge4A^2u\ge Lu\), which makes the middle coefficient
nonnegative. Hence \((F-2XF_X)/F^2\le1/L\), proving
\(f_m\ge-e\mu^2/L\ge-e/L\) in the remaining region. No sign of
\(F_X\) or unbounded range of \(Z\) is omitted.

Since \(J'=f_mJ\), \(J(Y_0)=1\), positivity follows from its exponential
formula. Backward integration gives

\[
J(Y)\le e^{\gamma(Y_0-Y)}\le e^{\gamma V_0^2}
\quad(0\le Y\le Y_0).
\]

### Forward variation with a constant independent of angle

For \(\mu>0\) and \(M_0\ne0\), \(X\) is strictly decreasing on every
finite forward \(Y\) interval. The positive part satisfies

\[
(f_m)_+\le\frac{2e\mu^2X(F_X)_+}{F^2}.
\]

Substitution of \(-dX=(2e\mu^2X/F)dY\) therefore proves equation (8)
along the actual trajectory. It does not hold \(Z\) fixed along that
trajectory; only the definition of the partial derivative \(F_X\) does.

For every \(X,Z\ge0\), \(|X-Z|\le\sqrt F\) and \(F\ge L\), so

\[
|F_X|\le2\sqrt F+(2+e)
\le\left(2+\frac{2+e}{\sqrt L}\right)\sqrt F.
\]

Using \(F\ge L(1+X)\), set

\[
c=\frac2{\sqrt L}+\frac{2+e}{L},\qquad
C_e^{\mathrm{forward}}=2c=\frac4{\sqrt L}+\frac{2(2+e)}L.
\]

Then

\[
\log J(Y)\le\int_{Y_0}^Y(f_m)_+\,dY
\le c\int_{X(Y)}^{X_0}\frac{dX}{\sqrt{1+X}}
\le C_e^{\mathrm{forward}}(\sqrt{1+M_0^2}-1)
\le C_e^{\mathrm{forward}}|M_0|.
\]

This supplies an explicit constant for equations (9)–(10), independent
of \(\delta\), \(V_0\), terminal \(Y\), and the trajectory \(Z(Y)\).
It does not require \(X(Y)\to0\), which generally need not hold at
positive separation. At \(\mu=0\), \(J=1\). At \(M_0=0\),

\[
J(Y)=\exp\left[-e\mu^2\int_{Y_0}^Y
\frac{ds}{(1+\delta^2s)(1+\delta^2s+e)}\right],
\]

which directly satisfies both the forward and backward bounds.

The Gaussian conclusion is sufficient as stated. A Gaussian \(M_0\)
has every linear-exponential moment; a Gaussian \(V_0\) has the required
quadratic-exponential moment under \(p\gamma\operatorname{Var}(V_0)<1/2\).
The inequality \((x+y)^p\le\max(1,2^{p-1})(x^p+y^p)\) shows that
correlation causes no additional restriction for the sum in (10).
This certifies only \(\partial m/\partial M_0\) at fixed terminal
contrast, not the entire initial-state Jacobian.

### Forcing, affine parity, and the explicitly unfinished step

The same normalized metric and adjoint calculation checked above gives
exactly

\[
M_u=\mu^2(ap+bq),\qquad V_u=aq+\delta^2bp.
\]

Thus the autonomous two-coordinate equation retains only the \(q\)
vector field. Its local response bound supplies no estimate for the
independent \(p\) forcing or trained higher-operator terms.

The affine freezing observation at lines 153–163 is valid on the
constructed symmetric population realization supplied by the permitted
dependency. Its unitary involutions make \(C,D_1,D_2,D_3\) odd and
\(1+M_\ell\) even. Intertwining makes \(B^*C\) odd. Therefore

\[
A'=B^*C\otimes D_1,\qquad B'=C\otimes D_2
\]

annihilate every even input by even–odd orthogonality. Since \(M_1'=0\),

\[
M_2'=A'(1+M_1)+AM_1'=0,\qquad
M_3'=B'(1+M_2)+BM_2'=0.
\]

All three affine common preactivation fields are thus frozen on that
population path. This is not a pointwise orthogonality assertion about
an arbitrary finite-width realization.

For nonlinear feature updates in the unnormalized feature clock, writing
sample averages and half-differences gives

\[
\tfrac12(\widehat\delta_1\otimes H_1-
\widehat\delta_2\otimes H_2)
=\widehat\delta_M\otimes H_D+
\widehat\delta_D\otimes H_M.
\]

Under opposite-label exchange, the first summand acts in the odd sector
and the second in the even sector, as claimed. Population parity
justifies this statement without imposing independent finite neuron pairs.

Lines 119–136 explicitly leave the fixed-driver clock proof unfinished.
The displayed clock has positive terminal derivative \(1/a\), but a
uniform fixed-driver result still requires the parameter-integral bounds,
initial-time derivatives, and both terminal-coordinate chain rules. This
audit does not supply or certify those missing steps. The proposed
decomposition is a research route and is excluded from the PASS verdict
as a completed response estimate. Its incompleteness is correctly
disclosed and is not a failure of the completed partial claims.

## Disposition

Candidate 1: **PASS** at the recorded hash, within its local theorem and
conditional algebraic scope. Candidate 2: **PASS** at the recorded hash
for its completed partial claims; its fixed-driver Jacobian remains
**INCOMPLETE / NOT CERTIFIED**. No candidate revision is required by a
failure found in this audit. No full-network theorem is established by
either verdict.
