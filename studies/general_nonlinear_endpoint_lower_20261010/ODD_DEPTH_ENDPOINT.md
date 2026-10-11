# Actual fitted endpoints at arbitrary fixed depth: the odd-activation case

This is a new partial extension, not a solution for the entire activation
class. It retains the old endpoint theorem's unused-input-direction geometry.
It applies to the **actual fully trained canonical network**, not readout-only
training. Oddness is essential to the proof below. No manuscript is changed.

## Statement

Use the canonical network, Gaussian initialization, block learning rates,
population Grams, and activation envelope of `paper/compact.tex`:

\[
 h^{(1)}(x)=\phi_1(W^{(1)}x/\sqrt d),\qquad
 h^{(j)}(x)=\phi_j(W^{(j)}h^{(j-1)}(x)),\qquad
 f_n(x)=w^\top h^{(L)}(x)/n.
\]

The initial readout is zero. First-layer entries have variance one, hidden
entries have variance $1/n$, and all blocks are independent. The loss is
$m^{-1}\sum_a(f_n(x_a)-y_a)^2$. The block mobilities are
$(n,1,\ldots,1,n)$. Let $\gamma=\lambda_{\min}(Q^{(L)})>0$,
$Y=\|y\|_2/\sqrt m>0$, and retain the existing assumptions
$\gamma/m\le1$ and $Y\le(\gamma/m)\beta^{-30L}$.

Assume additionally that every activation is odd and
\[
 Q^{(L)}_{11}\ge\beta^{-40L}.                                      \tag{1}
\]
The activation values may be unbounded. Let the training directions span a
proper subspace of $\mathbb R^d$, and choose a unit vector $v$ orthogonal to
that subspace, independently of initialization. For every sufficiently large
individual width, two independent canonical runs satisfy
\[
 \mathbb P\left\{
  |f_n(\infty,\sqrt d\,v)-\widetilde f_n(\infty,\sqrt d\,v)|
  \ge {\sqrt{Q^{(L)}_{11}\,y^\top(Q^{(L)})^{-1}y}\over8\sqrt n},
  \quad\text{both runs fit}\right\}\ge\frac12.                    \tag{2}
\]
All data, labels, activations, and depth are fixed before width increases.
The width threshold is unquantified. The same bound holds for a supremum
over any query set containing this orthogonal direction.

Condition (1) is automatic for the concrete families checked in Section 5.
It is **not** automatic for every admissible odd activation. A more precise
version, dispensing with (1), replaces it by the additional label condition
in (15) below. This qualification must not be hidden in the existing cap.

## 1. Fitting estimates and the unused Gaussian query

Here and below all auxiliary symbols are local to the proof. Put
$\lambda=\gamma/m$ and $\rho=\|f_n(X)-y\|_2/\sqrt m$. Use the coefficients
in the complete fitting lemma `paper/compact_fitting.tex`:
\[
\begin{split}
 H&=\max_{0\le j\le L}\sqrt{Q^{(j)}_{11}}\ge1,\qquad
 s=\max(1,\max_j\sup_{\mathbb R}|\phi_j'|),\\
 D_j&=s(9s)^{L-j},\quad U_1=D_1,\quad U_j=2HD_j\ (j\ge2),\\
 F_1&=sU_1,\qquad F_j=s(2HU_j+9F_{j-1}),\quad F=F_L.
\end{split}                                                       \tag{3}
\]
These definitions may use the smaller real derivative bound instead of the
strip bound in that lemma; its real-flow proof is unchanged. Its estimates
$H\le(2\beta)^L$ and $8H\sqrt F\le\beta^{5L}$ remain valid.

Apply that fitting lemma in the training span alone. With probability tending
to one over this active initialization, both parameter convergence and exact
fitting hold, all initialized and moving hidden operator norms are at most
$8$ and $9$, respectively, training feature RMS is at most $2H$, and
\[
 \rho(t)\le Ye^{-\lambda t/2},\qquad
 \int_0^\infty\rho(t)\,dt\le 2Y/\lambda.                          \tag{4}
\]
The initial feature Gram tends to $Q^{(L)}$ and has minimum eigenvalue at
least $\gamma/2$. The fitting event is measurable without the first-layer
Gaussian coordinates along $v$. Indeed the first-layer velocity is a sum
of outer products with training directions, so $W^{(1)}(t)v=W^{(1)}_0v$.
Conditional on the active initialization,
\[
 Z=W^{(1)}_0v\sim N(0,I_n)
\]
is independent of the complete training trajectory. Its query features are
$h^{(1)}(Z)=\phi_1(Z)$ and
$h^{(j)}(Z)=\phi_j(W^{(j)}h^{(j-1)}(Z))$. Oddness makes each such
vector odd in $Z$, at initialization and after training, so its mean is zero.

The argument in the remaining sections uses only (3)--(4), the stated operator
and feature bounds, initial Gram convergence, and the canonical equations.
It does not assume Gaussian trained features or independent trained neurons.

## 2. A readout comparison that preserves the label/gap ratio

Write $B_t=[h^{(L)}(t,x_a)]_{a=1}^m/\sqrt n$ and $u_t=w(t)/\sqrt n$.
Thus $f_n(t,X)=B_t^\top u_t$ and
$\dot u_t=-(2/m)B_t r_t$. Let
\[
 u_* = B_0(B_0^\top B_0)^{-1}y,\qquad e=\|u_*\|.
\]
This is the minimum-norm readout that interpolates using frozen initialized
features; it is only a proof comparator. In particular,
$e\le\sqrt2Y/\sqrt\lambda$ and $B_0^\top u_*=y$.

On a finite interval $[0,T]$ put $M=\sup_{t\le T}\|u_t\|$ and
$A=\int_0^T\rho$. The canonical hidden velocities and the forward chain rule
give
\[
 \sup_{t\le T}{\|B_t-B_0\|_{\rm op}\over\sqrt m}
 \le 2FMA.                                                        \tag{5}
\]
To verify the factor, each normalized hidden-block velocity is at most
$2U_j\rho\|u\|$. Forward differentiation has recursion (3), hence each
feature RMS velocity is at most $2F_j\rho\|u\|$. Integration and the
Frobenius upper bound for a matrix of $m$ such columns prove (5).

The exact comparator energy identity is
\[
 \frac12\partial_t\|u_t-u_*\|^2
 =-2\rho(t)^2+rac2m
       \langle(B_t-B_0)^\top u_*,r_t\rangle.
\]
Using the time-dependent version
$\|B_t-B_0\|_{\rm op}/\sqrt m\le2FM\int_0^t\rho$ and integrating yields
\[
 \|u_t-u_*\|^2\le e^2+4FMeA^2.
\]
At a maximizing time, $\|u_t-u_*\|\ge M-e$ when $M\ge e$, so
$M\le2e+4FeA^2\le3e$, since
$4FA^2\le16FY^2/\lambda^2\le1$ under the existing cap.
This bound is uniform in $T$, and therefore
\[
 \sup_{t\ge0}\|u_t\|\le3e.                                      \tag{6}
\]

Let $P$ project onto the range of $B_0$. Its orthogonal complement satisfies
\[
 \|(I-P)u_\infty\|
 \le2\int_0^\infty
       {\|B_t-B_0\|_{\rm op}\over\sqrt m}\rho(t)\,dt
 \le2FM(2Y/\lambda)^2\le24FeY^2/\lambda^2.
\]
Endpoint interpolation also gives
$B_0^\top(u_\infty-u_*)=-(B_\infty-B_0)^\top u_\infty$. Since the
smallest singular value of $B_0$ is at least $\sqrt{\gamma/2}$,
\[
\begin{split}
 \|P(u_\infty-u_*)\|
 &\le\sqrt{2/\lambda}\,(4FMY/\lambda)M\\
 &\le72FeY^2/\lambda^2.
\end{split}
\]
Here the final inequality uses $M\le3e$ and
$e\le\sqrt2Y/\sqrt\lambda$. In particular the slightly looser common bound
\[
 \|u_\infty-u_*\|\le120Fe(Y/\lambda)^2                           \tag{7}
\]
is valid. This argument avoids an exponential stability factor and avoids
an extra inverse-gap loss from separately perturbing the residual equation.

## 3. The endpoint correction at the fluctuation scale

Define local constants
\[
 K_j=s(8s)^{j-1},\qquad
 T_L=\sum_{j=2}^L s(9s)^{L-j}U_jK_{j-1},\qquad
 D=120K_LF+36\sqrt2\,T_L.                                        \tag{8}
\]
The initialized query map $Z\mapsto h_0^{(j)}(Z)$ is $K_j$-Lipschitz.
For each deterministic vector $a$, Gaussian Poincare gives
$\operatorname{Var}(a^\top h_0^{(j)})\le K_j^2\|a\|^2$.
Oddness therefore implies
\[
 \mathbb E_Z\|E h_0^{(j)}(Z)\|^2\le K_j^2\|E\|_F^2              \tag{9}
\]
for every deterministic matrix $E$. This is valid after conditioning on the
active initialization; it does not require independence of $E$ and the
initialized hidden matrices.

The trained hidden displacement is bounded by
$\|W^{(j)}_\infty-W^{(j)}_0\|_F\le4U_jMY/\lambda$ for $j\ge2$.
Subtracting the two query recursions, applying Minkowski and (9), and using
the moving operator bound $9$ gives
\[
 \big(\mathbb E_Z\|h^{(L)}_\infty-h^{(L)}_0\|^2\big)^{1/2}
 \le4MYT_L/\lambda.                                              \tag{10}
\]
There is no first-layer difference at this query.

The frozen-feature endpoint is $f_{\rm RF}(v)=u_*^\top h_0^{(L)}(Z)/\sqrt n$.
Decompose the actual endpoint correction using the changed readout and then
the changed features. Equations (6)--(10) imply
\[
\begin{split}
 &\left(\mathbb E_Z
 |f_n(\infty,\sqrt d\,v)-f_{\rm RF}(v)|^2\right)^{1/2}\\
 &\quad\le\frac{K_L\|u_\infty-u_*\|+4M^2YT_L/\lambda}{\sqrt n}
 \le\frac{De}{\sqrt n}(Y/\lambda)^2.                             \tag{11}
\end{split}
\]
This is an actual nonlinear endpoint comparison. The absence of $\sqrt n$
in (10) is the reason its error is on the required fluctuation scale.

For reference, the definitions give the deliberately loose envelope
\[
 D\le\beta^{16L}.                                                \tag{12}
\]
Indeed $F\le\beta^{10L}$, $K_L\le\beta^{2L}$, and
$T_L\le2LHs^3(9s)^{2L-4}\le\beta^{7L}$ for $L\ge2$, $\beta\ge10$.
Thus $120\beta^{12L}+36\sqrt2\beta^{7L}\le\beta^{16L}$.

## 4. Anti-concentration and transfer to the trained endpoint

Put $Q=Q^{(L)}$, $q=Q^{(L)}_{11}$ and
$e_0^2=y^\top Q^{-1}y$. These three symbols are local to this section.
Orthogonality of the query and oddness give zero population cross-covariance
with the training coordinates at every layer. The last-layer population
feature pair $(H,H_*)$ consequently has independent training vector $H$ and
query scalar $H_*$, with $\mathbb EH_*=0$ and
$\mathbb EH_*^2=q$. The influence of empirical feature interpolation is
\[
 H_*H^\top Q^{-1}y,
 \qquad\operatorname{Var}(H_*H^\top Q^{-1}y)=q e_0^2>0.            \tag{13}
\]

Here is why this iid influence applies to the actual finite-depth
initialization without presuming independent lower-layer coordinates.
Conditional on all preceding layers, last-layer neuron rows are independent
Gaussian transforms with covariance equal to the preceding empirical
augmented feature Gram. That Gram converges in probability to its population
counterpart: conditional variances of its finitely many entries are $O(1/n)$,
and Gaussian expectations are continuous in the covariance, including at
singular covariances, by the coupling $S^{1/2}G$ and linear activation growth.
Induct over the fixed layers.

For any deterministic sequence of preceding covariances tending to their
limit, expand empirical interpolation around its conditional population
Gram. In a neighborhood of that limit the training inverse is bounded.
Each covariance entry has an $O_{\mathbb P}(n^{-1/2})$ error, so the
matrix-inverse identity leaves an $O_{\mathbb P}(n^{-1})$ remainder.
The linear term is an average of the centered influences
$(H_*-q(S)^\top Q(S)^{-1}H)H^\top Q(S)^{-1}y$, where $q(S)$ is the
conditional population cross column. Their variances tend to (13); their
third absolute moments are uniformly bounded by Gaussian moments and linear
growth. Expanding their characteristic functions to second order, with
third-order remainder, proves a triangular central limit theorem with
variance (13).

Convergence to a continuous normal distribution is uniform over intervals;
a finite normal-quantile partition proves this from weak convergence.
It is locally uniform over preceding covariances as well: otherwise a
deterministic convergent subsequence would contradict the preceding argument.
Two independent frozen endpoints therefore have, conditional on lower layers,
a centered difference asymptotic to $N(0,2qe_0^2)$. The two conditional-
population centering constants can contribute an uncontrolled shift, but a centered normal places the
largest mass among intervals of a given length on the centered interval.
Writing $\Phi$ for the standard normal distribution function, this proves
\[
 \limsup_{n\to\infty}
 \mathbb P\left\{
 |f_{\rm RF}-\widetilde f_{\rm RF}|
 \le\frac{\sqrt q\,e_0}{4\sqrt n}\right\}
 \le2\Phi(1/(4\sqrt2))-1<\frac16.                                \tag{14}
\]
The last inequality follows from bounding the normal density by
$1/\sqrt{2\pi}$. Vanishing-probability singular empirical Grams may be
assigned any value and do not affect (14).

Intersect each active fitting event with $e\le\sqrt2e_0$, an event whose
probability also tends to one by initial Gram convergence. Equation (11),
Minkowski, and Markov show that the difference of the two endpoint corrections
exceeds $\sqrt q\,e_0/(8\sqrt n)$ on this event with probability at most
$512D^2(Y/\lambda)^4/q$. Thus the sufficient condition
\[
 D(Y/\lambda)^2\le\sqrt q/64                                    \tag{15}
\]
makes this probability at most $1/8$. Subtract (14), this error event, and
the vanishing exceptional events. The success probability is eventually
larger than $1/2$, and the triangle inequality proves (2).

Finally, (1), (12) and the original cap imply (15):
$D(Y/\lambda)^2\le\beta^{-44L}\le\beta^{-20L}/64\le\sqrt q/64$.
Without (1), the proof remains valid under (15); this can be guaranteed by
the additional activation-dependent cap
$Y\le\lambda q^{1/4}/(8\sqrt D)$ when $D>0$. No claim that the original
cap alone implies this for every odd activation is made.

## 5. Concrete scope and limitations

The extension includes arbitrary layerwise mixtures of $\tanh z$,
$\arctan z$, $\sin z$, and $z+\tanh z$, at arbitrary fixed depth.
These functions are nonaffine and analytic on a common strip with bounded
first derivative; the last is unbounded. For tanh and arctan choose a strip
strictly inside their nearest complex singularities. For sine choose any
fixed finite strip. Each mixture uses its actual envelope $\beta$.

Here is a direct check of (1). If $G\sim N(0,1)$ then
$\mathbb E[G^2\mathbf1_{|G|\le1}]\ge2e^{-1/2}/(3\sqrt{2\pi})>1/8$,
by bounding its density below on $[-1,1]$. For $0<q\le1$,
$\tanh(\sqrt q\,G)^2\ge qG^2/4$ and
$\arctan(\sqrt q\,G)^2\ge qG^2/4$ on that event. Monotonicity of their
absolute values extends the lower bound to $q\ge1$. Thus either transform
has Gaussian second moment at least $\min(q,1)/32$.
For sine the moment is $(1-e^{-2q})/2\ge\min(q,1)/4$.
For $z+\tanh z$ it is at least $q$, since the two summands have the same
sign on the real axis. Starting from input variance one gives
$Q^{(L)}_{11}\ge32^{-L}\ge\beta^{-40L}$. These families therefore need
no extra label restriction beyond the paper's cap. Odd activations normalized
layerwise to unit Gaussian second moment also satisfy (1) immediately.

This does not cover raw GELU, SiLU, softplus, sigmoid, or arbitrary shifted
activations: they are not odd. Centering the scalar output alone does not
repair (9), because hidden feature means enter the next matrix product.
`PRODUCT_QUERY_ROUTE.md` gives a concrete obstruction to the needed
whole-feature perturbation bound for noncentered activations. That is an
obstruction to this proof step, not a counterexample to the desired endpoint
theorem. Full-span training is likewise not covered: it removes the unused
Gaussian input block. Both generalizations remain open here.
