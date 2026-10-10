# Residual-clock regularity and the present Legendre proof

This is a bounded mathematical assessment dated 2026-10-09. Its scientific
inputs are the current `paper/compact.tex`, the complete proof of the first
Legendre construction in `paper/compact_legendre.tex`,
`paper/compact_fitting.tex`, and only the public analytic-source proposition
in `paper/compact_foundations.tex`. No other study, historical version, or
experiment was used. The paper has not been edited.

The question is whether analyticity of the activations upgrades the current
Legendre history approximation to a polylogarithmic order while retaining
the same whole-sphere, all-physical-time prediction guarantee. There are
two distinct obstacles to that proposed argument: the actual histories are
not globally analytic in their clock, and the current sufficient stability
threshold is itself larger than every fixed power of `log n`. Neither
obstacle, by itself, is a lower bound on the prediction error of the
nonlinear closure.

## 1. The actual clock and histories

Fix a finite width and a finite Legendre order. Hats denote the compressed
trajectory. Its residual RMS and clock are

\[
\widehat\rho(t)=\frac{\|\widehat r(t)\|_2}{\sqrt m},\qquad
\tau(t)=1+\int_0^t\widehat\rho(s)\,ds.
\]

Here \(\widehat r_a=\widehat f(x_a)-y_a\), and the forward and backward
network fields retain the paper's normalizations. The histories used in
the proof, at each relevant hidden interface, are

\[
h_a(\tau(t))=\widehat h_a(t),\qquad
b_a(\tau(t))=
\frac{\widehat r_a(t)}{\widehat\rho(t)}\widehat\delta_a(t).
\]

They are extended to the artificial initial interval by

\[
h_a(\xi)=h_{0,a},\qquad b_a(\xi)=0
\quad(0\leq\xi\leq1).
\]

The local fitting result gives \(\widehat\rho(t)>0\) at every finite
time, since \(Y>0\), and
\(1<\tau(\infty)\leq1+4Y/\lambda\), with
\(\lambda=\gamma/m\). Thus the join \(\xi=1\) is an interior point of
every projection interval \([0,\tau(t)]\) with \(t>0\).

At a fixed finite time the physical vector field is locally real analytic:
the activations are real analytic, \(\tau>0\), and the residual norm has a
local analytic square-root branch because the residual is nonzero. The
inverse change from physical time to the clock is also locally analytic.
This observation concerns the right side of the join. It does not make
the constant prefix agree analytically with that continuation.

## 2. Exact initial derivatives expose the join

Define the initial top-feature matrix
\(\mathsf H_0=[h_{0,1}^{(L)},\ldots,h_{0,m}^{(L)}]\in\mathbb R^{n\times m}\)
and the initial readout velocity

\[
\dot{\widehat w}(0)=\frac2m\mathsf H_0y.
\]

Since the initial readout is zero, every initial backward response is zero.
The first derivatives of all physical hidden matrices, including the first
matrix, vanish. Consequently
\(\dot{\widehat h}_a^{(j)}(0)=0\) and
\(\dot\tau(0)=Y\). The derivative of a backward response at zero is
obtained by applying the initialized backward recursion to
\(\dot{\widehat w}(0)\):

\[
\begin{aligned}
\dot{\widehat\delta}_a^{(L)}(0)
 &=\phi_L'(z_{0,a}^{(L)})\odot\frac2m\mathsf H_0y,\\
\dot{\widehat\delta}_a^{(j)}(0)
 &=\phi_j'(z_{0,a}^{(j)})\odot
 W_0^{(j+1)\top}\dot{\widehat\delta}_a^{(j+1)}(0)
 \quad(j<L).
\end{aligned}
\]

Terms differentiating a gate or a mixer multiply an initially zero
backward response and hence vanish. The clock derivative of the backward
history at the join is therefore exactly

\[
\partial_\xi b_a^{(\ell)}(1+)
=-\frac{y_a}{Y^2}\dot{\widehat\delta}_a^{(\ell)}(0),
\qquad
\partial_\xi b_a^{(\ell)}(1-)=0.                 \tag{1}
\]

The derivative of \(\widehat r_a/\widehat\rho\) does not contribute to
(1), since \(\widehat\delta_a(0)=0\). In contrast,

\[
\partial_\xi h_a^{(j)}(1+)=0,
\qquad
\partial_\xi^2 h_a^{(j)}(1+)
=\frac{\ddot{\widehat h}_a^{(j)}(0)}{Y^2},
\qquad
\partial_\xi^2 h_a^{(j)}(1-)=0.                 \tag{2}
\]

The second physical derivatives of the matrices coincide with those of
dense training at initialization:

\[
\begin{aligned}
\ddot{\widehat W}^{(1)}(0)
 &=\frac2m\sum_c y_c
      \dot{\widehat\delta}_c^{(1)}(0)v_c^\top,\\
\ddot{\widehat W}^{(\ell)}(0)
 &=\frac2{mn}\sum_c y_c
      \dot{\widehat\delta}_c^{(\ell)}(0)
      h_{0,c}^{(\ell-1)\top}\quad(\ell\geq2).
\end{aligned}
\]

One way to check this for the reconstructed hidden matrices is to
differentiate their moment formula: every backward moment and its first
derivative is initially zero, only the zeroth forward moment is initially
nonzero, and its paired backward second derivative is
\(-y_c\dot{\widehat\delta}_c^{(\ell)}(0)\). Thus the displayed
second derivative is independent of the truncation order. Differentiating
the forward pass gives

\[
\begin{aligned}
\ddot{\widehat h}^{(1)}_a(0)
 &=\phi_1'(z_{0,a}^{(1)})\odot
        \ddot{\widehat W}^{(1)}(0)v_a,\\
\ddot{\widehat h}^{(j)}_a(0)
 &=\phi_j'(z_{0,a}^{(j)})\odot
 \left[\ddot{\widehat W}^{(j)}(0)h_{0,a}^{(j-1)}
       +W_0^{(j)}\ddot{\widehat h}^{(j-1)}_a(0)\right].
\end{aligned}
\]

Thus a nonzero vector in (1) gives a continuous history which is not
\(C^1\), and a nonzero vector in (2) gives a \(C^1\) history which is
not \(C^2\). These are exact finite-width statements, not asymptotic
estimates.

There is a simple admissible example in which both failures are forced.
Take \(L=2\), identity activations, \(d=m\), and orthonormal normalized
training inputs \(v_a\). The population Gram is the identity, so
\(\gamma=1\); choose any nonzero labels satisfying the stated small-label
cap. On the initialization event, \(\mathsf H_0y\neq0\). For every
sample with \(y_a\neq0\),

\[
\partial_\xi b_a^{(2)}(1+)
=-\frac{2y_a}{mY^2}\mathsf H_0y\neq0.
\]

The Gaussian square mixer \(W_0^{(2)}\) is invertible with probability
one, and orthogonality of the training inputs gives

\[
\ddot{\widehat h}_a^{(1)}(0)
=\frac{4y_a}{m^2}W_0^{(2)\top}\mathsf H_0y\neq0.
\]

Both statements hold for every finite order. Identity activations are
entire and have bounded strip derivatives; their use here satisfies the
stated activation assumptions. In particular, the join problem cannot
be removed merely by strengthening strip analyticity to entire
activations.

## 3. What this proves about polynomial tails

The implication needed here has a short direct proof. For a continuous
vector-valued history \(g\) on \([0,A]\), let

\[
E_q=\|(I-\Pi_q^A)g\|_{L^2([0,A])}.
\]

If constants \(C,c,\alpha>0\), independent of the integer \(q\),
satisfy

\[
E_q\leq C\exp(-cq^\alpha)\quad\text{for all sufficiently large }q,
                                                               \tag{3}
\]

then \(g\) is \(C^\infty\) on the closed interval. Indeed, write
\(g=\sum_{j\geq0}c_jp_j^A\) in \(L^2\), where
\(p_j^A(\xi)=P_j(2\xi/A-1)\). Orthogonality yields

\[
\|c_j\|\leq\sqrt{\frac{2j+1}{A}}E_j.
\]

The derivative recurrence established in the paper,
\(P'_j=\sum_{i<j,\,j-i\ {m odd}}(2i+1)P_i\), has nonnegative
coefficients. Iterating it and using \(\|P_i\|_\infty\leq1\) shows
that the supremum of each fixed derivative is bounded by its value at
one. Expanding Rodrigues' formula about one gives, for \(j\geq k\),

\[
P_j^{(k)}(1)=\frac{(j+k)!}{2^k k!(j-k)!},\qquad
\|(p_j^A)^{(k)}\|_\infty\leq C_{A,k}(1+j)^{2k}.
\]

Thus (3) makes
\(\sum_j\|c_j\|\|(p_j^A)^{(k)}\|_\infty\) finite for every fixed
\(k\). Uniform convergence of these derivative series gives a smooth
function equal to \(g\) in \(L^2\); continuity identifies it with
\(g\) everywhere. This proves the implication without an external
approximation theorem.

Applying it to any fixed \(A=\tau(t)>1\) and the nonsmooth histories
above shows that they admit no bound (3), including ordinary exponential
tails and every stretched-exponential tail. More generally, no nonconstant
history that equals a constant on an open prefix can have an analytic
extension through the whole interval: uniqueness of analytic continuation
would force that extension to remain constant.

For a *fixed history*, a polynomial degree bounded by a fixed power of
\(\log(1/\varepsilon)\) for every sufficiently small approximation
tolerance \(\varepsilon\) would imply a bound of the form (3), and is
therefore excluded by the derivative jump. This statement keeps the
history fixed. It does not silently identify histories at different
network widths or at different closure orders: changing the order changes
the closure trajectory itself.

These results do **not** supply a prediction lower bound. The physical
defect is the product

\[
\mathcal E_\ell(t)=\frac{2\widehat\rho(t)}{mn}
\sum_a e_{b,a}^{(\ell)}(t)e_{h,a}^{(\ell-1)}(t)^\top,
\qquad
e_g(t)=g(\tau(t))-(\Pi_q^{\tau(t)}g)(\tau(t)).
\]

A lower bound on one history tail does not give a lower bound on this
product, its sample sum, its time integral, or the resulting scalar
prediction. The present proof bounds all those operations from above by
norm inequalities. Reversing them is unjustified. An impossibility theorem
for polylogarithmic-order prediction accuracy would require a separate
argument controlling those cancellations and the observable's sensitivity.

## 4. The fitted clock endpoint is a second issue

Even after addressing the artificial prefix, finite physical-time
analyticity does not imply analyticity at the fitted clock endpoint
\(A_\infty=\tau(\infty)\). The derivative transformation is

\[
\partial_\xi=\widehat\rho(t)^{-1}\partial_t,
\]

and its factor diverges as fitting is approached. The quoted analytic
source theorem supplies a physical-time complex domain up to a finite
\(T\), together with real all-time bounds. It does not supply a complex
clock domain containing \(A_\infty\), or such a domain for the closure
histories with their normalized residual factors.

An explicit analytic least-squares example isolates the issue. It is an
example of a residual equation, **not** a claimed counterexample to the
full Gaussian neural-network theorem. Let two residual components satisfy

\[
r_1(t)=-a e^{-\alpha t},\qquad
r_2(t)=-b e^{-\beta t},\qquad
a,b>0,\quad0<\alpha<\beta,
\]

and put \(\rho=\sqrt{(r_1^2+r_2^2)/2}\),
\(\tau(t)=1+\int_0^t\rho\). For an explicit least-squares realization,
take \(F(\theta)=(\sqrt\alpha\,\theta_1,\sqrt\beta\,\theta_2)\),
labels \((a,b)\), initial state \(\theta=0\), and Euclidean gradient
flow of \(\|F(\theta)-(a,b)\|_2^2/2\). Then
\(\dot r=-\operatorname{diag}(\alpha,\beta)r\). Write
\(s=A_\infty-\tau(t)\) and \(\nu=\beta/\alpha-1>0\). Direct
integration of the square-root expansion gives

\[
s=\frac{a}{\sqrt2\alpha}e^{-\alpha t}
\left[1+\frac{b^2}{2a^2}\frac{\alpha}{2\beta-\alpha}
e^{-2(\beta-\alpha)t}
+O\!\left(e^{-4(\beta-\alpha)t}\right)\right].
\]

Consequently the normalized second residual satisfies

\[
\frac{r_2(t)}{\rho(t)}
=-\frac{\sqrt2 b}{a}
\left(\frac{\sqrt2\alpha}{a}s\right)^\nu
\left[1+O(s^{2\nu})\right].                  \tag{4}
\]

For noninteger \(\nu\), (4) is incompatible with an analytic function
of \(s\) at zero: a nonzero analytic function has an integer order of
vanishing. Taking \(1<\beta/\alpha<2\) even gives a normalized residual
which is not differentiable at the fitted clock endpoint. Multiplying it
by a response with nonzero limiting value can retain that singularity;
whether a particular neural trajectory cancels it requires further proof.

Thus positivity of a residual gap and analyticity in physical time do not,
by themselves, furnish the missing clock analyticity. The current proof's
freezing of the comparison history after a finite \(t_q\) is consistent
with this limitation and avoids asserting endpoint regularity.

## 5. The literal absorption threshold is not polylogarithmic

For this calculation use only the coefficients defined inside the current
Legendre proof. Set
\(X=\beta^L\), \(z=Y/\lambda>0\),
\(u=\sqrt{\log(en)}\). They obey

\[
M=32X^{21}zu,
\qquad
\mathcal A_n=\sqrt{L+1}\exp\{14(K_0+K_1M)z\}.
\]

All fixed-problem factors \(K_0,K_1\) are independent of width. In
particular \(K_1>0\) under their literal definitions, which take the
second-derivative envelope to be at least one. Therefore

\[
\mathcal A_n=\sqrt{L+1}e^{14K_0z}e^{c u},
\qquad c=448K_1X^{21}z^2>0.
\]

The proof's response-discrepancy coefficient has the form

\[
B_d=s_0T_0^{L-1}(1+B_\delta)
 +Lt_2F_zT_0^{L-1}M =b_{d,0}+b_{d,1}u,
\]

where \(s_0\) denotes the paper's derivative envelope called \(s\),
to distinguish it from the endpoint distance used above. Both
\(b_{d,0},b_{d,1}\) are positive fixed-problem constants. The quantities
\(F_h\) and \(a_0=4z\) are also positive fixed-problem constants. Hence
the *specified sufficient threshold*

\[
q_{\rm abs}=4(L-1)F_h B_d\sqrt{a_0}\,\mathcal A_n
\]

satisfies the stronger explicit statement

\[
q_{\rm abs}=\Theta_{\rm problem}\!\left(
\sqrt{\log(en)}\,
e^{c\sqrt{\log(en)}}\right).
\]

For every fixed \(p>0\),

\[
\log\frac{q_{\rm abs}}{[\log(en)]^p}
=c\sqrt{\log(en)}
 +(\tfrac12-p)\log\log(en)+O_{\rm problem}(1)
\longrightarrow+\infty.
\]

At the same time \(\log q_{\rm abs}/\log n\to0\), so
\(q_{\rm abs}=n^{o(1)}\). The two classifications are different.
The small-label cap makes \(c\) small but, for a fixed nonzero label
vector, does not make it zero. Thus the current proof cannot accept
\(q=(\log n)^p\) in its absorption step merely from the statement
\(q_{\rm abs}=n^{o(1)}\). This is a limitation of the displayed
sufficient criterion, not a lower bound on a necessary dynamical order.

## Bounded conclusion

The current scheme already has analytically admissible examples whose
actual prefixed histories fail finite-order smoothness. Therefore an
upgrade of the current proof based on globally exponential Legendre tails
of those histories is false. The residual clock adds a separate possible
endpoint singularity, and the literal stability threshold is
superpolylogarithmic. Establishing polylogarithmic-order prediction accuracy
for the unmodified model remains open in this assessment; it would need
an argument that bypasses these history and stability estimates. A
construction that changes the prefix, basis, clock, or feedback would
require its own initialization, autonomy, stability, and all-time
whole-sphere comparison proof.
