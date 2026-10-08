# Adaptive temporal approximation: proved interfaces and missing domains

2026-10-08. Bounded theoretical route. This document proves deterministic
approximation statements and their rank/storage consequences. It does not
prove a stronger complex-time source event for the neural flow.

The existing fixed-strip hypotheses reproduce the sufficient
\([\log(en)]^{5/2}\) source rank and \([\log(en)]^5\) retained storage. A variable-radius
panel construction would improve these counts if a correspondingly larger
complex domain were proved. A fixed analytic neighborhood in an exponential
clock is sufficient for \([\log(en)]^2\) storage, but real loss decay does not
establish that neighborhood. Even a sum of two elementary decaying modes
can fail endpoint analyticity in that clock.

## 1. Contract and source objects

Use the notation of `PANEL_BOUND.md`: there are \(m\) training inputs and
\(p\) additional passive inputs, all fixed at initialization. Write

\[
\lambda=\gamma/m>0,\qquad Y=\|y\|_2/\sqrt m>0,
\qquad z=Y/\lambda,\qquad S=16z,\qquad \ell=\log(en).
\]

The dense model has normalized inputs \(v_i=x_i/\sqrt d\), forward pass
\(z_i^{(1)}=Av_i\), \(z_i^{(j)}=W^{(j)}h_i^{(j-1)}\),
\(h_i^{(j)}=\phi_j(z_i^{(j)})\), output \(f_n=w^\top h^{(L)}/n\), residual
\(r_a=f_n(v_a)-y_a\), and loss \(m^{-1}\sum_a r_a^2\). Its mobilities,
Gaussian initialization, zero initial readout, and full inherited label
allowance are those in `PANEL_BOUND.md` (2)--(3). No new cap on \(z\) is used.

At layer \(j\), the required real vector curves are

\[
h^{(j)}(t,v_i),\quad W_0^{(j)}h^{(j-1)}(t,v_i)
\quad(i\le m+p),
\]
\[
\delta_a^{(j)}(t),\quad
W_0^{(j+1)\top}\delta_a^{(j+1)}(t)
\quad(a\le m),
\tag{1}
\]

with nonexistent boundary images omitted. Here
\(\delta_a^{(L)}=w\odot\phi_L'(z_a^{(L)})\) and
\(\delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot W^{(j+1)\top}\delta_a^{(j+1)}\);
the residual is not included in \(\delta\). Thus at most

\[
F=2(2m+p)
\tag{2}
\]

curves occur per layer. Their coordinate norm is the ordinary
\(\ell^\infty\) norm in \(\mathbb R^n\).

The authorized source interface supplies holomorphy and coordinate bound

\[
\|u(\zeta)\|_\infty\le M_n=M_0\sqrt n,
\quad
\zeta\in[-r_n,T_0+r_n]+i[-r_n,r_n],
\tag{3}
\]
\[
T_0=32\ell/\lambda,\qquad
r_n=\frac{a}{1024\lambda z^2U_{\rm fin}(S)\sqrt\ell}.
\tag{4}
\]

The positive source coefficient \(U_{\rm fin}(S)\) and \(M_0\) are exactly the
recurrences in `PANEL_BOUND.md` (4), (7). Its finite initialization/jet
coefficient evaluator and its simultaneous coordinate-selection interface
are inherited separately. Neither follows from abstract holomorphy alone.

The error certificate used after source selection is

\[
\sup_{t\in[0,\infty]}\max_{i\le m+p}
|f_C(t,v_i)-f_n(t,v_i)|
\le \mathcal A_n\eta+\mathcal D e^{-8\ell}.
\tag{5}
\]

The current coefficient has \(e^{64\sqrt\ell}\), as in
`PANEL_BOUND.md` (15a). It is not replaced by the older coefficient 32.
The runtime remains the autonomous corrected optimizer in the original
physical time. Temporal bases below construct its initial source spaces;
they are not retained time-dependent forcing or a playback rule.

For fixed admissible problem parameters and either the existing
variability target or the stronger output target \(Y/n\), the source
tolerance prescribed in `PANEL_BOUND.md` obeys

\[
\log(M_n/\eta)=O(\ell).
\tag{6}
\]

The prefactors in (5) and its tail gate remain part of this statement.
Zero labels have the existing exact zero-predictor branch.

## 2. A complete adaptive panel lemma

Let \(T>0\). Suppose each required vector curve is holomorphic on a
neighborhood of the closed disk

\[
|\zeta-t|\le \varrho(t),\qquad 0\le t\le T,
\tag{7}
\]

and bounded there coordinatewise by \(M\). The radius \(\varrho(t)>0\) is
specified before coefficient selection. It may be constant. Suppose
also that \(\varrho\) is nondecreasing and Lipschitz with constant \(C_r\):

\[
0\le\varrho(t)-\varrho(s)\le C_r(t-s)\quad(s\le t).
\tag{8}
\]

Starting with \(t_0=0\), set

\[
t_{b+1}=\min\{T,t_b+\varrho(t_b)/2\}
\tag{9}
\]

until \(t_J=T\). Positivity and monotonicity imply a finite number \(J\)
of panels. On every full panel, (8) gives

\[
\int_{t_b}^{t_{b+1}}\frac{dt}{\varrho(t)}
\ge\frac{\varrho(t_b)/2}
{\varrho(t_b)+C_r\varrho(t_b)/2}
=\frac1{2+C_r}.
\]

Only the last panel might be shorter, so

\[
J\le1+(2+C_r)\int_0^T\frac{dt}{\varrho(t)}.
\tag{10}
\]

For each curve and each panel define the normalized Taylor coefficients

\[
b_{b,k}=\frac{\varrho(t_b)^k}{k!}u^{(k)}(t_b),
\qquad k\ge0.
\tag{11}
\]

The Cauchy integral on the circle in (7) gives
\(\|b_{b,k}\|_\infty\le M\): substitute
\(u^{(k)}(t_b)/k!=(2\pi i)^{-1}\oint u(\zeta)(\zeta-t_b)^{-k-1}\,d\zeta\) and bound the circle length by
\(2\pi\varrho(t_b)\). Consequently, for
\(x=(t-t_b)/\varrho(t_b)\in[0,1/2]\),

\[
\left\|u(t)-\sum_{k=0}^K b_{b,k}x^k\right\|_\infty
\le M\sum_{k=K+1}^{\infty}2^{-k}=M2^{-K}.
\tag{12}
\]

For prescribed \(\eta>0\), take

\[
K=\max\left\{0,
\left\lceil\log_2\frac{8M}{\eta}\right\rceil\right\}.
\tag{13}
\]

The error in (12) is at most \(\eta/8\). All coefficients from all
panels span one time-independent vector space of dimension at most

\[
N_{\rm time}=J(K+1)
\tag{14}
\]

per curve. A source approximant may use the polynomial for the current
panel; it need not be continuous at panel boundaries. Both adjacent
polynomials approximate the same exact source there. The runtime
comparison only uses source values, never derivatives of these
piecewise approximants, so this causes no new defect term.

This is a constructive upper bound. The number of vectors used by
this recipe is not asserted to be the smallest possible source rank.

### Exact image pairs and coefficient provenance

The initialized matrices have operator norm at most eight. If \(u=W_0 v\)
or \(u=W_0^\top v\), normalized Taylor coefficients satisfy exactly
\(b_{b,k}(u)=W_0 b_{b,k}(v)\) or its transpose version. Approximate each
base coefficient by a finite initial-jet computation to Euclidean
error at most \(\eta/128\), and form its image by the exact initialized
matrix operation. A sufficient coordinate tolerance for that finite
computation is \(\eta/(128\sqrt n)\).

On one panel, the base coefficient error sums to at most
\((\eta/128)\sum_{k\ge0}2^{-k}=\eta/64\); the image coefficient error
sums to at most \(\eta/8\). Together with (12), both members have
coordinate error below \(\eta\), while their algebraic image relation is
exact. No source approximation error has been differentiated.

The inherited finite coefficient evaluator must approximate the true
coefficients (11), using certified continuation from initialization
to the real anchors and finite local jets. An exact dense trajectory
oracle is not supplied. Abstract analyticity does not itself certify
this evaluator; the original initialization/jet interface remains a
separate dependency. The added adaptive panels change only a finite
list of requested anchors and coefficient accuracies. The preprocessing
time and its width-sized arrays are not bounded by (14).

Add the constant vector, exact initial training features and forward
images, and all first-weight columns. With

\[
B=2m+d+1,\qquad R=B+FJ(K+1),
\tag{15}
\]

every layer source space has dimension at most \(R\). The inherited
selection theorem gives selected widths \(q_j\le 9R\). Its source isometry
and projected initialized mixer then preserve both retained initialized
actions: a coefficient and its forward image lie in consecutive source
spaces, and a response coefficient and its transpose image lie in the
reverse pair. One initialized mixer and its metric adjoint give these
two identities; no independently initialized reverse operator is used.

The full retained inventory from `PANEL_BOUND.md` therefore becomes

\[
\begin{split}
\operatorname{storage}\le{}&1020(L+1)[B+FJ(K+1)]^2
+36[B+FJ(K+1)]\\
&+10m(d+1)+pd+(m+p)+D_{\rm alg}.
\end{split}
\tag{16}
\]

This includes moving matrices, fixed metrics and inverse caches,
initialized selected matrices, live training/Gram buffers, all declared
inputs and outputs, and evaluator/program storage. Source coefficients,
dense jets, anchors and selected-index lists are discarded. No adaptive
panel table is retained by the runtime. The count is exact-real scalar
storage; conditioning and bit complexity remain separate.

The exact panel-span reduction from `PANEL_BOUND.md` Section 9 may
replace \(d\) in \(B\) and the first matrix by
\(k=\dim\operatorname{span}\{v_i\}\le\min(d,m+p)\), while retaining the input map and all
panel data at extra \(O((m+p)d)\) cost. This is independent of the temporal
argument.

## 3. Consequences of different analytic domains

### The domain currently proved

Under (3), use \(\varrho(t)=r_n\), \(M=M_n\), and \(T=T_0\). Then

\[
J=\left\lceil\frac{2T_0}{r_n}\right\rceil
\le1+2^{16}\frac{U_{\rm fin}(S)}a z^2\ell^{3/2}.
\tag{17}
\]

Combining (6), (13) and (17) gives \(J(K+1)=O(\ell^{5/2})\).
Substitution in (16) reproduces the fifth logarithmic power and
the explicit leading dependence

\[
(L+1)(2m+p)^2
\left[\frac{U_{\rm fin}(16Ym/\gamma)}a\right]^2
Y^4(m/\gamma)^4\ell^5.
\tag{18}
\]

Thus local panels by themselves do not improve the *certified bound*
from the fixed rectangle. This calculation is not an optimality theorem
for all temporal bases.

### Conditional sector or linearly growing disks

Suppose instead that the same source bound holds on (7) with
\(\varrho(t)=r_*+c t\), where \(c>0\). This is additional complex-time
information. Equations (10) and (14) give

\[
J\le1+\frac{2+c}{c}\log(1+cT/r_*),\qquad
N_{\rm time}\le
\left[1+\frac{2+c}{c}\log(1+cT/r_*)\right](K+1).
\tag{19}
\]

For \(T=O(\ell)\), either fixed positive \(r_*\) or \(r_*=r_n\) gives
\(N_{\rm time}=O(\ell\log\ell)\) and storage
\(O(\ell^2[\log\ell]^2)\), with the displayed structural and source
prefactors. Calling a sector an immediate proof of \(O(\ell^2)\)
storage would omit the number of geometric panels in this construction.
Another global basis could conceivably improve that count; (19)
does not rule it out.

### Conditional residual-dependent continuation

A different prospective disk radius is

\[
\varrho(t)=\kappa^{-1}
\log(1+\kappa r_n e^{\nu t}),\qquad \kappa,\nu>0.
\tag{20}
\]

Its motivation is a *hypothetical* complex continuation estimate with
residual growth \(e^{\kappa|\zeta-t|}\) and real residual decay
\(\exp(-\nu t)\). Neither (20) nor the bound \(M_n\) on its disks is an
established source conclusion. The two must be proved together.

The exact count under these assumptions is useful. Differentiate (20)
to obtain \(0\le \varrho'(t)\le \nu/\kappa\). Put
\(t_c=\nu^{-1}\log_+(1/(\kappa r_n))\). For \(t\le t_c\),
\(\log(1+x)\ge x/2\) for \(0\le x\le 1\) gives
\(1/\varrho(t)\le 2e^{-\nu t}/r_n\). For \(t\ge t_c\), the logarithm
in (20) is at least \(\log(2)+(\nu/2)(t-t_c)\): its derivative is
at least \(\nu/2\) when its exponential argument is at least one.
This also holds from \(t_c=0\) if \(\kappa r_n\ge 1\). Hence

\[
\int_0^T\frac{dt}{\varrho(t)}
\le\frac2{\nu r_n}
+\frac{2\kappa}{\nu}
\log\left(1+\frac{\nu T}{2\log2}\right),
\tag{21}
\]
\[
J\le1+\left(2+\frac\nu\kappa\right)
\left[\frac2{\nu r_n}
+\frac{2\kappa}{\nu}
\log\left(1+\frac{\nu T}{2\log2}\right)\right].
\tag{22}
\]

For fixed \(\kappa,\nu\) and (4), this would give
\(J=O(\sqrt\ell+\log\ell)\), source rank \(O(\ell^{3/2})\), and storage
\(O(\ell^3)\). The initial \(1/r_n\) cost survives in (21). In particular,
even this strengthened continuation mechanism does not yield the
requested second power by the panel construction. Its leading radius
factor is explicitly

\[
\frac1{\nu r_n}
=\frac{1024\lambda}{\nu}
\frac{U_{\rm fin}(S)}a z^2\sqrt\ell;
\tag{23}
\]

the actual label/gap factor has not been replaced by the label cap.

The current paper's all-horizon extension instead keeps the fixed
\(r_n\): it uses a safe parameter ball of radius proportional to
\(n^{-1/2}\) after \(T_0\), bounds complex residual growth by two on
segments of length \(2r_n\), and glues these disks. That proof, at
`paper/integrated_appendix.tex` lines 12522--12628, does not assert
(19) or (20). Enlarging disks only after \(T_0\) would not improve
the rank already spent on \([0,T_0]\).

## 4. A sufficient compact-clock theorem for the second power

This section is a conditional approximation theorem, not a property
proved for the neural flow. Fix \(\nu>0\) and define

\[
s=1-e^{-\nu t},\qquad
g(s)=u(-\nu^{-1}\log(1-s))\quad(0\le s<1).
\tag{24}
\]

Assume every source \(g\) extends to a holomorphic function on a
neighborhood of the closed ellipse

\[
E_\rho=\left\{
\frac12+\frac{w+w^{-1}}4:1\le|w|\le\rho
\right\}\ \text{together with its interior},\qquad \rho>1,
\tag{25}
\]

and is bounded there by \(M_n\). Both \(\rho\) and \(\nu\) are independent of
width. The elliptical boundary is the image of \(|w|=\rho\); the set
contains \([0,1]\). For a finite required horizon \(T\), let
\(s_T=1-e^{-\nu T}\) and consider \(g(s_T x)\). Convexity of the ellipse
and \(0\in E_\rho\) imply \(s_TE_\rho\subset E_\rho\). Its bound is therefore
still \(M_n\). Only physical times in \([0,T]\) are needed below.

Set \(\alpha=\log(\rho)\) and
\(G(\theta)=g(s_T(1+\cos\theta)/2)\). This is even, periodic and
holomorphic for \(|\operatorname{Im}\theta|\le\alpha\). Its Fourier coefficient \(c_k\)
has norm at most \(M_ne^{-\alpha|k|}\): shift its defining integral
down by \(i \alpha\) for \(k>0\) and up for \(k<0\). The two vertical edges
cancel by periodicity. Therefore the Chebyshev remainder obeys

\[
\left\|g(s_Tx)-c_0-2\sum_{k=1}^Kc_kT_k(2x-1)\right\|_\infty
\le\frac{2M_n\rho^{-(K+1)}}{1-\rho^{-1}}.
\tag{26}
\]

Taking

\[
K=\max\left\{0,
\left\lceil\frac{
\log[16M_n/(\eta(1-\rho^{-1}))]}{\log\rho}
\right\rceil\right\}
\tag{27}
\]

makes (26) at most \(\eta/8\). Finite coefficient quadrature and the
inherited initial-jet evaluator produce approximations to \(c_k\), using
only initialized data and source values on \([0,T]\). For example,
base-coefficient Euclidean accuracy \(\eta/[128(K+1)]\) makes the
entire initialized image coefficient error at most \(\eta/8\) after the
factor two in the cosine series. Form images exactly from the computed
base coefficients, as in Section 2. Thus the source dimension is

\[
R=B+F(K+1),
\tag{28}
\]

and the retained inventory is (16) with \(J=1\). Under (6) it is
\(O((L+1)F^2\ell^2)\), plus the displayed initialization/data/evaluator
terms, with an explicit factor \((\log\rho)^{-2}\) and the constants
inside (27). This is the precise missing analytic input that makes
the requested second logarithmic power follow through the existing
selection and comparison machinery.

The scalar functions in physical time are
\(T_k(2(1-e^{-\nu t})/s_T-1)\). Expanding these polynomials gives a
finite exponential basis in \(\exp(-\nu t)\). The basis change does not
alter vector rank. Neither its coefficients nor the clock need appear
in the runtime after source selection. Thus this conditional theorem
preserves the optimizer and physical time.

### Why decay does not establish this clock hypothesis

The image of the currently known strip boundary near a real time is

\[
s(t+iy)-s(t)=e^{-\nu t}(1-e^{-i\nu y}).
\tag{29}
\]

Its transverse size is at most \(\nu r_ne^{-\nu t}\) for
\(|y|\le r_n\), because \(|1-e^{-ix}|\le|x|\). As \(s(t)\) tends to one,
the guaranteed complex neighborhood contracts to zero. This exact
calculation does not create a fixed ellipse through \(s=1\).

There is also an elementary endpoint obstruction. For
\(u(t)=e^{-\mu t}\) with \(\mu>0\), (24) gives

\[
g(s)=(1-s)^{\mu/\nu}.
\tag{30}
\]

If \(\mu/\nu\) is not an integer, set \(j=\lfloor\mu/\nu\rfloor+1\). Its \(j\)th
real derivative is a nonzero constant times
\((1-s)^{\mu/\nu-j}\), which diverges at one; hence \(g\) has no
holomorphic extension through that endpoint. With two positive rates
having irrational ratio, no single \(\nu\) makes both exponents positive
integers. This does not obstruct a basis that retains the two
exponentials explicitly; it obstructs the inference from real
exponential decay to the particular fixed-ellipse clock theorem.

A loss or motion clock has an additional issue: dividing the dynamics
by residual magnitude requires control of the residual's direction and
of a holomorphic nonvanishing clock derivative. The real Euclidean norm
of the residual is not itself a holomorphic function of complex time.
An algebraic complex square root may have zeros or branching. None of
these analytic continuation requirements follows from an upper bound
on the real loss alone.

## 5. Terminal subtraction, tails, and claim boundary

Even if one grants the stronger source-coordinate tail estimate

\[
\|u(t)-u_\infty\|_\infty\le D_n e^{-\nu t},
\tag{31}
\]

terminal subtraction needs at most one additional vector per source:
retain a computed approximation to \(u(T_*)\) with
\(D_ne^{-\nu T_*}\) below the coefficient tolerance. This is obtainable
by a finite initial-data computation if the original evaluator applies
to that finite horizon; an exact endpoint oracle is unnecessary. Such
subtraction does not move any complex singularity of \(u\). A decaying
real bound on \(u-u_\infty\) also is not a decaying bound on its
complex disks. Those additional complex estimates would be needed to
justify lower panel degrees from decay.

For polynomially sized \(D_n/\eta\), the sufficient cutoff from (31)
is still proportional to \(\log(n)\). More importantly, the inherited
runtime proof already handles late time without retaining an endpoint
source. Apply source approximation only through \(T_0\), use (5), and
compare each fitted trajectory to its own value at \(T_0\). Both flows
continue to evolve and converge. No approximation source is asserted
after \(T_0\), no output is frozen there, and the endpoint follows by
passing to each flow's limit. An adaptive source representation must
not silently replace this argument by freezing the runtime.

What is proved in this route is the variable-radius panel lemma,
its exact initialized-image construction, all retained rank charges,
and the conditional compact-clock theorem. The only specialization
using the currently authorized fixed-strip event is (17)--(18);
it keeps the existing fifth power. The lower powers in (19), (22)
and (28) require their displayed extra complex-domain assumptions.
They are not established results for the original neural flow. Failure
to derive those assumptions is not a no-go theorem for every rational,
exponential or nonlinear compression construction.

Scientific inputs read completely were the authorized
`studies/initialization_panel_compression_20261008/PANEL_BOUND.md`,
`studies/finite_panel_absolute_compression_20261005/PANEL_SOURCE.md`,
and `docs/notation.qmd`. Directly relevant current-paper passages read
were lines 8280--8570 and 12500--12700 of
`paper/integrated_appendix.tex`; repository-wide studies were not
searched. Required canonical-notation and neural-network references,
rigorous-math instructions, and conjecture research-contract/adversarial
instructions were applied. No experiment, training, maintained-book
edit, other-study edit, or Git mutation was performed.

## 6. Focused follow-up: the residual estimate and the insertion dependency

The original route above was frozen before this follow-up. The supervisor
then authorized complete reads of
`studies/integrated_general_compression_20261004/GENERAL_TRAJECTORY_LOWER_BRIDGE.md`
and
`studies/integrated_general_compression_20261004/UNBOUNDED_COMPRESSOR_BRIDGE.md`,
together with their directly relevant current-paper insertion passages.
Those two files were read completely. The additional paper passages read
were lines 5945--6190, 6188--6550 and 7235--7335. No new probability
theorem is claimed in this follow-up.

There is a precise obstacle to merely replacing the coarse residual
bound by its anchor-dependent version. Source Section 3 and current
paper IC.8 use the norm cost at most two of the **residual-free**
negative-Gram base propagator. The same factor appears again in IC.51's
ordered insertion trace, before the residual activity integrals. The
old proof obtains it from total nonreal/backward contour length at most
\(2r_n\), and \(e^{4\mathcal K r_n}\le2\). Small integrated
residual does not directly bound this part of the variational generator.
Thus the currently proved estimate
\(\|R_a^{(j)}\|_\infty\le SU_{\rm fin}\sqrt\ell\) is not a theorem
on arbitrary longer tubes satisfying only strip, operator and activity
stops. Its stated proof uses the short-contour propagator estimate.

The following deterministic calculation identifies a possible repair.
It is conditional on source bounds **on the proposed stopped contour**;
these bounds must not be imported from the old rectangle outside its
proved domain.

### A closed stopped-propagator estimate

Use the mobility coordinates
\(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\), and define
the real-valued unnormalized predictions \(F_a=n f_n(v_a)\) on real
states. Let \(g_a=\nabla_\Theta F_a\), with holomorphic continuation
given by the same algebraic differentiation, and form the matrix

\[
G(\zeta)=\frac1{\sqrt{mn}}[g_1(\zeta),\ldots,g_m(\zeta)].
\tag{32}
\]

Its columns lie in the Euclidean direct sum of all parameter blocks.
The exact residual and variational-base equations are

\[
\dot r=-2G^\top G r,\qquad
\dot P=-A(\zeta)P,\qquad A(\zeta)=2G(\zeta)G(\zeta)^\top.
\tag{33}
\]

The full parameter variational generator also contains
\(-(2/m)\sum_a r_aD_\Theta^2F_a\); this is the separate
residual-Hessian insertion term. All transposes in (33) are algebraic
transposes, not conjugate transposes. At a real time, \(G\) is real,
so \(A\) is real symmetric and positive semidefinite.

Assume on the stopped vertical contour \(\zeta=t+i v\) the original
operator/RMS bounds and the following source derivative bounds hold:

\[
\begin{gathered}
\|G(\zeta)\|_{\rm op}\le\sqrt{\mathcal K},\qquad
\|h_a^{(j)}\|_2/\sqrt n\le H_j,
\qquad \|\delta_a^{(j)}\|_2/\sqrt n\le S\tau_j,\\
\|\dot h_a^{(j)}\|_2/\sqrt n\le2\rho S q_j^{\rm src},\qquad
\|\dot\delta_a^{(j)}\|_2/\sqrt n
\le J_*^{\rm time}\rho B_n,\\
\rho(\zeta)=\|r(\zeta)\|_2/\sqrt m,\qquad
B_n=1+(S^2/\eta_{\rm src})\log(e+\ell).
\end{gathered}
\tag{34}
\]

Here \(\eta_{\rm src}>0\) is the fixed exponential-budget coefficient
of the source proof, distinct from this note's approximation tolerance
\(\eta\). The bounds on derivatives in (34) are the forms of source
S.27 and its preceding forward bound. On the enlarged contour they
are explicit provisional assumptions in this calculation. The fixed
coefficient \(q_j^{\rm src}\) is the source response recurrence, not
a selected width.

The normalized gradient blocks \(g_a/\sqrt n\) are respectively
\(\delta_a^{(1)}v_a^\top/\sqrt n\),
\(\delta_a^{(j)}h_a^{(j-1)\top}/n\), and
\(h_a^{(L)}/\sqrt n\). Differentiate these products, use (34),
and sum their Euclidean/Frobenius bounds. Since \(B_n\ge1\), this
gives

\[
\|\dot G(\zeta)\|_{\rm op}\le C_g B_n\rho(\zeta),
\tag{35}
\]
\[
C_g=J_*^{\rm time}\left(1+\sum_{j=2}^L H_{j-1}\right)
+2S^2\sum_{j=2}^L\tau_jq_{j-1}^{\rm src}
+2S q_L^{\rm src}.
\tag{36}
\]

Indeed each column derivative divided by \(\sqrt m\) obeys its
corresponding bound divided by \(\sqrt m\); the matrix Frobenius
norm, and hence its operator norm, has the same bound after summing
the squared columns. There is no factor \(m\) in (35).

At the real anchor \(t\), freeze \(A(t)\). Along the vertical
contour, the generator \(-iA(t)\) is skew-Hermitian, so its
propagator is unitary. From (34)--(35),

\[
\|A(t+i v)-A(t)\|_{\rm op}
\le4\sqrt{\mathcal K}\,C_gB_n
\int_0^{|v|}\rho(t+i\operatorname{sgn}(v)u)\,du.
\tag{37}
\]

Conjugate the vertical equation for \(P\) by the unitary propagator
of \(-iA(t)\), then apply the norm integral inequality. For a
vertical segment of length \(h\), the result is

\[
\|P\|_{\rm op}\le
\exp\left\{4\sqrt{\mathcal K}\,C_gB_n
\int_0^h(h-v)\rho(t\mathbin{\pm}i v)\,dv\right\}.
\tag{38}
\]

For products of propagators over disjoint ordered subsegments, the
same upper exponent applies: their nonnegative integrals over the
subsegments sum to no more than the integral over the whole segment.
This is the form needed for the ordered residual-Hessian expansion.

Equation (33) and \(\|G\|_{\rm op}\le\sqrt{\mathcal K}\) give
\(\rho(t\mathbin{\pm}i v)\le\rho(t)e^{2\mathcal K v}\).
The double integral in (38) is therefore bounded by

\[
\rho(t)\,
\frac{e^{2\mathcal K h}-1-2\mathcal K h}
{4\mathcal K^2}.
\tag{39}
\]

If the real residual satisfies \(\rho(t)\le Ye^{-\nu t}\), choose

\[
h(t)=\frac1{2\mathcal K}
\log(1+2\mathcal K r_n e^{\nu t}).
\tag{40}
\]

Then direct integration and (39) yield

\[
\begin{aligned}
\int_0^{h(t)}\rho(t\mathbin{\pm}i v)\,dv&\le Yr_n,\\
\rho(t\mathbin{\pm}i h(t))&\le
Y e^{-\nu t}+2\mathcal K Yr_n,\\
\|P\|_{\rm op}&\le
\exp\left\{\frac{2C_g}{\sqrt{\mathcal K}}B_nYr_n\right\}.
\end{aligned}
\tag{41}
\]

At fixed original problem parameters,
\(B_n r_n=O(\log(e+\ell)/\sqrt\ell)\to0\). Thus (41)'s
base-propagator cost is eventually below two, with a strict margin.
It avoids the unbounded relative factor \(e^{2\mathcal K h(t)}\)
by using that the frozen real Gram gives a unitary vertical flow.
It is stronger than the coarse absolute norm argument on this
specified stopped contour; it does not control arbitrary complex paths.

Assuming also the provisional response maximum on the contour, the
query preactivation displacement is at most
\(2SU_{\rm fin}\sqrt\ell\,Yr_n=a/32\), using (4). Extra residual
activity is at most \(2Yr_n\). These are the desired deterministic
pole/activity improvements. The normalized backward complex-minus-real
coefficient change is at most
\(J_*^{\rm time}B_nYr_n/S=o(1)\); the forward change also vanishes.
All of these deductions remain conditional on (34) and the provisional
maximum being available before the proposed stop.

### The remaining bridge

The current proof uses independently stopped cavities on nested convex
rectangles and projects each cavity onto its own stopped rectangle.
The paper's IC.stop identity requires its real-anchor map and cavity
projection to commute; its Gaussian moment argument requires globally
defined cavity-measurable coefficient paths with both a vanishing
complex-minus-real radius and a controlled global modulus. The actual
Gaussian insertion estimates are applied only after these constructions.

To turn (41) into a new source theorem, one must construct independent
stops and extensions for the flaring domain suggested by (40), include
the base-propagator bound as a provisional stop, and prove simultaneously
that the existing insertion estimates, maximum improvements, coefficient
moduli, and common-cavity moment estimates remain valid there. In
particular one must derive (34) on that domain before invoking (41),
and then improve every added stop. The rectangle projection construction
cannot simply be reused with its domain silently enlarged. Nor does a
new scalar Gaussian union establish this missing cavity construction.

This is a precise uncompleted bridge, not a contradiction in the original
fixed-rectangle theorem. Formula (41) is a conditional deterministic
ingredient for it. No enlarged source event, unchanged source prefactor
on that event, or new neural compression exponent has been proved in
this bounded follow-up. The established specialization (17)--(18) and
the original fifth-power storage conclusion therefore remain unchanged.
