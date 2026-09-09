# Can attracting ReLU gates rule out every continuous joint limit?

## Verdict

No.  The finite-width attracting-gate theorem rules out a global classical
ODE with a fixed value of \(\phi'(0)\); it does not rule out a continuous
Euler-selected generalized limit.  More strongly, for the scalar predictor
and loss one can prove a width- and mesh-uniform local compactness theorem:
for **every** deterministic sequence \(h_n\downarrow0\), their Euler
interpolants are tight on one explicit width-independent time interval, and
every subsequential limit is continuous and has the correct initialized
trace.

Thus a theorem asserting that no continuous initialized joint limit exists
for any \(h_n\) cannot be obtained from the known attracting-gate facts.
What remains open is determinism, uniqueness, identification with the
actual width-first OMFP state, and continuation on arbitrary compact time
intervals.

## 1. Exact finite-width system and normalized norms

Let

\[
 \phi(x)=c x_+,\qquad c=\sqrt2,
\]

and use the network and half-square loss

\[
 X=\phi(u),\quad Z=\bar W X,
 \quad Y=\phi(Z),\quad f=\langle a,Y\rangle_n,
 \quad \ell={1\over2}(1-f)^2,                           \tag{1.1}
\]

where

\[
 \bar W={W\over\sqrt n},\qquad
 \langle v,w\rangle_n={1\over n}v^Tw,\qquad
 \|v\|_n^2=\langle v,v\rangle_n.                       \tag{1.2}
\]

Choose any bounded gate convention satisfying
\(|\phi'(0)|\le c\).  Put

\[
 C=a\odot\phi'(Z),\qquad B=\bar W^TC,qquad
 D=\phi'(u)\odot B,qquad r=1-f.                       \tag{1.3}
\]

One loss Euler step of size \(h>0\) is

\[
 a^+=a+hrY,\qquad u^+=u+hrD,qquad
 \bar W^+=\bar W+hr\,{CX^T\over n}.                 \tag{1.4}
\]

Define

\[
 A=\|a\|_n,qquad U=\|u\|_n,qquad
 G=\|\bar W\|_{\rm op},qquad
 R=\max\{1,A,U,G\}.                                   \tag{1.5}
\]

ReLU Lipschitzness and \(|\phi'|\le c\) give

\[
 \begin{aligned}
 \|X\|_n&\le cU,&
 \|Y\|_n&\le c^2GU=2GU,\\
 \|C\|_n&\le cA,&
 \|D\|_n&\le c^2GA=2GA,                              \tag{1.6}
 \end{aligned}
\]

and hence

\[
 |f|\le2GAU\le2R^3,qquad |r|\le3R^3.                 \tag{1.7}
\]

Since

\[
 \left\|{CX^T\over n}\right\|_{\rm op}
 =\|C\|_n\|X\|_n,                                    \tag{1.8}
\]

(1.4)--(1.7) imply the pathwise recursion

\[
 \boxed{R^+\le R+6hR^5.}                              \tag{1.9}
\]

No differentiability at a gate and no loss-dissipation assertion is used
in (1.9).

## 2. Explicit width-uniform short-time bound

Let

\[
 R_*=6,\qquad S=2R_*=12,\qquad
 T_*={1\over192R_*^4},qquad T_0={T_*\over2}.           \tag{2.1}
\]

On the initialization event

\[
 \mathcal E_n=\{\|a^0\|_n\le2,\ \|u^0\|_n\le2,
                    \ \|W^0/\sqrt n\|_{\rm op}\le6\}, \tag{2.2}
\]

we have \(R_0\le R_*\).  If \(kh\le T_*\), induction in (1.9)
gives

\[
 R_k\le S.                                             \tag{2.3}
\]

Indeed, as long as the preceding iterates are at most \(S=2R_*\),

\[
 R_k\le R_*+6khS^5
 \le R_*+6T_*(2R_*)^5=2R_*.                           \tag{2.4}
\]

This closes the induction.

Moreover,

\[
 \mathbb P(\mathcal E_n)\longrightarrow1.             \tag{2.5}
\]

The first two bounds follow from the law of large numbers.  For
completeness, the matrix bound has an elementary net proof.  A
\(1/4\)-net of the unit sphere can be chosen with at most \(9^n\) points.
For fixed unit \(x,y\), \(y^TWx\sim N(0,1)\); therefore

\[
 \mathbb P\left\{\max_{x,y\text{ in the nets}}|y^TWx|>3\sqrt n\right\}
 \le2\,81^n e^{-9n/2}\longrightarrow0.                \tag{2.6}
\]

Approximating both maximizing unit vectors by the nets yields
\(\|W\|_{\rm op}\le2\max_{x,y\text{ in the nets}}|y^TWx|\), proving
the last assertion in (2.2).

## 3. Uniform continuity of the predictor

Assume two consecutive states satisfy \(R,R^+\le S\).  From (1.4)--(1.7),

\[
 \|a^+-a\|_n,\ \|u^+-u\|_n,
 \ \|\bar W^+-\bar W\|_{\rm op}\le6hS^5.             \tag{3.1}
\]

Writing \(X^+=\phi(u^+)\), ReLU Lipschitzness gives

\[
 \|X^+-X\|_n\le12hS^5.                               \tag{3.2}
\]

Consequently

\[
 \begin{aligned}
 \|Z^+-Z\|_n
 &\le \|\bar W^+\|_{\rm op}\|X^+-X\|_n
   +\|\bar W^+-\bar W\|_{\rm op}\|X\|_n\\
 &\le24hS^6,\\
 \|Y^+-Y\|_n&\le48hS^6.                              \tag{3.3}
 \end{aligned}
\]

Using \(\|Y^+\|_n\le2S^2\),

\[
 \begin{aligned}
 |f^+-f|
 &\le\|a^+-a\|_n\|Y^+\|_n
      +\|a\|_n\|Y^+-Y\|_n\\
 &\le60S^7h.                                          \tag{3.4}
 \end{aligned}
\]

## 4. Local compactness theorem

### Theorem 4.1

Let \(h_n\downarrow0\) be arbitrary.  For the width-\(n\) Euler path,
linearly interpolate the grid predictors, calling the result \(F_n\), and
put \(L_n=(1-F_n)^2/2\).  Then the laws of \(F_n\) and \(L_n\)
are tight in \(C([0,T_0])\).  Every subsequential limit is supported on
continuous paths satisfying

\[
 F(0)=0,\qquad L(0)={1\over2}.                       \tag{4.1}
\]

#### Proof

For all sufficiently large \(n\), \(h_n\le T_0\), so every grid state
needed to interpolate through time \(T_0\) lies before time
\(T_0+h_n\le T_*\).  On \(\mathcal E_n\), (2.3) and (3.4) show

\[
 \|F_n\|_\infty\le2S^3,\qquad
 |F_n(t)-F_n(s)|\le60S^7|t-s|.                         \tag{4.2}
\]

The set of functions satisfying (4.2) is compact in \(C([0,T_0])\) by
Arzela--Ascoli.  Its probability tends to one by (2.5), proving tightness.

At initialization, \(a^0\) is independent of \(Y^0\), and

\[
 \mathbb E(f_n^0)^2
 ={1\over n^2}\mathbb E\|Y^0\|_2^2={1\over n}.         \tag{4.3}
\]

The last equality uses ReLU homogeneity: conditionally on \(u\),
\(z_i\sim N(0,Q_n)\) and
\(\mathbb E[\phi(z_i)^2\mid u]=Q_n\), while
\(\mathbb EQ_n=\mathbb E\phi(G)^2=1\).  Hence
\(F_n(0)\to0\) in \(L^2\).  Every weak subsequential limit therefore
starts at zero.  The loss assertion follows by the continuous mapping
theorem.  If instead one linearly interpolates the loss values themselves,
then on a grid cell with endpoint predictors \(x,y\), its difference from
\((1-F_n)^2/2\) is
\[
 {1\over2}\lambda(1-\lambda)(x-y)^2
 \le {1\over8}(x-y)^2.
\]
It is uniformly \(O(h_n^2)\) by (3.4), so the same conclusion holds for
that interpolation. \(\square\)

Theorem 4.1 proves subsequential continuous scalar joint limits for every
mesh sequence.  It does **not** prove that the limit is deterministic, that
different subsequences agree, that the whole OMFP state is tight in a
strong enough topology, or that the result continues past \(T_0\).

## 5. Why the known attracting event cannot be amplified as claimed

The exact width-two construction supplies an open set of finite parameter
space, of positive Gaussian probability, on which a classical
fixed-convention trajectory reaches a noncontinuable attracting gate.  It
does not supply a lower bound uniform in width:

1. Embedding the displayed \(2\times2\) block into width \(n\) does not
   preserve its normal velocities.  The other \(n-2\) coordinates enter
   both forward fields and the reused-adjoint aggregate at order one.
2. Forcing all other coordinates to be inactive or negligible has
   probability tending to zero, rather than a width-uniform positive
   probability.
3. The marked surface calculation \(p>0>q\) with positive conditional
   Gaussian probability concerns a gate already on the surface.  Initial
   Gaussian gates hit that surface with probability zero.  A dynamic
   hitting theorem requires the presently missing hard-indicator
   state-evolution and coarea estimate.
4. Even a macroscopic family of attracting gates would not by itself make
   \(F_n\) discontinuous.  Euler confines every frozen attracting normal
   coordinate to an \(O(h_n)\) strip and gives a bounded occupation
   measure.  Gate derivatives jump, but the network output is continuous
   in the parameters; Theorem 4.1 quantifies this distinction.

Thus the finite-width obstruction is a proof against a classical
fixed-derivative ODE, not a proof against continuous generalized paths.

## 6. Kernel occupations do not currently give a nonconvergence theorem

At a frozen attracting gate with side velocities \(p>0>q\), hard Euler
selects

\[
 \lambda={p\over p-q},\qquad
 \nu=(1-\lambda)\delta_0+\lambda\delta_1.               \tag{6.1}
\]

The occupation discrepancy is less than one sample over every finite
window.  Hence this one-gate model supports, rather than contradicts, a
canonical hard-Euler limit.

The unresolved issue begins with **joint** occupations.  For example, take
two frozen rotations with the same \(\lambda=1/2\).  If their phases agree,
then

\[
 {1\over N}\sum_{k<N}I_k^{(1)}I_k^{(2)}\longrightarrow{1\over2};
 \tag{6.2}
\]

if their phases differ by one half-turn, the same limit is zero.  Both
marginal occupations equal one half.  Therefore marginal Filippov weights
do not determine products of gates.  Reused adjoints and squared
cotangents can see precisely such joint moments.

Equation (6.2) is a logical warning, not an actual-network counterexample.
To turn it into one, one must prove that two positive-probability mesh
subsequences of the initialized network generate different limiting phase
correlations and that the difference survives the mean-field
normalization in the loss readout.  No such theorem is currently present.

Likewise, the initialization slab regimes \(nh_n\to0\), finite, or
infinite do not alone produce different loss limits.  They count gates,
but supply no nonvanishing lower bound on the accumulated output or kernel
effect of those gates.  A one-step boundary term may vanish after summing
over physical time.

## 7. The logically independent outcomes

The proved facts leave four distinct possibilities:

1. **Unique continuous kinetic limit.**  All admissible hard-Euler meshes
   converge to one restartable OMFP--Young-measure flow.  The frozen
   one-gate rotation is evidence that this is possible.
2. **Several continuous hard-Euler limits.**  Joint gate phases or reused
   responses retain mesh information, producing different continuous loss
   or state paths.  This would refute canonicity, not continuity.
3. **State nonuniqueness invisible to loss.**  Different joint occupation
   states give the same scalar predictor and loss.  Scalar convergence
   would then coexist with failure of a canonical full state.
4. **Failure only after positive time.**  Theorem 4.1 rules out a scalar
   initialized jump on \([0,T_0]\), but does not exclude later loss of
   tightness, an initial layer in a stronger state topology, or a
   positive-time mesh bifurcation.

Deciding among these requires a width-uniform dynamic hitting/occupation
theorem, the hard-indicator reused-\(W/W^T\) identification, strong
square-tail control for the tangent kernel, and either uniqueness or an
explicit pair of mesh subsequences with different macroscopic readouts.
The currently proved attracting-gate and initialization-count statements
do not decide those logically independent alternatives.
