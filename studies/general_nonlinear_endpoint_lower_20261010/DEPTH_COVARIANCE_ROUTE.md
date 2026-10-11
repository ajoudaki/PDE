# Arbitrary-depth query covariance: an obstruction and a readout comparison

2026-10-10. Scoped derivation for `general_nonlinear_endpoint_lower_20261010`.
Scientific inputs were `paper/compact.tex`, `paper/compact_fitting.tex`, this
study's `POSITIVE_ROUTE.md`, and the explicitly assigned
`studies/integrated_general_compression_20261004/TANH_ENDPOINT_VARIABILITY_LOWER.md`.
The canonical-notation skill and its neural-network reference, and the
rigorous-math skill, were applied. No other research inputs, experiments,
or paper edits were used. Results below are internally derived, not promoted.

There are two distinct conclusions. A width-independent lower bound on the
entire conditional query covariance is false for the full activation class,
already at initialization and depth two. Nevertheless, the actual fitted
readout admits a useful arbitrary-depth comparison with the frozen-feature
interpolating readout. For odd activations this gives an endpoint remainder
on the fluctuation scale, without requiring a smallest-eigenvalue lower bound
for the deep query covariance. The exact original label cap does not close
the resulting fluctuation comparison solely from the estimates proved here.

## 1. Setup and the randomness that remains independent

Let the normalized training inputs be unit vectors
\(v_a=x_a/\sqrt d\), let
\(S=\operatorname{span}\{v_1,\ldots,v_m\}\) be proper, and fix a unit
\(v\in S^\perp\). Use the canonical forward map and mobilities from
`paper/compact.tex`. The first-layer flow is a sum of matrices with right
factors \(v_a^\top\), so its restriction to \(S^\perp\) is unchanged.
Consequently, after conditioning on the active initialized blocks and their
whole training trajectory, the query first preactivation is an independent
\(Z\sim N(0,I_n)\). Its features are exactly
\[
 h^{(1)}(Z)=\phi_1(Z),\qquad
 h^{(\ell)}(Z)=\phi_\ell(W^{(\ell)}h^{(\ell-1)}(Z)),\quad 2\le\ell\le L.
\]
Subscript zero denotes the same query map using initialized hidden matrices.
The fitting event must be constructed in the active input space; otherwise
conditioning can reveal the Gaussian query coordinates.

Write \(\lambda=\gamma/m\le1\), \(Y=\|y\|/\sqrt m\), and
\(\rho(t)=\|r(t)\|/\sqrt m\). The fitting source supplies parameter
convergence, interpolation, hidden operator norms below nine, and
\[
 A(t):=\int_0^t\rho(u)\,du,\qquad A(\infty)\le2Y/\lambda.
 \tag{1}
\]
Its positive constants \(F,U_\ell\) depend only on activations and depth.
They give the following velocity bounds on the fitting event, with
\(q(t)=w(t)/\sqrt n\):
\[
 \sup_a\frac{\|\dot h_a^{(L)}(t)\|}{\sqrt n}
       \le2F\rho(t)\|q(t)\|,
 \qquad
 \|\dot W^{(\ell)}(t)\|_F
       \le2U_\ell\rho(t)\|q(t)\|,\quad\ell\ge2.
 \tag{2}
\]

## 2. A readout comparison that holds without oddness

Set
\[
 B_t=\frac1{\sqrt n}[h_1^{(L)}(t),\ldots,h_m^{(L)}(t)]
       \in\mathbb R^{n\times m},\qquad
 q_{\rm RF}=B_0(B_0^\top B_0)^{-1}y,
 \qquad E=\|q_{\rm RF}\|.
\]
Thus \(B_0^\top q_{\rm RF}=y\): \(q_{\rm RF}\) is the normalized
minimum-norm readout fitted with all hidden features frozen at initialization.
The actual dynamics are
\[
 \dot q=-\frac2mB_t r,\qquad r=B_t^\top q-y.
 \tag{3}
\]
We use the active initialization event
\(B_0^\top B_0\succeq(m\lambda/2)I_m\). In particular,
\[
 E\le\sqrt2Y/\sqrt\lambda.
 \tag{4}
\]
At an eventual width threshold the stronger Gram comparison also gives
\[
 \frac23 y^\top Q^{-1}y\le E^2\le2y^\top Q^{-1}y.
 \tag{5}
\]

The useful estimate is
\[
 \sup_{t\ge0}\|q(t)\|\le3E,
 \qquad
 \|q(\infty)-q_{\rm RF}\|
       \le96F E\left(\frac Y\lambda\right)^2.
 \tag{6}
\]
For the first inequality it is enough that
\(8F(Y/\lambda)^2\le1/2\), which follows from the source's existing
\(Y\le\lambda\beta^{-30L}\) and its stated bounds on \(F\).

Here is a derivation that avoids estimating the difference of two residual
trajectories. For a finite time horizon \(T\), put
\(M_T=\sup_{t\le T}\|q(t)\|\). By (2),
\[
 \delta_t:=\frac{\|B_t-B_0\|_{\rm op}}{\sqrt m}
       \le2F M_T A(t),\qquad t\le T.
 \tag{7}
\]
Differentiate the distance from the fixed interpolating comparator. The
identity \(B_0^\top q_{\rm RF}=y\) gives exactly
\[
 \frac12\frac d{dt}\|q-q_{\rm RF}\|^2
 =-2\rho^2+\frac2m
   \langle(B_t-B_0)^\top q_{\rm RF},r\rangle
 \le2E\delta_t\rho.
 \tag{8}
\]
Since \(q(0)=0\), integration and
\(\int_0^t A(u)\rho(u)\,du=A(t)^2/2\) yield
\[
 \|q(t)-q_{\rm RF}\|^2
       \le E^2+4F M_T E A(T)^2.
\]
The triangle inequality at a maximizing time implies
\(M_T\le E+\sqrt{E^2+4FM_TE A(T)^2}\). If \(M_T>E\), squaring and
dividing by \(M_T\) gives
\[
 M_T\le2E(1+2F A(T)^2).
\]
The same upper bound already holds when \(M_T\le E\). Equation (1)
and the label cap prove the first assertion of (6), uniformly in \(T\).

Let \(P\) be the orthogonal projection onto the column space of \(B_0\).
Projecting the integrated readout equation onto its orthogonal complement,
then using (7), gives
\[
 \|(I-P)q(\infty)\|
 \le2\int_0^\infty\delta_t\rho(t)\,dt
 \le2F M A(\infty)^2
 \le24F E(Y/\lambda)^2,
 \tag{9}
\]
where \(M=\sup_t\|q(t)\|\le3E\). On the column space, interpolation at
the actual endpoint gives
\[
 B_0^\top(q(\infty)-q_{\rm RF})
       =-(B_\infty-B_0)^\top q(\infty).
\]
The smallest singular value of \(B_0\) is at least
\(\sqrt{m\lambda/2}\), so
\[
 \begin{split}
 \|P(q(\infty)-q_{\rm RF})\|
 &\le\sqrt{2/\lambda}\,\delta_\infty M\\
 &\le 2\sqrt2F M^2A(\infty)/\sqrt\lambda\\
 &\le72F E(Y/\lambda)^2.
 \end{split}
 \tag{10}
\]
The last step uses (1), (4), and \(M\le3E\). Adding (9) and (10)
proves (6). This proof uses actual training and fitting; it is not a
linearization in the label amplitude.

## 3. Odd activations give a fluctuation-scale endpoint remainder

Assume here that every activation is odd and globally Lipschitz, with
Lipschitz constant \(s_\ell\). Values may be unbounded. Every query feature
map is then odd in \(Z\), for every choice of hidden matrices; its mean is
zero. Define the initialized query Lipschitz constants
\[
K_1=s_1,\qquad K_\ell=8s_\ell K_{\ell-1}.
\]
Gaussian Poincare applied to each scalar linear combination gives
\[
 \operatorname{Cov}_Z h_0^{(\ell)}\preceq K_\ell^2 I_n.
 \tag{11}
\]
Consequently, for any deterministic matrix \(D\),
\[
 \mathbb E_Z\|D h_0^{(\ell)}\|^2
       \le K_\ell^2\|D\|_F^2.
 \tag{12}
\]
The source's Hermite proof of Gaussian Poincare applies: these maps are
Lipschitz, have linear growth, and have square-integrable gradients.

For trained and initialized hidden matrices define
\(D_\ell=(\mathbb E_Z\|h^{(\ell)}-h_0^{(\ell)}\|^2)^{1/2}\).
Here \(D_1=0\), because the orthogonal query's first preactivation is
unchanged. Subtracting the forward equations, using the trained operator
norm bound and (12), gives
\[
 D_\ell\le s_\ell\left(9D_{\ell-1}
       +K_{\ell-1}\|W^{(\ell)}-W_0^{(\ell)}\|_F\right).
 \tag{13}
\]
Equations (1), (2), and (6) improve the hidden displacement estimate to
\[
 \|W^{(\ell)}_\infty-W_0^{(\ell)}\|_F
       \le12U_\ell E Y/\lambda.
 \tag{14}
\]
Define deterministic coefficients
\[
 T_1=0,\qquad
 T_\ell=s_\ell(9T_{\ell-1}+K_{\ell-1}U_\ell),\qquad
 \mathcal D_{\phi,L}=96F K_L+36\sqrt2 T_L.
 \tag{14a}
\]
Then (13)--(14) give \(D_L\le12T_L E Y/\lambda\).
This is a bound for the total vector in Gaussian
\(L^2\), without a factor \(\sqrt n\).

Define the frozen-feature fitted query predictor by
\[
 f_{{\rm RF},n}(v)=\frac1{\sqrt n}q_{\rm RF}^\top h_0^{(L)}(Z).
\]
Conditioned on an active training realization in the fitting event, all
matrices and readouts in the following inequality are deterministic. By
(6), (11), and (13)--(14),
\[
 \begin{split}
 \|f_n(\infty,v)-f_{{\rm RF},n}(v)\|_{L^2(Z)}
 &\le\frac1{\sqrt n}\left[
 K_L\|q_\infty-q_{\rm RF}\|+\|q_\infty\|D_L\right]\\
 &\le\frac{\mathcal D_{\phi,L}E}{\sqrt n}
                 \left(\frac Y\lambda\right)^2.
 \end{split}
 \tag{15}
\]
Indeed the readout-error term is at most
\(96FK_L E(Y/\lambda)^2/\sqrt n\). The feature-error term is at most
\(36T_L E^2Y/(\lambda\sqrt n)\), and
\(E\lambda/Y\le\sqrt{2\lambda}\le\sqrt2\).
Both predictors in (15) have conditional mean zero. Thus (15) directly
controls their fluctuations and is stronger than a width-independent
absolute endpoint error of order \(Y^3\).

To turn (15) into the requested endpoint lower bound, one still needs a
proved frozen-feature fluctuation lower bound and a comparison of its
constant with the explicit remainder constant. A last-layer innovation
calculation is a plausible independent route to the frozen-feature bound;
it is not proved in this note. If its fluctuation coefficient is
\(\sqrt{q_L}\sqrt{y^\top Q^{-1}y}\), where
\[
 q_1=\mathbb E\phi_1(G)^2,\qquad
 q_\ell=\mathbb E\phi_\ell(\sqrt{q_{\ell-1}}G)^2,
 \qquad G\sim N(0,1),
 \tag{16}
\]
then the clean sufficient additional condition
\[
 \mathcal D_{\phi,L}(Y/\lambda)^2\le\sqrt{q_L}/100
 \tag{17a}
\]
makes the one-run conditional \(L^2\) remainder at most one hundredth
of \(\sqrt{q_L}E/\sqrt n\). A probability comparison can then use
Markov's inequality for each remainder together with the separately proved
frozen-feature lower bound; its numerical constants must be coordinated
with that lower bound's probability and threshold. It is not justified simply to replace
that comparison by the original \(\beta^{-30L}\) cap: the stated envelope
\(\beta\) does not give a positive lower bound on \(q_L\). For example,
the odd activation
\(\phi_T(z)=\tanh(z-T)+\tanh(z+T)\) has uniform strip derivative
bounds and \(\phi_T(0)=0\), while
\(\mathbb E\phi_T(G)^2\to0\) as \(T\to\infty\), by dominated
convergence. Sharper cancellation or activation-sensitive constants are
needed to retain the exact existing cap uniformly over this class.

The explicit constant above also yields a useful sufficient subclass under
the original cap. The fitting source gives
\(F\le\beta^{10L}/64\), because \(H\ge1\) and
\(8H\sqrt F\le\beta^{5L}\). Moreover
\[
 K_\ell\le\beta^{2\ell},\qquad
 U_\ell\le\beta^{4L-2\ell+2},\quad\ell\ge2.
\]
For the latter bound use
\(U_\ell=2Hs(9s)^{L-\ell}\),
\(H\le(2\beta)^L\le\beta^{2L}\), \(s\le\beta\), and
\(9\beta\le\beta^2\). Expanding (14a) as a geometric sum gives
\[
 T_L\le\sum_{j=2}^L\beta^{6L-2j+1}
       \le\beta^{6L-2},\qquad
 \mathcal D_{\phi,L}\le\beta^{13L}.
 \tag{17b}
\]
Thus if \(q_L\ge\beta^{-10L}\), the original cap implies (17a):
\(\mathcal D_{\phi,L}(Y/\lambda)^2\le\beta^{-47L}
\le\beta^{-5L}/100\). In particular this applies when the odd activations
are normalized to give \(q_L=1\).

It also applies to arbitrary fixed-depth combinations of
\(\tanh z\), \(\arctan z\), \(\sin z\), and \(z+\tanh z\).
For each such activation and every \(q>0\),
\[
 \mathbb E\phi(\sqrt qG)^2\ge\frac1{100}\min\{q,1\}.
 \tag{17c}
\]
For tanh and arctan, restrict to \(1/2\le|G|\le1\), an event of
probability greater than \(1/5\), and use
\(\tanh u,\arctan u\ge u/2\) for \(0\le u\le1\), together with
monotonicity for larger \(u\). This gives the stronger constant \(1/80\).
For sine, the Gaussian characteristic function gives exactly
\(\mathbb E\sin(\sqrt qG)^2=(1-e^{-2q})/2\ge\min\{q,1\}/3\).
Finally \(|z+\tanh z|\ge|z|\). Starting at \(q_0=1\), (17c) implies
\(q_L\ge100^{-L}\ge\beta^{-10L}\). These checks establish that the
readout-comparison error has sufficient size under the original cap for
these examples, including the unbounded activation \(z+\tanh z\).
The frozen-feature fluctuation theorem remains a separate proof obligation.

## 4. Why full covariance coercivity fails with nonzero means

Take two admissible nonaffine activations
\[
 \phi_1(z)=1+z+\tanh z,\qquad \phi_2(z)=\tanh z.
\]
Both are holomorphic on a fixed strip with bounded strip derivative; the
first is unbounded. Write
\(h^{(1)}=\mathbf1+\xi\), where
\(\xi_j=Z_j+\tanh Z_j\) are independent, centered, and have variance
\(\sigma^2\le4\). For an initialized row \(b_i^\top\), put
\(\mu_i=b_i^\top\mathbf1\). These means are independent \(N(0,1)\)
variables across rows. With probability tending to one,
\[
 \max_i\mu_i\ge\sqrt{\log n},\qquad\max_i\|b_i\|\le2.
 \tag{17}
\]
For the first assertion, the Gaussian tail integrated over
\([t,t+1/t]\) is at least \(c e^{-t^2/2}/t\) for \(t\ge1\).
Taking \(t=\sqrt{\log n}\), the probability that none of the \(n\)
means exceeds \(t\) tends to zero. The second assertion follows from
the chi-square exponential bound and a union over the rows.

For any row with \(\mu>0\) and \(\|b\|\le2\), Chebyshev gives
\(\Pr_Z(b^\top\xi<-\mu/2)\le16\sigma^2/\mu^2\). On the
complement, \(1-\tanh(\mu+b^\top\xi)\le2e^{-\mu}\).
Therefore
\[
 \operatorname{Var}_Z\tanh(b^\top h^{(1)})
 \le\mathbb E_Z[1-\tanh(b^\top h^{(1)})]^2
 \le\frac{64\sigma^2}{\mu^2}+4e^{-2\mu}.
 \tag{18}
\]
Using the row in (17) shows
\[
 \lambda_{\min}\big(\operatorname{Cov}_Z h_0^{(2)}\big)
 \le\min_i\operatorname{Var}_Z h_{0,i}^{(2)}
 \xrightarrow{\mathbb P}0.
 \tag{19}
\]
The bounded choice \(\phi_1(z)=1+\tanh z\) gives the same obstruction.
Hence a width-independent full covariance gap is false before any training.
This is not a counterexample to an endpoint lower bound in the actual
fitted readout direction.

There is also a direct obstruction to uniform robustness over a Frobenius
ball. In this example, perturb only the first mixer row by
\(\varepsilon\mathbf1^\top/\sqrt n\), for a fixed
\(\varepsilon>0\). The perturbation has Frobenius norm \(\varepsilon\),
but shifts that neuron's query preactivation mean by
\(\varepsilon\sqrt n\); its centered preactivation variance remains
bounded. Its output variance tends to zero by the same argument as (18).
This perturbation is not asserted to be produced by training. It shows
that the fitting theorem's Frobenius displacement estimate alone cannot
give the requested covariance robustness.

For arbitrary means \(\mu_\ell=\mathbb E_Z h_0^{(\ell)}\), the exact
replacement for (12) is
\[
 \mathbb E_Z\|D h_0^{(\ell)}\|^2
 =\operatorname{tr}\big(D\operatorname{Cov}(h_0^{(\ell)})D^\top\big)
      +\|D\mu_\ell\|^2.
 \tag{20}
\]
The second term need not be width-independent. Centering the final output
does not remove its effect before a nonlinear activation. A full-class
extension therefore requires a directional estimate for the actual trained
readout, or quantitative control of training-induced mean shifts and the
associated weighted covariance. Merely discarding saturated neurons does
not suffice: without a positive-semidefinite weighted lower bound, their
cross-covariances can cancel a selected good-row contribution.

## 5. A further arbitrary-depth result for odd activations

The odd case also has a uniform covariance statement that is weaker than
coercivity but requires no small perturbation radius. For fixed positive
radius \(R\), take all hidden matrices satisfying
\(\|W^{(\ell)}-W_0^{(\ell)}\|_F\le R\), with their operator norms
bounded by a fixed number. Then, uniformly over these choices,
\[
 \frac1n\operatorname{tr}\operatorname{Cov}_Z h^{(L)}
       \xrightarrow{\mathbb P}q_L>0.
 \tag{21}
\]
To prove this, first consider initialized features jointly over the query
and the initialized matrices. Their empirical squared norms converge in
\(L^1\) to (16). At the first layer this is the law of large numbers.
At each next layer, condition on the preceding features: the rows are
independent Gaussian projections of variance equal to the preceding
empirical squared norm. The conditional variance of their averaged squared
activations is at most \(C(1+q^2)/n\), by linear growth and the Gaussian
fourth moment. Induction bounds the second moments of these empirical norms;
continuity of \(q\mapsto\mathbb E\phi_\ell(\sqrt qG)^2\), linear growth,
and uniform integrability then give the asserted \(L^1\) convergence.
Conditioning only on the matrices preserves it, since conditional expectation
is an \(L^1\) contraction. Oddness makes this conditional squared norm
equal to the covariance trace. Every \(q_\ell\) is positive for a
nonconstant odd activation: otherwise that continuous activation vanishes
on the support of a nondegenerate Gaussian and hence everywhere.

Equation (13) gives a uniform bound \(D_L\le C R\) for these perturbed
features. Hence
\[
 \left|\mathbb E\|h^{(L)}\|^2-
             \mathbb E\|h_0^{(L)}\|^2\right|
 \le D_L\left(2\|h_0^{(L)}\|_{L^2}+D_L\right)=O(\sqrt n).
\]
After division by \(n\), this proves (21). A global query Lipschitz bound
also gives \(\operatorname{Cov}_Z h^{(L)}\preceq K^2I_n\), with a fixed
\(K\). Once its trace is at least \(nq_L/2\), at least
\(nq_L/(4K^2)\) eigenvalues are at least \(q_L/4\): if their number
is \(N\), the trace is at most \(NK^2+(n-N)q_L/4\).

This proves that a positive fraction of query directions remain variable
at arbitrary fixed depth, uniformly over the stated perturbations. It does
not locate the actual fitted readout in that eigenspace. Equation (15) is
the more direct endpoint route for odd activations; (19)--(20) identify why
the same argument does not yet cover general noncentered activations.
