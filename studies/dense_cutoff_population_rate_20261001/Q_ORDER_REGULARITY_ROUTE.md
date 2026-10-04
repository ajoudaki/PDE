# Temporal regularity of the actual Legendre closure

2026-10-03. Scoped internal route, frozen before receiving sibling results.
The target is the canonical two-tanh dense network versus its actual
autonomous residual-RMS Legendre closure, with shared Gaussian initialization,
small fixed labels, all physical time, and whole-input prediction error.
This note does **not** prove a sublinear-order root-width comparison or a
prediction lower bound requiring an order larger than \(n^{1/4}\).
Section 6 additionally proves a weaker, actual same-physical-time prediction
lower bound on a fixed input cap, including the whole-sphere norm.

The route gives a quantitative obstruction to a specific proposed repair:
the absolute velocity defect of the actual closure cannot have exponentially
small order dependence. Even with one normalized training input, its unit
history prefix forces, on events of probability tending to one,

\[
 \epsilon_q:=\int_0^\infty\|E_2(t)\|_F\,dt
 \ge c_y\min\{q^{-8},n^{-1}\},\qquad q\ge1.                 \tag{1}
\]

Thus improving only the source estimate cannot absorb the existing
deterministic amplification \(\exp(BY^2\sqrt n)\) at a sublinear order.
This is a limitation of that particular certificate. It does not imply that
the actual prediction discrepancy has the same amplification or the same
lower bound.

Scientific inputs: the setting and complete memory construction in
`paper/main.tex`; complete `paper/results.tex`, `paper/proof_alltime.tex`,
and `paper/proof_tracking.tex`; and this study's complete
`NONORTHOGONAL_DIRECT_ROUTE.md`, `GENERAL_DATA_STABILITY_ROUTE.md`,
`GENERAL_DATA_ASSESSMENT.md`, and `FINITE_MIXED_MOMENT_ROUTE.md`.
The polynomial/defect portion of `paper/proof_finite_time.tex` was also read,
but supplies no additional premise. `docs/index.qmd`, `docs/notation.qmd`,
the canonical-notation skill and its neural reference, the rigorous-math
skill, and the conjecture skill and its contract/audit references were
applied. No experiments, other-study inputs, Git operations, or paper edits
were used.

## 1. One actual admissible instance and its clock histories

Take one training input \(v=x/\sqrt d\) with \(\|v\|_2=1\), and one
fixed label \(0<y\le Y_*\). The first matrix is \(W^{(1)}\), the hidden
matrix is \(W=W^{(2)}\), and the readout is \(w\). For this sample put

\[
 z^{(1)}=W^{(1)}v,\quad h^{(1)}=\tanh z^{(1)},\quad
 z^{(2)}=Wh^{(1)},\quad h^{(2)}=\tanh z^{(2)},\quad
 f=n^{-1}w^\top h^{(2)},\quad r=f-y,\quad \rho=|r|.
\]

Write \(g(z)=\operatorname{sech}^2z\), acting coordinatewise, and define

\[
 \delta^{(2)}=w\odot g(z^{(2)}),\qquad
 k^{(1)}=W^\top\delta^{(2)},\qquad
 \delta^{(1)}=g(z^{(1)})\odot k^{(1)}.
\]

All evolving quantities in Sections 1--4 belong to the actual order-\(q\)
closure; hats are omitted. The dense system enters only in the later
discussion of stability. The first-layer entries initially are independent
\(N(0,1)\), hidden entries are independent \(N(0,1/n)\), and \(w(0)=0\).

On the manuscript's fitting event the residual never reaches zero at a
finite physical time. Since \(r(0)=-y\), it remains negative. Consequently
the normalized residual is exactly \(r/\rho=-1\). Set

\[
 s=\tau-1,\qquad \frac{ds}{dt}=\rho.
\]

A prime below denotes differentiation in \(s\), only in the displayed
clock equations. The first layer and readout obey exactly

\[
 (W^{(1)})'=2\delta^{(1)}v^\top,\qquad
 w'=2h^{(2)},\qquad
 (h^{(1)})'=2g(z^{(1)})^2\odot k^{(1)}.                \tag{2}
\]

The backward history stored by the closure is \(b=-\delta^{(2)}\), zero
on the unit prefix. The forward history equals \(h^{(1)}_0\) on that
prefix. A subscript zero denotes initialization. With \(\Pi_q^{1+s}\)
the orthogonal degree-below-\(q\) projection on \([0,1+s]\), reconstruction
therefore is

\[
 W(s)-W_0=\frac2n\int_0^{1+s}
       (\Pi_q^{1+s}\delta^{(2)})(\xi)
       (\Pi_q^{1+s}h^{(1)})(\xi)^\top\,d\xi.          \tag{3}
\]

In (3), \(\delta^{(2)}\) means its zero-prefix extension. This is the
original autonomous reconstruction evaluated on its own histories. No
dense or externally prescribed trajectory is substituted.

Define two initialized vectors

\[
 U=2g(z^{(2)}_0)\odot h^{(2)}_0,\qquad
 V=g(z^{(1)}_0)^2\odot W_0^\top U.                    \tag{4}
\]

The square in the second formula is coordinatewise. These vectors are
independent of the closure order.

## 2. Uniform initial-clock expansion

Assume initially \(\|W_0\|_{\rm op}\le K_0\). There are positive
constants \(s_0,C\), depending on \(K_0\) but not on \(n,q\), such that
for every reached clock value \(0\le s\le s_0\),

\[
 \begin{aligned}
  \|W(s)-W_0\|_F&\le Cs^2,\qquad \|w(s)\|_\infty\le2s,\\
  \frac{\|z^{(1)}(s)-z^{(1)}_0\|_2+
              \|h^{(1)}(s)-h^{(1)}_0\|_2}{\sqrt n}&\le Cs^2,\\
  \frac{\|z^{(2)}(s)-z^{(2)}_0\|_2+
              \|h^{(2)}(s)-h^{(2)}_0\|_2}{\sqrt n}&\le Cs^2,\\
  \frac{\|\delta^{(2)}(s)-sU\|_2}{\sqrt n}&\le Cs^3,\\
  \frac{\|h^{(1)}(s)-h^{(1)}_0-s^2V\|_2}{\sqrt n}
      &\le C\sqrt n\,s^4.                             \tag{5}
 \end{aligned}
\]

Here is a proof that keeps the constants uniform in the autonomous order.
Temporarily stop at \(\|W-W_0\|_{\rm op}=1\). Bounded tanh and (2) give
\(\|w\|_\infty\le2s\), hence
\(\|\delta^{(2)}\|_2/\sqrt n\le2s\). The first-layer equations then give
the second line of (5). In (3), split the forward history into its constant
part \(h^{(1)}_0\) and its zero-prefix change. Constants are represented
exactly by every projection order, and orthogonality gives

\[
 \begin{aligned}
 W-W_0=\frac2n\bigg[&
  \left(\int_0^s\delta^{(2)}(u)\,du\right)(h^{(1)}_0)^\top\\
 &+\int_0^{1+s}(\Pi_q^{1+s}\delta^{(2)})
             (\Pi_q^{1+s}(h^{(1)}-h^{(1)}_0))^\top\,d\xi\bigg].
                                                               \tag{6}
 \end{aligned}
\]

Projection contraction bounds the two terms by \(Cs^2\) and \(Cs^4\),
respectively: the normalized squared history norms of the two zero-prefix
factors are at most \(Cs^3\) and \(Cs^5\). Decreasing \(s_0\) makes the
bound in (6) smaller than the stopped operator margin and excludes that
stop. Forward subtraction proves the third line of (5).

Integrating \(w'=2h^{(2)}\) gives
\(\|w-2sh^{(2)}_0\|_2/\sqrt n\le Cs^3\). Boundedness and Lipschitz
continuity of \(g\), together with \(\|h^{(2)}_0\|_\infty\le1\), prove
the fourth line. It also follows that

\[
 \frac{\|k^{(1)}(s)-sW_0^\top U\|_2}{\sqrt n}\le Cs^3.
                                                               \tag{7}
\]

Finally subtract \(2sV\) from the last equation of (2). The contribution
of (7) is \(Cs^3\) in RMS. For the changed first-layer gate, use

\[
 \begin{aligned}
 &\frac{\|[g(z^{(1)}(s))^2-g(z^{(1)}_0)^2]
                    \odot W_0^\top U\|_2}{\sqrt n}\\
 &\hspace{2em}\le
 C\|W_0^\top U\|_\infty
       \frac{\|z^{(1)}(s)-z^{(1)}_0\|_2}{\sqrt n}
 \le C\sqrt n\,s^2.
 \end{aligned}
\]

The last step uses
\(\|W_0^\top U\|_\infty\le\|W_0^\top U\|_2\le C\sqrt n\).
Multiplication by \(2s\) and integration prove the final line of (5).
This deliberately retains the deterministic width loss; no evolved
Gaussian-tail statement is needed.

The clock interval used below is attained in finite physical time.
Indeed \(|f(s)|\le\|w(s)\|_\infty\le2s\). For \(s\le y/4\), this
implies \(\rho=y-f\ge y/2\). Thus a nonstationary globally existing
closure cannot approach an unreached clock endpoint below \(y/4\).

## 3. The initialized coefficients do not vanish

There are constants \(u_*,v_*>0\) and initialization events of probability
tending to one on which, simultaneously,

\[
 \|W_0\|_{\rm op}\le K_0,\qquad
 \|U\|_2/\sqrt n\ge u_*,\qquad
 \|V\|_2/\sqrt n\ge v_* .                             \tag{8}
\]

To verify this using only initialization, the coordinates of
\(z^{(1)}_0\) are iid \(N(0,1)\). Let

\[
 Q=\mathbb E\tanh^2 G>0,\quad G\sim N(0,1),\qquad
 Q_n=n^{-1}\|h^{(1)}_0\|_2^2\longrightarrow Q.
\]

Conditional on the first layer, the coordinates of \(z^{(2)}_0\) are iid
\(N(0,Q_n)\). Bounded conditional second moments and continuity in the
variance therefore give, with \(Z\sim N(0,Q)\),

\[
 \begin{aligned}
  n^{-1}\|U\|_2^2
   &\longrightarrow 4\mathbb E[g(Z)^2\tanh^2Z]>0,\\
  n^{-1}U^\top z^{(2)}_0
   &\longrightarrow 2\mathbb E[Zg(Z)\tanh Z]>0.
                                                               \tag{9}
 \end{aligned}
\]

Both integrands are bounded; the second is strictly positive away from
zero. Define an auxiliary initialized vector only for this estimate by

\[
 D_i=\frac{h^{(1)}_{0,i}}{g(z^{(1)}_{0,i})^2}
      =\tanh(z^{(1)}_{0,i})\cosh^4(z^{(1)}_{0,i}).
\]

Its squared Gaussian expectation is finite, since
\(D_i^2\le\cosh^8(z^{(1)}_{0,i})\) and a Gaussian has finite
exponential moments of every linear multiple of its absolute value.
The law of large numbers bounds \(\|D\|_2/\sqrt n\) by a fixed constant
with probability tending to one. The exact pairing

\[
 \frac{V^\top D}{n}
  =\frac{U^\top W_0h^{(1)}_0}{n}
  =\frac{U^\top z^{(2)}_0}{n}
\]

and Cauchy--Schwarz now give the lower bound on \(V\) in (8).
The operator bound is the manuscript's initialized Gaussian bound.
Intersect (8) with its common fitting event; the probability still tends
to one. These events involve only initialization and are independent of
the order. One sample has a strictly positive limiting readout-feature
Gram, so this instance satisfies the manuscript's fitting hypotheses.

## 4. A lower bound for the actual absolute velocity defect

For \(A=1+s\), the endpoint projection kernel is

\[
 K_q^A(A,\xi)=\frac1A\sum_{j=0}^{q-1}(2j+1)p_j(\xi/A).
\]

Since \(|p_j|\le1\) on \([0,1]\),
\(|K_q^A(A,\xi)|\le q^2/A\le q^2\). The zero prefixes and (5) imply

\[
 \begin{aligned}
  \frac{\|(\Pi_q^A\delta^{(2)})(A)\|_2}{\sqrt n}
    &\le Cq^2s^2,\\
  \frac{\|(\Pi_q^A(h^{(1)}-h^{(1)}_0))(A)\|_2}{\sqrt n}
    &\le Cq^2s^3.                                      \tag{10}
 \end{aligned}
\]

Choose \(\eta>0\), independent of width and order, small enough that
\(\eta\le\min\{s_0,y/4,1\}\) and all the error fractions below are at
most one half. Put

\[
 s_* =\eta\min\{q^{-2},n^{-1/4}\}.
\]

For \(0\le s\le s_*\), one has
\(q^2s\le\eta\) and \(\sqrt n\,s^2\le\eta^2\). Combining
(5), (8), and (10), and using exact reproduction of \(h^{(1)}_0\), gives

\[
 \begin{aligned}
 \frac{\|\delta^{(2)}(s)-(\Pi_q^{1+s}\delta^{(2)})(1+s)\|_2}{\sqrt n}
   &\ge \tfrac12u_*s,\\
 \frac{\|h^{(1)}(s)-(\Pi_q^{1+s}h^{(1)})(1+s)\|_2}{\sqrt n}
   &\ge \tfrac12v_*s^2.                               \tag{11}
 \end{aligned}
\]

The interval is reached by the preceding clock argument. There is only
one sample, so the defect is a single outer product and has no cancellation
between sample terms. The exact autonomous defect formula reads

\[
 E_2=\frac{2\rho}{n}(b-b^*)(h^{(1)}-h^{(1)*})^\top,
 \qquad b=-\delta^{(2)}.
\]

Changing variables \(ds=\rho\,dt\), the rank-one Frobenius identity and
(11) give

\[
 \begin{aligned}
 \epsilon_q
 &\ge2\int_0^{s_*}
   \frac{\|\delta^{(2)}-\delta^{(2)*}\|_2}{\sqrt n}
   \frac{\|h^{(1)}-h^{(1)*}\|_2}{\sqrt n}\,ds\\
 &\ge \frac{u_*v_*}{8}s_*^4
   =c_y\min\{q^{-8},n^{-1}\}.
 \end{aligned}
\]

This proves (1) uniformly over all integer orders on the common event.
The histories depend on \(q\); the proof handles that dependence through
the order-uniform local expansion (5). It is therefore stronger than
observing a nonsmooth join in one fixed history and then varying a separate
offline projection order.

The lower exponent eight is conservative. It is enough for the stated
obstruction, and is not asserted to be the sharp asymptotic source rate.

## 5. What this resolves and what it does not

The local formulas also identify the exact regularity defect at the unit
prefix:

\[
 b'(1+)=-U\ne0=b'(1-),\qquad
 (h^{(1)})'(1+)=(h^{(1)})'(1-)=0,\qquad
 (h^{(1)})''(1+)=2V\ne0=(h^{(1)})''(1-).
\]

Here derivatives are with respect to the full clock coordinate. The actual
finite-dimensional physical ODE is analytic near initialization when
\(y>0\), but its extended histories are not globally analytic: the
backward history is not \(C^1\), and the forward history is not \(C^2\).
The small total clock increment \(\tau(\infty)-1=O(y)\) does not erase
these joins for fixed nonzero labels. The quantitative lower bound uses
only a shrinking initial part of that increment and requires no endpoint
regularity claim at infinite physical time.

The direct-energy bound already available in this study is

\[
 \sup_{t\ge0}d_n(\widehat\theta,\theta_D)
 \le C\exp\{CY+CK_{n,q}\}\epsilon_q,\qquad
 K_{n,q}\le CY^2\sqrt n.
\]

If one uses only this deterministic bound on \(K_{n,q}\), the resulting
certificate has a factor \(\exp(BY^2\sqrt n)\), with a positive fixed
\(B\). For every order \(q\le n\), (1) gives

\[
 \exp(BY^2\sqrt n)\epsilon_q
 \ge c_y\exp(BY^2\sqrt n)n^{-8}\longrightarrow\infty.
\]

Hence even an optimal estimate of this same absolute source cannot make
that particular worst-case stability certificate yield a root-width bound
at sublinear order. Removing the width-dependent amplification, retaining
signed cancellation, or proving control of the actual defect-response
directions remains necessary for that approach.

Equation (1) alone gives no lower bound on a signed accumulated matrix
discrepancy, on \(d_n\), or on prediction error. Absolute velocity errors
can cancel or be damped. Section 6 performs the additional signed calculation
for this particular initial interval. Its resulting prediction lower bound
is too weak to force the requested order barrier. Neither result supplies a
counterexample to sublinear-order tracking or an actual-data construction
requiring \(q=\omega(n^{1/4})\).

| Claim | Status |
|---|---|
| Actual closure has the uniform initial-clock expansion (5) | Proved on the initialized operator event |
| Initial coefficients in (4) have positive RMS lower bounds | Proved with probability tending to one |
| Actual integrated absolute defect obeys (1), all orders | Proved on the common event |
| Analytic physical time plus a short clock interval yields exponentially small actual defect | Ruled out by this admissible instance |
| Source improvement alone absorbs the existing deterministic exponential width factor | Ruled out for that certificate |
| The canonical general-data root-width theorem at sublinear order | Still open |
| Actual same-time whole-input prediction lower bound | Proved in Section 6, but too weak for an order barrier |
| Actual prediction lower bound forcing order above \(n^{1/4}\) | Not obtained |

The missing implication remains a stability estimate for the actual
structured defect, or a sufficiently strong prediction-level lower bound.
Temporal regularity alone does not complete either target.

## 6. A weaker actual prediction lower bound

After freezing Sections 1--5, the supervisor requested a check of whether
the same initial-clock calculation retains a sign at the prediction level.
The following extension was derived without sibling findings. It proves,
for the uniform probability law \(\mu\) on the input sphere and the same
single training input,

\[
 \mathcal E_\mu(\widehat f_{n,q},f_{n,D})
 \ge c_{y,\mu}\min\{q^{-10},n^{-5/4}\}                 \tag{12}
\]

simultaneously in \(q\), on events of probability tending to one. More
generally it holds for any fixed query law giving positive mass to the cap
constructed below. The error is between the two actual systems at the same
physical time. The lower bound never exceeds its \(n^{-5/4}\) branch, and
therefore imposes no necessary order growth for an \(n^{-1/2}\) target.

### 6.1 Equal-activity parameter expansion

Initially compare the two actual trajectories at the same activity value
\(s\); the conversion to equal physical time is done in Section 6.3.
Let \(\Delta W^{(1)},\Delta W,\Delta w\) denote closure minus dense at
that activity. The initialized quantities \(U,V\) are those of (4), and
put

\[
 a_n=\frac{V^\top h^{(1)}_0}{n},\qquad
 \alpha(s)=q^2s+\sqrt n\,s^2.
\]

This \(a_n\) is an initialized scalar used only in this section; it is not
the width remainder denoted by the same letter in the manuscript.
For \(s\le\eta\min\{q^{-2},n^{-1/4}\}\), after decreasing the fixed
\(\eta\), the expansions are

\[
 \begin{aligned}
 \Delta W(s)&=-\frac{UV^\top}{2n}s^4+R_W(s),
       &\|R_W(s)\|_F&\le Cs^4\alpha(s),\\
 \Delta w(s)&=-\frac{a_n}{5}
              [g(z^{(2)}_0)\odot U]s^5+R_w(s),
       &\frac{\|R_w(s)\|_2}{\sqrt n}&\le Cs^5\alpha(s),\\
 &&\frac{\|\Delta W^{(1)}(s)\|_F}{\sqrt n}&\le Cs^6.
                                                               \tag{13}
 \end{aligned}
\]

To justify the feedback remainders, (5) and (10) first give the *signed*
clock defect

\[
 \frac{E_2}{\rho}
   =-\frac{2UV^\top}{n}s^3+R_E(s),\qquad
 \|R_E(s)\|_F\le Cs^3\alpha(s).                       \tag{14}
\]

In particular its norm is at most \(Cs^3\) on the stated interval.
Let \(e_1,e_2,e_w\) be the three normalized discrepancy block norms,
namely \(\|\Delta W^{(1)}\|_F/\sqrt n\),
\(\|\Delta W\|_F\), and \(\|\Delta w\|_2/\sqrt n\).
Subtracting the actual clock equations gives the integral inequalities
corresponding to

\[
 \begin{aligned}
 D^+e_1&\le C[e_w+se_2+\sqrt n\,s e_1],\\
 D^+e_2&\le C[e_w+s(e_2+e_1)]+Cs^3,\\
 D^+e_w&\le C(e_2+e_1).                               \tag{15}
 \end{aligned}
\]

For the first line, the only larger factor is a changed first-layer gate
times a dense carrier. Its maximum is bounded by
\(\|k_D^{(1)}\|_2\le C\sqrt n\,s\). The top gate is multiplied by
\(\|w_D\|_\infty\le2s\), giving the other terms. The second line
uses the rank-one update identity; the third uses forward subtraction.

For a terminal \(s\), let \(X,Y_1,Z\) be the suprema through that time of
\(e_2(u)/u^4,e_w(u)/u^5,e_1(u)/u^6\). Integral forms of (15) give

\[
 Y_1\le C(X+s^2Z),\quad
 Z\le C(X+Y_1)+C\sqrt n\,s^2Z,\quad
 X\le C+Cs^2(X+Y_1)+Cs^4Z.
\]

They can equivalently be proved by a first-exit bootstrap from zero.
At every fixed \(n,q\), smoothness near the initial nonzero residual and
the \(O(s^3)\) source start that bootstrap: the successive integral
equations first give \(e_2=O(s^4)\), \(e_w=O(s^5)\), \(e_1=O(s^6)\)
with possibly nonuniform constants. Since
\(\sqrt n\,s^2\le\eta^2\), absorption of the displayed inequalities
then gives \(X,Y_1,Z\le C\) uniformly in \(n,q\).

The difference of the canonical hidden velocities now integrates to
\(O(s^6)\) in Frobenius norm. Integrating (14) supplies the first line
of (13); \(s^6\le s^4\alpha(s)\). For the training input, forward
subtraction and the Taylor formula for tanh give

\[
 \Delta h^{(2)}(s)
  =-\frac{a_n}{2}[g(z^{(2)}_0)\odot U]s^4
       +O_{\rm RMS}(s^4\alpha(s)).                    \tag{16}
\]

Here \(O_{\rm RMS}(R)\) means a vector of Euclidean norm at most
\(C\sqrt n R\). To check the potentially larger gate remainder, the
base preactivation has RMS displacement \(Cs^2\), hence maximum
displacement \(C\sqrt n\,s^2\). The changed preactivation has RMS
\(Cs^4\). Their product bounds the Taylor remainder by
\(C\sqrt n\,s^6\); the quadratic changed-preactivation remainder is
at most \(C\sqrt n\,s^8\). Both are included in (16). Integrating
\(\Delta w'=2\Delta h^{(2)}\) proves the second line of (13).

### 6.2 A positive initialized coefficient on a fixed query cap

The scalar \(a_n\) is positive with a fixed margin with probability
tending to one. To prove this, condition on the first-layer vectors and put
\(h=h^{(1)}_0\), \(\widetilde h=g(z^{(1)}_0)^2\odot h\). Then

\[
 Q_n=\|h\|_2^2/n\to Q>0,\qquad
 B_n=h^\top\widetilde h/n
   \to B:=\mathbb E[\tanh^2G\operatorname{sech}^4G]>0.
\]

In one initialized matrix row, \(Z=W_{0,j,:}h\) and
\(T=W_{0,j,:}\widetilde h\) are jointly Gaussian with
\(\operatorname{Var}Z=Q_n\), \(\operatorname{Cov}(Z,T)=B_n\).
Gaussian regression gives
\(\mathbb E[T\mid Z]=(B_n/Q_n)Z\). This identity follows by writing
\(T=(B_n/Q_n)Z+\widetilde Z\); its centered Gaussian remainder has
zero covariance with \(Z\) and is independent of it. The rows are
conditionally independent and the relevant second moments are bounded, so

\[
 a_n=\frac1n\sum_j2g(Z_j)\tanh(Z_j)T_j
 \longrightarrow \frac BQ\,2\mathbb E[Zg(Z)\tanh Z]>0,
 \qquad Z\sim N(0,Q).                                 \tag{17}
\]

Intersect the initial event with \(a_n\ge a_*>0\) and with the usual
bound on \(\|W^{(1)}_0\|_F/\sqrt n\). Its probability still tends to
one.

For a normalized query direction \(u=x/\sqrt d\) on the unit sphere,
let \(h^{(1)}_0(u),h^{(2)}_0(u),z^{(2)}_0(u)\) be its initialized forward
features. Define the scalar initialized function

\[
 \begin{aligned}
 J_n(u)={}&
 \frac{V^\top h^{(1)}_0(u)}n
 \frac{(h^{(2)}_0)^\top[g(z^{(2)}_0(u))\odot U]}n\\
 &+\frac{a_n}{5}
   \frac{[g(z^{(2)}_0)\odot U]^\top h^{(2)}_0(u)}n.
                                                               \tag{18}
 \end{aligned}
\]

At the training direction \(u=v\),

\[
 J_n(v)=\frac35a_n\frac{\|U\|_2^2}{n}\ge j_*>0.       \tag{19}
\]

All normalized feature maps in (18) are Lipschitz in \(u\), with a
constant independent of width on this event: use bounded slopes,
\(\|W^{(1)}_0\|_F/\sqrt n\le C\), and
\(\|W_0\|_{\rm op}\le K_0\). The fixed vectors multiplying the gate
differences have bounded coordinates, and \(\|V\|_2/\sqrt n\le C\).
Thus \(J_n\) has a common Lipschitz constant. A fixed radius \(r_*>0\)
therefore gives a deterministic cap

\[
 \mathcal C=\{u\in S^{d-1}:\|u-v\|_2\le r_*\},
 \qquad J_n(u)\ge j_*/2\quad(u\in\mathcal C).          \tag{20}
\]

The expansions above are uniform over all unit query directions. Indeed,
the trained first-matrix increment has every row proportional to \(v^\top\),
so a query first-layer increment is the training increment multiplied by
\(v^\top u\). Its absolute multiplier is at most one; the same observation
applies to the first-layer discrepancy. Forward subtraction and the same
Taylor remainder as in (16) consequently give

\[
 \widehat f(s,u)-f_D(s,u)
  =-s^5J_n(u)+O(s^5\alpha(s)),                        \tag{21}
\]

uniformly on the sphere. Formula (18) includes both the hidden-matrix and
readout effects. Omitting the readout response would miss its factor \(1/5\).
In deriving (21), the dense readout is
\(2s h^{(2)}_0+O_{\rm RMS}(s^3)\), and replacing evolving query features
by initialized ones contributes only \(O(s^7)\), included because
\(\alpha(s)\ge s^2\).

### 6.3 Returning to one physical time

Let \(t_q(s)\) be the physical time at which the closure reaches activity
\(s\), and let
\(\sigma(s)=\tau_D(t_q(s))-1\) be the dense activity at that same time.
The actual clock equations imply

\[
 \sigma'(s)=\frac{y-f_D(\sigma(s),v)}{y-\widehat f(s,v)},
 \qquad \sigma(0)=0.                                  \tag{22}
\]

Both residuals stay at least \(y/2\) on the small interval.
The dense clock derivative \(\partial_s f_D(s,u)\) is bounded by a
common \(C\) for unit queries, using (2), the local operator bound, and
\(\|w_D\|_\infty\le2s\). Subtracting one from (22), using (21) at
\(v\), and applying the scalar integrating factor give

\[
 |\sigma(s)-s|\le C_y s^6.                            \tag{23}
\]

For this argument use the local estimates on twice the final interval,
decreasing \(\eta\) accordingly, and stop provisionally at
\(\sigma=2s_*\). Equation (23) excludes that stop. The
equal-physical-time discrepancy is therefore

\[
 \widehat f(t_q(s),u)-f_D(t_q(s),u)
   =-s^5J_n(u)+O(s^5\alpha(s)+C_y s^6).               \tag{24}
\]

Choose \(\eta\) once more so that the remainder at \(s=s_*\) is at
most \(j_*s_*^5/4\). Since \(q^2s_*\le\eta\) and
\(\sqrt n\,s_*^2\le\eta^2\), this choice is independent of width and
order. Equations (20) and (24) give, at one shared physical time,

\[
 |\widehat f(t_q(s_*),u)-f_D(t_q(s_*),u)|
       \ge \frac{j_*}{4}s_*^5\qquad(u\in\mathcal C).
\]

The supremum in the whole-input metric includes this time. Integrating over
the fixed cap proves (12), with the factor \(\sqrt{\mu(\mathcal C)}\).
Here \(\mu(\mathcal C)\) denotes the mass of inputs whose normalized
direction lies in the cap. For uniform sphere measure this factor is
positive; for \(d=1\) the sphere is the two-point set and the conclusion
is immediate.

This calculation verifies an actual signed prediction effect and its
same-time interpretation. Its conservative width-dependent early interval
makes it much too weak for the requested lower-bound alternative. It should
not be presented as a proof that order \(n^{1/4}\), or any growing order,
is necessary at the root-width accuracy scale.
