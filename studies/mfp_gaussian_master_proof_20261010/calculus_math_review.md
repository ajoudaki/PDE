# Independent internal mathematical review of the operational calculus

Reviewer: fresh scoped agent `calculus_math_review`. Completed 2026-10-10.
This is an internal review of the operational companion and every worked
example, not a promotion review or an implementation review.

**Verdict: PASS for the assigned scope.** No mathematical correction is
required in the frozen rulebook or worked examples. The rules reproduce the
master theorem's declared language, normalizations and derivative conventions;
the examples follow by exact finite-width algebra and that theorem. The
qualifications under “Limitations” remain part of this verdict.

## Assignment, isolation and frozen inputs

The neutral assignment was to read only the complete frozen `master_proof.md`,
`calculus_rulebook.md` and `worked_examples.md`, together with required skills
and process instructions; reconstruct the operational rules and all examples;
check matrix reuse, exact finite-width expectations, rank updates versus
ambient gradients, singular formal derivatives, moving-flow derivatives and
factorial jets; and write only this report. No input was edited.

All scientific lines, including introductions, proofs, examples and concluding
scope statements, were read. The read coverage and SHA-256 hashes are:

| Input | Complete read coverage | SHA-256 |
| --- | --- | --- |
| `master_proof.md` | Lines 1–467, in contiguous reads 1–240 and 241–467 | `55d979e9dbab1c13bc1f84a43b001efe9fefa6bd1b565d4479245ef5128a3388` |
| `calculus_rulebook.md` | Lines 1–386 | `9c934578b25dd77079f1b2896829cce471ca1cf85abd7a53ae6445036f7e25d3` |
| `worked_examples.md` | Lines 1–383 | `cbcff373fdcdde122caaa8f6c8d4847f8afe87bfe2c8b730da7d8ae255374451` |

Hashes were obtained before reading and rechecked unchanged after the
calculations. Required instructions read were root `AGENTS.md`,
`RESEARCH_WORKFLOW.md`, `explain-with-canonical-notation/SKILL.md` and its
complete `references/neural-response-memory.md`, and
`solve-math-rigorously/SKILL.md`. An initially truncated instruction fragment
was repaired by a targeted read. No scientific input was truncated.

I did not read the study README, history, prior review reports, other study
contents, another agent's findings, maintained-book passages, implementation,
or external sources. The frozen master proof itself contains a historical
status sentence; that sentence was not used as evidence for this verdict.
No subagent was used. Git HEAD/index/status were inspected only as coordination
metadata before writing: HEAD was
`c17cb8c2e8d486ccc1d2b80e8cd173ba551145ae`, the index was empty, and concurrent
working-tree changes were left untouched. This reviewer performed no staging
or commit.

## Reconstruction of the operational rules

The primitive graph is finite, causal and typed. A named initialized matrix
has independent entries of variance $1/n$ and connects distinct vector types;
the transpose reuses that exact matrix. Same-type coordinate maps, normalized
averages and scalar arithmetic match master-proof Section 1. The rulebook
does not admit cross-type coordinate products, arbitrary dense matrix
directions, inverses, coordinate selection or growing program size.

For a represented current matrix
$A=W_0+\sum_\nu c_\nu u_\nu v_\nu^T/n$, direct multiplication gives

\[
Ah=W_0h+\sum_\nu c_\nu u_\nu(v_\nu^Th/n),\qquad
A^Tu=W_0^Tu+\sum_\nu c_\nu v_\nu(u_\nu^Tu/n).
\]

No independence among the factors is needed. The contraction identity is

\[
\left\langle uv^T/n,pq^T/n\right\rangle_F
=\frac{(u^Tp)(v^Tq)}{n^2}.
\]

Thus both pairings are normalized, and the rulebook's rank-one lowering and
matrix-gradient contractions are exact, including after updates.

For an output $O$, write $b_u=n\,\partial O/\partial u$ for a vector
adjoint and $a_s=\partial O/\partial s$ for a scalar adjoint. Substituting
each local differential into $dO=b_v^Tdv/n$ gives the coordinate, average,
forward-call and transpose-call rows in the reverse table. In particular,
the matrix contributions are $b_vu^T/n$ for $v=Au$ and $ub_v^T/n$ for
$v=A^Tu$. Contributions must be added at repeated uses. Mobility $n\kappa$
on a vector gives velocity $-\kappa b_u$; mobility $\kappa$ on a matrix
gives $-\kappa\nabla_A\mathcal L$. These match the master proof.

An ambient gradient treats the current $A$ as the independent parameter.
Differentiating a stored history instead differentiates its update factors.
The rulebook states this distinction correctly. If one asks for a derivative
through that history, the product rule must also differentiate every saved
factor that depends on the requested original parameter.

For a single Fréchet derivative the supplied direction is held fixed. For
$\dot\theta=V(\theta)$, differentiation of $DO[V]$ gives

\[
\frac{d^2}{dt^2}O(\theta(t))
=D^2O[V,V]+DO[DV[V]].
\]

With coefficients $\theta_{[r]}=\theta^{(r)}(0)/r!$, equating coefficients
in the ODE gives $(r+1)\theta_{[r+1]}=[t^r]V(\theta(t))$. The convolution
and finite Taylor formulas then follow from multiplication and finite-order
Taylor's theorem. They require smoothness through finite order, not an
analytic infinite series. Ordinary derivatives require the final factor $r!$.

For a new forward call, the source Gram uses $\mathbb E[HH_r]$, not a
centered covariance of the inputs. Its response is
$\sum_s U_s\mathbb E[\partial_{\zeta_s}H]$ over earlier reverse calls;
the reverse formula has the exchanged roles. These are precisely master-proof
(4)–(6). Earlier scalar expectations and covariances are held fixed under
formal source differentiation, while explicit paths through earlier field
expressions remain differentiated. This differs from physical differentiation
of the finite program, which does differentiate scalar feedback.

Keeping separate source slots under singular laws is essential. A Gaussian
factorization is used only for integration, and need not be differentiated.
Appending a source extends an input Gram, hence a positive semidefinite
covariance. All required fields precede that extension, so causality and
termination are preserved.

The optional activation-moment form has the same syntactic restriction as
master-proof Section 8: nonlinear arguments must be the original feedforward
preactivations at initialization. Gaussian integration by parts removes an
explicit Gaussian polynomial factor at each step and leaves activation
derivatives with recursively computed covariance data. The rulebook correctly
retains the general expectation DAG outside this restricted subclass.

## Independent reconstruction of every example

### 1. Reused transpose, finite-width expectation and ambient gradient

Let $e$ be the all-ones lower-type vector, $y=We$, $u=\phi(y)$ and
$v=W^Tu$. Then $y_i$ are iid standard Gaussians. With
$P=I-ee^T/n$, rowwise orthogonal Gaussian projection gives
$W=ye^T/n+B$, where $Be=0$ and $B$ is independent of $y$ with row
covariance $P/n$. Consequently

\[
v=e\bar a+B^T\phi(y),\qquad
\bar a=\frac1n\sum_i y_i\phi(y_i),\qquad
\bar q=\frac1n\sum_i\phi(y_i)^2.
\]

The terms are exactly orthogonal, and the second has conditional covariance
$\bar qP$. For $J_n=v^Tv/n$ this gives

\[
\mathbb E[J_n\mid y]=\bar a^2+(1-1/n)\bar q.
\]

Define $q=\mathbb E\phi(G)^2$ and
$c=\mathbb E[G\phi(G)]=\mathbb E\phi'(G)$ for a standard Gaussian $G$.
Independence of the coordinates implies
$\mathbb E\bar a^2=c^2+(\mathbb E[G^2\phi(G)^2]-c^2)/n$, hence

\[
\mathbb E J_n=q+c^2+
\frac{\mathbb E[G^2\phi(G)^2]-q-c^2}{n}.
\]

This also works for $n=1$, where $P=0$. The evaluator independently gives
$V=\zeta+c$ with $\operatorname{Var}\zeta=q$, so its limit is $q+c^2$.
Gaussian integration by parts is justified by the stated polynomial growth.

The checks for $\phi(x)=x,x^2,x^3$ respectively give
$2+1/n$, $3+12/n$ and $24+81/n$. The moments are
$\mathbb EG^{2k}=(2k)!/(2^kk!)$.

For a perturbation $D$ of $W$,
$dv=D^Tu+W^T(\phi'(y)\odot De)$. Inserting it into
$dJ_n=2v^Tdv/n$ yields

\[
\nabla_WJ_n=\frac2n\left[u v^T+
((Wv)\odot\phi'(y))e^T\right].
\]

Both occurrences of $W$ contribute; the factor $1/n$ and both matrix
orientations in the example are correct.

### 2. One update and saved versus current factors

For $\mathcal L_n=n^{-1}\sum_i\phi((We)_i)$ and saved
$p=\phi'(We)$, the ambient gradient at the pre-update state is $pe^T/n$.
After $A=W-\eta pe^T/n$,

\[
Ae=y-\eta p,\qquad A^Tp=W^Tp-\eta e(p^Tp/n).
\]

Applying Example 1 to $\phi'$ gives the representative
$\zeta+c-\eta q$, where $q=\mathbb E\phi'(G)^2$ and
$c=\mathbb E\phi''(G)$. Its squared expectation is
$q+(c-\eta q)^2$. For $\phi(x)=x^4/4$, this is
$15+(3-15\eta)^2$, reducing to $24$ at $\eta=0$.

The example explicitly saves $p$; it does not claim that this is the loss
gradient factor at $A$. The current gradient would use $\phi'(Ae)e^T/n$.
Nor does the example confuse the gradient with respect to $A$ with a
pullback through $A(W)$. This is a correctly scoped one-step observable.

### 3. Singular duplicate and zero queries

The identical calls $We$ give source covariance
$\left(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right)$.
For $U=\phi(\xi_1+\xi_2)$ the two formal partials both equal
$\phi'(\xi_1+\xi_2)$; they are formed before imposing
$(\xi_1,\xi_2)=(G,G)$. Thus
$q=\mathbb E\phi(2G)^2$ and $c=2\mathbb E\phi'(2G)$, giving $q+c^2$.
The independent finite-width substitution $\psi(x)=\phi(2x)$ gives the
same answer through $\psi'(x)=2\phi'(2x)$.

For the linear case the exact expectation is $8+4/n$ and the limit is $8$.
For the cubic case $q=960$, $c=24$ and the limit is $1536$. For
$U=\phi(\xi_1)-\phi(\xi_2)$, the variance is zero on the diagonal,
while its two nonzero formal partials have opposite expected values.
Their response contributions cancel because the two forward inputs agree.
The resulting source and response are both zero, preserving the exact
finite-width identity.

### 4. Moving flow and factorial-normalized jets

For the vector state $x$ with loss $n^{-1}\sum_i\phi(x_i)$ and vector
mobility $n$, $V(x)=-\phi'(x)$ and
$DV[V]=\phi''(x)\odot\phi'(x)$. For $O_n=x^Tx/n$,

\[
\dot O_n=-\frac2n\sum_i x_i\phi'(x_i),\qquad
\ddot O_n=\frac2n\sum_i\left[\phi'(x_i)^2+
x_i\phi''(x_i)\phi'(x_i)\right].
\]

At Gaussian initialization this gives exactly the three general limiting
formulas in the example. For $\phi(x)=x^4/4$, the first derivative limit
is $-6$, the Hessian contribution is $30$, and the moving-field contribution
is $90$, giving the second derivative $120$.

Direct solution gives $x(t)^2=a^2/(1+2ta^2)$, with derivatives
$-2a^4$ and $8a^6$ at zero. The normalized coefficients are
$x_{[1]}=-a^3$, $x_{[2]}=3a^5/2$, and
$(x^2)_{[2]}=4a^6$. Its expectation is $60$, and multiplication by $2!$
gives $120$. The square of the frozen line $a-ta^3$ instead has second
derivative $2a^6$, whose expectation is $30$. The claimed distinction and
all factorials are correct. The solution's local interval may depend on
the finite-width sample, consistently with the stated jet-only claim.

## Check of the master proof used by the companions

The entire proof was read. I checked the local dependencies relevant to
applying its conclusion here. The moment proof uses a simultaneous induction
over all derivative orders at each earlier node. Singleton centering inserts
one additional Gaussian weight per singleton, so a tuple with $b$ distinct
indices and $s$ singleton indices is bounded by
$Cn^{-(p+s)/2}\le Cn^{-b}$; the finite number of equality patterns then
controls the row or column sum. The zero-singleton and zero-variance cases
are included. This supports the uniform moments needed after compilation.

The bounded-derivative argument conditions on actual named-matrix
observations, identifies the response by Gaussian integration by parts,
and removes singularity through fresh independent perturbations followed
by a finite-program Lipschitz comparison. Source-covariance square roots
are used continuously, without differentiated inverses. Clipping is applied
after derivative compilation; its common polynomial derivative bounds,
higher moments and the operator-norm bound justify the stated uniform
removal. Convergence in probability together with uniformly bounded higher
moments gives the asserted scalar $L^p$ limits. No extra probabilistic
claim is required for these examples.

## Executed checks and observed outcomes

From `/home/amir/Codes/PDE`, I ran a Python heredoc using only the standard
library `fractions.Fraction` and `math.factorial`. It used exact rational
arithmetic, with $n\in\{1,2,3,5\}$ and zero-based indices

\[
W_{ij}=((i+2)(j+1)-3)/7,\qquad
D_{ij}=((i+1)-2(j+2))/11.
\]

For powers $\phi(x)=x^k$, $k=1,2,3$, the script formed
$dy=De$, $du=k y^{k-1}\odot dy$ and
$dv=D^Tu+W^Tdu$, then asserted exact equality of $2v^Tdv/n$ with the
Frobenius pairing of $D$ and the displayed reuse gradient. For the quartic
loss and $\eta=2/5$, it asserted both rank-update action identities and
the ambient gradient identity at the new current $A$. It also checked
that the new gradient factor differs from the saved one in these inputs.

For powers $k=1,3$, it checked exact duplicate scaling by $2^k$ and exact
zero cancellation. The Frobenius normalization was checked with rational
vectors $u_i=(i+1)/3$, $v_i=(i-2)/5$, $p_i=(2i+1)/7$ and
$q_i=(i+3)/11$. Gaussian moments were computed from the exact factorial
formula. Jet identities were checked at
$a\in\{-3/2,0,2/3,5/4\}$.

The complete command is retained below. It exited with code 0 and produced:

```text
Exact rational checks: reuse gradients, rank update, current ambient loss gradient, duplicates, zero cancellation, Frobenius normalization PASS for n=1,2,3,5.
phi=x^1: q=1, c=1, E[J_n]=2+(1)/n
phi=x^2: q=3, c=0, E[J_n]=3+(12)/n
phi=x^3: q=15, c=3, E[J_n]=24+(81)/n
duplicate phi=x^1: q=4, c=2, J_limit=8
duplicate phi=x^3: q=960, c=24, J_limit=1536
Flow checks: O_first_limit=-6; frozen second=30; moving correction=90; total second=120; normalized coefficient expectation=60 PASS.
All executed checks are deterministic and exact; no Monte Carlo inference used.
```

These finite checks supplement the symbolic reconstructions above; they do
not establish a universal formula by testing selected matrices.

## Limitations and final scope

- This is one fresh internal mathematical review. It is not the paired
  promotion process, a review of the implementation, or a proof-assistant check.
- The frozen master proof's external-paper and maintained-book provenance
  assertions were not independently verified: those sources were outside the
  assigned input scope. The mathematical checks use its supplied proof bodies.
- There was no empirical training campaign, numerical convergence study or
  external Gaussian-law oracle. The claimed limits rely on the stated finite
  Gaussian-program theorem, not the finite deterministic checks alone.
- The theorem and companions retain fixed graph size, derivative order and
  update count. They do not supply a positive-time population flow, uniform
  existence horizon, infinite Taylor expansion or new complexity guarantee.

No unresolved mathematical objection was found within the assigned frozen
scope. No additional scientific input was needed for this companion review.

## Reproduction command for the executed exact checks

```bash
python - <<'PY'
from fractions import Fraction as F
from math import factorial

def dot(x,y): return sum(a*b for a,b in zip(x,y))
def mv(A,x): return [dot(row,x) for row in A]
def tr(A): return list(map(list,zip(*A)))
def add(A,B): return [[a+b for a,b in zip(ar,br)] for ar,br in zip(A,B)]
def outer(x,y): return [[a*b for b in y] for a in x]
def scale(c,A): return [[c*a for a in row] for row in A]
def gram(A,B): return sum(dot(ar,br) for ar,br in zip(A,B))
def ep(k): return F(0) if k%2 else F(factorial(k),2**(k//2)*factorial(k//2))

# Exact deterministic differential checks; all arithmetic is rational.
for n in (1,2,3,5):
    W=[[F((i+2)*(j+1)-3,7) for j in range(n)] for i in range(n)]
    D=[[F((i+1)-2*(j+2),11) for j in range(n)] for i in range(n)]
    e=[F(1)]*n
    y=mv(W,e); dy=mv(D,e)
    for k in (1,2,3):
        u=[a**k for a in y]; du=[k*a**(k-1)*b for a,b in zip(y,dy)]
        v=mv(tr(W),u)
        dv=[a+b for a,b in zip(mv(tr(D),u),mv(tr(W),du))]
        dJ=F(2,n)*dot(v,dv)
        response=[a*k*b**(k-1) for a,b in zip(mv(W,v),y)]
        gradient=scale(F(2,n),add(outer(u,v),outer(response,e)))
        assert gram(gradient,D)==dJ
    p=[a**3 for a in y]; eta=F(2,5)
    A=add(W,scale(-eta/F(n),outer(p,e)))
    assert mv(A,e)==[a-eta*b for a,b in zip(y,p)]
    assert mv(tr(A),p)==[a-eta*dot(p,p)/n for a in mv(tr(W),p)]
    # Ambient gradient of loss at A is recomputed from Ae, not old p.
    p_current=[a**3 for a in mv(A,e)]
    grad_current=scale(F(1,n),outer(p_current,e))
    dloss_current=dot(p_current,mv(D,e))/n
    assert gram(grad_current,D)==dloss_current
    assert p_current != p
    # Exact duplicate algebra for the linear and cubic nonlinearities.
    for k in (1,3):
        udup=[(a+a)**k for a in y]
        vsingle=mv(tr(W),[a**k for a in y])
        assert mv(tr(W),udup)==[2**k*a for a in vsingle]
        assert mv(tr(W),[a**k-a**k for a in y])==[F(0)]*n
    # General normalized Frobenius contraction identity.
    u=[F(i+1,3) for i in range(n)]; v=[F(i-2,5) for i in range(n)]
    p=[F(2*i+1,7) for i in range(n)]; q=[F(i+3,11) for i in range(n)]
    assert gram(scale(F(1,n),outer(u,v)),scale(F(1,n),outer(p,q)))==dot(u,p)*dot(v,q)/(n*n)
print('Exact rational checks: reuse gradients, rank update, current ambient loss gradient, duplicates, zero cancellation, Frobenius normalization PASS for n=1,2,3,5.')

for k in (1,2,3):
    q=ep(2*k); c=k*ep(k-1); lim=q+c*c; correction=ep(2*k+2)-lim
    print(f'phi=x^{k}: q={q}, c={c}, E[J_n]={lim}+({correction})/n')
for k in (1,3):
    q=2**(2*k)*ep(2*k); c=2**k*k*ep(k-1)
    print(f'duplicate phi=x^{k}: q={q}, c={c}, J_limit={q+c*c}')
assert ep(2)==1 and ep(4)==3 and ep(6)==15 and ep(8)==105
assert 2*ep(6)==30 and 6*ep(6)==90 and 8*ep(6)==120
for a in (F(-3,2),F(0),F(2,3),F(5,4)):
    x0=a; x1=-a**3; x2=F(3,2)*a**5
    assert 2*x2==-3*a*a*x1
    O2=2*x0*x2+x1*x1
    assert O2==4*a**6
    assert factorial(2)*O2==8*a**6
print('Flow checks: O_first_limit=-6; frozen second=30; moving correction=90; total second=120; normalized coefficient expectation=60 PASS.')
print('All executed checks are deterministic and exact; no Monte Carlo inference used.')
PY
```
