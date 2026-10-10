# Isolated check of the finite-horizon fifth-power estimate

Date: 2026-10-10.

Reviewed frozen input: `FINITE_HORIZON_FIFTH_POWER.md`, SHA256
`93d66c58ff227281c9be627c57a6d207fe4b606ea5f0fdd7205e71375e3e96b4`.

Verdict: **PASS for the stated fixed finite-horizon estimate**, using the
paper's fitting and source results with their stated hypotheses. I found
no mathematical gap in the fifth-power tail estimate, its transfer to the
actual closure, the continuation argument, or conversion to the same
physical time on the whole sphere. This does not establish the all-time
order \(q=n^{1/10+o(1)}\) requested in the broader task.

One wording correction is required: line 29 says that the labels are
“fixed and positive.” Replace this by “The label vector is fixed, with
\(Y>0\).” The original setup explicitly permits signed labels
(`paper/compact.tex`, lines 119–125), and this proof only uses positivity
of their RMS norm \(Y\), not positivity of individual labels.

The complete assigned inputs were read: the frozen note,
`paper/compact.tex`, `paper/compact_fitting.tex`,
`paper/compact_foundations.tex`, `paper/compact_legendre.tex`, and
`CROSS_TAIL_IDENTITIES.md`. The last file was used only for the scalar
projection dependency. No study history, prior reports, other studies,
or unassigned author notes were consulted. In particular, the additional
study note named at frozen-input line 7 was not needed: the required
uniform scalar identities appear in the assigned cross-tail input.
This is an audit of the finite-horizon argument and its use of the
paper's theorem interfaces, not a new independent certification of the
entire source theorem's cavity argument.

## Setup and source scope

The dense and Legendre trajectories use the same initialization and the
original equations. In mobility coordinates write

\[
 \theta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n),
 \qquad r_a=f(x_a)-y_a,\qquad
 \rho=\|r\|_2/\sqrt m.
\]

The parameter norm below is the Euclidean norm of these blocks. The
original forward features are \(h^{(j)}=\phi_j(z^{(j)})\), with
\(z^{(1)}=W^{(1)}x/\sqrt d\) and
\(z^{(j)}=W^{(j)}h^{(j-1)}\). The prediction is
\(f=w^\top h^{(L)}/n\). The residual-free backward responses are
\(\delta^{(j)}=\phi'_j(z^{(j)})\odot k^{(j)}\), where
\(k^{(L)}=w\) and
\(k^{(j)}=W^{(j+1)\top}\delta^{(j+1)}\).
For a training family of neuron vectors use
\(\|u\|_{\mathrm{RMS}}^2=(mn)^{-1}\sum_a\|u_a\|_2^2\).
The layer index is suppressed when the same bound holds in every layer.

Let \(\ell_n=\log(en)\), fix \(T<\infty\) independently of width,
and write subscripts \(D\) for the dense trajectory and hats for the
closure. All constants in this report may depend on the fixed problem,
confidence, and \(T\), including the positive number \(Y\), but not
on \(n\) or \(q\).

The source proposition's complex-time domain extends through
\(32(m/\gamma)\ell_n\), with time radius

\[
 r_t=\frac{c_0}{\sqrt{\ell_n}},\qquad
 c_0=\frac{\gamma}{\beta^{30L}Y^2m\sqrt{d+3}}>0.
\]

It gives width-independent neuron-RMS bounds on both forward and
backward fields, including \(w=k^{(L)}\), throughout that domain
(`compact_foundations.tex`, lines 8–59). Eventually its real interval
contains \([0,T+1]\); every disk of radius \(r_t/2\) centered on this
interval is contained in the stated rectangle. The required carrier
estimate is the proposition's actual dense training-carrier estimate,
also stated there. Neither a bound on closure carriers nor a coordinate
bound on passive-query carriers is imported.

The dense fitting lemma supplies the real operator and readout bounds.
The order-independent Legendre fitting claim supplies global physical
existence for every finite \(q\), on the same initialization event
(`compact_legendre.tex`, lines 204–325). These conclusions apply under
the original small-label condition. Consequently the probabilistic event
used here is independent of \(q\); a union over orders is unnecessary.

## Dense derivatives in the residual clock

Let \(J_D\) be the training-prediction Jacobian from parameter space to
sample space with its RMS inner product. Its norm is bounded by a fixed
constant on the fitting tube, as seen from its gradient blocks
\(\delta_a^{(1)}v_a^\top/\sqrt n\),
\(\delta_a^{(j)}h_a^{(j-1)\top}/n\), and
\(h_a^{(L)}/\sqrt n\). Thus
\(\dot r_D=-2J_DJ_D^*r_D\) implies
\(\dot\rho_D\ge-2\|J_D\|^2\rho_D\). Integration gives
\(\rho_D(t)\ge c_T>0\) on \([0,T+1]\).

Set \(\tau_D(t)=1+\int_0^t\rho_D(s)\,ds\) and
\(A_*=\tau_D(T+1)\). Its inverse exists on \([1,A_*]\), and fitting
gives \(A_*\le1+2Ym/\gamma\). Cauchy's formula in the normalized
Euclidean vector norm gives, for a bounded holomorphic field \(u\),

\[
 \|\partial_t^k u(t)\|_{\mathrm{RMS}}
 \le k!B(2/c_0)^k\ell_n^{k/2},\qquad 0\le k\le4.
\]

There is no factor \(\sqrt n\) left after RMS normalization. The
holomorphic readout pairing also bounds prediction derivatives through
order four. Along real time,
\(\rho_D=(m^{-1}\sum_a r_{D,a}^2)^{1/2}\); its derivatives and those
of \(1/\rho_D\) through order four have the same logarithmic powers,
with constants depending on \(c_T^{-1}\). No complex square root or
holomorphic inverse residual clock is needed.

Repeatedly applying \(\partial_\xi=\rho_D^{-1}\partial_t\), and
defining \(b_{D,a}=(r_{D,a}/\rho_D)\delta_{D,a}\), now gives

\[
 \sup_{1\le\xi\le A_*}
 \bigl(\|\partial_\xi^k h_D\|_{\mathrm{RMS}}
       +\|\partial_\xi^k b_D\|_{\mathrm{RMS}}\bigr)
 \le C_T\ell_n^2,\qquad 0\le k\le4.
\]

The derivative count is sufficient: the fourth physical derivative of
\(b_D\) uses prediction, response, and reciprocal-residual derivatives
through order four; converting four clock derivatives requires no higher
derivative. The original zero readout makes every initial hidden-weight
velocity zero. Hence the constant forward and zero backward prefixes
satisfy \(h_D'(1+)=0\) and \(b_D(1)=0\), as required.

## The fifth-power cross-tail

For projection \(\Pi_q^A\) onto degrees below \(q\) in
\(L^2([0,A])\), put \(Q_q^A=I-\Pi_q^A\). The normalized hidden
matrix cross-tail is

\[
 H_j[b,h](A)=\frac2{mn}\sum_a\int_0^A
       (Q_q^Ab_a^{(j)})(\xi)
       (Q_q^Ah_a^{(j-1)})(\xi)^\top\,d\xi.
\]

The dense histories decompose as

\[
 \begin{aligned}
 h_D(\xi)&=h_D(1)+\sum_{k=2}^4
        \frac{h_D^{(k)}(1+)}{k!}(\xi-1)_+^k+R_h(\xi),\\
 b_D(\xi)&=\sum_{k=1}^4
        \frac{b_D^{(k)}(1+)}{k!}(\xi-1)_+^k+R_b(\xi).
 \end{aligned}
\]

Both remainders and their derivatives through order four match at the
join. For \(x=2\xi/A-1\), the operator
\(\mathcal L=-\partial_x((1-x^2)\partial_x)\) has Legendre
eigenvalues \(j(j+1)\). Twice integrating by parts has zero outer
boundary terms and cancelling join terms. Parseval therefore gives
\(\|Q_q^AR\|_{L^2,\mathrm{RMS}}
 \le[q(q+1)]^{-2}\|\mathcal L^2R\|_{L^2,\mathrm{RMS}}
 \le C_T\ell_n^2q^{-4}\).
The bounded interval lengths and four derivative bounds justify the
last inequality uniformly in \(1\le A\le A_*\).

The assigned scalar input establishes
\(\|Q_q^A(\xi-1)_+^k\|_{L^2}\le C_kq^{-k-1/2}\) uniformly
down to \(A=1\). Its moment formula and differentiated Legendre
equation give the required endpoint-uniform estimates; no interior-only
asymptotic is being substituted. For \(u=(\xi-1)_+\), \(v=u^2\),
orthogonality and \(v'=2u\) give

\[
 \langle Q_q^Au,Q_q^Av\rangle
 =\frac14\bigl((Q_q^Av)(A)^2-(Q_q^Av)(0)^2\bigr)
 =I_q(A)I_{q-1}(A),
\]

where \(I_j(A)=\int_1^A(\xi-1)P_j(2\xi/A-1)\,d\xi\).
The uniform bound \(|I_j(A)|\le Cj^{-5/2}\) yields \(O(q^{-5})\).
Small orders are covered by a larger constant.

This is precisely the only jet pair for which multiplying tail norms
would lose a power. All other degree pairs have degree sum at least
four, hence cost at most \(q^{-5}\). Terms involving a remainder cost
at most \(q^{-11/2}\), from a ramp times a fourth-order remainder.
Sample Cauchy–Schwarz and the Frobenius norm of an outer product then give

\[
 \|Q_q^Ab_D\|_{L^2,\mathrm{RMS}}\le C_T\ell_n^2q^{-3/2},
 \quad
 \|Q_q^Ah_D\|_{L^2,\mathrm{RMS}}\le C_T\ell_n^2q^{-5/2},
 \quad
 \sum_{j=2}^L\|H_j[b_D,h_D](A)\|_F\le C_T\ell_n^4q^{-5}.
\]

## Transfer, stopping, and physical time

Compare \(\widehat\theta(A)\) and \(\theta_D(A)\) at the same
numerical value of their respective residual clocks. Let
\(\widehat t(A)\) and \(t_D(A)\) be their inverse-clock physical
times. On \(\widehat\rho\ge c_T/2\), both the ordinary clock
vector field \(-2J^*r/\rho\) and time derivative \(1/\rho\) have
dense-to-closure difference bounded by
\(C_T\sqrt{\ell_n}\|\widehat\theta-\theta_D\|\).

For this statement, forward subtraction costs a fixed constant.
Backward subtraction uses

\[
 \widehat\delta-\delta_D
 =\phi'(\widehat z)\odot(\widehat k-k_D)
  +[\phi'(\widehat z)-\phi'(z_D)]\odot k_D.
\]

The second term uses only the dense carrier maximum
\(C\sqrt{\ell_n}\); homogeneous propagation uses bounded operators.
The resulting logarithmic factor is additive across the fixed number of
layers, not multiplied once per layer. The normalized-residual map and
the reciprocal residual are Lipschitz on the indicated tube. In
particular, for the running maximum

\[
 E(A)=\sup_{1\le B\le A}
 \bigl(\|\widehat\theta(B)-\theta_D(B)\|
       +|\widehat t(B)-t_D(B)|\bigr),
\]

the history differences in \(L^2\), including their zero prefix
differences, obey \(\|\widehat h-h_D\|\le C_TE(A)\) and
\(\|\widehat b-b_D\|\le C_T\sqrt{\ell_n}E(A)\).
Projection contraction and bilinear expansion consequently give the
note's bound

\[
 \sum_j\|H_j[\widehat b,\widehat h]-H_j[b_D,h_D]\|_F
 \le C_T\ell_n^3\bigl(q^{-3/2}E(A)+E(A)^2\bigr).
\]

The exact moment reconstruction is the integral of the closure's own
ordinary clock vector field plus \(H_j[\widehat b,\widehat h](A)\)
in hidden block \(j\). Its sign and factor \(2/(mn)\) agree with
the paper's reconstruction. Orthogonality removes the mixed projected
terms. The first layer, readout, and physical-time coordinate have no
such defect. Thus the integral inequality for \(E\) follows without
differentiating \(H_j\), \(\widehat h\), or \(\widehat b\).

To make the bootstrap explicit, stop at
\(E=\eta\ell_n^{-3}\), the residual boundary, or \(A=A_*\),
with fixed sufficiently small \(\eta>0\). Choose \(q\) so that
\(C_T\ell_n^3q^{-3/2}\le1/4\) and choose \(\eta\) so that
\(C_T\ell_n^3E\le1/4\) before the stop. Absorption and the
integral Gronwall inequality give

\[
 E(A)\le C_T\ell_n^4
        \exp(C_T\sqrt{\ell_n})q^{-5}.
\]

Taking the threshold \(q\ge\exp(K_T\sqrt{\ell_n})\) with a
sufficiently large fixed \(K_T\) makes this strictly smaller than
\(\eta\ell_n^{-3}\) and than the fixed parameter discrepancy that
would allow \(\widehat\rho=c_T/2\). Both stops are excluded.
The already global physical solution cannot have a smaller limiting
clock value: on such a segment \(\widehat\rho\ge c_T/2\), so its
inverse-clock time has derivative at most \(2/c_T\) and cannot tend
to infinity at a finite clock endpoint. Finite-time continuation then
extends the clock segment to \(A_*\).

Finally \(|\widehat t(A_*)-(T+1)|<1/2\). Every closure time
\(t\in[0,T]\) therefore corresponds to a clock
\(A=\widehat\tau(t)\le A_*\). Bounded real operators and readouts
give a parameter-to-prediction Lipschitz bound uniform over
\(\|x\|=\sqrt d\). Dense prediction speed is uniformly bounded
on this sphere by the same gradient bounds and \(\rho_D\le Y\).
Consequently

\[
 \begin{aligned}
 |\widehat f(t,x)-f_D(t,x)|
 &\le|\widehat f(\widehat t(A),x)-f_D(t_D(A),x)|\\
 &\quad+|f_D(t_D(A),x)-f_D(t,x)|
 \le C_TE(A).
 \end{aligned}
\]

Absorbing \(\ell_n^4\) into the exponential proves the frozen
note's displayed estimate (1), with one enlarged constant in both its
bound and its order threshold.

For \(q=\lceil n^{1/10}\exp(\ell_n^{3/4})\rceil\), the ratio
of this bound to \(Y/(\sqrt n\ell_n^3)\) is at most
\(Y^{-1}\ell_n^3\exp(C_T\sqrt{\ell_n}-5\ell_n^{3/4})\),
which tends to zero for every fixed \(T\). The constants use
\(c_T^{-1}\), so the same argument gives no uniform all-time
estimate and does not justify replacing \(T\) by a width-dependent
horizon. The note correctly retains that limitation.
