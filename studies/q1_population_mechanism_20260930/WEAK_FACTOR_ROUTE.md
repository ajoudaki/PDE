# Weak-factor acquisition: exact startup coefficients and all-time geometry

Second bounded round. The first-round `LATENT_ORBIT_ROUTE.md` is preserved.
This note uses only the supplied model, the supervisor's selected weak-factor
geometry and feature-clock convention, and elementary calculations below.
Diagnostic quadrature values supplied by the supervisor were not used as proof.
No experiment, training simulation, external scientific retrieval, or finite-width
substitute was used. Exact reductions below are self-checked candidate results;
the sign certificate described at the end is a separate remaining input.

## Model, clock, and target

Take standard isotropic Gaussian initial weights \(A_0=(X,Y,Z)\), independent
standard normal coordinates, and the four normalized inputs

\[
 u_{\sigma\tau}=(c,\varepsilon\sigma,\varepsilon\tau),\qquad
 c=\sqrt{1-2\varepsilon^2},\qquad y_{\sigma\tau}=\sigma\tau,
 \quad 0<\varepsilon<1/\sqrt2.
\]

The physical-time equations remain exactly those supplied:
\(\dot W=-2\operatorname{mean}_a r_aG_a\),
\(\dot A=-2\operatorname{mean}_a r_aL_au_a\), and the other q1 equations
unchanged. Signed-input symmetry and the stipulated unique equivariant flow
give \(F_a=y_af\). Use **feature time**

\[
 s(t)=2\int_0^t(1-f(t'))\,dt'.
\]

It is an increasing local clock near initialization, since \(f(0)=0\).
Every prime and acceleration in this note means differentiation with respect
to \(s\). In this clock

\[
 W'=\operatorname{mean}_a y_aG_a,
 \qquad A'=\operatorname{mean}_a y_aL_au_a,
 \qquad V'_a=y_aD_a.
\]

Every observable considered below has zero initial first derivative; therefore
its physical-time second derivative is four times its feature-time second
derivative. The sign conclusions are clock invariant.

For \(\chi\in\{0,\sigma,\tau,y\}\), with character \(0\) meaning the constant
one, define

\[
 h_\chi(A)=\tfrac14\sum_a\chi(a)\tanh(A\cdot u_a),
 \qquad E_\chi(s)=\langle h_\chi(A_s)^2\rangle_1,
 \qquad v_\chi=E_\chi(0).
\]

The primitive factors \(\sigma,\tau\) are specified by the data construction;
they are not supervised targets, and
\(\operatorname{mean}y\sigma=\operatorname{mean}y\tau=0\).
Acquisition here means increasing their fixed linear-decoder energies, starting
from their small positive Gaussian-initialization energies. It does not mean
creating previously absent information. Opposite signs for primitive-factor and
context energies would exclude a common rescaling explanation.

The startup statement is for sufficiently small **fixed** \(\varepsilon>0\)
and then a positive time interval depending on that fixed value. The
\(\varepsilon\to0\) calculation supplies signs; it changes neither the exact
population model nor the order of the width limit.

## Exact conditional drift, including normalization

At initialization let
\(z_a=TH_a\), \(g_y=\tfrac14\sum_a y_a\tanh z_a\), and
\(J=\langle g_y^2\rangle_2\). Reflection symmetry makes the first-layer Walsh
coefficients orthogonal. The given canonical forward rule implies that the
Walsh coefficients \(\zeta_\chi\) of \(z\) are independent centered Gaussians
with variances \(v_\chi\). Thus

\[
 J(v)=\mathbb E\left[
 \tfrac14\sum_{\sigma,\tau}\sigma\tau
 \tanh(\zeta_0+\sigma\zeta_\sigma+\tau\zeta_\tau+
             \sigma\tau\zeta_y)\right]^2.
 \tag{1}
\]

Write \(J_\chi=\partial J/\partial v_\chi\), with one-sided derivatives at
zero variances. These derivatives exist by boundedness of all tanh derivatives
and Gaussian integration by parts.

At startup, \(A'=V'=K'=0\), \(W'=g_y\), and

\[
 A''=\operatorname{mean}_a y_a\phi'(A\cdot u_a)u_a
           T^*\!\left[g_y\phi'(z_a)\right],\qquad \phi=\tanh.
 \tag{2}
\]

Apply the supplied **canonical** first reverse-call rule to
\(U_a(z)=g_y(z)\phi'(z_a)\):

\[
 T^*U_a=\sum_bM_{ab}H_b+\xi_a,
 \qquad M_{ab}=\mathbb E\partial_bU_a,
\]

where \(\xi\) is centered and independent of \(A_0\), with the full supplied
covariance. No regression covariance is subtracted. Set

\[
 C_{ab}=\frac{y_a}{4}M_{ab}
 =\frac{y_ay_b}{16}\mathbb E[\phi'(z_a)\phi'(z_b)]
   +\mathbf1_{a=b}\frac{y_a}{4}\mathbb E[g_y\phi''(z_a)].
\]

This symmetric matrix equals one half the expected Hessian of \(g_y^2\).
For completeness, if a covariance matrix \(Q\) is perturbed by \(\delta Q\),
differentiating a Gaussian integral and integrating by parts gives
\(\delta J=\frac12\sum_{ab}\mathbb E[\partial_{ab}(g_y^2)]\delta Q_{ab}\).
It can first be proved for positive definite \(Q\) by differentiating its
Gaussian density twice; bounded derivatives then allow limits to semidefinite
\(Q\). Consequently \(\delta J=\sum_{ab}C_{ab}\delta Q_{ab}\).

Since \(Q_{ab}=\sum_\chi\chi(a)\chi(b)v_\chi\), this covariance variation
and the chain rule for \(H_a(A)\) give

\[
 \mathbb E[A''\mid A_0=A]
 =\sum_{ab}C_{ab}\phi'(A\cdot u_a)u_aH_b(A)
 =\frac12\sum_\chi J_\chi\nabla_A h_\chi(A)^2.
 \tag{3}
\]

The last equality can also be checked by varying the population distribution:
the derivative of \(Q_{ab}=\mathbb E H_aH_b\) under a root-dependent particle
perturbation has two equal symmetric terms, whereas (2) has one. The independent
transpose innovation disappears only after conditional expectation in (3).

Because \(A'(0)=0\), the exact first-layer energy acceleration is

\[
 E_\eta''(0)=\frac12\sum_\chi J_\chi
 \mathbb E\left[\nabla h_\eta^2\cdot\nabla h_\chi^2\right].
 \tag{4}
\]

This is a source-dependent q1 calculation reduced by its actual canonical
reverse law; it is not an ordinary independent random-features transpose.

## The weak-factor expansion

Write
\(p=\phi'(X)\), \(q=\phi''(X)\), \(r=\phi'''(X)\).
Taylor expansion of the four input values gives

\[
 h_0=\phi(X)+O(\varepsilon^2),\quad
 h_\sigma=\varepsilon Yp+O(\varepsilon^3),\quad
 h_\tau=\varepsilon Zp+O(\varepsilon^3),\quad
 h_y=\varepsilon^2YZq+O(\varepsilon^4).
 \tag{5}
\]

These remainder statements also hold after any fixed finite number of
\(A\)-derivatives in every finite Gaussian \(L^k\) norm. To see this directly,
apply Taylor's formula with remainder to each affine logit. Every derivative of
tanh is bounded; the remainders are bounded by a constant times powers of
\(\varepsilon(|X|+|Y|+|Z|)\), whose Gaussian moments are finite. The Walsh
sums cancel the lower terms of the wrong parity. The replacement of \(cX\)
by \(X\) affects the shown terms only at two higher powers of \(\varepsilon\).

Set

\[
 v=\mathbb E\phi(X)^2,\quad a_1=\mathbb Ep^2,\quad a_2=\mathbb Eq^2,
 \quad B_1(v)=\mathbb E\phi'(\sqrt vN)^2,\quad
 B_2(v)=\mathbb E\phi''(\sqrt vN)^2.
\]

Here \(N\) is a separate standard normal. From (5),

\[
 v_0=v+O(\varepsilon^2),\quad
 v_\sigma=v_\tau=\varepsilon^2a_1+O(\varepsilon^4),\quad
 v_y=\varepsilon^4a_2+O(\varepsilon^6).
\]

Expanding (1) in its three small Gaussian fields yields

\[
 J=B_1v_y+B_2v_\sigma v_\tau+O(\varepsilon^6),
\]

and, with
\(C=B_1'(v)a_2+B_2'(v)a_1^2\),

\[
 J_y=B_1+O(\varepsilon^2),\quad
 J_\sigma=J_\tau=\varepsilon^2B_2a_1+O(\varepsilon^4),\quad
 J_0=\varepsilon^4C+O(\varepsilon^6).
 \tag{6}
\]

One explicit way to verify the coefficients is to condition on \(\zeta_0\):
the label Walsh coefficient is
\(\phi'(\zeta_0)\zeta_y+\phi''(\zeta_0)\zeta_\sigma\zeta_\tau\)
to the required order. The cross term has expectation zero. The same expansion
after the heat-derivative identity proves the derivative remainders in (6);
bounded higher derivatives control the Gaussian Taylor remainders uniformly
for variances in a fixed compact neighborhood. In particular no derivative
of an uncontrolled asymptotic remainder is being assumed.

The leading Gram entries needed in (4) are

\[
\begin{aligned}
 \varepsilon^{-2}\mathbb E[\nabla h_\sigma^2\cdot\nabla h_0^2]
  &\to4\mathbb E[\phi p^2q],\\
 \varepsilon^{-4}\mathbb E\|\nabla h_\sigma^2\|^2
  &\to12\mathbb E[p^2q^2]+4\mathbb Ep^4,\\
 \varepsilon^{-4}\mathbb E[\nabla h_\sigma^2\cdot\nabla h_\tau^2]
  &\to4\mathbb E[p^2q^2],\\
 \varepsilon^{-6}\mathbb E[\nabla h_\sigma^2\cdot\nabla h_y^2]
  &\to12\mathbb E[pq^2r]+4\mathbb E[p^2q^2],\\
 \mathbb E\|\nabla h_0^2\|^2&\to4\mathbb E[\phi^2p^2],\\
 \varepsilon^{-4}\mathbb E[\nabla h_0^2\cdot\nabla h_y^2]
  &\to4\mathbb E[\phi pqr],\\
 \varepsilon^{-8}\mathbb E\|\nabla h_y^2\|^2
  &\to36\mathbb E[q^2r^2]+24\mathbb Eq^4.
\end{aligned}
 \tag{7}
\]

For example,
\(\nabla h_\sigma^2=2\varepsilon^2(Y^2pq,Yp^2,0)+O(\varepsilon^4)\)
and
\(\nabla h_y^2=2\varepsilon^4(Y^2Z^2qr,YZ^2q^2,Y^2Zq^2)
+O(\varepsilon^6)\). Their inner product has Gaussian multipliers
\(\mathbb EY^4Z^2=3\) and \(\mathbb EY^2Z^2=1\), giving the fourth line.
The other entries follow from the displayed gradients and
\(\nabla h_0^2=(2\phi p,0,0)+O(\varepsilon^2)\).

## Reduction to one-dimensional Gaussian moments

Define the exact one-dimensional integrals

\[
 I_n=\frac1{\sqrt{2\pi}}\int_{\mathbb R}
       e^{-x^2/2}\operatorname{sech}^{2n}x\,dx,
 \qquad
 J_n=\frac1{\sqrt{2\pi}}\int_{\mathbb R}
       e^{-z^2/2}\operatorname{sech}^{2n}(\sqrt v z)\,dz.
\]

Thus

\[
\begin{gathered}
 v=1-I_1,\quad a_1=I_2,\quad a_2=4(I_2-I_3),\\
 B_1=J_2,\quad B_2=4(J_2-J_3),\\
 C=(8J_2-10J_3)a_2+(32J_2-112J_3+84J_4)a_1^2.
\end{gathered}
\]

Indeed \(\frac{d}{dv}J_n=2n^2J_n-n(2n+1)J_{n+1}\), by differentiating
the Gaussian variance and integrating by parts. Define

\[
 P=13I_4-31I_5+18I_6,\quad
 R=2I_3-5I_4+3I_5,\quad
 U=14I_4-52I_5+65I_6-27I_7.
\]

The exact leading coefficient brackets are

\[
\begin{aligned}
 F_\sigma={}&16B_1P+4B_2a_1(17I_4-16I_5)-8C(I_3-I_4),\\
 F_0={}&-16B_1R-16B_2a_1(I_3-I_4)+4C(I_2-I_3),\\
 F_y={}&192B_1U+32B_2a_1P-16CR.
\end{aligned}
 \tag{8}
\]

Equations (4)–(7) prove, in the feature clock,

\[
\begin{aligned}
 E_\sigma''(0)=E_\tau''(0)&=\tfrac12F_\sigma\varepsilon^6
                                      +O(\varepsilon^8),\\
 E_0''(0)&=\tfrac12F_0\varepsilon^4+O(\varepsilon^6),\\
 E_y''(0)&=\tfrac12F_y\varepsilon^8+O(\varepsilon^{10}).
\end{aligned}
 \tag{9}
\]

The reduction uses \(q=-2\phi p\), \(r=4p-6p^2\), and \(\phi^2=1-p\).
For explicit algebra checks,

\[
\begin{aligned}
 12\mathbb E[pq^2r]+4\mathbb E[p^2q^2]&=16P,\\
 16\mathbb E[p^2q^2]+4\mathbb Ep^4&=4(17I_4-16I_5),\\
 4\mathbb E[\phi p^2q]&=-8(I_3-I_4),\\
 4\mathbb E[\phi pqr]&=-16R,\\
 36\mathbb E[q^2r^2]+24\mathbb Eq^4&=192U.
\end{aligned}
\]

Two hierarchy observables have coefficients

\[
 \left(\frac{E_\sigma}{E_0}\right)''(0)
 =\frac{vF_\sigma-a_1F_0}{2v^2}\varepsilon^6+O(\varepsilon^8),
 \tag{10}
\]

\[
 \left(\frac{E_y}{E_\sigma}\right)''(0)
 =\frac{a_1F_y-a_2F_\sigma}{2a_1^2}\varepsilon^6+O(\varepsilon^8).
 \tag{11}
\]

If \(F_\sigma>0\), \(F_0<0\), and \(F_y>0\) are certified, (9) implies
that for all sufficiently small fixed \(\varepsilon>0\), actual population
training initially amplifies both unsupervised primitive factors and the XOR
channel while suppressing the common context. Continuous second derivatives
then give strict change on a positive feature-time interval. This is a
positive-horizon consequence of signed, nonzero accelerations, not a claim
that an infinite Taylor series converges. Equation (10) is then automatically
positive; the stronger label-versus-factor acceleration needs the additional
sign in (11).

## Stronger all-time architecture inequality, without tetrahedral symmetry

For any real \(x,a,b\) and any monotone activation \(\phi\), form the four
features \(H_{\sigma\tau}=\phi(x+\sigma a+\tau b)\). Their Walsh coefficients
satisfy

\[
 |h_y|\le\min(|h_\sigma|,|h_\tau|).
 \tag{12}
\]

To prove the first inequality, set
\(\Delta_\pm=\phi(x+a\pm b)-\phi(x-a\pm b)\).
Both differences have the same sign, so

\[
 h_\sigma=(\Delta_++\Delta_-)/4,\qquad
 h_y=(\Delta_+-\Delta_-)/4,
\]

and \(|\Delta_+-\Delta_-|\le|\Delta_++\Delta_-|\).
Interchanging \(a,b\) proves the other inequality. For tanh at finite logits,
the first inequality is strict whenever \(a\ne0\), and the second is strict
whenever \(b\ne0\); strict monotonicity makes both corresponding differences
nonzero. If a coefficient vanishes, the same formulas cover the equality case.

Therefore (12) holds pointwise for **every** first-layer state of the weak-factor
XOR model, without isotropy, population symmetry, an initialization hypothesis,
or a dynamical approximation. Integrating gives
\(E_y\le\min(E_\sigma,E_\tau)\) at every existing time. The signed-input
orbit symmetries of the actual equivariant population flow also make the four
Walsh coefficients mutually orthogonal and give \(E_\sigma=E_\tau\).
Explicitly, the signed inputs are
\(p_{\sigma\tau}=(c\sigma\tau,\varepsilon\tau,\varepsilon\sigma)\).
The translation \((\sigma,\tau)\mapsto(\alpha\sigma,\beta\tau)\) is
implemented by the orthogonal matrix
\(\operatorname{diag}(\alpha\beta,\beta,\alpha)\). The invariant signed
feature covariance therefore depends only on the group difference of its two
sample indices; its Walsh characters are orthogonal. Undoing the signed gauge
permutes the four characters and preserves this orthogonality. Exchanging the
last two physical coordinates exchanges the two primitive factors.
Consequently the exact minimum-norm population linear decoders have squared
norm \(1/E_\chi\), whenever the corresponding energy is nonzero: the
decoder \(h_\chi/E_\chi\) attains this norm, while Cauchy's inequality proves
minimality. Thus (12) is an operational accessibility order, not only an
inequality between convenient coefficients.

This general monotonicity proof strictly strengthens the special first-round
tetrahedral spectral bound. It does **not** itself show acquisition. The
actual acquisition claim requires (9) and a strict sign certificate for (8).

## Check status and exact remaining sign obligation

Proved reductions: the canonical conditional drift (3), exact energy identity
(4), controlled weak-factor expansions (9)–(11), and all-time architecture
inequality (12). Self-checks: feature/physical clock factor; direct reverse-rule
substitution; Gaussian moment factors in every Gram entry; reduction of those
entries to sech moments; all equality/zero cases in the monotonicity argument.

Remaining to close the stated acquisition theorem: a rigorous enclosure of
the explicit one-dimensional integrals in (8) proving
\(F_\sigma>0\), \(F_0<0\), \(F_y>0\), and optionally
\(a_1F_y-a_2F_\sigma>0\). The supervisor's approximate positive coefficient
for the factor acceleration is diagnostic evidence only. A certified quadrature
enclosure or an analytic inequality with explicit bounds closes this finite
sign obligation; no population-training simulation is required.

The theorem remains conditional on existence of a regular population trajectory
with the assumed equivariance and differentiability. No global existence,
global fitting, monotonic all-time acquisition, or second-layer factor acquisition
is claimed.
