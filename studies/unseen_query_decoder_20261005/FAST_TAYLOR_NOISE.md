# Stable noisy Taylor source with charged real activation values

2026-10-06. Scoped candidate proof for the current study. This note has
not received independent reconstruction or promotion. It establishes a
physical-source bridge, not a complete compact decoder or a fast unseen-query
algorithm. No experiment, new Gaussian source event, strengthened label
allowance, or Git operation is used.

The coefficientwise Taylor program can tolerate independent Gaussian noise in
both orientations of every initialized hidden-matrix action. Its matrix-noise
precision and its activation-value precision can both be bounded by

\[
 C\beta^{100L}(1+m/\gamma)Z
 \tag{1}
\]

bits, where the notation below is that of `SANE_TAYLOR_SOURCE.md`. The number
of initialized actions remains

\[
 R\le C\{d+mL\beta^{200L}(1+m/\gamma)^2Z^2\sqrt{\log(en)}\}.
 \tag{2}
\]

The physical perturbation proof does not propagate errors through the depth
of the entire arithmetic graph. It interprets all realized coefficientwise
answer errors as short analytic forcing polynomials and compares the
resulting local flows. Real-point interpolation supplies activation values,
first derivatives, and second derivatives on the necessary small complex
disk. The jets used in the Taylor recurrence are the derivatives of these
explicit interpolation polynomials. Their value evaluations are charged.

## 1. Contract and inherited bounds

The inputs read completely for this derivation are:

- `SANE_TAYLOR_SOURCE.md`, SHA-256
  `24b8d368da31e9d8bf00bb1c7fc85f75cb0efcc30a9cbc8409ac9c520bb916af`;
- `PHYSICAL_PARAMETER_ACCOUNTING.md`;
- `PHYSICAL_NOISY_PROGRAM_BRIDGE.md`;
- `NOISY_TWO_ORIENTATION_TRANSCRIPT.md`;
- the explicitly assigned
  `../integrated_general_compression_20261004/GENERAL_TRAJECTORY_LOWER_BRIDGE.md`.

No other study source or linked research history was retrieved. The required
research, rigorous-proof, canonical-notation, and neural-network convention
skills were read. The source theorem and its scientific event remain inherited
inputs; this note does not re-prove their Gaussian insertion argument.

For unit inputs \(v_a=x_a/\sqrt d\), the actual network is

\[
 z_a^{(1)}=Av_a,\qquad
 z_a^{(j)}=W^{(j)}h_a^{(j-1)},\qquad
 h_a^{(j)}=\phi_j(z_a^{(j)}),\qquad
 f_n(v_a)=w^Th_a^{(L)}/n.
 \tag{3}
\]

The residual is \(r_a=f_n(v_a)-y_a\). The loss is
\(m^{-1}\sum_a r_a^2\), the readout initially vanishes, and every layer
trains with the original mobilities. The residual-free backward variables are

\[
 k_a^{(L)}=w,\qquad
 \delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot k_a^{(j)},\qquad
 k_a^{(j)}=W^{(j+1)T}\delta_a^{(j+1)}.
 \tag{4}
\]

Thus the physical velocities are

\[
 \dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^T,
 \qquad
 \dot W^{(j)}=-\frac2{mn}\sum_a r_a\delta_a^{(j)}h_a^{(j-1)T},
 \qquad
 \dot w=-\frac2m\sum_a r_a h_a^{(L)}.
 \tag{5}
\]

Write

\[
 \lambda=\gamma/m,\quad r=\lambda^{-1},\quad
 Y=\|y\|_2/\sqrt m>0,\quad S=16Yr\le1,\quad
 \ell=\log(en),\quad B=\beta^{100L},
 \qquad
 Z=(a_0+1)\ell+\log(e+B(1+r)(m+d+2)).
 \tag{6}
\]

This enlarges the earlier Taylor source's logarithm by an explicit
input-size allowance; no sample-count or dimension logarithm is suppressed.
Here \(1\le a_0\le12\), and \(\beta\ge10\) is the source activation
envelope, including \(16/a\) and the first two half-strip derivative
bounds. The scalar \(r\) is not a sample residual. The case \(Y=0\) has
the exact zero predictor. Keep every inherited deterministic width gate,
including \(Y\ge n^{-1}\), and the explicit horizon gate in the Taylor
source. No additional label restriction is imposed.

For the learned displacement \(u\), use the physical norm

\[
 \|u\|=\|A-A_0\|_F/\sqrt n+
 \sum_{j=2}^L\|W^{(j)}-W_0^{(j)}\|_F+\|w\|_2/\sqrt n.
 \tag{7}
\]

Let \(\tau=\lambda t\), \(\bar u(\tau)=u(\tau/\lambda)/Y\), and
denote its holomorphic normalized vector field by \(\overline F\).
For a vector, \(\|v\|_{2,n}=\|v\|_2/\sqrt n\). Complex norms use
absolute values; the holomorphic formulas themselves use algebraic transpose.

The Taylor source supplies a horizon \(T<32\ell\), complex radius
\(r_\tau^{-1}\le B\sqrt\ell\), and a patch length

\[
 h=\min\{1/8,r_\tau/8,[64B(1+r)\sqrt\ell]^{-1}\}.
 \tag{8}
\]

Take \(H=\lceil T/h\rceil\) equal patches of length \(h_j=T/H\).
For finite arithmetic, obtain a certified rational upper bound on \(T/h\)
with excess at most \(1/4\), and take its ceiling instead. This requires
no exact test at an integer boundary. The resulting \(H\) exceeds the
mathematical ceiling by at most one and \(h/3\le h_j\le h\), since
the source's horizon satisfies \(T>h\). This partition avoids a tiny final
remainder. Every source disk and left-sum estimate uses only the upper
bound \(h_j\le h\), and is unchanged. The left endpoint is
\(\tau_j\). Put

\[
 q(\tau)=2^{-\lfloor\tau/4\rfloor},\quad q_j=q(\tau_j),\quad
 q_T=q(T),\quad
 d_n=\frac{\beta^{-200L}q_T}{(1+r)^2\sqrt n},
 \quad M=B(1+r),
 \quad \Lambda_j=B(1+r)(1+q_j\sqrt\ell),
 \quad E=B(1+r)(T+9\sqrt\ell).
 \tag{9}
\]

In the normalized-state tube of radius \(d_n\) about the reference
complex trajectory on each disk \(|\tau-\tau_j|<4h_j\), the true field
is holomorphic and \(\|D\overline F\|\le\Lambda_j\). The supplied
reference derivative is at most \(M\). Moreover

\[
 H\le CB(1+r)Z\sqrt\ell,\qquad
 \sum_jh_j\Lambda_j\le E\le CB(1+r)Z,\qquad
 4h_j\Lambda_j\le1/8.
 \tag{10}
\]

The source forward RMS, backward RMS, carrier maximum, and parameter-to-output
subtraction bounds hold on this tube, with the slack recorded in the Taylor
source. In particular prediction is \(B\)-Lipschitz in (7), uniformly over
real unit queries, and its normalized fitting tail after \(T\) is at most
\(n^{-a_0}/4\).

## 2. A local scalar disk follows from the existing response event

Set

\[
 \alpha=\min\{1,a/16\};\qquad \beta^{-1}\le\alpha\le1.
 \tag{11}
\]

An activation polynomial will be centered at a real, actually computed
preactivation \(x\). We need to control variation about this center, not
the possibly large value of \(x\) itself.

The finite-query source gives
\(\|R_a^{(j)}\|_\infty\le S U_{\rm fin}(S)\sqrt\ell\), with
\(U_{\rm fin}(S)\le\beta^{72L}\), throughout the relevant complex
source domain. Here
\(R_a^{(j)}=D_\Theta z^{(j)}\nabla_\Theta(nf_n(v_a))\), with
\(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\).
Equations (5) give exactly

\[
 \partial_\tau z^{(j)}
       =-\frac{2r}{m}\sum_a r_aR_a^{(j)}.
\]

The complex residual RMS is at most \(2Y\). Cauchy--Schwarz over the
sample index, followed by \(16Yr=S\), proves

\[
 \|\partial_\tau z^{(j)}\|_\infty
 \le4YrS U_{\rm fin}(S)\sqrt\ell
 =\tfrac14S^2U_{\rm fin}(S)\sqrt\ell.
 \tag{12}
\]

Consequently, on a radius-\(4h_j\) disk,

\[
 \|z^{(j)}(\tau_j+z)-z^{(j)}(\tau_j)\|_\infty
 \le h_jS^2U_{\rm fin}(S)\sqrt\ell
 \le\frac{\beta^{-28L}}{64(1+r)}<\frac\alpha{4096}.
 \tag{13}
\]

This is an existing complex response estimate, not a new coordinate maximum
event. A normalized parameter perturbation of size \(d_n\) changes any
preactivation coordinate by at most

\[
 \sqrt n\beta^{4L}Yd_n
 \le\beta^{-193L}<\alpha/4096,
 \tag{14}
\]

using the inherited \(Y\le\beta^{3L}\). Below, a forward computational
defect will contribute less than another \(\alpha/4096\). Thus both
the computed center and all local evaluations stay within
\(|z-x|<\alpha/64\), with ample margin inside \(\alpha/4\).
The estimate also covers very wide analytic strips: it does not introduce
an upper bound on \(a\) or a cost proportional to \(a\).

## 3. Real value samples give stable finite jets

Fix a real center \(x\), integer \(J\ge2\), and equally spaced rational
nodes

\[
 t_i=-1+\frac{2i}{J-1},\qquad 0\le i<J.
\]

Let \(p_x(w)\) be the degree-at-most-\(J-1\) polynomial interpolating
values \(v_i\) that satisfy

\[
 |v_i-\phi(x+\alpha t_i)|\le\nu.
 \tag{15}
\]

Define the physical polynomial activation
\(\psi_x(z)=p_x((z-x)/\alpha)\). For a fixed center and fixed samples
it is entire, even when the sample evaluator itself is not analytic.

For \(|w|\le1/2\), the interpolation error with exact samples is bounded
by \(C\beta\alpha2^{-J}\). Here is a direct proof. Subtract the constant
\(\phi(x)\), which interpolation reproduces exactly, and write
\(g(w)=\phi(x+\alpha w)-\phi(x)\). On \(|s|=4\), the line segment
from zero to \(s\) lies inside the half-strip after rescaling, and hence
\(|g(s)|\le4\beta\alpha\). With
\(\omega(w)=\prod_i(w-t_i)\), the residue formula gives

\[
 g(w)-I_Jg(w)=\frac1{2\pi i}\int_{|s|=4}
       \frac{g(s)\omega(w)}{\omega(s)(s-w)}\,ds.
\]

Its residues are \(g(w)\) at \(s=w\) and the negatives of the
Lagrange summands at the nodes. On the stated disks,
\(|\omega(w)|\le(3/2)^J\), \(|\omega(s)|\ge3^J\), and
\(|s-w|\ge7/2\), proving the estimate.

The interpolation effect of the sample errors is at most \(5^J\nu\)
on the same disk. Indeed the absolute sum of the Lagrange polynomials is
bounded by

\[
 \sum_i\frac{(3/2)^{J-1}}
 {(2/(J-1))^{J-1}i!(J-1-i)!}
 =\frac{[3(J-1)/2]^{J-1}}{(J-1)!}
 \le(3e/2)^{J-1}\le5^J.
\]

The factorial bound follows by summing \(\log k\) above its integral.
Apply Cauchy's derivative formula on a radius-\(1/4\) circle about
each \(|w|\le1/4\) point. Rescaling derivatives by \(\alpha^{-1}\)
and \(\alpha^{-2}\) gives

\[
 \max_{s=0,1,2}\sup_{|z-x|\le\alpha/4}
       |\psi_x^{(s)}(z)-\phi^{(s)}(z)|
 \le C\beta^2\{2^{-J}+5^J\nu\}.
 \tag{16}
\]

Thus an absolute error target \(0<\delta<1\) is achieved by

\[
 J\ge\max\{K+2,\lceil\log_2(C\beta^2/\delta)\rceil\},
 \qquad
 \nu\le\frac{\delta}{C\beta^2 5^J},
 \tag{17}
\]

with an enlarged numerical \(C\). Unlike finite differences with vanishing
spacing, this requires \(O(J+\log\delta^{-1}+\log\beta)\) value bits.
There are \(J\) real sample requests per scalar center. Interpolation
coefficients and the required normalized jets can be formed by elementary
polynomial products and sums with at most \(O(J^3)\) scalar arithmetic
and \(O(J^2)\) scratch; no fast interpolation theorem is needed.

Only the first \(K+1\) Taylor coefficients of \(\psi_x\), and the
corresponding coefficients of \(\psi_x'\), are needed. These coefficients
are used exactly in the usual truncated-series composition. The omitted
polynomial powers have zero contribution through the relevant time degree.

### 3.1 A continuous value interface, if row regularity is needed

An arbitrary finite-precision value routine can jump as its argument changes.
A uniform error guarantee alone does not prove a Lipschitz row function.
There is a simple explicit repair that costs two routine calls per sample.

Take a real mesh spacing \(\Delta=\nu/(8\beta)\). At each mesh point
\(k\Delta\), define one deterministic routine output with error at most
\(\nu/8\). Interpolate linearly between successive outputs. This defines
a globally continuous real function \(A_\phi\) satisfying

\[
 |A_\phi(x)-\phi(x)|\le\nu/4,\qquad
 \operatorname{Lip}(A_\phi)\le3\beta.
 \tag{18}
\]

The first estimate is the triangle inequality using the derivative bound.
For the second, the difference of consecutive knot values is at most
\(\beta\Delta+\nu/4=3\beta\Delta\). Repeated requests at the same
knot use the same deterministic rule. A table over the real line is not
stored: only the two required knot values are evaluated on demand.
The integer mesh index and input-argument precision are charged. On the
source range their lengths are
\(O(\log(en)+\log\nu^{-1}+\log\beta+\log(1+r))\).

Use \(A_\phi(x+\alpha t_i)\) for the samples in (15). Equations
(16)--(17) still hold. As a function of its real center, every interpolation
coefficient is now Lipschitz, with a bound exponential in \(CJ\) times
the displayed polynomial scales. This assertion uses (18) and the explicit
linear interpolation weights; it does not differentiate a discontinuous
rounded activation routine. Subsequent finite arithmetic approximates these
specified continuous functions. The exact row-law model uses those functions.

The actual work of a value routine at the requested precision is an external
cost interface. Analyticity alone does not bound it. Denote its worst-case
work on the displayed input range by \(\mathcal V_\phi(b)\), retaining
the argument-encoding cost as well. The source uses at most
\(2nmLH(J+1)\) such scalar calls when (18) is used, or
\(nmLH(J+1)\) direct
calls if a suitable continuous value interface is already supplied.
The extra sample permits the centered value in (36) even when zero is
not one of the interpolation nodes.

## 4. Freeze coefficient errors into analytic forcing

Use \(\xi=(\tau-\tau_j)/h_j\). At each initialized hidden-matrix
action of order \(k\), return

\[
 W_0v[k]+\sigma\zeta_k
 \quad\hbox{or}\quad W_0^Tu[k]+\sigma\zeta_k,
 \qquad \zeta_k\sim N(0,I_n),
 \tag{19}
\]

with fresh independent noises. The raw noises are hidden from the observable
program. For each sample, layer, and orientation in one patch, freeze their
realized values and define

\[
 N(\xi)=\sigma\sum_{k=0}^{K-1}\zeta_k\xi^k.
 \tag{20}
\]

On the event \(\|\zeta_k\|_{2,n}\le2\) for every call,

\[
 \sup_{|\xi|\le4}\|N(\xi)\|_{2,n}\le\sigma4^K,
 \qquad
 \sup_{|\xi|\le4}\|N(\xi)\|_\infty\le\sqrt n\sigma4^K.
 \tag{21}
\]

This polynomial is a proof device. The running program never observes or
evaluates it. Its order-\(k\) coefficient is acquired only when that action
is actually called.

At order zero, evaluate the forward pass in layer order. At each coordinate,
first compute its noisy preactivation center \(x\), then construct
\(\psi_x\) by Section 3 and use it for the activation. Its derivative is
used in the backward pass. Retain this polynomial during the patch. There
is no implicit definition of a center: all preceding layer values and the
current order-zero observed answer are already available.

For a fixed realized patch, define a holomorphic nonautonomous field by
replacing each initialized action in the forward/backward formulas by that
action plus (20), and replacing its corresponding activation and gate by
\(\psi_x\) and \(\psi_x'\). Keep the same parameters, residual,
gradient factors, normalizations, and learned-matrix actions in (3)--(5).
Call the resulting normalized field \(\overline F_j^{\rm num}(\xi,U)\).
The centers and polynomial coefficients are constants in this definition.

Suppose (16) and the RMS bound in (21) are at most \(\delta\), and

\[
 \delta\le
 \delta_0:=\frac{\beta^{-150L}S q_T}{(1+r)^2\sqrt n}.
 \tag{22}
\]

On the tube from Section 1, the following bounds then hold:

\[
 \|\overline F_j^{\rm num}(\xi,U)-\overline F(U)\|
       \le C_N\delta,
 \qquad
 \|D_U\overline F_j^{\rm num}(\xi,U)\|\le2\Lambda_j,
 \qquad
 C_N=B^2(1+r)^2\sqrt\ell.
 \tag{23}
\]

Here and below numerical constants are absorbed by the large exponent slack
between the source subtraction recurrences and \(B^2\). The following
details specify the subtraction, including the small-label issue.

Forward subtraction uses the operator cap eleven, the bounded activation
derivative, an error \(\delta\) in each activation, and an error
\(\delta\) in each initialized action. Its RMS error is at most
\(\beta^{4L}\delta\). The coordinate error is at most
\(\sqrt n\beta^{4L}\delta\). Equations (13)--(14), (22), and a
first-exit argument therefore keep every activation argument in the disk
required by (16). Thus those estimates are not assumed outside their domain.

In backward subtraction, split the gate difference as

\[
 (\psi_x'(\widetilde z)-\phi'(z))\odot k
       +\psi_x'(\widetilde z)\odot(\widetilde k-k).
\]

The first term contains one *reference* carrier maximum
\(C\beta^{40L}S\sqrt\ell\). Propagating the matrix and gate
differences down the fixed layer chain gives an RMS error at most
\(\beta^{60L}(1+S\sqrt\ell)\delta\). There is one carrier-maximum
factor in this bound, not its \(L\)th power. Equation (22) also keeps
the perturbed carrier coordinate maximum within a fixed factor of the
reference cap. The readout RMS is at most \(C\beta^{3L}S\), so the
residual change is at most \(\beta^{10L}S\delta\). Since
\(S/Y=16r\), (22) makes this less than \(Yq_T\); the perturbed
residual therefore retains a bound \(C Yq_j\).

Subtract each gradient product in its residual, backward, and forward
factors. Before time and amplitude normalization, this gives

\[
 \|F_j^{\rm num}-F\|
 \le C\beta^{80L}[Y(1+S\sqrt\ell)+S+S^2]\delta.
\]

Multiply by \(r/Y\), use \(S\le1\) and \(S/Y=16r\), and obtain
the first bound in (23). Thus no inverse power of \(Y\) appears in the
field amplification. For the second bound, differentiate the same finite
forward/backward and gradient recursions with respect to the physical
parameters. The first two derivatives of \(\psi_x\) are at most
\(\beta+\delta\); noise polynomials and centers are fixed. The carrier
and residual caps just proved give precisely the subtraction pattern in
the Taylor source's (11)--(15), with fixed-factor larger caps. The unused
powers between \(\beta^{70L}\) and \(B\) absorb those factors, giving
\(2\Lambda_j\). No derivative with respect to the center is taken in
this physical local-flow comparison.

## 5. Holomorphic perturbed flow and stable endpoint comparison

Let \(a=\bar u(\tau_j)\) and let \(b\) be the computed real anchor,
with \(e_j=\|b-a\|\le d_n/8\). Write \(X_a(z)\) for the exact
reference solution in local normalized time. Set
\(\eta=C_N\delta\). If \(4h_j\eta\le d_n/16\), the equation

\[
 D(z)=b-a+\int_0^z
 [\overline F_j^{\rm num}(s/h_j,X_a(s)+D(s))
                         -\overline F(X_a(s))],ds
 \tag{24}
\]

is a contraction on holomorphic functions with \(\sup\|D\|\le d_n/2\)
on every closed disk of radius less than \(4h_j\). Its contraction
factor is at most \(8h_j\Lambda_j\le1/4\), and its image norm is
at most \(d_n/8+d_n/16+d_n/8<d_n/2\). Uniform convergence of its
iterates gives a holomorphic solution. Nested disks agree by uniqueness.

Subtracting the exact field first and then using (23), radial integration
and the scalar integral Gronwall inequality give

\[
 \|D(z)\|\le(e_j+|z|\eta)e^{\Lambda_j|z|}
              \le2e_j+8h_j\eta.
 \tag{25}
\]

The actual noisy recurrence computes exactly the first \(K+1\) Taylor
coefficients of \(X_a+D\), in the dimensionless variable \(\xi\).
To verify this, at order \(k\) every forward coefficient, backward
coefficient, residual coefficient, and gradient coefficient is obtained by
formal multiplication and composition of already known state coefficients.
Adding the order-\(k\) answer noise is exactly adding \([\xi^k]N\).
Dividing the resulting velocity coefficient by \(k+1\), and multiplying
by \(h_j\), is the Taylor coefficient identity for (24). Induction over
orders, and within an order over the forward/backward layer order, proves
the assertion. Future coefficients of (20) never enter an earlier order.

On \(|z|=2h_j\), (25) and Cauchy's formula bound the tail of the
difference series at every \(0\le s\le h_j\) by
\((2e_j+8h_j\eta)2^{-K}\). The exact source tail is at most
\(2Mh_j2^{-K}\). If \(K\ge4\), the committed endpoint therefore
satisfies

\[
 e_{j+1}\le(1+2h_j\Lambda_j+2\,2^{-K})e_j
                  +3h_j\eta+2Mh_j2^{-K}.
 \tag{26}
\]

The same bound, with the exact-flow factor at the requested local time,
controls each interior polynomial value. In particular there is no constant
factor larger than one raised to the number of patches.

Choose

\[
 \varepsilon=\min\{d_n/128,n^{-a_0}/(128B)\},
\]
\[
 K=8+\left\lceil
 \frac{4E+\log[2^{20}(M+1)(T+1)/\varepsilon]
                  +\log(1+16H)}{\log2}\right\rceil,
 \tag{27}
\]
\[
 \delta=\min\left\{\delta_0,
 \frac{\varepsilon e^{-4E-10}}{2^{20}C_N(T+1)}\right\},
 \qquad
 \sigma=2^{-b_\sigma},\quad
 b_\sigma=\left\lceil2K+\log_2(4/\delta)\right\rceil.
 \tag{28}
\]

Iterating (26) bounds its products by
\(\exp(2E+2H2^{-K})\le e^{2E+1}\). The total forcing sum is
at most \(3T\eta+2MT2^{-K}\). The corresponding interior bound is
at most a fixed factor larger. Equations (27)--(28) consequently give

\[
 \sup_{0\le\tau\le T}
       \|\widetilde u(\tau)-\bar u(\tau)\|<\varepsilon/8.
 \tag{29}
\]

This closes every anchor and tube bootstrap in (24). It also gives strict
slack for a separately allocated arithmetic-error budget. By (21), the
choice of \(\sigma\) pays for every analytic forcing polynomial.

The logarithmic bounds are explicit. From \(Y\ge n^{-1}\) and
\(r^{-1}\le\beta^{6L}\),
\(S=16Yr\ge16\beta^{-6L}/n\). Hence

\[
 \log(\delta_0^{-1})\le CZ,\qquad
 \log(\varepsilon^{-1})\le CZ,
\]
\[
 K+\log(\delta^{-1})+b_\sigma
        \le CB(1+r)Z.
 \tag{30}
\]

The least \(J\) and value precision satisfying (17) obey the same bound.
Thus (1) is a parameter-explicit logarithmic-width bound. No numerical
conditioning cost has been hidden in a sufficient-width qualification.

The physical parameter error is \(Y\) times (29). Uniform prediction
subtraction contributes \(B\), and freezing the numerical parameter state
at \(T\) adds the inherited fitting tail. Therefore the parameter-defined
predictor has normalized all-time, whole-sphere error less than
\(n^{-a_0}\), including the fitted endpoint. This is an approximation to
the dense predictor, not an assertion of exact fitting by the noisy program.
Smaller passive-source or parameter tolerances can replace the second term
in \(\varepsilon\); only their logarithms are added to (27)--(30).

## 6. Arithmetic implementation and source-law compatibility

The precise theorem above treats coefficient arithmetic as exact and charges
finite activation-value errors. It already closes the matrix-noise and
activation-jet interface missing from the earlier Taylor source. A finite
arithmetic implementation need not use the depth of the entire training
graph to choose its precision. The following local implementation makes the
additional requirement explicit.

For one principal coefficient output, compute the required finite convolution,
inner product, or polynomial composition with certified absolute output
error at most \(\rho\), allocating errors inside that local computation.
For a vector output this is a maximum-coordinate tolerance; for a normalized
empirical average it is a scalar tolerance. Form each activation polynomial
in its centered variable \((z-x)/\alpha\); do not expand powers of the
large center \(x\). Its interpolation weights and all their partial
products have size at most \(e^{CJ}\): factors with inverse node distance
larger than one have product bounded by the same factorial argument as in
Section 3. Polynomial-product coefficient sums add only another \(e^{CJ}\).

On the good local disks, the centered preactivation series has coefficient
\(\ell^1\)-norm below \(1/8\) on \(|\xi|\le1\). To check this,
its constant is exactly zero and its supremum on \(|\xi|\le4\) is
less than \(1/64\), by Section 2 and the forward bound following (23).
Cauchy's coefficient estimate and \(\sum_{k\ge1}4^{-k}=1/3\) give
the stated strict inequality. Truncated convolution is submultiplicative
in coefficient \(\ell^1\)-norm. Thus powers and compositions have local
rounding amplification bounded by \(e^{CJ}\) times a polynomial in
\(K,J\), the operand ranges, and the number of terms. They do not acquire
one instability factor for every earlier patch.

Learned-matrix products use rank-one factors and normalized pairings as in
the Taylor source. Their number of summands is polynomial in \(R,K\).
Their operand bounds are supplied by (25), Cauchy's coefficient estimates,
and the initialized operator caps. They are at most polynomial in
\(n,B,1+r,R\), with an extra \(e^{CJ}\) only for interpolation scratch.
Ordinary summation and product subtraction therefore give a local working
precision

\[
 b_{\rm work}\le C\{J+K+\log(\rho^{-1})+
   \log(en)+\log(e+R+m+L+d)+\log B+\log(1+r)\}
 \tag{31}
\]

plus the supplied encodings of data and activation constants. This follows
from the displayed product/sum formulas: their number is polynomial, their
arity is bounded, and the only potentially long multiplication chains have
the explicit \(e^{CJ}\) bound above. It is not a claim that a black-box
value evaluator has this work complexity.

Choose
\[
 \rho\le\frac{\delta}
 {C4^K(n+1)^3[B(1+r)(R+K+1)]^C},
 \tag{31a}
\]
with a sufficiently large absolute exponent to cover the rank-factor and
normalization operations. The displayed factor \((n+1)^3\) covers even
the conservative conversions from coordinate errors to the block norm,
including normalization by \(Y\ge n^{-1}\). Its precision cost is
only \(O(\ell)\). Also \(h_j^{-1}\le C B(1+r)\sqrt\ell\).
Rounding an integrated coefficient is represented by its corresponding
velocity-coefficient error, without an uncharged inverse final-step length.
Independent endpoint rounding is instead an additive endpoint defect in
(26). Choose its block norm at most \(h_j\eta\); this only changes the
numerical coefficient of \(h_j\eta\) in that recurrence. It is not
identified with a constant forcing that preserves the same computed polynomial.
Represent each realized principal coefficient error as another polynomial,
just as in (20). The errors in forward or backward algebra are added at
their respective nodes; errors in gradient integration or its stored scalar
weights are added as parameter-velocity forcing. The physical block-norm
conversion and the number of summands are covered by the displayed factors.
Their total analytic defect is then at most the unused fraction of
\(C_N\delta\). Applying (24)--(29) with a fixed larger defect constant
preserves the conclusion. Equation (31) still has the bound in (1), apart
from the logarithmic input-description term. Rounding a query before its
matrix action is covered by the initialized operator cap. A rounded stored
answer is a deterministic postprocessing of its noisy observed answer.

This arithmetic paragraph concerns approximation of a specified continuous
row program. It does not assert that literal finite-precision rounding is
itself globally Lipschitz. The row regularity statement is for the continuous
extension in (18), with explicit caps; finite computation approximates it.

### 6.1 Chronology and exact Gaussian law

The next initialized-matrix label, orientation, and coefficient query are
functions only of the external first-layer Gaussian columns, deterministic
inputs, and previously observed answers. Scalar value evaluations and
coefficient arithmetic are deterministic functions of this same information.
The raw noise in (19) is never supplied separately. Thus the exact
two-orientation posterior theorem applies without any modification.

The artificial polynomial forcing used in the proof changes none of these
filtration facts. Its later coefficients are not used to choose an earlier
query. No new history-Gram gap or independence conditional on a complete
dense matrix tape is asserted.

There are \(O(mLHK)\) initialized calls and principal row fields. Since
\(J=O(K)\), retaining scalar sample or jet outputs as named row fields,
if convenient, only changes the numerical constant in this count. Temporary
scalar products inside interpolation or series composition are charged as
row-local work and scratch; they need no new empirical average. The learned
rank representation still has \(O(mLHK^2)\) scalar weights. Substitution of
(10), (30) gives (2). The activation calls, polynomial work, coefficient
storage, and later query computations are separate costs; (2) is not their
total.

### 6.2 Row and scalar caps agree on the good program

From the local holomorphic solution and Cauchy on \(|\xi|=2\), principal
forward/backward coefficient vectors have RMS at most a fixed polynomial in
\(B,1+r\). An initialized observed answer has the same type of RMS bound
by its operator cap and the event in (21). Its coordinate maximum can be
\(\sqrt n\) times this bound. No polylogarithmic maximum for every raw
answer is needed or claimed.

Let \(B_{\rm phys}\) be a sufficiently large fixed polynomial in
\(B,1+r\) dominating these RMS bounds. The noisy posterior formulas give
one-call mean and square-root coefficients polynomial in
\(R,B_{\rm phys},\sigma^{-1}\). On the original physical coupling,
the whitened innovation therefore satisfies

\[
 \|g\|_{2,n}\le
       [C(1+R)(1+B_{\rm phys})(1+\sigma^{-1})]^C=:G_*.
 \tag{32}
\]

This follows by multiplying the observed-answer-minus-posterior-mean bound
by \(\|\Gamma^{-1/2}\|\le\sigma^{-1}\), using the one-call formulas.
It is not an iterated inverse-Gram bound. Innovation coordinates may be
\(\sqrt nG_*\), and their cross-moments and second moments must use
caps \(B_{\rm phys}G_*\) and \(G_*^2\), respectively.

Choose coordinate and moment caps strictly above these certified bounds.
The PSD-Gram extension from the transcript then retains its explicit inverse
and square-root gaps. Interpolation scratch, centered powers, and scalar
rank-factor sums admit caps whose logarithms are bounded by a polynomial in
\(R,K,J,\ell,\log B,\log(1+r),b_\sigma\), using their explicit finite
formulas. These caps are the identity on the good program. Off that range,
they specify a bounded extension. Combining (18) with capped arithmetic and
the gapped posterior operations gives Lipschitz row functions. Their global
Lipschitz constants may be exponentially large in a polynomial of these
arguments; this note does not turn that statement into a low-degree bound
for a later expectation evaluator or scalar-summary compiler.

Each fresh Gaussian has RMS at most two except with probability
\(e^{-cn}\), by exponential Markov applied to its squared norm. A union
over all calls costs at most \(Re^{-cn}\), separately from the inherited
source/fitting failure. All deterministic estimates above hold simultaneously
on this intersection. A later forward query can use the same direct physical
subtraction argument with fresh raw noise. An efficient retained-state
implementation of all such queries remains outside this note.

## 7. Claim status and adversarial checks

| Claim | Status and scope |
|---|---|
| Existing Taylor call chronology with Gaussian answers | Candidate proof: (19)--(30), on the inherited source event and the explicit raw-noise RMS event |
| Activation jets from finitely many real values | Constructive: (15)--(18), with value work and argument precision charged |
| Polynomial parameter dependence and logarithmic width precision | Candidate bound (30), inherited scientific width gates unchanged |
| Exact two-orientation row-law applicability | The observable chronology meets the supplied theorem's hypotheses |
| Good-program caps and continuous row functions | Explicitly supplied in Sections 3.1 and 6.2 |
| Full compact storage, scalar-summary precision, fast unseen queries | Open here; neither (1) nor (2) proves these claims |

The main objections addressed are: a large real preactivation center (use a
centered scalar disk and (12)); loss of the original label range (use the
full \(U_{\rm fin}\) bound, not its small-label specialization); future
noise leakage (formal forcing is proof-only); nonlinear activation error
outside its interpolation disk (first-exit and thin-tube bounds); a constant
error multiplier per patch (use (26)); discontinuous value evaluators (use
(18)); and an unjustified small innovation cap (use (32)).

The argument upgrades the stable physical noisy-Taylor interface left open
by the source note. It does not upgrade the original unquantified stochastic
width threshold, the storage bound of an entire decoder, or the runtime of
a late unseen query. Independent reconstruction should in particular audit
the local forcing identification, the scaling in (23), and the rounded
rank-factor implementation described after (31).

## 8. Causal coefficient caps and per-operation compiler bounds

This section is an additional deterministic compiler interface. It does not
alter the physical-source proof in Sections 1--7. It proves a small
logarithmic bound for each specified local operation; it does not assert that
the entire expanded training history has the same Lipschitz constant.

### 8.1 A causal coefficient budget is Lipschitz

For a real sequence \(a=(a_1,\ldots,a_K)\) and a budget \(c>0\), define
\(P_c(a)\) sequentially by

\[
 b_k=\operatorname{clip}\left(a_k,
 -\left(c-\sum_{p<k}|b_p|\right)_+,
  \left(c-\sum_{p<k}|b_p|\right)_+\right),
 \qquad P_c(a)=(b_1,\ldots,b_K).
 \tag{33}
\]

The first \(k\) outputs use only the first \(k\) inputs. It is the
identity whenever \(\sum_k|a_k|\le c\), and always has
\(\sum_k|b_k|\le c\). It also satisfies the dimension-independent bound

\[
 \|P_c(a)-P_c(\widetilde a)\|_1
                 \le2\|a-\widetilde a\|_1.
 \tag{34}
\]

To prove (34), if neither sequence saturates its budget the map is the
identity. Otherwise let \(p\) be the first saturation index of either
sequence, and suppose the first sequence saturates there. Before \(p\)
both outputs equal their inputs. Put

\[
 D=\sum_{k<p}|a_k-\widetilde a_k|,\quad
 A=c-\sum_{k<p}|a_k|,\quad
 B=c-\sum_{k<p}|\widetilde a_k|.
\]

Then \(|A-B|\le D\), \(|a_p|\ge A\), and the first output has no
tail after \(p\). Write \(v=\min\{|\widetilde a_p|,B\}\). The other
output's remaining tail has total modulus at most \(B-v\). Splitting
the two signs and the cases \(v\le A\), \(v>A\) gives

\[
 |\operatorname{sgn}(a_p)A-
             \operatorname{sgn}(\widetilde a_p)v|+B-v
       \le2|a_p-\widetilde a_p|+|A-B|.
\]

For equal signs and \(v\le A\), the left side is \(A+B-2v\): if
\(v=|\widetilde a_p|\), use \(|a_p|\ge A\); if \(v=B\), it is
\(A-B\). For equal signs and \(v>A\), it is \(B-A\). For opposite
signs it is \(A+B\), while
\(|a_p-\widetilde a_p|\ge A\). These checks prove the displayed
inequality in every case, including a zero entry by continuity. Adding the
prefix error \(D\) proves (34).

At one neuron and activation center \(x=z[0]\), submit the positive-order
dimensionless preactivation coefficients
\(a_k=z[k]/\alpha\) to \(P_{1/8}\), and use

\[
 v(\xi)=\sum_{k=1}^K [P_{1/8}(a)]_k\xi^k
 \tag{35}
\]

in the activation and gate compositions. The zero coefficient is kept as
the center. The good-program centered series has supremum below \(1/64\)
on \(|\xi|\le4\), by Section 2 and the forward comparison. Its positive
coefficients therefore have total modulus below
\((1/64)\sum_{k\ge1}4^{-k}<1/64\). Hence (33) is the identity on
the good program, including the already allocated arithmetic slack.
An earliest-differing-instruction argument proves agreement of the capped
and original programs: the first supposedly active cap would see the
original good sequence, on which no cap is active. Off that event, the
finite capped program is explicitly defined and still predictable.

### 8.2 Centered composition avoids a power of the coordinate cap

Implement the interpolation polynomial in the form

\[
 p_x(w)=A_\phi(x)+
       \sum_i [A_\phi(x+\alpha t_i)-A_\phi(x)]\,l_i(w),
 \tag{36}
\]

where the \(l_i\) are the Lagrange polynomials. Since \(A_\phi\) is
\(3\beta\)-Lipschitz, every bracket has modulus at most
\(3\beta\alpha\). The large real center contributes only to the single
constant \(A_\phi(x)\). Each coefficient of every \(l_i\), and the
sum of their absolute coefficients, is at most \(e^{CJ}\). This follows
from expanding their \(J-1\) factors (coefficient sum at most \(2^{J-1}\))
and using the factorial bound for their denominators from Section 3.
Thus interpolation scratch has size \(e^{CJ}\operatorname{poly}(\beta,J)\),
apart from the separately stored constant value. A coordinate bound
\(C\sqrt n B_{\rm phys}\) is never raised to power \(J\).

For a truncated series \(v\), write
\(\|v\|_1=\sum_{k=0}^K|v[k]|\). Truncated convolution obeys
\(\|uv\|_1\le\|u\|_1\|v\|_1\). If
\(\|v\|_1,\|\widetilde v\|_1\le1/8\), then

\[
 \|v^q-\widetilde v^q\|_1
       \le q(1/8)^{q-1}\|v-\widetilde v\|_1,
 \tag{37}
\]

by telescoping the product into \(q\) terms. The centered scalar
polynomial \(p_x(w)-\phi(x)\) is bounded by \(C\beta\alpha\) on
\(|w|\le1/2\), as in the proof of (16). Consequently its coefficient
of degree \(q\ge1\) has magnitude at most
\(C\beta\alpha2^q\). Substitution in (37) shows that the complete
activation coefficient sequence depends Lipschitz-continuously on \(v\),
with constant \(C\beta\alpha\). The gate sequence
\(p_x'(v)/\alpha\) has a bound of the same kind with a polynomial in
\(\beta,\alpha^{-1}\), obtained by differentiating this coefficient
bound once more. These are geometric sums since \(2/8<1\).

Dependence on the center also has an explicit bound. Every value in the
brackets of (36) changes by at most \(6\beta|x-\widetilde x|\). The
sum of the absolute interpolation coefficients is at most \(e^{CJ}\),
and differentiation of the polynomial adds only a factor polynomial in
\(J,\alpha^{-1}\). Equations (34), (36)--(37) therefore give a joint
Lipschitz bound for the local activation/gate coefficient operation of

\[
 L_{\rm act}\le
     e^{CJ}\operatorname{poly}(K,J,\beta),
 \qquad \log L_{\rm act}\le C(J+\log(e+K)+\log\beta).
 \tag{38}
\]

Here the raw positive-order coefficients use (34) and
\(\alpha^{-1}\le\beta\). Converting between coefficient maximum norm
and coefficient \(\ell^1\)-norm costs only \(K\), already included
in (38). This bound holds on the entire capped domain. It does not depend
on an accidental cancellation of large raw coefficients.

### 8.3 What the resulting compiler bound does and does not state

Treat previous principal row fields and scalar summaries as the inputs of
one local operation. Learned-matrix action, gradient, residual, and empirical
pairing operations are fixed-degree sums and products of their bounded
operands. A sum has at most polynomially many terms in \(R,K\). Their
local Lipschitz constants are polynomial in the row/scalar caps and those
term counts. The explicitly gapped one-call Gaussian posterior operations
have the corresponding polynomial bounds in
\(R,B_{\rm phys},G_*,\sigma^{-1}\). Use (36) for interpolation and
(35) for every activation/gate composition. For these local operations,
one may therefore choose a common bound \(\chi_{\rm local}\) for the
logarithms of operand amplitudes and Lipschitz constants satisfying

\[
 \chi_{\rm local}\le C\{J+\ell+b_\sigma+
                  \log(e+R)+\log B+\log(1+r)\}
          \le CB(1+r)Z.
 \tag{39}
\]

The \(\ell\) term pays once for a raw coordinate cap, while the
\(J\) term pays for interpolation coefficients. Their product is absent.
This replaces the looser off-domain implementation that expands powers of
an uncentered, \(\sqrt n\)-sized variable.

The charged activation arithmetic also fits a useful quadratic envelope.
Let \(N=mLH\). Computing and caching successive power coefficients uses
\(O(JK^2)\) arithmetic, and interpolation uses \(O(J^3)\), per neuron,
sample, layer, and patch. Because \(J\le CK\), the per-row total is
\(O(NK^3)\). The chosen parameters give \(K\le CH\le CN\):
indeed \(H\ge64B(1+r)T\sqrt\ell\), \(T,\sqrt\ell\ge1\), and
all terms defining \(K\) in (27) are bounded by a fixed multiple of
this expression. Since \(R\) may be chosen to dominate \(NK\),

\[
 mLH K^3=NK^3\le C(NK)^2\le CR^2.
 \tag{40}
\]

This counts local scalar activation arithmetic per row. It excludes the
charged activation-value work \(\mathcal V_\phi\), arithmetic bit cost,
and the small-matrix posterior routines; it is not a total decoder-work
bound.

Finally, (39) is an operation-level bound. An entire row function obtained
by recursively substituting many previous row operations can still have
a Lipschitz constant equal to a product of their constants. In particular,
these estimates alone do not replace a possible \(R\chi_{\rm local}\)
history sensitivity by \(\chi_{\rm local}\). A downstream compiler that
takes bounded local operations as its input may use (39)--(40). A theorem
requiring an already-expanded row function with a global history Lipschitz
bound must prove the extra stability step separately.
