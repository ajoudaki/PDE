# Phase-I activation discovery and hostile audit

Status: discovery contract frozen; initial clean-room round reconciled;
focused mechanism round in progress, 22 August 2026.

This note records only conclusions that survive the corrected premise that
the two jointly reused Ginibre actions and their true adjoints already have
an immutable pointed-action realization.  A route that treated the source as
missing was rerun under that premise before its activation verdict was used.

## 1. Universal new depth-three obstruction

The added hidden layer creates the current middle cotangent

\[
 R_2=G_2^*\{A\phi'(Z_3)\},\qquad
 B_2=\phi'(Z_2)R_2.                                    \tag{1.1}
\]

This has no analogue in the proved depth-two cutoff argument.  If
\(d=\phi'\) is bounded, continuous, and nonconstant, the map

\[
 (Z,R)\longmapsto d(Z)R                               \tag{1.2}
\]

is not uniformly continuous on bounded subsets of
\(L^2\times L^2\).  Indeed, on a nonatomic probability space choose
\(d(a)\ne d(b)\), sets \(E_k\) with measure \(\varepsilon_k\downarrow0\),
and

\[
 R_k=\varepsilon_k^{-1/2}{\bf1}_{E_k}.
\]

Let \(Z_k=a\) and \(\widetilde Z_k=b\) on \(E_k\), with the fields equal
off \(E_k\).  Then

\[
 \|R_k\|_2=1,\qquad
 \|Z_k-\widetilde Z_k\|_2=|a-b|\sqrt{\varepsilon_k}\to0,
\]

but

\[
 \|d(Z_k)R_k-d(\widetilde Z_k)R_k\|_2=|d(a)-d(b)|.
\]

For a \(C^1\) activation, avoiding this obstruction for every state forces
\(d\) to be constant and hence \(\phi\) to be affine.  Thus activation
selection can reduce the reachable-tail burden but cannot remove it on bare
energy balls.

The exact quantitative repair is a square-tail modulus.  For bounded
Lipschitz \(d\),

\[
\begin{aligned}
 \|d(Z)R-d(\widetilde Z)\widetilde R\|_2
 &\le \|d\|_\infty\|R-\widetilde R\|_2
       +\|d'\|_\infty L\|Z-\widetilde Z\|_2\\
 &\quad+2\|d\|_\infty
 \{\mathbb E[\widetilde R^2\mathbf 1_{|\widetilde R|>L}]\}^{1/2}.
                                                               \tag{1.3}
\end{aligned}
\]

A uniform subexponential current tail gives the Osgood modulus
\(\delta\log(e/\delta)\); a fixed \(L^{2+\epsilon}\) bound gives only a
non-Osgood Holder modulus.  The proof target is therefore a reachable,
mesh-stable Orlicz estimate, not an unspecified collection of moments.

## 2. What scalar energy cannot prove

Physical gradient flow gives the exact path-energy identity

\[
 \int_0^T\|\dot\theta_n(t)\|_{\mathcal P_n}^2dt
 \le \mathcal L_n(0),                                 \tag{2.1}
\]

and hence normalized \(L^2\), Frobenius, and operator-norm bounds.  These
do not control coordinate square tails.  For an independent Ginibre matrix
\(W_{ij}\sim N(0,1/n)\), the bounded adaptive query

\[
 b_i=\operatorname {sign}(W_{i1})
\]

has \(\|b\|_n=1\), while

\[
 (W^*b)_1=\sum_i|W_{i1}|\sim\sqrt{2n/\pi}.
\]

Thus one vanishing-mass coordinate carries order-one extra square energy.
A random column selected by an iid label makes the construction
permutation-equivariant.  This is not known to be reachable by the smooth
gradient flow, so it falsifies the proposed inference from energy and
exchangeability, not the canonical convergence conjecture.

Similarly, an \(L_t^1\) kernel bound permits a height-\(n\), width-\(1/n\)
temporal spike.  Consequently neither path energy nor state equicontinuity
alone passes the raw tangent kernel.

## 3. Candidate comparison after the clean-room round

| candidate | exact current algebra | finite flow | forward/readout tails | middle-tail feature | audited verdict |
|---|---|---|---|---|---|
| \(\arctan x\) | bottom cubic natural coordinate; bounded coefficient algebra | smooth, global | bounded features; \(A=A_0+L^\infty\) | positive derivative; inverse weight \(1+Z^2\) | strongest established contract, but its depth-three \(\psi_1\) lemma remains open |
| \(\tanh x\) | polynomial in \(X=\tanh Z\) | smooth, global | bounded features; Gaussian-shift readout | bounded log derivative, but exponential inverse weight | no convergence advantage over arctangent; saturation can hide a cotangent |
| \(\sin x\) | compact \((\sin Z,\cos Z)\) phase lift | smooth, global | all activation coefficients bounded | derivative has finite zeros and changes sign | rejected as finalist: the lift only rotates a carrier concentration defect |
| fixed bi-Lipschitz residual | bounded half-density gauge and coercive \(B\leftrightarrow R\) | smooth, global | linearly unbounded features/readout | no hiding, but no tail gain | balanced frame recreates an unbounded logarithmic connection; total bootstrap is harder |
| piecewise homogeneous / absolute value | sectorwise deep-linear conjugacy | fails generically at attracting switching surfaces | bounded slopes | switching needs state-dependent sliding rule | rejected: finite-width uniqueness/stability is not available |
| polynomial / exponential | finite symbolic formulas | possible finite-time growth issues | unbounded or lognormal fields | worse products and moment hierarchy | rejected on proof feasibility |
| a.e.-flat nonlinearities | trivial closure | often nonsmooth | bounded | feature flow is suppressed | rejected as degenerate |

No nonaffine smooth activation admits a bounded local pointwise gauge that
removes (1.2).  Absorbing \(d(Z)\) into a cotangent introduces the connection

\[
 M_{(\phi''/\phi')\dot Z},                             \tag{3.1}
\]

which is only an \(L^2\) multiplier under the available estimates.  It
vanishes identically for all network states only when \(\phi''=0\).

## 4. Rational family and the critical endpoint

The strongest new smooth family from the discovery round is

\[
 \phi_m(x)=\int_0^x(1+s^2)^{-m}\,ds,qquad \tfrac12<m<1. \tag{4.1}
\]

It has

\[
 \phi_m'(x)=(1+x^2)^{-m},\qquad
 \frac{\phi_m''}{\phi_m'}=-\frac{2mx}{1+x^2},          \tag{4.2}
\]

so the output is bounded, the derivative is positive, the logarithmic
curvature is bounded, and unmasking a cotangent costs only the polynomial
weight \((1+Z^2)^m\).  The representative \(m=3/4\) improves that weight
over arctangent's \(m=1\) without introducing tanh's exponential inverse.
It was initially represented by \(m=3/4\), but the focused algebraic audit
found a stronger boundary candidate.  Write instead

\[
 d_q(x)=(1+x^2)^{-q/2},\qquad
 \phi_q(x)=\int_0^x d_q(s)\,ds.                       \tag{4.3}
\]

The unique Pareto endpoint is \(q=1\):

\[
 \boxed{\phi_1(x)=\operatorname {arsinh}x,\qquad
 d_1(x)=(1+x^2)^{-1/2}.}                              \tag{4.4}
\]

It has two exact advantages not shared simultaneously by the interior or
bounded-output choices.  First, for every \(0<\alpha\le2\),

\[
 e^{\alpha|\operatorname {arsinh}z|}\le C_\alpha(1+z^2). \tag{4.5}
\]

Thus a deterministic \(L^2\) bound on any preactivation yields exponential
uniform integrability of its forward activation, with no independence
assumption.  If \(q<1\), \(\phi_q(z)\asymp |z|^{1-q}\), and a sparse
\(L^2\) field disproves (4.5).  If \(q>1\), the output is bounded but the
second exact structure below is lost.

Second, put

\[
 d=(1+z^2)^{-1/2},\qquad s=zd.
\]

Then \(d^2+s^2=1\).  For every cotangent carrier \(R\), the pair

\[
 p=dR,\qquad q=sR                                      \tag{4.6}
\]

satisfies, under an arbitrary current velocity \(z'\),

\[
 p'=-d^2qz'+dR',\qquad q'=d^2pz'+sR',\qquad
 p^2+q^2=R^2.                                          \tag{4.7}
\]

The entire local multiplier contribution is therefore a skew rotation and
cannot amplify carrier energy.  The companion \(q\) is essential: a hidden
carrier can rotate into the raw-kernel component \(p\), so tracking \(p\)
alone is not stable.

Equations (4.5)--(4.7) promote \(\operatorname {arsinh}\) above
\(m=3/4\) for the focused proof round.  They still do not control the
nonlocal adaptive action \(\Gamma^*p\); a full leave-one-column tangent
lemma is now being derived.  Hence (4.4) is the leading candidate, not yet a
frozen theorem witness.

## 5. Exact sine and all-depth Picard audit

For sine, let \(E_j=\cos Z_j+i\sin Z_j\), and let \(C_j\) denote the
corresponding cotangent carrier.  The phase/cotangent field

\[
 W_j=E_jC_j
\]

obeys

\[
 E_j'=iZ_j'E_j,\qquad W_j'=iZ_j'W_j+E_jC_j'.          \tag{5.1}
\]

This is an exact finite-species current-time lift, but
\(|W_j|^2=C_j^2\).  A one-coordinate carrier spike is merely rotated
between its cosine and sine components.  The term \(Z_j'W_j\) is generally
only \(L^1\) on bare \(L^2\) states, and a cosine zero does not dissipate
the hidden carrier.  The independent focused route therefore rejected a
phase-only proof even though its finite algebra is elegant.  A later route
tested a stronger idea: approximate the *continuous* sine flow by nonlinear
Picard iterates, identify every fixed iterate by the transpose-reusing source
theorem, and then sum the iteration tail.  That route also fails at the
theorem boundary.

Indeed, with \(G_2=\Gamma_2+P_2\), differentiation of the learned forward
piece gives the exact term

\[
 D B_{3,i}[h]\supset-A_i(t)\sin Z_{3,i}(t)
 \int_0^t B_{3,i}(s)
 \langle X_2(s),D X_2(t)[h]\rangle_n\,ds .           \tag{5.2}
\]

There is no hidden \(1/n\) in the coordinate factor
\(A_i(t)B_{3,i}(s)\).  The phase field \(W_3=Ae^{iZ_3}\) turns the same
term into an imaginary rotation of the base carrier, but it is not
orthogonal to a *relative error*, so it does not cancel in a comparison
energy.  The lower phase field has the analogous \(R_2(t)B_2(s)\) term.

There may still be a useful transport-versus-reset combinatorics: the
normalized learned action closes the incoming open error mark before it
emits the two-amplitude coordinate factor.  What was actually proved,
however, is only a bound for every separately fixed Picard order.  It does
not imply

\[
 \lim_{M\to\infty}\limsup_{n\to\infty}
 \mathbb E\sup_{t\le T}d_n(Y_n(t),Y_n^{[M]}(t))^2=0. \tag{5.3}
\]

The forbidden interchange is the elementary triangular-array failure
\(e_{n,r}=\mathbf 1_{\{r=n\}}\): every fixed-order limit is zero while the
tail is one.  The available tensor-program theorem is fixed-program, and no
finite-\(n\), all-order summable envelope or growing-depth theorem was
proved.  Consequently sine is now rejected as a theorem-ready finalist,
not because its exact IDE is wrong, but because the proposed continuous-time
identification mechanism stops strictly below C4--C5.

## 6. Surviving proof obligations

For any bounded finalist, the learned transpose pieces are pointwise safe:

\[
 P_2(t)^*B_3(t)=\int_0^t X_2(s)
   \langle B_3(s),B_3(t)\rangle\,ds,                  \tag{5.1}
\]

and analogously for \(P_1^*B_2\).  The sharp stochastic bottleneck is the
pair of static adaptive queries

\[
 \Gamma_2^*B_3,qquad \Gamma_1^*B_2.                 \tag{5.2}
\]

A positive route must prove, uniformly in width, comparison mesh, and
compact time, a bound such as

\[
 \|\Gamma_2^*B_3\|_p+\|\Gamma_1^*B_2\|_p
 \le C_Tp^\gamma,qquad \gamma\le1,                  \tag{5.3}
\]

through the moderate range needed for empirical square tails.  Fixed-mesh
tensor-program moments do not prove (5.3) uniformly as the mesh is removed.

The first focused round tested three non-equivalent repairs:

1. an asinh-specific leave-one-column response estimate using (4.7);
2. a full current Malliavin/sensitivity operator with a dimension-free
   Gaussian-Sobolev norm; and
3. a stronger fixed current topology whose evolution must itself close.

The scalar-energy versions of all three have now failed.  If
`Z_i^{(j)}` is the response of row `i` to removal of column `j`, the exact
asinh phase tangent contains

\[
 \frac1n\sum_i d_i^2p_i^2\sum_j|Z_i^{(j)}|^2.        \tag{6.1}
\]

Separate bounds on the carrier energy and total response energy do not
control (6.1); an explicit one-row concentration makes (6.1) diverge while
both separate quantities stay bounded.  This is a proof-route refutation,
not a reachable-trajectory counterexample.  A second round is therefore
testing dynamic rowwise cavity control, a direct moderate-moment bootstrap,
and activation designs whose stability does not rely on scalar tangent
energy.

The residual-perturbation route also fails at first nonlinear order.  For
`phi(x)=x+epsilon h(x)`, the bottom cotangent contains

\[
 \epsilon\,\Gamma_1^*M_{h'(Z_2)}\Gamma_2^*B_3,       \tag{6.2}
\]

and the standard sign-column construction gives an order-`epsilon` jump
under a vanishing normalized-\(L^2\) perturbation.  Thus a small fixed
nonlinearity is genuinely nonlinear but does not regularize the missing
continuous-time bridge.

The third route has already ruled out finitely many ordinary joint \(W_2\)
laws, diagonal energy measures, and finite alternating-word lists.  Such
objects forget a current field's orientation relative to the true Gaussian
adjoint.  A full current sensitivity operator remains under audit because,
unlike a two-time response kernel, it is an extensional one-time state; it
will be accepted only if its norm and autonomous evolution close without an
infinite derivative hierarchy.

Activation and final IDE contract remain deliberately unfrozen until those
routes are audited.

## 7. Finite current-sensitivity hierarchies

Appending the full first Gaussian response \(J=D_\xi Y\) is algebraically
current-time and restartable, but the tested Hilbert--Schmidt energies do not
close.  At either nonlinear hidden layer write

\[
 Z_i'=aB_i+F_i,\qquad B_i=d_iR_i,\qquad
 S_i=\sum_\alpha|D_\alpha Z_i|^2.
\]

For Gudermannian, with \(d'=-sd\), the exact weighted response energy

\[
 E_m=\langle |B|^{2m}S\rangle
\]

has leading derivative

\[
 E_m'=-2a(m+1)\langle sB|B|^{2m}S\rangle+\mathcal R_m. \tag{7.1}
\]

Absolute estimation therefore generates the next \(B\)-power at every
finite truncation.  The unique scalar weight cancelling the principal term
is \(d^{-2(m+1)}=\cosh^{2(m+1)}Z\); Gaussian initialization gives this
weight lognormal rather than \(\psi_1\) or \(\psi_2\), and cross-layer
forcing reintroduces \(d^{-1}D F\).  The sine analogue uses the singular
weight \(\sec^2 Z\).  This rules out the tested finite polynomial,
phase-energy, and ordinary current-HS Lyapunov closures.  It does not rule
out a reachable-state cavity theorem, an all-order completed norm, or every
possible operator IDE.

## 8. Smooth flat-support quenching audit

A separate clean-room route tested whether a bounded smooth activation whose
derivative is a compactly supported flat bump could turn large backward
coordinates off before they concentrate.  This mechanism fails for three
independent exact reasons.

First, if (b=\phi'\) is (C^\infty), nonzero on ((-1,1)), and flat at
(1), then

\[
 \int_{s_0}^1\frac{ds}{b(s)}=\infty .
\]

Thus even the favorable scalar equation (z'=c(t)b(z)), with locally
integrable (c), approaches the flat boundary only asymptotically and never
enters the exactly inactive region at finite time.  Second, inactivity of one
coordinate is not invariant in the network because

\[
 Z_2'=(\|X_1\|^2I+G_1D_1^2G_1^*)B_2,
 \qquad
 Z_3'=(\|X_2\|^2I+G_2D_2K_2D_2G_2^*)B_3;
\]

off-diagonal Gram forcing generically reactivates a coordinate whose own gate
is zero.  Finally, every nonconstant bump has an interior interval on which
​(|b'|\ge c>0).  Canonical Gaussian initialization therefore gives

\[
 \|\operatorname{diag}(A_0b'(Z_{3,0}))\|_{\rm op}
 \gtrsim\sqrt{\log n}
\]

with high probability.  Flatness at the edge does not improve this genuine
interior variational coefficient.  Compact support remains a valid exact
finite algebra and a globally well-posed finite flow, but it supplies neither
finite-time quenching nor the required mesh-stable adjoint-tail estimate.

## 9. Fixed residual of the solved linear core

The most favorable near-linear witness tested was the fixed, width-independent
activation

\[
 \phi_\varepsilon(x)=x+\varepsilon\sin x,
 \qquad 0<\varepsilon<1.
\]

It is genuinely nonlinear and bi-Lipschitz.  At initialization its limiting
raw kernel is

\[
 K_\varepsilon(0)=4+24e^{-1/2}\varepsilon+O(\varepsilon^2),
\]

and its Hermite-three feature component is

\[
 \left\langle H_3(u_0),\phi_\varepsilon(u_0)-u_0\right\rangle
 \longrightarrow-\varepsilon e^{-1/2}.
\]

Thus the nonlinear contribution is fixed and nonvanishing, while every layer
still moves at order one.  Algebraically the route is unusually clean: the
feature vector field has the exact decomposition

\[
 V_\varepsilon=V_0+\varepsilon W_\varepsilon,
\]

where (V_0) is the proved deep-linear vector field, every sine/cosine gate
in (W_\varepsilon) is kept exact, and each summand has at most two
unbounded coordinate carriers.  On a stopped operator/norm tube this proves
a dimension-free (O(\varepsilon)) comparison with the linear trajectory,
a finite target-hitting feature clock, and uniform integrability of the
scalar raw kernel.

It does not prove the exact fixed-(\varepsilon) width limit.  Repeated exact
divided differences reduce the problem to a reachable source-word estimate
uniform simultaneously in width and insertion order.  A representative
sufficient bound for every (m)-reset word is

\[
 \|\mathcal W_{m,n}\|_{L^2(\Omega;H_n)}
 \le C_0(C_1\sqrt m)^m
\]

(a charge-two (C_0(C_1m)^m) bound also suffices for small enough fixed
(\varepsilon)).  Fixed-order tensor programs give no constants uniform as
(m\) grows with (n), and after the first coordinatewise reset the full
orthogonal invariance of the linear core is lost.  Norm bounds plus the
remaining signed-permutation symmetry allow concentration.  Conversely, an
ordinary Taylor expansion is invalid already at (n=1): for the cubic
backward carrier (H=G_1G_2A),

\[
 \left\|\frac{H^m}{m!}\right\|_2
 =\frac{[(2m-1)!!]^{3/2}}{m!},
 \qquad
 \left\|\frac{H^m}{m!}\right\|_2^{1/m}\asymp\sqrt m.
\]

The residual witness is therefore closer to the linear theorem in a rigorous
perturbative sense, but it has not crossed C4: its all-order source-word lemma
is another form of the adaptive reused-adjoint theorem, not a consequence of
the linear result.

## 10. Pointwise coercive-lift rigidity

A clean-room finite-lift audit gives a useful class-wide theorem, but not a
class-wide convergence impossibility.  Suppose a smooth finite pointwise lift
of the scalar channel

\[
 u'=q\phi'(u)
\]

has a positive tangent metric whose pullback is \(w(u)du^2\).  If the part of
the tangent-energy derivative proportional to an arbitrarily large signal
\(q\), of either sign, cancels or is bounded independently of \(q\), then

\[
 w'(u)\phi'(u)+2w(u)\phi''(u)=0,
 \qquad w(u)\phi'(u)^2=C.                         \tag{10.1}
\]

Thus a uniformly coercive pointwise metric forces \(|\phi'|\) to be bounded
above and away from zero.  Bounded, periodic, saturating, and
derivative-decaying nonlinearities necessarily have a singular or
noncoercive cancelling metric.  Extra complex, phase, or hyperbolic
coordinates do not evade (10.1), because every positive ambient metric pulls
back to a scalar \(w\).

For a bi-Lipschitz residual activation the direct scalar channel can indeed be
flattened.  At a hidden layer, however, the current natural-coordinate
operator has the form

\[
 T(y)=D(y)^{-1}HD(y),
\]

and its linearization contains

\[
 DT[y](h)a=[T(y),M_{\ell(y)h}]a.                  \tag{10.2}
\]

For a dense nonlocal \(T\), (10.2) is not a bounded map
\(L^2\times L^2\to L^2\).  The commutator vanishes for all states only in the
affine case.  This closes the *purely pointwise coercive-lift route*.  It does
not rule out stochastic delocalization along the canonical Gaussian flow.

The accompanying scalar feature-ascent blow-up for \(\inf|\phi'|>0\) is not a
physical-time obstruction.  MSE gradient flow satisfies

\[
 \dot{\mathcal L}=-\|\dot\theta\|^2,
 \qquad \|\theta(t)-\theta(0)\|\le\sqrt{t\mathcal L(0)},
\]

so every finite-width physical trajectory is globally continuable on compact
time.  The earlier feature-clock blow-up argument is therefore retained only
with this restricted scope.

## 11. Full cyclic-traffic proposal and retraction

A proposed positive sine proof retained two immutable Ginibre traffic
operators and the four current variables \((A,u,P_1,P_2)\), then metrized the
state by every rooted activation program.  Its exact finite and formal
current-time IDE is valid.  Its claimed C4--C6 bridge is not.

The missing assertion was a mesh-uniform empirical sub-Gaussian bound for

\[
 G_2^*B_3,\qquad G_1^*B_2.                         \tag{11.1}
\]

Fixed-mesh Gaussian regression does not supply it.  Consecutive Euler queries
coalesce as the mesh \(h\downarrow0\); their Gram matrices have eigenvalues of
order \(h^2\), often smaller at higher order, and the regression
pseudoinverses are not uniform.  Orthogonalizing avoids an explicit inverse
only by retaining a growing query span and still requires the same missing
leverage/delocalization theorem.  Bounded gates, rank-one update bounds, and
Gaussian operator norms do not exclude the adaptive sign-column
concentration example.

There is a second contract issue.  At finite width, a full cyclic module with
unrestricted diagonal functional calculus recovers every coordinate
projection almost surely and hence every matrix entry.  It is the microscopic
state modulo permutations, not a demonstrated compression.  A coarser
fixed-test traffic quotient forgets vanishing-density concentration defects;
adding every composite multiplier and raw square as an independent coordinate
makes the generator and kernel continuous only tautologically.  Accordingly,
the sine traffic semigroup, continuous-time convergence, and raw-kernel claims
are retracted.  The exact operator skeleton and fixed-mesh program limits
remain valid.

The next discovery round is testing activations with a positive output floor
and a fixed small but nonzero nonlinear derivative.  Two current candidates
are a shifted arctangent and

\[
 \phi_{c,\epsilon}(z)=c+\exp\{\epsilon\operatorname{arsinh}z\},
 \qquad c>0,\quad0<\epsilon<1.                     \tag{11.2}
\]

The latter has sublinear polynomial forward tails, a bounded positive
derivative, a finite physical residual clock, and the exact asinh cotangent
pair.  These are hypotheses under active audit, not promoted claims.

## 12. Shifted arctangent: exact gains and the surviving obstruction

Fix

\[
 \phi(x)=c+\epsilon\frac{2}{\pi}\arctan x,
 \qquad 0<\epsilon<c,
\]

and write \(m=c-\epsilon\), \(M=c+\epsilon\), and \(d_*=2/\pi\).
This activation is bounded away from zero.  Consequently the raw kernel
satisfies \(K\ge m^2\), so in physical residual time

\[
 |e(t)|\le |e(0)|e^{-m^2t},
 \qquad
 \Lambda:=\int_0^\infty |e(t)|\,dt
 \le \frac{|e(0)|}{m^2}.                         \tag{12.1}
\]

Let \(a_0=\lVert A_0\rVert_n\),
\(g_{\ell,0}=\lVert G_{\ell,0}\rVert_{\rm op}\), and define

\[
\begin{aligned}
 P_A&=a_0+M\Lambda,\\
 P_2&=g_{2,0}+d_*\epsilon M\Lambda P_A,\\
 P_1&=g_{1,0}+(d_*\epsilon)^2M\Lambda P_2P_A,\\
 P_u&=\lVert u_0\rVert_n+(d_*\epsilon)^3\Lambda P_1P_2P_A.
\end{aligned}                                      \tag{12.2}
\]

Direct integration of the exact finite-width equations proves, for all
physical times,

\[
 \lVert A\rVert_n\le P_A,
 \quad \lVert G_2\rVert_{\rm op}\le P_2,
 \quad \lVert G_1\rVert_{\rm op}\le P_1,
 \quad \lVert u\rVert_n\le P_u,                  \tag{12.3}
\]

and the successive backward fields have charges

\[
 \lVert B_3\rVert_n=O(\epsilon),\quad
 \lVert R_2\rVert_n=O(\epsilon),\quad
 \lVert B_2\rVert_n+\lVert Q_1\rVert_n=O(\epsilon^2),
 \quad \lVert D_1Q_1\rVert_n=O(\epsilon^3),       \tag{12.4}
\]

with the constants given explicitly by the products in (12.2).  Gaussian
initial operator-norm estimates and conditional Gaussianity of \(f(0)\)
then give dimension-uniform \(L^p\) bounds for these RMS quantities and their
raw squares for \(2\le p\le c_0n\).  This is a genuine all-time scalar
uniform-integrability theorem, not a coordinate-tail theorem.

The activation also remains nondegenerate.  For fixed sufficiently small
\(\epsilon>0\), the width limits of the squared feature-clock velocities of
\(G_2,G_1,u\) are respectively positive constants of orders
\(\epsilon^2,\epsilon^4,\epsilon^6\), and the squared feature velocity is a
positive constant of order \(\epsilon^4\).  None vanishes as \(n\to\infty\).

There is an exact local-curvature resummation.  Put

\[
 d(z)=\frac{2/\pi}{1+z^2},
 \qquad h(z)=\frac{d'(z)}{d(z)}=-\frac{2z}{1+z^2},
 \qquad w_\ell=\frac{\delta z_\ell}{d(z_\ell)}.
\]

It removes every diagonal self-curvature multiplier.  It does not remove the
nonlocal middle-layer product.  The exact gauged variational equation contains

\[
 2\epsilon^2d_2^{-1}G_1
 \bigl(h_1d_1^3Q_1w_1\bigr).                       \tag{12.5}
\]

Operator control reduces (12.5) only to \(\lVert Q_1w_1\rVert_n\).  There is
no dimension-free inequality controlling this product from the separate RMS
norms; simultaneous localization gives the sharp \(\sqrt n\) loss.  A fixed
small \(\epsilon\) cannot absorb that loss.  Thus shifted arctangent has
passed finite-flow, tail-integrability, and non-laziness tests, but has not
passed C4--C6: the remaining statement is precisely an annealed row-influence
or dynamic-delocalization theorem and cannot be inserted as an assumption.

The appropriate sufficient tail target is moderate rather than global
Orlicz control.  For all current coordinate fields \(Y\) and the required
quadratic current observables \(Q\), it would suffice to prove, uniformly for
\(2\le p\le c\log n\),

\[
 \sup_{i,Y}\left\|\sup_{t\le T}|Y_i(t)|\right\|_p
 \le C_T\sqrt p,
\]

and

\[
 \left\|\sup_{t\le T}
 \left|\langle Q(Y(t))\rangle_n
       -\mathbb E\langle Q(Y(t))\rangle_n\right|\right\|_p
 \le C_T\left(\sqrt{\frac pn}+\frac pn\right).    \tag{12.6}
\]

Equation (12.6) would imply square uniform integrability and continuity of
the raw kernel.  It remains a target, not a proved lemma.

A mechanism-preserving single-source experiment resampled one immutable
Gaussian row or column, coupled every other source, and integrated the exact
finite feature flow to clock (0.5).  For widths (64,128,256), both shifted
arctangent and (11.2) kept

\[
 \sqrt n\,\lVert Y_n-\widetilde Y_n\rVert_n
\]

stable for every tested forward and backward field, and likewise kept the
scaled predictor and raw-kernel differences stable.  The script is
`audit_single_source_influence.py`.  This discriminates against an order-one
single-source instability, but it is not the uniform all-source influence
bound, the centered concentration estimate, or the continuous-time theorem.

## 13. Strong derivative damping and the transpose-energy defect

The Gaussian-derivative witness

\[
 \phi(x)=\operatorname{erf}(x),
 \qquad \phi'(x)=\frac{2}{\sqrt\pi}e^{-x^2},
\]

has a globally well-posed finite flow and strictly positive initialization
speeds in all four trainable blocks.  Strong derivative decay nevertheless
does not quench the independent readout tail.  More generally, if (d) is
bounded and nonzero on a set of positive Gaussian measure, then at canonical
initialization

\[
 \frac{\max_{i\le n}|A_i d(Z_{3,i})|}{\sqrt{2\log n}}
 \xrightarrow{\mathbb P}
 \operatorname*{ess\,sup}_{Z}|d(Z)|.              \tag{13.1}
\]

The proof restricts to a positive-density set on which (|d|) is within an
arbitrary epsilon of its essential supremum and applies the Gaussian maximum
law to the independent (A_i)'s.  Thus super-Gaussian damping improves the
behavior after a coordinate moves, but cannot bound the cotangent at the
independent initial slice.

There is also a representation-level obstruction.  At initialization let

\[
 H_2=G_2^*B_3=G_2^*D_3A.
\]

For every finite family of upstream tests (v_n), independent of (A), with
bounded normalized norm,

\[
 \langle v_n,H_2\rangle_n\longrightarrow0
 \quad\text{in probability},                     \tag{13.2}
\]

because its conditional variance is (O(n^{-1})).  At the same time,

\[
 \lVert H_2\rVert_n^2\longrightarrow
 \mathbb E[d(Z_3)^2]>0,                           \tag{13.3}
\]

and multiplication by the next derivative leaves a positive lower-layer
gradient energy.  Hence (H_2) is weakly null but carries nonzero quadratic
energy.

An ordinary population isonormal operator (K) and its Hilbert adjoint give
the wrong answer: for an independent centered Gaussian mark (A),

\[
 \langle K^*(A d(Kx)),v\rangle
 =\mathbb E[A d(Wx)Wv]=0
\]

for every (v), whereas (13.3) is positive.  A viable current-state contract
must therefore retain a two-sided open/traffic Gaussian action.  Derivative
damping does not permit replacement by a classical layerwise (L^2) kernel.
This is a rigorous no-go for that representation class, not an impossibility
theorem for the richer traffic/operator contract.

## 14. Positive hyperbolic lift

For

\[
 \phi(z)=c+\exp\{\epsilon\operatorname{arsinh}z\},
 \qquad c>0,quad0<\epsilon<1,
\]

put (v=\operatorname{arsinh}z).  Its derivative is

\[
 D(v)=\epsilon e^{\epsilon v}\operatorname{sech}v,
\]

which is bounded and Lipschitz, and the standard hyperbolic cotangent pair
preserves its carrier (L^2) norm.  The positive constant gives
(K\ge c^2), hence a horizon-independent finite absolute residual clock.
Exact natural-coordinate counting puts the primitive nonlocal transports at
orders (epsilon^3) and (epsilon^4), with a composite term at
(epsilon^5).

These facts do not close convergence.  For any (a) with (D(a)\ne D(0)),

\[
 R_n=\sqrt n,e_1,qquad v_n=0,qquad
 \widetilde v_n=a e_1
\]

obey (lVert v_n-\widetilde v_n\rVert_n\to0), while

\[
 \lVert[D(v_n)-D(\widetilde v_n)]R_n\rVert_n
 =|D(0)-D(a)|.
\]

The phase identity does not see this co-localization.  More generally, fixed
(2+\delta) moments yield only a Hölder, non-Osgood stability modulus.  A
mesh-uniform empirical Weibull bound of order at least one together with a
leave-one-column theorem would be sufficient, but neither follows from the
phase energy or the sublinear forward tails.  Small fixed (epsilon) merely
scales the discontinuity and does not change its Osgood character.  Since
the nonlocal charges are not better than shifted arctangent's, this witness
does not win the depth-three tradeoff.

## 15. Shifted sine: absolute expansion obstruction

The positive shifted sine

\[
 \phi(z)=c+\epsilon\sin z,\qquad c>\epsilon>0,
\]

also has a finite absolute residual clock, bounded gates, a compact exact
current operator contract, and nonzero motion in every trained layer.  Its
deterministic dependency-path combinatorics are benign once pointwise sine
channels are treated exactly: an order-\(m\) time-ordered increment has a
simplex denominator \(m!\).

This is not enough for an absolute Gaussian diagram proof.  Already at
width one, a connected repeated local ladder in the bottom equation contains

\[
 D_m={ (\epsilon^3s)^m\over m!}
      (A_0\gamma_1\gamma_2)^m
      \cos(c\gamma_1)^m\cos(c\gamma_2)^m
      (-\sin u_0)^{m-1}\cos u_0 .
\]

Gaussian saddle estimates give

\[
 \|D_m\|_2\ge m^{-O(1)}
       (C_c\epsilon^3s\sqrt m)^m,
\]

so the terms fail to tend to zero for every fixed positive
\(\epsilon s\).  Thus taking norms term by term before resumming local
ladders is invalid.

This counterexample does **not** rule out the required width-first limit.
After maximal local resummation, a sufficient estimate would be a uniform
reachable-channel bound of the form

\[
 \limsup_{n\to\infty}
 \left(\mathbb E\,{1\over n}\sum_i |H_{n,i}(s)|^p\right)^{1/p}
 \le C\sqrt p
\]

for every exact-flow forward, adjoint, and tangent channel, together with
uniform connected-contraction estimates when immutable Gaussian edges are
replaced by learned rank-one insertions.  It would imply a remainder bounded
by

\[
 C_0{(C_1\epsilon S)^m m^{m/2}\over m!}\longrightarrow0.
\]

No current argument proves this for factors evaluated on the exact
continuous trajectory.  Fixed-order tensor programs prove it only for a
fixed approximant; replacing exact channels by that approximant requires the
same remainder estimate and is circular.  Shifted sine is therefore not
refuted as a model, but it is rejected as a theorem-ready Phase-I winner.

## 16. Shifted tanh and the single-Banach traffic obstruction

For \(c>\epsilon>0\), put

\[
 \phi(z)=c+\epsilon\tanh z,
 \qquad H_1=\tanh u,\quad H_2=\tanh Z_2,\quad H_3=\tanh Z_3.
\]

Writing \(M_j=1-H_j^2\) makes every pointwise operation polynomial in
bounded marks.  The resulting marked open-traffic hierarchy is exact at
every finite width, and the positive feature floor gives

\[
 K\ge(c-\epsilon)^2,
 \qquad
 \int_0^\infty |y-f(t)|\,dt
 \le {|y-f(0)|\over(c-\epsilon)^2}.
\]

This does not become a theorem merely by putting every open graph coordinate
into one weighted Banach algebra.  If a unital Banach algebra contains the
Gaussian readout mark \(a\), has continuous multiplication, and Gaussian
evaluation is continuous, then

\[
 (2m-1)!!=\tau(a^{2m})
 \le \|\tau\|M^{2m-1}\|a\|^{2m},
\]

which is impossible because the left-hand side has unbounded \(2m\)-th
root.  Independently, a bounded nonzero derivation on a commutative
semisimple state algebra would contradict the Singer--Wermer theorem,
whereas \(\mathcal DF=K\ne0\).

Factorial/Gaussian graph weights therefore lead at best to a scale of
spaces with radius loss,

\[
 \|\mathcal DP\|_{\rho,\eta}
 \le C\|P\|_{R,E},\qquad \rho<R,\quad\eta<E,
\]

or to unbounded affiliated operators.  Such a formulation is not ruled
out, but it still requires uniform all-graph tightness, positivity and
representation, a scale-space uniqueness theorem, concentration of the
quenched residual, preservation of the \(H_j=\tanh Z_j\) constraints, and
quadratic continuity of \(K\).  The exact polynomial hierarchy is thus C1,
not C4--C6.

## 17. Shifted arctan: corrected local resummation boundary

For

\[
 \phi(x)=1+\epsilon {2R\over\pi}\arctan(x/R),
 \qquad 0<\epsilon<(2R)^{-1},
\]

let \(D=\phi'(z)\), \(E=\phi''(z)\), and
\(h=E/D=-2z/(R^2+z^2)\).  If

\[
 \dot z_2=\alpha_1D_2R_2+H_2,qquad
 H_2=G_1D_1^2Q_1,\qquad \theta_2={\delta z_2\over D_2},
\]

then the exact covariant tangent equation is

\[
 \dot\theta_2=\delta\alpha_1R_2+\alpha_1\delta R_2
 +{\delta H_2\over D_2}-h_2H_2\theta_2.       \tag{17.1}
\]

The local \(E_2R_2\delta z_2\) term cancels, but the last nonlocal term in
(17.1) does not.  Since \(|h|\le R^{-1}\), it can still be treated as one
small-carrier insertion.  The analogous layer-three equation has the same
structure.

This corrects, but does not close, the cavity expansion.  Learned tangent
edges preserve one coordinatewise active line only after producing
empirical scalars.  A representative nested term is

\[
 B_3(s)\,
 \langle\delta X_2(s),D_2(t)\dot z_2(t)\rangle_n .    \tag{17.2}
\]

To prove the claimed moderate moments one must show, uniformly through all
insertion orders \(m\le n^{1/4}\), that every centered scalar in (17.2)
either factors to its deterministic limit or creates an extra label
identification and gains \(n^{-1}\).  The correctly normalized target is

\[
 \mathbb E\sup_t\langle|\mathcal C_m(t)|^p\rangle_n
 \le (C_0\sqrt p)^p C_1^{mp}
       \exp\{C(mp)^2/n\},
 \qquad p\le c\log n.                               \tag{17.3}
\]

The previously proposed bound had \(C^{m+p}\) before taking a \(p\)-th
root and was therefore undercounted.  The high-order stopped Picard tail can
be controlled once (17.3) is known; (17.3) itself is not proved for nested
\(P/P^*\) edges.  A Hilbert ultraproduct supplies a fixed current-time
true-adjoint realization, but bare \(L^2\) uniqueness fails for the same
multiplier reason.  Thus local resummation is a valid new lemma, not the
C4--C6 bridge.

## 18. Integrability--Osgood threshold and logarithmic saturators

Let \(\phi\) be strictly increasing and put
\(\eta=1/\phi'\).  The identity

\[
 \int_a^\infty {dx\over\eta(x)}
 =\int_a^\infty\phi'(x)\,dx
 =\phi(+\infty)-\phi(a)                         \tag{18.1}
\]

shows that a bounded monotone activation necessarily has a non-Osgood naked
inverse derivative on each saturating tail.  If \(\phi'>0\) is eventually
decreasing and integrable, then \(x\phi'(x)\to0\); a sparse random variable
with bounded second moment can therefore have unbounded
\(\|1/\phi'(X)\|_2\).  This is a sharp obstruction to any proof based only
on RMS control of an unpaired inverse gate.  It is not a no-go for paired
phase/cotangent variables, where the inverse can cancel.

A near-critical bounded family is obtained from

\[
 g_\beta(x)={C_\beta\over
 \sqrt{1+x^2}[\log(e+x^2)]^{1+\beta}},
 \qquad
 \phi_\beta(x)=c+\epsilon\int_0^xg_\beta(s)\,ds,
 \quad\beta>0.                                      \tag{18.2}
\]

For a Gaussian \(G\),

\[
 \|1/\phi_\beta'(G)\|_p
 \asymp \sqrt p\,(\log p)^{1+\beta},               \tag{18.3}
\]

which is much better than arctangent's order-\(p\) inverse-gate moment but
remains beyond the critical asinh order \(\sqrt p\).  Iterated-log gates can
approach the threshold arbitrarily closely, at the cost of one additional
auxiliary mark per logarithm; no bounded tail is optimal.

The log derivative \(\phi_\beta''/\phi_\beta'\) is bounded, and adjoining
the finite marks

\[
 (1+z^2)^{-1/2},\quad(e+z^2)^{-1},\quad
 [\log(e+z^2)]^{-1},\quad
 [\log(e+z^2)]^{-1-\beta}
\]

gives an exact one-time differential-algebraic lift.  This improves the
activation-local tail tradeoff but does not remove the adaptive true-adjoint
problem.  The Phase-I Pareto boundary is therefore structural: bounded
positive saturators trade a finite clock for non-Osgood inverse tails;
asinh is the RMS/Osgood endpoint; bi-Lipschitz residuals have bounded inverse
gate but linear forward tails.

## 19. Shifted Gudermannian: exact local win, surviving through ladder

For

\[
 \phi(z)=c+\epsilon\operatorname {gd}(z),\qquad
 c>\pi\epsilon/2,
\]

put `theta=gd(z)`, `d=cos(theta)=sech(z)`, and
`r=tan(theta)=sinh(z)`.  A prescribed direct cell

\[
 \dot\theta=\epsilon a(s)C(s)\cos^2\theta
\]

becomes the additive characteristic

\[
 \dot r=\epsilon a(s)C(s),
\]

and its exact phase propagator satisfies

\[
 \left|{\partial\theta(t)\over\partial\theta(s)}\right|
 ={1+r(s)^2\over1+r(t)^2}
 \le2(1+I_{s,t}^2).                               \tag{19.1}
\]

The coupled top `(A,r)` tangent likewise has coefficients independent of
the magnitude of the Gaussian readout.  This is a real improvement over
shifted sine, whose derivative-zero phase has an exact lognormal tangent.

It does not close the learned middle layer.  If `P2=delta G2`, then

\[
 \delta P_2(t)=\int_0^t
 [\delta B_3(s)\otimes X_2(s)+B_3(s)\otimes\delta X_2(s)]\,ds,
\]

and the phase variation contains

\[
 -\epsilon^2d_3(t)\int_0^t
 \beta(s,t)A(s)\sin\theta_3(s)\delta\theta_3(s)\,ds,
 \qquad
 \beta(s,t)=\langle X_2(s),\dot\theta_2(t)\rangle_n.       \tag{19.2}
\]

At equal times,

\[
 \beta(t,t)={1\over2\epsilon}{d\over dt}\langle X_2(t)^2\rangle_n,
\]

so it is not annihilated by a feature-norm conservation law.  Its
deterministic small-time expansion is generically nonzero.  Iterating
(19.2) retains one unsummed readout factor per insertion and gives the
moment scale

\[
 { (C\epsilon^5S)^m(mp)^{m/2}\over m!}.
\]

This is summable, with envelope `exp(C epsilon^10 S^2 p)`, but it is not the
previously claimed collision-free sub-Gaussian bound.  Shifted
Gudermannian therefore improves the local regularity without eliminating
the need for a coupled dynamic-cavity/Onsager theorem.

## 20. Exact Stein audit of the scalar high-temperature recursion

For one Gaussian source column

\[
 g=\Gamma_{\cdot j}\sim N(0,n^{-1}I),\qquad
 q_j=g^TB(g),
\]

the exact identity is

\[
 q_j=\delta_g(B)+{1\over n}\operatorname {div}_gB,        \tag{20.1}
\]

where `delta_g` is the Skorohod divergence.  It is centered conditionally
on the other columns but is not generally Gaussian.  If `B^0` is the
leave-column field, an exact innovation--response decomposition is

\[
 q_j=g^TB^0+\overline O_j+E_j,
 \qquad
 \overline O_j=\mathbb E_g[n^{-1}\operatorname {div}_gB\mid\mathcal F_{-j}],
\]

with a conditionally centered remainder.  A Meyer bound involves both the
field difference and the full Hilbert--Schmidt source derivative; an
operator-norm tangent estimate is insufficient.

The proposed step replacing an `exp(a p)` response by its mean is false.
Let a common random mode `U=exp(sigma Z)` be independent of `g` and set
`B=Ug`.  Then the centered error is

\[
 U(\|g\|^2-1)=O_{L^p}(p n^{-1/2}e^{ap}),
\]

exactly of the advertised small size, while

\[
 \overline O_j=U,\qquad \|\overline O_j\|_p=e^{ap}.
\]

No scalar absorption with a fixed coefficient below one follows.  In the
actual network the response is additionally coupled through
`delta P1`, `delta P2` and their adjoints in both orientations.  A valid
positive theorem must construct an intrinsic current Stein map on a fixed
weighted rooted-query space, prove concentration of its covariance data,
and bound the spectral radius of the complete coupled response.  Defining
that map as a conditional expectation of the ancestral interpolation would
merely rename the missing theorem and would not give a restartable state.

## 21. Actual-network failure of one-direction Onsager closure

The preceding common-mode example is an abstract audit.  There is also an
exact obstruction on the canonical network trajectory.  At initialization,
for either shifted arctangent or shifted Gudermannian, let

\[
 K_n(s,t)=\langle\Gamma _2X_2(s),B_3(t)\rangle_n,
 \qquad C_n(s,t)=\langle X_2(s),X_2(t)\rangle_n
\]

and define

\[
 \Delta_n(t)=K_n(0,t)C_n(t,t)-K_n(t,t)C_n(0,t).
\]

If the transpose action at time `t` were a fresh innovation orthogonal to
all previously exposed directions plus a scalar multiple of only `X2(t)`,
then `Delta_n(t)` would vanish in the width limit.  Direct differentiation
of the exact finite equations instead gives

\[
 \lim_{\epsilon\downarrow0}\epsilon^{-4}
 \lim_{n\to\infty}\Delta_n'(0)=-c^4m_c^2<0,
 \qquad m_c=\mathbb E[g(cZ)^2],
\]

where `g` is the unscaled derivative profile and `Z` is standard Gaussian.
Thus an older feature direction survives at order `epsilon^4` for every
sufficiently small fixed nonlinearity.  High temperature reduces its size;
it does not scalarize it.  Eliminating the immutable Gaussian operator
therefore produces a growing response span and, in the continuum, the
forbidden Volterra/two-time description.  An admissible positive result must
instead retain the fixed two-sided quenched operator in a genuine current
rooted-traffic representation.

A second audit rules out the simplest finite weighted-energy substitute.
For shifted Gudermannian, differentiating the first transpose field creates

\[
 S_2=G_2^*\{A^2d_3^2\tanh Z_3\}.
\]

Differentiating an energy containing `S2` creates the next contraction
`G2^*(A^3 F3(Z3))`, and iteration produces arbitrary powers `A^k`.
The unresummed Gaussian scale is `(C epsilon sqrt(k))^k`, which is too large
for a finite Gronwall hierarchy at `k` of logarithmic order in width.  This
does not refute a chronological tree or graded-traffic resummation, since its
time-simplex factors can be summable.  It does prove that neither a scalar
Onsager coefficient nor a finite list of polynomial readout weights closes
the convergence bridge.

## 22. Smooth activation cancellation and finite-gate no-go

There is a class-wide algebraic limit on what activation selection alone can
accomplish.  At the top layer write `D=phi'(Z3)`, `B3=A D`,
`q2=<X2^2>`, and `H=G2 X2dot`.  The exact current identity is

\[
 \dot B_3=\phi\phi'+q_2A^2\phi''\phi'+A\phi''H.       \tag{22.1}
\]

Assume `phi` is `C2`, the restart law of `Z3` has full support, and the
readout has a continuous full-support law.  If (22.1) vanishes for every
admissible current forcing `H`, varying `H` gives `phi''=0`.  The remaining
identity is `phi phi'=0`, equivalently `(phi^2)'=0`; continuity on the real
line makes `phi` constant.  In particular, pathwise elimination of only the
learned-through term already forces an affine activation.  An averaged
choice such as `q2 phi''+phi=0` cannot help because the centered `A^2-1`
chaos remains.

There is a parallel finite-algebra obstruction.  Every immediate
forward/adjoint round trip inserts the multiplier

\[
 g(z)=\phi'(z)^2.
\]

If a fixed finite pointwise multiplier module contains all response words,
then `1,g,g^2,...` are linearly dependent.  A polynomial therefore
annihilates the continuous function `g`.  Since its image is connected and
contained in the finite root set of that polynomial, `g` is constant;
continuity of `phi'` then makes `phi` affine.  Thus a successful nonlinear
contract must use a genuinely infinite-dimensional current operator/module
species, even though the number of species may remain fixed.  This theorem
does not rule out such a graded or rooted-traffic operator, but it rules out
finding a magical smooth scalar activation whose finite gate alphabet closes
the depth-three response exactly.

## 23. Graded traffic and generic Hida-scale audit

For the bounded positive activation

\[
 \phi_\epsilon(x)=1+{2\epsilon\over\pi}\arctan x,
 \qquad0<\epsilon\le1/4,
\]

the exact current tuple `(A,L1,L2,h)`, with
`h=u+u^3/3` and `G_l=W_l+L_l`, has a finite physical feature clock and
all fixed raw-kernel moments are uniformly integrable.  A natural proposed
limit is the GNS completion of typed rooted/open Wick traffic diagrams, with
the two orientations of each source edge representing the same Ginibre
matrix and its true adjoint.  Keeping the arctangent cell primitive avoids
the already known zero-radius local Taylor expansion.

The corresponding conditional scale theorem reduces to the estimate

\[
 \|DV(Y)H\|_{\alpha-\delta,\beta-\delta}
 \le C_{\rm tr}\epsilon(1+Y)^2\delta^{-1}
       \|H\|_{\alpha,\beta}.                           \tag{23.1}
\]

If (23.1) held uniformly on the reachable finite and limiting tubes, a
small fixed `epsilon` would leave positive regularity after the entire
finite feature clock and would give well-posedness, ordinary width
convergence, mesh removal, and raw-`K` continuity.  It is not currently a
theorem.  The exact differentiated word

\[
 G_1^*M_{\ell_2B_2}G_1M_{\partial_hX_1},
 \qquad B_2=D_2G_2^*(D_3A)+\cdots,
\]

exposes four source/carrier legs.  Naive reachable Wick grading gives a
`delta^-2`, not `delta^-1`, loss.  Improving it is precisely a
traffic/cavity contraction theorem, not a formal diagram identity.

A generic Hida or Vage multiplication theorem cannot replace this special
estimate.  For normalized Hermites `e_k` with weight `(k!)^s`, the leading
term in `e_k^2` forces any gap-`delta` multiplication constant to satisfy

\[
 \log C_{s,\delta}\ge c\delta\exp(c_s/\delta).
\]

With merely exponential chaos weights, multiplication is bounded only after
a fixed loss of at least `(log 2)/2`; successive Picard iterates consume
arbitrarily many such gaps.  Multiplying their coefficients by a fixed small
`epsilon` does not return them to the original space.  Hence generic
white-noise algebra is route-fatal, while a specially resummed reachable
traffic module remains open.

## 24. Classical Malliavin current-field nonclosability

There is a sharper obstruction to representing an adaptively reused
Ginibre action by an ordinary isonormal field plus finitely many Malliavin
response coordinates.  For one row, with
`gamma_j=sqrt(n) G_ij`, the exact Gaussian product formula is

\[
 (GX)_i=\delta(X/\sqrt n)
       +n^{-1/2}\sum_{j=1}^nD_jX_j.                  \tag{24.1}
\]

The second term is the diagonal/Onsager contraction.  On an
infinite-dimensional isonormal space with basis `e_j`, put

\[
 F_n={1\over n}\sum_{j=1}^nW(e_j)e_j .              \tag{24.2}
\]

For every fixed Malliavin order `m`,
`||F_n||_{D^{m,2}(H)}=O(n^{-1/2})`, but

\[
 \operatorname {Tr}(DF_n)=1,
 \qquad
 \delta(F_n)={1\over n}\sum_{j=1}^n(W(e_j)^2-1)
       \longrightarrow0,                             \tag{24.3}
\]

whereas the ordinary Gaussian product tends to one.  Therefore the
diagonal contraction, and hence the ordinary matrix action `delta+Tr D`,
is not closable in any fixed-order Gaussian Sobolev topology.  Chaos
weights depending only on chaos order do not help, because (24.2) lies
entirely in first chaos.

Adding finitely many derivative fields only moves the defect upward.  For
the probabilists' Hermite polynomial `H_r`,

\[
 Y_n^{(r)}={1\over r!n}\sum_{j=1}^nH_r(W(e_j))
\]

vanishes in every fixed lower-order seminorm while its `r`th diagonal
contraction equals one.  Propagating a genuinely nonlinear Nemytskii map
also generates all derivative orders through the Faà di Bruno formula.
Thus a classical Malliavin/Hida current state with finitely many response
levels cannot be the desired contract.  A full rooted traffic state may
retain all diagonal contractions, but then its nonlinear calculus,
tightness, uniqueness, and raw-square continuity still have to be proved;
calling the projective hierarchy one field does not establish those
bridges.

## 25. Weak-current and full-traffic trilemma

The exact rooted-open term algebra `T` has a current derivation `D` obtained
by the ordinary chain rule together with

\[
 D G_1=B_2\otimes X_1,\qquad D G_2=B_3\otimes X_2
\]

and the corresponding adjoint identities.  Consequently every finite
width current character satisfies the exact one-time hierarchy

\[
 {d\over ds}\tau_{n,s}(P)=\tau_{n,s}(DP),\qquad P\in\mathscr T. \tag{25.1}
\]

This is an algebraic identity, not yet a compact limiting IDE.  Three
natural topological realizations fail for different reasons.

1. Weak vector convergence plus weak-operator convergence is compact on
   bounded sets, but it does not make `(G,v) -> Gv` continuous.  For
   orthonormal `e_m`, the rank-one maps `T_m=e_0 tensor e_m` converge WOT to
   zero and `e_m` converges weakly to zero, while `T_m e_m=e_0`.  The raw
   square is lost as well.
2. A finite-depth Young/open-traffic enrichment is not invariant under
   `D`: differentiating a depth-`d` query creates deeper alternating
   forward/adjoint queries for every finite `d`.
3. The full separating marked traffic character retains every such query.
   With continuous iid node tags it separates all finite matrix entries up
   to layerwise permutation, and projectively it is the complete
   all-orders hierarchy.  Treating this as one symbol does not by itself
   prove a compressed topology, generator continuity, uniqueness, or raw
   square convergence.

Small fixed nonlinearity changes exponential coefficients but not the
Denjoy--Carleman class of a hierarchy: multiplication of the `r`th bound by
`epsilon^r` cannot turn a non-quasi-analytic sequence into a quasi-analytic
one.  The trilemma is scoped.  It does not exclude a nonseparating quotient
defined only on canonical reachable states, nor the already admissible
state consisting of fixed pointed sources plus current learned operators.
Such a quotient still needs a new reachable delocalization and hierarchy-
determinacy theorem; those properties cannot be inferred from weak
compactness or (25.1).

## 26. Compact-curvature residual audit

A fixed bi-Lipschitz residual

\[
 \phi_\epsilon(x)=x+\epsilon h(x),\qquad h''\not\equiv0,
\]

does preserve the deep-linear balance operators up to an explicit
`O(epsilon)` source.  For
`c_phi(z)=phi(z)-z phi'(z)` and

\[
 \mathcal D_3=A\otimes A-G_2G_2^*,\quad
 \mathcal D_2=G_2^*G_2-G_1G_1^*,\quad
 \mathcal D_1=G_1^*G_1-u\otimes u,
\]

the exact trace defects are

\[
 {d\over ds}\operatorname {Tr}\mathcal D_j
 =2\langle p_j,c_\phi(z_j)\rangle_n.                \tag{26.1}
\]

For `h=tanh`, `|c_phi|<=|epsilon|`.  This gives a controlled
balance perturbation, but it does not give a width theorem.  If `J` is an
interval on which `|h''|>=c`, then at canonical initialization a positive
fraction of the top preactivations lie in `J`, independently of the
Gaussian readout marks.  Consequently

\[
 \|D_z\{A\phi_\epsilon'(z)\}\|_{\ell_n^2\to\ell_n^2}
 =|\epsilon|\max_i|A_i h''(Z_{3,i})|
 \ge c|\epsilon|\sqrt{\log n}                       \tag{26.2}
\]

with probability tending to one.  Compact support or decay of curvature
does not change (26.2); it only selects a positive-density active set.

There are two further route-level failures.  The `L2` Taylor expansion of
`epsilon tanh(epsilon A)` has radius zero because Gaussian monomial norms
grow like powers of `sqrt(m)`.  And an adaptive Ginibre matrix is not
uniformly bounded on empirical `L^p`, `p>2`: choosing its own first row as
the input gives norm growth `n^(1/2-1/p)`.  These facts rule out transfer of
the deep-linear theorem by a fixed-`epsilon` ambient analytic or `L^p`
perturbation.  They do not show that the canonical residual trajectory
actually attains the worst adaptive alignment, and therefore are not an
activation-level impossibility theorem.

## 27. Bounded subcritical rational saturators

The unit-range normalization used in the first numerical comparison hid an
important distinction between a smaller gate coefficient and a better tail
exponent.  The fair two-parameter family is

\[
 \phi_{q,\lambda,c}(x)
 =c+\lambda\int_0^x(1+s^2)^{-q/2}\,ds,
 \qquad 1<q<2,                                      \tag{27.1}
\]

where `lambda>0` is fixed independently of width and trajectory, and

\[
 c>\lambda I_q,
 \qquad
 I_q=\int_0^\infty(1+s^2)^{-q/2}\,ds
 ={\sqrt\pi\,\Gamma((q-1)/2)\over2\Gamma(q/2)}       \tag{27.2}
\]

gives a strictly positive output floor.  Its exact structural data are

\[
 d(x)=\lambda(1+x^2)^{-q/2},\qquad
 {d'(x)\over d(x)}=-{qx\over1+x^2},
 \qquad
 d(x)^{-1}=\lambda^{-1}(1+x^2)^{q/2}.               \tag{27.3}
\]

Thus the features and all ordinary derivatives needed by the finite flow
are bounded, the log curvature is bounded, and the inverse gate is only a
degree-`q` polynomial weight at infinity.  The natural coordinate

\[
 H_q(x)=\lambda^{-1}\int_0^x(1+s^2)^{q/2}\,ds       \tag{27.4}
\]

satisfies `d H_q(u)/ds=Q1` exactly.  It is a primitive current functional,
not a history variable.  The exact autonomous state is therefore the same
four-species tuple `(A,L1,L2,H_q(u))` used for shifted arctangent, together
with the two fixed two-sided Gaussian sources.

There is a genuine exponent window here.  If `Z` is Gaussian (or has the
same moderate-moment scale), then

\[
 \|d(Z)^{-1}\|_{L^p}=O(p^{q/2}).                    \tag{27.5}
\]

Arctangent is the boundary `q=2`, where the cost is `O(p)`.  For every
`1<q<2`, a time-ordered term carrying one such endpoint cost per insertion
has the schematic size

\[
 {C^m m^{qm/2}\over m!},                            \tag{27.6}
\]

which is summable because `q/2<1`; at `q=2` it is merely geometric and
requires an additional smallness margin.  Bounded output, on the other
hand, fails at and below `q=1`.  Hence `(1,2)` is the only power-law window
that is simultaneously bounded-output and subcritical for this particular
chronological inverse-gate count.

This is not yet a convergence proof.  Formula (27.6) is useful only if the
reachable open-traffic/cavity expansion really has at most one inverse-gate
endpoint cost per chronological insertion.  A naive differentiation of the
middle true-adjoint query can expose several correlated source legs, and no
such all-order contraction estimate has yet survived audit.  Moreover,
normalizing (27.1) to a fixed output range multiplies the gate by `I_q^{-1}`;
as `q` decreases to one this makes all lower-layer velocities small.  The
activation must therefore be compared at fixed `lambda` (with `c` adjusted
to retain a positive floor) when deciding whether the exponent gain is real
rather than suppressed feature learning.

At small `lambda`, if `mu_q=E(1+Z^2)^{-q}>0`, the initialization scales are

\[
 \|G_2'\|_F^2=\Theta(\lambda^2\mu_q),\quad
 \|G_1'\|_F^2=\Theta(\lambda^4\mu_q^2),\quad
 \|u'\|_n^2=\Theta(\lambda^6\mu_q^3).               \tag{27.7}
\]

They have strictly positive width limits for every fixed `lambda>0` and
fixed `q>1`; the family is not lazy in the width limit.  The remaining
Phase-I decision is whether the one-cost property needed for (27.6) is
true.

A derivative-amplitude-matched stress run used `lambda=1/8` for
`q=4/3,3/2`.  At widths 256, 512, and 1024 the initialization Frobenius
speeds of both learned matrices and the normalized input-vector speed
stabilized at nonzero constants; they were slightly larger than for the
existing shifted-arctangent normalization.  Through feature clock `1.5`,
single-row and single-column resampling retained the predicted
`n^{-1/2}` scale at widths 64, 128, and 256, with constants comparable to
shifted arctangent.  This removes the simple “the candidate only looks
stable because its derivative was normalized to zero” explanation, but it
does not prove the all-order contraction behind (27.6).

## 28. Finite cotangent-orbit rigidity

Activation choice cannot make the immutable Gaussian source finite-rank in
time.  The following scoped theorem makes that statement precise.  Consider
the direct scalar top cell

\[
 \dot a=\phi(z),\qquad \dot z=Q a\phi'(z),\qquad
 b=a\phi'(z),qquad Q>0.                             \tag{28.1}
\]

Let `phi` be `C1`, and suppose the flow has a common local strip for all
initial data under consideration (or a uniform finite-rank germ at
arbitrarily large initial `a`).  If the functions of the initial state

\[
 \{b\circ\Phi_t:|t|<\epsilon\}                     \tag{28.2}
\]

span a fixed finite-dimensional space, then `phi` is affine.

Here is the proof skeleton.  On a component where `phi'` is nonzero, set

\[
 h'(z)=1/\phi'(z),\quad \tau=h(z),\quad
 s(\tau)=\phi'(h^{-1}\tau),\quad
 P(\tau)=\phi(h^{-1}\tau).
\]

Then `P'=s^2`; with `v=Qa`, (28.1) becomes

\[
 \dot\tau=v,\qquad \dot v=QP(\tau),\qquad b=vs/Q.  \tag{28.3}
\]

Starting from `v(0)=Lambda` and observing at `t=r/Lambda` shows that a
finite rank in (28.2) forces the translate kernel `s(tau+r)` to have finite
rank.  A continuous function with finite-dimensional local translate span
is an exponential polynomial.  The finite Koopman space is invariant under

\[
 D=v\partial_\tau+QP(\tau)\partial_v.
\]

Cayley--Hamilton gives a constant-coefficient relation among `D^k(vs)`.
The coefficient of its highest `v` power is `s^(k)`, so `s` is a polynomial.
If `deg s=r>=1`, assign weights `wt(tau)=1`, `wt(v)=r+1`.  The leading
derivation raises weight by `r`, and every iterate of the leading monomial
`v tau^r` is nonzero with one-sign coefficients.  The iterates therefore
have strictly increasing weights, a contradiction.  Thus `s` is constant;
continuity across components makes `phi` affine globally.

For a Gaussian layer, the orthogonal source contribution to the cotangent
has covariance `E[b(s)b(t)]`.  The theorem makes that kernel infinite-rank
for every covered genuinely nonlinear activation.  Therefore no exact
closure may integrate out the initial Gaussian matrix into finitely many
regular Gaussian innovation/query modes.  This is fully consistent with
the user's admissible contract: retaining one immutable *full two-sided
source operator*, available on every current query together with its true
adjoint, escapes the theorem.  The result rules out a tempting smaller
contract; it is not an impossibility theorem for the fixed-source operator
IDE.

## 29. Middle-cutoff bootstrap boundary

The successful depth-two cutoff strategy does not extend from scalar energy
alone.  For arctangent write

\[
 d(z)={a\over1+z^2},\qquad {|d'(z)|\over d(z)}\le1.
\]

If `b=d(z)r`, the componentwise clipped map is dimension-free Lipschitz:

\[
 |\operatorname {clip}_L(d(z)r)-
   \operatorname {clip}_L(d(w)\widetilde r)|
 \le a|r-\widetilde r|+L|z-w|.                     \tag{29.1}
\]

This is enough to identify a fixed-cutoff, fixed-mesh limit and then remove
the mesh.  The constant grows like `L`, however.  A radial `L2` cutoff does
not repair it: on one coordinate take `w=-n^(1/4)`, `z=0`, and
`r=(1+sqrt(n))/a`.  The normalized input perturbation tends to zero and the
two multiplier outputs stay on a bounded `L2` ball, but their normalized
difference stays order one.

Even square-tail uniform integrability does not supply a cutoff-uniform
Osgood modulus.  Put `n_k` comparable to `e^k`, use one coordinate with
`w=0,z=1`, and take `r=M_k/a`, `M_k=sqrt(n_k/k)`.  The tail square mass is
`O(1/k)`, hence tends to zero, while an input error `e_k=1/n_k` produces an
output square error comparable to `1/k`, only `1/log(1/e_k)`.  This modulus
is not Osgood.  The feature identity `f'=K` bounds the time integral of
`||B2||_2^2`; it supplies neither a coordinate tail modulus nor a bound on
spikes between auxiliary mesh points.  Differentiating

\[
 R_2'=\|B_3\|_2^2X_2+G_2^*B_3'                     \tag{29.2}
\]

merely creates a new adaptive adjoint query not present in `K`.

For the rational gate `d_q=epsilon(1+z^2)^(-q/2)`, `1<q<2`, desaturation
costs `|delta z|^q` rather than `|delta z|^2`.  A uniform
`L^(2+eta)` carrier bound would therefore suffice for cutoff removal when

\[
 q\le1+\eta/2.                                      \tag{29.3}
\]

Bare energy gives only exponent two.  Thus the rational window reduces the
precise moment that a source/traffic argument must prove, but a cutoff
bootstrap cannot manufacture that moment.  This is a route-level
impossibility, not a counterexample to the canonical Gaussian trajectory.

For the logarithmic gate

\[
 d_\beta(x)={\lambda\over\sqrt{1+x^2}
 [\log(e+x^2)]^{1+\beta}},\qquad\beta>0,
\]

desaturation grows only like `|x|(log|x|)^(1+beta)`.  For every fixed
`eta>0`, its square is bounded by `C_(eta,beta)(1+|x|^(2+eta))`.
Consequently *any* genuine excess-moment estimate of order `2+eta` would
remove this gate cutoff.  Square UI still does not: choose `a_n` so that
`d_beta(0)/d_beta(a_n)=sqrt(n)`; then `a_n/sqrt(n)->0`, while one coordinate
of the desaturated output has normalized size one.  The composed candidate
of Section 30 has desaturation `|x|(log|x|)^(3/2)` and inherits the same
“any positive excess moment suffices” advantage.  This strictly improves
the raw `q=3/2` gate, which needs third-moment control.

## 30. Composed near-critical bounded candidate

A composition improves the rational tail exponent without shrinking the
gate at typical Gaussian coordinates.  Let

\[
 F(v)=\int_0^v(1+s^2)^{-3/4}\,ds,qquad
 \boxed{\phi_\star(x)=1+\frac18F(\operatorname {arsinh}x).} \tag{30.1}
\]

Since `I_(3/2)=int_0^infinity(1+s^2)^(-3/4)ds` is approximately
`2.62206`, the range of `phi_star` is contained in
`[0.67224,1.32776]`.  In particular it has a fixed positive floor.  Its
gate is

\[
 d_\star(x)=\frac1{8\sqrt{1+x^2}
 (1+\operatorname {arsinh}^2x)^{3/4}},               \tag{30.2}
\]

so `d_star(0)=1/8`, independent of width, and

\[
 {d_\star'(x)\over d_\star(x)}
 =-{x\over1+x^2}
 -{3\operatorname {arsinh}x\over
  2(1+\operatorname {arsinh}^2x)\sqrt{1+x^2}}        \tag{30.3}
\]

is bounded.  The exact natural coordinate is the fixed primitive

\[
 H_\star(x)=8\int_0^x\sqrt{1+s^2}
 (1+\operatorname {arsinh}^2s)^{3/4}\,ds,             \tag{30.4}
\]

and again `H_star(u)'=Q1`.  No polynomial or time expansion of this cell is
needed.

For a standard Gaussian `Z`,

\[
 \|d_\star(Z)^{-1}\|_{L^p}
 \asymp \sqrt p\,(\log p)^{3/2}.                     \tag{30.5}
\]

This is strictly smaller than `p^(q/2)` for every raw rational exponent
`q>1`, and much smaller than arctangent's order `p`, while `phi_star`
remains bounded and has a derivative of the same numerical scale at the
origin.  Under the still-unproved one-endpoint-cost grammar, the chronological
majorant becomes

\[
 {C^m m^{m/2}(\log m)^{3m/2}\over m!},               \tag{30.6}
\]

which is supergeometrically summable.

Finite-width diagnostics do not reveal a degeneracy: the initial speeds of
`G2`, `G1`, and `u` stabilize at nonzero width limits, and through feature
clock `1.5` every tested single-row/column perturbation remains on the
`n^(-1/2)` scale at widths 64, 128, and 256.  The constants are comparable
to shifted arctangent.  Thus (30.1) is the current activation-selection
leader on local tail balance.  It is not frozen until the independent audit
either proves or refutes the one-cost open-traffic contraction; boundedness
and (30.5) alone do not control an adaptively aligned transpose query.

## 31. Quantitative tensor-program literature boundary

The current source-word obligation cannot be imported from a fixed-program
limit theorem.  The primary quantitative theorem in *Quantitative
Gaussian-Process Limits of Tensor Programs* (arXiv:2607.06290, Theorem 1.2)
gives an `O(n^(-1/2))` Wasserstein estimate for a **fixed** Netsor program.
Its constant depends on the number of program lines and the remaining
structural data.  Weight sharing is allowed, but the theorem is aimed at
fixed GP/NTK programs and does not provide a bound uniform when the number
of chronological insertions grows like `log n`.  Tensor Programs IVb
(arXiv:2308.01814) likewise identifies fixed finite transpose-reusing
programs; it does not supply an exact continuous-time feature-learning
remainder.

This distinction is material.  The candidate proof needs the triangular
estimate

\[
 \sup_{m\le c\log n}\|W_{m,n}\|_{L^2}
 \le \text{an explicitly summable function of }m                  \tag{31.1}
\]

and then a uniform tail estimate for all larger chronological orders before
interchanging width and the infinite series.  Convergence for each fixed
`m`, even with a sharp `n^(-1/2)` rate whose hidden constant is allowed to
depend arbitrarily on `m`, does not imply (31.1).  Thus the literature
validates the fixed-mesh rung C3 but leaves exactly the C3-to-C4 bridge under
audit here.

## 32. Hostile audit of the one-root grammar

The narrow gate-counting claim survives, but it does not imply the needed
probabilistic bound.  In physical coordinates put

\[
 K_2=c_1I+G_1D_1^2G_1^*,\qquad
 K_3=c_2I+G_2D_2K_2D_2G_2^* .                       \tag{32.1}
\]

Then `Z2'=K2 D2 G2^*D3 A` and `Z3'=K3D3A`.  In the
natural-coordinate equation for `h3`, the `c1 I` part of (32.1) contains,
for `i!=k`, the exact open summand

\[
 T_{ik}=c_1{d(Z_{3k})\over d(Z_{3i})}A_k
 \sum_jd(Z_{2j})^2(G_2)_{ij}(G_2)_{kj}.              \tag{32.2}
\]

At initialization the last sum is an off-diagonal weighted Wishart entry.
Conditioning on one row leaves a nondegenerate Gaussian projection of the
other row, while `A_k` is an independent Gaussian carrier.  Thus a source
estimate must control both the open carrier and the two-sided row
contraction; it cannot charge only the endpoint inverse.

There is no second inverse-gate counterterm.  An open edge contributes an
inverse gate at its target and a gate at its source, so internal ratios
cancel along a chain.  More generally the local factor at an `r`-fold
differentiated source is

\[
 d(z)^{-r}\{d(z)\partial_z\}^{r}d(z),                 \tag{32.3}
\]

which is bounded (indeed decaying) for both the rational and composed
near-critical gates.  What fails is the leap from (32.3) to an absolute
moment majorant.  At fixed width, high moments of the Wishart term see
repeated-edge collisions even though each fixed-order term is suppressed
as width tends to infinity.  Alternating `i,k` factors cancel the gate
ratio and leave powers of the same Wishart entry.

Keeping the full Gram blocks in (32.1), rather than expanding their
individual edges, may resum these collisions because their operator norms
are bounded.  That is now the focused route.  It still must prove that the
remaining diagonal carrier multiplications and learned `P/P*` descendants
have a summable stopped expansion uniformly through order `O(log n)`.
Equation (32.2) is therefore a proof-route obstruction, not a counterexample
to the canonical Gaussian trajectory or to width convergence itself.

## 33. Finite gate-algebra route: a scoped impossibility theorem

There is no remaining smooth nonlinear witness whose multiplier gates close
in a finite-dimensional ordinary pointwise algebra.  Indeed, if such a
unital algebra contains

\[
 h=(\phi')^2,
\]

then the powers of `h` are linearly dependent, so `p(h)=0` for a nonzero
polynomial `p`.  A continuous `h` consequently has connected finite range
and is constant.  The Darboux property of derivatives then makes `phi'`
constant (including its sign), hence `phi` is affine or constant.  A finite
differential lift does not evade this: multiplication by `h` generates all
powers of `h`; for example the two-component sine/cosine differential lift
is not a finite multiplication algebra.

Finite-valued nonsmooth gates fail dynamically instead.  Transport of a
step gate through a switching surface produces a boundary distribution
`delta`, and repeated transport produces all normal derivatives of that
distribution.  Equivalently, exact sector-moment evolution needs the
current boundary density and then its full normal-trace hierarchy.  Freezing
the sectors suppresses precisely the feature evolution required here.

The apparently strongest loophole, `|phi'|=c` almost everywhere, is also
inadmissible.  If such a locally Lipschitz activation is injective it is
monotone and affine; otherwise it has a fold.  For the local model
`phi(x)=|x|`, a width-two network has an open set of states in which a probe
coordinate reaches the cusp while its backpropagated velocity points into
the cusp, remains there while an active path reverses the velocity sign, and
then admits sticking, either signed departure, or delayed departure.  Two
oppositely signed regularized histories coalesce at the same cusp state and
later separate.  Hence a current-state differential inclusion is nonunique,
whereas a smoothing-selected continuation needs the erased incoming branch
and is not restartable.  The strict inequalities defining this construction
persist on an open parameter set and therefore have positive probability
under the canonical Gaussian initialization.

This proves a scoped no-go for deep-linear-style finite gate/Gram closures,
including smooth finite algebras, ReLU/leaky-ReLU splines, absolute value,
and triangle-wave folds.  It is not an impossibility theorem for the full
current pointed-operator law: that route retains an infinite functional
calculus inside a fixed number of operator species and still faces the
middle-carrier estimate (6.2).

## 34. Whole-neuron cavity and the first nonlocal response sandwich

Removing one outgoing column of the second immutable Gaussian matrix and
the corresponding receiving row of the first matrix does not close the
middle-carrier estimate.  A column cavity for a source column `C_j` makes

\[
 C_j^*B_3=C_j^*B_3^{[j]}+C_j^*(B_3-B_3^{[j]})        \tag{34.1}
\]

conditionally Gaussian only in its first term.  The response energy of the
second term contains

\[
 \sum_i |B_{2,i}|^2|\Delta_j Z_{2,i}|^2.             \tag{34.2}
\]

Resampling the receiving row that generates `Z_(2,i)` removes the direct
row correlation, but it does not remove the distinct source column `C_i`
inside

\[
 R_{2,i}=C_i^*B_3+P_2^*B_3.                          \tag{34.3}
\]

The same `C_i` returns through `B_(2,i)` in the learned row evolution and
therefore also enters `Delta_j Z_(2,i)`.  Decoupling (34.2) consequently
requires a third cavity column, and then a fourth, producing an all-order
alternating row/column hierarchy.  Summing over the new neuron index makes
each generation order one; there is no extra `n^(-1/2)` after aggregation.
The small gate contributes powers of the fixed activation amplitude and the
physical loss gives a finite total feature clock, so a convergent cluster
sum remains possible.  Neither fact proves the all-order majorant.

The same obstruction appears without cavity notation.  After every local
natural-coordinate shear is conjugated away, the first surviving middle
round trip in the response equation is, up to bounded diagonal factors,

\[
 \mathcal T_2 h
 =G_1^*M_{(\phi''(Z_2)/\phi'(Z_2))B_2}G_1D_1^2h.       \tag{34.4}
\]

For the composed candidate the logarithmic gate derivative is bounded, but
the multiplier `B2` is not.  A scalar `L^(2+eta)` estimate does not control
`||B2 h||_2`: Holder asks for `h` at exponent
`2(2+eta)/eta`, and that response equation contains (34.4) again.  Iteration
therefore asks for all response exponents.  A single Malliavin derivative is
the same failure in Gaussian-divergence form: applying a reused true adjoint
to a source-dependent response requires its next source derivative.

This is a proof-hierarchy statement, not a failure of the proposed Markov
contract.  The contract retains the full immutable jointly realized source
operators `Gamma_1,Gamma_2` and their adjoints.  If two source matrices agree
on the currently queried vectors but disagree on a new direction, they are
different fixed model data and the restart map is allowed to distinguish
them.  Likewise the current learned operator `P_j` may be applied
extensionally without retaining its rank-one creation history.  Conditional
variance left after conditioning on finitely many queries therefore refutes
only finite-innovation or finite-query closures; it does not refute the
five-species state coupled to the full fixed source actions.

The surviving positive obligation is now precise: prove an all-order
row/column cluster estimate, or an equivalent current weighted invariant,
which is summable uniformly in width and yields (6.2).  Packaging the
unproved hierarchy in an analytic norm is not itself that proof.

## 35. Finite local coercive lifts: exact entropy and scoped no-go

There is a useful exact entropy for the middle scalar cell, but it also
shows why no finite list of local moments closes the true-adjoint forcing.
Write

\[
 D=\phi'(Z_2),\qquad B_2=DR,qquad Z_2'=K_2B_2,qquad
 R'=F,\quad K_2\ge0.                                  \tag{35.1}
\]

For every `p>1` and `c>0`,

\[
 \mathcal E_{p,c}
 ={1\over p}\langle |R|^p\rangle-c\langle R,X_2\rangle
\]

satisfies the exact identity

\[
 \mathcal E_{p,c}'
 =\langle |R|^{p-2}R-cX_2,F\rangle
 -c\langle B_2,K_2B_2\rangle.                        \tag{35.2}
\]

Thus the cross term cancels the complete local Gram transport, not merely
its diagonal part.  In the actual network, however,

\[
 F=X_2\|B_3\|_2^2+G_2^*B_3'.                         \tag{35.3}
\]

The adjoint contribution to (35.2) requires

\[
 \|G_2(|R|^{p-2}R)\|_2
 \le\|G_2\|_{\rm op}\|R\|_{2p-2}^{p-1}.             \tag{35.4}
\]

Consequently `p=2+eta` asks for `2+2eta`, then `2+4eta`,
and so on.  More generally, a one-function Orlicz entropy `H` can pair with
an arbitrary `L2` forcing in the same energy only if
`|H'|^2 <= C(1+H)`, which forces `H` to have at most quadratic growth.
It cannot supply square equiintegrability.

The coordinate-free tangent calculation gives the same verdict.  For the
natural tangent `v=D^(-1) delta Z2`, after the local characteristic has been
removed, the surviving homogeneous term is

\[
 v'=D^{-1}\{K_2M_{\phi''B_2}-M_{\phi''(K_2B_2)}\}v.  \tag{35.5}
\]

The scalar part of `K2` cancels.  A nonlocal Gram part leaves a genuine
operator--diagonal commutator.  Adjoining finitely many current `K2`-words
does not help: differentiating a maximal word creates one longer word, and
generic Gram and diagonal matrices generate a width-growing algebra.  A
finite invariant local word list therefore requires `phi''=0` (affine) or
a diagonal Gram, neither of which is the target network.

This rules out finite local coercive or trigonometric/hyperbolic lift
mechanisms under arbitrary Gram and `L2` adjoint forcing.  It does not rule
out a Gaussian-specific all-order cluster or renormalized-flow theorem that
uses the full fixed source actions as proof data.

## 36. Rejection of the first connected-traffic contraction

The first proposed all-order repair assigned two Gaussian carrier letters and
two gate factors to every new feedback generation.  That degree count is
false for the exact depth-three vector field.  Write

\[
 D_j=\operatorname {diag}\phi'(Z_j),\qquad
 C_j=\operatorname {diag}{\phi''(Z_j)\over\phi'(Z_j)},
 \qquad \alpha_j=\langle X_j^2\rangle_n,
 \quad \beta_j=\langle B_j^2\rangle_n .              \tag{36.1}
\]

With `V2=Z2'` and `V3=Z3'`, exact differentiation gives

\[
\begin{aligned}
 V_2&=\alpha_1B_2+G_1D_1^2Q_1,\\
 V_3&=\alpha_2B_3+G_2D_2V_2,\\
 B_3'&=D_3X_3+C_3(B_3\odot V_3),\\
 B_2'&=C_2(B_2\odot V_2)
       +D_2\{\beta_3X_2+G_2^*B_3'\},\\
 Q_1'&=\beta_2X_1+G_1^*B_2'.                         \tag{36.2}
\end{aligned}
\]

In particular, `Q1'` contains both

\[
 G_1^*M_{C_2B_2}G_1D_1^2Q_1                         \tag{36.3}
\]

and

\[
 G_1^*D_2G_2^*\{C_3B_3\odot
   G_2D_2G_1D_1^2Q_1\}.                              \tag{36.4}
\]

At initialization, (36.3) already substitutes

\[
 B_2=D_2\Gamma_2^*D_3A,
\]

so one application contains `Gamma1*`, `Gamma1`, `Gamma2*`, and the
unbounded endpoint mark `A`; (36.4) contains four explicit matrix actions
before the endpoint carrier is counted.  The learned `P/P*` expansion adds
rank-one variants but does not delete these pure-source summands.

Consequently the proposed estimate

\[
 \|T_r\|_{L^p}\le { (C\lambda^2S)^r\over r!}
 \|1+\|\Gamma_1\|+\|\Gamma_2\|\|_{L^{2rp}}^{2r}
                                                               \tag{36.5}
\]

does not majorize the actual order-`r` contribution.  Calling `B2` a
bounded internal decoration is exactly the missing theorem: multiplication
by `B2` is not bounded on a fixed empirical `L^p` space.  For
`b=v=n^(1/p)e1`, both `||b||_(p,n)` and `||v||_(p,n)` equal one, whereas
`||b v||_(p,n)=n^(1/p)`.  An `L^(2+eta)` estimate for `B2` therefore cannot
close (36.3) in the same exponent.

The accompanying blanket collision estimate is also invalid.  For real
Ginibre `G`,

\[
 {1\over n}\mathbb E\operatorname {Tr}(G^*G)^2=2+{1\over n},    \tag{36.6}
\]

and the two order-one terms include the palindromic true-adjoint return.
These leading Onsager pairings must be part of the limiting traffic object;
they are not `O(r^2/n)` errors.  A fixed-order traffic limit followed by a
genuine summable majorant would need no uniform collision rate, but (36.5)
is not that majorant.

Thus the gate-ratio invariant and the finite-clock small parameter survive,
while the claimed Banach contraction, cutoff-independent Euler estimate,
and `B2` excess-moment consequence are retracted.  The next repair must
control the complete source degree of (36.3)--(36.4), for example in a
factorially weighted source scale or by a direct reachable `psi_1` theorem;
it may not assume that the middle multiplier is bounded.

## 37. Residual-erf block resummation: hostile weighted-Wishart audit

The strongest residual competitor tested was

\[
 \phi_\epsilon(x)=x+\epsilon\int_0^xe^{-s^2}\,ds,
 \qquad d_\epsilon(x)=1+\epsilon e^{-x^2}.            \tag{37.1}
\]

Its bi-Lipschitz natural coordinate is an exact and useful local
resummation, and the deep-linear part of the flow remains available as a
propagator.  A proposed proof then treated every interrupted `G*/G`
backtrack as a bounded deep-linear Gram block.  The following leading
diagram disproves that estimate.

At initialization put `D=D1^2`, let `g_i*` be row `i` of `G1`, and define

\[
 h_i=\left[{\phi''(Z_2)\over\phi'(Z_2)}B_2\right]_i
     =\phi''(Z_{2,i})R_{2,i}.                         \tag{37.2}
\]

Conditional on the forward weights, `R_(2,i)` is Gaussian in the independent
readout `A`, with a nondegenerate variance on a positive fraction of rows.
For the symmetric sandwich

\[
 \widetilde S=D^{1/2}G_1^*M_hG_1D^{1/2},             \tag{37.3}
\]

the same-row contribution to its `2k`th normalized trace is

\[
 \mathcal D_{2k,n}={1\over n}\sum_i
 h_i^{2k}(g_i^*Dg_i)^{2k}.                            \tag{37.4}
\]

Choose a fixed interval on which `|phi''|>=c epsilon`.  With probability
tending to one, a positive fraction of rows lie in that interval and have
both the conditional variance and `g_i*Dg_i` bounded below.  Gaussian
conditioning then gives

\[
 \mathbb E_A\mathcal D_{2k,n}
 \ge c_0(c_1\epsilon)^{2k}(2k-1)!! .                 \tag{37.5}
\]

This is order one in width: the normalized trace costs `1/n`, while there
are `n` choices of the reused row.  It is neither an accidental lower-order
collision nor removed by normalized `L2`, Frobenius, operator, or ordinary
Gram stops.  It proves that the interrupted block has an unbounded
sub-Gaussian carrier scale, rather than the order-independent bound used in
the proposed remainder.

Rank-one updates do not turn the decoration into an ordinary Gram scalar:

\[
 (b\otimes x)^*M_h(b\otimes x)
 =(x\otimes x)\langle b,hb\rangle_n,                 \tag{37.6}
\]

and the displayed scalar is a new decorated cubic statistic.  Iteration
produces all weighted moments.  The advertised skeleton count had already
spent its time-simplex factorial; after (37.4) is restored, the remaining
Wick multiplicity is not covered by its geometric majorant.  Fixed-order
Hermite/traffic convergence can evaluate every fixed `k`, but it supplies
no uniform tail allowing the fixed-order and exact-time limits to be
interchanged.

This audit retracts the claimed residual-erf cluster theorem, not the exact
natural-coordinate identities and not every possible signed or
width-first resummation.  A repair would have to keep the weighted-Wishart
block in its true tail class and prove a summed chronological estimate,
rather than call it a bounded copy of the deep-linear Gram operator.

## 38. Shifted-tanh high temperature: exact reduction and operator-tail boundary

The two-parameter bounded candidate

\[
 \phi(x)=c+\lambda\tanh(\kappa x),\qquad
 0<\lambda<c,\quad 0<\kappa\le1,                     \tag{38.1}
\]

separates feature amplitude from curvature scale:

\[
 d=\lambda\kappa\operatorname {sech}^2(\kappa x),
 \qquad {d'\over d}=-2\kappa\tanh(\kappa x).          \tag{38.2}
\]

The positive floor bounds the total absolute feature clock, all three
trained hidden blocks move by fixed nonzero powers of `lambda*kappa`, and
the logarithmic gate derivative is bounded.  Moreover the learned part of
the middle carrier is pointwise harmless.  Indeed,

\[
 P_2(s)^*B_3(s)=\int_0^sX_2(r)
     \langle B_3(r),B_3(s)\rangle_n\,dr,              \tag{38.3}
\]

so, if `M=c+lambda`,

\[
 \sup_{s\le S}|(D_2P_2^*B_3)_i(s)|
 \le(\lambda\kappa)^3MS
       (\|A_0\|_{2,n}+MS)^2.                         \tag{38.4}
\]

Thus the unresolved carrier is exactly
`D2 Gamma2* D3 A`, not the trained rank-one correction.

An absolute exponential-operator proof nevertheless fails already at
initialization.  Put `w=(d2'/d2)B2`.  The exact middle response block is

\[
 T_2=\Gamma_1^*M_w\Gamma_1D_1^2.                     \tag{38.5}
\]

Condition the forward projections in compact intervals where all gates are
bounded below and `d2'/d2` has fixed nonzero sign.  Orthogonal Gaussian
decomposition of one `Gamma1` row and one `Gamma2` row leaves independent
variables `h` and `eta` for which a symmetric conjugate of (38.5) has the
lower bound

\[
 \|T_2\|_{\rm op}\ge
 c\eta_+\|h\|^2-C(1+\eta_+)(1+\|h\|)                 \tag{38.6}
\]

on a positive-probability cylinder.  Consequently, for every fixed
nonzero `lambda,kappa` and every `theta>0`,

\[
 \mathbb E\exp\{\theta\|T_2(0)\|_{\rm op}\}=\infty. \tag{38.7}
\]

Subtracting the covariance/Onsager mean does not repair this: the centered
term still contains
`eta (||h||^2-E||h||^2)`.  Hence a termwise absolute Dyson estimate in an
exponential operator norm has zero radius.  Small activation parameters
multiply this variable but cannot create an exponential moment.

This is deliberately not promoted to a canonical no-go.  Equation (38.7)
concerns a worst spectral direction at each finite width; it neither
disproves moderate empirical moments through `p=O(log n)` nor exhibits a
concentration defect in the actual state or raw kernel.  It rules out only
the absolute-operator/finite-response proof architecture.  A surviving
high-temperature route must be width-first and typical-coordinate: it must
show that the canonical evolution cannot align with the rare centered
weighted-Wishart direction, while retaining the exact current operators
`P1,P2` rather than expanding them into forbidden two-time kernels.
