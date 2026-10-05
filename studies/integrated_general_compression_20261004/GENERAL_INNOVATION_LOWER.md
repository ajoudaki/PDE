# A general innovation lower bound from the uncentered feature gap

2026-10-04. Scoped algebraic/probabilistic derivation. Complete scientific
inputs read: `EARLY_VARIABILITY_AND_STORAGE.md` and
`GENERAL_EXPLICIT_FITTING.md`. No other new agent's proof, outside study,
or experiment was used. The central inequality below is distribution-free;
the Gaussian activation structure supplies its common marginal moments.

For at least two samples, a positive uncentered feature covariance gap
already forces nonzero initialized innovation in every nonzero label
direction. No centered covariance gap, oddness, input orthogonality, or
nonsingular preactivation covariance is needed. The proof gives a
polynomial quantitative lower bound. The one-sample case has a separate
scalar obstruction described at the end.

## 1. Setup and quantitative conclusion

Let \(m\ge2\), let \(Z=(Z_1,\ldots,Z_m)\) be a centered Gaussian
vector with an arbitrary positive semidefinite covariance and common
marginal variance \(q>0\), and put
\[
 H_a=\phi(Z_a),\qquad Q=\mathbb E[HH^\top],\qquad
 \gamma=\lambda_{\min}(Q)>0.
\]
The matrix \(Q\) is uncentered. Assume \(\phi\) is continuous with
at most linear growth, so that its scalar moments
\[
 \mu_2=\mathbb E\phi(\sqrt qG)^2,\qquad
 \mu_4=\mathbb E\phi(\sqrt qG)^4,
 \quad G\sim N(0,1),
\]
are finite. In particular the integrated study's activation class satisfies
these assumptions. Let \(y\in\mathbb R^m\setminus\{0\}\), and define
\[
 S=y^\top H,\qquad Y=\|y\|_2/\sqrt m,
 \qquad V_a=\operatorname{Var}(H_aS),\qquad
 V_{\rm sum}=\sum_{a=1}^m V_a=\operatorname{tr}\operatorname{Cov}(HS).
\]
Then
\[
 V_{\rm sum}\ge
 \frac{(m-1)^2}{4m^2}\frac{\gamma^4}{\mu_4}\|y\|_2^2.
                                                               \tag{1}
\]
The common marginal second moment gives the stronger bound
\[
 V_{\rm sum}\ge
 \frac{(m-1)\gamma^3(m\mu_2-\gamma)}{4m^2\mu_4}\|y\|_2^2
 \ge\frac{(m-1)^2}{4m^2}
             \frac{\gamma^3\mu_2}{\mu_4}\|y\|_2^2.     \tag{2}
\]
Here \(0<\gamma\le\mu_2\), so (2) implies (1). Consequently at least
one deterministic sample index \(a\) satisfies
\[
 V_a\ge\frac{(m-1)^2}{4m^2}
           \frac{\gamma^3\mu_2}{\mu_4}Y^2
 \ge\frac{\gamma^3\mu_2}{16\mu_4}Y^2
 \ge\frac{\gamma^4}{16\mu_4}Y^2.                        \tag{3}
\]
The index can depend on the fixed covariance and labels; it need not be
chosen from the random finite-width realization.

For the bounded subclass \(|\phi|\le K\), \(K>0\), the proof also
gives
\[
 V_{\rm sum}\ge
 \frac{\gamma^2(m\mu_2-\gamma)}{mK^2}\|y\|_2^2,
 \qquad
 \max_a V_a\ge\frac{m-1}{m}\frac{\gamma^2\mu_2}{K^2}Y^2.
                                                               \tag{4}
\]
The boundedness assumption is used only for this additional bound;
(1)--(3) apply to unbounded affine and other unbounded admissible
activations as well.

## 2. The distribution-free geometric inequality

In this section \(H\) can be any random vector with finite fourth
moment and \(Q=\mathbb E HH^\top\succ0\). Identical marginals and
Gaussianity are not assumed. Put
\[
 c=Qy=\mathbb E[HS],\qquad A=\|c\|_2>0,\qquad
 T=\operatorname{tr}Q,\qquad
 D=T-\frac{c^\top Qc}{A^2},\qquad
 M_4=\mathbb E\|H\|_2^4.
\]
For \(m\ge2\), \(D>0\). Define the squared area of the two vectors
\(c,H\) by
\[
 J(H)=A^2\|H\|_2^2-(c^\top H)^2.
\]
Because \(HS\) is parallel to \(H\), subtracting it from \(c\)
does not change this area. Thus pointwise
\[
 J(H)=\|HS-c\|_2^2\|H\|_2^2
                  -[(HS-c)^\top H]^2
 \le\|HS-c\|_2^2\|H\|_2^2,
\]
\[
 0\le J(H)\le A^2\|H\|_2^2,
 \qquad \mathbb E J(H)=A^2D.                            \tag{5}
\]
For any \(R>0\), the tail contribution satisfies
\[
 \mathbb E[J(H)\mathbf1_{\{\|H\|_2^2>R^2\}}]
 \le A^2\mathbb E[\|H\|_2^2\mathbf1_{\{\|H\|_2^2>R^2\}}]
 \le\frac{A^2M_4}{R^2}.
\]
On the complementary event, the first inequality in (5) is at most
\(R^2\|HS-c\|_2^2\). Therefore
\[
 R^2 V_{\rm sum}\ge A^2\left(D-\frac{M_4}{R^2}\right).
\]
Choose \(R^2=2M_4/D\). This yields the exact moment bound
\[
 V_{\rm sum}\ge\frac{A^2D^2}{4M_4}
 =\frac{[y^\top Q^2(TI-Q)y]^2}
        {4M_4\|Qy\|_2^2}.                              \tag{6}
\]
All denominators are strictly positive. This inequality is valid without
any assumptions about connected support or an analytic parametrization.

If \(\|H\|_2^2\le R^2\) almost surely, truncation is unnecessary:
directly taking expectations in (5) gives
\[
 V_{\rm sum}\ge\frac{A^2D}{R^2}
              =\frac{y^\top Q^2(TI-Q)y}{R^2}.           \tag{7}
\]

For comparison, the qualitative rank obstruction can be seen directly.
If \(V_{\rm sum}=0\), then \(HS=c\) almost surely. Multiplication
by \(y^\top\) gives \(S^2=y^\top Qy>0\), so
\(H=c/S\) lies on one line almost surely. Its second-moment matrix
then has rank at most one. This contradicts \(Q\succ0\) when
\(m\ge2\). A sphere-valued random vector of full second-moment rank
does not evade this obstruction.

## 3. Explicit spectral and marginal-moment bounds

Return to common marginal moments. Cauchy--Schwarz gives
\[
 M_4=\sum_{a,b}\mathbb E[H_a^2H_b^2]\le m^2\mu_4,
 \qquad T=m\mu_2.
                                                               \tag{8}
\]
Since \(Q\succeq\gamma I\),
\[
 A\ge\gamma\|y\|_2,\qquad
 D\ge T-\lambda_{\max}(Q)\ge(m-1)\gamma.
\]
Substitution in (6) proves (1).

For (2), write \(N=y^\top Q^2(TI-Q)y=A^2D\). Every eigenvalue
\(\xi\) of \(Q\) belongs to
\([\gamma,T-(m-1)\gamma]\subset[\gamma,T-\gamma]\).
The polynomial \(\xi^2(T-\xi)\) increases and then decreases on
\([0,T]\), so its minimum on \([\gamma,T-\gamma]\) is at an
endpoint. The two values there are
\(\gamma^2(T-\gamma)\) and \(\gamma(T-\gamma)^2\).
Since \(T\ge2\gamma\), the former is the smaller. Consequently
\[
 N\ge(m-1)\gamma A^2,
 \qquad N\ge\gamma^2(T-\gamma)\|y\|_2^2.
\]
Multiplying the two lower bounds for the same positive number gives
\[
 \frac{N^2}{A^2}\ge
       (m-1)\gamma^3(T-\gamma)\|y\|_2^2.
\]
Equations (6), (8) prove the first inequality in (2). The second uses
\(T-\gamma=m\mu_2-\gamma\ge(m-1)\mu_2\), since
\(\gamma\le\mu_2\). Taking a maximum among the \(m\) diagonal
variances and using \(\|y\|_2^2=mY^2\) proves (3).

If \(|H_a|\le K\), then \(\|H\|_2^2\le mK^2\).
Use (7) and \(N\ge\gamma^2(T-\gamma)\|y\|_2^2\) to obtain
(4). No regularity or sign condition on the bounded activation enters
this argument.

## 4. Consequence for the general-depth initialized innovation

Use the canonical model of the two complete source notes: fixed hidden
depth \(L\ge2\), arbitrary unit normalized inputs \(v_a\), width \(n\),
Gaussian first weights of variance one, Gaussian hidden mixers of
variance \(1/n\), zero initial readout, mean squared loss, and mobilities
\((n,1,\ldots,1,n)\). Activations can vary with the layer and need not
be centered, odd, bounded, or normalized.

The deterministic marginal variance recursion is
\[
 q_0=1,\qquad q_\ell=\mathbb E\phi_\ell(\sqrt{q_{\ell-1}}G)^2.
\]
At the last initialization layer, set
\[
 Z\sim N(0,Q^{(L-1)}),\quad H_a=\phi_L(Z_a),\quad
 Q=Q^{(L)},\quad \mu_2=q_L,\quad
 \mu_4=\mathbb E\phi_L(\sqrt{q_{L-1}}G)^4.
\]
The equal input norms imply equal covariance diagonals at every layer;
these scalar moments depend only on the fixed activations and depth,
not on training correlations, sample count, labels, or width. They are
finite. For example, if \(b=|\phi_L(0)|\) and
\(s=\sup_{t\in\mathbb R}|\phi_L'(t)|\), then
\[
                    \mu_4\le8b^4+24s^4q_{L-1}^2.        \tag{9}
\]
For \(m\ge2\), the assumption \(Q\succ0\) itself excludes
\(q_{L-1}=0\): that case would make every \(H_a\) the same
deterministic constant and \(Q\) have rank at most one.

The final innovation from `EARLY_VARIABILITY_AND_STORAGE.md` is the
covariance of the symmetric matrix \(HH^\top\). For each fixed
training-query index \(a\), its contraction with the labels is exactly
\[
 \sum_{b,c}y_by_c B_{L,ab,ac}
 =\operatorname{Var}\left(H_a\sum_b y_bH_b\right)=V_a.  \tag{10}
\]
Its initialized fluctuation covariance satisfies
\(C_L=T_LC_{L-1}T_L^\top+B_L\succeq B_L\) as a covariance form.
The exact zero-readout onset formula for two independent dense copies
therefore gives, at the deterministic query selected in (3),
\[
 \sqrt n\,[\dot f_n(0,v_a)-\dot{\widetilde f}_n(0,v_a)]
 \ \Longrightarrow\ N(0,\sigma_a^2),
 \qquad \sigma_a^2\ge\frac8{m^2}V_a.
\]
In particular
\[
 \sigma_a^2\ge
 \frac{2(m-1)^2}{m^4}\frac{\gamma^3\mu_2}{\mu_4}Y^2
 \ge\frac{\gamma^3\mu_2}{2m^2\mu_4}Y^2
 \ge\frac{\gamma^4}{2m^2\mu_4}Y^2.                     \tag{11}
\]
For a bounded last activation \(|\phi_L|\le K\), the additional
bound is
\[
 \sigma_a^2\ge\frac{8(m-1)}{m^3}
                      \frac{\gamma^2\mu_2}{K^2}Y^2
 \ge\frac{4\gamma^2\mu_2}{m^2K^2}Y^2.                 \tag{12}
\]
The maximizing query for (12) can be chosen separately from the one for
(11); each is a deterministic training input. Thus arbitrary correlation
and arbitrary nonzero label orientation cannot annihilate every
training-query onset innovation when \(m\ge2\) and \(Q\succ0\).

These bounds concern the initialized derivative observable. They supply
the quantitative variance input for a separately proved analytic
derivative-to-trajectory inequality. By themselves they do not assert a
positive-time predictor bound or a fitted-endpoint lower bound. Indeed
the chosen queries are training inputs, where all fitted endpoints agree
exactly with the prescribed labels. The central limit theorem keeps
\(m,d,L\), activations, data, and nonzero labels fixed as \(n\to\infty\);
the explicit factors in (11)--(12) are not a growing-dimension CLT.

## 5. Exact exceptions and limitations of moment-only bounds

For \(m=1\), the rank obstruction disappears. The exact last-layer
innovation is
\[
             \operatorname{Var}(H_1S)=y_1^2(\mu_4-\mu_2^2).       \tag{13}
\]
If \(q>0\) and \(\phi\) is continuous, this is zero precisely when
\(\phi^2\) is constant on the real line: equality almost everywhere
under a Gaussian, continuity, and full Gaussian support give equality
everywhere. A continuous real function with constant nonzero square is
constant, because the real line is connected. The zero-square case is
also constant. Thus nonconstant continuous activations and positive
preactivation variance give a positive scalar innovation, but its
coefficient is the activation-specific quantity in (13). A constant last
activation with \(\mu_2>0\), or a deterministic zero-variance
preactivation followed by a nonzero constant value, permits a positive
uncentered gap and zero innovation. The original broad class allows
these exceptions, so no unconditional positive one-sample claim follows
from the gap alone.

The fourth-moment dependence cannot be omitted in a distribution-free
argument. For example, with \(m=2\), let \(H\) take the values
\(\pm a(1,1)\) with total probability \(1-p\), and
\(\pm b(1,-1)\) with total probability \(p\), assigning equal mass
to the two signs within each pair. Set
\[
 a^2=\frac\gamma{2(1-p)},\qquad b^2=\frac\gamma{2p},
 \qquad y=(1,1)/\sqrt2,\quad 0<p<1.
\]
Then both marginals have the same distribution,
\[
 Q=\gamma I_2,\qquad
 \mu_4=\frac{\gamma^2}{4p(1-p)},\qquad
 V_{\rm sum}=\frac{\gamma^2p}{1-p}.
\]
For small \(p\), the last quantity is comparable to
\(\gamma^4/\mu_4\), and can be arbitrarily small at fixed gap if
fourth moments are uncontrolled. This discrete example is not claimed
to be a fixed analytic Gaussian-coordinate activation model; it explains
why that further structure, or moment control, is necessary to improve
a distribution-free result. The positive bounds (1)--(4) apply directly
to the stated Gaussian activation model without approximating it by this
example.

All actual label factors remain visible. No small-label allowance has
been substituted for \(Y\), and no label cap is needed for the algebraic
innovation bounds themselves. When composing with the study's actual
training results, their existing label, fitting, source, and probability
hypotheses must still be imposed.
