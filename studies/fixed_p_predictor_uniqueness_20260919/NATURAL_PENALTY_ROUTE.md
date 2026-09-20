# Ordinary physical gradients with fixed nullspace penalties

2026-09-19. Independently frozen candidate; internally checked theorem, not an
independent review or promoted result. This scoped author read only the complete
MODEL_AND_GEOMETRY.md and CANONICAL_FEATURES.md as scientific inputs, plus the
required research and rigorous-mathematics skills and their process references.
No other route, study, experiment, maintained source, or external scientific
source was consulted. Only this file is owned by this assignment; no Git-index
operations were performed.

Input SHA-256 values:

- MODEL_AND_GEOMETRY.md:
  d3ed7af3baadbb55e190e2423f0751b11da5ba24ef0c8fcc5c47f627ef57ff89.
- CANONICAL_FEATURES.md:
  5eab1371afaca04719bcd78a88c586f33042a008a28bbf1f3a07f0a0f6075b91.

## Frozen candidates and precise outcome

Write the physical state as \(S=(h,c)\), with \(h=(w,M)\), and use precisely the
Hilbert norms, weighted data operator \(A_h\), labels \(Y\), and loss

\[
 e=A_hc-Y,\qquad L=|e|^2,\qquad |Y|=1
\]

from the input model. Put \(A_0=A_{h_0}\), \(K_0=A_0A_0^*\),

\[
 \sigma=\lambda_{\min}(K_0)>0,\quad
 Q_0=A_0^*K_0^{-1}A_0,\quad P_0=I-Q_0.
\]

The canonical-feature input proves \(\sigma>0\) for every finite compatible
circle dataset after merging equal/antipodal constraints. Since \(\|A_0\|\le1\),
\(0<\sigma\le1\). No uniform lower bound over all datasets is asserted.

**Candidate A, fixed terminal geometry:**

\[
 V(h,c)=L(h,c)+\frac\rho2\|h-h_0\|^2+\|P_0c\|^2.
 \tag{A}
\]

For the explicit data-dependent \(\rho\) below, its literal physical gradient
flow, with arbitrary-amplitude bounded regular noise tangent to \(\nabla V\),
exists globally from \((h_0,0)\), has exponentially decaying loss, and converges
to the unique zero

\[
 (h_0,c_0^*),\qquad c_0^*=A_0^*K_0^{-1}Y.
\]

It needs only the fixed initial projection \(P_0\), current ordinary loss
gradients, and the quadratic hidden penalty. It uses no current inverse in the
flow and no feature transport. Its limiting predictor is exactly the selected
initial-kernel predictor. Transient hidden movement does not make its limiting
geometry learned.

**Candidate B, learned terminal geometry:** for a fixed \(\varepsilon>0\),

\[
 U(h,c)=L(h,c)+\frac\rho2\|h-h_0\|^2+\|P_0c\|^2
             +\varepsilon J(h),\qquad
 J(h)=\frac12Y^TK_h^{-1}Y.
 \tag{B}
\]

For the same construction of a sufficiently large \(\rho\), ordinary physical
gradient flow with noise tangent to \(\nabla U\) has a unique noise-independent
interpolating limit. The hidden limit uniquely minimizes

\[
 F(h)=\frac\rho2\|h-h_0\|^2+\varepsilon J(h)
\]

in the certified neighborhood. It differs from \(h_0\) exactly when
\(\nabla J(h_0)\ne0\), a condition proved below for every one-representative
dataset. This changes the actual data feature geometry. Candidate B retains a
current finite matrix inverse to evaluate \(J\) and its gradient, but still has
no moving-feature velocity, inverse transport, or auxiliary moving coordinates.
Its terminal readout lies in the fixed initial span; it need not be the
minimum-norm readout in the final current feature space.

The two candidates were specified before comparison with other routes. The
proof below treats A as the case \(\varepsilon=0\) of B. These are deliberately
changed optimizers. They make no claim about the unmodified loss gradient flow.

## 1. Explicit constants and certified domain

Use the constants from the model input:

\[
 a_1=4B_1B_2,\qquad a_2=8B_1B_2,\qquad a_3=2a_1^2+a_2,
\]

and let

\[
 R=\min\{1/2,\sigma/(8a_1)\},\qquad
 G_J=4a_1/\sigma^2,\qquad
 C_J=32a_1^2/\sigma^3+4(a_3+a_1^2)/\sigma^2.
\]

On \(\|h-h_0\|\le2R\), the input proves

\[
 K_h\succeq\sigma I/2,\quad
 \|\nabla J(h)\|\le G_J,\quad
 \operatorname{Lip}(\nabla J)\le C_J.
 \tag{1}
\]

Thus \(J\) is defined on a neighborhood of the closed hidden ball used below;
its existence along a trajectory is not assumed. All the feature estimates
used below hold on \(\|h-h_0\|\le1\):

\[
 \|A_h\|\le1,\quad \|DA_h\|\le a_1,\quad
 \operatorname{Lip}(DA)\le a_3.
 \tag{2}
\]

For any fixed \(\varepsilon\ge0\), set

\[
 W=1+\varepsilon J(h_0),\qquad
 C=1+\sqrt W+\frac{2(1+2\sqrt W)}{\sqrt\sigma},\qquad E=C+1,
 \tag{3}
\]

and choose, for example,

\[
\begin{split}
 \rho={}&1+\frac{8W}{R^2}+\frac{2\varepsilon G_J}{R}
       +\varepsilon C_J+2a_1^2 C^2+2Ea_3C
       +\frac{32E^2a_1^2}{\sigma},\\
 \mu={}&\sigma/8.
\end{split}
 \tag{4}
\]

Every quantity is computed from the finite dataset, canonical initialization,
and the declared \(\varepsilon\). None uses a future trajectory or endpoint.
These are sufficient, intentionally conservative constants. In particular they
can deteriorate severely as nearby data points make \(\sigma\) small.

Use the open convex physical-state domain

\[
 \Omega=\{(h,c):\|h-h_0\|<R,\ \|c\|<C\}.
 \tag{5}
\]

Two elementary consequences of (2) control readouts on this entire domain.
First, \(Q_0\) is the orthogonal projection onto the \(m\)-dimensional space
\(\operatorname{ran}A_0^*\), and

\[
 |A_0q|\ge\sqrt\sigma\|q\|\quad(q\in\operatorname{ran}Q_0).
\]

For completeness, \(E_0=A_0^*K_0^{-1/2}\) is an isometry from
\(\mathbb R^m\) onto that space, and \(A_0E_0=K_0^{1/2}\), which proves the
inequality and the dimension statement. Also

\[
 \|A_h-A_0\|\le a_1R\le\sigma/8\le\sqrt\sigma/2.
\]

Consequently

\[
 T_h:=A_h|_{\operatorname{ran}Q_0}:
       \operatorname{ran}Q_0\longrightarrow\mathbb R^m
 \quad\hbox{is invertible},\qquad \|T_h^{-1}\|\le2/\sqrt\sigma.
 \tag{6}
\]

The lower bound proves injectivity; equal finite dimensions prove surjectivity.
Second, for every readout variation \(d\), the inequality
\(|x+y|^2\ge|x|^2/2-|y|^2\) gives

\[
\begin{split}
 |A_hd|^2+2\|P_0d\|^2
 &\ge\frac\sigma2\|Q_0d\|^2+2\|P_0d\|^2
            -a_1^2R^2\|d\|^2\\
 &\ge\frac\sigma4\|d\|^2.
\end{split}
 \tag{7}
\]

Indeed \(a_1^2R^2\le\sigma/4\) and \(\sigma\le1\), so the two orthogonal
components have at least the displayed coefficient.

## 2. Strong convexity on the entire convex domain

Let a segment in \(\Omega\) have constant direction \((v,d)\). Along it,

\[
 e'=DA_h[v]c+A_hd.
\]

The regularity in (2) implies that this derivative is Lipschitz along the
segment, with directional derivative bound

\[
 |e''|\le a_3C\|v\|^2+2a_1\|v\|\|d\|
 \quad\hbox{for almost every segment parameter}.
 \tag{8}
\]

This uses only one-dimensional differentiation of a Lipschitz
\(\mathbb R^m\)-valued function. For example, subtract
\(DA_h[v]c+A_hd\) at two segment points, use the Lipschitz estimate for \(DA\),
and divide by their parameter difference. It does not posit a twice-Fréchet
differentiable \(L^2\) Nemytskii map.

Throughout \(\Omega\), \(|e|\le C+1=E\). Using (8) and
\(2|x+y|^2\ge|x|^2-2|y|^2\), the second directional derivative of \(L\) obeys

\[
 L''\ge |A_hd|^2-2a_1^2C^2\|v\|^2
               -2Ea_3C\|v\|^2-4Ea_1\|v\|\|d\|.
 \tag{9}
\]

The fixed projection penalty contributes \(2\|P_0d\|^2\). The hidden quadratic
contributes \(\rho\|v\|^2\). Finally the Lipschitz gradient bound for \(J\)
gives \(J''\ge-C_J\|v\|^2\) almost everywhere on the segment. From (7) and

\[
 4Ea_1\|v\|\|d\|\le\frac\sigma8\|d\|^2
                      +\frac{32E^2a_1^2}{\sigma}\|v\|^2,
\]

we obtain

\[
\begin{split}
 U''\ge{}&
 \left[\rho-\varepsilon C_J-2a_1^2C^2-2Ea_3C
              -\frac{32E^2a_1^2}{\sigma}\right]\|v\|^2
             +\frac\sigma8\|d\|^2\\
 \ge{}&\mu(\|v\|^2+\|d\|^2).
\end{split}
 \tag{10}
\]

The scalar function on each segment is \(C^{1,1}\). Integrating (10) twice
therefore proves, for any \(S,S'\in\Omega\),

\[
 U(S')\ge U(S)+\langle\nabla U(S),S'-S\rangle
                         +\frac\mu2\|S'-S\|^2.
 \tag{11}
\]

Thus this is strong convexity on a convex domain containing every trajectory
and its endpoint, not an unsupported claim that a nonlinear sublevel set is
convex. The objective need not be convex outside this domain.

For explicit local well-posedness bounds, put

\[
 D_1=a_1C+1,\qquad
 L_U=2D_1^2+2E(a_3C+2a_1)+\rho+2+\varepsilon C_J.
 \tag{12}
\]

The residual map has derivative norm at most \(D_1\) and derivative Lipschitz
constant at most \(a_3C+2a_1\). Subtracting the two factors in
\(\nabla L=2(De)^*e\) proves that \(\nabla U\) is \(L_U\)-Lipschitz on
\(\Omega\). Its norm is also bounded there by

\[
 G_U=2a_1CE+\rho R+\varepsilon G_J+2E+2C.
 \tag{13}
\]

## 3. The unique interpolating minimizer is constructed independently of flow

On the closed hidden ball of radius \(R/2\), consider

\[
 \mathcal T(h)=h_0-(\varepsilon/\rho)\nabla J(h).
\]

Equations (1) and (4) show that its image has distance strictly less than
\(R/2\) from \(h_0\), and that its Lipschitz constant is
\(\varepsilon C_J/\rho<1\). Iterating \(\mathcal T\) is Cauchy by the geometric
series estimate for successive differences. Completeness of the closed Hilbert
ball gives a limit \(h_\dagger\), and continuity makes it a fixed point. The
same Lipschitz inequality proves uniqueness. Hence

\[
 \rho(h_\dagger-h_0)+\varepsilon\nabla J(h_\dagger)=0,
 \qquad \|h_\dagger-h_0\|<R/2.
 \tag{14}
\]

The gradient of \(F(h)=\rho\|h-h_0\|^2/2+\varepsilon J(h)\) is strongly
monotone with constant \(\rho-\varepsilon C_J>0\), by integrating the
Lipschitz-gradient lower bound along a segment. Thus (14) gives the unique
minimizer of \(F\) throughout the hidden ball of radius \(R\).

Define

\[
 c_\dagger=T_{h_\dagger}^{-1}Y\in\operatorname{ran}Q_0.
 \tag{15}
\]

This inverse exists by (6), and \(\|c_\dagger\|\le2/\sqrt\sigma<C\).
Equivalently,

\[
 c_\dagger=A_0^*(A_{h_\dagger}A_0^*)^{-1}Y.
\]

This last formula is only an endpoint characterization; it is not evaluated
in the dynamics. At \(S_\dagger=(h_\dagger,c_\dagger)\), both \(e\) and
\(P_0c\) vanish. Therefore \(\nabla U(S_\dagger)=0\) and

\[
 U_*=U(S_\dagger)=F(h_\dagger),\qquad
 U(S)-U_*\ge L(S)+\|P_0c\|^2\quad(S\in\Omega).
 \tag{16}
\]

Equation (11) also gives

\[
 U(S)-U_*\ge\frac\mu2\|S-S_\dagger\|^2,\qquad
 \|\nabla U(S)\|^2\ge2\mu[U(S)-U_*].
 \tag{17}
\]

For the second inequality, apply (11) with \(S'=S_\dagger\) and maximize
\(\|\nabla U(S)\|r-\mu r^2/2\) over \(r\ge0\). No convergence theorem is
used to infer an endpoint; the unique endpoint has already been constructed.

When \(\varepsilon=0\), (14) gives \(h_\dagger=h_0\), and (15) becomes
\(c_\dagger=A_0^*K_0^{-1}Y\). In that case \(U_*=0\), and it is also the
unique zero of the globally defined nonnegative objective (A).

## 4. Literal physical gradient flow and a concrete bounded noise class

Use the physical Hilbert gradient and solve

\[
 \dot S=-\nabla U(S)+\xi(t,S),\qquad S(0)=(h_0,0).
 \tag{18}
\]

In components this is exactly

\[
\begin{split}
 \dot h={}&-2\{v\mapsto DA_h[v]c\}^*e
            -\rho(h-h_0)-\varepsilon\nabla J(h)+\xi_h,\\
 \dot c={}&-2A_h^*e-2P_0c+\xi_c.
\end{split}
 \tag{19}
\]

These are physical gradients, with the actual lower/middle transpose couplings
specified in the model input. There is no inverse preconditioner multiplying
the loss gradient and no cancellation of a moving-feature velocity.

Assume \(\xi\) is strongly measurable in time, uniformly Lipschitz in state on
each bounded time interval in \(\Omega\), bounded by some arbitrary finite
\(b\), and obeys

\[
 \langle\nabla U(S),\xi(t,S)\rangle=0.
 \tag{20}
\]

An explicit nontrivial such noise is available for every strongly measurable
physical-state-valued forcing \(z(t)\) with \(\|z(t)\|\le1\). With
\(g=\nabla U(S)\), set

\[
 \xi(t,S)=
 \begin{cases}
 \displaystyle\frac{b}{1+\|g\|}
       \left(\|g\|z(t)-\frac{\langle g,z(t)\rangle}{\|g\|}g\right),
              &g\ne0,\\[2mm]
 0,            &g=0.
 \end{cases}
 \tag{21}
\]

It is tangent, has norm at most \(b\|g\|/(1+\|g\|)\le b\), and is
Lipschitz in \(g\). One bound for the Lipschitz constant is \(5b\): the map
\(g\mapsto g\langle g,z\rangle/\|g\|\), extended by zero, is \(3\)-Lipschitz;
adding \(\|g\|z\) costs one more, and division by \(1+\|g\|\) costs at most
one more because the undivided tangent vector has norm at most \(\|g\|\).
For the \(3\)-Lipschitz bound, subtract \(g\langle g/\|g\|,z\rangle\)
and \(g'\langle g'/\|g'\|,z\rangle\), and use
\(\|g'\|\|g/\|g\|-g'/\|g'\|\|\le2\|g-g'\|\).
Consequently (21) has state Lipschitz constant at most \(5bL_U\).

This class permits arbitrary bounded time dependence and can act jointly in
all physical blocks. Random bounded forcing is also allowed, path by path.
It is not a claim about Brownian Itô noise, which has a different energy
formula. An unregularized projection of a fixed vector onto \(g^\perp\) is
singular at \(g=0\); merely declaring that projection at zero does not prove
well-posedness. Formula (21) removes this gap.

## 5. Confinement, global existence, and exponential convergence

Because the right side of (18) is measurable in time, bounded and Lipschitz in
state on \(\Omega\), local solutions follow directly by contracting the
integral equation on a sufficiently short interval in a closed state ball
inside \(\Omega\). The contraction constant is the time length times the state
Lipschitz bound. The same argument proves uniqueness and continuation as long
as the state stays in the domain. For general noise in the class above, use its
bounded-time-interval Lipschitz bound; for (21), use (12) and \(5bL_U\).

Every such solution is absolutely continuous and the \(C^1\) chain rule gives,
almost everywhere,

\[
 \frac{d}{dt}U(S(t))=-\|\nabla U(S(t))\|^2.
 \tag{22}
\]

Initially \(U(S(0))=W\). Thus, until any proposed exit from \(\Omega\),

\[
 \|h-h_0\|\le\sqrt{2W/\rho}<R/2,\qquad
 |e|\le\sqrt W,\qquad \|P_0c\|\le\sqrt W.
 \tag{23}
\]

The first bound uses \(J\ge0\). Applying (6) to \(Q_0c\), and using
\(\|A_h\|\le1\), gives

\[
\begin{split}
 \|Q_0c\|
 &\le\frac2{\sqrt\sigma}(|A_hc|+|A_hP_0c|)\\
 &\le\frac{2(1+2\sqrt W)}{\sqrt\sigma},\qquad
 \|c\|\le C-1.
\end{split}
 \tag{24}
\]

These are uniform strict interior margins in both coordinates. Equations
(13) and the noise bound give \(\|\dot S\|\le G_U+b\), so at any finite
putative maximal time the trajectory is Cauchy and has a Hilbert-space limit.
The margins place that limit inside \(\Omega\); local existence there extends
the solution. This contradicts finite maximal time. The solution is therefore
global, and (23)–(24) hold for all time. This proof uses completeness, not an
incorrect compactness assertion about infinite-dimensional bounded balls.

Combining (17) and (22), and integrating the scalar differential inequality,
gives

\[
\begin{split}
 U(S(t))-U_* &\le (W-U_*)e^{-2\mu t}\le W e^{-2\mu t},\\
 L(S(t)) &\le (W-U_*)e^{-2\mu t},\\
 \|S(t)-S_\dagger\| &\le
        \sqrt{\frac{2(W-U_*)}{\mu}}e^{-\mu t}.
\end{split}
 \tag{25}
\]

In particular, Candidate A satisfies the especially simple bound

\[
 L(t)\le e^{-\sigma t/4}.
 \tag{26}
\]

The endpoint is independent of the noise amplitude, path, and realization.
The rate guarantee is likewise independent of the noise; the coefficient
\(\sigma\), and hence the rate and penalty, remain dataset dependent.

The model's uniform circle-input derivative bound also gives

\[
 \sup_{|x|=\sqrt2}|f_{h,c}(x)-f_{h_\dagger,c_\dagger}(x)|
 \le\|c-c_\dagger\|+a_1\|c_\dagger\|\|h-h_\dagger\|
 \le\left(1+\frac{2a_1}{\sqrt\sigma}\right)\|S-S_\dagger\|.
 \tag{27}
\]

Here the first term uses \(\|H_h(x)\|_{L^2}\le1\), and the second integrates
the derivative of \(H_h(x)\) along the hidden segment. Thus the entire circle
predictor, not merely its training values, converges uniformly and
exponentially to one noise-independent function.

## 6. What learned geometry Candidate B actually retains

For \(\varepsilon>0\), equation (14) and uniqueness give the exact criterion

\[
 h_\dagger=h_0\quad\Longleftrightarrow\quad\nabla J(h_0)=0.
 \tag{28}
\]

If the gradient is nonzero, a sufficiently short step in its negative direction
strictly decreases \(F\). Since \(h_\dagger\) minimizes \(F\),

\[
 F(h_\dagger)<F(h_0)=\varepsilon J(h_0),\qquad
 J(h_\dagger)<J(h_0).
 \tag{29}
\]

The second strict inequality follows by subtracting the nonnegative quadratic
penalty. Hence \(Y^TK_{h_\dagger}^{-1}Y\) genuinely changes; the terminal
hidden motion is not merely a feature-preserving parameter symmetry.

The nonzero-gradient condition is not empty. For a dataset with one
representative direction, its merged weight is one and \(Y=\pm1\). Vary the
initial middle matrix along \(M(s)=(1+s)D\), holding \(w=g\). Write
\(z=b_2^TD a_{h_0}(x)\). Then

\[
 K(s)=E_2\tanh^2((1+s)z),\qquad
 K'(0)=2E_2[z\tanh z\,\operatorname{sech}^2z]>0.
\]

The integrand is positive whenever \(z\ne0\), and \(K(0)>0\) implies that this
event has positive probability. Boundedness of \(z\) justifies
differentiation. Consequently

\[
 \left.\frac d{ds}J(h(s))\right|_{s=0}
       =-\frac{K'(0)}{2K(0)^2}<0.
\]

Thus \(\nabla J(h_0)\ne0\), and Candidate B has nontrivial learned limiting
feature geometry for every such one-representative dataset. For general finite
datasets this report gives the exact criterion (28), not an unproved guarantee
that all datasets force hidden movement. The hidden penalty can make the
movement very small; no uniform lower movement bound or advantage in test error
is claimed.

The final readout deserves a separate qualification. It is the unique
interpolating readout in \(\operatorname{ran}Q_0\), which generally differs
from \(A_{h_\dagger}^*K_{h_\dagger}^{-1}Y\). The selector \(J\) measures the
best current-feature interpolation norm, while the fixed projector picks the
readout in the initial span. Both choices are explicit parts of Candidate B.
No claim that they coincide is needed in the proof.

## 7. Failures, exclusions, and claim ledger

- **Plain loss fitting is insufficient for predictor uniqueness.** The allowed
  canonical-feature input constructs distinct bounded readouts with the same
  finite labels and arbitrary value at an untrained non-antipodal query.
  Candidate A removes that freedom through a prescribed nullspace penalty; it
  does not prove that unmodified training selects it.
- **The hidden penalty alone does not remove all interpolants.** At \(h=h_0\),
  every \(c_0^*+q\), \(q\in\ker A_0\), has zero loss and zero hidden penalty.
  Thus \(L+\rho\|h-h_0\|^2/2\) has no unique zero. This is an objective-level
  obstruction, not a proof that every particular noise-free flow reaches
  several endpoints.
- **Ordinary readout weight decay generally prevents exact interpolation.**
  For an objective containing \(\lambda\|c\|^2/2\), \(\lambda>0\), with no
  compensating readout term, stationarity at an interpolating point gives
  \(0=2A_h^*e+\lambda c=\lambda c\). This forces \(c=0\), inconsistent with
  \(|Y|=1\). The fixed nullspace penalty avoids that bias because it vanishes
  at the selected interpolant.
- **Candidate A cannot retain learned limiting hidden geometry.** Its unique
  zero has \(h=h_0\). This is an exact feature of its objective, not a proof
  defect. Candidate B is an explicitly different objective which repairs this
  limitation, at the price of a current finite inverse in \(J\).
- **Loss-tangent noise is not enough for this proof.** Tangency must hold for
  the full selected objective \(U\), since the added penalties carry the
  confinement and selection. Their directional derivatives need not vanish
  under noise tangent only to \(L\). Tangency is the decisive imposed noise
  structure; arbitrary additive noise is outside the theorem.
- **No unproved global convexity or persistent Gram hypothesis.** Strong
  convexity is established on \(\Omega\); energy supplies strict confinement;
  the Gram lower bound follows from the explicit neighborhood. No all-space
  convexity or eventual convergence is assumed.
- **No white-noise or discretization theorem.** The result concerns
  continuous-time Hilbert-space ODEs with regular bounded tangent perturbation.
  It does not automatically cover Euler steps, SGD, quadrature populations,
  Brownian noise, or finite-width approximations.

| Claim | Status and evidence |
|---|---|
| Canonical \(K_0>0\) for every finite compatible circle dataset | Imported exact theorem from the allowed canonical-feature input. |
| Fixed initial-span interpolation remains unique in the certified ball | Proved by (6). |
| Explicit physical-state strong convexity and PL inequality | Proved by (7)–(17); no \(C^2\) Nemytskii assumption. |
| Global noisy flow from canonical initialization | Proved by (18)–(24), with an explicit Lipschitz bounded noise family. |
| Exponential training loss and unique full predictor limit | Proved by (25)–(27). |
| Candidate A retains learned limiting hidden geometry | False; its hidden limit is exactly \(h_0\). |
| Candidate B can retain nontrivial learned limiting hidden geometry | Proved by (28)–(29), and unconditionally for one-representative data. |
| Candidate B always moves hidden features for every finite dataset | Not asserted; equivalent here to the unresolved universal nonvanishing of \(\nabla J(h_0)\). |
| Unmodified physical loss flow enjoys these selection properties | Not established by this construction. |
| The learned selector improves generalization | Not claimed or tested. |

The strongest simple conclusion is Candidate A: two fixed quadratic penalties
already suffice for a complete noise-independent convergence theorem using
literal physical gradients. Candidate B gives a modest extension with actual
learned terminal geometry and the same proof architecture; a finite current
matrix solve remains, but inverse moving-feature transport does not.
