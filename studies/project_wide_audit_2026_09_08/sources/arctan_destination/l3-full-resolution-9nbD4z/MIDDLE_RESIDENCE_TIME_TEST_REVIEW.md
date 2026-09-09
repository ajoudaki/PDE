# Isolated complete proof audit

**PASS as an auxiliary prescribed-input route test. Required mathematical fixes: none. This is neither a full network theorem nor a canonical-network counterexample.**

Candidate: /tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/MIDDLE_RESIDENCE_TIME_TEST.md

Verified candidate SHA256:

    ed8826fbddbaa0f7710f0fcd0a8496dcb9819f02f75749fb380e437fc120eee0

I read all 227 candidate lines and the solve-math-rigorously instructions at /etc/codex/skills/solve-math-rigorously/SKILL.md. No ledgers, other proof files, external mathematical sources, inherited mathematical context, numerical experiments, or subagents were used. The candidate was not edited. The optional source variant requested subsequently is audited separately in Section 9.

All norms are ordinary Euclidean norms or their induced operator norms. Normalization is explicit. To keep layer indices on network-like fields, write \(A^{(2)},P^{(2)},w^{(2)}\) for the candidate's \(A,P,w\). This labels auxiliary objects; it does not identify them with trained-network fields. Scalar coordinates \(x,y,r,X,Y,\zeta,b\) retain the candidate's notation.

## 1. Elementary theorem hypotheses and mobility

Fix \(S>0\) and an integer \(n\ge2\). The ODE facts used are:

- A continuous vector field on \([0,S]\times\mathbb R^n\), globally Lipschitz in the state uniformly on that interval and bounded at state zero, has a unique solution throughout \([0,S]\) for every initial state. The resulting at-most-linear growth prevents finite-time escape.
- If its state derivative also exists and is jointly continuous, the flow is differentiable in the initial state and its derivative satisfies the variational equation. The uniform derivative bound verified below supplies the needed local control.
- For continuous \(m\ge0,u\ge0\) and a constant \(c\ge0\), \(u(s)\le c+\int_0^s m(t)u(t)\,dt\) implies \(u(s)\le c\exp(\int_0^s m)\). For \(c>0\), apply an integrating factor to \(c+\int_0^s mu\); for \(c=0\), use positive \(c\) and take its limit to zero.

Cone invariance and the other integral formulas are justified below rather than invoked without their hypotheses.

Here \(e_1,u\) are orthonormal and \(\|v\|_2^2=2\). Thus
\[
 h^{\mathsf T}A^{(2)}h=\|h\|_2^2+(v^{\mathsf T}h)^2,\qquad
 \|h\|_2^2\le h^{\mathsf T}A^{(2)}h\le3\|h\|_2^2.
\]
Moreover, \(A^{(2)}v=3v\), and \(A^{(2)}=I\) on \(v^\perp\). Therefore \(I\preceq A^{(2)}\preceq3I\) and \(\|A^{(2)}\|_{\rm op}=3\). Its block on \(E=\operatorname{span}\{e_1,u\}\) is exactly
\[
 \begin{pmatrix}2&1\\1&2\end{pmatrix},
\]
and it is the identity on \(E^\perp\). This verifies the positive scalar-plus-Gram form and bounded norm; no realization through trained weights follows from that algebraic fact.

## 2. Well-posedness and exact auxiliary trajectory

For \(\phi(z)=\arctan z\),
\[
 \phi'(z)=\frac1{1+z^2},\qquad
 \phi''(z)=-\frac{2z}{(1+z^2)^2},\qquad
 |\phi'|\le1,\quad |\phi''|\le2.
\]
For fixed \(n,S\), the prescribed query is smooth in time and
\(Q_{n,S}:=\sup_{s\le S}\max_j|q_j^{(2)}(s)|<\infty\). Consequently its vector field satisfies
\[
 \|f^{(2)}(s,z)-f^{(2)}(s,\widetilde z)\|_2
 \le6Q_{n,S}\|z-\widetilde z\|_2,\qquad
 \|f^{(2)}(s,z)\|_2\le3\|q^{(2)}(s)\|_2.
\]
It is jointly continuous, and the second bound is uniform in the state and bounded over the interval. These check every existence hypothesis above. No width-independent Lipschitz constant is needed.

Substitute \(z_1^{(2)}=1\) and \(z_j^{(2)}=\zeta=1+3\lambda_ns^2/4\) for \(j\ge2\). The gated query \(g^{(2)}:=\phi'(z^{(2)})\odot q^{(2)}\) is
\[
 g_1^{(2)}=-\sqrt n\,s/2,\qquad
 g_j^{(2)}=\lambda_ns\ (j\ge2),\qquad
 g^{(2)}=-\frac{\sqrt n\,s}{2}e_1+\sqrt n\,s\,u.
\]
Here \(\sqrt{n-1}\lambda_n=\sqrt n\). Applying the mobility block gives
\[
 A^{(2)}g^{(2)}=0\,e_1+\frac32\sqrt n\,s\,u.
\]
In ordinary coordinates this is zero in coordinate one and \(3\lambda_ns/2=\zeta'\) elsewhere. The initial values agree, so uniqueness proves the exact trajectory (3). The stationary rare coordinate results from an exact cancellation with the bulk contribution.

## 3. Every normalized bound

Since \(1\le\lambda_n\le\sqrt2\), let \(Z_S=1+3\sqrt2 S^2/4\). Then \(1\le\zeta\le Z_S\) and \(0\le\zeta'\le3\sqrt2 S/2\). Directly,
\[
 \frac{\|z^{(2)}\|_2^2}{n}
 =\frac{1+(n-1)\zeta^2}{n}\le Z_S^2,\qquad
 \frac{\|(z^{(2)})'\|_2^2}{n}
 =\frac{n-1}{n}\frac94\lambda_n^2s^2=\frac94s^2,
\]
\[
 \frac{\|q^{(2)}\|_2^2}{n}
 =s^2+\frac{n-1}{n}\lambda_n^2s^2(1+\zeta^2)^2
 =s^2\{1+(1+\zeta^2)^2\}.
\]
The query derivatives are
\[
 (q_1^{(2)})'=-\sqrt n,\qquad
 (q_j^{(2)})'=\lambda_n(1+\zeta^2+2s\zeta\zeta')\quad(j\ge2),
\]
so
\[
 \frac{\|(q^{(2)})'\|_2^2}{n}
 =1+(1+\zeta^2+2s\zeta\zeta')^2.
\]
A single valid constant in (4) is
\[
 C_S=\max\left\{
 Z_S,\quad \frac32S,\quad
 S\sqrt{1+(1+Z_S^2)^2},\quad
 \sqrt{1+(1+Z_S^2+3\sqrt2 S^2Z_S)^2}
 \right\},
\]
using \(2s\zeta\zeta'\le3\sqrt2 S^2Z_S\). It is finite and independent of \(n\). Also \(q^{(2)}(0)=0\).

For the activation \(h^{(2)}=\phi(z^{(2)})\),
\[
 \frac{\|h^{(2)}\|_2}{\sqrt n}\le\frac\pi2,\qquad
 \frac{\|(h^{(2)})'\|_2}{\sqrt n}
 \le\frac{\|(z^{(2)})'\|_2}{\sqrt n},\qquad
 \frac{\|g^{(2)}\|_2}{\sqrt n}\le\frac{\|q^{(2)}\|_2}{\sqrt n}.
\]
In fact, along this path,
\[
 \frac{\|(h^{(2)})'\|_2}{\sqrt n}=\frac{3s}{2(1+\zeta^2)},\qquad
 \frac{\|g^{(2)}\|_2}{\sqrt n}=\frac{\sqrt5}{2}s,\qquad
 \frac{\|(g^{(2)})'\|_2}{\sqrt n}=\frac{\sqrt5}{2}.
\]
Thus all inherited and temporal bounds hold. These are normalized Euclidean bounds: \(|q_1^{(2)}(S)|=\sqrt n S\) and \(|(q_1^{(2)})'|=\sqrt n\) are not bounded uniformly in width.

## 4. Curvature residence and empirical moments

Writing \(d_j^{(2)}=q_j^{(2)}\phi''(z_j^{(2)})\), substitution gives
\[
 d_1^{(2)}=\frac{\sqrt n}{2}s,\qquad
 d_j^{(2)}=b(s)=-\frac{2\lambda_ns\zeta}{1+\zeta^2}\quad(j\ge2).
\]
Since \(2\zeta\le1+\zeta^2\), one has \(-\lambda_ns\le b\le0\). The rare coefficient is positive on \((0,S]\); all coefficients are zero at time zero. The phrase “entire interval” has this harmless endpoint qualification. “Positive curvature” means the signed product \(q_j^{(2)}\phi''(z_j^{(2)})\), not positivity of \(\phi''(1)\).

With \([a]_+=\max\{a,0\}\),
\[
 I_1^{(2)}:=\int_0^S[d_1^{(2)}]_+\,ds=\frac{\sqrt n S^2}{4},
 \qquad I_j^{(2)}=0\quad(j\ge2).
\]
Hence, for every fixed \(c>0\),
\[
 \frac1n\sum_j e^{cI_j^{(2)}}
 =\frac{e^{c\sqrt n S^2/4}+n-1}{n}\longrightarrow\infty,\qquad
 \frac1n\sum_j I_j^{(2)}=\frac{S^2}{4\sqrt n}\longrightarrow0.
\]
These limits use fixed positive \(S,c\) and \(\log n/\sqrt n\to0\). Equations (6)--(7) and both empirical claims are correct.

## 5. Actual homogeneous response and cone invariance

The state derivative of the auxiliary vector field is jointly continuous and equals
\[
 D_zf^{(2)}(s,z)
 =A^{(2)}\operatorname{diag}(q^{(2)}(s)\odot\phi''(z)),
\]
with norm at most \(6Q_{n,S}\). The initial-state differentiation theorem therefore applies and gives exactly
\[
 (P^{(2)})'=M^{(2)}P^{(2)},\qquad P^{(2)}(0)=I,\qquad
 M^{(2)}=A^{(2)}\operatorname{diag}(d^{(2)}).
\]
There is no missing derivative of \(q^{(2)}\): it is explicitly held fixed. That conclusion would not automatically apply to a trained query depending on the perturbed state.

Both \(E\) and \(E^\perp\) are invariant. Put \(\alpha_n(s)=\sqrt n\,s\). On \(E\), the exact matrix is
\[
 B^{(2)}(s)=
 \begin{pmatrix}\alpha_n&b\\\alpha_n/2&2b\end{pmatrix}.
\]
Therefore \(P^{(2)}e_1=xe_1+yu\) satisfies
\[
 x'=\alpha_nx+by,\qquad y'=\alpha_nx/2+2by,\qquad (x(0),y(0))=(1,0).
\]
This verifies the full coupled system (9), not only its rare diagonal.

To justify the cone without assuming \(x>0\), first solve
\[
 r'=F(s,r):=\alpha_n(s)(1/2-r)+b(s)(2r-r^2),\qquad r(0)=0.
\]
The right-hand side is continuous in time and locally Lipschitz in \(r\), with
\(F(s,0)=\alpha_n/2\ge0\) and \(F(s,1/2)=3b/4\le0\).
On a compact neighborhood of \([0,1/2]\), choose a uniform Lipschitz constant \(L\). The absolutely continuous negative part and upper excess obey, almost everywhere,
\[
 ((-r)_+)'\le L(-r)_+,\qquad
 ((r-1/2)_+)'\le L(r-1/2)_+.
\]
For example, at \(r<0\), \(-F(s,r)\le-F(s,0)+L|r|\le L(-r)\); the other inequality uses \(F(s,1/2)\). Both parts start at zero, so integral comparison keeps them zero. This excludes exit, and compact boundedness permits continuation to \(S\).

Now define
\[
 x(s)=\exp\left(\int_0^s[\alpha_n(t)+b(t)r(t)]\,dt\right)>0,\qquad y=rx.
\]
Then \(x'=\alpha_nx+by\), and
\[
 y'=(r'+r(\alpha_n+br))x=\alpha_nx/2+2by.
\]
The initial values agree, so uniqueness identifies these with the actual response. Thus \(x>0\) and \(0\le y\le x/2\) throughout. No zero of \(x\) was divided by.

For completeness, the complementary homogeneous response is also exact:
\[
 P^{(2)}(s)|_{E^\perp}=\beta(s)I,\qquad
 \beta(s)=\exp\left(\int_0^s b(t)\,dt\right)
 =\left(\frac{2}{1+\zeta(s)^2}\right)^{2/3}.
\]
Indeed \(b=-(2/3)(\log(1+\zeta^2))'\). For \(n=2\), this complementary space has dimension zero.

## 6. Homogeneous growth and logarithmic compatibility

Set
\[
 a_n=\sqrt n-\lambda_n/2
 =\sqrt n\left(1-\frac1{2\sqrt{n-1}}\right)\ge\sqrt n/2>0.
\]
The cone and \(b\ge-\lambda_ns\) give \(-\lambda_ns/2\le br\le0\). Hence
\[
 a_nsx\le x'\le\sqrt n\,sx,\qquad
 e^{a_ns^2/2}\le x(s)\le e^{\sqrt n s^2/2}.
\]
Orthonormality gives \(\|P^{(2)}e_1\|_2^2=x^2+y^2\ge x^2\), proving (11). The trace identity
\[
 \operatorname{Tr}(P^{(2)}(P^{(2)})^{\mathsf T})
 =\sum_{j=1}^n\|P^{(2)}e_j\|_2^2
\]
therefore implies
\[
 \frac1n\operatorname{Tr}(P^{(2)}(s)(P^{(2)}(s))^{\mathsf T})
 \ge\frac1n e^{a_ns^2}\longrightarrow\infty
\]
for each fixed \(s\in(0,S]\), exactly as in (12).

Logarithmic compatibility can be checked without consulting any earlier proof:
\[
 \|M^{(2)}(s)\|_{\rm op}
 \le3\max\{\sqrt n\,s/2,\lambda_ns\}\le3\sqrt n\,s.
\]
The integral equation for \(P^{(2)}\), the operator-norm inequality, and integral comparison yield
\[
 1\le\|P^{(2)}(s)\|_{\rm op}\le e^{3\sqrt n s^2/2},\qquad
 \frac{(\log\|P^{(2)}(s)\|_{\rm op})^2}{n}\le\frac94s^4.
\]
The lower bound one follows from the first response column. This explicitly verifies compatibility with width-normalized squared logarithms. The note's reference to an “earlier” bound is a scope disclaimer, not a theorem dependency; no unspecified external logarithmic theorem is certified here.

## 7. Actual zero-initial forced response

The submitted source is \(\xi e_1\), with one real \(\xi\sim N(0,1)\), constant in time. Thus
\[
 \mathbb E\|\xi e_1\|_2^2=1,\qquad
 n\,\mathbb E[\|\xi e_1\|_2^2/n]=1.
\]
The coefficients are deterministic, so independence is valid. This is an ordinary randomly forced ODE, not white noise or a source with independent coordinates.

Continuous linear coefficients and forcing give a unique solution for each \(\xi\). Linearity and invariance of \(E\) imply
\[
 w^{(2)}=\xi(Xe_1+Yu),\qquad
 X'=\alpha_nX+bY+1,\quad Y'=\alpha_nX/2+2bY,\quad X(0)=Y(0)=0.
\]
The cone concerns deterministic \(X,Y\), not the sign of \(w^{(2)}\) for a negative Gaussian realization.

The claimed boundary calculations are exact:
\[
 Y'|_{Y=0}=\alpha_nX/2\ge0,\qquad
 (Y-X/2)'|_{Y=X/2}=3bX/4-1/2\le0.
\]
At the vertex the velocity is \((1,0)\), in the tangent cone. There is no other point with \(X=0\) in this cone.

A full invariance proof, including non-strict tangencies, follows by setting \(U=Y,\ V=X/2-Y\):
\[
 \begin{pmatrix}U\\V\end{pmatrix}'
 =C(s)\begin{pmatrix}U\\V\end{pmatrix}+
 \begin{pmatrix}0\\1/2\end{pmatrix},\qquad
 C(s)=\begin{pmatrix}\alpha_n+2b&\alpha_n\\-3b/2&0\end{pmatrix}.
\]
Both off-diagonal entries are nonnegative. With \(\mu=2\lambda_nS\), every entry of \(C(s)+\mu I\) is nonnegative, since
\(\alpha_n+2b+\mu\ge\alpha_n-2\lambda_ns+2\lambda_nS\ge0\).
The transformed vector \(e^{\mu s}(U,V)^{\mathsf T}\) has this nonnegative matrix and nonnegative forcing. Successive substitution in its integral equation from zero preserves entrywise nonnegativity. It converges uniformly: with finite matrix bound \(K\) and forcing bound \(G\), the successive terms are bounded by \(GK^jS^{j+1}/(j+1)!\). Uniqueness identifies the limit with the solution. Thus \(U,V\ge0\), or \(X\ge0,\ 0\le Y\le X/2\), on all of \([0,S]\).

It follows that
\[
 X'\ge(\alpha_n+b/2)X+1\ge a_nsX+1.
\]
An integrating factor and \(X(0)=0\) give
\[
 X(S)\ge\int_0^S e^{a_n(S^2-t^2)/2}\,dt
 \ge\frac S2 e^{3a_nS^2/8},
\]
where the last step restricts to \(0\le t\le S/2\). This checks both constants in (14).

The exact forced-response formula is
\[
 w^{(2)}(s)=\xi\int_0^s\Phi^{(2)}(s,t)e_1\,dt,\qquad
 \Phi^{(2)}(s,t)=P^{(2)}(s)(P^{(2)}(t))^{-1}.
\]
The fundamental matrix is invertible: any vector mapped to zero at a time would, by uniqueness for the continuous linear ODE solved backwards on that finite interval, have been zero initially. Differentiating the displayed integral verifies the forced equation and zero initial value. This confirms that the lower bound uses the actual time-dependent propagator.

Finally, orthonormality and \(\mathbb E\xi^2=1\) imply
\[
 n\,\mathbb E\left[\frac{\|w^{(2)}(S)\|_2^2}{n}\right]
 =X(S)^2+Y(S)^2
 \ge\frac{S^2}{4}e^{3a_nS^2/4}\longrightarrow\infty.
\]
This proves (15) without a missing factor of \(n\). Even the normalized second moment itself diverges:
\[
 \mathbb E\left[\frac{\|w^{(2)}(S)\|_2^2}{n}\right]
 \ge\frac{S^2}{4n}e^{3a_nS^2/4}\longrightarrow\infty.
\]
At fixed \(n,S\) all these quantities remain finite. For example, \(X'\le\sqrt n\,sX+1\) gives \(X(S)\le S e^{\sqrt n S^2/2}\), and \(Y\le X/2\) bounds the second moment by \(5S^2e^{\sqrt n S^2}/4\). The growth is in width, not finite-time blow-up.

## 8. Quantifiers, failed inference, and network scope

For every fixed \(S>0\), all integers \(n\ge2\) belong to the constructed family and share one finite \(C_S\) in (4). For every fixed \(c>0\), the empirical exponential curvature moment diverges as \(n\to\infty\). For every fixed \(s\in(0,S]\), the homogeneous normalized trace diverges; the forced estimates hold at every fixed positive horizon. No uniformity over all horizons, or assertion for horizons shrinking with \(n\), is claimed. At zero time the curvature integrals and forced response vanish, while \(P^{(2)}(0)=I\).

The example consequently defeats a width-uniform amplitude conclusion, or a residence argument that would exclude these curvature integrals, if based solely on the stated normalized temporal bounds, zero initial query, bounded activation, and positive bounded mobility in the prescribed-input auxiliary class. It does not defeat a width-dependent bound or an argument using additional assumptions.

The absence of actual trained query equations is essential. The mobility is frozen. The query is prescribed, not generated by upper-layer training or backpropagation. No \(W^{(2)},W^{(3)},W^{(4)}\) satisfying their training updates are constructed. The initial state is deterministic and supplies no Gaussian-initialization event or probability bound. The scalar Gaussian source does not realize a canonical source law. Therefore neither the actual-network response nor a joint mean-field/gradient-flow/gradient-descent theorem is proved or disproved.

The opening and closing scope statements retain these limitations. A successful canonical-network argument must use a restriction beyond this auxiliary assumption set, whether structural, dynamical, or probabilistic. This audit makes no claim about which additional restriction succeeds.

## 9. Separately verified optional source vanishing at zero

This section concerns only the subsequently suggested variant; it is not a change to, or premise needed by, the submitted candidate.

Replace the source in (13) by \(s\xi e_1\). Its ordinary second moment is \(s^2\), its normalized second moment is \(s^2/n\), and the source vanishes at zero. Write its solution as
\(\widetilde w^{(2)}=\xi(\widetilde X e_1+\widetilde Y u)\).
The deterministic first equation has \(+s\) instead of \(+1\). On the upper cone boundary,
\[
 (\widetilde Y-\widetilde X/2)'
 =3b\widetilde X/4-s/2\le0.
\]
The transformed \((U,V)\) equations above now have forcing \((0,s/2)^{\mathsf T}\), still nonnegative. The same proved invariance argument applies, including at time zero when the forcing vanishes.

Hence
\[
 \widetilde X'\ge a_ns\widetilde X+s,\qquad
 \widetilde X(S)\ge
 e^{a_nS^2/2}\int_0^S t e^{-a_nt^2/2}\,dt
 =\frac{e^{a_nS^2/2}-1}{a_n}.
\]
The division is legitimate because \(a_n>0\). Since \(\sqrt n/2\le a_n\le\sqrt n\), this lower bound diverges for fixed \(S>0\). Moreover,
\[
 \mathbb E\left[\frac{\|\widetilde w^{(2)}(S)\|_2^2}{n}\right]
 \ge\frac{(e^{a_nS^2/2}-1)^2}{n a_n^2}
 \ge\frac{(e^{\sqrt n S^2/4}-1)^2}{n^2}
 \longrightarrow\infty.
\]
The optional strengthening is valid and retains exactly the same auxiliary, noncanonical scope.

**Final determination: PASS for the submitted hash as written; no required fixes. The optional variant also checks out independently. Neither result supplies actual trained query equations or a canonical-network counterexample.**
