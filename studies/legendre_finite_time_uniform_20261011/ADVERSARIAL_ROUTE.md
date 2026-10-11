# Adversarial route: finite-time uniformity in width

11 October 2026. Scoped theoretical route. This is an author-side diagnostic,
not an independent promotion review. No experiment, Git operation, paper edit,
or book edit was performed.

**Result.** No Gaussian-reachable counterexample to the requested prediction
bound was obtained. Two rigorous Gaussian examples explain why the remaining
stability question cannot be settled by bounding carrier maxima: one has
diverging actual carrier maxima and exactly zero compression error; another
has an unbounded initial rate of positive curvature in the actual dense vector
field. Neither is a counterexample to prediction tracking. An exact readout
identity also controls clock activity without bounded activation values,
small labels, fitting, or a Gram gap.

The scientific inputs were the setup in `paper/compact.tex`, the construction
and Legendre proof in `paper/compact_legendre.tex`, and the assigned notes
`AUTONOMOUS_ONE_SAMPLE.md`, `AUTONOMOUS_SCOPE.md`, and
`ACTIVATION_UNIT_LABEL_FINITE_TIME.md` in the explicitly authorized predecessor
study, together with the relevant completed checks
`AUTONOMOUS_ONE_SAMPLE_CHECK.md` and `ACTIVATION_FINITE_TIME_CHECK.md`.
The rigorous-proof, canonical-notation, neural-response-memory, and
adversarial-audit instructions were applied. No scientific input from another
route was used below.

## 1. Contract and exact equations

Fix a finite number of samples \(m\), dimension \(d\), number of hidden layers
\(L\), labels \(y_a\), normalized inputs \(v_a=x_a/\sqrt d\), and horizon
\(T<\infty\). Each activation \(\phi_\ell\) is real on the real axis,
holomorphic on a fixed strip, and has bounded first derivative there; its
values may be unbounded. The canonical forward equations are

\[
z_a^{(1)}=W^{(1)}v_a,\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),\qquad
f_a=w^\top h_a^{(L)}/n.
\]

Write \(r_a=f_a-y_a\),
\(\|u\|_m^2=m^{-1}\sum_a u_a^2\), \(\rho=\|r\|_m\), and
\(Y=\|y\|_m\). The loss is \(\mathcal L=\rho^2\). Backward responses are

\[
\delta_a^{(L)}=w\odot\phi_L'(z_a^{(L)}),\qquad
\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot
W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]

The dense field \(F\), with the paper's block mobilities, has components

\[
F_1=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\quad
F_\ell=-\frac2{mn}\sum_a r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},\quad
F_w=-\frac2m\sum_a r_a h_a^{(L)}.
\]

The original closure has its own \(\widehat r\), clock
\(\tau=1+\int_0^t\widehat\rho\), and raw moments. Its physical parameters
obey the exact identity

\[
\dot{\widehat\theta}=F(\widehat\theta)+E,\qquad E_1=E_w=0,
\]
\[
E_\ell=\frac{2\widehat\rho}{mn}\sum_a
\left[b_a^{(\ell)}-(\Pi_q^\tau b_a^{(\ell)})(\tau)\right]
\left[h_a^{(\ell-1)}-(\Pi_q^\tau h_a^{(\ell-1)})(\tau)\right]^\top.
\tag{1}
\]

Here \(\Pi_q^\tau\) is the degree-below-\(q\) orthogonal projection in
\(L^2([0,\tau])\); histories in (1) belong to the closure. The forward
history is the initialized feature on \([0,1]\), then the current feature;
the backward history is zero on \([0,1]\), then
\(b_a^{(\ell)}=(\widehat r_a/\widehat\rho)\widehat\delta_a^{(\ell)}\).
The raw ODE never divides by a residual. At initial zero residual it is
stationary; otherwise uniqueness prevents a finite regular encounter with
a zero-residual equilibrium.

The requested conclusion is a whole-sphere prediction error
\(C_{T,\delta}/q^2\), on an event of probability at least \(1-\delta\), for
all sufficiently large orders with an order floor independent of \(n\).
The readout initially vanishes, the first weights are standard Gaussian,
and hidden entries are independent \(N(0,1/n)\). Fixed finite labels are
not restricted by a smallness condition.

## 2. A readout identity eliminates one proposed obstruction

The following identities hold for the original closure before any putative
maximal endpoint, since its readout equation is unchanged. They also hold
for dense training. Set \(B(t)^2=\|w(t)\|_2^2/n\), suppressing hats within
either system. Direct differentiation gives

\[
\begin{aligned}
\frac d{dt}B^2
&=-4\langle r,f\rangle_m\\
&=Y^2-4\|f-y/2\|_m^2\\
&=2Y^2-2\rho^2-2\|f\|_m^2.
\end{aligned}
\tag{2}
\]

The second equality is completion of the square; the last uses
\(2\langle f-y,f\rangle_m=\|f-y\|_m^2+\|f\|_m^2-Y^2\).
Thus for zero initial readout, every regular interval ending at \(t\le T\)
satisfies

\[
B(t)\le Y\sqrt t,\qquad
\int_0^t\rho(s)^2\,ds\le Y^2t,\qquad
\tau(t)-1=\int_0^t\rho(s)\,ds\le Yt.
\tag{3}
\]

The final inequality is Cauchy--Schwarz. These estimates use neither an
activation bound nor closeness to dense training. In particular, finite-time
blowup of the readout RMS or the clock cannot be the first failure mode.
They do not alone bound all hidden parameters or imply full raw-state
continuation.

For comparison, dense energy also gives

\[
\frac d{dt}\mathcal L_D=-\|F(\theta_D)\|_{\mathrm{par}}^2,
\qquad
\|\theta_D(t)-\theta_0\|_{\mathrm{par}}\le Y\sqrt t,
\tag{4}
\]

where the first-layer and readout blocks in \(\|\cdot\|_{\mathrm{par}}\)
are divided by \(\sqrt n\), and hidden blocks have ordinary Frobenius norm.
Equation (4) gives dense global continuation at every finite width: it bounds
all physical parameters on every finite interval, and the smooth finite
dimensional field extends at a finite endpoint. No comparable assertion for
every closure order follows just by reusing (4).

## 3. Actual Gaussian carrier maxima can diverge with zero closure error

Take two hidden layers, one normalized training input, label \(y>0\), and
\(\phi_1\equiv1\), \(\phi_2(z)=z\). Both activations meet the strip
assumption. The same example can be repeated over any fixed number of
identical training inputs and labels. It is a diagnostic in the broad
finite-data class, not an example with a positive Gram gap for repeated data.

The first feature is the constant vector \(\mathbf1\), the first layer is
stationary, and put

\[
Z=W_0^{(2)}\mathbf1,\qquad S_n=\|Z\|_2^2/n.
\]

The coordinates \(Z_i\) are independent standard normal variables. Let
\(\alpha(0)=0\) solve

\[
\dot\alpha=2\left[y-S_n\sinh\alpha\cosh\alpha\right].
\tag{5}
\]

Then the exact dense trajectory is

\[
z^{(2)}(t)=Z\cosh\alpha(t),\qquad
w(t)=Z\sinh\alpha(t),\qquad
f(t)=S_n\sinh\alpha(t)\cosh\alpha(t).
\tag{6}
\]

Indeed \(\dot z^{(2)}=-2rw\) and \(\dot w=-2rz^{(2)}\), and (5) is
\(\dot\alpha=-2r\). The positive root of
\(S_n\sinh\alpha\cosh\alpha=y\) bounds \(\alpha\) and proves global
existence when \(S_n>0\), an event of probability one.

For every \(q\ge1\), the closure's forward history at its only compressed
interface is constant on its complete clock interval. Its projection error
therefore vanishes identically. Equation (1) gives \(E_2=0\), so the
closure and dense physical parameters agree exactly by ODE uniqueness.
The raw moments are bounded integrals on each finite interval and therefore
also continue. Prediction discrepancy is zero for every order, width,
physical time, and query.

Nevertheless, for each fixed \(t>0\), the actual top carrier \(w(t)\) has
an unbounded maximum as width grows. On \(S_n\in[1/2,2]\), scalar
comparison in (5) gives \(\alpha(t)\ge\alpha_2(t)>0\), where
\(\alpha_2\) solves (5) with \(S_n=2\). Also
\(\Pr\{S_n\notin[1/2,2]\}\to0\), since
\(\mathbb E S_n=1\), \(\operatorname{Var}(S_n)=2/n\), and Chebyshev's
inequality applies. Hence

\[
\max_i|w_i(t)|\ge\sinh(\alpha_2(t))\max_i|Z_i|.
\tag{7}
\]

For any fixed \(M\),
\(\Pr\{\max_i|Z_i|\le M\}=\Pr\{|Z_1|\le M\}^n\to0\).
In fact the maximum has order \(\sqrt{\log n}\) in probability: the
upper bound follows from
\(\Pr\{\max_i|Z_i|>2\sqrt{\log n}\}\le2/n\); a Gaussian density
integral on \([u,u+1/(u+1)]\), with \(u=\sqrt{\log n}\), makes
\(n\Pr\{|Z_1|>u\}\to\infty\) and proves the lower bound.

This is a reachable Gaussian example, with zero initialized readout and
the unchanged clock. It disproves a uniform deterministic bound on carrier
maxima with fixed confidence. It simultaneously demonstrates why that
failure is not a counterexample to width-uniform compression accuracy.

## 4. Gaussian initialization produces an unbounded initial curvature rate

A second diagnostic retains a nonlinear first gate. Take one sample with
\(d=1\), \(L=2\), \(\phi_1(u)=\sin u\), \(\phi_2(z)=z\), and label
\(y\ne0\). Write \(u=W^{(1)}\), \(W=W^{(2)}\),
\(h=\sin u\), and \(k=W^\top w\). Then

\[
f=w^\top W\sin u/n,\qquad
F_u=-2r\cos u\odot k.
\]

At an arbitrary state, the Jacobian block for first-layer perturbations is

\[
D_uF_u=-\frac2n pp^\top-2r\operatorname{diag}(\phi_1''(u)\odot k),
\qquad p=\cos u\odot k.
\tag{8}
\]

Normalization of the first-layer coordinate by \(\sqrt n\) leaves this
block unchanged. Initially \(k=0\), \(r=-y\),
\(\dot w=2yWh\), and \(\dot W=0\). Along the actual dense trajectory,

\[
\left.\frac d{dt}D_uF_u\right|_{t=0}
=4y^2\operatorname{diag}\!\left(\phi_1''(u_0)\odot W_0^\top W_0h_0\right).
\tag{9}
\]

Both the largest and the negative of the smallest diagonal entry in (9)
grow on the scale \(\sqrt{\log n}\), with probability tending to one.
Here is a direct conditional Gaussian calculation.

Condition on \(h=h_0\), put \(e=h/\|h\|_2\), and decompose the Gaussian
matrix into its action on \(e\) and its orthogonal complement. With
\(a=W_0e\), one has \(a\sim N(0,I/n)\), and the Gaussian matrix
\(W_0(I-ee^\top)\) is independent of \(a\). Consequently, conditional
on \(h,a\),

\[
W_0^\top W_0h
\ \stackrel{\mathrm{law}}=
\|a\|_2^2h+
\frac{\|h\|_2\|a\|_2}{\sqrt n}(I-ee^\top)g,
\tag{10}
\]

where \(g\) is an independent standard normal vector. The coefficient of
the Gaussian term converges in probability to
\(\sigma=(\mathbb E\sin^2 G)^{1/2}>0\), with \(G\sim N(0,1)\): this
uses bounded independent \(\sin^2 u_{0,i}\), and
\(\mathbb E\|a\|^2=1\), \(\operatorname{Var}(\|a\|^2)=2/n\).

Choose \(c\in(0,1)\) such that
\(\Pr\{|\sin G|\ge c\}>0\). With probability tending to one, a fixed
positive fraction of indices satisfy \(|h_i|\ge c\). Conditional on
these indices, the independent variables \(h_i g_i\) have variances
between \(c^2\) and one; both their positive and negative maxima have
order \(\sqrt{\log n}\), by the same elementary Gaussian tail argument
as in Section 3. The orthogonal-projection correction obeys

\[
\max_i|h_i e_i(e^\top g)|
\le\frac{|e^\top g|}{\|h\|_2}=O_{\mathbb P}(n^{-1/2}).
\]

Finally \(\phi_1''(u_i)=-h_i\); multiplying (10) by \(-h_i\) adds the
bounded term \(-\|a\|^2h_i^2\) and preserves these two diverging extrema.
This proves the assertion about (9).

This obstruction is narrower than failure of the theorem. It rules out a
width-independent bound on the initial time derivative of the dense
Jacobian based only on bounded Gaussian operator norms and RMS scales.
It does not rule out an integrable stability estimate, a weighted estimate,
or bounded amplification of the closure's particular forcing. A diverging
derivative at time zero does not by itself imply that the Jacobian at a
fixed positive time, or the observable error, diverges.

## 5. The prefix permits the requested rate; two analytic bridges remain

With zero readout, every initialized backward response vanishes. Therefore
the backward history meets its zero prefix continuously, even when the
initial normalized residual is nonzero. There is no compulsory step tail of
size \(q^{-1/2}\). The prefix creates no intrinsic \(q^{-3/2}\) lower bound
for this initialization.

For a precise sufficient mechanism, define the sample/neuron history norm
\(\|g\|_H^2=(mn)^{-1}\sum_a\|g_a\|_2^2\). Suppose, on the stopped
actual closure, one can prove width- and order-independent bounds

\[
\tau\le A_T,\quad
\sum_{\ell=2}^L\int_0^\tau
\left(\|\partial_\xi h^{(\ell-1)}\|_H^2+
\|\partial_\xi b^{(\ell)}\|_H^2\right)d\xi\le K_T^2.
\tag{11}
\]

The exact differentiated projection energy and Cauchy--Schwarz give

\[
\int_0^T\|E_\ell\|_Fdt
\le2\|(I-\Pi_q^\tau)b^{(\ell)}\|_{L^2(H)}
       \|(I-\Pi_q^\tau)h^{(\ell-1)}\|_{L^2(H)}.
\]

The weighted Legendre tail bound

\[
\|(I-\Pi_q^\tau)g\|_{L^2(H)}^2
\le\frac{\tau^2}{4q(q+1)}
\int_0^\tau\|g'\|_H^2d\xi
\]

therefore gives an accumulated absolute defect bounded by
\(C_T/[q(q+1)]\). This is the source estimate; it does not compare the
autonomous trajectories. A second sufficient bridge is a width-independent
estimate on the particular two trajectories,

\[
\sup_{t\le T}\|\widehat\theta(t)-\theta_D(t)\|_{\mathrm{par}}
\le K_{T,\delta}\int_0^T\sum_{\ell=2}^L\|E_\ell(t)\|_Fdt.
\tag{12}
\]

Equations (11)--(12), applied with a strict stopping margin, would give a
width-independent order floor and raw-state continuation. Bounded hidden
operators, the first-layer RMS norm, the readout RMS, and globally bounded
activation slopes then transfer parameter discrepancy to whole-sphere
prediction discrepancy by forward subtraction. This last step needs no
maximum over neuron coordinates and no growing input net.

The unresolved terms are concrete. If
\(k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}\), backward
differentiation contains

\[
\phi_\ell''(z_a^{(\ell)})\odot
k_a^{(\ell)}\odot\partial_\xi z_a^{(\ell)},
\tag{13}
\]

and backward comparison contains

\[
\left[\phi_\ell'(\widehat z_a^{(\ell)})-
      \phi_\ell'(z_{D,a}^{(\ell)})\right]\odot k_{D,a}^{(\ell)}.
\tag{14}
\]

RMS control of each factor does not bound the RMS of these products. The
supremum-multiplier estimate introduces width dependence, and Sections 3--4
show that Gaussian initialization does not simply make every relevant
maximum bounded. A proof must exploit actual joint distributions,
trajectory-specific correlations, a suitable weighted norm, cancellation,
or weaker observable stability. Which such mechanism suffices at arbitrary
depth and data remains open in this route.

## 6. What would constitute a counterexample

Define \(\mathcal E_{n,q}\) as the supremum prediction discrepancy over
\([0,T]\) and the input sphere, and set it to infinity if the closure
fails to exist through \(T\). A valid counterexample must violate tightness
of \(\sup_{q\ge q_0}q^2\mathcal E_{n,q}\) uniformly over the promised
width range, for every fixed candidate \(q_0\), at a fixed positive failure
probability. It is not enough to exhibit a large constant on increasingly
rare Gaussian draws, a bad bounded-operator initialization, or the
diverging maxima in Section 3.

Likewise, a finite-time instability must couple the closure's own projection
defect to an observable with nonvanishing probability. Instability in an
arbitrary parameter direction, or lack of a Lipschitz bound on an entire
parameter ball, does not establish that coupling. The curvature calculation
above establishes a genuine obstacle to a simple proof route, but supplies
neither that defect alignment nor the requisite prediction lower bound.

The requested theorem therefore remains unresolved by this adversarial
route. The exact finite-time clock bound, the absence of a zero-readout
prefix jump, and both Gaussian diagnostics are retained as proved facts.
