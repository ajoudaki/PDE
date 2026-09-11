# Autonomous evolution driven by an arbitrary training law

Author: `/root/population`. Status: candidate proof, pending the study's
independent complete reviews. No established file is changed by this document.

This component proves full-state construction, law continuity and uniqueness.
The deterministic comparison lemma is proved in `TRANSPORT.md`; its exact form
used here is restated below. The only pre-existing scientific dependencies are
the complete proofs of `docs/special_data_limits.md` III.F.1–9 and
`docs/global_nonlinear.md` A.1–2, C.2. Their fixed-program scopes are
retained. Their finite Gaussian conditioning, singular-query
regularization, generated action construction, bounded multiplier argument and
weighted response proof are needed, not merely their theorem statements.

## 1. Model, state and equations

Write (u=x/\sqrt2\in S^1), and keep the stated cost

\[
 d_{\mathcal Z}((x,y),(x',y'))=|u-u'|+|y-y'|.
\]

Let \(\mathcal H_i=L^2(\Omega_i,\mathbb P_i)\), one separate neuron
probability space per hidden layer. Section 2 constructs these spaces, a
first-row root \(w_0=(g_1,g_2)\in L^2(\Omega_1;\mathbb R^2)\) with law
\(N(0,I_2)\), and a bounded initialized action
\(A_0:\mathcal H_1\to\mathcal H_2\), together with its actual adjoint.
No joint matching of neuron indices in different populations is used.

The state is

\[
 \theta=(w,A,c)\in
 \mathcal E=L^2(\Omega_1;\mathbb R^2)
 \times\mathcal B(\mathcal H_1,\mathcal H_2)\times\mathcal H_2,
 \qquad \theta_0=(w_0,A_0,0),
\tag{P1}
\]

with distance

\[
 D(\theta,\bar\theta)=\|w-\bar w\|_2+
 \|A-\bar A\|_{\rm op}+\|c-\bar c\|_2.
\tag{P2}
\]

Here the first norm sums both input-coordinate squares inside the expectation.
In particular the full first-row root is retained even for a training law
supported on a single input. For every passive or active input define

\[
 Z^1_\theta(x)=w\cdot u,\quad H^1_\theta(x)=\tanh Z^1_\theta(x),\quad
 Z^2_\theta(x)=AH^1_\theta(x),\quad H^2_\theta(x)=\tanh Z^2_\theta(x),
\]
\[
 f_\theta(x)=\mathbb E_2[cH^2_\theta(x)],\quad
 P^2_\theta(x)=c,\quad \delta^2_\theta(x)=\tanh'(Z^2_\theta(x))c,
\]
\[
 P^1_\theta(x)=A^*\delta^2_\theta(x),\qquad
 \delta^1_\theta(x)=\tanh'(Z^1_\theta(x))P^1_\theta(x).
\tag{P3}
\]

Expectations only contract fields in the same population. Set
\((v\otimes h)g=v\mathbb E_1[hg]\). For a probability law \(\mu\) on
\(\mathcal Z\), put \(r_\theta(x,y)=f_\theta(x)-y\), and define

\[
 F_\mu(\theta)=\left(
 -2\int r_\theta(z)\delta^1_\theta(x)u\,d\mu(z),\quad
 -2\int r_\theta(z)\delta^2_\theta(x)\otimes H^1_\theta(x)\,d\mu(z),\quad
 -2\int r_\theta(z)H^2_\theta(x)\,d\mu(z)
 \right).
\tag{P4}
\]

The strong population equation is

\[
 \theta_\mu(t)=\theta_0+\int_0^t F_\mu(\theta_\mu(s))\,ds.
\tag{P5}
\]

All integrals are strong Bochner integrals in the indicated spaces, with
operator norm for the middle component. Section 3 verifies their existence.
The factors two correspond to the unhalved mean squared loss and physical
time. The three stored-weight mobilities are exactly \((n,1,n)\).

## 2. One compatible initialized Gaussian action space

Start the countable language of III.F.7 with the full independent Gaussian
pair \((g_1,g_2)\) at population 1, a zero readout at population 2, constants,
both orientations of one initialized matrix, rational linear combinations,
tanh, smooth clipped products, and a countable family of smooth bounded
globally Lipschitz coordinate functions dense on each finite compact box.
Close under finite composition. The actual finite roots are the two columns
of \(W^{(1)}_0\), and the actual finite action is the same matrix
\(W^{(2)}_0\) in both orientations. They have the required independent laws.

The deterministic finite-program theorem III.F.1, including the proof of
singular-query regularization in III.F.5, identifies the joint limiting law
of every finite collection of these programs. Finite unions share the same
initialized arrays; deleting unused instructions changes no finite vector.
Consequently these joint laws are compatible. The chronological Gaussian
extension construction of III.F.4 and III.F.7 realizes the countable language
on two generated probability spaces. It does not sample a fresh independent
backward answer: independent oriented *source groups* acquire the response
corrections in equations (III.F.9)–(III.F.10).

For clarity, the operator-completion step uses three concrete facts from that
proof. The finite initialized norm obeys

\[
 \mathbb P(\|W^{(2)}_0\|_{\rm op}>10)
 \le2\,9^{2n}e^{-100n/8}\longrightarrow0.
\]

Second-moment convergence passes the inequality
\(\|W^{(2)}_0v\|_2/\sqrt n\le10\|v\|_2/\sqrt n\)
to every rational combination of generated nodes. Exact finite linear
identities and zero squared differences make the limiting assignment
linear and well-defined on its \(L^2\) classes. Generated smooth cylinder
functions are dense in each generated \(L^2\) space: cylinder simple
functions approximate measurable functions, bounded continuous functions
approximate finite-dimensional Borel functions in \(L^2\), and the included
smooth functions approximate those on compact boxes, with tails removed by
truncation. Thus the assignment extends to a bounded map \(A_0\), of norm
at most 10. The reverse assignments extend in the same way. Passing the
exact finite normalized identity

\[
 v^TW^{(2)}_0h/n=((W^{(2)}_0)^Tv)^Th/n
\]

through the finite-program theorem and then through density identifies the
reverse map with \(A_0^*\).

This language can be fixed independently of the training law. Arbitrary
real directions \(u\in S^1\) are limits of rational linear combinations of
the retained root pair; their initial projections have the joint law
\(\mathbb E[(w_0\cdot u)(w_0\cdot v)]=u\cdot v\).
Arbitrary real coefficients in each separately fixed program are obtained
by rational approximation. For continuous coordinate instructions of at
most linear growth, including the backward products in (P3), A.1 supplies
the extension by smooth clipping and \(L^2\) completion. Its proof chooses
one fixed approximation before taking width to infinity and then removes
the approximation, so no growing-program assertion is introduced here.
The response formulas for these fixed neural programs are those in A.2:
bounded derivatives of tanh and its derivative meet the stated hypotheses.

As a result all rational finite laws and rational-mesh Euler calculations,
their finite unions and full first-row updates belong to one common action
realization. A countable list of additional finite laws may equally be
included. Alternatively the preceding completion represents each of their
fixed calculations directly. This construction also includes any finite
list of passive input directions. There is no data-law-dependent arbitrary
extension of the initialized operator and no comparison of a finite matrix
to a population operator in operator norm.

Different causal enumerations have the same finite generated laws because
their finite arrays agree. Their generated spaces are therefore identified
by the \(L^2\) isometry sending each named coordinate expression to its
counterpart. The isometry preserves coordinate operations and intertwines
the actions and adjoints. This is the precise canonical-realization claim.

## 3. A common ball and continuity of the field

Take \(S_0=11\), so \(\|w_0\|_2=\sqrt2\),
\(\|A_0\|_{\rm op}\le10\), and \(c_0=0\) are strictly inside the ball
of radius \(S_0\) in each component. Put \(B=2S_0+2=24\).
On the ball where each component norm is at most \(B\), bounded tanh gives

\[
 \|H^i(x)\|_2\le1,\quad |f(x)|\le B,\quad |r(x,y)|\le B+Y,
 \quad \|\delta^2(x)\|_2\le B,
 \quad \|P^1(x)\|_2,\|\delta^1(x)\|_2\le B^2.
\tag{P6}
\]

Hence the sum of the three norms of (P4) is bounded by

\[
 V=2(B+Y)(B^2+B+1).
\tag{P7}
\]

These bounds are independent of sample number, individual atom weights,
coincident inputs, covariance ranks and the law. Choose a positive
\(T_{\rm ball}=\min\{1,(B-S_0)/(4V)\}\).
Until a first possible exit, every integral or Euler trajectory has
cumulative increment at most \(2T_{\rm ball}V\); it therefore cannot exit
the ball on \([0,2T_{\rm ball}]\). This is an a priori statement for any
solution, not an existence proof.

On this ball, forward expansion and \(\|\tanh'\|_\infty\le1\) give

\[
 \max_{i=1,2}\bigl(\|Z^i_\theta(x)-Z^i_{\bar\theta}(x')\|_2
 +\|H^i_\theta(x)-H^i_{\bar\theta}(x')\|_2\bigr)
 +|f_\theta(x)-f_{\bar\theta}(x')|
 \le C_B\bigl(D(\theta,\bar\theta)+|u-u'|\bigr).
\tag{P8}
\]

The backward fields are jointly continuous in \((\theta,x)\) with values
in the corresponding \(L^2\) spaces. Here is the necessary product detail.
For \(Z_j\to Z\), \(Q_j\to Q\) in \(L^2\), and bounded continuous \(b\),

\[
 b(Z_j)Q_j-b(Z)Q=b(Z_j)(Q_j-Q)+(b(Z_j)-b(Z))Q.
\]

The first term tends to zero in \(L^2\). For the second, restrict to
\(|Q|\le M\), use bounded convergence in probability there, and bound the
complement by \(2\|b\|_\infty\|Q1_{|Q|>M}\|_2\).
Let \(j\to\infty\) and then \(M\to\infty\). Apply this first to
\(\delta^2\), then use operator/adjoint continuity for \(P^1\), and then
apply it to \(\delta^1\). The same argument works when \(x_j\to x\).
Compactness of the circle shows that for \(\theta_j\to\theta\) this
continuity is uniform over \(x\): a contrary sequence has a subsequence of
inputs converging to one input, contradicting joint continuity.

Each integrand in (P4) is therefore continuous as a Banach-valued function
of \(z=(x,y)\) on the compact data space. Its range is compact and hence
separable; uniform boundedness makes it Bochner integrable. This argument
also resolves measurability despite the possibly nonseparable ambient
operator space. The middle integrand can in fact be integrated in the
Hilbert–Schmidt norm, since
\(\|v\otimes h\|_{\rm HS}=\|v\|_2\|h\|_2\) and the corresponding
rank-one difference bound is the same in that norm. Thus every learned
increment of a strong solution constructed below is Hilbert–Schmidt;
\(A_0\) itself need not be.

We shall use joint continuity

\[
 \theta_j\to\theta,\quad\mathcal W_1(\mu_j,\mu)\to0
 \quad\Longrightarrow\quad
 F_{\mu_j}(\theta_j)\to F_\mu(\theta)\text{ in }\mathcal E.
\tag{P9}
\]

To prove it, uniform continuity just established makes the change in the
integrand caused by \(\theta_j\to\theta\) uniformly small on \(\mathcal Z\).
For the remaining fixed continuous Banach-valued function \(g\), take a
coupling with mean distance \(q_j+o(1)\to0\). If
\(\omega_g(a)=\sup_{d(z,z')\le a}\|g(z)-g(z')\|\), then

\[
 \left\|\int g\,d\mu_j-\int g\,d\mu\right\|
 \le\omega_g(a)+2\|g\|_\infty(q_j+o(1))/a.
\]

First let \(j\to\infty\) and then \(a\downarrow0\). This proves (P9)
without invoking differentiability of a nonlinear map on all of \(L^2\).

## 4. Finite reference flows and the comparison estimate

For a fixed finite probability law
\(\nu=\sum_{a=1}^m\omega_a\delta_{(x_a,y_a)}\), discard zero weights
and combine identical atoms if desired. For each rational mesh \(\Delta>0\)
construct the full-state Euler recursion

\[
 \theta^\Delta_{\nu,k+1}=\theta^\Delta_{\nu,k}
                 +\Delta F_\nu(\theta^\Delta_{\nu,k}),\qquad
 \theta^\Delta_{\nu,0}=\theta_0,
\tag{P10}
\]

and interpolate the three parameters linearly between its grid points.
At every separately fixed mesh there are finitely many calls. Expanding
the learned middle action as a finite sum of rank-one increments rewrites
these calls using only \(A_0,A_0^*\), coordinate maps and deterministic
population contractions. These are the fixed neural programs represented
in Section 2. Each contraction is computed from earlier generated nodes;
no prospective trajectory value is supplied. The full first-row update
is included literally in this recursion. Projection on \(u_b\) gives
the first equation of C.2, since \(u_a\cdot u_b=G_{ab}\). Thus its
active fields obey precisely the equations to which that lemma applies,
without requiring the active directions to span \(\mathbb R^2\).
All full-row Euler velocities have the bound (P7).

The C.2 response bound applies here with \(L=d=2\),
\(|G_{ab}|\le1\), marginal first preactivation variance one, zero population
readout, bounded tanh and its first two derivatives, and all mobilities one.
The preliminary source RMS and residual bounds are (P6). Its complete
weighted argument supplies numbers \(\gamma_0,C_0,T_{\rm response}>0\), depending
only on these bounds and \(Y\), for which every separately fixed finite law
and all its Euler mesh states satisfy

\[
 \sup_{\Delta}\sup_{k\Delta\le T_*}\max_a
 \mathbb E_1 e^{\gamma_0|P^1_{\theta^\Delta_{\nu,k}}(x_a)|^2}\le C_0,
 \qquad \sup_{\Delta}\sup_{k\Delta\le T_*}
 \mathbb E_2 e^{\gamma_0|c^\Delta_{\nu,k}|^2}\le C_0,
\tag{P11}
\]

where
\(0<T_*\le\min(T_{\rm ball},T_{\rm response})\).
The constants do not depend on \(m\), the atom weights or Gram rank.
The C.2 proof uses weighted sums of individual subGaussian marginal bounds;
it makes no estimate of a maximum over a data set or Gaussian history.
The full-row updates change none of its active projected recursions.
C.2's hypotheses therefore remain exactly verified.

For later use, define the *integrated individual tail norm*

\[
 \tau_\nu(\bar\theta,R)=
 \|\bar c1_{|\bar c|>R}\|_2+
 \int\|P^1_{\bar\theta}(x)1_{|P^1_{\bar\theta}(x)|>R}\|_2\,d\nu(x,y).
\tag{P12}
\]

`TRANSPORT.md` proves, at finite width and on these population spaces,

\[
 \|F_\mu(\theta)-F_\nu(\bar\theta)\|_{\mathcal E}
 \le C(1+R)\bigl(D(\theta,\bar\theta)+\mathcal W_1(\mu,\nu)\bigr)
       +C\tau_\nu(\bar\theta,R).
\tag{P13}
\]

Its proof couples \((x,y)\) with \((x',y')\), uses (P8), cuts off only
the reference backward factors, and includes the explicit changed input
factor in \(\delta^1(x)u-\bar\delta^1(x')u'\).
In particular no Gaussian tail bound for \(\theta\) is a hypothesis.
From (P11) the Euler-grid reference tails are bounded by
\(C e^{-cR^2}\). Compare two Euler interpolants for the same finite law.
At time \(t\), each assigned velocity uses its preceding grid state.
Their grid-state distance is at most their interpolant distance plus
\(V(\Delta+\Delta')\), by (P7). Apply (P13) at these grid states,
integrate, and use scalar Gronwall. With fixed \(a,c,C>0\),

\[
 \sup_{t\le T_*}D(\theta^\Delta_\nu(t),\theta^{\Delta'}_\nu(t))
 \le Ce^{aR}\bigl((1+R)(\Delta+\Delta')+e^{-cR^2}\bigr).
\tag{P13a}
\]

Fix \(R\), send the meshes to zero, and then send \(R\to\infty\).
The paths are Cauchy in the complete full-state path space. Their limit
\(\theta_\nu\) satisfies the strong integral equation (P5): the
preceding grid states converge uniformly to this continuous path, and
continuity of \(F_\nu\), uniformly on this convergent family of compact
path ranges, passes their integrated assigned velocities to
\(\int_0^t F_\nu(\theta_\nu(s))ds\). This also proves strong \(C^1\)
regularity. At a fixed time, the reference backward fields at preceding
grid states converge in \(L^2\) by Section 3. Taking an almost surely
convergent subsequence and applying Fatou to (P11) transfers its bounds
to the finite-law flow. Hence
\(\tau_\nu(\theta_\nu(t),R)\le C e^{-cR^2}\), uniformly in time.

Integrating (P13) for two resulting finite-law solutions from their common
initial state now gives

\[
 \sup_{t\le T_*}D(\theta_\lambda(t),\theta_\nu(t))
 \le C e^{aR}\bigl((1+R)\mathcal W_1(\lambda,\nu)+e^{-cR^2}\bigr),
 \qquad R\ge1.
\tag{P14}
\]

For completeness, set \(L_R=C(1+R)\) and
\(b_R=C(1+R)q+C e^{-cR^2}\). The integral inequality is
\(D(t)\le\int_0^t(L_RD(s)+b_R)ds\).
Iterating it, or differentiating its scalar upper comparison, gives
\(D(t)\le b_R t e^{L_Rt}\), which is (P14).

## 5. Completion in the training law and identification of the equation

Every probability measure on the compact \(\mathcal Z\) admits finitely
supported approximations \(\nu_j\) with \(\mathcal W_1(\nu_j,\mu)\le1/j\):
take a finite \(1/j\)-net, partition measurably by the first nearest eligible
net point, and move the measure in each cell to that point. The transport
cost is at most \(1/j\); no boundary-zero assumption is needed. One may
choose the net points from a fixed countable dense set of input angles and
labels. The finite laws' weights need not be rational.

For fixed \(R\), (P14) bounds the limiting Cauchy error by
\(C e^{aR-cR^2}\). Let \(R\to\infty\). Thus \(\theta_{\nu_j}\) is
Cauchy in \(C([0,T_*];\mathcal E)\), which is complete. Let
\(\theta_\mu\) be its limit. It stays in the common ball and its forward
fields converge uniformly in time and input by (P8).

The vector fields converge uniformly in time:

\[
 \sup_{t\le T_*}\|F_{\nu_j}(\theta_{\nu_j}(t))-
                         F_\mu(\theta_\mu(t))\|_{\mathcal E}\to0.
\tag{P15}
\]

Indeed a contrary subsequence has times \(t_j\to t\). Uniform state
convergence and continuity of the limiting curve give
\(\theta_{\nu_j}(t_j)\to\theta_\mu(t)\), so (P9) contradicts the
nonvanishing field difference. Equation (P15) passes the finite-law integral
equations to (P5). The field there is continuous in time, so the result is
a strongly \(C^1\) solution. This proves existence of the autonomous
equation, rather than only Cauchy convergence of its scalar predictions.

It remains to transfer the tails in exactly the strength needed for
uniqueness. For fixed \(t\), backward continuity in Section 3 gives

\[
 \sup_x\|P^1_{\nu_j}(t,x)-P^1_\mu(t,x)\|_2\to0,
 \qquad \|c_{\nu_j}(t)-c_\mu(t)\|_2\to0.
\tag{P16}
\]

For \(M<\infty\), the function
\(b_M(s)=\min\{e^{\gamma_0s^2},M\}\) is bounded and globally Lipschitz.
Equation (P16) therefore shows uniform-in-input convergence of its
expectations. The function
\(x\mapsto\mathbb E_1 b_M(P^1_\mu(t,x))\) is continuous, so weak
convergence of \(\nu_j\) passes its integral to \(\mu\). From (P11),

\[
 \int\mathbb E_1 b_M(P^1_\mu(t,x))\,d\mu(x,y)\le C_0.
\]

Let \(M\uparrow\infty\) by monotone convergence. The same argument for
the readout proves

\[
 \sup_{t\le T_*}\int\mathbb E_1 e^{\gamma_0|P^1_\mu(t,x)|^2}\,d\mu(x,y)
 \le C_0,
 \qquad
 \sup_{t\le T_*}\mathbb E_2 e^{\gamma_0|c_\mu(t)|^2}\le C_0.
\tag{P17}
\]

The supremum is legitimate because the preceding argument holds separately
for every \(t\) with the same constants. No common almost-sure bound on
all times or inputs is asserted. In particular (P17) is an *integrated*
input-law bound, not a pointwise continuum-wide subGaussian statement.

The elementary bound
\(s^2 1_{|s|>R}\le C e^{-\gamma_0R^2/2}e^{\gamma_0s^2}\), followed by
Cauchy–Schwarz over \(\mu\), implies

\[
 \sup_{t\le T_*}\tau_\mu(\theta_\mu(t),R)\le C e^{-cR^2}.
\tag{P18}
\]

This is precisely the reference-tail estimate used by (P13).

## 6. Uniqueness, restart and quantitative law continuity

Let \(\widetilde\theta\) be any other strong solution of (P5) on the
same initialized spaces with initial state \(\theta_0\). Its components
are continuous in the topology (P2), its integrals have the meaning in (P4),
and no tail condition is imposed on it. The first-exit bound of Section 3
keeps it in the common ball. Apply (P13) with \(\mu=\nu\), constructed
\(\theta_\mu\) as reference, and (P18). Gronwall gives

\[
 \sup_{t\le T_*}D(\widetilde\theta(t),\theta_\mu(t))
 \le C e^{aR-cR^2}\quad\hbox{for every }R\ge1.
\]

Sending \(R\to\infty\) proves equality. It also proves independence of
the chosen finite-law approximating sequence: (P14) applied across two
approximating sequences gives the same conclusion directly.

For any two arbitrary laws, (P13) and (P18) prove (P14) with
\((\lambda,\nu)\) replaced by \((\mu,\nu)\). For
\(0<q=\mathcal W_1(\mu,\nu)\le1\), choose

\[
 R=K\sqrt{\log(e/q)},\qquad K\ge1,\qquad cK^2\ge2.
\]

Then \(e^{-cR^2}\le q^2\), while
\(1+K\sqrt{\log(e/q)}\le C e^{C\sqrt{\log(e/q)}}\).
Substitution yields

\[
 \sup_{t\le T_*}D(\theta_\mu(t),\theta_\nu(t))
 \le Cq\exp\bigl(C\sqrt{\log(e/q)}\bigr).
\tag{P19}
\]

Constants depend only on \(Y\) and the frozen model and support bounds.
For \(q=0\), the laws coincide and the solutions are identical; the right
side is interpreted as its zero limit. For \(q>1\), the common ball gives
\(D\le6B\), and in particular \(D\le6Bq\). The maximum possible
distance is at most \(2+2Y\).

Equation (P8) now proves the requested whole-input prediction bound and,
more strongly, the same modulus for the \(L^2\) displacement between
the two forward hidden fields, uniformly over time and the circle.
For \(q>1\) the prediction difference is at most \(2B\).

The equation depends only on the current \((w,A,c)\), its coordinate
functions and the fixed training law. At a time \(s<T_*\), restrict the
constructed path to \([s,T_*]\). The preceding uniqueness argument applied
on this interval, with initial distance zero and this path as reference,
gives unique restart among strong solutions staying on the common ball.
No extra response history must be supplied. More intrinsically, close the
current full-row coordinates, readout, actions and adjoints under the same
coordinate operations; their generated \(L^2\) spaces contain their
subsequent Euler constructions and limits. To justify this last statement
without presupposing Gaussian tails for restarted Euler trajectories,
compare such an Euler trajectory directly against the existing solution
as reference. At each time its preceding grid state differs from its
interpolated state by at most \(V\Delta\). Equation (P13), with reference
tails (P18) at that time, gives the upper error
\(Ce^{aR}((1+R)\Delta+e^{-cR^2})\). Sending \(\Delta\to0\) and then
\(R\to\infty\) proves convergence to the reference continuation. The
Euler law integrals also stay in the generated spaces: their continuous
integrands are limits of finite weighted sums using a dense countable
set of input directions, and the generated spaces are closed.
Equal current generated joint laws define the isometry described in
Section 2 and intertwine the equation. Uniqueness identifies their future
laws. This is a restart claim
on the constructed local interval, not global-time well-posedness from
every arbitrary operator state.

## 7. Forward displacement observables and the small readout

The initialized forward fields \(H^i_0(x)\) are the same for every law.
For each hidden layer put

\[
 M_i(\mu,t)=\int\|H^i_{\theta_\mu(t)}(x)-H^i_0(x)\|_2^2\,d\mu(x,y).
\tag{P20}
\]

They average representation motion over the actual training-input law.
Bounded tanh makes the norms inside the square at most 2. The difference
of their squares at a common input is bounded by four times the
\(L^2\) difference of the moving representations. Each field in (P20)
is uniformly Lipschitz in \(u\) by (P8), including the initialized field.
Coupling the two input laws therefore gives

\[
 \sup_{t\le T_*}|M_i(\mu,t)-M_i(\nu,t)|
 \le C\left(q+\sup_{t\le T_*}D(\theta_\mu(t),\theta_\nu(t))\right).
\tag{P21}
\]

Thus any positive finite-time activity margins for a reference finite law
persist in a sufficiently small open \(\mathcal W_1\)-ball. The actual
positive margins, their nondegenerate witness and their finite-width
transfer are proved separately in `NONLAZY.md` and the algorithm-limit
component; (P21) does not assert activity for every law.

Finally the finite stored readout entries have variance \(n^{-2}\), so

\[
 \mathbb E\left[\|W^{(3)}_0\|_2^2/n\right]=n^{-2},\qquad
 \|W^{(3)}_0\|_2/\sqrt n\longrightarrow0\text{ in probability}.
\tag{P22}
\]

Since \(|\tanh|\le1\), its initial prediction is bounded uniformly on
the circle by this RMS norm. The finite algorithm retains this small
random readout; the same-array comparison to a zero-readout fixed
reference has initial distance exactly this quantity, and the comparison
estimate propagates it at every fixed cutoff. Thus zero in (P1) is the
justified population initial condition, not a modified finite optimizer.

This component establishes a positive local interval, autonomous strong
law-driven dynamics, full-state law continuity and its prediction/feature
consequences. It asserts neither fitting nor a risk improvement, feature
superiority, global-time control, or any quantitative finite-width rate.
