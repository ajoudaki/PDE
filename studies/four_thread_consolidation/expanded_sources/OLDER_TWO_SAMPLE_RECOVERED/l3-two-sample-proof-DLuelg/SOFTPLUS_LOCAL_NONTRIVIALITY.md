# Local nontriviality of the constructed shifted-softplus path

Proof-author sidecar, 2026-09-06. Conditional local theorem: the local
population construction in the assembly below is accepted as a hypothesis.
This note does not promote its dependency candidates to independently
reviewed theorems. No experiments or agents were used.

## 1. Exact dependencies and scope

All mathematical source inspection was confined to these five files in
`/tmp/l3-two-sample-proof-DLuelg/`:

| File | SHA-256 | Use here |
| --- | --- | --- |
| `SOFTPLUS_LOCAL_POPULATION_ASSEMBLY.md` | `398d12f41a60276cbee91323293c2f64b97055eac935f45ee31b8cac6946c97d` | Hypothesized local regular path, common bounded initial operators and genuine adjoints, raw metric, equations, finite-reference symmetry. |
| `SOFTPLUS_FIXED_PROGRAM_IDENTIFICATION.md` | `875fe50be7d9eb859810504649020ae0005be5f47109ef4f98c0c288cbf5d603` | Fixed globally Lipschitz programs, joint empirical moments, Gaussian conditioning, matrix norm tightness. The uncut initial products are bridged explicitly below. |
| `SOFTPLUS_THREE_CUT_PRIMAL_COMPARISON.md` | `51323710f5c02314f232b3fa8e42a7dc9c0c385530398c009fa28a595bf3f02f` | Assembly's local primal/comparison premise and raw normalization; no further continuation inference. |
| `SOFTPLUS_LOCAL_GAUSSIAN_RESPONSE.md` | `0cf9f84eb9ff99d1831355b56e24034660fe5c0c98722d78b3a8e33c586a5b6b` | Assembly's local construction premise; its trajectory response estimates are not needed for the static bridge proved here. |
| `CONVEX_GATE_CURVATURE_ACTION.md` | `e222051b6b85c07a23243b4c502ae6db4bbf7a2e7c659d0a4393e18f03522b2c` | Section 4's initial Gaussian Gram/nonaffinity argument, restated below. No curvature-action result is imported. |

The three candidate hashes agree with those listed in the assembly.
The proof-writing skill is procedural guidance, not an additional
mathematical dependency. No files cited internally by these candidates
were consulted.

Fix any configuration

\[
 -1\leq\rho<1,\qquad y=(y_1,y_2)\in\{-1,1\}^2,
 \qquad C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},
 \qquad \phi(z)=1+\tfrac1{10}\log(1+\exp z).
 \tag{1}
\]

Write \(p=\phi'\), \(r=\phi''\). Thus
\(0<p<e:=1/10\), \(0<r\leq1/40\), and
\(1\leq\phi(z)\leq2+e|z|\). In particular \(\phi\) is Lipschitz,
and \(p\) is bounded and continuous.

Assume precisely the assembly's local conclusion on \([0,S_*]\),
including its specified initial operators, with \(S_*>0\) and
\(W^{(4)}(0)=0\). Denote \(W^{(2)}_0=A_2\), \(W^{(3)}_0=A_3\).
They act between the separate real spaces
\(E_\ell=L^2(\Omega_\ell)\), have norm at most 10, and their
reverse actions are their actual Hilbert adjoints. A tensor means
\((u\otimes h)f=u\,\mathbb E[hf]\), so
\(\|u\otimes h\|_{\rm HS}=\|u\|_2\|h\|_2\).

For \(|\rho|<1\) the raw first-field norm is
\(\|u\|_{\rm first}^2=\mathbb E_1[u^TC^{-1}u]\).
At \(\rho=-1\), represent the first field by one scalar, with sample
pair \((Z,-Z)\), and use \(\|u\|_{\rm first}^2=\mathbb E_1u^2\).
The squared hidden raw norm is the sum of the squared first norm and
the two squared HS norms. Frozen first-weight directions outside the input span
are irrelevant to this norm and stay frozen, as in the assembly.

**Local conclusion.** There is an \(\varepsilon=\varepsilon(\rho,y)>0\),
with \(\varepsilon\leq S_*\), on which all of the following hold.

* For every hidden layer \(\ell=1,2,3\) and sample \(a=1,2\),
  \[
  Z^{(\ell)}_a(s)=Z^{(\ell)}_{0a}+\tfrac{s^2}{2}J_{\ell a}+o_{L^2}(s^2),
  \qquad
  H^{(\ell)}_a(s)=H^{(\ell)}_{0a}
       +\tfrac{s^2}{2}p(Z^{(\ell)}_{0a})J_{\ell a}+o_{L^2}(s^2),
  \tag{2}
  \]
  where both displayed leading fields have strictly positive L2 norm.
* Each of the three hidden raw parameter blocks has increment
  \(s^2v_\ell/2+o(s^2)\) in its raw norm, with \(\|v_\ell\|>0\).
* For the raw readout Gram
  \(K^{\rm ro}_{ab}(s)=\mathbb E_3[H^{(3)}_a(s)H^{(3)}_b(s)]\),
  \[
  \kappa_y(s):=\tfrac14y^TK^{\rm ro}(s)y
   =\kappa_y(0)+s^2\|v\|_{\rm hiddenraw}^2+o(s^2),
  \qquad \|v\|_{\rm hiddenraw}^2>0.
  \tag{3}
  \]
  In particular \(\kappa_y(s)>\kappa_y(0)>0\) for
  \(0<s\leq\varepsilon\).
* Each of the six laws retains strictly positive squared affine-fit
  error \(\inf_{\alpha,\beta}\mathbb E[(\phi(Z)-\alpha-\beta Z)^2]\)
  throughout \([0,\varepsilon]\).

The asymptotics are at \(s=0+\). They imply nonzero displacement for
every sufficiently small positive time. The argument also gives
\((Z^{(\ell)}_a)'(s)/s\to J_{\ell a}\) and the corresponding
feature and parameter velocity limits. No assertion concerns times
beyond this configuration-dependent local interval.

The proof first identifies the two reused initial transpose laws,
including the unbounded-product bridge, then obtains the jet directly
from the local equations. Positive raw-gradient pairings and sample
symmetry prevent cancellation in individual preactivation movements.
Finally a continuous affine-fit formula propagates initial nonaffinity.

## 2. Initial Gaussian fields and feature Grams

For this section and the static argument, suppress the time-zero
subscript: \(Z_\ell=Z^{(\ell)}_0\), \(H_\ell=\phi(Z_\ell)\),
and \(p_{\ell a}=p(Z_{\ell a})\). Put

\[
 \Gamma_\ell=\mathbb E_\ell[H_\ell H_\ell^T].
 \tag{4}
\]

The initial forward programs use only Lipschitz coordinate maps, so
the fixed-program lemma applies to them as stated. Their population
laws are \(Z_1\sim N(0,C)\), \(Z_2\sim N(0,\Gamma_1)\), and
\(Z_3\sim N(0,\Gamma_2)\), in their respective populations.
These are uncentered feature second moments, not centered covariances.

For \(|\rho|<1\), positive density of \(Z_1\) on \(\mathbb R^2\)
and continuity imply that an almost surely zero linear combination
of \(\phi(Z_{11}),\phi(Z_{12})\) is identically zero as a function
of the two real coordinates. Varying each coordinate, strict
monotonicity forces both coefficients to vanish. Thus \(\Gamma_1>0\).
At \(\rho=-1\), use \(Z_1=(G,-G)\). Exchangeability makes the two
eigenvalues of \(\Gamma_1\) equal to

\[
 \tfrac12\mathbb E[(\phi(G)+\phi(-G))^2]>0,
 \qquad
 \tfrac12\mathbb E[(\phi(G)-\phi(-G))^2]=\tfrac1{200}>0,
 \tag{5}
\]

because the sum is at least 2 and the difference is \(G/10\).
The same full-density argument at layers two and three now proves
\(\Gamma_2,\Gamma_3>0\). All these moments are finite by linear
growth. Each scalar \(Z_{\ell a}\) is a nondegenerate Gaussian.

Define the exact initial reverse jet using the assembly's operators:

\[
 V_0=\tfrac12\sum_a y_aH_{3a},\qquad
 D_{3a}=V_0p_{3a},\qquad Q_{2a}=A_3^*D_{3a},
 \qquad D_{2a}=p_{2a}Q_{2a},
 \qquad Q_{1a}=A_2^*D_{2a},\qquad D_{1a}=p_{1a}Q_{1a}.
 \tag{6}
\]

Every expression is in its proper L2 space by boundedness of the
gates and operators. This alone does not identify the laws of
\(Q_2,Q_1\); that is the purpose of the next two sections.

## 3. Finite static conditioning for both actual transpose queries

Use precisely the Gaussian finite initialization of the fixed-program
candidate. This is an analytic argument, not an experiment. A field
pair is an \(n\)-by-2 matrix, with rows indexed by neurons. Write
\(\|x\|_{n,p}^p=n^{-1}\sum_i|x_i|^p\), using the Euclidean norm
for a row tuple. Define the finite versions of (6) with the original
matrices in both orientations, without cuts.

The forward empirical tuples converge against all continuous
polynomial-growth tests by the admissible forward program. In
particular their empirical moments of every finite order are tight,
and \(\Gamma_{\ell,n}:=H_{\ell,n}^TH_{\ell,n}/n\to\Gamma_\ell\)
in probability. The function
\[
 d_{3a}(z)=\tfrac12\sum_b y_b\phi(z_b)\,p(z_a)
 \tag{7}
\]
has linear growth, although it is not globally Lipschitz as a function
of both coordinates. Applying a continuous polynomial-growth **test**
of the forward tuple identifies all empirical moments of
\((Z_3,H_3,V_0,D_3)\). This step appends no matrix query under the
fixed-program lemma. In particular
\(S_{3,n}:=D_{3,n}^TD_{3,n}/n\to S_3:=\mathbb E_3[D_3D_3^T]\).

Condition on the initial first fields, the two forward answers of
\(W^{(2)}_0\), and the two forward answers of \(W^{(3)}_0\).
For an iid \(N(0,1/n)\) matrix \(W\), observing \(WH=Z\) leaves
the conditional representation

\[
 W=Z(H^TH)^{-1}H^T+\widetilde W P_{H^\perp},
 \tag{8}
\]

where \(\widetilde W\) is fresh with the original Gaussian law.
This follows by orthogonally projecting each Gaussian row onto the
span of the columns of \(H\); the orthogonal Gaussian component is
independent. Formula (8) is used on the event that \(H^TH\) is
invertible. For both hidden forward families that event has probability
tending to one, by (4)--(5); no inverse-moment assertion is needed.

At the first reverse query \(D_{3,n}\) is fixed by the transcript.
Consequently its exact conditional law is

\[
 Q_{2,n}\ \overset d=\ H_{2,n}B_{3,n}^T
       +P_{H_{2,n}^\perp}\mathcal G_{2,n}S_{3,n}^{1/2},
 \qquad
 B_{3,n}=\bigl(D_{3,n}^TZ_{3,n}/n\bigr)\Gamma_{2,n}^{-1},
 \tag{9}
\]

where \(\mathcal G_{2,n}\) has independent standard Gaussian entries
and is independent of the preceding transcript. In particular the
sample covariance of the fresh row before the neuron-space projection
is \(S_{3,n}\). It is not the covariance of \(D_3\) after regressing
it on \(Z_3\). The projection in (9) acts in the lower neuron space.

Here are the moment and averaging details needed to use (9) with
unbounded tests. If \(P\) is a projection of rank at most 2, then
for \(p\geq2\), conditionally on \(P,S\),

\[
 \mathbb E\|P\mathcal G S^{1/2}\|_{n,p}^p
  \leq \frac{c_p\|S\|_{\rm op}^{p/2}}n
                \sum_i P_{ii}^{p/2}
  \leq \frac{2c_p\|S\|_{\rm op}^{p/2}}n.
 \tag{10}
\]

Each row is a centered two-dimensional Gaussian of covariance
\(P_{ii}S\), which proves the first inequality by its Gaussian
moments; \(P_{ii}\leq1\) and \(\sum_iP_{ii}\leq2\) prove the
second. For smaller \(p\), use the RMS bound. Tightness of
\(S_{3,n}\) thus makes the discarded projection negligible in every
empirical Lp norm in probability.

The coefficients \(B_{3,n}\) converge in probability to
\[
 B_3=\mathbb E_3[D_3Z_3^T]\Gamma_2^{-1}.
 \tag{11}
\]
On an event where these coefficients and \(S_{3,n}\) are bounded,
the tuple with the projection dropped has tight empirical moments
of every order: its mean is linear in the old features, and its
added rows are Gaussian with bounded covariance. For a continuous
test of growth degree \(d\), its conditional empirical variance is
bounded by
\[
 \frac{C}{n}\left(1+\frac1n\sum_i|\text{old tuple}_i|^{2d}\right).
 \tag{12}
\]
This tends to zero in probability. Conditional expectations are
Gaussian-integrated tests of the old tuple, continuous in that tuple
and in the bounded coefficients. They converge by the preceding
empirical law, first on compact sets and then globally using
\[
 \frac1n\sum_i |x_i|^d\mathbf1_{|x_i|>L}
       \leq L^{d-q}\|x\|_{n,q}^q,\qquad q>d.
 \tag{13}
\]
The probability of the coefficient-localization complement tends to
zero as its bound increases. Restoring the projection using (10),
uniform continuity on compact sets, and (13) does not change the limit.
This proves joint empirical polynomial-moment convergence in population
two, with law

\[
 Q_2=B_3H_2+\eta_2,\qquad
 \eta_2\sim N(0,S_3),\qquad \eta_2\text{ independent of }Z_2.
 \tag{14}
\]

In particular the **actual** uncut \(Q_{2,n}\) has tight empirical
moments of every finite order. Multiplication by \(p(Z_{2a})\) is
a continuous bounded-gate operation with linear growth. Applying the
established tests identifies the joint tuple including \(D_2\), and

\[
 S_{2,n}:=D_{2,n}^TD_{2,n}/n\longrightarrow
 S_2:=\mathbb E_2[D_2D_2^T].
 \tag{15}
\]

The second transpose requires its own conditioning argument. After
revealing \(Z_{2,n}=W^{(2)}_0H_{1,n}\), the remaining Gaussian
component of \(W^{(2)}_0\) in (8) is independent of its forward
answer and of \(W^{(3)}_0\). Conditional on the first fields and
\(Z_{2,n}\), everything subsequently used to construct
\(H_{2,n},Z_{3,n},D_{3,n},Q_{2,n},D_{2,n}\) is a function of
\(Z_{2,n}\) and \(W^{(3)}_0\). Thus these revelations add no
observation of that remaining \(W^{(2)}_0\) component. This verifies
the conditional independence needed to reuse (8), with \(D_{2,n}\)
now measurable in the enlarged transcript. It gives

\[
 Q_{1,n}\ \overset d=\ H_{1,n}B_{2,n}^T
       +P_{H_{1,n}^\perp}\mathcal G_{1,n}S_{2,n}^{1/2},
 \qquad
 B_{2,n}=\bigl(D_{2,n}^TZ_{2,n}/n\bigr)\Gamma_{1,n}^{-1}.
 \tag{16}
\]

Here \(\mathcal G_{1,n}\) is a fresh array of independent standard
Gaussian entries, independent of this enlarged transcript.
The same estimates (10)--(13), now using the joint population-two
second moments just proved, give

\[
 B_2=\mathbb E_2[D_2Z_2^T]\Gamma_1^{-1},\qquad
 Q_1=B_2H_1+\eta_1,\qquad
 \eta_1\sim N(0,S_2),\qquad \eta_1\text{ independent of }Z_1.
 \tag{17}
\]

They also give joint empirical polynomial-moment convergence in
population one, including \(D_{1a}=p_{1a}Q_{1a}\). This works at
\(\rho=-1\): the inverted matrix here is the positive definite
feature Gram \(\Gamma_1\), not the singular input Gram \(C\).

The assertions (14), (17) concern each population's joint law with
its own forward fields. Reused finite neurons have not been declared
iid. Only the explicitly fresh Gaussian arrays are conditionally iid
before projection; (10)--(13) justify their empirical use. There is
no empirical pairing between different neuron populations.

For explicit response coefficients, ordinary Gaussian integration by
parts gives

\[
 \begin{split}
 (B_3)_{ab}
   &=\tfrac{y_b}{2}\mathbb E_3[p_{3a}p_{3b}]
       +\mathbf1_{a=b}\mathbb E_3[V_0r(Z_{3a})],\\
 (B_2)_{ab}
   &=\mathbf1_{a=b}\mathbb E_2[r(Z_{2a})Q_{2a}]
       +(B_3)_{ab}\mathbb E_2[p_{2a}p_{2b}].
 \end{split}
 \tag{18}
\]

Indeed for a centered Gaussian vector \(X\) of covariance \(\Gamma\),
integration of its density in each independent Gaussian coordinate
gives \(\mathbb E[f(X)X^T]=\mathbb E[\nabla f(X)]\Gamma\).
Here (7) and its first derivatives have at most linear growth, so
the Gaussian boundary terms vanish and all integrals are finite.
For the second line use
\(D_{2a}=p(z_a)[\sum_b(B_3)_{ab}\phi(z_b)+\eta_{2a}]\), holding
\(B_3\) and the independent \(\eta_2\) fixed in differentiation.
Its value and derivatives have at most linear growth in \((z,\eta_2)\),
so Gaussian moments justify both conditioning and integration by
parts. Substitution into (11), (17) proves (18). In particular the
return through the top matrix in the second line is retained.

## 4. Finite truncation bridge to the assembly's actual L2 operators

The preceding finite uncut calculation must be connected to (6) on
the assembly's common spaces. We do this explicitly; the fixed-program
lemma is not applied to the non-Lipschitz maps in (7) or to \(p(z)q\).

Use the assembly's smooth caps \(\tau_R\), which are 1-Lipschitz,
equal the identity on \([-R,R]\), satisfy
\(|\tau_R(x)|\leq\min(|x|,2R)\), and preserve sign. For a fixed
finite \(R\), adjoin only this finite static program:

\[
 \begin{split}
 D_{3a}^R&=p_{3a}\tau_R(V_0),&
 Q_{2a}^R&=A_3^*D_{3a}^R,\\
 D_{2a}^R&=p_{2a}\tau_R(Q_{2a}^R),&
 Q_{1a}^R&=A_2^*D_{2a}^R,\\
 D_{1a}^R&=p_{1a}\tau_R(Q_{1a}^R).
 \end{split}
 \tag{19}
\]

At finite width replace \(A_\ell^*\) by the actual original
matrix transpose. Every nonlinear query instruction now has bounded
first derivatives. Specifically the derivatives of
\(p(z)\tau_R(q)\) are \(r(z)\tau_R(q)\) and
\(p(z)\tau_R'(q)\), bounded by \(2R/40\) and \(e\).
The map \(z\mapsto V_0(z)\) is globally Lipschitz, so the top
composition is admissible as well. The fixed-program lemma therefore
applies at each fixed \(R\), on exactly the common spaces and
operators constructed by the assembly.

Here is the actual L2 comparison, valid both at finite width and in
population, with the appropriate norms. For
\(T_R(X)=\|X-\tau_R(X)\|_2\), one has, samplewise,

\[
 \begin{split}
 \|D_{3a}-D_{3a}^R\|_2&\leq eT_R(V_0),\\
 \|Q_{2a}-Q_{2a}^R\|_2
        &\leq\|A_3\|_{\rm op}\|D_{3a}-D_{3a}^R\|_2,\\
 \|D_{2a}-D_{2a}^R\|_2
        &\leq e\bigl(\|Q_{2a}-Q_{2a}^R\|_2+T_R(Q_{2a})\bigr),\\
 \|Q_{1a}-Q_{1a}^R\|_2
        &\leq\|A_2\|_{\rm op}\|D_{2a}-D_{2a}^R\|_2,\\
 \|D_{1a}-D_{1a}^R\|_2
        &\leq e\bigl(\|Q_{1a}-Q_{1a}^R\|_2+T_R(Q_{1a})\bigr).
 \end{split}
 \tag{20}
\]

For example insert \(\tau_R(Q_{2a})\) between \(Q_{2a}\) and
\(\tau_R(Q_{2a}^R)\) and use the contraction property. Thus the
tails in (20) are of the actual uncut queries, whose finite laws were
proved in Section 3. No unknown tail of an arbitrarily queried L2
operator is substituted for them.

At finite width, for any \(p>2\),
\[
 T_R(X_n)^2\leq\frac1n\sum_i|X_{n,i}|^2\mathbf1_{|X_{n,i}|>R}
              \leq R^{2-p}\|X_n\|_{n,p}^p.
 \tag{21}
\]
Section 3 proves tightness of the rightmost empirical moments for
\(V_{0,n},Q_{2,n},Q_{1,n}\); the Gaussian matrix operator norms
are tight by the fixed-program candidate's norm estimate. Let
\(\mathcal X\) denote the static tuple in any ONE population, including
its forward fields. All empirical tests and pairings below stay within
that population; the conclusions hold simultaneously for the three
populations by a finite union bound. Hence (20) implies, for any \(t>0\),
\[
 \lim_{R\to\infty}\limsup_{n\to\infty}
   \mathbb P\{\|\mathcal X_n-\mathcal X_n^R\|_{n,2}>t\}=0.
 \tag{22}
\]

There is also all-order empirical moment tightness uniform in the
fixed cap parameter. To see this without extrapolating the lemma's
cap-dependent constants, repeat (9) for \(D_3^R\).
The inequalities \(|D_{3a}^R|\leq e|V_0|\) bound its covariance
and regression numerator uniformly in \(R\). On an event where
\(\Gamma_{2,n}^{-1}\) and the forward empirical norms are bounded,
the regression coefficients and Gaussian covariances are consequently
bounded independently of \(R\). Gaussian moments and (10) give
empirical Lp tightness for \(Q_2^R\), for every finite \(p\).
Next \(|D_{2a}^R|\leq e|Q_{2a}^R|\); applying (16) to this
query bounds its regression coefficients by Cauchy--Schwarz and its
Gaussian covariance by its second moment. The same argument yields
tightness for \(Q_1^R,D_1^R\), uniformly in \(R\). All localization
events can be enlarged to have arbitrarily high probability. No
expectations of inverse Grams, nor iid laws for reused neurons, are
required.

In particular (22) is a genuine moment bridge, not merely weak
localization. For \(2<p<q\), interpolation gives
\[
 \|\mathcal X_n-\mathcal X_n^R\|_{n,p}
 \leq\|\mathcal X_n-\mathcal X_n^R\|_{n,2}^{\theta}
       \|\mathcal X_n-\mathcal X_n^R\|_{n,q}^{1-\theta},
 \qquad \frac1p=\frac\theta2+\frac{1-\theta}q.
 \tag{23}
\]
The second factor is tight by the actual and capped moment bounds.
Equations (13), (22)--(23) therefore transfer every fixed continuous
polynomial-growth test. For the needed joint second moments, the
simpler inequality
\[
 |\langle X,Y\rangle_n-\langle X^R,Y^R\rangle_n|
 \leq\|X-X^R\|_{n,2}\|Y\|_{n,2}
      +\|X^R\|_{n,2}\|Y-Y^R\|_{n,2}
 \tag{24}
\]
already suffices.

On the assembly's common spaces, (6) is initially defined just by
bounded L2 operators. Each of its fields is in L2, so its own
\(T_R\) tends to zero by dominated convergence. Applying (20)
with \(\|A_\ell\|\leq10\) proves
\(\mathcal X^R\to\mathcal X\) in L2 on these actual spaces.
For fixed \(R\), the finite capped tuple converges to
\(\mathcal X^R\) by the admissible fixed-program lemma. Combining
this fact with (22) and the population L2 convergence identifies the
law of \(\mathcal X\) with the explicit uncut laws of Section 3:
apply the three-term triangle inequality for bounded Lipschitz
tests, first sending width to infinity and then \(R\) to infinity.
Use (24) and its population counterpart for joint second moments.
Thus (14), (17), and (18) hold for the very adjoints in (6), not only
for an independently constructed scalar model. This completes the
finite static truncation/conditioning bridge.

## 5. Positive definite innovations and motion of all parameter blocks

The two innovation covariances in (14), (17) are strictly positive
definite. For \(u\in\mathbb R^2\),
\[
 u^TS_3u=\mathbb E_3\bigl[V_0^2(u_1p_{31}+u_2p_{32})^2\bigr].
 \tag{25}
\]
For equal labels \(|V_0|\geq1\). For opposite labels \(V_0=0\)
exactly on \(Z_{31}=Z_{32}\), by strict monotonicity of \(\phi\).
Since \(Z_3\) has a positive density on \(\mathbb R^2\), that
diagonal has probability zero. If (25) were zero, continuity and
positive density would give
\(u_1p(z_1)+u_2p(z_2)=0\) everywhere (first off the diagonal in
the opposite-label case, then everywhere by continuity). Varying
each coordinate and using that \(p\) is strictly increasing forces
\(u=0\). Thus \(S_3>0\).

By (14), conditionally on \(Z_2\),
\[
 \operatorname{Cov}(D_2\mid Z_2)
      =\operatorname{diag}(p_{21},p_{22})S_3
                         \operatorname{diag}(p_{21},p_{22})>0.
 \tag{26}
\]
The gates are strictly positive at every finite argument. Taking the
conditional second moment in any fixed nonzero direction proves
\(S_2=\mathbb E_2[D_2D_2^T]>0\). Likewise (17) gives
\[
 \operatorname{Cov}(D_1\mid Z_1)
      =\operatorname{diag}(p_{11},p_{12})S_2
                         \operatorname{diag}(p_{11},p_{12})>0,
 \tag{27}
\]
even when \(Z_1=(G,-G)\). These are positive conditional Gaussian
innovations in the actual initial reused-transpose laws.

Define the hidden raw vector \(v=(v_1,v_2,v_3)\) by
\[
 (v_1)_b=\tfrac12\sum_a C_{ba}y_aD_{1a},\qquad
 v_2=\tfrac12\sum_a y_aD_{2a}\otimes H_{1a},\qquad
 v_3=\tfrac12\sum_a y_aD_{3a}\otimes H_{2a}.
 \tag{28}
\]
At \(\rho=-1\), \(v_1\) means its reduced scalar coordinate
\((v_1)_1\), and \((v_1)_2=-(v_1)_1\). Put
\(Y=\operatorname{diag}(y_1,y_2)\). The rank-one HS pairing gives
\[
 \|v_3\|_{\rm HS}^2=\tfrac14\operatorname{tr}(\Gamma_2YS_3Y)>0,
 \qquad
 \|v_2\|_{\rm HS}^2=\tfrac14\operatorname{tr}(\Gamma_1YS_2Y)>0.
 \tag{29}
\]
For example a positive definite \(\Gamma\) bounds this trace below
by \(\lambda_{\min}(\Gamma)\operatorname{tr}(YSY)>0\).

For each first sample \(b\), the conditional variance of
\((v_1)_b\) is
\[
 \tfrac14 c_bY\operatorname{diag}(p_{11},p_{12})S_2
                   \operatorname{diag}(p_{11},p_{12})Yc_b^T>0,
 \tag{30}
\]
where \(c_b\) is row \(b\) of \(C\). It is a nonzero row since
its diagonal entry is one. Thus each \((v_1)_b\) has positive L2
norm. Finiteness in the first raw metric follows from the assembly's
input-span estimate; positivity follows from
\(\|(v_1)_b\|_2\leq\|v_1\|_{\rm first}\), also at \(\rho=-1\).
This proves strict positivity of every block in (28), for all four
label vectors and every allowed \(\rho\).

## 6. The exact one-sided jet on the local path

Restore time arguments, with (6), (28) still denoting initial fields.
Only the regularity and equations hypothesized from the assembly are
used in this section. The elementary multiplication fact needed is:
if \(X_s\to X\) in L2 and \(b_s\to b\) in probability with
\(|b_s|,|b|\leq M\), then \(b_sX_s\to bX\) in L2. Indeed the
part containing \(X_s-X\) is at most \(M\|X_s-X\|_2\).
For the other part, restrict \(|X|\leq L\), where bounded convergence
in probability gives convergence in L2, and bound its complement by
\(2M\|X\mathbf1_{|X|>L}\|_2\). Then let \(L\) increase.

The readout equation and continuity of the forward fields give
\(W^{(4)}(s)/s\to V_0\) in L2. Apply the multiplication fact at
the top gate, then the continuously varying bounded adjoint, then
the next gate, in order. This gives exactly
\[
 \frac{\delta^{(\ell)}_a(s)}s\longrightarrow D_{\ell a},
 \qquad \ell=3,2,1,\qquad
 \frac{q^{(j)}_a(s)}s\longrightarrow Q_{ja},\quad j=2,1,
 \tag{31}
\]
in the proper L2 spaces. For instance
\(W^{(3)}(s)^*\to A_3^*\) in operator norm, because its HS
increment tends to zero, so applying it to
\(\delta^{(3)}_a(s)/s\to D_{3a}\) is legitimate. The same reasoning
applies to \(W^{(2)}(s)^*\). No differentiability of the full uncut
vector field on an L2 ball is asserted.

Substitution into the hidden equations, using continuity of
\((u,h)\mapsto u\otimes h\) from L2 times L2 to HS, yields
\[
 \frac{\theta'_{\rm hidden}(s)}s\longrightarrow v,
 \qquad
 \theta_{\rm hidden}(s)-\theta_{\rm hidden}(0)
                 =\tfrac12s^2v+o_{\rm raw}(s^2).
 \tag{32}
\]
The second assertion follows by integrating the first: an error
bounded by \(o(1)t\) on \([0,s]\) integrates to \(o(s^2)\).
In particular all three blocks move to leading order by Section 5.

Define recursively
\[
 \begin{split}
 J_{1a}&=(v_1)_a,\qquad F_{1a}=p_{1a}J_{1a},\\
 J_{2a}&=v_2H_{1a}+A_2F_{1a},\qquad F_{2a}=p_{2a}J_{2a},\\
 J_{3a}&=v_3H_{2a}+A_3F_{2a},\qquad F_{3a}=p_{3a}J_{3a}.
 \end{split}
 \tag{33}
\]
All these fields are in L2. Along a C1 L2 curve \(Z\), the bounded
derivative of \(\phi\) gives
\((\phi(Z))'=p(Z)Z'\) in L2. For completeness, the difference
quotient is the product of \((Z(t+h)-Z(t))/h\) and
\(\int_0^1p(Z(t)+u[Z(t+h)-Z(t)])\,du\); the latter is bounded
and converges in probability to \(p(Z(t))\). The multiplication
fact proves the chain rule and continuity of its derivative.

Now \((Z^{(1)}_a)'(s)/s\to J_{1a}\) by (32), and the chain rule
gives \((H^{(1)}_a)'(s)/s\to F_{1a}\). The exact product rule
\[
 (Z^{(2)}_a)'=(W^{(2)})'H^{(1)}_a
                         +W^{(2)}(H^{(1)}_a)'
 \tag{34}
\]
gives \((Z^{(2)}_a)'(s)/s\to J_{2a}\). Repeating the chain rule
and (34) at the top gives the remaining limits with \(J_3,F_2,F_3\).
Integration proves (2). Equivalently
\(J_{\ell a}=(Z^{(\ell)}_a)''(0+)\), where this denotes the
one-sided strong derivative of the first derivative at zero. No C2
regularity on a positive-time interval is needed.

## 7. Positive pairings and individual hidden-field movement

The adjoint identities on the assembly's common spaces imply
\[
 \begin{split}
 \tfrac12\sum_a y_a\mathbb E_1[D_{1a}J_{1a}]
     &=\|v_1\|_{\rm first}^2,\\
 \tfrac12\sum_a y_a\mathbb E_2[D_{2a}J_{2a}]
     &=\|v_2\|_{\rm HS}^2+\|v_1\|_{\rm first}^2>0,\\
 \tfrac12\sum_a y_a\mathbb E_3[D_{3a}J_{3a}]
     &=\|v_3\|_{\rm HS}^2+\|v_2\|_{\rm HS}^2
                             +\|v_1\|_{\rm first}^2>0.
 \end{split}
 \tag{35}
\]

To verify the first identity for \(|\rho|<1\), put
\(b=YD_1/2\), so \(J_1=Cb\). Its left side is
\(\mathbb E b^TCb=\mathbb E(Cb)^TC^{-1}(Cb)\).
At \(\rho=-1\), put \(j=(y_1D_{11}-y_2D_{12})/2\).
Then \(J_1=(j,-j)\) and the same left side equals \(\mathbb Ej^2\),
the reduced raw norm. This verifies the singular endpoint directly.

For the second identity substitute (33). Its direct term is
\[
 \tfrac12\sum_a y_a\langle D_{2a},v_2H_{1a}\rangle
       =\left\langle\tfrac12\sum_a y_aD_{2a}\otimes H_{1a},v_2
         \right\rangle_{\rm HS}=\|v_2\|_{\rm HS}^2.
\]
Move \(A_2\) in the other term to its genuine adjoint. By (6) that
term becomes \(\tfrac12\sum_a y_a\mathbb E_1[D_{1a}J_{1a}]\).
The identical calculation with \(A_3\) proves the last identity.
Every pairing is finite by Cauchy--Schwarz; the argument multiplies
L2 fields only inside integrable pairings.

To pass from a positive sum to each sample, the required symmetry
is of **joint initial and current fields**, not just equality of
\(\mathbb E[H_a(s)^2]\). It follows from the assembly's finite
reference symmetry as follows. Set \(\sigma=y_1y_2\), so
\(y_{3-a}=\sigma y_a\). Exchange the two initial first fields,
keeping both initial matrices the same. This preserves their joint
initial law, including at \(\rho=-1\). In each reference program,
the forward fields exchange sample indices, the readout gains a
factor \(\sigma\), and the reverse fields gain that factor and
exchange indices. Each hidden matrix update is preserved, since
\(\sigma y_{3-a}=y_a\); the first-field update exchanges its sample
indices because \(C\) is invariant under simultaneous exchange.
The cuts are odd, so this induction also holds for every capped
reference. It holds simultaneously for time zero and any finite list
of reference times.

Apply fixed-program convergence to this joint list, then the assembly's
fixed-cap mesh convergence and cap removal in L2. Thus the joint laws
of \((Z^{(\ell)}_1(0),Z^{(\ell)}_1(s))\) and
\((Z^{(\ell)}_2(0),Z^{(\ell)}_2(s))\) are equal. In particular their
displacement norms agree. Dividing by \(s^2/2\) in (2) and passing
to the L2 norm limit gives
\[
 \|J_{\ell1}\|_2=\|J_{\ell2}\|_2,\qquad \ell=1,2,3.
 \tag{36}
\]
Each positive sum in (35) precludes both corresponding \(J\)'s
from being zero; (36) therefore makes each of them nonzero. The
first-layer positivity also follows directly from (30).
Since \(p_{\ell a}>0\) almost surely, \(F_{\ell a}=p_{\ell a}J_{\ell a}\)
is nonzero whenever \(J_{\ell a}\) is, and is in L2 because the gate
is bounded. Consequently
\[
 \lim_{s\downarrow0}\frac{\|Z^{(\ell)}_a(s)-Z^{(\ell)}_a(0)\|_2}{s^2}
       =\tfrac12\|J_{\ell a}\|_2>0,
 \qquad
 \lim_{s\downarrow0}\frac{\|H^{(\ell)}_a(s)-H^{(\ell)}_a(0)\|_2}{s^2}
       =\tfrac12\|F_{\ell a}\|_2>0.
 \tag{37}
\]
This proves the requested movement for every layer and sample, without
trying to infer it from nonzero parameter motion alone.

## 8. The label-mode raw readout kernel changes

Define \(V_3(s)=\tfrac12\sum_a y_aH^{(3)}_a(s)\), so \(V_3(0)=V_0\).
Equations (2), (33) give
\[
 V_3(s)=V_0+\tfrac{s^2}{2}\,DV_3v+o_{L^2}(s^2),
 \qquad DV_3v:=\tfrac12\sum_a y_aF_{3a}.
 \tag{38}
\]
Here \(DV_3\) denotes the bounded linear first-variation map at the
initial hidden state obtained by the recursion (33) with an arbitrary
hidden tangent in place of \(v\). Boundedness follows from the
bounded gates, the two bounded initial operators, the fixed L2
features, and the HS action bound. Formula (38) proves the needed
variation along this path; it does not assume Frechet differentiability
of the nonlinear composition map on an entire L2 neighborhood.

The last pairing in (35) reads exactly
\[
 \langle V_0,DV_3v\rangle_{E_3}
      =\tfrac12\sum_a y_a\mathbb E_3[D_{3a}J_{3a}]
      =\|v\|_{\rm hiddenraw}^2>0.
 \tag{39}
\]
Squaring (38) proves (3). Initial positivity follows also from
\(\kappa_y(0)=y^T\Gamma_3y/4>0\). Under sample symmetry,
\(K^{\rm ro}_{11}=K^{\rm ro}_{22}\) and the eigenvalue in the
direction \(y\) is \(\lambda_y=K^{\rm ro}_{11}+\sigma K^{\rm ro}_{12}
=2\kappa_y\). Thus in the eigenvalue convention its leading change
is \(2s^2\|v\|_{\rm hiddenraw}^2\). These factors specify the raw
readout normalization explicitly.

## 9. Persistence of strict distributional nonaffinity

For a real L2 field \(Z\) with \(\operatorname{Var}Z>0\), elementary
least squares, first minimizing over the intercept and then the
slope, gives
\[
 \mathcal A(Z):=\inf_{\alpha,\beta\in\mathbb R}
             \mathbb E[(\phi(Z)-\alpha-\beta Z)^2]
   =\operatorname{Var}(\phi(Z))
       -\frac{\operatorname{Cov}(Z,\phi(Z))^2}{\operatorname{Var}Z}.
 \tag{40}
\]
The minimizing slope is
\(\operatorname{Cov}(Z,\phi(Z))/\operatorname{Var}Z\) and the
intercept is \(\mathbb E\phi(Z)-\beta\mathbb EZ\), so the infimum
is attained. For each initial \(Z_{\ell a}\), a zero value would
make \(\phi(Z_{\ell a})\) affine in \(Z_{\ell a}\) almost surely.
Its nondegenerate Gaussian law has positive density on all of
\(\mathbb R\). Continuity would therefore make \(\phi\) affine
on all of \(\mathbb R\), contradicting \(\phi''>0\). Hence all
six initial values of \(\mathcal A\) are strictly positive.

L2 convergence \(Z_n\to Z\) implies
\(\phi(Z_n)\to\phi(Z)\) in L2 by Lipschitzness. Means, second
moments, and the cross moment \(\mathbb E[Z_n\phi(Z_n)]\) then
converge by Cauchy--Schwarz. Thus (40) is continuous under L2
convergence whenever \(\operatorname{Var}Z>0\). Along each of the
six local curves, both its variance and its affine-fit error
therefore remain at least half their strictly positive initial
values on some positive subinterval. Taking the minimum of these
six interval lengths, the lengths needed for the positive movement
and kernel asymptotics, and \(S_*\), and decreasing it if needed,
gives the \(\varepsilon>0\) in Section 1.

This continuity proof requires no positive-time support description.
All conclusions are conditional on the assembly's local path on its
stated common spaces. They prove local nontriviality for both label
modes and all \(\rho\in[-1,1)\), with no global existence,
uniform-in-configuration lower bound on movement, finite-width
dynamic convergence, or every-time-after-local conclusion.
