# One gap factor in the Taylor source by physical gradient stability

2026-10-06. Scoped author derivation, conditional on the physical source,
fitting, and finite-source interfaces identified below. This is not an
independent check, promotion, or complete passive-decoder theorem. No
experiment or Git operation was performed.

The physical Taylor source admits the revised bounds
\[
\begin{split}
 R&\le C\{d+mL\beta^{200L}(1+m/\gamma)
                 Z^2\sqrt{\log(en)}\},\\
 K+b_\sigma+b_{\rm value}+b_{\rm work}
     &\le C\beta^{100L}Z,
\end{split}                                                     \tag{1}
\]
apart from the separately supplied input encodings and activation-evaluator
work. Its finite iid-packet implementation has sufficient local precision
\[
 p_{\rm loc}\le C\{\beta^{100L}Z+\log(1/\rho)\},
       \qquad 0<\rho<1/4.                                  \tag{2}
\]
The field count in (1) includes activation samples and jets; the matrix
count has the same bound. The original small-label allowance, physical
optimizer, scientific width gates, and horizon gate are unchanged.

The proof retains the original complex patch size, hence one factor
\(1+m/\gamma\) in the patch count. It removes the other factor from
the Taylor degree and all local precision requirements by using the
negative semidefinite part of the physical gradient Jacobian on real
time segments. Complex-time estimates are used only within one patch.

## 1. Model, inputs, and exact claim scope

For unit training inputs \(v_a=x_a/\sqrt d\), let
\[
 z_a^{(1)}=Av_a,\qquad
 z_a^{(j)}=W^{(j)}h_a^{(j-1)},\qquad
 h_a^{(j)}=\phi_j(z_a^{(j)}),\qquad
 f_a=w^\top h_a^{(L)}/n.
                                                               \tag{3}
\]
The loss is \(\mathcal L=m^{-1}\sum_a r_a^2\), where
\(r_a=f_a-y_a\). The readout starts at zero. All blocks train with
the original mobilities \((n,1,\ldots,1,n)\). The residual-free
backward variables and physical velocities are
\[
\begin{aligned}
 k_a^{(L)}&=w,&
 \delta_a^{(j)}&=\phi_j'(z_a^{(j)})\odot k_a^{(j)},&
 k_a^{(j)}&=W^{(j+1)\top}\delta_a^{(j+1)},\\
 \dot A&=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,&
 \dot W^{(j)}&=-\frac2{mn}\sum_a
               r_a\delta_a^{(j)}h_a^{(j-1)\top},&
 \dot w&=-\frac2m\sum_a r_a h_a^{(L)}.
\end{aligned}                                                   \tag{4}
\]

Preserve the source notation
\[
\begin{gathered}
 r=m/\gamma>0,\qquad Y=\|y\|_2/\sqrt m>0,\qquad
 S=16Yr\le1,\qquad \ell=\log(en),\qquad B=\beta^{100L},\\
 Z=(a_0+1)\ell+\log(e+B(1+r)(m+d+2)),\qquad 1\le a_0\le12.
\end{gathered}                                                  \tag{5}
\]
Here \(r\) is the inverse normalized gap, whereas \(r_a\) is a
sample residual. The envelope \(\beta\ge10\) includes the first
two activation derivatives on the half-strip and \(16/a\), where
\(a\) is the activation strip width. The zero-label branch retains
the exact zero predictor. On the nonzero branch retain \(Y\ge n^{-1}\),
\(r^{-1}\le\beta^{6L}\), and every other inherited scientific gate.

The learned displacement is
\(u=(A-A_0,W^{(2)}-W_0^{(2)},\ldots,W^{(L)}-W_0^{(L)},w)\).
The original source uses the block sum norm
\[
 \|u\|_\Sigma=\|A-A_0\|_F/\sqrt n+
       \sum_{j=2}^L\|W^{(j)}-W_0^{(j)}\|_F+\|w\|_2/\sqrt n.
                                                               \tag{6}
\]
The new stability argument also uses the Hilbert norm
\[
 \|u\|_{\mathcal H}^2=\|A-A_0\|_F^2/n+
       \sum_{j=2}^L\|W^{(j)}-W_0^{(j)}\|_F^2+\|w\|_2^2/n.
                                                               \tag{7}
\]
For \(c_L=\sqrt{L+1}\),
\(\|u\|_{\mathcal H}\le\|u\|_\Sigma\le c_L\|u\|_{\mathcal H}\).
These are two norms on the same physical state; neither changes the
optimizer. Normalize state and time by
\(\bar u(\tau)=u(r\tau)/Y\), and denote its exact field by
\(\overline F\).

The complete allowed scientific inputs read were
SANE_TAYLOR_SOURCE.md, FAST_TAYLOR_NOISE.md,
PHYSICAL_PARAMETER_ACCOUNTING.md, SANE_ADAPTIVE_TIME.md, and
FAST_FINITE_SOURCE_BRIDGE.md. The supervisor subsequently authorized
FAST_SCALAR_FORCING.md to close the current-operand pair interface; it
was read completely. No outside-study links, route notes, reviews, or
passive-decoder notes were read. The conjecture, proof, canonical-notation,
and neural-network convention instructions were applied. Physical
scientific events and the finite-source theorem's external coefficient
and Gaussian-law lemmas remain conditional inputs as stated in these
files; they are not reconstructed here.

Use exactly the source horizon, tube, and equal patch partition:
\[
\begin{gathered}
 T=2\{a_0\log n+\log(1+66Br)\}<32\ell,\qquad
 r_\tau^{-1}\le B\sqrt\ell,\\
 q(\tau)=2^{-\lfloor\tau/4\rfloor},\qquad q_j=q(\tau_j),
 \qquad q_T=q(T),\qquad
 d_n=\frac{\beta^{-200L}q_T}{(1+r)^2\sqrt n},\\
 h=\min\{1/8,r_\tau/8,[64B(1+r)\sqrt\ell]^{-1}\},\qquad
 h_j=T/H\in[h/3,h],\\
 M=B(1+r),\qquad
 \Lambda_j=B(1+r)(1+q_j\sqrt\ell).
\end{gathered}                                                  \tag{8}
\]
The certified-ceiling convention for \(H\) is that of the noisy
Taylor source. In particular
\[
 H\le CB(1+r)Z\sqrt\ell,\qquad
 4h_j\Lambda_j\le1/8,\qquad
 \sum_j h_jq_j\le9,\qquad \log(d_n^{-1})\le CZ.             \tag{9}
\]
The unclipped field is holomorphic and \(\Lambda_j\)-Lipschitz in
the complex sum-norm tube of radius \(d_n\) about each reference
complex patch. Its reference derivative has sum norm at most \(M\).
Prediction is \(B\)-Lipschitz in the physical sum norm, uniformly
over real unit queries. These are the inherited source interfaces.

## 2. A real stability lemma on the entire numerical tube

Use Euclidean physical coordinates
\[
 p=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n).
                                                               \tag{10}
\]
The Euclidean displacement norm in these coordinates is exactly (7).
For \(g_a=\nabla_p f_a\), its block formulas are
\[
 g_a^{(1)}=\delta_a^{(1)}v_a^\top/\sqrt n,\qquad
 g_a^{(j)}=\delta_a^{(j)}h_a^{(j-1)\top}/n,
 \qquad g_a^{(L+1)}=h_a^{(L)}/\sqrt n.                      \tag{11}
\]
Substitution in (4) gives the exact identity
\[
 \dot p=-\nabla_p\mathcal L=-\frac2m\sum_a r_a g_a.
                                                               \tag{12}
\]
Thus the mobility factors have all been included.

**Lemma.** At every real point of the sum-norm tube in (8), and on
every real line segment contained in that tube, the normalized field
obeys
\[
 \langle v,D\overline F\,v\rangle_{\mathcal H}
       \le\mu_j\|v\|_{\mathcal H}^2,
 \qquad \mu_j=\beta^{80L}q_j(1+S\sqrt\ell).
                                                               \tag{13}
\]
Consequently its total real expansion allowance is
\[
 E_+:=9\beta^{80L}(1+S\sqrt\ell),\qquad
 \sum_jh_j\mu_j\le E_+\le C B\sqrt\ell.                  \tag{14}
\]

Here the tube is around the true trajectory, not merely the reference
trajectory itself. To verify this distinction, source forward subtraction
and (8) give, for every real point of the tube,
\[
 \|r(p)\|_2/\sqrt m\le2Yq_j+\beta^{8L}Yd_n\le3Yq_j.
                                                               \tag{15}
\]
The source tube argument also supplies operator caps eleven, feature RMS
at most \(\beta^{4L}\), backward RMS at most
\(\beta^{8L}S\), and carrier maximum at most
\(2\beta^{40L}S\sqrt\ell\), with exponent slack. We next verify
the needed output Hessian bound on these same points.

For a physical direction \(e\), differentiate the forward pass:
\[
\begin{split}
 Dz_a^{(1)}[e]&=e_Av_a,\\
 Dz_a^{(j)}[e]&=e_{W^{(j)}}h_a^{(j-1)}
       +W^{(j)}\{\phi_{j-1}'(z_a^{(j-1)})
                           \odot Dz_a^{(j-1)}[e]\},\\
 Dh_a^{(j)}[e]&=\phi_j'(z_a^{(j)})\odot Dz_a^{(j)}[e].
\end{split}                                                     \tag{16}
\]
The stated operator, feature, and derivative bounds imply
\(\|Dz_a^{(j)}[e]\|_{2,n}\le\beta^{8L}\|e\|_\Sigma\)
and \(\|Dh_a^{(j)}[e]\|_{2,n}\le\beta^{9L}\|e\|_\Sigma\).
For example, each matrix-direction term contributes at most
\(\beta^{4L}\|e_{W^{(j)}}\|_F\); subsequent propagation multiplies
by at most \((11\beta)^L\le\beta^{3L}\). Summing the direction
block norms is already paid by \(\|e\|_\Sigma\), and the remaining
fixed factors fit the displayed powers eight and nine.

Differentiate the backward pass at this same point:
\[
\begin{split}
 Dk_a^{(L)}[e]&=e_w,\\
 Dk_a^{(j)}[e]&=e_{W^{(j+1)}}^\top\delta_a^{(j+1)}
                         +W^{(j+1)\top}D\delta_a^{(j+1)}[e],\\
 D\delta_a^{(j)}[e]&=\phi_j'(z_a^{(j)})\odot Dk_a^{(j)}[e]
       +\phi_j''(z_a^{(j)})\odot Dz_a^{(j)}[e]\odot k_a^{(j)}.
\end{split}                                                     \tag{17}
\]
The gate term in the last line has RMS at most
\(2\beta^{40L+1}S\sqrt\ell\,
\|Dz_a^{(j)}[e]\|_{2,n}\). Only this term uses a carrier maximum.
Unrolling the linear downward recursion multiplies its coefficients
by at most \((11\beta)^L\le\beta^{3L}\), and there are at most
\(L+1\) additive terms. Together with the backward RMS bound this
gives
\[
 \max_j\|D\delta_a^{(j)}[e]\|_{2,n}
       \le\beta^{55L}(1+S\sqrt\ell)\|e\|_\Sigma.
                                                               \tag{18}
\]
It does not multiply a carrier maximum once per layer.

Differentiate (11). In a hidden block its Frobenius norm is at most
\[
 \|D\delta_a^{(j)}[e]\|_{2,n}\|h_a^{(j-1)}\|_{2,n}
   +\|\delta_a^{(j)}\|_{2,n}\|Dh_a^{(j-1)}[e]\|_{2,n}.
                                                               \tag{19}
\]
The first and readout blocks are bounded respectively by
\(\|D\delta_a^{(1)}[e]\|_{2,n}\) and
\(\|Dh_a^{(L)}[e]\|_{2,n}\). Sum the block bounds, use
\(\|e\|_\Sigma\le c_L\|e\|_{\mathcal H}\), and absorb
\((L+1)c_L\) in the slack up to exponent seventy. Therefore
\[
 \|D_p^2 f_a\|_{\mathcal H\to\mathcal H}
          \le\beta^{70L}(1+S\sqrt\ell)                   \tag{20}
\]
at every real point of the tube.

Since \(p=p_0+Y\bar p\) and \(\tau=t/r\), differentiation of
the normalized field multiplies the physical Jacobian by \(r\),
not \(r/Y\). Equation (12) yields
\[
 D\overline F=-\frac{2r}{m}\sum_a
                  \{g_a g_a^\top+r_aD_p^2 f_a\}.
                                                               \tag{21}
\]
For real \(v\), the first quadratic form is
\(-2r m^{-1}\sum_a(g_a^\top v)^2\le0\). For the second use
(15), (20), and Cauchy--Schwarz in the sample index:
\[
 \langle v,D\overline Fv\rangle_{\mathcal H}
 \le6rYq_j\beta^{70L}(1+S\sqrt\ell)\|v\|_{\mathcal H}^2
 \le\mu_j\|v\|_{\mathcal H}^2.                            \tag{22}
\]
The last step uses only \(rY\le1/16\), the original label
allowance. Equations (9) and (22) prove (13)--(14).

Integrating (13) along a real line segment also gives
\[
 \langle U-V,\overline F(U)-\overline F(V)\rangle_{\mathcal H}
       \le\mu_j\|U-V\|_{\mathcal H}^2.                   \tag{23}
\]
No negative quadratic-form assertion is made in complex time: algebraic
transpose is not a Hermitian Gram there.

## 3. Taylor propagation with separate real and complex estimates

Retain all noise/interpolation/local-arithmetic constructions of the noisy
Taylor source and scalar-forcing note. In one patch they define a
holomorphic auxiliary field \(\overline F_j^{\rm num}\) whose fixed
forcing polynomials have real coefficients. For
\[
 \delta\le\delta_0:={\beta^{-150L}S q_T\over(1+r)^2\sqrt n},
 \qquad C_N=B^2(1+r)^2\sqrt\ell,\qquad \eta=C_N\delta,
                                                               \tag{24}
\]
their supplied estimates, with fixed fractions allocated among defects,
are
\[
 \|\overline F_j^{\rm num}-\overline F\|_\Sigma\le\eta,
 \qquad \|D\overline F_j^{\rm num}\|_{\Sigma\to\Sigma}
          \le2\Lambda_j.
                                                               \tag{25}
\]
This includes current-operand scalar-pair and residual defects. Centers
and forcing polynomials are held fixed in this local field comparison.

Let \(e_j\) be the starting normalized error in Hilbert norm, with
\(c_Le_j\le d_n/8\). If \(4h_j\eta\le d_n/16\), the source's
complex contraction proof gives exact and perturbed local solutions
\(X_a(z),X_b^{\rm num}(z)\) on \(|z|<4h_j\). Their difference
\(D(z)\) satisfies
\[
 \|D(z)\|_\Sigma\le
       (c_Le_j+|z|\eta)e^{\Lambda_j|z|}
       \le2c_Le_j+8h_j\eta.                              \tag{26}
\]
Thus both solutions stay in the same tube used in the lemma. The existing
complex patch length and contraction have not been enlarged.

On the real segment, (23) and (25) give
\[
 \frac12\frac{d}{ds}\|D(s)\|_{\mathcal H}^2
       \le\mu_j\|D(s)\|_{\mathcal H}^2+
                           \eta\|D(s)\|_{\mathcal H}.
\]
Apply this inequality first to
\(\sqrt{\|D\|_{\mathcal H}^2+\varepsilon^2}\), and then send
\(\varepsilon\downarrow0\). Integration yields
\[
 \|D(s)\|_{\mathcal H}\le(e_j+s\eta)e^{\mu_js},
                      \qquad 0\le s\le h_j.               \tag{27}
\]
Only the exact field needs a one-sided estimate; the noisy field itself
need not be a gradient.

The coefficient recurrence computes the first \(K+1\) coefficients
of \(X_b^{\rm num}\), as in the source. On \(|z|=2h_j\), (26)
and Cauchy's coefficient formula bound the difference-series tail at
every \(s\le h_j\) by
\((2c_Le_j+8h_j\eta)2^{-K}\). The exact source tail is at most
\(2Mh_j2^{-K}\). Since \(\mu_j\le\Lambda_j\),
\(h_j\mu_j\le1/32\). For \(K\ge4\), the committed error obeys
\[
 e_{j+1}\le
       (1+2h_j\mu_j+2c_L2^{-K})e_j
                    +3h_j\eta+2Mh_j2^{-K}.               \tag{28}
\]
Independent endpoint rounding adds its allocated \(h_j\eta\) term;
it is not represented as a constant forcing that leaves the same
polynomial unchanged. A fixed increase in the coefficient three covers
all such allocations. Interior times have the same estimate with their
actual local real time.

The norm conversion \(c_L\) occurs only in the exponentially small
Taylor tail in (28). It is not a fixed multiplier incurred at each
patch. The products of the multipliers in (28) are bounded by
\[
 \exp(2E_++2c_LH2^{-K}).                                 \tag{29}
\]

## 4. Explicit degree and all physical local precisions

Set
\[
 \epsilon=\min\{d_n/(2^{12}c_L),
                         n^{-a_0}/(2^{12}Bc_L)\},
                                                               \tag{30}
\]
\[
 K=8+\left\lceil
 {4E_++\log[2^{20}(c_L+1)(M+1)(T+1)/\epsilon]
                    +\log(1+16c_LH)\over\log2}\right\rceil,
                                                               \tag{31}
\]
\[
 \delta=\min\left\{\delta_0,
        {\epsilon e^{-4E_+-10}\over2^{20}C_N(T+1)}\right\}.
                                                               \tag{32}
\]
With the zero initial displacement, let \(\widetilde u\) denote the
computed normalized displacement. Equations (28)--(32) and their interior
versions give
\[
 \sup_{0\le\tau\le T}
       \|\widetilde u(\tau)-\bar u(\tau)\|_{\mathcal H}
                      <\epsilon/8.                       \tag{33}
\]
For verification, (31) makes \(2c_LH2^{-K}<1\), so the global
bound is a numerical multiple of
\((T+1)[\eta+(M+1)2^{-K}]e^{2E_++1}\); substitution of (31)--(32)
makes this smaller than \(\epsilon/8\). Their large fixed constants
also leave room for the endpoint rounding just discussed. Multiplication
by \(c_L\) closes every sum-norm anchor and complex-tube assumption.
Uniform prediction subtraction, followed by the inherited tail after
freezing at \(T\), gives normalized all-time whole-sphere error less
than \(n^{-a_0}\), including the fitted endpoint of the dense flow.

The logarithmic costs do not conceal an inverse-gap factor. In fact
\[
 \log\epsilon^{-1}+\log\delta_0^{-1}+\log(M+1)
       +\log(C_N+1)+\log(H+1)\le CZ.                     \tag{34}
\]
The only potentially small label factor is \(S\) in \(\delta_0\).
The already required gates give
\(S=16Yr\ge16\beta^{-6L}/n\), which proves its contribution to
(34). All appearances of \(1+r\) in (34) are logarithms. Therefore
\[
 K+\log\delta^{-1}\le C\{E_++Z\}\le CBZ.                \tag{35}
\]

For matrix-answer noise keep the identical analytic-forcing construction
and take
\[
 \sigma=2^{-b_\sigma},\qquad
 b_\sigma=\left\lceil2K+\log_2(4/\delta)\right\rceil.
                                                               \tag{36}
\]
For activation values keep the same centered real interpolation, with
degree parameter \(J\) and sample tolerance \(\nu\) chosen as
\[
 J\ge\max\{K+2,\lceil\log_2(C\beta^2/\delta)\rceil\},
 \qquad \nu\le\delta/(C\beta^2 5^J).                     \tag{37}
\]
Write \(b_{\rm value}=\lceil\log_2(\nu^{-1})\rceil\).
The least choices obey \(J\le CK\) and
\(J+\log\nu^{-1}+b_\sigma\le CBZ\). In particular the real-value
interface, its continuous extension where needed, and its sample count
remain charged. The unchanged short complex patches preserve the
activation-disk and centered-power arguments of the source.

For physical coefficient arithmetic, the source's sufficient tolerance
has the form
\[
 \rho_{\rm arith}\le
 {\delta\over C4^K(n+1)^3[B(1+r)(R+K+1)]^C}.
                                                               \tag{38}
\]
Its logarithmic inverse is \(O(BZ)\). Substitution in the source's
local working-precision bound gives \(b_{\rm work}\le CBZ\),
besides the given input descriptions. No inverse final-step length is
unaccounted for, since the same equal-patch construction gives
\(h_j^{-1}\le CB(1+r)\sqrt\ell\).

For scalar pairs use precisely the current-operand specification and
actual stored rank-list interpretation of FAST_SCALAR_FORCING.md.
Its local defect calculation has no global stability exponent: with
\(N_{\rm sum}\le C(R+K+1)^3\) and its local magnitude/guard bound
\(A\), the analytic coefficient defect is at most
\(C4^K N_{\rm sum}^2A^8\epsilon_{\rm pair}\). The explicit
quantities defining \(A\) are polynomial scales in
\(n,B,1+r,R,K,h_{\min}^{-1},Y^{-1}\), guard-margin reciprocals,
and interpolation scratch of size \(e^{CJ}\). The new choices thus
give \(\log A\le CBZ\). Choose
\[
 \epsilon_{\rm pair}\le
       {\delta\over C4^K N_{\rm sum}^2A^{10}}.
                                                               \tag{39}
\]
Its logarithmic inverse is \(O(BZ)\). Residual-pair defects are
measured after division by \(Y\), as in that note; \(Y^{-1}\le n\)
pays that conversion once. The residual and carrier bounds needed in
(15)--(20) apply to the exact physical field at the perturbed parameters;
the extra scalar residual error is included separately in (25).

The scalar-forcing proof's causal prefix completion and strict-slack guard
argument use only the local complex contraction, coefficient bounds,
and certified endpoint error. These remain valid in (26)--(33).
There is no new residual projection or clipping operation in the field.
Thus (39) covers all its physical scalar pairs, learned-rank actions,
readout/residual reductions, and strict-slack cap tests at the new
precision. The old global \(E\) in that note is replaced exactly at
its endpoint-propagation step by \(E_+\); it is not left inside a cap.

Finally, the chronology still has \(O(mLHK)\) principal fields and
initialized actions, and \(O(mLHJ)=O(mLHK)\) scalar sample/jet
fields if they are named. Using (9) and (35) proves (1). The
\(O(mLHK^2)\) stored scalar rank weights, activation arithmetic,
and primitive evaluator work remain separately charged as before.

## 5. Transfer to the finite iid-packet source

This section is conditional on exactly the finite-source bridge's
protected coefficient, Gaussian-law, sampler, and finite-arithmetic
interfaces. It verifies their parameter substitution; it does not
independently re-prove those external lemmas.

Replace the bridge's physical source inputs by (8), (24), and
(30)--(39), and define
\(\chi_+=BZ\). The physical answer, pair, and local coefficient
tolerances all have logarithmic reciprocals at most \(C\chi_+\).
The physical query/raw-answer RMS cap remains a fixed polynomial in
\(B,1+r\), and the noise satisfies \(\log\sigma^{-1}\le C\chi_+\).
Also \(\log(e+n+R)\le C Z\).

In the notation of FAST_FINITE_SOURCE_BRIDGE.md, its one-call coefficient
scale is \(z=C(2+R+b+\sigma^{-1})\), and its elementary local
amplification is \(\mathcal M=(n+1)z^{120}\). Thus
\(\log z+\log\mathcal M\le C\chi_+\). The bridge's one-call
Gaussian-law bound remains
\[
 \kappa\le z^{230}\{\sqrt n\,e_c+n\eta_{\rm acq}^2\},
                                                               \tag{40}
\]
where \(e_c\) is its moment/coefficient input error and
\(\eta_{\rm acq}\) its scalar acquisition noise scale. This
\(\eta_{\rm acq}\) is distinct from the physical forcing amplitude
\(\eta\) in (24).

The bridge chooses a tolerance
\(\xi_0=\rho/[2^{20}(R+1)(n+1)z^{240}]\), then dyadic acquisition,
answer, coefficient, innovation, and finite-sampler tolerances using a
fixed number of products and minima. Its scalar-mark and rounding-boundary
condition likewise uses only \(P\le CR^2\), the two grid spacings,
and \(\rho\). Their logarithmic costs are consequently at most
\(C[\chi_++\log(1/\rho)]\). The Gaussian tail cutoff has square
\(O(\log(n(d+R)+P+1)+\log(1/\rho))\), so the finite sampler has
the same precision bound.

One old global exponent occurs separately in the bridge's first-layer
root coupling and must also be changed. Require the initial Hilbert
error to be at most
\[
 e_0\le\epsilon e^{-4E_+-10}/2^{20},\qquad
 \epsilon_G\le Y\epsilon e^{-4E_+-10}/[2^{20}(\sqrt d+1)].
                                                               \tag{41}
\]
The second inequality implies the first, because the normalized
first-layer error is at most \(\sqrt d\epsilon_G/Y\).
Iteration of (28) starting at this nonzero \(e_0\) preserves (33).
Equation (41) costs \(C\chi_+\) bits, using \(Y^{-1}\le n\).
The original Gaussian scientific initialization is thereby preserved in
the coupling.

These substitutions prove (2) within the inherited finite-source
interfaces. They keep the same iid finite packets, finite marks,
observable chronology, and conditional Gaussian augmentation. The
stopped coupling's failure bound is unchanged in form:
\[
 \Pr(\text{inherited scientific failure})+Re^{-cn}+\rho,
                                                               \tag{42}
\]
with the revised \(R\). No global sensitivity bound for an expanded
row-history function is asserted or needed for this substitution.

## 6. Consequences and precise remaining boundary

The two-sided complex Jacobian bound remains
\(\Lambda_j=B(1+r)(1+q_j\sqrt\ell)\), so (1) retains one
algebraic gap factor in \(H\). Trying to remove it by applying
(13) on a complex disk would be invalid. The present result also does
not remove the polynomial \((1+r)^2\) in the local defect conversion
\(C_N\); only its logarithm enters finite precision, which is why
that factor causes no algebraic gap cost in (2).

The finite-source bridge's acquisition base is \(O(R^2p_{\rm loc})\)
bits, conditional on its metric-acquisition interface. For fixed
confidence this bound now has algebraic inverse-gap degree two in
the displayed source/acquisition terms, plus the explicitly retained
logarithms in \(Z\). Previously the same expression used gap degree
five. This algebraic consequence concerns that acquisition base only.
Any independent downstream use of the old physical source precision or
field count must be substituted and checked explicitly; no complete
passive decoder, seed bound, or query-work theorem follows here.

The result is a positive refinement of this source witness, conditional
on its scientific events and finite-source interfaces. Its smallest
remaining local verification is an independent check of the real-tube
Hessian estimate, separation of real and complex stability in (28), and
the changed tolerance choices. The stochastic source-width theorem,
arbitrary-activation evaluator complexity, and full passive-decoder
requirements are unchanged external limitations.

In particular the inherited deterministic width gate in
PHYSICAL_PARAMETER_ACCOUNTING.md (28) is still in force: it lower-bounds
\(\sqrt{\log(en)}\) by a parameter-dependent multiple of the physical
source radius coefficient. It can therefore entail exponential width in
the inverse gap. No new width gate is used to prove (1)--(2), but this
numerical refinement does not turn the inherited scientific event into a
polynomial-width theorem.

### Frozen input hashes

| Input | SHA-256 |
|---|---|
| FAST_TAYLOR_NOISE.md | `71c67ce4de343077f3795aa9a9892052560da7b7ab51a59f6609027744c8881c` |
| SANE_TAYLOR_SOURCE.md | `24b8d368da31e9d8bf00bb1c7fc85f75cb0efcc30a9cbc8409ac9c520bb916af` |
| PHYSICAL_PARAMETER_ACCOUNTING.md | `395301fcca55af8937281f22b56c3ffe366d8e46fe7b4b12aeec35e5ca462279` |
| SANE_ADAPTIVE_TIME.md | `adb3aca056819e7276e82e6c18b969fd0f67cbe1fdb56c290c929a9a8b4f2d9f` |
| FAST_FINITE_SOURCE_BRIDGE.md | `7ef69972a213fb26b77cd1c0ed4dcbd8b7d12f9e3b06906f351f7443f79894e6` |
| FAST_SCALAR_FORCING.md | `6b74c2a49046bdce4d30b0bf46535ddbc6498332b91fb3d516fefb0bd09f23bb` |
