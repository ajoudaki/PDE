### G.2. Initial features and a positive nonlinear margin

Fix the normalized function \(\psi\) in (M.1a), and take \(a\ge2\),
\(0\le e\le1\). We first prove the initialized Gram estimate without
assuming that \(\psi\) is odd or increasing.

Let \(Z=(Z_1,Z_2,Z_3)\) be centered Gaussian, with common positive
marginal variance \(v\) and covariance \(Q\). Write \(Z=Q^{1/2}G_3\),
where \(G_3\) is a standard Gaussian three-vector; singular \(Q\) is
allowed. Integration by parts in each independent coordinate gives
\(E[G_{3,k}\psi(Z_i)]=(Q^{1/2})_{ik}E[\psi'(Z_i)]\).
The boundary term vanishes because \(\psi\) is bounded, and the
integrand derivative is integrable because \(\psi'\) is bounded.
Consequently the orthogonal projection of \(\phi(Z_i)\) onto the
constants and Gaussian linear functions is \(m_v+b_vZ_i\), where
\[
 m_v=a+eE[\psi(\sqrt vG)],\qquad
 b_v=a+eE[\psi'(\sqrt vG)],\qquad
            m_v,b_v\ge a-e\ge a/2.                         \tag{G.3}
\]
Here \(G\) is a scalar standard normal variable. This calculation
also verifies orthogonality to every \(Z_j\) in a singular system;
no inverse of \(Q\) is involved. The residuals are orthogonal to
all the projected terms, and their Gram is positive semidefinite.
Writing \(J=\mathbf1\mathbf1^T\), we obtain
\[
 E[\phi(Z)\phi(Z)^T]\succeq m_v^2J+b_v^2Q
                         \succeq (a^2/4)(J+Q).             \tag{G.4}
\]

At initialization the first preactivation triple is Gaussian with
covariance \(\Gamma\). Each next initialized forward call is fresh
and Gaussian with covariance equal to the preceding feature Gram,
as proved by the fixed-program construction in Part F. Equal
marginal variances are preserved. Let \(Q_\ell\) be the feature
Gram after layer \(\ell\), with \(Q_0=\Gamma\). Put \(k=a^2/4\).
Iterating (G.4) and applying (G.1) gives
\[
 \begin{split}
 K^4(0)=Q_3&\succeq k^3\Gamma+(k^3+k^2+k)J\\
           &\succeq (a^6/64)(\Gamma+J)
            \succeq\lambda a^6I_3,
             \qquad\lambda=\delta^2/256.                  \tag{G.5}
 \end{split}
\]
The first scalar preactivation standard deviation is \(\sigma_1=1\).
Since \(k\ge1\), the diagonal inequality in (G.4) implies
\(\sigma_2,\sigma_3\ge1\). The scalar initialization identities and
Minkowski's inequality also give
\[
 \sigma_2=\|\phi(G)\|_2\le2a+1\le3a,\qquad
 \sigma_3=\|\phi(\sigma_2G)\|_2
      \le a+a\sigma_2+1\le5a^2.                            \tag{G.5a}
\]
Thus every initialized scalar preactivation has standard deviation
in \([1,5a^2]\). These are marginal distribution estimates, not
operator norm estimates for the initialized actions.

For any random variable of positive finite variance, define
\[
 \mathcal R_\psi(Z)=\inf_{\alpha,\beta}E[\psi(Z)-\alpha-\beta Z]^2
 =\operatorname{Var}(\psi(Z))-
       \frac{\operatorname{Cov}(Z,\psi(Z))^2}
                         {\operatorname{Var}(Z)}.          \tag{G.6}
\]
We abbreviate this as \(\mathcal R(Z)\) in subsequent sections.
The equality follows by first optimizing the intercept and then
completing the square in the slope. We now give the promised
explicit positive lower bound at initialization.

For an integer \(r\ge1\), the space of affine functions is a closed
two-dimensional subspace of \(L^2([-r,r])\). Its squared distance
from \(\psi\) is
\[
 J_r=\int_{-r}^r\psi(x)^2\,dx
       -\frac1{2r}\left(\int_{-r}^r\psi(x)\,dx\right)^2
       -\frac3{2r^3}\left(\int_{-r}^rx\psi(x)\,dx\right)^2.
                                                               \tag{G.6a}
\]
This follows by using the orthogonal basis \(1,x\), whose squared
norms are \(2r,2r^3/3\). If \(J_r=0\), \(\psi\) equals an affine
function almost everywhere on that interval and hence everywhere
on it by continuity. If this held for every integer \(r\), the
affine coefficients would agree on all overlapping intervals.
Then \(\psi\) would be affine on \(\mathbb R\), hence constant by
boundedness, a contradiction. This proves the existence of
\(r_\psi\) and the positivity of \(J_\psi,c_\psi\) in (M.20a).

For \(\sigma\ge1\), the density of \(\sigma G\) on
\([-r_\psi,r_\psi]\) is at least
\(e^{-r_\psi^2/2}/(\sigma\sqrt{2\pi})\). Therefore, for every
\(\alpha,\beta\), restriction of its nonnegative regression
integral to that interval gives the same density lower bound
times its Lebesgue regression integral. Taking the infimum yields
\[
 \mathcal R(\sigma G)\ge\frac{c_\psi}{\sigma},\qquad
 \mathcal R(\sigma_\ell G)\ge\frac{c_\psi}{5a^2}
                        =\eta_*>0\quad(\ell=1,2,3).        \tag{G.7}
\]
This argument covers compactly supported and oscillatory functions;
it does not assume a positive limiting regression margin as
\(\sigma\to\infty\).

We next transfer the margin to nearby, possibly non-Gaussian
variables. Suppose \(\operatorname{sd}(Z_0)\ge1\),
\(\mathcal R(Z_0)\ge\eta_*\), and \(\|Z-Z_0\|_2\le t_*\).
By (M.21), \(t_*\le1/2\) and \(t_*\le\sqrt{\eta_*}/6\).
Centering is an orthogonal projection, so standard deviation is
1-Lipschitz in \(L^2\); hence \(\operatorname{sd}(Z)\ge1/2\).
The minimizing regression slope at \(Z\) obeys
\[
 |\beta_Z|=\frac{|\operatorname{Cov}(Z,\psi(Z))|}
                    {\operatorname{Var}(Z)}
       \le\frac{\sqrt{\operatorname{Var}(\psi(Z))}}
                    {\operatorname{sd}(Z)}\le2.
\]
Use its minimizing intercept and slope as a candidate predictor
at \(Z_0\). Since \(\psi\) is 1-Lipschitz, the triangle inequality
then gives
\[
 \sqrt{\mathcal R(Z_0)}
   \le\sqrt{\mathcal R(Z)}+(1+|\beta_Z|)\|Z-Z_0\|_2
   \le\sqrt{\mathcal R(Z)}+3t_*.
\]
It follows that
\[
                         \mathcal R(Z)\ge\eta_*/4.         \tag{G.8}
\]
No Gaussian assumption on the perturbed variable \(Z\) is used.
