# Fixed-depth neuron compression: proved pieces and the remaining cavity term

2026-10-03. Scoped theory for `closure_sampling_20261003`. The assigned inputs
were the complete two-input stable-geometry, complex-source, canonical-compression,
one-input complex-activity, and weighted-activity notes, together with the
manuscript model and relevant all-time/tracking proofs and the maintained
notation contract. Canonical-notation, rigorous-proof, and conjecture-audit
instructions were applied. No other study, contemporary route or verdict,
experiment, trained trajectory, manuscript edit, or Git operation was used.
This artifact was frozen before exchange with other routes.

**Outcome.** The requested arbitrary-depth, all-sphere, all-time
`C/sqrt(n)` compression theorem is not established here. Three positive
statements below are proved: width- and mass-independent small-label fitting
at every fixed depth; an actual Gaussian bound for the first nonzero
backward-response derivatives, using independent deep neuron cavities; and
exact matching of arbitrarily many initialized time derivatives by an
initialization-only autonomous weighted network with polynomial storage in
the derivative order. The precise positive-time obstruction is an interior
gate difference multiplied by an interior backward carrier. An explicit
three-layer construction disproves the mass-independent vector-field bound
on the operator/Gram tube used by the two-layer argument. This does not
disprove the Gaussian compression conjecture or a more refined comparison.

## 1. Canonical and weighted systems

Fix the number `L >= 2` of hidden layers and `m <= d` orthogonal inputs
`x_a = sqrt(d) e_a`. Labels `y_a` can have either sign; put
`Y = |y|_2`. The original model has width `n` in every hidden layer,
iid first weights `N(0,1)`, independent hidden entries `N(0,1/n)`, and
zero stored readout. Its loss is `m^{-1} sum_a (f_a-y_a)^2`, and its
block mobilities are `(n,1,...,1,n)`.

It is useful to state an exact weighted version. Layer `ell` has `N_ell`
neurons and a positive diagonal mass matrix `D_ell`, of total mass at most
one. For a vector on that layer and an operator between successive layers,
define

\[
 \|v\|_{D_\ell}^2=v^\top D_\ell v,\qquad
 B^{(\ell)*}=D_{\ell-1}^{-1}B^{(\ell)\top}D_\ell,
 \qquad
 \|B^{(\ell)}\|_{\rm HS}
 =\|D_\ell^{1/2}B^{(\ell)}D_{\ell-1}^{-1/2}\|_F.
 \tag{1}
\]

The operator norm is between the indicated weighted Euclidean spaces.
The first weights are `A in R^{N_1 x d}`, hidden matrices are
`B^(ell) in R^{N_ell x N_{ell-1}}`, and `w in R^{N_L}`. Put

\[
 z^{(1)}(x)=Ax/\sqrt d,\quad h^{(1)}(x)=\tanh z^{(1)}(x),
 \quad z^{(\ell)}(x)=B^{(\ell)}h^{(\ell-1)}(x),\quad
 h^{(\ell)}(x)=\tanh z^{(\ell)}(x),
 \quad f(x)=w^\top D_Lh^{(L)}(x).
 \tag{2}
\]

A sample subscript means evaluation at `x_a`. The residual is `f_a-y_a`.
Define its negative, including the physical loss factor, by
`c_a=(2/m)(y_a-f_a)`. The backward responses exclude that coefficient:

\[
 \delta_a^{(L)}=w\odot\tanh'(z_a^{(L)}),\qquad
 k_a^{(\ell)}=B^{(\ell+1)*}\delta_a^{(\ell+1)},\qquad
 \delta_a^{(\ell)}=\tanh'(z_a^{(\ell)})\odot k_a^{(\ell)}
 \quad(\ell<L).
 \tag{3}
\]

The complete autonomous equations are

\[
 \dot A=\sum_a c_a\delta_a^{(1)}e_a^\top,\qquad
 \dot B^{(\ell)}=\sum_a c_a\delta_a^{(\ell)}
                         h_a^{(\ell-1)\top}D_{\ell-1},\qquad
 \dot w=\sum_a c_ah_a^{(L)}.
 \tag{4}
\]

The canonical dense model is exactly (2)--(4) with `D_ell=I/n` and
`B^(ell)=W^(ell)`. Thus this weighted convention preserves the paper's
mobilities. There is no normalization by the retained neuron count.
The parameter distance used below is

\[
 d(\widehat\theta,\theta)
 =\|D_1^{1/2}(\widehat A-A)\|_F
 +\sum_{\ell=2}^L\|\widehat B^{(\ell)}-B^{(\ell)}\|_{\rm HS}
 +\|\widehat w-w\|_{D_L}.
 \tag{5}
\]

For the dense model this is precisely the manuscript's normalized distance.

## 2. Unconditional fitting for arbitrary fixed depth

**Proposition 1.** Suppose `w(0)=0`, every initialized hidden operator has
norm at most `K`, and the initialized readout-feature Gram satisfies

\[
 G_0=(h_a^{(L)}(0)^\top D_Lh_b^{(L)}(0))_{a,b=1}^m
 \succeq\gamma I_m.
 \tag{6}
\]

For sufficiently small `Y`, depending only on `L,m,K,gamma`, the exact
weighted system (4) exists for all physical time, converges to a fitted
endpoint, and satisfies

\[
 |y-f(t)|_2\le Y e^{-\kappa t},\qquad
 \int_0^\infty |c(t)|_1dt\le C Y,\qquad
 \|w(t)\|_\infty\le CY,
 \tag{7}
\]

\[
 \|D_1^{1/2}(A(t)-A(0))\|_F
 +\sum_{\ell=2}^L\|B^{(\ell)}(t)-B^{(\ell)}(0)\|_{\rm HS}
 \le CY^2.
 \tag{8}
\]

Moreover

\[
 \sup_{\|x\|_2=\sqrt d}|f(t,x)-f(\infty,x)|
 \le CY e^{-\kappa t}.
 \tag{9}
\]

All constants are independent of the neuron counts and the smallest mass.

**Proof.** Write `s(t)=int_0^t |c(v)|_1 dv` and stop while every
hidden operator is bounded by `K+1` and `s<=S`. Bounded real tanh gives
`||h||_{D_ell}<=1` and `||w||_infty<=s`. Backward induction in (3)
gives `||delta_a^(ell)||_{D_ell}<=C s`. The identity

\[
 \|u v^\top D_{\ell-1}\|_{\rm HS}
       =\|u\|_{D_\ell}\|v\|_{D_{\ell-1}}
 \tag{10}
\]

then bounds the sum of hidden and first-layer speeds by `C s dot s`.
Their accumulated displacement is at most `C S^2`. Forward subtraction,
using the real Lipschitz constant one of tanh, gives
`||h_a^(L)(t)-h_a^(L)(0)||_{D_L}<=C S^2`. Hence
`||G(t)-G_0||_op<=C S^2`.

Differentiating the predictions in (4) gives

\[
 \frac{d}{dt}(y-f)=-\frac2m K(t)(y-f),
\]
\[
 K_{ab}=\langle h_a^{(L)},h_b^{(L)}\rangle_{D_L}
 +\mathbf1_{a=b}\langle\delta_a^{(1)},\delta_b^{(1)}\rangle_{D_1}
 +\sum_{\ell=2}^L
   \langle\delta_a^{(\ell)},\delta_b^{(\ell)}\rangle_{D_\ell}
   \langle h_a^{(\ell-1)},h_b^{(\ell-1)}\rangle_{D_{\ell-1}}.
 \tag{11}
\]

Every summand is positive semidefinite: the hidden summand is the Gram
of the rank-one operators in (10), and the first-layer term is diagonal.
Choose a fixed `S_0` so that `CS_0^2` is below both `1/2` and
`gamma/2`. Then `K>=G>=gamma I/2` before the stop, and therefore
`|y-f(t)|<=Y exp(-gamma t/m)`. In particular

\[
 s(t)\le\frac2m\sqrt m\int_0^t |y-f(v)|_2dv
             \le 2\sqrt m Y/\gamma.
\]

Taking `Y<=gamma S_0/(4 sqrt m)` excludes the activity boundary;
the strict hidden displacement bounds exclude the operator boundary.
The finite-dimensional, smooth real ODE cannot escape at finite time
because these weighted norms bound all coordinates at fixed positive
masses. This proves (7)--(8) globally. The integrable speeds imply
parameter convergence, and (7) implies fitting.

For any `||x||=sqrt d`, the first-layer query speed is at most the
weighted Frobenius speed of `A`; forward induction gives
`||dot h^(L)(x)||_{D_L}<=CY |c|_1`. Differentiating the last
pairing in (2) now gives `|dot f(x)|<=C |c|_1`, uniformly in the
sphere query. Integrating the exponential residual estimate proves (9).
No backward coordinate maximum enters this proof. ∎

For canonical Gaussian initialization, (6) holds with fixed positive
`gamma` with exponentially high probability. In fact, put
`q_1=E tanh^2 Z` and `q_ell=E tanh^2(sqrt(q_{ell-1}) Z)` for a
standard real Gaussian `Z`. For orthogonal inputs the initialized feature
Gram converges to `q_ell I_m` at each layer. The first-layer entries are
independent across sample coordinates. Conditional on earlier layers,
the rows of the next preactivation matrix are iid centered Gaussian
vectors with the preceding empirical Gram as covariance. The Gaussian
expectation of each bounded tanh product is continuous in this covariance.
On a fixed neighborhood of `q_{ell-1} I_m`, that continuity and the
exponential concentration of bounded iid variables propagate a fixed
neighborhood of `q_ell I_m`. There are only finitely many layers and
entries. Gaussian sphere nets simultaneously bound all hidden operator
norms. This proves the required fixed Gram gap and operator event.

## 3. What the first-layer transformation does not remove

For the orthogonal training inputs, put

\[
 \Psi(a)=a/2+\sinh(2a)/4,\qquad u_a=\Psi(Ae_a).
\]

Then `dot u_a=c_a k_a^(1)` exactly. The corresponding inverse has the
fixed strip and real Lipschitz bounds proved in the assigned one-input
complex note. This still removes the first-layer gate from its own
velocity at every depth.

An interior response nevertheless contains

\[
 \widehat\delta_a^{(\ell)}-\delta_a^{(\ell)}
 =\tanh'(\widehat z_a^{(\ell)})\odot
                          (\widehat k_a^{(\ell)}-k_a^{(\ell)})
 +[\tanh'(\widehat z_a^{(\ell)})-\tanh'(z_a^{(\ell)})]
                          \odot k_a^{(\ell)},
 \quad 2\le\ell<L.
 \tag{12}
\]

The exact differential version of the second term is

\[
 \tanh''(z_a^{(\ell)})\odot k_a^{(\ell)}\odot dz_a^{(\ell)}.
 \tag{13}
\]

The multiplication operator in (13) has weighted Euclidean operator norm
`max_i |tanh''(z_i) k_i|`; changing the positive masses does not reduce
that norm. The estimates in Proposition 1 only give an RMS carrier bound.
At depth two the only response of this form in a learned matrix is the
top response, whose carrier is the coordinate-bounded readout. At depth
three (13) first occurs at an interior learned matrix.

There is a concrete obstruction to simply asserting a bounded derivative
of the transformed field on the real fitting tube.

**Proposition 2.** For arbitrarily large even widths `n`, there are
three-hidden-layer real initialized states with uniformly bounded hidden
operator norms and a fixed positive two-input readout Gram, and states
with the identical hidden parameters and readout maximum at most `tau`,
where the norm of the derivative of a residual-free vector field, measured
in (5) with the transformed first-layer coordinates, is at least
`c tau sqrt(n)`. The constants are independent of `n` and `tau>0`.

**Proof.** Write `n=2N` and divide the neurons into groups `H_1,H_2`
of size `N`. Choose a fixed `a_0>0`; set column `a` of `A` equal to
`a_0 1_{H_a}`. Let `B^(2)=I`. Put `b=tanh a_0` and `h=tanh b`,
so the first two training feature columns are `b 1_{H_a}` and
`h 1_{H_a}`. Within each group take

\[
 u_a=\mathbf1_{H_a}/\sqrt N,\qquad
 q_{a,i_a}=1/\sqrt2,\qquad
 q_{a,i}=1/\sqrt{2(N-1)}\quad(i\in H_a\setminus\{i_a\}),
\]

and zero coordinates elsewhere. Set
`B^(3)=u_1 q_1^T+u_2 q_2^T`, whose operator norm is one.
The third-layer preactivation for sample `a` is `beta_N 1_{H_a}`,
where

\[
 \beta_N=\frac h{\sqrt N}
           \left(\frac1{\sqrt2}+\sqrt{\frac{N-1}{2}}\right).
\]

Thus `g_N=tanh beta_N` is bounded away from zero for `N>=2`,
and the initialized Gram is `(g_N^2/2) I_2`.
Keep these hidden weights and set `w=tau g_N 1`. At the distinguished
neuron of sample `a`,

\[
 k_{a,i_a}^{(2)}
  =\frac{\tau g_N\tanh'(\beta_N)\sqrt N}{\sqrt2}
  \ge c\tau\sqrt N.
 \tag{14}
\]

Perturb only `B^(2)` by
`E=e_{i_a} h_a^(1)T / ||h_a^(1)||_2`. Its Frobenius norm is one,
and `d z_a^(2)=b sqrt(N) e_{i_a}`. The direct term in (13),
at coordinate `i_a`, is negative with magnitude at least `c tau N`,
since `tanh''(b)<0`. The additional term in `d k_a^(2)` comes
from the changed top gate; it is also nonpositive at this coordinate:
all intervening coefficients are positive and `tanh''(beta_N)<0`.
Consequently `|d delta_{a,i_a}^(2)|>=c tau N`.

The `B^(2)` block of the residual-free field is
`delta_a^(2) h_a^(1)T/n`. Its directional derivative therefore has
Frobenius norm at least

\[
 c\tau N\,\|h_a^{(1)}\|_2/n\ge c'\tau\sqrt n.
\]

The perturbation leaves the transformed first-layer coordinates unchanged,
so the same lower bound holds in the transformed state norm. ∎

This is a deterministic counterexample to a theorem using only operator,
Gram, displacement, and readout bounds. Its matrices are not Gaussian,
and its final readout state is not asserted to be an actual trained state.
It therefore does not disprove the canonical Gaussian theorem. It does
show exactly why the two-layer tube verification cannot be copied.

## 4. Actual independent deep cavities at initialization

A cavity deleting neuron `i` of hidden layer `ell` removes its incoming
row and its outgoing column; at the first or last layer the corresponding
outer coordinate is removed. Every normalization remains `n`. Its own
forward pass, its own labels, and its own residuals define an autonomous
network. The cavity is independent of every omitted Gaussian row or
column, since it is a deterministic function of the retained initialization.
No trained full residual is supplied to it.

There is a quantitative positive result for the first nonzero backward
response, which already requires the interior cavities.

**Proposition 3.** For the canonical Gaussian initialization at fixed
`L,m`, with probability at least `1-eta`, for all sufficiently large `n`,

\[
 \max_{a,\,\ell<L,\,i}|\dot k_{a,i}^{(\ell)}(0)|
 \le C_{L,m}Y\sqrt{\log(en/\eta)}.
 \tag{15}
\]

The same bound holds for `dot delta_a^(ell)(0)`. The top response has
the sharper coordinate bound `CY`.

**Proof.** At initialization the hidden velocities vanish. Define

\[
 v=\dot w(0)=\frac2m\sum_b y_bh_b^{(L)}(0).
\]

Then `||v||_infty<=CY`, and differentiating the actual equations gives

\[
 \dot\delta_a^{(L)}(0)=v\odot\tanh'(z_a^{(L)}(0)),\qquad
 \dot k_a^{(\ell)}(0)=W_0^{(\ell+1)\top}
                                  \dot\delta_a^{(\ell+1)}(0),
 \qquad
 \dot\delta_a^{(\ell)}(0)=\tanh'(z_a^{(\ell)}(0))
                                  \odot\dot k_a^{(\ell)}(0).
 \tag{16}
\]

Work on the event that every initialized hidden operator is at most `K`.
These recursions give all full and cavity derivative RMS norms at most
`CY` without any maximum estimate.

For a neuron deleted at layer `ell`, initialized full/cavity forward
features agree below it. At layer `ell+1` their difference is caused by
`W_0^(ell+1)_{:,i} h_{a,i}^(ell)`, of ordinary Euclidean norm at most
`K`; forward induction bounds every subsequent feature and preactivation
difference by `C_L`. The difference of the two vectors `v` is therefore
at most `CY` in ordinary Euclidean norm.

Set `M_p=max_{a,i}|dot k_{a,i}^(p)(0)|` for `p<L`, and set
`M_L=||v||_infty`. Descending through the backward derivative recursion,
using the full carrier in the changed-gate term, proves

\[
 \|\dot\delta_a^{(\ell+1)}(0)
      -\dot\delta_a^{(\ell+1),-i}(0)\|_2
 \le C\left(Y+\sum_{p=\ell+1}^{L-1}M_p\right).
 \tag{17}
\]

At the top this follows from the bound for `v`, its difference, and the
forward preactivation difference. At a lower retained layer, the changed
carrier costs `K` times the next backward difference, and the changed
gate costs `2M_p` times its bounded Euclidean preactivation difference.
These are all terms in (17).

The omitted outgoing column `xi=W_0^(ell+1)_{:,i}` is independent
of the cavity derivative source. Conditional on retained initialization,
it remains `N(0,I/n)`. Set that source to zero if its retained operator
condition fails. Its conditional RMS is at most `CY`, so the scalar
Gaussian tail and a union over the finitely many samples and `Ln`
neurons give

\[
 |\xi^\top\dot\delta_a^{(\ell+1),-i}(0)|
                  \le CY\sqrt{\log(en/\eta)}
 \tag{18}
\]

simultaneously. The Gaussian assertion is made before intersecting the
full operator event. On the latter event all needed cavity sources are
available and `||xi||_2<=K`. Equations (17)--(18) imply

\[
 M_\ell\le CY\sqrt{\log(en/\eta)}
                  +C\sum_{p>\ell}^{L-1}M_p.
\]

Finite downward induction proves (15). Multiplication by the bounded
initial gate in (16) proves the response claim. ∎

This proof has no adaptive conditioning problem: only initialized cavity
sources enter the Gaussian pairings. It does not give the same bound at
positive training time.

## 5. Exact finite-order compression at arbitrary depth

There is also a complete autonomous compression theorem for initialized
jets, with no complex-source hypothesis.

**Proposition 4.** Fix a nonnegative integer `q` and a finite list of
`P` passive query inputs. From the dense initialization and labels alone,
one can construct a weighted network (2)--(4), of the same depth, whose
training and passive-query prediction derivatives satisfy

\[
 \partial_t^r f_C(0,x)=\partial_t^r f_n(0,x),
 \qquad 0\le r\le q+1,
 \tag{19}
\]

at every input in that finite list and every training input. Its total
moving and fixed stored real coordinates after setup are at most

\[
 C_L\left[((m+P)(q+1)+d)^4
                    +d((m+P)(q+1)+d)^2\right].
 \tag{20}
\]

The construction preserves all initial hidden operator bounds and the
initial readout Gram. Consequently the small-label hypothesis of
Proposition 1 gives global own-feedback fitting and the all-sphere tail
bound for both networks. Equation (19) itself is only a finite-order,
finite-query statement; it is not a trajectory error estimate.

**Construction.** Differentiate the finite original ODE algebraically at
`t=0` through the required finite orders. These are initialized derivatives,
not values obtained by training. In layer `ell`, form a real source space
`S_ell` containing:

- all `partial_t^r h^(ell)(0,x)`, for training and passive queries and
  `0<=r<=q`;
- all `partial_t^r delta_a^(ell)(0)`, for training samples and
  `0<=r<=q`;
- every corresponding paired vector
  `W_0^(ell) partial_t^r h^(ell-1)(0,x)` when `ell>=2`;
- every corresponding paired vector
  `W_0^(ell+1)T partial_t^r delta_a^(ell+1)(0)` when `ell<L`.

Include the `d` columns of `A_0` in `S_1`. The dimension of each space
is at most `C[(m+P)(q+1)+d]`. Choose a basis matrix `V_ell` with
`V_ell^T V_ell/n=I`. Matching the constant and all symmetric products
of its basis columns by positive empirical cubature gives a node set
`I_ell` and positive masses `D_ell`, of total mass one, such that

\[
 V_{\ell,I_\ell}^\top D_\ell V_{\ell,I_\ell}=I,
 \qquad |I_\ell|\le1+\frac{r_\ell(r_\ell+1)}2,
 \quad r_\ell=\dim S_\ell.
 \tag{21}
\]

For completeness, the original uniform empirical weights give one positive
representation of those moments. If its positive support exceeds one plus
the number of symmetric products, an affine dependence of the evaluation
vectors permits a nonzero weight variation preserving every moment and
mass. Move in one sign until a weight first vanishes. Repeating gives
(21). Zero weights are discarded.

Initialize the smaller hidden operators by

\[
 C_\ell=V_\ell^\top W_0^{(\ell)}V_{\ell-1}/n,\qquad
 B_0^{(\ell)}=V_{\ell,I_\ell}C_\ell
                     V_{\ell-1,I_{\ell-1}}^\top D_{\ell-1}.
 \tag{22}
\]

The selected basis maps are isometries in the weighted norms. Hence
`||B_0^(ell)||_op<=||W_0^(ell)||_op`. For every included paired source,

\[
 B_0^{(\ell)}v_{I_{\ell-1}}=(W_0^{(\ell)}v)_{I_\ell},\qquad
 B_0^{(\ell)*}d_{I_\ell}=(W_0^{(\ell)\top}d)_{I_{\ell-1}}.
 \tag{23}
\]

These identities follow by expanding the two source vectors in their
basis matrices and using (21). Initialize `A_C=A_{0,I_1}` and
`w_C=0`, and run exactly (4). The ordinary retained forward pass is
therefore exact initially on the finite query list. The initial training
Gram is exactly preserved by (21).

**Proof of the jet claim.** Induct on the temporal order `r`. At order
zero the forward pass is matched by (23), and every backward response
and prediction vanishes because the readout is zero. Suppose all lower
orders of the computed sources and residuals have been matched. The
product rule applied to (4) determines the order-`r` first-weight,
readout, and learned-matrix derivatives from these lower source orders.

In a forward pass at order `r`, the initialized-matrix term is matched
by the first identity in (23). Each differentiated learned-matrix term
has the form of a training response derivative multiplied by a pairing
of two lower-layer feature derivatives. All those feature derivatives
belong to `S_{ell-1}`, so (21) preserves the pairing. Thus the entire
preactivation derivative is the restriction of the original one. Applying
the scalar product/chain rule to tanh gives the same statement for its
feature derivative. This proceeds upward through all layers and applies
to every passive query.

In the backward pass, the initialized-transpose term is matched by the
second identity in (23). A differentiated learned-transpose term is a
lower-layer training feature derivative multiplied by a pairing of two
training response derivatives in `S_ell`; again (21) preserves the
pairing. Descending through the layers and applying the scalar chain
rule proves matching of every order-`r` training response.

For prediction derivatives, each positive-order derivative of `w` is a
linear combination of initialized derivatives of training `h^(L)` of
strictly lower order, by the last equation in (4). Those vectors belong
to `S_L`. Every needed pairing with a feature derivative is consequently
preserved by (21). This proves prediction and residual matching at order
`r`, closes the induction through order `q`, and also gives prediction
matching at order `q+1`: the term involving the order-`q+1` feature
is multiplied by `w(0)=0`, and all remaining factors have just been
matched. This proves (19).

Only `A_C`, the matrices `B_C^(ell)`, and `w_C` move after setup.
Fixed masses and labels are retained; the full basis arrays, derivative
vectors, original matrices, and product-matching working arrays are
then discarded. Equation (21) gives (20). Current states determine all
future velocities, so this is autonomous and restartable. ∎

Taking `q` to be any fixed power of `log n` gives polylogarithmic total
storage and exact matching of that many training derivatives at any
fixed finite collection of probes. This is a positive finite-order result,
not an inference that the analytic continuation radius is width independent.

## 6. The unresolved positive-time bridge

At positive time an interior deletion has two direct discrepancies in
the retained equations. Deleting neuron `i` of layer `ell`, with
`1<ell<L`, produces the forward discrepancy at layer `ell+1` and
the reverse discrepancy at layer `ell-1`

\[
 e_a^z=W^{(\ell+1)}_{:,i}h_{a,i}^{(\ell)},\qquad
 e_a^k=W^{(\ell)\top}_{i,:}\delta_{a,i}^{(\ell)}.
 \tag{24}
\]

Here the second formula means the incoming row, transposed, multiplied
by the scalar response. All other retained differences propagate through
the ordinary forward/backward recursions. Operator bounds give

\[
 \|e_a^z\|_2\le C,\qquad
 \|e_a^k\|_2\le C|\delta_{a,i}^{(\ell)}|.
 \tag{25}
\]

The normalized second error is therefore only
`C |delta_{a,i}^(ell)|/sqrt(n)`. Proposition 1 bounds its RMS source,
but permits this particular coordinate to be of order `Y sqrt(n)`.
Even after imposing a candidate maximum cap `M`, comparison of the two
responses encounters precisely (12), and its available Lipschitz bound
has a factor `1+M`.

A bound obtained by Gronwall over total residual activity `CY` then
contains `exp(CY(1+M))`. With the desired Gaussian-scale cap
`M ~ Y sqrt(log n)`, this multiplier is larger than every fixed power
of `log n` as `n` grows. Feeding this bound into the elementary
reinsertion estimate

\[
 |k_{a,i}^{(\ell)}-\xi_i^\top\delta_a^{(\ell+1),-i}|
 \le \|\xi_i\|_2
          \|\delta_a^{(\ell+1)}-\delta_a^{(\ell+1),-i}\|_2
 +\|W^{(\ell+1)}_{:,i}-\xi_i\|_2
          \|\delta_a^{(\ell+1)}\|_2
 \tag{26}
\]

does not improve that cap. At initialization the triangular induction in
(17) uses only higher layers and avoids this amplification. Once the
hidden matrices learn, the cavity difference is coupled through the
training flow, and that triangular argument no longer supplies (26).

The cavity itself remains a valid independent Gaussian reference. What
is missing is a sufficiently strong *comparison to it*. Using the full
residual as its driving function would make the reference depend on the
omitted Gaussian coordinate, and would invalidate the conditional tail
argument. Declaring the full carrier to be Gaussian would have the same
problem.

For the required complex-source theorem one must additionally control
coordinate velocities of forward preactivations on short vertical complex
time segments, and passive sphere-query derivatives, before applying the
corresponding tanh gates. Real fitting and the finite initial derivative
bound do not provide those pole margins. Finite-dimensional analyticity
at each `n` supplies some positive radius, but gives no polylogarithmic
lower bound on it.

The all-time paper's integrated carrier tail has an unspecified remainder
`a_n -> 0` in probability. That type of statement cannot substitute for
the quantitative finite-network estimates needed here: it does not yield
an error `C/sqrt(n)` against the realized width-`n` run, nor a controlled
complex continuation radius. No quantitative rate for that remainder is
assumed in this note.

Thus the surviving obligation is an actual positive-time deep cavity
comparison controlling (12), (24), and (26), followed by a pole-safe
complex source domain with inverse-polylogarithmic widths. The jet
construction in Section 5 is already autonomous and has the right total
storage accounting; what remains unproved is the source-to-trajectory
estimate that would justify truncating its initialization information at
polylogarithmic order. This note does not relabel that obligation as an
assumption in a purported compression theorem.
