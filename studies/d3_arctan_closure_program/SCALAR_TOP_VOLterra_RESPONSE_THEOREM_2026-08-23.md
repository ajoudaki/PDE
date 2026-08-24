# Theorem: scalar arctangent Volterra response with a frozen lower path

## Scope and conclusion

Let \(|x(t)|\le B=\pi/2\), let
\(C(t,s)=\mathbb E[x(t)x(s)]\), and let \(g\) be a centered Gaussian process
with covariance \(C\).  For an independent \(A_0\sim N(0,1)\), consider

\[
 A_t=A_0+\int_0^t\arctan z_r\,dr,
 \qquad
 z_t=g_t+\int_0^tC(t,r)b_r\,dr,
 \qquad
 b_t=A_td(z_t),quad d(z)=(1+z^2)^{-1}.              \tag{1.1}
\]

For every \(T<\infty\), the covariance-isometric transfer of the Gaussian
first-chaos projection of \(b_t\) is uniformly bounded for \(t\le T\), over
every bounded path \(x\) and every possibly singular PSD covariance \(C\).
The bound is explicit and finite because the only unbounded response
amplitude is the Gaussian endpoint \(A_0\).

This is a proved component, not yet the full network theorem.  In the reused
static matrix program, the lower path can itself acquire an Onsager response
to the same top row; that produces an additional forward response kernel not
present in (1.1).  The theorem applies after that kernel is frozen or shown
to have the required causal bound.

## 1. Exact response measure

Put

\[
 q=\|d'\|_\infty={9\over8\sqrt3}.
\]

Saturation gives \(|A_t|\le|A_0|+Bt\).  Under a Cameron--Martin perturbation
\(g\mapsto g+\varepsilon h\), write

\[
 u_t=\delta A_t,qquad v_t=\delta z_t,qquad w_t=\delta b_t,
\]

and \(\alpha_t=d(z_t),\ \beta_t=A_td'(z_t)\).  Direct differentiation gives

\[
 u_t=\int_0^t\alpha_rv_r\,dr,
 \qquad
 v_t=h_t+\int_0^tC(t,r)w_r\,dr,
 \qquad
 w_t=\alpha_tu_t+\beta_tv_t.                         \tag{1.2}
\]

Eliminating \(u,v\) yields a signed Volterra resolvent

\[
 w_t=\langle\rho_t,h\rangle+
      \int_0^tK(t,r)w_r\,dr,                         \tag{1.3}
\]

with

\[
 \rho_t=\beta_t\delta_t+
         \alpha_t\alpha_s\mathbf1_{[0,t]}(s)\,ds,
\]

\[
 K(t,r)=\beta_tC(t,r)
 +\alpha_t\int_r^t\alpha_sC(s,r)\,ds.               \tag{1.4}
\]

Thus there is a finite signed measure \(\mu_t\), supported on \([0,t]\),
such that

\[
 w_t=\int h_s\,\mu_t(ds),
 \qquad
 \mu_t=\rho_t+\int_0^tK(t,r)\mu_r\,dr.              \tag{1.5}
\]

## 2. Uniform total-variation estimate

Since \(|C(t,s)|\le B^2\), define

\[
 F_T=q|A_0|+(qB+1)T.
\]

Equations (1.4)--(1.5) give

\[
 \|\rho_t\|_{\rm TV}\le F_T,
 \qquad |K(t,r)|\le B^2F_T,
\]

and the Volterra series therefore gives

\[
 \boxed{
 \|\mu_t\|_{\rm TV}
 \le F_Te^{B^2tF_T}
 \le F_Te^{B^2TF_T}.}                                \tag{2.1}
\]

Taking the expectation defines a deterministic signed measure
\(\nu_t(E)=\mathbb E\mu_t(E)\), with

\[
 |\nu_t|([0,t])le
 V_T:=\mathbb E\{F_Te^{B^2TF_T}\}<\infty.            \tag{2.2}
\]

The last expectation is finite for every \(T\) because \(A_0\) is Gaussian;
no small-time restriction occurs.

## 3. First-chaos identification without a covariance inverse

For a finite Gaussian linear combination
\(\xi=\sum_ic_ig(s_i)\), put
\(h_s=\mathbb E[g_s\xi]\).  Decompose the Gaussian process into its component
along \(\xi\) and its independent orthogonal complement, and apply
one-dimensional Gaussian integration by parts.  Using (1.5),

\[
 \mathbb E[b_t\xi]
 =\mathbb E[w_t[h]]
 =\int h_s\,\nu_t(ds)
 =\mathbb E\left[\left(\int g_s\nu_t(ds)\right)\xi\right].
\]

Consequently

\[
 \Pi_1b_t=\int_0^tg_s\nu_t(ds),
\]

including singular covariance kernels.  The covariance isometry transfers
this to

\[
 p_t=\int_0^tx_s\nu_t(ds),
 \qquad
 \boxed{\|p_t\|_\infty\le B V_T.}                    \tag{3.1}
\]

Thus \(p_t\) is in every Orlicz class; for the convention
\(\mathbb Ee^{|Y|/K}\le2\),
\(\|p_t\|_{\psi_1}\le BV_T/\log2\).

## 4. Exact boundary of the theorem

The estimate is uniform if the lower feature law evolves but, in the
top-row response calculation, \(x,C\) remain frozen and \(A_0\) remains
independent of the fresh Gaussian field.  It also works conditionally under
those hypotheses.

If perturbing the top Gaussian row changes \(x\) or makes \(C\) pathwise
random, differentiating \(z\) creates an additional term

\[
 \int (\delta C)(t,s)b_s\,ds.
\]

For the fully reused transpose program this is the lower-layer Onsager
response.  It cannot be discarded: a complete proof must couple (1.5) to
the corresponding middle and bottom response measures, or prove a
triangular conditioning in which this extra term has already been dressed.
