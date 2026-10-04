# Complex physical-time sources for two orthogonal training inputs

2026-10-03. Internally reconstructed research proof. This is a finite-network estimate
for the actual canonical dense model. Its new deterministic input is the
real all-time cavity comparison in `TWO_INPUT_STABLE_GEOMETRY.md`.
The inverse-coordinate strip is proved in `COMPLEX_ACTIVITY_ROUTE.md`.
No population approximation, clipped algorithm, or trained-path input is
assumed. Complete reconstructions are recorded in
`TWO_INPUT_COMPLEX_SOURCE_CHECK.md` and the source-theorem portion of
`TWO_INPUT_CANONICAL_COMPRESSION_CHECK.md`. This is not a promotion review.

## 1. Statement and physical equations

Let $x_1=\sqrt2e_1,x_2=\sqrt2e_2$, with fixed labels
$y=(y_1,y_2)\in\mathbb R^2$. Write $Y=|y|>0$. The two hidden layers
have width $n$, $A_0$ has iid $N(0,1)$ entries, $W_0$ has iid
$N(0,1/n)$ entries independently, and $w_0=0$. For a circle query put

\[
 h_\theta=\tanh(a_1\cos\theta+a_2\sin\theta),\quad
 g_\theta=\tanh(Wh_\theta),\quad f_\theta=w^\top g_\theta/n,
 \qquad a_a=Ae_a.
\]

Training features $h_a,g_a$ are the respective angles $0,\pi/2$.
Define $z_a=Wh_a$, $\delta_a=w\odot\operatorname{sech}^2z_a$,
$k_a=W^\top\delta_a$, and $c_a=y_a-f_a$. The loss is
$\tfrac12\sum_a(f_a-y_a)^2$, and the manuscript mobilities are
$(n,1,n)$. Its exact physical equations, including $2/m=1$, are

\[
 \dot a_a=c_a\operatorname{sech}^2a_a\odot k_a,\qquad
 \dot W=\frac1n\sum_{b=1}^2c_b\delta_bh_b^\top,\qquad
 \dot w=\sum_{b=1}^2c_bg_b.                                      \tag{1}
\]

Set $u_a=\Psi(a_a)$, where $\Psi(a)=a/2+\sinh(2a)/4$, and
$\sigma=\tanh\circ\Psi^{-1}$. With $H=\sqrt nW$,

\[
 \dot u_a=c_a k_a,\quad h_a=\sigma(u_a),\qquad
 \dot H=\frac1{\sqrt n}\sum_b c_b\delta_bh_b^\top,
 \quad \dot w=\sum_b c_bg_b.                                   \tag{2}
\]

The inverse $\Psi^{-1}$ is holomorphic on $|\Im u|<1/4$;
$\sigma$ and every fixed number of its derivatives are bounded on
strict substrips. These facts follow from the explicit injectivity and
boundary calculation in the one-input complex note, independently of
the number of training inputs.

Fix $B>0$ and a failure probability $0<\eta<1/2$. There are constants
$Y_*,c,C>0$, independent of $n$ and of the chosen label vector, such that
the following holds for every fixed $0<Y\le Y_*$. Put

\[
 \ell=\log(en/\eta),\qquad T=B\ell,\qquad
 r=c/\sqrt\ell,\qquad r_\theta=c_\theta/\sqrt\ell.
                                                                  \tag{3}
\]

For sufficiently large $n$ (the threshold can depend on $Y,B,\eta$),
with probability at least $1-\eta$ the actual source functions extend
jointly holomorphically to a neighborhood of

\[
 D=\{-r\le\Re t\le T+r,\ |\Im t|\le r\},\qquad
 |\Im\theta|\le r_\theta.                                    \tag{4}
\]

Uniformly there, the coordinate magnitudes of

\[
 h_\theta,\ g_\theta,\ W_0h_\theta,\ \delta_1,\delta_2,
 \ W_0^\top\delta_1,\ W_0^\top\delta_2                         \tag{5}
\]

are at most $C\sqrt\ell$. The activation coordinates are in fact bounded
by a fixed constant, and $|w_j|+|\delta_{a,j}|\le CY$.
Constants may depend on the fixed $B$, not on width or elapsed time.
The construction below does not impose signs or equality on $y_1,y_2$.

## 2. Real initialization event, fitting, and cavity comparison

Choose a fixed large $K$ and a fixed positive $\gamma$ so that the
canonical initialization satisfies, with exponentially small failure,

\[
 \|W_0\|_{\rm op}\le K,\qquad
 G_0=\big(g_{a,0}^\top g_{b,0}/n\big)_{a,b=1}^2\succeq\gamma I,
 \qquad \frac{\|a_{1,0}\|_2+\|a_{2,0}\|_2}{\sqrt n}\le C.
                                                                  \tag{6}
\]

Here the Gram gap is a conclusion about the specified Gaussian law.
Indeed the first-layer empirical covariance of the two independent tanh
Gaussian columns concentrates near $qI_2$, where
$q=\mathbb E\tanh^2 Z>0$. Conditional on those columns, the rows of
$(z_{1,0},z_{2,0})$ are independent Gaussian pairs with that covariance.
At covariance $qI_2$ their tanh second-moment matrix is $gI_2$ for
$g=\mathbb E\tanh^2(\sqrt q Z)>0$. This matrix depends continuously
on the covariance, by a Gaussian representation and bounded convergence.
Bounded-variable exponential concentration, first on the empirical lower
covariance and then on the three upper Gram entries, proves (6).
The Gaussian operator bound follows from finite sphere nets; the Gaussian
square moment generating function proves the RMS bound.

Gaussian entry tails also give, with the allocated failure probability,

\[
 \max_{i,j}|W_{0,ji}|\le C\sqrt{\ell/n},\qquad
 \max_{a,i}|a_{a,0,i}|+\max_{a,j}|z_{a,0,j}|\le C\sqrt\ell.
                                                                  \tag{7}
\]

Each singleton cavity deletes one lower column and its two read-in
coordinates, or one upper row and its readout coordinate. It retains the
normalization $n$ and evolves with its **own** residuals and fixed labels.
Its initial operator norm is at most $K$. A lower deletion changes each
initial top feature in Euclidean norm by at most $K$, hence changes its
normalized Gram by $O(n^{-1/2})$. An upper deletion changes that Gram by
$O(n^{-1})$. Thus every cavity has a fixed initial gap, say $\gamma/2$,
on (6), for all sufficiently large widths.

The real weighted fitting calculation in the stable-geometry note applies
to the full model and all cavities. With fixed $\kappa>0$ and small
$Y_*$ it gives, for $t\ge0$,

\[
 |c(t)|\le Y e^{-\kappa t},\qquad
 \int_0^\infty|c(t)|\,dt\le CY,
\]
\[
 \|w(t)\|_\infty\le CY,\quad
 \|W(t)-W_0\|_F\le CY^2,\quad
 \sum_a\|u_a(t)-u_a(0)\|_2/\sqrt n\le CY^2.                  \tag{8}
\]

All these statements hold with each cavity's own residual vector.
Write the retained full/cavity difference on the unnormalized scale as

\[
 D_c(t)=\sum_a\|u_{a,\mathrm{ret}}(t)-u_a^c(t)\|_2
          +\|H_{\mathrm{ret}}(t)-H^c(t)\|_F
          +\|w_{\mathrm{ret}}(t)-w^c(t)\|_2.
\]

The real singleton comparison established in that note gives

\[
 \sup_{t\ge0}D_{-i}(t)\le CY,
 \qquad
 \sup_{t\ge0}D_{-j}(t)\le C(Y^2+Y/\sqrt n).                 \tag{9}
\]

The proof is a dissipative comparison of accumulated residual differences,
not a frozen-residual cavity. In particular the conditional independence
of each cavity from its omitted Gaussian column or row is exact.

For real times in a fixed short negative interval $[-r_0,0]$, ordinary
finite-difference estimates in (2), starting at zero, give the same looser
bounds $D_c\le CY$ and the real bounds in (8) without decay, with enlarged
constants. The initial full-to-cavity forward column discrepancy has norm
$O(1)$, but is multiplied by residual $O(Y)$ in these physical equations.
All normalized state bounds follow by an elementary short-interval
bootstrap. No bound for arbitrarily negative physical time is needed.

## 3. Complex estimates from short vertical segments

Fix $b=1/64$. On any stopped complex domain where every relevant
$|\Im u_{a,i}|,|\Im z_{a,j}|\le2b$, the gates and their first few
derivatives are bounded. We claim the following bounds throughout that
domain, provided its imaginary height is at most a sufficiently small
fixed $r_0$:

\[
 \|W\|_{\rm op}\le K+C Y^2,\quad
 \|w\|_\infty+\|\delta_a\|_\infty\le CY,
 \quad |c(t)|\le CY e^{-\kappa\max(\Re t,0)},                 \tag{10}
\]
\[
 \frac{\|k_a\|_2}{\sqrt n}\le CY,
 \frac{\|\dot u_a\|_2+\|\dot h_a\|_2+\|\dot z_a\|_2}{\sqrt n}
       \le C Y|c|,
 \quad\frac{\|\dot\delta_a\|_2+\|\dot k_a\|_2}{\sqrt n}
       \le C|c|.                                             \tag{11}
\]

These estimates use the real-time anchor $t_0=\Re t$, followed by the
vertical segment from $t_0$ to $t$. They do not integrate a complex
Gronwall constant over length $T$.

To verify them, direct differentiation gives $\dot c=-K(t)c$, where
the algebraic complex matrix is

\[
 K_{ab}=g_a^\top g_b/n
  +(\delta_a^\top\delta_b/n)(h_a^\top h_b/n)
  +\mathbf1_{a=b}\frac1n\sum_i\sigma'(u_{a,i})k_{a,i}^2.
                                                                  \tag{12}
\]

All transposes and squares in the equations are algebraic; estimates use
ordinary complex norms. On an operator tube and a readout bound $CY$,
(12) has operator norm at most a fixed constant. Along the short vertical
segment, therefore, $|c|\le e^{Cr_0}|c(t_0)|$. Integrating (2) gives
a readout increment at most $Cr_0|c(t_0)|$ and a matrix increment at
most $Cr_0Y|c(t_0)|$. Start with operator cap $K+1$ and a sufficiently
large fixed readout cap times $Y$; choose $r_0$ small and $Y_*$ small
to improve both caps strictly. This proves (10). The same integration
gives the normalized read-in increment and excludes state escape on a
pole-safe segment. Substitution into (1)–(2), followed by the chain rule
for $\delta_a,k_a$, proves (11). For instance
$\dot\delta_a=\dot w\odot\operatorname{sech}^2z_a
+w\odot\tanh''z_a\odot\dot z_a$.

The learned rows and columns have the stronger estimates

\[
 \|W_{:,i}-W_{0,:,i}\|_2+
 \|W_{j,:}-W_{0,j,:}\|_2\le CY^2/\sqrt n,
 \quad \max_{i,j}|W_{ji}-W_{0,ji}|\le CY^2/n.                \tag{13}
\]

Indeed integrate each rank-one coordinate along the real anchor path and
then vertically, using $\int|c|\le CY$ and $|\delta_{a,j}|\le CY$.

For a cavity/full comparison on a common pole-safe complex domain, use the
same real anchor and (9). The physical vector fields have a fixed
finite-difference constant in the unnormalized $(u_1,u_2,H,w)$ norm.
To see the feedback part explicitly, on that scale

\[
 |\Delta f_a|\le C\big(D+Y\|e_a^z\|_2\big)/\sqrt n
                       +CY/n,                               \tag{14}
\]

where the last term is present only for an upper deletion and
$e_a^z=W_{:,i}h_{a,i}$ only for a lower deletion. The residual-free
field has norm $C\sqrt n$, so multiplying its norm by (14) costs
$CD+CY\|e_a^z\|_2+CY/\sqrt n$. Differences with fixed residual
cost $C|c|D+C|c|\|e_a^z\|_2$; a deleted upper row has additional
lower forcing $O(Y|c|)$. Since $\|e_a^z\|_2\le C$ and $|c|\le CY$,
Gronwall on a vertical segment of length at most $r_0$ yields

\[
 D_c(t)\le CY                                                   \tag{15}
\]

for both deletion types, uniformly in the real anchor and hence in $T$.
All scalar finite differences use convex safe strips of their endpoint
preactivations, not an unjustified pole-safe parameter-space segment.

Let $\xi_i=W_{0,:,i}$ and $\xi_j^\top=W_{0,j,:}$. Equations
(10), (13), (15) imply the reinsertion bounds

\[
 |k_{a,i}-\xi_i^\top\delta_a^{-i}|\le CY,\qquad
 \|k_{a,\mathrm{ret}}-k_a^c\|_2\le CY.                       \tag{16}
\]

For example the first expression is bounded by
$\|\xi_i\|_2\|\delta_a-\delta_a^{-i}\|_2
+\|W_{:,i}-\xi_i\|_2\|\delta_a\|_2$;
the response difference is $O(Y)$, including the direct lower-column
forward discrepancy multiplied by the readout. The second expression
also includes the omitted row's $\xi_j\delta_{a,j}$ when applicable.
Pole differences satisfy

\[
 \|u_{a,\mathrm{ret}}-u_a^c\|_\infty\le CY,\qquad
 \|z_{a,\mathrm{ret}}-z_a^c\|_\infty
       \le CY+C\max|W_{0,ji}|+CY^2/n,                        \tag{17}
\]

with the entry term needed only for lower deletion.

## 4. Stops and conditional Gaussian source estimates

Define the lower response without its residual coefficient by
$q_a=\sigma'(u_a)\odot k_a$. Thus $\dot h_a=c_aq_a$ exactly;
there is no division by a possibly zero residual. Fix a large constant
$A$ and set $M=L=AY\sqrt\ell$. Stop the full continuation on scaled
rectangles $\lambda D$, $0<\lambda\le1$, at the first equality in

\[
 \max|\Im u_a|=b,\quad \max|\Im z_a|=b,
 \quad \max|k_a|=M,\quad \max|Wq_a|=L.                        \tag{18}
\]

Each singleton cavity has its own stop with pole caps $2b$ and carrier
cap $2M$, with no cap on $W^cq_a^c$. At zero readout, $k_a=q_a=0$,
so all continuations start. The operator/readout estimates in Section 3
and the fixed pole margins give finite coordinate bounds, and holomorphic
ODE uniqueness patches local solutions. No other state blow-up can occur
before a cap; bounded derivatives on compact subdomains supply boundary
limits and continuation whenever caps have strict margins.

Choose $Y_*$ sufficiently small. Equations (16)–(17), on every common
prefix, imply all cavity pole values are strictly below $2b$ and its
carrier below $M+CY<2M$, for large $n$. Consequently no cavity can stop
before the full model. This uses a common-prefix argument, not a presumed
cavity survival event.

For a row cavity, (15)–(16) and its carrier cap give

\[
 \|q_a-q_a^{-j}\|_2
 \le C\|k_a-k_a^{-j}\|_2
       +C\max|k_a^{-j}|\|u_a-u_a^{-j}\|_2
 \le C(Y+YM).                                                \tag{19}
\]

Combining (13), (19) gives

\[
 |(Wq_a)_j-\xi_j^\top q_a^{-j}|\le C(Y+YM).                  \tag{20}
\]

The independent cavity source vectors are $v=\delta_a^{-i}$ for a
column and $v=q_a^{-j}$ for a row. On each cavity's own stopped domain,

\[
 \sup\|v\|_2/\sqrt n\le CY,
 \qquad\sup\|\dot v\|_2/\sqrt n\le CY(1+YM).               \tag{21}
\]

For $q_a$, differentiate it using (11): the term
$\sigma''(u_a)\dot u_a k_a$ has RMS at most $CY^2M$, and
$\sigma'(u_a)\dot k_a$ has RMS at most $CY$.

Condition on the real $A_0$ and on all retained initialization for that
cavity. Its stop scale and all reference values are then deterministic;
the omitted vector remains $N(0,I_n/n)$. Set the reference identically
zero if that cavity's retained operator or Gram condition fails. For each
fixed complex source value the Gaussian scalar tail is

\[
 \Pr\{|\xi^\top v|>u\mid\text{retained initialization}\}
       \le4\exp[-c u^2/Y^2].                                \tag{22}
\]

Parameterize the stopped domain by $t=\lambda_c z$, $z\in D$.
A rectangular grid of mesh at most $n^{-3}/[C(1+YM)]$ has cardinality
polynomial in $n,T,\ell$. Equation (21) and $\|\xi\|_2\le K$
bound interpolation error by $CYn^{-5/2}$. The domain and grid values
depend only on retained initialization. Union (22) over the grids, sample
indices and $2n$ cavities; since $T=B\ell$, their logarithmic
cardinality is $O_B(\ell)$. A sufficiently large fixed Gaussian threshold
therefore gives, outside the allocated failure probability,

\[
 \max_{a,i}\sup|\xi_i^\top\delta_a^{-i}|\le C_GY\sqrt\ell,
 \qquad
 \max_{a,j}\sup|\xi_j^\top q_a^{-j}|\le C_GY\sqrt\ell.
                                                                  \tag{23}
\]

This tail is never conditioned on a full-network stopping event. The
initialized full Gram and operator events are intersected afterward, and
then ensure that every needed nonzero reference is available throughout
the full stopped domain. Dependence of fixed grid constants on $A$ is
absorbed by choosing the Gaussian threshold first, $A$ afterward, and
then increasing the sufficiently-large-width threshold.

From (16), (20), (23),

\[
 \max|k_a|\le C_GY\sqrt\ell+CY,
 \qquad\max|Wq_a|\le C_GY\sqrt\ell+CY+CYM.                  \tag{24}
\]

Choose $A$ large and then $Y_*$ small. Since $CYM/L=CY$, these
improve both response caps by a fixed factor, say to $M/2,L/2$.
The exact forward derivative is

\[
 \dot z_a=\sum_b c_b\delta_b(h_b^\top h_a/n)+c_aWq_a.       \tag{25}
\]

It follows that $\max|\dot u_a|+\max|\dot z_a|\le CY^2\sqrt\ell$.
At a complex point, integrate these derivatives vertically from its real
anchor. With $r=c/\sqrt\ell$ and fixed small $c$, both imaginary
parts are strictly below $b/2$. All four full caps now have strict
margins, so the continuation reaches $D$ and a neighborhood of its closure.

This proves the training-source strip on the logarithmically long physical
interval. The constant does not accumulate an $e^{CT}$ factor: real
feedback comparison and local vertical continuation serve different roles.

## 5. Circle-query continuation

The initialized bounds (6)–(7), the carrier caps, and integration first
along real physical time then vertically give, for the full model and all
row cavities on their own stopped domains,

\[
 \frac{\|a_1\|_2+\|a_2\|_2}{\sqrt n}\le C,
 \quad\max_{a,i}|a_{a,i}|\le C\sqrt\ell,
 \quad\max_{a,i}|\Im a_{a,i}|\le4b.                         \tag{26}
\]

Here $\dot a_a=c_a(\Psi^{-1})'(u_a)k_a$, and the real residual
integral is $O(Y)$; this is why the coordinate bound does not grow with
$T$. For complex angle, the query first preactivation
$b_\theta=a_1\cos\theta+a_2\sin\theta$ therefore has imaginary
part at most $8b\cosh|\Im\theta|+C\sqrt\ell\sinh|\Im\theta|$.
With $b=1/64$ and sufficiently small $c_\theta$, this is less than
$1/4$. All first query gates are thus bounded before any top query gate
is evaluated.

Define the residual-free query response vectors

\[
 q_{\theta,a}=
 \operatorname{sech}^2b_\theta\odot e_a(\theta)
                      (\Psi^{-1})'(u_a)\odot k_a,
 \qquad e_1(\theta)=\cos\theta,\quad e_2(\theta)=\sin\theta.
                                                                  \tag{27}
\]

Then $\dot h_\theta=\sum_a c_a q_{\theta,a}$, while
$\partial_\theta h_\theta=\operatorname{sech}^2b_\theta
\odot(-a_1\sin\theta+a_2\cos\theta)$. Their RMS bounds are
$CY$ and $C$, respectively. The derivatives needed for interpolation
have bounds polynomial in $\ell$:

\[
 \|\partial_tq_{\theta,a}\|_2/\sqrt n\le CY(1+YM),\quad
 \|\partial_\theta q_{\theta,a}\|_2/\sqrt n\le CY\sqrt\ell,
\]
\[
 \|\partial_t\partial_\theta h_\theta\|_2/\sqrt n
       \le CY^2\sqrt\ell,
 \qquad\|\partial_\theta^2h_\theta\|_2/\sqrt n\le C\sqrt\ell.
                                                                  \tag{28}
\]

These follow by differentiating the displayed formulas: derivatives of
$\Psi^{-1}$ and the first gate are bounded, $k_a$ has RMS $CY$
and maximum $2M$, $\dot k_a$ has RMS $C|c|$, and the first
preactivation and angular derivative have maximum $C\sqrt\ell$
and bounded RMS. Bounds may harmlessly be enlarged by fixed constants.

The row-deletion differences are

\[
 \|q_{\theta,a}-q_{\theta,a}^{-j}\|_2\le C(Y+YM),\qquad
 \|\partial_\theta h_\theta
                -\partial_\theta h_\theta^{-j}\|_2
       \le CY(1+\sqrt\ell).                                \tag{29}
\]

Use (15)–(16), bounded inverse derivatives, and the first-preactivation
safe strip to prove the first inequality. In the second, a gate difference
multiplies a cavity angular preactivation of maximum $C\sqrt\ell$;
the direct angular preactivation difference is $O(Y)$ in Euclidean norm.

Repeat the conditional Gaussian argument on the cavity stopped rectangle
times one angular period, using the four real variables of complex $t$
and $\theta$. Work conditionally on the good initial $A_0$ RMS and
coordinate-maximum event in (6)–(7); it depends only on retained data for
a row cavity. Set the query reference to zero when this event fails, as
for the retained operator and Gram events. No event involving an omitted
Gaussian row is used to define or condition its reference. A mesh
$n^{-3}$ divided by a sufficiently large fixed
polynomial in $\ell$ controls interpolation by (28). Its cardinality
is polynomial in $n,T,\ell$. Sources $q_{\theta,a}^{-j}$ and
$\partial_\theta h_\theta^{-j}$ give independent Gaussian pairing
bounds $CY\sqrt\ell$ and $C\sqrt\ell$. Reinsert the actual row
using (13), (29), obtaining

\[
 \max_j|(Wq_{\theta,a})_j|
    +\max_j|(W_0q_{\theta,a})_j|\le CY\sqrt\ell,
\]
\[
 \max_j|\partial_\theta(Wh_\theta)_j|
    +\max_j|\partial_\theta(W_0h_\theta)_j|\le C\sqrt\ell.
                                                                  \tag{30}
\]

The learned rank-one derivative plus (27), (30) gives

\[
 \max|\partial_t(Wh_\theta)|
 +\max|\partial_t(W_0h_\theta)|
       \le CY\sqrt\ell\,|c(t)|.                            \tag{31}
\]

All estimates precede application of the query top tanh. Starting at real
time and angle, integrate first vertically in time, then vertically in
angle. Equations (30)–(31) bound the imaginary top preactivation by
$C Y^2c+C c_\theta$, which is below $1/4$ after reducing the two
fixed radii. Thus $g_\theta$ is jointly holomorphic and bounded.
The coordinate bounds for $Wh_\theta,W_0h_\theta$ follow by integrating
from the known initial training preactivation around one real angular
period and along real time: the latter integral uses (31) and
$\int_0^\infty|c|\le CY$, not the length $T$.

Finally, the training reverse source satisfies

\[
 [(W(t)-W_0)^\top\delta_a(t)]_i
 =\int_0^t\sum_b c_b(v)h_{b,i}(v)
               \frac{\delta_b(v)^\top\delta_a(t)}n\,dv.
                                                                  \tag{32}
\]

Integrate along the real-anchor-plus-vertical path. Bounded first gates,
response RMS $CY$, and residual integral $CY$ make this correction
coordinatewise $O(Y^3)$. The already proved carrier bound therefore gives
the bound for $W_0^\top\delta_a$ in (5).

Allocate fixed fractions of $\eta$ to (6)–(7), the training Gaussian
grids, and the query grids. Replacing $\ell$ by $\log(Cen/\eta)$
only changes fixed constants. This completes the source theorem.

## 6. Scope and checking obligations

The new ingredient relative to the one-input proof is the real all-time
comparison with autonomous cavities, followed by short vertical complex
comparisons. The positive Gram gap and small total residual activity
control differing feedback histories without commuting the two input
updates. All labels are fixed independently of width, and their signs
never enter an estimate.

The source theorem itself supplies neither cubature nor a compressed
algorithm. Those require the separately constructed finite source space
and own-feedback comparison. The theorem presently concerns the orthogonal
two-input pair; no nonorthogonal extension is claimed. The recorded full
checks explicitly reconstruct the real cavity comparison, vertical
feedback normalization, independent stopped Gaussian domains, and query
top-gate ordering. Subsequent status and typographical edits are recorded
against their revised hashes in the coordinator check.
