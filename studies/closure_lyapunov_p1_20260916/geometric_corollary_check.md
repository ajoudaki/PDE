# Post-freeze check: current-state fitting geometry of the antipodal extension

Date: 2026-09-16. This check was requested after `route_local.md` had been
frozen and shared. It reads `route_extension.md` only for this post-freeze
comparison. Neither route has been modified. The earlier allowed canonical
sources, notation and research/mathematics skills remain the background.

**Verdict.** The proposed current-state readout correction, its unique
physical-`L2` minimality and its squared norm are valid. Ordinary joint-law
Wasserstein distance is bounded by physical carrier length. Two qualifications
are essential: the normalized correction norm need not be monotone from the
estimates currently established, and the symmetry-restricted fitting set has
one independent constraint. Two unrestricted normal directions require an
additional rank condition.

## 1. Reflection gives the required orthogonality

Use the extension's reflection `R=diag(1,-1)`, the measure-preserving mark
involutions `S_1,S_2`, and their sign matrices `J_1,J_2`. At an invariant
current state,

\[
 w=Rw\circ S_1,\qquad c=-c\circ S_2,\qquad M=J_2MJ_1.
\]

From the first identity and a change of variables in the first population,
`a(Ru)=J_1 a(u)`. Thus

\[
 H(Ru,\omega)=H(u,S_2\omega),\qquad
 H_- = H_+\circ S_2.
\]

Define, using a new letter for the common hidden-output mode,

\[
 U=\frac{H_+-H_-}{2},\qquad B=\frac{H_++H_-}{2},
 \quad C=E_2U^2,\quad F=E_2[cU],\quad e=A-F.
\]

Then `U circ S_2=-U`, `B circ S_2=B`, and `c circ S_2=-c`.
Measure preservation makes the integral of any odd integrable function zero;
hence

\[
 E_2[UB]=0,\qquad E_2[cB]=0,
 \qquad f_+=F,\quad f_-=-F.
\]

These identities concern the full joint law. They do not assume independent
current readout and upper marks.

## 2. Exact fitting correction and minimality

Assume `C>0` and keep `w,M` fixed. Set

\[
 \delta c_* =\frac eC U,\qquad c_{\rm fit}=c+\delta c_*.
                                                        \tag{1}
\]

Since `H_+=B+U`, `H_-=B-U`, orthogonality gives

\[
 E_2[\delta c_*H_+]=e,
 \qquad E_2[\delta c_*H_-]=-e.
\]

Consequently `f_+(c_fit)=A` and `f_-(c_fit)=-A`. The correction is itself
odd under `S_2`, so the corrected state stays reflection invariant.

For any other readout increment `delta c` attaining both target outputs,
the two equations are equivalent to

\[
 E_2[\delta c\,U]=e,\qquad E_2[\delta c\,B]=0.
\]

The first equation and Cauchy–Schwarz imply
`||delta c||_2^2>=e^2/C`. Equality forces `delta c=(e/C)U` almost surely
when `e!=0`; for `e=0`, only zero has norm zero. This candidate satisfies
the second constraint by orthogonality. Thus (1) is the unique minimum-norm
increment among **all** physical-`L2` readout increments enforcing both target
outputs, including increments not assumed symmetric in advance. Precisely,

\[
 \|\delta c_*\|_2^2=\frac{e^2}{C}.                     \tag{2}
\]

In prose, use “enforcing both target outputs” or “fitting both labels,” not
“preserving the two outputs,” which could instead mean leaving the original
predictions unchanged.

This construction is operationally determined by the current law state:
compute `U(beta)` from the current lower law and matrix, then push the upper
joint law forward by `(beta,c) -> (beta,c+e U(beta)/C)`. No endpoint, elapsed
time or old characteristic history is used.

## 3. Exact evolution of the correction norm

Let `G=grad_raw F` denote the extension's feature-time velocity, and
`K=||G||_raw^2`. On the physical reached trajectory,

\[
 \dot X=2eG,\qquad \dot F=2eK,\qquad \dot e=-2eK.
\]

The changing hidden-feature norm must be differentiated as well. Put
`h_sigma=tanh(w.nu_sigma)`, `s_sigma=1-h_sigma^2`,
`S_sigma=1-H_sigma^2`, for `sigma=+,-`. Then

\[
 \dot a_\sigma
 =E_1[b_1s_\sigma\,\nu_\sigma\cdot\dot w],
\]
\[
 \dot H_\sigma
 =S_\sigma b_2^T(\dot M a_\sigma+M\dot a_\sigma),
 \qquad
 \dot C=E_2[U(\dot H_+-\dot H_-)].                     \tag{3}
\]

All the expectations are differentiable along the bounded-characteristic
trajectory; bounded marks and tanh derivatives provide integrable bounds on
every finite interval. Formula (3) is already an exact current-state formula
after substituting the physical velocities.

For a gradient form, define the finite upper vectors

\[
 t_\sigma=E_2[b_2 U S_\sigma].
\]

The physical gradient of `C` has blocks

\[
 \begin{split}
 (\nabla C)_c&=0,\\
 (\nabla C)_M&=t_+a_+^T-t_-a_-^T,\\
 (\nabla C)_w&=
 s_+(b_1^TM^Tt_+)\nu_+
 -s_-(b_1^TM^Tt_-)\nu_-.
 \end{split}                                                   \tag{4}
\]

In particular

\[
 \dot C=2e\langle\nabla C,\nabla F\rangle_{\rm raw}.
                                                        \tag{5}
\]

The factors in (4) have no missing one-half: differentiating
`C=E[(H_+-H_-)^2]/4` gives `delta C=E[U(delta H_+-delta H_-)]`.
The actual transpose `M^T` appears in its lower block.

For the squared minimum readout correction `Q=e^2/C`, the exact derivative is

\[
 \dot Q=-\frac{4Ke^2}{C}-\frac{e^2\dot C}{C^2}
       =-\left(4K+\frac{\dot C}{C}\right)Q.            \tag{6}
\]

Equivalently in the auxiliary parameter, `e_s=-K` and

\[
 Q_s=-\frac{2eK}{C}-\frac{e^2C_s}{C^2},
 \qquad \dot C=2eC_s.
\]

On the exact axis, the extension proves `C_s>=0`, so `Q` decreases whenever
`e!=0`. Away from the axis its established lower bound `C>=kappa` does not
control `dot C`. Monotonicity of `Q` requires the additional estimate
`dot C>=-4KC`; no such estimate is established by the extension. The sign of
`dot C` itself is stronger than necessary, but cannot silently be omitted.
It is therefore sound to call `Q` an exact current-state fitting certificate
or correction norm. Calling it a Lyapunov function away from the axis remains
unproved.

Nevertheless the extension's result immediately gives the decaying envelope

\[
 Q(t)\le\frac{A^2}{\kappa}e^{-4\kappa t},
 \qquad Q(t)\longrightarrow0.
\]

This is compatible with nonmonotonicity at intermediate times.

## 4. Physical and joint-law distances

Let
`Gamma_1(t)=Law(b_1,g,w(t))`, `Gamma_2(t)=Law(b_2,c(t))`, and define

\[
 d_{\rm state}(t,s)^2
 =\mathcal W_2(\Gamma_1(t),\Gamma_1(s))^2
 +\mathcal W_2(\Gamma_2(t),\Gamma_2(s))^2
 +\|M(t)-M(s)\|_F^2,                                  \tag{7}
\]

where each Wasserstein metric uses the ordinary Euclidean cost on the entire
displayed joint coordinate space, including all frozen marks. Its second
moments are finite: frozen `b_l` are bounded, `g` is Gaussian, and the moving
coordinates have finite physical norms.

Coupling each time pair by exactly the same marks is an admissible coupling.
Its mark displacements are zero, so

\[
 d_{\rm state}(t,s)
 \le\|X(t)-X(s)\|_{\rm raw}
 \le\int_{\min(t,s)}^{\max(t,s)}\|\dot X(r)\|_{\rm raw}\,dr.
                                                        \tag{8}
\]

The last inequality is the norm bound for the Bochner integral of the
continuous physical velocity. The extension's tail bound therefore implies

\[
 d_{\rm state}(X(t),X_\infty)
 \le\frac{|e(t)|}{\sqrt\kappa}.
\]

The explicit corrected law state from (1) gives a potentially sharper
current-state distance-to-fitting-set bound:

\[
 \inf_{Z\in\mathcal Z_A}d_{\rm state}(X(t),Z)
 \le\frac{|e(t)|}{\sqrt{C(X(t))}}.                     \tag{9}
\]

These are upper bounds, not equalities. Ordinary Wasserstein distance may
choose couplings that rearrange marks, whereas physical carrier distance
uses the identical-mark coupling. The minimality proved in Section 2 is
physical-`L2` minimality among readout corrections on that carrier. It does
not prove that `e^2/C` equals the minimal squared Wasserstein distance to the
fitting set, nor that this Wasserstein distance decreases monotonically.

## 5. Neutral directions and reconciliation of codimensions

For fixed `w,M`, every

\[
 \eta\in\{H_+,H_-\}^{\perp}\subset L^2(\lambda_2)
\]

can be added to a fitting readout without changing either output. This is
an exact affine family, not merely a first-order assertion. The upper
canonical mark law is nonatomic with positive density in its two active
coordinates, so its `L2` space is infinite dimensional. Removing a span of
dimension at most two leaves an infinite-dimensional neutral space. Within
reflection-invariant states, the odd subspace is infinite dimensional and
its neutral readout directions are the odd functions orthogonal to `U`.

There is one independent fitting constraint in the symmetry-fixed state
space: `F=A`. Its derivative is onto because its readout gradient is `U`
and `C>0`. A direct local graph in the fixed direction `U_*` makes this
precise. At an invariant fitting state choose its nonzero `U_*`, decompose
odd readouts as `c=k+a U_*`, with `k` odd and orthogonal to `U_*`. For nearby
reflection-invariant `(w,M)`, the denominator `E[U_*U(w,M)]` stays nonzero,
and the unique fitting coefficient is

\[
 a=\frac{A-E[kU(w,M)]}{E[U_*U(w,M)]}.
\]

This is a `C1` graph of codimension one. The restricted loss Hessian at a
fitting state is `2 grad F tensor grad F`: one positive normal eigenvalue
`2K>=2C` and a tangent kernel of infinite dimension.

For comparison, the full weighted two-output readout Gram at a reflection-
invariant state has, in the anti/common output basis, eigenvalues

\[
 C=\|U\|_2^2,\qquad D_{\rm com}=\|B\|_2^2.            \tag{10}
\]

Indeed its matrix is one-half times
`[[C+D_com,D_com-C],[D_com-C,C+D_com]]`. The extension bounds `C` away from
zero, but does not bound `D_com`. If `D_com>0`, the readout block itself
gives full output rank two, and the unrestricted codimension-two fitting
geometry proved in `route_local.md` applies locally. If `D_com=0`, other
parameter blocks might still supply a second independent derivative when
the inputs are non-antipodal; that requires a separate check. `C>0` alone
does not imply it.

At exactly antipodal inputs, input oddness gives `H_-=-H_+` and `f_-=-f_+`
for every state, including nonsymmetric states. Thus `B=0` identically, and
only one output constraint can be independent in the unrestricted space.
No ambient codimension-two statement can hold there.

There is no conflict with the earlier frozen local theorem: it explicitly
proved a uniformly positive two-by-two readout Gram near an orthogonal
pair, and therefore controlled both residual directions. The extension
controls the single residual direction selected by an invariant symmetry
and thereby admits unit labels near antipodal inputs. Both theorems allow
infinitely many neutral directions and obtain finite physical length from
transverse coercivity rather than full-state positive curvature.

## Scope of this check

Sections 1–5 validate the stated geometric corollary conditional on the
extension's claimed invariant reached trajectory, its `C>=kappa` estimate
and physical tail-length theorem. This report is not an independent full
audit of the extension's axis-cone or parameter-continuity constants. Its
only additional unresolved issue for a stronger corollary is monotonicity
of `e^2/C` away from the axis, or full ambient rank two if that is desired.
