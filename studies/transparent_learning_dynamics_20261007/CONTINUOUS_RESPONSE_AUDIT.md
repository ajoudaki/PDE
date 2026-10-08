# Independent audit of the continuous response limit

2026-10-07. Scoped internal mathematical audit.

## Verdict and scope

**PASS: the conditional qualitative theorem is supported in the corrected
version identified below.** I found no missing moment estimate,
rank assumption, width-dependent maximum, infinite-dimensional existence
theorem, or probability interchange in its principal Euler-to-flow argument.
The proof depends on the common Hilbert realization, which is a separate
foundation rather than an additional result certified by this report.

The originally displayed estimate in Section 6,
\[
|f_n(s,v)-f_n(t,v)|\le 2\tau(t)\qquad(s\ge t),
\]
does not follow from the stated assumption \(\tau(t)\to0\) unless
\(\tau\) is nonincreasing. The correct bound is
\(\tau(s)+\tau(t)\). This immediately gives the same Cauchy and all-time
conclusions. Alternatively one may use the decreasing tail envelope for
all sufficiently large times. No stronger source hypothesis is necessary.
The author incorporated this correction during the audit; the current
version uses the correct sum and explicitly mentions the tail envelope.

The complete independent inputs were:

- CONTINUOUS_RESPONSE_LIMIT.md, 304 lines, SHA-256
  c3322e5255743165f4b4a19cb5273767477fba07c7239c4506b121cd2b47f89a.
- RESPONSE_HILBERT_REALIZATION.md, 197 lines, SHA-256
  23118c6bfe5a6200a2653aad51d4de8813b7e4c2d049d13ed19e4915d8738ed3.

After writing the initial complete report, a final hash check detected
concurrent changes. I reread the complete current main note, Hilbert note,
and finite-history note. The final checked versions are:

- CONTINUOUS_RESPONSE_LIMIT.md:
  cd2121787ad56a6acd6643879e827320851cbb4d9dfa3e84401138c8ee34a6fd.
- RESPONSE_HILBERT_REALIZATION.md:
  09e36b34b0172aa88040d575cf1cab1baa0a73d3e51c98eb9970c2f04e14dc07.
- UNCLIPPED_FINITE_HISTORY.md:
  9d842305cf984f2f5841466faf878e99f8f40815cebbc9f5ec341f9642b9ee81.

The foundation changes clarify immutable registers, finite-description
piecewise-linear functions, rational-to-real extension, and compatibility
with prescribed new constants. They do not change the present proof.
FINITE_RESPONSE_MEMORY.md was previously read completely and remains at
edf19fb88cc1d3b719b3668c575aa6a1316fa30b2c822d277fc84e7428b34c91.
My own OSGOOD_RESPONSE_STABILITY.md supplies the independently derived
one-sided gate estimate and scalar comparison.

No integrated source, other study, external literature, or separate Hilbert
review report was read. The final main/foundation reread exposed short
author-added statements that the separate Hilbert audit had passed and led
to those clarifications. This occurred after the present complete supporting
verdict was written and was not used as evidence for it.
This audit does not establish that the finite-width
operator, carrier, or endpoint assumptions hold for the source's admitted
labels. The research/proof skills were used to separate the theorem from
those upstream obligations; canonical notation was used throughout.

## 1. State space and physical normalization

For finite input dimension \(d\), the limiting parameter space is
\[
\mathcal H=
\operatorname{HS}(\mathbb R^d,H_1)
\ \oplus\!
\bigoplus_{\ell=2}^{L}\operatorname{HS}(H_{\ell-1},H_\ell)
\ \oplus H_L.
\]
Here \(H_\ell\) is a probability \(L^2\) space, the hidden parameter is the
learned increment \(B_\ell\), and its fixed initialized action is \(G_\ell\).
The affine state is \(\theta=(A,(B_\ell)_{\ell=2}^{L},w)\).
The initial \(A_0\) is Hilbert--Schmidt because \(d<\infty\).

The finite-width norm is precisely
\[
\|\Delta A\|_F^2/n+
\sum_{\ell=2}^{L}\|\Delta W_\ell\|_F^2+
\|\Delta w\|_2^2/n.
\]
A hidden update \(\delta h^\top/n\) has Frobenius norm
\(\|\delta\|_{2,n}\|h\|_{2,n}\); no width factor is missing.
A parameter error \(e\) changes each hidden operator norm and the normalized
first operator norm by at most \(e\).

Bounded hidden operators, derivative gates, and readout RMS imply bounded
backward RMS by finite recursion. Multiplying by feature and residual
bounds controls all velocity blocks independently of width. A finite number
of blocks only changes the depth-dependent constant.

## 2. The one-sided vector-field modulus

Let \(s\) bound the derivative gate, let \(t_2\) be its Lipschitz constant,
and suppose the reference carrier satisfies
\(\mathbb E\exp(|k|/A)\le B\). Expectation can equally denote empirical
average. Since \(x^2e^{-x/A}\) decreases for \(x\ge2A\),
\[
\|k\mathbf1_{\{|k|>R\}}\|_2\le\sqrt B\,R e^{-R/(2A)}
\qquad(R\ge2A).
\]
The decomposition
\[
\begin{split}
\|\phi'(z')k'-\phi'(z)k\|_2
\le{}&s\|k'-k\|_2+t_2R\|z'-z\|_2\\
&+2s\|k\mathbf1_{\{|k|>R\}}\|_2
\end{split}
\]
uses only the reference tail. For \(0<e\le1\), choosing
\(R=4A\log(\exp(1)/e)\) makes the last term at most a constant times
\(\log(\exp(1)/e)(e/\exp(1))^2\), hence at most
\(Ce\log(\exp(1)/e)\). The central term has the same bound when
\(\|z'-z\|_2\le P e\).

Forward subtraction is Lipschitz in the physical norm on a bounded
neighborhood. Backward subtraction always puts the changed gate on a
reference carrier; other terms are bounded operators applied to the next
backward error or operator errors applied to reference fields. Thus recursion
only adds and multiplies the same modulus. It does not iterate logarithms.
The rank-one estimate
\[
\|u'\otimes v'-u\otimes v\|_{\rm HS}
\le\|u'-u\|_2\|v'\|_2+\|u\|_2\|v'-v\|_2
\]
then proves
\[
\|F(\theta')-F(\theta)\|_{\mathcal H}
\le C\omega(\|\theta'-\theta\|_{\mathcal H}),\qquad
\omega(e)=e\log(\exp(1)/e).
\]
No exponential budget, coordinate maximum, or higher moment of the
perturbed state is needed.

## 3. Euler comparison and its stopping condition

Write \(\pi_h(s)=\lfloor s/h\rfloor h\). The source velocity bound gives
\[
\|\theta_h(\pi_h(s))-\theta(s)\|_{\mathcal H}
\le e(\pi_h(s))+Vh.
\]
The reference in the vector-field comparison is the exact state at time
\(s\), so its assumed carrier budget applies. With
\[
E(t)=(V+1)h+\sup_{u\le t}e(u),
\]
the integral difference gives
\[
E(t)\le(V+1)h+C\int_0^t\omega(E(s))\,ds
\]
while \(E\le1\). The precise bootstrap should stop at the first \(E=1\),
not merely the first \(e=1\), because the queried state also has a \(Vh\)
displacement. The text already restricts its inequality to \(E\le1\);
this is a stopping-wording clarification, not an estimate defect.

The scalar equality has exactly the stated solution
\[
v(t)=\exp(1)
\left(\frac{(V+1)h}{\exp(1)}\right)^{\exp(-Ct)}.
\]
For fixed \(T\), taking \(h\) such that \(v(T)<1/2\) prevents the exit.
Positive-floor scalar comparison is valid. Forward errors are
\(O(\varepsilon_T(h))\), and training backward errors are
\(O(\omega(\varepsilon_T(h)))\). Their pairings follow by the \(L^2\)
product estimate. Euler carrier exponential budgets are never needed.

## 4. Common-Hilbert Cauchy construction

The two Euler runs are correctly concatenated on the same initialized
matrices; independent copies would not identify their distance.

For fixed meshes and evaluation time, first-layer and readout differences
are finite combinations of fields. Hidden increments are finite sums of
normalized rank-one updates. Expanding their squared Frobenius distance
requires only terms
\[
\langle u_i,u_j\rangle_{2,n}\langle v_i,v_j\rangle_{2,n}
\]
and finite scalar coefficient products. Individual pairings have
deterministic finite-program limits; their finite products therefore
converge in probability. This needs no fourth moment of original
finite-width fields: averages are multiplied only after their own limits
are known.

The limit is precisely the squared Hilbert distance by the rank-one
Hilbert--Schmidt identity. A deterministic limiting distance inherits an
upper bound holding with probability tending to one. Thus the source
comparison gives the limiting bound
\(\varepsilon_T(h)+\varepsilon_T(h')\).
Obtain this at rational times and extend by continuity. No theorem uniform
over infinitely many programs or times is invoked. The limiting mesh paths
are Cauchy in \(C([0,T];\mathcal H)\); completeness gives a continuous path.

## 5. Existence and the gradient-flow interpretation

The vector field is continuous on \(\mathcal H\). In particular,
\((z,k)\mapsto\phi'(z)k\) is continuous from \(L^2\times L^2\) to \(L^2\):
truncate the fixed reference carrier, take the \(L^2\) limit, then remove
the truncation using its square integrability. No uniform tail assumption
is needed for this continuity. Operator application and rank-one
Hilbert--Schmidt products are continuous as well.

Uniform convergence of mesh paths implies uniform convergence of their
left-endpoint states to the limiting path: the additional error is bounded
by that path's modulus of continuity on intervals of length \(h\).
Continuity of \(F\) makes its values converge uniformly along these
approximations to a compact path. Otherwise bad times have a convergent
subsequence and both parameter arguments approach the same point, a
contradiction.

Consequently the Euler Bochner integral equations pass to
\[
\theta_\infty(t)=\theta_\infty(0)
+\int_0^tF(\theta_\infty(s))\,ds.
\]
The integrand is continuous, so the solution is strong and \(C^1\).
This is a controlled Cauchy-approximation argument, not an incorrect appeal
to infinite-dimensional Peano existence.

An important distinction: a Lipschitz scalar activation need not define a
Fréchet differentiable Nemytskii map \(L^2\to L^2\). That assertion is not
needed. Along every fixed parameter direction, bounded \(\phi'\) gives
the \(L^2\) directional chain rule by dominated convergence. Applying
adjoints gives the displayed gradient of each scalar prediction. This
gradient is continuous by the gated-product argument. The fundamental
theorem of calculus on parameter segments then proves Fréchet
differentiability of the scalar prediction functional. Thus the vector
field is genuinely the negative Hilbert gradient of mean squared loss.

## 6. Transfer of bounds and uniqueness

For an operator bound, include a fixed generated test field \(u\) and
the query \((G+B_h)u\) in the joint finite program. The dense cap and
parameter Euler error bound this Euler operator by \(M+\varepsilon_T(h)\).
Pairing limits transfer the inequality to the common realization. Test
the countable generated dense set, extend by continuity, then let \(h\to0\);
Hilbert--Schmidt convergence of increments implies operator-norm
convergence. First-operator and RMS bounds are simpler instances.

For the carrier budget use the bounded \(N/A\)-Lipschitz function
\[
\psi_N(x)=\min\{N,\exp(|x|/A)\},\qquad N\ge1.
\]
If \(\delta_h\to0\) bounds the source-to-Euler carrier RMS error, then
finite-program convergence gives, at every fixed time,
\[
\mathbb E\psi_N(k_h)\le B+(N/A)\delta_h.
\]
Let \(h\to0\), using continuity of carrier evaluation, then let
\(N\to\infty\). Monotone convergence proves the required budget.
The constants are the same at each time, yielding
\(\sup_{t\le T}\mathbb E\exp(|k_\infty(t)|/A)\le B\).
This does not claim the stronger
\(\mathbb E\exp(\sup_{t\le T}|k_\infty(t)|/A)\le B\).
There is no uncountable-time probability interchange.

The limiting path can therefore be the reference in the one-sided
modulus. Any competing strong solution with the same initial state stays
locally in a bounded neighborhood by continuity. Zero-defect Osgood
comparison forces equality locally and continuation gives uniqueness.
No competing-solution tail budget is needed.

Constructions on nested integer horizons consequently agree and define a
global strong limiting flow. Constants may depend on the horizon. No single
event controlling every width and every horizon is needed, since each
deterministic finite-horizon conclusion has already been established.

## 7. Compact time, endpoints, and the sphere

The compact-time observable argument is compressed but valid. Evaluation
of interpolated Euler parameters at each fixed time is an allowed finite
program with a fixed scalar interpolation weight. Source velocity bounds
give uniform time equicontinuity of exact finite-width forward fields and
predictions on good events. Training backward fields have the uniform
one-sided modulus from the source carrier budget. A finite time net,
pointwise convergence, and these bounds give uniform compact-time
convergence. No Euler carrier budget is required.

For endpoints use the corrected estimate
\[
|f_n(s,v)-f_n(t,v)|\le\tau(s)+\tau(t).
\]
Two-fixed-time convergence makes \(f_\infty(t,v)\) Cauchy at infinity,
uniformly on the finite panel. Letting \(s\to\infty\) gives
\[
|f_\infty(t,v)-f_\infty(\infty,v)|\le\tau(t).
\]
Compact-time convergence up to a large fixed \(T\) controls endpoints by
the time-\(T\) discrepancy plus \(2\tau(T)\); the two tails then control
later times. For a nonmonotone tail use \(\sup_{s\ge T}\tau(s)\to0\).
This proves the all-time output statement, including the endpoint.

The theorem does not assert cross-width parameter Hilbert convergence,
existence of a limiting parameter endpoint, all-time hidden or backward
Gram convergence, or interpolation of the training labels. The last
claim would require identification of finite-width endpoints with the
labels; assumption 3 by itself supplies only endpoints and tails.

For the sphere extension, finite input dimension is essential. Bounded
normalized first/hidden operators and readout give the displayed input
Lipschitz bound on each fixed horizon. Added net points are passive inputs,
so including them in the finite program does not change training. Choose
the horizon using the uniform sphere tail, then a finite net for that
horizon, then take width large. Horizon-dependent operator/readout
constants are sufficient; no theorem over growing input nets is needed.

## 8. Genuine remaining limitations

None of the source geometry, empirical exponential carrier, or endpoint
tail hypotheses is established by this audit.

The order is fixed horizon, fine but fixed mesh, then large width. The
growth of finite-program constants with history length is uncontrolled.
No \(n^{-1/2+o(1)}\) all-time error rate, finite autonomous observable closure,
or quantitative continuous response-memory theorem follows.

Subject to the common-Hilbert foundation, and with the endpoint correction
now incorporated, the qualitative conditional global gradient-flow theorem and
its stated output/compact-time Gram comparisons pass this audit.
