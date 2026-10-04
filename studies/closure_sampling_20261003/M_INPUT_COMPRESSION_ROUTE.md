# Fixed orthogonal training inputs and whole-sphere compression

2026-10-03. Scoped theoretical extension of the two-input construction in
this study. This is an internally derived proof, not an independent promotion
review. The scientific inputs are the six assigned one-/two-input route notes,
the canonical model in `paper/main.tex`, and the maintained notation contract.
No other new route, experiment, trained trajectory, or Git operation enters
this derivation. The canonical-notation, rigorous-proof, and conjecture-audit
instructions were applied. The proof below gives the changed steps explicitly;
its unchanged deterministic comparison and initial-jet continuation lemmas
are the complete lemmas in `TWO_INPUT_STABLE_GEOMETRY.md`.

**Subsequent study status.** The final section records the historical
nonorthogonal obstruction of this particular regular-coordinate route.
The later checked construction in GENERAL_ANALYTIC_COMPRESSION.md
resolves the broader nonorthogonal compression question under its stated
assumptions. That result was not an input to the independent axis derivation
below; the route-specific open statements are not the current study status.

## 1. Statement and normalization

Fix integers $1\le m\le d$, independently of width. Let

\[
 A\in\mathbb R^{n\times d},\quad W\in\mathbb R^{n\times n},
 \quad w\in\mathbb R^n,\qquad
 h(x)=\tanh(Ax/\sqrt d),\quad g(x)=\tanh(Wh(x)),
 \quad f_n(t,x)=w^\top g(x)/n.
\]

Train on $x_a=\sqrt d\,e_a$, $1\le a\le m$. The loss is the
unhalved mean square $m^{-1}\sum_a(f_n(x_a)-y_a)^2$, and the block
mobilities are $(n,1,n)$. Initially the entries of $A_0$ are independent
$N(0,1)$, those of $W_0$ are independent $N(0,1/n)$, the arrays are
independent, and $w_0=0$. Define

\[
 \beta=2/m,\quad r_a=f_n(x_a)-y_a,\quad c_a=-r_a,
 \quad a_a=Ae_a,\quad h_a=\tanh a_a,\quad z_a=Wh_a,
 \quad g_a=\tanh z_a,
\]
\[
 \delta_a=w\odot\operatorname{sech}^2z_a,\qquad
 k_a=W^\top\delta_a.
\]

The exact physical equations are

\[
 \dot a_a=\beta c_a\operatorname{sech}^2a_a\odot k_a,
 \qquad
 \dot W={\beta\over n}\sum_a c_a\delta_ah_a^\top,
 \qquad \dot w=\beta\sum_a c_ag_a.                 \tag{1}
\]

The columns $Ae_b$, $m<b\le d$, remain exactly at initialization.
The factor \(\beta\) must occur in all three equations; it cannot be
discarded when comparing the models at the same physical time.

**Theorem.** There are constants $Y_*,C>0$, depending only on fixed
$m,d$, with the following property. For each fixed $y\in\mathbb R^m$
with $|y|\le Y_*$, each $0<\eta<1/2$, and sufficiently large $n$,
an initialization-only exact-real construction produces a positive weighted
two-hidden-layer network with its own autonomous residual-driven dynamics,
such that with probability at least $1-\eta$,

\[
 \sup_{t\in[0,\infty]}\sup_{\|x\|_2=\sqrt d}
       |f_C(t,x)-f_n(t,x)|\le Cn^{-1/2}.             \tag{2}
\]

The total number of moving and fixed stored real coordinates after setup is

\[
 C[\log(en/\eta)]^{6d+4}=o(n).                    \tag{3}
\]

Both systems fit their labels and converge to fitted limits. Their hidden
layers remain trainable. For fixed nonzero $y$, the dense system, and hence
the selected weighted construction for sufficiently large width, have
width-independent feature displacement in both hidden layers at a fixed
positive time, as explained in Section 8. Label signs and ratios are unrestricted.
The event for the source theorem may depend on the fixed label vector; no
simultaneous source estimate over a continuum of labels is asserted.

Setup work, temporary storage, precision, and conditioning are unrestricted.
The construction uses finite formulas in the initialized arrays and labels,
including finitely many initial derivatives. It never takes trained snapshots
as inputs. After setup, every retained real number is counted, and the dense
network, basis arrays, source coefficients, and initial derivatives are discarded.
There is no claim of efficient preprocessing or finite-precision complexity.
For $y=0$, the dense readout is identically zero and a stationary zero-output
weighted network gives (2) directly.

## 2. Real regular coordinates, fitting, and feedback stability

Put

\[
 \Psi(s)=s/2+\sinh(2s)/4,\quad
 u_a=\Psi(a_a),\quad \psi=\Psi^{-1},\quad \sigma=\tanh\circ\psi.
\]

Then \(\dot u_a=\beta c_ak_a\) exactly. The inverse is 1-Lipschitz on
the real axis. Its fixed complex strip, and bounded derivatives of \(\sigma\)
on strict substrips, are proved directly in `COMPLEX_ACTIVITY_ROUTE.md`.

For arbitrary positive diagonal neuron masses $D_1,D_2$, of total mass
one or less, write $B^*=D_1^{-1}B^\top D_2$. The weighted model uses
$h_a=\sigma(u_a)$, $z_a=Bh_a$, $g_a=\tanh z_a$,
$\delta_a=w\odot\operatorname{sech}^2z_a$,
$f_a=w^\top D_2g_a$. In coordinates $X=(u_1,\ldots,u_m,B,w)$, use

\[
 \|\Delta X\|=\sum_a\|\Delta u_a\|_{D_1}
  +\|D_2^{1/2}\Delta B D_1^{-1/2}\|_F+\|\Delta w\|_{D_2},
 \qquad \|v\|_D^2=v^\top Dv.
\]

The residual-free vector field $V_a$ has $u_a$ block
\(\beta B^*\delta_a\), zero in the other $u$ blocks, $B$ block
\(\beta\delta_ah_a^\top D_1\), and $w$ block \(\beta g_a\).
Thus \(\dot X=\sum_a c_aV_a(X)\). This is the exact weighted counterpart
of (1), not an approximation at this stage.

Let $s(t)=\int_0^t|c(v)|\,dv$. Bounded real gates and the weighted
rank-one norm identity give, while $s\le S$,

\[
 \|w\|_\infty\le\beta\sqrt mS,\quad
 \|B-B_0\|_{\rm HS}\le C_mS^2,\quad
 \sum_a\|u_a-u_{a,0}\|_{D_1}\le C_{m,K}S^2,       \tag{4}
\]

provided \(\|B_0\|_{D_1\to D_2}\le K\). Consequently
\(\|g_a-g_{a,0}\|_{D_2}\le C_{m,K}S^2\). On the convex real tube
specified by these bounds, \(\|DV_a\|\le C_{m,K}\) and
\(\|V_a-V_{a,0}\|\le C_{m,K}S\). For the $u_a$ block this is the
finite difference of $B^*(w\odot\operatorname{sech}^2(B\sigma(u_a)))$:
the transformed coordinate has removed a diagonal carrier multiplier.
The $B,w$ blocks follow from bounded gate derivatives and the operator
bound. These estimates require no lower bound on the smallest positive mass.

For the observation $F(X)=(f_a)_a$, define

\[
 (L_0\Delta X)_a=g_{a,0}^\top D_2\Delta w,\qquad
 N_a(X)=w^\top D_2(g_a-g_{a,0}).
\]

Then $F=L_0(X-X_0)+N$, \(\operatorname{Lip}(N)\le C_{m,K}S\),
and $L_0V_0=\beta G_0$, where
$G_{0,ab}=g_{a,0}^\top D_2g_{b,0}$. Thus the deterministic comparison
lemma of `TWO_INPUT_STABLE_GEOMETRY.md`, which is stated for arbitrary
output dimension $m$, applies with gap \(\beta\gamma\) whenever
\(G_0\succeq\gamma I_m\). In its notation, an additive velocity error
with integral at most \(\epsilon\), and an observation error uniformly
at most \(\epsilon\), produce state error \(C\epsilon\) on every
time interval, with a constant independent of the interval length, if both
actual residual lengths are sufficiently small. Its proof integrates the
difference of the signed residuals by parts and uses the positive gap of
\(\beta G_0\). Neither individual residual signs nor commuting input
vector fields are needed.

Direct differentiation of the weighted outputs gives

\[
 \dot c=-\beta K(X)c,
\]
\[
 K_{ab}=\langle g_a,g_b\rangle_{D_2}
 +\langle\delta_a,\delta_b\rangle_{D_2}
                         \langle h_a,h_b\rangle_{D_1}
 +\mathbf1_{a=b}\|
       \operatorname{sech}^2a_a\odot B^*\delta_a\|_{D_1}^2. \tag{5}
\]

Each term is positive semidefinite; the middle term is a Gram matrix of
rank-one tensors. Equations (4) keep the first term above \(\gamma I/2\)
until a fixed small activity exit. On that interval,

\[
 |c(t)|\le |y|e^{-\beta\gamma t/2},\qquad
 \int_0^t|c(v)|\,dv\le {2|y|\over\beta\gamma}.       \tag{6}
\]

Taking \(|y|\) small prevents the exit, and (4) prevents state escape.
This proves global fitting and finite residual length. The tail in the
displayed state norm is \(C|y|e^{-\kappa t}\), with a fixed
\(\kappa>0\). For a sphere query $x=\sqrt d\,v$, \(|v|=1\),
the first preactivation is \(\sum_{a\le m}v_a\psi(u_a)
+\sum_{b>m}v_bA_0e_b\). Its difference between two states with common
inactive columns is bounded in weighted norm by
\(\sum_{a\le m}\|\Delta u_a\|_{D_1}\). The subsequent real maps
are uniformly Lipschitz on the operator/readout tube. Hence the same
exponential prediction tail holds uniformly on the full sphere.

For the canonical initialization, the empirical first-feature covariance
converges exponentially in probability to \(qI_m\),
\(q=\mathbb E\tanh^2Z>0\), because the $m$ Gaussian columns are
independent and tanh is bounded and odd. Conditional on them, the $n$
upper preactivation rows are iid centered Gaussian vectors with this
empirical covariance. Bounded concentration and continuity of Gaussian
expectations show \(G_0\to\nu I_m\),
\(\nu=\mathbb E\tanh^2(\sqrt q Z)>0\). Thus a fixed gap, a fixed
Gaussian operator bound, and all fixed-column RMS bounds hold with high
probability. Only finitely many entries are involved because $m,d$ are fixed.

## 3. Autonomous cavities and the physical-time source rectangle

The singleton cavities retain normalization $n$, remove either one lower
neuron and all its $d$ read-in coordinates, or one upper neuron and its
readout coordinate, and use their own residuals. They are independent of
the omitted Gaussian mixer column or row, respectively. Deleting a lower
neuron changes each initial top feature by ordinary Euclidean norm at most
$K$; deleting an upper neuron changes a Gram entry by at most $1/n$.
Their initial Gram gaps therefore stay positive for large $n$.

Applying the comparison lemma just verified gives, on the ordinary

\[
 D_c=\sum_{a\le m}\|u_{a,\mathrm{ret}}-u_a^c\|_2
 +\|\sqrt n(W_{\mathrm{ret}}-W^c)\|_F
 +\|w_{\mathrm{ret}}-w^c\|_2
\]

scale, the same bounds as in the two-input proof:

\[
 \sup_{t\ge0}D_{-i}(t)\le C_mY,\qquad
 \sup_{t\ge0}D_{-j}(t)\le C_m(Y^2+Y/\sqrt n),\quad Y=|y|. \tag{7}
\]

Indeed the lower deletion has external forward input $W_{:,i}h_{a,i}$
of Euclidean norm $O(1)$; its actual velocity discrepancy is
$O(|c|/\sqrt n)$ in normalized state norm, and its output discrepancy
is $O(Y/\sqrt n)$. The upper deletion has additional lower velocity
\(\beta c_aW_{j,:}^\top\delta_{a,j}\), of normalized size
$O(Y|c|/\sqrt n)$, and missing output $O(Y/n)$. Summing the finitely
many sample contributions changes constants only. The inactive columns
coincide on retained indices and produce no state discrepancy.

For clarity, the following verifies why the full complex-source proof
also changes only constants before treating the new sphere variables.
Set

\[
 \ell=\log(en/\eta),\quad T=C_T\ell,\quad r=c/\sqrt\ell,
 \quad D=\{t:-r\le\Re t\le T+r,\ |\Im t|\le r\}.
\]

Fix a pole cap $b>0$, small enough depending on $d$. On stopped
domains with \(|\Im u_{a,i}|,|\Im z_{a,j}|\le2b\), anchor at real
time and integrate only along a vertical segment of length at most a
fixed small $r_0$. The algebraic complex version of (5) has uniformly
bounded operator norm: the last term uses the RMS norm of $k_a$,
not its coordinate maximum. Hence

\[
 |c(t)|\le CY e^{-\kappa\max(\Re t,0)},\quad
 \|w\|_\infty+\max_a\|\delta_a\|_\infty\le CY,
 \quad\|W\|_{\rm op}\le K+CY^2.                       \tag{8}
\]

The real interval of length $r_0$ before zero is handled by the same
short-interval bootstrap without decay. Differentiating (1) and the
forward pass gives

\[
 {\|k_a\|_2\over\sqrt n}\le CY,\quad
 {\|\dot u_a\|_2+\|\dot h_a\|_2+\|\dot z_a\|_2\over\sqrt n}
       \le CY|c|,
 \quad {\|\dot\delta_a\|_2+\|\dot k_a\|_2\over\sqrt n}\le C|c|.
                                                               \tag{9}
\]

Integrating the rank-one update yields each learned row/column norm
$O(Y^2/\sqrt n)$, and each learned entry $O(Y^2/n)$. Finite
differences on the short vertical segments, starting from (7), give
$D_c\le CY$ for all cavities. Residual feedback costs only $CD_c$:
the output discrepancy is $O(D_c/\sqrt n)$ while the residual-free
field has ordinary norm $O(\sqrt n)$. Thus no factor $e^{CT}$
is introduced.

Define $q_a=\sigma'(u_a)\odot k_a$, so
\(\dot h_a=\beta c_aq_a\). Stop the full model at pole caps $b$
and response caps

\[
 \max_a\|k_a\|_\infty=M,\qquad
 \max_a\|Wq_a\|_\infty=M,\qquad M=AY\sqrt\ell.
\]

Cavity stops use doubled pole and $k$ caps, without a $Wq$ cap.
The deterministic reinsertion estimates are

\[
 |k_{a,i}-W_{0,:,i}^\top\delta_a^{-i}|\le CY,
 \quad |(Wq_a)_j-W_{0,j,:}q_a^{-j}|\le C(Y+YM),          \tag{10}
\]

because \(\|q_a-q_a^{-j}\|_2\le C(Y+YM)\). Pole differences are
$O(Y)+O(\max|W_{0,ji}|)$. Consequently no cavity can stop before the
full stopped domain when $Y_*$ is sufficiently small.

Conditioning separately on each cavity's retained initialization leaves
the omitted mixer vector Gaussian with covariance $I/n$. The source
vectors \(\delta_a^{-i}\) and \(q_a^{-j}\) have RMS at most $CY$
and time-derivative RMS at most $CY(1+YM)$. On each cavity's own
stopped rectangle, a grid of mesh $n^{-3}/[C(1+YM)]$ has polynomial
cardinality in $n,T,\ell$. The Gaussian tail for each complex scalar
pairing is \(4\exp(-cu^2/Y^2)\). A union over the fixed $m$, the
$2n$ cavities and their grids gives pairings at most $C_GY\sqrt\ell$.
The reference is set to zero on failure of a retained initialization
condition, exactly as in `TWO_INPUT_COMPLEX_SOURCE.md`; a full-network
event is never included in this conditioning. The $O(YM)$ error in (10)
is absorbed by choosing $A$ large and then $Y_*$ small.

Finally

\[
 \dot z_a=\beta\sum_b c_b\delta_b(h_b^\top h_a/n)
                  +\beta c_aWq_a
\]

gives coordinate derivative $O(Y^2\sqrt\ell)$, as does \(\dot u_a\).
Vertical integration over $r=c/\sqrt\ell$ improves the pole caps.
All stopped caps therefore have strict margins, so holomorphic ODE
continuation reaches $D$ and a neighborhood of its closure. This is the
complete replacement of the training-source portion of the two-input
argument: every newly appearing sum has only $m$ terms, and \(\beta\)
is a fixed positive constant.

## 4. All sphere queries in fixed input dimension

For $d\ge2$, put $s=d-1$ and use the surjective periodic map
\(v:\mathbb R^s\to S^{d-1}\) given by

\[
 v_1=\cos\theta_1,\quad
 v_j=\Bigl(\prod_{k<j}\sin\theta_k\Bigr)\cos\theta_j
 \ (2\le j\le d-1),\quad
 v_d=\prod_{k<d}\sin\theta_k.
\]

For $d=2$ this reads \((\cos\theta_1,\sin\theta_1)\). On a fixed
complex polystrip its coefficients and every fixed number of derivatives
are bounded by constants depending on $d$. The redundancy and coordinate
singularities of this parameterization cause no difficulty: only a
surjective forward map and uniform approximation of its pullback are used.

Let $a_b=Ae_b$ for all $b\le d$, and define

\[
 b_\theta=\sum_{b=1}^dv_b(\theta)a_b,\quad
 h_\theta=\tanh b_\theta,\quad z_\theta=Wh_\theta,
 \quad g_\theta=\tanh z_\theta.
\]

Gaussian initial column bounds, the already proved training carrier caps,
and finite residual length imply, for the full solution and every row
cavity on its own stopped training domain,

\[
 \sum_{b\le d}\|a_b\|_2/\sqrt n\le C_d,\quad
 \max_{b,i}|a_{b,i}|\le C_d\sqrt\ell,\quad
 \max_{a\le m,i}|\Im a_{a,i}|\le Cb.                  \tag{11}
\]

The inactive columns are real and fixed. For \(|\Im\theta_j|\le r_\theta\),
the imaginary query first preactivation is bounded by
$C_d b+C_d\sqrt\ell r_\theta$. Choose $b$ first and then
\(r_\theta=c_\theta/\sqrt\ell\) sufficiently small. This gives a
fixed first-layer query pole margin before applying any top query gate.

Define the residual-free query derivative sources

\[
 q_{\theta,a}=\operatorname{sech}^2b_\theta\odot
                   v_a(\theta)\psi'(u_a)\odot k_a,
 \qquad \dot h_\theta=\beta\sum_a c_aq_{\theta,a}.
\]

For each angular index $j\le s$,
\(\partial_j h_\theta=\operatorname{sech}^2b_\theta\odot
\sum_b(\partial_jv_b)a_b\). Their RMS bounds are $CY$ and $C_d$,
respectively. Differentiation and (9), (11) give

\[
 \|\partial_tq_{\theta,a}\|_2/\sqrt n\le CY(1+YM),\quad
 \|\partial_jq_{\theta,a}\|_2/\sqrt n\le C_dY\sqrt\ell,
\]
\[
 \|\partial_t\partial_jh_\theta\|_2/\sqrt n
          \le C_dY^2\sqrt\ell,\qquad
 \|\partial_j\partial_kh_\theta\|_2/\sqrt n
          \le C_d\sqrt\ell.                              \tag{12}
\]

For example, a product of two angular preactivation derivatives is bounded
in RMS by their maximum times their RMS, hence $O(\sqrt\ell)$, not
$O(\ell)$. A row-deletion comparison gives

\[
 \|q_{\theta,a}-q_{\theta,a}^{-j}\|_2\le C_d(Y+YM),
 \quad\|\partial_kh_\theta-\partial_kh_\theta^{-j}\|_2
                                  \le C_dY(1+\sqrt\ell). \tag{13}
\]

The frozen inactive columns coincide exactly in these comparisons.
Condition on all of $A_0$ and the retained row-cavity initialization.
An independent Gaussian pairing argument on the $2+2s=2d$ real
coordinates of complex time and angles applies to the sources in (12).
A mesh $n^{-3}$ divided by a fixed polynomial in \(\ell\) has
cardinality \(n^{O_d(1)}\ell^{O_d(1)}\); its logarithm remains
$O_d(\ell)$. Equations (12) control interpolation, and (13) reinserts
the full row. The resulting estimates are

\[
 \max|Wq_{\theta,a}|+\max|W_0q_{\theta,a}|\le C_dY\sqrt\ell,
\]
\[
 \max|\partial_j(Wh_\theta)|+
 \max|\partial_j(W_0h_\theta)|\le C_d\sqrt\ell,
\]
\[
 \max|\partial_t(Wh_\theta)|+
 \max|\partial_t(W_0h_\theta)|\le C_dY\sqrt\ell\,|c(t)|. \tag{14}
\]

The learned row contribution uses its $O(Y^2/\sqrt n)$ Euclidean
bound. No query top derivative is used to prove (14). Starting from a
real time and real angle tuple, move vertically in time and then one
angular coordinate at a time. Equations (14) bound the imaginary top
preactivation by $C_dY^2c+C_ds c_\theta<1/4$ after reducing the
radii. Thus the query top gate is jointly holomorphic and bounded.
Starting at angle zero (a training direction), a real angular path of
length at most $2\pi s$, followed by the real-time path, bounds the
coordinates of $Wh_\theta,W_0h_\theta$ by $C_d\sqrt\ell$.
The time integral uses \(\int|c|\le CY\), not $T$.

The reverse source obeys

\[
 [(W-W_0)^\top\delta_a]_i
 =\beta\int_0^t\sum_b c_b(v)h_{b,i}(v)
                     {\delta_b(v)^\top\delta_a(t)\over n}\,dv.
\]

The real-anchor-plus-vertical integral is $O(Y^3)$ coordinatewise.
The training carrier bound therefore controls $W_0^\top\delta_a$.
We have proved that

\[
 h_\theta,\quad g_\theta,\quad W_0h_\theta,\quad
 \delta_a,\quad W_0^\top\delta_a\quad(1\le a\le m)       \tag{15}
\]

are bounded by $C_d\sqrt\ell$ and jointly holomorphic on a
neighborhood of $D\times\{\theta:|\Im\theta_j|\le c_\theta/\sqrt\ell\}$.
All angular dependence is periodic. For $d=1$, the sphere consists of
the two queries $+1,-1$; apply the same estimates to those two fixed
queries and take $s=0$. No angular approximation is needed.

## 5. Initial derivatives, tensor interpolation, and the exponent

Apply the finite initial-jet continuation construction of
`TWO_INPUT_STABLE_GEOMETRY.md` to each source (15), uniformly over the
complex angular polystrip. This lemma constructs approximate time nodes
from finite initial derivatives by a disk-to-rectangle conformal map and
then takes a Chebyshev interpolant. It gives time degree

\[
 p=O(\ell^{5/2})                                           \tag{16}
\]

at coordinate accuracy \(\epsilon=c_0n^{-1/2}\). All scalar operations
are identical on a paired source and its $W_0$ or $W_0^\top$ image.
The raw derivative order may be enormous, but it is finite and discarded.

For completeness, tensor angular interpolation adds no hidden exponential
in width. A function bounded by $M$ on an $s$-dimensional polystrip
of radius \(\rho=c_\theta/\sqrt\ell\) has Fourier coefficients at
multi-index $k\in\mathbb Z^s$ bounded by
$M e^{-\rho\sum_j|k_j|}$. This follows by shifting each contour in
the sign of its index. The sum of coefficients outside the cube
\(\max_j|k_j|\le L\) is at most

\[
 C_sM\rho^{-s}e^{-\rho L}.
\]

On the tensor equispaced grid of $2L+1$ nodes in each variable, each
Fourier mode aliases to one retained mode of modulus one on the real
torus. Thus twice this tail bounds interpolation error. Taking

\[
 L=C_d\rho^{-1}\log(C_dM/(\epsilon\rho^s))
       =O_d(\ell^{3/2})                                   \tag{17}
\]

suffices. Time approximation is first made uniformly on the complex
angular polystrip, where its error is $O(\epsilon)$; hence its
real-time values stay bounded there by $M+O(\epsilon)$. Apply the
angular tail estimate to this time polynomial. This avoids multiplying
a merely real-domain time error by a tensor interpolation norm.

The retained vector coefficient count for a query source is therefore

\[
 (p+1)(2L+1)^s
       =O_d\bigl(\ell^{5/2+3(d-1)/2}\bigr)
       =O_d\bigl(\ell^{(3d+2)/2}\bigr).                    \tag{18}
\]

Training-only sources use $p+1$ coefficients. Complex Fourier
coefficients may be split into real and imaginary parts; the sources are
real on real arguments and this changes dimensions by a fixed factor.

Let $S_1\subset\mathbb R^n$ contain the $h_\theta$ and
$W_0^\top\delta_a$ coefficient vectors, and let $S_2\subset\mathbb R^n$
contain those of $g_\theta,W_0h_\theta,\delta_a$. Include all $d$
columns of $A_0$, all initialized training $h_a(0)$, and their
forward images $W_0h_a(0)$, $g_a(0)$ in the appropriate spaces.
Identical scalar coefficient operations preserve exact pairings
$v,W_0v$ and $d,W_0^\top d$. Their dimensions satisfy

\[
 r_1,r_2\le C_{d,m}\ell^{(3d+2)/2}.                       \tag{19}
\]

The readout is coordinatewise $O(Y\epsilon)$-close to $S_2$, because
\(w=\beta\int\sum_a c_ag_a\) and the total residual length is $O(Y)$.
This integral establishes an approximation property in the proof; its
trajectory-dependent scalar coefficients are never supplied to setup.

## 6. Positive cubature and the complete runtime model

Choose bases $V,U$ with $V^\top V/n=I_{r_1}$, $U^\top U/n=I_{r_2}$.
Positive empirical cubature matching the constant and all symmetric basis
products gives selected original indices $I,J$ and positive masses
$D_1,D_2$, of total mass one, such that

\[
 V_I^\top D_1V_I=I,\quad U_J^\top D_2U_J=I,
 \quad N_i\le1+r_i(r_i+1)/2.                             \tag{20}
\]

The elementary construction repeatedly moves masses along an affine
dependence of the matched products until one mass becomes zero. It starts
from the empirical masses $1/n$, so feasibility requires no additional
assumption. Define

\[
 C_0=U^\top W_0V/n,\quad B_0=U_JC_0V_I^\top D_1,
 \quad B_0^*=D_1^{-1}B_0^\top D_2.                         \tag{21}
\]

The weighted basis maps are isometries, so \(\|B_0\|\le\|W_0\|\).
Whenever $v\in S_1,W_0v\in S_2$,
$B_0v_I=(W_0v)_J$; whenever $d\in S_2,W_0^\top d\in S_1$,
$B_0^*d_J=(W_0^\top d)_I$. In particular the initialized training
forward pass and its entire $m\times m$ Gram are preserved exactly.

The moving state is $A_C\in\mathbb R^{N_1\times d}$,
$B_C\in\mathbb R^{N_2\times N_1}$, $w_C\in\mathbb R^{N_2}$,
initialized as \((A_0)_I,B_0,0\). For any query use

\[
 h_C(x)=\tanh(A_Cx/\sqrt d),\quad g_C(x)=\tanh(B_Ch_C(x)),
 \quad f_C(x)=w_C^\top D_2g_C(x).
\]

At the training inputs define $c_{C,a}=y_a-f_C(x_a)$,
$\delta_{C,a}=w_C\odot\operatorname{sech}^2(B_Ch_C(x_a))$, and
$B_C^*=D_1^{-1}B_C^\top D_2$. The complete equations are

\[
 \dot A_C=\beta\sum_a c_{C,a}
 [\operatorname{sech}^2(A_Ce_a)\odot B_C^*\delta_{C,a}]e_a^\top,
\]
\[
 \dot B_C=\beta\sum_a c_{C,a}\delta_{C,a}h_C(x_a)^\top D_1,
 \qquad \dot w_C=\beta\sum_a c_{C,a}g_C(x_a).             \tag{22}
\]

Fixed data are the masses, labels, and the fixed structural constants.
The last $d-m$ columns of $A_C$ stay fixed and are still counted.
No $n$-dimensional arrays survive setup. Equations (19)--(20) give
$N_1,N_2=O(\ell^{3d+2})$, so the moving-plus-fixed count

\[
 dN_1+N_1N_2+N_2+(N_1+N_2)+m+O_{d,m}(1)
        \le C_{d,m}\ell^{6d+4}                            \tag{23}
\]

proves (3). Selected original indices need not be retained, since all
selected initial values are already stored; even retaining them does not
change the displayed real-coordinate order. The initialized operator and
Gram bounds prove that (22) independently fits and has the tails (6).

## 7. Source defects, own-residual comparison, and the endpoint

Define solely for the proof

\[
 B_R(t)=B_0+\beta\int_0^t\sum_a c_a(v)
                    \delta_a(v)_Jh_a(v)_I^\top D_1\,dv,
 \quad X_R=(u_1{}_I,\ldots,u_m{}_I,B_R,w_J).              \tag{24}
\]

The inactive first columns of its forward pass are \((A_0e_b)_I\).
For two real source vectors within coordinate error $O(\epsilon)$
of $S_i$, the empirical and selected weighted pairings differ by
$O(\epsilon)$: insert their approximants, use exact cubature on their
pairing, and bound the remaining terms in weighted/empirical RMS.
Total mass one and equality of approximant norms give constants independent
of the minimum mass. This applies to the readout approximation as well.

The paired frozen actions in (21), the pairing estimate, and the finite
residual length yield, uniformly for $0\le t\le T$ and all real angles,

\[
 \|B_Rh_\theta{}_I-z_\theta{}_J\|_{D_2}\le C\epsilon,
 \quad\|B_R^*\delta_a{}_J-(W^\top\delta_a)_I\|_{D_1}\le C\epsilon,
\]
\[
 |w_J^\top D_2g_\theta{}_J-f_n(t,\sqrt d\,v(\theta))|
                                      \le C\epsilon.       \tag{25}
\]

For the first learned defect, integrate \(\beta c_a\delta_{a,J}\)
against the error in the two pairings of $h_a(v)$ and $h_\theta(t)$.
For the reverse learned defect, integrate \(\beta c_bh_{b,I}\) against
the pairing error between \(\delta_b(v)\) and \(\delta_a(t)\).
These are precisely the two interaction directions of the same trained
matrix, and both are controlled. A factor $m$ only changes the constant.

The selected reference lies in the real small tube: its mixer increment
is $O(Y^2)$, and (25) bounds its selected carrier in weighted norm
by $CY+C\epsilon$, giving regular-coordinate increment
$O(Y^2+Y\epsilon)$. Relative to the residual-free field and output
of (22), it satisfies

\[
 \dot X_R=\sum_a c_aV_a(X_R)+e(t),\qquad
 c=y-F(X_R)+d(t),
\]
\[
 \|e(t)\|\le C\epsilon|c(t)|,\qquad |d(t)|\le C\epsilon. \tag{26}
\]

The $u$ error is the reverse defect; the $w$ error is the forward
gate defect; the $B$ error is the difference of top gates times bounded
readout. The observation error is the forward gate defect plus the last
line of (25). The compressed trajectory and (24) share their initial
state, and both actual residual paths have total length $O(Y)$.
Section 2 therefore gives

\[
 \sup_{t\le T}\|X_C(t)-X_R(t)\|\le C\epsilon.            \tag{27}
\]

The real sphere query maps are Lipschitz as proved after (6). Equations
(25), (27) give (2) through $T$. Choose $C_T$ so that the independent
query tails of the dense and compressed systems at $T=C_T\ell$ are
at most \(\epsilon\). Comparing each later query value with its own
value at $T$ adds $O(\epsilon)$, including at the fitted endpoint.
Both systems continue with their own physical-time equations; neither is
frozen at $T$. This completes the proof of the theorem.

## 8. Feature learning and the nonorthogonal boundary

The width-independent two-layer feature-motion proof in
`TWO_INPUT_FEATURE_LEARNING.md` extends to this orthogonal $m$-input
model with the following precise changes. The initialized truncated-feature
matrix $M_{ab,n}$ defined in that note becomes $m\times m$, and its
limit remains \(\tau I_m\) with \(\tau>0\), by independence and
oddness of the $m$ initialized Gaussian columns. The first-feature Gram
tends to \(qI_m\). For each $a$, the matrix

\[
 H_{a,bc,n}={1\over n}\sum_j
 g_{b,0,j}g_{c,0,j}\operatorname{sech}^4z_{a,0,j}
\]

has a diagonal positive definite limit: its $a$-entry is
\(\mathbb E[\tanh^2Z\operatorname{sech}^4Z]\), and every other
entry is \(\mathbb E\tanh^2Z\,\mathbb E\operatorname{sech}^4Z\),
with $Z\sim N(0,q)$. There are only finitely many matrices. All their
gaps are uniform over label directions.

Writing $v=\sum_a y_ag_{a,0}$, the readout expansion is now
\(w(t)=\beta tv+O(Yt^2)\) in RMS. The bounded first-feature test in
that proof therefore has leading term
\(\beta^2t^2y^\top M_ny/2\). Its remainder is still
$O(Y^2t^3+Y^4t^4)$. The second-feature scalar test
\(\sum_a y_av^\top(g_a(t)-g_{a,0})/n\) has derivative with leading
nonnegative terms

\[
 \beta^2t\left\|{1\over n}\sum_a y_a
  (v\odot\operatorname{sech}^2z_a)h_a^\top\right\|_F^2
 +\beta^2t\sum_a y_a^2
  {\|\operatorname{sech}^2a_a\odot W^\top
      (v\odot\operatorname{sech}^2z_a)\|_2^2\over n},
\]

and error $O(Y^4t^2)$. The tensor Gram argument lower-bounds the
first term by $ctY^4$, independent of label signs. Choosing one fixed
small $t_*>0$ proves that the tuple RMS displacements of both hidden
training-feature layers lie between $cY^2$ and $CY^2$. Cubature
preserves their squared displacements up to $O(\epsilon)$, and (27)
transfers them to the weighted model for each fixed nonzero $y$ and
sufficiently large width. These claims concern a fixed positive time;
no separate lower bound on endpoint feature displacement is asserted.

For general fixed normalized inputs $v_a=x_a/\sqrt d$, let
$G_{ab}=v_a^\top v_b$. The exact first-preactivation equation becomes

\[
 \dot a_a=\beta\sum_b c_bG_{ab}
                       \operatorname{sech}^2a_b\odot k_b.
\]

The separate transform then produces

\[
 \dot u_a=\beta\sum_b c_bG_{ab}
 {\operatorname{sech}^2a_b\over\operatorname{sech}^2a_a}\odot k_b.
                                                               \tag{28}
\]

These real gate ratios are unbounded. The uniform transformed Jacobian,
cavity comparison, and resulting independent Gaussian source proof used
above do not follow from (28). For two nonorthogonal noncollinear inputs,
the first-layer vector fields \(X_b(p)=\operatorname{sech}^2(v_b^\top p)v_b\)
have bracket

\[
 DX_2X_1-DX_1X_2
 =G_{12}[\tanh'(v_1^\top p)\tanh''(v_2^\top p)v_2
        -\tanh'(v_2^\top p)\tanh''(v_1^\top p)v_1],
\]

generically nonzero. Thus simultaneous straightening to constant coordinate
directions cannot repair (28). This is a proof-route obstruction, not a
nonexistence theorem for compression.

Real small-label fitting alone extends to any fixed input list whose initial
readout Gram has a fixed positive gap: direct estimates on $A-A_0$, $W-W_0$
and $w$ give the same $O(Y^2),O(Y^2),O(Y)$ bounds, and the tangent
Gram remains positive semidefinite and dominates the readout Gram. This
does not supply the missing comparison/source theorem. A statement for
arbitrary lists and arbitrary labels would additionally fail without a
nondegeneracy condition: duplicated inputs with distinct labels cannot fit,
and antipodal inputs require opposite labels for the bias-free odd network.
No general nonorthogonal compression theorem is claimed here.

The orthogonal theorem, total stored-coordinate count, initialization-only
provenance, own residuals, shared physical time, sphere norm, and fitted
endpoint are all included in the proved claim. Constants and the small-label
radius can depend on fixed $m,d$; neither may grow with width. Increasing
the input dimension with width is outside this theorem.
