# Weighted neuron reduction with the original mixer and its adjoint

2026-10-03. Scoped constructive route after the user clarified that the
desired saving must come from reducing the number of neurons. This note
does not claim the requested sublinear-in-width learned-state theorem.
It gives an actual autonomous reduced network, preserves every order-\(q\)
memory and its own residual clock, identifies the source estimate that
would prove fidelity, and proves a concrete obstruction to choosing the
reduction from initial forward responses alone.

The construction has \(N_1\) first-layer neurons and \(N_2\) second-layer
neurons. Its moving state is

\[
mq(N_1+N_2)+dN_1+N_2+1.
\tag{1}
\]

It uses block averages of the actual realized \(W_0\), together with
the exact weighted adjoint of those averages. It never substitutes an
independently initialized mixer. All partitions and coefficients are
chosen at initialization. Training uses only the reduced state, fixed
coefficients, labels, and inputs; it does not query a trained dense path.

The positive finite-state construction and the source identity below are
unconditional deterministic statements. All-time fitting requires a
directly checkable initial Gram gap, which the initialization construction
in Section 3 supplies with high probability. The missing fidelity estimate
is explicitly stated in Section 7. In particular, fitting the reduced
model does not by itself imply agreement with the original one.

Scientific inputs are the current manuscript's exact setting, moment
construction, deterministic all-order fitting proof, and one-reference
damping proof, and the authorized two-layer finite carrier maximum in
`studies/dense_cutoff_population_rate_20261001/Q_ORDER_RESULT.md`.
The two-layer source bound is the one derived in the authorized
`NONORTHOGONAL_DIRECT_ROUTE.md`. The earlier own-study history result is
not used as a substitute for neuron reduction. The canonical notation
skill and its neural reference, the rigorous-math skill, and
`docs/notation.qmd` govern the presentation. No other active route note,
experiment, Git operation, or manuscript edit was used. This is a
collaborative construction; its block-lift design and source mechanism
were discussed with the coordinator before this note was written.

## 1. Fixed data and weighted blocks

The original model has two tanh hidden layers, width \(n\), fixed inputs
\(v_a=x_a/\sqrt d\), \(a=1,\ldots,m\), and fixed labels \(y_a\).
The activation is \(\phi=\tanh\), and
\(Y^2=m^{-1}\sum_a y_a^2\). The original parameters are
\(W^{(1)}\in\mathbb R^{n\times d}\),
\(W\in\mathbb R^{n\times n}\), and \(w\in\mathbb R^n\), with
independent Gaussian first-layer and hidden initializations of variances
\(1\) and \(1/n\), respectively, and \(w(0)=0\).
The original dense and order-\(q\) closure systems are those in the
manuscript, with mobilities \((n,1,n)\).

Partition first-layer neuron indices into nonempty cells
\(C_{1,i}\), \(i=1,\ldots,N_1\), and second-layer indices into
nonempty cells \(C_{2,j}\), \(j=1,\ldots,N_2\). The two partitions
need not coincide. Define their masses and indicator lifts by

\[
\mu_i=|C_{1,i}|/n,\qquad \nu_j=|C_{2,j}|/n,
\qquad
(J_1)_{ri}=\mathbf1_{r\in C_{1,i}},\quad
(J_2)_{rj}=\mathbf1_{r\in C_{2,j}}.
\tag{2}
\]

Thus \(J_1u\) is a block-constant vector of length \(n\), and
\(\|J_1u\|_2^2/n=\sum_i\mu_i u_i^2\); the corresponding identity
holds with \(J_2,\nu\). Write
\(D_\mu=\operatorname{diag}(\mu_i)\),
\(D_\nu=\operatorname{diag}(\nu_j)\). The averaging maps and
orthogonal projections are

\[
R_1=\frac1nD_\mu^{-1}J_1^\top,\quad
R_2=\frac1nD_\nu^{-1}J_2^\top,
\qquad \Pi_1=J_1R_1,\quad \Pi_2=J_2R_2.
\tag{3}
\]

One has \(R_\ell J_\ell=I\) and
\(\Pi_\ell^\top=\Pi_\ell^2=\Pi_\ell\). The reduced fixed arrays are

\[
A_0=R_1W_0^{(1)},\qquad B_0=R_2W_0J_1.
\tag{4}
\]

In raw neuron values, \(B_0\) has shape \(N_2\times N_1\). Its
weighted adjoint is

\[
B_0^*=D_\mu^{-1}B_0^\top D_\nu=R_1W_0^\top J_2.
\tag{5}
\]

Indeed, for any reduced vectors \(u,v\),
\(\sum_j\nu_jv_j(B_0u)_j=\sum_i\mu_i(B_0^*v)_iu_i\), and
both sides equal \((J_2v)^\top W_0(J_1u)/n\).
This identity is exact for the realized initialized matrix and both
orientations of its action.

The Euclidean matrix
\(D_\nu^{1/2}B_0D_\mu^{-1/2}\) equals
\(U_2^\top W_0U_1\), where
\(U_1=J_1D_\mu^{-1/2}/\sqrt n\) and
\(U_2=J_2D_\nu^{-1/2}/\sqrt n\) have orthonormal columns.
Consequently its operator norm is at most \(\|W_0\|_{\rm op}\).
No approximation of \(W_0\) in ambient operator norm is asserted.

## 2. Exact reduced autonomous closure

The reduced first matrix is \(A\in\mathbb R^{N_1\times d}\), the
hidden operator is \(B\in\mathbb R^{N_2\times N_1}\), and the
readout is \(u\in\mathbb R^{N_2}\). The forward pass, residuals,
and loss are

\[
\begin{aligned}
z_a^{(1)}&=Av_a,&h_a^{(1)}&=\phi(z_a^{(1)}),\\
z_a^{(2)}&=Bh_a^{(1)},&h_a^{(2)}&=\phi(z_a^{(2)}),\\
f_{C,a}&=\sum_j\nu_j u_jh_{a,j}^{(2)},&r_{C,a}&=f_{C,a}-y_a,\\
\rho_C^2&=m^{-1}\sum_a r_{C,a}^2,&\mathcal L_C&=\rho_C^2.
\end{aligned}
\tag{6}
\]

The actual reduced responses and adjoint are

\[
\delta_a^{(2)}=u\odot\phi'(z_a^{(2)}),\quad
B^*=D_\mu^{-1}B^\top D_\nu,\quad
k_a=B^*\delta_a^{(2)},\quad
\delta_a^{(1)}=\phi'(z_a^{(1)})\odot k_a.
\tag{7}
\]

The first layer and readout evolve as

\[
\dot A=-\frac2m\sum_a r_{C,a}\delta_a^{(1)}v_a^\top,
\qquad
\dot u=-\frac2m\sum_a r_{C,a}h_a^{(2)}.
\tag{8}
\]

The corresponding uncompressed weighted hidden gradient flow would be

\[
\dot B=-\frac2m\sum_a r_{C,a}
                       \delta_a^{(2)}h_a^{(1)\top}D_\mu.
\tag{9}
\]

These are genuine gradient-flow equations for (6). In raw coordinates,
the positive diagonal mobilities are \(1/\mu_i\) for row \(i\) of
\(A\), \(1/\nu_j\) for readout coordinate \(j\), and
\(\mu_i/\nu_j\) for matrix coordinate \(B_{ji}\). Substituting
the ordinary partial derivatives of (6) gives (8)--(9), including all
mass factors. The partition masses therefore represent neuron
multiplicity; they are not arbitrary unnormalized learning-rate changes.

Now replace (9) by the original order-\(q\) memory construction in
these two finite weighted spaces. The clock is its own
\(\dot\tau_C=\rho_C\), \(\tau_C(0)=1\). For each sample and
\(s=0,\ldots,q-1\), store
\(\bar h_{a,s}^{(1)}\in\mathbb R^{N_1}\) and
\(\bar\delta_{a,s}^{(2)}\in\mathbb R^{N_2}\), with equations

\[
\begin{aligned}
\dot{\bar h}_{a,s}^{(1)}
 &=\rho_C h_a^{(1)}-\frac{\rho_C}{\tau_C}
   \left[s\bar h_{a,s}^{(1)}+
             \sum_{r<s}(2r+1)\bar h_{a,r}^{(1)}\right],\\
\dot{\bar\delta}_{a,s}^{(2)}
 &=r_{C,a}\delta_a^{(2)}-\frac{\rho_C}{\tau_C}
   \left[s\bar\delta_{a,s}^{(2)}+
             \sum_{r<s}(2r+1)\bar\delta_{a,r}^{(2)}\right],\\
B&=B_0-\frac2{m\tau_C}\sum_a\sum_{s=0}^{q-1}(2s+1)
        \bar\delta_{a,s}^{(2)}\bar h_{a,s}^{(1)\top}D_\mu.
\end{aligned}
\tag{10}
\]

Initially \(A=A_0\), \(u=0\),
\(\bar h_{a,0}^{(1)}=\phi(A_0v_a)\), and all other moments vanish.
The initial forward prefix is constant and the backward prefix zero.
Every response and every clock write is evaluated in the reduced
reconstructed network. Equation (10) has no division by the residual.
Its adjoint is the exact weighted adjoint of the entire reconstruction,
including each learned outer product. This defines the reduced algorithm
for every order \(q\) with state count (1).

## 3. Fitting survives this neuron reduction

The initial weighted readout-feature Gram is explicitly computable:

\[
(\Gamma_{C,w}(0))_{ab}
 =\frac1m\sum_j\nu_jh_{a,j}^{(2)}(0)h_{b,j}^{(2)}(0).
\tag{11}
\]

If its least eigenvalue is bounded below by a fixed positive number,
the manuscript's deterministic all-order fitting proof applies to (10)
with constants independent of \(n,N_1,N_2,q\) and of the smallest cell
mass. Here is why this assertion does not conceal a dimension assumption.
The spaces have squared norms displayed as
\(\sum_i\mu_i x_i^2\) and \(\sum_j\nu_j y_j^2\).
The initialized operator bound follows from (5). Bounded \(\phi,\phi'\)
give the same forward/backward norm inequalities. Outer-product matrix
norms become
\(\|D_\nu^{1/2}\Delta B D_\mu^{-1/2}\|_F\), and for
\(\Delta B=ab^\top D_\mu\) their squared value is exactly
\((\sum_j\nu_j a_j^2)(\sum_i\mu_i b_i^2)\).
All polynomial projection bounds are Hilbert-space bounds and are
unchanged. The residual tangent Gram is a sum of nonnegative Grams:

\[
\begin{aligned}
(\Gamma_C)_{ab}=\frac1m\bigg[&
 \sum_j\nu_j h_{a,j}^{(2)}h_{b,j}^{(2)}
 +(v_a^\top v_b)\sum_i\mu_i\delta_{a,i}^{(1)}\delta_{b,i}^{(1)}\\
 &+\left(\sum_j\nu_j\delta_{a,j}^{(2)}\delta_{b,j}^{(2)}\right)
   \left(\sum_i\mu_i h_{a,i}^{(1)}h_{b,i}^{(1)}\right)\bigg].
\end{aligned}
\tag{12}
\]

The same short-activity bootstrap keeps (11) open, bounds the relative
memory defect, and yields \(\rho_C(t)\le Ye^{-\kappa t}\), all-time
existence, and parameter limits for sufficiently small fixed labels.
In particular \(\|u(t)\|_\infty\le2Y/\kappa\).
No inverse cell mass appears in these estimates after using the weighted
adjoint (7).
Precisely, the labels must lie below the deterministic threshold for the
verified reduced Gram margin and operator bounds, as well as below the
original theorem's threshold. Their minimum is a fixed positive number;
it may be smaller than the previously chosen original-model threshold.
Fitting of the modified model is not asserted for every label vector
covered by an unspecified larger threshold.

The initial gap can be ensured without training. Let
\(H_0\in\mathbb R^{n\times m}\) contain the original initial
first-layer training features and put \(Z_0=W_0H_0\). Define

\[
a_0=\frac{\|(I-\Pi_1)W_0^{(1)}\|_F}{\sqrt n},\qquad
z_0=\max_a\frac{\|(I-\Pi_2)Z_{0,a}\|_2}{\sqrt n}.
\tag{13}
\]

Contraction and the Lipschitz constant one of tanh give, for every
normalized training input,

\[
\frac{\|J_2h_{C,a}^{(2)}(0)-h_{D,a}^{(2)}(0)\|_2}{\sqrt n}
 \le \|W_0\|_{\rm op}a_0+z_0.
\tag{14}
\]

Bounded feature values then control the difference of the two initial
readout Grams by \(C(\|W_0\|_{\rm op}a_0+z_0)\).
Thus a sufficiently accurate initial quantization preserves a fixed gap.

For an existence construction, grid the row vectors of \(W_0^{(1)}\)
inside a fixed bounded cube at a fixed fine spacing, and put the outside
rows in an overflow cell. Independently grid the row tuples of \(Z_0\)
in \(\mathbb R^m\) in the same fashion for the upper partition.
The squared error of block averaging is no larger than the error of
approximating every inner-cube row by its cell center and every overflow
row by zero. The resulting errors are bounded by a fixed squared mesh
diameter plus the corresponding empirical second-moment tails.
First choose the cube large and the spacing small; then Gaussian laws
of large numbers, including conditional Gaussian upper rows, make
\(a_0,z_0\) as small as a prescribed fixed constant with probability
tending to one. The numbers of cells are finite constants depending on
that accuracy, \(d\), and \(m\), but not on width.

This proves an actual reduction in neuron count with preserved all-order
fitting. It does not prove width-scale prediction fidelity. The next
sections identify what that stronger property costs.

## 4. Exact forward and adjoint discrepancies

For a reduced trajectory define a full-size *proof lift*

\[
\widetilde W^{(1)}=J_1A,\qquad
\widetilde w=J_2u,\qquad
\widetilde W=W_0+J_2(B-B_0)R_1.
\tag{15}
\]

The unchanged full \(W_0\) is present in (15). This lift is an analysis
object; the algorithm stores and applies the reduced arrays in (10).
For a current reduced forward feature and backward response define

\[
e_{F,a}=(I-\Pi_2)W_0J_1h_a^{(1)},\qquad
e_{B,a}=(I-\Pi_1)W_0^\top J_2\delta_a^{(2)}.
\tag{16}
\]

These are precisely the discarded actions, with identities

\[
\begin{aligned}
\widetilde WJ_1h_a^{(1)}&=J_2z_a^{(2)}+e_{F,a},\\
\widetilde W^\top J_2\delta_a^{(2)}&=J_1k_a+e_{B,a}.
\end{aligned}
\tag{17}
\]

For the second identity, the learned transpose contributes
\(R_1^\top(B-B_0)^\top J_2^\top J_2\delta
=J_1D_\mu^{-1}(B-B_0)^\top D_\nu\delta\), which verifies
every mass factor. The two discarded fields are different; controlling
forward averages alone does not control the adjoint action.

Let \(E_{C,B}\) be the mixer velocity defect of the reduced closure.
Differentiating (10) gives

\[
E_{C,B}=\frac{2\rho_C}{m}\sum_a
 (b_a^{(2)}-b_a^{(2)*})
 (h_a^{(1)}-h_a^{(1)*})^\top D_\mu,
\quad b_a^{(2)}=(r_{C,a}/\rho_C)\delta_a^{(2)}.
\tag{18}
\]

Stars mean degree-below-\(q\) endpoint projections in the reduced
model's own clock. Its lifted defect
\(E_C=J_2E_{C,B}R_1\) satisfies

\[
\|E_C\|_F=\|D_\nu^{1/2}E_{C,B}D_\mu^{-1/2}\|_F.
\tag{19}
\]

Projection energy in these two weighted spaces and the bounded top
readout give, exactly as in the two-layer direct source proof,

\[
\epsilon_{C,q}:=\int_0^\infty\|E_C(t)\|_Fdt
\le CY^{5/2}q^{-2}\sqrt{\log(e+q)}.
\tag{20}
\]

To verify the transfer, the forward clock derivative has squared
weighted integral at most \(CY^3\), so its omitted polynomial norm
is at most \(CY^{3/2}/q\). The top backward field has weighted norm
at most \(CY\) and physical derivative norm at most \(C(Y+\rho_C)\)
because \(\|u\|_\infty\le CY\). Freeze it after physical time
\((2/\kappa)\log q\); its omitted norm is at most
\(CYq^{-1}\sqrt{\log(e+q)}\). The exact product of these two
errors gives (20), with no smallest-weight or neuron-count factor.

## 5. A deterministic all-time fidelity estimate in terms of the sources

This section compares the reduced model to the same-realization dense
reference. The original order-\(q\) closure is addressed at the end of
the section. Suppose the original dense and reduced initial Grams have
the fixed gaps above, labels are sufficiently small, and the dense-only
carrier maximum obeys

\[
\sup_{t\ge0}\left[\max_a\|W_D(t)^\top\delta_{D,a}^{(2)}(t)\|_\infty
                         +\|w_D(t)\|_\infty\right]\le M,
\qquad M\ge1.
\tag{21}
\]

The supplied finite-network theorem makes \(M=O(\sqrt{\log(e+n)})\)
on events whose probability tends to one. Define

\[
\begin{aligned}
d(t)={}&\frac{\|\widetilde W^{(1)}(t)-W_D^{(1)}(t)\|_F}{\sqrt n}
 +\|\widetilde W(t)-W_D(t)\|_F
 +\frac{\|\widetilde w(t)-w_D(t)\|_2}{\sqrt n},\\
\ell(t)={}&\max_a
 \frac{\|e_{F,a}(t)\|_2+\|e_{B,a}(t)\|_2}{\sqrt n},\\
\mathcal R={}&\int_0^\infty\rho_D(t)\ell(t)dt.
\end{aligned}
\tag{22}
\]

Both model trajectories exist before making this comparison. In
particular, \(\sup_td(t)<\infty\) and \(\mathcal R<\infty\)
follow from their physical bounds and \(\|W_0\|_{\rm op}\le C\).
Then

\[
\sup_{t\ge0}d(t)
\le C e^{CYM}\,[a_0+\epsilon_{C,q}+\mathcal R].
\tag{23}
\]

Here is a derivation that avoids treating the coarse output as the output
of the proof lift. Those outputs differ, and confusing them would create
a nonintegrable forcing after the coarse model has fitted.

First, (17), forward subtraction, and Lipschitz activations give

\[
\max_a\frac{\|J_1h_a^{(1)}-h_{D,a}^{(1)}\|_2}{\sqrt n}\le Cd,
\qquad
\max_a\frac{\|J_2h_a^{(2)}-h_{D,a}^{(2)}\|_2}{\sqrt n}
 \le C(d+\ell).
\tag{24}
\]

For the top backward difference, bounded dense readout coordinates
give \(C(d+Y\ell)\). In the first layer the changed gate multiplies
only the dense carrier, bounded by \(M\); the changed carrier includes
the second line of (17). Thus

\[
\max_a\frac{\|J_1\delta_a^{(1)}-\delta_{D,a}^{(1)}\|_2}{\sqrt n}
\le C[(1+M)d+\ell].
\tag{25}
\]

The exact weighted tangent Gram (12) is an ordinary ambient Gram after
lifting its vectors by \(J_1,J_2\). Expanding each product with
(24)--(25) yields
\(\|\Gamma_C-\Gamma_D\|_{\rm op}
\le C[(1+M)d+\ell]\).

Put \(v_r=r_C-r_D\). The actual coarse residual equation is
\(\dot r_C=-2\Gamma_Cr_C+J_CE_{C,B}\), where \(J_C\) is the
coarse prediction derivative. Since \(\Gamma_C\) has its preserved
gap and \(\|J_CE_{C,B}\|_m\le CY\|E_C\|_F\), subtraction gives

\[
D^+\|v_r\|_m
\le-\kappa\|v_r\|_m
 +C\rho_D[(1+M)d+\ell]+C\|E_C\|_F.
\tag{26}
\]

Here \(\|v_r\|_m=(m^{-1}\sum_a v_{r,a}^2)^{1/2}\), as in the
manuscript, and \(v_r(0)=0\) because both readouts are zero.
Integrating (26) bounds \(\int\|v_r\|_m\) by the integrated right
sources. Subtracting the first-layer, readout, and hidden physical updates
gives, using the lifted rank-one identity,

\[
d(t)\le a_0+C\int_0^t\|E_C\|_Fds
 +C\int_0^t\|v_r\|_m ds
 +C\int_0^t\rho_D[(1+M)d+\ell]ds.
\]

Insert the integrated version of (26), use
\(\int\rho_D\le CY\), and apply the scalar integrating factor.
This proves (23). The dense reference enters the proof only; it is
not an input to the reduced algorithm.

There is an additional cancellation for unseen-input evaluation. For
any query \(x\), use the same reduced forward pass to define
\(e_F(t,x)=(I-\Pi_2)W_0J_1h_C^{(1)}(t,x)\). Let
\(f_{\rm lift}(t,x)\) be the ordinary full-network prediction from
the parameter lift (15). Its top preactivation is
\(J_2z_C^{(2)}+e_F\). Because
\(J_2u\odot\phi'(J_2z_C^{(2)})\) is block constant while
\(e_F\) is orthogonal to that space, the linear Taylor term cancels
exactly. Componentwise, the exact remainder is

\[
\phi(z+e)-\phi(z)-\phi'(z)e
=e^2\int_0^1(1-s)\phi''(z+se)ds.
\]

After multiplication by the corresponding readout coordinate and summing,
its absolute value is at most
\(\tfrac12\|\phi''\|_\infty\|u\|_\infty\|e_F\|_2^2/n\).
Using \(\|u\|_\infty\le CY\) gives

\[
|f_{\rm lift}(t,x)-f_C(t,x)|
\le CY\frac{\|e_F(t,x)\|_2^2}{n}.
\tag{27}
\]

Combining the usual full-network forward subtraction with (27), a fixed
query law \(\zeta\) with finite second moment satisfies

\[
\begin{aligned}
\mathcal E_\zeta(f_C,f_D)
&:=\left(\int\sup_{t\ge0}|f_C(t,x)-f_D(t,x)|^2d\zeta(x)\right)^{1/2}\\
&\le C_\zeta e^{CYM}[a_0+\epsilon_{C,q}+\mathcal R]
 +CY\left(\int\sup_{t\ge0}
             \frac{\|e_F(t,x)\|_2^4}{n^2}d\zeta(x)\right)^{1/2}.
\end{aligned}
\tag{28}
\]

The query-law symbol \(\zeta\) is distinct from the lower cell masses
\(\mu_i\). This bound includes the fitted endpoint and the supremum
inside the query integral. The final term is finite because tanh is
bounded and \(W_0\) has bounded operator norm.

This observable cancellation does not automatically cancel the first
backward variation. Put
\(H=(I-\Pi_2)W_0\Pi_1\), so \(e_F=H J_1h_C^{(1)}\), and
\(D_{\rm block}=\operatorname{diag}(J_2u\odot
\phi''(J_2z_C^{(2)}))\). This diagonal matrix is constant within
upper cells and hence commutes with \(\Pi_2\). At fixed current
features, differentiate the top response
\(J_2u\odot\phi'(J_2z_C^{(2)}+\eta e_F)\) with respect to
\(\eta\) at zero. Its derivative is exactly
\(D_{\rm block}e_F\), which lies in the orthogonal complement of
the retained upper space. Applying the retained lower adjoint gives

\[
\Pi_1\widetilde W^\top D_{\rm block}e_F
=\Pi_1W_0^\top D_{\rm block}e_F
=H^\top D_{\rm block}e_F.
\tag{28a}
\]

The learned transpose vanishes on this complementary upper vector.
The right side of (28a) need not be zero: its general norm bound is
\(CY\|H\|_{\rm op}\|e_F\|_2\), only first order in the current
forward leakage. Its pairing with the current lower feature is
quadratic, but that does not make its vector norm quadratic. Thus
accurate forward observable cubature still needs adjoint-range or
response-sensitivity control to justify learning dynamics.

For the original width-\(n\), order-\(q\) closure, the triangle
inequality adds its already proved same-realization dense discrepancy.
The prior theorem bounds that term by
\(n^{o(1)}q^{-2}\sqrt{\log(e+q)}\).
Thus (28) supplies a direct original-closure guarantee whenever both
memory errors are resolved at the target scale. It does **not** prove
the requested comparison at fixed \(q\) merely by this triangle:
for that case the common memory defect must be compared directly and
cannot be treated as two unrelated errors against dense training.
The reduced equations (10) themselves preserve every requested order.

## 6. Forward marks alone miss a leading reverse response

The following actual-network calculation rules out a tempting source
argument. It does not give a prediction-error lower bound and does not
rule out response-aware cubature.

Take one normalized training input \(v\), one fixed positive small label
\(y\), and set

\[
a=W_0^{(1)}v,\qquad h=\phi(a),\qquad z=W_0h,\qquad
D_1=\operatorname{diag}(\phi'(a_i)),\qquad
s=2y\,\phi(z)\odot\phi'(z).
\tag{29}
\]

Let \(P\) be any orthogonal projection of rank at most \(N\), chosen
measurably from \(W_0^{(1)}\) and \(z\). It can use every initial
first-layer row and every initial second-layer training preactivation,
not just a few selected statistics. Suppose \(N=o(n)\).
Then there is a constant \(c_y>0\) such that, with probability tending
to one,

\[
\frac{\|(I-P)\ddot W^{(1)}(0)\|_F}{\sqrt n}\ge c_y.
\tag{30}
\]

The constant is proportional to \(y^2\) at fixed small-label scale.
Statement (30) holds for the actual original dense flow and for every
original order-\(q\) closure, simultaneously, because their displayed
initial derivatives below agree.

To prove it, zero readout gives
\(\dot W^{(1)}(0)=\dot W(0)=0\),
\(\dot w(0)=2y\phi(z)\), and
\(\dot\delta^{(2)}(0)=s\). Thus

\[
\ddot W^{(1)}(0)=2yD_1W_0^\top s\,v^\top.
\tag{31}
\]

Condition on \(W_0^{(1)}\) and \(z=W_0h\). Gaussian conditioning,
row by row, gives the exact decomposition

\[
W_0=\frac{zh^\top}{\|h\|_2^2}
       +\frac1{\sqrt n}G(I-P_h),\qquad
P_h=\frac{hh^\top}{\|h\|_2^2},
\tag{32}
\]

where \(G\) has independent standard Gaussian entries and is independent
of the conditioned data. Consequently

\[
W_0^\top s\ \overset{d}=
 \frac{h(z^\top s)}{\|h\|_2^2}
   +\sigma(I-P_h)\gamma,
\qquad \sigma^2=\frac{\|s\|_2^2}{n},
\quad \gamma\sim N(0,I_n).
\tag{33}
\]

The projection \(P\) is fixed under this conditioning. The covariance
of \((I-P)D_1W_0^\top s\) has trace

\[
\begin{aligned}
\sigma^2\|(I-P)D_1(I-P_h)\|_F^2
&\ge\sigma^2\,[\operatorname{tr}(D_1^2)-N-1],\\
\|\operatorname{Cov}((I-P)D_1W_0^\top s)\|_{\rm op}
&\le\sigma^2.
\end{aligned}
\tag{34}
\]

For the first bound, removing the output subspace costs at most \(N\)
in squared Frobenius norm, and removing the one-dimensional input
subspace costs at most one; \(\|D_1\|_{\rm op}\le1\).
The initial Gaussian laws give

\[
\frac1n\operatorname{tr}(D_1^2)
 \longrightarrow\mathbb E[\operatorname{sech}^4(G_0)]>0,
\qquad
\sigma^2\longrightarrow
4y^2\mathbb E[\tanh^2(Z)\operatorname{sech}^4(Z)]>0,
\tag{35}
\]

where \(G_0\sim N(0,1)\),
\(Z\sim N(0,Q)\), and \(Q=\mathbb E[\tanh^2(G_0)]>0\).
The second convergence follows from conditionally independent upper
rows, bounded integrands, and convergence of \(\|h\|_2^2/n\) to
\(Q\).

For completeness, the nonzero conditional mean in (33) cannot eliminate
the covariance lower bound. If a Gaussian vector \(X\) has arbitrary
mean and covariance \(C\), direct diagonal Gaussian integration gives

\[
\mathbb E e^{-t\|X\|_2^2}
\le\det(I+2tC)^{-1/2}
\le\exp\{-t\operatorname{tr}C+t^2\operatorname{tr}(C^2)\}.
\]

The last inequality uses \(\log(1+x)\ge x-x^2/2\) for \(x\ge0\).
Exponential Markov with \(t=1/(4\|C\|_{\rm op})\) yields

\[
\Pr\{\|X\|_2^2\le\tfrac12\operatorname{tr}C\}
\le\exp\left\{-\frac{\operatorname{tr}C}{16\|C\|_{\rm op}}\right\}.
\tag{36}
\]

Equations (34)--(36) imply a positive conditional lower bound on
\(\|(I-P)D_1W_0^\top s\|_2/\sqrt n\), except with probability
\(e^{-cn}\) on events whose probability tends to one. Equation (31)
and \(\|v\|_2=1\) prove (30).

This rules out an initial-transverse-source estimate tending to zero for
any sublinear-dimensional lower space chosen only from these forward
marks. In particular, an argument that accurate initial forward
quadrature automatically controls all early feature-learning responses
is false. The result even grants the construction complete access to
the initial forward arrays. It does not assume that those arrays were
estimated from a subsample.

Including the reverse mark \(W_0^\top s\), or the gated acceleration
\(D_1W_0^\top s\), invalidates this conditional-independence argument
and can remove this particular obstruction. Such a response-aware
partition is allowed by the setup. It still needs control of later
endogenous forward and reverse fields; no fixed-dimensional sufficient
mark law follows from one additional response.

## 7. The precise remaining estimate

The block construction is a bona fide weighted neuron reduction and
preserves the original time, residual RMS, all \(q\) memories, and both
orientations of the same initialized source. Its sufficient fidelity
condition, after memory error is resolved, is the pair of estimates

\[
a_0+\int_0^\infty\rho_D(t)
 \max_a\frac{\|e_{F,a}(t)\|_2+\|e_{B,a}(t)\|_2}{\sqrt n}dt
\le n^{-1/2}e^{-C\sqrt{\log(e+n)}},
\tag{37}
\]

\[
\left(\int\sup_{t\ge0}
             \frac{\|e_F(t,x)\|_2^4}{n^2}d\zeta(x)\right)^{1/2}
\le C_\zeta n^{-1/2},
\tag{38}
\]

on high-probability events for a partition with
\(q(N_1+N_2)=o(n)\), or the corresponding weaker source condition
that exploits prediction-level cancellation throughout the feedback
argument. Equations (37)--(38) are not asserted here. They concern the
actual reduced path and the reused original mixer; they cannot be
replaced by a cubature bound for an unrelated independent population.

The source criterion (37) is deliberately strong: it controls normalized
parameter distance through the known damping proof. Its failure alone
would not disprove a sharper prediction-only theorem. In particular,
the acceleration calculation is a source obstruction, not an
all-time-query lower bound.

For the particular modified weighted model proved here, the available
source estimate (20) is \(q^{-2+o(1)}\). Using it at
\(q=n^{1/4+o(1)}\), a genuine neuron source rate
\(N^{-\beta+o(1)}\), with \(N=\max(N_1,N_2)\), would require
\(N=n^{1/(2\beta)+o(1)}\). Its learned state would be
\(n^{1/4+1/(2\beta)+o(1)}\), whose power exponent is below one only if
\(\beta>2/3\). At equality the unspecified subpolynomial factors do
not decide whether the count is \(o(n)\). The current certified memory baseline for the original
width-\(n\) system is instead \(q=n^{1/6+o(1)}\). If a separate
all-order-uniform neuron-sampling theorem transferred that original
closure at rate \(N^{-\beta+o(1)}\), its conditional state exponent
would be \(1/6+1/(2\beta)\), strictly below one exactly when
\(\beta>3/5\); at equality subpolynomial factors again remain
undetermined. The newer history certificate has not been silently
transferred to the modified weighted model in (10). Ordinary
\(N^{-1/2}\) sampling meets neither threshold. Better history
approximation changes this arithmetic but cannot by itself establish
any neuron source rate.

The construction therefore isolates two substantive questions for a
structured cubature proof: which initialization-derived response marks
control all future actions of \(W_0\) and \(W_0^\top\), and whether
those actions admit a sufficiently fast, high-probability cubature rate
along the autonomous path. Section 6 proves why using only the initial
forward marks does not answer the first question. Neither a finite
sufficient mark dimension nor the needed rate is assumed in this note.
