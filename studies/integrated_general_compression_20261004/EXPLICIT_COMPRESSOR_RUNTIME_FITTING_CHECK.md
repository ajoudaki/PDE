# Check of numerical corrected-runtime fitting and endpoint tails

2026-10-04. **PASS.** The numerical label condition, independent fitting
bootstrap, raw and effective readout bounds, and whole-sphere endpoint tail
are correct for the specified autonomous optimizer. No minimum selected
weight, activation-value bound, or extra geometry assumption enters the
estimates. The optimizer is not asserted to be ordinary gradient flow.

The complete principal source was
`EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md`, SHA-256
`9da5c0cd2bcd9731be8507995fe8d734293703863d002680a3d8154ccc342cb0`.
The complete inherited exact runtime was read from
`closure_sampling_20261003/STORAGE_QUADRATIC_IMPROVEMENT.md`, SHA-256
`ec18f54a3e3977bf9c99ce5c26066f48688848f8b5a9c142b75424badeb025e2`.
The dense initialization theorem, general activation-extension input, and
canonical-notation instructions were already read and remained current.
No other report or scientific source was used for this runtime check.
This is an internal reconstruction, not a promotion review.

## 1. The exact runtime and selected norm

The source uses the same corrected runtime as the inherited construction,
with its old metric symbol renamed \(M_\ell\). Its positive diagonal metric
is \(\mathsf D_\ell\), whereas the source's \(D_\ell\) denotes a scalar
response coefficient. These roles are distinct throughout.

The relations \(\mathsf D_\ell/4\preceq M_\ell\preceq\mathsf D_\ell\)
give \(\|u\|_{M_\ell}\le\|u\|_{\mathsf D_\ell}\le2\|u\|_{M_\ell}\).
The constant source vector has \(M_\ell\)-norm one, so its diagonal norm
is at most two. For every real pair \(z,z'\), linear growth and the
diagonal metric therefore imply

\[
\|\phi_\ell(z)\|_{M_\ell}\le2b+2s\|z\|_{M_\ell},\qquad
\|\phi_\ell(z)-\phi_\ell(z')\|_{M_\ell}
\le2s\|z-z'\|_{M_\ell}.
\]

Every coordinate gate similarly has operator norm at most \(2s\).
These arguments contain no reciprocal of a selected diagonal weight.
Exact source isometry on first-weight columns preserves the initial
first-block operator bound; the initialized hidden maps are contractions
of the original ones between their source spaces. Exact paired initialized
training features preserve the initialized training Gram.

Writing \(\mathsf H\) for the current training-feature matrix and
\(Q=\mathsf H^{\mathsf T}M_L\mathsf H\), substitution of the effective
readout formula gives

\[
\mathsf H^{\mathsf T}M_L\widehat w=y-c.
\]

Thus the stored \(c\) is exactly the model's residual with convention
labels minus predictions. The backward signals are the specified update
directions. No false identification with activation adjoints in a
non-diagonal metric is needed.

## 2. Exact raw energy and the two readouts

Under the stated parameter norm, the Hilbert--Schmidt norm of a hidden
rank-one direction \(\delta h^{\mathsf T}M_{\ell-1}\) is
\(\|\delta\|_{M_\ell}\|h\|_{M_{\ell-1}}\). The corresponding cross inner
product for samples \(a,b\) is the product of their two inner products.
The first block contributes the additional factor \(v_a^{\mathsf T}v_b\),
and the raw readout contributes the feature inner product. Expanding all
velocity squares therefore gives exactly

\[
\|\dot\theta\|_{\rm par}^2=4c^{\mathsf T}Kc/m^2.
\]

Independently, \(\dot c=-2Kc/m\) gives the same expression for
\(-d\rho_C^2/dt\). Each summand defining \(K\) is a Gram matrix, so
\(K\succeq Q\). On the stopped gap \(Q/m\succeq\lambda I/4\),

\[
-\dot\rho_C\ge\frac\lambda2\rho_C,\qquad
\|\dot\theta\|_{\rm par}
=\sqrt{2\rho_C(-\dot\rho_C)}
\le\frac2{\sqrt\lambda}(-\dot\rho_C).
\]

Integration gives both inequalities (9) and the raw readout bound
\(\|w\|_{M_L}\le2Y/\sqrt\lambda\). The parameter norm here excludes the
separately stored residual; it is exactly the norm of the raw neural
parameter velocities.

The map \(P=\mathsf H Q^{-1}\mathsf H^{\mathsf T}M_L\) is an orthogonal
projector in the \(M_L\) metric. Thus

\[
\widehat w=(I-P)w+\mathsf H Q^{-1}(y-c)
\]

is an orthogonal sum. Its first squared norm is at most
\(4Y^2/\lambda\). Its second is
\((y-c)^{\mathsf T}Q^{-1}(y-c)\), at most
\(4\|y-c\|_2^2/(m\lambda)\le16Y^2/\lambda\), because
\(\|c\|_2/\sqrt m\le Y\). Consequently

\[
\|\widehat w\|_{M_L}\le\sqrt{20}\,Y/\sqrt\lambda
<5Y/\sqrt\lambda=R\quad(Y>0).
\]

This is the necessary effective-readout bound; replacing it by the raw
readout estimate would not have been justified. When \(Y=0\), all raw
and effective variables are stationary with zero predictor, so no strict
readout comparison is required.

## 3. Numerical bootstrap and continuation

The initial first-feature bound is
\(2b+2s\cdot8\le H_1\). The later initialization bounds are dominated
by the recurrence with operator coefficient nine in (5). The \(H_\ell\)
increase, so every initialized sphere feature is bounded by \(H=H_L\).
The scalar Gaussian variance recursion is also dominated by these bounds;
hence \(\lambda=\gamma/m\le H^2\).

On the operator tube, backward responses are bounded by
\(D_\ell\|\widehat w\|\), with
\(D_\ell=2s(18s)^{L-\ell}\). Cauchy--Schwarz in the sample index gives
hidden velocities at most \(2\rho_C R U_\ell\). Integrating with
\(\int\rho_C\le2Y/\lambda\) yields

\[
4R U_\ell Y/\lambda=20U_\ell Y^2/\lambda^{3/2}.
\]

The feature subtraction recursion multiplies by \(2s\), has direct
coefficient \(2H\), and propagates with operator bound nine. It is
therefore exactly the recurrence defining \(F_\ell\). These coefficients
increase and \(F=F_L\) dominates every \(U_\ell,F_\ell\).

Under \(Y\le\lambda/(16H\sqrt F)\), the common displacement bound is

\[
20FY^2/\lambda^{3/2}
\le\frac{5\sqrt\lambda}{64H^2}
<\frac{\sqrt\lambda}{8},\qquad
\frac{5\sqrt\lambda}{64H^2}<\frac1{8H}.
\]

The latter uses \(\sqrt\lambda\le H\). Thus every operator remains below
\(8+1/8\), and every sphere feature remains below \(H+1/8<2H\).
The top normalized training-feature map has operator perturbation at most
the largest sample-feature displacement, so its least singular value is
at least
\((1/\sqrt2-1/8)\sqrt\lambda>\sqrt\lambda/2\). This strictly improves
the stopped gap. No additional sample-count factor occurs.

At each fixed selected size, the raw state is bounded and the Gram remains
uniformly positive. The finite-dimensional vector field is locally
Lipschitz there, so finite-time continuation follows. Finite raw parameter
path length gives convergence; the effective readout formula is continuous
on the retained Gram margin and therefore converges as well. Since
\(c\to0\), its limit interpolates the training labels.

## 4. Exact projector derivatives and the endpoint constant

Regard \(V=\mathsf H/\sqrt m\) as an operator from Euclidean sample space
to the \(M_L\) neuron space. Put \(q=V^*V\), \(T=Vq^{-1}\),
\(P=TV^*\), and \(b_c=(y-c)/\sqrt m\). The gap gives
\(\|q^{-1}\|\le4/\lambda\), \(\|T\|\le2/\sqrt\lambda\), and
\(\|P\|=\|I-P\|=1\) when the corresponding subspace is nontrivial
(the upper bound one suffices in all cases).

Differentiating \(q^{-1}\) and collecting the projectors gives precisely

\[
\dot T=(I-P)\dot Vq^{-1}-T\dot V^*T,
\qquad
\dot P=(I-P)\dot VT^*+T\dot V^*(I-P).
\]

Therefore \(\|\dot T\|\le8\|\dot V\|/\lambda\) and
\(\|\dot P\|\le4\|\dot V\|/\sqrt\lambda\). These stronger bounds do
not require the extra \(\lambda^{-2}\) from a crude product rule.
The instantaneous forward recursion gives
\(\|\dot V\|\le2RF\rho_C\) and the same speed bound at every sphere
query. The Gram trace bound gives
\(\|K/m\|\le G\), hence \(\|\dot b_c\|\le2G\rho_C\).

In the derivative of \(\widehat w=(I-P)w+Tb_c\), the four terms have
respective bounds

\[
4H\rho_C,\quad
16RFY\rho_C/\lambda,\quad
32RFY\rho_C/\lambda,\quad
4G\rho_C/\sqrt\lambda.
\]

The middle terms are \(\dot P w\) and \(\dot T b_c\), using
\(\|w\|\le2Y/\sqrt\lambda\) and \(\|b_c\|\le2Y\). Thus their sum
is exactly bounded by the stated
\(B_w=4H+48RFY/\lambda+4G/\sqrt\lambda\).
Differentiating the predictor gives

\[
|\dot f_C(v)|\le2H B_w\rho_C+R(2RF\rho_C)=B_f\rho_C,
\]

uniformly on the sphere. Since
\(\int_t^\infty\rho_C\le(2Y/\lambda)e^{-\lambda t/2}\), this proves
the complete endpoint bound (12), with no hidden width, sample, or
minimum-weight factor.

## 5. Scope supplied to the merged theorem

This component supplies the independent numerical runtime fitting cap and
uniform endpoint tail. At horizon
\(32\lambda^{-1}\log(en)\), the tail has factor \((en)^{-16}\), so it
is eventually smaller than every prescribed positive multiple of
\(n^{-1/2}\) at fixed data. It fills the fitting-and-tail obligation
excluded from the source-only check. A numerical same-time comparison
coefficient and a numerical stochastic width threshold are separate
obligations and are not certified here.
