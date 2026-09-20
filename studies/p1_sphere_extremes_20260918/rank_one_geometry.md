# Three rank-one terms and the two stationarity equations

This is a scoped, prompt-only theoretical result. The supplied scientific inputs are
three vectors \(a_i\in\mathbb R^6\), three vectors \(d_i\in\mathbb R^3\), scalars
\(\rho_i\in\mathbb R\), and the equations
\[
\sum_{i=1}^3\rho_i d_i a_i^T=0,
\qquad
\rho_i M^T d_i=0\quad(i=1,2,3).
\tag{1}
\]
Here \(M\) has three rows; the usual \(3\times6\) choice is included. The second
equation is taken as supplied under independence of the input directions. No
forward activation rule, formula for \(d_i\), or initialization is assumed. All
results below are exact algebraic consequences of these inputs, except the
explicitly stated perturbation estimates. No computation or experiments were
used. These results have not undergone independent review or promotion.

The proof first handles rank-one cancellation, then gives a classification of
both equations that includes every zero-factor case. A final estimate states what
survives under small errors.

## 1. Exact rank-one cancellation

**Two-term lemma.** Let \(u,s\in\mathbb R^p\setminus\{0\}\) and
\(v,t\in\mathbb R^q\setminus\{0\}\). Then
\[
\operatorname{rank}(uv^T+st^T)\leq1
\quad\Longleftrightarrow\quad
\dim\operatorname{span}\{u,s\}\leq1
\qquad\text{or}\qquad
\dim\operatorname{span}\{v,t\}\leq1.
\tag{2}
\]
If the left factors are dependent, the sum has a single left factor, so its rank
is at most one. The same argument applies to dependent right factors. Conversely,
suppose both pairs are independent. The map
\(x\mapsto(v^Tx,t^Tx)\) has rank two, so there are \(x,y\in\mathbb R^q\)
with
\[
(v^Tx,t^Tx)=(1,0),\qquad(v^Ty,t^Ty)=(0,1).
\]
The matrix in (2) maps \(x\) to \(u\) and \(y\) to \(s\). Its image therefore has
dimension at least two, and its image is contained in
\(\operatorname{span}\{u,s\}\), so its rank is exactly two. This proves (2).

**Three-term theorem.** If \(B_1,B_2,B_3\) are nonzero real rank-one matrices
of the same dimensions and
\[
B_1+B_2+B_3=0,
\tag{3}
\]
then all three have a common one-dimensional column space or all three have a
common one-dimensional row space. Equivalently, for any nonzero factorizations
\(B_i=u_iv_i^T\), either all \(u_i\) are proportional or all \(v_i\) are
proportional. The alternatives may both hold.

Indeed, \(B_1+B_2=-B_3\) has rank one. By (2), either \(u_1,u_2\) are
proportional or \(v_1,v_2\) are proportional. In the first case, write
\(u_i=c_i u\) for \(i=1,2\), with \(u\ne0\). Then
\[
B_3=-u(c_1v_1+c_2v_2)^T.
\]
Because \(B_3\ne0\), the parenthesized vector is nonzero, and the column space of
\(B_3\) is also \(\operatorname{span}\{u\}\). The second case gives the
corresponding common row space by the same factorization with left and right
exchanged. This proves the proposed matrix assertion.

Alignment is necessary but must be accompanied by a vector relation. In the
common-left case (3) is equivalent to
\(c_1v_1+c_2v_2+c_3v_3=0\), after writing \(u_i=c_i u\). In the common-right
case it is equivalent to the analogous relation between the left factors.

**All zero-term cases.** Suppose only \(\operatorname{rank}B_i\leq1\) is
assumed, and let \(k\) be the number of nonzero matrices.

* \(k=0\): (3) is automatic.
* \(k=1\): (3) is impossible.
* \(k=2\): the two nonzero matrices are negatives of one another. Their column
  spaces and their row spaces agree.
* \(k=3\): the three-term theorem applies.

For the supplied factors, set \(B_i=\rho_i d_i a_i^T\). Precisely,
\[
B_i\ne0\quad\Longleftrightarrow\quad
\rho_i\ne0,\ d_i\ne0,\ a_i\ne0.
\tag{4}
\]
To verify the reverse implication, choose nonzero coordinates of \(d_i\) and
\(a_i\); their product gives a nonzero matrix entry. Thus, with three active
terms, either all \(d_i\) or all \(a_i\) are proportional. With two active terms,
both sets of active factor lines agree. A zero term imposes no alignment on its
displayed factors: it can vanish through any factor in (4). For example,
\(B_1=e_1f_1^T\), \(B_2=-e_1f_1^T\), and
\(B_3=0\cdot e_2f_2^T\) satisfy (3), while the displayed third left and right
factors are unrelated to the first two. Here \(e_1,e_2\) and \(f_1,f_2\) are
distinct standard basis vectors in the respective spaces.

## 2. Complete classification of the supplied stationarity equations

Define
\[
q_i=\rho_i d_i,\qquad
Q=[q_1\ q_2\ q_3]\in\mathbb R^{3\times3},\qquad
A=[a_1\ a_2\ a_3]\in\mathbb R^{6\times3}.
\]
Then (1) is exactly
\[
M^TQ=0,\qquad QA^T=0.
\tag{5}
\]
The first equation says that every column of \(Q\) belongs to
\(\ker M^T\). The second says that every column of \(A^T\), equivalently the
transpose of every row of \(A\), belongs to \(\ker Q\). Consequently,
\[
\operatorname{rank}M+\operatorname{rank}Q\leq3,
\qquad
\operatorname{rank}A+\operatorname{rank}Q\leq3.
\tag{6}
\]
These inequalities alone are necessary; the following four cases give the full
equations, and are each sufficient as stated.

1. **\(\operatorname{rank}Q=0\).** Every \(\rho_i d_i=0\). Both equations
   hold for arbitrary \(A\) and arbitrary \(M\).
2. **\(\operatorname{rank}Q=1\).** Write \(Q=u c^T\), with nonzero
   \(u,c\in\mathbb R^3\). Then (5) is equivalent to
   \[
   M^Tu=0,\qquad Ac=0.
   \tag{7}
   \]
   Indeed, \(M^TQ=(M^Tu)c^T\), and \(QA^T=u(Ac)^T\); since \(u,c\ne0\),
   each outer product vanishes exactly when its remaining vector vanishes.
   In this case \(\operatorname{rank}M\leq2\) and
   \(\operatorname{rank}A\leq2\).
3. **\(\operatorname{rank}Q=2\).** Let
   \(\ker Q=\operatorname{span}\{\beta\}\), where
   \(\beta\in\mathbb R^3\setminus\{0\}\). Then (5) is equivalent to
   \[
   \operatorname{im}Q\subseteq\ker M^T,\qquad
   A=a\beta^T\quad\text{for some }a\in\mathbb R^6.
   \tag{8}
   \]
   For the second equivalence, every row of \(A\) must be a multiple of
   \(\beta^T\); collecting its six scalar multipliers gives \(a\). Conversely,
   \(QA^T=Q\beta a^T=0\). Here \(a=0\) is allowed, as are zero coordinates of
   \(\beta\). In particular, \(\operatorname{rank}M\leq1\).
4. **\(\operatorname{rank}Q=3\).** Since \(Q\) is invertible, (5) holds
   exactly when \(M=0\) and \(A=0\).

In every case the identities \(q_i=\rho_i d_i\) remain part of the data. If
\(\rho_i=0\), then \(q_i=0\) and \(d_i\) is unrestricted by (1). If
\(\rho_i\ne0\), then \(d_i=q_i/\rho_i\). This accounts for zero residuals and
zero derivative vectors without conflating them. A zero \(a_i\) removes its term
from middle stationarity, but does not remove the lower equation
\(M^Tq_i=0\).

In particular, **if \(M\) has full row rank three, then (1) is equivalent to
\(\rho_i d_i=0\) for each \(i\)**; middle stationarity adds no condition on
\(a_i\). The implication uses \(\ker M^T=\{0\}\), while the converse is direct
substitution. Therefore:

* If \(\rho_i\ne0\), then \(d_i=0\).
* If \(d_i\ne0\), then \(\rho_i=0\).
* A zero \(a_i\) does not allow \(\rho_i\ne0\) and \(d_i\ne0\) together.
* If all \(d_i\ne0\), all residuals vanish. This last conclusion requires
  precisely the stated nonvanishing assumption.

Thus three nonzero middle terms cannot coexist with full-row-rank \(M\) and the
supplied individual lower stationarity. This follows before using the three-term
theorem. More generally, every nonzero \(Q\) forces rank loss in \(M\), quantified
by (6), even if every middle term vanishes because the corresponding \(a_i\) is
zero. If the hidden vectors \(a_1,a_2,a_3\) themselves are independent, then
\(\operatorname{rank}A=3\) forces \(Q=0\) even without any rank assumption on
\(M\). Independence of the input directions must not be substituted for this
separate hidden-vector independence condition.

Two algebraic constructions verify that the rank-deficient alternatives are
substantive. They claim no compatibility with an unspecified forward model.

* If \(0\ne u\in\ker M^T\), take all \(\rho_i=1\),
  \(d_1=d_2=u\), \(d_3=-u\), and
  \(a_1=f_1\), \(a_2=f_2\), \(a_3=f_1+f_2\). Both equations hold; all terms
  are nonzero, the left factors agree as lines, and the right factors are not
  all proportional.
* If \(\ker M^T\) contains independent \(u,v\), take all \(\rho_i=1\),
  \(d_1=u\), \(d_2=v\), \(d_3=-u-v\), and \(a_1=a_2=a_3=f_1\). Both
  equations hold; all terms are nonzero, the right factors agree as lines, and
  the left factors are not all proportional.

With full-row-rank \(M\), the equally valid choice \(d_i=0\) for all \(i\)
permits arbitrary residuals and arbitrary hidden vectors. Therefore the supplied
relations do not by themselves rule out stationary states with nonzero residual.
Ruling those out requires an additional reason that the relevant \(d_i\) cannot
vanish, or another equation that excludes this case. Likewise, no architectural
conflict between alignment and distinct input directions follows without a
specified relation between those directions, \(a_i\), and \(d_i\). No conclusion
about reachability from initialization follows from these algebraic classifications.

## 3. A quantitative version for near cancellation

Let \(B_i=u_iv_i^T\ne0\), set
\[
E=B_1+B_2+B_3,\quad
\varepsilon=\|E\|_{\mathrm{op}},\quad
n_i=\|B_i\|_{\mathrm{op}}=\|u_i\|\,\|v_i\|>0.
\]
For nonzero vectors define their line-angle sine by
\[
s(x,y)=\sqrt{1-\frac{\langle x,y\rangle^2}{\|x\|^2\|y\|^2}}.
\]
For every distinct \(i,j,k\in\{1,2,3\}\),
\[
n_in_j\,s(u_i,u_j)s(v_i,v_j)
\leq
\varepsilon\min\{n_i+n_j,n_k+\varepsilon\}.
\tag{9}
\]
This controls the product of the two failures of alignment; it does not require
choosing in advance which side aligns.

To prove (9), it suffices to consider pairs for which both vector pairs are
independent, since otherwise its left side is zero. Set \(C=B_i+B_j\). In
orthonormal bases of the two-dimensional left and right spans, \(C\) has a
\(2\times2\) matrix equal to the product of the left-factor coordinate matrix
and the transpose of the right-factor coordinate matrix. Its determinant
magnitude is
\[
\|u_i\|\|u_j\|s(u_i,u_j)
\|v_i\|\|v_j\|s(v_i,v_j).
\]
If \(\sigma_1\geq\sigma_2>0\) are the two singular values of \(C\), their
product equals that determinant magnitude: the determinant of \(C^TC\), in
these coordinates, is both \(\sigma_1^2\sigma_2^2\) and the square of the
determinant of \(C\).

There is a unit vector \(x\in\operatorname{span}\{v_i,v_j\}\) with
\(v_k^Tx=0\), because one linear equation on a two-dimensional space has a
nontrivial kernel. Since \(C=E-B_k\),
\(\|Cx\|=\|Ex\|\leq\varepsilon\). The smaller singular value is the
minimum of \(\|Cy\|\) over unit \(y\) in this right span, so
\(\sigma_2\leq\varepsilon\). The triangle inequality gives both
\(\sigma_1\leq n_i+n_j\) and \(\sigma_1\leq n_k+\varepsilon\).
Multiplying these bounds proves (9).

A global alternative follows when no term is vanishingly small. Suppose
\(0<m\leq n_i\leq L\), \(\varepsilon>0\), and define
\[
\eta=\frac{\varepsilon(L+\varepsilon)}{m^2},\qquad \delta=\sqrt\eta.
\]
Then at least one of the following holds:
\[
\max_i s(u_i,u_1)\leq\delta,
\qquad\text{or}\qquad
\max_i s(v_i,v_1)\leq
\frac{\varepsilon}{m}+\frac{L}{m}\delta.
\tag{10}
\]
The bounds are useful when \(\varepsilon/m\) is small and \(L/m\) is
controlled. If the first bound fails, choose \(j\) with
\(s(u_1,u_j)>\delta\). Equation (9) gives
\(s(v_1,v_j)\leq\eta/\delta=\delta\). Let \(k\) be the remaining index and
\(P\) the orthogonal projection onto \(v_1^\perp\). Then
\[
B_kP=EP-B_jP,
\qquad
n_k s(v_k,v_1)=\|B_kP\|_{\mathrm{op}}
\leq\varepsilon+n_j s(v_j,v_1)
\leq\varepsilon+L\delta.
\]
Division by \(n_k\geq m\) proves the second bound; it also bounds the \(j\)
term because \(L/m\geq1\). At \(\varepsilon=0\), use the exact theorem rather
than divide by \(\delta=0\).

A lower bound on term sizes is needed for an unweighted global alignment claim.
For example,
\[
B_1=e_1f_1^T,\qquad
B_2=\varepsilon e_2f_2^T,\qquad
B_3=-e_1f_1^T
\]
have residual norm \(\varepsilon\), while the second term's left and right
directions are orthogonal to those of the other terms. For each
\(\varepsilon>0\) all three terms are nonzero.

Finally, lower stationarity itself has a simpler perturbation estimate. If \(M\)
has full row rank and \(\sigma>0\) is its least singular value, then
\(\|M^Ty\|\geq\sigma\|y\|\) for all \(y\in\mathbb R^3\). Thus
\[
\|\rho_i M^Td_i\|\leq\tau_i
\quad\Longrightarrow\quad
|\rho_i|\|d_i\|\leq\frac{\tau_i}{\sigma},
\qquad
\|\rho_i d_i a_i^T\|_{\mathrm{op}}
\leq\frac{\tau_i\|a_i\|}{\sigma}.
\tag{11}
\]
The same last bound holds in Frobenius norm because the matrix has rank at most
one. A uniform lower bound on \(|\rho_i|\) converts (11) into a small-\(d_i\)
bound; a uniform lower bound on \(\|d_i\|\) converts it into a small-residual
bound. Without these hypotheses, near stationarity does not distinguish the two
causes. Without a lower bound on \(\sigma\), it does not exclude approximate
kernel directions either.

Frozen conclusion: the rank-one assertion and the classification (5)–(8) are
proved under the supplied algebraic assumptions. A nonzero-residual exclusion,
an architectural incompatibility, and initialized reachability remain outside
what those assumptions establish.
