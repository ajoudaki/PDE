# Polynomial dense variability and a third-order Legendre error estimate

2026-10-10. Scoped author derivation for the current compact-paper construction.
This is a candidate proof, not an independent review or a promoted result.
No paper, book, implementation, or Git-index changes are made.

The new deterministic step is a `q^{-3}` Legendre error estimate on the
existing finite-source event. It uses the existing closure and its existing
order; neither its stored variables nor its physical optimizer changes.
The dense lower bound below has a polynomial qualifying width and an explicit,
weaker coefficient than the compact paper's eventual lower bound. It concerns
the same actual independent dense runs and the same complete-trajectory norm.

## 1. Setup and scientific inputs

Use exactly `paper/compact.tex`: normalized inputs `v_a=x_a/sqrt(d)`, width
`n`, hidden depth `L>=2`, independent first-layer `N(0,1)` and later
`N(0,1/n)` entries, zero readout, loss `m^{-1} sum_a(f_a-y_a)^2`, and
mobilities `(n,1,...,1,n)`. Write

\[
X=\beta^L\ge100,\quad \lambda=\gamma/m\le1,\quad
\chi=1+\lambda^{-1},\quad z=Y/\lambda\le X^{-30},\quad
\ell=\log(en),\quad u=\sqrt\ell.
\tag{1}
\]

Here `z` without layer/sample indices is the scalar label-to-gap ratio.
Network preactivations remain `z_a^{(j)}`. The query domain is the whole
sphere for Legendre and can be any panel containing the training set for
the dense lower bound. No input-rank assumption is used.

The network is

\[
z_a^{(1)}=W^{(1)}v_a,\quad
z_a^{(j)}=W^{(j)}h_a^{(j-1)},\quad h_a^{(j)}=\phi_j(z_a^{(j)}),
\quad f_a=w^\top h_a^{(L)}/n,\quad r_a=f_a-y_a.
\]

Its backward responses are `k_a^{(L)}=w`,
`delta_a^{(j)}=phi_j'(z_a^{(j)}) odot k_a^{(j)}`, and
`k_a^{(j)}=W^{(j+1)T}delta_a^{(j+1)}`. Thus `delta` has no residual factor.

The source dependency used here is the *finite training-query* theorem in
`unseen_query_decoder_20261005/FULL_FINITE_SOURCE_PROBABILITY.md`, including
its augmented training-response calculation (15)--(28), with the arithmetic
refinement in `WIDTH_GATE_REFINEMENT.md`. These two files and
`EXPLICIT_FITTING_WIDTH.md` were read through their proofs. The current
compact Legendre proof was read in full. The source's older restriction
`m>=d` is not used in its finite-query insertion or concentration arguments;
the fitting proof expressly states and demonstrates this. A transfer to the
current paper must retain that observation rather than impose it as a new
hypothesis.

For source failure allocation `rho`, let

\[
p_\rho=\max\left\{1,\left\lceil
\frac{\log(4emL/\rho)}{\log(64e^2)}\right\rceil\right\},\qquad
\mathcal A_\rho=X^{2000}\chi^4(m+d+p_\rho+1)^4.
\]

A sufficient inherited source width is

\[
n\ge(\mathcal A_\rho/\rho)^{1100}.
\tag{2}
\]

It supplies, on a neighborhood of its closed rectangle,

\[
[-r,T+r]+i[-r,r],\quad T=32\ell/\lambda,\quad
r=\frac{c_\rho}{\sqrt\ell},\quad
c_\rho=\frac1{p_\rho X^{100}(1+\lambda)},
\tag{3}
\]

the training sources, the original RMS bounds, and the coordinate caps
proved by the source's scalar insertion argument. The compact small-label
bound implies the original source allowance by the compact foundation's
local power calculation. In particular the *actual* source constants have
`K_src<=X^{21}` and `U_fin<=X^{26}`; the much larger coefficients used in
the older width ledger are upper bounds, not a redefinition of these caps.

For training indices `a,b`, define the preactivation response in the
Euclidean mobility coordinates

\[
\theta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n),
\qquad R_{ba}^{(j)}=D_\theta z_b^{(j)}\nabla_\theta f_a.
\tag{4}
\]

This matches the source's `D_Theta z_b grad_Theta(n f_a)` for
`Theta=(W^(1),sqrt(n)W^(2),...,sqrt(n)W^(L),w)`. Its exact recurrences are

\[
\begin{split}
R_{ba}^{(1)}&=\delta_a^{(1)}v_a^\top v_b,\\
R_{ba}^{(j)}&=\delta_a^{(j)}c_{ab}^{(j-1)}+
 W^{(j)}Q_{ba}^{(j-1)},\qquad
c_{ab}^{(j-1)}=h_a^{(j-1)\top}h_b^{(j-1)}/n,\\
Q_{ba}^{(j)}&=\phi_j'(z_b^{(j)})\odot R_{ba}^{(j)}.
\end{split}
\tag{5}
\]

The finite source gives `max |R_{ba,i}^{(j)}|<=16z X^{26}u` through `T`.
The dense all-time carrier cap remains

\[
\max_{a,j,i,t\ge0}|k_{a,i}^{(j)}(t)|\le32X^{21}zu.
\tag{6}
\]

Both (6) and a loose all-time version of the response cap have polynomial
extension gates. Here are sufficient details for the latter, which the
Legendre improvement needs. The dense physical tail in the block-sum
mobility norm is at most
`2sqrt(L+1)Y lambda^{-1/2}(en)^{-16}`. Subtract the backward and (5)
recurrences with the state at `T` as reference. Each changed gate multiplies
the reference carrier or reference response, whose coordinate maximum is
known. Products use feature RMS bounds and mixer operator bounds.
The resulting RMS Lipschitz coefficients are at most
`X^{100}chi^2(1+u)` for both families. Passing to coordinates costs one
`sqrt(n)`. Consequently the tail is at most

\[
Y X^{103}\chi^3(1+u)n^{-31/2}.
\tag{7}
\]

A polynomial gate makes it less than `Y chi u`. This gives the convenient
all-time bound
`max |R_{ba,i}^{(j)}|<=Y X^{110}chi^3(1+u)`.
For (6) retain the sharper backward-only recurrence and its cap; this is
also the calculation in `POLYNOMIAL_SOURCE_WIDTH.md` (27)--(30).
No complex whole-sphere source is used in this route.

The following arguments are conditional on (2)'s inherited finite-source
theorem. They do not replace an independent audit of its insertion maps,
scalar traces, or probability composition.

## 2. A finite anti-concentration inequality, without a central limit theorem

Let `V_i` be independent identically distributed centered real random
variables with variance `sigma^2>0` and `E|V_i|^3<=M_3`. For
`Z=n^{-1/2}sum_i V_i`, every real `b`, and every `a>0`,

\[
\Pr\{|Z-b|\le a\}
\le3a/\sigma+4\exp\left\{-\frac{9a^2\sigma^4n}{128M_3^2}\right\}.
\tag{8}
\]

To prove it, let `V'` be an independent copy. Taylor's formula and
`E|V-V'|^3<=8M_3` give

\[
|\mathbb E e^{itV}|^2
=\mathbb E\cos(t(V-V'))
\le1-\sigma^2t^2+\tfrac43M_3|t|^3.
\]

Thus `|E exp(itV)|<=exp(-sigma^2 t^2/4)` when
`|t|<=3sigma^2/(8M_3)`. The characteristic function of `Z` has the
same Gaussian bound for `|t|<=3sigma^2 sqrt(n)/(8M_3)`.
The pointwise inequality
`1_{|x-b|<=a}<=exp(1/2)exp(-(x-b)^2/(2a^2))` and the Gaussian Fourier
identity bound its expectation by

\[
\frac{e^{1/2}a}{\sqrt{2\pi}}
\int_{\mathbb R}e^{-a^2t^2/2}|\mathbb E e^{itZ}|\,dt.
\]

On the central interval the full Gaussian integral is at most `3a/sigma`.
On its complement use `|E exp(itZ)|<=1` and the elementary Gaussian tail
bound `Pr(|G|>x)<=2exp(-x^2/2)`. This proves (8), uniformly in `b`.
The same proof holds conditionally on any sigma-field providing the stated
independence and deterministic moment bounds.

If `sigma>=sigma_0`, take `a=eta sigma_0/12`. Then

\[
n\ge2048\,M_3^2\sigma_0^{-6}\eta^{-2}\log(16/\eta)
\quad\Longrightarrow\quad
\sup_b\Pr\{|Z-b|\le\eta\sigma_0/12\}\le\eta/2.
\tag{9}
\]

### Conditional last-layer innovation

Condition on the first network through layer `L-1`, and on the entire
initialization of the independent second network. The last-layer feature
rows `U_i` of the first network are conditionally iid. Let
`Qbar=E[U_i U_i^T|F]`. On an event with polynomial qualifying width,

\[
\overline Q\succeq(\gamma/2)I,
\qquad \max_a\|U_{i,a}\|_{L^6(\Pr(\cdot\mid\mathcal F))}\le X^4.
\tag{10}
\]

Here is the quantitative initialization argument behind the first assertion.
Use `H=max_j sqrt(Q^(j)_{11})` enlarged to at least one, `R=2H`, and the
constants `K=b+sR`, `D=2sb+4s^2R`,
`T_1=sum_{i<L}s^i`, `T_2=sum_{i<L}s^{2i}` from the explicit fitting proof.
Let `C=T_2(2K+1+DT_1)` and take

\[
\epsilon=\min\{(8T_1)^{-1},
\gamma/[4m\max\{C,s^2C+DT_1\}]\}.
\]

Conditional Gaussian norm concentration and polarization give, with failure
at most `rho`, RMS-diagonal errors `Delta_j<=epsilon T_1` and entry errors
`E_j<=epsilon C` for `j<L`, provided

\[
n\ge32s^2R^2\epsilon^{-2}\log[32L(m+1)^2/\rho].
\tag{11}
\]

The conditional mean Gram at the last layer has entry error at most
`s^2 E_{L-1}+D Delta_{L-1}<=gamma/(4m)`. Thus it has gap at least
`3gamma/4`, proving (10)'s weaker gap. The recurrences for this argument are
`Delta_j<=epsilon+s Delta_{j-1}` and
`E_j<=(2K+1)epsilon+s^2 E_{j-1}+D Delta_{j-1}`. They remain valid at
singular intermediate covariances; the fitting proof separately couples
marginal standard deviations and interpolates correlations. In particular
(11) is at most `X^{40}chi^2 log[32L(m+1)^2/rho]`, up to a universal
factor. The marginal Gaussian input standard deviation is at most `2H`,
so `b+2sH ||G||_6<=X^4`, proving the second assertion.

The compact innovation argument does not require equal diagonal moments.
For any real random vector `U` with `Qbar>=gI`, put `c=Qbar y`,
`A=||c||`, `T=tr Qbar`, and `M_4=E||U||^4`. Its squared-area argument
gives

\[
\sum_a\operatorname{Var}[U_a(U^\top y)]
\ge\frac{(m-1)g^3(T-g)}{4M_4}\|y\|^2.
\tag{12}
\]

For clarity, its two spectral estimates are
`y^T Qbar^2(TI-Qbar)y >=(m-1)g ||Qbar y||^2` and
`>=g^2(T-g)||y||^2`; multiply them in the squared-area lower bound.
On (10), `g=gamma/2`, `T>=mg`, and `M_4<=m^2X^{16}`. Hence some
`F`-measurable training index `a_*` satisfies

\[
\sigma^2:=\operatorname{Var}[U_{a_*}(U^\top y)\mid\mathcal F]
\ge\frac{Y^2\gamma^4}{256X^{16}}=:\sigma_0^2.
\tag{13}
\]

Choose the smallest maximizing index to ensure measurability. A random
training witness is permitted because the target norm takes the maximum
over all training queries. Centered row products have third absolute moment
at most `8m^3Y^3X^{24}`, by the conditional `L^6` bound and
`sum_a|y_a|<=mY`. The ratio in (9) is therefore at most
`2^{30}m^6X^{96}gamma^{-12}`, with no inverse power of `Y`.

The exact initial derivative identity is

\[
\dot f_n(0,x_a)=\frac2{mn}\sum_iU_{i,a}(U_i^\top y).
\]

The second network and the conditional mean of the first contribute an
arbitrary shift. Applying (9) conditionally and averaging proves, after
(11) and the additional polynomial width

\[
n\ge2^{44}m^6X^{96}\gamma^{-12}\delta^{-2}\log(64/\delta),
\tag{14}
\]

that, except with probability at most `delta/2`,

\[
\max_a|\dot f_n(0,x_a)-\dot{\widetilde f}_n(0,x_a)|
\ge\frac{\delta Y\gamma^2}{192mX^8\sqrt n}.
\tag{15}
\]

One may allocate less failure to (11); the numerical constants above leave
slack. No qualitative conditional CLT or convergence of row variances is
used, and no deterministic population witness index is required.

## 3. From the derivative to actual positive-time variability

Apply the compact paper's derivative-to-trajectory lemma on the parameter-two
Bernstein ellipse of `[0,r]`, with (3) for both runs. Its real projection is
`[-r/8,9r/8]` and its imaginary projection `[-3r/8,3r/8]`, so it lies in
the source rectangle. The difference of the predictions is bounded there
by `32X^6Y/lambda`. With `N=ceil(2ell/log 2)<=4ell`, (15) gives

\[
\|f_n-\widetilde f_n\|_{\mathcal X}
\ge\frac{c_\rho\delta Y\gamma^2}
 {6144mX^8\sqrt n\ell^{5/2}}
 -\frac{768X^6Y}{\lambda n^2}.
\tag{16}
\]

The last term is at most half the first at polynomial width. An explicit
gate is

\[
n^{3/2}\ge2^{24}p_\rho X^{114}
 \frac{m(1+\lambda)}{\lambda\delta\gamma^2}\ell^{5/2}.
\tag{17}
\]

For example a sufficiently large universal constant times the fourth power
of `p_rho X^{120}m chi(1+gamma^{-1})^2 delta^{-1}` implies (17).
Combining allocations `rho=delta/8` for each source, and (11)--(15), yields
the convenient conclusion

\[
\Pr\left\{\|f_n-\widetilde f_n\|_{\mathcal X}
\ge a_\delta\frac{Y}{\sqrt n\ell^{5/2}}\right\}\ge1-\delta,
\qquad
a_\delta=\frac{\delta\gamma^2}
 {2^{20}mp_{\delta/8}X^{108}(1+\lambda)}.
\tag{18}
\]

All gates are polynomial in the exposed parameters, with logarithmic
confidence dependence through `p_rho`. The lower coefficient deliberately
retains the smaller radius. It is not the compact paper's stronger
`c_{phi,L,delta}sqrt(gamma)` coefficient. It supplies the same actual-dense
benchmark needed by the headline relative-error contract. The witness time
is strictly positive since both predictions vanish initially. At training
inputs both fitted limits equal the label, as they should.

## 4. A second-order forward-history estimate for the unchanged closure

Use the exact order-`q` Legendre closure, moments, clock, and reconstruction
in `compact_legendre.tex`. Its clock obeys
`tau(0)=1`, `dot tau=hat rho`, where `hat rho=||hat r||/sqrt(m)`.
The constant forward prefix and zero backward prefix are unchanged.
All quantities below are proof objects, not extra stored state.

Let `E_j` be its exact hidden physical defect,

\[
\dot{\widehat W}^{(j)}
=-\frac2{mn}\sum_a\widehat r_a\widehat\delta_a^{(j)}
                  \widehat h_a^{(j-1)\top}+\mathcal E_j,
\quad
\mathcal E_j=\frac{2\widehat\rho}{mn}
 \sum_a e_{b,a}^{(j)}e_{h,a}^{(j-1)\top}.
\tag{19}
\]

For a finite physical horizon `T_0`, define

\[
d_{T_0}=\int_0^{T_0}\sum_{j=2}^L\|\mathcal E_j(t)\|_Fdt,
\quad
D_{T_0}=\sup_{t\le T_0}\sum_{j=1}^{L+1}
                  \|\widehat\theta_j(t)-\theta_j(t)\|,
\quad A=\tau(T_0).
\tag{20}
\]

The all-order fitting proof already establishes

\[
\widehat\rho(t)\le Ye^{-\kappa t},\quad
\int_t^{T_0}\widehat\rho(s)ds\le\widehat\rho(t)/\kappa,
\quad \kappa=\lambda/4,\quad A\le1+4z\le2,
\tag{21}
\]

and uniform physical operator/readout/feature bounds. It also establishes
the pointwise defect estimate (paper equation `legendre-pointwise-defect`),
which makes the full closure hidden velocity, including `E_j`, bounded by
`Y` times a polynomial in `X,chi`, times `hat rho`, in block-sum norm.

We work temporarily on the bootstrap

\[
D_{T_0}\le Y/\sqrt n.
\tag{22}
\]

It starts with a strict margin at time zero. The source bounds and the
one-reference subtraction of the backward recurrences give

\[
\max_{a,j}\|\widehat k_a^{(j)}-k_a^{(j)}\|_2/\sqrt n
\le X^{40}(1+u)D_{T_0}.
\tag{23}
\]

For (5), subtract `delta c`, `W Q`, and `Q=phi'(z)R` with the dense
state as reference. The only curvature product is
`[phi'(hat z)-phi'(z)]R_D`, bounded in RMS by the dense coordinate cap
times the RMS preactivation difference. Iterating at most `L` times gives

\[
\max_{a,b,j}\|\widehat R_{ba}^{(j)}-R_{ba}^{(j)}\|_2/\sqrt n
\le X^{130}\chi^4(1+u)D_{T_0}.
\tag{24}
\]

For example the forward difference coefficient is at most `X^5`; feature
pairing differences cost at most `X^9 D`; the backward difference is
`X^{40}(1+u)D`; and a changed response gate costs at most
`Y X^{116}chi^3(1+u)D`. Propagation costs `(9s)^L<=X^2` and at most
`L<=X` summands. Since `Y<=1`, these are all bounded by (24).
Under (22), converting (23)--(24) to coordinate maxima costs
`sqrt(n)D_{T_0}<=Y`. Thus

\[
\max|\widehat k|\le Y X^{50}\chi(1+u),\qquad
\max|\widehat R|\le Y X^{135}\chi^4(1+u).
\tag{25}
\]

These are only training-query caps; they suffice for the history estimate.

### Differentiating the ordinary feature velocity

Put `hat v_a=hat r_a/hat rho`; then
`||hat v||_m=1` and `||dot hat v||_m<=X^{11}`, by the compact all-order
residual calculation. Let `F` denote the ordinary dense vector field at the
closure state in mobility coordinates. For a training feature, define

\[
a_b^{(j)}(t)
=D_\theta h_b^{(j)}(\widehat\theta(t))
             \frac{\mathcal F(\widehat\theta(t))}{\widehat\rho(t)}
=-\frac2m\phi_j'(\widehat z_b^{(j)})\odot
             \sum_a\widehat v_a\widehat R_{ba}^{(j)}.
\tag{26}
\]

The whole closure state, including its defect, is used here. The following
bounds follow from differentiating its actual equations:

\[
\begin{split}
\max_{b,j}\|\dot{\widehat z}_b^{(j)}\|_2/\sqrt n
   &\le YX^{30}\chi^3\widehat\rho,\\
\max_{a,j}\|\dot{\widehat\delta}_a^{(j)}\|_2/\sqrt n
   &\le X^{110}\chi^4(1+u)\widehat\rho,\\
\max_{a,b,j}\|\dot{\widehat R}_{ba}^{(j)}\|_2/\sqrt n
   &\le X^{220}\chi^8(1+u)\widehat\rho,\\
\max_{b,j}\bigl(\|a_b^{(j)}\|_2+
                    \|\dot a_b^{(j)}\|_2\bigr)/\sqrt n
   &\le YX^{230}\chi^8(1+u).
\end{split}
\tag{27}
\]

Here are the product estimates needed to verify these bounds and to avoid
an incorrect coordinate conversion. The full hidden block velocity is
`<=YX^{20}chi^3 hat rho`; propagating it through the forward differential
costs `X^5`, giving the first line with slack. Differentiating
`delta=phi'(z)k` gives `phi''(z) dot z k +phi'(z)dot k`. The first product
uses the **coordinate maximum of `k` and RMS of `dot z`** from (25) and
the first line, while
`dot k=dot W^T delta+W^T dot delta` uses operator bounds. At the top
`||dot w||/sqrt(n)<=X^4 hat rho`. The forcing is bounded by
`X^{90}chi^4(1+u)hat rho`; geometric propagation and `L<=X` are covered
by the second line.

Differentiate (5). Its terms are `dot delta c`, `delta dot c`,
`dot W Q`, `W phi''(z)dot z R`, and `W phi'(z)dot R`.
The curvature product uses the **coordinate maximum of `R` and RMS of
`dot z`**. The other terms use feature/response RMS, pairing derivatives,
and mixer norms. The largest forcing coefficient is bounded by
`X^{180}chi^8(1+u)` and the third line covers its finite propagation.
Finally differentiate (26); its three terms use respectively `dot z`
times the ordinary response maximum, `dot hat v` times response RMS,
and `dot R` times `||hat v||_m=1`. Since `hat rho<=Y`, they prove the
last line. **There is no estimate of `||dot z||_infinity`, and no
`sqrt(n)||E||` factor.** This is why (22) suffices despite the physical
defect in the state velocity.

### Removing the accumulated feature defect

For each feature history on `[0,A]`, subtract the primitive of its defect
contribution:

\[
g_b^{(j)}(\tau(t))
=\widehat h_b^{(j)}(t)
 -\int_0^tD_\theta h_b^{(j)}(\widehat\theta(s))
                               \mathcal E(s)\,ds.
\tag{28}
\]

Use its constant initialized value on `[0,1]`. Here `E` consists only of
the hidden matrix blocks `E_2,...,E_L`. The forward differential bound
and (20) give aggregate RMS history norm

\[
\|h-g\|_{L^2([0,A])}/\sqrt{mn}\le X^{10}d_{T_0}.
\tag{29}
\]

Each layer history is viewed as the vector over samples and neurons, with
the normalization `(mn)^{-1/2}`. Exactly,
`partial_tau g=a(t)` and
`partial_tau^2 g=dot a(t)/hat rho(t)` on `(1,A)`.
The first derivative is zero at the prefix join because the initialized
readout and all hidden ordinary velocities vanish. There is therefore no
delta distribution at `tau=1`.

The second-order Legendre operator is

\[
\mathscr D_A g=-\partial_\xi[\xi(A-\xi)\partial_\xi g].
\]

By (21), `(A-tau(t))/hat rho(t)<=1/kappa`. Equations (27)--(29) imply

\[
\|\mathscr D_A g\|_{L^2}/\sqrt{mn}
\le YX^{240}\chi^9(1+u).
\tag{30}
\]

This statement holds at every finite horizon, uniformly in that horizon.
There is no regularity assertion for the normalized residual at the fitted
endpoint. Its possible singularity after changing clocks is paid by the
factor `A-xi` in the operator.

The shifted Legendre modes have eigenvalues `j(j+1)` for `D_A`.
Two integrations by parts, whose boundary flux vanishes because `g'` is
bounded and `xi(A-xi)=0` at the endpoints, show

\[
\|(I-\Pi_q^A)g\|_{L^2}
\le[q(q+1)]^{-1}\|\mathscr D_Ag\|_{L^2}.
\tag{31}
\]

The prefix join has no flux jump. Bessel's inequality proves (31) for the
Hilbert-valued history. Projection contraction applied to `h-g` now gives
the improved forward tail. With the deliberately loose common coefficient

\[
P=X^{500}\chi^{10},
\]

and with `q<=sqrt(n)`, it is

\[
H_{T_0}:=\|(I-\Pi_q^A)h\|_{L^2}/\sqrt{mn}
\le\frac{YP\ell}{q^2}+P d_{T_0}.
\tag{32}
\]

## 5. Closing the projection defect with the current order

The existing backward-history argument is unchanged. Its dense comparison
and frozen tail give, under (22),

\[
B_{T_0}:=\|(I-\Pi_q^A)b\|_{L^2}/\sqrt{mn}
\le\frac{YP\ell}{q}+P\ell D_{T_0}
\le\frac{2YP\ell}{q},\qquad q\le\sqrt n.
\tag{33}
\]

Indeed its `b_0+b_1 sqrt(log q)` is at most `YP ell` since
`b_0<=X^{42}(Y/lambda)(1+zu)` and
`b_1<=X^{16}(Y/lambda)sqrt(chi)`; its response discrepancy coefficient
`B_d sqrt(4z)` is at most `P ell`. The last inequality uses (22).

For each fixed history, the growing-interval projection identity gives
the integral of squared endpoint error as its final squared tail norm;
the initial forward and backward projection errors vanish. Apply sample
and activity-clock Cauchy--Schwarz to (19), then sum interfaces:

\[
d_{T_0}\le2(L-1)H_{T_0}B_{T_0}.
\tag{34}
\]

The signed parameter comparison in the current paper is also unchanged:

\[
D_{T_0}\le\mathcal A_n d_{T_0},\qquad
\mathcal A_n\le eX\exp(X^{36}z^2u).
\tag{35}
\]

The small-label hypothesis makes `X^{36}z^2<=X^{-24}`. Young's inequality
therefore gives the uniform numerical estimate

\[
\mathcal A_n\le X^2n^{1/64}\le P n^{1/64}.
\tag{36}
\]

Substitute (32)--(33) into (34), use `2(L-1)<=P` and `Y<=1`, and
absorb its term linear in `d_{T_0}` when `q>=4P^3 ell`. This yields

\[
d_{T_0}\le4YP^3\ell^2/q^3,\qquad
D_{T_0}\le4YP^4\ell^2 n^{1/64}/q^3.
\tag{37}
\]

Take exactly the current size, with an allowed activation/depth prefactor
equal to one (a larger fixed prefactor is harmless):

\[
q=\left\lceil\lambda^{-3}n^{1/4}\ell^2e^{u/2}\right\rceil.
\tag{38}
\]

At polynomial width `n>=(C P)^{64}`, where `C` is a sufficiently large
universal constant, the following three inequalities all hold:

\[
q\le\sqrt n,\qquad q\ge4P^3\ell,\qquad
8P^4\ell^2\le n^{15/64}.
\tag{39}
\]

For explicit arithmetic, `ell^2 exp(sqrt(ell)/2)<=e^{100}n^{1/8}`
gives the first once `n>=(2e^{100}lambda^{-3})^8`; and
`ell^2<=C_1 n^{1/64}` with numerical
`C_1=e^{1/64}(128/e)^2` gives the other two. These are dominated by
`(CP)^{64}` after a universal enlargement. Ceilings cost a factor two.
The last inequality and `q>=n^{1/4}` make (37) strictly improve (22)
to `D_{T_0}<=Y/(2sqrt(n))`. Continuity excludes a first bootstrap exit.
All constants are independent of `T_0`, so the estimate holds for all
finite horizons and then for the fitted limits already supplied by
all-order fitting.

Whole-sphere prediction subtraction costs at most `X^7D`. Consequently

\[
\|f_{\rm Leg}-f_n\|_{\mathcal X}
\le\frac{4YP^5\ell^2}{n^{47/64}}.
\tag{40}
\]

The more informative intermediate estimate is `4Y X^7 P^3 A_n ell^2/q^3`.
Equation (40) is deliberately weakened to expose a fixed width power.
It is stronger than the current `CY/(sqrt(n)ell^3)` estimate after another
polynomial gate. The moving inventory is unchanged:

\[
n(d+1)+1+2(L-1)mnq.
\]

Thus its current headline form
`C m(m/gamma)^3 n^{5/4}ell^2 exp(sqrt(ell)/2)` is retained. Absorbing
`nd` only requires a separate polynomial gate, for example `n>=d^4`.
The `(L-1)n^2` initialized fixed mixer storage is unchanged.

## 6. Relative tolerance and remaining review boundary

On the dense lower event (18) and the Legendre event,

\[
\frac{\|f_{\rm Leg}-f_n\|_{\mathcal X}}
 {\|f_n-\widetilde f_n\|_{\mathcal X}}
\le\frac{4P^5}{a_\delta}\ell^{9/2}n^{-15/64}.
\tag{41}
\]

The elementary maximization of `(1+log n)^{9/2}n^{-7/64}` gives a
universal constant `C_2` such that the right side is at most
`4C_2 P^5 a_delta^{-1} n^{-1/8}`. Therefore a requested relative
tolerance `epsilon>0` follows from the additional polynomial gate

\[
n\ge[4C_2P^5/(a_\delta\epsilon)]^8.
\tag{42}
\]

Allocate confidence between the source and dense lower events by replacing
their `delta` with fixed fractions of the final failure probability.
No independence between the compression event and the lower event is used.
The chosen Legendre order (38) is independent of the requested tolerance;
only the qualifying width changes.

For either selected construction, *if* its existing `Y/n` absolute error
has a polynomial source/approximation gate, (18) yields ratio at most
`a_delta^{-1}ell^{5/2}/sqrt(n)`. Its requested-tolerance gate is likewise
polynomial. This statement does not supply the selected constructions'
own source or storage-count repairs.

The proof obligation that matters for a fresh review is the new deterministic
history argument (22)--(37), especially the differentiated response products
in (27), the zero prefix-join derivative in (28), and using the final-tail
identity (34) after subtracting a defect primitive. The source probability
theorem (2) is a named dependency whose inherited proof must be checked in
the overall assembly; it was not replaced here by a summary or a PASS label.

There is no remaining *identified* deterministic Legendre obstruction in
this route. The result remains an author candidate until independently
reconstructed. It does not assert that Harmonic or Taylor are repaired,
that the stronger original dense lower coefficient has polynomial onset,
or that the displayed very conservative polynomial degrees are practical.
