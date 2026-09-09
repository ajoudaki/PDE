# Bounded sine: canonical response measures and the remaining global estimate

2026-09-08. Bounded proof subtask. Only `CONTRACT.md`,
`BOUNDED_SINE_PICARD.md`, and `SOURCE_ROUTE.md` were read. No experiment was run.

## Conclusion

For the distinct fixed activation

\[
\phi(x)=1+\tfrac12\sin x,
\qquad B=\|\phi\|_\infty=\tfrac32,
\quad D=\|\phi'\|_\infty=\tfrac12,
\quad D_2=\|\phi''\|_\infty=\tfrac12,
\]

the genuine two-orientation Gaussian program gives exactly the proposed
Gaussian-plus-response-measure representation at every fixed chronological
discretization. The learned operator return is absorbed into an explicit
absolutely continuous part of the response. The canonical response equations
below require no inverse temporal covariance or input Gram.

There is also a uniform short-time total-variation estimate. The obstacle to
making it global is a specific first-layer variational term, rather than a
temporal Gram condition number or an omitted current return. The strongest
general bound proved here is (20). It is not a global estimate: its comparison
equation can blow up. An exact scalar cancellation shows why replacing the
problematic term by its absolute value may be substantially wasteful. For the
general admitted three-input Gram, that cancellation has not been established.

Consequently this report does **not** prove finite total variation on every
fixed horizon, global canonical population existence, or the finite GF/GD
bridge. It identifies a canonical system and its precise remaining estimate.

## 1. Normalization and bounded physical quantities

Use the exact raw metric and all three trained blocks in the contract, and set
\(c_i=y_i-f_i\), \(u_i=x_i/\sqrt d\). Thus

\[
\dot w=\sum_i c_i\phi'(z_i)q_i u_i,
\quad \dot U=\sum_i c_i b_i\otimes h_i,
\quad \dot C=\sum_i c_i\phi(v_i),
\tag{1}
\]

where \(z_i=u_i^Tw\), \(h_i=\phi(z_i)\),
\(v_i=(A_0+U)h_i\), \(b_i=C\phi'(v_i)\), and
\(q_i=(A_0+U)^*b_i\). Singular \(\Gamma\) is allowed throughout.

On a physical energy-stopped interval \([0,T]\), write

\[
\sum_i|c_i(t)|\le S,\qquad
M=\|C(0)\|_\infty+BST,\qquad M_b=DM.
\tag{2}
\]

Then \(|h_i|\le B\), \(|C|\le M\), and \(|b_i|\le M_b\).
For population statements the prescribed \(C(0)=0\) is used. The actual finite
initialization is still \(C_a(0)\sim N(0,n^{-2})\): (2) holds with its actual
initial supremum, which tends to zero in probability. No finite dynamics is
replaced by zero-readout dynamics. All source statements below have the usual
fixed-program meaning before any mesh or cap limit.

## 2. The canonical representation, including its current atom

At a fixed chronological mesh, the Gaussian source rule from `SOURCE_ROUTE.md`
has the following unwhitened form. The forward primitives \(\xi_i(t)\) have
covariance \(\langle h_i(t),h_j(s)\rangle\); the reverse primitives
\(\zeta_i(t)\) have covariance \(\langle b_i(t),b_j(s)\rangle\).
With the deterministic previously generated contractions and controls held
fixed, let

\[
\alpha_{ij}(t,ds)=\mathbb E[D_{\zeta_j(ds)}h_i(t)],\qquad
\beta_{ij}(t,ds)=\mathbb E[D_{\xi_j(ds)}b_i(t)].
\tag{3}
\]

At a mesh these are finite sums of atoms: (3) means the ordinary partial
derivatives with respect to the corresponding *unwhitened formal source
coordinates*. It does not mean division by the variance of an innovation.
Unavailable source coordinates have derivative zero. Define

\[
\begin{split}
P_{ij}(t,ds)&=\alpha_{ij}(t,ds)
 +c_j(s)\langle h_j(s),h_i(t)\rangle\,ds,\\
R_{ij}(t,ds)&=\beta_{ij}(t,ds)
 +c_j(s)\langle b_j(s),b_i(t)\rangle\,ds.
\end{split}
\tag{4}
\]

Integrals in (4) mean the actual update quadrature at a mesh. The exact source
identities are

\[
\boxed{\quad
v_i(t)=\xi_i(t)+\sum_j\int_{[0,t]}b_j(s)P_{ij}(t,ds),\qquad
q_i(t)=\zeta_i(t)+\sum_j\int_{[0,t]}h_j(s)R_{ij}(t,ds).
\quad}
\tag{5}
\]

Indeed, the initialized calls give the derivative-response terms in (3), and
integrating the actual rank-one update in (1) gives exactly the two remaining
terms in (4). Both uses of the Gaussian matrix have the same genuine adjoint.

There is a top current derivative

\[
R_{ij}(t,\{t\})=
\delta_{ij}\mathbb E[C(t)\phi''(v_i(t))].
\tag{6}
\]

It must be retained. In continuous time \(P\) has no current atom: the bottom
state changes by a time integral. The learned terms have no current atoms
either. At a chronological Euler mesh, bottom state at a node depends only on
earlier reverse queries, while the top current derivative is still present.

Equations (3)--(5) are canonical relative to the actual chronological program.
Redundant source coordinates can give nonunique coefficient descriptions of
the same contracted response; retaining the formal program fixes a description
without selecting a pseudoinverse. The uniform total variation of these
descriptions is a substantive additional assertion. A bounded Hilbert-space
projection norm does not establish it.

For a continuous source path, (3)--(6) are justified only if an appropriate
limit of these finite-program derivatives has been obtained. The equations
below identify that candidate and give estimates for finite programs as well.
They do not silently assume the missing continuous-path construction.

## 3. Exact causal derivative equations

It is convenient to multiply causal matrix kernels as operators on source
perturbations. For example, \((R\eta)(t)=\int_{[0,t]}R(t,ds)\eta(s)\).
All expectations differentiate only coordinate functions, holding deterministic
controls, contractions, and response coefficients fixed, as the source rule
requires.

### Bottom derivative

Let \(J:\mathbb R^3\to\mathbb R^d\) have columns \(u_i\). With the *total*
physical path \(q\) supplied, the first-layer state transition \(\Phi_q(t,s)\)
solves

\[
\partial_t\Phi_q(t,s)=M_q(t)\Phi_q(t,s),\quad
\Phi_q(s,s)=I,\qquad
M_q(t)=\sum_i c_i(t)q_i(t)\phi''(z_i(t))u_i u_i^T.
\tag{7}
\]

Define the random causal density

\[
F_{ij}(t,s)=
\phi'(z_i(t))u_i^T\Phi_q(t,s)u_j\,
c_j(s)\phi'(z_j(s)),\qquad s<t.
\tag{8}
\]

If \(X\) is the derivative of \(h\) with respect to the primitive reverse
source, then

\[
\boxed{\qquad X=F+FRX,\qquad
P=\mathbb EX+L_h,\qquad
(L_h)_{ij}(t,s)=c_j(s)\langle h_j(s),h_i(t)\rangle.\qquad}
\tag{9}
\]

To verify this, vary (1):

\[
\delta\dot w=M_q\delta w+
\sum_j c_j\phi'(z_j)u_j\delta q_j,
\qquad \delta q=\delta\zeta+R\delta h,
\qquad \delta h_i=\phi'(z_i)u_i^T\delta w.
\]

Variation of constants gives (8)--(9). The current atom of \(R\) contributes
to \(FRX\); it is not removed from the variational equation. For fixed finite
variation coefficients and locally integrable \(M_q\), this is an ordinary
causal linear equation. Its existence follows by successive integrals, or
directly from the finite chronological recurrence. This conditional linear
fact is not existence of the unknown coupled coefficient paths.

### Top derivative

Set \(d_i^v(t)=\phi'(v_i(t))\) and
\(\Lambda_i(t)=C(t)\phi''(v_i(t))\). Define the random measure kernel

\[
Q_{ij}(t,ds)=\delta_{ij}\Lambda_i(t)\delta_t(ds)
 +d_i^v(t)c_j(s)d_j^v(s)\,ds.
\tag{10}
\]

The second term is the derivative through the entire learned readout
\(C(t)=C(0)+\sum_j\int_0^t c_j(s)\phi(v_j(s))ds\).
The first term is the direct derivative of \(\phi'(v_i(t))\).
Consequently the derivative \(Y\) of \(b\) with respect to the forward primitive
satisfies

\[
\boxed{\qquad Y=Q+QPY,\qquad
R=\mathbb EY+L_b,\qquad
(L_b)_{ij}(t,s)=c_j(s)\langle b_j(s),b_i(t)\rangle.\qquad}
\tag{11}
\]

This follows from \(\delta b=Q\delta v\) and
\(\delta v=\delta\xi+P\delta b\). Because \(P\) is strictly causal, the atom
in \(Q\) does not create an algebraic inverse at equal times.

Equations (9) and (11), together with the physical state equations and
covariances, retain both orientations, the readout history, both learned
returns, and all current response atoms. Their discrete versions are ordinary
chain-rule identities. No tiny temporal Gram is inverted anywhere.

## 4. A useful strengthening: the reverse primitive has a Gaussian path bound

This section concerns a genuine physical path or an energy-preserving
approximation with its source representation already identified. Let
\(\|A(t)\|_{\rm op}\le M_A\), and suppose

\[
\int_0^T(\|\dot w\|_2^2+\|\dot U\|_{\rm HS}^2+
\|\dot C\|_2^2)dt\le E_0.
\]

For each input,

\[
\int_0^T\|\dot v_i\|_2^2dt
\le 2(M_A^2D^2+B^2)E_0,
\]

because \(\dot v_i=A\dot h_i+\dot U h_i\),
\(\|\dot h_i\|_2\le D\|\dot w\|_2\), and
\(\|h_i\|_2\le B\). Therefore

\[
\sum_i\int_0^T\|\dot b_i\|_2^2dt
\le 6D^2E_0+12M^2D_2^2(M_A^2D^2+B^2)E_0=:V_T,
\tag{12}
\]

using \(\dot b_i=\phi'(v_i)\dot C+C\phi''(v_i)\dot v_i\).
Let \(S_\zeta=\sum_i\|b_i(0)\|_2^2+V_T\).
The isonormal construction applied to \(b_i(0)\) and \(\dot b_i\) produces a
Gaussian element in \(\mathbb R^3\oplus L^2([0,T];\mathbb R^3)\) with trace
at most \(S_\zeta\). Its integrated version has the prescribed reverse-source
covariance. The Gaussian Hilbert-space exponential-moment argument in
`SOURCE_ROUTE.md` and
\(\sup_t|g(t)|^2\le(1+T)(|g(0)|^2+\int|\dot g|^2)\) give

\[
\mathbb E\exp\left\{
\frac{\sum_i\sup_{t\le T}|\zeta_i(t)|^2}
{4(1+T)S_\zeta}\right\}\le e^{1/2}.
\tag{13}
\]

The zero-trace case is deterministic zero. This is stronger than an integrated
reverse-source bound, and its proof uses bounded \(C\) essentially. It still
does not control the response term in (5).

## 5. An integrated variation estimate, with its precise failure to close

The following estimates use (2), the source representation, and the actual
variational equations. They do not replace the genuine initialized action by
an arbitrary bounded \(L^2\) operator. They also do not require (13).

Write

\[
r(t)=\max_i\sum_j\|R_{ij}(t,\cdot)\|_{\rm TV},
\qquad I(t)=\int_0^t r(u)du.
\]

For this section assume the fixed program, or supplied continuous coefficient
path, has finite variation. All inequalities apply before any limit; the
question is whether the resulting bound is uniform.

### Bottom response bound

The source representation gives pointwise

\[
\max_i|q_i(t)|\le Z(t)+Br(t),\qquad
Z(t)=\max_i|\zeta_i(t)|.
\tag{14}
\]

Apply a unit impulse to reverse coordinate \(j\) at time \(s\). The initial
state response has norm at most \(D|c_j(s)|\). If \(m(t)\) is the supremum of
its state-response norm over \([s,t]\), the differentiated physical equation
and \(|\delta h_i|\le D|\delta w|\) give

\[
m(t)\le D|c_j(s)|+
\int_s^t\{D_2S Z(u)+S(BD_2+D^2)r(u)\}\,m(u)du.
\]

The second summand in the braces includes the entire variation of \(R\),
including its current atom. Set
\(a=D_2S\), \(b=S(BD_2+D^2)\). Gronwall then gives

\[
\sum_j|\mathbb EX_{ij}(t,s)|
\le D^2S\,\mathbb E\exp\!\left(a\int_s^t Z(u)du\right)
\exp\!\left(b\int_s^t r(u)du\right).
\tag{15}
\]

This is a bound on the expectation of the actual derivative, obtained by an
absolute derivative majorant; no independence between its factors is used.
The random integral in (15) is harmless by bounded legal reverse queries:
each \(\zeta_i(u)\) is centered Gaussian with variance at most \(M_b^2\).
Jensen in time and \(e^{\max_i x_i}\le\sum_i e^{x_i}\) give

\[
\mathbb E\exp\!\left(a\int_s^t Z(u)du\right)
\le 6\exp(a^2T^2M_b^2/2)=:G_T.
\tag{16}
\]

For a zero-length interval the left side is one and the bound remains valid.
The correlations between different source times never enter this estimate.
Together with \(\sum_j|(L_h)_{ij}(t,s)|\le SB^2\), it proves

\[
p(t,s):=\max_i\sum_j|P_{ij}(t,s)|
\le P_T\exp\{b(I(t)-I(s))\},\qquad
P_T=S(D^2G_T+B^2).
\tag{17}
\]

Here \(P(t,s)\) denotes its density; at a mesh it denotes the coefficient
divided by the actual step weight.

### Top response bound

The atom in \(Q\) has row norm at most \(L_0=D_2M\), and its density has row
norm at most \(L_1=D^2S\). Hence \(Q\) has row variation at most
\(Q_T=L_0+L_1T\). The causal density \(QP\) has row norm bounded by

\[
L_0p(t,s)+L_1\int_s^t p(u,s)du
\le K_T e^{b(I(t)-I(s))},\qquad K_T=Q_TP_T.
\tag{18}
\]

If \(y(t)\) is any sample's row variation of \(Y(t,\cdot)\), (11) and (18)
give

\[
y(t)\le Q_T+K_T\int_0^t e^{b(I(t)-I(s))}y(s)ds.
\]

Multiply by \(e^{-bI(t)}\), use that it is at most one, and apply the ordinary
integral Gronwall inequality. The resulting deterministic bound is

\[
y(t)\le Q_T\exp\{K_Tt+bI(t)\}.
\tag{19}
\]

Taking expectations can only reduce the variation needed to bound
\(\mathbb EY\). The learned reverse density has row norm at most
\(L_R=SM_b^2\). We obtain the promised closed necessary majorant:

\[
\boxed{\qquad
r(t)\le L_Rt+Q_T\exp\!\left\{K_Tt+b\int_0^t r(u)du\right\}.
\qquad}
\tag{20}
\]

All constants in this display are explicit functions of \(S,M,T\) and the
fixed activation bounds. They involve neither a temporal Gram inverse nor
an incoming-field supremum.

For example, let \(A_T=L_RT+Q_Te^{K_TT}\). Then (20) implies
\(I'\le A_Te^{bI}\), and consequently

\[
r(t)\le\frac{A_T}{1-bA_Tt},\qquad 0\le t<(bA_T)^{-1}.
\tag{21}
\]

Thus (20) is a genuine local uniform estimate. It is not a global one: the
comparison equation \(I'=A_Te^{bI}\) diverges at a finite time. Such divergence
does not show divergence of the physical response.

### Mesh and cap scope of this estimate

At a fixed chronological mesh, replace integrals by update-weighted sums and
use the chain rule at each node. The bottom linear recurrence is bounded by
products of \(1+\Delta t\,[aZ+br]\), hence by the same exponential of the
weighted sum. Jensen gives (16) with exactly those weights. The top recurrence
is strictly causal even though \(Q\) has its current atom. Discrete Gronwall
gives the counterparts of (19)--(21), with a harmless endpoint enlargement of
\(T\). In particular the local bound has no inverse step size. Bounds on the
physical controls must be supplied by the approximation or a stopping rule;
this argument does not assert unrestricted Euler energy monotonicity.

There is also no cap-derivative loss for the following explicit class of
energy-preserving first-layer caps. Apply a smooth nonexpansive radial map
\(\mathcal C_N(g)=\rho_N(|g|)g\), with \(0\le\rho_N\le1\) and
\(\|D\mathcal C_N\|_{\rm op}\le1\), to the entire first-row raw velocity
\(g=\sum_i c_i\phi'(z_i)q_i u_i\). Leave \(\dot U\) and \(\dot C\)
unchanged. It is dissipative because it multiplies that entire gradient by
a nonnegative scalar. Its differentiated equation inserts
\(D\mathcal C_N(g)\) in front of the same terms used above; their bounds
therefore remain unchanged. The bounded legal queries and learned terms also
remain unchanged. Equations (15)--(21) are uniform in these cap levels.
The uncapped transition formula (7)--(8) is replaced by the corresponding
capped transition when deriving the capped version of (9). No claim is made
for unrelated caps with unbounded derivatives or altered learned updates.

## 6. A cancellation that the absolute estimate loses

The problematic part of (15) is the signed matrix
\(M_q=\sum_i c_iq_i\phi''(z_i)u_i u_i^T\), not the top response atom, which is
bounded. To see why an absolute estimate can be misleading, consider the
admitted special case \(\Gamma=I_3\), still with the sine activation.

With the total \(q\) path held fixed, each scalar equation is
\(\dot z_i=c_i(t)q_i(t)\phi'(z_i)\). Let
\(\tau_i(t)=\int_0^t c_i(u)q_i(u)du\), and let \(\psi_\tau(z)\) denote the
complete scalar flow of \(x'=\phi'(x)\). Then
\(z_i(t)=\psi_{\tau_i(t)-\tau_i(s)}(z_i(s))\). The flow identity

\[
D_z\psi_\tau(z)\,\phi'(z)=\phi'(\psi_\tau(z))
\]

follows by differentiating
\(\psi_\tau(\psi_\epsilon(z))=\psi_{\tau+\epsilon}(z)\) at \(\epsilon=0\).
It also holds at zeros of \(\phi'\); no division by \(\phi'\) is needed.
Substitution in (8) yields the exact cancellation

\[
F_{ij}(t,s)=\delta_{ij}c_i(s)[\phi'(z_i(t))]^2,
\qquad \sum_j|F_{ij}(t,s)|\le SD^2.
\tag{22}
\]

In particular \(F\) is bounded independently of \(q\), even if the scalar
state-transition derivative itself is large. The return feedback \(FRX\)
still has to be solved; (22) is an exact bound on its forcing kernel, not a
claim that that feedback vanishes.

For a general admitted \(\Gamma\), the controlled first-layer vector fields
\(V_i(w)=\phi'(u_i^Tw)u_i\) do not commute. Their bracket is

\[
[V_i,V_j](w)=\Gamma_{ij}
\bigl(\phi'(z_i)\phi''(z_j)u_j
      -\phi'(z_j)\phi''(z_i)u_i\bigr),
\tag{23}
\]

with bracket convention \([V_i,V_j]=DV_jV_i-DV_iV_j\). It generally does not
vanish. Therefore the scalar flow identity does not supply (22) for the
contract's general data. Equations (22)--(23) exhibit a real cancellation and
its exact limitation; they neither prove nor disprove a corresponding
averaged cancellation on physical paths.

## 7. Exact remaining obligation

The desired conclusion is

\[
\sup_{\text{admissible meshes/caps}}\;
\sup_{t\le T}\max_i\sum_j\|R_{ij}(t,\cdot)\|_{\rm TV}<\infty
\quad\text{for every fixed }T.
\tag{24}
\]

Given (24), (5) and bounded \(h\) immediately give, uniformly in the
approximation,
\(\|q_i(t)\|_p\le C M_b\sqrt p+B\sup r\) for \(p\ge2\).
If the physical energy hypotheses also give (13), the same representation
gives a subGaussian bound for \(\sup_{t\le T}|q_i(t)|\). No independence of
the primitive and the return is needed.

The exact coupled response identities whose solutions need (24) are

\[
P=\mathbb E[(I-F_qR)^{-1}F_q]+L_h,
\qquad
R=\mathbb E[(I-QP)^{-1}Q]+L_b.
\tag{25}
\]

These inverse symbols denote causal Volterra resolvents, not temporal Gram
inverses. The unresolved estimate is control of the *signed, averaged bottom
resolvent* in (25) on physical paths, sufficiently stronger than (17) to prevent
the \(\exp(b\int r)\) feedback in (20). An acceptable alternative is a direct
bound on the whole coupled resolvent that avoids separately estimating that
factor. Bounded \(h,b,C\), the physical energy identity, and bounded top
derivatives give the other terms in (25) the explicit controls already shown.

This is a narrowly specified obligation: exploit physical residual feedback or
first-layer flow cancellations in

\[
\mathbb E[(I-F_qR)^{-1}F_q],\qquad
F_q(t,s)=D_z(t)J^*\Phi_q(t,s)J\operatorname{diag}(c(s))D_z(s),
\]

with \(\Phi_q\) governed by the actual \(q\)-weighted matrix (7), and with
\(q\) constrained by (5) and physical training. Replacing \(\Phi_q\) by a
generic bounded-coefficient \(L^2\) propagator, assuming a finite all-time
residual clock, or restarting (21) without a quantitative bound on the reached
response variation does not discharge it.

The derivation proves that the canonical response-measure route is meaningful
and locally controlled for a natural cap class. It leaves the global estimate
(24), its limiting representation, and the strong identification and
convergence conclusions open.

## 8. A precise averaged-chain condition would close by convolution

The next sufficient condition concerns averaged products, and permits unbounded
samplewise state-transition Jacobians. It makes precise one way to improve on
(20). For this subsection use the submultiplicative matrix norm
\(|M|_\Sigma=\sum_{ij}|M_{ij}|\).

**Proposition.** Fix \(T\). Suppose that for every chronological chain
\(t\ge t_0\ge s_0\ge t_1\ge s_1\ge\cdots\ge t_m\ge s_m\ge0\)
and every deterministic matrix collection with \(|D_j|_\Sigma\le1\), the
actual physical kernel (8) satisfies

\[
\left|\mathbb E\left[
 F(t_0,s_0)D_1F(t_1,s_1)\cdots D_mF(t_m,s_m)
\right]\right|_\Sigma\le f_T^{m+1},
\tag{26}
\]

uniformly over the approximations. The condition concerns signed expectations;
it does not replace the left side by the expectation of its norm. Then the
coupled response system (9), (11) has total-variation bounds on \([0,T]\)
depending only on \(f_T,S,M,T\), uniformly over those approximations.

**Proof.** Let \(\lambda\) bound the total-entry norm of the atom of \(Q\),
let \(l\) bound the total-entry norm of its density, and let \(\ell_h,\ell_b\)
bound the two learned densities. One may take

\[
\lambda=3D_2M,\quad l=3D^2S,\quad
\ell_h=3SB^2,\quad\ell_b=3SM_b^2.
\]

Expand the strictly causal resolvents in (9), (11). In the bottom expansion,
normalize each intervening deterministic matrix measure by its scalar
total-entry variation measure. Inequality (26) bounds each averaged chain by
the corresponding positive scalar chain with every \(F\) replaced by the
constant density \(f=f_T\). This step keeps the signed expectation until after
the entire chain, so no samplewise Jacobian bound is being smuggled in.
At a finite chronological program these expansions terminate. For an existing
continuous response with finite variation, (15)--(16) give an integrable
absolute majorant at that fixed response, justifying exchange of expectation
and its convergent expansion; the constants used for that justification need
not be uniform. The following argument then gives the uniform a priori bound.
It does not construct a continuous response from signed expectations alone.

Let \(p(t-s)\) dominate the total-entry density of \(P(t,ds)\), and let
\(\lambda\delta_t+\rho(t-s)ds\) dominate that of \(R(t,ds)\). It suffices to
construct positive scalar envelopes satisfying, with convolution on
\([0,\infty)\) and \(1(t)=1\),

\[
\begin{split}
p&\ge a+f\lambda(1*p)+f(1*\rho*p),\qquad a=f+\ell_h,\\
\rho&\ge l+\ell_b+\lambda^2p+\lambda(p*\rho)
                  +l\lambda(1*p)+l(1*p*\rho).
\end{split}
\tag{27}
\]

The first line is the positive envelope of \(F+FRX+L_h\), replacing the
response \(X\) by the larger envelope \(p\). For the second line use
\(Y=Q+QPY\) and replace the density of \(Y\) by the larger \(\rho\).
In particular the \(\lambda^2p\) term retains both current top atoms.

Eliminate that linear, equal-time \(p\) term by substituting the first line
into it in the positive recurrence. If \(k=p+\rho\), the resulting scalar
upper recurrence is bounded by

\[
k=A+B(1*k)+C(k*k)+D(1*k*k),
\tag{28}
\]

where

\[
\begin{split}
A&=(1+\lambda^2)a+l+\ell_b,\\
B&=(1+\lambda^2)f\lambda+l\lambda,\\
C&=\lambda,\qquad D=(1+\lambda^2)f+l.
\end{split}
\]

For \(A>0\), set \(E=B/A+C+DT\). The nonnegative function

\[
\overline k(t)=A\sum_{n=0}^{\infty}
\operatorname{Cat}_n\frac{(AE t)^n}{n!}
\le A e^{4AE t}
\tag{29}
\]

solves \(\overline k=A+E(\overline k*\overline k)\). Here
\(\operatorname{Cat}_0=1\),
\(\operatorname{Cat}_{n+1}=\sum_{j=0}^n\operatorname{Cat}_j
\operatorname{Cat}_{n-j}\), and
\(\operatorname{Cat}_n\le4^n\), which follows from the usual count of balanced
parenthesis words as a subset of all binary words of length \(2n\).
The convolution identity follows directly by multiplying the series and
integrating monomials: the convolution of \(t^j/j!\) and \(t^k/k!\) is
\(t^{j+k+1}/(j+k+1)!\).

Since \(\overline k\ge A\) and is nondecreasing,

\[
1*\overline k\le A^{-1}(\overline k*\overline k),\qquad
1*\overline k*\overline k
\le T(\overline k*\overline k)\quad(0\le t\le T).
\]

Thus (29) is a global supersolution of the positive recurrence (28).
Starting with the nonnegative constant terms, successive causal expansion is
bounded by this supersolution at every finite stage. The monotone limit is
therefore finite and dominates the original absolute response expansions.
The zero case \(A=0\) is trivial. In particular one gets

\[
\sup_{t\le T}\sum_{ij}\|R_{ij}(t,\cdot)\|_{\rm TV}
\le\lambda+TAe^{4AET}.
\tag{30}
\]

At a mesh, each continuous-time convolution in this proof corresponds to the
strictly ordered update sums. The bound
\(\sum_{k_1<\cdots<k_n}\Delta t_{k_1}\cdots\Delta t_{k_n}\le T^n/n!\)
replaces the simplex integral. All same-time top atoms have already been
retained in \(\lambda\); they contribute no inverse mesh factor. Thus the
same bound, with constants enlarged if necessary at the final node, is mesh
uniform. The finite-program causal induction does not presume an unknown
future coefficient path. \(\square\)

For the continuous uncapped orthogonal-input response system, (22) proves (26)
pathwise with \(f_T=SD^2\). Consequently its total-variation a priori estimate
is global, conditional on source identification. The scalar continuous-flow
identity does not hold exactly for an Euler update; no Euler-uniform instance
of (26) is inferred from (22). Cap removal, autonomous strong construction,
and actual finite-algorithm convergence remain separate tasks. A radial cap
can also couple the scalar fields, so (22) and this special-case conclusion
are not automatically asserted for that cap family.

For general admitted inputs, (26) is **unproved**. Using the usual absolute
bound on \(\Phi_q\) in an ordered chain does control the primitive Gaussian
part: the chain intervals are disjoint, so its exponential contains at most
\(a\int_0^T Z\), whose expectation is bounded by (16). The learned and
initialized return part of \(q\) still contributes a factor bounded only by
\(\exp(C\int_0^T r)\). Thus ordered chronology alone removes repeated charging
of the primitive Gaussian integral, but does not remove the unresolved return
factor. Establishing (26), or a weaker signed-chain estimate still yielding a
finite convolution supersolution, is an exact sufficient remaining obligation.

Finally, the squared-loss sign has been retained through \(c_i=y_i-f_i\).
It supplies the energy inequality, but does not make \(M_q\) in (7)
nonpositive. This is already visible in a physical initial jet: in the
orthogonal-input case, `BOUNDED_SINE_PICARD.md` identifies the initial derivative
\(\dot q_i(0)=Q_i\), where conditionally on \(Z\), \(Q\) has a nondegenerate
Gaussian innovation for a nonzero label vector. Choose \(i\) with \(y_i\ne0\).
On any event where \(\phi''(Z_i)\ne0\), the leading coefficient
\(y_iQ_i\phi''(Z_i)\) has both signs. This is an initial-jet observation,
not an assumed global Taylor expansion. It rules out a pointwise
negative-semidefinite argument for (7); it does not rule out the averaged
physical cancellations required by (26).
