# Part A. Uniform activation classes and examples

The theorem above is an existence result for an entire class of
nonlinear activations, with an explicit selection from \(\delta\)
and the chosen function. This part records uniform subclasses and
explains exactly which constants can be shared. All assertions
refer to the model and observables of Part M, with three inputs and
three hidden layers and with the original raw training metric.

## A.1. A common parameter recipe for a whole class of functions

Fix \(r\ge1\) and \(j>0\). Consider the class of all normalized
functions satisfying (M.1a) and
\[
 \inf_{\alpha,\beta}\int_{-r}^{r}
                   [\psi(x)-\alpha-\beta x]^2\,dx\ge j.
                                                               \tag{A.1}
\]
It is enough that this class be nonempty. Choose
\(c=e^{-r^2/2}j/\sqrt{2\pi}\), and use (M.21) with \(c_\psi\)
replaced by \(c\). The same \(a_{\delta,r,j}\) and
\(e_{\delta,r,j}>0\) work for every function in (A.1), every fixed
amplitude \(0<e\le e_{\delta,r,j}\), and every admissible dataset.
The margin in (M.19) is then at least \(e^2c/(20a_{\delta,r,j}^2)\),
uniform over the function class as well as data and time.

Indeed the density argument (G.7) needs only the lower bound
\(J_r\ge j\); all the remaining function-dependent estimates in
the proof use only (M.1a). The scalar constant chain in Part R uses
no further information about \(\psi\). Its threshold is therefore
uniform over this class. The convergence assertions retain their
meaning for each fixed function and fixed admissible dataset;
no supremum over an infinite class inside the finite-width
probability statement is asserted.

This gives genuinely infinite-dimensional neighborhoods of
admissible shapes. To verify this directly, choose a nonconstant
\(\psi_0\) with \(\max_{k=0,1,2}\|\psi_0^{(k)}\|_\infty<1\), and
an interval with \(J_r(\psi_0)>0\). Distance to a fixed subspace is
1-Lipschitz, so
\[
 \sqrt{J_r(\psi_0+u)}\ge\sqrt{J_r(\psi_0)}
                                -\sqrt{2r}\|u\|_\infty.
                                                               \tag{A.2}
\]
For every sufficiently small \(C_b^2\) perturbation \(u\), all three
norm bounds in (M.1a) hold and \(J_r(\psi_0+u)\ge J_r(\psi_0)/4\).
Here \(C_b^2\) has norm \(\max_{k=0,1,2}\|u^{(k)}\|_\infty\).
Small independent smooth compactly supported perturbations on
arbitrarily many disjoint intervals show that this neighborhood
has infinitely many independent functional directions.

## A.2. A separation-independent positive nonaffinity coefficient

A stronger uniform margin is available when a class of normalized
functions satisfies, for some fixed \(\eta_0>0\),
\[
 \inf_{\psi\text{ in the class}}\inf_{\sigma\ge1}
                \mathcal R_\psi(\sigma G)\ge\eta_0.         \tag{A.3}
\]
Set \(t_0=\min\{1/2,\sqrt{\eta_0}/6\}\),
\(\lambda=\delta^2/256\), and select instead
\[
 \begin{split}
 a_\delta&=\max\{2,2000/\sqrt\lambda,
                         (10^{12}/(\lambda^2t_0))^{1/4}\},\\
 S&=12/(\lambda a_\delta^6),\qquad
 e_\delta=\tfrac12\min\{1,e_*(a_\delta,12,S),
                                      (10^{10}a_\delta)^{-1}\}.
 \end{split}                                                \tag{A.4}
\]
Every conclusion of Theorem M.1 then holds for every fixed
function in this class, with the stronger margin
\[
 \inf_{t\ge0}\inf_{\alpha,\beta}
 E_\ell[\phi(z_i^\ell(t))-\alpha-\beta z_i^\ell(t)]^2
                         \ge e^2\eta_0/4.                  \tag{A.5}
\]
In particular its coefficient is independent of separation.
For the proof, (G.5a) gives initialized standard deviation at least
one, so (A.3) supplies the initial margin \(\eta_0\). The stability
argument (G.8) applies with radius \(t_0\). The quartic selection
in (A.4) makes
\(615a_\delta^2D_S\le0.08856t_0\); all other controlled, response,
and cap-transfer bounds use exactly the same inequalities as in
Parts G, R and V. Part N needs only the amplitude bound already
present in (A.4). This proves the claim without the interval
constant from (M.20a).

Here are two direct ways of verifying (A.3), requiring no
external kernel-positivity or approximation theorem.

First, let a normalized nonconstant \(\psi\) have finite distinct
limits \(\ell_-\) and \(\ell_+\) at negative and positive infinity.
For each positive \(\sigma\), its Gaussian regression residual is
positive: a zero residual, together with continuity and full
Gaussian support, would make \(\psi\) affine everywhere and hence
constant. Its residual is continuous in \(\sigma>0\) by bounded
convergence, with \(|G|\) as the additional integrable dominator
for the covariance term. Put \(m=(\ell_++\ell_-)/2\) and
\(b=(\ell_+-\ell_-)/2\). Bounded convergence gives
\(\psi(\sigma G)\to m+b\operatorname{sgn}(G)\) in \(L^2\).
Projection onto \(\operatorname{span}\{1,G\}\) therefore yields
\[
 \mathcal R_\psi(\sigma G)\longrightarrow
       b^2(1-(E|G|)^2)=b^2(1-2/\pi)>0.                    \tag{A.6}
\]
For completeness \(E|G|=2(2\pi)^{-1/2}
\int_0^\infty x e^{-x^2/2}\,dx=\sqrt{2/\pi}\).
Continuity on compact scale intervals and the strictly positive
limit prove \(\inf_{\sigma\ge1}\mathcal R_\psi(\sigma G)>0\).
Thus (A.3) holds for each such function, and for any class with a
common verified lower bound.

Second, a whole infinite-dimensional neighborhood can share a
single absolute \(\eta_0\), even when its members have no limits
at infinity. Let
\(\psi_0(z)=\tfrac14\arctan z\). Its first two derivatives are
\(1/[4(1+z^2)]\) and \(-z/[2(1+z^2)^2]\), respectively, so
\(\max_{k=0,1,2}\|\psi_0^{(k)}\|_\infty<1\).
The first construction gives
\(\eta_b=\inf_{\sigma\ge1}\mathcal R_{\psi_0}(\sigma G)>0\).
For \(\psi=\psi_0+u\), distance to the affine subspace gives
\[
 \sqrt{\mathcal R_\psi(\sigma G)}
   \ge\sqrt{\mathcal R_{\psi_0}(\sigma G)}-\|u\|_\infty.
                                                               \tag{A.7}
\]
Choose a positive \(C_b^2\) radius small enough that
\(\|u\|_\infty\le\sqrt{\eta_b}/2\) and (M.1a) holds throughout
the ball. Then (A.3) holds with \(\eta_0=\eta_b/4\), independently
of \(\delta\) and \(u\). For example a sufficiently small sine
perturbation has oscillating tails and can make \(\psi\)
nonmonotone; a cosine perturbation breaks oddness. All such
perturbations retain (A.5). The full activation \(\phi\) remains
strictly increasing because its affine slope dominates the
bounded perturbation derivative.

## A.3. Concrete function choices and precise scope

Any of
\[
 u(z)=\arctan z,\quad \tanh z,\quad \sin z,\quad \cos z,
                       \quad e^{-z^2}
                                                               \tag{A.8}
\]
is nonconstant, bounded and twice continuously differentiable
with bounded first and second derivatives. Divide \(u\) by
\(M_u=\max\{1,\|u\|_\infty,\|u'\|_\infty,\|u''\|_\infty\}\)
to obtain \(\psi\). Applying Theorem M.1 gives activations
\(\phi(z)=a_{\delta,\psi}(1+z)+e\psi(z)\), or equivalently
\(a_{\delta,\psi}(1+z)+\varepsilon u(z)\) for
\(0<\varepsilon\le e_{\delta,\psi}/M_u\).
The derivative bounds for sine and cosine are immediate from
their derivatives; those for \(e^{-z^2}\) follow from
\(u'=-2ze^{-z^2}\), \(u''=(4z^2-2)e^{-z^2}\), whose polynomial
factors are dominated at infinity by the exponential. For
\(\tanh\), \(u'=1-u^2\) and \(u''=-2u(1-u^2)\) are bounded.
The arctangent derivatives were displayed above up to their
constant scale. These checks establish every membership claim
in (A.8).

The theorem also covers nonzero compactly supported \(C^2\)
functions after normalization. Such a \(\psi\) need not satisfy
(A.3): bounded convergence gives
\(E\psi(\sigma G)^2\to0\), so
\(0\le\mathcal R_\psi(\sigma G)\le E\psi(\sigma G)^2\to0\).
This is why the more general theorem uses the finite-variance
range and the interval estimate (G.7).

The claims are for the displayed affine-plus-perturbation
activations, with their allowed separation-dependent gain and
small fixed positive perturbation amplitude. They do not assert
the same raw-gradient theorem for the bounded functions in
(A.8) used alone, or for every activation with arbitrary
nonlinearity size. Pairwise separation does not itself imply
linear independence of three inputs, and none is assumed here.
All specialized proof ingredients used in this manuscript are
proved in Parts F, R, G, V and N; Part A uses only the elementary
regression arguments supplied above.
