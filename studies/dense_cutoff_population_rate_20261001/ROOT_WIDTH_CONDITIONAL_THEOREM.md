# A strict all-time root-width theorem with one local response hypothesis

This is a conditional research theorem for the actual unclipped dense flow. Its one unproved response hypothesis is stated below in finite-network variables. The theorem covers two tanh hidden layers and fixed orthonormal training inputs. It is not a theorem for arbitrary depth or arbitrary training geometry. The derivations are internal study results, not promoted manuscript claims.

## 1. Exact model and conclusion

Fix training inputs \(x_1,\ldots,x_m\in\mathbb R^d\) with
\(x_a^\top x_b/d=\mathbf1_{a=b}\), and fixed labels \(y_a\). At width \(n\), let
\[
h(x)=\tanh(Ax/\sqrt d),\qquad g(x)=\tanh(Wh(x)),\qquad
f_n(x)=w^\top g(x)/n.
\]
Here \(A_0\) has iid standard Gaussian entries, \(W_0\) has independent iid \(N(0,1/n)\) entries, and \(w_0=0\). All three parameter blocks train. With residuals \(r_a=f_n(x_a)-y_a\), put
\[
\delta_a=w\odot(1-g_a^2),\qquad
\delta_a^{(1)}=(1-h_a^2)\odot W^\top\delta_a.
\]
The canonical dense gradient flow is
\[
\dot w=-\frac2m\sum_a r_a g_a,\quad
\dot A=-\frac2m\sum_a r_a\delta_a^{(1)}x_a^\top/\sqrt d,\quad
\dot W=-\frac2{mn}\sum_a r_a\delta_a h_a^\top.
\tag{1}
\]
There are no response-memory coordinates or clipping operations in (1).

Let \(f_\infty(t,x)\) be the manuscript's deterministic dense population limit with this initialization and data. Assume its initial readout-feature Gram has a strictly positive gap. Keep the manuscript's small fixed label assumption, reducing its threshold further if needed for the deterministic absorption below. Denote the fixed label RMS by \(Y=(m^{-1}\sum_a y_a^2)^{1/2}\). It does not vary with width.

Let \(\mu\) be any fixed probability law supported on \(\|x\|/\sqrt d\le B\). Define the whole-time prediction error
\[
\mathcal E_\mu(f_n,f_\infty)
=\left(\int\sup_{t\ge0}|f_n(t,x)-f_\infty(t,x)|^2\,d\mu(x)\right)^{1/2}.
\tag{2}
\]
This is an input-integrated functional norm with the time supremum inside the integral. It is not a supremum over the input space.

**Conditional theorem.** Under the local response hypothesis in Section 3, for every fixed \(\delta>0\) and all sufficiently large \(n\),
\[
\Pr\left\{\mathcal E_\mu(f_n,f_\infty)\le C_\delta/\sqrt n\right\}
\ge1-\delta.
\tag{3}
\]
The constant may depend on the fixed data, gap, label bound, query radius, and hypothesis constant; it is independent of width and training time. The estimate holds at the same physical time and includes the limiting fitted predictors. There is no additive nonvanishing term proportional to \(Y\).

## 2. Prescribed residual control and the only driver needed

For a path \(b=(b_a)\) starting at zero, replace \(-2r_a\,dt/m\) in (1) by \(db_a\). This defines the controlled finite network \(f_n^b\), using exactly the same forward pass and initialization. The selected deterministic path in this theorem is
\[
b_{*,a}(t)=-\frac2m\int_0^t[f_\infty(s,x_a)-y_a]\,ds.
\tag{4}
\]
The small-label fitting theorem gives a fixed bound \(S\le C Y\) on its total variation, as well as that of the actual finite residual control on its fitting event. Reparametrize (4) by its total variation \(u\), and extend constantly to \([0,S]\). The resulting deterministic path has \(\sum_a|b'_{*,a}(u)|\le1\) almost everywhere. Zero-activity intervals require no dynamics and cause no ambiguity. If \(Y=0\), both predictors are identically zero and (3) is immediate.

Only this one deterministic path is used in the response hypothesis and the stochastic comparison. No probabilistic estimate for a deterministic path is substituted at a random, initialization-dependent path.

## 3. The remaining local finite-network hypothesis

At even width \(N=2n\), split each of the two hidden layers into blocks of size \(n\). For \(s\in[0,1/2]\), put
\[
c_{ij}(s)=2(1-s)\quad\hbox{within blocks},\qquad
c_{ij}(s)=2s\quad\hbox{between blocks}.
\]
In an auxiliary controlled network, initialize \(W_{0,ij}\) independently with variance \(c_{ij}/N\), and use hidden updates
\[
dW_{ij}=\frac{c_{ij}}N\sum_a\delta_{a,i}h_{a,j}\,db_{*,a}.
\tag{5}
\]
Read-in and readout updates remain those defined in Section 2. Each row and column of \(c\) sums to \(N\). At \(s=0\), this is two independent canonical width-\(n\) networks, whose predictions are averaged. At \(s=1/2\), it is a canonical width-\(2n\) network. Both the variance and learning mobility must change as in (5) for these identities to hold.

Write \(q_N^b(u,x)=\partial_u f_N^b(u,x)\). For a tagged hidden edge \(e=(i,j)\), define
\[
\mathcal R_{N,e}(u,x;s)
=N^2\mathbb E\left[\partial_{c_e}q_N^{b_*}(u,x)
              +\frac1{2N}\partial_{W_{0,e}}^2q_N^{b_*}(u,x)\right].
\tag{6}
\]
The mobility derivative holds all initialized weights fixed; the initial-edge derivative holds the mobility fixed. Both differentiate the full past controlled trajectory. Symmetry gives one expected value for a within-block edge, \(\mathcal R_{N,\mathrm{in}}\), and one for a between-block edge, \(\mathcal R_{N,\mathrm{out}}\).

**Hypothesis H.** These derivatives have the expectation integrability and endpoint domination needed for Gaussian covariance differentiation, and
\[
|\mathcal R_{N,\mathrm{out}}(u,x;s)-\mathcal R_{N,\mathrm{in}}(u,x;s)|
\le C_B/\sqrt N
\tag{H}
\]
uniformly in even \(N\), almost every \(u\in[0,S]\), \(s\in(0,1/2)\), and for \(\mu\)-almost every query and each training query. A stronger sufficient form requires the bound on the ball of radius \(\max(B,1)\sqrt d\).

H concerns only finite networks. It assumes no population convergence rate, no independence of trained neurons, and no maximum-signal event. It asks that an edge's block type have at most root-width influence on its normalized, signed expected response. The normalizing factor \(N^2\) and the plus sign in (6) are necessary. In unnormalized units the requested contrast is \(O(N^{-5/2})\).

This is a substantive open cancellation estimate. Because it is exactly the derivative of the profiled mean, it must not be advertised as an automatically easy or weak assumption. What is proved below is that there is no further unidentified stochastic or adaptive-feedback assumption in the stated structured theorem.

## 4. Proof of the conditional theorem

### 4.1 The entire prescribed-control fluctuation

PASSIVE_QUERY_FLUCTUATIONS.md proves, for every deterministic controlled path of variation at most \(S\),
\[
\mathbb E\int\sup_{u\le S}|f_n^{b_*}(u,x)-\mathbb E f_n^{b_*}(u,x)|^2\,d\mu(x)
\le C_B S^2/n.
\tag{7}
\]
The same holds at each training point. Its proof uses finite Gaussian cavity estimates for the actual backward carriers, fourth moments of carrier products multiplied by first responses, and Gaussian variance inequalities. It integrates the activity derivative to bound the whole-time supremum, avoiding a growing time grid. Neither (7) nor any concentration estimate alone controls the mean bias.

### 4.2 Width doubling controls the mean bias

Gaussian covariance differentiation and the exact count of each edge type give
\[
\partial_s\mathbb E q_N^{b_*}
=\mathcal R_{N,\mathrm{out}}-\mathcal R_{N,\mathrm{in}}.
\tag{8}
\]
There are \(N^2/2\) edges of each type and their profile derivatives are \(+2,-2\). This verifies every width factor in (8). Integrating (8) in \(s\), then in \(u\), using the zero readout, gives
\[
\sup_{u\le S}|\mathbb E f_{2n}^{b_*}(u,x)-\mathbb E f_n^{b_*}(u,x)|
\le C_B S/\sqrt n.
\tag{9}
\]
The estimates are summable along \(n,2n,4n,\ldots\). Therefore the means converge uniformly in activity, and their distance to the limit is at most
\[
\frac{C_B S}{\sqrt n}\sum_{j\ge0}2^{-j/2}.
\tag{10}
\]

The limit is the actual dense population prediction along its driver (4), not a new unnamed limit. To see this without assuming a rate, use the manuscript's qualitative convergence of actual training predictions and uniform exponential residual tails. Integration up to fixed physical time, followed by a bound on the remaining residual tails, gives \(\|b_n-b_*\|_\infty\to0\) in probability. The deterministic control stability in CONTROLLED_FEEDBACK_STABILITY.md then makes \(f_n^{b_*}-f_n\to0\) in the whole-time bounded-query norm on the fitting/operator event. The manuscript's qualitative actual passive-query convergence identifies its limit as \(f_\infty\). The event probability tends to one, and \(|f_n^{b_*}|\le S\). Thus convergence also identifies the limiting expectation. This step supplies identification only, not the rate in (10).

Combining (7) and (10), and putting
\(\eta_n(t,x)=f_n^{b_*}(t,x)-f_\infty(t,x)\), proves
\[
\mathbb E\int\sup_{t\ge0}|\eta_n(t,x)|^2\,d\mu(x)
+\sum_a\mathbb E\sup_{t\ge0}|\eta_n(t,x_a)|^2
\le C/n.
\tag{11}
\]
Reparametrization by the common deterministic activity path preserves this supremum. The limiting endpoint follows by continuity and the constant extension. Both fluctuation and finite-width mean bias are included in (11).

### 4.3 Restore the actual adaptive flow at the same physical time

Let \(G_n\) be the event on which the initial operator norm is bounded, the initial empirical readout-feature Gram has a fixed positive gap, and the manuscript's small-label fitting/total-activity bounds hold. Its probability tends to one. All constants below are deterministic and uniform on \(G_n\).

CONTROLLED_FEEDBACK_STABILITY.md gives an exact controlled decomposition
\[
f_n^b(t,x)=\sum_a Q_0(x,a)b_a(t)+R_n^b(t,x),
\quad Q_0(x,a)=g_0(x)^\top g_0(x_a)/n,
\]
with the stronger difference estimate
\[
\sup_t|R_n^b(t,x)-R_n^c(t,x)|
\le C_B S^2\|b-c\|_\infty.
\tag{12}
\]
The actual hidden motion is retained in \(R\). The factor \(S^2\) is a Lipschitz bound on its difference, not an additive bias estimate.

For \(e=b_n-b_*\), the exact training equation is
\[
\dot e=-\frac2m Q_0e
        -\frac2m\{R_n^{b_n}(X)-R_n^{b_*}(X)+\eta_n(X)\}.
\tag{13}
\]
Its linear part is exponentially damped by the initial Gram gap. The convolution kernel has finite integral independent of elapsed time. For sufficiently small fixed labels, the term \(CS^2\sup|e|\) resulting from (12) is absorbed, yielding
\[
\sup_t|e(t)|\le C\max_a\sup_t|\eta_n(t,x_a)|.
\]
The query decomposition now gives
\[
\mathcal E_\mu(f_n,f_\infty)
\le C_B\max_a\sup_t|\eta_n(t,x_a)|+\mathcal E_\mu(f_n^{b_*},f_\infty).
\tag{14}
\]
Taking squared expectations with the indicator of \(G_n\), and using (11), gives
\[
\mathbb E\big[\mathbf1_{G_n}\mathcal E_\mu(f_n,f_\infty)^2\big]\le C/n.
\]
For fixed \(\delta\), choose \(n\) sufficiently large that \(\Pr(G_n^c)\le\delta/2\), and apply Markov's inequality with threshold \(2C/(\delta n)\). This proves (3), with \(C_\delta=\sqrt{2C/\delta}\) after increasing the constant if necessary. No rate for the probability of \(G_n^c\) is needed for this fixed-confidence, sufficiently-large-width statement. The manuscript's convergent fitted states and the time supremum imply the endpoint estimate. \(\square\)

## 5. Evidence for H and remaining limitations

The initialization calculation in DECISIVE_CONDITIONAL_ROUTE.md proves the stronger \(C/N\) contrast for any fixed input pair. A swap of two iid first-layer feature vectors changes one row covariance by \(O(1/N)\); bounded fourth tanh derivatives control the effect without inverting that covariance.

PROFILE_FIRST_FEEDBACK.md checks the first genuinely nonlinear activity coefficient for one normalized training input and \(b(u)=u\). The initial contrast is \(O(1/N)\), its first activity coefficient is zero, and its second activity coefficient is \(O(1/N)\). The calculation retains the nonzero mean induced by reusing a Gaussian matrix in a forward pass and a backward pass. These are coefficient calculations, not estimates on a positive training interval. No power series has been summed.

The local evidence, the complete finite fluctuation bound, and the damped feedback theorem support a root-width conjecture in the stated smooth small-label regime. They do not prove H or rule out its failure at later activity. The larger question for general finite geometry and depth still has additional finite-response moment gaps; bounded query support is also an explicit restriction here. No trained slower-than-root construction has been obtained.

The next specific target is a finite-profile cavity argument proving (H), preferably its stronger \(C/N\) version, on the fixed small activity interval. It must preserve the mobility/covariance combination in (6) and the order-one mean response. Merely bounding each normalized response by a constant would not suffice.
