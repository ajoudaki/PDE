# Proof-only adversarial audit

**Verdict: PASS.** All mathematical claims of the stated standalone two-driver theorem are justified. No mathematical correction is required.

Candidate audited: `/tmp/l3-two-sample-Un7kw9/CONVEX_SLOPE_TWO_DRIVER_RESPONSE.md`.

Candidate length: **378 lines**.

Candidate SHA-256:

```text
52fa972f19cd4f4aa28dc5fdc43611e441f0bb00a8822c6377defb5a44aa4305
```

## Exact scope and method

This verdict concerns the system

\[
M'=a(M)p+Vb(M)q,\qquad V'=a(M)q,
\quad a(M)=1+e\arctan M,\quad b(M)=\frac{e}{1+M^2},
\]

with the candidate's fixed parameter \(e=1/10\), arbitrary real initial data, arbitrary signed \(p,q\in L^1(0,T)\), and fixed finite time horizon. It includes global existence and uniqueness, both coordinate changes, the polynomial state bounds, and the actual joint Fréchet derivative from \(\mathbb R^2\times L^1(0,T)^2\) to continuous physical trajectories. It also includes the auxiliary-coordinate derivative bounds and the conditional finite-moment conclusion.

The probabilistic verdict is conditional on (23), or the explicitly sufficient individual square-exponential moment assumptions. It does not assert Gaussian or square-exponential tails for the output derivatives. It does not establish input tails for an application, a network theorem, an arbitrary-angle embedding, higher derivatives, or population continuation.

I read `/etc/codex/skills/solve-math-rigorously/SKILL.md` in full and all 378 lines of the candidate. The audit used direct algebra and proof reasoning only: no agents, experiments, network access, other mathematical files, history, or earlier reviews. The candidate was not edited. Its references to a supplied note at lines 109 and 378 are provenance statements, not mathematical premises used here; their historical accuracy is outside this audit.

## 1. Activation, nonsingularity, and forced invariant — PASS

The activation derivatives at lines 26–37 are correct. In particular,

\[
\frac{d}{dM}\left(M\arctan M-\tfrac12\log(1+M^2)\right)=\arctan M.
\]

Thus \(\ell=1-e\pi/2>0\), \(\ell\le a\le L\), and \(b>0\). These establish global Lipschitz continuity and strict convexity of the activation. Further positive-order derivatives are bounded: derivatives of \(b\) are rational functions without real poles that decay at infinity. The nonlinear part is unbounded with linear growth, as stated.

The antiderivative (2) is correct. The relevant integration-by-parts identity follows from

\[
\frac{H(M)}{1+M^2}=\frac M3+\frac{2M}{3(1+M^2)}.
\]

It gives exactly \(U'=2a(1+M^2)/e=2a/b\). The lower bound \(U'\ge2\ell/e>0\) implies strict monotonicity, divergence to the corresponding infinities at both ends of the real line, and a smooth inverse. The absolute-value bounds (3) hold also for negative \(M\), by reversing the orientation of the integral. No division by \(M\) or by a vanishing derivative occurs.

For an absolutely continuous solution, the chain rule yields

\[
I'=U'(M)M'-2VV'
=\frac{2a}{b}(ap+Vbq)-2Vaq
=\frac{2a^2}{b}p.
\]

The cancellation is exact for signed drivers. The map \((M,V)\mapsto(U(M)-V^2,V)\) is globally invertible with the stated inverse and determinant \(U'(M)>0\). Here “forced invariant” means precisely (4); conservation is asserted only when its forcing vanishes.

The differentiation in (5) correctly uses the invariant coordinate \(u\):

\[
\frac{dk}{du}
=\frac{4a-2a^2b'/b^2}{2a/b}
=2b-a\frac{b'}b
=\frac{2e+2aM}{1+M^2}.
\]

The bound \(|k'|\le2e+L\) follows from \(2|M|/(1+M^2)\le1\). Moreover,

\[
|M|^2\le\left(\frac{3e}{2\ell}|u|\right)^{2/3},
\qquad k(u)=\frac2e a(M)^2(1+M^2),
\]

which proves (6) with the candidate's explicit constant. Neither the positivity of \(k\) nor this growth bound assumes \(u\ge0\).

## 2. Polynomial state estimate — PASS

The bound \(|V(t)|\le K=|V_0|+LQ\) uses only \(|a|\le L\). For the constant \(D=1+K^2\) and \(W=D+|I|\), one has

\[
|U(M)|=|I+V^2|\le |I|+K^2=W-1.
\]

The absolute value of an absolutely continuous function is absolutely continuous, including across zeros. Consequently, almost everywhere,

\[
W'\le |I'|\le C_k\bigl(1+|U(M)|^{2/3}\bigr)|p|
\le 2C_kW^{2/3}|p|.
\]

Because \(W\ge1\), composition with the cube root and integration are legitimate without a singularity. They give exactly (8). Combining \(|U(M)|\le B^3\) with the cubic lower bound in (3) gives (9).

The reduction to (10) is also valid:

\[
1+K^2+|I_0|
\le C_e(1+|M_0|^3+V_0^2+Q^2),
\]

where the linear \(|M_0|\) term from (3) is absorbed into \(1+|M_0|^3\). Cubing (8) with \((x+y)^3\le4(x^3+y^3)\) supplies the \(P^3\) term. Since \(R\ge1\), (10) and the bound on \(V\) imply both parts of (11). These constants depend only on the fixed activation parameter, with no hidden dependence on time or driver ordering.

There is no circular existence argument: these are a priori bounds, and the next section constructs the global solution independently.

## 3. Cubic transform, both vector fields, and global existence — PASS

The cubic map \(H\) is onto, strictly increasing, and smooth with \(H'\ge1\). Direct substitution gives

\[
h'=a(M)(1+M^2)p+eVq,\qquad V'=a(M)q.
\]

The identity \((1+M^2)b=e\) is exact. With \(m=H^{-1}\), differentiation gives

\[
f'(h)=\frac{e+2a(M)M}{1+M^2},\qquad
g'(h)=\frac{e}{(1+M^2)^2}.
\]

Thus \(|f'|\le C_0=e+L\) and \(|g'|\le e\). More explicitly, for \(x=(h,V)\),

\[
DX=\begin{pmatrix}f'&0\\0&0\end{pmatrix},\qquad
DY=\begin{pmatrix}0&e\\g'&0\end{pmatrix}.
\]

Their induced one-norms are at most \(C_0\) and \(e\). Integrating the derivative along a line segment proves global Lipschitz continuity of each vector field on all of \(\mathbb R^2\). Both values at the origin have one-norm one, so the stated linear-growth conclusion holds as well.

The existence argument at lines 198–204 checks the necessary hypotheses. On a closed subinterval, the integral operator maps every continuous path to a continuous path: its image is an integral of an \(L^1\) function, since continuous paths are bounded. Its contraction factor is at most the integral of \(C_0|p|+e|q|\). Integrability permits a finite partition with each such integral less than one. Geometric convergence in the complete path space gives a unique fixed point on each piece, and concatenation gives an absolutely continuous global solution. Composition with \(m\) recovers a solution of the original equations. Conversely, applying \(H\) to an original solution proves uniqueness there. No additional ODE theorem is needed.

## 4. Full variational equation and quantitative bound — PASS

For \(x=(h,V)\) and its linear variation \(v=(Z,\eta)\), differentiating the integral equation gives the candidate's coefficients

\[
A=pDX(x)+qDY(x)
=\begin{pmatrix}c(M)p&eq\\d(M)q&0\end{pmatrix},
\qquad rX(x)+sY(x)=\binom{f(h)r+eVs}{a(M)s}.
\]

The initial variation is exactly \(((1+M_0^2)\mu,\nu)\). The independent calculation in physical coordinates is consistent: differentiating \(Z=(1+M^2)\delta M\) introduces the diagonal term whose \(q\) coefficient is

\[
V\left(b'+\frac{2Mb}{1+M^2}\right)=0.
\]

In particular, no term proportional to \(Vq\) is omitted. The second row has coefficient \(b/(1+M^2)=d(M)\), as required.

For arbitrary signs of both drivers,

\[
\|A\|_1=\max\{|c(M)p|+|d(M)q|,e|q|\}
\le C_0|p|+e|q|.
\]

The time-ordered series for the transition matrix is valid for these integrable coefficients. Bounding each matrix product by the product of its norms and integrating on the ordered simplex gives the stated factorial bound and hence (17), for \(0\le\tau\le t\le T\). No commutation of the two coefficient matrices is assumed. The variation-of-constants integral (18) is well defined for \(r,s\in L^1\), and differentiation almost everywhere or substitution into the integral equation verifies it.

Using \(|f(h)|\le L(1+B_M^2)\), \(|V|\le K\), and \(|a|\le L\) in that formula proves (19). Finally, \(|\delta M|\le|Z|\), \(B_M\le C_eR\), and \(K\le C_eR\) give

\[
\|D\mathcal S(M_0,V_0,p,q)\|
\le C_eR^2\exp((e+L)P+eQ),
\]

once differentiability is justified below. Here \(\mathcal S\) is the physical trajectory solution map, with exactly the input and output norms specified in the candidate. The operator includes arbitrary simultaneous perturbations of both initial coordinates and both drivers. Evaluation at a terminal time has norm at most one, so the terminal-time conclusion follows. Both base drivers remain in the transition matrix for each forcing response.

The auxiliary identities (21) follow by the chain rule. The bounded factor \(2a/e\) preserves the \(C_eR^2\) prefactor for \(H,U\), while the factor \(V\) adds at most one power of \(R\) for \(I\). These claims do not require higher derivatives of the solution map.

## 5. Actual joint Fréchet differentiability in the stated spaces — PASS

The second derivatives (22) are correct. In particular, differentiating \(c(M)\) with respect to \(M\) cancels the two terms \(2eM\), leaving

\[
f''(h)=\frac{2a(M)(1-M^2)}{(1+M^2)^3}.
\]

Both this expression and \(g''(h)=-4eM/(1+M^2)^4\) are globally bounded. The derivatives of \(m\) at lines 318–319 are also correct and bounded.

The following makes explicit why the candidate's remainder estimate is joint and uniform over perturbation directions. Fix the base input, let

\[
\varepsilon=|\mu|+|\nu|+\|r\|_1+\|s\|_1\le1,
\]

and write \(\widetilde x=x+\Delta x\) for the perturbed transformed solution. Its input size is at most \(R+1\), so (11) bounds its state uniformly over this entire perturbation ball. The difference equation is

\[
(\Delta x)'=p[X(x+\Delta x)-X(x)]
+q[Y(x+\Delta x)-Y(x)]
+rX(x+\Delta x)+sY(x+\Delta x).
\]

The last two terms have integral norm at most a base-dependent constant times \(\varepsilon\), and the initial difference has the same bound. The global Lipschitz estimates and the exponential integral estimate therefore give \(\|\Delta x\|_\infty\le C_{\rm base}\varepsilon\), uniformly in all four perturbations.

Let \(\rho=\Delta x-v\), where \(v\) solves (14)–(15). For \(F=X,Y\), put

\[
\mathcal R_F=F(x+\Delta x)-F(x)-DF(x)\Delta x.
\]

Exact subtraction gives

\[
\rho'=A\rho+p\mathcal R_X+q\mathcal R_Y
+r[X(x+\Delta x)-X(x)]
+s[Y(x+\Delta x)-Y(x)].
\]

Bounded second derivatives imply \(|\mathcal R_F|\le C_e|\Delta x|^2\). Bounded first derivatives bound the other two differences by \(C_e|\Delta x|\). Thus the remaining source has integral norm at most

\[
C_e(P+Q)\|\Delta x\|_\infty^2
+C_e(\|r\|_1+\|s\|_1)\|\Delta x\|_\infty.
\]

This is precisely the required treatment of mixed driver/state perturbations. It requires no pointwise, \(L^2\), smoothness, or sign restriction on \(r,s\). Concentrated \(L^1\) perturbations obey the same estimate.

The initial remainder is exactly \((M_0\mu^2+\mu^3/3,0)\). Applying the transition bound gives \(\|\rho\|_\infty\le C_{\rm base}\varepsilon^2\). Finally,

\[
m(h+\Delta h)-m(h)-m'(h)Z
=m'(h)\rho_h+O(\|\Delta h\|_\infty^2)
\]

uniformly in time, by the bounded second derivative of \(m\). This proves the quadratic remainder for the physical trajectory map. The proposed derivative is linear by (18), bounded by (20), and has remainder divided by \(\varepsilon\) tending to zero uniformly over the input ball. It is an actual Fréchet derivative, not just a directional derivative or a formal linearization.

## 6. Subquadratic dependence and conditional moments — PASS

With \(\psi=(e+L)P+eQ\), one has \(0\le\psi\le C_eR\). Hence \(\psi/R^2\le C_e/R\to0\) uniformly as the input size tends to infinity. The polynomial prefactor causes no problem for the moment argument.

Under the explicit assumption \(\mathbb E e^{\lambda R^2}<\infty\), fix any finite \(r>0\). Since

\[
2r\log x+rC_ex-\lambda x^2\longrightarrow-\infty,
\]

there is a finite constant \(C_{r,e,\lambda}\) such that

\[
\left(C_eR^2e^\psi\right)^r
\le C_{r,e,\lambda}e^{\lambda R^2}.
\]

Taking expectations proves (24). Replacing \(2r\log x\) by any fixed polynomial power times \(\log x\) proves the auxiliary-coordinate statement as well. No smallness of the deterministic growth constants is needed, because a fixed negative quadratic dominates any fixed positive linear term.

The sufficient condition using individual input moments is valid without independence. Explicitly, write \((Z_1,Z_2,Z_3,Z_4)=(M_0,V_0,P,Q)\), assume \(\mathbb E e^{\theta_i Z_i^2}<\infty\), and choose \(0<\lambda\le\min_i\theta_i/20\). Then

\[
\mathbb E e^{\lambda R^2}
\le e^{5\lambda}\mathbb E\prod_{i=1}^4 e^{5\lambda Z_i^2}
\le e^{5\lambda}\prod_{i=1}^4
\left(\mathbb E e^{20\lambda Z_i^2}\right)^{1/4}<\infty.
\]

This verifies all exponents in the Hölder step. The candidate correctly does not infer this assumption from the existence of all polynomial input moments. The conclusion is finiteness of every finite positive moment of the displayed response bound, and consequently of the corresponding derivative norms, under the stated tail assumption.

## Required fixes

**None within the stated mathematical scope.** The PASS verdict applies to the exact candidate hash above. The excluded application and network conclusions remain outside this verdict; no such additional conclusion is needed to close this standalone proof.
