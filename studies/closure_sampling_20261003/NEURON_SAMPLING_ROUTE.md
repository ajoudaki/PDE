# Sampling neurons of the actual initialized mixer

2026-10-03. Scoped research route; internally derived calculations, not a
compression theorem or an impossibility theorem for general encoders.

The question is whether an order-$q$ residual-RMS memory closure for the
actual width-$n$ network can be represented with $n^{5/4-\epsilon}$ moving
coordinates, for some fixed $\epsilon>0$, while retaining an all-time query
prediction error $n^{-1/2+o(1)}$. This note tests neuron subsampling and
stratification. The exact calculations identify information that a useful
sampling construction has to preserve, and a conditional route that would
beat the count. They do not prove that the desired construction is impossible.

Scientific inputs read: the model and residual-clock construction in
`paper/main.tex`; complete `paper/results.tex`, `paper/proof_alltime.tex`,
and `paper/proof_tracking.tex`; the explicitly authorized
`studies/dense_cutoff_population_rate_20261001/Q_ORDER_RESULT.md` and
complete `NONORTHOGONAL_DIRECT_ROUTE.md`. The prior result is used only to
specify the assigned baseline, not independently recertified here. No sibling
route, unrelated study, experiment, or Git operation was used. The canonical
notation skill, its neural reference, and the rigorous-math skill were applied.

## 1. Reference system and what a sampling estimate must control

There are fixed training pairs $(x_a,y_a)$, $1\le a\le m$, with
$v_a=x_a/\sqrt d$ and $\|v_a\|_2=1$. The first weights
$A=W^{(1)}\in\mathbb R^{n\times d}$, hidden matrix
$W=W^{(2)}\in\mathbb R^{n\times n}$, and readout $w\in\mathbb R^n$
give
\[
h_a^{(1)}=\tanh(Av_a),\qquad
z_a^{(2)}=Wh_a^{(1)},\qquad
h_a^{(2)}=\tanh z_a^{(2)},\qquad
f_a=n^{-1}w^\top h_a^{(2)}.
\]
Put $r_a=f_a-y_a$, $\rho=(m^{-1}\sum_a r_a^2)^{1/2}$, and
$Y=(m^{-1}\sum_a y_a^2)^{1/2}$. The loss is $\rho^2$ and the block
mobilities are $(n,1,n)$. Thus
\[
\delta_a^{(2)}=w\odot\operatorname{sech}^2z_a^{(2)},\qquad
\delta_a^{(1)}=\operatorname{sech}^2(Av_a)\odot W^\top\delta_a^{(2)},
\]
\[
\dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,
\quad \dot W=-\frac2{mn}\sum_a r_a\delta_a^{(2)}h_a^{(1)\top},
\quad \dot w=-\frac2m\sum_a r_a h_a^{(2)}.
\]
Initially $A_0$ has independent $N(0,1)$ entries, $W_0$ has independent
$N(0,1/n)$ entries, and $w_0=0$. Compatible duplicate/antipodal classes
may be quotiented with sample weights; the calculations below also apply
without quotienting. The one-sample examples are compatible sphere data.

The reference closure retains $W_0$ and evolves $A,w$, one clock, and
the $2mnq$ entries of $\bar h_{a,j}^{(1)},\bar\delta_{a,j}^{(2)}$.
The clock obeys $\dot\tau=\rho$, $\tau(0)=1$. These moments are
integrals against shifted Legendre polynomials $p_j(\xi/\tau)$, of
$h_a^{(1)}$ and $r_a\delta_a^{(2)}/\rho$, with the constant forward
and zero backward unit prefixes. Its reconstruction is
\[
\widehat W=W_0-\frac2{mn\tau}\sum_{a,j<q}(2j+1)
       \bar\delta_{a,j}^{(2)}\bar h_{a,j}^{(1)\top}.
\]
For either moment $M_j$, dilation contributes
$-(\rho/\tau)[jM_j+\sum_{k<j}(2k+1)M_k]$; the forward and backward
sources are $\rho h_a^{(1)}$ and $r_a\delta_a^{(2)}$, respectively.
The physical first/readout equations remain the displayed equations.
Every source is evaluated in this reconstructed state.

The assigned sufficient baseline is $q=n^{1/4+o(1)}$, with moving count
$n^{5/4+o(1)}$. Sampling each population down to $N$ would nominally give
$2mNq+N(d+1)+O(1)$. Keeping $n$ first-layer/readout coordinates and
compressing only the histories gives $2mNq+n(d+1)+O(1)$ instead. Either
count beats the exponent if $N\le n^{1-\epsilon+o(1)}$. Neither count
proves that the sampled histories supply the actual mixer actions.

For queries the target metric is
\[
\mathcal E_\mu(g,f)=
\left(\int\sup_{t\ge0}|g(t,x)-f(t,x)|^2\,d\mu(x)\right)^{1/2}.
\]
The established comparison controls full normalized parameter distance.
A width reduction need not control that distance, so failure of strong
matrix/vector coupling below is not a prediction lower bound.

## 2. Direct column subsampling has order-one forward mismatch

Condition on $A_0$ and take one fixed input with first features
$h=\tanh(A_0v)$. Choose $S\subset\{1,\ldots,n\}$, $|S|=N$, using
$A_0$ but not the rows of $W_0$. For an original top neuron $j$ define
\[
z_j=\sum_{i=1}^n(W_0)_{ji}h_i,
\qquad
\widetilde z_j=\sqrt{n/N}\sum_{i\in S}(W_0)_{ji}h_i.
\]
The factor $\sqrt{n/N}$ gives the usual variance-$1/N$ narrower mixer.
Conditionally these are centered jointly Gaussian, with
\[
\begin{aligned}
\mathbb E z_j^2&=\|h\|_2^2/n,\qquad
\mathbb E\widetilde z_j^2=\|h_S\|_2^2/N,\\
\mathbb E[z_j\widetilde z_j]&=\sqrt{n/N}\,\|h_S\|_2^2/n,\\
\mathbb E|z_j-\widetilde z_j|^2
&=\frac{\|h_{S^c}\|_2^2}{n}
 +(\sqrt{n/N}-1)^2\frac{\|h_S\|_2^2}{n}.
\end{aligned} \tag{1}
\]
If both empirical feature energies tend to the same positive $s^2$,
the correlation tends to $\sqrt{N/n}$ and (1) equals
$2s^2(1-\sqrt{N/n})+o(1)$. Thus $N=o(n)$ does not couple the actual
forward coordinates closely, even at initialization.

The unbiased Horvitz--Thompson sum uses $n/N$ instead. Averaging also
over a uniform size-$N$ subset gives
\[
\mathbb E\left|\frac nN\sum_{i\in S}(W_0)_{ji}h_i-z_j\right|^2
=\left(\frac nN-1\right)\frac{\|h\|_2^2}{n}. \tag{2}
\]
This is a Gaussian sum, not an empirical average of order-one terms.
Writing $W_0h=n^{-1}\sum_i[n(W_0)_{ji}]h_i$ exposes why an ordinary
quadrature theorem with width-independent integrand bounds is inapplicable:
the bracketed random coefficient has variance $n$.

## 3. Conditioning on the complete initial training forward pass

One might avoid (1) by preserving all initial training fields as fixed
data and stratifying neurons using these fields. This still leaves a
quantifiable adjoint innovation.

Write $H=[h_1^{(1)}(0),\ldots,h_m^{(1)}(0)]$, $Z=W_0H$, and let
$r_H=\operatorname{rank}H$. Define
\[
H^\dagger=(H^\top H)^\dagger H^\top,
\qquad P=HH^\dagger,\qquad P^\perp=I-P.
\]
The dagger on the symmetric Gram is its Moore--Penrose inverse. Conditional
on $A_0,Z$, exact Gaussian orthogonal projection gives
\[
W_0=ZH^\dagger+n^{-1/2}G P^\perp, \tag{3}
\]
in conditional law, where $G$ is an independent matrix of independent
$N(0,1)$ entries. To verify (3), decompose each isotropic Gaussian row
into its orthogonal projections on $\operatorname{col}H$ and its
orthogonal complement. The first projection is fixed by its product
with $H$; the second is independent and has covariance $P^\perp/n$.
No invertibility of $H^\top H$ is required.

For any response vector $u=u(A_0,Z)\in\mathbb R^n$,
\[
W_0^\top u=H(H^\top H)^\dagger Z^\top u
                   +n^{-1/2}P^\perp G^\top u. \tag{4}
\]
The last term has conditional covariance
$(\|u\|_2^2/n)P^\perp$. Its expected squared RMS is exactly
\[
\mathbb E\left[\frac1n\|n^{-1/2}P^\perp G^\top u\|_2^2
       \,\middle|\, A_0,Z\right]
=\left(1-\frac{r_H}{n}\right)\frac{\|u\|_2^2}{n}. \tag{5}
\]

This response already occurs in the actual training dynamics. Since
$w(0)=0$, both hidden velocities vanish and
\[
u_{a,j}:=\dot\delta_{a,j}^{(2)}(0)
=\frac2m\sum_b y_b\tanh(Z_{jb})\operatorname{sech}^2(Z_{ja}),
\quad
\frac{d}{dt}\left[W^\top\delta_a^{(2)}\right]_{t=0}=W_0^\top u_a.
\tag{6}
\]
Moreover
\[
\ddot A(0)=\frac2m\sum_a y_a
 \left[\operatorname{sech}^2(A_0v_a)\odot W_0^\top u_a\right]v_a^\top.
\tag{7}
\]
The same identities hold at every closure order: its initial hidden
velocity is zero and the first-layer/readout equations are unchanged.
For one sample with nonzero $y$, $u_j=2y\tanh Z_j\operatorname{sech}^2Z_j$.
Conditional laws of large numbers give
\[
\frac{\|u\|_2^2}{n}\longrightarrow
4y^2\mathbb E[\tanh^2 Z_*\operatorname{sech}^4Z_*]>0,
\quad
Z_*\sim N(0,\mathbb E\tanh^2 G_*),\ G_*\sim N(0,1).
\tag{8}
\]
The inequality holds because the variance is positive and the integrand
is positive except at a set of Gaussian measure zero. Thus initial
forward marks leave order-$Y$ RMS backward randomness, entering actual
hidden learning at order $Y^2$.

## 4. No forward-mark stratification removes this adjoint innovation

Allow a subset $S$ and arbitrary real coefficients $\alpha_j$ measurable
with respect to $A_0,Z$. Consider any retained-row estimator
$\widetilde k=\sum_{j\in S}\alpha_j(W_0)_{j,:}^\top u_j$.
In (3), its difference from $k=W_0^\top u$ has a conditional Gaussian
component with covariance
\[
\frac1n\sum_j(\alpha_j\mathbf1_{j\in S}-1)^2u_j^2\,P^\perp.
\]
Consequently
\[
\mathbb E\left[\frac{\|\widetilde k-k\|_2^2}{n}
                 \,\middle|\,A_0,Z\right]
\ge\left(1-\frac{r_H}{n}\right)\frac1n\sum_{j\notin S}u_j^2.
\tag{9}
\]
The omitted conditional mean can only increase this expectation. Since
$|u_{a,j}|\le2Y$, deleting $N$ rows removes at most $4Y^2N$ from
$\sum_j u_{a,j}^2$. For the one-sample nonzero-label example, (8)--(9)
stay bounded below by $cy^2$ when $N=o(n)$, regardless of the chosen
strata and weights. Because the conditional residual is isotropic on
a rank-$n-r_H$ subspace, its squared norm also concentrates around its
conditional mean when coefficients and $u$ are fixed.

For a uniform size-$N$ subset with $\alpha_j=n/N$, the expected
conditional Gaussian squared-RMS discrepancy is exactly
\[
\left(1-\frac{r_H}{n}\right)
\left(\frac nN-1\right)\frac{\|u\|_2^2}{n}. \tag{10}
\]
Stratification can reduce the regression term in (4), but has no access
to the remaining independent Gaussian coordinates if its marks contain
only $A_0,Z$. Sampling based on the full mixer or precomputed adjoint
marks is outside (9), and can escape this particular argument.

## 5. A query coefficient also retains unsampled randomness

The vector obstruction alone does not rule out weak cancellation in
predictions. A second calculation directly tests a query observable,
while retaining its deliberately restricted sampling class.

Take one training direction $v=e_1$ and a passive query direction
$v_x=e_2$ in $d\ge2$. Put
$h=\tanh(A_0e_1)$, $h_x=\tanh(A_0e_2)$, $z=W_0h$, and
$z_x=W_0h_x$. Conditional on $A_0,z$,
\[
z_{x,j}=c_nz_j+\sigma_n\eta_j,\qquad
c_n=\frac{h^\top h_x}{\|h\|_2^2},\qquad
\sigma_n^2=\frac{\|h_x-c_nh\|_2^2}{n}, \tag{11}
\]
where the $\eta_j$ are independent standard Gaussians. Bounded independent
first-layer features give $c_n=O_{\mathbb P}(n^{-1/2})$ and
$\sigma_n^2\to s^2:=\mathbb E\tanh^2G_*>0$. A Gaussian union bound
gives $\max_j|z_j|=O_{\mathbb P}(\sqrt{\log n})$. Hence, with
probability tending to one, $\max_j|c_nz_j|\le1$ and
$\sigma_n\in[s/2,2s]$.

On that event the conditional variances
\[
V_j=\operatorname{Var}[\tanh(c_nz_j+\sigma_n\eta_j)\mid A_0,z]
\]
have a common positive lower bound $v_0$. Indeed, this variance is a
continuous strictly positive function of $(\mu,\sigma)$ on the compact
set $[-1,1]\times[s/2,2s]$; positivity follows because tanh of a
nondegenerate Gaussian is not constant.

The query/training initial kernel and a weighted row estimate are
\[
K_n(x,v)=\frac1n\sum_j\tanh(z_{x,j})\tanh z_j,
\qquad
\widetilde K(x,v)=\sum_{j\in S}\omega_j\tanh(z_{x,j})\tanh z_j,
\]
where $S,\omega$ depend on $A_0,z$, and $|S|=N$. Conditional independence
in (11) yields the exact variance
\[
\operatorname{Var}[\widetilde K-K_n\mid A_0,z]
=\sum_j(\omega_j\mathbf1_{j\in S}-1/n)^2\tanh^2z_j\,V_j.
\tag{12}
\]
Suppose the sampler retains a nondegenerate initial training Gram,
$\sum_{j\in S}\omega_j\tanh^2z_j\ge\kappa>0$; a consistent sampler
must satisfy such an inequality. For $N/n\le\kappa/2$,
\[
\sum_{j\in S}(\omega_j-1/n)\tanh^2z_j\ge\kappa/2.
\]
Cauchy--Schwarz, and $\sum_{j\in S}\tanh^2z_j\le N$, give
\[
\sum_{j\in S}(\omega_j-1/n)^2\tanh^2z_j\ge\frac{\kappa^2}{4N}.
\]
Thus
\[
\operatorname{Var}[\widetilde K-K_n\mid A_0,z]
\ge\frac{v_0\kappa^2}{4N}. \tag{13}
\]
This permits signed weights and biased estimators: their conditional
mean-square error is at least the variance. The weights may depend on all
first-layer initialization, so knowing the query direction and its first
features does not by itself evade (13). Using the actual top query field
$z_x$ to select the rows does evade its measurability hypothesis.

Since $\dot f(0,x)=2yK_n(x,v)$ for dense training and every order of the
closure, (13) gives a conditional mean-square lower bound $cy^2/N$ for
this particular approximation to the initial prediction velocity. It is
not by itself an all-time prediction lower bound: converting it to one
requires control of later correlated terms on a time interval that does
not shrink too quickly with $n$. No such conversion is asserted here.
It nevertheless disproves a claimed better-than-Monte-Carlo bound for
this observable based solely on initial training-forward stratification.

Conversely, finitely many prescribed query coefficients can be added to
the strata or matched by weighted cubature. No universal claim against
all query-aware sampling follows from (13).

## 6. What finite-dimensional stratification could actually buy

Here is a precise sufficient quadrature mechanism, separated from the
unproved neural representation. Suppose an empirical population of $n$
marks $\xi_i\in\mathbb R^D$ is partitioned into $N$ nonempty cells
$C_s$ of masses $p_s=|C_s|/n$, with $p_s\le C/N$ and diameter at most
$h_N\le C N^{-1/D}$. Choose one index $I_s$ independently and uniformly
inside each cell. For a fixed Hilbert-valued $L$-Lipschitz integrand $F$,
\[
Q_NF=\sum_s p_sF(\xi_{I_s}),\qquad
\mathbb E[Q_NF\mid\xi]=\frac1n\sum_iF(\xi_i),
\]
and independence and centering give
\[
\mathbb E\left\|Q_NF-\frac1n\sum_iF(\xi_i)\right\|^2
=\sum_s p_s^2\mathbb E\|F(\xi_{I_s})-\mathbb E_sF\|^2
\le C L^2N^{-1-2/D}. \tag{14}
\]
This is an unbiased approximation of the actual empirical population;
there is no population-limit bias in (14). The assumed balanced small
cells have to be constructed for the mark distribution, with Gaussian
tails accounted for. Their existence is not automatic for every point cloud.

If all required evolving contractions and both directions of random mixing
admitted this fixed-$D$ description, if their uniform Lipschitz/complexity
loss were $n^{o(1)}$, and if their all-time feedback amplification were
$n^{o(1)}$, (14) would suggest
\[
N=n^{D/(D+2)+o(1)},\qquad q=n^{1/4+o(1)},\qquad
Nq=n^{5/4-2/(D+2)+o(1)}. \tag{15}
\]
Even if one retained all $n(d+1)$ physical root/readout coordinates,
the moving count would be
$n^{\max\{1,\,5/4-2/(D+2)\}+o(1)}$.
For any fixed $D$, this is a strict improvement on $5/4$.

The missing assertion is not a generic quadrature theorem. It is the
existence of the stated neural representation, preserving actual
$W_0,W_0^\top$, with sufficiently small residual error. Equations
(3)--(10) show that initial forward marks alone are not such a representation.
Independent fresh Gaussian replacement supplies a law, but loses the
specific initialized realization and its reused-matrix response.

## 7. Concrete control variates and the next unavoidable estimates

Equation (4) suggests a useful first repair: precompute the exact initial
adjoint fields $W_0^\top u_a$ as additional fixed marks. This costs $mn$
fixed numbers and exact mixer calls at setup, and retains (6)--(7).
It is permitted by a moving-state criterion, but does not yet evaluate
$W_0^\top\delta_a^{(2)}(t)$ for later, adaptively changed responses.

More generally, for fixed forward and backward query bases $V$ and $U$,
the exact finite Gaussian decomposition is
\[
W_0=Y_V(V^\top V)^{-1}V^\top
 +U(U^\top U)^{-1}Q_U^\top P_{V^\perp}
 +P_{U^\perp}\widetilde W P_{V^\perp},
\quad Y_V=W_0V,\quad Q_U=W_0^\top U, \tag{16}
\]
when the columns of each basis are independent. The consistency relation
$U^\top Y_V=Q_U^\top V$ verifies both constraints; orthogonal projection
identifies the independent conditional Gaussian remainder.
Its action on a new forward query $h$ has fresh squared RMS expectation
\[
\left(1-\frac{\operatorname{rank}U}{n}\right)
\frac{\|P_{V^\perp}h\|_2^2}{n}, \tag{17}
\]
and the reverse expression is obtained by interchanging $U,V$.
The bases can therefore preserve reuse exactly on their spans.

A possible construction must establish small residual distances in (17)
for every actual training/query field, or prove that the remaining
innovations cancel sufficiently in the required prediction observables.
This is a concrete approximation problem for evolving query subspaces.
It cannot be answered by counting only the $q$ moments: applying tanh or
its gate to a linear combination of known directions can create a new
direction outside their linear span. Conversely, this observation supplies
no lower bound on the number of directions needed to a specified accuracy.

At small fixed $Y$, the new fields beyond an early perturbation order may
have small powers of $Y$. A fixed neglected term $CY^p$ nevertheless does
not tend to zero with $n$. An argument based on a geometric remainder
$C\gamma^p$, $0<\gamma<1$, would need
$p\ge(\tfrac12+o(1))\log n/|\log\gamma|$. Such a remainder and the
resulting number of necessary Gaussian directions are both unproved here.
This is where an effective finite dimension could survive, or fail.

## 8. Feedback, clocks, and bias accounting

Unbiasedness in (14) is for a fixed integrand conditional on the point
cloud. Once the same sampled nodes determine the state, its current
integrand depends on the sample. It is invalid to reapply (14) pointwise
to that adaptive integrand without a uniform class estimate or a different
coupling argument. The moments, residual, and clock are all affected:
$\dot\tau=\rho$ must use the sampled model's own residual, and each
moment contains the entire earlier feedback.

A viable strong comparison would need a time-integrated defect estimate
of the form
\[
\int_0^\infty\|E_{\mathrm{sampling}}(t)\|\,dt
\le n^{o(1)}N^{-1/2-1/D}+\beta_{n,N}, \tag{18}
\]
in a norm for which an appropriate fitting and stability theorem holds.
Here $\beta_{n,N}$ includes systematic reconstruction or conditional-mean
error. The present manuscript's stability theorem applies to the same
initialized physical parameter space; it is not automatically a theorem
for a narrower network. A weak observable comparison could replace (18),
but must then be proved for the query norm with the time supremum inside.

If instead a sampler targets a population closure or population dense
flow, the necessary triangle inequality has a separate finite-width term:
\[
\mathcal E_\mu(\widetilde f_{N,q},\widehat f_{n,q})
\le\mathcal E_\mu(\widetilde f_{N,q},f_\infty)
 +\mathcal E_\mu(f_\infty,f_{n,D})
 +\mathcal E_\mu(f_{n,D},\widehat f_{n,q}). \tag{19}
\]
The middle term includes the actual width-$n$ population discrepancy;
it is not supplied with an $n^{-1/2+o(1)}$ rate by the manuscript's
qualitative convergence theorem. The first term includes both discretizing
the population random fields and any population closure bias. Merely
replacing $n$ by $N$ in the original theorem does not establish the desired
joint accuracy. Direct empirical stratification avoids that particular
population term only if it really approximates the actual finite model,
including (3), (16), their adaptive constraints, and query fields.

## 9. Route verdict

There is no certified $n^{5/4-\epsilon}$ representation from this route.
There are three quantitative findings rather than a universal obstruction:

1. Submatrix width reduction has order-one initialized forward discrepancy,
   and unbiased Gaussian-sum rescaling amplifies variance by $n/N$.
2. Conditioning on all initial training forward fields leaves an explicit
   order-$Y$ adjoint innovation. Any retained-row estimator selected only
   from those forward marks misses order-one relative RMS energy when
   $N=o(n)$. This innovation enters actual hidden learning immediately.
3. Training-forward stratification alone retains a $c/N$ conditional
   mean-square error in an actual unseen-query kernel coefficient, even
   when its sampled training Gram stays nondegenerate.

The promising repair is response-aware control variates or stratification
of a joint Gaussian source representation. Formulae (14)--(18) state the
gain and the exact missing estimates. A proof must bound the effective
source dimension, preserve both orientations of the same mixer, control
adaptive feedback uniformly through the fitted endpoint, and account for
any population or reconstruction bias. These obligations remain open here.
