# Near-quadratic activation extension: deterministic implication

28 September 2026. Scoped continuation of this study. This note proves the
deterministic part of the extension from tanh to layer-dependent, globally
Lipschitz activations with globally Lipschitz derivatives. The activations
may be unbounded and may have nonzero offsets. The supplied probabilistic
input is explicitly a tail estimate for the **full dense backward carriers,
including the trained readout**. This note does not prove or assume without
disclosure that the tanh Gaussian argument transfers to these activations.

Scientific inputs read in full: `NEAR_QUADRATIC_ALLTIME_BOUND.md`,
`ACTIVATION_EXTENSION.md`, `ACTIVATION_SMALL_LABEL_ROUTE.md`,
`ACTIVATION_LOCAL_MODULUS.md`, `SMALL_LABEL_ENERGY.md`, and
`docs/notation.qmd`. The investigator and rigorous-math skills were applied.
No other study, external source, experiment, maintained-file change, or Git
mutation is part of this scoped derivation. It is an internal proof
dependency, not an independent promotion review.

## 1. Statement, supplied inputs, and the required correction

Use the canonical network, squared loss, mobilities, and original autonomous
old-clock closure of `ACTIVATION_EXTENSION.md`. In particular,

\[
 z_{1,a}=W_1x_a/\sqrt d,\quad z_{\ell,a}=W_\ell h_{\ell-1,a},\quad
 h_{\ell,a}=\phi^{(\ell)}(z_{\ell,a}),\quad f_a=w^Th_{L,a}/n,
 \qquad r_a=f_a-y_a.
 \tag{1}
\]

Depth, sample count, input dimension, and data are fixed. Both systems use
the same initialized arrays and exactly zero readout. Assume

\[
 \phi^{(\ell)}\in C^1(\mathbb R),\qquad
 \sup| (\phi^{(\ell)})'|\le s_\ell<\infty,\qquad
 \operatorname{Lip}((\phi^{(\ell)})';\mathbb R)\le j_\ell<\infty.
 \tag{2}
\]

Write \(a_\ell=|\phi^{(\ell)}(0)|\). No common activation, bounded
activation value, oddness, monotonicity, analyticity, or positive derivative
is assumed. The initial hidden operators and training preactivation RMS
have fixed bounds, the initial readout-feature Gram has a fixed positive
gap, and the fixed label RMS \(Y=\|y\|_m\) is sufficiently small and
positive as in the activation-general fitting theorem. This is a fixed
label regime, not label shrinkage with width or order.

For memory order \(q\ge1\), define

\[
 d_n(t)=\frac{\|\widehat W_1-W_{1,D}\|_F}{\sqrt n}
 +\sum_{\ell=2}^L\|\widehat W_\ell-W_{\ell,D}\|_F
 +\frac{\|\widehat w-w_D\|_2}{\sqrt n},\qquad
 D_n(q)=\sup_{t\ge0}d_n(t).
 \tag{3}
\]

The existing activation-general physical/activity bounds are supplied
inputs. For both paths they give, with constants independent of width,
order, and physical time,

\[
 \|W_\ell\|_{\mathrm{op}}\le C\quad(\ell\ge2),\qquad
 \max_{\ell,a}\frac{\|z_{\ell,a}\|_2+\|h_{\ell,a}\|_2}{\sqrt n}\le C,
 \qquad \frac{\|w\|_2}{\sqrt n}
       +\max_{\ell,a}\frac{\|\delta_{\ell,a}\|_2}{\sqrt n}\le CY,
 \tag{4}
\]
\[
 \Gamma_w(t)\succeq\lambda I_m/2,\quad
 Y e^{-\Lambda t}\le\rho(t)\le Y e^{-\kappa t},\quad
 \int_t^\infty\rho(s)\,ds\le\rho(t)/\kappa,
 \tag{5}
\]
\[
 \frac{\|\dot W_1\|_F}{\sqrt n}
 +\sum_{\ell=2}^L\|\dot W_\ell\|_F\le CY\rho,
 \qquad \frac{\|\dot w\|_2}{\sqrt n}\le C\rho,
 \qquad
 \max_{\ell,a}\frac{\|\dot z_{\ell,a}\|_2+\|\dot h_{\ell,a}\|_2}{\sqrt n}
 \le CY\rho.
 \tag{6}
\]

Here each \(\rho\) belongs to its own path. The closure has exact physical
equation \(\dot{\widehat\theta}=F(\widehat\theta)+E\), where the outer
blocks of \(E\) vanish and

\[
 e_E(t):=\sum_{\ell=2}^L\|E_\ell(t)\|_F
 \le CY^{5/2}\widehat\rho(t),\qquad
 \varepsilon:=\int_0^\infty e_E(t)\,dt\le C/q.
 \tag{7}
\]

Global existence and these bounds hold for every finite order before the
comparison below. In particular \(D_n(q)\) is uniformly bounded: integrate
the physical velocities from the common initial parameters. Also
\(\int_0^\infty\|\widehat r-r_D\|_m\,dt\le
\int_0^\infty(\widehat\rho+\rho_D)\,dt<\infty\).

Define the dense **full** carriers by

\[
 k_{L,a,D}=w_D,\qquad
 k_{\ell,a,D}=W_{\ell+1,D}^{T}\delta_{\ell+1,a,D}\quad(\ell<L),
 \tag{8}
\]
\[
 H_n(M,t)=\sum_{\ell=1}^L\max_a
 \left(\frac1n\sum_i|k_{\ell,a,i,D}(t)|^2
                   \mathbf1_{\{|k_{\ell,a,i,D}(t)|>M\}}\right)^{1/2},
 \qquad
 Z_n(M)=\int_0^\infty\rho_D(t)H_n(M,t)\,dt.
 \tag{9}
\]

The supplied dense-only tail hypothesis is, simultaneously for all integers
\(M\ge M_0\),

\[
 Z_n(M)\le C e^{-cM^2}+a_n,
 \qquad a_n\ge0.
 \tag{10}
\]

For a probabilistic application, (4)--(10) hold on common events of
probability tending to one and \(a_n\to0\) in probability. The
deterministic proof below uses only the displayed estimate, not Gaussian
independence, trained closure Gaussianity, or any carrier coordinate
bound. Equation (4) implies \(H_n(M,t)\le C\) for all cutoffs and times.

**Conditional deterministic theorem.** Under these inputs, simultaneously
for every \(q\ge1\),

\[
 D_n(q)\le C\Phi(q^{-2}+a_n),\qquad
 \Phi(s)=s\exp\!\left(K\sqrt{\log(e+1/s)}\right),\quad \Phi(0)=0.
 \tag{11}
\]

Consequently, under the stated probabilistic tail input,

\[
 D_n(q)\le Cq^{-2}e^{K\sqrt{\log(e+q)}}+b_n,
 \qquad b_n\xrightarrow{\Pr}0,
 \tag{12}
\]

where the same dense-only \(b_n\) works for all orders. Constants may
depend on fixed data, depth, activation constants, initialization bounds,
Gram gap, and the fixed small-label regime. They do not depend on
\(n,q,t\). The theorem asserts neither exact \(Cq^{-2}\) nor a numerical
width rate.

The essential correction to the tanh auxiliary construction is

\[
 \delta^M_{L,a}=(\phi^{(L)})'(\widehat z_{L,a})
                         \odot\operatorname{clip}_M(\widehat w).
 \tag{13}
\]

For unbounded activations, the actual readout and its velocity have only
RMS bounds in (4), (6); their coordinate maxima need not be bounded
uniformly in width. Keeping the actual top response as the auxiliary top
response would leave precisely that unproved coordinate bound in the
regularity argument. Clipping (13) is used only in this proof. The closure
algorithm is unchanged.

## 2. Full-carrier damping estimate

Forward subtraction and bounded slopes give

\[
 \max_{\ell,a}\frac{\|\widehat z_{\ell,a}-z_{\ell,a,D}\|_2
                  +\|\widehat h_{\ell,a}-h_{\ell,a,D}\|_2}{\sqrt n}
 \le C d_n(t).
 \tag{14}
\]

At a hidden link, use
\((\widehat W-W_D)h_D+\widehat W(\widehat h-h_D)\).
The first term is bounded by the dense feature RMS times
\(\|\widehat W-W_D\|_F\), and the second by the common operator bound
times the preceding RMS difference. This verifies (14) without bounded
feature coordinates.

Let \(g_\ell=(\phi^{(\ell)})'\). For each dense carrier the gate term
has the bound

\[
 \frac{\|(g_\ell(\widehat z)-g_\ell(z_D))\odot k_D\|_2}{\sqrt n}
 \le j_\ell M\frac{\|\widehat z-z_D\|_2}{\sqrt n}
       +2s_\ell\frac{\|k_D\mathbf1_{\{|k_D|>M\}}\|_2}{\sqrt n}.
 \tag{15}
\]

This follows by separating \(|k_D|\le M\) and its complement. The exact
backward subtraction below the top is

\[
 \begin{split}
 \widehat\delta_\ell-\delta_{\ell,D}
 ={}&g_\ell(\widehat z_\ell)\odot
       \widehat W_{\ell+1}^T
                  (\widehat\delta_{\ell+1}-\delta_{\ell+1,D})\\
 &+g_\ell(\widehat z_\ell)\odot
       (\widehat W_{\ell+1}-W_{\ell+1,D})^T\delta_{\ell+1,D}\\
 &+(g_\ell(\widehat z_\ell)-g_\ell(z_{\ell,D}))\odot k_{\ell,D}.
 \end{split}
 \tag{16}
\]

At the top, the first term is the gate times \(\widehat w-w_D\), with
the same full-carrier gate term. Equations (4), (14)--(16), followed by
downward induction through fixed depth, prove

\[
 B(t):=\max_{\ell,a}
       \frac{\|\widehat\delta_{\ell,a}-\delta_{\ell,a,D}\|_2}{\sqrt n}
 \le C[(1+M)d_n(t)+H_n(M,t)].
 \tag{17}
\]

There is no initialized/learned decomposition in (15)--(17). The
bounded-activation learned-coordinate estimate in `SMALL_LABEL_ENERGY.md`
is not invoked.

For completeness the tangent Gram is

\[
 \Gamma_{ab}=\frac1m\left[
 \frac{h_{L,a}^Th_{L,b}}n+
 \frac{\delta_{1,a}^T\delta_{1,b}}n\frac{x_a^Tx_b}d+
 \sum_{\ell=2}^L\frac{\delta_{\ell,a}^T\delta_{\ell,b}}n
                     \frac{h_{\ell-1,a}^Th_{\ell-1,b}}n\right].
 \tag{18}
\]

Each is a positive semidefinite parameter-derivative Gram and
\(\Gamma\succeq\Gamma_w\). Differences of its forward pairings are
bounded by \(Cd_n\), and differences of backward pairings by \(CYB\),
by Cauchy--Schwarz and (4). Products in (18) therefore give

\[
 \|\widehat\Gamma-\Gamma_D\|_{\mathrm{op}}
 \le C[(1+M)d_n+H_n(M,t)].
 \tag{19}
\]

Here a sample matrix whose entries are at most \(A/m\) in absolute
value has operator norm at most \(A\), by its row and column sums.
Also
\((\widehat JE)_a=\sum_{\ell\ge2}
\widehat\delta_{\ell,a}^TE_\ell\widehat h_{\ell-1,a}/n\), so
\(\|\widehat JE\|_m\le CY e_E\).

Set \(u=\widehat r-r_D\), \(v=\|u\|_m\), and
\(Q(t)=\int_0^t v(s)ds\). Subtracting the residual equations gives

\[
 \dot u=-2\widehat\Gamma u
        -2(\widehat\Gamma-\Gamma_D)r_D+\widehat JE.
 \tag{20}
\]

The Gram gap, (19), and the norm derivative imply

\[
 D^+v\le-\lambda v+C\rho_D[(1+M)d_n+H_n]+Ce_E.
 \tag{21}
\]

One may integrate the regularized norm \(\sqrt{v^2+\eta^2}\) and let
\(\eta\downarrow0\) to include zeros of \(v\). Since \(u(0)=0\),
discarding the nonnegative terminal value after integration gives

\[
 Q(t)\le C\left[(1+M)\int_0^t\rho_Dd_n\,ds
                       +Z_n(M;t)+\varepsilon(t)\right],
 \tag{22}
\]

where \(Z_n(M;t)\) and \(\varepsilon(t)\) stop their defining integrals
at \(t\).

Subtract readout updates as
\(\widehat r\widehat h-r_Dh_D=u\widehat h+r_D(\widehat h-h_D)\).
For a hidden block use the three terms
\(u\widehat\delta\widehat h^T\),
\(r_D(\widehat\delta-\delta_D)\widehat h^T\), and
\(r_D\delta_D(\widehat h-h_D)^T\); use the fixed input in the first
block. The identity
\(\|ab^T/n\|_F=(\|a\|_2/\sqrt n)(\|b\|_2/\sqrt n)\),
(4), (14), and (17) bound the summed parameter differences by

\[
 d_n(t)\le C\varepsilon(t)+CQ(t)
       +C\int_0^t\rho_D[(1+M)d_n+H_n]ds.
 \tag{23}
\]

Insert (22). On a fixed terminal interval replace the nondecreasing
inhomogeneous term by its terminal value, and differentiate its integral
majorant. Integration of that scalar inequality and
\(\int\rho_D\le CY\) yield

\[
 D_n(q)\le A_M[\varepsilon+Z_n(M)],\qquad A_M=Ce^{KM}\ge1,
 \tag{24}
\]
\[
 Q:=Q(\infty)\le C[(1+M)D_n(q)+Z_n(M)+\varepsilon].
 \tag{25}
\]

This derives the required damping estimate with unbounded RMS features
and full carriers. The exponent grows linearly in the cutoff, not as a
cutoff power depending on depth.

## 3. Absolute defect from the two history tails

The closure clock is \(\tau(t)=1+\int_0^t\widehat\rho\), bounded above
by a fixed constant. Define \(c_a=\widehat r_a/\widehat\rho\) and
\(b_{\ell,a}=c_a\widehat\delta_{\ell,a}\) on the physical part of the
history. Forward prefixes are constant and backward prefixes are zero.
The positive lower bound in (5) makes this change of variables legitimate
on every finite physical interval. Equations (18), (7), and the residual
equation imply \(\|\dot{\widehat r}\|_m\le C\widehat\rho\); hence
\(\|\dot c\|_m\le C\), with \(|c_a|,|\dot c_a|\le C\) because
sample count is fixed.

Let \(\Pi_q^A\) project onto polynomials of degree below \(q\) on
\([0,A]\). The exact closure identity is

\[
 E_\ell(t)=\frac{2\widehat\rho(t)}m\sum_a
 \frac{(b_{\ell,a}-b_{\ell,a}^*)
       (h_{\ell-1,a}-h_{\ell-1,a}^*)^T}{n},
 \tag{26}
\]

where a star denotes projection evaluated at the current right endpoint.
For any of these histories set
\(V_q(A)=\int_0^A\|v-\Pi_q^A v\|_2^2/n\,d\xi\). Then

\[
 V_q'(A)=\|v(A)-(\Pi_q^A v)(A)\|_2^2/n\quad\text{a.e.}
 \tag{27}
\]

Indeed, the differentiated least-squares polynomial still has degree
below \(q\), so its pairing with the projection error vanishes. The
moment formula and invertible polynomial Gram matrix justify local
absolute continuity of its coefficients. Both prefix errors vanish at
\(A=1\). Integrating (26), changing variables
\(d\xi=\widehat\rho\,dt\), and using (27) with Cauchy--Schwarz gives

\[
 \varepsilon(t)\le\frac2m\sum_{\ell=2}^L\sum_a
 \left(\int_0^{\tau(t)}
       \frac{\|(I-\Pi_q^{\tau(t)})b_{\ell,a}\|_2^2}{n}\,d\xi\right)^{1/2}
 \left(\int_0^{\tau(t)}
       \frac{\|(I-\Pi_q^{\tau(t)})h_{\ell-1,a}\|_2^2}{n}\,d\xi\right)^{1/2}.
 \tag{28}
\]

The weighted Legendre inequality needed below is, for an ordinary
Hilbert-valued \(H^1\) function,

\[
 \|(I-\Pi_q^A)v\|_{L^2}^2
 \le\frac1{q(q+1)}\int_0^A\xi(A-\xi)\|v'(\xi)\|^2d\xi.
 \tag{29}
\]

To verify it, use the normalized shifted Legendre modes satisfying
\(-[\xi(A-\xi)e_j']'=j(j+1)e_j\). Integration by parts has zero
endpoint terms, and the functions
\(\sqrt{\xi(A-\xi)}e_j'/\sqrt{j(j+1)}\), \(j\ge1\), are orthonormal.
Bessel's inequality bounds the sum of squared history coefficients
weighted by \(j(j+1)\) by the right-hand energy. Each omitted mode
\(j\ge q\) has weight at least \(q(q+1)\). Smooth approximation gives
the \(H^1\) statement; orthonormal coordinate expansion gives the
Hilbert-valued version.

Apply (29) to the normalized vector \(h/\sqrt n\). By (6), its clock
derivative is bounded by \(CY\), is zero on the prefix, and has a
uniformly bounded squared integral. Thus the second factor of (28) is
at most \(C/q\), uniformly in the terminal time.

## 4. Clipped auxiliary history, including the top readout

Let \(\operatorname{clip}_M\) clamp each coordinate to \([-M,M]\).
Use (13) and, for \(\ell<L\), define at the actual closure state

\[
 \delta^M_{\ell,a}=g_\ell(\widehat z_{\ell,a})\odot
 \operatorname{clip}_M(\widehat W_{\ell+1}^T\delta^M_{\ell+1,a}).
 \tag{30}
\]

Clipping is one-Lipschitz and decreases coordinate magnitudes.
Consequently \(\|\delta^M_{\ell,a}\|_2/\sqrt n\le CY\) by
downward induction. At the top the almost-everywhere product/chain bound is

\[
 \frac{\|\dot\delta^M_{L,a}\|_2}{\sqrt n}
 \le j_L M\frac{\|\dot{\widehat z}_{L,a}\|_2}{\sqrt n}
       +s_L\frac{\|\dot{\widehat w}\|_2}{\sqrt n}
 \le C(1+M)\widehat\rho.
 \tag{31}
\]

For a lower layer it is

\[
 \begin{split}
 \frac{\|\dot\delta^M_{\ell,a}\|_2}{\sqrt n}
 \le{}&j_\ell M\frac{\|\dot{\widehat z}_{\ell,a}\|_2}{\sqrt n}
 +s_\ell\|\dot{\widehat W}_{\ell+1}\|_{\mathrm{op}}
                         \frac{\|\delta^M_{\ell+1,a}\|_2}{\sqrt n}\\
 &+s_\ell\|\widehat W_{\ell+1}\|_{\mathrm{op}}
                         \frac{\|\dot\delta^M_{\ell+1,a}\|_2}{\sqrt n}.
 \end{split}
 \tag{32}
\]

A Lipschitz scalar function composed with an absolutely continuous
coordinate is absolutely continuous; difference quotients give its
derivative bound by the Lipschitz constant times coordinate speed almost
everywhere. This justifies (31)--(32) for clipping and for merely Lipschitz
activation derivatives, including unit ELU. The recurrence adds cutoff
contributions; the coefficient propagating the next derivative contains
no cutoff. Fixed depth therefore preserves \(C(1+M)\widehat\rho\).

Put \(b^M_{\ell,a}=c_a\delta^M_{\ell,a}\) with zero prefix. Zero
initial readout makes it continuous at the prefix join. Its amplitude is
bounded in RMS and

\[
 \|\dot b^M_{\ell,a}(t)\|_2/\sqrt n
 \le C[1+(1+M)\widehat\rho(t)].
 \tag{33}
\]

For a terminal time \(t\), freeze this history after physical time
\(T\) when \(T<t\), calling the result \(b_T^M\). It is \(H^1\)
on the finite terminal clock interval: before the cutoff the residual
has a positive lower bound, and afterwards its derivative is zero.
The freeze error has normalized history norm at most
\(Ce^{-\kappa T/2}\), since its amplitude is bounded and its support
has clock length at most \(\widehat\rho(T)/\kappa\). Moreover,

\[
 \begin{split}
 \int_0^{\tau(t)}\xi(\tau(t)-\xi)
               \frac{\|\partial_\xi b_T^M\|_2^2}{n}\,d\xi
 &\le \frac{\sup_s\tau(s)}\kappa
       \int_0^{\min(t,T)}\frac{\|\dot b^M(s)\|_2^2}{n}\,ds\\
 &\le C[T+(1+M)^2].
 \end{split}
 \tag{34}
\]

The first inequality uses
\(\tau(t)-\tau(s)\le\int_s^\infty\widehat\rho
\le\widehat\rho(s)/\kappa\) to cancel the inverse clock speed.
The second uses (33) and the bounded integral of \(\widehat\rho^2\).
Equation (29) and projection contraction give

\[
 \left(\int_0^{\tau(t)}
       \frac{\|(I-\Pi_q^{\tau(t)})b^M_{\ell,a}\|_2^2}{n}\,d\xi\right)^{1/2}
 \le C\left[\frac{1+M+\sqrt T}{q}+e^{-\kappa T/2}\right].
 \tag{35}
\]

## 5. Auxiliary mismatch and quadratic absorption

Compare (13), (30) with the dense response. At the top, subtract by adding
and subtracting \(g_L(\widehat z_L)\operatorname{clip}_M(w_D)\)
and \(g_L(z_{L,D})\operatorname{clip}_M(w_D)\). The three terms are
bounded by readout discrepancy, \(CMd_n\), and the dense readout tail.
At a lower layer write the auxiliary input as
\(\widehat W_{\ell+1}^T\delta^M_{\ell+1}\). The difference of its
clipped version from the clipped dense full carrier is bounded, by
clipping contraction, by

\[
 C\frac{\|\delta^M_{\ell+1}-\delta_{\ell+1,D}\|_2}{\sqrt n}
 +CY\|\widehat W_{\ell+1}-W_{\ell+1,D}\|_F.
\]

The changed gate multiplying the clipped dense carrier costs \(CMd_n\);
the remaining dense clipping error costs its term in \(H_n\).
Downward induction and then (17) give

\[
 \max_{\ell,a}\frac{\|\delta^M_{\ell,a}-\delta_{\ell,a,D}\|_2}{\sqrt n}
 \le C[(1+M)d_n+H_n],\qquad
 \max_{\ell,a}\frac{\|\widehat\delta_{\ell,a}-\delta^M_{\ell,a}\|_2}{\sqrt n}
 \le C[(1+M)d_n+H_n].
 \tag{36}
\]

Multiplication by the bounded \(c_a\) and integration in the closure's
own clock imply, uniformly in terminal time,

\[
 \left(\int_0^{\tau(t)}\frac{\|b_{\ell,a}-b^M_{\ell,a}\|_2^2}{n}
                      \,d\xi\right)^{1/2}
 \le C(1+M)D_n(q)+C\sqrt{Z_n(M)+Q}.
 \tag{37}
\]

To verify the second term, \(H_n\le C\) and
\(|\widehat\rho-\rho_D|\le\|\widehat r-r_D\|_m\) give

\[
 \int_0^\infty\widehat\rho H_n^2\,dt
 \le C\int_0^\infty\rho_D H_n\,dt
        +C\int_0^\infty|\widehat\rho-\rho_D|\,dt
 \le C[Z_n(M)+Q].
 \tag{38}
\]

No ratio between the dense and closure clocks is used. Combining
(28), the \(C/q\) forward tail, (35), and (37), and then increasing
the terminal time to infinity, yields

\[
 \varepsilon\le C\left[
 \frac{1+M+\sqrt T}{q^2}+\frac{e^{-\kappa T/2}}q
 +\frac{(1+M)D_n(q)}q+\frac{\sqrt{Z_n(M)+Q}}q\right].
 \tag{39}
\]

Uniformity in terminal time and monotonicity of \(\varepsilon(t)\)
justify this passage. Set \(U=\varepsilon+Z_n(M)\). Equations
(24)--(25) give \(D_n(q)\le A_MU\) and
\(Z_n(M)+Q\le C(1+M)A_MU\). Thus

\[
 U\le Z_n(M)+C\left[\frac{1+M+\sqrt T}{q^2}
                         +\frac{e^{-\kappa T/2}}q\right]
 +\frac{C(1+M)A_M}{q}U
 +\frac{C\sqrt{(1+M)A_M}}q\sqrt U.
 \tag{40}
\]

If \(C(1+M)A_M/q\le1/4\), absorb the linear term. Apply
\(h\sqrt U\le U/4+h^2\) to the last term, absorb again, and multiply
by \(A_M\). This proves the explicit cutoff estimate

\[
 D_n(q)\le C A_M Z_n(M)
 +C A_M\left[\frac{1+M+\sqrt T}{q^2}
                         +\frac{e^{-\kappa T/2}}q\right]
 +\frac{C(1+M)A_M^2}{q^2}.
 \tag{41}
\]

Put \(s=q^{-2}+a_n\). For small \(s\), choose an integer cutoff with
\(Ce^{-cM^2}\le s\) and
\(M\le C+C\sqrt{\log(e+1/s)}\), and choose
\(T\le C\log(e+1/s)\) so \(e^{-\kappa T/2}\le\sqrt s\).
Then \(Z_n(M)\le Cs\), \(q^{-1}e^{-\kappa T/2}\le s\), and
\(M\le C+C\sqrt{\log(e+q)}\) because \(s\ge q^{-2}\).
The absorption condition therefore holds above one order threshold
independent of width and of \(a_n\). Every term of (41) is bounded by
the right-hand side of (11), after enlarging \(K\) to absorb logarithmic
factors. The common bound on \(D_n(q)\) handles the finitely many smaller
orders and all non-small \(s\).

Finally \(\Phi(s)/s\) is decreasing. Hence
\(\Phi(x+y)\le\Phi(x)+\Phi(y)\), by multiplying its value at
\(x+y\) separately by \(x\) and \(y\). Taking
\(b_n=C\Phi(a_n)\) proves (12). For every fixed \(0<\gamma<2\),
\(\Phi(s)\le C_\gamma s^{\gamma/2}\) on bounded intervals, so one
also has \(D_n(q)\le C_\gamma(q^{-\gamma}+a_n^{\gamma/2})\).

## 6. Test predictions, offsets, and full-domain compactness

For this section additionally assume a fixed bound on
\(\|W_{1,0}\|_F/\sqrt n\). The training-preactivation-only bound does
not control directions outside the span of the training inputs and does
not suffice for this assertion. Equation (6) preserves the first-matrix
bound for all times and orders.

For every test input \(x\in\mathbb R^d\), linear growth and forward
induction now give, on either path,

\[
 \frac{\|h_\ell(t,x)\|_2}{\sqrt n}\le C(1+\|x\|_2),\qquad
 |f(t,x)|\le CY(1+\|x\|_2).
 \tag{42}
\]

Subtracting forward recursions, as in (14), gives
\(\|\widehat h_L(t,x)-h_{L,D}(t,x)\|_2/\sqrt n
\le C(1+\|x\|_2)d_n(t)\). Therefore

\[
 |\widehat f_{n,q}(t,x)-f_{n,D}(t,x)|
 \le C(1+\|x\|_2)d_n(t),
 \tag{43}
\]

by expanding the output as
\((\widehat w-w_D)^T\widehat h_L/n
 +w_D^T(\widehat h_L-h_{L,D})/n\).
The constant term in \(1+\|x\|_2\) is essential when activations have
nonzero offsets: at \(x=0\), readout differences can still change the
prediction. A bound proportional to \(\|x\|_2d_n\) would be false in
that class.

For any probability test law \(\mu\) with finite second input moment,

\[
 \left[\int\sup_{t\ge0}
       |\widehat f_{n,q}(t,x)-f_{n,D}(t,x)|^2\,\mu(dx)\right]^{1/2}
 \le C\left[\int(1+\|x\|_2)^2\mu(dx)\right]^{1/2}D_n(q).
 \tag{44}
\]

This is a full-domain statement, not an assertion restricted to compactly
supported test laws. The reverse triangle inequality gives the same
bound for the difference of test RMSEs to any target in \(L^2(\mu)\),
uniformly in time. On a ball of radius \(R\), the maximum absolute
prediction discrepancy is at most \(C(1+R)D_n(q)\).

There is also enough regularity for predictor compactness, without a
coordinate bound on any feature. The first-matrix bound, the hidden
operator bounds, and the global slopes imply

\[
 |f(t,x)-f(t,x')|\le CY\|x-x'\|_2.
 \tag{45}
\]

Differentiate the test forward recursion using (6). Its feature speed is
at most \(C\rho(t)(1+\|x\|_2)\) in RMS; the readout product then gives
\(|\partial_t f(t,x)|\le C e^{-\kappa t}(1+\|x\|_2)\). Hence

\[
 |f(t,x)-f(s,x)|\le
 C(1+\|x\|_2)|e^{-\kappa t}-e^{-\kappa s}|,
 \tag{46}
\]

including the limiting endpoint \(t=\infty\). After the change
\(u=e^{-\kappa t}\), these predictors are uniformly bounded and
equicontinuous on every compact \([0,1]\times\overline B_R\).
The elementary compactness theorem for such continuous families gives
uniformly convergent subsequences on each compact; a diagonal choice
over integer radii gives local uniform convergence on the whole domain,
including infinite time. Equation (42) then upgrades this to convergence
in the norm in (44): the input tail is uniformly bounded by a constant
times \(\int_{\|x\|>R}(1+\|x\|)^2d\mu\), which tends to zero, while
the compact part converges uniformly.

Thus, for fixed order and a deterministic sequence on which the common
bounds hold and \(a_n\to0\), every joint dense/closure predictor limit
pair satisfies the pure order bound in (12), (43)--(44). Identification
of the dense limit with a particular population flow is a separate input.
This deterministic argument does not supply a unique fixed-order
population closure ODE. In a probabilistic formulation, the compact
families just described also supply tightness on the common high-probability
events; a claimed limit must still specify its convergence mode.

## 7. Local derivative moduli: a precise additional tail requirement

Now replace global derivative Lipschitzness by
\(\phi^{(\ell)}\in C^{1,1}_{\mathrm{loc}}\), retaining the global slope
bounds. The physical/activity inputs remain available, but (15) and
(31) no longer have a common global \(j_\ell\). Set

\[
 \ell(R)=\max_\ell\operatorname{Lip}
       ((\phi^{(\ell)})';[-R,R]),\qquad R\ge1.
\]

Use proof gates \(g_{\ell,R}(u)=g_\ell(\operatorname{clip}_R u)\)
in (13), (30), as well as carrier clipping at \(M\). These gates are
bounded by the original slope bounds and globally Lipschitz with constant
at most \(\ell(R)\). Their auxiliary derivative bound is
\(C[1+M\ell(R)]\widehat\rho\).

Define the dense mixed tail and the cutoff coefficient

\[
 H_n(M,R,t)=\sum_\ell\max_a
 \left[\frac1n\sum_i|k_{\ell,a,i,D}|^2
   \mathbf1_{\{|k_{\ell,a,i,D}|>M\ \mathrm{or}\ |z_{\ell,a,i,D}|>R\}}
 \right]^{1/2},
\]
\[
 Z_n(M,R)=\int_0^\infty\rho_D H_n(M,R,t)dt,\qquad
 B(M,R)=1+M[\ell(2R)+1/R].
 \tag{47}
\]

As before \(H_n(M,R,t)\le C\). To check the actual gate comparison,
on \(|z_D|\le R\) and \(|\widehat z-z_D|\le R\) both arguments
lie in \([-2R,2R]\), so the local Lipschitz bound applies. On
\(|\widehat z-z_D|>R\), the bounded gates give
\(|g(\widehat z)-g(z_D)|\le2s|\widehat z-z_D|/R\).
The remaining coordinates have \(|z_D|>R\) and are included in
(47). After also separating \(|k_D|>M\), the counterpart of (15) is
bounded by

\[
 C M[\ell(2R)+1/R]\frac{\|\widehat z-z_D\|_2}{\sqrt n}
 +C\left[\frac1n\sum_i|k_{i,D}|^2
       \mathbf1_{\{|k_{i,D}|>M\ \mathrm{or}\ |z_{i,D}|>R\}}\right]^{1/2}.
 \tag{48}
\]

For the auxiliary comparison, use
\(|g_R(\widehat z)-g_R(z_D)|\le\ell(R)|\widehat z-z_D|\),
while \(g_R(z_D)-g(z_D)\) vanishes on \(|z_D|\le R\). This gives
the same bound. Thus every step of Sections 2--5 applies with
\(1+M\) replaced by \(B=B(M,R)\), the mixed \(Z=Z_n(M,R)\), and
\(A=Ce^{KB}\). In particular, whenever \(CBA/q\le1/4\),

\[
 D_n(q)\le CAZ
       +CA\left[\frac{B+\sqrt T}{q^2}+\frac{e^{-\kappa T/2}}q\right]
       +\frac{CBA^2}{q^2}.
 \tag{49}
\]

This is a deterministic two-cutoff theorem. It also identifies the missing
input for quantitative local-modulus consequences. The original supplied
carrier estimate (10), combined only with preactivation RMS, gives

\[
 Z_n(M,R)\le Z_n(M)+CM/R.
 \tag{50}
\]

Indeed on the remaining set the carrier is at most \(M\), and the
fraction with \(|z_D|>R\) has square root at most its preactivation
RMS divided by \(R\). This generally does not offset the amplification
in (49). A near-quadratic local-modulus theorem is therefore not asserted
from carrier tails alone.

One sufficient additional source is an activity-weighted dense
**preactivation RMS-tail** estimate

\[
 P_n(R):=\int_0^\infty\rho_D(t)\sum_\ell\max_a
       \left[\frac1n\sum_i|z_{\ell,a,i,D}|^2
                       \mathbf1_{\{|z_{\ell,a,i,D}|>R\}}\right]^{1/2}dt
 \le Ce^{-cR^2}+a'_n.
 \tag{51}
\]

No independence between a carrier and its preactivation is needed:
splitting the union in (47) gives
\(Z_n(M,R)\le Z_n(M)+(M/R)P_n(R)\). Hence \(R=M\) gives
\(Z_n(M,M)\le Ce^{-cM^2}+a_n+a'_n\), reducing the source to the same
form as (10).

If (51) is separately established and
\(\ell(R)\le C(1+R^\alpha)\) for some \(0\le\alpha<1\), choose
\(M\asymp\sqrt{\log(e+1/s)}\), where
\(s=q^{-2}+a_n+a'_n\). Equation (49) yields

\[
 D_n(q)\le Cs\exp\!\left(K[\log(e+1/s)]^{(1+\alpha)/2}\right).
 \tag{52}
\]

Indeed \(B=O(1+M^{1+\alpha})\), its logarithmic amplification is
\(o(\log q)\), and \(CBA/q\to0\) uniformly because \(s\ge q^{-2}\).
Polynomial factors in \(B\), \(T\), and \(M\) are absorbed by the
displayed exponential. The same decreasing-factor argument as for
\(\Phi\) separates (52) into a pure order term and a dense-only width
remainder. More generally \(\ell(R)=o(R)\) gives a
\(q^{-2+o(1)}\) order envelope under (51).

At the borderline linear growth, suppose the constants can be recorded
as \(A(M,M)\le C e^{K_1M^2}\), \(B(M,M)\le C(1+M^2)\), and the
mixed tail is at most \(Ce^{-c_1M^2}+a_n+a'_n\). If \(c_1>K_1\),
choose
\(M^2\sim\log(1/s)/(c_1+K_1)\). The source term has power
\(s^{(c_1-K_1)/(c_1+K_1)}\), the quadratic term has the same power
up to logarithms, and the absorption condition holds because
\(2K_1/(c_1+K_1)<1\). Consequently every

\[
 0<\gamma<\frac{2(c_1-K_1)}{c_1+K_1}
 \quad\text{has}\quad
 D_n(q)\le C_\gamma
       [q^{-\gamma}+(a_n+a'_n)^{\gamma/2}].
 \tag{53}
\]

Integer cutoff rounding creates only a subpower correction and is covered
by the strict inequality on \(\gamma\). This is a narrower quantitative
regime requiring an explicit competition between the tail and feedback
constants. Small labels may improve the feedback constant, but no such
constant comparison is assumed here. Faster local-modulus growth, or
\(c_1\le K_1\), is not resolved by this optimization; that is a limit
of (49), not an impossibility theorem for the closure.

## 8. Activation examples and exact scope

The global theorem covers fixed layer-dependent choices of softplus,
exact GELU, SiLU, and unit-coefficient ELU, as well as tanh and the other
bounded-slope/global-derivative-Lipschitz examples in
`ACTIVATION_EXTENSION.md`. Their hypotheses can be checked directly:

* Softplus has derivative \(\sigma\) and second derivative
  \(\sigma(1-\sigma)\), bounded by \(1/4\).
* Exact GELU \(x\Phi(x)\) has derivative
  \(\Phi(x)+x\varphi(x)\) and second derivative
  \((2-x^2)\varphi(x)\), both bounded.
* SiLU \(x\sigma(x)\) has derivative
  \(\sigma+x\sigma(1-\sigma)\) and second derivative
  \(2\sigma(1-\sigma)+x\sigma(1-\sigma)(1-2\sigma)\).
  Exponential decay of \(\sigma(1-\sigma)\) bounds both expressions.
* Unit ELU has continuous derivative \(e^x\) for \(x<0\) and \(1\)
  for \(x\ge0\); this derivative is globally one-Lipschitz. Its second
  derivative need not be continuous at zero for any step of the proof.

Fixed gains, offsets, and finite linear combinations preserve the global
regularity assumptions. The positive initial feature-Gram condition is
still an independent condition on the resulting activation/data pair.
The zero-readout assumption removes the backward prefix jump and is used
in Section 4; a nonzero-readout extension needs its separate jump term.
At \(Y=0\) both systems are stationary. At \(L=1\), no hidden block is
compressed and the dense and closure physical paths coincide.

The global theorem is complete **as an implication from the supplied
physical/activity and dense full-carrier tail inputs**. Proving (10) for
the activation class is a separate Gaussian/source task. The local-modulus
quantitative corollaries additionally require (51), which is not contained
in the supplied carrier-tail hypothesis. No population identification,
unique fixed-order limit, numerical width rate, or promotion claim is
hidden in these conclusions.

## 9. Scoped check of the coordinator's synthesis

The coordinator subsequently authorized the complete additional input
`ACTIVATION_NEAR_QUADRATIC_ALLTIME.md`, which was read in full. Its checked
snapshot has SHA-256

`30d0eb49d29e09fe372a9ac1c9dcf5b267c401f6d54d2c23846c14f967ae8207`.

The assignment for this check was the theorem and deterministic proof,
treating Section 4's Gaussian bridge as a separately supplied input pending
its source specialist's check. This was a scoped collaborator check, not
an isolated promotion review. No Gaussian construction, population-flow
identification, or numerical width claim was independently certified here.

The global activation class, full-carrier damping, top-readout clipping,
auxiliary derivative recurrence, closure-clock mismatch estimate, terminal
weighted energy, absolute-defect identity, quadratic absorption, and
all-order cutoff optimization agree with the proof above. The test-output
factor `1+||x||/sqrt(d)` correctly covers offsets and unbounded activation
values; the supplied initial first-matrix bound and finite second input
moment justify the displayed full-domain observation bound. Predictor
compactness is justified by the stronger details in Section 6 of this note.

Two presentation corrections were sent to the coordinator: replace the
new global finite RMS shorthand `||v||_n` by the explicit normalization
required by `docs/notation.qmd`, making the history normalization explicit
as well; and replace “constant unit prefix” by “constant prefix of clock
length one” so it cannot be read as an all-one feature vector. No
mathematical defect was found in the deterministic implication under the
supplied source assumptions. Subsequent edits have a different hash and
are not automatically covered by this frozen-snapshot record.
