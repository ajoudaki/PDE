# Error-prefactor route: explicit tolerance cost and a polynomial tail

2026-10-04. Independent bounded theoretical route, frozen before exchanging
findings. This is a derivation from the five assigned internal source
statements, not a promotion review of their inherited proof chains. No
experiment, shared-file edit, or Git operation was performed.

## Scope and conclusion

The target is the same realized canonical Gaussian width-\(n\) network,
the same autonomous corrected-readout compression, and the supremum over
all physical time and the whole input sphere. The input dimension \(d\ge2\)
and depth \(L\ge2\) are fixed. All retained real coordinates count.
The allowed label condition remains \(0<Y\le c\lambda\), where
\(Y=\|y\|_2/\sqrt m\) and
\(\lambda=\min(1,\gamma/m)\), with \(\gamma>0\) the smallest
eigenvalue of the limiting initialized top-feature covariance. Zero labels
have the separate stationary zero representation. Constants denoted by
\(C\) are structural, depending on fixed dimension, depth, and activation
strip bounds; they do not hide sample count or gap dependence.

**Finding.** The existing comparison theorem genuinely gives a polynomial
error prefactor by choosing a smaller source tolerance. Its full cost has
additional polynomial gap/sample terms. It does **not** give the former
quadratic \(m\) storage prefactor unchanged. A refinement using accurate
training-only sources reduces this extra cost, and a direct differentiation
of the corrected readout proves a polynomial all-time tail. Neither argument
proves that the exponential stability bound is intrinsic.

The five assigned files were read completely:

- `STORAGE_QUADRATIC_IMPROVEMENT.md`, SHA-256
  `ec18f54a3e3977bf9c99ce5c26066f48688848f8b5a9c142b75424badeb025e2`;
- `DEPTH_INDEPENDENT_EXPONENT.md`, SHA-256
  `73c12dafdd05dcae7f287b2ccc49cc237a540ef7b2f26d53204c96bcd9feceda`;
- `INPUT_DEPTH_REFINEMENT.md`, SHA-256
  `9d468fe3469436c1c10cf01f9194cff7fea71339c8964578b83047b4f5c79a3d`;
- `SAMPLE_COUNT_REFINEMENT.md`, SHA-256
  `d1de9321308530b9cd648e3ffd25f4987f42b2a343260d087cae924fd13f7242`;
- `GENERAL_ANALYTIC_COMPRESSION.md`, SHA-256
  `4fd314dd28367430cd60fa8b88fe0eb4d9b12f575c61aadd60ff61dff76dec53`.

No linked scientific source outside that assignment was fetched. The required
canonical-notation and conjecture-investigation skills and their relevant
references were applied.

## 1. Quantitative interface being optimized

For \(v=x/\sqrt d\in S^{d-1}\), the reference forward pass is

\[
z^{(1)}=Av,\qquad z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\qquad
h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad f_n=w^\top h^{(L)}/n.
\]

The middle recurrence is for \(\ell\ge2\). Initialization has independent
standard Gaussian entries in \(A\), independent \(N(0,1/n)\) entries in
the hidden matrices, independent blocks, and \(w(0)=0\). With
\(c_a=y_a-f_n(v_a)\), \(k_a^{(L)}=w\),
\(\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)}\), and
\(k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}\), the reference is

\[
\dot A={2\over m}\sum_a c_a\delta_a^{(1)}v_a^\top,\quad
\dot W^{(\ell)}={2\over mn}\sum_a c_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},
\quad \dot w={2\over m}\sum_a c_ah_a^{(L)}.
\]

The existing compressed model retains fixed positive metrics \(H_\ell\),
moving hidden matrices, raw readout \(w_C\), and residual state \(c_C\).
Its effective readout is

\[
\widehat w_C=w_C+F_C(F_C^\top H_LF_C)^{-1}
 (y-c_C-F_C^\top H_Lw_C),\qquad
f_C(v)=\widehat w_C^\top H_Lh_C^{(L)}(v),
\]

where \(F_C\) consists of current training features. Its exact own-residual
identity is \(y-f_C(v_1,\ldots,v_m)=c_C\). Its autonomous equations and
surrogate positive Gram are those of Section 4 of the storage source; they
are not changed here.

Put \(\ell_n=\log(en)\), \(q_n=\ell_n+\log(e/\lambda)\). The assigned
source theorem supplies a complex time/input-angle radius
\(r_n=c\ell_n^{-1/2}\), horizon \(T=C\lambda^{-1}\ell_n\), and coordinate
bound \(C\sqrt n\). It supplies all source families and both paired
initialized matrix orientations. The carrier bound is
\(M\le1+C(Y/\lambda)\sqrt{\ell_n}\).

For source coordinate tolerance \(\epsilon\), the exact deterministic
comparison in Section 5 of the storage source gives

\[
E(t)+\epsilon\le\epsilon e^{\Xi_n},\qquad
\sup_{t\le T,v}|f_C-f_n|
 \le C\lambda^{-1/2}\epsilon e^{\Xi_n},
\tag{1}
\]

where \(E\) is the sum of parameter-distance and residual-distance norms
defined there, and a structural constant can be chosen so that

\[
\Xi_n=C\left({Y\over\lambda^{5/2}}
       +{Y^2\over\lambda^{7/2}}\sqrt{\ell_n}\right).
\tag{2}
\]

This is the raw width-dependent error bound. At the old choice
\(\epsilon=n^{-1}\), it is exactly the exponential-data/subpolynomial-width
tradeoff in the assigned source, up to structural constants.

## 2. A tighter tolerance gives a real, but more costly, improvement

Choose explicitly

\[
\epsilon_n=n^{-1/2}e^{-\Xi_n}.
\tag{3}
\]

Equations (1)--(3) give \(E\le n^{-1/2}\) and the finite-time error
\(C\lambda^{-1/2}/\sqrt n\). Thus the comparison tube closes once
\(n^{-1/2}\) is below its prescribed gap margin; a sufficient algebraic
condition is \(n\ge C/\lambda\). All original source-event thresholds
remain necessary. No exponential error factor is being discarded by
enlarging the width threshold.

Approximation to (3) has logarithmic degree factor

\[
Q_n=q_n+\Xi_n.
\]

Indeed \(\log(C\sqrt n/\epsilon_n)\le C(\ell_n+\Xi_n)\).
The prefactors in the analytic tail estimates contribute
\(\log(e/\lambda)\) and logarithms of degrees. Under \(Y\le c\lambda\),
\(\Xi_n\le C\lambda^{-3/2}\sqrt{\ell_n}\), so the logarithms of degrees
are absorbed by \(Cq_n\), without any condition that \(\ell_n\) dominate
a power of \(1/\lambda\). Thus one can take

\[
p\le C\lambda^{-1}\ell_n^{3/2}Q_n,\qquad
J\le C\ell_n^{1/2}Q_n,
\]

and the layer-space dimension and total retained count satisfy

\[
R\le C\lambda^{-1}\ell_n^{d/2+1}Q_n^d+C(m+d),
\]
\[
\operatorname{size}\le
C\lambda^{-2}\ell_n^{d+2}(q_n+\Xi_n)^{2d}+Cm(d+1).
\tag{4}
\]

The exact initialization additions are absorbed as in the assigned source,
using \(m\lambda\le C\). All fixed metrics, reduced matrices, residuals,
readouts and caches are counted by the same \(O(R^2)\) argument.

In particular (4) implies the fully explicit bound

\[
\operatorname{size}\le
C\lambda^{-2}\ell_n^{d+2}q_n^{2d}
 +C\lambda^{-(3d+2)}\ell_n^{2d+2}+Cm(d+1).
\tag{5}
\]

When \(\lambda=\gamma/m\), the new term is
\(C(m/\gamma)^{3d+2}\ell_n^{2d+2}\). The unchanged first term is the
previous quadratic sample count, with its logarithmic gap factor. The
new term cannot be omitted by assuming \(\ell_n\gtrsim\lambda^{-3}\).
Such an assumption would hide exactly the cost under investigation.

## 3. A mixed source space lowers the price of this tolerance change

The dynamical comparison uses training features and training backward
signals. The whole-query forward sources enter only the final evaluation
of a passive query and its layerwise forward subtraction. They do not enter
the residual/parameter Gronwall inequality except at training points.

Consequently there is a second admissible construction. Approximate the
whole-query forward source families to \(\epsilon_q=n^{-1/2}\), and add
all training-only forward and backward source families and their paired
images to accuracy \(\epsilon_t=n^{-1/2}e^{-\Xi_n}\). Add their spaces
before the same spectral selection and metric correction. The restriction
remains exactly isometric on the combined space, so both accuracies hold
in the selected weighted norm. All initialization additions are unchanged.

The training recursion now gives
\(E\le\epsilon_t e^{\Xi_n}\le n^{-1/2}\); the whole-query forward error
is \(C(E+\epsilon_q)\). The corrected-readout estimate depends only on
training accuracy. Thus the final whole-query bound is still
\(C\lambda^{-1/2}/\sqrt n\).

There are \(O(m)\) training-only time families, each with temporal degree
\(C\lambda^{-1}\ell_n^{3/2}(q_n+\Xi_n)\). Therefore

\[
R\le C\left[
 \lambda^{-1}\ell_n^{d/2+1}q_n^d
 +m\lambda^{-1}\ell_n^{3/2}(q_n+\Xi_n)\right]+C(m+d),
\]

and a complete count is

\[
\operatorname{size}\le
C\lambda^{-2}\ell_n^{d+2}q_n^{2d}
 +Cm^2\lambda^{-2}\ell_n^3(q_n+\Xi_n)^2+Cm(d+1).
\tag{6}
\]

At maximal allowed labels this gives

\[
\operatorname{size}\le
C\lambda^{-2}\ell_n^{d+2}q_n^{2d}
 +Cm^2\lambda^{-2}\ell_n^3q_n^2
 +Cm^2\lambda^{-5}\ell_n^4+Cm(d+1).
\tag{7}
\]

The last term is \(Cm^7\gamma^{-5}\ell_n^4\) in uncapped notation.
This improves the additional sample exponent relative to (5) for every
\(d\ge2\), but reintroduces the explicitly counted training-source factor.
One may choose the smaller of (4) and (6) before preprocessing, since their
error guarantees and runtime architecture agree. Neither bound establishes
the polynomial error prefactor at the former pure-quadratic sample count.

## 4. The endpoint tail has a polynomial constant already

This calculation removes an unnecessary ambiguity in the phrase
\(C_{\rm data}\) in the source's tail proof. Equip the neuron space with
the \(H_L\) inner product and let adjoints refer to that Hilbert structure.
Set

\[
V=F_C/\sqrt m,\quad q=V^*V,\quad
b=(y-c_C)/\sqrt m,\quad T_V=Vq^{-1},\quad P_V=T_VV^*.
\]

The existing independent fitting argument supplies

\[
q\succeq c\lambda I,\quad \|V\|\le C,\quad
\|w_C\|+\|\widehat w_C\|\le CY/\sqrt\lambda,\quad
\|\dot V\|\le C(Y/\sqrt\lambda)\rho_C,
\]

where \(\rho_C=\|c_C\|_2/\sqrt m\le Ye^{-c\lambda t}\).
It also supplies \(\|\dot w_C\|+\|\dot b\|\le C\rho_C\).
The map \(P_V\) is an orthogonal projector and
\(\|T_V\|\le C\lambda^{-1/2}\).

Differentiate without separating canceling projector terms:

\[
\dot T_V=(I-P_V)\dot Vq^{-1}-T_V\dot V^*T_V,
\]
\[
\dot P_V=(I-P_V)\dot VT_V^*
                  +T_V\dot V^*(I-P_V).
\tag{8}
\]

The first identity follows directly by differentiating \(Vq^{-1}\) and
using \(\dot q=\dot V^*V+V^*\dot V\); differentiating \(T_VV^*\) gives
the second. Hence

\[
\|\dot T_V\|\le C\lambda^{-1}\|\dot V\|,\qquad
\|\dot P_V\|\le C\lambda^{-1/2}\|\dot V\|.
\]

Since \(\widehat w_C=(I-P_V)w_C+T_Vb\) and \(\|b\|\le2Y\),

\[
\|\dot{\widehat w}_C\|
\le C\left(1+\lambda^{-1/2}+Y^2\lambda^{-3/2}\right)\rho_C
\le C\lambda^{-1/2}\rho_C.
\tag{9}
\]

For every sphere query, the feature norm is bounded and its derivative
is at most \(C(Y/\sqrt\lambda)\rho_C\). Differentiating the output and
using (9) proves

\[
\sup_v|\partial_t f_C(t,v)|\le C\lambda^{-1/2}\rho_C(t),
\]
\[
\sup_v|f_C(\infty,v)-f_C(t,v)|
 \le CY\lambda^{-3/2}e^{-c\lambda t}
 \le C\lambda^{-1/2}e^{-c\lambda t}.
\tag{10}
\]

The original gradient flow has the corresponding stronger elementary
bound \(C\rho_n\) on output speed: its readout velocity is \(C\rho_n\),
its readout norm is \(CY/\sqrt\lambda\), and its hidden velocity is
\(C(Y/\sqrt\lambda)\rho_n\). These follow from the same energy and Gram
gap estimates. Its tail is at most \(C(Y/\lambda)e^{-c\lambda t}\).
Taking a structural horizon multiplier so \(e^{-c\lambda T}\le n^{-1}\),
then comparing both paths with their values at \(T\), proves for either
(4) or (6)

\[
\boxed{\quad
\sup_{t\in[0,\infty],\ v\in S^{d-1}}|f_C(t,v)-f_n(t,v)|
\le {C\over\sqrt{\lambda n}}.
\quad}
\tag{11}
\]

This includes fitted endpoints and has prefactor
\(C\sqrt{m/\gamma}\) when the cap is inactive. The source high-probability
event and fixed-dataset quantifiers remain those of the assigned theorem;
this is not a growing-sample theorem. The tail calculation changes no
source tolerance and costs no extra retained coordinates.

## 5. What this route does and does not settle

The exponential in (2) is an upper bound from a scalar Gronwall majorant.
Nothing in the assigned sources proves a matching lower bound. In
particular, a badly conditioned correction map does not imply exponential
instability of the coupled autonomous dynamics: the residual equation has
a positive damping Gram and can have cancellations invisible to that
majorant.

The map \(T_V\) does have norm exactly
\(\sigma_{\min}(V)^{-1}\). A discrepancy in the associated sample singular
direction is multiplied by that inverse singular value. Thus
\(\lambda^{-1/2}\) is a real conditioning scale at the interpolation
interface. This is not a lower bound on the final compressed-model error,
since an actual error may avoid that direction and output evaluation can
further reduce it.

| Claim | Status from this route |
|---|---|
| Polynomial prefactor with the same reference, labels, optimizer and all-time norm | Derived from the inherited theorems with explicit extra storage (4) or (6) |
| Polynomial all-time tail prefactor | Direct identity calculation (8)--(10) |
| Same polynomial prefactor with the former pure-quadratic sample count | Open in this route |
| Exponential dependence is necessary | Unsupported; no lower bound was supplied |
| Merely enlarging \(n_0\) makes a prefactor of one a substantive optimization | Rejected: it changes no raw error or retained-count tradeoff |

The decisive remaining route is a sharper coupled stability estimate at
the original \(n^{-1}\) source tolerance, or an approximation method that
attains (3) without the additive degree terms in (4)/(6). This note supplies
neither claim and does not hide either inside an eventual-width condition.
