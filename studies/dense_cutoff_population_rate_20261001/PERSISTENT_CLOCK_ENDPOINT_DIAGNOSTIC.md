# A functional coefficient for replacing historical by final features

2026-10-03. Exact finite-order expansion of a specified static diagnostic,
followed by the limit of its coefficient. This is **not** an autonomous
closure endpoint theorem or a counterexample to the requested width rate.
It addresses the possible obstruction exposed by DATA_QUOTIENT_CLOCK.md.
The missing dynamical identification is stated explicitly below.

Scientific inputs: the canonical two-tanh equations in the current paper,
the own-study exact quotient/endpoint identities, and elementary Gaussian
conditioning derived here. No experiment or other study was used.

## 1. A precisely defined comparison

Take one effective unit input \(v\), and use the exact dense controlled
curve with parameter \(u\), initial Gaussian read-in and mixer, and zero
readout. For positive effective label this parameter satisfies
\(du/dt=2(y-f(v))\) until fitting. For the expansion it is simply the
independent variable of the following smooth finite-dimensional equations:
\[
 a'=\operatorname{sech}^2(a)\odot W^\top\delta,
 \qquad W'=\delta h^\top/n,\qquad w'=g,
\]
\[
 a=Av,\quad h=\tanh a,\quad z=Wh,\quad
 g=\tanh z,\quad \delta=w\odot\operatorname{sech}^2z.
\]
Other input directions in \(A\) are constant. Primes denote derivatives
in \(u\), not physical time.

Let initial quantities carry subscript zero and define
\[
 d=g_0\odot\operatorname{sech}^2z_0,\qquad
 H_2=\tfrac12\operatorname{sech}^4(a_0)\odot W_0^\top d,
\]
\[
 Q_n=\|g_0\|_2^2/n,\qquad Q_{d,n}=\|d\|_2^2/n,
 \qquad D(u)=\int_0^u\delta(s)ds.
\]
For fixed width and initialization with \(Q_n>0\), construct
\[
 W_{\mathrm{pair}}(u)=W_0+D(u)h(u)^\top/n.
\]
Keep the read-in at its dense value, and rescale the dense readout by
\[
 w_{\mathrm{pair}}(u)
 =w(u)\frac{f_D(u,v)}{
 n^{-1}w(u)^\top\tanh(W_{\mathrm{pair}}(u)h(u))}.
\]
For small nonzero \(u\), its denominator is \(Q_nu+O(u^3)\), so this
definition is valid. The constructed predictor fits exactly the same
training prediction as the dense curve at that \(u\).

This construction uses the **dense** integrated response \(D(u)\).
An actual closure endpoint instead uses its own integrated response and
read-in/readout trajectory. Equating those objects is not justified here.

## 2. The leading functional difference

Uniqueness and the parity symmetry of these controlled equations give
even \(A(u),W(u)\) and odd \(w(u)\). Direct differentiation at zero yields
\[
 w(u)=u g_0+O(u^3),\qquad
 h(u)=h_0+u^2H_2+O(u^4),\qquad
 \delta(u)=u d+O(u^3).
\]
All remainders in this section are at fixed width, initialization, and
query. They are not asserted uniform in width or memory order.

Using the exact dense integral instead of differentiating its fourth
coefficient separately,
\[
\begin{aligned}
 W_{\mathrm{pair}}(u)-W_D(u)
 &=\frac1n\int_0^u\delta(s)[h(u)-h(s)]^\top ds\\
 &=\frac{u^4}{4n}\,dH_2^\top+O(u^6).
\end{aligned}
\]
Here \(\int_0^u s(u^2-s^2)ds=u^4/4\). Define initialized query features
\(h_0(x)=\tanh(A_0x/\sqrt d)\),
\(g_0(x)=\tanh(W_0h_0(x))\), and
\(\kappa_n(x)=g_0^\top g_0(x)/n\), with training input \(x=\sqrt d v\).
Define also the asymmetric query factor
\[
 Q_{d,n}(x)=\frac1n\sum_j
       g_{0,j}\operatorname{sech}^2(z_{0,j}(x))d_j.
\]
It equals \(Q_{d,n}\) at the training input, but is generally different
at an unseen query. The unrescaled predictor change is
\(u^5Q_{d,n}(x)H_2^\top h_0(x)/(4n)+O(u^7)\).
The readout rescaling subtracts its training component. Consequently
\[
 f_{\mathrm{pair}}(u,x)-f_D(u,x)=u^5 C_n(x)+O(u^7),
\]
\[
 C_n(x)=\frac14\left[
 Q_{d,n}(x)\frac{H_2^\top h_0(x)}n
 -Q_{d,n}\frac{H_2^\top h_0}n\frac{\kappa_n(x)}{Q_n}\right].
 \tag{1}
\]
This coefficient vanishes at the training input by construction.

## 3. The limiting coefficient near an unseen input

Consider queries \(x_r=\sqrt d\,r v\), near \(r=0\). Let
\(a\sim N(0,1)\), \(H=\tanh a\), and put
\[
 V=\mathbb E H^2,\quad s_1=\mathbb E\operatorname{sech}^2a,
 \quad U=\mathbb E[H^2\operatorname{sech}^4a],\quad
 T=\mathbb E[aH\operatorname{sech}^4a].
\]
For \(Z\sim N(0,V)\), define
\[
 Q=\mathbb E\tanh^2 Z,\quad s_2=\mathbb E\operatorname{sech}^2 Z,
 \quad d(z)=\tanh z\operatorname{sech}^2 z,
 \quad Q_d=\mathbb E d(Z)^2,\quad c_d=\mathbb E d'(Z),
 \quad Q_{gd}=\mathbb E[\tanh^2 Z\operatorname{sech}^2Z].
\]
Then the derivative at zero of the finite-width coefficient in (1)
converges in probability to
\[
 C'(0)=\frac{c_d}{8}
 \left[Q_{gd}T-Q_dU\frac{s_1s_2}{Q}\right].
 \tag{2}
\]
Here coefficient differentiation is performed first at each width, followed
by the width limit. No exchange of a trained endpoint limit and width is used.

To verify the probabilistic step, condition on the independent first-layer
rows. Each row of \(W_0\) is an independent Gaussian vector. For a bounded
vector \(t\) determined by those rows,
\[
 \frac{H_2^\top t}{n}
 =\frac1{2n}\sum_j d((W_0h_0)_j)
          [W_0(\operatorname{sech}^4(a_0)\odot t)]_j.
\]
The two Gaussian linear forms in a summand have covariance
\(n^{-1}h_0^\top(\operatorname{sech}^4(a_0)\odot t)\).
One-dimensional Gaussian integration by parts gives its conditional mean
as that covariance times \(\mathbb E d'(Z_n)\), where
\(\operatorname{Var}Z_n=\|h_0\|_2^2/n\).
Conditional variances of the normalized average are \(O(1/n)\).
Apply this with \(t=h_0\) and with \(t=a_0\); in the second case the
product \(a_0\operatorname{sech}^4(a_0)\) is bounded. The row law of
large numbers then gives limits \(c_dU/2\) and \(c_dT/2\).

Similarly \(Q_n\to Q\), \(Q_{d,n}\to Q_d\), and
\[
 \left.\frac{d\kappa_n(x_r)}{dr}\right|_{r=0}
 =\frac1n\sum_j\tanh((W_0h_0)_j)(W_0a_0)_j
 \longrightarrow s_1s_2.
\]
For the last variance estimate, the Gaussian variance
\(\|a_0\|_2^2/n\) is bounded in probability and has bounded moments.
Also \(Q_{d,n}(0)\to Q_{gd}\), because the query preactivation is
zero at the origin. These computations prove the displayed coefficient
limit. In particular the query factor cannot be replaced by its training
value before differentiating.

For a partial sign calculation, Gaussian integration by parts gives
\(c_d=\mathbb E[Zd(Z)]/V>0\), and \(Q_d,U>0\).
Under the probability law with density proportional to \(H^2\) relative
to the Gaussian law, the function \(a/\tanh a\), continuously extended
at zero, is strictly increasing in \(|a|\). The factor
\(\operatorname{sech}^4a\) is strictly decreasing in \(|a|\).
Their covariance is strictly negative; this follows by taking two
independent copies and averaging the product of their differences.
Thus
\[
 \frac{T}{U}<\frac{\mathbb E[a\tanh a]}{V}=\frac{s_1}{V}.
\]
Also \(Z\tanh Z>\tanh^2 Z\) away from zero, so Gaussian integration
by parts yields \(Vs_2=\mathbb E[Z\tanh Z]>Q\). Combining these strict
inequalities gives \(T/U<s_1s_2/Q\). However \(Q_{gd}>Q_d\), so this
inequality does **not** establish the sign or nonvanishing of (2).
Dropping this distinction would be an incorrect train/query identification.

The same conditioning argument defines a limiting coefficient \(C(x_r)\)
for each fixed \(r\), and differentiation under its Gaussian integrals
is dominated by integrable Gaussian coordinates. Its derivative is (2).
No strict nonzero coefficient at a specified query is asserted here.

## 4. What this does and does not resolve

The persistent-clock endpoint identity shows why the final-feature pairing
is relevant. The calculation here identifies the first possible prediction
coefficient after replacing the dense historical pairing and restoring the
training prediction by readout adjustment. Proving its nonvanishing remains
an additional obligation.

It does **not** prove that the autonomous closure has the constructed
endpoint, that its integrated response equals the dense one to sufficient
order uniformly in \(q\), or that the small-\(u\) remainder is uniform in
width and order. It therefore supplies neither a slower-than-root lower
bound nor a counterexample for fixed compatible correlated data. Those
unproved identifications must be resolved before using this calculation
as a negative answer to the user's theorem request.
