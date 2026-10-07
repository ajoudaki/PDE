# A short causal program for the actual nonlinear dense flow

2026-10-06. Author proof with a separate reconstruction and its requested
bookkeeping corrections; see
[SHORT_CAUSAL_TRAINING_PROGRAM_CHECK.md](SHORT_CAUSAL_TRAINING_PROGRAM_CHECK.md).
This is a
reduction within the unseen-query study, not a compact decoder theorem.

On the inherited good event, the actual dense flow can be approximated,
uniformly through its fitted endpoint and on the sphere, to any fixed
inverse-polynomial accuracy by a causal program using at most

\[
 C[\log(en)]^8
\]

calls to its initialized Gaussian matrices and their transposes. Between
calls it uses coordinatewise functions, scalar empirical inner products,
and linear combinations of previously obtained vectors. All scalar
instructions and all low-rank descriptions have size bounded by another
absolute power of \(\log(en)\). The constants and sufficient width depend
on the fixed problem; the exponent does not depend on depth or dimension.

The vector instructions still act on width-\(n\) vectors. In particular,
this does **not** remove the initialized matrices, compress the Gaussian
roots, or establish an autonomous compact replacement. It supplies a
finite causal chronology to which such a replacement theorem could apply.

## 1. Setup and supplied estimates

Use the network, loss, and mobilities in Section 1 of
[RECOMPUTATION_SPACE.md](RECOMPUTATION_SPACE.md). Thus \(v=x/\sqrt d\),
\(\|v\|=1\), the first matrix is \(A\), hidden matrices are \(W^\ell\),
and the readout is \(w\). Their initialized values are \(A_0,W_0^\ell,0\).
Let \(Y=\|y\|_2/\sqrt m>0\). Constants in this note may depend on all
fixed admissible data, activations, depth, label allowance, and Gram gap.
They do not depend on \(n\). The case \(Y=0\) has identically zero output.

We use the inherited good-event estimates from
`GENERAL_DENSE_COMPARISON.md`, `UNBOUNDED_COMPRESSOR_BRIDGE.md`, and
`ANALYTIC_TAIL_EXTENSION.md` in the
authorized integrated study. They include fixed real operator/RMS bounds,
exponential residual decay, a \(C\sqrt{\log(en)}\) coordinate bound for
training backward carriers, and exponential decay of the output derivative
uniformly on the sphere. They also supply a complex-time neighborhood of
every real time through \(T=C\log(en)\), of radius
\(c/\sqrt{\log(en)}\), on which the forward/backward RMS bounds hold.
The analytic-tail extension permits the fixed factor in \(T\) to depend
on the requested inverse-polynomial accuracy, at its inherited eventual
width thresholds. The complete relevant sources were read; these are internally checked
inputs, not newly promoted book results.

Write the state as the **learned displacement**

\[
 u=(A-A_0,W^2-W_0^2,\ldots,W^L-W_0^L,w),
\]

with norm

\[
 \|u\|=\frac{\|A-A_0\|_F}{\sqrt n}
       +\sum_{\ell=2}^L\|W^\ell-W_0^\ell\|_F
       +\frac{\|w\|_2}{\sqrt n}.                         \tag{1}
\]

The actual displacement is bounded in this norm by a fixed constant.
Indeed, each hidden gradient is a sum of
\(-2r_a\delta_a^\ell h_a^{\ell-1\,T}/(mn)\), and

\[
 \|\delta h^T/n\|_F
       =(\|\delta\|_2/\sqrt n)(\|h\|_2/\sqrt n).
\]

The other two blocks have the same normalized bound. Fixed forward and
backward RMS bounds and the integrability of \(\|r(t)\|_2/\sqrt m\)
prove the assertion. It also proves a fixed norm bound for the time
derivative on the inherited complex neighborhoods: the displayed gradient
formulas hold holomorphically, and the complex RMS/residual bounds apply.

## 2. A controlled vector field without a full matrix function

Choose fixed radii strictly above these actual displacement bounds. In
each evaluation project the blocks of \(u\) onto their respective
Frobenius or Euclidean balls, with the normalizations in (1). For a block
\(D\), its projection is simply

\[
 D\longmapsto D\min\{1,B/\|D\|_F\},                    \tag{2}
\]

where the fraction is ignored at zero and the appropriate radius includes
\(\sqrt n\) for the first/readout blocks. These maps are nonexpansive in
the corresponding Hilbert norm. A direct proof is the nearest-ball
projection inequality
\(\langle D-PD,V-PD\rangle\le0\) for every \(V\) in the ball;
adding the inequalities for two inputs gives
\(\|PD-PE\|^2\le\langle PD-PE,D-E\rangle\).

Use \(A_0\) and \(W_0^\ell\) plus these projected displacements in the
forward pass. Clip training backward carriers coordinatewise at
\(M=C\sqrt{\log(en)}\) **before** multiplying by activation derivatives:
\(\widehat\delta^L=\phi_L'(z^L)\odot\operatorname{clip}_M(w)\) and
\(\widehat\delta^\ell=\phi_\ell'(z^\ell)\odot
\operatorname{clip}_M((W^{\ell+1})^T\widehat\delta^{\ell+1})\), with
the projected parameters understood. Clip residuals to a fixed interval containing
the actual residuals. Substitute these fields in the exact gradient
formulas. Denote this autonomous extension by \(F(u)\).

The initialized matrices are held fixed in this construction. On their
inherited operator-norm event, the projected matrices have fixed operator
bounds: a displacement's operator norm is at most its bounded Frobenius
norm. The first matrix has a fixed \(\|A\|_F/\sqrt n\) bound. Consequently

\[
 \|F(u)\|\le C,\qquad
 \|F(u)-F(\widetilde u)\|
       \le C\sqrt{\log(en)}\|u-\widetilde u\|.           \tag{3}
\]

Here is the width accounting in the second estimate. Forward subtraction
costs \(C\|u-\widetilde u\|\) in every feature RMS norm. In a backward
gate difference the multiplying clipped carrier is bounded coordinatewise
by \(C\sqrt{\log(en)}\); bounded second activation derivatives therefore
give this factor once. Carrier subtraction costs the previous backward
RMS difference plus the parameter difference times a bounded RMS norm.
Induction down the fixed number of layers adds these gate contributions;
it does not multiply a new carrier maximum at each layer. Residual and
rank-one gradient subtraction then give (3). This is the argument of
Section 2 of the recomputation note, now with the nonexpansive projections
of the displacement instead of spectral projections of the full matrices.

No projection or clipping changes the actual good trajectory, so it solves
\(\dot u=F(u), u(0)=0\). The projected-parameter predictor has

\[
 \sup_{\|v\|=1}|f(u,v)-f(\widetilde u,v)|
                         \le C\|u-\widetilde u\|.        \tag{4}
\]

Only real first derivatives and fixed operator/RMS bounds are needed for
(4). There is no query-specific event or spatial discretization.

If bounded scalar node ranges are needed later, training preactivations
can additionally be clipped at their inherited good-event coordinate cap
before applying the activation and its derivative. Coordinate clipping is
nonexpansive and decreases norm, so (3) remains valid, and the actual flow
is unchanged. This optional version is not a proof that every raw matrix
answer in the program has a polylogarithmic coordinate bound.

## 3. Elementary interpolation facts with a positive endpoint rule

For an integer \(K\ge2\), take nodes
\(s_j=(1+\cos\theta_j)/2\),
\(\theta_j=(2j+1)\pi/(2K)\), \(0\le j<K\), on \([0,1]\).
Let \(I_K\) be degree-\(K-1\) interpolation at these nodes.
Discrete cosine orthogonality gives its Chebyshev coefficients

\[
 a_0=K^{-1}\sum_j b_j,\qquad
 a_k=2K^{-1}\sum_j b_j\cos(k\theta_j)\quad(1\le k<K)
\]

for vector data \(b_j\). Since \(|T_k|\le1\) on \([-1,1]\),

\[
 \sup_{0\le s\le1}\|I_K b(s)\|
                       \le(2K-1)\max_j\|b_j\|.          \tag{5}
\]

We use this elementary bound, not a sharper logarithmic Lebesgue estimate.
The endpoint integral has positive weights:

\[
 \int_0^1 I_K b(s)\,ds=\sum_j\omega_j b_j,\qquad
 \omega_j=\frac1K\left[1-2\sum_{k=1}^{\lfloor(K-1)/2\rfloor}
               \frac{\cos(2k\theta_j)}{4k^2-1}\right].   \tag{6}
\]

The cosine orthogonality and
\(\int_0^1T_{2k}(2s-1)ds=1/(1-4k^2)\) prove the formula.
The identity
\(\sum_{k=1}^r2/(4k^2-1)=1-1/(2r+1)<1\)
proves \(\omega_j>0\); exactness for the constant polynomial gives
\(\sum_j\omega_j=1\). The positivity is important: it avoids multiplying
the global time-stability exponent by the interpolation norm in (5).

Suppose a vector function extends holomorphically to the complex disk of
radius twice the interval length about its midpoint, with norm bounded by
\(C\). Taylor truncation and the geometric-series bound give a polynomial
of degree \(K-1\) with real-interval error at most \(C2^{-K}\), after
enlarging \(C\). Interpolating that error and using (5) gives

\[
 \sup\|b-I_Kb\|\le CK2^{-K}.                            \tag{7}
\]

These arguments apply to the finite-dimensional block norm (1); no
dimension-dependent constant is introduced.

## 4. A causal collocation calculation

For clarity put \(\lambda=C\sqrt{\log(en)}\), a supplied upper bound in
(3), and choose

\[
 K=\lceil[\log(en)]^2\rceil+2,\qquad J=K,
 \qquad h=\frac1{16\lambda K}.                           \tag{8}
\]

Use consecutive patches of this length to reach \(T=C\log(en)\); the
last may be shorter. Increase the fixed constant in \(\lambda\), if
necessary, so a disk of twice every patch length fits in the inherited
complex-time neighborhood. There are
\(H\le C[\log(en)]^{7/2}\) patches.

On a patch beginning at \(t_0\), with numerical starting value \(b\),
define the finite-node Picard map

\[
 (\mathcal P U)_j
   =b+\int_{t_0}^{t_0+hs_j}
          I_K\bigl(F(U_0),\ldots,F(U_{K-1})\bigr)(s)\,ds. \tag{9}
\]

The interpolation in (9) is affinely rescaled to the physical patch.
In the maximum node norm, (3), (5), and (8) give contraction factor
at most \(\lambda h(2K-1)\le1/8\). Starting from \(U_j=b\), perform
\(J\) explicit iterations. The last node array gives the polynomial
patch path by the right side of (9), now evaluated at any patch time,
and the committed endpoint by (6). This is an ordinary finite causal
computation: a complete iteration uses only the previous iteration's
node arrays. There is no simultaneous-equation oracle.

We spell out global error propagation because a crude patchwise
contraction estimate alone gives the wrong exponential. Let \(e\) be
the starting-value error, and let \(V_j=u(t_0+hs_j)\) be the actual
nodes. Along the actual solution \(F(u(t))=\dot u(t)\), and this time
function is holomorphic and bounded on the supplied neighborhood even
though the extended field \(F\) need not be analytic off the trajectory.
Equation (7) therefore bounds its interpolation defect by
\(\eta=CK2^{-K}\). Comparing the fixed point \(U^*\) of (9) with
\(V\) gives

\[
 \max_j\|U_j^*-V_j\|\le2(e+h\eta).                     \tag{10}
\]

Boundedness of \(F\) gives
\(\|U^*-(b,\ldots,b)\|_{\max}\le ChK\).
Thus the actual \(J\)-th iterate is within
\(\zeta=ChK8^{-J}\) of \(U^*\). At the endpoint, use the positive
rule (6), not the norm (5). The new error obeys

\[
 e_{\rm new}
 \le(1+2h\lambda)e
       +h\eta(1+2h\lambda)+h\lambda\zeta.               \tag{11}
\]

Starting from zero error and iterating (11) yields

\[
 \max_{\rm endpoints}e
 \le CT\exp(2\lambda T)(\eta+\lambda\zeta).             \tag{12}
\]

At an interior time the integrated interpolation norm (5), (10), and
the iterate error give the same bound up to a fixed factor, since
\(h\lambda(2K-1)\le1/8\). As
\(\lambda T=O([\log(en)]^{3/2})\) and \(K,J\) grow as
\([\log(en)]^2\), (12) is smaller than \(n^{-a}\) for every fixed
\(a>0\), at every sufficiently large individual width. Constants may
depend on \(a\). Use (4) to transfer the estimate to all sphere queries.

Finally choose the fixed factor in \(T\) so the inherited output tail
after \(T\) is at most \(n^{-a}\). Retain the numerical endpoint as
the approximating parameter state for \(t\ge T\), including infinity.
This proves time-uniform numerical approximation of the actual model.
It is not a claim that the finite program itself exactly fits the labels.

## 5. Gaussian calls and scalar instructions

Every evaluation of \(F\) uses \(O(mL)\) initialized matrix calls and
transposed calls. The learned matrix action needs none: every Picard
increment and every committed endpoint is a linear combination of
previous rank-one gradients. A displacement can be represented as

\[
 D=\sum_{r=1}^p c_r a_r b_r^T/n,
 \qquad
 \|D\|_F^2=\sum_{r,s}c_rc_s
          \frac{a_r^Ta_s}{n}\frac{b_r^Tb_s}{n}.           \tag{13}
\]

Thus (2), its action on a new vector, and the corresponding transpose
use only source inner products and scalar combinations. First-layer
increments use the fixed training inputs instead of the right vectors
in (13); readout increments are vector sums. Their norms have the same
scalar implementation.

There are \(HK(J+1)\) field evaluations, including the final evaluation
of the right sides defining the patch path. Within a patch, the current
state consists of the committed starting displacement plus the previous
iteration's \(K\) rank-one right sides. It does not recursively expand
into \(K^J\) distinct stored terms. At a committed endpoint the
\(K\) new right sides are appended. All vector arrays ever generated
number \(O(mLHK(J+1))\), whether retained or recomputed. All pairwise
inner products of these arrays therefore require at most their squared
count; evaluating the combinations in (13) adds another fixed
polynomial number of scalar instructions. We need no exponent depending
on \(d,m,L\) in these counts.

In particular,

\[
 \#\{\text{initialized Gaussian matrix calls}\}
    \le C HK(J+1)\le C[\log(en)]^{15/2}
    \le C[\log(en)]^8.                                  \tag{14}
\]

The first initialized matrix has \(d\) columns; its row roots and the
fixed training/query coordinates can be included as the ordinary
initial row inputs of the program. The constants in the count include
the fixed input dimension. A late query adds \(O(L)\) forward calls
and polynomially many scalar contractions with the learned factors.
Uniform numerical accuracy already follows from (4), with no stored
spatial net.

Equations (9), (13), and the explicit projections describe the exact-real
program. A finite-bit implementation still needs activation and input
precision interfaces. No total bit-complexity or initialization-free
evaluation theorem is asserted here; those interfaces are discussed in
the separate numerical notes.

## 6. What this resolves, and what it does not

The finite growing chronology is no longer an assumed consequence of
time analyticity. It has an explicit stable causal construction retaining
the actual nonlinear forward and backward updates. Its quadrature error
uses analyticity only on the true trajectory, so no width-uniform bounds
on high Frechet derivatives of the clipped field are needed. The use of
learned-displacement projection removes the full matrix-function obstacle.

Three distinct steps remain before the requested result follows:

1. Replace the width-\(n\) initialized matrix actions and source vectors
   by a genuinely compact autonomous state, not a saved future transcript.
2. Prove that this replacement preserves passive unseen-query statistics
   uniformly, including nearly dependent training histories, at the dense
   variability scale. A uniform law over known scalar coefficients alone
   does not control inversely conditioned query regression coefficients.
3. Count all retained coefficients, numerical descriptions and peak live
   decoder workspace for that replacement.

The short program proves none of these steps by itself. No new assumption
on the original labels, training Gram gap, depth, or activation values is
used in its dense-flow approximation.
