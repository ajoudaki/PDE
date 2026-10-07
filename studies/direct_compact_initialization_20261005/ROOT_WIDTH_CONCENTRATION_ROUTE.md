# Strict root-width concentration: tanh coordinates remove the exponential loss

Status: author work, 2026-10-06. The strict
\(C_{\mathrm{data},\delta}/\sqrt n\) full-time, full-sphere comparison
is not proved or disproved here. A new deterministic change of variables
does remove the carrier maximum from the stability exponent for the
specified two-layer tanh model with orthogonal data. Combined with the
authorized source event, it gives a polynomial-logarithmic root-width
bound, improving the previous \(e^{C\sqrt{\log n}}\) amplification.
The last joint stochastic sensitivity bound remains explicit below.

The complete authorized `GENERAL_DENSE_COMPARISON.md`,
`DENSE_SAMPLE_EXPONENT_REFINEMENT.md`, and `README.md` from
`integrated_general_compression_20261004` were read. The complete relevant
correction, section 12 of that study's `UNBOUNDED_COMPRESSOR_BRIDGE.md`,
was also read for its all-time counting fourth-moment conclusion. Its
source theorem and physical fitting theorem are inherited inputs, not
reproved probability theorems here. No other study was read. The shared
instructions were reread; previously read mathematical skills apply, with
the already disclosed canonical-notation permission failure and authorized
fallback. No experiments, Git operations, or dense realizations were used.

## 1. Model and exact tanh coordinates

Let \(v_a=x_a/\sqrt d\), \(a=1,\ldots,m\), be orthonormal vectors.
The network and its training values are

\[
 u_a=Av_a,\quad h_a=\phi(u_a),\quad z_a=Wh_a,\quad
 g_a=\phi(z_a),\quad f_a=w^Tg_a/n,\qquad \phi=\tanh.
\]

Write \(r_a=f_a-y_a\),
\(\rho=\|r\|_2/\sqrt m\), and
\(Y=\|y\|_2/\sqrt m\). Labels are fixed, signed, and nonzero, with
the existing sufficiently small fixed-label condition; they do not
shrink with width. The squared mean loss has mobilities \((n,1,n)\),
and initially \(A_{ij}\sim\mathcal N(0,1)\),
\(W_{ij}\sim\mathcal N(0,1/n)\), independently, with \(w=0\).
Set

\[
 d_a=w\odot\phi'(z_a),\qquad k_a=W^Td_a.
\]

Orthogonality of the training inputs gives the exact equations

\[
 \dot u_a=-\frac2m r_a\phi'(u_a)\odot k_a,\quad
 \dot W=-\frac2{mn}\sum_a r_a d_ah_a^T,\quad
 \dot w=-\frac2m\sum_a r_ag_a.
 \tag{1}
\]

The first weights on the orthogonal complement of the training span are
constant. Define the strictly increasing scalar function

\[
 Q(u)=\frac u2+\frac{\sinh(2u)}4,
 \qquad Q'(u)=\frac1{\phi'(u)}=\cosh^2u.
\]

It maps the real line onto itself. Introduce coordinatewise increments

\[
 \eta_a(t)=Q(u_a(t))-Q(u_a(0)),\qquad
 T(u_0,\eta)=Q^{-1}(Q(u_0)+\eta).
\]

Equation (1) becomes

\[
 \dot\eta_a=-\frac2m r_ak_a,\qquad \eta_a(0)=0.
 \tag{2}
\]

This is an exact reparametrization of the same physical-time flow. It
does not freeze features or change the optimizer. Crucially, the diagonal
term involving \(\phi''(u_a)k_a\) has disappeared from the state
linearization in \(\eta\).

Here are uniform scalar bounds that will also control the initial source.
Let \(p(u)=\phi'(u)\). The chain rule gives

\[
 \partial_\eta T=p(T),\quad
 \partial_{u_0}T=\frac{p(T)}{p(u_0)},\quad
 \partial_\eta\phi(T)=p(T)^2\le1.
 \tag{3}
\]

The apparently dangerous gate ratio is only linear in the increment:

\[
 \frac{p(T)}{p(u_0)}\le1+2|\eta|.
 \tag{4}
\]

Indeed, for \(L(q)=1/p(Q^{-1}(q))\),
\(L'(q)=2\tanh(Q^{-1}(q))\), so \(|L'|\le2\).
Thus \(L(Q(u_0))\le L(Q(u_0)+\eta)+2|\eta|\); divide by
\(L(Q(u_0)+\eta)\ge1\). This proves (4), including arbitrarily
saturated initial coordinates.

Consequently \(T\) and \(\phi(T)\) are one-Lipschitz in \(\eta\)
and \((1+2|\eta|)\)-Lipschitz in \(u_0\). The squared gate
\(p(T)^2\) has derivative at most four in \(\eta\), and at most
\(4(1+2|\eta|)\) in \(u_0\). These follow from (3), (4),
\(|p|\le1\), and \(|\phi''|\le2\).

## 2. A deterministic all-time comparison without a carrier in the exponent

Consider two actual trajectories for the same data. Assume both satisfy,
for constants independent of width and time,

\[
 \begin{gathered}
 \|W(t)\|_{\rm op}\le M,\qquad
 \|w(t)\|_\infty\le C_wY,\qquad
 \left(\frac1n\sum_i|k_{a,i}(t)|^4\right)^{1/4}\le C_4Y,\\
 K(t)/m\succeq\kappa I,\qquad
 \rho(t)\le Ye^{-2\kappa t},\qquad
 \max_{a,i,t}|\eta_{a,i}(t)|\le H.
 \end{gathered}
 \tag{5}
\]

Here \(K\) is the actual tangent Gram in the residual equation
\(\dot r=-2Kr/m\). We may take \(M\ge1\), \(Y\le1\).
Constants denoted \(C\) below depend only on
\(m,M,C_w,C_4,\kappa\), not on \(n,H,t\). In particular \(H\)
will enter an initial-source factor, not a Gronwall exponent.

For two quantities use \(\Delta\) to denote their difference. Define

\[
 E_A=(1+2H)\frac{\|\Delta A(0)\|_F}{\sqrt n},\quad
 D(t)=\frac{\|\Delta\eta(t)\|_F}{\sqrt n}
                           +\|\Delta W(t)\|_F,\quad
 D_w(t)=\frac{\|\Delta w(t)\|_2}{\sqrt n}.
\]

Splitting
\(T(u_0,\eta)-T(u_0',\eta')\) by first keeping \(\eta\) fixed,
then keeping \(u_0'\) fixed, uses only an actual endpoint's bound
\(|\eta|\le H\). The estimates (3)--(4) then imply, for each
training sample,

\[
 \frac{\|\Delta u_a\|_2+\|\Delta h_a\|_2}{\sqrt n}
 +\frac{\|\Delta(p(u_a)^2)\|_2}{\sqrt n}
 \le C(E_A+D).
 \tag{6}
\]

No trajectory corresponding to interpolated initial roots is assumed.
Forward and backward subtraction, using bounded tanh derivatives and the
readout infinity bound in (5), gives

\[
 \begin{aligned}
 \|\Delta z_a\|_2/\sqrt n+\|\Delta g_a\|_2/\sqrt n
 &\le C(E_A+D),\\
 \|\Delta d_a\|_2/\sqrt n+\|\Delta k_a\|_2/\sqrt n
 &\le C[D_w+Y(E_A+D)].
 \end{aligned}
 \tag{7}
\]

For example,
\(\Delta d_a=\Delta w\odot\phi'(z_a)
+w'\odot[\phi'(z_a)-\phi'(z_a')]\), and
\(\Delta k_a=\Delta W^Td_a+W'^T\Delta d_a\).
Only \(\|w'\|_\infty\), a width-independent consequence of bounded
top features and integrated residual, is used. No first-layer carrier
maximum occurs in (7).

The tangent Gram has the particularly useful orthogonal-data form

\[
 K_{ab}=
 \frac{g_a^Tg_b}{n}
 +\frac{d_a^Td_b}{n}\frac{h_a^Th_b}{n}
 +\delta_{ab}\frac1n\sum_i p(u_{a,i})^2k_{a,i}^2.
 \tag{8}
\]

The last term is the only one needing a higher counting moment. Its
difference is bounded using (6), (7), and

\[
 \frac1n\sum_i|\Delta(p_i^2)|\,k_i^2
 \le\left(\frac1n\sum_i|\Delta(p_i^2)|^2\right)^{1/2}
      \left(\frac1n\sum_i k_i^4\right)^{1/2}.
\]

The remaining difference in \(k_i^2\) is bounded by the two RMS
carrier norms times the RMS carrier difference. Consequently

\[
 \|\Delta K/m\|_{\rm op}
 \le C[E_A+D+Y D_w].
 \tag{9}
\]

This is a use of an actual fourth-moment product inequality, not a
replacement of a coordinate maximum by an unrelated RMS norm.
In particular, no vector estimate of the false general form
\(\|k\odot\Delta u\|_{2,n}\le C\|k\|_{4,n}
\|\Delta u\|_{2,n}\) is used. The coordinate change cancels this
product from the state equation, and the remaining fourth-moment use is
only in the scalar Gram pairing just displayed. Here
\(\|b\|_{p,n}=(n^{-1}\sum_i|b_i|^p)^{1/p}\).

Put \(E(t)=\int_0^t\|\Delta r(s)\|_2/\sqrt m\,ds\) and
\(\bar\rho(s)=Ye^{-2\kappa s}\). Subtracting (1)--(2) yields

\[
 \begin{aligned}
 D(t)&\le D(0)+CY E(t)
  +C\int_0^t\bar\rho[D_w+Y(E_A+D)]\,ds,\\
 D_w(t)&\le C E(t)+C\int_0^t\bar\rho(E_A+D)\,ds.
 \end{aligned}
 \tag{10}
\]

The two initial readouts and residuals agree. For the residual difference,
use one path's positive tangent Gram as the homogeneous matrix and the
other path's residual in the forcing. The propagator norm is at most
\(e^{-2\kappa(t-s)}\). Integrating its bound and using Tonelli gives

\[
 E(t)\le\frac C\kappa\int_0^t
              \bar\rho(E_A+D+YD_w)\,ds.
 \tag{11}
\]

Insert this into (10), divide the readout inequality by \(Y>0\), and
add the constant \(E_A\). Since \(Y\le1\), the resulting function
\(R(t)=E_A+D(t)+D_w(t)/Y\) obeys

\[
 R(t)\le E_A+D(0)+
 \frac{C(1+\kappa^{-1})}{Y}\int_0^t\bar\rho(s)R(s)\,ds.
\]

Because \(\int_0^\infty\bar\rho=Y/(2\kappa)\), integral
Gronwall proves

\[
 \sup_{t\ge0}\{D(t)+D_w(t)/Y\}
 \le C[E_A+\|\Delta W(0)\|_F].
 \tag{12}
\]

The constant can be exponential in fixed inverse-gap and other data
constants, but it is independent of width and of \(H\).

For any unit query \(v\), decompose it into training-span and
orthogonal components. The latter first weights are unchanged. The
former preactivations are reconstructed with \(T\), and (6) gives a
uniform query RMS bound on their difference. Forward subtraction and
\(|\phi|\le1\) now imply

\[
 \sup_{t\ge0,\ \|v\|_2=1}|f_n(t,v)-f_n'(t,v)|
 \le CY\left[(1+2H)\frac{\|\Delta A(0)\|_F}{\sqrt n}
                       +\|\Delta W(0)\|_F\right].
 \tag{13}
\]

If the two fitted limits exist, the same bound holds there by continuity
and the uniform estimate. This proves the new deterministic comparison.

The same inequalities also bound the linearized propagator in the
\((\eta,W,w)\) coordinates, using the norm
\(\|\delta\eta\|_F/\sqrt n+\|\delta W\|_F
+\|\delta w\|_2/(Y\sqrt n)\), with fixed initial source.
For a nonzero initial state variation, (11) gains the initial residual
difference divided by \(2\kappa\); that difference is bounded by the
same state norm through the forward derivative. Thus the width-independent
propagator bound is not restricted to variations initialized at zero.

## 3. What the inherited source event now gives

The authorized source correction's quadratic-exponential budget, equation
(40) of its section 12, gives on one event of probability tending to one

\[
 \sup_{a,t}\left(\frac1n\sum_i|k_{a,i}(t)|^4\right)^{1/4}
 \le C Y.
\]

Its constants depend on the fixed data and source allowance. This supplies
the fourth-moment hypothesis in (5), without an extra label restriction.
The fitting event supplies the operator caps, tangent gap, and residual
envelope. Bounded tanh gives
\(\|w(t)\|_\infty\le2\int_0^\infty\rho\le CY\).
Finally the already proved running carrier maximum is
\(\max_{a,i,t}|k_{a,i}(t)|\le CY\sqrt{\log(en)}\).
Equation (2), using \(|r_a|\le\sqrt m\rho\), gives

\[
 H\le CY^2\sqrt{\log(en)}.
 \tag{14}
\]

The standard Gaussian initialization coordinates are
\(G=(A(0),\sqrt nW(0))\). Equation (13) is a good-set Lipschitz
bound with coefficient

\[
 L_n=\frac{CY}{\sqrt n}
                  [1+CY^2\sqrt{\log(en)}].
 \tag{15}
\]

Unlike the inherited general bound, there is no exponential of a growing
carrier maximum. The only growing coefficient is the source gate ratio.

For completeness, the remaining probability and topology conversion can
be performed without differentiating an event indicator. Extend each
scalar good-set prediction by its infimum Lipschitz extension and truncate
to the known amplitude interval. The extensions agree with actual
predictions on the good set and are globally \(L_n\)-Lipschitz.

A useful elementary Gaussian comparison is the following. For independent
standard Gaussian vectors \(G,G'\), write
\(G_\theta=G\cos\theta+G'\sin\theta\) and
\(V_\theta=-G\sin\theta+G'\cos\theta\). For each \(\theta\),
these are independent standard Gaussians. The fundamental theorem of
calculus and Minkowski give, for smooth \(F\) and \(p\ge2\),

\[
 \|F(G)-F(G')\|_{L^p}
 \le\frac\pi2\|N(0,1)\|_{L^p}
                          \|\,\|\nabla F(G)\|_2\,\|_{L^p}.
 \tag{16}
\]

Condition on \(G_\theta\) to evaluate the Gaussian inner product
with \(V_\theta\). Smooth approximation extends this to Lipschitz
functions, giving an upper bound \(C\sqrt pL_n\); the scalar Gaussian
moment bound follows by integrating its tail.

Use the inherited physical proof coordinate \(u=1-e^{-ct}\) and the
width-independent time/query moduli, including the endpoint. A mesh of
size \(1/n\) has at most \(N_n=(n+1)(1+2n)^d\) points. Apply (16)
with \(p\) a fixed multiple of \(\log(2N_n/\delta)\), then Markov
and a union bound, and add the \(O(Y/n)\) off-grid error. At each
sufficiently large width the inherited good-path failures can be made at
most \(\delta/2\). Thus the new comparison, conditional on those
inherited probability inputs and their original label allowance, is

\[
 \|f_n-f_n'\|_*
 \le\frac{C_{\mathrm{data}}Y}{\sqrt n}
 [1+C_{\mathrm{data}}Y^2\sqrt{\log(en)}]
 \sqrt{\log[2(n+1)(1+2n)^d/\delta]}
 +\frac{C_{\mathrm{data}}Y}{n}
 \tag{17}
\]

with probability at least \(1-\delta\). The notation \(\|\cdot\|_*\)
means the complete physical trajectory, the full sphere, and the fitted
endpoint. At fixed nonzero labels this is
\(O_{\mathrm{data},\delta}(\log(en)/\sqrt n)\), not a strict
root-width bound. The stochastic eventual threshold remains inherited
and unquantified. No numerical dependence on data constants beyond the
displayed deterministic hypotheses is claimed.

## 4. A log-free topology and Gaussian-calculus implication

The net loss in (17) is avoidable if the appropriate directional moments
are proved. The following sufficient criterion requires only first query
derivatives, at a fixed moment order determined by dimension.

Let \(F_n(t,v;G)\) be a globally defined smooth Gaussian-root prediction
family on a fixed cube containing the unit sphere, with common initial
value zero. Fix \(p>\max(d,2)\). Suppose

\[
 \int_0^\infty\left[
 \int_{\text{cube}}
 \left(\|\,\|\nabla_G\partial_tF_n(t,v)\|_2\,\|_{L^p}^p
 +\sum_{j=1}^d
 \|\,\|\nabla_G\partial_{v_j}\partial_tF_n(t,v)\|_2\,\|_{L^p}^p
 \right)dv\right]^{1/p}dt
 \le\frac C{\sqrt n}.
 \tag{18}
\]

Then independent copies satisfy

\[
 \left\|\sup_{t\ge0,\ \|v\|=1}
 |F_n(t,v;G)-F_n(t,v;G')|\right\|_{L^p}
 \le\frac{C_{d,p}C}{\sqrt n}.
 \tag{19}
\]

Here is a direct proof of the only spatial estimate needed. On a fixed
convex cube, average the line-segment fundamental theorem between a point
\(x\) and points \(y\) in the cube. Substituting
\(z=x+t(y-x)\) gives

\[
 |H(x)|\le C_d\|H\|_{L^p}
 +C_d\int_{\text{cube}}\frac{|\nabla H(z)|}{|z-x|^{d-1}}\,dz.
\]

For \(d=1\) the kernel is one. For \(d>1\), its Hölder conjugate
power is integrable uniformly in \(x\) precisely when \(p>d\).
Thus \(\|H\|_\infty\le C_{d,p}\|H\|_{W^{1,p}}\).
Apply this inequality to the difference of two time derivatives, then
apply (16) to it and each first spatial derivative. Fubini identifies the
spatial/probability \(L^p\) norm with the integrand of (18).
Finally integrate in time and use Minkowski and the common initial value.
This proves (19). Markov gives confidence \(1-\delta\) with coefficient
\(C_{d,p}C\delta^{-1/p}\). Where fitted limits exist, the uniform
estimate passes to the endpoint.

This criterion has no growing net or neuron maximum. It is also explicit
about localization: a family agreeing with the physical flow on an event
of probability \(1-\delta/4\) suffices if (18) holds globally for
that family. A bound on
\(\mathbb E[\mathbf1_{\Omega_n}\|\nabla F_n\|^p]\) alone does
not supply such a family. Differentiating its indicator would add a
boundary contribution. The existing infimum extensions justify (17), but
have not been shown to satisfy the sharper moment condition (18).

Here are the full quantifiers of this remaining sufficient condition.
For each fixed admissible dataset and \(\delta\in(0,1)\), it is enough
to construct one \(p>\max(d,2)\), constants
\(C<\infty\), \(n_0<\infty\), and, for every \(n\ge n_0\), a
globally defined family \(F_n\) and a Gaussian-root event \(\Omega_n\)
such that \(\Pr(\Omega_n)\ge1-\delta/4\), equation (18) holds with
that same \(C\), and \(F_n(t,v;G)=f_n(t,v;G)\) for every physical
time and sphere query whenever \(G\in\Omega_n\). The families must
have common initial value zero and the differentiability/integrability
used above. Equations (18)--(19), Markov with failure \(\delta/2\),
and the two exceptional events would then give the requested
\(C_{\mathrm{data},\delta}/\sqrt n\) comparison. This precise
extension-and-moment statement is **not proved** here. It is sufficient;
no assertion is made that every proof of strict root concentration must
establish it.

## 5. The precise remaining mixed term

The tanh transformation does not silently solve the Gaussian-root problem.
The initial source enters the recovered features through the following
partial derivative, with the current increment held fixed:

\[
 S_{a,i}(t)=\partial_{u_{a,i}(0)}T(u_{a,i}(0),\eta_{a,i}(t))
 =\frac{p(u_{a,i}(t))}{p(u_{a,i}(0))}
 \le1+2|\eta_{a,i}(t)|.
 \tag{20}
\]

This is not the total derivative through the trajectory
\(\eta(t)\). That additional derivative is the transported state
response.

An adjoint representation of an initial-root derivative multiplies such
diagonal source factors by transported response coordinates. The new
state stability bounds the response in global Euclidean norm. The source
event bounds every fixed counting moment of \(S\), since (2) and the
carrier moment budgets bound the corresponding moments of \(\eta\).
Neither statement controls their correlated product. A bound of the
needed form is, schematically,

\[
 \mathbb E\sum_{a,i} S_{a,i}(t)^2|q_{a,i}(t,v)|^2\le C/n,
 \tag{21}
\]

for the actual appropriately normalized prediction response, with the
time-integrated and first-query-derivative versions required by (18).
The global localization must also be supplied. Equation (21) is a stated
mixed-product form, not a fully specified response theorem or an added
assumption in a claimed strict theorem. The precise sufficient missing
estimate, with its norm and all width/confidence quantifiers, is (18)
and the final paragraph of section 4.

Here is a concrete reason separate moment bounds cannot replace (21).
Let \(Z_i\) be independent standard Gaussians and choose
\(q_i=n^{-1/2}\mathbf1_{i=i_*}\), where \(i_*\) maximizes
\(|Z_i|\). Then \(\sum_iq_i^2=1/n\), and all expected counting
moments \(n^{-1}\sum_i|Z_i|^p\) are Gaussian constants, but

\[
 \mathbb E\sum_i Z_i^2q_i^2
 =\frac1n\mathbb E\max_iZ_i^2\ge c\frac{\log n}{n}.
 \tag{22}
\]

For the lower bound, put \(u=\sqrt{\log n}\). Integrating the
Gaussian density on \([u,u+1/u]\) gives
\(\mathbb P(|Z|\ge u)\ge c n^{-1/2}/\sqrt{\log n}\).
Independence implies \(\mathbb P(\max_i|Z_i|\ge u)\to1\), proving
(22). Smooth normalized soft-max weights approximate the displayed
\(q\) and retain the same obstruction at each fixed width. This is not
a counterexample to neural concentration: it only refutes the proposed
inference from marginal carrier moments and a global response norm.

The change of variables makes a more focused cavity approach plausible:
a cavity-linearized Gaussian source transported by a width-independent
operator has controlled coordinate fourth moments, so its quadratic
remainder need not pay an operator maximum. However, the removed neuron's
time-dependent amplitudes and the cavity's terminal response must use
their own joint source law. No complete proof of those coupled insertion
and remainder estimates is provided here. Treating their coefficients as
independent would recreate the matrix-reuse error identified in the
authorized sources.

## Internal check and final claim boundary

- Orthogonality is used exactly in (1) and in the diagonal first-layer
  contribution of (8); the new argument is not advertised for general
  data geometry.
- The primitive is \(Q'=1/\phi'\), not \(1/(\phi')^2\). Its inverse
  has derivative \(p\), and the hidden feature has derivative \(p^2\).
- The gate-ratio inequality follows from the bounded derivative of
  \(1/p\) in \(Q\)-coordinates and avoids an unjustified exponential
  gate-ratio estimate.
- The state comparison uses actual endpoint trajectories. Fourth carrier
  moments enter the explicit product inequality preceding (9).
- The inherited source supplies those fourth moments without a new label
  cap; it still supplies the maximum used in the source factor (14).
- Width-independent dynamical stability does not by itself imply
  width-independent Gaussian-root concentration. Equations (20)--(22)
  retain that distinction.
- The new conditional dense-copy upper is logarithmic-over-root (17).
  The strict root theorem, the necessary mixed directional estimate,
  global localization, and its query increments remain unproved.
- The author check is internal, not an independent review. The final
  source hash is reported separately after the final edit.
