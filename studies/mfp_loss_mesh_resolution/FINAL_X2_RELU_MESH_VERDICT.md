# Loss-gradient mesh removal for normalized `x^2` and ReLU

## Contract and verdict

Use the one-input, two-hidden-layer network

\[
 H_j=\phi(u_j),\qquad z_i=n^{-1/2}\sum_jW_{ij}H_j,
 \qquad f_n=n^{-1}\sum_i a_i\phi(z_i),
\]

with iid standard-Gaussian initialization and half-square loss

\[
 \ell_n={1\over2}(1-f_n)^2.
\]

One loss Euler step is

\[
 \theta^+=\theta+h(1-f_n)n\nabla f_n.
\]

Width is sent to infinity for each fixed finite step schedule, and only
then is the mesh removed on a fixed physical interval.

The conclusions are:

1. For \(\phi(x)=x^2/\sqrt3\), the width-first Euler predictors and losses
   do **not** converge uniformly on compact time intervals to a continuous
   trajectory with the initialized trace.  They develop an instantaneous
   initial layer.  This is an unconditional all-orders result.
2. For \(\phi(x)=\sqrt2x_+\), a classical gradient flow based on any fixed
   value of \(\phi'(0)\) is not a globally well-posed random dynamics:
   already at width two there is a positive-probability open set of Gaussian
   initializations whose trajectory reaches a noncontinuable attracting
   gate.  Explicit Euler may nevertheless possess a generalized
   Filippov/Young-measure limit.  Existence and uniqueness of that
   width-first generalized mesh limit remain open.
3. A terminal test alone,

   \[
   \ell_{2t}(h)-\ell_t(2h),
   \]

   is weaker than compact-time mesh removal.  The quadratic theorem below
   does not decide that terminal number; both discretizations could pass
   through the same discontinuous initial layer.  For ReLU, even the
   actual-network fixed-mesh indicator DAG required to define the limiting
   terminal comparison has not been proved.

## 1. Quadratic initial-layer theorem

Let \(c=3^{-1/2}\) and \(\phi(x)=cx^2\).  Denote by
\(F_k^h\) the deterministic width-first output after \(k\) loss steps of
size \(h\).  For \(T>0\), set \(h_N=T/N\) and, for \(0<\delta<1\),

\[
 \tau_N(\delta)=h_N\min\{k:F_k^{h_N}\ge\delta\},
\]

with the minimum of the empty set defined as \(+\infty\).

Then

\[
 \tau_N(\delta)\longrightarrow0.                       \tag{1.1}
\]

Consequently no continuous interpolation of the grid predictors can
converge uniformly on \([0,T]\) to a continuous function with value zero at
time zero, and the corresponding losses cannot converge uniformly to a
continuous function with value \(1/2\) at time zero.

### Proof

For a deterministic nonnegative feature-step schedule
\(s=(s_0,\ldots,s_{m-1})\), let \(\mathcal F_{m,n}(s)\) be the expected
finite-width output after the feature-ascent updates

\[
\begin{aligned}
 a_i^+&=a_i+s_kcz_i^2,\\
 W_{ij}^+&=W_{ij}+{s_k\over\sqrt n}(2ca_iz_i)(cu_j^2),\\
 u_j^+&=u_j+s_k(2cu_j)n^{-1/2}\sum_iW_{ij}(2ca_iz_i).
\end{aligned}                                             \tag{1.2}
\]

Regard all initialization coordinates and the \(s_k\)'s as formal
indeterminates.  The initial output, every component of (1.2), and every
composition of these maps are polynomials with nonnegative coefficients.
Gaussian expectation deletes a monomial if one independent exponent is odd
and assigns it a positive product of double factorials otherwise.  Hence
\(\mathcal F_{m,n}\) has nonnegative coefficients in the schedule variables.
Therefore

\[
 0\le s_k\le\widetilde s_k\quad\forall k
 \quad\Longrightarrow\quad
 \mathcal F_{m,n}(s)\le\mathcal F_{m,n}(\widetilde s).    \tag{1.3}
\]

The fixed-schedule polynomial tensor-program theorem gives every-finite-
\(L^p\) convergence for (1.2).  Passing to the width limit in (1.3) gives
the same monotonicity for \(\mathcal F_m\).

For each fixed loss schedule, the empirical residual converges in every
finite moment.  Induction through the same finite polynomial program thus
gives the exact width-first adaptive representation

\[
 F_k^h=\mathcal F_k(s_0,\ldots,s_{k-1}),\qquad
 s_k=h(1-F_k^h).                                      \tag{1.4}
\]

This is a fixed-schedule statement; no mesh/width limit has been exchanged.
Before the first hit of \(\delta\),

\[
 s_k>(1-\delta)h>0.                                    \tag{1.5}
\]

The established all-order quadratic feature theorem states that, for every
\(\rho>0\),

\[
 \mathcal F_{2t}(\rho/t,\ldots,\rho/t)\longrightarrow+\infty.
                                                               \tag{1.6}
\]

Fix \(0<\varepsilon<T\), put

\[
 t_N=\left\lfloor{\varepsilon\over2h_N}\right\rfloor,
 \qquad \rho_*={(1-\delta)\varepsilon\over4}.
\]

Then \(t_N\to\infty\), \(2t_Nh_N\le\varepsilon\), and, eventually,

\[
 {\rho_*\over t_N}\le(1-\delta)h_N.                  \tag{1.7}
\]

If no hit occurred by step \(2t_N\), (1.3)--(1.5) would give

\[
 F_{2t_N}^{h_N}\ge
 \mathcal F_{2t_N}(\rho_*/t_N,\ldots,\rho_*/t_N)
 \longrightarrow+\infty,
\]

contradicting \(F_{2t_N}^{h_N}<\delta\).  Thus
\(\tau_N(\delta)\le\varepsilon\) eventually.  Since \(\varepsilon>0\)
was arbitrary, (1.1) follows.

Let \(\overline F_N\) be the piecewise-linear grid interpolation.  During
the first crossing it takes the value \(\delta\) at a time \(r_N\to0\).
Uniform convergence to a continuous \(F\) with \(F(0)=0\) would imply

\[
 \delta=\overline F_N(r_N)\longrightarrow F(0)=0,
\]

a contradiction.  At the same times the interpolated loss equals
\(\frac12(1-\delta)^2\ne\frac12\), proving the loss claim.

In particular, no dyadically summable split-mesh estimate in a norm
controlling this compact-time loss readout can hold: such an estimate would
make the continuous interpolants uniformly Cauchy, whose uniform limit would
be continuous.

The proof stops at the first label crossing.  After an overshoot,
\(1-F_k^h\) can be negative and coefficientwise schedule monotonicity is no
longer available.  Thus (1.1) must not be converted into an unproved claim
about a single terminal paired loss.

## 2. Exact ReLU classical obstruction

Let \(\phi(x)=cx_+\), \(c=\sqrt2\).  At width two consider

\[
 u=(1,1),\quad W_1=(1,-1),\quad W_2=(2,0),
 \quad a_1=-1/c,\quad a_2=1/(4c).
\]

Then \(z_1=0\), \(z_2=2\), \(f=1/4\), and the residual is \(r=3/4\).
If \(s\) is the selected one-sided slope at the first top gate, direct
differentiation of both the connector and lower-feature updates gives

\[
 \dot z_1=r\{4a_1s+2a_2c\}.                           \tag{2.1}
\]

Thus the negative- and positive-side normal velocities are

\[
 p={3\over8}>0,
 \qquad q=-{21\over8}<0.                              \tag{2.2}
\]

For the standard convention \(\phi'(0)=0\), the velocity assigned at the
gate is \(v_0=p\ne0\).  For any other fixed convention, one may vary
\(a_1\) slightly while preserving \(p>0>q\) and avoid the single value that
makes \(v_0=0\).

Freezing the tangential state at the contact gives the scalar normal model

\[
 \dot z=p\quad(z<0),\qquad
 \dot z=q\quad(z>0),\qquad
 \dot z=v_0\quad(z=0).                                \tag{2.3}
\]

For the actual evolving state, continuity inside the two adjacent sign
cells gives a neighborhood in which, for some \(\gamma>0\),

\[
 \dot z\ge\gamma\quad(z<0),\qquad
 \dot z\le-\gamma\quad(z>0),                           \tag{2.4}
\]

and the convention-assigned velocity obeys \(|\dot z|\ge\gamma_0>0\) on
the gate.  To prove noncontinuation without assuming a last crossing, let
\(w(t)=|z(t)|\).  It is absolutely continuous.  Equation (2.4) gives
\(w'\le-\gamma\) almost everywhere on \(\{w>0\}\), while the level-set
property of absolutely continuous functions gives \(w'=0\) almost
everywhere on \(\{w=0\}\).  Starting from \(w(0)=0\), integration yields

\[
 0\le w(t)\le-\gamma\,|\{s\le t:w(s)>0\}|,
\]

so \(w\equiv0\).  But then \(z'=0\) almost everywhere, contradicting
\(|\dot z|\ge\gamma_0\) on the gate.  Therefore the standard convention
has no classical continuation at this contact.

For completeness, the hitting set has positive probability rather than
being only one measure-zero contact.  Choose a small patch of the gate
through the displayed point on which all other gates stay strictly away
from zero and the plus-side normal velocity is at most \(-\gamma\).  The
plus-cell vector field is polynomial.  Its backward flow map

\[
 (y,s)\longmapsto\Phi_{-s}(y),qquad y\text{ in the gate patch},quad
 0<s<s_0,
\]

has full-rank derivative: the patch tangents span the gate tangent space
and the vector-field column has nonzero normal component.  The inverse
function theorem therefore makes its image an open upstream flow tube.
Every point in a sufficiently small such tube stays in the plus cell until
it hits the patch, before any other gate changes.  Gaussian initialization
has a strictly positive density on this open tube.  Thus the actual
width-two random network encounters this failure with positive probability.
A fixed derivative convention does not define a globally well-posed
classical finite-width ReLU loss flow.

This finite-width open-set theorem does not prove that a width-first
population trajectory hits an attracting gate with positive source mass;
the open-set probability has not been bounded uniformly in width.  It is a
well-posedness obstruction to the classical model, not a substitute for the
population mesh analysis below.

## 3. Why this does not settle the ReLU Euler mesh

For frozen \(p>0>q\), with the standard convention at zero (or for a generic
phase whose orbit never lands exactly at zero), explicit Euler enters the strip
\(hq<z<hp\).  Put

\[
 y_k=z_k/h,\qquad
 \alpha={p\over p-q},\qquad
 x_k={y_k-q\over p-q}\in(0,1).
\]

The update is rotation by \(\alpha\) modulo one.  If
\(I_k=\mathbf1_{\{z_k>0\}}\), then

\[
 x_{k+1}=x_k+\alpha-I_k,
 \qquad
 \left|\sum_{k=0}^{N-1}I_k-N\alpha\right|<1.           \tag{3.1}
\]

Hence \(z_k=O(h)\), while the gate converges weakly to the source-dependent
occupation

\[
 \lambda_+=\alpha={p\over p-q},
 \qquad (1-\lambda_+)p+\lambda_+q=0.                   \tag{3.2}
\]

So the attracting switch refutes a classical fixed-value ODE, but it does
not refute a mesh-selected Filippov limit.

The occupation cannot be replaced by one pointwise averaged gate.  Since
\(I_k^2=I_k\), its weak second moment is \(\lambda_+\), not
\(\lambda_+^2\).  In the network the loss rate contains

\[
 \|B\|_2^2,\qquad \|G^*B\|_2^2,
 \qquad B=A\phi'(Z),
\]

and therefore sees the gate Young measure and its reused-adjoint
correlations.

Positive homogeneity supplies useful but insufficient a priori estimates.
Conditionally on the existence of a selected population trajectory starting
from the width-limit initialization, with

\[
 R_T=1+T/2,\qquad g_T=2+2TR_T,
\]

one has

\[
 0<1-f(t)\le1,
 \quad \|A(t)\|_2^2,\|u(t)\|_2^2\le R_T,
 \quad \|q(t)\|_1\le2TR_T,
\]

and

\[
 K(t)\le8g_T^2R_T+4R_T^2.                              \tag{3.3}
\]

These follow from

\[
 \dot f=(1-f)K,
 \quad {d\over dt}\|A\|_2^2={d\over dt}\|u\|_2^2
 =2(1-f)f\le1/2,
\]

ReLU homogeneity, and the trace norm of the learned rank-one connector.
They preclude ordinary norm explosion but do not determine gate occupation
or give stability between two meshes.

The fixed-schedule smooth OMFP theorem does not apply to the hard query
\(\mathbf1_{\{Z>0\}}\).  The no-rank theorem requires pseudo-Lipschitz
coordinate maps; the a.e.-continuous rank-stable route would require a new
stagewise proof of eventual empirical/population rank agreement and of
non-atomicity for every adaptive learned gate.  Singular/duplicate histories
and possible zero-innovation inactive branches have not been excluded and
therefore prevent invoking it without that proof.  Strict Gram rank for
matrix-generated queries would not by itself prove non-atomicity of a purely
learned or deterministic gate argument.  Even such a pointwise theorem
would not provide mesh-uniform Young-measure sewing.

Accordingly, the exact ReLU Euler-mesh question is open under the current
model.  To make it a well-posed positive theorem one must specify the Euler/
Filippov selection and prove: hard-indicator fixed-mesh width identification,
an occupation-augmented reused-\(G/G^*\) OMFP, compact-time tail stability,
and uniqueness/restartability of its loss readout.

## 4. Hostile-audit boundary

- The quadratic result keeps the order `width first, mesh second` and uses
  an all-orders feature theorem, not a finite jet.
- It disproves compact-uniform continuous-flow convergence, but not the
  isolated terminal paired-loss limit.
- ReLU positive homogeneity controls sizes, not discontinuous gate choices.
- Classical ReLU failure is not silently promoted to Euler-mesh failure;
  the exact occupation identity (3.1) shows why that promotion would be
  invalid.
- No semialgebraic or generic Filippov theorem supplies uniqueness of a
  nonconvex ReLU loss readout.  That uniqueness must be proved for this
  network and its reused responses.
