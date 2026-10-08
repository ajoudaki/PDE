# A short-time trajectory obstruction from initialization Grams

This is a continuation of `TYPICAL_GRAM_INFORMATION.md`, whose original
independent comparison freeze had SHA256
`ad68a8a0ba9d8a67fe5f96b00f4233b213bcba0a9c5c521980e51f4d45af6b02`.
After that freeze the supervisor supplied the conditional-pair coupling and
complex-time/Chebyshev derivative-extraction idea developed here. This extension
therefore is not an independent rediscovery of that idea. Inputs were the
original prompt-only model, the author's frozen derivation, and the new prompt.
No additional scientific source, literature, experiment, or Git operation was
used. The companion report was subsequently revised only to remove its
conflicting use of the symbol for the established gap and to state fixed-label
rescaling.

The result concerns actual prediction trajectories. For a fixed interval
\([0,T]\) and fixed nonzero labels, no predictor curve initialized solely from
the feature, derivative-feature, and mixed Grams can approximate the realized
network with error \(o_p(n^{-1/2}(\log n)^{-7})\). In particular this excludes
an \(n^{-1+o(1)}\) error claim for that information class. The logarithmic loss
is real in this proof: the result does not exclude every
\(o_p(n^{-1/2})\) error rate.

## 1. Model, retained information, and precise statement

There are two unit orthogonal inputs, width \(n\), activation \(\sin\), and
initial readout zero. Equivalently, the initial neuron coordinates
\((X_i,Y_i)\), \(1\le i\le n\), are iid with independent standard Gaussian
coordinates, and

\[
z_{1i}(0)=X_i,\quad z_{2i}(0)=Y_i,\quad w_i(0)=0.
\]

Fix \(\eta>0\), independent of \(n\), and labels
\(y_1=y_2=\eta\). The value of \(\eta\) may be arbitrarily small to meet
any fixed positive label cap. The forward pass, residuals, and loss are

\[
h_{ai}=\sin z_{ai},\qquad
f_a=\frac1n\sum_iw_i h_{ai},\qquad
c_a=\eta-f_a,\qquad
\mathcal L=\frac12(c_1^2+c_2^2).
\]

The physical-time training flow is

\[
\dot z_{ai}=c_a w_i\cos z_{ai},\quad a=1,2,
\qquad
\dot w_i=c_1\sin z_{1i}+c_2\sin z_{2i}.
\]

At initialization define

\[
r_i=(\sin X_i,\sin Y_i,\cos X_i,\cos Y_i)^\top,\qquad
\Gamma_n=\frac1n\sum_i r_i r_i^\top.
\]

This is the full collection of feature, derivative-feature, and mixed Grams.
Let \(G\) denote its upper-left \(2\times2\) feature block. A predictor
\(\widehat f_{1,n}(t)\) may be any measurable function of
\((\Gamma_n,n,\eta,t)\); no differential equation, analyticity, or continuity
is required of it. We require only that its supremum error below is measurable.
The known input geometry and distribution may also be used.

**Theorem.** There are constants \(T>0\), \(c_\eta>0\), and \(p>0\),
independent of width and predictor, such that, with
\(K_n=\lceil2\log_2 n\rceil\), every such sequence of predictors satisfies

\[
\liminf_{n\to\infty}\mathbb P\left\{
\sup_{0\le t\le T}|f_1(t)-\widehat f_{1,n}(t)|
\ge \frac{c_\eta}{\sqrt n\,K_n^7}\right\}\ge p.
\]

One valid interval is
\(T=1/[256(\eta+2)]\). The constant \(c_\eta\) is strictly positive for
every fixed \(\eta>0\) and is defined in the proof. The result also applies
to predictors using a subset of \(\Gamma_n\). It does not apply to arbitrary
finite summaries that include additional fourth-order moments.

The proof first constructs two networks with identical retained Grams but a
typical cubic-derivative difference. An analytic inequality converts that
difference into a trajectory difference. A common predictor cannot fit both
trajectories closer than half their separation.

## 2. The cubic statistic and its missing conditional randomness

Put \(U=\sin x,V=\sin y\), and define the bounded trigonometric polynomial

\[
J(x,y)=5U^2+3V^2+8UV-4U^4-7U^3V-UV^3-4U^2V^2.
\]

For the specified flow its exact initialization derivatives are

\[
\dot f(0)=\eta G\mathbf1,\qquad
\ddot f(0)=-\eta G^2\mathbf1,\qquad
f_1^{(3)}(0)=\eta(G^3\mathbf1)_1
+\frac{\eta^3}{n}\sum_iJ(X_i,Y_i),
\quad \mathbf1=(1,1)^\top.
\]

To check the nonlinear term, set
\(S=\eta(h_1+h_2)\) and \(p_a=\cos z_a(0)\). At zero readout,
\(\dot h_a=0\), \(\dot w=S\), and
\(\ddot h_a=\eta S\odot p_a^2\). The nonzero third-product-rule terms in
\(f_1=n^{-1}w^\top h_1\) are
\(n^{-1}w^{(3)\top}h_1+3n^{-1}\dot w^\top\ddot h_1\).
Here
\(w^{(3)}=\eta\sum_b(G^2\mathbf1)_bh_b+
\eta\sum_b\ddot h_b\). Substitution gives, per neuron and after factoring
\(\eta^3\),

\[
4U^2(1-U^2)+7UV(1-U^2)
+U^2(1-V^2)+UV(1-V^2)+3V^2(1-U^2),
\]

which expands to the displayed \(J\).

The information in \(\Gamma_n\) is equivalent to the average of

\[
t(x,y)=\big(\cos2x,\sin2x,\cos2y,\sin2y,
\cos(x+y),\sin(x+y),\cos(x-y),\sin(x-y)\big).
\]

Both directions of this equivalence follow from the double-angle and
product-to-sum identities. The nine functions \(1,t_1,\ldots,t_8\) are
linearly independent. The coefficient of \(\cos4x\) in \(J\) is
\(-1/2\), while that frequency is absent from every \(t_j\). Therefore
\(1,t_1,\ldots,t_8,J\) are linearly independent. Independence of the
frequencies can be checked by integration against complex exponentials over
\([0,2\pi]^2\).

Use blocks of \(b=9\) neurons and define their summary and cubic statistic by

\[
T_j=\sum_{i\in j}t(X_i,Y_i),\qquad
B_j=\sum_{i\in j}J(X_i,Y_i),\qquad
\kappa=\mathbb E\operatorname{Var}(B_j\mid T_j).
\]

The constant \(\kappa\) is finite and strictly positive. Here is a
self-contained justification of strict positivity. The derivatives of the map
\((t_1,\ldots,t_8,J):\mathbb R^2\to\mathbb R^9\), evaluated at all
points, span \(\mathbb R^9\). Otherwise a nonzero linear combination of
its components would have both partial derivatives zero everywhere and so
would be constant, contradicting the function independence. Select nine
independent derivative vectors and place the nine block neurons at their
corresponding points. The block map to \((T_j,B_j)\) has Jacobian rank nine
at this configuration. The inverse function theorem and the positive Gaussian
input density imply that the law of \((T_j,B_j)\) has a component with
positive density on a nonempty open subset of \(\mathbb R^9\). If
\(\kappa=0\), \(B_j\) would be a measurable function of \(T_j\) almost
surely, whose graph has nine-dimensional Lebesgue measure zero by Fubini's
theorem. That contradicts the positive density component.

## 3. Coupling two networks with the same retained Gram

Write \(N_n=\lfloor n/b\rfloor\). Reveal all \(T_j\),
\(1\le j\le N_n\), and reveal the individual coordinates of any leftover
neurons. Denote this information by \(\mathcal H_n\). Draw two conditionally
independent initialized networks from the original Gaussian law given
\(\mathcal H_n\). Such conditional laws exist on these finite-dimensional
Euclidean spaces. Equivalently, for each block draw two independent neuron
blocks from its conditional law given \(T_j\), independently across blocks;
the revealed leftover coordinates are shared.

Each network has exactly the original iid Gaussian initialization as its
marginal law. The two full Grams agree exactly because \(\mathcal H_n\)
determines their sums. Write their real prediction trajectories as
\(f_1^A,f_1^B\), and set

\[
D_n(t)=f_1^A(t)-f_1^B(t).
\]

The first two prediction derivatives agree, while the exact cubic identity
gives

\[
\sqrt n\,D_n^{(3)}(0)
=\frac{\eta^3}{\sqrt n}
\sum_{j=1}^{N_n}(B_j^A-B_j^B).
\]

Conditional on \(\mathcal H_n\), the block differences are independent,
have mean zero, are uniformly bounded, and have variances
\(2\operatorname{Var}(B_j\mid T_j)\). The strong law for these iid bounded
conditional-variance functions gives

\[
\frac1n\sum_{j=1}^{N_n}
2\operatorname{Var}(B_j\mid T_j)\longrightarrow\frac{2\kappa}{b}
\quad\text{almost surely}.
\]

Their conditional characteristic functions have the expansion
\(1-u^2\operatorname{Var}(B_j^A-B_j^B\mid T_j)/(2n)+O(n^{-3/2})\)
at argument \(u/\sqrt n\), uniformly in blocks and conditioning for each
fixed real \(u\). Uniform boundedness of the block variables justifies the
third-order Taylor remainder. Summing the remainders gives
\(O(n^{-1/2})\); multiplying the factors gives a conditional Gaussian limit.
After averaging the conditional laws, this proves

\[
\sqrt n\,D_n^{(3)}(0)
\ \Longrightarrow\ N(0,\eta^6\sigma^2),
\qquad \sigma^2=\frac{2\kappa}{b}>0.
\]

In particular, if \(\Phi\) is the standard Gaussian distribution function
and \(p_0=2[1-\Phi(1)]>0\),

\[
\mathbb P\left\{|D_n^{(3)}(0)|\ge
\frac{\eta^3\sigma}{\sqrt n}\right\}\longrightarrow p_0.
\]

## 4. A complex-time disk uniform in width and initialization

Extend the displayed real vector field holomorphically using the same formulas;
this is an analytic extension of the real flow, not a new complex-gradient
training rule. Use the maximum norm over all \(3n\) coordinates and the tube

\[
|z_{1i}-X_i|\le1,\quad |z_{2i}-Y_i|\le1,\quad |w_i|\le1.
\]

The initial phases \(X_i,Y_i\) are real, without any upper bound on their
magnitude. In this tube,
\(|\sin z_{ai}|,|\cos z_{ai}|\le\cosh1<2\). Hence
\(|f_a|\le2\) and \(|c_a|\le\eta+2\). The vector field has maximum
norm at most \(4(\eta+2)\).

It is Lipschitz in this tube with constant at most \(16(\eta+2)\), independent
of \(n\). To verify the dependence, two states at maximum distance \(\Delta\)
have \(|\delta f_a|\le4\Delta\). The preactivation velocity changes by
at most \([8+4(\eta+2)]\Delta\), and the readout velocity by at most
\([16+4(\eta+2)]\Delta\). Both are at most
\(16(\eta+2)\Delta\) since \(\eta+2\ge2\).
These bounds follow along segments in the convex tube from the derivative
bounds for sine and cosine.

Set

\[
R=\frac1{64(\eta+2)}.
\]

Continuous vector-valued functions on the closed complex disk \(|t|\le R\)
that are holomorphic inside form a Banach space in the supremum norm. On its
closed, complete subset of functions with the prescribed initial value and
staying in the tube, consider the Picard map, where \(\mathcal V\) is the
displayed training vector field:

\[
\Theta(t)\longmapsto\Theta(0)+\int_0^t\mathcal V(\Theta(s))\,ds.
\]

The integral may be taken along the radial segment and defines a holomorphic
primitive. The map moves each coordinate by at most
\(4(\eta+2)R=1/16\), so it preserves the tube, and its Lipschitz constant
is at most \(16(\eta+2)R=1/4\).
Its iterates therefore converge uniformly to a unique solution on this disk;
uniform convergence preserves holomorphy inside. On real times this agrees
with the specified real training flow by uniqueness. The associated prediction
is holomorphic and bounded in magnitude by \(2\).

Consequently, for every pair constructed above, \(D_n\) is holomorphic on
\(|t|<R\), continuous on the closed disk, and satisfies

\[
\sup_{|t|\le R}|D_n(t)|\le B,\qquad B=4,
\]

uniformly in width and in both real initializations.

## 5. Extracting the cubic derivative from the real-interval norm

Set \(T=R/4\) and \(a=T/2=R/8\). For any function \(D\) with the disk
property just proved, put

\[
g(x)=D(a(x+1)),\qquad
E=\sup_{0\le t\le T}|D(t)|=\sup_{-1\le x\le1}|g(x)|.
\]

Let \(T_k(x)\) now denote the degree-\(k\) Chebyshev polynomial, defined
by \(T_k(\cos\theta)=\cos(k\theta)\); it is unrelated to the block
summary \(T_j\) used earlier. Write its series as
\(g(x)=a_0+\sum_{k\ge1}a_kT_k(x)\). The real integral formula gives

\[
|a_k|\le2E\quad (k\ge1).
\]

There is also an analytic bound \(|a_k|\le2B\,2^{-k}\). To prove it,
substitute \(x=(\zeta+\zeta^{-1})/2\). On \(|\zeta|=2\),
\(|x|\le5/4\) and therefore \(|a(x+1)|\le9R/32<R\).
The resulting function of \(\zeta\) is holomorphic on an annulus containing
\(1/2\le|\zeta|\le2\), is bounded by \(B\) on \(|\zeta|=2\), and is
invariant under \(\zeta\mapsto\zeta^{-1}\). Cauchy's coefficient formula
bounds its positive Laurent coefficient of degree \(k\) by \(B2^{-k}\).
Since \(T_k((\zeta+\zeta^{-1})/2)=(\zeta^k+\zeta^{-k})/2\), this is
exactly the claimed Chebyshev coefficient bound. Restricting the Laurent
series to \(|\zeta|=1\) also gives the real integral formula.

At an endpoint the third derivative satisfies

\[
|T_k^{(3)}(-1)|
=\frac{k^2(k^2-1)(k^2-4)}{15}\le\frac{k^6}{15},\quad k\ge3.
\]

For example, the defining cosine relation gives
\((1-x^2)T_k''-xT_k'+k^2T_k=0\). Evaluation at \(x=1\), followed by one
and two differentiations of this equation, successively gives
\(T_k'(1)=k^2\),
\(T_k''(1)=k^2(k^2-1)/3\), and the displayed third derivative at \(1\).
Parity gives the magnitude at \(-1\).
The derivatives vanish for \(k=0,1,2\).

The exponentially decaying coefficient bound gives uniform convergence on
every smaller closed complex ellipse with parameter between \(1\) and \(2\).
Cauchy's derivative formula there justifies termwise differentiation on
\([-1,1]\), including at the endpoint. Thus for every integer \(K\ge3\),

\[
|D^{(3)}(0)|
\le \frac{2}{15a^3}\left[
K^7E+B C_6(K+1)^6 2^{-K}\right],
\qquad C_6=\sum_{j=1}^{\infty}j^6 2^{-j}<\infty.
\]

Indeed \(\sum_{k=1}^K k^6\le K^7\), and writing \(k=K+j\) bounds
the tail by
\(2^{-K}(K+1)^6\sum_{j\ge1}j^62^{-j}\), because
\(K+j\le(K+1)j\). The chain rule supplies the factor \(a^{-3}\).

This inequality concerns only the actual analytic network difference.
It imposes no regularity requirement on a prospective predictor.

## 6. The trajectory lower bound and the predictor transfer

Apply the inequality to \(D_n\) with
\(K=K_n=\lceil2\log_2n\rceil\). Since \(2^{-K_n}\le n^{-2}\), its
tail is \(O((\log n)^6n^{-2})=o(n^{-1/2})\). The constants depend on
fixed \(\eta\), but not on the realization or width. Thus for all
sufficiently large \(n\), the event
\(|D_n^{(3)}(0)|\ge\eta^3\sigma/\sqrt n\) implies

\[
\sup_{0\le t\le T}|D_n(t)|
\ge \frac{15a^3\eta^3\sigma}{4\sqrt n\,K_n^7}.
\]

The probability of this event converges to \(p_0>0\) by Section 3.
The pair has identical \(\Gamma_n\), so its Gram-based predictor curve is
identical for both members. For every realized pair the triangle inequality
gives

\[
\sup_t|D_n(t)|
\le \sup_t|f_1^A(t)-\widehat f_{1,n}(t)|
+\sup_t|f_1^B(t)-\widehat f_{1,n}(t)|.
\]

Both terms on the right have the original network's prediction-error
distribution, since the pair's marginals are the original Gaussian law.
A union bound, which needs no independence between these errors, therefore
proves the theorem with

\[
c_\eta=\frac{15a^3\eta^3\sigma}{8}>0,
\qquad p=\frac{p_0}{2}=1-\Phi(1)>0.
\]

Independent randomization by the predictor does not improve this lower bound:
use the same independent random seed for both coupled networks and repeat the
same argument conditionally on that seed.

## 7. What is and is not excluded

Since \(K_n\) is proportional to \(\log n\), the theorem rules out
\(o_p(n^{-1/2}(\log n)^{-7})\) error on this fixed interval. It consequently
rules out \(O_p(n^{-1+\varepsilon})\) for every fixed
\(0\le\varepsilon<1/2\), and any deterministic exponent sequence of the
form \(-1+o(1)\): those rates divided by
\(n^{-1/2}(\log n)^{-7}\) tend to zero.

The lower bound does not by itself give a constant times \(n^{-1/2}\).
For example, the rate \(n^{-1/2}/\log n\) is still compatible with this
theorem. Thus the original cubic-derivative obstruction at the dense
variability scale becomes a trajectory obstruction with a logarithmic loss;
the two statements should not be identified.

The result is for the specified one-layer sine model, two orthogonal inputs,
fixed positive labels, the realized finite network, and its initialization
Grams. It neither treats arbitrary finite observable families nor prohibits
an enriched statistic from directly retaining the cubic information. It gives
no assertion about larger architecture classes, unbounded-time stability, or
the optimal logarithmic exponent. Any error claim on an interval containing
\([0,T]\) is, however, already subject to this lower bound.

The author checked the conditional marginal laws, cancellation of the common
Gram contribution, cubic coefficient and label factors, dimension-free complex
disk constants, Chebyshev endpoint derivatives, analytic tail, and the final
union-bound factor. The proof imports no conditional-limit theorem: its
bounded-variable characteristic-function estimate is given explicitly. This
candidate awaits comparison or independent checking and is not promoted
material.
