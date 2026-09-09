# Hostile audit of the near-identity homotopy

Date: 25 August 2026.

## 1. Verdict

The homotopy is promising, but the proposed inference

\[
 \text{identity theorem}
 +\text{fixed-\(t\) continuity in }\varepsilon
 \Longrightarrow
 \text{one fixed nonlinear interval }|\varepsilon|\le\varepsilon_0
 \tag{1.1}
\]

is false. The missing property is continuity in a horizon-weighted sequence
space, or an equivalent uniform estimate on the intrinsic OMFP response
ledger.

The idea was partially tried before the present step-doubling question. The
depth-three IDE audit selected a normalized residual-sine activation as the
cleanest near-identity candidate. It also falsified two shortcuts:

1. its nonlinear correction is \(O(\varepsilon)\), not \(o_n(1)\), after
   taking width to infinity; and
2. the full finite-width sensitivity is not dimension-uniform: an
   initialization derivative has operator norm at least of order
   \(|\varepsilon|\sqrt{\log n}\).

The potentially successful version was not closed: use small curvature to
invert the intrinsic, step-weighted, mixed response block after all reused
matrix responses have been recombined into aggregate adjoint actions.

There is a decisive obstruction to simply perturbing the identity proof. In
the \(L^2\)/trace-class Banach topology used there, the \(C^2\) seminorm of
the activation map jumps from zero at \(\varepsilon=0\) to infinity for every
nonzero genuinely nonlinear perturbation. Small \(\varepsilon\) does not
repair this.

No admissible nonlinear OMFP counterexample is proved here. The audit
falsifies the naive continuity argument, not the desired network theorem.

## 2. Canonical activation and limit order

Let \(G\sim N(0,1)\), and set

\[
 v_\varphi^2=\mathbb E\varphi(G)^2,
 \qquad
 c_\varphi=\mathbb E[G\varphi(G)].
 \tag{2.1}
\]

Use the RMS-normalized family

\[
 s_\varepsilon^2
 =1+2\varepsilon c_\varphi+\varepsilon^2v_\varphi^2,
 \qquad
 \psi_\varepsilon(x)
 =\frac{x+\varepsilon\varphi(x)}{s_\varepsilon}.
 \tag{2.2}
\]

Then \(\mathbb E\psi_\varepsilon(G)^2=1\). The reverse triangle inequality
in \(L^2(\gamma)\) gives

\[
 1-|\varepsilon|v_\varphi
 \le s_\varepsilon
 \le 1+|\varepsilon|v_\varphi.
 \tag{2.3}
\]

In particular, \(|\varepsilon|v_\varphi\le1/4\) implies

\[
 \frac34\le s_\varepsilon\le\frac54.
 \tag{2.4}
\]

Moreover,

\[
 \psi_\varepsilon'(x)
 =\frac{1+\varepsilon\varphi'(x)}{s_\varepsilon},
 \qquad
 \psi_\varepsilon^{(r)}(x)
 =\frac{\varepsilon\varphi^{(r)}(x)}{s_\varepsilon},
 \quad r\ge2.
 \tag{2.5}
\]

Thus every curvature insertion obeys

\[
 \|\psi_\varepsilon^{(r)}\|_\infty
 \le\frac43|\varepsilon|\|\varphi^{(r)}\|_\infty,
 \qquad r\ge2.
 \tag{2.6}
\]

The class is genuinely nonlinear when
\(\varphi''\not\equiv0\) and \(\varepsilon\ne0\).

A canonical concrete candidate found in the earlier audit is

\[
 \varphi_*(x)=\sin x-e^{-1/2}x.
 \tag{2.7}
\]

Stein's identity gives

\[
 \mathbb E[G\sin G]=\mathbb E[\cos G]=e^{-1/2},
 \tag{2.8}
\]

so \(c_{\varphi_*}=0\), and

\[
 \psi_{\varepsilon,*}(x)
 =
 \frac{x+\varepsilon\varphi_*(x)}
 {\sqrt{1+\varepsilon^2v_{\varphi_*}^2}}.
 \tag{2.9}
\]

It is at most linear and globally bi-Lipschitz whenever

\[
 |\varepsilon|<(1+e^{-1/2})^{-1}.
 \tag{2.10}
\]

The bounded alternative \(\varphi(x)=\sin x\) belongs to the frozen
\(C^{12}\) bounded class; it merely has \(c_\varphi\ne0\).

The required order of limits is

\[
 F_{t,L}^{(\varepsilon)}(h)
 =
 \lim_{n\to\infty}F_{t,L,n}^{(\varepsilon)}(h)
 \quad\text{for every fixed }(t,h,\varepsilon),
 \tag{2.11}
\]

followed by \(h=T/t\) and \(t\to\infty\). The parameter \(\varepsilon\)
must remain fixed. A radius \(\varepsilon_t\to0\) proves no fixed nonlinear
class.

## 3. The correct continuity topology

Define

\[
 \Delta_{t,L}^{(\varepsilon)}(h)
 =
 F_{2t,L}^{(\varepsilon)}(h)
 -
 F_{t,L}^{(\varepsilon)}(2h),
 \tag{3.1}
\]

and let \(\kappa_{t,L}^{(\varepsilon)}\) be the explicit Gaussian cubic
coefficient, with its sign fixed consistently with (3.1). The canonical
least remainder coefficient is

\[
 b_{t,L}^{(\varepsilon)}(\rho)
 =
 \sup_{0<|h|\le\rho/t}
 \frac{
 \left|
 \Delta_{t,L}^{(\varepsilon)}(h)
 -
 \kappa_{t,L}^{(\varepsilon)}h^3
 \right|}
 {|h|^5}.
 \tag{3.2}
\]

Scalar dyadic convergence requires

\[
 \sum_{j\ge0}
 2^{-5j}b_{2^j,L}^{(\varepsilon)}(\rho)<\infty.
 \tag{3.3}
\]

Therefore the sharp continuity space is

\[
 \ell^1_5
 =
 \left\{
 (q_j):
 \sum_{j\ge0}2^{-5j}|q_j|<\infty
 \right\}.
 \tag{3.4}
\]

For example, either of the following would suffice:

\[
 \sum_{j\ge0}2^{-5j}
 \left|
 b_{2^j,L}^{(\varepsilon)}(\rho)
 -
 b_{2^j,L}^{(0)}(\rho)
 \right|
 \le C_{R,L}|\varepsilon|,
 \tag{3.5}
\]

or, for some \(\beta<1\),

\[
 \sup_{t\ge1}
 t^{-(4+\beta)}
 \left|
 b_{t,L}^{(\varepsilon)}(\rho)
 -
 b_{t,L}^{(0)}(\rho)
 \right|
 \le C_{R,L}|\varepsilon|.
 \tag{3.6}
\]

Because \(b_t\) is output-derived, (3.5)--(3.6) are not admissible
hypotheses. They identify the topology in which a primitive OMFP ledger
estimate has to be proved.

### Proposition 3.1: fixed-\(t\) continuity is insufficient

Analyticity in \(\varepsilon\) for each fixed \(t\), together with
\(b_t^{(0)}\le Ct^4\), does not imply (3.3) for any fixed
\(\varepsilon\ne0\).

#### Proof

Consider the scalar proof-route witnesses

\[
 b_t^{(\varepsilon)}=t^4e^{\varepsilon t}
 \quad(\varepsilon\ge0),
 \qquad
 \widetilde b_t^{(\varepsilon)}
 =t^4+\varepsilon t^6.
 \tag{3.7}
\]

They are analytic at zero for every fixed \(t\) and equal \(t^4\) at zero.
For every fixed \(\varepsilon>0\),

\[
 \sum_j2^{-5j}b_{2^j}^{(\varepsilon)}=\infty,
 \qquad
 \sum_j2^{-5j}\widetilde b_{2^j}^{(\varepsilon)}=\infty.
 \tag{3.8}
\]

These are not claimed to be OMFP outputs. They disprove only the proposed
logical inference. \(\square\)

The fixed-horizon compiler does give, for each fixed \(t,L,R\), a finite
local constant \(\Lambda_{t,L,R}\) such that, on a common fixed-\(t\)
interval,

\[
 \left|
 b_{t,L}^{(\varepsilon)}
 -
 b_{t,L}^{(0)}
 \right|
 \le \Lambda_{t,L,R}|\varepsilon|.
 \tag{3.9}
\]

This follows by joint dominated differentiation of the finite inverse-free
Gaussian DAG after width identification. It yields at best a radius

\[
 |\varepsilon|
 \lesssim
 \frac{t^4}{\Lambda_{t,L,R}}.
 \tag{3.10}
\]

No existing estimate prevents this radius from tending to zero.

## 4. The operator topology is discontinuous at identity

Let \(N_\varepsilon(u)=\psi_\varepsilon\circ u\) on a nonatomic Gaussian
probability space.

### Proposition 4.1: \(C^2(L^2,L^2)\) obstruction

If \(\varphi\in C^2\), \(\varphi''\not\equiv0\), and
\(\varepsilon\ne0\), then \(N_\varepsilon:L^2\to L^2\) has no bounded
second Fréchet derivative at a standard Gaussian field \(Z\). At
\(\varepsilon=0\), its second derivative is zero.

#### Proof

There are an interval \(I\) and \(c>0\) such that

\[
 |\varphi''(x)|\ge c,
 \qquad x\in I.
 \tag{4.1}
\]

The event \(A=\{Z\in I\}\) has positive probability. By nonatomicity choose
\(E_m\subset A\) with

\[
 p_m=\mathbb P(E_m)\downarrow0,
 \qquad
 v_m=w_m=p_m^{-1/2}\mathbf 1_{E_m}.
 \tag{4.2}
\]

Then \(\|v_m\|_2=\|w_m\|_2=1\). Pointwise differentiation along bounded
directions forces any putative second Fréchet derivative to equal

\[
 D^2N_\varepsilon(Z)[v,w]
 =
 \frac{\varepsilon}{s_\varepsilon}
 \varphi''(Z)vw.
 \tag{4.3}
\]

Consequently,

\[
 \left\|
 D^2N_\varepsilon(Z)[v_m,w_m]
 \right\|_2
 \ge
 \frac{|\varepsilon|c}{s_\varepsilon}p_m^{-1/2}
 \longrightarrow\infty.
 \tag{4.4}
\]

No bounded bilinear second derivative exists. For \(\varepsilon=0\),
\(N_0\) is the identity and \(D^2N_0=0\). \(\square\)

Thus the relevant ambient seminorm jumps from zero to infinity:

\[
 |\varepsilon|\cdot\infty=\infty
 \qquad(\varepsilon\ne0).
 \tag{4.5}
\]

This obstruction already occurs at the first nonlinear connector for
\(L=2\) and persists for \(L=3\).

Using an \(L^p\) scale alone does not close the problem. Products require an
exponent loss, such as

\[
 L^{2p}\times L^{2p}\longrightarrow L^p,
 \tag{4.6}
\]

whereas the reused-matrix adjoints have no ambient, rank-uniform \(L^p\)
bound. Any successful norm must live on the generated reachable core and
must retain intrinsic aggregate adjoint responses.

## 5. The accumulation dichotomy

If a proof pays an unweighted factor \(1+C_R|\varepsilon|\) at every step,
then

\[
 (1+C_R|\varepsilon|)^t
 \le e^{C_R|\varepsilon|t}.
 \tag{5.1}
\]

Keeping this below \(t^{1-\delta}\) requires

\[
 |\varepsilon|
 \le
 \frac{(1-\delta)\log t+O(1)}{C_Rt},
 \tag{5.2}
\]

which tends to zero.

If every temporal perturbation retains its actual step weight, the factor is

\[
 (1+C_R|\varepsilon||h|)^t
 \le
 e^{C_R|\varepsilon|t|h|}
 \le
 e^{C_R|\varepsilon|\rho},
 \qquad |h|\le\rho/t.
 \tag{5.3}
\]

This is uniform in \(t\). Same-time curvature insertions inside one
forward/backward sweep need not carry \(h\), but their number is bounded by
the fixed depth and differential order.

The exact OMFP divisibility theorem already supplies the source-step factor
for historical responses. The open bridge is to preserve it through all
mixed step/source derivatives and through recombination into aggregate
adjoint actions. The highest-order \(L=2\) block couples the forward and
transpose response families. Since every curvature is \(O(|\varepsilon|R)\),
a Neumann absorption is plausible, but only after that block is bounded in a
generated-core norm.

A proof which supplies only

\[
 b_t^{(\varepsilon)}
 \le Ct^4+C_R|\varepsilon|t^5
 \tag{5.4}
\]

is insufficient: its majorant contributes a nonzero constant at every
dyadic scale. This does not show the canonical coefficient diverges; it
shows that a small prefactor cannot certify a borderline \(t^5\) bound. The
loss must be strictly sub-\(t^5\), or directly summable.

## 6. Sharp noncircular perturbative target

The strongest plausible \(L=2\) target is the following.

### Conjecture NI-OMFP\(_2(R)\)

There are explicit \(A_R,B_R,C_R<\infty\), obtained only from the activation
envelope and stated Gaussian moments, such that every exact depth-two
coarse/fine hybrid DAG with total step variation \(t|h|\le\rho_R\) satisfies

\[
 \mathfrak E_{t,2}^{(\varepsilon)}(h)
 \le
 \frac{A_R}{1-C_R|\varepsilon|}
 e^{B_R|\varepsilon|t|h|},
 \tag{6.1}
\]

provided

\[
 |\varepsilon|
 \le
 \varepsilon_0(R)
 :=
 \min\left\{
 \frac1{4R},
 \frac1{2C_R}
 \right\}.
 \tag{6.2}
\]

Here \(\mathfrak E\) is the intrinsic finite response ledger: generated
fields; normalized \(h\)-jets through order three; source and mixed
source/\(h\) jets through total order four; moving raw actions; aggregate
adjoint responses; and the transported local-defect direction. Source
coordinates are recombined into aggregate adjoint actions before absolute
values are taken. Thus (6.1) contains no output derivative, trained-output
modulus, Gram inverse, or unknown trajectory constant.

A marked-insertion proof of (6.1) would need to establish:

1. historical nonlinear marks retain their causal step weights;
2. \(k\) ordered historical marks cost at most
   \((B_RT)^k/k!\);
3. the finitely many same-time marks cost only a depth/order polynomial;
4. aggregate \(W/W^*\) responses preserve the generated-core norm; and
5. the coupled highest-order response block has norm at most
   \(C_R|\varepsilon|<1\).

Items 4--5 are the genuinely new content. They are currently open.

### Proposition 6.1: consequence of NI-OMFP\(_2(R)\)

If (6.1) holds, define

\[
 \widehat C_R
 =
 \frac{A_R}{1-C_R\varepsilon_0(R)}
 e^{B_R\varepsilon_0(R)\rho_R}.
 \tag{6.3}
\]

Then, uniformly in \(t\ge1\),

\[
 \left|
 \Delta_{t,2}^{(\varepsilon)}(h)
 -
 \kappa_{t,2}^{(\varepsilon)}h^3
 \right|
 \le
 \frac{\widehat C_R}{6}t^4|h|^5,
 \qquad
 |h|\le\rho_R/t.
 \tag{6.4}
\]

#### Proof

The exact paired-Euler factorization is

\[
 \Delta_{t,2}^{(\varepsilon)}(h)
 =
 h^2Q_t^{(\varepsilon)}(h),
 \qquad
 Q_t^{(\varepsilon)}(h)
 =
 \sum_{j=0}^{t-1}A_{j,t}^{(\varepsilon)}(h).
 \tag{6.5}
\]

The normalized ledger is defined node by node so that

\[
 \left|
 (A_{j,t}^{(\varepsilon)})'''(h)
 \right|
 \le
 t^3\mathfrak E_{t,2}^{(\varepsilon)}(h).
 \tag{6.6}
\]

Summing the \(t\) transported defects and using (6.1)--(6.3) yields

\[
 \sup_{|h|\le\rho_R/t}
 \left|
 (Q_t^{(\varepsilon)})'''(h)
 \right|
 \le
 \widehat C_Rt^4.
 \tag{6.7}
\]

Initialization sign symmetry makes \(Q_t^{(\varepsilon)}\) odd. Taylor's
integral formula and

\[
 \kappa_{t,2}^{(\varepsilon)}
 =
 (Q_t^{(\varepsilon)})'(0)
 \tag{6.8}
\]

give (6.4), including the factor \(1/6\).

The explicit Gaussian formula for
\(J_{\psi_\varepsilon,2}\), together with (2.3)--(2.6), supplies an explicit
\(K_R<\infty\) such that

\[
 |\kappa_{t,2}^{(\varepsilon)}|
 \le K_Rt^2.
 \tag{6.9}
\]

Hence cubic dyadic increments are \(O_R(t^{-1})\), while the fifth-order
increments are summable because

\[
 \sum_{j\ge0}
 \frac{(2^j)^4}{(2^j)^5}
 =
 \sum_{j\ge0}2^{-j}<\infty.
 \tag{6.10}
\]

This proves scalar dyadic convergence. \(\square\)

Proposition 6.1 is a proved implication. Conjecture NI-OMFP\(_2(R)\) itself
remains open.

## 7. Depth-three audit

At \(L=3\) there are two reused connectors and two coupled causal response
pairs. A transfer theorem would have to carry (6.1) through the second
connector without adding a positive power of \(t\). Schematically, one needs

\[
 \|\mathcal C_{3,\varepsilon}\|
 \le C_{R,3}|\varepsilon|,
 \tag{7.1}
\]

in the same intrinsic generated-core scale. It would permit

\[
 \varepsilon_0(R,3)
 =
 \min\left\{
 \frac1{4R},
 \frac1{2C_{R,3}}
 \right\},
 \tag{7.2}
\]

and then

\[
 b_{t,3}^{(\varepsilon)}(\rho_{R,3})
 \le C'_{R,3}t^4.
 \tag{7.3}
\]

This is not automatic from \(L=2\). If a crude transfer squares a
\(t^\beta\) ledger estimate, the exponent becomes \(2\beta\). Under that
crude transfer, \(L=3\) would require \(\beta<1/2\), not merely
\(\beta<1\). The ideal \(\beta=0\) estimate is stable under finitely many
such products.

The second connector also receives moving queries already adapted through
the first connector. Thus the \(L=3\) theorem remains open until the
generated-core connector estimate is proved.

## 8. Claim ledger

### Proved

1. The normalization (2.2) gives an explicit genuinely nonlinear class.
2. The correct continuity topology is (3.4).
3. Fixed-\(t\) continuity, even analyticity, does not imply the desired
   horizon-uniform result.
4. The ambient \(C^2(L^2,L^2)\) seminorm is infinite for every nonzero
   genuinely nonlinear perturbation.
5. Unweighted accumulation \(e^{C|\varepsilon|t}\) forces
   \(\varepsilon\to0\), whereas the step-weighted factor
   \(e^{C|\varepsilon|t|h|}\) is uniform on \(t|h|\le\rho\).
6. A borderline \(t^5\) perturbative majorant is not sufficient.
7. NI-OMFP\(_2(R)\), if established, implies the explicit
   \(t^4|h|^5\) remainder by Proposition 6.1.

### Falsified proof routes

1. Ordinary operator-norm perturbation of the identity Banach theorem.
2. Uniform finite-width sensitivity followed by the width limit.
3. Pointwise-in-\(t\) continuity or a radius \(\varepsilon_0(t)\).
4. Ambient \(L^p\) bounds for reused-matrix adjoints.
5. Any absolute majorant with a borderline \(t^5\) nonlinear term.

### Open

1. NI-OMFP\(_2(R)\), especially aggregate-adjoint control of the mixed
   highest-order response block.
2. An admissible OMFP counterexample to dyadic summability; none is known.
3. The \(L=3\) connector transfer preserving an exponent below one.
4. Identification of a scalar dyadic limit with a state IDE or with
   finite-width continuous gradient flow.

## 9. Highest-leverage next step

Write the exact \(L=2\) mixed response block after recombining all source
coordinates into the two intrinsic aggregate adjoint actions, and prove

\[
 \|\mathcal C_{2,\varepsilon}\|_{\mathscr G_R\to\mathscr G_R}
 \le C_R|\varepsilon|
 \tag{9.1}
\]

in an explicitly constructed generated-core norm, or prove the equivalent
marked-insertion factorial estimate from Section 6.

This is the first place where small \(\varepsilon\) supplies a genuinely new
mechanism: it permits a Neumann inversion with an activation-defined radius.
If every candidate norm necessarily loses a moment or Malliavin order at
each pass, the homotopy route is disfavored. If (9.1) holds, the \(L=2\)
theorem follows with the explicit constants in (6.2)--(6.4), and the same
norm can immediately be pressure-tested at the second connector for \(L=3\).
