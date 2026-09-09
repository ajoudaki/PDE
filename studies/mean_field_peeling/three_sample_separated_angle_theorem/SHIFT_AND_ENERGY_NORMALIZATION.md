# The constant shift and Gaussian second-moment normalization

Mathematical follow-up, 2026-09-07. This note analyzes the activation in
PROOF.md without changing that theorem or its reviewed files.

The distinction is between (i) a genuine obstruction after making the
activation odd, and (ii) a failure of the existing proof to transfer
after energy normalization. The latter is not an impossibility theorem.

## 1. Deleting the constant falsifies the full stated conclusion

Replace the activation by
\[
                    \psi(z)=az+e\arctan z .
\]
This is odd, and its derivative is even. The network has no separate
additive biases. Consequently, at every parameter value and width,
\[
 z^\ell(-x)=-z^\ell(x),\quad h^\ell(-x)=-h^\ell(x),\quad
 f(-x)=-f(x),\quad b^\ell(-x)=b^\ell(x).
\]
The last identity uses the residual-free backward fields of PROOF.md.

Choose \(d=2\), inputs
\[
 x_1=\sqrt2(1,0),\qquad x_2=-x_1,\qquad x_3=\sqrt2(0,1),
 \qquad y_1=y_2=1,\quad y_3=\pm1 .
\]
Their correlation matrix is
\[
 \Gamma=\begin{pmatrix}1&-1&0\\-1&1&0\\0&0&1\end{pmatrix}.
\]
They satisfy the separation hypothesis for every \(0<\delta\le1\).
For every parameter state the antipodal pair contributes
\[
 \tfrac12[(f_1-1)^2+(f_2-1)^2]=f_1^2+1
\]
to the loss. Hence exact fitting and the positive-kernel/exponential-fit
mechanism are impossible. The direction \((1,1,0)\) is in the nullspace
of every raw kernel block because \(f_1+f_2\) is identically zero.

There is also a direct contradiction to the theorem's stated
every-sample initial-acceleration conclusion, independently of any
claim about fitting. At population initialization \(C_0=0\), all hidden
velocities are zero. Let \(\beta_j^1=\dot b_j^1(0)\).
Oddness gives \(b_2^1=b_1^1\), hence \(\beta_2^1=\beta_1^1\).
Differentiating the first projected physical equation at zero gives
\[
 \ddot z_i^1(0)=\sum_j y_j\Gamma_{ij}\beta_j^1.
\]
Terms involving \(\dot r_j b_j^1\) vanish because \(b_j^1(0)=0\).
The displayed Gram and labels therefore imply
\[
 \ddot z_1^1(0)=\ddot z_2^1(0)=0,\qquad
 \ddot h_1^1(0)=\ddot h_2^1(0)=0.
\]
Thus the full theorem does not survive this replacement, regardless of
the values of \(a,e\). For the two-input version, the same-label
antipodal pair already has a stationary zero-readout population path.

The numerical constant 1 is not itself a geometric necessity. An offset
\(c\ne0\) gives
\[
 \Gamma+c^2\mathbf1\mathbf1^T
 \succeq\min(1,c^2)(\Gamma+\mathbf1\mathbf1^T)
 \succeq\min(1,c^2)\frac{\delta^2}{4}I .
\]
The complete proof would need adjusted constants for another offset.
What cannot be done under the original data class is simply replace
the entire constant/even part by zero while keeping an odd activation
and the bias-free architecture. Other ways of breaking oddness are
not excluded by this counterexample.

For \(\delta>1\), an antipodal pair cannot belong to an admissible triple:
its two correlations with the third input are opposite numbers and
cannot both be negative. The counterexample refutes the theorem over
its full separation range; it does not settle this narrower regime.

## 2. Exact Gaussian energy normalization

Let \(G\sim N(0,1)\), \(a>0,e>0\), and
\[
 \phi(z)=a(1+z)+e\arctan z,\quad
 \mu=E[G\arctan G]>0,\quad \nu=E[(\arctan G)^2]>0.
\]
Oddness of \(G\) and \(\arctan G\) yields
\[
             N^2:=E[\phi(G)^2]=2a^2+2ae\mu+e^2\nu .
\]
Thus \(\widehat\phi=\phi/N\) always has unit Gaussian second moment.
Writing \(r=e/a\), this is exactly
\[
 \widehat\phi(z)
 =\frac{1+z+r\arctan z}{\sqrt{2+2\mu r+\nu r^2}}
 =A(1+z)+E\arctan z,
\]
where
\[
 A=\frac aN<\frac1{\sqrt2},\qquad E=\frac eN,\qquad E/A=e/a.
\]
The overall gain disappears, although the ratio of the two coefficients
is preserved. For the unshifted family the denominator squared would
instead be \(a^2+2ae\mu+e^2\nu\); normalization preserves its oddness and
therefore cannot remove the obstruction in Section 1.

Under the original population Gaussian initialization, a unit Gaussian
second moment makes all initialized scalar preactivation variances and
feature second moments equal to one: the variance recursion starts at
one, and one is a fixed point of
\(q\mapsto E[\widehat\phi(\sqrt qG)^2]\).
This is an initialization statement, not a conservation law during
training.

Positive initial feature coercivity survives normalization:
\[
 Q_3\succeq A^6\Gamma+(A^6+A^4+A^2)\mathbf1\mathbf1^T
      \succeq A^6(\delta^2/4)I .
\]
The projection proof needs only \(A>0,E>0\), not \(A\ge1\).
Initial nonaffinity survives as well:
\[
 \inf_{\alpha,\beta}E[\widehat\phi(G)-\alpha-\beta G]^2
                         =E^2(\nu-\mu^2)>0.
\]
Strictness follows from equality in Cauchy--Schwarz: arctangent is not
an almost-everywhere linear function of a full-support Gaussian.

## 3. Why the global theorem cannot simply be rescaled

The present three-input proof uses an absolutely large affine gain,
not merely a small ratio \(e/a\). Its kernel domination and bounded
total residual-clock estimates explicitly require that gain.
After normalization \(A<1/\sqrt2\). Also \(Q_3\) has diagonal entries
one, so \(\operatorname{tr}Q_3=3\) and
\(\lambda_{\min}(Q_3)\le1\). The proof's large initial kernel cannot
be retained by common output scaling of the activation.

Nor is this an innocuous change of time in the original dynamics.
Let \(c=1/N\) and \(\widehat\phi=c\phi\). At unchanged weights,
\[
 h_{\widehat\phi}^1=c h_\phi^1,\qquad
 h_{\widehat\phi}^2=c\,\phi(c z_\phi^2).
\]
The inner arguments have changed. One can restore the same represented
function by the parameter map
\[
 T_c(W^1,W^2,W^3,C)=(W^1,W^2/c,W^3/c,C/c).
\]
But this changes the prescribed initialization. It also pulls the raw
metric back to one with factors \(1,c^{-2},c^{-2},c^{-2}\) on its four
blocks. Accordingly the pulled-back normalized-network gradient flow
has block learning-rate factors \(1,c^2,c^2,c^2\), not one common
factor. A single time rescaling does not restore the original
all-block raw gradient flow.

Therefore Gaussian energy normalization is algebraically possible and
preserves useful initial properties. A global normalized three-input
theorem, with the original initialization and raw optimizer, needs a
new global argument. Neither its truth nor its impossibility is
established by the existing gain proof.

The oddness counterexample and the normalization/dynamics calculations
were checked independently by two additional agents. These checks do
not claim a proof of the open normalized global theorem.
