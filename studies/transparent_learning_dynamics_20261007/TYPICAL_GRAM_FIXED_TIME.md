# A fixed-time Gram-information obstruction at the dense fluctuation scale

This note strengthens the earlier initialization-jet and logarithmic-loss
trajectory results. The supervisor supplied the bounded-difference/Taylor
remainder route after those notes were frozen; the argument below is a
continuation, not an independent rediscovery. Scientific inputs were the
specified one-layer sine model, the author's conditional-block construction,
and that new route. No literature, experiment, other-study material, or Git
operation was used. The earlier frozen trajectory note is left unchanged.

For the specified model, initialization feature and derivative Grams cannot
predict the realized network to error \(o_p(n^{-1/2})\), even at one fixed
positive time. The proof permits every measurable Gram-based predictor and
fixed labels of arbitrarily small nonzero magnitude. The scope remains this
particular information class and model; it is not a statement about arbitrary
finite observable collections.

## 1. Precise model and result

There are two orthogonal unit inputs, width \(n\), sine activation, and zero
initial readout. The pairs \((X_i,Y_i)\), \(1\le i\le n\), are independent
standard Gaussian pairs with independent coordinates. Fix \(\eta>0\),
independent of \(n\), and initialize

\[
z_{1i}(0)=X_i,\quad z_{2i}(0)=Y_i,\quad w_i(0)=0,
\qquad y_1=y_2=\eta.
\]

The forward pass, residuals, loss, and physical-time training flow are

\[
\begin{aligned}
h_{ai}&=\sin z_{ai},&
f_a&=\frac1n\sum_i w_i h_{ai},&
c_a&=\eta-f_a,&
\mathcal L&=\frac12\sum_{a=1}^2c_a^2,\\
\dot z_{ai}&=c_aw_i\cos z_{ai},&&&
\dot w_i&=c_1\sin z_{1i}+c_2\sin z_{2i}.
\end{aligned}
\]

The retained initialization information is

\[
r_i=(\sin X_i,\sin Y_i,\cos X_i,\cos Y_i)^\top,
\qquad \Gamma_n=\frac1n\sum_i r_i r_i^\top.
\]

It includes all feature, derivative-feature, and mixed Grams; its upper-left
feature block is denoted by \(G\).

**Theorem.** For every fixed \(\eta>0\) and every fixed horizon \(T>0\),
there are a deterministic time \(t_*\in(0,T]\), constants
\(a_\eta>0\) and \(p>0\), independent of \(n\) and of the estimator, such
that every sequence of measurable estimators \(F_n(\Gamma_n)\) satisfies

\[
\liminf_{n\to\infty}
\mathbb P\left\{|f_1(t_*)-F_n(\Gamma_n)|
\ge\frac{a_\eta}{\sqrt n}\right\}\ge p.
\]

The constants, including the subscripted \(a_\eta\), may also depend on
the fixed horizon \(T\). Consequently a Gram-based predictor curve cannot
achieve \(o_p(n^{-1/2})\) error uniformly on \([0,T]\). Independent
randomization by the predictor does not change the conclusion.

## 2. A coupled pair with a nondegenerate cubic fluctuation

For \(U=\sin x,V=\sin y\), define

\[
J(x,y)=5U^2+3V^2+8UV-4U^4-7U^3V-UV^3-4U^2V^2.
\]

Differentiation of the stated flow at zero readout gives

\[
\dot f(0)=\eta G\mathbf1,\qquad
\ddot f(0)=-\eta G^2\mathbf1,\qquad
f_1^{(3)}(0)=\eta(G^3\mathbf1)_1
+\frac{\eta^3}{n}\sum_iJ(X_i,Y_i),
\quad\mathbf1=(1,1)^\top.
\]

One way to verify the cubic term is to set
\(S=\eta(h_1+h_2)\), \(p_a=\cos z_a(0)\), and use
\(\dot h_a=0\), \(\dot w=S\),
\(\ddot h_a=\eta S\odot p_a^2\), and
\(w^{(3)}=\eta\sum_b(G^2\mathbf1)_bh_b+
\eta\sum_b\ddot h_b\).
The third derivative of \(n^{-1}w^\top h_1\) has nonzero terms
\(n^{-1}w^{(3)\top}h_1+3n^{-1}\dot w^\top\ddot h_1\).
Their cubic per-neuron contribution, after dividing by \(\eta^3\), is

\[
4U^2(1-U^2)+7UV(1-U^2)+U^2(1-V^2)
+UV(1-V^2)+3V^2(1-U^2)=J(x,y).
\]

The full Gram is equivalent to the empirical average of

\[
t(x,y)=\big(\cos2x,\sin2x,\cos2y,\sin2y,
\cos(x+y),\sin(x+y),\cos(x-y),\sin(x-y)\big).
\]

Let the block size be \(b=9\). For a block define

\[
T_j=\sum_{i\in j}t(X_i,Y_i),\qquad
B_j=\sum_{i\in j}J(X_i,Y_i),\qquad
\kappa=\mathbb E\operatorname{Var}(B_j\mid T_j).
\]

The constant \(\kappa\) is strictly positive. Indeed, \(J\) has a
\(\cos4x\) coefficient \(-1/2\), a frequency absent from the Gram
functions, so \(1,t_1,\ldots,t_8,J\) are linearly independent.
The derivatives of the nine-component map \((t,J)\), over all points of
\(\mathbb R^2\), span \(\mathbb R^9\): otherwise a nontrivial linear
combination would have both derivatives identically zero, contradicting that
independence. Choosing nine independent derivative vectors makes the block
map to \((T_j,B_j)\) have rank nine at some configuration. The inverse
function theorem and positive Gaussian density give a component with positive
density in its nine-dimensional image. If \(\kappa=0\), \(B_j\) would
be a measurable function of \(T_j\); its graph has nine-dimensional measure
zero by Fubini's theorem. This contradicts the positive density component.

Sample each block summary \(T_j\) from its Gaussian law, and then draw two
independent blocks conditionally on that summary. Do this independently across
blocks. For the fewer than \(b\) leftover neurons, draw their Gaussian
coordinates once and share them between the pair. Write the two prediction
trajectories as \(f^A,f^B\), and their difference as
\(D_n(t)=f_1^A(t)-f_1^B(t)\). Each network separately has the original iid
Gaussian initialization. Their \(\Gamma_n\) agree exactly, and the full
paired blocks are independent of one another.

The cubic identity gives

\[
D_n(0)=\dot D_n(0)=\ddot D_n(0)=0,\qquad
\sqrt n\,D_n^{(3)}(0)
=\frac{\eta^3}{\sqrt n}\sum_j(B_j^A-B_j^B).
\]

The summands are iid bounded variables, have mean zero, and have variance
\(2\kappa\). The ordinary iid central limit theorem, whose finite-variance
hypothesis is satisfied, therefore yields

\[
\sqrt n\,D_n^{(3)}(0)\ \Longrightarrow\ N(0,\eta^6\sigma^2),
\qquad \sigma^2=\frac{2\kappa}{b}>0.
\]

In particular, with \(\Phi\) the standard Gaussian distribution function
and \(p_0=2[1-\Phi(1)]>0\),

\[
\mathbb P\left\{|D_n^{(3)}(0)|\ge
\frac{\eta^3\sigma}{\sqrt n}\right\}\longrightarrow p_0.
\]

## 3. Bounded neuron coordinates and average-distance stability

The Gaussian phases themselves are unbounded. Replace them by their actual
sines and cosines, without approximating the flow. For each neuron set

\[
u_{ai}=\sin z_{ai},\quad p_{ai}=\cos z_{ai},\qquad
\xi_i=(u_{1i},p_{1i},u_{2i},p_{2i},w_i)\in\mathbb R^5.
\]

Their closed equations are polynomial:

\[
\dot u_{ai}=c_aw_ip_{ai}^2,\qquad
\dot p_{ai}=-c_aw_iu_{ai}p_{ai},\qquad
\dot w_i=c_1u_{1i}+c_2u_{2i},\qquad
c_a=\eta-\frac1n\sum_iw_i u_{ai}.
\]

The circle constraint \(u_{ai}^2+p_{ai}^2=1\) is preserved. Also
\(\dot f=Kc\), where

\[
K_{ab}=\frac1n\sum_i u_{ai}u_{bi}
+\delta_{ab}\frac1n\sum_iw_i^2p_{ai}^2
\]

is positive semidefinite. Thus
\(\dot{\mathcal L}=-c^\top Kc\le0\),
\(\|c(t)\|_2\le\sqrt2\eta\), and
\(|\dot w_i|\le|c_1|+|c_2|\le2\eta\).
Set \(T_0=1/[2(\eta+1)]\). All real trajectories under consideration
remain in the box \([-1,1]^5\) for \(0\le t\le T_0\), including after
replacement of any initialization block.

For two such networks, match neuron indices and define the average distance

\[
d_n(t)=\frac1n\sum_i\|\xi_i(t)-\widetilde\xi_i(t)\|_\infty.
\]

Within the box, \(|f_a-\widetilde f_a|\le2d_n\), so the same bound holds
for residual differences. If the local coordinate distance is
\(\Delta_i\), the changes of the two activation velocities are each at most
\(2d_n+3(\eta+1)\Delta_i\), and the readout velocity change is at most
\(4d_n+2(\eta+1)\Delta_i\). This follows by subtracting the displayed
products, using \(|c_a|\le\eta+1\) on the box. Averaging the integral
equations therefore gives

\[
d_n(t)\le d_n(0)+(7+3\eta)\int_0^t d_n(s)\,ds,
\qquad
d_n(t)\le e^{Lt}d_n(0),\quad L=7+3\eta.
\]

The last inequality follows by integrating the scalar differential inequality
for the right-hand side. All constants are independent of width.

## 4. The fourth time derivative is a uniformly Lipschitz moment observable

We need a state-dependent formula for \(f_1^{(4)}\), with a Lipschitz
constant independent of width. It is unnecessary to expand its many terms.
Here is a finite algebraic construction that proves the required property.

For a polynomial \(P\) of the five coordinates \(\xi\), let
\(\langle P\rangle_n=n^{-1}\sum_iP(\xi_i)\). Define polynomial
derivations for each sample \(a=1,2\) by

\[
\mathcal A_aP
=wp_a^2\partial_{u_a}P
-wu_ap_a\partial_{p_a}P+u_a\partial_wP.
\]

The dynamics give exactly

\[
\frac{d}{dt}\langle P\rangle_n
=\sum_{a=1}^2
\big(\eta-\langle wu_a\rangle_n\big)
\langle\mathcal A_aP\rangle_n.
\]

Let \(\mathscr D\) act on a polynomial expression in finitely many moments
by the product rule and the displayed rule for each moment. Starting with
\(\langle wu_1\rangle_n\), apply this rule four times, and call the resulting
polynomial in moments \(\mathcal F_4\). Then

\[
f_1^{(4)}(t)=\mathcal F_4(\xi_1(t),\ldots,\xi_n(t)).
\]

The polynomial list and coefficients depend only on four differentiations and
the fixed \(\eta\), not on \(n\). This is an exact constructive expression,
not a derivative obtained from a stored trajectory.

Every participating polynomial \(P\) is bounded and Lipschitz on the fixed
box. More explicitly,

\[
|\langle P\rangle_n-\langle P\rangle_n^{\sim}|
\le\left(\sup_{\xi\in[-1,1]^5}\|\nabla P(\xi)\|_1\right)d_n.
\]

The finitely many moments range in fixed bounded intervals. The outer
polynomial defining \(\mathcal F_4\) has bounded partial derivatives on
their product. Applying the chain rule bound to those intervals gives a finite
constant \(L_4=L_4(\eta)\), independent of \(n\), such that

\[
|\mathcal F_4(\xi)-\mathcal F_4(\widetilde\xi)|\le L_4d_n.
\]

This also proves uniform boundedness and continuity of the fourth derivative
on the stated horizon. No bound on the initial Gaussian phases is needed.

## 5. A remainder bound at order \(n^{-1/2}\)

View \(D_n^{(4)}(s)\), for a fixed \(s\le T_0\), as a function of the
independent paired initialization blocks and the possible leftover block.
Replacing one of these independent blocks changes at most \(b\) neurons
in each marginal network. Each initial coordinate distance is at most \(2\),
so each marginal's initial average distance is at most \(2b/n\).
Sections 3 and 4 imply the bounded difference

\[
\left|D_n^{(4)}(s)-D_n^{(4)}(s)^{\rm replaced}\right|
\le\frac{4bL_4e^{LT_0}}{n}.
\]

For completeness, a function of independent coordinates with replacement
bounds \(\delta_j\) has variance at most \(\sum_j\delta_j^2\).
Expose the coordinates successively and use the conditional expectations as a
martingale. Its differences have mean zero and are mutually orthogonal in
\(L^2\). Each difference has magnitude at most \(\delta_j\), because
averaging over the still-unexposed coordinates preserves the replacement
bound. Summing their squared norms proves the variance assertion.

There are at most \(n/b+1\le2n/b\) independent blocks for \(n\ge b\).
The paired law is invariant under exchanging its two networks, while
\(D_n^{(4)}\) changes sign. Thus its mean is zero. The variance bound gives,
uniformly for \(0\le s\le T_0\),

\[
\|D_n^{(4)}(s)\|_{L^2}
\le\frac{C_4}{\sqrt n},\qquad
C_4=\sqrt{32b}\,L_4e^{LT_0}.
\]

Taylor's formula with its integral remainder is exact here:

\[
D_n(t)=\frac{t^3}{6}D_n^{(3)}(0)+\mathcal R_n(t),\qquad
\mathcal R_n(t)=\int_0^t\frac{(t-s)^3}{6}D_n^{(4)}(s)\,ds.
\]

The zero, first, and second derivatives vanished by the common initialization
Grams. The triangle inequality for the \(L^2\) norm of an integral, justified
also by boundedness and approximation by Riemann sums, gives

\[
\|\mathcal R_n(t)\|_{L^2}
\le\frac{C_4t^4}{24\sqrt n},\qquad 0\le t\le T_0.
\]

This is the step unavailable from a deterministic Taylor remainder alone:
the entire fourth-order remainder has the same width scale as the cubic
fluctuation and one extra power of the fixed time.

## 6. Choose a fixed time and transfer separation to any predictor

Choose, independently of width and predictor,

\[
t_*=\min\left\{T,\frac{T_0}{2},
\frac{\eta^3\sigma\sqrt{p_0}}{2(1+C_4)}\right\}>0.
\]

Chebyshev's inequality and the preceding remainder bound give

\[
\begin{aligned}
\mathbb P\left\{|\mathcal R_n(t_*)|>
\frac{\eta^3\sigma t_*^3}{12\sqrt n}\right\}
&\le\frac{C_4^2t_*^2}{4\eta^6\sigma^2}\\
&\le\frac{p_0}{16}.
\end{aligned}
\]

On the cubic event from Section 2, outside this remainder event, the pair
therefore satisfies

\[
|f_1^A(t_*)-f_1^B(t_*)|
\ge\frac{\eta^3\sigma t_*^3}{12\sqrt n}.
\]

Its probability has lower limit at least \(15p_0/16\). The pair has
identical \(\Gamma_n\), so it receives the same value \(F_n(\Gamma_n)\).
The triangle inequality implies that at least one of its two prediction
errors is at least half this separation. Both marginal errors have the law of
the original network's prediction error. A union bound therefore proves
the theorem, for example with

\[
a_\eta=\frac{\eta^3\sigma t_*^3}{24},\qquad
p=\frac{p_0}{4}>0,
\]

where the conservative probability constant is smaller than the proved
\(15p_0/32\). For an independently randomized predictor, share its same
independent seed across the coupled pair; the argument is unchanged.

## 7. Scope and check record

The result rules out Gram-only approximation negligible relative to dense
\(n^{-1/2}\) variability for the actual prediction at \(t_*\). It also rules
out such approximation in the supremum norm on every prescribed fixed
positive horizon. It does not rule out an error of order \(n^{-1/2}\),
population-law prediction, or additional initialization observables that retain
the missing fluctuation. No claim is made for arbitrary finite families, for
other activations or depths, or for all-time stability.

The proof does not require a kernel spectral gap or width-dependent labels.
For every fixed small \(\eta>0\), its constants and selected time are positive
and independent of width; they are not claimed uniform as \(\eta\downarrow0\).
All derivative observables and sensitivity estimates refer to the exact
nonlinear sine dynamics.

The author checked the independent-block construction, Gaussian marginal laws,
the cubic label factors, preservation of bounded neuron coordinates, the
average-distance inequality, the moment-generator construction of the fourth
derivative, the variance bound, and the Taylor and triangle-inequality
constants. This is a complete scoped candidate awaiting comparison or
independent checking, not promoted material.

Subsequent scoped internal verification in
CAUSAL_FINITE_AND_OBSTRUCTION_AUDIT.md reconstructed the full fixed-time proof
and found no proof-breaking gap. The present version incorporates its TeX
correction; the audit records the preceding frozen hash. This is still an
internal research result, not promoted material.
