# Huang–Yau NTH: source audit and storage consequences

Scope: external source audit requested by the supervisor of this study. No other study was consulted. This note is an internally checked derivation, not promoted theory. It distinguishes algebraic consequences of the published statement from a conditional theorem proved here.

Sources read completely: [PMLR 2020 paper](https://proceedings.mlr.press/v119/huang20l/huang20l.pdf), 10 pages; [arXiv:1909.08156v1](https://arxiv.org/pdf/1909.08156), 39 pages including Appendices A–C. The PMLR paper separates the regularity budget `p*` from truncation order `p`; the arXiv version uses `p` for both. The PMLR landing page supplies no supplementary-material link, although the paper refers to supplementary proofs. Thus the inspected detailed proof is explicitly the arXiv version, not an assumed final supplement.

## Model, notation, and exact storage

Here `n` is width, `m` is number of samples, `d` is input dimension, `L` is number of hidden layers, and `q` is truncation order. The paper's `(m,n,H,p)` equals our `(n,m,L,q)`. Let `s` denote the PMLR regularity budget `p*`.

For inputs \(x_a\in\mathbb R^d\) and scalar labels \(y_a\), the source model is

\[
h_a^{(0)}=x_a,\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=n^{-1/2}\phi(z_a^{(\ell)}),\qquad
f_a=a^\top h_a^{(L)}.
\]

Here \(W^{(1)}\in\mathbb R^{n\times d}\), \(W^{(\ell)}\in\mathbb R^{n\times n}\) for \(2\le\ell\le L\), and \(a\in\mathbb R^n\). Independent Gaussian initialization has variances \(\sigma_w^2\) for weights and \(\sigma_a^2\) for readout entries. Every parameter follows Euclidean gradient flow of

\[
\mathcal L(\theta)=\frac1{2m}\sum_{a=1}^m(f_a(\theta)-y_a)^2.
\]

This normalization and parameter metric must be preserved. The number of trainable real coordinates is exactly

\[
P=nd+(L-1)n^2+n.
\]

Define parameter-dependent tensors recursively by

\[
K^{(2)}_{ab}(\theta)=\langle\nabla_\theta f_a,\nabla_\theta f_b\rangle,
\qquad
K^{(r+1)}_{a_1\ldots a_r b}(\theta)
=\langle\nabla_\theta K^{(r)}_{a_1\ldots a_r},\nabla_\theta f_b\rangle.
\]

Writing \(r_a=f_a-y_a\), the chain rule gives the exact hierarchy

\[
\dot f_a=-\frac1m\sum_bK^{(2)}_{ab}r_b,
\qquad
\dot K^{(r)}_{a_1\ldots a_r}
=-\frac1m\sum_bK^{(r+1)}_{a_1\ldots a_r b}r_b.
\]

The order-\(q\) truncation evolves \(\widetilde f\) and \(\widetilde K^{(2)},\ldots,\widetilde K^{(q-1)}\) by these same contractions with tildes, freezes \(\widetilde K^{(q)}\), and copies all retained initial values exactly from the dense network. Its direct array representation uses

\[
S_q=2m+\sum_{r=2}^{q}m^r
\]

real coordinates, including labels. Of these, \(m^q+m\) are fixed coefficients and labels; \(m+\sum_{r=2}^{q-1}m^r\) evolve. Retaining the training inputs adds \(md\). This is an upper bound without exploiting tensor symmetries. For \(q=2\), the frozen matrix is symmetric and can instead use \(m(m+1)/2\) entries.

These are **online real-coordinate counts**, not bit-complexity, arithmetic-work, or initialization-memory bounds. Computing the initial tensors is a separate dense-network task. The theorem supplies no compressed procedure for that initialization. New test points require additional initial tensor slices or continued access to the initializer. Training-sample output compression alone does not supply arbitrary-input inference.

## What the literal published theorem would imply

The fixed-background assumptions are: a smooth activation with finite derivative bounds \(C_j=\|\phi^{(j)}\|_\infty\), \(1\le j\le 2s+1\); input norms bounded above and away from zero; and a positive lower singular-value bound \(c_j\) for every matrix formed from \(j\) distinct inputs, \(1\le j\le2s+1\). The PMLR theorem permits even \(2\le q\le s\) and assumes the realized initialization satisfies \(K^{(2)}_0\succeq\lambda I_m\), \(\lambda>0\). Its Section 1.3 fixes \(s,L,C_j,c_j\), assumes polynomial comparability of sample count and width, and does not track these constants.

Let \(A_q,b_q,C_q,C'_q>0\) name the constants in the literal PMLR Theorem 2.6. This naming makes no claim to have determined their dependence. For a fixed admissible background and on its claimed event, its prediction estimate becomes

\[
E_q(T):=\sup_{0\le t\le T}\frac{\|f(t)-\widetilde f(t)\|_2}{\sqrt m}
\le
\frac{A_q(1+T)T^{q-1}}{n^{q/2}}
\min\!\left(T,\frac m\lambda\right),                    \tag{1}
\]

provided

\[
T\le\min\!\left\{
\frac{b_q\sqrt{\lambda n/m}}{(\log n)^{C_q}},
\frac{n^{s/[2(s+1)]}}{(\log n)^{C'_q}}
\right\}.                                                   \tag{2}
\]

The supremum follows because the displayed upper bound is nondecreasing in time. All uses below require sufficiently large \(n\), as in the source.

For any target RMS discrepancy \(\varepsilon>0\), elementary rearrangement of (1) gives the sufficient precision condition

\[
n\ge
\left[
\frac{A_q(1+T)T^{q-1}\min(T,m/\lambda)}{\varepsilon}
\right]^{2/q}.                                              \tag{3}
\]

This is a storage corollary only when the actual counts also satisfy \(S_q<P\), or \(S_q+md<P\) if data storage is charged solely to the closure. Along an asymptotic family, a vanishing storage ratio requires the corresponding ratio to tend to zero. Equation (3) by itself is not a compression statement.

For the width-dependent target \(\varepsilon=\eta n^{-1/2}\), with fixed \(\eta>0\), (1) instead gives

\[
n\ge
\left[
\frac{A_q(1+T)T^{q-1}\min(T,m/\lambda)}{\eta}
\right]^{2/(q-1)}.                                         \tag{4}
\]

In particular, \(q=2\) uses \(m^2+2m\) coordinates and requires

\[
\sqrt n\ge
\frac{A_2}{\eta}(1+T)T\min(T,m/\lambda),                    \tag{5}
\]

in addition to (2). If \(T=(m/\lambda)h\), \(h\ge1\), and \(T\ge1\), then

\[
(1+T)T\min(T,m/\lambda)
\le2(m/\lambda)^3h^2.
\]

Thus \(n\ge4A_2^2\eta^{-2}(m/\lambda)^6h^4\) suffices for (5). Both timing conditions still have to be checked:

\[
n\ge b_2^{-2}(m/\lambda)^3h^2(\log n)^{2C_2},
\qquad
n\ge[(m/\lambda)h(\log n)^{C'_2}]^{2(s+1)/s}.               \tag{6}
\]

This preserves the source's unnormalized spectral parameter \(\lambda\). Replacing it by a constant without a data-dependent lower bound would change the result. A fitting-time claim additionally needs a stated target training residual and its own convergence argument; \(h\) here is just an explicitly chosen horizon factor.

Equations (1)–(6) are algebraic consequences of the **literal source statement**, not a new proof of its stochastic estimate. The proof discrepancies below prevent using them as a fully explicit joint theorem in \((n,m,d,L,q,\phi,\delta)\).

## A conditional order-two theorem proved here

This result avoids the unexplained constants in the source's truncation comparison. Assume the network trajectory exists on \([0,T]\), its activation is sufficiently smooth to define \(K^{(4)}\), and let

\[
R=\frac{\|f(0)-y\|_2}{\sqrt m}.
\]

Suppose explicit numbers \(B_3,B_4\ge0\) satisfy

\[
\|K^{(3)}_0\|_{\max}\le\frac{B_3}{n},\qquad
\sup_{0\le t\le T}\|K^{(4)}_t\|_{\max}\le\frac{B_4}{n},    \tag{7}
\]

where \(\|\cdot\|_{\max}\) is the largest absolute tensor entry. Define the frozen-kernel predictor by

\[
\dot u=-\frac1mK^{(2)}_0(u-y),\qquad u(0)=f(0).
\]

If \(K^{(2)}_0\succeq\lambda I_m\) with \(\lambda\ge0\), then

\[
\sup_{t\le T}\frac{\|f(t)-u(t)\|_2}{\sqrt m}
\le\frac{R^2B_3T+R^3B_4T^2/2}{n}
\begin{cases}
\min(T,m/\lambda),&\lambda>0,\\
T,&\lambda=0.
\end{cases}                                                \tag{8}
\]

For all \(\lambda\ge0\), the alternative bound

\[
\sup_{t\le T}\frac{\|f(t)-u(t)\|_2}{\sqrt m}
\le\frac{R^2B_3T^2/2+R^3B_4T^3/6}{n}                     \tag{9}
\]

also holds. No stability assumption on the truncated hierarchy, or smallness condition beyond (7), is needed for this order-two comparison.

Proof. Since \(K^{(2)}_t\) is a Gram matrix,

\[
\frac d{dt}\frac{\|f(t)-y\|_2^2}{2}
=-\frac1m(f(t)-y)^\top K^{(2)}_t(f(t)-y)\le0.
\]

Consequently \(m^{-1}\sum_b|f_b(t)-y_b|\le R\). The exact hierarchy and (7) give, successively,

\[
\|K^{(3)}_t\|_{\max}\le\frac{B_3+RB_4t}{n},
\quad
\|K^{(2)}_t-K^{(2)}_0\|_{\max}
\le\frac{RB_3t+R^2B_4t^2/2}{n}.                           \tag{10}
\]

For an \(m\times m\) matrix \(A\), \(\|A\|_{\mathrm{op}}\le m\|A\|_{\max}\). Subtracting the two prediction equations, with \(e=f-u\), yields

\[
\dot e=-\frac1mK^{(2)}_0e
-\frac1m(K^{(2)}_t-K^{(2)}_0)(f-y),\qquad e(0)=0.
\]

The matrix exponential satisfies \(\|e^{-K^{(2)}_0v/m}\|_{\mathrm{op}}\le e^{-\lambda v/m}\) for \(v\ge0\). Variation of constants and (10) imply

\[
\frac{\|e(t)\|_2}{\sqrt m}
\le\frac1n\int_0^t e^{-\lambda(t-v)/m}
\left(R^2B_3v+\frac{R^3B_4v^2}{2}\right)\,dv.
\]

Bounding the polynomial by its value at \(T\) and integrating the exponential proves (8); dropping the exponential and integrating the polynomial proves (9). The formulas also cover \(R=0\) and \(T=0\).

In this conditional theorem, a sufficient width condition for RMS error \(\varepsilon\) is the numerator in (8), including its time factor, divided by \(\varepsilon\). For \(\varepsilon=\eta n^{-1/2}\), the sufficient condition is the square of that numerator divided by \(\eta^2\). If (7), the residual bound, and the spectral bound hold jointly with probability \(1-\delta\), the deterministic conclusion holds with that same probability. This does not claim a probability for those hypotheses. The storage is the explicit order-two count above.

## Dependence and proof gaps that cannot be concealed

1. **Activation and depth.** Appendix B.4 propagates \(|\phi(0)|\) and powers of \(C_1\) through the layers. Its norm-flow bound contains a factor comparable to \(C_1^L\), and higher-order expression sets have depth-dependent lengths. Appendix A uses inverses of limiting Gram matrices of activation-derived expressions without numerical lower bounds. Thus tracking only \(C_j\) as upper bounds is insufficient to extract the claimed constants from that proof. Near constant activations, relevant Gram lower bounds can degenerate while derivative upper bounds stay finite. Neither growing \(L\) nor growing \(q\) has been justified by the paper's fixed-background notation.

2. **Input conditioning and dimension.** The general-position hypothesis implies
   \[
   d\ge\min(m,2s+1).
   \]
   It imposes more than this rank condition. Put \(R_x=\max_a\|x_a\|_2\). The two-column singular-value bound gives \(\|x_a-x_b\|_2\ge\sqrt2c_2\). Disjoint balls of radius \(c_2/\sqrt2\) around the inputs lie inside the ball of radius \(R_x+c_2/\sqrt2\). Comparing their volumes proves
   \[
   m\le(1+\sqrt2R_x/c_2)^d.
   \]
   Hence a sequence with bounded \(R_x\), fixed \(c_2>0\), and unbounded \(m\) cannot keep \(d\) fixed. Appendix A's Gram–Schmidt and pseudoinverse steps also absorb the \(c_j\). Theorem 2.6 supplies no quantitative replacement if these deteriorate.

3. **An additional dimension issue in the inspected proof.** Appendix B.1 bounds \(\|W^{(1)}_0\|_{\mathrm{op}}/\sqrt n\) by a fixed constant. For an \(n\times d\) Gaussian matrix the natural scale is \(\sigma_w(1+\sqrt{d/n})\). Thus that proof step needs bounded \(d/n\), or a revised argument restricting to the data span. No such aspect-ratio hypothesis is stated in the main theorem. This is a gap in the inspected proof route, not a claim that the actual training problem intrinsically requires \(d=O(n)\).

4. **Label and residual scale.** Appendix B.1 uses \(\sum_a|f_a(0)-y_a|^2=O(m)\) without a stated label bound; Appendix C repeatedly uses this estimate. Arbitrarily large labels cannot be ignored. A usable theorem should carry \(R\), as (8)–(9) do, or prove a bound using a label scale and a specified confidence. Gaussian initialization does not make a nondegenerate single initial output bounded by a fixed number with probability tending to one.

5. **Logarithms in the truncation proof.** Appendix C.16 bounds an odd-order kernel with a \((\log n)^C\) factor. The next estimate for the derivative of the top retained tensor drops that factor. The published prediction bound also has no logarithmic factor. No reason for the deletion is given in the inspected proof. Retaining the factor yields a weaker, plausible comparison, but cannot be silently advertised as the printed theorem. In (8), such factors remain explicitly inside \(B_3,B_4\).

6. **Confidence mismatch.** Section 1.3 defines its probability convention as \(1-\exp(-n^c)\). Appendix A.5 applies this convention to \(\|a_0\|_\infty\lesssim(\log n)^C\), since \(a_0\) belongs to its expression set. For any fixed positive \(c,C,M,\sigma_a\), however,
   \[
   \Pr\{\|a_0\|_\infty>M(\log n)^C\}
   \ge\Pr\{|(a_0)_1|>M(\log n)^C\}
   \]
   has Gaussian-tail scale \(\exp[-O((\log n)^{2C})]\), up to a logarithmic prefactor; it is eventually larger than \(\exp(-n^c)\). Thus that auxiliary claim cannot hold under the paper's stated probability convention. A theorem with arbitrary confidence \(\delta\) needs a fresh concentration calculation. Merely replacing the unspecified exponent by a symbol does not repair this mismatch.

7. **Further proof cautions.** Appendix A.4 reasons from distinct formal expressions to linear independence of their evaluations. Distinct activation-derived expressions need not be linearly independent: for example, \(\tanh'(z)=1-\tanh^2(z)\). A rank-revealing treatment is needed before claiming every new Gaussian innovation has positive variance. Appendix B.29 differentiates an inequality between norms repeatedly to control a high derivative of a maximum. Such differentiation is not justified by a first-derivative inequality; the maximum need not even be repeatedly differentiable, and direct higher differentiation of the actual trajectory introduces residual derivatives. A valid iterated-integral majorant may be possible, but it is not written there. In Appendix C, the odd-order improvement at order \(q+1\) uses a bound at order \(q+2\); when invoking only the stated bounds through \(s+1\), a safe regularity budget is \(s\ge q+1\). The source's examples discuss \(q=3\), despite the theorem's even-order assumption; those examples do not extend the stated theorem.

8. **Growing order.** The expression count, derivatives through order \(2s+1\), input lower singular values through the same order, and union bounds all change with \(s\). Choosing \(q=q(n)\) or \(q\) from an accuracy formula requires quantitative control of these changes. The informal source calculation \(q>\log(1/\varepsilon)/\log(\sqrt n/T)\) suppresses them. At fixed \(m,d,L\), one may discuss each fixed admissible order separately; this is not a uniform theorem over growing order.

Conclusion within this audit's scope: the literal published theorem has a straightforward finite-sample storage corollary, including (3) and (4), but it does not supply the requested fully quantified joint dependence. Equations (7)–(10) are a complete conditional order-two theorem. A fully explicit Gaussian-network result would still need justified bounds for \(B_3,B_4,R\), with their \((m,d,L,\phi,\delta,T)\) dependence and a compatible horizon. This note makes no claim about the actual dense-versus-dense variability scale or feature-learning behavior.
