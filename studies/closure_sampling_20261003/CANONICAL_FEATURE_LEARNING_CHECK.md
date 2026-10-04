# Independent reconstruction of canonical hidden-feature motion

2026-10-03. Scoped collaborator check. This is an internal mathematical check,
not an isolated promotion review. The assigned source was read completely,
all 206 lines:

- `CANONICAL_FEATURE_LEARNING.md`, SHA-256
  `c031de6bfe6fd9b926c8886ae145f164ebc587e9b8d4ba4ed34e53f2e432a0b9`.

The permitted companion was my own complete complex-activity route, current
SHA-256 `3190cbcef13c3089b2a475c297e9333e98ce3c01f69a686bde217cf87f193fe4`.
The present dense-motion proof does not require its complex continuation
result. The manuscript's canonical model had already been read in the scoped
route. No other study inputs, experiments, or Git operations were used. The
canonical-notation/neural reference, rigorous-proof, and adversarial-audit
instructions were applied.

**Verdict:** the canonical dense claims check: both hidden training-feature
RMS displacements are at least \(cs^2\) on one fixed activity interval,
and at least \(cy^2\) at the small-label fitted endpoint, outside an
exponentially small initialization event. The source's compression transfer
is a correct conditional implication of its stated pairing and trajectory
guarantees. Those guarantees themselves are not independently verified here:
`CANONICAL_NEURON_COMPRESSION.md` was outside the assigned scientific inputs
and was not read. No flaw was found in the dense argument.

## 1. Setup and initialized probability event

On the single training input, put
\[
 h=\tanh a,\quad z=Wh,\quad g=\tanh z,
 \quad\delta=w\odot\operatorname{sech}^2z,
 \quad f=w^\top g/n.
\]
The activity equations are
\[
 a'=\operatorname{sech}^2a\odot W^\top\delta,
 \qquad W'=\delta h^\top/n,\qquad w'=g,
 \qquad w(0)=0.                                             \tag{C1}
\]
All quantities in this check are real. Normalized vector norms mean
\(\|v\|_2/\sqrt n\). The source's \(k_0\) is
\(W_0^\top b_0\), where
\(b_0=\tanh z_0\odot\operatorname{sech}^2z_0\); it is the leading
coefficient of the carrier, not the actual zero initial carrier.

The first-layer empirical mean \(\|\tanh a_0\|_2^2/n\) is an average
of independent bounded variables with a positive expectation, so a fixed
positive lower bound fails with probability \(Ce^{-cn}\). Conditional on
\(a_0\), the entries of \(z_0\) are independent centered Gaussians of
variance \(Q=\|\tanh a_0\|_2^2/n\in[q_*,1]\). Each of
\[
 \tanh^2z,\qquad z\tanh z\operatorname{sech}^2z,
 \qquad\tanh^2z\operatorname{sech}^4z
\]
is bounded, nonnegative, and strictly positive away from zero. Its Gaussian
expectation is continuous and positive for \(Q\in[q_*,1]\), giving a
uniform positive minimum. Bounded-variable exponential concentration then
proves all the upper-layer empirical bounds in source equation (2), with
constants independent of the conditioning value of \(Q\). Gaussian sphere
nets give the stated operator bound. A union bound combines the events;
their mutual independence is unnecessary.

Choose \(\eta>0\) after these constants so that
\(K\sqrt\eta\le p_*/4\), and then choose \(R\) with
\(\Pr\{|N(0,1)|>R\}<\eta/2\). Bernoulli exponential concentration
gives source (3) at the same exponentially small failure scale. In
particular, no trained-carrier event has entered this initialization event.

## 2. Uniform real estimates and complete cubic remainders

For \(s\ge0\), \(\|w(s)\|_\infty\le s\) and
\(\|\delta(s)\|_2/\sqrt n\le s\). Hence
\[
 \|W'(s)\|_F
 =\|\delta(s)\|_2\|h(s)\|_2/n\le s,
 \qquad \|W(s)-W_0\|_F\le s^2/2.                           \tag{C2}
\]
The operator norm is therefore at most \(K+s^2/2\), and
\[
 \|a'(s)\|_2/\sqrt n\le(K+s^2/2)s.
\]
Integration gives the first displacement in source (4). The first gate is
1-Lipschitz; the identity
\(z-z_0=W(h-h_0)+(W-W_0)h_0\) gives the top-preactivation estimate;
the last gate is also 1-Lipschitz. Thus all four normalized displacements
in source (4) are \(O(s^2)\), uniformly on a fixed interval.

Integrating \(w'=g\) yields
\(\|w-sg_0\|_2/\sqrt n\le Cs^3\). The exact decomposition
\[
 \delta-sb_0
 =(w-sg_0)\odot\operatorname{sech}^2z
 +sg_0\odot(\operatorname{sech}^2z
                       -\operatorname{sech}^2z_0)
\]
has normalized norm \(Cs^3\). Multiplication by \(W^\top\), followed
by the additional term \(s(W-W_0)^\top b_0\), gives the second estimate
in source (5). This establishes complete uniform remainders; no unproved
bound on higher Taylor derivatives or coordinate maxima is being used.

## 3. First-layer lower bound

The exact pairing
\[
 h_0^\top k_0/n=z_0^\top b_0/n\ge p_*
\]
and \(\|k_0\|_2/\sqrt n\le K\) give the asserted moderate-coordinate
localization. Specifically, the normalized absolute pairing on
\(|a_{0,i}|>R\) is at most \(K\sqrt\eta\), by Cauchy--Schwarz.
On \(|k_{0,i}|>M\) it is at most \(K^2/M\), using \(|h_{0,i}|\le1\).
For \(M\ge4K^2/p_*\), these remove at most \(p_*/2\). Thus, for
\(E=\{|a_{0,i}|\le R,\ |k_{0,i}|\le M\}\),
\[
 n^{-1}\sum_{i\in E}|k_{0,i}|\ge p_*/2,
 \qquad n^{-1}\sum_{i\in E}k_{0,i}^2\ge p_*^2/4.             \tag{C3}
\]
The second inequality follows from Cauchy--Schwarz and \(|E|\le n\).
It remains valid despite correlations among the initialized quantities.

The real function \(\operatorname{sech}^4\) has a globally bounded
derivative. Restrict the nonnegative sum below to \(E\), use (C3), and
bound its gate perturbation by the fixed \(M^2\):
\[
 \frac1n\sum_i k_{0,i}^2\operatorname{sech}^4a_i(s)
 \ge \operatorname{sech}^4R\,p_*^2/4
       -CM^2\frac1n\sum_i|a_i(s)-a_{0,i}|
 \ge c_1>0                                                  \tag{C4}
\]
for a sufficiently small fixed interval. This is source (8); the last
average is bounded by the normalized Euclidean displacement.

Using \(h'=\operatorname{sech}^4a\odot W^\top\delta\) and source
(5),
\[
 k_0^\top h'(s)/n\ge c_1s-CKs^3\ge c_1s/2.
\]
After integration,
\[
 \frac{\|h(s)-h_0\|_2}{\sqrt n}
 \ge\frac{k_0^\top(h(s)-h_0)/n}{\|k_0\|_2/\sqrt n}
 \ge \frac{c_1}{4K}s^2.                                    \tag{C5}
\]
The positive pairing already excludes a zero denominator. No cancellation
of moving feature coordinates is assumed away; the fixed test direction
\(k_0\) controls it.

## 4. Second-layer lower bound

Set \(D_a=\operatorname{diag}(\operatorname{sech}^2a)\) and
\(D_z=\operatorname{diag}(\operatorname{sech}^2z)\). From (C1),
\[
 h'=D_a^2W^\top D_z w,
 \qquad
 z'=\frac{\|h\|_2^2}{n}D_z w+WD_a^2W^\top D_z w,
\]
and consequently
\[
 g'=T(s)w,
 \quad T(s)=D_z\left[\frac{\|h\|_2^2}{n}I
                              +WD_a^2W^\top\right]D_z.      \tag{C6}
\]
The learned-matrix term in \(z'\) is included. On the real flow the matrix
is positive semidefinite and its norm is at most
\(1+(K+S^2/2)^2\).

The uniform displacement bounds imply
\(\|h(s)\|_2^2/n\ge q_*/2\) on a smaller fixed interval. Bounded
\(g_0\), the Lipschitz gate, and the normalized displacement of \(z\)
give
\[
 \frac1n\sum_j g_{0,j}^2\operatorname{sech}^4z_j(s)\ge r_*/2.
\]
Dropping the positive semidefinite \(WD_a^2W^\top\) contribution in
(C6) proves source (10). Inserting \(w=sg_0+O_{\rm RMS}(s^3)\)
then gives
\(g_0^\top g'(s)/n\ge c_2s/2\). Integration and
\(\|g_0\|_2/\sqrt n\le1\) prove
\[
 \|g(s)-g_0\|_2/\sqrt n\ge c_2s^2/4.                       \tag{C7}
\]

## 5. Fitted endpoint

The exact slope, left implicit in the source, is
\[
 f'(s)=\frac{\|g(s)\|_2^2}{n}
                         +\frac{w(s)^\top T(s)w(s)}n.        \tag{C8}
\]
Both terms are nonnegative. The initialized lower bound for \(\|g_0\|\)
and (4) keep the first term above a fixed positive constant. Equations
(C2), (C6), and \(\|w\|_2/\sqrt n\le s\) give a fixed upper bound.
Thus there are \(0<c_f<C_f\) such that
\(c_f\le f'(s)\le C_f\) on the chosen interval, with \(f(0)=0\).
For \(y<c_fS\), a unique \(s_*\in(0,S)\) satisfies \(f(s_*)=y\),
and
\[
 y/C_f\le s_*\le y/c_f.
\]
The physical clock \(\dot s=2(y-f(s))\) increases to this root and has
no earlier stationary point. Equations (C5), (C7) therefore give the two
fitted lower bounds \(cy^2\), uniformly in width on the initialized event.

## 6. What the compression transfer does and does not establish here

Let the positive weighted norm of a retained feature vector be
\(\|v\|_p^2=\sum_i p_i|v_i|^2\), with \(\sum_i p_i=1\).
Suppose the compression theorem supplies, uniformly in the relevant activity
interval, both:

1. Pairing preservation to error \(C\epsilon\) for the original feature
   at \((s,s),(s,0),(0,0)\), in each hidden layer.
2. Weighted feature error \(\|\widehat h(s)-h_{\rm retained}(s)\|_p
   +\|\widehat g(s)-g_{\rm retained}(s)\|_p\le C\epsilon\), and
   fitted-clock error \(|\widehat s_*-s_*|\le C\epsilon\), with both
   endpoints lying in the controlled interval.

Expanding the squared displacement as its two self-pairings minus twice its
cross-pairing proves that the retained-reference squared displacement differs
from its original dense value by \(C\epsilon\). Bounded feature norms
and item 2 contribute another \(C\epsilon\). At the reduced fitted
activity \(\widehat s_*\ge cy\), the dense lower bound yields
\[
 \|\widehat h(\widehat s_*)-\widehat h(0)\|_p^2
       \ge c y^4-C\epsilon,
\]
and the same statement for \(\widehat g\). Taking
\(\epsilon\le c' y^4\) proves \(cy^2\) lower bounds on both reduced
feature norms. For fixed \(y>0\) and \(\epsilon=O(n^{-1/2})\), this
holds at all sufficiently large widths, as the source states.

The dependence on a fixed nonzero label is essential: this calculation does
not claim a threshold uniform as \(y\downarrow0\). Its pairing and
trajectory hypotheses are exactly the substantive compression input that
this scoped check has not verified. This is a dependency limit, not a defect
in the dense feature-learning proof or in the conditional implication.

## 7. Objections and scope

No major or fatal objection was found in the dense proof. The moderate-neuron
restriction in (C3)--(C4) correctly handles saturation without assuming a
trained maximum bound. The PSD argument in (C6) correctly includes the
learned hidden matrix. The cubic remainders are uniform finite-time estimates,
not merely formal Taylor coefficients. All constants are selected before
width, and all initialized concentration events have exponential tails.

The only unverified dependency is the compression theorem named above.
Actual nonlinear feature motion is proved; beneficial test performance,
non-reproducibility by fixed features, and a general multi-input theorem
would require separate claims and are not implied.
