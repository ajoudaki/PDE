##### C.4.7.3. Uniform passive-query tails for raw Euler programs

Fix \(Y\ge1\), \(T=40\), the raw state \(\theta=(w,K,c)\),
\(A=A_0+K\), and the initialization \((g,0,0)\) stated above.
The aliases \(w=W^{(1)}\), \(A=W^{(2)}\), and \(c=W^{(3)}\)
retain their stated population types. Let
\(\lambda=\sum_a p_a\delta_{(\sqrt2u_a,y_a)}\), where
\(p_a>0\), \(\sum_a p_a=1\), \(|u_a|=1\), and \(|y_a|\le Y\).
Consider any finite raw Euler program with deterministic positive steps
\(h_k\), nodes \(t_k=\sum_{j<k}h_j\), and total length at most \(T\).
All residuals are its actual population residuals. Every named-source
derivative below freezes residuals, contractions, covariance laws, and
deterministic response coefficients; it differentiates only the named
coordinate expression. Throughout, \(\phi=\tanh\); unqualified \(L^p\)
norms use the population of their argument. Generic constants \(C\),
\(C_B\), and \(C_{B,p}\) may increase from one estimate to the next and
depend only on \(Y,T\), the fixed model, and the displayed cap and moment
order. The constants \(C_0,R_0\) defined in (N9) remain fixed.

For a passive query \(u\in S^1\), distinguish its one current forward
slot from the earlier training slots, and define
\[
 \mathcal B_k=\sup_{u\in S^1}
 \left\{|\beta_{ku,ku}|+\sum_{s<k,b}|\beta_{ku,sb}|\right\}.
 \tag{N1}
\]
The coefficients are defined below. Each row is obtained by appending a
fresh unused query to a finite program; earlier unused queries contribute
zero response coefficients. The deterministic row functions extend
continuously to the whole circle. The supremum in (N1) is outside every
expectation.

We prove that there are \(\rho>0\), \(h_0>0\), and \(B<\infty\),
depending only on \(Y,T\) and the fixed model, such that
\[
 \mathcal W_1(\lambda,\nu_*)<\rho,\qquad
 h_{\max}:=\max_k h_k\le h_0
 \quad\Longrightarrow\quad
 \sup_{k:t_k\le T}\mathcal B_k\le B.
 \tag{N-cap}
\]
The same constants work for every finite support cardinality, every
positive set of atom weights, every covariance rank, and every admitted
mesh. They will give constants \(a,M>0\) such that every recomputed
passive reverse query, including at affine Euler interpolation times,
satisfies \(\tau_R(Q(u))\le M e^{-aR^2}\) for \(R\ge1\).

The proof first obtains all moment and transport estimates under a
temporary cap. It reduces (N-cap) to a uniform coefficient bound for
reference raw Euler programs. A fresh-query estimate proves a cap for
the reference physical-clock Euler programs; differentiated consistency
transfers it to reference raw Euler. A second causal induction then
transfers that raw reference cap to all nearby finite laws. All constants
are finite; no useful numerical lower bound on \(\rho\) is asserted.

###### 1. Exact source equations and construction order

Set

\[
 m_{ka}=h_kp_a,\qquad \gamma_{ka}=-2m_{ka}r_{ka}.
\]

Use \(H^{(1)}_{ka}=\phi(w_k\cdot u_a)\), \(Z^{(2)}_{ka}=A_kH^{(1)}_{ka}\),
\(H^{(2)}_{ka}=\phi(Z^{(2)}_{ka})\), \(\Delta^{(2)}_{ka}=c_k\phi'(Z^{(2)}_{ka})\), and
\(Q_{ka}=A_k^*\Delta^{(2)}_{ka}\). A subscript ku denotes an arbitrary passive
query at the current node. The exact Euler updates are

\[
 \begin{split}
 w_{k+1}&=w_k+\sum_a\gamma_{ka}\phi'(w_k\cdot u_a)Q_{ka}u_a,\\
 c_{k+1}&=c_k+\sum_a\gamma_{ka}\phi(Z^{(2)}_{ka}),\\
 K_{k+1}&=K_k+\sum_a\gamma_{ka}\Delta^{(2)}_{ka}\otimes H^{(1)}_{ka}.
 \end{split}                                                   \tag{N2}
\]

The two centered Gaussian orientation families are \(\xi\) on population 2
and \(\zeta\) on population 1. Their exact
source covariances are

\[
 \mathbb E_2[\xi_{ka}\xi_{sb}]=\mathbb E_1[H^{(1)}_{ka}H^{(1)}_{sb}],\qquad
 \mathbb E_1[\zeta_{ka}\zeta_{sb}]=\mathbb E_2[\Delta^{(2)}_{ka}\Delta^{(2)}_{sb}].                  \tag{N3}
\]

The orientation families are independent; the lower population uses \(g\)
and \(\zeta\), and the upper population uses \(\xi\). Within each family, times and inputs
need not be independent. Singular covariance is allowed. The two populations
are not paired finite-neuron coordinates.

With all deterministic objects frozen as above, define

\[
 \alpha_{ka,sb}=\mathbb E_1[\partial_{\zeta_{sb}}H^{(1)}_{ka}]\quad(s<k),\qquad
 \beta_{ka,sb}=\mathbb E_2[\partial_{\xi_{sb}}\Delta^{(2)}_{ka}]\quad(s\le k).
 \tag{N4}
\]

Specializing C.2 (6)–(11), with unit initialized variance and unit mobilities, gives

\[
 \begin{split}
 F_{ka,sb}&=\alpha_{ka,sb}+\gamma_{sb}\mathbb E_1[H^{(1)}_{ka}H^{(1)}_{sb}],\quad s<k,\\
 D_{ka,sb}&=\beta_{ka,sb}
              +\mathbf1_{s<k}\gamma_{sb}\mathbb E_2[\Delta^{(2)}_{ka}\Delta^{(2)}_{sb}],\\
 Z^{(2)}_{ka}&=\xi_{ka}+\sum_{s<k,b}F_{ka,sb}\Delta^{(2)}_{sb},\\
 Q_{ka}&=\zeta_{ka}+\sum_{s\le k,b}D_{ka,sb}H^{(1)}_{sb}.
 \end{split}                                                   \tag{N5}
\]

Here \(F,D\) are scalar coefficient arrays representing the displayed
answers of the retained action \(A\) and its actual adjoint \(A^*\).
All current forward calls precede the current reverse calls. In particular

\[
 \beta_{ka,kb}=\mathbf1_{a=b}\mathbb E_2[c_k \phi''(Z^{(2)}_{ka})].                  \tag{N6}
\]

For a freshly appended passive query replace the right side by its one
distinguished current slot. The current \(c,w\) use only earlier steps;
current \(Z^{(2)}\) has only its own direct current \(\xi\). This proves (N6), including at a
singular or duplicated query. There is no sum of unweighted current
coefficients over all the other inputs.

For a fixed past backward pulse \(p=(s,b)\), put
\(v_{k;p}=\partial_{\zeta_p}w_k\). It is zero for \(k\le s\). Differentiating (N2)
and (N5) gives exactly

\[
 \begin{split}
 v_{k+1;p}=v_{k;p}+\sum_a\gamma_{ka}u_a\bigg[
 &\phi''(w_k\cdot u_a)Q_{ka}(u_a\cdot v_{k;p})\\
 &+\phi'(w_k\cdot u_a)\bigg\{\mathbf1_{(k,a)=p}
       +\sum_{q\le k}D_{ka,q}\phi'(w_{t(q)}\cdot u_q)
                         (u_q\cdot v_{t(q);p})\bigg\}\bigg],\\
 \alpha_{ku,p}&=\mathbb E_1[\phi'(w_k\cdot u)\,u\cdot v_{k;p}].
 \end{split}                                                   \tag{N7}
\]

The notation \(q\le k\) sums named training slots through time \(k\);
\(t(q)\) is the time index of the slot, and \(u_q\) is its input.
The direct pulse at step \(s\) has magnitude at most \(2R_0m_p\);
this is where both its atom mass and its step enter.

For an upper forward pulse \(p\), define

\[
 U_{ku;p}=\partial_{\xi_p}Z^{(2)}_{ku},\quad
 C_{k;p}=\partial_{\xi_p}c_k,\quad
 V_{ku;p}=\partial_{\xi_p}\Delta^{(2)}_{ku}.
\]

The exact upper equations are

\[
 \begin{split}
 C_{k;p}&=\sum_{q<k}\gamma_q \phi'(Z^{(2)}_q)U_{q;p},\\
 U_{ku;p}&=\mathbf1_{(k,u)=p}+\sum_{q<k}F_{ku,q}V_{q;p},\\
 V_{ku;p}&=\phi'(Z^{(2)}_{ku})C_{k;p}+c_k \phi''(Z^{(2)}_{ku})U_{ku;p},\\
 \beta_{ku,p}&=\mathbb E_2V_{ku;p}.
 \end{split}                                                   \tag{N8}
\]

These are finite causal derivative equations, not a derivative of an
ambient \(L^2\) vector field. No covariance, contraction, residual, \(\alpha\), or
\(\beta\) is differentiated.

Every fixed finite graph is defined before a uniform cap is sought.
Chronological construction gives a finite Gaussian innovation list;
Q is a Gaussian plus finitely many bounded first features with already
finite coefficients. Lower source derivatives at the next instruction
have a finite polynomial envelope in that finite Gaussian list, and the
bounded upper gates/readout preserve their finite moments. This inductive
argument supplies the finite coefficients in (N4), even on a long graph;
it asserts no bound uniform in its number of instructions.

###### 2. Consequences of a temporary backward coefficient cap

The following bounds are useful without assuming an infinite-horizon
bootstrap. They hold for every prefix on which the already constructed
backward rows have a specified cap B. At a new node the lower estimates
use only past rows; the upper estimates then construct the current row.

For all raw Euler programs through T, independently of a coefficient cap,

\[
 \|c_k\|_\infty\le C_0:=Y(e^{2T}-1),\qquad |r_{ka}|\le R_0:=Y+C_0.
 \tag{N9}
\]

Indeed \(\|c_{k+1}\|_\infty\le(1+2h_k)\|c_k\|_\infty+2h_kY\), since
\(|\phi|\le1\) and \(|f|\le\|c\|_2\le\|c\|_\infty\); the product bound
\(\prod_k(1+2h_k)\le e^{2T}\) proves (N9). Together with (NE), this bounds the raw row, Hilbert–Schmidt increment,
action norm, and raw speed on every prefix, without a coefficient cap.

Suppose the \(\beta\) row cap is B. Define

\[
 D_0=B+2R_0C_0^2T.
\]

Then (N5) gives \(\sum_q|D_{ku,q}|\le D_0\), and hence

\[
 Q_{ku}=\zeta_{ku}+J_{ku},\qquad |J_{ku}|\le D_0,
 \qquad \mathbb E_1\zeta_{ku}^2\le C_0^2.                                \tag{N10}
\]

The J in this display includes both response and learned contributions.
For every \(\lambda\ge0\) and every prefix,

\[
 \mathbb E_1\exp\left(\lambda\sum_{j<k,a}h_jp_a|Q_{ja}|\right)
 \le 2\exp\{\lambda TD_0+\lambda^2T^2C_0^2/2\}.                 \tag{N11}
\]

To verify this, use (N10), the scalar bound
\(\mathbb E e^{\lambda|G|}\le2e^{\lambda^2\operatorname{Var}(G)/2}\), and Jensen with weights
\(h_jp_a/\sum_{i<k}h_i\). No temporal or input independence and no maximum of
a Gaussian history is used.

Put \(M_{k;p}=\max_{s<j\le k}|v_{j;p}|\). Since \(|\phi'|\le1\), \(|\phi''|\le2\), (N7)
and discrete Gronwall give

\[
 {M_{k;p}\over m_p}
 \le2R_0\exp\left\{2R_0D_0T+
                      4R_0\sum_{j<k,a}h_jp_a|Q_{ja}|\right\}.
 \tag{N12}
\]

The direct source appears only once, at time s; every later term is
bounded by \(2R_0h_j(D_0+2\sum_a p_a|Q_{ja}|)M_{j;p}\). Iterating this
scalar inequality proves (N12). Thus, for each \(p\ge1\),

\[
 \|M_{k;p_0}/m_{p_0}\|_{L^p}
 \le L_p(B):=4R_0\exp\{6R_0D_0T+8R_0^2pT^2C_0^2\}.                 \tag{N13}
\]

Here \(p_0\) denotes the slot and p the moment order. In particular

\[
 |\alpha_{ku,sb}|\le A_B h_sp_b,\qquad
 |F_{ku,sb}|\le f_Bh_sp_b,\quad
 A_B=L_1(B),\quad f_B=A_B+2R_0.                                \tag{N14}
\]

There is also a **past-source density bound for \(\beta\)**, stronger than its
row bound for handling law transport. Put \(d_0=2R_0T+2C_0\). From (N8), the
full derivative row sum of c is at most
\(2R_0\sum_{j<k}h_j\mathcal U_j\), where
\(\mathcal U_j=\max_{i\le j,a}\sum_p|U_{ia;p}|\). Hence the row sum of V is at most
\(d_0\mathcal U_k\), and

\[
 \mathcal U_k\le1+f_Bd_0\sum_{j<k}h_j\mathcal U_j
       \le e^{f_Bd_0T}.                                    \tag{N15}
\]

These inequalities hold pointwise. Consequently

\[
 \sum_{p\le k}|\beta_{ku,p}|\le d_0e^{f_Bd_0T}.              \tag{N16}
\]

For completeness fix a single past forward slot \(p_0=(s,b)\). At time s
only \(U_{sb;p_0}=1\) is nonzero, so only \(V_{sb;p_0}=c_s\phi''(Z^{(2)}_{sb})\) is
nonzero and its magnitude is at most \(2C_0\). For k>s, (N8) then yields

\[
 |C_{k;p_0}|\le2R_0m_{p_0}
       +2R_0\sum_{s<j<k}h_j\max_a|U_{ja;p_0}|,
\]
\[
 \max_a|U_{ka;p_0}|
 \le f_Bd_0m_{p_0}
       +f_Bd_0\sum_{s<j<k}h_j\max_a|U_{ja;p_0}|.
\]

In the second inequality the c-memory double sum is bounded by T times
the single sum. Thus

\[
 |\beta_{ku,sb}|\le b_Bh_sp_b\quad(s<k),\qquad
 b_B=2R_0+d_0^2f_Be^{f_Bd_0T},\qquad
 |\beta_{ku,ku}|\le2C_0.                                     \tag{N17}
\]

All constants in (N10)--(N17) are independent of the number of atoms,
minimum atom weight, number of steps, and covariance rank. The equations
also give, for each fixed finite p,

\[
 \|\sup_{j\le k}|w_j|\|_{L^p}+\sup_{j,a}\|Q_{ja}\|_{L^p}
       +\sup_{j,a}\|Z^{(2)}_{ja}\|_{L^p}\le C_{B,p}.               \tag{N18}
\]

For \(w\) use its accumulated update, (N10), and Minkowski with weights
\(h_jp_a\). For \(Z^{(2)}\) use \(|\Delta^{(2)}|\le C_0\), (N14), and the forward innovation of
variance at most one. This does not claim a moment bound for a supremum
of \(Q\) or \(Z^{(2)}\) over all times and inputs. All higher moments here
come from named-field decompositions and source recursions; actions and
adjoints are used only with their stated \(L^2\) bounds.

The absolute estimates alone do not continue the C.2 cap to T. For example
they offer only the sufficient inequality

\[
 B\ \ge\ \Psi_T(B):=d_0\exp\{d_0T(L_1(B)+2R_0)\}.             \tag{N19}
\]

With the overestimates (N9) at T=40 the right side already grows faster
than B with a larger positive value at zero; (N19) cannot select a cap.
This is a failure of this absolute estimate, not a demonstration that
the actual coefficients diverge.

###### 3. Weighted law transport of the coefficients

Assume temporarily that some \(h_*>0\) and \(B_*<\infty\) bound
\(\mathcal B_k\le B_*\) for every two-atom reference raw Euler program
through \(T\) with \(h_{\max}\le h_*\). The reference clock argument
below will prove this bound. We first prove its implication for nearby laws,
retaining all source weights and comparing the same passive input.

Take a finite optimal coupling of a finite \(\lambda\) and the two-atom
reference. Split atoms according to its nonzero pairs and write it as
\(p_a,(u_a,y_a),(v_a,z_a)\). Then

\[
 q=\mathcal W_1(\lambda,\nu_*)=\sum_ap_ae_a,\qquad
 e_a=|u_a-v_a|+|y_a-z_a|.                                   \tag{N20}
\]

Both programs now have the same source names and masses. Splitting a
reference atom does not enlarge its \(\beta\) row cap: for every old slot,
its \(\alpha\), F, and \(\beta\) coefficients split in proportion to the new atom
mass, while the current coefficient remains its one distinguished direct
coefficient (N6). To check this claim, the lower pulse in (N7) is linear in
its initial \(\gamma_{sb}\) and identical repeated reference queries have
identical scalar values. Its normalized derivative is therefore unchanged
by splitting. Equation (N5) then splits F in the same proportion. The
single upper pulse equations (N8), starting with its one current impulse,
split every later coefficient in that proportion as well. Induction in
time proves the claim. Zero coupling weights are discarded.

Run both programs on the same mesh and on their joint Gaussian-source
realization. Theorem III.F.1, the source rule (III.F.9)–(III.F.10), and the
fixed neural-product extension A.2, applied to their finite union
gives, for matched slots,

\[
 \|\xi_i-\bar\xi_i\|_{L^p}
      =\|N(0,1)\|_{L^p}\|H^{(1)}_i-\bar H^{(1)}_i\|_2,
\quad
 \|\zeta_i-\bar\zeta_i\|_{L^p}
      =\|N(0,1)\|_{L^p}\|\Delta^{(2)}_i-\bar\Delta^{(2)}_i\|_2.          \tag{N21}
\]

Indeed the cross covariances are the corresponding cross contractions;
subtracting them gives the squared source difference in (N21). This is a
coupling by the source covariance rule, not a Lipschitz claim for an
arbitrary matrix square root or an inverse Gram matrix.

Write \(\mathrm d V=V-\bar V\) for a comparison difference, and let
\(\eta\) bound the maximum raw distance between the two programs through
the prefix. The elementary forward/action subtractions on their common
ball give

\[
 |r_{ka}-\bar r_{ka}|
 +\|H^{(1)}_{ka}-\bar H^{(1)}_{ka}\|_2+\|Z^{(2)}_{ka}-\bar Z^{(2)}_{ka}\|_2
 +\|\Delta^{(2)}_{ka}-\bar\Delta^{(2)}_{ka}\|_2+\|Q_{ka}-\bar Q_{ka}\|_2
 \le C(\eta+e_a),
\]
\[
 |\gamma_{ka}-\bar\gamma_{ka}|
                  \le C h_kp_a(\eta+e_a).                  \tag{N22}
\]

For Q subtract \(A^*\Delta^{(2)}\) directly; c is uniformly bounded pointwise,
so the upper gate difference is \(L^2\) Lipschitz. No first-layer multiplier
occurs in Q itself. At the same passive input u replace \(e_a\) by zero.

Define the coefficient discrepancy at a common passive query by

\[
 E_k=\sup_u\left\{|\beta_{ku,ku}-\bar\beta_{ku,ku}|
          +\sum_{s<k,b}|\beta_{ku,sb}-\bar\beta_{ku,sb}|\right\}.
 \tag{N23}
\]

The current slots are paired as distinguished query slots. Earlier
training slots use the coupling (N20). Comparing the current coefficient
of a far contaminant with a reference *axis* current coefficient would
give an O(1) difference even at arbitrarily small contamination mass.
The same-passive-input convention in (N23) avoids that invalid norm.

Here is the quantitative comparison needed for the bootstrap. If both
programs' previously constructed \(\beta\) rows are at most B, then

\[
 E_k\le C_B\left\{(\eta+q)^{1/16}
                              +\sum_{j<k}h_jE_j\right\}.
 \tag{N24}
\]

Constants can be enlarged to cover \(\eta+q\ge1\); only its approach to zero
matters. The current bound in (N24) uses only past nearby-law \(\beta\) caps.
The rest of this section gives the derivative estimates proving (N24).

First, within either capped program the \(\beta\) row is Lipschitz in its
current passive input, with a constant depending only on B. For \(\alpha\),
differentiate only the displayed input in (N7), or use the mean-value
bound
\(|\phi'(w\cdot u)u-\phi'(w\cdot v)v|\le C(1+|w|)|u-v|\) and (N13). This gives
\(|\alpha_{ku,p}-\alpha_{kv,p}|\le C_Bm_p|u-v|\).
The same estimate holds for F by its contraction formula. For the
upper rows, all past V and the row C are identical at the two passive
queries. In (N8), the past part of U differs by at most
\(\sum_p|F_{ku,p}-F_{kv,p}|\sum_l|V_{p;l}|\), which is bounded by
\(C_B|u-v|\) using (N15). The current \(\phi'(Z^{(2)}),\phi''(Z^{(2)})\) factors differ in \(L^2\) by
\(C\|Z^{(2)}(u)-Z^{(2)}(v)\|_2\le C_B|u-v|\); tanh has bounded third derivative.
Multiplying by the pointwise derivative row bound (N15) proves the
asserted \(\beta\) row bound. Thus a matched active-output row costs at most
\(E_k+C_Be_a\), in addition to the learned contraction discrepancy in
(N22).

Second, subtraction of (N7) has a causal linear propagation part using
the nearby-law coefficients and a source part. The propagation coefficient
for the maximum norm of a pulse difference is bounded by

\[
 2R_0h_k\left(D_0+2\sum_ap_a|Q_{ka}|\right).                 \tag{N25}
\]

The source part consists exactly of the differences of \(\gamma\), the two
input vectors, the gates \(\phi',\phi''\), \(Q\), and \(D\), each multiplied by an
unchanged reference pulse. In particular there is no derivative of D in
this subtraction. The D difference is

\[
 \mathrm d  D_{i,p}=\mathrm d \beta_{i,p}
 +\mathbf1_{t(p)<t(i)}\left[
  \mathrm d \gamma_p \mathbb E_2[\bar\Delta^{(2)}_i\bar\Delta^{(2)}_p]
       +\gamma_p\mathrm d  \mathbb E_2[\Delta^{(2)}_i\Delta^{(2)}_p]\right],          \tag{N26}
\]

where unbarred \(\gamma\) is used in the second term. This also verifies that
learned-memory errors retain \(m_p\).

All unchanged normalized pulses have every fixed finite moment by (N13).
Gate and field differences needed in the source part have an \(L^{12}\) bound
\(C_B(\eta+e_a)^{1/16}\). For bounded gates interpolate the \(L^2\) bound (N22)
with their pointwise bound. For w or Q interpolate their \(L^2\) difference
with the uniform \(L^{24}\) bounds (N18); interpolation gives exponent 1/11,
which implies the weaker displayed exponent on a bounded distance range.
For the input factors themselves use \(|u_a-v_a|\le e_a\).
Products of up to three factors are bounded in \(L^4\) by Hölder with \(L^{12}\)
norms. The random integrating factor obtained from (N25) has every fixed
moment by (N11); Cauchy--Schwarz bounds its product with each forcing
term. Minkowski sums the time/atom masses. Discrete Gronwall therefore
gives, for every past pulse p=(s,b),

\[
 {\|\max_{j\le k}|v_{j;p}-\bar v_{j;p}|\|_2\over m_p}
 \le C_B\left\{(\eta+e_b)^{1/16}+q^{1/16}
                              +\sum_{j<k}h_jE_j\right\}.   \tag{N27}
\]

One way to verify the averaging in this estimate is to retain each
\(e_a^{1/16}\) until the last step and use
\(\sum_ap_ae_a^{1/16}\le q^{1/16}\). The direct pulse uses (N22) and has
the same factor \(m_p\); dividing by it does not leave \(1/p_b\).
In the D term, its row variation multiplies the reference maximum pulse
norm from (N13); its active-output discrepancy is bounded just above.
There is also a term in which D is unchanged and a *past source's* gate
or input changes. This is where (N17) is essential: its old-source
coefficient satisfies \(|D_{ka,sb}|\le C_Bh_sp_b\), so

\[
 \sum_{s<k,b}|D_{ka,sb}|e_b^{1/16}
             \le C_BT\sum_bp_be_b^{1/16}\le C_BTq^{1/16}.
 \tag{N27a}
\]

The one current coefficient costs \(C_Be_a^{1/16}\) and is averaged
with the outside update weight \(p_a\). A row bound without the past-source
density bound would not justify this step.
These account for every term from the two sums in (N7). No
maximum of the \(e_a\) and no unweighted sum over source indices is taken.

By the second line of (N7), (N27), and Hölder for the difference of its
outside gate, at a common passive input

\[
 \sum_{p<k}|\mathrm d \alpha_{ku,p}|
 \le C_B\left\{(\eta+q)^{1/16}
                              +\sum_{j<k}h_jE_j\right\}.   \tag{N28}
\]

Here \(\sum_{p<k}m_p\le T\); the contribution depending on the source
\(e_b\) averages as in (N27). The identical estimate holds for the F-row
difference by (N5) and (N22). For a matched active output add
\(C_Be_a\) using the passive-input estimate. Entrywise versions keep the
factor \(m_p\) and its \(e_b\) term.

For a current output slot \(i=(k,u)\), write \(q<i\) for
\(t(q)<k\); the symbols \(k,i\) in the next display have this relation.
The exact upper differences are

\[
 \begin{split}
 \mathrm d  U_{i;p}
    &=\sum_{q<i}\mathrm d  F_{i,q}\bar V_{q;p}
                       +\sum_{q<i}F_{i,q}\mathrm d  V_{q;p},\\
 \mathrm d  C_{k;p}
    &=\sum_{q<k}\{\mathrm d \gamma_q \phi'(\bar Z^{(2)}_q)\bar U_{q;p}
             +\gamma_q\mathrm d  \phi'(Z^{(2)}_q)\bar U_{q;p}
             +\gamma_q \phi'(Z^{(2)}_q)\mathrm d  U_{q;p}\},\\
 \mathrm d  V_{i;p}
    &=\phi'(Z^{(2)}_i)\mathrm d  C_{k;p}+\mathrm d  \phi'(Z^{(2)}_i)\bar C_{k;p}
          +c_k\phi''(Z^{(2)}_i)\mathrm d  U_{i;p}
          +\{\mathrm d  c_k \phi''(\bar Z^{(2)}_i)+c_k\mathrm d  \phi''(Z^{(2)}_i)\}
                                                        \bar U_{i;p}.
 \end{split}                                               \tag{N29}
\]

The direct U impulses cancel after pairing the distinguished current
slots. To keep output errors weighted, set

\[
 G_k=(\eta+q)^{1/16}+\sum_{j<k}h_jE_j,\qquad
 L_k=\sum_ap_a\left\|\sum_p|\mathrm d  V_{ka;p}|\right\|_2.
\]

Every barred upper derivative row is bounded pointwise by (N15).
The F propagation coefficients have density \(f_Bh_jp_a\), and \(\gamma\)
retains its original mass. Summing (N29) over source indices, taking \(L^2\),
then averaging its active output index gives

\[
 L_k\le C_BG_k+C_B\sum_{j<k}h_jL_j.                         \tag{N29a}
\]

In this estimate the F-row forcing at a matched active output is at most
\(C_B(G_k+e_a)\) by (N28); the field factors at that output cost
\(C_B(\eta+e_a)\) by (N22). Both are averaged with \(p_a\). In the C-row,
which does not depend on the output query, the same factors are already
multiplied by \(h_jp_a\). These are all appearances of an output transport
cost in (N29). Since \(G_k\) is nondecreasing, discrete Gronwall yields
\(L_k\le C_BG_k\) after increasing \(C_B\). For a common passive output there
is no \(e_a\) term, and the same equations give

\[
 \left\|\sum_p|\mathrm d  V_{ku;p}|\right\|_2
                 \le C_BG_k+C_B\sum_{j<k}h_jL_j\le C_BG_k.
 \tag{N29b}
\]

Taking expected absolute values proves (N24). The current diagonal
contributes at most \(C\eta\) directly from (N6). There is no current
unknown \(E_k\) on the right: (N28) uses only earlier lower updates, and all
upper memory terms in (N29) are strictly earlier. No supremum over the
matched active-output costs \(e_a\) was used.

The raw discrepancy \(\eta\) used above is available before the
reference raw coefficient bound has been proved. The raw bound (NE), the Hilbert–Schmidt transport estimate (NC), and
the actual reference tails of C.4.5.2 (R17)–(R18) give, for every finite
raw Euler program with training law \(\lambda\),

\[
 \sup_{k:t_k\le T}d_{\rm raw,1}(\theta_{\lambda,k},\theta_*(t_k))
       \le \omega_T(q+h_{\max}),\qquad \omega_T(s)\to0.     \tag{N30}
\]

To see the mesh term, interpolate the Euler path affinely; its speed is
uniformly bounded by the crude raw ball. Apply the transport estimate
with the actual reference as its tail-bearing endpoint. The distance
from the interpolated Euler state to its left endpoint is at most
\(V_Th_{\max}\), so the cutoff inequality acquires
\(C(1+R_{\rm cut})h_{\max}\). Integrating gives
\(C e^{CR_{\rm cut}}\{(1+R_{\rm cut})(q+h_{\max})+e^{-cR_{\rm cut}^2}\}\). Taking the cutoff to be a sufficiently large constant times
\(\sqrt{\log(e/(q+h_{\max}))}\) proves (N30) for small
\(q+h_{\max}>0\); define the modulus to be zero at zero and enlarge
it using the common raw bound outside that range. This is a comparison to one
existing flow, not a construction of a changed-law flow.
Applying (N30) to \(\lambda\) and to the reference raw Euler program gives a
valid \(\eta\) tending to zero with \(q+h_{\max}\) in (N24).

Assume the reference raw coefficient bound stated at the start of this part. Its reference Euler Q tails are Gaussian by (N10).
For the two raw programs on the **same** mesh, the transport estimate
therefore gives, at a fixed cutoff \(R_{\rm cut}\), the recurrence

\[
 d_{k+1}\le[1+Ch_k(1+R_{\rm cut})]d_k
          +Ch_k\{(1+R_{\rm cut})q+e^{-cR_{\rm cut}^2}\}.
\]

Both start at the same state. Iteration and cutoff choice give

\[
 \sup_k d_k\le\Phi_{B_*}(q),\qquad
 \Phi_{B_*}(q)\longrightarrow0\quad(q\downarrow0),          \tag{N30a}
\]

uniformly over admitted meshes; there is no mesh defect in this
comparison. One can take \(\Phi(q)=Cq e^{C\sqrt{\log(e/q)}}\) for small q
after enlarging constants. The crude ball for the nearby program
suffices; only the reference endpoint of the transport estimate
requires tails.

Set \(B=B_*+1\) and use its invariant duplication property.
At the first potential failed row, all prior nearby-law rows are at
most B. Estimates (N10)--(N29) apply in their causal order. Discrete
Gronwall in (N24) gives

\[
 E_k\le C_B e^{C_BT}
                 \{\Phi_{B_*}(q)+q\}^{1/16}.                \tag{N31}
\]

Choose positive \(\rho\) small enough that the right side is at most 1/2
whenever \(q<\rho\), and put \(h_0=h_*\).
The current row is then at most \(B_*+1/2<B\), contradicting first failure.
The zero-readout initialization has \(\beta=0\), so induction starts.
This proves (N-cap), conditional on that reference bound.
Formula (N10) gives a uniform Gaussian marginal tail for every passive
\(Q\), and (N9) controls the readout. This argument has not inferred
convergence of changed-law paths from their fixed positive proximity to
the reference.

More explicitly, once the cap is fixed, \(Q=G+J\), \(\operatorname{Var}(G)\le C_0^2\),
\(|J|\le D_0\). For \(R_{\rm cut}\ge2D_0\), the event \(|Q|>R_{\rm cut}\) implies
\(|G|>R_{\rm cut}/2\). Integrating the scalar Gaussian tail and absorbing its
polynomial prefactor gives \(\tau_{R_{\rm cut}}(Q)\le M e^{-aR_{\rm cut}^2}\) with finite
positive a,M depending only on the fixed caps. Enlarge M to cover the
remaining \(R_{\rm cut}\ge1\) and the bounded readout. Averaging these individual tail bounds over any admitted training law
preserves the same constants, as does restriction to a smaller radius. A state
on an affine Euler segment is obtained by appending one shorter final
step; the same bound applies to its recomputed fields. This is a
marginal-in-time statement, not an exponential bound for a path maximum.

###### 4. Raw-to-clock mesh errors and their named derivatives

The clock change is exact for continuous reference flow. Its raw Euler
defect and the named derivatives of that defect must still be summed;
the following bounds do so under the temporary cap.

Let

\[
 \mathcal F(w)=w/2+\sinh(2w)/4,\quad \mathcal F'(w)=1/\phi'(w),
\quad R_h(w,b_0)=\mathcal F(w+hb_0\phi'(w))-\mathcal F(w)-hb_0.
\]

Here \(b_0\) is a scalar velocity coefficient.
Put \(\vartheta=hb_0\phi'(w)\). Taylor's integral identity gives

\[
 R_h=h^2b_0^2\phi'(w)^2
                \int_0^1(1-s)\mathcal F''(w+s\vartheta)\,ds.
 \tag{N32}
\]

The elementary hyperbolic identities imply

\[
 \phi'(w)^2|\mathcal F''(w+z)|\le2e^{2|z|},\qquad
 \phi'(w)^2|\mathcal F'''(w+z)|\le4e^{2|z|},\qquad |\phi''|\le2\phi'.
\]

For example \(|\sinh(2(w+z))|\le e^{2|z|}\cosh(2w)\) and
\(\phi'(w)^2\cosh(2w)\le2\); the bound for the third derivative follows in
the same way. Differentiating the explicit integral (N32), rather than
separately estimating the large terms before cancellation, yields

\[
 |R_h|\le Ch^2 b_0^2e^{2h|b_0|},
\]
\[
 |\partial_wR_h|\le Ch^2b_0^2(1+h|b_0|)e^{2h|b_0|},\qquad
 |\partial_{b_0}R_h|\le Ch^2|b_0|(1+h|b_0|)e^{2h|b_0|}.
 \tag{N33}
\]

Every named derivative consequently obeys

\[
 |\partial_p R_h|
 \le Ch^2e^{2h|b_0|}(1+h|b_0|)
                \{b_0^2|\partial_p w|+|b_0||\partial_p b_0|\}.
 \tag{N34}
\]

On the reference, including any split representation, the row-coordinate
update has precisely this form with

\[
 b_{0,a,k}=-2\sum_{j:v_j=e_a}p_jr_{kj}Q_{kj}.
 \tag{N35}
\]

Under the temporary cap its scalar marginals have uniformly bounded
Gaussian norms, by (N10) and the total atom mass. Formula (N11) or the
scalar Gaussian exponential moment controls the factor in (N33)--(N34).
Therefore \(\sum_k\|R_{h_k}\|_{L^p}\le C_{B,p}h_{\max}\) for every fixed finite p.

For a backward source \(p_0\)=(s,j), at the direct injection step
\(|\partial_{p_0}b_0|\le2R_0p_j\) and \(\partial_{p_0}w_s=0\).
Dividing that step's estimate (N34) by \(m_{p_0}=h_sp_j\) costs at most
\(C_{B,p}h_s\). At every later step, (N7), (N13), and the D-row cap give

\[
 \|\partial_{p_0}w_k/m_{p_0}\|_{L^p}
 +\|\partial_{p_0}b_{0,a,k}/m_{p_0}\|_{L^p}\le C_{B,p}.
\]

Using Hölder in (N34) and \(\sum_kh_k^2\le Th_{\max}\) now proves

\[
 {1\over m_{p_0}}\sum_{k\ge s}
               \|\partial_{p_0}R_{h_k}\|_{L^p}
                                  \le C_{B,p}h_{\max}.     \tag{N36}
\]

This proves summability of the named backward-pulse clock defect with
its correct mass normalization. A local lower-population function is
independent of the upper \(\xi\) slots when deterministic coefficients are
frozen; there is no additional \(\xi\) derivative of its clock defect.
The c/K updates are the same in raw and clock formulations.

###### 5. The physical reference source anchor and its transfer

**The reference clock coefficient bound.**

Use the two reference clocks \(X_a=\mathcal F(w_a)-\mathcal F(g_a)\) and the scalar solution
\(w_a=J(X_a,g_a)\) of \(J_X=\operatorname{sech}^2J\), \(J(0,g)=g\). Thus
\(|J_X|\le1\). Its active first features have \(|\partial_X\phi(J)|=\operatorname{sech}^4J\le1\).
The physical reference clock equations are

\[
 \dot X_a=-r_aQ_a,\qquad
 \dot K=-\sum_{a=1}^2r_a\Delta^{(2)}_a\otimes H^{(1)}_a,\qquad
 \dot c=-\sum_{a=1}^2r_aH^{(2)}_a.                                \tag{N37}
\]

Their raw fields are the reference flow of C.4.5.1 (R4)–(R8).
The factor \(-r_a\) in (N37) is \(-2p_ar_a\) with \(p_a=1/2\).
On the common
carrier these equations are Lipschitz on the bounded sets used below,
by the explicit subtractions that follow; Euler convergence here needs
no raw first-gate estimate.

For the auxiliary source extraction use finite initialized matrices
with \(\|A_0\|_{\rm op}\le10\) and **zero readout**. This auxiliary fixed program identifies the zero-readout population
coefficients. The actual finite-network initialization in the theorem
retains its specified random readout. In the finite calculation every
field norm is \(\|v_n\|_2/\sqrt n\), and the increment norm is the
ordinary Frobenius norm \(\|K_n\|_F\). These are the finite versions of
population \(L^2\) and Hilbert–Schmidt norms by III.F.8
(III.F.28)–(III.F.31). By (N9) and bounded activations, at all nodes,

\[
 \|c_k\|_\infty\le C_0,\quad |r_{ka}|\le R_0,\quad
 \|K_k\|_{HS}\le2TR_0C_0,\quad \|A_k\|_{op}\le M:=10+2TR_0C_0.
 \tag{N38}
\]

These bounds also hold if a fresh root is added to one forward or
reverse query and all descendants, including residuals, are recomputed.
Forward tanh and its gate remain bounded, so every subsequent c and K
increment obeys the same estimate. Reverse forcing changes only the
clock increment directly. Thus there is no assumption that a forced
program retains a gradient-flow energy identity.

For two unforced subsequent clock states on this ball set
\(x=\sum_a\|\mathrm d  X_a\|_2\), \(\varkappa=\|\mathrm d  K\|_{\rm HS}\), \(z=\|\mathrm d  c\|_2\),
and \(d=x+\varkappa+z\). The same-root scalar bound for J gives

\[
 \begin{split}
 \sum_a\|\mathrm d  H^{(1)}_a\|_2&\le x,\qquad
 V:=\sum_a\|\mathrm d  Z^{(2)}_a\|_2\le Mx+2\varkappa,\\
 D:=\sum_a\|\mathrm d \Delta^{(2)}_a\|_2&\le2z+2C_0V,\qquad
 P:=\sum_a\|\mathrm d  Q_a\|_2\le MD+2C_0\varkappa,\\
 S:=\sum_a|\mathrm d  r_a|&\le2z+C_0V.
 \end{split}                                               \tag{N39}
\]

The three velocity differences in (N37) are at most

\[
 MC_0 S+R_0P,\qquad C_0S+R_0(D+C_0x),\qquad S+R_0V.                    \tag{N40}
\]

For example subtract \(r\Delta^{(2)}\otimes H^{(1)}\) into its residual, upper
field, and lower feature differences; the rank norm is the product of
its \(L^2\) factors. Equations (N39)--(N40) give a bound \(Ld\) with the fixed
overestimate

\[
 L=100(1+M+C_0+R_0)^4,
 \qquad E=\exp(LT).                                        \tag{N41}
\]

Hence any post-pulse Euler difference is amplified by at most E,
independently of width, step count, and step sizes. Splitting an atom
retains these equations after summing its identical descendants.

Insert \(\varepsilon e\), with \(e\) a fresh standard Gaussian root of
the answer's population, into the complete reverse answer at slot \((s,b)\).
Its only immediate state change is in the clock corresponding to
\(v_b=e_a\), with norm at most

\[
 2R_0 h_sp_b|\varepsilon|\|e\|_2.                               \tag{N42}
\]

For a passive first feature
\(H^{(1)}(u)=\phi(u_1J(X_1,g_1)+u_2J(X_2,g_2))\), the difference is at most x.
The subsequent passive feature difference is therefore bounded by
\(2R_0Eh_sp_b|\varepsilon|\|e\|_2\).

Instead insert the root into one complete forward answer \(Z^{(2)}_{sb}\).
At that node its activation, \(\Delta^{(2)}\), residual, and reverse answer change
by at most, respectively,

\[
 |\varepsilon|\|e\|_2,\quad 2C_0|\varepsilon|\|e\|_2,\quad
 C_0|\varepsilon|\|e\|_2,\quad 2MC_0|\varepsilon|\|e\|_2.
\]

Use the old Q and the bounded new residual when subtracting the clock
update. The three immediate state increments have total norm at most
\(P_0h_sp_b|\varepsilon|\|e\|_2\), where

\[
 P_0=2\{MC_0^2+2R_0MC_0+C_0^2+2R_0C_0+C_0+R_0\}.                          \tag{N43}
\]

The terms arise from \(\mathrm d (rQ)\), \(\mathrm d (r\Delta^{(2)}\otimes H^{(1)})\), and
\(\mathrm d (rH^{(2)})\), respectively. A passive later \(\Delta^{(2)}\) satisfies

\[
 \|\mathrm d \Delta^{(2)}(u)\|_2\le z+2C_0(Mx+\varkappa)\le K_0d,
 \qquad K_0=1+2C_0(M+1).                                    \tag{N44}
\]

Thus its post-pulse change is at most
\(P_0K_0Eh_sp_b|\varepsilon|\|e\|_2\).

Extract the named coefficients by the full mechanism of C.4.5.2
(R5)--(R15). Here are the hypotheses and the order of limits needed
for this application. At each fixed graph clip the Gaussian first
roots smoothly. The passive feature's derivatives with respect to X
are bounded uniformly in the root clipping level; its root
derivatives are bounded at each fixed level. A readout clip equal to
the identity on a neighborhood of \([-C_0,C_0]\) is inactive. Thus the
fixed-program theorem and its complete source extension apply to
forced and unforced graphs, including singular covariance and
variance-zero slots. At a fixed graph all source derivatives have a
finite deterministic bound independent of root clipping: the clock
derivatives are bounded, the readout is bounded, and every matrix
answer is a source plus a finite sum with fixed coefficients.
Chronological convergence and this derivative bound remove root
clipping and make all coefficients continuous as \(\varepsilon\) tends to
zero, exactly as proved in C.4.5.2, proof part 2, (R5)–(R7). No mesh-uniform source cap was
used in this fixed-graph step.

Fix the mesh and nonzero \(\varepsilon\) and first let width tend to infinity.
The initialization operator event and \(\|e_n\|_2/\sqrt n\to1\) have
probability tending to one, by III.F.2 (III.F.4) and the Gaussian
second-moment calculation. Theorem III.F.1 and its extension just checked transfer
(N42)--(N44) and their pairing with the fresh Gaussian root. In the
source coordinate expression that root enters only in the specified
slot as \(\mathrm{slot}+\varepsilon e\). The selected residuals and covariance laws
may depend on \(\varepsilon\) but are deterministic, and all Gaussian source
groups are independent of this local new root. Conditional
one-dimensional Gaussian integration by parts therefore gives

\[
 \mathbb E[eV^\varepsilon]=\varepsilon\mathbb E[\partial_{\rm slot}V^\varepsilon].
 \tag{N45}
\]

The expectation in (N45) is in the population of the observed field.
The unforced expression is independent of \(e\). Cauchy--Schwarz in the
joint limit, division by \(|\varepsilon|\), then the fixed-graph
zero-forcing continuity just proved yield

\[
 |\alpha^{\rm cl}_{ku,sb}|\le2R_0Eh_sp_b,
 \qquad |\beta^{\rm cl}_{ku,sb}|\le P_0K_0Eh_sp_b\quad(s<k),
 \qquad |\beta^{\rm cl}_{ku,ku}|\le2C_0.                     \tag{N46}
\]

The argument works for each passive u with the same constants.
Consequently every reference physical clock Euler program through T
has the cap

\[
 B_{\rm cl}=2C_0+TP_0K_0E.                                   \tag{N47}
\]

This proves a bound for the specified named coefficients. It does
not infer a derivative transverse to a singular source support from
the unforced value law. The fresh root and the width-first,
forcing-second order in (N45) are essential.

**Transfer from clock Euler to raw reference Euler.**

Compare the reference raw and clock Euler programs on the same mesh
and common Gaussian source carrier. Write
\(X^r_a=\mathcal F(w^r_a)-\mathcal F(g_a)\) for the transformed raw program and \(X^c\)
for clock Euler. The raw program satisfies the exact clock update
with the extra vector of defects (N32). Its lower first-feature
expression is the same function of X and g as in the clock program.

Define \(E_k\) by (N23) for this raw/clock pair, with no change of data
law, and assume a temporary cap B on all preceding raw \(\beta\) rows.
Let \(\eta_h\) bound the raw discrepancy of their fields. There is an
\(\eta_h\) tending to zero with \(h_{\max}\) independently of that cap: (N30)
compares raw Euler with the actual reference, while (N39)--(N41), the
bounded clock speed, and the integrated Euler error compare clock
Euler with the same reference in clock/HS/\(L^2\) norm. The scalar bound
\(|J_X|\le1\) converts the latter distance to raw distance. In particular
all the field differences in (N22) are \(O(\eta_h)\).

For a backward pulse \(p_0\)=(s,b), put
\(\chi^r_{k;p_0}=\partial_{\zeta_{p_0}}X^r_k\), and define \(\chi^c\) similarly.
For a lower first feature let \(J_q^r\) and \(J_q^c\) denote its two
clock derivatives. Each has norm at most two, and their difference
in \(L^2\) is at most \(C\eta_h\), since each is a product of bounded tanh
gates with bounded derivatives. At reference active slots one can
use the sharper bound one. Differentiating the two clock recursions
gives the exact pair

\[
 \chi^r_{k+1;p_0}=\chi^r_{k;p_0}
   +\sum_a\gamma^r_{ka}v_a\left\{\mathbf1_{(k,a)=p_0}
             +\sum_{q\le k}D^r_{ka,q}J_q^r\chi^r_{t(q);p_0}\right\}
   +\partial_{p_0}R_k,
\]
\[
 \chi^c_{k+1;p_0}=\chi^c_{k;p_0}
   +\sum_a\gamma^c_{ka}v_a\left\{\mathbf1_{(k,a)=p_0}
             +\sum_{q\le k}D^c_{ka,q}J_q^c\chi^c_{t(q);p_0}\right\}.
 \tag{N48}
\]

Here \(v_a\) is the reference axis of that atom, and the lower feature
derivative is a row vector applied to \(\chi\). The clock reference cap
(N47) bounds its D rows by \(D_{\rm cl}=B_{\rm cl}+2R_0C_0^2T\). Since the clock gates
are bounded, its pulses satisfy the **pointwise** bound

\[
 \max_{j\le k}|\chi^c_{j;p_0}|/m_{p_0}
                        \le2R_0\exp(4R_0D_{\rm cl}T).         \tag{N49}
\]

Subtract (N48). Its raw propagation coefficients have a deterministic
bound depending only on B and (N9); there is no random Q multiplier.
Differences of \(\gamma\) and the clock gates cost \(C\eta_h\), multiplied
by the bounded normalized reference pulse (N49). The D-row difference
is at most \(E_j+C\eta_h\) by (N26). Finally (N36) bounds the sum of
the normalized defect derivatives in \(L^2\) by \(C_Bh_{\max}\). Discrete
Gronwall gives

\[
 {\|\max_{j\le k}|\chi^r_{j;p_0}-\chi^c_{j;p_0}|\|_2\over m_{p_0}}
    \le C_B\left\{\eta_h+h_{\max}
                                  +\sum_{j<k}h_jE_j\right\}.
 \tag{N50}
\]

The maximum on the left is controlled by the sum of the forcing
norms and a deterministic integrating factor. It does not require
an \(L^2\) bound on a supremum of the raw field discrepancy.

Take expected first-feature derivatives to obtain the same bound for
the \(\alpha\) row difference, after summing its source masses. For a
passive output its derivative outside chi differs in \(L^2\) by
\(C\eta_h\) and is bounded, so the statement remains uniform in u.
The upper source equations (N8) are identical in the two schemes;
subtracting them as in (N29), using the source density bounds and
discrete Gronwall, proves

\[
 E_k\le C_B\left\{\eta_h+h_{\max}
                                  +\sum_{j<k}h_jE_j\right\}.
 \tag{N51}
\]

Set \(B=B_{\rm cl}+1\). At any first potentially failed raw row, all previous
rows obey this cap. The defect estimate (N36) uses only those previous
raw Q fields. The current \(\alpha\) then obeys (N50), and the current
\(\beta\) obeys (N51), whose right side has no current \(\beta\). Gronwall
yields \(E_k\le C_Be^{C_BT}(\eta_h+h_{\max})\). Choose \(h_*\) positive and
small enough that this is at most 1/2 whenever \(h_{\max}\le h_*\).
Then the current raw row is at most \(B_{\rm cl}+1/2<B\), so induction cannot
fail. Both zero-readout initial programs have \(\beta=0\). This proves the reference raw coefficient bound with \(B_*=B_{\rm cl}+1\).
The weighted law-transport induction above now proves (N-cap) and its
uniform passive Gaussian-tail consequence through physical time \(T=40\).

The two bootstraps are separate: the first uses one fixed, independently
proved clock anchor to control reference raw Euler; the second uses
that raw anchor and weighted law transport to control all nearby finite
laws. Neither bootstrap takes a supremum of far-atom transport costs
or assumes the tails of the not-yet-controlled current query.

<!-- END CANONICAL SCIENTIFIC BODY -->

### Assembly note — outside the proposed scientific text

Assembler: `/root/p2_canonical_source`, 2026-09-11. This is a scoped author
assembly, and this assembler is ineligible for subsequent independent review.
The scientific body preserves the source route and every numbered source
estimate, with tags N1–N51, N27a, N29a, N29b and N30a. Changes are canonical
notation, explicit types and constant names, exact established references,
and removal of provenance and downstream theorem claims. The preceding
canonical model/raw bounds and Hilbert–Schmidt comparison are assumed to
carry labels (NE) and (NC). No established file was changed; no training,
sweep, Git write, or external retrieval was performed.

Read in full: AGENTS.md, RESEARCH_WORKFLOW.md, docs/NOTATION.md,
P2_SOURCE_BOOTSTRAP.md (1–1070), P2_THEOREM.md (1–320),
P2_REFERENCE_COMPARISON.md (1–233), and P2_DEPENDENCIES.md (1–3976).
Also read the complete invoked proof units in P1_DEPENDENCIES.md (386–1783):
finite dynamics §§1–4, special-data III.F.1–11, global-nonlinear A.1–A.4,
and B.1. A truncated first read in III.F.3 was repaired by reading that
whole unit again. The supervisor explicitly approved this source-only scope.

The unread scientific complement is P1_SECTION.md in full and
P1_DEPENDENCIES.md lines 1–385 and 1784–3238; only heading metadata and file
hashes were inspected there. The invoked C.4.1, C.4.5.1 and C.4.5.2 bodies
in that complement were checked to be exact substrings of the completely
read P2_DEPENDENCIES.md. The full C.4.2 proof, including the relevant common
carrier construction, was also read in P2_DEPENDENCIES.md. No review report,
other study, or Git history was read. The scientific body does not invoke
the unrelated C.4.6 tangent or finite-derivative proofs.

Required skills read: solve-math-rigorously/SKILL.md and
investigate-conjectures/SKILL.md, together with its evidence-ledger.md and
adversarial-audit.md references. The assembly check found no new gap in this
source component; that statement is not an independent correctness verdict
on this component or on the full nonlinear theorem. Formula-tag coverage,
balanced math delimiters/braces, and the absence of source-file references
were checked. Every source tag is present exactly once under its N-prefix.

| Input | SHA-256 at reading snapshot |
|---|---|
| AGENTS.md | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| RESEARCH_WORKFLOW.md | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| docs/NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| P2_SOURCE_BOOTSTRAP.md | `0cf6d54dbb85c6d7f4c5b737dbbe3c92956aef4680d7a88214bd2c34c5034efb` |
| P2_THEOREM.md | `849655c74c7552b874085401ffb4af22fc51d126702bf5bc61b689946cb0854a` |
| P2_REFERENCE_COMPARISON.md | `a6d229fd69be98df8bf41fa7fdde9dad55cfcae86799f2c268791dc3e3904c4d` |
| P2_DEPENDENCIES.md | `35375c597d65df70ca7fcec375357b0fdbca8d06bab3a873e690fda285d290e9` |
| P1_SECTION.md (metadata only) | `33c819282d83f7f4704cbd3a90e87b445d17ce161cc922c1ad786b5eb0d9de38` |
| P1_DEPENDENCIES.md | `ca696bc4ed14ea337028eb1e6ef9c7f729ed2a0153bc210de8e16dea18f5ee79` |

Scratch: `data/generated/trained_data_response/p2_20260911_02/canonical_source/`.
