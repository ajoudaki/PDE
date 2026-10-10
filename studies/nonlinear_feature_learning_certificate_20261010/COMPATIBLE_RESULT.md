# Strict nonlinear feature activity for compatible data

Date: 2026-10-10. Author-derived result with scoped independent checks of the
initialization and fixed-time arguments. This revision replaces an unjustified
population smoothness assertion by strong directional expansions.

## Headline

The obstruction in the original counterexample disappears under a precise
geometric compatibility condition. For the same fixed-depth Gaussian network
and gradient-flow scaling as the compression paper, assume

\[
 \left|\frac{x_a^\top x_b}{d}\right|<1\quad(a\ne b),       \tag{1}
\]

so no two training inputs are parallel or antiparallel. Assume also that every
activation is paper-admissible, analytic and nonaffine. Gaussian second
moments may be normalized to one, but this is not an additional hypothesis:
finite positive moments suffice, and follow from the activation assumptions.

Then, for every fixed nonzero label vector satisfying the paper's label
condition:

1. every initialized feature Gram is positive definite;
2. every hidden parameter block has a nonzero order-\(t^2\) displacement;
3. the joint training-feature vector in every hidden layer has a nonzero
   order-\(t^2\) displacement;
4. the dense prediction separates at order \(t^3\) from its frozen initial
   tangent-kernel prediction; and
5. every activation retains a positive best-affine-fit error on a common
   initial time interval.

The third conclusion is layerwise: at every layer, at least one—and generally
many—of the training representations move at leading order. Claiming that
every individual training input moves requires additional label assumptions.
For example, an orthogonal zero-labelled input can decouple from the labelled
subproblem.

## Precise statement

Use the network, Gaussian initialization, zero readout, squared loss and
mobilities of the compression paper, at any fixed hidden depth \(L\ge2\).
Write \(v_a=x_a/\sqrt d\). In addition to (1), suppose:

- \(y\ne0\), with its fixed norm satisfying the existing small-label bound;
- every \(\phi_\ell\) is analytic on the paper's strip, has bounded strip
  derivative, and is nonaffine.

There is a fixed \(t_*>0\), depending on the fixed problem but not on width,
such that the following hold as \(n\to\infty\).

For every hidden layer \(\ell\), there is \(c_\ell>0\) such that, for each
fixed \(0<t\le t_*\),

\[
 \Pr\!\left\{
 \frac1n\sum_{a=1}^m
 \|h_a^{(\ell)}(t)-h_a^{(\ell)}(0)\|_2^2
 \ge c_\ell t^4
 \right\}\longrightarrow1.                               \tag{2}
\]

Every hidden parameter block has the corresponding positive \(t^2\)
displacement in its mobility norm. Moreover, for some \(c>0\),

\[
 \Pr\!\left\{
 y^\top\{f_n(t)-f_{{\rm NTK},n}(t)\}\ge ct^3
 \right\}\longrightarrow1,                               \tag{3}
\]

where \(f_{{\rm NTK},n}\) is the same-initialization frozen initial tangent
kernel evaluated on the training set.

Finally, the population preactivation in every layer satisfies, after possibly
decreasing \(t_*\),

\[
 \min_{1\le a\le m}\ \inf_{0\le t\le t_*}
 \inf_{\alpha,\beta\in\mathbb R}
 \mathbb E\!\left[
  \{\phi_\ell(Z_a^{(\ell)}(t))
     -\alpha Z_a^{(\ell)}(t)-\beta\}^2
 \right]>0.                                               \tag{4}
\]

Thus the dynamics are both effectively nonlinear and feature-learning on this
initial interval. The constants need not be uniform as inputs approach
parallelism, an activation approaches an affine function, or the label norm
approaches zero.

## Proof

### 1. Every initialized forward Gram is positive

At the first layer, suppose a linear combination of the ridge functions

\[
 g\longmapsto\phi_1(g^\top v_a)
\]

vanishes. Differentiate in a direction having nonzero inner product with every
\(v_a\). Because \(\phi_1\) is nonaffine, its derivative is bounded,
continuous and nonconstant. Bounded ridge functions along pairwise
nonparallel directions are linearly independent: successive finite
differences can eliminate every direction except one, and a bounded function
with a vanishing sufficiently high finite difference must be constant. Hence
all coefficients in the original combination vanish. The first feature Gram
is therefore positive definite.

Inductively, suppose the preceding feature Gram is positive definite. The next
initialized preactivation tuple is then a Gaussian with full support in
\(\mathbb R^m\). If

\[
 \sum_a c_a\phi_\ell(z_a)=0
\]

almost surely, continuity and full support make it an identity for every
\(z\in\mathbb R^m\). Varying one coordinate at a time and using nonconstancy
of \(\phi_\ell\) gives \(c_a=0\) for every \(a\). Thus every initialized
feature Gram is positive definite. In particular the paper's top Gram gap
\(\gamma>0\) follows automatically.

With unit second-moment normalization every one-sample preactivation is
standard Gaussian. Without it these marginals remain nondegenerate Gaussians
with finite variances, which is all that is used below.

### 2. Every backward-response Gram is positive

This step uses only local notation. Let \(H_a^{(\ell)}\) and
\(Z_a^{(\ell)}\) denote one population neuron at initialization. Put

\[
 S=\sum_a y_aH_a^{(L)}.
\]

Apart from the common positive factor \(2/m\), the first time derivative of
the top backward response is

\[
 B_a^{(L)}=S\,\phi_L'(Z_a^{(L)}).                         \tag{5}
\]

Its Gram is positive definite. Indeed, if
\(\sum_a c_aB_a^{(L)}=0\), full Gaussian support turns this into

\[
 \left\{\sum_a y_a\phi_L(z_a)\right\}
 \left\{\sum_a c_a\phi_L'(z_a)\right\}=0
 \quad\text{for every }z\in\mathbb R^m.                  \tag{6}
\]

The first factor is not identically zero because the top feature Gram is
positive definite and \(y\ne0\). Analyticity then makes the second factor
identically zero. Since \(\phi_L'\) is nonconstant, varying one coordinate
forces every \(c_a=0\).

Move downward recursively:

\[
 B_a^{(\ell)}
 =\phi_\ell'(Z_a^{(\ell)})
   (W^{(\ell+1)}_0)^*B_a^{(\ell+1)}.                     \tag{7}
\]

The Gaussian action and its transpose in (7) are the same initialized matrix,
not independent replacements. Here is the conditioning calculation. At finite
width write \(W=W_0^{(\ell+1)}\), let the columns of \(H\) be its lower
training features, and let the columns of \(U\) be the upper response tuple.
Condition on the other weight blocks and on \(Z=WH\). The tuple \(U\) is
then known: its construction uses these forward outputs and higher matrices,
but not this matrix's transpose. With \(Q_n=H^\top H/n\),
\(C_n=Z^\top U/n\), \(D_n=U^\top U/n\), and \(P_H\) the orthogonal
projection onto the columns of \(H\), Gaussian conditioning gives

\[
 W^\top U\overset d=H Q_n^{-1}C_n+(I-P_H)\Xi D_n^{1/2},
\]

where \(\Xi\) has independent standard Gaussian entries, independent of the
conditioned information. Invertibility holds with probability tending to one
by the positive limiting forward Gram. The projected-away part has conditional
normalized squared norm at most \(m\operatorname{tr}(D_n)/n\), which tends
to zero. The finite initialization program's second-moment convergence
therefore gives a fresh population Gaussian term of covariance \(D=\lim D_n\),
independent of the lower initial tuple, plus a conditional mean in its forward
span. Consequently, for any nonzero
coefficient vector \(c\),

\[
 \mathbb E\!\left[
  \left\{\sum_a c_aB_a^{(\ell)}\right\}^2
  \,\middle|\, Z^{(\ell)}
 \right]
 \ge
 \lambda_{\min}(D)
 \sum_a c_a^2\{\phi_\ell'(Z_a^{(\ell)})\}^2.             \tag{8}
\]

An analytic nonconstant activation has a derivative that is nonzero almost
everywhere under a nondegenerate Gaussian. The right side of (8) is therefore
positive with positive probability. Downward induction proves that every
backward-response Gram

\[
 D^{(\ell)}_{ab}=\mathbb E[B_a^{(\ell)}B_b^{(\ell)}]
\]

is positive definite.

### 3. Every hidden parameter block moves

All hidden velocities vanish at zero readout. Their first nonzero terms are
their accelerations. With lower-case response arrays denoting the finite-width
versions of (5)--(7), the exact formulas are

\[
 \ddot W^{(1)}(0)
 =\frac4{m^2}\sum_a y_ab_a^{(1)}v_a^\top,               \tag{9}
\]

\[
 \ddot W^{(\ell)}(0)
 =\frac4{m^2n}\sum_a y_ab_a^{(\ell)}
                 h_a^{(\ell-1)}(0)^\top,
 \qquad 2\le\ell\le L.                                  \tag{10}
\]

The limiting squared mobility norms in (9)--(10) are positive multiples of

\[
 y^\top(G\circ D^{(1)})y,
 \qquad
 y^\top(Q^{(\ell-1)}\circ D^{(\ell)})y,                  \tag{11}
\]

where \(G_{ab}=v_a^\top v_b\), \(Q^{(\ell-1)}\) is the preceding feature
Gram, and \(\circ\) denotes entrywise multiplication.

For \(\ell\ge2\), both matrices in the entrywise product are positive
definite, so their product is positive definite. Although \(G\) itself may be
singular, write \(G=\sum_jq_jq_j^\top\). Since \(G_{aa}=1\),

\[
 G\circ D^{(1)}
 =\sum_j\operatorname{diag}(q_j)D^{(1)}
                  \operatorname{diag}(q_j)
 \succeq\lambda_{\min}(D^{(1)})I.                        \tag{12}
\]

Because \(y\ne0\), every expression in (11) is strictly positive. Thus every
hidden parameter block has a nonzero acceleration.

### 4. The features in every layer move

There is a short adjoint identity that avoids a layer-by-layer cancellation
argument. Let \(R_a^{(\ell)}=\ddot Z_a^{(\ell)}(0)\) and
\(A_a^{(\ell)}=\ddot H_a^{(\ell)}(0)\). Since all first hidden velocities
vanish,

\[
 A_a^{(\ell)}
 =\phi_\ell'(Z_a^{(\ell)})R_a^{(\ell)}.                  \tag{13}
\]

The preactivation acceleration is its learned-link contribution plus the
forward propagation of the preceding feature acceleration:

\[
 R_a^{(\ell)}
 =\ddot W^{(\ell)}(0)H_a^{(\ell-1)}
  +W_0^{(\ell)}A_a^{(\ell-1)},                           \tag{14}
\]

with the evident first-layer version.

Pair (14) with \(y_aB_a^{(\ell)}\), sum over the samples, and use the adjoint
in (7). The learned-link term is a positive multiple of
\(\|\ddot W^{(\ell)}(0)\|^2\). The propagated term becomes exactly the same
pairing one layer lower. Iteration gives

\[
 \sum_a y_a\,
 \mathbb E[B_a^{(\ell)}R_a^{(\ell)}]
 =
 \frac{m^2}{4}\sum_{j=1}^{\ell}
 \|\ddot W^{(j)}(0)\|_{\rm mob}^2>0,                    \tag{15}
\]

where the first-block mobility norm is the population mean-square row norm
and later block norms are Hilbert--Schmidt norms. At finite width the same
identity has pairing \(n^{-1}\sum_a y_ab_a^\top r_a\), first-block squared
norm \(\|\ddot W^{(1)}\|_F^2/n\), and later squared norms
\(\|\ddot W^{(j)}\|_F^2\). Substitution of (9)--(10) gives the common
factor \(m^2/4\) exactly.

Therefore the joint tuple \(R^{(\ell)}\) cannot vanish. Because
\(\phi_\ell'(Z_a^{(\ell)})\ne0\) almost surely, (13) shows that the joint
feature acceleration \(A^{(\ell)}\) also cannot vanish. This proves strict
feature movement in every layer without requiring that a particular sample
carry the motion.

### 5. Separation from the frozen initial tangent kernel

Use the paper's Euclidean mobility coordinates

\[
 \theta_{\rm hid}
 =(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)}).
\]

At every finite width, zero readout gives the exact identity

\[
 y^\top\{f_n(t)-f_{{\rm NTK},n}(t)\}
 =\frac m3\|\ddot\theta_{\rm hid}(0)\|_2^2t^3+o(t^3).
                                                               \tag{16}
\]

Section 3 proves that the squared coefficient converges to a strictly positive
fixed limit: in fact every summand from a hidden block has a positive limit.
Hence the nonlinear trajectory and the frozen-kernel trajectory separate in
the label direction.

### 6. The nonlinearity remains effective

At initialization each marginal \(Z_a^{(\ell)}\) is a nondegenerate Gaussian.
If

\[
 \inf_{\alpha,\beta}
 \mathbb E[
  \{\phi_\ell(Z_a^{(\ell)})-\alpha Z_a^{(\ell)}-\beta\}^2
 ]=0,
\]

then \(\phi_\ell\) agrees almost everywhere with an affine function. Gaussian
full support, continuity and analyticity would make it affine everywhere,
contrary to assumption. The best-affine-fit error is therefore positive at
initialization. Its value is

\[
 \operatorname{Var}(\phi_\ell(Z_a^{(\ell)}(t)))
 -\frac{\operatorname{Cov}(Z_a^{(\ell)}(t),
                          \phi_\ell(Z_a^{(\ell)}(t)))^2}
        {\operatorname{Var}(Z_a^{(\ell)}(t))}.
\]

Mean-square continuity and the Lipschitz bound make every moment continuous;
the denominator remains positive near zero. Taking a common interval over
the finitely many samples and layers proves (4).

### 7. From coefficients to a fixed positive time

The maintained local fixed-depth population theorem applies here: strip
analyticity and bounded strip derivative give the required real
\(C^{1,1}\) bounds, and all initialization variances and mobilities are
positive. It supplies one width-independent interval on which the dense
hidden-path laws and predictions converge uniformly to the strong population
flow. The frozen initial kernel converges on the same interval by ordinary
finite-dimensional Gram convergence.

No Fréchet smoothness of a nonlinear map on \(L^2\) is assumed. The needed
directional rule is elementary: if \(X_s\to X_0\) in probability,
\(U_s\to U_0\) in \(L^2\), and \(g\) is bounded continuous, then
\(g(X_s)U_s\to g(X_0)U_0\) in \(L^2\). Subtract the varying \(U_s\)
term using the multiplier bound; for the other term truncate the fixed
integrable variable \(|U_0|^2\), apply bounded convergence in probability,
and remove the truncation. The integral mean-value formula applies this rule
to the bounded derivative \(\phi_\ell'\).

The readout integral equation first gives \(w(t)/t\to(2/m)S\) strongly.
The backward recursion then gives
\(\delta_a^{(\ell)}(t)/t\to(2/m)B_a^{(\ell)}\) strongly, since learned
actions converge in operator norm and activation gates obey the multiplier
rule. Insert these limits into the parameter integral equations. Their
finitely many rank-one terms converge in Hilbert--Schmidt norm, giving
\(W^{(\ell)}(t)-W_0^{(\ell)}=t^2\ddot W^{(\ell)}(0)/2+o(t^2)\)
in the respective mobility spaces. Forward recursion and the directional
chain rule give
\(H_a^{(\ell)}(t)-H_a^{(\ell)}(0)=t^2 A_a^{(\ell)}/2+o_{L^2}(t^2)\).
Consequently the population feature displacement is

\[
 \sum_a\mathbb E\bigl[
 |H_a^{(\ell)}(t)-H_a^{(\ell)}(0)|^2\bigr]
 =\frac{t^4}{4}\sum_a\mathbb E|A_a^{(\ell)}|^2+o(t^4),   \tag{17}
\]

with positive leading coefficient. To derive the output expansion without
exchanging width and finite-width Taylor remainders, put
\(E=\sum_\ell\|\ddot W^{(\ell)}(0)\|_{\rm mob}^2>0\) locally in this
paragraph, and write \(K(t)\) for the population tangent Gram, normalized so
that \(\dot f=-(2/m)K(t)(f-y)\). The strong response limits give

\[
 y^\top K_{\rm hidden}(t)y=\frac{m^2}{4}Et^2+o(t^2).
\]

The readout block is the top feature Gram. Its leading change, using (15), is
\(t^2\sum_a y_a\mathbb E[B_a^{(L)}R_a^{(L)}]
=(m^2/4)Et^2\). Both contributions are positive and equal. All entries of
\(K(t)-K(0)\) are \(O(t^2)\). Subtract the frozen-kernel equation and use
variation of constants:

\[
 f(t)-f_{\rm NTK}(t)
 =\frac2m\int_0^t e^{-2K(0)(t-s)/m}
       (K(s)-K(0))(y-f(s))\,ds.
\]

Since \(f(s)=O(s)\), replacing the propagator by the identity and \(y-f(s)\)
by \(y\) introduces only \(O(t^4)\). Thus

\[
 y^\top\{f(t)-f_{\rm NTK}(t)\}
 =\frac m3 E t^3+o(t^3).                                 \tag{18}
\]

Choosing \(t_*>0\) small enough makes the displayed
leading terms dominate their remainders. Uniform path-law and prediction
convergence then transfer these strict inequalities to finite width with
probability tending to one, proving (2)--(3).

For hidden-parameter displacement, use its integral-update identity rather
than infer Hilbert--Schmidt convergence from operator convergence. For
\(\ell\ge2\), exactly at finite width,

\[
\begin{aligned}
 \|W^{(\ell)}(t)-W^{(\ell)}(0)\|_F^2
 =\frac4{m^2}\sum_{a,b}\int_0^t\!\int_0^t
 &r_a(s)r_b(u)
 \frac{\delta_a^{(\ell)}(s)^\top\delta_b^{(\ell)}(u)}n\\
 &\times\frac{h_a^{(\ell-1)}(s)^\top h_b^{(\ell-1)}(u)}n\,ds\,du.
\end{aligned}
\]

The first-block identity replaces the last feature contraction by
\(v_a^\top v_b\) and normalizes its squared Frobenius norm by \(n\).
The local theorem gives convergence of these same-layer contractions at
each pair of times. Its common RMS/operator bounds dominate the integrands
on an event of probability tending to one; truncate off that event and apply
bounded convergence to their expected absolute differences, then integrate.
This proves convergence of the displacement norms to their population values.
The positive population acceleration in every block and the strong expansion
above give the claimed nonvanishing \(t^2\) displacements.

The local population input used here is Theorem C.1 of the maintained
`docs/03-local-population.qmd`, including its finite-GF consequence: for fixed
finite data, fixed depth, Gaussian initialization, positive variances and
mobilities, and bounded Lipschitz activation derivatives, there is a positive
width-independent interval of strong population evolution and convergence in
probability of predictions, same-layer path laws in Wasserstein-2, and the
correctly typed response contractions. Our \(\omega_a=1/m\), unit mobility
multipliers, Gaussian first-layer roots, and zero readout meet its hypotheses;
bounded strip derivative gives its real \(C^{1,1}\) regularity by Cauchy's
formula. The finite initialized forward/transpose program uses the established
Gaussian conditioning rules in `docs/02-gaussian-reuse.qmd`. These are explicit
maintained-book dependencies of this research proof, not additional assumptions
on the compression model.

## Boundary of the result

Pairwise nonparallel inputs are a clean sufficient compatibility rule, not a
necessary one. Parallel or antiparallel inputs can instead be quotiented by
the exact parity imposed by the architecture, but that produces a
case-dependent statement.

The normalization \(\mathbb E\phi(G)^2=1\) controls scale but does not by
itself prove activity. Nonaffinity supplies nonzero derivatives and response
rank; geometric compatibility supplies ridge-function independence.

The theorem proves layerwise activity of the joint training representation.
To claim that every individual sample moves, it is sufficient in the
two-hidden-layer result to assume every label is nonzero. The corresponding
samplewise arbitrary-depth strengthening is not used here and is not claimed.
