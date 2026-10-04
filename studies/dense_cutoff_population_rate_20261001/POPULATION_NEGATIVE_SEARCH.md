# Negative search for a polynomially slower dense population rate

2026-10-03. Scoped, independent theoretical attempt within this study.
**Outcome: no canonical counterexample obtained.** The calculations below
eliminate several proposed mechanisms in their stated scopes and identify a
real low-regularity obstruction to some proof arguments. They do not prove
the dense-to-population rate. They have been self-audited but have not
received an independent complete check or promotion review.

## 1. Contract and permitted evidence

The target is the actual dense network
\[
 z^{(1)}(x)=W^{(1)}x/\sqrt d,\quad
 z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),\quad
 h^{(\ell)}(x)=\phi_\ell(z^{(\ell)}(x)),\quad
 f_n(t,x)=w(t)^\top h^{(L)}(t,x)/n.
\]
There are fixed \(L\ge2\) hidden layers and fixed \(m,d\). First weights
have independent \(N(0,1)\) entries, hidden weights independent
\(N(0,1/n)\) entries, and \(w(0)=0\). All blocks are independent.
For fixed training data \((x_a,y_a)_{a=1}^m\), the loss is
\(\mathcal L_n=m^{-1}\sum_a r_a^2\), where \(r_a=f_n(x_a)-y_a\).
The backward fields and physical flow are
\[
 \delta_a^{(L)}=\phi_L'(z_a^{(L)})\odot w,\qquad
 \delta_a^{(\ell)}
 =\phi_\ell'(z_a^{(\ell)})\odot W^{(\ell+1)\top}\delta_a^{(\ell+1)},
\]
\[
 \dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}x_a^\top/\sqrt d,\quad
 \dot W^{(\ell)}=-\frac2{nm}\sum_a
 r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},\quad
 \dot w=-\frac2m\sum_a r_a h_a^{(L)}.
 \tag{1}
\]
The inputs lie on \(\|x_a\|=\sqrt d\), with the compatible duplicate
and parity quotients of DEPTH_EXTENSION_RESULT.md. On that weighted
quotient the limiting initialized last-feature Gram has a fixed
positive gap. Each activation is fixed, belongs to \(C^3(\mathbb R)\),
and has bounded first three derivatives. Its values may grow linearly.
The label RMS \(Y\) is fixed and sufficiently small as in that result.
Neither data, labels, activations, depth, nor query law varies with width.

The reference \(f_\infty\) is the deterministic dense population
predictor identified by the manuscript's Gaussian operator construction,
with the same physical dynamics. For a fixed probability law \(\mu\)
with finite second moment, the target norm is
\[
 \mathcal E_\mu(f,g)
 =\left(\int\sup_{t\in[0,\infty]}|f(t,x)-g(t,x)|^2\,d\mu(x)\right)^{1/2}.
 \tag{2}
\]
A successful negative construction would give some fixed
\(0<\alpha<1/2\), constants \(c,p>0\), and widths tending to infinity
such that
\[
 \Pr\{\mathcal E_\mu(f_n,f_\infty)
              \ge c n^{-1/2+\alpha}\}\ge p.
 \tag{3}
\]
A logarithmic loss alone would not establish this particular falsifier.
Changing to a different smooth least-squares system would not establish
it either.

Scientific reads were restricted to this study's complete
GENERAL_SELF_AVERAGING.md, DEPTH_EXTENSION_RESULT.md and
LARGE_LABEL_ASSESSMENT.md; the dense model/population specification in
paper/main.tex; complete paper/results.tex and paper/proof_alltime.tex;
and docs/index.qmd and docs/notation.qmd. MATCHED_LOSS_ASSESSMENT.md did
not exist when checked. Required research and mathematical-notation
skills and RESEARCH_WORKFLOW.md were read. No other new-route note,
other study, archived book, external scientific source or numerical
experiment was used. References inside the three study inputs were not
followed beyond this assignment's input scope.

## 2. A slower polynomial rate would have to be a center bias

GENERAL_SELF_AVERAGING.md supplies deterministic finite-width centers
\(c_n\) and fixed-confidence bounds
\[
 \mathcal E_\mu(f_n,c_n)
 =O_{\Pr}\!\left(n^{-1/2}e^{K\sqrt{\log(e+n)}}\right).
 \tag{4}
\]
For every fixed \(\alpha>0\), the scale on the right is
\(o(n^{-1/2+\alpha})\). If (3) held, the triangle inequality would give,
along its sequence and for all sufficiently large widths,
\[
 \mathcal E_\mu(c_n,f_\infty)\ge(c/2)n^{-1/2+\alpha}.
 \tag{5}
\]
Indeed choose the confidence failure in (4) below \(p/2\). Its good
event intersects the event in (3); on that intersection the triangle
inequality yields (5), whose left side is deterministic.

Conversely, (5) together with (4) gives a prediction lower bound of
the same order with arbitrarily high fixed confidence, after decreasing
the constant. Random branch selection with two prediction branches of
nonvanishing separation and nonvanishing probabilities is incompatible
with (4). This does not rule out a slowly converging common center.

## 3. Singular initialized covariances do not create a square-root loss

### 3.1 Smooth Gaussian covariance maps are Lipschitz at the boundary

For a fixed finite input list, define
\[
 \mathcal T_\ell(Q)_{ab}
   =\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
 \qquad Z\sim N(0,Q),\qquad Q\succeq0.
 \tag{6}
\]
If \(\|Q\|_{\rm op},\|\widetilde Q\|_{\rm op}\le M\), then
\[
 \|\mathcal T_\ell(Q)-\mathcal T_\ell(\widetilde Q)\|_F
       \le C_M\|Q-\widetilde Q\|_F.
 \tag{7}
\]
The constant depends on the list length and activation bounds, but not
on the smallest eigenvalue.

Put \(F(z)=\phi_\ell(z_a)\phi_\ell(z_b)\) and
\(Q_s=(1-s)Q+s\widetilde Q\). Linear growth and the bounded first two
derivatives give
\[
 |\partial_{ij}F(z)|\le C(1+|z_a|+|z_b|).
 \tag{8}
\]
First replace every \(Q_s\) by \(Q_s+\epsilon I\). Differentiating
its Gaussian density gives
\(\partial_s p_s=\frac12\sum_{ij}
(\widetilde Q-Q)_{ij}\partial_{ij}p_s\).
Two integrations by parts, justified by (8) and Gaussian tails, yield
\[
 \frac{d}{ds}\mathbb E F(N(0,Q_s+\epsilon I))
  =\frac12\sum_{ij}(\widetilde Q-Q)_{ij}
                  \mathbb E[\partial_{ij}F(N(0,Q_s+\epsilon I))].
 \tag{9}
\]
The expectation in (8) is bounded uniformly in \(s\) and
\(0<\epsilon\le1\). Integrate (9), then use square-root coupling and
dominated convergence to send \(\epsilon\downarrow0\). This proves
(7), including singular endpoints. Estimating only
\(\|Q^{1/2}-\widetilde Q^{1/2}\|\) misses this weak-observable
cancellation.

Write \(Q_n^{(\ell)}=H_\ell(0)^\top H_\ell(0)/n\). The first layer
is an average of independent finite-fourth-moment vectors, so
\[
 Q_n^{(1)}-Q^{(1)}=O_{\Pr}(n^{-1/2}).
 \tag{10}
\]
Conditionally on preceding layers, the next rows are independent
Gaussians with covariance \(Q_n^{(\ell-1)}\). On
\(\|Q_n^{(\ell-1)}\|_{\rm op}\le M\), activation products have
variance at most \(C_M\), by linear growth and Gaussian fourth moments.
Conditional Chebyshev therefore gives
\[
 Q_n^{(\ell)}-\mathcal T_\ell(Q_n^{(\ell-1)})
                                   =O_{\Pr}(n^{-1/2}).
 \tag{11}
\]
The complementary covariance event can be made arbitrarily unlikely
by fixed \(M\), since the preceding induction supplies boundedness
in probability. Combining (7), (10) and (11) proves the root-width
initialized covariance rate at every fixed depth, without
nonsingularity.

Append any fixed passive query \(x\) to this list. At zero readout
all hidden velocities vanish, so (1) gives the exact identity
\[
 \partial_t f_n(0,x)
   =\frac2m\sum_a y_a
       \frac{h^{(L)}(0,x)^\top h_a^{(L)}(0)}n.
 \tag{12}
\]
This velocity differs from its population counterpart by
\(O_{\Pr}(n^{-1/2})\), including singular augmented covariances.
The assertion is at a fixed query; it is not uniform over unbounded
queries and is not a trained population rate.

### 3.2 Population null relations hold for every initialized sample

At each initialized layer,
\[
 \ker Q^{(\ell)}\subseteq\ker Q_n^{(\ell)}
                       \quad\text{almost surely}.
 \tag{13}
\]
For the first layer, \(c^\top Q^{(1)}c=0\) means
\(\sum_a c_a\phi_1(G^\top x_a/\sqrt d)=0\) almost surely.
Continuity and full Gaussian support make this true at every root,
so each empirical row satisfies it. A basis of the deterministic
kernel establishes the simultaneous kernel inclusion.

For the induction, (13) at the preceding layer implies
\({\rm ran}\,Q_n^{(\ell-1)}\subseteq{\rm ran}\,Q^{(\ell-1)}\).
The Gaussian with covariance \(Q^{(\ell-1)}\) has full support on
that latter subspace. If \(c\in\ker Q^{(\ell)}\), continuity makes
\(\sum_a c_a\phi_\ell(z_a)=0\) throughout the subspace.
Every conditional finite preactivation row belongs to it, proving
(13) again.

A zero population eigenvalue therefore cannot be replaced by a
spurious positive \(n^{-1/2}\) empirical eigenvalue at initialization
and square-rooted into an \(n^{-1/4}\) innovation. This argument does
not assert rank preservation for adaptive history Grams after
training, which contain width-dependent learned contractions.

## 4. Weak training directions and newly appearing history directions

The compatible quotient removes exact duplicate and parity relations
before the positive-gap assumption is used. For shared odd activations
and no biases, \(f_n(-x)=-f_n(x)\) for every weight state; even
first-layer activations give \(f_n(-x)=f_n(x)\). Compatible labels
obey the same relation, so training does not randomly excite these
null directions.

On the quotient the initialized limiting gap is fixed and positive.
The small-label tube supplies \(\Gamma_n(t)\succeq\lambda I\) with
fixed \(\lambda>0\), after the fixed sample-weight conjugation. Hence
\[
 \dot r_n=-2\Gamma_n r_n,\qquad
 \rho_n(t)\le Y e^{-2\lambda t}.
 \tag{14}
\]
A very small but fixed activation component or data separation can
make \(\lambda\) and the allowed label threshold small. It changes
constants and the onset of asymptotics, not a power of width. Taking
that component or separation to zero with width violates the contract.

There is a concrete small-time check of a new history direction.
Define \(a_0=\dot w(0)=(2/m)\sum_b y_b h_b^{(L)}(0)\) and
\[
 D_a^{(L)}=\phi_L'(z_a^{(L)}(0))\odot a_0,\qquad
 D_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)}(0))\odot
                                  W_0^{(\ell+1)\top}D_a^{(\ell+1)}.
 \tag{15}
\]
These are \(\partial_t\delta_a^{(\ell)}(0)\). Since
\(\delta(0)=0\), differentiating (1) gives
\[
 \ddot W^{(1)}(0)=\frac2m\sum_a y_aD_a^{(1)}x_a^\top/\sqrt d,\qquad
 \ddot W^{(\ell)}(0)=\frac2{nm}\sum_a
                    y_aD_a^{(\ell)}h_a^{(\ell-1)}(0)^\top.
 \tag{16}
\]
All hidden first derivatives vanish. Their second derivatives obey
\[
 \ddot z^{(1)}=\ddot W^{(1)}x/\sqrt d,\quad
 \ddot z^{(\ell)}=\ddot W^{(\ell)}h^{(\ell-1)}(0)
                         +W_0^{(\ell)}\ddot h^{(\ell-1)},\quad
 \ddot h^{(\ell)}=\phi_\ell'(z^{(\ell)}(0))\odot\ddot z^{(\ell)}.
 \tag{17}
\]
Let \(P_{0,n}\) project onto a span of initialized feature vectors
at this layer, including the feature being followed. For each fixed
width, finite-dimensional smoothness yields
\[
 (I-P_{0,n})h^{(\ell)}(t)
  =\tfrac12t^2(I-P_{0,n})\ddot h^{(\ell)}(0)+O_n(t^3).
 \tag{18}
\]
Its squared RMS begins at order \(t^4\). The finite innovation
shares the vanishing time factor; independent time-independent
covariance noise is not its small-time expansion. The remainder is
only asserted at fixed width. This check does not quantitatively
compare all adaptive reused-matrix histories.

## 5. A C3 regularity trap, but not a prediction counterexample

Fix \(0<\beta<1\), and take smooth compactly supported \(\chi\)
equal to one on \([-1,1]\). The activation
\[
 \phi_\beta(s)=\chi(s)(s_+)^{3+\beta},\qquad s_+=\max(s,0),
 \tag{19}
\]
is \(C^3\) with bounded first three derivatives. Its third derivative
is not Lipschitz at zero. It is nonaffine and neither odd nor even,
so it is admissible under the sphere-data initialization criteria.

For \(Z\sim N(0,1)\) and \(v\downarrow0\), direct rescaling gives
\[
 \mathbb E[\phi_\beta^{(j)}(\sqrt v Z)]
   =c_jv^{(3+\beta-j)/2}+O(e^{-c/v}),\qquad 0\le j\le3,
 \tag{20}
\]
where
\[
 c_j=\left(\prod_{r=0}^{j-1}(3+\beta-r)\right)
                            \mathbb E[(Z_+)^{3+\beta-j}]>0.
\]
The empty product is one. Terms involving derivatives of \(\chi\),
and the omitted pure-power tail, have \(|\sqrt v Z|\ge1\).
Gaussian tail integration bounds them by \(Ce^{-c/v}\) after reducing
\(c>0\).

For the actual forward and gate functions, \(j=0,1\), the powers
exceed one: these averages do not magnify small covariance errors.
But \(j=2,3\) have powers \((1+\beta)/2\) and \(\beta/2\).
For example the former at \(v=n^{-1/2}\) has size
\(n^{-(1+\beta)/4}\), slower than root width.

This disproves a general covariance-Lipschitz assertion for these
derivative observables. It matters to proof routes involving
\(\phi''\) or \(\phi'''\) in response coefficients. It is not a
network prediction lower bound. Such a lower bound must additionally
exhibit the degenerating covariance in the actual trained law, prove
the size of its finite perturbation, and produce an uncancelled
prediction term. None of these steps follows from (20).

The simplest attempted embedding at a zero-variance initialized
training marginal fails. A sphere input has first-layer variance one.
At a later layer, zero preactivation variance means the previous
activation is zero almost surely. If its preactivation is a
nondegenerate Gaussian, continuity makes the activation identically
zero on the real line; its derivative vanishes too. It is a dead
branch, not a small innovation. For the nonconstant activations and
sphere inputs under consideration, all initialized marginal variances
stay positive. Joint covariances can still be singular; Section 3
treats them without positive joint eigenvalues.

At a passive zero input, if every activation vanishes at zero, all
features and predictions vanish exactly at every width and time.
This does not create a small finite Gaussian variance either. Other
trained singularities have not been ruled out.

## 6. Heavy queries and rare coordinates

The finite and population small-label tubes imply, on the finite good
event,
\[
 |f_n(t,x)|+|f_\infty(t,x)|\le CYB(x),\qquad
 B(x)=1+\|x\|/\sqrt d.
 \tag{21}
\]
Finite second moment makes the envelope square-integrable. But (21)
and convergence on every bounded query domain alone have no width
rate. For example choose \(\|x_k\|/\sqrt d=R_k\to\infty\), with
masses proportional to \(1/(k^2R_k^2)\), and put the remaining
probability at a fixed point. Then \(\mu\) has finite second moment.
Abstract discrepancies of size \(R_k\) at \(x_k\), vanishing at every
earlier fixed query, have norm of order \(1/k\); the corresponding
widths may grow arbitrarily fast.

These abstract discrepancies are not neural predictors. They show
why an envelope-only proof cannot settle the rate. Producing them
from the same trained weights is the missing construction.

Two more concrete checks failed. First, for same-width physical
states in the tube,
\[
 |f_n(\theta,x)-f_n(\widetilde\theta,x)|
                     \le CB(x)d_n(\theta,\widetilde\theta),
 \tag{22}
\]
where \(d_n\) is the normalized parameter distance in
GENERAL_SELF_AVERAGING.md. The first-layer feature RMS difference
is at most
\(\|\Delta W^{(1)}\|_F\|x\|/(\sqrt n\sqrt d)\).
At each later layer, subtraction gives a bounded-operator term from
the previous difference and
\(\|\Delta W^{(\ell)}\|_F
\|\widetilde h^{(\ell-1)}(x)\|_2/\sqrt n\).
The latter feature RMS is at most \(CB(x)\). Expanding the readout
pairing proves (22). A root-width state perturbation cannot be given
a worse exponent solely by choosing a finite-second-moment query law.
This is not a coupling of different widths or of a finite state with
the population operator.

Second, a missed rare initialized neuron does not give the target
bias. For a scalar Gaussian root \(G\), linear growth gives
\(|\phi(G)|^2\le C(1+G^2)\). If \(\Pr(|G|>R)\) is of order \(1/n\),
Gaussian density integration gives
\[
 R^2=O(\log n),\qquad
 \mathbb E[(1+G^2)\mathbf1_{\{|G|>R\}}]=O((\log n)/n).
 \tag{23}
\]
Failing to sample this tail therefore contributes at most this order
to a quadratic initialized feature mean, below root width. The
calculation does not control collective adaptive reuse of the matrices.

## 7. The endpoint does not supply critical slowing in this regime

The small-label finite and population speed bounds give
\[
 |\partial_t f_n(t,x)|+|\partial_t f_\infty(t,x)|
                         \le CYB(x)e^{-\kappa t}
 \tag{24}
\]
with fixed \(\kappa>0\). Integration from \(T\) to a later time and
the triangle inequality yield
\[
 \mathcal E_\mu(f_n,f_\infty)
 \le\left(\int\sup_{0\le t\le T}
       |f_n(t,x)-f_\infty(t,x)|^2\,d\mu(x)\right)^{1/2}
                             +C_\mu Y e^{-\kappa T}.
 \tag{25}
\]
For an obstruction at \(n^{-1/2+\alpha}\), take any \(\eta>0\) and
\[
 T_n=(1/2-\alpha+\eta)\log n/\kappa.
 \tag{26}
\]
The tail in (25) is smaller than that scale. An obstruction must
already appear by logarithmic physical times; a delayed loss of the
training gap cannot create it.

This is not a rate theorem: a compact-time estimate with uncontrolled
dependence on \(T\) cannot be evaluated at \(T_n\). It does show why
the critical scalar example in LARGE_LABEL_ASSESSMENT.md, whose
relaxation gap vanishes at a critical label, cannot be imported into
the present regime. A common bias in passive endpoint selection is
still possible until the population comparison controls it.

## 8. Actual implications and remaining obligation

| Proposed mechanism | Result | Boundary |
|---|---|---|
| Singular initialized covariance creates a square-root loss | Excluded for initialized Grams and initial prediction velocity by (7)--(13) | Adaptive history covariances were not quantitatively compared |
| Width-dependent weak training direction | Excluded by the fixed quotient gap and small-label tube | Constants vary across different fixed datasets |
| Random macroscopic endpoint branches | Incompatible with supplied near-root concentration | A common finite-width center can still be biased |
| C3 makes every response average covariance-Lipschitz | False for the derivative averages in (20) | No canonical prediction lower bound follows |
| Heavy query tails alone | Envelope-only arguments fail; (22) prevents amplification of a controlled state error | No population coupling was proved |
| Rare unsampled Gaussian feature | Direct quadratic initialization bias is only \(O(\log n/n)\) | Collective adaptive bias is unestimated |
| Critical slowing at the fitted endpoint | Prevented by the supplied uniform gap and speed estimates | Uniform bias over finite training activity remains open |

The unresolved task is specific: estimate, or disprove a rate for,
the deterministic prediction center produced by repeated forward and
adjoint Gaussian-matrix reuse over the finite total training activity.
Neither the initialized singularity nor the scalar endpoint examples
above achieve this. No slower canonical dense population rate has
been established here, and its impossibility has not been established.

For a positive route, inspect every covariance-continuity step for
response coefficients: it must use only forward/gate quantities,
establish adequate nondegeneracy, or prove the required cancellation.
Formula (20) prevents invoking C3 alone for an arbitrary derivative
observable at vanishing variance.

## 9. Source versions and check record

The assignment replaced routine study-author startup. This agent owns
only this report; the coordinator owns shared study records. Git HEAD
before writing was 4dfa5c1ef2c5b920eda2bbc84316b189b97da92e.
Concurrent modified-path metadata was observed and left untouched.
No Git staging or commit was performed.

| Read input | SHA-256 |
|---|---|
| GENERAL_SELF_AVERAGING.md | bfbc14cbb3cccf902420db74ca6e3627e341f27a84b52a229362848b376a56d5 |
| DEPTH_EXTENSION_RESULT.md | 6867c597f5efc368ba54b2ce9d810c653a54a2788ece2e748a8b8d98c487ce11 |
| LARGE_LABEL_ASSESSMENT.md | 736ad09b8081657373ba98687cc32f52bfdc2db33d46c72c69e5ad85ce977208 |
| paper/main.tex, scoped model/population passage | 60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95 |
| paper/results.tex | 6e76e83aae3a3e36f588bdf37dddf72ac811bf2644de664fb0b4b83f117704a1 |
| paper/proof_alltime.tex | f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d |
| docs/index.qmd | f7a21b794e21f145ebad87fb1d7bde05f5f55e5877c92440109c1b22232b06de |
| docs/notation.qmd | 78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023 |

Checks were analytic substitution into the exact dense equations,
Gaussian-density integration by parts, support/null relations, the
zero-readout time expansion, Gaussian power rescaling in (20), and
the probability intersection proving (5). No computer experiment,
GPU probe, numerical trajectory or external theorem was used.
The internally checked concentration and tube statements were
accepted as supplied inputs, not reconstructed from their full
dependency files in this scoped task.
