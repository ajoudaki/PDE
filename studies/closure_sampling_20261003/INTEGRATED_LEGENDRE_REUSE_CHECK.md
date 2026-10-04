# Check of the inherited Legendre theorem and explicit order schedule

2026-10-04. Scoped internal mathematical check. This checks the reuse of an
explicitly authorized prior-study theorem; it is not a new proof of its
finite-network insertion argument or an independent promotion review.

**Verdict: the theorem transfer and the elementary schedule/storage
calculations pass, with two quantifier clarifications.** The initialization
assumption is a fixed positive limiting feature-Gram gap, or the corresponding
width-uniform finite-width margin on the good event. Mere positive definiteness
at each finite width is insufficient. The probability statement is per width:
for each fixed confidence, every sufficiently large width has the stated good
event. It is not a single event for infinitely many independent initializations.

The complete scientific inputs read were `INTEGRATED_LEGENDRE_REUSE.md` and
the authorized prior study's `DEPTH_EXTENSION_RESULT.md`,
`DEPTH_TRACKING_CHECK.md`, `UNBOUNDED_ACTIVATION_CHECK.md`, and
`ACTIVATION_EXTENSION_CHECK.md`. No unrelated study, manuscript, or maintained
book passage was read. Required canonical-notation, neural-response-memory,
and rigorous-mathematics instructions were applied. Only this report was written.

## 1. What is inherited

Fix the data size \(m\), input dimension \(d\), hidden depth \(L\ge2\),
and training data independently of width \(n\). The source uses the bias-free
forward pass
\[
 z^{(1)}(x)=W^{(1)}x/\sqrt d,\qquad
 z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),\qquad
 h^{(\ell)}(x)=\phi_\ell(z^{(\ell)}(x)),\qquad
 f(x)=w^\top h^{(L)}(x)/n.
\]
The first matrix has independent standard Gaussian entries; each later
initialized hidden matrix has independent \(N(0,1/n)\) entries; the readout
starts at zero. The loss is \(m^{-1}\sum_a(f(x_a)-y_a)^2\), and the block
mobilities are \((n,1,\ldots,1,n)\).

The source assumption is exactly
\[
 \phi_\ell\in C^3(\mathbb R),\qquad
 \max_{1\le j\le3}\|\phi_\ell^{(j)}\|_\infty<\infty.
\]
It does not require bounded activation values. In particular,
\(|\phi_\ell(s)|\le |\phi_\ell(0)|+
\|\phi_\ell'\|_\infty |s|\). The constants can depend on these fixed
activation bounds and offsets. Nonaffinity is needed for the source's stated
automatic Gram-gap cases, not as an additional hypothesis when the positive
limiting Gram gap is supplied explicitly. The source permits layer-dependent
activations with this explicit Gram assumption; no orthogonality assumption
is needed.

The label RMS \(Y=(m^{-1}\sum_a y_a^2)^{1/2}\) must lie below the source's
fixed positive threshold. The threshold can depend on data geometry, depth,
activation bounds, and Gram margin. It is independent of width, order, and
time; no uniformity as depth grows or the Gram margin vanishes is asserted.
When exact data symmetries require a quotient, labels must be compatible and
the quotient retains the original positive sample weights. The activation
check establishes that these quotients preserve both trained systems and
their residual-RMS clock. For zero labels, both paths are stationary.

The closure is the original autonomous Legendre closure, sharing the dense
network's initialization. In particular,
\[
 \dot\tau=\widehat\rho,
 \qquad \widehat\rho^2=m^{-1}\sum_a
       (\widehat f_{n,q}(t,x_a)-y_a)^2,
 \qquad \tau(0)=1,
\]
and, for \(\ell=2,\ldots,L\), its reconstructed hidden matrix is
\[
 \widehat W^{(\ell)}=W_0^{(\ell)}-
 \frac{2}{mn\tau}\sum_{a=1}^m\sum_{j=0}^{q-1}(2j+1)
 \bar\delta_{a,j}^{(\ell)}\bar h_{a,j}^{(\ell-1)\top}.
\]
Here each forward or backward memory is an \(n\)-vector. The zeroth forward
memory starts at its initialized feature, and other forward memories and all
backward memories start at zero. The weighted quotient version replaces
\(m^{-1}\sum_a\) by its positive weighted sum. No dense trajectory drives
the actual closure, and no altered clock is used.

Let \(D_{n,q}\) denote the all-time normalized physical parameter distance
\[
 D_{n,q}=\sup_{t\ge0}\left[
 \frac{\|\widehat W^{(1)}(t)-W_D^{(1)}(t)\|_F}{\sqrt n}
 +\sum_{\ell=2}^L
       \|\widehat W^{(\ell)}(t)-W_D^{(\ell)}(t)\|_F
 +\frac{\|\widehat w(t)-w_D(t)\|_2}{\sqrt n}\right].
\]
The inherited result supplies fixed constants \(C,K\ge0\) and events
\(\Omega_n\), with \(\Pr(\Omega_n)\to1\), such that on \(\Omega_n\),
simultaneously for every integer \(q\ge1\),
\[
 D_{n,q}\le C e^{K\sqrt{\log(e+n)}}
                   q^{-2}\sqrt{\log(e+q)}.                 \tag{1}
\]
The deterministic check's simultaneous-order corollary explicitly handles
small orders using the all-order physical tube, and large orders using its
absorption estimate. Thus (1) does not conceal a \(q\)-dependent probability
event or a restriction to one selected sequence of orders. The enlarged
\(K\) in that corollary may exceed the damping exponent appearing before
the small-order extension.

The source also supplies a uniform prediction Lipschitz estimate
\[
 \sup_{t\ge0}|\widehat f_{n,q}(t,x)-f_{n,D}(t,x)|
 \le C\bigl(1+\|x\|/\sqrt d\bigr)D_{n,q}.
\]
Consequently the all-time supremum over the entire sphere
\(\{x:\|x\|=\sqrt d\}\) satisfies (1), after changing its fixed
prefactor. This is stronger than an integral norm over that sphere. The
source separately gives the norm with the time supremum inside the integral
for every fixed query law of finite second moment. Physical convergence of
both paths includes their fitted endpoints in these bounds.

These are same-width closure-to-dense statements. There is no population
comparison or additive width-bias remainder in (1). They remain inherited
internal research results, not maintained-book or manuscript theorems.

Precisely, the fixed-confidence consequence is
\[
 \forall\delta\in(0,1)\ \exists N_\delta\ 
 \forall n\ge N_\delta:\quad \Pr(\Omega_n)\ge1-\delta.
\]
Neither the result nor \(\Pr(\Omega_n)\to1\) alone supplies
\(\Pr(\bigcap_{n\ge N}\Omega_n)\ge1-\delta\).

## 2. Fresh reconstruction of the elementary schedule

Set \(s=\log(e+n)\), and define the integer memory order
\[
 q_n=\left\lceil n^{1/4}e^{s^{3/4}}\right\rceil.
\]
For integers \(n\ge1\), the expression inside the ceiling is at least one,
so
\[
 n^{1/4}e^{s^{3/4}}\le q_n\le2n^{1/4}e^{s^{3/4}}.
\]
Using \(n^{1/4}\le e^{s/4}\), then \(s^{3/4}\le s\) and \(s\ge1\),
gives
\[
 \log(e+q_n)
 \le \log(e+2)+s/4+s^{3/4}\le4s.
\]
Substitution in (1) therefore bounds the parameter or whole-sphere error by
\[
 \frac C{\sqrt n}\,
 2\sqrt s\exp\bigl(K\sqrt s-2s^{3/4}\bigr).             \tag{2}
\]
If \(s\ge\max(1,K^4)\), then \(K\sqrt s\le s^{3/4}\).
The function \(2\sqrt s e^{-s^{3/4}}\) decreases for \(s\ge1\), since
its logarithmic derivative is
\[
 \frac1{2s}-\frac34s^{-1/4}<0.
\]
Its value at one is \(2/e<1\), proving the asserted \(C/\sqrt n\)
bound with the prefactor already chosen in (1). In fact the multiplier in
(2) tends to zero, so this schedule gives \(o(n^{-1/2})\) within the
inherited estimate.

For real \(q\ge1\), the logarithmic derivative of
\(q^{-2}\sqrt{\log(e+q)}\) is
\[
 -\frac2q+\frac{1}{2(e+q)\log(e+q)}<0.
\]
Thus the same event and prefactor control every integer \(q\ge q_n\).
At fixed confidence, both the inherited condition \(n\ge N_\delta\)
and the explicit sufficient condition \(\log(e+n)\ge K^4\) must hold.
The order schedule itself contains no unknown coefficient.

Finally,
\[
 \frac{\log q_n}{\log n}
 =\frac14+\frac{[\log(e+n)]^{3/4}}{\log n}+o(1)
 \longrightarrow\frac14,
\]
where the ceiling contributes \(o(1)\). Hence
\(q_n=n^{1/4+o(1)}\), and
\(\log(q_n/n)=-\tfrac34\log n+[\log(e+n)]^{3/4}+o(1)\to-\infty\),
which proves \(q_n=o(n)\).

## 3. Fresh state and accuracy accounting

For the stated unreduced \(m\)-sample implementation, the moving arrays are:

- two families of \(n\)-vector memories for each of \(L-1\) reconstructed
  layers, \(m\) samples, and \(q\) modes: \(2(L-1)mnq\) coordinates;
- the first-layer matrix and readout: \(nd+n\) coordinates;
- the scalar clock: one coordinate.

The specified moving representation therefore has exactly
\[
 2(L-1)mnq+n(d+1)+1
\]
coordinates. An exact symmetry quotient can reduce the sample count; the
display is not a minimum over all possible encodings. Reconstructed hidden
matrices are functions of this state rather than additional trained state.
The fixed Gaussian hidden mixers require \((L-1)n^2\) stored real numbers
under the stated explicit-matrix representation. Fixed training data, fixed
activation specifications, and computable Legendre coefficients do not alter
the leading storage exponents at fixed \(L,m,d\).

At \(q=q_n\), the moving state is \(n^{5/4+o(1)}\), whereas storage
including the fixed mixers is \(\Theta(n^2)\), since \(q_n=o(n)\) and
\(L\ge2\). For a prescribed small error \(\epsilon>0\), choose an integer
\(n\) above the two sufficient-width thresholds and with
\(C/\sqrt n\le\epsilon\). For fixed constants and confidence, one may
take \(n=\Theta(\epsilon^{-2})\) as \(\epsilon\downarrow0\).
The corresponding sufficient moving storage is
\[
 \epsilon^{-5/2+o(1)},
\]
and total storage including the explicit fixed mixers is
\(\Theta(\epsilon^{-4})\). These exponents describe this sufficient
construction and target choice, not an optimal lower bound.

## 4. Source limitations and checked versions

No additional scientific assumption or theorem-scope gap was found in this
reuse. The source and its complete check records explicitly record the
unbounded-value extension, local-insertion dependency resolution, all-time
probability argument, and simultaneous-order deterministic corollary. This
scoped check relies on that inherited theorem and does not independently
recertify its full insertion/probability proof.

The numerical values of the label threshold, \(C,K\), and \(N_\delta\)
remain unspecified by these inputs. Accordingly this check proves an
asymptotic sufficient schedule and storage cost, not a usable numerical
width/order prescription at a chosen confidence. The special two-tanh result
referenced by the reuse note was outside this assignment and was not audited.

SHA-256 fingerprints of the complete inputs checked:

| Input | SHA-256 |
|---|---|
| INTEGRATED_LEGENDRE_REUSE.md | 7f2ef577114130f4a72b5b41b805de647db8cda7d0a2873e0379271f327089df |
| DEPTH_EXTENSION_RESULT.md | 6867c597f5efc368ba54b2ce9d810c653a54a2788ece2e748a8b8d98c487ce11 |
| DEPTH_TRACKING_CHECK.md | 29bbe7bd36317527f03a7cdaf61f24bf5742b3623dfea36c5bbbffe6502430c7 |
| UNBOUNDED_ACTIVATION_CHECK.md | 12884770ecde1f8de5b503ab7d62dadc1fe4e1541f3cf1cf2c7c3b7e9c5954fd |
| ACTIVATION_EXTENSION_CHECK.md | 339f234216b91a33113698b05cd7a404509f965b1cf35de2f35fb3c4d9f3adea |
