# Quantitative audit and provable improvements of the odd two-input coefficient

This note uses the existing theorem and its attached mathematical source
lemmas. It does not assert a polynomial activation coefficient for the complete
population/GF/raw-GD theorem. It proves two polynomial component estimates and
an improved finite-array bound, and identifies precisely the remaining source
response obstruction.

The sources are `PROOF.md`, `AFFINE_CORE.md`, `SOURCE_AND_LIMIT_BRIDGE.md`,
`sources/TWO_SAMPLE_SOURCE_BASELINE.md`, and
`sources/THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA.md` in
`studies/mean_field_peeling/two_sample_odd_activation_theorem/`.
No experiment, repository edit, or delegation was used.

## 1. What the old coefficient selection actually implies

Write
\[
 S_\delta=192/\delta,\quad U=11+12\sqrt2\,\delta^{-1/2},
 \quad p=11+2U+4S_\delta(2U)^3.
\]
As \(\delta\downarrow0\),
\[
 S_\delta=\Theta(\delta^{-1}),\quad U=\Theta(\delta^{-1/2}),
 \quad p=\Theta(\delta^{-5/2}),\quad p^2S_\delta=\Theta(\delta^{-6}).
\]
The actual selection (17), together with (16), therefore obeys
\[
 e_{\rm old}(\delta)
 \le\frac1{1280p^2S_\delta\exp(36p^2S_\delta)}
 \le C\delta^6\exp(-c\delta^{-6})
 \tag{1}
\]
for absolute positive \(c,C\), on a sufficiently small positive interval.
Thus this particular selected threshold is smaller than every fixed positive
power of \(\delta\). This is an upper bound on the threshold selected by that
proof, not an upper bound on the largest activation coefficient for which the
theorem is true.

Nor does the proof establish that its selected threshold is asymptotic to a
single exponential. Its other source restriction is
\[
 e\le [2K\exp(KS_\delta)]^{-1}.
 \tag{2}
\]
Here \(K\) is built from \(A_0,M_0\), which already contain
\(\exp(36p^2S_\delta)\), and from further exponentials and Gaussian exponential
moment bounds. Equation (1) does not lower-bound the minimum containing (2).
Calling the complete threshold simply \(\exp(-C\delta^{-6})\) is consequently
not justified by the displayed selection.

## 2. Explicit Gaussian nonaffinity: a polynomial bound independent of the upper variance cutoff

For a real square-integrable variable \(Z\), define
\[
 R(Z)=\inf_{\alpha,\beta\in\mathbb R}
 E[\arctan Z-\alpha-\beta Z]^2.
\]
Let \(G\sim N(0,1)\), \(H_3(G)=G^3-3G\). Its inner products with
\(1,G\) vanish, and \(E H_3^2=6\). Therefore every affine competitor has
the same inner product with \(H_3\), and Cauchy--Schwarz gives
\[
 R(\nu G)\ge \frac{(E[\arctan(\nu G)H_3(G)])^2}{6},\qquad \nu>0.
 \tag{3}
\]

One Gaussian integration by parts gives
\[
 E[\arctan(\nu G)H_3(G)]
 =\nu E\frac{G^2-1}{1+\nu^2G^2}.
\]
Indeed the Gaussian derivative identity applied to the test polynomial
\(G^2-1\) gives \(E[f(G)H_3(G)]=E[f'(G)(G^2-1)]\).
All boundary terms vanish because arctangent and its first derivative are
bounded and the Gaussian density dominates the polynomial factors.

Using
\((1+\nu^2G^2)^{-1}=\int_0^\infty e^{-u}e^{-u\nu^2G^2}\,du\)
and the elementary Gaussian integrals
\[
 E e^{-tG^2}=(1+2t)^{-1/2},\qquad
 E[G^2e^{-tG^2}]=(1+2t)^{-3/2},
\]
we obtain
\[
 B(\nu):=-E[\arctan(\nu G)H_3(G)]
 =2\nu^3\int_0^\infty
        \frac{u e^{-u}}{(1+2u\nu^2)^{3/2}}\,du>0.
 \tag{4}
\]
The signed interchange is justified by
\(E|G^2-1|\int_0^\infty e^{-u}\,du<\infty\).
Restricting (4) to \(0\le u\le1\) yields
\[
 B(\nu)\ge \frac{e^{-1}\nu^3}{(1+2\nu^2)^{3/2}},
 \qquad
 R(\nu G)\ge
 \frac{e^{-2}\nu^6}{6(1+2\nu^2)^3}.
 \tag{5}
\]
The right side is increasing with \(\nu>0\).

In the old notation, \(m=\sqrt{\delta/32}\), \(L=U^3\), and
\(\eta_\delta=\min_{m\le\nu\le L}R(\nu G)\). Thus
\[
 \eta_\delta\ge
 \frac{e^{-2}\delta^3}{6(32+2\delta)^3}
 \ge c_0\delta^3,
 \qquad c_0=\frac{1}{6e^2 34^3}>0.
 \tag{6}
\]
No upper variance bound was used in (6): the estimate holds uniformly on
the entire range \(\nu\ge m\).

In fact the exact small-\(\delta\) order, including the leading constant,
can be recovered without proving monotonicity of the full regression error.
For each \(u\ge0\), the function
\(\nu^3/(1+2u\nu^2)^{3/2}\) is increasing. Hence \(B\) is increasing.
Equation (3) gives
\[
 B(m)^2/6\le\eta_\delta\le R(mG).
\]
Dominated convergence in (4) gives \(B(\nu)/\nu^3\to2\).
Also
\[
 \left|\arctan z-z+\frac{z^3}{3}\right|\le\frac{|z|^5}{5}
 \tag{7}
\]
because the derivative of the expression on the left before taking its
absolute value is \(z^4/(1+z^2)\). Thus, in Gaussian \(L^2\),
\[
 \arctan(\nu G)=\nu G-\nu^3G^3/3+O_{L^2}(\nu^5).
\]
Orthogonal projection away from \(\operatorname{span}\{1,G\}\) removes
\(\nu G\) and sends \(G^3\) to \(H_3\). It follows that
\[
 R(\nu G)=\frac23\nu^6+O(\nu^8).
\]
The two bounds have the same leading constant, so
\[
 \boxed{\eta_\delta\sim\frac{\delta^3}{49152}}
 \qquad(\delta\downarrow0).
 \tag{8}
\]

## 3. Regression transfer loses no inverse power of the variance

For any nonconstant square-integrable \(Z\), its optimal slope is
\(\beta_Z=\operatorname{Cov}(Z,\arctan Z)/\operatorname{Var}(Z)\).
If \(Z'\) is an independent copy, then
\[
 \operatorname{Cov}(Z,\arctan Z)
 =\tfrac12E[(Z-Z')(\arctan Z-\arctan Z')].
\]
Monotonicity and the 1-Lipschitz property of arctangent imply
\[
 0\le (Z-Z')(\arctan Z-\arctan Z')\le(Z-Z')^2.
\]
Consequently \(0\le\beta_Z\le1\). If \(Z\) is constant, choose the
optimal slope \(\beta_Z=0\).

For every \(\beta\in[0,1]\), the derivative of
\(z\mapsto\arctan z-\beta z\) belongs to \([-\beta,1-\beta]\), so that
map is 1-Lipschitz. Use the optimizer \((\alpha_Z,\beta_Z)\) as a
competitor for an arbitrary coupled square-integrable \(Z_0\). Minkowski's
inequality gives
\[
 \sqrt{R(Z_0)}
 \le\sqrt{R(Z)}+\|Z-Z_0\|_2.
\]
Interchanging the variables proves
\[
 \boxed{|\sqrt{R(Z)}-\sqrt{R(Z_0)}|\le\|Z-Z_0\|_2.}
 \tag{9}
\]
Taking the infimum over couplings also makes \(\sqrt R\) a 1-Lipschitz
functional in the Wasserstein \(W_2\) distance on real probability laws
with finite second moments.

In particular,
\[
 R(Z_0)\ge\eta_\delta,\qquad
 \|Z-Z_0\|_2\le\tfrac12\sqrt{\eta_\delta}
 \quad\Longrightarrow\quad R(Z)\ge\eta_\delta/4.
 \tag{10}
\]
This replaces the old tolerance
\(\min\{m/2,\sqrt\eta/[2(1+\pi/m)]\}\), which has order \(\delta^2\),
by a tolerance of order \(\delta^{3/2}\). There is no variance side
condition on the perturbed variable. An entirely explicit sufficient
tolerance is \(\sqrt{c_0}\,\delta^{3/2}/2\).

If the existing field comparison is \(\|Z_e-Z_0\|_2\le Je\), this component
of the activation restriction becomes
\[
 e\le\frac{\sqrt{c_0}\,\delta^{3/2}}{2J}.
 \tag{11}
\]
The resulting activation regression error remains at least
\(e^2 c_0\delta^3/4\), by absorbing the linear activation term into its
affine regression competitor.

## 4. Sharper finite-array primal premise from the affine energy identity

The old bound \(p=11+2U+4S_\delta(2U)^3\) estimates each update factor
separately before summing time. For the actual constant feature controls
\(c_i=y_i/2\), the affine gradient energy gives a stronger estimate.
This argument is specific to these controls; it does not assert the same
energy bound for arbitrary time-varying controls in the general lemma.

Let \(S\le S_\delta\) be a reference path's first hit of \(g=3/2\).
Its exact raw energy identity is
\[
 \int_0^S\|V_0(\Theta(s))\|_{\rm raw}^2\,ds=3/2.
 \tag{12}
\]
Take population affine Euler meshes of \([0,S]\). The bounded affine
polynomial field has a uniform bounded-ball Lipschitz constant. Strong
Euler convergence, followed by convergence of the Riemann sums of the
continuous squared direction norm, gives
\[
 \sum_{k<N}h_k\|V_0(\Theta_k^0)\|_{\rm raw}^2\longrightarrow3/2
 \qquad (\max h_k\to0).
 \tag{13}
\]
The bounded-ball constants and the duration bound depend only on
\(\delta\). Thus meshes can be restricted to sufficiently small maximum
step, uniformly in the admissible data, so that the sum in (13) is at
most \(7/4\). This restriction is sufficient for the subsequent mesh
limit and for applying the source lemma to the meshes under consideration.

At any such fixed mesh, every finite affine squared raw update norm is a
finite sum of products of empirical scalar contractions of generated
fields. For example, a matrix update has squared Frobenius norm
\[
 \left\|\sum_i c_i b_i\otimes_n h_i\right\|_F^2
 =\sum_{i,j}c_ic_j\langle b_i,b_j\rangle_n
                         \langle h_i,h_j\rangle_n,
\]
and the first block has the corresponding fixed factor \(\Gamma_{ij}\).
The already supplied fixed-program convergence therefore implies
\[
 \sum_{k<N}h_k\|V_{0,n}(\Theta_{k,n}^0)\|_{{\rm raw},n}^2
 \le2
 \tag{14}
\]
with probability tending to one at that fixed mesh. This uses no operator
norm convergence and no Gaussian theorem for a growing transcript.
Keeping the original finite initial readout changes no fixed-program
limit, since its normalized norm tends to zero.

For every prefix, the exact Euler update and Cauchy--Schwarz now give
\[
 \|\Theta_{k,n}^0-\Theta_{0,n}^0\|_{{\rm raw},n}
 \le\sum_{r<k}h_r\|V_{0,n}(\Theta_{r,n}^0)\|_{{\rm raw},n}
 \le\sqrt{2S_\delta}.
 \tag{15}
\]
The raw norm controls each learned matrix's ordinary Frobenius norm, and
therefore its operator norm. It also controls the readout's normalized
norm and each first projected preactivation change:
\(\|\Delta W^1x_i\|_n\le\sqrt{d/n}\|\Delta W^1\|_F\), because
\(\|x_i\|=\sqrt d\).

Intersect (14) with the high-probability events that both initialized
matrix operator norms are at most 10, both initial first projection norms
are at most 2, and the initial readout norm is at most 1. Equations
(14)--(15) show that the finite-array primal premise holds with
\[
 \boxed{P_\delta=11+\sqrt{2S_\delta}
                 =11+8\sqrt6\,\delta^{-1/2}.}
 \tag{16}
\]
The added 1 supplies strict slack for the largest initial operator bound.
All events are at one fixed mesh; no probability assertion uniform over
growing meshes has been made. If preferred, the still-conservative
\(12+24\delta^{-1/2}\) follows by replacing the energy bound 2 with 3.

Substituting (16) into the existing source lemma is legitimate because
that lemma requires precisely a finite-array primal bound, independent
of mesh and width, on the meshes used in the limiting construction.
The remaining old source proof is unchanged, but its explicit affine
factor becomes
\[
 \widehat F_\delta=\exp(36P_\delta^2S_\delta)
                   =\exp(O(\delta^{-2})),
 \tag{17}
\]
instead of \(\exp(O(\delta^{-6}))\). In fact
\(36P_\delta^2S_\delta\sim2{,}654{,}208\,\delta^{-2}\).

## 5. An improved complete selection, with the unresolved restriction explicit

Keep the existing population comparison constants
\[
 b=4U,\quad Q=40b^3S_\delta e^{9b^2S_\delta},\quad
 J=12b^2Q+\pi b^2,\quad O=10b^3Q+b(J+\pi/2).
\]
Recompute the source constant \(K\) using the proven smaller primal
premise \(P_\delta\) in (16). Let
\[
 \widehat E_*=
 \min\left\{1,
 \frac1{640P_\delta^2S_\delta e^{36P_\delta^2S_\delta}},
 \frac1{2\widehat K e^{\widehat K S_\delta}}\right\},
\]
where \(\widehat K\) is obtained from the same source-response algebra
with these new arguments. Then the complete existing theorem is proved by
the modified selection
\[
 \widehat e_\delta=
 \frac12\min\left\{\frac12,\widehat E_*,
          \frac b{4Q},\frac1{4O},
          \frac{\sqrt{c_0}\,\delta^{3/2}}{2J}\right\}>0.
 \tag{18}
\]
The old separate restrictions involving \(m/(2J)\) and \(\pi/m\) can
be removed by (9)--(11). Every other use of the threshold in the old
proof remains satisfied. In particular the old raw-state margin and
prediction endpoint margin are preserved.

For orientation, set \(E_\delta=9b^2S_\delta\); then
\[
 E_\delta\sim7{,}962{,}624\,\delta^{-2},\quad
 Q=\Theta(\delta^{-5/2}e^{E_\delta}),\quad
 J=\Theta(\delta^{-7/2}e^{E_\delta}),\quad
 O=\Theta(\delta^{-4}e^{E_\delta}).
\]
The new nonaffinity restriction alone has order
\(\delta^5e^{-E_\delta}\), whereas the old transfer restriction has
order \(\delta^{11/2}e^{-E_\delta}\). All the explicit restrictions in
(18) except the one containing \(\widehat K\) can be met by a coefficient
of order \(c\delta^5\exp(-C\delta^{-2})\) with sufficiently large
absolute \(C\). This does not control the omitted restriction.

There remains a second difficulty besides polynomial raw stability:
the source argument controls absolute response coefficient rows, invokes
Volterra exponentials in those row bounds, bounds derivative envelope
moments, and performs another chronological Gronwall closure. The current
proof supplies a finite \(\widehat K\) for each \(\delta>0\), but does
not prove it polynomial in \(\delta^{-1}\), and even such a polynomial
bound by itself would leave \(\exp(\widehat K S_\delta)\).

Therefore a complete claim \(\theta_\delta\ge c\delta^p\) still requires
a new stability/response argument that avoids these exponential losses
(or an alternative construction bypassing the response perturbation
scheme). The nonaffinity gap is not the source of superpolynomial
smallness, and the \(\delta^{-6}\) in the first explicit exponential is
an avoidable artifact of the old finite-array primal estimate.

## 6. Stronger affine structure: the actual reference nonaffinity has a constant lower bound

The old \(\eta_\delta\) is the minimum over an unnecessarily large class
of Gaussian laws. Exact affine balancedness gives a lower variance bound
independent of \(\delta\) for the Gaussian laws that actually occur.

Absorb the label sign \(\sigma\) into the readout and write
\[
 v=v_u,\qquad p=P_1/\sqrt v,\qquad \lambda=a^3\sqrt v,
 \qquad r=\|C\|^2.
\]
The active raw coordinates satisfy
\[
 p'=\lambda A^*B^*C,\quad
 A'=\lambda B^*C\otimes p,\quad
 B'=\lambda C\otimes Ap,\quad C'=\lambda BAp.
 \tag{19}
\]
The initial Gaussian propagation gives
\(\|p_0\|=\|A_0p_0\|=\|B_0A_0p_0\|=1\).
Differentiate bounded operator products using (19). The derivatives
cancel in the differences, giving the exact identities
\[
 \|p\|^2=1+r,\qquad
 A^*A-p\otimes p=A_0^*A_0-p_0\otimes p_0,
 \qquad BB^*-C\otimes C=B_0B_0^*.
 \tag{20}
\]
No trace of an infinite-dimensional initialized action is used here.
These are identities of bounded operators obtained by integrating their
strongly differentiable products.

Since \(\|B_0\|\le10\), (20) implies
\(\|B\|^2\le100+r\). Pairing the middle identity with \(p\) and using
\(\|p_0\|=1\) yields
\[
 \|Ap\|^2
 =\|A_0p\|^2+\|p\|^4-|\langle p_0,p\rangle|^2
 \ge r(1+r).
 \tag{21}
\]
The existing radial argument gives \(\|C'\|\ge\|C'(0)\|=\lambda\).
Combining it with \(C'=\lambda BAp\) gives the second bound
\[
 \|Ap\|^2\ge\frac1{100+r}.
 \tag{22}
\]
For \(r\le1\), (22) is at least \(1/101\); for \(r\ge1\), (21)
is at least 2. Therefore
\[
 \|Ap\|^2\ge1/101\quad\text{at every reached affine time}.
 \tag{23}
\]

Use the already proved zero active/inactive covariance and frozen inactive
fields. At the first layer,
\[
 \operatorname{Var}(z_i^1)=v(1+r)+(1-v)\ge1.
\]
At the second layer, \(P_2=a\sqrt v Ap\), so
\[
 \operatorname{Var}(z_i^2)
 =a^2[v\|Ap\|^2+(1-v)]\ge a^2/101\ge1/404.
\]
At the third layer, \(P_3=a^2\sqrt v BAp\), and the radial bound gives
\(\|BAp\|\ge1\). Thus
\[
 \operatorname{Var}(z_i^3)
 =a^4[v\|BAp\|^2+(1-v)]\ge a^4\ge1/16.
 \tag{24}
\]
All affine marginal standard deviations are consequently at least
\(m_*=1/\sqrt{404}\). Applying (5) gives the uniform actual-path bound
\[
 R(z_i^\ell(s))\ge\eta_*:=\frac1{6e^2 406^3}>0.
 \tag{25}
\]
Unlike (8), (25) concerns the actual reference fields, rather than the
minimum over the old artificially expanded variance interval.
The coefficient choice in (18) can therefore be strengthened again by
replacing \(\sqrt{c_0}\,\delta^{3/2}/(2J)\) by
\(\sqrt{\eta_*}/(2J)\). The regression margin becomes
\(e^2\eta_*/4\), uniformly in the separated data and \(\delta\).

## 7. Additional affine duration and norm improvements from the same identities

These estimates can be used independently by a new stability analysis.
Put \(u=\|C\|\). Differentiating the last equation in (19) gives
\[
 C''=\lambda^2\bigl[
       \|Ap\|^2 I+\|p\|^2 BB^*+BAA^*B^*\bigr]C.
 \tag{26}
\]
For \(s>0\), \(u>0\), and direct differentiation of the norm gives
\[
 u''=\frac{\|C'\|^2-(u')^2+\langle C,C''\rangle}{u}.
\]
The first two terms in the numerator have nonnegative difference by
Cauchy--Schwarz. Moreover
\(\|B^*C\|^2\ge r^2\) by the last invariant in (20). Equations
(21) and (26) therefore imply
\[
 u''\ge2\lambda^2u^3(1+u^2).
 \tag{27}
\]
The radial argument gives \(u'\ge u'(0+)=\lambda\). Multiply (27)
by \(2u'\) and integrate from zero to obtain
\[
 (u')^2\ge\lambda^2(1+u^4+\tfrac23u^6).
 \tag{28}
\]
Since \(g=\langle C,C'\rangle=uu'\), before the hit \(g=3/2\),
\[
 g\ge\sqrt{2/3}\,\lambda u^4,\qquad
 u^4\le\frac{3\sqrt6}{4\lambda}.
 \tag{29}
\]
The invariants also give
\[
 \|A\|^2\le101+r,\qquad \|B\|^2\le100+r,\qquad
 \|p\|^2=1+r.
\]
Thus all actual reference primal norms are bounded by
\(C(1+\lambda^{-1/4})\), and hence by \(C\delta^{-1/8}\), with an
absolute constant. For the original first projections use
\(\|P_1\pm Q_1\|^2=1+v r\le1+r\).

Because \(u'\ge\lambda\sqrt{1+u^4+(2/3)u^6}\), the total reference
duration is at most
\[
 \frac1\lambda\int_0^\infty
       \frac{du}{\sqrt{1+u^4+(2/3)u^6}}
 \le\frac{1+\tfrac12\sqrt{3/2}}{\lambda}
 <\frac2\lambda\le16\sqrt2\,\delta^{-1/2}.
 \tag{30}
\]
Here the integral on \([0,1]\) is bounded by 1 and the integrand on
\([1,\infty)\) by \(\sqrt{3/2}\,u^{-3}\).
The first-hit existence proof remains valid with these bounds: before
the hit, (29) and the operator bounds preclude finite primal blowup;
local affine continuation applies, while (28) precludes a branch staying
below the target for a time longer than (30).

These sharpened affine estimates do not themselves establish a polynomial
nonlinear source threshold. They do suggest why a sharper stability proof
may achieve one: in the normalized time \(\tau=\lambda s\), an affine
linearization with size \(C(1+u^2)\) has integrated size bounded by
\[
 C\int_0^{u(S)}\frac{1+u^2}{\sqrt{1+u^4+(2/3)u^6}}\,du
 =O(1+\log(1/\delta)).
\]
Exponentiating this last bound would cost only a power of
\(\delta^{-1}\). Applying it to the actual source perturbation and all
response rows remains a separate proof obligation.
