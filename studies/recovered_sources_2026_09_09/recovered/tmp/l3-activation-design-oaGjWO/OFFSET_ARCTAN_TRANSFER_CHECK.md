# Conditional transfer check for the offset arctangent

This is the authorized destination-only adaptation check, not a review or
certification of a complete new proof. The entire prescribed skill, design
contract, and 2,321-line assembled source proof were read. No response
bootstrap, numerical experiment, or feature/nonlinearity certificate is
supplied here. No source proof or master ledger was changed.

Source: [L3_LOCAL_COMPLETE_PROOF.md](/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md).
Its SHA256 agrees with the contract:
`f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4`.
Line references below refer to that file. Contract:
[ACTIVATION_DESIGN_CONTRACT.md](/tmp/l3-activation-design-oaGjWO/ACTIVATION_DESIGN_CONTRACT.md).

The common-space construction, fixed-clipping construction, asymmetric
cutoff comparison, reached-state uniqueness, and raw-GD comparison mechanism
transfer with the replacements below. The old small physical-time guard
does **not** transfer to arbitrary physical horizons just by replacing the
activation. Sections 7–8 supply a positive-floor clock argument and a
stopped exact-GD argument that replace that guard. Every assertion here
about an uncut population limit remains conditional on the following
precise, still-to-be-discharged input.

## 1. Exact conditional input and conventions

Use, in every hidden layer,
\[
 \phi(z)=1+\lambda\arctan z,\quad \lambda=1/10,
 \qquad c=5/6,\quad b=7/6,\quad \mu=1/5,\quad S=3/2.
\]
Then
\[
 c\le\phi\le b,\qquad
 d(z):=\phi'(z)=\frac{\lambda}{1+z^2},\quad
 0<d\le\lambda,\quad |d'|\le\mu.
\]
The non-strict bounds suffice throughout. Retain every raw parameter,
normalization, independent initialization block, residual placement, and
physical step size in the contract. In particular, the rescaled readout
entries have variance \(n^{-2}\), not standard deviation \(n^{-2}\).
Use \(C=W^{(4)}\), and retain the source's notation for \(q^{(j)}\),
\(\delta^{(j)}\), adjoints, rank-one actions, and state distance.

**Required tail input (H).** For every integer clipping level \(R\ge1\)
and every fixed finite transformed Euler mesh with positive equal steps
and total feature time at most \(S\), the offset-activation scalar
representation of the actual empirical-feedback Gaussian-matrix program
satisfies
\[
 \sup_{R,\Delta,M,k:\,k\le M,\,M\Delta\le S}
 E\exp\!\left((q^{(2)}_{R,k})^2/K^2\right)\le2
 \tag{H}
\]
for one finite deterministic \(K\). A Gaussian-plus-uniformly-bounded
shift estimate implies this after enlarging \(K\). Here the initial
population readout is zero. The scalar derivatives must use the source's
formal-expression, frozen-coefficient convention, including singular
covariances and all current-step returns through the other matrix.

Update from main: the candidate
[OFFSET_ARCTAN_RESPONSE_BOOTSTRAP.md](/tmp/l3-activation-design-oaGjWO/OFFSET_ARCTAN_RESPONSE_BOOTSTRAP.md)
now states \(U<0.9\), \(V\le3067/3200<1\), and
\(q^{(2)}=\zeta+\beta\), with centered Gaussian \(\zeta\) of variance
at most \((7/40)^2\) and \(|\beta|\le7/6\), uniformly over the
required meshes and clipping levels. Its status is candidate, under a
separate independent audit; this note does not audit its response proof.
If accepted with the required program identification, these bounds imply
(H), for example with \(K=4\):
\[
 E e^{q^2/16}
 \le e^{49/288}E e^{\zeta^2/8}
 \le e^{49/288}(1-49/6400)^{-1/2}<2.
\]
The last inequality follows from \(49/288<1/5\),
\(e^{1/5}\le(1-1/5)^{-1}=5/4\), and
\((1-49/6400)^{-1/2}<4/3\). The Gaussian expectation is its elementary
quadratic exponential integral. No independence of \(\zeta\) and
\(\beta\) is used. This checks the candidate's sufficiency for the
bridge, not the candidate's validity.

A tail bound for a different scalar recursion, fixed \(R\) only, or a
constant growing with mesh length is insufficient. No Gaussian tail for
\(q^{(1)}\), no finite-width exponential moment, and no tail premise for
an arbitrary competing uncut solution are required by the bridge.
Uniformity of the marginal estimate in time suffices; a Gaussian tail for
the time supremum is not needed. This note does not prove (H).
In the clock discussion the positive quantity is the deficit \(1-f\);
the source's signed residual remains \(r=f-1\).

## 2. Activation-specific dependencies: exact replacements

| Source location | Dependency and required adaptation |
| --- | --- |
| Lines 9–73, 217, 462, 734, 1068 | Replace the activation, derivative bounds, and natural coordinate everywhere. The old explicit response constants and \(S_0\) are not a certificate for \([0,3/2]\). |
| Lines 217–295, 297–402 | Source covariances use full second moments \(E[H_kH_s]\), not centered activation covariances. Gaussian innovations are centered because the matrix entries are centered; \(EH=0\) is not a premise. |
| Lines 417–447, 617–669, 1159–1255 | Bounded activation, bounded first/second derivatives, bounded reference readout, and Lipschitz \(F^{-1},\phi\circ F^{-1}\) supply all product estimates. No activation oddness or \(\phi(0)=0\) is used. |
| Lines 470–547 | Constants are already included in every population's probe algebra. Keep them: the offset changes forward matrix queries and cannot be discarded as a centered-activation convention. Reconstruct/identify the new coordinate laws on common spaces; do not reuse the old trained trajectory or old covariance values. |
| Lines 558–566 | Oddness is imposed on the auxiliary clipping map. These same maps remain admissible. The comparison needs their identity region, contraction property, and amplitude bound, not oddness of the activation or symmetry of a trained law. |
| Lines 803–804 and 1970–2033 | Vanishing initial backward fields and initial hidden velocity come from \(C_0=0\). They do not come from \(\phi(0)=0\). The new hidden activations are already nonzero at zero preactivation. |
| Lines 1503–1614 | The exact cubic identity survives, but its quadratic and cubic remainder coefficients change by a factor of 10 when written in terms of the new \(d\). Section 8 gives the identity and summation estimate. |
| Lines 1509–1543, 1618–1693 | The old proof requires \(\bar S\le1/(4a^2)\), \(T_0=\bar S/4\), and small-predictor guards. Those do not establish every finite physical horizon. Replace them by Sections 7–8, not by merely enlarging \(T_0\). |
| Lines 2130–2167 | The claim \(z\phi(z)d(z)>0\) for all \(z\ne0\) is false for the offset activation: it is negative for \(z<0\). The needed initial expectation has the replacement below. This is the explicit sign-sensitive feature argument in the source. |
| Lines 2180–2189 | Coercivity of the forward velocity operators comes from \(m_1I,m_2I\) and adjunction, not activation oddness. Their structural inequalities survive. Positivity of \(d\) gives injectivity of a gate, not a uniformly bounded inverse. |
| Lines 2299–2320 | Initial nonaffineness and its continuity extension concern a small initial interval only. They do not certify noncollapse at every finite physical time. That remains with the separate feature/nonlinearity work. |

There is no further trained-state sign-symmetry argument in the supplied
assembled proof. In particular, its conditioning, asymmetric comparison,
gradient calculation, and clock construction do not assume symmetry of
the trained preactivations. The new activation satisfies
\(\phi(-z)=2-\phi(z)\), not \(\phi(-z)=-\phi(z)\).
Its derivative is even and its second derivative odd. These facts do not
make a trained field centered. They may be used for the explicitly
symmetric *initial Gaussian* expectations below.

The correct natural coordinate is
\[
 F(z)=\lambda^{-1}(z+z^3/3)=10(z+z^3/3),\qquad
 F'(z)=1/d(z).
\]
It is a smooth increasing bijection of \(\mathbb R\), and
\[
 (F^{-1})'(F(z))=d(z),\qquad
 \operatorname{Lip}(F^{-1})\le\lambda,\qquad
 (\phi\circ F^{-1})'(F(z))=d(z)^2\le\lambda^2.
\]
Thus \(X'=q^{(1)}\) is exactly equivalent to the continuous raw
equation \((Z^{(1)})'=d(Z^{(1)})q^{(1)}\). The factor 10 is
necessary for that statement. Although \(F\) is still odd, only its
invertibility, derivative identities, and root moments are needed here.
It is not globally Lipschitz and must remain a root coordinate in the
finite-program construction. For \(G\sim N(0,1)\),
\(E F(G)^2=100(1+2+5/3)=1400/3<\infty\).

At initialization set \(m_0=1\). The Gaussian forward laws become
\[
 Z^{(\ell)}_0\sim N(0,m_{\ell-1}),\qquad
 m_\ell=1+\lambda^2 E\arctan(\sqrt{m_{\ell-1}}G)^2,
 \quad \ell=1,2,3.
\]
Here \(EH^{(\ell)}_0=1\), and
\(m_\ell=E(H^{(\ell)}_0)^2\), not
\(\operatorname{Var}(H^{(\ell)}_0)\). Conditional on an input
\(h\), an independent centered Gaussian matrix sends it to centered
Gaussians of variance \(\|h\|_n^2\); this verifies the forward law
despite the nonzero activation mean. Source covariances and learned
rank-one contractions must retain the constant contribution.

For the one sign-sensitive initial moment, if \(Z\) is any centered
nondegenerate Gaussian, symmetry gives
\[
 E[Z\phi(Z)d(Z)]
 =\lambda E\frac{Z}{1+Z^2}
  +\lambda^2 E\frac{Z\arctan Z}{1+Z^2}
 =\lambda^2 E\frac{Z\arctan Z}{1+Z^2}>0.
\]
This replaces the source's pointwise sign argument for its initial
\(c_3,c_2\) coefficients. It is an initial-law replacement only;
no such cancellation is asserted at positive time. The transpose
conditioning formulas still retain the full response term and the
innovation variance \(E\beta_3^2\), without subtracting a response
variance. The subsequent nontriviality argument is outside this check.

## 3. Common population spaces and fixed finite programs

The mechanism at lines 297–451 and 470–547 can be rerun with the new
coordinate maps. Its hypotheses are verified as follows.

1. Keep independent Gaussian matrices of entry variance \(1/n\), the
   same iid first-layer roots, and root tuple \((G,F(G))\). The tuple
   has finite second moments. Include constants, both matrix directions,
   rational linear combinations, the new activation/inverse coordinate,
   clipping maps, and the bounded Lipschitz dense probe family.
2. For each fixed clipped finite program, \(|C_k|\le bM\Delta\),
   \(|\delta^{(3)}_k|\le\lambda bM\Delta\), and
   \(|\delta^{(2)}_k|\le2\lambda R\). The top product can be extended
   outside its attained readout range to a globally Lipschitz smooth map;
   the middle product already has bounded first derivatives. This is
   exactly the coordinate regularity needed for the source conditioning
   and finite oracle/empirical-feedback comparison.
3. Conditional Gaussian projection and Gaussian integration by parts
   use second-moment Gram matrices. They impose no mean-zero condition
   on the query vectors. Retain the same causal order and both reused
   transposes. In particular the current terms remain
   \[
   b^{(3)}_{kk}=E[C_k\phi''(Z^{(3)}_k)],
   \]
   \[
   b^{(2)}_{kk}=E[\phi''(Z^{(2)}_k)\tau_R(q^{(2)}_k)]
    +b^{(3)}_{kk}E[d(Z^{(2)}_k)^2\tau_R'(q^{(2)}_k)].
   \]
   No term here is discarded on a symmetry argument.
4. The source's finite-query noise regularization, covariance-square-root
   continuity, and removal of query noise use the verified fixed-program
   Lipschitz bounds. Singular covariances remain allowed. No inverse
   Gram convergence at a rank drop is asserted.
5. Joint consistency over finite unions gives the three generated
   probability spaces. The same Gaussian matrix norm estimate gives
   initial operator norm at most 10 in the population construction.
   Passing finite norm inequalities to countably many rational probes
   gives well-defined linear actions, and density extends them to the
   generated \(L^2\) spaces. Passing finite transpose pairings identifies
   the reverse actions as adjoints. All these steps use the new laws.

This establishes which fixed-program mechanism identifies the scalar
system that (H) must bound. It does not import a response bound from the
old activation, nor identify arbitrary independent scalar processes with
the trained common-space state.

## 4. Fixed-clipping construction with explicit uniform primal bounds

The state remains \((X^{(1)},W^{(2)},W^{(3)},C)\), with the source's
sum of two \(L^2\) distances and two operator distances. In feature
time the four equations remain
\[
 X'= (W^{(2)})^*\delta_R^{(2)},\quad
 (W^{(2)})'=\delta_R^{(2)}\otimes H^{(1)},\quad
 (W^{(3)})'=\delta^{(3)}\otimes H^{(2)},\quad C'=H^{(3)}.
\]
They are auxiliary clipped equations, with no assumed gradient identity.

For initial matrix norm bound \(M\) and readout \(L^2\) norm
\(\varepsilon\), define deterministic bounds
\[
 B_4=\varepsilon+bS,\qquad
 B_3=M+\lambda b B_4S,\qquad
 B_2=M+\lambda^2 b B_3B_4S.
\]
Contraction of clipping gives successively
\[
 \|C\|_2\le B_4,\quad
 \|\delta^{(3)}\|_2\le\lambda B_4,\quad
 \|W^{(3)}\|_{\rm op}\le B_3,
\]
\[
 \|\delta_R^{(2)}\|_2\le\lambda^2B_3B_4,\quad
 \|W^{(2)}\|_{\rm op}\le B_2,\quad
 \|q_R^{(1)}\|_2\le\lambda^2B_2B_3B_4.
\]
These follow by integrating or summing the rank-one norm inequality
\(\|u\otimes v\|=\|u\|_2\|v\|_2\). They hold for continuous
flows and every positive-step Euler prefix of total length at most
\(S\), uniformly in width and clipping. They bound \(X\) by its
initial norm plus its bounded velocity integral. For the zero-readout
reference one also has the pointwise bounds
\[
 cs\le C(s)\le bs.
\]

For state differences, the bottom forward estimate improves to
\[
 \|Z^{(2)}-\widetilde Z^{(2)}\|_2
 \le b\|W^{(2)}-\widetilde W^{(2)}\|_{\rm op}
     +B_2\lambda^2\|X-\widetilde X\|_2.
\]
If the reference readout has pointwise bound \(B\), the top estimate is
\[
 \|\delta^{(3)}-\widetilde\delta^{(3)}\|_2
 \le\lambda\|C-\widetilde C\|_2
       +\mu B\|Z^{(3)}-\widetilde Z^{(3)}\|_2.
\]
The middle estimate is
\[
 \|\delta_R^{(2)}-\widetilde\delta_R^{(2)}\|_2
 \le\lambda\|q^{(2)}-\widetilde q^{(2)}\|_2
       +2\mu R\|Z^{(2)}-\widetilde Z^{(2)}\|_2.
\]
Together with bounded matrix actions these give precisely a
\(C_S(1+R)\) Lipschitz bound in the state distance. Only the reference
readout needs a pointwise bound in the asymmetric comparisons.

Consequently the source's complete closed path set, short-interval
contraction, and repeated continuation construct the fixed-\(R\) flow
on every fixed feature interval. The readout bound is preserved by
integral iteration and by \(L^2\) limits. One-step Euler error is
\(O_R(\Delta^2)\), so the uniform error is \(O_R(\Delta)\).
Fixed-program width convergence, followed by mesh removal at fixed
\(R\), yields the fixed-clipping action-law limit. There is no use of
\(\phi(0)=0\), no assumption that an uncut \(L^2\) vector field is
locally Lipschitz, and no cutoff-independent contraction claim.

## 5. Cutoff removal, uniqueness, and reached-state restart

With the changed gate constants, the exact asymmetric decomposition at
source lines 1260–1286 is unchanged. For a reference state \(B\) clipped
at \(R\) and a state \(A\) clipped at \(R'\ge R\), including
\(R'=\infty\), it gives
\[
 \|\mathcal V_{R'}(A)-\mathcal V_R(B)\|
 \le C(1+R)d(A,B)+C\|b_R(q_B^{(2)})\|_2,
 \qquad b_R(q)=(|q|-R/2)_+.
\]
The constant is independent of \(R'\). This is why no tail bound on
the uncut comparison state is needed.

At fixed \(R\), Euler convergence and the top backward Lipschitz
estimate pass (H) to the continuous clipped \(q_R^{(2)}(s)\) by an
almost-sure subsequence and Fatou. Thus, exactly as at lines 1289–1308,
\[
 \sup_{s\le S}\|b_R(q_R^{(2)}(s))\|_2
 \le2K e^{-R^2/(16K^2)}=:\epsilon_R.
\]
Subtracting integral equations gives
\[
 \sup_{s\le S}d(\Theta_{R'}(s),\Theta_R(s))
 \le e^{C(1+R)S}
       [d(\Theta_{R'}(0),\Theta_R(0))+CS\epsilon_R].
\]
For common initial data, Gaussian decay in \(R\) dominates this
exponential in \(R\). Completeness gives an uncut limit. The same
asymmetric estimate, now evaluated at that limit, proves uniform
convergence of velocities: the extra factor \(1+R\) still vanishes
against the Gaussian error. This justifies the unbounded middle product
and passage through the integral equations.

For an arbitrary other bounded-primal uncut integral solution, the same
comparison to the clipped reference proves uniqueness, without its own
tail estimate. For restart at \(\sigma\in[0,S)\), its initial error
against the restricted reference is already bounded by
\(C e^{C(1+R)S}\epsilon_R\). Gronwall on \([\sigma,S]\) adds
another exponential in \(R\), still dominated by \(\epsilon_R\).
This proves unique restart from a reached state on the remaining
constructed feature interval. It does not establish continuation from
arbitrary initial states, fresh Gaussian restart laws, or feature time
beyond \(S\).

The finite-width bridge also transfers. At fixed \(R\), the continuous
quadratic-growth measurement \(b_R(q)^2\) has a uniformly converging
empirical average. The state velocity bound and the top backward
Lipschitz estimate give a common time modulus, so a finite time net
yields
\[
 \sup_{s\le S}|a_{n,R}(s)-a_R(s)|\to0
 \quad\text{in probability},\qquad
 a_{n,R}=\|b_R(q_{n,R}^{(2)})\|_n.
\]
The reference always has zero initial readout. The prescribed readout
obeys \(\varepsilon_n=\|C_0\|_n=O_{\mathbb P}(n^{-1})\); its
conditional initial predictor variance is
\(\|H^{(3)}_0\|_n^2/n^3\), so the offset introduces no order-one
initial predictor. Comparing the finite uncut flow to the clipped
reference adds \(\varepsilon_n\), exactly as in source equation (14).
The reference pointwise bound avoids any need for a coordinatewise-small
uncut readout. Finite uncut feature flows have global finite-dimensional
existence on fixed feature intervals from the displayed primal bounds
and smoothness. Take width to infinity at fixed \(R\), then remove
\(R\). No finite-width Gaussian-tail assertion is being added.

## 6. Raw gradient structure, coercivity, and observable transfer

The source's scalar-predictor differentiability argument at lines
1814–1856 uses bounded first and second derivatives and an \(L^2\)
backward coefficient. On its truncated part use Taylor remainder
\((\mu/2)|e|^2\); on its tail use \(2\lambda|e|\).
The identical two-limit argument proves the derivative in the raw
Hilbert metric. Rank-one velocity differences converge also in
Hilbert–Schmidt norm, so trained matrix increments belong to that
metric even though initial Gaussian actions need not be
Hilbert–Schmidt. The gradient and all four kernel formulas survive
with the new gates and features:
\[
 \nabla f=(\delta^{(1)},\delta^{(2)}\otimes H^{(1)},
                 \delta^{(3)}\otimes H^{(2)},H^{(3)}),
 \qquad \frac{df}{ds}=\kappa=\sum_{j=1}^4\kappa_j.
\]
The continuous inverse-coordinate chain rule uses
\(\operatorname{Lip}(F^{-1})\le\lambda\). It is not a change to the
raw gradient metric or a rescaling of the physical clock.

There is now a distribution-independent kernel lower bound
\[
 \kappa\ge\kappa_4=E(H^{(3)})^2\ge c^2=25/36.
\]
The primal bounds give, for the uncut flow, the finite upper bound
\[
 \kappa\le K_*:=b^2+\lambda^2b^2B_4^2
   +\lambda^4b^2B_3^2B_4^2
   +\lambda^6B_2^2B_3^2B_4^2.
\]
For the population reference take \(\varepsilon=0\). These are
coercivity bounds for prediction dynamics. They do not say every hidden
kernel block has a positive lower bound or that \(d(Z)\) is bounded
away from zero. The source's forward velocity operators also satisfy
\(\mathcal A^{(2)}\succeq c^2I\) and
\(\mathcal A^{(3)}\succeq c^2I\), by their displayed positive
operator decompositions; no sign symmetry is involved. These structural
facts do not substitute for the separate feature certificate.

The output map is Lipschitz on the bounded state sets. The uniform
backward-field comparison first supplies \(\delta^{(2)}\), then
\(q^{(1)}\). For products with bounded gates, use the source's extra
fixed truncation of the \(L^2\) factor and uniform integrability of
squared tails. Compactness of the continuous population \(L^2\) time
image, together with uniform joint \(\mathcal W_2\) convergence,
allows that truncation to be removed uniformly in time. This transfers:

- the stated finite same-layer action measurements in both orientations
  of both hidden matrices, including joint specified times;
- prediction, residual, loss, and all four raw kernel blocks;
- the source equation (22) for preactivation velocities, with the new
  \(d,d^2,H\), and the corresponding feature velocities;
- hidden path laws and second moments of the path supremum, via finite
  time grids and
  \(\|z-I_\pi z\|_\infty^2\le4|\pi|\int|\dot z|^2\);
- integrated squared velocities after the same gate truncation for the
  recomputed raw-GD interpolants.

State distances compare only states on the same population spaces or
at the same finite width. Cross-width and finite-to-population claims
are action-law statements, not operator-norm convergence between
different Hilbert spaces. No cross-layer neuron pairing is introduced.
The current four fields/operators determine their own velocities; the
Gaussian response coefficients are proof variables, not external
state inputs. Nothing here establishes hidden movement or noncollapse
by itself.

## 7. Replacement for the local physical-clock restriction

The old guard \(|f|\le a^2s\le1/4\) is unnecessary for this activation,
but it must be replaced by an argument. There are two complementary
facts, both with explicit hypotheses.

**Clock confinement, even for auxiliary clipped references.** Every
zero-readout clipped or uncut feature trajectory on \([0,S]\) satisfies
pointwise \(C(s)=\int_0^s H^{(3)}(u)\,du\ge cs\). Hence
\[
 f_R(s)=E[C_R(s)H_R^{(3)}(s)]\ge c^2s,
 \qquad f_R(0)=0,
 \qquad f_R(3/2)\ge25/24>1.
\]
Their predictors have a common finite Lipschitz constant on \([0,S]\)
by the uniform state velocities and output-map bound. Let \(s_R^*\)
be their first level-one point. Continuity gives
\(0<s_R^*\le1/c^2=36/25<S\). Before that point the scalar clock
\(s_R'=2(1-f_R(s_R))\) is positive. It cannot reach the equilibrium
\(s_R^*\) in finite time: if \(L\) is a predictor Lipschitz constant,
then \(s_R'\le2L(s_R^*-s_R)\), so
\(s_R^*-s_R(t)\ge s_R^*e^{-2Lt}\). The scalar equation therefore
exists on every finite physical horizon and stays in the constructed
feature interval. In fact, scalar integration of
\(s_R'\le2(1-c^2s_R)\) gives
\[
 0\le s_R(t)\le\frac{1-e^{-2c^2t}}{c^2}<\frac{36}{25}<\frac32.
 \tag{C}
\]
This uses the positive activation floor and the readout equation, not
monotonicity of a clipped predictor. The margin to \(S\) is at least
\(3/50\), uniformly in physical time and clipping.

**Residual separation for the uncut population flow.** Conditional on
(H) and cutoff removal, the raw gradient identity gives
\(c^2\le f'(s)=\kappa(s)\le K_*\) on \([0,S]\). Thus its level-one
point is unique and satisfies
\[
 1/K_*\le s^*\le1/c^2<S.
\]
For \(s<s^*\),
\(1-f(s)=\int_s^{s^*}\kappa(u)\,du\le K_*(s^*-s)\).
Consequently \(\int_0^{s^*}[2(1-f(s))]^{-1}\,ds=\infty\).
Every finite physical horizon is covered before \(s^*\). More
quantitatively,
\[
 1-f(s(t))
 =\exp\left(-2\int_0^t\kappa(s(u))\,du\right),\qquad
 e^{-2K_*T}\le1-f(s(t))\le e^{-2c^2t}
 \quad(0\le t\le T).
 \tag{R}
\]
The positive lower bound is for fixed finite \(T\); no uniform
positive residual at infinite time is claimed.

For finite feature flows with small nonzero initial readout, the same
gradient identity holds. Their predictor starts at \(f_n(0)=o_P(1)\)
and has derivative at least \(c^2\). With probability tending to one
its level-one point is below \(S\), since
\(f_n(0)+c^2S>1\) whenever \(f_n(0)>-1/24\). Its physical deficit
\(1-f_n\) stays positive on finite horizons by the finite gradient identity and
the upper primal bounds. Uniform feature prediction convergence and
scalar Gronwall then compare its clock with the population clock on
each fixed \([0,T]\). The same scalar comparison applies to clipped
reference clocks using (C).

Raw physical uniqueness and restart also extend to each such horizon.
For a competing bounded-primal raw integral solution, the rank-one
equations place trained increments in the raw Hilbert space, and the
gradient chain rule gives
\(1-f(t)=(1-f(0))\exp(-2\int_0^t\kappa(u)du)>0\).
Its feature clock is increasing. The coordinatewise chain rule gives
\[
 F(Z^{(1)}(t))=F(Z^{(1)}_0)
       +\int_0^t2(1-f(u))q^{(1)}(u)\,du\in L^2.
\]
The readout equation implies \(C(t)\ge c s(t)\), and hence
\(f(t)\ge c^2s(t)\); positivity of \(1-f(t)\) confines this clock
below \(36/25\). Feature uniqueness from Section 5 and scalar-clock
uniqueness identify the competing trajectory. From a reached state at
feature time \(\sigma\), use \(C(\sigma)\ge c\sigma\) and the
absolute feature clock \(\sigma+\int2(1-f)dt\). The same argument
uses only reached-state restart within \([0,S]\). It does not require
a fresh response bootstrap at restart.

## 8. Exact raw GD: corrected coordinate error and a stopped clock proof

The continuous clock proof alone does not justify positive raw-GD
increments. The following argument repairs the exact gap left by
replacing the source's \(T_0\) by an arbitrary \(T\).

Let \(\eta=n^{-2}\), \(\alpha_k=2\eta(1-f_{n,k})\), and
\(s_k=\sum_{j<k}\alpha_j\). Consider any prefix for which all updates
used so far start at nodes with \(f_{n,k}<1\), so their increments are
positive. On such a prefix, exact readout
updates imply, at every reached node,
\[
 C_k\ge C_0+cs_k\quad\text{coordinatewise},\qquad
 f_{n,k}\ge c^2s_k-b\varepsilon_n.
\]
The latter follows from Cauchy–Schwarz for \(\langle C_0,H_k^{(3)}\rangle_n\),
so it does not require \(C_0\ge0\). Work on the event
\(\varepsilon_n\le1/112\), whose probability tends to one; then
\(b\varepsilon_n\le1/96\). Whenever an increment is positive,
\[
 0<\alpha_k\le2\eta(1+b\varepsilon_n)<3\eta,
\]
\[
 s_{k+1}\le(1-2c^2\eta)s_k+2\eta(1+b\varepsilon_n).
\]
For \(2c^2\eta\le1\), induction gives
\[
 0\le s_k\le\frac{1+b\varepsilon_n}{c^2}
       \le\frac{291}{200}<\frac32
 \tag{G1}
\]
at every reached node, including the first possibly bad endpoint.
Thus all positive-prefix primal bounds are valid on the already
constructed feature interval, independently of its physical duration.
This does not yet rule out that bad endpoint; the comparison below does.

For the raw first-layer step \(z_+=z+\alpha d(z)q\), the exact
identity is
\[
 F(z_+)=F(z)+\alpha q
        +10\alpha^2z\,d(z)^2q^2
        +\frac{10}{3}\alpha^3d(z)^3q^3.
 \tag{G2}
\]
The factor 10 in both remainders is essential. Since
\(\sup_z10|z|d(z)^2<\infty\) and \(d\le\lambda\), while
\(\|q\|_n\le C\), use
\[
 \|q^2\|_n\le\sqrt n\|q\|_n^2,\qquad
 \|q^3\|_n\le n\|q\|_n^3
\]
to bound the single-step defect by
\(C(\alpha_k^2\sqrt n+\alpha_k^3n)\). By (G1) and
\(\max\alpha_k<3\eta\), its sum over any such prefix is
\[
 CS(\eta\sqrt n+\eta^2n)=O(n^{-3/2}+n^{-3})\longrightarrow0.
 \tag{G3}
\]
The other blocks are exactly the uncut feature-field Euler updates.
No fourth/sixth population moment of \(q^{(1)}\) is being assumed.

At fixed \(R\), compare these nodes to the exact finite zero-readout
clipped reference at \(s_k\). The source's recurrence (17), with
changed constants, gives for every stopped positive prefix
\[
 \max_k d_n(\Theta^{\rm GD}_{n,k},\Theta_{n,R}(s_k))
 \le e^{C(1+R)S}\left[
 \varepsilon_n+C\int_0^S a_{n,R}(u)du
       +C_R\eta+C_S(\eta\sqrt n+\eta^2n)\right].
 \tag{G4}
\]
Indeed, \(a_{n,R}\) is Lipschitz in feature time, and its left sums
over *any*, including random, positive partition differ from the
corresponding integral by at most \(CS\max\alpha_k\). This is a
pathwise estimate, so selecting random stopped times creates no new
tail premise. Width convergence at fixed \(R\), then
\(R\to\infty\), and uniform clipped/population prediction convergence
show that
\[
 E_n:=\max_{\text{reached stopped nodes }k}
       |f_{n,k}-f(s_k)|\longrightarrow0
 \quad\text{in probability}.
 \tag{G5}
\]
Here the maximum includes the possible first bad endpoint. All estimates
to that endpoint use only earlier positive increments. There is no
assumption that the actual width-dependent GD mesh itself satisfies (H).

Here is main's proposed two-stop formulation, with its endpoint made
explicit. Fix \(T<\infty\), \(0<\eta<1\), and
\(N=\lceil T/\eta\rceil\), so \(N\eta\le T+\eta\le T+1\).
Choose the deficit bound on this enlarged horizon:
\[
 \rho_T=e^{-2K_*(T+1)},\qquad
 1-f(s(t))\ge\rho_T\quad(0\le t\le T+1).
\]
Let \(J\) be the first node \(j\le N\) satisfying either
\[
 f_{n,j}\ge1-\rho_T/2\qquad\text{or}\qquad s_j\ge147/100;
 \tag{G6}
\]
if no such node exists, take \(J=N\). Initialization is good with
probability tending to one since \(f_{n,0}\to0\) and
\(1-\rho_T/2\ge1/2\). At every node before a bad exit,
\(\alpha_k>\eta\rho_T>0\) and \(\alpha_k<3\eta\). Hence the
step *into* the exit node is a positive step. For \(3\eta<3/100\),
its endpoint obeys
\[
 s_J<147/100+3\eta<3/2.
\]
This endpoint argument certifies the interval required by (G4);
the stronger bound (G1) is also available. No post-exit update is taken
or analyzed. The comparison (G4) and the error (G5) include node \(J\)
because their recurrence to it uses only the good nodes \(k<J\).

On \([0,J\eta]\) interpolate \(s_k\) linearly in physical time. It
satisfies \(s_n'=2(1-f_{n,k})\) on each preceding step. If \(L\)
bounds the population predictor's feature-time Lipschitz constant, then
\[
 |s_n(t)-s(t)|
 \le2\int_0^t[E_n+3L\eta+L|s_n(u)-s(u)|]du.
\]
In particular, writing \(D_n=\sup_{t\le J\eta}|s_n(t)-s(t)|\),
\[
 D_n\le2(T+1)(E_n+3L\eta)e^{2L(T+1)}\longrightarrow0
 \quad\text{in probability}.
\]
At a putative first bad endpoint \(t_J\), (G5) gives
\[
 f_{n,J}\le1-\rho_T+E_n+LD_n<1-\rho_T/2,
 \qquad
 s_J\le36/25+D_n<147/100
\]
on the event \(E_n+LD_n<\rho_T/2\) and \(D_n<3/100\), whose
probability tends to one. Both exit conditions are contradicted,
including when the first exit would be the final interpolation endpoint
\(N\). Therefore all nodes needed on \([0,T]\) satisfy the guards
with probability tending to one, and (G4) applies throughout.
This is a stopped, finite-\(T\) comparison. It proves the conditional
extension of the exact-GD bridge without a global GD descent assertion
or an exact discrete gradient-flow identity. A deficit bound stated
only up to \(T\) must be enlarged to cover the extra endpoint; the
choice of \(\rho_T\) above does that.

For the specified raw linear interpolation, apply (G2) at every
fractional step \(0\le\alpha\le\alpha_k\). It controls the difference
between transforming the raw interpolant and interpolating in \(X\).
Recompute hidden objects from the raw interpolated parameters, as the
contract requires. The source's bounded-gate truncation argument for
velocities and squared speeds then applies with the new derivative
bounds. Use right derivatives at interior GD nodes and a left derivative
at a terminal node when needed.

Comparing GD and finite gradient flow to the same finite clipped
reference, using their convergent clocks and the reference's bounded
velocity, proves their same-width state-distance convergence on each
fixed \([0,T]\). Their action laws converge to the same population
law. Every limiting operation here fixes \(R\) before taking width to
infinity and subsequently removes \(R\); the resulting assertion is
full-sequence convergence in probability, not a selected subsequence
claim or an unproved exchange of limits. Constants may depend on \(T\).
No claim is made uniformly over \(T\to\infty\) or horizons growing
with width.

## 9. Handoff checklist and remaining scope

| Item | Status of this bounded transfer check |
| --- | --- |
| New activation at all hidden layers; unchanged raw normalization and initialization | Specified and checked above. |
| New common population actions, both matrices and both adjoints | Construction mechanism transfers with new roots/maps and full second moments; old trajectory/covariances cannot be reused. |
| Fixed-mesh source identification, singular cases, empirical feedback | Required hypotheses checked; retain all derivative returns and formal-source conventions. |
| Uniform Gaussian \(q^{(2)}\) tails on \([0,3/2]\) | **Candidate supplied by main, pending independent audit.** Its stated Gaussian/shift bounds imply (H), as checked in Section 1. The response proof is not audited here. |
| Fixed-clipping existence, Euler consistency, width limit | Transfers with explicit bounds in Section 4. |
| Cutoff removal and no surviving clipping | Conditional on (H), Section 5 passes the uncut field and velocities. |
| Unique uncut solution and restart at a reached state | Conditional on (H), same-space comparison works on the remaining feature interval; Section 7 extends physical restart along reached states. |
| Raw Hilbert gradient, autonomy, four raw kernel blocks | Transfers with new derivative gates; no finite-scalar closure is asserted. |
| Every finite physical horizon inside the constructed feature interval | Replacement derived in Section 7; strict feature margin follows from \(36/25<3/2\). |
| Exact raw GD, positive computational increments, prescribed interpolation | Original long-horizon gap explicitly closed conditionally by (G1)–(G6) and the finite-\(T\) two-stop argument, including its last endpoint. |
| Full-sequence joint MF/GF/GD action laws, paths, velocities, squared speeds | The source's convergence mechanisms transfer under (H) and the specified replacements; preserve its same-layer measurement scope. |
| Arctan pointwise sign argument | Does not transfer; initial Gaussian expectation replacement is displayed in Section 2. |
| Nonzero hidden learning, changing kernel, nonaffineness without distributional collapse at every finite physical time | **Not certified here.** Assigned to the separate feature/nonlinearity worker. The source itself proves its nonaffineness persistence only on an initial interval. |
| Complete new theorem / unconditional certification | **Not supplied.** Requires (H), assembly with the separate certificates, and the contract's subsequent adversarial checks. |

The concrete hazards are centering the new activation in covariance
formulas, treating zero backward initialization as a consequence of
\(\phi(0)=0\), copying the pointwise arctan sign argument, omitting the
factor 10 in the raw-GD coordinate defect, extending the old physical
guard without a replacement, and using a continuous clock argument as
if it already proved positivity of discrete increments. The displayed
replacements address those transfer hazards. They do not turn the
unproved response input or the separate feature certificates into a
full theorem.
