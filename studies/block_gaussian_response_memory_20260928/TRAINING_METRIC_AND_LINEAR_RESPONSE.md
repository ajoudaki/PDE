# Which initialization estimate matters for training?

This note derives a quantitative all-time consequence of the initialization
estimates in INITIALIZATION_UPPER.md. The consequence concerns the first
derivative with respect to label amplitude at zero labels. It does not assert
an approximation theorem for a fixed nonzero label amplitude. The final
section identifies a sufficient trained-history estimate for that stronger
theorem, without assuming it has been established.

All results here are internal derivations in this study. No earlier study is
a proof dependency.

## 1. Canonical model and the observable

There are L hidden layers of width n, m training inputs, and scalar output

\[
z^{(1)}(x)=W^{(1)}x/\sqrt d,\qquad
z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),\qquad
h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad
f(x)=w^T h^{(L)}(x)/n.
\]

The loss is \(m^{-1}\sum_a r_a^2\), with \(r_a=f(x_a)-y_a\).
Use the canonical equations

\[
\dot w=-\frac2m\sum_a r_a h_a^{(L)},\qquad
\dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}x_a^T/\sqrt d,
\qquad
\dot W^{(\ell)}=-\frac2{nm}\sum_a r_a\delta_a^{(\ell)}
                      (h_a^{(\ell-1)})^T\quad(2\leq\ell\leq L),
\]

where \(\delta_a^{(L)}=w\odot\phi_L'(z_a^{(L)})\) and ordinary
backpropagation defines the preceding \(\delta\)'s. The readout is initially
zero. In the block model only the initialized hidden matrices are block
diagonal. All their entries remain trainable under these equations.

For predictors on a test-input probability law \(\mu\), define the strong
test discrepancy

\[
\mathcal E_\mu(f,g)
=\left(\int\sup_{t\geq0}|f(t,x)-g(t,x)|^2\,d\mu(x)\right)^{1/2}.
\tag{1}
\]

It bounds test RMSE at every physical time, and also bounds the supremum in
time of that RMSE. A deterministic supremum over every input is stronger.
Neither should be confused with parameter distance or operator-norm
approximation of the initialized matrices.

Since \(w(0)=0\), every initial prediction is exactly zero. The useful
initialization observable is instead

\[
K_n(x,x')=n^{-1}(h^{(L)}(0,x))^T h^{(L)}(0,x').
\tag{2}
\]

It determines the first prediction velocity and the entire first-label
response, as shown next.

## 2. Exact first-label response of the full gradient flow

Set \(y_a=a v_a\), where \(\|v\|_2=\sqrt m\), and differentiate with
respect to the scalar a at a=0. Write

\[
g_n(t,x)=\left.\frac{\partial f_n(t,x;a)}{\partial a}\right|_{a=0}.
\tag{3}
\]

This is defined by differentiating a fixed finite network at each finite
time. Smooth activations give the required differentiability of the ODE.
For bounded smooth activations the finite gradient flow exists on every
finite interval: the loss dissipation bounds the squared gradient in the
fixed positive mobility metric, hence the parameter displacement on such
an interval by Cauchy--Schwarz. It cannot escape to infinity in finite time.

At a=0 the network is stationary: w=0, r=0 and every backward signal is
zero. The derivative of each hidden update is therefore zero, because
that update contains the product r times a backward signal. Thus every
first-label derivative of a hidden weight vanishes. Differentiating the
readout equation leaves

\[
\dot w^{[1]}=-\frac2m\sum_a(g_n(t,x_a)-v_a)h^{(L)}(0,x_a).
\]

Introduce only the finite training matrix and test vector

\[
\Gamma_n=\frac1m(K_n(x_a,x_b))_{a,b},\qquad
b_n(x)=\frac1m(K_n(x,x_a))_a.
\]

The training derivative obeys
\(\dot g_{n,\mathrm{tr}}=-2\Gamma_n(g_{n,\mathrm{tr}}-v)\), so

\[
g_{n,\mathrm{tr}}(t)=(I-e^{-2\Gamma_nt})v,\qquad
g_n(t,x)=2\int_0^t b_n(x)^T e^{-2\Gamma_ns}v\,ds.
\tag{4}
\]

These formulas concern the exact canonical dynamics differentiated at
zero labels. They do not replace the nonlinear dynamics at nonzero labels
by a frozen kernel. In particular, no claim of uniform differentiability
in t or exchange between population limits and differentiation is used.

## 3. All-time block-to-dense comparison for this response

Assume the C_b^4 activation hypotheses of INITIALIZATION_UPPER.md. Write
K for its dense population kernel at layer L and K^(k) for the block
population kernel. Let D=D_L and V=V_L be the explicit constants there,
and M=\(\|\phi_L\|_\infty\). Then

\[
\sup_{x,x'}|K^{(k)}(x,x')-K(x,x')|\leq D/k.
\tag{5}
\]

Assume the dense normalized training Gram
\(\Gamma=(K(x_a,x_b)/m)_{a,b}\) has gap
\(\lambda_{\min}(\Gamma)\geq\gamma>0\).
Define g and g^(k) by (4) with these deterministic population kernels.
They are the limits of the finite-network first-label responses; this
derivative-first construction avoids asserting an interchange of limits.

**Theorem.** For every \(k\geq2D/\gamma\),

\[
\boxed{
\sup_{t\geq0}\sup_{x\in\mathbb R^d}
 |g^{(k)}(t,x)-g(t,x)|
\leq\frac{2D}{k}\left(\frac1\gamma+\frac{M^2}{\gamma^2}\right).
}
\tag{6}
\]

Consequently the same bound holds for (1) under any test probability law.
The constants are independent of width, block size and physical time.
They depend on depth, activation bounds and the initial training gap.

**Proof.** Equation (5) implies

\[
\|\Gamma^{(k)}-\Gamma\|_{\mathrm{op}}\leq D/k,
\quad
\|b^{(k)}(x)-b(x)\|_2\leq D/(k\sqrt m),
\quad \|b(x)\|_2\leq M^2/\sqrt m.
\]

Thus \(\Gamma^{(k)}\succeq(\gamma/2)I\). More generally write
\(\lambda_k=\lambda_{\min}(\Gamma^{(k)})\geq\gamma/2\).
The difference between the two integrals (4) splits into a test-vector
difference and a semigroup difference. The first has magnitude at most
\(D/(k\lambda_k)\). Duhamel's identity gives

\[
e^{-2\Gamma^{(k)}s}-e^{-2\Gamma s}
=-2\int_0^s e^{-2\Gamma^{(k)}(s-u)}
 (\Gamma^{(k)}-\Gamma)e^{-2\Gamma u}\,du.
\]

Integrating its norm over s from zero to infinity gives

\[
\int_0^\infty
\|e^{-2\Gamma^{(k)}s}-e^{-2\Gamma s}\|_{\mathrm{op}}ds
\leq\frac{\|\Gamma^{(k)}-\Gamma\|_{\mathrm{op}}}
 {2\lambda_k\gamma}.
\]

The second prediction term is therefore at most
\(M^2D/(k\lambda_k\gamma)\). Use \(\lambda_k\geq\gamma/2\) to
obtain (6), uniformly in x and the integration upper endpoint. This proves
the theorem.

The gap is a property of the particular inputs and activation. Distinct
or nonparallel inputs do not by themselves replace that hypothesis for
every activation, depth and label symmetry.

## 4. A finite-width all-time response estimate

The initialization theorem also gives a complete sampling statement for
this same linear response. Let n=Bk and put

\[
\delta_{n,k}^2=D^2/k^2+V/n.
\]

Let \(g_{n,k}\) be (3) for a randomly initialized block network. For
every test probability law \(\mu\), and failure probability p in (0,1),
if \(\sqrt{2/p}\,\delta_{n,k}\leq\gamma/2\), then with probability
at least 1-p,

\[
\boxed{
\mathcal E_\mu(g_{n,k},g)
\leq2\left(\frac1\gamma+\frac{M^2}{\gamma^2}\right)
        \sqrt{\frac2p}\,\delta_{n,k}.
}
\tag{7}
\]

**Proof.** Put
\(A=\|\Gamma_{n,k}-\Gamma\|_{\mathrm{op}}\) and
\(c(x)=\sqrt m\|b_{n,k}(x)-b(x)\|_2\).
The per-entry second-moment kernel estimate, summed with the displayed
normalizations, gives

\[
\mathbb E A^2\leq\delta_{n,k}^2,\qquad
\mathbb E\int c(x)^2d\mu(x)\leq\delta_{n,k}^2.
\]

The second statement follows by Tonelli; no uniform empirical-process
bound over x is needed. With probability at least 1-p, Markov's inequality
gives \(A^2+\int c^2d\mu\leq2\delta_{n,k}^2/p\). On that event
the empirical training gap is at least \(\gamma/2\). The proof of (6),
now with the actual random A and c(x), gives

\[
\sup_t|g_{n,k}(t,x)-g(t,x)|
\leq 2c(x)/\gamma+2M^2A/\gamma^2.
\]

Minkowski's inequality proves (7).

The supremum over time in (7) is inside the test integral. A supremum
over all test inputs *after* sampling is a different empirical-process
question and is not claimed. The deterministic population bound (6) does
permit that supremum.

## 5. Why this is not yet the nonlinear all-time theorem

The linear response fixes the coefficient of label amplitude a at a=0.
Even an expansion \(f(t,x;a)=a g(t,x)+O(a^3)\) on finite intervals
would not prove an O(1/k) block-to-dense discrepancy at fixed a: a remainder
bound O(a^3) that does not vanish with k is insufficient. Neither a
uniform-in-time nonlinear remainder nor its block-size decay has been
established here.

The training metric needed beyond initialization is visible from an exact
identity. In either a dense or a block model with zero initial readout,
integrating its readout equation gives

\[
f(t,x)=-\frac2m\sum_a\int_0^t
 r_a(s)Q(t,x;s,x_a)\,ds,
\quad
Q(t,x;s,x')=\frac1n h^{(L)}(t,x)^T h^{(L)}(s,x').
\tag{8}
\]

This identity also holds for a moment closure whenever its readout follows
the canonical equation. At initialization Q reduces to K. Later Q is a
two-time covariance of *trained*, correlated features.

Here is an explicit sufficient comparison principle, useful for specifying
the remaining obligation. It is not a claim that a block model satisfies
its hypotheses. Let models 1 and 0 have the same labels and zero initial
output; set

\[
\Gamma_j(t,s)=\big(Q_j(t,x_a;s,x_b)/m\big)_{a,b},\qquad
b_j(t,s;x)=\big(Q_j(t,x;s,x_a)/m\big)_a.
\]

Assume the reference satisfies

\[
\Gamma_0(t,t)\succeq\gamma I,\qquad
\|\partial_t\Gamma_0(t,s)\|_{\mathrm{op}}\leq a(t)
\quad(0\leq s\leq t),\qquad
A_*:=\int_0^\infty a(t)dt<\infty.
\tag{9}
\]

Assume the reference features are bounded by M, and the kernels are
absolutely continuous in their first time variable with integrable
expressions below. Define the normalized accumulated training source

\[
D(t)=-2\int_0^t[\Gamma_1(t,s)-\Gamma_0(t,s)]r_1(s)\,ds,
\qquad
V_*:=\frac1{\sqrt m}\int_0^\infty\|\dot D(t)\|_2dt,
\]

and the direct test source

\[
D_x(t)=-2\int_0^t[b_1(t,s;x)-b_0(t,s;x)]^T r_1(s)\,ds,
\qquad
U_\mu:=\left(\int\sup_t|D_x(t)|^2d\mu(x)\right)^{1/2}.
\]

Then the exact comparison satisfies

\[
\boxed{\mathcal E_\mu(f_1,f_0)
\leq U_\mu+\frac{M^2}{\gamma}e^{A_*/\gamma}V_*.}
\tag{10}
\]

To prove it, subtract (8) on the training inputs. With
\(e=r_1-r_0\),

\[
e(t)=D(t)-2\int_0^t\Gamma_0(t,s)e(s)\,ds.
\]

Differentiate and use variation of constants for
\(\dot e+2\Gamma_0(t,t)e\); its propagator contracts at rate 2γ,
as follows by differentiating the squared Euclidean norm. If
\(F(t)=\int_0^t\|e(s)\|_2ds/\sqrt m\), integration of this
variation-of-constants estimate gives

\[
F(t)\leq\frac{V_*}{2\gamma}
  +\frac1\gamma\int_0^t a(u)F(u)du.
\]

The elementary integral Gronwall inequality yields
\(F(\infty)\leq V_* e^{A_*/\gamma}/(2\gamma)\).
Subtracting (8) at a test input gives
\(f_1-f_0=D_x-2\int b_0^T e\).
Since \(\sqrt m\|b_0\|_2\leq M^2\), this proves (10).

For clarity, the source variation can be bounded directly by

\[
V_*\leq 2\int_0^\infty
 \|\Gamma_1(t,t)-\Gamma_0(t,t)\|_{\mathrm{op}}
 \frac{\|r_1(t)\|_2}{\sqrt m}\,dt
\]
\[
\hspace{8mm}+2\int_0^\infty\int_0^t
 \|\partial_t[\Gamma_1(t,s)-\Gamma_0(t,s)]\|_{\mathrm{op}}
 \frac{\|r_1(s)\|_2}{\sqrt m}\,ds\,dt.
\tag{11}
\]

Thus a nonlinear all-time O(1/k) bridge would follow from O(1/k)
residual-weighted *trained* kernel errors in (10)--(11), together with
reference bounds (9) uniform in the approximation sizes. The initialization
recursion proves only the t=s=0 case. It neither proves (9) for the trained
block model nor the O(1/k) trained sources. The block model retains reuse
of its fixed Gaussian weights inside each k-dimensional block, so this
last step is substantive.

## 6. Scope of the result

Proved: sharp-order initialization bias O(1/k); initialization sampling
RMS O(1/sqrt(n)); and the corresponding all-time, whole-test-space bounds
for the exact first-label response, including a finite-width probability
estimate. The tanh example in BLOCK_BIAS_LOWER.md shows the population
response rate O(1/k) is attained at a fixed positive physical time.

Not proved: the same rates for fully trained fixed-nonzero-label deep
feature learning, or a uniform combined theorem in block size k and memory
order q. Equation (10) isolates rather than assumes away the missing
nonlinear comparison.
