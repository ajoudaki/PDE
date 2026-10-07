# Reconstruction of the physical gap-degree refinement

2026-10-06. Bounded source check of the frozen
`GAP_DEGREE_REFINEMENT.md`. This is not a promotion review, a reconstruction
of the external scientific source event, or a complete passive-decoder
theorem. No experiment, web access, Git operation, or unassigned scientific
input was used. Only this report was written.

**Verdict: the refinement passes within its stated conditional interfaces.**
The real physical gradient structure removes the algebraic factor
\(G=1+m/\gamma\) from Taylor degree and local physical/coupling precision.
The unchanged complex patch length retains one factor \(G\) in the field
count. I found no missing width or sample factor in the output Hessian,
no repeated norm-conversion loss, and no surviving old global stability
exponent in the stated local choices. Below I supply the additional
\(K\le CH\) calculation needed for the row-work and cache bounds.

This conclusion preserves every inherited scientific width, probability,
label, activation, and horizon condition. The coefficient, Gaussian-law,
finite-arithmetic, sampler-work, and metric-acquisition interfaces that the
finite-source bridge takes from outside the allowed inputs remain
conditional here. Their parameter substitution is checked; their original
proofs have not been imported or independently certified.

## 1. Frozen inputs and precise target

All six authorized inputs were read completely. Their SHA-256 hashes are:

| Input | SHA-256 |
|---|---|
| GAP_DEGREE_REFINEMENT.md | `78e209842b99ac054659bf32a2dd9e77ed9fef26af6047d209312152aa619875` |
| FAST_TAYLOR_NOISE.md | `71c67ce4de343077f3795aa9a9892052560da7b7ab51a59f6609027744c8881c` |
| SANE_TAYLOR_SOURCE.md | `24b8d368da31e9d8bf00bb1c7fc85f75cb0efcc30a9cbc8409ac9c520bb916af` |
| PHYSICAL_PARAMETER_ACCOUNTING.md | `395301fcca55af8937281f22b56c3ffe366d8e46fe7b4b12aeec35e5ca462279` |
| FAST_SCALAR_FORCING.md | `6b74c2a49046bdce4d30b0bf46535ddbc6498332b91fb3d516fefb0bd09f23bb` |
| FAST_FINITE_SOURCE_BRIDGE.md | `7ef69972a213fb26b77cd1c0ed4dcbd8b7d12f9e3b06906f351f7443f79894e6` |

In particular, the candidate matches the supervisor's frozen hash. Its
additional listed `SANE_ADAPTIVE_TIME.md` was not an input to this check.
No link to another study, earlier review, or route note was followed. The
research, rigorous-proof, canonical-notation and neural-network convention
instructions, including the research adversarial-audit reference, were
applied.

Use the candidate's model with unit training inputs \(v_a\in\mathbb R^d\),
\(a=1,\ldots,m\), width \(n\), and \(L\) hidden layers:
\[
 z_a^{(1)}=Av_a,\qquad z_a^{(j)}=W^{(j)}h_a^{(j-1)},
 \qquad h_a^{(j)}=\phi_j(z_a^{(j)}),
 \qquad f_a=\frac{w^\top h_a^{(L)}}n.
\]
Here \(A\in\mathbb R^{n\times d}\), hidden matrices have size
\(n\times n\), and \(w\in\mathbb R^n\). The residual is
\(r_a=f_a-y_a\), and the loss is
\(\mathcal L=m^{-1}\sum_a r_a^2\). The physical mobilities are
\((n,1,\ldots,1,n)\), with initially zero readout. Define
\[
 \begin{gathered}
 r=m/\gamma,\quad G=1+r,\quad Y=\|y\|_2/\sqrt m>0,
 \quad S=16Yr\le1,\quad \ell=\log(en),\quad B=\beta^{100L},\\
 Z=(a_0+1)\ell+\log(e+BG(m+d+2)),\qquad 1\le a_0\le12.
 \end{gathered}
\]
The scalar \(r\) is not the residual \(r_a\). The source has
\(\beta\ge10\), \(L\ge2\), \(Y\ge n^{-1}\), and
\(r^{-1}\le\beta^{6L}\); \(\beta\) includes the first two activation
derivative bounds and \(16/a\), where \(a\) is the strip width.
The zero-label branch remains exactly zero.

The learned displacement \(u\) has norms
\[
 \begin{split}
 \|u\|_\Sigma&=\|A-A_0\|_F/\sqrt n+
  \sum_{j=2}^L\|W^{(j)}-W_0^{(j)}\|_F+\|w\|_2/\sqrt n,\\
 \|u\|_{\mathcal H}^2&=\|A-A_0\|_F^2/n+
  \sum_{j=2}^L\|W^{(j)}-W_0^{(j)}\|_F^2+\|w\|_2^2/n.
 \end{split}
\]
For \(c_L=\sqrt{L+1}\),
\(\|u\|_{\mathcal H}\le\|u\|_\Sigma\le c_L\|u\|_{\mathcal H}\).
Normalized state and time are \(\bar u(\tau)=u(r\tau)/Y\).

The claim being checked is
\[
 R\le C\{d+mLB^2GZ^2\sqrt\ell\},\qquad
 K+b_\sigma+b_{\rm value}+b_{\rm work}\le CBZ,
\]
and, within the finite-source interfaces,
\[
 p_{\rm loc}\le C\{BZ+\log(1/\rho)\},\qquad 0<\rho<1/4.
\]
Here \(R\) bounds actual principal fields and initialized actions,
including activation samples/jets when they are named. Input descriptions,
activation evaluator work, and the separate scalar-storage/work terms
are still charged.

## 2. Exact gradient coordinates and the tube Hessian

Introduce Euclidean coordinates
\[
 p=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n).
\]
This map is an isometry from physical displacements with norm
\(\|\cdot\|_{\mathcal H}\) to ordinary Euclidean/Frobenius block
coordinates. In all Hessian statements below, a direction in \(p\)
coordinates is measured in that ordinary Euclidean norm. Equivalently,
its corresponding physical direction is measured in
\(\|\cdot\|_{\mathcal H}\). This interpretation prevents applying
the factors \(n^{-1/2}\) twice to the candidate's Hessian notation.

Let the residual-free backward variables be
\[
 k_a^{(L)}=w,\qquad
 \delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot k_a^{(j)},\qquad
 k_a^{(j)}=W^{(j+1)\top}\delta_a^{(j+1)}.
\]
Direct differentiation, including the factors from changing coordinates,
gives
\[
 g_a:=\nabla_p f_a=left(
 \frac{\delta_a^{(1)}v_a^\top}{\sqrt n},\quad
 \left(\frac{\delta_a^{(j)}h_a^{(j-1)\top}}n\right)_{j=2}^L,
 \quad\frac{h_a^{(L)}}{\sqrt n}\right).
\]
The actual physical velocities therefore satisfy exactly
\[
 \dot p=-\frac2m\sum_a r_a g_a=-\nabla_p\mathcal L.
\]
Thus this is the given optimizer, with every mobility retained.
Writing \(p=p_0+Y\bar p\) and \(\tau=t/r\), the chain rule gives
\[
 D_{\bar p}\overline F
 =-\frac{2r}{m}\sum_a
   \left(g_ag_a^\top+r_aD_p^2f_a\right).                 \tag{1}
\]
The factor is \(r\), since differentiation of the input supplies the
factor \(Y\) that cancels the field's normalization \(1/Y\).

Use the original complex tube, centered at the true complex trajectory:
\[
 q_j=2^{-\lfloor\tau_j/4\rfloor},\qquad
 q_T=2^{-\lfloor T/4\rfloor},\qquad
 d_n=\frac{\beta^{-200L}q_T}{G^2\sqrt n}.
\]
A normalized sum-norm radius \(d_n\) is a physical radius \(Yd_n\).
The complete tube construction in `SANE_TAYLOR_SOURCE.md` §2 gives
operator cap eleven, feature RMS at most \(\beta^{4L}\), backward
RMS at most \(\beta^{8L}S\), and carrier maximum at most
\(2\beta^{40L}S\sqrt\ell\) throughout the tube. These are bounds
at nearby parameters, not just at the reference trajectory. In particular,
its backward subtraction compares changed gates to reference carriers,
then uses \(r^{-1}\le\beta^{6L}\) to pay for division by \(S\).

Write \(r(p)=(f_a(p)-y_a)_{a=1}^m\) for the residual vector at a
parameter point; the argument distinguishes it from the scalar \(r\).
The reference residual has RMS at most \(2Yq_j\). Uniform prediction
subtraction at the same tube point gives
\[
 \frac{\|r(p)\|_2}{\sqrt m}
 \le2Yq_j+\beta^{8L}Yd_n\le3Yq_j.                       \tag{2}
\]
Here \(q_T\le q_j\), so the second inequality does not weaken at
late patches. No sample-maximum estimate is substituted for the RMS.

For a physical direction \(e\), differentiating the forward pass gives
\[
 \begin{split}
 Dz_a^{(1)}[e]&=e_Av_a,\\
 Dz_a^{(j)}[e]&=e_{W^{(j)}}h_a^{(j-1)}
       +W^{(j)}\bigl(\phi_{j-1}'(z_a^{(j-1)})
                         \odot Dz_a^{(j-1)}[e]\bigr),\\
 Dh_a^{(j)}[e]&=\phi_j'(z_a^{(j)})\odot Dz_a^{(j)}[e].
 \end{split}
\]
With \(\|v\|_{2,n}=\|v\|_2/\sqrt n\), each matrix-direction
term has RMS at most \(\beta^{4L}\|e_{W^{(j)}}\|_F\).
The first term has RMS at most \(\|e_A\|_F/\sqrt n\).
Propagation costs at most \((11\beta)^L\le\beta^{3L}\);
the additive direction sizes are already summed in \(\|e\|_\Sigma\).
Consequently the deliberately loose bounds
\[
 \|Dz_a^{(j)}[e]\|_{2,n}\le\beta^{8L}\|e\|_\Sigma,
 \qquad
 \|Dh_a^{(j)}[e]\|_{2,n}\le\beta^{9L}\|e\|_\Sigma
                                                               \tag{3}
\]
hold on the whole real tube.

For the backward derivatives,
\[
 \begin{split}
 Dk_a^{(L)}[e]&=e_w,\\
 Dk_a^{(j)}[e]&=e_{W^{(j+1)}}^\top\delta_a^{(j+1)}
                  +W^{(j+1)\top}D\delta_a^{(j+1)}[e],\\
 D\delta_a^{(j)}[e]&=\phi_j'(z_a^{(j)})\odot Dk_a^{(j)}[e]
   +\phi_j''(z_a^{(j)})\odot Dz_a^{(j)}[e]\odot k_a^{(j)}.
 \end{split}
\]
The last term is bounded by
\(2\beta^{40L+1}S\sqrt\ell\,
\|Dz_a^{(j)}[e]\|_{2,n}\). The carrier maximum multiplies
this inhomogeneous term once. The remaining downward recursion is linear
with operator factors at most \(11\beta\). Unrolling and using (3)
therefore gives
\[
 \max_j\|D\delta_a^{(j)}[e]\|_{2,n}
 \le\beta^{55L}(1+S\sqrt\ell)\|e\|_\Sigma.               \tag{4}
\]
In particular it does not cost \(n^{1/2}\) or a carrier maximum to
the power \(L\).

Differentiate the gradient blocks. The hidden block's Frobenius norm is
at most
\[
 \|D\delta_a^{(j)}[e]\|_{2,n}\|h_a^{(j-1)}\|_{2,n}
 +\|\delta_a^{(j)}\|_{2,n}\|Dh_a^{(j-1)}[e]\|_{2,n}.
\]
The first and last blocks have norms at most
\(\|D\delta_a^{(1)}[e]\|_{2,n}\) and
\(\|Dh_a^{(L)}[e]\|_{2,n}\), respectively. The factors
\(1/n\) and \(1/\sqrt n\) in the gradient are essential here.
Summing the blocks and using
\(\|e\|_\Sigma\le c_L\|e\|_{\mathcal H}\) proves
\[
 \|D_p^2f_a\|_{2\to2}
 \le\beta^{70L}(1+S\sqrt\ell).                          \tag{5}
\]
The slack from exponent 59 to 70 covers all layer sums and the single
factor \(c_L\). This is an output Hessian bound independent of both
\(n\) and \(m\), apart from the explicitly displayed \(\sqrt\ell\).

For a real Euclidean direction \(v\), (1)'s Gram contribution is
\(-2r m^{-1}\sum_a(g_a^\top v)^2\le0\). The other term is bounded
using (2), (5), and
\(m^{-1}\sum_a|r_a|\le(m^{-1}\sum_a|r_a|^2)^{1/2}\). Thus
\[
 \langle v,D\overline Fv\rangle
 \le6rYq_j\beta^{70L}(1+S\sqrt\ell)\|v\|_2^2
 \le\mu_j\|v\|_2^2,
 \qquad\mu_j=\beta^{80L}q_j(1+S\sqrt\ell).               \tag{6}
\]
Only the existing \(rY\le1/16\) was used. In physical coordinates
this is the candidate's Hilbert-norm assertion. The tube ball at each
fixed real time is convex, so integrating (6) on the segment between
two points in that ball gives the corresponding one-sided difference
estimate. It is not necessary for the union of tube balls to be convex.

## 3. Local complex existence and real propagation are separate

Retain
\[
 \begin{gathered}
 T=2\{a_0\log n+\log(1+66Br)\}<32\ell,\qquad
 h=\min\{1/8,r_\tau/8,(64BG\sqrt\ell)^{-1}\},\\
 h_j=T/H\in[h/3,h],\quad
 \Lambda_j=BG(1+q_j\sqrt\ell),\quad M=BG.
 \end{gathered}
\]
The inherited complex estimates are
\(4h_j\Lambda_j\le1/8\), \(\sum_jh_jq_j\le9\), and
\(H\le CBGZ\sqrt\ell\). Hence
\[
 \sum_jh_j\mu_j\le E_+:=9\beta^{80L}(1+S\sqrt\ell),
 \qquad E_+\le CB\sqrt\ell,
 \qquad \mu_j\le\Lambda_j.                              \tag{7}
\]
No negative-semidefinite assertion holds for the algebraic transpose
at complex parameters; (6) is used only on real time segments.

Freeze the realized matrix, scalar-pair, residual and arithmetic errors
as the source's real-coefficient forcing polynomials. Freeze each
activation center and its interpolation polynomial within a patch.
With
\[
 \delta\le\delta_0=rac{\beta^{-150L}Sq_T}{G^2\sqrt n},
 \qquad C_N=B^2G^2\sqrt\ell,\qquad \eta=C_N\delta,
\]
the allowed source interfaces give, in the same complex sum-norm tube,
\[
 \|\overline F_j^{\rm num}-\overline F\|_\Sigma\le\eta,
 \qquad \|D_U\overline F_j^{\rm num}\|\le2\Lambda_j.       \tag{8}
\]
This field is nonautonomous and need not be a gradient. Its coefficients
are fixed for the comparison; there is no differentiation of the history
that produced them.

Let the initial Hilbert error be \(e_j\), with
\(c_Le_j\le d_n/8\) and \(4h_j\eta\le d_n/16\).
The original contraction on the radius-\(4h_j\) disk has factor
at most \(8h_j\Lambda_j\le1/4\). It constructs the exact local
perturbed flow, whose difference \(D(z)\) from the reference satisfies
\[
 \|D(z)\|_\Sigma
 \le(c_Le_j+|z|\eta)e^{\Lambda_j|z|}
 \le2c_Le_j+8h_j\eta.                                  \tag{9}
\]
Both points and their segment remain within the local tube. This is
the only complex stability estimate needed, and its patch size is
unchanged.

On the real interval, (6) and (8) instead give
\[
 \tfrac12\frac{d}{ds}\|D(s)\|_{\mathcal H}^2
 \le\mu_j\|D(s)\|_{\mathcal H}^2+\eta\|D(s)\|_{\mathcal H}.
\]
Applying this to \(\sqrt{\|D\|_{\mathcal H}^2+\varepsilon^2}\)
and taking \(\varepsilon\downarrow0\) yields
\[
 \|D(s)\|_{\mathcal H}\le(e_j+s\eta)e^{\mu_js},
 \qquad 0\le s\le h_j.                                 \tag{10}
\]
This step uses the exact field's gradient structure, while treating the
numerical-field discrepancy as an additive forcing.

The causal coefficient recurrence is the Taylor recurrence of the
perturbed flow. Cauchy's coefficient formula on \(|z|=2h_j\)
bounds the difference-series tail at the endpoint by
\((2c_Le_j+8h_j\eta)2^{-K}\). The true source tail is at most
\(2Mh_j2^{-K}\). Since \(h_j\mu_j\le1/32\), for \(K\ge4\)
the committed error therefore obeys
\[
 e_{j+1}\le(1+2h_j\mu_j+2c_L2^{-K})e_j
                   +C h_j\eta+2Mh_j2^{-K}.               \tag{11}
\]
Here \(C\) is a fixed numerical constant including independently
allocated endpoint rounding. Such rounding is an endpoint defect;
it is not asserted to preserve the polynomial after adding a constant
velocity forcing. For interior times the same Cauchy series also gives
the bound with the actual local time in the additive terms.

The product of the stability multipliers in (11) is bounded by
\[
 \exp(2E_++2c_LH2^{-K}).                                \tag{12}
\]
Thus \(c_L\) appears in an exponentially small Taylor tail and in
one-time norm conversions, not as a factor raised to \(H\).

## 4. Closing the bootstrap and every local physical precision

Take the candidate's explicit choices
\[
 \epsilon=\min\{d_n/(2^{12}c_L),n^{-a_0}/(2^{12}Bc_L)\},
\]
\[
 K=8+\left\lceil\frac{
 4E_++\log[2^{20}(c_L+1)(M+1)(T+1)/\epsilon]
       +\log(1+16c_LH)}{\log2}\right\rceil,
\]
\[
 \delta=\min\left\{\delta_0,
  \frac{\epsilon e^{-4E_+-10}}{2^{20}C_N(T+1)}\right\}.    \tag{13}
\]
Then \(2c_LH2^{-K}<1\). Iterating (11) gives a fixed numerical
multiple of
\[
 \{e_0+(T+1)[\eta+(M+1)2^{-K}]\}e^{2E_++1}.              \tag{14}
\]
At \(e_0=0\), substitution of (13) makes (14) less than
\(\epsilon/8\), with the displayed constants leaving ample fixed
allocation for endpoint rounding. Also \(4h_j\eta\ll d_n/16\).
Multiplication by \(c_L\) puts every anchor and interior value well
inside the sum-norm tube, closing the induction. Prediction sensitivity
is \(B\) in the physical sum norm; normalization cancels the state
factor \(Y\). Freezing at \(T\) then adds only the inherited
normalized fitting tail \(n^{-a_0}/4\). This verifies the stated
all-time whole-sphere predictor accuracy, including the fitted endpoint.

There is no hidden algebraic gap factor in the logarithmic terms:
\[
 \log\epsilon^{-1}+\log\delta_0^{-1}+\log(M+1)
       +\log(C_N+1)+\log(H+1)\le CZ.
\]
In particular \(S\ge16\beta^{-6L}/n\), so
\(\log S^{-1}\le\ell+6L\log\beta\). All occurrences of
\(G\) here are logarithmic. Equations (7) and (13) give
\[
 K+\log\delta^{-1}\le C(E_++Z)\le CBZ.                  \tag{15}
\]

The following checks cover the individual interfaces rather than only
the endpoint solver.

* **Matrix answers.** The proof-only polynomial
  \(\sigma\sum_{k<K}\zeta_k\xi^k\) has RMS at most
  \(\sigma4^K\) on \(|\xi|\le4\), on the original Gaussian
  RMS event. The least
  \(b_\sigma=\lceil2K+\log_2(4/\delta)\rceil\) makes this at
  most \(\delta/4\), with \(b_\sigma=O(BZ)\). Future coefficients
  remain proof devices and are not available to earlier queries.
* **Activation values and jets.** Put \(\alpha=\min\{1,a/16\}\).
  The original response bound on the unchanged complex patches keeps
  \(|z-x|<\alpha/64\) around each causal real center. Interpolation
  from \(J_{\rm act}\) real samples gives simultaneous errors in
  value, first derivative and second derivative at most
  \(C\beta^2(2^{-J_{\rm act}}+5^{J_{\rm act}}\nu)\) on
  \(|z-x|\le\alpha/4\). Choose
  \(J_{\rm act}\ge\max\{K+2,\lceil\log_2(C\beta^2/\delta)\rceil\}\)
  and \(\nu\le\delta/(C\beta^2 5^{J_{\rm act}})\).
  The least choices obey \(J_{\rm act}=O(K)\): every term of
  \(\log\delta^{-1}\) is bounded by a constant times the terms
  defining \(K\), including \(\log\delta_0^{-1}\), controlled by
  \(\log\epsilon^{-1}\). Consequently sample count, jet count and
  value precision have the claimed sizes. The continuous real value
  extension from `FAST_TAYLOR_NOISE.md` §3.1 remains available and
  costs its two primitive evaluations per sample.
* **Coefficient arithmetic.** The source tolerance
  \(\rho_{\rm arith}\le
  \delta/[C4^K(n+1)^3(BG(R+K+1))^C]\)
  has logarithmic inverse \(O(BZ)\). The equal patches satisfy
  \(h_{\min}^{-1}\le CBG\sqrt\ell\), so converting a rounded
  integrated coefficient to velocity forcing introduces no uncharged
  tiny final-step denominator. The centered interpolation implementation
  has scratch magnitude \(e^{CJ_{\rm act}}\) times fixed polynomial
  scales; it does not raise a raw \(\sqrt n\) coordinate cap to
  power \(J_{\rm act}\). The source's local working-precision
  formula therefore gives \(b_{\rm work}=O(BZ)\), plus supplied
  input descriptions.
* **Current-operand pairs.** An actual stored hidden rank list defines
  \(D=n^{-1}\sum_\mu c_\mu a_\mu b_\mu^\top\), even when
  its factors arose from imperfect pairs. Pair error relative to those
  same current operands gives exactly
  \(\sum_\mu c_\mu a_\mu e(b_\mu,v)\) as the learned-action
  defect. With \(N_{\rm sum}\le C(R+K+1)^3\) and the scalar
  forcing note's local bound \(A\), all coefficient defects are at
  most \(C N_{\rm sum}^2A^8\epsilon_{\rm pair}\). Freezing them
  on the complex disk adds \(4^K\). The choice
  \(\epsilon_{\rm pair}\le
  \delta/[C4^K N_{\rm sum}^2A^{10}]\) thus suffices.
  Here \(\log A\le CBZ\): its factors are local operand bounds,
  rank counts, \(Y^{-1}\le n\), \(h_{\min}^{-1}\), explicit
  guard margins, and \(e^{CJ_{\rm act}}\). There is no old
  accumulated stability exponent in their definitions.
* **Residuals and norm guards.** Readout-pair errors produce a fixed
  scalar residual polynomial measured after division by \(Y\);
  its physical field contribution is at most
  \(C\beta^{20L}r\delta\), absorbed by \(C_N\delta\).
  Its derivative uses the same forward/backward bounds. It is separate
  from the exact residual bound (2) used in the one-sided estimate.
  The rank-list squared-norm identity has pair-error bound
  \(3N_{\rm sum}^2A^4\epsilon_{\rm pair}\), small relative to
  the prescribed positive guard margin. For a hypothetical first active
  guard, complete its causal prefix with zero future defects; the local
  holomorphic flow then bounds that prefix's raw guard input strictly
  inside the cap. This contradicts first activation. The argument uses
  the unchanged complex contraction and the new certified endpoints,
  so it survives replacement of the old propagation budget by \(E_+\).

There is no residual projection onto the radius-\(Y\) ball in this
Taylor field. Such an older real extension could act with zero slack
and is not covered by the proof. The candidate correctly uses the
unclipped physical field and strict-slack numerical guards.

The choices are noncircular: choose \(T,h,H,E_+,\epsilon,K,\delta\),
then \(\sigma,J_{\rm act},\nu\), then a declared count \(R\),
then local operand/guard bounds and arithmetic/pair tolerances. Decreasing
the latter tolerances does not change the earlier chronology or add a
new matrix action.

## 5. The counting inequalities needed beyond the headline bound

The source radius inequality \(r_\tau^{-1}\le B\sqrt\ell\)
actually makes the third argument of the displayed minimum for \(h\)
the smallest. Hence
\[
 h=(64BG\sqrt\ell)^{-1},\qquad
 H\ge64BGT\sqrt\ell.                                   \tag{16}
\]
The certified-ceiling rule increases \(H\) by at most a constant.

To bound \(K\) by \(H\) without hiding input size, note that
\(r\ge\beta^{-6L}\) implies \(Br\ge\beta^{94L}\), so
\(T\ge188L\log\beta\). Also
\(a_0\log n\le T/2\) and \(\log G\le T/2\).
The explicit formula for \(d_n\) therefore gives
\(\log\epsilon^{-1}\le CT\). The other logarithms defining
\(K\), apart from \(\log H\), have the same bound. Consequently
\[
 K\le C\{E_++T+\log(H+1)\}\le CH,                     \tag{17}
\]
where (7), (16), and \(T\ge1\) justify the last inequality.
This does not use a bound involving \(\log m\) or \(\log d\):
those enlarged \(Z\) terms were upper allowances, not mandatory
terms in the selected degree. Thus even very large input descriptions
do not invalidate (17).

Let \(N=mLH\). The coefficient chronology has \(O(NK)\)
principal vectors and initialized calls. The \(O(NJ_{\rm act})\)
named scalar sample/jet fields also fit \(O(NK)\). Adding the first
roots gives
\[
 R\le C(d+NK)\le C\{d+mLB^2GZ^2\sqrt\ell\}.
\]
Take the declared chronology bound \(R\) large enough to dominate
\(NK\), as in the source. The learned scalar rank weights number
\(O(NK^2)\), which fits \(O(R^2)\). Cached local activation powers
and interpolation arrays use at most \(O(NK^2)\) scalar entries
if all centers' caches are retained, again within \(O(R^2)\).

The elementary cached activation computation costs per row
\[
 O\{N(J_{\rm act}K^2+J_{\rm act}^3)\}
 =O(NK^3)\le O((NK)^2)\le O(R^2),                       \tag{18}
\]
because \(J_{\rm act}=O(K)\) and \(K\le CH\le CN\).
These are scalar operation/cache counts only. Activation primitive work,
bit arithmetic, posterior routines and metric preprocessing are still
separate; (18) does not assert a total decoder-work bound.

## 6. Finite iid packets and the total-law bridge

Set \(\chi_+=BZ\). The revised physical answer, pair and principal
coefficient tolerances have logarithmic reciprocals at most
\(C\chi_+\). Physical query/raw-answer RMS caps are fixed polynomials
in \(B,G\), and \(\log(e+n+R)\le CZ\). Therefore the finite
bridge's scales
\[
 z=C(2+R+b+\sigma^{-1}),\qquad \mathcal M=(n+1)z^{120}
\]
satisfy \(\log z+\log\mathcal M\le C\chi_+\). Its supplied
one-call coefficient/Gaussian estimate remains
\[
 \kappa\le z^{230}\{\sqrt n\,e_c+n\eta_{\rm acq}^2\}.   \tag{19}
\]
Here \(\eta_{\rm acq}\) is acquisition noise, not the physical
forcing \(\eta=C_N\delta\).

For clarity, the total-law mechanism does not rely on perturbing a
globally expanded history. At a complete shared past, the finite bridge
freezes its coefficient arrays and constructs the affine proof pair
\[
 t=A_cg+\eta_{\rm acq}e,\qquad
 y=\widetilde m+B_ct+cg,
\]
where \(g,e\) are independent standard Gaussians and \(c>0\).
The map is invertible:
\[
 g=(y-\widetilde m-B_ct)/c,\qquad
 e=(t-A_cg)/\eta_{\rm acq}.
\]
Thus the actual finite sampler, innovation rounding, answer rounding,
and all future-used finite marks form a common deterministic
postprocessor \(J_H(y,t)\). This inversion is for the proof only.

For the physical call use the true Gaussian raw answer law \(P_H(dy)\)
and augment by the affine shadow's conditional kernel \(Q_H(dt\mid y)\).
That kernel is independent of hidden matrices once the complete past and
raw answer are fixed, so its likelihood cancels in Bayes' formula.
The completed-call Gaussian posterior is preserved. Moreover
\[
 \|Q_H(dy,dt)-P_H(dy)Q_H(dt\mid y)\|_{\rm TV}
 =\|Q_H(dy)-P_H(dy)\|_{\rm TV}.
\]
Integration against the common conditional kernel and projection onto
\(y\) give the two inequalities. Applying \(J_H\) cannot increase
this distance, regardless of its rounding discontinuities. No matrix
call is allowed between innovation acquisition and completion of that
answer. A Gaussian posterior at an intermediate rounded prefix is not
being claimed.

At the same complete history, every finite stored answer is within its
local postprocessing tolerance of its own physical raw answer. Thus raw
query/answer Gram inputs differ from the finite inputs by the bridge's
local moment estimate, with no accumulated history factor. Equation
(19) is applied at this shared history and summed over calls. Matrix
posterior independence, unconsumed iid packet coordinates, and exclusion
of private metric/packet selection are all preserved by the original
chronology; the new values of \(K,H,R\) do not change these properties.

The bridge selects
\[
 \xi_0=\frac{\rho}{2^{20}(R+1)(n+1)z^{240}},
\]
then acquisition, answer, coefficient, innovation-grid and sampler
tolerances using a fixed number of products and minima. Each now costs
\(C[\chi_++\log(1/\rho)]\) bits. Its scalar-mark replay condition
\[
 \eta_{\rm acq}\epsilon_G\le
 \frac{(\rho/16)\min(h_{\rm acq},h_t)}{64(P+1)},
 \qquad P\le CR^2,
\]
is another such local requirement; here \(h_{\rm acq}\) is the
ordinary scalar grid, not the physical patch length. The grids and
\(\eta_{\rm acq}\) are chosen before decreasing \(\epsilon_G\),
so this choice is noncircular.

The Gaussian tail cutoff has
\(T_G^2=O(\log(n(d+R)+P+1)+\log(1/\rho))\). The explicit
finite sampler's bit condition is
\(b_G\log2\ge T_G^2/2+\log(C/\epsilon_G)\); hence it has the
same precision envelope. Different coordinate types may use different
precisions, with identical coordinate-type laws across rows. The packets
therefore remain iid and finite. The computational cost of the sampler
and protected small-matrix routines is the inherited charged interface.

The first-layer root coupling needs its own updated allocation. An
entrywise root error at most \(\epsilon_G\) gives normalized initial
Hilbert error at most \(\sqrt d\epsilon_G/Y\). Taking
\[
 \epsilon_G\le
 \frac{Y\epsilon e^{-4E_+-10}}{2^{20}(\sqrt d+1)}          \tag{20}
\]
makes \(e_0\le\epsilon e^{-4E_+-10}/2^{20}\), which fits (14).
This replaces the old global exponent in the root allocation explicitly;
it is not enough to replace only the local answer tolerances. Since
\(Y^{-1}\le n\), (20) costs \(O(\chi_+)\) bits. The physical
scientific initialization stays the original Gaussian one, with the
finite first matrix treated as a nearby numerical initial state.

Maximal coupling of completed calls now costs at most the sum of (19).
Before failure, both sides execute exactly the same finite operations
and have the same finite tape. Their differences from the physical raw
matrix actions are local forcing defects. Current-operand physical pairs,
rank-list parameters and all guards meet the conditions checked above.
The stopped coupling therefore retains
\[
 \Pr(\text{inherited scientific failure})+Re^{-cn}+\rho
\]
as its failure bound. Source-marginal sampler failure and
physical-marginal scientific/raw-noise failure may be charged separately
before the coupling stops, as in the bridge. The resulting local precision
is \(p_{\rm loc}\le C[BZ+\log(1/\rho)]\).

## 7. Boundary of the verified result

There is no required correction to the candidate's main asymptotic claim.
Two useful clarifications have been made explicit here: the Hessian norm
uses the Euclidean isometry in §2, and \(K\le CH\), together with
\(J_{\rm act}=O(K)\), supplies the work/cache substitution in §5.

The finite acquisition base, conditional on the bridge's separate metric
interface, is consequently
\[
 O\left(\{d+mLB^2GZ^2\sqrt\ell\}^{,2}
                  [BZ+\log(1/\rho)]\right).
\]
At fixed confidence its displayed algebraic gap degree is two; the old
source-plus-precision substitution gave degree five. The gap dependence
inside logarithms remains visible. This does not give a full passive
decoder, a compact seed, a uniform query-work theorem, or local stability
for arbitrary newly substituted row packets.

Finally, the original small-label intersection and all scientific width
conditions remain in force. In particular, the deterministic condition
in `PHYSICAL_PARAMETER_ACCOUNTING.md` (28), with physical radius
coefficient \(c=\chi(S)/\lambda\), is unchanged, as is the inherited
unquantified stochastic width threshold. The explicit horizon gate
\(n\ge\max\{1,e^{-1}\sqrt{1+66Br}\}\) is also retained.
These can entail exponential width in inverse-gap parameters. Removing
one algebraic gap factor from numerical degree and local precision does
not turn those scientific events into a polynomial-width theorem.
