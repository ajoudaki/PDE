## 8. Frozen quadratic reduction and joint initial layers

The results in Sections 8–9 concern one sample, `d=m=1`, `x_1=y_1=1`,
and two hidden layers. They use **order-one stored readout initialization**,
not the small stored readout used in the nonlinear limit theorems. They
separate a joint width/step obstruction for a frozen-bottom quadratic model
from a finite-width classical ReLU obstruction and a positive local
compactness theorem for actual ReLU Euler outputs. None replaces a theorem
about genuinely nonlinear training on correlated data.

Write `u=W^(1)`, `W=W^(2)` and `a=W^(3)` for finite arrays of sizes `n`,
`n` by `n`, and `n`. Thus

\[
 h^{(1)}=\phi(u),\qquad z^{(2)}=Wh^{(1)},\qquad
 h^{(2)}=\phi(z^{(2)}),\qquad f_n=a^Th^{(2)}/n.
\]

In Sections 8–9 the loss is the **half-square loss**
\(\ell_n=(f_n-1)^2/2\), and the residual remains \(r_n=f_n-1\).
The mobilities of the three stored blocks are \((n,1,n)\). Time is the
physical clock for this half loss. For the book's full one-sample squared
loss the same trajectories run twice as fast: an Euler step \(\eta\) for
the full loss equals a step \(2\eta\) here.

### 8.1 Exact frozen-feature reduction and arbitrary joint steps

First fix any deterministic bottom feature vector \(h^{(1)}\in\mathbb R^n\)
and train only \(W,a\), using the top activation \(\phi(z)=cz^2\), where
\(c=1/\sqrt3\). Put

\[
 Q=\frac{\|h^{(1)}\|_2^2}{n},\qquad z=Wh^{(1)},\qquad
 f_n=\frac c n\sum_{i=1}^n a_i z_i^2.
\]

The parameter derivatives are

\[
 \frac{\partial f_n}{\partial a_i}=\frac c n z_i^2,
 \qquad
 \frac{\partial f_n}{\partial W_{ij}}=
       \frac{2c}{n}a_i z_i h_j^{(1)}.
\]

Consequently an exact simultaneous raw Euler step of size \(\eta>0\),
with \(s=\eta(1-f_n)=-\eta r_n\), gives the closed update

\[
 a_i^+=a_i+cs z_i^2,\qquad
 z_i^+=z_i+2cQs a_i z_i.                              \tag{8.1}
\]

Indeed \(W^+=W+(2cs/n)(a\odot z)(h^{(1)})^T\), and multiplying by the
unchanged \(h^{(1)}\) gives the second equation. Both right sides use the
same pre-update state; there is no continuous-flow approximation in
(8.1). The raw kernel for the two trained blocks is also exactly

\[
 K_n=\frac{c^2}{n}\sum_i z_i^4+
            \frac{4c^2Q}{n}\sum_i a_i^2z_i^2.          \tag{8.2}
\]

The first term is \(n\|\nabla_a f_n\|_2^2\), and the second is
\(\|\nabla_Wf_n\|_F^2\). Thus the associated smooth finite flow satisfies
\(\dot f_n=(1-f_n)K_n\) and \(\dot\ell_n=-(1-f_n)^2K_n\).
These identities hold for every finite frozen vector, including \(Q=0\).
They assert neither a discrete energy inequality nor population convergence.

For the probabilistic theorem, specialize to

\[
 h_j^{(1)}=cu_j^2,\qquad u_j\sim N(0,1),\qquad
 W_{ij}(0)\sim N(0,1/n),\qquad a_i(0)\sim N(0,1),     \tag{8.3}
\]

with all displayed initialization variables independent. The bottom vector
is frozen permanently. Conditional on it, the pairs
\((a_i(0),z_i(0))\) are independent across rows, with independent coordinates
of laws \(N(0,1)\) and \(N(0,Q_n)\), where
\(Q_n=n^{-1}\sum_j c^2u_j^4\).

**Frozen-bottom joint-step theorem.** Let \(\eta_n>0\) be any deterministic
sequence tending to zero, without a restriction on its rate relative to
\(n\). Iterate (8.1), recomputing the loss residual at every step. For
\(0<\delta<1\), define

\[
 \tau_n(\delta)=\eta_n\inf\{k\ge0:|f_n^k|\ge\delta\},
 \qquad \inf\varnothing=+\infty.
\]

Then \(\tau_n(\delta)\to0\) in probability. With the raw parameters
linearly interpolated and the network and half loss recomputed, both the
predictor and loss undergo a fixed change at times tending to zero.
They cannot converge in probability uniformly on any \([0,T]\), \(T>0\),
to continuous paths with their initialized traces \(0\) and \(1/2\).

The proof controls all negative rows from their initial values, without a
union bound over steps, and uses a fixed favorable Gaussian tail block for
the positive growth.

First, the elementary Gaussian identities \(\mathbb EG^4=3\) and
\(\mathbb EG^8=105\) give

\[
 \mathbb E Q_n=1,\qquad
 \operatorname{Var}(Q_n)=\frac{32}{3n},\qquad
 \mathbb E(f_n^0)^2=\frac{\mathbb E Q_n^2}{n}
   =\frac1n\left(1+\frac{32}{3n}\right).              \tag{8.4}
\]

For the last identity condition on the bottom vector, use independence of
the centered readouts to eliminate cross terms, and use
\(\mathbb E[z_i(0)^4\mid h^{(1)}]=3Q_n^2\) and \(3c^2=1\).
Thus \(Q_n\to1\) and \(f_n^0\to0\) in probability.

Fix \(T>0\) and suppose no grid hit occurs through time \(T\). Every
step starting before that time then has

\[
 (1-\delta)\eta_n\le s_k\le(1+\delta)\eta_n.          \tag{8.5}
\]

In particular, each \(a_i^k\) increases. Let
\(a_{i,-}^0=\max\{-a_i^0,0\}\). While \(a_i^k<0\),
\(|a_i^k|\le a_{i,-}^0\), and (8.1) yields

\[
 |z_i^{k+1}|\le |z_i^k|
       \exp\{2cQ_n(1+\delta)\eta_n a_{i,-}^0\}.
\]

If a row is negative at step \(k\), it was negative at every earlier step.
Multiplying these inequalities therefore proves, at all \(k\eta_n\le T\),

\[
 a_i^k(z_i^k)^2\ge
 -a_{i,-}^0(z_i^0)^2
   \exp\{4cQ_n(1+\delta)T a_{i,-}^0\}.               \tag{8.6}
\]

After a row becomes nonnegative, the same inequality holds because its
left side is nonnegative.

On \(Q_n\in[1/2,2]\), write \(z_i^0=\sqrt{Q_n}v_i\). Conditional on the
bottom vector, \(a_i^0,v_i\) are independent standard Gaussians. Define

\[
 B_T=1+4c\,\mathbb E\!\left[
       G_-e^{8c(1+\delta)T G_-}\right],\qquad
 G_-=\max\{-G,0\},\quad G\sim N(0,1).                 \tag{8.7}
\]

This is finite: every polynomial times \(e^{b|G|}\) is integrable, as follows
by completing the square in the Gaussian density. The conditional mean of
\(c a_{i,-}^0(z_i^0)^2e^{4cQ_n(1+\delta)T a_{i,-}^0}\) is at most
\(2c\mathbb E[G_-e^{8c(1+\delta)TG_-}]\), strictly below \(B_T\).
Its conditional second moment is uniformly bounded on \(Q_n\in[1/2,2]\)
by the same Gaussian integrability and \(\mathbb Ev_i^4=3\).
Conditional Chebyshev, followed by (8.4), proves that with probability
tending to one

\[
 \frac c n\sum_i a_{i,-}^0(z_i^0)^2
          e^{4cQ_n(1+\delta)T a_{i,-}^0}\le B_T.       \tag{8.8}
\]

This is one event determined by initialization. By (8.6), on survival it
bounds the total contribution of all currently negative rows below by
\(-B_T\) at every grid time under consideration.

For a fixed number \(b>1\), retain the rows

\[
 \mathcal I_b=\{i:a_i^0\in[b,b+1],\ v_i\in[b,b+1]\},
 \qquad p_b=\Pr\{G\in[b,b+1]\}^2>0.
\]

Conditionally, \(|\mathcal I_b|\) is binomial with parameters \(n,p_b\).
Its variance bound \(np_b(1-p_b)\) shows
\(|\mathcal I_b|/n\ge p_b/2\) with probability tending to one. These rows
remain in the positive quadrant before an output hit. Put
\(\gamma=c(1-\delta)\). On \(Q_n\ge1/2\), (8.1) and (8.5) give, for
\(y_i^k=\min\{a_i^k,z_i^k\}\),

\[
 y_i^{k+1}\ge y_i^k+\gamma\eta_n(y_i^k)^2,
 \qquad y_i^0\ge b/\sqrt2.                            \tag{8.9}
\]

For the scalar recursion \(y^+=y+\gamma\eta_n y^2\), while \(0<y<M\)
and \(\gamma\eta_n M\le1\),

\[
 \frac1y-\frac1{y^+}
 =\frac{\gamma\eta_n}{1+\gamma\eta_n y}
 \ge\frac{\gamma\eta_n}{2}.
\]

The scalar map is increasing on \([0,\infty)\), so it bounds (8.9) below.
Summing reciprocals shows that every selected row reaches level \(M\) no
later than \(2\sqrt2/(\gamma b)+\eta_n\), unless the output already hit.
A row already above \(M\) requires no waiting; after reaching \(M\) it
stays above it while survival continues.

Choose \(b>\max\{1,4\sqrt2/(\gamma T)\}\), and then the finite constant

\[
 M=\left(\frac{2(B_T+2\delta)}{cp_b}\right)^{1/3}.
\]

Both depend on \(T,\delta\), not on \(n\). Eventually
\(\gamma\eta_n M\le1\), and the common level is reached before \(T\).
If no output hit had occurred, (8.8) and the favorable-row count would give

\[
 f_n^k\ge \frac{cp_b}{2}M^3-B_T=2\delta,
\]

a contradiction. The intersection of the three initialization events
\(Q_n\in[1/2,2]\), (8.8), and the favorable-row count has probability
tending to one. Consequently \(\Pr\{\tau_n(\delta)>T\}\to0\). Since this
holds for every \(T>0\), the hitting-time assertion is proved.

On \(|f_n^0|<\delta/2\), continuous raw-parameter interpolation reaches
one of \(\delta,-\delta\) during the first crossing step, at a time no
later than \(\tau_n(\delta)\). At that time its predictor differs from its
initial value by at least \(\delta/2\). Its loss differs from \(1/2\) by
at least \(\delta-\delta^2/2>0\), while its initial loss tends to \(1/2\)
by (8.4). If these paths converged uniformly in probability to a continuous
initialized path, evaluation at these times tending to zero would instead
make both changes vanish. For a random continuous proposed limit the same
argument holds: its modulus of continuity tends to zero almost surely,
and hence in probability. This proves the asserted obstruction.

### 8.2 Freezing a layer supplies no pathwise lower comparison

The theorem just proved does not transfer by deleting the bottom update
from a fully trained trajectory. An exact one-step counterexample explains
why. This paragraph uses the separate deterministic width-one model with
raw activation \(\phi(z)=z^2\), so

\[
 f(a,w,u)=aw^2u^4.
\]

A feature-ascent step of size \(s>0\) and unit mobilities is

\[
 a^+=a+sw^2u^4,\qquad w^+=w+2sawu^4,\qquad
 u^+=u+4saw^2u^3.                                    \tag{8.10}
\]

The frozen-bottom step omits the last update. Fix any \(\varepsilon>0\),
put \(a=-1\), and choose positive \(u,w\) by

\[
 R=\frac{1/2+\varepsilon}{s},\qquad
 u^2=\frac{\rho}{R},\qquad w^2=\frac{R^2}{\rho}.
\]

Then \(w^2u^2=R\), \(w^2u^4=\rho\), and
\(u^+/u=-1-4\varepsilon\). The two updates have identical \(a^+,w^+\).
Choose \(\rho>0\) small enough that \(s\rho<1\) and
\(0<2s(\rho/R)^2<1\). The frozen output is

\[
 f_{\mathrm{frozen}}^+=(-1+s\rho)\rho
              \{1-2s(\rho/R)^2\}^2<0,
 \qquad |f_{\mathrm{frozen}}^+|\le\rho.
\]

The full output equals \((1+4\varepsilon)^4f_{\mathrm{frozen}}^+\),
which is strictly smaller. Taking also
\((1+4\varepsilon)^4\rho<\delta\) keeps the initial output and both
terminal outputs inside \((-\delta,\delta)\). This works for every
\(s>0\), with an \(s\)-dependent state. It refutes the pathwise deletion
inequality; it is not a typical-Gaussian-trajectory counterexample.
The arbitrary joint-step theorem for the fully trained quadratic network
is not supplied by this section.

## 9. ReLU classical-flow and Euler boundaries

### 9.1 A reached finite-width obstruction to classical ReLU flow

Now use \(\phi(z)=cz_+\), \(c=\sqrt2\), where \(z_+=\max\{z,0\}\),
and train all three blocks. A prescribed kink convention is a fixed real
number \(\sigma\) assigned to \(\phi'(0)\), with derivatives \(0\) on
negative inputs and \(c\) on positive inputs. Write

\[
 \delta^{(2)}=a\odot\phi'(z^{(2)}),\qquad
 \delta^{(1)}=\phi'(u)\odot W^T\delta^{(2)}.
\]

The convention defines the pointwise vector field

\[
 \dot a=(1-f_n)h^{(2)},\qquad
 \dot u=(1-f_n)\delta^{(1)},\qquad
 \dot W=\frac{1-f_n}{n}\delta^{(2)}(h^{(1)})^T.       \tag{9.1}
\]

By a solution of this field we mean an absolutely continuous parameter path
satisfying (9.1) almost everywhere. Nonexistence in this class includes
nonexistence of an ordinary classical continuation. It says nothing about
a differential inclusion with an additional selection rule.

**Classical ReLU obstruction.** For every fixed \(\sigma\in\mathbb R\),
already at width \(n=2\), there is an open set of initial parameters of
positive Gaussian probability whose smooth trajectory reaches a gate
where (9.1) has no absolutely continuous continuation. The Gaussian law
is independent \(u_j,a_i\sim N(0,1)\), \(W_{ij}\sim N(0,1/2)\).
No probability bound uniform in width is asserted.

To prove this, at a contact point take

\[
 u=(1,1),\quad W=\frac1{\sqrt2}
       \begin{pmatrix}1&-1\\2&0\end{pmatrix},\quad
 a_1=-\lambda/c,\quad a_2=1/(4c),\qquad \lambda>1/8.
\]

Then \(h^{(1)}=(c,c)\), \(z^{(2)}=(0,2)\), \(f_2=1/4\).
When the slope used at the first top gate is \(v\), differentiation of
\(z^{(2)}=Wh^{(1)}\) gives

\[
 \dot z^{(2)}=(1-f_2)
 \left\{\frac{\|h^{(1)}\|_2^2}{2}\delta^{(2)}
             +W\operatorname{diag}(\phi'(u)^2)W^T\delta^{(2)}\right\}.
\]

Here \(\|h^{(1)}\|_2^2/2=2\),
\(WW^T=\left(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\right)\),
and \(\phi'(u)^2=(2,2)\). The first normal component is therefore

\[
 \dot z_1^{(2)}=\frac34\{4a_1v+2a_2c\}.
\]

Its negative-side, positive-side and convention-assigned values at contact
are respectively

\[
 p=\frac38>0,\qquad
 q=\frac34(1/2-4\lambda)<0,\qquad
 v_0=\frac34(1/2-4\lambda\sigma/c).                   \tag{9.2}
\]

Choose \(\lambda>1/8\) avoiding the at most one value for which \(v_0=0\).
All other gates are strictly positive. The formulas for each adjacent sign
cell and for the gate itself vary continuously in the remaining parameters.
A sufficiently small neighborhood of this contact therefore has constants
\(\gamma,\gamma_0>0\) such that

\[
 \dot z_1^{(2)}\ge\gamma\quad(z_1^{(2)}<0),\qquad
 \dot z_1^{(2)}\le-\gamma\quad(z_1^{(2)}>0),\qquad
 |\dot z_1^{(2)}|\ge\gamma_0\quad(z_1^{(2)}=0).        \tag{9.3}
\]

If an absolutely continuous solution started on this gate, continuity would
keep it in the neighborhood for a short time. Put \(w=|z_1^{(2)}|\).
It is absolutely continuous, and \(w'\le-\gamma\) almost everywhere on
\(\{w>0\}\). It has derivative zero almost everywhere on \(\{w=0\}\):
at every differentiable accumulation point of a level set the derivative
vanishes by difference quotients, while its isolated points form a
countable set. Integration from the contact gives

\[
 0\le w(t)\le-\gamma\,|\{s\in[0,t]:w(s)>0\}|.
\]

Thus \(w\equiv0\). The derivative of \(z_1^{(2)}\) is then zero almost
everywhere, contradicting the third inequality in (9.3).

The failure is reached from an open set, not just from the contact surface.
Perturb the first row to \((1+\epsilon,-1)/\sqrt2\); then
\(z_1^{(2)}=\epsilon>0\). In a fixed small ball about the contact, the
plus-cell field is smooth, its norm is bounded by a finite \(M\), and its
normal component is at most \(-\gamma\). Choose \(\epsilon\) sufficiently
small that \(2\epsilon/\gamma\) is less than the distance to the ball's
boundary divided by \(M\). A small open neighborhood of this perturbed
state still has \(0<z_1^{(2)}<2\epsilon\), stays away from every other
gate, and reaches \(z_1^{(2)}=0\) before it can exit the ball. Local smooth
ODE existence and continuation inside the sign cell follow from its
locally Lipschitz polynomial field; bounded speed precludes escape before
the stated hit. The contact lies in (9.3), so continuation fails there.
Independent nondegenerate Gaussian coordinates have a strictly positive
density everywhere in this finite parameter space, giving positive
probability to that open set.

### 9.2 Positive local compactness for every ReLU Euler step sequence

For this theorem impose \(|\sigma|\le c=\sqrt2\), keep all three blocks
trained, and initialize independently by
\(u_j,a_i\sim N(0,1)\), \(W_{ij}\sim N(0,1/n)\).
The exact Euler step for (9.1) is

\[
 a^+=a-\eta r_nh^{(2)},\qquad
 u^+=u-\eta r_n\delta^{(1)},\qquad
 W^+=W-\frac{\eta r_n}{n}\delta^{(2)}(h^{(1)})^T.     \tag{9.4}
\]

Let \(F_n(t)\) be the predictor recomputed from the linearly interpolated
raw parameters, and let \(J_n(t)=(F_n(t)-1)^2/2\). For every deterministic
\(\eta_n>0\) tending to zero, their joint laws are tight in
\(C([0,T_0];\mathbb R^2)\), where

\[
 T_0=\frac1{384\cdot6^4}.                              \tag{9.5}
\]

Every subsequential distributional limit consists of continuous paths with
\(F(0)=0\), \(J(0)=1/2\). The same holds if one instead linearly
interpolates the grid predictors, the grid losses, or both. No determinism,
uniqueness, full parameter-state compactness, tangent-kernel convergence,
or extension beyond \(T_0\) is asserted.

The proof needs neither differentiability at a gate nor energy dissipation
for the Euler scheme. Set

\[
 R=\max\left\{1,\frac{\|a\|_2}{\sqrt n},
                   \frac{\|u\|_2}{\sqrt n},\|W\|_{\mathrm{op}}\right\}.
\]

The Lipschitz constant \(c\) of ReLU and the bound \(|\phi'|\le c\) imply

\[
 \frac{\|h^{(1)}\|_2}{\sqrt n}\le cR,\quad
 \frac{\|h^{(2)}\|_2}{\sqrt n}\le2R^2,\quad
 \frac{\|\delta^{(2)}\|_2}{\sqrt n}\le cR,\quad
 \frac{\|\delta^{(1)}\|_2}{\sqrt n}\le2R^2.
\]

Hence \(|f_n|\le2R^3\) and \(|r_n|\le3R^3\). The rank-one norm identity
\(\|vw^T/n\|_{\mathrm{op}}=\|v\|_2\|w\|_2/n\), together with
(9.4), bounds each of the three parameter increments in its displayed
norm by \(6\eta R^5\). Therefore, pathwise,

\[
 R^+\le R+6\eta R^5.                                  \tag{9.6}
\]

Let \(R_*=6\), \(S=12\), \(T_*=1/(192\cdot6^4)=2T_0\).
On the initialization event

\[
 \mathcal E_n=\left\{
   \|a^0\|_2/\sqrt n\le2,\quad \|u^0\|_2/\sqrt n\le2,
   \quad\|W^0\|_{\mathrm{op}}\le6\right\},             \tag{9.7}
\]

induction gives \(R_k\le S\) at every grid time \(k\eta_n\le T_*\).
Indeed, if all preceding states satisfy that bound, telescoping (9.6)
gives

\[
 R_k\le R_*+6k\eta_nS^5
       \le R_*+6T_*(2R_*)^5=2R_*=S.
\]

The event (9.7) has probability tending to one. For the first two
conditions the empirical mean of Gaussian squares has mean one and
variance \(2/n\), so Chebyshev applies. For the matrix condition there is
an elementary finite-net argument. Choose a maximal \(1/4\)-separated
set on the unit sphere. The disjoint radius-\(1/8\) balls about its points
lie in the radius-\(9/8\) ball, so its size is at most \(9^n\); maximality
makes it a \(1/4\)-net. For fixed unit vectors \(x,y\),
\(y^TW^0x\sim N(0,1/n)\). Exponential Markov applied to the Gaussian
moment generating function gives
\(\Pr\{|y^TW^0x|>3\}\le2e^{-9n/2}\). The union bound for two such nets
then gives

\[
 \Pr\left\{\max_{x,y\text{ in the net}}|y^TW^0x|>3\right\}
 \le2\,81^n e^{-9n/2}\longrightarrow0.
\]

Approximating two maximizing unit vectors by net points changes the bilinear
form by at most \(\|W^0\|_{\mathrm{op}}/2\). Hence
\(\|W^0\|_{\mathrm{op}}\le2\max_{x,y\text{ in the net}}|y^TW^0x|\),
which proves the final initialization bound.

For all sufficiently large \(n\), \(\eta_n\le T_0\), so every endpoint
needed to interpolate through \(T_0\) lies before \(T_*\). Raw linear
interpolation preserves the bound \(R\le S\) by convexity of the three
norms. Within one grid cell, its three parameter velocities in those norms
are at most \(6S^5\). For times \(t,s\) in that cell, ReLU Lipschitzness
and the product difference \(W(t)h^{(1)}(t)-W(s)h^{(1)}(s)\) give

\[
 \frac{\|h^{(1)}(t)-h^{(1)}(s)\|_2}{\sqrt n}
       \le6cS^5|t-s|,
\]
\[
 \frac{\|z^{(2)}(t)-z^{(2)}(s)\|_2}{\sqrt n}
       \le12cS^6|t-s|,
 \qquad
 \frac{\|h^{(2)}(t)-h^{(2)}(s)\|_2}{\sqrt n}
       \le24S^6|t-s|.
\]

A final product difference in \(a^Th^{(2)}/n\) proves

\[
 |F_n(t)-F_n(s)|\le(12S^7+24S^7)|t-s|
                    \le60S^7|t-s|.
\]

Summing over intervening cells gives the same bound for arbitrary times.
Thus on \(\mathcal E_n\),

\[
 \sup_{t\le T_0}|F_n(t)|\le2S^3,\qquad
 |F_n(t)-F_n(s)|\le60S^7|t-s|.                         \tag{9.8}
\]

Uniformly bounded functions with a common Lipschitz constant form a compact
subset of \(C([0,T_0])\): convergence on a countable dense set is obtained
by successive bounded subsequences, and the common modulus extends it to
uniform convergence and a continuous limit. The squared-loss map sends
this set continuously to another compact set. Since
\(\Pr(\mathcal E_n)\to1\), (9.8) proves asymptotic tightness of the
pair. To include any finite set of smaller widths, restrict their Gaussian
initial parameters to a sufficiently large bounded set. Repeated use of
(9.6) bounds their finitely many Euler states and parameter velocities,
yielding their own compact sets by the same argument. A finite union is
compact. This proves tightness of the entire sequence. The usual weak
compactness theorem for tight probability measures on the complete
separable space \(C([0,T_0];\mathbb R^2)\) then supplies convergent
subsequences.

At initialization, condition first on \(u\). Writing
\(Q_n=\|\phi(u)\|_2^2/n\), the independent Gaussian rows give
\(z_i^{(2)}\mid u\sim N(0,Q_n)\). Symmetry and \(c^2=2\) imply
\(\mathbb E[\phi(z_i^{(2)})^2\mid u]=Q_n\), and \(\mathbb E Q_n=1\).
Conditioning next on the two hidden blocks and using the independent
centered readouts proves

\[
 \mathbb E(F_n(0))^2
 =\frac1{n^2}\mathbb E\|h^{(2)}(0)\|_2^2=\frac1n.
\]

Therefore \(F_n(0)\to0\) in probability. Evaluation at time zero is
continuous in the uniform topology, so every weak subsequential limit has
\(F(0)=0\), and the loss relation gives \(J(0)=1/2\).

Finally the grid predictor interpolation has the same endpoint Lipschitz
bound as (9.8). It differs from the raw-parameter predictor by at most
\(2\cdot60S^7\eta_n\) on \(\mathcal E_n\), since both agree at the left
endpoint of each cell. The loss map is Lipschitz on the bounded output
interval. For grid predictors \(x,y\), the linear interpolation of their
losses differs from the loss of their linear interpolation by exactly
\(\lambda(1-\lambda)(x-y)^2/2\), at cell fraction \(\lambda\in[0,1]\).
It is at most \((x-y)^2/8\), hence uniformly \(O(\eta_n^2)\) on the same
event. These differences vanish in probability, proving all interpolation
variants stated above.

### 9.3 A frozen gate retains occupation information

An elementary local model further separates classical noncontinuation from
Euler compactness. Freeze two normal velocities \(p>0>q\), choose the
standard contact convention \(v(0)=p\), and consider

\[
 z_{k+1}=z_k+\eta\{p+(q-p)I_k\},\qquad I_k=\mathbf1_{\{z_k>0\}}.
\]

Its strip \(\eta q<z\le\eta p\) is invariant: below or at zero add
\(\eta p\), and above zero add \(\eta q\). Every initial point enters
this strip after finitely many steps by repeated motion toward zero.
Inside it, put

\[
 \lambda=\frac p{p-q},\qquad
 x_k=\frac{z_k/\eta-q}{p-q}\in(0,1].
\]

The update gives exactly \(x_{k+1}=x_k+\lambda-I_k\), including a visit
to zero under the stated convention. Consequently, on every finite window
of length \(N\),

\[
 \left|\sum_{k=j}^{j+N-1}I_k-N\lambda\right|
   =|x_j-x_{j+N}|<1.                                  \tag{9.9}
\]

Thus a gate initialized in the strip has \(z=O(\eta)\) uniformly in time,
while its occupation converges to a binary mixture with weights
\(1-\lambda,\lambda\). All its positive integer gate moments converge to
\(\lambda\), since \(I_k^r=I_k\) for every integer \(r\ge1\).
Replacing the binary gate by its scalar mean instead gives second moment
\(\lambda^2\), which is different for \(0<\lambda<1\).

Joint moments also need separate information. For \(p=-q\), two identical
nonboundary phases produce identical alternating gates and average product
\(1/2\); two phases differing by half the strip's circle length produce
complementary gates and average product zero. Their marginal occupations
are both \(1/2\). These are exact frozen scalar examples, not claimed
reachable configurations of the random network. In a neural kernel, squares
of \(a\odot\phi'(z^{(2)})\) and of its reused transpose action can detect
such second and joint moments.

The ReLU local compactness theorem therefore does not identify a generalized
population flow or its loss law uniquely. Conversely, the reached classical
obstruction does not preclude continuous scalar Euler subsequences. Neither
statement resolves the fully trained quadratic arbitrary-step problem.
