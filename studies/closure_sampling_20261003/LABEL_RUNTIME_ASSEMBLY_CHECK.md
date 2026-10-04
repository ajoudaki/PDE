# Post-exchange check of the rescaled label and separated runtime constants

2026-10-04. Scoped post-exchange coupling check. The label derivation was
frozen before the runtime separation route was supplied. This note checks
the new runtime substitution and its compatibility with that label proof;
it is not an independent review of its author's own label derivation or a
promotion review of the inherited compression theorem. No experiments,
Git operations, manuscript changes, or source-file edits were made.

**Verdict: the two routes combine under
\(Y/\lambda\le\beta^{-60L}\).** They yield the claimed all-time error
coefficient \(\beta^{122L}\) with the capped gap, and
\(\beta^{124L}\) after conversion to the unnormalized gap. A simple
uncapped sufficient label restriction is
\(Y\le(\gamma/m)\beta^{-62L}\). No new dimension or sample-count
coefficient occurs in that restriction.

The complete new inputs read were:

| File | SHA-256 |
| --- | --- |
| `DEPTH_CONSTANT_SEPARATION.md` | `6e23f2eb95b1979e7be722f76bafb43ee239f83cc5175d58d17a0f9e73fcb17f` |
| `EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md` | `775ed6756af7de018c961173b850ad69930a71e4273c669bfe71c93182987bcd` |
| `STORAGE_QUADRATIC_IMPROVEMENT.md` | `ec18f54a3e3977bf9c99ce5c26066f48688848f8b5a9c142b75424badeb025e2` |

The frozen label source is `LABEL_DEPTH_RESCALING_ROUTE.md`, hash
`d06ceea6598bf3f86e0843682c5600365ef01b4b80eaad6544ceec1a9d4ec1f1`.
Its previously read mathematical and process instructions remain in force.

## 1. Common normalization and the actual initialized mixer cap

Retain the canonical physical mean-loss flow, zero readout, bounded-strip
activation class, and fixed \(L\ge2,d,m\ge1\). Set
\[
B=\max(1,B_\phi),\quad
\beta=\max(10,B,4B/a,32B/a^2,16/a),\quad
\lambda=\min(1,\gamma/m),\quad Y=\|y\|_2/\sqrt m.
\]
These are exactly the label route's constants: its additional maxima with
one in the definitions of its derivative bounds do not change \(\beta\).
The runtime activation norm
\(B_{\rm rt}=\max(1,B_\phi,2B_\phi/a,8B_\phi/a^2)\)
is at most \(\beta\).

In the source construction, each source basis \(U_\ell\) has columns
orthonormal in the dense empirical norm. Its selected restriction
\(P_\ell=U_{\ell,I_\ell}\) satisfies
\(P_\ell^\top H_\ell P_\ell=I\). Thus both maps from source
coefficient space to the corresponding dense or selected neuron space
are isometries. The stored initialized mixer is
\[
B_0^{(\ell)}
=P_\ell\frac{U_\ell^\top W_0^{(\ell)}U_{\ell-1}}n
                 P_{\ell-1}^\top H_{\ell-1}.
\]
The selected restriction adjoint is a contraction, as is the dense source
projection. Consequently
\[
\|B_0^{(\ell)}\|_{H_{\ell-1}\to H_\ell}
                         \le\|W_0^{(\ell)}\|_{\rm op}\le8.
\tag{1}
\]
There is no factor two from the metric comparison in this inequality.
The factor two for pointwise diagonal gates remains separately present
in the runtime choices \(g=h=2B_{\rm rt}\). Therefore the runtime
mixer tube \(R=9\) is justified for both dense and compressed mixers.

The source-approximation and carrier coefficient remains
\[
K=8+4K_{\rm src}\le\beta^{5L},\qquad
M\le1+16K_{\rm src}(Y/\lambda)\sqrt{\ell_n}
 \le1+4K(Y/\lambda)\sqrt{\ell_n},\quad \ell_n=\log(en).
\tag{2}
\]
It is harmless that the initialized operator also obeys the weaker bound
\(K\); the layer-propagation recurrences need only the stronger (1).
The actual-activity wording in the original runtime interface is not
used: (2) is the directly supplied allowance-based estimate.

## 2. Reconstruction of the runtime envelope

All occurrences of \(R\) in the explicit runtime proof are initialized
plus moving mixer tube bounds, forward propagation by the compressed
mixer, backward propagation by its metric adjoint, or bounds on the dense
reference's actual mixer. None bounds a coordinate approximation error or
the carrier maximum. The latter continue to use \(K\) and \(M\).
The selected reference mixer used for comparison is handled through its
forward/reverse action defects, not by silently asserting its norm is nine.

Writing \(b_\ell=g^{L-\ell+1}9^{L-\ell}\) and
\(b=\max b_\ell\), the first recurrence has
\(9g\le18\beta\le\beta^3\) and \(b\le\beta^{3L}\).
The sums and affine forward recurrence give
\(U\le\beta^{5L}\), \(F\le\beta^{6L}\). I substituted these
and \(K\le\beta^{5L}\) into every subsequent finite definition.
The separation route's table passes. In particular:
\[
D_\delta\le\beta^{6L},\quad W\le\beta^{7L},\quad
J_0\le\beta^{8L},\quad P_h,P_\delta\le\beta^{11L},\quad
D_r\le\beta^{12L},
\]
\[
A_0\le\beta^{18L},\quad C_f\le\beta^{25L},\quad
H_0\le\beta^{33L},\quad Z_0\le\beta^{30L},\quad
J_1\le\beta^{39L},\quad D_0^{\rm rt}\le\beta^{19L}.
\tag{3}
\]
The superscript on \(D_0^{\rm rt}\) distinguishes the runtime Gram
defect coefficient from the label proof's singleton-shift constant.
For example, the leading terms in these substitutions are
\(A_0\le29\beta^{17L}\),
\(H_0\le7\beta^{32L}\), and
\(Z_0\le3L\beta^{28L}\). The expression for \(J_1\) is dominated
by \(\sqrt L\,h b H_0\); the expression for \(D_0^{\rm rt}\) is
at most \(14L\beta^{17L}\). All fit (3) for \(\beta\ge10,L\ge2\).

The remaining definitions then give
\[
F_0\le38\beta^{47L}\le\beta^{48L},\quad
G^{\rm rt}\le12\beta^{48L}\le\beta^{49L},
\]
\[
C_1\le\beta^{57L},\quad C_2\le\beta^{55L},\quad
O_0\le\beta^{35L},\quad W_1\le\beta^{17L},\quad
T_1\le\beta^{19L}.
\tag{4}
\]
For the last two, the displayed formulas give
\(W_1\le84\beta^{16L}\) and
\(T_1\le9\beta^{17L+1}\). Those inequalities also hold at the
smallest allowed \(\beta=10,L=2\).

Let \(s_{\rm rt}=Y/\lambda\), the quantity called \(s\) in the
runtime proof. This differs from the activation-slope bound called
\(s\) in the source proof. The real fitting and geometric-comparison
conditions are exactly
\[
224FU s_{\rm rt}^2\le1,\qquad6J_0s_{\rm rt}\le1.
\tag{5}
\]
The hidden displacement is then at most \(1/4\), so it improves the
stopped mixer norm to at most \(8+1/4<9\). The normalized Gram margin
also strictly improves, as in the original explicit runtime calculation.
Thus the smaller tube is not assumed beyond its first-exit argument.

Put \(Q_{\rm rt}=\beta^{60L}\). Equations (3)--(4) show that
\(Q_{\rm rt}\) bounds
\(C_1,C_2,O_0,T_1,6J_0,\sqrt{224FU}\).
For \(s_{\rm rt}\le c=Q_{\rm rt}^{-1}\), (5) holds and
\(C_1c+C_2^2c^4\le2\). The exact completed-square bound in the
runtime proof gives
\[
C_{\rm err}
=O_0[1+\sqrt e(C_1+C_2c)e^{C_1c+C_2^2c^4}]+8T_1
\le40Q_{\rm rt}^2\le\beta^{122L}.
\tag{6}
\]
The last inequality uses \(40\le\beta^{2L}\). The source horizon
\(32\lambda^{-1}\ell_n\) is longer than the horizon needed in the
runtime calculation. Both endpoint tails are at most
\(4T_1Y\lambda^{-3/2}e^{-\lambda t/4}\), so their all-time
contribution is included in (6). No coefficient in (3)--(6) has been
discarded into a width threshold.

## 3. Coupling with the rescaled source proof

The frozen label route evaluates explicit \(\eta,\mathcal B,S_*\)
and proves
\[
c_{L,\phi}^{\rm src}
 =\min((8\sqrt{C_*})^{-1},S_*/16)\ge\beta^{-32L}.
\]
Therefore \(Y/\lambda\le\beta^{-60L}\) implies all its physical,
variational, endpoint-series, activity-modulus, and asymmetric query-trace
conditions. Its source allowance is \(S=16Y/\lambda\); the factor
sixteen was already included in the evaluated coefficient above.

The budget exponent \(\eta\), empirical budget \(\mathcal B\),
cutoff, and all corresponding stops are proof parameters. Neither the
canonical dense vector field nor the compressed autonomous state equations
contain them. The compressed state remains the moving hidden matrices,
raw readout, and its own residual, with the same algebraic readout
correction and fixed neuron metrics. The proof uses no externally supplied
residual or reference trajectory at runtime.

The rescaling changes higher carrier-moment bounds and the conditions
needed to sum traces. Once those conditions hold, the forward and angular
endpoint norms, the trace values \(T_Q,T_J\), the Gaussian-grid maximum
coefficient \(K_{\rm src}\), and the source-radius coefficient are the
same finite expressions as before. Consequently the source count remains
\[
R\le\beta^{50Ld}(d+3)^{3d/2}
              \lambda^{-1}\ell_n^{3d/2+1}.
\tag{7}
\]
The rescaled singleton shift is a fixed finite multiple of \(S\), and
its ratio to \(S\sqrt{\ell_n}\) tends to zero. Absorbing that ratio
into the eventual width does not suppress a nonvanishing radius or runtime
coefficient. The complex correction similarly has vanishing Gaussian
radius. Fixed positive \(Y\) permits the already required condition
\(n^{-1}\le Y\) eventually.

Combining (6)--(7) with the source event therefore proves
\[
Y/\lambda\le\beta^{-60L}
\quad\Longrightarrow\quad
\sup_{t\in[0,\infty],\ \|x\|=\sqrt d}|f_C(t,x)-f_n(t,x)|
\le\beta^{122L}\frac{Y}{\lambda^{3/2}\sqrt n}.
\tag{8}
\]
This includes \(d=1\), where (7) already accounts for both time-only
queries \(v=+1,-1\).

## 4. Conversion to the unnormalized gap and scope

The initialized covariance trace implies \(\gamma\le B^2\), so
\[
\lambda\ge\gamma/(mB^2),\qquad
\lambda^{-3/2}\le B^3(m/\gamma)^{3/2}.
\]
If \(Y\le(\gamma/m)\beta^{-62L}\), then
\[
Y/\lambda\le B^2\beta^{-62L}
 \le\beta^{2-62L}\le\beta^{-60L}.
\]
Likewise, \(\beta^{122L}B^3\le\beta^{124L}\), since \(L\ge2\).
Thus the uncapped sufficient condition and error are exactly
\[
Y\le(\gamma/m)\beta^{-62L},\qquad
\sup_{t,x}|f_C-f_n|
\le\beta^{124L}Y(m/\gamma)^{3/2}/\sqrt n.
\tag{9}
\]
The source size and total retained-coordinate count can retain the
previous explicit envelopes. This check establishes compatibility of the
two new routes and reconstructs the runtime constants; it does not replace
the separate independent check of the rescaled source proof or the inherited
full insertion and autonomous-compression proofs. Fixed architecture and
data precede the width limit, the width threshold is still unquantified,
and preprocessing and precision retain their existing qualifications.
The zero-label case is stationary and separate.
